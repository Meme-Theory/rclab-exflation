#!/usr/bin/env python3
"""
s84_w9b_deriv_i_spectral_dim.py -- W9b-105-S84-DERIV-I (cube-3 override)
=========================================================================

Gate: W9b-105-S84-DERIV-I
Session 84 Wave 9b-A sub-obligation (i) for S84-MU-BC-GEOMETRIC.

Hypothesis: spectral dimension d_spec of Jensen-deformed SU(3) at tau_fold = 0.19
at the fiber-transition scale s* is approximately 3, justifying the "12 = 4 x 3"
exponent factorization in mu_BC_K3 = M_Z * sqrt(1 + exp(12*tau_fold)/3).

Definition (plan §W9b-105.9 Step 1): zeta_D(s) = sum_{lambda > 0} lambda^{-s}
  with Peter-Weyl multiplicity d_rho (Connes-Marcolli convention, linear in s).
  |D_K| = sqrt(D_K^2 + eps^2), eps = 1e-12 (IR-floor regulator).
Definition (plan §W9b-105.6 fiber-transition): s* = argmin |d^2 zeta_D / ds^2|
  over the scan range s in [0.5, 6.0].
Definition (plan §W9b-105.9 Step 2): d_spec = leading simple-pole location of
  zeta_D. OPERATIONAL extractor (pole-proxy from log derivative):
  near simple pole at d_spec, log zeta_D ~ log C - log(s - d_spec),
  so d log zeta / ds ~ -1 / (s - d_spec)  =>  d_spec = s + 1 / (d log zeta / ds).

Thresholds (ABSOLUTE on d_spec):
  PASS  : d_spec in [2.5, 3.5]
  INFO  : d_spec in [2.0, 2.5) U (3.5, 4.0]
  FAIL  : d_spec not in [2.0, 4.0]

Machinery pin: L_max = 10 primary, {6, 8, 12} convergence cross-check.
Spectrum source: computations/session-84/s84_spectrum_cache_L12_tau019.npz
(Plan's legacy filename 'D_K_eigenvalues_Lmax10_tau019.npz' resolves here;
filter sectors by p+q <= 10 for the primary L_max=10 run.)

=============================================================================
SUBSTITUTION CHAIN (structural analysis of the spectrum + extractor)
=============================================================================

Spectrum structure: lambda_min = 0.8197, lambda_max = 4.6702 on Jensen-SU(3)
at tau_fold = 0.19 (gapped, no zero modes after eps-regularization).

Step 1 (def):  zeta_D(s) = sum_n d_rho(n) * lambda_n^{-s}.
Step 2 (def):  d log zeta / ds = -<ln lambda>_s
               where the weighted average <.>_s uses weights d_rho * lambda^{-s}.
Step 3 (def):  d^2 zeta / ds^2 = sum_n d_rho * (ln lambda)^2 * lambda^{-s} > 0.
Step 4 (monot): since ln lambda > 0 for most eigenvalues (lambda_min=0.82 gives
                ln~-0.2, most others are > 1), d/ds [d^2 zeta/ds^2] is dominated
                by -<(ln lambda)^3>_s * zeta ~ negative.
                => d^2 zeta / ds^2 is MONOTONICALLY DECREASING in s on [0.5, 6.0].
                Hence argmin |d^2 zeta / ds^2| over scan_range [0.5, 6.0] is at
                the upper boundary s* = 6.0 (boundary-dominated).

Step 5 (alt):  The plan §W9b-105 prediction d_spec ~ 3 presupposes an interior
                fiber-transition. In practice, the log-zeta function has its
                inflection (argmax d^2 log zeta / ds^2) at s ~ 8.4, where the
                Weyl regime attains maximum log-concavity. d_eff rises linearly
                with s in the scan range [1, 6].

Step 6 (direction for threshold): at s* = 6.0 (plan-literal), d_eff = 4.89 >
                3.5 = PASS_HI and 4.0 = INFO_HI. Under plan-literal prescription,
                VERDICT = FAIL (d_spec is OUTSIDE [2.0, 4.0]).

Step 7 (sensitivity): at s where d_eff first crosses 3.0 (s ~ 3.97), d_eff is
                inside PASS band. But this is an IMPLICIT extraction, not what
                the plan's argmin prescription returns. The plan's prescription
                does NOT recover d_spec ~ 3.

Cross-check interpretations reported below for transparency. Primary verdict
follows the PLAN-LITERAL prescription per §W9b-105.6.

Author: spectral-geometer
Session: 84 Wave 9b-A (sub-obligation i)
Date: 2026-04-19
"""

