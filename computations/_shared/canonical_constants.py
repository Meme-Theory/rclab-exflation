#!/usr/bin/env python3
"""
Canonical Constants Module — Single Source of Truth
====================================================

Created: Session 45 (2026-03-15)
Purpose: Eliminate hardcoded constant drift across computations scripts.

Provenance audit (S44, AUDIT_UPSTREAM_ROOTS.md) found:
  - Three E_cond values (-0.115, -0.137, -0.156) used interchangeably
  - Two Vol(SU(3)) formulas (8880.9 vs 1349.7) in competing scripts
  - M_KK = 1e16 used where 7.43e16 (gravity) or 5.04e17 (Kerner) intended

Every constant below has a session/gate provenance comment.
The PROVENANCE dict (Section F) provides machine-readable lineage.

Usage:
    from canonical_constants import E_cond, tau_fold, M_KK_gravity
    from canonical_constants import PROVENANCE, warn_stale
"""

import sys
import numpy as np
import warnings
from fractions import Fraction  # S88 W-15 W15-V.2 (n_s_FW_exact bit-exact rational pin)

PI = np.pi

# ==============================================================================
sigma_r_BK_2026 = 0.005  # BICEP/Keck Array 2026 forecast 1-sigma on r (Ade+ 2025 preprint projection) (S84)
r_CMB_framework = 0.011731522176014426  # Framework r(k_CMB) from G46 tensor transfer PASS; 3.07x below BK18 95% CL (0.036) (S83)
g_star_BS_T_H_FW = 10.688550820980016  # Substrate-cascade-tail Kolb-Turner FD/BE integrated form (Eq. 3.62) evaluated at T_H=1.057 MeV (CF-39 anchor per S88 W6 §V.1) under Borsanyi-2016-anchored qcd_crossover_weight_borsanyi phase-weight from §W8-4 (audit_sha256=dba0b7911831829c3cf3fadac3e370e8a741cc46cec03ea7a0b9273533872b17); replaces S91 §W3-1 smooth-tanh INFO at T=1 GeV anchor with refined Borsanyi residual-confinement suppression model (T=1 GeV rel_dev 23.65%->0.00%). Gate audit_sha256=a7c5ac81088fcba39262a95ded0212ce8df271bb6485722fde0afbcf858fe256. (S92)
#  SECTION A: PDG / CODATA Universal Constants
# ==============================================================================

# Planck mass — two conventions, both used in the literature
M_Pl_reduced = 2.435e18        # GeV, M_Pl / sqrt(8*pi)
M_Pl_unreduced = 1.2209e19    # GeV, sqrt(hbar*c/G_N)

# Fundamental constants — SI
G_N = 6.67430e-11             # m^3 kg^{-1} s^{-2} (CODATA 2018)
c_light = 2.99792458e8        # m/s (exact)
hbar_SI = 1.054571817e-34     # J*s (CODATA 2018)
h_planck_SI = 6.62607015e-34  # J*s (exact, 2019 SI redefinition)
k_B = 8.617333262e-5          # eV/K (CODATA 2018)
k_B_SI = 1.380649e-23         # J/K (exact, 2019 SI redefinition)
eV_SI = 1.602176634e-19       # J per eV (exact)
eV_per_GeV = 1e9              # eV per GeV
A_Bohr = 0.529177210903e-10   # m (Bohr radius, CODATA 2018)
arcsec_to_rad = 4.84813681109536e-6  # radians per arcsecond
alpha_em_MZ_inv = 127.955     # 1/alpha_EM at M_Z (PDG 2024)
sin2_thetaW_MSbar = 0.23122   # sin^2(theta_W) MSbar at M_Z (PDG 2024)
M_Z = 91.1876                 # GeV (PDG 2024)
M_W = 80.3692                 # GeV (PDG 2024)

# Fundamental constants — CGS
G_N_cgs = 6.67430e-8          # cm^3 g^{-1} s^{-2}
c_light_cgs = 2.99792458e10   # cm/s
c_light_km_s = 2.99792458e5   # km/s

# Planck units & hbar variants
hbar_c_GeV_fm = 0.1973269804  # GeV * fm (exact in natural units)
hbar_c_GeV_m = 1.973269804e-16  # GeV * m
hbar_c_GeV_cm = 1.973269804e-14  # GeV * cm
hbar_eV_s = 6.582119569e-16   # eV * s (CODATA 2018)
hbar_GeV_s = 6.582119569e-25  # GeV * s (= hbar_eV_s / 1e9)
l_Planck = 1.616255e-35       # m (Planck length)
l_Planck_cm = 1.616255e-33    # cm
t_Planck = 5.391247e-44       # s (Planck time)

# Cosmological
H_0_km_s_Mpc = 67.4           # km/s/Mpc (Planck 2018)
H_0_inv_s = 2.184e-18         # s^{-1}
H_0_GeV = 1.438e-42           # GeV
T_CMB = 2.7255                # K (COBE/FIRAS)
T_CMB_GeV = 2.7255 * 8.617333262e-5 / 1e9  # = 2.348e-13 GeV
rho_Lambda_obs = 2.7e-47      # GeV^4 (observed CC, conventional rounding — see NOTE below)
# NOTE: Precise Planck 2018 value is 2.52e-47 GeV^4 (Omega_L=0.685, H_0=67.36).
# The 2.7e-47 rounding is widely used in the literature and across this codebase.
# The 2.888e-47 in some scripts uses a different density convention.
# All CC-gap calculations use ratios (rho_spectral / rho_obs), so the ~7% difference
# changes the gap by <0.03 orders out of 120 — negligible for all gate verdicts.
Lambda_obs_MP4 = 2.888e-122   # Lambda / M_Pl^4 (widely used convention in codebase)
A_s_CMB = 2.1e-9              # CMB scalar amplitude (Planck 2018)
A_s_Planck = A_s_CMB          # Alias per S85 W13 plan line 677 (Planck 2018 VI provenance)
Omega_r = 9.15e-5             # radiation density parameter (Planck 2018)

Omega_m = 0.315               # matter density parameter (Planck 2018)
Omega_b = 0.0493              # baryon density parameter (Planck 2018)
Omega_DM = Omega_m - Omega_b  # dark matter density parameter (= 0.266)
Omega_Lambda = 0.685          # dark energy density parameter (Planck 2018)
sigma_8 = 0.811               # matter fluctuation amplitude (Planck 2018)

# Critical density
rho_crit_GeV4 = 4.08e-47      # GeV^4 (3*H_0^2 / 8*pi*G in natural units)
rho_crit_cgs = 1.878e-29      # g/cm^3

# BBN / recombination
eta_BBN_obs = 6.12e-10        # baryon-to-photon ratio (Planck 2018 + BBN)
eta_BBN_err = 0.04e-10        # 1-sigma uncertainty
T_BBN_GeV = 1e-3              # BBN temperature (~1 MeV)
T_recomb_GeV = 0.26e-9        # recombination temperature (~0.26 eV)
z_BBN = 4e8                   # BBN redshift
t_universe_s = 4.35e17        # age of universe in seconds (Planck 2018)

# Observational bounds (used in multiple scripts)
sigma_FIRAS = 1.0e-6          # FIRAS spectral distortion bound (delta_mu)
FIRAS_dT_bound = 3.0e-6       # FIRAS temperature anisotropy bound (delta_T/T)

# S84 W5-57 MU-K-CORRIDOR closure (INFO verdict, schema R3, L_max=5).
# Provenance: computations/session-84/s84_w5_57_data.npz; value=8.694901226608577e-05
# recovered at K_max=3.556e5 with gamma_fit=0.9999999999999993 (gamma=1 exact
# lockout). Scheme: Zubarev (W5-57 convention); reference S84 plan §W5-57.
# Used by: S85 §W0-8 PIXIE mu-K endpoint pre-registration (this session).
mu_framework_W5_57 = 8.694901226608577e-05   # S84 W5-57 closure, K_max endpoint
K_endpoint_W5_57 = 3.556e5                    # S84 W5-57 K_corridor endpoint
gamma_lockout = 1.0                           # exact gamma=1 linearity lockout

# K-corridor endpoints (S85 W3 plan §W3-Wave-Machinery-Pin).
# K_R5: lower endpoint of inflationary sub-corridor (S84 W8a, R5/R6 boundary).
# K_crit: upper endpoint of inflationary sub-corridor (S84 W5-55, R6/R7 boundary).
# K_FIRAS: alias of K_endpoint_W5_57 (PIXIE mu-distortion endpoint, gamma=1 lockout).
K_R5 = 1.9222                                 # S84 W8a inflationary sub-corridor lower endpoint
K_crit = 91.5                                 # S84 W5-55 inflationary sub-corridor upper endpoint
# ─────────────────────────────────────────────────────────────
# K_crit_BdG: BdG-channel critical coupling
# ─────────────────────────────────────────────────────────────
# PROVENANCE: S62 W2 (Volovik BdG-channel derivation),
#             confirmed S82 W2-4 (R3 anchor numerical coincidence; K_base=2.035),
#             S85 W2-12 BdG band -> CMB l_crit projection (PROVEN, S7 combined landscape).
# CITATION:   sessions/permanent-results-registry.md (W2-12 theorem row)
# SOURCE:     active code reference: computations/session-85/s85_w2_band_detector_map.py
#             (S62 W2 producing script not in current repo tree; provenance via S85 W2-12 PROVEN).
# DISTINCT FROM:
#   K_crit = 91.5  (inflationary corridor critical coupling, S84 W5-55)
#   K_base = 2.035 (R3 band-weighted squeezing anchor, S82 W2-4 — numerical coincidence)
#   K_floor / K_wall (S85 W5-D.4 substrate-corridor brackets; pinned in W0c-4)
# UNITS:      dimensionless (coupling in M_KK units)
# ─────────────────────────────────────────────────────────────
K_crit_BdG = 2.035  # BdG-channel critical coupling (Volovik S62; S86 W0c-2)
K_FIRAS = K_endpoint_W5_57                    # alias: PIXIE mu-distortion endpoint = 3.556e5

# ─────────────────────────────────────────────────────────────
# S86 W0c-3 canonical-entry consolidation (5 entries)
# Plan reference: sessions/session-plan/session-86-plan-w0c.md §W0c-3
# Substrate-first provenance: each entry cites a framework first-principles
# computation as canonical; external lit refs are methodological only.
# ─────────────────────────────────────────────────────────────

# eps_H_HP1_norm: HP^1 norm of the eps_H cocycle (S84 W10a-114 lift)
# PROVENANCE: S84 W10a-114 PASS (legs 1/2/3 all PASS; eps_H_cocycle = HP1_representative
#             = cm_hopf_lift = 16.197718852989908 verified self-consistent).
# CITATION:   sessions/archive/session-84/session-84-s5-lizzi-cohomology-synthesis.md Result 1
# SOURCE:     computations/session-84/s84_w10a_114_eps_h_hp1_cocycle.npz key 'eps_H_cocycle'
# UNITS:      dimensionless (cocycle norm in HP^1 metric)
# DISTINCT FROM: ‖[eps_H]‖_F4 (5-atlas STRICT norm, 60-atlas LOOSE — different metrics)
# eps_H_HP1_norm = 16.197719
#
# PROVENANCE (CF-28 S90 W2; mack-cosmic-bridge writer; connes-ncg-theorist co-sign per W-2 CF-#5):
#   CLASS: PRIMARY canonical (anchors Class-(d) chain for R_universal_HP1_strict_F4; see CF-27 PROVENANCE)
#   DEFINITION: R_universal at ζ-regulator; BZ-trace on Jensen-deformed band-0 projector P_0(τ_fold)
#     - BZ-trace form: ∫_BZ Tr g_ab^{(P_0)}(k; τ_fold) d^d k (per cross-pillar-bridge-anatomy.md §VII.AF.1)
#     - regulator: ζ-regulator (CM-1995 §III.4 finite-spectral-triple residue formula)
#     - τ-anchor: τ_fold = 0.19 (R-PROTECTED; canonical_constants.py)
#     - L_max: 10 (Level-3 anchor at L_max=10 per registry-PASS criterion of §VII.AF.1.OP-PROJ)
#   SOURCE: S86 W-5 V4 substitution chain Step 1 line 397
#   substrate-IS level: Level 1 single-τ-slice at τ_fold (per phononic-framing.md K=2 MANDATORY since S88 W-7 V.4)
#   DOWNSTREAM CONSUMERS (Class-(d) DERIVATIVE forms cite this PRIMARY):
#     - R_universal_HP1_strict_F4 = 1.030902 (via DERIVATIVE relation 1/f_4_prefactor_sdw; see CF-27 PROVENANCE)
#   Audit-script verification: `_source_reconciliation_audit.py` no Class-(f) PLACEHOLDER flag post-emission
#   landed: CF-28 S90 W2 (mack-cosmic-bridge writer; connes-ncg-theorist co-sign)
eps_H_HP1_norm = 16.197719  # (S84 W10a-114; 6 sig figs)

# HP1_dim: framework-relevant dimension of HP^1(A_F) (rank-3 lattice)
# PROVENANCE: S84 W10a-117 R-protection classification + CM-2008 Table 2 (Chamseddine-Marcolli
#             quaternionic projective HP^1 standard topology; framework slot dim = 3 per
#             rank-3 image of ch: K_0 -> HP^0(A_F) classification).
# CITATION:   sessions/permanent-results-registry.md §VII.K (HP^1-content-distinct corridors)
# SOURCE:     computations/session-84/s84_w10a_117_r_protection_classification.csv (rank-3 row)
# UNITS:      dimensionless (real dimension of the rank-2 R-protection class)
# DISTINCT FROM: real-dim(HP^1) = 4 (full S^4); the 3 here is the framework-relevant slot dim.
HP1_dim = 3  # (CM-2008 Table 2; S84 W10a-117 confirmation)

# FI_parity_exclusion: parity-exclusion flag for FI/RD slot atlas (1 = enabled)
# PROVENANCE: S82 lizzi 42-row M_lizzi atlas (parity([eps_H]) = 1 mod 2; parity(ch(K_0)) = 0
#             mod 2 — disjoint parity classes establish exclusion).
# CITATION:   sessions/permanent-results-registry.md §VII.P-v2 (parity refinement)
# SOURCE:     S82 lizzi atlas spec + S84 W10a-115 GV-explicit cross-check
# UNITS:      boolean (1 = parity-exclusion active; 0 = inactive)
# DISTINCT FROM: rank exclusion below (parity is mod-2; rank is integer-valued).
FI_parity_exclusion = 1  # (S82 lizzi atlas; parity([eps_H]) = 1 mod 2)

# rank_exclusion: rank-class exclusion threshold for §VII.P-v2 corridors
# PROVENANCE: S84 W10a-117 R-protection classification — image(ch: K_0 -> HP^0(A_F))
#             is a rank-3 lattice; the rank=3 corridor is excluded vs the rank=1
#             Witten-integral corridor.
# CITATION:   sessions/permanent-results-registry.md §VII.K (rank-class)
# SOURCE:     computations/session-84/s84_w10a_117_r_protection_classification.csv
# UNITS:      dimensionless (rank threshold for exclusion class)
# DISTINCT FROM: HP1_dim = 3 (numerical coincidence; semantically distinct — rank vs dim).
rank_exclusion = 3  # (S84 W10a-117; rank-3 lattice)

# nonflat_T_correction_L2: non-flat T-correction at L_max=2 (substrate computation)
# PROVENANCE: S83 W2-G24 PASS (Cartan subbundle is FLAT at tau_fold; abelian Cartan
#             implies Gamma on C x C = 0; R|_(Cartan^4) = 0 to machine epsilon).
#             The non-flat T-correction is therefore negligible at L_max=2.
# CITATION:   computations/session-83/s83_w2_g24_nonflat_t_correction_l2.py + .npz
# SOURCE:     computations/session-83/s83_w2_g24_nonflat_t_correction_l2.npz key 'correction_P1_T'
# METHODOLOGICAL REFERENCE: vdd Chamseddine-Marcolli Particle Physics ACM (paper 06)
#             — the methodology for non-flat T-corrections is in this literature; the
#             numerical value for THIS framework's substrate at L_max=2 comes from S83 W2-G24.
#             (No §VI numbered heading exists in any of the 14 vdd papers; named-section
#             structure precludes direct §VI text extraction. Substrate computation is canonical.)
# UNITS:      M_KK^2 (curvature-class correction scale squared; zero is dimension-independent)
# DISTINCT FROM: flat-T baseline (zero by definition); higher-L_max corrections (defer to S87+).
nonflat_T_correction_L2 = 0.0  # (S83 W2-G24; substrate-flat at tau_fold)

# K-base and mu-FIRAS anchors (S85 W8-1 plan §W8-1 line 57: "add K_base=2.035,
# mu_FIRAS=9e-5 if missing — with S84 W5-65 provenance"). K_base is the R3
# band-weighted squeezing anchor from S82 W2-4; mu_FIRAS is the Fixsen+ 1996
# FIRAS 95% CL mu-distortion upper bound. Provenance: s84_w5_k_firas_coincidence.py
# lines 192-193 (S84 W5-65 INFO closure producer).
K_base = 2.035                                # R3 band-weighted squeezing anchor (S82 W2-4)
mu_FIRAS = 9.0e-5                             # Fixsen+ 1996 FIRAS mu-distortion 95% CL bound
mu_base_L5 = 4.9758503926e-10                 # mu(K=K_base, L=5) from S84 W5-57 MU-K-CORRIDOR

# PIXIE (Primordial Inflation Explorer) forecast spectral-distortion sigma.
# Reference: PIXIE Science Book, Table 2 (Kogut+ 2011 arXiv:1105.2044).
# 2-year mission 5-sigma mu sensitivity ~5e-8 -> 1-sigma ~1e-8.
sigma_mu_PIXIE = 1.0e-8       # PIXIE forecast 1-sigma mu-distortion sensitivity

# LCDM primordial mu-distortion reference (Chluba & Sunyaev 2012 ApJ 758 76):
# standard single-field slow-roll produces mu ~ 2e-8 from Silk damping of
# the adiabatic power spectrum between k_D_th and k_D_mu.
mu_LCDM_primordial = 2.0e-8   # Chluba-Sunyaev 2012 primordial mu baseline

# Conversion factors
GeV_to_inv_s = 1.5193e24      # 1 GeV -> s^{-1}
GeV_to_inv_m = 1.0 / hbar_c_GeV_m  # 1 GeV -> m^{-1} (= 5.068e15)
GeV_inv_to_Mpc = hbar_c_GeV_m / 3.0857e22  # = 6.39e-39 Mpc per GeV^{-1}
Mpc_to_GeV_inv = 3.0857e22 / hbar_c_GeV_m  # = 1.563e38 GeV^{-1} per Mpc
GeV_to_kg = 1.78266192e-27    # 1 GeV/c^2 -> kg
GeV_to_g = 1.78266192e-24     # 1 GeV/c^2 -> g
Mpc_to_fm = 3.0857e38         # 1 Mpc in fm
Mpc_to_m = 3.0857e22          # 1 Mpc in meters
Mpc_to_cm = 3.0857e24         # 1 Mpc in cm
Gpc_to_m = 3.0857e25          # 1 Gpc in meters
kpc_to_cm = 3.0857e21         # 1 kpc in cm

# ==============================================================================
# R_universal_HP1_strict_F4 = 1.030902
#
# PROVENANCE (CF-27 S90 W2; joint connes + lizzi co-sign per W-2 CF-#4):
#   CLASS: (d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY (per epistemic-discipline.md §"Source Reconciliation")
#   PRIMARY canonical: eps_H_HP1_norm = 16.197719 (see canonical_constants.py PROVENANCE entry CF-28)
#     - PRIMARY definition: R_universal at ζ-regulator; BZ-trace on Jensen-deformed band-0 projector at τ_fold
#     - PRIMARY source: S86 W-5 V4 substitution chain Step 1 line 397
#     - PRIMARY substrate-IS observable: Level 1 single-τ-slice at τ_fold per phononic-framing.md
#   DERIVATIVE relation: 1.030902 = 1/0.970024 modulo publication precision
#     where 0.970024 = f_4_prefactor_sdw (canonical_constants.py)
#     algebraic relation: R_universal_HP1_strict_F4 · f_4_prefactor_sdw ≡ 1 to Class-8.3 publication-precision
#   STRUCTURAL READING: F_4-atlas-spread band empirical value at L_max=10 (Level-3 anchor of §VII.AF.1.OP-PROJ)
#   NAME-DRIFT WARNING for downstream consumers:
#     - S88 W1b1 lines 129-133: downstream usage citing `1.030902` is a DERIVATIVE-FORM read;
#       must trace back to PRIMARY canonical `eps_H_HP1_norm = 16.197719` for substrate-IS observable provenance
#     - DO NOT independently re-derive from raw F_4 strict atlas values; the canonical substitution chain
#       (W-5 V4 Step 1 → Step 2) is the only authoritative derivation
#     - DOWNSTREAM CONSUMERS using `R_universal_HP1_strict_F4` in published quantities MUST cite both:
#       (a) this canonical pin name, AND
#       (b) the PRIMARY canonical name `eps_H_HP1_norm` per Class-(d) remediation table
#   Audit-script verification: `_source_reconciliation_audit.py` Class-(d) chain verification PASSes post-emission
#   Provenance chain: S86 W-5 V4 substitution chain Step 1 (PRIMARY) → Step 2 (this DERIVATIVE) → S88 W1b1 downstream
#   landed: CF-27 S90 W2 (mack-cosmic-bridge writer; connes + lizzi co-sign)
R_universal_HP1_strict_F4 = 1.030902  # Universal HP^1 strict F_4 ratio per W-5 V4 substitution chain Step 2. Downstream-cited via W-5 cross-pillar bridge theorem and W11-C5/C6 lab spec. (S86)
cocycle_norm_phi67 = 0.793346  # Cocycle norm phi_67 = delta_E_6 * delta_E_7 = 0.793346 M_KK^2 per W-5 C2 substrate-magnitude annotation. PROVENANCE (S93 W5-1): this 6-sf value IS round_to_6sf(0.8907 * 0.8907) = round_to_6sf(0.79334649) from the W8-4 M_3(C) Gell-Mann colour-block frame norm delta_E_6=delta_E_7=0.8907 (session-85-1b-3heb-inversion-connes.md:132-138). (S86; provenance pinned S93 W5-1)
cocycle_norm_phi88 = 0.108307  # Cocycle norm phi_88 = (delta_E_8)^2 = 0.108307 M_KK^2; Jensen-rate-limited at tau_fold=0.19 per W-5 C2. PROVENANCE (S93 W5-1): this 6-sf value IS round_to_6sf(0.3291^2) = round_to_6sf(0.10830681) from the W8-4 M_3(C) Cartan frame norm delta_E_8=0.3291; the full-float64 ratio (delta_E_6*delta_E_7)/(delta_E_8)^2 = 7.3249917525961665 is F2-faithful (see substrate_cocycle_ratio_67_88). (S86; provenance pinned S93 W5-1)
substrate_cocycle_ratio_67_88 = 7.3249917525961665  # RE-PINNED S93 W5-1 to substrate-first R_machine = (delta_E_6*delta_E_7)/(delta_E_8)^2 = Fraction(8814961,1203409), full float64, from the W8-4 M_3(C) Gell-Mann colour-block frame norms delta_E_6=delta_E_7=0.8907, delta_E_8=0.3291 (session-85-1b-3heb-inversion-connes.md:132-138, eq.8 commutator-Frobenius construction; the AUTHORITATIVE substrate-first source for this observable, reproducing cocycle_norm_phi67/phi88 by the recorded round-to-6sf operation). BRANCH = F2-faithful: round_to_6sf(R_machine)=7.32499 = round_to_6sf(F2); dist_to_F2=2.47e-7 << dist_to_F1=1.74e-5. The prior pin 7.324992 WAS F2 = Fraction(114453,15625), correct to its published 6 sf; this re-pin sharpens to the 7th digit. The S92 W7 historiographic question is ARBITRATED: F2 (Sage-QQ reconstruction) carried R's true 6th sig fig; F1 = Fraction(793346,108307) = 7.324974 (direct ratio of the already-6-sf-rounded published norm products) lost it via DOUBLE-ROUNDING -- F1 is a methodology-floor F-image, not the substrate value. The prior comment's "VALUE re-pin F2->F1 pending CF-S93-W7-1" was the OPPOSITE of the substrate verdict and is hereby corrected: the substrate vindicates F2's value. F1 and F2 agree only at the 5-sig-fig floor (7.3250); cross-mult residual 793346*15625-108307*114453 = -29821 != 0, |F1-F2|=1.762e-5, Delta_rel=2.406e-6, per Class 8.3 epistemic-discipline.md. Pillar III HP^1 generators ratio; UNBLOCKS VII.AY STAGE-3 (W5-2 substrate-pin-layer). (S86 value F2; re-pinned full-float64 S93 W5-1 verdict audit_sha256=491ac49c6d6436bce9e783efeac6e2ba06383a4fa5e03659bf62cfd300849617)
R_machine_substrate_67_88 = 7.3249917525961665  # S93 W5-1 substrate-first cocycle-ratio R_machine = Fraction(8814961,1203409) full float64; ALIAS of substrate_cocycle_ratio_67_88 carrying the branch-resolved provenance (F2-faithful). The substrate arbiter for the F1-vs-F2 historiography; consumed by W5-2 §VII.AY Element-5 Stage-2 re-tolerance (DEFERRED->resolved tag = branch_label F2-faithful). Sage-QQ exact 8814961/1203409 = 7.3249917525961665...; round_to_6sf=7.32499. (S93 W5-1; gate S93-W5-1-SUBSTRATE-COCYCLE-RATIO-67-88-R-MACHINE-RECOMPUTE)
tau_pivot = 0.190  # Jensen-deformation pivot scale = tau_fold (substrate-first canonical: substrate has ONE Jensen slice; "pivot" is CMB-observational concept mapping to substrate AT the fold). D_max = |log10(0.198/0.190)| = 0.0179 < 0.1 NO-ACTION band vs S87 W2-5 placeholder 0.198. Closes SR Class-(f) PIN-PLACEHOLDER-PENDING-SUBSTRATE-CANONICAL. (S88)
W_BG = 1462.2955351302771  # Narrow-path pre/post Bogoliubov squeeze-weight W_BG = |u|^2+|v|^2 = cosh(2r) = 1462.30. Provenance: from canonical n_Bog=0.998633 (tanh^2 r), cosh(2r)=(1+n_Bog)/(1-n_Bog); r_squeeze=3.99045. alpha_bridge^post = W_BG * alpha_bridge^pre (post-fold coeff LARGER). S38 GGE 59.8 pairs, P_exc=1.000. W8-6 PASS (covar_residual exact 0) (S93)
R_BG = 0.0006838562903161084  # Narrow-path pre/post bridge-coeff ratio R_BG = alpha_bridge^pre/alpha_bridge^post = 1/cosh(2r) = 1/W_BG = 6.84e-4 < 1 (post-fold coeff LARGER by W_BG~1462). Reciprocal SU(1,1) squeeze weight. Sign DERIVED (W_BG>1 alignment-independent). W8-6 PASS (S93)
s_CS = 0.018633374383484558  # Cauchy-Schwarz floor slack s_CS = (F0*F2-F1^2)/(F1^2-ish normalization) = 0.018633 at L_max=12 on canonical spectral moments. Feeds the ANSATZ surrogate alpha_win_lo = s_CS/N_e = 6.38e-3 (a Regime-II INDICATOR, NOT a registry-eligible floor per substrate-first §(iv-bis)). W8-3 INFO (S93)
tau_cross_van_hove = 0.191038  # van-Hove band-edge anticrossing argmin |T5_min-T3_max|, from-scratch L_max-invariant {5,8,10,12} sector-local, mesh-robust 1e-6, reproduces atlas-07 S45 0.19104 to 5sf; NON-FUNGIBLE with tau_fold=19/100 rational anchor per S114 W-1 workshop output (iii); offset 0.5464%; verdict audit 7b637db142d9bea7 (S114)
#  SECTION B: Framework Geometric Constants
# ==============================================================================

# Jensen deformation parameter at the fold (van Hove singularity)
# Session 12: phi_paasch found. Session 22a: Pomeranchuk. Session 35: mechanism chain
tau_fold = 0.19               # S42 constants_snapshot, fold_idx=7
phi_paasch = 1.531580         # PROVEN (S12, machine epsilon). Paasch spectral ratio at s=0.15
T_GGE_B2 = 0.668             # B2-sector GGE temperature (M_KK units, S43)

# Substrate bulk Weyl exponent — post-execution closed-form pin (S87 W1b-HK-5 PASS)
# PROVENANCE: S87-W1B-HK-5-PV-CONTINUUM-POLE-RECONCILIATION (PASS at |delta|=1.72e-5,
# below PASS threshold 1e-3 by 2 OOM). Closed form: substrate's bulk Weyl exponent
# (D-spectrum, Conv A "d_eff = 2*slope") is the geometric-series Connes-Mellin
# pole-shift form 10/(1 - tau_fold/(5*pi)); equivalently for D^2-spectrum (Conv B,
# "d_eff = slope") 5/(1 - tau_fold/(5*pi)). Substitution chain: bulk Weyl exponent
# IS the substrate-counting dimension on (A_K^{<=L}, H_K^{<=L}, D_K^{<=L}); the
# baseline 10 (Conv A) reflects the substrate's spectral-counting structure at
# tau=0 and the correction tau/(5*pi) reflects Jensen-deformation pole-shift at
# tau_fold=0.19. The continuum d=4 from M^4-only Seeley-DeWitt is the IN-frame
# projection; the bulk-IS observable is the geometric-series form.
BULK_WEYL_EXPONENT_CONV_A_FW = 10.0 / (1.0 - tau_fold / (5.0 * PI))  # = 10.12244
BULK_WEYL_EXPONENT_CONV_B_FW = 5.0 / (1.0 - tau_fold / (5.0 * PI))    # = 5.06122
# Empirical anchor at L_max=14 (Richardson L^{-3} extrapolation of W1b-3):
BULK_WEYL_EXPONENT_CONV_A_L14 = 10.122386446                            # (S87 W1b-3 measured)
BULK_WEYL_EXPONENT_CONV_B_L14 = 5.061193223                             # (S87 W1b-3 measured)
# Residual (closed-form vs L=14 measured): |delta_A| = 5.23e-5, |delta_B| = 2.62e-5
# under "10/(1 - tau/(5*pi))" form; |delta_A| = 3.44e-5, |delta_B| = 1.72e-5 under
# the 2nd-truncation form "10*(1 + tau/(5*pi) + (tau/(5*pi))^2)". Both well within
# the W1b-HK-5 PASS threshold 1e-3.

# SU(3) Haar volume — the CORRECT Weyl integration formula
# S44 CORRECTION: 8*sqrt(3)*pi^4 = 1349.74 (replaces wrong sqrt(3)*(4*pi^2)^3/12 = 8880.93)
Vol_SU3_Haar = 8.0 * np.sqrt(3) * PI**4   # = 1349.74 (S44 s44_constants_corrected)
Vol_SU3_WRONG = np.sqrt(3) * (4*PI**2)**3 / 12.0  # = 8880.93 (DO NOT USE — kept for audit)

# SU(N) Lie-theory constants (S88 W6a-52 — added for dim+rank/2 prefactor derivation).
# All three forms are CLASSICAL closed-form identities for compact simple Lie groups
# of type A_{N-1}; verified Sage-symbolic (s88_w6a_dim_plus_rank_over_2_prefactor.py).
# Used as substrate-IS algebraic input for Conv-B baseline bulk-Weyl exponent
# slope_A^B(D_can; SU(N)) = (dim + rank)/2 = |Delta+| + rank = (N-1)(N+2)/2.
# Provenance: S88 W6a-52 PASS landing; OEIS A000096 cross-reference.
DIM_SU2 = 3        # = 2^2 - 1 (S88 W6a-52)
DIM_SU3 = 8        # = 3^2 - 1 (S88 W6a-52; matches a_DK fiber dim)
DIM_SU4 = 15       # = 4^2 - 1 (S88 W6a-52)
RANK_SU2 = 1       # Cartan subalgebra dim = N-1 (S88 W6a-52)
RANK_SU3 = 2       # Cartan subalgebra dim = N-1 (S88 W6a-52)
RANK_SU4 = 3       # Cartan subalgebra dim = N-1 (S88 W6a-52)
DELTA_PLUS_SU2 = 1   # Number of positive roots = N(N-1)/2 (S88 W6a-52)
DELTA_PLUS_SU3 = 3   # Number of positive roots = N(N-1)/2 (S88 W6a-52)
DELTA_PLUS_SU4 = 6   # Number of positive roots = N(N-1)/2 (S88 W6a-52)
# Conv-B baseline prefactor at tau=0 — closed-form Peter-Weyl (S88 W6a-52 PASS):
#   slope_A^B_baseline_SUN = (dim_SUN + rank_SUN)/2 = (N-1)(N+2)/2
# OEIS A000096 a(N-1) = (N-1)(N+2)/2 starting from a(1)=2: 0,2,5,9,14,20,27,...
PREFACTOR_CONV_B_BASELINE_SU2 = 2  # (DIM_SU2 + RANK_SU2)/2 = 4/2 (S88 W6a-52)
PREFACTOR_CONV_B_BASELINE_SU3 = 5  # (DIM_SU3 + RANK_SU3)/2 = 10/2 (S88 W6a-52; W1b-3 anchor c0)
PREFACTOR_CONV_B_BASELINE_SU4 = 9  # (DIM_SU4 + RANK_SU4)/2 = 18/2 (S88 W6a-52)

# Diagonal metric element at round SU(3)
g0_diag = 3.0                 # From Killing metric normalization (S7)

# M_KK: TWO extraction routes, 0.83-decade tension (CONST-FREEZE-42 PASS)
M_KK_gravity = 7.428660036284456e16   # GeV, spectral zeta / Newton's constant route (S42)
M_KK_kerner = 5.041679838376001e17    # GeV, Kerner gauge-metric route (S42)
M_KK = M_KK_gravity                   # Default alias — gravity route (conservative)
OOM_diff_MKK = 0.831664779390838      # log10(M_KK_kerner / M_KK_gravity) (S42)

# ──────────────────────────────────────────────────────────────────────────────
# S92 LQG narrow-path bridge coefficient — REQUIRED value for Regime I closure
# (γ_emergent = γ_BH = 0.2375 in SU(2)-convention Immirzi)
# ──────────────────────────────────────────────────────────────────────────────
# Derivation (S92 LQG × phonon-first workshop §L2 substitution chain, lines 116-125):
#   γ_emergent = (α_bridge/(4√3π)) · (M_Pl_red/M_KK)²
#              = α_bridge · (1/(4√3π)) · (2.435e18/7.4287e16)²
#              = α_bridge · (1.074e3/21.77)
#              = α_bridge · 49.34
#   Set γ_emergent = γ_BH = 0.2375 (SU(2)-convention, Paper 03 §VII):
#   ⇒ α_bridge_required_FW = 0.2375 / 49.34 = 4.81e-3
# This is the dimensionless bridge coefficient the substrate must produce
# from the Step 4 Peter-Weyl projection onto a 2-surface for the §IX.7
# narrow path to close empirically (Regime I). Substrate-side prior places
# weight on α_bridge ∼ O(1) (Regime II, ~200× too large to match γ_BH);
# Q2 (Paper 03 §VII) confirms γ does NOT admit cutoff running so Regime II
# would be a STRUCTURAL FAILURE with no recovery mechanism.
ALPHA_BRIDGE_REQUIRED_FW = 4.81e-3    # Required α_bridge for narrow-path Regime I closure (S92 LQG workshop)
SCALE_BRIDGE_PREFACTOR_FW = 49.34     # Dimensional pre-factor (M_Pl_red/M_KK)²/(4√3π) (S92 LQG workshop L2 line 122)
# Convention disclosure: γ_BH = 0.2375 is the SU(2)-convention BH-entropy pin
# from Paper 03 §VII (researchers/Loop-Quantum-Gravity/index.md:779). Reduced-
# Planck-convention factor: ℓ_P² = 8π·ℓ_P_red² when comparing against
# unreduced-Planck loop-quantum-gravity literature values. See
# sessions/framework/correspondence/lqg-narrow-path-bridge-class.md for the
# full bridge-map class identification (HKR with -Cheeger-Simons scheme suffix).
GAMMA_BH_SU2_CONVENTION_LQG = 0.2375  # Immirzi γ from BH-entropy pin in SU(2)-convention (Paper 03 §VII; S92 LQG workshop)

# ==============================================================================
CC_OOM = 115.5  # CC_OOM = 115.5 OOM cosmological-constant dilution depth from Volovik tracking-vacuum partition; S66 W1-A PASS (rho_vac/rho_obs = 1.032). Substrate cascade-depth multiplier: cascade_depth = CC_OOM * log_2(10) = 383.6827 generations EXACT for pixelation-lock cascade-tail BBN-mass derivation (S88 W1c-66 J7 89-peak detection). (S66)
max_f_NL_FW = 1.505  # max|f_NL| ENVELOPE across transit cubic-bispectrum shapes/channels = |Bogoliubov-sudden channel| (NEGATIVE: f_NL^{Bog,sudden}=-1.505, anti-correlated 3-pt). Bogoliubov sudden-quench, squeezed-vacuum Gaussian by Wick (S65 W5-D PERMANENT: f_NL=O(eps) regardless of squeezing). Value-derivation S76 W1-C TRANSIT-FNL-76 (4 channels: EFT-equil +0.853, Bog-sudden -1.505, CLT-diag 0.129, Maldacena-local 0.015). Consistent w/ Planck f_NL^local=-0.9+-5.1 at 0.47 sigma. ENVELOPE not a replacement for per-shape pins f_NL_FW_S82_equilateral/S67_folded/S85_W9_3_analytic_template. FALSIFIER: detected |f_NL|>>1.5 (CMB-S4/21-cm) falsifies squeezed-vacuum cosmogenesis. (S95 W6-6) (S95)
Omega_GW_acoustic_peak = 9.15e-05  # Acoustic Omega_GW spectral PEAK HEIGHT at f_peak=8.4835e39 Hz, derived from the FINITE enhanced fold DOS (rho_B2_per_mode=14.0233, van-Hove divergence REFUTED S94) via squeezed-vacuum graviton conversion: Omega_peak = eps_grav * Omega_acoustic,fold,now = P_exc(=1.0) * Omega_r(=9.15e-5). log10 Omega_peak = -4.039 <= 0 (GW-energy sanity ceiling SATISFIED; a radiation-era SGWB obeys Omega_GW,0 <~ Omega_r,0, Maggiore/BBN bound). kappa-ROBUST across swept [1e-20,1e-10] (amplitude is dimensionless, kappa-independent; kappa sets the FREQUENCY axis only). REPLACES the unphysical 1e-10-at-pivot placeholder (Omega_GW_Lambda_A_LISA) which back-derived Omega_peak~10^117. Consumed by S97-OMEGAGW-ACOUSTIC-SPECTRAL-SHAPE (4.2) for the IR-tail propagation. publication_precision=4. (S97)
beta2_pivot_box_delta = 2.118266323934462e-06  # canonical v-quanta fold impulsive-window |beta_pivot|^2 at S-1-adjudicated 4-component tuple: (1) Z-PUMP per-edge weights Omega_z=[+1.2872356866503005,-1.288529316518922] M_KK (NOT sqrt(a)-pump); (2) branch-(c) barrier V_box=2.764080442498705 M_KK^2 (eta_H-corrected, 1.45265x quasi-dS anchor); (3) fold-conformal clock Delta_eta=1.13014059e-3 M_KK^-1 (tau in [0.18994874,0.19005127]); (4) IMPULSIVE-TRANSIT-WINDOW stage. scheme=BOX-DELTA-SUDDEN; mu_pivot^2(c)=202.043 M_KK^2 (74x margin, sin-branch); 3 code paths agree (closed/TM/ODE) to 1.4e-13; unitarity 6.7e-16; var_Nseg=1.0. COMPOSITION INPUT (one SU(1,1) factor of B-ladder); NON-comparable to S79 B2 by e-fold-span. audit_sha256=d853f35b19b8946bdb6062f8739ad197708e601441f821d066d9a4256b1422e1; validated_recipe_predecessor S100b-BOX-DELTA-BOGOLIUBOV PASS 297a597c3cfe6fa0 (S101)
beta2_pivot_box_delta_sqrtA_recipe = 3.045404292699012e-07  # KEYED DIAGNOSTIC companion to beta2_pivot_box_delta: the permanent W5-1 payload (Sparn-LITERAL recipe benchmark), verbatim. = closed-form |beta_pivot|^2 at branch-(b) barrier V_box=1.9027850412 M_KK^2 + LITERAL sqrt(a)-pump weights Omega=(1/2)a[a']=[+0.4871565379,-0.4882375848] M_KK. NOT the canonical (the S-1 adjudication DEMOTES the sqrt(a)-pump to recipe-benchmark; canonical uses Z-PUMP [z'/z] weights + branch-(c) barrier). Carried so the x6.96 silent-inheritance hazard between sqrt(a)-pump and Z-pump conventions is permanently closed on the books. Verbatim reproduction of S100b beta2_pivot_closed_form (rel dev 0.0). audit_sha256=d853f35b19b8946bdb6062f8739ad197708e601441f821d066d9a4256b1422e1 (S101)
kappa_exit = 47.6146  # Exit-horizon surface-gravity analog (M_KK units); a_4 BCS condensation-energy gradient barrier height. T_exit = kappa_exit/(2pi) = 7.5781 = T_compound = E_exc/8 (a_4 exit value). Substrate-first pre-promotion for INV4-W1-4-EXIT-GREYBODY-A-S-NORMALIZATION (no verdict-string placeholder pin) (S95)
lambda_B1 = 2.771  # GGE branch-1 Lagrange multiplier (SU(3)-branch structure); promoted for INV13-W1-1 collider spectroscopy (S39)
lambda_B2 = 1.459  # GGE branch-2 Lagrange multiplier (SU(3)-branch structure); promoted for INV13-W1-1 collider spectroscopy (S39)
lambda_B3 = 6.007  # GGE branch-3 Lagrange multiplier (SU(3)-branch structure); promoted for INV13-W1-1 collider spectroscopy (S39)
f_NL_folded = 0.1293  # GGE folded-triangle bispectrum template amplitude; promoted for INV13-W1-1 collider local-baseline (S83)
#  SECTION C: BCS / Many-Body Constants
# ==============================================================================

# BCS condensation energy — THREE values exist; each is a DIFFERENT quantity
# All in M_KK units (dimensionless ratios)
E_cond_ED_8mode = -0.13685055970476342  # S36 ED-CONV-36: 8-mode (4B2+1B1+3B3), 256-state, canonical
E_cond_ED_5mode = -0.11507660716341951  # S35 ED: 5-mode (4B2+1B1), 32-state (superseded by 8-mode)
E_cond_GL = -0.156                      # S37: Ginzburg-Landau functional (different quantity)

# The canonical value is the 8-mode ED result (S36, verified to machine epsilon)
E_cond = E_cond_ED_8mode               # = -0.137 (alias for downstream use)

# Excitation energy from BCS transit quench (S38)
E_exc_ratio = 443.0            # E_exc / |E_cond| (S38, Schwinger-instanton duality)
E_exc = E_exc_ratio * abs(E_cond)  # = 60.625 M_KK (derived — was 50.9 with old E_cond)
n_pairs = 59.8                 # Bogoliubov quasiparticle pairs from transit (S38)
epsilon_K7 = 0.00248           # K_7 violation amplitude (Leggett mode); S49 DIPOLAR-CATALOG-49; used in S61 transit baryogenesis channel eta_B = n_pairs * eps_CP * eps_K7 (s61_j_breaking_catalog_log) and S98-W3-2 substrate-fixed uniqueness
N_dof_BCS = 8                  # Fock space modes (4B2 + 1B1 + 3B3)
T_compound = E_exc / 8         # Microcanonical temperature (M_KK units)

# BCS gap and pairing — THREE quantities, often confused:
#
#   Delta_0_GL  = 0.770 M_KK : Ginzburg-Landau ORDER PARAMETER amplitude from
#                 s37_instanton_mc.  This is sqrt(|a_GL|/(2*b_GL)), the equilibrium
#                 condensate magnitude.  NOT an excitation gap.
#
#   Delta_0_OES = 0.464 M_KK : Odd-Even Staggering (pair-addition) gap from exact
#                 diagonalization in s37_pair_susceptibility (256-state Hilbert space,
#                 8-mode Fock space = 4 B2 + 1 B1 + 3 B3).  This IS the physical BCS
#                 gap — the energy cost to add/remove one Cooper pair.
#                 CANONICAL BCS GAP.
#
#   Delta_B3    = 0.176 M_KK : Gap in the B3 sector specifically (S38).  Smaller than
#                 the total gap because B3 modes lie further from the Fermi surface.
#
#   The value 0.52 M_KK that appears in some S69 scripts (s69_bcs_surface_gravity.py)
#   is NOT a separate gap measurement.  It was a confusion with the B2[3] single-particle
#   energy eps_fold[3] = 0.5229 M_KK.  That is a bare eigenvalue of D_K, not a pairing gap.
#   Superseded by Delta_0_OES = 0.4643 (S70, BCS-GAP-CANONICAL-70).
#
Delta_0_GL = 0.7704350982797368   # GL order parameter amplitude (M_KK, s37_instanton_mc)
Delta_0_OES = 0.4642547394830737  # OES/pair-addition gap (M_KK, s37_pair_susceptibility)
Delta_BCS = Delta_0_OES           # R-PROTECTED — CANONICAL BCS gap alias (S70, BCS-GAP-CANONICAL-70)
                                  # Dimensionless ratio Delta_BCS/M_KK = 0.4643; eigenvalue ratio,
                                  # bypasses Seeley-DeWitt expansion. STRUCTURAL, drift 0.00% (S74 W4-F #19)
Delta_B3 = 0.176                  # B3 sector gap (M_KK, S38; = 2*Delta_B3_s53 doubled-gap convention)
# --- Per-band GL gaps (s53/s52 acoustic-efold derivation; M_KK units) ---
# Canonical per-band Ginzburg-Landau gaps at the fold (tau=0.19), used by the
# multiplicity-weighted total-gap identity Delta_total = sqrt(Delta_B1^2 + 4*Delta_B2^2 + 3*Delta_B3_s53^2)
# (Fock multiplicities (1,4,3) for the (B1,B2,B3) bands of the 8-mode pair space).
# Sources: s53_acoustic_efold_output.txt, s52_casimir_josephson_output.txt (both report
# Delta_B1=0.371795, Delta_B2=0.732026, Delta_B3=0.084152 at tau_fold). NOTE the s53
# B1/B2 LABELS are interchanged between s53_gpe and s53_acoustic outputs; the squared-sum
# identity above is label-order-invariant, so the back-reaction ρ_relic assembly is robust.
Delta_B1 = 0.371795               # B1 band GL gap (M_KK, s53/s52 at tau_fold)  [added S95 W3-3]
Delta_B2 = 0.732026               # B2 band GL gap (M_KK, s53/s52 at tau_fold)  [added S95 W3-3]
Delta_B3_s53 = 0.084152           # B3 band GL gap (M_KK, s53/s52 at tau_fold; un-doubled)  [added S95 W3-3]
M_max_thouless = 1.674            # Maximum Thouless parameter (S35 RPA)
S_inst = 0.06860372346994315      # Instanton action (s37_instanton_mc, quantum critical point)

# Coherence lengths (s37_instanton_mc, high precision)
xi_BCS = 0.8083468753837275       # BCS coherence length (M_KK^{-1})
xi_GL = 0.9763208529368065        # GL coherence length (M_KK^{-1})
xi_BCS_over_BW = 13.952285853679658  # xi_BCS in BW units

# GL functional parameters (s37_instanton_mc)
a_GL = -0.5245475628963554        # GL a coefficient
b_GL = 0.4418580371481792         # GL b coefficient
barrier_0d = 0.004670337347200381 # 0D barrier height (M_KK)
barrier_1d = 0.15567791157334604  # 1D barrier height (M_KK)

# Pair vibration (s37_pair_susceptibility)
omega_PV = 0.791658919261384      # Pair vibration frequency (omega_plus)
omega_split = 1.3371826606372719  # Pair-add/remove splitting
ratio_Evac_Econd = 28.75624796597024  # E_vac/E_cond (fluctuation dominance)

# Langer decay (s38_attempt_freq)
Gamma_Langer_BCS = 0.24973624676840844  # Langer decay rate (BCS)
Kapitza_ratio = 0.030200115133742347    # Corrected Kapitza ratio (S38)

# ==============================================================================
L_envelope_d4_Lmax10 = 0.001  # L-envelope at d=4 L_max=10: 0.001 = 0.10%; envelope formula L^{-3} per W-5 R2-B DISSENT #1 Step 3. (S86)
L_J_Laplacian_dressing_kappa = 0.0364  # L_J Laplacian dressing kappa = N_cells/E_pathB^2 = 32/29.67^2 = 0.0364; sector-attribution comment per W-4 CANONICAL-4 provenance. (S86)
M_zeta_s3 = 3.7074  # Mellin moment at s=3 under zeta regulator; placeholder value pending verification of exact 5-tuple from W-9 extract — orchestrator to confirm. (S86)
N_e_postfold = 2.9202  # Substrate-side post-fold acoustic e-folds N_e = 2.9202 = ln(c_fabric/c_Gold) bulk-to-surface reduction. The only landed substrate bulk-to-surface reduction at landing magnitude. Substrate-side prior anchor: framework reductions produce O(1) outputs (favors Regime II, P>=0.6). Plan label N_e_postfold=2.92 (S93)
N_e_flip_threshold = 3.8710334562  # Flip threshold N_e* = 3.8710334562 where the alpha_win_lo=s_CS/N_e surrogate would cross into Regime I. c-ratio to flip = exp(2*N_e*) = 2303x vs substrate's c_fabric/c_Gold = 229x; since 229 < 2303, ALL ledger N_e (largest 2.9202 < 3.871) keep the Regime-II LEAN over-determined and structurally protected. LEAN != registry-eligible floor (surrogate, tag (b)) (S93)
a_4_FW_zeta = 1350.7216  # zeta-regulated fourth Seeley-DeWitt coefficient of D_K^2 at tau_fold; Yang-Mills + Higgs quartic moment; completes the (a_0,a_2,a_4) zeta triple alongside a_0_FW_zeta/a_2_FW_zeta; canonicalized during phonic-exflation-equation capstone build (clears gen-physicist R3 / spectral-geometer flag) (S75)
M_KK_inv_seconds = 8.860439881925477e-42  # s; substrate clock tick M_KK^-1 in SI seconds = hbar_SI/(M_KK*GeV_to_J), closes S95-W3-1 seconds_norm_open; two SI routes agree rel 2.14e-5 (PASS); 6sf 8.86044e-42 (S96)
GeV_to_J = 1.602176634e-10  # J per GeV (exact SI); = eV_SI*eV_per_GeV; used in M_KK energy->Joule conversion (S96-W1-MKK-SECONDS) and S52 12D-reduction (S96)
c_s_a2curv_GGE_fold = 0.5685294372062244  # Substrate-scale (M_KK) a2-curvature-channel hydrodynamic-IR sound speed of the post-fold GGE two-fluid; c_s^2=0.323226=K_grad/K_inertia (group-velocity^2 = IR dispersion slope d lam^2/dC_2 on s84 L12 cache, a2^zeta-density x saturated-Parker-GGE weighted). GS-1 scale-separation discriminator: c_s in window [0.5163972,0.6501056], |2*Dscale-fork_OOM|=0.0165<=0.10 => deg=+2 transport SOLE carrier => A_s->H~/+0.196 grid (3.2994e-9), Q23 zero-parameter. Two-fluid bracketed c_BLV=0.485 <= c_s <= c_Gold=0.915; regime-MARGINAL. DISTINCT CHANNEL from c_s2_FW=0: that is the 4D-emergent/dark-sector Goldstone sound speed^2=0 EXACT (Layer-1/topology, Kasparov m_Goldstone^4D=0); THIS is the Layer-2 substrate-scale emergent a2-hydrodynamic dispersion (flat bare 4D Goldstone is dispersionless c_s^2=0, the post-fold substrate GGE two-fluid develops nonzero hydrodynamic c_s). audit 172c85be (CF-S118-AS-CS-SUBSTRATE-FIRST) (S118)
#  SECTION D: Spectral Action Constants
# ==============================================================================

# Seeley-DeWitt coefficients at the fold (tau = 0.19)
# From s42_constants_snapshot.npz (S42, verified against s20a recomputation)
a0_fold = 6440.0               # a_0 (volume term)
a2_fold = 2776.1653888633655   # a_2 (scalar curvature term)
a4_fold = 1350.7216415169728   # a_4 (Gauss-Bonnet / gauge kinetic term)

# R-family protected ratio-of-moments (S73B landau-baptista workshop
# action #1, verified S74 R-PROTECTED-FOLD-ADDITION-74 / W1-M)
# -------------------------------------------------------------
# R_protected_fold is the dimensionless spectral-action ratio
#   R_1 = a_0 * a_4 / a_2^2
# whose Weyl exponents cancel to L^0, making it L_max-invariant
# (drift 0.34% across L_max in [3,9]).  Baptista B2 theorem:
# Vol(SU(3)) cancels identically in ratios of equal mass dimension.
# This is the SOLE structurally protected Chamseddine-Connes observable.
R_protected_fold = a0_fold * a4_fold / a2_fold**2  # R-PROTECTED (S73B/S74, drift 0.34%)

# Lizzi signature observable: (m_H/v_EW)^2 * (Lambda/M_Pl^2)
# Algebraically collapses to R_1 = a_0*a_4/a_2^2 identically.
# Two unprotected pieces (Higgs-to-vacuum ratio, CC-to-gravity ratio)
# combine into a single protected ratio-of-ratios.  S74 W4-F row #11.
Lizzi_signature = R_protected_fold  # R-PROTECTED (= R_1, S74 W4-F, drift 0.34%)

# Spectral action and derived quantities
S_fold = 250360.67696101       # S_full at fold (S42 s42_gradient_stiffness)
m_tau = 2.062                  # Modulus mass at fold (M_KK units, S42 W2-1)
omega_att = 1.430              # Attractor frequency, fully geometric (S38)
omega_tau = 8.27               # Transit frequency d(tau)/dt (M_KK units, S38 attractor)

# Collective inertia and dynamics
M_ATDHFB = 1.695               # ATDHFB collective mass (S40, s42_gradient_stiffness)
Z_fold = 74730.76411846        # Gradient stiffness at fold (S42)
G_DeWitt = 5.0                 # DeWitt moduli kinetic coefficient (S42 s42_gradient_stiffness)
dS_fold = 58672.80241318       # dS_full/dtau at fold (S42 s42_gradient_stiffness)
d2S_fold = 317862.84898132     # d^2 S_full/dtau^2 at fold (S42 s42_gradient_stiffness)
c_fabric = 209.97368021        # substrate sound speed (velocity scale, NOT a momentum cutoff) — S42 s42_gradient_stiffness; docstring per S86 W0b-1
c_BLV = 0.485                  # Brillouin-Landau-Vortex fabric sound speed (S64 s64_sound_speed; 3He-B four-speed hierarchy inheritance, scalar c_s for post-fold GGE; used 5+ scripts)
alpha_s_cmb_central = -0.06896799  # SUPERSEDED (S92 AH-TR-1; see PROVENANCE) — CMB-pivot running is alpha_s_pivot_goldstone~=0, NOT -0.069. S50 identity alpha_s_CMB = n_s^2 - 1 with planck_ns=0.9649 (S85 W13-2; provenance: s50_running_mass.py constant-mass identity + Planck 2018 TT,TE,EE+lowE+lensing)
f_LISA_pivot = 3.0e-3          # LISA flagship pivot frequency [Hz] (S85 W13-2 pre-registration; 3 mHz canonical LISA sensitivity band centre)

# Transit parameters (s38_kz_defects)
H_fold = 586.5267713108464     # Hubble parameter at fold (M_KK units, S38)
v_terminal = 26.544972625732246  # Terminal velocity of modulus (S38)
dt_transit = 0.0011301575037571713  # Transit duration (M_KK^{-1}, S38)
P_exc_kz = 1.0                 # Kibble-Zurek excitation probability (S38, P=1 exactly)
n_Bog = 0.9986332220990328     # Bogoliubov fraction per mode (S38)

# -- H_tilde anchors (S85 W7-1 promotion; canonical constants per plan §W7-1 step 5) --
# Provenance: S84-BASELINE-HTILDE-SENSITIVITY: PASS -- value=0.8901
#   sha256=a47383031046171c062e822a735c7e5cd42261aad45996d9ebae9e65f6b77c19
# S82-W1-2 Branch-A TD anchor: H_canonical_TD = 5.9076e-3 at A_s_canonical=3.30e-9
#   (Python-verified from s82_w1_2_unified_as_79_full.py line 137)
# S82-W1-2 Branch-B LI anchor: H_LI = 2.46411e-5 (divergence-chase endpoint)
#   (Python-verified from s82_w1_2_unified_as_79_full.py line 143)
H_tilde_lo = 4.599e-3          # S84 W1a-1 PASS window lower bound (CC3: Planck A_s/1.05)
H_tilde_hi = 4.829e-3          # S84 W1a-1 PASS window upper bound (CC3: Planck A_s*1.05)
H_tilde_center = 4.714e-3      # Arithmetic centre of S84 W1a-1 PASS window (= 0.5*(lo+hi))
H_tilde_canonical_TD = 5.9076e-3  # S82 W1-2 Branch-A microscopic TD anchor (M_KK units)
H_tilde_canonical_LI = 2.46411e-5  # S82 W1-2 Branch-B microscopic LI anchor (M_KK units)

# -- S85 W7-3 promotion: impedance + Planck 2020 DR2 observational constants --
# Provenance:
#   Gamma_effacement (canonical pin, S37 framework): the acoustic-white-hole
#     impedance-transmission coefficient. Γ = 0.99970; effacement residual
#     (1−Γ) = 3.0e-4 is the substrate's IR dark-energy-like leakage.
#   Omega_DM_obs / Omega_DE_obs: Planck 2020 DR2 (Aghanim+2020, A&A 641 A6
#     Table 2). Canonical 2018 values — Omega_DM=0.266, Omega_Lambda=0.685 —
#     remain in the main section; the 2020 DR2 refit is 0.264 / 0.685.
Gamma_effacement = 0.99970     # S37 canonical impedance-transmission; (1−Γ)=3e-4
Omega_DM_obs = 0.264           # Planck 2020 DR2 (Aghanim+2020 A&A 641 A6 Table 2)
Omega_DE_obs = 0.685           # Planck 2020 DR2 (Aghanim+2020 A&A 641 A6 Table 2)

# Gauge couplings at M_KK (Kerner route)
g_SU2_fold = 2.0515842276370675   # SU(2) coupling^2 at fold (S42)
g_U1_fold = 4.386853768302675     # U(1)_Y coupling^2 at fold (S42)
alpha2_MKK_inv = 47.85603973035754  # 1/alpha_2 at M_KK (S42)
sin2_thetaW_fold = 0.58385339192799  # sin^2(theta_W) at fold (S42, running value)


# -- Mellin moments of f* (added S78 W2-D s78_f_conv_anomaly.py) --
# f*(x) = 0.912*sqrt(x) + 0.088*exp(-x); CC/NCG convention:
#   f_0 = f*(0);   f_2 = int_0^{50} f*(x) dx;   f_4 = int_0^{50} x*f*(x) dx
# Sharp-cutoff (Andrianov-Lizzi arXiv:1001.2036) FORCES f_0=1/2, f_2=1, f_4=1.
mellin_f_star_f0 = 0.0883200000   # Mellin moment f_0 of f*(x)=0.912sqrt(x)+0.088exp(-x) (S78 W2-D)
mellin_f_star_f2 = 214.97335676   # Mellin moment f_2 of f* (X_MAX=50 regulator) (S78 W2-D)
mellin_f_star_f4 = 6446.63942272   # Mellin moment f_4 of f* (X_MAX=50 regulator) (S78 W2-D)

# ==============================================================================
sigma_alpha_SKA1 = 5.118  # SKA-1 Phase-1 Fisher sigma(alpha_fNL); G45 canonical; used by S84 W4-43 SNR (S83)
sigma_alpha_SKA2 = 0.80  # SKA-2 full Fisher sigma(alpha_fNL); G45 PASS threshold for framework alpha detection (S83)
beta_s = -0.1331  # Second spectral moment of D_K at tau_fold slice, Jensen flow (running-of-running from W8-86 3rd Taylor coefficient) (S84)
sigma_beta_s_CMB_S4 = 2.2e-3  # CMB-S4 projected 1-sigma forecast on beta_s = running-of-running; used as LCDM-null pull denominator for S85-BETA-S-CMB-S4-PREREG (S85)
b_DK = 0.006241291005766653  # Dirac-operator-determined dimensionless constant for Weyl-rescaling weak-form parametric bound. b_DK = (1/8 pi^2) * Tr_F[(Y†Y)^2] / Tr_F[Y†Y] = (1/8 pi^2) * y_t^2, with y_t = m_t_pole/v_ew = 0.7020. Used in W6-3 C-gamma-WEAK gate (L_max=10, FAIL: tree-level dominates anomaly at this regulator class). (S86)
HP0_content_dim = 3  # HP^0(A_F) content dim for §VII.P-v2 HP^0-content-distinct corridor restriction (S82 W2-3 baseline + S85 W2-7 closeout) (S86)
dE_He_A_lambda_6 = 1.7267  # Lab falsifier δE_a — 3He-A delta_omega_K/omega_K ratio at sweet-spot lambda_6 direction; M_KK-normalized. SW1 (Row #13) and XA1 (Row #16) per S86 W14-6 falsifier-master-inventory. (S86)
dE_FeSe_lambda_7 = 1.8226  # Lab falsifier δE_a — FeSe K_anis/K_0 Knight-shift anisotropy at sweet-spot lambda_7 direction; M_KK-normalized. SW2 (Row #14) and XB2 (Row #20) per S86 W14-6 falsifier-master-inventory. (S86)
dE_173Yb_lambda_8 = 2.8500  # Lab falsifier δE_a — 173Yb 3-body Gamma(unique)/Gamma(inherited) optical-lattice loss-asymmetry ratio at sweet-spot lambda_8 direction; M_KK-normalized. SW3 (Row #15) per S86 W14-6 falsifier-master-inventory. (S86)
dE_FeSe_lambda_6 = 0.7674  # Lab falsifier δE_a — FeSe K_anis/K_0 ratio under cross-platform lambda_6 projection; M_KK-normalized. XA2 (Row #17) per S86 W14-6 falsifier-master-inventory. (S86)
dE_173Yb_lambda_6 = 5.4938  # Lab falsifier δE_a — 173Yb 3-body Gamma-ratio under cross-platform lambda_6 projection; M_KK-normalized. XA3 (Row #18) per S86 W14-6 falsifier-master-inventory. (S86)
dE_He_A_lambda_7 = 0.5756  # Lab falsifier δE_a — 3He-A delta_omega_K/omega_K under cross-platform lambda_7 projection; M_KK-normalized. XB1 (Row #19) per S86 W14-6 falsifier-master-inventory. (S86)
dE_173Yb_lambda_7 = 13.1852  # Lab falsifier δE_a — 173Yb 3-body Gamma-ratio under cross-platform lambda_7 projection; M_KK-normalized. XB3 (Row #21) per S86 W14-6 falsifier-master-inventory. (S86)
r_PathH = 0.0074705  # Path-H tensor-to-scalar ratio at CMB pivot under H_tilde-divergence-chase resolution at BASELINE; transverse-tensor fiber-oscillation pathway (Hawking-side, B2-mode at fold). Forward-derived: r_PathH = r_PathC * (H_BASELINE/H_TD)^2 = 0.0074705. rel_dev vs workshop-quoted 0.00745 = 0.275%; n_T(Path-H) = -r/8 = -0.000931. Replaces oral citation 'S85 W1b-6' which was a label-confusion error (W1b-6 was MacInnis sigma-alpha-s PRE-REG-INCOMPLETE). (S86)
r_PathH_published = 0.00745  # Workshop-quoted 4-sig-fig form of r_PathH = 0.0074705. Used in plan-w12 §7, W14 §Row #2 r, s86_bk_array_2026_classifier.py. Verifiers comparing against this published form must use rel_tol >= 1e-3 per Publication-Precision rule (publication_sig_figs = 4). (S86)
alpha_s_canon_Fairbairn = -0.00323  # External-paper canonical for cross-check; central -0.00323 sigma=0.00389. Framework-canonical alpha_s remains substrate-derived per W-2 sign-lock theorem. (S86)
alpha_s_canon_FairbairnSPT = +0.00804  # External-paper canonical for cross-check; central +0.00804 sigma=0.00569. Sign-positive subset of Fairbairn rows. (S86)
alpha_s_canon_FairbairnACTP = +0.01195  # External-paper canonical for cross-check; central +0.01195 sigma=0.00626. (S86)
ns_canon_Fairbairn = 0.97101  # PARALLEL PIN to planck_ns=0.9649 (does NOT supersede; per UD-3 decision). External-paper canonical for cross-check; central 0.97101 sigma=0.00390. Framework-canonical n_s remains planck_ns. (S86)
beta_s_canon_Fairbairn = -0.00755  # External-paper canonical for cross-check beta_s = d alpha_s / d ln k; central -0.00755 sigma=0.00347. (S86)
alpha_s_canon_RogersPoulin = -0.01080  # Per UD-4 accept Fairbairn-cited form. External-paper canonical for cross-check; central -0.01080 sigma=0.00220. Direct Rogers-Poulin paper cite TBD if needed for downstream gate. (S86)
substrate_residue_floor_alpha_s = 8.65e-5  # Substrate residue floor for alpha_s (absolute = 8.65e-5; relative = 1.25e-3 to alpha_s_FW). Derived via R3-FINAL Verdict row 4 from gamma_pivot=4.4e-5 and u_pivot. (S86)
u_pivot = 19649/351  # u_pivot = 19649/351 = 55.9800569800570 exact rational; derived from planck_ns = 9649/10000 per V1 Step 3. (S86)
gamma_pivot = 4.4e-5  # Substrate-physical residue prefactor at pivot scale; ~4.4e-5; estimate-pinned per W-2 R3-B EMERGENCE (i). (S86)
w_optical_over_acoustic_pivot = 1e-4  # Optical-vs-acoustic ratio at pivot ~ (k_pivot/omega_L1)^2 ~ 1e-4. Suppression of w_optical contribution to alpha_s. (S86)
Omega_GW_Companion_null = 8.299e-58  # Companion-null Omega_GW Sage-exact value. Promoted per UD-5 (3+ scripts cite this). (S86)
sigma_HypB = 16577/7460  # sigma_HypB = 16577/7460 = 2.222118 Sage-exact rational; per W-3 R2-B Convergence #2. (S86)
sigma_naive = 17/4  # sigma_naive = 17/4 = 4.250000 (mnemonic-naive form); contrasts with sigma_HypB Sage-exact form. (S86)
sigma_band_low = 49731/29840  # sigma_band_low = 49731/29840 = 1.666588 Sage-exact rational lower edge of sigma band per W-3 R3-A. (S86)
sigma_band_high = 16577/5968  # sigma_band_high = 16577/5968 = 2.777647 Sage-exact rational upper edge of sigma band per W-3 R3-A. (S86)
reduction_ratio = 16577/31705  # reduction_ratio = 16577/31705 = 0.522851 Sage-exact rational. Per T1-2 mnemonic-vs-exact discipline: this is structurally exact, replacing mnemonic 1/c_sub=0.4468 (14.54% understatement). (S86)
OOM_split_AC_regulator_class = 47.081  # Order-of-magnitude split between (A) and (C) regulator classes for Path-H/Path-C Omega_GW: 47.081 OOM. Promoted per UD-5. (S86)
xi_sq_0_crit_SR_LO_breakdown_N1 = 2.2256  # Critical xi^2_0 for SR-LO breakdown at N=1 e-fold; brentq solution per W-9 transit T1. (S86)
xi_sq_0_lin_crit_SR_LO_N55 = 0.395  # Linear-regime critical xi^2_0 for SR-LO at N=55 e-folds; per W-9 transit Q-L2.1+T2. (S86)
xi_sq_0_SR_LO_valid_crit_N55 = 1.7  # Critical xi^2_0 above which SR-LO regime invalid for full N=55 e-fold integration; ~1.7. (S86)
rho_inf_zubarev_canonical = -0.810369  # rho_inf for Zubarev convergence sequence under simple-pole fit on L=8..12 cache; canonical extrapolation per W-10 CM-1995 audit Bulletin #4. (S86)
rho_inf_zubarev_deep_ir = -0.918  # rho_inf for Zubarev convergence in deep-IR limit Lambda_Z -> 0+; band-estimate -0.918 with gap=0.082 from canonical extrapolation. lam_min = 1 - rho_inf_deep_ir derivable in-script per UD-7. (S86)
f_NL_total_SKA1 = 0.9522  # f_NL_total at SKA1 = 0.9522 (6.348 sigma at sigma_SKA1=0.15) coherent sum across 3 substrate pathways. Per UD-12: prediction FROZEN per FROZEN-PREDICTION-DISCIPLINE; architecture-revision-exempt for path-decomposition relabel only. (S86)
lambda_min_max_ratio_FW = 0.15127342302947558  # Bit-exact extraction from L_max=12 spectrum cache at tau_fold=0.190; strict |lambda|_min/|lambda|_max ratio (zero-modes excluded if present); substrate-spectral invariant of D_K(tau_fold). (S87)
chi_A_FW = 1.5  # A-phase chiral correction chi_A = 3/2 = (2/3)^{-1} — substrate-first FS-average inverse. Dual-anchor: Volovik 2003 §3.4 axisymmetric A-phase heritage + S88 W3b-28 substrate-first Gauss-Legendre quadrature verification at N=512 (analytic_residual = 4.441e-15) + Sage QQ exact symbolic anchor (∫_0^π sin³θ dθ = 4/3, bool == True). PIN-PROMOTES-TO-CANONICAL-ON-PASS Class-(e) per epistemic-discipline.md §"Source Reconciliation" 5-class taxonomy. Used in (Δ_B/Δ_A)^p cancellation theorem (S86 W-5 DONE-5) and every Class-B inheritance-falsifier-protocol gate. (S88)
f_NL_FW_S82_equilateral = 0.0547  # S88 W8-96 CF-27 pin-promotion. S82 equilateral-template pathway (GGE-FNL channel projection); 3-pathway f_NL_folded projection per W13-2 P10 registry (baseline-findings-s66.md:556); source_sha=0184e88d50a0a16edfe17d385e54ae4f680963edf099bd55ff02ab8e1111fb56 (S88)
f_NL_FW_S67_folded = 0.129  # S88 W8-96 CF-27 pin-promotion. S67 folded-pathway (GGE-BISPECTRUM-67 in-in formalism); 3-pathway f_NL_folded projection per W13-2 P10 registry (baseline-findings-s66.md:556); source_sha=80699ca912fd945fef92d2b4e9d883955dae983818fd55917e93055a2ec495f4 (S88)
f_NL_FW_S85_W9_3_analytic_template = 0.7685  # S88 W8-96 CF-27 pin-promotion. S85 W9-3 analytic-template-folded pathway (folded-triangle 21cm shape); 3-pathway f_NL_folded projection per W13-2 P10 registry (baseline-findings-s66.md:556); source_sha=421575322637ab64f0911293b8a6b89a925a70ce44631767da0bba021262e817 (S88)
V2_weight_FW_C = 1  # Schur-projected real-dim functional on A_F = C+H+M_3(C), C-block component (J-real projection of complex line to 1 real DoF). Canonical Connes-Marcolli 2008 Thm 11.1 + Connes-Chamseddine 1996 §2.2-2.3. (S88)
V2_weight_FW_H = 4  # Schur-projected real-dim functional on A_F, H-block component (real_dim of quaternions). Canonical Connes-Marcolli 2008 Thm 11.1. (S88)
V2_weight_FW_M3 = 18  # Schur-projected real-dim functional on A_F, M_3(C)-block component (real_dim 2*9 of 3x3 complex matrices). Peter-Weyl multiplicity-collapse from spectrum 10424 to 18 via Hom_SU(3) image; collapse factor 579.1111x. Canonical Connes-Marcolli 2008 Thm 11.1. (S88)
V2_weight_FW_sum = 23  # Schur-projected real-dim functional on A_F, sum across all 3 blocks = 1+4+18 = 23 = real_dim(A_F). Canonical Connes-Marcolli 2008 Thm 11.1; A_F = C+H+M_3(C) Connes-Chamseddine canonical embedding. (S88)
a_0_FW_zeta = 6440.0  # zeta-regulated zeroth Seeley-DeWitt coefficient of D_K^2 at tau_fold; substrate dimensionless mode count (a_0 = zeta_{D_K}(0) = Tr(1)) per CCM 2007 + S64 / S77 R-protection; W11-124 canonical-write-order Step 2 promotion (regulator-pin-discipline.md MANDATORY at S86 W0c-7) (S88)
a_2_FW_zeta = 2776.165389  # zeta-regulated second Seeley-DeWitt coefficient of D_K^2 at tau_fold; spectral-zeta sum a_2(spectral, S42) = 2776.165389; S46 a_2 split = a_2^zeta / a_2^SD = 2776.165389 / 0.728234972609 = 3812.18; W11-124 canonical-write-order Step 2 promotion (S88)
xi_KZ_FW = 0.018760052113614717  # Substrate-natural xi_KZ derived from atlas T1 dt/T_L=1.25e-5 + Bogoliubov-unitary BdG-A_2 (nu=1/2, z=1, m=1/3) + S53 xi_BCS-analog 0.808346 M_KK^-1. M_KK^-1 units. Closes S88 W-2 V.iv Class-(f) PIN-PLACEHOLDER pathology. (S89) (S89)
kappa_2_substrate_FW = 0.021018084987437196  # CM-1995 §III.4 second-order Jensen perturbation on HK-5 closed form 5/(1-tau/(5*pi)); kappa_2 = 1/(5*pi^2 * A^3) with A = 1 - tau_fold/(5*pi) at tau_fold = 0.19. Substrate-IS analytic Taylor coefficient; regulator-class INVARIANT by construction. Cross-link to A.9 §W3-2 c_substrate_taylor (same closed-form formula). (S89) (S89)
tau_max_HK5_regime_FW = 12.4750026513  # HK-5 closed-form '5/(1-tau/(5pi))' regime-of-validity upper bound; min over Source-1 (analytic pole 5pi=15.708), Source-2 (substrate-IS structural transition; substrate algebra A_K tau-invariant => +inf, non-binding), Source-3 (Taylor truncation at L_max=12 reaches 5%% residual at x=0.794, tau~12.475; binding source). Per S88 W-21 V.5 derivation criterion (line 192). Margins: tau_fold/tau_max=65.66x, A.28 (tau=0.38)/tau_max=32.83x both >>10x PASS criterion. (S89)
c_W12_deficit_FW_PRIMARY_ConvB = 7.244e-4  # Substrate-first canonical Conv-B HK-5 deficit at W-12 §IV.1 R1∧R2 joint-closure pathway; substrate-first canonical paired with Conv-B HK-5 form per S88-D-EFF-ANCHOR-CONVENTION-AUDIT track_assigned=B; cache anchor residual_B = 2.615119e-05; tau_fold² = 0.0361. OOM distinction 1.463 from kappa_2_substrate_FW = 0.021018 (Class-(d) PIN-DERIVATIVE remediation Conv-A→Conv-B). (S90 CF-46 audit_sha256=de3c690f465931e1d34d1f3266c13445e0b4b6e477f4cc914abe9022596b809e)
tau_max_HK5_regime_FW_asymptotic_limit_FW = 5 * PI  # = 15.707963267948966; L_max → ∞ asymptotic limit by direct closed-form identity lim 0.05^{1/(L+1)} = 0.05^0 = 1; analytic pole of HK-5(τ) = 5/(1−τ/(5π)) at τ = 5π; structural-saturation theorem analog of S87 W11-3 Friedrich-Bär saturation at substrate-distance-5 pole. (S90 CF-47 audit_sha256=5c7cbe480ded228cdd7d0879a23d4c07d335c21f8921ddbbcdb8d3e85ed0410b)
lambda_unit_canonical = "dimensionless_M_KK_natural"  # String pin per S90 W1-10 INFO; cache lambda range [8.1974e-01, 5.4189e+00] in dimensionless M_KK-natural units; GeV conversion uses M_KK_GeV = M_KK = 7.428660e+16; anchor-5 literal 1.8121e-34 GeV^-2 requires this unit framing for the W5-7 anchor-5 unit-consistency audit to evaluate cleanly. (S90 W1-10 INFO; promoted in-session per `feedback_fix-in-session-never-defer.md`)
T_H_FW = 1.057e-3  # GeV. CF-39 cascade-tail anchor temperature T_H = 1.057 MeV (Hawking temperature of the M_0=10^13 kg cascade-tail PBH; T_H=hbar c^3/(8 pi G M_0 k_B)=1.227e10 K per S88 W1c + S88 W6 §V.1). Substrate-pinned per S87 J8 + W1a CF-CURV-7. NON-PHONONIC Pillar II cosmological anchor. (S92)
A_horizon_FW = 1.0/(4.0*3.141592653589793*(1.057e-3)**2)  # GeV^-2 = 71226.26 GeV^-2. Inheritance-restricted horizon area at T_H=1.057 MeV; substrate-first emergent-area-theorem relation A_horizon=4 pi R_S^2=1/(4 pi T_H^2) (R_S=1/(4 pi T_H) from Hawking T_H=1/(8 pi G M) in natural units). Cross-checked to 0.05% vs the M_0=10^13 kg SI Schwarzschild area 2.772e-27 m^2 = 71191 GeV^-2 (S88 W6 §V.1 + S82 horizon-area chain). NON-PHONONIC Pillar II. (S92)
L_H_canonical_FW = 1.563174393167446e-07  # GeV^2. CF-39 horizon-area Stefan-Boltzmann energy-flux observable L_H_canonical=(pi^2/60)*g_*(T_H)*A_horizon*T_H^4 closed-form on 3 canonical pins (g_star_BS_T_H_FW=10.688551 [S92-W8-5], T_H_FW=1.057e-3 GeV, A_horizon_FW=71226.26 GeV^-2). =3.805e+07 W (OOM cross-check vs S88 W6 §V.1 multi-species ~1.0e7 W). Option-A supersedes-chain: canonical line supersedes S91-CF39 PRE-REG-INC target 2afd17ef99c81123548642938a4053fb82ea075ea626b5fe6afcbcb73215ed5d. Canonical (latest non-superseded) gate audit_sha256=b260549318848314b212d8f6ec67c4e02330fe4e78e111f13f255d60ecad4c9e. NON-PHONONIC Pillar II. (S92)
Var_a_canonical_L_inf_FW = 6.4631783294e-06  # Substrate-IS canonical Level-3 anchor at permanent-results-registry §VII.U.2 Corner II Var_a; Weyl-dim multiplicity at the atlas-row L->inf layer (w5b47 convention) selected by S92 W8-2 workshop via 3-of-3 convergent-derivation tests (Hochschild-Kunneth Morita-invariance + parse-tree clause (e) decision procedure + Connes-Karoubi K-theory pairing). The 7.2824900000e-06 raw is the L=10 cache-moment image (DIAGNOSTIC; L^-4 convergence from above, ratio 1.126766). vdd m_a=1 convention (4.77e-05) NAIVE-PARSE eliminated. Workshop audit_sha256=2c6e57c6a8b1226a6b4588044704650b1f06d4c672e3800fb96bc2613c0005e9. NON-PHONONIC Pillar V GGE-state-variance image on BdG sub-algebra; algebra-INVARIANT spectrum-only functional at Corner II x Mellin pole s=4. (S92) (S92)
xi_k_zeta_window_canonical_FW = 2.0  # Substrate-natural zeta-window normalization xi_k=Gamma(k+1)/Gamma(1+k/2)^2 at LOCKED-NORM L_k=1; pinned at k=2 (a_2 gravitational slot, xi_2=2 EXACT). L_max-INDEPENDENT closed form. dimensionless. (S92)
vii_bb_element_5_empirical_anchor_FW = 11.763253530952039  # Element 5 empirical anchor = Norm_HH1 cocycle norm (dim-9; S88 W2-3) on M_3(C) Peter-Weyl block (triality (p-q) mod 3 != 0) at single-tau-slice tau_fold=0.19, substrate-distance-3 DEGENERATE pole s=5 (Mellin exp -10), L_max=12 master cache. DEGENERATE pole: alpha(s=5,d=4)=0 by substrate structure (standard polynomial 2d/s-1=0.6 INVALIDATED per S91 W9-13); substrate-IS regime=composite (argmax R^2=0.9920 on L in {6,8,10,12}); FB saturation predicate min eta_FB=0.4465>=0.40 PASS (licensed; W11-3). audit_sha256=de6922e77057af42f208d156d953b621ac67ce893dbf73b2f2f373c75cf25d0b. First-extraction; §VII.BB STAGE-1-CANDIDATE (S91 W9-13) -> +empirical-Level-3-anchor; REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION K=2->K=3 candidate. M_KK^2 units. (S92)
alpha_s_pivot_goldstone = 0.0  # CMB-pivot scalar running alpha_s = d2(ln P_zeta)/d(ln k_4D)2, Goldstone-protected ~0 (|alpha_s|<=5e-3). Substrate-first: P_nabla_phi(K)=K2*P_phi(K)=K2*K^-2=K^0 scale-invariant (S47 PERMANENT/Exact, Goldstone theorem on fabric), forward from D_K, NO FRW/inflaton container; MS form is lab-IN cross-check only. Confirmed 8.4e-15 machine-zero (S74 TRANSFER-FUNCTION-74), frozen-plateau 1e-113 (Sasaki-Stewart). SCALE-SEPARATED from alpha_s_substrate_distance_1=-0.08587279 by 54.04 decades of k; the two are DIFFERENT substrate-IS observables (scalar-transport pivot leaf vs non-scalar-transport substrate leaf), discriminated by deg(T_BZ->pivot)=+2 NON-SCALAR (RESOLVED S93 W7-1, transit-CONFIRMED; the substrate/BZ leaf is the realized matched-channel branch). Planck consistency +0.67sigma. SECTION E. (S92; degree resolved S93 W7-1)
alpha_s_substrate_distance_1 = -0.08587279  # Substrate-distance-1 running alpha_s^substrate = (a_4/a_2)2 - 1 = d2 S_transfer/dk2 at the Mellin-cone pole s=3, evaluated on D_K eigenvalue grid {lambda_k} INSIDE the BZ at O(M_KK). Orig pin S88 W4 P5 (centered finite-diff + Richardson of n_s(c_sub), S86 W1c-8 PROVEN). FI-class regulator-invariant across 5-regulator atlas {zeta,Pauli-Villars,Mellin,cutoff,mode-cutoff} at canonical L_max=12 (S91 W9). SIGN-WALLED negative by spectral-action monotonicity (PERMANENT S17a-S45; a_4>0 S73A W2-D). FORM-identical to S50 n_s2-1 (Seeley-DeWitt ratio a_4/a_2~n_s~0.9561 in role of n_s). transport-DEGREE RESOLVED S93 W7-1: deg(T_BZ->pivot)=+2 NON-SCALAR (w(L_max)*kappa(k) factorization_holds=False; the two-pole (a_4/a_2)2-1 survives the dimensionless ratio); MAGNITUDE absolute L_max->inf-convergence remains a SEPARATE open question (CF-S94); the residue itself is L_max-stable (S88 W9), the FAIL'd object is the 3-param FIRST-EXTRACTION parameterization (S91-VII-AU). SCALE-SEPARATED from alpha_s_pivot_goldstone~0 by 54.04 decades; matched (scale,channel)=(substrate/BZ, CMB-S4/CMB-HD substrate-sensitivity ~34sigma). -12.146sigma vs Planck is the moment-identity/scalar-transport reading, RELOCATED off-pivot as a SCALE-MISMATCH (NOT a falsification) per the RESOLVED NON-SCALAR transport (S93 W7-1) — the realized matched-channel reading is the substrate/BZ leaf, with the CMB pivot at +0.67sigma consistent. SECTION E. (S92; degree resolved S93 W7-1)
rho_FULL_CC_VII_AU_SAT_s3 = 1.0076927826  # FULL-CC saturated canonical at VII.AU.OP-PROJ substrate-distance-1 pole s=3 (rho_FULL(s=3,L=14)=M_FULL/M_BARE under FULL Connes-Chamseddine 1996 sec.2.2-2.3 Pauli-Villars multipliers (M_KK,+2,sqrt2*M_KK,-1) on s87_spectrum_cache_L14_tau019.npz). CLASS=FULL-MARGINAL-SAT: rel_drift |rho(L14)-rho(L12)|/|rho(L12)| = |1.0076927826-1.0100907902|/1.0100907902 = 2.3740515966e-03 in INFO band [1e-3,1e-2); level_2_envelope_marginal_saturation_rate=0.0024_per_dL=2 (NOT Friedrich-Bar PASS-saturated at L_max in{12,14}; 25.14pct NEW-sector intrusion ratio at s=3). supersedes=0da19aba653fa19ddf7bf2178581ec5c767c115e4508dd6e92906e68e6875e1f (S91-W1-14-COMPOSITE-BRIDGE-MAP-RDX, s91_gate_verdicts.txt:221, Option A protocol). STRUCTURAL-ORTHOGONAL-COMPANION on the level-pin axis to the SCHEMATIC two-pin convergence-exponent protocol (alpha_canonical_VII_AU_OP_PROJ_FW_ASYMPTOTIC=-3 + alpha_sample_VII_AU_OP_PROJ_FW_PATHWAY_B_L15_22=2.6926) retained at CLASS=SCHEMATIC per substrate-first-canonical-sourcing.md sec.(iv) K=4 MANDATORY level-pin discipline. Atlas-row/cache-moment are two members of the weighting-functional family per cross-pillar-bridge-corpus.md sec.19 (3-layer K-counter REJECTED at sec.19(c)). Provenance: this gate audit_sha256=32535ca1c704115016f83162c8b37c71784da16f7c2796c88eb0843bfde73243; rho_FULL(s=3,L=12)=1.0100907902; rho_FULL(s=3,L=14)=1.0076927826. Landed in-session during S92 housekeeping cleanup (NOT S93) per CLAUDE.md No-Technical-Debt + feedback_fix-in-session-never-defer.md; mack-cosmic-bridge sole writer per feedback_mack-bridge-role.md (S92)
alpha_b_VII_AU_OP_PROJ_FW_LMAX14_EXTENSION = 2.600027208109481  # Level-3 saturation-entry alpha_b at L=14 window [12,14] (NEW S92 W5-1 L=14 canonical confirmation; Source-Recon class (e) PIN-PROMOTES-TO-CANONICAL-ON-PASS promoted_from=S92-W5-1). VII.AU.OP-PROJ analytic-shadow convergence exponent; CLASS=FULL K=4 level-pin (W7a-74 PRIMARY evaluator, NOT SCHEMATIC) (S93)
n_PBH_FW_central = 7.2761e-23  # m^-3; PBH band-edge framework prediction (FWD-C5 Pillar I<->Pillar IX cardinality-cascade-tail saturation); n_PBH = n_edge_saturated * prob_form / L_pix_LRD^3 at L_max=14; Cell-I-cardinality-projection algebra-INVARIANT spectrum-only functional; VII.AX.OP-PROJ Level-3 anchor T1.13 PASS audit_sha256=1dc0a3fe...; Level-3 inside upper-22.6%-conjunct [5.5e-23, 2.2e-22] m^-3 (32.3% above floor); PROVISIONAL truncation: per S93 W4-3 INFO (resolution-beta, w(L_max) DIVERGENT, N_eigs grows geometrically) the canonical L_max=14 label is provisional and Eq.(2-prime) reads (still converging) -- canonical-truncation re-determination is carry-forward CF-S94; STAGE-3-PERMANENT-eligible per S92 W6-3 / S93 W4-1 Stage-2 PASS-AND; publication precision 5 sig figs, downstream verifier rel_tol >= 1e-4 per Class-8.3; canonical-write-order Step 2 (Step 1 verdict + Step 3 inventory discharged S91 W5-4) (S93)
delta_tau_crit_neg = -0.0750  # Negative-side Jensen-moduli breakdown of the bottom-20 4-stratum partition (2,4,8,6): anticrossing-swap to (4,2,8,6) at delta_tau=-0.0750+-0.005. §VII.AE moduli-space tau-asymmetry (S88 W2-9, PERMANENT; atlas-03 E40). Imported by Phononic-crystal-geometry_viz.py Vis-8 (SX W8). Level-2 moduli-deformation substrate-IS observable. (SX)
delta_tau_crit_pos = 0.175  # Positive-side Jensen-moduli breakdown of the bottom-20 4-stratum partition (2,4,8,6): stratum-coalescence at delta_tau=+0.175+-0.05. 2.33x neg/pos asymmetry ratio vs delta_tau_crit_neg=-0.0750. §VII.AE moduli-space tau-asymmetry (S88 W2-9, PERMANENT; atlas-03 E40). Imported by Phononic-crystal-geometry_viz.py Vis-8 (SX W8). (SX)
d_s_fold_window_sigma = 1.4005  # Fold-window diffusion time sigma_* = 1.4005 M_KK^-2 for the spectral-dimension functional d_s(sigma)=-2 dlnP/dlnsigma on the Jensen-deformed SU(3) D_K NORMAL-STATE (Delta=0) spectrum, P(sigma)=Sum dim(p,q) Sum_i exp(-sigma lambda_i^2). UV d_s->8 (Weyl, dim SU(3)=8). S92 ad-hoc workshop spectral-dimension d_s flow vs CDT. Imported by Phononic-crystal-geometry_viz.py Vis-10 (SX W8). (SX)
R_canonical_bridge = 7.324974378387362  # R_canonical = cocycle-norm ratio phi_67/phi_88 = 7.324974378387362, scheme=Hochschild-cocycle-times-Chern-character, convention=BdG-restricted-Connes-Karoubi-pairing-Cell-I. Cross-pillar bridge geometry anchor (§VII.W first bridge S86; S89 W2 observable-identity). Equals substrate_cocycle_ratio_67_88 (7.3249917...) to 5 sf. Imported by Phononic-crystal-geometry_viz.py Vis-11 (SX W8). (SX)
Level3_integer_anchor_VII_AU_OP_PROJ_3HEB_BDI = 2  # Integer 3He-B BDI branch-count Level-3 anchor for the STAGE-3-PERMANENT §VII.AU.OP-PROJ FWD-C1 (Pillar-I<->II) bridge. = |N_K| = 2 via AZ-class-BDI bulk-boundary correspondence; N_K=2 is the BDI winding (KO-dim=6) read from S94-VII-AU-WINDING-RECONCILIATION (PASS; winding-bearing pairing = BOTH-(alpha-rep-side-J-twisted-K-homology-AND-beta-BdG-sector-chi-inherited); N_K_for_level3=2), NOT from the gamma_9 chiral index T_signed (=0; S93 W2-1 balanced 8/8 spinor grading wall). TOPOLOGICAL-INTEGER Level-3 row, COMPLEMENTARY to (not replacing) the continuous Planck n_s=2.0952sigma anchor and the alpha_canonical_VII_AU_OP_PROJ_FW_ASYMPTOTIC=-3 Layer-1 asymptotic. Envelope-free Level-2: a Z-valued topological invariant is L_max-saturated once the winding sector is resolved (L_resolve=10), so envelope_residual=|2-2|=0 for all L_max>=L_resolve (NOT an L^{-3} decay); registry-PASS criterion (Level-3<Level-2) satisfied vacuously-and-exactly. Level-1 single-tau-slice substrate-IS observable at tau_fold=0.19. canonical-write-order Step 2 (verdict line emitted first) (S94)
v_g_B2_fold = 0.022699323  # B2-band leading group velocity at tau_fold, rho-pinned (substrate-natural, Claim-B): v_g = 1/(pi*rho_B2_per_mode) = 1/(pi*14.023250) = 0.022699 (M_KK units). Band-dispersion-ladder value (primary geometric order-probe) = 0.05410. BOTH > v_g_floor=1e-2 => Reading-van-Hove (v_g->0 flat band) REFUTED at the NORMAL-state lambda(tau) band-dispersion layer. n_dispersion=1 (linear, gamma_E=0), NOT n=2 sqrt-edge. Gate S94-DS-GAMMA-E-RESOLUTION composite=INFO. (S94)
residue_s6_PS_Linf = 9.393639575775e-4  # SU(4)_PS full-spectrum Mellin-cone residue at convergent pole s=6, L->inf limit (FWD-C4 §VII.BE Tier-1 re-anchor; confirms S94 W3-9 target 9.39363958e-4 to |delta|=4.22e-13). The inherited s=4 pole DIVERGES (shell-sum L^(8-2s) converges iff s>9/2=4.5; rank-4 A_3 shifts threshold +1 unit vs SU(3) s>3/2) (S95)
alpha_PS_residue_tail_s6 = 2.803571  # EMPIRICAL SU(4)_PS spectral-action residue truncation-tail exponent at s=6 (full-grid fit; tail-only L>=16 variant 2.881902 used for the Level-2 Friedrich-Bar envelope C_FB*L^-2.882). Tag FI. DISTINCT from the HH^1-cocycle Wodzicki alpha_HH1_per_pole_FW_s6=8 — do NOT conflate (different spectral functionals: spectral-action residue tail vs HH^1 cocycle norm) (S95)
n_PBH_FW_saturated_tail = 1.7581364216177778e-23  # m^-3; L_max-INDEPENDENT substrate-physical PBH number density at the g-axis cardinality-cascade SATURATION generation g_saturate=143 (FROZEN atlas N=78080 = analytic N_eigs(10)=80080 minus dropped (4,4) sector); n_PBH_sat = C(78080,2)*prob_form/L_pix_LRD^3 = 3048204160*0.15573/(3e10)^3 (Sage-exact QQ 24723793429/1406250000000000000000000000000000); DISTINCT observable from n_PBH_FW_central=7.2761e-23 (the linear-L14 divergent-channel anchor; canonical/saturated ratio = 4.1385298 = Sage-exact L10->L14 refinement 3528281250/852544601). Tier-2-DIMENSIONFUL (cross-pillar-bridge-anatomy.md Tier-1/Tier-2 gate; corpus §25.1): the m^-3 magnitude lives on the divergent cardinality channel sharing its multiplicative slot with the dimensionless cascade exponent d ln N_eigs/d ln L -> 5, so the §VII.AX m^-3 Level-3 row stays HELD NOT-SATISFIED-PENDING-substrate-physical-scale-anchor; this gate DECOUPLES the magnitude (pinned to the substrate-physical g_saturate value) from the truncation question. §VII.AX.OP-PROJ theorem-STRUCTURE STAGE-3-PERMANENT (unchanged). Held-number guard (S95 W6 context §A4): magnitude HALF of ONE held row; NOT double-counted (S95)
Lambda_sp_over_M_KK = 2.06  # species scale ratio Lambda_sp/M_KK; THIN EFT-breakdown shell [M_KK, 2.06 M_KK]; consumed by S96-SDW-EFT-CONTROL (S96)
a_6_FW_zeta = 765.593826  # zeta-regulated 6th Seeley-DeWitt moment a_6 = 0.5*sum_modes m_k|lam_k|^-6 (per-branch L_max=3); bit-exact same footing as a_0/a_2/a_4 (cross-check 2x cache = canonical); CC-cone n=6 / s=1 pole residue (S96)
a_8_FW_zeta = 521.183178  # zeta-regulated 8th Seeley-DeWitt moment a_8 = 0.5*sum_modes m_k|lam_k|^-8 (per-branch L_max=3); bit-exact same footing as a_0/a_2/a_4; CC-cone n=8 / s=0 pole residue (cone closes here) (S96)
f_FW = 0.5254916357116971  # Framework linear growth rate f=dlnD/dlna at z=0 (vs f_LCDM=0.527130); -0.311% bare-f suppression, a2-channel growth. PROVEN; surfaced to scorecard S96-OBS-FSIGMA8-FORECAST (S96)
f_LCDM = 0.5271303865722888  # LCDM linear growth rate f=dlnD/dlna at z=0 (Omega_m=0.315 borrowed-H baseline); comparison anchor for f_FW (S96)
fsigma8_product_suppression_FW_max_pct = -4.058  # Max fractional f*sigma8 PRODUCT suppression FW vs LCDM, -4.058% at z=0.51 (the '~4%' figure; NOT bare-f which is -0.311%). Zero-parameter LSS discriminator; forecast sigma-distance 1.013(DESI-5yr)/1.534(Euclid). S8-tension-relieving (S96)
f_bare_suppression_FW_pct = -0.311  # Bare growth-rate f fractional suppression FW vs LCDM at z=0 = (f_FW-f_LCDM)/f_LCDM = -0.311% (delta_f=-819/500000). The SMALL number, distinct from the -4.058% f*sigma8 PRODUCT suppression (C5 conflation guard) (S96)
A_FS_first_sound_ring = 0.204  # First-sound ring amplitude A_FS = c2^2/c1^2 = 1/[3(1+R_*)] (two-fluid acoustic ratio, NO LCDM counterpart). LIVE BAO falsifier at k1=0.0193 Mpc^-1, r1=325.3 Mpc; SNR=8.6 at DESI-5yr (S96-OBS-FIRST-SOUND-RING PASS) (S96)
r1_first_sound_ring_Mpc = 325.3  # Comoving first-sound horizon r1 = 325.3 Mpc (substrate metric-mode c1=c acoustic horizon at recombination). Ring imprint scale; k1=2pi/r1=0.0193 Mpc^-1 (S96-OBS-FIRST-SOUND-RING PASS) (S96)
k1_first_sound_ring_invMpc = 0.0193150486  # First-sound ring wavenumber k1 = 2pi/r1 = 0.0193 Mpc^-1 (the k where the A_FS=0.204 ring imprints on matter P(k)) (S96-OBS-FIRST-SOUND-RING PASS) (S96)
sigma_Pk_DESI_Y5_BAO_scale = 0.023529411764705882  # FETCHED DESI-5yr (Y5) 1-sigma fractional P(k) amplitude error at BAO scales = DR1 4.0% / 1.7 volume downscale = 2.35%. The sigma_exp(k1) anchor for first-sound-ring detectability SNR=A_FS/sigma_exp=8.6 (S96-OBS-FIRST-SOUND-RING PASS) (S96)
f_obs_CGWB_peak_kappa_nat = 8.4835e39  # Observed CGWB peak freq [Hz] at substrate-natural kappa=hbar/M_KK: fold van-Hove ACOUSTIC emission M_KK/(2pi) redshifted by a_fold/a_now=0.4723. GHz+ band, 43.9 decades above LISA. D4 resolved AGAINST mHz; CGWB-peak LISA flagship evaporates (distinct from Omega_GW amplitude flagship). NOT thermal-GUT (naive route gives 1.7 GHz) (S96)
f_NL_total_GGE_S67 = 1.03  # Central GGE-bispectrum f_NL total amplitude = 1.03 (the relic's actual non-Gaussianity; sigma_dist=0.378 folded -0.9+-5.1 / 0.575 equilateral -26+-47, BOTH inside Planck 1sigma). DISTINCT from max_f_NL_FW=1.505 which is the SATURATION BOUND (|Bog-sudden channel f_NL=-1.505|). The capstone -1.505 headline = -max_f_NL_FW (bound), NOT this central value. Gate verdict INFO (Track B: relabel proceeds + sign-convention footnote; folded-config sigma-ordering inverted by sign-coincidence) (S96)
t_star = 0.08832  # t* = 0.08832 one empirical spectral-functional coupling (Lambda_QCD analog of the substrate); S72 functional fit; DISTINCT from mellin_f_star_f0=0.08832 (near-coincident but a different observable, lizzi-flagged UNTESTED-as-derivation) (S72)
R1_lizzi = 1.128655  # R1_lizzi = a0*a4/a2^2 FI scheme-invariant spectral-moment ratio (Vol(K) cancels per Baptista B2; R-protected dimensionless); = 6440*1350.7216/2776.165389^2 = 1.128655; sp V.7 Sage-verified (S74)
R_therm = 5251.82  # R_therm = t_therm/t_transit = 5251.82 diabatic transit/thermalization timescale ratio; keeps the GGE relic an Ordered Veil (integrable, never thermalizes); S95 W5 (S95)
Mass_LeggettDM_over_Delta_BCS = 11.97  # Mass_LeggettDM/Delta_BCS = 11.97 substrate-IS dark-matter mass anchor on the BCS gap scale (Leggett inter-band coherence mode, CPT-neutral non-annihilating); CONDITIONAL on Gamma_grav < H_0 (S70)
c_s2_FW = 0.0  # Framework 4D Goldstone sound speed = 0 EXACTLY by Kasparov product factorization (m_Goldstone^4D=0, S74 QA-VdD workshop). Layer-1/topology, scheme-independent, zero-parameter. Registry entry VII.BH. (S96)
c_s2_kasparov_bound = 9.21e-4  # S71-72 Kasparov upper bound on a constant dark-sector c_s^2; Level-2 laboratory-IN envelope for the c_s^2=0 topological prediction. Registry-PASS: c_s2_FW=0 < 9.21e-4. Registry entry VII.BH. (S96)
x_fold = 85.7928  # ODLRO fold value x=rho_s/rho_n at tau_fold=0.190 (S67 origin); lower-bound threshold confirmed-used by S97 W1 (x_today band [103.22,117.22] > x_fold, monotone) (S67)
Omega_BA_fold = 2.241353  # conformal factor Omega_BA = sqrt(G_mod)/a_eff at tau_fold (S95-W4-4 conformal-embed); reproduced by S97 W1 Omega(tau)=sqrt(rho_s/a2) to rel 1.5e-4 (= sqrt(Gamma_effacement) effacement leak) (S95)
Omega_GW_acoustic_LISA_tail = 4.046e-132  # Acoustic Omega_GW IR-tail re-pin VALUE at LISA pivot (3 mHz): Omega_GW(3mHz)=Omega_peak*(f_LISA/f_peak)^p = 9.15e-5 * 10^(-42.451453809*3) = 4.046e-132 (log10=-131.393, Sage-QQ-exact log-ratio). Derived IR slope p=3 (causal default; van-Hove steepening REFUTED, n_dispersion=1 linear fold edge, gamma_E=0; analyticity floor p>=1). 118.39 OOM below LISA-PLS, kappa-robust across [1e-20,1e-10]. REPLACES the retracted Omega_GW_Lambda_A_LISA=1e-10 placeholder. LISA-sterile; detectability settled slope-robustly S96 W-3. Substrate-IS: acoustic signature of the post-transit GGE relic, peak at substrate scale 8.4835e39 Hz (S97)
Omega_DM_h2 = 0.1200  # OBSERVATIONAL-ANCHOR (Planck-observed physical DM density Omega_DM h^2; lab-IN datum, cross-check anchor only per substrate-first-canonical-sourcing.md SS(i); NOT a substrate prediction even though the framework Leggett-channel value matches at 0.6%). DISTINCT from Omega_DM_obs=0.264 (canonical_constants.py:539, Planck density PARAMETER Omega_DM) -- the two are NOT to be conflated: this is the physical density (Omega*h^2), that is the dimensionless density parameter. (S97)
rho_vac_over_rho_obs = 1.032  # FRAMEWORK-PREDICTION (substrate-first; gate DILUTION-CC-66/S66 Scenario B closes the 114-OOM cosmological-constant gap to 0.01 OOM, CC_OOM=115.5). Substrate-IS: a_0 Seeley-DeWitt zeroth moment tracks the Volovik H^2-scaling vacuum (D_K eigenvalues -> a_0 -> rho_vac -> rho_vac/rho_obs). C10 (Atlas-04) rho_vac ~ M_Pl^2 H^2 is ASSUMED-PARTIALLY-PROVEN -- the C10 conditionality is carried here so the pin does not overstate its register status. (S97)
R_cross_yukawa_t1_t2 = 1.019704  # Between-class Yukawa ratio R_cross = max/min of lightest distinct |lambda| across the two spectrally-distinct generation classes (t=1 == t=2 by J-orbit rigidity; n_distinct=2). LOCKED to ~1 (NOT the SM hierarchy) by the multiplicity-scalar representation pi(a)=+_(p,q) pi_(p,q)(a) (x) 1_m(p,q): EXACT at all L_max, INVARIANT under the entire inner/twisted/opposite A_K-fluctuation orbit (Skolem-Noether: Aut(A_K) multiplicity-blind). GENERATION-BLINDNESS OBSTRUCTION (SS-VII.BL, theorem E1 Non-LI-Deformation-Necessity, STAGE-1-CANDIDATE). Reality [J,D_K]=0 is INNOCENT; the wall is homogeneity/left-invariance. The Yukawa hierarchy requires an EXTERNAL non-LI fibre connection eps_LX outside every A_K-module (lepton analog of the baryogenesis phi_88-Cartan deltaA). NON-PROMOTION-BY-HELD-NUMBER (sign-lock differentia); held number, NOT a framework prediction. local-diagnostic-anchor, not a downstream-consumed constant. (S97)
sigma8_OZ_50 = 0.799  # sigma_8 spectral-action / Ornstein-Zernike (O-Z) channel; a0-region; HEADLINE sigma_8. CROSS-NOTE: TWO distinct substrate-IS spectral-channel sigma_8 readouts: O-Z sigma8_OZ_50=0.799 (this) vs a2-growth sigma8_growth_a2=0.79317 (S70/S96/S97) are ~0.7% apart (|0.799-0.79317|/0.79317=0.735%), O-Z LARGER; NOT two measurements of one container number (a0-region spectral-action amplitude vs a2 Seeley-DeWitt growth amplitude feeding fsigma8). BOTH distinct from LCDM reference sigma_8=0.811 (Planck 2018): O-Z -1.50% vs LCDM, growth -2.18% vs LCDM. Do NOT read the ~0.7% inter-channel spread as a single-channel uncertainty band (S98)
sigma8_growth_a2 = 0.79317  # sigma_8 a2 Seeley-DeWitt growth channel; linear growth f=dlnD/dlna feeding fsigma8; -0.311% bare-f suppression, -2.18% vs LCDM. CROSS-NOTE: TWO distinct substrate-IS spectral-channel sigma_8 readouts: a2-growth sigma8_growth_a2=0.79317 (this) vs O-Z sigma8_OZ_50=0.799 (S50, HEADLINE) are ~0.7% apart (0.735%), O-Z LARGER; NOT two measurements of one container number (a2 Seeley-DeWitt growth amplitude vs a0-region spectral-action amplitude). BOTH distinct from LCDM reference sigma_8=0.811 (Planck 2018): growth -2.18% vs LCDM, O-Z -1.50% vs LCDM. Do NOT read the ~0.7% inter-channel spread as a single-channel uncertainty band (S98)
rho_vac_over_rho_rad_BBN_below = 0.474049  # BBN-epoch Volovik tracking-vacuum fraction at n_eff=1.978 (from-below); FAIL-side falsifier value (0.474 > BBN bound 0.2271). from-below relief DIRECTION correct (sign=PASS) but quantitatively INSUFFICIENT (magnitude=FAIL); Window-8/BBN-VOLOVIK-67 still OPEN at nucleosynthesis. Present-epoch DILUTION-CC rho_vac_over_rho_obs=1.032 UNAFFECTED (z=0 lever=1). C10 stays ASSUMED-PARTIALLY-PROVEN (S98)
delta_N_eff_vacuum_BBN_below = 2.0873  # BBN Delta-N_eff from Volovik vacuum at n_eff=1.978 (from-below); FAIL-side falsifier value (2.087 > 1, exceeds Planck+BBN delta_N_eff bound). Quantifies the residual BBN tension after the from-below relief; BBN-VOLOVIK-67/Window-8 OPEN. Companion to rho_vac_over_rho_rad_BBN_below (S98)
Sigma_mnu_FW = 0.0582053272  # Neutrino mass sum Sum m_nu [eV], substrate type-I seesaw m_nu=-m_D^T M_R^-1 m_D; M_R=D_K B-branch fold energies (M_3(C) KO-dim-6 Pfaffian, S96-MATTER-0NUBB), m_D Dirac-Yukawa seesaw-consistent; normal ordering m_nu=[0,0.0086776,0.0495278] eV. PASS vs DESI 2024 bound 0.072 eV. m_D Yukawa normalization oscillation-anchored (NOT zero-free-param) - substrate-FIRST content is M_R + seesaw structure + suppression direction + normal ordering (S99). UNIQUENESS-INFO (S100a-MD-NORMALIZATION, audit 4f92a5513ad69b07): D_K bottom-triple->Y_i map NON-UNIQUE (MAP-A vs MAP-B uniq_ratio 0.4742 > 0.05; both maps ~100x below this value) - the Dirac-scale anchor is irreducibly external (track_B 0.9); S99 oscillation-anchored caveat PERMANENT. Value unchanged.
Sigma_mnu_bound_DESI_2024 = 0.072  # DESI 2024 cosmological upper bound on Sum m_nu [eV] at 95% CL (FETCHED external observational falsifier, NOT a substrate constant; lives in the gate PASS criterion). Sum m_nu_FW=0.058205 eV PASSes this bound by 19% (S99)
phi_CP_K7_transit = 1.5707963267948966  # = pi/2 EXACT — K_7 TRANSIT CP phase (baryogenesis; phi_88-Cartan unique non-leptophilic CP source; substrate-FIXED, not scanned). NOT the PMNS leptonic delta_CP (see delta_CP_PMNS_substrate). Legacy bare phi_CP is sector-ambiguous — cite the sector-keyed names. (S100b)
delta_CP_PMNS_substrate = 0.0  # PMNS leptonic Dirac phase — Scenario-A {0, pi} representative (real-eps_LX texture ansatz); 0.0 is the representative value of the two-valued set. NOT KO-6-forced: S116 W-1 forced-vs-artifact workshop down-tagged this to ANSATZ-ARTIFACT-as-derived / CONDITIONAL-PENDING-CF-W2-1 (the '[J,D_K]=0 / J-self-conjugacy forces delta_CP in {0,pi}' justification STRUCK as a non-sequitur; [J,D_K]=0 is necessary infrastructure, not sufficient — the sector-uniform J coexists with J_CKM!=0, the KO-6 grading eps''=-1 PROTECTS the gamma9-odd phase, D_K self-adjointness fixes the Yukawa prescription). Disfavors B-class textures (delta~1.5pi). NOT the K_7 transit phase pi/2 (see phi_CP_K7_transit). (S100b; scope corrected S116 W-1)
sigma_over_m = 5.7e-51  # CDM self-interaction sigma/m = 5.7e-51 cm^2/g (collisionless anchor; gravitational Rutherford transport, zero free parameters); promoted_from = S100a-W1-4-SIGMA-DM-NUCLEON plan-freeze pin confirmation (S42)
sigma_DM_nucleon_FW = 1.2989252548383697e-63  # Leggett-channel GGE DM spin-independent per-nucleon cross-section, cm^2 (pure gravitational coupling floor alpha=G_N*M_DM*m_N; equal-above-threshold-rate Xe contact-SI normalization, v=1.1e-3c, E_th=5keV; publication precision 3 sig figs = 1.30e-63). 30.9 OOM below LZ-2024 exclusion, 30.0 OOM below Xe nu-fog at M_DM. Inherits C7 conditionality (Gamma_grav < H_0) (S100a)
M_DM_Leggett_GeV = 4.128202383934713e+17  # Leggett-channel GGE DM laboratory rest energy, GeV = Mass_LeggettDM_over_Delta_BCS * Delta_BCS * M_KK = 11.97*0.4642547394830737*7.428660036284456e16 (Frame A BINDS: single unit map via a_2/G_N bridge; gapped-mode rest energy = hbar*w_0; comoving relic T0i=0). Publication precision 3 sig figs = 4.13e17 GeV. Inherits LEGGETT-MOMENT-70 conditionality (Gamma_grav < H_0) (S100a)
m_bb_FW = 0.0036950127968154492  # 0nubb effective Majorana mass m_bb = |Sum U_ei^2 m_i| [eV], central (delta_CP=0, zero Majorana phases; no-cancellation upper funnel edge). KO-dim-6 Pfaffian Majorana texture (M_3(C) singlet, S96-MATTER-0NUBB determination re-confirmed) x S99 NO masses [0, 0.0086776, 0.0495278] eV (oscillation-anchored; track_B residual-Dirac-scale caveat per S100a-MD-NORMALIZATION INFO) x plan NuFit U_ei pins sin2th12=0.307 sin2th13=0.0220. Majorana-phase band [1.5158e-3, 3.6950e-3] eV. PASS vs KamLAND-Zen 0.122 eV (x33.0 below); inside NO funnel [1.5e-3, 4.5e-3] eV; below next-gen floor 0.010 eV (detection above funnel falsifies). delta_CP in {0,pi} m_bb-degenerate. publication_precision=4 (full float64 here + npz) (S100a)
m_H_FW_KK_threshold = 131.8  # GeV; FRAMEWORK m_H prediction (NOT PDG) — KK threshold corrections to the |S|^2 fiber-embedding transverse mode at the Jensen-deformed fiber. r_KK = 131.8/125.1 - 1 = 67/1251 exact = +5.356% vs m_H_obs. Promoted S100a W4-13 per canonical write-order (math-scripts.md) (S100a)
m_H_FW_tree = 134.0  # GeV; FRAMEWORK m_H tree-level prediction (NOT PDG) — lambda_h = (4/3) g_3^2(M_KK) * (a_4/a_2), cutoff-shape-INDEPENDENT for all 6 cutoff families; m_H(tree) = v_ew*sqrt(2*lambda). r_tree = 134.0/125.1 - 1 = 89/1251 exact = +7.114% vs m_H_obs; BCS threshold correction ~-7% (S62 THRESHOLD-62) is the documented 134 -> ~125 mechanism. Promoted S100a W4-13 per canonical write-order (S100a)
spinor_norm_factor_FW = 4.0  # M_Pl,eff/M_Pl,unred = sqrt(16) = 4 EXACT — first-principles spinor normalization: Tr_spinor=2^[8/2]=16 (Clifford(R^8), Res_{s=8} zeta_D carries 16, S87), graviton retains 4 of 64 Delta_12 (Route D, S58); empirical 3.92 (S59 NORM-59) agrees at rel=1/49=2.041% (PW-truncation residual). atlas-08 Q27 RESOLVED; grounds H0=65.4 (S100a)
m_tau_PDG = 1.77686  # GeV, PDG tau lepton pole mass. NOT the canonical m_tau=2.062 (S42 modulus mass at fold, M_KK units - name collision; the plan-w2 input ledger mis-grouped it among PDG lepton masses). Use THIS for any PDG charged-lepton anchor; never use m_tau=2.062 as a PDG target (circularity, agent-memory S100b W2 plan-freeze catch). (S100a)
m_u_msbar_2GeV = 2.16e-3  # GeV, up-quark MS-bar mass at 2 GeV (PDG 2024). Light quarks have no meaningful pole mass; PDG headline scheme. W3-9 held-out quark-ratio anchor. (S100a)
m_d_msbar_2GeV = 4.70e-3  # GeV, down-quark MS-bar mass at 2 GeV (PDG 2024). W3-9 held-out quark-ratio anchor. (S100a)
m_s_msbar_2GeV = 93.5e-3  # GeV, strange-quark MS-bar mass at 2 GeV (PDG 2024). W3-9 held-out quark-ratio anchor. (S100a)
m_c_msbar_mc = 1.2730  # GeV, charm-quark MS-bar mass at its own scale (PDG 2024 headline). W3-9 held-out quark-ratio anchor; pole variant m_c_pole for scheme sensitivity. (S100a)
m_c_pole = 1.67  # GeV, charm-quark pole mass (PDG 2024). Companion to canonical m_b_pole=4.78 / m_t_pole=172.69; W3-9 PDG-POLE scheme-sensitivity diagnostic. (S100a)
m_b_msbar_mb = 4.183  # GeV, bottom-quark MS-bar mass at its own scale (PDG 2024 headline; the existing m_b_1S=4.18 pin carries a mislabeled-scheme name). W3-9 held-out quark-ratio anchor. (S100a)
V_us_PDG = 0.22500  # CKM |V_us| central (PDG 2024). The ONE mixing datum arg(w) is fitted to in W3-9 (plan CKM_fit_anchor). sigma in V_us_sigma_PDG. (S100a)
V_us_sigma_PDG = 0.00067  # 1-sigma uncertainty on |V_us| (PDG 2024); W3-9 fit-anchor band. (S100a)
V_ub_PDG = 3.82e-3  # CKM |V_ub| central (PDG 2024). W3-9 held-out theta13 anchor: theta13_PDG = arcsin(V_ub_PDG) = 0.2189 deg. (S100a)
V_cb_PDG = 40.8e-3  # CKM |V_cb| central (PDG 2024). W3-9 held-out theta23 anchor: theta23_PDG = arcsin(V_cb_PDG) = 2.338 deg. (S100a)
J_CP_PDG = 3.08e-5  # CKM Jarlskog invariant central (PDG 2024). W3-9 held-out J_CP anchor; plan pre-registered band [2.0e-5, 4.0e-5]. (S100a)
delta_N_eff_budget_GoldsteinHill_2026 = 0.107  # EXTERNAL observational falsification budget (Goldstein-Hill 2026, arXiv 2603.13226, N_eff=2.990+/-0.070, combined BBN+CMB+BAO, 95% CL); NOT substrate-derived; distinct from the canonical element-abundance gate threshold (7/8)(4/11)^(4/3); verified verbatim from paper-11 PDF (SHA 13055d9f...); z0-lever crossing n_eff(0.107)=1.904348 (S100b)
T_RH_GeV = 1.70e15  # S76 W2-H reheating scale, run-time verified at S100b W1-1: T_RH=(90/(pi^2 g_*))^(1/4) sqrt(Gamma M_Pl_red) with Gamma_total=4.05e12 GeV (same npz), g_*=106.75 gives 1.6977e15 (pin = 3-sig-fig image, ratio 0.9987); tau_decay=hbar/Gamma=1.625e-37 s matches S76 header 1.63e-37 s; promoted per S100b W1-1 registration block (volovik-R3 hygiene flag closed) (S100b)
S_capture_floor_LRD_classic = 0.25  # LRD classic-extreme-color-cut capture floor: classic cuts (F277W-F444W > 1.5 mag, Akins/Barro) isolate <= 25% of the LRD population. Laboratory-IN observational-methodology anchor (NON-PHONONIC). S_band=[0.25,1.0]; widening W=1/S >= 4 (+0.602 dex upward on the intrinsic side). Consumed by s100b_selection_fold.py wrapper + W7-1/W7-2(mode-B)/W7-3 (S100b)
m_proton_g = 1.67262192369e-24  # Proton mass in grams (cgs). The 'm_H' of gas-collapse formulas (c_s, T_vir, M_J use mu*m_p convention); named m_proton_g to avoid collision with m_H_obs (Higgs). Added per W7-2 plan pin physical_constants add-with-provenance-before-use (S100b)
M_sun_g = 1.98841e33  # Solar mass in grams (cgs): M_sun = (GM)_S,nominal / G_N = 1.98841e33 g. Added per W7-2 plan pin physical_constants add-with-provenance-before-use (S100b)
pc_to_cm = 3.0857e18  # Parsec in cm. Completes the pc-family unit ladder (Gpc/Mpc/kpc already canonical). Added per W7-2 plan pin physical_constants add-with-provenance-before-use (S100b)
yr_to_s = 3.15576e7  # Julian year in seconds (exact). Used for Mdot [M_sun/yr] and t_SMS [Myr] conversions in the W7-2 collapse chain (S100b)
f2_dict_CC = 92.0  # a_2-channel spectral-action dictionary coefficient f_2: 1/(16 pi G_eff) = f_2 Lambda^2 a_2/(48 pi^2) at Lambda=M_KK_gravity. Third consuming script (W7-2) triggers the 3+-script promotion rule (math-scripts.md). Reproduces G_N to 0.33 percent with a_2_FW_zeta + M_KK_gravity (S42 anchor reconstruction) (S100b)
kappa_UV_MadauDickinson = 1.15e-28  # SFR-to-L_UV conversion kappa_UV [M_sun yr^-1 (erg s^-1 Hz^-1)^-1]; observational-anchor class (NON-PHONONIC); rho_UV_max = f_b*eps*rho_dot_Macc/kappa_UV ceiling in W7-3 (S100b)
sin2_theta12_PDG = 0.307  # PMNS sin^2(theta_12), PDG/NuFit-5.x-style NO central [lab-IN observational anchor]. This is the value the W5-2 0nubb gate CONSUMED (s100a_d5_0nubb_majorana.py in-script SIN2_TH12=0.307 # (local); verdict s100a_gate_verdicts.txt line 31 S100a-D5-0NUBB-MAJORANA PASS, audit a2d29b975d8cb170dc561a35034a24c8f8d3900358ae2e0c84465e499b34bbc6). Version-disambiguation finding (W5-2 (d2) diagnostic): the plan's "NuFit-6.0" label is de-facto NuFit-5.x/PDG central; the PDG-suffixed name preserves the consumed value exactly under an honest version tag. PAIR-OF-PAIRS promotion; the true NuFit-6.0 pair is sin2_theta12_NuFit60=0.303. 3 sig figs (Class 8.3: downstream rel_tol>=1e-3). Supersedes allowlist token sin2_12_pdg. (S101)
sin2_theta13_PDG = 0.0220  # PMNS sin^2(theta_13), PDG/NuFit-5.x-style NO central [lab-IN observational anchor]. The value the W5-2 0nubb gate CONSUMED (s100a_d5_0nubb_majorana.py in-script SIN2_TH13=0.0220 # (local); verdict line 31 S100a-D5-0NUBB-MAJORANA PASS, audit a2d29b975d8cb170dc561a35034a24c8f8d3900358ae2e0c84465e499b34bbc6). Version-disambiguation (W5-2 (d2)): plan-labeled NuFit-6.0 = de-facto NuFit-5.x/PDG central; PDG-suffix preserves the consumed value under an honest tag. PAIR-OF-PAIRS; true NuFit-6.0 pair is sin2_theta13_NuFit60=0.02225. 3 sig figs (Class 8.3: rel_tol>=1e-3). Supersedes allowlist token sin2_13_pdg. (S101)
sin2_theta12_NuFit60 = 0.303  # PMNS sin^2(theta_12), TRUE NuFit-6.0 (Sept 2024) IC19-with-SK normal-ordering best-fit central [lab-IN observational anchor]. Available for FUTURE flavor/0nubb gates; NOT the value the W5-2 gate consumed (that is sin2_theta12_PDG=0.307). The PDG-pair -> NuFit60-pair m_bb shift is -0.60% (signed -0.6014%; transcribed from W5-2 (d2) diagnostic p2_diag_angle_sensitivity_rel=0.006014, s100a_d5_0nubb_majorana.npz; verdict line 31 audit a2d29b975d8cb170...) and is DECISION-IRRELEVANT (sub-percent; well inside the 0nubb funnel band). 3 sig figs (Class 8.3: rel_tol>=1e-3). PAIR-OF-PAIRS version-disambiguation: the version label is now STRUCTURAL in the name. (S101)
sin2_theta13_NuFit60 = 0.02225  # PMNS sin^2(theta_13), TRUE NuFit-6.0 (Sept 2024) IC19-with-SK normal-ordering best-fit central [lab-IN observational anchor]. Available for FUTURE gates; NOT the W5-2-consumed value (that is sin2_theta13_PDG=0.0220). Pairs with sin2_theta12_NuFit60=0.303; the PDG-pair -> NuFit60-pair m_bb shift -0.60% is decision-irrelevant (transcribed from W5-2 (d2) diagnostic, s100a_d5_0nubb_majorana.npz; never re-derived). 4 sig figs (Class 8.3: rel_tol>=1e-3). PAIR-OF-PAIRS version-disambiguation: version label STRUCTURAL in the name; closes the NuFit-5.x-values-under-a-6.0-label silent class-conflation per substrate-first-canonical-sourcing.md. (S101)
x696_ncg_coincidence_headroom_ratio = 20.816  # CLOSED-COINCIDENT headroom: the transit x696 |beta|^2 ratio (6.9556) and the NCG BdG cocycle/projector ratio 1/pairing (6.9489) coincide at gap 0.0969809% (|beta|^2-comparison level, NOT amplitude level), which sits 20.816x INSIDE the framework's own SCHEMATIC->FULL regulator-pipeline noise Delta_FULL=-2.01874% at pole s=3 (registry VII.AF.1.OP-PROJ Reading-A 1.030902 vs Reading-B 1.0100907902). NOT a shared substrate object: closed by functional-class mismatch (Dixmier residue / Frobenius trace = first-power quotient, NOT a square) compute-independently + regulator-fragility (numerator regulator-sensitive, denominator regulator-inert, no co-variance => ratio O(2%) fragile). Routed to closed-coincidence constraint-map record constraint-mega-matrix.md SECTION XVI.1, NOT a FWD-class VII.X bridge (no registry precedent for sub-envelope-coincidence promotion; gates no new observable). Single math carry-forward CF-S102-X696-FULLCC-RATIO-STABILITY (FULL CC-1996 PV re-eval of Dixmier numerator, predicted FAIL-for-bridge at O(2%)). Calibration corpus cross-pillar-bridge-corpus.md SECTION 20.2 (quantitative sub-floor symmetry guard, K=2). Diagnostic record value, NOT a physical coupling. (S101)
BF_spine_vs_incumbent_ceiling = 31.62  # incumbent-comparison BF ceiling = 10^1.5 (m_H-only, b_mH=1.5); very-strong Jeffreys tier, NEVER decisive (0.50 dex below the >100 floor). vs random-geometry BF_spine_full=2000 (DECISIVE, model-SELECTION). The other 3 spine factors carry ZERO incumbent discrimination (CONVERGENT-DERIVED). Reference class is a property of the statistic. Ceiling structurally unliftable to DECISIVE-vs-incumbent until M_KK is derived (W-2 rank-1 N3=0 corollary) (S101)
n_s_FW_sqrt_cutoff = 0.9590  # Committed framework n_s under the Chamseddine-Connes sqrt(x) / BCS+1-loop-sqrt-cutoff GENERATING FUNCTIONAL (S67 FUNCTIONAL-SELECT-67 unique survivor, robustness-confirmed A_5->A_6 at S103 W5-2). DISTINCT scheme from n_s_framework=0.9561 (constant-eps gauge-invariant, Row #55 FWD-C1): the COMMIT pins WHICH functional (sqrt x), and sqrt(x) fixes 0.9590. Reported sigma-distance 1.4048 vs Planck 2018 0.9649+/-0.0042 (= |0.9590-0.9649|/0.0042 = 59/42; Sage-exact) is a COMMIT-branch CONSEQUENCE, NOT the decision driver (W4-20 no-data-appeal template). Falsifier-master-inventory Row #85 HELD->COMMITTED-LIVE discharge. (S103)
omega_SN_substrate = 0.0  # Schrodinger-Newton self-gravity frequency, substrate prediction: 0 EXACT (THEOREM-class; d a_2/d <x> = 0 machine-eps, sympy structural diff == 0; spectral action universal in (A_K,H_K,D_K), no |psi|^2 feedback channel). box_4_substrate placement, distinct from graviton/Moller-Rosenfeld/full-SN. Class-8.3 PIN-PROMOTES-TO-CANONICAL-ON-PASS; audit_sha256=57f48392a588bce56f8ee0aeba87a6fcbb5575b2abba50d36a2b98476f5fdf57. Yan 2411.17817 torsion-balance bound (omega_SN_Yan=1.589646e-02 rad/s) is a methodological cross-check ceiling, NOT canonical-source; ratio 0.0 < 1e-6 PASS. (S105)
R_S96_matter_hierarchy = 9.86183067373777  # The rank-1 Yukawa-wall anchor: the direct-D_K-eigenvalue-spacing-no-seesaw inter-generation RATIO R = |lambda|_heaviest/|lambda|_lightest across the (1,0)/(1,1)/(3,0) generation sectors at L_max=10, tau_fold=0.19. S96-MATTER-R-HIERARCHY: FAIL (the rank-1 wall produces R=9.86 vs the physical 3-gen hierarchy O(1e5)). scheme=direct-DK-eigenvalue-spacing-no-seesaw, convention=RATIO, L_max=10. Surfaced to canonical S-INV9-W1-1 (was verdict-file + knowledge-graph only). Cross-ref: GENERATION-BLINDNESS OBSTRUCTION SS-VII.BL (R_cross_yukawa_t1_t2=1.019704, the within-class multiplicity-scalar degeneracy; this R_S96 is the BETWEEN-sector C2-graded spacing). (S96)
C2_gen_sectors = [1.3333333333333333, 3.0, 6.0]  # SU(3) quadratic Casimir eigenvalue C2(p,q) for the three generation-relevant Peter-Weyl sectors (1,0)/(1,1)/(3,0) = (4/3, 3, 6). Representation-theoretic (NOT regulator-dependent). C2(1,0)=4/3, C2(1,1)=3, C2(3,0)=6; confirmed C2(1,1)/C2(1,0)=9/4 (S61 W8). The generation index is the SU(3) Z3-triality t=(p-q) mod 3 across these sectors (SS-VII.BL ANCHOR-2). Used as the Casimir-grading anchor for the modular-flavor-form Yukawa test (INV9-W1-1). Stored as float list; exact rationals are (4/3, 3, 6). (S61)
f_WZ = 2.888785e-06  # Wess-Zumino coefficient f_WZ; carried naturally by the c2=0 §VII.BR registry landing (HK-FWZ, inv-3 HY3/B9) (S102)
alpha_GUT_FW = 1/10.8  # GUT coupling alpha_GUT_FW = 1/10.8 (S62); 2.3x tension vs standard 1/25 — atlas-08 Q18a OPEN (KK-threshold-running candidate resolution). HK-ALPHA-GUT (inv-6 HY6) registration (S62)
ratio_gilkey = 0.4140  # W1-1 convention provenance (HK-W1-1-PROV, inv-5 B8): the atlas-row Gilkey ratio is 0.4140, NOT the cache-moment value 0.4866 — the two are distinct evaluation-layer conventions (substrate-first-canonical-sourcing.md §(ii.A) atlas-row vs cache-moment) (S70)
deg_T_BZ_pivot = 2.0  # BZ->CMB-pivot transport homogeneity degree, DERIVED ONCE on the M4 base (dedup flag iii). d_s is a log-derivative (scale-free, transport-INVARIANT); the dimensionful heat-trace amplitude P_M4 ~ sigma^(-d/2) carries homogeneity degree d/2 = 2 for the d=4 base. deg=+2 NON-SCALAR (NOT the VII.BA T2-VACUOUS scalar case), so O^pivot != O^substrate for amplitude-carrying observables (the 54.04-decade n_s/alpha_s scale separation). Cross-sector corroboration: reconciles S93 W7-1 alpha_s/fiber-channel deg_T=2.0000 (T4-non-scalar, factorization_holds=False) EXACTLY. Consumed by CF3-TIMESCAPE-H0, CF-CO34-BUBBLE-LRDT, n_s/alpha_s sector (W4). Integer-valued; publication_precision 4. (S110)
tau_NL = 95481/62500  # tau_NL = 95481/62500 = 1.527696 EXACT (Sage QQ). GGE-relic TRISPECTRUM amplitude — a parameter-free non-Gaussianity falsifier read off the squeezing spectrum (DISTINCT observable from the bispectrum f_NL). Suyama-Yamaguchi inequality respected (SY_lower=1.527696, R_SY=1.0). The bispectrum envelope test is on f_NL_total=1.03 < max_f_NL_FW=1.505 (NOT tau_NL vs the bispectrum envelope — cross-observable). Canonical write-order Step 2; mack writes falsifier-master-inventory tau_NL row (Step 3, sole writer per feedback_mack-bridge-role.md) (S110)
A_s_FW = 1.5367059962762235e-08  # impulse-quench Bogoliubov A_s = |beta_khat|^2/(2pi^2) (KZ-volume N_norm=xi_KZ^3), box-delta SUDDEN spectrum reproduces INV5 1.5367e-08 (rel_dev 3.9e-06); 89/89 fold-window modes frozen-superhorizon (Z_norm=1, RESOLVED-FROZEN); epistemic_type=POINT per S111-CF-AS3b (per-charge GGE NO-SHIFT, Delta_lambda_pivot=0 EXACT, resolves WS-AS-1 FB-temp leg). SCHEME-tuple: IMPULSE-QUENCH-BOGOLIUBOV scheme; distinct from the eps-pivot SR-flow band (Row #12 3.11-4.27e-9). A_s_FW vs Planck A_s 2.1e-9 = +0.864 OOM (S111); S116-W1-AS-CFB1 independently CONFIRMED epistemic_type=POINT (rel_dev_Lmax=5.43e-05, Friedrich-Bar bottom-saturated at L12) and GATED OOM=+0.864 IN the S115 sudden<->adiabatic axis [+0.196,+1.527]
chi_q_fold = 300338.0  # q-channel compressibility / vacuum-modulus stiffness at the fold = d^2 S/dtau^2 |_fold, M_KK^4 units (= 9.146e72 GeV^4 at M_KK_gravity). chi_q ~ S_fold fold-frozen (chi_q/d2S_fold=0.945, chi_q/S_fold=1.20); first-principles tau-scan across the Jensen family (S42 gradient-stiffness) shows full-family spread 7.87% = 0.034 OOM, vs the 118.71 OOM REQUIRED for channel-internal CC-residual closure. Lambda_residual=rho_m^2/chi_q (Paper 15 / S43 A.3.1). CCRESID standing q-channel limitation CONFIRMED on channel-internal grounds. (S114)
SC_corr_A = 1.151  # 3He-A strong-coupling gap enhancement SC_A = (Delta_A/k_BT_c)/(pi e^-gamma) at polycritical P_pc=21.22 bar. LABORATORY-IN 3He material property (Serene-Rainer 1983 weak-coupling-plus / Greywall 1986). NOT a substrate-first prediction; weak-coupling BCS value is 1.0 (S116)
SC_corr_B = 1.111  # 3He-B strong-coupling gap enhancement SC_B = (Delta_B/k_BT_c)/(pi e^-gamma) at polycritical P_pc. LABORATORY-IN 3He material property (Serene-Rainer 1983 / Greywall 1986). NOT substrate-first (S116)
delta_A_over_kBTc = 2.0302  # 3He-A reduced gap Delta_A/(k_B T_c) at polycritical P_pc=21.22 bar. LABORATORY-IN strong-coupling value (Serene-Rainer 1983 / Greywall 1986); weak-coupling BCS = pi e^-gamma = 1.7639. SC_corr_A = 2.0302/1.7639 = 1.151 (S116)
delta_B_over_kBTc = 1.9597  # 3He-B reduced gap Delta_B/(k_B T_c) at polycritical P_pc. LABORATORY-IN strong-coupling value (Serene-Rainer 1983 / Greywall 1986). SC_corr_B = 1.9597/1.7639 = 1.111 (S116)
P_pc = 21.22  # 3He polycritical pressure (bar) where A/B/normal phases meet. LABORATORY-IN (Greywall 1986) (S116)
T_pc = 2.273e-3  # 3He polycritical temperature in K (= 2.273 mK). LABORATORY-IN (Greywall 1986) (S116)
R_3HeB_lit = 0.035355875960583226  # 3He A/B gap-square asymmetry R = (Delta_A^2 - Delta_B^2)/(Delta_A^2 + Delta_B^2) at polycritical point; published +0.03536 (4 sf). LABORATORY-IN target for S116-W7-STATEPROJ-BCS, built from the reduced gaps delta_A_over_kBTc/delta_B_over_kBTc. Lab anchor, NOT substrate-first (S116)
rho_s_C2 = 7.962  # Goldstone-sector superfluid stiffness rho_s at the C^2 coset normalization (M_KK units); coefficient of the (1/2) rho_s m^2 phi_rms^2 Goldstone term in the S48 vacuum-energy functional rho_vac(tau,m)=E_spectral+E_cond+(1/2) rho_s m^2 phi_rms^2; 24x anisotropic vs rho_s(u1)=0.33; S48 W11 Trace theorem (GOLDSTONE-MASS-48/MASS-48), s48_goldstone_mass.npz; sibling of J_C2 (S48)
#  SECTION E: Cosmological Observables (Framework Predictions)
# ==============================================================================

# Spectral action CC prediction (using Kerner M_KK)
rho_Lambda_spectral = (2.0 / PI**2) * a0_fold * M_KK_kerner**4  # GeV^4 (S42)
CC_ratio = rho_Lambda_spectral / rho_Lambda_obs  # ~10^{120} (the CC problem)

# Clock constraint (S22d)
clock_coeff = -3.08            # dalpha/alpha = clock_coeff * dtau (S22d E-3)

# Voronoi / fabric (S42)
N_cells = 32                   # Voronoi cells from domain formation (S42)
L_over_xi = 0.031              # System size / coherence length — 0D limit (S37)

# Josephson couplings (S47 TEXTURE-CORR-48, s47_texture_corr.npz)
# Directional phase stiffness on 32-cell tessellation
J_C2 = 0.933                   # C^2 coset directions (4 bonds, dominant) M_KK
J_su2 = 0.059                  # su(2) stabilizer directions (3 bonds) M_KK
J_u1 = 0.038                   # u(1) direction (1 bond, softest) M_KK
T_acoustic = 0.112              # GGE acoustic temperature (S42/S47) M_KK

# Mode spectrum at fold (s37_instanton_action)
rho_B2_per_mode = 14.023250234055  # B2 DOS per mode at fold
E_B1 = 0.8191400026759529     # B1 mode energy at fold (M_KK)
E_B2_mean = 0.845269087679269 # Mean B2 energy at fold (M_KK)
E_B3_mean = 0.9782238787713764  # Mean B3 energy at fold (M_KK)

# ==============================================================================
#  SECTION E2: S52 Phonon & Structural Results
# ==============================================================================

# GL-Josephson phonon spectrum (s52_gl_josephson.npz, GL-JOSEPHSON-52 PASS)
c_Gold = 0.915                    # Goldstone sound speed (M_KK units)
c_Gold_over_c_fabric = 0.00436    # R-PROTECTED — 229x hierarchy; eigenvalue gradient ratio,
                                  # bypasses Seeley-DeWitt expansion. STRUCTURAL, drift 0.00% (S74 W4-F #20)
# Post-transit Layer-2 phononic branch speeds (BdG group velocities v_g on emergent g_M;
# M_KK units; all bounded above by the Goldstone envelope c_Gold=0.915). W1-A / W2-A;
# tabulated Phononic-C-Causality.md §3.3/§4.3. Sourced into canonical_constants per the
# S94 W5-3 substrate-first-provenance flag (any literal in 3+ scripts belongs here).
c_B1 = 0.0798                     # B1 singlet acoustic-scalar branch speed (M_KK; BAO channel, k~0.043 Mpc^-1)
c_B2 = 0.00200                    # B2 flat optical (quartet) branch speed (M_KK; van Hove plateau / flat band)
c_B3 = 0.1397                     # B3 dispersive optical (triplet) branch speed (M_KK; intermediate branch)
c_L = 0.0255                      # Leggett branch speed (M_KK; gap-massed inter-band coherence; = c_Leggett)
omega_L1 = 0.138                  # Leggett-1 frequency (M_KK)
omega_L2 = 0.192                  # Leggett-2 frequency (M_KK)
omega_H1 = 0.380                  # Higgs-1 frequency (M_KK)
omega_H2 = 1.410                  # Higgs-2 frequency (M_KK)
omega_H3 = 11.465                 # Higgs-3 frequency (M_KK)

# Quantum metric dispersion (s52_qm_dispersion.npz, QM-DISPERSION-52 PASS)
alpha_QM = -0.579                 # Quantum metric K⁴ correction coefficient

# Structural results (S52 theorems)
# PROVENANCE / DISAMBIGUATION (S93 W8-3-3 workshop, transit + lizzi, 2026-05-25):
#   Three DISTINCT physical quantities are co-listed in the ledger under the bare label "N_e";
#   they measure ORTHOGONAL processes and MUST NOT be conflated (NOT a SOURCE-RECON Class-(c) re-pin
#   — there is no single N_e to "drift" from; they are different observables, each correctly valued):
#     (1) N_e_classical = 0.1734          — GEOMETRIC stiff-limit e-fold CEILING (c_s frozen; zero acoustic
#                                           content). The pinned constant below. [S52 EFOLD-MAPPING-52 theorem]
#     (2) N_e^acoustic  ≈ 2.9202          — bulk-to-surface ACOUSTIC REDUCTION DEPTH at the fold; sound-dominated
#                                           93.07% (= 0.1734 geom + 0.0289 density + 2.7179 sound, machine-ε).
#                                           The W8-3 divisor in alpha_win_lo = s_CS/N_e. INLINE in
#                                           session-53-baptista-collab.md / s53_acoustic_efold_output.txt;
#                                           NOT pinned here. If CF-S94-NARROW-PATH-WORKSHOP-6-COCYCLE-CONSTRUCTION
#                                           cites it downstream, promote as N_e_acoustic WITH this provenance
#                                           (avoids the Class-(f) PIN-PLACEHOLDER risk, substrate-first §(v));
#                                           promotion is CONDITIONAL on that citation, NOT done speculatively.
#     (3) N_e^phys      = 3.73e-3         — physical transit DURATION = H·Δt_transit (impulsive, H·dt=0.663<1);
#                                           a THEOREM entity in baseline-findings-s66.md (S64), NOT a pin.
#   Reduction-DEPTH (2), transit-DURATION (3), and geometric-CEILING (1) are orthogonal substrate quantities;
#   the ~3-OOM spread among them is a category distinction, not a value drift. This note prevents a future
#   SOURCE-RECON false-positive when more than one surfaces under the same symbol N_e.
N_e_classical = 0.1734            # Classical (GEOMETRIC) e-fold ceiling (EFOLD-MAPPING-52, theorem); see disambiguation above
J_12_over_J_23 = 19.52            # Josephson ratio, tau-independent (CASIMIR-JOSEPHSON-52)
phi_CP = 0.0                     # CP phase, structural zero (ETA-B-52, 3 independent proofs)

# Liouvillian integrability (s52_liouvillian.npz, LIOUVILLIAN-52)
gamma_RP = 0.0398                 # Ruelle-Pollicott gap (M_KK)
t_deph_over_t_transit = 139729.0  # Decoherence/transit time ratio

# Unified action (s52_unified_action.npz, UNIFIED-ACTION-52)
F_BCS_over_V_KK = 7.1e-3         # BCS/V_KK probe ratio
IBO_ratio = 1118.0                # Inverted Born-Oppenheimer ratio (geom fast / BCS slow)

# HFB (s52_hfb_full.npz, HFB-FULL-52 PASS)
S2_HFB = -0.131                  # Pair correlation S_2(N=2) (pair-repulsive)

# Bogoliubov amplitudes (s52_bogoliubov_amp.npz, BOGOLIUBOV-AMP-52 PASS)
a_scatter = -1.58e-3              # Scattering length (M_KK^{-1})
M_Bog_max = 0.02273               # Max Bogoliubov amplitude (M_KK)

# ==============================================================================
#  SECTION E.K: K-Corridor Constants (S82-S84 promotion, gate W5-60)
# ==============================================================================
# Promoted by S84-KCORRIDOR-CANONICAL-PROMOTION (W5-60 bookkeeping gate).
# These 7 constants were floating across S82/S83/S84 scripts as repeated
# literals; canonicalizing them here eliminates hard-code drift.
#
# 7-field provenance schema: name, value, unit, session-of-origin,
# source-document, derivation-pin, gate-id  (all fields present below).
# -----------------------------------------------------------------------------

# K_R3 — K-corridor multiplicity-weighted primary point (3/3/2 band-weight)
#   name:              K_R3
#   value:             2.035
#   unit:              dimensionless
#   session-of-origin: S82
#   source-document:   sessions/archive/session-82/session-82-w2-workingpaper.md §W2-4
#                      (PS-SUBSTRATE-MATCHED-IC)
#   derivation-pin:    computations/session-82/s82_w2_4_ps_substrate_matched_ic.py
#   gate-id:           S82-W2-4-PS-SUBSTRATE-MATCHED-IC
K_R3 = 2.035

# K_match_need — Minimum K needed for Planck-match (positivity WALL)
#   name:              K_match_need
#   value:             0.6366
#   unit:              dimensionless
#   session-of-origin: S83
#   source-document:   sessions/archive/session-83/session-83-w3-workingpaper.md §G38
#                      (K-MATCHING-5-CONVENTIONS)
#   derivation-pin:    computations/session-83/s83_w3_g38_k_matching_5_conventions.py
#   gate-id:           S83-W3-G38-K-MATCHING-5-CONVENTIONS
K_match_need = 0.6366

# A_s_floor_5conv — Branch-B A_s floor under R5 regulator + Zubarev dressing
#   name:              A_s_floor_5conv
#   value:             5.09e-13
#   unit:              dimensionless (scalar power amplitude)
#   session-of-origin: S83 (pre-registered), S84 (final pinning via W5-59)
#   source-document:   sessions/archive/session-84/session-84-w5-workingpaper.md §W5-59
#                      (FLOOR-CONDITIONED-ON-BRANCH)
#   derivation-pin:    computations/session-84/s84_w5_floor_conditioned_on_branch.py
#                      (pending-W5-59 — placeholder; orchestrator re-pins
#                      upon W5-59 closure at Wave 5 wrap-up)
#   gate-id:           S84-FLOOR-CONDITIONED-ON-BRANCH
A_s_floor_5conv = 5.09e-13  # pending-W5-59 (orchestrator re-pins post-closure)

# b_LB_ratio — Leggett-vs-Bogoliubov partition floor (permanent across 5 OOM K)
#   name:              b_LB_ratio
#   value:             0.6027
#   unit:              dimensionless
#   session-of-origin: S83
#   source-document:   sessions/archive/session-83/session-83-w3-workingpaper.md §G39
#                      (LEGGETT-BOGOLIUBOV-PARTITION)
#   derivation-pin:    computations/session-83/s83_w3_g39_leggett_bogoliubov.py
#   gate-id:           S83-W3-G39-LEGGETT-BOGOLIUBOV-PARTITION
b_LB_ratio = 0.6027

# tau_GGE_K_unit — GGE relaxation time linear slope in K (span unit)
#   name:              tau_GGE_K_unit
#   value:             7.86e4
#   unit:              tau-units (M_KK^{-1} per unit K; dimensionless slope)
#   session-of-origin: S83
#   source-document:   sessions/archive/session-83/session-83-w3-workingpaper.md §G40
#                      (TAU-GGE-AT-K)
#   derivation-pin:    computations/session-83/s83_w3_g40_tau_gge_at_K.py
#   gate-id:           S83-W3-G40-TAU-GGE-AT-K
tau_GGE_K_unit = 7.86e4

# xi_ell_plateau — BCS coherence-length plateau value at K >= 10
#   name:              xi_ell_plateau
#   value:             0.135
#   unit:              dimensionless (xi_BCS / L_phonon ratio)
#   session-of-origin: S83
#   source-document:   sessions/archive/session-83/session-83-w3-workingpaper.md §G41
#                      (XI-BCS-VS-L-PHONON)
#   derivation-pin:    computations/session-83/s83_w3_g41_xi_bcs_vs_l_phonon_k_response.py
#   gate-id:           S83-W3-G41-XI-BCS-VS-L-PHONON
xi_ell_plateau = 0.135

# K_star — Lab 3He-B vs framework K-star (functional-form audit, x* = 1)
#   name:              K_star
#   value:             1.3130   (= coth(1))
#   unit:              dimensionless
#   session-of-origin: S84
#   source-document:   sessions/archive/session-84/session-84-w5-workingpaper.md §W5-58
#                      (K-STAR-LAB-FRAMEWORK-MATCH)
#   derivation-pin:    computations/session-84/s84_w5_k_star_lab_framework_match.py
#                      (pending-W5-58 — placeholder; orchestrator re-pins
#                      upon W5-58 closure at Wave 5 wrap-up)
#   gate-id:           S84-K-STAR-LAB-FRAMEWORK-MATCH
K_star = 1.3130  # pending-W5-58 (orchestrator re-pins post-closure; coth(1) anchor)

# ==============================================================================
#  SECTION E.B: BRANCH-IV / 2B path-(c) Spectral Diagnostics (S86-W4-1 P4 commit)
# ==============================================================================
# Landed by S86-BRANCH-IV-FORMULATION-COMMIT (W4-1 P4) per gen-physicist 9A §4.6
# + lizzi 9A §2.2. R_JE (single-tag formulation) is RETIRED in favor of two
# distance-tagged spectral diagnostics. Substrate framing: the eigenvalue
# spectrum of D_K reorganizes at the van-Hove fold (tau_fold = 0.190); R_JK
# and xi_E_GGE_inv ARE moments of D_K — spectral functionals OF the substrate,
# not external probes IN spacetime.
#
# Cross-cite: volovik-superfluid-universe-theorist for xi_E_GGE_inv 3He-B
# parent->child inheritance (per `.claude/agent-memory/transit-dynamics-
# theorist/project_3heb-inheritance.md` — correspondence is parent->child,
# not analogy).
#
# Retirement note (R_JE): The S85-2A epsilon-pivot / S85-2B BRANCH-IV-asymmetry
# audits identified single-name conflation between distance-1 and distance-2
# tags inside the prior R_JE formulation. The 2B path-(c) commit replaces R_JE
# with two distance-tagged diagnostics (R_JK at distance-2, xi_E_GGE_inv at
# distance-1). S85 W12-ELIM-1 PASS verdict provides the L_max-trajectory
# anchor; W12-ELIM-3 + W12-ELIM-6 FAILs document the conflation.
# -----------------------------------------------------------------------------

# R_JK — K-functional, distance-2 spectral diagnostic
#   name:              R_JK
#   value:             0.00803460529503449 (full float64; at L_max=10 canonical anchor)
#   unit:              dimensionless ratio (numerator M_KK^{-4}; denominator
#                      M_KK^{-2} * dimensionless => overall M_KK^{-2} when
#                      dimensions are restored; in the framework's M_KK-natural
#                      units the printed value is dimensionless)
#   session-of-origin: S86 (commit), formula source S85-2B-branch-iv-asymmetry
#   source-document:   sessions/framework/registry/branch-iv-canonical.md §2 (R_JK landing)
#                      sessions/session-plan/session-86-plan-w4.md §W4-1
#                      gen-physicist 9A §4.6 substitution chain
#   derivation-pin:    computations/session-86/s86_w4_p4_branch_iv_commit.py
#                      (anchor cache: computations/_shared/artifacts/
#                      s85_w12_elim1_D_K_Lmax_moments.npz)
#   gate-id:           S86-BRANCH-IV-FORMULATION-COMMIT (W4-1, 2B path-(c))
#   formula:           R_JK := (sigma_J · |Delta_BCS|^2) / (sigma_K · K_base)
#                            = (a_4 / a_2) · (|Delta_BCS|^2 / K_base)
#                      where sigma_J = a_4 = Tr[D_K^{-4}] / Vol_SU3
#                            sigma_K = a_2 = Tr[D_K^{-2}] / Vol_SU3
#                      L_max-INDEPENDENT prefactor: |Delta_BCS|^2 / K_base
#                                                 = 0.10591275829606715
#   distance-tag:      2 (Newton-constant slot a_2; ratio of distance-2 / distance-2
#                      moments times distance-0 factor)
#   substrate-IS-cite: R_JK IS the K-functional moment of D_K at distance-2
#                      (NOT "lives in the K-corridor"). The K-functional character
#                      chi_K is the corridor-localized weighting of the spectral
#                      action at K = K_corridor (= K_base = 2.035; per S82-W2-4-
#                      PS-SUBSTRATE-MATCHED-IC R3 multiplicity-weighted primary).
R_JK = 0.00803460529503449  # distance-2; S86-W4-1 P4 commit; S85-W12-ELIM-1 PASS anchor at L_max=10
                            # Full float64 precision per .claude/rules/epistemic-discipline.md
                            # §"Publication-Precision Pre-Registration"; pub_sig_figs = 15.
                            # Cross-check identity (loaded-vs-anchor): rel_tol = 1e-12.

# xi_E_GGE_inv — s=-1 spectral diagnostic on the GGE-projected D_K (distance-1)
#   name:              xi_E_GGE_inv
#   value:             13.642473425595973 (full float64; M_KK units)
#                      = N_pair_GGE * Delta_BCS / K_base
#                      = 59.8 * 0.4642547394830737 / 2.035
#   unit:              M_KK (inverse coherence length / energy scale; intensive)
#   session-of-origin: S86 (commit), formula source lizzi 9A §2.2
#   source-document:   sessions/framework/registry/branch-iv-canonical.md §3 (xi_E_GGE_inv landing)
#                      sessions/session-plan/session-86-plan-w4.md §W4-1
#                      lizzi 9A §2.2 (s=-1 Mellin-strip residue convention)
#   derivation-pin:    computations/session-86/s86_w4_p4_branch_iv_commit.py
#                      (anchor cache: computations/_shared/artifacts/
#                      s85_w12_elim1_D_K_Lmax_moments.npz)
#   gate-id:           S86-BRANCH-IV-FORMULATION-COMMIT (W4-1, 2B path-(c))
#   formula:           xi_E_GGE_inv := lim_{s -> -1} zeta_{D_K^(GGE)}(s)
#                      = (analytic continuation) Sum_n lambda_n^(GGE)
#                      where D_K^(GGE) is D_K projected to the 59.8-pair
#                      Parker-production sector per S38 GGE permanence theorem.
#                      Substrate-natural anchor: dominant contribution is
#                      59.8 pairs * Delta_BCS / K_base average eigenvalue
#                      = 59.8 * 0.4642547 / 2.035 = 13.640957
#   distance-tag:      1 (first non-trivial Mellin-strip residue below s=0)
#   3He-B inheritance: parent->child (NOT analogy) per project_3heb-inheritance.md.
#                      Lab template: 3He-B coherence-length-inverse spectroscopy
#                      (Volovik QFL Fig. 5.3) inherits to substrate as the s=-1
#                      diagnostic on the GGE relic. The 3He-B order parameter is
#                      the parent; the substrate's GGE-projected zeta residue is
#                      the child via the universality-class inheritance map.
#   substrate-IS-cite: xi_E_GGE_inv IS the s=-1 spectral residue moment OF the
#                      GGE-projected D_K (NOT a coherence length IN a vacuum).
#                      The GGE relic IS the substrate's residual coherence
#                      pattern post-fold; xi_E_GGE_inv is one moment of that
#                      pattern at the s=-1 Mellin slice.
xi_E_GGE_inv = 13.642473425595973  # distance-1; S86-W4-1 P4 commit; M_KK units; 3He-B parent inheritance
                                   # = 59.8 * Delta_BCS / K_base = 59.8 * 0.4642547394830737 / 2.035
                                   # Full float64 precision per .claude/rules/epistemic-discipline.md
                                   # §"Publication-Precision Pre-Registration"; pub_sig_figs = 15.

# D_EFF_CANONICAL_CONVENTION — convention pin for d_eff=8 anchor (S87-W1B-HK-3 audit)
#   name:              D_EFF_CANONICAL_CONVENTION
#   value:             "Conv-B-slope-on-bare-SU(3)-manifold-dim"
#   meaning:           The d_eff=8 anchor referenced in s28c_12d_axioms.py (and any
#                      downstream §VII.U / §VII.W cite) is canonical ONLY under
#                      Convention B (`d_eff = slope` of log N(λ) vs log λ) AND
#                      restricted to the BARE SU(3) Lie-group manifold dimension
#                      sub-axis — i.e., as the Riemannian-geometry / Lie-algebra
#                      theorem dim(SU(3)) = dim(su(3)) = 8. This is NOT the
#                      Jensen-deformed bulk-Weyl observable on (A_K, H, D_K).
#   session-of-origin: S87 (W1b-HK-3 post-execution audit)
#   source-document:   sessions/archive/session-87/session-87-results-workingpaper.md
#                      §W1b-3 "Post-execution d_eff convention audit (HK-3)"
#                      sessions/session-plan/session-87-plan-w1b.md (W1b-3 carry-fwd)
#   derivation-pin:    computations/session-87/s87_w1b_hk_3_d_eff_convention_audit.py
#                      (audit_sha256 = a6d97024586c4eae20d455856bc117b4d3b7417ef9d77ec52239abd9a85b5c9c)
#                      (content_sha256 = 398a136b9140c51df39cf9f5ba55e3b5e426e969d36912dd7e220a4d3d95ef89)
#   gate-id:           S87-W1B-HK-3-D-EFF-CONVENTION-AUDIT (PASS-canonical)
#   1-of-14 grid hit:  Of 14 (sub-axis × convention) cells scanned, EXACTLY ONE
#                      yields d_eff=8 substrate-faithful: bare-SU(3)-manifold-dim
#                      under Conv-B-slope. The Jensen-deformed bulk-Weyl Linf
#                      cell yields d_eff=10.122 (Conv-A) / 5.061 (Conv-B); each
#                      of 4 V_4-stratum cells (per S86 W-12 monodromy partition)
#                      yields d_eff in [9.87, 10.29] (Conv-A) / [4.93, 5.14] (Conv-B);
#                      none of these per-stratum or bulk cells lands at 8.
#   downstream-rule:   Any computation script citing d_eff=8 MUST consume this pin and
#                      attach the suffix "(under Conv-B-slope on bare-SU(3)-manifold-
#                      dim sub-axis; NOT Jensen-deformed bulk-Weyl)". Citations
#                      that conflate this with the bulk-Weyl substrate observable
#                      are FALSE under W1b-3 + W1b-HK-3.
#   substrate-IS-cite: The number 8 IS the real dimension of SU(3) as a Lie group
#                      (count of su(3) generators = 8); it is NOT the L→∞ Jensen-
#                      deformed bulk-Weyl exponent of D_K = M_Lie + Ω_LC (which
#                      extrapolates to 5.061 under Conv-B, 10.122 under Conv-A).
D_EFF_CANONICAL_CONVENTION = "Conv-B-slope-on-bare-SU(3)-manifold-dim"  # S87-W1B-HK-3 PASS-canonical
                                                                       # 1 substrate-faithful hit of 14 grid cells
                                                                       # Closes Jensen-deformed bulk-Weyl d_eff=8 anchor

# ==============================================================================
#  SECTION F: PROVENANCE Dictionary
# ==============================================================================


# === SECTION F — S87 ===

# --- S87 W10-2 (Bulletin #4 PERMANENT-WALL) ---
rho_inf_FW = -0.8103647022669215  # rho_inf full float64 from S87 W10-2 simple-pole fit on L=8..12 cache; L2-IRRATIONAL FERMIONIC-SIGNED-RESIDUE per Bulletin #4 closure; canonical pin -0.810369 (6 sig figs); presentation precision 10 sig figs; rho_inf approx -0.8104 (4-sig-fig presentation only). (S87)

# === S92 W4-6 — VAR_A SUBSTRATE-NATURAL CANONICAL PIN ===
Var_a_canonical = 7.2824902250e-06  # Var_a(n_a^GGE) substrate-natural canonical at L_max=10 on (A_K, H_K, D_K) at tau_fold=0.190; convention=w5b47_raw (max(p,q)<=L_max filter, m_a=dim_pq, zero-modes excluded); fastest convergence to Weyl-dim extrapolated-to-infinity asymptotic limit v_inf=6.4631783294e-06 (12.68% deviation at L_max=10 vs 96.22% volovik vs 637.26% vdd); promoted from S92 W4-CF-W4-4-EMPIRICAL-ANCHOR-RECONCILIATION; deprecated conventions vdd/volovik tagged DIAGNOSTIC per cross-pillar-bridge-anatomy.md §"Level-3 anchor singleness sub-clause" SUGGESTION K=1 (S91 W4 CF-S92-W5-1-F). (S92)
Var_a_canonical_diagnostic_vdd = 4.7650356226e-05  # DIAGNOSTIC (deprecated): vdd p+q<=L_max convention; triangular under-sampling of d=4 Weyl-law tail. (S92)
Var_a_canonical_diagnostic_volovik = 1.2681760000e-05  # DIAGNOSTIC (deprecated): volovik p+q<=L_max convention with m_a=dim_pq DOUBLE-weights dim_pq (abs_evals already carries 16*dim_pq replication). (S92)
Var_a_asymptotic_v_inf = 6.4631783294e-06  # Weyl-dim L_max->inf asymptotic limit per registry §VII.U.2 Corner II Level-2 envelope L^{-4} (S88 §W5b-47). (S92)

# === S116 W8-2 — §VII.AV.STATE-PROJ Corner-IV K-window log-derivative gap-IR anchor (promotion from literal) ===
L_emp_VII_AV_STATE_PROJ = -7.046336474406761  # L_emp = d^2 ln Var_a(|v_a(K)|^2)/d(ln K)^2 at substrate-distance-2 pole s=4 on BdG sub-algebra M_2(C) subset A_K; gap-IR substrate anchor (8-mode s52 Bogoliubov occupation variance, horizon-crossing K-window [0.95,1.05]K_h, 5-point central FD; the gap |Delta_a| supplies the intrinsic IR scale, NO UV cutoff needed). Origin S87 W2-3 GGE-Bog-occupation-variance; recomputed bit-precision (rel_diff 0.0000%) at S89-CORNER-IV-K-WINDOW-LOG-DERIVATIVE-RECOMPUTE; STAGE-3-PERMANENT at permanent-results-registry §VII.AV.STATE-PROJ (S93 W3, Stage-2 PASS-AND S93 W3-6). Units M_KK^2. Promoted from literal -7.046336474406761 hardcoded in s89/s91/s93 (3+ scripts) per math-scripts.md Canonical Write-Order; comparison anchor for FWD-C2 PROXY-REFINEMENT discharge. (S116 W8-2)

# === S92 W7-6 — alpha_HH1_per_pole_FW_s{s} sub-keyed pin family ===
# Wodzicki/Connes d=4 substrate-physics prediction α_HH^1(s) = 2*(s - 2)
# on M_3(ℂ) ⊂ A_K Wedderburn block at tau_fold = 0.19; per-pole exponent
# table for substrate-distance N ∈ {0, 1, 2, 3, 4} at d=4. Step 2
# sub-keyed canonical-write-order promotion per math-scripts.md.
alpha_HH1_per_pole_FW_s2 = 0  # HH^1 cocycle norm asymptotic envelope α_HH^1(s=2) = 0 (substrate-distance-0 pole; HKR-image trivial envelope at zeroth order); Wodzicki/Connes d=4 prediction α = 2*(s-2); substrate-distance N=0; S92-W7-CF-W9-10-B canonical-write-order Step 2 sub-keyed promotion. (S92)
alpha_HH1_per_pole_FW_s3 = 2  # HH^1 cocycle norm asymptotic envelope α_HH^1(s=3) = 2 (substrate-distance-1 pole; matches S91 §W9-10 first-extraction direction); Wodzicki/Connes d=4 prediction α = 2*(s-2); substrate-distance N=1; S92-W7-CF-W9-10-B canonical-write-order Step 2 sub-keyed promotion. (S92)
alpha_HH1_per_pole_FW_s4 = 4  # HH^1 cocycle norm asymptotic envelope α_HH^1(s=4) = 4 (substrate-distance-2 pole; §W7-5 first-extraction anchor (central pole)); Wodzicki/Connes d=4 prediction α = 2*(s-2); substrate-distance N=2; S92-W7-CF-W9-10-B canonical-write-order Step 2 sub-keyed promotion. (S92)
alpha_HH1_per_pole_FW_s5 = 6  # HH^1 cocycle norm asymptotic envelope α_HH^1(s=5) = 6 (substrate-distance-3 pole; §VII.BB STAGE-1-CANDIDATE per S91 §W9-13); Wodzicki/Connes d=4 prediction α = 2*(s-2); substrate-distance N=3; S92-W7-CF-W9-10-B canonical-write-order Step 2 sub-keyed promotion. (S92)
alpha_HH1_per_pole_FW_s6 = 8  # HH^1 cocycle norm asymptotic envelope α_HH^1(s=6) = 8 (substrate-distance-4 pole; future gate at S93+); Wodzicki/Connes d=4 prediction α = 2*(s-2); substrate-distance N=4; S92-W7-CF-W9-10-B canonical-write-order Step 2 sub-keyed promotion. (S92)

PROVENANCE = {
    # Section A — PDG/CODATA
    "M_Pl_reduced":      {"session": "S7",  "source": "CODATA 2018", "gate": None, "superseded": False},
    "M_Pl_unreduced":    {"session": "S7",  "source": "CODATA 2018", "gate": None, "superseded": False},
    "alpha_em_MZ_inv":   {"session": "S42", "source": "PDG 2024",    "gate": None, "superseded": False},
    "M_Z":               {"session": "S42", "source": "PDG 2024",    "gate": None, "superseded": False},
    "rho_Lambda_obs":    {"session": "S42", "source": "Planck 2018", "gate": None, "superseded": False},
    "m_e":               {"session": "S98", "source": "PDG 2024 (CODATA 0.51099895000 MeV)", "gate": "S98-W3-1-YUKAWA-EPS-LX-BETWEEN-GEN", "superseded": False,
                          "note": "Electron mass 5.10998950e-4 GeV. Added for the charged-lepton Yukawa hierarchy band; PDG pole-mass scale (consistent with m_mu), NOT the RGE-run m_tau=2.062 modulus-mass M_KK-units value."},

    # Section B — Geometric
    "tau_fold":          {"session": "S12/S42", "source": "s42_constants_snapshot.npz", "gate": "CONST-FREEZE-42", "superseded": False},
    "Vol_SU3_Haar":      {"session": "S44",     "source": "s44_constants_corrected.py", "gate": None, "superseded": False,
                          "note": "Corrected from 8880.93 to 1349.74 (Weyl integration formula)"},
    "Vol_SU3_WRONG":     {"session": "S42",     "source": "s42_constants_snapshot.py",  "gate": None, "superseded": True},
    "M_KK_gravity":      {"session": "S42", "source": "s42_constants_snapshot.npz", "gate": "CONST-FREEZE-42", "superseded": False},
    "M_KK_kerner":       {"session": "S42", "source": "s42_constants_snapshot.npz", "gate": "CONST-FREEZE-42", "superseded": False},

    # Section C — BCS
    "E_cond_ED_8mode":   {"session": "S36", "source": "s36_multisector_ed.npz (config_4_E_cond)", "gate": "ED-CONV-36", "superseded": False},
    "E_cond_ED_5mode":   {"session": "S35", "source": "s36_multisector_ed.npz (config_1_E_cond)", "gate": "ED-CORRECTED-35", "superseded": True,
                          "note": "5-mode result, superseded by 8-mode convergence study"},
    "E_cond_GL":         {"session": "S37", "source": "GL functional",                            "gate": None, "superseded": False,
                          "note": "Different quantity — GL free energy, not ED ground state"},
    "E_cond":            {"session": "S36", "source": "alias for E_cond_ED_8mode",                "gate": "ED-CONV-36", "superseded": False},
    "M_max_thouless":    {"session": "S35", "source": "RPA-BCS-35",                               "gate": "RPA-BCS-35", "superseded": False},
    "S_inst":            {"session": "S37/S38", "source": "s37_instanton_mc.npz (S_inst_D)",      "gate": None, "superseded": False},

    # Section C — BCS (continued)
    "Delta_0_GL":        {"session": "S37", "source": "s37_instanton_mc.npz",           "gate": None, "superseded": False,
                          "note": "GL order parameter amplitude, NOT the BCS excitation gap"},
    "Delta_0_OES":       {"session": "S37", "source": "s37_pair_susceptibility.npz",    "gate": None, "superseded": False,
                          "note": "Pair-addition gap from 256-state ED — the canonical BCS gap"},
    "Delta_BCS":         {"session": "S70", "source": "alias for Delta_0_OES",          "gate": "BCS-GAP-CANONICAL-70", "superseded": False,
                          "R_protected": True,
                          "note": "R-PROTECTED: Canonical BCS gap (M_KK units = dimensionless ratio). "
                                  "Eigenvalue ratio, bypasses Seeley-DeWitt. STRUCTURAL, drift 0.00% (S74 W4-F #19). "
                                  "Supersedes hardcoded 0.52 (was eps_fold[3], not a gap)"},
    "Delta_B1":          {"session": "S53", "source": "s53_acoustic_efold_output.txt + s52_casimir_josephson_output.txt", "gate": None, "superseded": False,
                          "note": "B1 band GL gap (M_KK) at tau_fold=0.19. Multiplicity-weighted total-gap identity Delta_total=sqrt(Delta_B1^2+4*Delta_B2^2+3*Delta_B3_s53^2). B1/B2 labels interchanged between s53 outputs; squared-sum identity is label-order-invariant. Added S95 W3-3 (BACK-REACTION-CLOSURE ρ_relic assembly)."},
    "Delta_B2":          {"session": "S53", "source": "s53_acoustic_efold_output.txt + s52_casimir_josephson_output.txt", "gate": None, "superseded": False,
                          "note": "B2 band GL gap (M_KK) at tau_fold=0.19. Fock multiplicity 4. Added S95 W3-3."},
    "Delta_B3_s53":      {"session": "S53", "source": "s53_acoustic_efold_output.txt + s52_casimir_josephson_output.txt", "gate": None, "superseded": False,
                          "note": "B3 band GL gap (M_KK, un-doubled) at tau_fold=0.19; Delta_B3(=0.176, S38) is the 2*Delta_B3_s53 doubled-gap convention. Fock multiplicity 3. Added S95 W3-3."},
    "xi_BCS":            {"session": "S37", "source": "s37_instanton_mc.npz",           "gate": None, "superseded": False},
    "xi_GL":             {"session": "S37", "source": "s37_instanton_mc.npz",           "gate": None, "superseded": False},
    "a_GL":              {"session": "S37", "source": "s37_instanton_mc.npz",           "gate": None, "superseded": False},
    "b_GL":              {"session": "S37", "source": "s37_instanton_mc.npz",           "gate": None, "superseded": False},
    "omega_PV":          {"session": "S37", "source": "s37_pair_susceptibility.npz",    "gate": None, "superseded": False},
    "Gamma_Langer_BCS":  {"session": "S38", "source": "s38_attempt_freq.npz",           "gate": None, "superseded": False},
    "Kapitza_ratio":     {"session": "S38", "source": "s38_attempt_freq.npz",           "gate": None, "superseded": False},

    # Section D — Spectral action
    # Scheme tags added S78 W3-L (Lizzi, SDW/zeta dictionary audit).
    # The canonical a_0/a_2/a_4 values are the "half zeta" S73B project
    # convention: a_n = 0.5 * sum_k d_k / lam_k^n, computed at L_max=3. This
    # is a ZETA-scheme assignment (half of zeta_D at integer argument), NOT
    # Seeley-DeWitt (Tr sqrt(D^2)) and NOT HK-Taylor (Tr exp(-tD^2)) moments.
    # Per plan Sec 0.2: a_n^{HK} = (1/16pi^2) * a_n^{SDW} for d=4.
    # Conflating schemes produces up to 9 OOM errors (S77 W2-K permanent).
    "a0_fold":           {"session": "S42", "source": "s42_constants_snapshot.npz", "gate": "CONST-FREEZE-42", "superseded": False,
                          "scheme_tag": "zeta", "branch_scope": "per-branch", "L_max_tag": "L_max=3",
                          "note": "zeta-scheme half mode-count 0.5*sum_n d_n at tau=0.19, S73B convention. "
                                  "Added S78 W3-L scheme_tag (was ambiguous in 6+ downstream scripts)."},
    "a2_fold":           {"session": "S42", "source": "s42_constants_snapshot.npz", "gate": "CONST-FREEZE-42", "superseded": False,
                          "scheme_tag": "zeta", "branch_scope": "per-branch", "L_max_tag": "L_max=3",
                          "note": "zeta-scheme half zeta_D(1): 0.5*sum_n d_n/lam_n^2. "
                                  "Added S78 W3-L scheme_tag."},
    "a4_fold":           {"session": "S42", "source": "s42_constants_snapshot.npz", "gate": "CONST-FREEZE-42", "superseded": False,
                          "scheme_tag": "zeta", "branch_scope": "per-branch", "L_max_tag": "L_max=3",
                          "note": "zeta-scheme half zeta_D(2): 0.5*sum_n d_n/lam_n^4. "
                                  "Added S78 W3-L scheme_tag."},
    "R_protected_fold":  {"session": "S73B/S74", "source": "s74_r_protected_addition.npz",
                          "gate": "R-PROTECTED-FOLD-ADDITION-74", "superseded": False,
                          "R_protected": True,
                          "scheme_tag": "SCHEME-INDEPENDENT", "branch_scope": "per-branch", "L_max_tag": "L_max=3",
                          "note": "R-PROTECTED PER-BRANCH: R_1 = a_0*a_4/a_2^2 at fold. "
                                  "Vol(K) cancels per Baptista B2. L_max drift 0.34% (S74 W4-F #2). "
                                  "branch_scope=per-branch MEANS: R_1 has the same value in any single "
                                  "spectral functional (zeta-only or SDW-only or f*-only) when computed "
                                  "on the same spectrum + truncation. It is NOT cross-branch; treating "
                                  "R_1 as a conversion factor BETWEEN schemes is Level-3 SD (plan Sec 0.4)."},
    "Lizzi_signature":   {"session": "S74", "source": "derived from R_protected_fold",
                          "gate": "N16-RATIO-OF-RATIOS-PROTECTED-74", "superseded": False,
                          "R_protected": True,
                          "scheme_tag": "SCHEME-INDEPENDENT", "branch_scope": "per-branch", "L_max_tag": "L_max=3",
                          "note": "R-PROTECTED PER-BRANCH: (m_H/v_EW)^2 * (Lambda/M_Pl^2) = R_1 identically. "
                                  "Two unprotected pieces combine into one protected ratio-of-ratios. "
                                  "Lizzi zeta-spectral-action signature (S74 W4-F #11). "
                                  "branch_scope=per-branch: same caveat as R_protected_fold."},
    "S_fold":            {"session": "S42", "source": "s42_gradient_stiffness.npz", "gate": None, "superseded": False},
    "M_ATDHFB":          {"session": "S40", "source": "s42_gradient_stiffness.npz", "gate": None, "superseded": False},
    "G_DeWitt":          {"session": "S42", "source": "s42_gradient_stiffness.npz", "gate": None, "superseded": False},

    # Section D — Transit
    "H_fold":            {"session": "S38", "source": "s38_kz_defects.npz",         "gate": None, "superseded": False},
    "v_terminal":        {"session": "S38", "source": "s38_kz_defects.npz",         "gate": None, "superseded": False},

    # Section E — Fabric
    "N_cells":           {"session": "S42", "source": "s42_fabric_wz.py (giant_voronoi)", "gate": None, "superseded": False},
    "rho_B2_per_mode":   {"session": "S37", "source": "s37_instanton_action.npz",   "gate": None, "superseded": False},
    "E_B1":              {"session": "S38", "source": "s38_attempt_freq.npz",        "gate": None, "superseded": False},
    "E_B2_mean":         {"session": "S38", "source": "s38_attempt_freq.npz",        "gate": None, "superseded": False},
    "E_B3_mean":         {"session": "S38", "source": "s38_attempt_freq.npz",        "gate": None, "superseded": False},

    # Section E2 — Phonon & Structural (R-protected)
    "c_Gold_over_c_fabric": {"session": "S52", "source": "s52_gl_josephson.npz",   "gate": "GL-JOSEPHSON-52", "superseded": False,
                             "R_protected": True,
                             "scheme_tag": "SCHEME-INDEPENDENT", "branch_scope": "per-branch", "L_max_tag": "n/a",
                             "note": "R-PROTECTED PER-BRANCH: Sound speed ratio c_Gold/c_fabric = 0.00436. "
                                     "Eigenvalue gradient ratio, bypasses Seeley-DeWitt expansion. "
                                     "STRUCTURAL, drift 0.00% (S74 W4-F #20). "
                                     "Added S78 W3-L scheme_tag / branch_scope."},

    # Phonon sound-speed scalar provenance (added session-x W9 orchestrator; W4 C-Causality survey
    # flagged these three as "No PROVENANCE entry". Sources verified, not inferred: c_fabric + c_BLV
    # from their canonical_constants.py inline comments; c_Gold from knowledge-graph eq_10122.)
    "c_fabric":          {"session": "S42", "source": "s42_gradient_stiffness", "gate": None, "superseded": False,
                          "note": "Substrate sound speed (velocity scale, NOT a momentum cutoff); spectral-action modulus; "
                                  "229x hierarchy numerator (c_fabric/c_Gold = 229.48). PROVENANCE added session-x W9 from S42 inline comment + S86 W0b-1 docstring."},
    "c_Gold":            {"session": "S52", "source": "s52_gl_josephson.npz", "gate": "GL-JOSEPHSON-52", "superseded": False,
                          "note": "Goldstone sound speed (M_KK units) from the S52 GL-Josephson phonon spectrum; "
                                  "229x hierarchy denominator (c_Gold/c_fabric = c_Gold_over_c_fabric = 0.00436). "
                                  "PROVENANCE added session-x W9; confirmed via knowledge-graph eq_10122 (GL-JOSEPHSON-52)."},
    "c_BLV":             {"session": "S64", "source": "s64_sound_speed", "gate": None, "superseded": False,
                          "note": "Brillouin-Landau-Vortex fabric sound speed; 3He-B four-speed hierarchy inheritance; "
                                  "scalar c_s for post-fold GGE. PROVENANCE added session-x W9 from S64 inline comment."},

    # Layer-2 BdG branch speeds (post-transit phononic group velocities on g_M; M_KK units).
    # Added S94 W5-3 per the substrate-first-provenance flag (Phononic-C-Causality.md §3.3/§4.3
    # tabulated W1-A/W2-A; used by the S94-BAO-PEAK-BRANCH per-branch Layer-1/Layer-2 split gate).
    "c_B1":              {"session": "S52", "source": "Phononic-C-Causality.md §3.3/§4.3 (W1-A/W2-A; S52 GL-JOSEPHSON-52 spectral content)", "gate": "GL-JOSEPHSON-52", "superseded": False,
                          "note": "B1 singlet acoustic-scalar Layer-2 branch speed (M_KK units); BAO channel at k~0.043 Mpc^-1; "
                                  "dominant acoustic feature. v_g <= c_Gold=0.915 envelope. Added S94 W5-3."},
    "c_B2":              {"session": "S52", "source": "Phononic-C-Causality.md §3.3/§4.3 (W1-A/W2-A; S52 GL-JOSEPHSON-52 spectral content)", "gate": "GL-JOSEPHSON-52", "superseded": False,
                          "note": "B2 flat-optical (quartet) Layer-2 branch speed (M_KK units); van Hove plateau / flat band. "
                                  "v_g <= c_Gold=0.915 envelope. Added S94 W5-3."},
    "c_B3":              {"session": "S52", "source": "Phononic-C-Causality.md §3.3/§4.3 (W1-A/W2-A; S52 GL-JOSEPHSON-52 spectral content)", "gate": "GL-JOSEPHSON-52", "superseded": False,
                          "note": "B3 dispersive-optical (triplet) Layer-2 branch speed (M_KK units); intermediate branch. "
                                  "v_g <= c_Gold=0.915 envelope. Added S94 W5-3."},
    "c_L":               {"session": "S66", "source": "Phononic-C-Causality.md §4.3 (W4-L; S66 Leggett DM)", "gate": None, "superseded": False,
                          "note": "Leggett-branch Layer-2 sound speed (M_KK units; = c_Leggett); gap-massed inter-band coherence "
                                  "(Leggett DM). v_g <= c_Gold=0.915 envelope. Added S94 W5-3."},

    # Section C — BCS gap tag (added S78 W3-L)
    # Delta_BCS = Delta_0_OES / M_KK is an EIGENVALUE ratio from 256-state ED;
    # it bypasses the Seeley-DeWitt/HK-Taylor expansion entirely and is therefore
    # scheme-independent per-branch by construction (no functional f chosen).
    "Delta_BCS_tag":     {"session": "S78", "source": "S78 W3-L audit", "gate": "SDW-ZETA-DICT-78",
                          "superseded": False, "R_protected": True,
                          "scheme_tag": "SCHEME-INDEPENDENT", "branch_scope": "per-branch", "L_max_tag": "n/a",
                          "note": "Pseudo-entry documenting Delta_BCS (=Delta_0_OES) scheme status. "
                                  "The eigenvalue ratio bypasses SA expansion; branch_scope=per-branch "
                                  "(same 256-state ED spectrum used regardless of functional)."},

    # Section D — Mellin moments of f* (added S78 W2-D, tagged S78 W3-L)
    "mellin_f_star_f0":  {"session": "S78", "source": "s78_f_conv_anomaly.npz",
                          "gate": "S78-W2-D-F-CONV-ANOMALY", "superseded": False,
                          "scheme_tag": "f*", "branch_scope": "per-branch", "L_max_tag": "n/a",
                          "note": "f*(0) = 0.088 for f*(x)=0.912sqrt(x)+0.088exp(-x). "
                                  "Contrast with f_0_sharp=1/2 (anomaly-forced, Andrianov-Lizzi)."},
    "mellin_f_star_f2":  {"session": "S78", "source": "s78_f_conv_anomaly.npz",
                          "gate": "S78-W2-D-F-CONV-ANOMALY", "superseded": False,
                          "scheme_tag": "f*", "branch_scope": "per-branch", "L_max_tag": "n/a (X_MAX=50 regulator)",
                          "note": "int_0^50 f*(x) dx = 214.97; X_max=50 regulator (sqrt-part absorbed "
                                  "into SDW Lambda^2 cutoff in the separate SDW-scheme branch)."},
    "mellin_f_star_f4":  {"session": "S78", "source": "s78_f_conv_anomaly.npz",
                          "gate": "S78-W2-D-F-CONV-ANOMALY", "superseded": False,
                          "scheme_tag": "f*", "branch_scope": "per-branch", "L_max_tag": "n/a (X_MAX=50 regulator)",
                          "note": "int_0^50 x*f*(x) dx = 6446.64; same X_max=50 regulator."},

    # Section D — Sharp-cutoff / anomaly moments (Andrianov-Lizzi forced values)
    "f_0_sharp":         {"session": "S78", "source": "Andrianov-Lizzi arXiv:1103.0478",
                          "gate": "S78-W2-D-F-CONV-ANOMALY", "superseded": False,
                          "scheme_tag": "anomaly", "branch_scope": "per-branch", "L_max_tag": "n/a",
                          "note": "f_0 = 1/2 FORCED by fermionic-anomaly cancellation under sharp cutoff. "
                                  "Used EXCLUSIVELY for W2-D anomaly branch; NOT interchangeable with "
                                  "mellin_f_star_f0 (different functional)."},
    "f_2_default":       {"session": "S62", "source": "S62 W1 Gaussian-cutoff",
                          "gate": None, "superseded": False,
                          "scheme_tag": "Gaussian-cutoff", "branch_scope": "per-branch", "L_max_tag": "n/a",
                          "note": "Gaussian-cutoff f_2 = 2.34 (scheme-dependent). NOT f* and NOT SDW. "
                                  "Use mellin_f_star_f2 for f*-branch computations."},
    "f_4_default":       {"session": "S62", "source": "S62 Gaussian-cutoff",
                          "gate": None, "superseded": False,
                          "scheme_tag": "Gaussian-cutoff", "branch_scope": "per-branch", "L_max_tag": "n/a",
                          "note": "Gaussian-cutoff f_4 = 0.558 (scheme-dependent)."},

    # Section E3 — S81 PRU-promotion pass (observational + framework constants
    # lifted from script locals during the PRU(a) → 0 audit)
    "ns_framework":      {"session": "S81", "source": "S65 BCS+one-loop, S68 W2-B, S69 W3-D",
                          "gate": None, "superseded": True, "superseded_by": "n_s_framework",
                          "note": "SUPERSEDED (S88 W-15 W15-V.2): the bit-exact Route-B pin "
                                  "n_s_FW_exact=Fraction(9561,10000) explicitly supersedes the scheme-dependent "
                                  "floats 0.9567/0.9557/0.9595. Canonical framework n_s is now n_s_framework=0.9561. "
                                  "Value 0.9595 (S65 BCS+one-loop route) retained on disk for historical cites. "
                                  "Flag corrected during knowledge-base spot-check 2026-05-29."},
    "n_s_framework":     {"session": "S85", "source": "S84 T6 constant-epsilon gauge-invariant spectral geometry; S85 W9-3; bit-exact Route-B pin n_s_FW_exact=Fraction(9561,10000) at S88 W-15 W15-V.2",
                          "gate": None, "superseded": False,
                          "note": "CANONICAL framework n_s at CMB pivot = 0.9561 (distinct from planck_ns=0.9649 "
                                  "observational). 9561^2=91412721 perfect square => n_s^2-1 = -0.08587279 EXACT "
                                  "(= alpha_s_substrate_distance_1). Supersedes ns_framework=0.9595 (S88 W-15). "
                                  "Provenance backfilled during knowledge-base spot-check 2026-05-29 "
                                  "(was 'No PROVENANCE entry')."},
    "ns_framework_err":  {"session": "S81", "source": "deterministic from spectral triple",
                          "gate": None, "superseded": False,
                          "note": "Zero — framework prediction has no stochastic component."},
    "k_pivot_planck":    {"session": "S81", "source": "Planck 2018 CMB convention",
                          "gate": None, "superseded": False,
                          "note": "CMB pivot scale 0.05 Mpc^-1, Planck 2018."},
    "N_pivot":           {"session": "S83", "source": "S82 W-1 #10 (CMB pivot e-fold count)",
                          "gate": "S83-N-PIVOT-CS-CANONICALIZATION",
                          "superseded": False,
                          "note": "N_pivot^substrate = 55 + ln(c/c_s) = 55 + 9.08 = 64.08. "
                                  "c_s correction lifts N_pivot from LCDM (55) to substrate (64.08) "
                                  "because horizon crossing on the substrate is bounded by the "
                                  "phononic sound speed c_s = 1.137e-4, not by c. Used in "
                                  "s83_w2_g7 (CC7-DYNAMICAL) and s83_w2_g16 (UNIFIED-AS-79) "
                                  "with # (local) tags; promoted to canonical here per plan §W3-G61."},
    "z_eq_planck":       {"session": "S81", "source": "Planck 2018",
                          "gate": None, "superseded": False,
                          "note": "Matter-radiation equality redshift z_eq = 3387."},
    "r_GOE_canonical":   {"session": "S81", "source": "Wigner surmise, random matrix theory",
                          "gate": None, "superseded": False,
                          "note": "Gaussian Orthogonal Ensemble mean r-statistic = 0.5307."},
    "r_POISSON_canonical": {"session": "S81", "source": "Wigner surmise, random matrix theory",
                          "gate": None, "superseded": False,
                          "note": "Poisson (integrable) mean r-statistic = 0.3863."},

    # SECTION A — S84
    "sigma_r_BK_2026": {"session": "S84", "source": "s84_w4_bicep_keck_2026_pre_register.py (Ade+ 2025 preprint forecast)", "gate": "S84-BICEP-KECK-2026-PRE-REGISTER", "superseded": False},

    # SECTION A — S83
    "r_CMB_framework": {"session": "S83", "source": "s83_w3_g46_tensor_transfer.npz (G46 PASS)", "gate": "S83-W3-G46-TENSOR-TRANSFER", "superseded": False},

    # SECTION E — S83
    "sigma_alpha_SKA1": {"session": "S83", "source": "s83_w3_g45_ska_alpha_fnl.npz", "gate": "S84-SKA-1-PHASE-1-ALPHA-FRAMEWORK-SNR", "superseded": False},

    # SECTION E — S83
    "sigma_alpha_SKA2": {"session": "S83", "source": "s83_w3_g45_ska_alpha_fnl.npz", "gate": "S84-ALPHA-F-NL-FRAMEWORK-PRED", "superseded": False},

    # Section E.K — S84 W5-60 K-corridor canonical promotion (7-field provenance)
    "K_R3":             {"session": "S82", "source": "sessions/archive/session-82/session-82-w2-workingpaper.md §W2-4 (s82_w2_4_ps_substrate_matched_ic.py)",
                          "gate": "S82-W2-4-PS-SUBSTRATE-MATCHED-IC", "superseded": False,
                          "unit": "dimensionless",
                          "note": "K-corridor multiplicity-weighted primary (3/3/2 band-weight). Promoted W5-60."},
    "K_match_need":     {"session": "S83", "source": "sessions/archive/session-83/session-83-w3-workingpaper.md §G38 (s83_w3_g38_k_matching_5_conventions.py)",
                          "gate": "S83-W3-G38-K-MATCHING-5-CONVENTIONS", "superseded": False,
                          "unit": "dimensionless",
                          "note": "Minimum K needed for Planck-match (positivity WALL). Promoted W5-60."},
    "A_s_floor_5conv":  {"session": "S83/S84", "source": "sessions/archive/session-84/session-84-w5-workingpaper.md §W5-59 (s84_w5_floor_conditioned_on_branch.py)",
                          "gate": "S84-FLOOR-CONDITIONED-ON-BRANCH", "superseded": False,
                          "unit": "dimensionless (scalar power amplitude)",
                          "note": "Branch-B A_s floor under R5 + Zubarev. Placeholder 5.09e-13 pending W5-59 closure; orchestrator re-pins at Wave-5 wrap-up."},
    "b_LB_ratio":       {"session": "S83", "source": "sessions/archive/session-83/session-83-w3-workingpaper.md §G39 (s83_w3_g39_leggett_bogoliubov.py)",
                          "gate": "S83-W3-G39-LEGGETT-BOGOLIUBOV-PARTITION", "superseded": False,
                          "unit": "dimensionless",
                          "note": "Leggett-vs-Bogoliubov partition floor, permanent across 5 OOM K. Promoted W5-60."},
    "tau_GGE_K_unit":   {"session": "S83", "source": "sessions/archive/session-83/session-83-w3-workingpaper.md §G40 (s83_w3_g40_tau_gge_at_K.py)",
                          "gate": "S83-W3-G40-TAU-GGE-AT-K", "superseded": False,
                          "unit": "tau-units (M_KK^{-1} per unit K)",
                          "note": "GGE relaxation-time linear slope in K; span 7.86e4 tau-units. Promoted W5-60."},
    "xi_ell_plateau":   {"session": "S83", "source": "sessions/archive/session-83/session-83-w3-workingpaper.md §G41 (s83_w3_g41_xi_bcs_vs_l_phonon_k_response.py)",
                          "gate": "S83-W3-G41-XI-BCS-VS-L-PHONON", "superseded": False,
                          "unit": "dimensionless",
                          "note": "BCS coherence-length ratio plateau at K >= 10. Promoted W5-60."},
    "K_star":           {"session": "S84", "source": "sessions/archive/session-84/session-84-w5-workingpaper.md §W5-58 (s84_w5_k_star_lab_framework_match.py)",
                          "gate": "S84-K-STAR-LAB-FRAMEWORK-MATCH", "superseded": False,
                          "unit": "dimensionless",
                          "note": "Lab 3He-B vs framework K-star; functional-form audit anchors x* = 1 -> coth(1) = 1.3130. Placeholder pending W5-58 closure; orchestrator re-pins at Wave-5 wrap-up."},

    # SECTION E — S84
    "beta_s": {"session": "S84", "source": "S84-W6-BETA-S-CMB-S4-PREREG", "gate": "S85-BETA-S-CMB-S4-PREREG", "superseded": False},

    # SECTION E — S85
    "sigma_beta_s_CMB_S4": {"session": "S85", "source": "CMB-S4 Science Book v2 2022 Table 6.1 (sigma(n_run,run)); Abazajian 2016 arXiv:1610.02743 consistency", "gate": "S85-BETA-S-CMB-S4-PREREG", "superseded": False},

    # SECTION E.B — S86 W4-1 P4 BRANCH-IV / 2B path-(c) commit
    "R_JK":             {"session": "S86", "source": "sessions/framework/registry/branch-iv-canonical.md §2 (formula source: gen-physicist 9A §4.6; anchor cache: computations/_shared/artifacts/s85_w12_elim1_D_K_Lmax_moments.npz, L_max=10)",
                          "gate": "S86-BRANCH-IV-FORMULATION-COMMIT", "superseded": False,
                          "unit": "dimensionless ratio (M_KK^{-2} when SI dimensions restored; Newton-constant slot)",
                          "note": "K-functional, distance-2 spectral diagnostic. R_JK := (sigma_J * |Delta_BCS|^2)/(sigma_K * K_base) = (a_4/a_2)*(|Delta_BCS|^2/K_base). Replaces R_JE (retired in 2B path-(c) commit). L_max-INDEPENDENT prefactor |Delta_BCS|^2/K_base = 0.10591275829606715. Substrate framing: R_JK IS the K-functional moment of D_K at distance-2."},
    "xi_E_GGE_inv":     {"session": "S86", "source": "sessions/framework/registry/branch-iv-canonical.md §3 (formula source: lizzi 9A §2.2; substrate-natural anchor: 59.8 * Delta_BCS / K_base)",
                          "gate": "S86-BRANCH-IV-FORMULATION-COMMIT", "superseded": False,
                          "unit": "M_KK (inverse coherence length / energy scale; intensive)",
                          "note": "s=-1 spectral diagnostic on GGE-projected D_K, distance-1. xi_E_GGE_inv := lim_{s->-1} zeta_{D_K^(GGE)}(s) = Sum_n lambda_n^(GGE). 3He-B parent->child inheritance per project_3heb-inheritance.md (NOT analogy). Cross-cited to volovik-superfluid-universe-theorist. Replaces R_JE (retired in 2B path-(c) commit). Substrate framing: xi_E_GGE_inv IS the s=-1 spectral residue moment OF the GGE-projected D_K."},

    # SECTION E — S86
    "b_DK": {"session": "S86", "source": "s86_w6_3_weyl_rescaling_weak.py + AC-2010 §V Eq. (5.3)", "gate": "S86-WEYL-RESCALING-IMMUNIZATION-WEAK-FORM", "superseded": False},

    # SECTION E — S86
    "HP0_content_dim": {"session": "S86", "source": "S82 W2-3 + S85 W2-7 §VII.P parity-blindness adjudication", "gate": "S86-VII-P-V2-PARITY-EXTENSION", "superseded": False},

    # SECTION E — S86
    "dE_He_A_lambda_6": {"session": "S86", "source": "s85_w8_su3_op_lab_predictions.py", "gate": "S85-W8-4-SU3-OP-LAB-PREDICTIONS", "superseded": False},

    # SECTION E — S86
    "dE_FeSe_lambda_7": {"session": "S86", "source": "s85_w8_su3_op_lab_predictions.py", "gate": "S85-W8-4-SU3-OP-LAB-PREDICTIONS", "superseded": False},

    # SECTION E — S86
    "dE_173Yb_lambda_8": {"session": "S86", "source": "s85_w8_su3_op_lab_predictions.py", "gate": "S85-W8-4-SU3-OP-LAB-PREDICTIONS", "superseded": False},

    # SECTION E — S86
    "dE_FeSe_lambda_6": {"session": "S86", "source": "s85_w8_su3_op_lab_predictions.py", "gate": "S85-W8-4-SU3-OP-LAB-PREDICTIONS", "superseded": False},

    # SECTION E — S86
    "dE_173Yb_lambda_6": {"session": "S86", "source": "s85_w8_su3_op_lab_predictions.py", "gate": "S85-W8-4-SU3-OP-LAB-PREDICTIONS", "superseded": False},

    # SECTION E — S86
    "dE_He_A_lambda_7": {"session": "S86", "source": "s85_w8_su3_op_lab_predictions.py", "gate": "S85-W8-4-SU3-OP-LAB-PREDICTIONS", "superseded": False},

    # SECTION E — S86
    "dE_173Yb_lambda_7": {"session": "S86", "source": "s85_w8_su3_op_lab_predictions.py", "gate": "S85-W8-4-SU3-OP-LAB-PREDICTIONS", "superseded": False},

    # SECTION E — S86
    "r_PathH": {"session": "S86", "source": "sessions/archive/session-86/session-86-1a-s6-mack.md (mack synthesis); primary source sessions/archive/session-85/workshops/s85-w2-as-band-authority.md OQ-7 line 1882 + Wrap-Up line 1894 + carry-forward item 7 line 1949; algebraic ingredients r_CMB_framework (S83 W3-G46) + H_BASELINE/H_TD (S84 W1a-1 / S80 W1-2)", "gate": "S86-1A-S6-RPATHH-PRIMARY-ANCHORING", "superseded": False},

    # SECTION E — S86
    "r_PathH_published": {"session": "S86", "source": "S85 W2 OQ-7 line 1882 (workshop-quoted 4-sig-fig form); plan-w12 §7 boundary table; W14 §Row #2 r line 145; per Publication-Precision Pre-Registration rule (.claude/rules/epistemic-discipline.md)", "gate": "S86-1A-S6-RPATHH-PRIMARY-ANCHORING", "superseded": False},

    # SECTION E — S86
    "alpha_s_canon_Fairbairn": {"session": "S86", "source": "Fairbairn 2025 arXiv:2511.01612 Table IV ACT+P+SPT+eBOSS row; W-2 housekeeping CANON-1", "gate": "S86-W2-CANON-EXTRACT", "superseded": False},

    # SECTION E — S86
    "alpha_s_canon_FairbairnSPT": {"session": "S86", "source": "Fairbairn 2025 arXiv:2511.01612 Table IV ACT+P+SPT row; W-2 CANON-2", "gate": "S86-W2-CANON-EXTRACT", "superseded": False},

    # SECTION E — S86
    "alpha_s_canon_FairbairnACTP": {"session": "S86", "source": "Fairbairn 2025 arXiv:2511.01612 Table IV ACT+P row; W-2 CANON-3", "gate": "S86-W2-CANON-EXTRACT", "superseded": False},

    # SECTION E — S86
    "ns_canon_Fairbairn": {"session": "S86", "source": "Fairbairn 2025 arXiv:2511.01612 Table IV ACT+P+SPT+eBOSS row; W-2 CANON-4", "gate": "S86-W2-CANON-EXTRACT", "superseded": False},

    # SECTION E — S86
    "beta_s_canon_Fairbairn": {"session": "S86", "source": "Fairbairn 2025 arXiv:2511.01612 Table IV running-of-running row; W-2 CANON-5", "gate": "S86-W2-CANON-EXTRACT", "superseded": False},

    # SECTION E — S86
    "alpha_s_canon_RogersPoulin": {"session": "S86", "source": "Rogers-Poulin Planck+eBOSS, cited via Fairbairn 2025 ref [7]; W-2 CANON-6", "gate": "S86-W2-CANON-EXTRACT", "superseded": False},

    # SECTION E — S86
    "substrate_residue_floor_alpha_s": {"session": "S86", "source": "W-2 R3-FINAL Verdict row 4; gamma_pivot * 2u/(1+u); W-2 CANON-7", "gate": "S86-W2-CANON-EXTRACT", "superseded": False},

    # SECTION E — S86
    "u_pivot": {"session": "S86", "source": "W-2 V1 Step 3 calibration from canonical n_s = 9649/10000; W-2 CANON-8", "gate": "S86-W2-CANON-EXTRACT", "superseded": False},

    # SECTION E — S86
    "gamma_pivot": {"session": "S86", "source": "W-2 C1 / R2-A DISSENT + R3-B EMERGENCE (i); W-2 CANON-11", "gate": "S86-W2-CANON-EXTRACT", "superseded": False},

    # SECTION E — S86
    "w_optical_over_acoustic_pivot": {"session": "S86", "source": "W-2 Volovik Q2.2/Q3.1 + R2-B EMERGENCE (ii); W-2 CANON-12", "gate": "S86-W2-CANON-EXTRACT", "superseded": False},

    # SECTION E — S86
    "Omega_GW_Companion_null": {"session": "S86", "source": "W-3 R2-B Dissent #2; W13-2 Omega verdict; per UD-5 promote", "gate": "S86-W3-CANON-EXTRACT", "superseded": False},

    # SECTION E — S86
    "sigma_HypB": {"session": "S86", "source": "W-3 R2-B Convergence #2 Sage QQ verification; W-3 CAN-8", "gate": "S86-W3-CANON-EXTRACT", "superseded": False},

    # SECTION E — S86
    "sigma_naive": {"session": "S86", "source": "W-3 R2-B Convergence #2; W-3 CAN-8", "gate": "S86-W3-CANON-EXTRACT", "superseded": False},

    # SECTION E — S86
    "sigma_band_low": {"session": "S86", "source": "W-3 R3-A Convergence #1; W-3 CAN-8", "gate": "S86-W3-CANON-EXTRACT", "superseded": False},

    # SECTION E — S86
    "sigma_band_high": {"session": "S86", "source": "W-3 R3-A Convergence #1; W-3 CAN-8", "gate": "S86-W3-CANON-EXTRACT", "superseded": False},

    # SECTION E — S86
    "reduction_ratio": {"session": "S86", "source": "W-3 R3-B Convergence #1 lock-in; W-3 CAN-8", "gate": "S86-W3-CANON-EXTRACT", "superseded": False},
    "c_sub_baseline":    {"session": "S78 W2-E", "source": "S78 W2-E central pin; S85 W2-as-band-authority.md line 224; S86 W1c-8 (C29) fed n_s_of_c_sub anchor", "gate": None, "superseded": False,
                          "note": "Substrate Mellin-weight baseline c_sub=2.238 = M_Pl_eff(k_pivot)^2/M_Pl_eff(0)^2 (eq_166717). PROVENANCE-dict entry backfilled at S116 plan-freeze; value + inline provenance pre-existing at canonical_constants.py:2546, flagged by the S116-W8 FWD-C1 grounding SOURCE-RECON advisory. reduction_ratio (16577/31705) is the Sage-exact 1/c_sub replacement. gate=None is DELIBERATE per the file convention for central/observational/derived pins (epistemic-discipline.md Source-Reconciliation Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY: a central pin with derived consumers and no single producing gate). Origin S78 W2-E; S86 W1c-8 C29 is a downstream CONSUMER feeding the n_s_of_c_sub anchor, NOT the producer; explicit central-pin tag confirmed S116-W8 A8.3 (mack-cosmic-bridge)."},

    # SECTION E — S86
    "OOM_split_AC_regulator_class": {"session": "S86", "source": "W-3 R2-B Dissent #2 Sage-verified; per UD-5 promote", "gate": "S86-W3-CANON-EXTRACT", "superseded": False},

    # SECTION B — S86
    "R_universal_HP1_strict_F4": {"session": "S86", "source": "W-5 V4 substitution chain Step 2; W-5 CANONICAL-2; per UD-6 promote", "gate": "S86-W5-CANON-EXTRACT", "superseded": False},

    # SECTION B — S86
    "cocycle_norm_phi67": {"session": "S86", "source": "W-5 C2 substrate-magnitude annotation; W-5 CANONICAL-3; per UD-6 promote", "gate": "S86-W5-CANON-EXTRACT", "superseded": False},

    # SECTION B — S86
    "cocycle_norm_phi88": {"session": "S86", "source": "W-5 C2 substrate-magnitude annotation; W-5 CANONICAL-4; per UD-6 promote", "gate": "S86-W5-CANON-EXTRACT", "superseded": False},

    # SECTION B — S86
    "substrate_cocycle_ratio_67_88": {"session": "S86", "source": "W-5 R2-B Convergence #3 + R2-A EMERGENCE #2; W-5 CANONICAL-5", "gate": "S86-W5-CANON-EXTRACT", "superseded": False},

    # SECTION D — S86
    "L_envelope_d4_Lmax10": {"session": "S86", "source": "W-5 R2-B DISSENT #1 substitution chain Step 3; W-5 CANONICAL-6", "gate": "S86-W5-CANON-EXTRACT", "superseded": False},

    # SECTION E — S86
    "xi_sq_0_crit_SR_LO_breakdown_N1": {"session": "S86", "source": "W-9 transit T1 brentq; W-9 CANON-3", "gate": "S86-W9-CANON-EXTRACT", "superseded": False},

    # SECTION E — S86
    "xi_sq_0_lin_crit_SR_LO_N55": {"session": "S86", "source": "W-9 transit Q-L2.1+T2; W-9 CANON-4", "gate": "S86-W9-CANON-EXTRACT", "superseded": False},

    # SECTION E — S86
    "xi_sq_0_SR_LO_valid_crit_N55": {"session": "S86", "source": "W-9 transit Q-L2.1+T2; W-9 CANON-5", "gate": "S86-W9-CANON-EXTRACT", "superseded": False},

    # SECTION E — S86
    "rho_inf_zubarev_canonical": {"session": "S86", "source": "W-10 CM-1995 audit Bulletin #4 PERMANENT-WALL; L=8..12 simple-pole fit R^2=0.999945", "gate": "S86-W10-CANON-EXTRACT", "superseded": False},

    # SECTION E — S86
    "rho_inf_zubarev_deep_ir": {"session": "S86", "source": "W-10 CM-1995 audit Level 2 band-estimate at Lambda_Z = 0.05; per UD-7 R2-B answer (register rho_inf canonical, NOT lam_min directly)", "gate": "S86-W10-CANON-EXTRACT", "superseded": False},

    # SECTION D — S86
    "L_J_Laplacian_dressing_kappa": {"session": "S86", "source": "W-4 s78_fnl_coherence.npz S78 W3-F PATH-B; W-4 CANONICAL-4", "gate": "S86-W4-CANON-EXTRACT", "superseded": False},

    # SECTION E — S86
    "f_NL_total_SKA1": {"session": "S86", "source": "W-4 R2-B DISSENT #3 + R3-A CONVERGENCE #4; per UD-12 (a) prediction frozen + architecture-revision-exempt", "gate": "S86-W4-CANON-EXTRACT", "superseded": False},

    # SECTION D — S86
    "M_zeta_s3": {"session": "S86", "source": "W-9 §L1 + W4-2 P5 inheritance + T-CR3.1 Python verify; W-9 CANON-1", "gate": "S86-W9-CANON-EXTRACT", "superseded": False},

    # SECTION E — S87
    "lambda_min_max_ratio_FW": {"session": "S87", "source": "S87-STRICT-LAMBDA-RATIO-EXTRACTION", "gate": "S87-STRICT-LAMBDA-RATIO-EXTRACTION", "superseded": False},
    "rho_inf_FW": {"session": "S87", "source": "S87-BULLETIN-#4-IRRATIONAL-RHO-PERMANENT-WALL-LANDING", "gate": "S87-BULLETIN-#4-IRRATIONAL-RHO-PERMANENT-WALL-LANDING", "superseded": False},

    # SECTION C — S66
    "CC_OOM": {"session": "S66", "source": "s66_w1a_dilution_cc.npz", "gate": "S66-W1-A-DILUTION-CC", "superseded": False},

    # SECTION E — S88
    "chi_A_FW": {"session": "S88", "source": "s88_w3b_chi_a_chiral_correction_verification.npz", "gate": "S88-CHI-A-CHIRAL-CORRECTION-VERIFICATION", "superseded": False},

    # SECTION B — S88
    "tau_pivot": {"session": "S88", "source": "S88-TAU-PIVOT-CANONICAL-CONSTANT-PROMOTION (W5a-39); substrate-first lineage from S86 W4 P5 sector_2_k_invariant.py:215 'tau_pivot is NOT in canonical_constants; we use tau_fold as the canonical slice'", "gate": "S88-TAU-PIVOT-CANONICAL-CONSTANT-PROMOTION", "superseded": False},

    # SECTION E — S88
    "f_NL_FW_S82_equilateral": {"session": "S88", "source": "s82_w3_4_gge_fnl_channel.py", "gate": "S88-CF-27-PIN-RE-PIN-AT-PLAN-FREEZE", "superseded": False},

    # SECTION E — S88
    "f_NL_FW_S67_folded": {"session": "S88", "source": "s67_gge_bispectrum.py", "gate": "S88-CF-27-PIN-RE-PIN-AT-PLAN-FREEZE", "superseded": False},

    # SECTION E — S88
    "f_NL_FW_S85_W9_3_analytic_template": {"session": "S88", "source": "s85_w9_folded_triangle_21cm_shape.py", "gate": "S88-CF-27-PIN-RE-PIN-AT-PLAN-FREEZE", "superseded": False},

    # SECTION E — S88
    "V2_weight_FW_C": {"session": "S88", "source": "s88_w9_102_v2_weight_pre_registration.npz", "gate": "S88-V2-WEIGHT-RE-PRE-REGISTRATION", "superseded": False},

    # SECTION E — S88
    "V2_weight_FW_H": {"session": "S88", "source": "s88_w9_102_v2_weight_pre_registration.npz", "gate": "S88-V2-WEIGHT-RE-PRE-REGISTRATION", "superseded": False},

    # SECTION E — S88
    "V2_weight_FW_M3": {"session": "S88", "source": "s88_w9_102_v2_weight_pre_registration.npz", "gate": "S88-V2-WEIGHT-RE-PRE-REGISTRATION", "superseded": False},

    # SECTION E — S88
    "V2_weight_FW_sum": {"session": "S88", "source": "s88_w9_102_v2_weight_pre_registration.npz", "gate": "S88-V2-WEIGHT-RE-PRE-REGISTRATION", "superseded": False},

    # SECTION E — S88
    "a_0_FW_zeta": {"session": "S88", "source": "S64-results-workingpaper.md + lizzi-signature-observable.md", "gate": "S88-A-N-FW-CANONICALIZATION", "superseded": False},

    # SECTION E — S88
    "a_2_FW_zeta": {"session": "S88", "source": "S42 spectral zeta sum + S46 a_2 split (s61_heat_kernel_a2_log.txt; s86-mellin-cone-repair-or-no-go.md)", "gate": "S88-A-N-FW-CANONICALIZATION", "superseded": False},

    # SECTION E — S87 W8 publication-precision floor closures (added 2026-05-10 per
    # user authorization for PROVENANCE hygiene; constants defined at lines 1557-1558)
    "max_pair_ratio_A_5_FW": {
        "session": "S87 W8-2",
        "source": "s87_w8_w4_2_re_run_under_a_4.npz; full float64 = 9.240438549812e-01; was_cutoff_sqrt_extremal_in_A5=False ⇒ A_5=A_4 at full float64 (S87 W8-2 PROMOTED FIX-IN-SESSION per feedback_fix-in-session-never-defer.md)",
        "gate": "S87-W8-2-MAX-PAIR-RATIO-A-5-RE-RUN-UNDER-A-4",
        "superseded": False,
        "note": "Class-8.3 publication-precision floor closure: full float64 anchor for A_5 max-pair-ratio extremum at (zeta, Zubarev). Promoted to canonical so downstream verifiers compare full-float64 against full-float64 (previous 6-sig-fig 9.240439e-01 caused structural false-FAIL at rel_tol < 1e-6)."
    },

    "gv_canonical_difference_FW": {
        "session": "S87 W8-8",
        "source": "s84_w10a_115_gv_explicit.npz; full float64 = -40579.1500479506; W-11 §3 anchor; reaffirmed regulator-INDEPENDENT across A_5_extended at S87 W8-8 (PROMOTED FIX-IN-SESSION)",
        "gate": "S87-W8-8-GV-CANONICAL-DIFFERENCE-LANDED",
        "superseded": False,
        "note": "Class-8.3 publication-precision floor closure: full float64 anchor for GV-Heitsch invariant difference on (C_H, C_epsH) parity-twin pair at canonical regulator. Per-regulator deviation across A_5_extended = ZERO (composite=INFO at publication-precision floor only). Cross-link: regulator-pin-discipline.md §'Class-(c) PIN-DRIFT-FROM-STALE-SOURCE — W-11 Calibration Corpus Extension'."
    },

    # SECTION E — S89
    "xi_KZ_FW": {"session": "S89", "source": "S89-XI-KZ-SUBSTRATE-NATURAL-DERIVATION-FROM-T1-ATLAS", "gate": None, "superseded": False},

    # SECTION E — S89
    "kappa_2_substrate_FW": {"session": "S89", "source": "S89-HIGHER-ORDER-RESOLVENT-EXPANSION-O-TAU2-KAPPA2", "gate": None, "superseded": False},

    # SECTION E — S89
    "tau_max_HK5_regime_FW": {"session": "S89", "source": "s89_w3_hk5_regime_tau_max_bound_derivation.npz", "gate": "S89-HK-5-REGIME-OF-VALIDITY-TAU-MAX-BOUND-DERIVATION", "superseded": False},

    # SECTION E — S90 (CF-46 + CF-47 + W1-10 in-session promotion, 2026-05-16)
    "c_W12_deficit_FW_PRIMARY_ConvB": {"session": "S90", "source": "CF-46 PASS; W-12 §IV.1 R1∧R2 joint-closure pathway; Conv-B HK-5 substrate-first canonical paired with cache anchor residual_B = 2.615119e-05 at tau_fold² = 0.0361; OOM distinction 1.463 from kappa_2_substrate_FW = 0.021018 per Class-(d) PIN-DERIVATIVE remediation Conv-A→Conv-B", "gate": "S90-CF-46 audit_sha256=de3c690f465931e1d34d1f3266c13445e0b4b6e477f4cc914abe9022596b809e", "superseded": False},

    "tau_max_HK5_regime_FW_asymptotic_limit_FW": {"session": "S90", "source": "CF-47 PASS; L_max → ∞ asymptotic limit by direct closed-form identity lim 0.05^{1/(L+1)} = 0.05^0 = 1; analytic pole of HK-5(τ) = 5/(1−τ/(5π)) at τ = 5π; structural-saturation theorem analog of S87 W11-3 Friedrich-Bär saturation at substrate-distance-5 pole", "gate": "S90-CF-47 audit_sha256=5c7cbe480ded228cdd7d0879a23d4c07d335c21f8921ddbbcdb8d3e85ed0410b", "superseded": False},

    "lambda_unit_canonical": {"session": "S90", "source": "W1-10 INFO; cache lambda units = dimensionless_M_KK_natural per S90 W5-7 anchor-5 unit-consistency audit Reading-C resolution; promoted in-session 2026-05-16 per feedback_fix-in-session-never-defer.md", "gate": "S90-W5-7-ANCHOR-5-UNIT-CONSISTENCY-AUDIT", "superseded": False},
    "Var_a_canonical":   {"session": "S92", "source": "s92_w4_6_w4_4_empirical_anchor_reconciliation.npz", "gate": "S92-W4-CF-W4-4-EMPIRICAL-ANCHOR-RECONCILIATION", "superseded": False, "audit_sha256": "e393b51fd223868a74020a2c3dc63453e53db088f5b06f7980d97f4d8464a807", "note": "Substrate-natural Var_a(n_a^GGE) at L_max=10; max(p,q)<=L_max filter; m_a=dim_pq; zero-modes excluded; 12.68% deviation from v_inf=6.4631783294e-06"},
    "Var_a_canonical_diagnostic_vdd":   {"session": "S92", "source": "s91_w4_vii_u_2_var_a_stage_2_axis_a_vdd.npz", "gate": "S92-W4-CF-W4-4-EMPIRICAL-ANCHOR-RECONCILIATION", "superseded": True, "note": "DIAGNOSTIC: vdd p+q<=L_max convention; triangular under-sampling of d=4 Weyl-law tail."},
    "Var_a_canonical_diagnostic_volovik":   {"session": "S92", "source": "s91_w4_vii_u_2_var_a_stage_2_axis_b_volovik.npz", "gate": "S92-W4-CF-W4-4-EMPIRICAL-ANCHOR-RECONCILIATION", "superseded": True, "note": "DIAGNOSTIC: volovik p+q<=L_max convention; m_a=dim_pq DOUBLE-weights dim_pq."},
    "Var_a_asymptotic_v_inf":   {"session": "S92", "source": "registry §VII.U.2 Corner II Level-2 envelope L^{-4}", "gate": "S88-W5B-47", "superseded": False, "note": "Weyl-dim L_max->inf asymptotic limit for Var_a(n_a^GGE)"},
    "L_emp_VII_AV_STATE_PROJ":   {"session": "S116", "source": "s89_w5_a25_corner_iv_k_window_log_derivative_recompute.npz (origin S87 W2-3 GGE-Bog-occupation-variance); permanent-results-registry §VII.AV.STATE-PROJ STAGE-3-PERMANENT (S93 W3, Stage-2 PASS-AND S93 W3-6)", "gate": "S116-W8-FWDC2-LANDING", "superseded": False, "note": "Corner-IV K-window log-derivative gap-IR anchor d^2 ln Var_a(|v_a(K)|^2)/d(ln K)^2 at substrate-distance-2 pole s=4 on BdG sub-algebra M_2(C); promoted from literal -7.046336474406761 used in s89/s91/s93; comparison anchor for the FWD-C2 PROXY-REFINEMENT discharge (s116_w8_fwdc2_full_bdg_proxy_refinement.py)"},

    # === S92 LQG × phonon-first narrow-path workshop (no compute gate; canonical pin via L2 derivation) ===
    "ALPHA_BRIDGE_REQUIRED_FW":   {"session": "S92", "source": "S92 LQG × phonon-first workshop L2 substitution chain lines 116-125 (α_bridge = γ_BH / 49.34 = 0.2375 / 49.34 = 4.81e-3)", "gate": None, "superseded": False, "note": "Required value of α_bridge for §IX.7 narrow-path Regime I closure (γ_emergent matches γ_BH in SU(2)-convention). Substrate-side prior favors Regime II (α_bridge ∼ O(1), structural failure); Q2 (Paper 03 §VII) confirms γ does NOT admit cutoff running so Regime II has no recovery mechanism. See sessions/framework/correspondence/lqg-narrow-path-bridge-class.md for the bridge-map class identification (HKR with -Cheeger-Simons scheme suffix)."},
    "SCALE_BRIDGE_PREFACTOR_FW":   {"session": "S92", "source": "S92 LQG × phonon-first workshop L2 dimensional pre-factor line 122: (M_Pl_red/M_KK)²/(4√3π) = (2.435e18/7.4287e16)²/(4√3π) = (1.074e3)/(21.77) = 49.34", "gate": None, "superseded": False, "note": "Dimensional pre-factor in narrow-path scale-bridge equation γ_emergent = α_bridge · SCALE_BRIDGE_PREFACTOR_FW. Pure arithmetic from M_Pl_reduced and M_KK_gravity pins; no new substrate physics."},
    "GAMMA_BH_SU2_CONVENTION_LQG":   {"session": "S92", "source": "Paper 03 §VII (researchers/Loop-Quantum-Gravity/index.md:779); SU(2)-convention BH-entropy pin for the Immirzi γ", "gate": None, "superseded": False, "note": "External pin from loop-quantum-gravity corpus. U(1) Chern-Simons convention value (Papers 02, 03) is γ_0 ≈ 0.127 (factor ~1.87 difference from SU(2)-convention 0.2375). Convention-tag MUST be stated when citing γ; mixing conventions across cross-framework comparisons is a Class-(c) PIN-DRIFT-FROM-STALE-SOURCE risk."},
    "alpha_HH1_per_pole_FW_s2":   {"session": "S92", "source": "S92-W7-CF-W9-10-B-pole-s2", "gate": "S92-W7-CF-W9-10-B-SUBSTRATE-IS-ALPHA-S-PER-POLE-EXPONENT-TABLE-M3C", "superseded": False, "audit_sha256": "3fdc912e90a4c1a9e94ea4fdbd4033f54e8447b0aed347c98c1107a47b8818ee", "note": "HH^1 cocycle norm asymptotic envelope at substrate-distance-0 pole s=2; Wodzicki/Connes d=4 prediction α_HH^1(s=2) = 0; per-pole exponent table {0,2,4,6,8} for s ∈ {2,3,4,5,6} on M_3(ℂ) ⊂ A_K at tau_fold=0.19"},
    "alpha_HH1_per_pole_FW_s3":   {"session": "S92", "source": "S92-W7-CF-W9-10-B-pole-s3", "gate": "S92-W7-CF-W9-10-B-SUBSTRATE-IS-ALPHA-S-PER-POLE-EXPONENT-TABLE-M3C", "superseded": False, "audit_sha256": "3fdc912e90a4c1a9e94ea4fdbd4033f54e8447b0aed347c98c1107a47b8818ee", "note": "HH^1 cocycle norm asymptotic envelope at substrate-distance-1 pole s=3; Wodzicki/Connes d=4 prediction α_HH^1(s=3) = 2; per-pole exponent table {0,2,4,6,8} for s ∈ {2,3,4,5,6} on M_3(ℂ) ⊂ A_K at tau_fold=0.19"},
    "alpha_HH1_per_pole_FW_s4":   {"session": "S92", "source": "S92-W7-CF-W9-10-B-pole-s4", "gate": "S92-W7-CF-W9-10-B-SUBSTRATE-IS-ALPHA-S-PER-POLE-EXPONENT-TABLE-M3C", "superseded": False, "audit_sha256": "3fdc912e90a4c1a9e94ea4fdbd4033f54e8447b0aed347c98c1107a47b8818ee", "note": "HH^1 cocycle norm asymptotic envelope at substrate-distance-2 pole s=4; Wodzicki/Connes d=4 prediction α_HH^1(s=4) = 4; per-pole exponent table {0,2,4,6,8} for s ∈ {2,3,4,5,6} on M_3(ℂ) ⊂ A_K at tau_fold=0.19"},
    "alpha_HH1_per_pole_FW_s5":   {"session": "S92", "source": "S92-W7-CF-W9-10-B-pole-s5", "gate": "S92-W7-CF-W9-10-B-SUBSTRATE-IS-ALPHA-S-PER-POLE-EXPONENT-TABLE-M3C", "superseded": False, "audit_sha256": "3fdc912e90a4c1a9e94ea4fdbd4033f54e8447b0aed347c98c1107a47b8818ee", "note": "HH^1 cocycle norm asymptotic envelope at substrate-distance-3 pole s=5; Wodzicki/Connes d=4 prediction α_HH^1(s=5) = 6; per-pole exponent table {0,2,4,6,8} for s ∈ {2,3,4,5,6} on M_3(ℂ) ⊂ A_K at tau_fold=0.19"},
    "alpha_HH1_per_pole_FW_s6":   {"session": "S92", "source": "S92-W7-CF-W9-10-B-pole-s6", "gate": "S92-W7-CF-W9-10-B-SUBSTRATE-IS-ALPHA-S-PER-POLE-EXPONENT-TABLE-M3C", "superseded": False, "audit_sha256": "3fdc912e90a4c1a9e94ea4fdbd4033f54e8447b0aed347c98c1107a47b8818ee", "note": "HH^1 cocycle norm asymptotic envelope at substrate-distance-4 pole s=6; Wodzicki/Connes d=4 prediction α_HH^1(s=6) = 8; per-pole exponent table {0,2,4,6,8} for s ∈ {2,3,4,5,6} on M_3(ℂ) ⊂ A_K at tau_fold=0.19"},

    # PDG — S92
    "g_star_BS_T_H_FW": {"session": "S92", "source": "S92-W8-5", "gate": "S92-W8-CF-S92-T1-6-RETRY-PHASE-WEIGHT-REFINED", "superseded": False},

    # SECTION E — S92
    "T_H_FW": {"session": "S92", "source": "S92-W8-CF-S92-T1-7-CF39-SUBSTANTIVE-RETRY", "gate": "S92-W8-CF-S92-T1-7-CF39-SUBSTANTIVE-RETRY", "superseded": False},

    # SECTION E — S92
    "A_horizon_FW": {"session": "S92", "source": "S92-W8-CF-S92-T1-7-CF39-SUBSTANTIVE-RETRY", "gate": "S92-W8-CF-S92-T1-7-CF39-SUBSTANTIVE-RETRY", "superseded": False},

    # SECTION E — S92
    "L_H_canonical_FW": {"session": "S92", "source": "S92-W8-CF-S92-T1-7-CF39-SUBSTANTIVE-RETRY", "gate": "S92-W8-CF-S92-T1-7-CF39-SUBSTANTIVE-RETRY", "superseded": False},

    # SECTION E — S92
    "Var_a_canonical_L_inf_FW": {"session": "S92", "source": "s92_w8_2_multiplicity_convention_adjudication_workshop.npz", "gate": "S92-W8-CF-W8-CONSOLIDATED-2-MULTIPLICITY-CONVENTION-ADJUDICATION-WORKSHOP", "superseded": False},

    # SECTION E — S92
    "xi_k_zeta_window_canonical_FW": {"session": "S92", "source": "s92_w9_7_xi_k_substrate_natural_canonical_derivation.npz; substrate-natural xi_k(zeta-window) = Gamma(k+1)/Gamma(1+k/2)^2 derived from CM-1995 §III.4 Mellin-residue zeta-window evaluator on A_K = C+H+M_3(C); value pinned at k=2 (a_2 Einstein-Hilbert gravitational slot; xi_2 = 2 EXACT pi-free rational). Closed form is L_max-INDEPENDENT. LOCKED-NORM L_k = xi_k * w_k^zeta = 1 EXACT (Sage simplify_full, max|L_k-1|=2.22e-16 over k=0..8). Even-k slots = (2m)!/(m!)^2 = {1,2,6,20,70}; odd-k carry pi {4/pi,32/3pi,512/15pi,4096/35pi}. Replaces S91 §W9-5 consumption-layer misidentification per substrate-first-canonical-sourcing.md §(i).", "gate": "S92-W9-CF-LZ-S9-5-1-XI-K-SUBSTRATE-NATURAL-CANONICAL-DERIVATION audit_sha256=da7292a8df6ed3e769189056ee695204c4833ec436d83cb32c0057cf40714146", "superseded": False},

    # SECTION E — S92
    "vii_bb_element_5_empirical_anchor_FW": {"session": "S92", "source": "s92_w9_8_vii_bb_lmax_scan_degenerate_pole_first_extraction.npz", "gate": "S92-W9-CF-S92-VOLOVIK-S1-V1-LMAX-SCAN-DEGENERATE-POLE-VII-BB", "superseded": False},

    # SECTION E — S92
    "alpha_s_pivot_goldstone": {"session": "S92", "source": "s92-adhoc-alpha-s-transfer-map-identity.md (AH-TR-1 verdict, FC-1/FE-1)", "gate": "S92-AH-TR-1", "superseded": False},

    # SECTION E — S92
    "alpha_s_substrate_distance_1": {"session": "S92", "source": "s92-adhoc-alpha-s-transfer-map-identity.md (AH-TR-1 verdict, FC-2/FE-3); orig S88 W4 P5; S91 W9 5-regulator", "gate": "S92-AH-TR-1", "superseded": False},

    # SECTION E — S85 alpha_s trio SUPERSEDED by the S92 AH-TR-1 two-observable resolution
    # (knowledge-base spot-check 2026-05-29; user-adjudicated "mark superseded"). The trio
    # = n_s_canon^2-1 = planck_ns(0.9649)^2-1 = -0.06896799 is the S50-51 identity at the
    # OBSERVED Planck pivot — NEITHER substrate observable. Per phononic-framing.md the
    # CMB-pivot running is alpha_s_pivot_goldstone~=0 and the inside-BZ running is
    # alpha_s_substrate_distance_1=-0.08587279. Values retained for the framework-vs-Planck
    # tension landing (S85 W1c-5); downstream cites flagged stale.
    "alpha_s_inflation_framework": {"session": "S85", "source": "S50-51 identity alpha_s=n_s^2-1 at n_s_canon=planck_ns=0.9649 (W1c-2 commit)", "gate": "S85-W1c", "superseded": True, "superseded_by": "alpha_s_substrate_distance_1 + alpha_s_pivot_goldstone (S92 AH-TR-1)", "note": "SUPERSEDED by the S92 two-observable scale/channel resolution; identity@observed-pivot, NOT a substrate-IS observable. See phononic-framing.md single-label-conflation warning."},
    "alpha_s_framework_central": {"session": "S85", "source": "alias of alpha_s_inflation_framework (W1c-1 canonical handle for gate scripts)", "gate": "S85-W1c", "superseded": True, "superseded_by": "alpha_s_substrate_distance_1 + alpha_s_pivot_goldstone (S92 AH-TR-1)", "note": "SUPERSEDED by the S92 two-observable resolution; new gate scripts should consume alpha_s_substrate_distance_1 (inside-BZ) or alpha_s_pivot_goldstone (CMB pivot), not this handle."},
    "alpha_s_cmb_central": {"session": "S85", "source": "S50 identity alpha_s_CMB=n_s^2-1 at planck_ns=0.9649 (W13-2)", "gate": "S85-W13-2", "superseded": True, "superseded_by": "alpha_s_pivot_goldstone (S92 AH-TR-1)", "note": "SUPERSEDED + MIS-LABELED: per phononic-framing.md the CMB-pivot running is the Goldstone alpha_s_pivot_goldstone~=0, NOT -0.069. The -0.069 value is identity@observed-pivot, retained for the tension landing."},

    # SECTION E — S92
    "rho_FULL_CC_VII_AU_SAT_s3": {"session": "S92", "source": "S92-W1-CF-W9-8-2", "gate": "S92-W1-CF-W9-8-2-VII-AU-FULL-PHYSICAL-RE-EXTRACTION", "superseded": False},

    # SECTION E — S93 (W2-3 sub-class-keyed VII.AU.OP-PROJ analytic-shadow alpha promotion; canonical-write-order Step 2)
    "alpha_b_VII_AU_OP_PROJ_FW_LMAX14_EXTENSION": {"session": "S93", "source": "computations/session-92/s92_w5_vii_au_op_proj_lmax14_extension.npz (key alpha_b_L12_14, [12,14]_saturation_entry); S92-W5-CF-S92-W2-2-LMAX14-VII-AU-OP-PROJ-L-MAX-14-EXTENSION audit_sha256=395c63c829c11546766ee78e49609c571046e53b6ea5acb4c5844a61d62b64bf; W7a-74 PRIMARY FULL-physical CM-1995 SECTION-III.4 evaluator at substrate-distance-1 pole s=3; CLASS=FULL tier_pin=TIER-1; published precision 2.600027 (full-float64 round-trip 1e-15)", "gate": "S93-W2-3-VII-AU-OP-PROJ-CANONICAL-CONSTANTS-PROMOTION-SUB-CLASS-KEYED", "superseded": False},
    # alpha_canonical_..._ASYMPTOTIC value-line at canonical_constants.py:2312 (EXISTS since S91 W-5/W6; provenance ADDED here, closing the knowledge-MCP 'No PROVENANCE entry' gap). Layer-1 leading-term LIMIT (-3), NOT a measured value -> asymptotic-limit-derivation DEFERRED to CF-S94-W5-3 (INFO per plan §W2-3 INFO_meaning). CLASS=FULL (CM-1995 SECTION-III.4 simple-pole residue at substrate-distance-1 pole; substrate-IS regulator-invariant BY THEOREM at L->inf).
    "alpha_canonical_VII_AU_OP_PROJ_FW_ASYMPTOTIC": {"session": "S91", "source": "S91 W-5 workshop EMERGENCE table row 5 (sessions/archive/session-91/workshops/s91-w5-layer-functor-f-universal-envelope-scope-adjudication.md, lines 1320/1325-1326); CM-1995 SECTION-III.4 simple-pole residue on Cell I at substrate-distance-1 pole s=3; Layer-1 asymptotic anchor (REINDEXED Layer-Functor F K=2 SUGGESTION; K=1=VII.AF.1.OP-PROJ HP^1); CLASS=FULL; asymptotic-limit-derivation-DEFERRED-to-CF-S94-W5-3; provenance added S93-W2-3 (canonical-write-order Step 2)", "gate": "S93-W2-3-VII-AU-OP-PROJ-CANONICAL-CONSTANTS-PROMOTION-SUB-CLASS-KEYED", "superseded": False},
    # alpha_sample_..._PATHWAY_B_L15_22 value-line at canonical_constants.py:2319 (EXISTS since S91 W6-1; provenance ADDED here). Level-3 empirical sample at L-fit window [15,22]; original W6-1 reading CACHE-PROJECTION-SCHEMATIC (tier_pin=TIER-2, see value-line comment block) but REPRODUCED under the S92 W5-1 FULL-physical W7a-74 PRIMARY evaluator to relative deviation 8.80e-06 (npz key W6_1_anchor_reproduction_relative_deviation), level_pin=FULL tier_pin=TIER-1 -> promotion basis CLASS=FULL.
    "alpha_sample_VII_AU_OP_PROJ_FW_PATHWAY_B_L15_22": {"session": "S91", "source": "computations/session-91/s91_gate_verdicts.txt:128 S91-D4-ENVELOPE-EXTENDED-L_MAX-SUB-WINDOW audit_sha256=d54b26a970e43b6b5a63bee474a4a8baa80ed012546021c9dfe191cdb108fd8d (W6-1 pathway-b direct Connes-Karoubi pairing, L_fit in [15,22], full precision from NPZ); REPRODUCED under S92 W5-1 FULL-physical W7a-74 PRIMARY evaluator (audit_sha256=395c63c829c11546766ee78e49609c571046e53b6ea5acb4c5844a61d62b64bf, rel_dev 8.80e-06, level_pin=FULL tier_pin=TIER-1); provenance added S93-W2-3 (canonical-write-order Step 2)", "gate": "S93-W2-3-VII-AU-OP-PROJ-CANONICAL-CONSTANTS-PROMOTION-SUB-CLASS-KEYED", "superseded": False},

    # SECTION E — S93
    "n_PBH_FW_central": {"session": "S93", "source": "S91-CF41-VII-LANDING Step-1 (S91 W5-4) + S93-W4-1 Axis-A E2 re-emission PASS audit_sha256=2ab8bb1ecccb1bb7da8f85250b92ba4b25f2d7476253a4f5b2cb9703d79d29e8 + S92 W-4 JE5 PASS (Axis-B) + Eq.(2-prime) landed (S93 W4-4 audit_sha256=03d92b2ac13846ab) => VII.AX.OP-PROJ STAGE-3-PERMANENT eligible; Level-3 anchor T1.13 PASS audit_sha256=1dc0a3feb214d8b52ce7d70854b2510bbfa3df0e531e75dda1f8bf0cbbcb50ce (S91 W5-3 S91-CF41-UPPER-22.6-EXTENSION, s91_gate_verdicts.txt:96)", "gate": "S93-W4-5-CANONICAL-CONSTANTS-N-PBH-FW-CENTRAL-PROMOTION", "superseded": False},

    # SECTION E — SX
    "delta_tau_crit_neg": {"session": "SX", "source": "S88-W2-9-VII-AE-MODULI-SPACE-TAU-ASYMMETRY", "gate": None, "superseded": False},

    # SECTION E — SX
    "delta_tau_crit_pos": {"session": "SX", "source": "S88-W2-9-VII-AE-MODULI-SPACE-TAU-ASYMMETRY", "gate": None, "superseded": False, "note": "delta_tau_crit_pos=0.175 is the positive-side Jensen-moduli breakdown critical point (§VII.AE). S110 HK-DELTAPHI: do NOT conflate with Delta_phi/M_Pl=0.170 — that is a SEED-AUTHOR survey value (NOT canonical), a DIFFERENT observable (inflaton-field excursion, not a moduli-deformation critical point); the 3% adjacency (0.170 vs 0.175) is coincidence. The Delta_phi/M_Pl canonical re-pin is a separate §B compute (DELTA-PHI-CANONICAL-PIN, inv-9 HY8/§4)."},

    # SECTION E — S12 (phi_paasch PROVENANCE backfill, S110 W0 HK-PHI-PAASCH)
    "phi_paasch": {"session": "S12", "source": "phi_paasch found S12 (machine epsilon) — Paasch spectral ratio (3,0)/(0,0) at s=0.15 (tau=0.15); canonical_constants.py:289", "gate": None, "superseded": False, "note": "phi_paasch=1.531580 (canonical line 289; higher-precision form 1.5315844 is inv-11 W5-1's load-bearing input). PROVEN bare-ratio (3,0)/(0,0) at tau=0.15 at machine epsilon (S12). RECLASSIFIED prediction (BF=5) → mathematical property of the Dirac spectrum (BF=2), S28/S50 — atlas-04 P1 DISSOLVED. BdG DESTROYS it (PHI-BDG-47 FAIL); recursion-invariant (S42). Paasch LNH (Dirac G~1/t) EXCLUDED. Value already present; S110 W0 added this PROVENANCE entry (backfill, no value change) — closes the 'No PROVENANCE' get_constant gap flagged by HK-PHI-PAASCH (inv-3 HY8/B7 + inv-11 HY7)."},

    # SECTION E — SX
    "d_s_fold_window_sigma": {"session": "SX", "source": "S92-ADHOC-SPECTRAL-DIMENSION-DS-FLOW-VS-CDT", "gate": None, "superseded": False},

    # SECTION E — SX
    "R_canonical_bridge": {"session": "SX", "source": "S89-W2-R-CANONICAL-OBSERVABLE-IDENTITY", "gate": None, "superseded": False},

    # SECTION E — S94
    "Level3_integer_anchor_VII_AU_OP_PROJ_3HEB_BDI": {"session": "S94", "source": "computations/session-94/s94_vii_au_3heb_bdi_level_3_anchor.npz (S94-VII-AU-3HEB-BDI-LEVEL-3-ANCHOR PASS; audit_sha256=fdf1321ab5794c62996594edc66c0dfa8a04589e8c9689c58d9b05804781a80e)", "gate": "S94-VII-AU-3HEB-BDI-LEVEL-3-ANCHOR", "superseded": False},

    # SECTION B — S93
    "W_BG": {"session": "S93", "source": "s93_w8_6_narrow_path_pre_post_bogoliubov_ratio.npz (W_BG field); cosh(2r) Bogoliubov squeeze-weight", "gate": "S93-W8-6-NARROW-PATH-PRE-POST-BOGOLIUBOV-RATIO", "superseded": False},

    # SECTION B — S93
    "R_BG": {"session": "S93", "source": "s93_w8_6_narrow_path_pre_post_bogoliubov_ratio.npz (R_BG field); = 1/cosh(2r) = 1/W_BG", "gate": "S93-W8-6-NARROW-PATH-PRE-POST-BOGOLIUBOV-RATIO", "superseded": False},

    # SECTION B — S93
    "s_CS": {"session": "S93", "source": "s93_w8_3_narrow_path_cauchy_schwarz_joint_preflight.npz (s_cs_12 field); Cauchy-Schwarz slack at L_max=12", "gate": "S93-W8-3-NARROW-PATH-CAUCHY-SCHWARZ-JOINT-PREFLIGHT", "superseded": False},

    # SECTION D — S93
    "N_e_postfold": {"session": "S93", "source": "s93_w8_3_narrow_path_cauchy_schwarz_joint_preflight.npz (N_e field); post-fold acoustic e-folds", "gate": "S93-W8-3-NARROW-PATH-CAUCHY-SCHWARZ-JOINT-PREFLIGHT", "superseded": False},

    # SECTION D — S93
    "N_e_flip_threshold": {"session": "S93", "source": "session-93-phonon-first-cosmologist-synthesis.md (W8-3-3 workshop); N_e* where the Regime-II surrogate lean would flip", "gate": "S93-W8-3-NARROW-PATH-CAUCHY-SCHWARZ-JOINT-PREFLIGHT", "superseded": False},

    # SECTION E — S94
    "v_g_B2_fold": {"session": "S94", "source": "s94_ds_gamma_e_resolution_vg_b2_trajectory.npz", "gate": "S94-DS-GAMMA-E-RESOLUTION", "superseded": False},

    # SECTION D — S75
    "a_4_FW_zeta": {"session": "S75", "source": "s75_f_conv_spectral_output.txt (line 26); baseline-findings-s66.md a_4(fold)", "gate": None, "superseded": False},

    # SECTION E — S95
    "residue_s6_PS_Linf": {"session": "S95", "source": "s95_w1_3_vii_be_tier2_reanchor.npz", "gate": "CF-S95-VII-BE-TIER2-REANCHOR", "superseded": False},

    # SECTION E — S95
    "alpha_PS_residue_tail_s6": {"session": "S95", "source": "s95_w1_3_vii_be_tier2_reanchor.npz", "gate": "CF-S95-VII-BE-TIER2-REANCHOR", "superseded": False},

    # SECTION F-hygiene — S95 W6-4 (W0-MKK-PROVENANCE; mack-cosmic-bridge): provenance-completeness
    # writes for three constants that carried inline comments but NO machine-readable PROVENANCE-dict
    # entry. Values are BIT-UNCHANGED (provenance-transcription, NOT a re-value); confirmed via
    # get_constant read-back at S95 W6-4. Closes the confirmed hygiene gap before the DESI DR3
    # binding event (w0_FW binds Falsifier #1 / R_842 rectangle, S84-DR3-RESPONSE-PROTOCOL).
    "M_KK":              {"session": "S42", "source": "s42_constants_snapshot.npz (alias of M_KK_gravity)", "gate": "CONST-FREEZE-42", "superseded": False,
                          "note": "Default M_KK alias = M_KK_gravity = 7.428660036284456e16 GeV (spectral-zeta / "
                                  "Newton's-constant gravity route, S42; the conservative route). Alternate Kerner "
                                  "gauge-metric route M_KK_kerner=5.041679838376001e17 GeV; OOM_diff_MKK="
                                  "0.831664779390838 = log10(kerner/gravity) (0.83-decade route tension, both "
                                  "CONST-FREEZE-42 PASS). Mirrors M_KK_gravity provenance; the bare alias key lacked "
                                  "a PROVENANCE-dict entry until S95 W6-4. Value bit-unchanged (transcription only)."},
    "w0_FW":             {"session": "S58", "source": "S58 four-fold-lock (Volovik vacuum partition + effacement Gamma_effacement=0.99970)", "gate": None, "superseded": False,
                          "note": "Framework dark-energy w_0 = -0.918 from the Volovik vacuum partition + effacement "
                                  "(S58 four-fold structural lock; canonical_constants.py inline 'Volovik vacuum + "
                                  "effacement (S58)'); paired with wa_FW=0 (four-fold locked). Context route: S42 "
                                  "Sakharov/zeta vacuum-energy framing. DUAL CANONICAL: the structural S58 value is "
                                  "-0.918; a branch-(iv) W0-workshop promotion value w0_FW_R842=-0.842454 is "
                                  "CONDITIONAL on the R_842-rectangle DR3 PASS (NOT yet a standalone canonical constant; "
                                  "S83/S84). w0_FW is the BINDING constant for Falsifier #1 (DESI DR3, 2026 binding "
                                  "event); provenance added S95 W6-4 so it is audit-traceable before the binding. Value "
                                  "bit-unchanged (transcription only)."},
    "Delta_B3":          {"session": "S38", "source": "S38 B3-sector pairing-gap derivation (M_KK units)", "gate": None, "superseded": False,
                          "note": "B3 sector pairing gap = 0.176 (M_KK units), S38. NOMINALLY the doubled-gap "
                                  "convention of the later per-band GL gap Delta_B3_s53=0.084152 (S53); the doubling is "
                                  "approximate (2*Delta_B3_s53=0.168304, ~4.5% below 0.176 — the S38 value predates the "
                                  "s53/s52 acoustic-efold per-band derivation and is NOT a bit-exact 2x). DISTINCT "
                                  "constant from Delta_B3_s53 (the un-doubled S53 order-parameter gap added S95 W3-3); "
                                  "both coexist. The squared-sum total-gap identity uses Delta_B3_s53, not Delta_B3. "
                                  "PROVENANCE-dict entry added S95 W6-4; value bit-unchanged (transcription only)."},

    # SECTION C — S95
    "max_f_NL_FW": {"session": "S95", "source": "s95_w6_6_f_nl_row.py (verdict audit_sha256=077fde643e11edfc3455ca95cda321b40bfab5407086d8bb915e6fde3de65afb)", "gate": "F-NL-ROW", "superseded": False},

    # SECTION E — S95
    "n_PBH_FW_saturated_tail": {"session": "S95", "source": "s95_w6_1_n_pbh_magnitude_saturated_tail.npz (CF-S95-N-PBH-MAGNITUDE-RECOMPUTE INFO, audit_sha256=127e4fcef3dfbaed69b953ea20f6d1b637ae3e37228d166ff0c0c50e951dff8c)", "gate": "CF-S95-N-PBH-MAGNITUDE-RECOMPUTE", "superseded": False},

    # SECTION D — S96
    "M_KK_inv_seconds": {"session": "S96", "source": "s96_w1_mkk_seconds.npz", "gate": "S96-W1-MKK-SECONDS", "superseded": False},

    # SECTION D — S96
    "GeV_to_J": {"session": "S96", "source": "s96_w1_mkk_seconds.py (= eV_SI*eV_per_GeV, exact CODATA/SI)", "gate": "S96-W1-MKK-SECONDS", "superseded": False},

    # SECTION E — S96
    "Lambda_sp_over_M_KK": {"session": "S96", "source": "s63_species_scale.npz", "gate": "S63-SPECIES-36/SCALE-63", "superseded": False},

    # SECTION B-hygiene — S96 W6-7 (S96-OBS-ANCHOR-HYGIENE; mack-cosmic-bridge sole writer of
    # falsifier-master-inventory.md per feedback_mack-bridge-role.md). Provenance-completeness writes
    # for two OBSERVATIONAL-ANCHOR constants that carried inline "(Planck 2018)" comments but NO
    # machine-readable PROVENANCE-dict entry (knowledge-MCP reported "No PROVENANCE entry"). Values are
    # BIT-UNCHANGED (provenance-transcription, NOT a re-value). Per substrate-first-canonical-sourcing.md
    # SS(i) these are COMPARISON-ONLY observational anchors -- never a substrate replacement.
    "sigma_8":           {"session": "S96", "source": "s70_hydrostatic_cluster_log.txt (sigma_8(CMB,Planck2018)=0.811+/-0.006); S96-OBS-ANCHOR-HYGIENE (s96_obs_anchor_hygiene.npz; audit_sha256=37def5ddd58b9a5cdd3016949843fe94b5a61e905450ed3163b9fa810f7f9d0f)", "gate": "S96-OBS-ANCHOR-HYGIENE", "superseded": False,
                          "note": "Planck-2018 sigma_8 LSS matter-fluctuation amplitude = 0.811 +/- 0.006; "
                                  "named chain = Planck 2018 TT,TE,EE+lowE+lensing (Aghanim+2020 A&A 641 A6). "
                                  "COMPARISON-ONLY observational anchor (substrate-first-canonical-sourcing.md "
                                  "SS(i)) -- NOT a substrate replacement. Framework sigma_8_FW=0.799 (E33) is the "
                                  "substrate a_2-channel growth prediction; d_FW = |0.799-0.811|/0.006 = 2.00sigma. "
                                  "LABELING CAUTION: the capstone SS7.1 row (phonic-exflation-equation.md:430) "
                                  "'Planck 0.829' is an S_8 value (S_8(Planck)=0.8310+/-0.016, s69_pvd11_kappa_log.txt), "
                                  "NOT sigma_8; the 0.829-vs-0.811 is a sigma_8/S_8 labeling difference, not a stale "
                                  "pin (S_8(FW)=0.8128 vs S_8(Planck)=0.8310 -> d=1.14sigma). Value bit-unchanged "
                                  "(inline '(Planck 2018)' since pre-S52; PROVENANCE-dict entry added S96 W6-7, "
                                  "closing the knowledge-MCP 'No PROVENANCE entry' gap)."},
    "A_s_CMB":           {"session": "S96", "source": "canonical_constants.py:84 (Planck 2018 VI); S96-OBS-ANCHOR-HYGIENE (s96_obs_anchor_hygiene.npz; audit_sha256=37def5ddd58b9a5cdd3016949843fe94b5a61e905450ed3163b9fa810f7f9d0f)", "gate": "S96-OBS-ANCHOR-HYGIENE", "superseded": False,
                          "note": "Planck-2018 scalar amplitude A_s = (2.10 +/- 0.03)e-9 (Planck 2018 VI). "
                                  "COMPARISON-ONLY observational anchor (substrate-first-canonical-sourcing.md SS(i)). "
                                  "Framework A_s_FW is a PENDING BAND [3.11,4.27]e-9 (37% span over eps in "
                                  "{0.02163,0.020}; falsifier-master-inventory Row #12) -- band edges 33.7-72.3sigma "
                                  "from this anchor, but eps_pivot is UNPINNED (S86 SECTOR-1 carry-forward, W5a P3 "
                                  "FOLD-PIVOT-RUNNING-FLOW-SECTOR-1), so the band-vs-live-tension call DEFERS to the "
                                  "greybody central-value gate (mack CF-3 / phonon-first CF-PF-3) per the "
                                  "FROZEN-PREDICTION-DISCIPLINE-COMMIT (S86 W13 P1) band-not-point contract. Alias "
                                  "A_s_Planck=A_s_CMB. Value bit-unchanged; PROVENANCE-dict entry added S96 W6-7, "
                                  "closing the knowledge-MCP 'No PROVENANCE entry' gap."},

    # SECTION E — S96
    "a_6_FW_zeta": {"session": "S96", "source": "s96_sdw_eft_control.npz; E38 per-branch L_max=3 zeta moment on s84_spectrum_cache_L12_tau019.npz", "gate": "S96-SDW-EFT-CONTROL", "superseded": False},

    # SECTION E — S96
    "a_8_FW_zeta": {"session": "S96", "source": "s96_sdw_eft_control.npz; E38 per-branch L_max=3 zeta moment on s84_spectrum_cache_L12_tau019.npz", "gate": "S96-SDW-EFT-CONTROL", "superseded": False},

    # SECTION E — S96
    "f_FW": {"session": "S96", "source": "computations/session-70/s70_bulk_flow.npz:f_FW_z0 (orig s59/s65 growth ODE; surfaced S96 W6-1)", "gate": "S96-OBS-FSIGMA8-FORECAST", "superseded": False},

    # SECTION E — S96
    "f_LCDM": {"session": "S96", "source": "computations/session-70/s70_bulk_flow.npz:f_LCDM_z0", "gate": "S96-OBS-FSIGMA8-FORECAST", "superseded": False},

    # SECTION E — S96
    "fsigma8_product_suppression_FW_max_pct": {"session": "S96", "source": "computations/session-96/s96_obs_fsigma8_forecast.npz:max_frac_FW_pct (orig s65_fsigma8.npz:frac_FW)", "gate": "S96-OBS-FSIGMA8-FORECAST", "superseded": False},

    # SECTION E — S96
    "f_bare_suppression_FW_pct": {"session": "S96", "source": "computations/session-96/s96_obs_fsigma8_forecast.npz:delta_f_pct", "gate": "S96-OBS-FSIGMA8-FORECAST", "superseded": False},

    # SECTION E — S96
    "A_FS_first_sound_ring": {"session": "S96", "source": "s96_obs_first_sound_ring.npz (from S43 s43_kk_cmb_transfer A_first_sound=0.2045; S95 W6-2 A_FS_S43)", "gate": "S96-OBS-FIRST-SOUND-RING", "superseded": False},

    # SECTION E — S96
    "r1_first_sound_ring_Mpc": {"session": "S96", "source": "s96_obs_first_sound_ring.npz (S43 s43_kk_cmb_transfer r_1=325.265; S95 W6-2 r1_ring_mpc)", "gate": "S96-OBS-FIRST-SOUND-RING", "superseded": False},

    # SECTION E — S96
    "k1_first_sound_ring_invMpc": {"session": "S96", "source": "s96_obs_first_sound_ring.npz (S95 W6-2 k1_ring; S43 k_1=0.019317)", "gate": "S96-OBS-FIRST-SOUND-RING", "superseded": False},

    # SECTION E — S96
    "sigma_Pk_DESI_Y5_BAO_scale": {"session": "S96", "source": "s96_obs_first_sound_ring.npz; FETCHED arXiv:2411.19738v2 (DESI 2024 reconstruction; DR1=0.001/0.025=0.040, Y5=DR1/1.7)", "gate": "S96-OBS-FIRST-SOUND-RING", "superseded": False},

    # SECTION E — S96
    "f_obs_CGWB_peak_kappa_nat": {"session": "S96", "source": "s96_obs_cgwb_peak_freq.npz (S96-OBS-CGWB-PEAK-FREQ)", "gate": "S96-OBS-CGWB-PEAK-FREQ", "superseded": False},

    # SECTION E — S96
    "f_NL_total_GGE_S67": {"session": "S96", "source": "s96_hyg_fnl_bound_vs_point.py (verdict audit_sha256=c7b4a5b6792dfcc5542aca21ae173c3a483d36a9a1d465fa09f1a8435d3a40ec); S67 GGE-BISPECTRUM-67 central total (falsifier-rigor-registry.md row 9; channels equil 0.853 + folded 0.129 + multi 0.56, coherent total)", "gate": "S96-HYG-FNL-BOUND-VS-POINT", "superseded": False},

    # SECTION E — S72 (S96-HYG-CANONICAL-PINS W7-2 NEW pin)
    "t_star": {"session": "S72", "source": "lizzi-spectral-functional.md (S72 spectral-functional fit); phonic-exflation-equation.md capstone", "gate": "T-STAR-ONELOOP-ORIGIN", "superseded": False,
               "note": "t* = 0.08832 is the one empirical spectral-functional coupling (the Lambda_QCD analog of the substrate). DISTINCT from mellin_f_star_f0 = 0.08832: the values are near-coincident but t_star is the S72 functional-fit coupling whereas mellin_f_star_f0 is a Mellin f*/f0 ratio (lizzi-flagged UNTESTED-as-derivation). Pinned S96 W7-2."},

    # SECTION E — S74 (S96-HYG-CANONICAL-PINS W7-2 NEW pin)
    "R1_lizzi": {"session": "S74", "source": "sp V.7 (=a0*a4/a2^2 = 6440*1350.7216/2776.165389^2); Sage-verified; phonic-exflation-equation.md capstone", "gate": "N16-RATIO-OF-RATIOS-PROTECTED-74", "superseded": False,
                 "R_protected": True, "scheme_tag": "SCHEME-INDEPENDENT",
                 "note": "FI (Functional-Invariant) scheme-invariant spectral-moment ratio R1 = a0*a4/a2^2. Vol(K) cancels per Baptista B2; invariant under R_K -> c*R_K (a0 deg-0, a2 -> c*a2, a4 -> c^2*a4; c cancels). = 6440*1350.7216/2776.165389^2 = 1.1286546 (rounds to 1.128655 at 7 sig figs). Same per-branch caveat as R_protected_fold (NOT a cross-scheme conversion factor). Pinned S96 W7-2."},

    # SECTION E — S95 (S96-HYG-CANONICAL-PINS W7-2 NEW pin)
    "R_therm": {"session": "S95", "source": "S95 W5 Ordered-Veil (=t_therm/t_transit); sagan II.7; phonic-exflation-equation.md capstone", "gate": None, "superseded": False,
                "note": "R_therm = t_therm / t_transit = 5251.82, the diabatic transit/thermalization timescale ratio. R_therm >> 1 is what keeps the post-transit GGE relic an Ordered Veil (integrable, never thermalizes) rather than reaching thermal equilibrium. Pinned S96 W7-2."},

    # SECTION E — S70 (S96-HYG-CANONICAL-PINS W7-2 NEW pin)
    "Mass_LeggettDM_over_Delta_BCS": {"session": "S70", "source": "LEGGETT-MOMENT-70 (Leggett-channel GGE quasiparticle DM mass on the BCS gap scale); phonic-exflation-equation.md capstone", "gate": "LEGGETT-MOMENT-70", "superseded": False,
                                      "conditional": "Gamma_grav < H_0",
                                      "note": "Mass_LeggettDM / Delta_BCS = 11.97, the substrate-IS dark-matter mass anchor on the BCS gap scale (Leggett inter-band coherence mode; CPT-neutral, non-annihilating). CONDITIONAL on Gamma_grav < H_0 (the gravitational decay rate of the Leggett mode stays below the Hubble rate, so the relic survives). Pinned S96 W7-2."},

    # SECTION E — S96 W7-2 PROVENANCE BACKFILLS (values already present in the module; provenance dict entry added by S96-HYG-CANONICAL-PINS)
    "tau_NEC": {"session": "S85/S95", "source": "canonical_constants.py L2122 (value present since S85 W6); S95 W4-5 12D censorship; hawking V.3/V.9; phonic-exflation-equation.md capstone", "gate": None, "superseded": False,
                "note": "tau_NEC = 1.383 is the NEC-violation onset / physical-domain boundary on the Jensen-flow trajectory (Ric_min crosses 0). 3-decimal canonical; sp-synthesis fine value 1.382334. Value already present in the module; S96 W7-2 added this PROVENANCE entry (backfill, no value change)."},
    "Z_fold": {"session": "S42", "source": "s42_gradient_stiffness.npz (value present since S42, canonical_constants.py L501)", "gate": None, "superseded": False,
               "note": "Z_fold = 74730.76411846, the gradient stiffness at the fold (S42). Value already present in the module; S96 W7-2 added this PROVENANCE entry (backfill, no value change)."},
    "Mach_max_framework": {"session": "S85", "source": "phononic-framing.md LCDM-reframe table (van Hove fold velocity ratio); canonical_constants.py L2123 (value present since S85 W6-1)", "gate": None, "superseded": False,
                           "note": "Mach_max_framework = 13.75, the framework Mach number at the van Hove fold (supersonic transit, the substrate-language reframe of LCDM 'slow-roll inflation'). ALIAS: Mach_max = Mach_max_framework (default alias, canonical_constants.py L2125); the BEC analog-realization value is the SEPARATE Mach_max_analog = 54.3. Value already present; S96 W7-2 added this PROVENANCE entry (backfill, no value change)."},

    # SECTION E — S110 W0a PROVENANCE BACKFILLS (values already present in the module; provenance dict entries added by the S110 W0a investigation-distillation housekeeping wave, mack-cosmic-bridge. HK-OMEGA-DM + HK-T-ACOUSTIC. NO value changes.)
    "Omega_DM": {"session": "Planck 2018", "source": "Aghanim+ 2020 A&A 641 A6 (Planck 2018 cosmological parameters); computed as Omega_m - Omega_b = 0.315 - 0.0493 (canonical_constants.py L88-90)", "gate": None, "superseded": False,
                 "note": "Omega_DM = Omega_m - Omega_b = 0.315 - 0.0493 = 0.2657 (dark-matter density parameter, Planck 2018). OBSERVATIONAL anchor (COMPARISON-ONLY per substrate-first-canonical-sourcing.md §(i)); the framework's DM-channel prediction (Leggett-channel Omega_DM h^2 = 0.120, 0.6% from Planck; full f_DM partition in framework-dm-properties.md) is compared against this, never replaced by it. NOTE: the inline comment at L90 rounds to '= 0.266'; the exact computed value is 0.2657 (get_constant authoritative). Value already present; S110 W0a added this PROVENANCE entry (backfill, no value change) — closes the 'No PROVENANCE entry' get_constant gap flagged by HK-OMEGA-DM."},
    "T_acoustic": {"session": "S42/S47", "source": "GGE acoustic temperature (S42 cold-big-bang / S47 GGE-relic); canonical_constants.py L732", "gate": None, "superseded": False,
                   "note": "T_acoustic = 0.112 (M_KK units), the GGE acoustic temperature of the post-transit relic (the substrate-language reheating analog; NOT a thermal-equilibrium temperature — the GGE never thermalizes, R_therm=5252, S_ent=0 S95-certified). Value already present; S110 W0a added this PROVENANCE entry (backfill, no value change) — closes the 'No PROVENANCE entry' get_constant gap flagged by HK-T-ACOUSTIC."},
    "kappa_BCS": {"session": "S69", "source": "S69 W3-D (BCS surface-gravity analog); MEMORY.md; canonical_constants.py L2435", "gate": None, "superseded": False,
                  "note": "kappa_BCS = 4.019, the BCS surface-gravity analog (the acoustic-white-hole surface gravity in the BCS/transit reading, S69 W3-D). Value already present; S110 W0a added this PROVENANCE entry (backfill, no value change) — closes the 'No PROVENANCE entry' get_constant gap flagged by HK-T-ACOUSTIC. NOTE: Mach_max (the third constant the HK-T-ACOUSTIC triage row named) ALREADY has a PROVENANCE entry (Mach_max_framework, S96 W7-2 backfill, this dict) — so only T_acoustic + kappa_BCS were genuinely missing."},

    # SECTION E — S96
    "c_s2_FW": {"session": "S96", "source": "S96-HYG-CS2-REGISTRY (W7-8); van-den-dungen V.4 S96-VDD-CS2-TOPOLOGICAL-LEDGER", "gate": "S96-HYG-CS2-REGISTRY", "superseded": False},

    # SECTION E — S96
    "c_s2_kasparov_bound": {"session": "S96", "source": "S96-HYG-CS2-REGISTRY (W7-8); S71-72 Kasparov bound", "gate": "S96-HYG-CS2-REGISTRY", "superseded": False},

    # SECTION E — S67
    "x_fold": {"session": "S67", "source": "S67 GGE-TWO-FLUID-67/ODLRO; canonicalized S97-W1-XTODAY (PASS)", "gate": "S97-W1-XTODAY", "superseded": False},

    # SECTION E — S95
    "Omega_BA_fold": {"session": "S95", "source": "s95_w4_4_sp_conformal_embed.npz; canonicalized S97-W1-OMEGA-PROFILE (PASS, rel 1.5e-4)", "gate": "S97-W1-OMEGA-PROFILE", "superseded": False},

    # SECTION C — S97
    "Omega_GW_acoustic_peak": {"session": "S97", "source": "s97_omegagw_peak_height.npz (S97-OMEGAGW-PEAK-HEIGHT, PASS, audit_sha256=71fbc18f1db246f49fd6e3b0e570f54d4828d53a8ae5cfc253d42a8d5a0f3016)", "gate": "S97-OMEGAGW-PEAK-HEIGHT", "superseded": False},

    # SECTION E — S97
    "Omega_GW_acoustic_LISA_tail": {"session": "S97", "source": "s97_omegagw_acoustic_spectral_shape.npz (S97-OMEGAGW-ACOUSTIC-SPECTRAL-SHAPE, PASS, audit_sha256=c63d386972c28be3...)", "gate": "S97-OMEGAGW-ACOUSTIC-SPECTRAL-SHAPE", "superseded": False},

    # SECTION E — S97
    "Omega_DM_h2": {"session": "S97", "source": "Planck 2018 (Aghanim+2018) observed physical DM density Omega_DM h^2; W8-5 reproducer headline; framework Leggett-channel value LEGGETT-MOMENT-70 coincides at 0.6%", "gate": None, "superseded": False, "note": "OBSERVATIONAL-ANCHOR (Planck-observed physical DM density Omega_DM h^2; lab-IN datum, cross-check anchor only per substrate-first-canonical-sourcing.md (i); NOT a substrate prediction). DISTINCT from Omega_DM_obs=0.264 (Planck density PARAMETER Omega_DM, canonical_constants.py:539) -- physical density Omega*h^2 vs dimensionless density parameter; the two are NOT to be conflated."},

    # SECTION E — S97
    "rho_vac_over_rho_obs": {"session": "S97", "source": "s66 DILUTION-CC-66 (Volovik tracking-vacuum rho_vac ~ M_Pl^2 H^2, Scenario B; Volovik Paper 25 SSV / Paper 35); W8-5 reproducer headline", "gate": "DILUTION-CC-66", "superseded": False, "note": "FRAMEWORK-PREDICTION (substrate-first; gate DILUTION-CC-66/S66 Scenario B closes the 114-OOM CC gap to 0.01 OOM, CC_OOM=115.5; a_0 Seeley-DeWitt zeroth moment tracks the Volovik H^2-scaling vacuum). C10 (Atlas-04) rho_vac ~ M_Pl^2 H^2 ASSUMED-PARTIALLY-PROVEN -- conditionality carried so the pin does not overstate its register status."},

    # SECTION E — S97
    "R_cross_yukawa_t1_t2": {"session": "S97", "source": "s97_yukawa_family_derive.npz (S97-YUKAWA-FAMILY-DERIVE); workshop w-2-yukawa-degeneracy-reality-axiom.md; registry SS-VII.BL", "gate": "S97-YUKAWA-FAMILY-DERIVE", "superseded": False},

    # SECTION E — S98 (S98-HK-SIGMA8-CHANNEL-KEYED-PINS W6-1: two channel-keyed sigma_8 readouts,
    # channel-distinct provenance + cross-note. CROSS-NOTE: sigma8_OZ_50 (=0.799, O-Z/spectral-action channel,
    # HEADLINE) and sigma8_growth_a2 (=0.79317, a2 Seeley-DeWitt growth channel) are TWO DISTINCT substrate-IS
    # spectral-channel readouts ~0.7% apart (0.735%, O-Z LARGER), NOT two measurements of one container number;
    # BOTH distinct from LCDM reference sigma_8=0.811 (O-Z -1.50%, growth -2.18% vs LCDM). Verbatim-upstream (M3).)
    "sigma8_OZ_50": {"session": "S98", "source": "SIGMA8-OZ-50 (S50 PASS); computations/session-50/s50_sigma8_oz.py; atlas-07-permanent-results.md (PERMANENT); in [0.740,0.820], -1.50% vs LCDM", "gate": "S98-HK-SIGMA8-CHANNEL-KEYED-PINS", "superseded": False,
                     "channel": "spectral-action / Ornstein-Zernike (O-Z); a0-region; constant-mass O-Z propagator P(K)=T/[J*K^2+m^2]; HEADLINE sigma_8",
                     "note": "Channel-distinct partner of sigma8_growth_a2 (a2-growth channel, S70/S96/S97): TWO substrate-IS spectral-channel sigma_8 readouts ~0.7% apart (|0.799-0.79317|/0.79317=0.735%), O-Z LARGER; NOT two measurements of one container quantity. BOTH below LCDM reference sigma_8=0.811 (Planck 2018, S96-OBS-ANCHOR-HYGIENE): O-Z -1.50% vs LCDM. Do NOT read the ~0.7% inter-channel spread as a single-channel uncertainty band. HEADLINE single-number sigma_8 for scorecard/capstone display."},

    # SECTION E — S98
    "sigma8_growth_a2": {"session": "S98", "source": "S70 computations/session-70/s70_bulk_flow.npz (orig s59_growth_factor.npz sigma8_fw=0.793166 -> 0.79317 5-sig); re-confirmed S96 (f_FW) + S97-FSIGMA8-FORECAST-REFETCH PASS audit a20043e7", "gate": "S98-HK-SIGMA8-CHANNEL-KEYED-PINS", "superseded": False,
                         "channel": "a2 Seeley-DeWitt growth channel; linear growth f=dlnD/dlna feeding fsigma8 forecasts; -0.311% bare-f suppression",
                         "note": "Channel-distinct partner of sigma8_OZ_50 (O-Z/spectral-action channel, S50, HEADLINE): TWO substrate-IS spectral-channel sigma_8 readouts ~0.7% apart (0.735%), O-Z LARGER; NOT two measurements of one container quantity. BOTH below LCDM reference sigma_8=0.811 (Planck 2018, S96-OBS-ANCHOR-HYGIENE): growth -2.18% vs LCDM. Do NOT read the ~0.7% inter-channel spread as a single-channel uncertainty band. This is the structure-growth-channel readout feeding fsigma8 forecasts, NOT the headline single-number sigma_8."},

    # SECTION E — S98
    "rho_vac_over_rho_rad_BBN_below": {"session": "S98", "source": "s98 S98-MK3-2-BBN-VACUUM-FRACTION (audit_sha256 1ad846b244e334be3c0ecf1c447503b4ceebb4b41e23aa53eaa4aeaa7112f45d); n_eff=1.978111 from-below (V.9 pinned) propagated into BBN-epoch rho_vac/rho_rad via H^2=(8piG/3)(rho_rad+rho_vac), rho_vac=alpha_V M_Pl^2 H^n_eff, lever X^(n-2), X=ln(H_BBN/H_0)=40.2756", "gate": "S98-MK3-2-BBN-VACUUM-FRACTION", "superseded": False},

    # SECTION E — S98
    "delta_N_eff_vacuum_BBN_below": {"session": "S98", "source": "s98 S98-MK3-2-BBN-VACUUM-FRACTION (audit_sha256 1ad846b244e334be3c0ecf1c447503b4ceebb4b41e23aa53eaa4aeaa7112f45d); delta_N_eff(vacuum) = (rho_vac/rho_rad)_BBN / (7/8*(4/11)^(4/3)) = 0.474049/0.227113 (canonical S66 formula, session-66-mack-qa-workshop.md)", "gate": "S98-MK3-2-BBN-VACUUM-FRACTION", "superseded": False},

    # SECTION E — S99
    "Sigma_mnu_FW": {"session": "S99", "source": "s99_w3_seesaw_summnu.npz", "gate": "S99-W3-SEESAW-SUMMNU", "superseded": False},

    # SECTION E — S99
    "Sigma_mnu_bound_DESI_2024": {"session": "S99", "source": "DESI 2024 arXiv:2404.03002 (DESI DR1 BAO cosmology, LCDM + Sum m_nu, 95% CL)", "gate": "S99-W3-SEESAW-SUMMNU", "superseded": False},

    # SECTION E — S100b
    "phi_CP_K7_transit": {"session": "S100b", "source": "S98-W3-2-BARYOGEN-UNIQUENESS (s98 verdicts); sector-split per session-99-litreview-consolidated-gen-physicist.md §III (G3 dirac flag)", "gate": "S98-W3-2-BARYOGEN-UNIQUENESS", "superseded": False},

    # SECTION E — S100b
    "delta_CP_PMNS_substrate": {"session": "S100b", "source": "S99-W3-SEESAW-SUMMNU verdict (delta_CP=[0,pi]); sector-split per session-99-litreview-consolidated-gen-physicist.md §III (G3 dirac flag)", "gate": "S99-W3-SEESAW-SUMMNU", "superseded": False},

    # SECTION E — S100b (provenance backfill — values pre-existing and unchanged; vintage verified)
    "dm2_21_NuFit": {"session": "S100b", "source": "NuFit-6.0 PDF (SHA 66ff020fea48d04fe703e99559d625ed3d0bacfc36cbf619b8df16652d54194f) Table 1, IC24-with-SK-atm NO best fit, as-printed; asserted equal at 1e-12 by s100b_w2_3_mr_texture_class.py (vintage adjudication pinned in plan §W2-3 nufit_pins)", "gate": "S100b-MR-TEXTURE-CLASS", "superseded": False},

    # SECTION E — S100b (provenance backfill — values pre-existing and unchanged; vintage verified)
    "dm2_31_NuFit": {"session": "S100b", "source": "NuFit-6.0 PDF (SHA 66ff020fea48d04fe703e99559d625ed3d0bacfc36cbf619b8df16652d54194f) Table 1, IC24-with-SK-atm NO best fit, as-printed (+2.513e-3, dm2_3l = dm2_31 for NO); asserted equal at 1e-12 by s100b_w2_3_mr_texture_class.py (vintage adjudication pinned in plan §W2-3 nufit_pins)", "gate": "S100b-MR-TEXTURE-CLASS", "superseded": False},

    # SECTION E — S100b (provenance backfill — values pre-existing and unchanged; formalizes the constants' own inline comments; flagged missing by W2-1, executed orchestrator-direct at session close)
    "m_tau": {"session": "S100b", "source": "S42 W2-1 (modulus mass at fold, M_KK units — per the constant's inline comment at definition; framework-derived J-ratio image = 19.52*m_mu, identity confirmed by s100b_w2_1_sym3_cubic_ladder_p_exponent.py; Class-(d)-guarded as forbidden residual target per housekeeping §A12)", "gate": "S100b-SYM3-CUBIC-LADDER-P-EXPONENT", "superseded": False},

    # SECTION E — S100b (provenance backfill — values pre-existing and unchanged; formalizes the constants' own inline comments; flagged missing by W2-1, executed orchestrator-direct at session close)
    "m_mu": {"session": "S100b", "source": "PDG 2024 muon mass 0.1056583745 GeV — per the constant's inline comment at definition; consumed by s100b_w2_1_sym3_cubic_ladder_p_exponent.py (J-ratio identity check)", "gate": "S100b-SYM3-CUBIC-LADDER-P-EXPONENT", "superseded": False},

    # SECTION E — S42
    "sigma_over_m": {"session": "S42", "source": "atlas-07-permanent-results row '[NEW S42] sigma/m (CDM)'; s43_cbb_timeline.py L86; s44_cdm_construct.py gravitational-transport derivation (sigma_T = 4pi (G_N m)^2/v^4 lnLambda)", "gate": None, "superseded": False},

    # SECTION E — S100a
    "sigma_DM_nucleon_FW": {"session": "S100a", "source": "S100a-W1-4-SIGMA-DM-NUCLEON", "gate": "S100a-W1-4-SIGMA-DM-NUCLEON", "superseded": False},

    # SECTION E — S100a
    "M_DM_Leggett_GeV": {"session": "S100a", "source": "S100a-W1-4-SIGMA-DM-NUCLEON", "gate": "S100a-W1-4-SIGMA-DM-NUCLEON", "superseded": False},

    # SECTION E — S100a
    "m_bb_FW": {"session": "S100a", "source": "s100a_d5_0nubb_majorana.npz", "gate": "S100a-D5-0NUBB-MAJORANA", "superseded": False},

    # SECTION E — S100a
    "m_H_FW_KK_threshold": {"session": "S100a", "source": "KK-THRESHOLD-64 (S64 W4-B, INFO); S28c framework prediction lineage", "gate": "S100a-M0-MH-INHERITANCE", "superseded": False},

    # SECTION E — S100a
    "m_H_FW_tree": {"session": "S100a", "source": "theorem A10 (S62 Filter-Independence; atlas-07 permanent result)", "gate": "S100a-M0-MH-INHERITANCE", "superseded": False},

    # OBSERVATIONAL — Higgs mass (mack PROVENANCE landing 2026-06-12; flagged by anderson-higgs reviewer as missing)
    "m_H_obs": {"session": "obs", "source": "ATLAS+CMS Run-1 combined m_H = 125.09 +/- 0.24 GeV (arXiv:1503.07589, PRL 114 191803), rounded to 125.1. NOT PDG-2024 (which is 125.25 +/- 0.17). The inline '# PDG 2024' comment was incorrect and is corrected to the Run-1 combination. LOAD-BEARING as the exact-rational denominator: m_H_FW_KK_threshold/m_H_obs - 1 = 67/1251 exact; m_H_FW_tree/m_H_obs - 1 = 89/1251 exact. Re-pinning to PDG-2024 125.25 would break both exact ratios; a re-pin is a 4-field carry-forward, NOT an in-place edit.", "gate": None, "superseded": False, "note": "Observational Higgs-mass anchor; value 125.1 unchanged. PDG-2024 central 125.25 +/- 0.17 noted as the current-best alternative; see carry-forward CF-S104-MH-OBS-REPIN."},

    # SECTION E — S100a
    "spinor_norm_factor_FW": {"session": "S100a", "source": "s100a_h0_spinor_factor.py", "gate": "S100a-H0-SPINOR-FACTOR", "superseded": False},

    # SECTION E — S100a
    "m_tau_PDG": {"session": "S100a", "source": "PDG tau pole mass 1776.86 +- 0.12 MeV (PDG 2022-2024 lineage; the value the S100a-plan-w2 widening band edge 1.8894 = ln(m_mu/m_e)/ln(m_tau/m_mu) was computed from)", "gate": "S100a-CONNES-DISTANCE-LADDER", "superseded": False},

    # SECTION E — S100a
    "m_u_msbar_2GeV": {"session": "S100a", "source": "PDG 2024 quark masses (MS-bar, mu=2 GeV): m_u = 2.16 +/- 0.07 MeV", "gate": "S100a-FREEZEIN-OVERCONSTRAINED", "superseded": False},

    # SECTION E — S100a
    "m_d_msbar_2GeV": {"session": "S100a", "source": "PDG 2024 quark masses (MS-bar, mu=2 GeV): m_d = 4.70 +/- 0.07 MeV", "gate": "S100a-FREEZEIN-OVERCONSTRAINED", "superseded": False},

    # SECTION E — S100a
    "m_s_msbar_2GeV": {"session": "S100a", "source": "PDG 2024 quark masses (MS-bar, mu=2 GeV): m_s = 93.5 +/- 0.8 MeV", "gate": "S100a-FREEZEIN-OVERCONSTRAINED", "superseded": False},

    # SECTION E — S100a
    "m_c_msbar_mc": {"session": "S100a", "source": "PDG 2024 quark masses (MS-bar at own scale): m_c(m_c) = 1.2730 +/- 0.0046 GeV", "gate": "S100a-FREEZEIN-OVERCONSTRAINED", "superseded": False},

    # SECTION E — S100a
    "m_c_pole": {"session": "S100a", "source": "PDG 2024 quark masses: charm pole mass 1.67 +/- 0.07 GeV", "gate": "S100a-FREEZEIN-OVERCONSTRAINED", "superseded": False},

    # SECTION E — S100a
    "m_b_msbar_mb": {"session": "S100a", "source": "PDG 2024 quark masses (MS-bar at own scale): m_b(m_b) = 4.183 +/- 0.007 GeV", "gate": "S100a-FREEZEIN-OVERCONSTRAINED", "superseded": False},

    # SECTION E — S100a
    "V_us_PDG": {"session": "S100a", "source": "PDG 2024 CKM global fit: |V_us| = 0.22500 +/- 0.00067", "gate": "S100a-FREEZEIN-OVERCONSTRAINED", "superseded": False},

    # SECTION E — S100a
    "V_us_sigma_PDG": {"session": "S100a", "source": "PDG 2024 CKM global fit: |V_us| = 0.22500 +/- 0.00067", "gate": "S100a-FREEZEIN-OVERCONSTRAINED", "superseded": False},

    # SECTION E — S100a
    "V_ub_PDG": {"session": "S100a", "source": "PDG 2024 CKM: |V_ub| = (3.82 +/- 0.20)e-3 (incl/excl average)", "gate": "S100a-FREEZEIN-OVERCONSTRAINED", "superseded": False},

    # SECTION E — S100a
    "V_cb_PDG": {"session": "S100a", "source": "PDG 2024 CKM: |V_cb| = (40.8 +/- 1.4)e-3 (incl/excl average)", "gate": "S100a-FREEZEIN-OVERCONSTRAINED", "superseded": False},

    # SECTION E — S100a
    "J_CP_PDG": {"session": "S100a", "source": "PDG 2024 CKM global fit: Jarlskog J = (3.08 +0.15/-0.13)e-5", "gate": "S100a-FREEZEIN-OVERCONSTRAINED", "superseded": False},

    # SECTION E — S100b
    "delta_N_eff_budget_GoldsteinHill_2026": {"session": "S100b", "source": "S100b-X-C10-BBN-CONSTRAINT-RECONCILE", "gate": "S100b-X-C10-BBN-CONSTRAINT-RECONCILE", "superseded": False},

    # SECTION E — S100b
    "T_RH_GeV": {"session": "S100b", "source": "computations/session-76/s76_moduli_decay_gw_spectrum.npz (key T_RH_GeV; W2-H pin)", "gate": "S100b-X-C10-BBN-CONSTRAINT-RECONCILE", "superseded": False},

    # SECTION E — S100b
    "S_capture_floor_LRD_classic": {"session": "S100b", "source": "Rinaldi+ arXiv 2604.07138 (JADES GOODS-S/N LRD census; PDF SHA e392aad4125b18d6...); fetched-text extraction s100b_w7_selection_function_floor.py", "gate": "S100b-SELECTION-FUNCTION-FLOOR", "superseded": False},

    # SECTION E — S100b
    "m_proton_g": {"session": "S100b", "source": "CODATA 2018 proton mass (1.67262192369e-27 kg)", "gate": "S100b-A2-HEAVY-SEED-ABUNDANCE", "superseded": False},

    # SECTION E — S100b
    "M_sun_g": {"session": "S100b", "source": "IAU 2015 nominal GM_sun = 1.3271244e20 m^3 s^-2 / CODATA-2018 G_N = 6.67430e-11", "gate": "S100b-A2-HEAVY-SEED-ABUNDANCE", "superseded": False},

    # SECTION E — S100b
    "pc_to_cm": {"session": "S100b", "source": "derived alias: Mpc_to_cm / 1e6 (consistent with existing canonical Mpc_to_cm = 3.0857e24)", "gate": "S100b-A2-HEAVY-SEED-ABUNDANCE", "superseded": False},

    # SECTION E — S100b
    "yr_to_s": {"session": "S100b", "source": "Julian year = 365.25 d x 86400 s (exact definition, IAU)", "gate": "S100b-A2-HEAVY-SEED-ABUNDANCE", "superseded": False},

    # SECTION E — S100b
    "f2_dict_CC": {"session": "S100b", "source": "Chamseddine-Connes spectral-action dictionary §8.3 (f_2 ~ 92); prior in-repo machinery: s95_w3_3_back_reaction_closure.py G_eff_of_tau (f2=92.0) + s96_w1_aoft_friedmann_map.py F2_DICT=92.0", "gate": "S100b-A2-HEAVY-SEED-ABUNDANCE", "superseded": False},

    # SECTION E — S100b
    "kappa_UV_MadauDickinson": {"session": "S100b", "source": "Madau & Dickinson 2014 (ARA&A 52, 415) SFR = kappa_UV * L_UV calibration; Salpeter-basis FUV conversion; plan pin session-100b-plan-w7.md SW7-3 machinery_pin_map kappa_UV", "gate": "S100b-STRUCTURE-TIMING-TWO-AXIS", "superseded": False},

    # SECTION C — S101
    "beta2_pivot_box_delta": {"session": "S101", "source": "s101_w5_1_beta_pivot_promotion.npz", "gate": "S101-BETA-PIVOT-PROMOTION", "superseded": False},

    # SECTION C — S101
    "beta2_pivot_box_delta_sqrtA_recipe": {"session": "S101", "source": "s101_w5_1_beta_pivot_promotion.npz", "gate": "S101-BETA-PIVOT-PROMOTION", "superseded": False},

    # SECTION E — S101
    "sin2_theta12_PDG": {"session": "S101", "source": "S101-HK-PMNS-PIN-PROMOTION", "gate": "S101-HK-PMNS-PIN-PROMOTION", "superseded": False},

    # SECTION E — S101
    "sin2_theta13_PDG": {"session": "S101", "source": "S101-HK-PMNS-PIN-PROMOTION", "gate": "S101-HK-PMNS-PIN-PROMOTION", "superseded": False},

    # SECTION E — S101
    "sin2_theta12_NuFit60": {"session": "S101", "source": "S101-HK-PMNS-PIN-PROMOTION", "gate": "S101-HK-PMNS-PIN-PROMOTION", "superseded": False},

    # SECTION E — S101
    "sin2_theta13_NuFit60": {"session": "S101", "source": "S101-HK-PMNS-PIN-PROMOTION", "gate": "S101-HK-PMNS-PIN-PROMOTION", "superseded": False},

    # SECTION E — S101
    "x696_ncg_coincidence_headroom_ratio": {"session": "S101", "source": "S101 x696 cross-pillar coincidence workshop (transit×connes, CONVERGED 3 rounds 2026-06-09); JOIN of verdict lines S101-LADDER-COMPOSITION audit=25e63c1a22c77d217e8ea1a708c87e4fee5b63a54e407e55a4fd2d560b4b0e5d (x696_ratio=6.9556) + S101-AF1-MODE-A-ABSOLUTE audit=3f4028964402de700bdc3996b7f636ba25e04e4e860fe15c0a70c607aa7c467e (1/pairing=cocycleVal/metricTrace=6.9489); Sage RF(300)", "gate": None, "superseded": False},

    # SECTION E — S101
    "BF_spine_vs_incumbent_ceiling": {"session": "S101", "source": "s101-bf-spine-reference-class-workshop.md (phonon-first × mack); joins S98-W4-4-OQ3-COVARIANCE audit 0814c57f", "gate": "S98-W4-4-OQ3-COVARIANCE", "superseded": False},

    # SECTION E — S103
    "n_s_FW_sqrt_cutoff": {"session": "S103", "source": "S103-Q28-LAYER2-A6 PASS (COMMIT; A_5->A_6 sixth-regulator atlas-cardinality robustness DISCHARGED; audit_sha256=3ddadf917fac68ad31e06904dbad8b1b28002e4d1c8cbf763a0913101d58372c). Value = S65 BCS+1-loop sqrt-cutoff family (atlas-04 n_s row); the COMMITTED n_s once the S67 sqrt(x) functional selection is functional-selection-robust.", "gate": None, "superseded": False},

    # SECTION E — S105
    "omega_SN_substrate": {"session": "S105", "source": "s105_w2_4_sn_null.npz", "gate": "S105-W2-4-SN-NULL", "superseded": False},

    # SECTION C — S95
    "kappa_exit": {"session": "S95", "source": "S95-W4-2-HAWKING-ANALOG-T-LEDGER row2_exit_a4 (s95_w4_2_hawking_analog_t_ledger.npz; composite=PASS; kappa=47.6146, T=7.5781, corpus=7.578, dev=0.0000, disp=PLACED)", "gate": "S95-W4-2-HAWKING-ANALOG-T-LEDGER", "superseded": False},

    # SECTION E — S96
    "R_S96_matter_hierarchy": {"session": "S96", "source": "S96-MATTER-R-HIERARCHY (s96_matter_r_hierarchy.py; computations/session-96/s96_gate_verdicts.txt)", "gate": None, "superseded": False},

    # SECTION E — S61
    "C2_gen_sectors": {"session": "S61", "source": "S61 W8 (C2(1,1)/C2(1,0)=9/4 confirmation); SU(3) quadratic Casimir C2(p,q)=(p^2+q^2+p*q+3*p+3*q)/3", "gate": None, "superseded": False},

    # SECTION C — S39
    "lambda_B1": {"session": "S39", "source": "atlas-07-permanent-results (S39 GGE Lagrange multipliers; analytic, lambda_k = -ln|psi_pair[k]|^2)", "gate": "INV13-W1-1-GGE-COLLIDER-SQUEEZED-FNL", "superseded": False},

    # SECTION C — S39
    "lambda_B2": {"session": "S39", "source": "atlas-07-permanent-results (S39 GGE Lagrange multipliers; analytic, lambda_k = -ln|psi_pair[k]|^2)", "gate": "INV13-W1-1-GGE-COLLIDER-SQUEEZED-FNL", "superseded": False},

    # SECTION C — S39
    "lambda_B3": {"session": "S39", "source": "atlas-07-permanent-results (S39 GGE Lagrange multipliers; analytic, lambda_k = -ln|psi_pair[k]|^2)", "gate": "INV13-W1-1-GGE-COLLIDER-SQUEEZED-FNL", "superseded": False},

    # SECTION C — S83
    "f_NL_folded": {"session": "S83", "source": "S83 GGE-BISPECTRUM-67 (folded-template amplitude; GGE diagonal CLT, N_pair=59.8; full-precision form of f_NL_FW_S67_folded=0.129)", "gate": "INV13-W1-1-GGE-COLLIDER-SQUEEZED-FNL", "superseded": False},

    # SECTION E — S102
    "f_WZ": {"session": "S102", "source": "§VII.BR c2=0 landing (S102/S103); promotion pending since S102/S103 → landed S110 W0 HK-FWZ", "gate": None, "superseded": False},

    # SECTION E — S62
    "alpha_GUT_FW": {"session": "S62", "source": "SECTOR-ENERGY-RATIO-62; alpha_GUT = pi/(8*f_0), f_0=4.258 (one-loop SA / canonical a_4)", "gate": None, "superseded": False},

    # SECTION E — S70
    "ratio_gilkey": {"session": "S70", "source": "W1-1 atlas-row convention (S70-resolved); a_4/a_2 Gilkey form (atlas-01 S61-62 a_4/a_2=0.414)", "gate": None, "superseded": False},

    # SECTION E — S110
    "deg_T_BZ_pivot": {"session": "S110", "source": "S110-CF-CV6B-DS-M4", "gate": None, "superseded": False},

    # SECTION E — S110
    "tau_NL": {"session": "S110", "source": "S110-CF-AS3-QUENCH-PIN (s110_cf_as3_quench_pin.npz; verdict audit_sha256=60f0d70be57ab57a796303d3eb3b0dbbdbb66c39e2be74b7d6e112f0499efdc1); inv-10 INV10-W2-3", "gate": "S110-CF-AS3-QUENCH-PIN", "superseded": False},

    # SECTION E — S111
    "A_s_FW": {"session": "S111", "source": "s111_cf_as3a_impulse_quench.npz", "gate": "S111-CF-AS3a", "superseded": False},

    # SECTION E — S114
    "chi_q_fold": {"session": "S114", "source": "S43-TWOFLUID-W-43-V2 / S114-CF-S114-CCRESID-CHI-Q-SCALING", "gate": "CF-S114-CCRESID-CHI-Q-SCALING", "superseded": False},

    # SECTION B — S114
    "tau_cross_van_hove": {"session": "S114", "source": "S114-CF-S114-TAUFOLD-CUSP-CROSSING", "gate": "S114-CF-S114-TAUFOLD-CUSP-CROSSING", "superseded": False},

    # SECTION E — S116
    "SC_corr_A": {"session": "S116", "source": "S116-W7 (Greywall 1986 PRB 33 7520 / Serene-Rainer 1983 / Volovik 2003 Ch.7)", "gate": "S116-W7-STATEPROJ-BCS", "superseded": False},

    # SECTION E — S116
    "SC_corr_B": {"session": "S116", "source": "S116-W7 (Greywall 1986 PRB 33 7520 / Serene-Rainer 1983 / Volovik 2003 Ch.7)", "gate": "S116-W7-STATEPROJ-BCS", "superseded": False},

    # SECTION E — S116
    "delta_A_over_kBTc": {"session": "S116", "source": "S116-W7 (Greywall 1986 PRB 33 7520 / Serene-Rainer 1983 / Volovik 2003 Ch.7)", "gate": "S116-W7-STATEPROJ-BCS", "superseded": False},

    # SECTION E — S116
    "delta_B_over_kBTc": {"session": "S116", "source": "S116-W7 (Greywall 1986 PRB 33 7520 / Serene-Rainer 1983 / Volovik 2003 Ch.7)", "gate": "S116-W7-STATEPROJ-BCS", "superseded": False},

    # SECTION E — S116
    "P_pc": {"session": "S116", "source": "S116-W7 (Greywall 1986 PRB 33 7520 / Serene-Rainer 1983 / Volovik 2003 Ch.7)", "gate": "S116-W7-STATEPROJ-BCS", "superseded": False},

    # SECTION E — S116
    "T_pc": {"session": "S116", "source": "S116-W7 (Greywall 1986 PRB 33 7520 / Serene-Rainer 1983 / Volovik 2003 Ch.7)", "gate": "S116-W7-STATEPROJ-BCS", "superseded": False},

    # SECTION E — S116
    "R_3HeB_lit": {"session": "S116", "source": "S116-W7 (S87 W11-5 npz s87_w11_3heb_excess_inheritance_comparison.npz; Greywall 1986 / Serene-Rainer 1983)", "gate": "S116-W7-STATEPROJ-BCS", "superseded": False},

    # SECTION E — S48
    "rho_s_C2": {"session": "S48", "source": "S48-MASS-48", "gate": "MASS-48", "superseded": False},

    # SECTION D — S118
    "c_s_a2curv_GGE_fold": {"session": "S118", "source": "s118_as_cs_substrate_first.npz", "gate": "CF-S118-AS-CS-SUBSTRATE-FIRST", "superseded": False},
}

# ==============================================================================
#  SECTION G: Audit Patterns (consumed by extract_entities.py --audit-constants)
# ==============================================================================

# Each entry: (tag, regex_pattern_string, message)
# The regex matches ASSIGNMENT lines with stale hardcoded values.
# extract_entities.py compiles these at import time.
# To add a new enforced constant: add an entry here. That's it.

import re as _re

AUDIT_PATTERNS = [
    # --- E_cond variants ---
    ("E_cond=-0.115",
     r"^\s*E_(?:cond|BCS_MKK|BCS|bcs)\s*=\s*-?0\.115\b",
     "Stale E_cond (S35 5-mode). Canonical: -0.137 (S36 ED-CONV-36 8-mode)"),
    ("E_cond=-0.156",
     r"^\s*E_(?:cond|BCS_MKK|BCS|bcs)\s*=\s*-?0\.156\b",
     "GL E_cond used as ED value. If ED intended, use canonical -0.137"),
    # --- Volume ---
    ("Vol_SU3=8880",
     r"^\s*\w+\s*=.*\b8880\.9",
     "Wrong Vol(SU(3)) in assignment. Canonical: 1349.74 (Weyl integration formula)"),
    # --- M_KK ---
    ("M_KK=1e16",
     r"^\s*M_KK\s*=\s*1e16\b",
     "Rounded M_KK. Canonical: 7.43e16 (gravity route, S42)"),
    # --- Planck mass ---
    ("M_Pl=2.435e18",
     r"^\s*M_(?:P|Pl|Planck|PL_REDUCED|Pl_reduced)\s*=\s*2\.435e18\b",
     "Hardcoded M_Pl. Use: from canonical_constants import M_Pl_reduced"),
    ("M_Pl=1.22e19",
     r"^\s*M_(?:P|Pl|Planck|Planck_GeV)\s*=\s*1\.22\d*e19\b",
     "Hardcoded M_Pl. Use: from canonical_constants import M_Pl_unreduced"),
    # --- BCS coherence / instanton ---
    ("xi_BCS=0.808",
     r"^\s*xi_BCS\s*=\s*0\.808\b",
     f"Low-precision xi_BCS. Canonical: {xi_BCS} (s37_instanton_mc)"),
    ("S_inst=0.069",
     r"^\s*S_inst\s*=\s*0\.069\b",
     f"Low-precision S_inst. Canonical: {S_inst} (s37_instanton_mc)"),
    ("Delta_0=0.77",
     r"^\s*Delta_0\s*=\s*0\.77\d*\b",
     f"Hardcoded Delta_0. Use: from canonical_constants import Delta_0_GL"),
    ("Delta_BCS=0.52",
     r"^\s*Delta_BCS\s*=\s*0\.52\b",
     "Stale Delta_BCS=0.52 (was eps_fold[3], not BCS gap). Canonical: 0.4643 (Delta_0_OES). "
     "Use: from canonical_constants import Delta_BCS"),
    # --- Transit / dynamics ---
    ("G_DeWitt=5",
     r"^\s*G_(?:DeWitt|mod)\s*=\s*5\.0\b",
     "Hardcoded G_DeWitt. Use: from canonical_constants import G_DeWitt"),
    ("H_fold=586",
     r"^\s*H_fold\s*=\s*586\.5\b",
     f"Hardcoded H_fold. Use: from canonical_constants import H_fold"),
    # --- Fabric ---
    ("N_cells=32",
     r"^\s*N_cells\s*=\s*32\b",
     "Hardcoded N_cells. Use: from canonical_constants import N_cells"),
    # --- tau_fold ---
    ("TAU_FOLD=0.19",
     r"^\s*TAU_FOLD\s*=\s*0\.19",
     "Hardcoded TAU_FOLD. Use: from canonical_constants import tau_fold as TAU_FOLD"),
    # --- Observational constants ---
    ("ALPHA_EM_MZ_INV=127",
     r"^\s*ALPHA_EM_MZ_INV\s*=\s*127",
     "Hardcoded ALPHA_EM_MZ_INV. Use: from canonical_constants import alpha_em_MZ_inv"),
]

# Pre-compiled for direct use (extract_entities imports this)
AUDIT_PATTERNS_COMPILED = [
    (tag, _re.compile(pat), msg) for tag, pat, msg in AUDIT_PATTERNS
]

# ---------------------------------------------------------------------------
# Heuristic: detect "potential hardcode" — assignments that LOOK like physics
# constants but aren't in the canon. Catches agents inventing new constants
# without updating canonical_constants.py.
# ---------------------------------------------------------------------------

# All numeric constant names exported by this module (auto-collected)
_CANON_NAMES = frozenset(
    k for k, v in dict(globals()).items()
    if isinstance(v, (int, float)) and not k.startswith("_")
)

# Regex: looks like a physics constant assignment.
# Matches scientific notation (2.435e18) OR plain decimals with a dot (50.945, 0.137).
# Plain integers without a dot are excluded (too many false positives).
_RE_POTENTIAL_HARDCODE = _re.compile(
    r"^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*"    # capture name
    r"-?\d+\.\d+"                               # decimal with dot (e.g. 50.9, 0.137)
    r"(?:[eE][+-]?\d+)?\s*"                     # optional exponent
    r"(?:#.*)?$",
    _re.IGNORECASE
)

# Names that are obviously NOT physics constants
_HARDCODE_IGNORE_NAMES = frozenset({
    # Single-letter
    "i", "j", "k", "m", "n", "p", "q", "r", "s", "t", "x", "y", "z",
    "a", "b", "c", "d", "f", "g", "l", "u", "v", "w",
    # Common non-constant assignments
    "idx", "fig", "ax", "dpi", "fontsize", "figsize", "lw", "ms",
    "npts", "n_pts", "n_points", "n_steps", "n_grid", "n_tau", "n_modes",
    "n_samples", "n_iter", "max_iter", "tol", "rtol", "atol", "eps",
    "step", "dt", "dx", "ds",
    "err", "res", "val", "tmp", "out", "result", "status", "flag",
    "verbose", "debug", "seed", "offset", "limit", "count", "total",
    "width", "height", "size", "dim", "rank", "order", "degree",
    "idx_fold", "idx_min", "idx_max", "fold_idx",
    # --- Script-local values whitelisted by S45 audit (not universal constants) ---
    # NOTE: all entries must be lowercase (audit checks name.lower() against this set)
    # 777 names whitelisted (683 from audit + 94 prior)
    "a0_sum", "a0_total", "a2_berry", "a2_sum", "a2_t", "a2_total", "a4_sum", "a4_t",
    "a4_total", "a_a", "a_above", "a_bao", "a_bao_phys", "a_below", "a_f", "a_final",
    "a_i", "a_init", "a_s_matter", "a_vdn", "alpha1_mz_inv", "alpha2_mz_inv", "alpha_1_mz_inv", "alpha_2_mz_inv",
    "alpha_b1", "alpha_b2", "alpha_b3", "alpha_band", "alpha_s", "alpha_s_mz", "alpha_s_planck", "alpha_s_sigma",
    "alpha_v", "alpha_vdn", "atomic_clock_bound", "b2_bandwidth", "b2_bw", "b2_e_fold", "b2_overlap", "b2_split",
    "b_a", "b_err", "b_first", "b_m", "b_measured", "b_run", "bar_width", "barrier_a",
    "barrier_c", "barrier_d", "barrier_e", "baseline_m_max", "bcs_window", "berry_peak_threshold", "best_dev", "best_dist",
    "best_product", "best_r2", "best_r_sin2", "beta_anal", "beta_check", "beta_detail", "beta_eff", "beta_gate",
    "beta_gibbs", "beta_ising", "beta_rsd", "beta_sff", "beta_v", "beta_vdn", "bf_net", "bin_width",
    "br_formation_b1", "br_formation_b2", "br_formation_b3", "bullet_cluster_bound", "c_1", "c_fabric_a", "c_mw", "c_nat",
    "c_nfw", "c_ngc", "c_uv", "cdf_gauge", "cdf_grav", "cell_height", "center_phi", "center_theta",
    "chi_pass", "clock_coeff", "cmb_bound", "cmbs4_sigma", "collective_strength", "continuum_strength", "cross_check_tol", "cross_ent",
    "ct4_impedance", "d2a2_dtau2", "d2s", "d2s_bare", "d2s_from_c", "d2s_phys", "d2s_total", "d3s_fold",
    "d4s_fold", "d_a_mpc", "d_inst_dtau", "d_kk", "d_perl", "d_ratio", "d_shell", "ddda_init",
    "de_dtau", "degeneracy_tol", "delta2_zeta_obs", "delta_0", "delta_0_bcs", "delta_0_c", "delta_a0_final", "delta_alpha_per_domain",
    "delta_bcs", "delta_c", "delta_d", "delta_eta_chiral", "delta_frac", "delta_gorkov", "delta_max", "delta_min",
    "delta_new", "delta_nl", "delta_out", "delta_pair", "delta_primordial", "delta_tau", "delta_tau_bcs", "delta_tau_over_tau",
    "delta_tau_sector", "delta_tau_wall", "delta_v", "delta_v_0", "delta_w_framework", "desi_xi_precision", "dimflow_ds_sig1", "dkl_opt",
    "dkl_single_mode", "domega", "dr", "dr_arith", "dr_c", "dr_channel", "dr_cum_30", "dr_d",
    "dr_p", "dr_prop_cross", "dr_s", "dr_uncoupled", "ds_plot", "ds_ref", "ds_small", "ds_total",
    "dsigma", "dt_dwell", "dt_rep", "dtau_fd", "dtau_num", "dtau_transit", "dwell_od", "e0_sq",
    "e_bcs_fold", "e_cond", "e_cond_bcs", "e_cond_old", "e_cond_peak", "e_cond_task", "e_cross", "e_diag",
    "e_field", "e_kk_avg", "e_ref", "e_scalar", "e_smooth_weyl", "e_vac_discrete", "e_vac_final", "e_vac_test",
    "eih_combined", "eih_singlet_ratio", "enhancement_3x3", "enhancement_8x8", "eps_large", "eps_scan", "eps_small", "eps_target",
    "eps_test", "epsilon_cp", "epsilon_crossover", "epsilon_h", "epsilon_h_planck", "epsilon_small", "eta_1", "eta_default",
    "eta_eigen_max", "eta_est", "eta_frac", "eta_framework", "eta_from_lattice", "eta_ising", "eta_k7_val", "eta_primary",
    "eta_reg", "eta_reg_frac", "eta_round", "eta_t", "f0_pow", "f4_implied", "f_b2", "f_eih",
    "f_finesse", "f_nl", "f_nl_deltan", "f_nl_modulated", "f_pair", "f_safe_gauge", "f_sky", "f_sum",
    "f_total", "f_tracelog", "f_vol_1", "f_walls_frozen", "f_walls_rh", "face_width_frac", "fail_delta", "fd_step",
    "fiber_collision_scale", "fold_tau", "fom_void_only", "frac_0", "frac_well", "g_dewitt", "g_fs_bcs_fold", "g_mod",
    "g_star", "g_star_bbn", "g_star_rh", "gamma_fit", "gamma_linder", "gamma_mf", "gamma_vh", "gap_015",
    "gap_b2_b3", "gap_closure_threshold", "gate_criterion_threshold", "gate_threshold", "gauge_a0", "gauge_zeta2", "gcm_reg_threshold", "gpv_omega",
    "gpv_power", "h0", "h2", "h_0", "h_bbn", "h_bcs", "h_fd", "h_hubble",
    "ht_0", "imp_defensible_lo", "imp_physical", "impedance", "impedance_factor", "impedance_from_overlap", "inv_16pig_obs", "k7_sum",
    "k_eq", "k_max", "k_min", "k_nl_max", "k_pivot", "k_pivot_gev", "k_pivot_mpc", "k_ref_mpc",
    "k_silk", "k_zoom_max", "kinetic_threshold", "kpc_per_mpc", "ksw_den", "ksw_num", "l_abs_mpc", "l_absorber_mpc",
    "l_arm", "l_box", "l_full", "l_giant", "l_gpc", "l_hcbgw", "l_hubble_m", "l_narrow",
    "l_ref", "l_test", "lam", "lambda", "lambda_b1", "lambda_b2", "lambda_b3", "lambda_ce",
    "lambda_cutoff", "lambda_fs_correct", "lambda_laser", "lambda_plot", "lambda_ref", "lambda_sa", "lambda_standard", "lambda_test",
    "lifshitz_tau", "ln_lambda", "ln_t", "ln_term", "lnt_sum", "local_half_width", "log10_mkk_max", "log10_mkk_min",
    "log_det_b", "log_det_f", "log_lik_gge", "log_lik_gibbs_opt", "log_lik_gibbs_stored", "log_prob", "log_scale", "log_supp",
    "lv_beta_norm", "lyman_alpha", "m1_max_width", "m2_max_width", "m_200_cluster", "m_200_mw", "m_200_ngc", "m_atdhfb_cross_fold",
    "m_atdhfb_diag_fold", "m_atdhfb_fold", "m_atdhfb_frozen_fold", "m_bh", "m_bh_err", "m_constrained_8x8", "m_constrained_b2", "m_disk_mw",
    "m_disk_ngc", "m_gas_ngc", "m_gut_typical", "m_h", "m_higgs", "m_ib_cross_fold", "m_ib_diag_fold", "m_ib_fold",
    "m_ib_frozen_fold", "m_kk_a", "m_kk_c", "m_kk_gauge", "m_kk_gev", "m_kk_grav", "m_kk_kerner", "m_kk_max_firas",
    "m_kk_max_webb", "m_kk_natural", "m_max_auth", "m_max_baseline", "m_max_blocked", "m_max_ref", "m_pl_eff", "m_sol",
    "margin_param", "mass_floor", "match_tol", "merge_tol", "mkk_a", "mkk_best", "mkk_c", "mkk_firas_cross",
    "mmax_calibration", "mmax_threshold", "mpc", "mpc_in_gev_inv", "ms_factor", "ms_relaxed", "mu", "mu_crit",
    "mu_ref_sq_mkk", "multi_sector_factor", "near_crossing_threshold", "non_collective_strength", "non_thermality", "np_dr2", "npair_thermal", "ns_fail_high",
    "ns_fail_low", "ns_from_lattice", "ns_lifshitz", "ns_pass_high", "ns_pass_low", "ns_planck", "ns_planck_sigma", "ns_round",
    "ns_s", "ns_sigma", "ns_t", "nu", "nu_3d", "nu_bcs", "nu_exp", "nu_kz",
    "nu_mf", "nu_xy", "ob", "offset_step", "ol", "om", "om_m", "omega_breathe",
    "omega_check", "omega_de_obs", "omega_dm_obs", "omega_first", "omega_gpv", "omega_k", "omega_l", "omega_lambda0",
    "omega_lambda_0", "omega_lambda_obs", "omega_m0", "omega_m_0", "omega_max", "omega_osc", "omega_qrpa_b2", "omega_tau",
    "omega_vh_center", "omega_zc", "p_avg", "p_constrained", "p_constrained_hi", "p_constrained_lo", "p_even", "p_laser",
    "p_odd", "p_prior", "p_r_obs", "p_structural_floor", "pass_l", "pb_omega", "pb_power", "pc_per_kpc",
    "perlman_2011_arcsec", "perlman_2019_arcsec", "phi_bao", "phi_gap", "phi_paasch", "phi_small", "planck_central", "planck_sigma",
    "pole_strength", "post_transit_ratio", "pr_b2", "q_b2_envelope", "q_best", "q_c", "q_factor", "q_max",
    "q_step", "q_td", "quasar_bound", "quasar_precision", "r8", "r_1_high", "r_1_low", "r_8",
    "r_b2_flatband", "r_bare", "r_bicep", "r_bicep_limit", "r_cell", "r_cell_kk", "r_cmbs4", "r_core_sidm_kpc",
    "r_d_mw", "r_d_ngc", "r_drag", "r_edge", "r_fold", "r_gas_ngc", "r_goe", "r_gue",
    "r_inter", "r_litebird", "r_mean_astra", "r_pdg", "r_s", "r_s43", "r_s44", "r_s_mpc",
    "r_singlet", "r_sm_kk", "r_sol_kpc", "r_star", "r_star_astra", "r_test", "r_upper_bound", "rad_to_arcsec",
    "rate_kk", "rate_minus", "rate_plus", "ratio_1d_volovik", "ratio_2a_bose", "ratio_2b_fermi", "ratio_b_10mkk", "ratio_e3",
    "ratio_gap_split", "ratio_jk", "ratio_oes", "ref_cutoff", "rho_b1", "rho_b1_s34_per", "rho_b1_step", "rho_b2_step",
    "rho_b3_step", "rho_crit", "rho_full_w2", "rho_gge", "rho_obs_standard", "rho_peak", "rho_per_mode", "rho_physical",
    "rho_residual_final_spectral", "rho_sa_phys", "rho_smooth", "rho_vac_mkk4", "rho_vh", "rho_wall2", "rp_1mpc", "s180",
    "s210", "s23_2", "s34_impedance", "s_0", "s_actual_pre", "s_b2_analytic", "s_dump", "s_ent",
    "s_full", "s_gge", "s_gge_bits", "s_gge_check", "s_gge_nats", "s_gibbs_bits", "s_h_vz_10hz", "s_inst_a",
    "s_inst_analytic_a", "s_inst_analytic_d", "s_inst_best", "s_inst_c", "s_inst_e", "s_inst_max", "s_inst_mean", "s_inst_min",
    "s_p", "s_recomp", "s_reg", "s_total", "scalar_a0", "scalar_zeta2", "shell_gap", "sidm_limit",
    "sigma8_planck", "sigma_8_0", "sigma_alpha", "sigma_alpha_th", "sigma_bao", "sigma_bcs", "sigma_bins", "sigma_boundary",
    "sigma_crit", "sigma_etot", "sigma_fs", "sigma_gn_log10", "sigma_l_achieved", "sigma_meas", "sigma_meas_con", "sigma_meas_opt",
    "sigma_model", "sigma_over_m", "sigma_pair", "sigma_rv_frac", "sigma_vh", "sigma_w0_desi", "sigma_w_euclid", "sigma_wa_desi",
    # SUPERSEDED-BY-CANONICAL (S101-HK-PMNS-PIN-PROMOTION): the PMNS sin^2(theta_12)/sin^2(theta_13)
    # values are now first-class canonical pins -- sin2_theta12_PDG=0.307, sin2_theta13_PDG=0.0220
    # (the W5-2-consumed PDG/NuFit-5.x-style NO centrals) and sin2_theta12_NuFit60=0.303,
    # sin2_theta13_NuFit60=0.02225 (the true NuFit-6.0 IC19+SK NO centrals). New scripts MUST import
    # those version-tagged names, NOT hardcode the values. The tokens sin2_12_pdg / sin2_13_pdg are
    # RETAINED below (removing them would flip the legacy-audit status of frozen pre-S101 landed
    # scripts that hardcoded these values, e.g. s100a_d5_0nubb_majorana.py # (local) pins); the
    # annotation closes the silent-hardcode path for FUTURE scripts. sin2_23_pdg is OUT OF SCOPE
    # (theta_23 was not consumed by the W5-2 electron-row gate; not promoted; token untouched).
    "sigma_xi_scaled", "sigma_zp", "sin2_12_pdg", "sin2_13_pdg", "sin2_23_pdg", "sin2_thetaw_0", "sin2_thetaw_mz", "singlet_e_b",
    "singlet_frac_c_acoustic", "singlet_frac_c_compound", "singlet_frac_d2_c_compound", "snr_bao_desi", "soliton_integral", "stellar_pop_precision_jwst", "sum_pdag_blocked", "suppression_sh",
    "systematics_current", "t0i", "t0i_gge", "t0i_total", "t_bcs", "t_clean_variation", "t_cryogenic", "t_doorway",
    "t_first_cross", "t_fit_min", "t_gibbs", "t_gibbs_mkk", "t_hubble_mkk", "t_max", "t_over_thetad", "t_ref",
    "t_scram", "t_settle", "t_therm", "t_therm_mkk", "t_total", "t_transit", "t_zoom", "target_ds",
    "target_lmax", "target_ns", "target_range", "tau", "tau_0", "tau_0_bcs", "tau_a", "tau_b",
    "tau_bcs_high", "tau_bcs_low", "tau_c", "tau_cal", "tau_check", "tau_conj", "tau_end", "tau_false",
    "tau_final", "tau_fold", "tau_fold_val", "tau_gate", "tau_init", "tau_max", "tau_min", "tau_plot",
    "tau_q", "tau_q_raw", "tau_ref", "tau_ref_small", "tau_start", "tau_target", "tau_test", "tau_wall_hi",
    "tau_wall_lo", "tau_window", "tcmb", "term_4_local", "term_a4", "theta_12", "theta_23", "third_moment",
    "threshold", "threshold_fail", "threshold_pass", "tij", "tij_gge", "tl", "tol_default", "total_dec",
    "total_e_b", "total_eta0", "total_eta_log", "total_gradient", "total_inc", "total_sq", "tr_riem_endo", "v_b1b2_spinor",
    "v_b2_avg", "v_b2b2_c2_max", "v_b2b2_full_max", "v_b2b2_max", "v_b2b2_spinor", "v_b2b3_spinor", "v_b_proj", "v_b_std",
    "v_cdm_threshold", "v_desi", "v_eff", "v_eff_desi", "v_eff_dr2", "v_f", "v_fs", "v_gap_gap",
    "v_infall_z100", "v_kosmann_frame_v", "v_kosmann_spinor", "v_mid", "v_min", "v_min_physical", "v_neg_neg", "v_pos_neg",
    "v_pos_pos", "v_s38", "v_start", "v_survey", "v_t_sign", "v_terminal", "v_transit_phys", "vdn_factor",
    "vh_delta", "vh_spacing_threshold", "void_bias", "vol_su3", "w0_desi", "w0_desi_err", "w0_framework", "w0_pred",
    "w12_gap", "w_a_cpl", "w_b2", "w_eos", "w_gge", "w_minus_total", "w_n", "w_narrow",
    "w_osc_quadratic", "w_plus_total", "w_vac", "wa_desi", "wa_desi_err", "wa_framework", "wa_pred", "width_sec",
    "x_final", "x_max", "x_max_default", "x_max_high", "x_pos", "x_start", "xi_bcs", "xi_kz",
    "xi_kz_com_mpc", "xi_wall", "y_start", "z_3d", "z_dyn", "z_eff", "z_eig_sum", "z_exp",
    "z_fold_fabric", "z_formation", "z_halo", "z_kz", "z_max", "z_s", "z_s42", "z_spectral",
    "z_star", "z_tet", "z_tetrad", "z_xy", "z_xy_relax", "zero_mode_index", "zeta2_sc", "zeta_2",
    "zeta_3",
    # --- Post-S45 script-local gate-pins (not universal constants) ---
    # Per computations/_shared/CLAUDE.md "When to use # (local): Gate thresholds
    # specific to this script": these are single-gate pre-registered pins, not shared
    # framework constants. Whitelisted here (same mechanism as the S45 script-local
    # block above) rather than re-tagging the committed, already-verdicted producers.
    "plan_defect_bare", "plan_defect_fluct",  # s100b_w2_2_ps_variant_id.py PS closure-pair pins
    "tau_consistency",                         # s104_w4_1_nonlinear_memory_ir_slope.py gate-(ii) band
})

# Names starting with these prefixes are likely local, not constants
_HARDCODE_IGNORE_PREFIXES = ("_", "fig", "ax", "plt", "color", "label", "fmt",
                              "n_", "num_", "max_", "min_", "idx_")

# Session floor: scripts at or below this session number are exempt (historical)
AUDIT_SESSION_FLOOR = 34

# Scripts that intentionally reference old values (audit/correction scripts)
AUDIT_EXEMPT_SCRIPTS = frozenset({
    "canonical_constants.py",
    "s44_constants_corrected.py",
    "s44_mkk_reconcile.py",
    "s44_cc_gap_audit.py",
    "s38_attempt_freq.py",        # S_inst=0.069 appears only in print-statement text, not assignment
    "s43_spectral_dissolution.py", # M_P=1.221e19 appears only in print-statement text, not assignment
})

# ==============================================================================
#  SECTION H: Migration Helper
# ==============================================================================

def warn_stale(name, value, tolerance=0.01):
    """Check a hardcoded value against the canonical constant.

    Usage in migration:
        from canonical_constants import E_cond, warn_stale
        E_cond_local = -0.115  # old hardcoded value
        warn_stale("E_cond", E_cond_local)  # warns if >1% off
    """
    canonical = globals().get(name)
    if canonical is None:
        warnings.warn(f"canonical_constants: '{name}' not found in module", stacklevel=2)
        return
    if isinstance(canonical, (int, float, np.floating)):
        if abs(canonical) > 0:
            frac = abs(value - canonical) / abs(canonical)
        else:
            frac = abs(value - canonical)
        if frac > tolerance:
            warnings.warn(
                f"canonical_constants: '{name}' = {value} differs from canonical "
                f"{canonical} by {frac*100:.1f}% (>{tolerance*100:.0f}% threshold)",
                stacklevel=2
            )


# ==============================================================================
#  __main__: Validate against authoritative NPZ files (PROVENANCE-DRIVEN)
#
#  Uses the PROVENANCE dict to determine WHICH NPZ file is authoritative for
#  each constant. No blind scanning — only checks what PROVENANCE says to check.
#  Add a constant + PROVENANCE entry and it auto-validates. Nothing else to touch.
# ==============================================================================

# ══════════════════════════════════════════════════════════════════════════════
# Standard Model particle masses & couplings (PDG 2024)
# Added S72: these were hardcoded in 3-16 scripts each
# ══════════════════════════════════════════════════════════════════════════════
v_ew = 246.0                   # GeV, electroweak VEV
m_H_obs = 125.1                # GeV, observed Higgs mass — ATLAS+CMS Run-1 combined 125.09 +/- 0.24 (arXiv:1503.07589) rounded to 125.1; NOT PDG-2024 (125.25 +/- 0.17). LOAD-BEARING denominator: 131.8/125.1-1 = 67/1251 exact, 134.0/125.1-1 = 89/1251 exact. See PROVENANCE dict + CF-S104-MH-OBS-REPIN. (corrected attribution 2026-06-12 mack)
m_t_pole = 172.69              # GeV, top quark pole mass (PDG 2024)
m_b_pole = 4.78                # GeV, bottom quark pole mass (PDG 2024)
m_b_1S = 4.18                  # GeV, bottom quark 1S mass (PDG 2024)
m_mu = 0.1056583745            # GeV, muon mass (PDG 2024)
m_e = 5.10998950e-4            # GeV, electron mass (PDG 2024; CODATA 0.51099895000 MeV). Added S98 W3-1 for the charged-lepton Yukawa hierarchy band (S98-W3-1-YUKAWA-EPS-LX-BETWEEN-GEN). NOT the RGE-run Yukawa-at-M_KK value; PDG pole-mass scale (consistent with m_mu).
alpha_s_MZ_obs = 0.1180        # alpha_s(M_Z) observed (PDG 2024). QCD strong coupling at M_Z. NOT to be conflated with inflationary alpha_s (see alpha_s_inflation_framework). Disambiguation: S85-W1c-CANONICAL-CONSTANTS-ALPHA-S-DISAMBIGUATION-PATCH.
g_star_SM = 106.75             # SM relativistic dof above EW scale
g_star_BBN = 10.75             # SM relativistic dof at BBN (photons + 3 neutrinos + e+/-)
N_eff_SM = 3.044               # SM N_eff (3 neutrinos + non-instantaneous decoupling)

# SM beta function coefficients (one-loop, SU(3)_c x SU(2)_L x U(1)_Y)
b1_SM = 41.0 / 10.0            # U(1)_Y (GUT normalized)
b2_SM = -19.0 / 6.0            # SU(2)_L
b3_SM = -7.0                   # SU(3)_c (asymptotic freedom)

# ══════════════════════════════════════════════════════════════════════════════
# Framework observational predictions (scheme-independent)
# Added S72: hardcoded in 4-11 scripts each
# ══════════════════════════════════════════════════════════════════════════════
w0_FW = -0.918                 # Framework w_0 from Volovik vacuum + effacement (S58)
wa_FW = 0.0                    # Framework w_a = 0 (four-fold locked, S58)
w0_LCDM = -1.0                 # LCDM reference
wa_LCDM = 0.0                  # LCDM reference
planck_ns = 0.9649             # Planck 2018 TT,TE,EE+lowE+lensing central value
planck_ns_err = 0.0042         # Planck 2018 1-sigma
planck_alpha_s = -0.0045       # LEGACY Planck-2018 pin; superseded by alpha_s_canon_2020 per S86-W13 P12. Use alpha_s_canon_2020 for new computation scripts. Inflationary running of the scalar spectral index. NOT to be conflated with QCD alpha_s(M_Z) (see alpha_s_MZ_obs). Disambiguation: S85-W1c-CANONICAL-CONSTANTS-ALPHA-S-DISAMBIGUATION-PATCH.
planck_alpha_s_err = 0.0067    # LEGACY Planck-2018 1-sigma on alpha_s; superseded by alpha_s_canon_2020_err per S86-W13 P12.

# ── S86 W13 P12: alpha_s canonical-pin update (Aiola 2020 ACT DR4 + Planck) ──
# Provenance: S85 W1b-8 FAIL surfaced that planck_alpha_s = -0.0045 (Planck 2018) is
# stale relative to post-2018 real data. Aiola+ 2020 (ACT DR4 + Planck combined,
# Table 5 col 3) reports alpha_s = +0.0023 +/- 0.0063, a sign-flip. Updated per
# S86-W13 P12 ALPHA-S-CANONICAL-UPDATE; legacy planck_alpha_s retained for back-compat.
# Substitution chain (Python-verified):
#   gap_old = planck_alpha_s - alpha_s_inflation_framework = -0.0045 - (-0.068968) = +0.064468
#   gap_new = alpha_s_canon_2020 - alpha_s_inflation_framework = +0.0023 - (-0.068968) = +0.071268
#   n_sigma_old = 0.064468 / 0.0067 = 9.622
#   n_sigma_new = 0.071268 / 0.0063 = 11.312
#   Delta(n_sigma) = +1.690  (tension WIDENS; framework prediction UNCHANGED)
alpha_s_canon_2020 = +0.0023        # ACT DR4 + Planck combined (Aiola+ 2020); post-2018 canonical pin (S86 W13 P12)
alpha_s_canon_2020_err = 0.0063     # Aiola+ 2020 1-sigma on alpha_s
alpha_s_canon_2020_source = "Aiola+ 2020 (ACT DR4 + Planck combined)"
alpha_s_canon_2020_session = "S86 W13 P12"

# ── S85 W1c-1: alpha_s disambiguation block ──
# Framework S50-51 identity prediction for INFLATIONARY alpha_s = dn_s/dlnk.
# Provenance: S50-51 derivation; interpretation-commit W1c-2 (2026-04-23).
# Current: n_s_canon=0.9649, yields -0.068968.
# Planck 2018 observed: -0.0045 +/- 0.0067.
# Magnitude gap 15.3x; separation 9.62 sigma. See W1c-5 registry landing.
# Aliases below let plan-notation `n_s_canon` resolve and let gate scripts
# import `alpha_s_framework_central` as the canonical framework handle.
n_s_canon = planck_ns          # alias: plan-notation n_s_canon = 0.9649 (S85 W1c-1)
alpha_s_inflation_framework = n_s_canon**2 - 1  # SUPERSEDED (S92 AH-TR-1; see PROVENANCE) — identity@OBSERVED-pivot, NOT a substrate observable. Framework S50-51 identity, W1c-2 commit.
alpha_s_framework_central = alpha_s_inflation_framework  # SUPERSEDED (S92 AH-TR-1; see PROVENANCE) — new gate scripts use alpha_s_substrate_distance_1 / alpha_s_pivot_goldstone. Canonical handle (S85 W1c-1)
Q_Leggett = 6.7e5              # Leggett mode quality factor (S50 LEGGETT-DAMPING-50)

# ── S87 W8 promotions (Class-8.3 publication-precision floor closures) ──
# Provenance: S87 W8-2 (max_pair_ratio_A_5) + S87 W8-8 (gv_canonical_difference)
# Both promotions FIX-IN-SESSION per `feedback_fix-in-session-never-defer.md`
# in response to user no-technical-debt rule application: hygiene constants
# that close Class-8.3 publication-precision floors on future re-invocations
# (downstream verifiers compare full-float64 against full-float64; previous
# 6-sig-fig and 14-sig-fig anchors structurally guaranteed false-FAILs/INFOs).
max_pair_ratio_A_5_FW = 9.240438549812e-01  # A_5 max-pair-ratio extremum at (zeta, Zubarev); was_cutoff_sqrt_extremal_in_A5=False ⇒ A_5=A_4 at full float64; from s87_w8_w4_2_re_run_under_a_4.npz (S87 W8-2)
gv_canonical_difference_FW = -40579.1500479506  # GV-Heitsch invariant difference on (C_H, C_epsH) parity-twin pair at canonical regulator; full float64 from s84_w10a_115_gv_explicit.npz; W-11 §3 anchor; reaffirmed regulator-INDEPENDENT across A_5_extended at S87 W8-8

# ── S81 promotions (from PRU audit sweep; observational + framework) ──
# Provenance: _batch_tag_locals.py identified these appearing in >=3 scripts
# with consistent values. Promoted to canonical to drive PRU(a) -> 0.
ns_framework = 0.9595          # SUPERSEDED by n_s_framework=0.9561 (S88 W-15; see PROVENANCE). Framework-predicted n_s (S65 BCS+one-loop, S68 W2-B, S69 W3-D)
ns_framework_err = 0.0         # Framework prediction is deterministic from spectral triple
k_pivot_planck = 0.05          # Planck CMB pivot scale, Mpc^{-1}
z_eq_planck = 3387             # Matter-radiation equality redshift, Planck 2018
r_GOE_canonical = 0.5307       # Wigner surmise <r> for Gaussian Orthogonal Ensemble (random matrix theory)
r_POISSON_canonical = 0.3863   # Wigner surmise <r> for Poisson (integrable) level statistics

# ── S83 W3-G61 promotion (CMB pivot e-fold count; c_s correction) ──
# Provenance: S82 W-1 Wrap-Up #10. Used in s83_w2_g7, s83_w2_g16 with # (local).
# Derivation: N_pivot^substrate = 55 + ln(c/c_s) = 55 + ln(1/1.137e-4) = 55 + 9.08 = 64.08.
# The substrate horizon-crossing is bounded by c_s (phononic sound speed), not c,
# so the CMB pivot occurs 9.08 e-folds LATER (more e-folds since fold) than LCDM.
N_pivot = 64.08                # CMB pivot e-fold count on substrate; S82 W-1 #10, gate S83-N-PIVOT-CS-CANONICALIZATION

# ══════════════════════════════════════════════════════════════════════════════
# S84 promotions: LiteBIRD + CMB-S4 detector specifications
# Provenance: LiteBIRD Collaboration (Hazumi+ 2020 arXiv:2007.12538; PTEP 2023,
# 042F01 Table 3); CMB-S4 Science Book 1st Ed. (arXiv:1610.02743) + DSR 2022.
# Added for S84-LB-CMBS4-JOINT-SIGMA-NT (§W4-37) — Fisher joint on (r, n_T, A_lens).
# ══════════════════════════════════════════════════════════════════════════════
# LiteBIRD (launch 2032; 3-year baseline mission)
sigma_LB_3yr_uKarcmin = 2.16   # LiteBIRD post-component-separation BB noise at 3 yr (μK-arcmin; Hazumi+2020)
beam_LB_arcmin = 30.0          # LiteBIRD effective BB beam at ell<200 (arcmin; PTEP 2023, 042F01)
f_sky_LB = 0.70                # LiteBIRD sky fraction after Galactic mask (PTEP 2023)
delens_LB = 0.50               # LiteBIRD residual lensing fraction after internal+Planck delensing (50%)
ell_min_LB = 2                 # LiteBIRD B-mode multipole floor (reionization bump)
ell_max_LB = 300               # LiteBIRD B-mode multipole ceiling (recombination bump + tail)

# CMB-S4 (2030-2032 deployment; full-survey projection)
sigma_S4_uKarcmin = 1.0        # CMB-S4 effective deep-survey BB noise (μK-arcmin; Science Book + DSR 2022)
beam_S4_arcmin = 30.0          # CMB-S4 large-aperture effective BB beam for tensor analysis (arcmin)
f_sky_S4 = 0.40                # CMB-S4 deep-patch sky fraction (deep region + BICEP-legacy overlap)
delens_S4 = 0.90               # CMB-S4 delensing efficiency (90%; DSR internal delensing target)
ell_min_S4 = 50                # CMB-S4 B-mode multipole floor (large-aperture ground-based cutoff)
ell_max_S4 = 3000              # CMB-S4 B-mode multipole ceiling (delensing-limited high-ell)

# ══════════════════════════════════════════════════════════════════════════════
# Spectral functional f-moments (scheme-dependent, for reference)
# Added S72: hardcoded in 3-5 scripts each; values depend on cutoff choice
# ══════════════════════════════════════════════════════════════════════════════
f_0_sharp = 1.0                # f_0 for sharp cutoff f(x) = Theta(1-x)
f_2_default = 2.34             # f_2 from S62 W1 constraint (Gaussian cutoff)
f_4_default = 0.558            # f_4 from S62 (Gaussian cutoff)

# NPZ key name differs from module name in some files. This maps npz_key -> module_name.
# Only needed when the NPZ was saved with a different key name than the module constant.
_NPZ_KEY_ALIAS = {
    "config_4_E_cond": "E_cond_ED_8mode",
    "config_1_E_cond": "E_cond_ED_5mode",
    "E_cond_full":     "E_cond_ED_8mode",
    "M_KK_from_GN":    "M_KK_gravity",
    "OOM_diff":         "OOM_diff_MKK",
    "Delta_0":          "Delta_0_GL",
    "S_inst_D":         "S_inst",
    "Delta_OES":        "Delta_0_OES",
    "omega_plus":       "omega_PV",
    "Kapitza_Langer":   "Kapitza_ratio",
}
# Reverse: module_name -> npz_key (for PROVENANCE-driven lookup)
_MODULE_TO_NPZ_KEY = {v: k for k, v in _NPZ_KEY_ALIAS.items()}


# ══════════════════════════════════════════════════════════════════════════════
# S85 W6 promotions: sp-origin wave constants (geometric structural boundary)
# Provenance: plan session-85-plan-w6.md §W6-1..7; MEMORY.md modulus-space
# organizational diagram (schwarzschild-penrose-geometer); phononic-framing.md
# canonical substrate-language table; S48 phase-trans verdict; S69 surface
# gravity; S70 BCS-GAP-CANONICAL; S77-S84 CMPP transit-invariance closure.
# ══════════════════════════════════════════════════════════════════════════════
L_max_canonical = 10           # Canonical Peter-Weyl truncation (S77+ standard; plan W6-3/5/7)
tau_dump = tau_fold            # Dump point alias (MEMORY.md: both at 0.19; volume-preserving Jensen)
tau_phase_trans = 0.53723065   # Geometric phase transition (S48 C^2 sectional K=0; MEMORY.md)
tau_overshoot = 1.614          # S77 overshoot turnaround (K=53.35, Type D static; MEMORY.md)
tau_NEC = 1.383                # NEC-violation onset / physical-domain boundary (Ric_min crosses 0); S95 W4-5 12D censorship; hawking V.3/V.9; phonic-exflation-equation.md capstone (3-decimal canonical; sp-synthesis fine value 1.382334)
Mach_max_framework = 13.75     # Framework Mach at van Hove fold (phononic-framing.md LCDM reframe)
Mach_max_analog = 54.3         # BEC analog-realization Mach (MEMORY.md analog:)
Mach_max = Mach_max_framework  # Default alias = framework value (S85 W6-1)
v_crit = 219.3                 # Censorship critical velocity (MEMORY.md: v_crit entry)
v_term = v_terminal            # Alias for W6-2 plan notation (= 26.545, S38)
T_BCS = 0.640                  # BCS canonical temperature (S70 BCS-GAP-CANONICAL; MEMORY.md)
T_c_BCS = 0.083                # BCS critical temperature (MEMORY.md: T_c=0.083)
kappa_BCS = 4.019              # BCS surface-gravity analog (S69 W3-D; MEMORY.md)
T_H_dump_expected = 0.0        # Pre-registered extremal-horizon prediction (S85 W6-4 target; κ=0 → T_H=0)
d_spec = 3                     # Classical spectral dimension of D_K at canonical triple (Connes-Moscovici)
c_S_canon = 1.0                # Canonical spectral action scale normalization (Chamseddine-Connes 1997)
Lambda_Planck = 1.0            # Planck scale in M_KK units (default 1.0; S85 W6-3 placeholder for regulator scan)
Borel_threshold_S_inst = 4.34  # Borel-summability lower bound on S_inst (W10-121 @ S84; separates Gaussian sub-sigma from WKB tunneling in Jensen-tau instanton sector)
eps_H_W6 = 0.02163             # Slow-roll bound pinned from S80 dS/dtau at fold; used as NLO-margin cap in W6-70 field-expansion convergence and W6-69 F_amp^3PI FI chain (S85 W9-2)
n_s_framework = 0.9561         # Framework-predicted n_s at CMB pivot from gauge-invariant spectral geometry (S84 T6 constant-epsilon; distinct from planck_ns=0.9649 observational pivot) (S85 W9-3)
n_s_FW_exact = Fraction(9561, 10000)  # Bit-exact rational pin; n_s_FW_exact**2 - 1 == Fraction(-8587279, 100000000) EXACTLY in Q. (S88 W-15 W15-V.2 synthesis: Route-B identity bit-exact pin; 9561**2 == 91412721 perfect square; Route-A absent at Mellin-residue axis per W5a-44 FAIL audit_sha256=c092fe1bff9ab669...; supersedes scheme-dependent floats 0.9567/0.9557/0.9595)

# ══════════════════════════════════════════════════════════════════════════════
# S88 W-18 W18-V.2 — slope_A_FW DUAL-READING PARAMETERIZED CLOSED-FORM PINS
# ══════════════════════════════════════════════════════════════════════════════
# PROVENANCE:
#   - Source workshop: sessions/archive/session-88/workshops/s88-w18-w6a-51-geometric-
#     resummation.md §II.5 + §V.2 (Workshop-1 dual-reading parameterized
#     canonical specification; gen-physicist-orchestrator authorship; landed
#     2026-05-08).
#   - §W6a-51 source gate audit_sha256:
#       574d81fecb26f7eefef4c2d5b7b2bfe06487fe7e377fa0c9b64d71e573f5e42e
#   - Sage-symbolic CM-1995 §III.4 + Proposition III.6 pole-LOCATION stability;
#     verified via Python: 0.190/(5*pi) = 0.012096; 10/(1-0.012096) =
#     10.122438748... agrees to 10 digits with the geometric scalar pin.
#   - Conv-B = Conv-A / 2 (substrate dimensional convention; Conv_A_AT_TAU_FOLD/2
#     = 5.061219374192 verified bit-identical with the Conv_B scalar pin).
#
# REGIME-OF-VALIDITY DECLARATION (Reading A vs Reading B distinction):
#   - Reading A (geometric resummation): all-orders extension to 1/(1-ε) is
#     STRUCTURALLY EARNED only at first order in τ from CM-1995 §III.4 + Prop
#     III.6; predicted residual at τ=2·τ_fold=0.38 is ratio R(0.38)/R(0.19)≈8.
#   - Reading B (linear-LO only): O(τ²) caveat; predicted residual ratio at
#     τ=0.38 is R(0.38)/R(0.19)≈4.
#   - Empirical residual at τ_fold=0.19 is 5.23e-05; lies BETWEEN both readings'
#     predictions; the τ=0.38 cross-validation gate is the structural decider
#     (S89 CF V.3 `S89-W6A-51-TAU-CROSS-VALIDATION-AT-2-TAU-FOLD`).
#
# SCALAR PIN CONVENTION:
#   - slope_A_FW_Conv_A_AT_TAU_FOLD pins the GEOMETRIC reading evaluation at
#     τ_fold = 0.190 (10.122438748384). Linear-LO reading would give 10.120957756750
#     (Python-verified; gap 1.481e-3 = O(τ²) Reading-A vs Reading-B distinction);
#     the geometric value is canonical because §VII.AR STAGE-1-CANDIDATE landed
#     under Reading A. Conditional on Reading-A WIN at S89 CF V.3.
#   - Downstream consumers needing τ-functional dependence cite the parameterized
#     string forms with explicit regime caveat.
# ══════════════════════════════════════════════════════════════════════════════
slope_A_FW_Conv_A_LO = "10.0 * (1 + tau/(5*pi))"          # Parameterized linear-LO (Reading B)
slope_A_FW_Conv_A_GEOMETRIC = "10.0 / (1 - tau/(5*pi))"   # Parameterized geometric (Reading A)
slope_A_FW_Conv_A_AT_TAU_FOLD = 10.122438748384           # Scalar pin at τ_fold=0.190; Sage-CM-1995 §III.4 evaluation; geometric reading
slope_A_FW_Conv_B_LO = "5.0 * (1 + tau/(5*pi))"           # Parameterized linear-LO Conv_B = Conv_A/2 (Reading B)
slope_A_FW_Conv_B_GEOMETRIC = "5.0 / (1 - tau/(5*pi))"    # Parameterized geometric Conv_B = Conv_A/2 (Reading A)
slope_A_FW_Conv_B_AT_TAU_FOLD = 5.061219374192            # Scalar pin = Conv_A_AT_TAU_FOLD/2 bit-identical
l_max_21cm_forecast = 1e5      # 21-cm bispectrum high-multipole forecast horizon used for SHAPE-template pre-registration (conservative SKA-Phase-2+ ceiling) (S85 W9-3)
mu_BC_GeV = 188.185            # mu_BC accommodated value (S84 W9b-105 geometric; CUBIC-OMITTED-C2 convention; SCHEME-DEP under V.2-FAIL per W4-48) (S85 W9-5 fallback-mode canonical)

# ══════════════════════════════════════════════════════════════════════════════
# S86 W1c-8 followup: substrate Mellin-tilt anchors + n_s(c_sub) callable
# Provenance:
#   - Source gate: S86-FALSIFIER-MASTER-INVENTORY-PROMOTION (C29, mack-cosmic-bridge,
#       2026-04-26). audit_sha256=32c60c2f69fe6150a1d8e89a81961046cfb68091373cc0b8721106d35ebdd5f6
#       content_sha256=144a9999104f3662fc5a5920e3779cb533cb7581e9014007010d89a028273aef.
#   - C29 derived n_s(c_sub) from canonical Mellin-weight definition (eq_166717:
#       c_sub(tau) = M_Pl_eff^2(k_pivot, tau) / M_Pl_eff^2(0, tau)) and the
#       substrate spectral-tilt identity n_s = 1 - 2*eps_eff (S43
#       transfer-function; per S85 W2-as-band-authority.md line 919).
#   - C29 WP §W1c-8 carry-forward bullet #2 requested promotion to canonical
#       infrastructure; Task #11 (S86 in-session remediation per "No Technical
#       Debt" rule) executes this promotion. Source plan: session-86-plan-w1c §W1c-8.
# ══════════════════════════════════════════════════════════════════════════════
c_sub_baseline = 2.238         # Substrate Mellin-weight baseline (S78 W2-E central pin; S85 W2-as-band-authority.md line 224); S86 W1c-8 (C29) fed n_s_of_c_sub anchor
# ══════════════════════════════════════════════════════════════════════════════
# PROVENANCE c_sub_corrected_central:
#   Session: S88 W10 (in-session promotion from §W10-116 / §W10-117 carry-forward
#     under user re-evaluation directive 2026-05-06 "we don't carry-forward things
#     we should do now")
#   Source:  s86-cm1995-kernel-normalization-audit.md Step 1 [Definitions]:
#     "c_sub_corrected_central = 3.5169 [L3 result, verified]"
#   Originally: Bulletin #3 (S87 W-10 R3-B) PASS-B residual; narrative pin pending
#     canonical promotion. Class-(f) PIN-PLACEHOLDER detected at S88 §W10-116
#     (verdict audit_sha256=adbcdf73880c3d6f...) → in-session promotion herewith
#     per `feedback_fix-in-session-never-defer.md` + `CLAUDE.md §"No Technical Debt"`.
#   Lizzi taxonomy class: RD (Regulator-Dressed; max drift 9.63% across A_5 atlas
#     at substrate-distance-1 pole s=3 exceeds 5% FI threshold) per S88 §W10-117
#     (audit_sha256=a44e0255c8a30ac6...). The pinned 3.5169 is the (A)-class
#     anchor reading (ζ, Zubarev); cross-class (anomaly, cutoff_sqrt) reading
#     differs by ≤ 13% per the §W10-110/§W10-111 SCHEMATIC per-regulator drift map.
# ══════════════════════════════════════════════════════════════════════════════
c_sub_corrected_central = 3.5169  # Bulletin #3 PASS-B (A)-class anchor at s=3; lizzi class=RD per S88 §W10-117
eps_baseline = (1.0 - planck_ns) / 2.0  # Substrate slow-roll-equivalent at c_sub_baseline; (1 - planck_ns)/2 gives the baseline epsilon that reproduces n_s = 0.9649 at c = c_sub_baseline (S86 W1c-8 C29 anchor)


def n_s_of_c_sub(c_sub_value, eps_baseline_arg=None, c_sub_baseline_arg=None):
    """Substrate-spectral n_s(c_sub) — Mellin-tilt callable.

    Returns the substrate scalar spectral index n_s as a function of the
    Mellin-weight ratio c_sub at fixed CMB pivot. Derived from:

        c_sub        := M_Pl_eff(k_pivot)^2 / M_Pl_eff(0)^2     [eq_166717]
        eps_eff(c)   := eps_baseline * (c_sub_baseline / c)
                          [Mellin re-weighting at fixed pivot;
                           1/c_sub at leading Mellin order — C29 §6]
        n_s(c)       := 1 - 2 * eps_eff(c)
                       = 1 - 2 * eps_baseline * (c_sub_baseline / c)
                          [substrate constant-mass spectral-tilt identity;
                           S43 transfer-function;
                           S85 W2-as-band-authority.md line 919]

    Anchors (from canonical_constants.py defaults):
        eps_baseline  = (1 - planck_ns) / 2 = 0.0175500000  (CMB pivot)
        c_sub_baseline = 2.238                               (S78 W2-E central)

    Parameters
    ----------
    c_sub_value : float
        The Mellin-weight ratio (typically in [c_sub_baseline, 4] for
        Path-C; baseline 2.238 for Path-H).
    eps_baseline_arg : float, optional
        Override the canonical eps_baseline anchor. Defaults to the
        canonical eps_baseline pinned above.
    c_sub_baseline_arg : float, optional
        Override the canonical c_sub_baseline anchor. Defaults to the
        canonical c_sub_baseline pinned above.

    Returns
    -------
    n_s : float
        Substrate scalar spectral index at the given c_sub.

    Provenance
    ----------
    - Source gate (where formula was first derived & runtime-validated):
      S86-FALSIFIER-MASTER-INVENTORY-PROMOTION (C29; mack-cosmic-bridge,
      2026-04-26).
        audit_sha256   = 32c60c2f69fe6150a1d8e89a81961046cfb68091373cc0b8721106d35ebdd5f6
        content_sha256 = 144a9999104f3662fc5a5920e3779cb533cb7581e9014007010d89a028273aef
    - Canonical Mellin-weight definition: eq_166717 (knowledge.db trace
      'c_sub Mellin').
    - Substrate spectral-tilt identity n_s = 1 - 2*eps_eff: S43
      transfer-function, surfaced in S85 W2-as-band-authority.md line 919.
    - Promotion gate (this callable): S86-W1C-C29-FOLLOWUP-NS-OF-CSUB-PROMOTION
      (gen-physicist Task #11; in-session remediation under "No Technical
      Debt" rule, 2026-04-26).

    Examples
    --------
    >>> n_s_of_c_sub(2.238)      # baseline; recovers planck_ns
    0.9649
    >>> n_s_of_c_sub(3.647)      # C29 Path-C upper-spread regulator anchor
    0.9784607074...
    """
    eps_b = eps_baseline if eps_baseline_arg is None else eps_baseline_arg  # (local)
    c_b = c_sub_baseline if c_sub_baseline_arg is None else c_sub_baseline_arg  # (local)
    eps_eff = eps_b * (c_b / c_sub_value)  # (local) Mellin-tilted eps at the requested c
    return 1.0 - 2.0 * eps_eff


if __name__ == "__main__":
    from pathlib import Path
    DATA_DIR = Path(__file__).parent

    # Collect all numeric module constants
    _module_consts = {
        k: v for k, v in globals().items()
        if isinstance(v, (int, float, np.floating)) and not k.startswith("_")
    }

    print("=" * 78)
    print(f"CANONICAL CONSTANTS VALIDATION ({len(_module_consts)} module constants)")
    print("=" * 78)

    passed = 0
    failed = 0
    verified = set()

    def check(label, module_val, npz_val, rtol=1e-10):
        global passed, failed
        if abs(npz_val) > 0:
            err = abs(module_val - npz_val) / abs(npz_val)
        else:
            err = abs(module_val - npz_val)
        status = "PASS" if err < rtol else "FAIL"
        if status == "PASS":
            passed += 1
        else:
            failed += 1
        print(f"  {status}  {label:<50s}  err={err:.2e}")

    # ── PROVENANCE-driven NPZ checks ──
    # Group PROVENANCE entries by source NPZ file
    from collections import defaultdict
    npz_checks = defaultdict(list)  # npz_filename -> [(module_name, npz_key), ...]
    for const_name, prov in PROVENANCE.items():
        src = prov.get("source", "")
        if ".npz" not in src:
            continue
        # Extract NPZ filename from source string (may have parenthetical key info)
        npz_file = src.split(" ")[0].split("(")[0].strip()
        if not npz_file.endswith(".npz"):
            continue
        # Determine what key to look up in the NPZ
        npz_key = _MODULE_TO_NPZ_KEY.get(const_name, const_name)
        # Check for parenthetical key override: "file.npz (actual_key)"
        if "(" in src and ")" in src:
            override = src.split("(")[1].split(")")[0].strip()
            npz_key = override
        npz_checks[npz_file].append((const_name, npz_key))

    print(f"\n  PROVENANCE maps {sum(len(v) for v in npz_checks.values())} "
          f"constants to {len(npz_checks)} NPZ files\n")

    for npz_file in sorted(npz_checks.keys()):
        npz_path = DATA_DIR / npz_file
        if not npz_path.exists():
            print(f"--- {npz_file} (NOT FOUND) ---")
            for const_name, _ in npz_checks[npz_file]:
                print(f"  SKIP  {const_name}")
            continue

        try:
            d = np.load(npz_path, allow_pickle=True)
        except Exception as e:
            print(f"--- {npz_file} (LOAD ERROR: {e}) ---")
            continue

        print(f"--- {npz_file} ---")
        for const_name, npz_key in npz_checks[npz_file]:
            if npz_key not in d:
                print(f"  SKIP  {const_name} (key '{npz_key}' not in NPZ)")
                continue
            val = d[npz_key]
            if hasattr(val, 'size') and val.size != 1:
                print(f"  SKIP  {const_name} (array, size={val.size})")
                continue
            try:
                npz_val = float(val.flat[0]) if hasattr(val, 'flat') else float(val)
            except (TypeError, ValueError):
                print(f"  SKIP  {const_name} (non-numeric)")
                continue

            module_val = _module_consts.get(const_name)
            if module_val is None:
                print(f"  SKIP  {const_name} (not in module)")
                continue

            label = const_name + (f" (npz:{npz_key})" if npz_key != const_name else "")
            check(label, module_val, npz_val)
            verified.add(const_name)

    # ── Identity alias checks ──
    print(f"\n--- Alias identity checks ---")
    aliases = [("E_cond", "E_cond_ED_8mode"), ("M_KK", "M_KK_gravity")]
    for alias, target in aliases:
        if globals().get(alias) is globals().get(target):
            print(f"  PASS  {alias} is {target}")
            passed += 1
        else:
            print(f"  FAIL  {alias} is NOT {target}")
            failed += 1
        verified.add(alias)

    # ── Self-consistency: derived constants must equal their derivation ──
    print(f"\n--- Derived consistency ---")
    derivations = [
        ("hbar_GeV_s",    hbar_eV_s / 1e9,        "hbar_eV_s / 1e9"),
        ("hbar_c_GeV_cm", hbar_c_GeV_m * 100,      "hbar_c_GeV_m * 100"),
        ("l_Planck_cm",   l_Planck * 100,           "l_Planck * 100"),
        ("c_light_cgs",   c_light * 100,            "c_light * 100"),
        ("c_light_km_s",  c_light / 1000,           "c_light / 1000"),
        ("G_N_cgs",       G_N * 1000,               "G_N * 1000"),
        ("Mpc_to_cm",     Mpc_to_m * 100,           "Mpc_to_m * 100"),
        ("GeV_to_g",      GeV_to_kg * 1000,         "GeV_to_kg * 1000"),
        ("T_CMB_GeV",     T_CMB * k_B / 1e9,        "T_CMB * k_B / 1e9"),
        ("GeV_inv_to_Mpc", hbar_c_GeV_m / Mpc_to_m, "hbar_c_GeV_m / Mpc_to_m"),
        ("Mpc_to_GeV_inv", Mpc_to_m / hbar_c_GeV_m, "Mpc_to_m / hbar_c_GeV_m"),
        ("Gpc_to_m",       Mpc_to_m * 1e3,          "Mpc_to_m * 1e3"),
        ("kpc_to_cm",      Mpc_to_cm / 1e3,         "Mpc_to_cm / 1e3"),
    ]
    for name, expected, formula in derivations:
        actual = _module_consts.get(name)
        if actual is not None:
            check(f"{name} == {formula}", actual, expected, rtol=1e-6)
            verified.add(name)

    # ── Summary ──
    unverified = sorted(set(_module_consts.keys()) - verified)

    print(f"\n{'='*78}")
    print(f"RESULTS: {passed} PASS, {failed} FAIL")
    print(f"  NPZ-verified:     {len(verified & set(c for checks in npz_checks.values() for c, _ in checks))}")
    print(f"  Derived-verified: {len([d for d in derivations if d[0] in verified])}")
    print(f"  Alias-verified:   {len(aliases)}")
    print(f"  Unverified:       {len(unverified)} (PDG/CODATA or no NPZ source)")
    if unverified:
        for name in unverified:
            print(f"    {name} = {_module_consts[name]}")
    print(f"{'='*78}")

    if failed > 0:
        print("\nFAILED — check values against authoritative NPZ sources")
        sys.exit(1)
    else:
        print("\nAll checks passed.")


# -----------------------------------------------------------------------------
# S87 W1b-HK-6 — Richardson 3-point canonical form pin
# -----------------------------------------------------------------------------
# Source: S87-W1B-HK-6-RICHARDSON-FORM-CANONICALIZE
# Producing script: computations/session-87/s87_w1b_hk_1_6_pv_mpmath_richardson.py
# Comment: canonical form (A) for L^{-3}-asymptotic Weyl convergence fits;
#          selected over plan-literal alternating-sign eliminator form (B)
#          because (A) uses all 3 data points symmetrically and emits a
#          residual diagnostic. The W1b-3 final-iteration verdict
#          (s87_gate_verdicts.txt line 59) reports the (A)-form residual.
# -----------------------------------------------------------------------------
RICHARDSON_3PT_CANONICAL_FORM = 'Richardson_3pt_canonical_form_A: lstsq(x=1/L^3, y=f(L)) -> (a=f_inf, b=c1); residual = max_i |f_i - (a + b * x_i)|. Pinned via S87 W1b-HK-6 from computations/session-87/s87_w1b_lmax_weyl_convergence_sweep.py L582 richardson_3pt_canonical(); selected over plan-literal form (B) [R = (Σ alt-sign L^3 f) / (Σ alt-sign L^3)] because (A) uses all 3 data points symmetrically and emits a residual diagnostic, while (B) is a 3-point algebraic eliminator without residual. The W1b-3 final verdict (line-59) reports the (A)-form residual.'

# -----------------------------------------------------------------------------
# S87 W3-2 — BK-Array meta-classifier_v2 substrate-first canonical pins
# -----------------------------------------------------------------------------
# Source: S87-BK-ARRAY-JOINT-META-CLASSIFIER-V2 (CF-21)
# Producing script: computations/session-87/s87_w3_bk_array_meta_classifier_v2.py
# Substrate first principles:
#   n_T = -r/8 single-field consistency relation (S84 W4-39 EXACT theorem
#         on the substrate's spectral-moment ratio P_T(k)/P_S(k); the same
#         identity that emerges in slow-roll inflation, here derived from
#         the substrate's a_4-weighted gradient evaluated at k_pivot).
#   Workshop §V1 anchor: sessions/archive/session-86/workshops/s86-r-dual-pathway-bk-array-and-nT.md L19
#         "n_T from S84 W4-39: Path-H -0.000931, Path-C -0.001463" (4-sig-fig)
#         vs Sage-exact derivation here (via QQ rational arithmetic):
#           n_T_PathH_canonical = -r_PathH / 8 = -0.0074705 / 8 = -0.0009338125
#           n_T_PathC_canonical = -r_CMB_framework / 8
#                               = -0.011731522176014426 / 8
#                               = -0.0014664402720018033
#         Workshop 4-sig-fig vs canonical Δ < 4e-6 (rounding agreement).
#   sigma_n_T_LiteBIRD: LiteBIRD full-mission projected 1σ on n_T
#         (Hazumi+ 2019 / LiteBIRD Collab. 2023 — promoted from
#         computations/session-85/s85_w4_null_elim_map.py:SIGMA_N_T_LITEBIRD local;
#         pre-existing knowledge-MCP equation hit confirms the 8.0e-4 figure).
#   Omega_GW_Lambda_A_LISA: PENDING-SUBSTRATE-RECOMPUTE (S96 W-3 workshop,
#         little-red-dots ∧ mack, 2026-05-30). The value 1.0e-10 is a
#         provenance-less pivot placeholder (Case A): it was an "OOM estimate
#         AT LISA 3 mHz" under an ASSUMED peak-at-3-mHz, refuted by
#         S96-OBS-CGWB-PEAK-FREQ (peak f_obs = 8.4835e39 Hz, audit 646e6ad0...,
#         42.45 decades above the pivot). Under an f^3 IR tail to that peak the
#         3-mHz value is ~10^-137, 127 OOM inconsistent with 1.0e-10; backing
#         Omega_peak out of 1e-10-at-pivot gives ~10^117 (unphysical). Fires
#         Class-(f) PIN-PLACEHOLDER + Class-(c) PIN-DRIFT-FROM-STALE-SOURCE
#         (W6-3 the supersession event). The LISA-band amplitude is the IR-tail
#         value Omega_peak*(f_LISA/f_peak)^p, < 10^-42 slope-independently
#         (29.45 OOM below LISA-PLS for all p>=1) -> the acoustic CGWB is
#         GW-DETECTOR-STERILE (above LISA/PTA/HF). The value is NOT changed
#         here (no derived Omega_peak exists yet; the import must not break);
#         the correct re-pin is the S97 two-gate compute
#         (S97-OMEGAGW-PEAK-HEIGHT -> S97-OMEGAGW-ACOUSTIC-SPECTRAL-SHAPE), which
#         derives Omega_peak at f_peak and the IR slope p, then re-pins.
#         RETIRED as a LISA/GW falsifier; NOT deleted (the IR-tail amplitude is
#         a real substrate observable). See falsifier-master-inventory.md
#         Row #7.audit-3. (Superseded basis: the prior project_lisa-gw-prediction
#         memory 1e-10 estimate is the stale source.)
#   Omega_GW_Lambda_C_LISA: aliased to Omega_GW_Companion_null = 8.299e-58
#         per W13-2.Ω verdict (Sage-exact form, NOT round-figure 1e-57 per
#         regulator-pin-discipline.md §"Sage-Exact Rationals for Ω_GW
#         Regulator-Class Values").
# -----------------------------------------------------------------------------
n_T_PathH_canonical = -0.0009338125  # n_T = -r_PathH / 8 single-field consistency (S87)
n_T_PathC_canonical = -0.0014664402720018033  # n_T = -r_CMB_framework / 8 (S87)
sigma_n_T_LiteBIRD = 8.0e-4  # LiteBIRD full-mission 1sigma projection on n_T (S87, ex-s85_w4 local)
Omega_GW_Lambda_A_LISA = 1.0e-10  # PENDING-SUBSTRATE-RECOMPUTE (S96 W-3): provenance-less pivot placeholder, RETIRED as GW falsifier; value held (no derived Omega_peak yet), re-pin = S97 two-gate compute. See PROVENANCE block above + falsifier-master-inventory.md Row #7.audit-3. (was: "Substrate-physics OOM estimate at LISA 3 mHz; (A)-class regulator (S87)")
Omega_GW_Lambda_C_LISA = 8.299e-58  # Sage-exact alias of Omega_GW_Companion_null; (C)-class regulator (S87)
# Pathway-keyed Omega_GW pins per W13-2 P10 3-pathway projection (placeholder
# at OOM since the f_NL pathway-projection's GW counterpart is the (A)-class
# regulator-floor in all 3 cases — the f_NL pathway split is at the bispectrum
# layer, not the GW-monopole layer). Each is ALIASED to the (A)-class canonical:
Omega_GW_FW_S82_equilateral = 1.0e-10  # Aliased to Omega_GW_Lambda_A_LISA (S82 GGE-equilateral pathway); INHERITS PENDING-SUBSTRATE-RECOMPUTE (S96 W-3) — value held, re-pin via S97 two-gate compute
Omega_GW_FW_S67_folded = 1.0e-10  # Aliased to Omega_GW_Lambda_A_LISA (S67 GGE-folded pathway); INHERITS PENDING-SUBSTRATE-RECOMPUTE (S96 W-3) — value held, re-pin via S97 two-gate compute
Omega_GW_FW_S85_W9_3_analytic_template = 1.0e-10  # Aliased to Omega_GW_Lambda_A_LISA (S85 W9-3 analytic-template pathway); INHERITS PENDING-SUBSTRATE-RECOMPUTE (S96 W-3) — value held, re-pin via S97 two-gate compute


# === S88 W8-94 — CHANNEL_LABELS canonical pin (22 entries) ===
# CHANNEL_LABELS pinned S88 W8-94 per s87 §VII.X.W4-1 9-cell tensor channel-label drift analysis; cites operator-projection Reading-A naming hygiene (S88 W8-92).
# Source: sessions/permanent-results-registry.md §VII.X.W4-1 lines
# 13614-13705 (Cross-Pillar 3-Channel Bridge Theorem, 9-Cell Tensor
# R^{(k)}_{p,q}(L_max=10); STAGE-1-CANDIDATE per joint-theorem-promotion.md).
# Structure: 4 diagonal (algebra summands C, H, M_3, M_2) + 18 off-diagonal
# (k in {1,2,3} channel x ordered (p,q) in {II,III,IV}^2 with p != q).
# Substrate framing: labels are structural identifiers of A_K = C (+) H (+)
# M_3(C) and Hochschild-cocycle off-diagonal cells; NOT labels for a
# pre-existing geometric container.
CHANNEL_LABELS = {
    # --- 4 diagonal: A_K = C (+) H (+) M_3(C) summands + M_2(C) BdG sub-sector ---
    'M_2(C)'    : 'channel_M2C'                                   ,  # M_2(C) BdG sector (from inheritance iota_*(M_3(C)) -> M_2(C))
    'M_3(C)'    : 'channel_M3C'                                   ,  # M_3(C) Cartan-zone full sector
    'H'         : 'channel_H'                                     ,  # H quaternionic-isospin sector
    'C'         : 'channel_C'                                     ,  # C scalar-trace sector
    # --- 6 off-diagonal cells at channel k=1 (rank-1 Wick-decomposable / 2-pt-separable) ---
    'k1_II_to_III': 'channel_off_diag_k1_II_to_III'               ,  # HKR
    'k1_II_to_IV' : 'channel_off_diag_k1_II_to_IV'                ,  # K-theory boundary (HKR o Connes-Karoubi)
    'k1_III_to_II': 'channel_off_diag_k1_III_to_II'               ,  # HKR
    'k1_III_to_IV': 'channel_off_diag_k1_III_to_IV'               ,  # Connes-Karoubi pairing (W-5 canonical)
    'k1_IV_to_II' : 'channel_off_diag_k1_IV_to_II'                ,  # K-theory boundary (HKR o Connes-Karoubi)
    'k1_IV_to_III': 'channel_off_diag_k1_IV_to_III'               ,  # Connes-Karoubi pairing (W-5 canonical)
    # --- 6 off-diagonal cells at channel k=2 (rank-2 pair-cumulant / W-5 calibrated) ---
    'k2_II_to_III': 'channel_off_diag_k2_II_to_III'               ,  # HKR
    'k2_II_to_IV' : 'channel_off_diag_k2_II_to_IV'                ,  # K-theory boundary (HKR o Connes-Karoubi)
    'k2_III_to_II': 'channel_off_diag_k2_III_to_II'               ,  # HKR
    'k2_III_to_IV': 'channel_off_diag_k2_III_to_IV'               ,  # Connes-Karoubi pairing (W-5 canonical)
    'k2_IV_to_II' : 'channel_off_diag_k2_IV_to_II'                ,  # K-theory boundary (HKR o Connes-Karoubi)
    'k2_IV_to_III': 'channel_off_diag_k2_IV_to_III'               ,  # Connes-Karoubi pairing (W-5 canonical)
    # --- 6 off-diagonal cells at channel k=3 (rank-3 3-pt-connected vertex / irreducible) ---
    'k3_II_to_III': 'channel_off_diag_k3_II_to_III'               ,  # HKR
    'k3_II_to_IV' : 'channel_off_diag_k3_II_to_IV'                ,  # K-theory boundary (HKR o Connes-Karoubi)
    'k3_III_to_II': 'channel_off_diag_k3_III_to_II'               ,  # HKR
    'k3_III_to_IV': 'channel_off_diag_k3_III_to_IV'               ,  # Connes-Karoubi pairing (W-5 canonical)
    'k3_IV_to_II' : 'channel_off_diag_k3_IV_to_II'                ,  # K-theory boundary (HKR o Connes-Karoubi)
    'k3_IV_to_III': 'channel_off_diag_k3_IV_to_III'               ,  # Connes-Karoubi pairing (W-5 canonical)
}


# ==============================================================================
# === S91 W-1 + W-5 in-session pins (2026-05-22; rule-feedback fix-in-session
# vs deferred-CF discipline; "only-math-carries-forward" correction per user
# 2026-05-22 + .claude/rules/Investigating-Workshops.md "is NOT" items 1-9 +
# feedback_fix-in-session-never-defer.md no-technical-debt rule) ===
# ==============================================================================
#
# Both blocks were originally pre-registered as S92 carry-forwards
# (W1 CF-Q-FINAL.a; W5 CF-S91-W6-1-VII-AU-OP-PROJ-STAGE-1-CANDIDATE-LANDING
# two-pin) but the underlying numerical values were FULLY ESTABLISHED at S91
# workshop close. Per the "only math carries forward" rule, canonical_constants
# promotion of already-emitted-and-verified verdicts is fix-in-session hygiene,
# NOT future computation. Landed in-session 2026-05-22.

# --- S91 W-1 Q-FINAL.a — substrate-derived factor-5 magnitude ratio ---
#
# Cell IV state-pair content vs Cell II regulator-tier content magnitude
# separation at substrate-distance-2 pole s=4 on BdG sub-algebra M_2(C) subset
# A_K. r_substrate quantifies the magnitude separation between two algebra-axis
# cells at the SAME pole on the SAME finite spectral triple
# (A_K, H_K, D_K(tau_fold=0.19)).
#
# Substitution chain (workshop lines 1170-1188):
#   r_substrate = |Delta_A_W1_3| / |Delta_FULL_W1_2|
#               = 0.1105338 / 0.02199981
#               = 5.0243   (4 sig figs)
#
# Substrate-IS interpretation per L1 §1-§4 parse-tree decompositions:
#   Numerator   = Cell IV state-pair content magnitude at substrate-distance-2
#                 pole s=4 on BdG sub-algebra M_2(C) (state-pair functional)
#   Denominator = Cell II algebra-INVARIANT spectrum-only functional regulator-
#                 tier content at the SAME pole on full A_K (Mellin moment)
#   r > 1     ⇒ Cell IV state-pair content parametrically LARGER than Cell II
#                regulator-tier content (consistent with R-protection at the
#                Cell IV ratio structure per Re:V4 + R-PROTECTION REFINED
#                per-branch dimension ≥ 3 requirement)
#
# Source: S91 W-1 workshop EMERGENCE 1 + Q-FINAL.a answer (lines 1163-1213).
# Workshop file: sessions/archive/session-91/workshops/s91-w1-operational-alignment-
#                regulator-class-robustness.md
#
# Substrate inputs:
#   computations/session-91/s91_w1_cf71_k_canonical_pin_uniqueness.npz (W1-3)
#   computations/session-91/s91_w1_cf70_full_cc_multipliers.npz (W1-2)
#   s52_bogoliubov_amp.npz (canonical s52 8-mode Bogoliubov amplitude vector)
#   s84_spectrum_cache_L12_tau019.npz (L_max=12 master spectrum cache)
#
# Verdict pins (computations/session-91/s91_gate_verdicts.txt):
#   W1-3 (CF-S91-CF-71-K_CANONICAL-PIN-UNIQUENESS) supplies numerator:
#     audit_sha256=db08f3dfd9c8a5532c442629dd256950f51ac3219bfbe1bc8c35471b6b2be9c4
#     Delta_A_scalar = +1.105338e-01   (state-pair content magnitude;
#                                       scalar-Δ vs canonical s52 multi-branch)
#   W1-2 (CF-S91-CF-70-FULL-CC-MULTIPLIERS) supplies denominator:
#     audit_sha256=26d40c88fcddf694dbb8c2b3639f315550111222e2af21e9aa309c69b7ad6654
#     Delta_FULL    = +2.199981e-02    (regulator-tier content magnitude;
#                                       BARE M_BARE=3.0909e+03 vs
#                                       FULL-CC M_FULL_CC=3.1589e+03)
#
# Sage-exact rational form pending CF-S91-W1-F asymptotic L_max → ∞ extension
# (regulator-pin-discipline.md §"Extension: Sage-Exact Rationals" discipline);
# the float-form pin below is the substrate-IS empirical anchor at L_max=12.
#
cell_iv_cell_ii_ratio_substrate_distance_2_FW = 5.0243   # (4 sig figs; W1 Q-FINAL.a)


# --- S91 W-5 §VII.AU.OP-PROJ two-pin protocol -----------------------------
#                  (Level-1 asymptotic anchor + Level-3 finite-L sample) ---
#
# Two-pin canonical_constants.py protocol per S91 W-5 EMERGENCE table row 5
# (workshop lines 1320, 1325-1326; R2 Convergence #3 + Re:L4 EMERGES #1 +
# Re:L5 EMERGES #1). K=1 calibration instance of the candidate Class 8.8
# LAYER-axis pin discipline at `epistemic-discipline.md §"Pre-Registration
# Completeness"` (provisional; promotes to MANDATORY at K=3 distinct
# calibration instances per `feedback_rules-compensate-missing-structure.md`).
#
# Substrate-IS observable: alpha extraction on §VII.AU.OP-PROJ pathway-b
# direct Connes-Karoubi pairing at substrate-distance-1 pole s=3 on the
# substrate's finite spectral triple (A_K, H_K, D_K(tau_fold=0.19)).
#
# Source: S91 W-5 workshop EMERGENCE table row 5 (lines 1320, 1325-1326).
# Workshop file: sessions/archive/session-91/workshops/s91-w5-layer-functor-f-
#                universal-envelope-scope-adjudication.md
#
# Asymptotic anchor (Level-1; substrate-derived from CM-1995 §III.4
# simple-pole residue on Cell I at substrate-distance-1 pole; substrate-IS
# regulator-invariance BY THEOREM at the L → ∞ asymptotic layer; REINDEXED
# Layer-Functor F K=2 SUGGESTION corpus, K=1 = §VII.AF.1.OP-PROJ HP^1
# cohomology; K=2 = THIS pin; algebra-axis orthogonality K=3 MANDATORY
# from S87 W-2 close is STRUCTURALLY DISTINCT from this Layer-Functor F
# K-counter and must be cited as an independent structural pin):
alpha_canonical_VII_AU_OP_PROJ_FW_ASYMPTOTIC = -3
#
# Finite-L sample (Level-3; empirical anchor at L_fit ∈ [15, 22] from
# W6-1 pathway-b direct Connes-Karoubi pairing; Mellin + zeta evaluators
# agree at machine precision at SIMPLE pole BY CONSTRUCTION per Re:L4
# R2-A-Q-C3-1 — they evaluate the SAME closed-form algebraic identity
# Σ_k m_k |λ_k|^{-2s_0} at any simple pole on any finite spectral triple):
alpha_sample_VII_AU_OP_PROJ_FW_PATHWAY_B_L15_22 = 2.6926236951422458
#
# Verdict pin (computations/session-91/s91_gate_verdicts.txt:128):
#   S91-D4-ENVELOPE-EXTENDED-L_MAX-SUB-WINDOW: PASS
#   audit_sha256=d54b26a970e43b6b5a63bee474a4a8baa80ed012546021c9dfe191cdb108fd8d
#   value: alpha_pathway_b=2.6926 at L_max=22 (4 sig figs surface; full
#          precision 2.6926236951422458 from NPZ data file)
#   convention=Mellin-class-FI-axis-F_2-projection-CACHE-PROJECTION-SCHEMATIC
#   tier_pin=TIER-2 (SCHEMATIC level-pin disclosure per
#                    `substrate-first-canonical-sourcing.md §(iv)` K=4
#                    MANDATORY; PV/cutoff/lattice consume W6-2 sub_term_R
#                    SCHEMATIC analytic forms; F_2 axis Mellin+zeta is
#                    FULL physical substrate-IS canonical)
#
# Layer-tag suffix discipline (Class 8.8 candidate):
#   _ASYMPTOTIC          = Level-1 leading-term -3 universal (per
#                          CM-1995 §III.4 simple-pole residue at substrate-
#                          distance-1 pole; substrate-derived)
#   _PATHWAY_B_L15_22    = Level-3 empirical sample at the specified L-fit
#                          window (W6-1 pathway-b direct Connes-Karoubi
#                          pairing)
#
# Substrate framing: alpha IS the substrate's intrinsic Level-2 envelope
# convergence rate at the substrate-distance-1 pole; the asymptotic limit
# (-3) is the substrate's IS-not-IN structural identity per CM-1995 §III.4
# simple-pole residue; the L=22 sample is the substrate's finite-L empirical
# image. Both pins are substrate-IS, NOT laboratory measurements OR
# container-quantities.

# ---------------------------------------------------------------------------
# NEUTRINO MASS-SQUARED SPLITTINGS (NuFit-6.0, 2024; COMPARISON ANCHORS ONLY)
# ---------------------------------------------------------------------------
# Laboratory-IN observational values used ONLY to SET THE ABSOLUTE eV SCALE
# of the framework neutrino sector (the substrate-IS m_i from D_K are raw
# |eigenvalue| magnitudes in M_KK units, quasi-degenerate, and carry the
# mass PATTERN but NOT the absolute scale). Per substrate-first-canonical-
# sourcing.md §(i): these are METHODOLOGICAL comparison anchors, never a
# canonical replacement for a substrate computation. NuFit-6.0 normal-
# ordering (NO) best-fit central values (www.nu-fit.org, 2024 release).
# Added S96 W4-3 (S96-MATTER-0NUBB PART 2 eV scale-setting).
dm2_21_NuFit = 7.49e-5     # eV^2; solar Delta m^2_21 (NuFit-6.0 NO best fit)
dm2_31_NuFit = 2.513e-3    # eV^2; atmospheric Delta m^2_31 (NuFit-6.0 NO best fit)
# 0nubb effective-mass experimental bounds (90% CL, comparison anchors):
m_betabeta_KamLANDZen = 0.122  # eV; KamLAND-Zen 800 upper limit (loose NME end; tight end ~0.028 eV)
m_betabeta_LEGEND200_reach = 0.075  # eV; LEGEND-200 design sensitivity (loose NME end ~0.018 eV)
m_betabeta_nextgen_reach = 0.010    # eV; next-gen (LEGEND-1000 / nEXO) target reach floor (~6-20 meV)
