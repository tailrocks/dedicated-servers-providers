# Sources, evidence classes and limitations

[Study index](README.md) · [Benchmark ledger](published-benchmarks.md) · [Financial method](break-even-analysis.md) · [Independent review](review-and-validation.md)

**Research snapshot: 20 November 2026, Asia/Saigon.** Some source requests occurred on 19 November UTC. The last published ECB fixing available at the check was 19 November. Prices, tariffs and stock observations are dated claims, not promises about later invoices.

## Scope and relation to existing work

The task is to choose Singapore-first, Malaysia-second **desktop/workstation hardware with non-ECC system RAM** for Rust, TypeScript and Docker CI. The performance reference is the exact EPYC 9454P, normalized to 100 separately for each named benchmark. The target is near-equivalent aggregate compute with a 3–5% tolerance, or a useful 10–50% improvement if supported by evidence. No arbitrary acquisition ceiling excludes a faster candidate.

The existing repository was inspected across its catalog, watchlist, methodology, contributor instructions, dated reports, 141-offer ownership chapters, and documentation checker. Work started at `5b26e01a2165d686d1094ad3173152700fb00157` with 170 rental entries. A concurrent, signed update advanced main to `4495bf93464f65182107960b814364644fe3d284`, with 195 entries; that update was integrated before publishing this study. Its new UHost disk upgrade and 040Hosting legacy offer enter the new financial model. The earlier 141-offer calculation snapshot remains unchanged and attributable to its own date and assumptions. [Catalog](../../rentals/README.md) · [Latest expansion](../../research/2026-11-20-further-options.md) · [Historical ownership index](../../research/buy-vs-rent/README.md)

The new work is under `old/buy-vs-rent/` because the requested destination was `old/`. Its directory name does not mean that its November 20 evidence predates the preserved study. The root and research indexes make the current decision guide explicit.

The new study makes its recommendation entirely from public information. It does not adopt the earlier physical replay prerequisite or any earlier colocation-budget assumptions. No CPU benchmark, hardware stress test, Rust/TypeScript/Docker performance test or assembly was performed or requested. Financial arithmetic, source checks and repository validation are the only executed tests.

## Four evidence classes

| Class | What it means here | Examples / boundaries |
|---|---|---|
| **Direct published observation** | An external source reports a specification, result, offer or tariff. | AMD cores; exact Kingston system list; GamersNexus Chromium minutes; live variant price/availability; SP tariff. A vendor listing is not proof of physical allocation. |
| **Derived result** | Arithmetic from identified observations. | Baseline time / candidate time, Clang rate ratio, sum of BOM quantities, FX conversion, monthly electricity and break-even. A derived rate is not a new measurement. |
| **Analytical scenario** | An explicit assumption explores a possible configuration or workload. | 80–90% two-host queue efficiency, midpoint wall power, allocation of cores/RAM at six job counts, flat multi-year line renewal. |
| **Unavailable** | The required evidence was not found or could not be independently recovered. | Exact customer CI jobs/hour, 3–5% end-to-end equivalence, SKU-specific allocated stock, complete Malaysian WRX80 landed quote, selected unknown taxes. |

Confidence is attached to the narrow claim. Memory-vendor compatibility is strong evidence for the exact named module/system pair, but is different from an ASUS-tested eight-module revision. A direct one-system benchmark is evidence of that run, with low confidence for a production queue prediction. A reproducible financial answer can have high arithmetic confidence and still depend on uncertain procurement inputs.

## Benchmark comparison rules

1. **Name the workload and denominator.** The primary comparable Clang observation is AX162-R 327.4 Klines/s multi, 10.8 single. A 337.1 result gives 103.0% work rate. Overall Geekbench scores, PassMark, Cinebench and SPEC are not silently blended into a CI score.
2. **Keep versions and environments visible.** Same Geekbench 6 versions and Linux AVX2 are preferred. The publisher documents CPU-score compatibility across 6.3–6.7; the report still records version differences. Geekbench 7 is not mixed with 6. A compile time from another revision of Chromium or another test harness is not normalized directly against it.
3. **Use independent, longer builds as corroboration.** TechSpot and Puget establish sustained 5995WX build behavior. Phoronix supplies original Linux compiler and Rust results. GamersNexus independently corroborates the mainstream desktop ordering. These do not contain the exact 9454P on the same production-pipeline protocol, so they cannot close the requested equivalence gap.
4. **Show variation and inconvenient observations.** The two Dell 9454P submissions from one account differ; their paired 5995WX ratios are 98.6% and 106.2%. They need not be two different physical servers. Intel's six public Clang submissions include a low outlier rather than quietly discarding it. Implausible frequency metadata and an anomalous isolated kernel result are flagged.
5. **Do not equate CPU maximum with rental configuration.** EPYC has twelve memory channels, but the AX162's stated 128/256 GB capacity does not prove twelve populated channels. A public four-DIMM specimen and a fully populated SPEC machine have different bandwidth opportunities.
6. **Keep pipeline latency separate from throughput.** More cores can serve more repositories while an individual link or type-check stage favors clock speed/cache. Two hosts cannot combine their RAM for an ordinary single Cargo invocation. No jobs-per-hour figure is invented.

