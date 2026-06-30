"""s88_w9_106_hbw_3c_convention_audit.py — S88-HBW-3C-CONVENTION-AUDIT

HBW-3C convention audit on the §W8-4 SUB-ATLAS-A_2 cascade (which is the S87
W8-4 5-sub-channel HBW positivity audit on atlas A_4 = {zeta, Zubarev, SDW,
anomaly} per the workshop document at
sessions/archive/session-87/workshops/s87-atlas-cardinality-cascade-vs-ensemble.md).

Plan reference: sessions/session-plan/session-88-plan-w9.md §W9-106.

Question (per plan §W9-106 Method 1-5):
  Re-run the W8-4 5-sub-channel cascade with sub-channel 3c evaluator under
  TWO conventions, then compare the cascade verdict:

    Convention A (W8-4 baseline; rule §"3c Bernstein-density"):
        signed_A[k](lam) := (-1)^k * (d^k w_R / d lam^k)(lam)
        test predicate: signed_A[k](lam) >= 0 for k in {0,1,2,3} on
                        [lam_min, lam_max].

    Convention B (plan §W9-106 alternating-sign x-derivative):
        signed_B[k](x) := (-1)^k * (d^k w_R / d x^k)(x), where x = (lam/Lambda_cut)^2
        test predicate: signed_B[k](x) >= 0 for k in {0,1,2,3} on
                        [x_min, x_max] = [lam_min^2, lam_max^2].

PASS / FAIL / INFO threshold (per plan §W9-106 Pre-registered):
  PASS: verdict_A == verdict_B (CONVENTION-INVARIANT; cascade structurally
        invariant; HBW-3C PRU vulnerability NOT detected).
  FAIL: verdict_A != verdict_B (CONVENTION-DEPENDENT; HBW-3C PRU vulnerability
        surfaced; advisory text-spec emitted in WP §W9-106 Results).
  INFO: verdict_A or verdict_B is INFO under its respective convention.

Substitution chain (per .claude/rules/math-scripts.md §"Double-Check Logic"):

  Step 1 — Definitions:
      Lambda_cut = M_KK = 1 (canonical M_KK-units normalization, Vol_SU3_Haar
                            base; cf. canonical_constants.py).
      lam_min, lam_max from cache abs-eigenvalue range at L_max=12, tau=0.190
                            (substrate-IS Jensen-deformed SU(3) D_K spectrum).
      x = (lam/Lambda_cut)^2; x-domain = [lam_min^2, lam_max^2].
      Regulator weight functions (in x):
        f_zeta(x)    = 1
        f_Zubarev(x) = x/(1+x^2)
        f_SDW(x)     = exp(-x)
        f_anomaly(x) = exp(-x)/sqrt(x)

  Step 2 — Substitution (define both conventions):
      Convention A: g(lam) := f(lam^2); signed_A[k](lam) = (-1)^k * d^k g/d lam^k.
      Convention B: signed_B[k](x) = (-1)^k * d^k f/d x^k.
      The two conventions are NOT algebraically equivalent: the chain rule
      x = lam^2 introduces polynomial pre-factors (2 lam, 4 lam^2 + 2, ...)
      between (d/d lam) and (d/d x), so even on the SAME spectral support
      they test different positive-cone predicates.

  Step 3 — Simplification (per regulator):
      zeta:    f' = f'' = f''' = 0 in both x and lam (constant). Trivially PASSes
               under both conventions (vacuously).
      Zubarev: in x, f'' < 0 on x in (sqrt(3)/3, sqrt(3)) and f''' is non-monotone.
               In lam (= sqrt(x)), the Bernstein test under chain rule has a
               broader negative region per W8-4 NPZ. PRE-VERIFICATION via Sage:
               signed_A min = -6.587 (FAIL); signed_B min = -2.059 (FAIL).
               BOTH FAIL on 3c — verdict matches.
      SDW:     in x, f^{(k)}(x) = (-1)^k exp(-x); signed_B[k] = exp(-x) > 0
               (completely monotonic in x; vacuously PASSes Bernstein).
               In lam, chain rule introduces 2lam factor on odd-k derivatives
               which break the alternating-sign cancellation; signed_A k=3 has
               minimum -2.773 (FAIL per W8-4 NPZ).
               SDW FAIL under A, PASS under B — VERDICT FLIPS.
      anomaly: f(x) = exp(-x)/sqrt(x). In x, the (-1)^k cancellations partially
               survive; signed_B PASSes on the cache support per Sage analysis.
               In lam, the chain-rule pre-factors and sqrt-singularity at lam->0
               combine to keep signed_A positive on a finite support starting
               above lam_min; PASS in W8-4 NPZ.
               anomaly PASSes under both A and B.

  Step 4 — Direction (the prediction):
      Sub-grid changes (3c only):
        Zubarev: A=FAIL, B=FAIL  -> sub-cell verdict matches
        SDW:     A=FAIL, B=PASS  -> SUB-CELL VERDICT FLIPS
      Cascade composite collapse rule (gate-verdicts.md §"Composite-collapse"):
        n_sub_FAIL_A = 6 (4*3a + 2*3c[Zubarev,SDW])  -> composite FAIL
        n_sub_FAIL_B = 5 (4*3a + 1*3c[Zubarev only]) -> composite FAIL
      verdict_A == verdict_B == FAIL (composite collapse CONVENTION-INVARIANT).
      However, the sub-grid is CONVENTION-DEPENDENT (SDW row 3c flips).

  Step 5 — Conclusion (substrate-physics direction):
      The composite cascade verdict is convention-INVARIANT (both FAIL); the
      Bernstein sub-test 3c is convention-DEPENDENT at the sub-cell layer.
      Per plan §W9-106 PASS criterion ("verdict_A == verdict_B"), the gate
      VERDICT IS PASS at the composite layer. However, the sub-cell flip for
      SDW under convention B has structural significance: any downstream
      consumer that cited SDW_3c_min ~ -2.773 as a bare-decomposition deviation
      magnitude (e.g., the workshop §"Concession on lab discriminator" lab-
      feasibility chain) is convention-A-specific; under convention B, SDW
      is substrate-IS HBW-positive in x, eliminating that specific lab-
      feasibility margin. This carries a Class-(d) PIN-DERIVATIVE-VS-SOURCE-
      PRIMARY observation (not a Class-(c) PIN-DRIFT) for downstream cite
      hygiene.

Substrate framing (per .claude/rules/phononic-framing.md):
  The x-derivative operator and the lam-derivative operator are BOTH
  substrate-IS choices on the spectral support of D_K (the substrate's own
  Jensen-deformed eigenvalue measure). Convention A treats "the spectral
  variable" as lam (the abs-eigenvalue itself); convention B treats it as
  x = (lam/M_KK)^2 (the dimensionless squared-eigenvalue, natural for the
  spectral-action f(D^2/Lambda^2) trace). NEITHER is laboratory-imposed;
  the convention pair (A, B) is a substrate-level symmetry test on the
  Bernstein positive-cone predicate. Direction of explanation: substrate IS
  the cascade; substrate IS the differential operator; the convention pair
  is a substrate-level symmetry test of the HBW positivity discipline.

Author: connes-ncg-theorist (S88 W9-106 dispatch, 2026-05-06).
"""

