#!/usr/bin/env python3
"""
S84-W4-37: LB-CMBS4-JOINT-SIGMA-NT — Fisher joint LiteBIRD + CMB-S4 on (r, n_T, A_lens)
=========================================================================================

Gate: [VERIFY]
PASS: sigma(n_T)_joint_3yr <= 0.04
INFO: 0.04 < sigma(n_T)_joint_3yr <= 0.06
FAIL: sigma(n_T)_joint_3yr > 0.06

Classification: GEOMETRIC (Fisher-matrix joint on B-mode observables; not substrate excitation).

Method
------
Extend S83-G43 (LiteBIRD-alone sigma(n_T)=0.054 INFO) to 3-parameter joint Fisher
combining LiteBIRD B-modes + CMB-S4 delensing. Treat LB and S4 as INDEPENDENT
experiments per the orchestrator override: F_joint = F_LB + F_S4 (Fisher sum, NOT
fused-likelihood).

Substitution chain [VERIFY]
---------------------------
Step 1 (definition): For a Gaussian CMB B-mode likelihood with multipoles as
       independent measurements,
          F_{ij}^X = sum_l  (2l+1)/2 · f_sky^X · (dC_l/dp_i)(dC_l/dp_j) / (C_l^tot)^2
       where X in {LB, S4}, p = (r, n_T, A_lens), C_l^tot = C_l^sig + A_lens·C_l^lens,res + N_l^BB.
Step 2 (substitution): Build C_l^sig from framework fiducial (r=0.0117, n_T=-0.003024)
       with tilt factor (l/l_pivot)^{n_T}; lensing residual C_l^lens,res = (1 - delens_X)·C_l^lens;
       noise from Knox formula N_l = sigma_arcmin^2 · exp(l(l+1) theta_beam^2 / (8 ln 2)).
Step 3 (simplification): Independent-experiment Fisher sum F_joint = F_LB + F_S4;
       Cov = F_joint^{-1}; sigma(n_T) = sqrt(Cov_{22}).
Step 4 (direction): Fisher is positive-definite, so marginalized sigma is always
       positive; the joint-vs-alone improvement must be verified numerically.
       Shapes: dC/dn_T ∝ C_sig · ln(l/l_pivot), which is ZERO at l=l_pivot and
       grows in magnitude toward either end of the multipole range. Hence high-l
       CMB-S4 leverage on n_T only helps where C_sig is not subdominant to N_l;
       the joint improvement is tempered by C_sig drop-off at l>~300.

Outputs
-------
- computations/session-84/s84_w4_lb_cmbs4_joint_sigma_nt.npz
- computations/session-84/s84_w4_lb_cmbs4_joint_sigma_nt.png (sigma(n_T) vs delens_S4 heatmap)
- Verdict line -> computations/session-84/s84_gate_verdicts.txt
"""
import sys
import os
import hashlib
import json

# CPU-only path: 3x3 Fisher is trivial; cap threads to avoid contention
os.environ.setdefault('OMP_NUM_THREADS', '4')
os.environ.setdefault('MKL_NUM_THREADS', '4')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    PI, k_pivot_planck, A_s_CMB,
    # S84 LiteBIRD + CMB-S4 additions
    sigma_LB_3yr_uKarcmin, beam_LB_arcmin, f_sky_LB, delens_LB, ell_min_LB, ell_max_LB,
    sigma_S4_uKarcmin, beam_S4_arcmin, f_sky_S4, delens_S4, ell_min_S4, ell_max_S4,
)

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.linalg import inv


# =============================================================================
# SECTION 1: Input-pin SHA-256 ledger (mandatory for S81+ gates)
# =============================================================================
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FILES = [
    os.path.join(SCRIPT_DIR, "canonical_constants.py"),
    os.path.join(SCRIPT_DIR, "s83_w3_g43_litebird_sigma_nT_reach.npz"),
    os.path.join(SCRIPT_DIR, "s83_w3_g46_tensor_transfer.npz"),
]


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for block in iter(lambda: fh.read(8192), b""):
            h.update(block)
    return h.hexdigest()


input_pins = {os.path.relpath(p, start=os.path.dirname(SCRIPT_DIR)).replace("\\", "/"): _sha256(p)
              for p in INPUT_FILES}