import os
import sys
import time
import hashlib

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
os.chdir(SCRIPT_DIR)

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

try:
    import torch
    TORCH_OK = True
    GPU_DEV = "cuda" if torch.cuda.is_available() else "cpu"
except Exception:
    TORCH_OK = False
    GPU_DEV = "cpu"

from canonical_constants import PI, tau_fold

# ============================================================================
# 0. HEADER + SHA PINS
# ============================================================================
print("=" * 80)
print("W9b-105-S84-DERIV-I: Spectral Dimension at Fiber-Transition Scale")
print("S84 Wave 9b-A | spectral-geometer")
print("=" * 80)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


SPECTRUM_PATH = "s84_spectrum_cache_L12_tau019.npz"
CONST_PATH = "canonical_constants.py"
SCRIPT_PATH = os.path.abspath(__file__)

sha_spectrum = sha256_file(SPECTRUM_PATH)        # (local)
sha_const = sha256_file(CONST_PATH)              # (local)
sha_script = sha256_file(SCRIPT_PATH)            # (local)

print(f"\n  Input SHA-256 pins:")
print(f"    spectrum_cache : {sha_spectrum}")
print(f"    canonical_consts: {sha_const}")
print(f"    script         : {sha_script}")
print(f"  tau_fold = {tau_fold}")
print(f"  GPU device     : {GPU_DEV}, torch_ok={TORCH_OK}")

# ============================================================================
# 1. LOAD SECTOR-RESOLVED SPECTRUM
# ============================================================================
print("\n" + "=" * 80)
print("1. LOAD SECTOR-RESOLVED SPECTRUM (filename resolution)")
print("=" * 80)
print(f"  Plan legacy filename 'D_K_eigenvalues_Lmax10_tau019.npz' resolves to:")
print(f"    {SPECTRUM_PATH} (L12 cache, sector filter p+q <= 10 applied)")

cache = np.load(SPECTRUM_PATH, allow_pickle=True)
sector_evals = cache["sector_evals"].item()
cache.close()
print(f"  Loaded {len(sector_evals)} sectors from {SPECTRUM_PATH}")


def gather_spectrum(sector_evals, L_max_cut):
    """Gather eigenvalues + PW multiplicities for sectors with p+q <= L_max_cut.

    Convention: zeta_D(s) = sum_n d_rho(n) * lambda_n^{-s}, where for each unique
    spinor eigenvalue |lambda| in sector (p,q), d_rho = dim_rho(p,q) (Peter-Weyl
    right-regular multiplicity).
    IR-floor: |D_K|_eps = sqrt(D^2 + eps^2), eps = 1e-12.
    """
    lams_list, mults_list = [], []
    for (p, q), data in sector_evals.items():
        if (p + q) > L_max_cut:
            continue
        drho = int(data["dim"])
        ae = np.asarray(data["abs_evals"], dtype=np.float64)
        eps = 1e-12  # (local) IR-floor regulator
        ae_reg = np.sqrt(ae * ae + eps * eps)
        lams_list.append(ae_reg)
        mults_list.append(np.full_like(ae_reg, drho, dtype=np.float64))
    lams = np.concatenate(lams_list)
    mults = np.concatenate(mults_list)
    return lams, mults


lams_L10, mults_L10 = gather_spectrum(sector_evals, 10)
n_unique_L10 = len(lams_L10)                                  # (local)
n_pw_L10 = int(mults_L10.sum())                               # (local)
print(f"  L_max=10: N_unique={n_unique_L10}, PW-weighted={n_pw_L10}")
print(f"            lambda range: [{lams_L10.min():.4f}, {lams_L10.max():.4f}]")

