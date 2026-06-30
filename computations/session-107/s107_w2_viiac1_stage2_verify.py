#!/usr/bin/env python3
"""
S107 W2-1 S107-VIIAC1-STAGE2-VERIFY — Stage-2 blind cross-axis PASS-AND aggregator
=================================================================================

Gate: S107-VIIAC1-STAGE2-VERIFY ([VERIFY-THEOREM])

Pre-registered rule (NON-COMPUTE adjudication gate; NO physics here):
  This script aggregates the TWO blind reviewers' clause-verdict JSONs into the
  cross-axis composite per joint-theorem-promotion.md §"Stage 2" + plan §W2-1
  (sessions/session-plan/session-107-plan-w2.md lines 173-193). It performs NO
  physics computation — the physics audit is the reviewers' first-principles
  re-derivation; this script is the deterministic AND-aggregator.

  AGGREGATION RULE (applied EXACTLY; not re-derived):
    - A JOINT clause contributes PASS only if PASS in BOTH reviewer verdicts
      (logical AND); if INFO/FAIL in EITHER, it degrades to that worse verdict.
    - single-axis-A clauses come from reviewer-A's verdict; single-axis-B from
      reviewer-B's.
    - composite = FAIL if ANY clause is FAIL in either reviewer OR either
      overall_axis_verdict is FAIL; else INFO if ANY clause is INFO in either
      reviewer OR either overall_axis_verdict is INFO; else PASS.

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - computations/session-107/s107_w2_viiac1_reviewerA_vandendungen_clause_verdicts.json
  - computations/session-107/s107_w2_viiac1_reviewerB_kitaev_clause_verdicts.json
  - the registered §VII.AC.1 Stage-1 entry span (registry lines 15145-15165) — content SHA
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

audit_sha256 inputs (per plan audit_discriminators):
  [script, registered_stage1_entry_sha, reviewer_A_clause_verdict_json_sha,
   reviewer_B_clause_verdict_json_sha, pinmap]
content_sha256 inputs: [script]

Output 4-tuple:
  (value=<composite + per-clause matrix + caveat>, scheme=STAGE-2-BLIND-CROSS-AXIS-VERIFY,
   convention=SOURCE-DOUBLE-CITE-CO-PRIMARY-PASS-AND, L_max=10)

Classification: GEOMETRIC (the audited object is a substrate-IS B1/B2 block
decomposition of D_K^2 at tau_fold forced by Schur orthogonality on
A_F = C (+) H (+) M_3(C); the aggregation itself is NON-PHONONIC bookkeeping).

DISCIPLINE
----------
- `from canonical_constants import *`
- every local/intermediate tagged `# (local)`
- NO linear algebra (integer/boolean aggregation) — cpu, no GPU needed
- SHA-256 of all inputs logged in first lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- verdict emitted via the emit_verdict knowledge-MCP tool: this script PRINTS
  the payload (print_verdict_payload); the dispatching AGENT calls emit_verdict.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — Make computations/_shared importable (canonical_constants lives
# there; this keeps the script self-contained regardless of caller PYTHONPATH).
# ---------------------------------------------------------------------------
import sys as _sys
from pathlib import Path as _Path
_SHARED = _Path(__file__).resolve().parent.parent / "_shared"
if str(_SHARED) not in _sys.path:
    _sys.path.insert(0, str(_SHARED))

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403,E402

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S107"                                                  # (local)
GATE_ID = "S107-VIIAC1-STAGE2-VERIFY"                             # (local)
SCHEME = "STAGE-2-BLIND-CROSS-AXIS-VERIFY"                        # (local)
CONVENTION = "SOURCE-DOUBLE-CITE-CO-PRIMARY-PASS-AND"            # (local)
L_MAX = 10                                                        # (local)

# Reviewer clause-verdict JSONs (produced at dispatch; blind reviewers)
REVIEWER_A_JSON = SESSION_DIR / "s107_w2_viiac1_reviewerA_vandendungen_clause_verdicts.json"  # (local)
REVIEWER_B_JSON = SESSION_DIR / "s107_w2_viiac1_reviewerB_kitaev_clause_verdicts.json"        # (local)

# Registered §VII.AC.1 Stage-1 entry span — lines 15145-15165 (1-indexed inclusive)
REGISTRY_FILE = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)
REG_LINE_START = 15145                                            # (local) §VII.AC.1 header line
REG_LINE_END = 15165                                              # (local) end of AC.1 substrate-framing block

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / "s107_w2_viiac1_stage2_verify.npz"        # (local)
OUT_PNG = SESSION_DIR / "s107_w2_viiac1_stage2_verify.png"        # (local)

# ---- Pre-registered clause partition (plan §W2-1 lines 173-184) ----
# single-axis-A clauses come from reviewer-A; single-axis-B from reviewer-B;
# JOINT clauses are PASS-AND'd across both. The keys MUST match the JSON keys
# the blind reviewers emitted.
SINGLE_AXIS_A_CLAUSES = ["single-axis-A-1", "single-axis-A-2"]    # (local)
SINGLE_AXIS_B_CLAUSES = ["single-axis-B-1", "single-axis-B-2"]    # (local)
JOINT_CLAUSES = ["JOINT-1", "JOINT-2"]                            # (local)

# Verdict severity ordering (worst-wins for degradation / composite collapse)
SEVERITY = {"PASS": 0, "INFO": 1, "FAIL": 2}                      # (local)
SEVERITY_INV = {0: "PASS", 1: "INFO", 2: "FAIL"}                  # (local)


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def sha256_of_registry_span(path: Path, start: int, end: int) -> str:
    """Content SHA-256 of the §VII.AC.1 entry span (1-indexed inclusive lines).

    Pins the registered Stage-1 entry text the blind reviewers audited — so the
    audit_sha256 is bound to the EXACT registry text in effect at verify time.
    """
    h = hashlib.sha256()  # (local)
    try:
        lines = path.read_text(encoding="utf-8").splitlines(keepends=True)  # (local)
    except OSError:
        return ""
    span = "".join(lines[start - 1:end])  # (local) 1-indexed inclusive
    h.update(span.encode("utf-8"))
    return h.hexdigest()


def closure_hash(pins: dict[str, str]) -> str:
    """Stable hash over input SHAs (invariant to dict ordering)."""
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
    """(audit_sha256, content_sha256) per S84+ schema.

    audit_sha256 = sha256( script || canonical || pinmap_json )
      where pinmap_json carries the reviewer JSON SHAs + the registered
      §VII.AC.1 entry-span SHA (per plan audit_discriminators).
    content_sha256 = sha256( script ) — responds to script edits only.
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
# Section 5 — Aggregate (NO physics; deterministic clause-verdict AND)
# ---------------------------------------------------------------------------