print("=" * 72)
print("S84-W4-37: LB-CMBS4-JOINT-SIGMA-NT")
print("=" * 72)
print("\n-- Input pins (SHA-256, full 64-char) --")
for p, s in input_pins.items():
    print(f"  {p}")
    print(f"    sha256={s}")


# =============================================================================
# SECTION 2: Framework fiducial from G46 (CMB-scale)
# =============================================================================
# Per orchestrator override: n_T = -0.003024 is the G46 eps_H-flow value at CMB.
# r_CMB_fiducial uses the G46 direct transfer output r_CMB = 0.01173 (PASS verdict,
# consistent with working-paper §W4-37 machinery pin). This differs from G43's
# s66-chain r_CMB = 0.0242 (INFO predecessor); the G46 value is the updated
# single-source-of-truth at CMB scale.
#
# Load both candidate r sources and document the choice transparently:

d46 = np.load(os.path.join(SCRIPT_DIR, "s83_w3_g46_tensor_transfer.npz"),
              allow_pickle=True)
r_CMB_g46 = float(d46["r_CMB"])                          # (local) G46 direct transfer output
n_T_CMB_g46 = -0.003024                                  # (local) G46 eps_H-flow fiducial (orchestrator override)

d43 = np.load(os.path.join(SCRIPT_DIR, "s83_w3_g43_litebird_sigma_nT_reach.npz"),
              allow_pickle=True)
r_CMB_g43 = float(d43["r_CMB_fw"])                       # (local) s66-chain r (older)
n_T_CMB_g43 = float(d43["nT_CMB_fw"])                    # (local) s66-chain n_T (same as G46)
sigma_nT_G43_3yr = float(d43["sigma_nT_3yr"])            # (local) G43 LiteBIRD-alone baseline for comparison
sigma_r_G43_3yr = float(d43["sigma_r_3yr"])              # (local)

r_fid = r_CMB_g46                                        # (local) fiducial r (G46 PASS)
n_T_fid = n_T_CMB_g46                                    # (local) fiducial n_T (G46 eps_H-flow)
A_lens_fid = 1.0                                         # (local) lensing amplitude fiducial

print(f"\n-- Framework fiducial (G46 CMB-scale) --")
print(f"  r_fid        = {r_fid:.6e}  (source: s83_w3_g46_tensor_transfer.npz r_CMB)")
print(f"  n_T_fid      = {n_T_fid:.6e}  (orchestrator override; matches G46 eps_H-flow)")
print(f"  A_lens_fid   = {A_lens_fid:.4f}")
print(f"  [cross-check] G43 nT_CMB: {n_T_CMB_g43:.6e}  (agrees)")
print(f"  [note] G43 r (from s66 chain): {r_CMB_g43:.6e}  (older, ~2x G46)")


# =============================================================================
# SECTION 3: B-mode D_l model (tensor signal + lensing residual)
# =============================================================================
# Use same parametric BB shape as G43 (Kamionkowski-Kovetz 2016 fit), extended
# to l<=3000 for CMB-S4. This is a numerical-fit proxy for CAMB output,
# sufficient for Fisher forecasting.


def D_l_BB_tensor(ells, r_val, nT_val, k_pivot=k_pivot_planck):
    """Tensor BB D_l = l(l+1)C_l/(2pi) in uK^2 for power-law P_T proportional to r·(k/k_pivot)^{nT}.

    Shape: reionization bump at l<10, recombination peak at l~80, exponential cutoff near l~400.
    """
    ells_arr = np.asarray(ells, dtype=float)                                  # (local)
    x = ells_arr / 80.0                                                       # (local)
    D_reion = 0.0037 * np.exp(-((ells_arr - 4.0) / 3.0) ** 2)                 # (local)
    D_recomb = 0.022 * x ** 2 / (1.0 + x ** 4.0) * np.exp(-(ells_arr / 400.0) ** 2)  # (local)
    D0 = D_reion + D_recomb
    r_star_Mpc = 144.43                                                       # (local) Planck 2018 decoupling sound horizon
    l_pivot = k_pivot * r_star_Mpc                                            # (local) ~ 7.2
    tilt_factor = (np.maximum(ells_arr, 1.0) / l_pivot) ** nT_val
    return r_val * D0 * tilt_factor


