"""
s45_cc_gap_update.py — CC Gap Update with ALL S45 Results (CC-GAP-UPDATE-45)

Consolidates all S45 CC-relevant computations into an updated gap picture.
Inputs: 10 NPZ files from S44-S45 + canonical_constants.py.
Output: Summary to stdout (written into W5-R1 of working paper).

Author: Gen-Physicist
Session: 45
"""
import numpy as np
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
import canonical_constants as CC

# Load all relevant NPZ files
DATA = os.path.dirname(__file__)
s44_gap = np.load(os.path.join(DATA, 's44_cc_gap_resolved.npz'), allow_pickle=True)
s45_qkk = np.load(os.path.join(DATA, 's45_qtheory_kk.npz'), allow_pickle=True)
s45_qbcs = np.load(os.path.join(DATA, 's45_qtheory_bcs.npz'), allow_pickle=True)
s45_usa = np.load(os.path.join(DATA, 's45_unexpanded_sa.npz'), allow_pickle=True)
s45_at = np.load(os.path.join(DATA, 's45_analytic_torsion.npz'), allow_pickle=True)
s45_tt = np.load(os.path.join(DATA, 's45_truncated_torsion.npz'), allow_pickle=True)
s45_ed = np.load(os.path.join(DATA, 's45_euler_deficit.npz'), allow_pickle=True)
s45_hc = np.load(os.path.join(DATA, 's45_cc_hierarchy_cubed.npz'), allow_pickle=True)
s45_rg = np.load(os.path.join(DATA, 's45_running_gn.npz'), allow_pickle=True)

rho_obs = 2.7e-47  # GeV^4, canonical rounding
M_KK = float(s44_gap['M_KK_used'])

print("=" * 72)
print("CC GAP UPDATE — ALL S45 RESULTS")
print("=" * 72)

# I. Starting Point (unchanged)
rho_spec = float(s44_gap['rho_spec'])
gap_spec = np.log10(rho_spec / rho_obs)
print(f"\nI. STARTING POINT (unchanged from S44)")
print(f"   M_KK (gravity)     = {M_KK:.4e} GeV")
print(f"   rho_SA             = {rho_spec:.4e} GeV^4")
print(f"   Gap (spectral)     = {gap_spec:.2f} orders")

# II. Chain A (unchanged)
orders_tl = float(s44_gap['orders_poly_to_log'])
orders_eih = float(s44_gap['orders_eih'])
rho_singlet = float(s44_gap['rho_singlet'])
gap_honest = np.log10(rho_singlet / rho_obs)
print(f"\nII. CHAIN A: TL + EIH (S44, UNCHANGED)")
print(f"   Poly -> TL:        -{orders_tl:.3f} orders")
print(f"   EIH singlet:       -{orders_eih:.3f} orders")
print(f"   Total suppression: -{orders_tl + orders_eih:.3f} orders")
print(f"   rho_singlet        = {rho_singlet:.3e} GeV^4")
print(f"   HONEST GAP         = {gap_honest:.2f} orders  [UNCHANGED]")

# III. S45 New Results
print(f"\nIII. S45 NEW RESULTS")

# A. Q-Theory BCS
tau_star_vac = float(s45_qkk['tau_star'])
tau_star_fb = float(s45_qbcs['tau_star_flatband'])
tau_star_uni = float(s45_qbcs['tau_star_uniform'])
tau_star_multi = float(s45_qbcs['tau_star_multi'])
tau_fold = float(s45_qbcs['tau_fold'])

print(f"\n  A. Q-THEORY BCS SELF-TUNING (Q-THEORY-BCS-45 = PASS)")
print(f"     S43 crossing:      tau* = 1.230   (polynomial full spectrum)")
print(f"     S45 vacuum (W1):   tau* = {tau_star_vac:.3f}   (TL singlet)")
print(f"     S45 BCS uniform:   tau* = {tau_star_uni:.3f}   (genuine, outside gate)")
print(f"     S45 BCS multi:     tau* = {tau_star_multi:.3f}   (genuine, inside domain)")
print(f"     S45 BCS flatband:  tau* = {tau_star_fb:.4f}  (PASS, 10.2% from fold)")
print(f"     Fold:              tau  = {tau_fold:.3f}")
print(f"     Improvement S43->S45: {1.230/tau_star_fb:.1f}x")

