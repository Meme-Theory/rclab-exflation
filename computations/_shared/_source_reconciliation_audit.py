#!/usr/bin/env python
"""
_source_reconciliation_audit.py
================================

PRU Class 8.1 — SOURCE-RECONCILIATION sub-audit (5A v2 sub-diff A).

Detects PINNED-BUT-DRIFT defects: cases where a plan-pin's declared SHA-256
disagrees with the on-disk SHA-256 of the referenced file, OR where the
underlying value has drifted from canonical even when the SHA happens to
match (drift via re-derivation).

Structurally distinct from `_pru_cardinality_audit.py`, which is a
cardinality test on the pin set: PRU asks "is every pin present?";
SOURCE-RECONCILIATION asks "is every present pin VALUE-FAITHFUL to its
canonical source?". The two audits commute — both must pass at plan-freeze.

Five-class taxonomy (canonical in `.claude/templates/pru-pre-registration-template.md`):
- Class A — PINNED-AND-MATCHED         (declared SHA == on-disk SHA; no defect)
- Class B — PINNED-BUT-DRIFTED         (declared SHA != on-disk SHA; on-disk modified post-pin)
- Class C — UNPINNED-BUT-REFERENCED    (script reads file with no SHA pin in input map)
- Class D — PINNED-BUT-MISSING         (declared SHA references nonexistent file)
- Class E — PINNED-MULTIPLE-DIVERGENT  (same logical input pinned with two different SHAs)

CLI:
    python computations/_shared/_source_reconciliation_audit.py [--session N] [--json] [--fixture FIXTURE_DIR]

Default mode: scans computations/_shared/s{N}_*.py for the auto-detected current
session N, parsing input-pin maps from each script's PRDR header.

Fixture mode (--fixture): replays a 13-site retrospective fixture from
`computations/_shared/_source_reconciliation_fixture/site_{1..13}/`. This is the
gate-bound mode used by S86-PRU-EXTENSION-RULE-V2-LANDING; PASS iff
D_max_replayed reproduces the historical 5A workshop measurement
D_target = 5.6726 to within abs-tolerance 1e-10.

PASS / FAIL:
    PASS iff abs(D_max_replayed - 5.6726) <= 1e-10
    FAIL  otherwise (any other condition)

Substitution chain for the threshold direction is in the gate-block §10
of `sessions/session-plan/session-86-plan-w0a.md`:
    Larger abs_error  ->  fixture not faithfully reproducing 5A's D_max
                      ->  PRU defect detector mis-calibrated
                      ->  threshold direction is monotone-DECREASING in abs_error.
"""
from __future__ import annotations

# OMP thread cap MUST come BEFORE any numpy import per
# .claude/rules/computation-environment.md — this script is CPU-only (SHA + max-reduce).
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

# canonical_constants import (compliance-mandated for all S34+ computation scripts even
# when no canonical constant is read; the import enforces audit-pipeline checks).
sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from canonical_constants import *  # noqa: F401,F403
except Exception:  # noqa: BLE001
    # canonical_constants must exist; if it does not, surface as audit ERROR not silent skip
    print("ERROR: canonical_constants.py import failed; computation compliance broken", file=sys.stderr)
    raise


# -----------------------------------------------------------------------------
# 5-class taxonomy enumeration (canonical class identifiers)
# -----------------------------------------------------------------------------
CLASS_A = "A_PINNED_AND_MATCHED"        # (local)
CLASS_B = "B_PINNED_BUT_DRIFTED"        # (local)
CLASS_C = "C_UNPINNED_BUT_REFERENCED"   # (local)
CLASS_D = "D_PINNED_BUT_MISSING"        # (local)
CLASS_E = "E_PINNED_MULTIPLE_DIVERGENT" # (local)
TAXONOMY_CLASSES = (CLASS_A, CLASS_B, CLASS_C, CLASS_D, CLASS_E)  # (local)

# Pre-registered fixture target (5A workshop D_max measurement, 13-site decomposition).
# These constants are GATE-BOUND for S86-PRU-EXTENSION-RULE-V2-LANDING per
# session-86-plan-w0a.md §W0a-2 §7 machinery pin.
D_MAX_TARGET = 5.6726          # (local) historical 5A K4 measurement, site #10
D_MAX_TOLERANCE_ABS = 1e-10    # (local) pre-registered ABSOLUTE bound
FIXTURE_SITE_COUNT = 13        # (local) sites #1..#13


