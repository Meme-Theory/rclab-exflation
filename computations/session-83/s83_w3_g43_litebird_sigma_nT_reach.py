#!/usr/bin/env python3
"""
S83-W3-G43: LITEBIRD-SIGMA-N_T-REACH — Projected σ(n_T) by detector-year
=========================================================================

Gate: [VERIFY][PENDING-EVENT]
PASS: σ(n_T) @ 3 detector-years <= 0.04
INFO: 0.04 < σ(n_T) <= 0.06
FAIL: σ(n_T) > 0.06

Classification: PHONONIC (tensor spectrum observability).

Method
------
Fisher forecast on (r, n_T) from CMB B-mode spectrum at LiteBIRD
detector performance (15-band whole-sky, 3-year baseline).

Substitution chain:
  Step 1: F_ij = sum_l (2l+1) f_sky (dC_l/dp_i)(dC_l/dp_j) / [2 (C_l^tot)^2]
          where C_l^tot = C_l^signal + C_l^lens,residual + N_l^BB
  Step 2: σ(n_T) = sqrt([F^{-1}]_{n_T,n_T})  (marginalized over r)
  Step 3: Noise scaling: N_l^BB ∝ 1/t_obs  (white-noise integration)
          => in noise-limited regime F ∝ t_obs^2 => σ ∝ 1/t_obs
          in sample-variance regime F saturates => σ → floor
  Step 4: Direction — σ(n_T) decreases monotonically with t_obs
          with a sample-variance/lensing floor.

Inputs
------
- r(CMB) = 0.0242 from s66_tensor_transfer.npz (framework prediction)
- n_T(CMB) = -3.02e-3 (framework, scenario A)
- LiteBIRD instrument spec (PTEP 2023, 042F01):
  - 15 frequency bands, 40–402 GHz
  - Combined post-component-separation BB noise ≈ 2.16 μK-arcmin at 1 yr
  - Effective beam ~30 arcmin for tensor analysis (CMB-scale l<200)
  - f_sky = 0.7 after Galactic mask
  - Residual lensing ~50% after internal + Planck delensing
- l-range: 2–200 (tensor BB dominated by recombination bump l~80 + reion l<10)

Outputs
-------
- computations/session-83/s83_w3_g43_litebird_sigma_nT_reach.npz
- computations/session-83/s83_w3_g43_litebird_sigma_nT_reach.png
- Verdict line appended to s83_gate_verdicts.txt
"""
import sys
import os
import hashlib
import json

os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

sys.path.insert(0, "computations")
from canonical_constants import (
    PI, k_pivot_planck, A_s_CMB,
)

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.linalg import inv


# =============================================================================
# SECTION 1: Input-pin SHA-256 ledger (mandatory for S81+ gates)
# =============================================================================
INPUT_FILES = [
    "computations/session-66/s66_tensor_transfer.npz",
    "computations/session-67/s67_acoustic_tensor.npz",
    "computations/_shared/canonical_constants.py",
]


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for block in iter(lambda: fh.read(8192), b""):
            h.update(block)
    return h.hexdigest()


input_pins = {p: _sha256(p) for p in INPUT_FILES}
print("=" * 72)
print("S83-W3-G43: LITEBIRD-SIGMA-N_T-REACH")
print("=" * 72)
print("\n-- Input pins --")
for p, s in input_pins.items():
    print(f"  {p}  sha256={s[:16]}...")


# =============================================================================
# SECTION 2: Load framework tensor inputs
# =============================================================================
d66 = np.load("computations/session-66/s66_tensor_transfer.npz", allow_pickle=True)
r_CMB_fw = float(d66["r_CMB_standard"])                 # (local) framework r(CMB)
nT_CMB_fw = float(d66["n_T_CMB_scenario_A"])            # (local) framework n_T(CMB)

print(f"\n-- Framework inputs --")
print(f"  r(CMB)   = {r_CMB_fw:.4f}")
print(f"  n_T(CMB) = {nT_CMB_fw:.6f}")


