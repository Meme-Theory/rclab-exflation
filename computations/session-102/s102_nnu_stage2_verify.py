#!/usr/bin/env python3
# ---------------------------------------------------------------------------
# S102-NNU-STAGE2-VERIFY — aggregation harness (gate primary executor)
#
# Stage-2 two-agent parallel cross-axis independent-verify per
# joint-theorem-promotion.md §"Stage 2".  Ingests BOTH reviewer clause-verdict
# JSONs and applies the PASS-AND gate operator:
#
#   PASS iff (reviewer_A PASSes {b, d})
#        AND (reviewer_B PASSes {f, g})
#        AND (clause a PASSes in BOTH)
#        AND (clause c PASSes in BOTH)
#        AND (clause e PASSes in BOTH)            [logical AND across all, NOT OR]
#
# This script makes NO new sign/direction/threshold claim of its own — it
# adjudicates whether the registered §VII.BS theorem-tag's clauses survive
# independent cross-axis review (the directional content lives in clauses
# (a)/(d), re-verified FROM FIRST PRINCIPLES by the two reviewers in their
# JSONs, NOT transcribed here).
#
# Substrate framing (GEOMETRIC): the theorem verifies a structural claim about
# the FABRIC's normalization structure — D_K eigenvalues -> a_n spectral moments
# -> dimensionless shapes (the protected Ohat) -> measurement, with M_KK the one
# externally-calibrated dimensional scale entering as the multiplicative w in
# O = w * Ohat.  The gate is the cross-axis adjudication that this O = w * Ohat
# factorization (and its rank-1 covariance signature) is structurally robust.
# ---------------------------------------------------------------------------

# Section 1 — canonical constants (MANDATORY)
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str((_Path(__file__).resolve().parent.parent / "_shared")))
from canonical_constants import *  # noqa: F401,F403

# Section 2 — standard imports
import hashlib
import json
import time

import numpy as np

# Section 3 — paths + identity
SESSION_DIR = _Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S102"                                        # (local)
GATE_ID = "S102-NNU-STAGE2-VERIFY"                      # (local)
SCHEME = "STAGE-2-TWO-AGENT-PARALLEL-CROSS-AXIS"        # (local) plan machinery_pin_map.scheme
CONVENTION = "JOINT-CLAUSES-PASS-AND"                   # (local) plan machinery_pin_map.convention
L_MAX = "N/A"                                           # (local) L-independent Level-1 identity verify

# Inputs (plan §W1-4 input_files / audit_discriminators)
CANONICAL = SHARED_DIR / "canonical_constants.py"                            # (local)
REGISTRY = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"      # (local)
S44_NPZ = PROJECT_ROOT / "computations" / "session-44" / "s44_n3_bdg.npz"   # (local) clause-(b) anchor (A-only leg)
COV_NPZ = SESSION_DIR / "s102_nnu_falsifier_ii_rank1_covariance.npz"        # (local) clause-(a) anchor (B-only leg)
REVIEWER_A_JSON = SESSION_DIR / "s102_nnu_stage2_axisA_verdicts.json"        # (local)
REVIEWER_B_JSON = SESSION_DIR / "s102_nnu_stage2_axisB_verdicts.json"        # (local)

# Pinned canonical SHA (plan §W1-4 input_files.canonical_constants.sha256)
CANONICAL_SHA_PIN = "9f2fe9983ecbbb76a2ba1b3e951cf9275deda8d7f2241576ef23b7f728ba1047"  # (local)

# §VII.BS block extraction anchor (the registered Stage-1 entry being verified)
BS_HEADER_ANCHOR = "### §VII.BS — Normalization Non-Universality"           # (local)

# Gate operator pin (plan operator.form) — clause routing
AXIS_A_SINGLE = ("b", "d")          # (local) connes single-axis clauses
AXIS_B_SINGLE = ("f", "g")          # (local) transit single-axis clauses
JOINT_CLAUSES = ("a", "c", "e")     # (local) PASS-AND across BOTH verdicts

