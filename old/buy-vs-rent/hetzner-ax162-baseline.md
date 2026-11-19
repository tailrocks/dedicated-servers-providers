# The Hetzner reference for CI

[Study overview](README.md) · [Rental comparisons](rental-market-update.md) · [Market inputs](data/market-inputs.json)

**Checked 20 November 2026, Asia/Ho_Chi_Minh.** The regular AX162-1 is the 128 GB, larger-disk reference. AX162-2 buys twice the RAM but has half the nominal mirrored storage. Both use a single EPYC 9454P. The monthly quotes are for a new bare-metal order in Falkenstein, Germany or Helsinki, Finland.

## What a job can actually use

| Feature | AX162-1 | AX162-2 |
|---|---|---|
| Processor | AMD EPYC 9454P, 48 Zen 4 cores and 96 threads with SMT, one socket | Same |
| Memory | 128 GB registered DDR5 ECC | 256 GB registered DDR5 ECC |
| Local drives | 2 × 3.84 TB Gen4 datacenter NVMe | 2 × 1.92 TB Gen4 datacenter NVMe |
| Raw installed / nominal RAID 1 | 7.68 TB / **3.84 TB** (about 3.49 TiB) | 3.84 TB / **1.92 TB** (about 1.75 TiB) |
| Network and access | 1 Gbps port, 1 Gbps guaranteed, unlimited traffic on the standard connection, /64 IPv6, root access and remote reset | Same |
| Locations offered | FSN1 and HEL1 | FSN1 and HEL1 |