# =============================================================================
# SECTION 3: LiteBIRD instrument specification
# =============================================================================
# Source: LiteBIRD Collaboration, PTEP 2023, 042F01, Table 3.
# Post-component-separation BB noise quoted at 3-year full mission = 2.16 μK-arcmin.
# We parameterise N_l^BB at arbitrary t_obs as:
#   N_l^BB(t) = (σ_3yr * sqrt(3/t_yr))^2 * exp[l(l+1) θ_b^2 / (8 ln 2)]
# where σ_3yr = 2.16 μK-arcmin is the 3-year combined sensitivity.

sigma_noise_3yr_uKarcmin = 2.16                         # (local) LiteBIRD 3-year combined BB noise
beam_fwhm_arcmin = 30.0                                 # (local) effective BB beam at l<200
f_sky = 0.70                                            # (local) after Galactic mask
delensing_frac = 0.50                                   # (local) residual lensing after delensing
l_min, l_max_analysis = 2, 200                          # (local) LiteBIRD BB multipole range


# =============================================================================
# SECTION 4: BB power-spectrum model D_l = l(l+1) C_l / (2π)
# =============================================================================
# Standard parametric fit to CAMB BB tensor output (Kamionkowski & Kovetz 2016,
# eq. replicated in s68_liteb_r_forecast.py §2). Reionisation bump at l<10,
# recombination peak at l~80, exponential cutoff near l~400.

def D_l_BB_tensor(ells, r_val, nT_val, k_pivot=k_pivot_planck):
    """Tensor BB D_l in μK^2 for power-law tensor spectrum P_T ∝ r · (k/k_pivot)^{nT}."""
    x = ells / 80.0                                                    # (local)
    D_reion = 0.0037 * np.exp(-((ells - 4.0) / 3.0) ** 2)              # (local) l<10 bump
    D_recomb = 0.022 * x**2 / (1.0 + x**4.0) * np.exp(-(ells / 400.0) ** 2)  # (local)
    D0 = D_reion + D_recomb
    r_star_Mpc = 144.43                                                # (local) sound horizon @ decoupling (Planck 2018)
    l_pivot = k_pivot * r_star_Mpc                                     # (local) ~ 7.2
    tilt_factor = (np.maximum(ells, 1.0) / l_pivot) ** nT_val
    return r_val * D0 * tilt_factor


def D_l_BB_lens(ells):
    """Lensing-induced B-mode D_l [μK^2] (parametric Smith+12 fit)."""
    return 5.0e-6 * (ells / 1000.0) ** 0.5 * (1.0 + (ells / 60.0) ** 2) ** (-0.1)  # (local)


# =============================================================================
# SECTION 5: Fisher matrix builder as function of detector-years
# =============================================================================
def compute_fisher_LiteBIRD(detector_years, r_fid, nT_fid):
    """
    Fisher on (r, n_T) from LiteBIRD BB spectrum assuming fiducial (r_fid, nT_fid).
    Noise rescales as N_l ∝ 1 / detector_years.
    Returns 2x2 Fisher matrix.
    """
    ell = np.arange(l_min, l_max_analysis + 1)                         # (local)

    # --- Signal ---
    D_sig = D_l_BB_tensor(ell, r_fid, nT_fid)                          # μK^2
    C_sig = D_sig * 2.0 * PI / (ell * (ell + 1))                       # μK^2 · sr (C_l)

    # --- Lensing residual ---
    D_lens_full = D_l_BB_lens(ell)                                     # (local)
    D_lens_res = delensing_frac * D_lens_full                          # (local)
    C_lens_res = D_lens_res * 2.0 * PI / (ell * (ell + 1))             # (local)

    # --- Noise (scales as 1/t_obs) ---
    noise_uKrad = (sigma_noise_3yr_uKarcmin *
                   np.sqrt(3.0 / detector_years)) * (PI / 180.0 / 60.0)   # (local)
    beam_sigma_rad = (beam_fwhm_arcmin *
                      (PI / 180.0 / 60.0)) / np.sqrt(8.0 * np.log(2.0))   # (local)
    N_l = noise_uKrad ** 2 * np.exp(ell * (ell + 1) * beam_sigma_rad ** 2)  # (local)

    # --- Total ---
    C_tot = C_sig + C_lens_res + N_l

    # --- Signal derivatives wrt (r, n_T) by finite difference on D_l, then → C_l ---
    dr = 1e-4                                                          # (local)
    dnT = 1e-4                                                         # (local)
    D_rp = D_l_BB_tensor(ell, r_fid + dr, nT_fid)
    D_rm = D_l_BB_tensor(ell, r_fid - dr, nT_fid)
    D_np = D_l_BB_tensor(ell, r_fid, nT_fid + dnT)
    D_nm = D_l_BB_tensor(ell, r_fid, nT_fid - dnT)
    dDdr = (D_rp - D_rm) / (2.0 * dr)                                  # (local)
    dDdnT = (D_np - D_nm) / (2.0 * dnT)                                # (local)
    dCdr = dDdr * 2.0 * PI / (ell * (ell + 1))                         # (local)
    dCdnT = dDdnT * 2.0 * PI / (ell * (ell + 1))                       # (local)

    # --- Fisher sums (knox-formula weight) ---
    weight = (2.0 * ell + 1.0) * f_sky / (2.0 * C_tot ** 2)            # (local)
    F = np.zeros((2, 2))                                               # (local)
    F[0, 0] = np.sum(weight * dCdr * dCdr)
    F[0, 1] = np.sum(weight * dCdr * dCdnT)
    F[1, 0] = F[0, 1]
    F[1, 1] = np.sum(weight * dCdnT * dCdnT)
    return F, ell, C_sig, C_lens_res, N_l


