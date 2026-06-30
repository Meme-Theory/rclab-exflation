"""
S73B DESI-DR3-PREP-73B: Consolidated pre-registered prediction bundle for DESI DR3.

This is not a new computation. It collects the full pre-registered prediction suite
from S67 (w_0 = -0.918, Volovik), S68 (w_a = 0, four-fold lock), S70 (BAO, SNe, RSD),
and S73B W2-D (Gibbs-Duhem: w_0 = -0.917 algebraic anchor) into a single .npz for
the DR3 response matrix. No adjustable parameters. Frozen as of 2026-04-10.
"""

import numpy as np
from canonical_constants import w0_FW

# Framework prediction bundle (S67 + S68 + S73B W2-D anchor)
w0_fw = w0_FW                     # -0.918 (Volovik relaxation, S67 / Gibbs-Duhem S73B) # (local)
w0_fw_sigma_scheme = 0.06         # Scheme variation from S72 workshop A-Q2 # (local)
wa_fw = 0.0                       # Four-fold locked: GGE integrability + Josephson + texture + therm barrier # (local)
wa_fw_sigma = 0.0                 # Exact, no internal flexibility (S68) # (local)

# S73B W2-D Gibbs-Duhem algebraic anchor
w_GGE_S73B = -0.4076492063533559  # Physical multicomponent w (hidden GGE) # (local)
w_combined_S73B = -0.9172266785396007  # Volovik partition scheme-consistent reconciliation # (local)
discrepancy_after_S73B = 0.0      # Zubarev-Keldysh reconciled # (local)

# DESI DR3 scenarios (from S60 DR3-PREREGISTER-60, updated S68/S70)
scenario_labels = np.array(['A', 'B', 'C'])
scenario_description = np.array([
    'Confirms DR2 (DESY5 systematics dominate)',
    'Moves toward LCDM (partial regression)',
    'More dynamical (DR2 trend amplified)',
])
scenario_w0 = np.array([-0.75, -0.90, -0.65])
scenario_wa = np.array([-0.73, -0.30, -1.00])

# Pre-registered significance at 5x DR1 statistics
sig_fw_scenarios = np.array([3.91, 2.06, 6.33])    # from S70 (S68 DR3 errors) # (local)
sig_lcdm_scenarios = np.array([6.25, 2.12, 37.1])  # from S70 (S68 DR3 errors) # (local)

# Decision thresholds (pre-registered S60)
wa_excluded_at = -0.530           # < -0.53 at 3-sigma = framework excluded # (local)
wa_survival_at = -0.350           # > -0.35 = framework survives # (local)

# BAO predictions (from S70 s70_desi_dr3_update.npz)
s70 = np.load('s70_desi_dr3_update.npz', allow_pickle=True)
z_eff = s70['z_eff']
tracer_labels = s70['tracer_labels']
DM_rd_FW = s70['DM_rd_FW']
DH_rd_FW = s70['DH_rd_FW']
DM_rd_LCDM = s70['DM_rd_LCDM']
DH_rd_LCDM = s70['DH_rd_LCDM']
DM_rd_obs_dr2 = s70['DM_rd_obs']
DM_rd_err_dr2 = s70['DM_rd_err']
DM_rd_err_dr3_projected = s70['DM_rd_err_dr3']
DH_rd_obs_dr2 = s70['DH_rd_obs']
DH_rd_err_dr2 = s70['DH_rd_err']

# Derived D_V/r_d = (z * D_M^2 * D_H)^(1/3) / r_d
def DV_rd(DM_rd, DH_rd, z):
    return (z * DM_rd**2 * DH_rd) ** (1.0 / 3.0)

DV_rd_FW = DV_rd(DM_rd_FW, DH_rd_FW, z_eff)
DV_rd_LCDM = DV_rd(DM_rd_LCDM, DH_rd_LCDM, z_eff)

# Current (DR2) chi^2 from S70
chi2_DM_fw_dr2 = float(s70['chi2_DM_fw'])
chi2_dof_DM_fw_dr2 = float(s70['chi2_dof_DM_fw'])
chi2_DM_fw_dr3_projected = float(s70['chi2_DM_fw_dr3'])
chi2_dof_DM_fw_dr3_projected = float(s70['chi2_dof_DM_fw_dr3'])

