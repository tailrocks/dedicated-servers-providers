# Break-even formulas, assumptions and sensitivity

[Study index](README.md) · [Decision tables](rent-vs-buy.md) · [Complete generated results](financial-results.md) · [Calculation source](calculate.py)

## Exactly what is calculated

Let `H` be complete hardware component cost under the documented purchasing assumptions, `E` monthly electricity, `I` incremental monthly internet, `M` an optional monthly repair allowance, `S` rental setup and `R` monthly rent. `A` is any one-time internet setup charge; all selected default plans currently have A = 0.

```text
BuyCost(m)  = H + A + m × (E + I + M)
RentCost(m) = S + m × R
Savings(m)  = RentCost(m) − BuyCost(m)

Break-even month = ceil((H + A − S) / (R − E − I − M))
```

The ceiling formula applies when H + A > S and the denominator is positive. If ongoing ownership cost is at least the rental cost and hardware starts more expensive, there is **no economic break-even** under those assumptions. If buying starts cheaper at month zero, the reported earliest crossing is zero; a higher subsequent ownership slope could reverse that advantage. No actual study row relies on that special case.

The four cases independently set E and I to zero or their selected charge. M is zero in all default rows. A rental server's included electricity and network are never added again. No office rent, building rent, workplace rent or rack-space fee appears in the code or financial inputs.

**“The hardware costs zero after X months” means that avoided rental expenditure has recovered the initial capital outlay.** The hardware was paid for, still consumes resources and can fail; it has not literally become free. There is no resale credit, income-tax deduction, financing cost or speculative appreciation in this simple cash model.

## Inputs and currency

