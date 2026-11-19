#!/usr/bin/env python3
"""Check repository documentation links and the ordered rental catalog."""

import argparse
from collections import Counter
from datetime import date
from decimal import Decimal
from itertools import groupby
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parent.parent
CATALOG = Path("rentals/README.md")
OFFER_HEADER = (
    "Provider", "Location", "Specs", "Price (USD/mo)", "URL", "Last checked", "Notes"
)
HEADING = re.compile(r"^ {0,3}(#{1,6})\s+(.+?)(?:\s+#+)?\s*$")
NAMED_ANCHOR = re.compile(r'<(?:a|span)\b[^>]*\b(?:name|id)=["\']([^"\']+)["\']')
LINK = re.compile(r"""\]\((<[^>]+>|(?:[^()\s]|\([^()\s]*\))+)(?:\s+["'][^)]*)?\)""")
REFERENCE = re.compile(r"^ {0,3}\[[^]]+\]:\s*(<[^>]+>|\S+)")
INLINE_CODE = re.compile(r"(\x60+)[^\x60]+\1")
HTTP_URL = re.compile(r"https?://(?:[^\s<>()\x5b\x5d\x60]|\([^()\s]*\))+")
FENCE = re.compile(r"^ {0,3}(\x60{3,}|~{3,})")
DIVIDER = re.compile(r"^:?-{2,}:?$")
AMOUNT = r"[0-9]+(?:,[0-9]{3})*(?:\.[0-9]{1,2})?"
PRICE = re.compile(rf"~?({AMOUNT})\s*†?")
BAND = re.compile(rf"(?:(?:\$(?P<lower>{AMOUNT}) to )?under \$(?P<upper>{AMOUNT})|\$(?P<tail>{AMOUNT}) and up)", re.IGNORECASE)
DATED_REPORT = re.compile(r"research/(?:\d{4}-\d{2}-\d{2}|buy-vs-rent/\d{2}-)")


def git(*args):
    return subprocess.check_output(["git", "-C", ROOT, *args], text=True)


def markdown_lines(document):
    """Yield numbered Markdown lines outside fenced code examples."""
    fence = None
    for number, line in enumerate(document.splitlines(), 1):
        marker = FENCE.match(line)
        if marker and fence is None:
            fence = marker[1]
        elif fence and line.strip() and set(line.strip()) == {fence[0]} and len(line.strip()) >= len(fence):
            fence = None
        elif fence is None:
            yield number, line


def anchors(document):
    found = set()
    headings = set()
    for _, line in markdown_lines(document):
        found.update(NAMED_ANCHOR.findall(line))
        heading = HEADING.match(line)
        if heading:
            title = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", heading[2])
            slug = re.sub(r"[^\w\s-]", "", title.lower()).strip().replace(" ", "-")
            anchor = slug
            suffix = 0
            while anchor in headings:
                suffix += 1
                anchor = f"{slug}-{suffix}"
            headings.add(anchor)
    return found | headings


def local_link_errors(documents, files):
    indexed = {name: anchors(document) for name, document in documents.items()}
    for source, document in documents.items():
        for number, line in markdown_lines(document):
            line = INLINE_CODE.sub("", line)
            destinations = [match[1] for match in LINK.finditer(line)]
            definition = REFERENCE.match(line)
            if definition:
                destinations.append(definition[1])
            for destination in destinations:
                parsed = urlsplit(destination.strip("<>"))
                if parsed.scheme or parsed.netloc:
                    continue
                if not parsed.path:
                    target = source
                else:
                    link_path = unquote(parsed.path)
                    base = ROOT if link_path.startswith("/") else ROOT / source.parent
                    absolute = (base / link_path.lstrip("/")).resolve()
                    if not absolute.is_relative_to(ROOT):
                        yield f"{source}:{number}: {destination} points outside the repository"
                        continue
                    target = absolute.relative_to(ROOT)
                    if target not in files and target / "README.md" in files:
                        target /= "README.md"
                if target not in files:
                    yield f"{source}:{number}: missing link destination {destination}"
                elif parsed.fragment and target in indexed:
                    fragment = unquote(parsed.fragment)
                    if fragment not in indexed[target]:
                        yield f"{source}:{number}: missing anchor in {destination}"


def table_cells(line):
    stripped = line.strip()
    if not (stripped.startswith("|") and stripped.endswith("|")):
        return ()
    return tuple(cell.strip() for cell in re.split(r"(?<!\\)\|", stripped[1:-1]))


def table_rows(document):
    for line_number, line in markdown_lines(document):
        cells = table_cells(line)
        if cells and not all(DIVIDER.fullmatch(cell) for cell in cells):
            yield line_number, line, cells


def catalog_sections(document):
    """Yield the Servers section and its price-band subsections."""
    section = None
    for number, line in markdown_lines(document):
        heading = HEADING.match(line)
        level = len(heading[1]) if heading else 0
        if section is None:
            if level == 2 and heading[2] == "Servers":
                section = (number, None, [])
            continue
        if level in (1, 2, 3):
            yield section
            if level < 3:
                return
            section = (number, heading[2], [])
        else:
            section[2].append((number, line))
    if section is not None:
        yield section


def offer_table_line(row):
    stripped = row[1].strip()
    return stripped.startswith("|") or stripped.endswith("|") or stripped.count("|") >= len(OFFER_HEADER) - 1


def monthly_price(cell):
    quote = PRICE.fullmatch(cell)
    return Decimal(quote[1].replace(",", "")) if quote else None