def D_l_BB_lens(ells):
    """Lensing-induced B-mode D_l [uK^2] (parametric Smith+12 fit)."""
    ells_arr = np.asarray(ells, dtype=float)                                  # (local)
    return 5.0e-6 * (ells_arr / 1000.0) ** 0.5 * (1.0 + (ells_arr / 60.0) ** 2) ** (-0.1)  # (local)


# =============================================================================
# SECTION 4: Per-experiment Fisher builder (3x3 on r, n_T, A_lens)
# =============================================================================
def build_fisher_experiment(
    sigma_noise_uKarcmin,      # detector BB noise depth (uK-arcmin)
    beam_fwhm_arcmin,          # effective BB beam FWHM (arcmin)
    f_sky,                     # observed sky fraction
    delens_frac,               # delensing efficiency (e.g. 0.50 => 50% of lensing removed)
    ell_min,
    ell_max,
    r_fid_val,
    nT_fid_val,
    A_lens_fid_val,
    # 5-point centered stencil step sizes per plan
    delta_r=None,
    delta_nT=0.005,
    delta_Al=0.01,
):
    """Return F (3x3), C_tot, C_sig, C_lens_res, N_l, and parameter derivatives.

    Derivative scheme: 5-point centered stencil f'(x) ~= (-f(x+2h) + 8f(x+h) - 8f(x-h) + f(x-2h))/(12h).
    Parameter order: (r, n_T, A_lens).
    Lensing residual model: C_l^lens,res = A_lens · (1 - delens_frac) · C_l^lens,full.
    Noise: Knox with Gaussian beam deconvolution.
    """
    if delta_r is None:
        delta_r = 0.01 * abs(r_fid_val) if r_fid_val != 0.0 else 1e-4        # (local)

    ell = np.arange(ell_min, ell_max + 1)                                    # (local) int multipoles

    # --- Precompute tensor signal D_l at 5 points in r, 5 in n_T; A_lens only affects lensing ---
    def C_of_D(D):
        # Convert D_l = l(l+1)C_l/(2pi) to C_l (uK^2 sr)
        return D * 2.0 * PI / (ell * (ell + 1))                              # (local)

    # Signal at fiducial
    D_sig_fid = D_l_BB_tensor(ell, r_fid_val, nT_fid_val)                    # (local)
    C_sig_fid = C_of_D(D_sig_fid)                                            # (local)

    # Lensing full + residual at fiducial
    D_lens_full = D_l_BB_lens(ell)                                           # (local)
    C_lens_full = C_of_D(D_lens_full)                                        # (local)
    C_lens_res_fid = A_lens_fid_val * (1.0 - delens_frac) * C_lens_full      # (local)

    # Noise (Knox)
    noise_rad = sigma_noise_uKarcmin * (PI / 180.0 / 60.0)                   # (local) uK·rad
    beam_sigma_rad = (beam_fwhm_arcmin * (PI / 180.0 / 60.0)) / np.sqrt(8.0 * np.log(2.0))  # (local)
    N_l = noise_rad ** 2 * np.exp(ell * (ell + 1) * beam_sigma_rad ** 2)     # (local)

    # Total power at fiducial
    C_tot = C_sig_fid + C_lens_res_fid + N_l                                 # (local)

    # --- 5-point centered stencil in r (only C_sig depends on r) ---
    def dC_dr():
        h = delta_r
        D_p2 = D_l_BB_tensor(ell, r_fid_val + 2 * h, nT_fid_val)
        D_p1 = D_l_BB_tensor(ell, r_fid_val + 1 * h, nT_fid_val)
        D_m1 = D_l_BB_tensor(ell, r_fid_val - 1 * h, nT_fid_val)
        D_m2 = D_l_BB_tensor(ell, r_fid_val - 2 * h, nT_fid_val)
        dD = (-D_p2 + 8 * D_p1 - 8 * D_m1 + D_m2) / (12.0 * h)               # (local)
        return C_of_D(dD)                                                     # (local)

    # --- 5-point centered stencil in n_T (only C_sig depends on n_T) ---
    def dC_dnT():
        h = delta_nT
        D_p2 = D_l_BB_tensor(ell, r_fid_val, nT_fid_val + 2 * h)
        D_p1 = D_l_BB_tensor(ell, r_fid_val, nT_fid_val + 1 * h)
        D_m1 = D_l_BB_tensor(ell, r_fid_val, nT_fid_val - 1 * h)
        D_m2 = D_l_BB_tensor(ell, r_fid_val, nT_fid_val - 2 * h)
        dD = (-D_p2 + 8 * D_p1 - 8 * D_m1 + D_m2) / (12.0 * h)               # (local)
        return C_of_D(dD)                                                     # (local)

    # --- 5-point stencil in A_lens (only C_lens_res depends on A_lens, linearly) ---
    # Closed form: dC_total/dA_lens = (1 - delens_frac) · C_lens_full; verify numerically.
    def dC_dAlens():
        h = delta_Al
        C_lens_res_p2 = (A_lens_fid_val + 2 * h) * (1.0 - delens_frac) * C_lens_full
        C_lens_res_p1 = (A_lens_fid_val + 1 * h) * (1.0 - delens_frac) * C_lens_full
        C_lens_res_m1 = (A_lens_fid_val - 1 * h) * (1.0 - delens_frac) * C_lens_full
        C_lens_res_m2 = (A_lens_fid_val - 2 * h) * (1.0 - delens_frac) * C_lens_full
        dC = (-C_lens_res_p2 + 8 * C_lens_res_p1 - 8 * C_lens_res_m1 + C_lens_res_m2) / (12.0 * h)  # (local)
        return dC                                                             # (local)

    dCdr = dC_dr()                                                           # (local)
    dCdnT = dC_dnT()                                                         # (local)
    dCdAl = dC_dAlens()                                                      # (local)

    # Self-consistency check: dC/dA_lens should equal (1-delens)·C_lens_full to machine precision
    dCdAl_closed = (1.0 - delens_frac) * C_lens_full                         # (local)
    max_rel_err = float(np.max(np.abs(dCdAl - dCdAl_closed) /
                               np.maximum(np.abs(dCdAl_closed), 1e-300)))
    assert max_rel_err < 1e-8, f"dC/dA_lens stencil mismatch {max_rel_err:.2e}"

    # --- Fisher 3x3 (Knox weight per multipole) ---
    weight = (2.0 * ell + 1.0) * f_sky / (2.0 * C_tot ** 2)                  # (local)
    deriv = np.stack([dCdr, dCdnT, dCdAl], axis=0)                           # (local) (3, nl)

    F = np.zeros((3, 3))                                                     # (local)
    for i in range(3):
        for j in range(3):
            F[i, j] = np.sum(weight * deriv[i] * deriv[j])

    return {
        "F": F, "ell": ell, "C_sig": C_sig_fid, "C_lens_res": C_lens_res_fid,
        "N_l": N_l, "C_tot": C_tot, "dCdr": dCdr, "dCdnT": dCdnT, "dCdAl": dCdAl,
        "C_lens_full": C_lens_full, "delta_r": delta_r, "delta_nT": delta_nT,
        "delta_Al": delta_Al, "max_rel_err_Alens_stencil": max_rel_err,
    }