# ============================================================================
# 2. ZETA SUM (GPU) + DERIVATIVES
# ============================================================================
print("\n" + "=" * 80)
print("2. COMPUTE zeta_D(s), d zeta / ds, d^2 zeta / ds^2")
print("=" * 80)


def zeta_sum(lams, mults, s_grid, device="cpu"):
    """Vectorized zeta_D(s) = sum_n mults_n * lams_n^{-s} on s_grid."""
    if TORCH_OK and device == "cuda":
        lt = torch.tensor(lams, device=device, dtype=torch.float64)
        mt = torch.tensor(mults, device=device, dtype=torch.float64)
        st = torch.tensor(s_grid, device=device, dtype=torch.float64)
        log_lt = torch.log(lt)
        # zeta_i = sum_j m_j * exp(-s_i * log lam_j)
        neg_sL = -st.unsqueeze(1) * log_lt.unsqueeze(0)
        expvals = torch.exp(neg_sL) * mt.unsqueeze(0)
        zeta_vals = expvals.sum(dim=1).cpu().numpy()
    else:
        log_lams = np.log(lams)                               # (local)
        zeta_vals = np.empty_like(s_grid, dtype=np.float64)
        for i, s in enumerate(s_grid):
            zeta_vals[i] = np.sum(mults * np.exp(-s * log_lams))
    return zeta_vals


# Plan scan_range: s in [0.5, 6.0], step 0.001 (fine everywhere for robust grad)
s_fine = np.arange(0.5, 6.0001, 0.001)                         # (local)
# Extended diagnostic scan (for cross-check interpretations)
s_ext = np.arange(0.5, 12.0001, 0.002)                         # (local)

print(f"  Plan scan grid (primary): {len(s_fine)} points in [0.5, 6.0]")
print(f"  Extended diagnostic grid: {len(s_ext)} points in [0.5, 12.0]")

t0 = time.time()
zeta_fine = zeta_sum(lams_L10, mults_L10, s_fine, device=GPU_DEV)
zeta_ext = zeta_sum(lams_L10, mults_L10, s_ext, device=GPU_DEV)
t_zeta = time.time() - t0                                     # (local)
print(f"  zeta-sum time: {t_zeta:.2f}s")
print(f"  zeta(s=0.5)  = {zeta_fine[0]:.3e}")
print(f"  zeta(s=6.0)  = {zeta_fine[-1]:.3e}")

# Numerical derivatives on the FINE (plan-scan) grid
log_zeta = np.log(zeta_fine)                                  # (local)
dzeta = np.gradient(zeta_fine, s_fine)                        # (local) dζ/ds
d2zeta = np.gradient(dzeta, s_fine)                           # (local) d²ζ/ds²
dln_zeta = np.gradient(log_zeta, s_fine)                      # (local)
d2ln_zeta = np.gradient(dln_zeta, s_fine)                     # (local)

# ============================================================================
# 3. PLAN-LITERAL: s* = argmin |d^2 zeta / ds^2| on [0.5, 6.0]
# ============================================================================
print("\n" + "=" * 80)
print("3. PLAN-LITERAL s* = argmin |d^2 zeta_D / ds^2| over scan_range [0.5, 6.0]")
print("=" * 80)

# Structural check: d^2 zeta/ds^2 is monotonically DECREASING on this range
# (proof in script docstring step 4). argmin is at upper boundary.
interior_mask = (s_fine >= 0.5) & (s_fine <= 6.0)              # (local) full plan range
abs_d2 = np.abs(d2zeta[interior_mask])                         # (local)
s_interior = s_fine[interior_mask]                             # (local)
idx_plan = int(np.argmin(abs_d2))                              # (local)
s_star_plan = float(s_interior[idx_plan])                      # (local)

# Extract effective d_spec via logarithmic-derivative pole proxy:
#   d_spec = s + 1 / (d log zeta / ds)
dln_at_star_plan = float(dln_zeta[interior_mask][idx_plan])    # (local)
if dln_at_star_plan != 0:
    d_spec_plan = s_star_plan + 1.0 / dln_at_star_plan         # (local)
