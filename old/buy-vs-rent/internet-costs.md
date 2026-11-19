# Internet costs at an existing Singapore or Malaysia site

[Study overview](README.md) · [Electricity](electricity-costs.md) · [Market inputs](data/market-inputs.json)

**Prices checked 20 November 2026, Asia/Ho_Chi_Minh.** Use **zero incremental cost** if an existing, permitted connection can handle the runners without an upgrade, extra traffic charges, or another circuit. When CI causes a change of plan, use the new bill less the existing bill. When CI requires its own subscription, use the full incremental price and its commitment. A pool of two machines can use one connection.

## Singapore

| Use and eligible subscriber | Price and commitment | Connection, initial charges and restrictions |
|---|---|---|
| Existing service | **S$0/month incremental** under the conditions above | Verify upstream capacity, permitted use and any data cap on the existing contract. |
| **Business budget. StarHub SME Dynamic Fibre, 500 Mbps** | **S$105/month for 36 months**, or S$109/month for 24 months, inclusive of 9% GST | New qualifying ACRA-registered business, subject to building coverage and approval. Standard activation, router rental and installation waived. Dynamic IP. After the term, prevailing rates apply. [StarHub plan matrix](https://www.starhub.com/sme/business-broadband.html) · [Business promotion terms](https://www.starhub.com/business/promotions/terms-and-conditions.html) |
| Business, 1 Gbps Dynamic Fibre | S$170/month on 36 months or S$174/month on 24 months on the regular new-customer page, GST included. A separate eligible fibre-zone offer lists **S$105 / S$109** on the respective terms. | Address qualification makes the two public quotes materially different. The cost model uses the 500 Mbps standard plan above. [Standard matrix](https://www.starhub.com/sme/business-broadband.html) · [Fibre-zone promotion and conditions](https://www.starhub.com/business/forms/broadband-promo-sme.html) |
| Residential sensitivity. WhizComms 10 Gbps No-Frills | S$7.99 first month and S$27.99/month for the next 23 months. Current rolling auto-renewal is S$30/month. The listed prices include GST. | New residential subscriber, fibre-ready address, 24 months, sign up by **22 November 2026** and install by **31 December** for the offer. Standard weekday/weekend installation and activation are waived. ONR included, Wi-Fi router supplied by customer. Special appointments or new termination-point work may cost extra. [Plan](https://whizcomms.com.sg/broadband/) · [Promotion](https://whizcomms.com.sg/promotion-tcs/) · [Residential terms, including renewal](https://whizcomms.com.sg/tcs-broadband/) |

Across 24 full months the Singapore residential offer costs S$651.76, before equipment or nonstandard work. If the stated S$30 rolling rate continues, 36 months cost S$1,011.76. The 36-month business commitment costs **S$3,780** at S$105. A hardware payback before month 36 does not release the remaining ISP obligation. The business scenario continues S$105 after the term only as a flat-rate sensitivity. The old study’s S$50 allowance is a separate dated input. [Earlier direct payback](../../research/buy-vs-rent/06-direct-payback.md)

## Malaysia

| Use and eligible subscriber | Price and commitment | Connection, initial charges and restrictions |
|---|---|---|
| Existing business or personal connection suitable for the actual usage | **RM0 incremental** | An existing household line subject to a personal-use clause cannot supply the commercial-workload baseline. |
| **Business budget. Time Business Fibre, 300/300 Mbps** | **RM128/month before service tax**, **RM135.68/month at 6%**, 24 months | Standard 24-month offer has no additional installation charge. Dynamic address by default, one fixed IP is an optional RM200/month before applicable tax. Address coverage and nonstandard wiring are separate. 12-month term adds RM66/month for its first 12 months. No-contract installation is RM1,200 upfront. [Business plan](https://business.time.com.my/sme/) · [Provider FAQ](https://business.time.com.my/support/for-business/faq/) · [Malaysian Customs telecom tax](https://mysst.customs.gov.my/faq-services-tax/) |
| Personal use only. Time Home Fibre, 200/200 Mbps | RM99/month before service tax or **RM104.94/month at 6%**, 24 months | Standard installation included, subject to coverage. The same speed without a contract carries an RM400 one-time fee. Time’s home service schedule specifies personal use and says subscribers should not use it for a trade, business or profession. [Home offer](https://www.time.com.my/) · [Home service schedule, section 4](https://www.time.com.my/wp-content/uploads/2023/07/250123-Service-Schedule-C-CONSUMER-BROADBAND-endorsed.pdf) |

For 24 full months the business base is **RM3,256.32** including 6%. A new eligible online subscriber can receive one free full billing cycle on the 300 Mbps plan, giving RM3,120.64 in equivalent full-month subscription charges if accepted. The first partial bill and any actual extras follow the provider terms. The main model conservatively budgets 24 paid months and holds the post-term price flat for longer horizons. The gross business allowance is approximately **S$42.55/month** using the [19 November ECB rates](https://data-api.ecb.europa.eu/service/data/EXR/D.MYR+SGD.EUR.SP00.A?startPeriod=2026-11-19&endPeriod=2026-11-19&format=csvdata). [Time’s online promotion](https://business.time.com.my/support/for-business/faq/)

## Using the connection price for CI

The default AX162 has a guaranteed **1 Gbps port and unlimited traffic**. The owner’s quoted broadband plans describe access speed and contract terms. A shared last mile, upstream speed, IP addressing, package registry routing and contention can affect the time that workers spend pulling images, restoring caches and uploading artifacts. Residential access and a separately subscribed SME line do not establish dedicated internet access with committed bandwidth. A static public IPv4 is relevant when inbound connections or allowlists require one. An outbound CI runner may work with dynamic addressing. [Hetzner traffic](https://docs.hetzner.com/robot/general/traffic/) · [Time’s distinction between Business Fibre and Internet Direct](https://business.time.com.my/sme/)

Apply the selected internet cost **once per site** to the internet-only and both-utilities cases. Use zero in the hardware-only and electricity-only cases. The rented machine’s published port and allowance are already part of its own charge. If both deployment models use the same developer-office internet independently of the runner, that common charge cancels.

Signed-off-by: Alexey Zhokhov <alexey@zhokhov.com>