# Exclusion-audit result (run pre-dispatch by orchestrator)
EXCLUSION_AUDIT_RESULT = "EXCLUSION-PASS"                          # (local)
REVIEWERS = ("connes-ncg-theorist", "transit-dynamics-theorist")  # (local) A, B
FALLBACK_FIRED = {"axis_A": False, "axis_B": False}               # (local) none fired

# Output destinations
OUT_NPZ = SESSION_DIR / "s102_nnu_stage2_verify.npz"
OUT_PNG = SESSION_DIR / "s102_nnu_stage2_verify.png"


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block + dual-SHA (plan audit_discriminators)
#   audit_sha256_inputs: [script, registry_stage1_entry_sha, reviewer_A_verdict_sha,
#                         reviewer_B_verdict_sha, pinmap]
#   content_sha256_inputs: [script]
# ---------------------------------------------------------------------------
def sha256_of_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def sha256_of(path: _Path) -> str:
    try:
        return sha256_of_bytes(path.read_bytes())
    except OSError:
        return ""


def extract_bs_block(registry_text: str) -> str:
    """Byte-extract the §VII.BS registry block: header -> next top-level '### ' header."""
    i = registry_text.find(BS_HEADER_ANCHOR)  # (local)
    if i < 0:
        raise RuntimeError("§VII.BS header anchor not found in registry")
    j = registry_text.find("\n### ", i + len(BS_HEADER_ANCHOR))  # (local)
    if j < 0:
        j = len(registry_text)
    return registry_text[i:j]


def closure_hash(pins: dict) -> str:
    """SHA-256 over the ordered (sorted) input-pin map (legacy closure form)."""
    h = hashlib.sha256()  # (local)
    for k, v in sorted(pins.items()):
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: _Path, bs_block_sha: str,
                     rev_a_sha: str, rev_b_sha: str, pins: dict) -> tuple:
    """audit_sha256 = sha256(script || bs_block_sha || rev_a_sha || rev_b_sha || pinmap_json);
       content_sha256 = sha256(script).  Matches plan audit_discriminators exactly."""
    script_bytes = script_path.read_bytes() if script_path.exists() else b""   # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(bs_block_sha.encode("utf-8"))
    h_audit.update(rev_a_sha.encode("utf-8"))
    h_audit.update(rev_b_sha.encode("utf-8"))
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256(script_bytes)  # (local)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — ingest the two reviewer JSONs (on-disk truth)
# ---------------------------------------------------------------------------
def load_reviewer(path: _Path, expect_axis: str, expect_clauses: set) -> dict:
    d = json.loads(path.read_text(encoding="utf-8"))  # (local)
    assert d["axis"] == expect_axis, f"{path.name}: axis {d['axis']} != {expect_axis}"
    have = set(d["clauses"].keys())  # (local)
    assert have == expect_clauses, f"{path.name}: clause set {sorted(have)} != {sorted(expect_clauses)}"
    return d