# =============================================================================
# SECTION 6: Fisher forecast at 1 / 2 / 3 detector-years
# =============================================================================
print("\n-- Fisher forecast per detector-year --")
results = {}
for t_yr in [1, 2, 3]:
    F, ell_arr, C_sig, C_lens_res, N_l = compute_fisher_LiteBIRD(
        detector_years=t_yr, r_fid=r_CMB_fw, nT_fid=nT_CMB_fw)
    Cov = inv(F)
    sigma_r = float(np.sqrt(Cov[0, 0]))                                # (local)
    sigma_nT = float(np.sqrt(Cov[1, 1]))                               # (local)
    rho = float(Cov[0, 1] / (sigma_r * sigma_nT))                      # (local)
    results[t_yr] = {
        "F": F, "Cov": Cov, "sigma_r": sigma_r,
        "sigma_nT": sigma_nT, "rho": rho,
    }
    print(f"  t_obs={t_yr} yr :  σ(r)={sigma_r:.4f}  σ(n_T)={sigma_nT:.4f}  ρ(r,n_T)={rho:+.3f}")


# =============================================================================
# SECTION 7: Saturation check — fixed t_obs=3 yr under noise vs sample-variance
# =============================================================================
# Sanity: σ(n_T) should saturate for small sigma_r as more detector-years are
# added (sample variance on D_l^sig becomes the dominant term).
print("\n-- Saturation sanity check (longer t_obs) --")
for t_yr in [5, 10, 100]:
    F, *_ = compute_fisher_LiteBIRD(
        detector_years=t_yr, r_fid=r_CMB_fw, nT_fid=nT_CMB_fw)
    Cov = inv(F)
    sigma_nT = float(np.sqrt(Cov[1, 1]))                               # (local)
    print(f"  t_obs={t_yr:3d} yr :  σ(n_T)={sigma_nT:.4f}")


# =============================================================================
# SECTION 8: Verdict — PASS/INFO/FAIL at 3 detector-years
# =============================================================================
sigma_nT_3yr = results[3]["sigma_nT"]                                  # (local)
threshold_pass = 0.04                                                  # (local) PASS gate
threshold_info = 0.06                                                  # (local) INFO gate

if sigma_nT_3yr <= threshold_pass:
    verdict = "PASS"
elif sigma_nT_3yr <= threshold_info:
    verdict = "INFO"
else:
    verdict = "FAIL"

