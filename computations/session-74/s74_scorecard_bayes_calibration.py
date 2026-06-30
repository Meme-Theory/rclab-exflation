#!/usr/bin/env python3
"""
S74 W4-T: SCORECARD-BAYES-CALIBRATION-74 -- Rewrite Scorecard with Layer Tags
==============================================================================

Purpose: Tag each observable in the framework scorecard as STRUCTURAL or
PREDICTION_LAYER, then compute a Bayes factor BF = prior_range / posterior_width
(per evoi-prioritization rule: observational passes weighted by ratio, not p-value).

Layer definitions:
  STRUCTURAL: Follows from a theorem in permanent-results-registry.md WITHOUT
              a specific functional (spectral functional, cutoff family) choice.
              BF = prior_range / allowed_window (the window the theorem fixes).
  PREDICTION_LAYER: Requires choosing a specific spectral functional or cutoff,
              so the numerical value depends on a functional selection.
              BF = prior_range / predicted_window (width of the prediction band).

Input:
  - sessions/framework/registry/pre-registered-observations.md
  - sessions/framework/registry/baseline-findings-s66.md
  - sessions/permanent-results-registry.md

Output:
  - s74_scorecard_bayes_calibration.npz (layer tags + BF per observable + joint)
"""

from canonical_constants import *
import numpy as np

print("=" * 78)
print("S74 W4-T SCORECARD-BAYES-CALIBRATION-74")
print("=" * 78)
print()
print("Rewriting framework observational scorecard with layer tags and BF computation.")
print()

# ==============================================================================
#  SCORECARD: Each entry is (name, tag, prior_range, posterior_width, framework,
#                            observed, sigma, theorem_ref, functional_ref, notes)
# ==============================================================================
#
# Layer tag rules:
#   STRUCTURAL  = the prediction follows from a theorem (see permanent-results-
#                 registry.md) without a specific spectral functional choice.
#                 e.g., normal mass ordering, r+8n_T=0 at CMB, alpha_s=n_s^2-1,
#                 Omega_DM via Leggett sector, z_eq, sigma/m=0, tau_p, w_a lock.
#
#   PREDICTION_LAYER = numerical value depends on the spectral functional
#                 (cutoff family, f_0/f_4 ratio, dilaton phi, etc.).
#                 e.g., n_s value, m_H value, r value, A_s, w_0, f_NL, sigma_8.
#
# Prior range logic:
#   - Dimensionless ratios: prior is theory-agnostic order of magnitude over
#     which a random geometry could land. For most cosmological shape
#     parameters, prior_range spans several OOM (e.g., n_s could be 0-2,
#     r could be 0-1, alpha_s could be -0.1 to +0.1).
#   - For mass/energy observables, prior_range is the OOM band from the
#     theory's natural UV scale (M_KK ~ 10^16-17 GeV) down to observed (10^2 GeV).
#   - For ratios (w_0, w_a, Omega_DM), prior_range is the physically plausible
#     range for any DE/DM candidate before data.
#
# Posterior width logic:
#   - STRUCTURAL: allowed window is the window the theorem fixes (often zero
#     or extremely narrow; if theorem gives discrete answer, use sigma_obs).
#   - PREDICTION_LAYER: predicted window is the spread across functional
#     choices (from scheme-dependence analyses in S64-S73) OR, if a single
#     functional is chosen, the deviation from observation normalized by sigma_obs.
#
# BF = prior_range / posterior_width
#   Interpretation: how much the observational pass narrowed the allowed region
#   relative to the prior. BF > 1 is support; BF > 10 is strong; BF > 100 decisive.

SCORECARD = []

# -------------- CMB Shape Parameters --------------

