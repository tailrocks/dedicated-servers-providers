# Further dedicated server options and price corrections — 20 November 2026

[Home](../README.md) · [Current rental catalog](../rentals/README.md) · [Research archive](README.md)

**Evidence date:** 20 November 2026, Asia/Ho_Chi_Minh. Checks also fall on 19 November UTC. This report continues the 170-offer inventory at commit `5b26e01` and preserves the repository's new rental/ownership navigation. The separate ownership calculations remain tied to their documented 141-offer snapshot.

## What this pass adds

The catalog now contains **195 hardware and billing variants from 78 alternative seller brands plus Hetzner**. This pass adds **25 rows**: 24 across **12 new seller brands**, plus one materially different UHost storage configuration. Seventeen added rows use the exact 9454P; six use the independently benchmark-supported non-P 9455 and two use the 9455P. All 170 existing offers are retained. UHost's base listing was freshly rechecked and its date updated; the prior dated reports remain intact.

These are the main additions, grouping term variants instead of presenting every payment period as a different seller. Converted prices are comparative USD amounts; actual invoices remain in the stated currency. **†** retains a seller's tax-inclusive quote. A year figure with unknown setup is rent only.

| Seller / configuration | CPU / RAM / NVMe | Monthly USD comparison | Setup and first-year or prepaid cost | Evidence and material qualification |
|---|---|---:|---|---|
| [040Hosting 7-NVME24](https://www.040support.nl/client/index.php/store/umanaged-servers-50) | 9454P / 256 GB / 2 × 1.92 TB | **~$262.71** | €239/mo + €95 setup; €2,963 first year (~$3,256.93), ex VAT | Legacy billing catalog and exact price feed; domain step reached, no complete invoice. Current distinct 7-NVME26 is €989. Confirm supply of this older SKU. |
| [UHost with additional NVMe pair](https://uhost.online/en/dedicated/19) | 9454P / 256 GB / 2 × 1.92 + 2 × 3.84 TB | **$306.00** | +$120 setup; $426 initial; $3,792 first year before unknown tax | Published upgrades and matching cart total. Added disks are not itemized in the cart; actual RAID and allocation remain unconfirmed. |
| [Quicservers](https://quicservers.com/dedicated-servers/dedicated-servers-finland/) | 9454P / 256 GB / 2 × 1.92 TB | **~$343.00** | INR 32,000/mo, free setup; INR 384,000 annual rent (~$4,115.97) | Finland/Germany advertised; callback only. Tax, foreign payment eligibility, exact port and stock unknown. |
| [COLO BIRD, Helsinki](https://billing.colobird.com/store/elsinki-edicated-ervers-inland) | 9454P / 256 GB with 2 × 1.92 TB; or 128 GB with 2 × 3.84 TB | **$363 / $366** | 256 GB: +$1,496.35 setup, $5,852.35 first year. 128 GB: +$1,134.69, $5,526.69 first year | Both selected DDR5 carts match. Higher setup makes the $366 configuration cheaper over the first year. Tax and allocation unknown. |
| [W3 DATA](https://www.w3data.cloud/cart.php?a=add&pid=666&billingcycle=monthly) | 9454P / 256 GB / 2 × 1.92 TB | **$365.12†** | +$139.14 setup; $504.26 initial; $4,520.58 first year | Selected product data and totals, Stripe payment option. Terms include VAT; US-default calculation adds zero. Two identical product IDs consolidated. Location and allocation unknown. |
| [TRAIDNT GROUP](https://manage.traidnt.com/store/dedicated-servers/t-server4) | 9454P / 256 GB / 2 × 1.92 TB | **~$399.87** | SAR 1,500/mo + SAR 2,000 setup; SAR 3,500 initial; SAR 20,000 first year (~$5,331.63) | Exact matching selected totals; two indistinguishable SKUs consolidated. The Saudi seller's address and SAUDI S5 name do not establish physical location. |
| [TezHost AMD Power 4](https://client.tezhost.com/cart.php?a=add&pid=204&billingcycle=monthly&currency=1) | 9454P / 256 GB / 2 × 1.92 TB | **$400.00 net** | +$700 setup; $5,500 net first year. Calculator adds 5%: $1,155 initial / $5,775 annual due | Exact selected configuration and totals; no annual rent discount. Location and stock unknown. |
| [99RDP, annual](https://portal.99rdp.com/store/new-plan-launch) | 9454P / 128 GB with 2 × 3.84 TB; or 256 GB with 2 × 1.92 TB | **$422.99 effective** | $5,075.89 paid per 12-month term, no setup added in selected calculation | Both hardware variants have the same current price. Monthly $449.99; quarterly and six-month discounts also documented. Tax extra; location and stock unknown. |
| [COLO BIRD, Warsaw](https://billing.colobird.com/cart.php?a=add&pid=42212) | 9455P / 128 GB / 2 × 1.92 TB | **$448.00** | +$708 setup; $1,156 initially; $6,084 first year | Selected cart; exact P-suffix CPU. No RAID selected; tax and allocation unknown. |
| [Capa7 XL](https://www.capasiete.com/en/servidores-dedicados) | 9455 / 128 GB / 2 × 1.92 TB | **$499.95** | $5,999.40 for twelve monthly rents, before unknown setup/tax/fees | Quote-only. Published 15% annual discount implies $5,099.49 rent (~$424.96/mo), but no complete annual invoice. MercadoPago carries a stated 10% fee. |
| [Visual Web DED-CA 7](https://www.vwt.net/serversca.html) | 9455P / 128 GB / 2 × 1.92 TB | **$537.00** | Free setup; $6,444 annual rent before unknown tax | Montreal, one-month minimum, shared unmetered 1 Gbps network; contact-only, stock unconfirmed. |
| [BPHOST DEDI 4](https://www.bphost.biz/my/cart.php?a=add&pid=101&currency=1&billingcycle=monthly) | 9455 / 128 GB / 2 × 1.92 TB | **~$578.63** | ZAR 9,999/mo + ZAR 5,999 setup; ZAR 125,987 first year (~$7,290.67) before buyer-specific VAT | Matching cart; Gravelines selected. Both advertised coupon codes were rejected for this SKU. Terms denominate prices in ZAR; USD display is not verified USD settlement. |
| [DV Hosting, 24-month term](https://dvhosting.in/dedicated-server.php) | 9455 / 128 GB / 2 × 1.92 TB | **~$578.80 net** | INR 1,295,978.40 net plus 18% GST = **INR 1,529,254.51 upfront for 24 months**, zero setup | Selected public calculator; four distinct rate/setup structures retained. Gross equivalent ~$682.98/mo exceeds Hetzner's net comparison. No allocation verified. |
| [Websupport.cz Dell S5, annual](https://www.websupport.cz/cart/server/?period=12&uuid=01fc8b28-a06a-43ae-9537-2a21a7f6cb5c) | 9454P / 256 GB / 2 × 1.92 TB NVMe plus 2 × 480 GB SSD | **~$671.71 net** | Exact public configuration data: CZK 179,124 per 12 months; setup unknown | Only €1.21/month below the reference. API resolves the previously missing annual amount, but the order remains contact-based and the final invoice/stock is unconfirmed. |

The [exact-CPU report](2026-11-20-further-options-exact-cpu.md) records every 99RDP cycle, W3 DATA's tax terms, 040Hosting's two different generations and Websupport's recovered price data. The [regional report](2026-11-20-further-options-global.md) records Quicservers, TRAIDNT and the Teleserve/Mostdeef/Sahaba conflicts. The [newer-CPU report](2026-11-20-further-options-newer-cpu.md) records every selected DV total, COLO BIRD configuration and BPHOST coupon rejection. The BPHOST currency wording was corrected in independent review: the USD selector does not override rand-denominated terms.

## Cheap leads withheld and follow-up priorities

The pass did **not** establish a new lower net monthly price than Arxan's existing ~$212.74 comparison. The closest new headline was Teleserve's separate INR tariff (~$215.45), but its fresh product-site requests returned HTTP 503 and the available primary snapshot was three weeks old. Its $239 native USD tariff is preserved in the regional report as a lead, not ranked as currently orderable. 040Hosting's €239 is the lowest newly added published catalog amount, with the legacy-SKU limitation stated.

Mostdeef's older implied $250 price did not survive verification: its current cart quotes $395.99 but its linked sales page names a different CPU, and its $2/$4 long-term calculator totals conflict with its published four-figure term prices. Sahaba's $410 card points to an explicitly empty store. RoyalCloud has replaced the indexed AZN 590 amount with an unpublished price. These are useful corrections, not additional confirmed bargains.

The next checks should prioritize fresh Teleserve accessibility, 040Hosting's legacy SKU availability, any correction to Mostdeef's CPU and term data, and complete quotes for the strongest existing low-cost offers. Lower COLO BIRD DDR4-labelled listings and tagDiv's unspecified drive medium require corrected primary hardware evidence. Seller responses or actual hardware allocation would require a separately authorized procurement step.

## Scope and reference recheck

The requirements remain a whole physical server, CPU performance at least in the EPYC 9454P class, at least 128 GB installed RAM and at least 2 TB raw SSD capacity. A supplier's quoted 2 × 1.92 TB NVMe layout meets the raw floor but yields only 1.92 TB nominal when mirrored. A matching catalog, cart or calculator is evidence of a published offer, not an allocated physical unit. No account was registered, supplier contacted, order submitted or hardware reserved.

The [Hetzner public live price feed](https://www.hetzner.com/_resources/app/data/app/live_data_prices.json) still returns product `ROBOT_1724` at **€612.30/month + €304 setup**, with a separate **$722.10/month + $359 setup** tariff, for NBG1, FSN1 and HEL1. The EUR first-year subtotal remains €7,651.60 before VAT and IPv4. At the dated ECB EUR/USD 1.0992 comparison rate, that is **$673.04/month and $8,410.64 in year one**. These conversions are distinct from Hetzner's native USD tariff.

## UHost: additional NVMe pair on the less expensive base

The [AX162-R configurator](https://uhost.online/en/dedicated/19) was rechecked at **$220/month + $120 setup** in Helsinki, with an EPYC 9454P, 256 GB DDR5 ECC and 2 × 1.92 TB Gen4 NVMe in software RAID 1. Falkenstein adds $4/month. One IPv4 is priced at $0 in the selected form. The public billing-period calculation applies no discount for paying 3, 6 or 12 months.

The same configurator offers an **additional 3.84 TB datacenter NVMe for $43/month per drive**. Selecting two gives:

| Item | USD |
|---|---:|
| Base server, monthly | 220.00 |
| Two additional 3.84 TB NVMe drives, monthly | 86.00 |
| Combined recurring monthly amount | **306.00** |
| Setup, once | 120.00 |
| Initial cart total | **426.00** |
| Calculated first-year subtotal | **3,792.00** |

An ordinary anonymous submission of the published configuration to the cart returned **$426.00** for one AX162-R. The cart's description repeats the base CPU, 256 GB and 2 × 1.92 TB; it **does not itemize the additional disks**. The row is therefore labelled a public configuration with a matching cart total, rather than a fully itemized issued invoice. The four-drive layout is **11.52 TB raw**. The additional pair could provide 3.84 TB nominal if mirrored, but the selected RAID layout and actual drive allocation have not been confirmed. Taxes, port speed, traffic allowance, final supply and customer-specific payment acceptance remain unresolved.

## TezHost: matching AMD Power 4 configuration

The [AMD Dedicated Server catalog](https://client.tezhost.com/index.php/store/amd-dedicated-server?language=english) identifies product **204, AMD Power 4**. A fresh anonymous session using its [numeric monthly USD order link](https://client.tezhost.com/cart.php?a=add&pid=204&billingcycle=monthly&currency=1) reached the matching selected hardware: **EPYC 9454P, 48 cores with SMT, 256 GB DDR5 ECC registered RAM, 2 × 1.92 TB Gen4 NVMe and a 1 Gbps port**. Linux is free; Windows and commercial control panels are optional. The [dedicated service description](https://tezhost.com/dedicated-server/) describes an exclusive physical machine, root access and a dedicated IP. This SKU does not establish the physical datacenter or traffic allowance.

The public selected-price calculation gave:

| Billing term | Rent | Setup | Calculator tax | Initial due |
|---|---:|---:|---:|---:|
| Monthly | $400.00 | $700.00 | $55.00 at 5% | **$1,155.00** |
| Annual | $4,800.00 | $700.00 | $275.00 at 5% | **$5,775.00** |

Quarterly, semiannual, biennial and triennial selectors also retain the $400 monthly equivalent and $700 setup. There is no lower recurring term to add as a separate row. The net first-year subtotal is **$5,500**; applying the same observed 5% tax throughout gives **$5,775**. A buyer's actual tax can differ: [seller terms](https://tezhost.com/terms-of-services/) say localized taxes may depend on billing details. [Payment methods](https://tezhost.com/payment-methods/) advertise international cards, PayPal, Wise, bank transfer and cryptocurrency, as well as Pakistani payment methods. These are general methods, not confirmation that every buyer or this exact invoice can use each route. The [promotion page](https://tezhost.com/coupons-and-promotions/) currently says no active coupons. No stock quantity or guaranteed allocation was established.

The storefront also displayed a generic service-impact warning. Its [status-details link](https://client.tezhost.com/serverstatus.php) requires sign-in. The affected service and relevance to AMD Power 4 could not be determined; this is not evidence of an outage on this particular dedicated product.

## Cheapest existing offers rechecked

- [Arxan's dedicated catalog](https://hosting.arxan.app/store/dedicated-server) still lists its 9454P / 256 GB / 2 × 1.92 TB offer at IDR 3,885,000/month plus IDR 1,510,000 setup. This pass did not repeat the preceding pass's full tax/payment checkout. Its already recorded **~$212.74 net monthly comparison**, observed 11% PPN, and unresolved international payment/location/stock remain as documented in the [prior Arxan check](2026-11-20-more-options.md#arxan-lowest-configured-net-quote-with-a-visible-tax-and-payment-distinction).
- [Nindohost's explicit USD catalog](https://nindohost.co.zm/servers/dedicated/?currency=USD) still shows **$234/month** for 256 GB / 2 × 1.92 TB and **$450/month** for 128 GB / 2 × 3.84 TB. Those remain quote-only German offers; no new setup, tax, network, stock or payment confirmation was recovered.
- UHost's unchanged base price and newly checked upgrade are recorded above. Rechecking the same price does not add another duplicate base row.

## Root checks that do not enter the qualified ranking

| Provider / source | Observed evidence | Decision |
|---|---|---|
| [Aminserve](https://aminserve.com/dedicated) | The old indexed `standard-servers.php` lead redirects to the current catalog. The catalog's public [JavaScript product data](https://aminserve.com/catalog.js?v=b863f8736e) contains no 9454P, 9455/P, 9474F, 9555/P, 7980X or 7995WX offer. The linked [German live stock feed](https://aminserve.com/api/de-stock) returned 12 older Core, Xeon W and Ryzen configurations, none meeting the CPU floor. | An old CPU snippet is insufficient. No matching current tariff was recovered. Only catalog/stock reads were performed; the separate allocation/order endpoints were not invoked. |
| [RoyalCloud RC-9 / RC-10](https://royalcloud.az/servers?lang=en) | Search indexes retain **AZN 590/month** for 9454P / 128 GB / 2 × 3.84 TB and 256 GB / 2 × 1.92 TB. The freshly linked [server-page bundle](https://royalcloud.az/_next/static/chunks/app/servers/page-87482f7137276f7d.js) retains those specifications but sets both prices to `null`, displaying a telephone price inquiry instead. | Current price is unpublished. Do not promote the old AZN 590 amount to a live ~$347.06 offer. That historical conversion uses the [Azerbaijan central bank's 19 November rate](https://www.cbar.az/currency/rates?language=en), USD 1 = AZN 1.7000; it does not establish a payable USD tariff. |
| [Magyar Hosting / Websupport Hungary, Dell S5](https://www.mhosting.hu/dedikalt-szerver-berles/) | HUF 209,000/month before 27% VAT with a one-year contract, 256 GB DDR5, 2 × 1.92 TB NVMe plus two 480 GB boot SSDs, redundant 1 Gbps links and one IP. A normal cookie-preserving [selected cart](https://online.mhosting.hu/index.php?rp=/store/szerver-berles-1/dedikalt-szerver-dell-s5) works, but both it and the marketing page say **2 × EPYC 9454P in a Dell R6615**. | Hardware inconsistency remains: [AMD specifies the 9454P for a single socket](https://www.amd.com/en/products/processors/server/epyc/4th-generation-9004-and-8004-series/amd-epyc-9454p.html). Do not silently substitute a different processor or fix the seller's CPU count. A cookie-less redirect to shared hosting is superseded by the matching cart, but the CPU discrepancy is unresolved. |
| [Advanced Hosting](https://advancedhosting.com/high-performance-dedicated-servers/) | Search indexing retains a 9454P / 256 GB / 2 × 960 GB NVMe tier at €890/month. Fresh page retrieval no longer contains a 9454P offer; its rendered profile text instead covers older Xeons and an EPYC 9254 configuration. | No matching current quote. The indexed amount also exceeds the ceiling and its 1.92 TB raw storage is below the floor. Do not carry an old indexed card into the current catalog. |
| [Qentra](https://qentra.pro/en/dedicated) | Indexed 9454P offers show $1,000/month + $500 setup for 128 GB / 2 × 4 TB, and $1,300 + $600 for 256 GB / 2 × 1.92 TB. Fresh direct retrieval returned HTTP 503; the web fetch timed out. | Indexed prices exceed the reference and current live pricing remains unverified. No qualifying addition. |
| [EcuaHosting / Partnerts](https://supersite.website/servidores-dedicados-en-alemania/) | The $299 + $99 AX162-R/S pages were found again. The S still says DDR4 and the linked contract still calls the named products virtual dedicated servers. | Already documented in the [earlier regional report](2026-11-20-follow-up-global.md). No correction of physical exclusivity or the S memory type was established. |
| [NODYNA](https://nodyna.com/en/servers) | €299.99 including tax, 9454P / 256 GB / 2 × 3.84 TB, but the dedicated range and exact Enterprise card both remain marked coming soon. | Existing unavailable lead, rechecked without change. |
| [RBB Host](https://rbbhost.com/pricing) | Exact 9454P / 128 GB / 2 × 1.92 TB remains €799/month before VAT. | Above the ceiling. Its cheaper cloud and Ryzen tiers do not satisfy this comparison. |
| [ABCD.HOST's older €495 promotion](https://blog.abcd.host/gorjachie-vydelennye-servery-v-evrope-luchshie-predlozhenija-po-cene-kachestvu/) | Search rediscovered an August 2026 limited-supply announcement, alongside the previously recorded newer, higher regular tariffs and unavailable RISE-XL feed. | No new offer. Preserve the [earlier current-catalog correction](2026-11-20-global.md) and [seller-specific inventory result](2026-11-20-more-options-newer-cpu.md). |

All prices and evidence above describe the checked pages, not a promise of future stock or a determination of the buyer's tax liability.