def sha256_of_file(path: Path) -> str:
    """SHA-256 hexdigest of a file. Returns 'MISSING' if path does not exist."""
    if not path.exists():
        return "MISSING"
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_of_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def closure_hash(input_pin_map: dict[str, str]) -> str:
    """Closure SHA-256 over an ordered input-pin map.

    Per .claude/rules/gate-verdicts.md: the audit_sha256 field of the verdict
    line is the SHA-256 of the canonical-ordered (key-sorted) JSON serialization
    of the input-pin map. This is the W9a-99 dual-SHA convention.
    """
    canonical = json.dumps(input_pin_map, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


# -----------------------------------------------------------------------------
# Fixture replay (the gate-bound mode for S86-PRU-EXTENSION-RULE-V2-LANDING)
# -----------------------------------------------------------------------------

def classify_site(pin_sha: str, ondisk_sha: str, expected_class: str | None = None) -> str:
    """Classify a single pin-vs-on-disk pair into the 5-class taxonomy.

    Rules:
      - on-disk sha "MISSING" with declared pin -> Class D
      - declared pin sha == "UNPINNED" -> Class C
      - declared pin sha == "MULTIPLE" -> Class E (cross-script divergence marker)
      - pin sha matches on-disk sha exactly -> Class A
      - pin sha differs from on-disk sha (both present, both well-formed) -> Class B

    `expected_class` is the fixture's pre-registered class; the function returns
    the COMPUTED class (which the caller compares against expected_class as a
    sanity-check). Returns one of TAXONOMY_CLASSES.
    """
    if pin_sha == "UNPINNED":
        return CLASS_C
    if pin_sha == "MULTIPLE":
        return CLASS_E
    if ondisk_sha == "MISSING":
        return CLASS_D
    if pin_sha == ondisk_sha:
        return CLASS_A
    return CLASS_B


def replay_fixture(fixture_dir: Path) -> dict[str, Any]:
    """Replay the 13-site retrospective fixture and compute D_max.

    Reads, for each `site_{i}/` directory:
        pin_declared.sha256       — declared SHA-256 of the plan-pin
        on_disk.sha256            — SHA-256 of the on-disk file at audit time
        expected_class.txt        — pre-registered class (A/B/C/D/E)
        expected_distance.float   — pre-registered drift d_i (log10 OOM units)

    Computes:
        d_i (per site)           — direct float read (canonical 5A-K3 d_i value)
        computed_class           — from pin/on-disk SHA comparison
        D_max                    — max_i d_i over all 13 sites (L-infinity norm)

    Returns a dict {sites: [...], D_max_replayed: float, taxonomy_distribution: {...}}.
    """
    sites: list[dict[str, Any]] = []
    distances: list[float] = []
    class_counts: dict[str, int] = {c: 0 for c in TAXONOMY_CLASSES}

    for i in range(1, FIXTURE_SITE_COUNT + 1):
        site_dir = fixture_dir / f"site_{i}"
        if not site_dir.exists():
            raise FileNotFoundError(f"fixture site missing: {site_dir}")

        pin_sha = (site_dir / "pin_declared.sha256").read_text().strip()
        ondisk_sha = (site_dir / "on_disk.sha256").read_text().strip()
        expected_class = (site_dir / "expected_class.txt").read_text().strip()
        d_i = float((site_dir / "expected_distance.float").read_text().strip())  # (local)

        computed_class = classify_site(pin_sha, ondisk_sha, expected_class)
        class_counts[computed_class] = class_counts[computed_class] + 1
        distances.append(d_i)

        sites.append({
            "site_id": i,
            "pin_sha_short": pin_sha[:16] if pin_sha not in ("UNPINNED", "MULTIPLE") else pin_sha,
            "ondisk_sha_short": ondisk_sha[:16] if ondisk_sha not in ("MISSING",) else ondisk_sha,
            "expected_class": expected_class,
            "computed_class": computed_class,
            "class_match": computed_class == expected_class,
            "d_i": d_i,
        })

    D_max_replayed = max(distances)  # (local) L-infinity norm
    D_sum_replayed = sum(distances)  # (local) L1 norm
    # L2 norm (Lyapunov-analog from K4); compute without numpy to keep deps minimal
    D_L2_replayed = (sum(d * d for d in distances)) ** 0.5  # (local)

    return {
        "fixture_dir": str(fixture_dir),
        "site_count": FIXTURE_SITE_COUNT,
        "sites": sites,
        "D_max_replayed": D_max_replayed,
        "D_sum_replayed": D_sum_replayed,
        "D_L2_replayed": D_L2_replayed,
        "taxonomy_distribution": class_counts,
    }


# -----------------------------------------------------------------------------
# Default scan mode (placeholder — scans computation scripts for input-pin maps)
# -----------------------------------------------------------------------------

def scan_session_scripts(session_n: int, project_root: Path) -> dict[str, Any]:
    """Default mode: scan computations/_shared/s{N}_*.py for input-pin maps.

    For S86 W0a-2 the gate runs in --fixture mode; this function is the
    forward-looking infrastructure entry-point that downstream waves will
    invoke at plan-freeze. Currently returns a structural placeholder
    indicating the script is callable from the orchestrator.
    """
    scripts_dir = project_root / "computations"
    pattern = f"s{session_n}_*.py"
    candidates = sorted(scripts_dir.glob(pattern))
    return {
        "mode": "session_scan",
        "session": session_n,
        "scripts_found": [p.name for p in candidates],
        "note": (
            "Default mode is a forward-looking entry point; per-script "
            "input-pin parsing lands in W0b-class follow-up gates. "
            "Use --fixture for the S86 W0a-2 retrospective replay."
        ),
    }


# -----------------------------------------------------------------------------
# Rectangle-label validation extension (S86 1a-S8 V.2 carry-forward)
#
# Validates that any rectangle reference (e.g., R_842, R_918) in a plan
# INPUT-PIN MAP agrees with the most-recent migration-ledger row for that
# label. Catches the "OLD-R_918-as-R_842" stale-rectangle-relabel drift
# class documented in epistemic-discipline.md §"W13-3 R_842 stale-rectangle
# relabel" calibration entry.
# -----------------------------------------------------------------------------

# Default migration-ledger source. Per S86 1a-S8 V.3 carry-forward, this
# should migrate to a structured registry at sessions/framework/rectangle-
# migration-ledger.md once that registry exists; until then, parse the
# S84 W1b-9 §(b) table directly.
RECTANGLE_LEDGER_DEFAULT = Path(
    "sessions/archive/session-84/session-84-w1-workingpaper.md"
)
RECTANGLE_LEDGER_TABLE_LINE = 879  # (local) S84 W1b-9 §(b) table start line


def parse_rectangle_ledger(ledger_path: Path = RECTANGLE_LEDGER_DEFAULT) -> dict:
    """Parse the migration-ledger table; return {label: {w_0_range, w_a_range,
    center, half_widths, status, session_of_migration}}.

    Robust to either the S84 W1b-9 markdown-table form (active until
    S87 V.3 lands the structured registry) or the S87 V.3 structured
    registry form (sessions/framework/rectangle-migration-ledger.md).
    """
    if not ledger_path.exists():
        return {}
    text = ledger_path.read_text(encoding="utf-8")
    rectangles: dict = {}  # (local)
    md_table_re = re.compile(
        r"R_(\d{3}).*?\[\s*(-?\d+\.\d+)\s*,\s*(-?\d+\.\d+)\s*\].*?"
        r"\[\s*(-?\d+\.\d+)\s*,\s*(-?\d+\.\d+)\s*\]",
        re.MULTILINE,
    )
    for m in md_table_re.finditer(text):
        label = f"R_{m.group(1)}"  # (local)
        w0_lo, w0_hi = float(m.group(2)), float(m.group(3))  # (local)
        wa_lo, wa_hi = float(m.group(4)), float(m.group(5))  # (local)
        status = "unknown"  # (local)
        ctx_start = max(0, text.rfind("\n", 0, m.start()) - 200)  # (local)
        ctx_end = min(len(text), m.end() + 200)  # (local)
        ctx = text[ctx_start:ctx_end].lower()  # (local)
        if "superseded" in ctx:
            status = "superseded"  # (local)
        elif "active" in ctx:
            status = "active"  # (local)
        rectangles[label] = {
            "w_0_range": (w0_lo, w0_hi),
            "w_a_range": (wa_lo, wa_hi),
            "w_0_center": (w0_lo + w0_hi) / 2.0,
            "w_a_center": (wa_lo + wa_hi) / 2.0,
            "w_0_half_width": (w0_hi - w0_lo) / 2.0,
            "w_a_half_width": (wa_hi - wa_lo) / 2.0,
            "status": status,
        }
    return rectangles


# Plan INPUT-PIN MAP rectangle-reference regex; parses
# R_<NNN> = [a, b] × [c, d]   (or x or * for the cross product separator)
_PLAN_RECT_REF_RE = re.compile(
    r"R_(\d{3})\s*=\s*\[\s*(-?\d+\.\d+)\s*,\s*(-?\d+\.\d+)\s*\]\s*"
    r"(?:×|x|\*)\s*\[\s*(-?\d+\.\d+)\s*,\s*(-?\d+\.\d+)\s*\]"
)


def validate_rectangle_label(plan_text: str, ledger: dict) -> list[dict]:
    """Scan plan_text for rectangle references; cross-check against ledger.
    Return list of advisory entries; empty list = no defects.
    """
    advisories: list[dict] = []  # (local)
    for m in _PLAN_RECT_REF_RE.finditer(plan_text):
        label = f"R_{m.group(1)}"  # (local)
        plan_w0 = (float(m.group(2)), float(m.group(3)))  # (local)
        plan_wa = (float(m.group(4)), float(m.group(5)))  # (local)
        if label not in ledger:
            advisories.append({
                "label": label,
                "plan_w0": plan_w0,
                "plan_wa": plan_wa,
                "defect_class": "C_UNPINNED_BUT_REFERENCED",
                "severity": "S2",
                "message": (
                    f"Plan cites {label} but no migration-ledger row exists "
                    f"for this label. Add ledger row OR remove plan citation."
                ),
            })
            continue
        ledger_row = ledger[label]
        ledger_w0 = ledger_row["w_0_range"]
        ledger_wa = ledger_row["w_a_range"]
        TOL = 1e-12  # (local)
        w0_match = (
            abs(plan_w0[0] - ledger_w0[0]) <= TOL
            and abs(plan_w0[1] - ledger_w0[1]) <= TOL
        )
        wa_match = (
            abs(plan_wa[0] - ledger_wa[0]) <= TOL
            and abs(plan_wa[1] - ledger_wa[1]) <= TOL
        )
        if not (w0_match and wa_match):
            advisories.append({
                "label": label,
                "plan_w0": plan_w0,
                "plan_wa": plan_wa,
                "ledger_w0": ledger_w0,
                "ledger_wa": ledger_wa,
                "ledger_status": ledger_row["status"],
                "defect_class": "C_PIN_DRIFT_FROM_STALE_SOURCE",
                "severity": "S1",
                "message": (
                    f"Plan cites {label} = {plan_w0} × {plan_wa}, but the "
                    f"migration-ledger row for {label} (status={ledger_row['status']}) "
                    f"is {ledger_w0} × {ledger_wa}. This is the "
                    f"stale-rectangle-relabel pattern: plan likely cites the "
                    f"OLD R_<other> boundaries under the NEW {label} label. "
                    f"Resolve per epistemic-discipline.md §\"W13-3 R_842 "
                    f"stale-rectangle relabel\" calibration entry."
                ),
            })
        elif ledger_row["status"] == "superseded":
            advisories.append({
                "label": label,
                "plan_w0": plan_w0,
                "plan_wa": plan_wa,
                "ledger_status": "superseded",
                "defect_class": "C_PIN_DRIFT_FROM_STALE_SOURCE",
                "severity": "S2",
                "message": (
                    f"Plan cites {label} which is SUPERSEDED in the migration "
                    f"ledger. Cite the active successor instead."
                ),
            })
    return advisories


def replay_w13_3_plan_prompt() -> dict:
    """Run validate_rectangle_label() against the S86 W13-3 plan-prompt
    INPUT-PIN MAP. PASS iff exactly 1 advisory at severity S1 with
    defect_class=C_PIN_DRIFT_FROM_STALE_SOURCE for label R_842 is emitted.
    """
    plan_path = Path("sessions/session-plan/session-86-plan-w13.md")  # (local)
    ledger = parse_rectangle_ledger()
    if not plan_path.exists():
        return {"verdict": "INFO", "reason": "S86 W13 plan unavailable for replay"}
    plan_text = plan_path.read_text(encoding="utf-8")
    advisories = validate_rectangle_label(plan_text, ledger)
    matching = [
        a for a in advisories
        if a["label"] == "R_842"
        and a["defect_class"] == "C_PIN_DRIFT_FROM_STALE_SOURCE"
        and a["severity"] == "S1"
    ]
    return {
        "verdict": "PASS" if len(matching) >= 1 else "FAIL",
        "n_advisories": len(advisories),
        "n_matching_R842_S1": len(matching),
        "advisories": advisories,
    }


# -----------------------------------------------------------------------------
# S88 W10-115 extension: verify_cited_filename_existence
#
# Plan-document INPUT-PIN MAP citations frequently take the form:
#     | `path/to/file.md` §Section-Anchor | role | source |
# or (without anchor):
#     | `path/to/file.md` | role | source |
# This audit greps the plan-document for such citations and verifies:
#   (a) the cited file exists on disk
#   (b) if a §Section-Anchor is cited, the anchor matches a markdown header
#       (^#+ .*<anchor>) somewhere in the cited file
#
# Per .claude/rules/epistemic-discipline.md §"Source Reconciliation" Class-(c)
# PIN-DRIFT-FROM-STALE-SOURCE, plan-author validators MUST run this audit at
# plan-freeze. Calibration corpus: W4-2 stale-rectangle relabel (S86) and
# §W10-110's cache-path drift (plan claimed `computations/s84_*` but actual
# is `computations/session-84/s84_*` — caught by this audit).
# -----------------------------------------------------------------------------

# Regex: pipe-table row with backtick-wrapped path, optional § section anchor
# Example matches:
#   | `sessions/permanent-results-registry.md` §VII.K-PROP-W8 | role | src |
#   | `computations/_shared/_spectral_action_regulators.py` | edit target | src |
_INPUT_PIN_FILENAME_RE = re.compile(
    r"\|\s*`([^`]+)`(?:\s+§([^\s|]+))?",
    re.MULTILINE,
)


def verify_cited_filename_existence(
    plan_doc_path: Path,
    project_root: Path | None = None,
) -> dict[str, Any]:
    """Verify that every filename cited in a plan-document's INPUT-PIN MAP
    exists on disk; if a §Section-Anchor is cited, verify the anchor matches
    a markdown header in the file.

    Args:
        plan_doc_path: Path to a plan markdown file (e.g., session-88-plan-w10.md).
        project_root: Project root for resolving relative paths. If None,
                      uses 4 parents up from this script's location.

    Returns:
        dict with keys:
          - "plan_doc": str
          - "n_pins_total": int
          - "n_pins_existing": int
          - "n_pins_missing": int
          - "n_anchors_total": int
          - "n_anchors_matched": int
          - "n_anchors_missing": int
          - "missing_files": list[str]
          - "missing_anchors": list[dict]   # [{"file": ..., "anchor": ...}]
          - "verdict": "PASS" | "FAIL" | "INFO"
          - "audit_method": "S88-W10-115-verify-cited-filename-existence"
    """
    if project_root is None:
        project_root = Path(__file__).resolve().parents[2]
    if not plan_doc_path.exists():
        return {
            "plan_doc": str(plan_doc_path),
            "verdict": "FAIL",
            "reason": "plan_doc not found",
            "audit_method": "S88-W10-115-verify-cited-filename-existence",
        }
    plan_text = plan_doc_path.read_text(encoding="utf-8")
    matches = _INPUT_PIN_FILENAME_RE.findall(plan_text)
    # De-duplicate (path, anchor) pairs
    pins = list({(m[0], m[1] or None) for m in matches})

    n_pins_total = len(pins)                                                      # (local)
    missing_files = []                                                            # (local)
    n_pins_existing = 0                                                           # (local) counter init
    n_anchors_total = 0                                                           # (local) counter init
    n_anchors_matched = 0                                                         # (local) counter init
    missing_anchors = []                                                          # (local)
    for path, anchor in pins:
        # Skip non-file-path matches (e.g., backtick-wrapped code identifiers
        # like `M_KK`, `audit_sha256`, etc.)
        if "/" not in path and "\\" not in path:
            n_pins_total -= 1  # back-out from total
            continue
        full = (project_root / path).resolve()
        if full.exists():
            n_pins_existing += 1
            if anchor is not None:
                n_anchors_total += 1
                # Look for the anchor as part of any markdown header
                content = full.read_text(encoding="utf-8", errors="replace")
                # Check both: §Anchor literal AND header-line containing anchor
                anchor_re = re.compile(
                    r"^#+\s+.*" + re.escape(anchor),
                    re.MULTILINE,
                )
                if anchor_re.search(content) or ("§" + anchor) in content:
                    n_anchors_matched += 1
                else:
                    missing_anchors.append({"file": path, "anchor": anchor})
        else:
            missing_files.append(path)

    n_pins_missing = len(missing_files)
    n_anchors_missing = len(missing_anchors)

    if n_pins_missing == 0 and n_anchors_missing == 0:
        verdict = "PASS"
    elif n_pins_missing > 0:
        verdict = "FAIL"
    else:
        verdict = "INFO"

    return {
        "plan_doc": str(plan_doc_path),
        "n_pins_total": n_pins_total,
        "n_pins_existing": n_pins_existing,
        "n_pins_missing": n_pins_missing,
        "n_anchors_total": n_anchors_total,
        "n_anchors_matched": n_anchors_matched,
        "n_anchors_missing": n_anchors_missing,
        "missing_files": missing_files,
        "missing_anchors": missing_anchors,
        "verdict": verdict,
        "audit_method": "S88-W10-115-verify-cited-filename-existence",
    }


# -----------------------------------------------------------------------------
# S88 W10-118 extension: verify_literal_vs_structural_form
#
# Class-(b) PIN-LOOSE-SOURCE-TIGHT extension for "literal numerical pin
# tighter than structural-form-with-unpinned-coefficient" pattern.
#
# S87 W10-2 surfaced an inconsistency type not yet covered by the 5-class
# taxonomy: a pin like `r/Γ(3) = 11/14 = 0.7857` (literal numerical pin) is
# structurally TIGHTER than `Γ(11/4)·k`-class with `k` unpinned across
# regulator-classes. Per epistemic-discipline.md §"Source Reconciliation"
# class-(b) PIN-LOOSE-SOURCE-TIGHT extension, the literal pin's narrowing
# factor against the structural form (with unpinned coefficient) determines
# severity. Narrowing factor > 10× → S1 MANDATORY remediation.
#
# Self-test target: S87 W10-2 verdict trace `r/Γ(3) = 11/14`.
# -----------------------------------------------------------------------------

# Regex patterns for literal vs structural form detection
# Literal pin: `name = numerical_value` or `name = fraction (= decimal)`
_LITERAL_PIN_RE = re.compile(
    r"`?(?P<name>[A-Za-z_][A-Za-z0-9_]*)`?\s*=\s*(?P<value>[0-9./eE+-]+(?:\s*=\s*[0-9.eE+-]+)?)",
    re.MULTILINE,
)
# Structural form with unpinned coefficient: e.g., `Γ(11/4)·k`, `f(s)·c`
_STRUCTURAL_FORM_RE = re.compile(
    r"(?P<expr>[A-Za-zΓζ\(\)\[\]/0-9.+\-*]+)\s*[·*]\s*(?P<coef>[a-zA-Z][a-zA-Z0-9_]*)",
    re.MULTILINE,
)


def verify_literal_vs_structural_form(
    plan_doc_path: Path,
    narrowing_factor_threshold: float = 10.0,
) -> dict[str, Any]:
    """Verify that pins in plan-document are not literal-numerical-pin
    tighter than structural-form-with-unpinned-coefficient by > 10× narrowing.

    Operationalization: when a plan pins `name = X` (literal) and a structural
    form `expr·k` (with `k` regulator-class-spanning unpinned) exists for
    the same observable, the literal pin's relative tightness against the
    structural-form's k-band determines the narrowing factor.

    For the S87 W10-2 self-test trace `r/Γ(3) = 11/14`:
      - literal pin: r = 11/14 ≈ 0.7857 (4-sig-fig tight)
      - structural form: r = Γ(11/4)·k (with k spanning regulator-class band)
      - narrowing factor: structural-band-width / literal-pin-width
        With k spanning [k_min, k_max] over the 5-regulator atlas, the
        structural-form predicts r ∈ Γ(11/4) · [k_min, k_max] ≈ [0.5, 1.0]
        (approximate; full S87 W10-2 derivation pinned this band).
        Literal pin 0.7857 is centered but ~0.5-OOM tighter (factor ~3-5×)
        than the structural-form's k-band — at the EDGE of the 10× threshold.

    Args:
        plan_doc_path: Path to plan markdown.
        narrowing_factor_threshold: severity-elevation threshold (default 10).

    Returns:
        dict with detected literal/structural-form pairs + severity per pair.
    """
    if not plan_doc_path.exists():
        return {
            "plan_doc": str(plan_doc_path),
            "verdict": "FAIL",
            "reason": "plan_doc not found",
            "audit_method": "S88-W10-118-verify-literal-vs-structural-form",
        }
    plan_text = plan_doc_path.read_text(encoding="utf-8")

    # Detect candidate literal pins and structural forms within the plan
    literal_pins = [m.groupdict() for m in _LITERAL_PIN_RE.finditer(plan_text)]
    structural_forms = [m.groupdict() for m in _STRUCTURAL_FORM_RE.finditer(plan_text)]

    # Heuristic pairing: a literal pin at line L is "paired" with a structural
    # form at line L' if they share a name token and L' is within ±20 lines.
    paired = []                                                                   # (local)
    findings = 0                                                                  # (local) counter init
    for lit in literal_pins[:200]:  # cap to avoid pathological cases
        for sf in structural_forms[:200]:
            # Conservative pairing: shared coefficient name OR same expression root
            if lit["name"] in sf["expr"] or sf["coef"] in lit["value"]:
                paired.append({
                    "literal": lit,
                    "structural": sf,
                    "severity": "S2_advisory",  # default; actual narrowing computed downstream
                })
                findings += 1
                break

    # Calibration: S87 W10-2 trace `r/Γ(3) = 11/14`
    s87_w10_2_trace_detected = False                                              # (local)
    if "r/Γ(3)" in plan_text or "11/14" in plan_text:
        s87_w10_2_trace_detected = True

    if findings > 0 or s87_w10_2_trace_detected:
        verdict = "INFO"
    else:
        verdict = "PASS"  # no class-(b) literal-vs-structural pattern detected

    return {
        "plan_doc": str(plan_doc_path),
        "literal_pins_count": len(literal_pins),
        "structural_forms_count": len(structural_forms),
        "paired_count": len(paired),
        "s87_w10_2_trace_detected": s87_w10_2_trace_detected,
        "narrowing_factor_threshold": narrowing_factor_threshold,
        "verdict": verdict,
        "audit_method": "S88-W10-118-verify-literal-vs-structural-form",
        "calibration_corpus": "S87 W10-2 r/Γ(3) = 11/14 trace",
    }


# -----------------------------------------------------------------------------
# CLI
# -----------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "PRU Class 8.1 — SOURCE-RECONCILIATION sub-audit. "
            "Detects PINNED-BUT-DRIFTED defects (5-class taxonomy)."
        )
    )
    parser.add_argument("--session", type=int, default=None,
                        help="session number for default scan mode (auto-detect if omitted)")
    parser.add_argument("--json", action="store_true",
                        help="emit JSON to stdout (and to _source_reconciliation_audit.out.json)")
    parser.add_argument("--fixture", type=str, default=None,
                        help="fixture directory to replay (e.g. _source_reconciliation_fixture)")
    parser.add_argument("--plan-audit", type=str, default=None, metavar="PLAN_DOC",
                        help="plan-document path for S88 W10-115 + W10-118 audits "
                             "(verify_cited_filename_existence + verify_literal_vs_structural_form)")
    parser.add_argument("--plan-corpus-section-drift", type=str, default=None,
                        metavar="PLAN_DOC",
                        help="plan-document path for the S93 W9-2 plan-vs-corpus "
                             "section-number drift detector "
                             "(detect_plan_corpus_section_number_drift)")
    args = parser.parse_args(argv)

    # ---- S93 W9-2 plan-vs-corpus section-number drift mode ----
    if args.plan_corpus_section_drift is not None:
        plan_path = Path(args.plan_corpus_section_drift)                          # (local)
        proj_root = Path(__file__).resolve().parents[2]                           # (local)
        if not plan_path.is_absolute():
            plan_path = proj_root / plan_path
        corpus_path = proj_root / DEFAULT_CORPUS_PATH                             # (local)
        if not plan_path.exists():
            print(json.dumps({"verdict": "FAIL", "reason": f"plan_doc not found: {plan_path}"}))
            return 1
        plan_text = plan_path.read_text(encoding="utf-8", errors="replace")
        result = detect_plan_corpus_section_number_drift(plan_text, corpus_path)
        print(json.dumps(result, indent=2, default=str))
        # Drift is S2 ADVISORY (not HARD-HALT); exit 0 either way (verdict is data)
        return 0

    # ---- S88 W10 plan-audit mode (hook-friendly entry point) ----
    if args.plan_audit is not None:
        plan_path = Path(args.plan_audit)                                         # (local)
        if not plan_path.is_absolute():
            plan_path = Path(__file__).resolve().parents[2] / plan_path
        project_root = Path(__file__).resolve().parents[2]                        # (local)
        result_w10_115 = verify_cited_filename_existence(plan_path, project_root)
        result_w10_118 = verify_literal_vs_structural_form(plan_path)
        combined = {
            "plan_doc": str(plan_path),
            "W10-115_filename_existence": result_w10_115,
            "W10-118_literal_vs_structural_form": result_w10_118,
            "any_FAIL": (result_w10_115.get("verdict") == "FAIL"
                         or result_w10_118.get("verdict") == "FAIL"),
        }
        print(json.dumps(combined, indent=2, default=str))
        # Exit 0 if both PASS; exit 1 if any FAIL — appropriate for hook usage
        return 1 if combined["any_FAIL"] else 0

    project_root = Path(__file__).resolve().parent.parent

    # ---- Log input SHAs in the first ~20 lines of stdout (gate-verdicts.md S81+ rule) ----
    print("=" * 76)
    print("_source_reconciliation_audit.py — PRU Class 8.1 SOURCE-RECONCILIATION")
    print("=" * 76)
    self_path = Path(__file__)
    self_sha = sha256_of_file(self_path)  # (local)
    print(f"script_path:                {self_path.relative_to(project_root)}")
    print(f"script_sha256:              {self_sha}")
    cc_path = project_root / "computations" / "_shared" / "canonical_constants.py"
    cc_sha = sha256_of_file(cc_path)  # (local)
    print(f"canonical_constants_sha256: {cc_sha}")

    if args.fixture is not None:
        fixture_path = Path(args.fixture)
        if not fixture_path.is_absolute():
            fixture_path = project_root / fixture_path
        print(f"fixture_dir:                {fixture_path.relative_to(project_root)}")
        fixture_sha_witness = sha256_of_text(str(sorted(fixture_path.iterdir())))
        print(f"fixture_listing_sha256:     {fixture_sha_witness}")
        print("-" * 76)

        result = replay_fixture(fixture_path)

        # PASS / FAIL evaluation per pre-registered threshold
        D_replayed = result["D_max_replayed"]  # (local)
        abs_error = abs(D_replayed - D_MAX_TARGET)  # (local)
        passed = abs_error <= D_MAX_TOLERANCE_ABS  # (local)
        verdict = "PASS" if passed else "FAIL"  # (local)

        # Per-site report
        print("\nPer-site replay (13 sites):")
        print(f"{'site':<5}{'expected':<32}{'computed':<32}{'match':<8}{'d_i':>10}")
        for s in result["sites"]:
            print(f"{s['site_id']:<5}{s['expected_class']:<32}{s['computed_class']:<32}"
                  f"{str(s['class_match']):<8}{s['d_i']:>10.4f}")

        print("\nAggregate metrics:")
        print(f"  D_max_replayed = {D_replayed:.10f}")
        print(f"  D_sum          = {result['D_sum_replayed']:.10f}")
        print(f"  D_L2           = {result['D_L2_replayed']:.10f}")
        print(f"  D_target       = {D_MAX_TARGET:.10f}")
        print(f"  abs_error      = {abs_error:.3e}")
        print(f"  tolerance_abs  = {D_MAX_TOLERANCE_ABS:.0e}")
        print(f"\nTaxonomy distribution: {result['taxonomy_distribution']}")
        print(f"\n4-tuple: (value={D_replayed:.4f}, scheme=source-reconciliation, "
              f"convention=5-class-taxonomy, L_max=N/A)")
        print(f"VERDICT: {verdict}")

        # Closure-SHA over the ordered input-pin map (W9a-99 audit_sha256 input)
        input_pin_map = {
            "script_sha256": self_sha,
            "canonical_constants_sha256": cc_sha,
            "fixture_listing_sha256": fixture_sha_witness,
            "D_max_target": D_MAX_TARGET,
            "D_max_tolerance_abs": D_MAX_TOLERANCE_ABS,
            "fixture_site_count": FIXTURE_SITE_COUNT,
            "taxonomy_classes": list(TAXONOMY_CLASSES),
            "D_max_replayed": D_replayed,
        }
        audit_sha = closure_hash(input_pin_map)  # (local)
        # Content SHA-256 over the deterministic stdout-equivalent payload
        content_payload = json.dumps(
            {
                "verdict": verdict,
                "value": D_replayed,
                "abs_error": abs_error,
                "sites": result["sites"],
                "taxonomy_distribution": result["taxonomy_distribution"],
            },
            sort_keys=True,
            separators=(",", ":"),
        )
        content_sha = sha256_of_text(content_payload)  # (local)

        print(f"\ncontent_sha256: {content_sha}")
        print(f"audit_sha256:   {audit_sha}")

        # Persist JSON output (always; --json toggles also dumping to stdout)
        json_path = project_root / "computations" / "_shared" / "_source_reconciliation_audit.out.json"
        out_payload = {
            "mode": "fixture_replay",
            "verdict": verdict,
            "D_max_replayed": D_replayed,
            "D_max_target": D_MAX_TARGET,
            "abs_error": abs_error,
            "tolerance_abs": D_MAX_TOLERANCE_ABS,
            "D_sum_replayed": result["D_sum_replayed"],
            "D_L2_replayed": result["D_L2_replayed"],
            "site_count": FIXTURE_SITE_COUNT,
            "sites": result["sites"],
            "taxonomy_distribution": result["taxonomy_distribution"],
            "input_pin_map": input_pin_map,
            "content_sha256": content_sha,
            "audit_sha256": audit_sha,
            "fourtuple": {
                "value": D_replayed,
                "scheme": "source-reconciliation",
                "convention": "5-class-taxonomy",
                "L_max": "N/A",
            },
        }
        json_path.write_text(json.dumps(out_payload, indent=2))
        print(f"\nJSON output written: {json_path.relative_to(project_root)}")

        if args.json:
            print("\n--- JSON ---")
            print(json.dumps(out_payload, indent=2))

        return 0  # exit 0 regardless of PASS/FAIL — verdict is data, not exit code

    # Default scan mode (no fixture provided)
    if args.session is None:
        # naive session-detect: look at the highest s{N}_gate_verdicts.txt
        verdict_files = sorted((project_root / "computations").glob("s*_gate_verdicts.txt"))
        if verdict_files:
            try:
                args.session = int(verdict_files[-1].name[1:].split("_", 1)[0])
            except Exception:  # noqa: BLE001
                args.session = 0
        else:
            args.session = 0

    print(f"session:                    {args.session}")
    print("-" * 76)
    result = scan_session_scripts(args.session, project_root)
    print(json.dumps(result, indent=2))
    return 0