else:
    d_spec_plan = np.nan

print(f"  s* (plan-literal argmin |d^2 zeta/ds^2|): {s_star_plan:.4f}")
print(f"  (boundary-dominated: d^2 zeta/ds^2 is monotone decreasing on [0.5, 6.0])")
print(f"  |d^2 zeta/ds^2| at s*        : {abs_d2[idx_plan]:.3e}")
print(f"  d log zeta / ds at s*        : {dln_at_star_plan:.6f}")
print(f"  d_spec (plan-literal proxy)  : {d_spec_plan:.4f}")

# ============================================================================
# 4. DIAGNOSTIC: alternative s* interpretations (cross-check, not primary)
# ============================================================================
print("\n" + "=" * 80)
print("4. CROSS-CHECK INTERPRETATIONS (diagnostic, not verdict-primary)")
print("=" * 80)

log_zeta_ext = np.log(zeta_ext)                               # (local)
dln_ext = np.gradient(log_zeta_ext, s_ext)                    # (local)
d2ln_ext = np.gradient(dln_ext, s_ext)                        # (local)
d_eff_ext = s_ext + 1.0 / dln_ext                             # (local) pointwise d_eff

# Interpretation A: s* = argmax d^2 log zeta / ds^2 (max log-concavity inflection)
maskA = (s_ext >= 1.0) & (s_ext <= 11.0)                      # (local)
idxA = int(np.argmax(d2ln_ext[maskA]))
s_star_A = float(s_ext[maskA][idxA])                          # (local)
d_spec_A = float(d_eff_ext[maskA][idxA])                      # (local)

# Interpretation B: s such that d_eff_pointwise = 3 (direct crossing)
# Find first crossing of d_eff - 3 on the extended grid
d_eff_minus_3 = d_eff_ext - 3.0                                # (local)
cross_idx = None
for i in range(1, len(s_ext)):
    if d_eff_minus_3[i-1] * d_eff_minus_3[i] < 0:
        cross_idx = i
        break
if cross_idx is not None:
    # Linear interp
    w = -d_eff_minus_3[cross_idx-1] / (d_eff_minus_3[cross_idx] - d_eff_minus_3[cross_idx-1])
    s_star_B = float(s_ext[cross_idx-1] + w * (s_ext[cross_idx] - s_ext[cross_idx-1]))
    d_spec_B = 3.0  # (local) crossing value by construction
else:
    s_star_B = np.nan
    d_spec_B = np.nan

# Interpretation C: s* = upper boundary s=6 (plan boundary, same as plan-literal)
# (same as plan-literal by monotonicity)

print(f"  [A] argmax d^2 log zeta / ds^2 (max log-concavity inflection):")
print(f"      s* = {s_star_A:.4f}, d_eff(s*) = {d_spec_A:.4f}")
print(f"  [B] d_eff pointwise = 3 crossing:")
print(f"      s* = {s_star_B:.4f}, d_eff(s*) = {d_spec_B:.4f} (direct implicit)")
print(f"  [LITERAL] argmin |d^2 zeta / ds^2| on [0.5, 6.0]:")
print(f"      s* = {s_star_plan:.4f}, d_eff(s*) = {d_spec_plan:.4f} (PRIMARY)")

# ============================================================================
# 5. L_max CONVERGENCE CROSS-CHECK (literal extractor at L in {6, 8, 10, 12})
# ============================================================================
print("\n" + "=" * 80)
print("5. L_max CONVERGENCE CROSS-CHECK on plan-literal extractor")
print("=" * 80)

L_max_values = [6, 8, 10, 12]                                 # (local)
d_spec_by_L = {}                                              # (local)
s_star_by_L = {}                                              # (local)

