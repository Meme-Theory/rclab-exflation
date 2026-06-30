"""
_joint_theorem_independent_verify_audit.py

Two-agent independent-verify gate-completeness audit
(T4-17, S86 W-9 AUDIT-4).

# NEEDS-ORCHESTRATOR-FOLLOWUP: NEEDS-DECISION readiness — orchestrator
# must approve the joint-theorem 4-stage promotion pathway (RULE-1)
# AND the format of the Stage-2 verify-dispatch tag in plan blocks
# BEFORE this audit fires non-trivially. The audit infrastructure
# is COMPLETE here; activation depends on first joint theorem
# entering Stage 2 (S88+ per W-9 CF-6 spec).

Purpose
-------
For joint cross-axis theorem registrations (e.g., the Joint F_2-Class
Path-(c) Theorem, S86 W-9), audit verifies the Stage 2 promotion
gate is dispatched to TWO agents (one spectral-side, one transit-side)
when the theorem contains joint-axis clauses. Refuses Stage 2 → 3
promotion if a single-agent verify fired on joint clauses.

4-stage promotion pathway (W-9 RULE-1):
  Stage 0: workshop-internal candidate
  Stage 1: S87 registration as candidate
  Stage 2: two-agent parallel cross-check
  Stage 3: permanent registration (joins KO-dim=6, etc.)

Joint-clause definition: a clause whose validation requires evidence
from BOTH a spectral-side axis (e.g., HC^2 cohomology, HKR pairing,
Mellin-cone moments) AND a transit-side axis (e.g., SR-LO ODE,
Bogoliubov backreaction-onset N, autocatalysis bound).

Audit logic:
  Read Stage-1 registry entry's clause list and per-clause axis tags.
  For each joint-axis clause, verify the Stage-2 verify-dispatch
  recorded TWO independent agent verdicts (one per axis).
  Refuse Stage 2 → 3 if any joint clause has only single-agent
  verification.

Sample joint clauses (Joint F_2-Class Path-(c) Theorem, W-9 R-1):
  Clauses (a), (e)  — spectral-side only
  Clauses (b), (f)  — transit-side only
  Clauses (c), (d)  — JOINT-AXIS (both required)

Source
------
S86 W-9 §AUDIT-4 (lines 37-38).
S86 W-9 §T-CR3.2 (workshop lines 2094-2148).
S86 W-9 §L-ER3.2 (lines 1948-2003).
S86 W-9 RULE-1: 4-stage upgrade pathway.
S86 W-9 CF-6: S88-OR-LATER-EXTENDED-THEOREM-INDEPENDENT-VERIFY.

Provenance
----------
S86 W0c-7 housekeeping queue Tier-4 row T4-17.
Promoted from S86 W-9 AUDIT-4 (lizzi+transit, 2026-04-26).

Status
------
SCAFFOLD. Major dependencies marked TODO(S87+):
  - Joint-theorem registry-entry format (clause-list + axis tags)
    must be canonical in `permanent-results-registry.md`
  - Stage-2 verify-dispatch tag format must be plan-frozen

Usage (post-S88 wire-up)
------------------------
    python _joint_theorem_independent_verify_audit.py
    python _joint_theorem_independent_verify_audit.py --json
    python _joint_theorem_independent_verify_audit.py --strict

Stage-0-authorship reviewer-exclusion check (S100a hardening)
------------------------------------------------------------
S99 W3-1 lesson (E1 / §VII.BL): the original axis-A Stage-2 reviewer
(`connes-ncg-theorist`) was an E1 Stage-0 CO-AUTHOR — a
`joint-theorem-promotion.md` Stage-2 audit-item-3 violation caught at
session close and re-dispatched (corrective verdict 0f0c4f65 supersedes
13998949). The exclusion attaches to the REGISTERED §VII entry's
Stage-0 authorship (Sponsors / co-author lines), NOT merely the
immediately-prior column-computing gates. Recurrence prevention
(S99 housekeeping §A process observations → S100a plan-freeze):

    python _joint_theorem_independent_verify_audit.py \
        --check-reviewers VII.AM \
        --reviewers lizzi-spectral-functional-theorist,schwarzschild-penrose-geometer
    python _joint_theorem_independent_verify_audit.py --self-test

The check extracts the Stage-0 author set from the registered slot
block (full agent names anywhere in authorship-context lines; short
aliases like `volovik PRIMARY + connes CO-AUTHOR` only on lines
carrying the short-form markers) and FAILS if any proposed reviewer is
in that set. Conservative by design: an entry-landing writer (e.g.
mack as registry-row author) is included in the exclusion set — the
cost of over-exclusion is a substitute reviewer; the cost of
under-exclusion is a compromised Stage-2.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# Project canonical constants (mandatory per .claude/rules/math-scripts.md S34+).
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import *  # noqa: F401,F403


# ---------------------------------------------------------------------------
# Pinned audit parameters
# ---------------------------------------------------------------------------

REGISTRY_PATH = (
    # __file__ = computations/_shared/<this>.py → project root is THREE levels up.
    # (S100a fix: the S86 scaffold used parent.parent → computations/sessions/…,
    #  a path bug never caught because the audit had not fired non-trivially.)
    Path(__file__).resolve().parent.parent.parent
    / "sessions" / "permanent-results-registry.md"
)

# Joint-theorem section header pattern.
JOINT_SECTION_REGEX = re.compile(
    r"^#+\s*Joint\s+(?P<name>.+?)\s+Theorem\b.*$",
    re.IGNORECASE | re.MULTILINE,
)

# Per-clause axis tag patterns within a joint section.
SPECTRAL_AXIS_KEYWORDS = (                                # (local)
    "spectral-side", "hc^2", "hkr", "mellin-cone moment",
    "spectral-functional", "ncg axiom",
)
TRANSIT_AXIS_KEYWORDS = (                                  # (local)
    "transit-side", "sr-lo", "bogoliubov", "backreaction-onset",
    "autocatalysis", "transit-dynamics",
)

# Stage-2 verify-dispatch tag pattern within a clause block.
VERIFY_TAG_REGEX = re.compile(
    r"verified[-_\s]?by[\s:]+(?P<agent>[a-z0-9-_]+)",
    re.IGNORECASE,
)


# ---------------------------------------------------------------------------
# Core audit
# ---------------------------------------------------------------------------

def find_joint_theorem_sections(registry_text: str) -> list[dict]:
    """Locate joint-theorem sections in the registry."""
    sections = []                                          # (local)
    matches = list(JOINT_SECTION_REGEX.finditer(registry_text))
    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(registry_text)
        sections.append({
            "name": m.group("name").strip(),
            "anchor": m.group(0).strip(),
            "start": start,
            "end": end,
            "text": registry_text[start:end],
        })
    return sections


def split_into_clauses(section_text: str) -> list[dict]:
    """Split section text into clauses by `Clause (X)` or `clause (X)` headers."""
    clause_regex = re.compile(
        r"^[\-\*\s]*[Cc]lause\s*\(([a-z])\)\s*[:\.\-]?\s*(.*?)(?=^[\-\*\s]*[Cc]lause\s*\(|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    clauses = []                                           # (local)
    for m in clause_regex.finditer(section_text):
        clauses.append({
            "letter": m.group(1).lower(),
            "body": m.group(2).strip(),
        })
    return clauses


def classify_clause_axis(body_lower: str) -> str:
    """Classify a clause as spectral-only / transit-only / joint."""
    has_spectral = any(k in body_lower for k in SPECTRAL_AXIS_KEYWORDS)
    has_transit = any(k in body_lower for k in TRANSIT_AXIS_KEYWORDS)
    if has_spectral and has_transit:
        return "joint"
    if has_spectral:
        return "spectral_only"
    if has_transit:
        return "transit_only"
    return "unclassified"


def extract_verify_agents(body: str) -> list[str]:
    """Extract list of `verified-by: <agent>` tags within a clause."""
    return [m.group("agent").lower() for m in VERIFY_TAG_REGEX.finditer(body)]


# ---------------------------------------------------------------------------
# Stage-0-authorship reviewer-exclusion check (S100a hardening; S99 E1 lesson)
# ---------------------------------------------------------------------------

# Known agent roster (full names as they appear in registry authorship lines).
KNOWN_AGENTS = frozenset({                                 # (local)
    "baptista-spacetime-analyst", "berry-geometric-phase-theorist",
    "connes-ncg-theorist", "cosmic-web-theorist", "dirac-antimatter-theorist",
    "einstein-theorist", "feynman-theorist", "gen-physicist",
    "hawking-theorist", "kaku-speculative-theorist", "kaluza-klein-theorist",
    "kitaev-quantum-chaos-theorist", "landau-condensed-matter-theorist",
    "little-red-dots-jwst-analyst", "lizzi-spectral-functional-theorist",
    "loop-quantum-gravity-theorist", "mack-cosmic-bridge",
    "nazarewicz-nuclear-structure-theorist", "neutrino-detection-specialist",
    "paasch-mass-quantization-analyst", "phonon-first-cosmologist",
    "quantum-acoustics-theorist", "quantum-foam-theorist", "sagan-empiricist",
    "schwarzschild-penrose-geometer", "spectral-geometer",
    "string-theory-theorist", "tesla-resonance", "transit-dynamics-theorist",
    "van-den-dungen-bridge-theorist", "volovik-superfluid-universe-theorist",
})

# Short aliases used in registry header idiom ("volovik PRIMARY + connes CO-AUTHOR").
ALIAS_MAP = {                                              # (local)
    "baptista": "baptista-spacetime-analyst",
    "connes": "connes-ncg-theorist",
    "dirac": "dirac-antimatter-theorist",
    "hawking": "hawking-theorist",
    "kk": "kaluza-klein-theorist",
    "kaluza-klein": "kaluza-klein-theorist",
    "landau": "landau-condensed-matter-theorist",
    "lizzi": "lizzi-spectral-functional-theorist",
    "mack": "mack-cosmic-bridge",
    "transit": "transit-dynamics-theorist",
    "vdd": "van-den-dungen-bridge-theorist",
    "volovik": "volovik-superfluid-universe-theorist",
}

# A line is authorship-context iff it carries one of these markers.
AUTHORSHIP_LINE_REGEX = re.compile(                        # (local)
    r"(PRIMARY|CO-AUTHOR|co-author|co-authored|primary author"
    r"|authorship|authoring|Sponsors)",
)
# Reviewer-ASSIGNMENT lines name reviewers by construction, never authors
# (e.g. §VII.AM's own Stage-2 dispatch spec: "Semiclassical-gravity-axis
# cross-reviewer: hawking-theorist (or schwarzschild-penrose-geometer) …
# must use schwarzschild-penrose-geometer instead"). Such lines often ALSO
# contain authorship marker words ("hawking authored Stage-0 …"), so they
# must be skipped to avoid harvesting a registry-nominated SUBSTITUTE
# reviewer as an author (S100a calibration: schwarzschild over-catch).
REVIEWER_ASSIGNMENT_LINE_REGEX = re.compile(               # (local)
    r"(?i)cross-review",
)
# Short-form alias harvesting fires only on lines carrying these markers
# (the "volovik PRIMARY + connes CO-AUTHOR" registry idiom).
SHORTFORM_MARKER_REGEX = re.compile(                       # (local)
    r"(PRIMARY|CO-AUTHOR|co-authored)"
)


def normalize_agent(name: str) -> str:
    """Map a short alias to its canonical full agent name."""
    n = name.strip().lower()                               # (local)
    return ALIAS_MAP.get(n, n)


def find_registry_slot_block(registry_text: str, slot: str) -> str | None:
    """Locate the §VII.<slot> section block (header → next ## header)."""
    slot_norm = slot.strip().lstrip("§").upper()           # (local)
    if not slot_norm.startswith("VII"):
        slot_norm = "VII." + slot_norm                     # (local)
    header_regex = re.compile(                             # (local)
        r"^##+\s+.*§" + re.escape(slot_norm) + r"(?![A-Z0-9.\-])",
        re.MULTILINE,
    )
    m = header_regex.search(registry_text)                 # (local)
    if m is None:
        return None
    nxt = re.compile(r"^##\s+", re.MULTILINE).search(registry_text, m.end())  # (local)
    return registry_text[m.start(): nxt.start() if nxt else len(registry_text)]


def extract_stage0_authors(block_text: str) -> set[str]:
    """Extract the Stage-0 author set from a registered slot block.

    Full agent names are harvested from any authorship-context line;
    short aliases only from lines carrying the short-form markers.
    Conservative: registry-landing writers count as authors (the cost
    of over-exclusion is a substitute reviewer).
    """
    authors: set[str] = set()                              # (local)
    for line in block_text.splitlines():
        if not AUTHORSHIP_LINE_REGEX.search(line):
            continue
        if REVIEWER_ASSIGNMENT_LINE_REGEX.search(line):
            continue  # reviewer-assignment line — names reviewers, not authors
        low = line.lower()                                 # (local)
        for full in KNOWN_AGENTS:
            if full in low:
                authors.add(full)
        if SHORTFORM_MARKER_REGEX.search(line):
            for alias, full in ALIAS_MAP.items():
                if re.search(r"\b" + re.escape(alias) + r"\b", low):
                    authors.add(full)
    return authors


def check_stage2_reviewer_exclusion(
    slot: str, reviewers: list[str], registry_text: str
) -> dict:
    """Cross-reference proposed Stage-2 reviewers against the registered
    §VII slot's Stage-0 authorship (S99 E1 lesson; joint-theorem-promotion.md
    Stage-2 audit item 3 + Axis-B Selection Protocol condition 2)."""
    block = find_registry_slot_block(registry_text, slot)  # (local)
    if block is None:
        return {
            "check_id": "STAGE0-AUTHORSHIP-REVIEWER-EXCLUSION",
            "slot": slot,
            "verdict": "INFO_SLOT_NOT_FOUND",
            "note": f"no §{slot} section header found in registry",
        }
    authors = extract_stage0_authors(block)                # (local)
    proposed = [normalize_agent(r) for r in reviewers]     # (local)
    violations = sorted(set(p for p in proposed if p in authors))  # (local)
    return {
        "check_id": "STAGE0-AUTHORSHIP-REVIEWER-EXCLUSION",
        "slot": slot,
        "stage0_authors": sorted(authors),
        "proposed_reviewers": proposed,
        "violations": violations,
        "verdict": "EXCLUSION-FAIL" if violations else "EXCLUSION-PASS",
        "note": (
            "violating reviewer(s) are Stage-0 authors of the registered "
            "entry; re-select per joint-theorem-promotion.md Axis-B "
            "Selection Protocol (downstream-inheritance reach test still "
            "applies to substitutes at dispatch time)"
            if violations else
            "no proposed reviewer is a registered Stage-0 author; the "
            "downstream-inheritance reach test (condition 2b) still "
            "applies at dispatch time"
        ),
    }


def run_self_test() -> dict:
    """Synthetic POSITIVE + NEGATIVE cases for the exclusion check."""
    synthetic = (                                          # (local)
        "## §VII.ZZ — Synthetic Test Theorem (S00 W-0 — volovik PRIMARY "
        "+ connes + mack co-authored, 2026-01-01)\n\n"
        "### Sponsors\n\n"
        "- **hawking-theorist** — semiclassical-gravity-axis primary author\n"
        "- **transit-dynamics-theorist** — transit-axis co-author for the "
        "substrate cascade transit framework\n\n"
        "body text mentioning lizzi-spectral-functional-theorist in plain "
        "prose carrying no marker words at all.\n"
    )
    pos = check_stage2_reviewer_exclusion(                 # (local)
        "VII.ZZ", ["connes-ncg-theorist", "lizzi-spectral-functional-theorist"],
        synthetic,
    )
    neg = check_stage2_reviewer_exclusion(                 # (local)
        "VII.ZZ",
        ["lizzi-spectral-functional-theorist", "schwarzschild-penrose-geometer"],
        synthetic,
    )
    expected_authors = {                                   # (local)
        "volovik-superfluid-universe-theorist", "connes-ncg-theorist",
        "mack-cosmic-bridge", "hawking-theorist", "transit-dynamics-theorist",
    }
    ok = (                                                 # (local)
        pos["verdict"] == "EXCLUSION-FAIL"
        and pos["violations"] == ["connes-ncg-theorist"]
        and neg["verdict"] == "EXCLUSION-PASS"
        and set(pos["stage0_authors"]) == expected_authors
    )
    return {
        "self_test": "PASS" if ok else "FAIL",
        "positive_case": pos,
        "negative_case": neg,
        "expected_authors_matched": set(pos["stage0_authors"]) == expected_authors,
    }


def audit_joint_section(section: dict) -> dict:
    """Audit a single joint-theorem section."""
    clauses = split_into_clauses(section["text"])         # (local)
    clause_audits = []                                     # (local)
    joint_violations = []                                  # (local)

    for clause in clauses:
        axis = classify_clause_axis(clause["body"].lower())  # (local)
        agents = extract_verify_agents(clause["body"])    # (local)
        unique_agents = sorted(set(agents))                # (local)

        # For joint clauses: require ≥ 2 distinct verifying agents.
        if axis == "joint":
            sufficient = len(unique_agents) >= 2
            if not sufficient:
                joint_violations.append({
                    "clause": clause["letter"],
                    "verifiers": unique_agents,
                    "reason": (
                        f"joint-axis clause has {len(unique_agents)} verifier(s); "
                        "needs ≥ 2 distinct agents (one spectral, one transit)"
                    ),
                })
        else:
            sufficient = len(unique_agents) >= 1

        clause_audits.append({
            "clause": clause["letter"],
            "axis": axis,
            "verifiers": unique_agents,
            "sufficient_for_promotion": sufficient,
        })

    # PASS only if every clause sufficient (joint clauses ≥ 2 verifiers).
    promotion_blocked = len(joint_violations) > 0
    return {
        "section_name": section["name"],
        "n_clauses": len(clauses),
        "joint_violations": joint_violations,
        "promotion_blocked": promotion_blocked,
        "clause_audits": clause_audits,
    }


def run_audit() -> dict:
    """Run the joint-theorem independent-verify audit."""
    if not REGISTRY_PATH.exists():
        return {
            "audit_id": "S86-W9-JOINT-THEOREM-INDEPENDENT-VERIFY",
            "verdict": "INFO_NO_REGISTRY",
            "registry_path": str(REGISTRY_PATH),
            "blocked_by": "permanent-results-registry.md not found",
        }

    text = REGISTRY_PATH.read_text(encoding="utf-8")      # (local)
    sections = find_joint_theorem_sections(text)          # (local)
    if not sections:
        return {
            "audit_id": "S86-W9-JOINT-THEOREM-INDEPENDENT-VERIFY",
            "verdict": "INFO_NO_JOINT_THEOREMS",
            "note": (
                "No `Joint ... Theorem` sections found in registry. "
                "Audit becomes load-bearing once first joint theorem "
                "(e.g., Joint F_2-Class Path-(c)) lands at Stage 1 (S87)."
            ),
        }

    audits = [audit_joint_section(s) for s in sections]   # (local)
    any_blocked = any(a["promotion_blocked"] for a in audits)
    verdict = "FAIL" if any_blocked else "PASS"

    return {
        "audit_id": "S86-W9-JOINT-THEOREM-INDEPENDENT-VERIFY",
        "verdict": verdict,
        "n_joint_sections": len(sections),
        "section_audits": audits,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Joint-theorem independent-verify audit (T4-17 / S86 W-9 AUDIT-4)"
    )
    parser.add_argument("--json", action="store_true",
                        help="emit machine-readable JSON")
    parser.add_argument("--strict", action="store_true",
                        help="exit nonzero on FAIL")
    parser.add_argument("--check-reviewers", metavar="SLOT",
                        help="Stage-0-authorship reviewer-exclusion check for "
                             "a §VII slot (e.g. VII.AM); use with --reviewers")
    parser.add_argument("--reviewers", metavar="A,B,C",
                        help="comma-separated proposed Stage-2 reviewer agent "
                             "names (full names or short aliases)")
    parser.add_argument("--self-test", action="store_true",
                        help="run synthetic positive+negative exclusion-check "
                             "cases (no registry dependency)")
    args = parser.parse_args()

    if args.self_test:
        result = run_self_test()                           # (local)
        print(json.dumps(result, indent=2, default=str) if args.json
              else f"self_test: {result['self_test']}  "
                   f"(positive={result['positive_case']['verdict']}, "
                   f"negative={result['negative_case']['verdict']}, "
                   f"authors_matched={result['expected_authors_matched']})")
        return 0 if result["self_test"] == "PASS" else 1

    if args.check_reviewers:
        if not args.reviewers:
            print("ERROR: --check-reviewers requires --reviewers A,B,C")
            return 2
        if not REGISTRY_PATH.exists():
            print(f"ERROR: registry not found at {REGISTRY_PATH}")
            return 2
        text = REGISTRY_PATH.read_text(encoding="utf-8")   # (local)
        result = check_stage2_reviewer_exclusion(          # (local)
            args.check_reviewers,
            [r for r in args.reviewers.split(",") if r.strip()],
            text,
        )
        if args.json:
            print(json.dumps(result, indent=2, default=str))
        else:
            print(f"=== Stage-0-authorship reviewer-exclusion: §{result['slot']} ===")
            print(f"Verdict: {result['verdict']}")
            for k in ("stage0_authors", "proposed_reviewers", "violations", "note"):
                if k in result:
                    print(f"  {k}: {result[k]}")
        if args.strict and result["verdict"] == "EXCLUSION-FAIL":
            return 1
        return 0

    result = run_audit()                                   # (local)

    if args.json:
        print(json.dumps(result, indent=2, default=str))
    else:
        print("=== S86 W-9 / T4-17 Joint-Theorem Independent-Verify Audit ===")
        print(f"Verdict: {result['verdict']}")
        for k in ("note", "blocked_by", "n_joint_sections"):
            if k in result:
                print(f"  {k}: {result[k]}")
        for sa in result.get("section_audits", []):
            blocked = "BLOCKED" if sa["promotion_blocked"] else "OK"
            print(f"\n  Section: {sa['section_name']} → {blocked}")
            print(f"    Clauses: {sa['n_clauses']}")
            for v in sa["joint_violations"]:
                print(f"    VIOLATION clause ({v['clause']}): {v['reason']}")

    if args.strict and result["verdict"] == "FAIL":
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