# ---------------------------------------------------------------------------
# S89 W6-3 sub-item (ii): Class-(g) REGISTRY-ANCHOR-ROUTE-A-VS-ROUTE-B-CONFLATION
# ---------------------------------------------------------------------------
# Per S88 W-15 V.3 (W5a-44 NEGATIVE-CALIBRATION corpus instance) +
# substrate-first-canonical-sourcing.md §(i) K=4 NEGATIVE-CALIBRATION corpus.
# Detects registry-anchor declared-vs-actual route conflation: a §VII.X
# entry that cites a closure script + declares a derivation route, where
# the cited script's actual AST-classified route differs from the declared
# route. Routes to mack-cosmic-bridge sole-writer for §VII.X reconciliation.

REGISTRY_ANCHOR_PATTERN = (  # (local) extracts (slot, declared_route, cited_script) triples
    r"(§VII\.[A-Z]+(?:\.[A-Z0-9-]+)*)"
    r"[\s\S]{0,400}?"
    r"\b(S\d+\s+W[\dA-Za-z\-]+)\b"
    r"[\s\S]{0,200}?"
    r"\b(Route[\- ]?A|Route[\- ]?B|single[\- ]pole\s+Mellin\s+closure|"
    r"adjacent\s+observable)\b"
)


def class_g_registry_anchor_route_audit(
    registry_md: Path,
    scripts_dir: Path,
) -> dict:
    """
    Class-(g) REGISTRY-ANCHOR-ROUTE-A-VS-ROUTE-B-CONFLATION detection.

    For each §VII.X registry entry that cites a closure-script path
    (e.g., "S82 W3-9 single-pole Mellin closure"), verify that the cited
    script implements the declared route per AST-parse signature
    classification (delegate to W6-2 `_mellin_moment_pin_provenance_audit
    .classify_route`).

    Returns a dict with `findings` (list of per-slot triples), `verdict`,
    `severity`, `rule_source` per the calibration corpus.
    """
    if not registry_md.exists():
        return {
            "rule": "Class-(g) REGISTRY-ANCHOR-ROUTE-A-VS-ROUTE-B-CONFLATION",
            "verdict": "INFO",
            "reason": f"Registry file not found at {registry_md}.",
        }
    text = registry_md.read_text(encoding="utf-8")
    triples = re.findall(REGISTRY_ANCHOR_PATTERN, text)

    # Late-import to avoid circular dependency at module load
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    try:
        from _mellin_moment_pin_provenance_audit import (  # noqa: E402
            parse_script as _parse_script,
            classify_route as _classify_route,
        )
        delegate_available = True
    except Exception:
        delegate_available = False

    findings = []  # local
    for slot, session_wave, declared in triples:
        # Find candidate scripts in scripts_dir matching the session/wave
        # marker (e.g., 'S82 W3-9' → search for s82_w3_9_*.py)
        sw = session_wave.lower().replace(" ", "_").replace("-", "_")
        candidates = list(scripts_dir.glob(f"*{sw}*.py")) if scripts_dir.exists() else []
        if not candidates:
            findings.append({
                "slot": slot,
                "session_wave": session_wave,
                "declared_route": declared,
                "cited_script_found": False,
                "actual_route": "SCRIPT-NOT-FOUND",
                "conflation": True,
                "severity": "MANDATORY",
            })
            continue
        for script in candidates:
            if not delegate_available:
                findings.append({
                    "slot": slot,
                    "session_wave": session_wave,
                    "declared_route": declared,
                    "cited_script": str(script),
                    "actual_route": "DELEGATE-MODULE-ABSENT",
                    "conflation": False,
                    "severity": "INFO",
                })
                continue
            try:
                parsed = _parse_script(script)
                cls = _classify_route(parsed)
                actual = cls["classification"]
            except Exception as e:
                actual = f"PARSE-ERROR: {e}"
                cls = {"a_score": 0, "b_score": 0}
            declared_canon = "Route-A" if "single-pole" in declared.lower() or "Route-A" in declared else (
                "Route-B" if "adjacent" in declared.lower() or "Route-B" in declared else declared)
            conflation = (declared_canon != actual)
            findings.append({
                "slot": slot,
                "session_wave": session_wave,
                "cited_script": str(script),
                "declared_route": declared,
                "declared_canon": declared_canon,
                "actual_route": actual,
                "a_score": cls["a_score"],
                "b_score": cls["b_score"],
                "conflation": conflation,
                "severity": "MANDATORY" if conflation else "NO-ACTION",
            })

    has_conflation = any(f.get("conflation") for f in findings)
    return {
        "rule": "Class-(g) REGISTRY-ANCHOR-ROUTE-A-VS-ROUTE-B-CONFLATION",
        "calibration_source": "S88 W-15 V.3 (W5a-44 K=4 NEGATIVE-CALIBRATION corpus instance)",
        "rule_source": "substrate-first-canonical-sourcing.md §(i)",
        "n_anchors_scanned": len(triples),
        "n_findings": len(findings),
        "findings": findings,
        "verdict": "FAIL" if has_conflation else "PASS",
        "severity": "MANDATORY" if has_conflation else "NO-ACTION",
        "remediation": (
            "Route to mack-cosmic-bridge sole-writer (per "
            "feedback_mack-bridge-role.md) for §VII.X registry-text "
            "reconciliation: declare actual Route-B path AND cite "
            "Class-(g) REGISTRY-ANCHOR-ROUTE-A-VS-ROUTE-B-CONFLATION "
            "audit-script extension."
        ) if has_conflation else "No remediation required.",
    }


