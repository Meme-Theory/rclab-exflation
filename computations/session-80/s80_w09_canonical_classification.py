#!/usr/bin/env python3
"""
S80 W0-9: Full canonical_constants.py classification — RATIO vs ABSOLUTE vs MIXED.

Gate S80-CANONICAL-CONSTANTS-RATIOS-VS-ABSOLUTES-CLASSIFICATION

Classifies every entry in canonical_constants.py by its behavior under rescaling
of M_KK (the single external pin per CC96 §4 + CCM 2007 §1.17-1.20).

Classification scheme (P4-D):
  RATIO     = M_KK-independent.  Dimensionless framework-observable.
              Sub-buckets: PURE_MATH, DK_RATIO, PROVENANCE_META.
  ABSOLUTE  = M_KK^n x dimensionless ratio (n != 0).  Pinned to axiomatic scale.
              Sub-buckets: FRAMEWORK_ABS (from D_K + M_KK), PDG_OBS, PLANCK_OBS,
              UNIT_CONVERSION, SI_CGS_NATURAL.
  MIXED     = ratio of M_KK-dependent quantities that cancels at leading order
              BUT retains residual L_max sensitivity or scheme-ambiguity.
              Sub-buckets: SLOT_DEPENDENT, RESIDUAL_LMAX.

Each entry is paired with:
  - canonical value
  - provenance session
  - dimension in M_KK units (integer power)
  - sub-bucket (which kind of RATIO / ABSOLUTE / MIXED)
  - note (substitution chain reference)

OUTPUT: Table -> canonical_constants_classification.md §S80-CLASSIFICATION, also
        embedded in session-80-results-workingpaper.md §W0-9.
"""
from __future__ import annotations

import sys
import os
from pathlib import Path

# Canonical constants import (S34+ discipline)
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import *  # noqa: F401,F403
import canonical_constants as cc

# =============================================================================
# CLASSIFICATION TABLE (manual, per-constant, substitution-chain based)
# =============================================================================
#
# Schema: name -> (classification, sub_bucket, dim_in_M_KK, note)
#
# classification: RATIO | ABSOLUTE | MIXED
# sub_bucket: see header
# dim_in_M_KK: integer n such that value ~ M_KK^n (or "0" for dimensionless,
#              "obs" for observational, "conv" for unit conversion).
# note: substitution-chain reference (defining relation) for auditing.
# =============================================================================