# SNe Ia chi^2/dof (from S70 full-cov Pantheon+)
pan = np.load('s70_full_cov_pantheon.npz', allow_pickle=True)
chi2_dof_sne_FW_full = float(pan['chi2_dof_FW_full'])
chi2_dof_sne_LCDM_full = float(pan['chi2_dof_LCDM_full'])
delta_chi2_sne_FW_minus_LCDM = float(pan['delta_chi2_full'])  # -7.82 (FW preferred) # (local)
N_SNe = int(pan['N_valid'])

# RSD chi^2 (S70)
chi2_FW_fsig8_full = float(s70['delta_chi2_fsig8_full'])  # -0.609 FW preferred # (local)

# Sensitivity of w_0 tension to SN calibration systematic
# From S72 Mack audit II: ~0.08 in w_0 from Pantheon+ vs DESY5 vs Union3 choice
sn_calibration_systematic_w0 = 0.08  # 1-sigma equivalent shift # (local)

# Current tensions
w0_dr2_central = -0.752  # (local)
w0_dr2_sigma = 0.057  # (local)
wa_dr2_central = -0.73  # (local)
wa_dr2_sigma = 0.25  # (local)

tension_w0_current = abs(w0_fw - w0_dr2_central) / np.sqrt(w0_dr2_sigma**2 + w0_fw_sigma_scheme**2)  # (local)
tension_wa_current = abs(wa_fw - wa_dr2_central) / wa_dr2_sigma  # (local)

# After SN systematic marginalization (add 0.08 in quadrature to w_0 uncertainty)
w0_sigma_with_syst = np.sqrt(w0_dr2_sigma**2 + w0_fw_sigma_scheme**2 + sn_calibration_systematic_w0**2)  # (local)
tension_w0_with_syst = abs(w0_fw - w0_dr2_central) / w0_sigma_with_syst  # (local)

print("=" * 70)
print("S73B DESI-DR3-PREP-73B: Pre-Registered Prediction Bundle")
print("=" * 70)
print()
print(f"Framework prediction (FROZEN 2026-04-10):")
print(f"  w_0 = {w0_fw} +/- {w0_fw_sigma_scheme} (scheme variation)")
print(f"  w_a = {wa_fw} (exact, four-fold locked)")
print(f"  Gibbs-Duhem algebraic anchor (S73B W2-D): w_combined = {w_combined_S73B:.6f}")
print()
print(f"Current (DR2 DESY5):")
print(f"  w_0 = {w0_dr2_central} +/- {w0_dr2_sigma}  --> tension {tension_w0_current:.2f}-sigma")
print(f"  w_a = {wa_dr2_central} +/- {wa_dr2_sigma}  --> tension {tension_wa_current:.2f}-sigma")
print()
print(f"With SN calibration systematic ({sn_calibration_systematic_w0} in w_0):")
print(f"  w_0 tension: {tension_w0_with_syst:.2f}-sigma (from {tension_w0_current:.2f}-sigma)")
print()
print("Pre-registered DR3 scenarios:")
for lab, desc, w0s, was, sfw, slc in zip(scenario_labels, scenario_description,
                                            scenario_w0, scenario_wa,
                                            sig_fw_scenarios, sig_lcdm_scenarios):
    print(f"  {lab}: {desc}")
    print(f"     w_0={w0s}, w_a={was}   FW tension={sfw}-sig, LCDM tension={slc}-sig")
print()
print(f"Decision rule:")
print(f"  w_a > {wa_survival_at}  -->  framework SURVIVES")
print(f"  w_a < {wa_excluded_at}  at 3-sigma  -->  framework EXCLUDED")
print()
print(f"BAO predictions at {len(z_eff)} DESI bins (D_V/r_d):")
for i, (z, lab, dv_fw, dv_lcdm) in enumerate(zip(z_eff, tracer_labels, DV_rd_FW, DV_rd_LCDM)):
    print(f"  z={z:.3f} {lab:12s}: FW={dv_fw:.3f}  LCDM={dv_lcdm:.3f}  delta={dv_fw-dv_lcdm:+.3f}")
