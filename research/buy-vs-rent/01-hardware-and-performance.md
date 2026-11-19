# CI server hardware and performance research

Original research: **19 November 2026**; targeted hardware and storage refresh: **20 November 2026**. Prices: **Singapore dollars (SGD)** unless stated otherwise. Workload: native Linux CI runners building and testing Rust and TypeScript projects in Docker containers. Priority: performance first, then value; ordinary non-ECC RAM for owned desktop/workstation hardware. Entries not explicitly refreshed retain the original observation date.

This file extends the repository's rental research with CI-specific ownership candidates. Regional hosting and ownership economics are in [02-rental-market.md](02-rental-market.md) and [03-rent-vs-buy-tco.md](03-rent-vs-buy-tco.md). The [initial 104-offer comparison](05-repository-rental-comparison.md), [15-offer follow-up](08-latest-rental-comparisons.md) and [22-offer expansion](09-expanded-rental-comparisons.md) together cover all 141 current rental rows, with [current corrections](10-current-offer-updates.md) applied to earlier offers. The workload acceptance procedure is in [04-validation-and-procurement.md](04-validation-and-procurement.md).

## 1. Decision

**Closest single-host non-ECC candidate: Threadripper PRO 5995WX, 256 GB DDR4-3200 across eight channels, and two NVMe drives.** This is workstation hardware in a tower. It is not a mainstream AM5/LGA1851 consumer platform. The selected ASUS WRX80 board explicitly supports non-ECC unbuffered DIMMs. Public compiler evidence makes this a credible AX162 substitute, but does not guarantee the user's actual CI workload will be within 3–5%.

**Mainstream desktop alternative: two Core Ultra 7 270K Plus runners.** Use this when the queue contains independent jobs, each fitting within one host. A pair of Ryzen 9 9950X3D runners is the AMD alternative. Two hosts do not provide a shared memory pool and cannot jointly execute one ordinary unsharded Cargo build.

**Modern faster single-host alternative: Threadripper 9970X.** It is a credible faster compilation candidate, but the proposed TRX50 configuration requires ECC RDIMMs and therefore fails the strict non-ECC requirement. It is listed only as an optional change of requirements.

| Configuration | RAM | Storage | Advertised parts subtotal | Interpretation |
|---|---|---|---:|---|
| 5995WX / WRX80 | 256 GB, 8 × 32 GB non-ECC DDR4 | 2 × 2 TB NVMe | S$8,609.40 | Single-host screening candidate; actual CI unmeasured |
| 5995WX / WRX80 | 128 GB, 8 × 16 GB non-ECC DDR4 | 2 × 4 TB NVMe | S$8,891.00 | Exact eight-DIMM qualification still needed |
| 5995WX / WRX80 | 256 GB, 8 × 32 GB non-ECC DDR4 | 2 × 4 TB NVMe | S$9,889.40 | More RAM and slightly more raw capacity than AX162-1 |
| Two Intel 270K Plus hosts | 64 GB each, 128 GB aggregate | 2 × 2 TB per host | S$7,479.20 | Aggregate-throughput candidate; not a measured AX162 equivalent |
| Two Intel 270K Plus hosts | 128 GB each, 256 GB aggregate | 2 × 2 TB per host | S$10,439.20 | More expensive than single 256 GB WRX80 build |
| Two Ryzen 9950X3D hosts | 64 GB each, 128 GB aggregate | 2 × 2 TB per host | S$8,241.20 | AMD alternative; validate project-specific benefit |
| Two Ryzen 9950X3D hosts | 128 GB each, 256 GB aggregate | 2 × 2 TB per host | S$11,201.20 | Memory remains separated by host |
| 9970X / TRX50 | 128 GB ECC RDIMM | 2 × 4 TB NVMe | About S$13,400 | Optional ECC exception |
| 9970X / TRX50 | 256 GB ECC RDIMM | 2 × 2 TB NVMe | About S$13,300 | Optional ECC exception |

