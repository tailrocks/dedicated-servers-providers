# Buying non-ECC CI hardware in Singapore or Malaysia

**Evidence date: 20 November 2026, Asia/Saigon.** [Repository home](../../README.md) · [195-offer rental catalog](../../rentals/README.md) · [Earlier 141-offer ownership study](../../research/buy-vs-rent/README.md)

## Decision

**Rent a competitively priced EPYC 9454P if the main objective is economical access to one large CI host.** UHost's published 256 GB / 2 × 1.92 TB configuration is USD 220/month plus USD 120 setup; its network terms, final tax and physical allocation remain unconfirmed. The comparable new non-ECC workstation below costs **S$13,330 in components**. Its modeled recovery of that investment takes **47 months with hardware alone, 60 with electricity and existing internet, or 114 with electricity and a new business line**. The last figure is beyond the useful 60-month comparison horizon, not a credible nine-year price forecast. [Rental evidence](rental-market-update.md) · [Financial interpretation](rent-vs-buy.md)

**If buying one non-ECC machine to replace the AX162 is the requirement, choose AMD Threadripper PRO 5995WX, ASUS Pro WS WRX80E-SAGE SE WIFI, eight Kingston KVR32N22D8/32 modules and two Lexar NM790 2 TB drives.** This is the closest supported single-host candidate. Published parallel Clang observations put it at approximately **98.6–106.2%** of separate same-version 9454P submissions; one named AX162 comparison gives **103.0%**. These are compiler-proxy ratios, not a demonstrated 3–5% equivalence for a Rust/TypeScript/Docker pipeline. No physical test is a prerequisite for this recommendation. [CPU evidence](cpu-alternatives.md) · [Exact parts and compatibility](recommended-builds.md)

The old S$8,609.40 parts basket is retained in its original historical study. Several of its low-price product variants now report unavailable, and its memory price cannot be carried into a new build. The new strict 256 GB basket uses **eight new, exact Kingston modules at S$858 each**. A **S$9,098 refurbished-Crucial scenario** is explicitly conditional on quantity, revision and warranty; it is not the primary purchase quote. [Current Singapore evidence and stale listings](singapore-hardware.md) · [RAM qualification](ram-comparison.md)

## Ranked purchase choices

The best overall single-host purchase and the closest EPYC substitute use the same CPU family. The capacity variants avoid inventing a different recommendation merely to fill a category.

| Rank / purpose | Exact platform and capacity | Singapore component subtotal | Decision |
|---|---|---:|---|
| **1 — Primary purchase, 256 GB / closest EPYC-class single host** | 5995WX, WRX80E-SAGE SE WIFI, 8 × 32 GB non-ECC DDR4, 2 × NM790 2 TB | **S$13,330** | A/E: 256 GB available to one job and 2 TB nominal mirrored. Custom-order CPU; cooler and complete allocation conditional. |
| **2 — 128 GB optimized EPYC-class capacity** | Same 5995WX platform, 8 × 16 GB Kingston KVR32N22D8/16, 2 × NM790 4 TB | **S$10,022 indicative** | D: closest capacity alternative to AX162-1, with all eight memory channels populated. Exact 16 GB RAM price is an indicative supplier quote, not confirmed eight-stick stock. |
| **3 — Higher-throughput independent runner pool** | **Two** Ryzen 9 9950X3D machines; each MSI B850M GAMING PLUS WIFI, 128 GB non-ECC DDR5 and 2 × NM790 2 TB | **S$10,228** | C: fast independent jobs. A 125–144% parallel proxy requires **assumed 80–90% pool efficiency**. RAM and storage do not combine for one job. |
| Mainstream value alternative | One 9950X3D node, 128 GB / 2 × 2 TB | **S$5,114** | Faster per-core work, but 78–80% in the parallel Clang proxy; not an equivalent aggregate AX162 replacement. |
| Lowest capital desktop alternative | Core Ultra 7 270K Plus, ASUS TUF B860M-PLUS WIFI, 128 GB / 2 × 2 TB | **S$4,757** | B: close to 9950X in a controlled full Chromium compile. Published multi results are heterogeneous; less suitable for a tight throughput promise. |

These totals assume the documented local collection or eligible standard delivery and fee-free payment choices. They are complete component subtotals, not reserved stock, issued invoices, assembly services or cross-border landed quotes. An existing Ethernet cable and switch/router port are assumed. Operating systems and the wired NIC are included/free in the documented configuration. [Singapore](singapore-hardware.md) · [Malaysia](malaysia-hardware.md) · [Complete bills of materials](data/procurement.json)

Singapore is the stronger purchasing market in the checked listings. Malaysia's 128 GB Intel configuration is **RM19,153**, about **S$6,006.26**, and its 256 GB Intel configuration is **RM32,211**, about **S$10,101.16**, at the dated ECB fixing. A local Malaysian buyer should not treat the cheaper Singapore subtotal as a landed Malaysian price: transport, import charges and the warranty route have not been quoted. [Regional purchasing analysis](malaysia-hardware.md)

## Read the evidence

| Question | Document |
|---|---|
| What exactly does AX162 provide? | [Reference hardware, live tariffs and tax scenarios](hetzner-ax162-baseline.md) |
| Which CPUs qualify, including newer generations? | [CPU alternatives](cpu-alternatives.md) |
| Where do the performance numbers come from? | [Published benchmarks, versions and limits](published-benchmarks.md) |
| How do 1 / 4 / 8 / 16 / 32 / 64 jobs differ? | [Rust, TypeScript and Docker concurrency](ci-cd-performance-analysis.md) |
| Can 128 or 256 GB work without ECC? | [Exact memory, BIOS and population evidence](ram-comparison.md) |
| Is PCIe 5 storage worth the money? | [NVMe sustained performance, endurance and layouts](nvme-comparison.md) |
| Where can the parts be purchased? | [Singapore](singapore-hardware.md) · [Malaysia](malaysia-hardware.md) |
| Do the complete systems fit together? | [Recommended builds and compatibility](recommended-builds.md) |
| What does electricity add? | [Tariffs and idle/moderate/heavy estimates](electricity-costs.md) |
| What does internet add independently? | [Existing, residential and business connectivity](internet-costs.md) |
| Which rentals materially change the decision? | [Rental market update](rental-market-update.md) |
| What does owning cost across all four scenarios? | [Buying versus renting](rent-vs-buy.md) · [Generated results](financial-results.md) |
| How is break-even computed and checked? | [Formulas, horizons and sensitivity](break-even-analysis.md) |
| How were uncertainty and sources handled? | [Sources and methodology](sources-and-methodology.md) · [Review and validation](review-and-validation.md) |
| What should I do? | [Final recommendations](final-recommendations.md) |

## Reproduce the financial work

From the repository root, using Python 3.9 or later:

```sh
python3 old/buy-vs-rent/calculate.py
python3 old/buy-vs-rent/calculate.py --check
python3 -m unittest discover -s old/buy-vs-rent -p 'test_calculate.py' -v
python3 scripts/check_docs.py --baseline 4495bf93464f65182107960b814364644fe3d284
```

The program uses decimal arithmetic and checks every economic build against its line-item BOM. It performs **no hardware benchmarks**. [Native market inputs](data/market-inputs.json) · [Economic build assumptions](data/economic-builds.json) · [Full four-scenario comparison](data/break-even.csv) · [All horizon costs](data/cumulative-costs.csv) · [Sensitivity](data/sensitivity.csv)

All new models exclude premises, office and rack rent. Electricity, internet and the optional repair allowance remain separate. The older study and all 195 rental rows remain available with their own dates and assumptions.

Signed-off-by: Alexey Zhokhov