def load_reviewer(path: Path) -> dict:
    """Load a reviewer clause-verdict JSON; fail loudly if absent/malformed."""
    data = json.loads(path.read_text(encoding="utf-8"))  # (local)
    if "clause_verdicts" not in data or "overall_axis_verdict" not in data:
        raise ValueError(f"{path.name}: missing clause_verdicts / overall_axis_verdict")
    return data


def clause_verdict(reviewer: dict, clause_key: str) -> str:
    """Extract a single clause's verdict string from a reviewer JSON."""
    cv = reviewer["clause_verdicts"]  # (local)
    if clause_key not in cv:
        raise KeyError(f"clause {clause_key!r} absent from {reviewer.get('reviewer','?')}")
    v = cv[clause_key]["verdict"].strip().upper()  # (local)
    if v not in SEVERITY:
        raise ValueError(f"clause {clause_key}: unknown verdict {v!r}")
    return v


def aggregate(reviewer_a: dict, reviewer_b: dict) -> dict:
    """Deterministic cross-axis PASS-AND aggregation per plan §W2-1.

    Returns a dict carrying:
      - per_clause: {clause_key: {"A": v|None, "B": v|None, "agg": v, "type": t}}
      - composite: PASS|FAIL|INFO
      - overall_axis: {"A": v, "B": v}
      - info_clauses / fail_clauses: lists
      - matrix: 2x6 reviewer x clause int verdict matrix (np.int8)
      - clause_order: column order for the matrix
    """
    per_clause: dict = {}  # (local)

    # single-axis-A: from reviewer-A only (reviewer-B column = None / -1)
    for c in SINGLE_AXIS_A_CLAUSES:
        va = clause_verdict(reviewer_a, c)  # (local)
        per_clause[c] = {"A": va, "B": None, "agg": va, "type": "single-axis-A"}

    # single-axis-B: from reviewer-B only (reviewer-A column = None / -1)
    for c in SINGLE_AXIS_B_CLAUSES:
        vb = clause_verdict(reviewer_b, c)  # (local)
        per_clause[c] = {"A": None, "B": vb, "agg": vb, "type": "single-axis-B"}

    # JOINT: PASS-AND across both — worst-of (max severity) is the aggregate
    for c in JOINT_CLAUSES:
        va = clause_verdict(reviewer_a, c)  # (local)
        vb = clause_verdict(reviewer_b, c)  # (local)
        agg = SEVERITY_INV[max(SEVERITY[va], SEVERITY[vb])]  # (local) logical-AND degrade
        per_clause[c] = {"A": va, "B": vb, "agg": agg, "type": "JOINT"}

    overall_a = reviewer_a["overall_axis_verdict"].strip().upper()  # (local)
    overall_b = reviewer_b["overall_axis_verdict"].strip().upper()  # (local)

    # --- composite collapse (plan §W2-1 + spawn-prompt rule, worst-wins) ---
    # Gather every per-reviewer clause verdict actually present + both overalls.
    all_verdicts = []  # (local)
    for c, d in per_clause.items():
        if d["A"] is not None:
            all_verdicts.append(d["A"])
        if d["B"] is not None:
            all_verdicts.append(d["B"])
    all_verdicts.append(overall_a)
    all_verdicts.append(overall_b)

    worst = max(SEVERITY[v] for v in all_verdicts)  # (local)
    composite = SEVERITY_INV[worst]  # (local)

    # Bookkeeping: which clauses drove INFO / FAIL (per-reviewer granularity)
    info_clauses = []  # (local)
    fail_clauses = []  # (local)
    for c, d in per_clause.items():
        for side in ("A", "B"):
            v = d[side]
            if v == "INFO":
                info_clauses.append(f"{c}[{side}]")
            elif v == "FAIL":
                fail_clauses.append(f"{c}[{side}]")

    # 2 x N int verdict matrix (rows: A, B; cols: clause_order). -1 = N/A (clause
    # not on that reviewer's axis).
    clause_order = (SINGLE_AXIS_A_CLAUSES + SINGLE_AXIS_B_CLAUSES + JOINT_CLAUSES)  # (local)
    matrix = np.full((2, len(clause_order)), -1, dtype=np.int8)  # (local)
    for j, c in enumerate(clause_order):
        d = per_clause[c]
        if d["A"] is not None:
            matrix[0, j] = SEVERITY[d["A"]]
        if d["B"] is not None:
            matrix[1, j] = SEVERITY[d["B"]]

    return {
        "per_clause": per_clause,
        "composite": composite,
        "overall_axis": {"A": overall_a, "B": overall_b},
        "info_clauses": info_clauses,
        "fail_clauses": fail_clauses,
        "matrix": matrix,
        "clause_order": clause_order,
    }