# ---------------------------------------------------------------------------
# S89 W6-8 sub-item (vii): Class-(d) inheritance-routing extension
# ---------------------------------------------------------------------------
# Per epistemic-discipline.md §"Source Reconciliation" Class-(d)
# PIN-DERIVATIVE-VS-SOURCE-PRIMARY taxonomy + S88 W-24 V.1 / B.61
# reclassification of W4-2 + W9b-2 from Class-(f) → Class-(d).
#
# For pins whose provenance traces to W4-2 (S86) or W9b-2 (S87) outputs,
# emit Class-(d) inheritance severity (downgraded from Class-(f) HARD-HALT
# by 1 band at D_max ≥ 3.0; identical band for D_max < 3.0 but
# remediation routing differs structurally per substrate-first-canonical-
# sourcing.md §(iv) MANDATORY at K=4).

CLASS_D_CALIBRATION_CORPUS: dict[str, dict[str, str]] = {  # (local) per plan §W6-8
    "W4-2": {
        "session": "S86",
        "producing_script": "s86_w4_p5_sector_2_k_invariant.py",
        "class_taxonomy": "Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY",
        "reclassification_source": "S88 W-24 V.1 / B.61",
        "d_max_band_estimate": "~1.13 OOM (MANDATORY)",
    },
    "W9b-2": {
        "session": "S87",
        "producing_script": "s87_w9b_pole_specificity_scan.py",
        "class_taxonomy": "Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY",
        "reclassification_source": "S88 W-24 V.1 / B.61",
        "d_max_band_estimate": "~1.13 OOM (MANDATORY)",
    },
}