These are sums of observed listings, not binding assembled quotes. Assembly, delivery, UPS, network changes and any tax not already included by the seller are additional. Stock, quantities, exact revisions, warranty and GST must be resolved in a final quote. No parts were purchased and no seller was contacted.

## 2. Reference: Hetzner AX162

| Property | Reference |
|---|---|
| Processor | AMD EPYC 9454P, Zen 4, 48 cores / 96 threads |
| Clock | 2.75 GHz base, up to 3.8 GHz boost; boost is not a sustained all-core guarantee |
| Cache / nominal TDP | 256 MB L3 / 290 W |
| CPU memory capability | 12 DDR5-4800 channels, registered memory |
| AX162-1 | 128 GB ECC registered DDR5; 2 × 3.84 TB DC NVMe |
| AX162-2 | 256 GB ECC registered DDR5; 2 × 1.92 TB DC NVMe |
| Advertised dedicated locations | Falkenstein, Germany; Helsinki, Finland |

Sources: [AMD EPYC 9454P][H01], [Hetzner configuration table][H02], [AX162 product page][H03].

Do not assume that all twelve channels are populated in the 128 GB or 256 GB rental. DIMM population is not established by the advertised capacity. The maximum theoretical bandwidth of the processor is not a measurement of the rented configuration.

Two capacity measures matter. AX162-1 has 7.68 TB raw; AX162-2 has 3.84 TB raw. If mirrored, usable device capacity is approximately 3.84 TB or 1.92 TB respectively, before filesystem overhead. Consumer 2 × 4 TB and 2 × 2 TB pairs provide slightly more capacity. The presence of two drives alone does not establish that the user's rental is configured as RAID1.

## 3. Performance evidence and its limits

### 3.1 Common compiler subtest against an actual AX162

The following are public **Geekbench 6.4 Linux AVX2 Clang** results, not overall Geekbench scores. Higher work rate is better. The AX162 and 9950X submissions used Ubuntu 24.04.2 on the same date; the other submissions differ in platform and OS details. These are not a controlled laboratory comparison.

| System | Single-core, thousand lines/s | Multicore, thousand lines/s | Multicore work-rate difference versus AX162 |
|---|---:|---:|---:|
| [Hetzner AX162-R, EPYC 9454P][H04] | 10.8 | 327.4 | Baseline |
| [Ryzen 9 9950X][H05] | 17.2 | 250.4 | −23.5% |
| [Threadripper PRO 5995WX][H06] | 10.6 | 337.1 | +3.0% |
| [Threadripper 9970X][H07] | 17.1 | 410.6 | +25.4% |

The [Geekbench methodology][H08] describes a Clang/Lua source compilation workload with a fixed 96-file multicore task. It is short and does not reproduce a sustained Rust/TypeScript/Docker queue. Do not convert these results into a guarantee for actual CI, and do not interpret a 25% higher work rate as a 25% shorter elapsed time.

The 5995WX is the nearest multicore result in this small screening sample. Its submission uses an **ASRock WRX80 Creator with 125.53 GB reported memory and Ubuntu 24.10**, whereas the AX162 reports **251.38 GB and Ubuntu 24.04.2**. The proposed owned build uses an ASUS board and 256 GB. ECC mode, DIMM layout and sustained stock operation are not established. In particular, the 5995WX submission reports a 4.57 GHz frequency field; that metadata is not proof of either stock settings or a sustained all-core clock. These differences and the single submitted observation prevent a 3–5% CI equivalence claim. A single 9950X is much faster in the single-core subtest but behind in this multicore task. The 9970X is a candidate for the requested 10–50% higher work rate on this proxy only.