def maybe_plot(agg: dict) -> bool:
    """OPTIONAL clause-verdict heatmap. Returns True if written, False if skipped."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        from matplotlib.colors import ListedColormap, BoundaryNorm
    except Exception as exc:  # (local) plotting is optional per plan
        print(f"  [plot skipped: {exc}]")
        return False

    matrix = agg["matrix"]  # (local)
    clause_order = agg["clause_order"]  # (local)
    # Colormap: -1 N/A (grey), 0 PASS (green), 1 INFO (amber), 2 FAIL (red)
    cmap = ListedColormap(["#cfcfcf", "#2ca02c", "#ff9e1b", "#d62728"])  # (local)
    norm = BoundaryNorm([-1.5, -0.5, 0.5, 1.5, 2.5], cmap.N)  # (local)

    fig, ax = plt.subplots(figsize=(9.5, 3.0))  # (local)
    ax.imshow(matrix, cmap=cmap, norm=norm, aspect="auto")
    ax.set_xticks(range(len(clause_order)))
    ax.set_xticklabels(clause_order, rotation=30, ha="right", fontsize=8)
    ax.set_yticks([0, 1])
    ax.set_yticklabels(["A: van-den-dungen\n(NCG-axiomatic)",
                        "B: kitaev\n(spectral-block)"], fontsize=8)
    label = {-1: "N/A", 0: "PASS", 1: "INFO", 2: "FAIL"}  # (local)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            ax.text(j, i, label[int(matrix[i, j])], ha="center", va="center",
                    fontsize=7, color="black")
    ax.set_title(f"{GATE_ID} — clause-verdict matrix → composite = {agg['composite']}\n"
                 f"(JOINT = PASS-AND across both axes; single-axis from own reviewer)",
                 fontsize=9)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)
    return True


# ---------------------------------------------------------------------------
# Section 6 — Verdict payload (printed; agent calls emit_verdict)
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
    """PRINT the verdict payload for the dispatching agent to pass to emit_verdict.

    NOT a [SIGN] gate — no 3-tuple. The script does NOT write the verdict file;
    the lock-serialized write is owned by emit_verdict (gate-verdicts.md
    §"Race-Safe Emission"). `value` carries NO single-quote chars (the tool
    wraps value='...').
    """
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
# Section 7 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)

    # 1. Input SHA-256 pins (first lines of stdout). The pinmap that feeds
    #    audit_sha256 carries exactly the plan's audit_discriminators:
    #    [script, registered_stage1_entry_sha, reviewer_A_json_sha,
    #     reviewer_B_json_sha] (+ canonical folded into compute_dual_sha).
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    reg_span_sha = sha256_of_registry_span(REGISTRY_FILE, REG_LINE_START, REG_LINE_END)  # (local)
    rev_a_sha = sha256_of(REVIEWER_A_JSON)  # (local)
    rev_b_sha = sha256_of(REVIEWER_B_JSON)  # (local)
    script_sha = sha256_of(script_path)  # (local)
    canonical_sha = sha256_of(canonical_path)  # (local)

    pins = {
        "script:s107_w2_viiac1_stage2_verify.py": script_sha,
        f"registry:VII.AC.1[L{REG_LINE_START}-{REG_LINE_END}]": reg_span_sha,
        "reviewerA:vandendungen_clause_verdicts.json": rev_a_sha,
        "reviewerB:kitaev_clause_verdicts.json": rev_b_sha,
    }  # (local)
    for k, v in sorted(pins.items()):
        print(f"  {k}: {v[:16]}...")
    print(f"  canonical_constants.py: {canonical_sha[:16]}... (folded into audit_sha256)")

    closure = closure_hash(pins)  # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. Dual SHAs
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Load reviewers + aggregate (NO physics)
    reviewer_a = load_reviewer(REVIEWER_A_JSON)  # (local)
    reviewer_b = load_reviewer(REVIEWER_B_JSON)  # (local)
    print(f"  reviewer-A: {reviewer_a.get('reviewer')} (axis {reviewer_a.get('axis')})")
    print(f"  reviewer-B: {reviewer_b.get('reviewer')} (axis {reviewer_b.get('axis')})")
    agg = aggregate(reviewer_a, reviewer_b)  # (local)

    # 3. Report the matrix
    print("\n=== per-clause verdict matrix (cross-axis PASS-AND) ===")
    for c in agg["clause_order"]:
        d = agg["per_clause"][c]  # (local)
        a_s = d["A"] if d["A"] is not None else "  -- "  # (local)
        b_s = d["B"] if d["B"] is not None else "  -- "  # (local)
        print(f"  {c:<16} type={d['type']:<14} A={a_s:<5} B={b_s:<5} -> agg={d['agg']}")
    print(f"  overall_axis: A={agg['overall_axis']['A']}  B={agg['overall_axis']['B']}")
    print(f"  INFO clauses: {agg['info_clauses']}")
    print(f"  FAIL clauses: {agg['fail_clauses']}")
    composite = agg["composite"]  # (local)
    print(f"\n  ==> COMPOSITE = {composite}")

    # 4. Substrate-input-overlap caveat (plan §W2-1 lines 214-223). Both reviewers
    #    load the SAME s87_w3 npz -> structural-OUTPUT-type independence ONLY.
    caveat = ("SUBSTRATE-INPUT-OVERLAP-CAVEAT: both reviewers loaded the same "
              "s87_w3_path_h_path_c_registry_landing npz/json; Stage-2 PASS-AND "
              "establishes structural-OUTPUT-type independence (two distinct "
              "decision pipelines on shared data), NOT structural-INPUT "
              "independence (no obs loaded by exactly one reviewer)")  # (local)

    # 5. Save data (reviewer x clause verdict matrix + aggregate)
    np.savez(
        OUT_NPZ,
        clause_order=np.array(agg["clause_order"], dtype=object),
        verdict_matrix=agg["matrix"],
        verdict_legend=np.array(["-1=N/A", "0=PASS", "1=INFO", "2=FAIL"], dtype=object),
        reviewer_rows=np.array(["A:van-den-dungen", "B:kitaev"], dtype=object),
        per_clause_agg=np.array([agg["per_clause"][c]["agg"] for c in agg["clause_order"]], dtype=object),
        per_clause_type=np.array([agg["per_clause"][c]["type"] for c in agg["clause_order"]], dtype=object),
        composite=np.array(composite, dtype=object),
        overall_axis_A=np.array(agg["overall_axis"]["A"], dtype=object),
        overall_axis_B=np.array(agg["overall_axis"]["B"], dtype=object),
        info_clauses=np.array(agg["info_clauses"], dtype=object),
        fail_clauses=np.array(agg["fail_clauses"], dtype=object),
        audit_sha256=np.array(audit_sha, dtype=object),
        content_sha256=np.array(content_sha, dtype=object),
        reviewerA_json_sha256=np.array(rev_a_sha, dtype=object),
        reviewerB_json_sha256=np.array(rev_b_sha, dtype=object),
        registry_span_sha256=np.array(reg_span_sha, dtype=object),
        substrate_input_overlap_caveat=np.array(caveat, dtype=object),
    )
    print(f"  wrote {OUT_NPZ.name}")

    # 6. Optional plot
    plotted = maybe_plot(agg)  # (local)
    if plotted:
        print(f"  wrote {OUT_PNG.name}")

    # 7. Build the verdict value payload (no single-quote chars). Encode the
    #    composite, the compact per-clause matrix, the INFO drivers, and the
    #    substrate-input-overlap caveat.
    matrix_str = ";".join(
        f"{c}=A:{agg['per_clause'][c]['A'] or 'NA'}/B:{agg['per_clause'][c]['B'] or 'NA'}"
        f"->{agg['per_clause'][c]['agg']}"
        for c in agg["clause_order"]
    )  # (local)
    info_str = ",".join(agg["info_clauses"]) if agg["info_clauses"] else "none"  # (local)
    fail_str = ",".join(agg["fail_clauses"]) if agg["fail_clauses"] else "none"  # (local)
    value = (
        f"composite={composite};"
        f"overall_A={agg['overall_axis']['A']};overall_B={agg['overall_axis']['B']};"
        f"INFO_clauses={info_str};FAIL_clauses={fail_str};"
        f"matrix[{matrix_str}];"
        f"{caveat}"
    )  # (local)

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)

    # Routing reminder for the orchestrator (per plan §W2-1 PASS/INFO/FAIL_meaning)
    extra_rows = [
        f"# stage2_cross_axis: reviewerA={reviewer_a.get('reviewer')} "
        f"reviewerB={reviewer_b.get('reviewer')} composite={composite}",
        f"# substrate_input_overlap=TRUE (shared s87_w3 npz; OUTPUT-type independence only)",
        f"# routing: composite={composite} -> "
        + ("STAGE-3-PERMANENT (flip atlas-04 K2 + atlas-07 + open-channel-ledger §C K2 + registry)"
           if composite == "PASS"
           else "STAYS-STAGE-1-CANDIDATE; INFO clauses Stage-2-INFO-deferred (single-axis-A-2 s=3 Mellin-pole -> substrate-first Mellin-residue anchor + poleconv-{A|B}; JOINT-1 w0_FW anchor-provenance hygiene)"
           if composite == "INFO"
           else "STAYS-STAGE-1-CANDIDATE; FAILing clause -> S108"),
    ]  # (local)

    print_verdict_payload(composite, value, audit_sha, content_sha, extra_rows=extra_rows)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} (wall {wall:.2f}s) ===")
    # Exit 0 regardless of PASS/FAIL/INFO — verdict is data, not script health.
    return 0


if __name__ == "__main__":
    sys.exit(main())
