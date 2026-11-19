# Current corrections to existing rental offers

**Updated: 20 November 2026 (Asia/Ho_Chi_Minh).** This file overlays changes to existing stable rental IDs without rewriting their earlier evidence. The [initial 104-offer costs](05-repository-rental-comparison.md) and [payback appendix](07-all-rentals-break-even.md) remain dated snapshots. The [141-offer expansion](09-expanded-rental-comparisons.md) includes the 22 newly added rows separately.

## 087 — PowerDedi European EPYC 9454P first-month coupon

The current repository [expansion evidence](../2026-11-20-expansion.md#powerdedi-first-month-reduction-unchanged-renewal) records the Amsterdam-selected **EPYC 9454P / 256 GB / two 3.84 TB NVMe** offer with `BIRTHDAY20`: **USD 391.20 for month one, then USD 489/month**, with zero setup. A fresh direct retrieval of the [public order URL](https://powerdedi.com/order?plan=e-9454p&promo=BIRTHDAY20) in this integration again returned USD 391.20 due, USD 97.80 discount and explicit first-month-only wording. The search-service parameterized fetch failed, so this verification used the returned public HTML. No account or order was created.

The offer fits both A1 and A2 nominal capacity floors. Physical allocation, the legal operator, customer-specific tax and payment fees remain unresolved. Payment uses a crypto-funded balance; buyer eligibility still needs confirmation. A cycling promotion timer does not establish a permanent discount or a contractual last redemption date. The comparison is conditional on the coupon being accepted for the intended new order. **Do not transfer this Amsterdam check to the separate Singapore lead in file 06.** That location still has conflicting fulfillment evidence.

### Rental costs with the introductory reduction

At the same dated conversion, `USD × 1.4176 / 1.0992`, the one-time USD 97.80 reduction is **S$126.1292576**. The unchanged recurring rent is **S$630.6462882/month**. The monthly schedule for an integer horizon `n ≥ 1` is:

```text
Rental charges = n × USD 489 − USD 97.80
```

| Horizon | USD known charges with coupon | SGD known charges with coupon | SGD without coupon, historical baseline |
|---|---:|---:|---:|
| 12 months | 5,770.20 | 7,441.63 | 7,567.76 |
| 24 months | 11,638.20 | 15,009.38 | 15,135.51 |
| 36 months | 17,506.20 | 22,577.14 | 22,703.27 |

These are known rental subtotals before unquoted tax and payment/network charges, with unchanged renewal rent assumed. The recurring price remains USD 489. Paying USD 391.20 for every month would incorrectly treat an introductory discount as a permanent rate.

### Independent electricity and internet payback

Use A1 hardware **S$8,891.00** or A2 hardware **S$8,609.40**, and the same independent monthly ownership costs: **S$0 / S$79.6138 server electricity / S$50 internet / S$129.6138 both**. Server electricity assumes 350 W average wall draw for 730 hours at S$0.3116/kWh; it is not a hardware measurement. Office rent is excluded. Room cooling, UPS, assembly and maintenance remain separately optional. [Direct cost model](06-direct-payback.md)

For a new rental receiving this coupon, with recurring rent `R`, hardware `H`, selected owner running cost `O` and one-time rental credit `C`:

```text
H + n × O ≤ n × R − C
Service-month crossover = (H + C) / (R − O)
```

The credit increases the hardware recovery period because it makes the rental cheaper. It is not an avoidable setup fee to subtract from the purchase price. An existing lease uses its avoidable future invoices; a discount already received is sunk.

| Owned capacity profile | Neither utility: fractional → whole month | Electricity only | Internet only | Both utilities |
|---|---:|---:|---:|---:|
| A1, S$8,891.00 | 14.30 → **15** | 16.36 → **17** | 15.53 → **16** | 17.9971 → **18** |
| A2, S$8,609.40 | 13.85 → **14** | 15.85 → **16** | 15.04 → **16** | 17.44 → **18** |

Fractions and integer ceilings use unrounded inputs. Compared with the no-coupon snapshot, the A2 internet-only whole-month crossing moves from **15 to 16**; the other seven whole-month results remain the same. Even after the coupon, this offer's 36-month rental subtotal exceeds both direct and expanded ownership budgets, so it does not add a rental to the cheaper-at-36-month counts.

These are cash-cost comparisons between capacity-compatible options. They do not establish CI performance equivalence, supplier fulfillment or a refundable hardware purchase. The [workload acceptance procedure](04-validation-and-procurement.md) still applies.

## Source and review trail

- [Pinned upstream 141-row source](https://github.com/tailrocks/dedicated-servers-providers/blob/175399c50339f5d8192c4a5821e74db4d5fbd4f6/README.md) and [coupon evidence](../2026-11-20-expansion-global.md).
- [Original 087 row and recurring-only payback](07-all-rentals-break-even.md#offers-that-fit-either-profile).
- [ECB SGD, 19 November 2026](https://data-api.ecb.europa.eu/service/data/EXR/D.SGD.EUR.SP00.A?startPeriod=2026-11-19&endPeriod=2026-11-19&format=csvdata) and [same-day USD](https://data-api.ecb.europa.eu/service/data/EXR/D.USD.EUR.SP00.A?startPeriod=2026-11-19&endPeriod=2026-11-19&format=csvdata).

This update is part of the GPT-6.2 Astra max research integration and GPT-6.2 Sol max independent review requested by the user. No purchase, supplier contact or actual CI replay occurred.