# =============================================================================
# SECTION 5: LiteBIRD-only (3-yr) Fisher (with A_lens marginalization)
# =============================================================================
print(f"\n-- LiteBIRD-only 3-yr Fisher (3x3 with A_lens marg) --")
res_LB = build_fisher_experiment(
    sigma_noise_uKarcmin=sigma_LB_3yr_uKarcmin,
    beam_fwhm_arcmin=beam_LB_arcmin,
    f_sky=f_sky_LB,
    delens_frac=delens_LB,
    ell_min=ell_min_LB,
    ell_max=ell_max_LB,
    r_fid_val=r_fid,
    nT_fid_val=n_T_fid,
    A_lens_fid_val=A_lens_fid,
)
F_LB = res_LB["F"]
Cov_LB = inv(F_LB)
sigma_r_LB = float(np.sqrt(Cov_LB[0, 0]))                                    # (local)
sigma_nT_LB = float(np.sqrt(Cov_LB[1, 1]))                                   # (local)
sigma_Al_LB = float(np.sqrt(Cov_LB[2, 2]))                                   # (local)
rho_rnT_LB = float(Cov_LB[0, 1] / (sigma_r_LB * sigma_nT_LB))                # (local)
print(f"  sigma(r)       = {sigma_r_LB:.6f}")
print(f"  sigma(n_T)     = {sigma_nT_LB:.6f}")
print(f"  sigma(A_lens)  = {sigma_Al_LB:.6f}")
print(f"  rho(r, n_T)    = {rho_rnT_LB:+.4f}")