# ---------------------------------------------------------------------------
# Section 6 — gate operator (PASS-AND; non-numerical adjudication)
# ---------------------------------------------------------------------------
def evaluate_gate(rev_a: dict, rev_b: dict) -> dict:
    """PASS-AND over the two reviewer clause-verdicts per the plan operator.form.

    PASS iff (A PASSes {b,d}) AND (B PASSes {f,g}) AND each JOINT clause (a,c,e) PASSes in BOTH.
    Any clause FAIL -> composite FAIL; any clause INFO (with no FAIL) -> composite INFO.
    """
    ca = rev_a["clauses"]  # (local)
    cb = rev_b["clauses"]  # (local)

    # Axis-A single-axis clauses (b, d): must be PASS in reviewer A
    axis_a_single = {k: ca[k] for k in AXIS_A_SINGLE}                      # (local)
    # Axis-B single-axis clauses (f, g): must be PASS in reviewer B
    axis_b_single = {k: cb[k] for k in AXIS_B_SINGLE}                      # (local)
    # JOINT clauses (a, c, e): must be PASS in BOTH verdicts (logical AND)
    joint = {k: {"A": ca[k], "B": cb[k]} for k in JOINT_CLAUSES}          # (local)
    joint_pass_and = {k: (ca[k] == "PASS" and cb[k] == "PASS")
                      for k in JOINT_CLAUSES}                              # (local)

    # Collect every clause-verdict that participates in the gate
    all_verdicts = (
        list(axis_a_single.values())
        + list(axis_b_single.values())
        + [ca[k] for k in JOINT_CLAUSES]
        + [cb[k] for k in JOINT_CLAUSES]
    )  # (local)

    any_fail = any(v == "FAIL" for v in all_verdicts)   # (local)
    any_info = any(v == "INFO" for v in all_verdicts)   # (local)
    all_pass = all(v == "PASS" for v in all_verdicts)   # (local)

    if any_fail:
        composite = "FAIL"   # (local) — a clause FAILed in some reviewer -> promotion BLOCKED
    elif any_info:
        composite = "INFO"   # (local) — a clause is INFO (ambiguous) -> Stage-2-INFO-deferred
    else:
        assert all_pass
        composite = "PASS"   # (local) — every clause PASSes in its required reviewer(s)

    return {
        "composite": composite,
        "axis_a_single": axis_a_single,
        "axis_b_single": axis_b_single,
        "joint": joint,
        "joint_pass_and": joint_pass_and,
        "all_pass": all_pass,
        "any_fail": any_fail,
        "any_info": any_info,
    }