print("\n" + "=" * 72)
print("VERDICT")
print("=" * 72)
print(f"  σ(n_T) @ 3 yr LiteBIRD = {sigma_nT_3yr:.4f}")
print(f"  PASS threshold:  <= {threshold_pass:.2f}")
print(f"  INFO threshold:  <= {threshold_info:.2f}")
print(f"  FAIL threshold:  >  {threshold_info:.2f}")
print(f"  Verdict: {verdict}")


# =============================================================================
# SECTION 9: Data save + closure SHA
# =============================================================================
save_path = "computations/session-83/s83_w3_g43_litebird_sigma_nT_reach.npz"
np.savez(save_path,
         # Framework inputs
         r_CMB_fw=r_CMB_fw,
         nT_CMB_fw=nT_CMB_fw,
         # Instrument spec
         sigma_noise_3yr_uKarcmin=sigma_noise_3yr_uKarcmin,
         beam_fwhm_arcmin=beam_fwhm_arcmin,
         f_sky=f_sky,
         delensing_frac=delensing_frac,
         l_min=l_min, l_max_analysis=l_max_analysis,
         # Per-year results
         t_yr=np.array([1, 2, 3, 5, 10, 100]),
         F_1yr=results[1]["F"], F_2yr=results[2]["F"], F_3yr=results[3]["F"],
         sigma_r_1yr=results[1]["sigma_r"],
         sigma_r_2yr=results[2]["sigma_r"],
         sigma_r_3yr=results[3]["sigma_r"],
         sigma_nT_1yr=results[1]["sigma_nT"],
         sigma_nT_2yr=results[2]["sigma_nT"],
         sigma_nT_3yr=results[3]["sigma_nT"],
         rho_r_nT_3yr=results[3]["rho"],
         # Verdict block
         threshold_pass=threshold_pass,
         threshold_info=threshold_info,
         verdict=verdict,
         gate_name="S83-LITEBIRD-SIGMA-N_T-REACH",
         # Input pins
         input_pins=json.dumps(input_pins),
         )
print(f"\nData saved: {save_path}")

# Closure SHA: stable over input-pin + key numerical outputs (not the .npz itself)
closure_map = {
    "gate": "S83-LITEBIRD-SIGMA-N_T-REACH",
    "inputs": input_pins,
    "sigma_nT_3yr": f"{sigma_nT_3yr:.10e}",
    "sigma_r_3yr": f"{results[3]['sigma_r']:.10e}",
    "verdict": verdict,
    "scheme": "LiteBIRD-Fisher",
    "convention": "B-mode-spectra",
    "r_fid": f"{r_CMB_fw:.10e}",
    "nT_fid": f"{nT_CMB_fw:.10e}",
    "threshold_pass": f"{threshold_pass:.6f}",
    "f_sky": f"{f_sky:.6f}",
    "delensing_frac": f"{delensing_frac:.6f}",
    "sigma_noise_3yr_uKarcmin": f"{sigma_noise_3yr_uKarcmin:.6f}",
    "beam_fwhm_arcmin": f"{beam_fwhm_arcmin:.6f}",
    "l_range": f"{l_min}-{l_max_analysis}",
}
closure_sha = hashlib.sha256(
    json.dumps(closure_map, sort_keys=True).encode()).hexdigest()
print(f"Closure sha256: {closure_sha}")


# =============================================================================
# SECTION 10: Plot
# =============================================================================
fig, axes = plt.subplots(1, 2, figsize=(13, 5.2))

# --- Panel A: σ(n_T) vs detector-years ---
ax = axes[0]
t_years_plot = np.array([0.5, 1, 2, 3, 5, 10, 100])                    # (local)
sigmas_nT_plot = []                                                    # (local)
for t_yr in t_years_plot:
    F, *_ = compute_fisher_LiteBIRD(
        detector_years=float(t_yr), r_fid=r_CMB_fw, nT_fid=nT_CMB_fw)
    sigmas_nT_plot.append(float(np.sqrt(inv(F)[1, 1])))
