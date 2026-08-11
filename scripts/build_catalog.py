#!/usr/bin/env python3
"""Build the thin template catalog from an Octoparse structured-data snapshot.

The snapshot (one JSON per template, ~8KB each) is the upstream source of truth.
It is NOT committed to this repository: the Octoparse service will serve the same
structured data, and a committed copy would become a stale mirror.

What IS committed is `data/catalog.json` -- a thin projection carrying only the
fields needed to *route* a request to a template. Schemas, field definitions and
`sourceTree` stay upstream and are fetched at run time via `search_templates`.

Curation files reference templates by `template_id`. `validate` re-checks those
references against a fresh catalog so that an upstream removal fails loudly
instead of silently producing a recommendation for a template that is gone.

Usage:
    python3 scripts/build_catalog.py build    --snapshot <dir> [--out data/catalog.json]
    python3 scripts/build_catalog.py validate [--catalog data/catalog.json]
    python3 scripts/build_catalog.py candidates --need lead-generation [--all-languages]
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
from typing import Any, Iterable

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
DEFAULT_CATALOG = REPO_ROOT / "data" / "catalog.json"
CURATION_DIR = REPO_ROOT / "skills" / "octoparse-ultimate-scraper" / "references" / "workflows"

# Output-field name fragments that signal a template yields contact data.
# Matched case-insensitively against outputSchema property names.
CONTACT_MARKERS = {
    "email": ("email", "e-mail", "mail_"),
    "phone": ("phone", "tel", "mobile", "contact_number"),
    "website": ("website", "web_site", "homepage", "site_url"),
}

# Workflow guides are shaped by what a user is trying to accomplish, not by the
# upstream category tags. The tags describe where data comes from -- `Directories`,
# `Maps` and `Search Engine` are source types that nobody asks for by name, and 60 of
# the 103 `Directories` templates are also tagged `Lead Generation`. Conversely a
# single need is scattered across tags: templates that collect review or comment pages
# sit under Reviews, E-Commerce, Travel, Maps and Directories at once.
#
# Each need selects candidates by any combination of category tags, source page types,
# and name keywords, minus an explicit exclusion list for tag noise.
# `match` controls how the criteria combine: "any" unions them, "all" intersects the
# criteria that are present. Default is "all".
NEEDS: dict[str, dict[str, Any]] = {
    "lead-generation": {
        "match": "any",
        "categories": {"Lead Generation", "Directories", "Maps"},
        "name_any": ("email finder", "lead", "contact"),
        "exclude_ids": {1763, 876, 824, 833, 1647, 1659, 1661, 1658, 1660, 1104},
    },
    # The e-commerce split is a page-type split, and it maps to two genuinely
    # different jobs: watching the price of products you already track (detail pages)
    # versus finding out what is selling in a category (listing / search pages).
    "competitor-price-monitoring": {
        "categories": {"E-Commerce"},
        "page_types": {"DETAIL"},
    },
    "product-market-research": {
        "categories": {"E-Commerce"},
        "page_types": {"SEARCH_RESULTS", "LISTING"},
    },
    "review-reputation-analysis": {
        # The scattered need: select on page type, not on the Reviews tag, which
        # only covers 20 of the 44 templates that actually collect review text.
        "match": "any",
        "page_types": {"REVIEWS", "COMMENTS"},
        "name_any": ("review", "comment", "avis", "bewertung", "reseña", "recensioni", "口コミ"),
    },
    "company-supplier-research": {
        "match": "any",
        "categories": {"Directories"},
        "name_any": (
            "kompass", "clutch", "goodfirms", "north data", "societe", "pappers",
            "einforma", "ipros", "wlw", "europages", "b2bmap", "verif", "company",
        ),
        # Consumer-facing directories belong to lead generation, not B2B research.
        "exclude_ids": {876, 824, 833, 1129, 1324, 1366, 560, 249},
    },
    "talent-recruitment": {"categories": {"Jobs"}},
    "property-travel-market": {"categories": {"Real Estate", "Travel"}},
    "social-listening": {"categories": {"Social Media", "News Media"}},
    # Kept apart from social listening: monitoring where you rank on a search engine
    # and monitoring what people say about you are different jobs done by different
    # people. Note this need covers SERP capture only -- the library has no backlink,
    # domain-authority, keyword-volume or traffic templates at all.
    "serp-visibility": {"categories": {"Search Engine"}},
}


def _info(template: dict[str, Any]) -> dict[str, Any]:
    return template["templateInfo"]


def _output_properties(template: dict[str, Any]) -> dict[str, Any]:
    return (template.get("outputSchema") or {}).get("properties") or {}


def _input_properties(template: dict[str, Any]) -> dict[str, Any]:
    return (template.get("inputSchema") or {}).get("properties") or {}


def _contact_flags(template: dict[str, Any], builtin_detail_stage: bool) -> dict[str, bool | None]:
    """Which contact fields the template yields.

    `None` means "not knowable from the snapshot". Templates with an internal
    listing -> detail stage publish only the stage-1 handoff slot in their
    outputSchema -- template 1576 exposes exactly one property, `FollowField`,
    while its description promises emails, phones and websites. Those fields live
    in the unpublished follow template and are absent here.

    Reporting `False` for those would let a caller rule out a template that does
    in fact return the field, so they are marked unknown and must be confirmed
    against the live schema from `search_templates(id=...)`.
    """
    names = [name.lower() for name in _output_properties(template)]
    flags: dict[str, bool | None] = {}
    for kind, markers in CONTACT_MARKERS.items():
        found = any(marker in name for name in names for marker in markers)
        flags[kind] = True if found else (None if builtin_detail_stage else False)
    return flags


def project(template: dict[str, Any]) -> dict[str, Any]:
    """Reduce a full snapshot record to the routing-relevant projection."""
    info = _info(template)
    follow_id = (info.get("followTemplate") or {}).get("id")
    return {
        # `template_id` is the join key for every curation file. Never use `slug`:
        # 13 templates carry placeholder slugs ("aaaaaaaaa", "1737") that are not
        # resolvable via search_templates(slug=...). See references/gotchas.md.
        "template_id": info["id"],
        "name": info["title"],
        "slug": info["slug"],
        "categories": info.get("categories") or [],
        "language": info.get("language"),
        "run_on": info.get("run_on") or info.get("runOn"),
        "status": info.get("status"),
        "min_account_level": (info.get("access") or {}).get("minAccountLevel"),
        "price": (info.get("pricing") or {}).get("displayPrice"),
        "source_page_types": info.get("sourcePageTypes") or [],
        "input_field_count": len(_input_properties(template)),
        # Understated for builtin-detail-stage templates: the snapshot only carries
        # the stage-1 schema. Treat it as a floor, not a count.
        "output_field_count": len(_output_properties(template)),
        "yields": _contact_flags(template, follow_id is not None),
        # A non-null follow_template_id means the template already performs a
        # listing -> detail pass internally against a template that is not
        # published in the library. Chaining a detail template after one of these
        # re-collects the same rows and bills twice.
        "has_builtin_detail_stage": follow_id is not None,
        "url": info.get("url"),
    }


def load_snapshot(snapshot_dir: pathlib.Path) -> list[dict[str, Any]]:
    templates_dir = snapshot_dir / "templates"
    if not templates_dir.is_dir():
        raise SystemExit(f"no templates/ directory under {snapshot_dir}")
    records = []
    for path in sorted(templates_dir.glob("*.json")):
        with path.open() as handle:
            records.append(json.load(handle))
    if not records:
        raise SystemExit(f"no template JSON files found in {templates_dir}")
    return records


def read_manifest(snapshot_dir: pathlib.Path) -> dict[str, Any]:
    manifest_path = snapshot_dir / "manifest.json"
    if not manifest_path.is_file():
        return {}
    with manifest_path.open() as handle:
        manifest = json.load(handle)
    return {
        "generated_at": manifest.get("generatedAt"),
        "template_count": manifest.get("templateCount"),
    }


def build(snapshot_dir: pathlib.Path, out_path: pathlib.Path) -> None:
    templates = load_snapshot(snapshot_dir)
    entries = sorted((project(t) for t in templates), key=lambda e: e["template_id"])

    catalog = {
        "source": {
            "snapshot": snapshot_dir.name,
            **read_manifest(snapshot_dir),
        },
        "note": (
            "Routing projection only. Input/output schemas and sourceTree are served "
            "by the Octoparse MCP service; fetch them with search_templates(id=...)."
        ),
        "templates": entries,
    }

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w") as handle:
        json.dump(catalog, handle, ensure_ascii=False, indent=2)
        handle.write("\n")

    runnable = sum(1 for e in entries if e["run_on"] != "LOCAL" and e["status"] == "PUBLISHED")
    print(f"wrote {out_path.relative_to(REPO_ROOT)}")
    print(f"  templates          {len(entries)}")
    print(f"  cloud + published  {runnable}")
    print(f"  builtin 2-stage    {sum(1 for e in entries if e['has_builtin_detail_stage'])}")


def load_catalog(catalog_path: pathlib.Path) -> dict[str, Any]:
    if not catalog_path.is_file():
        raise SystemExit(f"catalog not found: {catalog_path}\nRun `build` first.")
    with catalog_path.open() as handle:
        return json.load(handle)


MARKER_RE = re.compile(r"<!--\s*id:(\d+)\s*-->")
# A shortlist row reads "| 1709 <!-- id:1709 --> | Home Depot ... |". The number the
# model reads and the marker the validator checks are written twice, so they can drift.
ROW_RE = re.compile(r"\|\s*(\d+)\s*<!--\s*id:(\d+)\s*-->")


def iter_curated_ids(paths: Iterable[pathlib.Path]) -> Iterable[tuple[pathlib.Path, int]]:
    """Yield (file, template_id) for every `<!-- id:NNNN -->` marker in a workflow file.

    Workflow prose stays human-authored; the marker is what `validate` checks, so a
    curated recommendation can never outlive the template it names.
    """
    for path in paths:
        for match in MARKER_RE.finditer(path.read_text()):
            yield path, int(match.group(1))


def iter_row_mismatches(paths: Iterable[pathlib.Path]) -> Iterable[tuple[pathlib.Path, str, str]]:
    """Yield rows whose displayed id disagrees with their marker."""
    for path in paths:
        for match in ROW_RE.finditer(path.read_text()):
            shown, marked = match.group(1), match.group(2)
            if shown != marked:
                yield path, shown, marked


def validate(catalog_path: pathlib.Path) -> int:
    catalog = load_catalog(catalog_path)
    by_id = {e["template_id"]: e for e in catalog["templates"]}

    workflow_files = sorted(CURATION_DIR.glob("*.md")) if CURATION_DIR.is_dir() else []
    if not workflow_files:
        print("no workflow files to validate")
        return 0

    problems = 0
    checked = 0

    for path, shown, marked in iter_row_mismatches(workflow_files):
        print(f"MISMATCH {path.relative_to(REPO_ROOT)}: row shows {shown} but marker says {marked}")
        problems += 1

    for path, template_id in iter_curated_ids(workflow_files):
        checked += 1
        where = f"{path.relative_to(REPO_ROOT)}"
        entry = by_id.get(template_id)
        if entry is None:
            print(f"MISSING  {where}: template {template_id} is not in the catalog")
            problems += 1
            continue
        if entry["status"] != "PUBLISHED":
            print(f"STATUS   {where}: {template_id} {entry['name']!r} is {entry['status']}")
            problems += 1
        if entry["run_on"] == "LOCAL":
            print(f"LOCAL    {where}: {template_id} {entry['name']!r} cannot run via MCP")
            problems += 1

    print(f"checked {checked} curated references across {len(workflow_files)} workflow files")
    if problems:
        print(f"{problems} problem(s) found")
    else:
        print("all curated references resolve to published, cloud-capable templates")
    return 1 if problems else 0


def _matches_need(entry: dict[str, Any], rule: dict[str, Any]) -> bool:
    if entry["template_id"] in rule.get("exclude_ids", ()):
        return False
    name = entry["name"].lower()

    tests = []
    if "categories" in rule:
        tests.append(bool(rule["categories"] & set(entry["categories"])))
    if "page_types" in rule:
        tests.append(bool(rule["page_types"] & set(entry["source_page_types"])))
    if "name_any" in rule:
        tests.append(any(kw in name for kw in rule["name_any"]))

    if not tests:
        return False
    return any(tests) if rule.get("match") == "any" else all(tests)


def candidates(catalog_path: pathlib.Path, selector: str, all_languages: bool) -> None:
    """Print the curation worksheet for one need (or a raw category tag)."""
    catalog = load_catalog(catalog_path)
    runnable = [
        e for e in catalog["templates"]
        if e["status"] == "PUBLISHED" and e["run_on"] != "LOCAL"
    ]

    if selector in NEEDS:
        rule = NEEDS[selector]
        rows = [e for e in runnable if _matches_need(e, rule)]
    else:
        rows = [e for e in runnable if selector.lower() in (c.lower() for c in e["categories"])]

    if not all_languages:
        rows = [e for e in rows if e["language"] in ("EN_US", "GLOBAL")]
    rows.sort(key=lambda e: -e["output_field_count"])

    print(f"{selector}: {len(rows)} candidates\n")
    print(f"{'id':>5}  {'lang':7} {'run':5} {'acct':8} {'EPW':3} {'2st':3} {'out':>4}  {'price':14} name")
    for e in rows:
        y = e["yields"]
        # "?" = unknown because the template hides its real output behind an
        # internal detail stage. Confirm against the live schema before ruling it out.
        epw = "".join(
            "?" if y[kind] is None else (letter if y[kind] else "-")
            for kind, letter in (("email", "E"), ("phone", "P"), ("website", "W"))
        )
        two = " * " if e["has_builtin_detail_stage"] else "   "
        print(
            f"{e['template_id']:>5}  {e['language'] or '?':7} {e['run_on']:5} "
            f"{e['min_account_level'] or '?':8} {epw:3} {two} {e['output_field_count']:>4}  "
            f"{(e['price'] or '-'):14} {e['name']}"
        )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    p_build = sub.add_parser("build", help="project a snapshot into data/catalog.json")
    p_build.add_argument("--snapshot", type=pathlib.Path, required=True, help="snapshot directory containing templates/")
    p_build.add_argument("--out", type=pathlib.Path, default=DEFAULT_CATALOG)

    p_validate = sub.add_parser("validate", help="check curated template ids still resolve")
    p_validate.add_argument("--catalog", type=pathlib.Path, default=DEFAULT_CATALOG)

    p_cand = sub.add_parser("candidates", help="print a curation worksheet for one need")
    p_cand.add_argument("--catalog", type=pathlib.Path, default=DEFAULT_CATALOG)
    p_cand.add_argument(
        "--need",
        required=True,
        help=f"a need ({', '.join(NEEDS)}) or a raw category tag",
    )
    p_cand.add_argument("--all-languages", action="store_true")

    args = parser.parse_args(argv)

    if args.command == "build":
        build(args.snapshot, args.out)
        return 0
    if args.command == "validate":
        return validate(args.catalog)
    candidates(args.catalog, args.need, args.all_languages)
    return 0


if __name__ == "__main__":
    sys.exit(main())