# =============================================================================
# SECTION 6: CMB-S4 only Fisher (full-survey)
# =============================================================================
print(f"\n-- CMB-S4 only full-survey Fisher (3x3 with A_lens marg) --")
res_S4 = build_fisher_experiment(
    sigma_noise_uKarcmin=sigma_S4_uKarcmin,
    beam_fwhm_arcmin=beam_S4_arcmin,
    f_sky=f_sky_S4,
    delens_frac=delens_S4,
    ell_min=ell_min_S4,
    ell_max=ell_max_S4,
    r_fid_val=r_fid,
    nT_fid_val=n_T_fid,
    A_lens_fid_val=A_lens_fid,
)
F_S4 = res_S4["F"]
Cov_S4 = inv(F_S4)
sigma_r_S4 = float(np.sqrt(Cov_S4[0, 0]))                                    # (local)
sigma_nT_S4 = float(np.sqrt(Cov_S4[1, 1]))                                   # (local)
sigma_Al_S4 = float(np.sqrt(Cov_S4[2, 2]))                                   # (local)
rho_rnT_S4 = float(Cov_S4[0, 1] / (sigma_r_S4 * sigma_nT_S4))                # (local)
print(f"  sigma(r)       = {sigma_r_S4:.6f}")
print(f"  sigma(n_T)     = {sigma_nT_S4:.6f}")
print(f"  sigma(A_lens)  = {sigma_Al_S4:.6f}")
print(f"  rho(r, n_T)    = {rho_rnT_S4:+.4f}")


# =============================================================================
# SECTION 7: Joint Fisher = F_LB + F_S4 (independent experiments)
# =============================================================================
print(f"\n-- JOINT Fisher: F_joint = F_LB + F_S4 --")
F_joint = F_LB + F_S4
Cov_joint = inv(F_joint)
sigma_r_joint = float(np.sqrt(Cov_joint[0, 0]))                              # (local)
sigma_nT_joint = float(np.sqrt(Cov_joint[1, 1]))                             # (local)
sigma_Al_joint = float(np.sqrt(Cov_joint[2, 2]))                             # (local)
rho_rnT_joint = float(Cov_joint[0, 1] / (sigma_r_joint * sigma_nT_joint))    # (local)
print(f"  sigma(r)       = {sigma_r_joint:.6f}")
print(f"  sigma(n_T)     = {sigma_nT_joint:.6f}")
print(f"  sigma(A_lens)  = {sigma_Al_joint:.6f}")
print(f"  rho(r, n_T)    = {rho_rnT_joint:+.4f}")

print(f"\n-- Full 3x3 F_joint (r, n_T, A_lens) --")
for row in F_joint:
    print("  [" + ", ".join(f"{v: .4e}" for v in row) + "]")

print(f"\n-- 3x3 Cov_joint = F_joint^{{-1}} --")
for row in Cov_joint:
    print("  [" + ", ".join(f"{v: .4e}" for v in row) + "]")


# =============================================================================
# SECTION 8: Sensitivity heatmap — sigma(n_T)_joint vs delens_S4, delens_LB
# =============================================================================
print(f"\n-- Sensitivity scan: sigma(n_T)_joint over (delens_LB, delens_S4) grid --")
delens_LB_grid = np.linspace(0.30, 0.70, 9)                                  # (local)
delens_S4_grid = np.linspace(0.70, 0.99, 9)                                  # (local)
heatmap = np.zeros((len(delens_LB_grid), len(delens_S4_grid)))               # (local)
for i, dL in enumerate(delens_LB_grid):
    for j, dS in enumerate(delens_S4_grid):
        rLB = build_fisher_experiment(
            sigma_noise_uKarcmin=sigma_LB_3yr_uKarcmin,
            beam_fwhm_arcmin=beam_LB_arcmin, f_sky=f_sky_LB,
            delens_frac=dL,
            ell_min=ell_min_LB, ell_max=ell_max_LB,
            r_fid_val=r_fid, nT_fid_val=n_T_fid, A_lens_fid_val=A_lens_fid,
        )
        rS4 = build_fisher_experiment(
            sigma_noise_uKarcmin=sigma_S4_uKarcmin,
            beam_fwhm_arcmin=beam_S4_arcmin, f_sky=f_sky_S4,
            delens_frac=dS,
            ell_min=ell_min_S4, ell_max=ell_max_S4,
            r_fid_val=r_fid, nT_fid_val=n_T_fid, A_lens_fid_val=A_lens_fid,
        )
        F_j = rLB["F"] + rS4["F"]
        heatmap[i, j] = float(np.sqrt(inv(F_j)[1, 1]))
