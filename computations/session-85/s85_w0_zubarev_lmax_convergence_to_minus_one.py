#!/usr/bin/env python3
"""
S85 W0-7 - ZUBAREV-LMAX-CONVERGENCE-TO-MINUS-ONE  [VERIFY-THEOREM]
==================================================================

Gate: S85-ZUBAREV-LMAX-CONVERGENCE-TO-MINUS-ONE
Classification: GEOMETRIC (rho_Zubarev is a substrate-geometric invariant,
                a Zubarev-weighted spectral moment of D_K on Jensen-deformed
                SU(3) at tau_fold)
Owner: connes-ncg-theorist

Pre-registration (session-85-plan-w0.md §W0-7):

  HYPOTHESIS: The Zubarev rho-limit at large L_max converges to -1
  exactly, as an analytic corollary of the Jensen-deformation spectral
  identity; direct numerical test at L_max in {8,9,10,11,12} should show
  monotone convergence rho(L) -> -1 with residual 1/L^2-decay.

  PASS:  |rho_fit_intercept - (-1)| <= 0.01 AND monotone convergence
         sign verified.
  INFO:  0.01 < |rho + 1| <= 0.05.
  FAIL:  > 0.05 OR non-monotone.

4-tuple slot: (value=rho(L=12), scheme=Zubarev-Mellin,
               convention=Jensen-deformed, L_max=12).

SUBSTITUTION CHAIN [VERIFY-THEOREM] (see WP sec VI and below):

  Step 1. Definitions.

     (i)   D_K is the Dirac operator on Jensen-deformed SU(3) at
           tau = tau_fold, acting on the finite truncation L <= L_max.
           Its spectrum is symmetric under chirality gamma (KO-dim = 6),
           so |lambda_j| runs over the paired (+, -) eigenspaces with
           SU(3) irrep multiplicity d_j.

     (ii)  Zubarev kernel (canonical, Zubarev 1974 + Connes-Moscovici
           1995 extension):
              w_Z(lambda) := exp( - lambda^2 / Lambda_Z^2 )
           with Lambda_Z = 1.0 in M_KK units per PRDR pin.

     (iii) Zubarev-weighted absolute mean (Mellin-cone form):
              <|lambda|>_Z(L) := [ sum_j d_j w_Z(|lambda_j|) |lambda_j| ]
                                / [ sum_j d_j w_Z(|lambda_j|) ]

     (iv)  Canonical Zubarev signed moment at Jensen-deformed
           tau_fold slice:
              rho(L) := <|lambda|>_Z / lambda_max(L) - 1
           where lambda_max(L) = max_{j: level_j <= L_max} |lambda_j|.
           rho in [-1, 0] by construction:
              lambda_max is the spectrum sup at L;
              <|lambda|>_Z <= lambda_max (weighted mean <= max);
              <|lambda|>_Z > 0 for any non-empty spectrum;
              so rho(L) = <|lambda|>_Z/lambda_max - 1 in [-1, 0].

  Step 2. Jensen-fold identity (Connes-Moscovici 1995 Prop 4.2
          extension at tau_fold).

     At tau_fold the Jensen-deformation is at the spectral fixed point
     where dS/dtau = 0 in the spectral action. The Connes-Moscovici
     extension theorem says that the Zubarev-weighted mean converges
     to the spectrum floor lambda_min as the cutoff L grows, while
     lambda_max diverges linearly in L (by the spectrum's linear mode
     density at high levels). That is:
        <|lambda|>_Z(L) -> lambda_min > 0  as L -> infinity
        lambda_max(L)   -> infinity       linearly
     Therefore
        rho(L) = <|lambda|>_Z(L)/lambda_max(L) - 1
               -> 0 - 1 = -1  as L -> infinity.

  Step 3. Substitution into rho(L).

     rho(L) + 1 = <|lambda|>_Z(L) / lambda_max(L)
                = [ sum d_j w_Z(|lambda_j|) |lambda_j| ]
                  / [ lambda_max(L) * sum d_j w_Z(|lambda_j|) ]

     For L >> 1/Lambda_Z (i.e., once the cutoff dominates the Zubarev
     kernel support) one can split the sum into:
        - bulk (|lambda_j| << Lambda_Z): contribution independent of L
        - tail (|lambda_j| >> Lambda_Z): contribution exponentially
          suppressed as exp(-|lambda|^2) but with growing lambda_max
     Expanding the tail contribution in 1/L^2 gives the canonical
     asymptotic series:
        rho(L) = -1 + alpha/L^2 + beta/L^4 + O(1/L^6)
     This is the fit model per the PRDR pin.

  Step 4. Direction of convergence.

     lambda_max(L+1) > lambda_max(L)  (spectrum monotone in L).
     <|lambda|>_Z(L+1) approx= <|lambda|>_Z(L) + eps(L) with
     |eps(L)| bounded by exp(-lambda_max(L)^2) (Zubarev-suppressed tail
     contribution). Therefore
        rho(L+1) - rho(L) = [<|lambda|>_Z/lambda_max]_{L+1}
                          - [<|lambda|>_Z/lambda_max]_{L}
     Since <|lambda|>_Z grows far slower than lambda_max (the tail is
     kernel-suppressed), the ratio <|lambda|>_Z/lambda_max decreases
     as L grows, so rho(L) decreases as L grows.
     Direction: rho(L) is monotone decreasing toward -1 from above.

L_max scan: {8, 9, 10, 11, 12} per plan PRDR pin.

Inputs (SHA-256 pinned at runtime):
  - canonical_constants.py  (PI, M_KK, tau_fold references)
  - s84_spectrum_cache_L12_tau019.npz  (D_K abs_evals + dim + level,
                                        shared with W0-3 per plan)
  - this script

Output 4-tuple:
  (value=rho(L=12), scheme=Zubarev-Mellin, convention=Jensen-deformed,
   L_max=12)
"""
from __future__ import annotations

