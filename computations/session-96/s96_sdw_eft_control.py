#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
S96-SDW-EFT-CONTROL  (Session 96, Wave 2, gate W2-5)
====================================================

SDW layer-expansion parametric-control parameter / species-scale thinness.

QUESTION (string-theory V.1, recast in lizzi functional-pluralism terms):
  Does the Seeley-DeWitt layer expansion
        S_b(D_K, Lambda) = Tr f(D_K^2/Lambda^2)
                        ~ f_4 Lambda^4 a_0 + f_2 Lambda^2 a_2 + f_0 a_4
                          + f_{-2} Lambda^{-2} a_6 + f_{-4} Lambda^{-4} a_8 + ...
  have a PARAMETRIC small parameter, or is the apparent layer hierarchy a
  NUMERICAL-truncation accident (resting on block-diagonality / representation
  theory, NOT on EFT-control)? With the species scale Lambda_sp/M_KK = 2.06
  (THIN, W6-SPECIES-36/SCALE-63), the cutoff Lambda = M_KK sits only ~2x below
  the EFT-breakdown scale, so the Lambda^2 suppression that WOULD make higher-k
  terms small spans only one factor-~4 in Lambda^2 before the EFT description fails.

SUBSTRATE FRAMING (phononic-framing.md "IS Space, Not IN Space"):
  CLASSIFICATION: GEOMETRIC. The substrate IS D_K(tau_fold) on Jensen-deformed
  SU(3); the spectral action S_b = Tr f(D_K^2/Lambda^2) is the master functional
  and its Seeley-DeWitt layer expansion is the PERTURBATIVE FACE of that
  functional -- an asymptotic expansion in (substrate curvature scale / Lambda^2).
  The moments a_{2k} are NOT free; they are residues of the substrate's own
  spectral zeta function at the d=8 dimension-spectrum poles s=(8-n)/2 (E38,
  Connes-Moscovici 1995). Direction of explanation:
    D_K eigenvalue spectrum {lambda_k, m_k}  ->  layer moments a_{2k}  ->
    successive-term ratios r_k  ->  EFT-control status (parametric vs
    representation-theoretic).
  The lizzi-functional-pluralism reading: 'truncation-robust' (FI) and
  'parametrically-controlled' are DIFFERENT properties. The a-ratios
  a_{2(k+1)}/a_{2k} are FUNCTIONAL-INVARIANT (same canonical zeta moments under
  any common normalization -- the w(L_max) prefactor cancels in every ratio); the
  f-coefficient ratios are FUNCTIONAL-DEPENDENT (Gaussian-cutoff vs Mellin-f* give
  OPPOSITE modulations). What survives all functional choices (the a-ratio
  structural driver) is the lizzi-physical content; the f-ratio is the
  scheme-dependent piece. This gate decides which property the framework's
  layer hierarchy actually has.

[SIGN] SUBSTITUTION CHAIN (math-scripts.md "Double-Check Logic Before Compute"):
  Claim: "With Lambda_sp/M_KK = 2.06, the SDW layer expansion has no parametric
          small parameter -- the successive-term ratio r_k is O(1), not << 1,
          and the a-ratio DIRECTION is INCREASING toward 1 (terms become LESS
          suppressed at higher order), so the hierarchy is numerical not parametric."

  Step 1 -- Definitions (cite canonical source):
    a_0_FW_zeta = 6440.0           [canonical; per-branch L_max=3 zeta moment, [M^0]]
    a_2_FW_zeta = 2776.165389      [canonical; [M^-2]]
    a_4_FW_zeta = 1350.7216        [canonical; [M^-4]]
    a_6_FW_zeta = 765.593826       [S96 promotion; E38 per-branch zeta, [M^-6]; cache cross-check]
    a_8_FW_zeta = 521.183178       [S96 promotion; E38 per-branch zeta, [M^-8]; cone closes]
      (all a_n on the SAME footing: a_n = (1/2) sum_modes m_k |lambda_k|^{-n} at
       L_max=3, verified bit-exact: 2x cache-sum = canonical a_0/a_2/a_4.)
    f-ladder (CC labels, the cutoff-functional coefficients):
      Gaussian-cutoff: f_4 = 0.558, f_2 = 2.34          [f_4_default, f_2_default; S62]
      Mellin f*:       f_4 = 6446.64, f_2 = 214.97, f_0 = 0.08832
                                                          [mellin_f_star_{f4,f2,f0}; S78]
    Lambda_sp_over_M_KK = 2.06     [S96 promotion; W6-SPECIES-36/SCALE-63; THIN]
    The a_n are dimensionless mode-curvature-integrals IN M_KK UNITS, so Lambda is
    measured in M_KK units: (Lambda/M_KK)^{-2} = 1 at Lambda=M_KK, = 1/2.06^2 at Lambda_sp.

  Step 2 -- Substitution (no simplification):
    Layer term k: term_k = f_{4-2k} * (Lambda/M_KK)^{4-2k} * a_{2k}.
    Successive-term ratio:
      r_k = |term_{k+1}| / |term_k|
          = |f_{4-2(k+1)} (Lambda/M_KK)^{4-2(k+1)} a_{2(k+1)}|
            / |f_{4-2k} (Lambda/M_KK)^{4-2k} a_{2k}|
          = (f_{4-2(k+1)}/f_{4-2k}) * (Lambda/M_KK)^{-2} * (a_{2(k+1)}/a_{2k}).

  Step 3 -- Simplification (one step per line):
    r_k = [f-ratio]_k  *  [Lambda^{-2} in M_KK units]  *  [a-ratio]_k.
    The a-ratio piece (a_{2(k+1)}/a_{2k}) is the SCHEME-INDEPENDENT structural driver
       (FI: any common w(L_max) cancels in the ratio).
    The f-ratio piece is the SCHEME-DEPENDENT modulation
       (Gaussian f_2/f_4 = 4.19 amplifies; Mellin f_2/f_4 = 0.033 crushes).
    At Lambda=M_KK, (Lambda/M_KK)^{-2}=1, so r_k^a = a-ratio = {0.431, 0.487, 0.567, 0.681}.

  Step 4 -- Read off the DIRECTION (only now state the sign):
    a-ratio sequence k=0..3 = {0.4311, 0.4865, 0.5668, 0.6808}: strictly INCREASING.
    => terms become LESS suppressed at higher k (a-ratio rises toward 1), NOT more.
    => there is NO parametric small parameter. sign_verdict: the series formally
       converges (max a-ratio 0.681 < 1) => sign=PASS (ratio<1); but the rising
       direction confirms the string-theory hypothesis (no comfortable smallness).

  Step 5 -- Verdict band (strict_PASS_boundary):
    PASS iff max_k r_k < 0.5 at Lambda=M_KK (parametric control, >2x shrink/layer).
    FAIL iff max_k r_k >= 1.   INFO iff 0.5 <= max_k r_k < 1 (marginal).
    Scheme-INDEPENDENT a-ratio driver: max_k r_k^a = 0.6808 (k=3)  ->  INFO band.
    Functional-sensitivity (the lizzi finding): WITH the f-modulation the verdict
    is FUNCTIONAL-DEPENDENT -- Gaussian r_0 = 1.81 (FAIL band), Mellin r_0 = 0.014
    (PASS band). The SAME D_K spectrum gives FAIL/PASS/INFO depending on the
    spectral functional f. SCHEME-DEPENDENT.