# Residual at fold vs at crossing
rho_gs_fb = float(s45_qbcs['rho_gs_fold_flatband'])
rho_gs_fb_GeV4 = abs(rho_gs_fb) * M_KK**4 / (16 * np.pi**2)
gap_qtheory_fold = np.log10(rho_gs_fb_GeV4 / rho_obs)
print(f"\n     Residual AT FOLD:   rho_gs = {rho_gs_fb:.4f} M_KK^4 = {rho_gs_fb_GeV4:.3e} GeV^4")
print(f"     Gap at fold:        {gap_qtheory_fold:.1f} orders")
print(f"     Residual AT tau*:   rho_gs = 0 by construction (self-tuning)")
print(f"     Gap at tau*:        0 orders (if fold IS the equilibrium)")

# B. Taylor exactness
taylor_err = float(s45_usa['taylor_20term_error'])
print(f"\n  B. TAYLOR EXPANSION EXACTNESS (UNEXPANDED-SA-45 = FAIL)")
print(f"     20-term Taylor relative error: {taylor_err:.2e}")
print(f"     Structural theorem: polynomial expansion is EXACT for finite spectrum")
print(f"     This is the 29th spectral action equilibrium closure")
print(f"     Implication: CC problem is entirely in cutoff function f, not in spectrum")

# C. Torsion
T_full_log10 = float(s45_at['log10_T_fold'])
T_singlet = float(s45_tt['T_singlet'])
T_singlet_log10 = float(s45_tt['log10_T_singlet'])
rho_st_grav = float(s45_tt['rho_singlet_grav'])
gap_st = float(s45_tt['log10_rho_over_obs_grav'])

print(f"\n  C. ANALYTIC TORSION (ANALYTIC-TORSION-45 + TRUNCATED-TORSION-45)")
print(f"     Full T(SU(3)):     10^{{{T_full_log10:.0f}}}  [ARTIFACT — extensive in N]")
print(f"     Singlet T:         {T_singlet:.4f}    [O(1) — physical bound]")
print(f"     log10(T_singlet):  {T_singlet_log10:.3f}")
print(f"     Scaling: log10 T ~ N^{{{float(s45_tt['trunc_scaling_alpha']):.2f}}} (EIH weights)")
print(f"     Full torsion is extensive artifact; singlet is meaningful")
print(f"     Singlet rho_torsion: {rho_st_grav:.3e} GeV^4, gap = {gap_st:.1f} orders")
print(f"     Physical torsion does NOT amplify — T < 1 for singlet sector")

# D. Euler deficit
deficit_over_Econd = float(s45_ed['deficit_over_Econd'])
print(f"\n  D. EULER DEFICIT DISPROOF (EULER-DEFICIT-45 = INFO)")
print(f"     S44 claim: deficit = |E_cond|")
print(f"     S45 result: deficit = {deficit_over_Econd:.4f} * |E_cond|")
print(f"     DISPROVED: was ensemble artifact, not exact identity")
print(f"     Deficit is NOT a CC suppression mechanism")

# E. Hierarchy cubed
ratio = float(s45_hc['ratio_gap_over_36'])
print(f"\n  E. CC-HIERARCHY CUBED (CC-HIERARCHY-CUBED-45 = COINCIDENCE)")
print(f"     gap / 36 = {ratio:.3f} (~ 3)")
print(f"     Moment ratios A_0/A_2 = {float(s45_hc['R_spec_02']):.4f}, A_2/A_4 = {float(s45_hc['R_spec_24']):.4f}")
print(f"     Both O(1), not 10^36. The approximate factor-3 is numerological")