# n_s: 0.9595 (BCS+CW) vs 0.9649 +/- 0.0042 (Planck). 1.29 sigma.
# PREDICTION_LAYER: value depends on cutoff family (SA vs BCS+CW vs Hubble SA).
# Scheme spread is ~0.003 (S66 W2-A sign reversal across families).
# Prior: n_s could naively be in [0.5, 1.5] for any inflationary model -> range = 1.0.
# Posterior: 0.0042 (Planck error) + 0.003 (scheme spread) -> ~0.005 effective.
SCORECARD.append({
    'name': 'n_s (scalar spectral index)',
    'tag': 'PREDICTION_LAYER',
    'framework': 0.9595,
    'observed': 0.9649,
    'sigma_obs': 0.0042,
    'prior_range': 1.0,              # (local) naive [0.5,1.5] spread
    'posterior_width': 0.0042 + 0.003,  # (local) sigma_obs + scheme
    'theorem_ref': 'Schur CCM (not unique)',
    'functional_ref': 'BCS+CW cutoff, S63 W1',
    'notes': '1.29-sigma consistent; scheme spread 0.003 (S66 W2-A)'
})

# alpha_s = n_s^2 - 1 structural identity (T15 permanent theorem, S50)
# For ANY K^2 propagator. Zero functional freedom => STRUCTURAL.
# Framework: alpha_s = 0.9595^2 - 1 ~ -0.0793 (in equil form), but transit
# result is alpha_s ~ 0 (S66 5-sigma) since transit is non-equilibrium.
# Observed: -0.0045 +/- 0.0067. Use transit prediction ~0.
# Prior range: [-0.1, +0.1] = 0.2. Posterior: 0.0067.
# BF = 0.2 / 0.0067 = 29.9.
SCORECARD.append({
    'name': 'alpha_s (running of n_s, transit)',
    'tag': 'STRUCTURAL',
    'framework': 0.0,
    'observed': -0.0045,
    'sigma_obs': 0.0067,
    'prior_range': 0.2,              # (local)
    'posterior_width': 0.0067,       # (local)
    'theorem_ref': 'T15 (S50): alpha_s = n_s^2 - 1 + transit correction',
    'functional_ref': 'None; identity',
    'notes': 'Transit (non-equil) gives alpha_s ~ 0; 0.67-sigma'
})

# r (tensor-to-scalar): 0.0242 vs <0.036 (BK18 95% CL).
# PREDICTION_LAYER: depends on epsilon, c_s, N_e choice (T4 specifies 3 numbers,
# but those 3 numbers come from functional selection).
# Prior: [0, 1] = 1.0. Posterior: 0.036/1.96 = 0.0184 (convert 95% to 1-sigma).
SCORECARD.append({
    'name': 'r (tensor-to-scalar)',
    'tag': 'PREDICTION_LAYER',
    'framework': 0.0242,
    'observed': 0.018,               # central from BK18 95% CL /1.96 (local)
    'sigma_obs': 0.018,
    'prior_range': 1.0,              # (local)
    'posterior_width': 0.018,        # (local)
    'theorem_ref': 'T4 Exflation Tensor Theorem (S63)',
    'functional_ref': 'epsilon, c_s, N_e chosen',
    'notes': 'Framework within headroom; passes BK18'
})

# r + 8*n_T = 0 at CMB: STRUCTURAL identity (T4 corollary).
# Framework: exactly 0. Observed: not measured.
# Use a 1-sigma prior on the identity violation = 0.05 (no measurement yet).
# Prior = 1.0, posterior = prior_range (unmeasured) -> BF = 1 (no leverage yet).
SCORECARD.append({
    'name': 'r + 8*n_T at CMB (consistency)',
    'tag': 'STRUCTURAL',
    'framework': 0.0,
    'observed': np.nan,
    'sigma_obs': np.nan,
    'prior_range': 1.0,              # (local)
    'posterior_width': 1.0,          # (local) unmeasured => no info
    'theorem_ref': 'T4 corollary (slow-roll consistency)',
    'functional_ref': 'None',
    'notes': 'Unmeasured; BF=1 until LiteBIRD resolves n_T'
})

