# Reproducible financial results

[Study index](README.md) · [Interpretation](rent-vs-buy.md) · [Assumptions](break-even-analysis.md)

Generated from `data/economic-builds.json` and `data/market-inputs.json` by `calculate.py`.

All figures are SGD; no premises/rack rent. Moderate estimated wall power is the default. Electricity and a separately purchased business internet line are independently selectable. The existing-line case is the electricity-only column. See the CSVs for every requested horizon.

Hetzner SG rows include the documented 9% non-GST-registered buyer scenario and IPv4. Other sellers retain their stated/unknown tax basis: known-charge comparisons are not tax-normalized final invoices. Crossings against different RAM, disks, CPUs or node counts are cash comparisons, not performance-equivalence certificates.

## SG-WRX256-2 — 1 × 5995WX, 256 GB/node, 2 × 2 TB/node

Hardware **S$13330.00**; modeled moderate electricity **S$62.55/month**; separate business internet **S$105.00/month**; maintenance **S$0**. Procurement basis: A/E. Closest single-host compiler candidate. Custom-order CPU and listed cooler. Component subtotal under local collection/free eligible delivery and fee-free payment; final mixed-seller invoicing/stock not guaranteed.

| Rental | Monthly / setup S$ | Hardware | + electricity | + internet | + both |
|---|---:|---:|---:|---:|---:|
| Hetzner AX162-1 | 948.74 / 469.74 | 14 | 15 | 16 | 17 |
| Hetzner AX162-2 | 1304.14 / 647.43 | 10 | 11 | 11 | 12 |
| UHost AX162-R | 283.73 / 154.76 | 47 | 60 | 74 | 114 |
| PlusClouds / Radius AX162-S | 324.63 / 582.63 | 40 | 49 | 59 | 82 |
| PlusClouds Radius AX102-U | 168.69 / 381.33 | 77 | 122 | 204 | 11352 |
| ServerWala Helsinki 128 GB | 432.04 / 0.00 | 31 | 37 | 41 | 51 |
| ServerWala Helsinki 256 GB | 432.04 / 0.00 | 31 | 37 | 41 | 51 |
| DediJet Singapore Ryzen 9 9950X | 346.92 / 0.00 | 39 | 47 | 56 | 75 |
| IP-Projects sTR5 L G1 | 764.64 / 486.02 | 17 | 19 | 20 | 22 |
| INTROSERV DC4SC-a4 AE9455 SG | 1559.35 / 1213.17 | 8 | 9 | 9 | 9 |
| VPSShell Dedicated EPYC Max | 1797.78 / 0.00 | 8 | 8 | 8 | 9 |
| Arxan EPYC 9454P | 304.55 / 118.37 | 44 | 55 | 67 | 97 |
| UHost AX162-R plus 2 × 3.84 TB NVMe | 394.64 / 154.76 | 34 | 40 | 46 | 59 |
| 040Hosting 7-NVME24 (legacy listing) | 338.81 / 134.67 | 39 | 48 | 57 | 78 |
| DediJet Singapore, two 9950X nodes (quantity scenario) | 693.84 / 0.00 | 20 | 22 | 23 | 26 |
| PlusClouds Radius AX162-R 256 GB | 324.63 / 768.34 | 39 | 48 | 58 | 80 |

| Horizon | Hardware | + electricity | + business internet | + both | + electricity and residential internet* |
|---|---:|---:|---:|---:|---:|
| 6 months | 13330.00 | 13705.32 | 13960.00 | 14335.32 | 13853.26 |
| 12 months | 13330.00 | 14080.64 | 14590.00 | 15340.64 | 14396.52 |
| 18 months | 13330.00 | 14455.97 | 15220.00 | 16345.97 | 14939.79 |
| 24 months | 13330.00 | 14831.29 | 15850.00 | 17351.29 | 15483.05 |
| 36 months | 13330.00 | 15581.93 | 17110.00 | 19361.93 | 16593.69 |
| 48 months | 13330.00 | 16332.58 | 18370.00 | 21372.58 | 17704.34 |
| 60 months | 13330.00 | 17083.22 | 19630.00 | 23383.22 | 18814.98 |

*Residential service requires eligibility and suitable permitted use; router/installation exceptions and renewal assumptions are in [internet costs](internet-costs.md). The business subscription's minimum contract remains payable if service is cancelled early.

## SG-WRX256-4 — 1 × 5995WX, 256 GB/node, 2 × 4 TB/node

Hardware **S$14040.00**; modeled moderate electricity **S$62.55/month**; separate business internet **S$105.00/month**; maintenance **S$0**. Procurement basis: Largest single-host capacity configuration in both dimensions. Component subtotal under local collection/free eligible delivery and fee-free payment; final mixed-seller invoicing/stock not guaranteed.

| Rental | Monthly / setup S$ | Hardware | + electricity | + internet | + both |
|---|---:|---:|---:|---:|---:|
| Hetzner AX162-1 | 948.74 / 469.74 | 15 | 16 | 17 | 18 |
| Hetzner AX162-2 | 1304.14 / 647.43 | 11 | 11 | 12 | 12 |
| UHost AX162-R | 283.73 / 154.76 | 49 | 63 | 78 | 120 |
| PlusClouds / Radius AX162-S | 324.63 / 582.63 | 42 | 52 | 62 | 86 |
| PlusClouds Radius AX102-U | 168.69 / 381.33 | 81 | 129 | 215 | 11974 |
| ServerWala Helsinki 128 GB | 432.04 / 0.00 | 33 | 38 | 43 | 54 |
| ServerWala Helsinki 256 GB | 432.04 / 0.00 | 33 | 38 | 43 | 54 |
| DediJet Singapore Ryzen 9 9950X | 346.92 / 0.00 | 41 | 50 | 59 | 79 |
| IP-Projects sTR5 L G1 | 764.64 / 486.02 | 18 | 20 | 21 | 23 |
| INTROSERV DC4SC-a4 AE9455 SG | 1559.35 / 1213.17 | 9 | 9 | 9 | 10 |
| VPSShell Dedicated EPYC Max | 1797.78 / 0.00 | 8 | 9 | 9 | 9 |
| Arxan EPYC 9454P | 304.55 / 118.37 | 46 | 58 | 70 | 102 |
| UHost AX162-R plus 2 × 3.84 TB NVMe | 394.64 / 154.76 | 36 | 42 | 48 | 62 |
| 040Hosting 7-NVME24 (legacy listing) | 338.81 / 134.67 | 42 | 51 | 60 | 82 |
| DediJet Singapore, two 9950X nodes (quantity scenario) | 693.84 / 0.00 | 21 | 23 | 24 | 27 |
| PlusClouds Radius AX162-R 256 GB | 324.63 / 768.34 | 41 | 51 | 61 | 85 |

| Horizon | Hardware | + electricity | + business internet | + both | + electricity and residential internet* |
|---|---:|---:|---:|---:|---:|
| 6 months | 14040.00 | 14415.32 | 14670.00 | 15045.32 | 14563.26 |
| 12 months | 14040.00 | 14790.64 | 15300.00 | 16050.64 | 15106.52 |
| 18 months | 14040.00 | 15165.97 | 15930.00 | 17055.97 | 15649.79 |
| 24 months | 14040.00 | 15541.29 | 16560.00 | 18061.29 | 16193.05 |
| 36 months | 14040.00 | 16291.93 | 17820.00 | 20071.93 | 17303.69 |
| 48 months | 14040.00 | 17042.58 | 19080.00 | 22082.58 | 18414.34 |
| 60 months | 14040.00 | 17793.22 | 20340.00 | 24093.22 | 19524.98 |

*Residential service requires eligibility and suitable permitted use; router/installation exceptions and renewal assumptions are in [internet costs](internet-costs.md). The business subscription's minimum contract remains payable if service is cancelled early.

## SG-WRX128-4 — 1 × 5995WX, 128 GB/node, 2 × 4 TB/node

Hardware **S$10022.00**; modeled moderate electricity **S$62.55/month**; separate business internet **S$105.00/month**; maintenance **S$0**. Procurement basis: D. Exact eight-DIMM topology; indicative memory quote only. Component subtotal under local collection/free eligible delivery and fee-free payment; final mixed-seller invoicing/stock not guaranteed.

