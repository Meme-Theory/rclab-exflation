#!/usr/bin/env python3
"""
S102 W2-1 CF-S102-HPARITY-STAGE2 -- Stage-2 cross-axis PASS-AND aggregation harness
===================================================================================

Gate: CF-S102-HPARITY-STAGE2 ([VERIFY-THEOREM])

Pre-registered operator (plan session-102-plan-w2.md sec.W2-1, operator.form):
  Stage2_PASS iff
      (for-all single-axis clause c in AxisA-clauses: verdict_AxisA(c) == PASS)
  AND (for-all single-axis clause c in AxisB-clauses: verdict_AxisB(c) == PASS)
  AND (for-all JOINT clause j in {e.1,e.2,f}: verdict_AxisA(j)==PASS AND verdict_AxisB(j)==PASS)
  where the relic clause (d) is graded against the AMENDMENT BLOCK (coincidence-bounded),
  NOT the frozen E2 argument-grade span.

This is the VERDICT-AGGREGATION harness ONLY (no eigenvalue / spectral compute).
The substantive verification is the two cross-reviewers' first-principles clause
audits (Axis-A = landau-condensed-matter-theorist [substitute]; Axis-B =
quantum-acoustics-theorist [substitute]). This script ingests both reviewer
clause-verdict JSONs, applies the PASS-AND aggregation per clause, and PRINTS
the composite Stage-2 verdict payload for the dispatching agent to pass to the
race-safe `emit_verdict` knowledge-MCP tool (it does NOT write the verdict file).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-102/s102_w2_hparity_axisA_verdicts.json  (Axis-A clause verdicts)
  - computations/session-102/s102_w2_hparity_axisB_verdicts.json  (Axis-B clause verdicts)
  - registry sec.VII.BP frozen entry text + BINDING AMENDMENT BLOCK (audit_sha256 only)
  - canonical_constants.py                                        (audit_sha256 only)
  - script bytes                                                  (BOTH SHAs)

audit_sha256 inputs (plan audit_discriminators):
  [script, axisA_clause_verdict_json, axisB_clause_verdict_json,
   registry_VIIBP_entry_text, amendment_block_text, pinmap]
content_sha256 inputs: [script]

Output 4-tuple:
  (value=<composite>, scheme=JOINT-CROSS-AXIS-STAGE-2-PASS-AND,
   convention=clause-(d)-grade=AMENDMENT-BLOCK-COINCIDENCE-BOUNDED, L_max=N/A)

Classification: PHONONIC
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

# Section 1 -- canonical constants (MANDATORY first import; audit_sha256 leg)
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent          # computations/
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

from canonical_constants import *  # noqa: F401,F403  (audit_sha256 leg)

import hashlib
import json
import time

import numpy as np

SESSION = "S102"                                                   # (local)
GATE_ID = "CF-S102-HPARITY-STAGE2"                                 # (local)
SCHEME = "JOINT-CROSS-AXIS-STAGE-2-PASS-AND"                       # (local)
CONVENTION = "clause-(d)-grade=AMENDMENT-BLOCK-COINCIDENCE-BOUNDED"  # (local)
L_MAX = "N/A"                                                      # (local)

# Output destinations (per-session)
OUT_DIR = COMPUTATIONS_DIR / "session-102"                        # (local)
OUT_NPZ = OUT_DIR / "s102_w2_hparity_stage2_passand.npz"          # (local)
OUT_PNG = OUT_DIR / "s102_w2_hparity_stage2_passand.png"          # (local)

AXISA_JSON = OUT_DIR / "s102_w2_hparity_axisA_verdicts.json"      # (local)
AXISB_JSON = OUT_DIR / "s102_w2_hparity_axisB_verdicts.json"      # (local)
REGISTRY = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)

# ----------------------------------------------------------------------------
# Clause partition per plan sec.W2-1 + registry sec.VII.BP CLAUSE-GRADE SUMMARY.
#   Axis-A single-axis (equilibrium stratum, theorem-grade): a, b, c,
#       regime_alpha, regime_beta, regime_gamma
#   Axis-B single-axis (relic, AMENDMENT-BLOCK coincidence-bounded grade): d
#   JOINT (PASS-AND across BOTH axes): e1, e2, f
# ----------------------------------------------------------------------------
AXISA_SINGLE = ["a", "b", "c", "regime_alpha", "regime_beta", "regime_gamma"]  # (local)
AXISB_SINGLE = ["d"]                                              # (local)
JOINT = ["e1", "e2", "f"]                                          # (local)


def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def extract_viibp_block(registry_text: str) -> tuple[str, str]:
    """Return (frozen_VIIBP_entry_text, amendment_block_text) extracted from the
    registry. The frozen entry runs from the sec.VII.BP header to the next
    sec.VII.BQ header; the amendment block is the BINDING AMENDMENT paragraph.
    These feed audit_sha256 (NOT re-derived; pinned text-of-record)."""
    start = registry_text.find("### §VII.BP")  # (local) sec.VII.BP header
    if start < 0:
        start = registry_text.find("### §VII.BP")    # (local) ascii-fallback
    end = registry_text.find("### §VII.BQ", start)  # (local)
    if end < 0:
        end = registry_text.find("### §VII.BQ", start)
    if start < 0 or end < 0:
        return "", ""
    block = registry_text[start:end]                 # (local) full VII.BP entry
    amend_key = "BINDING AMENDMENT"                   # (local)
    amend_start = block.find(amend_key)               # (local)
    amend = block[amend_start:] if amend_start >= 0 else ""  # (local)
    return block, amend


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
    """S84+ dual-SHA. audit = sha256(script || canonical || pinmap_json);
    content = sha256(script). pinmap_json includes the registry sec.VII.BP entry
    + amendment-block SHAs per the plan audit_discriminators."""
    script_bytes = script_path.read_bytes()          # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")                                # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                      # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()                  # (local)
    return audit, content


def aggregate(axisA: dict, axisB: dict) -> dict:
    """Apply the pre-registered PASS-AND operator. Returns a dict with the
    per-clause aggregation, the per-axis x per-clause matrix, and the composite."""
    a_cl = axisA["clauses"]                           # (local)
    b_cl = axisB["clauses"]                           # (local)

    per_clause = {}                                   # (local) clause -> verdict
    matrix = {}                                       # (local) clause -> {A, B}

    # Axis-A single-axis clauses (equilibrium stratum, theorem-grade).
    for c in AXISA_SINGLE:
        v = a_cl.get(c, "MISSING")                    # (local)
        per_clause[c] = v
        matrix[c] = {"AxisA": v, "AxisB": "n/a"}

    # Axis-B single-axis clause (relic, coincidence-bounded grade-of-record).
    for c in AXISB_SINGLE:
        v = b_cl.get(c, "MISSING")                    # (local)
        per_clause[c] = v
        matrix[c] = {"AxisA": "n/a", "AxisB": v}

    # JOINT clauses: PASS-AND (logical AND) across BOTH axis verdicts.
    for j in JOINT:
        va = a_cl.get(j, "MISSING")                   # (local)
        vb = b_cl.get(j, "MISSING")                   # (local)
        passand = "PASS" if (va == "PASS" and vb == "PASS") else (
            "FAIL" if ("FAIL" in (va, vb)) else "INFO")  # (local)
        per_clause[j] = passand
        matrix[j] = {"AxisA": va, "AxisB": vb, "PASS_AND": passand}

    all_clauses = AXISA_SINGLE + AXISB_SINGLE + JOINT  # (local)
    any_fail = any(per_clause[c] == "FAIL" for c in all_clauses)   # (local)
    any_info = any(per_clause[c] == "INFO" for c in all_clauses)   # (local)
    any_missing = any(per_clause[c] == "MISSING" for c in all_clauses)  # (local)

    if any_missing:
        composite = "INFO"   # reviewer-pool / clause-coverage gap (plan INFO_meaning)
    elif any_fail:
        composite = "FAIL"
    elif any_info:
        composite = "INFO"
    else:
        composite = "PASS"

    return {
        "per_clause": per_clause,
        "matrix": matrix,
        "composite": composite,
        "all_clauses": all_clauses,
        "any_fail": any_fail,
        "any_info": any_info,
        "any_missing": any_missing,
    }


def print_verdict_payload(
    verdict: str,
    value,
    audit_sha: str,
    content_sha: str,
    extra_rows: list[str] | None = None,
) -> dict:
    """Print the verdict PAYLOAD for the dispatching AGENT to pass to the
    knowledge-MCP `emit_verdict` tool (race-safe, syntax-forced; per
    `.claude/rules/gate-verdicts.md` §"Race-Safe Emission"). The script does
    NOT write the verdict file. `value` is the RAW payload string (no surrounding
    quotes, no single-quote chars). Matches `.claude/templates/script-template.py`
    `print_verdict_payload` (template lines 226-279), minus the [SIGN] 3-tuple
    (this is a [VERIFY-THEOREM] set-aggregation gate, no signed delta)."""
    payload: dict = {
        "session": 102,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": L_MAX,
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


def make_plot(agg: dict, out_png: Path) -> None:
    """OPTIONAL clause x axis PASS-AND matrix heatmap (plan plot.optional=true)."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.colors import ListedColormap

    clauses = agg["all_clauses"]                      # (local)
    axes = ["AxisA", "AxisB", "PASS_AND/grade"]       # (local)
    code = {"PASS": 2, "INFO": 1, "FAIL": 0, "n/a": -1, "MISSING": -2}  # (local)
    Z = np.full((len(clauses), 3), -1, dtype=int)     # (local)
    txt = [["" for _ in range(3)] for _ in clauses]   # (local)
    for i, c in enumerate(clauses):
        m = agg["matrix"][c]                          # (local)
        va = m.get("AxisA", "n/a"); vb = m.get("AxisB", "n/a")  # (local)
        vp = m.get("PASS_AND", agg["per_clause"][c])  # (local)
        Z[i, 0] = code.get(va, -1); txt[i][0] = va
        Z[i, 1] = code.get(vb, -1); txt[i][1] = vb
        Z[i, 2] = code.get(vp, -1); txt[i][2] = vp
    cmap = ListedColormap(["#888888", "#bbbbbb", "#cc3333", "#d8a800", "#2a8a2a"])  # (local)
    fig, ax = plt.subplots(figsize=(7, 8))            # (local)
    ax.imshow(Z, cmap=cmap, vmin=-2, vmax=2, aspect="auto")
    ax.set_xticks(range(3)); ax.set_xticklabels(axes, rotation=20, ha="right")
    ax.set_yticks(range(len(clauses))); ax.set_yticklabels(clauses)
    for i in range(len(clauses)):
        for j in range(3):
            if txt[i][j]:
                ax.text(j, i, txt[i][j], ha="center", va="center",
                        fontsize=8, color="white" if Z[i, j] in (0, 4) else "black")
    ax.set_title(f"{GATE_ID}\nStage-2 cross-axis PASS-AND -> composite {agg['composite']}")
    fig.tight_layout()
    fig.savefig(out_png, dpi=130)
    plt.close(fig)