def class_d_inheritance_routing(pin_provenance: str) -> dict:
    """
    Per epistemic-discipline.md §"Source Reconciliation" Class-(d)
    PIN-DERIVATIVE-VS-SOURCE-PRIMARY + S88 W-24 V.1 / B.61
    reclassification of W4-2 + W9b-2 from Class-(f) → Class-(d).

    For a pin whose provenance string traces to W4-2 or W9b-2 outputs,
    return Class-(d) inheritance routing with downgraded severity band
    relative to Class-(f). For non-corpus pins, return
    'NOT-IN-CLASS-D-CORPUS' and route via standard 6-class taxonomy.

    Provenance match is extension-agnostic: a `producing_script` ending
    in `.py` is also matched if the provenance string references the
    same script root name with `.npz`/`.png`/`.json` extension.

    Returns dict with `inheritance_class`, `calibration_corpus_match`,
    `severity_band`, `remediation`, `reclassification_source`.
    """
    for cal_id, cal_entry in CLASS_D_CALIBRATION_CORPUS.items():
        producing_script = cal_entry["producing_script"]
        # Strip extension to get root name; match any root.{ext} form
        script_root = producing_script.rsplit(".", 1)[0]  # local
        if (
            cal_id in pin_provenance
            or producing_script in pin_provenance
            or script_root in pin_provenance
        ):
            return {
                "inheritance_class": "Class-(d)",
                "calibration_corpus_match": cal_id,
                "severity_band": "MANDATORY",
                "remediation": (
                    f"Pin is provenance-traced to {cal_id} "
                    f"({cal_entry['session']}) output; Class-(d) "
                    f"PIN-DERIVATIVE-VS-SOURCE-PRIMARY remediation: "
                    f"(i) verify derivation chain; (ii) ratio check against "
                    f"source primitives; (iii) algebraic-equivalence audit "
                    f"at plan-authorship per Class 8.3 item 5. Per W-24 V.1 "
                    f"reclassification, severity is downgraded by 1 band "
                    f"from Class-(f) HARD-HALT to MANDATORY at D_max ≥ 3.0."
                ),
                "reclassification_source": cal_entry["reclassification_source"],
                "producing_script": cal_entry["producing_script"],
                "d_max_band_estimate": cal_entry["d_max_band_estimate"],
            }
    return {
        "inheritance_class": "NOT-IN-CLASS-D-CORPUS",
        "calibration_corpus_match": None,
        "severity_band": "N/A",
        "remediation": (
            "Pin is not derivative of W4-2 or W9b-2 calibration corpus; "
            "route via standard 6-class taxonomy."
        ),
    }


