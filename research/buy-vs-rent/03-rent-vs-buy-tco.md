# Rent versus buy: Singapore and Malaysia CI server budgets

Original cost model: **19 November 2026**; repository-wide rental comparison and alternative-drive sensitivities added **20 November 2026**. All amounts in the cost tables are **Singapore dollars** unless stated otherwise. These are reproducible planning budgets, not supplier quotes, forecasts or proof that the proposed machine meets the performance target. Read with [all 104 existing rental offers](05-repository-rental-comparison.md).

## 1. Decision supported by the evidence

**Cheap European rentals already researched in this repository can cost less than owning in Singapore, even over three years.** Buying for an existing suitable Singapore office remains the strongest ownership case when local placement or control matters. Singapore colocation is a much more expensive case. Malaysia has lower published colocation leads, but power, chassis acceptance, tax, contract and servicing details remain unresolved.

Do not use only Hetzner's expensive regular new-order rate to decide whether to buy. The current repository includes UHost, BizoSiz and PlusClouds offers with matching A1 or A2 capacity at much lower recurring prices, subject to their evidence and service limitations. AX162-1-LTD is **unavailable in the current public feeds** and remains below only as a historical sensitivity. Retain a cheap existing lease's actual invoice. Regional figures and limitations are in [02-rental-market.md](02-rental-market.md).

All financial conclusions below are conditional on the [candidate passing the actual CI replay](04-validation-and-procurement.md). A low cost cannot compensate for failing the user's 3–5% performance tolerance.

## 2. Owned profiles compared with Hetzner

| Profile | Proposed single owned host | Parts subtotal | Matching rental capacity class |
|---|---|---:|---|
| **A1** | Threadripper PRO 5995WX, WRX80, 128 GB non-ECC DDR4 in eight modules, 2 × 4 TB consumer NVMe | **S$8,891.00** | AX162-1: 128 GB, 2 × 3.84 TB DC NVMe |
| **A2** | Same CPU/platform, 256 GB non-ECC DDR4 in eight modules, 2 × 2 TB consumer NVMe | **S$8,609.40** | AX162-2: 256 GB, 2 × 1.92 TB DC NVMe |

The [full BOM](01-hardware-and-performance.md) includes cooling, case and PSU. A1 costs more despite less RAM because its two 4 TB drives cost more. The 256 GB eight-module RAM option has stronger exact-part compatibility evidence; the 128 GB option still needs validation.

These are **capacity-class comparisons**, not identical machines: consumer versus enterprise storage, memory protection, platform generation, support and network service differ. The public Clang benchmark is useful screening evidence for the 5995WX, not a measured performance result for either proposed BOM.

## 3. Model and assumptions

The budget counts upfront cash plus recurring costs and an earmarked repair reserve:

`Owner budget(N months) = upfront + N × monthly operating budget − any explicitly modeled resale proceeds`

`Rental budget(N months) = setup + N × recurring invoice`

A commitment longer than N can create a larger liability or upfront payment than this simple rental equation. This matters particularly for UltaHost's two-year offer.

| Input | Base assumption | Status |
|---|---|---|
| Analysis periods | 12, 24 and 36 months; 730 hours per modeled month | Planning convention |
| Single workstation average wall power | **350 W**, including idle and busy periods | Assumption; not measured, and not CPU TDP or PSU rating |
| Separate office cooling | **25%** extra energy | Assumption; actual ambient temperature and cooling arrangement can differ |
| Singapore electricity | **S$0.3116/kWh including GST** | SP Q4 2026 reference tariff; use actual marginal bill if different |
| Office connectivity increment | **S$50/month** | Allowance; may be zero on an adequate existing connection or more for business connectivity |
| Maintenance reserve | **3% of parts cost per year** | Budget contingency, not a claimed annual repair rate |
| Office initial extras | **S$700**: S$500 UPS allowance and S$200 assembly/delivery allowance | Not retail quotes; size UPS from actual load/runtime |
| Resale value | Zero | Conservative simplification; resale is uncertain |
| Financing, discount rate, tax deductions | Not modeled | Cash-budget comparison, not discounted investment valuation |
| Additional ownership labour | Zero in base; **S$100/month** sensitivity shown | Incremental work only; common CI/software administration applies to rentals too |
| Extra office floor-space/rent | Zero | Assumes an existing suitable location; add any incremental premises cost |
| Future power tariffs, FX and service rates | Held constant | Sensitivity assumption, not a forecast |

