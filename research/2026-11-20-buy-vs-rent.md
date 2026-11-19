# CI ownership and worldwide rental comparison — 20 November 2026

This extension compares buying non-ECC desktop/workstation hardware in Singapore or Malaysia with the rental research already in this repository. It adds a permanent [buy-versus-rent research folder](buy-vs-rent/README.md) for Rust/TypeScript builds and tests in Docker. Singapore is the preferred purchase/hosting market, with Malaysia second; worldwide rental locations remain available for comparison when geography is flexible.

## Source snapshot and repository scope

The rental input is the root README and dated logs at commit **07180f43068a8de01ae30c41a265ec16ef1f138b**, containing 104 rows across 38 alternative seller brands plus Hetzner. The seven-column table, numeric sort, row contents and existing historical logs are preserved. Importing an offer into the cost model does not reset its original checked date or establish new inventory.

New files:

- [Research index](buy-vs-rent/README.md).
- [Owned hardware and performance](buy-vs-rent/01-hardware-and-performance.md).
- [Singapore/Malaysia rental, colocation and local purchase](buy-vs-rent/02-rental-market.md).
- [12/24/36-month ownership and rental budgets](buy-vs-rent/03-rent-vs-buy-tco.md).
- [CI acceptance and procurement requirements](buy-vs-rent/04-validation-and-procurement.md).
- [All 104 existing rentals, capacity and commitment comparison](buy-vs-rent/05-repository-rental-comparison.md).

The root README links the extension, and METHODOLOGY distinguishes the new CI-specific requirement from the earlier general rental minimum.

## Findings that change the earlier ownership conclusion

**Worldwide rental coverage matters.** Comparing only against the regular Hetzner tariff overstates ownership's financial advantage. At the dated FX, UHost's 256 GB AX162-R known charges total S$10,368.91 over 36 months, BizoSiz's separate A1/A2 carts each S$13,096.55, and PlusClouds' A1 listing S$12,269.33. The corresponding Samsung-drive Singapore office budgets are S$15,466.87 for A2 and S$15,773.81 for A1. The rental figures precede unquoted taxes, IP/network and customer-specific charges; stock, term and operator qualifications remain visible.

**Capacity matching is stricter than the original raw-disk floor.** A1 requires at least 128 GB and two drives of at least 3.84 TB; A2 requires at least 256 GB and two drives of at least 1.92 TB. There are 32 A1-only, 32 A2-only, two dual-profile and 38 neither-profile rows. All 104 remain represented. CPU and storage performance are separate gates.

**The 5995WX is a screening candidate.** The +3% public multicore Clang observation is from an ASRock WRX80 system reporting 125.53 GB and Ubuntu 24.10, compared with an AX162 reporting 251.38 GB and Ubuntu 24.04.2. Frequency metadata does not establish sustained stock settings. The proposed ASUS/non-ECC BOM is a different machine, and the short fixed-task test does not certify actual CI within 3–5%.

**Lower-price storage options affect value.** The 20 November check added ADATA LEGEND 900 PRO 2 TB at S$479 and Lexar NM790 4 TB at S$859. Example parts estimates become S$8,069.40 for 5995WX/256 GB/two ADATA drives, S$6,399.20 for the Intel 64 GB-per-node pair with four ADATA drives, and S$8,829.40 for 5995WX/256 GB/two 4 TB Lexars. Manufacturer disclosures and actual CI I/O remain prerequisites; no equivalent latency is assumed from price or sequential bandwidth.

**Compatibility and operation are concrete procurement conditions.** The original ASUS board lists BIOS 1003 for 5995WX and qualifies the exact 32 GB Crucial revision CT32G4DFD832A.C16FE for eight sockets. Retail base SKUs do not guarantee the revision or quantity. The proposed eight-module 16 GB alternative remains unqualified. The build must also satisfy the board's power-cable, cooling, case and NVMe-layout instructions. Malaysia 4U hosting remains a cost floor until fit, intake airflow, peak current/power and facility approval are established.

## Current feed and price verification

The official [live price feed](https://www.hetzner.com/_resources/app/data/app/live_data_prices.json) and [availability feed](https://www.hetzner.com/_resources/app/data/app/live_data_upfront.json) were fetched successfully in this pass:

| Product | Monthly EUR / setup EUR | Separate USD tariff / setup | Availability result |
|---|---|---|---|
| ROBOT_1724, AX162-1 | 612.30 / 304 | 722.10 / 359 | FSN1, HEL1 |
| ROBOT_1725, AX162-2 | 842.30 / 419 | 992.10 / 494 | FSN1, HEL1 |
| LTD IDs 1727 and 1757 | Absent | Absent | Absent |

Prices exclude IPv4 and tax. The price feed also contains NBG1 entries, which do not override the narrower availability feed. The historical adjustment-document URL returns 404 on direct retrieval; it is no longer the sole support for regular prices. LTD is historical or existing-contract sensitivity only, not current purchasable supply.

The [UHost AX162-R configurator](https://uhost.online/en/dedicated/19) and [PlusClouds listings](https://plusclouds.com/servers) were reopened and retained the cited base configuration/rates. The independent BizoSiz fetch failed in this pass; its comparison uses the repository's already recorded 20 November matching-cart evidence rather than claiming a new checkout verification. No login, seller message, reservation or purchase was made.

The [dated ECB SGD observation](https://data-api.ecb.europa.eu/service/data/EXR/D.SGD.EUR.SP00.A?startPeriod=2026-11-19&endPeriod=2026-11-19&format=csvdata) and [MYR observation](https://data-api.ecb.europa.eu/service/data/EXR/D.MYR.EUR.SP00.A?startPeriod=2026-11-19&endPeriod=2026-11-19&format=csvdata) were fetched as CSV and confirm **1.4176 SGD/EUR** and **4.5205 MYR/EUR**. The extension preserves the repository's 19 November USD and BRL basis. These are fixed comparison rates, not future settlement forecasts.

## Calculation and evidence rules

Of 104 rental rows, **78 state a setup amount**, **23 omit setup from the selected quote**, and **three lack enough terms for a total**. Horizon calculations preserve those distinctions. A missing setup line is marked unknown, not changed to zero. Twenty-four- and thirty-six-month prepaid variants retain the whole commitment needed for the selected horizon; later renewals at the same price are explicit assumptions.

The office model separates retail parts, UPS/assembly allowances, assumed average wall power, cooling, connectivity and maintenance reserve. The 350 W workstation and 450 W combined desktop-pair figures are assumptions, not measurements. A 9% Singapore-billing rental calculation is a scenario, not a determination of the customer's tax position. Malaysia hosting of Singapore-sourced parts is not described as a locally sourced Malaysian workstation quote. A separate Malaysia-local Intel pair, with 64 GB per host and RM24,008 parts, has illustrative office budgets of S$10,405.90 / S$12,083.05 / S$13,760.19 over 12/24/36 months; its split memory and unmeasured throughput remain explicit.

The CI acceptance procedure requires both critical-job latency and sustained queue throughput by default: 1.03× duration / 0.97× rate for 3%, or 1.05× / 0.95× for 5%. Uncertainty crossing a threshold is unresolved. No actual user repository benchmark or candidate wall-power measurement has been performed.

## Research and review

GPT-6.2 Astra at max reasoning performed the hardware refresh and exhaustive rental comparison. GPT-6.2 Sol at max reviewed benchmark claims, compatibility, calculations, capacity matching, tax/fee treatment and repository integration. Validation covers the 104-row mapping, arithmetic, source/relative links and preservation of the existing table. No application code or CI workflow was changed.
