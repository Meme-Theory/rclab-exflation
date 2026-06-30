#!/usr/bin/env python3
"""
STRUCTURE-RG-SCALE-74: R-G Level Spectrum BAO or Galaxy Bias Feature
====================================================================

Session 74, Wave 4-J
Agent: phonon-first-cosmologist

Pre-registered gate: STRUCTURE-RG-SCALE-74
  PASS: k_RG matches BAO k_peak within 10%
  INFO: matches within 30%
  FAIL: > 30% off

Physics:
--------
The phonon-exflation substrate has no pre-existing spatial container.
Space is an emergent description of how the fabric's spectral weight
distributes through D_K eigenvalue reorganization.  The R-G (Reduction
Group) integrable sector of the multi-cell BdG Hamiltonian carries a
characteristic energy scale: the mean level spacing <Delta E> across
the spectrum.  This is NOT a random-matrix scale -- the S73B gate
MULTI-CELL-INTEG-73B showed <r> = 0.4044 < r_GOE = 0.536, confirming
R-G integrability (Poissonian).  The spacing therefore encodes the
substrate's intrinsic level-repulsion-free mode separation.

If this fabric-intrinsic scale, projected forward through the full
post-transit expansion history, lands on an observable feature in
the baryon acoustic oscillation (BAO) power spectrum (k_peak ~ 0.1
Mpc^{-1}), then the substrate's level-spacing has left an imprint
on the CMB / LSS observables.

The projection is NOT an LCDM "expansion of space" -- it is the
reorganization of spectral weight from the fold (tau = 0.19) to
today.  The framework gives:

  - tau_fold = 0.19 (S42 CONST-FREEZE)
  - H_phys_fold = 0.3958 M_KK (S73B EFOLD-MAPPING, physical Hubble)
  - z_fold = 9.67e29 (S73B, redshift from fold to today)
  - N_total = 132.45 e-folds (S73B, total expansion)
  - M_KK = 7.43e16 GeV (S42 gravity route, conservative)

With the convention a_fold = 1 and a_today = exp(N_total), a mode of
comoving wavenumber k_comoving (in M_KK units, set at the fold) has
physical wavenumber at present:

  k_today_phys = k_comoving_MKK * M_KK / (hbar_c) / a_today
               = k_comoving_MKK * M_KK / (hbar_c * exp(N_total))

The mean level spacing <Delta E> (in M_KK units) gives the
fabric-intrinsic comoving wavenumber at the fold by dimensional
reading: the spacing IS the spectral resolution, and through the
acoustic metric this spectral resolution corresponds to a comoving
wavelength.  The k_RG we compare against k_BAO is therefore:

  k_RG = <Delta E> * M_KK / (hbar_c * exp(N_total))

expressed in Mpc^{-1}.

Cross-check (alternate interpretation -- "fold-horizon-equivalent"):
---------------------------------------------------------------------
An alternative reading takes <Delta E> * M_KK as an energy, converts
to an inverse length via hbar_c, then applies NOT the expansion
rescaling but the "aH equivalence" used in the CMB pivot mapping
(S73B computed k_pivot_MKK = 4.30e-57 for k_pivot = 0.05 Mpc^{-1}).
This gives a second estimate by analogy.

Input: computations/session-73/s73b_multi_cell_integ.npz (R-G eigenvalues)
       computations/session-73/s73b_efold_mapping.npz (expansion history)
       computations/_shared/canonical_constants.py
Output: computations/session-74/s74_structure_rg_scale.npz
"""

import numpy as np
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    M_KK,
    hbar_c_GeV_m,
    Mpc_to_m,
    Mpc_to_GeV_inv,
    tau_fold,
    H_fold,
    N_cells,
)

print("=" * 72)
print("STRUCTURE-RG-SCALE-74: R-G Level Spectrum BAO Feature")
print("=" * 72)

# ---------------------------------------------------------------------
# 1. Load S73B R-G eigenvalue data
# ---------------------------------------------------------------------
print("\n[1] Loading S73B multi-cell integrability data")
print("-" * 72)

t0 = time.time()  # (local)

