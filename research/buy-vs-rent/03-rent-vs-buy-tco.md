# Optional ownership budgets for Singapore and Malaysia

For the direct hardware-versus-rent decision, choose whether to count server electricity and internet independently. The direct comparison shows the months of rent needed to recover the hardware price, both for an existing lease and for a new rental with a setup fee. [Direct hardware payback](06-direct-payback.md)

This report adds **optional** UPS, assembly/delivery, separate room cooling and repair allowances. **Office, room and floor-space rent are excluded from every scenario.** Figures are in Singapore dollars unless another currency is shown. The original 19 November 2026 model was extended on 20 November with worldwide rental and alternative-drive comparisons.

## 1. How the choice of costs changes the decision

The Singapore 256 GB workstation costs **S$8,609.40 in parts**. UHost's published Helsinki rental and setup total **S$10,368.91 over 36 months**. Buying comes out **S$1,759.51 lower** when comparing hardware alone. Counting the workstation's electricity and S$50/month of incremental internet brings ownership to **S$13,275.50**, so the same rental comes out **S$2,906.59 lower**. Including the separately priced allowances in this report brings ownership to **S$15,466.87**. The rental amounts precede unquoted customer-specific charges. Stock and CI performance remain unverified. [Worldwide rental offers](05-repository-rental-comparison.md)

For a runner that must be in Singapore or Malaysia, compare the existing-site purchase with a rental physically available there. Colocation has its own facility and network charges. For an existing lease, use its current invoice. The AX162-1-LTD is **unavailable in the current public feeds** and appears here only as a historical sensitivity. Final comparisons depend on the 3–5% CI performance tolerance and the site's service requirements. [Regional offerings](02-rental-market.md) · [CI acceptance test](04-validation-and-procurement.md)

## 2. Owned profiles compared with Hetzner

| Profile | Proposed single owned host | Parts subtotal | Matching rental capacity class |
|---|---|---:|---|
| **A1** | Threadripper PRO 5995WX, WRX80, 128 GB non-ECC DDR4 in eight modules, 2 × 4 TB consumer NVMe | **S$8,891.00** | AX162-1: 128 GB, 2 × 3.84 TB DC NVMe |
| **A2** | Same CPU/platform, 256 GB non-ECC DDR4 in eight modules, 2 × 2 TB consumer NVMe | **S$8,609.40** | AX162-2: 256 GB, 2 × 1.92 TB DC NVMe |

The [full BOM](01-hardware-and-performance.md) includes cooling, case and PSU. A1 costs more despite less RAM because its two 4 TB drives cost more. The 256 GB eight-module RAM option has stronger exact-part compatibility evidence; the 128 GB option still needs validation.

These are **capacity-class comparisons**, not identical machines: consumer versus enterprise storage, memory protection, platform generation, support and network service differ. The public Clang benchmark is useful screening evidence for the 5995WX, not a measured performance result for either proposed BOM.

## 3. Optional budget components and assumptions

The expanded existing-site example selects both utilities and all four allowances. Use each selected input once.

`Expanded owner budget(N months) = hardware + selected upfront allowances + N × (selected server electricity + selected room cooling + selected internet + selected repair reserve + selected extra labour) − resale proceeds`

`New monthly rental budget(N months) = setup + N × recurring invoice`

A term commitment can require payment beyond the chosen horizon. For example, UltaHost displays a two-year term. Past setup on an existing lease is a sunk cost.

