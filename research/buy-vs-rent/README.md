# CI server ownership versus dedicated rental

[Start](../../README.md) / Buy or rent

**Historical snapshot.** The new [20 November internet-only purchasing study](../../old/buy-vs-rent/README.md) provides current component evidence, 18 priced build variants and independent electricity/internet calculations. It supersedes this snapshot's parts basket and physical replay prerequisite for the current buying decision. This earlier study remains unchanged below to preserve its 141-offer calculations and evidence; its colocation scenarios are not inputs to the new model.

Compare buying a **non-ECC workstation or desktop runners** for Rust/TypeScript builds and tests in Docker with renting a dedicated server. The purchase and hosting preference is Singapore first, Malaysia second.

**Rental coverage is fixed at 141 offers through `175399c`.** The [rental catalog](../../rentals/README.md) continues to grow. Offers added after this snapshot have no payback calculation in this study.

<a name="decision"></a>
<a name="direct-hardware-payback-the-primary-comparison"></a>

## When would buying pay back?

The Singapore A2 workstation with 256 GB of RAM and two 2 TB NVMe SSDs costs **S$8,609.40** in parts. That equals **30.34 months of UHost's recurring European rent**. For a new rental, counting its known setup fee changes when buying breaks even. Performance on the actual CI workload still needs validation.

| Costs counted for ownership | First whole break-even month against UHost |
|---|---:|
| Hardware only | 30 |
| Hardware and electricity | 42 |
| Hardware and internet | 37 |
| Hardware, electricity and internet | 55 |

This example assumes 350 W average server power at S$79.61/month and a separate S$50/month internet allowance. Every scenario excludes office rent. Cooling, UPS, assembly and repair reserves are optional extras. UHost's stock, network, service terms and final taxes still need confirmation. [Payback calculations and assumptions](06-direct-payback.md) · [Results for other rental offers](findings.md#direct-hardware-payback-the-primary-comparison)

<a name="files"></a>

## Choose a question

- <a name="reference-capacity-classes"></a><a name="owned-hardware-shortlist"></a>**Which hardware fits?** Compare RAM and mirrored storage for A1 and A2, then check the single-workstation and two-runner alternatives. [Capacity classes](findings.md#reference-capacity-classes) · [Owned hardware shortlist](findings.md#owned-hardware-shortlist) · [Parts lists and benchmark evidence](01-hardware-and-performance.md)
- <a name="performance-and-procurement-gates"></a>**Will it run our CI within 3–5%?** Check critical-job latency and busy-queue throughput on a representative replay. [Performance criteria](findings.md#performance-and-procurement-gates) · [Validation procedure and quote requirements](04-validation-and-procurement.md)
- <a name="optional-expanded-financial-comparison"></a>**What if the server must be local?** Compare regional rentals and colocation, or add cooling, maintenance and other costs over 12, 24 or 36 months. [Singapore and Malaysia market](02-rental-market.md) · [Expanded budget results](findings.md#optional-expanded-financial-comparison) · [Budget assumptions](03-rent-vs-buy-tco.md)

## Find a rental in the calculations

Use browser Find in the comparison files below to look up the provider and configuration or the stable ID. For example, UHost AX162-R is `001` in the original comparison.

In this snapshot, 93 of the 141 rows meet at least one A1 or A2 mirrored-capacity profile. Two meet both, giving 95 profile comparisons. The other 48 rows are also documented.

| Offer IDs | Calculations |
|---|---|
| 001–104 | [Original rental charges and capacity](05-repository-rental-comparison.md) · [Four-scenario payback](07-all-rentals-break-even.md) |
| N01–N15 | [15 follow-up offers, bringing coverage to 119](08-latest-rental-comparisons.md) |
| E01–E22 | [22 expansion offers, bringing coverage to 141](09-expanded-rental-comparisons.md) |
| 087 correction | [PowerDedi's first-month coupon and unchanged recurring rent](10-current-offer-updates.md) |

<a name="research-and-review-record"></a>

For all comparison tables, historical assumptions and the research record, see the [full findings](findings.md), [chapter index](findings.md#files) and [dated integration and review log](../2026-11-20-buy-vs-rent.md).