# F. Heat kernel
print(f"\n  F. HEAT KERNEL AUDIT (HEAT-KERNEL-AUDIT-45)")
print(f"     a_2 Seeley-DeWitt: 30-50% truncation error at p+q <= 5")
print(f"     Spectral dimension d_s: scale-dependent artifact on finite spectrum")
print(f"     Torsion: extensive artifact (resolved above)")
print(f"     Valid quantities: forward moments A_{{2n}}, zeta sums Z_{{2n}}, trace-log")
print(f"     Approximate: a_2, d_s (converge slowly with truncation)")
print(f"     Artifact: torsion, short-time heat kernel asymptotics")

# G. Running G_N
gn_ratio = float(s45_rg['ratio_at_fold'])
gn_var = float(s45_rg['total_variation'])
print(f"\n  G. RUNNING G_N(tau) (RUNNING-GN-45 = INFO)")
print(f"     G_N^Sak(fold) / G_N^obs = {gn_ratio:.4f}")
print(f"     Total variation across [0, 0.5]: {gn_var*100:.1f}%")
print(f"     Monotonic: {bool(s45_rg['sak_monotone'])}")
print(f"     G_N is stable during transit — no dynamical CC contribution from G_N drift")

# IV. Updated summary table
print(f"\n{'=' * 72}")
print(f"IV. UPDATED SUMMARY TABLE")
print(f"{'=' * 72}")

print(f"\n{'Chain/Route':<40} {'Gap (orders)':>12} {'Status':>12} {'Change':>10}")
print(f"{'-'*40} {'-'*12} {'-'*12} {'-'*10}")
print(f"{'A: TL + EIH (honest)':<40} {'110.5':>12} {'COMPUTED':>12} {'unchanged':>10}")
print(f"{'B: Jacobson + EIH':<40} {'106.7':>12} {'COMPUTED':>12} {'unchanged':>10}")
print(f"{'C: Holographic':<40} {'107.4':>12} {'FAIL':>12} {'unchanged':>10}")
print(f"{'D: q-Theory vacuum (W1-R1)':<40} {'111.5':>12} {'INFO':>12} {'from S44':>10}")
print(f"{'D2: q-Theory BCS flatband (W2-R5)':<40} {'0 at tau*':>12} {'PASS':>12} {'NEW':>10}")
print(f"{'E: Torsion (full)':<40} {'AMPLIFIES':>12} {'ARTIFACT':>12} {'RESOLVED':>10}")
print(f"{'E2: Torsion (singlet)':<40} {'112.1':>12} {'INFO':>12} {'NEW':>10}")
print(f"{'F: Euler deficit':<40} {'--':>12} {'DISPROVED':>12} {'NEW':>10}")
print(f"{'G: 3*hierarchy':<40} {'--':>12} {'COINCIDENCE':>12} {'NEW':>10}")

# V. Net position
print(f"\n{'=' * 72}")
print(f"V. NET POSITION")
print(f"{'=' * 72}")

print(f"""
The CC balance sheet has TWO qualitatively different regimes after S45:

REGIME 1: Suppression-chain approach (Chain A)
  Starting gap: 117.2 orders
  Best proven suppression: -6.76 orders (TL + EIH)
  Honest residual: 110.5 orders
  STATUS: UNCHANGED. No S45 result modifies the structural suppression factors.
  Every S45 attempt to find additional suppression factors FAILED:
    - Unexpanded SA: exact at finite truncation (29th closure)
    - Torsion: amplifies (full) or neutral (singlet T=0.15)
    - Euler deficit: disproved
    - Hierarchy cubed: coincidence
  The suppression-chain approach is at a structural floor.

REGIME 2: Thermodynamic self-tuning (q-theory + BCS)
  Mechanism: Volovik Gibbs-Duhem condition rho(q_0) = 0 at equilibrium
  S43: crossing at tau* = 1.23 (outside domain)
  S45 vacuum: crossing at tau* = 0.472 (inside domain, outside gate)
  S45 BCS flatband: crossing at tau* = 0.209 (PASS, 10.2% from fold)
  Residual at crossing: ZERO by construction
  STATUS: FIRST CC MECHANISM PASS IN PROJECT HISTORY

  The q-theory does not suppress the CC. It CANCELS it at the self-tuned
  equilibrium point. If tau_fold IS the equilibrium (tau* = tau_fold),
  then rho_vac = 0 identically. The residual CC would come from the
  displacement |tau* - tau_fold| = 0.019 in the quadratic expansion.

RESIDUAL ESTIMATE from q-theory displacement:
""")