The advertised parts prices were collected from several retailers, not one complete GST-normalized assembled invoice. Obtain a final tax-inclusive quote. Final invoice differences could reverse close results.

**Tax reference:** the main Hetzner table uses an illustrative **9% Singapore-billed consumer/non-recoverable tax case**. The user's billing residence, registration and recoverability have not been established. Server location alone does not decide tax. [Hetzner's VAT page][T01] lists Singapore at 9%; [IRAS][T02] explains the effect of business registration for imported services. Net prices are shown below as well. A GST-registered business should compare consistently on its actual recoverable/non-recoverable basis.

**FX reference:** [ECB on 19 November 2026][T03], EUR 1 = SGD 1.4176 = USD 1.0992 = MYR 4.5205. Bank/card spreads are excluded.

## 4. Rental inputs: current new-order schedule

| Hetzner offer, including one IPv4 | Monthly before tax | Setup before tax | Monthly in the illustrative 9% case | Setup in the 9% case |
|---|---:|---:|---:|---:|
| AX162-1 regular | S$870.41 | S$430.95 | **S$948.74** | S$469.74 |
| AX162-2 regular | S$1,196.45 | S$593.97 | **S$1,304.14** | S$647.43 |
| AX162-1-LTD, historical / currently unavailable | S$452.21 | S$55.29 | **S$492.91** | S$60.26 |

The [official live price feed][T09] confirms the regular EUR 612.30 / 842.30 monthly and EUR 304 / 419 setup amounts on 20 November. Add [IPv4 at EUR 1.70/month][T05]. The EUR 317.30 + 39 LTD price is historical [schedule evidence][T04], not available current inventory. Existing contracts can have different legacy rates. Provider USD tariffs differ from the FX-converted EUR scenario used here.

### Worldwide rental alternatives already in the repository

These use the repository's exact native quotes at the fixed 19 November FX, before unquoted tax/IP/network charges. They are **known-charge scenarios**, not tax-normalized final invoices or supplier endorsements. Unknown final terms remain material. A1 requires at least 128 GB and two drives supporting about 3.84 TB mirrored; A2 requires at least 256 GB and two drives supporting about 1.92 TB mirrored. These capacity classes do not certify CPU, SSD or CI performance.

| Existing rental offer | Capacity class | Native recurring / setup | 12 months | 24 months | 36 months | Evidence limit |
|---|---|---|---:|---:|---:|---|
| UHost AX162-R | A2 | USD 220/month + 120 setup | S$3,559 | S$6,964 | S$10,369 | Configurator; stock, network and final tax unconfirmed |
| BizoSiz AX162-S / AX162-R | Separate A1 / A2 offers | USD 279/month + 111 setup | S$4,461 | S$8,779 | S$13,097 | Repository cart evidence; stock/delivery and final tax unconfirmed |
| PlusClouds AX162-S | A1 | EUR 229/month + 411 setup | S$4,478 | S$8,374 | S$12,269 | Listed/general portal; exact term and supply unconfirmed |
| PlusClouds AX162-R | A2 | EUR 229/month + 542 setup | S$4,664 | S$8,559 | S$12,455 | Listed/general portal; exact term and supply unconfirmed |

Sources and all remaining offers are mapped in [05-repository-rental-comparison.md](05-repository-rental-comparison.md), preserving original dates and qualifications. These are European placements; the owner's or reseller's country is not the physical server location. They do not satisfy a requirement to place the machine in Singapore/Malaysia.

For A2, UHost's S$10,369 and BizoSiz's S$13,097 known 36-month charges are below the S$15,467 Singapore office reference. For A1, PlusClouds' S$12,269 and BizoSiz's S$13,097 are below the S$15,774 reference. Illustratively adding 9% to those rental amounts gives S$11,302 for UHost, S$14,275 for BizoSiz and S$13,374 for PlusClouds A1. This sensitivity is **not a claim that any provider owes that exact tax**. Stock, network requirements, payment eligibility, supplier identity and final invoice costs can change the choice. The direct UHost and PlusClouds listings were re-opened on 20 November; BizoSiz retains the repository's existing 20 November cart evidence after this pass's independent fetch failed.

## 5. Main 12-, 24- and 36-month comparison

Whole-dollar totals below are calculated from unrounded inputs. They include the repair reserve for ownership; actual spending can be lower if that reserve remains unused. Do not also add repair spending funded from the same reserve without adjusting it.

