# Dedicated rental and colocation market: Singapore first, Malaysia second

Regional-offer snapshot: **19 November 2026**. Repository integration and Hetzner live-feed recheck: **20 November 2026**. This is a comparison of publicly advertised dedicated hardware and ownership-hosting options, not a reserved inventory list or a supplier endorsement. Regional entries retain their original observation date unless a later check is specifically recorded. No orders, account registrations, paid trials or vendor messages were made.

The non-ECC preference applies to **owned hardware**. Rental servers may use ECC. Ordinary cloud vCPUs are not treated as dedicated physical cores. See [01-hardware-and-performance.md](01-hardware-and-performance.md) for the owned builds and [03-rent-vs-buy-tco.md](03-rent-vs-buy-tco.md) for cost scenarios. The [main repository table](../../README.md#servers) supplies the worldwide rental baseline: [file 05](05-repository-rental-comparison.md) preserves the original 104 rows and [file 08](08-latest-rental-comparisons.md) adds the latest 15, covering all 119. The Singapore/Malaysia leads below supplement that baseline; they do not replace cheaper European options when geography is flexible.

## 1. Currency and comparison rules

[ECB reference rates dated 19 November 2026][R01]: EUR 1 = SGD 1.4176 = USD 1.0992 = MYR 4.5205. Derived conversions: USD 1 = SGD 1.289665211; MYR 1 = SGD 0.313593629. These are reference conversions, not a card/bank settlement quote. Tables retain the original price and show rounded SGD for comparison. Future FX, bank spreads and taxes can change actual costs.

Prices below exclude taxes unless explicitly stated. Do not infer customer billing residence from server location. Singapore GST and Malaysian SST applicability require the actual seller, service, customer and invoice. A monthly-equivalent term price must not be treated as month-to-month cancellation.

Performance classes:

- **Closest CPU family:** 9454P, or one socket of 9454. [AMD][R02] lists the same 48 Zen 4 cores, 96 threads, clocks and cache for these single-socket comparisons. DIMM layout, power settings, disks and actual CI still determine whether a 3–5% tolerance is met.
- **Faster candidates:** 48-core Zen 5 9455 or 64-core 9554/9555(P). Greater parallel capability does not prove a particular CI speedup.
- **Separate worker pools:** two 9950X hosts can process independent jobs, with per-host RAM/storage limits.
- **Unproven throughput-oriented alternatives:** Zen 4c 8534P/9754 and older CPUs must be benchmarked; a high core count alone does not satisfy the requested latency or throughput target.

## 2. Hetzner: European reference, not a Singapore dedicated server

The [AX162 dedicated product][R03] advertises Falkenstein and Helsinki. [Hetzner's Singapore cloud location][R04] does not make the AX162 available in Singapore.

The [official live price feed][R59] was rechecked on 20 November: **ROBOT_1724** is EUR 612.30/month + EUR 304 setup; **ROBOT_1725** is EUR 842.30/month + EUR 419 setup, before tax and IPv4. This independently confirms the regular rates from [the historical adjustment page][R05], whose direct URL now returns 404. The price feed has NBG1, FSN1 and HEL1 entries, while the [availability feed][R60] currently lists **FSN1 and HEL1** for these products; a location's price entry alone is not inventory. Add one [primary IPv4 at EUR 1.70/month][R06].

| Offer | RAM / NVMe | Monthly including one IPv4, before tax | Setup before tax | Approx. SGD monthly / setup, before tax |
|---|---|---:|---:|---:|
| AX162-1 regular | 128 GB / 2 × 3.84 TB | EUR 614.00 | EUR 304.00 | S$870.41 / S$430.95 |
| AX162-2 regular | 256 GB / 2 × 1.92 TB | EUR 844.00 | EUR 419.00 | S$1,196.45 / S$593.97 |
| AX162-1-LTD — historical sensitivity, unavailable in current feed | Same AX162-1 configuration | EUR 319.00 | EUR 39.00 | S$452.21 / S$55.29 |

**LTD is not an available alternative in this snapshot.** Product IDs 1727 and 1757 are absent from the live price and availability feeds, consistent with the repository's [earlier inventory check](../2026-11-19.md). Retain its old price only for an existing invoice or a hypothetical future reappearance, not for a new purchase recommendation. No current AX162-2-LTD price was established. The standard connection is a 1 Gbps port with unlimited traffic; the 10 Gbps upgrade has different traffic terms. [Configuration][R08].

An existing grandfathered server may have a different invoice. Compare that actual recurring charge before cancelling or replacing it. [The new-order change][R09] should not automatically be applied to an existing lease. [Robot cancellation/billing rules][R10] also matter when planning short trials or churn. The live feed has separate USD tariffs: USD 722.10 + 359 setup for AX162-1 and USD 992.10 + 494 for AX162-2, before IPv4/tax. Do not assume an FX-converted EUR quote is the amount charged on a USD-billed account.

## 3. Singapore dedicated rental shortlist

### Single-host candidates

| Provider / advertised Singapore configuration | Published recurring price | Setup, term and network | Evidence and limitations |
|---|---:|---|---|
| **PowerDedi: EPYC 9454P, 256 GB, 2 × 3.84 TB NVMe** | **USD 489 ≈ S$630.65/month**, before VAT | Zero setup; monthly; 10 Gbps unmetered; one IPv4; IPMI/KVM; crypto-only | Same CPU, more capacity than either reference. Singapore summary says in stock, but the same rendered order form says location “Not offered.” Fulfilment remains unresolved. **Quote lead, not confirmed availability.** [Source][R11] |
| **UltaHost Ulta-X10: one EPYC 9454, 512 GB, 2 × 1.92 TB NVMe** | **USD 1,087.82 ≈ S$1,402.92/month equivalent** | Displayed **two-year** term; setup/tax not established; 2 Gbps; management/unlimited bandwidth advertised | Closest CPU class, more RAM than AX162-2. No stock count. Confirm the exact physical SKU, commitment, renewal and provisioning; do not use this as a one-month rental price. [Source][R12] |
| **INTROSERV DC4SC-a5: EPYC 9554, 64C/128T; 128 GB + 2 × 3.84 TB + 2 × 960 GB NVMe** | **EUR 1,028.49 ≈ S$1,457.99/month** | One-month term selectable; no setup amount shown in this selector, final confirmation required; 1 Gbps / 25 TB, then 10 Mbps; one IPv4, IP-KVM | Arithmetic from local configurator: EUR 784.29 base + 244.20 disks. No visible unit count. Faster candidate, unmeasured CI uplift. [Source][R13] |
| Same INTROSERV 9554, **256 GB + 2 × 1.92 TB + 2 × 960 GB** | **EUR 1,428.89 ≈ S$2,025.59/month** | Same service conditions | Adds EUR 499.40 RAM and 145.20 disk options to the base. More cores than reference, but substantially more expensive. [Source][R13] |
| **INTROSERV DC4SC-a4: EPYC 9455, 48C/96T Zen 5; 128 GB + 2 × 3.84 TB + 2 × 1.92 TB** | **EUR 1,099.99 ≈ S$1,559.35/month** | EUR 855.79 setup ≈ S$1,213.17 on one-month term; 1 Gbps / 25 TB, then 10 Mbps | 256 GB + 2 × 1.92 TB alternative is EUR 1,163.79 ≈ S$1,649.79/month. Higher-generation candidate; no user CI benchmark or stock count. [Source][R14] |
| **Servers99 #25315 / DC-49: EPYC 9555P, 64C/128T Zen 5; 384 GB + 2 × 3.84 TB NVMe** | **$1,140/month; ≈ S$1,470.22 if USD** | Free setup in detailed catalogue; monthly; 1 Gbps / 30 TB; one IPv4; KVM/IPMI | Confirm invoice currency: the individual SKU shows “$” without an explicit currency label. No unit count. Candidate upgrade; not an established +10–50% CI result. [Detailed catalogue][R15], [billing][R16] |
| **DataPacket, Equinix SG3: EPYC 9555, 64C/128T Zen 5; 192 GB + 2 × 3.84 TB** | **From USD 2,110 ≈ S$2,721.19/month** | Published USD 1,891 base + 219 disks; bandwidth selection can add cost; free setup/pay-as-you-go per FAQ | Selector displayed three units and 48-hour delivery; no reservation was made. 384 GB + 2 × 1.92 TB hardware subtotal is USD 2,650 ≈ S$3,417.61. High-cost option with more visible inventory evidence. [Site][R17], [configurator][R18], [FAQ][R19] |

INTROSERV also lists a single 9454 in Singapore, with 128 GB / larger-drive configuration at EUR 1,016.39 and 256 GB / smaller-drive configuration at EUR 1,416.79, plus an observed EUR 772.19 setup. This is an additional [availability-confirmation lead][R20]; the 9554/9455 rows above had fresher selector evidence.

### Mainstream rental worker pools

| Provider | Per host | Pair price before tax | Important limit |
|---|---|---:|---|
| **DediJet Singapore** | Ryzen 9950X, 128 GB, 2 × 2 TB NVMe, 1 Gbps unmetered, one IPv4, console | **USD 538 ≈ S$693.84/month**; USD 269 each, zero setup | Monthly, crypto payment shown. “Ready” is provider-reported; two units not reserved. Each job sees one 16-core CPU and one 128 GB pool. [Source][R21] |
| PowerDedi Singapore | Ryzen 9950X, 128 GB, 2 × 1.92 TB, 10 Gbps unmetered | USD 318 ≈ S$410.11/month; USD 159 each | Same supplier/provisioning verification required as its EPYC lead; do not treat the headline as a secured two-host quote. [Source][R22] |

Compare these with the **128 GB-per-host** owned pairs, not the cheaper 64 GB-per-host budgets. The topology and per-job capacity differ from a single AX162 even when aggregate memory looks similar.

### Options excluded from a firm matched-price ranking

- [Cherry Servers Singapore 9554P][R23] showed zero stock, and the base had only 2 × 1 TB drives.
- [OVHcloud Scale-a4][R24] exposes Singapore and multiple storage options, but a fully matched location/RAM/NVMe price was not established. A generic regional “from” price is not a configured quote.
- The cheaper Servers99 9454P catalogue rows observed at $549/$969 included only **one** drive. They were not used as mirrored two-drive equivalents.
- Older dual Xeon or 16-core Ryzen plans are not declared full-throughput equivalents solely because their thread count or RAM capacity looks substantial.

## 4. Malaysia dedicated rental shortlist

| Provider / advertised physical site | Hardware | Published price and terms | Interpretation |
|---|---|---|---|
| **VPSShell, Kuala Lumpur**; building not disclosed | One EPYC 9454, 48C/96T; 512 GB; 2 × 1.92 TB NVMe; 2 Gbps; one IPv4 | **USD 1,393.99 ≈ S$1,797.78/month**, no setup; crypto-only; tax, transfer allowance and stock not established | Closest CPU/storage family to AX162-2, with more RAM. Request exact allocation and contract. [Source][R25] |
| **ServerPacket, AIMS KL2, Kuala Lumpur** | EPYC 9754, 128C/256T Zen 4c; 256 GB; 2 × 2 TB NVMe; 1 Gbps / 100 TB; one IPv4 | **USD 770 ≈ S$993.04/month starting price**, free setup per FAQ; optional management USD 39 | Location page has conflicting 50%-for-three-month promotion and crossed-out USD 2,310; generic catalogue lists USD 770. **Renewal and KL stock unresolved; not a firm TCO rate.** More cores do not prove required latency. [Source][R26], [store][R27], [FAQ][R28] |
| **DataPacket, AIMS KL2** | EPYC 9555, 64C/128T Zen 5; 192 GB + 2 × 3.84 TB NVMe | From **USD 2,110 ≈ S$2,721.19/month**, before final bandwidth/tax selection | High-core stock available upon confirmation; location selector showed conditional lead time around 21 days. Similar hardware pricing to Singapore, not an automatic Malaysia discount. [Site][R29], [configurator][R30] |
| **iDatam, Kuala Lumpur catalogue lead** | Ryzen 7950X3D, 16C/32T; 128 GB; 2 × 3.84 TB NVMe; 1 Gbps / 20 TB | USD 374 ≈ S$482.34/month; no setup advertised; unmanaged, optional management extra | Lower-throughput single-worker candidate, not a proven 48-core replacement. City assignment was corrected using the vendor's CPU-specific catalogue; require a location-confirmed quote. [Source][R31] |

ServerPacket's 64-core Zen 4c 8534P at USD 495 has 256 GB but only 2 × 1 TB. Its older 48-core Zen 2 7642 also has undersized disks. Neither is a valid capacity/performance match at the headline price. No full AX162-equivalent Malaysian rental at a lower guaranteed all-in price was established in this investigation.

For Johor specifically, [Zenlayer's city page][R32] offers custom/bulk enquiries but does not establish generally available local bare-metal stock. [Equinix JH1][R33] is a quote-only colocation lead. Being nearer Singapore can matter for physical servicing, but those pages do not supply an orderable matched-price configuration.

## 5. Singapore colocation

| Provider | Published service | Suitability for the proposed owned machine |
|---|---|---|
| **IT Block** | 1U from S$170/month, or S$150/month on 12 months; selected towers considered | **Tower price is quote-only.** Do not apply the 1U figure to Meshify 2 XL. Get exact space, sustained/peak power, bandwidth, IPs, taxes and hands. [Source][R34] |
| **QUAPE** | 1U S$280 / 0.3 kVA; 2U S$350 / 0.5 kVA; **5U S$680 / 0.8 kVA**, ex GST; 100 Mbps shared; 5U includes six IPv4 | 5U becomes **S$741.20 including 9% GST**. Needs a rack chassis and approval; space limited and enquiries required. Setup/hands extra if charged. Power is bundled; do not add office electricity. [Source][R35] |
| Ascenix | 10U S$800/month + S$500 setup, ex GST; 0.5 kW; 100 Mbps shared; eight IPs; 24-month minimum | S$872/month and S$545 setup with 9% tax. Tower acceptance and peak load still need confirmation. [Source][R36] |
| Exabytes | 1U S$191.84/month or annual-plan equivalent S$172.80; 2U S$299.75 or S$270 on annual plan; **125 W included** | Included power is below the modeled workstation load; 16 A socket rating is not the allowance. Requote rack fit, power, bandwidth split, tax and setup. [Source][R37], [features][R38] |

These network allocations are not interchangeable with Hetzner's 1 Gbps connection. A shared 100 Mbps plan can materially affect image pulls, artifact uploads and remote caches. Benchmark the real registry and network path rather than assuming the nearest city gives the fastest complete pipeline.

### Rack conversion

The [Meshify 2 XL][R39] measures 600 × 240 × 566 mm. A nominal 5U slot is 222.25 mm high, smaller than even its narrowest dimension; usable rack width also matters. Use an approved tower service or a real rack chassis.

- [SilverStone RM51 5U][R40]: S$624. Manufacturer data gives 181 mm cooler clearance with retainer, sufficient nominal height for the 145 mm Freezer 4U-M. Exact board/standoff/airflow fit still needs assembly verification.
- [RMS05-22 rails][R41]: S$159; confirm rack compatibility. Do not assume rails are bundled with the chassis.
- For a **new** system replacing the S$302.40 tower case, the RM51-plus-rails hardware increment is **S$480.60**. Retrofitting an already purchased tower has a different cash cost.
- [RM44 4U][R42]: S$469, with 148 mm cooler clearance only after removing the card retainer. It is a conditional option for a 4U quote; the 145 mm cooler leaves only 3 mm nominal clearance.

The TCO file uses a 5U Singapore scenario and separately labels Malaysia's 4U/tower cases as conditional floors.

## 6. Malaysia colocation

| Provider / location | Published plan | Material unresolved items |
|---|---|---|
| **AwanPrime, Menara AIMS, Kuala Lumpur** | **4U RM550/month ≈ S$172.48**; **460 W**; 100 Mbps unmetered on shared 1 Gbps port; two IPv4; standard hands | Rackmount, no ordinary-tower acceptance advertised. Confirm non-ECC workstation acceptance, peaks below contracted power, exact 4U case, setup/tax and chargeable repairs. One allocation cannot automatically house both desktop runners. [Source][R43] |
| **ServerHosting.MY, CX2 Cyberjaya** | Explicit **4U/tower** plan from **RM599/month ≈ S$187.84 + RM100 setup ≈ S$31.36**; 100 Mbps guaranteed/unmetered; one IPv4; remote reboot | A 13 A socket is shown, **allowed watts are not**. Dimensions, non-ECC acceptance, power cost/overage, tax and hands must be quoted. Generic terms can create an annual obligation despite monthly advertised prices. [Product][R44], [terms][R45] |
| GB Network, CJ1 Cyberjaya | 4U RM650/month + RM300 setup; **200 W**; shared 1 Gbps; two IPv4 | Published power is below the 350 W model before peak allowance. More power by quote; visits need notice. Not a valid price for the full workload without an upgrade. [Source][R46] |

Malaysia's colocation price leads are substantially lower than the quoted Singapore 5U plan, but they are not complete approved quotes for this build. Include cross-border delivery/return logistics if buying in Singapore, local technician arrangements, spare parts and any incremental tax. Ordinary tower eligibility and non-ECC RAM policy were not affirmatively established for a particular completed machine.

## 7. Malaysian local-purchase cross-check

A separate locally sourced **two-host Intel configuration** was found. This is not merely the Singapore price converted into MYR. It has the same 64 GB-per-host topology, but different board, SSD, cooling and case selections. It remains subject to exact RAM qualification, BIOS, thermal testing, stock quantity and a complete quote.

| Part per host | MYR | Local source |
|---|---:|---|
| Intel Core Ultra 7 270K Plus | 1,499 | [E Cytech][R47] |
| MSI PRO B860M-A WiFi6E | 699 | [E Cytech][R48] |
| TeamGroup T-Create Expert 2 × 32 GB DDR5-6000 CL34 | 4,399 | [ALL IT][R49] |
| Two Samsung 990 PRO 2 TB, RM2,335 each | 4,670 | [Gloo / SNS][R50] |
| Thermalright Phantom Spirit 120 Digital EVO | 259 | [E Cytech][R51] |
| Cooler Master Elite 301 | 209 | [E Cytech][R52] |
| MSI MAG A650GL PSU | 269 | [E Cytech][R53] |
| **One host / two hosts** | **12,004 / 24,008** | **Pair ≈ S$7,528.76** |

The pair is only about S$50 above the Singapore S$7,479.20 parts example, before differing delivery/tax/assembly arrangements. This sample does not establish that either entire country's market is cheaper. Buy where support and physical servicing are practical. The 160 mm cooler has little margin under the case's stated 163.5 mm limit; validate RAM/fan clearance and sustained cooling. No complete Malaysia-priced 5995WX/WRX80 non-ECC bill of materials was verified.

## 8. Electricity sources for ownership scenarios

**Singapore:** [SP's Q4 2026 tariff][R54] is S$0.2859/kWh before GST or **S$0.3116/kWh including GST**, effective 1 October–31 December. Use the actual office/landlord/retailer marginal tariff if different. The regulated rate is a reference, not proof of eligibility for every business account.

**Peninsular Malaysia commercial LV General:** the [published schedule][R55] has energy 27.03, capacity 8.83 and network 14.82 sen/kWh, plus RM20/month retail per account. [November AFA][R56] adds 3.60 sen/kWh. [TNB's levy calculation][R57] applies 1.6% to the first three components, excluding AFA and retail. The model's existing-meter marginal rate is **RM0.5509088/kWh**. The fixed retail charge is extra only if a new account is required. Commercial billing is not modeled using household exemptions; [Customs' electricity service category][R58] is relevant when confirming invoice treatment.

At the illustrative 350 W average wall load, 730 hours/month and 25% separate cooling overhead, energy is **S$99.52/month in Singapore versus RM175.95 ≈ S$55.18 in Malaysia**. The Malaysian calculation includes the levy and AFA but is prior to any additional invoice-specific tax. These are calculated sensitivities, not measured machine power or guaranteed future tariffs. The detailed model follows in [03-rent-vs-buy-tco.md](03-rent-vs-buy-tco.md).

## Source links

[R01]: https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html
[R02]: https://www.amd.com/en/products/processors/server/epyc/4th-generation-9004-and-8004-series/amd-epyc-9454.html
[R03]: https://www.hetzner.com/dedicated-rootserver/ax162/
[R04]: https://docs.hetzner.com/cloud/general/locations/
[R05]: https://docs.hetzner.com/general/infrastructure-and-availability/price-adjustment/
[R06]: https://docs.hetzner.com/general/infrastructure-and-availability/ipv4-pricing/
[R07]: https://docs.hetzner.com/general/infrastructure-and-availability/order-processing/
[R08]: https://www.hetzner.com/dedicated-rootserver/ax162/configurator/
[R09]: https://www.hetzner.com/pressroom/standardization-and-price-adjustment-of-our-server-products/
[R10]: https://docs.hetzner.com/general/billing-and-account-management/cancellation/cancellations-robot/
[R11]: https://powerdedi.com/order?loc=SIN&plan=e-9454p
[R12]: https://ultahost.com/dedicated-server-singapore
[R13]: https://introserv.com/order/dc4sc-a5-ae9554-sg/
[R14]: https://introserv.com/order/dc4sc-a4-ae9455-sg/
[R15]: https://ds.servers99.com/dedicated-server/asia/singapore/
[R16]: https://www.servers99.com/billing/store/ingapore-edicated-ervers
[R17]: https://www.datapacket.com/datacenters/singapore
[R18]: https://www.datapacket.com/server-configuration?cpu=1~14dauhf&location=singapore&region=asia-pacific
[R19]: https://www.datapacket.com/faq
[R20]: https://introserv.com/order/dc4sc-a4-ae9454-sg/
[R21]: https://dedijet.com/order/ryzen-9-9950x?loc=sin
[R22]: https://powerdedi.com/locations/singapore
[R23]: https://www.cherryservers.com/pricing/dedicated-servers/amd-epyc-9554p?region=sg-singapore
[R24]: https://www.ovhcloud.com/en-au/bare-metal/scale/scale-a4/
[R25]: https://www.vpsshell.com/malaysia-dedicated-server/
[R26]: https://www.serverpacket.com/malaysia-dedicated-server/
[R27]: https://app.serverpacket.com/store/dedicated-servers
[R28]: https://www.serverpacket.com/faq/
[R29]: https://www.datapacket.com/datacenters/kuala-lumpur
[R30]: https://www.datapacket.com/server-configuration?cpu=1~14dauhf&location=kuala-lumpur&region=asia-pacific
[R31]: https://www.idatam.com/dedicated-servers-malaysia/
[R32]: https://cloud.zenlayer.com/datacenters/johor-bahru
[R33]: https://www.equinix.com/data-centers/asia-pacific-colocation/malaysia-colocation/johor-data-center/jh1
[R34]: https://www.itblock.sg/single-server-colocation-singapore
[R35]: https://www.quape.com/servers/colocation-server/
[R36]: https://www.ascenix.net/?p=colo
[R37]: https://www.exabytes.sg/servers/colocation
[R38]: https://www.exabytes.sg/servers/colocation/single-server-features
[R39]: https://www.fractal-design.com/app/uploads/2020/10/Meshify-2-XL-_Product-Sheet_EN.pdf
[R40]: https://dynacoretech.com/products/silverstone-rm51-5u-rackmount-server-chassis-support-up-to-ssi-eeb-black-sst-rm51
[R41]: https://dynacoretech.com/products/silverstone-rms05-22-tool-less-ball-bearing-sliding-rail-kit-sst-rms05-22
[R42]: https://dynacoretech.com/products/silverstone-rm44-4u-rackmount-server-chassis-with-enhanced-liquid-cooling-capability-sst-rm44
[R43]: https://awanprime.com/colocation
[R44]: https://clientarea.serverhosting.my/cart.php?gid=7
[R45]: https://www.serverhosting.my/terms/
[R46]: https://www.gbnetwork.my/servers/colocation/
[R47]: https://www.ecytech.com.my/product-page/intel-core-ultra-7-270k-plus
[R48]: https://www.ecytech.com.my/product-page/msi-pro-b860m-a-wifi6e
[R49]: https://www.allithypermarket.com.my/products/teamgroup-t-create-expert-ddr5-6000mhz-cl34-desktop-ram-64gb32gbx2
[R50]: https://www.gloo.com.my/SMB-PC-Components/SAMSUNG-990-PRO-2TB-PCIe-4.0-NVMe-M.2-SSD
[R51]: https://www.ecytech.com.my/product-page/thermalright-phantom-spirit-120-digital-evo
[R52]: https://www.ecytech.com.my/product-page/cooler-master-elite-301
[R53]: https://www.ecytech.com.my/product-page/msi-mag-a650gl
[R54]: https://www.spgroup.com.sg/our-services/utilities/tariff-information
[R55]: https://myenergystats.st.gov.my/documents/d/guest/jadual-tarif-tnb-terkini
[R56]: https://www.st.gov.my/AFA
[R57]: https://mra.com.my/wp-content/uploads/2025/07/New-RP4-Electricity-Tariff-Structure-Now-in-Effect-%E2%80%93-What-Retailers-Should-Know.pdf
[R58]: https://mysst.customs.gov.my/registering-business/
[R59]: https://www.hetzner.com/_resources/app/data/app/live_data_prices.json
[R60]: https://www.hetzner.com/_resources/app/data/app/live_data_upfront.json
