# Fifteen additional rentals against the Singapore hardware options

**Progressive Robot is the only new seller with a stated setup fee whose rent falls below the expanded Singapore ownership budgets at 36 months.** Its A1 and A2 offers both list GBP 221/month plus GBP 88 setup. That is **S$13,643.26 over 36 months** at the dated FX. The direct purchase budget with server electricity and internet is lower by S$86.16 for A1 and S$367.76 for A2. The expanded ownership budgets are higher by S$2,130.55 and S$1,823.61, respectively. These small direct-budget gaps make final tax and other fees material. The order path reached domain selection, with deployment country, minimum commitment, final checkout and physical stock unresolved. [Progressive Robot catalog and ordering evidence](../2026-11-20-follow-up-global.md#progressive-robot)

The 20 November 2026 repository follow-up adds **15 offers from nine brands** to the original 104, for **119 rental rows across 47 alternative brands plus Hetzner**. The following IDs, N01–N15, follow the order of the additions in the pinned main table. The original 001–104 IDs and figures remain available in the [104-offer rental comparison](05-repository-rental-comparison.md) and [104-offer break-even appendix](07-all-rentals-break-even.md). The calculations here use the recorded November primary-source checks. The follow-up took place on 19 November UTC, 20 November in Vietnam. [Pinned 119-row source][snapshot] · [Dated follow-up](../2026-11-20-follow-up.md)

| Single-host capacity fit | Original 104 | New 15 | All 119 |
|---|---:|---:|---:|
| A1 only · at least 128 GB and two drives of at least 3.84 TB each | 32 | 3 | 35 |
| A2 only · at least 256 GB and two drives of at least 1.92 TB each | 32 | 7 | 39 |
| Both profiles | 2 | 0 | 2 |
| Neither profile | 38 | 5 | 43 |
| **Distinct offers** | **104** | **15** | **119** |

Across the full inventory, 76 distinct rows fit at least one profile. Counting the two dual-profile offers for each relevant purchase produces 37 A1 and 41 A2 comparisons. Capacity screening uses the individual drives’ nominal mirrored size. Actual array configuration, endurance, memory platform and service levels still matter. The ten new capacity matches list the exact EPYC 9454P. Actual CI performance still needs a workload replay. None of the 15 additions establishes a Singapore or Malaysian deployment. The regional report covers those locations. [CI replay](04-validation-and-procurement.md) · [Regional rental comparison](02-rental-market.md)

## Native invoices and Singapore-dollar cash budgets

Each horizon cell gives **native currency / Singapore dollars**, for example `2,740 / 4,647.26` in a GBP row. `+` means the figure is **rent alone** and the payable total is **N/Q** because setup was undisclosed. These rent subtotals assume the listed tariff continues. Six new offers have unknown setup, including IT-24’s two selected configurators. Nine publish an amount or explicitly waive setup. Across all 119 rows, 87 have stated setup and 32 have unknown setup. Taxes follow each seller’s recorded basis below.

The model counts each required invoice in full, then adds setup once. A monthly schedule uses `months × rent + setup`. A prepaid schedule uses `ceil(months / months per invoice) × actual invoice + setup`. All three horizons here are exact multiples of AmazingRDP’s annual term. Extending service assumes the same tariff and cycle are obtainable again. An undisclosed contractual minimum or fee can increase the liability. FX is fixed on **19 November 2026** at EUR 1 = SGD 1.4176 = USD 1.0992 = GBP 0.83581. The calculations use `GBP × 1.4176 / 0.83581` or `USD × 1.4176 / 1.0992`. EUR uses `× 1.4176`. FX is rounded only for display. GBP is the documented tariff for both Progressive Robot SKUs. [ECB GBP][gbpfx] · [ECB SGD][sgdfx] · [ECB USD][usdfx]

| ID and recorded offer | CPU · GB RAM / drives (TB each unless shown) | Fit | Native rent + one-time setup | 12 mo, native / S$ | 24 mo, native / S$ | 36 mo, native / S$ |
|---|---|---|---|---:|---:|---:|
| N01 [Nindohost 256 GB, Germany][N01] | 9454P · 256 / 2×1.92 | A2 | USD 234/mo + N/Q | 2,808+ / 3,621.38+ | 5,616+ / 7,242.76+ | 8,424+ / 10,864.14+ |
| N02 [Progressive Robot AX162-R][N02] | 9454P · 256 / 2×1.92 | A2 | GBP 221/mo + 88 | 2,740 / 4,647.26 | 5,392 / 9,145.26 | 8,044 / 13,643.26 |
| N03 [Progressive Robot AX162-S][N03] | 9454P · 128 / 2×3.84 | A1 | GBP 221/mo + 88 | 2,740 / 4,647.26 | 5,392 / 9,145.26 | 8,044 / 13,643.26 |
| N04 [PowerVPS.net 9454P, DE/FI][N04] | 9454P · 256 / 2×2 | A2 | USD 320/mo + N/Q | 3,840+ / 4,952.31+ | 7,680+ / 9,904.63+ | 11,520+ / 14,856.94+ |
| N05 [IT-24 AX162-R][N05] | 9454P · 256 / 2×1.92 | A2 | USD 341.93/mo + N/Q | 4,103.16+ / 5,291.70+ | 8,206.32+ / 10,583.41+ | 12,309.48+ / 15,875.11+ |
| N06 [IT-24 AX162-S][N06] | 9454P · 128 / 2×3.84 | A1 | USD 341.93/mo + N/Q | 4,103.16+ / 5,291.70+ | 8,206.32+ / 10,583.41+ | 12,309.48+ / 15,875.11+ |
| N07 [Faciotech Enterprise Metal, Germany][N07] | 9454P · 256 / 2×1.92 | A2 | USD 389/mo + 0 | 4,668 / 6,020.16 | 9,336 / 12,040.31 | 14,004 / 18,060.47 |
| N08 [PowerVPS.net 9455, France][N08] | 9455 · 128 / 2×2 | Neither | USD 405/mo + N/Q | 4,860+ / 6,267.77+ | 9,720+ / 12,535.55+ | 14,580+ / 18,803.32+ |
| N09 [AmazingRDP Ultra, Europe, annual][N09] | 9454P · 256 / 2×1.92 | A2 | USD 5,400/12 mo prepaid + 0 | 5,400 / 6,964.19 | 10,800 / 13,928.38 | 16,200 / 20,892.58 |
| N10 [Nindohost 128 GB, Germany][N10] | 9454P · 128 / 2×3.84 | A1 | USD 450/mo + N/Q | 5,400+ / 6,964.19+ | 10,800+ / 13,928.38+ | 16,200+ / 20,892.58+ |
| N11 [Good-host.net 9455, Gravelines][N11] | 9455 · 128 / 2×1.9 | Neither | EUR 434.99/mo + 389.99 | 5,609.87 / 7,952.55 | 10,829.75 / 15,352.25 | 16,049.63 / 22,751.96 |
| N12 [AmazingRDP Ultra, Europe, monthly][N12] | 9454P · 256 / 2×1.92 | A2 | USD 499.99/mo + 0 | 5,999.88 / 7,737.84 | 11,999.76 / 15,475.67 | 17,999.64 / 23,213.51 |
| N13 [XDLHOST DX182, Finland][N13] | 9454P · 128 / 1×1,024 GB + 1×1 TB | Neither | EUR 470.60/mo + 2,180 | 7,827.20 / 11,095.84 | 13,474.40 / 19,101.31 | 19,121.60 / 27,106.78 |
| N14 [JHCloud.ai 9455P, Montreal][N14] | 9455P · 128 / 2×1.92 | Neither | USD 643.99/mo + 0 | 7,727.88 / 9,966.38 | 15,455.76 / 19,932.76 | 23,183.64 / 29,899.13 |
| N15 [JHCloud.ai 9455P, Lille/Warsaw][N15] | 9455P · 128 / 2×1.92 | Neither | USD 663.42/mo + 0 | 7,961.04 / 10,267.08 | 15,922.08 / 20,534.15 | 23,883.12 / 30,801.23 |

## Direct hardware break-even in months

A1 costs **S$8,891.00** for a Samsung-equipped 5995WX with 128 GB and two 4 TB drives. A2 costs **S$8,609.40** with 256 GB and two 2 TB drives. The four monthly owner costs are **S$0 / S$79.6138 electricity / S$50 internet / S$129.6138 both**. Electricity assumes `0.350 kW × 730 h × S$0.3116/kWh`. The expanded model’s optional 25% room cooling adds S$19.90345 when electricity is counted. Every ownership scenario excludes office rent. Each direct purchase starts with the parts price alone. [Direct purchase assumptions and Malaysian scenarios](06-direct-payback.md) · [Expanded ownership budgets](03-rent-vs-buy-tco.md)

Each scenario cell reports **monthly recurring rent only / including quoted rental setup**. For parts cost `H`, converted monthly recurring rent `R`, owner operating cost `O` and setup `F`, the figures are `H / (R − O)` and `(H − F) / (R − O)`. The left value under neither utility is the direct `H / R`. An unquoted fee leaves the right value N/Q, and the left remains a sensitivity that ignores setup. For a continuing rental, use the actual renewal price and count savings only from the first avoidable bill. A noncancellable term or overlap while migrating delays those savings. For every eligible new row here, `R > O` and each known `F < H`. With `H > F` and `R ≤ O` there is no forward payback. Monthly billing reaches equality or better at the next whole month computed from unrounded figures. The one annual prepay has a separate cash calculation below. [Full monthly and prepaid methodology](07-all-rentals-break-even.md#how-to-read-a-payback-cell)

| ID and capacity | R / F in S$ | Neither utility | Electricity only | Internet only | Both utilities |
|---|---:|---:|---:|---:|---:|
| N01 · A2 [Nindohost 256 GB, Germany][N01] | 301.78 / N/Q | 28.53 / N/Q | 38.75 / N/Q | 34.19 / N/Q | 50.01 / N/Q |
| N02 · A2 [Progressive Robot AX162-R][N02] | 374.83 / 149.25 | 22.97 / 22.57 | 29.16 / 28.66 | 26.50 / 26.04 | 35.11 / 34.50 |
| N03 · A1 [Progressive Robot AX162-S][N03] | 374.83 / 149.25 | 23.72 / 23.32 | 30.12 / 29.61 | 27.37 / 26.91 | 36.26 / 35.65 |
| N04 · A2 [PowerVPS.net 9454P, DE/FI][N04] | 412.69 / N/Q | 20.86 / N/Q | 25.85 / N/Q | 23.74 / N/Q | 30.41 / N/Q |
| N05 · A2 [IT-24 AX162-R][N05] | 440.98 / N/Q | 19.52 / N/Q | 23.82 / N/Q | 22.02 / N/Q | 27.65 / N/Q |
| N06 · A1 [IT-24 AX162-S][N06] | 440.98 / N/Q | 20.16 / N/Q | 24.60 / N/Q | 22.74 / N/Q | 28.56 / N/Q |
| N07 · A2 [Faciotech Enterprise Metal, Germany][N07] | 501.68 / 0.00 | 17.16 / 17.16 | 20.40 / 20.40 | 19.06 / 19.06 | 23.14 / 23.14 |
| N09 · A2 [AmazingRDP Ultra, Europe, annual][N09] | 580.35 / 0.00 | 14.83 / 14.83 | 17.19 / 17.19 | 16.23 / 16.23 | 19.10 / 19.10 |
| N10 · A1 [Nindohost 128 GB, Germany][N10] | 580.35 / N/Q | 15.32 / N/Q | 17.76 / N/Q | 16.76 / N/Q | 19.73 / N/Q |
| N12 · A2 [AmazingRDP Ultra, Europe, monthly][N12] | 644.82 / 0.00 | 13.35 / 13.35 | 15.23 / 15.23 | 14.47 / 14.47 | 16.71 / 16.71 |

The five remaining offers are **N/A for both purchase profiles**. N08’s 128 GB / 2 × 2 TB misses A1’s larger drives and A2’s RAM. N11’s 128 GB / 2 × 1.9 TB misses both mirror floors and A2’s RAM. N13’s second-drive upgrade leaves about 1 TB mirrored. N14 and N15 give 1.92 TB mirrored at 128 GB, below the A1 disk and A2 memory requirements. Their native and SGD rental charges remain visible in the first table.

**AmazingRDP N09.** The annual offer requires **USD 5,400, or S$6,964.19, upfront**, with explicitly zero setup. Under the quoted renewal terms the second invoice becomes due at month 13. The A2 parts price already exceeds the first invoice, while two invoices total S$13,928.38. Even counting both utilities, the owned hardware totals S$11,720.13 through month 24. With identical renewals, **month 13 is the first completed month from which cumulative ownership cash stays no higher in all four scenarios**. The fractional service-month equivalents in the table spread annual rent over the year. The USD 1,455 quarterly and USD 2,820 half-year alternatives in the cart are separate prepaid options. [Selected billing cycles](../2026-11-20-follow-up-global.md#amazingrdp)

## What changes at 36 months across all 119 offers?

The counts below compare actual committed rent at 36 months with the matching ownership budget. They include only rows with a stated setup. A dual-profile offer counts once per applicable profile. All amounts assume the recorded rates continue. Taxes, buyer eligibility and allocation still require resolution.

| Profile and Singapore ownership budget | Budget at 36 mo S$ | Lower rental subtotals in original 104 | Lower rental subtotals in new 15 | Lower rental subtotals in all 119 | Compared with stated setup | Setup unknown |
|---|---:|---:|---:|---:|---:|---:|
| A1 direct · parts only | 8,891.00 | 0 | 0 | 0 | 25 | 12 |
| A1 direct · parts + server electricity + internet | 13,557.10 | 3 | 0 | 3 | 25 | 12 |
| A1 expanded ownership budget | 15,773.81 | 3 | 1 | 4 | 25 | 12 |
| A2 direct · parts only | 8,609.40 | 0 | 0 | 0 | 25 | 16 |
| A2 direct · parts + server electricity + internet | 13,275.50 | 3 | 0 | 3 | 25 | 16 |
| A2 expanded ownership budget | 15,466.87 | 4 | 1 | 5 | 25 | 16 |

With electricity alone, no A1 rental with a quoted setup costs less than owning at 36 months, and one A2 rental does (UHost). The result is the same with internet alone. With **both** costs counted, six distinct stated-setup rentals remain below the direct purchase budgets. A1 has PlusClouds S, HummingTribe and BizoSiz S. A2 has UHost R, PlusClouds R and BizoSiz R. The **expanded** budgets bring the count to nine by including Provisov A2 and both Progressive Robot offers. The expanded model adds UPS and assembly, a repair reserve and a separate cooling allowance. The [earlier inventory](05-repository-rental-comparison.md#which-rentals-change-the-buying-decision) gives the terms and limitations of the original offers.

**Two leads with unquoted setup warrant separate treatment.** Nindohost N01 quotes USD 234/month for A2. Three years of rent alone is S$10,864.14, leaving S$2,411.36 before reaching the direct A2 budget with both utilities, or S$4,602.73 before reaching the expanded budget. The UHost A2 Helsinki quote is S$10,368.91 for 36 months including stated setup, with different network and fulfillment uncertainties. PowerVPS.net N04 has S$14,856.94 known rent over 36 months, above the direct budget but below the expanded A2 budget. It leaves S$609.92 for setup and other charges before reaching that expanded budget. IT-24’s identical R/S rents alone already exceed their respective expanded budgets. [Nindohost evidence](../2026-11-20-follow-up-global.md#nindohost) · [PowerVPS.net evidence](../2026-11-20-follow-up-newer-cpu.md#new-qualifying-seller-powervpsnet) · [IT-24 fee discrepancy](../2026-11-20-follow-up-exact-cpu.md#it-24--two-exact-cpu-configurations-at-usd-34193-per-month)

## Offer evidence and exclusions

| Offer IDs | Term, availability and tax evidence recorded in the repository |
|---|---|
| N01, N10 · Nindohost | Both SKUs identify Germany. The seller’s USD catalog opens a general quote form. Setup, minimum commitment, tax, port, traffic, IPs and physical allocation are unresolved. The two differently priced RAM/disk configurations explain why the USD 234 rate applies to A2 only. [Catalog and quote form](../2026-11-20-follow-up-global.md#nindohost) |
| N02, N03 · Progressive Robot | Native GBP monthly listing, software RAID 1, guaranteed unmetered 1 Gbps. Both order paths reached domain selection. No buyer-specific VAT, additional contractual minimum, final checkout, server country, IP allowance or stock was established. A UK business address does not establish a UK datacenter. [Product and payment evidence](../2026-11-20-follow-up-global.md#progressive-robot) |
| N04, N08 · PowerVPS.net | Order requires registration. The 9454P is advertised in Germany/Finland and the non-P 9455 in France. A 1 Gbps port and unlimited traffic are advertised. Hardware setup, tax, minimum, individual IP allocation and physical stock are unresolved. Published legal PDF carries a future revision date. [Storefront and model-specific hardware reference](../2026-11-20-follow-up-newer-cpu.md#new-qualifying-seller-powervpsnet) |
| N05, N06 · IT-24 | Selected monthly USD configurators confirm the named hardware, 1 Gbps and software RAID 1. No setup line was shown. An older catalog refers to a Hetzner tariff and the final total was unrecovered. Actual fee, tax, minimum, deployment location, IPs, traffic and stock remain unresolved. [Exact carts](../2026-11-20-follow-up-exact-cpu.md#it-24--two-exact-cpu-configurations-at-usd-34193-per-month) |
| N07 · Faciotech | Germany unmanaged base, ex tax, USD 389/month, explicitly zero setup and the same rent on annual billing. Managed is USD 549/month and two years requires a quote. Root, KVM and IPv4/v6 are advertised. The engineer and accepted agreement establish location-specific supply, final configuration, term price and legal seller. Port/traffic unconfirmed. [Configurator and terms](../2026-11-20-follow-up.md#faciotech--new-matching-quoted-configuration) |
| N09, N12 · AmazingRDP | Public cart for the same European machine on two billing cycles. Explicit zero setup, applicable tax extra, renews for the prepaid term unless cancelled. Monthly USD 499.99 due today or USD 5,400 upfront for twelve months. Country, city, IP allocation, actual RAID layout and stock unresolved. [Selected cycles and conditions](../2026-11-20-follow-up-global.md#amazingrdp) |
| N11 · Good-host.net | Gravelines listing shows EUR 434.99/month and EUR 389.99 setup. The order route requires registration and the seller requests support confirmation despite its stock label. Tax, minimum and SKU-specific bandwidth are unknown. An older EUR 298 exact-CPU FAQ is superseded. [Offer and updates](../2026-11-20-follow-up-exact-cpu.md#good-hostnet--newer-cpu-listing-exact-cpu-faq-superseded) |
| N13 · XDLHOST | Finland monthly total includes EUR 12.60 for the added NVMe and EUR 2,180 setup. Germany adds EUR 5/month. Tax, additional minimum and stock unconfirmed. The source’s **month 14** measures when lower recurring **rental** charges recover XDLHOST’s higher setup against regular Hetzner. Hardware purchase payback is **N/A** because of the undersized mirror and RAM. [Selected drive and checkout totals](../2026-11-20-follow-up-exact-cpu.md#xdlhost--exact-cpu-in-dell-upgraded-with-a-second-nvme) |
| N14, N15 · JHCloud.ai | Native USD monthly listings, advertised zero setup, ex GST. Lille and Warsaw share USD 663.42, Montreal USD 643.99. Login required. Physical supply is subject to manual review and delivery estimates differ. One IPv4 and IPMI are advertised. Additional contractual minimum unresolved. [Regional products and stock evidence](../2026-11-20-follow-up-global.md#jhcloudai) |

The follow-up watchlist separately records **AvalinHost**, whose buyer invoice is in Iranian toman and whose pricing is indexed internally to EUR. Direct EUR payment and an international payment route remained unverified. **Gengbiz** identifies a Malaysian seller. The datacenter, actual SSD medium and a working selected order remain unresolved. Neither lead supplies a comparable payable quote for these tables. Sold-out, checkout-disabled, contradictory tenancy or demonstration leads remain in their dated evidence logs. [AvalinHost payment basis](../2026-11-20-follow-up-exact-cpu.md) · [Gengbiz and other conditional catalogs](../2026-11-20-follow-up-global.md#conditional-catalogs) · [Exclusions and corrected leads](../2026-11-20-follow-up.md#exclusions-and-corrected-leads)

[snapshot]: https://github.com/tailrocks/dedicated-servers-providers/blob/c868b31019be4c449bb62cbfa9786d44ac663db4/README.md?plain=1#L23-L158
[gbpfx]: https://data-api.ecb.europa.eu/service/data/EXR/D.GBP.EUR.SP00.A?startPeriod=2026-11-19&endPeriod=2026-11-19&format=csvdata
[sgdfx]: https://data-api.ecb.europa.eu/service/data/EXR/D.SGD.EUR.SP00.A?startPeriod=2026-11-19&endPeriod=2026-11-19&format=csvdata
[usdfx]: https://data-api.ecb.europa.eu/service/data/EXR/D.USD.EUR.SP00.A?startPeriod=2026-11-19&endPeriod=2026-11-19&format=csvdata
[N01]: https://nindohost.co.zm/servers/dedicated/?currency=USD
[N02]: https://account.progressiverobot.com/cart.php?a=add&pid=64&billingcycle=monthly&currency=1
[N03]: https://account.progressiverobot.com/cart.php?a=add&pid=65&billingcycle=monthly&currency=1
[N04]: https://powervps.net/
[N05]: https://my.it-24.pro/cart.php?a=add&pid=132
[N06]: https://my.it-24.pro/cart.php?a=add&pid=131
[N07]: https://faciotech.com/dedicated-servers.php#configurator
[N08]: https://powervps.net/
[N09]: https://my.amazingrdp.com/order/dedicated-server-6
[N10]: https://nindohost.co.zm/servers/dedicated/?currency=USD
[N11]: https://dedicated.good-host.net/offer/amd-epyc-turin-9455-128gb-3840gb-gravelines?currency=eur
[N12]: https://my.amazingrdp.com/order/dedicated-server-6
[N13]: https://client.xdlhost.com/cart.php?a=add&pid=232
[N14]: https://www.jhcloud.ai/dedicated-servers/amd-epyc-9455p-315ghz-48-cores
[N15]: https://www.jhcloud.ai/dedicated-servers/amd-epyc-9455p-315ghz-48-cores-2