| Scenario | Upfront | Monthly budget | 12 months | 24 months | 36 months |
|---|---:|---:|---:|---:|---:|
| Rent AX162-1 standard | S$470 | S$948.74 | S$11,855 | S$23,240 | S$34,624 |
| Rent AX162-2 standard | S$647 | S$1,304.14 | S$16,297 | S$31,947 | S$47,596 |
| Historical AX162-1 LTD (unavailable) | S$60 | S$492.91 | S$5,975 | S$11,890 | S$17,805 |
| Buy A1 SG office | S$9,591 | S$171.74 | S$11,652 | S$13,713 | S$15,774 |
| Buy A2 SG office | S$9,309 | S$171.04 | S$11,362 | S$13,414 | S$15,467 |
| Buy A1 SG 5U colo | S$9,572 | S$764.63 | S$18,747 | S$27,923 | S$37,098 |
| Buy A2 SG 5U colo | S$9,290 | S$763.93 | S$18,457 | S$27,624 | S$36,791 |

### What the office rows include

A1 upfront is S$8,891 + S$700 = **S$9,591**. A2 is S$8,609.40 + S$700 = **S$9,309.40**.

Single-host energy and cooling = 0.350 kW × 730 hours × S$0.3116 × 1.25 = **S$99.52/month**. Add S$50 network and reserve of S$22.23 for A1 or S$21.52 for A2. These give S$171.74 and S$171.04 monthly, respectively.

At 12 months, A1 office ownership is only about **S$203** below regular AX162-1 in this model. That is too close for a categorical purchase decision before complete quotes and validation. At 36 months it is about **S$18,851** below that regular rate.

Against the historical, currently unavailable AX162-1-LTD rate, however, the same office build saves only about **S$2,031 over 36 months**. Adding S$100/month of ownership-specific work makes rental cheaper over that horizon. This is why the actual existing or obtainable rental rate matters more than a generic “buy is cheaper” claim.

A2 office ownership is approximately **S$32,129 below regular AX162-2 over 36 months** under the stated assumptions. Its capacity-matched consumer storage and benchmark confidence still need acceptance.

### What the Singapore colocation rows include

The [QUAPE 5U plan][T06] is S$680 before tax / **S$741.20 including 9% GST**, with 0.8 kVA and 100 Mbps shared. It requires facility approval and space confirmation. This is not contractual parity with Hetzner's 1 Gbps dedicated connection.

For a new build, replace the S$302.40 tower case with [RM51 5U at S$624][T07] and [rails at S$159][T08]: **S$480.60 additional hardware**. Add S$200 assembly/delivery; no office UPS allowance. Reserve is calculated on the revised hardware subtotal.

The recurring colocation price already includes the listed power allocation, so office electricity/cooling is **not added again**. Unknown facility setup, nonstandard network service, repairs/remote hands and installation charges are not asserted to be zero; these rows are known-charge budgets subject to the final facility quote.

At 36 months, A1 Singapore colocation is about **S$2,474 more** than regular AX162-1, before such unknown charges, and considerably more than LTD. A2 colocation can be cheaper than regular AX162-2, but its weaker network allocation and owner hardware responsibility remain material.

## 6. Financial crossover and sensitivity to labour

For fixed costs with no resale value:

`Crossover months = (owner upfront − rental setup) / (rental monthly − owner monthly)`

This is meaningful only if the rental monthly cost is higher and the performance/service difference is acceptable. It is not an investment return guarantee.

| Comparison | Base crossover | With S$100/month extra ownership work |
|---|---:|---:|
| Buy A1 SG office vs Rent AX162-1 standard | 11.7 months | 13.5 months |
| Buy A2 SG office vs Rent AX162-2 standard | 7.6 months | 8.4 months |
| Buy A1 SG office vs Historical AX162-1 LTD (unavailable) | 29.7 months | 43.1 months |
| Buy A1 SG 5U colo vs Rent AX162-1 standard | 49.4 months | 108.2 months |
| Buy A2 SG 5U colo vs Rent AX162-2 standard | 16.0 months | 19.6 months |
| Buy A1 SG 5U colo vs Historical AX162-1 LTD (unavailable) | No crossing | No crossing |

A long theoretical crossover such as 49 or 108 months is especially uncertain for older hardware because failure, availability, resale and replacement decisions can change. If both upfront and monthly ownership costs are higher, there is no crossing in this model.

**A useful quote threshold:** for A2 in a Singapore office, a zero-setup, capacity- and performance-acceptable rental at approximately **S$429.64/month all-in** equals the modeled 36-month ownership budget. The equivalent A1 threshold is **S$438.16/month**. These rise by S$100/month if that additional ownership work is required. A cheaper acceptable rental can beat ownership even when an expensive regular AX162 tariff does not.

