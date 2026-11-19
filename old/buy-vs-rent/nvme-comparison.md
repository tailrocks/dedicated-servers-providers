# NVMe for sustained CI work

[Study index](README.md) · [Builds](recommended-builds.md) · [Performance](ci-cd-performance-analysis.md)

Checked **20 November 2026, Asia/Saigon**. This is internet research. Every measured result below belongs to its cited independent publisher; no drive or build was benchmarked for this report.

## Decision

Use **two Lexar NM790 2 TB, LNM790X002T-RNNNG**, for the AX162-2 capacity class, or **two NM790 4 TB, LNM790X004T-RNNNG**, for the AX162-1 class. The Singapore listings are **S$504 and S$859 per drive**, respectively, including GST and standard local delivery. The seller advertises ordering and delivery, not a reserved two-drive inventory. [2 TB offer][S01] · [4 TB offer][S02]

The NM790 is a value recommendation based on its price, capacity, endurance, and published sustained-write behavior. It is **not a claim that consumer storage matches the unspecified Hetzner DC SSDs within 3–5%**. For an existing runner whose bottleneck is CPU compilation, spending the saved money on enough RAM and CPU capacity is a stronger purchase than paying a Gen5 premium on a Gen4 motherboard. For databases in integration tests, power-loss protection and sustained mixed-I/O latency can justify enterprise storage independently of peak bandwidth.

## Exact candidates and vendor specifications

Peak rates below are manufacturer claims in decimal MB/s, usually with caches active and high queue depths. They are not CI throughput or sustained full-drive results. `k` means thousand IOPS. The DWPD column for consumer products is a calculation: `TBW / capacity_TB / (365 × 5)`, rather than an enterprise workload guarantee. Warranty conditions include write limits and vary by regional seller.

| Exact model | Interface / physical form | Peak read / write MB/s | Peak random read / write IOPS | Endurance and warranty | Assessment |
|---|---|---:|---:|---|---|
| Lexar NM790 2 TB, LNM790X002T-RNNNG | PCIe 4.0 ×4; M.2 2280; single-sided; HMB | 7,400 / 6,500 | 1,000k / 900k | 1,500 TBW; 5-year limited; calculated 0.411 DWPD | Preferred 2 TB value option; dedicated DRAM absent; current NAND revision is not guaranteed by a historical review |
| Lexar NM790 4 TB, LNM790X004T-RNNNG | PCIe 4.0 ×4; M.2 2280; single-sided; HMB | 7,400 / 6,500 | 900k / 900k | 3,000 TBW; 5-year limited; calculated 0.411 DWPD | Preferred large cache/workspace option; strongest directly cited sustained-write evidence |
| Samsung 990 PRO 2 TB, MZ-V9P2T0BW | PCIe 4.0 ×4; M.2 2280; TLC; 2 GB DRAM | 7,450 / 6,900 | 1,400k / 1,550k | 1,200 TBW; 5 years or TBW; calculated 0.329 DWPD | High-end Gen4; buy only if its price premium is modest for the desired mixed-I/O behavior |
| Samsung 990 PRO 4 TB, MZ-V9P4T0BW; heatsink SKU MZ-V9P4T0CW | PCIe 4.0 ×4; M.2 2280; TLC; 4 GB DRAM | 7,450 / 6,900 | 1,600k / 1,550k | 2,400 TBW; 5 years or TBW; calculated 0.329 DWPD | Consistent drive with DRAM; currently expensive in the checked Singapore listing |
| Samsung 9100 PRO 2 TB, MZ-VAP2T0BW | PCIe 5.0 ×4; M.2 2280; TLC; 2 GB LPDDR4X | 14,700 / 13,400 | **1,850k / 2,600k** | 1,200 TBW; 5 years or TBW; calculated 0.329 DWPD | Gen5 alternative; the 2 TB specification is not the family's 2,200k read marketing headline |
| ADATA LEGEND 900 PRO 2 TB, SLEG-900P-2TCS | PCIe 4.0 ×4; M.2 2280; HMB; vendor specifies “3D NAND” | 7,400 / 6,500 | Not stated in the retrieved exact-model data sheet | 1,200 TBW; 5-year limited; calculated 0.329 DWPD | Lower quoted price, but no adequate independent exact-model sustained-write result recovered; do not assume its flash/controller from a similarly named drive |
| WD_BLACK SN850X 4 TB with factory heatsink, WDS400T2XHE | PCIe 4.0 ×4; M.2 2280; TLC; 80 × 24.46 × 10.31 mm envelope | 7,300 / 6,600 | 1,200k / 1,100k | 2,400 TBW; 5 years or endurance limit; calculated 0.329 DWPD | Verified Malaysian 4 TB retail alternative; remove the motherboard's removable M.2 cover and retain the drive heatsink [S30] |
| Micron 7450 PRO 1.92 TB, MTFDKBG1T9TFR-1BC1ZABYYR | PCIe 4.0 ×4; **M.2 22110**; enterprise TLC | 5,000 / 2,400 | 735k / 120k | 3,650 TBW; published 1 DWPD; 5-year limited | Enterprise option with PLP; checked regional reseller says supply shortage |
| Micron 7450 PRO 3.84 TB, MTFDKCC3T8TFR-1BC15ABYY | PCIe 4.0 ×4; **2.5-inch U.3, 15 mm**; enterprise TLC | 6,800 / 5,300 | 1,000k / 180k | 7,300 TBW; published 1 DWPD; 5-year limited | Capacity-matched datacenter alternative; regional price/stock not verified; adapter/backplane and power costs required |

