# Should the CI capacity be owned or rented?

[Study index](README.md) · [Exact builds](recommended-builds.md) · [All generated comparisons](financial-results.md) · [Break-even method](break-even-analysis.md)

**20 November 2026.** The decision depends much more on the chosen rental tariff and required memory per job than on the headline CPU price. Buying the closest new 256 GB non-ECC workstation is compelling against the regular Hetzner AX162-2 tariff. It is not a quick saving against the lowest published exact-CPU European offers.

## Comparable capacity before cost

| Owned configuration | Capacity it can replace | Performance interpretation |
|---|---|---|
| SG-WRX256-2, 5995WX / 256 GB / 2 × 2 TB | AX162-2 class: at least 256 GB in one host and 1.92 TB nominal mirrored | Closest non-ECC single-host candidate; compiler proxy around the baseline, production CI equivalence unavailable. |
| SG-WRX128-4, 5995WX / 128 GB / 2 × 4 TB | AX162-1 class: at least 128 GB and 3.84 TB nominal mirrored | Same CPU, all eight channels populated with 16 GB DIMMs; indicative memory price. |
| SG-WRX256-4, 5995WX / 256 GB / 2 × 4 TB | Both capacity classes in one host | S$14,040 components; the bigger pair costs S$710 more. |
| SG-RYZEN128-2 / SG-INTEL128-2 | 128 GB and 2 TB mirrored per host | Lower capacity than A1's mirror and lower memory than A2. Faster serial stages do not create equal aggregate CI throughput. |
| SG-RYZEN2X128-2 / SG-INTEL2X128-2 | Two separate 128 GB / 2 TB mirrors | 256 GB aggregate is **not** a 256 GB single-host replacement. Independent-job queue alternative only. |
| MY-INTEL256-2 | A2 memory and mirror capacity | Modern non-ECC DDR5, four 64 GB DIMMs at a lower supported data rate; CPU remains a smaller parallel-throughput class. |

The matrix intentionally reports all relevant cash comparisons, including mismatches. The CPU, memory, storage and node fields preserve those distinctions. The [published benchmarks](published-benchmarks.md) and [RAM analysis](ram-comparison.md) determine whether a cheaper row is a useful substitute. NM790 lacks capacitor-backed power-loss protection, a feature documented for named enterprise drives such as Micron 7450. The exact AX162 SSD models and their PLP implementation are unestablished. Owning also does not include a rental provider's replacement service. [Storage choices](nvme-comparison.md)

## Four independent ownership scenarios

For the primary Singapore 256 GB workstation, the component subtotal is **S$13,330** and moderate estimated wall consumption is **275 W**. At 730 hours/month and **S$0.3116/kWh**, electricity is **S$62.5537/month** before display rounding. An eligible new **StarHub SME Dynamic 500 Mbps** line adds **S$105/month**, including GST and standard installation under the cited offer. The minimum term is 36 months. Existing suitable internet has zero incremental charge. [Procurement](singapore-hardware.md) · [Electricity](electricity-costs.md) · [Internet](internet-costs.md)

| Ownership scenario | Electricity / month | Internet / month | Maintenance / month | Total recurring ownership charge |
|---|---:|---:|---:|---:|
| Hardware only | S$0 | S$0 | S$0 | S$0 |
| Hardware + electricity | S$62.55 | S$0 | S$0 | S$62.55 |
| Hardware + internet | S$0 | S$105.00 | S$0 | S$105.00 |
| Hardware + both | S$62.55 | S$105.00 | S$0 | S$167.55 |

Hardware-only and internet-only are the requested excluded-cost comparisons; a real operating computer still consumes electricity. The table never assumes that electricity is physically free. No premises, rack or office rent enters any scenario. New cooling equipment, a UPS, spare parts and assembly are not silently included. No supplier quote was recovered for a required extra in these builds. An optional 3%-of-hardware annual repair budget is explicitly modeled only in sensitivity.

## Selected break-even results

Figures are **first whole months**, using new-rental setup and unchanged quoted rates. Electricity is moderate; internet means one separate business line for the site, including when two nodes share it. Values beyond 60 months are mathematical extrapolations with no assumption that old hardware or prices remain attractive that long.

| Owned build / component cost | Rented alternative | Hardware only | + electricity | + internet | + both |
|---|---|---:|---:|---:|---:|
| **5995WX 256 GB / S$13,330** | **Hetzner AX162-2**, SG non-GST-registered buyer | **10** | **11** | **11** | **12** |
| Same | UHost 9454P / 256 GB | 47 | 60 | 74 | 114 |
| Same | ServerWala 9454P / 256 GB, monthly | 31 | 37 | 41 | 51 |
| Same | 040Hosting 9454P / 256 GB, legacy listing | 39 | 48 | 57 | 78 |
| Same | Arxan 9454P / 256 GB, observed 11% levy included | 44 | 55 | 67 | 97 |
| **5995WX 128 GB / 2 × 4 TB / S$10,022 indicative** | **Hetzner AX162-1**, SG non-GST-registered buyer | **11** | **11** | **12** | **13** |
| Same | PlusClouds 9454P / 128 GB / 2 × 3.84 TB | 30 | 37 | 43 | 61 |
| **One 9950X3D / S$5,114** | DediJet Singapore one 9950X / 128 GB | 15 | 18 | 22 | 27 |
| Same, lower parallel CPU class | UHost 9454P / 256 GB | 18 | 22 | 28 | 38 |
| **Two 9950X3D / S$10,228** | Two DediJet Singapore 9950X nodes | 15 | 18 | 18 | 21 |
| Same, analytical pool comparison | One UHost 9454P / 256 GB | 36 | 54 | 57 | 122 |
| **One 270K Plus / S$4,757** | One DediJet Singapore 9950X node | 14 | 17 | 20 | 26 |
| **MY 270K Plus / 128 GB / RM19,153** | UHost 9454P / 256 GB | 21 | 23 | 25 | 28 |
| **MY 270K Plus / 256 GB / RM32,211** | UHost 9454P / 256 GB | 36 | 40 | 42 | 47 |