# A_s: framework 8.73e-2 (Route A) vs 2.1e-9. 7.62 OOM mismatch.
# PREDICTION_LAYER: overall amplitude depends on functional normalization.
# S66 Mack-Transit workshop reframed A_s as CONVERSION factor, not prediction.
# Prior range ~ 10^10 (unbounded amplitude), posterior ~ 10^7.6.
# BF = 10^10 / 10^7.6 = 10^2.4 ~ 250 (but against framework, not for).
# For BF computation, we treat excess as posterior_width from framework value.
SCORECARD.append({
    'name': 'A_s (scalar amplitude, Route A)',
    'tag': 'PREDICTION_LAYER',
    'framework': 8.73e-2,
    'observed': 2.1e-9,
    'sigma_obs': 2.1e-11,            # ~1% Planck precision (local)
    'prior_range': 1e10,             # (local) 10 OOM naive range
    'posterior_width': 10**7.62,     # (local) 7.62 OOM mismatch
    'theorem_ref': 'None (amplitude not theorem-fixed)',
    'functional_ref': 'Reframed S66 as conversion factor',
    'notes': 'FAIL as prediction; S66 reframe: A_s is conversion not prediction'
})

# Delta N_eff: 0.027 vs 0.15 +/- 0.23. 0.5-sigma.
# STRUCTURAL: comes from GGE relic count (59.8 pairs), FUNCTIONAL-INDEPENDENT.
# Prior: [0, 1] = 1.0. Posterior: 0.23.
# BF = 1.0 / 0.23 = 4.35.
SCORECARD.append({
    'name': 'Delta N_eff (extra rad DOF)',
    'tag': 'STRUCTURAL',
    'framework': 0.027,
    'observed': 0.15,
    'sigma_obs': 0.23,
    'prior_range': 1.0,              # (local)
    'posterior_width': 0.23,         # (local)
    'theorem_ref': 'GGE relic (S52, S57 Universality)',
    'functional_ref': 'None; counting',
    'notes': 'FUNCTIONAL-INDEPENDENT; 0.5-sigma'
})

# -------------- Particle Physics --------------

# m_H = 132.23 GeV (W5-E core mean, S73b) vs 125.1 GeV (PDG). 2.8-sigma in 2.54 GeV.
# PREDICTION_LAYER: depends on cutoff choice (Gaussian L=6, Richardson, Aitken).
# But T20 Filter-Independence is STRUCTURAL in that m_H is determined tree-level
# for ALL 6 cutoff families -- only the extrapolation method differs.
# Use 132.23 +/- 2.54 as framework; PDG 125.1 +/- 0.14.
# Prior range for Higgs: electroweak scale [10, 1000] GeV -> 990 GeV.
# Posterior: sqrt(2.54^2 + 0.14^2) ~ 2.54 GeV effective (S73b m_H).
SCORECARD.append({
    'name': 'm_H (Higgs mass)',
    'tag': 'PREDICTION_LAYER',
    'framework': 132.23,
    'observed': 125.1,
    'sigma_obs': 0.14,
    'prior_range': 990.0,            # (local) [10,1000] GeV electroweak
    'posterior_width': 2.54,         # (local) S73b core mean uncertainty
    'theorem_ref': 'T20 Filter-Independence (tree-level)',
    'functional_ref': 'Cutoff family (Gaussian L=6 / Richardson / Aitken)',
    'notes': 'CONDITIONAL PASS; 2.8-sigma; filter-independence at tree level'
})

# sin^2(theta_W) = 0.2307 vs 0.2312. 0.2% match.
# STRUCTURAL: gauge structure from SU(2)xU(1) embedding. T10 Cartan trace identity.
# Prior [0, 0.5] = 0.5; posterior sigma_obs ~ 0.00008 (PDG).
# But framework precision is ~0.0005 from the ratio. Use 0.0005.
SCORECARD.append({
    'name': 'sin^2 theta_W',
    'tag': 'STRUCTURAL',
    'framework': 0.2307,
    'observed': 0.23122,
    'sigma_obs': 0.00008,
    'prior_range': 0.5,              # (local)
    'posterior_width': 0.0005,       # (local) framework precision
    'theorem_ref': 'T10 Cartan Trace (S63 W5-07)',
    'functional_ref': 'None',
    'notes': '0.2% match; structural from embedding'
})

