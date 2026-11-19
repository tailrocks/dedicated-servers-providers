# Hardware purchase break-even across all 104 rental offers

**How many months of rent buy a server?** On UHost’s Helsinki A2 quote, S$8,609.40 of Singapore hardware equals **30.34 months of recurring rent**. The provider also lists USD 120 setup. Counting that fee on a new rental moves hardware-only break-even to **29.80 months**. Counting both electricity and internet on the owned host moves it to **54.86 months**, or month 55 on monthly billing. For the A1 server with the larger mirrored drives, BizoSiz gives **24.71 months of recurring rent**, **24.31 months** including setup and **38.0006 months** including setup and both operating costs. The first completed month at or beyond that last threshold is **39**. Supply, taxes and actual CI performance remain unverified. [Recorded UHost quotes](../2026-11-19-global.md#exact-cpu-published-qualifying-offers) · [BizoSiz carts](../2026-11-20-exact-cpu.md#bizosiz)

The [rental inventory and evidence](05-repository-rental-comparison.md) supplies 104 rows from 38 alternative brands plus Hetzner. The tables below cover 32 A1-only offers, 32 A2-only offers, two that fit both and 38 that miss both. Evaluating each dual-profile offer against both hardware prices gives **68 capacity-matched comparisons** across 66 distinct offers. Numbered entries keep their original IDs and primary offer links. This appendix prices Singapore parts and electricity. The companion report covers Malaysia, alternative parts, and optional cooling under the same four scenarios. [Direct Singapore and Malaysia comparisons](06-direct-payback.md) · [November 2026 rental snapshot][snapshot]

## Hardware, utilities and rental prices

| Owned Singapore hardware | Parts price H | Capacity reproduced by rental |
|---|---:|---|
| A1 · 5995WX / WRX80, 128 GB non-ECC, 2 × 4 TB Samsung 990 PRO NVMe | S$8,891.00 | At least 128 GB and two drives of at least 3.84 TB each |
| A2 · 5995WX / WRX80, 256 GB non-ECC, 2 × 2 TB Samsung 9100 PRO NVMe | S$8,609.40 | At least 256 GB and two drives of at least 1.92 TB each |

| Monthly costs counted on the owned host | Electricity | Internet | Total O per month |
|---|---:|---:|---:|
| Neither utility | — | — | S$0 |
| Electricity only | S$79.6138 | — | S$79.6138 |
| Internet only | — | S$50 | S$50 |
| Electricity and internet | S$79.6138 | S$50 | S$129.6138 |

The server’s 350 W average wall draw is a planning assumption. `0.350 kW × 730 hours × S$0.3116/kWh = S$79.6138/month` of electricity. The four columns use the server draw alone. To add the separate 25% room-cooling allowance used in the expanded ownership budget, add S$19.90345/month when electricity is counted. This makes electricity plus cooling S$99.51725/month, or S$149.51725 with internet. Internet is an assumed incremental S$50/month. A dash omits a charge from that scenario, and the underlying service can still cost money. All four scenarios use **zero office rent**. The purchase outlay is parts only. UPS, assembly, repairs, labour, financing and resale fall outside this calculation. The broader ownership budgets include different items. [Hardware bill of materials](01-hardware-and-performance.md) · [Regional utility evidence](02-rental-market.md) · [Ownership budget](03-rent-vs-buy-tco.md)

For an invoice of `Q` SGD covering `p` months, effective recurring rent is `R = Q / p`. `F` is the one-time rental setup fee in SGD. The tables retain the native invoice and convert using **19 November 2026** rates of EUR 1 = SGD 1.4176 = USD 1.0992 = BRL 6.4765. Each USD amount is multiplied by `1.4176 / 1.0992`, each BRL amount by `1.4176 / 6.4765`. The calculations use unrounded rates and native term invoices. The reference Hetzner row is ex VAT and IPv4. Other rows keep their original known or unknown tax basis. Buyer-specific tax, FX spreads, traffic, IP and other charge changes can alter the payable amounts. [FX and per-offer tax evidence](05-repository-rental-comparison.md#reading-the-full-comparison)

### How to read a payback cell

Each cell is **months ignoring rental setup / months including the quoted setup**. For instance, `30.34 / 29.80` in the neither-utility column means the parts price equals 30.34 recurring rental payments, and a new rental with the stated setup reaches equal cumulative cost in 29.80 months. Avoided setup makes buying pay back sooner. For a continuing lease whose setup was paid already, the first number applies to future spending.

| Comparison | Calculation | Interpretation |
|---|---|---|
| Parts divided by recurring rent | `H / R` | Left number under neither utility. Measures how many monthly rental charges equal the hardware price. |
| Parts plus selected utilities, ignoring rental setup | `H / (R − O)` | Left number in each scenario. If setup was omitted in the offer, this remains an expressly zero-setup sensitivity. |
| Parts plus selected utilities, including quoted rental setup | `(H − F) / (R − O)` | Right number in each scenario. Equates `H + nO` to `F + nR`. `N/Q` means the setup-adjusted result is unquoted. |

The monthly calculation applies when hardware initially costs more than setup and `R > O`. If `H > F` and `R ≤ O`, ownership never recovers its initial premium. If `H ≤ F` and `R ≥ O`, ownership is already no dearer at purchase. If `H < F` and `R < O`, higher owner operating costs reverse the initial advantage after `(F − H) / (O − R)` months. When `H = F` and `R < O`, the two sides tie at purchase and renting is cheaper thereafter. For every capacity match here, the advertised monthly equivalent exceeds the largest modeled operating cost, and every known setup is below its matched parts price.

For monthly billing, round the **unrounded** fractional crossing up to the first completed month in which ownership costs no more. The tables display two decimal places, with extra digits when rounding to an integer would move the whole-month answer one month early. For prepaid terms, the fractional result expresses the cost of the service months consumed. Cash paid and minimum contract liability can cross on different dates. [Prepaid cash calculations](#prepaid-cash-and-contract-commitments)

`F = 0` applies only to an explicitly free or waived setup in the setup-adjusted calculation. A blank fee in a selected cart gives `N/Q` on the right, even if the first payment shown equals one month’s rent. For Lindau, the left number also assumes the advertised **from** rate is obtainable. Minimum terms, address-dependent tax, stock and shared upstream supply can all affect the result. The figures use hardware capacity as an initial screen. Passing the 3–5% CI tolerance requires running the actual workload on the proposed system. [Seller evidence](05-repository-rental-comparison.md) · [CI acceptance test](04-validation-and-procurement.md)

## How many models cross within 36 months?

Counts use setup-adjusted monthly-equivalent results only where the fee is stated. Each dual-profile rental is eligible for both profiles when it has a stated fee. The unknown-fee rows remain in the detailed tables with their recurring-only sensitivities.

| Profile | Fee stated | Neither utility | Electricity only | Internet only | Both utilities | Fee unknown |
|---|---:|---:|---:|---:|---:|---:|
| A1 | 24 | 24 | 24 | 24 | 21 | 10 |
| A2 | 21 | 21 | 20 | 20 | 18 | 13 |

With both utilities counted, PlusClouds S, HummingTribe and BizoSiz S cross after month 36 for A1. For A2, they are UHost R, PlusClouds R and BizoSiz R. Provisov A2 reaches equality at 32.27 months in this parts-and-utilities model. Its recorded quote also has an unconfirmed minimum term. The [full office budgets](05-repository-rental-comparison.md#which-rentals-change-the-buying-decision) add UPS and assembly, a repair reserve and room cooling. Those items move Provisov’s three-year comparison back in favour of renting.

## A1 only

Compare these 32 offers with the **S$8,891.00** A1 parts price. Every pair is recurring-only / setup-adjusted months.

| Rental ID and offer | Native rent per cycle + setup | Effective R, S$/mo | Neither, months | Electricity only | Internet only | Both utilities |
|---|---|---:|---:|---:|---:|---:|
| 005 [PlusClouds / Radius AX162-S, FI/DE][r5] | EUR 229/mo + 411 · term N/Q | 324.63 | 27.39 / 25.59 | 36.29 / 33.91 | 32.37 / 30.25 | 45.59 / 42.60 |
| 006 [HummingTribe Dedicated Power, Germany][r6] | EUR 249.99/mo + 449 | 354.39 | 25.09 / 23.29 | 32.36 / 30.04 | 29.21 / 27.12 | 39.56 / 36.72 |
| 008 [BizoSiz AX162-S, DE/FI][r8] | USD 279/mo + 111 | 359.82 | 24.71 / 24.31 | 31.73 / 31.22 | 28.70 / 28.24 | 38.62 / 38.0006 |
| 016 [AMS SOFT AX162-S, Finland][r16] | BRL 1,989.90/mo + N/Q | 435.56 | 20.41 / N/Q | 24.98 / N/Q | 23.06 / N/Q | 29.06 / N/Q |
| 017 [Pro-m, Finland][r17] | USD 347/mo + 527 · 1-mo min | 447.51 | 19.87 / 18.35 | 24.17 / 22.32 | 22.37 / 20.66 | 27.97 / 25.83 |
| 023 [UHost AX162-S, Helsinki][r23] | USD 363/mo + 120 | 468.15 | 18.99 / 18.66 | 22.88 / 22.49 | 21.26 / 20.89 | 26.26 / 25.81 |
| 024 [CTCServers, Falkenstein][r24] | USD 364/mo + 1,496.35 | 469.44 | 18.94 / 14.83 | 22.81 / 17.86 | 21.20 / 16.60 | 26.16 / 20.48 |
| 026 [iDatam, Falkenstein][r26] | USD 364/mo + 1,496.35 | 469.44 | 18.94 / 14.83 | 22.81 / 17.86 | 21.20 / 16.60 | 26.16 / 20.48 |
| 027 [GTZHost, Helsinki][r27] | USD 365/mo + 1,134.69 | 470.73 | 18.89 / 15.78 | 22.73 / 18.99 | 21.13 / 17.65 | 26.06 / 21.77 |
| 028 [Servers99, Helsinki][r28] | USD 365/mo + 1,134.69 | 470.73 | 18.89 / 15.78 | 22.73 / 18.99 | 21.13 / 17.65 | 26.06 / 21.77 |
| 029 [BytesRack, Helsinki][r29] | USD 366/mo + 1,134.69 | 472.02 | 18.84 / 15.74 | 22.66 / 18.93 | 21.07 / 17.60 | 25.97 / 21.69 |
| 030 [GTZHost, Falkenstein][r30] | USD 367/mo + 1,496.35 | 473.31 | 18.78 / 14.71 | 22.58 / 17.68 | 21.0037 / 16.44 | 25.87 / 20.25 |
| 031 [KW Servers, Falkenstein][r31] | USD 367/mo + 1,496.35 | 473.31 | 18.78 / 14.71 | 22.58 / 17.68 | 21.0037 / 16.44 | 25.87 / 20.25 |
| 033 [KW Servers, Helsinki][r33] | USD 369/mo + 1,134.69 | 475.89 | 18.68 / 15.61 | 22.44 / 18.74 | 20.88 / 17.44 | 25.68 / 21.45 |
| 034 [Pro-m, Germany][r34] | USD 369/mo + 527 · 1-mo min | 475.89 | 18.68 / 17.25 | 22.44 / 20.72 | 20.88 / 19.28 | 25.68 / 23.71 |
| 036 [Servers99, Falkenstein][r36] | USD 369/mo + 1,496.35 | 475.89 | 18.68 / 14.63 | 22.44 / 17.57 | 20.88 / 16.35 | 25.68 / 20.10 |
| 037 [LeoServers, Falkenstein][r37] | USD 370/mo + 1,496.35 | 477.18 | 18.63 / 14.59 | 22.36 / 17.51 | 20.81 / 16.30 | 25.58 / 20.03 |
| 038 [LeoServers, Helsinki][r38] | USD 370/mo + 1,134.69 | 477.18 | 18.63 / 15.57 | 22.36 / 18.68 | 20.81 / 17.39 | 25.58 / 21.37 |
| 048 [XHN.ES, Finland][r48] | EUR 380/mo + 99 | 538.69 | 16.50 / 16.24 | 19.37 / 19.06 | 18.19 / 17.91 | 21.73 / 21.39 |
| 050 [EPY Host, Falkenstein][r50] | USD 423/mo + N/Q | 545.53 | 16.30 / N/Q | 19.08 / N/Q | 17.94 / N/Q | 21.38 / N/Q |
| 052 [Servers99, Falkenstein][r52] | USD 424/mo + N/Q | 546.82 | 16.26 / N/Q | 19.03 / N/Q | 17.90 / N/Q | 21.31 / N/Q |
| 054 [LeoServers, Falkenstein][r54] | USD 425/mo + N/Q | 548.11 | 16.22 / N/Q | 18.98 / N/Q | 17.85 / N/Q | 21.25 / N/Q |
| 056 [GTZHost, Falkenstein][r56] | USD 427/mo + N/Q | 550.69 | 16.15 / N/Q | 18.87 / N/Q | 17.76 / N/Q | 21.12 / N/Q |
| 057 [iDatam, Falkenstein][r57] | USD 427/mo + N/Q | 550.69 | 16.15 / N/Q | 18.87 / N/Q | 17.76 / N/Q | 21.12 / N/Q |
| 058 [CTCServers, Falkenstein][r58] | USD 428/mo + N/Q | 551.98 | 16.11 / N/Q | 18.82 / N/Q | 17.71 / N/Q | 21.05 / N/Q |
| 059 [KW Servers, Falkenstein/Nuremberg][r59] | USD 429/mo + N/Q | 553.27 | 16.07 / N/Q | 18.77 / N/Q | 17.67 / N/Q | 20.99 / N/Q |
| 064 [Servers99, Nuremberg][r64] | USD 432/mo + N/Q | 557.14 | 15.96 / N/Q | 18.62 / N/Q | 17.53 / N/Q | 20.80 / N/Q |
| 095 [IP-Projects, Frankfurt][r95] | EUR 11,780.29/24 mo + 0 | 695.82 | 12.78 / 12.78 | 14.43 / 14.43 | 13.77 / 13.77 | 15.70 / 15.70 |
| 098 [IP-Projects, Frankfurt][r98] | EUR 6,084.32/12 mo + 342.85 | 718.76 | 12.37 / 11.69 | 13.91 / 13.15 | 13.29 / 12.57 | 15.09 / 14.27 |
| 100 [IP-Projects, Frankfurt][r100] | EUR 539.39/mo + 342.85 · 12-mo min | 764.64 | 11.63 / 10.99 | 12.98 / 12.27 | 12.44 / 11.76 | 14.0010 / 13.24 |
| 103 [iTHOSTER AX162-S, Helsinki/Falkenstein][r103] | USD 663/mo + 100 | 855.05 | 10.40 / 10.25 | 11.47 / 11.30 | 11.04 / 10.88 | 12.26 / 12.08 |
| 104 [Hetzner AX162-1, DE/FI][r104] | EUR 612.30/mo + 304 | 868.00 | 10.24 / 9.75 | 11.28 / 10.73 | 10.87 / 10.34 | 12.04 / 11.46 |

## A2 only

Compare these 32 offers with the **S$8,609.40** A2 parts price. Every pair is recurring-only / setup-adjusted months.

| Rental ID and offer | Native rent per cycle + setup | Effective R, S$/mo | Neither, months | Electricity only | Internet only | Both utilities |
|---|---|---:|---:|---:|---:|---:|
| 001 [UHost AX162-R, Helsinki][r1] | USD 220/mo + 120 | 283.73 | 30.34 / 29.80 | 42.18 / 41.42 | 36.84 / 36.17 | 55.86 / 54.86 |
| 002 [Lindau AX162-R, DE/FI][r2] | from USD 235.03/mo + N/Q · term N/Q | 303.11 | 28.40 / N/Q | 38.52 / N/Q | 34.01 / N/Q | 49.62 / N/Q |
| 004 [PlusClouds / Radius AX162-R, FI/DE][r4] | EUR 229/mo + 542 · term N/Q | 324.63 | 26.52 / 24.15 | 35.14 / 32.0022 | 31.35 / 28.55 | 44.15 / 40.21 |
| 007 [BizoSiz AX162-R, DE/FI][r7] | USD 279/mo + 111 | 359.82 | 23.93 / 23.53 | 30.73 / 30.21 | 27.79 / 27.33 | 37.40 / 36.78 |
| 013 [Provisov, Nuremberg][r13] | USD 304/mo + 109 · term N/Q | 392.06 | 21.96 / 21.60 | 27.55 / 27.11 | 25.17 / 24.76 | 32.80 / 32.27 |
| 015 [AMS SOFT AX162-R, Finland][r15] | BRL 1,989.90/mo + N/Q | 435.56 | 19.77 / N/Q | 24.19 / N/Q | 22.33 / N/Q | 28.14 / N/Q |
| 018 [Pro-m, Finland][r18] | USD 347/mo + 697 · 1-mo min | 447.51 | 19.24 / 17.23 | 23.40 / 20.96 | 21.66 / 19.40 | 27.08 / 24.25 |
| 019 [Servers99, Helsinki][r19] | USD 359/mo + 1,496.35 | 462.99 | 18.60 / 14.43 | 22.46 / 17.42 | 20.85 / 16.17 | 25.82 / 20.04 |
| 020 [BytesRack, Helsinki][r20] | USD 360/mo + 1,496.35 | 464.28 | 18.54 / 14.39 | 22.38 / 17.36 | 20.78 / 16.12 | 25.73 / 19.96 |
| 022 [LeoServers, Helsinki][r22] | USD 363/mo + 1,496.35 | 468.15 | 18.39 / 14.27 | 22.16 / 17.19 | 20.59 / 15.97 | 25.43 / 19.73 |
| 025 [KW Servers, Helsinki][r25] | USD 364/mo + 1,496.35 | 469.44 | 18.34 / 14.23 | 22.09 / 17.13 | 20.53 / 15.93 | 25.33 / 19.66 |
| 032 [GTZHost, Helsinki][r32] | USD 368/mo + 1,496.35 | 474.60 | 18.14 / 14.07 | 21.80 / 16.91 | 20.28 / 15.73 | 24.96 / 19.36 |
| 035 [Pro-m, Germany][r35] | USD 369/mo + 689 · 1-mo min | 475.89 | 18.09 / 16.22 | 21.73 / 19.48 | 20.22 / 18.13 | 24.86 / 22.30 |
| 039 [Servers99, Falkenstein][r39] | USD 373/mo + 1,496.35 | 481.05 | 17.90 / 13.89 | 21.45 / 16.64 | 19.97 / 15.50 | 24.50 / 19.01 |
| 040 [LeoServers, Falkenstein][r40] | USD 374/mo + 1,496.35 | 482.33 | 17.85 / 13.85 | 21.38 / 16.59 | 19.91 / 15.45 | 24.41 / 18.94 |
| 042 [CTCServers, Falkenstein][r42] | USD 377/mo + 1,496.35 | 486.20 | 17.71 / 13.74 | 21.17 / 16.43 | 19.74 / 15.31 | 24.14 / 18.73 |
| 043 [KW Servers, Falkenstein][r43] | USD 378/mo + 1,496.35 | 487.49 | 17.66 / 13.70 | 21.11 / 16.38 | 19.68 / 15.27 | 24.06 / 18.66 |
| 044 [GTZHost, Falkenstein][r44] | USD 379/mo + 1,496.35 | 488.78 | 17.61 / 13.67 | 21.04 / 16.32 | 19.62 / 15.22 | 23.97 / 18.60 |
| 045 [iDatam, Falkenstein][r45] | USD 382/mo + 1,496.35 | 492.65 | 17.48 / 13.56 | 20.84 / 16.17 | 19.45 / 15.09 | 23.71 / 18.40 |
| 046 [HostAddon HADE/HAFI, DE/FI][r46] | USD 4,806/12 mo + 999 | 516.51 | 16.67 / 14.17 | 19.71 / 16.76 | 18.45 / 15.69 | 22.25 / 18.92 |
| 049 [CTCServers, Falkenstein][r49] | USD 423/mo + N/Q | 545.53 | 15.78 / N/Q | 18.48 / N/Q | 17.37 / N/Q | 20.70 / N/Q |
| 051 [EPY Host, Falkenstein][r51] | USD 423/mo + N/Q | 545.53 | 15.78 / N/Q | 18.48 / N/Q | 17.37 / N/Q | 20.70 / N/Q |
| 055 [LeoServers, Falkenstein][r55] | USD 425/mo + N/Q | 548.11 | 15.71 / N/Q | 18.38 / N/Q | 17.28 / N/Q | 20.57 / N/Q |
| 060 [iDatam, Falkenstein][r60] | USD 429/mo + N/Q | 553.27 | 15.56 / N/Q | 18.18 / N/Q | 17.11 / N/Q | 20.32 / N/Q |
| 061 [GTZHost, Falkenstein][r61] | USD 431/mo + N/Q | 555.85 | 15.49 / N/Q | 18.08 / N/Q | 17.02 / N/Q | 20.20 / N/Q |
| 062 [Servers99, Falkenstein][r62] | USD 431/mo + N/Q | 555.85 | 15.49 / N/Q | 18.08 / N/Q | 17.02 / N/Q | 20.20 / N/Q |
| 063 [KW Servers, Nuremberg][r63] | USD 432/mo + N/Q | 557.14 | 15.45 / N/Q | 18.03 / N/Q | 16.98 / N/Q | 20.14 / N/Q |
| 065 [Servers99, Nuremberg][r65] | USD 432/mo + N/Q | 557.14 | 15.45 / N/Q | 18.03 / N/Q | 16.98 / N/Q | 20.14 / N/Q |
| 066 [KW Servers, Falkenstein][r66] | USD 433/mo + N/Q | 558.43 | 15.42 / N/Q | 17.98 / N/Q | 16.93 / N/Q | 20.08 / N/Q |
| 080 [HostAddon HADE/HAFI, DE/FI][r80] | USD 444.99/mo + 999 | 573.89 | 15.0019 / 12.76 | 17.42 / 14.81 | 16.43 / 13.97 | 19.38 / 16.48 |
| 085 [19CLOUDS DEDI-AX162, Falkenstein][r85] | EUR 418/mo + 55.57 | 592.56 | 14.53 / 14.40 | 16.78 / 16.63 | 15.87 / 15.72 | 18.60 / 18.43 |
| 101 [0DayHost, Amsterdam][r101] | USD 650/mo + N/Q · term N/Q | 838.28 | 10.27 / N/Q | 11.35 / N/Q | 10.92 / N/Q | 12.15 / N/Q |

## Offers that fit either profile

Each offer below is evaluated at both hardware prices. Lindau lists four 3.84 TB drives and leaves the array layout, actual price and setup unresolved. PowerDedi’s recorded cart is the European offer. Its legal operator and physical supply remain unresolved.

| Rental ID and offer | Native rent per cycle + setup | Effective R, S$/mo | Neither, months | Electricity only | Internet only | Both utilities |
|---|---|---:|---:|---:|---:|---:|
| 003 [Lindau AX162-S, DE/FI][r3] · A1 | from USD 236.41/mo + N/Q · term N/Q | 304.89 | 29.16 / N/Q | 39.47 / N/Q | 34.88 / N/Q | 50.73 / N/Q |
| 003 [Lindau AX162-S, DE/FI][r3] · A2 | from USD 236.41/mo + N/Q · term N/Q | 304.89 | 28.24 / N/Q | 38.22 / N/Q | 33.78 / N/Q | 49.12 / N/Q |
| 087 [PowerDedi, Amsterdam/Frankfurt][r87] · A1 | USD 489/mo + 0 | 630.65 | 14.10 / 14.10 | 16.14 / 16.14 | 15.31 / 15.31 | 17.75 / 17.75 |
| 087 [PowerDedi, Amsterdam/Frankfurt][r87] · A2 | USD 489/mo + 0 | 630.65 | 13.65 / 13.65 | 15.62 / 15.62 | 14.83 / 14.83 | 17.18 / 17.18 |

## Prepaid cash and contract commitments

For a rental actually paid in advance, compare cumulative cash at the end of integer service month `n ≥ 1` using `rent paid = F + ceil(n / p) × Q` and `owner paid = H + nO`. One complete invoice is due before service for each new term, including a term used only in part. Setup is charged once. The figures assume the same rates, charge timing and term on renewal, with no unused-term refund. A 24-month monthly-billed minimum still commits the buyer to 24 months but can have a different cash schedule.

Within a prepaid term, the rental payment stays fixed as owner operating costs accumulate. Buying can therefore be ahead after an invoice, fall behind before renewal, and pass the rental again on the next invoice. The table reports the **first completed service month from which owner cash remains no higher at every later month-end**, under unchanged renewals. When `Q > pO`, the end of each term is the least favorable point for owning within that term, and the term-end balance improves with every renewal. Compute `k = max(1, ceil((H − F) / (Q − pO)))`. The durable month is `1 + (k − 1) × p`. For these `H > F` quotes, `p = 1` reduces the result to the rounded-up monthly crossing. Month 1 means the initial term invoice already covers the purchase and the modeled operating costs through that term.

| Capacity-matched non-monthly row | Recorded billing | Neither utility | Electricity only | Internet only | Both utilities |
|---|---|---:|---:|---:|---:|
| 095 · IP-Projects A1 2 × 4 TB | EUR 11,780.29 prepaid for 24 months, zero setup | 1 | 1 | 1 | 1 |
| 098 · IP-Projects A1 2 × 4 TB | EUR 6,084.32 prepaid annually + EUR 342.85 setup | 1 | 13 | 13 | 13 |
| 046 · HostAddon A2 | USD 4,806 rent per 12-month cycle + USD 999 setup. Collection date unconfirmed. | N/Q | N/Q | N/Q | N/Q |

For row 098, the first rental invoice is **S$9,111.16**. On both utilities, buying costs S$9,020.61 through month 1 and S$9,150.23 through month 2. The initial cash advantage has reversed by the second month. After the second annual invoice, buying remains ahead from **month 13** under the modeled terms. Its setup-adjusted service-month equivalent is **14.27 months**. Row 095’s first invoice is S$16,699.74, enough to cover the S$8,891.00 parts price and all 24 months of the modeled utilities. [IP-Projects contract and invoice data](../2026-11-19-performance-pricing.md#additional-drive-choices)

For HostAddon row 046, annual collection in advance would produce a durable month of **13** in all four scenarios. If the annual contracted amount is instead paid in equal monthly installments, the four setup-adjusted completed months are **15, 17, 16 and 19**, respectively. A 12-month commitment applies in either case. The source establishes the cycle price but leaves the actual cash crossing conditional on collection terms. IP-Projects row 100 prices monthly billing on a 12-month minimum, with EUR 342.85 setup. A separate 24-month minimum billed monthly waives setup, and its contractual obligation and cash schedule should be evaluated using that specific offer. [HostAddon cycle evidence](../2026-11-19-global.md#additional-public-configurations-recovered-using-anonymous-sessions-19-november) · [IP-Projects billing versus contract length](../2026-11-19-performance-pricing.md#additional-drive-choices)

## Offers below both owned capacity profiles

All 38 rows below have 128 GB RAM. The column with the limiting specifications identifies the advertised configuration that blocks a direct payback comparison. Each horizon is **N/A** against A1 and A2. The recorded charges remain available for a workload with different RAM or disk needs. [Native 12-, 24- and 36-month costs](05-repository-rental-comparison.md#neither-a1-nor-a2)

| Rental ID and offer | CPU · RAM / NVMe drives (TB each) | Native rent per cycle + setup | Capacity limit |
|---|---|---|---|
| 009 [NineHost AX162-R, FRA selected][r9] | 9454P · 128 GB / 2×1.92 | USD 279.90/mo + N/Q | A1 needs larger drives. A2 needs 256 GB. |
| 010 [ENTRONYX TITAN-96, Helsinki][r10] | 9455 · 128 GB / 2×1.92 | EUR 6,226.32/24 mo + 0 | A1 needs larger drives. A2 needs 256 GB. |
| 011 [ENTRONYX TITAN-96, Helsinki][r11] | 9455 · 128 GB / 2×1.92 | EUR 3,214.68/12 mo + 0 | A1 needs larger drives. A2 needs 256 GB. |
| 012 [Nexia AX162-R, FRA selected][r12] | 9454P · 128 GB / 2×1.92 | USD 299.90/mo + N/Q | A1 needs larger drives. A2 needs 256 GB. |
| 014 [ENTRONYX TITAN-96, Helsinki][r14] | 9455 · 128 GB / 2×1.92 | EUR 281.99/mo + 299.99 | A1 needs larger drives. A2 needs 256 GB. |
| 021 [Introserv DC4RXL AE9455, FR/CA][r21] | 9455 · 128 GB / 2×1.92 | EUR 329.99/mo + 329.99 · 1-mo min | A1 needs larger drives. A2 needs 256 GB. |
| 041 [HSTQ, Paris][r41] | 9455 · 128 GB / 2×1.92 | USD 13,473/36 mo + 0 | A1 needs larger drives. A2 needs 256 GB. |
| 047 [NetVO, France][r47] | 9455 · 128 GB / 2×1.92 | USD 4,949.99/12 mo + N/Q | A1 needs larger drives. A2 needs 256 GB. |
| 053 [HSTQ, Paris][r53] | 9455 · 128 GB / 2×1.92 | USD 10,179.60/24 mo + 0 | A1 needs larger drives. A2 needs 256 GB. |
| 067 [CrockyHost Pro 10, Europe][r67] | 9455 · 128 GB / 2×1.9 | EUR 9,475/24 mo + 0 | Drive size misses both mirror floors. A2 also needs 256 GB. |
| 068 [NetVO, France][r68] | 9455 · 128 GB / 2×1.92 | USD 434.99/mo + 435 | A1 needs larger drives. A2 needs 256 GB. |
| 069 [Fit Servers, Gravelines][r69] | 9455 · 128 GB / 2×1.92 | USD 438/mo + 708 | A1 needs larger drives. A2 needs 256 GB. |
| 070 [KW Servers, Gravelines][r70] | 9455 · 128 GB / 2×1.92 | USD 438/mo + 708 | A1 needs larger drives. A2 needs 256 GB. |
| 071 [Servers99, Strasbourg][r71] | 9455P · 128 GB / 2×1.92 | USD 438/mo + 708 | A1 needs larger drives. A2 needs 256 GB. |
| 072 [KW Servers, Warsaw][r72] | 9455P · 128 GB / 2×1.92 | USD 439/mo + 708 | A1 needs larger drives. A2 needs 256 GB. |
| 073 [iRexta, Strasbourg][r73] | 9455P · 128 GB / 2×1.92 | USD 439/mo + 708 | A1 needs larger drives. A2 needs 256 GB. |
| 074 [inSave Compute 48, FR/CA/PL/DE][r74] | 9455 · 128 GB / 2×1.92 | USD 439/mo + 439 | A1 needs larger drives. A2 needs 256 GB. |
| 075 [Unihost OVE-X8, FR/PL/CA][r75] | 9455 · 128 GB / 2×1.92 | EUR 399.90/mo + 299.90 · term N/Q | A1 needs larger drives. A2 needs 256 GB. |
| 076 [Servers99, Gravelines][r76] | 9455 · 128 GB / 2×1.92 | USD 440/mo + 708 | A1 needs larger drives. A2 needs 256 GB. |
| 077 [Servers99, Roubaix][r77] | 9455 · 128 GB / 2×1.92 | USD 441/mo + 708 | A1 needs larger drives. A2 needs 256 GB. |
| 078 [KW Servers, Roubaix][r78] | 9455 · 128 GB / 2×1.92 | USD 442/mo + 708 | A1 needs larger drives. A2 needs 256 GB. |
| 079 [Servers99, Warsaw][r79] | 9455P · 128 GB / 2×1.92 | USD 444/mo + 708 | A1 needs larger drives. A2 needs 256 GB. |
| 081 [KW Servers, Strasbourg][r81] | 9455P · 128 GB / 2×1.92 | USD 448/mo + 708 | A1 needs larger drives. A2 needs 256 GB. |
| 082 [LeoServers, Gravelines][r82] | 9455 · 128 GB / 2×1.92 | USD 448/mo + 708 | A1 needs larger drives. A2 needs 256 GB. |
| 083 [HSTQ, Paris][r83] | 9455 · 128 GB / 2×1.92 | USD 5,389.20/12 mo + 0 | A1 needs larger drives. A2 needs 256 GB. |
| 084 [CrockyHost Pro 10, Europe][r84] | 9455 · 128 GB / 2×1.9 | EUR 4,990/12 mo + 0 | Drive size misses both mirror floors. A2 also needs 256 GB. |
| 086 [Gokiebox DEDICADO XL, CA/FR][r86] | 9455 · 128 GB / 2×1.92 | USD 484/mo + 357 | A1 needs larger drives. A2 needs 256 GB. |
| 088 [HSTQ, Paris][r88] | 9455 · 128 GB / 2×1.92 | USD 499/mo + 0 | A1 needs larger drives. A2 needs 256 GB. |
| 089 [IP-Projects, Frankfurt][r89] | 9980X · 128 GB / 1×2 | EUR 11,109.13/24 mo + 0 | Single drive. Both profiles require a mirror. A2 also needs 256 GB. |
| 090 [CrockyHost Pro 10, Europe][r90] | 9455 · 128 GB / 2×1.9 | EUR 468/mo + 300 | Drive size misses both mirror floors. A2 also needs 256 GB. |
| 091 [Evolushost, Vienna][r91] | 9454P · 128 GB / 2×1 | EUR 5,640/12 mo + N/Q | Drive size misses both mirror floors. A2 also needs 256 GB. |
| 092 [IP-Projects, Frankfurt][r92] | 9980X · 128 GB / 2×2 | EUR 11,305.51/24 mo + 0 | A1 needs larger drives. A2 needs 256 GB. |
| 093 [Evolushost, Vienna][r93] | 9454P · 128 GB / 2×1 | EUR 480/mo + 99.99 | Drive size misses both mirror floors. A2 also needs 256 GB. |
| 094 [IP-Projects, Frankfurt][r94] | 9980X · 128 GB / 2×2 | EUR 5,839.12/12 mo + 342.85 | A1 needs larger drives. A2 needs 256 GB. |
| 096 [HostX DS-3, Germany][r96] | 9454P · 128 GB / 2×1.9 | EUR 499/mo + 1,999 · 12-mo min | Drive size misses both mirror floors. A2 also needs 256 GB. |
| 097 [TLFHost Enterprise 128GB, FR/DE][r97] | 9455 · 128 GB / 2×1.92 | USD 549/mo + 540 | A1 needs larger drives. A2 needs 256 GB. |
| 099 [IP-Projects, Frankfurt][r99] | 9980X · 128 GB / 2×2 | EUR 517.65/mo + 342.85 · 12-mo min | A1 needs larger drives. A2 needs 256 GB. |
| 102 [IP-Projects, Frankfurt][r102] | 9985WX · 128 GB / 2×2 | EUR 14,263.82/24 mo + 0 | A1 needs larger drives. A2 needs 256 GB. |

The historical Hetzner AX162-1 LTD was absent from the recorded public availability feeds. A customer still paying a legacy invoice can apply the formulas to its actual future charges. [Inventory check and reference tariffs](../2026-11-19.md#hetzner-reference-and-limited-stock-variants)

[snapshot]: https://github.com/tailrocks/dedicated-servers-providers/blob/07180f43068a8de01ae30c41a265ec16ef1f138b/README.md?plain=1#L23-L142
[r1]: https://uhost.online/en/dedicated/19
[r2]: https://www.lindau.cloud/en/products/31
[r3]: https://www.lindau.cloud/en/products/32
[r4]: https://plusclouds.com/servers
[r5]: https://plusclouds.com/servers
[r6]: https://hummingtribe.com/dedicated
[r7]: https://my.bizosiz.com/cart.php?a=add&pid=30&currency=1
[r8]: https://my.bizosiz.com/cart.php?a=add&pid=31&currency=1
[r9]: https://ninehost.net/cart?plan=AX162-R
[r10]: https://entronyx.cloud/en/bare-metal/titan
[r11]: https://entronyx.cloud/en/bare-metal/titan
[r12]: https://nexia.host/cart?plan=AX162-R
[r13]: https://www.provisov.net/services/arenda-serverov/
[r14]: https://entronyx.cloud/en/bare-metal/titan
[r15]: https://loja.amssoft.com.br/cart.php?a=add&pid=10102&billingcycle=monthly
[r16]: https://loja.amssoft.com.br/cart.php?a=add&pid=10099&billingcycle=monthly
[r17]: https://my.pro-m.org/products/dedicated/ded-fi-030/checkout?plan=95&options%5B1%5D=2
[r18]: https://my.pro-m.org/products/dedicated/ded-fi-028/checkout?plan=83&options%5B1%5D=2
[r19]: https://www.servers99.com/billing/cart.php?a=add&pid=30134&carttpl=new-theme-cart
[r20]: https://www.bytesrack.com/billing/cart.php?a=add&carttpl=bytesrack_cart&pid=26509
[r21]: https://introserv.com/order/dc4rxl-ae9455/
[r22]: https://www.leoservers.com/billing/cart.php?a=add&pid=49693&carttpl=newleocart
[r23]: https://uhost.online/en/dedicated/20
[r24]: https://www.ctcservers.com/billing/cart.php?a=add&pid=50636
[r25]: https://www.kwservers.com/billing/cart.php?a=add&pid=29123&carttpl=kw_cart
[r26]: https://billing.idatam.com/cart.php?a=add&pid=35662
[r27]: https://www.gtzhost.com/billing/cart.php?a=add&pid=62898&carttpl=gtz-new-cart
[r28]: https://www.servers99.com/billing/cart.php?a=add&pid=30133&carttpl=new-theme-cart
[r29]: https://www.bytesrack.com/billing/cart.php?a=add&carttpl=bytesrack_cart&pid=26508
[r30]: https://www.gtzhost.com/billing/cart.php?a=add&pid=62907&carttpl=gtz-new-cart
[r31]: https://www.kwservers.com/billing/cart.php?a=add&pid=29131&carttpl=kw_cart
[r32]: https://www.gtzhost.com/billing/cart.php?a=add&pid=62899&carttpl=gtz-new-cart
[r33]: https://www.kwservers.com/billing/cart.php?a=add&pid=29122&carttpl=kw_cart
[r34]: https://my.pro-m.org/products/dedicated/ded-de-029/checkout?plan=91&options%5B1%5D=3
[r35]: https://my.pro-m.org/products/dedicated/ded-de-027/checkout?plan=75&options%5B1%5D=3
[r36]: https://www.servers99.com/billing/cart.php?a=add&pid=30142&carttpl=new-theme-cart
[r37]: https://www.leoservers.com/billing/cart.php?a=add&pid=49701&carttpl=newleocart
[r38]: https://www.leoservers.com/billing/cart.php?a=add&pid=49692&carttpl=newleocart
[r39]: https://www.servers99.com/billing/cart.php?a=add&pid=30143&carttpl=new-theme-cart
[r40]: https://www.leoservers.com/billing/cart.php?a=add&pid=49702&carttpl=newleocart
[r41]: https://cp.hstq.net/cart.php?a=add&language=english&pid=94
[r42]: https://www.ctcservers.com/billing/cart.php?a=add&pid=50637
[r43]: https://www.kwservers.com/billing/cart.php?a=add&pid=29132&carttpl=kw_cart
[r44]: https://www.gtzhost.com/billing/cart.php?a=add&pid=62908&carttpl=gtz-new-cart
[r45]: https://billing.idatam.com/cart.php?a=add&pid=35663
[r46]: https://www.hostaddon.com/clients/cart.php?a=add&pid=1519
[r47]: https://netvo.io/cart.php?a=add&pid=66
[r48]: https://www.xhn.es/clientes/cart.php?a=add&pid=85
[r49]: https://www.ctcservers.com/billing/cart.php?a=add&pid=60206
[r50]: https://billing.epyhost.com/cart.php?a=add&pid=46715
[r51]: https://billing.epyhost.com/cart.php?a=add&pid=46716
[r52]: https://www.servers99.com/billing/cart.php?a=add&pid=39713&carttpl=new-theme-cart
[r53]: https://cp.hstq.net/cart.php?a=add&language=english&pid=94
[r54]: https://www.leoservers.com/billing/cart.php?a=add&pid=59272&carttpl=newleocart
[r55]: https://www.leoservers.com/billing/cart.php?a=add&pid=59273&carttpl=newleocart
[r56]: https://www.gtzhost.com/billing/cart.php?a=add&pid=72477&carttpl=gtz-new-cart
[r57]: https://billing.idatam.com/cart.php?a=add&pid=45243
[r58]: https://www.ctcservers.com/billing/cart.php?a=add&pid=60205
[r59]: https://www.kwservers.com/billing/cart.php?a=add&pid=38700&carttpl=kw_cart
[r60]: https://billing.idatam.com/cart.php?a=add&pid=45244
[r61]: https://www.gtzhost.com/billing/cart.php?a=add&pid=72478&carttpl=gtz-new-cart
[r62]: https://www.servers99.com/billing/cart.php?a=add&pid=39714&carttpl=new-theme-cart
[r63]: https://www.kwservers.com/billing/cart.php?a=add&pid=38693&carttpl=kw_cart
[r64]: https://www.servers99.com/billing/cart.php?a=add&pid=39705&carttpl=new-theme-cart
[r65]: https://www.servers99.com/billing/cart.php?a=add&pid=39706&carttpl=new-theme-cart
[r66]: https://www.kwservers.com/billing/cart.php?a=add&pid=38701&carttpl=kw_cart
[r67]: https://crocky.host/cart.php?a=add&pid=112&billingcycle=biennially
[r68]: https://netvo.io/cart.php?a=add&pid=66
[r69]: https://www.fitservers.com/billing/cart.php?a=add&pid=52359
[r70]: https://www.kwservers.com/billing/cart.php?a=add&pid=30165&carttpl=kw_cart
[r71]: https://www.servers99.com/billing/cart.php?a=add&pid=31178&carttpl=new-theme-cart
[r72]: https://www.kwservers.com/billing/cart.php?a=add&pid=30168&carttpl=kw_cart
[r73]: https://my.irexta.com/cart.php?a=add&pid=33570
[r74]: https://my.insave.hosting/cart.php?a=add&pid=321&billingcycle=monthly&currency=1&language=english
[r75]: https://unihost.com/dedicated/epyc/
[r76]: https://www.servers99.com/billing/cart.php?a=add&pid=31176&carttpl=new-theme-cart
[r77]: https://www.servers99.com/billing/cart.php?a=add&pid=45070&carttpl=new-theme-cart
[r78]: https://www.kwservers.com/billing/cart.php?a=add&pid=44060&carttpl=kw_cart
[r79]: https://www.servers99.com/billing/cart.php?a=add&pid=31179&carttpl=new-theme-cart
[r80]: https://www.hostaddon.com/clients/cart.php?a=add&pid=1519
[r81]: https://www.kwservers.com/billing/cart.php?a=add&pid=30167&carttpl=kw_cart
[r82]: https://www.leoservers.com/billing/cart.php?a=add&pid=50735&carttpl=newleocart
[r83]: https://cp.hstq.net/cart.php?a=add&language=english&pid=94
[r84]: https://crocky.host/cart.php?a=add&pid=112&billingcycle=annually
[r85]: https://clients.19clouds.com/cart.php?a=add&pid=134
[r86]: https://app.gokiebox.com/carrito/agregar/237?moneda=USD
[r87]: https://powerdedi.com/order?plan=e-9454p
[r88]: https://cp.hstq.net/cart.php?a=add&language=english&pid=94
[r89]: https://www.ip-projects.de/en/order/dedicated-server/amd-str5-l-g1
[r90]: https://crocky.host/cart.php?a=add&pid=112&billingcycle=monthly
[r91]: https://dash.evolushost.com/cart.php?a=add&pid=3895
[r92]: https://www.ip-projects.de/en/order/dedicated-server/amd-str5-l-g1
[r93]: https://dash.evolushost.com/cart.php?a=add&pid=3895
[r94]: https://www.ip-projects.de/en/order/dedicated-server/amd-str5-l-g1
[r95]: https://www.ip-projects.de/en/order/dedicated-server/amd-str5-l-g1
[r96]: https://www.hostx.eu/dedicated-servers/
[r97]: https://my.tlfhost.com/store/france-dedicated-servers/enterprise-dedicated-128gb
[r98]: https://www.ip-projects.de/en/order/dedicated-server/amd-str5-l-g1
[r99]: https://www.ip-projects.de/en/order/dedicated-server/amd-str5-l-g1
[r100]: https://www.ip-projects.de/en/order/dedicated-server/amd-str5-l-g1
[r101]: https://0dayhost.com/amsterdam-dedicated-servers.php
[r102]: https://www.ip-projects.de/en/order/dedicated-server/amd-str5-xl-g1
[r103]: https://client.ithoster.com/store/dedicated-server/ax162-s
[r104]: https://www.hetzner.com/dedicated-rootserver/ax162/configurator/
