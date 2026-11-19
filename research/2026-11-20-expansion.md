# More dedicated-server sellers — 20 November 2026 expansion

Research date: **2026-11-20, Asia/Ho_Chi_Minh**; retrievals took place on 19 November UTC. This pass continues the previous 119-row comparison. It adds **22 rows from eight additional seller brands**, updates an existing PowerDedi promotion, and preserves every earlier offer and evidence file. The current comparison has **141 rows: 55 alternative seller brands plus Hetzner**. Rows include materially different RAM/storage and payment terms; they are not counts of independently available physical machines.

The requirements remain a whole physical dedicated server, CPU performance at least in the EPYC 9454P class, at least 128 GB RAM and at least 2 TB **raw** SSD. An exact 9454P is preferred for an unambiguous CPU-model match. All accepted new rows use that CPU or the separately benchmark-supported non-P EPYC 9455. No VPS or dedicated-vCPU offer was admitted.

## What this pass adds

| Additional seller | Lowest new recurring / effective monthly amount | Qualifying configuration | Evidence and material qualification |
|---|---:|---|---|
| Wsla Technology | **$289.99**, monthly | 9454P, 256 GB DDR5 ECC, 2 × 1.92 TB NVMe | +$99 setup; product-specific domain-selection gate; deployment location and stock unknown |
| ServerWala, Helsinki | **$301.50** on annual prepayment; **$335** monthly | 9454P, either 128 GB / 2 × 3.84 TB NVMe or 256 GB / 2 × 1.92 TB NVMe | Selected annual carts show $3,618 upfront and $0 setup; monthly carts show $335 due; shared 1 Gbps port, 20 TB |
| HOSTING.WORKS, Finland | **~$362.73**, monthly | 9454P, either 128 GB / two nominal 4 TB NVMe or 256 GB / two nominal 2 TB NVMe | Published €329.99 +€119.99 setup; product-specific EUR data; final invoice, tax and stock unconfirmed |
| IpServer.su, France / Canada | **~$384.71** annual equivalent; **~$391.30** monthly | 9455, 128 GB DDR5 ECC, 2 × 1.92 TB NVMe | €4,199.88 annual rent +€344.99 setup; or €355.99/month +same setup; stock unconfirmed |
| Alpenhost, Vienna | **~$384.71†**, 36-month prepayment | 9454P, 256 GB DDR5 ECC, 2 × 1.92 TB NVMe | €12,599.64 due for 36 months; actual selected cart; † gross quote retained, VAT split unknown |
| Cheap Ai Servers | **$439.99**, monthly | 9454P, 128 GB DDR5 ECC, 7.68 TB NVMe total | +$99.95 setup; listed USD/domain gate; drive count, location, stock and contracting identity unresolved |
| IDCBEST / 天下数据 | **~$525**, monthly | 9455, 128 GB, 2 × 1.92 TB SSD | CNY 3,500 before tax; displayed mid-year promotion, fulfillment and renewal unconfirmed; SSD interface not specified |
| HostingSaint | **$553.93**, monthly | 9455, 128 GB DDR5, 2 × 1.92 TB NVMe | Selected USD invoice: $0 setup, $553.93 due; Frankfurt selected; other locations are options, not allocation evidence |

These are additional choices, not a new all-time minimum. The previously recorded UHost USD offer remains $220/month in the table; no newly researched seller undercuts that published monthly rent in this pass. The earlier offer's evidence date and limitations remain unchanged. The strongest new lower-cost cart checks are ServerWala's two Helsinki hardware variants. Wsla is cheaper in rent, but its full selected invoice and physical location were not reached.

