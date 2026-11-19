# Initial 104 rental offers against the owned CI hosts

[Home](../../README.md) · [Buy vs rent](README.md)

**Rental snapshot** · 104 offers at `07180f4`

[Read the comparison](#reading-the-full-comparison) · [A1 only](#a1-only) · [A2 only](#a2-only) · [Both profiles](#both-a1-and-a2) · [Neither profile](#neither-a1-nor-a2)

**Snapshot scope:** this file preserves IDs 001–104 from commit `07180f4`. The [next 15 additions](08-latest-rental-comparisons.md) and [following 22 additions](09-expanded-rental-comparisons.md) extend the same capacity, horizon-cost and payback methodology to **141** offers through `175399c`. Counts and the seven-offer finding below refer to this initial snapshot; the 141-offer snapshot's expanded-budget count is fifteen. [Current offer corrections](10-current-offer-updates.md) overlay the 087 PowerDedi first-month coupon. Do not renumber these stable IDs using current sorted rental catalog positions.

**This file preserves the original rental inventory and its optional expanded-budget comparison.** For the user's primary hardware-only and independently selected electricity/internet question, start with [direct payback](06-direct-payback.md), [initial rental break-even months](07-all-rentals-break-even.md) and [the 141-offer coverage update](09-expanded-rental-comparisons.md). Office rent is excluded in every scenario. The expanded ownership totals here additionally count UPS/assembly, room cooling and a repair reserve; they must not be mistaken for hardware-only totals.

**At 36 months, seven capacity-matched rental offers have published rent and setup below the corresponding optional expanded Singapore budget before additional customer-specific charges.** The lowest A2 quote with a stated fee is UHost in Helsinki at S$10,368.91. For A1, PlusClouds lists S$12,269.33, while BizoSiz reached a matching cart at S$13,096.55. These are European server locations. If runners must be in Singapore or Malaysia, the relevant alternatives are in the [regional rental comparison](02-rental-market.md).

The 104 rows represent 38 alternative seller brands plus Hetzner. The source is the repository’s 19–20 November 2026 rental research, frozen at commit `07180f4`. The 20 November label follows Vietnam time. This analysis recalculates the recorded offers and inherits their check dates and stock evidence. [Original seven-column table][snapshot] · [Rental methodology][method] · [Dated research summary](../2026-11-20.md)

## Which rentals change the buying decision?

**A1** requires at least 128 GB and two drives of at least 3.84 TB each. **A2** requires at least 256 GB and two drives of at least 1.92 TB each. These floors reproduce the nominal mirrored capacities of the AX162-1 and AX162-2. Two 1.92 TB drives on a 128 GB host miss both profiles. A 256 GB server with two 3.84 TB drives satisfies both. Actual space after formatting, application throughput, SSD endurance, ECC and service obligations are separate checks. [Hardware and CI performance](01-hardware-and-performance.md) · [Workload validation](04-validation-and-procurement.md)

The optional expanded Singapore budgets use 5995WX systems with S$8,891.00 (A1) or S$8,609.40 (A2) in parts, S$700 for UPS and assembly/delivery, 350 W assumed average at the wall, 25% cooling overhead, S$50/month incremental connectivity and a 3% annual parts reserve. Resale and incremental owner labour are zero; office rent is excluded. The rentals below use the exact EPYC 9454P. Each rental’s **headroom** is the additional total rental cost it could absorb before equalling its matching 36-month expanded budget. Taxes, any unpriced IPv4 or traffic, and the cost of meeting service requirements can use that headroom. Headroom uses unrounded inputs, so subtracting displayed amounts can differ by one cent. [Separate cost components and sensitivities](03-rent-vs-buy-tco.md)

| Profile and alternative | 12 months S$ | 24 months S$ | 36 months S$ | 36-month headroom S$ | Commercial evidence |
|---|---:|---:|---:|---:|---|
| **A1 Singapore office** | **11,651.94** | **13,712.87** | **15,773.81** | — | Modeled ownership budget. |
| A1 · [PlusClouds / Radius AX162-S, FI/DE][q5] | 4,478.20 | 8,373.76 | 12,269.33 | 3,504.48 | Listing, ex VAT. Minimum term and SKU allocation unconfirmed. |
| A1 · [BizoSiz AX162-S, DE/FI][q8] | 4,460.95 | 8,778.75 | 13,096.55 | 2,677.26 | Monthly cart. Tax, IP/traffic, delivery queue and payment eligibility unresolved. |
| A1 · [HummingTribe Dedicated Power, Germany][q6] | 4,889.13 | 9,141.76 | 13,394.39 | 2,379.42 | Monthly listing. Seller says no VAT. One-person operator with business-hours support. |
| **A2 Singapore office** | **11,361.89** | **13,414.38** | **15,466.87** | — | Modeled ownership budget. |
| A2 · [UHost AX162-R, Helsinki][q1] | 3,559.48 | 6,964.19 | 10,368.91 | 5,097.96 | Configurator. Tax, network terms, contracting entity and stock unresolved. |
| A2 · [PlusClouds / Radius AX162-R, FI/DE][q4] | 4,663.90 | 8,559.47 | 12,455.03 | 3,011.83 | Listing, ex VAT. Minimum term and SKU allocation unconfirmed. |
| A2 · [BizoSiz AX162-R, DE/FI][q7] | 4,460.95 | 8,778.75 | 13,096.55 | 2,370.32 | Monthly cart. Tax, IP/traffic, delivery queue and payment eligibility unresolved. |
| A2 · [Provisov, Nuremberg][q13] | 4,845.27 | 9,549.97 | 14,254.67 | 1,212.20 | Application form. Tax, minimum term and stock unresolved. |

The BizoSiz AX162-S and AX162-R have the same price but different memory and disk layouts. UHost’s USD 220/month AX162-R fits A2 only. Its A1 configuration is USD 363/month plus USD 120 setup, S$17,008.10 over 36 months. Lindau’s AX162-S lists 256 GB and four 3.84 TB drives from USD 236.41/month, with setup, minimum term, merchant details and a selected order unresolved. AMS SOFT’s Finnish A1 cart showed BRL 1,989.90 due for the first month. Its three-year **rent alone** is S$15,680.04, leaving S$93.77 for any setup or tax before reaching the A1 office budget. [European and global listings](../2026-11-19-global.md) · [BizoSiz carts](../2026-11-20-exact-cpu.md#bizosiz) · [AMS SOFT cart totals](../2026-11-20-latin-america.md#ams-soft)

The three-year Malaysia **A2 office electricity sensitivity** is approximately S$13,871 using the same Singapore-procured parts and Peninsular commercial power. UHost R, PlusClouds R and BizoSiz R are below that modeled amount at their stated rates. Provisov exceeds it. Cross-border logistics, tax and local servicing can change the ownership side. The Malaysia A2 4U and tower known-cost budgets are about S$16,148 and S$16,378 at 36 months, with enclosure, power or contract approval outstanding. Use the local-purchase scenarios separately when comparing Malaysian-sourced hardware. [Ownership and colocation models](03-rent-vs-buy-tco.md) · [Local parts and facilities](02-rental-market.md)

### What changes with the time horizon?

These counts use rows that meet the indicated capacity and have a specified setup amount (including explicitly free setup). A dual-profile row with a specified setup counts in both totals. Unknown tax, price changes, minimum-term uncertainty and stock can change a result. Additional rows with an undisclosed setup remain visible in the full tables below.

| Matching rental rows with a specified setup | Cheaper than Singapore office at 12 months | At 24 months | At 36 months |
|---|---:|---:|---:|
| A1 · 24 rows | 23 | 18 | 3 |
| A2 · 21 rows | 21 | 11 | 4 |

The bare regular Hetzner AX162-1 costs EUR 7,651.60 in year one and EUR 22,346.80 over three years, S$10,846.91 and S$31,678.82 at the fixed FX. That year-one subtotal is below the A1 office cash budget. The ownership model’s separate illustrative Singapore-billed case adds IPv4 and 9% non-recoverable tax to the rental, taking year one to about S$11,855. Use the tax and IP treatment applicable to the actual buyer. **Hetzner AX162-1 LTD was unavailable in the repository’s product/availability feed check.** An existing contract at a legacy rate can be evaluated using its actual invoice. [Reference feed evidence](../2026-11-20.md#reference-and-currency-recheck) · [LTD inventory and both reference models](../2026-11-19.md#hetzner-reference-and-limited-stock-variants)

## Reading the full comparison

| Capacity of the advertised single host | Distinct rental rows |
|---|---:|
| A1 only | 32 |
| A2 only | 32 |
| Both A1 and A2 | 2 |
| Neither profile | 38 |
| **Total** | **104** |

- **Currency and setup.** The first three horizon columns use the currency in that row’s price. `USD 279/mo + 111` means USD 279 rent per month and USD 111 setup once. `EUR 6,226.32/24 mo + 0` means a full EUR 6,226.32 term invoice. Zero appears only for an expressly free or waived setup. The last money column converts the full 36-month native amount into SGD. The 19 November 2026 rates were EUR 1 = SGD 1.4176 = USD 1.0992 = BRL 6.4765. Conversion uses the native invoice and rounds the result once. A provider’s separate USD tariff can differ. [ECB SGD][sgdfx] · [ECB USD][usdfx] · [ECB BRL][brlfx]
- **Commitments.** For a horizon of `N` months, count `ceil(N / billing-cycle months)` full invoices, then add setup once. A 24-month prepay covers a 12-month need with one 24-month payment. A 36-month need on the same rate requires two 24-month payments and covers 48 months. Monthly billing with a 12-month minimum is marked separately. HostAddon row 046 specifies a 12-month cycle commitment. The precise collection date on that cycle was unconfirmed. All extensions assume the same term and rate are offered again, without a second setup. `Term N/Q` marks an expressly unresolved minimum. Amounts for those rows use the listed rate for N months and a longer minimum could increase the liability. A monthly figure by itself gives no assurance of cancellation terms.
- **Missing fees and taxes.** `N/Q` means the source could not establish the amount or term. Of 104 rows, 78 state a setup and 23 show no setup line on the selected quote. For the latter, a trailing `+` on each horizon (for example `5,076+`) means known rent with **setup still N/Q**. The other three rows have a starting price or quote-only rate with both the setup and term unresolved, so the horizon totals are N/Q. `Tax N/Q` leaves the customer’s tax unresolved. `Ex VAT`, `VAT included`, `tax extra` and HummingTribe’s no-VAT statement retain the quoted basis. Optional services, payment/FX fees and unpriced mandatory items are outside the displayed subtotal.
- **Capacity and evidence.** The hardware column shows CPU model, installed GB RAM and the count × size of individual NVMe drives in decimal TB. A mirror on two equal drives has nominal capacity equal to one drive. EPYC 9454P is the reference chip. The 9455, 9455P, 9980X and PRO 9985WX have separate benchmark evidence. The quoted Threadrippers use two DIMMs, so at most two memory channels can be populated. All candidates still require the same CI replay to assess the 3–5% tolerance. The evidence column reports the repository’s selected cart, configurator, listing, quote or feed check. Physical allocation remained unverified in every row. Stock may overlap among reseller brands using the same datacenter references, notably CTCServers, EPY Host, iDatam, KW Servers, LeoServers, Servers99, GTZHost, Fit Servers and iRexta. [CPU and supply evidence][method] · [Reseller checkout evidence](../2026-11-20.md#useful-price-distinctions)

Each numbered offer links to the primary product or configurator recorded in the [frozen rental table][snapshot]. Numbers follow the source ordering (row 001 is README line 27). The tables group offers by capacity and preserve source order within each group.

For a direct comparison at any horizon, the same Singapore office budgets expressed in each rental currency are below. A rental subtotal below the corresponding ceiling has room for additional charges before reaching that office budget.

| Native currency | A1 · 12 mo | A1 · 24 mo | A1 · 36 mo | A2 · 12 mo | A2 · 24 mo | A2 · 36 mo |
|---|---:|---:|---:|---:|---:|---:|
| USD | 9,034.85 | 10,632.89 | 12,230.93 | 8,809.95 | 10,401.44 | 11,992.93 |
| EUR | 8,219.48 | 9,673.30 | 11,127.12 | 8,014.88 | 9,462.74 | 10,910.60 |
| BRL | 53,233.47 | 62,649.15 | 72,064.82 | 51,908.35 | 61,285.43 | 70,662.50 |

## A1 only

These hosts can supply a 3.84 TB mirror or larger from at least 128 GB RAM. Each has under 256 GB RAM. Compare the 36-month SGD column with **S$15,773.81** for the Singapore office A1.

| Source row and rental offer | CPU · GB RAM / drives (TB) | Native rent per cycle + setup | 12 mo, native | 24 mo, native | 36 mo, native | 36 mo, S$ | Evidence and tax |
|---|---|---|---:|---:|---:|---:|---|
| 005 [PlusClouds / Radius AX162-S, FI/DE][q5] | 9454P · 128 / 2×3.84 | EUR 229/mo + 411 · term N/Q | 3,159 | 5,907 | 8,655 | 12,269.33 | Listing · ex VAT. General portal, no selected SKU. |
| 006 [HummingTribe Dedicated Power, Germany][q6] | 9454P · 128 / 2×3.84 | EUR 249.99/mo + 449 | 3,448.88 | 6,448.76 | 9,448.64 | 13,394.39 | Listing · seller says no VAT. Business-hours support. |
| 008 [BizoSiz AX162-S, DE/FI][q8] | 9454P · 128 / 2×3.84 | USD 279/mo + 111 | 3,459 | 6,807 | 10,155 | 13,096.55 | Cart · tax N/Q. Delivery queue and payment eligibility. |
| 016 [AMS SOFT AX162-S, Finland][q16] | 9454P · 128 / 2×3.84 | BRL 1,989.90/mo + N/Q | 23,878.80+ | 47,757.60+ | 71,636.40+ | 15,680.04+ | Cart total · tax N/Q. Due today equals one month’s rent. |
| 017 [Pro-m, Finland][q17] | 9454P · 128 / 2×3.84 | USD 347/mo + 527 · 1-mo min | 4,691 | 8,855 | 13,019 | 16,790.15 | Cart · final tax N/Q. Port, traffic and IPv4 unconfirmed. |
| 023 [UHost AX162-S, Helsinki][q23] | 9454P · 128 / 2×3.84 | USD 363/mo + 120 | 4,476 | 8,832 | 13,188 | 17,008.10 | Configurator · tax N/Q. Port, traffic and contracting entity unresolved. |
| 024 [CTCServers, Falkenstein][q24] | 9454P · 128 / 2×3.84 | USD 364/mo + 1,496.35 | 5,864.35 | 10,232.35 | 14,600.35 | 18,829.56 | Cart · tax N/Q. |
| 026 [iDatam, Falkenstein][q26] | 9454P · 128 / 2×3.84 | USD 364/mo + 1,496.35 | 5,864.35 | 10,232.35 | 14,600.35 | 18,829.56 | Cart · tax N/Q. Cart and catalog DC references differ. |
| 027 [GTZHost, Helsinki][q27] | 9454P · 128 / 2×3.84 | USD 365/mo + 1,134.69 | 5,514.69 | 9,894.69 | 14,274.69 | 18,409.57 | Cart · tax N/Q. ID verification. |
| 028 [Servers99, Helsinki][q28] | 9454P · 128 / 2×3.84 | USD 365/mo + 1,134.69 | 5,514.69 | 9,894.69 | 14,274.69 | 18,409.57 | Cart · tax N/Q. |
| 029 [BytesRack, Helsinki][q29] | 9454P · 128 / 2×3.84 | USD 366/mo + 1,134.69 | 5,526.69 | 9,918.69 | 14,310.69 | 18,456.00 | Cart · tax N/Q. |
| 030 [GTZHost, Falkenstein][q30] | 9454P · 128 / 2×3.84 | USD 367/mo + 1,496.35 | 5,900.35 | 10,304.35 | 14,708.35 | 18,968.85 | Cart · tax N/Q. ID verification. |
| 031 [KW Servers, Falkenstein][q31] | 9454P · 128 / 2×3.84 | USD 367/mo + 1,496.35 | 5,900.35 | 10,304.35 | 14,708.35 | 18,968.85 | Cart · tax N/Q. |
| 033 [KW Servers, Helsinki][q33] | 9454P · 128 / 2×3.84 | USD 369/mo + 1,134.69 | 5,562.69 | 9,990.69 | 14,418.69 | 18,595.28 | Cart · tax N/Q. |
| 034 [Pro-m, Germany][q34] | 9454P · 128 / 2×3.84 | USD 369/mo + 527 · 1-mo min | 4,955 | 9,383 | 13,811 | 17,811.57 | Cart · final tax N/Q. Port, traffic and IPv4 unconfirmed. |
| 036 [Servers99, Falkenstein][q36] | 9454P · 128 / 2×3.84 | USD 369/mo + 1,496.35 | 5,924.35 | 10,352.35 | 14,780.35 | 19,061.70 | Cart · tax N/Q. |
| 037 [LeoServers, Falkenstein][q37] | 9454P · 128 / 2×3.84 | USD 370/mo + 1,496.35 | 5,936.35 | 10,376.35 | 14,816.35 | 19,108.13 | Cart · tax N/Q. |
| 038 [LeoServers, Helsinki][q38] | 9454P · 128 / 2×3.84 | USD 370/mo + 1,134.69 | 5,574.69 | 10,014.69 | 14,454.69 | 18,641.71 | Cart · tax N/Q. |
| 048 [XHN.ES, Finland][q48] | 9454P · 128 / 2×3.84 | EUR 380/mo + 99 | 4,659 | 9,219 | 13,779 | 19,533.11 | Cart · tax N/Q. Disk selector 3.98 TB vs description 3.84 TB. |
| 050 [EPY Host, Falkenstein][q50] | 9454P · 128 / 2×3.84 | USD 423/mo + N/Q | 5,076+ | 10,152+ | 15,228+ | 19,639.02+ | Cart · tax N/Q. |
| 052 [Servers99, Falkenstein][q52] | 9454P · 128 / 2×3.84 | USD 424/mo + N/Q | 5,088+ | 10,176+ | 15,264+ | 19,685.45+ | Cart · tax N/Q. |
| 054 [LeoServers, Falkenstein][q54] | 9454P · 128 / 2×3.84 | USD 425/mo + N/Q | 5,100+ | 10,200+ | 15,300+ | 19,731.88+ | Cart · tax N/Q. |
| 056 [GTZHost, Falkenstein][q56] | 9454P · 128 / 2×3.84 | USD 427/mo + N/Q | 5,124+ | 10,248+ | 15,372+ | 19,824.73+ | Cart · tax N/Q. ID verification. |
| 057 [iDatam, Falkenstein][q57] | 9454P · 128 / 2×3.84 | USD 427/mo + N/Q | 5,124+ | 10,248+ | 15,372+ | 19,824.73+ | Cart · tax N/Q. Cart and catalog DC references differ. |
| 058 [CTCServers, Falkenstein][q58] | 9454P · 128 / 2×3.84 | USD 428/mo + N/Q | 5,136+ | 10,272+ | 15,408+ | 19,871.16+ | Cart · tax N/Q. |
| 059 [KW Servers, Falkenstein/Nuremberg][q59] | 9454P · 128 / 2×3.84 | USD 429/mo + N/Q | 5,148+ | 10,296+ | 15,444+ | 19,917.59+ | Cart · tax N/Q. |
| 064 [Servers99, Nuremberg][q64] | 9454P · 128 / 2×3.84 | USD 432/mo + N/Q | 5,184+ | 10,368+ | 15,552+ | 20,056.87+ | Cart · tax N/Q. |
| 095 [IP-Projects, Frankfurt][q95] | 9980X · 128 / 2×4 | EUR 11,780.29/24 mo + 0 | 11,780.29 | 11,780.29 | 23,560.58 | 33,399.48 | Orderable in configurator · ex VAT. Two DIMMs. |
| 098 [IP-Projects, Frankfurt][q98] | 9980X · 128 / 2×4 | EUR 6,084.32/12 mo + 342.85 | 6,427.17 | 12,511.49 | 18,595.81 | 26,361.42 | Orderable in configurator · ex VAT. Two DIMMs. |
| 100 [IP-Projects, Frankfurt][q100] | 9980X · 128 / 2×4 | EUR 539.39/mo + 342.85 · 12-mo min | 6,815.53 | 13,288.21 | 19,760.89 | 28,013.04 | Orderable in configurator · ex VAT. Two DIMMs. |
| 103 [iTHOSTER AX162-S, Helsinki/Falkenstein][q103] | 9454P · 128 / 2×3.84 | USD 663/mo + 100 | 8,056 | 16,012 | 23,968 | 30,910.70 | Cart · tax N/Q. Region selection only. |
| 104 [Hetzner AX162-1, DE/FI][q104] | 9454P · 128 / 2×3.84 | EUR 612.30/mo + 304 | 7,651.60 | 14,999.20 | 22,346.80 | 31,678.82 | Official feed · ex VAT and IPv4. Allocation depends on region. |

## A2 only

These hosts have at least 256 GB RAM and can mirror 1.92 TB or more. Their quoted drives are below 3.84 TB each. Compare the 36-month SGD column with **S$15,466.87** for the Singapore office A2.

| Source row and rental offer | CPU · GB RAM / drives (TB) | Native rent per cycle + setup | 12 mo, native | 24 mo, native | 36 mo, native | 36 mo, S$ | Evidence and tax |
|---|---|---|---:|---:|---:|---:|---|
| 001 [UHost AX162-R, Helsinki][q1] | 9454P · 256 / 2×1.92 | USD 220/mo + 120 | 2,760 | 5,400 | 8,040 | 10,368.91 | Configurator · tax N/Q. Port, traffic and contracting entity unresolved. |
| 002 [Lindau AX162-R, DE/FI][q2] | 9454P · 256 / 2×1.92 | from USD 235.03/mo + N/Q · term N/Q | N/Q | N/Q | N/Q | N/Q | Listing · tax N/Q. Login required, merchant and stock unresolved. |
| 004 [PlusClouds / Radius AX162-R, FI/DE][q4] | 9454P · 256 / 2×1.92 | EUR 229/mo + 542 · term N/Q | 3,290 | 6,038 | 8,786 | 12,455.03 | Listing · ex VAT. General portal, no selected SKU. |
| 007 [BizoSiz AX162-R, DE/FI][q7] | 9454P · 256 / 2×1.92 | USD 279/mo + 111 | 3,459 | 6,807 | 10,155 | 13,096.55 | Cart · tax N/Q. Delivery queue and payment eligibility. |
| 013 [Provisov, Nuremberg][q13] | 9454P · 256 / 2×1.92 | USD 304/mo + 109 · term N/Q | 3,757 | 7,405 | 11,053 | 14,254.67 | Application form · tax N/Q. Traffic and allocation unresolved. |
| 015 [AMS SOFT AX162-R, Finland][q15] | 9454P · 256 / 2×1.92 | BRL 1,989.90/mo + N/Q | 23,878.80+ | 47,757.60+ | 71,636.40+ | 15,680.04+ | Cart total · tax N/Q. Due today equals one month’s rent. |
| 018 [Pro-m, Finland][q18] | 9454P · 256 / 2×1.92 | USD 347/mo + 697 · 1-mo min | 4,861 | 9,025 | 13,189 | 17,009.39 | Cart · final tax N/Q. Port, traffic and IPv4 unconfirmed. |
| 019 [Servers99, Helsinki][q19] | 9454P · 256 / 2×1.92 | USD 359/mo + 1,496.35 | 5,804.35 | 10,112.35 | 14,420.35 | 18,597.42 | Cart · tax N/Q. |
| 020 [BytesRack, Helsinki][q20] | 9454P · 256 / 2×1.92 | USD 360/mo + 1,496.35 | 5,816.35 | 10,136.35 | 14,456.35 | 18,643.85 | Cart · tax N/Q. |
| 022 [LeoServers, Helsinki][q22] | 9454P · 256 / 2×1.92 | USD 363/mo + 1,496.35 | 5,852.35 | 10,208.35 | 14,564.35 | 18,783.14 | Cart · tax N/Q. |
| 025 [KW Servers, Helsinki][q25] | 9454P · 256 / 2×1.92 | USD 364/mo + 1,496.35 | 5,864.35 | 10,232.35 | 14,600.35 | 18,829.56 | Cart · tax N/Q. |
| 032 [GTZHost, Helsinki][q32] | 9454P · 256 / 2×1.92 | USD 368/mo + 1,496.35 | 5,912.35 | 10,328.35 | 14,744.35 | 19,015.28 | Cart · tax N/Q. ID verification. |
| 035 [Pro-m, Germany][q35] | 9454P · 256 / 2×1.92 | USD 369/mo + 689 · 1-mo min | 5,117 | 9,545 | 13,973 | 18,020.49 | Cart · final tax N/Q. Port, traffic and IPv4 unconfirmed. |
| 039 [Servers99, Falkenstein][q39] | 9454P · 256 / 2×1.92 | USD 373/mo + 1,496.35 | 5,972.35 | 10,448.35 | 14,924.35 | 19,247.41 | Cart · tax N/Q. |
| 040 [LeoServers, Falkenstein][q40] | 9454P · 256 / 2×1.92 | USD 374/mo + 1,496.35 | 5,984.35 | 10,472.35 | 14,960.35 | 19,293.84 | Cart · tax N/Q. |
| 042 [CTCServers, Falkenstein][q42] | 9454P · 256 / 2×1.92 | USD 377/mo + 1,496.35 | 6,020.35 | 10,544.35 | 15,068.35 | 19,433.13 | Cart · tax N/Q. |
| 043 [KW Servers, Falkenstein][q43] | 9454P · 256 / 2×1.92 | USD 378/mo + 1,496.35 | 6,032.35 | 10,568.35 | 15,104.35 | 19,479.55 | Cart · tax N/Q. |
| 044 [GTZHost, Falkenstein][q44] | 9454P · 256 / 2×1.92 | USD 379/mo + 1,496.35 | 6,044.35 | 10,592.35 | 15,140.35 | 19,525.98 | Cart · tax N/Q. ID verification. |
| 045 [iDatam, Falkenstein][q45] | 9454P · 256 / 2×1.92 | USD 382/mo + 1,496.35 | 6,080.35 | 10,664.35 | 15,248.35 | 19,665.27 | Cart · tax N/Q. Cart and catalog DC references differ. |
| 046 [HostAddon HADE/HAFI, DE/FI][q46] | 9454P · 256 / 2×1.92 | USD 4,806/12 mo + 999 | 5,805 | 10,611 | 15,417 | 19,882.77 | Cart · tax N/Q. Base IPv4 price unresolved. |
| 049 [CTCServers, Falkenstein][q49] | 9454P · 256 / 2×1.92 | USD 423/mo + N/Q | 5,076+ | 10,152+ | 15,228+ | 19,639.02+ | Cart · tax N/Q. |
| 051 [EPY Host, Falkenstein][q51] | 9454P · 256 / 2×1.92 | USD 423/mo + N/Q | 5,076+ | 10,152+ | 15,228+ | 19,639.02+ | Cart · tax N/Q. |
| 055 [LeoServers, Falkenstein][q55] | 9454P · 256 / 2×1.92 | USD 425/mo + N/Q | 5,100+ | 10,200+ | 15,300+ | 19,731.88+ | Cart · tax N/Q. |
| 060 [iDatam, Falkenstein][q60] | 9454P · 256 / 2×1.92 | USD 429/mo + N/Q | 5,148+ | 10,296+ | 15,444+ | 19,917.59+ | Cart · tax N/Q. Cart and catalog DC references differ. |
| 061 [GTZHost, Falkenstein][q61] | 9454P · 256 / 2×1.92 | USD 431/mo + N/Q | 5,172+ | 10,344+ | 15,516+ | 20,010.45+ | Cart · tax N/Q. ID verification. |
| 062 [Servers99, Falkenstein][q62] | 9454P · 256 / 2×1.92 | USD 431/mo + N/Q | 5,172+ | 10,344+ | 15,516+ | 20,010.45+ | Cart · tax N/Q. |
| 063 [KW Servers, Nuremberg][q63] | 9454P · 256 / 2×1.92 | USD 432/mo + N/Q | 5,184+ | 10,368+ | 15,552+ | 20,056.87+ | Cart · tax N/Q. |
| 065 [Servers99, Nuremberg][q65] | 9454P · 256 / 2×1.92 | USD 432/mo + N/Q | 5,184+ | 10,368+ | 15,552+ | 20,056.87+ | Cart · tax N/Q. |
| 066 [KW Servers, Falkenstein][q66] | 9454P · 256 / 2×1.92 | USD 433/mo + N/Q | 5,196+ | 10,392+ | 15,588+ | 20,103.30+ | Cart · tax N/Q. |
| 080 [HostAddon HADE/HAFI, DE/FI][q80] | 9454P · 256 / 2×1.92 | USD 444.99/mo + 999 | 6,338.88 | 11,678.76 | 17,018.64 | 21,948.35 | Cart · tax N/Q. Base IPv4 price unresolved. |
| 085 [19CLOUDS DEDI-AX162, Falkenstein][q85] | 9454P · 256 / 2×1.92 | EUR 418/mo + 55.57 | 5,071.57 | 10,087.57 | 15,103.57 | 21,410.82 | Cart · tax N/Q. Traffic and IP costs unresolved. |
| 101 [0DayHost, Amsterdam][q101] | 9455P · 256 / 2×2 | USD 650/mo + N/Q · term N/Q | N/Q | N/Q | N/Q | N/Q | Quote only · tax N/Q. Contact-based order. |

## Both A1 and A2

Both advertised configurations have 256 GB RAM and at least two 3.84 TB drives. Lindau lists four drives, enabling a 3.84 TB mirrored pair under a suitable configuration. The selected array layout and checkout price remain unresolved.

| Source row and rental offer | CPU · GB RAM / drives (TB) | Native rent per cycle + setup | 12 mo, native | 24 mo, native | 36 mo, native | 36 mo, S$ | Evidence and tax |
|---|---|---|---:|---:|---:|---:|---|
| 003 [Lindau AX162-S, DE/FI][q3] | 9454P · 256 / 4×3.84 | from USD 236.41/mo + N/Q · term N/Q | N/Q | N/Q | N/Q | N/Q | Listing · tax N/Q. Four drives advertised, layout and merchant unresolved. |
| 087 [PowerDedi, Amsterdam/Frankfurt][q87] | 9454P · 256 / 2×3.84 | USD 489/mo + 0 | 5,868 | 11,736 | 17,604 | 22,703.27 | Cart · tax N/Q. Amsterdam selected, Frankfurt advertised. Crypto balance, operator on invoice. |

## Neither A1 nor A2

All 38 offers have 128 GB RAM and lack a pair of drives of at least 3.84 TB. Some meet the original repository’s 2 TB **raw** minimum with one drive or a smaller pair. Their pricing is relevant if the job’s actual per-host RAM or mirrored working-set requirement is lower.

| Source row and rental offer | CPU · GB RAM / drives (TB) | Native rent per cycle + setup | 12 mo, native | 24 mo, native | 36 mo, native | 36 mo, S$ | Evidence and tax |
|---|---|---|---:|---:|---:|---:|---|
| 009 [NineHost AX162-R, FRA selected][q9] | 9454P · 128 / 2×1.92 | USD 279.90/mo + N/Q | 3,358.80+ | 6,717.60+ | 10,076.40+ | 12,995.18+ | Cart · tax extra. Region selection only, dedicated refund exclusions. |
| 010 [ENTRONYX TITAN-96, Helsinki][q10] | 9455 · 128 / 2×1.92 | EUR 6,226.32/24 mo + 0 | 6,226.32 | 6,226.32 | 12,452.64 | 17,652.86 | Listing · ex VAT. B2B, historical demonstration notice, static stock field. |
| 011 [ENTRONYX TITAN-96, Helsinki][q11] | 9455 · 128 / 2×1.92 | EUR 3,214.68/12 mo + 0 | 3,214.68 | 6,429.36 | 9,644.04 | 13,671.39 | Listing · ex VAT. B2B, historical demonstration notice, static stock field. |
| 012 [Nexia AX162-R, FRA selected][q12] | 9454P · 128 / 2×1.92 | USD 299.90/mo + N/Q | 3,598.80+ | 7,197.60+ | 10,796.40+ | 13,923.74+ | Cart · tax extra. Region selection only, legal identity unresolved. |
| 014 [ENTRONYX TITAN-96, Helsinki][q14] | 9455 · 128 / 2×1.92 | EUR 281.99/mo + 299.99 | 3,683.87 | 7,067.75 | 10,451.63 | 14,816.23 | Listing · ex VAT. B2B, historical demonstration notice, static stock field. |
| 021 [Introserv DC4RXL AE9455, FR/CA][q21] | 9455 · 128 / 2×1.92 | EUR 329.99/mo + 329.99 · 1-mo min | 4,289.87 | 8,249.75 | 12,209.63 | 17,308.37 | Listing · ex VAT. Inconsistent retrieval, including 404s. |
| 041 [HSTQ, Paris][q41] | 9455 · 128 / 2×1.92 | USD 13,473/36 mo + 0 | 13,473 | 13,473 | 13,473 | 17,375.66 | Cart · tax N/Q. Paris is seller-stated. |
| 047 [NetVO, France][q47] | 9455 · 128 / 2×1.92 | USD 4,949.99/12 mo + N/Q | 4,949.99+ | 9,899.98+ | 14,849.97+ | 19,151.49+ | Cart · tax extra if applicable. |
| 053 [HSTQ, Paris][q53] | 9455 · 128 / 2×1.92 | USD 10,179.60/24 mo + 0 | 10,179.60 | 10,179.60 | 20,359.20 | 26,256.55 | Cart · tax N/Q. Paris is seller-stated. |
| 067 [CrockyHost Pro 10, Europe][q67] | 9455 · 128 / 2×1.9 | EUR 9,475/24 mo + 0 | 9,475 | 9,475 | 18,950 | 26,863.52 | Cart · ex VAT. Country and city unconfirmed. |
| 068 [NetVO, France][q68] | 9455 · 128 / 2×1.92 | USD 434.99/mo + 435 | 5,654.88 | 10,874.76 | 16,094.64 | 20,756.70 | Cart · tax extra if applicable. |
| 069 [Fit Servers, Gravelines][q69] | 9455 · 128 / 2×1.92 | USD 438/mo + 708 | 5,964 | 11,220 | 16,476 | 21,248.52 | Cart · tax N/Q. Selected CPU is the non-P 9455. |
| 070 [KW Servers, Gravelines][q70] | 9455 · 128 / 2×1.92 | USD 438/mo + 708 | 5,964 | 11,220 | 16,476 | 21,248.52 | Cart · tax N/Q. |
| 071 [Servers99, Strasbourg][q71] | 9455P · 128 / 2×1.92 | USD 438/mo + 708 | 5,964 | 11,220 | 16,476 | 21,248.52 | Cart · tax N/Q. |
| 072 [KW Servers, Warsaw][q72] | 9455P · 128 / 2×1.92 | USD 439/mo + 708 | 5,976 | 11,244 | 16,512 | 21,294.95 | Cart · tax N/Q. |
| 073 [iRexta, Strasbourg][q73] | 9455P · 128 / 2×1.92 | USD 439/mo + 708 | 5,976 | 11,244 | 16,512 | 21,294.95 | Cart · tax N/Q. |
| 074 [inSave Compute 48, FR/CA/PL/DE][q74] | 9455 · 128 / 2×1.92 | USD 439/mo + 439 | 5,707 | 10,975 | 16,243 | 20,948.03 | Cart · VAT extra if applicable. Region selection only. |
| 075 [Unihost OVE-X8, FR/PL/CA][q75] | 9455 · 128 / 2×1.92 | EUR 399.90/mo + 299.90 · term N/Q | 5,098.70 | 9,897.50 | 14,696.30 | 20,833.47 | Range listing · ex VAT. No SKU-specific order result. |
| 076 [Servers99, Gravelines][q76] | 9455 · 128 / 2×1.92 | USD 440/mo + 708 | 5,988 | 11,268 | 16,548 | 21,341.38 | Cart · tax N/Q. |
| 077 [Servers99, Roubaix][q77] | 9455 · 128 / 2×1.92 | USD 441/mo + 708 | 6,000 | 11,292 | 16,584 | 21,387.81 | Cart · tax N/Q. |
| 078 [KW Servers, Roubaix][q78] | 9455 · 128 / 2×1.92 | USD 442/mo + 708 | 6,012 | 11,316 | 16,620 | 21,434.24 | Cart · tax N/Q. |
| 079 [Servers99, Warsaw][q79] | 9455P · 128 / 2×1.92 | USD 444/mo + 708 | 6,036 | 11,364 | 16,692 | 21,527.09 | Cart · tax N/Q. |
| 081 [KW Servers, Strasbourg][q81] | 9455P · 128 / 2×1.92 | USD 448/mo + 708 | 6,084 | 11,460 | 16,836 | 21,712.80 | Cart · tax N/Q. |
| 082 [LeoServers, Gravelines][q82] | 9455 · 128 / 2×1.92 | USD 448/mo + 708 | 6,084 | 11,460 | 16,836 | 21,712.80 | Cart · tax N/Q. |
| 083 [HSTQ, Paris][q83] | 9455 · 128 / 2×1.92 | USD 5,389.20/12 mo + 0 | 5,389.20 | 10,778.40 | 16,167.60 | 20,850.79 | Cart · tax N/Q. Paris is seller-stated. |
| 084 [CrockyHost Pro 10, Europe][q84] | 9455 · 128 / 2×1.9 | EUR 4,990/12 mo + 0 | 4,990 | 9,980 | 14,970 | 21,221.47 | Cart · ex VAT. Country and city unconfirmed. |
| 086 [Gokiebox DEDICADO XL, CA/FR][q86] | 9455 · 128 / 2×1.92 | USD 484/mo + 357 | 6,165 | 11,973 | 17,781 | 22,931.54 | Configurator · ex IGV where applicable. Region selection only. |
| 088 [HSTQ, Paris][q88] | 9455 · 128 / 2×1.92 | USD 499/mo + 0 | 5,988 | 11,976 | 17,964 | 23,167.55 | Cart · tax N/Q. Paris is seller-stated. |
| 089 [IP-Projects, Frankfurt][q89] | 9980X · 128 / 1×2 | EUR 11,109.13/24 mo + 0 | 11,109.13 | 11,109.13 | 22,218.26 | 31,496.61 | Orderable in configurator · ex VAT. Two DIMMs. |
| 090 [CrockyHost Pro 10, Europe][q90] | 9455 · 128 / 2×1.9 | EUR 468/mo + 300 | 5,916 | 11,532 | 17,148 | 24,309.00 | Cart · ex VAT. Country and city unconfirmed. |
| 091 [Evolushost, Vienna][q91] | 9454P · 128 / 2×1 | EUR 5,640/12 mo + N/Q | 5,640+ | 11,280+ | 16,920+ | 23,985.79+ | Built to order · VAT included. Quoted 1–10 working days. |
| 092 [IP-Projects, Frankfurt][q92] | 9980X · 128 / 2×2 | EUR 11,305.51/24 mo + 0 | 11,305.51 | 11,305.51 | 22,611.02 | 32,053.38 | Orderable in configurator · ex VAT. Two DIMMs. |
| 093 [Evolushost, Vienna][q93] | 9454P · 128 / 2×1 | EUR 480/mo + 99.99 | 5,859.99 | 11,619.99 | 17,379.99 | 24,637.87 | Built to order · VAT included. Quoted 1–10 working days. |
| 094 [IP-Projects, Frankfurt][q94] | 9980X · 128 / 2×2 | EUR 5,839.12/12 mo + 342.85 | 6,181.97 | 12,021.09 | 17,860.21 | 25,318.63 | Orderable in configurator · ex VAT. Two DIMMs. |
| 096 [HostX DS-3, Germany][q96] | 9454P · 128 / 2×1.9 | EUR 499/mo + 1,999 · 12-mo min | 7,987 | 13,975 | 19,963 | 28,299.55 | Quote only · ex VAT. Managed, 15 TB, best-effort port. |
| 097 [TLFHost Enterprise 128GB, FR/DE][q97] | 9455 · 128 / 2×1.92 | USD 549/mo + 540 | 7,128 | 13,716 | 20,304 | 26,185.36 | Cart · tax N/Q. Delivery conditional. |
| 099 [IP-Projects, Frankfurt][q99] | 9980X · 128 / 2×2 | EUR 517.65/mo + 342.85 · 12-mo min | 6,554.65 | 12,766.45 | 18,978.25 | 26,903.57 | Orderable in configurator · ex VAT. Two DIMMs. |
| 102 [IP-Projects, Frankfurt][q102] | 9985WX · 128 / 2×2 | EUR 14,263.82/24 mo + 0 | 14,263.82 | 14,263.82 | 28,527.64 | 40,440.78 | Orderable in configurator · ex VAT. Two DIMMs. |

## Other sites, billing choices and exclusions in the research logs

The 104-row total follows the canonical rental table at the frozen initial commit. Its notes also record the following material alternatives. They use the same calculation rules when substituted for a main-row price. The subsequent 15 additions are recorded separately in [file 08](08-latest-rental-comparisons.md).

| Source rows | Alternative recorded in the supporting evidence |
|---|---|
| 001, 023 · UHost | Falkenstein adds USD 4/month to either Helsinki plan. The regular prices exclude a generic new-customer promotion with unverified eligibility and renewal terms. [Global evidence](../2026-11-19-global.md) |
| 010, 011, 014 · ENTRONYX | Frankfurt/Düsseldorf list EUR 299.99/mo + 299.99, EUR 3,419.88/12 months prepaid + 0, or EUR 6,623.76/24 months prepaid + 0. The business-only listings have the same historical supply concern. [Regional pricing](../2026-11-19-performance-pricing.md#entronyx-titan-96-current-advertised-configuration-with-unverified-allocation) |
| 015, 016 · AMS SOFT | German R/S carts both show BRL 2,099.90/mo, setup line absent. At 36 months the rent alone is BRL 75,596.40 or S$16,546.82. Finland and Germany are distinct tariffs. [Country-specific carts](../2026-11-20-latin-america.md#ams-soft) |
| 046, 080 · HostAddon | The six-month option is USD 436.10/mo equivalent, USD 2,616.60 rent per term + 999 setup. A separate Finland SKU shows the same rates. [HostAddon options](../2026-11-19-global.md#additional-public-configurations-recovered-using-anonymous-sessions-19-november) |
| 048 · XHN.ES | Finland EUR 1,140/quarter + 79, 2,280/half-year + 59, or 4,560/year with setup N/Q (no line). Germany adds EUR 7/mo on monthly billing. [Disk selector and terms](../2026-11-20-exact-cpu.md#regional-providers) |
| 019–082 · Regional reseller carts | Several offer annual billing at 12 times monthly rent with the same specified setup. Nuremberg/Falkenstein copies can share terms. Their dated records include regional price variants and the evidence of possible common supply. [Exact-CPU carts](../2026-11-20-exact-cpu.md) · [Other carts and datacenter references](../2026-11-20-newer-cpu.md) · [CTCServers and EPY Host](../2026-11-19-europe.md#falkenstein-carts-recovered-from-two-additional-sellers) |
| 067, 084, 090 · CrockyHost | EUR 1,342/quarter + 300 or EUR 2,527/half-year + 300, ex VAT. The selected 2 × 1.9 TB drives remain below both owned capacity profiles at 128 GB. [Cycle invoices](../2026-11-20-newer-cpu.md#new-qualifying-sellers-and-offers) |
| 074, 097 · inSave and TLFHost | Prepaid annual rent is USD 5,268 at inSave and USD 6,588 at TLFHost, both with setup waived. The main rows price monthly billing. [Selected billing options](../2026-11-19-global.md#additional-public-configurations-recovered-using-anonymous-sessions-19-november) |
| 091, 093 · Evolushost | EUR 1,428/quarter + 75 or EUR 2,840/half-year + 50, gross as displayed. Quoted build-to-order, 100 TB description versus selected 150 TB fair use. [Vienna configurations](../2026-11-19-europe.md#additional-verified-public-configurators) |
| 089–102 · IP-Projects | The 9980X monthly 2 × 2 TB and 2 × 4 TB rates can also carry a 24-month minimum and explicit zero setup, with rent collected monthly. Their minimum contractual rents are EUR 12,423.60 and EUR 12,945.36 respectively. This option differs from paying the full two-year invoice on day one. The pricing audit also records annual billing on two-year terms and further drive combinations. [Full contract and drive matrices](../2026-11-19-performance-pricing.md#ip-projects-configurations) |
| 104 · Hetzner and the separate A2 reference | AX162-1 has its own USD tariff of 722.10/mo + 359. Regular AX162-2 (256 GB / 2 × 1.92 TB) is EUR 842.30/mo + 419 or USD 992.10/mo + 494. Both exclude tax and IPv4. Use the billed currency. The A2 reference is an additional benchmark outside the 104-row inventory. [Native EUR and USD tariffs](../2026-11-19.md#hetzner-reference-and-limited-stock-variants) |

**Singapore and Malaysia.** The source-table PowerDedi row prices Amsterdam/Frankfurt. Its separately advertised Singapore location has conflicting fulfillment evidence. NineHost and Nexia selected FRA, with unverified geographic alternatives. Singapore KW Servers, Servers99 and iHoster appear in the watchlist at USD 546, 549 and 574.35/month. Their descriptions specify 384 GB, a single 2 TB drive and 48 cores/48 threads. Each misses the mirrored-disk floor, and the enabled SMT configuration remains unresolved. The regional report covers the separate Singapore and Malaysia candidates, colocation terms, and network and delivery constraints. [Singapore CPU and inventory evidence](../2026-11-20-global.md#exact-cpu-offers-with-a-thread-count-discrepancy) · [KW Servers Singapore](../2026-11-20-exact-cpu.md#kw-servers-leoservers-and-servers99) · [Regional comparison](02-rental-market.md)

**Historical and excluded leads.** The dated logs retain unavailable OVH/Kimsufi RISE-XL, OneProvider, Evolushost Berlin, iWebFusion clearance and Hetzner LTD, unpriced disk upgrades, DDR4 descriptions incompatible with the advertised 9454P, and CPUs with conflicting throughput and per-thread results such as 9355P and 9654. Incorporating these as purchasable quotes would require new evidence on the specific blocker. More expensive and customer-conditional options, including the 9475F, remain documented for a workload or service requirement that justifies their premium. [Historical audit and corrections](../2026-11-19.md) · [European exclusions](../2026-11-19-europe.md) · [Global exclusions](../2026-11-19-global.md) · [Latest exclusions](../2026-11-20.md#root-level-exclusions-and-unresolved-leads) · [Newer CPU evidence](../2026-11-20-newer-cpu.md#additional-configurations-with-material-conditions)

[snapshot]: https://github.com/tailrocks/dedicated-servers-providers/blob/07180f43068a8de01ae30c41a265ec16ef1f138b/README.md?plain=1#L23-L142
[method]: https://github.com/tailrocks/dedicated-servers-providers/blob/07180f43068a8de01ae30c41a265ec16ef1f138b/METHODOLOGY.md
[sgdfx]: https://data-api.ecb.europa.eu/service/data/EXR/D.SGD.EUR.SP00.A?startPeriod=2026-11-19&endPeriod=2026-11-19&format=csvdata
[usdfx]: https://data-api.ecb.europa.eu/service/data/EXR/D.USD.EUR.SP00.A?startPeriod=2026-11-19&endPeriod=2026-11-19&format=csvdata
[brlfx]: https://data-api.ecb.europa.eu/service/data/EXR/D.BRL.EUR.SP00.A?startPeriod=2026-11-19&endPeriod=2026-11-19&format=csvdata
[q1]: https://uhost.online/en/dedicated/19
[q2]: https://www.lindau.cloud/en/products/31
[q3]: https://www.lindau.cloud/en/products/32
[q4]: https://plusclouds.com/servers
[q5]: https://plusclouds.com/servers
[q6]: https://hummingtribe.com/dedicated
[q7]: https://my.bizosiz.com/cart.php?a=add&pid=30&currency=1
[q8]: https://my.bizosiz.com/cart.php?a=add&pid=31&currency=1
[q9]: https://ninehost.net/cart?plan=AX162-R
[q10]: https://entronyx.cloud/en/bare-metal/titan
[q11]: https://entronyx.cloud/en/bare-metal/titan
[q12]: https://nexia.host/cart?plan=AX162-R
[q13]: https://www.provisov.net/services/arenda-serverov/
[q14]: https://entronyx.cloud/en/bare-metal/titan
[q15]: https://loja.amssoft.com.br/cart.php?a=add&pid=10102&billingcycle=monthly
[q16]: https://loja.amssoft.com.br/cart.php?a=add&pid=10099&billingcycle=monthly
[q17]: https://my.pro-m.org/products/dedicated/ded-fi-030/checkout?plan=95&options%5B1%5D=2
[q18]: https://my.pro-m.org/products/dedicated/ded-fi-028/checkout?plan=83&options%5B1%5D=2
[q19]: https://www.servers99.com/billing/cart.php?a=add&pid=30134&carttpl=new-theme-cart
[q20]: https://www.bytesrack.com/billing/cart.php?a=add&carttpl=bytesrack_cart&pid=26509
[q21]: https://introserv.com/order/dc4rxl-ae9455/
[q22]: https://www.leoservers.com/billing/cart.php?a=add&pid=49693&carttpl=newleocart
[q23]: https://uhost.online/en/dedicated/20
[q24]: https://www.ctcservers.com/billing/cart.php?a=add&pid=50636
[q25]: https://www.kwservers.com/billing/cart.php?a=add&pid=29123&carttpl=kw_cart
[q26]: https://billing.idatam.com/cart.php?a=add&pid=35662
[q27]: https://www.gtzhost.com/billing/cart.php?a=add&pid=62898&carttpl=gtz-new-cart
[q28]: https://www.servers99.com/billing/cart.php?a=add&pid=30133&carttpl=new-theme-cart
[q29]: https://www.bytesrack.com/billing/cart.php?a=add&carttpl=bytesrack_cart&pid=26508
[q30]: https://www.gtzhost.com/billing/cart.php?a=add&pid=62907&carttpl=gtz-new-cart
[q31]: https://www.kwservers.com/billing/cart.php?a=add&pid=29131&carttpl=kw_cart
[q32]: https://www.gtzhost.com/billing/cart.php?a=add&pid=62899&carttpl=gtz-new-cart
[q33]: https://www.kwservers.com/billing/cart.php?a=add&pid=29122&carttpl=kw_cart
[q34]: https://my.pro-m.org/products/dedicated/ded-de-029/checkout?plan=91&options%5B1%5D=3
[q35]: https://my.pro-m.org/products/dedicated/ded-de-027/checkout?plan=75&options%5B1%5D=3
[q36]: https://www.servers99.com/billing/cart.php?a=add&pid=30142&carttpl=new-theme-cart
[q37]: https://www.leoservers.com/billing/cart.php?a=add&pid=49701&carttpl=newleocart
[q38]: https://www.leoservers.com/billing/cart.php?a=add&pid=49692&carttpl=newleocart
[q39]: https://www.servers99.com/billing/cart.php?a=add&pid=30143&carttpl=new-theme-cart
[q40]: https://www.leoservers.com/billing/cart.php?a=add&pid=49702&carttpl=newleocart
[q41]: https://cp.hstq.net/cart.php?a=add&language=english&pid=94
[q42]: https://www.ctcservers.com/billing/cart.php?a=add&pid=50637
[q43]: https://www.kwservers.com/billing/cart.php?a=add&pid=29132&carttpl=kw_cart
[q44]: https://www.gtzhost.com/billing/cart.php?a=add&pid=62908&carttpl=gtz-new-cart
[q45]: https://billing.idatam.com/cart.php?a=add&pid=35663
[q46]: https://www.hostaddon.com/clients/cart.php?a=add&pid=1519
[q47]: https://netvo.io/cart.php?a=add&pid=66
[q48]: https://www.xhn.es/clientes/cart.php?a=add&pid=85
[q49]: https://www.ctcservers.com/billing/cart.php?a=add&pid=60206
[q50]: https://billing.epyhost.com/cart.php?a=add&pid=46715
[q51]: https://billing.epyhost.com/cart.php?a=add&pid=46716
[q52]: https://www.servers99.com/billing/cart.php?a=add&pid=39713&carttpl=new-theme-cart
[q53]: https://cp.hstq.net/cart.php?a=add&language=english&pid=94
[q54]: https://www.leoservers.com/billing/cart.php?a=add&pid=59272&carttpl=newleocart
[q55]: https://www.leoservers.com/billing/cart.php?a=add&pid=59273&carttpl=newleocart
[q56]: https://www.gtzhost.com/billing/cart.php?a=add&pid=72477&carttpl=gtz-new-cart
[q57]: https://billing.idatam.com/cart.php?a=add&pid=45243
[q58]: https://www.ctcservers.com/billing/cart.php?a=add&pid=60205
[q59]: https://www.kwservers.com/billing/cart.php?a=add&pid=38700&carttpl=kw_cart
[q60]: https://billing.idatam.com/cart.php?a=add&pid=45244
[q61]: https://www.gtzhost.com/billing/cart.php?a=add&pid=72478&carttpl=gtz-new-cart
[q62]: https://www.servers99.com/billing/cart.php?a=add&pid=39714&carttpl=new-theme-cart
[q63]: https://www.kwservers.com/billing/cart.php?a=add&pid=38693&carttpl=kw_cart
[q64]: https://www.servers99.com/billing/cart.php?a=add&pid=39705&carttpl=new-theme-cart
[q65]: https://www.servers99.com/billing/cart.php?a=add&pid=39706&carttpl=new-theme-cart
[q66]: https://www.kwservers.com/billing/cart.php?a=add&pid=38701&carttpl=kw_cart
[q67]: https://crocky.host/cart.php?a=add&pid=112&billingcycle=biennially
[q68]: https://netvo.io/cart.php?a=add&pid=66
[q69]: https://www.fitservers.com/billing/cart.php?a=add&pid=52359
[q70]: https://www.kwservers.com/billing/cart.php?a=add&pid=30165&carttpl=kw_cart
[q71]: https://www.servers99.com/billing/cart.php?a=add&pid=31178&carttpl=new-theme-cart
[q72]: https://www.kwservers.com/billing/cart.php?a=add&pid=30168&carttpl=kw_cart
[q73]: https://my.irexta.com/cart.php?a=add&pid=33570
[q74]: https://my.insave.hosting/cart.php?a=add&pid=321&billingcycle=monthly&currency=1&language=english
[q75]: https://unihost.com/dedicated/epyc/
[q76]: https://www.servers99.com/billing/cart.php?a=add&pid=31176&carttpl=new-theme-cart
[q77]: https://www.servers99.com/billing/cart.php?a=add&pid=45070&carttpl=new-theme-cart
[q78]: https://www.kwservers.com/billing/cart.php?a=add&pid=44060&carttpl=kw_cart
[q79]: https://www.servers99.com/billing/cart.php?a=add&pid=31179&carttpl=new-theme-cart
[q80]: https://www.hostaddon.com/clients/cart.php?a=add&pid=1519
[q81]: https://www.kwservers.com/billing/cart.php?a=add&pid=30167&carttpl=kw_cart
[q82]: https://www.leoservers.com/billing/cart.php?a=add&pid=50735&carttpl=newleocart
[q83]: https://cp.hstq.net/cart.php?a=add&language=english&pid=94
[q84]: https://crocky.host/cart.php?a=add&pid=112&billingcycle=annually
[q85]: https://clients.19clouds.com/cart.php?a=add&pid=134
[q86]: https://app.gokiebox.com/carrito/agregar/237?moneda=USD
[q87]: https://powerdedi.com/order?plan=e-9454p
[q88]: https://cp.hstq.net/cart.php?a=add&language=english&pid=94
[q89]: https://www.ip-projects.de/en/order/dedicated-server/amd-str5-l-g1
[q90]: https://crocky.host/cart.php?a=add&pid=112&billingcycle=monthly
[q91]: https://dash.evolushost.com/cart.php?a=add&pid=3895
[q92]: https://www.ip-projects.de/en/order/dedicated-server/amd-str5-l-g1
[q93]: https://dash.evolushost.com/cart.php?a=add&pid=3895
[q94]: https://www.ip-projects.de/en/order/dedicated-server/amd-str5-l-g1
[q95]: https://www.ip-projects.de/en/order/dedicated-server/amd-str5-l-g1
[q96]: https://www.hostx.eu/dedicated-servers/
[q97]: https://my.tlfhost.com/store/france-dedicated-servers/enterprise-dedicated-128gb
[q98]: https://www.ip-projects.de/en/order/dedicated-server/amd-str5-l-g1
[q99]: https://www.ip-projects.de/en/order/dedicated-server/amd-str5-l-g1
[q100]: https://www.ip-projects.de/en/order/dedicated-server/amd-str5-l-g1
[q101]: https://0dayhost.com/amsterdam-dedicated-servers.php
[q102]: https://www.ip-projects.de/en/order/dedicated-server/amd-str5-xl-g1
[q103]: https://client.ithoster.com/store/dedicated-server/ax162-s
[q104]: https://www.hetzner.com/dedicated-rootserver/ax162/configurator/
