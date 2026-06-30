#!/usr/bin/env python3
"""
S105 W6-1 S105-VIIU2-STAGE2-VERIFY — Stage-2 PASS-AND closeout
=============================================================

Gate: S105-VIIU2-STAGE2-VERIFY ([VERIFY-THEOREM])

Stage-2 two-agent parallel cross-axis independent-verify of the §VII.U.2 PARENT
four-corner classification theorem (algebra-axis × Mellin-pole orthogonality),
per `.claude/rules/joint-theorem-promotion.md §"Stage 2"`.

This script is STEP 2 (the PASS-AND closeout). STEP 1 (the two blind reviewer
dispatches) is orchestrated by the gen-physicist agent OUTSIDE this script; the
two reviewer verdict JSONs are this script's inputs.

Pre-registered aggregation (plan §W6-1 machinery_pin_map.passand_logic +
substitution_chain Step 3-4):
  PARENT clause partition (registered entry, registry ~line 13029-13044 + clause (e)):
    single_axis(A) = {(a) INVARIANT family, (b) DEPENDENT family}   [vdd / Axis-A audits]
    JOINT          = {(c) orthogonality, (d) 4-corner partition, (e) convergence}
  PASS-AND logic:
    - JOINT clauses (c),(d),(e) PASS iff BOTH reviewer JSONs return PASS on that
      clause (logical AND, NOT OR).
    - single-axis clauses (a),(b) PASS iff the Axis-A reviewer returns PASS.
    - composite = FAIL  if any audited clause == FAIL in either verdict
                = INFO  elif any audited clause == INFO (no FAIL)
                = PASS  else (every conjunct PASS).

SCOPE FENCE: the Corner-II Var_a SUB-row (registry ~line 13098-13136) is
STAGE-3-PERMANENT (S92 W4-7) and is OUT OF SCOPE — the PARENT theorem clauses
ONLY are aggregated here. The scope-fence flag is recorded in the npz.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-105/s105_w6_viiu2_reviewer_vdd_axisA_verdict.json
  - computations/session-105/s105_w6_viiu2_reviewer_kitaev_axisB_verdict.json
  - sessions/permanent-results-registry.md (the registered PARENT entry text;
    feeds audit_sha256 — the closeout pins the entry it validated)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<composite + per-clause matrix>, scheme=joint-theorem-stage-2-cross-axis-verify,
   convention=vii-u-2-PARENT-stage-1-candidate-to-stage-3-promotion-cross-axis-PASS-AND, L_max=N/A)

Classification: NON-PHONONIC (methodology-floor F-image; structural validation of
an algebra-axis GEOMETRIC substrate-IS theorem).

METHODOLOGY
-----------
Pure verdict-aggregation: JSON load + categorical string compare + dual-SHA. No
linear algebra. The two reviewer JSONs were produced by blind dispatches (no
workshop context); this script performs the deterministic PASS-AND collapse per
the pre-registered partition and emits ONE verdict line. The aggregation is
monotone in the per-clause verdicts (removing a PASS conjunct cannot raise the
composite); PASS is reachable ONLY by the full all-PASS conjunction over the
PARENT partition.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- CPU-only aggregation; OMP capped to 8 (no GPU; avoids contention)
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- Gate verdict emitted via the `emit_verdict` knowledge-MCP tool (race-safe):
  the script PRINTS the payload (print_verdict_payload); the dispatching AGENT
  reads it and calls mcp__knowledge__emit_verdict(**payload).
"""

from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403,E402

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION = "S105"                                                   # (local)
GATE_ID = "S105-VIIU2-STAGE2-VERIFY"                              # (local)
SCHEME = "joint-theorem-stage-2-cross-axis-verify"               # (local)
CONVENTION = ("vii-u-2-PARENT-stage-1-candidate-to-stage-3-"
              "promotion-cross-axis-PASS-AND")                    # (local)
L_MAX = "N/A"                                                     # (local)

# Pre-registered PARENT clause partition (plan §W6-1 machinery_pin_map)
SINGLE_AXIS_A_CLAUSES = ["a", "b"]                                # (local)
JOINT_CLAUSES = ["c", "d", "e"]                                   # (local)
ALL_PARENT_CLAUSES = ["a", "b", "c", "d", "e"]                    # (local)

