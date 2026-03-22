#!/usr/bin/env python3
"""
S44 EIH-GRAV-44: ADM Mass of the Fold via EIH in Spectral Geometry
====================================================================

Computes the gravitating energy (ADM mass) of the fold geometry using
three independent routes:

  (a) Spectral action (polynomial): rho_SA = S_fold * M_KK^4
  (b) Sakharov/trace-log (logarithmic): from W1-1, W1-4
  (c) ADM/spectral zeta (EIH): singlet projection via Peter-Weyl

The EIH approach in spectral geometry:
  In GR, the ADM mass is extracted from the 1/r falloff of h_00 at spatial
  infinity via surface integrals (Einstein-Infeld-Hoffmann 1938). The Bianchi
  identity nabla_mu G^{mu nu} = 0 constrains the motion of singularities.
  The ADM mass depends on the MONOPOLE (l=0) component of the gravitational
  field -- higher multipoles fall off faster and are invisible at infinity.

  In Kaluza-Klein spectral geometry (Connes NCG on M4 x K):
  - The 4D gravitational field couples ONLY to the singlet (0,0) sector
    of the internal stress-energy tensor
  - Non-singlet sectors integrate to zero over K by Peter-Weyl orthogonality
  - This is the block-diagonal theorem (S22b) applied to gravity: D_K
    decomposes by SU(3) representation, and the KK reduction projects
    to the singlet
  - The EIH "effacement" (strong equivalence principle) becomes:
    the gravitating mass = singlet spectral action, not the full S_fold

Gate: EIH-GRAV-44
  PASS if M_ADM / S_fold < 10^{-50}
  FAIL if M_ADM / S_fold > 0.1
  INFO if intermediate

Author: einstein-theorist
Date: 2026-03-14
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ============================================================
# 1. LOAD DATA
# ============================================================

data_const = np.load('tier0-computation/s42_constants_snapshot.npz', allow_pickle=True)
data_sfull = np.load('tier0-computation/s36_sfull_tau_stabilization.npz', allow_pickle=True)

# Key constants
tau_fold_const = float(data_const['tau_fold'])     # 0.19
a0_fold = float(data_const['a0_fold'])             # 6440
a2_fold = float(data_const['a2_fold'])             # 2776.17
a4_fold = float(data_const['a4_fold'])             # 1350.72
M_KK_GN = float(data_const['M_KK_from_GN'])       # 7.43e16 GeV
M_KK_kerner = float(data_const['M_KK_kerner'])     # 5.04e17 GeV

# S_fold and level/sector decomposition
S_fold = float(data_sfull['S_fold'][0])            # 250360.68
tau_combined = data_sfull['tau_combined']
fold_idx = 7  # tau = 0.19

# Seeley-DeWitt coefficients from S_full decomposition
S_level = {}
for i in range(4):
    S_level[i] = data_sfull[f'S_level_{i}']

# Sector spectral actions
sectors_computed = [(0,0), (1,0), (0,1), (1,1), (2,0), (0,2), (3,0), (0,3), (2,1), (1,2)]
S_sector = {}
for (p,q) in sectors_computed:
    key = f'S_sector_{p}_{q}'
    if key in data_sfull.files:
        S_sector[(p,q)] = data_sfull[key]

# Eigenvalue data at fold (from S36 file)
sector_evals = {}
for (p,q) in sectors_computed:
    key = f'evals_tau0.190_{p}_{q}'
    if key in data_sfull.files:
        sector_evals[(p,q)] = data_sfull[key]

# Physical constants
from canonical_constants import M_Pl_unreduced as M_Pl  # GeV
inv_16piG_obs = M_Pl**2 / (16 * np.pi)  # 2.965e36 GeV^2

print(f"=== LOADED DATA ===")
print(f"tau_fold = {tau_fold_const}")
print(f"a0 = {a0_fold}, a2 = {a2_fold:.4f}, a4 = {a4_fold:.4f}")
print(f"S_fold = {S_fold:.2f}")
print(f"M_KK (GN) = {M_KK_GN:.3e} GeV")
print(f"M_KK (Kerner) = {M_KK_kerner:.3e} GeV")

# ============================================================
# 2. SINGLET FRACTION OF SPECTRAL ACTION (EIH Route)
# ============================================================
# The gravitating energy as seen by a 4D observer is the singlet
# projection of the spectral action.
#
# S_level_0 = S_{(0,0)} = spectral action from the singlet sector ONLY.
# S_fold = sum over ALL levels = sum over ALL representations.
#
# The EIH "mass" is S_singlet, not S_fold.

S_singlet = S_level[0][fold_idx]    # = S_{(0,0)} at fold
S_full = S_fold

ratio_singlet_to_full = S_singlet / S_full

print(f"\n=== EIH SINGLET PROJECTION (Route c) ===")
print(f"S_singlet = S(0,0) = {S_singlet:.6f}")
print(f"S_full = S_fold = {S_full:.2f}")
print(f"Ratio S_singlet/S_full = {ratio_singlet_to_full:.6e}")
print(f"log10(ratio) = {np.log10(ratio_singlet_to_full):.4f}")
print(f"Suppression: {1/ratio_singlet_to_full:.0f}x")

# ============================================================
# 3. SPECTRAL ZETA FUNCTION FROM EIGENVALUES
# ============================================================
# Compute sector-by-sector spectral zeta invariants

print(f"\n=== SPECTRAL ZETA INVARIANTS (sector decomposition) ===")
print(f"{'Sector':<10} {'N':<8} {'sum|lam|':<12} {'sum(lam^2)':<12} {'sum(lam^4)':<12} {'Tr ln|lam|':<12} {'S_sector':<12}")

results = {}
total_abs = 0
total_sq = 0
total_4th = 0
total_ln = 0

for (p,q) in sectors_computed:
    ev = sector_evals[(p,q)]
    ae = np.abs(ev)
    ae_pos = ae[ae > 0]
    n = len(ev)
    s_abs = np.sum(ae_pos)
    s_sq = np.sum(ae_pos**2)
    s_4th = np.sum(ae_pos**4)
    s_ln = np.sum(np.log(ae_pos))
    s_sa = S_sector[(p,q)][fold_idx]

    results[(p,q)] = {
        'n': n, 'sum_abs': s_abs, 'sum_sq': s_sq,
        'sum_4th': s_4th, 'Tr_ln': s_ln, 'S_sector': s_sa
    }
    total_abs += s_abs
    total_sq += s_sq
    total_4th += s_4th
    total_ln += s_ln

    print(f"  ({p},{q}){'':<5} {n:<8} {s_abs:<12.4f} {s_sq:<12.4f} {s_4th:<12.4f} {s_ln:<12.4f} {s_sa:<12.4f}")

print(f"  {'TOTAL':<10} {sum(results[k]['n'] for k in results):<8} {total_abs:<12.4f} {total_sq:<12.4f} {total_4th:<12.4f} {total_ln:<12.4f}")

# Singlet fractions for different moments
singlet = results[(0,0)]
frac_abs = singlet['sum_abs'] / total_abs       # zeta(-1/2) ~ Casimir
frac_sq = singlet['sum_sq'] / total_sq           # zeta(-1) ~ a_2 ~ G_N
frac_4th = singlet['sum_4th'] / total_4th        # zeta(-2) ~ a_4 ~ CC
frac_ln = singlet['Tr_ln'] / total_ln            # zeta'(0) ~ analytic torsion
frac_SA = singlet['S_sector'] / sum(results[k]['S_sector'] for k in results)

print(f"\n=== SINGLET FRACTIONS (10 computed sectors only) ===")
print(f"  sum|lam| (Casimir, zeta(-1/2)): {frac_abs:.6f} ({frac_abs*100:.3f}%)")
print(f"  sum(lam^2) (G_N, zeta(-1)):     {frac_sq:.6f} ({frac_sq*100:.3f}%)")
print(f"  sum(lam^4) (CC, zeta(-2)):       {frac_4th:.6f} ({frac_4th*100:.3f}%)")
print(f"  Tr ln|lam| (torsion, zeta'(0)):  {frac_ln:.6f} ({frac_ln*100:.3f}%)")
print(f"  S_sector (spectral action):       {frac_SA:.6f} ({frac_SA*100:.3f}%)")

# ============================================================
# 4. FULL SPECTRAL ACTION: SINGLET vs TOTAL (all levels)
# ============================================================
# The FULL spectral action S_fold includes ALL Casimir levels (0 through ~max).
# S_level_0 = singlet. S_fold = sum of all levels.
# This is the physically relevant ratio for the Friedmann equation.

# Ratio for different tau values
print(f"\n=== SINGLET FRACTION OF FULL SPECTRAL ACTION vs tau ===")
tau_vals_all = data_sfull['tau_combined']
S_full_all = data_sfull['S_full']

singlet_ratios = []
for i, tau in enumerate(tau_vals_all):
    s0 = S_level[0][i]
    sf = S_full_all[i]
    ratio = s0 / sf
    singlet_ratios.append(ratio)
    print(f"  tau={tau:.3f}: S_singlet={s0:.4f}, S_full={sf:.2f}, ratio={ratio:.6e} ({ratio*100:.4f}%)")

singlet_ratios = np.array(singlet_ratios)

# ============================================================
# 5. SPECTRAL ZETA FUNCTION: ANALYTIC CONTINUATION
# ============================================================
# For the FINITE discrete spectrum, zeta(s) = sum |lambda_k|^{-2s}
# converges for all s (no poles). Analytic continuation is trivial.

all_evals_fold = np.concatenate([sector_evals[(p,q)] for (p,q) in sectors_computed])
abs_evals = np.abs(all_evals_fold)
abs_evals_pos = abs_evals[abs_evals > 0]

# Singlet eigenvalues only
ev_singlet = np.abs(sector_evals[(0,0)])
ev_singlet_pos = ev_singlet[ev_singlet > 0]

print(f"\n=== SPECTRAL ZETA FUNCTION ===")
print(f"Total eigenvalues (10 sectors): {len(all_evals_fold)}")
print(f"Positive eigenvalues: {len(abs_evals_pos)}")
print(f"Singlet eigenvalues: {len(ev_singlet_pos)}")

# Compute zeta at key values
s_range = np.linspace(0.5, 6.0, 200)
zeta_total = np.array([np.sum(abs_evals_pos**(-2*s)) for s in s_range])
zeta_singlet = np.array([np.sum(ev_singlet_pos**(-2*s)) for s in s_range])

print(f"\n{'s':<8} {'zeta_total':<18} {'zeta_singlet':<18} {'ratio':<12}")
for s_check in [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]:
    zt = np.sum(abs_evals_pos**(-2*s_check))
    zs = np.sum(ev_singlet_pos**(-2*s_check))
    print(f"  {s_check:<6.1f} {zt:<18.6f} {zs:<18.6f} {zs/zt:<12.6f}")

# Analytic continuation to negative s (for finite spectrum, just evaluate directly)
print(f"\nAnalytic continuation (negative s):")
for s_check in [-2.0, -1.5, -1.0, -0.5, 0.0]:
    # zeta(s) = sum |lambda|^{-2s} = sum |lambda|^{|2s|}
    zt = np.sum(abs_evals_pos**(-2*s_check))
    zs = np.sum(ev_singlet_pos**(-2*s_check))
    ratio_s = zs/zt if zt != 0 else 0
    print(f"  s={s_check:<6.1f}: zeta_total={zt:<14.4f}, zeta_singlet={zs:<14.4f}, ratio={ratio_s:.6f}")

# Casimir energy = (1/2) zeta(-1/2) = (1/2) sum |lambda_k|
E_Casimir_total = 0.5 * np.sum(abs_evals_pos)
E_Casimir_singlet = 0.5 * np.sum(ev_singlet_pos)

print(f"\n=== ZETA-REGULARIZED CASIMIR ENERGY ===")
print(f"E_Casimir (total, 10 sectors) = {E_Casimir_total:.4f} M_KK")
print(f"E_Casimir (singlet) = {E_Casimir_singlet:.4f} M_KK")
print(f"Singlet fraction = {E_Casimir_singlet/E_Casimir_total:.6f}")

# Analytic torsion
Tr_ln_total = np.sum(np.log(abs_evals_pos))
Tr_ln_singlet = np.sum(np.log(ev_singlet_pos))
zeta_prime_0_total = -2 * Tr_ln_total
zeta_prime_0_singlet = -2 * Tr_ln_singlet

print(f"\n=== ANALYTIC TORSION ===")
print(f"Tr ln|D_K| (total) = {Tr_ln_total:.4f}")
print(f"Tr ln|D_K| (singlet) = {Tr_ln_singlet:.4f}")
print(f"zeta'(0) total = {zeta_prime_0_total:.4f}")
print(f"zeta'(0) singlet = {zeta_prime_0_singlet:.4f}")
print(f"T_K = exp(-zeta'(0)/2) = {np.exp(-zeta_prime_0_total/2):.6e}")

# ============================================================
# 6. THREE GRAVITATING ENERGY ESTIMATES
# ============================================================
#
# (a) SPECTRAL ACTION (polynomial): S_fold = 250361 spectral units
#     This uses f(D^2/Lambda^2) = polynomial weighting. ALL sectors contribute.
#     Physical: rho_SA = 8.43e73 GeV^4 (S42 calibration)
#
# (b) TRACE-LOG (logarithmic): Tr ln(D_K^2) = 773.46 spectral units
#     From W1-4: ratio to S_fold = 3.09e-3 (2.51 orders suppression)
#     During transit: Volovik-subtracted delta = 7.76e-6 * S_fold
#     Post-transit: exactly 0 (Delta=0, condensate destroyed)
#
# (c) EIH SINGLET (ADM mass): S_singlet = 14.23 spectral units
#     Only the (0,0) singlet sector gravitates in 4D.
#     This is the ADM mass: what a 4D observer actually sees.
#
# The EIH ratio S_singlet/S_fold = 5.68e-5 is a GEOMETRIC suppression
# (Peter-Weyl decomposition), not a fine-tuning.

rho_SA_phys = 8.43e73  # GeV^4 from S42
conversion = rho_SA_phys / S_fold  # GeV^4 per spectral unit

# Trace-log from W1-4
rho_TL_transit = S_fold * 7.76e-6 * conversion  # Volovik-subtracted during transit
TL_spectral = S_fold * 3.09e-3  # |Tr ln| in spectral units
rho_TL_phys = TL_spectral * conversion

# EIH singlet
rho_singlet_phys = S_singlet * conversion

# Observed
from canonical_constants import rho_Lambda_obs as rho_obs  # GeV^4

print(f"\n{'='*70}")
print(f"THREE GRAVITATING ENERGY ESTIMATES")
print(f"{'='*70}")
print(f"")
print(f"{'Functional':<35} {'Spectral':<15} {'GeV^4':<15} {'OOM from obs':<15}")
print(f"{'(a) Spectral action (poly)':<35} {S_fold:<15.2f} {rho_SA_phys:<15.3e} {np.log10(rho_SA_phys/rho_obs):<15.1f}")
print(f"{'(b) Trace-log (full)':<35} {TL_spectral:<15.2f} {rho_TL_phys:<15.3e} {np.log10(rho_TL_phys/rho_obs):<15.1f}")
print(f"{'(b) Trace-log (transit, Volovik)':<35} {S_fold*7.76e-6:<15.6f} {rho_TL_transit:<15.3e} {np.log10(rho_TL_transit/rho_obs):<15.1f}")
print(f"{'(b) Trace-log (post-transit)':<35} {'0':<15} {'0':<15} {'---':<15}")
print(f"{'(c) EIH singlet':<35} {S_singlet:<15.4f} {rho_singlet_phys:<15.3e} {np.log10(rho_singlet_phys/rho_obs):<15.1f}")
print(f"{'Observed':<35} {'---':<15} {rho_obs:<15.3e} {'0':<15}")

print(f"\n=== SUPPRESSION CHAIN ===")
print(f"(a) -> (b) Trace-log: {np.log10(TL_spectral/S_fold):.2f} orders (poly -> log)")
print(f"(a) -> (c) EIH singlet: {np.log10(S_singlet/S_fold):.2f} orders (total -> singlet)")
print(f"(b) -> (c) EIH of trace-log: singlet fraction of Tr ln = {frac_ln:.6f}")
print(f"(a) -> (b)x(c) Combined: {np.log10(S_singlet/S_fold * 3.09e-3):.2f} orders")

# The EIH-aware trace-log: apply BOTH singlet projection AND logarithmic weighting
# rho_EIH_TL = singlet fraction of Tr ln * conversion
TL_singlet = Tr_ln_singlet
rho_EIH_TL = abs(TL_singlet) * conversion  # Use abs because Tr ln can be negative for small eigenvalues

print(f"\nCOMBINED EIH + TRACE-LOG:")
print(f"  Tr ln|D_K| singlet = {Tr_ln_singlet:.4f}")
print(f"  |Tr ln singlet| / S_fold = {abs(Tr_ln_singlet)/S_fold:.6e}")
print(f"  log10(ratio) = {np.log10(abs(Tr_ln_singlet)/S_fold):.4f}")
print(f"  rho_combined = {rho_EIH_TL:.3e} GeV^4")
print(f"  OOM from observed: {np.log10(rho_EIH_TL/rho_obs):.1f}")

# ============================================================
# 7. WEYL SCALING ANALYSIS
# ============================================================
# Weyl's law predicts the mode counting fraction:
# N_singlet / N_total ~ (dim singlet)^2 / sum_R (dim R)^2
# For our 10 sectors: N_00 = 16, N_total = 1232

weyl_frac = 16 / 1232
# For FULL Hilbert space (a_0 = 6440):
# The singlet count in a_0 = 6440 is dim(spinor) * (dim_00)^2 = 16 * 1 = 16
# (The factor 16 = 2^4 for 8D spinor comes from spinor bundle)
# But a_0 is the total trace, so singlet a_0 = 16 out of 6440 -> 16/6440 = 0.00248
weyl_frac_full = 16 / a0_fold

print(f"\n=== WEYL SCALING ===")
print(f"Weyl prediction (10 sectors): {16}/{1232} = {weyl_frac:.6f}")
print(f"Weyl prediction (full a_0):   {16}/{int(a0_fold)} = {weyl_frac_full:.6f}")
print(f"Actual EIH ratio (S_singlet/S_fold): {ratio_singlet_to_full:.6e}")
print(f"Actual/Weyl_full: {ratio_singlet_to_full/weyl_frac_full:.4f}")
print(f"")
print(f"The actual ratio is {ratio_singlet_to_full/weyl_frac_full:.2f}x the Weyl prediction.")
print(f"Deviation from Weyl reflects spectral non-uniformity at the fold:")
print(f"higher representations have LARGER eigenvalues (a_4 ~ lambda^4 grows")
print(f"with Casimir eigenvalue), so their spectral action contribution grows")
print(f"FASTER than the mode count suggests.")

# ============================================================
# 8. LEVEL HIERARCHY
# ============================================================

print(f"\n=== LEVEL HIERARCHY AT FOLD ===")
print(f"{'Level':<10} {'S_level':<15} {'Fraction':<15} {'Cumulative':<15}")
cumul = 0
for i in range(4):
    s = S_level[i][fold_idx]
    frac = s / S_fold
    cumul += frac
    print(f"  {i:<10} {s:<15.4f} {frac*100:<14.4f}% {cumul*100:<14.4f}%")

print(f"\nLevel 3 dominance: {S_level[3][fold_idx]/S_fold*100:.2f}%")
print(f"Levels 0+1+2: {(S_level[0][fold_idx]+S_level[1][fold_idx]+S_level[2][fold_idx])/S_fold*100:.2f}%")

# The SU(3) Casimir eigenvalue for representation (p,q):
# C_2(p,q) = (p^2 + q^2 + pq + 3p + 3q) / 3
# dim(p,q) = (p+1)(q+1)(p+q+2)/2
# Higher Casimir = higher eigenvalues = MUCH larger spectral action contribution
# This is why level 3 dominates: it has the highest-dimensional reps

print(f"\n=== SU(3) CASIMIR SCALING ===")
for (p,q) in [(0,0),(1,0),(0,1),(1,1),(2,0),(0,2),(3,0),(0,3),(2,1),(1,2)]:
    C2 = (p**2 + q**2 + p*q + 3*p + 3*q) / 3
    dim_pq = (p+1)*(q+1)*(p+q+2)//2
    print(f"  ({p},{q}): C_2 = {C2:.3f}, dim = {dim_pq}, S = {S_sector[(p,q)][fold_idx]:.4f}, S/dim^2 = {S_sector[(p,q)][fold_idx]/dim_pq**2:.6f}")

# ============================================================
# 9. GATE EVALUATION
# ============================================================

M_ADM_spectral = S_singlet  # The gravitating energy = singlet spectral action
ratio_ADM_to_Sfold = ratio_singlet_to_full

print(f"\n{'='*70}")
print(f"GATE: EIH-GRAV-44")
print(f"{'='*70}")
print(f"")
print(f"M_ADM (EIH singlet) = {M_ADM_spectral:.6f} spectral units")
print(f"S_fold (full spectral action) = {S_full:.2f} spectral units")
print(f"RATIO: M_ADM / S_fold = {ratio_ADM_to_Sfold:.6e}")
print(f"log10(ratio) = {np.log10(ratio_ADM_to_Sfold):.4f}")
print(f"")

if ratio_ADM_to_Sfold < 1e-50:
    verdict = "PASS"
    print(f"VERDICT: PASS (ratio < 10^-50: massive suppression)")
elif ratio_ADM_to_Sfold > 0.1:
    verdict = "FAIL"
    print(f"VERDICT: FAIL (ratio > 0.1: no suppression)")
else:
    verdict = "INFO"
    print(f"VERDICT: INFO (ratio = {ratio_ADM_to_Sfold:.3e} ~ 10^{np.log10(ratio_ADM_to_Sfold):.1f})")
    print(f"  Between PASS (<10^-50) and FAIL (>0.1)")
    print(f"  4.25 orders of suppression from Peter-Weyl singlet projection")

print(f"\n=== PHYSICAL INTERPRETATION ===")
print(f"The 4D gravitational field (what enters the Friedmann equation) sees")
print(f"ONLY the singlet component of the internal energy. The EIH effacement")
print(f"principle -- that the motion of bodies depends on mass, not internal")
print(f"structure -- manifests here as the Peter-Weyl projection to (0,0).")
print(f"")
print(f"Of the {S_full:.0f} spectral units of 'energy' encoded in the full spectral")
print(f"action, only {S_singlet:.4f} units ({ratio_ADM_to_Sfold*100:.4f}%) couple to 4D gravity.")
print(f"The remaining 99.994% is in non-singlet representations that are")
print(f"invisible to a 4D observer -- they are the 'dark' internal structure.")
print(f"")
print(f"This provides {np.log10(1/ratio_ADM_to_Sfold):.2f} orders of CC reduction")
print(f"(from ~120 OOM to ~116 OOM above observed). While insufficient to solve")
print(f"the CC problem alone, this is a STRUCTURAL suppression (exact, from")
print(f"Peter-Weyl orthogonality) that stacks multiplicatively with the")
print(f"trace-log suppression ({np.log10(3.09e-3):.2f} orders from W1-4).")
print(f"")
print(f"Combined: EIH singlet x trace-log = {np.log10(abs(Tr_ln_singlet)/S_fold):.2f} orders total")
print(f"This reduces the CC problem from ~120 to ~{120+np.log10(abs(Tr_ln_singlet)/S_fold):.0f} OOM.")

# ============================================================
# 10. SAVE DATA
# ============================================================

np.savez('tier0-computation/s44_eih_grav.npz',
    # Gate
    gate_verdict=np.array([verdict]),
    gate_name=np.array(['EIH-GRAV-44']),
    gate_ratio=ratio_ADM_to_Sfold,
    # Spectral action decomposition
    S_singlet=S_singlet,
    S_fold=S_fold,
    ratio_singlet_to_full=ratio_singlet_to_full,
    # Level hierarchy
    S_level_0_fold=S_level[0][fold_idx],
    S_level_1_fold=S_level[1][fold_idx],
    S_level_2_fold=S_level[2][fold_idx],
    S_level_3_fold=S_level[3][fold_idx],
    # Sector data at fold
    sector_S_fold=np.array([S_sector[(p,q)][fold_idx] for (p,q) in sectors_computed]),
    sector_labels=np.array(sectors_computed),
    # Singlet fractions
    singlet_frac_abs=frac_abs,
    singlet_frac_sq=frac_sq,
    singlet_frac_4th=frac_4th,
    singlet_frac_ln=frac_ln,
    singlet_frac_SA=frac_SA,
    # Spectral zeta
    s_range=s_range,
    zeta_total=zeta_total,
    zeta_singlet=zeta_singlet,
    Tr_ln_total=Tr_ln_total,
    Tr_ln_singlet=Tr_ln_singlet,
    zeta_prime_0_total=zeta_prime_0_total,
    zeta_prime_0_singlet=zeta_prime_0_singlet,
    E_Casimir_total=E_Casimir_total,
    E_Casimir_singlet=E_Casimir_singlet,
    # tau dependence
    tau_vals=tau_vals_all,
    singlet_ratios_vs_tau=singlet_ratios,
    # Physical densities
    rho_SA_phys=rho_SA_phys,
    rho_TL_phys=rho_TL_phys,
    rho_singlet_phys=rho_singlet_phys,
    rho_obs=rho_obs,
    # Weyl comparison
    weyl_frac_10sectors=weyl_frac,
    weyl_frac_full=weyl_frac_full,
    # Three-estimate chain
    chain_poly_to_log=np.log10(TL_spectral/S_fold),
    chain_total_to_singlet=np.log10(S_singlet/S_fold),
    chain_combined=np.log10(abs(Tr_ln_singlet)/S_fold),
)
print(f"\nSaved: tier0-computation/s44_eih_grav.npz")

# ============================================================
# 11. PLOT
# ============================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('EIH-GRAV-44: ADM Mass of the Fold via Spectral Zeta Function\n'
             f'Gate: {verdict} | S_singlet/S_fold = {ratio_singlet_to_full:.3e}',
             fontsize=13, fontweight='bold')

# Panel (a): Spectral zeta function
ax = axes[0, 0]
ax.semilogy(s_range, zeta_total, 'b-', linewidth=1.5, label='Total (10 sectors)')
ax.semilogy(s_range, zeta_singlet, 'r-', linewidth=1.5, label='Singlet (0,0)')
ax.set_xlabel('s', fontsize=11)
ax.set_ylabel(r'$\zeta_{D_K^2}(s)$', fontsize=11)
ax.set_title('Spectral Zeta Function', fontsize=11)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel (b): Sector spectral action at fold (bar chart)
ax = axes[0, 1]
sector_labels_str = [f'({p},{q})' for (p,q) in sectors_computed]
sector_S_vals = [S_sector[(p,q)][fold_idx] for (p,q) in sectors_computed]
colors = ['red' if (p==0 and q==0) else 'steelblue' for (p,q) in sectors_computed]
bars = ax.bar(sector_labels_str, sector_S_vals, color=colors, edgecolor='black', linewidth=0.5)
ax.set_xlabel('SU(3) representation (p,q)', fontsize=11)
ax.set_ylabel('S(p,q) at fold', fontsize=11)
ax.set_title('Sector Spectral Action Decomposition', fontsize=11)
ax.annotate(f'Singlet\n{S_singlet:.2f}\n({ratio_singlet_to_full*100:.4f}% of S_fold)',
            xy=(0, S_singlet), xytext=(2, max(sector_S_vals)*0.7),
            fontsize=9, arrowprops=dict(arrowstyle='->', color='red'),
            color='red', fontweight='bold')
ax.grid(True, alpha=0.3, axis='y')
ax.tick_params(axis='x', rotation=45)

# Panel (c): Level hierarchy
ax = axes[1, 0]
level_labels = ['Level 0\n(singlet)', 'Level 1\n(fund.)', 'Level 2\n(adj.+)', 'Level 3\n(high)']
level_vals = [S_level[i][fold_idx] for i in range(4)]
level_colors = ['red', 'darkorange', 'steelblue', 'darkblue']
bars = ax.bar(level_labels, np.log10(level_vals), color=level_colors, edgecolor='black', linewidth=0.5)
ax.set_ylabel(r'$\log_{10}$(S_level)', fontsize=11)
ax.set_title('Level Hierarchy of Spectral Action', fontsize=11)
for bar, lv in zip(bars, level_vals):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
            f'{lv:.1f}\n({lv/S_fold*100:.2f}%)',
            ha='center', va='bottom', fontsize=8, fontweight='bold')
ax.axhline(y=np.log10(S_fold), color='gray', linestyle='--', alpha=0.5, label=f'S_fold = {S_fold:.0f}')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, axis='y')

# Panel (d): Singlet fraction vs tau
ax = axes[1, 1]
ax.semilogy(tau_vals_all, singlet_ratios*100, 'ko-', markersize=5, linewidth=1.5, label='Actual')
ax.axhline(y=weyl_frac_full*100, color='r', linestyle='--', alpha=0.7,
           label=f'Weyl prediction ({weyl_frac_full*100:.3f}%)')
ax.axvline(x=0.19, color='gray', linestyle=':', alpha=0.5, label='Fold')
ax.set_xlabel(r'$\tau$', fontsize=11)
ax.set_ylabel('Singlet fraction of S_full (%)', fontsize=11)
ax.set_title(r'Singlet Fraction vs. $\tau$ (EIH Suppression)', fontsize=11)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('tier0-computation/s44_eih_grav.png', dpi=150, bbox_inches='tight')
print(f"Saved: tier0-computation/s44_eih_grav.png")

print(f"\n{'='*70}")
print(f"COMPUTATION COMPLETE: EIH-GRAV-44")
print(f"{'='*70}")