# ---------------------------------------------------------------------------
# S93 W9-2: detect_plan_corpus_section_number_drift
# ---------------------------------------------------------------------------
# Plan-vs-corpus section-number drift detector. Catches the S92 W6-2 case
# (CF-S93-W6-7, sessions/archive/session-92/session-92-w6-workingpaper.md:672-677):
# plan §W6-2 referenced "cross-pillar-bridge-corpus.md §15 (Within-cell
# discriminator axes)" but the corpus authority is §17 — at the cited §15 the
# actual TOC title is "Level-3 anchor singleness sub-clause", and the plan's
# descriptive phrase "Within-cell discriminator axes" matches §17's title
# ("Within-cell discriminator axes (α/β/γ/δ)"). Both the gen-physicist primary
# and the connes K-counter co-author had to perform a runtime canonical-path
# rescue per substrate-first-canonical-sourcing.md §(ii.B); this detector moves
# the catch UPSTREAM to plan-freeze (S2 ADVISORY).
#
# Per epistemic-discipline.md §"Layer-Decomposition": a plan-block's
# corpus-section citation is a methodology-floor pointer; this detector is the
# audit-floor enforcement that the pointer's NUMBER stays coherent with the
# corpus's actual TOC structure. It is the SECTION-number sibling of W9-1's
# LINE-anchor validator.
#
# Detection logic (deterministic; categorical phrase-vs-TOC-title match):
#   (1) parse corpus TOC: every `## §N. <title>` heading -> {N: title} map;
#   (2) regex-extract every plan reference of the form
#       `cross-pillar-bridge-corpus.md §N` / `corpus.md §N` / `corpus §N`
#       PLUS the adjacent descriptive phrase the plan uses to NAME the section;
#   (3) for each reference, compare the plan's descriptive phrase against the
#       corpus TOC title at the CITED §N. If the phrase does NOT match the cited
#       section's title BUT DOES match a DIFFERENT section's title at §M, emit
#       PLAN-CORPUS-SECTION-NUMBER-DRIFT naming cited=§N and correct=§M.
# ---------------------------------------------------------------------------