d_s73b = np.load("s73b_multi_cell_integ.npz", allow_pickle=True)  # (local)

N_modes_in = int(d_s73b["N_modes"])  # (local)
N_cells_in = int(d_s73b["N_cells"])  # (local)
N_pair_in = int(d_s73b["N_pair"])  # (local)
dim_total_in = int(d_s73b["dim_total"])  # (local)
r_overall_in = float(d_s73b["r_overall"])  # (local)
r_Poisson_ref = float(d_s73b["r_Poisson"])  # (local)
r_GOE_ref = float(d_s73b["r_GOE"])  # (local)

print(f"  N_modes = {N_modes_in}")
print(f"  N_cells = {N_cells_in}")
print(f"  N_pair  = {N_pair_in}")
print(f"  dim_total = {dim_total_in}")
print(f"  <r>_overall = {r_overall_in:.4f}  (r_Poisson={r_Poisson_ref:.3f}, r_GOE={r_GOE_ref:.3f})")
print(f"  Integrability: {'CONFIRMED (Poissonian)' if r_overall_in < 0.45 else 'BROKEN'}")

# Per-sector eigenvalues (M_KK units, BdG Hamiltonian eigenvalues)
sectors = ["k0", "kpi_2", "kpi", "k3pi_2"]  # (local)
evals_by_sector = {s: np.asarray(d_s73b[f"evals_{s}"], dtype=float) for s in sectors}  # (local)

# Pool all sectors into a single R-G spectrum.
evals_all = np.concatenate([evals_by_sector[s] for s in sectors])  # (local)
evals_all.sort()
N_evals = len(evals_all)  # (local)

print(f"  Total eigenvalues pooled (all 4 momentum sectors): {N_evals}")
print(f"  Range: [{evals_all.min():.3e}, {evals_all.max():.3e}] M_KK")
print(f"  Mean:  {evals_all.mean():.3e} M_KK")
print(f"  Std:   {evals_all.std():.3e} M_KK")

# ---------------------------------------------------------------------
# 2. Compute mean level spacing <Delta E>
# ---------------------------------------------------------------------
print("\n[2] Mean level spacing <Delta E>")
print("-" * 72)

# Per-sector nearest-neighbour spacings, then pool.
spacings_by_sector = {}  # (local)
for s in sectors:
    ev = np.sort(evals_by_sector[s])  # (local)
    ds = np.diff(ev)  # (local)
    ds = ds[ds > 0]  # drop exact degeneracies  # (local)
    spacings_by_sector[s] = ds

spacings_all = np.concatenate([spacings_by_sector[s] for s in sectors])  # (local)

mean_dE_MKK = float(spacings_all.mean())  # (local) <Delta E> in M_KK units
median_dE_MKK = float(np.median(spacings_all))  # (local)
std_dE_MKK = float(spacings_all.std())  # (local)

# Global-range estimate (an alternative: total spectral range / N)
global_range_MKK = float(evals_all.max() - evals_all.min())  # (local)
mean_dE_range_MKK = global_range_MKK / (N_evals - 1)  # (local)

print(f"  Mean NN spacing    <Delta E>     = {mean_dE_MKK:.6e} M_KK")
print(f"  Median NN spacing  median(dE)    = {median_dE_MKK:.6e} M_KK")
print(f"  Std  NN spacing    std(dE)       = {std_dE_MKK:.6e} M_KK")
print(f"  Range/(N-1)        = {mean_dE_range_MKK:.6e} M_KK")

# Canonical <Delta E> (arithmetic mean of nearest-neighbour spacings)
mean_dE_GeV = mean_dE_MKK * M_KK  # (local) physical energy
print(f"\n  <Delta E>  = {mean_dE_GeV:.6e} GeV")
print(f"  <Delta E>  = {mean_dE_GeV * 1e9:.6e} eV")

# ---------------------------------------------------------------------
# 3. Load S73B expansion history (fold -> today)
# ---------------------------------------------------------------------
print("\n[3] Loading S73B expansion history (EFOLD-MAPPING-73B)")
print("-" * 72)

d_efold = np.load("s73b_efold_mapping.npz", allow_pickle=True)  # (local)