The [benchmark ledger](published-benchmarks.md) preserves source URLs, run IDs, versions, raw values, ratios and exclusions. The [workload document](ci-cd-performance-analysis.md) cites Cargo, Rust, TypeScript, Node and Docker technical documentation. TypeScript 7's native parallel compiler is distinguished from the older JavaScript compiler; assuming every `tsc` workload is single-threaded is no longer adequate.

## Procurement evidence rules

The seller's exact variant is checked where exposed, not merely a generic product header. Shopify variant `available`, selected capacity prices, WooCommerce variations and manufacturer part numbers can contradict search snippets or range pricing. Public JSON is evidence of what the seller's storefront reports, not a reservation of the listed quantity.

- Several older TechDeals components still have product pages and prices while the exact variants report unavailable. They are preserved as historical evidence and excluded from the new-stock BOM.
- The Founder's Threadripper page has a generic header price; the selected 5995WX row is **S$2,990**. No other processor's entry is substituted.
- The chosen PSU is the exact black **850 W** variant at **S$251**, even though the generic URL contains 750 in its name. The exact variant ID is retained.
- The **S$2,579 KLEVV 2×64 GB** description omits the printed manufacturer part number. The required black part is specified in the recommendation; a separate exact-SKU **S$2,889** listing adds S$310 per node. The lower subtotal remains a qualified description-based offer, not a verified allocation of that exact SKU.
- Eight refurbished Crucial modules at S$329 each are a separate conditional scenario. The base part number alone does not establish the ASUS-tested `.C16FE` revision, eight-unit supply or new-memory warranty.
- A listing's local warranty is recorded where stated. Contradictory one-year versus generic three-year motherboard warranty wording remains unresolved. No blanket warranty is inferred across sellers.

The [Singapore](singapore-hardware.md), [Malaysia](malaysia-hardware.md), [RAM](ram-comparison.md) and [complete-build](recommended-builds.md) documents preserve each exact component, seller, country, price, availability, warranty and check date. CPU, RAM, BIOS, NVMe lanes, network support, connector count and case/cooler clearance are documentary compatibility checks, not assertions that a physical build was tested.

## Main source families

| Evidence | Primary/original sources | Location of exact citations |
|---|---|---|
| Processor and platform | AMD, Intel ARK/datasheets, ASUS, MSI, Kingston, KLEVV | [CPU table](cpu-alternatives.md), [memory](ram-comparison.md), [builds](recommended-builds.md) |
| Compilation and system measurements | Original Geekbench submissions and internals, Phoronix/OpenBenchmarking, GamersNexus, TechSpot, Puget, SPEC, PC Watch, MyNavi, PC Perspective | [Benchmark ledger](published-benchmarks.md), [electricity](electricity-costs.md) |
| Storage | Lexar, Samsung, ADATA, Micron specifications and original Tom's Hardware/PC Gamer testing | [NVMe comparison](nvme-comparison.md) |
| Retail | Local product pages and their public exact-variant data | [Singapore](singapore-hardware.md), [Malaysia](malaysia-hardware.md), [BOM JSON](data/procurement.json) |
| Rental | Hetzner live price/availability feeds, selected provider configurators and seller terms | [Baseline](hetzner-ax162-baseline.md), [rental update](rental-market-update.md), preserved [rental catalog](../../rentals/README.md) |
| Utility and FX | Singapore SP Group, Malaysia ST/TNB, StarHub, WhizComms, Time, Malaysia Customs, ECB | [Electricity](electricity-costs.md), [internet](internet-costs.md), [native inputs](data/market-inputs.json) |

## What remains uncertain

The strongest unresolved issue is **performance transfer to the user's actual CI**, not arithmetic. Public evidence identifies the closest hardware and likely bottlenecks, but does not warrant a 95–105% guarantee for every mix of clean/incremental Rust, type-checking, tests, downloads and container layers. Stock, final invoicing, BIOS on a shipped board, quoted CPU delivery, consumer SSD endurance under the eventual write load and multi-year tariffs are additional bounded uncertainties.

These limits support a decisive recommendation now: rent the competitively priced exact EPYC when economy and a single large host dominate; buy the documented WRX80 configuration for non-ECC single-host ownership; use the Ryzen pool only when jobs can be assigned independently. They do not defer the research until a physical test.

Signed-off-by: Alexey Zhokhov