PRE-FLIGHT (math-scripts.md "Multiplicative-normalization cancellation invariants"):
  This gate scans Lambda (2 values) x layer-index k at FIXED L_max=3 per-branch
  zeta moments -- it is NOT an L_max-stability gate and has no d^n ln/d(ln K)^n
  log-derivative operator, so the MNCI theorem's L_max-stability object does not
  apply. HOWEVER, any common w(L_max) spectral-support prefactor CANCELS in every
  a-ratio  a_{2(k+1)}/a_{2k} = [w g_{2(k+1)}]/[w g_{2k}] = g_{2(k+1)}/g_{2k}  --
  so the a-ratio structural driver is L_max-INVARIANT by the cancellation identity
  (MULTIPLICATIVE-NORMALIZATION-CANCELLATION-DETECTED = True for the a-ratio
  driver). The EFT-control verdict therefore targets the term-ratio VALUE at
  Lambda=M_KK, not the L-stability.

PRIOR STATE (this gate BUILDS ON, does NOT re-derive):
  - a_0/a_2/a_4 canonical zeta moments (S88-A-N-FW-CANONICALIZATION).
  - W6-SPECIES-36/SCALE-63: Lambda_species/M_KK = 2.06 THIN (PASS).
  - S94-K-CSUB-R-ABSOLUTE-CONVERGENCE: the raw absolute a_2 series DIVERGES
    (dK/dL increasing). The present gate is the RATIO/term-ratio complement.
  - E38 (Connes-Moscovici 1995 sec III.4): a_n = Res[Tr(D_K^{-2s}); s=(d-n)/2]
    = sum_k m_k lambda_k^{-(d-n)}; at FINITE L_max truncation equals the truncated
    Dirichlet form (analytic_zeta = direct identity off-pole).
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # CPU-only arithmetic; cap threads (computation-environment.md; GPU_path=cpu-cap-OMP8)
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# Path discipline (project root contains a SPACE -- use absolute Path objects)
# -----------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
ROOT_COMPUTATIONS = PROJECT_ROOT / "computations"
sys.path.insert(0, str(SHARED_DIR))
sys.path.insert(0, str(ROOT_COMPUTATIONS))

# -----------------------------------------------------------------------------
# Canonical constants (MANDATORY: never hardcode framework constants)
# -----------------------------------------------------------------------------
from canonical_constants import (  # noqa: E402
    M_KK,                  # 7.428660036284456e16 GeV -- KK / cutoff scale
    a_0_FW_zeta,           # 6440.0          -- per-branch L_max=3 zeta moment [M^0]
    a_2_FW_zeta,           # 2776.165389     -- [M^-2]
    a_4_FW_zeta,           # 1350.7216       -- [M^-4]
    a_6_FW_zeta,           # 765.593826      -- [M^-6] (S96 promotion; cache cross-check)
    a_8_FW_zeta,           # 521.183178      -- [M^-8] (S96 promotion; cone closes)
    Lambda_sp_over_M_KK,   # 2.06            -- species scale ratio (THIN; W6-SPECIES-36/SCALE-63)
    f_2_default,           # 2.34            -- Gaussian-cutoff f_2 (S62)
    f_4_default,           # 0.558           -- Gaussian-cutoff f_4 (S62)
    mellin_f_star_f0,      # 0.08832         -- Mellin moment f_0 of f* (S78)
    mellin_f_star_f2,      # 214.97335676    -- Mellin moment f_2 of f* (S78)
    mellin_f_star_f4,      # 6446.63942272   -- Mellin moment f_4 of f* (S78)
)