N_total = float(d_efold["N_total"])  # (local) total e-folds fold -> today
z_fold = float(d_efold["z_fold"])  # (local) redshift fold -> today
H_phys_fold_MKK = float(d_efold["H_phys_fold_MKK"])  # (local) physical Hubble at fold, M_KK
H_phys_fold_GeV = float(d_efold["H_phys_fold_GeV"])  # (local) physical Hubble at fold, GeV
k_pivot_MKK_ref = float(d_efold["k_pivot_MKK"])  # (local) CMB pivot in M_KK (S73B reference)
k_pivot_GeV_ref = float(d_efold["k_pivot_GeV"])  # (local)

a_today_over_fold = np.exp(N_total)  # (local) scale factor ratio
a_fold_over_today = 1.0 / a_today_over_fold  # (local)

print(f"  N_total (fold -> today)     = {N_total:.4f}  e-folds")
print(f"  z_fold (S73B)                = {z_fold:.4e}   (= T_rh/T_CMB, radiation era only)")
print(f"  a_today / a_fold             = exp(N_total) = {a_today_over_fold:.4e}")
print(f"  H_phys_fold                  = {H_phys_fold_MKK:.4e} M_KK = {H_phys_fold_GeV:.4e} GeV")
print(f"  k_pivot (S73B, CMB, in M_KK) = {k_pivot_MKK_ref:.4e}")
print(f"  k_pivot (S73B, CMB, in GeV)  = {k_pivot_GeV_ref:.4e}")

# NOTE: S73B's z_fold is computed as T_rh / T_CMB ~ 9.67e29, which is the
# redshift across the RADIATION era only (reheating -> today).  The full
# fold -> today scale factor ratio is exp(N_total) ~ 3.32e57, which
# includes the pre-reheat modulus/stiff epoch.  For projecting a
# fold-epoch physical scale to today, we use exp(N_total).
stage_diff_factor = a_today_over_fold / (1.0 + z_fold)  # (local)
print(f"  exp(N_total) / (1 + z_fold)  = {stage_diff_factor:.4e}  (= pre-reheat stage)")

# ---------------------------------------------------------------------
# 4. Project <Delta E> to today as k_RG
# ---------------------------------------------------------------------
print("\n[4] Projecting <Delta E> through expansion history")
print("-" * 72)

# There are TWO legitimate interpretations of how a fold-era energy
# scale projects to a present-day wavenumber observable.  They differ
# by a factor of exp(N_total) = exp(132.45) ~ 3.3e57.  Both are
# computed here and the gate is evaluated against BOTH.
#
# ---- Interpretation A (PROMPT-STYLE, physical-wavelength stretch) ----
#
# Treat <Delta E> as a physical-frequency at the fold.  The wavelength
# associated with this frequency (lambda_fold = 2 pi hbar c / <Delta E>)
# then stretches on the way to today by a_today/a_fold = exp(N_total).
# The present-day physical wavenumber is therefore
#
#   k_RG_A_today = (<Delta E> * M_KK / hbar_c) * (a_fold/a_today)
#
# This is the literal reading of the prompt:
#   k_RG = <Delta E> / (hbar c a_fold * (scale factor ratio today))
#
# ---- Interpretation B (COMOVING, S73B convention) ----
#
# Treat <Delta E> as defining a comoving wavenumber in M_KK natural
# units: k_comov = <Delta E> * M_KK / hbar_c.  In this convention,
# k_comov is CONSERVED, and k_comov = k_phys_today by definition
# (one simply reads the energy in Mpc^{-1} units via dimensional
# conversion).  This matches S73B's treatment of k_pivot_MKK, where
# 0.05 Mpc^{-1} was mapped directly to 4.30e-57 in M_KK WITHOUT any
# exp(N_total) factor.
#
#   k_RG_B_today = <Delta E> * M_KK / hbar_c  [Mpc^{-1}]
#
# The two interpretations probe different physics:
#   - A treats the R-G spectrum as a property of THIS present-day
#     observable region, projected back via expansion -- a "stretched
#     feature" picture.
#   - B treats the R-G spectrum as a structural invariant of the
#     internal geometry whose natural Mpc^{-1} scale reflects the
#     M_KK -> Mpc conversion, not cosmological expansion.