REVIEWER_A_JSON = (SESSION_DIR
                   / "s105_w6_viiu2_reviewer_vdd_axisA_verdict.json")
REVIEWER_B_JSON = (SESSION_DIR
                   / "s105_w6_viiu2_reviewer_kitaev_axisB_verdict.json")
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"

OUT_NPZ = SESSION_DIR / "s105_w6_viiu2_stage2_passand.npz"
OUT_PNG = SESSION_DIR / "s105_w6_viiu2_stage2_passand.png"

# The registered §VII.U.2 PARENT entry block bounds (PARENT clauses ONLY; the
# Var_a SUB-row at ~13098+ is OUT OF SCOPE — scope-fence). Located by header
# anchor at plan-freeze; offsets pinned for the audit-SHA entry-text excerpt.
PARENT_HEADER_ANCHOR = ("### §VII.U.2 — Four-corner classification of "
                        "(A_K, H_K, D_K) functionals")             # (local)
VAR_A_SUBROW_ANCHOR = ("**STAGE-3-PERMANENT — Var_a(n_a^GGE) "
                       "Corner-II joint theorem")                  # (local)

INPUT_FILES = [
    CANONICAL_PATH,
    REVIEWER_A_JSON,
    REVIEWER_B_JSON,
    REGISTRY_PATH,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def extract_parent_entry_text() -> str:
    """Extract the registered §VII.U.2 PARENT entry text (PARENT clauses ONLY,
    up to but EXCLUDING the Var_a SUB-row) for the audit-SHA entry-text pin."""
    try:
        full = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)
    except OSError:
        return ""
    start = full.find(PARENT_HEADER_ANCHOR)  # (local)
    if start < 0:
        return ""
    sub = full.find(VAR_A_SUBROW_ANCHOR, start)  # (local)
    if sub < 0:
        # fall back to a bounded window if the subrow anchor drifts
        return full[start:start + 12000]
    return full[start:sub]


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
    parent_entry_text: str,
) -> tuple[str, str]:
    """audit_sha256 = sha256(script || canonical || pinmap_json || parent_entry).
    content_sha256 = sha256(script). The parent_entry_text is folded into
    audit_sha256 so the closeout pins the EXACT registered text it validated
    (audit_discriminators.audit_sha256_inputs includes
    'registered_VII_U_2_PARENT_entry_text')."""
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

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_audit.update(parent_entry_text.encode("utf-8"))
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Compute (PASS-AND aggregation)
# ---------------------------------------------------------------------------

_VALID_TOKENS = {"PASS", "FAIL", "INFO"}  # (local)


def load_reviewer(path: Path, expected_axis: str) -> dict:
    """Load a reviewer verdict JSON; assert structure + valid verdict tokens."""
    if not path.exists():
        raise FileNotFoundError(f"Reviewer JSON missing: {path}")
    obj = json.loads(path.read_text(encoding="utf-8"))  # (local)
    if obj.get("axis") != expected_axis:
        raise ValueError(
            f"{path.name}: axis={obj.get('axis')!r} != expected {expected_axis!r}")
    cv = obj.get("clause_verdicts", {})  # (local)
    for c in ALL_PARENT_CLAUSES:
        if c not in cv:
            raise ValueError(f"{path.name}: missing clause '{c}' verdict")
        tok = str(cv[c].get("verdict", "")).strip().upper()  # (local)
        if tok not in _VALID_TOKENS:
            raise ValueError(
                f"{path.name}: clause '{c}' verdict {tok!r} not in {_VALID_TOKENS}")
    return obj


def clause_token(reviewer: dict, clause: str) -> str:
    return str(reviewer["clause_verdicts"][clause]["verdict"]).strip().upper()