| Rental | Monthly / setup S$ | Hardware | + electricity | + internet | + both |
|---|---:|---:|---:|---:|---:|
| Hetzner AX162-1 | 948.74 / 469.74 | 11 | 11 | 12 | 13 |
| Hetzner AX162-2 | 1304.14 / 647.43 | 8 | 8 | 8 | 9 |
| UHost AX162-R | 283.73 / 154.76 | 35 | 45 | 56 | 85 |
| PlusClouds / Radius AX162-S | 324.63 / 582.63 | 30 | 37 | 43 | 61 |
| PlusClouds Radius AX102-U | 168.69 / 381.33 | 58 | 91 | 152 | 8452 |
| ServerWala Helsinki 128 GB | 432.04 / 0.00 | 24 | 28 | 31 | 38 |
| ServerWala Helsinki 256 GB | 432.04 / 0.00 | 24 | 28 | 31 | 38 |
| DediJet Singapore Ryzen 9 9950X | 346.92 / 0.00 | 29 | 36 | 42 | 56 |
| IP-Projects sTR5 L G1 | 764.64 / 486.02 | 13 | 14 | 15 | 16 |
| INTROSERV DC4SC-a4 AE9455 SG | 1559.35 / 1213.17 | 6 | 6 | 7 | 7 |
| VPSShell Dedicated EPYC Max | 1797.78 / 0.00 | 6 | 6 | 6 | 7 |
| Arxan EPYC 9454P | 304.55 / 118.37 | 33 | 41 | 50 | 73 |
| UHost AX162-R plus 2 × 3.84 TB NVMe | 394.64 / 154.76 | 26 | 30 | 35 | 44 |
| 040Hosting 7-NVME24 (legacy listing) | 338.81 / 134.67 | 30 | 36 | 43 | 58 |
| DediJet Singapore, two 9950X nodes (quantity scenario) | 693.84 / 0.00 | 15 | 16 | 18 | 20 |
| PlusClouds Radius AX162-R 256 GB | 324.63 / 768.34 | 29 | 36 | 43 | 59 |

| Horizon | Hardware | + electricity | + business internet | + both | + electricity and residential internet* |
|---|---:|---:|---:|---:|---:|
| 6 months | 10022.00 | 10397.32 | 10652.00 | 11027.32 | 10545.26 |
| 12 months | 10022.00 | 10772.64 | 11282.00 | 12032.64 | 11088.52 |
| 18 months | 10022.00 | 11147.97 | 11912.00 | 13037.97 | 11631.79 |
| 24 months | 10022.00 | 11523.29 | 12542.00 | 14043.29 | 12175.05 |
| 36 months | 10022.00 | 12273.93 | 13802.00 | 16053.93 | 13285.69 |
| 48 months | 10022.00 | 13024.58 | 15062.00 | 18064.58 | 14396.34 |
| 60 months | 10022.00 | 13775.22 | 16322.00 | 20075.22 | 15506.98 |

*Residential service requires eligibility and suitable permitted use; router/installation exceptions and renewal assumptions are in [internet costs](internet-costs.md). The business subscription's minimum contract remains payable if service is cancelled early.

## SG-WRX128-2 — 1 × 5995WX, 128 GB/node, 2 × 2 TB/node

Hardware **S$9312.00**; modeled moderate electricity **S$62.55/month**; separate business internet **S$105.00/month**; maintenance **S$0**. Procurement basis: Lower storage variant; indicative memory quote only. Component subtotal under local collection/free eligible delivery and fee-free payment; final mixed-seller invoicing/stock not guaranteed.

| Rental | Monthly / setup S$ | Hardware | + electricity | + internet | + both |
|---|---:|---:|---:|---:|---:|
| Hetzner AX162-1 | 948.74 / 469.74 | 10 | 10 | 11 | 12 |
| Hetzner AX162-2 | 1304.14 / 647.43 | 7 | 7 | 8 | 8 |
| UHost AX162-R | 283.73 / 154.76 | 33 | 42 | 52 | 79 |
| PlusClouds / Radius AX162-S | 324.63 / 582.63 | 27 | 34 | 40 | 56 |
| PlusClouds Radius AX102-U | 168.69 / 381.33 | 53 | 85 | 141 | 7830 |
| ServerWala Helsinki 128 GB | 432.04 / 0.00 | 22 | 26 | 29 | 36 |
| ServerWala Helsinki 256 GB | 432.04 / 0.00 | 22 | 26 | 29 | 36 |
| DediJet Singapore Ryzen 9 9950X | 346.92 / 0.00 | 27 | 33 | 39 | 52 |
| IP-Projects sTR5 L G1 | 764.64 / 486.02 | 12 | 13 | 14 | 15 |
| INTROSERV DC4SC-a4 AE9455 SG | 1559.35 / 1213.17 | 6 | 6 | 6 | 6 |
| VPSShell Dedicated EPYC Max | 1797.78 / 0.00 | 6 | 6 | 6 | 6 |
| Arxan EPYC 9454P | 304.55 / 118.37 | 31 | 38 | 47 | 68 |
| UHost AX162-R plus 2 × 3.84 TB NVMe | 394.64 / 154.76 | 24 | 28 | 32 | 41 |
| 040Hosting 7-NVME24 (legacy listing) | 338.81 / 134.67 | 28 | 34 | 40 | 54 |
| DediJet Singapore, two 9950X nodes (quantity scenario) | 693.84 / 0.00 | 14 | 15 | 16 | 18 |
| PlusClouds Radius AX162-R 256 GB | 324.63 / 768.34 | 27 | 33 | 39 | 55 |

| Horizon | Hardware | + electricity | + business internet | + both | + electricity and residential internet* |
|---|---:|---:|---:|---:|---:|
| 6 months | 9312.00 | 9687.32 | 9942.00 | 10317.32 | 9835.26 |
| 12 months | 9312.00 | 10062.64 | 10572.00 | 11322.64 | 10378.52 |
| 18 months | 9312.00 | 10437.97 | 11202.00 | 12327.97 | 10921.79 |
| 24 months | 9312.00 | 10813.29 | 11832.00 | 13333.29 | 11465.05 |
| 36 months | 9312.00 | 11563.93 | 13092.00 | 15343.93 | 12575.69 |
| 48 months | 9312.00 | 12314.58 | 14352.00 | 17354.58 | 13686.34 |
| 60 months | 9312.00 | 13065.22 | 15612.00 | 19365.22 | 14796.98 |

*Residential service requires eligibility and suitable permitted use; router/installation exceptions and renewal assumptions are in [internet costs](internet-costs.md). The business subscription's minimum contract remains payable if service is cancelled early.

## SG-WRX256-2-USED — 1 × 5995WX, 256 GB/node, 2 × 2 TB/node (conditional refurbished RAM)

Hardware **S$9098.00**; modeled moderate electricity **S$62.55/month**; separate business internet **S$105.00/month**; maintenance **S$0**. Procurement basis: Sensitivity only. Eight matching .C16FE modules unconfirmed. Component subtotal under local collection/free eligible delivery and fee-free payment; final mixed-seller invoicing/stock not guaranteed.