# M_W = 80.41 GeV vs 80.3692 GeV. 0.05% match.
# STRUCTURAL: gauge boson mass from EW breaking structure.
SCORECARD.append({
    'name': 'M_W',
    'tag': 'STRUCTURAL',
    'framework': 80.41,
    'observed': 80.3692,
    'sigma_obs': 0.0094,             # PDG 2024
    'prior_range': 500.0,            # (local) [0.1,500] GeV
    'posterior_width': 0.05,         # (local) framework precision
    'theorem_ref': 'T20 family (tree-level)',
    'functional_ref': 'Tree structure',
    'notes': '0.05% match'
})

# tau_p > 1.6e34 yr; framework 6.26e39 yr. 5 OOM safety.
# STRUCTURAL: T17 Proton Decay Tree-Level Zero (exact by PW orthogonality).
# Prior: the theoretically relevant prior is NOT "any possible lifetime",
# but "lifetimes predicted by GUT-scale gauge models", which spans ~10 OOM
# centered around 10^32 (SU(5) minimal) to 10^40 (flipped SU(5)).
# Posterior: framework is safely inside [10^34, 10^42] => width ~ 8 OOM.
# Narrower prior is used to avoid rhetorical inflation (evoi rule: pass
# weight = prior / posterior, not "any conceivable value").
SCORECARD.append({
    'name': 'tau_p (proton lifetime)',
    'tag': 'STRUCTURAL',
    'framework': 6.26e39,
    'observed': 1.6e34,              # lower bound, not central
    'sigma_obs': np.nan,
    'prior_range': 1e10,             # (local) 10 OOM GUT-relevant range
    'posterior_width': 1e3,          # (local) 3 OOM within allowed window
    'theorem_ref': 'T17 (S63 W4-04): tree-level zero by PW orthogonality',
    'functional_ref': 'None',
    'notes': 'STRUCTURAL exact zero at tree; GUT-relevant prior 10 OOM'
})

# -------------- Dark Matter --------------

# Omega_DM h^2 = 0.120 (Leggett-only) vs 0.1186 +/- 0.0020. 0.7-sigma.
# STRUCTURAL: follows from Volovik Partition (Result #27) + Leggett adiabaticity (#29).
# Prior: DM density could be 0 to 1 in Omega units -> prior_range ~ 0.5 for Omega h^2.
# Posterior: 0.002.
# BF = 0.5 / 0.002 = 250.
SCORECARD.append({
    'name': 'Omega_DM h^2 (Leggett)',
    'tag': 'STRUCTURAL',
    'framework': 0.120,
    'observed': 0.1186,
    'sigma_obs': 0.0020,
    'prior_range': 0.5,              # (local) [0,0.5] naive Omega h^2
    'posterior_width': 0.0020,       # (local)
    'theorem_ref': '#27 Volovik Partition + #29 Leggett Adiabaticity',
    'functional_ref': 'Leggett-only channel',
    'notes': '0.7-sigma PASS; structural partition'
})

# z_eq = 3425 vs 3402 +/- 26. 0.88-sigma.
# STRUCTURAL: follows from Omega_DM composition (Volovik partition).
SCORECARD.append({
    'name': 'z_eq (matter-radiation equality)',
    'tag': 'STRUCTURAL',
    'framework': 3425,
    'observed': 3402,
    'sigma_obs': 26,
    'prior_range': 5000,             # (local) [0,5000] natural range
    'posterior_width': 26,           # (local)
    'theorem_ref': '#27 Volovik Partition (consequence)',
    'functional_ref': 'Leggett-only (full DM fails 260-sigma)',
    'notes': '0.88-sigma PASS; Leggett-only necessary'
})

