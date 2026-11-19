# Dedicated server offer audit, 19 November 2026

[Home](../README.md) · [Research](README.md)

**Evidence date** · 19 November 2026

[Pro-m](#pro-m-physical-dedicated-servers) · [IP-Projects](#ip-projects-configurations) · [Drive options](#additional-drive-choices) · [Excluded offers](#other-leads-and-exclusions)

Evidence record from the 2026-11-19 research pass. The [rental catalog](../rentals/README.md) is the canonical comparison; [the consolidated history](2026-11-19.md#continuation-of-research) records later corrections across parallel checks.

## Pro-m physical dedicated servers

The anonymous configurator reached through each published order button returned HTTP 200 with the matching CPU, capacities, selected country, a USD first invoice and subsequent monthly charge. Its public price data specified zero tax and setup-fee tax for this unauthenticated display. Final taxes can depend on billing address. Hardware stock counts, port speed, included traffic, city and IPv4 pricing were not disclosed. The check reached the initial order summary only. The provider’s FAQ describes isolated physical hardware, no virtualization, and a one-month minimum. All totals below are in USD.

| Country | RAM | NVMe | Recurring | Setup | First invoice | Year one | Checkout |
|---|---:|---|---:|---:|---:|---:|---|
| Finland | 128 GB | 2 × 3.84 TB | 347 | 527 | 874 | 4,691 | https://my.pro-m.org/products/dedicated/ded-fi-030/checkout?plan=95&options%5B1%5D=2 |
| Finland | 256 GB | 2 × 1.92 TB | 347 | 697 | 1,044 | 4,861 | https://my.pro-m.org/products/dedicated/ded-fi-028/checkout?plan=83&options%5B1%5D=2 |
| Germany | 128 GB | 2 × 3.84 TB | 369 | 527 | 896 | 4,955 | https://my.pro-m.org/products/dedicated/ded-de-029/checkout?plan=91&options%5B1%5D=3 |
| Germany | 256 GB | 2 × 1.92 TB | 369 | 689 | 1,058 | 5,117 | https://my.pro-m.org/products/dedicated/ded-de-027/checkout?plan=75&options%5B1%5D=3 |

All four have the exact 48-core/96-thread EPYC 9454P. The 128 GB versions also match AX162-1 raw storage and mirrored capacity. The 256 GB versions have 3.84 TB raw, 1.92 TB mirrored. The site provides a published quote and an active matching checkout. Physical allocation and delivery have not been confirmed. The provider lists a one-month term for each offer. The [published order button for the German 256 GB plan](https://pro-m.org/order/start?offer=ddcf2b98-fed3-482d-9adf-9cd37e647de2) redirects to the matching checkout. Sources: https://pro-m.org/en/services/dedicated , https://pro-m.org/en/faq , https://pro-m.org/en/about .

## IP-Projects configurations

All figures below are in EUR. Exact chassis entries at https://www.ip-projects.de/api/order/products/dedicatedServer report orderable YES. The public configurator defaults to Germany and explicitly sets tax_country_code DE and tax_percent 19. Each line calculation uses the appropriate contract-duration and billing-interval chassis price plus the RAM kit and selected drive count from the same interval's slot prices. Gross figures divided by 1.19 yield net. The provider's client calculator tests for at least one installed drive, permitting single-drive variants. Base chassis amount excludes all selected slots, including the catalog defaults. Default RAM and SSD options are replaced, not added. All examples use 128 GB ECC registered RAM from two 64 GB modules and free Linux/basic default options. Frankfurt; redundant 2 × 1 Gbit/s and 100 TB fair-use traffic, one IPv4 and /64 IPv6 included. Hardware allocation unconfirmed; the Threadripper catalog lists commonly 1–3 business days if the system is not already available.

Public pages and inputs:

- 9980X, 9985WX and 9995WX: https://www.ip-projects.de/en/dedicated-server/performance/amd_str5 . 9980X configurator: https://www.ip-projects.de/en/order/dedicated-server/amd-str5-l-g1 . 9985WX: https://www.ip-projects.de/en/order/dedicated-server/amd-str5-xl-g1 .
- 9355P, dual 9535 and dual 9745: https://www.ip-projects.de/en/dedicated-server/enterprise/amd . 9355P configurator: https://www.ip-projects.de/en/order/dedicated-server/amd-enterprise-l-g1 .
- Slot matrices: https://www.ip-projects.de/api/order/products/dedicatedServer/AMD_STR5_L_G1/slots , https://www.ip-projects.de/api/order/products/dedicatedServer/AMD_STR5_XL_G1/slots , https://www.ip-projects.de/api/order/products/dedicatedServer/AMD_ENTERPRISE_L_G1/slots , https://www.ip-projects.de/api/order/products/dedicatedServer/AMD_ENTERPRISE_XL_G1/slots . Replace /slots with /options for OS and optional services.
- Net baseline: €612.30/month plus €304 once = €7,651.60 at 12 months/€14,999.20 at 24 months. Compare like horizons. 9985WX with 2 × 1 TB at €606.99/month-equivalent prepaid plus €476.95 setup totals €7,760.81, €109.21 more in year one. At 24 months prepaid it totals €14,102.78, €896.42 less. For the two-year commitment with one year's rent paid at a time, the setup fee is also zero.
- Exact regular 9980X gross chassis €384.5604, RAM €210.0469, each 2 TB NVMe €10.6981. Exact gross annual rent for 2 × 2 TB €6,948.5528, 24-month rent €13,453.5569. Gross 12-month-term setup €407.9915. Independent matrix sums rather than rounding a monthly discount.
- Storage interpretation: 1 × 2 TB has no disk redundancy. 2 × 1 TB offers 2 TB raw or 1 TB mirrored. 2 × 2 TB offers 4 TB raw or 2 TB mirrored before formatting. 2 × 1.9 TB gives 3.8 TB raw or 1.9 TB mirrored. The manufacturer names enterprise U.2 NVMe in slots. Both 2 × 2 TB and 2 × 4 TB pairs retain at least 2 TB in a mirror before formatting.
- CPU evidence: https://www.cpubenchmark.net/high_end_cpus.html and https://www.cpubenchmark.net/singleThread.html show 9980X 143,623 / 4,556 versus baseline 94,689 / 2,988; 9985WX 150,121 / 4,486. The 9980X supports four memory channels, the PRO 9985WX eight and EPYC 9454P twelve. Two DIMMs occupy at most two channels. The actual Hetzner DIMM layout was not verified. Throughput figures are CPU test results rather than tests of these specific machines.
- 9355P PassMark comparison: https://www.cpubenchmark.net/compare/5596vs6449/AMD-EPYC-9454P-vs-AMD-EPYC-9355P . 96,603 / 3,747 versus 94,689 / 2,988 means +2.02% CPU Mark, +25.4% single-thread. 32 instead of 48 physical cores could underperform on sustained wide workloads. The sTR5 M 9965WX reads 92,220 aggregate and misses the strict floor. IPP has no orderable 9555P SKU. The Enterprise XL is two 9535 processors, not one; even a 24-month prepaid 128 GB configuration exceeds the baseline.

**AMD_STR5_L_G1, 2 × 2 TB NVMe**

| Minimum term | Billing interval | Gross per invoice for rent | Net rent per invoice | Net effective/month | Net setup | Net committed total |
|---|---|---:|---:|---:|---:|---:|
| 1 mo | 1 mo | 616.00 | 517.65 | 517.65 | 2,742.80 | 3,260.45 |
| 12 mo | 1 mo | 616.00 | 517.65 | 517.65 | 342.85 | 6,554.65 |
| 24 mo | 1 mo | 616.00 | 517.65 | 517.65 | 0.00 | 12,423.60 |
| 12 mo | 12 mo | 6,948.55 | 5,839.12 | 486.59 | 342.85 | 6,181.97 |
| 24 mo | 12 mo | 6,948.55 | 5,839.12 | 486.59 | 0.00 | 11,678.24 |
| 24 mo | 24 mo | 13,453.56 | 11,305.51 | 471.06 | 0.00 | 11,305.51 |

**AMD_STR5_L_G1, 2 × 1 TB NVMe**

| Minimum term | Billing interval | Gross per invoice for rent | Net rent per invoice | Net effective/month | Net setup | Net committed total |
|---|---|---:|---:|---:|---:|---:|
| 1 mo | 1 mo | 607.22 | 510.27 | 510.27 | 2,742.80 | 3,253.07 |
| 12 mo | 1 mo | 607.22 | 510.27 | 510.27 | 342.85 | 6,466.09 |
| 24 mo | 1 mo | 607.22 | 510.27 | 510.27 | 0.00 | 12,246.48 |
| 12 mo | 12 mo | 6,849.57 | 5,755.94 | 479.66 | 342.85 | 6,098.79 |
| 24 mo | 12 mo | 6,849.57 | 5,755.94 | 479.66 | 0.00 | 11,511.88 |
| 24 mo | 24 mo | 13,261.92 | 11,144.47 | 464.35 | 0.00 | 11,144.47 |

**AMD_STR5_L_G1, 1 × 2 TB NVMe**

| Minimum term | Billing interval | Gross per invoice for rent | Net rent per invoice | Net effective/month | Net setup | Net committed total |
|---|---|---:|---:|---:|---:|---:|
| 1 mo | 1 mo | 605.31 | 508.66 | 508.66 | 2,742.80 | 3,251.46 |
| 12 mo | 1 mo | 605.31 | 508.66 | 508.66 | 342.85 | 6,446.77 |
| 24 mo | 1 mo | 605.31 | 508.66 | 508.66 | 0.00 | 12,207.84 |
| 12 mo | 12 mo | 6,827.85 | 5,737.69 | 478.14 | 342.85 | 6,080.54 |
| 24 mo | 12 mo | 6,827.85 | 5,737.69 | 478.14 | 0.00 | 11,475.38 |
| 24 mo | 24 mo | 13,219.86 | 11,109.13 | 462.88 | 0.00 | 11,109.13 |

**AMD_ENTERPRISE_L_G1, 2 × 1.9 TB NVMe**

| Minimum term | Billing interval | Gross per invoice for rent | Net rent per invoice | Net effective/month | Net setup | Net committed total |
|---|---|---:|---:|---:|---:|---:|
| 1 mo | 1 mo | 570.20 | 479.16 | 479.16 | 1,800.00 | 2,279.16 |
| 12 mo | 1 mo | 570.20 | 479.16 | 479.16 | 225.00 | 5,974.92 |
| 24 mo | 1 mo | 570.20 | 479.16 | 479.16 | 0.00 | 11,499.84 |
| 12 mo | 12 mo | 6,431.94 | 5,404.99 | 450.42 | 225.00 | 5,629.99 |
| 24 mo | 12 mo | 6,431.94 | 5,404.99 | 450.42 | 0.00 | 10,809.98 |
| 24 mo | 24 mo | 12,453.30 | 10,464.96 | 436.04 | 0.00 | 10,464.96 |

**AMD_ENTERPRISE_L_G1, 1 × 3.8 TB NVMe**

| Minimum term | Billing interval | Gross per invoice for rent | Net rent per invoice | Net effective/month | Net setup | Net committed total |
|---|---|---:|---:|---:|---:|---:|
| 1 mo | 1 mo | 561.39 | 471.76 | 471.76 | 1,800.00 | 2,271.76 |
| 12 mo | 1 mo | 561.39 | 471.76 | 471.76 | 225.00 | 5,886.12 |
| 24 mo | 1 mo | 561.39 | 471.76 | 471.76 | 0.00 | 11,322.24 |
| 12 mo | 12 mo | 6,332.57 | 5,321.49 | 443.46 | 225.00 | 5,546.49 |
| 24 mo | 12 mo | 6,332.57 | 5,321.49 | 443.46 | 0.00 | 10,642.98 |
| 24 mo | 24 mo | 12,260.90 | 10,303.28 | 429.30 | 0.00 | 10,303.28 |

**AMD_STR5_XL_G1, 2 × 1 TB NVMe**

| Minimum term | Billing interval | Gross per invoice for rent | Net rent per invoice | Net effective/month | Net setup | Net committed total |
|---|---|---:|---:|---:|---:|---:|
| 1 mo | 1 mo | 768.41 | 645.72 | 645.72 | 3,815.60 | 4,461.32 |
| 12 mo | 1 mo | 768.41 | 645.72 | 645.72 | 476.95 | 8,225.59 |
| 24 mo | 1 mo | 768.41 | 645.72 | 645.72 | 0.00 | 15,497.28 |
| 12 mo | 12 mo | 8,667.79 | 7,283.86 | 606.99 | 476.95 | 7,760.81 |
| 24 mo | 12 mo | 8,667.79 | 7,283.86 | 606.99 | 0.00 | 14,567.72 |
| 24 mo | 24 mo | 16,782.31 | 14,102.78 | 587.62 | 0.00 | 14,102.78 |

**AMD_STR5_XL_G1, 2 × 2 TB NVMe**

| Minimum term | Billing interval | Gross per invoice for rent | Net rent per invoice | Net effective/month | Net setup | Net committed total |
|---|---|---:|---:|---:|---:|---:|
| 1 mo | 1 mo | 777.19 | 653.10 | 653.10 | 3,815.60 | 4,468.70 |
| 12 mo | 1 mo | 777.19 | 653.10 | 653.10 | 476.95 | 8,314.15 |
| 24 mo | 1 mo | 777.19 | 653.10 | 653.10 | 0.00 | 15,674.40 |
| 12 mo | 12 mo | 8,766.78 | 7,367.04 | 613.92 | 476.95 | 7,843.99 |
| 24 mo | 12 mo | 8,766.78 | 7,367.04 | 613.92 | 0.00 | 14,734.08 |
| 24 mo | 24 mo | 16,973.95 | 14,263.82 | 594.33 | 0.00 | 14,263.82 |

**AMD_ENTERPRISE_XL_G1, 2 × 1.9 TB NVMe**

| Minimum term | Billing interval | Gross per invoice for rent | Net rent per invoice | Net effective/month | Net setup | Net committed total |
|---|---|---:|---:|---:|---:|---:|
| 1 mo | 1 mo | 922.92 | 775.56 | 775.56 | 5,464.00 | 6,239.56 |
| 12 mo | 1 mo | 922.92 | 775.56 | 775.56 | 683.00 | 9,989.72 |
| 24 mo | 1 mo | 922.92 | 775.56 | 775.56 | 0.00 | 18,613.44 |
| 12 mo | 12 mo | 10,410.61 | 8,748.41 | 729.03 | 683.00 | 9,431.41 |
| 24 mo | 12 mo | 10,410.61 | 8,748.41 | 729.03 | 0.00 | 17,496.82 |
| 24 mo | 24 mo | 20,156.71 | 16,938.41 | 705.77 | 0.00 | 16,938.41 |

**AMD_ENTERPRISE_XL_G1, 1 × 3.8 TB SATA SSD**

| Minimum term | Billing interval | Gross per invoice for rent | Net rent per invoice | Net effective/month | Net setup | Net committed total |
|---|---|---:|---:|---:|---:|---:|
| 1 mo | 1 mo | 870.66 | 731.65 | 731.65 | 5,464.00 | 6,195.65 |
| 12 mo | 1 mo | 870.66 | 731.65 | 731.65 | 683.00 | 9,462.80 |
| 24 mo | 1 mo | 870.66 | 731.65 | 731.65 | 0.00 | 17,559.60 |
| 12 mo | 12 mo | 9,821.18 | 8,253.09 | 687.76 | 683.00 | 8,936.09 |
| 24 mo | 12 mo | 9,821.18 | 8,253.09 | 687.76 | 0.00 | 16,506.18 |
| 24 mo | 24 mo | 19,015.47 | 15,979.39 | 665.81 | 0.00 | 15,979.39 |

## Additional drive choices

**AMD_STR5_L_G1, 2 × 4 TB NVMe**

| Minimum term | Billing interval | Gross per invoice for rent | Net rent per invoice | Net effective/month | Net setup | Net committed total |
|---|---|---:|---:|---:|---:|---:|
| 1 mo | 1 mo | 641.87 | 539.39 | 539.39 | 2,742.80 | 3,282.19 |
| 12 mo | 1 mo | 641.87 | 539.39 | 539.39 | 342.85 | 6,815.53 |
| 24 mo | 1 mo | 641.87 | 539.39 | 539.39 | 0.00 | 12,945.36 |
| 12 mo | 12 mo | 7,240.34 | 6,084.32 | 507.03 | 342.85 | 6,427.17 |
| 24 mo | 12 mo | 7,240.34 | 6,084.32 | 507.03 | 0.00 | 12,168.64 |
| 24 mo | 24 mo | 14,018.55 | 11,780.29 | 490.85 | 0.00 | 11,780.29 |

**AMD_STR5_XL_G1, 1 × 2 TB NVMe**

| Minimum term | Billing interval | Gross per invoice for rent | Net rent per invoice | Net effective/month | Net setup | Net committed total |
|---|---|---:|---:|---:|---:|---:|
| 1 mo | 1 mo | 766.49 | 644.11 | 644.11 | 3,815.60 | 4,459.71 |
| 12 mo | 1 mo | 766.49 | 644.11 | 644.11 | 476.95 | 8,206.27 |
| 24 mo | 1 mo | 766.49 | 644.11 | 644.11 | 0.00 | 15,458.64 |
| 12 mo | 12 mo | 8,646.08 | 7,265.61 | 605.47 | 476.95 | 7,742.56 |
| 24 mo | 12 mo | 8,646.08 | 7,265.61 | 605.47 | 0.00 | 14,531.22 |
| 24 mo | 24 mo | 16,740.25 | 14,067.44 | 586.14 | 0.00 | 14,067.44 |

**AMD_ENTERPRISE_L_G1, 1 × 3.8 TB SATA SSD**

| Minimum term | Billing interval | Gross per invoice for rent | Net rent per invoice | Net effective/month | Net setup | Net committed total |
|---|---|---:|---:|---:|---:|---:|
| 1 mo | 1 mo | 517.95 | 435.25 | 435.25 | 1,800.00 | 2,235.25 |
| 12 mo | 1 mo | 517.95 | 435.25 | 435.25 | 225.00 | 5,448.00 |
| 24 mo | 1 mo | 517.95 | 435.25 | 435.25 | 0.00 | 10,446.00 |
| 12 mo | 12 mo | 5,842.51 | 4,909.67 | 409.14 | 225.00 | 5,134.67 |
| 24 mo | 12 mo | 5,842.51 | 4,909.67 | 409.14 | 0.00 | 9,819.34 |
| 24 mo | 24 mo | 11,312.07 | 9,505.94 | 396.08 | 0.00 | 9,505.94 |

## Evidence on the two EPYC generations

Lenovo tested one CPU per ThinkSystem SR635 V3 system with twelve 32 GB DIMMs. The 32-core EPYC 9355P posted 478 on SPECrate2017_int_base versus 525 for the 48-core 9454P, or 9.0% lower. Its SPECrate2017_fp_base was 644 versus 544, or 18.4% higher. These results demonstrate a real throughput trade-off behind the small PassMark difference. The generations used different software and memory speeds. Neither system was the rented machine. Sources: [9355P integer](https://www.spec.org/cpu2017/results/res2024q4/cpu2017-20241104-45295.html), [9454P integer](https://www.spec.org/cpu2017/results/res2023q1/cpu2017-20230227-34459.html), [9355P floating point](https://www.spec.org/cpu2017/results/res2024q4/cpu2017-20241104-45293.html), [9454P floating point](https://spec.org/cpu2017/results/res2023q1/cpu2017-20230227-34461.html).

For Turin EPYC 9455 without a P or embedded suffix, Lenovo measured 627 on SPECrate2017_int_base in the SR635 V3, 19.4% higher than the 9454P's 525. Both have 48 cores and 96 threads. A 9455P or 9455 Emb PassMark result is for a different part. Sources: [9455 integer](https://www.spec.org/cpu2017/results/res2025q2/cpu2017-20250324-47137.html), [AMD 9455 specs](https://www.amd.com/en/products/processors/server/epyc/9005-series/amd-epyc-9455.html), [AMD 9454P specs](https://www.amd.com/en/products/processors/server/epyc/4th-generation-9004-and-8004-series/amd-epyc-9454p.html), [AMD 9980X specs](https://www.amd.com/en/products/processors/ryzen-threadripper/9000-series/amd-ryzen-threadripper-9980x.html).

## ENTRONYX TITAN-96, current advertised configuration with unverified allocation

Both current catalogs identify one EPYC 9455, 128 GB DDR5-4800 ECC registered, 2 × 1.92 TB NVMe, 1 Gbit/s unmetered transfer, one IPv4 and a /64 IPv6 block. Default RAID 1 leaves 1.92 TB before formatting. The current provider configurator's product data fixes the monthly setup at €299.99 for this plan. Its pricing function applies the region factor to rental and omits it from setup. On 12- and 24-month prepaid contracts, the setup fee is zero. Prices are EUR, ex VAT. The provider also shows USD using its own exchange rate.

| Location | Term and payment | Net rent per month or equivalent | Net setup | Net first invoice | Net year-one total on monthly renewals or net committed total on prepaid term |
|---|---|---:|---:|---:|---:|
| Helsinki | Monthly | 281.99 | 299.99 | 581.98 | 3,683.87 |
| Helsinki | Prepay 12 months | 267.89 | 0.00 | 3,214.68 | 3,214.68 |
| Helsinki | Prepay 24 months | 259.43 | 0.00 | 6,226.32 | 6,226.32 |
| Frankfurt or Düsseldorf | Monthly | 299.99 | 299.99 | 599.98 | 3,899.87 |
| Frankfurt or Düsseldorf | Prepay 12 months | 284.99 | 0.00 | 3,419.88 | 3,419.88 |
| Frankfurt or Düsseldorf | Prepay 24 months | 275.99 | 0.00 | 6,623.76 | 6,623.76 |

The current company site accepts business customers. The exact official configure link opens plan ID titan-96t. Its downloadable catalog includes the availability label and stockPct=33 as static product fields shared across its regions. This label cannot verify live, region-specific hardware counts. A September-indexed version of the provider’s German terms and legal notice described the website as a demonstration project. That wording is absent from the versions checked on 19 November. The corporate domain now redirects to the current cloud site. This history warrants listing the offer as a current business-only advertised lead pending confirmation of physical allocation. The public site’s storage and network options group the model under the product name rise-xl. That mapping alone does not establish supplier identity or availability.

Sources: [TITAN regional prices](https://entronyx.cloud/en/bare-metal/titan), [configurator for the exact model](https://entronyx.cloud/en/konfigurator/bare-metal?plan=titan-96t), [prepayment rules](https://entronyx.cloud/en/preise), [current business-only legal notice](https://entronyx.cloud/impressum), [current German terms](https://entronyx.cloud/agb), [price and stock definitions served by configurator](https://entronyx.cloud/en/_next/static/chunks/1c6et-nlv6oug.js), [region and fee calculation](https://entronyx.cloud/en/_next/static/chunks/36fmw83yu8mcs.js). Asset URLs may change with a site deployment.

## Other leads and exclusions

| Provider | Hardware and displayed price | Result |
|---|---|---|
| [VisuHost](https://visuhost.com/dedicated/epyc-dedicated-server) | Germany 9454P, 256 GB, 2 × 2 TB NVMe, from €299.99. 9554P with 256 GB and 2 × 2 TB from €399.99. | The 9454P link points to 9374F and returned HTTP 525. The 9554P link points to 7543P. Live, matching price and stock unconfirmed. |
| [HostX DS-3](https://www.hostx.eu/dedicated-servers/) | Germany 9454P, 128 GB, 2 × 1.9 TB NVMe RAID 1, 1 Gbps best-effort/15 TB. €499/mo + €1,999 setup ex VAT, 12-month minimum. IPv4 and standard management included. | €7,987 first year, €335.40 above Hetzner. At 15 months the setup difference has been recovered if prices hold. Order link opens general sales contact. |
| [LowCostDedi](https://lowcostdedi.com/dedicated-servers/amd-epyc-9455p) | Search index recorded 9455P, 256 GB, 2 × 3.84 TB at $329/month. | Product, category and root all returned 404 on the live check. Retain as a historical lead only. |
| [NetVO](https://netvo.io/store/dedicated-servers) | France EPYC 9455, 128 GB, 2 × 1.92 TB, 1G unmetered, $434.99/month + $435. | An early request redirected to web hosting. A later anonymous session preserving normal cookies reached the [matching PID 66 cart](https://netvo.io/cart.php?a=add&pid=66) and verified $434.99/month + $435 setup ($5,654.88 in year one), or $4,949.99 annual prepayment ($412.50/month equivalent) with no setup line shown on that cycle. Applicable tax and physical stock remain unconfirmed. Its 9454P alternative costs $888.99 + $440 setup. |
| [TeraSwitch](https://teraswitch.com/configure) | EPYC 9554P, 128 GB DDR5, 2 × 25G bonded, catalog $665/month. Public configurator supplies only 2 × 960 GB NVMe for that base price. Cheapest extra drive is another 960 GB at $17/month. | $682/month estimate on the minimum 2.88 TB raw configuration, above the $673.04 Hetzner recurring benchmark at the specified FX rate. Setup and stock unconfirmed, actual billing hourly. The [pricing page](https://teraswitch.com/pricing) advertises an 8 TB minimum but the current configurator uses only the two required 960 GB slots by default. [Public configurator matrix](https://teraswitch.com/_next/static/chunks/0gq3tn~k_4rt7.js), plan 9554p-NB. |
| [Contabo](https://contabo.com/en-us/dedicated-servers/) | EPYC 9355P, 128 GB, 2 × 1 TB NVMe and 1G. Regional provider page gives €399 with VAT as applicable. Dedicated product page advertises €359.10/month for the first 12 months. | Promotional horizon and mixed benchmark results are material. 2 TB raw is 1 TB under RAID 1. Checkout under the visitor's address is needed to state an exact ex-VAT price. [Regional reference](https://contabo.com/en-us/locations/europe/), [physical tenancy](https://docs.contabo.com/docs/servers-hosting/dedicated-servers/). |
| [Q-DC](https://q-dc.net/en/server-configurator/?platform=qdc-06) | NL 9355P/128 GB and 2 × 960 GB U.2 NVMe from €454. | 1.92 TB raw misses 2 TB. The form explicitly requires a separate quote for hardware upgrades. |
| [quicksrv](https://quicksrv.io/dedicated-servers) | NL 9354, 384 GB/2 × 3.84 TB for €349. | Single 9354 is below CPU floor. Dual 9354 variant lists €649, made to order/out of stock. |
| [WebNX](https://webnx.com/dedicated-servers) | Threadripper 9970X advertised from $1,499/month. | No price advantage over the stipulated benchmark. |
| [Privex](https://pay.privex.io/order/choose-server) | FI, exact 9454P/128 GB/2 × 3.84 TB, $880/month + $440 setup. | Above recurring baseline. |

For IP-Projects the 24-month prepaid chassis-plus-RAM cost alone is €633.80/month for dual 9535 and €865.94 for dual 9745. Every qualifying drive configuration lies above the €612.30 monthly benchmark. The Threadripper PRO 9995WX/128 GB also exceeds the benchmark even with 24 months prepaid. A single 2 TB NVMe drive costs €17,497.97 total (€729.08/month equivalent), while two 1 TB drives cost €17,533.31 (€730.55/month equivalent). Prices above use the capacities shown in the provider’s slot matrix.