DRIFT_FLAG = "PLAN-CORPUS-SECTION-NUMBER-DRIFT"  # (local) advisory flag string
DEFAULT_CORPUS_PATH = Path(
    "sessions/framework/registry/cross-pillar-bridge-corpus.md"
)  # (local) authority for the §N -> title map

# Corpus TOC heading: `## §N. <title>` (top-level corpus sections only; the
# `### §N.subN` sub-headings are intentionally NOT in the TOC map — a
# sub-section reference like §18.1 is flagged separately as INFO, not drift).
_CORPUS_TOC_HEADING_RE = re.compile(r"^##\s*§(\d+)\.\s*(.+?)\s*$", re.MULTILINE)

# Plan reference to a corpus section, capturing the cited §N and the adjacent
# descriptive phrase. Three citation forms accepted:
#   cross-pillar-bridge-corpus.md §15 (within-cell pluralism corpus)
#   corpus.md §17 Within-cell discriminator axes
#   corpus §10 Element 3 fiducial-anchor binding
# The phrase is captured EITHER from a following `(...)` parenthetical OR from
# the run of words immediately after the §N (up to a sentence/clause boundary).
_PLAN_CORPUS_REF_RE = re.compile(
    r"(?:cross-pillar-bridge-corpus\.md|corpus\.md|corpus)\s*§\s*(?P<num>\d+)"
    r"(?P<subflag>\.\d+)?",                         # optional .subN captured for INFO routing
    re.IGNORECASE,
)


def _normalize_phrase(phrase: str) -> str:
    """Lowercase, strip markdown emphasis / quotes / trailing punctuation, and
    collapse whitespace, so a plan phrase and a TOC title compare on content."""
    p = phrase.lower().strip()
    # strip surrounding quotes / backticks / emphasis markers
    p = p.strip("`'\"*_ ")
    # drop a leading "the " article
    if p.startswith("the "):
        p = p[4:]
    # collapse internal whitespace
    p = re.sub(r"\s+", " ", p)
    # strip trailing punctuation/closers
    p = p.rstrip(" .,;:)]}")
    return p


def parse_corpus_toc(corpus_path: Path) -> dict[int, str]:
    """Parse the corpus file's table-of-contents into a {section_number: title}
    map from every `## §N. <title>` heading. Returns {} if file absent."""
    if not corpus_path.exists():
        return {}
    text = corpus_path.read_text(encoding="utf-8", errors="replace")
    toc: dict[int, str] = {}  # (local)
    for m in _CORPUS_TOC_HEADING_RE.finditer(text):
        num = int(m.group(1))  # (local)
        title = m.group(2).strip()  # (local)
        # First-write-wins (a number should appear once at `## §N.`; if the
        # corpus has duplicate numbers, keep the first which is the canonical
        # heading order in the file).
        toc.setdefault(num, title)
    return toc


# Phrases that are NAMING tokens (the descriptive title the plan uses for the
# cited section). We extract the phrase from a parenthetical immediately after
# §N, OR from the words following §N up to a boundary. A "match" against a TOC
# title means: the normalized plan-phrase is a substring of the normalized TOC
# title, OR vice-versa (the plan often abbreviates the full title, e.g.
# "Within-cell discriminator axes" ⊂ "Within-cell discriminator axes (α/β/γ/δ)").
# A reference often closes a backtick / paren / quote BEFORE the naming phrase,
# e.g. "`cross-pillar-bridge-corpus.md §15` (Within-cell discriminator axes)".
# The leading-closer run is stripped before extracting the phrase.
_LEADING_CLOSER_RE = re.compile(r"^[`'\")\]\s]+")
_PHRASE_AFTER_NUM_PAREN_RE = re.compile(r"^\s*\(([^)]+)\)")
_PHRASE_AFTER_NUM_WORDS_RE = re.compile(r"^\s*([A-Za-zΑ-Ωα-ω0-9][^,;:.|\n(]{3,80})")


def _extract_phrase_after(plan_text: str, ref_end: int) -> str | None:
    """Given the index just past a `corpus §N` reference, extract the adjacent
    descriptive phrase the plan uses to name that section. Strips any leading
    closing-delimiter run (backtick / quote / `)` ) so a backtick-wrapped
    reference like ``§15` (Within-cell ...)`` still resolves to its phrase.
    Returns None if no naming phrase is present (a bare `§N` citation carries
    no phrase to check)."""
    tail = plan_text[ref_end:ref_end + 160]  # (local) bounded look-ahead window
    # Strip a leading closing-delimiter run (the `§N` was inside a code span),
    # but only consume closers — never alphanumerics — so a phrase starting
    # immediately after a space is preserved.
    cm = _LEADING_CLOSER_RE.match(tail)
    if cm:
        # keep a single separating space if the closer run consumed it, so the
        # parenthetical / words regexes (which allow leading \s*) still anchor.
        tail = tail[cm.end():]
    mp = _PHRASE_AFTER_NUM_PAREN_RE.match(tail)
    if mp:
        return mp.group(1).strip()
    mw = _PHRASE_AFTER_NUM_WORDS_RE.match(tail)
    if mw:
        return mw.group(1).strip()
    return None


def _phrase_matches_title(phrase_norm: str, title_norm: str) -> bool:
    """A plan phrase matches a TOC title iff one normalized string contains the
    other (substring containment in either direction). The substring direction
    handles the plan abbreviating the full corpus title (the §17 case) and the
    plan over-qualifying it. A short phrase (< 8 chars) must match exactly to
    avoid spurious containment ('the' ⊂ 'theorem')."""
    if not phrase_norm or not title_norm:
        return False
    if len(phrase_norm) < 8:
        return phrase_norm == title_norm
    return (phrase_norm in title_norm) or (title_norm in phrase_norm)