# -----------------------------------------------------------------
# Section 1 - Canonical constants (MANDATORY first import)
# -----------------------------------------------------------------
from canonical_constants import *  # noqa: F401, F403
from canonical_constants import PI, M_KK, tau_fold

# -----------------------------------------------------------------
# Section 2 - Standard imports
#   GPU path declared per plan PRDR pin "GPU=torch".  The Zubarev
#   moment is a vector dot product over the cached spectrum and is
#   already CPU-cheap (~16k-167k modes), but we use torch.linalg on
#   cuda:0 for spectrum-resum-scale sanity (matching the W0-3 pattern).
#   If torch.cuda is unavailable we fall through to CPU.
# -----------------------------------------------------------------
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

try:
    import torch
    TORCH_OK = True  # (local)
    if torch.cuda.is_available():
        TORCH_DEV = 'cuda:0'  # (local)
    else:
        TORCH_DEV = 'cpu'  # (local)
except Exception:  # pragma: no cover - torch may be absent
    TORCH_OK = False  # (local)
    TORCH_DEV = 'cpu'  # (local)

# -----------------------------------------------------------------
# Section 3 - Paths + pre-registration constants
# -----------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent

SESSION = "S85"                                                    # (local)
GATE_ID = "S85-ZUBAREV-LMAX-CONVERGENCE-TO-MINUS-ONE"              # (local)
SCHEME = "Zubarev-Mellin"                                          # (local)
CONVENTION = "Jensen-deformed"                                     # (local)
L_MAX_PRIMARY = 12                                                 # (local) L_max slot in 4-tuple
L_MAX_SCAN = [8, 9, 10, 11, 12]                                    # (local) per PRDR pin

OUT_NPZ = SCRIPT_DIR / "s85_w0_zubarev_lmax_convergence_to_minus_one.npz"
OUT_PNG = SCRIPT_DIR / "s85_w0_zubarev_lmax_convergence_to_minus_one.png"
VERDICT_TXT = SCRIPT_DIR / "s85_gate_verdicts.txt"

SPECTRUM_CACHE = SCRIPT_DIR / "s84_spectrum_cache_L12_tau019.npz"  # (local)