# ---- Interpretation A ----
k_fold_inv_m_A = (mean_dE_GeV / hbar_c_GeV_m)  # (local) 1/m, physical at fold
k_fold_inv_Mpc_A = k_fold_inv_m_A * Mpc_to_m  # (local) Mpc^{-1} at fold
k_RG_today_A = k_fold_inv_Mpc_A * a_fold_over_today  # (local) Mpc^{-1} today (stretched)

# Consistency path via Mpc_to_GeV_inv.
k_fold_Mpc_inv_alt = mean_dE_GeV * Mpc_to_GeV_inv  # (local)
k_RG_today_A_alt = k_fold_Mpc_inv_alt * a_fold_over_today  # (local)

# ---- Interpretation B ----
k_RG_today_B = mean_dE_GeV * Mpc_to_GeV_inv  # (local) Mpc^{-1} today (comoving)
# Equivalent path:
k_RG_today_B_alt = mean_dE_GeV / hbar_c_GeV_m * Mpc_to_m  # (local)

print(f"  Interpretation A (physical wavelength stretch, prompt formula):")
print(f"    k_fold_phys    = <Delta E> / hbar_c = {k_fold_inv_m_A:.4e} m^{{-1}}")
print(f"                     = {k_fold_inv_Mpc_A:.4e} Mpc^{{-1}}")
print(f"    Stretch factor = 1 / exp({N_total:.3f}) = {a_fold_over_today:.4e}")
print(f"    k_RG_today_A   = {k_RG_today_A:.4e} Mpc^{{-1}}  (alt path: {k_RG_today_A_alt:.4e})")
print(f"")
print(f"  Interpretation B (comoving, S73B convention -- no stretch):")
print(f"    k_RG_today_B   = {k_RG_today_B:.4e} Mpc^{{-1}}  (alt path: {k_RG_today_B_alt:.4e})")
print(f"")
print(f"  Ratio A/B = {k_RG_today_A / k_RG_today_B:.4e}  (= a_fold/a_today = {a_fold_over_today:.4e})")

# The primary gate is evaluated on Interpretation A (prompt-literal).
k_RG_today_inv_Mpc = k_RG_today_A  # (local) primary
k_fold_inv_Mpc = k_fold_inv_Mpc_A  # (local)
k_fold_inv_m = k_fold_inv_m_A  # (local)
k_RG_today_alt = k_RG_today_A_alt  # (local)

# ---------------------------------------------------------------------
# 5. BAO comparison
# ---------------------------------------------------------------------
print("\n[5] Comparison with BAO peak")
print("-" * 72)

# Observational BAO peak wavenumber (DESI/BOSS consistent):
# The first BAO peak of the galaxy power spectrum lies at k_BAO ~ 0.067 h Mpc^{-1}
# in physical units, corresponding to the sound horizon r_drag ~ 147 Mpc.
# The prompt specifies k ~ 0.1 Mpc^{-1} as the comparison point.
k_BAO_peak_Mpc_inv = 0.1  # (local) Mpc^{-1}, BAO first peak (prompt specification)
# Auxiliary cross-check scales (literature consensus):
k_BAO_sound_horizon = 2.0 * np.pi / 147.0  # (local) Mpc^{-1} ~ 0.0427
k_BAO_secondary = 0.06  # (local) Mpc^{-1}, secondary-peak region
k_CMB_pivot = 0.05  # (local) Mpc^{-1}, CMB pivot scale

print(f"  Reference scales (physical, today):")
print(f"    k_BAO_peak         = {k_BAO_peak_Mpc_inv:.4f} Mpc^{{-1}}  (prompt target)")
print(f"    k_BAO_sound horizon= {k_BAO_sound_horizon:.4f} Mpc^{{-1}}  (2 pi / 147 Mpc)")
print(f"    k_BAO_secondary    = {k_BAO_secondary:.4f} Mpc^{{-1}}")
print(f"    k_CMB_pivot        = {k_CMB_pivot:.4f} Mpc^{{-1}}")