The reference remains the regular [Hetzner AX162 configurator](https://www.hetzner.com/dedicated-rootserver/ax162/configurator/), with 9454P, 128 GB and 2 × 3.84 TB NVMe. Its [live price feed](https://www.hetzner.com/_resources/app/data/app/live_data_prices.json), `ROBOT_1724`, gives €612.30/month +€304 setup, or €7,651.60 for twelve months before tax/IPv4. At the dated EUR/USD rate this is $673.04/month and $8,410.64 in year one. Lower recurring rent can still lose on setup: Alpenhost's monthly option is an example below.

## Evidence files

- [Exact 9454P regional sellers and local payment channels](2026-11-20-expansion-exact-cpu.md): HOSTING.WORKS, ServerFee, MarsAI, ShopingServer, Kariha and other checks.
- [Newer CPU sellers and a conditional Intel alternative](2026-11-20-expansion-newer-cpu.md): IpServer.su, HostingSaint, IDCBEST, DediRoom and exclusions.
- [ServerWala, Wsla and the PowerDedi promotion](2026-11-20-expansion-global.md): all four physical products, selected payment cycles, tax conditions, domain gates and regional exclusions.

## Alpenhost: actual configuration and payment-period totals

The [AMD dedicated category](https://alpenhost.at/Kundencenter/store/dedicated-server-amd) identifies AE9454P as an exact 48-core/96-thread 9454P with 256 GB registered DDR5 ECC and two 1.92 TB NVMe SSDs. The [product-specific order](https://alpenhost.at/Kundencenter/store/dedicated-server-amd/ae9454-dedicated-server) and older published [enterprise-category link](https://alpenhost.at/Kundencenter/store/enterprise-server-amd/ae9454-dedicated-server) reach the matching public configuration with normal anonymous session cookies. A cookie-less redirect to a generic category was not treated as evidence that the SKU cannot be configured.

All four quoted configurations selected **Austria, ISO27001 NDC2 Vienna**, standard RAM and storage, the included up-to-1-Gbps uplink with unlimited fair-use traffic, rescue OS, no managed service and no extra monitoring. Every selected option was free. No IPv4 allocation was established. Storage is 3.84 TB raw; a mirror has 1.92 TB nominal before filesystem overhead. The public cart's own total calculator returned these exact term amounts:

| Selected billing cycle | Actual term rent | Setup shown | Actual due today | USD recurring / effective monthly |
|---|---:|---:|---:|---:|
| Monthly | €599 | €2,493.99 | **€3,092.99** | **~$658.42†** |
| Annual, prepaid | €5,399 | €239.99 | **€5,638.99** | **~$494.55†** |
| 24 months, prepaid | €8,999 | No separate setup line | **€8,999** | **~$412.15†** |
| 36 months, prepaid | €12,599.64 | No separate setup line | **€12,599.64** | **~$384.71†** |

The amounts due for the two longer terms equal their complete displayed rent; do not invent an extra setup fee from the category's mixed-period headline. Conversely, a missing setup line is not a general contractual promise that every purchase has free setup. Annual effective rent is €5,399 / 12; the two-year equivalent is €8,999 / 24. Currency conversion uses the unrounded invoices. The 36-month quote really is €349.99/month equivalent, requiring payment for all 36 months.

The [marketing page](https://alpenhost.at/dedicated-server/) advertises €189.49; that did not match any checked selected base configuration and is **not** an accepted quote. The category's “from €349.99” and €2,493.99 setup combine different cycle fields; they must not be presented as one selected monthly tariff. Other selector-only options showed €533/month equivalent quarterly plus €1,779.99 setup and €499.83/month equivalent half-yearly plus €959 setup. Their full invoices were not recalculated; they are recorded here without extrapolating exact prepaid totals from rounded labels.

At monthly billing, twelve rents plus setup are **€9,681.99**, exceeding Hetzner's €7,651.60 first-year subtotal, even though €599 is below €612.30 in recurring rent. The annual first payment is €5,638.99. Two- and three-year prepayments are multi-year cash commitments, not first-year payments. The 2 × 2 TB upgrade was shown at an additional €5.49/month plus €1.90 setup on the monthly form; it is optional, and no equivalent upgrade invoice was verified for the prepaid cycles.

[Terms §6.4](https://alpenhost.at/allgemeine-geschaeftsbedingungen/) describe gross prices including applicable VAT unless otherwise specified. No rate or tax split was separated in the quote. The comparison retains the full displayed amount with **†**, rather than removing an assumed Austrian tax percentage. The terms align the dedicated-server term with the payment interval; the general cancellation notice is 30 days to month end, subject to the agreed term. The [dedicated-order knowledge base](https://alpenhost.at/Kundencenter/knowledgebase/36/Order-processing.html) explicitly identifies physical machines and manual provisioning, with a typical 24-hour to seven-day range depending on availability. No specific 9454P stock quantity was found. Availability badges on other processors are not evidence for this SKU.

The stated operator is Alpenhost e.U., Vienna. Generic shared/virtual-hosting terms and stray marketing text are not substituted for the specific physical dedicated SKU and its ordering guidance. The final accepted order and applicable term still govern.

## Cheap Ai Servers: one consistent qualifying listing

The [physical dedicated-server page](https://cheapaiservers.com/dedicatedservers.html) describes single-tenant bare metal. Its **Elite Dedicated Server 10** is an exact 9454P with 48 physical cores, 128 GB DDR5 ECC and 7.68 TB NVMe total. The [live billing category](https://cheapaiservers.com/billing/index.php?rp=/store/amd-ryzen-dedicated-server) independently shows **$439.99 USD monthly +$99.95 setup**, one primary IPv4, IPv6 /64, full root access, 1 Gbps and unlimited traffic with an asterisk. Drive count and RAID layout are not given; do not assume two 3.84 TB drives. The physical server location is unspecified.

The calculated first payment is **$539.94**, and twelve rents plus setup are **$5,379.83**, before unknown tax. The [PID 54 order link](https://cheapaiservers.com/billing/cart.php?a=add&pid=54) reaches the seller's matching product slug and a domain selection screen in a normal anonymous session. No domain was submitted; final invoice and allocation are unverified. Listing classification is **LISTED / DOMAIN STEP**, not cart-verified delivery. The [terms](https://cheapaiservers.com/tos.html) retain an unfilled jurisdiction placeholder and did not establish a full contracting entity. This is recorded as an unresolved commercial limitation, not evidence of misconduct.

**Elite Dedicated Server 11 is withheld.** Its category says 256 GB DDR5, but the marketing card says DDR4 alongside the DDR5-only 9454P. Its $439.99 price and 3.84 TB NVMe would otherwise qualify; the contradictory product-specific RAM remains unresolved. The 128 GB product 10 does not show that contradiction.

## PowerDedi: first-month reduction, unchanged renewal

The [same previously listed 9454P configuration with BIRTHDAY20](https://powerdedi.com/order?plan=e-9454p&promo=BIRTHDAY20) explicitly calculates **$391.20 due for month one**, after a $97.80 discount, then **$489/month**. Setup is $0. The checked Amsterdam configuration retains 256 GB DDR5 ECC, 2 × 3.84 TB NVMe and advertised unmetered 10 Gbps. Twelve payments total **$5,770.20** before unknown tax. The existing row is updated; no artificial $391.20 recurring row is added.

The current banner window ends at 08:00 UTC / 15:00 Vietnam on 20 November. Its public data implement cycling windows and did not establish a contractual final expiration. It is a currently applied one-time introductory reduction, not a guaranteed permanently available coupon. The earlier unresolved operator, crypto-funded balance and stock limitations remain visible. See the [regional evidence file](2026-11-20-expansion-global.md) for the exact quote and cycle details.

## Other excluded and unresolved offers

| Seller / source | Observed offer or problem | Decision |
|---|---|---|
| [Horizons Direct](https://horizons.direct/metal) | Public [plans API](https://horizons.direct/api/v1/plans) lists 9454P/384 GB/2 × 3.84 TB NVMe/10 Gbps/100 TB at $459 and 768 GB at $589, $0 setup | Public login/signup behavior is simulated; production network identity is inconsistent. Do not treat as an established purchasable server. |
| [HostingLD](https://www.hostingld.com/dedicated-rootserver/brands/matrix-dell/) | DX182 headline €259 / $288 with 9454P and 128 GB, but disks are optional; [configurator](https://www.hostingld.com/dedicated-rootserver/dx182/configurator) returns 404 | No complete priced ≥2 TB SSD configuration. [Legal page](https://www.hostingld.com/legal/legal-notice/) contains placeholders; contracting identity unresolved. |
| [Frenzy Host](https://frenzy.host/dedicated) | R: 9454P/256 GB/2 × 1.92 TB at $799; S: 128 GB/2 × 3.84 TB at $899 | Above ceiling. The [R order form](https://frenzy.host/order?plan=epyc-enterprise-r&type=enterprise-dedicated) advertises up to 15% annual reduction; even $799 × 85% = $679.15 would exceed $673.04. That arithmetic is not a recovered annual invoice. |
| [Servers.Guru](https://servers.guru/anonymous-dedicated-servers/) | 9454P/128 GB/2 × 3.84 TB at €1,229/month +€304; annual rent €12,290 | Above ceiling even when annual rent is divided by twelve. |
| [Intergrid](https://www.intergrid.cat/en/dedicated-servers) | 9454P/128 GB/2 × 3.84 TB at €899 +€349, before 21% VAT | Prior over-budget result rechecked; unchanged. |
| [Hostnox](https://hostnox.gr/eng/dedicated-servers/amd-epyc-9454p/) | Lowest 9454P/128 GB/2 × 3.84 TB at €796 +€396, Germany, with applicable VAT extra | Above ceiling. |
| [BIGBANG ITS](https://portal.its.ae/store/dedicated-hosting) | 9454P/128 GB/2 × 3.84 TB at $1,011.90 monthly; 256 GB/2 × 1.92 TB at $1,389.90 | Above ceiling; even the advertised 15% three-year reduction would not qualify. |
| [SupportHost](https://supporthost.com/dedicated-servers/) | Custom dedicated quotations; older [store URL](https://my.supporthost.com/index.php?language=english&rp=%2Fstore%2Fservers) redirects to portal login | No current public, complete 9454P price; old third-party listings are not current quotes. |
| [Privex Germany](https://pay.privex.io/order/package/dk128-nvme-de) | 9454P/128 GB/2 × 1.92 TB, 1 Gbps fair use, $1,040/month +$515 | Above ceiling. Distinct from the earlier Finland $880 +$440 listing; not presented as a price change to the same location. |
| [NODYNA](https://nodyna.com/en/servers) | €299.99 tax-inclusive, 9454P/256 GB/2 × 3.84 TB | Still marked coming soon; no verified current supply. |
| [ServerRental.store](https://serverrental.store/Developers) | Older $270 9454P/256 GB/2 × 2 TB table | Page explicitly identifies affiliate PowerVPS; order leads to current PowerVPS offer. Not a new seller or a verified $270 tariff. |

### Horizons Direct: why the attractive API data are insufficient

The public [JavaScript bundle](https://horizons.direct/assets/index-Co1VzxRd.js) and APIs describe whole bare metal separately from VPS, with the hardware and USD prices above. However, inspection of the public signup/login component shows a local timed success state for signup and a fixed failure state for login, without an authentication request. No account or credentials were supplied. This is direct evidence that those exposed forms do not establish a functioning account/order route.

The site also claims its production network uses AS64496. [IANA's primary registry](https://www.iana.org/assignments/iana-as-numbers-special-registry) reserves 64496–64511 for documentation. The site's network page acknowledges documentation IPs in its display and directs readers to the [regions API](https://horizons.direct/api/v1/regions) for actual endpoints; that API still returned documentation-range test addresses. These facts require supplier/network clarification before treating the stock counters, operator identity or prices as verified service availability. They are not evidence of delivered physical capacity. Do not infer fraud or ownership of the similarly named real facilities from the unresolved storefront.

## Currency and accounting checks

The existing EUR rate remains [EUR 1 = USD 1.0992 on 19 November](https://data-api.ecb.europa.eu/service/data/EXR/D.USD.EUR.SP00.A?startPeriod=2026-11-19&endPeriod=2026-11-19&format=csvdata). IDCBEST introduces a published Chinese-yuan quote. The same date's [ECB CNY observation](https://data-api.ecb.europa.eu/service/data/EXR/D.CNY.EUR.SP00.A?startPeriod=2026-11-19&endPeriod=2026-11-19&format=csvdata) is **EUR 1 = CNY 7.3280**, giving `3500 / 7.3280 × 1.0992 = USD 525.00`. IDCBEST's own payment instructions call for an 8% addition when tax-inclusive billing is required, yielding CNY 3,780 / USD 567.00. No further annual discount is assigned to the already promotional SKU without a matching quote.

All converted prepaid monthly amounts use actual term amounts before rounding; IpServer's totals are explicitly calculations from its published exact per-month equivalents. ServerWala's selected annual invoices are $3,618 and $3,791, rather than multiplication of an approximate savings label. Stock, tax and payment-method charges remain separate from a public subtotal. ServerWala's payment terms additionally impose gateway fees on card/online methods, with bank transfers exempt; the fee amount was not fixed in the public quote.

## Preservation and validation

The seven original columns and ascending numeric USD sort are retained. All 119 prior rows remain, with only the documented PowerDedi promotion refreshed. The eight new brands add 22 rows: ServerWala eight, HOSTING.WORKS four, Alpenhost four, IpServer.su two, and one each for Wsla, Cheap Ai Servers, HostingSaint and IDCBEST. Every new row has a primary offer link, native currency, setup/term information or an explicit unknown, evidence classification and the actual check date. Earlier research files are preserved unchanged.

No supplier contact, account registration, domain registration, purchase, hardware reservation or payment was made. Public configurations and quote calculators were inspected without completing checkout.