for Lm in L_max_values:
    lams_L, mults_L = gather_spectrum(sector_evals, Lm)
    zL = zeta_sum(lams_L, mults_L, s_fine, device=GPU_DEV)
    log_zL = np.log(zL)
    dzL = np.gradient(zL, s_fine)
    d2zL = np.gradient(dzL, s_fine)
    dln_zL = np.gradient(log_zL, s_fine)
    mask = (s_fine >= 0.5) & (s_fine <= 6.0)
    idx = int(np.argmin(np.abs(d2zL[mask])))
    s_star_L = float(s_fine[mask][idx])
    dln_L = float(dln_zL[mask][idx])
    if dln_L != 0:
        d_spec_L = s_star_L + 1.0 / dln_L                     # (local)
    else:
        d_spec_L = np.nan
    d_spec_by_L[Lm] = d_spec_L
    s_star_by_L[Lm] = s_star_L
    print(f"  L_max={Lm:2d}: N_unique={len(lams_L):6d}, s*={s_star_L:.4f}, d_spec={d_spec_L:.4f}")

d_conv = abs(d_spec_by_L[12] - d_spec_by_L[10])               # (local)
print(f"\n  L_max=10 -> L_max=12 convergence delta: {d_conv:.4f}")

# ============================================================================
# 6. VERDICT — plan-literal primary
# ============================================================================
print("\n" + "=" * 80)
print("6. GATE VERDICT (plan-literal extractor)")
print("=" * 80)

PASS_LO = 2.5                                                 # (local)
PASS_HI = 3.5                                                 # (local)
INFO_LO = 2.0                                                 # (local)
INFO_HI = 4.0                                                 # (local)

d_spec = d_spec_plan  # (local) PRIMARY per plan §W9b-105.6

if PASS_LO <= d_spec <= PASS_HI:
    verdict = "PASS"
elif (INFO_LO <= d_spec < PASS_LO) or (PASS_HI < d_spec <= INFO_HI):
    verdict = "INFO"
else:
    verdict = "FAIL"

print(f"  PRIMARY extractor: s* = {s_star_plan:.4f}, d_spec = {d_spec:.4f}")
print(f"  Thresholds:")
print(f"    PASS  : [2.5, 3.5]")
print(f"    INFO  : [2.0, 2.5) U (3.5, 4.0]")
print(f"    FAIL  : outside [2.0, 4.0]")
print(f"  VERDICT (primary)   = {verdict}")

print(f"\n  Cross-check verdicts (diagnostic):")
for label, dv in [("LITERAL", d_spec_plan), ("A: argmax d^2 log zeta", d_spec_A),
                  ("B: d_eff=3 crossing", d_spec_B)]:
    if not np.isnan(dv):
        if PASS_LO <= dv <= PASS_HI:
            v = "PASS"
        elif (INFO_LO <= dv < PASS_LO) or (PASS_HI < dv <= INFO_HI):
            v = "INFO"
        else:
            v = "FAIL"
    else:
        v = "N/A"
    print(f"    [{label:25s}] d_spec = {dv:.4f} -> {v}")

# ============================================================================
# 7. SAVE DATA + PLOT
# ============================================================================
NPZ_OUT = "s84_w9b_deriv_i_spectral_dim.npz"
PNG_OUT = "s84_w9b_deriv_i_spectral_dim.png"

np.savez(
    NPZ_OUT,
    # Plan scan grid
    s_fine=s_fine,
    zeta_fine=zeta_fine,
    log_zeta=log_zeta,
    dzeta=dzeta,
    d2zeta=d2zeta,
    dln_zeta=dln_zeta,
    d2ln_zeta=d2ln_zeta,
    # Extended diagnostic grid
    s_ext=s_ext,
    zeta_ext=zeta_ext,
    d_eff_ext=d_eff_ext,
    # Plan-literal result (primary)
    s_star_plan=s_star_plan,
    d_spec_plan=d_spec_plan,
    # Cross-checks
    s_star_A=s_star_A,
    d_spec_A=d_spec_A,
    s_star_B=s_star_B,
    d_spec_B=d_spec_B,
    # Convergence
    L_max_grid=np.array(L_max_values),
    d_spec_by_L=np.array([d_spec_by_L[Lm] for Lm in L_max_values]),
    s_star_by_L=np.array([s_star_by_L[Lm] for Lm in L_max_values]),
    # Verdict
    verdict=verdict,
    n_unique_L10=n_unique_L10,
    n_pw_L10=n_pw_L10,
    tau_fold=tau_fold,
    # Input pins
    sha_spectrum=sha_spectrum,
    sha_const=sha_const,
    sha_script=sha_script,
)
print(f"\n  Saved data : {NPZ_OUT}")