def aggregate(rev_a: dict, rev_b: dict) -> dict:
    """Compute the per-clause PASS-AND aggregate + composite per the
    pre-registered partition (plan §W6-1)."""
    per_clause: dict[str, str] = {}  # (local)
    detail: dict[str, dict] = {}     # (local)

    for c in ALL_PARENT_CLAUSES:
        a_tok = clause_token(rev_a, c)  # (local)
        b_tok = clause_token(rev_b, c)  # (local)

        if c in JOINT_CLAUSES:
            # JOINT: PASS iff BOTH PASS; FAIL if either FAIL; else INFO.
            if a_tok == "FAIL" or b_tok == "FAIL":
                agg = "FAIL"  # (local)
            elif a_tok == "PASS" and b_tok == "PASS":
                agg = "PASS"
            else:
                agg = "INFO"
        else:
            # single-axis (a),(b): governed by the Axis-A reviewer ONLY.
            agg = a_tok
        per_clause[c] = agg
        detail[c] = {
            "axis_A": a_tok,
            "axis_B": b_tok,
            "aggregate": agg,
            "kind": "JOINT" if c in JOINT_CLAUSES else "single-axis-A",
        }

    # Composite collapse: FAIL on any clause FAIL; INFO on any clause INFO
    # (no FAIL); else PASS.
    agg_vals = list(per_clause.values())  # (local)
    if "FAIL" in agg_vals:
        composite = "FAIL"  # (local)
    elif "INFO" in agg_vals:
        composite = "INFO"
    else:
        composite = "PASS"

    return {
        "per_clause": per_clause,
        "detail": detail,
        "composite": composite,
    }