| Rental | Monthly / setup S$ | Hardware | + electricity | + internet | + both |
|---|---:|---:|---:|---:|---:|
| Hetzner AX162-1 | 948.74 / 469.74 | 10 | 10 | 11 | 12 |
| Hetzner AX162-2 | 1304.14 / 647.43 | 7 | 7 | 8 | 8 |
| UHost AX162-R | 283.73 / 154.76 | 32 | 41 | 51 | 77 |
| PlusClouds / Radius AX162-S | 324.63 / 582.63 | 27 | 33 | 39 | 55 |
| PlusClouds Radius AX102-U | 168.69 / 381.33 | 52 | 83 | 137 | 7642 |
| ServerWala Helsinki 128 GB | 432.04 / 0.00 | 22 | 25 | 28 | 35 |
| ServerWala Helsinki 256 GB | 432.04 / 0.00 | 22 | 25 | 28 | 35 |
| DediJet Singapore Ryzen 9 9950X | 346.92 / 0.00 | 27 | 32 | 38 | 51 |
| IP-Projects sTR5 L G1 | 764.64 / 486.02 | 12 | 13 | 14 | 15 |
| INTROSERV DC4SC-a4 AE9455 SG | 1559.35 / 1213.17 | 6 | 6 | 6 | 6 |
| VPSShell Dedicated EPYC Max | 1797.78 / 0.00 | 6 | 6 | 6 | 6 |
| Arxan EPYC 9454P | 304.55 / 118.37 | 30 | 38 | 46 | 66 |
| UHost AX162-R plus 2 × 3.84 TB NVMe | 394.64 / 154.76 | 23 | 27 | 31 | 40 |
| 040Hosting 7-NVME24 (legacy listing) | 338.81 / 134.67 | 27 | 33 | 39 | 53 |
| DediJet Singapore, two 9950X nodes (quantity scenario) | 693.84 / 0.00 | 14 | 15 | 16 | 18 |
| PlusClouds Radius AX162-R 256 GB | 324.63 / 768.34 | 26 | 32 | 38 | 54 |

| Horizon | Hardware | + electricity | + business internet | + both | + electricity and residential internet* |
|---|---:|---:|---:|---:|---:|
| 6 months | 9098.00 | 9473.32 | 9728.00 | 10103.32 | 9621.26 |
| 12 months | 9098.00 | 9848.64 | 10358.00 | 11108.64 | 10164.52 |
| 18 months | 9098.00 | 10223.97 | 10988.00 | 12113.97 | 10707.79 |
| 24 months | 9098.00 | 10599.29 | 11618.00 | 13119.29 | 11251.05 |
| 36 months | 9098.00 | 11349.93 | 12878.00 | 15129.93 | 12361.69 |
| 48 months | 9098.00 | 12100.58 | 14138.00 | 17140.58 | 13472.34 |
| 60 months | 9098.00 | 12851.22 | 15398.00 | 19151.22 | 14582.98 |

*Residential service requires eligibility and suitable permitted use; router/installation exceptions and renewal assumptions are in [internet costs](internet-costs.md). The business subscription's minimum contract remains payable if service is cancelled early.

## SG-WRX256-4-USED — 1 × 5995WX, 256 GB/node, 2 × 4 TB/node (conditional refurbished RAM)

Hardware **S$9808.00**; modeled moderate electricity **S$62.55/month**; separate business internet **S$105.00/month**; maintenance **S$0**. Procurement basis: Sensitivity only. Eight matching .C16FE modules unconfirmed. Component subtotal under local collection/free eligible delivery and fee-free payment; final mixed-seller invoicing/stock not guaranteed.

| Rental | Monthly / setup S$ | Hardware | + electricity | + internet | + both |
|---|---:|---:|---:|---:|---:|
| Hetzner AX162-1 | 948.74 / 469.74 | 10 | 11 | 12 | 12 |
| Hetzner AX162-2 | 1304.14 / 647.43 | 8 | 8 | 8 | 9 |
| UHost AX162-R | 283.73 / 154.76 | 35 | 44 | 55 | 84 |
| PlusClouds / Radius AX162-S | 324.63 / 582.63 | 29 | 36 | 43 | 59 |
| PlusClouds Radius AX102-U | 168.69 / 381.33 | 56 | 89 | 148 | 8264 |
| ServerWala Helsinki 128 GB | 432.04 / 0.00 | 23 | 27 | 30 | 38 |
| ServerWala Helsinki 256 GB | 432.04 / 0.00 | 23 | 27 | 30 | 38 |
| DediJet Singapore Ryzen 9 9950X | 346.92 / 0.00 | 29 | 35 | 41 | 55 |
| IP-Projects sTR5 L G1 | 764.64 / 486.02 | 13 | 14 | 15 | 16 |
| INTROSERV DC4SC-a4 AE9455 SG | 1559.35 / 1213.17 | 6 | 6 | 6 | 7 |
| VPSShell Dedicated EPYC Max | 1797.78 / 0.00 | 6 | 6 | 6 | 7 |
| Arxan EPYC 9454P | 304.55 / 118.37 | 32 | 41 | 49 | 71 |
| UHost AX162-R plus 2 × 3.84 TB NVMe | 394.64 / 154.76 | 25 | 30 | 34 | 43 |
| 040Hosting 7-NVME24 (legacy listing) | 338.81 / 134.67 | 29 | 36 | 42 | 57 |
| DediJet Singapore, two 9950X nodes (quantity scenario) | 693.84 / 0.00 | 15 | 16 | 17 | 19 |
| PlusClouds Radius AX162-R 256 GB | 324.63 / 768.34 | 28 | 35 | 42 | 58 |

| Horizon | Hardware | + electricity | + business internet | + both | + electricity and residential internet* |
|---|---:|---:|---:|---:|---:|
| 6 months | 9808.00 | 10183.32 | 10438.00 | 10813.32 | 10331.26 |
| 12 months | 9808.00 | 10558.64 | 11068.00 | 11818.64 | 10874.52 |
| 18 months | 9808.00 | 10933.97 | 11698.00 | 12823.97 | 11417.79 |
| 24 months | 9808.00 | 11309.29 | 12328.00 | 13829.29 | 11961.05 |
| 36 months | 9808.00 | 12059.93 | 13588.00 | 15839.93 | 13071.69 |
| 48 months | 9808.00 | 12810.58 | 14848.00 | 17850.58 | 14182.34 |
| 60 months | 9808.00 | 13561.22 | 16108.00 | 19861.22 | 15292.98 |

*Residential service requires eligibility and suitable permitted use; router/installation exceptions and renewal assumptions are in [internet costs](internet-costs.md). The business subscription's minimum contract remains payable if service is cancelled early.

## SG-INTEL128-2 — 1 × 270K Plus, 128 GB/node, 2 × 2 TB/node

Hardware **S$4757.00**; modeled moderate electricity **S$52.32/month**; separate business internet **S$105.00/month**; maintenance **S$0**. Procurement basis: B. Single 128 GB value worker. Component subtotal under local collection/free eligible delivery and fee-free payment; final mixed-seller invoicing/stock not guaranteed.

| Rental | Monthly / setup S$ | Hardware | + electricity | + internet | + both |
|---|---:|---:|---:|---:|---:|
| Hetzner AX162-1 | 948.74 / 469.74 | 5 | 5 | 6 | 6 |
| Hetzner AX162-2 | 1304.14 / 647.43 | 4 | 4 | 4 | 4 |
| UHost AX162-R | 283.73 / 154.76 | 17 | 20 | 26 | 37 |
| PlusClouds / Radius AX162-S | 324.63 / 582.63 | 13 | 16 | 20 | 25 |
| PlusClouds Radius AX102-U | 168.69 / 381.33 | 26 | 38 | 69 | 385 |
| ServerWala Helsinki 128 GB | 432.04 / 0.00 | 12 | 13 | 15 | 18 |
| ServerWala Helsinki 256 GB | 432.04 / 0.00 | 12 | 13 | 15 | 18 |
| DediJet Singapore Ryzen 9 9950X | 346.92 / 0.00 | 14 | 17 | 20 | 26 |
| IP-Projects sTR5 L G1 | 764.64 / 486.02 | 6 | 6 | 7 | 8 |
| INTROSERV DC4SC-a4 AE9455 SG | 1559.35 / 1213.17 | 3 | 3 | 3 | 3 |
| VPSShell Dedicated EPYC Max | 1797.78 / 0.00 | 3 | 3 | 3 | 3 |
| Arxan EPYC 9454P | 304.55 / 118.37 | 16 | 19 | 24 | 32 |
| UHost AX162-R plus 2 × 3.84 TB NVMe | 394.64 / 154.76 | 12 | 14 | 16 | 20 |
| 040Hosting 7-NVME24 (legacy listing) | 338.81 / 134.67 | 14 | 17 | 20 | 26 |
| DediJet Singapore, two 9950X nodes (quantity scenario) | 693.84 / 0.00 | 7 | 8 | 9 | 9 |
| PlusClouds Radius AX162-R 256 GB | 324.63 / 768.34 | 13 | 15 | 19 | 24 |