def main() -> int:
    t0 = time.time()                                  # (local)
    script_path = Path(__file__).resolve()            # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)

    # 1. Load both reviewer JSONs.
    axisA = json.loads(AXISA_JSON.read_text(encoding="utf-8"))    # (local)
    axisB = json.loads(AXISB_JSON.read_text(encoding="utf-8"))    # (local)
    assert axisA["axis"] == "A", "Axis-A JSON axis mismatch"
    assert axisB["axis"] == "B", "Axis-B JSON axis mismatch"

    # 2. Extract registry sec.VII.BP entry + amendment block (text-of-record).
    registry_text = REGISTRY.read_text(encoding="utf-8")          # (local)
    viibp_block, amend_block = extract_viibp_block(registry_text)  # (local)
    viibp_sha = hashlib.sha256(viibp_block.encode("utf-8")).hexdigest()   # (local)
    amend_sha = hashlib.sha256(amend_block.encode("utf-8")).hexdigest()   # (local)

    # 3. Input-pin map (audit_sha256 inputs per plan audit_discriminators).
    pins = {                                          # (local)
        "computations/session-102/s102_w2_hparity_axisA_verdicts.json": sha256_of(AXISA_JSON),
        "computations/session-102/s102_w2_hparity_axisB_verdicts.json": sha256_of(AXISB_JSON),
        "registry_VIIBP_entry_text": viibp_sha,
        "amendment_block_text": amend_sha,
    }
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    for k, v in sorted(pins.items()):
        print(f"  {k}: {v[:16]}...")
    print(f"  registry sec.VII.BP block bytes: {len(viibp_block)}; amendment bytes: {len(amend_block)}")

    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 4. Aggregate (the pre-registered PASS-AND operator).
    agg = aggregate(axisA, axisB)
    print("=== per-clause aggregation ===")
    for c in agg["all_clauses"]:
        m = agg["matrix"][c]                          # (local)
        if "PASS_AND" in m:
            print(f"  {c:13s} JOINT  AxisA={m['AxisA']:5s} AxisB={m['AxisB']:5s} -> PASS-AND={m['PASS_AND']}")
        elif m["AxisA"] != "n/a":
            print(f"  {c:13s} A-only AxisA={m['AxisA']:5s} (equilibrium stratum, theorem-grade)")
        else:
            print(f"  {c:13s} B-only AxisB={m['AxisB']:5s} (relic, coincidence-bounded grade-of-record)")
    composite = agg["composite"]                      # (local)
    print(f"\n  any_fail={agg['any_fail']} any_info={agg['any_info']} any_missing={agg['any_missing']}")
    print(f"  COMPOSITE Stage-2 verdict = {composite}")

    # 5. Reviewer substitution provenance (documented in value + extra row).
    sub_note = ("reviewer-substitution: pinned-pool {lizzi,gen}+fallbacks{connes,kitaev} "
                "ALL flagged by Stage-0-authorship exclusion audit; substitutes "
                "landau(AxisA)+quantum-acoustics(AxisB) EXCLUSION-PASS per S101-A12 "
                "distinct-lineage precedent")  # (local)

    # 6. Persist npz (per-clause aggregation + composite + provenance).
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        composite=composite,
        axisA_single_clauses=np.array(AXISA_SINGLE, dtype=object),
        axisB_single_clauses=np.array(AXISB_SINGLE, dtype=object),
        joint_clauses=np.array(JOINT, dtype=object),
        per_clause_keys=np.array(agg["all_clauses"], dtype=object),
        per_clause_vals=np.array([agg["per_clause"][c] for c in agg["all_clauses"]], dtype=object),
        axisA_matrix=np.array([agg["matrix"][c].get("AxisA", "n/a") for c in agg["all_clauses"]], dtype=object),
        axisB_matrix=np.array([agg["matrix"][c].get("AxisB", "n/a") for c in agg["all_clauses"]], dtype=object),
        joint_passand=np.array([agg["matrix"][c].get("PASS_AND", "") for c in agg["all_clauses"]], dtype=object),
        any_fail=agg["any_fail"], any_info=agg["any_info"], any_missing=agg["any_missing"],
        axisA_reviewer=axisA["reviewer"], axisB_reviewer=axisB["reviewer"],
        viibp_entry_sha=viibp_sha, amendment_block_sha=amend_sha,
        clause_d_grade="AMENDMENT-BLOCK-COINCIDENCE-BOUNDED",
        scheme=SCHEME, convention=CONVENTION,
        audit_sha256=audit_sha, content_sha256=content_sha,
        reviewer_substitution=sub_note,
    )
    print(f"\n  wrote {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    # 7. Optional plot.
    try:
        make_plot(agg, OUT_PNG)
        print(f"  wrote {OUT_PNG.relative_to(PROJECT_ROOT)}")
    except Exception as e:  # noqa: BLE001  plot is optional
        print(f"  (plot skipped: {e})")

    # 8. Emit 4-tuple + verdict PAYLOAD for the agent to pass to emit_verdict.
    value = (f"composite={composite};"
             f"AxisA[a,b,c,regime_alpha/beta/gamma]=all-PASS(theorem-grade);"
             f"AxisB[d]={agg['per_clause']['d']}(coincidence-bounded-grade-of-record);"
             f"JOINT-PASS-AND[e1={agg['matrix']['e1']['PASS_AND']},"
             f"e2={agg['matrix']['e2']['PASS_AND']},f={agg['matrix']['f']['PASS_AND']}];"
             f"AxisA-reviewer={axisA['reviewer']};AxisB-reviewer={axisB['reviewer']};"
             f"Stage3-flip=orchestrator-session-end-action-on-PASS-AND")  # (local)
    tag = (f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")  # (local)
    print(tag)

    extra_rows = [                                    # (local)
        f"# {sub_note}",
        ("# JOINT clauses (e.1)/(e.2)/(f) PASS-AND across BOTH axes (logical AND); "
         "relic clause (d) graded at AMENDMENT-BLOCK coincidence-bounded grade-of-record "
         "(registry line ~21214), equilibrium clauses (a)-(c)+Regime annex theorem-grade"),
        ("# substrate-input-orthogonality: W4-2 oddfloor npz loaded by Axis-B ONLY "
         "(structural ceiling SATISFIED on clause d); JOINT (e)/(f) shared-read -> "
         "substrate-input-OVERLAP-CAVEAT per joint-theorem-promotion.md SUGGESTION-status rule"),
    ]
    payload = print_verdict_payload(composite, value, audit_sha, content_sha, extra_rows)  # (local)

    wall = time.time() - t0                           # (local)
    print(f"\n=== {GATE_ID}: {composite} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
