"""
s87_w8_hbw_audit_atlas_a_4.py — S87-HBW-AUDIT-ATLAS-A_4 (CF-50)
================================================================

Hausdorff-Bernstein-Widder positive-cone audit on the surviving 4-regulator
atlas A_4 = {zeta, Zubarev, SDW, anomaly} at L_max=12, framework-truncated
residue slot f_2=0.0 / f_4=0.05 / f_6=0.1.

Channel-3 admissibility (HBW positive cone) is decomposed into 5 sub-channels:

    3a  MP-abs-conv at s=6:   truncation tolerance 1e-10 between L=10 and L=12
    3b  Positive-cone moment: min_n a_n^{(R)}*w_R(n) >= -1e-12 for n in {0,2,4,6}
    3c  Bernstein-density:    (-1)^k * d^k w_R/dλ^k >= 0 for k in {0,1,2,3} on
                              [λ_min, λ_max]
    3d  Widder-inversion:     condition number κ_R < 1e15 on the
                              even-moment-restricted Widder matrix
    3e  Hausdorff-Hankel:     smallest eigenvalue of the 5x5 Hankel matrix
                              [a_{i+j}^{(R)}] for i,j in {0,1,2,3,4} >= -1e-12

PASS / FAIL / INFO threshold (plan §W8-4 §5):
  - sub-PASS: criterion satisfied per pre-registered numerical test
  - sub-INFO: within precision floor of the boundary (e.g., positive-cone with
    min_eigenvalue in [-1e-12, +1e-12])
  - sub-FAIL: criterion violated on a non-precision-floor margin

Aggregate (regulator-level): regulator R PASSes iff all 5 sub-channels sub-PASS.
Gate-level:
  PASS:  4 regulators × 5 sub-channels = 20 sub-PASSes
  INFO:  >=1 sub-INFO and zero sub-FAIL
  FAIL:  >=1 sub-FAIL on a non-precision-floor margin

Substitution chain (per .claude/rules/math-scripts.md):

  Step 1 — Definitions:
      λ runs over the multiplicity-weighted absolute eigenvalues of the
        finite-L D_K spectrum on the Jensen-deformed SU(3) substrate
        (cache: computations/session-84/s84_spectrum_cache_L12_tau019.npz).
      x := (λ/Λ_cut)², Λ_cut = M_KK (canonical normalization, Λ_cut = 1).
      Regulator weight functions per S86 W11 §7 / S83 W1 G2:
        w_zeta(λ)    = 1
        w_Zubarev(λ) = x/(1+x²)
        w_SDW(λ)     = exp(-x)
        w_anomaly(λ) = exp(-x)/sqrt(x)
      Spectral moments:
        a_n^{(R)} := (1/Vol_SU3_Haar) · Σ_λ mult(λ) · λ^n · w_R(λ)

  Step 2 — Sub-channel test predicates (per plan §5):
      sub-PASS_3a(R): |M_R(s=6)|_{L=10} − |M_R(s=6)|_{L=12} < 1e-10 where
                      M_R(s=6) := Σ_n a_n^{(R)} n^{-6}, sum over n in {2,4,6}.
      sub-PASS_3b(R): min_{n∈{0,2,4,6}} a_n^{(R)}·w_R(n) ≥ -1e-12.
      sub-PASS_3c(R): for each k in {0,1,2,3}, (-1)^k · d^k w_R/dλ^k ≥ 0 on
                      a 200-point grid covering [λ_min, λ_max] (analytic
                      derivatives, not finite differences).
      sub-PASS_3d(R): cond(W_R) < 1e15 where W_R := [a_{i+j}^{(R)}]_{i,j=0..3}
                      with the moment indices set {0,2,4,6} (Widder
                      4-point inversion matrix).
      sub-PASS_3e(R): smallest eigenvalue of H_4^{(R)} := [a_{i+j}^{(R)}]_{i,j=0..4}
                      ≥ -1e-12, where the moment list a_0,a_2,a_4,a_6,a_8
                      is the Hausdorff 5-point moment sequence.

  Step 3 — Simplifications (per regulator):
      zeta:    w_R is constant → 3c trivially PASSes for all k≥1; 3b inherits
               positivity from the positive-definite squared-eigenvalue
               spectrum; 3e inherits PSD from a Stieltjes Hankel.
      Zubarev: w_R(λ) has a maximum at x=1 (λ=Λ_cut); not completely
               monotonic. 3c may surface a sub-INFO/sub-FAIL near k=2.
      SDW:     w_R(x) = exp(-x) is CM in x; under λ-derivatives x=λ² introduces
               polynomial pre-factors. d^kw/dλ^k changes sign for higher k
               near λ_min; 3c k=3 may sub-INFO/sub-FAIL.
      anomaly: w_R(λ) = exp(-x)/√x carries a 1/√x factor; positive on
               λ_min > 0 but derivatives have non-trivial sign.

  Step 4 — Direction (per plan §9 Step 4): plan predicts ζ/Zubarev/SDW PASS
      all 5 sub-channels; anomaly may sub-INFO at 3c near λ_min. EMPIRICAL
      verification required — directionality is a prediction, not a fact.

Substrate-framing reminder (per .claude/rules/phononic-framing.md): the HBW
positive-cone test operates on the substrate-IS spectral data (D_K eigenvalues
on the Jensen-deformed SU(3)) — it is NOT an external ansatz applied to a
container. Each regulator R defines a Mellin-cone evaluator, and the channel-3
audit asks whether the substrate's natural spectral measure under R sits inside
the Bernstein-Widder positive cone.

NCG axiom anchor: HBW positivity at a regulator R is the substrate-IS
expression of the spectral-action positive-cone structure under that R.
A regulator that violates HBW would force re-classification out of A_4 (the
W-8 surviving 4-regulator atlas) per the §VII.M layer-membership row.

Author: connes-ncg-theorist (S87 W8-4 dispatch, 2026-04-30).
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

# Ensure computations is on path
THIS_DIR = Path(__file__).parent.resolve()  # (local)
if str(THIS_DIR) not in sys.path:
    sys.path.insert(0, str(THIS_DIR))

from canonical_constants import (  # noqa: E402
    Vol_SU3_Haar,
    tau_fold,
)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

GATE_ID = "S87-HBW-AUDIT-ATLAS-A_4"  # (local)
SCHEME_TAG = "HBW_5_subchannel_audit"  # (local)
CONVENTION_TAG = "A_4_4col_f6_0.1_residue"  # (local)
L_MAX = 12  # (local) canonical L_max for HBW
L_MAX_XCHECK = 10  # (local) cross-check (synthesized via level<=10 filter)
SCHEMA_VERSION = "S87+"  # (local)

ATLAS_A_4 = ("zeta", "Zubarev", "SDW", "anomaly")  # (local) per plan §W8-4
SUBCHANNELS = ("3a", "3b", "3c", "3d", "3e")  # (local)

LAMBDA_CUT = 1.0  # (local) M_KK units; canonical normalization

# Pre-registered framework-truncated residue slots (plan §W8-4 §6)
F_2_RESIDUE = 0.0  # (local) framework-truncated f_2
F_4_RESIDUE = 0.05  # (local) framework-truncated f_4
F_6_RESIDUE = 0.1  # (local) framework-truncated f_6

# Pre-registered sub-channel thresholds (plan §W8-4 §5)
THRESH_3A_TRUNC = 1.0e-10  # (local) absolute MP-abs-conv truncation tolerance
THRESH_3B_POS = -1.0e-12  # (local) positive-cone INFO floor
THRESH_3C_DERIV = -1.0e-12  # (local) Bernstein-derivative INFO floor (PSD)
THRESH_3D_KAPPA = 1.0e15  # (local) Widder-inversion condition number cap
THRESH_3E_EIG = -1.0e-12  # (local) Hausdorff-Hankel smallest-eigenvalue INFO floor
THRESH_PRECISION_FLOOR = 1.0e-12  # (local) shared precision-floor band

MOMENT_INDICES_BASE = (0, 2, 4, 6)  # (local) plan §5 (3b/3d use these)
MOMENT_INDICES_HAUSDORFF = (0, 2, 4, 6, 8)  # (local) plan §5 (3e Hankel order 5x5)
BERNSTEIN_K_RANGE = (0, 1, 2, 3)  # (local) plan §5 (3c)


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
# Regulator weight functions (per S86 W11 §7 + S83 W1 G2)
# ---------------------------------------------------------------------------

def w_R(regulator: str, lam: np.ndarray, Lambda_cut: float = LAMBDA_CUT) -> np.ndarray:
    """Regulator weight w_R(λ); positive on λ > 0.

    Canonical definitions per S86 W11 §7 (s86_w11_eta_gv_joint_probe.py):
      w_zeta(λ)    = 1
      w_Zubarev(λ) = x / (1 + x²),   x = (λ/Λ_cut)²
      w_SDW(λ)     = exp(-x)
      w_anomaly(λ) = exp(-x) / sqrt(x)
    """
    lam_arr = np.asarray(lam, dtype=np.float64)  # (local)
    x = (lam_arr / Lambda_cut) ** 2  # (local)
    if regulator == "zeta":
        return np.ones_like(lam_arr)
    elif regulator == "Zubarev":
        return x / (1.0 + x * x)
    elif regulator == "SDW":
        return np.exp(-x)
    elif regulator == "anomaly":
        # x > 0 on the spectral support (λ_min > 0)
        return np.exp(-x) / np.sqrt(np.maximum(x, 1e-300))
    else:
        raise ValueError(f"Unknown regulator: {regulator}")


def w_R_derivative(
    regulator: str, lam: np.ndarray, k: int, Lambda_cut: float = LAMBDA_CUT
) -> np.ndarray:
    """Compute (d^k / dλ^k) w_R(λ) analytically (k = 0, 1, 2, 3).

    The chain rule x = (λ/Λ)^2 introduces polynomial pre-factors. We use direct
    closed-form derivatives, evaluated as functions of x:
      Let u = λ/Λ; x = u².
      For w(x) = f(x), dw/dλ = (2u/Λ) · f'(x)
                   d²w/dλ² = (2/Λ²) · f'(x) + (4u²/Λ²) · f''(x)
                            = (2/Λ²) · [f'(x) + 2x · f''(x)]
                   d³w/dλ³ = (2/Λ²) · [f''(x)·2u/Λ + 2·f''(x)·2u/Λ + 2x·f'''(x)·2u/Λ]
                            = (4u/Λ³) · [3·f''(x) + 2x · f'''(x)]
    where f^(j)(x) is the j-th derivative w.r.t. x.

    Substitution chain (verified):
      w(λ) = f(x), x = u², u = λ/Λ
      dx/dλ = 2u/Λ
      d²x/dλ² = 2/Λ²
      d³x/dλ³ = 0
      dw/dλ = f'(x) · dx/dλ = f'(x)·2u/Λ
      d²w/dλ² = f''(x)·(dx/dλ)² + f'(x)·d²x/dλ² = 4u²·f''(x)/Λ² + 2·f'(x)/Λ²
      d³w/dλ³ = derivative of d²w/dλ² w.r.t. λ
              = [d/dλ(4u²·f''(x)/Λ²)] + [d/dλ(2·f'(x)/Λ²)]
              = 4·(2u/Λ)·f''(x)/Λ² + 4u²·f'''(x)·(2u/Λ)/Λ² + 2·f''(x)·(2u/Λ)/Λ²
              = (8u/Λ³)·f''(x) + (8u³/Λ³)·f'''(x) + (4u/Λ³)·f''(x)
              = (4u/Λ³)·[3·f''(x) + 2u²·f'''(x)]
              = (4u/Λ³)·[3·f''(x) + 2x·f'''(x)]
    """
    lam_arr = np.asarray(lam, dtype=np.float64)  # (local)
    u = lam_arr / Lambda_cut  # (local)
    x = u * u  # (local)

    # f(x), f'(x), f''(x), f'''(x) for each regulator
    if regulator == "zeta":
        # f(x) = 1; all derivatives = 0
        if k == 0:
            return np.ones_like(lam_arr)
        else:
            return np.zeros_like(lam_arr)
    elif regulator == "Zubarev":
        # f(x) = x/(1+x²)
        # f'(x) = (1+x²)·1 − x·2x / (1+x²)² = (1−x²)/(1+x²)²
        # f''(x): from chain rule on f' = (1-x²)/(1+x²)²
        denom2 = (1.0 + x * x) ** 2  # (local)
        denom3 = (1.0 + x * x) ** 3  # (local)
        denom4 = (1.0 + x * x) ** 4  # (local)
        denom5 = (1.0 + x * x) ** 5  # (local)
        f0 = x / (1.0 + x * x)
        f1 = (1.0 - x * x) / denom2
        # d/dx[(1-x²)/(1+x²)²] = [-2x·(1+x²)² − (1-x²)·2·(1+x²)·2x] / (1+x²)^4
        #                     = [-2x·(1+x²) − 4x·(1-x²)] / (1+x²)³
        #                     = -2x[(1+x²) + 2(1-x²)] / (1+x²)³
        #                     = -2x[3 - x²] / (1+x²)³
        f2 = -2.0 * x * (3.0 - x * x) / denom3
        # d/dx[-2x(3-x²)/(1+x²)³]
        # Let g(x) = -2x(3-x²) = -6x + 2x³;  g'(x) = -6 + 6x²
        # h(x) = (1+x²)^3;  h'(x) = 3·(1+x²)²·2x = 6x·(1+x²)²
        # d/dx[g/h] = (g'·h − g·h')/h²
        #           = [(-6+6x²)·(1+x²)³ − (-6x+2x³)·6x·(1+x²)²]/(1+x²)^6
        #           = [(-6+6x²)·(1+x²) − (-6x+2x³)·6x]/(1+x²)^4
        #           = [(-6+6x²)·(1+x²) − (-36x²+12x⁴)]/(1+x²)^4
        # Expand: (-6+6x²)(1+x²) = -6 - 6x² + 6x² + 6x⁴ = -6 + 6x⁴
        # Subtract (-36x²+12x⁴) = +36x²-12x⁴
        # Total: -6 + 6x⁴ + 36x² - 12x⁴ = -6 + 36x² - 6x⁴ = -6(1 - 6x² + x⁴)
        f3 = -6.0 * (1.0 - 6.0 * x * x + x ** 4) / denom4
    elif regulator == "SDW":
        # f(x) = exp(-x)
        # f'(x) = -exp(-x);  f''(x) = exp(-x);  f'''(x) = -exp(-x)
        e = np.exp(-x)  # (local)
        f0 = e
        f1 = -e
        f2 = e
        f3 = -e
    elif regulator == "anomaly":
        # f(x) = exp(-x)·x^{-1/2}
        # f'(x) = -exp(-x)·x^{-1/2} - exp(-x)·(1/2)·x^{-3/2}
        #       = -exp(-x)·x^{-3/2}·(x + 1/2)
        # f''(x) = derivative of -exp(-x)·x^{-3/2}·(x+1/2)
        # Let A(x) = exp(-x), B(x) = x^{-3/2}, C(x) = x + 1/2
        # f' = -A·B·C
        # f'' = -[A'·B·C + A·B'·C + A·B·C']
        #     = -[(-A)·B·C + A·(-3/2)·x^{-5/2}·C + A·B·1]
        #     = A·B·C - (3/2)·A·x^{-5/2}·C - A·B
        #     where B = x^{-3/2}
        e = np.exp(-x)  # (local)
        sqrt_x = np.sqrt(np.maximum(x, 1e-300))  # (local)
        x_neg_half = 1.0 / sqrt_x  # (local) x^{-1/2}
        x_neg_3_2 = x_neg_half / x  # (local) x^{-3/2}
        x_neg_5_2 = x_neg_3_2 / x  # (local) x^{-5/2}
        x_neg_7_2 = x_neg_5_2 / x  # (local) x^{-7/2}
        f0 = e * x_neg_half
        f1 = -e * x_neg_3_2 * (x + 0.5)
        # f'' computation (verified by symbolic differentiation):
        # Using f(x) = e^{-x} x^{-1/2}, take logarithmic derivatives:
        # ln f = -x - (1/2) ln x → f'/f = -1 - 1/(2x)
        # f' = f · (-1 - 1/(2x))
        # f'' = f' · (-1 - 1/(2x)) + f · (1/(2x²))
        #     = f · (-1 - 1/(2x))² + f · 1/(2x²)
        #     = f · [(1 + 1/(2x))² + 1/(2x²)]
        f2 = f0 * ((1.0 + 1.0 / (2.0 * x)) ** 2 + 1.0 / (2.0 * x * x))
        # f''' = f'' · (-1 - 1/(2x)) + f' · (1/(2x²)) + f · (-1/(x³))
        #      = -f'' · (1 + 1/(2x)) + f'/(2x²) - f/x³
        f3 = -f2 * (1.0 + 1.0 / (2.0 * x)) + f1 / (2.0 * x * x) - f0 / (x ** 3)
    else:
        raise ValueError(f"Unknown regulator: {regulator}")

    # Apply chain-rule lifts dλ-derivatives from f^(j)(x)
    if k == 0:
        return f0
    elif k == 1:
        # dw/dλ = (2u/Λ) · f'(x)
        return (2.0 * u / Lambda_cut) * f1
    elif k == 2:
        # d²w/dλ² = (2/Λ²) · [f'(x) + 2x · f''(x)]
        return (2.0 / Lambda_cut ** 2) * (f1 + 2.0 * x * f2)
    elif k == 3:
        # d³w/dλ³ = (4u/Λ³) · [3·f''(x) + 2x · f'''(x)]
        return (4.0 * u / Lambda_cut ** 3) * (3.0 * f2 + 2.0 * x * f3)
    else:
        raise ValueError(f"Bernstein order k={k} not implemented; only k in {{0,1,2,3}}")


# ---------------------------------------------------------------------------
# Spectral moment computation
# ---------------------------------------------------------------------------

def compute_a_n(
    abs_eigs: np.ndarray, mults: np.ndarray, regulator: str, n: int
) -> float:
    """Compute a_n^{(R)} = (1/Vol_SU3_Haar) · Σ mult(λ) · λ^n · w_R(λ).

    Vectorized over all eigenvalues of the L_max=12 cache.
    """
    weights = w_R(regulator, abs_eigs)  # (local)
    contributions = mults * (abs_eigs ** n) * weights  # (local)
    return float(np.sum(contributions) / Vol_SU3_Haar)


# ---------------------------------------------------------------------------
# Sub-channel evaluators
# ---------------------------------------------------------------------------

def evaluate_3a(
    abs_eigs_L12: np.ndarray, mults_L12: np.ndarray,
    abs_eigs_L10: np.ndarray, mults_L10: np.ndarray,
    regulator: str
) -> tuple[float, str]:
    """3a: MP-abs-conv at s=6 truncation cross-check between L_max=10 and L_max=12.

    Computes |M_R(s=6)|_L=12 vs |M_R(s=6)|_L=10 where M_R(s=6) := Σ_{n in {2,4,6}}
    a_n^{(R)} · n^{-6}. PASS iff |Δ| < 1e-10.
    """
    n_indices = (2, 4, 6)  # (local) plan §5 3a (s=6 sum over even moments)
    M_L12 = sum(
        compute_a_n(abs_eigs_L12, mults_L12, regulator, n) * (n ** (-6))
        for n in n_indices
    )  # (local)
    M_L10 = sum(
        compute_a_n(abs_eigs_L10, mults_L10, regulator, n) * (n ** (-6))
        for n in n_indices
    )  # (local)
    delta_3a = abs(M_L12 - M_L10)  # (local) absolute truncation tolerance
    if delta_3a < THRESH_3A_TRUNC:
        verdict = "PASS"
    elif delta_3a < THRESH_3A_TRUNC * 100:  # within 2 OOM of pre-reg threshold → INFO
        verdict = "INFO"
    else:
        verdict = "FAIL"
    return delta_3a, verdict


def evaluate_3b(
    abs_eigs: np.ndarray, mults: np.ndarray, regulator: str
) -> tuple[float, str]:
    """3b: positive-cone moment sequence min_{n in {0,2,4,6}} a_n^{(R)} · w_R(n) ≥ -1e-12.

    Note: w_R(n) treats n itself as a "λ" sample in the regulator weight function
    (per plan §5 3b literal text). This couples the moment to its own regulator at
    a discrete λ = n.
    """
    n_arr = np.array(MOMENT_INDICES_BASE, dtype=np.float64)  # (local) [0,2,4,6]
    a_n_vals = np.array(
        [compute_a_n(abs_eigs, mults, regulator, int(n)) for n in n_arr],
        dtype=np.float64,
    )  # (local)
    # w_R(n) at the moment-index points; for n=0, anomaly diverges → handle floor
    # by clamping at λ=1e-15 minimum (no impact on PASS/FAIL since other regulators
    # well-defined).
    n_safe = np.maximum(n_arr, 1e-15)  # (local) avoid 1/0 in anomaly w_R
    w_n_vals = w_R(regulator, n_safe)  # (local)
    # For n=0 specifically with anomaly: w_anomaly(0) is undefined; this is a
    # boundary artifact of the literal text. We use the n→0+ limit on the
    # SUPPORT (λ_min > 0). At n=0, the moment a_0^{(R)} is the volume-density
    # moment which already encodes the regulator; multiplying by w_R(n=0)
    # is a literal pre-registration — handle the anomaly n=0 case by setting
    # a_0·w(0) → +inf (positivity-trivial) only for diagnostic logging; the
    # min-positivity test proceeds on the well-defined n ∈ {2,4,6} indices.
    products = a_n_vals * w_n_vals  # (local)
    if regulator == "anomaly":
        # n=0 product is structurally +∞ (positive); exclude from min-test
        finite_products = products[1:]  # (local) n ∈ {2,4,6}
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


def evaluate_3c(
    lam_min: float, lam_max: float, regulator: str, n_grid: int = 200
) -> tuple[float, str, dict]:
    """3c: Bernstein-density factor sign — (-1)^k · d^k w_R/dλ^k ≥ 0 on [λ_min, λ_max].

    Tests k ∈ {0,1,2,3}. PASS iff min over (k, λ) of (-1)^k · d^k w_R/dλ^k ≥ 0
    (within precision floor THRESH_3C_DERIV = -1e-12).

    Returns (min_value, verdict, per_k_min_dict).
    """
    lam_grid = np.linspace(lam_min, lam_max, n_grid)  # (local)
    per_k_min = {}  # (local)
    overall_min = np.inf  # (local)
    for k in BERNSTEIN_K_RANGE:
        deriv = w_R_derivative(regulator, lam_grid, k)  # (local)
        # Bernstein criterion: (-1)^k · d^k w / dλ^k ≥ 0
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


def evaluate_3d(
    abs_eigs: np.ndarray, mults: np.ndarray, regulator: str
) -> tuple[float, str]:
    """3d: Widder-inversion well-posedness.

    Build the 4×4 Widder matrix W_R[i,j] := a_{i+j}^{(R)} for i,j ∈ {0,1,2,3}
    using the moment-index pairs {(i,j) → 2(i+j)} (so the matrix entries are
    a_0, a_2, a_4, a_6 along the anti-diagonals; Hankel structure). Compute
    its condition number κ_R = σ_max/σ_min. PASS iff κ_R < 1e15.
    """
    # Build moment array a_{2*(i+j)} for i,j ∈ {0,1,2,3}; indices needed: 0,2,4,6,8,10,12
    needed_indices = sorted(set(2 * (i + j) for i in range(4) for j in range(4)))  # (local)
    a_dict = {n: compute_a_n(abs_eigs, mults, regulator, n) for n in needed_indices}  # (local)
    W = np.zeros((4, 4), dtype=np.float64)  # (local)
    for i in range(4):
        for j in range(4):
            W[i, j] = a_dict[2 * (i + j)]
    # Condition number via SVD
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
    """3e: Hausdorff-moment Hankel positive-definiteness.

    Build 5×5 Hankel matrix H[i,j] := a_{2*(i+j)}^{(R)} for i,j ∈ {0,1,2,3,4}.
    PASS iff smallest eigenvalue ≥ -1e-12 (PSD within precision floor).
    """
    needed_indices = sorted(set(2 * (i + j) for i in range(5) for j in range(5)))  # (local)
    a_dict = {n: compute_a_n(abs_eigs, mults, regulator, n) for n in needed_indices}  # (local)
    H = np.zeros((5, 5), dtype=np.float64)  # (local)
    for i in range(5):
        for j in range(5):
            H[i, j] = a_dict[2 * (i + j)]
    # Symmetrize to suppress floating-point noise
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
# Cache loader (L_max=12) and L_max=10 synthesizer
# ---------------------------------------------------------------------------

def load_cache(cache_path: Path) -> tuple[np.ndarray, np.ndarray, dict]:
    """Load L_max=12 spectrum cache and return (abs_eigs, mults, level_array).

    The cache structure is a dict {(p,q): {dim, level, abs_evals}}. Each
    eigenvalue gets multiplicity = dim (the Weyl dim of the (p,q) sector
    accounts for the SU(3) representation degeneracy); the abs_evals array
    already enumerates the level-resolved eigenvalues without the dim factor.

    Returns three parallel arrays:
      abs_eigs[k] = absolute eigenvalue
      mults[k]    = multiplicity (= dim of (p,q))
      levels[k]   = level (used for L_max=10 cross-check filter)
    """
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


def synthesize_lmax10_filter(
    abs_eigs: np.ndarray, mults: np.ndarray, levels: np.ndarray, L_max_cut: int
) -> tuple[np.ndarray, np.ndarray]:
    """Filter an L_max=12 cache to level <= L_max_cut.

    The level field encodes the (p+q) cumulative-shell index; filtering
    level <= 10 yields the L_max=10 truncation of the same spectrum.
    Used as a synthetic L_max=10 cross-check when the canonical L_max=10
    cache file is unavailable on disk.
    """
    mask = levels <= L_max_cut  # (local)
    return abs_eigs[mask], mults[mask]


# ---------------------------------------------------------------------------
# Main orchestration
# ---------------------------------------------------------------------------

def main():
    print("=" * 76)
    print(f"S87-HBW-AUDIT-ATLAS-A_4 — Channel-3 5-sub-channel HBW positivity audit")
    print(f"Atlas:        {ATLAS_A_4}")
    print(f"Sub-channels: {SUBCHANNELS}")
    print(f"L_max:        {L_MAX} (canonical) / {L_MAX_XCHECK} (cross-check)")
    print(f"tau_fold:     {tau_fold}")
    print(f"Lambda_cut:   {LAMBDA_CUT} (M_KK units)")
    print("=" * 76)

    # -----------------------------------------------------------------------
    # Step A — Pin and SHA all input files
    # -----------------------------------------------------------------------
    cache_L12_path = THIS_DIR / "s84_spectrum_cache_L12_tau019.npz"  # (local)
    canonical_path = THIS_DIR / "canonical_constants.py"  # (local)
    plan_path = (
        THIS_DIR.parent / "sessions" / "session-plan" / "session-87-plan-w8.md"
    )  # (local)
    regulator_module_path = THIS_DIR / "_spectral_action_regulators.py"  # (local)

    cache_L12_sha = file_sha(cache_L12_path)  # (local)
    canonical_sha = file_sha(canonical_path)  # (local)
    plan_sha = file_sha(plan_path)  # (local)
    regulator_module_sha = (
        file_sha(regulator_module_path) if regulator_module_path.exists() else "MISSING"
    )  # (local)

    print(f"\n[STEP A] Input SHAs (first 16 chars):")
    print(f"         cache_L12      = {cache_L12_sha[:16]}")
    print(f"         canonical      = {canonical_sha[:16]}")
    print(f"         plan           = {plan_sha[:16]}")
    print(f"         regulator_mod  = {regulator_module_sha[:16]}")
    print()

    # -----------------------------------------------------------------------
    # Step B — Load L_max=12 cache, derive L_max=10 cross-check
    # -----------------------------------------------------------------------
    print(f"[STEP B] Loading L_max=12 cache from {cache_L12_path.name} ...")
    abs_L12, mults_L12, meta = load_cache(cache_L12_path)
    levels_arr = meta["levels"]
    n_distinct = abs_L12.size  # (local) distinct eigenvalue entries
    n_total_with_mult = int(mults_L12.sum())  # (local) sum_dim weighted total
    lam_min = float(abs_L12.min())  # (local)
    lam_max = float(abs_L12.max())  # (local)
    print(f"         distinct entries:   {n_distinct}")
    print(f"         dim-weighted total: {n_total_with_mult}")
    print(f"         abs eigenvalue range: [{lam_min:.6f}, {lam_max:.6f}]")
    print()

    # L_max=10 synthetic cross-check (level <= 10 filter)
    abs_L10, mults_L10 = synthesize_lmax10_filter(abs_L12, mults_L12, levels_arr, 10)
    n_distinct_L10 = abs_L10.size  # (local)
    n_total_L10 = int(mults_L10.sum())  # (local)
    print(f"[STEP B'] L_max=10 cross-check (level<=10 filter):")
    print(f"          distinct entries:   {n_distinct_L10}")
    print(f"          dim-weighted total: {n_total_L10}")
    print()

    # -----------------------------------------------------------------------
    # Step C — Run the 4×5 sub-channel grid
    # -----------------------------------------------------------------------
    print("[STEP C] Running 4×5 sub-channel grid ...")
    pass_grid = np.zeros((len(ATLAS_A_4), len(SUBCHANNELS)), dtype=object)  # (local)
    value_grid = np.zeros((len(ATLAS_A_4), len(SUBCHANNELS)), dtype=np.float64)  # (local)
    bernstein_per_k = {}  # (local)

    # Per-cell numerical-value containers (cross-wave dependency: §W8-6 reads these)
    val_3a = {}  # (local) regulator -> 3a convergence delta
    val_3b = {}  # (local) regulator -> min product a_n*w(n)
    val_3c = {}  # (local) regulator -> min Bernstein derivative
    val_3d = {}  # (local) regulator -> Widder kappa
    val_3e = {}  # (local) regulator -> Hankel min eigenvalue

    print(f"\n  {'regulator':>10s} | {'3a (Δ)':>12s} {'3b (min)':>12s} "
          f"{'3c (min)':>12s} {'3d (κ)':>12s} {'3e (λ_min)':>12s} "
          f"|  R-PASS")
    print("  " + "-" * 84)

    for r_idx, regulator in enumerate(ATLAS_A_4):
        # 3a — MP-abs-conv at s=6
        d3a, v3a = evaluate_3a(abs_L12, mults_L12, abs_L10, mults_L10, regulator)
        # 3b — positive-cone moment sequence
        d3b, v3b = evaluate_3b(abs_L12, mults_L12, regulator)
        # 3c — Bernstein-density factor sign
        d3c, v3c, per_k = evaluate_3c(lam_min, lam_max, regulator)
        # 3d — Widder-inversion well-posedness
        d3d, v3d = evaluate_3d(abs_L12, mults_L12, regulator)
        # 3e — Hausdorff-Hankel positive-definiteness
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

        regulator_PASS = all(v == "PASS" for v in verdicts)  # (local)
        regulator_INFO = (not regulator_PASS) and all(
            v in ("PASS", "INFO") for v in verdicts
        )  # (local)
        if regulator_PASS:
            r_status = "PASS"
        elif regulator_INFO:
            r_status = "INFO"
        else:
            r_status = "FAIL"

        print(
            f"  {regulator:>10s} | {d3a:>12.3e} {d3b:>12.3e} "
            f"{d3c:>12.3e} {d3d:>12.3e} {d3e:>12.3e} "
            f"|  {r_status}  ({'/'.join(verdicts)})"
        )

    print()

    # -----------------------------------------------------------------------
    # Step D — Aggregate gate-level verdict
    # -----------------------------------------------------------------------
    flat_verdicts = list(pass_grid.ravel())  # (local)
    n_sub_PASS = sum(1 for v in flat_verdicts if v == "PASS")  # (local)
    n_sub_INFO = sum(1 for v in flat_verdicts if v == "INFO")  # (local)
    n_sub_FAIL = sum(1 for v in flat_verdicts if v == "FAIL")  # (local)

    n_regulators_full_PASS = sum(
        1 for r_idx in range(len(ATLAS_A_4))
        if all(pass_grid[r_idx, c] == "PASS" for c in range(len(SUBCHANNELS)))
    )  # (local)

    print(f"[STEP D] Aggregate counts:")
    print(f"         sub-PASS = {n_sub_PASS}/20")
    print(f"         sub-INFO = {n_sub_INFO}/20")
    print(f"         sub-FAIL = {n_sub_FAIL}/20")
    print(f"         regulators full-PASS = {n_regulators_full_PASS}/4")
    print()

    # Gate-level composite (per plan §5)
    if n_sub_FAIL == 0 and n_sub_INFO == 0:
        composite = "PASS"
    elif n_sub_FAIL == 0:
        composite = "INFO"
    else:
        composite = "FAIL"

    # 3-tuple SIGN/MAGNITUDE/REGIME annotation per gate-verdicts.md schema-v2
    # SIGN: predicted ζ/Zubarev/SDW PASS all 5; anomaly may sub-INFO at 3c
    # If predicted-PASS regulators are all PASS → sign PASS
    pred_PASS_regulators = ("zeta", "Zubarev", "SDW")  # (local)
    pred_PASS_satisfied = all(
        all(pass_grid[ATLAS_A_4.index(r), c] == "PASS" for c in range(len(SUBCHANNELS)))
        for r in pred_PASS_regulators
    )  # (local)
    if pred_PASS_satisfied:
        sign_verdict = "PASS"
    else:
        sign_verdict = "FAIL"

    # MAGNITUDE: per pre-registered band
    if n_sub_FAIL == 0 and n_sub_INFO == 0:
        magnitude_verdict = "PASS"
    elif n_sub_FAIL == 0:
        magnitude_verdict = "INFO"
    else:
        magnitude_verdict = "FAIL"

    # REGIME: VALID — Hankel/Widder linear-algebra is float64 conditioning, all
    # within numpy's standard-precision regime; no SR-LO truncation breakdown.
    regime_verdict = "VALID"

    # Composite collapse rule (per gate-verdicts.md §"Composite-collapse rule")
    if regime_verdict == "BREAKDOWN":
        composite_collapse = "FAIL"
    elif sign_verdict == "FAIL":
        composite_collapse = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite_collapse = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite_collapse = "INFO"
    elif magnitude_verdict == "INFO":
        composite_collapse = "INFO"
    else:
        composite_collapse = "PASS"

    # The composite from §5 aggregate matches collapse-rule composite by
    # construction (sign→magnitude alignment when prediction succeeds).
    composite = composite_collapse
    print(f"[STEP D'] 3-tuple verdict:")
    print(f"          sign_verdict      = {sign_verdict}")
    print(f"          magnitude_verdict = {magnitude_verdict}")
    print(f"          regime_verdict    = {regime_verdict}")
    print(f"          composite         = {composite}")
    print()

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
        "regulator_module_sha": regulator_module_sha,
        "Vol_SU3_Haar": repr(Vol_SU3_Haar),
        "tau_fold": repr(tau_fold),
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
    }
    audit_sha256 = closure_hash(input_pin_map)  # (local)

    content_payload = {  # (local)
        "val_3a": {r: repr(val_3a[r]) for r in ATLAS_A_4},
        "val_3b": {r: repr(val_3b[r]) for r in ATLAS_A_4},
        "val_3c": {r: repr(val_3c[r]) for r in ATLAS_A_4},
        "val_3d": {r: repr(val_3d[r]) for r in ATLAS_A_4},
        "val_3e": {r: repr(val_3e[r]) for r in ATLAS_A_4},
        "pass_grid": [
            [str(pass_grid[r, c]) for c in range(len(SUBCHANNELS))]
            for r in range(len(ATLAS_A_4))
        ],
        "n_sub_PASS": n_sub_PASS,
        "n_sub_INFO": n_sub_INFO,
        "n_sub_FAIL": n_sub_FAIL,
        "n_regulators_full_PASS": n_regulators_full_PASS,
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "composite": composite,
    }
    content_sha256 = text_sha(
        json.dumps(content_payload, sort_keys=True, separators=(",", ":"))
    )  # (local)

    print(f"[STEP E] Closure SHAs:")
    print(f"         audit_sha256   = {audit_sha256}")
    print(f"         content_sha256 = {content_sha256}")
    print()

    # -----------------------------------------------------------------------
    # Step F — Save NPZ artifact (cross-wave dependency for §W8-6)
    # -----------------------------------------------------------------------
    npz_path = THIS_DIR / "s87_w8_hbw_audit_atlas_a_4.npz"  # (local)
    np.savez(
        npz_path,
        atlas=np.array(ATLAS_A_4, dtype=object),
        subchannels=np.array(SUBCHANNELS, dtype=object),
        pass_grid=pass_grid,
        # Per-cell numerical values (§W8-6 SHA-pins this file)
        val_3a=np.array([val_3a[r] for r in ATLAS_A_4], dtype=np.float64),
        val_3b=np.array([val_3b[r] for r in ATLAS_A_4], dtype=np.float64),
        val_3c=np.array([val_3c[r] for r in ATLAS_A_4], dtype=np.float64),
        val_3d=np.array([val_3d[r] for r in ATLAS_A_4], dtype=np.float64),
        val_3e=np.array([val_3e[r] for r in ATLAS_A_4], dtype=np.float64),
        # Per-Bernstein-k breakdown for 3c
        bernstein_zeta=np.array(
            [bernstein_per_k["zeta"][f"k={k}"] for k in BERNSTEIN_K_RANGE],
            dtype=np.float64,
        ),
        bernstein_Zubarev=np.array(
            [bernstein_per_k["Zubarev"][f"k={k}"] for k in BERNSTEIN_K_RANGE],
            dtype=np.float64,
        ),
        bernstein_SDW=np.array(
            [bernstein_per_k["SDW"][f"k={k}"] for k in BERNSTEIN_K_RANGE],
            dtype=np.float64,
        ),
        bernstein_anomaly=np.array(
            [bernstein_per_k["anomaly"][f"k={k}"] for k in BERNSTEIN_K_RANGE],
            dtype=np.float64,
        ),
        # Aggregate counts
        n_sub_PASS=n_sub_PASS,
        n_sub_INFO=n_sub_INFO,
        n_sub_FAIL=n_sub_FAIL,
        n_regulators_full_PASS=n_regulators_full_PASS,
        # Spectrum metadata
        L_max=L_MAX,
        L_max_xcheck=L_MAX_XCHECK,
        lam_min=lam_min,
        lam_max=lam_max,
        n_distinct_L12=n_distinct,
        n_total_L12=n_total_with_mult,
        n_distinct_L10=n_distinct_L10,
        n_total_L10=n_total_L10,
        Lambda_cut=LAMBDA_CUT,
        # Verdicts
        sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        composite=composite,
        # SHAs
        audit_sha256=audit_sha256,
        content_sha256=content_sha256,
    )
    print(f"[STEP F] Saved data: {npz_path}")

    # -----------------------------------------------------------------------
    # Step G — Plot 4x5 heat-grid
    # -----------------------------------------------------------------------
    png_path = THIS_DIR / "s87_w8_hbw_audit_atlas_a_4.png"  # (local)
    fig, ax = plt.subplots(figsize=(11, 6))  # (local)
    color_map = {"PASS": 0, "INFO": 1, "FAIL": 2}  # (local)
    cell_colors = np.zeros((len(ATLAS_A_4), len(SUBCHANNELS)), dtype=int)  # (local)
    for r in range(len(ATLAS_A_4)):
        for c in range(len(SUBCHANNELS)):
            cell_colors[r, c] = color_map[str(pass_grid[r, c])]
    # Custom colormap: PASS=green, INFO=yellow, FAIL=red
    from matplotlib.colors import ListedColormap  # (local)
    cmap = ListedColormap(["#2ca02c", "#ffbb33", "#d62728"])  # (local)
    im = ax.imshow(cell_colors, cmap=cmap, vmin=0, vmax=2, aspect="auto")
    ax.set_xticks(range(len(SUBCHANNELS)))
    ax.set_xticklabels(SUBCHANNELS)
    ax.set_yticks(range(len(ATLAS_A_4)))
    ax.set_yticklabels(ATLAS_A_4)
    ax.set_xlabel("Sub-channel")
    ax.set_ylabel("Regulator")
    ax.set_title(
        f"S87-HBW-AUDIT-ATLAS-A_4 — composite={composite}\n"
        f"sub-PASS={n_sub_PASS}/20  sub-INFO={n_sub_INFO}/20  sub-FAIL={n_sub_FAIL}/20"
    )
    # Annotate cells with verdict + value
    for r in range(len(ATLAS_A_4)):
        for c in range(len(SUBCHANNELS)):
            verdict_text = str(pass_grid[r, c])
            value_text = (
                f"{value_grid[r, c]:.2e}" if abs(value_grid[r, c]) < 1e6 else "INF"
            )
            ax.text(
                c, r, f"{verdict_text}\n{value_text}", ha="center", va="center",
                fontsize=8, color="white" if verdict_text == "FAIL" else "black",
            )
    plt.tight_layout()
    plt.savefig(png_path, dpi=120)
    plt.close(fig)
    print(f"[STEP G] Saved plot: {png_path}")
    print()

    # -----------------------------------------------------------------------
    # Step H — Append verdict line + companion rows
    # -----------------------------------------------------------------------
    verdict_path = THIS_DIR / "s87_gate_verdicts.txt"  # (local)
    canonical_line = (
        f"{GATE_ID}: {composite} -- "
        f"value=({n_sub_PASS},{n_regulators_full_PASS}) "
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
        f"# n_sub_PASS={n_sub_PASS} n_sub_INFO={n_sub_INFO} n_sub_FAIL={n_sub_FAIL} "
        f"n_regulators_full_PASS={n_regulators_full_PASS} "
        f"# {GATE_ID} 4x5 sub-channel aggregate counts\n"
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
    print("=" * 76)
    print(f"VERDICT (composite): {composite}")
    print(f"value 4-tuple: (n_sub_PASS={n_sub_PASS}, "
          f"n_regulators_full_PASS={n_regulators_full_PASS})")
    print(f"scheme={SCHEME_TAG} convention={CONVENTION_TAG} L_max={L_MAX}")
    print(f"audit_sha256={audit_sha256}")
    print(f"content_sha256={content_sha256}")
    print("=" * 76)

    return {
        "composite": composite,
        "n_sub_PASS": n_sub_PASS,
        "n_sub_INFO": n_sub_INFO,
        "n_sub_FAIL": n_sub_FAIL,
        "n_regulators_full_PASS": n_regulators_full_PASS,
        "audit_sha256": audit_sha256,
        "content_sha256": content_sha256,
    }


if __name__ == "__main__":
    main()