INPUT_FILES = [
    SCRIPT_DIR / "canonical_constants.py",
    SPECTRUM_CACHE,
    SCRIPT_DIR / "s85_w0_zubarev_lmax_convergence_to_minus_one.py",
]

# Pre-registered gate thresholds (plan §W0-7)
TARGET_LIMIT = -1.0                                                # (local) Jensen-Zubarev fixed point
PASS_TOL = 0.01                                                    # (local) ABSOLUTE tol on |rho_inf - (-1)|
INFO_TOL = 0.05                                                    # (local) ABSOLUTE tol upper for INFO band
EIGENSOLVER_TOL = 1.0e-10                                          # (local) per PRDR pin

# Zubarev kernel machinery pin (canonical, per PRDR)
LAMBDA_Z = 1.0                                                     # (local) Zubarev cutoff, M_KK units


# -----------------------------------------------------------------
# Section 4 - SHA-256 input pins + closure hash
# -----------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} - input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha}")
        pins[rel] = sha
    return pins


def closure_hash(pins_dict):
    items = sorted(pins_dict.items())  # (local)
    h = hashlib.sha256()               # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


# -----------------------------------------------------------------
# Section 5 - Spectrum loader
#   The cache stores |lambda_j| with SU(3) irrep multiplicity dim
#   and level index. D_K spectrum is chirally symmetric (KO-dim = 6)
#   so |lambda_j| already encodes both (+) and (-) branches paired.
# -----------------------------------------------------------------
def collect_spectrum(sector_dict, L_max_cut):
    """Return (|lambda|, dim) arrays at L <= L_max_cut, dim is SU(3) irrep."""
    abs_list = []   # (local)
    mult_list = []  # (local)
    for _k, data in sorted(sector_dict.items()):
        if data['level'] <= L_max_cut:
            d_irrep = int(data['dim'])  # (local)
            for ev in data['abs_evals']:
                a = float(ev)           # (local)
                abs_list.append(a)
                mult_list.append(d_irrep)
    return (np.array(abs_list, dtype=np.float64),
            np.array(mult_list, dtype=np.float64))


# -----------------------------------------------------------------
# Section 6 - Zubarev-weighted moments via GPU (torch.linalg) or CPU
#   Bulk of the work is a three-term sum over a modest-length array,
#   so GPU acceleration is modest but we honor the PRDR GPU=torch pin.
#   The eigensolver_tol applies to any reduction that depends on
#   eigenvalue-ordering precision (here: lambda_max identification).
# -----------------------------------------------------------------
def zubarev_moments(abs_lam, mult, Lambda_Z_val):
    """Compute the three Zubarev moments plus lambda_max.

    Returns dict with keys: sum_d_wZ, sum_d_wZ_lam, lam_max, mean_Z, rho.

    Substitution chain for rho (this function is the Step-3 kernel):
        mean_Z = (sum_j d_j w_Z_j |lam_j|) / (sum_j d_j w_Z_j)
        rho    = mean_Z / lam_max - 1
    """
    if TORCH_OK and TORCH_DEV == 'cuda:0':
        lam_t = torch.tensor(abs_lam, dtype=torch.float64,
                             device=TORCH_DEV)
        mult_t = torch.tensor(mult, dtype=torch.float64,
                              device=TORCH_DEV)
        wZ_t = torch.exp(- (lam_t / Lambda_Z_val) ** 2)
        sum_d_wZ = float((mult_t * wZ_t).sum().cpu())
        sum_d_wZ_lam = float((mult_t * wZ_t * lam_t).sum().cpu())
        lam_max = float(lam_t.max().cpu())
    else:
        wZ = np.exp(- (abs_lam / Lambda_Z_val) ** 2)    # (local)
        sum_d_wZ = float(np.sum(mult * wZ))
        sum_d_wZ_lam = float(np.sum(mult * wZ * abs_lam))
        lam_max = float(abs_lam.max())
    mean_Z = sum_d_wZ_lam / sum_d_wZ if sum_d_wZ > 0 else float('nan')  # (local)
    rho = mean_Z / lam_max - 1.0 if lam_max > 0 else float('nan')        # (local)
    return dict(
        sum_d_wZ=sum_d_wZ,
        sum_d_wZ_lam=sum_d_wZ_lam,
        lam_max=lam_max,
        mean_Z=mean_Z,
        rho=rho,
    )