print(f"  heatmap min={heatmap.min():.4f}  max={heatmap.max():.4f}")


# =============================================================================
# SECTION 9: Verdict
# =============================================================================
sigma_nT_joint_3yr = sigma_nT_joint                                          # (local) output scalar
threshold_pass = 0.04                                                        # (local) PASS gate (plan §W4-37)
threshold_info = 0.06                                                        # (local) INFO gate

if sigma_nT_joint_3yr <= threshold_pass:
    verdict = "PASS"
elif sigma_nT_joint_3yr <= threshold_info:
    verdict = "INFO"
else:
    verdict = "FAIL"

print("\n" + "=" * 72)
print("VERDICT")
print("=" * 72)
print(f"  sigma(n_T)_joint_3yr            = {sigma_nT_joint_3yr:.6f}")
print(f"  PASS threshold (<=)             = {threshold_pass:.3f}")
print(f"  INFO threshold (<=)             = {threshold_info:.3f}")
print(f"  FAIL threshold (>)              = {threshold_info:.3f}")
print(f"  sigma(n_T) G43 LiteBIRD alone   = {sigma_nT_G43_3yr:.6f}  (S83 baseline; re-derived: {sigma_nT_LB:.6f})")
print(f"  Improvement factor (LB-alone -> joint): {sigma_nT_G43_3yr / sigma_nT_joint_3yr:.2f}x")
print(f"  Verdict: {verdict}")


# =============================================================================
# SECTION 10: Data save
# =============================================================================
save_path = os.path.join(SCRIPT_DIR, "s84_w4_lb_cmbs4_joint_sigma_nt.npz")
np.savez(save_path,
         # Fiducial
         r_fid=r_fid,
         n_T_fid=n_T_fid,
         A_lens_fid=A_lens_fid,
         # Per-experiment Fisher matrices
         F_LB=F_LB, Cov_LB=Cov_LB,
         F_S4=F_S4, Cov_S4=Cov_S4,
         F_joint=F_joint, Cov_joint=Cov_joint,
         # Marginalized 1-sigmas
         sigma_r_LB=sigma_r_LB, sigma_nT_LB=sigma_nT_LB, sigma_Al_LB=sigma_Al_LB, rho_rnT_LB=rho_rnT_LB,
         sigma_r_S4=sigma_r_S4, sigma_nT_S4=sigma_nT_S4, sigma_Al_S4=sigma_Al_S4, rho_rnT_S4=rho_rnT_S4,
         sigma_r_joint=sigma_r_joint, sigma_nT_joint=sigma_nT_joint,
         sigma_Al_joint=sigma_Al_joint, rho_rnT_joint=rho_rnT_joint,
         sigma_nT_joint_3yr=sigma_nT_joint_3yr,
         # Comparison baseline
         sigma_nT_G43_3yr=sigma_nT_G43_3yr,
         sigma_r_G43_3yr=sigma_r_G43_3yr,
         # Heatmap
         delens_LB_grid=delens_LB_grid, delens_S4_grid=delens_S4_grid,
         heatmap_sigma_nT=heatmap,
         # Detector specs
         sigma_LB_3yr_uKarcmin=sigma_LB_3yr_uKarcmin, beam_LB_arcmin=beam_LB_arcmin,
         f_sky_LB=f_sky_LB, delens_LB=delens_LB,
         ell_min_LB=ell_min_LB, ell_max_LB=ell_max_LB,
         sigma_S4_uKarcmin=sigma_S4_uKarcmin, beam_S4_arcmin=beam_S4_arcmin,
         f_sky_S4=f_sky_S4, delens_S4=delens_S4,
         ell_min_S4=ell_min_S4, ell_max_S4=ell_max_S4,
         # Verdict
         threshold_pass=threshold_pass, threshold_info=threshold_info,
         verdict=verdict,
         gate_name="S84-LB-CMBS4-JOINT-SIGMA-NT",
         input_pins=json.dumps(input_pins),
         )