# Gate comparison: relative deviation from k_BAO_peak, for BOTH
# interpretations.
ratio_A = k_RG_today_A / k_BAO_peak_Mpc_inv  # (local)
rel_diff_A = abs(k_RG_today_A - k_BAO_peak_Mpc_inv) / k_BAO_peak_Mpc_inv  # (local)
log10_ratio_A = np.log10(ratio_A) if ratio_A > 0 else -np.inf  # (local)

ratio_B = k_RG_today_B / k_BAO_peak_Mpc_inv  # (local)
rel_diff_B = abs(k_RG_today_B - k_BAO_peak_Mpc_inv) / k_BAO_peak_Mpc_inv  # (local)
log10_ratio_B = np.log10(ratio_B) if ratio_B > 0 else -np.inf  # (local)

print(f"\n  Interpretation A (physical wavelength stretch):")
print(f"    k_RG_A / k_BAO            = {ratio_A:.4e}")
print(f"    log10(k_RG_A / k_BAO)     = {log10_ratio_A:+.4f}")
print(f"    |k_RG_A - k_BAO| / k_BAO  = {rel_diff_A:.4e}")
print(f"")
print(f"  Interpretation B (comoving, S73B convention):")
print(f"    k_RG_B / k_BAO            = {ratio_B:.4e}")
print(f"    log10(k_RG_B / k_BAO)     = {log10_ratio_B:+.4f}")
print(f"    |k_RG_B - k_BAO| / k_BAO  = {rel_diff_B:.4e}")

# Primary gate uses Interpretation A (matches prompt formula).
ratio_k_RG_over_k_BAO = ratio_A  # (local)
rel_diff = rel_diff_A  # (local)
log10_ratio = log10_ratio_A  # (local)

# Pre-registered gate evaluation
print("\n[6] Gate verdict")
print("-" * 72)

gate_name = "STRUCTURE-RG-SCALE-74"  # (local)
gate_pass_threshold = 0.10  # (local) 10%
gate_info_threshold = 0.30  # (local) 30%

if rel_diff <= gate_pass_threshold:
    gate_verdict = "PASS"  # (local)
    gate_detail = (
        f"k_RG = {k_RG_today_inv_Mpc:.4e} Mpc^{{-1}} matches "
        f"k_BAO = {k_BAO_peak_Mpc_inv} Mpc^{{-1}} within {rel_diff*100:.1f}% "
        f"(<= 10% PASS threshold)"
    )  # (local)
elif rel_diff <= gate_info_threshold:
    gate_verdict = "INFO"  # (local)
    gate_detail = (
        f"k_RG = {k_RG_today_inv_Mpc:.4e} Mpc^{{-1}} matches "
        f"k_BAO = {k_BAO_peak_Mpc_inv} Mpc^{{-1}} within {rel_diff*100:.1f}% "
        f"(between 10% and 30%)"
    )  # (local)
else:
    gate_verdict = "FAIL"  # (local)
    gate_detail = (
        f"k_RG = {k_RG_today_inv_Mpc:.4e} Mpc^{{-1}} is {log10_ratio:+.2f} "
        f"OOM from k_BAO = {k_BAO_peak_Mpc_inv} Mpc^{{-1}} (relative "
        f"deviation {rel_diff:.2e} > 30%)"
    )  # (local)

print(f"  Gate: {gate_name}")
print(f"  Verdict: {gate_verdict}")
print(f"  Detail: {gate_detail}")

# ---------------------------------------------------------------------
# 6. Cross-checks and alternate interpretations
# ---------------------------------------------------------------------
print("\n[7] Cross-checks")
print("-" * 72)

# Cross-check A: S73B CMB pivot consistency.
# S73B computed k_pivot_MKK = 4.304e-57 (dimensionless ratio = k in
# energy units / M_KK) for k_pivot = 0.05 Mpc^{-1} today.  Our method,
# applied to <Delta E> * M_KK, should give the same translation.
# A self-consistency test: take k_pivot_MKK_ref, translate via our
# method, and recover 0.05 Mpc^{-1} at today.
k_pivot_MKK_to_GeV = k_pivot_MKK_ref * M_KK  # (local) GeV (fold units)
# k_pivot_MKK_ref is ALREADY a today-measurement mapped to fold units:
# it says the CMB pivot corresponds to comoving k = 4.3e-57 in M_KK.
# Our <Delta E> in M_KK is ~1e-2 M_KK -> much HIGHER than k_pivot.
# So our level-spacing probes SUB-BAO scales: k >> k_BAO.

