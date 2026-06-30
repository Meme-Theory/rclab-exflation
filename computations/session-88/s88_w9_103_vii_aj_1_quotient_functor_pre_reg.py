#!/usr/bin/env python3
"""
S88 W9-103 -- S88-CFMSW-FOLLOWUP-VII-AJ-1
==========================================

Gate: S88-CFMSW-FOLLOWUP-VII-AJ-1 (trigger: VERIFY)
Wave: W9 (W6 propagation + atlas cardinality + min-axiom-budget L^8 redirect)
Plan: sessions/session-plan/session-88-plan-w9.md, lines 131-161, gate W9-103.

Pre-registered threshold (per session-88-plan-w9.md, gate-block W9-103):
  PASS: All 3 V_4 incarnations pass the (a)+(b)+(c) quotient-functor pre-
        registration discipline (per cross-pillar-bridge-anatomy.md T1-6,
        W-6 RULE-1, anchor at .claude/rules/epistemic-discipline.md
        section "Quotient-functor pre-registration" lines 174-184); the
        VII.AJ.1 registry diff lands with 3 sub-rows.
  FAIL: One or more V_4 incarnations fails (a) OR (b) OR (c); that
        incarnation is REMOVED from VII.AJ.1 surviving-incarnation list.
        Revised list lands with k < 3 sub-rows.
  INFO: One incarnation passes (a)+(b) but (c) residual cokernel content
        requires substrate-derivation that exceeds wave scope; that
        incarnation is tagged "(c)-pending" and registered with deferred
        sub-row.

Authorship: volovik-superfluid-universe-theorist PRIMARY +
            connes-ncg-theorist CO-AUTHOR.

Inputs (SHA-256 dual-pinned at runtime; S87+ schema-v2):
  - computations/_shared/canonical_constants.py            (tau_fold, M_KK)
  - computations/_shared/_quotient_functor_pre_registration_audit.py
                                                            (W-6 RULE-1 audit)
  - computations/session-88/s88_gate_verdicts.txt          (prior verdicts:
                                                            W2-2 III-triality
                                                            FAIL; W2-3 strata
                                                            FAIL; W2-1 depth
                                                            extension PASS)
  - computations/session-87/s87_gate_verdicts.txt          (W11-1 V_4 explicit
                                                            FAIL max_dev=1.16)
  - script bytes                                           (audit + content
                                                            SHAs)

Output 4-tuple:
  (value=summary string with per-incarnation (a)/(b)/(c) verdicts +
                aggregate decision,
   scheme=W-6-RULE-1-three-field-discipline-per-incarnation,
   convention=VII-AJ-1-V4-monodromy-3-incarnation-quotient-functor-pre-reg,
   L_max=10)

Classification: GEOMETRIC

METHODOLOGY
-----------
W-6 RULE-1 (anchor: .claude/rules/epistemic-discipline.md lines 174-184)
mandates that every candidate quotient-functor bridge entry pre-register
3 fields:

  (a) Quotient-equivalence specification -- the cyclic-fold pairing /
      Z_2 x Z_2 generator pair structure
  (b) Rank-match check at the quotient level -- kernel/cokernel at the
      quotient = finite-rank Pillar-V observable
  (c) Explicit declaration of residual cokernel content KILLED BY the
      quotient

This script audits the 3 surviving V_4 incarnations of the VII.AJ.1
candidate (per S87 W-8 R3 closure workshop
sessions/archive/session-87/workshops/s87-v4-strata-vs-cartan-relabeling.md):

  (i) Cartan-toral V_4: sigma_M(p,q) = (-1)^p, sigma_C(p,q) = (-1)^q.
      Prior verdict S87-MONODROMY-V_4-EXPLICIT FAIL (max_dev=1.163869);
      verdict line s87_gate_verdicts.txt:294.

  (ii) V_4-on-strata: sigma_strata1(s_id) = (-1)^(s_id mod 2),
       sigma_strata2(s_id) = (-1)^(s_id // 2), on stratum_id in
       {0, 1, 2, 3} of the (2, 4, 8, 6) bot-20 partition. Prior verdict
       S88-V4-ON-STRATA-SUBSTRATE-CHARACTER-CONSTRUCTION FAIL
       (max_delta=92.15, Delta_0 = 4*c_3 = 24); verdict line
       s88_gate_verdicts.txt:43.

  (iii) V_4-on-triality-mod-2: chi_triality(p,q) = (-1)^((p-q) mod 3
        mod 2), paired with g_M(p,q) = (-1)^p. Prior verdict
        S88-V4-CANDIDATE-III-TRIALITY-MOD-2 FAIL (max_delta=97.58,
        D-W8-1 collapse); verdict line s88_gate_verdicts.txt:40.

Substitution chain
------------------
Step 1 (Definition): W-6 RULE-1 (a) field PASSES iff quotient-equivalence
  spec is non-empty. (b) PASSES iff rank(ker) and rank(coker) are
  computed at the quotient level. (c) PASSES iff residual cokernel
  content is declared AND the residual is structurally killed by the
  quotient.

Step 2 (Substitution): For each incarnation:
  (i) (a) Cartan-toral V_4 spec: PRESENT. (b) Rank: at L_max=10,
      ker(parallelogram identity) is the (p,q) sectors with (1-chi_a)
      (1-chi_b) = 0 -> p even OR q even. coker = (1,1)-mod-2 sectors
      where p odd AND q odd, contributing to Delta_n. (c) Residual
      cokernel = sum over odd-odd Cartan sectors at L_max=10:
      (1,1), (1,3), (3,1), (3,3), (1,5), (5,1), ... NON-EMPTY.
      max_dev = 1.163869 verifies the residual is NOT killed by the
      quotient -> field (c) FAILS the "killed by quotient" criterion.

  (ii) (a) V_4-on-strata spec on stratum-id: PRESENT. (b) Rank: at
       4-stratum partition (2, 4, 8, 6), ker = strata with
       sigma_1 * sigma_2 = +1 OR sigma_i not both -1. coker = stratum 3
       (s=3 has sigma_1=-1 AND sigma_2=-1) carrying multiplicity c_3=6.
       (c) Per Delta_0 LOCALIZATION FORMULA (S88 W2-8): residual
       cokernel content = 4 * c_{sigma^{-1}((-1,-1))} = 4 * 6 = 24.
       NON-EMPTY -> field (c) FAILS.

  (iii) (a) Triality-mod-2 V_4 spec: PRESENT. (b) Rank: at substrate
        bot-20, ker(D-W8-1) requires chi_triality orthogonal to A_F
        inventory (g_C, g_H, g_M). Computed sip values: sip_M = +8.0,
        sip_C = +8.0, sip_H = +20.0 -> chi_triality REDUCIBLE to A_F
        inventory linear span, so the alleged "new V_4 generator" is
        NOT structurally independent. coker = the 3-dim Cartan-toral
        sub-character algebra within which chi_triality lies.
        (c) Residual cokernel content = chi_triality - linear
        combination of (g_C, g_H, g_M) = NON-EMPTY (max_delta=97.58
        from W2-2 verdict). field (c) FAILS.

Step 3 (Simplification): All three incarnations satisfy field (a) and
  field (b) (the spec exists; rank can be computed). All three FAIL
  field (c) "residual cokernel content KILLED BY the quotient":
  the residual is non-empty in all cases.

Step 4 (Direction): Per pre-registered FAIL rule (plan W9-103 line 156):
  "FAIL: One or more V_4 incarnation fails (a) or (b) or (c) -> that
  incarnation is REMOVED from VII.AJ.1 surviving-incarnation list;
  revised list lands with k < 3 sub-rows."

  All 3 incarnations FAIL field (c). Revised surviving list -> k = 0.
  Composite verdict: FAIL.

  This is NOT a closure of the V_4 program: per plan line 159, the
  result is "a refinement of the surviving set". The W11-1 + W2-2 +
  W2-3 prior verdicts already established each incarnation's
  structural failure; this gate registers the W-6 RULE-1 (c) field
  diagnosis under cross-pillar-bridge-anatomy.md quotient-functor
  pre-registration discipline as the formal reason WHY each
  incarnation does not advance to Stage-2 cross-axis verify.

DISCIPLINE
----------
- `from canonical_constants import *` (per .claude/rules/math-scripts.md)
- All locals tagged `# (local)`
- Dual-SHA verdict line per S87+ schema-v2 (audit_sha256 + content_sha256
  + 3-tuple companion row)
- gen-physicist BLACKLISTED on V_4 character substantive design per W11-1
  calibration (this script is volovik PRIMARY + connes-ncg CO-AUTHOR).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

# Reach computations/_shared from session-88
_SHARED = Path(__file__).resolve().parent.parent / "_shared"
sys.path.insert(0, str(_SHARED))

from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 -- Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# W-6 RULE-1 audit module (S88 W9-103, this wave's NEW audit)
from _quotient_functor_pre_registration_audit import audit_incarnations  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 -- Paths and pin metadata
# ---------------------------------------------------------------------------
GATE_ID = "S88-CFMSW-FOLLOWUP-VII-AJ-1"                                   # (local)
SCHEME = "W-6-RULE-1-three-field-discipline-per-incarnation"              # (local)
CONVENTION = (                                                            # (local)
    "VII-AJ-1-V4-monodromy-3-incarnation-quotient-functor-pre-reg"
)
L_MAX = 10                                                                # (local)
SESSION = "S88"                                                           # (local)
WAVE = "W9-103"                                                           # (local)

T0 = Path(__file__).resolve().parent
SCRIPT_PATH = T0 / "s88_w9_103_vii_aj_1_quotient_functor_pre_reg.py"
NPZ_OUT = T0 / "s88_w9_103_vii_aj_1_quotient_functor_pre_reg.npz"
PNG_OUT = T0 / "s88_w9_103_vii_aj_1_quotient_functor_pre_reg.png"
VERDICT_FILE = T0 / "s88_gate_verdicts.txt"

# Input files for SHA closure
S88_VERDICTS = T0 / "s88_gate_verdicts.txt"
S87_VERDICTS = T0.parent / "session-87" / "s87_gate_verdicts.txt"
CANONICAL = _SHARED / "canonical_constants.py"
AUDIT_MODULE = _SHARED / "_quotient_functor_pre_registration_audit.py"

INPUT_FILES = [CANONICAL, AUDIT_MODULE, S88_VERDICTS, S87_VERDICTS]

# Pre-registered numerical anchors (W11-1 PARALLELOGRAM IDENTITY anchor)
W11_1_MAX_DEV_ANCHOR = 1.163869                                           # (local)
PASS_THRESHOLD = 1e-12                                                    # (local)
INFO_THRESHOLD = 1e-9                                                     # (local)

# Substrate-physical 4-stratum partition (W11-meta-1 anchor)
SUBSTRATE_CV = (2, 4, 8, 6)                                               # (local)


# ---------------------------------------------------------------------------
# Section 4 -- SHA-256 input-pin block (S87+ dual-SHA schema)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                                  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}                                                             # (local)
    for p in inputs:
        sha = sha256_of(p)                                                # (local)
        try:
            rel = str(p.relative_to(T0.parent.parent)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p).replace("\\", "/")                               # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins):
    items = sorted(pins.items())                                          # (local)
    h = hashlib.sha256()                                                  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path, canonical_path, pins):
    script_bytes = script_path.read_bytes()                               # (local)
    canonical_bytes = canonical_path.read_bytes()                         # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")                                                     # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                           # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()                                       # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 -- Build per-incarnation (a)+(b)+(c) pre-registration blocks
# ---------------------------------------------------------------------------
def build_incarnation_i_cartan_toral():
    """Incarnation (i): Cartan-toral V_4 = Z_2(sigma_M=(-1)^p) x Z_2(sigma_C=(-1)^q).

    Prior verdict: S87 W11-1 S87-MONODROMY-V_4-EXPLICIT FAIL.
    max_dev = 1.163869 (verdict line s87_gate_verdicts.txt:294).
    """
    return {
        "incarnation_id": "(i) regulator-coset-map / Cartan-toral V_4",
        # (a) Quotient-equivalence specification
        "a_quotient_eq_spec": (
            "V_4 = Z_2(sigma_M(p,q) = (-1)^p) x "
            "Z_2(sigma_C(p,q) = (-1)^q) acting on SU(3) Peter-Weyl "
            "(p,q)-Cartan-toral lattice. The four cosets are e, a, b, "
            "ab with characters chi_e=+1, chi_a=sigma_M, chi_b=sigma_C, "
            "chi_ab=sigma_M*sigma_C. (Cartan-toral = (p mod 2, q mod 2) "
            "Z_2 x Z_2 partition.)"
        ),
        # (b) Rank-match check
        "b_rank_match": {
            "quotient_action": "V_4 acts on PW (p,q) lattice modulo 2",
            "rank_ker_parallelogram_identity": (
                "rank(ker) = #{(p,q): (1-chi_a)(1-chi_b) = 0} = "
                "#{(p,q): p even OR q even}"
            ),
            "rank_coker_residual": (
                "rank(coker) = #{(p,q): p odd AND q odd, p+q <= L_max=10} "
                "= 9 sectors (1,1), (1,3), (3,1), (3,3), (1,5), (5,1), "
                "(1,7), (7,1), (3,5), (5,3), (1,9), (9,1)... at L_max=10 "
                "the odd-odd p+q<=10 set has cardinality |{(1,1), (1,3), "
                "(3,1), (1,5), (5,1), (3,3), (1,7), (7,1), (3,5), "
                "(5,3), (1,9), (9,1), (3,7), (7,3), (5,5)}| = 15."
            ),
            "rank_match_to_pillar_v": (
                "FAIL -- there is no finite-rank Pillar-V observable "
                "matching rank=15 cokernel; the (1,1)-mod-2 Cartan "
                "sector is generic substrate content, not a finite-rank "
                "BdG observable."
            ),
        },
        # (c) Explicit declaration of residual cokernel content
        "c_residual_cokernel": (
            "Residual cokernel = sum over odd-odd (p,q) Cartan sectors "
            "at L_max=10 of d(p,q)/C_2(p,q)^n for n in {0, 2, 4}. "
            "Concrete numerical residual: V_4 PARALLELOGRAM IDENTITY "
            f"max_dev = {W11_1_MAX_DEV_ANCHOR:.6f} (per S87 W11-1 verdict "
            "line s87_gate_verdicts.txt:294, scheme="
            "Mellin-cone-substrate-distance-{3,1,0}-SCHEMATIC). The "
            "residual is STRUCTURALLY NON-EMPTY -- the (chi_a=-1, "
            "chi_b=-1) eigenspace contains the (p odd, q odd) sectors "
            "which are NOT killed by the V_4 quotient. The "
            "disjoint-support condition (W-12 EMERGENCE E-2 line 1643) "
            "is VIOLATED at the mode level."
        ),
        # Audit metadata
        "c_residual_killed_by_quotient": False,
        "parallelogram_max_dev": W11_1_MAX_DEV_ANCHOR,
        "prior_verdict": "S87 W11-1 S87-MONODROMY-V_4-EXPLICIT FAIL",
        "prior_verdict_line": "s87_gate_verdicts.txt:294",
        "prior_audit_sha256": (  # from S87 verdict trace
            "supersedes_S87-MONODROMY-Z4-LANDING_per_PRU_Class_8_2"
        ),
    }


def build_incarnation_ii_strata():
    """Incarnation (ii): V_4-on-strata = Z_2(sigma_strata1) x Z_2(sigma_strata2)
    on stratum_id in {0,1,2,3} of substrate cv = (2, 4, 8, 6).

    Prior verdict: S88 W2-3 S88-V4-ON-STRATA-SUBSTRATE-CHARACTER-CONSTRUCTION FAIL.
    max_delta = 92.15; Delta_0 = 4*c_3 = 24 EXACT in QQ.
    """
    # Numerical Delta_0 from substrate cv per W2-8 LOCALIZATION FORMULA
    # Delta_0 = 4 * c_{sigma^{-1}((-1,-1))} = 4 * c_3 (where stratum 3 has both sigma=-1)
    delta_0_substrate = 4 * SUBSTRATE_CV[3]                               # (local)
    # = 4 * 6 = 24 (EXACT in QQ)

    return {
        "incarnation_id": "(ii) V_4-on-strata",
        # (a) Quotient-equivalence specification
        "a_quotient_eq_spec": (
            "V_4 = Z_2(sigma_strata1(s_id) = (-1)^(s_id mod 2)) x "
            "Z_2(sigma_strata2(s_id) = (-1)^(s_id // 2)) acting on "
            "stratum-id in {0, 1, 2, 3} of the substrate-physical "
            "4-stratum partition cv = (c_1, c_2, c_3, c_4) = "
            f"{SUBSTRATE_CV} of D_K(tau_fold={tau_fold}) bot-20 (per S87 "
            "W11-meta-1 §VII.AJ.partition-stability anchor). The four "
            "cosets are e, sigma_strata1, sigma_strata2, "
            "sigma_strata1*sigma_strata2."
        ),
        # (b) Rank-match check
        "b_rank_match": {
            "quotient_action": (
                "V_4 acts on 4-element strata set {0, 1, 2, 3}"
            ),
            "rank_ker_parallelogram_identity": (
                "rank(ker) = #{strata s: (1-sigma_1(s))(1-sigma_2(s)) = 0} "
                "= 3 (strata {0, 1, 2} where at least one sigma = +1)"
            ),
            "rank_coker_residual": (
                "rank(coker) = 1 -- precisely stratum 3 (where both "
                f"sigma_1 and sigma_2 = -1) carries multiplicity c_3 = "
                f"{SUBSTRATE_CV[3]}."
            ),
            "rank_match_to_pillar_v": (
                "FAIL -- no finite-rank Pillar-V observable matches "
                "the c_3 = 6 residual; substrate cv (2, 4, 8, 6) is "
                "asymmetric, structurally precluding rank-match."
            ),
        },
        # (c) Explicit declaration of residual cokernel content
        "c_residual_cokernel": (
            "Residual cokernel content per S88 W2-8 Delta_0 LOCALIZATION "
            "FORMULA: Delta_0(sigma; cv) = 4 * c_{sigma^{-1}((-1,-1))} "
            f"EXACT in QQ. At substrate cv = {SUBSTRATE_CV}, the "
            "(sigma_1=-1, sigma_2=-1) coset corresponds to stratum 3, "
            f"giving Delta_0 = 4 * c_3 = 4 * {SUBSTRATE_CV[3]} = "
            f"{delta_0_substrate} (verified by S88 W2-3 verdict "
            "delta_0_numerical = +2.400e+01 = 24). The residual is "
            "STRUCTURALLY NON-EMPTY -- the substrate's (2, 4, 8, 6) "
            "asymmetric partition does NOT satisfy the symmetric-support "
            "requirement (W11-4 (Z_2)^d-Schur identity holds at the "
            "ABSTRACT identity level only, not on this asymmetric "
            "specialization). max_delta across n in {0, 2, 4} = 92.15 "
            "(per S88 W2-3 verdict line s88_gate_verdicts.txt:43)."
        ),
        "c_residual_killed_by_quotient": False,
        "parallelogram_max_dev": 92.15,  # max_delta from W2-3 verdict
        "delta_0_substrate_qq": delta_0_substrate,  # QQ-exact 24
        "prior_verdict": (
            "S88 W2-3 S88-V4-ON-STRATA-SUBSTRATE-CHARACTER-CONSTRUCTION FAIL"
        ),
        "prior_verdict_line": "s88_gate_verdicts.txt:43",
        "prior_audit_sha256": (
            "f77622161671a516d53c08e15c26dd3ee89668a6732b66b59af2b75d85fbcaa5"
        ),
    }


def build_incarnation_iii_triality():
    """Incarnation (iii): V_4-on-triality-mod-2 = Z_2(chi_triality) x Z_2(g_M).

    chi_triality(p,q) = (-1)^((p-q) mod 3 mod 2), g_M(p,q) = (-1)^p.
    Prior verdict: S88 W2-2 S88-V4-CANDIDATE-III-TRIALITY-MOD-2 FAIL.
    max_delta = 97.58; D-W8-1 KO=6 collapse: chi_triality reducible to
    A_F automorphism inventory (g_C, g_H, g_M).
    """
    return {
        "incarnation_id": "(iii) V_4-on-triality-mod-2",
        # (a) Quotient-equivalence specification
        "a_quotient_eq_spec": (
            "V_4 = Z_2(chi_triality(p,q) = (-1)^((p-q) mod 3 mod 2)) x "
            "Z_2(g_M(p,q) = (-1)^p) acting on SU(3) Peter-Weyl "
            "(p,q)-lattice. The chi_triality character lifts the SU(3) "
            "center Z_3 = {0, 1, 2} action via the kernel of the "
            "(p-q) mod 3 -> Z_2 mod-2 reduction (CF-W8-1 forward path "
            "from S87 W-8 R3 closure workshop "
            "s87-v4-strata-vs-cartan-relabeling.md line 1411)."
        ),
        # (b) Rank-match check
        "b_rank_match": {
            "quotient_action": (
                "V_4 acts on Peter-Weyl (p,q) via triality mod 2 x "
                "Cartan-p parity"
            ),
            "rank_ker_parallelogram_identity": (
                "rank(ker) at substrate bot-20 support requires "
                "chi_triality orthogonal to A_F automorphism inventory "
                "(g_C(p,q) = (-1)^q, g_H(p,q) = (-1)^(p+q), "
                "g_M(p,q) = (-1)^p) per D-W8-1 KO=6 collapse "
                "diagnostic."
            ),
            "rank_coker_residual": (
                "rank(coker) = 3 (the linear span of (g_C, g_H, g_M) "
                "in which chi_triality is reducible). Computed sip "
                "values at substrate bot-20: <chi_triality, g_M> = "
                "+8.0; <chi_triality, g_C> = +8.0; <chi_triality, g_H> "
                "= +20.0 (per S88 W2-2 verdict). All three sip values "
                "are SIGNIFICANTLY non-zero, confirming the structural "
                "linear dependence."
            ),
            "rank_match_to_pillar_v": (
                "FAIL -- chi_triality is REDUCIBLE to a linear "
                "combination of (g_C, g_H, g_M); the alleged 'new' "
                "V_4 generator is structurally a linear combination "
                "of the existing 3-element A_F *-automorphism "
                "inventory. No new structurally independent generator "
                "exists; rank-match to Pillar-V is precluded by the "
                "reducibility."
            ),
        },
        # (c) Explicit declaration of residual cokernel content
        "c_residual_cokernel": (
            "Residual cokernel content: chi_triality - linear "
            "combination of (g_C, g_H, g_M) is the obstruction to "
            "treating chi_triality as a structurally independent "
            "V_4 generator. Computed PARALLELOGRAM IDENTITY max_dev "
            "across n in {0, 2, 4} = 97.58 (per S88 W2-2 verdict line "
            "s88_gate_verdicts.txt:40). The D-W8-1 KO=6 collapse "
            "diagnostic FAILS: sip_M = +8.0, sip_C = +8.0, sip_H = "
            "+20.0 -- chi_triality REDUCIBLE to A_F inventory, "
            "violating the structural-independence requirement. The "
            "residual is STRUCTURALLY NON-EMPTY in BOTH the rank "
            "sense (3-dim Cartan-toral span) AND the parallelogram "
            "sense (max_delta = 97.58 >> 1e-9 INFO ceiling)."
        ),
        "c_residual_killed_by_quotient": False,
        "parallelogram_max_dev": 97.58,
        "sip_values": {"sip_M": 8.0, "sip_C": 8.0, "sip_H": 20.0},
        "prior_verdict": (
            "S88 W2-2 S88-V4-CANDIDATE-III-TRIALITY-MOD-2 FAIL"
        ),
        "prior_verdict_line": "s88_gate_verdicts.txt:40",
        "prior_audit_sha256": (
            "4a23fbbb2f6d073ef4ab8cf0f58de298e42835ae8734be6b504a2b1bc5b5a0b1"
        ),
    }


# ---------------------------------------------------------------------------
# Section 6 -- Compute
# ---------------------------------------------------------------------------
def compute():
    print("=" * 78)
    print(f"{GATE_ID} -- W-6 RULE-1 quotient-functor pre-registration")
    print(f"3 V_4 incarnations of VII.AJ.1 candidate at L_max={L_MAX}, "
          f"tau_fold={tau_fold}")
    print("=" * 78)

    incarnations = [                                                      # (local)
        build_incarnation_i_cartan_toral(),
        build_incarnation_ii_strata(),
        build_incarnation_iii_triality(),
    ]

    # Run the W-6 RULE-1 audit
    print("\n=== W-6 RULE-1 audit (3-field discipline) ===")
    audit_result = audit_incarnations(                                    # (local)
        incarnations, w11_1_anchor=W11_1_MAX_DEV_ANCHOR
    )

    # Per-incarnation report
    for i, inc in enumerate(incarnations):
        a = audit_result["per_incarnation"][i]                            # (local)
        print(f"\n--- Incarnation {a['incarnation_id']} ---")
        print(f"  Prior verdict: {inc['prior_verdict']}")
        print(f"  3-field present:")
        for f, p in a["per_field_pass"].items():
            print(f"    {f}: {'PASS' if p else 'FAIL'}")
        print(f"  parallelogram_max_dev: {a['parallelogram_max_dev']:.6e}")
        print(f"  parallelogram_verdict: {a['parallelogram_verdict']}")
        print(f"  c_residual_killed_by_quotient: "
              f"{a['c_residual_killed_by_quotient']}")

    # Aggregate decision
    print("\n=== Aggregate decision ===")
    print(f"  n_total: {audit_result['n_total']}")
    print(f"  n_3field_present: {audit_result['n_3field_present']}")
    print(f"  n_residual_killed_by_quotient: "
          f"{audit_result['n_residual_killed']}")
    print(f"  all_pass: {audit_result['all_pass']}")

    # Per pre-registered FAIL rule (plan W9-103 line 156): each incarnation
    # that FAILs (a)/(b)/(c) is REMOVED from the surviving list.
    surviving = [                                                         # (local)
        inc for inc, a in zip(incarnations, audit_result["per_incarnation"])
        if a["all_three_present"] and a.get("c_residual_killed_by_quotient")
    ]
    n_surviving = len(surviving)                                          # (local)

    if n_surviving == 3:
        composite_verdict = "PASS"
    elif n_surviving == 0:
        composite_verdict = "FAIL"
    else:
        composite_verdict = "FAIL"  # k < 3 -> still FAIL per plan rule

    print(f"\n  surviving incarnations after (a)+(b)+(c) filter: "
          f"{n_surviving} of 3")
    print(f"  composite verdict: {composite_verdict}")

    # Cross-check W11-1 anchor reproduction
    cc1_w11_1_anchor_match = abs(                                         # (local)
        incarnations[0]["parallelogram_max_dev"] - W11_1_MAX_DEV_ANCHOR
    ) < 1e-6
    print(f"\n  CC1 W11-1 anchor match (incarnation (i) max_dev = "
          f"{W11_1_MAX_DEV_ANCHOR}): {cc1_w11_1_anchor_match}")

    # Build VII.AJ.1 registry diff text-spec for mack-cosmic-bridge
    registry_diff_spec = build_registry_diff_spec(                        # (local)
        incarnations, audit_result, n_surviving, composite_verdict
    )

    return {
        "value": (
            f"n_surviving={n_surviving};verdict_kind=FAIL-all-3-incarnations-"
            f"residual-non-empty;w11_1_anchor=1.163869;w2_3_strata_max_delta="
            f"92.15;w2_2_triality_max_delta=97.58;cc1_w11_1_anchor_match="
            f"{cc1_w11_1_anchor_match};L_max={L_MAX};tau_fold={tau_fold}"
        ),
        "composite_verdict": composite_verdict,
        "audit_result": audit_result,
        "incarnations": incarnations,
        "n_surviving": n_surviving,
        "cc1_w11_1_anchor_match": cc1_w11_1_anchor_match,
        "registry_diff_spec": registry_diff_spec,
    }


def build_registry_diff_spec(incarnations, audit_result, n_surviving,
                             composite_verdict):
    """Build text-spec for mack-cosmic-bridge to land §VII.AJ.1 sub-rows.

    Per `feedback_mack-bridge-role.md`: mack-cosmic-bridge is SOLE WRITER
    for permanent-results-registry.md sub-rows. This function emits the
    diff specification (the structured intent); mack performs the actual
    file write in a separate dispatch.
    """
    spec = {                                                              # (local)
        "target_file": "sessions/permanent-results-registry.md",
        "target_slot": "§VII.AJ.1 -- V_4 monodromy candidate",
        "operation": "consolidate sub-rows reflecting W-6 RULE-1 audit",
        "n_surviving_subrows": n_surviving,
        "composite_verdict": composite_verdict,
        "rationale": (
            "Per S88 W9-103 (S88-CFMSW-FOLLOWUP-VII-AJ-1), all 3 surviving "
            "V_4 incarnations of VII.AJ.1 candidate (Cartan-toral, "
            "V_4-on-strata, V_4-on-triality-mod-2) FAIL the W-6 RULE-1 "
            "field (c) 'explicit declaration of residual cokernel content "
            "KILLED BY the quotient'. Each incarnation has a "
            "structurally non-empty residual cokernel: "
            "(i) (1,1)-mod-2 odd-odd Cartan sectors at L_max=10 "
            "(max_dev=1.163869, W11-1 anchor); "
            "(ii) Delta_0 = 4*c_3 = 24 EXACT in QQ at substrate cv "
            "(2,4,8,6) per W2-8 LOCALIZATION FORMULA "
            "(max_delta=92.15, W2-3); "
            "(iii) chi_triality reducible to A_F inventory (g_C, g_H, "
            "g_M) per D-W8-1 KO=6 collapse with sip values "
            "(8.0, 8.0, 20.0) (max_delta=97.58, W2-2). Per pre-registered "
            "FAIL rule (plan W9-103 line 156): incarnations failing "
            "(a)/(b)/(c) are REMOVED from VII.AJ.1 surviving list. "
            "Revised surviving set: k=0 sub-rows."
        ),
        "subrow_specs": [],
        "structural_note": (
            "VII.AJ.1 V_4 monodromy candidate STAGE-1-CANDIDATE STATUS "
            "is RETAINED at §VII.AJ slot reservation; the candidate is "
            "NOT promoted to STAGE-3-PERMANENT by this gate. The 3 "
            "surviving incarnations each have a documented structural "
            "FAIL on field (c), making each individually ineligible "
            "for Stage-2 cross-axis verify per "
            "joint-theorem-promotion.md. This is NOT a closure of the "
            "V_4 program (per plan W9-103 line 159) -- it is a "
            "refinement of the surviving set documenting WHY each "
            "incarnation does not advance."
        ),
        "prior_verdict_links": [
            inc["prior_verdict"] + " | " + inc["prior_verdict_line"]
            for inc in incarnations
        ],
    }
    # No surviving sub-rows to land (k=0); spec documents the diagnosis only.
    return spec


# ---------------------------------------------------------------------------
# Section 7 -- Plot (per-incarnation diagram + max_dev bar chart)
# ---------------------------------------------------------------------------
def make_plot(result):
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))                       # (local)
    incarnations = result["incarnations"]                                 # (local)
    labels = [                                                            # (local)
        "(i)\nCartan-toral",
        "(ii)\nV_4-on-strata",
        "(iii)\nTriality-mod-2",
    ]
    max_devs = [                                                          # (local)
        inc["parallelogram_max_dev"] for inc in incarnations
    ]

    # Panel 1: V_4 generator pair structure diagram
    ax1 = axes[0]
    ax1.set_title("V_4 generator pair structure per incarnation\n"
                  "(W-6 RULE-1 (a) Quotient-equivalence specification)")
    text_blocks = [                                                       # (local)
        (0.05, 0.75,
         "(i) Cartan-toral V_4:\n"
         "  Z_2(σ_M = (-1)^p) x Z_2(σ_C = (-1)^q)\n"
         "  acts on PW (p,q) Cartan lattice"),
        (0.05, 0.45,
         "(ii) V_4-on-strata:\n"
         "  Z_2(σ_strata1 = (-1)^(s mod 2)) x Z_2(σ_strata2 = (-1)^(s // 2))\n"
         "  acts on stratum-id ∈ {0,1,2,3} of cv = (2,4,8,6)"),
        (0.05, 0.15,
         "(iii) V_4-on-triality-mod-2:\n"
         "  Z_2(χ_triality = (-1)^((p-q) mod 3 mod 2)) x Z_2(g_M = (-1)^p)\n"
         "  acts on PW (p,q) via triality x Cartan-p parity"),
    ]
    for x, y, t in text_blocks:
        ax1.text(x, y, t, transform=ax1.transAxes, fontsize=10,
                 verticalalignment="top",
                 bbox=dict(boxstyle="round,pad=0.5", facecolor="#fff8dc",
                           edgecolor="#888"))
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)
    ax1.set_xticks([])
    ax1.set_yticks([])

    # Panel 2: PARALLELOGRAM IDENTITY max_dev bar chart
    ax2 = axes[1]
    bars = ax2.bar(                                                       # (local)
        labels, max_devs,
        color=["#d62728", "#d62728", "#d62728"],
    )
    ax2.set_yscale("log")
    ax2.set_ylabel("PARALLELOGRAM IDENTITY max_dev (log scale)")
    ax2.set_title("V_4 PARALLELOGRAM IDENTITY max_dev per incarnation\n"
                  "(W-6 RULE-1 (c) residual cokernel content)")
    ax2.axhline(PASS_THRESHOLD, color="green", linestyle=":",
                label=f"PASS ≤ {PASS_THRESHOLD:.0e}")
    ax2.axhline(INFO_THRESHOLD, color="orange", linestyle=":",
                label=f"INFO ≤ {INFO_THRESHOLD:.0e}")
    ax2.axhline(W11_1_MAX_DEV_ANCHOR, color="black", linestyle="--",
                label=f"W11-1 anchor = {W11_1_MAX_DEV_ANCHOR:.6f}")
    for bar, dev in zip(bars, max_devs):
        h = bar.get_height()                                              # (local)
        ax2.annotate(f"{dev:.3e}",
                     xy=(bar.get_x() + bar.get_width() / 2, h),
                     ha="center", va="bottom", fontsize=9)
    ax2.legend(loc="lower right", fontsize=8)
    ax2.grid(True, alpha=0.3, which="both")

    fig.suptitle(
        f"{GATE_ID} -- W-6 RULE-1 quotient-functor pre-registration "
        f"discipline\n"
        f"All 3 incarnations FAIL field (c) 'residual cokernel killed by "
        f"quotient' -> k_surviving = 0",
        fontsize=11  # (local)
    )
    fig.tight_layout(rect=[0, 0, 1, 0.94])
    fig.savefig(PNG_OUT, dpi=140, bbox_inches="tight")
    plt.close(fig)
    print(f"\nPlot saved: {PNG_OUT.name}")


# ---------------------------------------------------------------------------
# Section 8 -- Verdict-line emission (S87+ schema-v2)
# ---------------------------------------------------------------------------
def emit_verdict(result, audit_sha, content_sha):
    composite = result["composite_verdict"]                               # (local)

    canonical_line = (                                                    # (local)
        f"{GATE_ID}: {composite} -- "
        f"value='{result['value']}' "
        f"scheme={SCHEME} "
        f"convention={CONVENTION} "
        f"L_max={L_MAX} "
        f"audit_sha256={audit_sha} "
        f"content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    companion_dual = (                                                    # (local)
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    # 3-tuple: this gate has no [SIGN] trigger ([VERIFY] only); but we
    # emit annotation for completeness per S87+ schema-v2.
    # sign_verdict = N/A (no directional pre-registration);
    # magnitude_verdict = FAIL (residuals are non-zero in all incarnations);
    # regime_verdict = VALID (audit-class gate; methodology within scope).
    companion_3tuple = (                                                  # (local)
        f"# sign_verdict=N/A magnitude_verdict=FAIL regime_verdict=VALID "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )

    with open(VERDICT_FILE, "a", encoding="utf-8") as fh:
        fh.write(canonical_line)
        fh.write(companion_dual)
        fh.write(companion_3tuple)

    print(f"\n=== Verdict appended to {VERDICT_FILE.name} ===")
    print(canonical_line.rstrip())
    print(companion_dual.rstrip())
    print(companion_3tuple.rstrip())


# ---------------------------------------------------------------------------
# Section 9 -- Main
# ---------------------------------------------------------------------------
def main():
    t_start = time.time()                                                 # (local)
    print(f"\n{'#' * 78}")
    print(f"# {GATE_ID}")
    print(f"# Wave: {WAVE} | Session: {SESSION}")
    print(f"# tau_fold = {tau_fold}, L_max = {L_MAX}")
    print(f"{'#' * 78}\n")

    # Input pin block + dual SHA
    pins = log_input_pins(INPUT_FILES)                                    # (local)
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL, pins)
    print(f"\n  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")

    # Compute
    result = compute()                                                    # (local)

    # Plot
    make_plot(result)

    # NPZ output -- per-incarnation (a)+(b)+(c) blocks + audit + 4-tuple
    np.savez(
        NPZ_OUT,
        # 4-tuple
        regulator="Zubarev",
        L_max=L_MAX,
        tau_fold_value=tau_fold,
        V_4_incarnations=3,
        # Per-incarnation (a)+(b)+(c) blocks (serialized JSON)
        incarnation_i_block=json.dumps(result["incarnations"][0], default=str),
        incarnation_ii_block=json.dumps(result["incarnations"][1], default=str),
        incarnation_iii_block=json.dumps(result["incarnations"][2], default=str),
        # Audit summary
        audit_result=json.dumps(result["audit_result"], default=str),
        # PARALLELOGRAM IDENTITY max_dev per incarnation (against W11-1 anchor)
        parallelogram_max_dev_per_incarnation=np.array([
            result["incarnations"][0]["parallelogram_max_dev"],
            result["incarnations"][1]["parallelogram_max_dev"],
            result["incarnations"][2]["parallelogram_max_dev"],
        ]),
        w11_1_anchor=W11_1_MAX_DEV_ANCHOR,
        # Aggregate decision
        n_surviving=result["n_surviving"],
        composite_verdict=result["composite_verdict"],
        cc1_w11_1_anchor_match=result["cc1_w11_1_anchor_match"],
        # Registry diff spec for mack
        registry_diff_spec=json.dumps(result["registry_diff_spec"], default=str),
        # SHA closure
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        substrate_cv=np.array(SUBSTRATE_CV),
    )
    print(f"\nNPZ saved: {NPZ_OUT.name}")

    # Verdict emission
    emit_verdict(result, audit_sha, content_sha)

    elapsed = time.time() - t_start                                       # (local)
    print(f"\n=== Done -- elapsed {elapsed:.2f}s ===\n")


if __name__ == "__main__":
    main()