| Horizon | Hardware | + electricity | + business internet | + both | + electricity and residential internet* |
|---|---:|---:|---:|---:|---:|
| 6 months | 4757.00 | 5070.91 | 5387.00 | 5700.91 | 5218.85 |
| 12 months | 4757.00 | 5384.81 | 6017.00 | 6644.81 | 5700.69 |
| 18 months | 4757.00 | 5698.72 | 6647.00 | 7588.72 | 6182.54 |
| 24 months | 4757.00 | 6012.62 | 7277.00 | 8532.62 | 6664.38 |
| 36 months | 4757.00 | 6640.44 | 8537.00 | 10420.44 | 7652.20 |
| 48 months | 4757.00 | 7268.25 | 9797.00 | 12308.25 | 8640.01 |
| 60 months | 4757.00 | 7896.06 | 11057.00 | 14196.06 | 9627.82 |

*Residential service requires eligibility and suitable permitted use; router/installation exceptions and renewal assumptions are in [internet costs](internet-costs.md). The business subscription's minimum contract remains payable if service is cancelled early.

## SG-INTEL128-4 — 1 × 270K Plus, 128 GB/node, 2 × 4 TB/node

Hardware **S$5467.00**; modeled moderate electricity **S$52.32/month**; separate business internet **S$105.00/month**; maintenance **S$0**. Procurement basis: Lower-cost DDR5 128 GB / 4 TB mirrored option. Component subtotal under local collection/free eligible delivery and fee-free payment; final mixed-seller invoicing/stock not guaranteed.

| Rental | Monthly / setup S$ | Hardware | + electricity | + internet | + both |
|---|---:|---:|---:|---:|---:|
| Hetzner AX162-1 | 948.74 / 469.74 | 6 | 6 | 6 | 7 |
| Hetzner AX162-2 | 1304.14 / 647.43 | 4 | 4 | 5 | 5 |
| UHost AX162-R | 283.73 / 154.76 | 19 | 23 | 30 | 43 |
| PlusClouds / Radius AX162-S | 324.63 / 582.63 | 16 | 18 | 23 | 30 |
| PlusClouds Radius AX102-U | 168.69 / 381.33 | 31 | 44 | 80 | 448 |
| ServerWala Helsinki 128 GB | 432.04 / 0.00 | 13 | 15 | 17 | 20 |
| ServerWala Helsinki 256 GB | 432.04 / 0.00 | 13 | 15 | 17 | 20 |
| DediJet Singapore Ryzen 9 9950X | 346.92 / 0.00 | 16 | 19 | 23 | 29 |
| IP-Projects sTR5 L G1 | 764.64 / 486.02 | 7 | 7 | 8 | 9 |
| INTROSERV DC4SC-a4 AE9455 SG | 1559.35 / 1213.17 | 3 | 3 | 3 | 4 |
| VPSShell Dedicated EPYC Max | 1797.78 / 0.00 | 4 | 4 | 4 | 4 |
| Arxan EPYC 9454P | 304.55 / 118.37 | 18 | 22 | 27 | 37 |
| UHost AX162-R plus 2 × 3.84 TB NVMe | 394.64 / 154.76 | 14 | 16 | 19 | 23 |
| 040Hosting 7-NVME24 (legacy listing) | 338.81 / 134.67 | 16 | 19 | 23 | 30 |
| DediJet Singapore, two 9950X nodes (quantity scenario) | 693.84 / 0.00 | 8 | 9 | 10 | 11 |
| PlusClouds Radius AX162-R 256 GB | 324.63 / 768.34 | 15 | 18 | 22 | 29 |

| Horizon | Hardware | + electricity | + business internet | + both | + electricity and residential internet* |
|---|---:|---:|---:|---:|---:|
| 6 months | 5467.00 | 5780.91 | 6097.00 | 6410.91 | 5928.85 |
| 12 months | 5467.00 | 6094.81 | 6727.00 | 7354.81 | 6410.69 |
| 18 months | 5467.00 | 6408.72 | 7357.00 | 8298.72 | 6892.54 |
| 24 months | 5467.00 | 6722.62 | 7987.00 | 9242.62 | 7374.38 |
| 36 months | 5467.00 | 7350.44 | 9247.00 | 11130.44 | 8362.20 |
| 48 months | 5467.00 | 7978.25 | 10507.00 | 13018.25 | 9350.01 |
| 60 months | 5467.00 | 8606.06 | 11767.00 | 14906.06 | 10337.82 |

*Residential service requires eligibility and suitable permitted use; router/installation exceptions and renewal assumptions are in [internet costs](internet-costs.md). The business subscription's minimum contract remains payable if service is cancelled early.

## SG-INTEL2X128-2 — 2 × 270K Plus, 128 GB/node, 2 × 2 TB/node

Hardware **S$9514.00**; modeled moderate electricity **S$104.64/month**; separate business internet **S$105.00/month**; maintenance **S$0**. Procurement basis: Separate 128 GB per worker; no shared memory or mirror. Component subtotal under local collection/free eligible delivery and fee-free payment; final mixed-seller invoicing/stock not guaranteed.

| Rental | Monthly / setup S$ | Hardware | + electricity | + internet | + both |
|---|---:|---:|---:|---:|---:|
| Hetzner AX162-1 | 948.74 / 469.74 | 10 | 11 | 11 | 13 |
| Hetzner AX162-2 | 1304.14 / 647.43 | 7 | 8 | 8 | 9 |
| UHost AX162-R | 283.73 / 154.76 | 33 | 53 | 53 | 127 |
| PlusClouds / Radius AX162-S | 324.63 / 582.63 | 28 | 41 | 41 | 78 |
| PlusClouds Radius AX102-U | 168.69 / 381.33 | 55 | 143 | 144 | Never |
| ServerWala Helsinki 128 GB | 432.04 / 0.00 | 23 | 30 | 30 | 43 |
| ServerWala Helsinki 256 GB | 432.04 / 0.00 | 23 | 30 | 30 | 43 |
| DediJet Singapore Ryzen 9 9950X | 346.92 / 0.00 | 28 | 40 | 40 | 70 |
| IP-Projects sTR5 L G1 | 764.64 / 486.02 | 12 | 14 | 14 | 17 |
| INTROSERV DC4SC-a4 AE9455 SG | 1559.35 / 1213.17 | 6 | 6 | 6 | 7 |
| VPSShell Dedicated EPYC Max | 1797.78 / 0.00 | 6 | 6 | 6 | 6 |
| Arxan EPYC 9454P | 304.55 / 118.37 | 31 | 47 | 48 | 99 |
| UHost AX162-R plus 2 × 3.84 TB NVMe | 394.64 / 154.76 | 24 | 33 | 33 | 51 |
| 040Hosting 7-NVME24 (legacy listing) | 338.81 / 134.67 | 28 | 41 | 41 | 73 |
| DediJet Singapore, two 9950X nodes (quantity scenario) | 693.84 / 0.00 | 14 | 17 | 17 | 20 |
| PlusClouds Radius AX162-R 256 GB | 324.63 / 768.34 | 27 | 40 | 40 | 77 |

| Horizon | Hardware | + electricity | + business internet | + both | + electricity and residential internet* |
|---|---:|---:|---:|---:|---:|
| 6 months | 9514.00 | 10141.81 | 10144.00 | 10771.81 | 10289.75 |
| 12 months | 9514.00 | 10769.62 | 10774.00 | 12029.62 | 11085.50 |
| 18 months | 9514.00 | 11397.44 | 11404.00 | 13287.44 | 11881.26 |
| 24 months | 9514.00 | 12025.25 | 12034.00 | 14545.25 | 12677.01 |
| 36 months | 9514.00 | 13280.87 | 13294.00 | 17060.87 | 14292.63 |
| 48 months | 9514.00 | 14536.49 | 14554.00 | 19576.49 | 15908.25 |
| 60 months | 9514.00 | 15792.12 | 15814.00 | 22092.12 | 17523.88 |

*Residential service requires eligibility and suitable permitted use; router/installation exceptions and renewal assumptions are in [internet costs](internet-costs.md). The business subscription's minimum contract remains payable if service is cancelled early.