Sources: Lexar's capacity-specific sheet [S03], Samsung 990 PRO sheet [S04], Samsung's **2 TB** 9100 PRO specification section [S05], ADATA's July 2025 sheet [S06], Micron's product brief and part catalog [S07–S09]. Enterprise IOPS are obtained under different steady-state and queue-depth conditions from consumer burst specifications; comparing the two columns as a single ranking would be misleading.

## Published sustained behavior and thermal evidence

| Independently tested drive | Published observation | What it establishes / what it does not |
|---|---|---|
| NM790 4 TB | Tom's Hardware's 15-minute sequential-write procedure reported roughly **5.9 GB/s in pseudo-SLC and 2.6 GB/s in native TLC** [S10] | Useful evidence that writes remain substantial after cache exhaustion; not random Docker/metadata latency or a promise for a later flash revision |
| 990 PRO 4 TB | Tom's Hardware reported about **6.2 GB/s for over 75 seconds**, then **above 1.6 GB/s in TLC**, without its usual folding collapse [S11] | Consistency matters; its high price does not buy the highest large sequential-write rate |
| 9100 PRO 2 TB | Tom's Hardware reported about **12.9 GB/s cached**, then **just below 1.9 GB/s** in TLC; peak sensor temperature **67°C** in that test [S12] | Gen5 peak bandwidth is real in a suitable test system, but post-cache behavior is far below 13.4 GB/s; the review used cooling and does not predict tropical ambient temperatures |
| NM790 4 TB, separate publisher | PC Gamer reported cache exhaustion after about **642 GB** and a **72°C** temperature during a long transfer, with approximately **23°C ambient** [S13] | Independent confirmation that cache size and temperature depend on method; do not merge its cache size with another review as one controlled result |
| ADATA LEGEND 900 PRO 2 TB | Adequate independent exact-model sustained trace **not found** | Specification-only alternative; its lower price alone does not settle sustained CI behavior |
| Micron 7450 PRO exact listed variants | Vendor steady-state specification available; matched independent drive-level trace **not recovered** | Stronger enterprise durability/PLP feature evidence, without fabricating comparative CI results |
| SN850X 4 TB, independent community drive-fill report | The original September 2026 reviewer reports about 1.2 TB of cache at roughly 6,655 MB/s, followed by roughly 1,808 MB/s in the first fresh-state 128 KiB / QD256 fill [S31] | One borrowed/refurbished sample and a deep-queue sequential test, not a CI trace or a thermal qualification of the quoted factory-heatsink revision. Confidence is lower than a matched multi-drive lab comparison. |

Use the supplied motherboard heatspreaders with bare M.2 drives and retain front-to-back case airflow. Do not stack a factory SSD heatsink underneath a motherboard heatspreader. The 990 PRO heatsink model is about 25 mm wide and 8.88 mm high according to its retailer's manufacturer-derived specifications [S14]; its fit is different from a bare 22 mm module. A published room-temperature result is not a thermal guarantee for an unattended machine in Singapore or Malaysia.