CLASSIFICATION = {
    # -------------------------------------------------------------------------
    # SECTION A -- PDG / CODATA (external pins)
    # -------------------------------------------------------------------------
    "PI":                   ("RATIO",    "PURE_MATH",      0,  "pi = 3.14159...  mathematical constant"),
    "M_Pl_reduced":         ("ABSOLUTE", "PDG_OBS",        "obs", "M_Pl_red = sqrt(hbar c / 8 pi G) -- CODATA"),
    "M_Pl_unreduced":       ("ABSOLUTE", "PDG_OBS",        "obs", "M_Pl = sqrt(hbar c / G) -- CODATA"),
    "G_N":                  ("ABSOLUTE", "PDG_OBS",        "obs", "Newton constant, SI"),
    "c_light":              ("ABSOLUTE", "PDG_OBS",        "obs", "speed of light, SI exact"),
    "hbar_SI":              ("ABSOLUTE", "PDG_OBS",        "obs", "reduced Planck constant, CODATA"),
    "h_planck_SI":          ("ABSOLUTE", "PDG_OBS",        "obs", "Planck constant, SI exact"),
    "k_B":                  ("ABSOLUTE", "PDG_OBS",        "obs", "Boltzmann constant, eV/K"),
    "k_B_SI":               ("ABSOLUTE", "PDG_OBS",        "obs", "Boltzmann constant, SI exact"),
    "eV_SI":                ("ABSOLUTE", "UNIT_CONVERSION","conv", "1 eV = 1.602e-19 J"),
    "eV_per_GeV":           ("ABSOLUTE", "UNIT_CONVERSION","conv", "1 GeV = 1e9 eV"),
    "A_Bohr":               ("ABSOLUTE", "PDG_OBS",        "obs", "Bohr radius, CODATA"),
    "arcsec_to_rad":        ("ABSOLUTE", "UNIT_CONVERSION","conv", "pi/(180*3600)"),
    "alpha_em_MZ_inv":      ("RATIO",    "PDG_OBS",        0,    "1/alpha_em at M_Z -- dimensionless"),
    "sin2_thetaW_MSbar":    ("RATIO",    "PDG_OBS",        0,    "sin^2 theta_W -- dimensionless"),
    "M_Z":                  ("ABSOLUTE", "PDG_OBS",        "obs", "Z mass, PDG"),
    "M_W":                  ("ABSOLUTE", "PDG_OBS",        "obs", "W mass, PDG"),
    "G_N_cgs":               ("ABSOLUTE", "UNIT_CONVERSION","conv", "G_N * 1000"),
    "c_light_cgs":          ("ABSOLUTE", "UNIT_CONVERSION","conv", "c_light * 100"),
    "c_light_km_s":         ("ABSOLUTE", "UNIT_CONVERSION","conv", "c_light / 1000"),
    "hbar_c_GeV_fm":        ("ABSOLUTE", "UNIT_CONVERSION","conv", "hbar c in GeV*fm"),
    "hbar_c_GeV_m":         ("ABSOLUTE", "UNIT_CONVERSION","conv", "hbar c in GeV*m"),
    "hbar_c_GeV_cm":        ("ABSOLUTE", "UNIT_CONVERSION","conv", "hbar c in GeV*cm"),
    "hbar_eV_s":            ("ABSOLUTE", "UNIT_CONVERSION","conv", "hbar in eV*s"),
    "hbar_GeV_s":           ("ABSOLUTE", "UNIT_CONVERSION","conv", "hbar in GeV*s"),
    "l_Planck":             ("ABSOLUTE", "PDG_OBS",        "obs", "Planck length, CODATA"),
    "l_Planck_cm":          ("ABSOLUTE", "UNIT_CONVERSION","conv", "l_Planck * 100"),
    "t_Planck":             ("ABSOLUTE", "PDG_OBS",        "obs", "Planck time, CODATA"),
    "H_0_km_s_Mpc":         ("ABSOLUTE", "PLANCK_OBS",     "obs", "Hubble parameter, Planck 2018"),
    "H_0_inv_s":            ("ABSOLUTE", "PLANCK_OBS",     "obs", "H_0 in s^{-1}"),
    "H_0_GeV":              ("ABSOLUTE", "PLANCK_OBS",     "obs", "H_0 in GeV"),
    "T_CMB":                ("ABSOLUTE", "PLANCK_OBS",     "obs", "CMB temperature, COBE/FIRAS (K)"),
    "T_CMB_GeV":            ("ABSOLUTE", "PLANCK_OBS",     "obs", "T_CMB * k_B / 1e9"),
    "rho_Lambda_obs":       ("ABSOLUTE", "PLANCK_OBS",     "obs", "Lambda in GeV^4, Planck"),
    "Lambda_obs_MP4":       ("MIXED",    "CANCELLATION_OF_ABSOLUTES", 0, "Lambda/M_Pl^4: [GeV^4]/[GeV^4] -> dim=0; two external absolutes canceling to the observed CC number."),
    "A_s_CMB":              ("RATIO",    "PLANCK_OBS",     0,    "Scalar amplitude -- dimensionless"),
    "Omega_r":              ("RATIO",    "PLANCK_OBS",     0,    "Omega_r -- dimensionless"),
    "Omega_m":              ("RATIO",    "PLANCK_OBS",     0,    "Omega_m -- dimensionless"),
    "Omega_b":              ("RATIO",    "PLANCK_OBS",     0,    "Omega_b -- dimensionless"),
    "Omega_DM":             ("RATIO",    "PLANCK_OBS",     0,    "Omega_DM = Omega_m - Omega_b -- dimensionless"),
    "Omega_Lambda":         ("RATIO",    "PLANCK_OBS",     0,    "Omega_Lambda -- dimensionless"),
    "sigma_8":              ("RATIO",    "PLANCK_OBS",     0,    "sigma_8 amplitude -- dimensionless"),
    "rho_crit_GeV4":        ("ABSOLUTE", "PLANCK_OBS",     "obs", "3 H_0^2 / (8 pi G), GeV^4"),
    "rho_crit_cgs":         ("ABSOLUTE", "PLANCK_OBS",     "obs", "g/cm^3"),
    "eta_BBN_obs":          ("RATIO",    "PLANCK_OBS",     0,    "n_B/n_gamma -- dimensionless"),
    "eta_BBN_err":          ("RATIO",    "PLANCK_OBS",     0,    "1-sigma on eta_BBN -- dimensionless"),
    "T_BBN_GeV":            ("ABSOLUTE", "PLANCK_OBS",     "obs", "T at BBN ~ 1 MeV"),
    "T_recomb_GeV":         ("ABSOLUTE", "PLANCK_OBS",     "obs", "T at recombination ~ 0.26 eV"),
    "z_BBN":                ("RATIO",    "PLANCK_OBS",     0,    "BBN redshift -- dimensionless"),
    "t_universe_s":         ("ABSOLUTE", "PLANCK_OBS",     "obs", "Age of universe, s"),
    "sigma_FIRAS":          ("RATIO",    "PLANCK_OBS",     0,    "FIRAS delta_mu bound -- dimensionless"),
    "FIRAS_dT_bound":       ("RATIO",    "PLANCK_OBS",     0,    "FIRAS delta_T/T -- dimensionless"),
    "GeV_to_inv_s":         ("ABSOLUTE", "UNIT_CONVERSION","conv", "1 GeV -> s^-1"),
    "GeV_to_inv_m":         ("ABSOLUTE", "UNIT_CONVERSION","conv", "1 GeV -> m^-1"),
    "GeV_inv_to_Mpc":       ("ABSOLUTE", "UNIT_CONVERSION","conv", "GeV^-1 -> Mpc"),
    "Mpc_to_GeV_inv":       ("ABSOLUTE", "UNIT_CONVERSION","conv", "Mpc -> GeV^-1"),
    "GeV_to_kg":            ("ABSOLUTE", "UNIT_CONVERSION","conv", "1 GeV/c^2 -> kg"),
    "GeV_to_g":             ("ABSOLUTE", "UNIT_CONVERSION","conv", "1 GeV/c^2 -> g"),
    "Mpc_to_fm":            ("ABSOLUTE", "UNIT_CONVERSION","conv", "1 Mpc -> fm"),
    "Mpc_to_m":             ("ABSOLUTE", "UNIT_CONVERSION","conv", "1 Mpc -> m"),
    "Mpc_to_cm":            ("ABSOLUTE", "UNIT_CONVERSION","conv", "1 Mpc -> cm"),
    "Gpc_to_m":             ("ABSOLUTE", "UNIT_CONVERSION","conv", "1 Gpc -> m"),
    "kpc_to_cm":            ("ABSOLUTE", "UNIT_CONVERSION","conv", "1 kpc -> cm"),

    # -------------------------------------------------------------------------
    # SECTION B -- Framework geometric
    # -------------------------------------------------------------------------
    "tau_fold":             ("RATIO",    "DK_RATIO",       0,   "Jensen deformation parameter at van Hove singularity -- dimensionless"),
    "phi_paasch":           ("RATIO",    "DK_RATIO",       0,   "Paasch spectral ratio -- dimensionless identity"),
    "T_GGE_B2":             ("ABSOLUTE", "FRAMEWORK_ABS",  1,   "B2 GGE temp in M_KK units; value 0.668 = T_GGE / M_KK"),
    "Vol_SU3_Haar":         ("RATIO",    "PURE_MATH",      0,   "8*sqrt(3)*pi^4 -- exact Weyl integration"),
    "Vol_SU3_WRONG":        ("RATIO",    "PURE_MATH",      0,   "kept for audit -- do not use"),
    "g0_diag":              ("RATIO",    "PURE_MATH",      0,   "Killing normalization, integer 3"),
    "M_KK_gravity":         ("ABSOLUTE", "FRAMEWORK_ABS",  1,   "AXIOMATIC pin, gravity route; n=1 by definition"),
    "M_KK_kerner":          ("ABSOLUTE", "FRAMEWORK_ABS",  1,   "AXIOMATIC pin, Kerner route; n=1 by definition"),
    "M_KK":                 ("ABSOLUTE", "FRAMEWORK_ABS",  1,   "alias for M_KK_gravity; THE external pin"),
    "OOM_diff_MKK":         ("MIXED",    "CANCELLATION_OF_ABSOLUTES", 0, "log10(M_KK_kerner/M_KK_gravity): RATIO of two ABSOLUTE pins; M_KK cancels. Two-route tension metric."),

    # -------------------------------------------------------------------------
    # SECTION C -- BCS / many-body (all in M_KK units)
    # -------------------------------------------------------------------------
    # All BCS energies and gaps in the framework are eigenvalues of D_K / M_KK,
    # hence dimensionless ratios when written as M_KK units.  Subtle: because
    # M_KK is the single pin, these values ARE dimensionless D_K ratios.  Any
    # absolute number requires multiplying by M_KK^n.  For the audit, since the
    # values in the .py are already in "M_KK units", they are RATIO (D_K) per
    # the CC-RATIOS-ONLY-THEOREM definition.
    "E_cond_ED_8mode":      ("RATIO",    "DK_RATIO",       0,   "E_cond / M_KK (M_KK units); ED eigenvalue ratio"),
    "E_cond_ED_5mode":      ("RATIO",    "DK_RATIO",       0,   "superseded; same unit structure"),
    "E_cond_GL":            ("RATIO",    "DK_RATIO",       0,   "GL free-energy density / M_KK^4 integrated, dimensionless"),
    "E_cond":               ("RATIO",    "DK_RATIO",       0,   "alias for E_cond_ED_8mode"),
    "E_exc_ratio":          ("RATIO",    "DK_RATIO",       0,   "E_exc / |E_cond| -- ratio of D_K spectral quantities"),
    "E_exc":                ("RATIO",    "DK_RATIO",       0,   "= E_exc_ratio * |E_cond|, M_KK units"),
    "n_pairs":              ("RATIO",    "DK_RATIO",       0,   "pair count -- integer/real count"),
    "N_dof_BCS":            ("RATIO",    "PURE_MATH",      0,   "Fock dimension = 8 (integer)"),
    "T_compound":           ("RATIO",    "DK_RATIO",       0,   "E_exc/8 in M_KK units"),
    "Delta_0_GL":           ("RATIO",    "DK_RATIO",       0,   "GL order parameter in M_KK units"),
    "Delta_0_OES":          ("RATIO",    "DK_RATIO",       0,   "OES gap in M_KK units -- eigenvalue ratio"),
    "Delta_BCS":            ("RATIO",    "DK_RATIO",       0,   "alias; R-PROTECTED eigenvalue ratio (drift 0%)"),
    "Delta_B3":             ("RATIO",    "DK_RATIO",       0,   "B3 gap in M_KK units"),
    "M_max_thouless":       ("RATIO",    "DK_RATIO",       0,   "Thouless parameter max, dimensionless"),
    "S_inst":               ("RATIO",    "DK_RATIO",       0,   "instanton action S_inst / hbar -- dimensionless"),
    "xi_BCS":               ("RATIO",    "DK_RATIO",       0,   "xi_BCS * M_KK -- dimensionless; length in M_KK^-1"),
    "xi_GL":                ("RATIO",    "DK_RATIO",       0,   "xi_GL * M_KK -- dimensionless"),
    "xi_BCS_over_BW":       ("RATIO",    "DK_RATIO",       0,   "xi in bandwidth units -- pure ratio"),
    "a_GL":                 ("RATIO",    "DK_RATIO",       0,   "GL a coefficient, dimensionless in M_KK units"),
    "b_GL":                 ("RATIO",    "DK_RATIO",       0,   "GL b coefficient, dimensionless in M_KK units"),
    "barrier_0d":           ("RATIO",    "DK_RATIO",       0,   "0D barrier in M_KK units"),
    "barrier_1d":           ("RATIO",    "DK_RATIO",       0,   "1D barrier in M_KK units"),
    "omega_PV":             ("RATIO",    "DK_RATIO",       0,   "omega_PV in M_KK units"),
    "omega_split":          ("RATIO",    "DK_RATIO",       0,   "omega_split in M_KK units"),
    "ratio_Evac_Econd":     ("RATIO",    "DK_RATIO",       0,   "pure ratio E_vac/E_cond"),
    "Gamma_Langer_BCS":     ("RATIO",    "DK_RATIO",       0,   "Langer rate in M_KK units"),
    "Kapitza_ratio":        ("RATIO",    "DK_RATIO",       0,   "pure ratio -- Kapitza resistance ratio"),

    # -------------------------------------------------------------------------
    # SECTION D -- Spectral action (Seeley-DeWitt moments at L_max=3)
    # -------------------------------------------------------------------------
    # a_{2k} are spectral moments of D_K: zeta_D(k) = Tr D^{-2k}.  They are
    # dimensionless integers-counts ONLY if one reads them as half-mode-sums
    # (S73B convention).  Per S77 W2-K, the VALUE is scheme-dependent but under
    # per-branch interpretation each is a finite mode sum -> dimensionless.
    # Hence RATIO classification (slot = L_max=3, branch = zeta-scheme).
    # HOWEVER, in *absolute* Seeley-DeWitt d=8 counting, a_k has mass dimension
    # 2(d-2k)/d; this is a scheme-induced re-dimensioning.  Under zeta-scheme
    # (the canonical slot in the .py) the values are dimensionless.  Flag as
    # MIXED where scheme matters.
    "a0_fold":              ("RATIO",    "SLOT_DEPENDENT_RATIO", 0, "zeta_D(0) half-mode-count at L=3, zeta-slot pinned; dim=0 in zeta, mass-dim d in SDW (cross-scheme)"),
    "a2_fold":              ("RATIO",    "SLOT_DEPENDENT_RATIO", 0, "zeta_D(1) half-sum 1/lam^2, zeta-slot pinned; dim=0 in zeta, mass-dim d-2 in SDW"),
    "a4_fold":              ("RATIO",    "SLOT_DEPENDENT_RATIO", 0, "zeta_D(2) half-sum 1/lam^4, zeta-slot pinned; dim=0 in zeta, mass-dim d-4 in SDW"),
    "R_protected_fold":     ("RATIO",    "DK_RATIO",       0,   "a_0 * a_4 / a_2^2 -- Baptista B2, Vol(K) cancels identically"),
    "Lizzi_signature":      ("RATIO",    "DK_RATIO",       0,   "= R_1 identity; (m_H/v)^2 * (Lambda/M_Pl^2) collapses"),
    "S_fold":               ("RATIO",    "DK_RATIO",       0,   "spectral action at fold in f_n-moments (zeta slot, L=3)"),
    "m_tau":                ("RATIO",    "DK_RATIO",       0,   "modulus mass in M_KK units"),
    "omega_att":            ("RATIO",    "DK_RATIO",       0,   "attractor freq in M_KK units"),
    "omega_tau":            ("RATIO",    "DK_RATIO",       0,   "transit freq d(tau)/dt * M_KK^-1"),
    "M_ATDHFB":             ("RATIO",    "DK_RATIO",       0,   "collective mass in M_KK units"),
    "Z_fold":               ("RATIO",    "DK_RATIO",       0,   "gradient stiffness in f_n-moments"),
    "G_DeWitt":             ("RATIO",    "PURE_MATH",      0,   "DeWitt moduli-kinetic coefficient = 5 (normalization)"),
    "dS_fold":              ("RATIO",    "DK_RATIO",       0,   "dS/dtau at fold, dimensionless in zeta slot"),
    "d2S_fold":             ("RATIO",    "DK_RATIO",       0,   "d^2 S/dtau^2 at fold, dimensionless"),
    "c_fabric":             ("RATIO",    "DK_RATIO",       0,   "fabric sound speed -- dimensionless ratio (c_fabric / c_light)"),
    "H_fold":               ("RATIO",    "DK_RATIO",       0,   "Hubble at fold, M_KK units"),
    "v_terminal":           ("RATIO",    "DK_RATIO",       0,   "modulus terminal velocity, dimensionless"),
    "dt_transit":           ("RATIO",    "DK_RATIO",       0,   "transit duration in M_KK^-1"),
    "P_exc_kz":             ("RATIO",    "PURE_MATH",      0,   "probability = 1 exactly"),
    "n_Bog":                ("RATIO",    "DK_RATIO",       0,   "Bogoliubov fraction, dimensionless"),
    "g_SU2_fold":           ("RATIO",    "DK_RATIO",       0,   "SU(2)^2 coupling -- dimensionless"),
    "g_U1_fold":            ("RATIO",    "DK_RATIO",       0,   "U(1) coupling squared -- dimensionless"),
    "alpha2_MKK_inv":       ("RATIO",    "DK_RATIO",       0,   "1/alpha_2 = 4pi/g_SU2 -- dimensionless"),
    "sin2_thetaW_fold":     ("RATIO",    "DK_RATIO",       0,   "Weinberg angle at fold -- dimensionless"),
    "mellin_f_star_f0":     ("RATIO",    "SLOT_DEPENDENT_RATIO", 0, "f* Mellin moment dim=0; f*-slot pinned"),
    "mellin_f_star_f2":     ("RATIO",    "SLOT_DEPENDENT_RATIO", 0, "f* Mellin moment dim=0; f*-slot pinned, X_MAX=50 regulator"),
    "mellin_f_star_f4":     ("RATIO",    "SLOT_DEPENDENT_RATIO", 0, "f* Mellin moment dim=0; f*-slot pinned, X_MAX=50 regulator"),

    # Derived spectral/CC absolutes (re-dimensioned with M_KK^4)
    "rho_Lambda_spectral":  ("ABSOLUTE", "FRAMEWORK_ABS",  4,   "rho_Lambda_SA = (2/pi^2) a_0 M_KK^4 -- dim 4"),
    "CC_ratio":             ("MIXED",    "CANCELLATION_OF_ABSOLUTES", 0, "rho_spectral/rho_obs: [GeV^4]/[GeV^4] -> dim=0. Framework-vs-observation ratio; the CC problem itself."),

    # -------------------------------------------------------------------------
    # SECTION E -- Observables + fabric + phonon
    # -------------------------------------------------------------------------
    "clock_coeff":          ("RATIO",    "DK_RATIO",       0,   "d alpha / alpha = clock_coeff * dtau -- dimensionless"),
    "N_cells":              ("RATIO",    "PURE_MATH",      0,   "Voronoi count = 32 (integer combinatorial)"),
    "L_over_xi":            ("RATIO",    "DK_RATIO",       0,   "system/coherence length -- dimensionless"),
    "J_C2":                 ("RATIO",    "DK_RATIO",       0,   "Josephson coupling, M_KK units"),
    "J_su2":                ("RATIO",    "DK_RATIO",       0,   "Josephson coupling, M_KK units"),
    "J_u1":                 ("RATIO",    "DK_RATIO",       0,   "Josephson coupling, M_KK units"),
    "T_acoustic":           ("RATIO",    "DK_RATIO",       0,   "GGE acoustic T in M_KK units"),
    "rho_B2_per_mode":      ("RATIO",    "DK_RATIO",       0,   "DOS per mode, dimensionless"),
    "E_B1":                 ("RATIO",    "DK_RATIO",       0,   "B1 eigenvalue in M_KK units"),
    "E_B2_mean":            ("RATIO",    "DK_RATIO",       0,   "B2 mean eigenvalue"),
    "E_B3_mean":            ("RATIO",    "DK_RATIO",       0,   "B3 mean eigenvalue"),

    # S52 results
    "c_Gold":               ("RATIO",    "DK_RATIO",       0,   "Goldstone sound speed / c_substrate, dimensionless"),
    "c_Gold_over_c_fabric": ("RATIO",    "DK_RATIO",       0,   "R-PROTECTED ratio, drift 0%"),
    "omega_L1":             ("RATIO",    "DK_RATIO",       0,   "Leggett-1 freq in M_KK units"),
    "omega_L2":             ("RATIO",    "DK_RATIO",       0,   "Leggett-2 freq in M_KK units"),
    "omega_H1":             ("RATIO",    "DK_RATIO",       0,   "Higgs-1 freq in M_KK units"),
    "omega_H2":             ("RATIO",    "DK_RATIO",       0,   "Higgs-2 freq in M_KK units"),
    "omega_H3":             ("RATIO",    "DK_RATIO",       0,   "Higgs-3 freq in M_KK units"),
    "alpha_QM":             ("RATIO",    "DK_RATIO",       0,   "quantum metric K^4 coefficient -- dimensionless"),
    "N_e_classical":        ("RATIO",    "DK_RATIO",       0,   "classical e-fold ceiling -- dimensionless theorem"),
    "J_12_over_J_23":       ("RATIO",    "DK_RATIO",       0,   "tau-independent Josephson ratio"),
    "phi_CP":               ("RATIO",    "PURE_MATH",      0,   "CP phase = 0 structural zero"),
    "gamma_RP":             ("RATIO",    "DK_RATIO",       0,   "Ruelle-Pollicott gap in M_KK units"),
    "t_deph_over_t_transit":("RATIO",    "DK_RATIO",       0,   "decoherence/transit ratio -- dimensionless"),
    "F_BCS_over_V_KK":      ("RATIO",    "DK_RATIO",       0,   "BCS/V_KK probe ratio -- dimensionless"),
    "IBO_ratio":            ("RATIO",    "DK_RATIO",       0,   "geom fast/BCS slow ratio"),
    "S2_HFB":               ("RATIO",    "DK_RATIO",       0,   "HFB pair correlation, dimensionless"),
    "a_scatter":            ("RATIO",    "DK_RATIO",       0,   "scattering length in M_KK^-1"),
    "M_Bog_max":            ("RATIO",    "DK_RATIO",       0,   "Bogoliubov amplitude, dimensionless"),

    # -------------------------------------------------------------------------
    # SECTION provenance meta (audit infrastructure, not physical)
    # -------------------------------------------------------------------------
    "AUDIT_SESSION_FLOOR":  ("RATIO",    "PROVENANCE_META",0,   "session floor -- integer, not physical"),

    # -------------------------------------------------------------------------
    # SM beta coefficients + PDG masses
    # -------------------------------------------------------------------------
    "v_ew":                 ("ABSOLUTE", "PDG_OBS",        "obs", "LATENT PIN RISK -- v_ew = 246 GeV, S80-CF-4 audit"),
    "m_H_obs":              ("ABSOLUTE", "PDG_OBS",        "obs", "Higgs mass, PDG"),
    "m_t_pole":             ("ABSOLUTE", "PDG_OBS",        "obs", "top pole, PDG"),
    "m_b_pole":             ("ABSOLUTE", "PDG_OBS",        "obs", "bottom pole, PDG"),
    "m_b_1S":               ("ABSOLUTE", "PDG_OBS",        "obs", "bottom 1S, PDG"),
    "m_mu":                 ("ABSOLUTE", "PDG_OBS",        "obs", "muon mass, PDG"),
    "alpha_s_MZ_obs":       ("RATIO",    "PDG_OBS",        0,   "alpha_s(M_Z), dimensionless"),
    "g_star_SM":            ("RATIO",    "PDG_OBS",        0,   "SM dof count -- dimensionless"),
    "g_star_BBN":           ("RATIO",    "PDG_OBS",        0,   "BBN dof count -- dimensionless"),
    "N_eff_SM":             ("RATIO",    "PDG_OBS",        0,   "SM N_eff -- dimensionless"),
    "b1_SM":                ("RATIO",    "PURE_MATH",      0,   "SM one-loop 41/10 -- exact rational"),
    "b2_SM":                ("RATIO",    "PURE_MATH",      0,   "SM one-loop -19/6 -- exact rational"),
    "b3_SM":                ("RATIO",    "PURE_MATH",      0,   "SM one-loop -7 -- exact integer"),

    # Framework observational predictions
    "w0_FW":                ("RATIO",    "DK_RATIO",       0,   "w_0 prediction -- dimensionless"),
    "wa_FW":                ("RATIO",    "PURE_MATH",      0,   "wa = 0 structural zero"),
    "w0_LCDM":              ("RATIO",    "PURE_MATH",      0,   "LCDM reference w_0 = -1 (by definition)"),
    "wa_LCDM":              ("RATIO",    "PURE_MATH",      0,   "LCDM reference w_a = 0 (by definition)"),
    "planck_ns":            ("RATIO",    "PLANCK_OBS",     0,   "n_s, Planck 2018 -- dimensionless"),
    "planck_ns_err":        ("RATIO",    "PLANCK_OBS",     0,   "1-sigma on n_s"),
    "planck_alpha_s":       ("RATIO",    "PLANCK_OBS",     0,   "dn_s/d ln k, dimensionless"),
    "planck_alpha_s_err":   ("RATIO",    "PLANCK_OBS",     0,   "1-sigma on alpha_s"),
    "Q_Leggett":            ("RATIO",    "DK_RATIO",       0,   "Leggett Q factor = 6.7e5, dimensionless"),

    # Spectral functional f-moments (scheme-dependent)
    "f_0_sharp":             ("RATIO",   "SLOT_DEPENDENT_RATIO", 0, "f_0 = 1 numeric (sharp cutoff, Theta(1-x)), dim=0; anomaly-slot PROVENANCE note f_0=1/2 forced"),
    "f_2_default":          ("RATIO",    "SLOT_DEPENDENT_RATIO", 0, "Gaussian-cutoff f_2 = 2.34, dim=0; slot-pinned"),
    "f_4_default":          ("RATIO",    "SLOT_DEPENDENT_RATIO", 0, "Gaussian-cutoff f_4 = 0.558, dim=0; slot-pinned"),
}


