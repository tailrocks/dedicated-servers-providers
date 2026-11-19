# Contribute rental research

[Home](README.md) / [Rental offers](rentals/README.md)

## How to add or update an offer

1. Read the [methodology](METHODOLOGY.md), [rental catalog](rentals/README.md) and latest [dated research log](research/README.md). Verify the whole physical server, exact CPU, installed RAM and SSD capacity from primary sources.
2. Add one row per materially different server or promotion. Keep the original seven columns. Place each offer in the matching price band and sort `Price (USD/mo)` numerically ascending across the catalog. Do not inflate coverage with identical location copies.
3. Use `CPU / RAM / Storage / Bandwidth` in `Specs`. Give a direct server, configurator or promotion URL; if only a named entry on a range page exists, identify it explicitly.
4. Record native currency, tax basis, setup, contract length, prepayment, stock evidence and performance limitations in `Notes`. Show a lower monthly rate even when useful, but state if first-year total is higher.
5. Update `Last checked` only when that offer is rechecked. Record failed checks and corrections in a dated log, preserving earlier evidence rather than silently deleting it.
6. Keep below-floor CPUs, incomplete disk upgrades, sold-out deals and unresolved demonstrations in the [watchlist](rentals/watchlist.md) or [dated log](research/README.md), not among established strict matches. Do not contact sellers, reserve hardware or place orders as part of research.
7. Follow [AGENTS.md](AGENTS.md): sign off every commit, publish completed research and merge every PR created or touched once required checks permit. Respect protections and report any actual blocker.

## Row template

| Provider | Location | Specs | Price (USD/mo) | URL | Last checked | Notes |
|----------|----------|-------|----------------|-----|--------------|-------|

## Columns

- **Provider:** company / trading name and distinguishable server or contract variant.
- **Location:** advertised datacenter city and country; unknown or selector-only locations are labelled.
- **Specs:** exact CPU / installed RAM / raw drive layout / network port and allowance.
- **Price (USD/mo):** recurring or explicitly labelled prepaid monthly equivalent; currency conversions marked `~`, retained gross quotes marked `†`. Setup is separate. Unknown taxes are not silently assumed to be zero.
- **URL:** direct offer or configuration, with cookies sometimes needed for public shopping carts.
- **Last checked:** ISO date of the cited price/configuration check.
- **Notes:** evidence level, native quote, tax, setup, term, stock, mirrored capacity and material qualification concerns.

## Check your changes

Run `python3 scripts/check_docs.py` to check local links, anchors and catalog order. For a documentation move that should preserve the existing offer rows, run `python3 scripts/check_docs.py --baseline <git-revision>` against the revision before the move.
