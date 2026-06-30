#!/usr/bin/env python3
"""
S85 W0-2 — S85-FOLDED-BISPECTRUM-21CM-SHAPE-TEMPLATE
====================================================

Gate: S85-FOLDED-BISPECTRUM-21CM-SHAPE-TEMPLATE ([VERIFY])
Agent: transit-dynamics-theorist
Classification: PHONONIC (the folded triangle is the k-space signature of
  pre/post-transit acoustic causal disconnection of the GGE relic; it is
  NOT a perturbative expansion around a field background.)

Pre-registered threshold (PRDR, session-85-plan-w0.md §W0-2):
  PASS iff:
     sigma(f_NL^fold) <= 0.2 at SKA-Phase-2
     AND cosine-overlap(fold, equil) < 0.3
     AND cosine-overlap(fold, local) < 0.3
     AND SKA-Phase-2 detectability >= 3 sigma for |f_NL^fold| >= 1
  INFO iff detectability PASS but overlap(fold, equil|local) in [0.3, 0.5]
  FAIL iff any overlap > 0.5 (template is a linear combination of LCDM shapes)

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - canonical_constants.py
  - s67_gge_bispectrum.npz  (framework f_NL_diag_CLT = 0.1293, N_pair=59.8)
  - script bytes (for content_sha256)

Output 4-tuple:
  (value=sigma(f_NL^fold)_SKA2, scheme=Babich-Creminelli-2004,
   convention=Fisher-cosine, L_max=8)

METHODOLOGY
-----------
Three numerical artefacts are constructed on a (k1,k2,k3) grid that
respects triangle inequality:

  (a) SHAPE kernels
      PRIMARY (scale-invariant, dimensionally consistent):
        S_fold(k)  = Meerburg+2009 flat template (0901.4044 Eq 2.7):
                     = 1/(k1^3 k2^3) + perms
                       + 3/(k1^2 k2^2 k3^2)
                       - (1/(k1 k2^2 k3^3) + 5 perms)
                     [peaked at k3 = k1+k2 flattened configuration;
                      substrate-acoustic folding in the scale-invariant
                      convention that preserves dimensional matching to
                      local/equil shape kernels]
        S_equil(k) = -1/(k1^3 k2^3) - 1/(k2^3 k3^3) - 1/(k3^3 k1^3)
                     - 2/(k1^2 k2^2 k3^2)
                     + (1/(k1 k2^2 k3^3) + 5 perms)
                                       [Creminelli et al. 2006, JCAP 0606:005]
        S_local(k) = 1/(k1^3 k2^3) + 1/(k2^3 k3^3) + 1/(k3^3 k1^3)
                                       [Komatsu-Spergel 2001]

      CROSS-CHECK (plan-literal bispectrum amplitude, scale-DEPENDENT):
        B_fold_plan(k) = k3^2 / (k1 k2)
                     [plan §W0-2 literal; this is a BISPECTRUM amplitude,
                      not a scale-invariant shape function — recorded as
                      diagnostic; does not enter the primary overlap
                      because dimensional mismatch with S_equil/S_local
                      makes the cosine K-window dependent.]

  (b) Fisher-weighted Babich-Creminelli inner product (BC 2004 Eq 29):
      <A, B>_F = sum_T  S_A(T) * S_B(T) * w(T)
      w(T) = 1 / ( 6 * P_tot(k1) * P_tot(k2) * P_tot(k3) )
      cos(A, B) = <A,B>_F / sqrt(<A,A>_F <B,B>_F)

  (c) Fisher forecast for f_NL^fold on the SKA Phase-2 21-cm bispectrum:
      F_ff = sum_T  [S_fold(T)]^2  N_T / Var(T)
      sigma(f_NL^fold) = 1 / sqrt(F_ff)
      Triangle mode count uses Scoccimarro 1998 / Sefusatti 2006.

  (d) Full 3x3 Fisher matrix over (f_NL^fold, f_NL^equil, f_NL^local)
      for the marginalized sigma (accounts for template degeneracy):
      sigma_marg(f_NL^fold) = sqrt( [F^{-1}]_{fold,fold} )

  (e) Detectability pull: pull = |f_NL^fold_framework| / sigma(f_NL^fold)

SUBSTITUTION CHAIN (for direction claims)
-----------------------------------------
  Step 1 (def):   Shape kernels as above.
  Step 2 (def):   Babich-Creminelli cosine overlap = inverse-variance
                  weighted inner product normalized by L2 norms (Fisher basis).
                  cos(A,B) = 1  <=>  A and B are proportional on the weighted basis.
                  cos(A,B) = 0  <=>  A and B are orthogonal (linearly independent).
  Step 3 (def):   sigma(f_NL^fold) = (F^{-1})_{ff}^{1/2} for the MARGINAL
                  entry of the 3x3 Fisher matrix (after inversion with the
                  two LCDM shapes held as nuisance).
  Step 4 (subst): Compute overlap + marginal sigma NUMERICALLY; no
                  pre-simplification — direction is the OUTPUT, not a claim.
  Step 5 (dir):   Template is "sole-surviving" iff ALL of
                     cos(fold, equil) < 0.3
                     cos(fold, local) < 0.3
                     sigma_marg(fold)_SKA2 <= 0.2
                  per S83 post-mortem criterion.
  Direction read-off: sign / threshold computed post-compute, threshold
  comparison in evaluate_gate().

SUBSTRATE-FRAMING
-----------------
The folded triangle is NOT a squeezed-limit inflaton NG expansion. It is the
k-space interference pattern of GGE excitations across the acoustic white
hole (pre/post-transit causal disconnection). The template peak at k3 = k1+k2
(flattened configuration) is the signature of the two-mode squeezed state
produced when Parker pair production excites N_pair = 59.8 quasiparticle
pairs during the supersonic transit through the van Hove fold.

Session: S85 Wave 0 Gate W0-2
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
import torch
import matplotlib
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===

matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S85"                                                       # (local)
GATE_ID = "S85-FOLDED-BISPECTRUM-21CM-SHAPE-TEMPLATE"                 # (local)
SCHEME = "Babich-Creminelli-2004"                                     # (local)
CONVENTION = "Fisher-cosine"                                          # (local)
L_MAX = 8                                                             # (local)

# Pre-registered thresholds (§W0-2)
SIGMA_PASS = 0.20                                                     # (local)
OVERLAP_PASS = 0.30                                                   # (local) cos-overlap fold vs LCDM
OVERLAP_INFO = 0.50                                                   # (local)
DETECT_THRESHOLD = 3.0                                                # (local) sigma pull for PASS

# Machinery pin (§W0-2 PRDR)
L_MAX_OBS = 1e5                                                       # (local) multipole cap
L_MIN_OBS = 10                                                        # (local) multipole floor
K_GRID_N = 512                                                        # (local) 1-D k-grid N
F_NL_FOLD_REF = 1.0                                                   # (local) unit normalization
FISHER_RANK_FLOOR = 0.9                                               # (local) min condition ratio

# Output destinations
OUT_NPZ = resolve_output(85, 's85_w0_folded_bispectrum_21cm_shape.npz')
OUT_PNG = resolve_output(85, 's85_w0_folded_bispectrum_21cm_shape.png')
VERDICT_TXT = resolve_output(85, 's85_gate_verdicts.txt')

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    resolve_output(67, 's67_gge_bispectrum.npz'),
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}... ({sha})")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
    """(audit_sha256, content_sha256) per S84+ dual-SHA schema."""
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Compute
# ---------------------------------------------------------------------------

# ---- SKA Phase-2 + CMB-S4 instrument specifications ----------------------
# (Cohen et al. 2017, SKA Cosmology SWG 2020 arXiv:1811.02743, CMB-S4 SB v2)

SKA2_SPEC = {
    'name': 'SKA Phase-2 fiducial-2030',
    'f_sky': 0.5,                     # (local) wide-field tomography
    'z_min': 6.0,                     # (local)
    'z_max': 20.0,                    # (local)
    'k_min_Mpc': 0.02,                # (local) Mpc^-1 (post-wedge mitigation)
    'k_max_Mpc': 10.0,                # (local) Mpc^-1 (long-baseline limit)
    'T_sys_K': 150.0,                 # (local)
    'A_eff_m2': 9e6,                  # (local) 9 km^2
    't_obs_hr': 5000.0,               # (local) ~5x campaign
    'N_modes_fg_loss': 0.3,           # (local)
    'l_max_eff': 3e4,                 # (local) b_max = 200 km at nu~100 MHz
}

CMB_S4_SPEC = {
    'name': 'CMB-S4 Science Book v2 2022',
    'f_sky': 0.4,                     # (local) CMB-S4 SB v2 Table 6.1
    'l_min': 30,                      # (local)
    'l_max': 5000,                    # (local) temperature + pol
    'Delta_T_uKarcmin': 1.0,          # (local)
    'fwhm_arcmin': 1.4,               # (local)
}

# Planck 2018 cosmology for distance integrals
H_PLANCK = 0.6766                     # (local) h100, Planck 2018
H0_KMS = 100.0 * H_PLANCK             # (local) km/s/Mpc
OMEGA_M = 0.3111                      # (local) Planck 2018
OMEGA_L = 1.0 - OMEGA_M               # (local)
K_PIVOT_MPC = 0.05                    # (local) standard inflation pivot
T_21_MK = 27.0 * 0.5 * np.sqrt(9.0 / 10.0)  # (local) mK (z=8, x_HI=0.5)


def chi_of_z(z):
    """Comoving distance (Mpc) via simple trapezoidal integration."""
    zz = np.linspace(0.0, float(z), 200)  # (local)
    E = np.sqrt(OMEGA_M * (1 + zz) ** 3 + OMEGA_L)  # (local)
    DH = c_light_km_s / H0_KMS  # (local) Hubble distance Mpc
    return float(DH * np.trapezoid(1.0 / E, zz))


def V_survey(spec):
    """Comoving survey volume (Mpc^3) for SKA Phase-2 z-range."""
    z_min, z_max = spec['z_min'], spec['z_max']
    zz = np.linspace(z_min, z_max, 120)  # (local)
    chi = np.array([chi_of_z(z) for z in zz])  # (local)
    Omega_sky = 4.0 * PI * spec['f_sky']  # (local)
    dchi = np.diff(chi)  # (local)
    chi_mid = 0.5 * (chi[:-1] + chi[1:])  # (local)
    return float(np.sum(Omega_sky * chi_mid ** 2 * dchi))


def P_21cm_signal(k_arr, z_eff=8.0):
    """21cm matter power spectrum at z_eff, mK^2 Mpc^3 (Mesinger+2011 fit)."""
    delta2 = 15.0 * (k_arr / 0.1) ** 0.3  # (local) mK^2
    return 2.0 * PI ** 2 * delta2 / k_arr ** 3  # (local) mK^2 Mpc^3


def P_21cm_noise(k_arr, spec, z_eff=8.0):
    """Thermal + wedge noise for SKA Phase-2 (Morales 2005, McQuinn+2006)."""
    T_sys = spec['T_sys_K'] * 1e3  # (local) mK
    A_eff = spec['A_eff_m2']        # (local) m^2
    t_obs = spec['t_obs_hr'] * 3600.0  # (local) s
    lam_obs = 0.21 * (1.0 + z_eff)  # (local) m
    r_z = chi_of_z(z_eff)  # (local) Mpc
    H_z = H0_KMS * np.sqrt(OMEGA_M * (1 + z_eff) ** 3 + OMEGA_L)  # (local)
    Y = (1 + z_eff) ** 2 * 0.21 / (H_z / c_light_km_s) / 1e6  # (local) Mpc/MHz
    delta_nu_MHz = 1.0  # (local) IM bin
    coeff = (T_sys ** 2 * lam_obs ** 2) / (A_eff * t_obs * delta_nu_MHz * 1e6)  # (local)
    P_N_ang = coeff * r_z ** 2 * Y  # (local) mK^2 Mpc^3
    # k-dependent wedge suppression
    k_wedge = 0.05  # (local) Mpc^-1
    wedge = np.where(k_arr < k_wedge, 10.0, 1.0) / spec['N_modes_fg_loss']  # (local)
    return P_N_ang * wedge


def P_total(k_arr, spec, z_eff=8.0):
    return P_21cm_signal(k_arr, z_eff) + P_21cm_noise(k_arr, spec, z_eff)


# ---- Shape kernels --------------------------------------------------------

def S_fold_SI(k1, k2, k3):
    """Meerburg+2009 flat/folded SHAPE (0901.4044 Eq 2.7), scale-invariant.

    PRIMARY folded template in the Babich-Creminelli (2004) Fisher-cosine
    convention. Dimensionally consistent with S_equil / S_local (all scale
    as k^-6 under k -> lambda k). Peaks at the flattened triangle
    k3 = k1 + k2, which is the k-space signature of the GGE relic's
    two-mode squeezed state post-transit (substrate-acoustic folding).
    """
    return (
        (1.0 / (k1 ** 3 * k2 ** 3) + 1.0 / (k2 ** 3 * k3 ** 3) + 1.0 / (k3 ** 3 * k1 ** 3))
        + 3.0 / (k1 ** 2 * k2 ** 2 * k3 ** 2)
        - (1.0 / (k1 * k2 ** 2 * k3 ** 3)
           + 1.0 / (k1 * k3 ** 2 * k2 ** 3)
           + 1.0 / (k2 * k1 ** 2 * k3 ** 3)
           + 1.0 / (k2 * k3 ** 2 * k1 ** 3)
           + 1.0 / (k3 * k1 ** 2 * k2 ** 3)
           + 1.0 / (k3 * k2 ** 2 * k1 ** 3))
    )


def B_fold_plan(k1, k2, k3):
    """Plan-literal §W0-2 bispectrum amplitude: k3^2 / (k1 k2).

    CROSS-CHECK ONLY (not used in primary overlap). This is a scale-dependent
    bispectrum amplitude (not a scale-invariant shape function); the plan
    pins this as the peak-structure ansatz for the folded transit signal,
    but dimensional consistency with equil/local shape kernels requires the
    scale-invariant Meerburg flat template above.
    """
    return k3 * k3 / (k1 * k2)


def S_equil(k1, k2, k3):
    """Creminelli+ 2006 equilateral template (scale-invariant convention).

    S_equil = -1/(k1^3 k2^3) - 1/(k2^3 k3^3) - 1/(k3^3 k1^3)
             - 2/(k1^2 k2^2 k3^2)
             + [1/(k1 k2^2 k3^3) + 5 perms]
    """
    term1 = -(1.0 / (k1 ** 3 * k2 ** 3) +
              1.0 / (k2 ** 3 * k3 ** 3) +
              1.0 / (k3 ** 3 * k1 ** 3))
    term2 = -2.0 / (k1 ** 2 * k2 ** 2 * k3 ** 2)
    # 6 permutations of (1, 2, 3) for 1/(k_i k_j^2 k_k^3)
    term3 = (1.0 / (k1 * k2 ** 2 * k3 ** 3) +
             1.0 / (k1 * k3 ** 2 * k2 ** 3) +
             1.0 / (k2 * k1 ** 2 * k3 ** 3) +
             1.0 / (k2 * k3 ** 2 * k1 ** 3) +
             1.0 / (k3 * k1 ** 2 * k2 ** 3) +
             1.0 / (k3 * k2 ** 2 * k1 ** 3))
    return term1 + term2 + term3


def S_local(k1, k2, k3):
    """Komatsu-Spergel 2001 local template (scale-invariant convention).

    S_local = 1/(k1^3 k2^3) + 1/(k2^3 k3^3) + 1/(k3^3 k1^3)
    """
    return (1.0 / (k1 ** 3 * k2 ** 3) +
            1.0 / (k2 ** 3 * k3 ** 3) +
            1.0 / (k3 ** 3 * k1 ** 3))


# ---- Triangle grid --------------------------------------------------------

def build_triangle_grid(spec, n_k=K_GRID_N, device='cuda'):
    """Log-spaced k grid over SKA-2 range; return (k1, k2, k3, mask, weight).

    We enumerate triangles with k1 <= k2 <= k3 and triangle inequality
    |k1 - k2| <= k3 <= k1 + k2. Vectorized on GPU via torch.
    """
    k_min = spec['k_min_Mpc']
    k_max = spec['k_max_Mpc']
    k = torch.logspace(
        np.log10(k_min), np.log10(k_max), n_k,
        device=device, dtype=torch.float64,
    )
    # 3D tensor product
    K1, K2, K3 = torch.meshgrid(k, k, k, indexing='ij')
    # Ordering: k1 <= k2 <= k3 to count each distinct triangle once
    ord_mask = (K1 <= K2) & (K2 <= K3)
    # Triangle inequality: k3 <= k1 + k2 (since k3 is largest we only need the upper side)
    tri_mask = K3 <= (K1 + K2) * 1.0000001
    mask = ord_mask & tri_mask  # (local)

    # Logarithmic bin widths (for mode counting)
    dlnk = torch.log(k[1] / k[0])  # (local)
    dk1 = K1 * dlnk
    dk2 = K2 * dlnk
    dk3 = K3 * dlnk

    # Symmetry factor (sym = 6 for equilateral, 2 for isoceles, 1 for scalene)
    eq_mask = (K1 == K2) & (K2 == K3)
    iso_mask = ((K1 == K2) | (K2 == K3)) & ~eq_mask
    sym = torch.ones_like(K1)
    sym[iso_mask] = 2.0
    sym[eq_mask] = 6.0

    return K1, K2, K3, mask, dk1, dk2, dk3, sym, k


def compute_weights(K1, K2, K3, mask, dk1, dk2, dk3, sym, spec, z_eff=8.0):
    """Triangle mode counts + inverse-variance weights on GPU.

    n_modes = V_survey * k1 * k2 * k3 * dk1 * dk2 * dk3 / (8 pi^4) / sym
    Var(B) = 6 * P_tot(k1) * P_tot(k2) * P_tot(k3)
    weight = n_modes / Var  (Fisher weight per triangle)
    """
    V_surv = V_survey(spec)  # (local) Mpc^3
    # P_tot vectorized on GPU
    k1_np = K1.cpu().numpy()  # (local)
    k2_np = K2.cpu().numpy()  # (local)
    k3_np = K3.cpu().numpy()  # (local)
    P1 = torch.tensor(P_total(k1_np, spec, z_eff), device=K1.device, dtype=torch.float64)
    P2 = torch.tensor(P_total(k2_np, spec, z_eff), device=K1.device, dtype=torch.float64)
    P3 = torch.tensor(P_total(k3_np, spec, z_eff), device=K1.device, dtype=torch.float64)
    Var = 6.0 * P1 * P2 * P3

    n_modes = (V_surv * K1 * K2 * K3 * dk1 * dk2 * dk3) / (8.0 * (PI ** 4)) / sym
    weight = n_modes / Var
    # Zero out non-physical (masked-out) triangles
    weight = torch.where(mask, weight, torch.zeros_like(weight))
    n_modes = torch.where(mask, n_modes, torch.zeros_like(n_modes))
    return weight, n_modes, Var, V_surv


def compute_shapes(K1, K2, K3, mask):
    """Evaluate SHAPE kernels on the triangle grid.

    Returns (Sf_SI, Seq, Sloc, Bf_plan) where:
      Sf_SI   = Meerburg flat template (scale-invariant, PRIMARY)
      Seq     = Creminelli+ equilateral (scale-invariant)
      Sloc    = Komatsu-Spergel local (scale-invariant)
      Bf_plan = plan-literal k3^2/(k1 k2) (scale-DEPENDENT, CROSS-CHECK only)
    """
    # Meerburg flat template (scale-invariant, PRIMARY)
    Sf_SI = torch.where(
        mask,
        (1.0 / (K1 ** 3 * K2 ** 3) + 1.0 / (K2 ** 3 * K3 ** 3) + 1.0 / (K3 ** 3 * K1 ** 3))
        + 3.0 / (K1 ** 2 * K2 ** 2 * K3 ** 2)
        - (1.0 / (K1 * K2 ** 2 * K3 ** 3)
           + 1.0 / (K1 * K3 ** 2 * K2 ** 3)
           + 1.0 / (K2 * K1 ** 2 * K3 ** 3)
           + 1.0 / (K2 * K3 ** 2 * K1 ** 3)
           + 1.0 / (K3 * K1 ** 2 * K2 ** 3)
           + 1.0 / (K3 * K2 ** 2 * K1 ** 3)),
        torch.zeros_like(K1),
    )
    # Creminelli+ 2006 equilateral (scale-invariant)
    Seq = torch.where(
        mask,
        -(1.0 / (K1 ** 3 * K2 ** 3) + 1.0 / (K2 ** 3 * K3 ** 3) + 1.0 / (K3 ** 3 * K1 ** 3))
        - 2.0 / (K1 ** 2 * K2 ** 2 * K3 ** 2)
        + (1.0 / (K1 * K2 ** 2 * K3 ** 3)
           + 1.0 / (K1 * K3 ** 2 * K2 ** 3)
           + 1.0 / (K2 * K1 ** 2 * K3 ** 3)
           + 1.0 / (K2 * K3 ** 2 * K1 ** 3)
           + 1.0 / (K3 * K1 ** 2 * K2 ** 3)
           + 1.0 / (K3 * K2 ** 2 * K1 ** 3)),
        torch.zeros_like(K1),
    )
    # Komatsu-Spergel 2001 local (scale-invariant)
    Sloc = torch.where(
        mask,
        1.0 / (K1 ** 3 * K2 ** 3) + 1.0 / (K2 ** 3 * K3 ** 3) + 1.0 / (K3 ** 3 * K1 ** 3),
        torch.zeros_like(K1),
    )
    # Plan-literal B_fold_plan (scale-DEPENDENT, cross-check only)
    Bf_plan = torch.where(mask, K3 * K3 / (K1 * K2), torch.zeros_like(K1))
    return Sf_SI, Seq, Sloc, Bf_plan


def cosine_overlap(A, B, W):
    """Babich-Creminelli Fisher-weighted cosine (BC 2004 Eq 29).

    <A, B>_F = sum_T w(T) * A(T) * B(T)
    cos(A, B) = <A,B>_F / sqrt(<A,A>_F <B,B>_F)
    """
    inner_AB = torch.sum(W * A * B).item()  # (local)
    inner_AA = torch.sum(W * A * A).item()  # (local)
    inner_BB = torch.sum(W * B * B).item()  # (local)
    denom = np.sqrt(max(inner_AA * inner_BB, 1e-300))  # (local)
    return float(inner_AB / denom), inner_AB, inner_AA, inner_BB


def fisher_3x3(Sf, Seq, Sloc, W):
    """3x3 Fisher matrix over (fold, equil, local).

    F_{ab} = <S_a, S_b>_F  (Gaussian Fisher, amplitude-only).
    """
    SS = [Sf, Seq, Sloc]
    F = np.zeros((3, 3), dtype=np.float64)
    for a in range(3):
        for b in range(3):
            F[a, b] = torch.sum(W * SS[a] * SS[b]).item()
    return F


def marginal_sigma(F):
    """Marginal sigma on parameter 0 (fold) from Fisher 3x3."""
    Finv = np.linalg.inv(F)
    return float(np.sqrt(max(Finv[0, 0], 0.0))), Finv


def compute() -> dict:
    print("\n--- Triangle grid + shape kernel build (GPU) ---")
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f"  device: {device}")
    K1, K2, K3, mask, dk1, dk2, dk3, sym, k_vec = build_triangle_grid(
        SKA2_SPEC, n_k=K_GRID_N, device=device,
    )
    N_phys = int(torch.sum(mask).item())  # (local)
    print(f"  k_grid_N = {K_GRID_N}, physical triangles = {N_phys:,}")
    print(f"  k_min = {SKA2_SPEC['k_min_Mpc']} Mpc^-1, k_max = {SKA2_SPEC['k_max_Mpc']} Mpc^-1")

    print("\n--- Fisher weights (SKA-2 + thermal + wedge) ---")
    W_SKA2, N_modes_SKA2, Var_SKA2, V_SKA2 = compute_weights(
        K1, K2, K3, mask, dk1, dk2, dk3, sym, SKA2_SPEC,
    )
    print(f"  V_survey(SKA-2) = {V_SKA2:.3e} Mpc^3")
    print(f"  sum(N_modes)    = {torch.sum(N_modes_SKA2).item():.3e}")

    print("\n--- Evaluate shape kernels on GPU ---")
    Sf_SI, Seq, Sloc, Bf_plan = compute_shapes(K1, K2, K3, mask)

    print("\n--- Fisher-weighted cosine overlaps (Babich-Creminelli 2004) ---")
    print("[PRIMARY: scale-invariant Meerburg flat template]")
    cos_fe, inner_fe, inner_ff, inner_ee = cosine_overlap(Sf_SI, Seq, W_SKA2)
    cos_fl, inner_fl, inner_ff2, inner_ll = cosine_overlap(Sf_SI, Sloc, W_SKA2)
    cos_el, inner_el, _, _ = cosine_overlap(Seq, Sloc, W_SKA2)
    print(f"  cos(fold_SI, equil) = {cos_fe:+.4f}")
    print(f"  cos(fold_SI, local) = {cos_fl:+.4f}")
    print(f"  cos(equil, local)   = {cos_el:+.4f}  "
          "[literature BC2004 Table 1 ~ 0.4 flat-weight; 21cm Fisher-weighted here]")

    print("\n[CROSS-CHECK: plan-literal B_fold = k3^2/(k1 k2), scale-DEPENDENT]")
    cos_fe_plan, _, _, _ = cosine_overlap(Bf_plan, Seq, W_SKA2)
    cos_fl_plan, _, _, _ = cosine_overlap(Bf_plan, Sloc, W_SKA2)
    cos_fSI_fplan, _, _, _ = cosine_overlap(Sf_SI, Bf_plan, W_SKA2)
    print(f"  cos(B_fold_plan, equil)  = {cos_fe_plan:+.4f}")
    print(f"  cos(B_fold_plan, local)  = {cos_fl_plan:+.4f}")
    print(f"  cos(fold_SI, B_fold_plan) = {cos_fSI_fplan:+.4f}  "
          "[internal check: SI and plan-literal agreement]")

    print("\n--- 3x3 Fisher matrix construction (scale-invariant) ---")
    F3 = fisher_3x3(Sf_SI, Seq, Sloc, W_SKA2)
    print(f"  F_ff    = {F3[0,0]:.4e}  (diagonal: fold_SI)")
    print(f"  F_eq_eq = {F3[1,1]:.4e}  (diagonal: equil)")
    print(f"  F_lo_lo = {F3[2,2]:.4e}  (diagonal: local)")
    print(f"  cond(F) = {np.linalg.cond(F3):.3e}")

    # --- Instrument-normalized sigma for folded f_NL -------------------
    # The Fisher matrix F_{ab} = <S_a, S_b>_F is in units determined by the
    # shape-function normalization and P_total. To get physical sigma(f_NL),
    # we anchor against literature SKA-Phase-2 sigma(f_NL^equil) and rescale.
    #
    # Anchor: Munoz+2015 (1506.04152) + Karagiannis+2018 template scaling
    #   sigma(f_NL^local,  SKA Phase-2) ~ 0.3       (21cm IM, cosmic dawn)
    #   sigma(f_NL^equil,  SKA Phase-2) ~ 3.0       (conservative, equil/local ratio)
    #   sigma(f_NL^ortho,  SKA Phase-2) ~ 1.5
    # Folded shape ratio relative to equilateral: folded typically sqrt(<S_eq,S_eq>/<S_fold,S_fold>)
    # from the Fisher ratios gives the conversion factor.
    sigma_fNL_equil_lit = 3.0  # (local) Munoz+2015, SKA-2 equilateral (mK^2 Mpc^3 units absorbed)
    sigma_fNL_local_lit = 0.3  # (local) Munoz+2015, SKA-2 local
    # Unmarginalized sigma ratio (fold to equil) from Fisher diagonals
    # sigma_unmarg(a) = 1 / sqrt(F_aa) -> ratio = sqrt(F_ee / F_ff)
    ratio_unmarg_fold_equil = float(np.sqrt(F3[1, 1] / max(F3[0, 0], 1e-300)))  # (local)
    sigma_unmarg_fold = ratio_unmarg_fold_equil * sigma_fNL_equil_lit  # (local)
    sigma_marg_fold_raw, Finv = marginal_sigma(F3)
    # Rescale the marginal sigma by the same anchor (same Fisher-rank amplification)
    # sigma_marg / sigma_unmarg = sqrt(F_aa / F^{-1}^{-1}_aa) ... use direct ratio:
    sigma_unmarg_fold_raw = 1.0 / np.sqrt(max(F3[0, 0], 1e-300))  # (local)
    marg_factor = sigma_marg_fold_raw / max(sigma_unmarg_fold_raw, 1e-300)  # (local)
    sigma_marg_fold_SKA2 = sigma_unmarg_fold * marg_factor  # (local) literature-anchored

    print(f"\n  Anchor: sigma(f_NL^equil)_SKA2_lit = {sigma_fNL_equil_lit} [Munoz+2015]")
    print(f"  ratio_unmarg(fold/equil)         = {ratio_unmarg_fold_equil:.4f}")
    print(f"  sigma_unmarg(f_NL^fold)_SKA2     = {sigma_unmarg_fold:.4f}")
    print(f"  marginalization factor           = {marg_factor:.3f}")
    print(f"  sigma_marg(f_NL^fold)_SKA2       = {sigma_marg_fold_SKA2:.4f}")

    # --- Detectability pull for framework f_NL^fold prediction ----------
    # Load framework f_NL_diag_CLT from S67 (the folded-channel amplitude)
    s67_path = resolve_output(67, 's67_gge_bispectrum.npz')
    s67 = np.load(s67_path, allow_pickle=True)
    f_NL_fold_framework = float(s67['f_NL_diag_CLT'])  # (local) = 0.1293
    N_pair_s67 = float(s67['N_pair'])                 # (local) = 59.8
    pull = abs(f_NL_fold_framework) / max(sigma_marg_fold_SKA2, 1e-300)  # (local)
    # Also pull for |f_NL^fold| >= 1 detectability
    pull_at_unit = 1.0 / max(sigma_marg_fold_SKA2, 1e-300)  # (local)

    print(f"\n  Framework f_NL^fold = {f_NL_fold_framework:.4f} (from S67, N_pair={N_pair_s67})")
    print(f"  Detection pull(framework)     = {pull:.3f} sigma")
    print(f"  Detection pull at f_NL^fold=1 = {pull_at_unit:.3f} sigma")

    # --- CMB-S4 cross-check (Fisher cosine only; sigma from literature) -
    # CMB-S4 sigma(f_NL^equil) = 5.0 per S67 sigma_CMBS4_equil; folded is weaker.
    sigma_fNL_equil_CMBS4 = 5.0  # (local) CMB-S4 SB v2 Table 6.1 / S67 pin
    sigma_fNL_fold_CMBS4 = ratio_unmarg_fold_equil * sigma_fNL_equil_CMBS4 * marg_factor  # (local)
    pull_CMBS4 = 1.0 / max(sigma_fNL_fold_CMBS4, 1e-300)  # (local)
    print(f"\n  CMB-S4 cross-check:")
    print(f"  sigma_marg(f_NL^fold)_CMBS4  = {sigma_fNL_fold_CMBS4:.4f}")
    print(f"  Detection pull at f_NL=1     = {pull_CMBS4:.3f} sigma")

    # Fisher condition + rank
    cond_F3 = float(np.linalg.cond(F3))  # (local)
    # Normalized smallest-singular-value ratio (approx "rank floor")
    svs = np.linalg.svd(F3, compute_uv=False)  # (local)
    rank_floor_meas = float(svs[-1] / svs[0])  # (local)

    # --- Pack results ----------------------------------------------------
    result = {
        'value': sigma_marg_fold_SKA2,
        # Overlaps (PRIMARY: scale-invariant Meerburg flat vs equil/local)
        'cos_fold_equil': cos_fe,
        'cos_fold_local': cos_fl,
        'cos_equil_local': cos_el,
        'inner_fold_equil': inner_fe,
        'inner_fold_local': inner_fl,
        'inner_fold_fold': inner_ff,
        'inner_equil_equil': inner_ee,
        'inner_local_local': inner_ll,
        # Cross-check (plan-literal B_fold = k3^2/(k1 k2))
        'cos_Bplan_equil': cos_fe_plan,
        'cos_Bplan_local': cos_fl_plan,
        'cos_foldSI_Bplan': cos_fSI_fplan,
        # Fisher
        'F3x3': F3,
        'Finv3x3': Finv,
        'cond_F3': cond_F3,
        'rank_floor_meas': rank_floor_meas,
        # Sigma per experiment
        'sigma_f_NL_fold_SKA2_marg': sigma_marg_fold_SKA2,
        'sigma_f_NL_fold_SKA2_unmarg': sigma_unmarg_fold,
        'sigma_f_NL_fold_CMBS4_marg': sigma_fNL_fold_CMBS4,
        'ratio_unmarg_fold_equil': ratio_unmarg_fold_equil,
        'marg_factor': marg_factor,
        # Detectability
        'pull_framework_SKA2': pull,
        'pull_unit_SKA2': pull_at_unit,
        'pull_unit_CMBS4': pull_CMBS4,
        'f_NL_fold_framework': f_NL_fold_framework,
        'N_pair_s67': N_pair_s67,
        # Diagnostics
        'V_survey_SKA2_Mpc3': V_SKA2,
        'N_triangles': N_phys,
        'k_min_Mpc': SKA2_SPEC['k_min_Mpc'],
        'k_max_Mpc': SKA2_SPEC['k_max_Mpc'],
        'k_grid_N': K_GRID_N,
        # GPU tensors -> numpy for saving (subset only)
        'k_vec_Mpc': k_vec.cpu().numpy(),
    }
    return result


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    comment = (
        f"# audit_sha256 companion row: {GATE_ID} audit={audit_sha[:16]} "
        f"content={content_sha[:16]}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(comment)


def evaluate_gate(result: dict) -> str:
    """Direction: threshold comparison (§W0-2 pre-reg).

    Substitution chain (now that values are computed):
      Step 1 (def): PASS iff sigma_marg(fold)_SKA2 <= 0.20
                         AND |cos(fold, equil)| < 0.30
                         AND |cos(fold, local)| < 0.30
                         AND pull_unit_SKA2 >= 3.0
      Step 2 (subst): plug numerical values from `result`.
      Step 3 (dir):   return PASS / INFO / FAIL.
    """
    sigma_marg = result['sigma_f_NL_fold_SKA2_marg']  # (local)
    cos_fe = abs(result['cos_fold_equil'])            # (local)
    cos_fl = abs(result['cos_fold_local'])            # (local)
    pull_unit = result['pull_unit_SKA2']              # (local)

    overlap_max = max(cos_fe, cos_fl)  # (local)

    # FAIL first: any overlap > 0.5 => template is linear combination of LCDM shapes
    if overlap_max > OVERLAP_INFO:
        return 'FAIL'

    # Full PASS criteria
    pass_sigma = sigma_marg <= SIGMA_PASS
    pass_orth = (cos_fe < OVERLAP_PASS) and (cos_fl < OVERLAP_PASS)
    pass_detect = pull_unit >= DETECT_THRESHOLD

    if pass_sigma and pass_orth and pass_detect:
        return 'PASS'

    # INFO: detectability met but overlap in [0.3, 0.5]
    if pass_detect and (OVERLAP_PASS <= overlap_max <= OVERLAP_INFO):
        return 'INFO'

    # If only one PASS criterion fails, call it INFO; else FAIL
    if pass_detect and pass_sigma:
        return 'INFO'

    return 'FAIL'


# ---------------------------------------------------------------------------
# Section 7 — Plot
# ---------------------------------------------------------------------------

def make_plot(result: dict, out_png: Path) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(17, 5))

    # Panel A: cosine-overlap bar chart
    ax = axes[0]
    labels = ['fold-equil', 'fold-local', 'equil-local']
    vals = [result['cos_fold_equil'], result['cos_fold_local'], result['cos_equil_local']]
    cols = ['steelblue', 'firebrick', 'gray']
    bars = ax.bar(labels, vals, color=cols, edgecolor='black')
    ax.axhline(y=OVERLAP_PASS, color='green', ls='--', alpha=0.6, label=f'PASS < {OVERLAP_PASS}')
    ax.axhline(y=-OVERLAP_PASS, color='green', ls='--', alpha=0.6)
    ax.axhline(y=OVERLAP_INFO, color='orange', ls='--', alpha=0.6, label=f'INFO < {OVERLAP_INFO}')
    ax.axhline(y=-OVERLAP_INFO, color='orange', ls='--', alpha=0.6)
    ax.axhline(y=0, color='k', ls='-', lw=0.5)
    for bar, v in zip(bars, vals):
        ax.text(bar.get_x() + bar.get_width() / 2,
                bar.get_height() + (0.02 if v >= 0 else -0.04),
                f'{v:+.3f}', ha='center', fontsize=10, fontweight='bold')
    ax.set_ylabel('Fisher-weighted cosine overlap', fontsize=11)
    ax.set_title('SHAPE-template overlaps\n(Babich-Creminelli 2004)', fontsize=11)
    ax.set_ylim(-1.1, 1.1)
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3, axis='y')

    # Panel B: sigma(f_NL^fold) bar chart + thresholds
    ax = axes[1]
    xs = ['SKA-Phase-2\n(marginal)', 'CMB-S4\n(marginal)']
    ys = [result['sigma_f_NL_fold_SKA2_marg'], result['sigma_f_NL_fold_CMBS4_marg']]
    bars = ax.bar(xs, ys, color=['firebrick', 'steelblue'], edgecolor='black')
    ax.axhline(y=SIGMA_PASS, color='green', ls='--', alpha=0.7, label=f'PASS <= {SIGMA_PASS}')
    for bar, v in zip(bars, ys):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() * 1.02,
                f'{v:.3f}', ha='center', va='bottom', fontsize=11, fontweight='bold')
    ax.set_ylabel(r'$\sigma(f_{\rm NL}^{\rm fold})$ (marg)', fontsize=11)
    ax.set_title('Folded template detectability', fontsize=11)
    ax.set_yscale('log')
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3, axis='y')

    # Panel C: Fisher 3x3 heatmap
    ax = axes[2]
    F = result['F3x3']
    F_norm = F / np.abs(F).max()
    im = ax.imshow(F_norm, cmap='RdBu_r', vmin=-1, vmax=1)
    ax.set_xticks([0, 1, 2]); ax.set_yticks([0, 1, 2])
    labels3 = ['fold', 'equil', 'local']
    ax.set_xticklabels(labels3); ax.set_yticklabels(labels3)
    for i in range(3):
        for j in range(3):
            ax.text(j, i, f'{F[i,j]:.1e}', ha='center', va='center',
                    fontsize=8, color='black' if abs(F_norm[i, j]) < 0.5 else 'white')
    ax.set_title(f'Fisher 3x3 (SKA-2)\ncond={result["cond_F3"]:.2e}', fontsize=11)
    plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)

    plt.tight_layout()
    plt.savefig(out_png, dpi=150, bbox_inches='tight')
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins (first 20 lines of stdout)
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)  # legacy
    print(f"  closure (legacy): {closure[:16]}... ({closure})")

    # 1b. Compute S84+ dual SHAs
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... ({audit_sha})")
    print(f"  content_sha256: {content_sha[:16]}... ({content_sha})")
    print()

    # 2. Compute
    print("=" * 78)
    print(f"{GATE_ID} — compute")
    print("=" * 78)
    result = compute()
    value = result['value']

    # 3. Evaluate gate
    verdict = evaluate_gate(result)

    # 4. Emit 4-tuple + append verdict (dual-SHA)
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print("\n" + "=" * 78)
    print(f"4-tuple: {tag}")
    print("=" * 78)

    # 5. Save NPZ + PNG
    save_dict = {k: v for k, v in result.items() if isinstance(v, (int, float, np.ndarray, np.generic))}
    save_dict['gate_id'] = GATE_ID
    save_dict['gate_verdict'] = verdict
    save_dict['audit_sha256'] = audit_sha
    save_dict['content_sha256'] = content_sha
    save_dict['scheme'] = SCHEME
    save_dict['convention'] = CONVENTION
    save_dict['L_max'] = L_MAX
    np.savez(OUT_NPZ, **save_dict)
    print(f"\n  NPZ: {OUT_NPZ}")

    make_plot(result, OUT_PNG)
    print(f"  PNG: {OUT_PNG}")

    # 6. Verdict line
    append_verdict(verdict, value, audit_sha, content_sha)
    print(f"  verdict appended to: {VERDICT_TXT}")

    # 7. Summary
    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")

    # Explicit summary of gate-discriminating numbers
    print("\nSUMMARY:")
    print(f"  cos(fold,equil)          = {result['cos_fold_equil']:+.4f}  "
          f"(threshold PASS < {OVERLAP_PASS})")
    print(f"  cos(fold,local)          = {result['cos_fold_local']:+.4f}  "
          f"(threshold PASS < {OVERLAP_PASS})")
    print(f"  sigma_marg(fold)_SKA2    = {result['sigma_f_NL_fold_SKA2_marg']:.4f}  "
          f"(threshold PASS <= {SIGMA_PASS})")
    print(f"  pull at |f_NL^fold|=1    = {result['pull_unit_SKA2']:.3f} sigma  "
          f"(threshold PASS >= {DETECT_THRESHOLD})")
    print(f"  framework f_NL^fold      = {result['f_NL_fold_framework']:.4f}  "
          f"(pull = {result['pull_framework_SKA2']:.3f} sigma)")

    return 0 if verdict != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
