# Direct hardware payback: electricity and internet chosen independently

[Home](../../README.md) · [Buy vs rent](README.md)

**Rental snapshot** · 141 offers through `175399c`

[Choose costs](#3-electricity-cooling-and-internet-separate-inputs) · [Singapore payback](#4-singapore-direct-payback-against-selected-monthly-rental-quotes) · [12/24/36-month budgets](#5-direct-cash-budgets-at-12-24-and-36-months) · [Malaysia payback](#6-malaysia-separate-electricity-sensitivity-and-local-purchase) · [Optional costs](#7-additional-costs-stay-separate-and-optional)

**Updated: 20 November 2026.** This is the primary purchase-versus-rental view requested by the user. **Office, room, floor-space and premises rent are excluded from every scenario**, including optional sensitivities. Singapore is the first purchase/hosting preference; Malaysia is second.

**The analysis covers 141 rental offers through `175399c`** across the [initial 104-offer payback snapshot](07-all-rentals-break-even.md), [15 subsequent additions](08-latest-rental-comparisons.md) and [22 further additions](09-expanded-rental-comparisons.md), with [current corrections to existing offers](10-current-offer-updates.md). Stable original IDs are preserved. New quotes inherit their evidence dates; a cost calculation does not establish new stock or payment eligibility.

## 1. What “the hardware has cost me zero” means

Here it means that the rental bills avoided have recovered the purchase price and whichever operating costs you choose to count. It does **not** mean the hardware purchase is refunded or that electricity and internet become free after the crossover.

For a rental you could otherwise keep at monthly price `R`, hardware price `H`, optional monthly server electricity `E`, and independently optional monthly incremental internet `I`:

`Unrecovered cost after N months = H + N × (selected E + selected I) − N × R`

The hardware is recovered in this model when that balance reaches zero or below. The pure hardware-versus-recurring-rent comparison is **`H / R`**. Each of the four operating scenarios is **`H / (R − selected E − selected I)`**. These calculations exclude rental setup; this is appropriate for an existing lease whose setup was already paid, provided the rental can actually be stopped.

For choosing between a **new purchase and a new rental** with a known, avoidable setup payment `F`, the corresponding comparison is **`(H − F) / (R − selected E − selected I)`**. Avoiding a large setup fee can shorten the purchase crossover; it does not reduce the hardware seller's invoice. If setup is unknown, the setup-adjusted result is unknown. Previously paid setup is sunk: do not deduct it again.

The four scenarios are:

| Scenario | Electricity counted | Internet counted | Owned cost over N months |
|---|---|---|---|
| **Hardware only** | No | No | `H` |
| **Hardware + electricity** | Yes | No | `H + N×E` |
| **Hardware + internet** | No | Yes | `H + N×I` |
| **Hardware + electricity + internet** | Yes | Yes | `H + N×(E+I)` |

An excluded cost is excluded from this comparison, not asserted to be physically zero. Internet can have zero **incremental** cost if an existing connection is adequate and its bill does not increase. Electricity is calculated from assumed whole-machine wall consumption, including the PSU and internal fans. Additional room air-conditioning is a separately selectable sensitivity below, not silently included in `E`.

## 2. Hardware prices used

These are the existing source-linked [Singapore hardware BOMs](01-hardware-and-performance.md) and [Malaysian local BOM](02-rental-market.md#7-malaysian-local-purchase-cross-check). Prices are sums of observed retail listings, not reserved, assembled, consistently tax-normalized invoices. CPU, board, RAM, SSD, case, PSU and CPU cooler are in `H`; UPS, assembly/delivery allowance and repair reserve are not.

| Owned configuration | Hardware only, SGD | Capacity / procurement qualification |
|---|---:|---|
| SG: 5995WX, 256 GB, Samsung 2 × 2 TB (A2) | 8,609.40 | One 256 GB host |
| SG: 5995WX, 256 GB, ADATA 2 × 2 TB | 8,069.40 | A2; validate sustained SSD I/O |
| SG: 5995WX, 128 GB, Samsung 2 × 4 TB (A1) | 8,891.00 | Eight 16 GB DIMMs still need qualification |
| SG: 5995WX, 128 GB, Lexar 2 × 4 TB | 7,831.00 | Same RAM qualification condition |
| SG: 5995WX, 256 GB, Lexar 2 × 4 TB | 8,829.40 | Both A1/A2 capacities; qualify exact RAM revision |
| SG: two Intel 270K Plus, 64 GB each, ADATA 2 × 2 TB each | 6,399.20 | Two separate 64 GB memory pools |
| SG: two Intel 270K Plus, 128 GB each, Samsung 2 × 2 TB each | 10,439.20 | Two separate 128 GB memory pools |
| MY-local: two Intel 270K Plus, 64 GB each, Samsung 2 × 2 TB each | 7,528.76 | RM24,008; separately sourced Malaysian parts |

Capacity matching does not prove performance matching. Every owned option remains conditional on the [actual Rust/TypeScript/Docker latency and throughput acceptance test](04-validation-and-procurement.md). A two-host pool cannot give one job their combined RAM.

## 3. Electricity, cooling and internet: separate inputs

The model uses **730 hours per month**, **350 W average wall power for one workstation** or **450 W combined for the two-desktop pool**. Both power figures are assumptions, not measurements. Replace them with measured duty-cycle averages. CPU TDP and PSU nameplate watts do not establish consumption.

**Singapore:** [SP's Q4 2026 reference](https://www.spgroup.com.sg/our-services/utilities/tariff-information), rechecked on 20 November, is **S$0.3116/kWh including GST**. Use the actual marginal electricity rate if different.

**Peninsular Malaysia:** retain the [commercial marginal calculation and primary sources](02-rental-market.md#8-electricity-sources-for-ownership-scenarios), **RM0.5509088/kWh**, including the stated levy and November AFA, before any additional invoice-specific tax. The [November AFA source](https://www.st.gov.my/AFA) was rechecked at RM0.0360/kWh. It is not a Sabah/Sarawak or household-tariff calculation. A new electricity account can add the separate RM20 retail charge; the main table assumes an existing meter.

FX is pinned to **19 November 2026**: EUR 1 = SGD 1.4176 = USD 1.0992 = MYR 4.5205 = GBP 0.83581. Convert GBP directly as `GBP / 0.83581 × 1.4176`; use full-precision derived rates before rounding displayed values. [FX methodology](../../METHODOLOGY.md#ci-ownership-comparison).

| Deployment and assumed draw | Server electricity `E`, SGD/month | Optional extra cooling `C = 25%×E`, SGD/month | Incremental internet `I`, SGD/month |
|---|---:|---:|---:|
| Singapore, 350 W workstation | 79.61 | 19.90 | 50.00 |
| Singapore, 450 W combined pair | 102.36 | 25.59 | 50.00 |
| Malaysia, 350 W workstation sensitivity | 44.14 | 11.04 | 50.00 |
| Malaysia, 450 W combined local pair | 56.75 | 14.19 | 50.00 |

**Internet's S$50/month is a replaceable planning allowance, not an ISP quote.** It is per connection, including for a pair sharing the same connection. In Malaysia it equals approximately **RM159.44** at the comparison FX. Set it independently to zero, your actual incremental charge, or a separately priced line. Connection setup, equipment, public IP and overage charges stay separate if required; they are not established as free.

For the Malaysia-local pair, server electricity is **RM180.97** and optional cooling **RM45.24** per month. For the Singapore workstation, the canonical four monthly operating amounts are **S$0 / S$79.61 / S$50 / S$129.61**. Enabling the optional 25% cooling changes electricity to S$99.52 and electricity-plus-internet to S$149.52. Office rent remains excluded.

## 4. Singapore: direct payback against selected monthly rental quotes

Each four-scenario cell gives **fractional service months → first whole month**. The four columns deduct **known new-rental setup**; the separate `H/R` column is the hardware-versus-recurring-rent answer **without** a setup credit. If you already have the rental, use `F=0`, the formula above or [the all-rental matrix's recurring-only entries](07-all-rentals-break-even.md).

These are monthly-rate planning equations, not promises of allocation or renewal. **PlusClouds' final term is unconfirmed**, so its figures are explicitly monthly-equivalent sensitivities. Whole months are computed from unrounded results: BizoSiz A1 with both utilities is **38.0006**, therefore month **39**; PlusClouds A2 with electricity alone is **32.0022**, therefore month **33**. Display rounding must not turn either into an earlier pass.

All amounts are SGD. Rental quotes retain their source tax treatment and exclude unquoted tax/IP/network charges; Hetzner rows explicitly include one IPv4 and exclude tax. The heterogeneous retail prices are not claimed to be tax-normalized against these quotes. [Native quotes and evidence](02-rental-market.md), [104 original rental rows](05-repository-rental-comparison.md), [15-offer follow-up](08-latest-rental-comparisons.md), [22-offer expansion](09-expanded-rental-comparisons.md) and [current corrections](10-current-offer-updates.md).

| Rental / owned capacity | Hardware H | Rent R/month | Known setup F | H/R, months | Neither utility | Electricity only | Internet only | Both utilities |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| UHost A2, Europe | 8,609.40 | 283.73 | 154.76 | 30.34 | 29.80 → **30** | 41.42 → **42** | 36.17 → **37** | 54.86 → **55** |
| BizoSiz A2, Europe | 8,609.40 | 359.82 | 143.15 | 23.93 | 23.53 → **24** | 30.21 → **31** | 27.33 → **28** | 36.78 → **37** |
| PlusClouds A2, Europe; term unconfirmed | 8,609.40 | 324.63 | 768.34 | 26.52 | 24.15 → **25** | 32.0022 → **33** | 28.55 → **29** | 40.21 → **41** |
| Progressive Robot A2; location and term unconfirmed | 8,609.40 | 374.83 | 149.25 | 22.97 | 22.57 → **23** | 28.66 → **29** | 26.04 → **27** | 34.50 → **35** |
| BizoSiz A1, Europe | 8,891.00 | 359.82 | 143.15 | 24.71 | 24.31 → **25** | 31.22 → **32** | 28.24 → **29** | 38.0006 → **39** |
| PlusClouds A1, Europe; term unconfirmed | 8,891.00 | 324.63 | 582.63 | 27.39 | 25.59 → **26** | 33.91 → **34** | 30.25 → **31** | 42.60 → **43** |
| Progressive Robot A1; location and term unconfirmed | 8,891.00 | 374.83 | 149.25 | 23.72 | 23.32 → **24** | 29.61 → **30** | 26.91 → **27** | 35.65 → **36** |
| Hetzner A2 regular + one IPv4, before tax | 8,609.40 | 1,196.45 | 593.97 | 7.20 | 6.70 → **7** | 7.18 → **8** | 6.99 → **7** | 7.51 → **8** |
| Hetzner A1 regular + one IPv4, before tax | 8,891.00 | 870.41 | 430.95 | 10.21 | 9.72 → **10** | 10.70 → **11** | 10.31 → **11** | 11.42 → **12** |

UHost's unknown complete service/network terms, BizoSiz's stock/payment conditions, and PlusClouds' final term/supply remain open. These figures prioritize obtaining quotes; they do not endorse a supplier. An existing low-price rental should use its actual renewal invoice and cancellation date, not the new-order Hetzner tariff. Current AX162-LTD inventory was not established, so no purchasable LTD offer is introduced here.

Progressive Robot's two additions each use a **GBP221 monthly listing plus GBP88 setup**, not a USD payment quote. Its server country/city, final tax, minimum term and allocation remain unresolved; a UK operator address does not establish UK deployment. These are monthly-equivalent planning calculations. [The 15-offer update](08-latest-rental-comparisons.md) also retains Nindohost's USD234/month A2 as a quote with unknown setup and models AmazingRDP's actual annual prepayment separately from its monthly-equivalent payback.

### No setup credit: existing lease versus owned A2

For clarity, the A2 / UHost calculation without credit for an old setup payment is:

| Owned fees counted | Monthly selected cost | H/(R−selected cost), months → whole month |
|---|---:|---:|
| Neither | 0.00 | 30.34 → **31** |
| Electricity only | 79.61 | 42.18 → **43** |
| Internet only | 50.00 | 36.84 → **37** |
| Both | 129.61 | 55.86 → **56** |

If an existing contract cannot be cancelled immediately, the avoided rental savings start only when the bill actually stops. Add unavoidable overlap/migration and remaining obligations to the appropriate cash flow. This research has no access to an existing customer contract or invoice.

### Lower-price storage alternatives

Same whole-machine power assumption; storage performance and procurement conditions remain. These four columns also use known **new-rental setup**.

| Alternative and rental | Hardware H | Rent R/month | Known setup F | H/R, months | Neither utility | Electricity only | Internet only | Both utilities |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A2 ADATA versus UHost A2 | 8,069.40 | 283.73 | 154.76 | 28.44 | 27.90 → **28** | 38.78 → **39** | 33.86 → **34** | 51.36 → **52** |
| A2 ADATA versus BizoSiz A2 | 8,069.40 | 359.82 | 143.15 | 22.43 | 22.03 → **23** | 28.29 → **29** | 25.58 → **26** | 34.43 → **35** |
| 256 GB + Lexar 2 × 4 TB versus BizoSiz A1 | 8,829.40 | 359.82 | 143.15 | 24.54 | 24.14 → **25** | 31.00 → **31** | 28.04 → **29** | 37.73 → **38** |
| 256 GB + Lexar 2 × 4 TB versus PowerDedi Singapore 9454P; lead only | 8,829.40 | 630.65 | 0.00 | 14.00 | 14.0006 → **15** | 16.02 → **17** | 15.21 → **16** | 17.62 → **18** |

The PowerDedi listing has contradictory Singapore availability/location labels, unresolved fulfillment and restrictive payment terms. The [new first-month coupon check](10-current-offer-updates.md) applies to Amsterdam; it is not applied to this separate Singapore lead. Its advertised zero setup is used only as a conditional scenario. The owned 256 GB / 2 × 4 TB option matches its capacity more closely than the smaller-drive A2 build; actual CI and SSD behavior remain unmeasured.

## 5. Direct cash budgets at 12, 24 and 36 months

For the **S$8,609.40 A2 Singapore workstation**, these totals include only hardware and the utilities you select. No UPS, assembly allowance, maintenance reserve, additional cooling, labour, financing, resale or office rent is included.

| Scenario | Electricity/month | Internet/month | 12 months | 24 months | 36 months |
|---|---:|---:|---:|---:|---:|
| Hardware only | 0.00 | 0.00 | 8,609.40 | 8,609.40 | 8,609.40 |
| Hardware + electricity | 79.61 | 0.00 | 9,564.77 | 10,520.13 | 11,475.50 |
| Hardware + internet | 0.00 | 50.00 | 9,209.40 | 9,809.40 | 10,409.40 |
| Hardware + both | 79.61 | 50.00 | 10,164.77 | 11,720.13 | 13,275.50 |
| UHost new rental: known setup + rent | No separate charge quoted | Terms unconfirmed | 3,559.48 | 6,964.19 | 10,368.91 |

At 36 months, hardware-only ownership is **S$1,759.51 below** UHost's known rental charges. Counting both server electricity and S$50 internet instead puts ownership **S$2,906.59 above** those charges. This is why a single bundled ownership total cannot answer all four versions of the user's question. Unquoted supplier charges and actual performance still affect the decision.

## 6. Malaysia: separate electricity sensitivity and local purchase

### Same single workstation, hosted in Malaysia

This retains **Singapore-procured A2 hardware at S$8,609.40**, changes only the marginal electricity input to **S$44.14/month**, and leaves internet independently at S$50. No complete Malaysian 5995WX BOM was verified; cross-border delivery, taxes and servicing are unquoted and excluded from these direct sensitivities, not declared zero.

| Rental / owned capacity | Hardware H | Rent R/month | Known setup F | H/R, months | Neither utility | Electricity only | Internet only | Both utilities |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| UHost A2, Europe | 8,609.40 | 283.73 | 154.76 | 30.34 | 29.80 → **30** | 35.29 → **36** | 36.17 → **37** | 44.60 → **45** |
| BizoSiz A2, Europe | 8,609.40 | 359.82 | 143.15 | 23.93 | 23.53 → **24** | 26.82 → **27** | 27.33 → **28** | 31.87 → **32** |
| PlusClouds A2, Europe; term unconfirmed | 8,609.40 | 324.63 | 768.34 | 26.52 | 24.15 → **25** | 27.95 → **28** | 28.55 → **29** | 34.02 → **35** |

### Malaysia-local Intel pair

For the locally sourced **RM24,008 / S$7,528.76 pair**, the four monthly costs are **S$0 / S$56.75 / S$50 / S$106.75**. Each host has **64 GB RAM and two 2 TB drives**. It is not one 128 GB or 256 GB memory pool. The following is its direct purchase-and-utilities budget:

| Scenario | Electricity/month | Internet/month | 12 months | 24 months | 36 months |
|---|---:|---:|---:|---:|---:|
| Hardware only | 0.00 | 0.00 | 7,528.76 | 7,528.76 | 7,528.76 |
| Hardware + electricity | 56.75 | 0.00 | 8,209.78 | 8,890.81 | 9,571.83 |
| Hardware + internet | 0.00 | 50.00 | 8,128.76 | 8,728.76 | 9,328.76 |
| Hardware + both | 56.75 | 50.00 | 8,809.78 | 10,090.81 | 11,371.83 |

### Desktop-pool rental comparisons

The **Singapore-owned 128 GB-per-host Intel pair** has a comparable per-host capacity envelope to DediJet's two Singapore 9950X / 128 GB / 2 × 2 TB hosts. The **Malaysia-owned 64 GB-per-host pair does not**: its row below is price-only and relevant only if every required job fits comfortably within 64 GB after overhead and the measured queue passes. Do not rank it as a full capacity match. The CPUs and physical locations also differ.

| Pair versus DediJet two-host quote | Hardware H | Rent R/month | Known setup F | H/R, months | Neither utility | Electricity only | Internet only | Both utilities |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| SG Intel 128 GB per host; capacity-comparable | 10,439.20 | 693.84 | 0.00 | 15.05 | 15.05 → **16** | 17.65 → **18** | 16.21 → **17** | 19.28 → **20** |
| MY Intel 64 GB per host; price-only, less RAM per job | 7,528.76 | 693.84 | 0.00 | 10.85 | 10.85 → **11** | 11.82 → **12** | 11.69 → **12** | 12.82 → **13** |

No equivalent, fully specified Malaysian rental pool was established. DediJet's advertised availability, payment method and allocation of two machines need confirmation. PowerDedi's cheaper pair has unestablished setup; therefore no known setup-adjusted payback is asserted for it. These are [regional leads](02-rental-market.md), not allocated hosts.

## 7. Additional costs stay separate and optional

| Cost | Direct four-scenario tables | How to add it when applicable |
|---|---|---|
| Server electricity | Independent yes/no switch | `E = average kW × 730 × actual marginal tariff` |
| Internet recurring charge | Independent yes/no switch | Actual incremental `I`; S$50 is only the illustrated allowance |
| Extra room cooling | Excluded by default | Add measured incremental cooling; sensitivity `C=25%×E` only if electricity is counted |
| UPS | Excluded | Optional upfront allowance: S$500 one workstation / S$1,000 pair; replace with quote |
| Assembly / delivery | Excluded | Optional S$200 upfront allowance; replace with quote |
| Repair reserve | Excluded | Optional annual 3% of parts / 12; earmarked funds, not observed expenditure |
| Additional ownership labour / remote management | Excluded | Separately priced only if wanted; common CI administration is not automatically an ownership-only cost |
| ISP setup / public IP / router / overage | Not established | Keep one-time and recurring amounts distinct; do not assume an excluded amount is free |
| Payment processing / FX spread / financing | Not established, excluded | Enter actual purchase fee upfront, rental fee on its applicable invoice, or financing cash flow; do not double-count financed principal as cash hardware payment |
| Tax | Preserve each observed source basis | Add only actual nonrecoverable amounts; known-tax and unknown-tax prices are not automatically comparable |
| Resale proceeds | Excluded | Do not assume a sale value to accelerate payback |
| **Office / room / floor-space / premises rent** | **Always excluded** | **Never add it to any scenario in this research** |

For explicit optional extras `A` upfront and `M` monthly, the extended new-order formula is `(H + A − F) / (R − E − I − C − M)`. Use only the selected costs, and add any actual rental-side recurring fees to `R`. All excluded charges remain outside the stated result; if a required invoice item is unknown, a complete all-in result is unknown.

### Cooling and earlier expanded-budget reconciliation

The prior [expanded budgets](03-rent-vs-buy-tco.md) used 25% cooling, S$700 workstation UPS/assembly allowances, and a 3% annual reserve. They remain available as optional planning cases, with electricity, cooling, internet and reserve broken out. They are not the direct hardware-only figures.

| SG A2 versus new UHost rental | Owned upfront | Owned monthly costs | Fractional months → whole month |
|---|---:|---:|---:|
| Hardware + server electricity + internet | 8,609.40 | 129.61 | 54.86 → **55** |
| Also count 25% cooling | 8,609.40 | 149.52 | 63.00 → **63** |
| Also add S$700 upfront and 3% annual reserve | 9,309.40 | 171.04 | 81.24 → **82** |

This also explains why the old tax-inclusive, extras-inclusive regular-Hetzner comparison cannot be copied into a hardware-only table. For taxes, the earlier 9% Singapore-billing case is a sensitivity only; billing residence, registration and recoverability were not established. Provider EUR and USD tariff schedules can differ; a converted EUR tariff is not a USD invoice quote.

**Colocation is a separate service choice.** The earlier datacenter rack/tower plans bundle space, power and connectivity in one provider price. Their electricity and internet subprices are unquoted, so an independent toggle cannot be honestly implemented by subtracting invented components. Keep the quoted colocation package as its own optional service scenario, with no office rent and no duplicated office electricity/internet. Request itemized terms if this route is chosen.

## 8. Contracts, rounding and situations with no payback

For a usual purchase with `H > F`, there is no future crossover if `R` is at most the selected owned monthly cost. If `H ≤ F`, ownership may already cost less at purchase; check the direction of monthly costs rather than blindly clamping the formula to zero. If running ownership costs exceed rent, an initial advantage can reverse. All examples above have positive initial purchase gaps and positive monthly savings under their selected assumptions.

The whole-month number is the first integer service-month whose **modeled cumulative cost** satisfies the comparison, calculated from full-precision inputs. It is not a refund date or an assurance of remaining useful hardware life. It also assumes monthly comparability and that the rental can be avoided from the beginning of that period. A five-year arithmetic crossover is conditional on the machine continuing to provide acceptable service for that long.

For prepaid `p`-month blocks costing `P`, rental cash needed for a horizon `N≥1` is `F + ceil(N/p)×P`, assuming the same terms renew. Monthly equivalent `R=P/p` is useful for an economic comparison but is not the actual payment schedule. Buying may appear cheaper at the first prepayment, become more expensive before that paid term ends, then become cheaper at renewal. Do not call the first temporary crossing permanent payback. Monthly-paid minimum contracts also create liabilities without implying the entire term was paid on day one.

The [initial 104-offer payback appendix](07-all-rentals-break-even.md), [next 15 offers](08-latest-rental-comparisons.md) and [following 22 offers](09-expanded-rental-comparisons.md) keep these cases distinct across all 141 rows in that rental snapshot, mark unknown setup/terms, and exclude capacity-unmatched offers from equivalence rankings. The initial appendix's regular Hetzner row preserves the frozen rental table's **bare** server price. This file's regular Hetzner rows include one IPv4.

A verified first-month-only rental credit lowers rental costs once; it does not lower recurring rent. With credit `C`, a new monthly-rental comparison becomes `(H − F + C)/(R − O)` when the crossing occurs after that credit. [File 10](10-current-offer-updates.md) applies this to the European PowerDedi offer and preserves the historical no-coupon baseline.

## 9. Practical interpretation

- **If both electricity and internet are already covered or intentionally excluded**, use `H/R` for an existing rental or the “neither utility” setup-adjusted column for a new one.
- **If only electricity increases**, use its column and your measured average power; internet remains independently zero.
- **If a new connection is needed but electricity is excluded**, use the internet-only column, keeping its installation costs separate.
- **If both bills increase**, use both columns, then choose explicitly whether additional cooling or other optional costs belong in your decision.
- **Always compare actual performance and per-job memory before interpreting payback.** Saved rent is meaningful only if the owned system does the required work at the accepted latency and throughput.

No office rent, purchase, supplier contact, hardware reservation, actual workload replay or wall-power measurement is part of this update. GPT-6.2 Astra max produced the research and calculations; GPT-6.2 Sol max independently reviews the final arithmetic and methodology.