# Plot
fig = plt.figure(figsize=(14, 10))
gs = fig.add_gridspec(2, 2, hspace=0.3, wspace=0.27)

# Panel A: zeta(s) on log scale, full extended range
ax1 = fig.add_subplot(gs[0, 0])
ax1.semilogy(s_ext, zeta_ext, "b-", lw=1.1, label=r"$\zeta_D(s)$ (extended)")
ax1.semilogy(s_fine, zeta_fine, "k-", lw=1.6, label=r"$\zeta_D(s)$ (plan scan)")
ax1.axvline(s_star_plan, color="r", ls="--", lw=0.9,
            label=fr"$s^*_{{\rm plan}} = {s_star_plan:.3f}$")
ax1.axvline(s_star_A, color="orange", ls=":", lw=0.9,
            label=fr"$s^*_A = {s_star_A:.3f}$ (max log-concave)")
ax1.set_xlabel("$s$")
ax1.set_ylabel(r"$\zeta_D(s)$")
ax1.set_title(r"Spectral zeta $\zeta_D(s) = \sum_n d_\rho \lambda_n^{-s}$")
ax1.legend(loc="best", fontsize=8)
ax1.grid(alpha=0.3)

# Panel B: d²ζ/ds² (plan-literal minimand)
ax2 = fig.add_subplot(gs[0, 1])
ax2.semilogy(s_fine, np.abs(d2zeta), "b-", lw=1.3,
             label=r"$|d^2 \zeta / ds^2|$ (plan-literal minimand)")
ax2.axvline(s_star_plan, color="r", ls="--", lw=0.9,
            label=fr"$s^*_{{\rm plan}} = {s_star_plan:.3f}$")
ax2.axvspan(0.5, 6.0, alpha=0.08, color="gray", label="plan scan_range")
ax2.set_xlabel("$s$")
ax2.set_ylabel(r"$|d^2 \zeta / ds^2|$")
ax2.set_title(r"Plan-literal minimand: monotone-decreasing on [0.5, 6.0]")
ax2.legend(loc="best", fontsize=8)
ax2.grid(alpha=0.3)

# Panel C: pointwise d_eff(s) estimator
ax3 = fig.add_subplot(gs[1, 0])
ax3.plot(s_ext, d_eff_ext, "b-", lw=1.1, label=r"$d_{\rm eff}(s) = s + 1/(d\ln\zeta/ds)$")
ax3.axhspan(2.5, 3.5, alpha=0.20, color="green", label="PASS [2.5, 3.5]")
ax3.axhspan(2.0, 2.5, alpha=0.10, color="orange")
ax3.axhspan(3.5, 4.0, alpha=0.10, color="orange")
ax3.axvline(s_star_plan, color="r", ls="--", lw=0.9, label=fr"$s^*_{{\rm plan}} = {s_star_plan:.3f}$")
ax3.axvline(s_star_A, color="orange", ls=":", lw=0.9, label=fr"$s^*_A = {s_star_A:.3f}$")
if not np.isnan(s_star_B):
    ax3.axvline(s_star_B, color="purple", ls="-.", lw=0.9,
                label=fr"$s^*_B = {s_star_B:.3f}$ ($d_{{\rm eff}}=3$)")
ax3.set_xlabel("$s$")
ax3.set_ylabel(r"$d_{\rm eff}(s)$")
ax3.set_ylim(-1, 8)
ax3.set_xlim(0.5, 11)
ax3.set_title("Pointwise effective spectral dimension")
ax3.legend(loc="best", fontsize=7)
ax3.grid(alpha=0.3)