## Regional procurement observations

All checks are dated 20 November 2026. A listing is not a physical inventory reservation, and a button alone is not proof of stock. The table preserves the actual seller and tax language. Local prices are not automatically cross-border delivered prices.

| Model | Singapore: seller / price / status | Malaysia: seller / price / status |
|---|---|---|
| NM790 2 TB | **theShop S$504**, GST included, free stated delivery, local distributor warranty; **available to order, physical stock unverified** [S01] | **ITX Lab RM1,430**, exact 2 TB variant `9424-9719`, public product data `is_in_stock=true`, `is_purchasable=true`; quantity, shipping and tax breakdown not published in retrieved variant [S15] |
| NM790 4 TB | **theShop S$859**, same terms [S02]. CR Group search evidence S$851.90 marked available, but direct page initially returned HTTP 403 and returned HTTP 404 on final review; not used to shave S$7.10 from the BOM [S16] | Sun Cycle **RM2,599 suggested retail price**, SKU LNM790X004T-RNNNG; distributor reference, **not a retail checkout or stock confirmation** [S17]. No sufficiently verified local retail offer used in the main BOM |
| 990 PRO 2 TB | No preferable exact-current offer selected; compare only with a fresh capacity-specific quote | **Brightstar RM2,699**, `MZ-V9P2T0BW` product variant available; exact public JSON, not the product page's 1 TB minimum price [S18] |
| 990 PRO 4 TB | **Dynacore S$1,389** for heatsink SKU MZ-V9P4T0CW, explicit in-stock claim, 5-year local warranty, free stated delivery [S14] | Brightstar bare 4 TB variant **RM4,679**, `available=false`: **out of stock**, not a purchase option [S18] |
| 9100 PRO 2 TB | **Dynacore S$749**, explicit in-stock claim and 5-year local warranty [S19] | Exact current capacity-specific price/stock not verified; do not reuse a multi-capacity minimum price |
| ADATA LEGEND 900 PRO 2 TB | **Dynacore S$479**, explicit in-stock claim, 5-year local warranty, free stated delivery [S20] | Exact local price/stock not verified |
| Micron 7450 PRO 1.92 TB 22110 | RS catalog **S$1,517.73 excluding GST**; product page **supply shortage / no restock date** [S21–S22] | RS catalog **RM5,002.53**; product page **supply shortage / no restock date** [S23–S24] |
| Micron 7450 PRO 3.84 TB U.3 | Quote required; SourceIT's current enterprise catalog has moved to quotations for its listed models [S25] | Quote required; no verified local purchasable exact-SKU price obtained |
| SN850X 4 TB with heatsink | No cheaper exact local price needed for the selected Singapore NM790 baskets | **GameShop RM3,532**, exact WDS400T2XHE variant `42164827816013`, public JSON `available=true`; alternative Dotatech exact SKU **RM3,999**, available [S32–S34]. A stated 7% bank-transfer promotion is excluded until its exact checkout applicability is confirmed. Two GameShop drives give the MY-INTEL128-4 subtotal of **RM23,357**. |

**Rejected stale result:** PC Themes' search/category excerpt advertised NM790 2 TB at S$489, but the opened product page showed **S$579 and out of stock** [S26]. The latter controls the decision. ITX Lab's capacity selector was checked through its public WooCommerce `data-product_variations` attribute; Brightstar's exact variants through its public Shopify product JSON. These are public retail data, not signed-in carts or purchases. Numeric Shopify prices are minor units: `269900 / 100 = RM2,699`.

Singapore is the primary purchasing market for the recommended workstation. Malaysia's lower standalone 2 TB SSD price does not prove a cheaper complete imported machine: transport, destination taxes, payment conversion and cross-border warranty differ. See [regional procurement](malaysia-hardware.md).

The Malaysian SN850X alternative supplies a genuinely quoted 4 TB retail option instead of substituting Sun Cycle's NM790 suggested retail price. Its standard M-key 2280 interface fits the selected ASUS slots. The larger factory-heatsink envelope and headless board layout support a mechanical-fit inference, not a separately tested ASUS qualification. Do not stack the board covers on top, and follow the board's double-sided-drive retention instructions. No controlled thermal result for this exact heatsink revision was found; retain case airflow. [Manufacturer dimensions][S30] · [Country compatibility evidence](malaysia-hardware.md)