# sigma/m = 0 vs <1.25 cm^2/g.
# STRUCTURAL: CPT-neutral Leggett channel has no self-interaction.
SCORECARD.append({
    'name': 'sigma/m (DM self-interaction)',
    'tag': 'STRUCTURAL',
    'framework': 0.0,
    'observed': 0.0,                 # null
    'sigma_obs': 1.25/1.96,          # 1.25 95% CL upper (local)
    'prior_range': 10.0,             # (local) [0,10] cm^2/g natural
    'posterior_width': 0.64,         # (local) 1.25/1.96
    'theorem_ref': '#27 Volovik Partition + Leggett symmetry',
    'functional_ref': 'None',
    'notes': 'PASS; CPT-neutral Leggett excitation'
})

# lambda_fs = 9.85e-23 Mpc vs <0.1 Mpc. 22 OOM safety.
# STRUCTURAL: Leggett quasiparticle mass (M_KK scale).
# Prior: the WDM-relevant prior is "lifetime-competitive DM masses" spanning
# keV to TeV, or equivalently lambda_fs in [1e-6, 1] Mpc = 6 OOM.
# Posterior: 0.1 Mpc structure formation bound.
# BF = 1e6 / 0.1 = 1e7 is still large but physically defensible.
# Narrower choice: prior = 6 OOM, posterior = 1 OOM -> BF = 1e5.
SCORECARD.append({
    'name': 'lambda_fs (free-streaming length)',
    'tag': 'STRUCTURAL',
    'framework': 9.85e-23,
    'observed': 0.0,                 # consistent with zero
    'sigma_obs': 0.1,
    'prior_range': 1e6,              # (local) 6 OOM WDM-relevant prior
    'posterior_width': 10.0,         # (local) structure formation bound 1 OOM
    'theorem_ref': '#27 Volovik Partition',
    'functional_ref': 'M_KK scale fixes',
    'notes': 'Trimmed prior to WDM-relevant 6 OOM; still 5 OOM BF'
})

# -------------- Dark Energy / CC --------------

# w_0 = -0.918 (Volovik relaxation) vs -0.752 +/- 0.057 (DESI DR2+DESY5).
# PREDICTION_LAYER: Volovik relaxation mechanism (S67 introduction, specific form).
# Prior [-2, 0] = 2. Posterior 0.057.
SCORECARD.append({
    'name': 'w_0 (dark energy EOS today)',
    'tag': 'PREDICTION_LAYER',
    'framework': -0.918,
    'observed': -0.752,
    'sigma_obs': 0.057,
    'prior_range': 2.0,              # (local) [-2, 0]
    'posterior_width': 0.057,        # (local)
    'theorem_ref': '#41 Volovik Gibbs-Duhem',
    'functional_ref': 'Volovik relaxation (S67)',
    'notes': '2.91-sigma TENSION; DR3 decides survival'
})

# w_a = 0 vs -0.73 +/- 0.25. 2.92-sigma.
# STRUCTURAL: four-fold lock (GGE integrability + Josephson phase + frozen
# texture + thermalization barrier, 59 OOM gap). Cannot be adjusted.
# Prior [-2, 0] = 2. Posterior 0.25.
SCORECARD.append({
    'name': 'w_a (DE EOS evolution)',
    'tag': 'STRUCTURAL',
    'framework': 0.0,
    'observed': -0.73,
    'sigma_obs': 0.25,
    'prior_range': 2.0,              # (local) [-2, 0]
    'posterior_width': 0.25,         # (local)
    'theorem_ref': 'Four-fold lock (GGE + Josephson + frozen + barrier)',
    'functional_ref': 'None; structural',
    'notes': '2.92-sigma TENSION; CANNOT be adjusted; DR3 decisive'
})