Every quoted monthly entry, every priced build and all seven horizons are in [break-even.csv](data/break-even.csv). Sources and taxes are in [rental-market-update.md](rental-market-update.md) and [market-inputs.json](data/market-inputs.json). These comparisons do not claim equal service: regular Hetzner prices include the documented SG 9% scenario and IPv4, while UHost and other third-party quotes retain unknown buyer-specific taxes. The 040Hosting price is specifically a legacy listed SKU. Arxan's deployed location and foreign payment route remain unresolved. No provider is represented as having allocated a server.

## Cumulative cost at every requested horizon

Primary 256 GB workstation against the A2-class rentals, **SGD**. The UHost column is its known-charge subtotal; Hetzner includes 9% SG tax. All are undiscounted cumulative costs at the snapshot exchange rate.

| Months | Buy: hardware | Buy: + electricity | Buy: + internet | Buy: + both | Rent: UHost A2 | Rent: Hetzner A2 |
|---|---:|---:|---:|---:|---:|---:|
| 6 | 13330.00 | 13705.32 | 13960.00 | 14335.32 | 1857.12 | 8472.24 |
| 12 | 13330.00 | 14080.64 | 14590.00 | 15340.64 | 3559.48 | 16297.06 |
| 18 | 13330.00 | 14455.97 | 15220.00 | 16345.97 | 5261.83 | 24121.87 |
| 24 | 13330.00 | 14831.29 | 15850.00 | 17351.29 | 6964.19 | 31946.68 |
| 36 | 13330.00 | 15581.93 | 17110.00 | 19361.93 | 10368.91 | 47596.30 |
| 48 | 13330.00 | 16332.58 | 18370.00 | 21372.58 | 13773.62 | 63245.93 |
| 60 | 13330.00 | 17083.22 | 19630.00 | 23383.22 | 17178.34 | 78895.55 |

At 36 months with an existing line, this owned machine costs **S$15,581.93**. UHost costs **S$10,368.91**, a **S$5,213.02 advantage for renting** before unquoted charges. Monthly ServerWala costs **S$15,553.36**, just **S$28.57 less than owning**: a transaction fee, tax difference or small procurement-price change can reverse that near tie. Regular Hetzner A2 costs **S$47,596.30**, so owning saves **S$32,014.37** against that tariff. Choosing the expensive reference as the only comparison would obscure the actual market decision.

## Performance-adjusted value is a different question

The following index uses only the **named Linux AVX2 Clang subtest**, with AX162's published 327.4 Klines/s = 100. It is not a blended CI score. For X3D the arithmetic mean of two published work rates is used; for Intel the six-submission median is used, retaining its broad spread in the evidence document. The two-node row applies an explicit, unmeasured 80% pool-efficiency assumption. [Observed inputs](published-benchmarks.md)

| 36-month option | Normalized Clang proxy | Cost with electricity / existing internet | SGD per proxy point | Cost with electricity / new business line | SGD per proxy point |
|---|---:|---:|---:|---:|---:|
| 5995WX / 256 GB / 2 × 2 TB | 102.96 | 15581.93 | 151.34 | 19361.93 | 188.05 |
| 5995WX / 128 GB / 2 × 4 TB | 102.96 | 12273.93 | 119.21 | 16053.93 | 155.92 |
| One 270K Plus / 128 GB | 74.18 | 6640.44 | 89.52 | 10420.44 | 140.48 |
| One 9950X3D / 128 GB | 78.96 | 6833.66 | 86.55 | 10613.66 | 134.43 |
| Two 9950X3D, **assumed 80% scaling** | 126.33 | 13667.32 | 108.19 | 17447.32 | 138.11 |
| UHost same-CPU reference class | Assumed 100 | 10368.91 | 103.69 | 10368.91 | 103.69 |
| ServerWala monthly same-CPU reference class | Assumed 100 | 15553.36 | 155.53 | 15553.36 | 155.53 |
| Hetzner AX162-2, SG buyer scenario | 100 reference | 47596.30 | 475.96 | 47596.30 | 475.96 |

Lower SGD/point is better only for that workload and scope. The inexpensive X3D wins this ownership proxy while offering 128 GB per host and less aggregate capacity. UHost still beats the modeled two-X3D pool at 36 months with an existing line on this proxy. A busy queue, lower single-job latency, local placement and longer ownership may favor the pool; none is captured by pretending its RAM is one address space. Rental network connectivity is already in rent, so no office internet charge is added to the rental columns. [Owned proxy data](data/performance-value.csv) · [Same-CPU rental proxy data](data/rental-performance-value.csv)

For real build latency, GamersNexus measured Chromium at 95 minutes on 9950X3D, 101 on 9950X and 103 on 270K Plus; X3D2 took 88.1 minutes. These comparisons independently support the desktop choice, but the same lab did not include the EPYC. An EPYC-normalized full-pipeline value score is therefore unavailable. See the [CPU value comparison](cpu-alternatives.md), including why Malaysia's smaller X3D2 whole-build premium changes the local value result.

Signed-off-by: Alexey Zhokhov
