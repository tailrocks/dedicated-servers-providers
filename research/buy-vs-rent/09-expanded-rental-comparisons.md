# 141 rental offers against the Singapore CI workstations

**At 36 months, six capacity-matched rental quotes with a stated setup charge cost less than buying the matching Singapore workstation and paying for server electricity and internet.** Counting only the hardware price gives zero cheaper rentals. Adding a UPS, assembly/delivery, room cooling and a repair reserve raises the count to **15**, including six of the 22 offers added on 20 November 2026. Wsla has the lowest new three-year A2 quote at **S$13,591.32**. ServerWala’s Helsinki annual plan has the lowest new A1 quote at **S$13,998.03**, with its hardware and first invoice documented. [Wsla evidence](../2026-11-20-expansion-global.md#wsla-technology) · [ServerWala evidence](../2026-11-20-expansion-global.md#serverwala) · [Ownership budgets](03-rent-vs-buy-tco.md)

The 22 additions cover eight seller brands. IDs E01–E22 follow their order in the 141-row source table. The full inventory spans 55 alternative seller brands plus Hetzner and counts hardware, location and billing variants. The earlier 104 offers retain IDs 001–104 and the next 15 retain N01–N15. PowerDedi’s first-month promotion updates the existing Amsterdam offer 087. Source checks for the additions were made on 19 November 2026 UTC, 20 November in Vietnam. [141-row source snapshot][snapshot] · [Original 104 offers](05-repository-rental-comparison.md) · [Next 15 offers](08-latest-rental-comparisons.md) · [PowerDedi update](10-current-offer-updates.md)

| Single-host capacity | Prior 119 | New 22 | All 141 |
|---|---:|---:|---:|
| A1 only · at least 128 GB RAM and two SSDs of at least 3.84 TB each | 35 | 6 | 41 |
| A2 only · at least 256 GB RAM and two SSDs of at least 1.92 TB each | 39 | 11 | 50 |
| Both profiles | 2 | 0 | 2 |
| Neither profile established | 43 | 5 | 48 |
| **Distinct offers** | **119** | **22** | **141** |

**93 distinct offers qualify for at least one profile.** The two dual-profile offers yield 43 A1 and 52 A2 comparisons, or 95 in total. The limits use nominal drive capacities available for a mirror. All 17 new capacity matches use the exact EPYC 9454P. The cost comparison assumes the corresponding owned 5995WX workstation passes the CI workload test. DIMM compatibility, parallel-job throughput, SSD behavior and recovery from failure still require validation. The additions establish no deployment in Singapore or Malaysia. [CI acceptance test](04-validation-and-procurement.md) · [Singapore and Malaysian locations](02-rental-market.md)

## Which quotes cost less at 36 months?

Each count cell reads **prior 119 + new 22 = all 141**. The counts compare the full rental cash required to cover month 36 with the matching ownership budget. They include rent and a separately quoted setup amount, including explicitly free setup. Of the 95 profile comparisons, 31 A1 and 34 A2 have that evidence. The remaining 12 A1 and 18 A2 comparisons have no separate setup amount. E15 and E17 give an exact cart total despite leaving setup unitemized. Their quoted costs exceed the expanded A2 budget at 36 months. Unpriced taxes, IPs, payment fees and uncertain renewals may change which option costs less. [Earlier 119-row counts](08-latest-rental-comparisons.md#what-changes-at-36-months-across-all-119-offers) · [Expanded model](03-rent-vs-buy-tco.md#what-the-office-rows-include)

| Singapore ownership costs included | A1 budget S$ | Cheaper A1 rents | A2 budget S$ | Cheaper A2 rents |
|---|---:|---:|---:|---:|
| Hardware only | 8,891.00 | 0 + 0 = **0** | 8,609.40 | 0 + 0 = **0** |
| Hardware + server electricity | 11,757.10 | 0 + 0 = **0** | 11,475.50 | 1 + 0 = **1** |
| Hardware + incremental internet | 10,691.00 | 0 + 0 = **0** | 10,409.40 | 1 + 0 = **1** |
| Hardware + electricity + internet | 13,557.10 | 3 + 0 = **3** | 13,275.50 | 3 + 0 = **3** |
| Expanded budget including UPS, assembly/delivery, room cooling and repair reserve | 15,773.81 | 4 + 3 = **7** | 15,466.87 | 5 + 3 = **8** |

UHost A2 is the one rental below the electricity-only and internet-only budgets. The six below the direct budgets with both utilities are PlusClouds S, HummingTribe and BizoSiz S for A1, and UHost R, PlusClouds R and BizoSiz R for A2. The earlier expanded-budget results also include Provisov A2 and Progressive Robot’s two profile-specific offers. [Original quotes](05-repository-rental-comparison.md#which-rentals-change-the-buying-decision) · [Progressive Robot](08-latest-rental-comparisons.md)

The following additions fall below at least one expanded budget. Positive amounts are the extra rental charges the quote could absorb over 36 months before it crosses that budget. Each ServerWala location offers two separate hardware configurations. The A1 and A2 monthly Helsinki carts illustrate how even the same rent can give different purchasing decisions.

| New offer | 36-month rent + setup S$ | A1 expanded budget minus rent S$ | A2 expanded budget minus rent S$ |
|---|---:|---:|---:|
| Wsla monthly · E01 | 13,591.32 | — | 1,875.55 |
| ServerWala Helsinki annual · E02 / E03 | 13,998.03 | 1,775.78 | 1,468.84 |
| ServerWala Falkenstein annual · E04 / E05 | 14,667.36 | 1,106.45 | 799.50 |
| ServerWala Helsinki monthly · E06 / E07 | 15,553.36 | 220.45 | −86.50 |

## Native rental charges and Singapore-dollar cash required

Each horizon cell gives **native currency / Singapore dollars**. The term figure is the actual rent per payment period. Add stated setup once. For a prepaid term costing `Q` for `p` months, a new customer pays `ceil(horizon / p) × Q + setup`. This assumes the same term and tariff can be renewed. In E15 and E17, the selected cart’s first payment exactly equals the term rent. E20’s plus sign shows rent alone pending a setup quote. Across all 141 offers, 106 state a setup amount and 35 leave it unitemized or unquoted. Buyer-specific taxes are unresolved unless explained below.

The 19 November 2026 exchange rates are EUR 1 = SGD 1.4176 = USD 1.0992 = GBP 0.83581 = CNY 7.3280. Convert native charges to EUR using the corresponding rate and multiply by 1.4176. Every horizon and crossover uses unrounded exchange rates and invoice amounts, with rounding only for display. The SGD budget excludes currency-conversion fees. [ECB SGD][sgdfx] · [ECB USD][usdfx] · [ECB GBP][gbpfx] · [ECB CNY][cnyfx]

| ID and linked offer | CPU · RAM GB / nominal disks in TB | Fit | Native rent per term + one-time setup | 12 months, native / S$ | 24 months, native / S$ | 36 months, native / S$ |
|---|---|---|---|---:|---:|---:|
| E01 [Wsla Serv.Ws162-R][E01] | 9454P · 256 / 2×1.92 | A2 | USD 289.99/mo + 99 | 3,578.88 / 4,615.56 | 7,058.76 / 9,103.44 | 10,538.64 / 13,591.32 |
| E02 [ServerWala Helsinki, 128 GB annual][E02] | 9454P · 128 / 2×3.84 | A1 | USD 3,618/12 mo + 0 | 3,618 / 4,666.01 | 7,236 / 9,332.02 | 10,854 / 13,998.03 |
| E03 [ServerWala Helsinki, 256 GB annual][E03] | 9454P · 256 / 2×1.92 | A2 | USD 3,618/12 mo + 0 | 3,618 / 4,666.01 | 7,236 / 9,332.02 | 10,854 / 13,998.03 |
| E04 [ServerWala Falkenstein, 128 GB annual][E04] | 9454P · 128 / 2×3.84 | A1 | USD 3,791/12 mo + 0 | 3,791 / 4,889.12 | 7,582 / 9,778.24 | 11,373 / 14,667.36 |
| E05 [ServerWala Falkenstein, 256 GB annual][E05] | 9454P · 256 / 2×1.92 | A2 | USD 3,791/12 mo + 0 | 3,791 / 4,889.12 | 7,582 / 9,778.24 | 11,373 / 14,667.36 |
| E06 [ServerWala Helsinki, 128 GB monthly][E06] | 9454P · 128 / 2×3.84 | A1 | USD 335/mo + 0 | 4,020 / 5,184.45 | 8,040 / 10,368.91 | 12,060 / 15,553.36 |
| E07 [ServerWala Helsinki, 256 GB monthly][E07] | 9454P · 256 / 2×1.92 | A2 | USD 335/mo + 0 | 4,020 / 5,184.45 | 8,040 / 10,368.91 | 12,060 / 15,553.36 |
| E08 [ServerWala Falkenstein, 128 GB monthly][E08] | 9454P · 128 / 2×3.84 | A1 | USD 351/mo + 0 | 4,212 / 5,432.07 | 8,424 / 10,864.14 | 12,636 / 16,296.21 |
| E09 [ServerWala Falkenstein, 256 GB monthly][E09] | 9454P · 256 / 2×1.92 | A2 | USD 351/mo + 0 | 4,212 / 5,432.07 | 8,424 / 10,864.14 | 12,636 / 16,296.21 |
| E10 [HOSTING.WORKS ZEN-186F, Finland][E10] | 9454P · 256 / 2×≈1.92 | A2 | EUR 329.99/mo + 119.99 | 4,079.87 / 5,783.62 | 8,039.75 / 11,397.15 | 11,999.63 / 17,010.68 |
| E11 [HOSTING.WORKS ZEN-184F, Finland][E11] | 9454P · 128 / 2×≈3.84 | A1 | EUR 329.99/mo + 119.99 | 4,079.87 / 5,783.62 | 8,039.75 / 11,397.15 | 11,999.63 / 17,010.68 |
| E12 [HOSTING.WORKS ZEN-184, Germany][E12] | 9454P · 128 / 2×≈3.84 | A1 | EUR 339.99/mo + 119.99 | 4,199.87 / 5,953.74 | 8,279.75 / 11,737.37 | 12,359.63 / 17,521.01 |
| E13 [HOSTING.WORKS ZEN-186, Germany][E13] | 9454P · 256 / 2×≈1.92 | A2 | EUR 339.99/mo + 677.50 | 4,757.38 / 6,744.06 | 8,837.26 / 12,527.70 | 12,917.14 / 18,311.34 |
| E14 [IpServer.su RISE-XL, FR/CA annual][E14] | 9455 · 128 / 2×1.92 | Neither | EUR 4,199.88/12 mo + 344.99 | 4,544.87 / 6,442.81 | 8,744.75 / 12,396.56 | 12,944.63 / 18,350.31 |
| E15 [Alpenhost Vienna, 36-month prepay][E15] | 9454P · 256 / 2×1.92 | A2 | EUR 12,599.64/36 mo due | 12,599.64 / 17,861.25 | 12,599.64 / 17,861.25 | 12,599.64 / 17,861.25 |
| E16 [IpServer.su RISE-XL, FR/CA monthly][E16] | 9455 · 128 / 2×1.92 | Neither | EUR 355.99/mo + 344.99 | 4,616.87 / 6,544.87 | 8,888.75 / 12,600.69 | 13,160.63 / 18,656.51 |
| E17 [Alpenhost Vienna, 24-month prepay][E17] | 9454P · 256 / 2×1.92 | A2 | EUR 8,999/24 mo due | 8,999 / 12,756.98 | 8,999 / 12,756.98 | 17,998 / 25,513.96 |
| E18 [Cheap Ai Servers Elite 10][E18] | 9454P · 128 / 7.68 total | Unproven | USD 439.99/mo + 99.95 | 5,379.83 / 6,938.18 | 10,659.71 / 13,747.46 | 15,939.59 / 20,556.73 |
| E19 [Alpenhost Vienna, annual][E19] | 9454P · 256 / 2×1.92 | A2 | EUR 5,399/12 mo + 239.99 | 5,638.99 / 7,993.83 | 11,037.99 / 15,647.45 | 16,436.99 / 23,301.08 |
| E20 [IDCBEST Europe][E20] | 9455 · 128 / 2×1.92 | Neither | CNY 3,500/mo + N/Q | 42,000+ / 8,124.89+ | 84,000+ / 16,249.78+ | 126,000+ / 24,374.67+ |
| E21 [HostingSaint Frankfurt, RISE-XL][E21] | 9455 · 128 / 2×1.92 | Neither | USD 553.93/mo + 0 | 6,647.16 / 8,572.61 | 13,294.32 / 17,145.22 | 19,941.48 / 25,717.83 |
| E22 [Alpenhost Vienna, monthly][E22] | 9454P · 256 / 2×1.92 | A2 | EUR 599/mo + 2,493.99 | 9,681.99 / 13,725.19 | 16,869.99 / 23,914.90 | 24,057.99 / 34,104.61 |

HOSTING.WORKS rounds the drive labels to 2 and 4 TB. Its per-drive data imply approximately 1.92 and 3.84 TB respectively. The classification uses those nominal sizes and assumes RAID 1 can be configured. E18’s 7.68 TB of raw storage at 128 GB RAM leaves the drive count and largest available mirror unknown, so it contributes to “neither profile established.” E14, E16, E20 and E21 document 128 GB RAM and two 1.92 TB drives, which fall below A1 disk and A2 memory. This accounts for all five additions without a confirmed match. [HOSTING.WORKS drive fields](../2026-11-20-expansion-exact-cpu.md) · [Cheap Ai Servers configuration](../2026-11-20-expansion.md#cheap-ai-servers-one-consistent-qualifying-listing) · [9455 configurations](../2026-11-20-expansion-newer-cpu.md)

## Direct payback for 17 capacity-matched offers

The Singapore non-ECC 5995WX workstation costs **S$8,891.00 for A1** with 128 GB and two Samsung 4 TB drives, or **S$8,609.40 for A2** with 256 GB and two Samsung 2 TB drives. The exact eight-module combination in the A1 parts list still needs validation. Select server electricity and incremental internet independently. Monthly operating cost `O` is **S$0**, **S$79.6138** for electricity, **S$50** for internet, or **S$129.6138** for both. Electricity assumes 350 W average at the wall for 730 hours at S$0.3116/kWh. Internet is a planning allowance for an increase in the bill. All four cases exclude premises rent. Optional additional room cooling costs S$19.90345/month if selected. The expanded budget also adds S$700 upfront and 3% of parts cost per year for repairs. [Parts list](01-hardware-and-performance.md) · [Utility assumptions and direct budgets](06-direct-payback.md) · [Expanded cost components](03-rent-vs-buy-tco.md#monthly-components-at-an-existing-site)

Each cell gives **months using recurring rent alone / months including the avoidable setup on a new rental**. For hardware price `H`, effective monthly rent `R` and setup `F`, these are `H / (R − O)` and `(H − F) / (R − O)`. The first figure with neither utility is the simple hardware-price / monthly-rent result. An existing customer uses the rent they can actually stop paying and credits no previously paid setup. With monthly billing, round the full-precision crossing upward to obtain the first completed month at which buying costs no more. With prepaid billing these are service-month equivalents. E15 and E17 have N/Q for a separately stated setup. Their exact cash comparisons follow in the next section. [Break-even method](07-all-rentals-break-even.md#how-to-read-a-payback-cell)

| Offer and matching purchase | Monthly rent / setup S$ | Neither utility | Electricity only | Internet only | Both utilities |
|---|---:|---:|---:|---:|---:|
| E01 · A2 | 373.99 / 127.68 | 23.02 / 22.68 | 29.25 / 28.81 | 26.57 / 26.18 | 35.23 / 34.71 |
| E02 · A1 | 388.83 / 0.00 | 22.87 / 22.87 | 28.75 / 28.75 | 26.24 / 26.24 | 34.30 / 34.30 |
| E03 · A2 | 388.83 / 0.00 | 22.14 / 22.14 | 27.84 / 27.84 | 25.41 / 25.41 | 33.21 / 33.21 |
| E04 · A1 | 407.43 / 0.00 | 21.82 / 21.82 | 27.12 / 27.12 | 24.88 / 24.88 | 32.00355 / 32.00355 |
| E05 · A2 | 407.43 / 0.00 | 21.13 / 21.13 | 26.26 / 26.26 | 24.09 / 24.09 | 30.99 / 30.99 |
| E06 · A1 | 432.04 / 0.00 | 20.58 / 20.58 | 25.23 / 25.23 | 23.27 / 23.27 | 29.40 / 29.40 |
| E07 · A2 | 432.04 / 0.00 | 19.93 / 19.93 | 24.43 / 24.43 | 22.54 / 22.54 | 28.47 / 28.47 |
| E08 · A1 | 452.67 / 0.00 | 19.64 / 19.64 | 23.83 / 23.83 | 22.08 / 22.08 | 27.52 / 27.52 |
| E09 · A2 | 452.67 / 0.00 | 19.02 / 19.02 | 23.08 / 23.08 | 21.38 / 21.38 | 26.65 / 26.65 |
| E10 · A2 | 467.79 / 170.10 | 18.40 / 18.04 | 22.18 / 21.74 | 20.61 / 20.20 | 25.46 / 24.96 |
| E11 · A1 | 467.79 / 170.10 | 19.01 / 18.64 | 22.90 / 22.47 | 21.28 / 20.87 | 26.29 / 25.79 |
| E12 · A1 | 481.97 / 170.10 | 18.45 / 18.09 | 22.10 / 21.67 | 20.58 / 20.19 | 25.23 / 24.75 |
| E13 · A2 | 481.97 / 960.42 | 17.86 / 15.87 | 21.40 / 19.01 | 19.93 / 17.71 | 24.43 / 21.71 |
| E15 · A2 | 496.15 / N/Q | 17.35 / N/Q | 20.67 / N/Q | 19.30 / N/Q | 23.49 / N/Q |
| E17 · A2 | 531.54 / N/Q | 16.20 / N/Q | 19.05 / N/Q | 17.88 / N/Q | 21.42 / N/Q |
| E19 · A2 | 637.80 / 340.21 | 13.50 / 12.97 | 15.42 / 14.81 | 14.65 / 14.07 | 16.94 / 16.27 |
| E22 · A2 | 849.14 / 3,535.48 | 10.14 / 5.98 | 11.19 / 6.59 | 10.77 / 6.35 | 11.97 / 7.05 |

Wsla E01 illustrates the difference between the purchase price and the bills it can displace. Ignoring rental setup, A2 earns back its parts price in **23.02 months**, or **35.23 months** with both utilities. Avoiding the new rental’s USD 99 setup moves those crossings to **22.68 and 34.71 months**. With both utilities, buying is cheaper by month 35 and by **S$315.82** at month 36. If the order requires additional charges or the existing rental is committed for longer, the cash flows must start from the first avoidable payment. [Wsla product and billing evidence](../2026-11-20-expansion-global.md#wsla-technology)

## When prepaid cash crosses

This table gives the **first completed service month after which cumulative ownership cash stays at or below rental cash at every later month-end**, assuming the same renewal invoices. Prepayment can move this point to the start of a billing period. For quoted opening payment `P`, recurring term invoice `Q`, term length `p` and monthly owner cost `O`, compare `H + m × O` with `P + (ceil(m / p) − 1) × Q`. The owner’s position is weakest at the end of each invoice period. Here `Q > p × O`, so the first term that finishes with buying no dearer is `k = max(1, ceil((H − (P − Q)) / (Q − p × O)))`. The durable month is `1 + (k − 1) × p`. This calculation uses E15 and E17’s exact upfront quote without assuming a contractual promise of free setup. [Prepaid method and earlier examples](07-all-rentals-break-even.md#prepaid-cash-and-contract-commitments)

| Offer and purchase | Prepaid months | First payment S$ | Neither utility | Electricity only | Internet only | Both utilities |
|---|---:|---:|---:|---:|---:|---:|
| E02 · A1 | 12 | 4,666.01 | 13 | 25 | 25 | 25 |
| E03 · A2 | 12 | 4,666.01 | 13 | 25 | 25 | 25 |
| E04 · A1 | 12 | 4,889.12 | 13 | 25 | 25 | 25 |
| E05 · A2 | 12 | 4,889.12 | 13 | 25 | 25 | 25 |
| E15 · A2 | 36 | 17,861.25 | 1 | 1 | 1 | 1 |
| E17 · A2 | 24 | 12,756.98 | 1 | 1 | 1 | 1 |
| E19 · A2 | 12 | 7,993.83 | 13 | 13 | 13 | 13 |

For ServerWala Helsinki, two annual invoices total **S$9,332.02** through month 24. At that point A1 ownership with both utilities costs **S$12,001.73** and A2 costs **S$11,720.13**. The third annual payment is due in month 25 and brings rental cash to **S$13,998.03**. Ownership then stays cheaper in both cases. The service equivalents with both utilities are 34.30 and 33.21 months. [Helsinki billing terms and both configurations](../2026-11-20-expansion-global.md#serverwala)

At Alpenhost the selected 36-month cart collects **S$17,861.25** immediately, and the 24-month cart collects **S$12,756.98**. Each opening payment exceeds the A2 hardware price and both utilities through the entire first term, giving month 1 in all four scenarios. The amount of service consumed by month 12 is smaller than these payments. The table gives the prorated value of the service used at each horizon so that the cost of unused prepaid months is visible. [Selected Alpenhost carts and term lengths](../2026-11-20-expansion.md#alpenhost-actual-configuration-and-payment-period-totals)

| Alpenhost term | 12 months of service, EUR / S$ | 24 months of service, EUR / S$ | 36 months of service, EUR / S$ |
|---|---:|---:|---:|
| E15 · 36 months prepaid | 4,199.88 / 5,953.75 | 8,399.76 / 11,907.50 | 12,599.64 / 17,861.25 |
| E17 · 24 months prepaid | 4,499.50 / 6,378.49 | 8,999.00 / 12,756.98 | 13,498.50 / 19,135.47 |

At month 36, E17 has consumed 36 months of service and has paid for 48. The two invoiced terms total **EUR 17,998 / S$25,513.96**. If usage ends then, 12 prepaid months remain and any refund depends on the contract. E14 is also prepaid, but its 128 GB / two 1.92 TB configuration qualifies for neither purchase, so its payback is N/A.

## Malaysian electricity sensitivity for the same A2 workstation

Placing the Singapore-procured A2 at an existing Peninsular Malaysian site changes average server electricity to **S$44.14056/month**, using 255.5 kWh × RM0.5509088/kWh and EUR 1 = MYR 4.5205 = SGD 1.4176. Internet stays independently selectable at S$50. The hardware-only and internet-only service comparisons therefore equal the Singapore values above. The following two columns give the revised **recurring-only / setup-adjusted** values for the scenarios that change. The prepaid column gives the four durable cash months in the order neither, electricity, internet, both. A monthly customer rounds the corresponding service crossing up. Cross-border shipment, duties, seller-specific taxes and servicing remain unpriced. The locally sourced Malaysian desktop pair has two separate 64 GB memory pools and a separate purchase and power budget. [Malaysian electricity and local purchasing](06-direct-payback.md#6-malaysia-separate-electricity-sensitivity-and-local-purchase) · [Regional tariff details](02-rental-market.md#8-electricity-sources-for-ownership-scenarios)

| New A2 rental | Electricity only, months | Both utilities, months | Prepaid cash months |
|---|---:|---:|---|
| E01 · Wsla Serv.Ws162-R | 26.10 / 25.71 | 30.76 / 30.31 | Monthly |
| E03 · ServerWala Helsinki annual | 24.98 / 24.98 | 29.21 / 29.21 | 13 / 25 / 25 / 25 |
| E05 · ServerWala Falkenstein annual | 23.70 / 23.70 | 27.48 / 27.48 | 13 / 13 / 25 / 25 |
| E07 · ServerWala Helsinki monthly | 22.20 / 22.20 | 25.48 / 25.48 | Monthly |
| E09 · ServerWala Falkenstein monthly | 21.07 / 21.07 | 24.01 / 24.01 | Monthly |
| E10 · HOSTING.WORKS ZEN-186F | 20.32 / 19.92 | 23.04 / 22.59 | Monthly |
| E13 · HOSTING.WORKS ZEN-186 | 19.66 / 17.47 | 22.20 / 19.72 | Monthly |
| E15 · Alpenhost Vienna, 36 months | 19.05 / N/Q | 21.42 / N/Q | 1 / 1 / 1 / 1 |
| E17 · Alpenhost Vienna, 24 months | 17.66 / N/Q | 19.68 / N/Q | 1 / 1 / 1 / 1 |
| E19 · Alpenhost Vienna, annual | 14.50 / 13.93 | 15.84 / 15.21 | 13 / 13 / 13 / 13 |
| E22 · Alpenhost Vienna, monthly | 10.69 / 6.30 | 11.40 / 6.72 | Monthly |

At month 36 the direct A2 budget with both Malaysian utilities is **S$11,998.46** and the optional expanded budget is **S$13,870.57**. Wsla E01 is the only addition with a stated setup below that expanded figure, by **S$279.25**. ServerWala E03 at S$13,998.03 is S$127.45 above it. Final procurement and supplier quotes matter particularly at these margins. [Expanded Malaysia model](03-rent-vs-buy-tco.md#9-malaysia-electricity-sensitivity-and-conditional-colocation-floors)

## What the supplier evidence establishes

| Seller and rows | Quoted terms and outstanding checks |
|---|---|
| Wsla Technology · E01 | Monthly USD 289.99 + USD 99 setup. The offer includes one IPv4 and unmetered 1 Gbps. The order reached domain selection. Physical location, RAID mode, additional minimum, tax, payment total and stock remain unconfirmed. The separately listed annual USD 3,479.99 rent exceeds twelve monthly rents by USD 0.11, and annual-specific setup is unknown. [Seller catalog](https://client.wsla.ps/store/dedicated-servers?language=english) · [Monthly terms and fee evidence](../2026-11-20-expansion-global.md#wsla-technology) |
| ServerWala · E02–E09 | All four hardware/location combinations have monthly and annual carts with explicit USD 0 setup and a first payment matching the term. They include RAID 1 and a shared 1 Gbps port with 20 TB of traffic. Indian-registered customers face 18% GST. Payment-gateway charges depend on method, with bank transfers exempt. Applicable buyer tax, later renewal prices, IP allocation and stock remain unconfirmed. [Seller hardware and term catalog](https://www.serverwala.com/hosting/amd-dedicated-server) · [Seller payment terms](https://www.serverwala.com/term-condition) · [Exact four carts and other terms](../2026-11-20-expansion-global.md#serverwala) |
| HOSTING.WORKS · E10–E13 | Product-specific EUR fields give recurring rent and setup. E13’s Germany 256 GB setup is EUR 677.50. The other three are EUR 119.99. Each includes 1 IPv4, IPv6 /64 and unlimited 1 Gbps. Private-customer cards are listed. Ukrainian resident businesses use a UAH bank transfer. Foreign-buyer payment terms, VAT, RAID mode and allocated stock need confirmation. [Payment policy](https://hosting.works/payment_methods) · [Pricing fields and drive evidence](../2026-11-20-expansion-exact-cpu.md) |
| IpServer.su · E14, E16 | France and Canada list the same 9455 and software RAID 1 with 1.92 TB mirrored. The annual and monthly terms each add EUR 344.99 setup. The annual invoice here is calculated from the exact published term rate. The upstream availability feed reported no available locations. Reseller inventory, customer eligibility and final tax remain open. [Canada configurator](https://www.ipserver.su/en/prices/index/view/id/7423/ca-rise-xl) · [Both configurators, term and supply evidence](../2026-11-20-expansion-newer-cpu.md) |
| Alpenhost · E15, E17, E19, E22 | Unmanaged AE9454P in Vienna NDC2, standard hardware and up to 1 Gbps under fair use. All four EUR quotes retain applicable VAT under the seller’s gross-price terms. The rate and tax split are unconfirmed. Annual and monthly carts quote setup separately. On 24- and 36-month carts the amount due equals the term rent, with no separate setup line. The contract period follows the billing interval. Physical stock and IPv4 allocation remain unconfirmed. [Supplier category](https://alpenhost.at/Kundencenter/store/dedicated-server-amd) · [Terms](https://alpenhost.at/allgemeine-geschaeftsbedingungen/) · [Exact selected subtotals](../2026-11-20-expansion.md#alpenhost-actual-configuration-and-payment-period-totals) |
| Cheap Ai Servers · E18 | Elite 10 lists monthly USD 439.99 + USD 99.95 setup, one IPv4, IPv6 /64 and 1 Gbps. The order reached domain selection. Physical drive count, RAID, traffic allowance conditions, datacenter, tax, operator, final invoice and stock remain unresolved. [Billing listing][E18] · [Configuration and order evidence](../2026-11-20-expansion.md#cheap-ai-servers-one-consistent-qualifying-listing) |
| IDCBEST / 天下数据 · E20 | CNY 3,500/month ex tax with one IP, 1 Gbps and two SSDs of unspecified interface. The seller adds 8% for tax-inclusive billing, producing CNY 3,780/month, or CNY 136,080 / S$26,324.65 rent alone at 36 months. The mid-year promotion remained listed with a generic order path. Setup, country, availability, expiry and renewal are unknown. [Seller payment policy](https://www.idcbest.com/about/pay1.asp) · [Product evidence](../2026-11-20-expansion-newer-cpu.md) |
| HostingSaint · E21 | Monthly USD 553.93 with explicit USD 0 setup in the selected Frankfurt order. Other locations were selectable. The machine has two 1.92 TB NVMe drives, 1 Gbps, one IPv4 and IPv6 /64. Tax, array configuration and actual inventory are unconfirmed. [Selected USD configuration][E21] · [Billing and location evidence](../2026-11-20-expansion-newer-cpu.md) |

The source watchlist also covers the benchmark-dependent DediRoom Xeon 6761P, region-limited IRR billing at ServerFee, and conflicting CPU or currency evidence at MarsAI. Those entries have separate procurement or performance conditions. [Conditional CPU comparison](../2026-11-20-expansion-newer-cpu.md) · [Regional payment and configuration checks](../2026-11-20-expansion-exact-cpu.md) · [Expansion exclusions](../2026-11-20-expansion.md#other-excluded-and-unresolved-offers)

[snapshot]: https://github.com/tailrocks/dedicated-servers-providers/blob/175399c50339f5d8192c4a5821e74db4d5fbd4f6/README.md?plain=1#L23-L167
[sgdfx]: https://data-api.ecb.europa.eu/service/data/EXR/D.SGD.EUR.SP00.A?startPeriod=2026-11-19&endPeriod=2026-11-19&format=csvdata
[usdfx]: https://data-api.ecb.europa.eu/service/data/EXR/D.USD.EUR.SP00.A?startPeriod=2026-11-19&endPeriod=2026-11-19&format=csvdata
[gbpfx]: https://data-api.ecb.europa.eu/service/data/EXR/D.GBP.EUR.SP00.A?startPeriod=2026-11-19&endPeriod=2026-11-19&format=csvdata
[cnyfx]: https://data-api.ecb.europa.eu/service/data/EXR/D.CNY.EUR.SP00.A?startPeriod=2026-11-19&endPeriod=2026-11-19&format=csvdata
[E01]: https://client.wsla.ps/cart.php?gid=3&carttpl=standard_cart
[E02]: https://serverwala.cloud/?cmd=cart&action=add&id=2867&cycle=a
[E03]: https://serverwala.cloud/?cmd=cart&action=add&id=2868&cycle=a
[E04]: https://serverwala.cloud/?cmd=cart&action=add&id=2875&cycle=a
[E05]: https://serverwala.cloud/?cmd=cart&action=add&id=2876&cycle=a
[E06]: https://serverwala.cloud/?cmd=cart&action=add&id=2867&cycle=m
[E07]: https://serverwala.cloud/?cmd=cart&action=add&id=2868&cycle=m
[E08]: https://serverwala.cloud/?cmd=cart&action=add&id=2875&cycle=m
[E09]: https://serverwala.cloud/?cmd=cart&action=add&id=2876&cycle=m
[E10]: https://hosting.works/dedicated/997
[E11]: https://hosting.works/dedicated/1484
[E12]: https://hosting.works/dedicated/1757
[E13]: https://hosting.works/dedicated/1059
[E14]: https://www.ipserver.su/en/prices/index/view/id/7217/fr-rise-xl
[E15]: https://alpenhost.at/Kundencenter/store/dedicated-server-amd/ae9454-dedicated-server?billingcycle=triennially
[E16]: https://www.ipserver.su/en/prices/index/view/id/7217/fr-rise-xl
[E17]: https://alpenhost.at/Kundencenter/store/dedicated-server-amd/ae9454-dedicated-server?billingcycle=biennially
[E18]: https://cheapaiservers.com/billing/index.php?rp=/store/amd-ryzen-dedicated-server
[E19]: https://alpenhost.at/Kundencenter/store/dedicated-server-amd/ae9454-dedicated-server?billingcycle=annually
[E20]: https://www.idcbest.com/server/ouzhou.asp
[E21]: https://hostingsaint.com/cart.php?a=add&pid=99&billingcycle=monthly&currency=2
[E22]: https://alpenhost.at/Kundencenter/store/dedicated-server-amd/ae9454-dedicated-server?billingcycle=monthly