| Input | Expanded example | How to apply it |
|---|---|---|
| Analysis periods | 12, 24 and 36 months; 730 hours per modeled month | Planning convention |
| Average wall power | **350 W** per workstation or **450 W combined** per desktop pair | Duty-cycle assumptions that include internal cooling and power supply losses. Replace with measured averages. |
| Server electricity | Singapore **S$0.3116/kWh** including GST. Peninsular Malaysia **RM0.5509088/kWh** before account-specific tax. | Select independently from internet. Use the applicable marginal tariff. |
| Separate room cooling | Optional **25% of server electricity** | Use measured incremental air-conditioning if available. |
| Incremental internet | Optional **S$50/month per site** or about **RM159.44** | An allowance for the bill increase. Use zero if the existing connection can serve the runners at the same charge. |
| Repair reserve | Optional **3% of parts cost per year** | A contingency. Actual cash outlay depends on repairs. |
| UPS and assembly/delivery | Optional **S$500 UPS per single host or S$1,000 per pair**, plus **S$200** assembly/delivery per deployment | Upfront allowances totaling S$700 or S$1,200. Use supplier prices if these items are needed. |
| Resale value | Zero | Conservative simplification; resale is uncertain |
| Financing, discount rate, tax deductions | Not modeled | Cash-budget comparison, not discounted investment valuation |
| Additional ownership labour | Zero in the expanded example. Optional **S$100/month** sensitivity. | Count only owner-specific work beyond common CI administration. |
| Future power tariffs, FX and service rates | Held constant | Sensitivity assumption, not a forecast |

The advertised parts prices were collected from several retailers, not one complete GST-normalized assembled invoice. Obtain a final tax-inclusive quote. Final invoice differences could reverse close results.

**Tax reference:** the main Hetzner table uses an illustrative **9% Singapore-billed consumer/non-recoverable tax case**. The user's billing residence, registration and recoverability have not been established. Server location alone does not decide tax. [Hetzner's VAT page][T01] lists Singapore at 9%; [IRAS][T02] explains the effect of business registration for imported services. Net prices are shown below as well. A GST-registered business should compare consistently on its actual recoverable/non-recoverable basis.

On 19 November 2026 the model fixes EUR 1 = SGD 1.4176 = USD 1.0992 = MYR 4.5205, before any bank or card spread. [ECB reference rates][T03]

### Monthly components at an existing site

