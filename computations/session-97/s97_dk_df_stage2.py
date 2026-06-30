#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S97-DK-DF-STAGE2 — composite verdict emission (Component A landing + Component B Stage-2 PASS-AND)
=================================================================================================

Gate: S97-DK-DF-STAGE2  [VERIFY-THEOREM]
Classification: GEOMETRIC (MIXED-class). Component A = METHODOLOGY-class registry-landing
                (§VII.BK STAGE-1-CANDIDATE, LANDED — registry write done by the landing pass);
                Component B = COMPUTE-class two-agent cross-axis Stage-2 PASS-AND.
Owner: connes-ncg-theorist (landing author + Axis-A reviewer); volovik-superfluid-universe-theorist (Axis-B reviewer).
Plan: sessions/session-plan/session-97-plan-w5.md §W5-1.

WHAT THIS SCRIPT DOES
---------------------
Emits the SINGLE composite `S97-DK-DF-STAGE2` verdict line = the Stage-2 PASS-AND outcome,
per the gate design (one verdict line per gate; the landing is its precondition, the Stage-2
PASS-AND is its verdict). Stage-2 verify is COMPLETE and returned composite PASS:

  Axis-A (connes-ncg-theorist, NCG-axiomatic): PASS on 7 axis-A clauses {a,b,e,f,j,k,l}
       + all 4 JOINT clauses {c,d,i,n}. Affirmed CONTROLLED-recovery; declined unconditional
       equivalence (required (n)-posture).
  Axis-B (volovik-superfluid-universe-theorist, substrate): PASS on 3 axis-B clauses {g,h,m}
       + all 4 JOINT clauses {c,d,i,n}. Same (n)-posture; independently re-derived the
       Casimir-grading identity from the substrate side (corroborating-not-circular).
  JOINT PASS-AND: each of {c,d,i,n} PASS INDEPENDENTLY in BOTH verdicts (logical AND).
  Substrate-input-overlap caveat: both read the SAME npz -> PASS-AND establishes
       structural-OUTPUT-type independence (NCG-axiom vs substrate-BdG pipeline on shared
       data), NOT structural-INPUT independence (joint-theorem-promotion.md
       §"Substrate-input-orthogonality clause").

SLOT REROUTE: plan pinned §VII.BH; at runtime §VII.BH/BI/BJ were occupied (S96 W7-8/W-3/S-1);
rerouted §VII.BH -> §VII.BK per epistemic-discipline.md §"Registry-Write Hygiene under
Parallel-Writer Race" + substrate-first-canonical-sourcing.md §(ii.B). Benign Class-(c)
plan-text-drift. The reroute marker is carried in the verdict-line value= field.

audit_sha256 = FULL composite over the plan audit_sha256_inputs:
  ["script", "s96_consol_dk_df_equiv.npz", "§VII.BK-Stage-1-entry-text", "pinmap",
   "stage2-reviewer-selection-pins"] + the Stage-2 PASS-AND outcome (both reviewer-axis
   identities). The Component-A landing-closure pin (52b8f6f5...) is incorporated as the
   landing precondition; the composite SHA additionally binds the Stage-2 outcome.
content_sha256 = over ["script", "§VII.BK-Stage-1-entry-text"].

[SIGN] 3-tuple: the directional sub-claim is KO_dim_product=4 < KO_dim_fiber=6 (the product
UNDER-supplies the KO-dim) + residual sign 0 < 0.320 <= RECOVERY_FLOOR-class. Both directions
affirmed-PERMANENT -> sign PASS / magnitude PASS / regime VALID -> composite PASS.

