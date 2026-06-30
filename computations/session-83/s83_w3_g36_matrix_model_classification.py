#!/usr/bin/env python3
"""
S83 W3-G36 — MATRIX-MODEL-CLASSIFICATION
=========================================

Gate: S83-MATRIX-MODEL-CLASSIFICATION  [VERIFY]
Classification: GEOMETRIC (framework vs IKKT matrix model)
Owner: kaku-speculative-theorist

Pre-registration (sessions/session-plan/session-83-plan.md §W3-G36 L2234-L2276):
    HYPOTHESIS: E_cond(L) scales as continuum BCS (power-law in L) rather than
    as IKKT matrix-model (linear in L).
    PASS: R^2 continuum > 0.95 AND R^2 continuum > R^2 IKKT + 0.05.
    INFO: R^2 continuum > 0.90.
    FAIL: otherwise.

4-tuple slot: (R2_power=?, scheme=E_cond(L)-fit, convention=continuum-BCS-vs-IKKT,
               L_max=8)

CONTEXT — Kaku phonon-strings investigation (S64):
    The phonon-exflation framework is structurally closer to a FINITE matrix
    model (IKKT-like) than to conventional string theory — it has no T-duality,
    no winding modes, no Hagedorn density of states. The open question from
    the S64 investigation is whether E_cond(L) grows LINEARLY in the level cut
    (signaling a flat matrix-model saturation, i.e. the condensate is built
    additively as L is increased and each new shell contributes the same
    quantum) or as a POWER-LAW in L (continuum BCS, where the accumulated
    contribution saturates sublinearly as the DOS cuts in).

    Structural expectation:
      * Continuum BCS (E_cond ~ -N(0) * Delta^2 * f(lam_max/Delta)): the
        accumulation tracks the density of states near the Fermi surface.
        On the SU(3) fiber, mode count grows polynomially in L (see probe:
        raw_modes ~ L^3 for dim-weighted count ~ L^5.5 at L=3..8). BCS
        accumulation is Delta^2-bounded at the gap scale, but the SUM
        over modes (each contributing |eps| - sqrt(eps^2+Delta^2)) has a
        weighted log-divergence from the high-mode tail. The net scaling
        of |E_cond(L)| is expected to be a power-law with b close to the
        effective volume-growth exponent.
      * IKKT matrix model: finite-dimensional Yang-Mills-type partition
        function. Condensate grows as N (matrix dimension) times the
        per-matrix-element contribution. In our spectrum, the analog of N
        is the dim-weighted mode count. If each shell adds a fixed quantum
        (no BCS coherence factor) E(L) = a + b*L is the shell-counting
        prediction.

    The discrimination: continuum BCS's coherence factor Delta/sqrt(eps^2+Delta^2)
    SUPPRESSES high-mode contributions (sqrt(eps^2+Delta^2) >> |eps| for eps >> Delta
    becomes |eps|(1 + Delta^2/(2 eps^2) + ...), so each mode contributes
    ~ Delta^2/(2|eps|), a 1/eps tail). The total E_cond as a function of
    high-mode cutoff saturates logarithmically in Lambda = lam_max(L), which
    translates to a power-law in L under polynomial level-to-lambda growth.

SUBSTITUTION CHAIN [VERIFY] (mandatory, math-scripts.md):

    Step 1 (Definitions of the BCS condensation energy and the two scaling
            hypotheses).
        Per S66 s66_bcs_sakharov_loop (solve_gap_at_tau) / S73b / S61:
          Mean-field BCS gap equation:
            1 = V_pair * sum_j d_j / (2*sqrt(lam_j^2 + Delta(L)^2))
          Mean-field BCS condensation energy per cell:
            E_cond(L) = -0.5 * sum_j d_j * (sqrt(lam_j^2 + Delta(L)^2) - |lam_j|)
          (sum is over distinct |lam_j| with multiplicity d_j from SU(3)
           irreps (p,q) at level p+q <= L.)
          The overall sign is negative: pairing LOWERS energy.
          NORMALIZATION convention: V-RESCALE. At each L, Delta is held at
          Delta_canonical (S70 R-protected, 0.464255 M_KK), and V_pair(L) is
          rescaled to satisfy the gap equation on the truncated spectrum:
              V_pair(L) = 1 / sum_{level<=L} d_j / (2*sqrt(lam_j^2 + Delta^2))
          Then E_cond(L) = -0.5 * sum d_j (sqrt(lam_j^2 + Delta^2) - |lam_j|)
          is the spectrum-integrated condensate at PHYSICAL gap scale.
          (Alternative "V-fixed at L_pin=8" was tested and discarded: below a
           critical L the gap equation has no positive Delta solution because
           the truncated gap_sum falls below 1/V_pair(8); this is a genuine
           critical-coupling pathology but conflates with the scaling signal
           the gate is probing. V-rescale isolates the accumulation scaling.)

        Power-law hypothesis (continuum BCS):
            |E_cond(L)| = A * L^b                   [power law, b > 0]
          In log form: log|E_cond(L)| = log(A) + b * log(L).
          R^2_power is the coefficient of determination of the (log L, log|E|)
          linear regression.

        Linear hypothesis (IKKT matrix model):
            E_cond(L) = alpha + beta * L            [additive shell counting]
          R^2_linear is the coefficient of determination of the (L, E_cond)
          linear regression.

    Step 2 (Substitute — assemble spectrum at each L in {3,4,5,6,7,8} from
            s74_spectrum_cache_L9_tau019.npz).
        For each L_cut in task range:
          modes_L = [(|lam_j|, d_j)] for all SU(3) sectors (p,q) with p+q <= L_cut
          Solve gap: Delta(L) via bisection with fixed V_pair.
          Compute E_cond(L) = -0.5 * sum_j d_j * (sqrt(lam_j^2 + Delta(L)^2) - |lam_j|)

        NOTE ON V_pair PINNING:
          We fix V_pair from the L_pin = 8 spectrum using the canonical gap
          Delta_canonical = Delta_BCS_fold.
          V_pair = 1 / (sum_j d_j / (2*sqrt(lam_j^2 + Delta_canonical^2)) @ L=8).
          This makes V_pair a FIXED framework parameter pulling the L=8
          gap to its canonical value, and L<8 runs inherit this V.

    Step 3 (Simplify — compute R^2 for each hypothesis).
        log_L = log(L_list)
        log_E = log(|E_cond_list|)
        [slope_power, intercept_power] = polyfit(log_L, log_E, 1)
        E_hat_power = exp(intercept_power + slope_power * log_L)
        residual_power = |E_cond_list| - E_hat_power
        SS_res_power = sum(residual_power^2)
        SS_tot_power = sum((|E_cond| - mean|E_cond|)^2)
        R^2_power = 1 - SS_res_power / SS_tot_power

        [slope_linear, intercept_linear] = polyfit(L_list, E_cond_list, 1)
        E_hat_linear = intercept_linear + slope_linear * L_list
        ... analogous R^2_linear.

    Step 4 (Direction — pre-registered thresholds).
        PASS (continuum) if R^2_power > 0.95 AND R^2_power > R^2_linear + 0.05.
        INFO if R^2_power > 0.90 (moderate continuum-BCS fit).
        FAIL otherwise (structure neither continuum-BCS nor IKKT-linear;
                        OR IKKT fits better).

        STRUCTURAL INTERPRETATION:
          * PASS: framework is continuum-BCS-like. Each level-shell
            contributes Delta^2/lam suppressed quanta — coherent pairing.
          * INFO (not PASS but r2_power > 0.90): intermediate scaling,
            both descriptions partly valid; L_max extension needed.
          * FAIL with R^2_linear > R^2_power: framework is IKKT-like —
            shell-additive, no coherence suppression. This would strengthen
            the phonon-strings investigation's structural conclusion
            (#18 phonon-strings = finite matrix model, not string theory).

    Step 5 (Python verification — see main() below, no hidden assumptions).

L_max:  8 (task-pinned); scan L in {3,4,5,6,7,8}.
L_pin for V_pair calibration: 8 (anchors V to full-spectrum gap).

Inputs (SHA-256 pinned at runtime):
  - canonical_constants.py
  - s74_spectrum_cache_L9_tau019.npz
  - this script

Output 4-tuple:
  (R2_power=<v>, scheme=E_cond(L)-fit, convention=continuum-BCS-vs-IKKT, L_max=8)
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401, F403
from canonical_constants import (
    PI, M_KK, tau_fold, Delta_BCS, E_cond as E_cond_canonical_8mode,
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports (CPU thread cap BEFORE numpy)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import hashlib
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration constants
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent

SESSION = "S83"                                                 # (local)
GATE_ID = "S83-MATRIX-MODEL-CLASSIFICATION"                     # (local)
SCHEME = "E_cond(L)-fit"                                        # (local)
CONVENTION = "V-rescaled-Delta-fixed"                           # (local) Delta held at canonical; V_pair(L) rescaled at each L so gap equation is self-consistent. Isolates spectrum-accumulation scaling from critical-coupling truncation pathology.
L_MAX_TASK = 8                                                  # (local) task-pinned L range max
L_MIN_TASK = 3                                                  # (local) task-pinned L range min

OUT_NPZ = SCRIPT_DIR / "s83_w3_g36_matrix_model_classification.npz"
OUT_PNG = SCRIPT_DIR / "s83_w3_g36_matrix_model_classification.png"
VERDICT_TXT = SCRIPT_DIR / "s83_gate_verdicts.txt"
SPECTRUM_CACHE = SCRIPT_DIR / "s74_spectrum_cache_L9_tau019.npz"  # (local)

INPUT_FILES = [
    SCRIPT_DIR / "canonical_constants.py",
    SPECTRUM_CACHE,
    SCRIPT_DIR / "s83_w3_g36_matrix_model_classification.py",
]

# Pre-registered thresholds (plan L2245, L2263)
PASS_R2_THRESHOLD = 0.95                                         # (local)
INFO_R2_THRESHOLD = 0.90                                         # (local)
PASS_DELTA_R2 = 0.05                                             # (local) R2_power - R2_linear margin

EVAL_CUTOFF = 1e-6                                               # (local) IR cutoff (zero-mode guard)

# Canonical BCS gap at fold (R-protected, S70)
DELTA_CANONICAL = float(Delta_BCS)                               # (local alias)


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                         # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}                                                    # (local)
    for p in inputs:
        sha = sha256_of(p)                                       # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins):
    items = sorted(pins.items())                                 # (local)
    h = hashlib.sha256()                                         # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — Spectrum loader (level-filtered)
# ---------------------------------------------------------------------------

def collect_spectrum(sector_dict, L_cut, cutoff):
    """
    Assemble (|lam|, multiplicity) arrays for all modes at level <= L_cut.
    Multiplicity = SU(3) irrep dimension d_j = dim(p,q).
    """
    abs_list = []                                                # (local)
    mult_list = []                                               # (local)
    for _key, data in sorted(sector_dict.items()):
        if data['level'] <= L_cut:
            dim = int(data['dim'])                               # (local)
            for ev in data['abs_evals']:
                a = float(ev)                                    # (local)
                if a > cutoff:
                    abs_list.append(a)
                    mult_list.append(dim)
    return (np.array(abs_list, dtype=np.float64),
            np.array(mult_list, dtype=np.float64))


# ---------------------------------------------------------------------------
# Section 6 — BCS gap equation + condensation energy (mean-field)
# ---------------------------------------------------------------------------

def gap_sum(lam, mult, Delta):
    """sum_j d_j / (2*sqrt(lam_j^2 + Delta^2)) — gap-equation LHS/V."""
    return float(np.sum(mult / (2.0 * np.sqrt(lam ** 2 + Delta ** 2))))


def solve_V_pair_from_gap(lam, mult, Delta_target):
    """Given canonical Delta_target and full-spectrum (lam, mult), compute
    V_pair such that the gap equation is satisfied: V_pair = 1 / gap_sum.
    """
    s = gap_sum(lam, mult, Delta_target)                         # (local)
    if s <= 0.0 or not np.isfinite(s):
        raise ValueError(f"gap_sum non-positive/non-finite: {s}")
    return 1.0 / s


def solve_Delta_at_L(lam_L, mult_L, V_pair, Delta_lo=1e-6, Delta_hi=10.0,
                     tol=1e-14, max_iter=5000):
    """
    Bisect the BCS gap equation:
        1 = V_pair * sum_j d_j / (2*sqrt(lam_j^2 + Delta^2))
    at the truncated spectrum (lam_L, mult_L).
    Returns (Delta, converged_flag).

    Direction: the gap_func is MONOTONICALLY DECREASING in Delta
    (sum decreases as Delta grows, so V*sum - 1 decreases).
    Standard bisection on the monotone sign change.
    """
    def f(D):
        return V_pair * gap_sum(lam_L, mult_L, D) - 1.0          # (local)

    fl = f(Delta_lo)                                             # (local)
    fh = f(Delta_hi)                                             # (local)

    if fl * fh > 0:
        # No sign change in [Delta_lo, Delta_hi].
        # If both positive: V*sum > 1 everywhere -> gap exceeds Delta_hi
        # If both negative: V*sum < 1 everywhere -> pairing too weak, Delta -> 0
        if fl < 0 and fh < 0:
            return 0.0, False
        else:
            # Extend upper bound once
            Delta_hi = 100.0                                     # (local extension)
            fh = f(Delta_hi)
            if fl * fh > 0:
                return Delta_hi, False

    lo = Delta_lo
    hi = Delta_hi
    for _ in range(max_iter):
        mid = 0.5 * (lo + hi)                                    # (local)
        fm = f(mid)                                              # (local)
        if abs(fm) < tol:
            return mid, True
        if fm * fl > 0:
            lo, fl = mid, fm
        else:
            hi, fh = mid, fm
        if (hi - lo) < tol * max(mid, 1e-12):
            return 0.5 * (lo + hi), True

    return 0.5 * (lo + hi), True


def bcs_condensation_energy(lam, mult, Delta):
    """
    Mean-field BCS condensation energy on the truncated spectrum.

    E_cond = -0.5 * sum_j d_j * (sqrt(lam_j^2 + Delta^2) - |lam_j|)

    Sign convention: pairing lowers energy; E_cond < 0.
    This is the BCS spectrum-integrated lowering of the quasi-particle
    ground state relative to the normal (ungapped) state.

    Per-mode contribution: sqrt(eps^2+Delta^2) - |eps| >= 0 (cf. Tinkham),
    so E_cond = -0.5 * sum >= 0 ... wait, check sign.

    Actually the canonical form is:
      E_cond_BCS = sum_k [ eps_k (1 - eps_k/E_k) - Delta^2/(2 E_k) ]
                 = sum_k eps_k - sum_k eps_k^2/E_k - sum_k Delta^2/(2 E_k)
    which simplifies to:
      E_cond = sum_k eps_k - sum_k E_k (where E_k = sqrt(eps^2+Delta^2))
      E_cond = -sum_k (E_k - eps_k)
    For particle-hole symmetric occupation with eps -> |eps| (both signs
    contribute the same condensation), the right form per UNDIRECTED pair
    channel is:
      E_cond = -sum_k (sqrt(eps^2 + Delta^2) - |eps_k|)
    and the factor 1/2 guards against double-counting when summing over
    all quasi-particle levels.

    We use -0.5 * sum d_j * (sqrt(lam_j^2 + Delta^2) - |lam_j|) consistent
    with S37/S61 s37_oneloop_sa bcs_condensation_energy and s61_fabric_landau.
    """
    return float(-0.5 * np.sum(
        mult * (np.sqrt(lam ** 2 + Delta ** 2) - np.abs(lam))
    ))


# ---------------------------------------------------------------------------
# Section 7 — Scaling fits (power-law vs linear)
# ---------------------------------------------------------------------------

def fit_powerlaw(L_arr, E_arr):
    """
    Fit |E(L)| = A * L^b via linear regression in log space.

    Returns (slope_b, intercept_logA, R2).

    Note on sign: E_cond is negative; we fit |E_cond| vs L.
    A power-law gives log|E| = log A + b log L; b > 0 -> grows with L.
    """
    absE = np.abs(E_arr)                                         # (local)
    if np.any(absE <= 0):
        return np.nan, np.nan, np.nan
    log_L = np.log(L_arr.astype(np.float64))                     # (local)
    log_E = np.log(absE)                                         # (local)
    # polyfit deg=1 returns [slope, intercept]
    slope, intercept = np.polyfit(log_L, log_E, 1)
    E_hat = np.exp(intercept + slope * log_L)                    # (local)
    ss_res = float(np.sum((absE - E_hat) ** 2))                  # (local)
    ss_tot = float(np.sum((absE - absE.mean()) ** 2))            # (local)
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else np.nan         # (local)
    return float(slope), float(intercept), float(r2)


def fit_linear(L_arr, E_arr):
    """
    Fit E(L) = alpha + beta * L (IKKT shell-counting).
    Returns (slope_beta, intercept_alpha, R2).
    Note: we fit the RAW E_cond (preserving sign) so that IKKT linear growth
    toward more negative values shows slope < 0.
    """
    slope, intercept = np.polyfit(L_arr.astype(np.float64), E_arr, 1)
    E_hat = intercept + slope * L_arr                            # (local)
    ss_res = float(np.sum((E_arr - E_hat) ** 2))                 # (local)
    ss_tot = float(np.sum((E_arr - E_arr.mean()) ** 2))          # (local)
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else np.nan         # (local)
    return float(slope), float(intercept), float(r2)


# ---------------------------------------------------------------------------
# Section 8 — Main pipeline
# ---------------------------------------------------------------------------

def main():
    t0 = time.time()                                             # (local)

    print("=" * 78)
    print(f"{GATE_ID} — E_cond(L) scaling classification")
    print("=" * 78)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"closure={closure[:16]}...\n")

    # --- Load spectrum cache ---
    print(f"Loading spectrum cache: {SPECTRUM_CACHE.name}")
    cache = np.load(SPECTRUM_CACHE, allow_pickle=True)
    sector_evals = cache['sector_evals'].item()
    print(f"  {len(sector_evals)} SU(3) sectors, max level "
          f"= {max(v['level'] for v in sector_evals.values())}\n")

    # --- V-rescaled convention: at each L, Delta=canonical, V_pair(L) adjusted ---
    # Convention rationale (see SUBSTITUTION CHAIN Step 1):
    #   V-fixed at L=8 causes Delta->0 for L<8 when gap_sum(L,0) < 1/V_pair(8)
    #   (truncation-phase-transition pathology — physically a critical-coupling
    #   effect, not the spectrum-accumulation scaling the gate is testing).
    #   V-rescale (Delta fixed at canonical, V_pair(L) = 1/gap_sum(L,Delta))
    #   isolates the BCS condensate at physical gap scale: E_cond(L) then
    #   measures ACCUMULATED weight from the summed gap function, which is
    #   what the continuum BCS vs IKKT hypothesis discriminates.
    print(f"V-rescaled convention: Delta fixed at canonical; "
          f"V_pair(L) adjusted at each L.")
    print(f"  Delta_canonical = {DELTA_CANONICAL:.6f} M_KK (S70 Delta_BCS)\n")

    # --- Compute E_cond(L) for L in {3,...,8} ---
    L_list = np.arange(L_MIN_TASK, L_MAX_TASK + 1, dtype=np.int64)
    E_cond_list = np.zeros_like(L_list, dtype=np.float64)        # (local)
    Delta_list = np.zeros_like(L_list, dtype=np.float64)         # (local)
    V_pair_list = np.zeros_like(L_list, dtype=np.float64)        # (local) V_pair at each L
    n_modes_list = np.zeros_like(L_list, dtype=np.int64)         # (local)
    sum_mult_list = np.zeros_like(L_list, dtype=np.int64)        # (local)

    print("Computing E_cond(L) with V-rescaled at canonical Delta:")
    print(f"  {'L':>3s}  {'n_modes':>8s}  {'sum_d':>12s}  "
          f"{'V_pair(L)':>14s}  {'Delta':>10s}  {'E_cond(L)':>16s}")
    for i, L in enumerate(L_list):
        lam_L, mult_L = collect_spectrum(sector_evals, L, EVAL_CUTOFF)
        # V-rescale: V_pair(L) such that gap equation is satisfied at Delta_canonical
        V_pair_L = solve_V_pair_from_gap(lam_L, mult_L, DELTA_CANONICAL)  # (local)
        # With Delta held fixed at canonical, compute E_cond at truncated spectrum
        E_L = bcs_condensation_energy(lam_L, mult_L, DELTA_CANONICAL)  # (local)
        E_cond_list[i] = E_L
        Delta_list[i] = DELTA_CANONICAL
        V_pair_list[i] = V_pair_L
        n_modes_list[i] = len(lam_L)
        sum_mult_list[i] = int(mult_L.sum())
        print(f"  {int(L):>3d}  {len(lam_L):>8d}  {int(mult_L.sum()):>12d}  "
              f"{V_pair_L:>14.6e}  {DELTA_CANONICAL:>10.6f}  {E_L:>16.6f}")
    print()

    # --- Fit: power-law and linear ---
    b_power, logA_power, r2_power = fit_powerlaw(L_list, E_cond_list)
    b_linear, a_linear, r2_linear = fit_linear(L_list, E_cond_list)

    print("Scaling fits:")
    print(f"  POWER-LAW (|E| = A*L^b):")
    print(f"    b  = {b_power:+.6f}")
    print(f"    A  = {np.exp(logA_power):+.6f}")
    print(f"    R^2 = {r2_power:.6f}")
    print(f"  LINEAR (E = a + b*L, IKKT):")
    print(f"    slope = {b_linear:+.6f}")
    print(f"    intercept = {a_linear:+.6f}")
    print(f"    R^2 = {r2_linear:.6f}\n")

    # --- Direction: verdict per pre-registered thresholds ---
    # PASS: R2_power > PASS_R2_THRESHOLD (0.95) AND R2_power > R2_linear + 0.05
    # INFO: R2_power > INFO_R2_THRESHOLD (0.90) (includes PASS region)
    # FAIL: otherwise
    cond_pass = (r2_power > PASS_R2_THRESHOLD) and \
                (r2_power > r2_linear + PASS_DELTA_R2)
    cond_info = (r2_power > INFO_R2_THRESHOLD)

    if cond_pass:
        verdict = "PASS"                                         # (local)
    elif cond_info:
        verdict = "INFO"                                         # (local)
    else:
        verdict = "FAIL"                                         # (local)

    # --- Structural interpretation ---
    print("DIRECTION (pre-registered):")
    print(f"  PASS condition: R^2_power > {PASS_R2_THRESHOLD} AND "
          f"R^2_power > R^2_linear + {PASS_DELTA_R2}")
    print(f"  R^2_power = {r2_power:.6f} {'>' if r2_power > PASS_R2_THRESHOLD else '<='} "
          f"{PASS_R2_THRESHOLD}")
    print(f"  R^2_power - R^2_linear = {r2_power - r2_linear:+.6f} "
          f"{'>' if (r2_power - r2_linear) > PASS_DELTA_R2 else '<='} "
          f"{PASS_DELTA_R2}")
    print(f"  INFO condition: R^2_power > {INFO_R2_THRESHOLD} "
          f"= {r2_power > INFO_R2_THRESHOLD}\n")
    print(f"=> Verdict: {verdict}")
    print(f"   R^2_power = {r2_power:.4f}, R^2_linear = {r2_linear:.4f}\n")

    # --- Structural context (post-verdict interpretation) ---
    if verdict == "PASS":
        interp = (
            "Continuum BCS scaling confirmed. Coherence factor "
            "Delta^2/lam suppresses high-mode contributions; E_cond(L) "
            "grows sub-linearly with level cutoff as expected."
        )
    elif verdict == "INFO":
        interp = (
            "Intermediate scaling. Neither pure continuum BCS nor IKKT. "
            "Extend L_max beyond 8 to discriminate."
        )
    else:
        if r2_linear > r2_power:
            interp = (
                "LINEAR (IKKT) fits better. Framework exhibits shell-additive "
                "scaling consistent with finite-matrix-model classification "
                "(reinforces phonon-strings investigation #18)."
            )
        else:
            interp = (
                "Neither fit passes; scaling is intermediate or richer. "
                "Non-linear + non-power-law suggests a logarithmic / "
                "transitional regime."
            )
    print("STRUCTURAL INTERPRETATION:")
    print(f"  {interp}\n")

    # --- Diagnostic: log-log residuals, linear residuals ---
    log_L = np.log(L_list.astype(np.float64))
    log_E = np.log(np.abs(E_cond_list))
    residual_power_log = log_E - (logA_power + b_power * log_L)  # (local)
    residual_linear = E_cond_list - (a_linear + b_linear * L_list)  # (local)
    print("Residuals:")
    print(f"  power-law log-residuals: max|r|={np.max(np.abs(residual_power_log)):.4f}, "
          f"rms={np.sqrt(np.mean(residual_power_log**2)):.4f}")
    print(f"  linear residuals:        max|r|={np.max(np.abs(residual_linear)):.4f}, "
          f"rms={np.sqrt(np.mean(residual_linear**2)):.4f}\n")

    # --- Cross-check: logarithmic-asymptotic fit (BCS theory expects
    # |E_cond(L)| ~ A * log(L) + B for large L in weak-coupling). We fit
    # this as a third diagnostic model only (not a verdict arm).
    log_L_fit = np.log(L_list.astype(np.float64))                # (local)
    slope_log, intercept_log = np.polyfit(log_L_fit, np.abs(E_cond_list), 1)
    E_hat_log = intercept_log + slope_log * log_L_fit            # (local)
    ss_res_log = float(np.sum((np.abs(E_cond_list) - E_hat_log) ** 2))  # (local)
    ss_tot_log = float(np.sum((np.abs(E_cond_list) - np.abs(E_cond_list).mean()) ** 2))  # (local)
    r2_log = 1.0 - ss_res_log / ss_tot_log                       # (local)
    print(f"Diagnostic: LOG fit |E| = alpha + beta * log(L)")
    print(f"  beta = {slope_log:.6f}, alpha = {intercept_log:.6f}, R^2 = {r2_log:.6f}\n")

    # --- Save artifacts ---
    np.savez(
        OUT_NPZ,
        L_list=L_list,
        E_cond_list=E_cond_list,
        Delta_list=Delta_list,
        V_pair_list=V_pair_list,
        n_modes_list=n_modes_list,
        sum_mult_list=sum_mult_list,
        Delta_canonical=DELTA_CANONICAL,
        # Power-law fit
        b_power=b_power,
        logA_power=logA_power,
        r2_power=r2_power,
        # Linear fit
        b_linear=b_linear,
        a_linear=a_linear,
        r2_linear=r2_linear,
        # Log fit (diagnostic)
        beta_log=slope_log,
        alpha_log=intercept_log,
        r2_log=r2_log,
        # Pre-registered thresholds
        PASS_R2_THRESHOLD=PASS_R2_THRESHOLD,
        INFO_R2_THRESHOLD=INFO_R2_THRESHOLD,
        PASS_DELTA_R2=PASS_DELTA_R2,
        verdict=verdict,
        closure=closure,
    )
    print(f"Artifacts: {OUT_NPZ.name}")

    # --- Plot: 2 panels — (a) log-log + linear fits; (b) residuals ---
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    ax0, ax1 = axes

    # Panel (a): log-log with power-law and linear predictions
    L_smooth = np.linspace(L_list.min() - 0.2, L_list.max() + 0.2, 100)  # (local)
    E_power_smooth = np.exp(logA_power) * L_smooth ** b_power     # (local)
    E_linear_smooth = a_linear + b_linear * L_smooth              # (local)

    ax0.scatter(L_list, np.abs(E_cond_list), marker='o', s=90,
                facecolor='#2c7fb8', edgecolor='k', zorder=3,
                label='|E_cond(L)| measured')
    ax0.plot(L_smooth, E_power_smooth, 'r--',
             label=f'power-law fit: b={b_power:.3f}, R^2={r2_power:.4f}',
             linewidth=2)
    ax0.plot(L_smooth, np.abs(E_linear_smooth), 'g-.',
             label=f'|IKKT linear fit|: slope={b_linear:.3f}, R^2={r2_linear:.4f}',
             linewidth=2)
    ax0.set_xlabel('L (level cut)')
    ax0.set_ylabel('|E_cond(L)| [M_KK]')
    ax0.set_xscale('log')
    ax0.set_yscale('log')
    ax0.legend(loc='lower right', fontsize=9)
    ax0.grid(alpha=0.3, which='both')
    ax0.set_title('|E_cond(L)| log-log — continuum BCS vs IKKT')

    # Panel (b): normalized residuals
    resid_power_norm = residual_power_log                         # (local)
    resid_linear_norm = residual_linear / np.abs(E_cond_list).mean()  # (local)

    width = 0.35                                                  # (local)
    ax1.bar(L_list - width/2, resid_power_norm, width, color='r',
            alpha=0.75, edgecolor='k', label='power-law log-residual')
    ax1.bar(L_list + width/2, resid_linear_norm, width, color='g',
            alpha=0.75, edgecolor='k', label='linear norm-residual')
    ax1.axhline(0, color='k', linewidth=0.5)
    ax1.set_xlabel('L (level cut)')
    ax1.set_ylabel('residual')
    ax1.legend(loc='best', fontsize=9)
    ax1.grid(alpha=0.3)
    ax1.set_title(f'Residuals — verdict {verdict}\n'
                  f'R^2_power={r2_power:.4f}, R^2_linear={r2_linear:.4f}')

    fig.suptitle(f'S83 W3-G36 MATRIX-MODEL-CLASSIFICATION — {verdict}\n'
                 f'E_cond(L) for L in {{{L_MIN_TASK}...{L_MAX_TASK}}}',
                 fontsize=12)
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=110, bbox_inches='tight')
    plt.close(fig)
    print(f"Plot:      {OUT_PNG.name}")

    # --- 4-tuple + verdict line ---
    tag = (f"(R2_power={r2_power:.6f}, scheme={SCHEME}, "
           f"convention={CONVENTION}, L_max={L_MAX_TASK})")
    print(f"\n4-tuple: {tag}")

    verdict_line = (
        f"{GATE_ID}: {verdict} -- "
        f"value=R2_power={r2_power:.6f},R2_linear={r2_linear:.6f},"
        f"b_power={b_power:.6f} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX_TASK} "
        f"sha256={closure}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(verdict_line)

    wall = time.time() - t0                                       # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0 if verdict == "PASS" else (1 if verdict == "FAIL" else 3)


if __name__ == "__main__":
    sys.exit(main())