## SG-RYZEN128-2 — 1 × 9950X3D, 128 GB/node, 2 × 2 TB/node

Hardware **S$5114.00**; modeled moderate electricity **S$47.77/month**; separate business internet **S$105.00/month**; maintenance **S$0**. Procurement basis: Single AM5 worker; denominator for pool price. Component subtotal under local collection/free eligible delivery and fee-free payment; final mixed-seller invoicing/stock not guaranteed.

| Rental | Monthly / setup S$ | Hardware | + electricity | + internet | + both |
|---|---:|---:|---:|---:|---:|
| Hetzner AX162-1 | 948.74 / 469.74 | 5 | 6 | 6 | 6 |
| Hetzner AX162-2 | 1304.14 / 647.43 | 4 | 4 | 4 | 4 |
| UHost AX162-R | 283.73 / 154.76 | 18 | 22 | 28 | 38 |
| PlusClouds / Radius AX162-S | 324.63 / 582.63 | 14 | 17 | 21 | 27 |
| PlusClouds Radius AX102-U | 168.69 / 381.33 | 29 | 40 | 75 | 298 |
| ServerWala Helsinki 128 GB | 432.04 / 0.00 | 12 | 14 | 16 | 19 |
| ServerWala Helsinki 256 GB | 432.04 / 0.00 | 12 | 14 | 16 | 19 |
| DediJet Singapore Ryzen 9 9950X | 346.92 / 0.00 | 15 | 18 | 22 | 27 |
| IP-Projects sTR5 L G1 | 764.64 / 486.02 | 7 | 7 | 8 | 8 |
| INTROSERV DC4SC-a4 AE9455 SG | 1559.35 / 1213.17 | 3 | 3 | 3 | 3 |
| VPSShell Dedicated EPYC Max | 1797.78 / 0.00 | 3 | 3 | 4 | 4 |
| Arxan EPYC 9454P | 304.55 / 118.37 | 17 | 20 | 26 | 33 |
| UHost AX162-R plus 2 × 3.84 TB NVMe | 394.64 / 154.76 | 13 | 15 | 18 | 21 |
| 040Hosting 7-NVME24 (legacy listing) | 338.81 / 134.67 | 15 | 18 | 22 | 27 |
| DediJet Singapore, two 9950X nodes (quantity scenario) | 693.84 / 0.00 | 8 | 8 | 9 | 10 |
| PlusClouds Radius AX162-R 256 GB | 324.63 / 768.34 | 14 | 16 | 20 | 26 |

| Horizon | Hardware | + electricity | + business internet | + both | + electricity and residential internet* |
|---|---:|---:|---:|---:|---:|
| 6 months | 5114.00 | 5400.61 | 5744.00 | 6030.61 | 5548.55 |
| 12 months | 5114.00 | 5687.22 | 6374.00 | 6947.22 | 6003.10 |
| 18 months | 5114.00 | 5973.83 | 7004.00 | 7863.83 | 6457.65 |
| 24 months | 5114.00 | 6260.44 | 7634.00 | 8780.44 | 6912.20 |
| 36 months | 5114.00 | 6833.66 | 8894.00 | 10613.66 | 7845.42 |
| 48 months | 5114.00 | 7406.88 | 10154.00 | 12446.88 | 8778.64 |
| 60 months | 5114.00 | 7980.10 | 11414.00 | 14280.10 | 9711.86 |

*Residential service requires eligibility and suitable permitted use; router/installation exceptions and renewal assumptions are in [internet costs](internet-costs.md). The business subscription's minimum contract remains payable if service is cancelled early.

## SG-RYZEN2X128-2 — 2 × 9950X3D, 128 GB/node, 2 × 2 TB/node

Hardware **S$10228.00**; modeled moderate electricity **S$95.54/month**; separate business internet **S$105.00/month**; maintenance **S$0**. Procurement basis: C. Potential higher busy-queue throughput for independent jobs. Component subtotal under local collection/free eligible delivery and fee-free payment; final mixed-seller invoicing/stock not guaranteed.

| Rental | Monthly / setup S$ | Hardware | + electricity | + internet | + both |
|---|---:|---:|---:|---:|---:|
| Hetzner AX162-1 | 948.74 / 469.74 | 11 | 12 | 12 | 14 |
| Hetzner AX162-2 | 1304.14 / 647.43 | 8 | 8 | 8 | 9 |
| UHost AX162-R | 283.73 / 154.76 | 36 | 54 | 57 | 122 |
| PlusClouds / Radius AX162-S | 324.63 / 582.63 | 30 | 43 | 44 | 78 |
| PlusClouds Radius AX102-U | 168.69 / 381.33 | 59 | 135 | 155 | Never |
| ServerWala Helsinki 128 GB | 432.04 / 0.00 | 24 | 31 | 32 | 45 |
| ServerWala Helsinki 256 GB | 432.04 / 0.00 | 24 | 31 | 32 | 45 |
| DediJet Singapore Ryzen 9 9950X | 346.92 / 0.00 | 30 | 41 | 43 | 70 |
| IP-Projects sTR5 L G1 | 764.64 / 486.02 | 13 | 15 | 15 | 18 |
| INTROSERV DC4SC-a4 AE9455 SG | 1559.35 / 1213.17 | 6 | 7 | 7 | 7 |
| VPSShell Dedicated EPYC Max | 1797.78 / 0.00 | 6 | 7 | 7 | 7 |
| Arxan EPYC 9454P | 304.55 / 118.37 | 34 | 49 | 51 | 98 |
| UHost AX162-R plus 2 × 3.84 TB NVMe | 394.64 / 154.76 | 26 | 34 | 35 | 52 |
| 040Hosting 7-NVME24 (legacy listing) | 338.81 / 134.67 | 30 | 42 | 44 | 73 |
| DediJet Singapore, two 9950X nodes (quantity scenario) | 693.84 / 0.00 | 15 | 18 | 18 | 21 |
| PlusClouds Radius AX162-R 256 GB | 324.63 / 768.34 | 30 | 42 | 44 | 77 |

| Horizon | Hardware | + electricity | + business internet | + both | + electricity and residential internet* |
|---|---:|---:|---:|---:|---:|
| 6 months | 10228.00 | 10801.22 | 10858.00 | 11431.22 | 10949.16 |
| 12 months | 10228.00 | 11374.44 | 11488.00 | 12634.44 | 11690.32 |
| 18 months | 10228.00 | 11947.66 | 12118.00 | 13837.66 | 12431.48 |
| 24 months | 10228.00 | 12520.88 | 12748.00 | 15040.88 | 13172.64 |
| 36 months | 10228.00 | 13667.32 | 14008.00 | 17447.32 | 14679.08 |
| 48 months | 10228.00 | 14813.75 | 15268.00 | 19853.75 | 16185.51 |
| 60 months | 10228.00 | 15960.19 | 16528.00 | 22260.19 | 17691.95 |

*Residential service requires eligibility and suitable permitted use; router/installation exceptions and renewal assumptions are in [internet costs](internet-costs.md). The business subscription's minimum contract remains payable if service is cancelled early.

## MY-INTEL128-2 — 1 × 270K Plus, 128 GB/node, 2 × 2 TB/node

Hardware **S$6006.26**; modeled moderate electricity **S$29.01/month**; separate business internet **S$42.55/month**; maintenance **S$0**. Procurement basis: Malaysia-local 128 GB shared pool. Component subtotal under local collection/free eligible delivery and fee-free payment; final mixed-seller invoicing/stock not guaranteed.

