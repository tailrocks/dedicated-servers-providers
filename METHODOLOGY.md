# Comparison methodology

The current offers live in the seven-column table in [README.md](README.md). Dated files under `research/` preserve evidence, rejected offers, older prices and unresolved questions. A historical entry is not a current purchase recommendation.

## Requirements

- A whole physical dedicated / bare-metal server. VPS, VDS, dedicated-vCPU and shared-hosting products do not qualify.
- CPU performance at least in the AMD EPYC 9454P class.
- At least 128 GB of installed RAM.
- At least 2 TB of installed SSD capacity, preferably NVMe. HDD capacity does not satisfy this floor.
- A lower recurring price than the reference server, with setup fees and minimum commitments shown separately. A lower monthly rate does not necessarily mean a lower first-year cost.

The original general rental comparison did not specify a location, operating system, network allowance, workload or minimum physical core count. Those original rental-table criteria remain separate from the [CI ownership extension](research/buy-vs-rent/README.md), which explicitly specifies Rust/TypeScript testing in Docker, Singapore-first/Malaysia-second purchasing, non-ECC owned memory and a 3–5% performance tolerance. Do not silently relabel the general table's rows as measured CI equivalents. Differences that materially affect a purchase are recorded in Notes.

## Reference configuration

The regular Hetzner AX162-1 is an EPYC 9454P (48 cores / 96 threads), 128 GB DDR5 ECC registered RAM and two 3.84 TB datacenter NVMe SSDs. On 2026-11-19 the official price list and live price feed showed EUR 612.30/month plus EUR 304 setup, excluding VAT and IPv4; the same live tariffs were rechecked on 2026-11-20 Asia/Ho_Chi_Minh. The provider's separate USD tariff was USD 722.10/month plus USD 359 setup. The EUR first-year subtotal is EUR 7,651.60 before IPv4 and tax.

Sources:

- [AX162 configurator](https://www.hetzner.com/dedicated-rootserver/ax162/configurator/)
- [AX hardware matrix](https://www.hetzner.com/dedicated-rootserver/matrix-ax/)
- [Historical official price adjustment table](https://docs.hetzner.com/general/infrastructure-and-availability/price-adjustment/) — still indexed with the same amounts, but direct retrieval returned HTTP 404 in the final 20 November check; the live feed below independently confirms the current prices.
- [Public live price feed](https://www.hetzner.com/_resources/app/data/app/live_data_prices.json), product `ROBOT_1724`
- [Public availability feed](https://www.hetzner.com/_resources/app/data/app/live_data_upfront.json)

Limited-stock / legacy AX162 prices are separate offers. An absent limited-stock SKU is not evidence that a regular server can be bought at the limited-stock price.

## CPU qualification

An exact 9454P is an exact CPU-model match, subject to contradictory product-specific details. For example, the Singapore listings reviewed on 20 November explicitly say 48 cores and 48 threads instead of the model's 96 threads; do not assume an enabled SMT setting or silently repair the listing. Those offers remain conditional. A newer or different CPU is evaluated with primary specifications and benchmarks; core count, model number or vendor marketing alone is insufficient. Record whether performance is directly benchmark-supported or inferred from a newer architecture and comparable specifications.

PassMark observations used in the 2026-11-19 research:

| CPU | Cores / threads | CPU Mark | Single-thread score | Interpretation |
|---|---|---:|---:|---|
| AMD EPYC 9454P | 48 / 96 | 94,689 | 2,988 | Reference |
| AMD EPYC 9355P | 32 / 64 | 96,603 | 3,747 | About +2% aggregate and +25% single-thread, but lower SPEC integer throughput; conditional, excluded from the strict main table |
| AMD EPYC 9455P | 48 / 96 | 116,817 | 3,746 | Above reference in both scores; do not silently assign this exact result to the non-P 9455 |
| AMD Ryzen Threadripper 9980X | 64 / 128 | 143,623 | 4,556 | About +52% in both CPU scores; different memory platform |
| AMD Ryzen Threadripper PRO 9985WX | 64 / 128 | 150,121 | 4,486 | Above reference in both scores; quoted memory population remains a limitation |
| AMD EPYC 9554P | 64 / 128 | 104,920 | 2,737 | More aggregate throughput but lower single-thread; not an unconditional match |

Primary benchmark sources: [9355P vs 9454P](https://www.cpubenchmark.net/compare/6449vs5596/AMD-EPYC-9355P-vs-AMD-EPYC-9454P), [9455P vs 9454P](https://www.cpubenchmark.net/compare/6461vs5596/AMD-EPYC-9455P-vs-AMD-EPYC-9454P), [same-day high-end CPU chart for 9980X and 9985WX](https://www.cpubenchmark.net/high_end_cpus.html), [same-day single-thread chart](https://www.cpubenchmark.net/singleThread.html), [9554P vs 9454P](https://www.cpubenchmark.net/compare/5596vs5599/AMD-EPYC-9454P-vs-AMD-EPYC-9554P). Different cached individual-CPU pages can reflect a different sample date.

These are submitted-system averages, not measurements of a particular rental server. RAM channel population, power limits, NUMA, software and storage may change application performance. A candidate with benchmark evidence still needs workload validation where the difference matters.

### Cross-checks beyond PassMark

The [Lenovo SR635 V3 result for the 9355P](https://www.spec.org/cpu2017/results/res2024q4/cpu2017-20241104-45295.html) reports SPECrate2017_int_base of 478, compared with [525 for the 9454P](https://www.spec.org/cpu2017/results/res2023q1/cpu2017-20230227-34459.html): about **9.0% lower integer throughput**. Both used one CPU and twelve 32GB DIMMs. Floating-point throughput went the other way: [644 for the 9355P](https://www.spec.org/cpu2017/results/res2024q4/cpu2017-20241104-45293.html) versus [544 for the 9454P](https://spec.org/cpu2017/results/res2023q1/cpu2017-20230227-34461.html), about **18.4% higher**. Software, firmware and memory speed differed. These are evidence of workload dependence, not tests of the rented servers. A slight PassMark advantage is insufficient to admit this 32-core chip as an unconditional replacement.

The non-P **EPYC 9455** has its own evidence. A [single-socket Lenovo SR635 V3 result](https://www.spec.org/cpu2017/results/res2025q2/cpu2017-20250324-47137.html) reports integer throughput of 627 versus the 9454P's 525, about +19.4%. Dell's [9455 integer-rate result](https://www.spec.org/cpu2017/results/res2026q1/cpu2017-20260206-51021.html) is 624 versus [520 on a 9454P](https://www.spec.org/cpu2017/results/res2023q2/cpu2017-20230421-35918.pdf). Its [SPECspeed integer-base result of 18.6](https://www.spec.org/cpu2017/results/res2026q1/cpu2017-20260109-50919.html) compares with [14.2 on the older part](https://www.spec.org/cpu2017/results/res2023q2/cpu2017-20230421-35938.html). SPECspeed is a single-copy workload and must not automatically be called a single-thread test. The systems differ; [AMD's exact 9455 specifications](https://www.amd.com/en/products/processors/server/epyc/9005-series/amd-epyc-9455.html) and these results support inclusion as a newer CPU candidate, without borrowing the P or embedded part's score.

The EPYC 9654 illustrates the opposite tradeoff: [119,259 CPU Mark versus 94,689](https://www.cpubenchmark.net/compare/5088vs5596/AMD-EPYC-9654-vs-AMD-EPYC-9454P), but single-thread 2,898 versus 2,988. Keep it and similar throughput-first alternatives in the workload-dependent research section under the user's strict performance requirement.

In particular, [AMD specifies four memory channels for the 9980X](https://www.amd.com/en/products/processors/ryzen-threadripper/9000-series/amd-ryzen-threadripper-9980x.html) and [twelve for the 9454P](https://www.amd.com/en/products/processors/server/epyc/4th-generation-9004-and-8004-series/amd-epyc-9454p.html). The quoted IP-Projects 128 GB option is two 64 GB DIMMs. Do not assume every channel is populated on either server.

The [Threadripper PRO 9985WX offers eight channels](https://www.amd.com/en/products/processors/workstations/ryzen-threadripper/9000-wx-series/amd-ryzen-threadripper-pro-9985wx.html), but the quoted 128GB configuration still uses only two DIMMs. Neither Threadripper row guarantees equivalent memory bandwidth to a fully populated EPYC system. These rows are explicitly CPU-benchmark candidates, with this limitation shown in the table.

Older Xeons, EPYC 7702/7763, mainstream Ryzen and EPYC 9354P offers from broader budget searches must not enter the qualifying shortlist simply because they are inexpensive. A dual-socket aggregate result also must not be confused with a single-socket score.

The 20 November follow-up adds two cautionary examples. The [dual Xeon Gold 6438Y+ result](https://www.cpubenchmark.net/cpu.php?cpu=Intel+Xeon+Gold+6438Y%2B&cpuCount=2) was 92,419 CPU Mark, below 94,689 for the reference despite the combined 64 cores. The [Threadripper PRO 7975WX](https://www.cpubenchmark.net/compare/5729vs5596/AMD-Ryzen-Threadripper-PRO-7975WX-vs-AMD-EPYC-9454P) was only about 0.9% ahead on the aggregate score and lower in several parallel subtests. It is retained as workload-dependent, rather than qualifying from the overall score alone. The [newer CPU evidence](research/2026-11-20-newer-cpu.md) records the subtests and the stronger 9475F's separate SPEC evidence and customer-specific price conditions.

## Storage qualification

The main table interprets the requested 2 TB as raw installed SSD capacity. Mirrored capacity is separately noted where material.

| Drives | Raw capacity | Nominal RAID 1 capacity |
|---|---:|---:|
| 2 x 960 GB | 1.92 TB | 0.96 TB — fails even the raw minimum |
| 2 x 1 TB | 2 TB | 1 TB |
| 2 x 1.92 TB | 3.84 TB | 1.92 TB |
| 2 x 2 TB | 4 TB | 2 TB |
| 2 x 3.84 TB | 7.68 TB | 3.84 TB |

Capacities are nominal decimal TB before filesystem overhead. Do not round 1.92 TB up to 2 TB. A CPU-qualified server with insufficient disks belongs in the research log until an adequate disk upgrade is priced.

## Price normalization

The README retains the original `Price (USD/mo)` column and ascending sort. Native prices, currencies, setup fees and payment terms remain in Notes so the original quote can be reconstructed.

- Native USD offers use their advertised USD recurring amount.
- EUR offers are converted for comparison at **EUR 1 = USD 1.0992**, the [ECB reference rate dated 2026-11-19](https://data-api.ecb.europa.eu/service/data/EXR/D.USD.EUR.SP00.A?startPeriod=2026-11-19&endPeriod=2026-11-19&format=csvdata). Converted amounts are prefixed `~` and rounded to two decimals. This dated API source remains reproducible after the ECB's landing page advances to the next business day.
- BRL offers use **EUR 1 = BRL 6.4765**, the [same date's ECB observation](https://data-api.ecb.europa.eu/service/data/EXR/D.BRL.EUR.SP00.A?startPeriod=2026-11-19&endPeriod=2026-11-19&format=csvdata). Calculate `BRL / 6.4765 * 1.0992` and round only the final USD amount. Keep the actual BRL invoice in Notes. The 20 November pass took place before that day's new ECB publication, so the 19 November rates remain dated explicitly.
- The converted amount is not a promise that the provider will charge that USD price. Provider-specific USD tariffs, card fees and future exchange rates can differ.
- Prices are before VAT where the tax basis is verified. A provider stating that it does not charge VAT is recorded accordingly. Unknown tax treatment is explicitly marked; do not silently subtract an assumed tax rate.
- An advertised tax-inclusive price whose VAT rate cannot be established must never be presented as a verified net amount. Mark it **†** in the price column and retain the full displayed gross amount, with the tax caveat in Notes. This is a conservative comparison when that gross amount is already below the reference's net amount. Do not subtract an assumed VAT percentage. Unknown prices without an established currency belong in the evidence log.
- Show mandatory setup fees and minimum contract length. A prepaid annual or two-year amount divided by its term is an effective monthly rate, not a month-to-month subscription.
- Separate promotions / contract variants may have their own rows. State the upfront commitment, renewal terms when known, and whether the offer is conditional on a code, region or prepayment.
- For prepaid terms, normalize the actual term invoice to a monthly rate and convert currencies before the final rounding. Multiplying a rounded native monthly equivalent can introduce a one-cent discrepancy.
- First-year cost is `12 x recurring monthly + mandatory setup` for monthly billing. For annual prepayment, use the actual annual amount plus setup. A two-year prepayment is a two-year cash commitment and must not be disguised as a first-year payment.

## Evidence and availability

Use provider product pages, exact public configurators, checkout summaries, documented public pricing/stock data, CPU-vendor specifications and benchmark-producer results. Search indexes can expose useful leads, but stale snippets and third-party directories do not establish current stock.

Each table row distinguishes the evidence available:

- **Configured / orderable:** matching hardware and prices were checked in a public configurator or its data; the product reports orderable. This does not prove hardware allocation or delivery.
- **Cart checked:** the public cart names the exact configuration and recurring amount; final tax, stock or delivery may remain unknown.
- **Listed / stock unconfirmed:** a matching provider listing exists, but the exact order or allocation could not be verified.
- **Unavailable:** the provider's current catalogue or stock feed reports no availability.
- **Order mismatch / stale lead:** the advertised link resolves to a different product, errors, or is only indexed. Preserve the evidence in the log; never promote it to confirmed availability.
- **Conditional CPU:** benchmark or platform tradeoffs require workload-specific confirmation.

When a website describes itself as a demonstration or a checkout explicitly simulates hardware, exclude it from recommendations. Missing identity information, inconsistent specifications or a registration-number discrepancy are verification concerns, not proof of fraud. Record what was actually observed and any possible benign explanation.

Some WHMCS storefronts need normal session cookies to preserve a selected product through redirects. Before concluding that a link selects the wrong server, retry the provider's published numeric product link in a fresh anonymous session. Do not use a cookie-less fetch failure as evidence that no order exists. A successful matching follow-up supersedes the earlier retrieval result; keep both observations in the dated log. This process requires no login, checkout submission or payment.

Text extraction can expose hidden alternative-cycle labels such as `Unavailable` or `Indisponível`. Check the selected billing cycle, active product link, HTML state, price calculation and relevant stylesheet before treating those words as stock evidence. This resolved the AMS SOFT and CrockyHost false negatives on 20 November. A working selected cart still does not prove physical stock. Conversely, an explicitly sold-out SKU or negative live inventory result is not overridden merely because a configurator accepts the product.

If demonstration wording is historical and current legal/product pages have changed, record that chronology explicitly. Do not claim the current service is definitely a demonstration; require fresh supply evidence before treating static stock indicators as availability.

No account registration, vendor contact, paid order or hardware reservation was performed as part of this comparison.

## CI ownership comparison

The [buy-versus-rent folder](research/buy-vs-rent/README.md) compares the locally purchased candidates with every existing rental row, using the table and logs at commit `07180f43068a8de01ae30c41a265ec16ef1f138b` as the source snapshot. Existing rows retain their checked dates and evidence levels; importing a row into a calculation is not a fresh checkout or stock check.

- **A1 capacity class:** at least 128 GB and a drive layout supporting about 3.84 TB mirrored capacity. **A2:** at least 256 GB and about 1.92 TB mirrored. These are stricter than the general 2 TB raw disk floor. A two-host pool has per-host limits, not a shared memory pool.
- **Performance:** use public compiler results only to screen candidates. Predeclare actual CI critical-job latency and sustained queue-throughput targets; require both by default. For a 3% tolerance use duration at most 1.03× baseline and rate at least 0.97×; for 5%, 1.05× and 0.95×. A test whose uncertainty spans the threshold remains unresolved.
- **Direct payback:** the primary [hardware comparison](research/buy-vs-rent/06-direct-payback.md) uses parts cost `H` and recurring rental `R`. Show `H/R` without setup or operating costs, then independently select server electricity `E` and incremental internet `I`: `H/(R−E−I)`. For a new rental with a known, avoidable setup `F`, show `(H−F)/(R−E−I)` separately. Already paid setup is sunk; savings begin only when an existing bill can actually stop. If `H>F` and `R≤E+I`, there is no payback. Check the direction of the initial and recurring gaps for other cases. Recovered cost means cumulative avoided rent covers the selected purchase and operating costs, not that future utilities become free.
- **Independent costs:** always publish all four combinations of electricity and internet. Use modeled server wall electricity alone as the direct input; the 25% room-cooling allowance is separate and optional. S$50/month internet is a replaceable incremental allowance, not an ISP quote. **Never add office, room, floor-space or premises rent in any scenario.** UPS, assembly, maintenance reserve, labour, payment/FX charges and financing are separate optional or unquoted items. The earlier [expanded budgets](research/buy-vs-rent/03-rent-vs-buy-tco.md) must not be presented as hardware-only payback. A reserve is a contingency, not measured repair spending.
- **Pricing:** keep native rent/setup/term quotes, then convert with dated FX. Unknown supplier/facility charges remain unknown. Datacenter colocation packages may bundle power and internet without itemized subprices; do not invent an electricity or internet deduction, or add those utilities a second time. A colocation service is separate from the always-excluded office-premises cost.
- **Tax:** ordinary advertised retail ownership prices and rental quotes are not automatically tax-normalized. The 9% Singapore-billing rental calculation is an explicit sensitivity, not a tax determination based on server geography. Preserve tax-inclusive quotes without subtracting an invented rate.
- **Commitment:** prepaid rental comparisons show the entire term commitment needed to cover the selected horizon. A 24-month prepayment is not a 12-month cash price; renewed term prices are assumptions. Distinguish service-month equivalent crossover, actual payment cash flow and minimum liability. A first cash crossing before a prepaid term ends can reverse, so do not label it permanent payback. Keep unknown collection timing unknown. Do not treat a missing setup line as verified free setup. Compute whole-month crossings from unrounded values; preserve extra digits if rounding a fractional value to an integer would imply the wrong month. The [all-rental payback appendix](research/buy-vs-rent/07-all-rentals-break-even.md) applies these rules to all 104 offers.
- **Location:** buying in Singapore and hosting in Malaysia are separate choices. Include power/chassis acceptance, servicing and logistics; a country's seller address is not a datacenter location. European rental savings apply only if European placement is acceptable.
- **Availability:** absent LTD inventory stays historical. Ordinary storefront stock labels, a successful cart and a selected city do not prove allocation. No purchase or supplier contact is part of this research.

The currency reference remains **19 November 2026**: EUR 1 = SGD 1.4176 = USD 1.0992 = MYR 4.5205 = BRL 6.4765. SGD/MYR are additional currencies for the ownership extension; the root table retains its existing USD conversions. [Dated SGD observation](https://data-api.ecb.europa.eu/service/data/EXR/D.SGD.EUR.SP00.A?startPeriod=2026-11-19&endPeriod=2026-11-19&format=csvdata), [dated MYR observation](https://data-api.ecb.europa.eu/service/data/EXR/D.MYR.EUR.SP00.A?startPeriod=2026-11-19&endPeriod=2026-11-19&format=csvdata).

## Ongoing updates

1. Read the current README and latest dated log before searching.
2. Recheck the cheapest relevant offers and any expiring promotions or stock changes.
3. Search new providers and stronger CPU configurations; do not pad the table with below-floor CPUs or duplicate locations without a meaningful difference.
4. Preserve the seven columns and ascending numeric USD order. Keep native currency, tax, setup, term, performance and availability caveats in Notes.
5. Append new evidence and exclusions to a dated research log. Do not erase earlier observations; explain corrections and superseded prices.
6. Review the diff for unsupported availability claims, inadequate storage, tax errors and prepaid-rate confusion before publishing.
7. Never contact suppliers, buy services, alter provider accounts or change unrelated repository files as part of automated research.
