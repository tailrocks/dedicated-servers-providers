# Brazilian and Peruvian storefronts, 20 November 2026

Hardware locations below are supplied by the storefronts and differ from the reseller's location. Verification took place 19 November UTC, after midnight in Asia/Ho_Chi_Minh. The 19 November ECB reference rates were [6.4765 BRL per EUR](https://data-api.ecb.europa.eu/service/data/EXR/D.BRL.EUR.SP00.A?startPeriod=2026-11-19&endPeriod=2026-11-19&format=csvdata) and [1.0992 USD per EUR](https://data-api.ecb.europa.eu/service/data/EXR/D.USD.EUR.SP00.A?startPeriod=2026-11-19&endPeriod=2026-11-19&format=csvdata). Converted monthly values use BRL ÷ 6.4765 × 1.0992.

## AMS SOFT

The [Brazilian seller's dedicated-server catalog](https://loja.amssoft.com.br/dedicated-servers) and all four public cart totals agree. Each whole server has a 9454P, 48 cores and 96 threads, DDR5 ECC, software RAID 1, unmetered 1 Gbps, one IPv4 and an IPv6 /64. The two countries have different prices, and the two hardware mixes trade twice the memory for half the disk capacity.

| Country and verified cart | Memory and drives | Monthly and amount due today | Twelve-month subtotal |
|---|---|---:|---:|
| [Finland AX162-S, 10099](https://loja.amssoft.com.br/cart.php?a=add&pid=10099&billingcycle=monthly) | 128GB, 2 × 3.84TB NVMe | R$1,989.90 (US$337.73) | R$23,878.80 |
| [Finland AX162-R, 10102](https://loja.amssoft.com.br/cart.php?a=add&pid=10102&billingcycle=monthly) | 256GB, 2 × 1.92TB NVMe | R$1,989.90 (US$337.73) | R$23,878.80 |
| [Germany AX162-S, 10100](https://loja.amssoft.com.br/cart.php?a=add&pid=10100&billingcycle=monthly) | 128GB, 2 × 3.84TB NVMe | R$2,099.90 (US$356.40) | R$25,198.80 |
| [Germany AX162-R, 10101](https://loja.amssoft.com.br/cart.php?a=add&pid=10101&billingcycle=monthly) | 256GB, 2 × 1.92TB NVMe | R$2,099.90 (US$356.40) | R$25,198.80 |

The selected billing cycle is monthly, with no longer cycle priced. For every PID the public order form's [price-calculation code](https://loja.amssoft.com.br/templates/orderforms/lagom2/js/order.min.js?v=2.4.1-9cb37156aa46295a6445fc38bc8cbab5) returned the selected product, the monthly amount and the identical amount due today. No setup charge appeared. Optional Proxmox Backup Server and Graylog services were unchecked. Tax and any additional contractual minimum were not stated. No coupon or expiry appeared, and the catalog's displayed discount was 0%. No physical inventory count or delivery date was established.

The site's rendered controls resolve a misleading text-extraction artifact. Each AX162 card has an active monthly order button and lacks the `is-disabled` class. The [provider stylesheet](https://loja.amssoft.com.br/templates/lagom2/core/extensions/CMS/assets/css/lagom-cms.css?v=1.1.3) hides the button's `Indisponível` text by default and displays it for a disabled card. Unpriced longer billing cycles use a fallback message. Reading every hidden template label as visible availability would misclassify all four monthly configurations.

## Gokiebox

The Peruvian seller's [dedicated-server product page](https://gokiebox.com/servidores-dedicados) offers Dedicado XL as an entire physical server. The [anonymous selected USD configuration, PID 237](https://app.gokiebox.com/carrito/agregar/237?moneda=USD) specifies EPYC Turin 9455 (48 cores/96 threads), 128GB DDR5 ECC and 2 × 1.92TB NVMe in software RAID. The catalog advertises unlimited traffic on up to 3 Gbps and private vRack. This is 3.84TB raw and 1.92TB nominal mirrored.

The public configurator embeds its initial product data in a JSON script named `app`. It gives the billing currency as USD and only the monthly cycle, **$484/month plus $357 setup**, for an $841 first payment and a $6,165 first year. The marketing page omits that setup fee. No coupon, promotional deadline or additional minimum term appeared. The listed location is Canada. The configuration also offers Beauharnois, Gravelines, Strasbourg and Roubaix at the same base price and no regional surcharge. Its product-level stock field is null. These choices provide no proof of available machines. The [terms, section 6.1](https://gokiebox.com/terminos-y-condiciones) state that published prices exclude Peruvian IGV and that any applicable tax based on place of consumption is specified on the offer or billing document. The advertised Canadian location is Beauharnois; prices for optional additional IPv4 addresses require inquiry.

The `moneda=USD` parameter is material for reproducibility: a fresh anonymous request returned USD 484 plus 357, while the bare route defaulted to PEN 1,790 plus 1,320. The original marketing link's `currency=3` is interpreted on the `/store/` redirect; that same parameter on `/carrito/` did not reliably select USD. The README uses the verified direct USD link.

## Hospedagem Segura

Earlier indexing of the [seller's dedicated-server page](https://www.hospedagemsegura.com.br/servidor-dedicado/) showed HS-32, a 9455 with 128GB and 2 × 1.92TB NVMe in Canada or France, at R$2,819.72/month plus R$2,354.61 activation, with optional management at R$348.84/month. The currently retrieved page labels its full catalog as 13 configurations with four to 24 cores, lists HS-31 and HS-33 but omits HS-32, and contains no 9455. The old stock label and offer do not qualify as current.

All checks used the provider's public pages and anonymous price calculations. No order, reservation, account creation or vendor contact occurred.