## 7. Local rentals: financial context without promoting uncertain quotes to guarantees

The [market report](02-rental-market.md) records hardware, setup, term, location and limitations. The following are before-tax service budgets for perspective, with FX fixed. They are **not** substitutes for the main tax scenario above.

| Offer | Advertised recurring rate in SGD | 24-month price arithmetic | Important qualification |
|---|---:|---:|---|
| PowerDedi Singapore 9454P / 256 GB / 2 × 3.84 TB | S$630.65 | S$15,136 | Zero setup advertised, but location/availability contradiction; not a confirmed buy-versus-rent alternative |
| UltaHost Singapore 9454 / 512 GB / 2 × 1.92 TB | S$1,402.92 monthly equivalent | S$33,670 for the displayed two-year term | USD 26,107.68 term price; setup/tax not established; do not interpret as cancellable monthly billing |
| INTROSERV Singapore 9554 / 128 GB / larger drives | S$1,457.99 | S$34,992 plus any confirmed setup | Month-to-month selector; same price held constant for illustration; 64-core candidate is not identical performance |
| VPSShell Kuala Lumpur 9454 / 512 GB / 2 × 1.92 TB | S$1,797.78 | S$43,147 | No setup advertised; crypto-only, stock and transfer terms unresolved |
| DediJet Singapore, two 9950X / 128 GB hosts | S$693.84 for the pair | S$16,652 | Zero setup advertised; compare with 128 GB-per-host owned pairs; two-host availability not reserved |

The lowest PowerDedi advertised rate would materially improve Singapore rental economics if its exact location, fulfilment and contract are verified. It has not been used as a firm central TCO assumption. Similarly, ServerPacket's Malaysia EPYC 9754 “from USD 770” promotion/renewal discrepancy must be resolved before extrapolating a multi-year bill.

For more expensive faster rental candidates, compare **successful CI jobs per dollar**, queue latency and required completion time after a workload test. Paying 50% more is reasonable only when the measured benefit or service requirement justifies it.

## 8. Two mainstream desktop nodes in a Singapore office

These models use **450 W combined average wall power**, also an assumption, plus 25% cooling. The pair gets **S$1,200 upfront allowances**: S$1,000 total UPS budget and S$200 assembly/delivery. Network is S$50/month for the pair, and reserve is 3% of pair parts per year. External KVM/remote power, if required, is not included.

| Pair | Upfront incl. allowances | Monthly budget | 12 months | 24 months | 36 months |
|---|---:|---:|---:|---:|---:|
| Two Intel 270K Plus, 64 GB each | S$8,679 | S$196.65 | S$11,039 | S$13,399 | S$15,759 |
| Two Intel 270K Plus, 128 GB each | S$11,639 | S$204.05 | S$14,088 | S$16,536 | S$18,985 |
| Two AMD 9950X3D, 64 GB each | S$9,441 | S$198.55 | S$11,824 | S$14,206 | S$16,589 |
| Two AMD 9950X3D, 128 GB each | S$12,401 | S$205.95 | S$14,873 | S$17,344 | S$19,816 |

DediJet's two rented 128 GB hosts cost **S$24,978 before tax over 36 months**, or **S$27,226 in an illustrative 9% non-recoverable tax scenario**. The relevant owned comparisons are the **128 GB-per-host** rows. Its 9950X and the owned 9950X3D/Intel CPUs are not identical; validate the queue.

The cheaper 64 GB-per-host models cannot run a job that requires 128 GB on one host. Aggregate memory across runners is not a shared pool. For bursty work, purchasing one node and adding the second only when measured queue pressure warrants it can reduce unused capital; the complete pool must still satisfy the target when compared with AX162.

## 9. Malaysia: electricity sensitivity and conditional colocation floors

No complete Malaysian 5995WX non-ECC BOM was established. The following keep the Singapore-procured parts assumption so the effect of hosting location is visible. They **exclude unquoted cross-border logistics, import/transaction taxes, local servicing arrangements and extra hands**. They are not Malaysia local-purchase quotes.

| Scenario | Upfront known costs | Monthly known costs/reserve | 12 months | 24 months | 36 months |
|---|---:|---:|---:|---:|---:|
| Buy A2 MY office sensitivity | S$9,309 | S$126.70 | S$10,830 | S$12,350 | S$13,871 |
| Buy A2 MY Awan4U floor | S$9,135 | S$194.81 | S$11,473 | S$13,811 | S$16,148 |
| Buy A2 MY tower floor | S$8,841 | S$209.37 | S$11,353 | S$13,866 | S$16,378 |