## Organization of the two drives

| Layout | Nominal capacity with 2 × 2 TB / 2 × 4 TB | CI benefit | Cost / risk / decision |
|---|---|---|---|
| Two independent filesystems | 4 TB / 8 TB total, split into separate volumes | Put OS, runner services and persistent artifacts on one; disposable workspaces and build caches on the other; concurrent I/O can use both devices | Best capacity per dollar for replaceable workers, but one failed disk can still stop its assigned service and lose its local cache |
| Linux software RAID1 | 2 TB / 4 TB before formatting | Continued operation after one drive failure; simpler one-volume allocation | **Default for the single consolidated workstation** if continuity matters. Both devices receive writes; write endurance is not doubled. RAID is not backup |
| Two independent drives with OS/cache separation | Same raw capacity as independent above | Easier cache eviction and isolation of some write bursts | This is an alternative use of the same two drives, not an extra free third disk. Keep OS/artifact backups elsewhere |
| RAID0 | 4 TB / 8 TB before formatting | May improve large, concurrent, sequential scratch transfers | **Not recommended as default**: loss of either device destroys the array, and no published end-to-end CI evidence justifies the risk/premium here |
| Separate third scratch drive | Additional capacity and write budget | Useful when many jobs contend for the same cache or integration-test data | Only add when the expected workload needs it; price the actual drive and account for motherboard slot/chipset sharing. Not silently included |

Two 2 TB retail drives exceed the AX162-2's 3.84 TB raw / 1.92 TB mirrored nominal capacities; two 4 TB drives exceed the AX162-1's 7.68 TB raw / 3.84 TB mirrored capacities. Decimal capacity is not formatted GiB/TiB. RAID configuration is a choice; merely advertising two rental SSDs does not establish the installed RAID mode.

## Motherboard and filesystem implications

The recommended WRX80 board accepts ordinary PCIe NVMe M.2 2280 devices; the two primary onboard CPU-connected sockets avoid an unnecessary storage adapter. Its Gen4 link limits a Gen5 drive to Gen4 signaling. The exact socket and shared U.2/chipset routes are recorded in [the compatibility review](recommended-builds.md). A 22110 enterprise M.2 must use a socket/standoff documented for 110 mm devices. A U.3 drive does **not** fit an M.2 socket: require a compatible powered PCIe/U.2/U.3 path and check support for the exact drive. Do not assume a SATA cable or an unpowered mechanical adapter is sufficient.

Docker's documentation explains that OverlayFS copies up changed files, that copy-up can amplify writes, and that volumes can avoid storage-driver overhead for suitable write-intensive data [S27]. BuildKit supports independent build stages and cache mounts; a well-ordered Dockerfile and correctly keyed dependency cache can avoid work altogether [S28]. Rust incremental outputs and package-manager stores contain many smaller files, so CPU scheduling, metadata latency, decompression and cache hits can dominate a headline sequential GB/s figure. No source recovered establishes a universal percentage reduction in Cargo or TypeScript build time from a Gen4-to-Gen5 upgrade.

## Endurance sizing without invented write measurements

Use **host writes reported by the drive**, not source-code size. As an analytical example, 0.5 TB/day of host writes would consume 182.5 TB/year; a 1,500 TBW budget corresponds to about 8.2 years of that arithmetic, but the 5-year warranty can expire sooner and failure can occur earlier. At 2 TB/day, the same budget corresponds to about 2.05 years. For the 3,000 TBW 4 TB drive the corresponding arithmetic is 16.4 and 4.1 years. These are **budget calculations, not predicted service lives**. A RAID1 mirror writes the same workload to each member.

Maintain free space and sensible cache eviction, keep source and important artifacts backed up, and inspect health/temperature as routine operation. A UPS helps ride through external power loss; it does not turn a consumer SSD into a drive with capacitor-backed power-loss protection [S29]. The recommendation is complete from public evidence and does not require buying hardware or running a new benchmark to finish this research.

## Sources

