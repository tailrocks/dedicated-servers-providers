# Online-only hardware buying study — 20 November 2026

[Repository home](../README.md) · [New study](../old/buy-vs-rent/README.md) · [195-offer catalog](../rentals/README.md) · [Research archive](README.md)

## Scope and integration

The user requested a complete internet-only recommendation for a non-ECC desktop/workstation in Singapore first or Malaysia second, running Rust, TypeScript and Docker CI/CD, against EPYC 9454P performance and rented-server economics. The destination was explicitly `old/`; the new study is therefore under `old/buy-vs-rent/` despite being the newer decision document.

Research began at `5b26e01a2165d686d1094ad3173152700fb00157`, with 170 catalog rows. During the work, main advanced to the signed 195-offer expansion at `4495bf93464f65182107960b814364644fe3d284`; the working branch was fast-forwarded to preserve all of it. No rental row or dated report was deleted, rewritten or recast as a newly allocated server. The new study adds the material UHost extra-disk and 040Hosting legacy cases from that expansion and a refreshed PlusClouds 256 GB comparison. The older 141-offer ownership analysis retains its original assumptions and results.

## Material findings

- **Closest non-ECC single host:** 5995WX on WRX80 with eight qualified DDR4 UDIMMs. The parallel Clang ratio is about baseline scale, but published observations do not establish 3–5% end-to-end customer CI equivalence. A two-host Ryzen pool has separate memory spaces and analytical queue efficiency, never a fabricated measured pipeline rate.
- **Current procurement changes the economic result:** the strict new 256 GB build is **S$13,330**, with exact new Kingston modules priced at S$858 each. The earlier S$210 Crucial offer and several old cooling/case variants report unavailable. The lower refurbished memory basket remains an explicitly conditional alternative, with quantity/revision/warranty uncertainty.
- **Desktop value:** SG 9950X3D at S$5,114 and Intel 270K Plus at S$4,757 are cheaper fast-pipeline options, with lower aggregate CPU/memory capacity than the consolidated reference. Modern Threadripper alternatives requiring ECC RDIMMs fail the purchased-memory restriction. Malaysia's smaller whole-build X3D2 premium changes that local value choice.
- **Storage:** 2 × 2 TB or 2 × 4 TB NM790 is the value default. Sustained write evidence, endurance, thermal behavior, RAID1 capacity and absence of enterprise power-loss protection are explicit. PCIe 5 peak speed alone does not justify a CI premium.
- **Economics:** strict 256 GB WRX80 against UHost is **47 / 60 / 74 / 114 whole months** for hardware / electricity / internet / both. Against regular AX162-2 in the stated SG-buyer scenario it is **10 / 11 / 11 / 12 months**. These are known-charge cash comparisons, with capacity, source uncertainty and tax basis visible.

## Reproducible outputs and review

The study includes 18 complete priced build variants, exact procurement JSON, dated market inputs, decimal-arithmetic calculations, four independent utility combinations and seven requested horizons. Prepaid rental cash, minimum contract exposure, optional repair reserves, FX/tariff/hardware changes and named compiler-proxy value are separate. No premises or rack rent enters the new model. [Generated tables](../old/buy-vs-rent/financial-results.md) · [Calculation method](../old/buy-vs-rent/break-even-analysis.md)

Primary research workers used **GPT-6.2 Astra with maximum reasoning effort**. A separate **GPT-6.2 Sol with maximum reasoning effort** independently checked source evidence, compatibility, procurement, formulas and generated values. Corrections include exact SKU stock handling, memory qualification levels, annual payment scenarios, a missing rental CPU selector, monthly versus contracted exposure, CSV line endings and several documentary source corrections. [Complete validation record](../old/buy-vs-rent/review-and-validation.md)

No hardware benchmark, stress test, physical assembly, supplier contact, purchase or reservation was performed. The recommendation is complete from available public evidence. Root README, research index, historical ownership entry points and methodology now distinguish the new decision from the preserved study.

Signed-off-by: Alexey Zhokhov