from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")  # (local) non-interactive backend
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# Resolve THIS_DIR / project paths
THIS_DIR = Path(__file__).parent.resolve()  # (local)
PROJECT_ROOT = THIS_DIR.parent.parent  # (local)
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"  # (local)
SESSION_84_DIR = PROJECT_ROOT / "computations" / "session-84"  # (local)

if str(SHARED_DIR) not in sys.path:
    sys.path.insert(0, str(SHARED_DIR))
if str(THIS_DIR) not in sys.path:
    sys.path.insert(0, str(THIS_DIR))

from canonical_constants import (  # noqa: E402
    Vol_SU3_Haar,
    tau_fold,
    M_KK,
)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

GATE_ID = "S88-HBW-3C-CONVENTION-AUDIT"  # (local)
SCHEME_TAG = "HBW_5_subchannel_audit_TWO_CONVENTION"  # (local)
CONVENTION_TAG = "A_4_4col_f6_0.1_residue_dual_convention_A_lam_B_x"  # (local)
L_MAX = 12  # (local) canonical
L_MAX_XCHECK = 10  # (local)
SCHEMA_VERSION = "S88+"  # (local)

ATLAS_A_4 = ("zeta", "Zubarev", "SDW", "anomaly")  # (local) per W8-4 baseline
SUBCHANNELS = ("3a", "3b", "3c", "3d", "3e")  # (local)

LAMBDA_CUT = 1.0  # (local) M_KK-units canonical

# Pre-registered framework-truncated residue slots (W8-4 baseline)
F_2_RESIDUE = 0.0  # (local)
F_4_RESIDUE = 0.05  # (local)
F_6_RESIDUE = 0.1  # (local)

# Pre-registered sub-channel thresholds (W8-4 baseline; convention-INDEPENDENT
# for 3a/3b/3d/3e; ONLY 3c uses the (-1)^k Bernstein-density test affected by
# convention)
THRESH_3A_TRUNC = 1.0e-10  # (local)
THRESH_3B_POS = -1.0e-12  # (local)
THRESH_3C_DERIV = -1.0e-12  # (local)
THRESH_3D_KAPPA = 1.0e15  # (local)
THRESH_3E_EIG = -1.0e-12  # (local)

MOMENT_INDICES_BASE = (0, 2, 4, 6)  # (local)
MOMENT_INDICES_HAUSDORFF = (0, 2, 4, 6, 8)  # (local)
BERNSTEIN_K_RANGE = (0, 1, 2, 3)  # (local)

# Plan §W9-106 PASS-criterion convention pin
CONVENTION_A_LABEL = "d^k w_R / d lam^k"  # (local) W8-4 baseline (lam-derivative)
CONVENTION_B_LABEL = "(-1)^k * d^k w_R / d x^k"  # (local) plan §W9-106 (x-derivative)


# ---------------------------------------------------------------------------
# SHA helpers (canonical W9a-99 dual-SHA pattern)
# ---------------------------------------------------------------------------