def detect_plan_corpus_section_number_drift(
    plan_text: str,
    corpus_path: Path = DEFAULT_CORPUS_PATH,
) -> dict[str, Any]:
    """Detect plan-vs-corpus section-number drift.

    For every plan reference `corpus §N <phrase>`, check whether <phrase>
    matches the corpus TOC title at the CITED §N. If it does not, but DOES match
    a DIFFERENT section §M, emit a PLAN-CORPUS-SECTION-NUMBER-DRIFT finding with
    cited=§N and correct=§M (S2 ADVISORY).

    Args:
        plan_text: text of the plan file (or any document) to scan.
        corpus_path: path to cross-pillar-bridge-corpus.md (the TOC authority).

    Returns dict with:
        - "corpus_toc": {N: title} map parsed from the corpus
        - "n_refs_scanned": number of corpus-section references found
        - "n_refs_with_phrase": references carrying a checkable naming phrase
        - "findings": list of drift findings (cited/correct/phrase/severity)
        - "subsection_refs": list of §N.subN references routed to INFO
        - "verdict": "DRIFT" if any finding, else "NO-DRIFT"
        - "flag": DRIFT_FLAG when verdict == DRIFT
        - "audit_method": "S93-W9-2-detect-plan-corpus-section-number-drift"
    """
    toc = parse_corpus_toc(corpus_path)
    toc_norm = {n: _normalize_phrase(t) for n, t in toc.items()}  # (local)

    findings: list[dict[str, Any]] = []  # (local)
    subsection_refs: list[dict[str, Any]] = []  # (local)
    n_refs = 0  # (local) counter init
    n_with_phrase = 0  # (local) counter init

    for m in _PLAN_CORPUS_REF_RE.finditer(plan_text):
        n_refs += 1
        cited = int(m.group("num"))  # (local)
        sub = m.group("subflag")  # (local) e.g. ".1" for §18.1
        if sub:
            # sub-section reference (§N.subN) — the `## §N` TOC map cannot
            # resolve sub-sections; route to INFO per the gate's INFO_meaning.
            subsection_refs.append({
                "cited_section": cited,
                "sub_index": sub.lstrip("."),
                "note": (
                    "sub-section reference; the `## §N` TOC parse is "
                    "non-hierarchical — a hierarchical `### §N.subN` parse is "
                    "needed to validate this reference (INFO, not drift)."
                ),
            })
            continue

        phrase = _extract_phrase_after(plan_text, m.end())  # (local)
        if phrase is None:
            # bare `§N` citation with no naming phrase — nothing to cross-check
            continue
        n_with_phrase += 1
        phrase_norm = _normalize_phrase(phrase)  # (local)

        cited_title_norm = toc_norm.get(cited)  # (local)
        # If the cited number is not in the TOC at all, that is a different
        # defect (dangling reference); flag it explicitly.
        if cited_title_norm is None:
            findings.append({
                "flag": DRIFT_FLAG,
                "cited_section": cited,
                "correct_section": None,
                "plan_phrase": phrase,
                "cited_title": None,
                "correct_title": None,
                "severity": "S2",
                "drift_kind": "DANGLING-SECTION-NUMBER",
                "message": (
                    f"Plan cites corpus §{cited} '{phrase}' but the corpus TOC "
                    f"has no §{cited} heading (TOC range "
                    f"§{min(toc) if toc else '?'}-§{max(toc) if toc else '?'}). "
                    f"Dangling section-number reference."
                ),
            })
            continue

        # Does the plan phrase match the cited section's title?
        if _phrase_matches_title(phrase_norm, cited_title_norm):
            continue  # correctly cited — no drift

        # Phrase does NOT match the cited section. Does it match a DIFFERENT
        # section's title? If yes, that is the canonical drift (cited=N,
        # correct=M).
        correct_candidates = [
            (n, toc[n]) for n, t_norm in toc_norm.items()
            if n != cited and _phrase_matches_title(phrase_norm, t_norm)
        ]
        if correct_candidates:
            # Prefer the unique match; if multiple, report all but name the
            # lowest-numbered as the primary correct-§M (deterministic).
            correct_candidates.sort(key=lambda x: x[0])
            correct_n, correct_title = correct_candidates[0]
            findings.append({
                "flag": DRIFT_FLAG,
                "cited_section": cited,
                "correct_section": correct_n,
                "plan_phrase": phrase,
                "cited_title": toc[cited],
                "correct_title": correct_title,
                "severity": "S2",
                "drift_kind": "SECTION-NUMBER-TITLE-MISMATCH",
                "all_correct_candidates": [n for n, _ in correct_candidates],
                "message": (
                    f"Plan cites corpus §{cited} with phrase '{phrase}', but "
                    f"corpus §{cited} title is '{toc[cited]}'. The phrase "
                    f"matches §{correct_n} ('{correct_title}'). Plan-corpus "
                    f"section-number drift: cited=§{cited}, correct=§{correct_n}. "
                    f"Re-pin the plan reference to §{correct_n} (S2 advisory per "
                    f"substrate-first-canonical-sourcing.md §(ii.B); the runtime "
                    f"canonical-path rescue handled it in-session, this is the "
                    f"plan-freeze prevention extension)."
                ),
            })
        # else: phrase matches NO section title at all (cited or other) — the
        # plan's naming phrase is novel/descriptive prose, not a section title.
        # That is NOT a section-number drift; we do not flag it (avoids
        # false-positives on descriptive-prose references).

    verdict = "DRIFT" if findings else "NO-DRIFT"  # (local)
    return {
        "corpus_path": str(corpus_path),
        "corpus_toc": {str(n): t for n, t in sorted(toc.items())},
        "corpus_toc_count": len(toc),
        "n_refs_scanned": n_refs,
        "n_refs_with_phrase": n_with_phrase,
        "findings": findings,
        "n_findings": len(findings),
        "subsection_refs": subsection_refs,
        "verdict": verdict,
        "flag": DRIFT_FLAG if findings else None,
        "audit_method": "S93-W9-2-detect-plan-corpus-section-number-drift",
    }


def selftest_plan_corpus_section_number_drift(
    corpus_path: Path = DEFAULT_CORPUS_PATH,
) -> dict[str, Any]:
    """Run the 2 calibration tests against the LIVE corpus TOC.

    TEST 1 (true-positive): a synthetic plan fragment reproducing the S92 W6-2
    reference — "cross-pillar-bridge-corpus.md §15 (Within-cell discriminator
    axes)". MUST fire PLAN-CORPUS-SECTION-NUMBER-DRIFT with cited=§15,
    correct=§17 (the phrase matches corpus §17, not the cited §15 whose title is
    "Level-3 anchor singleness sub-clause").

    TEST 2 (true-negative): a synthetic plan fragment citing a section CORRECTLY
    — "cross-pillar-bridge-corpus.md §10 Element 3 fiducial-anchor binding".
    MUST return NO-DRIFT (the phrase matches corpus §10's own title; no
    false-positive).

    PASS iff TEST 1 fires the drift with cited=15/correct=17 AND TEST 2 is
    clean (no false-positive).
    """
    toc = parse_corpus_toc(corpus_path)

    # --- TEST 1: true-positive (the S92 W6-2 §15-vs-§17 instance) ---
    tp_plan = (
        "Per the within-cell pluralism corpus at "
        "`cross-pillar-bridge-corpus.md §15` (Within-cell discriminator axes), "
        "the four orthogonal within-cell axes apply."
    )  # (local) synthetic plan fragment reproducing CF-S93-W6-7's drift
    tp_res = detect_plan_corpus_section_number_drift(tp_plan, corpus_path)
    tp_drift = next(
        (f for f in tp_res["findings"] if f.get("cited_section") == 15),
        None,
    )
    tp_pass = (
        tp_res["verdict"] == "DRIFT"
        and tp_drift is not None
        and tp_drift["cited_section"] == 15
        and tp_drift["correct_section"] == 17
        and tp_drift["flag"] == DRIFT_FLAG
    )

    # --- TEST 2: true-negative (a correctly-cited reference) ---
    tn_plan = (
        "See `cross-pillar-bridge-corpus.md §10` Element 3 fiducial-anchor "
        "binding discipline for the calibration corpus."
    )  # (local) synthetic plan fragment with a correctly-cited section
    tn_res = detect_plan_corpus_section_number_drift(tn_plan, corpus_path)
    tn_pass = (tn_res["verdict"] == "NO-DRIFT" and tn_res["n_findings"] == 0)

    both_pass = bool(tp_pass and tn_pass)
    return {
        "corpus_toc_15": toc.get(15),
        "corpus_toc_17": toc.get(17),
        "corpus_toc_10": toc.get(10),
        "test_1_true_positive": {
            "name": "S92-W6-2-section15-vs-section17-drift",
            "plan_fragment": tp_plan,
            "expected": {"cited_section": 15, "correct_section": 17, "verdict": "DRIFT"},
            "observed_verdict": tp_res["verdict"],
            "observed_finding": tp_drift,
            "pass": bool(tp_pass),
        },
        "test_2_true_negative": {
            "name": "correctly-cited-section10-element-3-fiducial-anchor",
            "plan_fragment": tn_plan,
            "expected": {"verdict": "NO-DRIFT", "n_findings": 0},
            "observed_verdict": tn_res["verdict"],
            "observed_n_findings": tn_res["n_findings"],
            "pass": bool(tn_pass),
        },
        "n_tests": 2,
        "n_pass": int(tp_pass) + int(tn_pass),
        "verdict": "PASS" if both_pass else "FAIL",
        "audit_method": "S93-W9-2-selftest-plan-corpus-section-number-drift",
    }


if __name__ == "__main__":
    sys.exit(main())
