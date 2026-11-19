# Independent review and validation record

[Study index](README.md) · [Methodology](sources-and-methodology.md) · [Financial source](calculate.py) · [Dated integration](../../research/2026-11-20-online-hardware-buy-vs-rent.md)

**20 November 2026, Asia/Saigon.** This was a documentary and numerical review. No physical hardware, CPU/storage benchmark, stress test or Rust/TypeScript/Docker performance workload was executed.

## Research and reviewer independence

Primary research was delegated to three **GPT-6.2 Astra** workers at **maximum reasoning effort**, covering CPU/workloads, components/compatibility, and rentals/utilities. A separately initialized **GPT-6.2 Sol** worker at **maximum reasoning effort** reviewed the source evidence and generated results. The reviewer independently fetched important manufacturer, retailer, tariff and benchmark evidence and used exact rational arithmetic rather than reusing the decimal calculator as its oracle. Root integrated the documents and performed release validation.

This records actual tool-selected model assignments. It does not claim that every orchestration or writing step used the same model, nor that a model review substitutes for physical measurement.

## Findings resolved

| Review area | Finding and resolution |
|---|---|
| Benchmark validity | Confirmed raw Clang values and their ratios. Two Dell EPYC submissions can be the same hardware; wording now says submissions. The 98.6–106.2% observation range is neither a confidence interval nor proof of ±3–5% complete CI performance. |
| Non-ECC memory | Separated Kingston's exact-system compatibility from ASUS's tested Crucial `.C16FE` eight-module entry. Refurbished base-SKU quantity/revision remains conditional. The KLEVV lower-price listing omits its printed SKU; the exact-SKU higher price is shown. |
| 256 GB DDR5 | Independently checked CPU, board and memory-vendor capacity evidence. Four 64 GB dual-rank Intel modules use the documented 4400 MT/s rating; no four-stick XMP or 5600 guarantee. |
| Physical compatibility | Checked CPU-connected versus chipset M.2 routing, motherboard dimensions, BMC console, cooler/case fit, EPS and supplemental PCIe power connectors, desktop PSU cable count and removable drive covers. Documentary inferences remain labelled. |
| Procurement evidence | Exact variant data supersedes generic product-page headers. Earlier unavailable components remain historical. Corrected the 750/850 W URL ambiguity and retired 9900X price. Seller-stated availability never becomes a reservation claim. |
| Rental selection | Added PlusClouds' separate 256 GB / EUR229 +542 case, retained UHost's extra-drive quote, and distinguished legacy 040Hosting supply. Rechecked Hetzner net prices, IPv4 and location availability. |
| Financial generation | Corrected an exact-string CPU selector that initially left the rental value output empty. Added all four prepaid ownership scenarios, separate cash versus service-equivalent crossings and minimum-contract exposure. |
| Numerical accuracy | Corrected a tax-test fixture's last digits. Every economic subtotal is checked against its quantity-based BOM before output. Ceiling crossings use unrounded values. |
| Storage wording | Removed any implication that the unspecified AX162 drives were proven to implement capacitor-backed PLP. Named enterprise Micron specifications remain distinct from the selected consumer models. |
| Source links | Replaced a retired Customs PDF with current official guidance, corrected a CPU URL, and withdrew an unavailable price-based value claim. A stale CR Group SSD source is labelled as historical/inaccessible and is excluded from the BOM. |
| Publication format | CSV output uses explicit LF line endings; generated files remain byte-reproducible and pass ordinary Git whitespace validation. |

## Numerical coverage

The final input set contains **18 priced builds**, **16 monthly rental cases** and **one annual-prepayment case**. Two-node rental and ownership cases explicitly preserve per-node memory. The selected matrix does not pretend that all 195 catalog entries were repriced or recalculated in this pass.

| Output checked | Final coverage |
|---|---:|
| Complete procurement builds | 18 |
| Quantity-priced component lines | 126 |
| Four-scenario monthly break-even rows | 1,152 |
| Cumulative build/rental/scenario/horizon rows | 8,064 |
| Annual-prepayment scenario/horizon rows | 504 |
| Owned named-proxy value rows | 504 |
| Same-CPU rental named-proxy value rows | 140 |
| Sensitivity rows | 1,170 |

The independent reviewer checked the original 17 builds and then the added Malaysian 128 GB / two-SN850X-4-TB variant. The extra variant does not change the primary purchase or rental conclusion. Financial tests cover exact/fractional crossing, no crossing, independent utilities, FX, power, tax and term handling. The standard-library unit suite has **10 tests**, including a separate exhaustive month-search oracle over a grid of costs.

As a representative check, the S$13,330 workstation's first whole crossings are **10 / 11 / 11 / 12** against regular AX162-2 and **47 / 60 / 74 / 114** against UHost. Its 36-month cost with electricity and existing internet is **S$15,581.93**; UHost is **S$10,368.91**, and monthly ServerWala is **S$15,553.36**, all under their documented invoice assumptions. That S$28.57 ServerWala difference is too small to override unquoted fees or tax.

## Source and repository verification

The focused final source check issued public GET requests to 68 distinct URLs, including all then-existing 29 unique primary procurement offers. Most returned HTTP200; access-limited responses were retained with explicit qualifications. The detected broken CPU URL was replaced. A broader reviewer pass checked 266 non-cart sources, retried HEAD failures with GET, and reported the source corrections above. The late Malaysian SN850X sources were checked separately through exact public variant JSON and manufacturer documentation. A successful HTTP response is not proof of the claim; exact model, price and source context were checked as well.

The repository documentation checker compares against **`4495bf93464f65182107960b814364644fe3d284`**. It verifies local links/anchors, the ordered seven-column catalog and preservation of prior dated evidence. All **195 rental rows** and their order remain unchanged. Historical research is clearly labelled at its entry points rather than erased. New research Markdown contains `Signed-off-by: Alexey Zhokhov` or the same attribution with the verified email.

Release commands from the repository root:

```sh
python3 old/buy-vs-rent/calculate.py --check
python3 -m unittest discover -s old/buy-vs-rent -p 'test_calculate.py' -v
python3 scripts/check_docs.py --baseline 4495bf93464f65182107960b814364644fe3d284
git diff --check
```

The final GitHub PR carries the publication state and checks. Commit and merge identifiers are reported only after their completion; this research file does not claim that an unpublished or unmerged commit is already on main.

## Remaining limits

Public evidence supports the closest hardware choice, exact sourced component baskets and conditional financial comparisons. It does not establish allocated multi-seller inventory, shipped BIOS revision, final buyer-specific invoices, future rates, complete customer CI throughput, or a guaranteed ±3–5% replacement. Those limits are explicit in the recommendation and do not impose a physical-testing prerequisite.

Signed-off-by: Alexey Zhokhov