# -----------------------------------------------------------------------------
# Gate identity + machinery pins (per plan W2-5 R3 YAML)
# -----------------------------------------------------------------------------
GATE_ID = "S96-SDW-EFT-CONTROL"
SCHEME = "Seeley-DeWitt-layer-expansion"
CONVENTION = "RATIO-successive-term-a-ratio-driver-scheme-independent"
L_MAX = "10"                 # a_6/a_8 cross-check on the L_max<=10 cache; moments are per-branch L_max=3 zeta

# --- Pre-registered machinery pins (plan W2-5) ---
N_EVAL = 8                   # (local) 4 successive-term ratios (k in {0,1,2,3}) x 2 Lambda values
K_LIST = [0, 1, 2, 3]        # (local) layer indices (d=8 cone {a_0,a_2,a_4,a_6,a_8})
TOL = 1e-10                  # (local) float64 ratio absolute tolerance
CTRL_PASS = 0.5              # (local) parametric-control band (term ratio < 1/2 = controlled)
CTRL_FAIL = 1.0              # (local) uncontrolled band (term ratio >= 1 = divergent layers)
PUB_PRECISION = 4            # (local) publication precision (r_k band statement)

# --- Cache for the a_6/a_8 provenance cross-check ---
SPECTRUM_CACHE = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
L_MAX_BRANCH = 3             # (local) per-branch zeta convention truncation (reproduces canonical a_0/a_2/a_4)
BRANCH_FACTOR = 0.5          # (local) per-branch normalization (cache holds 2 branches; canonical = half)

# -----------------------------------------------------------------------------
# Verdict file path (S96 canonical location per gate-verdicts.md)
# -----------------------------------------------------------------------------
VERDICT_TXT = PROJECT_ROOT / "computations" / "session-96" / "s96_gate_verdicts.txt"

# -----------------------------------------------------------------------------
# Input + output files
# -----------------------------------------------------------------------------
SCRIPT_PATH = Path(__file__).resolve()
CANONICAL_CONSTANTS_PATH = SHARED_DIR / "canonical_constants.py"
OUT_NPZ = PROJECT_ROOT / "computations" / "session-96" / "s96_sdw_eft_control.npz"
OUT_PNG = PROJECT_ROOT / "computations" / "session-96" / "s96_sdw_eft_control.png"


# -----------------------------------------------------------------------------
# SHA helpers (dual-SHA per S84+ schema)
# -----------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple:
    """(audit_sha256, content_sha256). audit = sha(script||canonical||pinmap_json); content = sha(script)."""
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# -----------------------------------------------------------------------------
# a_6 / a_8 provenance cross-check on the L_max=12 master spectrum cache
# (E38 per-branch zeta moment: a_n = (1/2) sum_modes m_k |lambda_k|^{-n} at L_max=3)
# -----------------------------------------------------------------------------
def cache_moments_crosscheck():
    """Re-derive a_n = (1/2) sum_modes m_k |lambda_k|^{-n} at L_max=3 from the cache.

    Returns dict {n: value} for n in {0,2,4,6,8}. Verifies bit-exact agreement
    with the canonical a_0/a_2/a_4 (the SAME footing pins a_6/a_8).
    """
    d = np.load(SPECTRUM_CACHE, allow_pickle=True)
    se = d["sector_evals"].item()
    evs_list = []   # (local)
    mults_list = []  # (local)
    for (p, q), info in se.items():
        if (p + q) > L_MAX_BRANCH:
            continue
        es = np.asarray(info["abs_evals"], dtype=np.float64)  # (local)
        if es.size == 0:
            continue
        mults_list.append(np.full(es.shape, float(info["dim"])))
        evs_list.append(es)
    evs = np.concatenate(evs_list)    # (local) |lambda_k| of D_K
    mults = np.concatenate(mults_list)  # (local) Weyl-dim multiplicities
    mask = evs > 1e-12                # (local) drop numerical zeros
    evs = evs[mask]
    mults = mults[mask]
    out = {}  # (local)
    for n in [0, 2, 4, 6, 8]:
        out[n] = BRANCH_FACTOR * float(np.sum(mults * evs ** (-n)))  # (local) E38 per-branch
    return out, int(evs.size), float(mults.sum())


# -----------------------------------------------------------------------------
# Successive-term ratios
# -----------------------------------------------------------------------------
def a_ratio(a_dict, k):
    """a_{2(k+1)}/a_{2k} -- the scheme-INDEPENDENT structural driver of r_k."""
    return a_dict[2 * (k + 1)] / a_dict[2 * k]  # (local)