def file_sha(path: Path) -> str:
    """Return SHA-256 hexdigest of file contents."""
    h = hashlib.sha256()  # (local)
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def text_sha(text: str) -> str:
    """Return SHA-256 hexdigest of a text string."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def closure_hash(pin_map: dict) -> str:
    """SHA-256 of the JSON-canonicalized ordered input-pin map."""
    canonical = json.dumps(pin_map, sort_keys=True, separators=(",", ":"))  # (local)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Regulator weight functions (per S86 W11 §7 + S83 W1 G2; identical to W8-4)
# ---------------------------------------------------------------------------

def w_R(regulator: str, lam: np.ndarray, Lambda_cut: float = LAMBDA_CUT) -> np.ndarray:
    """Regulator weight w_R(lam); positive on lam > 0."""
    lam_arr = np.asarray(lam, dtype=np.float64)  # (local)
    x = (lam_arr / Lambda_cut) ** 2  # (local)
    if regulator == "zeta":
        return np.ones_like(lam_arr)
    elif regulator == "Zubarev":
        return x / (1.0 + x * x)
    elif regulator == "SDW":
        return np.exp(-x)
    elif regulator == "anomaly":
        return np.exp(-x) / np.sqrt(np.maximum(x, 1e-300))
    else:
        raise ValueError(f"Unknown regulator: {regulator}")


# ---------------------------------------------------------------------------
# Convention-A derivatives (W8-4 baseline; d^k w/d lam^k via chain rule)
# ---------------------------------------------------------------------------

def w_R_lam_derivative(
    regulator: str, lam: np.ndarray, k: int, Lambda_cut: float = LAMBDA_CUT
) -> np.ndarray:
    """(d^k / d lam^k) w_R(lam) analytically (k = 0,1,2,3).

    Chain-rule lifts of the x-derivatives via x = (lam/Lambda)^2.
    Identical to the W8-4 baseline implementation; reproduces NPZ-verified
    Bernstein curves exactly.
    """
    lam_arr = np.asarray(lam, dtype=np.float64)  # (local)
    u = lam_arr / Lambda_cut  # (local)
    x = u * u  # (local)

    if regulator == "zeta":
        if k == 0:
            return np.ones_like(lam_arr)
        else:
            return np.zeros_like(lam_arr)
    elif regulator == "Zubarev":
        denom2 = (1.0 + x * x) ** 2  # (local)
        denom3 = (1.0 + x * x) ** 3  # (local)
        denom4 = (1.0 + x * x) ** 4  # (local)
        f0 = x / (1.0 + x * x)
        f1 = (1.0 - x * x) / denom2
        f2 = -2.0 * x * (3.0 - x * x) / denom3
        f3 = -6.0 * (1.0 - 6.0 * x * x + x ** 4) / denom4
    elif regulator == "SDW":
        e = np.exp(-x)  # (local)
        f0 = e
        f1 = -e
        f2 = e
        f3 = -e
    elif regulator == "anomaly":
        e = np.exp(-x)  # (local)
        sqrt_x = np.sqrt(np.maximum(x, 1e-300))  # (local)
        x_neg_half = 1.0 / sqrt_x
        f0 = e * x_neg_half
        f1 = -e * x_neg_half * (1.0 + 0.5 / x)
        f2 = f0 * ((1.0 + 1.0 / (2.0 * x)) ** 2 + 1.0 / (2.0 * x * x))
        f3 = -f2 * (1.0 + 1.0 / (2.0 * x)) + f1 / (2.0 * x * x) - f0 / (x ** 3)
    else:
        raise ValueError(f"Unknown regulator: {regulator}")

    if k == 0:
        return f0
    elif k == 1:
        return (2.0 * u / Lambda_cut) * f1
    elif k == 2:
        return (2.0 / Lambda_cut ** 2) * (f1 + 2.0 * x * f2)
    elif k == 3:
        return (4.0 * u / Lambda_cut ** 3) * (3.0 * f2 + 2.0 * x * f3)
    else:
        raise ValueError(f"Bernstein order k={k} not implemented; k in {{0,1,2,3}}")


# ---------------------------------------------------------------------------
# Convention-B derivatives (plan §W9-106 alternating-sign x-derivative)
# ---------------------------------------------------------------------------

def w_R_x_derivative(
    regulator: str, x: np.ndarray, k: int
) -> np.ndarray:
    """(d^k / dx^k) f_R(x) analytically (k = 0,1,2,3).

    Convention B operates on x = (lam/Lambda_cut)^2 directly. The signed
    Bernstein test then wraps this with (-1)^k externally.
    """
    x_arr = np.asarray(x, dtype=np.float64)  # (local)
    if regulator == "zeta":
        if k == 0:
            return np.ones_like(x_arr)
        else:
            return np.zeros_like(x_arr)
    elif regulator == "Zubarev":
        # f(x) = x/(1+x^2)
        # f'(x) = (1-x^2)/(1+x^2)^2
        # f''(x) = -2x(3-x^2)/(1+x^2)^3
        # f'''(x) = -6(1-6x^2+x^4)/(1+x^2)^4
        denom1 = (1.0 + x_arr * x_arr)
        denom2 = denom1 ** 2
        denom3 = denom1 ** 3
        denom4 = denom1 ** 4
        if k == 0:
            return x_arr / denom1
        elif k == 1:
            return (1.0 - x_arr * x_arr) / denom2
        elif k == 2:
            return -2.0 * x_arr * (3.0 - x_arr * x_arr) / denom3
        elif k == 3:
            return -6.0 * (1.0 - 6.0 * x_arr * x_arr + x_arr ** 4) / denom4
        else:
            raise ValueError("k > 3 not implemented")
    elif regulator == "SDW":
        # f(x) = exp(-x); f^{(k)}(x) = (-1)^k * exp(-x)
        e = np.exp(-x_arr)  # (local)
        if k == 0:
            return e
        elif k == 1:
            return -e
        elif k == 2:
            return e
        elif k == 3:
            return -e
        else:
            raise ValueError("k > 3 not implemented")
    elif regulator == "anomaly":
        # f(x) = exp(-x) * x^{-1/2}
        # ln f = -x - (1/2) ln x; f'/f = -1 - 1/(2x); recursion:
        # f^{(k+1)} = f^{(k)} * (-1 - 1/(2x)) + (correction from differentiating 1/(2x))
        # Direct closed forms from logarithmic recursion (verified):
        e = np.exp(-x_arr)  # (local)
        sqrt_x = np.sqrt(np.maximum(x_arr, 1e-300))
        x_neg_half = 1.0 / sqrt_x  # (local) x^{-1/2}
        f0 = e * x_neg_half
        if k == 0:
            return f0
        # Use recursion on phi(x) := ln f = -x - (1/2) ln x; phi'(x) = -1 - 1/(2x)
        # f' = f * phi'(x)
        phi_p = -1.0 - 1.0 / (2.0 * x_arr)
        f1 = f0 * phi_p
        if k == 1:
            return f1
        # f'' = f' * phi' + f * phi''; phi''(x) = 1/(2 x^2)
        phi_pp = 1.0 / (2.0 * x_arr * x_arr)
        f2 = f1 * phi_p + f0 * phi_pp
        if k == 2:
            return f2
        # f''' = f'' * phi' + 2 * f' * phi'' + f * phi'''; phi'''(x) = -1/x^3
        phi_ppp = -1.0 / (x_arr ** 3)
        f3 = f2 * phi_p + 2.0 * f1 * phi_pp + f0 * phi_ppp
        if k == 3:
            return f3
        else:
            raise ValueError("k > 3 not implemented")
    else:
        raise ValueError(f"Unknown regulator: {regulator}")


# ---------------------------------------------------------------------------
# Spectral moment computation
# ---------------------------------------------------------------------------

def compute_a_n(
    abs_eigs: np.ndarray, mults: np.ndarray, regulator: str, n: int
) -> float:
    """a_n^{(R)} = (1/Vol_SU3_Haar) * sum_lam mult(lam) * lam^n * w_R(lam)."""
    weights = w_R(regulator, abs_eigs)  # (local)
    contributions = mults * (abs_eigs ** n) * weights  # (local)
    return float(np.sum(contributions) / Vol_SU3_Haar)


# ---------------------------------------------------------------------------
# Sub-channel evaluators
# Convention-INDEPENDENT (3a, 3b, 3d, 3e — they do not invoke the (-1)^k
#   Bernstein test); identical to W8-4 baseline.
# Convention-DEPENDENT (3c — uses (-1)^k * d^k w/d{var}^k Bernstein test)
# ---------------------------------------------------------------------------

def evaluate_3a(
    abs_eigs_L12: np.ndarray, mults_L12: np.ndarray,
    abs_eigs_L10: np.ndarray, mults_L10: np.ndarray,
    regulator: str
) -> tuple[float, str]:
    """3a: MP-abs-conv truncation cross-check (convention-independent)."""
    n_indices = (2, 4, 6)  # (local)
    M_L12 = sum(
        compute_a_n(abs_eigs_L12, mults_L12, regulator, n) * (n ** (-6))
        for n in n_indices
    )  # (local)
    M_L10 = sum(
        compute_a_n(abs_eigs_L10, mults_L10, regulator, n) * (n ** (-6))
        for n in n_indices
    )  # (local)
    delta_3a = abs(M_L12 - M_L10)  # (local)
    if delta_3a < THRESH_3A_TRUNC:
        verdict = "PASS"
    elif delta_3a < THRESH_3A_TRUNC * 100:
        verdict = "INFO"
    else:
        verdict = "FAIL"
    return delta_3a, verdict


def evaluate_3b(
    abs_eigs: np.ndarray, mults: np.ndarray, regulator: str
) -> tuple[float, str]:
    """3b: positive-cone moment sequence (convention-independent)."""
    n_arr = np.array(MOMENT_INDICES_BASE, dtype=np.float64)  # (local)
    a_n_vals = np.array(
        [compute_a_n(abs_eigs, mults, regulator, int(n)) for n in n_arr],
        dtype=np.float64,
    )  # (local)
    n_safe = np.maximum(n_arr, 1e-15)  # (local)
    w_n_vals = w_R(regulator, n_safe)  # (local)
    products = a_n_vals * w_n_vals  # (local)
    if regulator == "anomaly":
        finite_products = products[1:]  # (local)
    else:
        finite_products = products
    min_product = float(np.min(finite_products))  # (local)
    if min_product >= 0.0:
        verdict = "PASS"
    elif min_product >= THRESH_3B_POS:
        verdict = "INFO"
    else:
        verdict = "FAIL"
    return min_product, verdict


def evaluate_3c_convention_A(
    lam_min: float, lam_max: float, regulator: str, n_grid: int = 200
) -> tuple[float, str, dict]:
    """3c sub-channel under convention A (W8-4 baseline; lam-derivative).

    Tests min over (k, lam) of (-1)^k * d^k w_R / d lam^k on [lam_min, lam_max].
    """
    lam_grid = np.linspace(lam_min, lam_max, n_grid)  # (local)
    per_k_min = {}  # (local)
    overall_min = np.inf  # (local)
    for k in BERNSTEIN_K_RANGE:
        deriv = w_R_lam_derivative(regulator, lam_grid, k)  # (local)
        signed_deriv = ((-1.0) ** k) * deriv  # (local)
        k_min = float(np.min(signed_deriv))  # (local)
        per_k_min[f"k={k}"] = k_min
        if k_min < overall_min:
            overall_min = k_min
    if overall_min >= 0.0:
        verdict = "PASS"
    elif overall_min >= THRESH_3C_DERIV:
        verdict = "INFO"
    else:
        verdict = "FAIL"
    return float(overall_min), verdict, per_k_min


def evaluate_3c_convention_B(
    lam_min: float, lam_max: float, regulator: str, n_grid: int = 200,
    Lambda_cut: float = LAMBDA_CUT
) -> tuple[float, str, dict]:
    """3c sub-channel under convention B (plan §W9-106; x-derivative).

    Tests min over (k, x) of (-1)^k * d^k w_R / d x^k on [x_min, x_max] where
    x_min = (lam_min/Lambda_cut)^2 and x_max = (lam_max/Lambda_cut)^2. Same
    physical support as convention A; different differential operator.
    """
    x_min = (lam_min / Lambda_cut) ** 2  # (local)
    x_max = (lam_max / Lambda_cut) ** 2  # (local)
    x_grid = np.linspace(x_min, x_max, n_grid)  # (local)
    per_k_min = {}  # (local)
    overall_min = np.inf  # (local)
    for k in BERNSTEIN_K_RANGE:
        deriv_x = w_R_x_derivative(regulator, x_grid, k)  # (local)
        signed_deriv = ((-1.0) ** k) * deriv_x  # (local)
        k_min = float(np.min(signed_deriv))  # (local)
        per_k_min[f"k={k}"] = k_min
        if k_min < overall_min:
            overall_min = k_min
    if overall_min >= 0.0:
        verdict = "PASS"
    elif overall_min >= THRESH_3C_DERIV:
        verdict = "INFO"
    else:
        verdict = "FAIL"
    return float(overall_min), verdict, per_k_min


def evaluate_3d(
    abs_eigs: np.ndarray, mults: np.ndarray, regulator: str
) -> tuple[float, str]:
    """3d: Widder-inversion well-posedness (convention-independent)."""
    needed_indices = sorted(set(2 * (i + j) for i in range(4) for j in range(4)))  # (local)
    a_dict = {n: compute_a_n(abs_eigs, mults, regulator, n) for n in needed_indices}  # (local)
    W = np.zeros((4, 4), dtype=np.float64)  # (local)
    for i in range(4):
        for j in range(4):
            W[i, j] = a_dict[2 * (i + j)]
    sigmas = np.linalg.svd(W, compute_uv=False)  # (local)
    sig_max = float(sigmas.max())  # (local)
    sig_min = float(sigmas.min())  # (local)
    if sig_min > 0.0:
        kappa = sig_max / sig_min  # (local)
    else:
        kappa = np.inf  # (local)
    if np.isfinite(kappa) and kappa < THRESH_3D_KAPPA:
        verdict = "PASS"
    elif np.isfinite(kappa) and kappa < 10.0 * THRESH_3D_KAPPA:
        verdict = "INFO"
    else:
        verdict = "FAIL"
    return kappa, verdict


def evaluate_3e(
    abs_eigs: np.ndarray, mults: np.ndarray, regulator: str
) -> tuple[float, str]:
    """3e: Hausdorff-Hankel positive-definiteness (convention-independent)."""
    needed_indices = sorted(set(2 * (i + j) for i in range(5) for j in range(5)))  # (local)
    a_dict = {n: compute_a_n(abs_eigs, mults, regulator, n) for n in needed_indices}  # (local)
    H = np.zeros((5, 5), dtype=np.float64)  # (local)
    for i in range(5):
        for j in range(5):
            H[i, j] = a_dict[2 * (i + j)]
    H = 0.5 * (H + H.T)  # (local)
    eigs = np.linalg.eigvalsh(H)  # (local)
    min_eig = float(np.min(eigs))  # (local)
    if min_eig >= 0.0:
        verdict = "PASS"
    elif min_eig >= THRESH_3E_EIG:
        verdict = "INFO"
    else:
        verdict = "FAIL"
    return min_eig, verdict


# ---------------------------------------------------------------------------
# Cache loader
# ---------------------------------------------------------------------------

def load_cache(cache_path: Path) -> tuple[np.ndarray, np.ndarray, dict]:
    """Load L_max=12 spectrum cache (sector_evals dict per (p,q))."""
    d = np.load(cache_path, allow_pickle=True)
    se = d["sector_evals"].item()
    abs_list = []  # (local)
    mult_list = []  # (local)
    level_list = []  # (local)
    pq_list = []  # (local)
    for (p, q), v in se.items():
        dim_pq = int(v["dim"])
        level_pq = int(v["level"])
        evs = np.asarray(v["abs_evals"]).ravel()
        for ev in evs:
            abs_list.append(float(ev))
            mult_list.append(dim_pq)
            level_list.append(level_pq)
            pq_list.append((p, q))
    abs_eigs = np.array(abs_list, dtype=np.float64)
    mults = np.array(mult_list, dtype=np.float64)
    levels = np.array(level_list, dtype=np.int32)
    return abs_eigs, mults, {"levels": levels, "pq": pq_list}


def synthesize_lmax_filter(
    abs_eigs: np.ndarray, mults: np.ndarray, levels: np.ndarray, L_max_cut: int
) -> tuple[np.ndarray, np.ndarray]:
    """Filter L=12 cache to level <= L_max_cut for cross-check."""
    mask = levels <= L_max_cut  # (local)
    return abs_eigs[mask], mults[mask]


# ---------------------------------------------------------------------------
# Cascade composite-collapse (per gate-verdicts.md schema-v2)
# ---------------------------------------------------------------------------

def composite_collapse(n_sub_PASS: int, n_sub_INFO: int, n_sub_FAIL: int,
                       sign_v: str, magnitude_v: str, regime_v: str) -> str:
    """Apply gate-verdicts.md §"Composite-collapse rule"."""
    if regime_v == "BREAKDOWN":
        return "FAIL"
    elif sign_v == "FAIL":
        return "FAIL"
    elif magnitude_v == "FAIL" and regime_v == "VALID":
        return "FAIL"
    elif magnitude_v == "FAIL" and regime_v == "MARGINAL":
        return "INFO"
    elif magnitude_v == "INFO":
        return "INFO"
    else:
        return "PASS"


def run_cascade_under_convention(
    convention_label: str, evaluate_3c_fn,
    abs_L12: np.ndarray, mults_L12: np.ndarray,
    abs_L10: np.ndarray, mults_L10: np.ndarray,
    lam_min: float, lam_max: float,
) -> dict:
    """Run the full 5-sub-channel cascade under one convention; return verdict bundle."""
    pass_grid = np.zeros((len(ATLAS_A_4), len(SUBCHANNELS)), dtype=object)  # (local)
    value_grid = np.zeros((len(ATLAS_A_4), len(SUBCHANNELS)), dtype=np.float64)  # (local)
    bernstein_per_k = {}  # (local)

    val_3a, val_3b, val_3c, val_3d, val_3e = {}, {}, {}, {}, {}  # (local)
    for r_idx, regulator in enumerate(ATLAS_A_4):
        d3a, v3a = evaluate_3a(abs_L12, mults_L12, abs_L10, mults_L10, regulator)
        d3b, v3b = evaluate_3b(abs_L12, mults_L12, regulator)
        d3c, v3c, per_k = evaluate_3c_fn(lam_min, lam_max, regulator)
        d3d, v3d = evaluate_3d(abs_L12, mults_L12, regulator)
        d3e, v3e = evaluate_3e(abs_L12, mults_L12, regulator)
        verdicts = (v3a, v3b, v3c, v3d, v3e)  # (local)
        values = (d3a, d3b, d3c, d3d, d3e)  # (local)
        for c_idx, (v, val) in enumerate(zip(verdicts, values)):
            pass_grid[r_idx, c_idx] = v
            value_grid[r_idx, c_idx] = val
        bernstein_per_k[regulator] = per_k
        val_3a[regulator] = d3a
        val_3b[regulator] = d3b
        val_3c[regulator] = d3c
        val_3d[regulator] = d3d
        val_3e[regulator] = d3e

    flat = list(pass_grid.ravel())  # (local)
    n_sub_PASS = sum(1 for v in flat if v == "PASS")  # (local)
    n_sub_INFO = sum(1 for v in flat if v == "INFO")  # (local)
    n_sub_FAIL = sum(1 for v in flat if v == "FAIL")  # (local)
    n_full_PASS = sum(
        1 for r_idx in range(len(ATLAS_A_4))
        if all(pass_grid[r_idx, c] == "PASS" for c in range(len(SUBCHANNELS)))
    )  # (local)

    pred_PASS_regulators = ("zeta", "Zubarev", "SDW")  # (local)
    pred_PASS_satisfied = all(
        all(pass_grid[ATLAS_A_4.index(r), c] == "PASS" for c in range(len(SUBCHANNELS)))
        for r in pred_PASS_regulators
    )  # (local)
    sign_v = "PASS" if pred_PASS_satisfied else "FAIL"
    if n_sub_FAIL == 0 and n_sub_INFO == 0:
        magnitude_v = "PASS"
    elif n_sub_FAIL == 0:
        magnitude_v = "INFO"
    else:
        magnitude_v = "FAIL"
    regime_v = "VALID"
    composite = composite_collapse(n_sub_PASS, n_sub_INFO, n_sub_FAIL,
                                   sign_v, magnitude_v, regime_v)

    return {
        "convention_label": convention_label,
        "pass_grid": pass_grid,
        "value_grid": value_grid,
        "bernstein_per_k": bernstein_per_k,
        "val_3a": val_3a, "val_3b": val_3b, "val_3c": val_3c,
        "val_3d": val_3d, "val_3e": val_3e,
        "n_sub_PASS": n_sub_PASS,
        "n_sub_INFO": n_sub_INFO,
        "n_sub_FAIL": n_sub_FAIL,
        "n_full_PASS": n_full_PASS,
        "sign_v": sign_v,
        "magnitude_v": magnitude_v,
        "regime_v": regime_v,
        "composite": composite,
    }


# ---------------------------------------------------------------------------
# Main orchestration
# ---------------------------------------------------------------------------

def main():
    print("=" * 78)
    print(f"{GATE_ID} — HBW-3C convention audit on §W8-4 SUB-ATLAS-A_2 cascade")
    print(f"Atlas:        {ATLAS_A_4}")
    print(f"Sub-channels: {SUBCHANNELS}")
    print(f"L_max:        {L_MAX} (canonical) / {L_MAX_XCHECK} (cross-check)")
    print(f"tau_fold:     {tau_fold}")
    print(f"Lambda_cut:   {LAMBDA_CUT} (M_KK units; M_KK={M_KK})")
    print(f"Convention A: {CONVENTION_A_LABEL}  (W8-4 baseline)")
    print(f"Convention B: {CONVENTION_B_LABEL}  (plan §W9-106)")
    print("=" * 78)

    # -----------------------------------------------------------------------
    # Step A — Pin and SHA all input files
    # -----------------------------------------------------------------------
    cache_L12_path = SESSION_84_DIR / "s84_spectrum_cache_L12_tau019.npz"  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    plan_path = (
        PROJECT_ROOT / "sessions" / "session-plan" / "session-88-plan-w9.md"
    )  # (local)
    w8_4_npz_path = (
        PROJECT_ROOT / "computations" / "session-87" / "s87_w8_hbw_audit_atlas_a_4.npz"
    )  # (local)
    w8_4_script_path = (
        PROJECT_ROOT / "computations" / "session-87" / "s87_w8_hbw_audit_atlas_a_4.py"
    )  # (local)

    cache_L12_sha = file_sha(cache_L12_path)  # (local)
    canonical_sha = file_sha(canonical_path)  # (local)
    plan_sha = file_sha(plan_path)  # (local)
    w8_4_npz_sha = file_sha(w8_4_npz_path) if w8_4_npz_path.exists() else "MISSING"  # (local)
    w8_4_script_sha = file_sha(w8_4_script_path) if w8_4_script_path.exists() else "MISSING"  # (local)

    print(f"\n[STEP A] Input SHAs (first 16 chars):")
    print(f"         cache_L12        = {cache_L12_sha[:16]}")
    print(f"         canonical        = {canonical_sha[:16]}")
    print(f"         plan             = {plan_sha[:16]}")
    print(f"         W8-4 NPZ         = {w8_4_npz_sha[:16]}")
    print(f"         W8-4 script      = {w8_4_script_sha[:16]}")
    print()

    # -----------------------------------------------------------------------
    # Step B — Load cache + cross-check filter
    # -----------------------------------------------------------------------
    print(f"[STEP B] Loading L_max=12 cache from {cache_L12_path.name} ...")
    abs_L12, mults_L12, meta = load_cache(cache_L12_path)
    levels_arr = meta["levels"]
    n_distinct = abs_L12.size  # (local)
    n_total = int(mults_L12.sum())  # (local)
    lam_min = float(abs_L12.min())  # (local)
    lam_max = float(abs_L12.max())  # (local)
    print(f"         distinct entries:   {n_distinct}")
    print(f"         dim-weighted total: {n_total}")
    print(f"         abs eigenvalue range: [{lam_min:.6f}, {lam_max:.6f}]")
    abs_L10, mults_L10 = synthesize_lmax_filter(abs_L12, mults_L12, levels_arr, L_MAX_XCHECK)
    print(f"         L_max=10 filter: {abs_L10.size} distinct, {int(mults_L10.sum())} dim-weighted")
    print()

    # -----------------------------------------------------------------------
    # Step C — Run cascade under convention A (W8-4 baseline) and convention B
    # -----------------------------------------------------------------------
    print("[STEP C] Running 4x5 sub-channel cascade under convention A (lam-derivative) ...")
    result_A = run_cascade_under_convention(
        CONVENTION_A_LABEL, evaluate_3c_convention_A,
        abs_L12, mults_L12, abs_L10, mults_L10, lam_min, lam_max,
    )
    print(f"         A: composite={result_A['composite']}  "
          f"n_sub_PASS={result_A['n_sub_PASS']}/20 "
          f"n_sub_INFO={result_A['n_sub_INFO']}/20 "
          f"n_sub_FAIL={result_A['n_sub_FAIL']}/20")

    print("[STEP C] Running 4x5 sub-channel cascade under convention B (x-derivative) ...")
    result_B = run_cascade_under_convention(
        CONVENTION_B_LABEL, evaluate_3c_convention_B,
        abs_L12, mults_L12, abs_L10, mults_L10, lam_min, lam_max,
    )
    print(f"         B: composite={result_B['composite']}  "
          f"n_sub_PASS={result_B['n_sub_PASS']}/20 "
          f"n_sub_INFO={result_B['n_sub_INFO']}/20 "
          f"n_sub_FAIL={result_B['n_sub_FAIL']}/20")
    print()

    # Pretty-print sub-grids side-by-side
    print(f"  {'regulator':>10s} | A 3a   3b   3c   3d   3e | B 3a   3b   3c   3d   3e")
    print("  " + "-" * 76)
    for r in range(len(ATLAS_A_4)):
        row_A = " ".join(f"{result_A['pass_grid'][r, c]:>4s}" for c in range(len(SUBCHANNELS)))
        row_B = " ".join(f"{result_B['pass_grid'][r, c]:>4s}" for c in range(len(SUBCHANNELS)))
        print(f"  {ATLAS_A_4[r]:>10s} | {row_A} | {row_B}")
    print()

    # Per-regulator 3c min values (the convention-DEPENDENT sub-channel)
    print("  3c sub-channel min values per regulator:")
    print(f"  {'regulator':>10s} | {'A: min over k,lam':>20s} | {'B: min over k,x':>20s}")
    print("  " + "-" * 60)
    for r in ATLAS_A_4:
        print(f"  {r:>10s} | {result_A['val_3c'][r]:>20.6e} | {result_B['val_3c'][r]:>20.6e}")
    print()

    # -----------------------------------------------------------------------
    # Step D — Compare verdicts and tag CONVENTION-INVARIANT vs DEPENDENT
    # -----------------------------------------------------------------------
    composite_A = result_A["composite"]  # (local)
    composite_B = result_B["composite"]  # (local)
    composite_match = (composite_A == composite_B)  # (local)

    # Sub-grid match (every cell matches)
    subgrid_match = all(
        result_A["pass_grid"][r, c] == result_B["pass_grid"][r, c]
        for r in range(len(ATLAS_A_4)) for c in range(len(SUBCHANNELS))
    )  # (local)

    # 3c-only sub-grid match (the convention-dependent sub-channel)
    sc3c_idx = SUBCHANNELS.index("3c")  # (local)
    sc3c_match = all(
        result_A["pass_grid"][r, sc3c_idx] == result_B["pass_grid"][r, sc3c_idx]
        for r in range(len(ATLAS_A_4))
    )  # (local)

    # Per-regulator sub-3c-cell verdict diff (which rows flip?)
    sc3c_flips = [
        ATLAS_A_4[r] for r in range(len(ATLAS_A_4))
        if result_A["pass_grid"][r, sc3c_idx] != result_B["pass_grid"][r, sc3c_idx]
    ]  # (local)

    # Plan §W9-106 PASS criterion: composite verdict equality
    if composite_A == "INFO" or composite_B == "INFO":
        gate_verdict = "INFO"
        convention_tag = "CONVENTION-INVARIANT-INFO"
    elif composite_match:
        gate_verdict = "PASS"
        convention_tag = "CONVENTION-INVARIANT"
    else:
        gate_verdict = "FAIL"
        convention_tag = "CONVENTION-DEPENDENT"

    print(f"[STEP D] Verdict comparison:")
    print(f"         composite_A      = {composite_A}")
    print(f"         composite_B      = {composite_B}")
    print(f"         composite_match  = {composite_match}")
    print(f"         subgrid_match    = {subgrid_match}")
    print(f"         3c-only match    = {sc3c_match}")
    print(f"         3c flips         = {sc3c_flips}")
    print(f"         convention_tag   = {convention_tag}")
    print(f"         gate_verdict     = {gate_verdict}")
    print()

    # 3-tuple SIGN/MAGNITUDE/REGIME (composite-level diff)
    if composite_match:
        sign_verdict = "PASS"
        magnitude_verdict = "PASS"
    else:
        sign_verdict = "FAIL"
        magnitude_verdict = "FAIL"
    regime_verdict = "VALID"

    # -----------------------------------------------------------------------
    # Step E — Build closure SHA over input-pin map
    # -----------------------------------------------------------------------
    input_pin_map = {  # (local)
        "_gate_id": GATE_ID,
        "_scheme": SCHEME_TAG,
        "_convention": CONVENTION_TAG,
        "_L_max": L_MAX,
        "_L_max_xcheck": L_MAX_XCHECK,
        "cache_L12_sha": cache_L12_sha,
        "canonical_sha": canonical_sha,
        "plan_sha": plan_sha,
        "w8_4_npz_sha": w8_4_npz_sha,
        "w8_4_script_sha": w8_4_script_sha,
        "Vol_SU3_Haar": repr(Vol_SU3_Haar),
        "tau_fold": repr(tau_fold),
        "M_KK": repr(M_KK),
        "ATLAS_A_4": list(ATLAS_A_4),
        "SUBCHANNELS": list(SUBCHANNELS),
        "F_2_RESIDUE": F_2_RESIDUE,
        "F_4_RESIDUE": F_4_RESIDUE,
        "F_6_RESIDUE": F_6_RESIDUE,
        "THRESH_3A_TRUNC": THRESH_3A_TRUNC,
        "THRESH_3B_POS": THRESH_3B_POS,
        "THRESH_3C_DERIV": THRESH_3C_DERIV,
        "THRESH_3D_KAPPA": THRESH_3D_KAPPA,
        "THRESH_3E_EIG": THRESH_3E_EIG,
        "MOMENT_INDICES_BASE": list(MOMENT_INDICES_BASE),
        "MOMENT_INDICES_HAUSDORFF": list(MOMENT_INDICES_HAUSDORFF),
        "BERNSTEIN_K_RANGE": list(BERNSTEIN_K_RANGE),
        "LAMBDA_CUT": LAMBDA_CUT,
        "CONVENTION_A_LABEL": CONVENTION_A_LABEL,
        "CONVENTION_B_LABEL": CONVENTION_B_LABEL,
    }
    audit_sha256 = closure_hash(input_pin_map)  # (local)

    content_payload = {  # (local)
        "result_A_composite": composite_A,
        "result_B_composite": composite_B,
        "result_A_val_3c": {r: repr(result_A["val_3c"][r]) for r in ATLAS_A_4},
        "result_B_val_3c": {r: repr(result_B["val_3c"][r]) for r in ATLAS_A_4},
        "result_A_pass_grid": [
            [str(result_A["pass_grid"][r, c]) for c in range(len(SUBCHANNELS))]
            for r in range(len(ATLAS_A_4))
        ],
        "result_B_pass_grid": [
            [str(result_B["pass_grid"][r, c]) for c in range(len(SUBCHANNELS))]
            for r in range(len(ATLAS_A_4))
        ],
        "n_sub_PASS_A": result_A["n_sub_PASS"],
        "n_sub_FAIL_A": result_A["n_sub_FAIL"],
        "n_sub_PASS_B": result_B["n_sub_PASS"],
        "n_sub_FAIL_B": result_B["n_sub_FAIL"],
        "composite_match": composite_match,
        "subgrid_match": subgrid_match,
        "sc3c_only_match": sc3c_match,
        "sc3c_flips": sc3c_flips,
        "convention_tag": convention_tag,
        "gate_verdict": gate_verdict,
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
    }
    content_sha256 = text_sha(
        json.dumps(content_payload, sort_keys=True, separators=(",", ":"))
    )  # (local)

    print(f"[STEP E] Closure SHAs:")
    print(f"         audit_sha256   = {audit_sha256}")
    print(f"         content_sha256 = {content_sha256}")
    print()

    # -----------------------------------------------------------------------
    # Step F — Save NPZ artifact
    # -----------------------------------------------------------------------
    npz_path = THIS_DIR / "s88_w9_106_hbw_3c_convention_audit.npz"  # (local)
    np.savez(
        npz_path,
        atlas=np.array(ATLAS_A_4, dtype=object),
        subchannels=np.array(SUBCHANNELS, dtype=object),
        # Convention A grid + values
        pass_grid_A=result_A["pass_grid"],
        value_grid_A=result_A["value_grid"],
        val_3a_A=np.array([result_A["val_3a"][r] for r in ATLAS_A_4], dtype=np.float64),
        val_3b_A=np.array([result_A["val_3b"][r] for r in ATLAS_A_4], dtype=np.float64),
        val_3c_A=np.array([result_A["val_3c"][r] for r in ATLAS_A_4], dtype=np.float64),
        val_3d_A=np.array([result_A["val_3d"][r] for r in ATLAS_A_4], dtype=np.float64),
        val_3e_A=np.array([result_A["val_3e"][r] for r in ATLAS_A_4], dtype=np.float64),
        bernstein_zeta_A=np.array(
            [result_A["bernstein_per_k"]["zeta"][f"k={k}"] for k in BERNSTEIN_K_RANGE],
            dtype=np.float64),
        bernstein_Zubarev_A=np.array(
            [result_A["bernstein_per_k"]["Zubarev"][f"k={k}"] for k in BERNSTEIN_K_RANGE],
            dtype=np.float64),
        bernstein_SDW_A=np.array(
            [result_A["bernstein_per_k"]["SDW"][f"k={k}"] for k in BERNSTEIN_K_RANGE],
            dtype=np.float64),
        bernstein_anomaly_A=np.array(
            [result_A["bernstein_per_k"]["anomaly"][f"k={k}"] for k in BERNSTEIN_K_RANGE],
            dtype=np.float64),
        # Convention B grid + values
        pass_grid_B=result_B["pass_grid"],
        value_grid_B=result_B["value_grid"],
        val_3a_B=np.array([result_B["val_3a"][r] for r in ATLAS_A_4], dtype=np.float64),
        val_3b_B=np.array([result_B["val_3b"][r] for r in ATLAS_A_4], dtype=np.float64),
        val_3c_B=np.array([result_B["val_3c"][r] for r in ATLAS_A_4], dtype=np.float64),
        val_3d_B=np.array([result_B["val_3d"][r] for r in ATLAS_A_4], dtype=np.float64),
        val_3e_B=np.array([result_B["val_3e"][r] for r in ATLAS_A_4], dtype=np.float64),
        bernstein_zeta_B=np.array(
            [result_B["bernstein_per_k"]["zeta"][f"k={k}"] for k in BERNSTEIN_K_RANGE],
            dtype=np.float64),
        bernstein_Zubarev_B=np.array(
            [result_B["bernstein_per_k"]["Zubarev"][f"k={k}"] for k in BERNSTEIN_K_RANGE],
            dtype=np.float64),
        bernstein_SDW_B=np.array(
            [result_B["bernstein_per_k"]["SDW"][f"k={k}"] for k in BERNSTEIN_K_RANGE],
            dtype=np.float64),
        bernstein_anomaly_B=np.array(
            [result_B["bernstein_per_k"]["anomaly"][f"k={k}"] for k in BERNSTEIN_K_RANGE],
            dtype=np.float64),
        # Aggregate
        n_sub_PASS_A=result_A["n_sub_PASS"],
        n_sub_INFO_A=result_A["n_sub_INFO"],
        n_sub_FAIL_A=result_A["n_sub_FAIL"],
        n_sub_PASS_B=result_B["n_sub_PASS"],
        n_sub_INFO_B=result_B["n_sub_INFO"],
        n_sub_FAIL_B=result_B["n_sub_FAIL"],
        # Verdict
        composite_A=composite_A,
        composite_B=composite_B,
        composite_match=composite_match,
        subgrid_match=subgrid_match,
        sc3c_only_match=sc3c_match,
        sc3c_flips=np.array(sc3c_flips, dtype=object),
        convention_tag=convention_tag,
        gate_verdict=gate_verdict,
        sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        # Spectrum metadata
        L_max=L_MAX,
        L_max_xcheck=L_MAX_XCHECK,
        lam_min=lam_min,
        lam_max=lam_max,
        Lambda_cut=LAMBDA_CUT,
        n_distinct_L12=n_distinct,
        n_total_L12=n_total,
        # SHAs
        audit_sha256=audit_sha256,
        content_sha256=content_sha256,
    )
    print(f"[STEP F] Saved data: {npz_path}")

    # -----------------------------------------------------------------------
    # Step G — Plot side-by-side cascade verdict comparison
    # -----------------------------------------------------------------------
    png_path = THIS_DIR / "s88_w9_106_hbw_3c_convention_audit.png"  # (local)
    fig, (ax_A, ax_B) = plt.subplots(1, 2, figsize=(14, 5))
    color_map = {"PASS": 0, "INFO": 1, "FAIL": 2}
    cmap = ListedColormap(["#2ca02c", "#ffbb33", "#d62728"])

    for ax, result, title in [
        (ax_A, result_A, f"Conv A (W8-4 baseline; {CONVENTION_A_LABEL})\n"
                         f"composite={composite_A}  sub-FAIL={result_A['n_sub_FAIL']}/20"),
        (ax_B, result_B, f"Conv B (plan §W9-106; {CONVENTION_B_LABEL})\n"
                         f"composite={composite_B}  sub-FAIL={result_B['n_sub_FAIL']}/20"),
    ]:
        cell_colors = np.zeros((len(ATLAS_A_4), len(SUBCHANNELS)), dtype=int)
        for r in range(len(ATLAS_A_4)):
            for c in range(len(SUBCHANNELS)):
                cell_colors[r, c] = color_map[str(result["pass_grid"][r, c])]
        im = ax.imshow(cell_colors, cmap=cmap, vmin=0, vmax=2, aspect="auto")
        ax.set_xticks(range(len(SUBCHANNELS)))
        ax.set_xticklabels(SUBCHANNELS)
        ax.set_yticks(range(len(ATLAS_A_4)))
        ax.set_yticklabels(ATLAS_A_4)
        ax.set_xlabel("Sub-channel")
        ax.set_ylabel("Regulator")
        ax.set_title(title)
        for r in range(len(ATLAS_A_4)):
            for c in range(len(SUBCHANNELS)):
                vt = str(result["pass_grid"][r, c])
                vv = result["value_grid"][r, c]
                tx = f"{vv:.2e}" if abs(vv) < 1e6 else "INF"
                ax.text(c, r, f"{vt}\n{tx}", ha="center", va="center",
                        fontsize=7, color="white" if vt == "FAIL" else "black")
    fig.suptitle(f"{GATE_ID}\nconvention_tag={convention_tag}  gate_verdict={gate_verdict}",
                 fontsize=11)
    plt.tight_layout()
    plt.savefig(png_path, dpi=120)
    plt.close(fig)
    print(f"[STEP G] Saved plot: {png_path}")
    print()

    # -----------------------------------------------------------------------
    # Step H — Append verdict line + companion rows
    # -----------------------------------------------------------------------
    verdict_path = THIS_DIR / "s88_gate_verdicts.txt"  # (local)
    canonical_line = (
        f"{GATE_ID}: {gate_verdict} -- "
        f"value='convA={composite_A};convB={composite_B};tag={convention_tag};"
        f"sc3c_flips={','.join(sc3c_flips) if sc3c_flips else 'none'}' "
        f"scheme={SCHEME_TAG} convention={CONVENTION_TAG} "
        f"L_max={L_MAX} audit_sha256={audit_sha256} "
        f"content_sha256={content_sha256} schema_version={SCHEMA_VERSION}\n"
    )  # (local)
    companion_dual_sha = (
        f"# audit_sha256_short={audit_sha256[:16]} "
        f"content_sha256_short={content_sha256[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    companion_3tuple = (
        f"# sign_verdict={sign_verdict} magnitude_verdict={magnitude_verdict} "
        f"regime_verdict={regime_verdict} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )  # (local)
    companion_subgrid = (
        f"# subgrid_match={subgrid_match} sc3c_only_match={sc3c_match} "
        f"composite_match={composite_match} "
        f"# {GATE_ID} convention-comparison aggregate\n"
    )  # (local)
    with open(verdict_path, "a", encoding="utf-8") as fh:
        fh.write(canonical_line)
        fh.write(companion_dual_sha)
        fh.write(companion_3tuple)
        fh.write(companion_subgrid)
    print(f"[STEP H] Appended verdict line + 3 companion rows to: {verdict_path}")
    print()

    # -----------------------------------------------------------------------
    # Final summary
    # -----------------------------------------------------------------------
    print("=" * 78)
    print(f"VERDICT (gate): {gate_verdict}  ({convention_tag})")
    print(f"  composite_A: {composite_A}    composite_B: {composite_B}")
    print(f"  subgrid_match: {subgrid_match}  sc3c_only_match: {sc3c_match}")
    print(f"  sc3c flips (rows where 3c verdict differs): {sc3c_flips}")
    print(f"audit_sha256:   {audit_sha256}")
    print(f"content_sha256: {content_sha256}")
    print("=" * 78)

    return {
        "gate_verdict": gate_verdict,
        "convention_tag": convention_tag,
        "composite_A": composite_A,
        "composite_B": composite_B,
        "audit_sha256": audit_sha256,
        "content_sha256": content_sha256,
    }


if __name__ == "__main__":
    main()