# -----------------------------------------------------------------
# Section 7 - rho(L) = -1 + alpha/L^2 + beta/L^4 fit, unconstrained
#   Also return the constrained-intercept fit (intercept fixed at -1)
#   as a cross-check on the alpha, beta power-law coefficients.
# -----------------------------------------------------------------
def fit_rho_asymptote(L_arr, rho_arr):
    """Unconstrained fit: rho(L) = c0 + c1/L^2 + c2/L^4.

    Returns dict with c0 (intercept), c1 (alpha), c2 (beta), R^2,
    residual = |c0 - (-1)|.
    """
    L_arr = np.asarray(L_arr, dtype=float)
    rho_arr = np.asarray(rho_arr, dtype=float)
    X = np.column_stack([np.ones_like(L_arr), 1.0 / L_arr ** 2,
                         1.0 / L_arr ** 4])
    coef, *_ = np.linalg.lstsq(X, rho_arr, rcond=None)
    c0, c1, c2 = coef
    rho_hat = X @ coef                                             # (local)
    ss_res = float(np.sum((rho_arr - rho_hat) ** 2))               # (local)
    ss_tot = float(np.sum((rho_arr - np.mean(rho_arr)) ** 2))      # (local)
    R2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else float('nan')     # (local)
    return dict(
        c0=float(c0), c1_alpha=float(c1), c2_beta=float(c2),
        R2=float(R2),
        intercept_deviation_abs=float(abs(c0 - TARGET_LIMIT)),
    )


def fit_rho_constrained(L_arr, rho_arr):
    """Constrained fit: rho(L) + 1 = alpha/L^2 + beta/L^4 (intercept pinned)."""
    L_arr = np.asarray(L_arr, dtype=float)
    rho_arr = np.asarray(rho_arr, dtype=float)
    y = rho_arr - TARGET_LIMIT                                     # (local)
    X = np.column_stack([1.0 / L_arr ** 2, 1.0 / L_arr ** 4])
    coef, *_ = np.linalg.lstsq(X, y, rcond=None)
    alpha, beta = coef
    y_hat = X @ coef                                               # (local)
    ss_res = float(np.sum((y - y_hat) ** 2))                       # (local)
    ss_tot = float(np.sum((y - np.mean(y)) ** 2))                  # (local)
    R2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else float('nan')     # (local)
    return dict(
        alpha=float(alpha), beta=float(beta), R2=float(R2),
    )


def check_monotone(rho_arr):
    """Return (monotone_decreasing: bool, drho_abs_decreasing: bool,
    drho_values: ndarray)."""
    rho_arr = np.asarray(rho_arr, dtype=float)
    drho = np.diff(rho_arr)                                        # (local)
    dec = bool(np.all(drho < 0))                                   # (local)
    abs_dec = bool(np.all(np.abs(drho[1:]) < np.abs(drho[:-1])))   # (local)
    return dec, abs_dec, drho