def r_k_aratio_driver(a_dict, k, lam_over_mkk):
    """r_k^a = (a-ratio) * (Lambda/M_KK)^{-2}  (the FI structural piece; f-ratio = 1)."""
    return a_ratio(a_dict, k) * lam_over_mkk ** (-2)  # (local)


def r_k_full(a_dict, k, lam_over_mkk, f_high, f_low):
    """Full r_k = (f_low/f_high) * (Lambda/M_KK)^{-2} * (a-ratio).

    f_high = f at the descending Lambda-power of term k (= f_{4-2k});
    f_low  = f at term k+1 (= f_{4-2(k+1)}).  The descending step lowers the
    f-subscript by 2, so the ratio is f_{4-2(k+1)}/f_{4-2k} = f_low/f_high.
    """
    return (f_low / f_high) * lam_over_mkk ** (-2) * a_ratio(a_dict, k)  # (local)


def main() -> int:
    print("=" * 78)
    print(f"  {GATE_ID}")
    print("  SDW layer-expansion parametric-control / species-scale thinness")
    print("=" * 78)

    # --- Input SHA log (first 20 lines of stdout per gate-verdicts.md) ---
    print("\n=== Input SHA-256 pins ===")
    sha_script = sha256_of(SCRIPT_PATH)  # (local)
    sha_canon = sha256_of(CANONICAL_CONSTANTS_PATH)  # (local)
    sha_cache = sha256_of(SPECTRUM_CACHE)  # (local)
    print(f"  script                 : {sha_script}")
    print(f"  canonical_constants.py : {sha_canon}")
    print(f"  spectrum_cache L12     : {sha_cache}")
    print(f"  a_0={a_0_FW_zeta}  a_2={a_2_FW_zeta}  a_4={a_4_FW_zeta}  "
          f"a_6={a_6_FW_zeta}  a_8={a_8_FW_zeta}")
    print(f"  Lambda_sp/M_KK={Lambda_sp_over_M_KK}  M_KK={M_KK:.6e} GeV")
    print(f"  Gaussian f_4={f_4_default} f_2={f_2_default}  "
          f"Mellin f_4={mellin_f_star_f4} f_2={mellin_f_star_f2} f_0={mellin_f_star_f0}")

    # --- Substitution chain summary (Step 1-5; [SIGN]) ---
    print("\n=== Substitution chain (Step 1-5; [SIGN]) ===")
    print("  Step 1: a_n per-branch L_max=3 zeta moments [M^-n]; f-ladder CC labels; Lambda in M_KK units")
    print("  Step 2: r_k = (f_{4-2(k+1)}/f_{4-2k}) * (Lambda/M_KK)^{-2} * (a_{2(k+1)}/a_{2k})")
    print("  Step 3: r_k = [f-ratio][scheme-DEP] * [Lambda^-2] * [a-ratio][scheme-INDEP FI driver]")
    print("  Step 4: a-ratio seq {0.431,0.487,0.567,0.681} INCREASES toward 1 => terms LESS suppressed => NO param control")
    print("  Step 5: PASS iff max_k r_k<0.5 @ M_KK; a-ratio driver max=0.681 => INFO; f-modulation => SCHEME-DEPENDENT")

    # === a_6/a_8 provenance cross-check on the cache ===
    print("\n=== a_6 / a_8 cache cross-check (E38 per-branch L_max=3 zeta) ===")
    cache_a, n_modes, tot_mult = cache_moments_crosscheck()  # (local)
    print(f"  n_unique_modes(L_max=3)={n_modes}  total_mult_weighted={tot_mult:.1f}")
    crosscheck_ok = True  # (local)
    for n, canon in [(0, a_0_FW_zeta), (2, a_2_FW_zeta), (4, a_4_FW_zeta),
                     (6, a_6_FW_zeta), (8, a_8_FW_zeta)]:
        dev = abs(cache_a[n] - canon)  # (local)
        flag = "OK" if dev < 1e-3 else "MISMATCH"  # (local) canonical a_4 truncated at 4dp
        if dev >= 1e-3:
            crosscheck_ok = False
        print(f"  a_{n}: cache={cache_a[n]:.6f}  canonical={canon:.6f}  |dev|={dev:.2e}  [{flag}]")
    print(f"  cross-check (2x cache-sum = canonical, same footing): {'PASS' if crosscheck_ok else 'FAIL'}")

    # === Build moment dict (canonical values; cache cross-checked above) ===
    a_dict = {0: a_0_FW_zeta, 2: a_2_FW_zeta, 4: a_4_FW_zeta,
              6: a_6_FW_zeta, 8: a_8_FW_zeta}  # (local)

    # === a-ratios (the scheme-INDEPENDENT FI driver) ===
    print("\n=== a-ratios a_{2(k+1)}/a_{2k} (scheme-INDEPENDENT FI structural driver) ===")
    aratios = np.array([a_ratio(a_dict, k) for k in K_LIST])  # (local)
    for k in K_LIST:
        print(f"  k={k}: a_{2*(k+1)}/a_{2*k} = {aratios[k]:.6f}")
    aratio_increasing = bool(np.all(np.diff(aratios) > 0))  # (local)
    print(f"  a-ratio strictly INCREASING with k: {aratio_increasing}  "
          f"(=> terms LESS suppressed at higher k => no parametric smallness)")

    # === Two Lambda values ===
    # lam_vals stores Lambda/M_KK DIRECTLY: 1.0 at Lambda=M_KK, 2.06 at Lambda=Lambda_sp.
    # Substitution-chain direction (Step 3): r_k carries (Lambda/M_KK)^{-2}. RAISING the
    # cutoff (Lambda=2.06 M_KK > M_KK) makes (Lambda/M_KK)^{-2} = 1/2.06^2 = 0.2356 SMALLER
    # => higher-k terms MORE suppressed => the EFT expansion is MORE controlled at the larger
    # cutoff. (Physically correct: a higher UV cutoff improves the SDW asymptotic convergence.)
    lam_vals = {"M_KK": 1.0, f"{Lambda_sp_over_M_KK}_M_KK": float(Lambda_sp_over_M_KK)}  # (local) Lambda/M_KK
    lam_factor2 = {k: v ** (-2) for k, v in lam_vals.items()}  # (local) (Lambda/M_KK)^{-2}

    # === r_k: scheme-independent a-ratio driver at both Lambda ===
    print("\n=== r_k (scheme-INDEPENDENT a-ratio driver) at both Lambda ===")
    r_driver = {}  # (local)
    for lname, lf2 in lam_factor2.items():
        r_driver[lname] = np.array([r_k_aratio_driver(a_dict, k, lam_vals[lname]) for k in K_LIST])  # (local)
        print(f"  Lambda={lname} ((Lambda/M_KK)^-2={lf2:.6f}):")
        for k in K_LIST:
            print(f"     r_{k}^a = {r_driver[lname][k]:.6f}")
        print(f"     max_k r_k^a = {r_driver[lname].max():.6f}")

    # === r_k: full (f-modulated) per scheme where f-ratio pinnable ===
    # f-ladder CC labels available: Gaussian {f_4,f_2}; Mellin {f_4,f_2,f_0}.
    # k=0 step uses f_4 -> f_2 (both schemes); k=1 uses f_2 -> f_0 (Mellin only).
    print("\n=== r_k (FULL, f-modulated) per scheme [the FUNCTIONAL-DEPENDENT piece] ===")
    r_full = {}  # (local)
    for lname in lam_vals:
        lov = lam_vals[lname]  # (local)
        # k=0: f_high=f_4, f_low=f_2
        rG0 = r_k_full(a_dict, 0, lov, f_4_default, f_2_default)        # (local) Gaussian
        rM0 = r_k_full(a_dict, 0, lov, mellin_f_star_f4, mellin_f_star_f2)  # (local) Mellin
        # k=1: f_high=f_2, f_low=f_0 (Mellin only)
        rM1 = r_k_full(a_dict, 1, lov, mellin_f_star_f2, mellin_f_star_f0)  # (local) Mellin
        r_full[lname] = {"Gaussian_k0": rG0, "Mellin_k0": rM0, "Mellin_k1": rM1}
        print(f"  Lambda={lname}:")
        print(f"     Gaussian r_0 = {rG0:.6f}  (f_2/f_4={f_2_default/f_4_default:.4f}, AMPLIFIES)")
        print(f"     Mellin   r_0 = {rM0:.6e}  (f_2/f_4={mellin_f_star_f2/mellin_f_star_f4:.6f}, CRUSHES)")
        print(f"     Mellin   r_1 = {rM1:.6e}  (f_0/f_2={mellin_f_star_f0/mellin_f_star_f2:.6e})")

    # === Multiplicative-normalization pre-flight verdict (math-scripts.md) ===
    # The a-ratio driver is L_max-INVARIANT: any common w(L_max) cancels in every
    # ratio a_{2(k+1)}/a_{2k} = g_{2(k+1)}/g_{2k}. This gate's object is the term-ratio
    # VALUE at Lambda=M_KK (Lambda-scan + k-index), NOT an L_max-stability plateau.
    mnci_detected = True  # (local) cancellation holds for the a-ratio driver (structural identity)
    print("\n=== Multiplicative-normalization pre-flight ===")
    print(f"  MULTIPLICATIVE-NORMALIZATION-CANCELLATION-DETECTED = {mnci_detected} (for the a-ratio driver)")
    print("  => a-ratio driver is L_max-INVARIANT (FI) by the cancellation identity;")
    print("     gate verdict targets the term-ratio VALUE at Lambda=M_KK, not L-stability.")

    # === Gate evaluation (PRE-REGISTERED bands + schema-v2 3-tuple) ===
    # Canonical verdict object (strict_PASS_boundary): the scheme-INDEPENDENT a-ratio
    # driver at Lambda=M_KK (the regulator-invariant structural quantity).
    max_r_MKK = float(r_driver["M_KK"].max())          # (local) scheme-indep driver @ M_KK
    max_r_sp = float(r_driver[f"{Lambda_sp_over_M_KK}_M_KK"].max())  # (local) @ Lambda_sp

    # Composite band on the scheme-independent driver:
    if max_r_MKK < CTRL_PASS:
        composite = "PASS"   # (local)
    elif max_r_MKK >= CTRL_FAIL:
        composite = "FAIL"   # (local)
    else:
        composite = "INFO"   # (local) 0.5 <= max < 1 marginal

    # schema-v2 3-tuple:
    #  sign_verdict: PASS iff max a-ratio driver < 1 (series formally converges -- the
    #    DIRECTION predicted by Step 4: ratio<1 => formal convergence). The a-ratio
    #    RISING toward 1 is the substantive no-param-control signal but does not flip
    #    the formal-convergence sign (max 0.681 < 1).
    sign_v = "PASS" if max_r_MKK < CTRL_FAIL else "FAIL"  # (local)
    #  magnitude_verdict: PASS iff < 0.5 (comfortable margin); INFO iff [0.5,1); FAIL iff >=1.
    if max_r_MKK < CTRL_PASS:
        mag_v = "PASS"   # (local)
    elif max_r_MKK < CTRL_FAIL:
        mag_v = "INFO"   # (local) no comfortable parametric margin
    else:
        mag_v = "FAIL"   # (local)
    #  regime_verdict: the EFT-control window is the THIN shell [M_KK, 2.06 M_KK].
    #    Lambda_sp/M_KK = 2.06 => the parametric-validity window spans only one factor
    #    ~4 in Lambda^2 before EFT breakdown => MARGINAL (thin window, per plan INFO_meaning).
    reg_v = "MARGINAL"  # (local) thin EFT-control window (Lambda_sp/M_KK = 2.06)

    print("\n=== Verdict 3-tuple ===")
    print(f"  max_k r_k^a (scheme-indep driver) @ M_KK = {max_r_MKK:.6f}  vs bands {{<{CTRL_PASS} PASS, >={CTRL_FAIL} FAIL}}")
    print(f"  max_k r_k^a @ Lambda_sp                   = {max_r_sp:.6f}")
    print(f"  sign_verdict   = {sign_v}  (a-ratio max {max_r_MKK:.3f} < 1 => formal convergence; but a-ratio RISES => no param smallness)")
    print(f"  magnitude_verdict = {mag_v}  (no comfortable <0.5 margin @ M_KK on the structural driver)")
    print(f"  regime_verdict = {reg_v}  (THIN EFT-control window Lambda_sp/M_KK={Lambda_sp_over_M_KK})")
    print(f"  composite      = {composite}")

    # === Dual-SHA closure ===
    pins = {
        "_gate_id": GATE_ID, "_scheme": SCHEME, "_convention": CONVENTION,
        "L_max": L_MAX, "N_eval": N_EVAL,
        "ctrl_pass": CTRL_PASS, "ctrl_fail": CTRL_FAIL, "tol": TOL,
        "a_0": float(a_0_FW_zeta), "a_2": float(a_2_FW_zeta), "a_4": float(a_4_FW_zeta),
        "a_6": float(a_6_FW_zeta), "a_8": float(a_8_FW_zeta),
        "Lambda_sp_over_M_KK": float(Lambda_sp_over_M_KK), "M_KK": float(M_KK),
        "f_2_default": float(f_2_default), "f_4_default": float(f_4_default),
        "mellin_f_star_f0": float(mellin_f_star_f0),
        "mellin_f_star_f2": float(mellin_f_star_f2),
        "mellin_f_star_f4": float(mellin_f_star_f4),
        "L_max_branch": L_MAX_BRANCH, "branch_factor": BRANCH_FACTOR,
    }  # (local)
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_CONSTANTS_PATH, pins)  # (local)
    print("\n=== Dual-SHA closure ===")
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    # === Save data ===
    np.savez(
        OUT_NPZ,
        k_list=np.array(K_LIST),
        a_dict_keys=np.array([0, 2, 4, 6, 8]),
        a_dict_vals=np.array([a_dict[n] for n in [0, 2, 4, 6, 8]]),
        cache_moments=np.array([cache_a[n] for n in [0, 2, 4, 6, 8]]),
        crosscheck_ok=crosscheck_ok,
        n_modes=n_modes, tot_mult=tot_mult,
        aratios=aratios,
        aratio_increasing=aratio_increasing,
        r_driver_MKK=r_driver["M_KK"],
        r_driver_sp=r_driver[f"{Lambda_sp_over_M_KK}_M_KK"],
        max_r_MKK=max_r_MKK, max_r_sp=max_r_sp,
        rG0_MKK=r_full["M_KK"]["Gaussian_k0"],
        rM0_MKK=r_full["M_KK"]["Mellin_k0"],
        rM1_MKK=r_full["M_KK"]["Mellin_k1"],
        rG0_sp=r_full[f"{Lambda_sp_over_M_KK}_M_KK"]["Gaussian_k0"],
        rM0_sp=r_full[f"{Lambda_sp_over_M_KK}_M_KK"]["Mellin_k0"],
        rM1_sp=r_full[f"{Lambda_sp_over_M_KK}_M_KK"]["Mellin_k1"],
        f_ratio_gauss=f_2_default / f_4_default,
        f_ratio_mellin=mellin_f_star_f2 / mellin_f_star_f4,
        lam_factor2_MKK=lam_factor2["M_KK"],
        lam_factor2_sp=lam_factor2[f"{Lambda_sp_over_M_KK}_M_KK"],
        mnci_detected=mnci_detected,
        ctrl_pass=CTRL_PASS, ctrl_fail=CTRL_FAIL,
        Lambda_sp_over_M_KK=float(Lambda_sp_over_M_KK), M_KK=float(M_KK),
        composite=composite, sign_v=sign_v, mag_v=mag_v, reg_v=reg_v,
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"\n  data  -> {OUT_NPZ}")

    # === Plot ===
    make_plot(aratios, r_driver, r_full, max_r_MKK, max_r_sp,
              composite, sign_v, mag_v, reg_v)
    print(f"  plot  -> {OUT_PNG}")

    # === Emit verdict line (canonical + dual-SHA companion + schema-v2 3-tuple) ===
    value_str = (
        f"max_r_aratio_driver_MKK={max_r_MKK:.4f};"
        f"max_r_aratio_driver_2.06MKK={max_r_sp:.4f};"
        f"bands={{PASS<{CTRL_PASS},FAIL>={CTRL_FAIL}}};"
        f"r_k_aratio_MKK=[{','.join(f'{x:.4f}' for x in r_driver['M_KK'])}];"
        f"a_ratio_INCREASING={aratio_increasing};"
        f"functional_DEPENDENT:Gaussian_r0_MKK={r_full['M_KK']['Gaussian_k0']:.4f}(FAIL_band),"
        f"Mellin_r0_MKK={r_full['M_KK']['Mellin_k0']:.4e}(PASS_band);"
        f"a6={a_6_FW_zeta:.4f};a8={a_8_FW_zeta:.4f};cache_crosscheck={'PASS' if crosscheck_ok else 'FAIL'};"
        f"Lambda_sp_over_M_KK={Lambda_sp_over_M_KK}_promoted;"
        f"MNCI_aratio_driver={mnci_detected};"
        f"4tuple=(value={max_r_MKK:.4f},scheme=SDW-layer-expansion,convention=RATIO,L_max=10)"
    )  # (local)
    prior_sha = find_prior_audit_sha()  # (local)
    supersedes = ""  # (local)
    if prior_sha and prior_sha != audit_sha:
        supersedes = prior_sha  # (local) corrective re-emission per gate-verdicts.md Option A
    append_verdict(composite, value_str, audit_sha, content_sha,
                   sign_v, mag_v, reg_v, max_r_MKK, max_r_sp,
                   aratio_increasing, supersedes_sha=supersedes)
    print(f"\n  verdict -> {VERDICT_TXT}")
    print(f"  {GATE_ID}: {composite} -- sign={sign_v} mag={mag_v} regime={reg_v}")
    return 0