- Exact hardware is enumerated in [procurement.json](data/procurement.json). `calculate.py` independently sums quantity × price and refuses stale economic totals, IDs, currency, RAM, node or mirror-capacity fields.
- [market-inputs.json](data/market-inputs.json) retains quote currencies, recurring amounts, setups, terms, source URLs and unresolved tax/stock. [economic-builds.json](data/economic-builds.json) makes the wall-power profile and performance-proxy assumptions explicit.
- The dated [ECB fixing](https://data-api.ecb.europa.eu/service/data/EXR/D.MYR+SGD+USD.EUR.SP00.A?startPeriod=2026-11-19&endPeriod=2026-11-20&format=csvdata) is 19 November: EUR 1 = SGD 1.4176 = MYR 4.5205 = USD 1.0992. The [separate IDR observation](https://data-api.ecb.europa.eu/service/data/EXR/D.IDR.EUR.SP00.A?startPeriod=2026-11-19&endPeriod=2026-11-19&format=csvdata) is IDR 20,073.1 per EUR. Amount X converts by multiplying by `1.4176 / units_X_per_EUR`.
- Decimal arithmetic retains unrounded cross-rates and power costs until presentation. Two-decimal display rounding can make printed component sums differ by a cent. The rental EUR tariff is not replaced with the provider's different native USD tariff.
- Singapore non-GST-registered Hetzner examples include the documented 9% charge; the Malaysia example uses the published before-customer-tax amount. This is not a determination of an individual buyer's business-tax liability. Arxan includes the 11% levy observed in its selected quote. Other sellers' unknown buyer taxes are explicitly left unknown, not asserted to be zero.
- Card FX spreads, import charges, shipping and payment fees are included only when actually quoted for the assumed transaction. Local fee-free payment/collection or eligible standard delivery is the component-subtotal basis. Unquoted cross-border transport and taxes make a landed total unavailable; no zero-cost import is implied. [Regional procurement](malaysia-hardware.md)

## Electricity and internet assumptions

The default is **730 hours per month**. Electricity uses complete estimated AC wall power, including a modeled allowance for the board, DIMMs, drives, fans and PSU loss. CPU TDP is not converted directly into a wall bill. Moderate power is an explicit midpoint between the idle/light and heavy budgets. These budgets are informed by externally published measurements and are not measurements of the proposed build. [Evidence and tariff details](electricity-costs.md)

The business internet case is SGD 105/month in Singapore or MYR 135.68/month in Malaysia, one line per site. Existing suitable connectivity is zero incremental cost. Residential rates, promotional first month and post-contract changes are modeled separately; permitted use matters, especially Time Home's household-only condition. A 10 Gbps advertised connection does not prove 10 Gbps to a remote registry. [Internet evidence](internet-costs.md)

The regular monthly model assumes rates persist. The Singapore business offer commits 36 months and the Malaysian offer 24. Six-month cash paid is not the same as the total obligation if cancelling a contracted line. After the quoted term, flat business renewals are scenarios because a binding future renewal tariff is unavailable. The optional WhizComms line uses the published month-one and after-term prices instead of extending its promotion indefinitely.

## Horizon and term handling

All default combinations report **6, 12, 18, 24, 36, 48 and 60 months**. [break-even.csv](data/break-even.csv) includes every cost, tax basis, CPU, memory/storage distinction, node count, scenario and earliest whole-month crossing. [cumulative-costs.csv](data/cumulative-costs.csv) stores the same seven horizons in long form.

The IP-Projects monthly invoice has a **12-month minimum**. At month six its paid-cash amount covers six invoices, but the buyer owes a longer commitment. The detailed CSV therefore also includes minimum-commitment rental amounts, calculated as `setup + max(horizon, minimum_term) × monthly`. Unknown minimum terms remain unknown, not assumed to be freely cancellable.

ServerWala's selected annual payment is **USD 3,618 upfront**, equivalent to USD 301.50 per service month. Its actual cash flow is a staircase. The [prepaid-rentals.csv](data/prepaid-rentals.csv) reports all four ownership scenarios and every horizon, both cash paid and consumed-service equivalent, the linear service-equivalent crossing, and the first actual cash crossing within 600 months. The latter can reverse before the next renewal and is not called a permanent payback. Refund terms and unchanged renewal prices are unverified. No prepaid rate is mislabelled a cancellable monthly invoice.

Crossings after 60 months answer the algebraic question under frozen inputs. They should not support a procurement decision that assumes a decade of unchanged rent, tariffs, software requirements and repair-free hardware. The `break_even_within_60_months` field distinguishes that limit. An explicit example with no crossing is a two-X3D pool plus electricity and a business line versus the cheaper 16-core PlusClouds AX102: ownership running costs already exceed that lower-class rental. It is also an unsuitable equal-performance substitution, which is why the CPU fields remain visible.

## Sensitivity that changes the decision

For **SG-WRX256-2 vs UHost**, default electricity plus a new business line gives S$167.55/month of ownership cost and a **114-month** algebraic crossing. Each row below changes just the named assumption, holding the other base inputs fixed.

| Assumption | First whole crossing | Interpretation |
|---|---:|---|
| Base moderate use and business line | 114 | Outside 60 months. |
| Hardware price −10% / +10% | 102 / 125 | Cheaper components help, but do not make this a short recovery. |
| SGD price of foreign rental −10% / +10% | 151 / 92 | Currency risk matters when the rental and running costs are close. |
| Electricity tariff −20% / +20% | 103 / 128 | Tariffs are future-variable; this is a sensitivity, not a forecast. |
| Idle/light 110 W / continuous heavy 440 W | 86 / 168 | Utilization changes both energy and the quantity of useful work; this table changes cost only. |
| Suitable existing internet | 60 | S$105/month avoided; this is the major site assumption. |
| Optional repair allowance, 3% of hardware/year | 160 | Explicit S$33.325/month reserve; no claim of a measured failure rate. |
| Additional 9% rental charge, if applicable | 93 | Illustrative unknown-charge sensitivity, not an assertion of UHost's tax treatment. |
| Already-paid rental setup treated as sunk | 115 | Correct incremental comparison when the old setup cannot be recovered. |

[All sensitivity rows](data/sensitivity.csv) also cover both Hetzner references, PlusClouds and DediJet for every owned build. No selected hardware subtotal is a guaranteed vendor bundle quote. The refurbished WRX80 case is kept separate and cannot be substituted into a new-memory recommendation without changing its procurement and warranty qualifications.

## Confidence and validation

Cash arithmetic has high reproducibility under the stated inputs. Future supplier prices, operating utilization, component failure, line renewals, currency and individual invoices do not. The normalized compiler index has lower predictive confidence for a complete CI queue and cannot make a 128 GB desktop a 256 GB EPYC equivalent.

The numerical tests cover exact and fractional crossings, a separate month-by-month search, no-crossing cases, independent utility switches, FX round trips, 730-hour electricity, tax application, term prepayment and promotion transitions. The independent review additionally uses rational arithmetic and its own month search on the generated matrix. Documentation validation checks local references and preservation of the existing rental catalog. None of these operations executes a hardware benchmark. [Review record](review-and-validation.md)

Signed-off-by: Alexey Zhokhov