# Compute residual from displacement
dtau = abs(tau_star_fb - tau_fold)
# The q-theory gives rho ~ c2 * (tau - tau*)^2 near the crossing
# From the NPZ, the convex epsilon has c2 ~ 10 in M_KK^4 units
# rho_residual ~ c2 * dtau^2
# We can estimate c2 from the flatband data
# rho_gs(fold) = -0.342 and the crossing is at tau*=0.209
# rho_gs ~ c2*(tau - tau*)^2 - c2*(0 - tau*)^2 = c2*(tau^2 - 2*tau*tau* + tau*^2 - tau*^2)
# = c2*(tau^2 - 2*tau*tau*)
# At tau=tau_fold=0.19: rho_gs = c2*(0.19^2 - 2*0.19*0.209) = c2*(0.0361 - 0.07942) = c2*(-0.04332)
# So c2 = rho_gs / (-0.04332) = 0.342 / 0.04332 = 7.90
c2_est = abs(rho_gs_fb) / abs(tau_fold**2 - 2*tau_fold*tau_star_fb)
dtau_sq = dtau**2
rho_residual_MKK4 = c2_est * dtau_sq
rho_residual_GeV4 = rho_residual_MKK4 * M_KK**4 / (16 * np.pi**2)
gap_residual_qtheory = np.log10(rho_residual_GeV4 / rho_obs) if rho_residual_GeV4 > 0 else float('inf')

print(f"  c_2 estimate: {c2_est:.2f} M_KK^4")
print(f"  delta_tau = |tau* - tau_fold| = {dtau:.4f}")
print(f"  rho_residual ~ c_2 * (delta_tau)^2 = {c2_est:.2f} * {dtau_sq:.6f} = {rho_residual_MKK4:.4f} M_KK^4")
print(f"  = {rho_residual_GeV4:.3e} GeV^4")
print(f"  Gap from q-theory residual: {gap_residual_qtheory:.1f} orders")
print(f"  Reduction from Chain A: {gap_honest - gap_residual_qtheory:.1f} orders")

print(f"\n  CRITICAL CAVEAT: This residual assumes (delta_tau)^2 displacement.")
print(f"  The 110.5 -> {gap_residual_qtheory:.1f} reduction depends entirely on")
print(f"  the self-tuning mechanism being physical, which requires:")
print(f"    1. Self-consistent Delta(tau) from coupled BCS gap equation")
print(f"    2. Verification that the fold IS the q-theory equilibrium")
print(f"    3. Stability of the equilibrium under fluctuations")

# Closed routes count
print(f"\n{'=' * 72}")
print(f"VI. CLOSED CC ROUTES (cumulative)")
print(f"{'=' * 72}")
print(f"  Spectral action equilibrium closures: 29")
print(f"  S45 new closures:")
print(f"    - Unexpanded SA (FAIL, 29th spectral closure)")
print(f"    - Torsion full (ARTIFACT, extensive in N)")
print(f"    - Euler deficit (DISPROVED, ensemble artifact)")
print(f"    - CC~3*hierarchy (COINCIDENCE, numerological)")
print(f"  Total S45 closures affecting CC: 4 new")
print(f"  Total closed CC routes: 29 spectral + 4 other = 33")

print(f"\n{'=' * 72}")
print(f"VII. OPEN ROUTES")
print(f"{'=' * 72}")
print(f"  1. Q-Theory + self-consistent BCS (next: coupled gap equation)")
print(f"  2. Continuum limit (max_pq_sum -> inf) effects on CC")
print(f"  3. Dynamical cutoff selection principle for f")
print(f"  4. Torsion singlet sector: T=0.147, O(1) but NOT a suppression")

print(f"\nDone.")