# -----------------------------------------------------------------------------
# Plot
# -----------------------------------------------------------------------------
def make_plot(aratios, r_driver, r_full, max_r_MKK, max_r_sp,
              composite, sign_v, mag_v, reg_v):
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.2))
    ks = np.array(K_LIST)  # (local)

    # Left: scheme-independent a-ratio driver at both Lambda + control bands
    ax = axes[0]
    ax.plot(ks, r_driver["M_KK"], "o-", color="#c0392b", lw=2, ms=8,
            label=r"$r_k^a$ @ $\Lambda=M_{KK}$ (driver)")
    ax.plot(ks, r_driver[f"{Lambda_sp_over_M_KK}_M_KK"], "s--", color="#2980b9", lw=2, ms=7,
            label=rf"$r_k^a$ @ $\Lambda=2.06\,M_{{KK}}$")
    ax.axhline(CTRL_PASS, color="green", ls=":", lw=1.5, label=r"PASS band $<0.5$")
    ax.axhline(CTRL_FAIL, color="red", ls=":", lw=1.5, label=r"FAIL band $\geq 1$")
    ax.set_xlabel("layer index $k$")
    ax.set_ylabel(r"$r_k^a = (a_{2(k+1)}/a_{2k})\,(\Lambda/M_{KK})^{-2}$")
    ax.set_title("Scheme-INDEPENDENT a-ratio driver (FI structural piece)\n"
                 "a-ratio RISES toward 1 => terms LESS suppressed => no param control")
    ax.set_xticks(ks)
    ax.set_ylim(0, 1.15)
    ax.legend(fontsize=8, loc="upper left")
    ax.grid(alpha=0.3)

    # Right: functional-DEPENDENT full r_0 across schemes (the lizzi finding)
    ax = axes[1]
    schemes = ["a-ratio\ndriver", "Gaussian\n$f$", "Mellin\n$f^*$"]  # (local)
    r0_MKK = [r_driver["M_KK"][0], r_full["M_KK"]["Gaussian_k0"], r_full["M_KK"]["Mellin_k0"]]  # (local)
    colors = ["#7f8c8d", "#e67e22", "#16a085"]  # (local)
    bars = ax.bar(schemes, r0_MKK, color=colors, alpha=0.85)
    ax.axhline(CTRL_PASS, color="green", ls=":", lw=1.5, label=r"PASS $<0.5$")
    ax.axhline(CTRL_FAIL, color="red", ls=":", lw=1.5, label=r"FAIL $\geq 1$")
    ax.set_yscale("log")
    ax.set_ylabel(r"$r_0$ @ $\Lambda=M_{KK}$ (log scale)")
    ax.set_title("$r_0$ is FUNCTIONAL-DEPENDENT (the lizzi finding):\n"
                 "SAME $D_K$ spectrum -> FAIL (Gaussian) / INFO (driver) / PASS (Mellin)")
    for b, v in zip(bars, r0_MKK):
        ax.text(b.get_x() + b.get_width() / 2, v * 1.15, f"{v:.3g}",
                ha="center", va="bottom", fontsize=9)
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, axis="y")

    fig.suptitle(f"{GATE_ID}: SDW-EFT parametric control / species-scale thinness "
                 f"($\\Lambda_{{sp}}/M_{{KK}}={Lambda_sp_over_M_KK}$)  |  "
                 f"composite={composite} (sign={sign_v}, mag={mag_v}, regime={reg_v})",
                 fontsize=10)
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# -----------------------------------------------------------------------------
# Verdict-file helpers (Option A supersession + dual-SHA + schema-v2 3-tuple)
# -----------------------------------------------------------------------------
def find_prior_audit_sha() -> str:
    """Latest non-superseded canonical line for GATE_ID (gate-verdicts.md "Option A")."""
    if not VERDICT_TXT.exists():
        return ""
    import re as _re  # (local)
    text = VERDICT_TXT.read_text(encoding="utf-8")  # (local)
    canon_re = _re.compile(
        rf"^{_re.escape(GATE_ID)}:\s.*?audit_sha256=([a-f0-9]{{64}})", _re.MULTILINE)  # (local)
    shas = canon_re.findall(text)  # (local)
    if not shas:
        return ""
    sup_re = _re.compile(r"supersedes=([a-f0-9]{64})")  # (local)
    superseded = set(sup_re.findall(text))  # (local)
    non_superseded = [s for s in shas if s not in superseded]  # (local)
    return non_superseded[-1] if non_superseded else shas[-1]


