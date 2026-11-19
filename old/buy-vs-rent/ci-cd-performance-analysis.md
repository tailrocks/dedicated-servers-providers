# Rust, TypeScript and Docker runner capacity

**Research date 20 November 2026, Asia/Saigon.** For one large build, a 5995WX with 256 GB on one non-ECC WRX80 host is the closest purchase candidate to the 9454P. It keeps every dependency, test and service in one memory pool. For independent CI jobs, two 128 GB desktop runners can overlap two builds and isolate their cache and disk activity. The 270K Plus pair is the lower-cost shortlist, and a pair of Ryzen 9950X3D runners is the stronger AMD value option. The distribution of time among clean compilation, incremental checks, tests and I/O determines which choice wins.

[Published measurements](published-benchmarks.md) · [CPU and motherboard comparison](cpu-alternatives.md) · [Purchase configurations](recommended-builds.md)

## What the public evidence measures

**Direct** evidence includes single-core and parallel Clang work rates on a named Hetzner AX162-R, longer independent Chromium builds, a Rust Wasmer compilation profile and Microsoft's TypeScript compiler measurements. **Derived** values below are arithmetic from identified scores or capacities. **Analytical** cases vary an explicit assumption. **Unavailable** covers the exact project, queue trace, peak memory distribution, cache hit rate, SSD model and production jobs/hour. No hardware was accessed and no local benchmark or stress test was run.