| Rental | Monthly / setup S$ | Hardware | + electricity | + internet | + both |
|---|---:|---:|---:|---:|---:|
| Hetzner AX162-1 | 870.41 / 430.95 | 7 | 7 | 7 | 7 |
| Hetzner AX162-2 | 1196.45 / 593.97 | 5 | 5 | 5 | 5 |
| UHost AX162-R | 283.73 / 154.76 | 21 | 23 | 25 | 28 |
| PlusClouds / Radius AX162-S | 324.63 / 582.63 | 17 | 19 | 20 | 22 |
| PlusClouds Radius AX102-U | 168.69 / 381.33 | 34 | 41 | 45 | 58 |
| ServerWala Helsinki 128 GB | 432.04 / 0.00 | 14 | 15 | 16 | 17 |
| ServerWala Helsinki 256 GB | 432.04 / 0.00 | 14 | 15 | 16 | 17 |
| DediJet Singapore Ryzen 9 9950X | 346.92 / 0.00 | 18 | 19 | 20 | 22 |
| IP-Projects sTR5 L G1 | 764.64 / 486.02 | 8 | 8 | 8 | 8 |
| INTROSERV DC4SC-a4 AE9455 SG | 1559.35 / 1213.17 | 4 | 4 | 4 | 4 |
| VPSShell Dedicated EPYC Max | 1797.78 / 0.00 | 4 | 4 | 4 | 4 |
| Arxan EPYC 9454P | 304.55 / 118.37 | 20 | 22 | 23 | 26 |
| UHost AX162-R plus 2 × 3.84 TB NVMe | 394.64 / 154.76 | 15 | 17 | 17 | 19 |
| 040Hosting 7-NVME24 (legacy listing) | 338.81 / 134.67 | 18 | 19 | 20 | 22 |
| DediJet Singapore, two 9950X nodes (quantity scenario) | 693.84 / 0.00 | 9 | 10 | 10 | 10 |
| PlusClouds Radius AX162-R 256 GB | 324.63 / 768.34 | 17 | 18 | 19 | 21 |

| Horizon | Hardware | + electricity | + business internet | + both | + electricity and residential internet* |
|---|---:|---:|---:|---:|---:|
| 6 months | 6006.26 | 6180.30 | 6261.55 | 6435.59 | 6377.75 |
| 12 months | 6006.26 | 6354.34 | 6516.84 | 6864.92 | 6749.24 |
| 18 months | 6006.26 | 6528.38 | 6772.13 | 7294.25 | 7120.73 |
| 24 months | 6006.26 | 6702.42 | 7027.42 | 7723.58 | 7492.22 |
| 36 months | 6006.26 | 7050.50 | 7538.00 | 8582.24 | 8235.20 |
| 48 months | 6006.26 | 7398.58 | 8048.58 | 9440.90 | 8978.19 |
| 60 months | 6006.26 | 7746.66 | 8559.16 | 10299.56 | 9721.17 |

*Residential service requires eligibility and suitable permitted use; router/installation exceptions and renewal assumptions are in [internet costs](internet-costs.md). The business subscription's minimum contract remains payable if service is cancelled early.

## MY-INTEL256-2 — 1 × 270K Plus, 256 GB/node, 2 × 2 TB/node

Hardware **S$10101.16**; modeled moderate electricity **S$29.01/month**; separate business internet **S$42.55/month**; maintenance **S$0**. Procurement basis: Malaysia-local 256 GB 4 x 64 GB JEDEC DDR5; two channels, 4400 MT/s controller rating at 2DPC/2R. Component subtotal under local collection/free eligible delivery and fee-free payment; final mixed-seller invoicing/stock not guaranteed.

| Rental | Monthly / setup S$ | Hardware | + electricity | + internet | + both |
|---|---:|---:|---:|---:|---:|
| Hetzner AX162-1 | 870.41 / 430.95 | 12 | 12 | 12 | 13 |
| Hetzner AX162-2 | 1196.45 / 593.97 | 8 | 9 | 9 | 9 |
| UHost AX162-R | 283.73 / 154.76 | 36 | 40 | 42 | 47 |
| PlusClouds / Radius AX162-S | 324.63 / 582.63 | 30 | 33 | 34 | 38 |
| PlusClouds Radius AX102-U | 168.69 / 381.33 | 58 | 70 | 78 | 101 |
| ServerWala Helsinki 128 GB | 432.04 / 0.00 | 24 | 26 | 26 | 29 |
| ServerWala Helsinki 256 GB | 432.04 / 0.00 | 24 | 26 | 26 | 29 |
| DediJet Singapore Ryzen 9 9950X | 346.92 / 0.00 | 30 | 32 | 34 | 37 |
| IP-Projects sTR5 L G1 | 764.64 / 486.02 | 13 | 14 | 14 | 14 |
| INTROSERV DC4SC-a4 AE9455 SG | 1559.35 / 1213.17 | 6 | 6 | 6 | 6 |
| VPSShell Dedicated EPYC Max | 1797.78 / 0.00 | 6 | 6 | 6 | 6 |
| Arxan EPYC 9454P | 304.55 / 118.37 | 33 | 37 | 39 | 43 |
| UHost AX162-R plus 2 × 3.84 TB NVMe | 394.64 / 154.76 | 26 | 28 | 29 | 31 |
| 040Hosting 7-NVME24 (legacy listing) | 338.81 / 134.67 | 30 | 33 | 34 | 38 |
| DediJet Singapore, two 9950X nodes (quantity scenario) | 693.84 / 0.00 | 15 | 16 | 16 | 17 |
| PlusClouds Radius AX162-R 256 GB | 324.63 / 768.34 | 29 | 32 | 34 | 37 |

| Horizon | Hardware | + electricity | + business internet | + both | + electricity and residential internet* |
|---|---:|---:|---:|---:|---:|
| 6 months | 10101.16 | 10275.20 | 10356.45 | 10530.49 | 10472.66 |
| 12 months | 10101.16 | 10449.24 | 10611.74 | 10959.82 | 10844.15 |
| 18 months | 10101.16 | 10623.28 | 10867.04 | 11389.16 | 11215.64 |
| 24 months | 10101.16 | 10797.32 | 11122.33 | 11818.49 | 11587.13 |
| 36 months | 10101.16 | 11145.40 | 11632.91 | 12677.15 | 12330.11 |
| 48 months | 10101.16 | 11493.48 | 12143.49 | 13535.81 | 13073.09 |
| 60 months | 10101.16 | 11841.56 | 12654.07 | 14394.47 | 13816.07 |

*Residential service requires eligibility and suitable permitted use; router/installation exceptions and renewal assumptions are in [internet costs](internet-costs.md). The business subscription's minimum contract remains payable if service is cancelled early.

## MY-RYZEN128-2 — 1 × 9950X3D, 128 GB/node, 2 × 2 TB/node

Hardware **S$6539.37**; modeled moderate electricity **S$26.48/month**; separate business internet **S$42.55/month**; maintenance **S$0**. Procurement basis: Malaysia-local 128 GB AM5 worker. Component subtotal under local collection/free eligible delivery and fee-free payment; final mixed-seller invoicing/stock not guaranteed.

| Rental | Monthly / setup S$ | Hardware | + electricity | + internet | + both |
|---|---:|---:|---:|---:|---:|
| Hetzner AX162-1 | 870.41 / 430.95 | 8 | 8 | 8 | 8 |
| Hetzner AX162-2 | 1196.45 / 593.97 | 5 | 6 | 6 | 6 |
| UHost AX162-R | 283.73 / 154.76 | 23 | 25 | 27 | 30 |
| PlusClouds / Radius AX162-S | 324.63 / 582.63 | 19 | 20 | 22 | 24 |
| PlusClouds Radius AX102-U | 168.69 / 381.33 | 37 | 44 | 49 | 62 |
| ServerWala Helsinki 128 GB | 432.04 / 0.00 | 16 | 17 | 17 | 19 |
| ServerWala Helsinki 256 GB | 432.04 / 0.00 | 16 | 17 | 17 | 19 |
| DediJet Singapore Ryzen 9 9950X | 346.92 / 0.00 | 19 | 21 | 22 | 24 |
| IP-Projects sTR5 L G1 | 764.64 / 486.02 | 8 | 9 | 9 | 9 |
| INTROSERV DC4SC-a4 AE9455 SG | 1559.35 / 1213.17 | 4 | 4 | 4 | 4 |
| VPSShell Dedicated EPYC Max | 1797.78 / 0.00 | 4 | 4 | 4 | 4 |
| Arxan EPYC 9454P | 304.55 / 118.37 | 22 | 24 | 25 | 28 |
| UHost AX162-R plus 2 × 3.84 TB NVMe | 394.64 / 154.76 | 17 | 18 | 19 | 20 |
| 040Hosting 7-NVME24 (legacy listing) | 338.81 / 134.67 | 19 | 21 | 22 | 24 |
| DediJet Singapore, two 9950X nodes (quantity scenario) | 693.84 / 0.00 | 10 | 10 | 11 | 11 |
| PlusClouds Radius AX162-R 256 GB | 324.63 / 768.34 | 18 | 20 | 21 | 23 |

