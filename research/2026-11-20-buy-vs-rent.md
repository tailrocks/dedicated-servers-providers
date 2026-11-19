# CI ownership and worldwide rental comparison — 20 November 2026

This extension compares buying non-ECC desktop/workstation hardware in Singapore or Malaysia with the rental research already in this repository. It adds a permanent [buy-versus-rent research folder](buy-vs-rent/README.md) for Rust/TypeScript builds and tests in Docker. Singapore is the preferred purchase/hosting market, with Malaysia second; worldwide rental locations remain available for comparison when geography is flexible.

**Analyzed coverage: the 119-offer snapshot at `c868b31`.** The canonical comparison has subsequently expanded; later additions and revised promotions are outside this ownership model until separately analyzed. The initial 104-offer snapshot and direct-payback follow-up are preserved chronologically below. The [latest integration](#follow-up-integrating-the-119-offer-main-branch) adds the 15 offers subsequently published on main.

## Source snapshot and repository scope

The rental input is the root README and dated logs at commit **07180f43068a8de01ae30c41a265ec16ef1f138b**, containing 104 rows across 38 alternative seller brands plus Hetzner. The seven-column table, numeric sort, row contents and existing historical logs are preserved. Importing an offer into the cost model does not reset its original checked date or establish new inventory.

New files:

- [Research index](buy-vs-rent/README.md).
- [Owned hardware and performance](buy-vs-rent/01-hardware-and-performance.md).
- [Singapore/Malaysia rental, colocation and local purchase](buy-vs-rent/02-rental-market.md).
- [12/24/36-month ownership and rental budgets](buy-vs-rent/03-rent-vs-buy-tco.md).
- [CI acceptance and procurement requirements](buy-vs-rent/04-validation-and-procurement.md).
- [All 104 existing rentals, capacity and commitment comparison](buy-vs-rent/05-repository-rental-comparison.md).

The root README links the extension, and METHODOLOGY distinguishes the new CI-specific requirement from the earlier general rental minimum.

## Findings that change the earlier ownership conclusion

**Worldwide rental coverage matters.** Comparing only against the regular Hetzner tariff overstates ownership's financial advantage. At the dated FX, UHost's 256 GB AX162-R known charges total S$10,368.91 over 36 months, BizoSiz's separate A1/A2 carts each S$13,096.55, and PlusClouds' A1 listing S$12,269.33. The corresponding Samsung-drive Singapore office budgets are S$15,466.87 for A2 and S$15,773.81 for A1. The rental figures precede unquoted taxes, IP/network and customer-specific charges; stock, term and operator qualifications remain visible.

**Capacity matching is stricter than the original raw-disk floor.** A1 requires at least 128 GB and two drives of at least 3.84 TB; A2 requires at least 256 GB and two drives of at least 1.92 TB. There are 32 A1-only, 32 A2-only, two dual-profile and 38 neither-profile rows. All 104 remain represented. CPU and storage performance are separate gates.

**The 5995WX is a screening candidate.** The +3% public multicore Clang observation is from an ASRock WRX80 system reporting 125.53 GB and Ubuntu 24.10, compared with an AX162 reporting 251.38 GB and Ubuntu 24.04.2. Frequency metadata does not establish sustained stock settings. The proposed ASUS/non-ECC BOM is a different machine, and the short fixed-task test does not certify actual CI within 3–5%.

**Lower-price storage options affect value.** The 20 November check added ADATA LEGEND 900 PRO 2 TB at S$479 and Lexar NM790 4 TB at S$859. Example parts estimates become S$8,069.40 for 5995WX/256 GB/two ADATA drives, S$6,399.20 for the Intel 64 GB-per-node pair with four ADATA drives, and S$8,829.40 for 5995WX/256 GB/two 4 TB Lexars. Manufacturer disclosures and actual CI I/O remain prerequisites; no equivalent latency is assumed from price or sequential bandwidth.

**Compatibility and operation are concrete procurement conditions.** The original ASUS board lists BIOS 1003 for 5995WX and qualifies the exact 32 GB Crucial revision CT32G4DFD832A.C16FE for eight sockets. Retail base SKUs do not guarantee the revision or quantity. The proposed eight-module 16 GB alternative remains unqualified. The build must also satisfy the board's power-cable, cooling, case and NVMe-layout instructions. Malaysia 4U hosting remains a cost floor until fit, intake airflow, peak current/power and facility approval are established.

## Current feed and price verification

The official [live price feed](https://www.hetzner.com/_resources/app/data/app/live_data_prices.json) and [availability feed](https://www.hetzner.com/_resources/app/data/app/live_data_upfront.json) were fetched successfully in this pass:

| Product | Monthly EUR / setup EUR | Separate USD tariff / setup | Availability result |
|---|---|---|---|
| ROBOT_1724, AX162-1 | 612.30 / 304 | 722.10 / 359 | FSN1, HEL1 |
| ROBOT_1725, AX162-2 | 842.30 / 419 | 992.10 / 494 | FSN1, HEL1 |
| LTD IDs 1727 and 1757 | Absent | Absent | Absent |

Prices exclude IPv4 and tax. The price feed also contains NBG1 entries, which do not override the narrower availability feed. The historical adjustment-document URL returns 404 on direct retrieval; it is no longer the sole support for regular prices. LTD is historical or existing-contract sensitivity only, not current purchasable supply.

The [UHost AX162-R configurator](https://uhost.online/en/dedicated/19) and [PlusClouds listings](https://plusclouds.com/servers) were reopened and retained the cited base configuration/rates. The independent BizoSiz fetch failed in this pass; its comparison uses the repository's already recorded 20 November matching-cart evidence rather than claiming a new checkout verification. No login, seller message, reservation or purchase was made.

The [dated ECB SGD observation](https://data-api.ecb.europa.eu/service/data/EXR/D.SGD.EUR.SP00.A?startPeriod=2026-11-19&endPeriod=2026-11-19&format=csvdata) and [MYR observation](https://data-api.ecb.europa.eu/service/data/EXR/D.MYR.EUR.SP00.A?startPeriod=2026-11-19&endPeriod=2026-11-19&format=csvdata) were fetched as CSV and confirm **1.4176 SGD/EUR** and **4.5205 MYR/EUR**. The extension preserves the repository's 19 November USD and BRL basis. These are fixed comparison rates, not future settlement forecasts.

## Calculation and evidence rules

Of 104 rental rows, **78 state a setup amount**, **23 omit setup from the selected quote**, and **three lack enough terms for a total**. Horizon calculations preserve those distinctions. A missing setup line is marked unknown, not changed to zero. Twenty-four- and thirty-six-month prepaid variants retain the whole commitment needed for the selected horizon; later renewals at the same price are explicit assumptions.

The office model separates retail parts, UPS/assembly allowances, assumed average wall power, cooling, connectivity and maintenance reserve. The 350 W workstation and 450 W combined desktop-pair figures are assumptions, not measurements. A 9% Singapore-billing rental calculation is a scenario, not a determination of the customer's tax position. Malaysia hosting of Singapore-sourced parts is not described as a locally sourced Malaysian workstation quote. A separate Malaysia-local Intel pair, with 64 GB per host and RM24,008 parts, has illustrative office budgets of S$10,405.90 / S$12,083.05 / S$13,760.19 over 12/24/36 months; its split memory and unmeasured throughput remain explicit.

The CI acceptance procedure requires both critical-job latency and sustained queue throughput by default: 1.03× duration / 0.97× rate for 3%, or 1.05× / 0.95× for 5%. Uncertainty crossing a threshold is unresolved. No actual user repository benchmark or candidate wall-power measurement has been performed.

## Research and review

GPT-6.2 Astra at max reasoning performed the hardware refresh and exhaustive rental comparison. GPT-6.2 Sol at max reviewed benchmark claims, compatibility, calculations, capacity matching, tax/fee treatment and repository integration. Validation covers the 104-row mapping, arithmetic, source/relative links and preservation of the existing table. No application code or CI workflow was changed.

## Follow-up: direct payback and independent utility charges

The user's follow-up explicitly authorizes `Signed-off-by: Alexey Zhokhov <alexey@zhokhov.com>` on commits and requires office rent to be excluded from every scenario. That standing sign-off instruction is recorded in [AGENTS.md](../AGENTS.md); the previously unsigned PR commit was replaced with an otherwise identical signed commit. No base-branch history was rewritten.

The new [direct-payback report](buy-vs-rent/06-direct-payback.md) and [104-offer break-even appendix](buy-vs-rent/07-all-rentals-break-even.md) make electricity and internet independent choices: neither, electricity only, internet only, or both. The direct purchase price contains the hardware BOM only. UPS, assembly/delivery, repair reserves, additional room cooling, labour, payment/FX charges and financing are separately identified optional or unquoted items. Office, room, floor-space and premises rent are never added, including in sensitivities. Existing expanded-budget figures remain labeled and reconciled rather than silently overwritten.

The primary Singapore workstation electricity input is now **S$79.6138/month**, from assumed 350 W average wall consumption, 730 hours/month and the rechecked [SP Q4 2026 tariff](https://www.spgroup.com.sg/our-services/utilities/tariff-information) of S$0.3116/kWh including GST. **S$19.90345/month additional cooling** is separate and optional. **S$50/month incremental internet** remains a user-replaceable assumption, independently includable, not an ISP quote. The [November Malaysian AFA](https://www.st.gov.my/AFA) was rechecked at RM0.0360/kWh; the documented existing-meter commercial rate and dated FX remain unchanged. Electricity is not measured on candidate hardware.

For the S$8,609.40 A2 workstation, UHost's USD220/month quote is **30.34 months of recurring rent** before setup and utilities. Crediting only the avoidable setup on a new rental gives **29.80 / 41.42 / 36.17 / 54.86 months** across the four Singapore scenarios, or whole months **30 / 42 / 37 / 55**. With both utilities, direct three-year ownership is **S$13,275.50**; the previous **S$15,466.87** expanded budget also included S$716.52 cooling, S$700 UPS/assembly and S$774.85 reserve. Neither includes office rent. Previously paid setup is sunk and cannot shorten an existing-lease comparison; savings begin when that rental can actually be stopped.

All 104 rental IDs and source URLs remain represented, with **68 capacity-profile comparisons across 66 distinct matching offers**, plus 38 nonmatches. Unknown setup remains `N/Q` for setup-adjusted payback. Prepaid service-month equivalents, actual term payments and minimum commitments are distinguished; a temporary cash crossing is not called permanent payback. Whole-month results use unrounded values: BizoSiz A1 with both utilities is 38.0006, so the crossing is month 39, not 38.

GPT-6.2 Astra max computed the utility and all-rental extensions; GPT-6.2 Sol max independently checked the formulas, arithmetic, payment timing, source mappings and repository integration. No purchase, vendor contact, actual CI replay or wall-power measurement was performed.

## Follow-up: integrating the 119-offer main branch

On the next repository check, main had advanced to **c868b31019be4c449bb62cbfa9786d44ac663db4**, adding **15 offers from nine sellers** and four evidence logs. The original 104 rows were unchanged. The research branch integrates that upstream work without replacing its table or logs. The ownership extension now covers **119 rows across 47 alternative seller brands plus Hetzner**.

The new [08-latest-rental-comparisons.md](buy-vs-rent/08-latest-rental-comparisons.md) preserves all 15 additions as stable IDs **N01–N15**, including hardware, capacity matching, native price/setup/term, 12/24/36-month known charges and the same four independent electricity/internet payback scenarios. Files 05 and 07 retain their initial IDs 001–104 and explicitly state their snapshot scope. Their combination covers every current canonical row. No office or premises rent is introduced; room cooling remains separately optional.

The additions consist of **three A1-only, seven A2-only and five nonmatching offers**. Current totals are **35 A1-only, 39 A2-only, two matching both and 43 matching neither**: **76 distinct matches and 78 profile comparisons**. Across all 119 offers, 87 state a setup fee and 32 leave it unresolved. Unknown fees are not changed to zero. The five capacity failures remain visible, including XDLHOST's roughly 1 TB mirror; its advertised rental-versus-Hetzner month-14 setup recovery is not a hardware-purchase payback result.

The dated GBP observation was fetched directly from the [ECB CSV](https://data-api.ecb.europa.eu/service/data/EXR/D.GBP.EUR.SP00.A?startPeriod=2026-11-19&endPeriod=2026-11-19&format=csvdata), confirming **EUR1 = GBP0.83581**. GBP-to-SGD calculations use the native quote divided by 0.83581 and multiplied by 1.4176 without an intermediate rounded USD amount.

The [Progressive Robot catalogue](https://account.progressiverobot.com/index.php?rp=/store/dedicated-servers) was reopened and retains GBP221/month plus GBP88 setup for each exact A1/A2 listing. That gives **S$13,643.26** in 36-month known charges for each. With direct Singapore electricity plus internet, setup-adjusted purchase crossings are **35.65 months for A1** and **34.50 for A2**, or whole months **36** and **35**. Deployment country/city, final tax, minimum term and physical allocation remain unresolved. These two offers bring the number below the optional expanded ownership budgets to **nine**, while the number below direct hardware-plus-both-utilities remains **six**, and below hardware alone remains **zero**, considering the ranked capacity matches with stated setup fees.

The [Faciotech configurator](https://faciotech.com/dedicated-servers.php#configurator) was reopened and retains the USD389/month / zero-setup Enterprise Metal quote, with engineer confirmation before billing. Nindohost's USD234 A2 remains quote-only with unknown setup; this integration uses the upstream evidence after a fresh parameterized web fetch failed. Its 36-month rent-only subtotal of **S$10,864.14** is not a complete invoice. UHost A2 and PlusClouds A1 remain the lowest stated-setup 36-month totals in the ranked inventory before unquoted charges.

The update preserves payment-specific watchlists separately. AvalinHost's EUR pricing basis is paid in Iranian toman, with international payment eligibility unverified; Gengbiz's Malaysian-market page does not establish a qualifying Malaysian physical deployment. Neither is silently promoted to a generally payable or locally allocated replacement. AmazingRDP's annual quote is modeled as a real USD5,400 upfront term invoice, with cash crossover distinguished from its monthly equivalent.

GPT-6.2 Astra max performed the delta comparison and decision-impact review, followed by GPT-6.2 Sol max's independent review of new calculations, capacity counts, fee/currency handling, prepaid behavior and cross-file integration. The current canonical server table is preserved byte-for-byte from `c868b31`; the authored integration commit includes the standing Alexey Zhokhov sign-off.

## Publication follow-up: preserve the analyzed snapshot

On 20 November 2026, the user explicitly instructed that completed work be committed, pushed and any created or touched PRs merged. PR #1 was reviewed against main `175399c50339f5d8192c4a5821e74db4d5fbd4f6`, whose canonical comparison had grown to 141 rows. The ownership extension's arithmetic still analyzes the earlier 119-offer snapshot. Its current-facing summaries now state that scope explicitly, while historical sections, all original amounts, source IDs and the 104/15-row analyses remain intact. No claim is made that the later 22 rows or refreshed PowerDedi promotion have been recalculated in the ownership model.

The prospective merge preserves the full 141-row canonical table and all six files from the newer supplier expansion. Changes in this follow-up concern snapshot labeling and integration only. The existing DCO check passed on the prior PR head; the new publication commit carries the standing sign-off and must pass the same check before merging. No new hardware-performance or cost-model conclusions are introduced.