| Work on the runner | Concurrency inside one job | Constraint that changes the CPU decision |
|---|---|---|
| Clean `cargo build`, especially release | Cargo can compile independent crates concurrently. Ready build units depend on the package graph. Code generation, optimization, build scripts, linking and LTO can dominate different phases. The default Cargo job cap follows the logical CPU count. | WRX80/EPYC can sustain more independent compilation. A dependency chain or one final link can leave many cores idle. Depending on compiler, profile and linker, a link can itself use multiple threads. Treat a “one-job” build as potentially highly parallel. [Cargo timings](https://doc.rust-lang.org/cargo/reference/timings.html) · [Cargo profiles](https://doc.rust-lang.org/cargo/reference/profiles.html) · [Compiler codegen controls](https://doc.rust-lang.org/rustc/codegen-options/index.html) |
| Incremental Rust build or `cargo check` | `check` avoids final code generation for the checked target. Procedural macros and build dependencies can still require compiled executables. Invalidating a large dependency can fan out across downstream crates. | With a warm target directory, a fast core, low-latency memory and fast metadata reads may matter more than the core count. Incremental is enabled by default in Cargo's development profile and disabled in release. Remote compiler hits shift time into cache retrieval and decompression. [Cargo check](https://doc.rust-lang.org/cargo/commands/cargo-check.html) · [Profile defaults](https://doc.rust-lang.org/cargo/reference/profiles.html) |
| `cargo test`, unit and integration | Building test binaries and running them are separate phases. Cargo runs ordinary test targets in sequence and the harness can run tests within a binary concurrently. Doctests use a different execution model. | Independent CPU-heavy tests exploit cores. Test fixtures, external services, temporary databases, filesystem locks and a large final integration target can set the critical path. `cargo -j` and `--test-threads` address different kinds of concurrency. [Cargo test execution](https://doc.rust-lang.org/cargo/commands/cargo-test.html) |
| TypeScript check/build | The JS compiler through TS6 and TypeScript 7's native compiler have different scaling behavior. TS7 parses, checks and emits in parallel. Its default is four checking workers. A referenced project must have its prerequisites available. | A single JS-bound pass can favor Zen 5 desktop cores. TS7 can give a single job parallel work, and more workers can duplicate state. Four builders × four checkers allow up to 16 checkers inside just one job. Persisted build information can shorten incremental checks. [TypeScript 7](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/) · [Project references](https://www.typescriptlang.org/docs/handbook/project-references.html) |
| JavaScript tooling and Node tests | A JS application thread, independent Node child processes, native tools and worker pools have different limits. Node's isolated test runner can execute files in separate processes. | CPU-heavy file shards can occupy several cores. Concurrent asynchronous waits may use little CPU. Increasing both runner concurrency and per-file workers can increase private heaps and hurt latency. [Node test isolation](https://nodejs.org/api/test.html) · [Node workers](https://nodejs.org/api/worker_threads.html) |
| Docker image build and services | BuildKit executes independent stages in its dependency graph. A cache hit can omit compilation. Cold image pulls, extraction, building source and writing/exporting layers exercise different subsystems. | Native Linux containers share host CPU, memory and storage. BuildKit stages, Cargo jobs and test workers can all run concurrently. CPU quota and memory limits change the effective machine. Remote cache throughput and local NVMe latency can dominate when little code compiles. [BuildKit](https://docs.docker.com/build/buildkit/) · [Cache mounts and layer reuse](https://docs.docker.com/build/cache/optimize/) · [Container resource constraints](https://docs.docker.com/engine/containers/resource_constraints/) |

Microsoft's VS Code project compile used 4.2 GB on TypeScript 7, compared with 5.2 GB on TypeScript 6 on the test system. A job that builds Rust, starts a database and runs a browser can consume substantially more. A package install with thousands of small files exercises metadata and filesystem cache. A registry pull or layer export may be network-bound. At 1 Gbit/s, transferring 10 decimal GB takes at least 80 seconds before protocol costs, compression or disk I/O. Neither a higher core count nor an extra runner removes a saturated common registry link. [Microsoft's measurements](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/) · [Docker cache backends](https://docs.docker.com/build/cache/backends/)

Architecture can affect test coverage as well as duration. The 9454P supports AVX-512, while the submitted Zen 3 5995WX exposes AVX2. When Rust builds use `-C target-cpu=native`, rustc selects the host's features. A job that specifically tests the AVX-512 path cannot run that path on the 5995WX. Projects building for a common portable target have a different requirement. [AX162 instruction sets](https://browser.geekbench.com/v6/cpu/10776095) · [WRX80 instruction sets](https://browser.geekbench.com/v6/cpu/11222188) · [rustc target CPU](https://doc.rust-lang.org/rustc/codegen-options/index.html#target-cpu)

## One job and its critical path

**Analytical example.** On the published 9950X versus AX162 Clang runs, the single-core work-rate ratio is `s = 17.2/10.8 = 1.593` and the parallel ratio is `p = 250.4/327.4 = 0.765`. If a hypothetical job spends fraction `f` of its AX162 time in CPU work that scales like the single-core proxy and the rest like the parallel proxy, its modeled 9950X rate is `1 / (f/s + (1−f)/p)`. The fractions use **baseline elapsed time**, so averaging the two work rates would give a different, incorrect answer. This model assumes the same fixed work and excludes waits and cache changes. [Original AX162 run](https://browser.geekbench.com/v6/cpu/10776095) · [Original 9950X run](https://browser.geekbench.com/v6/cpu/10772280)

| Share of AX162 time behaving like the single-core proxy | Modeled single-9950X job rate, AX162 = 100% |
|---:|---:|
| 0% | 76.5% |
| 25% | 87.9% |
| 50% | 103.3% |
| 75% | 125.3% |
| 100% | 159.3% |

The model enters the 95–105% band at about **37.5–52.3%** single-core-like time. Its 110% and 150% thresholds occur at about **58.6%** and **94.3%**. These percentages are sensitivity thresholds. No publication establishes the user's `f`, or that Rust, the linker and V8 scale like this Clang subtest. If a fraction `w` of baseline time is unchanged local I/O or networking and `f` is within the remaining CPU time, add the wait explicitly: `T_candidate/T_EPYC = w + (1−w) × (f/s + (1−f)/p)`. An ordinary job dispatched to one member of a pair still uses that member.

## Concurrency at 1, 4, 8, 16, 32 and 64 simultaneous jobs

**Derived resource arithmetic.** One 9454P has 48 physical cores, one 5995WX has 64, one 9950X/X3D/X3D2 has 16, and one 270K Plus has 8 performance and 16 efficiency cores. The values below divide physical cores by runnable job count under an even split. For one job on two machines only one host participates. Fractional values describe contention across jobs. They are not scheduler reservations, and P-cores, E-cores and SMT threads have different throughput.

| Simultaneous CI jobs | 9454P cores/job | 5995WX cores/job | One Ryzen cores/job | Two Ryzen cores/job | Two 270K Plus, P+E shares/job | Analytical interpretation |
|---:|---:|---:|---:|---:|---|---|
| 1 | 48 | 64 | 16 | 16 | 8P + 16E | Critical path, usable build parallelism and single-host RAM decide latency. Second worker can handle a different job. |
| 4 | 12 | 16 | 4 | 8 | 4P + 8E | Four substantial clean builds can absorb a wide machine. Two hosts can each run two independent builds and maintain local caches. |
| 8 | 6 | 8 | 2 | 4 | 2P + 4E | Enough distinct work to exploit a pool. Several unbounded Cargo jobs or TS builders can contend long before memory capacity is exhausted. |
| 16 | 3 | 4 | 1 | 2 | 1P + 2E | Narrow tests or checks may still scale. Heavy release compiles now share cores, bandwidth and storage. |
| 32 | 1.5 | 2 | 0.5 | 1 | 0.5P + 1E | A Ryzen pair has one physical core per job on average. High worker counts inside every job increase the runnable queue. |
| 64 | 0.75 | 1 | 0.25 | 0.5 | 0.25P + 0.5E | Only WRX80 has one physical core per job. Even there, 64 fully parallel builds can be memory-bound. Cheap primarily-waiting tests can still coexist. |

**Analytical RAM ceiling.** For a reproducible sizing example reserve **16 GiB per physical host** in total for the OS, services, cache and headroom. Treat a nominal 128/256 GB DIMM configuration as about 128/256 GiB installed and use that reserve before dividing. With `J` equal-size co-running jobs on a host, usable per-job memory is `(installed − reserve)/J`. The reserve is a scenario input. Browser farms, databases and tmpfs might require substantially more.

| Concurrent jobs | One 128 GB host, GiB/job | One 256 GB host, GiB/job | Two 128 GB hosts, GiB/job when balanced |
|---:|---:|---:|---:|
| 1 | 112 | 240 | 112 |
| 4 | 28 | 60 | 56 |
| 8 | 14 | 30 | 28 |
| 16 | 7 | 15 | 14 |
| 32 | 3.5 | 7.5 | 7 |
| 64 | 1.75 | 3.75 | 3.5 |

At an **illustrative 8 GiB peak per job**, one 128 GB host has room for 14, one 256 GB host for 30 and two separate 128 GB hosts for 28 in total. At **16 GiB per job**, those counts become 7, 15 and 14. A single 140 GiB job fits the 256 GB host under this assumption and exceeds each node in the pair. With 64 equally active jobs at 8 GiB per job, 512 GiB of working sets is needed before the host reserve. CPU counts cannot remedy swapping, allocation failures or OOM kills. Conversely, a lightly loaded runner with small working sets may see little benefit from more RAM. [Docker memory and swap behavior](https://docs.docker.com/engine/containers/resource_constraints/)

## When can two desktop runners deliver 10–50% more work?

**Analytical, aggregate only.** Assume a continuing backlog of independent host-sized jobs, each node sustains the published same-work proxy rate, and both can run concurrently. Let `r` be one desktop's published parallel-Clang rate divided by the AX162's 327.4 Klines/s. Let `e` be the useful fraction of the two-node proxy capacity after imbalance, idle time and shared overhead. Then the modeled pool index is `100 × 2 × r × e`. This efficiency is unknown and specific to the workload. It can change when jobs hit an external cache or tests wait on a service. The four rows are assumptions, not measured pair throughput.

| Assumed usable fraction of two-node capacity | 2×9950X, one node 76.5% | 2×9950X3D, one node 78.1–79.8% | 2×270K Plus, one node sample median 74.2% |
|---:|---:|---:|---:|
| 70% | 107.1% | 109.3–111.7% | 103.8% |
| 80% | 122.4% | 125.0–127.7% | 118.7% |
| 90% | 137.7% | 140.6–143.7% | 133.5% |
| 100% ideal arithmetic ceiling for these proxy inputs | 153.0% | 156.2–159.6% | 148.4% |

To reach **110%** on the 9950X3D example, usable pool capacity must be about **69–70%**. To reach **150%**, it must be about **94–96%**. Two unsplittable stages in one dependency chain offer no way to occupy both hosts at the same time. A long nightly queue of independent shards can come much closer. The Intel column uses the six-upload median. Its lowest observed single-node rate, if representative, would put the corresponding ideal pair at only 68.1%. The controlled desktop build reviews support Intel's value while leaving the actual project's throughput unresolved. [Observations, versions and sample limits](published-benchmarks.md)

For operations, **elapsed job time**, **completed jobs/hour** and **queue delay** answer different questions. For a homogeneous continuously busy pool with `J` simultaneously executing jobs and mean execution time `t_J` seconds at that concurrency, completed jobs/hour equals `3600 × J / t_J`. With a fixed submitted batch of `B` jobs, its realized completion rate is `3600 × B / batch makespan in seconds`. Neither formula supplies `t_J` or the makespan. A saturated queue can complete more jobs/hour while individual jobs take longer. One long final shard determines a pipeline's completion time even after the other runner becomes idle.

## Decision for this queue

* **One heavy job or unpredictable peak memory** favors 5995WX/256 GB. The measured multicore compiler rates put it closest to the actual 9454P reference, and every job can use all eight memory channels and one shared address space.
* **Many independent builds of known size** favor two desktop workers. Start the financial comparison with 270K Plus, or choose 9950X3D for the stronger AMD desktop compile evidence. A two-node 9950X3D2 configuration has the highest published mainstream general compilation ceiling among these CPUs. Its roughly 7% same-lab advantage over X3D sets a modest premium limit for value. The 110–150% queue outcome remains conditional on the realized overlap.
* **Warm, lightly threaded feedback jobs** can finish faster on one high-clock Ryzen or Intel worker. **Long clean parallel builds, many CPU-bound tests and memory-heavy service suites** give the wider WRX80/EPYC host a stronger claim. **Registry/network or storage-bound jobs** can converge across CPUs, with queue tails set by cache capacity, local storage contention and remote services.

Existing pipeline logs can place a queue in one of these cases by describing cache hits, queue time, build/test durations and peak resident memory. The buying decision above follows the published evidence without requiring access to either prospective system.

Signed-off-by: Alexey Zhokhov <alexey@zhokhov.com>