| Horizon | Hardware | + electricity | + business internet | + both | + electricity and residential internet* |
|---|---:|---:|---:|---:|---:|
| 6 months | 6539.37 | 6698.27 | 6794.66 | 6953.56 | 6895.73 |
| 12 months | 6539.37 | 6857.18 | 7049.95 | 7367.76 | 7252.08 |
| 18 months | 6539.37 | 7016.09 | 7305.24 | 7781.96 | 7608.44 |
| 24 months | 6539.37 | 7174.99 | 7560.53 | 8196.15 | 7964.80 |
| 36 months | 6539.37 | 7492.80 | 8071.11 | 9024.55 | 8677.51 |
| 48 months | 6539.37 | 7810.62 | 8581.69 | 9852.94 | 9390.22 |
| 60 months | 6539.37 | 8128.43 | 9092.27 | 10681.33 | 10102.94 |

*Residential service requires eligibility and suitable permitted use; router/installation exceptions and renewal assumptions are in [internet costs](internet-costs.md). The business subscription's minimum contract remains payable if service is cancelled early.

## MY-RYZEN2X128-2 — 2 × 9950X3D, 128 GB/node, 2 × 2 TB/node

Hardware **S$13078.74**; modeled moderate electricity **S$52.97/month**; separate business internet **S$42.55/month**; maintenance **S$0**. Procurement basis: Two independent 128 GB workers; totals cover all four SSDs. Component subtotal under local collection/free eligible delivery and fee-free payment; final mixed-seller invoicing/stock not guaranteed.

| Rental | Monthly / setup S$ | Hardware | + electricity | + internet | + both |
|---|---:|---:|---:|---:|---:|
| Hetzner AX162-1 | 870.41 / 430.95 | 15 | 16 | 16 | 17 |
| Hetzner AX162-2 | 1196.45 / 593.97 | 11 | 11 | 11 | 12 |
| UHost AX162-R | 283.73 / 154.76 | 46 | 57 | 54 | 69 |
| PlusClouds / Radius AX162-S | 324.63 / 582.63 | 39 | 46 | 45 | 55 |
| PlusClouds Radius AX102-U | 168.69 / 381.33 | 76 | 110 | 101 | 174 |
| ServerWala Helsinki 128 GB | 432.04 / 0.00 | 31 | 35 | 34 | 39 |
| ServerWala Helsinki 256 GB | 432.04 / 0.00 | 31 | 35 | 34 | 39 |
| DediJet Singapore Ryzen 9 9950X | 346.92 / 0.00 | 38 | 45 | 43 | 53 |
| IP-Projects sTR5 L G1 | 764.64 / 486.02 | 17 | 18 | 18 | 19 |
| INTROSERV DC4SC-a4 AE9455 SG | 1559.35 / 1213.17 | 8 | 8 | 8 | 9 |
| VPSShell Dedicated EPYC Max | 1797.78 / 0.00 | 8 | 8 | 8 | 8 |
| Arxan EPYC 9454P | 304.55 / 118.37 | 43 | 52 | 50 | 63 |
| UHost AX162-R plus 2 × 3.84 TB NVMe | 394.64 / 154.76 | 33 | 38 | 37 | 44 |
| 040Hosting 7-NVME24 (legacy listing) | 338.81 / 134.67 | 39 | 46 | 44 | 54 |
| DediJet Singapore, two 9950X nodes (quantity scenario) | 693.84 / 0.00 | 19 | 21 | 21 | 22 |
| PlusClouds Radius AX162-R 256 GB | 324.63 / 768.34 | 38 | 46 | 44 | 54 |

| Horizon | Hardware | + electricity | + business internet | + both | + electricity and residential internet* |
|---|---:|---:|---:|---:|---:|
| 6 months | 13078.74 | 13396.55 | 13334.03 | 13651.84 | 13594.00 |
| 12 months | 13078.74 | 13714.36 | 13589.32 | 14224.94 | 14109.26 |
| 18 months | 13078.74 | 14032.17 | 13844.61 | 14798.04 | 14624.53 |
| 24 months | 13078.74 | 14349.98 | 14099.90 | 15371.15 | 15139.79 |
| 36 months | 13078.74 | 14985.61 | 14610.48 | 16517.35 | 16170.31 |
| 48 months | 13078.74 | 15621.23 | 15121.06 | 17663.55 | 17200.84 |
| 60 months | 13078.74 | 16256.86 | 15631.64 | 18809.76 | 18231.37 |

*Residential service requires eligibility and suitable permitted use; router/installation exceptions and renewal assumptions are in [internet costs](internet-costs.md). The business subscription's minimum contract remains payable if service is cancelled early.

## SG-RYZENX3D2-128-2 — 1 × 9950X3D2, 128 GB/node, 2 × 2 TB/node

Hardware **S$5644.00**; modeled moderate electricity **S$51.18/month**; separate business internet **S$105.00/month**; maintenance **S$0**. Procurement basis: Single performance-first desktop alternative, higher 200 W CPU thermal design. Component subtotal; local fee-free payment/collection assumptions; final invoices and physical stock unverified.

| Rental | Monthly / setup S$ | Hardware | + electricity | + internet | + both |
|---|---:|---:|---:|---:|---:|
| Hetzner AX162-1 | 948.74 / 469.74 | 6 | 6 | 7 | 7 |
| Hetzner AX162-2 | 1304.14 / 647.43 | 4 | 4 | 5 | 5 |
| UHost AX162-R | 283.73 / 154.76 | 20 | 24 | 31 | 44 |
| PlusClouds / Radius AX162-S | 324.63 / 582.63 | 16 | 19 | 24 | 31 |
| PlusClouds Radius AX102-U | 168.69 / 381.33 | 32 | 45 | 83 | 421 |
| ServerWala Helsinki 128 GB | 432.04 / 0.00 | 14 | 15 | 18 | 21 |
| ServerWala Helsinki 256 GB | 432.04 / 0.00 | 14 | 15 | 18 | 21 |
| DediJet Singapore Ryzen 9 9950X | 346.92 / 0.00 | 17 | 20 | 24 | 30 |
| IP-Projects sTR5 L G1 | 764.64 / 486.02 | 7 | 8 | 8 | 9 |
| INTROSERV DC4SC-a4 AE9455 SG | 1559.35 / 1213.17 | 3 | 3 | 4 | 4 |
| VPSShell Dedicated EPYC Max | 1797.78 / 0.00 | 4 | 4 | 4 | 4 |
| Arxan EPYC 9454P | 304.55 / 118.37 | 19 | 22 | 28 | 38 |
| UHost AX162-R plus 2 × 3.84 TB NVMe | 394.64 / 154.76 | 14 | 16 | 19 | 24 |
| 040Hosting 7-NVME24 (legacy listing) | 338.81 / 134.67 | 17 | 20 | 24 | 31 |
| DediJet Singapore, two 9950X nodes (quantity scenario) | 693.84 / 0.00 | 9 | 9 | 10 | 11 |
| PlusClouds Radius AX162-R 256 GB | 324.63 / 768.34 | 16 | 18 | 23 | 29 |

| Horizon | Hardware | + electricity | + business internet | + both | + electricity and residential internet* |
|---|---:|---:|---:|---:|---:|
| 6 months | 5644.00 | 5951.08 | 6274.00 | 6581.08 | 6099.02 |
| 12 months | 5644.00 | 6258.16 | 6904.00 | 7518.16 | 6574.04 |
| 18 months | 5644.00 | 6565.25 | 7534.00 | 8455.25 | 7049.07 |
| 24 months | 5644.00 | 6872.33 | 8164.00 | 9392.33 | 7524.09 |
| 36 months | 5644.00 | 7486.49 | 9424.00 | 11266.49 | 8498.25 |
| 48 months | 5644.00 | 8100.65 | 10684.00 | 13140.65 | 9472.41 |
| 60 months | 5644.00 | 8714.82 | 11944.00 | 15014.82 | 10446.58 |