# ---------------------------------------------------------------------------
# Section 6 — Verdict payload + 4-tuple
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(
    verdict: str,
    value,
    audit_sha: str,
    content_sha: str,
    extra_rows: list[str] | None = None,
) -> dict:
    payload: dict = {
        "session": int(SESSION.lstrip("Ss")),
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 7 — Plot (per-clause PASS/FAIL/INFO grid)
# ---------------------------------------------------------------------------

def make_plot(detail: dict, composite: str) -> None:
    tok_to_num = {"PASS": 2, "INFO": 1, "FAIL": 0}  # (local)
    tok_to_color = {"PASS": "#2e7d32", "INFO": "#f9a825", "FAIL": "#c62828"}  # (local)
    clauses = ALL_PARENT_CLAUSES                                            # (local)
    cols = ["Axis-A (vdd)", "Axis-B (kitaev)", "PASS-AND"]                  # (local)

    grid = np.zeros((len(clauses), 3))                                     # (local)
    labels = [["", "", ""] for _ in clauses]                               # (local)
    for i, c in enumerate(clauses):
        d = detail[c]  # (local)
        a_tok = d["axis_A"]  # (local)
        b_tok = d["axis_B"]  # (local)
        agg = d["aggregate"]  # (local)
        # single-axis clauses: Axis-B did render a verdict but it is NON-binding
        # for (a),(b); show it greyed via a label note.
        grid[i, 0] = tok_to_num[a_tok]
        grid[i, 1] = tok_to_num[b_tok]
        grid[i, 2] = tok_to_num[agg]
        labels[i][0] = a_tok
        labels[i][1] = b_tok + ("*" if d["kind"] == "single-axis-A" else "")
        labels[i][2] = agg

    fig, ax = plt.subplots(figsize=(8.0, 5.2))  # (local)
    for i in range(len(clauses)):
        for j in range(3):
            tok = labels[i][j].rstrip("*")  # (local)
            ax.add_patch(plt.Rectangle((j, len(clauses) - 1 - i), 1, 1,
                                       facecolor=tok_to_color.get(tok, "#999"),
                                       edgecolor="white", lw=2))
            ax.text(j + 0.5, len(clauses) - 1 - i + 0.5, labels[i][j],
                    ha="center", va="center", color="white",
                    fontsize=11, fontweight="bold")
    ax.set_xlim(0, 3)
    ax.set_ylim(0, len(clauses))
    ax.set_xticks([0.5, 1.5, 2.5])
    ax.set_xticklabels(cols, fontsize=10)
    ax.set_yticks([len(clauses) - 1 - i + 0.5 for i in range(len(clauses))])
    clause_names = {
        "a": "(a) INVARIANT family [single-axis-A]",
        "b": "(b) DEPENDENT family [single-axis-A]",
        "c": "(c) orthogonality [JOINT]",
        "d": "(d) 4-corner partition [JOINT]",
        "e": "(e) convergence [JOINT]",
    }  # (local)
    ax.set_yticklabels([clause_names[c] for c in clauses], fontsize=9)
    ax.xaxis.tick_top()
    ax.set_title(
        f"§VII.U.2 PARENT Stage-2 cross-axis verify — composite: {composite}\n"
        "(* = Axis-B verdict NON-binding for single-axis-A clauses; "
        "Var_a SUB-row OUT OF SCOPE [already STAGE-3-PERMANENT])",
        fontsize=10, pad=28)
    ax.set_aspect("equal")
    for spine in ax.spines.values():
        spine.set_visible(False)
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=130, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    parent_entry_text = extract_parent_entry_text()  # (local)
    print(f"  parent_entry_text_len: {len(parent_entry_text)} chars "
          f"(scope-fenced PARENT block; Var_a SUB-row excluded)")

    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(
        script_path, CANONICAL_PATH, pins, parent_entry_text)
    print(f"  audit_sha256:   {audit_sha[:16]}... "
          f"(script+canonical+pinmap+parent_entry)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # Load both blind reviewer verdicts
    rev_a = load_reviewer(REVIEWER_A_JSON, "A")  # (local)
    rev_b = load_reviewer(REVIEWER_B_JSON, "B")  # (local)
    print(f"  Axis-A reviewer: {rev_a.get('reviewer')} "
          f"(blind={rev_a.get('blind_dispatch_confirmed')}, "
          f"workshop_read={rev_a.get('workshop_transcripts_read')})")
    print(f"  Axis-B reviewer: {rev_b.get('reviewer')} "
          f"(blind={rev_b.get('blind_dispatch_confirmed')}, "
          f"workshop_read={rev_b.get('workshop_transcripts_read')})")
    print()

    # PASS-AND aggregation
    agg = aggregate(rev_a, rev_b)  # (local)
    composite = agg["composite"]   # (local)

    print("  Per-clause aggregation (PARENT partition):")
    for c in ALL_PARENT_CLAUSES:
        d = agg["detail"][c]  # (local)
        print(f"    ({c}) [{d['kind']:>14}]  A={d['axis_A']:>4}  "
              f"B={d['axis_B']:>4}  ->  {d['aggregate']}")
    print(f"\n  COMPOSITE: {composite}")

    make_plot(agg["detail"], composite)

    # Persist the verdict matrix
    per_clause = agg["per_clause"]  # (local)
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        composite=composite,
        clauses=np.array(ALL_PARENT_CLAUSES),
        single_axis_A_clauses=np.array(SINGLE_AXIS_A_CLAUSES),
        joint_clauses=np.array(JOINT_CLAUSES),
        axis_A_tokens=np.array([clause_token(rev_a, c)
                                for c in ALL_PARENT_CLAUSES]),
        axis_B_tokens=np.array([clause_token(rev_b, c)
                                for c in ALL_PARENT_CLAUSES]),
        passand_aggregate=np.array([per_clause[c]
                                    for c in ALL_PARENT_CLAUSES]),
        reviewer_A=rev_a.get("reviewer", ""),
        reviewer_B=rev_b.get("reviewer", ""),
        scope_fence_var_a_subrow="OUT-OF-SCOPE-STAGE-3-PERMANENT-S92-W4-7",
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )

    # Build a compact value string for the verdict line (no single quotes)
    matrix = ";".join(f"{c}:A={clause_token(rev_a, c)}/B={clause_token(rev_b, c)}"
                      f"/AND={per_clause[c]}"
                      for c in ALL_PARENT_CLAUSES)  # (local)
    value = (f"composite={composite}|partition[{matrix}]|"
             f"single_axis(a,b)=Axis-A-only|JOINT(c,d,e)=PASS-AND|"
             f"scope-fence:Var_a-SUB-row-OUT(STAGE-3-PERMANENT-S92-W4-7)")  # (local)

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)

    extra = [
        f"# reviewer_axis_A={rev_a.get('reviewer')} "
        f"reviewer_axis_B={rev_b.get('reviewer')} "
        f"(blind two-agent parallel cross-axis verify; "
        f"EXCLUDED={{connes-ncg-theorist,lizzi-spectral-functional-theorist,"
        f"mack-cosmic-bridge}}) # {GATE_ID} reviewer-pair annotation",
        f"# scope-fence: §VII.U.2 PARENT clauses (a)-(e) ONLY; "
        f"Corner-II Var_a SUB-row STAGE-3-PERMANENT (S92 W4-7) NOT re-verified "
        f"# {GATE_ID} scope annotation",
    ]  # (local)
    print_verdict_payload(composite, value, audit_sha, content_sha,
                          extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