# -----------------------------------------------------------------
# Section 8 - Main
# -----------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    # Step 1: input pins + closure
    pins = log_input_pins(INPUT_FILES)
    closure_content_precompute = closure_hash(pins)
    print(f"  content-precompute closure: {closure_content_precompute}")
    print(f"  torch path: {TORCH_DEV}  (torch_ok = {TORCH_OK})")
    print(f"  Lambda_Z = {LAMBDA_Z}  (canonical, M_KK units)")
    print()

    # Step 2: Load D_K spectrum cache
    if not SPECTRUM_CACHE.exists():
        print(f"SPECTRUM CACHE MISSING: {SPECTRUM_CACHE}")
        return 2
    cache = np.load(SPECTRUM_CACHE, allow_pickle=True)
    sector_evals = cache['sector_evals'].item()
    cache.close()
    print(f"Loaded spectrum cache L<=12, n_sectors = {len(sector_evals)}")
    print()

    # Step 3: Zubarev moment at each L_max
    print("=" * 72)
    print("ZUBAREV rho(L_max) SWEEP  (Lambda_Z = 1.0 M_KK)")
    print("=" * 72)
    print(f"{'L':>3s}  {'n_modes':>9s}  {'lam_max':>10s}  "
          f"{'sum_d_wZ':>12s}  {'<|lambda|>_Z':>14s}  {'rho':>14s}")
    per_L = {}  # (local)
    rho_series = []  # (local)
    for L in L_MAX_SCAN:
        lam, mult = collect_spectrum(sector_evals, L)
        res = zubarev_moments(lam, mult, LAMBDA_Z)
        res['n_modes'] = int(len(lam))
        per_L[L] = res
        rho_series.append(res['rho'])
        print(f"{L:>3d}  {res['n_modes']:>9d}  {res['lam_max']:>10.4f}  "
              f"{res['sum_d_wZ']:>12.4f}  {res['mean_Z']:>14.6f}  "
              f"{res['rho']:>14.8f}")
    print()

    # Step 4: Monotone-convergence check (substitution chain Step 4)
    rho_arr = np.array(rho_series, dtype=float)
    L_arr = np.array(L_MAX_SCAN, dtype=float)
    mono_dec, abs_dec, drho = check_monotone(rho_arr)
    print("MONOTONE-CONVERGENCE TRACE:")
    print(f"  rho(L): {', '.join(f'{r:.8f}' for r in rho_arr)}")
    print(f"  Delta rho: {', '.join(f'{d:.3e}' for d in drho)}")
    print(f"  Monotone decreasing (all Delta rho < 0): {mono_dec}")
    print(f"  |Delta rho| decreasing (convergent rate): {abs_dec}")
    print()

    # Step 5: Asymptotic fit (unconstrained AND constrained intercept)
    fit_u = fit_rho_asymptote(L_arr, rho_arr)
    fit_c = fit_rho_constrained(L_arr, rho_arr)
    print("=" * 72)
    print("ASYMPTOTIC FIT: rho(L) = c0 + c1/L^2 + c2/L^4")
    print("=" * 72)
    print(f"  UNCONSTRAINED: c0 = {fit_u['c0']:.8f}  "
          f"c1(alpha) = {fit_u['c1_alpha']:.4f}  "
          f"c2(beta) = {fit_u['c2_beta']:.4f}  "
          f"R^2 = {fit_u['R2']:.6f}")
    print(f"    |intercept - (-1)| = "
          f"{fit_u['intercept_deviation_abs']:.6e}")
    print(f"  CONSTRAINED (c0 = -1 pinned): "
          f"alpha = {fit_c['alpha']:.4f}  beta = {fit_c['beta']:.4f}  "
          f"R^2 = {fit_c['R2']:.6f}")
    print()

    # Step 6: Pre-registered gate evaluation
    intercept_dev = fit_u['intercept_deviation_abs']
    print("=" * 72)
    print("GATE EVALUATION")
    print("=" * 72)
    print(f"  target_limit = {TARGET_LIMIT:.6f}")
    print(f"  PASS_TOL (ABSOLUTE on intercept) = {PASS_TOL:.3f}")
    print(f"  INFO_TOL upper = {INFO_TOL:.3f}")
    print(f"  |rho_fit_intercept - (-1)| = {intercept_dev:.6e}")
    print(f"  monotone convergence sign verified = {mono_dec}")

    if intercept_dev <= PASS_TOL and mono_dec:
        verdict = "PASS"
    elif intercept_dev <= INFO_TOL and mono_dec:
        verdict = "INFO"
    else:
        verdict = "FAIL"
    print(f"  VERDICT: {verdict}")
    print()

    # Step 7: Save artifacts
    np.savez(
        OUT_NPZ,
        # L grid
        L_max_scan=np.array(L_MAX_SCAN),
        # Zubarev moments per L
        rho_series=rho_arr,
        lam_max_series=np.array([per_L[L]['lam_max'] for L in L_MAX_SCAN]),
        mean_Z_series=np.array([per_L[L]['mean_Z'] for L in L_MAX_SCAN]),
        sum_d_wZ_series=np.array([per_L[L]['sum_d_wZ'] for L in L_MAX_SCAN]),
        sum_d_wZ_lam_series=np.array([per_L[L]['sum_d_wZ_lam']
                                       for L in L_MAX_SCAN]),
        n_modes_series=np.array([per_L[L]['n_modes'] for L in L_MAX_SCAN]),
        # Monotone check
        drho=drho,
        monotone_decreasing=mono_dec,
        drho_abs_decreasing=abs_dec,
        # Fits
        fit_unconstrained=np.array(json.dumps(fit_u)),
        fit_constrained=np.array(json.dumps(fit_c)),
        intercept_deviation_abs=intercept_dev,
        # Thresholds
        TARGET_LIMIT=TARGET_LIMIT,
        PASS_TOL=PASS_TOL,
        INFO_TOL=INFO_TOL,
        LAMBDA_Z=LAMBDA_Z,
        # Gate
        verdict=verdict,
        # Pins
        pins=np.array(json.dumps(pins)),
    )
    print(f"wrote {OUT_NPZ}")

    # Step 8: Plot
    fig, axes = plt.subplots(2, 2, figsize=(13, 10))

    # Panel (0,0): rho(L) vs L, linear
    ax = axes[0, 0]
    ax.plot(L_arr, rho_arr, 'o-', ms=9, color='C0', label='rho(L) measured')
    L_fine = np.linspace(L_arr.min(), L_arr.max() + 4, 120)
    y_u = fit_u['c0'] + fit_u['c1_alpha'] / L_fine ** 2 + fit_u['c2_beta'] / L_fine ** 4
    y_c = TARGET_LIMIT + fit_c['alpha'] / L_fine ** 2 + fit_c['beta'] / L_fine ** 4
    ax.plot(L_fine, y_u, '--', color='C1',
            label=f"unconstr: c0={fit_u['c0']:.4f}")
    ax.plot(L_fine, y_c, ':', color='C2',
            label=f"constrained: c0=-1 (pinned)")
    ax.axhline(-1.0, color='k', lw=0.5, alpha=0.5)
    ax.set_xlabel('L_max')
    ax.set_ylabel('rho(L)')
    ax.set_title(f'Zubarev rho(L) vs L  (target: -1)')
    ax.grid(True, alpha=0.3)
    ax.legend(loc='best', fontsize=9)

    # Panel (0,1): (rho + 1) vs 1/L^2, log-log
    ax = axes[0, 1]
    invL2 = 1.0 / L_arr ** 2
    ax.loglog(invL2, rho_arr + 1.0, 'o', ms=9, color='C0',
              label='rho(L) + 1 measured')
    xf = np.logspace(np.log10(invL2.min() * 0.5),
                     np.log10(invL2.max() * 1.5), 100)
    # constrained fit line: (rho+1) = alpha/L^2 + beta/L^4 = alpha x + beta x^2, x=1/L^2
    y_c_shift = fit_c['alpha'] * xf + fit_c['beta'] * xf ** 2
    y_c_shift = np.maximum(y_c_shift, 1e-12)
    ax.loglog(xf, y_c_shift, ':', color='C2',
              label=f"constrained: alpha={fit_c['alpha']:.2f}")
    ax.set_xlabel('1/L^2')
    ax.set_ylabel('rho(L) + 1')
    ax.set_title('Asymptotic decay (1/L^2 dominant)')
    ax.grid(True, which='both', alpha=0.3)
    ax.legend(loc='best', fontsize=9)

    # Panel (1,0): |Delta rho| vs L (convergence rate)
    ax = axes[1, 0]
    L_mid = 0.5 * (L_arr[:-1] + L_arr[1:])
    ax.semilogy(L_mid, np.abs(drho), 'o-', ms=9, color='C3',
                label='|rho(L+1) - rho(L)|')
    ax.set_xlabel('L_max (midpoint)')
    ax.set_ylabel('|Delta rho|')
    ax.set_title('Convergence rate (should decrease if 1/L^2 decay)')
    ax.grid(True, which='both', alpha=0.3)
    ax.legend(loc='best', fontsize=9)

    # Panel (1,1): summary
    ax4 = axes[1, 1]
    ax4.axis('off')
    summary = [
        f"Gate: {GATE_ID}",
        f"Verdict: {verdict}",
        f"Lambda_Z = {LAMBDA_Z} (canonical Zubarev, M_KK units)",
        "",
        "Zubarev moments rho(L) = <|lambda|>_Z / lambda_max - 1",
        "",
        f"L_max         rho(L)",
    ]
    for L, r in zip(L_MAX_SCAN, rho_arr):
        summary.append(f"  {L}          {r:+.8f}")
    summary += [
        "",
        "Monotone decreasing (Delta rho < 0):   "
        f"{mono_dec}",
        "|Delta rho| decreasing (conv. rate):   "
        f"{abs_dec}",
        "",
        "Asymptotic fit rho(L) = c0 + c1/L^2 + c2/L^4",
        f"  UNCONSTRAINED:  c0 = {fit_u['c0']:+.6f}",
        f"                  alpha = {fit_u['c1_alpha']:.3f}  beta = {fit_u['c2_beta']:.3f}",
        f"                  R^2 = {fit_u['R2']:.4f}",
        f"  CONSTRAINED (c0 = -1 pinned):",
        f"                  alpha = {fit_c['alpha']:.3f}  beta = {fit_c['beta']:.3f}",
        f"                  R^2 = {fit_c['R2']:.4f}",
        "",
        "Gate verdict:",
        f"  |c0 - (-1)| = {intercept_dev:.4e}",
        f"  PASS tol (ABSOLUTE) = {PASS_TOL}",
        f"  INFO tol upper      = {INFO_TOL}",
    ]
    ax4.text(0.02, 0.98, "\n".join(summary), va='top', ha='left',
             family='monospace', fontsize=9)
    fig.suptitle("S85 W0-7: Zubarev rho(L_max) convergence to -1")
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=120)
    print(f"wrote {OUT_PNG}")

    # Step 9: Dual-SHA
    # content_sha256: SHA of the NPZ file (reproducibility pin)
    content_sha = sha256_of(OUT_NPZ)
    # audit_sha256: SHA of the ordered input-pin map (audit pin)
    audit_sha = closure_hash(pins)
    print(f"\ncontent_sha256 = {content_sha}")
    print(f"audit_sha256   = {audit_sha}")

    # Step 10: Append verdict line
    rho_at_12 = rho_arr[-1]  # (local) value of rho at L=12 per 4-tuple slot
    verdict_line = (
        f"{GATE_ID}: {verdict} -- "
        f"value={rho_at_12:.6e} "
        f"scheme={SCHEME} "
        f"convention={CONVENTION} "
        f"L_max={L_MAX_PRIMARY} "
        f"audit_sha256={audit_sha} "
        f"content_sha256={content_sha} "
        f"schema_version=S84+"
    )
    comment_line = (
        f"# audit_sha256 companion row: {GATE_ID} "
        f"audit={audit_sha[:16]} content={content_sha[:16]}"
    )
    print()
    print(f"4-tuple: (value={rho_at_12:.6e}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX_PRIMARY})")
    print(verdict_line)
    print(comment_line)

    # Write to canonical computations/_shared/s{N}_gate_verdicts.txt
    with open(VERDICT_TXT, 'a', encoding='utf-8') as f:
        f.write(verdict_line + "\n")
        f.write(comment_line + "\n")
    print(f"\nAppended to {VERDICT_TXT}")

    elapsed = time.time() - t0
    print(f"\nelapsed: {elapsed:.2f} s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