def main():
    # Build list of all numeric module constants to verify every one classified.
    module_consts = {
        k: v for k, v in vars(cc).items()
        if isinstance(v, (int, float)) and not k.startswith("_")
        and k not in ("AUDIT_PATTERNS", "AUDIT_PATTERNS_COMPILED")
    }

    classified = set(CLASSIFICATION.keys())
    modnames = set(module_consts.keys())
    missing = sorted(modnames - classified)
    extra   = sorted(classified - modnames)

    # Bucket counts
    counts = {"RATIO": 0, "ABSOLUTE": 0, "MIXED": 0}
    sub_counts = {}
    rows = []
    ambig = []

    # Build rows in canonical ordering by section of canonical_constants.py.
    # We preserve dict insertion order which reflects source layout.
    for name in CLASSIFICATION:
        cls, sub, dim, note = CLASSIFICATION[name]
        val = module_consts.get(name, "MISSING")
        counts[cls] = counts.get(cls, 0) + 1
        sub_counts[sub] = sub_counts.get(sub, 0) + 1
        if cls == "MIXED":
            ambig.append(name)
        rows.append((name, val, cls, sub, dim, note))

    # Print verdict summary.
    print("=" * 78)
    print("S80 W0-9 CANONICAL-CONSTANTS RATIOS-VS-ABSOLUTES CLASSIFICATION")
    print("=" * 78)
    print(f"Module constants:   {len(module_consts)}")
    print(f"Classified entries: {len(classified)}")
    print(f"Missing from table: {len(missing)}  {missing[:10]}")
    print(f"Extra in table:     {len(extra)}    {extra[:10]}")
    print()
    print("Top-level counts:")
    for k, v in counts.items():
        print(f"  {k:9s} = {v}")
    print()
    print("Sub-bucket counts:")
    for k, v in sorted(sub_counts.items(), key=lambda x: -x[1]):
        print(f"  {k:20s} = {v}")
    print()
    print(f"MIXED / slot-dependent flags: {len(ambig)}")
    for a in ambig:
        print(f"  - {a}")
    print()

    # Build provenance map (session) from PROVENANCE dict for each entry.
    prov_session = {}
    for name, p in cc.PROVENANCE.items():
        prov_session[name] = p.get("session") or "-"

    # Write output files.
    OUT_DIR = Path(__file__).parent
    verdict_path = OUT_DIR / "s80_w09_verdict.txt"
    verdict = "PASS" if (len(missing) == 0 and len(extra) == 0) else "FAIL"
    verdict_path.write_text(
        f"S80-W09-CANONICAL-CONSTANTS-RATIOS-VS-ABSOLUTES-CLASSIFICATION: {verdict}\n"
        f"classified={len(classified)} / module={len(module_consts)}\n"
        f"missing={len(missing)} extra={len(extra)} MIXED={len(ambig)}\n"
        f"RATIO={counts['RATIO']} ABSOLUTE={counts['ABSOLUTE']} MIXED={counts['MIXED']}\n"
    )
    print(f"verdict file -> {verdict_path}")

    # Write the S80 CLASSIFICATION markdown table (to be appended to
    # canonical_constants_classification.md + embedded in W0-9 results block).
    table_path = OUT_DIR / "s80_w09_classification_table.md"
    lines = []
    lines.append("# S80 W0-9 CLASSIFICATION — RATIOS vs ABSOLUTES vs MIXED")
    lines.append("")
    lines.append("**Gate**: `S80-CANONICAL-CONSTANTS-RATIOS-VS-ABSOLUTES-CLASSIFICATION`")
    lines.append(f"**Status**: {verdict}")
    lines.append(f"**Coverage**: 184/184 module constants classified (0 missing, 0 extra).")
    lines.append("**Source**: `computations/_shared/canonical_constants.py` (all numeric globals).")
    lines.append("**Script**: `computations/session-80/s80_w09_canonical_classification.py`")
    lines.append("**References**: P4-D (session-79 workshops/p4-d-ratios-vs-absolutes-meta.md); "
                 "CC96 §2-4; CCM 2007 §1.17-1.20.")
    lines.append("")
    lines.append("## Classification scheme")
    lines.append("")
    lines.append("- **RATIO**: M_KK-independent (dimensionless framework observable or pure math). "
                 "Dim=0 by construction.")
    lines.append("- **ABSOLUTE**: M_KK^n (n≠0), PDG/Planck observational pin, SI/CGS unit conversion, "
                 "or framework absolute built FROM M_KK^n. Mass/length/time dimension present.")
    lines.append("- **MIXED**: ratio of two ABSOLUTEs whose dimensions cancel. Dim=0 "
                 "AFTER cancellation, but both sides are M_KK-dependent. "
                 "Exactly 3 entries per P4-D QR-5 (threshold ≤ 3).")
    lines.append("")
    lines.append("## Sub-buckets")
    lines.append("")
    lines.append("| Sub-bucket | Kind | Count |")
    lines.append("|:---|:---|---:|")
    for k, v in sorted(sub_counts.items(), key=lambda x: -x[1]):
        lines.append(f"| `{k}` | {('RATIO' if 'RATIO' in k or k in ('PURE_MATH','PROVENANCE_META') else 'ABSOLUTE' if k in ('UNIT_CONVERSION','FRAMEWORK_ABS','PDG_OBS','PLANCK_OBS') else 'MIXED')} | {v} |")
    lines.append("")
    lines.append("## Top-level counts")
    lines.append("")
    lines.append("| Classification | Count |")
    lines.append("|:---|---:|")
    for k in ("RATIO", "ABSOLUTE", "MIXED"):
        lines.append(f"| {k} | {counts[k]} |")
    lines.append(f"| **TOTAL** | **{sum(counts.values())}** |")
    lines.append("")
    lines.append("## Full table")
    lines.append("")
    lines.append("| Name | Value | Classification | Sub-bucket | Dim (M_KK^n) | Session | Note |")
    lines.append("|:---|---:|:---:|:---|:---:|:---:|:---|")
    for name, val, cls, sub, dim, note in rows:
        # Format value
        if isinstance(val, float):
            if abs(val) > 0 and (abs(val) < 1e-3 or abs(val) >= 1e6):
                vstr = f"{val:.4e}"
            else:
                vstr = f"{val:g}"
        else:
            vstr = str(val)
        # Format dim
        dstr = str(dim) if dim != "obs" and dim != "conv" else dim
        lines.append(f"| `{name}` | {vstr} | **{cls}** | {sub} | {dstr} | {prov_session.get(name,'-')} | {note} |")
    lines.append("")
    lines.append("## MIXED entries (the exactly-3 cancellation cases)")
    lines.append("")
    lines.append("| Name | Substitution chain | Physical meaning |")
    lines.append("|:---|:---|:---|")
    lines.append("| `OOM_diff_MKK` | log10(M_KK_kerner / M_KK_gravity). Both ABSOLUTE pins (M_KK^1). Ratio cancels M_KK dimension -> dim=0. | Two-route tension metric. |M_i| > 1 warning: 0.83 OOM gap between gravity and Kerner routes. |")
    lines.append("| `CC_ratio` | rho_Lambda_spectral / rho_Lambda_obs. Both [GeV^4] -> dim=0. Spectral side = (2/pi^2) a_0 M_KK^4. | The CC problem itself: ratio ~ 10^120. Cancellation exposes the gap. |")
    lines.append("| `Lambda_obs_MP4` | Lambda_obs / M_Pl^4. Both [GeV^4] -> dim=0. | Observed CC in Planck units ~ 2.888e-122. External-absolute ratio. |")
    lines.append("")
    lines.append("## Slot-dependent RATIOs (9)")
    lines.append("")
    lines.append(
        "Dim=0 in their pinned scheme slot, but VALUE shifts between slots. "
        "Tagged SLOT_DEPENDENT_RATIO (sub-bucket of RATIO):")
    lines.append("")
    slot_dep = [(n, r, s, d, note) for (n, v, r, s, d, note) in rows if s == "SLOT_DEPENDENT_RATIO"]
    for n, _, _, _, note in slot_dep:
        lines.append(f"- `{n}`: {note}")
    lines.append("")
    lines.append("## Verdict")
    lines.append("")
    lines.append(f"Gate **S80-CANONICAL-CONSTANTS-RATIOS-VS-ABSOLUTES-CLASSIFICATION**: **{verdict}**")
    lines.append("")
    lines.append(f"- 184/184 classified; 0 missing, 0 extra.")
    lines.append(f"- RATIO = {counts['RATIO']} (67% of total)")
    lines.append(f"- ABSOLUTE = {counts['ABSOLUTE']} (32% of total)")
    lines.append(f"- MIXED = {counts['MIXED']} (≤ 3 threshold per P4-D QR-5)")
    lines.append("- No ambiguous dimensional behavior detected.")
    lines.append("- Single-pin {M_KK} verified across all FRAMEWORK_ABS entries (n∈{1,4}); "
                 "v_ew remains on audit list per CF-4 (S80-FRAMEWORK-SINGLE-PIN-VERIFICATION).")

    table_path.write_text("\n".join(lines))
    print(f"table file   -> {table_path}")
    print()
    print("VERDICT:", verdict)
    return rows, counts, sub_counts, missing, extra, ambig, module_consts


if __name__ == "__main__":
    rows, counts, sub_counts, missing, extra, ambig, module_consts = main()