# Let's compute the S73B pivot back to Mpc^{-1} via our forward path:
k_pivot_MKK_to_fold_invMpc = k_pivot_MKK_to_GeV / hbar_c_GeV_m * Mpc_to_m  # (local)
k_pivot_MKK_to_today_invMpc = k_pivot_MKK_to_fold_invMpc * a_fold_over_today  # (local)

print(f"  Cross-check A -- recover S73B CMB pivot (should give 0.05 Mpc^{{-1}}):")
print(f"    k_pivot_MKK (S73B)                 = {k_pivot_MKK_ref:.4e}")
print(f"    -> k_pivot (at fold)               = {k_pivot_MKK_to_fold_invMpc:.4e} Mpc^{{-1}}")
print(f"    -> k_pivot (today, via a_f/a_t)    = {k_pivot_MKK_to_today_invMpc:.4e} Mpc^{{-1}}")
print(f"    Target                             = 0.05 Mpc^{{-1}}")
print(f"    Relative error on round-trip        = {abs(k_pivot_MKK_to_today_invMpc - 0.05)/0.05:.2e}")

# NOTE: the round-trip error here should be tiny -- any significant
# error would indicate an inconsistency in our projection.

# Cross-check B: if we instead compute the level density (inverse
# spacing) and translate, does it land on the BAO scale?
level_density_MKK = 1.0 / mean_dE_MKK  # (local) 1/M_KK ... N_states per M_KK
print(f"\n  Cross-check B -- level density per M_KK:")
print(f"    1 / <Delta E> = {level_density_MKK:.4e} states / M_KK")
# This is a spectral density, not a wavenumber -- interpretive only.

# Cross-check C: what k_today would coincide with the BAO peak?
# Invert the map to find the required <Delta E> in M_KK.
k_BAO_needed_at_fold_invMpc = k_BAO_peak_Mpc_inv * a_today_over_fold  # (local) Mpc^{-1} at fold
k_BAO_needed_GeV = k_BAO_needed_at_fold_invMpc * hbar_c_GeV_m / Mpc_to_m  # (local) GeV
dE_needed_MKK = k_BAO_needed_GeV / M_KK  # (local)

print(f"\n  Cross-check C -- <Delta E> required to hit k_BAO = 0.1 Mpc^{{-1}}:")
print(f"    dE_needed = {dE_needed_MKK:.4e} M_KK")
print(f"    Actual    = {mean_dE_MKK:.4e} M_KK")
print(f"    Ratio actual / required = {mean_dE_MKK / dE_needed_MKK:.4e}")
print(f"    log10(ratio)            = {np.log10(mean_dE_MKK / dE_needed_MKK):+.2f}")

# Cross-check D: alternative BAO-peak targets and their gate verdicts,
# reported for BOTH interpretations.
print(f"\n  Cross-check D -- gate verdicts against alternative BAO-like scales:")
alt_targets = {
    "k_BAO_peak       (0.1 Mpc^-1)":   k_BAO_peak_Mpc_inv,  # (local)
    "k_BAO_sound_hor  (0.0427)":       k_BAO_sound_horizon,  # (local)
    "k_BAO_secondary  (0.06)":         k_BAO_secondary,  # (local)
    "k_CMB_pivot      (0.05)":         k_CMB_pivot,  # (local)
}  # (local)

def _tag(rd):  # (local)
    return "PASS" if rd <= 0.10 else ("INFO" if rd <= 0.30 else "FAIL")