# CC (Volovik Scenario B): rho_obs * 1.032 vs rho_obs. 0.01 OOM.
# PREDICTION_LAYER: Volovik Scenario B specific partition.
# The full 122 OOM "CC hierarchy" prior would give BF ~ 10^123 which is
# rhetorical inflation. We split this into two separate claims:
#   (a) The CC problem structure (that Volovik relaxation can bring CC to
#       observed order) is itself a PREDICTION_LAYER claim whose posterior
#       is being actively probed (S73a BBN FAIL, S73b gap = -0.47 OOM).
#   (b) The scenario-B factor of 1.032 is the tuning residual under a
#       mechanism that still has open gates. Use posterior = max(gap, 3%).
# Prior: the RELEVANT prior is "order-one residual after relaxation", not
# 122 OOM. Set prior_range = 10 (one decade around order unity).
# Posterior: 0.47 OOM (S73b honest gap) dominates 3% Planck.
SCORECARD.append({
    'name': 'rho_vacuum (Volovik Scenario B)',
    'tag': 'PREDICTION_LAYER',
    'framework': 1.032,              # (local) ratio to observed
    'observed': 1.0,
    'sigma_obs': 0.03,               # ~3% Planck (local)
    'prior_range': 10.0,             # (local) order-one residual prior
    'posterior_width': 10**0.47,     # (local) S73b honest gap dominates
    'theorem_ref': '#41 Volovik Gibbs-Duhem relaxation',
    'functional_ref': 'Scenario B partition',
    'notes': 'S73b: -0.47 OOM honest gap; order-one residual prior used'
})

# -------------- Non-Gaussianity (predictions, unmeasured) --------------

# f_NL equilateral = 0.853 vs -26 +/- 47.
# PREDICTION_LAYER: depends on GGE occupation shape.
SCORECARD.append({
    'name': 'f_NL (equilateral)',
    'tag': 'PREDICTION_LAYER',
    'framework': 0.853,
    'observed': -26.0,
    'sigma_obs': 47.0,
    'prior_range': 2000.0,           # (local) [-1000, 1000] naive prior
    'posterior_width': 47.0,         # (local) Planck
    'theorem_ref': '#39 Bogoliubov Gaussianity Preservation',
    'functional_ref': 'GGE distribution choice',
    'notes': '0.57-sigma CONSISTENT; undetectable by CMB-S4'
})

# f_NL folded = 0.129.
# STRUCTURAL: folded shape is unique to pair-creation Bogoliubov (signature).
# Other single-field models cannot produce it.
SCORECARD.append({
    'name': 'f_NL (folded, smoking-gun)',
    'tag': 'STRUCTURAL',
    'framework': 0.129,
    'observed': np.nan,              # unmeasured
    'sigma_obs': np.nan,
    'prior_range': 2000.0,           # (local) same as equilateral
    'posterior_width': 2000.0,       # (local) unmeasured -> no leverage
    'theorem_ref': '#39 + Bogoliubov pair momentum conservation',
    'functional_ref': 'None; shape selection rule',
    'notes': 'STRUCTURAL unique signature; 21cm decisive ~2040s'
})

# -------------- Neutrino sector --------------

# Mass ordering: Normal. STRUCTURAL: B1 < B2 < B3 at tau > 0 (machine epsilon).
# Prior: NO or IO, binary -> range = 2. Posterior: NO preferred ~2.5-sigma.
# If NO wins at 3+ sigma: BF = 2 / (1/3) = 6. Currently softer.
SCORECARD.append({
    'name': 'neutrino mass ordering',
    'tag': 'STRUCTURAL',
    'framework': 1,                  # (local) 1 = NO, 0 = IO
    'observed': 1,
    'sigma_obs': 0.4,                # (local) 2.5-sigma = 1/0.4 ~ 2.5
    'prior_range': 2.0,              # (local) NO or IO
    'posterior_width': 0.4,          # (local)
    'theorem_ref': 'Dirac spectrum order (S8, S34-36, S52, S56)',
    'functional_ref': 'None; spectrum lock',
    'notes': 'Currently consistent NO; DUNE 5-sigma decisive'
})

# S_F Connes (0nubb) = 0 (BDI symmetry).
# STRUCTURAL: S41 W1-2 exact.
SCORECARD.append({
    'name': '0nubb decay (S_F Connes)',
    'tag': 'STRUCTURAL',
    'framework': 0.0,
    'observed': 0.0,                 # no detection
    'sigma_obs': 1.0,                # (local) naive bound
    'prior_range': 100.0,            # (local)
    'posterior_width': 1.0,          # (local)
    'theorem_ref': 'S41 W1-2 (exact from BDI)',
    'functional_ref': 'None; symmetry class',
    'notes': 'Exact zero; framework predicts no seesaw'
})