sigmas_nT_plot = np.array(sigmas_nT_plot)
ax.loglog(t_years_plot, sigmas_nT_plot, 'o-', color='C0', lw=1.8, label=r'$\sigma(n_T)$')
ax.axhline(threshold_pass, color='C2', ls='--', lw=1.0, label=f'PASS (<= {threshold_pass:.2f})')
ax.axhline(threshold_info, color='orange', ls='--', lw=1.0, label=f'INFO (<= {threshold_info:.2f})')
ax.axvline(3, color='gray', ls=':', lw=0.9)
ax.plot([3], [sigma_nT_3yr], 's', color='C3', ms=9,
        label=f'3 yr baseline: σ(n_T)={sigma_nT_3yr:.3f}')
ax.set_xlabel('Detector-years', fontsize=11)
ax.set_ylabel(r'$\sigma(n_T)$', fontsize=11)
ax.set_title('LiteBIRD σ(n_T) vs Mission Duration\n(framework fid: r=%.3f, n_T=%.4f)'
             % (r_CMB_fw, nT_CMB_fw), fontsize=11)
ax.grid(True, which='both', alpha=0.3)
ax.legend(fontsize=9, loc='lower left')

# --- Panel B: BB spectrum stack vs LiteBIRD noise floor ---
ax2 = axes[1]
F3, ell_arr, C_sig, C_lens_res, N_l = compute_fisher_LiteBIRD(
    detector_years=3, r_fid=r_CMB_fw, nT_fid=nT_CMB_fw)
D_sig = D_l_BB_tensor(ell_arr, r_CMB_fw, nT_CMB_fw)                    # (local)
D_lens_full = D_l_BB_lens(ell_arr)                                     # (local)
D_lens_res = delensing_frac * D_lens_full                              # (local)
D_noise = N_l * ell_arr * (ell_arr + 1) / (2.0 * PI)                   # (local)
ax2.loglog(ell_arr, D_sig, 'C0-', lw=1.8,
           label=r'Framework tensor BB (r=%.3f, n$_T$=%.4f)' % (r_CMB_fw, nT_CMB_fw))
ax2.loglog(ell_arr, D_lens_full, color='gray', ls=':', lw=1.0, label='Lensing BB (no delensing)')
ax2.loglog(ell_arr, D_lens_res, color='gray', ls='--', lw=1.0, label='Lensing BB (50% delensed)')
ax2.loglog(ell_arr, D_noise, 'k-.', lw=1.0, label='LiteBIRD noise (3 yr)')
ax2.set_xlim(2, 200)
ax2.set_ylim(1e-7, 1e-1)
ax2.set_xlabel(r'Multipole $\ell$', fontsize=11)
ax2.set_ylabel(r'$D_\ell^{BB}\;[\mu \mathrm{K}^2]$', fontsize=11)
ax2.set_title('LiteBIRD BB Budget (3-year)', fontsize=11)
ax2.grid(True, which='both', alpha=0.3)
ax2.legend(fontsize=8, loc='lower right')

plt.tight_layout()
plot_path = "computations/session-83/s83_w3_g43_litebird_sigma_nT_reach.png"
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"Plot saved: {plot_path}")
plt.close()


# =============================================================================
# SECTION 11: Verdict-line append (S81+ canonical form)
# =============================================================================
verdict_line = (
    f"S83-LITEBIRD-SIGMA-N_T-REACH: {verdict} -- "
    f"value=sigma_nT_3yr={sigma_nT_3yr:.6f} "
    f"scheme=LiteBIRD-Fisher "
    f"convention=B-mode-spectra "
    f"L_max=N/A "
    f"sha256={closure_sha}\n"
)

verdicts_path = "computations/session-83/s83_gate_verdicts.txt"
with open(verdicts_path, "a", encoding="utf-8") as fh:
    fh.write(verdict_line)
print(f"\nVerdict appended to {verdicts_path}:")
print(f"  {verdict_line.rstrip()}")


# =============================================================================
# SECTION 12: 4-tuple tag
# =============================================================================
tag = (f"(sigma_nT_3yr={sigma_nT_3yr:.6f}, "
       f"scheme=LiteBIRD-Fisher, "
       f"convention=B-mode-spectra, "
       f"L_max=N/A)")
print(f"\n4-tuple: {tag}")
print("\nS83-W3-G43: COMPLETE.")
