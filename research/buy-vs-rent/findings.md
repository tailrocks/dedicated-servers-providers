# Ownership costs and CI findings

[Start](../../README.md) / [Buy or rent](README.md) / Detailed findings

Jump to [capacity classes](#reference-capacity-classes), [owned hardware](#owned-hardware-shortlist), [direct payback](#direct-hardware-payback-the-primary-comparison), [expanded budgets](#optional-expanded-financial-comparison), or [performance checks](#performance-and-procurement-gates).

**Updated: 20 November 2026 (Asia/Ho_Chi_Minh).**

**Buy/host priority:** Singapore first, Malaysia second.

**Rental coverage:** the **141-offer snapshot through `175399c`**: the original 104 plus 15 follow-up and 22 expansion additions, with worldwide locations and evidence retained. The canonical rental table subsequently expanded to 170 rows; the additional 29 rows are not included in these ownership calculations.

**Workload:** Linux Rust/TypeScript builds and tests in Docker containers.

**Owned hardware:** non-ECC desktop/workstation memory; performance first, price second.

**Primary cost comparison:** hardware alone, hardware plus electricity, hardware plus internet, or hardware plus both. **Office / room / floor-space / premises rent is excluded in every scenario.** Cooling and other ownership allowances are separate optional additions.

## Decision

**Choose which costs to count before deciding whether to buy.** With electricity and internet excluded, the S$8,609.40 A2 machine equals 30.34 months of UHost's recurring rent. Against a new rental including its avoidable setup, buying crosses in month 30 with neither utility, month 42 with electricity, month 37 with internet, and month 55 with both. Stock, final invoice, network, operator and payment conditions still need acceptance. Several cheaper European quotes can beat ownership when running costs are counted; regular Hetzner new-order pricing alone gives a different answer.

**If Singapore placement or local physical control is required, a 5995WX with 256 GB non-ECC RAM is the strongest single-host ownership candidate found for testing.** Prefer an existing suitable office over assuming that cheap 1U colocation will accept a large workstation. Malaysia colocation has lower published leads but unresolved power, chassis, contract and local-service costs.

**No proposed owned configuration is proven to be within 3–5% of the user's actual CI.** A public +3% multicore Clang observation is a screening result from a different 5995WX system. The [acceptance procedure](04-validation-and-procurement.md) requires both critical-job latency and busy-queue throughput by default before declaring CI equivalence.

## Files

| File | Purpose |
|---|---|
| [01-hardware-and-performance.md](01-hardware-and-performance.md) | Exact Singapore BOMs, compiler evidence, RAM qualification, storage alternatives, cooling and PSU requirements |
| [02-rental-market.md](02-rental-market.md) | Singapore/Malaysia rental and colocation leads; Malaysian local BOM; electricity and currency sources |
| [03-rent-vs-buy-tco.md](03-rent-vs-buy-tco.md) | Optional expanded 12/24/36-month budgets, with electricity, cooling, internet and reserves broken out |
| [04-validation-and-procurement.md](04-validation-and-procurement.md) | Actual CI replay, strict acceptance gates and complete quote requirements |
| [05-repository-rental-comparison.md](05-repository-rental-comparison.md) | Initial 104-offer snapshot: A1/A2 capacity matching, native terms and horizon costs |
| [06-direct-payback.md](06-direct-payback.md) | **Start here:** hardware-only rent equivalents, four independent electricity/internet scenarios, first whole break-even month, Singapore and Malaysia |
| [07-all-rentals-break-even.md](07-all-rentals-break-even.md) | Four-scenario payback for the initial 104 offers; setup unknowns, prepaid cash and commitment distinctions |
| [08-latest-rental-comparisons.md](08-latest-rental-comparisons.md) | Fifteen additions and the combined 119-offer snapshot; GBP quotes, horizon costs, four-scenario payback and prepaid cash |
| [09-expanded-rental-comparisons.md](09-expanded-rental-comparisons.md) | Twenty-two additions and the 141-offer snapshot totals; native charges, four utility scenarios, annual and multi-year cash commitments |
| [10-current-offer-updates.md](10-current-offer-updates.md) | Current corrections to existing stable IDs, including PowerDedi’s first-month coupon and its effect on payback |
| [Integration and corrections log](../2026-11-20-buy-vs-rent.md) | Changes from the earlier standalone hardware research and exact source snapshot |

The [seven-column rental catalogue](../../rentals/README.md) remains the canonical provider list. This folder adds a workload-specific ownership decision; it does not silently change the original rental table's raw-capacity floor or label every listed CPU as a measured CI match.

## Reference capacity classes

| Profile | CPU | Minimum installed RAM | Drive layout | Nominal mirrored capacity |
|---|---|---:|---|---:|
| **A1: AX162-1** | EPYC 9454P, 48 cores / 96 threads | 128 GB | 2 × 3.84 TB NVMe | 3.84 TB |
| **A2: AX162-2** | Same | 256 GB | 2 × 1.92 TB NVMe | 1.92 TB |

Mirroring is the comparison convention, not a claim that the user's current rental is already configured as RAID1. Filesystem overhead and operating headroom reduce available space. CPU, SSD latency/endurance, memory protection, network and support are separate acceptance questions.

The repository's general minimum is only 128 GB plus 2 TB **raw** SSD. In the **141-offer ownership snapshot, 93 distinct rows meet at least one of these stricter capacity classes**: 41 only A1, 50 only A2, two both; 48 meet neither. This gives **95 capacity-profile comparisons**. No row in that snapshot establishes allocation in Singapore or Malaysia. Files 05/07 preserve the initial stable IDs 001–104, file 08 covers additions N01–N15, and file 09 covers E01–E22; file 10 overlays updates to existing IDs. Together they retain every offer in the 141-row snapshot and its evidence. A one-drive or undersized host is not presented as equivalent to a mirrored owned system.

## Owned hardware shortlist

All prices are **SGD parts estimates**, not one assembled tax-normalized quote. Supplier quantities, exact memory revision, BIOS and whole-system support remain to be confirmed. The source-linked BOM is in file 01.

| Candidate | RAM and storage | Samsung-drive reference | Lower-price drive candidate | Fit |
|---|---|---:|---:|---|
| **Threadripper PRO 5995WX / ASUS WRX80** | **256 GB: 8 × 32 GB non-ECC DDR4-3200; 2 × 2 TB** | **S$8,609.40** | **S$8,069.40**, ADATA | One large host; A2 capacity |
| Same platform | 128 GB: 8 × 16 GB; 2 × 4 TB | S$8,891.00 | S$7,831.00, Lexar | A1 capacity; exact eight-module 16 GB qualification open |
| Same platform, larger RAM/storage | 256 GB: 8 × 32 GB; 2 × 4 TB | S$9,889.40 | S$8,829.40, Lexar | Covers both capacity classes; stronger exact RAM-revision evidence |
| **Two Intel Core Ultra 7 270K Plus hosts** | **64 GB and 2 × 2 TB per host** | **S$7,479.20 total** | **S$6,399.20 total**, ADATA | Independent-job pool; each job fits one 64 GB host after overhead |
| Two Intel 270K Plus hosts | 128 GB and 2 × 2 TB per host | S$10,439.20 total | See drive sensitivity | Independent-job pool; no shared 256 GB memory space |
| Two Ryzen 9950X3D hosts | 64 GB / 128 GB per host; 2 × 2 TB each | S$8,241.20 / S$11,201.20 total | See drive sensitivity | AMD alternative; validate project-specific benefit |

The 5995WX option is workstation-class hardware with ordinary non-ECC DIMMs on the chosen board. Modern 9970X/TRX50 configurations are documented only as an optional ECC-RDIMM exception. A single mainstream consumer desktop is not established here as a full AX162 throughput replacement.

Lower-priced storage is not assumed equally fast under sustained mixed CI I/O. ADATA's cited data sheet leaves the NAND cell type and dedicated DRAM unspecified; Samsung documents TLC and DRAM. The Lexar offer's displayed delivery estimate is not a reservation of two drives.

## Direct hardware payback: the primary comparison

For an existing rental with avoidable future monthly charge `R`, hardware `H` is recovered after `H / (R − selected electricity − selected internet)` months. With both utilities excluded, this is simply **`H/R`**. An already paid setup is sunk. When choosing between a **new** rental and purchase, deduct only its known avoidable setup `F` from the numerator. After break-even, the hardware is paid for through avoided rent; future utility bills still exist.

The Singapore single-host direct inputs are **S$79.6138/month server electricity**, assuming 350 W average wall power and 730 hours, and **S$50/month internet** as an independent, replaceable incremental allowance. Optional extra room cooling is **S$19.90345/month**. The direct table does not add cooling, UPS, assembly allowances, repairs, labour or office rent.

| New rental / owned profile | Hardware only | Known recurring rental/month | Hardware ÷ recurring rent | Neither utility: first whole month | Electricity only | Internet only | Both utilities |
|---|---:|---:|---:|---:|---:|---:|---:|
| UHost Europe / A2 | S$8,609.40 | S$283.73 | 30.34 months | **30** | **42** | **37** | **55** |
| BizoSiz Europe / A2 | S$8,609.40 | S$359.82 | 23.93 months | **24** | **31** | **28** | **37** |
| PlusClouds Europe / A2, term unconfirmed | S$8,609.40 | S$324.63 | 26.52 months | **25** | **33** | **29** | **41** |
| Progressive Robot / A2, location and term unconfirmed | S$8,609.40 | S$374.83 | 22.97 months | **23** | **29** | **27** | **35** |
| BizoSiz Europe / A1 | S$8,891.00 | S$359.82 | 24.71 months | **25** | **32** | **29** | **39** |
| PlusClouds Europe / A1, term unconfirmed | S$8,891.00 | S$324.63 | 27.39 months | **26** | **34** | **31** | **43** |
| Progressive Robot / A1, location and term unconfirmed | S$8,891.00 | S$374.83 | 23.72 months | **24** | **30** | **27** | **36** |
| Hetzner regular + IPv4, before tax / A2 | S$8,609.40 | S$1,196.45 | 7.20 months | **7** | **8** | **7** | **8** |

The four whole-month columns credit known new-rental setup; `H/R` does not. Unknown taxes/network charges and supplier limitations remain. Actual prices and native quotes, fractions, existing-lease versions, alternative drives and Malaysia are in [06](06-direct-payback.md). Whole months use unrounded values; BizoSiz A1 with both is 38.0006, so month 39. PlusClouds' unconfirmed term makes its result a monthly-equivalent sensitivity, not a promised payment/cancellation schedule.

For A2 Singapore ownership, the direct **36-month costs** are:

| Costs selected | Electricity/month | Internet/month | Hardware + selected costs over 36 months |
|---|---:|---:|---:|
| Neither utility | Excluded | Excluded | **S$8,609.40** |
| Electricity only | S$79.61 | Excluded | **S$11,475.50** |
| Internet only | Excluded | S$50 | **S$10,409.40** |
| Both utilities | S$79.61 | S$50 | **S$13,275.50** |

UHost's known 36-month rent plus setup is **S$10,368.91**. Thus hardware alone is below it, while including both selected bills puts ownership above it. Do not describe either conclusion as universal. The [initial break-even appendix](07-all-rentals-break-even.md), [15-offer follow-up](08-latest-rental-comparisons.md) and [22-offer expansion](09-expanded-rental-comparisons.md) together preserve all **141 offers**, **95 capacity-profile comparisons over 93 matching offers**, missing fees, and prepaid cash flows. Among the stated-setup matches, **six** offers are cheaper at 36 months than the direct hardware-plus-both-utilities models; **fifteen** are cheaper than the optional expanded budgets. No stated-setup capacity match is cheaper than the corresponding parts-only purchase at 36 months. Files 05 and 08 retain their earlier seven- and nine-offer expanded counts within their pinned snapshots.

In the 141-offer snapshot, UHost A2 and PlusClouds A1 have the lowest stated-setup 36-month quotes for their respective capacity classes. The 22 new rows add six offers below the expanded budgets: Wsla A2, ServerWala’s four annual options, and ServerWala Helsinki A1 monthly. They add none below the direct hardware-plus-both-utilities budgets. Nindohost A2 remains USD234/month with setup, term and stock unresolved. Progressive Robot’s two listings remain part of the prior 119-offer snapshot. File 09 distinguishes Alpenhost’s exact two-/three-year upfront totals from unquoted separate setup, and file 10 applies PowerDedi’s one-time coupon without changing its recurring rent. Payment-specific and non-orderable watchlist leads remain separately qualified.

## Optional expanded financial comparison

The following earlier budgets include UPS/assembly allowances, cooling and a repair reserve in addition to electricity and internet. They remain useful as explicitly selected planning cases, **not the hardware-only answer**. Office rent is still excluded.

These rental figures are **known charges before unquoted taxes/network/IP costs**, with fixed 19 November FX and unchanged renewal rates assumed. They are not final tax-normalized invoices. Ownership includes the explicit allowances below.

| Scenario | Capacity class | 12 months | 24 months | 36 months |
|---|---|---:|---:|---:|
| UHost Europe, USD 220/month + 120 setup | A2 | S$3,559 | S$6,964 | **S$10,369** |
| BizoSiz Europe, USD 279/month + 111 setup | Separate A1 / A2 carts | S$4,461 | S$8,779 | **S$13,097** |
| PlusClouds Europe, EUR 229/month + 411 setup | A1 | S$4,478 | S$8,374 | **S$12,269** |
| PlusClouds Europe, EUR 229/month + 542 setup | A2 | S$4,664 | S$8,559 | **S$12,455** |
| Own 5995WX A2, Samsung, Singapore office | A2 candidate | S$11,362 | S$13,414 | **S$15,467** |
| Own 5995WX A1, Samsung, Singapore office | A1 candidate | S$11,652 | S$13,713 | **S$15,774** |

UHost is a configurator lead with unknown stock and network terms. BizoSiz has matching repository cart evidence but unresolved final supply, taxes and service details. PlusClouds is listed and its configure link opens a general portal, so the quote/term and supply remain less certain. These figures justify investigating the offers; they do not establish a completed supplier selection.

The expanded reference assumes **350 W average wall power**: S$79.61/month server electricity, **S$19.90/month separate cooling**, **S$50/month internet**, a 3% annual hardware reserve, and S$700 upfront UPS/assembly/delivery allowances. Power is unmeasured; labour and resale are zero in this optional case. S$100/month additional ownership work, if separately chosen, adds S$3,600 over three years. Office rent is never added.

Alternative-drive sensitivities reduce three-year Singapore office budgets to **S$14,878 for A2 with ADATA**, **S$14,618 for A1 with Lexar**, or **S$15,707 for 256 GB plus two 4 TB Lexars**. Performance and procurement conditions remain.

The optional expanded model also contains:

- Singapore 5U colocation: A2 about **S$36,791/36 months**, plus unquoted facility extras; a shared 100 Mbps service differs from the European 1 Gbps offers.
- Malaysia office electricity sensitivity: same Singapore-procured A2 hardware about **S$13,871/36 months** before unquoted logistics and tax differences.
- Malaysia 4U/tower colocation: about **S$16,148–16,378 known-cost floors**, not approved full quotes.
- Regular Hetzner A1/A2 and a separate illustrative Singapore-billing tax case.
- Historical AX162-LTD sensitivity: **unavailable in the public feeds at the time of the study**, not a purchasable alternative.

A Malaysia-local pair of Intel desktops was separately priced at **RM24,008 ≈ S$7,529**. Its [direct four-scenario budgets](06-direct-payback.md#malaysia-local-intel-pair) separate S$56.75/month modeled server electricity and S$50/month optional internet; the earlier **S$13,760 three-year expanded Malaysian budget** additionally includes the stated cooling/UPS/assembly/reserve allowances. It is an independent-job topology with 64 GB per host, not a locally verified Malaysian 5995WX quote or a shared A1/A2 memory pool.

## Performance and procurement gates

For a 5% tolerance, require representative critical-job latency at most **1.05× baseline** and busy-queue throughput at least **0.95× baseline**. For 3%, use **1.03×** and **0.97×**. Predeclare jobs, toolchains, cache states and concurrency; keep results unresolved if variability spans the limit.

For the 5995WX, obtain BIOS **1003 or a later supported version**, the exact qualified **CT32G4DFD832A.C16FE** RAM revision or a validated substitute, correct motherboard power cabling, measured sustained cooling, and confirmed SSD quantities. Test the largest job within per-host usable RAM.

If Singapore placement is essential, compare the owned candidate with the regional leads in file 02. If geography is flexible, start with the [original 104 worldwide rentals](05-repository-rental-comparison.md), then see [the next 15](08-latest-rental-comparisons.md), [the next 22](09-expanded-rental-comparisons.md) and [the correction to an existing offer](10-current-offer-updates.md). Evaluate the actual registry, cache and artifact network path, since distance alone does not determine end-to-end CI time.

## Research and review record

The original hardware and regional investigation and the repository integration used **GPT-6.2 Astra at max reasoning**. **GPT-6.2 Sol at max** independently reviewed the hardware evidence, compatibility, cost arithmetic and final repository changes. No account registration, supplier contact, paid order, hardware reservation or actual repository CI replay was performed.
