# Final buying and renting recommendations

[Study index](README.md) · [Complete build variants](recommended-builds.md) · [Financial results](financial-results.md) · [Evidence and limits](sources-and-methodology.md)

## Primary decision

**Choose a competitively priced exact EPYC 9454P rental for the best ownership-versus-rental economics today. If you specifically want to own one non-ECC machine close to AX162 throughput, buy the 5995WX / WRX80 configuration below in Singapore.** These conclusions answer different decisions: the best qualifying computer to purchase need not beat the cheapest suitable rental over a practical horizon.

UHost's listed 256 GB machine costs USD 220/month plus USD 120 setup, or **S$283.73/month and S$154.76 setup** at the dated fixing, before any unquoted buyer charges. PlusClouds' 256 GB AX162-R lists **EUR229/month plus EUR542 setup** and explicitly advertises 1 Gbps unlimited network. Both need suitable final commercial terms and allocation; neither is represented as reserved stock. For a clearer currently selected monthly cart, ServerWala's equivalent 256 GB Helsinki layout is USD335/month, zero setup, a shared 1 Gbps port and 20 TB. [Rental comparison and qualifications](rental-market-update.md)

The strict new-memory workstation costs S$13,330. Against UHost it recovers capital in **47 / 60 / 74 / 114 months** for hardware / electricity / internet / both respectively. Against regular Hetzner AX162-2 on the documented SG non-GST-registered-buyer tariff it takes **10 / 11 / 11 / 12 months**. The new business line is an independent S$105/month assumption; do not add it if a suitable existing line already covers the site. [All four scenarios](rent-vs-buy.md)

## 1 — Best qualifying single-host purchase: 5995WX, 256 GB

This is both the primary overall single-host choice under the stated replacement constraint and the closest documented EPYC-equivalent purchase candidate. The ranking does not assert that it is the cheapest way to buy any amount of CI compute.