print()
print(f"SNe Pantheon+ (full cov, {N_SNe} SNe):")
print(f"  chi^2/dof (FW)   = {chi2_dof_sne_FW_full:.4f}")
print(f"  chi^2/dof (LCDM) = {chi2_dof_sne_LCDM_full:.4f}")
print(f"  Delta chi^2 = {delta_chi2_sne_FW_minus_LCDM:.2f}  (FW preferred)")
print()
print(f"BAO D_M/r_d (DR2 current):")
print(f"  chi^2/dof (FW) = {chi2_dof_DM_fw_dr2:.3f}")
print()
print("GATE: DESI-DR3-PREP-73B")
print("VERDICT: INFO (strategic pre-registration, not a computation)")

np.savez(
    's73b_desi_dr3_predictions.npz',
    # Framework prediction
    w0_fw=w0_fw,
    w0_fw_sigma_scheme=w0_fw_sigma_scheme,
    wa_fw=wa_fw,
    wa_fw_sigma=wa_fw_sigma,
    # S73B W2-D anchor
    w_GGE_S73B=w_GGE_S73B,
    w_combined_S73B=w_combined_S73B,
    discrepancy_after_S73B=discrepancy_after_S73B,
    # DESI DR3 scenarios
    scenario_labels=scenario_labels,
    scenario_description=scenario_description,
    scenario_w0=scenario_w0,
    scenario_wa=scenario_wa,
    sig_fw_scenarios=sig_fw_scenarios,
    sig_lcdm_scenarios=sig_lcdm_scenarios,
    wa_excluded_at=wa_excluded_at,
    wa_survival_at=wa_survival_at,
    # BAO predictions
    z_eff=z_eff,
    tracer_labels=tracer_labels,
    DM_rd_FW=DM_rd_FW,
    DH_rd_FW=DH_rd_FW,
    DV_rd_FW=DV_rd_FW,
    DM_rd_LCDM=DM_rd_LCDM,
    DH_rd_LCDM=DH_rd_LCDM,
    DV_rd_LCDM=DV_rd_LCDM,
    DM_rd_obs_dr2=DM_rd_obs_dr2,
    DM_rd_err_dr2=DM_rd_err_dr2,
    DM_rd_err_dr3_projected=DM_rd_err_dr3_projected,
    DH_rd_obs_dr2=DH_rd_obs_dr2,
    DH_rd_err_dr2=DH_rd_err_dr2,
    chi2_DM_fw_dr2=chi2_DM_fw_dr2,
    chi2_dof_DM_fw_dr2=chi2_dof_DM_fw_dr2,
    chi2_DM_fw_dr3_projected=chi2_DM_fw_dr3_projected,
    chi2_dof_DM_fw_dr3_projected=chi2_dof_DM_fw_dr3_projected,
    # SNe Ia
    chi2_dof_sne_FW_full=chi2_dof_sne_FW_full,
    chi2_dof_sne_LCDM_full=chi2_dof_sne_LCDM_full,
    delta_chi2_sne_FW_minus_LCDM=delta_chi2_sne_FW_minus_LCDM,
    N_SNe=N_SNe,
    # RSD
    chi2_FW_fsig8_full=chi2_FW_fsig8_full,
    # Systematics
    sn_calibration_systematic_w0=sn_calibration_systematic_w0,
    tension_w0_current=tension_w0_current,
    tension_wa_current=tension_wa_current,
    tension_w0_with_syst=tension_w0_with_syst,
    # Current DR2 central values
    w0_dr2_central=w0_dr2_central,
    w0_dr2_sigma=w0_dr2_sigma,
    wa_dr2_central=wa_dr2_central,
    wa_dr2_sigma=wa_dr2_sigma,
    # Metadata
    gate_name=np.array(['DESI-DR3-PREP-73B']),
    gate_verdict=np.array(['INFO']),
    gate_detail=np.array(['Pre-registered prediction bundle for DESI DR3 (2026-2027). Frozen 2026-04-10. w_0 = -0.918 +/- 0.06, w_a = 0 exact. Decision rule: w_a > -0.35 survives, w_a < -0.53 at 3-sigma excluded. SN calibration systematic ~0.08 in w_0 is the primary controllable uncertainty.']),
    frozen_date=np.array(['2026-04-10']),
)
print()
print("Bundle written: s73b_desi_dr3_predictions.npz")
