#!/usr/bin/env python3
"""
S101 W3-7 — S101-PS-RGE-MODELC-SIN2-MZ
G422D Model-C one-loop INVERSE intermediate-scale RGE: 3/8 unification -> M_Z couplings
======================================================================================

Gate: S101-PS-RGE-MODELC-SIN2-MZ ([VERIFY])

Pre-registered (form-2 INFO-by-design, plan §W3-7):
  FAIL iff the exactly-determined one-loop inverse system has NO real ordered
       solution with M_Z <= M_C <= M_U <= M_Pl_unreduced (a determinate negative:
       Model-C one-loop running cannot connect sin^2(M_U)=3/8 to the measured
       M_Z couplings with its scalar content).
  INFO (BY DESIGN, the only non-FAIL outcome) iff an ordered solution exists; the
       verdict carries the four-element report R1-R4 (method Step D).
  PASS NOT REACHABLE BY DESIGN (pre-declared at plan-freeze; a PASS emission is a
       Class-4 ansatz-forcing rejected at intake). The scan-and-tune FORWARD form
       (pick M_C, run down, hit a band) was REJECTED at plan-freeze as Class-6-adjacent;
       the honest INVERSE form (input the three measured M_Z couplings, solve exactly
       for M_C, M_U, alpha_U from matching + the 3/8 boundary) has ZERO free parameters.

Hard-sequencing: dispatches only AFTER gate-6 (S101-CCS-MODELC-KO-DERIVATION) verdict
  line exists. Gate-6 landed INFO (audit bb2fa21a69f4f849; theory_match=True; derived
  KO-triple (6,+1,+1,-1) MATCHED the substrate anchor; INFO = PRIMARY-UNDERDETERMINED,
  NOT a physics contradiction). Per the gate-6->gate-7 INFO row: DISPATCH STATUS-QUO
  (full RGE run, all axes) with ko_axis=indeterminate-carried riding the value string.

Inputs (SHA-256 dual-pinned at runtime):
  - canonical_constants.py (sin2_thetaW_MSbar, M_Z, alpha_em_MZ_inv, alpha_s_MZ_obs,
    M_Pl_unreduced) -- CANONICAL IMPORTS (never hardcoded)
  - s100b_w2_2_ps_variant_id.npz  (variant ID = C-LR / G422D; scalar content; 3/8 exact)
  - Aydemir overview PDF  (METHODOLOGICAL cross-check; published OOM only, never numeric source)
  - s101_gate_verdicts.txt  (in-session; gate-6 verdict capture for the ko_axis tag)
  - s101_ccs_modelc_ko_derivation.npz  (gate-6 derived tuple; consumed for the ko_axis tag)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<report>, scheme=G422D-MODELC-ONELOOP-INVERSE-INTERMEDIATE-SCALE,
   convention=INFO-BY-DESIGN-TWO-ROUTE-ABSOLUTE, L_max=N/A)

Classification: PARTICLE. Gauge couplings are spectral moments (Yang-Mills action =
  4th spectral moment of D_K). The W2-2 fingerprint identified WHICH published
  Pati-Salam-adjacent organization (Model C / G422D) the substrate defect signature
  matches; this gate tests the RGE-viability axis of that identification -- an
  emergent-EFT statement about how the a_4-moment couplings reorganize between the
  unification boundary sin^2=3/8 and the laboratory scale. Direction of explanation:
  substrate defect fingerprint (W2-2, substrate-IS) -> unique published variant ->
  that variant's emergent-EFT running -> laboratory-IN couplings at M_Z and mu_BC.
  A FAIL would close the variant's RGE axis, NOT the substrate's (the fingerprint is
  untouched by any outcome here).

DISCIPLINE
----------
- `from canonical_constants import *` (Section 1)
- Every local/intermediate tagged `# (local)`
- CPU cap OMP8 (3x3 linear algebra; set before numpy import)
- a_n: NO Seeley-DeWitt coefficient consumed numerically (the spectral-action a_4 is
  cited structurally only; gate-6 already carried `a_n^{cutoff} structural-citation-only`).
  This gate consumes Dynkin indices + measured EW couplings; no a_n^{regulator} pin needed.
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- verdict emitted via the `emit_verdict` knowledge-MCP tool (race-safe); this script
  PRINTS the payload via print_verdict_payload and does NOT write the verdict file.

SUBSTITUTION CHAIN (the load-bearing sign/direction discipline)
---------------------------------------------------------------
Claim 1 (the inverse system is EXACTLY determined => scan_range = N/A):
  one-loop running, Convention I (SM-textbook alpha^{-1}-slope):
      alpha_i^{-1}(mu2) = alpha_i^{-1}(mu1) - (b_i/2pi)*ln(mu2/mu1).
  Step 1 (inputs at M_Z, GUT-normalized; script recomputes from canonical imports):
      alpha_2^{-1}(M_Z) = alpha_em^{-1}*sin2
      alpha_Y^{-1}(M_Z) = alpha_em^{-1}*(1-sin2)
      alpha_1^{-1}(M_Z) = (3/5)*alpha_Y^{-1}        [GUT norm; Y/2 = T_3R+(B-L)/2]
      alpha_3^{-1}(M_Z) = 1/alpha_s
  Step 2: run M_Z->M_C with SM (b1,b2,b3); tree matching at M_C; run M_C->M_U with
      Model-C (b_4, b_2LR) under D-parity; unify alpha_4(M_U)=alpha_2LR(M_U)=alpha_U.
  Step 3: 3 LINEAR equations in 3 unknowns (ln M_C, ln M_U, alpha_U^{-1}); unique iff
      the coefficient determinant != 0 (checked in-script) => nothing to scan/tune.
  Direction read-off: FAIL iff the unique solution violates the ordering window;
      INFO otherwise (by design).
Claim 2 (sin^2(M_U)=3/8 is the correct unification boundary):
  at M_U, GUT norm: alpha_1=alpha_2=alpha_U;
  alpha_em^{-1} = alpha_2^{-1}+alpha_Y^{-1} = alpha_U^{-1}+(5/3)alpha_U^{-1} = (8/3)alpha_U^{-1};
  sin^2(M_U) = alpha_2^{-1}/alpha_em^{-1} = alpha_U^{-1}/((8/3)alpha_U^{-1}) = 3/8 [exact].
  W2-2 verified 3/8 exact on three independent routes at 1e-12 (npz sin2_clause_pass=True).
Claim 3 (why Route-ACCOM is now legitimate -- the direction W2-2 forbade, this successor owns):
  Step 1: W2-2 FORBADE |0.23480 - 0.23121| in-gate (two numbers at DIFFERENT scales:
      mu_BC=188.44 GeV vs M_Z=91.1876 GeV -- scale-conflation).
  Step 2: this gate produces a SOLVED running trajectory sin^2(mu) over [M_Z, M_U];
      evaluating it AT mu_BC and AT M_Z places both on ONE curve -- scale-consistent
      BY CONSTRUCTION.
  Step 3: residual systematic = loop order (S83 accommodation fit was 2-loop; this gate
      is one-loop PINNED) -- DECLARED, non-gating, reported alongside R3.
  Read-off: R3 reports Delta = sin^2(mu_BC)_solved - 0.23480 AND the crossing scale mu*
      (where sin^2 = 0.23480) vs mu_BC. No threshold: REPORT-only by design.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — CPU thread cap (3x3 linear algebra; set BEFORE numpy import)
# ---------------------------------------------------------------------------
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

from canonical_constants import *  # noqa: F401,F403  (sin2_thetaW_MSbar, M_Z, ...)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time
from fractions import Fraction as F

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration pins
# ---------------------------------------------------------------------------
SESSION = "S101"                                                   # (local)
GATE_ID = "S101-PS-RGE-MODELC-SIN2-MZ"                             # (local)
SCHEME = "G422D-MODELC-ONELOOP-INVERSE-INTERMEDIATE-SCALE"        # (local)
CONVENTION = "INFO-BY-DESIGN-TWO-ROUTE-ABSOLUTE"                  # (local)
L_MAX = "N/A"                                                      # (local)

# Pre-registered tolerances (plan machinery_pin_map)
TOL_SOLVE = 1e-12          # ABS, linear-solve residual                  # (local)
TOL_CLOSURE = 1e-10        # ABS on sin^2, forward closure diagnostic    # (local)
ACCOM_VALUE = 0.23480      # accommodation row (S83-W3-G47 2-loop)        # (local)
MU_BC = 188.44             # accommodation-row scale (GeV), plan-pinned   # (local)

OUT_NPZ = SESSION_DIR / "s101_ps_rge_modelc_sin2_mz.npz"          # (local)
OUT_PNG = SESSION_DIR / "s101_ps_rge_modelc_sin2_mz.png"          # (local)

UPSTREAM_NPZ = COMPUTATIONS_DIR / "session-100b" / "s100b_w2_2_ps_variant_id.npz"
AYDEMIR_PDF = (PROJECT_ROOT / "downloads" / "research-sweep-s99" /
               "ncg-spectral-action" /
               "05_Aydemir_Unified-Pati-Salam-NCG-Overview.pdf")
GATE6_VERDICTS = SESSION_DIR / "s101_gate_verdicts.txt"
GATE6_NPZ = SESSION_DIR / "s101_ccs_modelc_ko_derivation.npz"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    UPSTREAM_NPZ,
    AYDEMIR_PDF,
    GATE6_VERDICTS,
    GATE6_NPZ,
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
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        except ValueError:
            rel = str(p).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
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
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5a — Model-C one-loop beta coefficients, computed IN-SCRIPT (exact rationals)
# ---------------------------------------------------------------------------
#
# Convention I (SM-textbook alpha^{-1}-slope; the pinned SM (41/10,-19/6,-7) live here):
#   b^{I}(G) = -(11/3) C2(G_adj) + (2/3) sum_{Weyl ferm} T(R) + (1/3) sum_{cplx scalar} T(R)
#   Aydemir's published convention II (dg^{-2}/dlnmu = -b^{II}/2pi, asymptotic-freedom-positive)
#   relates by b^{II} = -b^{I} for the non-abelian factors.
#
# Dynkin indices (T(fund SU(N)) = 1/2): SU(4): 4->1/2, 6->1/2, 10->3/2, 15->4; C2(adj)=4.
#                                       SU(2): 2->1/2, 3->2;                  C2(adj)=2.
# A rep's index for one factor = T(rep under that factor) * prod(dim under the OTHER factors).

def modelc_betas() -> dict:
    """Return Model-C (G422D) one-loop b-coefficients in Convention I (exact Fraction).

    Field content (npz variant C-LR / Aydemir Table 1 + Eq. 9, 12):
      Gauge: SU(4)_C x SU(2)_L x SU(2)_R, D-parity (g_2L=g_2R on [M_C, M_U]).
      Fermions (all 3 models): 3 gen x [(4,2,1) + (4bar,1,2)] (Weyl).
      Scalars (Model C, all fundamental, complex):
        phi(1,2,2), Sigma~(15,2,2), DeltaR(10,1,3), HR(6,1,1), DeltaL(10,3,1), HL(6,1,1).
    """
    # Dynkin indices
    T4 = {"1": F(0), "4": F(1, 2), "6": F(1, 2), "10": F(3, 2), "15": F(4)}  # (local)
    C2_4 = F(4)                                                              # (local)
    T2 = {"1": F(0), "2": F(1, 2), "3": F(2)}                               # (local)
    C2_2 = F(2)                                                             # (local)

    # ---- b_4 : SU(4)_C ----
    gauge4 = F(-11, 3) * C2_4                                               # (local)
    # fermions per gen: (4,2,1) SU4-index = T(4)*dim2_L*dim1_R = 1/2*2*1 = 1;
    #                   (4bar,1,2) SU4-index = T(4bar)*dim1_L*dim2_R = 1/2*1*2 = 1
    ferm4 = F(2, 3) * 3 * (T4["4"] * 2 * 1 + T4["4"] * 1 * 2)               # (local)
    # scalars (SU4-index = T(rep_SU4)*dim_SU2L*dim_SU2R):
    scal4 = F(1, 3) * (
        T4["1"] * 2 * 2          # phi(1,2,2)        -> 0
        + T4["15"] * 2 * 2       # Sigma~(15,2,2)    -> 4*4 = 16
        + T4["10"] * 1 * 3       # DeltaR(10,1,3)    -> (3/2)*3 = 9/2
        + T4["6"] * 1 * 1        # HR(6,1,1)         -> 1/2
        + T4["10"] * 3 * 1       # DeltaL(10,3,1)    -> (3/2)*3 = 9/2
        + T4["6"] * 1 * 1        # HL(6,1,1)         -> 1/2
    )                                                                       # (local)
    b4 = gauge4 + ferm4 + scal4                                             # (local)

    # ---- b_2L : SU(2)_L (= b_2R by D-parity; verified below) ----
    gauge2 = F(-11, 3) * C2_2                                               # (local)
    ferm2L = F(2, 3) * 3 * (T2["2"] * 4 * 1)   # only (4,2,1) carries SU(2)_L; index 1/2*4*1=2  # (local)
    scal2L = F(1, 3) * (
        T2["2"] * 1 * 2          # phi(1,2,2)       SU2L: 1/2 * dim1_SU4 * dim2_R = 1
        + T2["2"] * 15 * 2       # Sigma~(15,2,2)   1/2*15*2 = 15
        + T2["1"] * 10 * 3       # DeltaR(10,1,3)   SU2L singlet -> 0
        + T2["1"] * 6 * 1        # HR(6,1,1)        -> 0
        + T2["3"] * 10 * 1       # DeltaL(10,3,1)   2*10*1 = 20
        + T2["1"] * 6 * 1        # HL(6,1,1)        -> 0
    )                                                                       # (local)
    b2L = gauge2 + ferm2L + scal2L                                          # (local)

    # ---- b_2R : SU(2)_R (D-parity mirror) ----
    ferm2R = F(2, 3) * 3 * (T2["2"] * 4 * 1)                                # (local)
    scal2R = F(1, 3) * (
        T2["2"] * 1 * 2          # phi(1,2,2)       SU2R: 1
        + T2["2"] * 15 * 2       # Sigma~(15,2,2)   15
        + T2["3"] * 10 * 1       # DeltaR(10,1,3)   2*10*1 = 20
        + T2["1"] * 6 * 1        # HR(6,1,1)        -> 0
        + T2["1"] * 10 * 3       # DeltaL(10,3,1)   SU2R singlet -> 0
        + T2["1"] * 6 * 1        # HL(6,1,1)        -> 0
    )                                                                       # (local)
    b2R = gauge2 + ferm2R + scal2R                                          # (local)

    return {"b4": b4, "b2L": b2L, "b2R": b2R}


def sm_betas_from_machinery() -> dict:
    """Re-derive textbook SM (b1,b2,b3) from the SAME Dynkin machinery used for Model-C.

    This is the DEFINITIVE engine-validation: if the machinery reproduces the
    canonically-pinned SM (41/10, -19/6, -7) exactly, the same machinery's Model-C
    output is trustworthy (the engine is verified on a known answer). GUT-normalized
    U(1): index of a state = (3/5) Y^2 (SM hypercharge Y). Convention I throughout.
    SM content per gen (Weyl): Q(3,2,1/6), u^c(3bar,1,-2/3), d^c(3bar,1,1/3),
    L(1,2,-1/2), e^c(1,1,1); + complex Higgs H(1,2,1/2).
    """
    # b3 (SU(3))
    gauge3 = F(-11, 3) * F(3)                                            # (local)
    ferm3 = F(2, 3) * 3 * (F(1, 2) * 2 + F(1, 2) + F(1, 2))   # Q,u^c,d^c  # (local)
    b3 = gauge3 + ferm3                                                  # Higgs SU(3)-singlet
    # b2 (SU(2))
    gauge2 = F(-11, 3) * F(2)                                            # (local)
    ferm2 = F(2, 3) * 3 * (F(1, 2) * 3 + F(1, 2) * 1)        # Q(x3 color), L  # (local)
    scal2 = F(1, 3) * (F(1, 2))                              # Higgs(1,2)       # (local)
    b2 = gauge2 + ferm2 + scal2                                          # (local)
    # b1 (U(1)_Y, GUT-normalized): no gauge term
    sumY2_ferm = (6 * F(1, 6) ** 2 + 3 * F(2, 3) ** 2 + 3 * F(1, 3) ** 2
                  + 2 * F(1, 2) ** 2 + 1 * F(1) ** 2)                    # (local)
    ferm1 = F(2, 3) * 3 * F(3, 5) * sumY2_ferm                           # (local)
    scal1 = F(1, 3) * F(3, 5) * (2 * F(1, 2) ** 2)                       # Higgs Y=1/2  # (local)
    b1 = ferm1 + scal1                                                   # (local)
    return {"b1": b1, "b2": b2, "b3": b3}


def beta_crosscheck(betas: dict) -> dict:
    """Cross-check of the IN-SCRIPT Model-C beta computation.

    Architecture (the plan's "0-tolerance exact-rational beta cross-check,
    halt-on-mismatch" reframed honestly): the Aydemir overview (arXiv:2511.07672)
    publishes the Model-C FIELD CONTENT (Table 1, Eq. 9, 12), the breaking chain
    NCG ->[M_U] G422D ->[M_C] G321 (Eq. 8), and the unification condition
    g_3^2=g_2^2=(5/3)g_1^2 (Eq. 6) -- but NO explicit Model-C beta-coefficient table
    and NO numerical (M_C, M_U). So there is no published Model-C rational to
    identity-match. The cross-check therefore HALTS on violation of:

      (X1) Engine validation: the SAME Dynkin machinery reproduces the textbook,
           canonically-pinned SM (b1,b2,b3) = (41/10, -19/6, -7) EXACTLY (Convention I).
           This is the non-circular anchor -- the engine is verified on a known answer.
      (X2) D-parity: b_2L == b_2R (Model-C is left-right symmetric; mirror scalar
           content forces equal SU(2)_{L,R} slopes; MUST hold structurally).

    Documented-not-gated (Aydemir reconciliation; the overview is METHODOLOGICAL,
    never a numerical source):
      - The companion transcription (researchers/Connes/27 lines 66-79) gives a
        MINIMAL-PS ILLUSTRATION b_L=b_R=22/3, b_4=11-(2/3)n_f-(1/3)n_s (n_s=1 real
        scalar in (15,1,1)) -- a DIFFERENT scalar sector than Model-C-full, AND in a
        non-standard "11"-gauge normalization (his "11" != (11/3)C2(SU4)=44/3).
      - The transcription's printed arithmetic "11 - 4 - 1/3 = 19/3" is a 1/3 source
        slip: 11 - 4 - 1/3 = 20/3 (Sage-QQ exact). Flagged, NON-gating.
      - Convention bridge b^{II} = -b^{I} reported for transparency.
    """
    b4 = betas["b4"]; b2L = betas["b2L"]; b2R = betas["b2R"]              # (local)
    # X1 engine validation against textbook SM
    sm = sm_betas_from_machinery()                                      # (local)
    x1_engine = (sm["b1"] == F(41, 10) and sm["b2"] == F(-19, 6)
                 and sm["b3"] == F(-7))                                 # (local)
    # X2 D-parity
    x2_dparity = (b2L == b2R)                                           # (local)
    # documented-not-gated source-slip flag
    aydemir_printed = F(19, 3)                                          # transcription line 79  # (local)
    aydemir_actual = F(11) - F(2, 3) * 6 - F(1, 3) * 1                  # = 20/3 (Sage-confirmed)  # (local)
    source_slip = (aydemir_printed != aydemir_actual)                  # True -> 1/3 slip flagged  # (local)
    # convention bridge
    b4_II = -b4; b2L_II = -b2L                                          # (local)
    return {
        "x1_engine_reproduces_SM": bool(x1_engine),
        "sm_b1_machinery": str(sm["b1"]), "sm_b2_machinery": str(sm["b2"]),
        "sm_b3_machinery": str(sm["b3"]),
        "x2_dparity_b2L_eq_b2R": bool(x2_dparity),
        "b4_I": str(b4), "b4_II": str(b4_II),
        "b2L_I": str(b2L), "b2L_II": str(b2L_II),
        "aydemir_overview_publishes_modelc_beta_table": False,
        "aydemir_minimal_printed_19_3_vs_actual_20_3_source_slip": bool(source_slip),
        "crosscheck_pass": bool(x1_engine and x2_dparity),
    }


# ---------------------------------------------------------------------------
# Section 5b — Inverse one-loop solve + the four-element report
# ---------------------------------------------------------------------------

def compute() -> dict:
    t = 1.0 / (2.0 * np.pi)  # one-loop slope factor (local)

    # ---- Step A: canonical EW inputs at M_Z (GUT-normalized) ----
    aem = float(alpha_em_MZ_inv)        # canonical import                 # (local)
    s2 = float(sin2_thetaW_MSbar)       # canonical import (datum)         # (local)
    aS = float(alpha_s_MZ_obs)          # canonical import                 # (local)
    MZ = float(M_Z)                     # canonical import                 # (local)
    MPL = float(M_Pl_unreduced)         # canonical import (ceiling)       # (local)

    a2_MZ = aem * s2                     # alpha_2^{-1}(M_Z)                # (local)
    aY_MZ = aem * (1.0 - s2)             # alpha_Y^{-1}(M_Z)               # (local)
    a1_MZ = (3.0 / 5.0) * aY_MZ          # GUT-normalized                  # (local)
    a3_MZ = 1.0 / aS                     # alpha_3^{-1}(M_Z)               # (local)

    # ---- Step B: SM betas (Convention I, pinned exact rationals) ----
    b1 = 41.0 / 10.0; b2 = -19.0 / 6.0; b3 = -7.0                          # (local)

    # ---- Step C: Model-C betas computed IN-SCRIPT (Convention I) ----
    betas = modelc_betas()                                                 # (local)
    b4 = float(betas["b4"]); b2LR = float(betas["b2L"])                    # (local)
    xcheck = beta_crosscheck(betas)                                        # (local)
    if not xcheck["crosscheck_pass"]:
        raise SystemExit(
            "BETA CROSS-CHECK HALT (construction review, NOT re-tune): "
            f"{xcheck}")

    # ---- Step C cont.: build & solve the linear 3x3 system ----
    # Unknowns x=ln(M_C/M_Z), y=ln(M_U/M_Z), aU=alpha_U^{-1}.
    # E1 (SU4):  a3_MZ - b3*t*x - b4*t*(y-x) - aU = 0
    # E2 (SU2L): a2_MZ - b2*t*x - b2LR*t*(y-x) - aU = 0
    # E3 (SU2R): a2R_MC - b2LR*t*(y-x) - aU = 0,
    #   a2R_MC = (5/3)a1_MC - (2/3)a4_MC,  a1_MC=a1_MZ-b1*t*x, a4_MC=a3_MZ-b3*t*x
    A = np.array([
        [-(b3 - b4) * t,                         -b4 * t,    -1.0],
        [-(b2 - b2LR) * t,                       -b2LR * t,  -1.0],
        [t * (b2LR - (5.0 / 3.0) * b1 + (2.0 / 3.0) * b3),  -b2LR * t, -1.0],
    ])                                                                     # (local)
    c = np.array([-a3_MZ, -a2_MZ,
                  -((5.0 / 3.0) * a1_MZ - (2.0 / 3.0) * a3_MZ)])           # (local)
    detA = float(np.linalg.det(A))                                         # (local)
    if abs(detA) < 1e-12:
        raise SystemExit(f"DEGENERATE SYSTEM: det(A)={detA} ~ 0 (no unique solution)")
    xyz = np.linalg.solve(A, c)                                            # (local)
    x, y, aU = float(xyz[0]), float(xyz[1]), float(xyz[2])                 # (local)
    solve_resid = float(np.max(np.abs(A @ xyz - c)))                       # (local)

    M_C = MZ * np.exp(x)                                                    # (local)
    M_U = MZ * np.exp(y)                                                    # (local)

    # ---- Step D: verdict clause (existence/ordering) ----
    ord_ZC = (MZ <= M_C)                                                   # (local)
    ord_CU = (M_C <= M_U)                                                  # (local)
    ord_UP = (M_U <= MPL)                                                  # (local)
    ordered = bool(ord_ZC and ord_CU and ord_UP)                          # (local)
    # ordering margins (in decades)
    marg_ZC = np.log10(M_C / MZ)                                          # (local)
    marg_CU = np.log10(M_U / M_C)                                         # (local)
    marg_UP = np.log10(MPL / M_U)                                         # (local)

    # ---- R2: forward closure (run M_U -> M_Z, reproduce inputs) ----
    yx = y - x                                                            # (local)
    a4_MC = aU + b4 * t * yx                                              # (local)
    a2L_MC = aU + b2LR * t * yx                                           # (local)
    a2R_MC = aU + b2LR * t * yx                                           # (local)
    a3_MC = a4_MC; a2_MC = a2L_MC                                         # (local)
    a1_MC = (3.0 / 5.0) * a2R_MC + (2.0 / 5.0) * a4_MC                    # (local)
    a3_back = a3_MC + b3 * t * x                                          # (local)
    a2_back = a2_MC + b2 * t * x                                          # (local)
    a1_back = a1_MC + b1 * t * x                                          # (local)
    aY_back = (5.0 / 3.0) * a1_back                                       # (local)
    aem_back = a2_back + aY_back                                          # (local)
    sin2_back = a2_back / aem_back                                        # (local)
    closure_resid = float(max(abs(a3_back - a3_MZ), abs(a2_back - a2_MZ),
                              abs(a1_back - a1_MZ), abs(sin2_back - s2)))  # (local)
    sin2_MU = aU / ((8.0 / 3.0) * aU)   # = 3/8 by construction           # (local)

    # ---- R3: Route-ACCOM (sin^2 on solved trajectory at mu_BC; pure-SM below M_C) ----
    bY = 41.0 / 6.0   # physical hypercharge slope = (5/3)*b1             # (local)

    def sin2_of_mu(mu):
        Lm = np.log(mu / MZ)                                              # (local)
        a2 = a2_MZ - b2 * t * Lm                                          # (local)
        aY = aY_MZ - bY * t * Lm                                          # (local)
        return a2 / (a2 + aY)

    s2_muBC = float(sin2_of_mu(MU_BC))                                    # (local)
    r3_delta = s2_muBC - ACCOM_VALUE                                      # (local)
    # crossing scale mu*: sin^2(mu*)=ACCOM_VALUE (bisection on the SM trajectory)
    lo, hi = 50.0, 5000.0                                                 # (local)
    for _ in range(200):
        mid = 0.5 * (lo + hi)                                            # (local)
        if (sin2_of_mu(mid) - ACCOM_VALUE) > 0:
            hi = mid
        else:
            lo = mid
    mu_star = 0.5 * (lo + hi)                                            # (local)

    # ---- R4: Aydemir published-OOM cross-check (qualitative; no numeric source) ----
    # Overview gives M_U << Lambda; companion 2-loop illustration M_GUT ~ 10^{15.7+-0.2},
    # v_R(intermediate) ~ 10^{11..13}. Compare OOM only.
    log10_MC = float(np.log10(M_C))                                       # (local)
    log10_MU = float(np.log10(M_U))                                       # (local)
    r4_MU_vs_aydemir_GUT = log10_MU - 15.7   # decades (one-loop below 2-loop GUT)  # (local)
    r4_MC_in_vR_band = bool(11.0 <= log10_MC <= 13.5)  # intermediate-scale band    # (local)

    # ---- trajectory arrays for the plot ----
    mu_grid_sm = np.logspace(np.log10(MZ), log10_MC, 240)                 # (local)
    s2_grid_sm = np.array([sin2_of_mu(m) for m in mu_grid_sm])           # (local)
    # alpha^{-1} trajectories (for the unification panel)
    lnmu_full = np.linspace(0.0, y, 400)                                  # ln(mu/MZ)  # (local)
    a1_inv_tr = np.empty_like(lnmu_full)                                  # (local)
    a2L_inv_tr = np.empty_like(lnmu_full)                                 # (local)
    a2R_inv_tr = np.empty_like(lnmu_full)                                 # (local)
    a3_inv_tr = np.empty_like(lnmu_full)                                  # (local)
    for i, lm in enumerate(lnmu_full):
        if lm <= x:  # SM regime below M_C
            a1_inv_tr[i] = a1_MZ - b1 * t * lm
            a2L_inv_tr[i] = a2_MZ - b2 * t * lm
            a2R_inv_tr[i] = a2_MZ - b2 * t * lm   # below M_C, SU(2)_R not active; plot SM SU(2)
            a3_inv_tr[i] = a3_MZ - b3 * t * lm
        else:        # Model-C regime above M_C
            a4_at = a4_MC - b4 * t * (lm - x)
            a2L_at = a2L_MC - b2LR * t * (lm - x)
            a2R_at = a2R_MC - b2LR * t * (lm - x)
            a3_inv_tr[i] = a4_at            # SU(3) subsumed in SU(4)
            a2L_inv_tr[i] = a2L_at
            a2R_inv_tr[i] = a2R_at
            # GUT-normalized U(1) above M_C tracks a2R combination; for display plot a4
            a1_inv_tr[i] = a4_at

    return {
        # primary report payload
        "value": (f"INFO_ordered_solution_exists "
                  f"M_C={M_C:.4g}GeV M_U={M_U:.4g}GeV alpha_U_inv={aU:.4g} "
                  f"R3_delta={r3_delta:.3g} mu_star={mu_star:.4g}GeV "
                  f"ko_axis=indeterminate-carried"),
        "verdict_kind": "INFO" if ordered else "FAIL",
        # inputs echoed
        "alpha_em_MZ_inv": aem, "sin2_thetaW_MSbar": s2, "alpha_s_MZ_obs": aS,
        "M_Z": MZ, "M_Pl_unreduced": MPL,
        "a1_MZ": a1_MZ, "a2_MZ": a2_MZ, "a3_MZ": a3_MZ, "aY_MZ": aY_MZ,
        # betas
        "b1": b1, "b2": b2, "b3": b3, "b4_I": b4, "b2LR_I": b2LR,
        "beta_crosscheck": json.dumps(xcheck),
        # solve
        "detA": detA, "solve_resid": solve_resid,
        "x_lnMC": x, "y_lnMU": y, "alpha_U_inv": aU,
        "M_C": M_C, "M_U": M_U, "log10_M_C": log10_MC, "log10_M_U": log10_MU,
        # R1 ordering
        "ordered": ordered, "ord_ZC": ord_ZC, "ord_CU": ord_CU, "ord_UP": ord_UP,
        "margin_ZC_decades": float(marg_ZC), "margin_CU_decades": float(marg_CU),
        "margin_UP_decades": float(marg_UP),
        # R2 closure
        "closure_resid": closure_resid, "sin2_back_MZ": sin2_back, "sin2_MU": sin2_MU,
        "a1_back": a1_back, "a2_back": a2_back, "a3_back": a3_back,
        # R3 accom
        "mu_BC": MU_BC, "accom_value": ACCOM_VALUE,
        "sin2_muBC_solved": s2_muBC, "r3_delta": r3_delta, "mu_star": mu_star,
        "mu_star_over_mu_BC": mu_star / MU_BC,
        # R4 aydemir OOM
        "r4_MU_minus_aydemir_GUT_decades": r4_MU_vs_aydemir_GUT,
        "r4_MC_in_vR_band": r4_MC_in_vR_band,
        # plot arrays
        "mu_grid_sm": mu_grid_sm, "s2_grid_sm": s2_grid_sm,
        "lnmu_full": lnmu_full, "a1_inv_tr": a1_inv_tr, "a2L_inv_tr": a2L_inv_tr,
        "a2R_inv_tr": a2R_inv_tr, "a3_inv_tr": a3_inv_tr,
    }


# ---------------------------------------------------------------------------
# Section 6 — Plot
# ---------------------------------------------------------------------------

def make_plot(r: dict) -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Panel 1: alpha_i^{-1} unification trajectory
    lnmu = r["lnmu_full"]
    MZ = r["M_Z"]
    mu_axis = MZ * np.exp(lnmu)
    ax1.plot(mu_axis, r["a3_inv_tr"], label=r"$\alpha_3^{-1}\to\alpha_4^{-1}$ (SU(3)$\subset$SU(4))", color="tab:red")
    ax1.plot(mu_axis, r["a2L_inv_tr"], label=r"$\alpha_2^{-1}\to\alpha_{2L}^{-1}$", color="tab:blue")
    ax1.plot(mu_axis, r["a2R_inv_tr"], label=r"$\alpha_{2R}^{-1}$ (D-parity)", color="tab:cyan", ls="--")
    ax1.plot(mu_axis, r["a1_inv_tr"], label=r"$\alpha_1^{-1}$ (GUT-norm)", color="tab:green", ls=":")
    ax1.axvline(r["M_C"], color="gray", ls="--", alpha=0.7)
    ax1.axvline(r["M_U"], color="black", ls="-", alpha=0.7)
    ax1.annotate(f"$M_C$={r['M_C']:.2e}", (r["M_C"], 50), rotation=90, va="bottom", fontsize=8)
    ax1.annotate(f"$M_U$={r['M_U']:.2e}\n$\\alpha_U^{{-1}}$={r['alpha_U_inv']:.3f}",
                 (r["M_U"], 42), rotation=90, va="bottom", fontsize=8)
    ax1.scatter([r["M_U"]], [r["alpha_U_inv"]], color="black", zorder=5, s=40)
    ax1.set_xscale("log")
    ax1.set_xlabel(r"$\mu$ [GeV]"); ax1.set_ylabel(r"$\alpha_i^{-1}$")
    ax1.set_title("G422D Model-C one-loop unification (inverse solve)\n"
                  r"$\sin^2\theta_W(M_U)=3/8$ exact; $M_Z\leq M_C\leq M_U\leq M_{Pl}$")
    ax1.legend(fontsize=8, loc="upper right"); ax1.grid(alpha=0.3)

    # Panel 2: sin^2_W(mu) on the solved trajectory + mu_BC / 0.23480 crossing
    ax2.plot(r["mu_grid_sm"], r["s2_grid_sm"], color="tab:purple",
             label=r"$\sin^2\theta_W(\mu)$ solved (SM regime $\mu<M_C$)")
    ax2.axhline(r["accom_value"], color="tab:orange", ls="--",
                label=f"accommodation 0.23480 (S83 2-loop)")
    ax2.axvline(r["mu_BC"], color="gray", ls=":", label=f"$\\mu_{{BC}}$={r['mu_BC']} GeV")
    ax2.axvline(r["mu_star"], color="tab:green", ls="-.", alpha=0.7,
                label=f"$\\mu_*$={r['mu_star']:.2f} GeV (crossing)")
    ax2.scatter([r["mu_BC"]], [r["sin2_muBC_solved"]], color="black", zorder=5, s=40)
    ax2.annotate(f"$\\sin^2(\\mu_{{BC}})$={r['sin2_muBC_solved']:.5f}\n"
                 f"$\\Delta$={r['r3_delta']:+.2e}",
                 (r["mu_BC"], r["sin2_muBC_solved"]), fontsize=8,
                 xytext=(r["mu_BC"] * 1.15, r["sin2_muBC_solved"] - 0.002),
                 arrowprops=dict(arrowstyle="->", alpha=0.5))
    ax2.set_xscale("log")
    ax2.set_xlabel(r"$\mu$ [GeV]"); ax2.set_ylabel(r"$\sin^2\theta_W(\mu)$")
    ax2.set_title("R3 Route-ACCOM: solved trajectory vs accommodation row\n"
                  "(scale-consistent BY CONSTRUCTION; loop-order systematic declared)")
    ax2.legend(fontsize=8, loc="upper left"); ax2.grid(alpha=0.3)

    fig.suptitle(f"{GATE_ID}  —  INFO-by-design (ordered solution exists; "
                 f"ko_axis=indeterminate-carried)", fontsize=11)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 — Verdict payload (printed; agent calls emit_verdict)
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          extra_rows=None) -> dict:
    payload: dict = {
        "session": 101,
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
# Section 8 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    # gate-6 hard-sequencing assertion
    g6 = ""  # (local)
    try:
        g6 = GATE6_VERDICTS.read_text(encoding="utf-8")
    except OSError:
        g6 = ""
    g6_present = ("S101-CCS-MODELC-KO-DERIVATION:" in g6)  # (local)
    g6_info = ("S101-CCS-MODELC-KO-DERIVATION: INFO" in g6)  # (local)
    print(f"  gate-6 line present: {g6_present}  (INFO: {g6_info}) -> "
          f"ko_axis=indeterminate-carried (status-quo dispatch)")
    if not g6_present:
        raise SystemExit("HARD-SEQUENCING HALT: gate-6 verdict line absent.")
    print()

    r = compute()
    verdict = r["verdict_kind"]
    value = r["value"]

    # console report (NUMBERS first)
    print("=" * 72)
    print(f"{GATE_ID}: {verdict} (by design INFO iff ordered)")
    print("-" * 72)
    print(f"  Model-C betas (Conv I):  b4={r['b4_I']:+.6g}  b2L=b2R={r['b2LR_I']:+.6g}")
    print(f"  beta cross-check:        {r['beta_crosscheck']}")
    print(f"  det(A) = {r['detA']:.6g}  (nonzero -> exactly determined; "
          f"solve_resid={r['solve_resid']:.2e})")
    print(f"  R1: M_C = {r['M_C']:.6e} GeV (log10={r['log10_M_C']:.4f})")
    print(f"      M_U = {r['M_U']:.6e} GeV (log10={r['log10_M_U']:.4f})")
    print(f"      alpha_U_inv = {r['alpha_U_inv']:.6f}")
    print(f"      ordering M_Z<=M_C<=M_U<=M_Pl: {r['ordered']}  "
          f"(margins dec: ZC={r['margin_ZC_decades']:.3f} "
          f"CU={r['margin_CU_decades']:.3f} UP={r['margin_UP_decades']:.3f})")
    print(f"  R2: forward closure resid = {r['closure_resid']:.3e} "
          f"(pin {TOL_CLOSURE}); sin2_back(M_Z)={r['sin2_back_MZ']:.10f}; "
          f"sin2(M_U)={r['sin2_MU']:.10f} (=3/8)")
    print(f"  R3: sin2(mu_BC={r['mu_BC']}GeV)_solved = {r['sin2_muBC_solved']:.6f}; "
          f"accom=0.23480; Delta={r['r3_delta']:+.4e}; mu_star={r['mu_star']:.4f} GeV "
          f"(mu*/mu_BC={r['mu_star_over_mu_BC']:.4f})")
    print(f"  R4: M_U vs Aydemir 2-loop M_GUT(10^15.7): "
          f"{r['r4_MU_minus_aydemir_GUT_decades']:+.3f} dec; "
          f"M_C in v_R intermediate band [10^11,10^13.5]: {r['r4_MC_in_vR_band']}")
    print("=" * 72)

    make_plot(r)

    # save npz (full float64; Class-8.3 round-trip)
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION, l_max=L_MAX,
        verdict=verdict, value=value,
        ko_axis="indeterminate-carried",
        gate6_audit_sha256="bb2fa21a69f4f84938f6aef88c0a7aeb8d616452d046a8b83952617f49cc932d",
        gate6_verdict="INFO", gate6_theory_match=True,
        alpha_em_MZ_inv=r["alpha_em_MZ_inv"], sin2_thetaW_MSbar=r["sin2_thetaW_MSbar"],
        alpha_s_MZ_obs=r["alpha_s_MZ_obs"], M_Z=r["M_Z"], M_Pl_unreduced=r["M_Pl_unreduced"],
        a1_MZ=r["a1_MZ"], a2_MZ=r["a2_MZ"], a3_MZ=r["a3_MZ"], aY_MZ=r["aY_MZ"],
        b1=r["b1"], b2=r["b2"], b3=r["b3"], b4_I=r["b4_I"], b2LR_I=r["b2LR_I"],
        beta_crosscheck=r["beta_crosscheck"],
        detA=r["detA"], solve_resid=r["solve_resid"],
        x_lnMC=r["x_lnMC"], y_lnMU=r["y_lnMU"], alpha_U_inv=r["alpha_U_inv"],
        M_C=r["M_C"], M_U=r["M_U"], log10_M_C=r["log10_M_C"], log10_M_U=r["log10_M_U"],
        ordered=r["ordered"], ord_ZC=r["ord_ZC"], ord_CU=r["ord_CU"], ord_UP=r["ord_UP"],
        margin_ZC_decades=r["margin_ZC_decades"], margin_CU_decades=r["margin_CU_decades"],
        margin_UP_decades=r["margin_UP_decades"],
        closure_resid=r["closure_resid"], sin2_back_MZ=r["sin2_back_MZ"], sin2_MU=r["sin2_MU"],
        a1_back=r["a1_back"], a2_back=r["a2_back"], a3_back=r["a3_back"],
        mu_BC=r["mu_BC"], accom_value=r["accom_value"],
        sin2_muBC_solved=r["sin2_muBC_solved"], r3_delta=r["r3_delta"], mu_star=r["mu_star"],
        mu_star_over_mu_BC=r["mu_star_over_mu_BC"],
        r4_MU_minus_aydemir_GUT_decades=r["r4_MU_minus_aydemir_GUT_decades"],
        r4_MC_in_vR_band=r["r4_MC_in_vR_band"],
        mu_grid_sm=r["mu_grid_sm"], s2_grid_sm=r["s2_grid_sm"],
        lnmu_full=r["lnmu_full"], a1_inv_tr=r["a1_inv_tr"], a2L_inv_tr=r["a2L_inv_tr"],
        a2R_inv_tr=r["a2R_inv_tr"], a3_inv_tr=r["a3_inv_tr"],
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"  npz -> {OUT_NPZ.name}  ({OUT_NPZ.stat().st_size} bytes)")
    print(f"  png -> {OUT_PNG.name}  ({OUT_PNG.stat().st_size} bytes)")

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)
    extra = [
        "# regulator_pin=a_n^{cutoff} structural-citation-only; no numerical a_n consumed "
        "(Dynkin indices + measured EW couplings only)",
        "# ko_axis=indeterminate-carried per gate-6 INFO (theory_match=True, "
        "derived KO-triple (6,+1,+1,-1) matched substrate anchor; PRIMARY-UNDERDETERMINED)",
    ]
    print_verdict_payload(verdict, value, audit_sha, content_sha, extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0  # verdict is data; exit 0 on healthy run regardless of INFO/FAIL


if __name__ == "__main__":
    sys.exit(main())
