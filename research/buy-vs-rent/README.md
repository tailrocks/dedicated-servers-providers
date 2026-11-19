# CI server ownership versus dedicated rental

**Updated: 20 November 2026 (Asia/Ho_Chi_Minh).**

**Buy/host priority:** Singapore first, Malaysia second.

**Rental coverage:** all 104 offers already in this repository, with existing worldwide locations and evidence retained.

**Workload:** Linux Rust/TypeScript builds and tests in Docker containers.

**Owned hardware:** non-ECC desktop/workstation memory; performance first, price second.

## Decision

**If a European placement is acceptable, investigate the repository's cheaper capacity-matched rentals before buying.** Their known charges can be below three-year office ownership, even though regular Hetzner new-order pricing makes buying look attractive. Stock, final invoice, network, operator and payment conditions still need acceptance.

**If Singapore placement or local physical control is required, a 5995WX with 256 GB non-ECC RAM is the strongest single-host ownership candidate found for testing.** Prefer an existing suitable office over assuming that cheap 1U colocation will accept a large workstation. Malaysia colocation has lower published leads but unresolved power, chassis, contract and local-service costs.

**No proposed owned configuration is proven to be within 3–5% of the user's actual CI.** A public +3% multicore Clang observation is a screening result from a different 5995WX system. The [acceptance procedure](04-validation-and-procurement.md) requires both critical-job latency and busy-queue throughput by default before declaring CI equivalence.

## Files

| File | Purpose |
|---|---|
| [01-hardware-and-performance.md](01-hardware-and-performance.md) | Exact Singapore BOMs, compiler evidence, RAM qualification, storage alternatives, cooling and PSU requirements |
| [02-rental-market.md](02-rental-market.md) | Singapore/Malaysia rental and colocation leads; Malaysian local BOM; electricity and currency sources |
| [03-rent-vs-buy-tco.md](03-rent-vs-buy-tco.md) | 12/24/36-month ownership budgets, worldwide rental comparisons, power/tax/labour assumptions and sensitivities |
| [04-validation-and-procurement.md](04-validation-and-procurement.md) | Actual CI replay, strict acceptance gates and complete quote requirements |
| [05-repository-rental-comparison.md](05-repository-rental-comparison.md) | Coverage of all 104 existing rental rows, A1/A2 capacity matching, native terms and horizon costs |
| [Integration and corrections log](../2026-11-20-buy-vs-rent.md) | Changes from the earlier standalone hardware research and exact source snapshot |

The [root seven-column table](../../README.md#servers) remains the canonical provider list. This folder adds a workload-specific ownership decision; it does not silently change the original rental table's raw-capacity floor or label every listed CPU as a measured CI match.

## Reference capacity classes

| Profile | CPU | Minimum installed RAM | Drive layout | Nominal mirrored capacity |
|---|---|---:|---|---:|
| **A1: AX162-1** | EPYC 9454P, 48 cores / 96 threads | 128 GB | 2 × 3.84 TB NVMe | 3.84 TB |
| **A2: AX162-2** | Same | 256 GB | 2 × 1.92 TB NVMe | 1.92 TB |

Mirroring is the comparison convention, not a claim that the user's current rental is already configured as RAID1. Filesystem overhead and operating headroom reduce available space. CPU, SSD latency/endurance, memory protection, network and support are separate acceptance questions.

The repository's general minimum is only 128 GB plus 2 TB **raw** SSD. Of its 104 current offers, **66 distinct rows meet at least one of these stricter capacity classes**: 32 only A1, 32 only A2, two both; 38 meet neither. No main-table row establishes allocation in Singapore or Malaysia. The comprehensive appendix preserves these distinctions instead of comparing a one-drive or undersized host with a mirrored owned system.

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

## Financial comparison that changes the recommendation

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

The office reference assumes **350 W average wall power**, 25% cooling overhead, S$50/month incremental connectivity, a 3% annual hardware reserve, and S$700 upfront UPS/assembly/delivery allowances. Power is unmeasured; labour and resale are zero in the base case. S$100/month additional ownership work adds S$3,600 over three years.

Alternative-drive sensitivities reduce three-year Singapore office budgets to **S$14,878 for A2 with ADATA**, **S$14,618 for A1 with Lexar**, or **S$15,707 for 256 GB plus two 4 TB Lexars**. Performance and procurement conditions remain.

The main model also contains:

- Singapore 5U colocation: A2 about **S$36,791/36 months**, plus unquoted facility extras; a shared 100 Mbps service differs from the European 1 Gbps offers.
- Malaysia office electricity sensitivity: same Singapore-procured A2 hardware about **S$13,871/36 months** before unquoted logistics and tax differences.
- Malaysia 4U/tower colocation: about **S$16,148–16,378 known-cost floors**, not approved full quotes.
- Regular Hetzner A1/A2 and a separate illustrative Singapore-billing tax case.
- Historical AX162-LTD sensitivity: **unavailable in the current public feeds**, not a purchasable alternative.

A Malaysia-local pair of Intel desktops was separately priced at **RM24,008 ≈ S$7,529**, with an illustrative **S$13,760 three-year Malaysian office budget** using local electricity and the same stated allowances. It is an independent-job topology with 64 GB per host, not a locally verified Malaysian 5995WX quote or a shared A1/A2 memory pool.

## Performance and procurement gates

For a 5% tolerance, require representative critical-job latency at most **1.05× baseline** and busy-queue throughput at least **0.95× baseline**. For 3%, use **1.03×** and **0.97×**. Predeclare jobs, toolchains, cache states and concurrency; keep results unresolved if variability spans the limit.

For the 5995WX, obtain BIOS **1003 or a later supported version**, the exact qualified **CT32G4DFD832A.C16FE** RAM revision or a validated substitute, correct motherboard power cabling, measured sustained cooling, and confirmed SSD quantities. Test the largest job within per-host usable RAM.

If Singapore placement is essential, compare the owned candidate with the regional leads in file 02. If geography is flexible, start with the complete worldwide comparison in file 05. Evaluate the actual registry, cache and artifact network path, since distance alone does not determine end-to-end CI time.

## Research and review record

The original hardware and regional investigation and the repository integration used **GPT-6.2 Astra at max reasoning**. **GPT-6.2 Sol at max** independently reviewed the hardware evidence, compatibility, cost arithmetic and final repository changes. No account registration, supplier contact, paid order, hardware reservation or actual repository CI replay was performed.
