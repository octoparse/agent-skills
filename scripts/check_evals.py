#!/usr/bin/env python3
"""Static checks for the eval sets.

These do not run a model. Running behavioural evals needs an agent, an authorized
MCP connection, and a budget, so it belongs in a manual or scheduled job rather
than in CI on every push.

What CI *can* enforce is that the evals stay wired to reality: that a case does
not assert a file which has been renamed, cite a template id that no longer
resolves, or promise behaviour no guide actually documents. Those are the ways an
eval set rots silently — it keeps passing review because nobody reads it, then
turns out to have been asserting against a deleted path all along.

Usage:
    python3 scripts/check_evals.py
"""

from __future__ import annotations

import json
import pathlib
import re
import sys

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILL_DIR = REPO_ROOT / "skills" / "octoparse-ultimate-scraper"
EVAL_DIR = SKILL_DIR / "evals"
CATALOG = REPO_ROOT / "data" / "catalog.json"

# Any `references/...md` or `<name>.md` mentioned inside an eval must exist.
PATH_RE = re.compile(r"(?:references/)?[\w./-]+\.md")
# A bare number of four digits or fewer, when it appears next to "template", is a
# template id being asserted.
ID_RE = re.compile(r"template\s+(\d{1,4})\b", re.IGNORECASE)


def fail(problems: list[str], message: str) -> None:
    problems.append(message)


def load_json(path: pathlib.Path, problems: list[str]):
    if not path.is_file():
        fail(problems, f"missing: {path.relative_to(REPO_ROOT)}")
        return None
    try:
        return json.loads(path.read_text())
    except json.JSONDecodeError as exc:
        fail(problems, f"{path.relative_to(REPO_ROOT)}: invalid JSON — {exc}")
        return None


def check_behavioural(data, catalog_ids: set[int], problems: list[str]) -> int:
    cases = data.get("evals") if isinstance(data, dict) else data
    if not isinstance(cases, list):
        fail(problems, "evals.json: expected a list of cases, or an object with an 'evals' list")
        return 0

    seen_ids = set()
    for case in cases:
        cid = case.get("id", "<no id>")
        where = f"evals.json case {cid}"

        if cid in seen_ids:
            fail(problems, f"{where}: duplicate id")
        seen_ids.add(cid)

        for field in ("prompt", "expected_output", "assertions"):
            if not case.get(field):
                fail(problems, f"{where}: empty or missing '{field}'")

        assertions = case.get("assertions") or []
        if isinstance(assertions, list) and len(assertions) < 2:
            fail(problems, f"{where}: only {len(assertions)} assertion(s) — a case with one "
                           f"assertion tests a fact, not a behaviour")

        blob = " ".join([case.get("expected_output", ""), *assertions])

        # Referenced files must exist.
        for ref in PATH_RE.findall(blob):
            name = ref.split("/")[-1]
            if not list(SKILL_DIR.rglob(name)):
                fail(problems, f"{where}: references '{ref}', which no file matches")

        # Referenced template ids must resolve.
        for raw in ID_RE.findall(blob):
            if int(raw) not in catalog_ids:
                fail(problems, f"{where}: asserts template {raw}, not in the catalog")

    return len(cases)


def check_triggers(data, problems: list[str]) -> int:
    if not isinstance(data, list):
        fail(problems, "trigger-evals.json: expected a list")
        return 0

    positives = negatives = 0
    for case in data:
        text = case.get("query") or case.get("prompt")
        where = f"trigger-evals.json {case.get('group', '<no group>')}"
        if not text:
            fail(problems, f"{where}: case has neither 'query' nor 'prompt'")
        if "should_trigger" not in case:
            fail(problems, f"{where}: missing 'should_trigger'")
            continue
        if case["should_trigger"]:
            positives += 1
        else:
            negatives += 1

    # A trigger set without negatives only proves the skill fires, never that it
    # stays quiet — which is the half that actually degrades as descriptions grow.
    if negatives == 0:
        fail(problems, "trigger-evals.json: no negative cases")
    elif negatives < positives / 5:
        fail(problems, f"trigger-evals.json: {negatives} negative vs {positives} positive — "
                       f"too few negatives to catch over-triggering")

    return positives + negatives


def main() -> int:
    problems: list[str] = []

    catalog = load_json(CATALOG, problems)
    catalog_ids = {e["template_id"] for e in catalog["templates"]} if catalog else set()

    behavioural = load_json(EVAL_DIR / "evals.json", problems)
    triggers = load_json(EVAL_DIR / "trigger-evals.json", problems)

    n_behavioural = check_behavioural(behavioural, catalog_ids, problems) if behavioural else 0
    n_triggers = check_triggers(triggers, problems) if triggers else 0

    print(f"checked {n_behavioural} behavioural and {n_triggers} trigger cases")

    if problems:
        for p in problems:
            print(f"  {p}")
        print(f"{len(problems)} problem(s) found")
        return 1

    print("eval sets are internally consistent")
    return 0


if __name__ == "__main__":
    sys.exit(main())