| Required component | Exact choice and purchase source | Qty | SGD subtotal |
|---|---|---:|---:|
| CPU | [AMD Threadripper PRO 5995WX — Founder Extreme custom order](https://founderextreme.com/product/amd-ryzen-threadripper-pro-series-custom-order/) | 1 | 2990.00 |
| Motherboard | [ASUS Pro WS WRX80E-SAGE SE WIFI, original model — ElectronicsCrazy](https://www.electronicscrazy.sg/asus-pro-ws-wrx80e-sage-se-wifi-amd-threadripper-pro-eatx-workstation-motherboard-black/) | 1 | 1789.00 |
| RAM | [Kingston KVR32N22D8/32, 32 GB DDR4-3200 non-ECC UDIMM — Bizgram / Sim Lim](https://simlimsquare.com.sg/product/kingston-3200mhz-32gb-dimm-kvr32n22d832-20662) | 8 | 6864.00 |
| NVMe | [Lexar NM790 2 TB LNM790X002T-RNNNG — TheShop](https://theshop.sg/products/pc-parts/m2-nvme-ssd/lexar-nm790-m-2-2280-pcie-gen-4x4-nvme-ssd-2tb) | 2 | 1008.00 |
| Cooler | [ARCTIC Freezer 4U-M Rev.2 ACFRE00133B — Bizgram / Sim Lim](https://www.simlimsquare.com.sg/public/product/arctic-freezer-4u-m-sp6-sp3-str5-tr4-swrx8-strx4-lga4677-lg-21515) | 1 | 119.00 |
| Case and fans | [Fractal Define 7 XL Solid FD-C-DEF7X-01, three 140 mm fans included — The Techyard](https://thetechyard.com/products/fractal-design-define-7-xl-black-solid-panel) | 1 | 309.00 |
| PSU | [Seasonic FOCUS GX-850 V4, exact black 850 W variant — ViiPC](https://www.viipc.sg/products/focus-gx-750-v4atx-3-80-plus-gold?variant=45415426719893) | 1 | 251.00 |
| GPU, wired NIC, NVMe adapters, OS | Onboard BMC graphics and wired NIC; motherboard M.2 slots; included mounting/PSU cables and paste; Linux | Included | 0.00 |
| **Component subtotal** | Local collection / eligible delivery and fee-free-payment basis | | **13330.00** |

The board's eight channels accept the exact non-ECC module according to Kingston's system configurator. CPU support needs the documented BIOS revision or newer, not an arbitrary out-of-box firmware assumption. The SSI-EEB case, 145 mm cooler, ordinary-height DIMMs, EPS/supplemental power connections and two CPU-connected Gen4 M.2 slots are addressed in the [compatibility ledger](recommended-builds.md). The GPU is unnecessary because the motherboard supplies a management/display controller; the separate management interface should not be exposed as a public CI service.

**Expected performance:** approximately baseline scale for parallel compilation, with public same-version Clang pairings at 98.6–106.2%. A 64-core/128-thread CPU and all eight channels make it a plausible consolidated many-job host. Zen 3's slower critical path means current desktop CPUs can complete individual stages sooner. No evidence establishes 3–5% equivalence for the user's complete pipeline. [Raw observations and corroborating longer builds](published-benchmarks.md)

**Expected power:** 110 / 275 / 440 W idle / moderate / heavy, analytically budgeted from original external wall measurements. In Singapore, these imply approximately **S$25.02 / S$62.55 / S$100.09 per month** at the current tariff. [Electricity evidence](electricity-costs.md)

**Availability:** the CPU is custom order, the cooler's direct listing is intermittent, and a complete unit has not been allocated. The new RAM listing states 100 modules; that is seller inventory metadata, not a reservation. The motherboard has conflicting warranty wording. These are commercial qualifications on an exact documented build, not reasons to defer the recommendation until physical testing. [Country evidence and warranty](singapore-hardware.md)

## 2 — Closest 128 GB capacity alternative to AX162-1

Use the same CPU, board, cooler, case and PSU, replacing memory with **8 × Kingston KVR32N22D8/16** at S$355.75 each and storage with **2 × NM790 4 TB** at S$859 each. The resulting subtotal is **S$10,022**, including **S$2,846 memory and S$1,718 storage**. This is an indicative RAM quote, not a confirmed eight-stick shipment. All eight channels remain populated; using four 32 GB sticks would change the memory-bandwidth proposition. [Memory evidence](ram-comparison.md) · [Full 128 GB bill](singapore-hardware.md)

A Linux RAID1 mirror gives 4 TB nominal usable, exceeding the AX162-1's 3.84 TB mirror. The two independent-drive alternative can separate caches and workload I/O but is not redundant; select it only when reconstruction is acceptable. RAID0 is unsuitable for the only persistent working copy. NM790 provides good capacity/value and a generous rated write budget but lacks capacitor-backed power-loss protection. Named enterprise SSDs such as Micron 7450 offer that feature; the exact AX162 SSD models and their PLP implementation are unestablished. [Storage performance and layouts](nvme-comparison.md)

At moderate power this configuration crosses the regular SG-taxed Hetzner AX162-1 cost at **11 / 11 / 12 / 13 months** across the four scenarios. Against PlusClouds' 128 GB / 2 × 3.84 TB listing it is **30 / 37 / 43 / 61 months**. The provider choice again changes the recommendation more than a small storage-speed premium.

For 256 GB and the larger mirror together, keep the primary eight 32 GB modules and choose the 4 TB drives: **S$14,040**. That capacity meets both profiles in one host.

## 3 — Best practical higher-throughput purchase path: two Ryzen 9950X3D runners

Buy **two identical Singapore nodes**, each with:

- Ryzen 9 **9950X3D** CPU, S$959.
- **MSI B850M GAMING PLUS WIFI**, S$279.
- **KLEVV CRAS V RGB KD5CGUB80-60A320G**, 128 GB as 2 × 64 GB, S$2,579 description-based listing; exact-SKU alternative S$2,889.
- **2 × Lexar NM790 2 TB**, S$1,008 for the pair.
- **Thermalright Aqua Elite 360 V3** with radiator fans, S$88.
- **Cooler Master Elite 502 ARGB** with three case fans, S$85.
- **Thermalright TR-KG650 black, 650 W Gold**, S$116, EAN 814256019729.

Total **S$5,114 per node / S$10,228 for two**. Selecting the exact-SKU RAM offer instead adds **S$310 per node**, yielding S$5,424 / S$10,848. The lower RAM listing's store description identifies capacity/speed/timing but omits the printed part number and uses unlimited inventory tracking. It is not described as confirmed physical stock. [Every purchase link and warranty](singapore-hardware.md) · [Exact JSON BOM](data/procurement.json)

Each node has 16 cores / 32 threads, its own 128 GB address space and its own disks. Keep job-local caches local and schedule repositories between hosts. A 256 GB job cannot use this pair as one machine. Two nodes offer fast serial work and useful queue parallelism while one can stay available during the other's maintenance.

**The faster-than-EPYC case is analytical:** at 80–90% effective queue scaling, two observed X3D Clang rates imply **125–144%** of the reference proxy. At 70%, the range is roughly 109–112%. These efficiency assumptions are neither measurements nor promises. There is no supported 10–50% gain for one ordinary unsharded pipeline. [Concurrency limits and RAM budgets](ci-cd-performance-analysis.md)

Budget **420 W** for moderate combined draw, or **S$95.54/month** in Singapore. Against two DediJet Singapore 9950X nodes at USD538/month, capital recovery is **15 / 18 / 18 / 21 months**. Against one low-cost UHost EPYC, it takes **36 / 54 / 57 / 122 months**, while still offering different memory topology and uncertain relative queue throughput. This is the better ownership upgrade when independently schedulable jobs and local placement have value.

## Mainstream and Malaysian alternatives

The **S$4,757 Core Ultra 7 270K Plus** node is the lowest initial-price 128 GB desktop in the checked SG baskets. It changes the AMD board to ASUS TUF B860M-PLUS WIFI and costs only slightly less per unit of the controlled Chromium workload than the plain 9950X. The X3D is a better balance than plain 9950X at the verified S$93 whole-system premium. Neither 16-core AMD nor the 24-core Intel desktop is certified as a complete parallel replacement for the 48-core EPYC. [CPU value table](cpu-alternatives.md)

The **9950X3D2** is the fastest mainstream candidate in the retrieved longer compiler tests. Its SG whole-node price is **S$5,644**, about 10.4% above X3D for roughly 7–8% more work rate in the two cited compiler comparisons. In Malaysia its **RM21,663** price is only about 3.9% above the **RM20,853 X3D** build, making X3D2 the stronger local performance/value variant in those tests. Singapore still has the cheaper checked procurement route. [Malaysia exact bill and current BIOS](malaysia-hardware.md)

For a Malaysian buyer requiring **256 GB of non-ECC DDR5 in one host**, the 270K Plus / ASUS B860M / **4 × Kingston KVR56U46BD8-64** is a supported-capacity alternative at **RM32,211**. Plan for the controller's documented **4400 MT/s** four-dual-rank-DIMM rate, not the kit sticker or the CPU's fastest memory headline. The entire 256 GB is usable by one job, but it remains a lower aggregate compute class than the 5995WX/EPYC candidates. Malaysia did not yield a current, complete, locally stocked WRX80 quote. [RAM qualification and limits](ram-comparison.md)

## What this settles

The best documented **single non-ECC computer** near the AX162's aggregate scale remains a 5995WX workstation with fully populated memory channels. Its current new-memory price weakens the case for ownership against inexpensive European EPYC rentals. The best affordable desktop for build responsiveness is the 9950X3D in Singapore, or the X3D2 within the checked Malaysian chassis prices. Two such nodes are an independently scheduled upgrade path, not a substitute for one large memory space.

This is a completed online recommendation. No purchase, supplier contact, physical access or hardware benchmark was required or performed. Commercial quote uncertainties and the limits of published workload evidence remain visible alongside the exact buying choices.

Signed-off-by: Alexey Zhokhov