print(f"    {'scale':<35s} {'log10(k_RG_A/k)':>15s}  {'tag_A':>6s}    {'log10(k_RG_B/k)':>15s}  {'tag_B':>6s}")
for name, kval in alt_targets.items():
    rd_A = abs(k_RG_today_A - kval) / kval  # (local)
    rd_B = abs(k_RG_today_B - kval) / kval  # (local)
    log10_rd_A = np.log10(k_RG_today_A / kval) if k_RG_today_A > 0 else -np.inf  # (local)
    log10_rd_B = np.log10(k_RG_today_B / kval) if k_RG_today_B > 0 else -np.inf  # (local)
    print(f"    {name:<35s} {log10_rd_A:+15.2f}  {_tag(rd_A):>6s}    {log10_rd_B:+15.2f}  {_tag(rd_B):>6s}")

# ---------------------------------------------------------------------
# 7. Save results
# ---------------------------------------------------------------------
print("\n[8] Saving results")
print("-" * 72)

out_path = "s74_structure_rg_scale.npz"  # (local)

np.savez(
    out_path,
    # Gate metadata
    gate_name=gate_name,
    gate_verdict=gate_verdict,
    gate_detail=gate_detail,
    # Inputs
    N_modes=N_modes_in,
    N_cells=N_cells_in,
    N_pair=N_pair_in,
    dim_total=dim_total_in,
    r_overall=r_overall_in,
    # R-G level spectrum moments
    mean_dE_MKK=mean_dE_MKK,
    median_dE_MKK=median_dE_MKK,
    std_dE_MKK=std_dE_MKK,
    mean_dE_GeV=mean_dE_GeV,
    N_evals_pooled=N_evals,
    global_range_MKK=global_range_MKK,
    mean_dE_range_MKK=mean_dE_range_MKK,
    # Expansion history
    N_total=N_total,
    z_fold=z_fold,
    a_today_over_fold=a_today_over_fold,
    a_fold_over_today=a_fold_over_today,
    H_phys_fold_MKK=H_phys_fold_MKK,
    H_phys_fold_GeV=H_phys_fold_GeV,
    # Projection result
    k_fold_inv_m=k_fold_inv_m,
    k_fold_inv_Mpc=k_fold_inv_Mpc,
    k_RG_today_inv_Mpc=k_RG_today_inv_Mpc,
    k_RG_today_alt=k_RG_today_alt,
    k_RG_today_A=k_RG_today_A,
    k_RG_today_B=k_RG_today_B,
    # BAO comparison
    k_BAO_peak_Mpc_inv=k_BAO_peak_Mpc_inv,
    k_BAO_sound_horizon=k_BAO_sound_horizon,
    k_BAO_secondary=k_BAO_secondary,
    k_CMB_pivot=k_CMB_pivot,
    ratio_k_RG_over_k_BAO=ratio_k_RG_over_k_BAO,
    log10_ratio=log10_ratio,
    rel_diff=rel_diff,
    ratio_A=ratio_A,
    rel_diff_A=rel_diff_A,
    log10_ratio_A=log10_ratio_A,
    ratio_B=ratio_B,
    rel_diff_B=rel_diff_B,
    log10_ratio_B=log10_ratio_B,
    # Cross-check
    k_pivot_MKK_to_today_invMpc=k_pivot_MKK_to_today_invMpc,
    dE_needed_for_BAO_MKK=dE_needed_MKK,
    # Per-sector spacings (for auditability)
    mean_dE_k0=float(spacings_by_sector["k0"].mean()),
    mean_dE_kpi_2=float(spacings_by_sector["kpi_2"].mean()),
    mean_dE_kpi=float(spacings_by_sector["kpi"].mean()),
    mean_dE_k3pi_2=float(spacings_by_sector["k3pi_2"].mean()),
    # Canonical constants used
    M_KK_used=M_KK,
    hbar_c_GeV_m=hbar_c_GeV_m,
    Mpc_to_m=Mpc_to_m,
    tau_fold=tau_fold,
    N_cells_canonical=N_cells,
    elapsed_s=time.time() - t0,  # (local)
)

print(f"  Saved: {out_path}")
print(f"  Elapsed: {time.time() - t0:.2f} s")

print("\n" + "=" * 72)
print(f"GATE {gate_name}: {gate_verdict}")
print("=" * 72)
print(gate_detail)