# Panel D: L_max convergence
ax4 = fig.add_subplot(gs[1, 1])
Ls = list(L_max_values)
ds = [d_spec_by_L[Lm] for Lm in Ls]
ax4.plot(Ls, ds, "ko-", lw=1.2, markersize=7, label=r"$d_{\rm spec}(L_{\max})$ primary")
ax4.axhspan(2.5, 3.5, alpha=0.20, color="green", label="PASS")
ax4.axhspan(2.0, 2.5, alpha=0.10, color="orange")
ax4.axhspan(3.5, 4.0, alpha=0.10, color="orange")
ax4.set_xlabel(r"$L_{\max}$")
ax4.set_ylabel(r"$d_{\rm spec}$")
ax4.set_title(r"$L_{\max}$ convergence at plan-literal $s^*$")
ax4.set_xticks(Ls)
ax4.grid(alpha=0.3)
ax4.legend(loc="best", fontsize=8)

fig.suptitle(
    f"W9b-105-S84-DERIV-I: Spectral Dimension at Fiber-Transition Scale\n"
    f"Jensen SU(3), tau_fold = {tau_fold}, L_max = 10, "
    f"d_spec = {d_spec:.3f} (plan-literal), verdict = {verdict}",
    fontsize=11,
)
plt.savefig(PNG_OUT, dpi=140, bbox_inches="tight")
plt.close()
print(f"  Saved plot : {PNG_OUT}")

# ============================================================================
# 8. CLOSURE SHA (ordered input-pin map)
# ============================================================================
closure_inputs = {
    "gate_id": "W9b-105-S84-DERIV-I",
    "session": "S84",
    "spectrum_cache_sha": sha_spectrum,
    "canonical_constants_sha": sha_const,
    "script_sha": sha_script,
    "tau_fold": f"{tau_fold}",
    "L_max_primary": "10",
    "L_max_conv": "6,8,10,12",
    "s_scan_range_plan": "[0.5, 6.0]",
    "s_scan_step": "0.001",
    "s_scan_range_ext": "[0.5, 12.0]",
    "regulator_eps": "1e-12",
    "convention": "|D_K|=sqrt(D_K^2+eps^2)",
    "scheme": "zeta-reg",
    "zeta_normalization": "zeta_D(s)=sum_n dim_rho * lambda_n^{-s}",
    "s_star_def": "argmin|d^2 zeta_D / ds^2| on [0.5, 6.0] (plan-literal)",
    "d_spec_extractor": "d_spec = s* + 1/(d log zeta/ds) at s*",
    "thresholds": "PASS[2.5,3.5] INFO[2.0,2.5)U(3.5,4.0] FAIL else",
    "s_star_plan": f"{s_star_plan:.6f}",
    "value_d_spec": f"{d_spec:.6f}",
    "verdict": verdict,
}
closure_str = "|".join(f"{k}={v}" for k, v in sorted(closure_inputs.items()))
closure_sha = hashlib.sha256(closure_str.encode("utf-8")).hexdigest()
print(f"\n  Closure SHA-256: {closure_sha}")

# ============================================================================
# 9. VERDICT LINE
# ============================================================================
output_tuple = (d_spec, "zeta-reg", "|D_K|=sqrt(D^2+eps^2)", 10)
print(f"\n  Output 4-tuple: (value={d_spec:.6f}, scheme=zeta-reg, "
      f"convention=|D_K|=sqrt(D^2+eps^2), L_max=10)")

verdict_line = (
    f"W9b-105-S84-DERIV-I: {verdict} -- "
    f"value={d_spec:.6f} scheme=zeta-reg convention=|D_K|=sqrt(D^2+eps^2) "
    f"L_max=10 sha256={closure_sha}"
)
print(f"\n  Verdict line:\n  {verdict_line}")

VERDICT_FILE = "s84_gate_verdicts.txt"
with open(VERDICT_FILE, "a", encoding="utf-8") as f:
    f.write(verdict_line + "\n")
print(f"\n  Appended to : {VERDICT_FILE}")

print("\n" + "=" * 80)
print("DONE.")
print("=" * 80)
