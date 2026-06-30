#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S88 W7a-71 — S88-CROSS-AXIS-STAGE-2-VERIFY-CORNER-PINNED
=========================================================

Gate: S88-CROSS-AXIS-STAGE-2-VERIFY-CORNER-PINNED ([VERIFY-THEOREM])

Pre-registered threshold (per session-88-plan-w7a.md §W7a-71 §74-77):
  PASS iff
    (1) all 4 single-axis clause verdicts (a, b, e, f) PASS, AND
    (2) joint clauses (c) and (d) PASS independently in ALL FOUR
        (axis × corner) combinations:
          (corner_I × axis_A_connes) ∧ (corner_III × axis_A_connes) ∧
          (corner_I × axis_B_volovik) ∧ (corner_III × axis_B_volovik).
  FAIL iff any clause returns FAIL.
  INFO iff any clause returns INFO without any FAIL.
  rel_tol = 1e-9 (presentation-precision-tolerant default; verdicts are
  categorical PASS/FAIL/INFO from cross-reviewer auditors, not numerical).

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - computations/session-88/s88_w7a_71_connes_verdict.json (Axis-A reviewer)
  - computations/session-88/s88_w7a_71_volovik_verdict.json (Axis-B reviewer)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<verdict_str>, scheme=zeta-spectral-action,
   convention=substrate-distance-1-corner-pinned, L_max=12)

Classification: GEOMETRIC (substrate-IS spectral-triple observable identity
at corner-cell granularity) + PHONONIC (joint clauses concern phononic
GGE-class observables on Path-(c)).

METHODOLOGY
-----------
Stage-2 two-axis independent-verify per `joint-theorem-promotion.md §"Stage 2
details"`, RE-SCOPED under W7a-71 corner-pinning. This script is a CONSUMER:
it does not perform substrate physics — it consumes structured verdict JSONs
emitted by two parallel cross-reviewer subagents (connes-ncg-theorist Axis-A;
volovik-superfluid-universe-theorist Axis-B) dispatched from the orchestrator
under user-authorized hybrid /rclab-solo path. Each subagent audits its
canonical clauses (connes: a, c-JOINT, d-JOINT, e; volovik: b, c-JOINT,
d-JOINT, f) at corner I + corner III separately, with explicit context-
isolation (no W-9 R1/R2/R3 transcripts; no §W9a-1 plan-block; no §W7a-71
plan-block). This script applies the PASS-AND threshold logic over the 4
joint-clause (axis × corner) verdicts and the 4 single-axis clause verdicts,
collapses to a composite PASS/FAIL/INFO per the pre-registered rule, and
appends the canonical dual-SHA verdict line.

DISCIPLINE
----------
- `from canonical_constants import *` (canonical_constants.py is bytes-pinned
  in audit_sha256; constants not actively used in this consumer-style script).
- All intermediates tagged `# (local)`.
- No GPU; no heavy linear algebra (this is a verdict-aggregator, not a
  spectral compute).
- Dual-SHA over (script || canonical || pinmap_json) per S84+.
- Reads the §VII.AH text from permanent-results-registry.md to bind the
  registered text into the audit pin map (so the audit_sha256 commits to
  the exact theorem text the subagents audited).

INPUT-PIN MAP (closure_hash → audit_sha256):
- connes_verdict_json_sha
- volovik_verdict_json_sha
- canonical_constants_sha
- permanent_results_registry_sha
- script_bytes_sha

Author: lizzi-spectral-functional-theorist (orchestrator-direct under
user-authorized hybrid solo dispatch; cross-reviewers run as subagents).
Session: 88, Wave: W7a, Plan: session-88-plan-w7a.md §W7a-71
Date: 2026-05-05
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys as _sys
from pathlib import Path as _Path

