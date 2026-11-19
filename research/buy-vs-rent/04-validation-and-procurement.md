# CI workload validation and procurement requirements

Updated: **20 November 2026**. This procedure makes the requested 3–5% performance tolerance measurable. It has **not** been executed against the user's repositories. No hardware or hosting was bought, no account was created, and no vendor was contacted during the research.

## 1. Acceptance criteria

Use the actual AX162 as the baseline, with the same representative repository commits, toolchain versions and build flags. Define two separate success measures:

1. **Individual job latency:** representative job duration no greater than 1.05 times the AX162 duration for a 5% tolerance. Use 1.03 if the user chooses a 3% tolerance.
2. **Busy-queue throughput:** completed jobs per hour at least 0.95 times the AX162 rate for a 5% throughput tolerance, or at least **0.97 times** for a 3% tolerance. Report this independently from latency.

A machine can pass one measure and fail the other. Predeclare representative jobs, required metrics and tolerance before testing. Require **both** critical-job latency and sustained queue throughput by default for full CI equivalence; a throughput-only or latency-only acceptance is an explicit narrower requirement. If run-to-run variability or measurement uncertainty spans the threshold, the result is unresolved rather than a pass. A two-node runner pool must be tested as a two-node pool; adding single-host benchmark scores is not a measurement. If claiming a 10–50% improvement, identify whether that means jobs/hour or elapsed time. For example, a 25% higher work rate is a 20% shorter duration for the same perfectly scalable workload.

The whole required job must fit in the candidate host's usable memory and storage after reserving capacity for the OS, service containers, caches and other concurrent jobs. Aggregate RAM across hosts cannot satisfy one process's memory requirement. Report the maximum supported job size alongside throughput.

## 2. Representative CI replay

| Workload | Conditions to capture | Primary measurements |
|---|---|---|
| Rust debug/check build | Cold dependency/artifact state and normal warm state | Elapsed time, CPU use, peak RSS, cache size |
| Rust release build | Exact production/test optimization flags, linker and target | Elapsed time, peak RSS, linker behavior |
| Rust test suite | Real test parallelism and backing service containers | Pass/fail, elapsed time, p95 job latency |
| TypeScript build/type check | Pinned compiler and runtime versions | Elapsed time, CPU scaling, peak memory |
| JavaScript/TypeScript tests | Actual test-runner shard/worker count | Jobs/hour and latency |
| Docker image build | Identical base-image, registry and BuildKit cache conditions | Build time, network transfer, storage writes |
| Concurrent queue | Start with 1, 2, 4, then more concurrent jobs where appropriate | Sustained completions/hour, queue time, memory pressure |
| Largest expected job | Production-size monorepo/service/test data | Fit without OOM, unacceptable swapping or storage exhaustion |

Run at least five repeats for useful median comparisons, then run a longer representative queue (for example an hour or more) to reveal thermal and storage behavior. Five samples alone do not establish a reliable p95; collect enough queue jobs for tail metrics. Keep cold and warm results separate.

Record the OS/kernel, `rustc -Vv`, Cargo version, Node/runtime version, TypeScript version, linker, Docker/BuildKit versions, CPU power limits, BIOS, DIMM layout/speed, SSD model/firmware and filesystem. Do not compare architecture-specific `target-cpu=native` builds as if they produced equivalent artifacts; either use the same deployment target or explicitly classify that separate experiment.

`docker build --no-cache` does not by itself remove every possible cache, downloaded base image, package mirror or BuildKit cache mount. Specify and reproduce the intended cache state. Include registry/image download time in the end-to-end test, while also reporting a compute-only warmed test to explain bottlenecks.

## 3. CPU and RAM scheduling