print(f"\nData saved: {save_path}")


# =============================================================================
# SECTION 11: Closure SHA-256 — canonical ordered input-pin map
# =============================================================================
closure_map = {
    "gate": "S84-LB-CMBS4-JOINT-SIGMA-NT",
    "inputs": input_pins,
    "sigma_nT_joint_3yr": f"{sigma_nT_joint_3yr:.10e}",
    "sigma_r_joint":      f"{sigma_r_joint:.10e}",
    "sigma_Al_joint":     f"{sigma_Al_joint:.10e}",
    "rho_rnT_joint":      f"{rho_rnT_joint:.10e}",
    "verdict": verdict,
    "scheme": "Fisher 3-param marginalized",
    "convention": "Planck 2018 n_T sign",
    "r_fid":            f"{r_fid:.10e}",
    "nT_fid":           f"{n_T_fid:.10e}",
    "Al_fid":           f"{A_lens_fid:.10e}",
    "threshold_pass":   f"{threshold_pass:.6f}",
    "threshold_info":   f"{threshold_info:.6f}",
    "sigma_LB_uKarcmin": f"{sigma_LB_3yr_uKarcmin:.6f}",
    "f_sky_LB":          f"{f_sky_LB:.6f}",
    "delens_LB":         f"{delens_LB:.6f}",
    "ell_LB":            f"{ell_min_LB}-{ell_max_LB}",
    "sigma_S4_uKarcmin": f"{sigma_S4_uKarcmin:.6f}",
    "f_sky_S4":          f"{f_sky_S4:.6f}",
    "delens_S4":         f"{delens_S4:.6f}",
    "ell_S4":            f"{ell_min_S4}-{ell_max_S4}",
}
audit_sha = hashlib.sha256(
    json.dumps(closure_map, sort_keys=True).encode()).hexdigest()
print(f"\nAudit SHA-256 (closure over input-pin map): {audit_sha}")

# Content SHA-256: SHA of the output .npz content
content_sha = _sha256(save_path)
print(f"Content SHA-256 (output .npz): {content_sha}")


# =============================================================================
# SECTION 12: Plot — 2-panel (BB budget + sigma(n_T) heatmap vs delens_S4, delens_LB)
# =============================================================================
fig = plt.figure(figsize=(14, 5.8))

# Panel A: BB spectrum stack (LB + S4 noise vs signal + lensing-residual)
ax1 = fig.add_subplot(1, 2, 1)
ell_plot_LB = res_LB["ell"]
ell_plot_S4 = res_S4["ell"]
D_sig_LB = D_l_BB_tensor(ell_plot_LB, r_fid, n_T_fid)                        # (local)
D_sig_S4 = D_l_BB_tensor(ell_plot_S4, r_fid, n_T_fid)                        # (local)
D_lens_full_LB = D_l_BB_lens(ell_plot_LB)                                    # (local)
D_lens_full_S4 = D_l_BB_lens(ell_plot_S4)                                    # (local)
D_lens_res_LB = A_lens_fid * (1.0 - delens_LB) * D_lens_full_LB              # (local)
D_lens_res_S4 = A_lens_fid * (1.0 - delens_S4) * D_lens_full_S4              # (local)
# noise back to D_l = l(l+1)C_l/(2pi)
N_l_LB = res_LB["N_l"]
N_l_S4 = res_S4["N_l"]
D_noise_LB = N_l_LB * ell_plot_LB * (ell_plot_LB + 1) / (2.0 * PI)           # (local)
D_noise_S4 = N_l_S4 * ell_plot_S4 * (ell_plot_S4 + 1) / (2.0 * PI)           # (local)

# Union signal curve for plotting
ell_all = np.arange(2, 3001)
D_sig_all = D_l_BB_tensor(ell_all, r_fid, n_T_fid)
ax1.loglog(ell_all, D_sig_all, 'C0-', lw=2,
           label=f'Framework tensor BB (r={r_fid:.4f}, n_T={n_T_fid:.4f})')
ax1.loglog(ell_plot_LB, D_lens_res_LB, color='gray', ls='--', lw=1.2,
           label=f'LB lensing residual ({(1 - delens_LB) * 100:.0f}%)')
ax1.loglog(ell_plot_S4, D_lens_res_S4, color='black', ls='--', lw=1.2,
           label=f'S4 lensing residual ({(1 - delens_S4) * 100:.0f}%)')
