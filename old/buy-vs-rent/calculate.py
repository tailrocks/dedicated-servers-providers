#!/usr/bin/env python3
"""Reproduce cash-cost comparisons; this program runs no hardware benchmarks.

Signed-off-by: Alexey Zhokhov <alexey@zhokhov.com>
"""

import argparse
import csv
from decimal import Decimal, ROUND_CEILING, ROUND_HALF_UP
import io
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ZERO = Decimal("0")
ONE = Decimal("1")
SCENARIOS = {
    "hardware_only": (False, False),
    "hardware_electricity": (True, False),
    "hardware_internet": (False, True),
    "hardware_both": (True, True),
}
HORIZONS = (6, 12, 18, 24, 36, 48, 60)


def dec(value):
    return value if isinstance(value, Decimal) else Decimal(str(value))


def money(value):
    return format(dec(value).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP), "f")


def convert(amount, source_currency, target_currency, units_per_eur):
    return dec(amount) * dec(units_per_eur[target_currency]) / dec(units_per_eur[source_currency])


def electricity(power_watts, hours, tariff):
    return dec(power_watts) / Decimal("1000") * dec(hours) * dec(tariff)


def buy_cost(hardware, month, monthly_electricity=ZERO, monthly_internet=ZERO,
             monthly_maintenance=ZERO, internet_setup=ZERO):
    return (dec(hardware) + dec(internet_setup) + dec(month) *
            (dec(monthly_electricity) + dec(monthly_internet) + dec(monthly_maintenance)))


def rent_cost(setup, monthly, month):
    return dec(setup) + dec(monthly) * dec(month)


def break_even(hardware, setup, rental_monthly, owner_monthly):
    """Earliest nonnegative whole month satisfying buy <= rent for constant rates.

    Returns None if there is no crossing. If buying is already cheaper at month
    zero, returns zero; callers must not imply that it stays cheaper when its
    running cost exceeds rent. Current study rows do not have that edge case.
    """
    numerator = dec(hardware) - dec(setup)
    margin = dec(rental_monthly) - dec(owner_monthly)
    if numerator <= ZERO:
        return 0
    if margin <= ZERO:
        return None
    return int((numerator / margin).to_integral_value(rounding=ROUND_CEILING))


def prepaid_rent_cost(setup, monthly_equivalent, month, period_months):
    """Actual paid cash for complete periods bought before each covered month.

    At m=0 only setup is counted. For m=1..period, the first term is paid in
    full. This is intentionally separate from the user's linear monthly model.
    """
    if month == 0:
        return dec(setup)
    periods = (month + period_months - 1) // period_months
    return dec(setup) + periods * period_months * dec(monthly_equivalent)


def internet_cost(plan, month):
    """Published first-month and post-term rates when supplied, otherwise flat.

    A flat post-contract extrapolation is a scenario, not a verified renewal.
    """
    if month == 0:
        return dec(plan.get("setup", 0))
    term = plan.get("term_months") or month
    initial_months = min(month, term)
    total = dec(plan.get("setup", 0)) + dec(plan["monthly"]) * initial_months
    if "first_month" in plan:
        total += dec(plan["first_month"]) - dec(plan["monthly"])
    if month > term:
        total += (month - term) * dec(plan.get("after_term_monthly", plan["monthly"]))
    return total


def csv_text(rows):
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=list(rows[0]), lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue()


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"), parse_float=Decimal)


def verify_procurement(builds, procurement):
    """Fail on stale copied totals or an incomplete BOM-to-finance mapping."""
    source = {b["id"]: b for b in procurement["owned_builds"]}
    if set(source) != {b["id"] for b in builds["builds"]}:
        raise ValueError("Procurement and economic build IDs differ")
    for build in builds["builds"]:
        parts = source[build["id"]]
        subtotal = sum((dec(p["unit_price"]) * p["quantity"] for p in parts["bom"]), ZERO)
        if subtotal != dec(parts["parts_total"]) or subtotal != dec(build["purchase_cost"]):
            raise ValueError(f"BOM subtotal mismatch: {build['id']}")
        for field in ("currency", "nodes", "ram_gb_per_node", "mirror_tb_per_node"):
            if parts[field] != build[field]:
                raise ValueError(f"BOM field mismatch: {build['id']} {field}")


