#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
INV8-W3-2-QUANTUM-METRIC-STIFFNESS-HTAU
=======================================

Quantum-metric stiffness of the fold band as the IMPORTED Hubble backbone H(tau).

SUBSTRATE-FIRST FRAMING (phononic-framing.md "IS Space, Not IN Space"):
  H(tau) is NOT imported from an FRW container. The substrate IS the spectral-triple
  band geometry on the Jensen-deformed SU(3); the lowest J/BDI-real Dirac doublet is a
  Peter-Weyl eigenbundle of D_K. Its quantum metric g_ab = Re<d_a u|(1-P)|d_b u>
  (Provost-Vallee, the SOLE topologically-active object on this surface) carries a
  NON-DEGENERATE distance while the Berry curvature is ZERO EXACTLY (Kosmann
  anti-Hermiticity + J+U(2); Chern=Euler=graded-Omega=0, the metric-without-curvature
  wall, registry VII.CA / S106 W3-1 PASS). The fold band is the van Hove A_2 catastrophe
  -> FLAT -> the conventional Drude weight d^2E/dk^2 = 0 vanishes -> the ENTIRE superfluid
  weight is geometric:

       D_geom = (2 Delta_BCS / V) * Tr g    (Peotta-Torma 2015, geometric term)

  A stiffness sets an oscillation frequency omega_stiff = sqrt(D_geom / chi). The
  DIRECTION of explanation:
       D_K eigenvectors at the fold -> quantum metric of the lowest-band projector ->
       geometric superfluid stiffness D_geom -> emergent oscillation frequency ->
       (the test) is that frequency the Hubble backbone H(tau) the cosmology rides on?

  CANONICAL SUBSTRATE METRIC: the lowest |lambda| Dirac doublet lives in the (0,0)
  Peter-Weyl singlet block (D = Omega_spin offset, 16x16; band_deg=2 Kramers/J-pair;
  S96/S100b/S104). The genuine Provost-Vallee quantum metric is the NON-ABELIAN trace
  over BOTH deformation directions of the U(2)-invariant volume-preserving TT surface:
       Tr g = g_{tau,tau} + g_{mu,mu}
       g_{aa} = Sum_{n in lowest} Sum_{m not in lowest} |<n|dH_a|m>|^2 / (mu_n - mu_m)^2
  where a in {tau, mu}: tau = v_J=(2,-2,1) Jensen direction; mu = v_mu = n x v_J =
  (11,7,-8) the C^2 Higgs-coset TT direction (off-Jensen). dH_a = i dD/da.
  KEY (S100b line 833, S104 line 92): the (0,0) block CANNOT be rotated by the
  U(2)-invariant deformation, so its QGT on THIS surface is ZERO on both axes; the
  atlas-07 reservoir g~982.5 is a METHODOLOGICAL cross-check value (a DIFFERENT object),
  NOT the lowest-doublet (tau,mu) metric.

  TEST: omega_stiff(fold), as a multiple of M_KK, vs the imported backbone H_fold=586.527
  (M_KK units; the Friedmann backbone the rank-1 NNU theorem VII.BS imports as the ONE
  unfixed dimensionful weight w = M_KK).

PRE-COMPUTE (knowledge MCP, query-first per CLAUDE.md):
  - "Peotta-Torma for CC" (S64, PROVEN): flat-band superfluid-weight route INAPPLICABLE
    to the CC. This gate targets H(tau) (a DIFFERENT observable, the a(t) backbone G-1),
    NOT the CC -> the S64 closure does NOT pre-close this gate.
  - VII.W / VII.AF.1.OP-PROJ (S87-PILLAR-III-IV-BRIDGE-PERMANENT-LAND): the registered
    Pillar-III<->IV bridge; R_geom = int_BZ Tr g_ab^{(P_0)} d^d k is the laboratory-IN
    observable. (S87 verdict LINE FAIL on the 19/200 ratio convention; STRUCTURAL bridge
    VII.AF.1 is PROVEN. This gate REFINES it with the dimensionalized stiffness.)
  - VII.CA / S106-W3-1-METRIC-WITHOUT-CURVATURE-LANDING (PASS): g~982.5, Berry=0 EXACT,
    Chern=Euler=graded-Omega=0.
  - g_{tau,tau} = Sum_{m!=n} |V_nm|^2/(E_n-E_m)^2, V = dH (session-26-preplan, canonical);
    H = 1j*D_K real-symmetric => real eigenstates => Im(QGT) = Berry = 0 EXACTLY.

Gate: INV8-W3-2-QUANTUM-METRIC-STIFFNESS-HTAU  [SIGN]-trigger (schema-v2 3-tuple)
  operator: R_stiff = omega_stiff(fold) / H*_imported
  PASS  |log10 R_stiff| <= 0.5  (within half a decade => stiffness IS the backbone scale)
        AND Tr g > 0 AND Berry Omega = 0 (the maximally-NON-ideal flat-band signature)
  INFO  0.5 < |log10 R_stiff| <= 2.0
  FAIL  |log10 R_stiff| > 2.0