# Add SHARED_DIR to path so canonical_constants imports cleanly
_THIS_FILE = _Path(__file__).resolve()  # (local)
_SHARED_DIR = _THIS_FILE.parent.parent / "_shared"  # (local)
if str(_SHARED_DIR) not in _sys.path:
    _sys.path.insert(0, str(_SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from pathlib import Path

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S88"                                                    # (local)
GATE_ID = "S88-CROSS-AXIS-STAGE-2-VERIFY-CORNER-PINNED"            # (local)
SCHEME = "zeta-spectral-action"                                    # (local)
CONVENTION = "substrate-distance-1-corner-pinned"                  # (local)
L_MAX = 12                                                         # (local)

# Pre-registered threshold: rel_tol=1e-9 default per plan §W7a-71 §79
# (presentation-precision-tolerant). Verdicts here are categorical
# PASS/FAIL/INFO from auditor JSONs; rel_tol applies if any auditor
# returns a numerical sub-verdict requiring tolerance comparison.
REL_TOL = 1e-9                                                     # (local)

# Cross-reviewer JSON inputs
CONNES_JSON = SESSION_DIR / "s88_w7a_71_connes_verdict.json"       # (local)
VOLOVIK_JSON = SESSION_DIR / "s88_w7a_71_volovik_verdict.json"     # (local)

# §VII.AH theorem text source (read for pin-map but NOT modified)
PERM_REGISTRY = (
    PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
)                                                                  # (local)

# Verdict file (canonical per gate-verdicts.md S84+)
VERDICT_TXT = SESSION_DIR / "s88_gate_verdicts.txt"

CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"             # (local)


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 helpers (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def closure_hash_of_pinmap(pinmap: dict) -> str:
    """Audit-SHA convention: SHA-256 over JSON-canonicalized pinmap.

    Sorted-key + no whitespace for byte-stable canonicalization. Matches
    the project's `closure_hash(input_pin_map)` pattern.
    """
    canonical = json.dumps(pinmap, sort_keys=True, separators=(",", ":"))  # (local)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict,
) -> tuple:
    """Compute (audit_sha256, content_sha256) per S84+ dual-SHA schema.

    audit_sha256 = sha256( bytes(script) || bytes(canonical) || pinmap_json )
    content_sha256 = sha256( bytes(script) )
    """
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Verdict aggregation (PASS-AND across 4 (axis × corner) verdicts
# for joint clauses + AND across 4 single-axis clause verdicts)
# ---------------------------------------------------------------------------

def collapse_verdicts(verdicts: list) -> str:
    """Composite collapse rule for a list of categorical verdicts.

    Per pre-registration:
      if any FAIL → FAIL
      elif any INFO → INFO
      else → PASS
    """
    if any(v == "FAIL" for v in verdicts):
        return "FAIL"
    if any(v == "INFO" for v in verdicts):
        return "INFO"
    return "PASS"


def load_auditor_json(path: Path, expected_axis: str, expected_agent: str) -> dict:
    """Load and validate an auditor JSON.

    Validates required fields per the pre-registered schema in the
    spawn prompts. Raises ValueError on schema violation.
    """
    if not path.exists():
        raise FileNotFoundError(
            f"Auditor JSON missing: {path}. The cross-reviewer subagent "
            f"may not have completed yet, or write failed."
        )
    data = json.loads(path.read_text(encoding="utf-8"))  # (local)

    required = [
        "axis", "agent", "gate_id",
        "single_axis_clauses", "joint_clauses_per_corner",
        "context_isolation_confirmed", "cross_corner_reading_smuggled_anywhere",
    ]
    missing = [k for k in required if k not in data]  # (local)
    if missing:
        raise ValueError(
            f"Auditor JSON {path.name} missing required fields: {missing}"
        )
    if data["axis"] != expected_axis:
        raise ValueError(
            f"Auditor JSON {path.name} has axis={data['axis']!r}, "
            f"expected {expected_axis!r}"
        )
    if data["agent"] != expected_agent:
        raise ValueError(
            f"Auditor JSON {path.name} has agent={data['agent']!r}, "
            f"expected {expected_agent!r}"
        )
    if data["gate_id"] != GATE_ID:
        raise ValueError(
            f"Auditor JSON {path.name} has gate_id={data['gate_id']!r}, "
            f"expected {GATE_ID!r}"
        )
    return data


def aggregate_verdicts(connes: dict, volovik: dict) -> dict:
    """Apply Stage-2 PASS-AND logic across the 4 joint (axis × corner) verdicts
    and the 4 single-axis clause verdicts.

    Returns a structured aggregate with:
      - per_clause_status: dict mapping clause-id to status
      - composite: top-level PASS/FAIL/INFO
      - joint_pass_and_status: PASS iff all 4 joint (c) verdicts PASS AND
                                all 4 joint (d) verdicts PASS
      - stage2_promotion_eligible: bool
      - context_isolation_failures: list of agents that FAILed isolation
      - cross_corner_smuggle_failures: list
    """
    # Single-axis clauses: connes audits (a)+(e); volovik audits (b)+(f)
    single_axis = {
        "a": connes["single_axis_clauses"]["(a)"]["verdict"],
        "e": connes["single_axis_clauses"]["(e)"]["verdict"],
        "b": volovik["single_axis_clauses"]["(b)"]["verdict"],
        "f": volovik["single_axis_clauses"]["(f)"]["verdict"],
    }                                                              # (local)

    # Joint clauses: each cross-reviewer fires twice (corner I + corner III)
    # 4 verdicts on (c), 4 verdicts on (d)
    joint_c = {
        "axis_A_corner_I": connes["joint_clauses_per_corner"]["(c)_at_corner_I"]["verdict"],
        "axis_A_corner_III": connes["joint_clauses_per_corner"]["(c)_at_corner_III"]["verdict"],
        "axis_B_corner_I": volovik["joint_clauses_per_corner"]["(c)_at_corner_I"]["verdict"],
        "axis_B_corner_III": volovik["joint_clauses_per_corner"]["(c)_at_corner_III"]["verdict"],
    }                                                              # (local)
    joint_d = {
        "axis_A_corner_I": connes["joint_clauses_per_corner"]["(d)_at_corner_I"]["verdict"],
        "axis_A_corner_III": connes["joint_clauses_per_corner"]["(d)_at_corner_III"]["verdict"],
        "axis_B_corner_I": volovik["joint_clauses_per_corner"]["(d)_at_corner_I"]["verdict"],
        "axis_B_corner_III": volovik["joint_clauses_per_corner"]["(d)_at_corner_III"]["verdict"],
    }                                                              # (local)

    # PASS-AND: each joint clause passes iff ALL 4 (axis × corner) verdicts PASS
    joint_c_status = collapse_verdicts(list(joint_c.values()))     # (local)
    joint_d_status = collapse_verdicts(list(joint_d.values()))     # (local)

    # Composite over all 4 single-axis + 2 joint statuses
    all_statuses = list(single_axis.values()) + [joint_c_status, joint_d_status]  # (local)
    composite = collapse_verdicts(all_statuses)                    # (local)

    # Joint PASS-AND status: PASS iff both (c) and (d) collapse to PASS
    joint_pass_and = "PASS" if joint_c_status == "PASS" and joint_d_status == "PASS" else (
        "FAIL" if "FAIL" in (joint_c_status, joint_d_status) else "INFO"
    )                                                              # (local)

    # Stage-2 promotion: eligible iff composite==PASS AND joint_pass_and==PASS
    promotion_eligible = composite == "PASS" and joint_pass_and == "PASS"  # (local)

    # Context-isolation failures
    iso_failures = []                                              # (local)
    if not connes.get("context_isolation_confirmed", False):
        iso_failures.append("connes")
    if not volovik.get("context_isolation_confirmed", False):
        iso_failures.append("volovik")

    smuggle_failures = []                                          # (local)
    if connes.get("cross_corner_reading_smuggled_anywhere", False):
        smuggle_failures.append("connes")
    if volovik.get("cross_corner_reading_smuggled_anywhere", False):
        smuggle_failures.append("volovik")

    # Context-isolation or cross-corner-smuggle FAIL forces composite to FAIL
    # (these are structural Stage-2 protocol violations regardless of clause-level PASSes)
    if iso_failures or smuggle_failures:
        composite = "FAIL"
        promotion_eligible = False

    return {
        "single_axis": single_axis,
        "joint_c": joint_c,
        "joint_d": joint_d,
        "joint_c_status": joint_c_status,
        "joint_d_status": joint_d_status,
        "joint_pass_and_status": joint_pass_and,
        "composite": composite,
        "stage_2_promotion_eligible": promotion_eligible,
        "context_isolation_failures": iso_failures,
        "cross_corner_smuggle_failures": smuggle_failures,
    }


def build_value_str(agg: dict) -> str:
    """Construct the canonical value=... field per gate-verdicts.md S84+.

    Single-quoted; semicolon-separated key=value sub-fields; no spaces.
    """
    sa = agg["single_axis"]                                        # (local)
    jc = agg["joint_c"]                                            # (local)
    jd = agg["joint_d"]                                            # (local)
    parts = [
        f"composite={agg['composite']}",
        f"joint_pass_and={agg['joint_pass_and_status']}",
        f"a={sa['a']}",
        f"b={sa['b']}",
        f"e={sa['e']}",
        f"f={sa['f']}",
        f"c@I_axA={jc['axis_A_corner_I']}",
        f"c@III_axA={jc['axis_A_corner_III']}",
        f"c@I_axB={jc['axis_B_corner_I']}",
        f"c@III_axB={jc['axis_B_corner_III']}",
        f"d@I_axA={jd['axis_A_corner_I']}",
        f"d@III_axA={jd['axis_A_corner_III']}",
        f"d@I_axB={jd['axis_B_corner_I']}",
        f"d@III_axB={jd['axis_B_corner_III']}",
        f"stage_2_promotion_eligible={agg['stage_2_promotion_eligible']}",
        f"context_isolation_failures={'-'.join(agg['context_isolation_failures']) or 'none'}",
        f"cross_corner_smuggle={'-'.join(agg['cross_corner_smuggle_failures']) or 'none'}",
        f"rel_tol={REL_TOL}",
    ]                                                              # (local)
    return ";".join(parts)


# ---------------------------------------------------------------------------
# Section 6 — Append verdict line (canonical S84+ schema)
# ---------------------------------------------------------------------------

def append_verdict(
    verdict: str,
    value_str: str,
    audit_sha: str,
    content_sha: str,
) -> None:
    """Append canonical verdict line + dual-SHA companion row.

    Matches gate-verdicts.md S84+ format. Atomic append (single open("a")).
    """
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )                                                              # (local)
    companion_row = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )                                                              # (local)

    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(companion_row)


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()                                               # (local)

    print(f"=== {GATE_ID} — input SHA-256 pins ===")

    # 1. Hash all input files for the pin map
    pins = {
        "computations/session-88/s88_w7a_71_connes_verdict.json": sha256_of(CONNES_JSON),
        "computations/session-88/s88_w7a_71_volovik_verdict.json": sha256_of(VOLOVIK_JSON),
        "computations/_shared/canonical_constants.py": sha256_of(CANONICAL_PATH),
        "sessions/permanent-results-registry.md": sha256_of(PERM_REGISTRY),
    }                                                              # (local)
    for k, v in pins.items():
        print(f"  {k}: {v[:16]}...")

    # 2. Compute dual-SHA (script || canonical || pinmap_json)
    audit_sha, content_sha = compute_dual_sha(
        Path(__file__).resolve(), CANONICAL_PATH, pins
    )
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 3. Load auditor JSONs (fail fast if missing)
    print("=== Loading auditor JSONs ===")
    connes = load_auditor_json(
        CONNES_JSON, "spectral-functional", "connes-ncg-theorist"
    )                                                              # (local)
    volovik = load_auditor_json(
        VOLOVIK_JSON, "transit-dynamics", "volovik-superfluid-universe-theorist"
    )                                                              # (local)
    print(f"  connes: {len(connes['single_axis_clauses'])} single-axis clauses, "
          f"{len(connes['joint_clauses_per_corner'])} joint (axis × corner) verdicts")
    print(f"  volovik: {len(volovik['single_axis_clauses'])} single-axis clauses, "
          f"{len(volovik['joint_clauses_per_corner'])} joint (axis × corner) verdicts")
    print()

    # 4. Aggregate verdicts (PASS-AND logic)
    print("=== Aggregating Stage-2 verdicts ===")
    agg = aggregate_verdicts(connes, volovik)                      # (local)

    print(f"  Single-axis clauses (a, b, e, f):")
    for k, v in agg["single_axis"].items():
        print(f"    ({k}): {v}")
    print(f"  Joint clause (c) per (axis × corner) — PASS-AND status: {agg['joint_c_status']}")
    for k, v in agg["joint_c"].items():
        print(f"    {k}: {v}")
    print(f"  Joint clause (d) per (axis × corner) — PASS-AND status: {agg['joint_d_status']}")
    for k, v in agg["joint_d"].items():
        print(f"    {k}: {v}")
    print(f"  Composite: {agg['composite']}")
    print(f"  Joint PASS-AND status: {agg['joint_pass_and_status']}")
    print(f"  Stage-2 promotion eligible: {agg['stage_2_promotion_eligible']}")
    print(f"  Context-isolation failures: {agg['context_isolation_failures'] or 'none'}")
    print(f"  Cross-corner smuggle failures: {agg['cross_corner_smuggle_failures'] or 'none'}")
    print()

    # 5. Build value string + emit verdict
    value_str = build_value_str(agg)                               # (local)
    verdict = agg["composite"]                                     # (local)

    tag = (f"(value='{value_str}', scheme={SCHEME}, "
           f"convention={CONVENTION}, L_max={L_MAX})")             # (local)
    print(f"4-tuple: {tag}")
    print()

    append_verdict(verdict, value_str, audit_sha, content_sha)

    wall = time.time() - t0                                        # (local)
    print(f"=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    print(f"  Verdict appended to: {VERDICT_TXT.name}")

    # Exit 0 regardless of PASS/FAIL/INFO (verdict is data, not exit code)
    # per math-scripts.md §"Exit Codes and Verdict Semantics"
    return 0


if __name__ == "__main__":
    sys.exit(main())