As secondary corroboration, [PassMark's aggregate comparison][H09] showed 94,689 for EPYC 9454P and 94,796 for 5995WX, approximately +0.1%. This is a mixed synthetic aggregate, not a CI benchmark. A separate 5995WX submission with implausible reported clock metadata was excluded from the main evidence.

### 3.2 Real compilation tests

- [GamersNexus][H10] measured a Windows Chromium build at about 103 minutes on the Intel 270K Plus versus 101 minutes on the Ryzen 9950X. This is explicitly a Windows test, not a Linux Rust measurement.
- [Phoronix's Linux 270K Plus review][H11] generally placed the Intel close behind 9950X/9950X3D across builds. Test memory settings differ from the priced high-capacity configurations.
- [OpenBenchmarking's Wasmer 7.0.1 build][H12], a Rust project, reported heterogeneous public averages of about 82 seconds for 270K Plus (10 results), 85 for 9950X (4), 78 for 9950X3D (6), 78 for 9980X (6), and 76 for 9950X3D2 (13). There was no matching 9454P or 5995WX row. These numbers show that one build does not scale directly with core count; they do not establish cross-host causal speed differences.
- [Phoronix's Threadripper review][H13] measured a controlled Linux-kernel compile at 34 seconds on 7970X, 28 on 9970X, 27 on 7980X, and 21 on 9980X. It did not include the AX162.
- [Phoronix's 9950X3D2 compilation composite][H14] was about 7% faster than 9950X3D across nine codebases. Extra cache can help compilation; it should not be dismissed solely as a gaming feature. Whether the price premium is worthwhile depends on the user's actual projects.

### 3.3 What performance means for this purchase

Measure both individual-job latency and aggregate completed jobs per hour. Dependency graphs, linking, test sharding, filesystem activity, cache reuse and memory pressure can all change the CPU ranking. Do not sum two single-host benchmark scores and present the sum as measured two-node CI throughput. A 24-core hybrid Intel CPU is also not 24 homogeneous EPYC-class cores: [Intel specifies][H15] 8 performance cores, 16 efficiency cores and 24 threads.

## 4. Owned build A: 5995WX / WRX80 / 256 GB non-ECC

| Component | Exact proposed item | Price | Procurement observation |
|---|---|---:|---|
| CPU | AMD Threadripper PRO 5995WX | S$2,990 | [Founder Extreme custom order][H16]; price is in model-specific description, not generic S$1,800 page header |
| Motherboard | ASUS Pro WS WRX80E-SAGE SE WIFI | S$1,789 | [ElectronicsCrazy / MemoryWorld][H17]; marked in stock, one-year warranty shown |
| RAM | 8 × Crucial 32 GB DDR4-3200 non-ECC UDIMM | S$1,680 | [TechDeals][H18], S$210/module incl tax; confirm eight matching revisions and stock |
| NVMe | 2 × Samsung 9100 PRO 2 TB | S$1,498 | [Dynacore][H19], S$749/drive, marked in stock |
| Cooler | ARCTIC Freezer 4U-M | S$115 | [TechDeals][H20]; sWRX8 support |
| Case | Fractal Meshify 2 XL | S$302.40 | [TechDeals][H21]; SSI-EEB support |
| PSU | Seasonic Focus GX-850 | S$235 | [Volta PC][H22], incl GST |
| Console graphics | Board BMC display | S$0 | [ASUS documentation][H23] |
| **Total** | | **S$8,609.40** | Parts subtotal |

The [5995WX specification][H24] has 64 Zen 3 cores, 128 threads, eight DDR4-3200 channels and 280 W TDP. The [selected ASUS board][H25] explicitly supports non-ECC UDIMMs. Thus the non-ECC preference can be met without falling back to a dual-channel consumer platform.

**Exact memory validation:** [ASUS QVL][H26] lists **CT32G4DFD832A.C16FE**, 32 GB, at 3200 MT/s with all eight sockets populated. The retailer lists only the base SKU and requests a stock check. Require eight matching qualified revisions or an explicitly validated substitute. [ASUS CPU support][H55] lists **BIOS 1003** for the 5995WX on the original board; check the installed BIOS before assembly.

**Mechanical and thermal validation:** use a case supporting the board's 12.2 × 13-inch EEB dimensions. Cooler mounting, RAM clearance, fan airflow and sustained temperatures must be checked. No dedicated GPU is needed for ordinary headless CI because this board provides BMC console graphics. Its remote-management capability is useful when the host is physically elsewhere. Follow the [ASUS power-connector instructions][H56], including the separate PCIe 8-pin motherboard connection for heavy load; confirm the exact PSU's cable inventory. EPS CPU and PCIe power plugs are not interchangeable merely because both have eight pins.

**NVMe lanes:** the two CPU-connected M.2 sockets are PCIe 4.0 ×4. The 9100 PRO runs at Gen4 here. Its selection is based on the observed 2 TB price, not a claim that the platform can use Gen5 speed. Avoid assuming native U.2 ports have the same generation as those M.2 sockets.

**Capacity alternatives:** [Crucial 16 GB modules][H27] at S$85.20 each bring RAM to S$681.60 for 128 GB. Combined with [two Samsung 990 PRO 4 TB heatsink drives][H28] at S$1,389 each, the total is S$8,891.00. Exact eight-DIMM qualification of the quoted 16 GB module was not established. Keeping 256 GB and using those two 4 TB drives costs S$9,889.40. The 256 GB memory layout has stronger exact-part compatibility evidence.

**Procurement risk:** this is an older platform with custom-order CPU sourcing. Founder explicitly reconfirms price and availability before deposit. Obtain the CPU, board revision, BIOS, DIMM revision, final GST-inclusive cost, and system warranty in writing. The research did not place an order.

## 5. Owned builds B and C: two mainstream desktop runners

### Per-host parts

| Component | Intel host | AMD host |
|---|---|---|
| CPU | [Core Ultra 7 270K Plus][H29], S$488 | [Ryzen 9 9950X3D tray][H30], S$959; retailer advertises four-year local warranty |
| Motherboard | [MSI B860M Gaming Plus WiFi][H31], S$369 | [MSI B850M Gaming Plus WiFi][H32], S$279 |
| 64 GB RAM option | [Lexar THOR 2 × 32 GB DDR5-6000][H33], S$1,099 | Same |
| 128 GB RAM option | [KLEVV CRAS V 2 × 64 GB DDR5-6000][H34], S$2,579 | Same |
| Storage | Two 9100 PRO 2 TB, S$1,498 | Same |
| Cooling | [Thermalright Aqua Elite V3 360][H35], S$84.60 | Same |
| Case | [Cooler Master Elite 502 with three fans][H36], S$85 | Same |
| PSU | [Thermalright TR-KG650 Gold][H37], S$116 | Same |

| Platform | RAM per host | One host | Pair |
|---|---:|---:|---:|
| Intel 270K Plus | 64 GB | S$3,739.60 | S$7,479.20 |
| Intel 270K Plus | 128 GB | S$5,219.60 | S$10,439.20 |
| AMD 9950X3D | 64 GB | S$4,120.60 | S$8,241.20 |
| AMD 9950X3D | 128 GB | S$5,600.60 | S$11,201.20 |

Two drives are included **per host**, four across the pair. With RAID1, each host has approximately 2 TB usable; the pair has 4 TB across separate filesystems. Dropping one drive per host saves S$1,498 and removes both local mirrors. That can be reasonable for disposable runners when source and important artifacts are stored elsewhere.

**Memory compatibility:** the [KLEVV November 2026 compatibility list][H38] includes **KD5CGUB80-60A320G** on both selected MSI boards. The exact Lexar 64 GB kit qualification was not established. Require builder validation or a qualified substitute. The kit's advertised speed is not a guarantee for every CPU, BIOS or memory setting.

**Cooling compatibility:** [Thermalright][H39] lists both LGA1851 and AM5 for this cooler. Verify the mounting kit in the shipped box, radiator clearance and sustained load temperatures. Run stock-supported CPU power settings rather than relying on aggressive motherboard defaults.

**Storage sockets:** [MSI's Intel specification][H40] gives one CPU Gen5 ×4 socket, one chipset Gen4 ×4 socket and another Gen4 ×2 socket. Use the first two for the main drives; Linux software RAID1 is an option. Do not assume both drives run at Gen5 simultaneously.

Choose the Intel pair as the first value candidate; it is about S$762 cheaper than the AMD pair at identical RAM/storage. Choose AMD if the actual CI replay justifies it. At 256 GB aggregate, the Intel pair is S$1,829.80 more than the single 256 GB WRX80 host, while still having two separate memory pools.

## 6. Optional modern workstation: 9970X / TRX50

This build explicitly changes the non-ECC requirement. [AMD's 9970X specification][H41] uses DDR5 RDIMMs, and the [ASUS TRX50 board][H42] specifies ECC registered memory. Ordinary desktop UDIMMs are not substitutes.

| Component | Listed price |
|---|---:|
| [Threadripper 9970X, 32 cores / 64 threads][H43] | S$4,075 |
| [ASUS Pro WS TRX50-SAGE WIFI][H44] | S$1,489 |
| [4 × 32 GB Kingston DDR5-5600 ECC RDIMM][H45] | S$4,350 |
| Or [4 × 64 GB Kingston DDR5-5600 ECC RDIMM][H46] | S$5,514 |
| Same cooler/case/PSU as WRX80 | S$652.40 |
| Basic UEFI-GOP-compatible console graphics allowance | About S$80 |
| 2 × 4 TB or 2 × 2 TB NVMe | S$2,778 or S$1,498 |

The full budgets are approximately S$13,400 for 128 GB + two 4 TB drives, or S$13,300 for 256 GB + two 2 TB drives. [Kingston][H47] lists both exact RDIMM models for the board. These are **5600 MT/s** parts; benchmark configurations using faster RAM are not identical. Confirm BIOS, console-card firmware, stock and continuous cooling performance at deployment ambient temperature. The Freezer 4U-M's stated 350 W rating is not itself a measured thermal validation of this assembled system.

For quote comparison, the older 64-core 7980X appears at S$5,260 custom order, S$1,185 above the 9970X CPU; the 64-core 9980X is listed at S$8,151 by theShop, S$4,076 more. These may be useful for heavily parallel queues, but core counts alone do not establish the benefit. The 9950X3D2 local offer at S$1,489 also merits a project-specific check before paying its S$530-per-node premium over the quoted 9950X3D. [Founder][H16], [theShop 9980X][H54], [9950X3D2 retailer][H48].

## 7. RAM topology and capacity

For mainstream desktops, prefer **2 × 32 GB for 64 GB** and **2 × 64 GB for 128 GB**. A 256 GB layout normally requires 4 × 64 GB and exact CPU/board/BIOS qualification. Four DIMMs on a dual-channel processor are still two channels.

[AMD's 9950X specification][H49] lists DDR5-5600 with two DIMMs and DDR5-3600 with four DIMMs. Validated overclocked kits may run faster; the guaranteed rating is not a universal ceiling. However, buying a DDR5-6000 kit does not guarantee that four populated slots will run at 6000. Do not combine two arbitrary kits and assume their advertised profile is valid together.

Size RAM from concurrent job peak resident memory, service containers, filesystem cache and host headroom. Avoiding swaps and OOMs usually matters more than a small timing improvement. Eight populated channels on WRX80 are not directly comparable to two DDR5 channels by generation label alone.

## 8. NVMe choices and enterprise differences

| Drive | Observed Singapore offer | Decision |
|---|---|---|
| Samsung 9100 PRO 2 TB | S$749, Dynacore, in stock | Priced 2 TB default, including on Gen4 boards |
| Samsung 990 PRO 4 TB with heatsink | S$1,389, Dynacore, in stock | Priced 4 TB default; do not stack its heatsink with a board heatspreader |
| [Lexar NM790 4 TB][H50] | S$899, PC Themes, preorder / out of stock | Conditional lower-cost option, not an available-price baseline |
| [Lexar NM790 4 TB, alternate seller][H57] | **S$859 including GST, theShop**, listed with local distributor warranty and 2–3 working day delivery | New 20 November price candidate; exact two-drive quantity unconfirmed |
| [ADATA LEGEND 900 PRO 2 TB][H58] | **S$479, Dynacore**, marked in stock on 20 November | Lower-price Gen4 candidate; sustained CI I/O and exact flash details need validation |
| Micron 7450 PRO 3.84 TB or similar enterprise NVMe | Quote required | Investigate for sustained write-heavy operation and full power-loss protection |

Prioritize capacity for useful caches, sustained mixed-I/O behavior, endurance, temperatures, price and warranty over advertised peak sequential bandwidth. Modern DRAMless TLC drives are not automatically unsuitable, but the application should validate their sustained behavior. Do not select a cheap QLC drive solely from its peak specification for a continuously write-heavy runner.

The [990 PRO data sheet][H51] specifies 2,400 TBW for 4 TB and 1,200 TBW for 2 TB. Those are warranty write budgets, not exact failure dates. Mirroring writes both members and does not double write endurance. Keep reasonable free space, monitor SMART/NVMe health and temperature, and avoid thermal throttling.

Consumer NVMe cannot automatically be declared a 3–5% equivalent to Hetzner's unspecified DC-Edition SSD model. The exact rented SSD SKU, workload, latency distribution and write duty cycle are needed. [Micron's 7450 documentation][H52] describes enterprise power-loss protection and different form factors, including M.2 22110. Check mechanical fit and any powered U.2/U.3 adapter requirements. [Kingston explains][H53] why a UPS does not replace protection inside the SSD.

### 20 November storage-price sensitivities

The Samsung BOM remains a documented reference rather than a claim that a Gen5 label is worth a premium on WRX80. [Samsung specifies TLC and 2 GB LPDDR4X for the 9100 PRO 2 TB][H59]. [ADATA specifies 3D NAND, HMB, SLC caching and 1,200 TBW][H60], but the cited data sheet does not establish TLC versus QLC or dedicated onboard DRAM. [Lexar specifies HMB, dynamic SLC caching and a 3,000 TBW rating for 4 TB][H61]. None establishes sustained CI equivalence from the specification sheet alone.

| Same rest of the build | Original Samsung subtotal | Alternative drives | Revised parts subtotal | Saving |
|---|---:|---|---:|---:|
| 5995WX, 256 GB, two 2 TB drives | S$8,609.40 | 2 × ADATA LEGEND 900 PRO 2 TB | **S$8,069.40** | S$540 |
| Two Intel hosts, 64 GB and two 2 TB drives per host | S$7,479.20 | 4 × ADATA LEGEND 900 PRO 2 TB | **S$6,399.20** | S$1,080 |
| 5995WX, 128 GB, two 4 TB drives | S$8,891.00 | 2 × Lexar NM790 4 TB | **S$7,831.00** | S$1,060 |
| 5995WX, 256 GB, two 4 TB drives | S$9,889.40 | 2 × Lexar NM790 4 TB | **S$8,829.40** | S$1,060 |

These are priced alternatives to test, not automatic substitutions that preserve a 3–5% performance margin. The Lexar seller lists delivery and warranty but did not reserve two units; the 128 GB DDR4 layout still needs exact qualification. The alternative with 256 GB and 2 × 4 TB avoids that particular 16 GB-module qualification gap while providing enough nominal capacity for both AX162 profiles. Endurance ratings are warranty limits, not promises about workload latency or service life.

The full workload and procurement acceptance procedure is in [04-validation-and-procurement.md](04-validation-and-procurement.md).

## Sources

The initial links were retrieved on 19 November 2026. The 20 November refresh reconfirmed the headline CPU/board/RAM prices and added H55–H61 and the alternative-drive scenarios. Retail listings are observations, not reserved inventory. Source claims, calculations and engineering recommendations are distinguished above.

[H01]: https://www.amd.com/en/products/processors/server/epyc/4th-generation-9004-and-8004-series/amd-epyc-9454p.html
[H02]: https://docs.hetzner.com/robot/dedicated-server/server-lines/ax-server/
[H03]: https://www.hetzner.com/dedicated-rootserver/ax162/
[H04]: https://browser.geekbench.com/v6/cpu/10776095
[H05]: https://browser.geekbench.com/v6/cpu/10772280
[H06]: https://browser.geekbench.com/v6/cpu/11222188
[H07]: https://browser.geekbench.com/v6/cpu/13840531
[H08]: https://www.geekbench.com/doc/geekbench6-benchmark-internals.pdf
[H09]: https://www.cpubenchmark.net/compare/5596vs4764/AMD-EPYC-9454P-vs-AMD-Ryzen-Threadripper-PRO-5995WX
[H10]: https://gamersnexus.net/cpus/not-waste-sand-ultra-7-270k-plus-cpu-review-benchmarks
[H11]: https://www.phoronix.com/review/intel-core-ultra-7-270k-plus/3
[H12]: https://mail.openbenchmarking.org/test/pts/build-wasmer
[H13]: https://www.phoronix.com/review/amd-threadripper-9970x-9980x-linux/2
[H14]: https://www.phoronix.com/review/amd-ryzen-9950x3d2-benchmarks
[H15]: https://www.intel.com/content/www/us/en/products/sku/245692/intel-core-ultra-7-processor-270k-plus-36m-cache-up-to-5-50-ghz/specifications.html
[H16]: https://founderextreme.com/product/amd-ryzen-threadripper-pro-series-custom-order/
[H17]: https://www.electronicscrazy.sg/asus-pro-ws-wrx80e-sage-se-wifi-amd-threadripper-pro-eatx-workstation-motherboard-black/
[H18]: https://www.techdeals.com.sg/products/crucial-ddr4-3200-cl22-udimm-desktop-pc-ram-memory-ct32g4dfd832a-32gb
[H19]: https://dynacoretech.com/products/samsung-9100-pro-2tb-14700mb-s-gen5-pcie5-0-m-2-ssd5yrs-8806095811710
[H20]: https://www.techdeals.com.sg/products/arctic-freezer-4u-m-cpu-air-cooler-sp6-sp3-str5-tr4-swrx8-strx4-lga4677-lga4189
[H21]: https://www.techdeals.com.sg/products/fractaldesign-meshify-2-xl-black-tg-light-tint-dark-tint-pc-case
[H22]: https://voltapc.sg/shop/?filter_brand=seasonic
[H23]: https://servers.asus.com/support/faq/detail/1049293
[H24]: https://www.amd.com/en/support/downloads/drivers.html/processors/ryzen-threadripper-pro/ryzen-threadripper-pro-5000wx-series/amd-ryzen-threadripper-pro-5995wx.html
[H25]: https://www.asus.com/sg/motherboards-components/motherboards/workstation/pro-ws-wrx80e-sage-se-wifi/techspec/
[H26]: https://www.asus.com/us/motherboards-components/motherboards/workstation/pro-ws-wrx80e-sage-se-wifi/helpdesk_qvl_memory?model2Name=Pro-WS-WRX80E-SAGE-SE-WIFI
[H27]: https://www.techdeals.com.sg/products/crucial-ct16g4dfra32a-16gb-ddr4-3200-udimm-desktop-ram-memory
[H28]: https://dynacoretech.com/products/samsung-990-pro-with-heatsink-pcie-4-0-m-2-4tb-mz-v9p4t0cw-8806094946857
[H29]: https://dynacoretech.com/collections/cpu
[H30]: https://dynacoretech.com/products/amd-ryzen-9-9950x3d-4-3ghz-16c-32t-144mb-cache-tray-processor4yrs-100-000000719
[H31]: https://www.pcthemes.com.sg/motherboard/intel-motherboard?price_min=1&stock_id=1
[H32]: https://dynacoretech.com/products/msi-b850m-gaming-plus-wifi-am5-m-atx-motherboard3yrs-4711377347570
[H33]: https://6amproductionstech.com/allproducts/p/lexar-thor-rgb-2nd-gen-ddr5-64gb-2x32gb
[H34]: https://6amproductionstech.com/allproducts/p/klevv-cras-v-rgb-ddr5-128gb-2x64gb
[H35]: https://www.techdeals.com.sg/collections/cpu-cooler/products/thermalright-aqua-elite-v3-argb-360-aio-cooler-black
[H36]: https://dynacoretech.com/products/cooler-master-elite-502-steel-tempered-glass-atx-case-with-3-x-120mm-argb-fans
[H37]: https://dynacoretech.com/collections/psu
[H38]: https://www.klevv.com/HyAdmin/upload/goodFile/KLEVV%20CRAS%20V%20RGB%20DDR5%20Memory%20Compatibility%20List_Nov26.pdf
[H39]: https://www.thermalright.com/product/aqua-elite-360-v3/
[H40]: https://sg.msi.com/Motherboard/B860M-GAMING-PLUS-WIFI/Specification
[H41]: https://www.amd.com/en/products/processors/ryzen-threadripper/9000-series/amd-ryzen-threadripper-9970x.html
[H42]: https://www.asus.com/us/motherboards-components/motherboards/workstation/pro-ws-trx50-sage-wifi/techspec/
[H43]: https://theshop.sg/products/pc-parts/cpu/amd-ryzen-threadripper-9970x
[H44]: https://theshop.sg/products/pc-parts/mainboard/asus-pro-ws-trx50-sage-wifi
[H45]: https://simlimsquare.com.sg/product/kingston-ksm56r46bd8pmi-32hai-32gb-5600mts-ddr5-ecc-reg-cl4-20781
[H46]: https://simlimsquare.com.sg/product/kingston-ksm56r46bd4pmi-64hai-64gb-5600mts-ddr5-ecc-reg-cl4-20800
[H47]: https://www.kingston.com/en/memory/search/model/108911/asus-pro-ws-trx50-sage-wifi-motherboard?status_2=active
[H48]: https://dynacoretech.com/products/amd-ryzen%E2%84%A2-9-9950x3d2-dual-edition-desktop-processor-730143318327
[H49]: https://www.amd.com/en/products/processors/desktops/ryzen/9000-series/amd-ryzen-9-9950x.html
[H50]: https://www.pcthemes.com.sg/M2-Solid-State-Drives-SSD/lexar-nm790-4tb-nvme-gen4-solid-state-drive-7400r-6500w
[H51]: https://download.semiconductor.samsung.com/resources/data-sheet/samsung_nvme_ssd_990_pro_datasheet_rev.2.0.pdf
[H52]: https://www.micron.com/content/dam/micron/global/public/documents/products/technical-marketing-brief/7450-nvme-ssd-tech-prod-spec.pdf
[H53]: https://www.kingston.com/en/blog/servers-and-data-centers/ssd-power-loss-protection
[H54]: https://theshop.sg/products/pc-parts/cpu/amd-ryzen-threadripper-9980x
[H55]: https://www.asus.com/motherboards-components/motherboards/workstation/pro-ws-wrx80e-sage-se-wifi/helpdesk_cpu?model2Name=Pro-WS-WRX80E-SAGE-SE-WIFI
[H56]: https://dlcdnets.asus.com/pub/ASUS/mb/SocketTRX4/Pro_WS_WRX80E-SAGE_SE_WIFI/E19401_Pro_WS_WRX80E-SAGE_SE_WIFI_UM_V2_WEB.pdf
[H57]: https://theshop.sg/products/pc-parts/m2-nvme-ssd/lexar-nm790-m-2-2280-pcie-gen-4x4-nvme-ssd-4tb
[H58]: https://dynacoretech.com/products/adata-legend-900-pro-2tb-ssd
[H59]: https://www.samsung.com/sg/memory-storage/nvme-ssd/9100-pro-2tb-nvme-pcie-gen-5-mz-vap2t0bw/
[H60]: https://webapi3.adata.com/storage/downloadfile/datasheet_legend_900_pro_pcie_gen4_x4_m2_2280_ssd_20250731.pdf
[H61]: https://americas.lexar.com/product/lexar-nm790-m-2-2280-pcie-gen-4x4-nvme-ssd/