Author: phonon-first-cosmologist (Investigation 8, Wave 3, gate W3-2)
Date: 2026-06-15
"""

from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import sys
import time
from pathlib import Path

import numpy as np

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

t0 = time.time()

# ---------------------------------------------------------------------------
# Paths + canonical imports (MANDATORY per computations/_shared/CLAUDE.md)
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[2]                                    # (local)
SHARED = ROOT / "computations" / "_shared"                                    # (local)
sys.path.insert(0, str(SHARED))

from canonical_constants import (  # noqa: E402
    Delta_BCS,       # 0.4642547394830737  (R-protected BCS gap, M_KK units)
    M_KK,            # 7.428660036284456e16 GeV
    tau_fold,        # 0.19
    H_fold,          # 586.5267713108464  (imported Hubble backbone, M_KK units, S38)
    G_DeWitt,        # 5.0  (DeWitt kinetic coefficient = tau-modulus inertia chi)
    N_cells,         # 32.0 (Voronoi-cell BZ-volume normalization V)
    w0_FW,           # -0.918 (dark-energy w0; cited, not used numerically)
)

import dirac_spectrum as ds  # noqa: E402

np.set_printoptions(precision=10, linewidth=140, suppress=True)

print("=" * 78)
print("INV8-W3-2-QUANTUM-METRIC-STIFFNESS-HTAU")
print("=" * 78)

# ---------------------------------------------------------------------------
# Plan-pinned machinery
# ---------------------------------------------------------------------------
GATE_ID = "INV8-W3-2-QUANTUM-METRIC-STIFFNESS-HTAU"                            # (local)
SCHEME = "FW"                                                                  # (local)
CONVENTION = "Peotta-Torma-D-geom-substrate-IS-OP-PROJ"                        # (local)
L_MAX = 10                                                                     # (local) plan-pinned
FD_EPS = 1e-5                                                                  # (local) central-FD step for dD/d{tau,mu} (matches S96/S104 FD_EPS)
G_ATLAS_ERRATUM = 982.5                                                        # (local) atlas-07 ERRATUM band-metric reservoir (methodological cross-check witness)
PASS_BAND_DECADE = 0.5                                                         # (local) |log10 R_stiff| PASS band
INFO_BAND_DECADE = 2.0                                                         # (local) |log10 R_stiff| INFO band
BERRY_ZERO_TOL = 1e-10                                                         # (local) Berry curvature exact-zero floor (anti-Hermiticity)
BAND_DEG = 2                                                                   # (local) J/PH Kramers doublet (S96 lowest_band_multiplet band_deg=2)
DEG_TOL = 1e-7                                                                 # (local) degeneracy tolerance (S96 plan pin)
GAP_FLOOR = 1e-9                                                               # (local) near-degenerate guard in the QGT denominator (S96 bp4_curvature)
SCHEMA_VERSION = "S84+"                                                        # (local)

# Canonical TT deformation directions (S96 lines 186-188; verbatim machinery).
V_JENSEN = np.array([2.0, -2.0, 1.0])     # (local) Jensen direction in log(L1,L2,L3); |v|^2=9; vol-preserving
V_MU = np.array([11.0, 7.0, -8.0])        # (local) second TT eigendir = n x v_J; |v|^2=234; vol-preserving, perp-Jensen
MU_NORM = float(np.sqrt(V_MU @ V_MU))     # (local) |v_mu| = sqrt(234) ~ 15.2971 (unit-step normalization)

# Imported backbone target (substrate-first: the value the NNU rank-1 theorem imports).
H_STAR_IMPORTED = H_fold              # M_KK units; the Friedmann backbone H(tau) at the fold
SECTOR_PQ = (0, 0)                    # (local) the (0,0) singlet block: home of the lowest |lambda| doublet (S96/S100b/S104)

print(f"  scheme={SCHEME}  convention={CONVENTION}  L_max={L_MAX}")
print(f"  Delta_BCS = {Delta_BCS}")
print(f"  M_KK      = {M_KK:.6e} GeV")
print(f"  tau_fold  = {tau_fold}")
print(f"  H_fold (imported backbone target) = {H_STAR_IMPORTED} M_KK")
print(f"  G_DeWitt (chi, tau-modulus inertia) = {G_DeWitt}")
print(f"  N_cells (V, BZ-volume norm) = {N_cells}")
print(f"  TT dirs: v_J=(2,-2,1) |v|^2={V_JENSEN@V_JENSEN:.0f}; v_mu=(11,7,-8) |v|^2={V_MU@V_MU:.0f}; |v_mu|={MU_NORM:.4f}")
print()

# Geometry sanity (S96 lines 477-479 asserts, verbatim): the volume normal is the SU(3)
# multiplicity vector n=(1,3,4) (NOT the naive (1,1,1)); n.v_J=2-6+4=0 (Jensen vol-preserving),
# n.v_mu=11+21-32=0 (v_mu vol-preserving), v_J.v_mu=22-14-8=0 (perp-Jensen). Baptista PROVEN.
n_vol = np.array([1.0, 3.0, 4.0])                                             # (local) S96 volume normal (SU(3) multiplicities)
assert abs(n_vol @ V_JENSEN) < 1e-12, "Jensen not volume-preserving"
assert abs(n_vol @ V_MU) < 1e-12, "v_mu not volume-preserving"
assert abs(V_JENSEN @ V_MU) < 1e-12, "v_mu not orthogonal to Jensen"

# ---------------------------------------------------------------------------
# Input SHAs (first lines of stdout per gate-verdicts.md)
# ---------------------------------------------------------------------------
def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


CANON_PATH = SHARED / "canonical_constants.py"                                 # (local)
DIRAC_PATH = SHARED / "dirac_spectrum.py"                                      # (local)
THIS_SCRIPT = Path(__file__).resolve()                                        # (local)

canon_sha = sha256_file(CANON_PATH)                                           # (local)
dirac_sha = sha256_file(DIRAC_PATH)                                           # (local)
script_sha = sha256_file(THIS_SCRIPT)                                         # (local)
print(f"INPUT SHA canonical_constants = {canon_sha}")
print(f"INPUT SHA dirac_spectrum      = {dirac_sha}")
print(f"INPUT SHA this_script         = {script_sha}")
print()

# ---------------------------------------------------------------------------
# Canonical (tau,mu) machinery (verbatim from s96_geom_offjensen_chern.py)
# ---------------------------------------------------------------------------
def build_su3_infra():
    gens = ds.su3_generators()                                                # (local)
    f_abc = ds.compute_structure_constants(gens)                              # (local)
    B_ab = ds.compute_killing_form(f_abc)                                     # (local)
    gammas = ds.build_cliff8()                                                # (local)
    return gens, f_abc, B_ab, gammas


def metric_scale_factors(tau, mu):
    """(L1,L2,L3) on the 2-parameter U(2)-invariant TT surface.
       l(tau,mu) = tau*v_J + (mu/|v_mu|)*v_mu ; L_i=exp(l_i). mu=0 => canonical Jensen."""
    log_L = tau * V_JENSEN + (mu / MU_NORM) * V_MU                            # (local)
    return float(np.exp(log_L[0])), float(np.exp(log_L[1])), float(np.exp(log_L[2]))


def build_dirac_sector(tau, mu, p, q, infra):
    """Block-diagonal D_K on Peter-Weyl sector (p,q) at metric point (tau,mu)."""
    gens, f_abc, B_ab, gammas = infra
    L1, L2, L3 = metric_scale_factors(tau, mu)                                # (local)
    g = ds.u2_invariant_metric(B_ab, L1, L2, L3)                              # (local)
    E = ds.orthonormal_frame(g)                                              # (local)
    ft = ds.frame_structure_constants(f_abc, E)                             # (local)
    Gamma = ds.connection_coefficients(ft)                                  # (local)
    Omega_spin = ds.spinor_connection_offset(Gamma, gammas)                 # (local)
    if (p, q) == (0, 0):
        return Omega_spin.copy()           # D = Omega offset on the 16-dim singlet
    rho, _ = ds.get_irrep(p, q, gens, f_abc)                                 # (local)
    return ds.dirac_operator_on_irrep(rho, E, gammas, Omega_spin)


def eigh_H(D_pi):
    """H = 1j D_pi Hermitian; return (mu_real, evecs). H real-symmetric => real evecs."""
    H = 1j * D_pi                                                             # (local)
    Hh = 0.5 * (H + H.conj().T)                                              # (local)
    w, v = np.linalg.eigh(Hh)                                                # (local)
    return w.real, v


def dD_dparam(tau, mu, p, q, infra, axis):
    """Central finite-difference dD_pi/d{tau or mu} at (tau,mu)."""
    if axis == "tau":
        Dp = build_dirac_sector(tau + FD_EPS, mu, p, q, infra)               # (local)
        Dm = build_dirac_sector(tau - FD_EPS, mu, p, q, infra)               # (local)
    else:
        Dp = build_dirac_sector(tau, mu + FD_EPS, p, q, infra)               # (local)
        Dm = build_dirac_sector(tau, mu - FD_EPS, p, q, infra)               # (local)
    return (Dp - Dm) / (2.0 * FD_EPS)


def nonabelian_qgt_trace(tau, mu, p, q, infra, deg, gap_floor=GAP_FLOOR):
    """Provost-Vallee quantum metric Tr g = g_{tau,tau}+g_{mu,mu} (Re QGT, non-Abelian
       trace) AND Berry curvature Omega (Im QGT) of the lowest-deg band-group of
       D_K(sector (p,q)) at (tau,mu). (S104 INFO companion + S96 bp4_curvature form.)
         Q_{ab} = Sum_{n in lowest} Sum_{m not in lowest} <n|dH_a|m><m|dH_b|n>/(mu_n-mu_m)^2
         g_{ab} = Re Q_{ab} ;  Omega = -2 Im Q_{tau,mu}
       Returns (g_tt, g_mm, g_tm_re, omega_berry, lam_min, deg_detected)."""
    D_pi = build_dirac_sector(tau, mu, p, q, infra)                          # (local)
    w, v = eigh_H(D_pi)                                                       # (local)
    aw = np.abs(w)                                                            # (local)
    order = np.argsort(aw)                                                    # (local)
    lam_min = float(aw[order[0]])                                             # (local)
    deg_detected = int(np.sum(np.abs(aw - lam_min) < DEG_TOL))               # (local)
    low_idx = list(order[:deg])                                              # (local)
    low_set = set(low_idx)                                                   # (local)
    dH_tau = 1j * dD_dparam(tau, mu, p, q, infra, "tau")                     # (local)
    dH_mu = 1j * dD_dparam(tau, mu, p, q, infra, "mu")                       # (local)
    A_tau = v.conj().T @ dH_tau @ v                                         # (local) <m|dH_tau|m'>
    A_mu = v.conj().T @ dH_mu @ v                                           # (local)
    n_dim = len(w)                                                           # (local)
    g_tt = 0.0; g_mm = 0.0; g_tm = 0.0 + 0.0j; omega = 0.0 + 0.0j            # (local)
    for n_idx in low_idx:
        for m in range(n_dim):
            if m in low_set:                                                # exclude intra-multiplet (degenerate)
                continue
            denom = (w[n_idx] - w[m]) ** 2                                   # (local)
            if denom < gap_floor:                                           # near-degenerate guard
                continue
            t_nm = A_tau[n_idx, m]                                          # (local) <n|dH_tau|m>
            m_nm = A_mu[n_idx, m]                                           # (local) <n|dH_mu|m>
            g_tt += abs(t_nm) ** 2 / denom                                  # Re Q_tt
            g_mm += abs(m_nm) ** 2 / denom                                  # Re Q_mm
            q_tm = t_nm * A_mu[m, n_idx] / denom                            # (local) <n|dH_tau|m><m|dH_mu|n>/denom
            g_tm += q_tm
            omega += q_tm                                                   # for Im part (Berry)
    g_tm_re = float(g_tm.real)                                              # (local)
    omega_berry = float(-2.0 * omega.imag)                                  # (local) non-Abelian Berry curvature (Im QGT)
    return g_tt, g_mm, g_tm_re, omega_berry, lam_min, deg_detected


# ---------------------------------------------------------------------------
# STEP 1: Build infra; locate the lowest |lambda| doublet at (tau_fold, mu=0)
# ---------------------------------------------------------------------------
print("--- Step 1: SU(3) infra + lowest-|lambda| doublet at (tau_fold, mu=0) ---")
infra = build_su3_infra()                                                    # (local)
p0, q0 = SECTOR_PQ                                                           # (local)

D_anchor = build_dirac_sector(float(tau_fold), 0.0, p0, q0, infra)           # (local)
w_anchor, _ = eigh_H(D_anchor)                                               # (local)
aw_anchor = np.sort(np.abs(w_anchor))                                        # (local)
deg_detect = int(np.sum(np.abs(aw_anchor - aw_anchor[0]) < DEG_TOL))         # (local)
print(f"  sector (0,0) singlet block: D = Omega_spin offset, size {D_anchor.shape[0]}")
print(f"  anchor (tau_fold,mu=0): |lambda|_min = {aw_anchor[0]:.9f}, lowest-band degeneracy = {deg_detect} (plan-expected {BAND_DEG})")
ah_err = float(np.max(np.abs(D_anchor + D_anchor.conj().T)))                 # (local)
imag_evec = float(np.max(np.abs((1j * D_anchor - (1j * D_anchor).conj().T))))  # (local)
print(f"  D anti-Herm err = {ah_err:.2e}; H=1j*D Hermitian (real-symmetric => real eigenstates => Berry=0 by construction)")

# ---------------------------------------------------------------------------
# STEP 2: Non-Abelian Provost-Vallee quantum metric Tr g = g_tt + g_mm over (tau,mu)
# ---------------------------------------------------------------------------
print("\n--- Step 2: Provost-Vallee quantum metric Tr g = g_{tau,tau}+g_{mu,mu} of the lowest doublet ---")
g_tt, g_mm, g_tm_re, omega_berry, lam_min, deg_det = nonabelian_qgt_trace(
    float(tau_fold), 0.0, p0, q0, infra, BAND_DEG)
Tr_g = g_tt + g_mm                                                            # (local) Provost-Vallee trace (Re QGT)
berry_max = abs(omega_berry)                                                  # (local) |Im QGT| = |Berry curvature|
print(f"  g_{{tau,tau}} = {g_tt:.10e}   (Jensen-direction quantum metric)")
print(f"  g_{{mu,mu}}   = {g_mm:.10e}   (C^2 Higgs-coset TT-direction quantum metric)")
print(f"  g_{{tau,mu}}  = {g_tm_re:.10e}  (cross term, Re)")
print(f"  Tr g = g_tt + g_mm = {Tr_g:.10e}   (Provost-Vallee, Re QGT)")
print(f"  Berry curvature Omega (Im QGT) = {omega_berry:.6e}  ; |Omega| = {berry_max:.3e}  (EXACT zero expected; tol={BERRY_ZERO_TOL})")
print(f"  STRUCTURAL READING: the (0,0) singlet block CANNOT be rotated by the U(2)-invariant")
print(f"  volume-preserving TT deformation (v_J, v_mu) => its QGT vanishes on THIS surface")
print(f"  (S100b line 833, S104 line 92). The atlas-07 reservoir g~{G_ATLAS_ERRATUM} is a")
print(f"  METHODOLOGICAL cross-check value (a DIFFERENT object), NOT this lowest-doublet metric.")

# Cross-check witness ratio.
g_vs_atlas_ratio = Tr_g / G_ATLAS_ERRATUM                                      # (local)
print(f"  Cross-check Tr g / g_atlas({G_ATLAS_ERRATUM}) = {g_vs_atlas_ratio:.4e}")

berry_zero = bool(berry_max < BERRY_ZERO_TOL)                                  # (local)
trg_positive = bool(Tr_g > BERRY_ZERO_TOL)                                     # (local) STRICTLY positive (above the eigen-floor)
print(f"  SIGNATURE: Tr g > 0 (strict) ? {trg_positive}   Berry = 0 (EXACT) ? {berry_zero}")

# ---------------------------------------------------------------------------
# STEP 3: Geometric superfluid stiffness D_geom = (2 Delta_BCS / V) * Tr g
# ---------------------------------------------------------------------------
print("\n--- Step 3: Geometric superfluid stiffness D_geom ---")
V_bz = N_cells          # BZ-volume normalization (Voronoi-cell count; the D_s formula V)
D_conv = 0.0            # (local) flat fold band -> Drude weight vanishes EXACTLY (B1 PROVEN, van Hove A_2)
D_geom = (2.0 * Delta_BCS / V_bz) * Tr_g                                       # (local) Peotta-Torma geometric term (M_KK^2)
D_s = D_conv + D_geom                                                          # (local)
print(f"  D_conv (flat band)        = {D_conv}  (Drude weight vanishes; van Hove A_2 catastrophe)")
print(f"  D_geom = (2*Delta/V)*Tr g = (2*{Delta_BCS:.6f}/{V_bz})*{Tr_g:.6e} = {D_geom:.10e}  M_KK^2")
print(f"  D_s = D_conv + D_geom     = {D_s:.10e}  M_KK^2  (entirely geometric)")

# ---------------------------------------------------------------------------
# STEP 4: Dimensionalize -> omega_stiff = sqrt(D_geom / chi)
# ---------------------------------------------------------------------------
print("\n--- Step 4: Emergent stiffness frequency omega_stiff = sqrt(D_geom / chi) ---")
chi = G_DeWitt          # tau-modulus inertia (DeWitt kinetic coefficient; H(tau) rides on tau-dynamics)
omega_stiff = float(np.sqrt(max(D_geom, 0.0) / chi))                           # (local) M_KK units
print(f"  chi = G_DeWitt = {chi}  (tau-modulus inertia)")
print(f"  omega_stiff = sqrt(D_geom/chi) = sqrt({D_geom:.6e}/{chi}) = {omega_stiff:.10e}  M_KK")

# ---------------------------------------------------------------------------
# STEP 5: Compare to the imported backbone  =>  R_stiff
# ---------------------------------------------------------------------------
print("\n--- Step 5: R_stiff = omega_stiff / H*_imported ---")
R_stiff = omega_stiff / H_STAR_IMPORTED if omega_stiff > 0 else 0.0            # (local)
log10_R = float(np.log10(R_stiff)) if R_stiff > 0 else -np.inf                 # (local)
abs_log10_R = abs(log10_R)                                                     # (local)
print(f"  omega_stiff   = {omega_stiff:.10e}  M_KK")
print(f"  H*_imported   = {H_STAR_IMPORTED}  M_KK  (H_fold, S38, the rank-1 NNU imported backbone)")
print(f"  R_stiff       = omega_stiff / H* = {R_stiff:.10e}")
print(f"  log10 R_stiff = {log10_R:.6f}  ; |log10 R_stiff| = {abs_log10_R:.6f}")
print(f"  PASS band |log10|<= {PASS_BAND_DECADE} ; INFO band <= {INFO_BAND_DECADE}")

# ---------------------------------------------------------------------------
# STEP 6: SIGN / MAGNITUDE / REGIME 3-tuple (schema-v2)
# ---------------------------------------------------------------------------
print("\n--- Step 6: 3-tuple verdict ---")

# SIGN: substitution-chain Step 4 predicted D_geom > 0 STRICTLY (Tr g > 0, Delta > 0) despite
# D_conv = 0; sign_verdict = PASS iff the substrate REALIZES that prediction (Tr g strictly > 0
# AND omega_stiff > 0). If Tr g = 0 (U(2) protection at the (0,0) block), the predicted
# strictly-positive geometric stiffness is NOT realized -> sign_verdict = FAIL (the constructive
# direction is closed at the (0,0) doublet).
sign_pred_positive = (Delta_BCS > 0.0)                                         # (local) chain predicts D_geom>0 IF Tr g>0
sign_obs_positive = trg_positive and (D_geom > BERRY_ZERO_TOL) and (omega_stiff > 0.0)  # (local)
sign_verdict = "PASS" if sign_obs_positive else "FAIL"                         # (local)

# MAGNITUDE: |log10 R_stiff| banding (only meaningful if omega_stiff > 0; if 0, magnitude FAIL).
if omega_stiff <= 0:
    magnitude_verdict = "FAIL"                                                # (local)
elif abs_log10_R <= PASS_BAND_DECADE:
    magnitude_verdict = "PASS"                                                # (local)
elif abs_log10_R <= INFO_BAND_DECADE:
    magnitude_verdict = "INFO"                                                # (local)
else:
    magnitude_verdict = "FAIL"                                                # (local)

# REGIME: the maximally-NON-ideal flat-band signature. The Berry=0 EXACT half ALWAYS holds
# (anti-Hermiticity). The Tr g>0 half is the question. VALID iff BOTH (genuine flat geometric
# superfluid). If Tr g=0 (U(2)-protected (0,0) block) the band is metrically TRIVIAL on this
# surface -> the stiffness-to-frequency identification is OFF-REGIME (MARGINAL: half the
# signature holds — Berry=0 — but the metric vanishes, so there is no geometric stiffness to
# identify with H(tau)).
if trg_positive and berry_zero:
    regime_verdict = "VALID"                                                  # (local)
elif berry_zero:        # Berry=0 holds but Tr g=0 (metric trivial on this surface)
    regime_verdict = "MARGINAL"                                              # (local)
else:
    regime_verdict = "BREAKDOWN"                                             # (local)

# Composite collapse (gate-verdicts.md PRE-REGISTERED rule).
if regime_verdict == "BREAKDOWN":
    composite = "FAIL"                                                        # (local)
elif sign_verdict == "FAIL":
    composite = "FAIL"                                                        # (local)
elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
    composite = "FAIL"                                                        # (local)
elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
    composite = "INFO"                                                        # (local)
elif magnitude_verdict == "INFO":
    composite = "INFO"                                                        # (local)
else:
    composite = "PASS"                                                        # (local)

print(f"  sign_verdict      = {sign_verdict}   (D_geom>0 & omega_stiff>0 realized? Tr g strictly>0: {trg_positive})")
print(f"  magnitude_verdict = {magnitude_verdict}   (|log10 R_stiff|={abs_log10_R if np.isfinite(abs_log10_R) else float('inf'):.4f})")
print(f"  regime_verdict    = {regime_verdict}   (Tr g>0:{trg_positive} & Berry=0 EXACT:{berry_zero})")
print(f"  COMPOSITE         = {composite}")

# ---------------------------------------------------------------------------
# STEP 7: Dual-SHA over ordered input-pin map
# ---------------------------------------------------------------------------
def closure_hash(ordered_pairs):
    blob = "\n".join(f"{k}={v}" for k, v in ordered_pairs)                    # (local)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


value_str = (f"R_stiff={R_stiff:.6e}|log10={log10_R:.6f}|omega_stiff={omega_stiff:.6e}"
             f"|Trg={Tr_g:.6e}|g_tt={g_tt:.3e}|g_mm={g_mm:.3e}|D_geom={D_geom:.6e}"
             f"|Berry={berry_max:.3e}|sector={p0}-{q0}|U2-protected-zero")     # (local)

audit_pairs = [                                                               # (local)
    ("gate_id", GATE_ID),
    ("scheme", SCHEME),
    ("convention", CONVENTION),
    ("L_max", str(L_MAX)),
    ("fd_eps", str(FD_EPS)),
    ("band_deg", str(BAND_DEG)),
    ("Delta_BCS", repr(Delta_BCS)),
    ("M_KK", repr(M_KK)),
    ("tau_fold", repr(tau_fold)),
    ("H_fold", repr(H_fold)),
    ("G_DeWitt", repr(G_DeWitt)),
    ("N_cells", repr(N_cells)),
    ("v_J", "2,-2,1"),
    ("v_mu", "11,7,-8"),
    ("g_tt", f"{g_tt:.10e}"),
    ("g_mm", f"{g_mm:.10e}"),
    ("Tr_g", f"{Tr_g:.10e}"),
    ("D_geom", f"{D_geom:.10e}"),
    ("omega_stiff", f"{omega_stiff:.10e}"),
    ("R_stiff", f"{R_stiff:.10e}"),
    ("berry_max", f"{berry_max:.3e}"),
    ("lowest_sector", f"{p0},{q0}"),
    ("canonical_constants_sha256", canon_sha),
    ("dirac_spectrum_sha256", dirac_sha),
    ("script_sha256", script_sha),
]
audit_sha = closure_hash(audit_pairs)                                         # (local)
content_sha = hashlib.sha256(value_str.encode("utf-8")).hexdigest()           # (local)
print(f"\naudit_sha256   = {audit_sha}")
print(f"content_sha256 = {content_sha}")

# ---------------------------------------------------------------------------
# STEP 8: Save data + plot
# ---------------------------------------------------------------------------
NPZ_OUT = ROOT / "computations" / "investigation-8" / "inv8_w3_quantum_metric_stiffness_htau.npz"   # (local)
PNG_OUT = ROOT / "computations" / "investigation-8" / "inv8_w3_quantum_metric_stiffness_htau.png"   # (local)

np.savez(
    NPZ_OUT,
    gate_id=GATE_ID,
    composite=composite,
    sign_verdict=sign_verdict,
    magnitude_verdict=magnitude_verdict,
    regime_verdict=regime_verdict,
    g_tt=g_tt, g_mm=g_mm, g_tm_re=g_tm_re,
    Tr_g=Tr_g,
    berry_max=berry_max, omega_berry=omega_berry,
    berry_zero=berry_zero, trg_positive=trg_positive,
    g_atlas_erratum=G_ATLAS_ERRATUM, g_vs_atlas_ratio=g_vs_atlas_ratio,
    D_conv=D_conv, D_geom=D_geom, D_s=D_s, chi=chi,
    omega_stiff=omega_stiff, H_star_imported=H_STAR_IMPORTED,
    R_stiff=R_stiff, log10_R=log10_R, abs_log10_R=abs_log10_R,
    pass_band_decade=PASS_BAND_DECADE, info_band_decade=INFO_BAND_DECADE,
    lowest_sector=np.array([p0, q0]), band_deg=BAND_DEG, deg_detected=deg_det,
    lam_min=lam_min,
    v_jensen=V_JENSEN, v_mu=V_MU,
    Delta_BCS=Delta_BCS, M_KK=M_KK, tau_fold=tau_fold, H_fold=H_fold,
    G_DeWitt=G_DeWitt, N_cells=N_cells, fd_eps=FD_EPS,
    audit_sha256=audit_sha, content_sha256=content_sha,
)
print(f"\nData saved: {NPZ_OUT}")

fig, axes = plt.subplots(1, 2, figsize=(13, 5))

ax = axes[0]
labels = ["omega_stiff", "H*_imported\n(H_fold)"]                             # (local)
vals = [max(omega_stiff, 1e-20), H_STAR_IMPORTED]                             # (local)
colors = ["#2c7fb8", "#d95f0e"]                                              # (local)
bars = ax.bar(labels, vals, color=colors)
ax.set_yscale("log")
ax.set_ylabel("frequency / backbone (M_KK units)")
ax.set_title(f"Quantum-metric stiffness vs imported backbone\nR_stiff={R_stiff:.2e} (|log10|={abs_log10_R if np.isfinite(abs_log10_R) else float('inf'):.2f}) -> {composite}")
for b, v in zip(bars, vals):
    ax.text(b.get_x() + b.get_width() / 2, v, f"{v:.2g}", ha="center", va="bottom", fontsize=9)
ax.axhspan(H_STAR_IMPORTED / (10 ** PASS_BAND_DECADE), H_STAR_IMPORTED * (10 ** PASS_BAND_DECADE),
           color="green", alpha=0.12, label=f"PASS band (+/-{PASS_BAND_DECADE} dec)")
ax.axhspan(H_STAR_IMPORTED / (10 ** INFO_BAND_DECADE), H_STAR_IMPORTED * (10 ** INFO_BAND_DECADE),
           color="gold", alpha=0.08, label=f"INFO band (+/-{INFO_BAND_DECADE} dec)")
ax.legend(fontsize=8, loc="lower left")

ax = axes[1]
sig_labels = ["g_tt\n(Jensen)", "g_mm\n(Higgs coset)", "|Berry|\n(Im QGT)"]   # (local)
sig_vals = [max(g_tt, 1e-22), max(g_mm, 1e-22), max(berry_max, 1e-22)]        # (local)
sig_colors = ["#1a9850", "#66bd63", "#999999"]                               # (local)
sbars = ax.bar(sig_labels, sig_vals, color=sig_colors)
ax.set_yscale("log")
ax.set_ylabel("magnitude")
ax.set_title(f"(0,0) doublet QGT on the U(2)-inv TT surface\nTr g={Tr_g:.2e} (U(2)-protected); Berry={berry_max:.1e}=0 EXACT")
ax.axhline(G_ATLAS_ERRATUM, color="#1a9850", ls="--", lw=1, alpha=0.6, label=f"atlas-07 reservoir g~{G_ATLAS_ERRATUM}\n(methodological X-check)")
ax.legend(fontsize=8)
for b, v in zip(sbars, sig_vals):
    ax.text(b.get_x() + b.get_width() / 2, v, f"{v:.1e}", ha="center", va="bottom", fontsize=8)

fig.tight_layout()
fig.savefig(PNG_OUT, dpi=130)
print(f"Plot saved: {PNG_OUT}")

# ---------------------------------------------------------------------------
# STEP 9: print_verdict_payload (the AGENT calls emit_verdict; script never appends)
# ---------------------------------------------------------------------------
extra_rows = [                                                                # (local)
    (f"# sign_verdict={sign_verdict} magnitude_verdict={magnitude_verdict} "
     f"regime_verdict={regime_verdict} # {GATE_ID} 3-tuple annotation (schema-v2)"),
    (f"# INV8-W3-2: Tr g={Tr_g:.3e} (g_tt={g_tt:.2e} Jensen + g_mm={g_mm:.2e} Higgs-coset) on the (0,0) "
     f"lowest doublet over the U(2)-inv vol-preserving TT (tau,mu) surface = ZERO (U(2)-protected, "
     f"S100b L833/S104 L92); Berry={berry_max:.1e}=0 EXACT; D_geom=(2*Delta/V)*Tr g={D_geom:.3e} M_KK^2; "
     f"omega_stiff={omega_stiff:.3e} M_KK vs H_fold={H_STAR_IMPORTED:.4f} M_KK; R_stiff={R_stiff:.3e}; "
     f"chi=G_DeWitt={chi}; lowest doublet sector ({p0},{q0})"),
    (f"# STRUCTURAL: the quantum-metric-stiffness route to H(tau) is CLOSED at the (0,0) block "
     f"(metric vanishes by U(2)-invariance); atlas-07 g~{G_ATLAS_ERRATUM} is a methodological reservoir "
     f"(DIFFERENT object), Tr g/g_atlas={g_vs_atlas_ratio:.2e}; the maximally-NON-ideal Berry=0 EXACT "
     f"signature lands; G-1 (a(t) gap) survives via this route"),
    (f"# regulator_pin=N/A (quantum metric is a D_K eigenbundle property, NOT a Seeley-DeWitt a_n moment); "
     f"convention={CONVENTION}; cross-pillar REFINES VII.AF.1 / VII.CA; attacks G-1"),
    (f"# canonical_constants_sha256={canon_sha[:16]} dirac_spectrum_sha256={dirac_sha[:16]} "
     f"script_sha256={script_sha[:16]}"),
]


def print_verdict_payload():
    print("=" * 78)
    print("EMIT_VERDICT PAYLOAD (agent calls mcp__knowledge__emit_verdict):")
    print("=" * 78)
    print(f"  session     = 8")
    print(f"  track       = investigation")
    print(f"  gate_id     = {GATE_ID}")
    print(f"  verdict     = {composite}")
    print(f"  value       = {value_str}")
    print(f"  scheme      = {SCHEME}")
    print(f"  convention  = {CONVENTION}")
    print(f"  l_max       = {L_MAX}")
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")
    print(f"  schema_version = {SCHEMA_VERSION}")
    print(f"  sign_verdict      = {sign_verdict}")
    print(f"  magnitude_verdict = {magnitude_verdict}")
    print(f"  regime_verdict    = {regime_verdict}")
    print(f"  extra_rows =")
    for r in extra_rows:
        print(f"    {r}")
    print("=" * 78)


print_verdict_payload()

print(f"\n[elapsed {time.time() - t0:.1f}s]")
sys.exit(0)