The **Malaysia office sensitivity** changes only the energy rate; it retains the S$700 office allowance, S$50 network and repair reserve. The modeled Peninsular commercial marginal rate is **RM0.5509088/kWh**, derived in the market report. It includes the renewable-energy levy and November AFA but is **prior to any additional invoice-specific tax**. The RM20 retail charge is incremental only for a new account. It is not a Sabah/Sarawak or domestic tariff.

At 350 W plus 25% cooling, this saves about **S$44.34/month, or S$1,596 over 36 months**, relative to the Singapore reference. That is much less than many multi-year rental differences and can be consumed by logistics or servicing. Lower electricity alone is not a sufficient reason to relocate.

The **AwanPrime 4U floor** uses its RM550/month / 460 W offer, substitutes a S$469 RM44 and S$159 rails, and adds S$200 assembly. The 4U chassis/cooler fit, board clearance, peak power, non-ECC acceptance, setup and tax remain unresolved. A 350 W modeled average is not proof that peaks satisfy 460 W.

The **ServerHosting.MY tower floor** retains the original case, adds S$200 assembly and the listed RM100 setup, then uses RM599/month. Its allowed wattage is unconfirmed; a 13 A socket is not the purchased power allocation. Generic terms may impose an annual obligation. The published floor cannot justify a final colocation purchase.

### Malaysian-local Intel runner pair

For an actual Malaysian local desktop purchase, the separate two-node Intel BOM in the market report is **RM24,008 ≈ S$7,528.76**, near the Singapore parts figure rather than substantially below it. This is two 270K Plus machines with **64 GB and 2 × 2 TB per host** using the locally listed parts; no Singapore-to-Malaysia hardware shipment is assumed for this row.

For a comparable office sensitivity, retain S$1,200 equivalent UPS/assembly/delivery allowances, S$50/month network and a 3% annual parts reserve. At an assumed 450 W combined average and 25% cooling, the Peninsular commercial electricity calculation is **S$70.94/month**. These allowances are planning figures, not Malaysian supplier quotes; add any unquoted invoice taxes, floor-space cost, labour or remote-management equipment.

| Malaysia-local Intel pair | Upfront incl. allowances | Monthly budget | 12 months | 24 months | 36 months |
|---|---:|---:|---:|---:|---:|
| 64 GB + 2 × 2 TB per host | S$8,728.76 | S$139.76 | **S$10,405.90** | **S$12,083.05** | **S$13,760.19** |

This is an independent-job pool with 64 GB per host before OS/services/headroom, not one A1 or A2 memory pool. Its queue performance is unmeasured. Compare it with rentals able to run the same jobs at the required throughput, rather than treating 128 GB aggregate as a single-host capacity match. The 128 GB-per-host DediJet/PowerDedi rental pairs in file 02 offer a larger per-job memory envelope.

## 10. Storage and RAM-qualification cost sensitivities