RAID 1 leaves the capacity of one drive before partitioning, filesystem overhead, OS and build caches. Quoted decimal TB and binary TiB refer to the same bytes. The default uplink, IPv6, and provider-side power are included in the server charge. The optional 10 Gbps uplink changes the traffic allowance. [Hetzner hardware table](https://docs.hetzner.com/robot/dedicated-server/server-lines/ax-server/) · [AX162 service details](https://www.hetzner.com/dedicated-rootserver/ax162/) · [Traffic terms](https://docs.hetzner.com/robot/general/traffic/)

AMD gives the 9454P a 2.75 GHz base, up to 3.8 GHz boost, 3.65 GHz all-core boost specification, 256 MB L3 and a default 290 W CPU TDP. Its memory controller supports 12 DDR5 channels and up to 4,800 MT/s. The 460.8 GB/s figure is AMD’s theoretical bandwidth per socket with all channels populated at that speed. The quoted AX162 configurations disclose total RAM and registered ECC, but the standard product sources do not establish DIMM count, channels populated, rank, actual memory clock, firmware limits or effective NUMA policy on an allocated machine. These quantities matter when several compiler processes stream data concurrently. [AMD 9454P specification](https://www.amd.com/en/products/processors/server/epyc/4th-generation-9004-and-8004-series/amd-epyc-9454p.html) · [Hetzner AX matrix](https://www.hetzner.com/dedicated-rootserver/matrix-ax/)

**The reference index is 100.** Normalize each published workload to its own 9454P result where a like-for-like result exists. For elapsed time use 100 × reference time / candidate time. For throughput use 100 × candidate jobs per unit time / reference jobs per unit time. Same CPU and nominal capacity give a strong rental comparison, but a serial TypeScript test, a parallel Rust compile and multiple Docker runners exercise different bottlenecks. The supply-side hardware specification alone cannot establish a candidate within 3–5% on all three. [Published benchmark evidence](published-benchmarks.md)

## Current monthly and setup prices

The public price feed reports separate EUR and USD tariffs. Each cell lists the monthly cap and one-time setup in that currency. The optional primary IPv4 costs **EUR 1.70 or USD 1.90 per month** with no setup charge. The model includes one IPv4 for both reference variants. The provider applies hourly billing up to the monthly cap and advertises immediate cancellation with no minimum term. [Live prices](https://www.hetzner.com/_resources/app/data/app/live_data_prices.json) · [Primary IPv4 price](https://docs.hetzner.com/general/infrastructure-and-availability/ipv4-pricing/) · [Robot billing and cancellation](https://docs.hetzner.com/general/billing-and-account-management/cancellation/cancellations-robot/)

| Currency and buyer basis | AX162-1 monthly / setup | AX162-2 monthly / setup |
|---|---:|---:|
| EUR, before tax, IPv6-only | 612.30 / 304.00 | 842.30 / 419.00 |
| **EUR, before tax, one IPv4** | **614.00 / 304.00** | **844.00 / 419.00** |
| EUR, SG consumer at 9% GST, one IPv4 | 669.26 / 331.36 | 919.96 / 456.71 |
| SGD equivalent of the EUR offer, before tax, one IPv4 | 870.41 / 430.95 | 1,196.45 / 593.97 |
| SGD equivalent of the EUR offer, SG consumer at 9%, one IPv4 | 948.74 / 469.74 | 1,304.14 / 647.43 |
| USD, provider tariff before tax, IPv6-only | 722.10 / 359.00 | 992.10 / 494.00 |
| USD, provider tariff before tax, one IPv4 | 724.00 / 359.00 | 994.00 / 494.00 |
| USD, provider tariff, SG consumer at 9%, one IPv4 | 789.16 / 391.31 | 1,083.46 / 538.46 |

With one IPv4 and the new setup, the EUR-account 12-month subtotal is **EUR 7,672** for AX162-1 and **EUR 10,547** for AX162-2. At 9% these become EUR 8,362.48 and EUR 11,496.23. At 36 months with the same rates, the corresponding totals are **EUR 22,408 / 30,803 before tax**, or **S$34,624.48 / S$47,596.30 with 9%** at the dated exchange rate. An existing customer deciding whether to keep a machine should substitute its avoidable future invoices and omit setup already paid.

**Tax follows the billing customer.** Hetzner lists 9% for Singapore, and 19% for a Germany-resident customer. Malaysia falls into its published group invoiced without VAT. That describes the supplier invoice only. IRAS tells GST-registered Singapore businesses to supply their registration number for qualifying overseas business purchases and specifies when reverse charge applies. Malaysian Customs separately describes service tax on qualifying digital services supplied by a registered foreign provider. Determine the actual status, invoice and non-recoverable tax before using a gross comparison. [Hetzner country table](https://docs.hetzner.com/general/billing-and-account-management/billing-at-hetzner/value-added-tax/) · [IRAS overseas services for local businesses](https://www.iras.gov.sg/taxes/goods-services-tax-%28gst%29/gst-and-digital-economy/local-businesses) · [Royal Malaysian Customs digital-service rules](https://mystods.customs.gov.my/about-mystods)

## How to reproduce the quote

1. In the [AX162 configurator](https://www.hetzner.com/dedicated-rootserver/ax162/configurator/) select the regular variant, location, currency and customer country. The public live JSON exposes the net fields even when the HTML shows a JavaScript loading screen.
2. In [the pricing feed](https://www.hetzner.com/_resources/app/data/app/live_data_prices.json), read `products.ROBOT_1724.locations` or `products.ROBOT_1725.locations`. Match `datacenter` to FSN1 or HEL1, then `prices.monthly` and `prices.setup` to the billing currency. Cross-check keys `1724` and `1725` in [the separate availability feed](https://www.hetzner.com/_resources/app/data/app/live_data_upfront.json). It reported both locations but no quantity or delivery commitment.
3. Use the [ECB dated observation](https://data-api.ecb.europa.eu/service/data/EXR/D.MYR+SGD+USD.EUR.SP00.A?startPeriod=2026-11-19&endPeriod=2026-11-20&format=csvdata). The latest value then available was **19 November 2026**, EUR 1 = SGD 1.4176 = MYR 4.5205 = USD 1.0992. A comparison in SGD uses the invoice currency once. EUR-account and USD-account totals differ even for the same machine.

Neither limited-stock ID `1727` nor `1757` appeared in those live feeds. The older AX162-1-LTD example at EUR 319 including IPv4 plus EUR 39 setup belongs to the historical research. A grandfathered price can remain relevant for an actual existing invoice. Hetzner’s June announcement applied the change to new orders and rescales. [Original announcement](https://www.hetzner.com/pressroom/standardization-and-price-adjustment-of-our-server-products/) · [Earlier dated comparison](../../research/buy-vs-rent/02-rental-market.md)

Signed-off-by: Alexey Zhokhov <alexey@zhokhov.com>