[Cargo supports explicit job limits](https://doc.rust-lang.org/stable/cargo/commands/cargo-build.html) and [configuration through `build.jobs` / `CARGO_BUILD_JOBS`](https://doc.rust-lang.org/stable/cargo/reference/config.html). Coordinate the CI scheduler's concurrent job count, container CPU/memory limits and compiler jobs. Several independent builds can otherwise compete for more CPU and RAM than the host can supply.

Size memory as concurrent job peak resident memory plus service containers, filesystem cache and host headroom. Threads are not a RAM-sizing rule. Avoiding an OOM or swap storm is worth more than a modest timing improvement.

Use a supported native Linux environment and validate sustained stock-supported CPU settings first. Advertised peak boost, a cooling product's rated watts, and the PSU's nameplate watts are not measurements of sustained compilation or whole-machine consumption. Measure average wall power over the actual CI duty cycle, including idle periods.

## 4. Cache and storage configuration

[Docker's cache guidance](https://docs.docker.com/build/cache/optimize/) covers layer ordering, cache mounts and external cache reuse. Preserve dependency cache value without confusing it with cold-build speed. Keep active workspace and hot caches on local NVMe; a shared network filesystem can change the result substantially.

Use mirroring when local continuity matters. Disposable workers may use a single local SSD and reconstruct caches after a failure, provided code and important artifacts are retained elsewhere. That is an explicit availability trade-off, not free redundancy.

Measure storage temperatures, I/O wait, write volume and sustained throughput while several builds run. Keep suitable free-space headroom and monitor NVMe health. Confirm actual usable capacity after mirroring and filesystem overhead.

The [TypeScript 7 announcement](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/) describes its native Go implementation and multithreading. Do not assume every TypeScript workload is single-threaded; benchmark the version actually pinned by the project. This research does not assume that upgrading the compiler gives a particular speedup for these repositories.

## 5. Required information for an owned-system quote

| Area | Information the quote must fix |
|---|---|
| CPU | Exact model, condition, availability, warranty and supported board/BIOS |
| RAM | Exact part and revision, number of modules, qualified populated slots, tested operating speed and non-ECC requirement |
| Motherboard | Exact revision, BIOS, memory qualification, NVMe lane layout, console/remote-management capability |
| Storage | Exact SSD capacities/models, warranty/TBW, heatsink clearance, expected layout and usable capacity |
| Cooling | Correct socket mount and full-package contact, cooler/RAM clearance, continuous load test at deployment ambient temperature |
| Chassis | Actual board dimensions and standoffs, cooler clearance, airflow, rack rails where required |
| PSU | Required CPU power connectors, quality, warranty and load margin; rated watts are not continuous usage |
| Total price | GST treatment, delivery, assembly, system burn-in, lead time and whole-system support responsibility |

For WRX80, require the exact validated eight-module Crucial revision or an explicitly qualified replacement, BIOS 1003 or a later supported version, and the motherboard's required supplemental power connections with the correct EPS/PCIe cables. For the 128 GB desktop builds, specify the exact KLEVV kit. The proposed 64 GB Lexar kit and eight-module 16 GB DDR4 alternative still need exact qualification.

The 5995WX board has BMC display/remote management. The proposed mainstream MSI boards do not provide the same server-management arrangement. If those desktops will be unattended in a remote location, price the required external KVM, remote power control, or provider service. That cost is not included in the basic parts totals.

## 6. Required information for a rented-server quote

Request the exact physical location and CPU/socket count, RAM capacity and DIMM population, SSD model/count/capacity, whole-host dedicated access, port speed and committed bandwidth, transfer cap and overage/throttling, one-time setup, invoice currency and taxes, minimum commitment, renewal price, cancellation rule, delivery date and hardware-replacement process.

A provider's city landing page does not establish that every advertised SKU is stocked there. A 24-month monthly-equivalent advertisement is not a one-month trial price. A billable port's nominal speed is not necessarily committed throughput. Provider SLA language is a contract claim, not a measured availability result from this research.

The PowerDedi listing had contradictory location/availability labels; ServerPacket's Malaysia 9754 price had conflicting promotion/renewal cues. Resolve those before using the advertised rates as firm TCO inputs. Crypto-only payment is a concrete procurement constraint on some low-price listings. No reliability endorsement or completed supplier due diligence is implied by their inclusion.

## 7. Colocation acceptance

Have the facility approve the actual hardware, chassis, dimensions, weight, non-ECC workstation use, airflow, peak and sustained wall power, number of power feeds, console access, rails/shelf, IPs, bandwidth, technician tasks and charges.

The original Meshify 2 XL tower cannot be assigned a 1U or 2U tariff. Its smallest dimension is 240 mm; a nominal 5U height is 222.25 mm, and a tower's other dimensions also matter. Use an expressly accepted tower service or a suitable rack chassis. A 13 A outlet description is not a 13 A purchased power allowance. A 460 W plan must accommodate measured peaks and the provider's actual power policy, not just an assumed 350 W average.

For the 5U Singapore scenario, the research substitutes the SilverStone RM51 and separately prices RMS05-22 rails. For the conditional 4U Malaysia scenario, RM44 cooler clearance is only 148 mm when its expansion-card retainer is removed; the 145 mm ARCTIC cooler leaves just 3 mm of nominal clearance. The exact board width, standoffs, cables, intake fans, airflow and assembly must be checked; extra fans and fitting are not silently priced at zero. The facility should approve peak wall power/current as well as the average. Do not count cooling electricity again if it is already included in a colocation plan.

## 8. How to decide on value

After validation, calculate:

`cost per successful CI job = total cost over the chosen period / successful completed representative jobs`

Include actual utilization, outages and job failures. Use queue latency as a second criterion; a cheap high-throughput machine can still be unacceptable if critical-path jobs finish late. For two-node options, retain the per-host memory and storage constraints.

If the duration of need is uncertain, a short rental commitment has value beyond a three-year cost table; a powered-off allocated dedicated server still has the modeled recurring bill. A reliable existing site can improve ownership economics; office rent is excluded from every scenario, and electricity and internet are independent choices. The repository's cheaper European rental candidates can remain below the ownership budget with selected costs. Use the [initial 104-rental coverage](05-repository-rental-comparison.md) plus [the 15 latest additions](08-latest-rental-comparisons.md), not only regular Hetzner pricing. Keep an inexpensive existing rental's actual invoice in the comparison. AX162-LTD is unavailable in the repository's latest inventory evidence and is only a historical sensitivity.

## 9. Review and remaining evidence gaps

Research was delegated to GPT-6.2 Astra at max reasoning; GPT-6.2 Sol at max independently reviewed the hardware and rent-versus-buy work. The review checked part totals, memory compatibility, CPU/benchmark interpretation, currency conversion, taxes-as-scenarios, power assumptions, rack conversion and cost arithmetic.

The remaining gaps are substantive: no actual repository replay, no measured candidate wall power, no supplier-reserved stock, no assembled quote, no confirmed colocation acceptance and no customer-specific tax determination. The documents label these as conditions rather than treating them as completed tests or confirmed purchases.