def catalog_tables(document, catalog_path=CATALOG):
    """Read every table block and report malformed or orphaned rows."""
    offers = []
    errors = []
    bands = []
    for section_line, title, lines in catalog_sections(document):
        blocks = [list(rows) for is_table, rows in groupby(lines, offer_table_line) if is_table]
        bounds = None
        if title:
            band = BAND.fullmatch(title)
            if not band:
                errors.append(f"{catalog_path}:{section_line}: invalid price band {title!r}")
            else:
                lower = monthly_price(band['lower'] or band['tail'] or '0')
                upper = monthly_price(band['upper']) if band['upper'] else None
                bounds = (lower, upper)
                bands.append((section_line, lower, upper))
            if not blocks:
                errors.append(f"{catalog_path}:{section_line}: price band has no offer table")
        elif blocks and catalog_path == CATALOG:
            errors.append(f"{catalog_path}:{section_line}: offer table must be in a price band")
        for block in blocks:
            header_line, header = block[0]
            if table_cells(header) != OFFER_HEADER:
                errors.append(f"{catalog_path}:{header_line}: expected the seven-column offer header")
                continue
            divider = table_cells(block[1][1]) if len(block) >= 2 else ()
            if len(divider) != len(OFFER_HEADER) or not all(DIVIDER.fullmatch(cell) for cell in divider):
                errors.append(f"{catalog_path}:{header_line + 1}: expected the offer table divider")
                continue
            for number, line in block[2:]:
                cells = table_cells(line)
                offers.append((number, line, cells))
                if bounds and len(cells) == len(OFFER_HEADER):
                    price = monthly_price(cells[3])
                    lower, upper = bounds
                    if price is not None and (price < lower or (upper is not None and price >= upper)):
                        errors.append(f"{catalog_path}:{number}: price {price} is outside {title!r}")
    if bands:
        expected_lower = Decimal('0')
        for number, lower, upper in bands:
            if lower != expected_lower or (upper is not None and upper <= lower):
                errors.append(f"{catalog_path}:{number}: price bands must be contiguous and ascending")
            expected_lower = upper
        if expected_lower is not None:
            errors.append(f"{catalog_path}: final price band must have no upper limit")
    elif catalog_path == CATALOG:
        errors.append(f"{catalog_path}: no price bands found")
    return offers, errors


def catalog_errors(offers):
    if not offers:
        yield f"{CATALOG}: no offers found"
    previous_price = Decimal("0")
    for number, _, cells in offers:
        if len(cells) != len(OFFER_HEADER):
            yield f"{CATALOG}:{number}: expected {len(OFFER_HEADER)} cells, found {len(cells)}"
            continue
        price = monthly_price(cells[3])
        if price is None:
            yield f"{CATALOG}:{number}: invalid monthly price {cells[3]!r}"
        else:
            if price < previous_price:
                yield f"{CATALOG}:{number}: price {price} follows {previous_price}"
            previous_price = price
        try:
            if date.fromisoformat(cells[5]).isoformat() != cells[5]:
                raise ValueError
        except ValueError:
            yield f"{CATALOG}:{number}: invalid last-checked date {cells[5]!r}"


def external_sources(document):
    return Counter(url.rstrip(".,;:") for url in HTTP_URL.findall(document))


def row_evidence(document):
    return Counter(
        LINK.sub(lambda match: match[0] if urlsplit(match[1].strip("<>")).scheme else "](LOCAL)", line)
        for _, line, _ in table_rows(document)
    )


def baseline_errors(revision, documents, offers):
    baseline = {
        Path(name): git("show", f"{revision}:{name}")
        for name in git("ls-tree", "-r", "--name-only", "-z", revision).split("\0")
        if name.endswith(".md")
    }
    original_path = CATALOG if CATALOG in baseline else Path("README.md")
    original_rows, original_errors = catalog_tables(baseline[original_path], original_path)
    if original_errors:
        yield f"Could not read the rental catalog at {revision}"
    original_offers = [line for _, line, _ in original_rows]
    if [line for _, line, _ in offers] != original_offers:
        yield f"{CATALOG}: offer rows or order differ from {revision}"
    current_sources = set().union(*(external_sources(document) for document in documents.values()))
    previous_sources = set().union(*(external_sources(document) for document in baseline.values()))
    for source in sorted(previous_sources - current_sources):
        yield f"Missing external source from {revision}: {source}"
    for name, original in baseline.items():
        if name not in documents:
            yield f"Missing original documentation path: {name}"
            continue
        current = documents[name]
        for anchor in sorted(anchors(original) - anchors(current)):
            yield f"{name}: missing original anchor #{anchor}"
        if DATED_REPORT.match(name.as_posix()):
            if row_evidence(original) - row_evidence(current):
                yield f"{name}: missing dated table rows from {revision}"
            if external_sources(original) - external_sources(current):
                yield f"{name}: missing dated source occurrences from {revision}"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", metavar="GIT_REV", help="Verify preservation from a prior revision")
    args = parser.parse_args()
    files = {
        Path(name) for name in git("ls-files", "--cached", "--others", "--exclude-standard", "-z").split("\0")
        if name and (ROOT / name).is_file()
    }
    documents = {
        name: (ROOT / name).read_text(encoding="utf-8")
        for name in sorted(files)
        if name.suffix == ".md"
    }
    offers, errors = catalog_tables(documents.get(CATALOG, ""))
    errors.extend(local_link_errors(documents, files))
    errors.extend(catalog_errors(offers))
    if args.baseline:
        errors.extend(baseline_errors(args.baseline, documents, offers))
    if errors:
        print("\n".join(errors))
        return 1
    print(f"Checked local links in {len(documents)} Markdown files and {len(offers)} ordered rental offers.")
    if args.baseline:
        print(f"Preserved offers, original paths and anchors, dated tables, and external sources from {args.baseline}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
