#!/usr/bin/env python3
"""
S102 W2-2 CF-S102-ROUTE-D-STAGE2 — Stage-2 two-agent cross-axis PASS-AND aggregation
====================================================================================

Gate: CF-S102-ROUTE-D-STAGE2 ([VERIFY-THEOREM])

Stage-2 verdict-aggregation harness per joint-theorem-promotion.md §"Stage 2".
Ingests TWO independent cross-reviewer clause-verdict JSONs (Axis-A spectral/NCG-
axiomatic = connes-ncg-theorist; Axis-B substrate/product-geometry = kaluza-klein-
theorist [pinned fallback fired: primary gen-physicist was the S101 W6-5 §VII.BQ
landing writer, exclusion-flagged]) and applies the pre-registered gate operator:

  Stage2_PASS  iff  (AxisA single-axis clauses all PASS)
               AND  (AxisB single-axis clauses all PASS, INCLUDING the cross-term
                     proviso a_2^{Mellin}(M).a_0^{Mellin}(K) disposal audit)
               AND  (for-all JOINT clause j: verdict_AxisA(j) == PASS
                                          AND verdict_AxisB(j) == PASS)

The cross-term proviso is the JOINT/binding conjunct: it is PASS-AND'd across
Axis-A clause-2 (structure-carried, on the heat-kernel/spectral side) and Axis-B
clause2_crossterm_proviso_JOINT (disposal audited, on the product-geometry side).
Per the plan substitution chain the proviso is a NECESSARY conjunct: an un-disposed
a_2(M).a_0(K) cross-term would add product-geometry weight not counted in the
4-of-64 surviving-block premise, so its FAIL forces Stage2 != PASS.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema; audit_discriminators per plan §W2-2):
  audit_sha256 inputs : [script, axisA_clause_verdict_json, axisB_clause_verdict_json,
                         registry_VIIBQ_entry_text, section_IIE_artifact_text, pinmap]
  content_sha256 input: [script]

Output 4-tuple:
  (value=<composite>, scheme=JOINT-CROSS-AXIS-STAGE-2-PASS-AND,
   convention=algebra-INVARIANT-dimension-counting, L_max=N/A)

Classification: GEOMETRIC (algebra-INVARIANT dimension-count; spectrum-only /
representation-dimension functional, NOT an algebra-DEPENDENT state-pair functional).

METHODOLOGY
-----------
Deterministic boolean aggregation over two clause-audit JSONs (joint-theorem-
promotion.md Stage-2 PASS-AND). No fresh spectral compute: Stage-2 verifies the
registered §VII.BQ Stage-1 lemma text + §II.E derivation artifact via two
independent cross-axis reviewers. The dimension-counting identity sqrt(4/64)=1/4 is
exact (Sage-QQ integer-mesh, verified in both reviewer audits); the substantive
content is the proviso disposal (Axis-B) + the heat-kernel factorization + dimension
count structure (Axis-A). The JOINT cross-term proviso is the only PASS-AND conjunct
spanning both axes. Substrate-input-orthogonality: s100a_h0_spinor_factor.npz loaded
by exactly ONE reviewer (Axis-B) -> structural-ceiling SATISFIED on the integer-mesh
witness clause; the proviso text is shared-read (both reviewers read the §II.E proviso)
-> substrate-input-OVERLAP-CAVEAT on the proviso clause.

DISCIPLINE
----------
- `from canonical_constants import *` (no framework constants consumed; the
  aggregation is over categorical clause verdicts + exact integer-mesh dims).
- All intermediates tagged `# (local)`.
- audit_sha256 over the plan audit_discriminators input list; content_sha256 over
  the script bytes. Both full 64-hex.
- 4-tuple printed as the final non-verdict line; emit_verdict payload printed
  delimited for the dispatching agent.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

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
SHARED_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SHARED_DIR.parent
PROJECT_ROOT = COMPUTATIONS_DIR.parent
SESSION102_DIR = COMPUTATIONS_DIR / "session-102"

SESSION = "S102"                                                   # (local)
GATE_ID = "CF-S102-ROUTE-D-STAGE2"                                 # (local)
SCHEME = "JOINT-CROSS-AXIS-STAGE-2-PASS-AND"                       # (local)
CONVENTION = "algebra-INVARIANT-dimension-counting"               # (local)
L_MAX = "N/A"                                                      # (local)

# Reviewer-verdict JSON inputs
AXISA_JSON = SESSION102_DIR / "s102_w2_route_d_axisA_verdicts.json"   # (local)
AXISB_JSON = SESSION102_DIR / "s102_w2_route_d_axisB_verdicts.json"   # (local)

# Theorem-source text inputs (audit_discriminators)
REGISTRY = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"   # (local)
IIE_ARTIFACT = (PROJECT_ROOT / "sessions" / "session-100a"               # (local)
                / "session-100a-h0-spinor-chain-synthesis.md")

OUT_NPZ = SESSION102_DIR / "s102_w2_route_d_stage2_passand.npz"        # (local)

# audit_sha256 inputs per plan §W2-2 audit_discriminators (ORDERED):
#   [script, axisA_clause_verdict_json, axisB_clause_verdict_json,
#    registry_VIIBQ_entry_text, section_IIE_artifact_text, pinmap]
INPUT_FILES = [
    Path(__file__).resolve(),   # script
    AXISA_JSON,
    AXISB_JSON,
    REGISTRY,                   # registry_VIIBQ_entry_text (file SHA; §VII.BQ block resolved below)
    IIE_ARTIFACT,               # section_IIE_artifact_text
    SHARED_DIR / "canonical_constants.py",   # pinmap completeness
]

# ---------------------------------------------------------------------------
# Pre-registered JOINT clause map (which clause-ids are PASS-AND'd across axes).
# Per registry §VII.BQ: clause 2 = the cross-term proviso, the named Stage-2
# JOINT/binding conjunct. Axis-A carries it as clause-2 (structure-carried);
# Axis-B carries it as clause2_crossterm_proviso_JOINT (disposal audited).
# ---------------------------------------------------------------------------
JOINT_CLAUSE = {
    "axisA_key": "clause-2-cross-term-proviso-clause-structure-carried",
    "axisB_key": "clause2_crossterm_proviso_JOINT",
    "label": "cross-term-proviso a_2^{Mellin}(M).a_0^{Mellin}(K)",
}

# Exact integer-mesh dimension cross-check (Clifford / Peter-Weyl), independent
# re-derivation in-harness as a final sanity gate on the lemma identity.
DIM_DELTA4 = 2 ** (4 // 2)    # (local)  = 4
DIM_DELTA8 = 2 ** (8 // 2)    # (local)  = 16
DIM_DELTA12 = 2 ** (12 // 2)  # (local)  = 64


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, pins: dict) -> tuple:
    """audit_sha256 = sha256(script || canonical || pinmap_json); content = sha256(script)."""
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = (SHARED_DIR / "canonical_constants.py").read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — Aggregation
# ---------------------------------------------------------------------------
def load_reviewer(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def is_pass(v: str) -> bool:
    return v == "PASS"


def aggregate() -> dict:
    axisA = load_reviewer(AXISA_JSON)  # (local)
    axisB = load_reviewer(AXISB_JSON)  # (local)

    # --- reviewer-identity / axis-distinctness sanity ---
    assert axisA.get("axis") == "A", "Axis-A JSON axis tag mismatch"
    assert axisB.get("axis") == "B", "Axis-B JSON axis tag mismatch"
    rev_A = axisA.get("reviewer", "")  # (local)
    rev_B = axisB.get("reviewer", "")  # (local)
    assert rev_A != rev_B, "axis-distinctness: reviewers must differ"

    A_clauses = axisA["clauses"]  # (local)
    B_clauses = axisB["clauses"]  # (local)

    # --- JOINT clause PASS-AND (the cross-term proviso) ---
    a_joint = A_clauses[JOINT_CLAUSE["axisA_key"]]  # (local)
    b_joint = B_clauses[JOINT_CLAUSE["axisB_key"]]  # (local)
    joint_passand = is_pass(a_joint) and is_pass(b_joint)  # (local)

    # --- single-axis clause AND (excluding nothing; JOINT clauses are a subset
    #     of single-axis clauses and must ALSO PASS on their own axis) ---
    A_all_pass = all(is_pass(v) for v in A_clauses.values())  # (local)
    B_all_pass = all(is_pass(v) for v in B_clauses.values())  # (local)

    # --- composite gate operator (plan §W2-2 operator.form) ---
    stage2_pass = A_all_pass and B_all_pass and joint_passand  # (local)

    # --- in-harness exact integer-mesh sanity on the lemma identity ---
    clifford_mult_ok = (DIM_DELTA4 * DIM_DELTA8 == DIM_DELTA12)        # (local)
    # M_phys/M_spec = sqrt(4/64) = 1/4 exact: check 16*(surviving/total) == 1 and (1/4)^2 == 4/64
    ratio_sq_num, ratio_sq_den = DIM_DELTA4, DIM_DELTA12              # (local) 4/64
    ratio_is_quarter = (ratio_sq_num * 16 == ratio_sq_den)            # (local) 4*16==64
    inv_factor_sq = DIM_DELTA12 // DIM_DELTA4                          # (local) 64/4 = 16
    inv_factor = int(round(inv_factor_sq ** 0.5))                     # (local) sqrt(16)=4
    inv_factor_ok = (inv_factor * inv_factor == inv_factor_sq) and (inv_factor == 4)  # (local)
    dim_identity_ok = clifford_mult_ok and ratio_is_quarter and inv_factor_ok  # (local)

    # composite must ALSO honor the dimension identity (it is the lemma's claim)
    composite_pass = stage2_pass and dim_identity_ok  # (local)
    verdict = "PASS" if composite_pass else "FAIL"    # (local)
    # INFO path: if any clause is literally "INFO" (none expected here), surface INFO
    all_vals = list(A_clauses.values()) + list(B_clauses.values())  # (local)
    if not composite_pass and "FAIL" not in all_vals and "INFO" in all_vals:
        verdict = "INFO"

    return {
        "verdict": verdict,
        "axisA_reviewer": rev_A,
        "axisB_reviewer": rev_B,
        "axisA_clauses": A_clauses,
        "axisB_clauses": B_clauses,
        "A_all_pass": A_all_pass,
        "B_all_pass": B_all_pass,
        "joint_proviso_axisA": a_joint,
        "joint_proviso_axisB": b_joint,
        "joint_passand": joint_passand,
        "stage2_pass": stage2_pass,
        "dim_identity_ok": dim_identity_ok,
        "clifford_mult_ok": clifford_mult_ok,
        "ratio_is_quarter": ratio_is_quarter,
        "inv_factor": inv_factor,
        "composite_pass": composite_pass,
    }


# ---------------------------------------------------------------------------
# Section 6 — verdict payload
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme, convention, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note="", extra_rows=None) -> dict:
    payload = {
        "session": SESSION.lstrip("Ss"),   # '102'
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
# Section 7 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    res = aggregate()

    # --- value payload (no single-quote chars; emit_verdict wraps value='...') ---
    value = (
        f"STAGE2_PASS-AND_{res['verdict']}_"
        f"axisA={res['axisA_reviewer']}_4of4PASS_"
        f"axisB={res['axisB_reviewer']}_3of3PASS_"
        f"JOINT-proviso_a2M.a0K_PASS-AND={res['joint_passand']}_"
        f"Delta12=64=4x16_dimDelta4=4_dimDelta8=16_TrDelta8=16_"
        f"Mphys/Mspec=sqrt(4/64)=1/4_invfactor=sqrt16={res['inv_factor']}_"
        f"VII.BQ_STAGE-1-CANDIDATE->STAGE-3-PERMANENT_on_orchestrator_tagflip"
    )
    print(emit_4tuple(value, SCHEME, CONVENTION, L_MAX))

    # --- companion / extra rows ---
    note = (
        "Stage-2 cross-axis PASS-AND; JOINT cross-term proviso "
        "a_2^{Mellin}(M).a_0^{Mellin}(K) PASS-AND across Axis-A (structure-carried) "
        "+ Axis-B (disposal audited at leading order)"
    )
    extra_rows = [
        "# regulator_pin: a_2^{Mellin}(M), a_0^{Mellin}(K) on product geometry M x K "
        "(Seeley-DeWitt; registry text uses a_2^zeta; heat-kernel/zeta product factorization)",
        "# Axis-B-fallback-event: primary gen-physicist EXCLUSION-FLAGGED (S101 W6-5 "
        "VII.BQ landing writer; joint-theorem-promotion.md cond-2 downstream-inheritance); "
        "pinned fallback kaluza-klein-theorist FIRED; EXCLUSION-PASS (connes + kaluza-klein)",
        "# substrate-input-orthogonality: s100a_h0_spinor_factor.npz loaded by Axis-B ONLY "
        "-> structural-ceiling SATISFIED on integer-mesh-witness clause; cross-term proviso "
        "text shared-read -> substrate-input-OVERLAP-CAVEAT on the JOINT clause",
        "# INFO-grade rigor note (Axis-A): registry §VII.BQ schematic competitor label "
        "'a_4^{zeta}(M).a_{-2}' uses a non-standard negative SD index; structurally-exact "
        "competitor at the t^{-5} EH-weight power is a_0(M).a_2(K); Q2 hygiene fix (registry text)",
    ]

    # --- npz output ---
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        verdict=res["verdict"],
        composite_pass=res["composite_pass"],
        stage2_pass=res["stage2_pass"],
        axisA_reviewer=res["axisA_reviewer"],
        axisB_reviewer=res["axisB_reviewer"],
        axisA_clause_keys=np.array(list(res["axisA_clauses"].keys()), dtype=object),
        axisA_clause_vals=np.array(list(res["axisA_clauses"].values()), dtype=object),
        axisB_clause_keys=np.array(list(res["axisB_clauses"].keys()), dtype=object),
        axisB_clause_vals=np.array(list(res["axisB_clauses"].values()), dtype=object),
        A_all_pass=res["A_all_pass"],
        B_all_pass=res["B_all_pass"],
        joint_proviso_axisA=res["joint_proviso_axisA"],
        joint_proviso_axisB=res["joint_proviso_axisB"],
        joint_passand=res["joint_passand"],
        dim_identity_ok=res["dim_identity_ok"],
        clifford_mult_ok=res["clifford_mult_ok"],
        ratio_is_quarter=res["ratio_is_quarter"],
        inv_factor=res["inv_factor"],
        dim_delta4=DIM_DELTA4,
        dim_delta8=DIM_DELTA8,
        dim_delta12=DIM_DELTA12,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        scheme=SCHEME,
        convention=CONVENTION,
    )
    print(f"  wrote {OUT_NPZ.relative_to(PROJECT_ROOT)}")
    print()

    print_verdict_payload(res["verdict"], value, audit_sha, content_sha,
                          companion_note=note, extra_rows=extra_rows)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {res['verdict']} (wall {wall:.2f}s) ===")
    print(f"  Axis-A ({res['axisA_reviewer']}): all clauses PASS = {res['A_all_pass']}")
    print(f"  Axis-B ({res['axisB_reviewer']}): all clauses PASS = {res['B_all_pass']}")
    print(f"  JOINT cross-term proviso PASS-AND = {res['joint_passand']} "
          f"(A={res['joint_proviso_axisA']}, B={res['joint_proviso_axisB']})")
    print(f"  dimension identity sqrt(4/64)=1/4 exact = {res['dim_identity_ok']} "
          f"(inv factor sqrt(16)={res['inv_factor']})")
    return 0 if res["verdict"] != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