*Residential service requires eligibility and suitable permitted use; router/installation exceptions and renewal assumptions are in [internet costs](internet-costs.md). The business subscription's minimum contract remains payable if service is cancelled early.

## MY-RYZENX3D2-128-2 — 1 × 9950X3D2, 128 GB/node, 2 × 2 TB/node

Hardware **S$6793.38**; modeled moderate electricity **S$28.38/month**; separate business internet **S$42.55/month**; maintenance **S$0**. Procurement basis: Regional single-node performance per ringgit alternative, 200 W CPU with dual-tower air cooling; sustained thermal behavior unknown. Component subtotal; local fee-free payment/collection assumptions; final invoices and physical stock unverified.

| Rental | Monthly / setup S$ | Hardware | + electricity | + internet | + both |
|---|---:|---:|---:|---:|---:|
| Hetzner AX162-1 | 870.41 / 430.95 | 8 | 8 | 8 | 8 |
| Hetzner AX162-2 | 1196.45 / 593.97 | 6 | 6 | 6 | 6 |
| UHost AX162-R | 283.73 / 154.76 | 24 | 26 | 28 | 32 |
| PlusClouds / Radius AX162-S | 324.63 / 582.63 | 20 | 21 | 23 | 25 |
| PlusClouds Radius AX102-U | 168.69 / 381.33 | 39 | 46 | 51 | 66 |
| ServerWala Helsinki 128 GB | 432.04 / 0.00 | 16 | 17 | 18 | 19 |
| ServerWala Helsinki 256 GB | 432.04 / 0.00 | 16 | 17 | 18 | 19 |
| DediJet Singapore Ryzen 9 9950X | 346.92 / 0.00 | 20 | 22 | 23 | 25 |
| IP-Projects sTR5 L G1 | 764.64 / 486.02 | 9 | 9 | 9 | 10 |
| INTROSERV DC4SC-a4 AE9455 SG | 1559.35 / 1213.17 | 4 | 4 | 4 | 4 |
| VPSShell Dedicated EPYC Max | 1797.78 / 0.00 | 4 | 4 | 4 | 4 |
| Arxan EPYC 9454P | 304.55 / 118.37 | 22 | 25 | 26 | 29 |
| UHost AX162-R plus 2 × 3.84 TB NVMe | 394.64 / 154.76 | 17 | 19 | 19 | 21 |
| 040Hosting 7-NVME24 (legacy listing) | 338.81 / 134.67 | 20 | 22 | 23 | 25 |
| DediJet Singapore, two 9950X nodes (quantity scenario) | 693.84 / 0.00 | 10 | 11 | 11 | 11 |
| PlusClouds Radius AX162-R 256 GB | 324.63 / 768.34 | 19 | 21 | 22 | 24 |

| Horizon | Hardware | + electricity | + business internet | + both | + electricity and residential internet* |
|---|---:|---:|---:|---:|---:|
| 6 months | 6793.38 | 6963.64 | 7048.67 | 7218.93 | 7161.09 |
| 12 months | 6793.38 | 7133.89 | 7303.96 | 7644.47 | 7528.79 |
| 18 months | 6793.38 | 7304.15 | 7559.25 | 8070.02 | 7896.50 |
| 24 months | 6793.38 | 7474.40 | 7814.54 | 8495.57 | 8264.21 |
| 36 months | 6793.38 | 7814.92 | 8325.12 | 9346.66 | 8999.62 |
| 48 months | 6793.38 | 8155.43 | 8835.70 | 10197.75 | 9735.04 |
| 60 months | 6793.38 | 8495.94 | 9346.28 | 11048.85 | 10470.45 |

*Residential service requires eligibility and suitable permitted use; router/installation exceptions and renewal assumptions are in [internet costs](internet-costs.md). The business subscription's minimum contract remains payable if service is cancelled early.

## MY-INTEL128-4 — 1 × 270K Plus, 128 GB, 2 × WD SN850X 4 TB with factory heatsinks

Hardware **S$7324.61**; modeled moderate electricity **S$29.01/month**; separate business internet **S$42.55/month**; maintenance **S$0**. Procurement basis: Malaysia-local AX162-1 storage-capacity alternative. Two SN850X factory heatsinks, omit motherboard M.2 covers, no GPU. Sticker-price subtotal; any bank-transfer promotion is excluded until final exact discount is confirmed. Local collection/eligible delivery, not a cross-border landed quote.

| Rental | Monthly / setup S$ | Hardware | + electricity | + internet | + both |
|---|---:|---:|---:|---:|---:|
| Hetzner AX162-1 | 870.41 / 430.95 | 8 | 9 | 9 | 9 |
| Hetzner AX162-2 | 1196.45 / 593.97 | 6 | 6 | 6 | 6 |
| UHost AX162-R | 283.73 / 154.76 | 26 | 29 | 30 | 34 |
| PlusClouds / Radius AX162-S | 324.63 / 582.63 | 21 | 23 | 24 | 27 |
| PlusClouds Radius AX102-U | 168.69 / 381.33 | 42 | 50 | 56 | 72 |
| ServerWala Helsinki 128 GB | 432.04 / 0.00 | 17 | 19 | 19 | 21 |
| ServerWala Helsinki 256 GB | 432.04 / 0.00 | 17 | 19 | 19 | 21 |
| DediJet Singapore Ryzen 9 9950X | 346.92 / 0.00 | 22 | 24 | 25 | 27 |
| IP-Projects sTR5 L G1 | 764.64 / 486.02 | 9 | 10 | 10 | 10 |
| INTROSERV DC4SC-a4 AE9455 SG | 1559.35 / 1213.17 | 4 | 4 | 5 | 5 |
| VPSShell Dedicated EPYC Max | 1797.78 / 0.00 | 5 | 5 | 5 | 5 |
| Arxan EPYC 9454P | 304.55 / 118.37 | 24 | 27 | 28 | 31 |
| UHost AX162-R plus 2 × 3.84 TB NVMe | 394.64 / 154.76 | 19 | 20 | 21 | 23 |
| 040Hosting 7-NVME24 (legacy listing) | 338.81 / 134.67 | 22 | 24 | 25 | 27 |
| DediJet Singapore, two 9950X nodes (quantity scenario) | 693.84 / 0.00 | 11 | 12 | 12 | 12 |
| PlusClouds Radius AX162-R 256 GB | 324.63 / 768.34 | 21 | 23 | 24 | 26 |

| Horizon | Hardware | + electricity | + business internet | + both | + electricity and residential internet* |
|---|---:|---:|---:|---:|---:|
| 6 months | 7324.61 | 7498.65 | 7579.90 | 7753.94 | 7696.10 |
| 12 months | 7324.61 | 7672.69 | 7835.19 | 8183.27 | 8067.59 |
| 18 months | 7324.61 | 7846.73 | 8090.48 | 8612.60 | 8439.08 |
| 24 months | 7324.61 | 8020.77 | 8345.77 | 9041.93 | 8810.57 |
| 36 months | 7324.61 | 8368.85 | 8856.35 | 9900.59 | 9553.55 |
| 48 months | 7324.61 | 8716.93 | 9366.93 | 10759.25 | 10296.53 |
| 60 months | 7324.61 | 9065.01 | 9877.51 | 11617.91 | 11039.52 |

*Residential service requires eligibility and suitable permitted use; router/installation exceptions and renewal assumptions are in [internet costs](internet-costs.md). The business subscription's minimum contract remains payable if service is cancelled early.

## Machine-readable outputs

- [Every build, monthly rental, scenario and horizon](data/break-even.csv)
- [Cumulative cash-cost rows](data/cumulative-costs.csv)
- [Named compiler-proxy value, not a CI score](data/performance-value.csv)
- [Same-CPU rental proxy value](data/rental-performance-value.csv)
- [Sensitivity scenarios](data/sensitivity.csv)
- [Annual prepayment versus service-equivalent expense](data/prepaid-rentals.csv)

Signed-off-by: Alexey Zhokhov