All figures below are **S$ per month** for the entire host or pair. Choose server electricity and internet independently. If counting electricity, optional room cooling adds 25% of the server electricity charge. The reserve is a separate choice. Totals use the unrounded inputs, so displayed components can differ from a total by one cent. [Electricity tariffs and their scope](02-rental-market.md#8-electricity-sources-for-ownership-scenarios)

| Location and configuration | Server electricity | Optional room cooling | Optional internet | Optional repair reserve | Expanded monthly budget |
|---|---:|---:|---:|---:|---:|
| Singapore A1, 128 GB / 2 × 4 TB Samsung | 79.61 | 19.90 | 50.00 | 22.23 | **171.74** |
| Singapore A2, 256 GB / 2 × 2 TB Samsung | 79.61 | 19.90 | 50.00 | 21.52 | **171.04** |
| Singapore Intel pair, 64 GB per host | 102.36 | 25.59 | 50.00 | 18.70 | **196.65** |
| Singapore Intel pair, 128 GB per host | 102.36 | 25.59 | 50.00 | 26.10 | **204.05** |
| Singapore AMD pair, 64 GB per host | 102.36 | 25.59 | 50.00 | 20.60 | **198.55** |
| Singapore AMD pair, 128 GB per host | 102.36 | 25.59 | 50.00 | 28.00 | **205.95** |
| Malaysia A2 sensitivity, Singapore-sourced hardware | 44.14 | 11.04 | 50.00 | 21.52 | **126.70** |
| Malaysia-local Intel pair, 64 GB per host | 56.75 | 14.19 | 50.00 | 18.82 | **139.76** |

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

Sources for these and the other original offers are mapped in [05-repository-rental-comparison.md](05-repository-rental-comparison.md); [file 08](08-latest-rental-comparisons.md) and [file 09](09-expanded-rental-comparisons.md) add the later offers, preserving their dates and qualifications. The named examples here are European placements; the owner's or reseller's country is not the physical server location. They do not satisfy a requirement to place the machine in Singapore/Malaysia.

For A2, UHost's S$10,369 and BizoSiz's S$13,097 known 36-month charges are below the **expanded** Singapore budget of S$15,467. For A1, PlusClouds' S$12,269 and BizoSiz's S$13,097 are below the **expanded** S$15,774. Across the current **141 offers**, **fifteen** capacity-matched rentals with a stated setup fee have lower known charges than the corresponding expanded budgets. **Six** do so with only hardware, server electricity and internet counted, and **zero** with hardware alone. The earlier 119-offer count was nine, including Progressive Robot’s separate A1/A2 listings at GBP221/month + GBP88 setup. The latest six expanded-budget additions are Wsla A2, ServerWala’s four annual variants and its Helsinki A1 monthly variant. Final taxes, payment charges, supply and customer eligibility remain unresolved where noted. These figures use the Samsung A1/A2 reference builds. [Initial rental snapshot](05-repository-rental-comparison.md) · [15-offer follow-up](08-latest-rental-comparisons.md) · [Latest 22 offers and current counts](09-expanded-rental-comparisons.md) · [Existing-offer corrections](10-current-offer-updates.md)

Illustratively adding 9% to the three named rental offers gives S$11,302 for UHost, S$14,275 for BizoSiz and S$13,374 for PlusClouds A1. Customer-specific billing, stock, network requirements, payment eligibility and the supplier's identity can change the choice. The UHost and PlusClouds listings were re-opened on 20 November. BizoSiz retains the repository's 20 November cart evidence after this pass's independent fetch failed.

## 5. Expanded budgets over 12, 24 and 36 months

The existing-site purchase rows select the optional UPS, assembly/delivery, 25% room cooling, S$50 internet and 3% annual repair reserve. The colocation rows use provider charges and rack costs described below. The Hetzner rows select IPv4 and the illustrative 9% non-recoverable tax. Whole-dollar totals use unrounded inputs. Actual cash spending can be lower when the reserve remains unused. Count repairs against the reserve once.

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

At 350 W for 730 hours, the host draws **255.5 kWh/month**, costing **S$79.61**. Allowing 25% for additional room cooling adds **S$19.90**, bringing electricity with cooling to **S$99.52/month** from unrounded inputs. Internet and repairs have their own lines in the [monthly component table](#monthly-components-at-an-existing-site).

At 12 months, A1 office ownership is only about **S$203** below regular AX162-1 in this model. That is too close for a categorical purchase decision before complete quotes and validation. At 36 months it is about **S$18,851** below that regular rate.

Against the historical, currently unavailable AX162-1-LTD rate, the same expanded purchase budget saves about **S$2,031 over 36 months**. Adding S$100/month of ownership-specific work makes rental cheaper over that horizon.

A2 office ownership is approximately **S$32,129 below regular AX162-2 over 36 months** under the stated assumptions. Its capacity-matched consumer storage and benchmark confidence still need acceptance.

### What the Singapore colocation rows include

The [QUAPE 5U plan][T06] is S$680 before tax / **S$741.20 including 9% GST**, with 0.8 kVA and 100 Mbps shared. It requires facility approval and space confirmation. This is not contractual parity with Hetzner's 1 Gbps dedicated connection.

For a new build, replace the S$302.40 tower case with [RM51 5U at S$624][T07] and [rails at S$159][T08]: **S$480.60 additional hardware**. Add S$200 assembly/delivery; no office UPS allowance. Reserve is calculated on the revised hardware subtotal.

QUAPE quotes one recurring service charge covering rack space, power allocation and shared connectivity. Separate power and internet prices are unquoted. The colocation budget counts the full service fee once, with **no additional office electricity, cooling or internet allowance**. Facility setup, higher network service levels, chargeable remote hands and installation can add to the final quote.

At 36 months, A1 Singapore colocation is about **S$2,474 more** than regular AX162-1, before such unknown charges, and considerably more than LTD. A2 colocation can be cheaper than regular AX162-2, but its weaker network allocation and owner hardware responsibility remain material.

## 6. Expanded-budget crossover and sensitivity to labour

These crossovers use the specific expanded ownership and tax-inclusive rental rows in section 5. At fixed inputs and zero resale value the calculation is

`Crossover months = (owner upfront − rental setup) / (rental monthly − owner monthly)`

Here owner upfront includes the selected UPS/assembly or rack conversion, and owner monthly includes the reserve. Rental setup is deducted only when comparing with a new rental. For crossover on the hardware invoice alone, or with either utility switched off, use [direct hardware payback](06-direct-payback.md).

| Comparison | Expanded-budget crossover | Expanded plus S$100/month extra ownership work |
|---|---:|---:|
| Buy A1 SG office vs Rent AX162-1 standard | 11.7 months | 13.5 months |
| Buy A2 SG office vs Rent AX162-2 standard | 7.6 months | 8.4 months |
| Buy A1 SG office vs Historical AX162-1 LTD (unavailable) | 29.7 months | 43.1 months |
| Buy A1 SG 5U colo vs Rent AX162-1 standard | 49.4 months | 108.2 months |
| Buy A2 SG 5U colo vs Rent AX162-2 standard | 16.0 months | 19.6 months |
| Buy A1 SG 5U colo vs Historical AX162-1 LTD (unavailable) | No crossing | No crossing |

A long theoretical crossover such as 49 or 108 months is especially uncertain for older hardware because failure, availability, resale and replacement decisions can change. If both upfront and monthly ownership costs are higher, there is no crossing in this model.

At 36 months, a zero-setup rental at **S$429.64/month all-in for A2** or **S$438.16/month for A1** equals the corresponding **expanded** Singapore ownership budget. The hardware-only thresholds are **S$239.15** and **S$246.97** respectively. Counting only hardware, server electricity and internet gives **S$368.76** and **S$376.59**. Selecting S$100/month of additional owner labour raises the corresponding threshold by S$100/month. A rental comparison still requires acceptable performance, capacity and service.

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

## 8. Expanded budget for two desktop nodes in Singapore

The pair draws **450 W combined** in this example. Server electricity is **S$102.36/month**, separate room cooling adds **S$25.59**, and internet adds **S$50 for the pair**. The expanded rows also select **S$1,200 upfront** for two UPS units and assembly/delivery, and a reserve of 3% of pair parts per year. External KVM or remote power, if required, would be a separate purchase. [Per-pair reserve and monthly totals](#monthly-components-at-an-existing-site)

| Pair | Upfront incl. allowances | Monthly budget | 12 months | 24 months | 36 months |
|---|---:|---:|---:|---:|---:|
| Two Intel 270K Plus, 64 GB each | S$8,679 | S$196.65 | S$11,039 | S$13,399 | S$15,759 |
| Two Intel 270K Plus, 128 GB each | S$11,639 | S$204.05 | S$14,088 | S$16,536 | S$18,985 |
| Two AMD 9950X3D, 64 GB each | S$9,441 | S$198.55 | S$11,824 | S$14,206 | S$16,589 |
| Two AMD 9950X3D, 128 GB each | S$12,401 | S$205.95 | S$14,873 | S$17,344 | S$19,816 |

DediJet's two rented 128 GB hosts cost **S$24,978 before tax over 36 months**, or **S$27,226 in an illustrative 9% non-recoverable tax scenario**. The relevant owned comparisons are the **128 GB-per-host** rows. Its 9950X and the owned 9950X3D/Intel CPUs are not identical; validate the queue.

The cheaper 64 GB-per-host models cannot run a job that requires 128 GB on one host. Aggregate memory across runners is not a shared pool. For bursty work, purchasing one node and adding the second only when measured queue pressure warrants it can reduce unused capital; the complete pool must still satisfy the target when compared with AX162.

## 9. Malaysia electricity sensitivity and conditional colocation floors

No complete Malaysian 5995WX non-ECC BOM was established. The following keep the Singapore-procured parts assumption so the effect of hosting location is visible. They **exclude unquoted cross-border logistics, import/transaction taxes, local servicing arrangements and extra hands**. They are not Malaysia local-purchase quotes.

| Scenario | Upfront known costs | Monthly known costs/reserve | 12 months | 24 months | 36 months |
|---|---:|---:|---:|---:|---:|
| Buy A2 MY office sensitivity | S$9,309 | S$126.70 | S$10,830 | S$12,350 | S$13,871 |
| Buy A2 MY Awan4U floor | S$9,135 | S$194.81 | S$11,473 | S$13,811 | S$16,148 |
| Buy A2 MY tower floor | S$8,841 | S$209.37 | S$11,353 | S$13,866 | S$16,378 |

The **expanded Malaysia existing-site sensitivity** changes only the electricity tariff for the Singapore-sourced A2. It keeps the optional S$700 equipment/assembly allowance, S$50 internet and repair reserve. Server electricity is **RM140.76 or S$44.14/month**. Optional room cooling adds **RM35.19 or S$11.04/month**. The Peninsular commercial marginal rate of **RM0.5509088/kWh** includes the renewable-energy levy and November fuel adjustment before any additional invoice-specific tax. The RM20 retail charge is incremental only for a new account. [Commercial tariff assumptions](02-rental-market.md#8-electricity-sources-for-ownership-scenarios)

At 350 W plus 25% cooling, this saves about **S$44.34/month, or S$1,596 over 36 months**, relative to the Singapore reference. That is much less than many multi-year rental differences and can be consumed by logistics or servicing. Lower electricity alone is not a sufficient reason to relocate.

The **AwanPrime 4U floor** uses its RM550/month / 460 W offer, substitutes a S$469 RM44 and S$159 rails, and adds S$200 assembly. The 4U chassis/cooler fit, board clearance, peak power, non-ECC acceptance, setup and tax remain unresolved. A 350 W modeled average is not proof that peaks satisfy 460 W.

The **ServerHosting.MY tower floor** retains the original case, adds S$200 assembly and the listed RM100 setup, then uses RM599/month. Allowed wattage is unconfirmed. A 13 A socket specifies the connection, and the contract must establish the paid power allowance. Generic terms may impose an annual obligation.

Both Malaysian facilities quote a hosting service with network and power terms. The recurring service fee is counted once. Separate electricity and internet prices are unquoted. The existing-site utility switches do not change that fee, and the floor includes no additional office electricity, cooling or internet charge. Required power upgrades or other facility charges would increase the floor.

### Malaysian-local Intel runner pair

For an actual Malaysian local desktop purchase, the separate two-node Intel BOM in the market report is **RM24,008 ≈ S$7,528.76**, near the Singapore parts figure rather than substantially below it. This is two 270K Plus machines with **64 GB and 2 × 2 TB per host** using the locally listed parts; no Singapore-to-Malaysia hardware shipment is assumed for this row.

At an assumed 450 W combined, the pair's server electricity is **RM180.97 or S$56.75/month**. Optional room cooling adds **RM45.24 or S$14.19**, bringing electricity with cooling to **S$70.94/month**. The expanded example selects S$1,200 equivalent UPS/assembly/delivery allowances, S$50/month incremental internet for the pair and a 3% annual parts reserve. These planning allowances can be replaced with actual costs. Unquoted transaction taxes, owner labour or remote-management equipment can be treated separately if applicable. [Monthly components](#monthly-components-at-an-existing-site)

| Malaysia-local Intel pair | Upfront incl. allowances | Monthly budget | 12 months | 24 months | 36 months |
|---|---:|---:|---:|---:|---:|
| 64 GB + 2 × 2 TB per host | S$8,728.76 | S$139.76 | **S$10,405.90** | **S$12,083.05** | **S$13,760.19** |

This is an independent-job pool with 64 GB per host before OS/services/headroom, not one A1 or A2 memory pool. Its queue performance is unmeasured. Compare it with rentals able to run the same jobs at the required throughput, rather than treating 128 GB aggregate as a single-host capacity match. The 128 GB-per-host DediJet/PowerDedi rental pairs in file 02 offer a larger per-job memory envelope.

## 10. Storage and RAM-qualification cost sensitivities

The 20 November hardware refresh found the ADATA LEGEND 900 PRO 2 TB at S$479 and Lexar NM790 4 TB at S$859. The expanded examples keep the S$700 single-host upfront allowances, server electricity, 25% room cooling and S$50 internet constant. Only the parts price and its corresponding 3% annual reserve change. Sustained CI I/O still needs validation. [Manufacturer disclosures and listings](01-hardware-and-performance.md#20-november-storage-price-sensitivities)

| Single host | Parts subtotal | Expanded Singapore budget, 36 months |
|---|---:|---:|
| A2, Samsung reference | S$8,609 | S$15,467 |
| A2, ADATA 2 × 2 TB candidate | S$8,069 | S$14,878 |
| A1, Samsung reference; 16 GB-module qualification open | S$8,891 | S$15,774 |
| A1, Lexar 2 × 4 TB candidate; same RAM qualification gap | S$7,831 | S$14,618 |
| 256 GB + 2 × 4 TB Samsung, qualified-revision RAM candidate | S$9,889 | S$16,862 |
| 256 GB + 2 × 4 TB Lexar candidate | S$8,829 | S$15,707 |

The Samsung 256 GB / 2 × 4 TB case addresses the unverified eight-module 16 GB layout by retaining the stronger 32 GB-revision qualification evidence. At S$16,862 over three years, it is about S$943 below the historical 9%-tax LTD scenario, but about S$527 above the historical tax-net LTD cost of S$16,335. Neither LTD scenario is current stock. This illustrates why RAM qualification, storage and actual tax basis matter before interpreting a small saving.

For the Intel 64 GB-per-host pair, four ADATA drives reduce parts by S$1,080 and the 36-month expanded budget by S$1,177.20, to **S$14,581.36**, holding 450 W average combined power and the other selected allowances constant.

There is also a lower-priced **conditional Singapore rental-pair lead** in file 02: PowerDedi advertises two 9950X / 128 GB / 2 × 1.92 TB hosts at USD 318/month for both, or S$410.11. At unchanged rates, 36 months of **rent alone** is S$14,764.09 before tax and any setup, or S$16,092.86 with an illustrative 9% tax on rent. Setup for this pair was not established. This could undercut the owned 128 GB-per-host pairs, but exact Singapore availability, complete invoice, operator and service conditions remain unresolved. The drives are slightly smaller than the owned 2 TB pair. Do not use it as a firm fulfilled quote.

## 11. Power, network and utilization

Monthly electricity at the stated tariffs and 730 hours, all in **S$**. The 450 W row represents the combined draw of a desktop pair.

| Average wall power | Singapore server | Optional cooling | Singapore with cooling | Malaysia server | Optional cooling | Malaysia with cooling |
|---|---:|---:|---:|---:|---:|---:|
| 100 W | 22.75 | 5.69 | 28.43 | 12.61 | 3.15 | 15.76 |
| 200 W | 45.49 | 11.37 | 56.87 | 25.22 | 6.31 | 31.53 |
| 350 W | 79.61 | 19.90 | 99.52 | 44.14 | 11.04 | 55.18 |
| 450 W | 102.36 | 25.59 | 127.95 | 56.75 | 14.19 | 70.94 |
| 500 W | 113.73 | 28.43 | 142.17 | 63.06 | 15.76 | 78.82 |

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