The 20 November hardware refresh found the ADATA LEGEND 900 PRO 2 TB at S$479 and Lexar NM790 4 TB at S$859. The following hold the office power/network/UPS assumptions constant and change only parts plus the 3% reserve. Lower price does not establish equivalent sustained CI I/O; use the [manufacturer disclosures and exact sources](01-hardware-and-performance.md#20-november-storage-price-sensitivities).

| Single host | Parts subtotal | Singapore office, 36 months |
|---|---:|---:|
| A2, Samsung reference | S$8,609 | S$15,467 |
| A2, ADATA 2 × 2 TB candidate | S$8,069 | S$14,878 |
| A1, Samsung reference; 16 GB-module qualification open | S$8,891 | S$15,774 |
| A1, Lexar 2 × 4 TB candidate; same RAM qualification gap | S$7,831 | S$14,618 |
| 256 GB + 2 × 4 TB Samsung, qualified-revision RAM candidate | S$9,889 | S$16,862 |
| 256 GB + 2 × 4 TB Lexar candidate | S$8,829 | S$15,707 |

The Samsung 256 GB / 2 × 4 TB case addresses the unverified eight-module 16 GB layout by retaining the stronger 32 GB-revision qualification evidence. At S$16,862 over three years, it is about S$943 below the historical 9%-tax LTD scenario, but about S$527 above the historical tax-net LTD cost of S$16,335. Neither LTD scenario is current stock. This illustrates why RAM qualification, storage and actual tax basis matter before interpreting a small saving.

For the Intel 64 GB-per-host pair, four ADATA drives reduce parts by S$1,080 and the 36-month office budget by S$1,177.20, to **S$14,581.36**, holding 450 W average combined power and all other assumptions constant. The individual-job RAM limit remains unchanged.

There is also a lower-priced **conditional Singapore rental-pair lead** in file 02: PowerDedi advertises two 9950X / 128 GB / 2 × 1.92 TB hosts at USD 318/month for both, or S$410.11. At unchanged rates, 36 months of **rent alone** is S$14,764.09 before tax and any setup, or S$16,092.86 with an illustrative 9% tax on rent. Setup for this pair was not established. This could undercut the owned 128 GB-per-host pairs, but exact Singapore availability, complete invoice, operator and service conditions remain unresolved. The drives are slightly smaller than the owned 2 TB pair. Do not use it as a firm fulfilled quote.

## 11. Power, network and utilization

| Average whole-host wall power | Singapore energy only | Singapore with 25% cooling | Malaysia with 25% cooling, converted |
|---|---:|---:|---:|
| 100 W | S$22.75 | S$28.43 | S$15.76 |
| 200 W | S$45.49 | S$56.87 | S$31.53 |
| 350 W | S$79.61 | S$99.52 | S$55.18 |
| 500 W | S$113.73 | S$142.17 | S$78.82 |

Measure average power across the intended duty cycle. A machine running several hours daily can average much less than a continuously busy compiler host; an always-full queue can average more. Neither an 850 W PSU nor a CPU's 280 W rating supplies the required average.

Likewise, office Internet and a colocation shared port are not equivalent to a dedicated datacenter connection. Time real package downloads, image pulls, cache access and artifact uploads. Location matters most through the actual network paths and physical service access; geographical proximity alone does not establish pipeline speed.

A shorter commitment can favor rental when the duration of need is uncertain. In these flat monthly dedicated-server comparisons, powering off an allocated machine does not reduce the modeled bill. A different fixed hardware configuration may require another order and setup fee. At sustained utilization, ownership can be attractive, but only if hardware and office uptime satisfy the intended service. Two nodes reduce the impact of one runner failure but do not make individual jobs share memory or make the whole service automatically redundant.

## 12. Recommended procurement order

1. **Obtain capacity-matched rental quotes from the existing worldwide shortlist**, plus the actual current Hetzner invoice if applicable. Resolve setup, IP/network, commitment, inventory and customer-specific tax. LTD is not currently available in the checked feed.
2. **Choose the topology from job size:** one large 256 GB host, or independent 64/128 GB runners. Do not let aggregate RAM conceal a per-job capacity limit.
3. **Get complete Singapore owned-system and local-rental quotes.** Prioritize the 5995WX candidate for strict non-ECC single-host requirements, or the Intel pair for separate jobs; verify the PowerDedi lead before treating its price as obtainable.
4. **Replay actual CI and measure wall power.** Apply the latency and throughput gates in the validation file.
5. **Choose hosting:** existing office first if suitable; Singapore colocation only after a tower/rack and power quote; Malaysia second if a local servicing plan and complete approved offer make the saving worthwhile.

No purchase decision is final until the capacity, performance and complete recurring bill are known. The useful outcome here is a researched shortlist and a cost model that makes those remaining decisions explicit.

## Primary cost sources

[T01]: https://docs.hetzner.com/general/billing-and-account-management/billing-at-hetzner/value-added-tax/
[T02]: https://www.iras.gov.sg/taxes/goods-services-tax-(gst)/gst-and-digital-economy/local-businesses
[T03]: https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html
[T04]: https://docs.hetzner.com/general/infrastructure-and-availability/price-adjustment/
[T05]: https://docs.hetzner.com/general/infrastructure-and-availability/ipv4-pricing/
[T06]: https://www.quape.com/servers/colocation-server/
[T07]: https://dynacoretech.com/products/silverstone-rm51-5u-rackmount-server-chassis-support-up-to-ssi-eeb-black-sst-rm51
[T08]: https://dynacoretech.com/products/silverstone-rms05-22-tool-less-ball-bearing-sliding-rail-kit-sst-rms05-22

Additional electricity, provider, chassis and retail source URLs are preserved beside their claims in [02-rental-market.md](02-rental-market.md) and [01-hardware-and-performance.md](01-hardware-and-performance.md).


[T09]: https://www.hetzner.com/_resources/app/data/app/live_data_prices.json