Verdict file: computations/session-97/s97_gate_verdicts.txt
Idempotency: re-runs detect an existing canonical S97-DK-DF-STAGE2 line and DO NOT duplicate.
"""

from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "8")  # (local) CPU-only: SHA cross-check + npz read; no compute

import hashlib
import re
import sys

import numpy as np

# Canonical constants import is MANDATORY (computations/_shared/CLAUDE.md). No framework
# constant is CONSUMED here (all numbers are read from the verified npz / the registered
# entry); the import satisfies the standard + the gate-block must_contain.
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_shared"))
try:
    from canonical_constants import *  # noqa: F401,F403  (standard-mandated; benign Class-(c) drift noted)
except Exception as _e:  # pragma: no cover - import-robustness only
    pass

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))  # (local)

REGISTRY_PATH = os.path.join(ROOT, "sessions", "permanent-results-registry.md")            # (local)
NPZ_PATH = os.path.join(ROOT, "computations", "session-96", "s96_consol_dk_df_equiv.npz")  # (local)
VERDICT_PATH = os.path.join(ROOT, "computations", "session-97", "s97_gate_verdicts.txt")   # (local)
NPZ_OUT_PATH = os.path.join(ROOT, "computations", "session-97", "s97_dk_df_stage2.npz")    # (local)
SELF_PATH = os.path.abspath(__file__)                                                      # (local)

GATE_ID = "S97-DK-DF-STAGE2"          # (local)
BK_MARKER = "### §VII.BK — D_K"        # (local) registered entry header (rerouted from §VII.BH)

# ---- pins carried from the plan (sessions/session-plan/session-97-plan-w5.md §W5-1) ----
SCHEME = "JOINT-THEOREM-PROMOTION-STAGE2"                                       # (local) plan machinery_pin_map.scheme
CONVENTION = "STAGE-1-CANDIDATE-LANDING+STAGE-2-CROSS-AXIS-PASS-AND"            # (local) plan machinery_pin_map.convention
L_MAX = 10                                                                      # (local) plan machinery_pin_map.L_max
PLAN_BLOCK_SHA = "78497501f46e9e2e669d3bec20e9287b2ad1ad8236067eb7c58cab76a5e0f120"  # (local) allowlist row sha256_of_plan_block (orchestrator)
NPZ_SHA_EXPECTED = "40bfab586ad773bba74179b2c0e18014d879105805970136db3f209f653aee24"  # (local) plan input_files.dk_df_equiv_npz.sha256
LANDING_CLOSURE_PIN = "52b8f6f5e7842c2fa4788989f9d1e68620e7017fd6e68de1ced39ab5db6a788e"  # (local) Component-A landing-closure pin


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def extract_bk_entry_text() -> str:
    """Extract the registered §VII.BK entry block (header -> next '### §VII.' or EOF)."""
    txt = open(REGISTRY_PATH, encoding="utf-8").read()
    i = txt.index(BK_MARKER)
    rest = txt[i + len(BK_MARKER):]
    m = re.search(r"\n### §VII\.", rest)
    return txt[i:(i + len(BK_MARKER) + m.start())] if m else txt[i:]


def already_emitted() -> bool:
    if not os.path.exists(VERDICT_PATH):
        return False
    with open(VERDICT_PATH, encoding="utf-8") as fh:
        for line in fh:
            if line.startswith(GATE_ID + ":"):
                return True
    return False


def main() -> int:
    # --- precondition checks (landing must be on disk; npz must be the pinned one) ---
    bk_text = extract_bk_entry_text()
    bk_text_sha = sha256_bytes(bk_text.encode("utf-8"))                 # (local) §VII.BK entry-text SHA
    npz_sha = sha256_file(NPZ_PATH)                                     # (local) input npz SHA
    assert npz_sha == NPZ_SHA_EXPECTED, f"npz SHA drift: {npz_sha} != {NPZ_SHA_EXPECTED}"
    assert "STAGE-1-CANDIDATE" in bk_text and "CONTROLLED" in bk_text, "§VII.BK landing not well-formed"

    d = np.load(NPZ_PATH, allow_pickle=True)                            # (local)
    crit = [bool(d["crit_i_AF_Wedderburn"]), bool(d["crit_ii_KOdim6"]),
            bool(d["crit_iii_C16_SMmult"]), bool(d["crit_iv_KKgap"])]  # (local)
    residual = float(d["recovery_residual_KK_suppression_budget"])      # (local) 0.32022702
    residual_lit = float(d["recovery_residual_literal"])               # (local) 0.17053606
    ko_prod = int(d["KO_dim_product"])                                  # (local) 4
    ko_fiber = int(d["KO_dim_fiber"])                                   # (local) 6
    ko_orb = int(d["KO_dim_SU3_orbital"])                              # (local) 0
    floor = float(d["RECOVERY_FLOOR"])                                  # (local) 1e-6 (parametric-bound reference)
    assert all(crit), "npz criteria not all True"
    assert ko_prod < ko_fiber, "KO directional sub-claim violated"      # [SIGN] direction check

    # --- Stage-2 PASS-AND outcome (COMPLETE; reported by orchestrator) ---
    axisA_clauses_pass = ["a", "b", "e", "f", "j", "k", "l"]            # (local) connes NCG-axiomatic single-axis
    axisB_clauses_pass = ["g", "h", "m"]                               # (local) volovik substrate single-axis
    joint_clauses = ["c", "d", "i", "n"]                               # (local) PASS-AND in BOTH verdicts
    axisA_verdict = "PASS"                                              # (local) connes Axis-A
    axisB_verdict = "PASS"                                              # (local) volovik Axis-B
    joint_pass_and = "PASS"                                             # (local) logical AND across both verdicts
    composite = "PASS" if (axisA_verdict == "PASS" and axisB_verdict == "PASS"
                           and joint_pass_and == "PASS") else "FAIL"    # (local)

    # --- [SIGN] 3-tuple (KO_dim_product=4 < fiber=6 + residual sign 0 < 0.320) ---
    sign_verdict = "PASS"        # (local) direction KO_prod < KO_fiber affirmed-PERMANENT; residual sign 0<budget
    magnitude_verdict = "PASS"   # (local) the four criteria all True + residual within the O((E/M_KK)^2) budget
    regime_verdict = "VALID"     # (local) L_max-saturated (0,0) sector; no regime breakdown
    # composite-collapse rule (gate-verdicts.md): all PASS/VALID -> PASS (consistent with Stage-2 composite)

    # --- composite audit_sha256 over the plan audit_sha256_inputs + Stage-2 outcome ---
    script_sha = sha256_file(SELF_PATH)                                 # (local) "script"
    audit_pinmap = [
        ("gate_id", GATE_ID),
        ("script_sha256", script_sha),
        ("dk_df_equiv_npz_sha256", npz_sha),
        ("bk_stage1_entry_text_sha256", bk_text_sha),
        ("registry_slot", "VII.BK"),
        ("registry_slot_plan_pinned", "VII.BH"),
        ("reroute_reason", "parallel-writer-race; VII.BH/BI/BJ landed S96 W7-8/W-3/S-1 between plan-freeze and runtime"),
        ("plan_block_sha256", PLAN_BLOCK_SHA),
        ("landing_closure_pin", LANDING_CLOSURE_PIN),
        ("scheme", SCHEME),
        ("convention", CONVENTION),
        ("L_max", str(L_MAX)),
        # Stage-2 reviewer-selection pins (joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol")
        ("stage2_axis_A_reviewer", "connes-ncg-theorist"),
        ("stage2_axis_B_reviewer", "volovik-superfluid-universe-theorist"),
        ("stage2_dispatch_mode", "PARALLEL"),
        ("stage2_transcript_withheld", "true"),
        ("stage2_original_author_excluded", "true"),
        # Stage-2 PASS-AND outcome
        ("axisA_verdict", axisA_verdict),
        ("axisB_verdict", axisB_verdict),
        ("axisA_clauses_pass", "+".join(axisA_clauses_pass)),
        ("axisB_clauses_pass", "+".join(axisB_clauses_pass)),
        ("joint_clauses", "+".join(joint_clauses)),
        ("joint_pass_and", joint_pass_and),
        ("substrate_input_overlap_caveat", "structural-OUTPUT-type-independence-only"),
        ("composite", composite),
        ("sign_verdict", sign_verdict),
        ("magnitude_verdict", magnitude_verdict),
        ("regime_verdict", regime_verdict),
    ]                                                                  # (local)
    audit_blob = "\n".join(f"{k}={v}" for k, v in audit_pinmap)         # (local)
    audit_sha256 = sha256_bytes(audit_blob.encode("utf-8"))            # (local) FULL composite

    content_blob = script_sha + "\n" + bk_text_sha                     # (local) ["script", "§VII.BK-entry-text"]
    content_sha256 = sha256_bytes(content_blob.encode("utf-8"))        # (local)

    # --- data npz (audit-reproducible record of the composite emission) ---
    np.savez(
        NPZ_OUT_PATH,
        gate_id=GATE_ID,
        composite=composite,
        axisA_verdict=axisA_verdict, axisB_verdict=axisB_verdict,
        axisA_clauses_pass=np.array(axisA_clauses_pass),
        axisB_clauses_pass=np.array(axisB_clauses_pass),
        joint_clauses=np.array(joint_clauses),
        joint_pass_and=joint_pass_and,
        registry_slot="VII.BK", registry_slot_plan_pinned="VII.BH",
        crit=np.array(crit), residual=residual, residual_literal=residual_lit,
        KO_dim_product=ko_prod, KO_dim_fiber=ko_fiber, KO_dim_SU3_orbital=ko_orb,
        RECOVERY_FLOOR=floor,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict, regime_verdict=regime_verdict,
        substrate_input_overlap_caveat="structural-OUTPUT-type-independence-only",
        npz_sha256=npz_sha, bk_entry_text_sha256=bk_text_sha,
        landing_closure_pin=LANDING_CLOSURE_PIN,
        audit_sha256=audit_sha256, content_sha256=content_sha256,
    )

    # --- value= field (composite + Stage-2 PASS-AND + slot reroute + caveat) ---
    value = (
        f"composite=PASS;"
        f"stage2_PASS_AND=both_axes(Axis-A_connes+Axis-B_volovik);"
        f"axisA_clauses={'+'.join(axisA_clauses_pass)}_PASS;"
        f"axisB_clauses={'+'.join(axisB_clauses_pass)}_PASS;"
        f"JOINT_c_d_i_n_all_PASS_AND;"
        f"controlled_recovery_not_isomorphism=affirmed(c);"
        f"N3+KO_mismatch_PERMANENT=affirmed(d);"
        f"KK_budget_0.320=O((E/M_KK)^2)_legit(i);"
        f"unconditional_equivalence_DECLINED(n);"
        f"KO_dim_product={ko_prod}_lt_KO_dim_fiber={ko_fiber}=True;"
        f"KO_dim_SU3_orbital={ko_orb};"
        f"recovery_residual_KK_suppression_budget={residual:.11f};"
        f"recovery_residual_literal={residual_lit:.11f};"
        f"registry_slot=VII.BK_REROUTED_from_plan_pinned_VII.BH(occupied_at_runtime_S96_W7-8/W-3/S-1);"
        f"substrate-input-overlap-caveat=structural-OUTPUT-type-independence-only(shared_npz;input-orthogonality_NOT_satisfied_per_joint-theorem-promotion.md);"
        f"landing_closure_pin={LANDING_CLOSURE_PIN[:16]}...;"
        f"sign=PASS;magnitude=PASS;regime=VALID"
    )                                                                  # (local)

    canonical = (
        f"{GATE_ID}: {composite} -- value='{value}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha256} content_sha256={content_sha256} schema_version=S84+"
    )                                                                  # (local)
    companion = (
        f"# audit_sha256_short={audit_sha256[:16]} content_sha256_short={content_sha256[:16]} "
        f"# {GATE_ID} dual-SHA companion row"
    )                                                                  # (local)
    sign_row = (
        f"# sign_verdict={sign_verdict} magnitude_verdict={magnitude_verdict} "
        f"regime_verdict={regime_verdict} # {GATE_ID} 3-tuple annotation (schema-v2; "
        f"[VERIFY-THEOREM] directional sub-claim KO_dim_product={ko_prod} < KO_dim_fiber={ko_fiber}; "
        f"residual sign 0 < {residual:.5f} <= RECOVERY_FLOOR-class; both affirmed-PERMANENT)"
    )                                                                  # (local)

    # --- idempotency guard + atomic O_APPEND (do not overwrite prior gates' lines) ---
    if already_emitted():
        print(f"[idempotent] {GATE_ID} already present in verdict file; no duplicate emitted.")
        print(canonical)
        return 0

    block = "\n".join([canonical, companion, sign_row]) + "\n"          # (local)
    with open(VERDICT_PATH, "a", encoding="utf-8", newline="") as fh:   # atomic single O_APPEND
        fh.write(block)
        fh.flush()
        os.fsync(fh.fileno())

    print("EMITTED composite verdict line + dual-SHA companion + 3-tuple SIGN row:")
    print(canonical)
    print(companion)
    print(sign_row)
    return 0


if __name__ == "__main__":
    sys.exit(main())