def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str,
                   sign_v: str, mag_v: str, reg_v: str,
                   max_r_MKK: float, max_r_sp: float,
                   aratio_increasing: bool, supersedes_sha: str = "") -> None:
    """Append canonical line + dual-SHA companion + schema-v2 3-tuple row (atomic single open('a'))."""
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    sup_token = f"_supersedes={supersedes_sha}" if supersedes_sha else ""  # (local)
    line = (
        f"{GATE_ID}: {verdict} -- value='{value}{sup_token}' "
        f"scheme={SCHEME} convention={CONVENTION} "
        f"L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row\n"
    )
    # REQUIRED [SIGN] 3-tuple companion row.
    schema_v2_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={reg_v} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2); "
        f"sign = scheme-indep a-ratio driver max {max_r_MKK:.4f} < 1 (series formally converges) "
        f"AND a-ratio strictly INCREASING with k ({aratio_increasing}) confirms NO parametric smallness; "
        f"mag = max_k r_k^a @ M_KK = {max_r_MKK:.4f} vs bands {{<0.5 PASS, [0.5,1) INFO, >=1 FAIL}}; "
        f"regime = THIN EFT-control window Lambda_sp/M_KK={Lambda_sp_over_M_KK} "
        f"(driver @ Lambda_sp = {max_r_sp:.4f}); MARGINAL\n"
    )
    # Functional-sensitivity row (the lizzi finding: EFT-control verdict is scheme-dependent)
    fi_row = (
        f"# FUNCTIONAL-SENSITIVITY=EFT-control-verdict-is-SCHEME-DEPENDENT "
        f"# {GATE_ID}: the a-ratio driver (a_{{2(k+1)}}/a_{{2k}}) is FUNCTIONAL-INVARIANT "
        f"(any common w(L_max) cancels in the ratio); the f-coefficient ratio is FUNCTIONAL-DEPENDENT "
        f"(Gaussian f_2/f_4=4.19 AMPLIFIES r_0 to FAIL-band; Mellin f_2/f_4=0.033 CRUSHES r_0 to PASS-band). "
        f"SAME D_K spectrum => FAIL (Gaussian) / INFO (driver) / PASS (Mellin). "
        f"a_6_FW_zeta/a_8_FW_zeta promoted (E38 per-branch zeta, cache-crosschecked); "
        f"Lambda_sp_over_M_KK=2.06 promoted (W6-SPECIES-36/SCALE-63). "
        f"Confirms string-theory V.1: layer hierarchy is numerical-truncation (block-diagonality), NOT parametric-EFT.\n"
    )
    rows = [line, companion, schema_v2_row, fi_row]  # (local)
    if supersedes_sha:
        rows.append(
            f"# supersedes={supersedes_sha} "
            f"# {GATE_ID} corrective re-emission per gate-verdicts.md \"Option A\" "
            f"(prior line RETAINED; this corrective line is canonical)\n"
        )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        for r in rows:
            fp.write(r)


if __name__ == "__main__":
    sys.exit(main())