ax1.loglog(ell_plot_LB, D_noise_LB, 'C3-.', lw=1.2, label='LiteBIRD noise (3 yr)')
ax1.loglog(ell_plot_S4, D_noise_S4, 'C1-.', lw=1.2, label='CMB-S4 noise')
ax1.axvspan(ell_min_LB, ell_max_LB, alpha=0.08, color='C3', label='LB l range')
ax1.axvspan(ell_min_S4, ell_max_S4, alpha=0.08, color='C1', label='S4 l range')
ax1.set_xlim(2, 3000)
ax1.set_ylim(1e-8, 1e-1)
ax1.set_xlabel(r'Multipole $\ell$', fontsize=11)
ax1.set_ylabel(r'$D_\ell^{BB}\;[\mu \mathrm{K}^2]$', fontsize=11)
ax1.set_title('LB + CMB-S4 BB Budget', fontsize=11)
ax1.grid(True, which='both', alpha=0.3)
ax1.legend(fontsize=8, loc='lower right', ncol=2)

# Panel B: heatmap sigma(n_T) vs (delens_LB, delens_S4)
ax2 = fig.add_subplot(1, 2, 2)
im = ax2.pcolormesh(delens_S4_grid, delens_LB_grid, heatmap,
                    cmap='viridis_r', shading='nearest')
cbar = plt.colorbar(im, ax=ax2, label=r'$\sigma(n_T)_\mathrm{joint}$')
# Contours for PASS / INFO thresholds
cs_pass = ax2.contour(delens_S4_grid, delens_LB_grid, heatmap,
                      levels=[threshold_pass], colors='lime', linewidths=2.0)
ax2.clabel(cs_pass, fmt={threshold_pass: 'PASS <=%.2f' % threshold_pass}, fontsize=9)
cs_info = ax2.contour(delens_S4_grid, delens_LB_grid, heatmap,
                      levels=[threshold_info], colors='orange', linewidths=2.0)
ax2.clabel(cs_info, fmt={threshold_info: 'INFO <=%.2f' % threshold_info}, fontsize=9)
# Mark baseline (delens_LB=0.50, delens_S4=0.90)
ax2.plot([delens_S4], [delens_LB], 'w*', ms=18, mec='k', mew=1.2,
         label=f'Baseline: sigma={sigma_nT_joint_3yr:.3f}')
ax2.set_xlabel(r'CMB-S4 delensing fraction', fontsize=11)
ax2.set_ylabel(r'LiteBIRD delensing fraction', fontsize=11)
ax2.set_title(r'$\sigma(n_T)_\mathrm{joint}$: LB+S4 Fisher sum', fontsize=11)
ax2.legend(fontsize=9, loc='upper right')

plt.tight_layout()
plot_path = os.path.join(SCRIPT_DIR, "s84_w4_lb_cmbs4_joint_sigma_nt.png")
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"Plot saved: {plot_path}")
plt.close()


# =============================================================================
# SECTION 13: Verdict-line append (S84 DUAL-SHA canonical form)
# =============================================================================
verdict_line = (
    f"S84-LB-CMBS4-JOINT-SIGMA-NT: {verdict} -- "
    f"value=sigma_nT_joint_3yr={sigma_nT_joint_3yr:.6f} "
    f"scheme=Fisher_3-param_marginalized "
    f"convention=Planck_2018_n_T_sign "
    f"L_max=N/A "
    f"audit_sha256={audit_sha} "
    f"content_sha256={content_sha}\n"
)

verdicts_path = os.path.join(SCRIPT_DIR, "s84_gate_verdicts.txt")
with open(verdicts_path, "a", encoding="utf-8") as fh:
    fh.write(verdict_line)
print(f"\nVerdict appended to {verdicts_path}:")
print(f"  {verdict_line.rstrip()}")


# =============================================================================
# SECTION 14: 4-tuple tag
# =============================================================================
tag = (f"(value=sigma_nT_joint_3yr={sigma_nT_joint_3yr:.6f}, "
       f"scheme=Fisher 3-param marginalized, "
       f"convention=Planck 2018 n_T sign, "
       f"L_max=N/A)")
print(f"\n4-tuple: {tag}")
print("\nS84-W4-37: COMPLETE.")