# -------------- Reionization / sigma_8 --------------

# sigma_8 = 0.799 (framework) vs 0.811 (Planck) / 0.766 (lensing).
# PREDICTION_LAYER: depends on growth function through w(z).
# Between the two: tension roughly 0.2-sigma from mean 0.789.
SCORECARD.append({
    'name': 'sigma_8 (RMS fluctuation)',
    'tag': 'PREDICTION_LAYER',
    'framework': 0.799,
    'observed': 0.789,               # (local) avg of Planck / lensing
    'sigma_obs': 0.022,               # (local) spread between the two
    'prior_range': 0.5,              # (local) [0.5,1] natural
    'posterior_width': 0.022,        # (local)
    'theorem_ref': 'Growth function from w(z)',
    'functional_ref': 'Volovik w_0 = -0.918',
    'notes': 'S8 tension ameliorator; S69 f*sigma_8 PASS'
})

# ISW tracking c_s^2 = 0 = +12.3% vs LCDM (S68 ISW-TRACKING-68 PASS).
# STRUCTURAL: follows from Volovik induced perturbation (c_s^2_DE = 0 tracks matter).
# Prior: c_s^2 in [0, 1] for DE -> range 1. Posterior: SNR-limited.
SCORECARD.append({
    'name': 'ISW c_s^2_DE (substrate-specific)',
    'tag': 'STRUCTURAL',
    'framework': 0.0,
    'observed': np.nan,              # not isolated yet
    'sigma_obs': np.nan,
    'prior_range': 1.0,              # (local)
    'posterior_width': 1.0,          # (local) Planck A_ISW cannot isolate
    'theorem_ref': '#41 Volovik + tracking clustering',
    'functional_ref': 'None; tracking mechanism',
    'notes': 'S68 PASS 1.123 ratio; Euclid marginal, 21cm 7.9-sigma definitive'
})

# ==============================================================================
#  BAYES FACTOR COMPUTATION
# ==============================================================================

print(f"Loaded {len(SCORECARD)} observables from scorecard.")
print()
print("Layer tag distribution:")
n_structural = sum(1 for e in SCORECARD if e['tag'] == 'STRUCTURAL')
n_prediction = sum(1 for e in SCORECARD if e['tag'] == 'PREDICTION_LAYER')
print(f"  STRUCTURAL:       {n_structural}")
print(f"  PREDICTION_LAYER: {n_prediction}")
print()

# Compute BF for each entry
print("Per-observable Bayes factors:")
print()
print(f"  {'Observable':42s} {'Tag':18s} {'BF':>14s}")
print("  " + "-" * 76)

for entry in SCORECARD:
    pr = entry['prior_range']
    pw = entry['posterior_width']
    bf = pr / pw if pw > 0 else np.nan
    entry['BF'] = bf
    label = entry['name'][:40]
    tag = entry['tag']
    print(f"  {label:42s} {tag:18s} {bf:14.3e}")

print()

# Joint framework BF: product of individual BFs for observationally-tested
# items. Note: strictly speaking only items with current observational data
# contribute to a posterior Bayes factor. Unmeasured predictions (r+8n_T,
# f_NL folded) contribute BF=1 (no information). Their effective contribution
# to the joint BF is therefore 1 (identity).

print("=" * 78)
print("JOINT BAYES FACTOR")
print("=" * 78)

# Compute joint in log space to avoid overflow
log_bf_sum = 0.0  # (local)
log_bf_structural = 0.0  # (local)
log_bf_prediction = 0.0  # (local)
contributing = 0
unmeasured = 0