# ---------------------------------------------------------------------------
# Section 7 — verdict payload (script PRINTS; AGENT calls emit_verdict)
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
                          companion_note: str = "", extra_rows=None) -> dict:
    payload = {
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
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 8 — plot (clause x reviewer PASS-AND matrix; OPTIONAL per plan)
# ---------------------------------------------------------------------------
def make_plot(rev_a: dict, rev_b: dict, g: dict) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    clauses = ["a", "b", "c", "d", "e", "f", "g"]                      # (local)
    rows = ["A (connes/spectral)", "B (transit/cosmo)"]               # (local)
    # value grid: 1=PASS, 0=FAIL, 0.5=INFO, nan=not-audited-by-this-reviewer
    code = {"PASS": 1.0, "INFO": 0.5, "FAIL": 0.0}                    # (local)
    grid = np.full((2, len(clauses)), np.nan)                        # (local)
    for ci, c in enumerate(clauses):
        if c in rev_a["clauses"]:
            grid[0, ci] = code[rev_a["clauses"][c]]
        if c in rev_b["clauses"]:
            grid[1, ci] = code[rev_b["clauses"][c]]

    fig, ax = plt.subplots(figsize=(9, 3.2))
    masked = np.ma.masked_invalid(grid)                              # (local)
    cmap = plt.cm.RdYlGn.copy()                                     # (local)
    cmap.set_bad(color="0.85")
    ax.imshow(masked, cmap=cmap, vmin=0, vmax=1, aspect="auto")
    ax.set_xticks(range(len(clauses)))
    ax.set_xticklabels([f"({c})" for c in clauses])
    ax.set_yticks(range(2))
    ax.set_yticklabels(rows)
    for ri in range(2):
        for ci, c in enumerate(clauses):
            if not np.isnan(grid[ri, ci]):
                lbl = {1.0: "PASS", 0.5: "INFO", 0.0: "FAIL"}[grid[ri, ci]]  # (local)
                tag = " (JOINT)" if c in JOINT_CLAUSES else ""             # (local)
                ax.text(ci, ri, lbl, ha="center", va="center", fontsize=8,
                        fontweight="bold" if c in JOINT_CLAUSES else "normal")
                ax.text(ci, ri + 0.30, tag, ha="center", va="center", fontsize=6, color="0.2")
    ax.set_title(
        f"{GATE_ID}: clause x reviewer PASS-AND matrix\n"
        f"composite = {g['composite']}  |  JOINT (a,c,e) PASS-AND in BOTH = "
        f"{all(g['joint_pass_and'].values())}  |  exclusion = {EXCLUSION_AUDIT_RESULT}",
        fontsize=9,
    )
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 9 — main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)
    print(f"=== {GATE_ID} — Stage-2 two-agent parallel cross-axis verify (aggregation) ===")

    # 1. Sanity-pin the canonical constants file (plan input pin)
    canon_sha = sha256_of(CANONICAL)  # (local)
    print(f"  canonical_constants.py: {canon_sha[:16]}... "
          f"(pin match: {canon_sha == CANONICAL_SHA_PIN})")

    # 2. Extract the §VII.BS registry block + its SHA (the registered entry being verified)
    reg_text = REGISTRY.read_text(encoding="utf-8")  # (local)
    bs_block = extract_bs_block(reg_text)            # (local)
    bs_block_sha = sha256_of_bytes(bs_block.encode("utf-8"))  # (local)
    print(f"  §VII.BS block: len={len(bs_block)} sha={bs_block_sha[:16]}... (registered Stage-1 entry)")

    # 3. Reviewer JSON SHAs (the two cross-axis verdict files; substrate-input-orthogonality legs)
    rev_a_sha = sha256_of(REVIEWER_A_JSON)  # (local)
    rev_b_sha = sha256_of(REVIEWER_B_JSON)  # (local)
    print(f"  reviewer_A (axisA) sha: {rev_a_sha[:16]}...")
    print(f"  reviewer_B (axisB) sha: {rev_b_sha[:16]}...")

    # 4. Ingest both reviewer clause-verdicts (on-disk truth; schema-asserted)
    rev_a = load_reviewer(REVIEWER_A_JSON, "A", set(AXIS_A_SINGLE) | set(JOINT_CLAUSES))  # {b,d,a,c,e}
    rev_b = load_reviewer(REVIEWER_B_JSON, "B", set(AXIS_B_SINGLE) | set(JOINT_CLAUSES))  # {f,g,a,c,e}
    print(f"  reviewer_A clauses: {rev_a['clauses']}")
    print(f"  reviewer_B clauses: {rev_b['clauses']}")

    # 5. Substrate-input-orthogonality witness (structural ceiling): S44 npz loaded by A-leg only;
    #    covariance npz the B-leg only. We RECORD the SHAs (not re-derive) for the audit trail.
    s44_sha = sha256_of(S44_NPZ)  # (local)
    cov_sha = sha256_of(COV_NPZ)  # (local)
    print(f"  substrate-input-orthogonality: S44 npz (A-only leg) {s44_sha[:16]}...; "
          f"covariance npz (B-only leg) {cov_sha[:16]}...  -> DISJOINT data, STRUCTURAL CEILING")

    # 6. Apply the gate operator (PASS-AND)
    g = evaluate_gate(rev_a, rev_b)  # (local)
    composite = g["composite"]       # (local)
    print(f"  axis_A single (b,d): {g['axis_a_single']}")
    print(f"  axis_B single (f,g): {g['axis_b_single']}")
    print(f"  JOINT (a,c,e) per-reviewer: {g['joint']}")
    print(f"  JOINT_pass_and vector: {g['joint_pass_and']}")
    print(f"  COMPOSITE: {composite}")

    # 7. Build the audit input-pin map (the legacy-closure pins; dual-SHA folds these per the plan)
    pins = {
        "computations/session-102/s102_nnu_stage2_verify.py": "<script-self>",
        "registry_stage1_entry_§VII.BS_block_sha": bs_block_sha,
        "reviewer_A_verdict_sha": rev_a_sha,
        "reviewer_B_verdict_sha": rev_b_sha,
        "canonical_constants_sha": canon_sha,
        "scheme": SCHEME,
        "convention": CONVENTION,
    }  # (local)
    closure = closure_hash(pins)  # (local)
    print(f"  legacy closure: {closure[:16]}... (informational)")

    # 8. Dual SHA (plan audit_discriminators: script||bs_block_sha||rev_a_sha||rev_b_sha||pinmap)
    script_path = _Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, bs_block_sha, rev_a_sha, rev_b_sha, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")

    # 9. Record everything to npz (plan output_artifacts.data fields)
    OUT_NPZ.parent.mkdir(parents=True, exist_ok=True)
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        composite=composite,
        reviewer_A_clause_verdicts=json.dumps(rev_a["clauses"]),
        reviewer_B_clause_verdicts=json.dumps(rev_b["clauses"]),
        reviewer_A_name=rev_a["reviewer"],
        reviewer_B_name=rev_b["reviewer"],
        axis_A_single_clauses=json.dumps(g["axis_a_single"]),
        axis_B_single_clauses=json.dumps(g["axis_b_single"]),
        JOINT_clauses_per_reviewer=json.dumps(g["joint"]),
        JOINT_pass_and_vector=json.dumps(g["joint_pass_and"]),
        all_joint_pass_and=bool(all(g["joint_pass_and"].values())),
        exclusion_audit_result=EXCLUSION_AUDIT_RESULT,
        reviewers=json.dumps(list(REVIEWERS)),
        fallback_fired_flags=json.dumps(FALLBACK_FIRED),
        any_fail=bool(g["any_fail"]),
        any_info=bool(g["any_info"]),
        all_pass=bool(g["all_pass"]),
        bs_block_sha=bs_block_sha,
        reviewer_A_verdict_sha=rev_a_sha,
        reviewer_B_verdict_sha=rev_b_sha,
        s44_npz_sha=s44_sha,
        covariance_npz_sha=cov_sha,
        substrate_input_orthogonality="STRUCTURAL-CEILING-DISJOINT-DATA",
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=str(L_MAX),
    )
    print(f"  npz written: {OUT_NPZ.name}")

    # 10. Plot (optional)
    try:
        make_plot(rev_a, rev_b, g)
        print(f"  png written: {OUT_PNG.name}")
    except Exception as e:  # noqa: BLE001
        print(f"  (plot skipped: {e})")

    # 11. Verdict payload — companion + extra rows carry the cross-axis adjudication detail
    joint_summary = ",".join(
        f"{k}:A={g['joint'][k]['A']}/B={g['joint'][k]['B']}" for k in JOINT_CLAUSES
    )  # (local)
    companion = (
        f"PASS-AND over 2 reviewers; A{{b,d}}+B{{f,g}}+JOINT(a,c,e) in BOTH; "
        f"exclusion={EXCLUSION_AUDIT_RESULT}; fallbacks=none; "
        f"substrate-input-orthogonality=STRUCTURAL-CEILING"
    )  # (local)
    extra_rows = [
        f"# STAGE2-CROSS-AXIS: reviewer_A=connes-ncg-theorist(spectral) clauses{rev_a['clauses']} "
        f"reviewer_B=transit-dynamics-theorist(transit/cosmo) clauses{rev_b['clauses']}",
        f"# JOINT-PASS-AND: {joint_summary}  all_joint_pass_and={all(g['joint_pass_and'].values())}",
        f"# substrate-input-orthogonality: S44_npz=A-only-leg covariance_npz=B-only-leg "
        f"-> DISJOINT data (structural ceiling, no overlap caveat)",
        f"# Stage-3 note: this PASS-AND is ONE of three Stage-3-PERMANENT criteria "
        f"(item-2 FAIL + item-3 sustained |Corr|=1 are the other two); the tag flip is the "
        f"orchestrator session-end action, NOT this gate",
    ]  # (local)
    print_verdict_payload(composite, f"composite={composite}", audit_sha, content_sha,
                          companion_note=companion, extra_rows=extra_rows)

    print(f"  elapsed: {time.time() - t0:.2f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