def benchmark_ratio(build):
    """A named published benchmark proxy only; never a synthetic CI score."""
    proxy = build.get("compiler_proxy")
    if not proxy:
        return None
    return (dec(proxy["candidate_work_rate"]) / dec(proxy["baseline_work_rate"])
            * dec(proxy.get("node_count", 1)) * dec(proxy.get("pool_efficiency", 1)))


def rental_terms(rental, market, rates):
    # No unquoted third-party tax is silently called a tax-inclusive invoice.
    tax = (Decimal("0.09") if market == "SG" and rental["id"] in ("ax162_1", "ax162_2")
           else dec(rental.get("comparison_tax_percent", 0)) / Decimal("100"))
    multiplier = ONE + tax
    monthly = convert(rental["monthly"], rental["currency"], "SGD", rates) * multiplier
    setup = convert(rental["setup"], rental["currency"], "SGD", rates) * multiplier
    basis = ("SG non-GST-registered buyer: 9% included"
             if market == "SG" and rental["id"] in ("ax162_1", "ax162_2")
             else rental["native_tax_basis"] + (f"; observed {money(tax * 100)}% included" if tax else ""))
    return monthly, setup, basis


def outputs(market, builds):
    rates = market["fx"]["units_per_eur"]
    hours = market["average_hours_per_month"]
    plans = {plan["id"]: plan for plan in market["internet_plans"]}
    monthly_rentals = [r for r in market["rentals"] if r["billing_period_months"] == 1]
    be_rows, tco_rows, value_rows, rental_value_rows, sensitivity_rows, annual_rows = [], [], [], [], [], []
    summary = [
        "# Reproducible financial results", "",
        "[Study index](README.md) · [Interpretation](rent-vs-buy.md) · [Assumptions](break-even-analysis.md)", "",
        "Generated from `data/economic-builds.json` and `data/market-inputs.json` by `calculate.py`.", "",
        "All figures are SGD; no premises/rack rent. Moderate estimated wall power is the default. "
        "Electricity and a separately purchased business internet line are independently selectable. "
        "The existing-line case is the electricity-only column. See the CSVs for every requested horizon.", "",
        "Hetzner SG rows include the documented 9% non-GST-registered buyer scenario and IPv4. "
        "Other sellers retain their stated/unknown tax basis: known-charge comparisons are not "
        "tax-normalized final invoices. Crossings against different RAM, disks, CPUs or node counts "
        "are cash comparisons, not performance-equivalence certificates.", "",
    ]
    for build in builds["builds"]:
        region = build["market"]
        hardware = convert(build["purchase_cost"], build["currency"], "SGD", rates)
        tariff = market["tariffs"][region]
        profile = market["power_w"][build["power_profile"]]
        e = convert(electricity(profile["moderate"], hours, tariff["per_kwh"]), tariff["currency"], "SGD", rates)
        business = plans["sg_business" if region == "SG" else "my_business"]
        internet = convert(business["monthly"], business["currency"], "SGD", rates)
        internet_setup = convert(business["setup"], business["currency"], "SGD", rates)
        summary.extend([
            f"## {build['id']} — {build['name']}", "",
            f"Hardware **S${money(hardware)}**; modeled moderate electricity **S${money(e)}/month**; "
            f"separate business internet **S${money(internet)}/month**; maintenance **S$0**. "
            f"Procurement basis: {build['cost_basis']}", "",
            "| Rental | Monthly / setup S$ | Hardware | + electricity | + internet | + both |",
            "|---|---:|---:|---:|---:|---:|",
        ])
        for rental in monthly_rentals:
            rent, setup, tax_basis = rental_terms(rental, region, rates)
            result = {}
            for name, (count_e, count_i) in SCENARIOS.items():
                elec = e if count_e else ZERO
                net = internet if count_i else ZERO
                net_setup = internet_setup if count_i else ZERO
                month = break_even(hardware + net_setup, setup, rent, elec + net)
                result[name] = "Never" if month is None else str(month)
                row = {
                    "build_id": build["id"], "owned_build": build["name"], "market": region,
                    "nodes": build["nodes"], "ram_gb_per_node": build["ram_gb_per_node"],
                    "relative_performance": build["performance_note"],
                    "rental_id": rental["id"], "rented_server": rental["name"],
                    "rental_cpu": rental["cpu"], "rental_ram_gb": rental["ram_gb"],
                    "rental_storage": rental["storage"], "rental_tax_basis": tax_basis,
                    "rental_minimum_months": rental["term_months"],
                    "rental_nodes": rental.get("nodes", 1),
                    "scenario": name, "hardware_sgd": money(hardware),
                    "rental_monthly_sgd": money(rent), "rental_setup_sgd": money(setup),
                    "electricity_monthly_sgd": money(elec), "internet_monthly_sgd": money(net),
                    "internet_setup_sgd": money(net_setup), "maintenance_monthly_sgd": "0.00",
                    "break_even_month": "none" if month is None else month,
                    "break_even_within_60_months": month is not None and month <= 60,
                }
                for horizon in HORIZONS:
                    owned = buy_cost(hardware, horizon, elec, net, internet_setup=net_setup)
                    rented = rent_cost(setup, rent, horizon)
                    row[f"buy_{horizon}m_sgd"] = money(owned)
                    row[f"rent_{horizon}m_sgd"] = money(rented)
                    row[f"rent_minimum_commitment_{horizon}m_sgd"] = money(
                        rent_cost(setup, rent, max(horizon, rental.get("term_months") or 1)))
                    row[f"saving_{horizon}m_sgd"] = money(rented - owned)
                    tco_rows.append({
                        "build_id": build["id"], "rental_id": rental["id"], "scenario": name,
                        "month": horizon, "buy_sgd": money(owned), "rent_sgd": money(rented),
                        "saving_sgd": money(rented - owned),
                    })
                be_rows.append(row)
            summary.append(
                f"| {rental['name']} | {money(rent)} / {money(setup)} | "
                + " | ".join(result[name] for name in SCENARIOS) + " |"
            )
            if rental["id"] in ("ax162_1", "ax162_2", "uhost_r", "plusclouds_s", "dedijet_sg"):
                variations = [
                    ("base_moderate_business", ONE, ONE, ONE, profile["moderate"], internet, ZERO),
                    ("hardware_minus_10pct", Decimal("0.90"), ONE, ONE, profile["moderate"], internet, ZERO),
                    ("hardware_plus_10pct", Decimal("1.10"), ONE, ONE, profile["moderate"], internet, ZERO),
                    ("rental_fx_minus_10pct", ONE, Decimal("0.90"), ONE, profile["moderate"], internet, ZERO),
                    ("rental_fx_plus_10pct", ONE, Decimal("1.10"), ONE, profile["moderate"], internet, ZERO),
                    ("electricity_minus_20pct", ONE, ONE, Decimal("0.80"), profile["moderate"], internet, ZERO),
                    ("electricity_plus_20pct", ONE, ONE, Decimal("1.20"), profile["moderate"], internet, ZERO),
                    ("idle_light", ONE, ONE, ONE, profile["idle"], internet, ZERO),
                    ("heavy_continuous", ONE, ONE, ONE, profile["heavy"], internet, ZERO),
                    ("existing_internet", ONE, ONE, ONE, profile["moderate"], ZERO, ZERO),
                    ("optional_3pct_annual_repair_allowance", ONE, ONE, ONE, profile["moderate"], internet,
                     hardware * Decimal("0.03") / Decimal("12")),
                    ("extra_9pct_rental_charge_if_applicable", ONE, Decimal("1.09"), ONE,
                     profile["moderate"], internet, ZERO),
                    ("existing_lease_setup_sunk", ONE, ONE, ONE, profile["moderate"], internet, ZERO),
                ]
                for label, capex_mult, rent_mult, tariff_mult, watts, net, maintenance in variations:
                    elec = convert(electricity(watts, hours, tariff["per_kwh"]), tariff["currency"], "SGD", rates) * tariff_mult
                    rent_setup = ZERO if label == "existing_lease_setup_sunk" else setup * rent_mult
                    month = break_even(hardware * capex_mult, rent_setup, rent * rent_mult, elec + net + maintenance)
                    sensitivity_rows.append({
                        "build_id": build["id"], "rental_id": rental["id"], "variation": label,
                        "hardware_sgd": money(hardware * capex_mult), "electricity_sgd": money(elec),
                        "internet_sgd": money(net), "maintenance_allowance_sgd": money(maintenance),
                        "rental_monthly_sgd": money(rent * rent_mult), "rental_setup_sgd": money(rent_setup),
                        "break_even_month": "none" if month is None else month,
                        "saving_36m_sgd": money(rent_cost(rent_setup, rent * rent_mult, 36) -
                            buy_cost(hardware * capex_mult, 36, elec, net, maintenance)),
                    })
            # Published prepayment is modeled separately; it does not contaminate
            # the linear monthly break-even matrix above.
        for rental in market["rentals"]:
            if rental["billing_period_months"] == 1:
                continue
            rent, setup, _ = rental_terms(rental, region, rates)
            for horizon in HORIZONS:
                annual_rows.extend({
                    "build_id": build["id"], "rental_id": rental["id"], "month": horizon,
                    "scenario": scenario,
                    "rent_cash_paid_sgd": money(prepaid_rent_cost(setup, rent, horizon, rental["billing_period_months"])),
                    "rent_service_equivalent_sgd": money(rent_cost(setup, rent, horizon)),
                    "buy_sgd": money(buy_cost(hardware, horizon, e if count_e else ZERO,
                                               internet if count_i else ZERO,
                                               internet_setup=internet_setup if count_i else ZERO)),
                    "service_equivalent_break_even_month": break_even(
                        hardware + (internet_setup if count_i else ZERO), setup, rent,
                        (e if count_e else ZERO) + (internet if count_i else ZERO)),
                    "first_cash_crossing_month_within_600": next((m for m in range(601)
                        if buy_cost(hardware, m, e if count_e else ZERO, internet if count_i else ZERO,
                                    internet_setup=internet_setup if count_i else ZERO)
                        <= prepaid_rent_cost(setup, rent, m, rental["billing_period_months"])), ">600 or never"),
                    "note": "Renewals assumed at same price; first cash crossing can reverse between renewal dates.",
                } for scenario, (count_e, count_i) in SCENARIOS.items())
        ratio = benchmark_ratio(build)
        if ratio is not None:
            for scenario, (count_e, count_i) in SCENARIOS.items():
                for horizon in HORIZONS:
                    owned = buy_cost(hardware, horizon, e if count_e else ZERO,
                                     internet if count_i else ZERO, internet_setup=internet_setup if count_i else ZERO)
                    value_rows.append({
                        "build_id": build["id"], "scenario": scenario, "month": horizon,
                        "benchmark": build["compiler_proxy"]["name"],
                        "candidate_work_rate": build["compiler_proxy"]["candidate_work_rate"],
                        "epyc_work_rate": build["compiler_proxy"]["baseline_work_rate"],
                        "node_count": build["compiler_proxy"].get("node_count", 1),
                        "assumed_pool_efficiency": build["compiler_proxy"].get("pool_efficiency", 1),
                        "normalized_proxy_percent": money(100 * ratio),
                        "cumulative_cost_sgd": money(owned),
                        "sgd_per_normalized_proxy_point": money(owned / (100 * ratio)),
                        "qualification": build["compiler_proxy"].get("qualification", "Published compiler proxy only; not measured CI jobs/hour or the quoted BOM."),
                    })
        # Actual published residential promotion is a separate internet option.
        residential = plans["sg_residential" if region == "SG" else "my_residential"]
        summary.extend(["", "| Horizon | Hardware | + electricity | + business internet | + both | + electricity and residential internet* |",
                        "|---|---:|---:|---:|---:|---:|"])
        for horizon in HORIZONS:
            resident = convert(internet_cost(residential, horizon), residential["currency"], "SGD", rates)
            vals = [buy_cost(hardware, horizon, e if ce else ZERO, internet if ci else ZERO,
                             internet_setup=internet_setup if ci else ZERO) for ce, ci in SCENARIOS.values()]
            vals.append(buy_cost(hardware, horizon, e) + resident)
            summary.append(f"| {horizon} months | " + " | ".join(money(v) for v in vals) + " |")
        summary.extend(["", "*Residential service requires eligibility and suitable permitted use; router/installation exceptions "
                        "and renewal assumptions are in [internet costs](internet-costs.md). "
                        "The business subscription's minimum contract remains payable if service is cancelled early.", ""])
    # Same-CPU rental value is an explicitly assumed baseline-class proxy. Other
    # processors are excluded unless a directly comparable work rate is supplied.
    for region in ("SG", "MY"):
        for rental in monthly_rentals:
            if rental["cpu"].removeprefix("AMD ") != "EPYC 9454P":
                continue
            rent, setup, tax_basis = rental_terms(rental, region, rates)
            for horizon in HORIZONS:
                cost = rent_cost(setup, rent, horizon)
                rental_value_rows.append({
                    "rental_id": rental["id"], "customer_market": region, "month": horizon,
                    "benchmark": "Geekbench 6.4 Linux AVX2 Clang reference class",
                    "normalized_proxy_percent": "100.00", "cumulative_cost_sgd": money(cost),
                    "sgd_per_normalized_proxy_point": money(cost / Decimal("100")),
                    "tax_basis": tax_basis,
                    "qualification": "Assumes the same EPYC CPU baseline class; vendor BOM, memory population and sustained CI rate are unmeasured.",
                })
    summary.extend(["## Machine-readable outputs", "",
                    "- [Every build, monthly rental, scenario and horizon](data/break-even.csv)",
                    "- [Cumulative cash-cost rows](data/cumulative-costs.csv)",
                    "- [Named compiler-proxy value, not a CI score](data/performance-value.csv)",
                    "- [Same-CPU rental proxy value](data/rental-performance-value.csv)",
                    "- [Sensitivity scenarios](data/sensitivity.csv)",
                    "- [Annual prepayment versus service-equivalent expense](data/prepaid-rentals.csv)", "",
                    "Signed-off-by: Alexey Zhokhov", ""])
    return {
        "data/break-even.csv": csv_text(be_rows),
        "data/cumulative-costs.csv": csv_text(tco_rows),
        "data/performance-value.csv": csv_text(value_rows),
        "data/rental-performance-value.csv": csv_text(rental_value_rows),
        "data/sensitivity.csv": csv_text(sensitivity_rows),
        "data/prepaid-rentals.csv": csv_text(annual_rows),
        "financial-results.md": "\n".join(summary),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if committed outputs differ from recalculation")
    args = parser.parse_args()
    market = load_json(HERE / "data/market-inputs.json")
    builds = load_json(HERE / "data/economic-builds.json")
    verify_procurement(builds, load_json(HERE / "data/procurement.json"))
    generated = outputs(market, builds)
    differences = []
    for name, content in generated.items():
        path = HERE / name
        if args.check:
            if not path.exists() or path.read_bytes() != content.encode("utf-8"):
                differences.append(name)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content.encode("utf-8"))
    if differences:
        raise SystemExit("Recalculation differs: " + ", ".join(differences))
    print(f"{'Verified' if args.check else 'Generated'} {len(generated)} financial outputs; no hardware tests performed.")


if __name__ == "__main__":
    main()