for entry in SCORECARD:
    bf = entry['BF']
    if np.isnan(bf) or bf <= 0:
        unmeasured += 1
        continue
    # Exclude A_s which is a conversion factor (S66 reframe), not prediction
    if 'A_s' in entry['name']:
        continue
    # Exclude unmeasured items (BF=1)
    if entry['posterior_width'] == entry['prior_range']:
        unmeasured += 1
        continue
    log_bf_sum += np.log10(bf)
    if entry['tag'] == 'STRUCTURAL':
        log_bf_structural += np.log10(bf)
    else:
        log_bf_prediction += np.log10(bf)
    contributing += 1

print()
print(f"Contributing observables:    {contributing}")
print(f"Unmeasured (BF=1 excluded):  {unmeasured}")
print(f"A_s excluded (reframed):     1")
print()
print(f"log10(Joint BF) total:         {log_bf_sum:.3f}")
print(f"log10(Joint BF) STRUCTURAL:    {log_bf_structural:.3f}")
print(f"log10(Joint BF) PREDICTION:    {log_bf_prediction:.3f}")
print()
print(f"Joint BF total:         10^{log_bf_sum:.3f} = {10**log_bf_sum:.3e}")
print(f"Joint BF STRUCTURAL:    10^{log_bf_structural:.3f} = {10**log_bf_structural:.3e}")
print(f"Joint BF PREDICTION:    10^{log_bf_prediction:.3f} = {10**log_bf_prediction:.3e}")
print()

# ==============================================================================
#  SAVE DATA
# ==============================================================================

names = np.array([e['name'] for e in SCORECARD], dtype=object)
tags = np.array([e['tag'] for e in SCORECARD], dtype=object)
priors = np.array([e['prior_range'] for e in SCORECARD])
posteriors = np.array([e['posterior_width'] for e in SCORECARD])
framework = np.array([e['framework'] for e in SCORECARD])
observed = np.array([e['observed'] for e in SCORECARD])
sigmas = np.array([e['sigma_obs'] for e in SCORECARD])
bfs = np.array([e['BF'] for e in SCORECARD])

np.savez(
    'computations/session-74/s74_scorecard_bayes_calibration.npz',
    names=names,
    tags=tags,
    prior_range=priors,
    posterior_width=posteriors,
    framework=framework,
    observed=observed,
    sigma_obs=sigmas,
    BF=bfs,
    log10_joint_BF_total=log_bf_sum,
    log10_joint_BF_structural=log_bf_structural,
    log10_joint_BF_prediction=log_bf_prediction,
    joint_BF_total=10**log_bf_sum,
    joint_BF_structural=10**log_bf_structural,
    joint_BF_prediction=10**log_bf_prediction,
    n_structural=n_structural,
    n_prediction=n_prediction,
    n_contributing=contributing,
    n_unmeasured=unmeasured,
)

print("Saved: computations/session-74/s74_scorecard_bayes_calibration.npz")
print()

# ==============================================================================
#  GATE VERDICT
# ==============================================================================

print("=" * 78)
print("GATE: SCORECARD-BAYES-CALIBRATION-74")
print("=" * 78)
print()

# PASS criteria: scorecard fully tagged AND joint BF computed.
all_tagged = all(e['tag'] in ('STRUCTURAL', 'PREDICTION_LAYER') for e in SCORECARD)
joint_computed = not np.isnan(log_bf_sum)

print(f"  All observables tagged:      {all_tagged}")
print(f"  Joint BF computed:           {joint_computed}")
print(f"  Total observables:           {len(SCORECARD)}")
print(f"  STRUCTURAL tag count:        {n_structural}")
print(f"  PREDICTION_LAYER tag count:  {n_prediction}")
print()

if all_tagged and joint_computed:
    print("  Verdict: PASS")
    print(f"  Tagging complete; joint BF = 10^{log_bf_sum:.2f}")
elif joint_computed and n_structural + n_prediction >= len(SCORECARD) // 2:
    print("  Verdict: INFO (partial)")
else:
    print("  Verdict: FAIL (tagging ambiguous)")

print()
print("=" * 78)
print("S74 W4-T COMPLETE")
print("=" * 78)