[S01]: https://theshop.sg/products/pc-parts/m2-nvme-ssd/lexar-nm790-m-2-2280-pcie-gen-4x4-nvme-ssd-2tb
[S02]: https://theshop.sg/products/pc-parts/m2-nvme-ssd/lexar-nm790-m-2-2280-pcie-gen-4x4-nvme-ssd-4tb
[S03]: https://resources.lexar.com/download/1048/documents/13165/lexar-productsheet-ssd-nm790-en-202410.pdf
[S04]: https://download.semiconductor.samsung.com/resources/data-sheet/samsung_nvme_ssd_990_pro_datasheet_rev.2.0.pdf
[S05]: https://www.samsung.com/sg/memory-storage/nvme-ssd/9100-pro-2tb-nvme-pcie-gen-5-mz-vap2t0bw/
[S06]: https://webapi3.adata.com/storage/downloadfile/datasheet_legend_900_pro_pcie_gen4_x4_m2_2280_ssd_20250731.pdf
[S07]: https://www.micron.com/content/dam/micron/global/public/products/product-flyer/7450-nvme-ssd-product-brief.pdf
[S08]: https://www.micron.com/products/storage/ssd/data-center-ssd/7450-ssd/part-catalog/part-detail/mtfdkbg1t9tfr-1bc15abyy
[S09]: https://www.micron.com/products/storage/ssd/data-center-ssd/7450-ssd/part-catalog
[S10]: https://www.tomshardware.com/reviews/lexar-nm790-ssd-review/2
[S11]: https://www.tomshardware.com/reviews/samsung-990-pro-4tb-ssd-review/2
[S12]: https://www.tomshardware.com/pc-components/ssds/samsung-9100-pro-ssd-review/2
[S13]: https://www.pcgamer.com/lexar-nm790-4tb-ssd-review/
[S14]: https://dynacoretech.com/products/samsung-990-pro-with-heatsink-pcie-4-0-m-2-4tb-mz-v9p4t0cw-8806094946857
[S15]: https://itxlab.com.my/product/lexar-nm790-m-2-2280-pcie-gen4x4-nvme-ssd-512gb-1tb-2tb/
[S16]: https://crgroup.com.sg/product/lexar-nm790-4tb-pcie-gen4-nvme-ssd/
[S17]: https://www.suncycle.com.my/brand/lexar/87
[S18]: https://brightstarcomp.com/products/samsung-990-pro-pcie-gen4x4-m-2-nvme-ssd.js
[S19]: https://dynacoretech.com/products/samsung-9100-pro-2tb-14700mb-s-gen5-pcie5-0-m-2-ssd5yrs-8806095811710
[S20]: https://dynacoretech.com/products/adata-legend-900-pro-2tb-ssd
[S21]: https://sg.rs-online.com/web/c/computing-peripherals/memory-data-storage/hard-drives/?if=micron-hard-drives
[S22]: https://sg.rs-online.com/web/p/hard-drives/2658599
[S23]: https://my.rs-online.com/web/c/computing-peripherals/memory-data-storage/hard-drives/?if=micron-hard-drives
[S24]: https://my.rs-online.com/web/p/hard-drives/2658599
[S25]: https://sourceit.com.sg/collections/micron-enterprise-data-center-ssds
[S26]: https://www.pcthemes.com.sg/M2-Solid-State-Drives-SSD/lexar-nm790-2tb-nvme-gen4-solid-state-drive-7400r-6500w
[S27]: https://docs.docker.com/engine/storage/drivers/overlayfs-driver/
[S28]: https://docs.docker.com/build/cache/optimize/
[S29]: https://www.kingston.com/en/blog/servers-and-data-centers/ssd-power-loss-protection
[S30]: https://documents.sandisk.com/content/dam/asset-library/en_us/assets/public/western-digital/product/internal-drives/wd-black-ssd/data-sheet-wd-black-sn850x-nvme-ssd.pdf
[S31]: https://freshflash4096.github.io/western-digital-sn850x-4tb-review/
[S32]: https://www.gameshop.my/products/wd_black-sn850x-nvme-ssd-with-heatsink
[S33]: https://www.gameshop.my/products/wd_black-sn850x-nvme-ssd-with-heatsink.js
[S34]: https://www.dotatech.com.my/products/wd_black-sn850x-series-nvme-pcie-gen4-x4-m-2-ssd-4tb-8tb.js

Signed-off-by: Alexey Zhokhov
