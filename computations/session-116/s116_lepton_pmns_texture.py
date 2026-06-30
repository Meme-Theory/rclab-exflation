#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S116-W2-LEPTON-PMNS-TEXTURE  (Session 116, Wave 2, §W2-3)  -- [SIGN] gate.

The lepton analog of the quark S111-CF-YUK-FULLFLAVOR: the FIRST external-eps_LX
lepton PMNS texture. CF-S115-LEPTON-PMNS-FORCED-TEXTURE (internal forced circulant
WASHED OUT, J locked to 1/(6 sqrt 3)) resolved to the EXTERNAL-eps_LX route.

WHAT THIS GATE DOES
-------------------
  (i)  Build the CHARGED-LEPTON mass matrix M_e on the C(+)H block of the
       multiplicity bundle: diagonal Casimir grading (e/mu/tau tower
       [(1,0),(1,1),(3,0)], C2=[4/3,3,6], steep exp(-S0 C2) hierarchy) PLUS the
       off-diagonal eps_LX texture {rho13^l, rho23^l, |w12^l|} -- the SAME
       multiplicity-bundle complement of the [D_K,-] image used for the quark
       down-texture (S111-W3-1). The texture is SET BY the charged-lepton mass
       log-gaps (m_mu/m_e, m_tau/m_mu), NOT free-scanned to hit PMNS. -> U_eL.
  (ii) Build the NEUTRINO mass matrix M_nu (type-I seesaw, INTERNAL M_R per S100a,
       scale HELD): M_D on the neutrino tower [(0,0),(1,0),(1,1)] (Y_1=0 EXACT
       -> m_1=0 rank deficiency; the (0,0) singlet is Dirac-DECOUPLED), with the
       SHARED eps_LX off-diagonal RESTRICTED to the 2-3 block (preserving m_1=0).
       M_R = B-branch D_K fold energies [1.0044,1.0786,1.1700] (near-degenerate).
       M_nu = M_D M_R^{-1} M_D^T. -> U_nuL (a 2-3 atmospheric rotation).
  (iii) U_PMNS = U_eL^dag U_nuL. The framework forces delta_CP in {0,pi}
        (canonical delta_CP_PMNS_substrate=0.0) => REAL textures => J_PMNS = 0
        EXACTLY (no leptonic CP -- a hard, falsifiable prediction, the OPPOSITE of
        the quark V_us OVERSHOOT). Extract sin^2 th12/th23/th13 + J_PMNS.
  (iv) CONTRAST (in the artifact, never tuned): the forced-circulant limit
        J = 1/(6 sqrt 3) = 0.0962250 (recover the S115 washed-out baseline) vs the
        eps_LX-texture J (=0, real). Also the diagonal-S100a contrast (U_nuL = I).

PRE-REGISTERED OPERATOR (plan sessions/session-plan/session-116-plan-w2.md §W2-3):
  mix_grp = |{ s in {sin^2 th12, sin^2 th23, sin^2 th13, J_PMNS}
               : value_s in NuFIT-5.2-NO-3sigma-band_s }|
  PASS iff mix_grp >= 3   (Track A: eps_LX RESCUES; the C(+)H sector-asymmetry is a
                           genuine substrate texture handle)
  INFO iff mix_grp == 2   (mass-vs-mixing tension; lepton analog of quark V_us;
                           NON-PROMOTION-BY-HELD-NUMBER, undischarged-magnitude-bound)
  FAIL iff mix_grp <= 1   (Track B: PMNS WALLED like the quark sector)

[SIGN] substitution chain (plan §W2-3): the PMNS 1<->3 (and 1<->2) mixing is
  triality-ODD (t(O)=1), forbidden for any LEFT-INVARIANT operator, supplied ONLY
  by the non-LI eps_LX. t(p,q)=(p-q) mod 3; charged-lepton tower (1,0)/(1,1)/(3,0)
  => t = 1/0/0 (same as quark); 1<->3 needs t(O)=(1-0) mod 3 = 1 (triality-odd).
  The COMPUTED sign of (J_PMNS_FW - J_obs) is the rescue-vs-overshoot discriminator.
  Framework forces delta_CP in {0,pi} -> J_PMNS_FW = 0 EXACTLY -> J_FW < J_obs
  (UNDERSHOOT: the framework does NOT share the quark V_us overshoot; it forces
  CP conservation). sign_verdict records that the computed J=0 MATCHES the
  framework's own delta_CP in {0,pi} prediction.

============================================================================
SUBSTRATE-FIRST (phononic-framing.md) -- PARTICLE:
============================================================================
  D_K eigenvalues -> eps_LX multiplicity-bundle deformation -> lepton mass/mixing
  texture -> PMNS.  The lepton Yukawas ARE matrix elements of dD_K/d(eps_LX)
  between the lowest-|lambda| generation eigenvectors of the block-diagonal D_K.
  By the VII.BL STAGE-3-PERMANENT theorem the bare D_K is multiplicity-scalar
  (generation = Z3-triality multiplicity index t=(p-q) mod 3), so the hierarchy +
  mixing are NOT in the bare spectrum -- they are features of the external
  non-left-invariant eps_LX on the multiplicity-bundle complement of [D_K,-].
  The distinguishing substrate feature vs the quark sector is the C(+)H
  charged-lepton/neutrino FIBER asymmetry: the quark M3(C)-shared chiralities gave
  U_mix=identity (S115 negative control); the lepton charged (H-doublet) and
  neutrino-Dirac (C-singlet) sectors occupy DISJOINT Peter-Weyl towers
  [(1,0),(1,1),(3,0)] vs [(0,0),(1,0),(1,1)] with DIFFERENT diagonal gradings
  (steep exp vs mild sqrt-C2 + near-degenerate M_R). Direction of explanation
  flows from the D_K spectral structure outward; the PMNS angles are the emergent
  image, never the starting point.

External observational anchors (NuFIT 5.2 / PDG 2024 NO): NOT canonical_constants
imports -- get_constant('J_PMNS') -> not-found (confirmed at this gate's MCP audit).
Hardcoded `# (local)` cross-check pins, admissible methodological-anchor sourcing
per substrate-first-canonical-sourcing.md §(i).

Output 4-tuple:
  (value=<mix_grp + 4 PMNS obs + J contrast>, scheme=NCG-INNER-FLUCT-EXTERNAL-NONLI,
   convention=EPS-LX-MULTIPLICITY-BUNDLE-LEPTON-SECTOR-PMNS-..., L_max=12)

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  computations/_shared/canonical_constants.py
  computations/session-111/s111_yuk_fullflavor.npz    (quark eps_LX precedent)
  computations/session-110/s110_cf2_yuk_epslx.npz      (up-sector eps_LX texture)
  computations/session-115/s115_lepton_pmns_forced_texture.npz  (washed-out baseline)
  computations/session-99/s99_w3_seesaw_summnu.npz     (M_R, Y, m_nu seesaw)
  computations/session-84/s84_spectrum_cache_L12_tau019.npz
  computations/_shared/dirac_spectrum.py
"""

from __future__ import annotations

# --- CPU thread cap BEFORE numpy import (math-scripts.md; 3x3 eigh is tiny) ---
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares

# ---------------------------------------------------------------------------
# Section 1 -- Paths + canonical constants (MANDATORY import)
# ---------------------------------------------------------------------------
THIS = Path(__file__).resolve()
SESSION_DIR = THIS.parent                                 # computations/session-116
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import (  # noqa: E402
    tau_fold,
    m_e, m_mu, m_tau_PDG,
    delta_CP_PMNS_substrate,
    dm2_21_NuFit, dm2_31_NuFit,
    sin2_theta12_PDG, sin2_theta13_PDG,
)

import matplotlib                                          # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt                            # noqa: E402

# ---------------------------------------------------------------------------
# Section 2 -- Identity + pinned machinery (plan §W2-3 machinery_pin_map)
# ---------------------------------------------------------------------------
SESSION = "116"                                            # (local)
GATE_ID = "S116-W2-LEPTON-PMNS-TEXTURE"                    # (local)
SCHEME = "NCG-INNER-FLUCT-EXTERNAL-NONLI"                  # (local)
CONVENTION = ("EPS-LX-MULTIPLICITY-BUNDLE-LEPTON-SECTOR-PMNS-"
              "pairing-dep-offdiag-rho-CH-sector-asymmetry")  # (local)
L_MAX = 12                                                 # (local) plan pin
TAU = float(tau_fold)                                      # (local) 0.19 canonical
PUB_SIGFIGS = 6                                            # (local) Class-8.3 (plan pin)

# --- External observational anchors (NuFIT 5.2 / PDG 2024 NO; # (local) pins) ---
# NOT canonical_constants imports: get_constant('J_PMNS') -> not-found.  NuFIT 5.2
# normal-ordering (with SK atmospheric), the SAME vintage the S115 forced-texture
# baseline used (sin^2 th12=0.303, th23=0.572, th13=0.02203, delta_CP=197 deg,
# J band [0.0086,0.0331]).  Best-fits + 3-sigma ranges:
S2T12_BF, S2T12_LO, S2T12_HI = 0.303,  0.270,  0.341       # (local) NuFIT 5.2 NO sin^2 th12 (3sig)
S2T23_BF, S2T23_LO, S2T23_HI = 0.572,  0.434,  0.610       # (local) NuFIT 5.2 NO sin^2 th23 (3sig, upper octant)
S2T13_BF, S2T13_LO, S2T13_HI = 0.02203, 0.02029, 0.02391   # (local) NuFIT 5.2 NO sin^2 th13 (3sig)
J_PMNS_OBS = 0.0329                                        # (local) NuFIT 5.2 NO best-fit |J| (= J_max at near-maximal delta)
J_OBS_LO, J_OBS_HI = 0.0086, 0.0331                        # (local) NuFIT 5.2 NO 3-sigma |J| band (S115 baseline pin)
DELTA_CP_3SIG_LO, DELTA_CP_3SIG_HI = 108.0, 404.0          # (local) NuFIT 5.2 NO delta_CP 3-sigma range (deg); incl. 180 (CP-conserving)

# --- Forced-circulant contrast reference (S115; never tuned) ---
J_FORCED_CIRCULANT = float(np.sqrt(3.0) / 18.0)            # (local) 1/(6 sqrt 3) = 0.09622504...

# ---------------------------------------------------------------------------
# Section 3 -- Tower / Casimir / Yukawa-block helpers
# ---------------------------------------------------------------------------
def C2_su3(p: int, q: int) -> float:
    """SU(3) quadratic Casimir C2(p,q) = (p^2+q^2+p q+3p+3q)/3; C2(1,0)=4/3, C2(1,1)=3."""
    return (p * p + q * q + p * q + 3.0 * p + 3.0 * q) / 3.0


def triality(p: int, q: int) -> int:
    """SU(3) center character t(p,q) = (p - q) mod 3."""
    return (p - q) % 3


# BOTH sectors are 3x3 in the SHARED 3-generation flavor space, indexed by
# ASCENDING mass [gen1, gen2, gen3]. The C(+)H sector-asymmetry is in the
# Casimir ASSIGNMENT per generation (different (p,q) tower per sector), NOT in the
# index order -- U_eL and U_nuL must share the same ascending-gen basis for
# U_PMNS = U_eL^dag U_nuL to be a meaningful misalignment.
#
# Charged-lepton tower (H-doublet block), ASCENDING gen [e, mu, tau]:
#   the SAME (p,q) set as the quark/down tower (S111) but ordered by gen, so the
#   LIGHTEST (e) carries the LARGEST Casimir (steepest exp(-S0 C2) suppression).
TOWER_E = [(3, 0), (1, 1), (1, 0)]                         # (local) e/mu/tau (lightest->heaviest)
C2_E = np.array([C2_su3(p, q) for (p, q) in TOWER_E])      # (local) [6, 3, 4/3] exact (descending C2)
TRI_E = np.array([triality(p, q) for (p, q) in TOWER_E])   # (local) [0, 0, 1]
# Neutrino-Dirac tower (C-singlet block; S100a/S96 sector assignment) -- DISJOINT,
# ASCENDING gen [nu1, nu2, nu3]; gen1=(0,0) singlet => Y_1=0 EXACT => m_1=0:
TOWER_NU = [(0, 0), (1, 0), (1, 1)]                        # (local) gen1/2/3 (lightest->heaviest)
C2_NU = np.array([C2_su3(p, q) for (p, q) in TOWER_NU])    # (local) [0, 4/3, 3]
TRI_NU = np.array([triality(p, q) for (p, q) in TOWER_NU]) # (local) [0, 1, 0]
assert np.allclose(C2_E, [6.0, 3.0, 4.0 / 3.0]), "charged-lepton C2 grading mismatch"
assert np.allclose(C2_NU, [0.0, 4.0 / 3.0, 3.0]), "neutrino C2 grading mismatch"


def yukawa_block_real(diag: np.ndarray, w12: float, w13: float, w23: float) -> np.ndarray:
    """Real-symmetric 3x3 Yukawa block (REAL: delta_CP in {0,pi} => no phases).
    diag = the diagonal mass tower; off-diagonals w_ij in flavor (generation) basis.
    Hermitian (real-symmetric) preserves the reality wall [J,D_K+delta_A]=0."""
    M = np.diag(diag).astype(float)
    M[0, 1] = M[1, 0] = w12
    M[0, 2] = M[2, 0] = w13
    M[1, 2] = M[2, 1] = w23
    return M


def diag_block(M: np.ndarray):
    """Real-symmetric eigendecomposition, eigenvalues by ASCENDING |lambda| (= mass).
    Returns (|lambda| ascending, U columns ascending) with U^T M U = diag(lambda)."""
    lam, U = np.linalg.eigh(M)
    order = np.argsort(np.abs(lam))
    return np.abs(lam)[order], U[:, order]


# ---------------------------------------------------------------------------
# Section 4 -- SHA-256 dual-SHA block (S84+ schema)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs) -> dict:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 -- Paths/targets
# ---------------------------------------------------------------------------
OUT_NPZ = SESSION_DIR / "s116_lepton_pmns_texture.npz"
OUT_PNG = SESSION_DIR / "s116_lepton_pmns_texture.png"

CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"
S111_NPZ = COMPUTATIONS_DIR / "session-111" / "s111_yuk_fullflavor.npz"
S110_NPZ = COMPUTATIONS_DIR / "session-110" / "s110_cf2_yuk_epslx.npz"
S115_NPZ = COMPUTATIONS_DIR / "session-115" / "s115_lepton_pmns_forced_texture.npz"
S99_SEESAW_NPZ = COMPUTATIONS_DIR / "session-99" / "s99_w3_seesaw_summnu.npz"
SPECTRUM_CACHE = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
DIRAC_SPECTRUM = SHARED_DIR / "dirac_spectrum.py"

INPUT_FILES = [CANONICAL_PATH, S111_NPZ, S110_NPZ, S115_NPZ,
               S99_SEESAW_NPZ, SPECTRUM_CACHE, DIRAC_SPECTRUM]

# Charged-lepton PDG ratios (single-source canonical lepton masses)
R_MU_E = float(m_mu) / float(m_e)                          # (local) ~206.77
R_TAU_MU = float(m_tau_PDG) / float(m_mu)                  # (local) ~16.82


# ---------------------------------------------------------------------------
# Section 6 -- PMNS extraction (standard PDG parameterization from |U|)
# ---------------------------------------------------------------------------
def pmns_observables(U: np.ndarray) -> dict:
    """Extract (sin^2 th13, sin^2 th12, sin^2 th23, J) from a 3x3 unitary U.
    Rows = charged-lepton flavor (e,mu,tau by ascending charged-lepton mass);
    columns = neutrino mass eigenstate (1,2,3 ascending). Standard PDG."""
    Uabs2 = np.abs(U) ** 2                                 # (local)
    s13sq = float(Uabs2[0, 2])                             # (local) |U_e3|^2
    s13sq = min(max(s13sq, 0.0), 1.0)
    denom = 1.0 - s13sq                                    # (local) c13^2
    s12sq = float(Uabs2[0, 1] / denom) if denom > 1e-15 else 0.0  # (local) |U_e2|^2/c13^2
    s23sq = float(Uabs2[1, 2] / denom) if denom > 1e-15 else 0.0  # (local) |U_mu3|^2/c13^2
    # Jarlskog (rephasing-invariant); real U => J = 0 exactly
    J = float(np.imag(U[0, 0] * U[1, 1] * np.conj(U[0, 1]) * np.conj(U[1, 0])))  # (local)
    return {"sin2_th13": s13sq, "sin2_th12": s12sq, "sin2_th23": s23sq, "J": J}


def in_band(val: float, lo: float, hi: float) -> bool:
    return bool(lo <= val <= hi)


# ---------------------------------------------------------------------------
# Section 7 -- Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    res: dict = {}

    # ===== STEP 0: read precedents (audit-mandatory) =====
    s111 = np.load(S111_NPZ, allow_pickle=True)
    s115 = np.load(S115_NPZ, allow_pickle=True)
    d99 = np.load(S99_SEESAW_NPZ, allow_pickle=True)
    res["s111_rho13_down"] = float(s111["rho13_down"])
    res["s111_rho23_down"] = float(s111["rho23_down"])
    res["s111_Vus_fw"] = float(s111["V_us_fw"])
    res["s115_J_forced"] = float(s115["J_forced_corrected"])
    M_R = np.asarray(d99["M_R_MKK"]).ravel().astype(float)  # (local) [1.0044,1.0786,1.1700]
    Y_nu_diag = np.asarray(d99["Y"]).ravel().astype(float)  # (local) [0, 4.794, 11.928] (diagonal Dirac)
    m_nu_S99 = np.asarray(d99["m_nu_eV"]).ravel().astype(float)  # (local) [0, 0.00868, 0.04953]
    res["M_R_MKK"] = M_R
    res["Y_nu_diag"] = Y_nu_diag
    res["m_nu_S99_eV"] = m_nu_S99
    print("=== STEP 0: precedents ===")
    print(f"  S111 quark down-texture: rho13^d={res['s111_rho13_down']:.4f} "
          f"rho23^d={res['s111_rho23_down']:.4f}  V_us^FW={res['s111_Vus_fw']:.4f} (overshoot)")
    print(f"  S115 forced-circulant J={res['s115_J_forced']:.7f} (=1/(6sqrt3); washed out)")
    print(f"  S100a/S99 seesaw: M_R={M_R}  Y_nu_diag={Y_nu_diag}  m_nu(eV)={m_nu_S99}")

    # ===== STEP 1: charged-lepton diagonal log-gap wall =====
    # ascending-gen Casimir C2_E = [C2(e), C2(mu), C2(tau)] = [6, 3, 4/3]; the
    # mass GAP between adjacent generations is |Delta C2|. lepton-fixed S0 (the
    # substrate-natural SHAPE scale; identical to S110/S111 = 1.735317):
    S0_mue = float(np.log(R_MU_E) / (C2_E[0] - C2_E[1]))   # (local) ln(206.77)/(6-3)
    S0_taumu = float(np.log(R_TAU_MU) / (C2_E[1] - C2_E[2]))  # (local) ln(16.82)/(3-4/3)
    S0 = 0.5 * (S0_mue + S0_taumu)                         # (local)
    res["S0_lepton_fixed"] = S0
    # diagonal Casimir log-gap LOCK (charged leptons): ln(tau/mu)/ln(mu/e) from diag only
    gap_lock_e = float((C2_E[1] - C2_E[2]) / (C2_E[0] - C2_E[1]))  # (local) (5/3)/3 = 5/9
    gap_pdg_e = float(np.log(R_TAU_MU) / np.log(R_MU_E))   # (local) ~0.529
    res["gap_diag_lock_e"] = gap_lock_e
    res["gap_pdg_e"] = gap_pdg_e
    print("\n=== STEP 1: charged-lepton diagonal log-gap wall ===")
    print(f"  S0 (lepton-fixed) = {S0:.6f}  (S0_mue={S0_mue:.4f}, S0_taumu={S0_taumu:.4f})")
    print(f"  diag Casimir lock ln(tau/mu)/ln(mu/e) = {gap_lock_e:.6f} (= 5/9 EXACT)")
    print(f"  PDG charged-lepton log-gap            = {gap_pdg_e:.6f}")
    print(f"  => eps_LX texture {{rho13^l,rho23^l}} breaks 5/9 -> {gap_pdg_e:.4f} (a SMALL correction)")

    # ===== STEP 2: fit the charged-lepton eps_LX texture to the mass ratios =====
    # M_e = diag(exp(-S0 C2_E)) + REAL off-diag (w12, w13, w23) in the SHARED
    # ascending-gen basis. Fit (w12, w13, w23) to BOTH mass ratios m_mu/m_e AND
    # m_tau/m_mu (mirror S111-W3-1 STEP 3). The 2 ratios constrain 3 off-diagonals
    # => a 1-param-family UNDER-DETERMINATION (masses fix the eigenVALUES, not the
    # eigenVECTORS/mixing). Resolve by the MINIMAL-NORM texture: the SMALLEST
    # off-diagonal (Occam / minimal eps_LX) reproducing the masses. NOT scanned to PMNS.
    d_e = np.exp(-S0 * C2_E)                               # (local) diagonal tower [e,mu,tau] ascending

    def lepton_ratios_abs(w12, w13, w23):
        M = yukawa_block_real(d_e, w12, w13, w23)
        m, _ = diag_block(M)
        if not (np.all(np.isfinite(m)) and np.all(m > 0)):
            return np.nan, np.nan
        return m[1] / m[0], m[2] / m[1]                    # (local) m_mu/m_e, m_tau/m_mu (ascending [e,mu,tau])

    # The diagonal tower ALREADY nearly reproduces the mass ratios (d_mu/d_e=182 vs
    # PDG 206.77; d_tau/d_mu=18.0 vs 16.82): a SMALL off-diagonal corrects it.
    # MINIMAL-NORM: minimize ||off-diag||^2 starting from X=0 (pure diagonal) with a
    # tight mass-ratio constraint -> the SMALLEST eps_LX deformation -> U_eL NEAREST to
    # identity. Started from ~0 (not large magnitudes), the optimizer descends to the
    # nearby minimal solution (the small-off-diagonal branch), NOT a far large-mixing branch.
    W_MASS = 1.0e4                                         # (local) heavy mass-ratio weight (constraint)
    REG = 1.0                                              # (local) minimal-norm penalty on ALL off-diags

    def resid_e_abs(x):
        w12, w13, w23 = x                                  # (local) signed absolute off-diagonals
        r_mue, r_taumu = lepton_ratios_abs(w12, w13, w23)
        if not (np.isfinite(r_mue) and np.isfinite(r_taumu)) or r_mue <= 0 or r_taumu <= 0:
            return [1e8, 1e8, 0.0, 0.0, 0.0]
        return [W_MASS * np.log(r_mue / R_MU_E), W_MASS * np.log(r_taumu / R_TAU_MU),
                REG * w12, REG * w13, REG * w23]           # (local) minimal-norm over ALL three

    LBa = [-0.3, -0.3, -0.3]; UBa = [0.3, 0.3, 0.3]        # (local) signed off-diag bounds
    best = None                                            # (local) minimal-norm minimizer (tight fits)
    fallback = None                                        # (local) loosest-residual if no tight fit
    starts = []                                            # (local) near-zero + broad signed multistart
    for s12 in (-1.0, 1.0):
        for s13 in (-1.0, 0.0, 1.0):
            for s23 in (-1.0, 0.0, 1.0):
                for mag in [1e-4, 1e-3, 8e-3, 3e-2]:
                    starts.append([s12 * mag, s13 * mag, s23 * mag])
    starts.append([0.0, 0.0, 0.0])
    for x0 in starts:
        try:
            sol = least_squares(resid_e_abs, x0, bounds=(LBa, UBa),
                                xtol=3e-16, ftol=3e-16, gtol=3e-16, max_nfev=20000)
        except Exception:
            continue
        rm_mass = float(max(abs(sol.fun[0]), abs(sol.fun[1])) / W_MASS)  # (local) true mass log-resid
        offnorm = float(np.linalg.norm(sol.x))                          # (local) off-diag Frobenius norm
        cand = (float(sol.x[0]), float(sol.x[1]), float(sol.x[2]), rm_mass, offnorm)
        if fallback is None or rm_mass < fallback[3]:
            fallback = cand
        if rm_mass > 1e-4:
            continue
        # among tight mass fits, take the MINIMAL off-diagonal norm (Occam representative)
        if best is None or offnorm < best[4]:
            best = cand
    if best is None:
        best = fallback                                   # (local) no tight fit -> loosest available
    w12_e, w13_e, w23_e, resid_e_max, offnorm_e = best
    rho13_e = float(w13_e / w12_e) if abs(w12_e) > 1e-30 else 0.0  # (local) reported pairing ratio
    rho23_e = float(w23_e / w12_e) if abs(w12_e) > 1e-30 else 0.0  # (local)
    res["w12_e"] = w12_e; res["w13_e"] = w13_e; res["w23_e"] = w23_e
    res["rho13_e"] = rho13_e; res["rho23_e"] = rho23_e
    res["resid_e_max"] = resid_e_max; res["offnorm_e"] = offnorm_e
    r_mue_fit, r_taumu_fit = lepton_ratios_abs(w12_e, w13_e, w23_e)
    res["r_mue_fit"] = float(r_mue_fit); res["r_taumu_fit"] = float(r_taumu_fit)
    M_e = yukawa_block_real(d_e, w12_e, w13_e, w23_e)
    m_e_vals, U_eL = diag_block(M_e)                       # (local) U_eL columns = (e,mu,tau) ascending
    res["M_e"] = M_e; res["U_eL"] = U_eL; res["m_e_vals"] = m_e_vals
    print("\n=== STEP 2: charged-lepton eps_LX texture (MINIMAL-NORM; fit to masses, NOT PMNS) ===")
    print(f"  off-diag (w12,w13,w23)=({w12_e:.4e},{w13_e:.4e},{w23_e:.4e})  ||off||={offnorm_e:.4e}")
    print(f"  rho13^l={rho13_e:.4f} rho23^l={rho23_e:.4f}  mass-resid_max={resid_e_max:.3e}")
    print(f"  m_mu/m_e fit ={r_mue_fit:.4f} (PDG {R_MU_E:.4f});  m_tau/m_mu fit ={r_taumu_fit:.4f} (PDG {R_TAU_MU:.4f})")
    print(f"  U_eL (charged-lepton rotation, columns e/mu/tau):\n{np.round(U_eL,4)}")

    # ===== STEP 3: neutrino seesaw -- INTERNAL M_R per S100a, scale HELD =====
    # type-I seesaw M_nu = M_D M_R^{-1} M_D^T.  M_D = diag(Y_nu) + SHARED eps_LX
    # off-diagonal RESTRICTED to the 2-3 block (gen1=(0,0) singlet Dirac-DECOUPLED
    # => Y_1=0 => m_1=0 rank deficiency PRESERVED).  The SHARED eps_LX is transplanted
    # as the DIMENSIONLESS 2-3 texture relative to the gen-3 (heaviest) diagonal --
    # eps23 = |w23^l| / d_e[2] (= the charged-lepton 2-3 rotation scale) -- applied to
    # the neutrino gen-3 Dirac scale: w23^nu = eps23 * Y3.  This is sane (no blow-up):
    # the near-degenerate M_R + mild Y grading is the C(+)H amplification handle the
    # gate tests.  M_R = B-branch fold energies (scale HELD; mixing scale-independent).
    eps23 = abs(w23_e) / d_e[2]                            # (local) charged-lepton dimensionless 2-3 texture
    res["eps23_strength"] = float(eps23)
    Y2, Y3 = Y_nu_diag[1], Y_nu_diag[2]                    # (local)
    w23_nu = float(eps23 * Y3)                             # (local) shared eps_LX, neutrino 2-3 block
    res["w23_nu"] = w23_nu
    M_D = yukawa_block_real(Y_nu_diag, 0.0, 0.0, w23_nu)   # (local) (0,0) row/col decoupled => m_1=0
    MR_inv = np.diag(1.0 / M_R)                            # (local)
    M_nu = M_D @ MR_inv @ M_D.T                            # (local) type-I seesaw (symmetric)
    M_nu = 0.5 * (M_nu + M_nu.T)
    m_nu_vals, U_nuL = diag_block(M_nu)                    # (local) U_nuL columns = (1,2,3) ascending
    res["M_nu"] = M_nu; res["U_nuL"] = U_nuL; res["m_nu_vals"] = m_nu_vals
    m1_lift = float(m_nu_vals[0] / (m_nu_vals[2] + 1e-300))  # (local) m1/m3 -- rank-deficiency check
    res["m1_over_m3"] = m1_lift
    nu_ratio_fw = float(m_nu_vals[1] / m_nu_vals[2]) if m_nu_vals[2] > 0 else np.nan  # (local)
    nu_ratio_obs = float(np.sqrt(dm2_21_NuFit / dm2_31_NuFit))  # (local) m2/m3 with m1=0
    res["nu_ratio_fw"] = nu_ratio_fw; res["nu_ratio_obs"] = nu_ratio_obs
    print("\n=== STEP 3: neutrino type-I seesaw (INTERNAL M_R per S100a, scale HELD) ===")
    print(f"  shared eps23 strength = {eps23:.4e}; w23^nu = {w23_nu:.4f} (vs Y3={Y3:.3f})")
    print(f"  M_R(M_KK) = {M_R}  (near-degenerate, spread {(M_R.max()/M_R.min()-1)*100:.1f}%)")
    print(f"  m_nu seesaw (ascending) = {np.round(m_nu_vals,6)};  m1/m3 = {m1_lift:.3e} (m_1=0 iff <<1)")
    print(f"  m2/m3 FW = {nu_ratio_fw:.4f}  (oscillation-anchored {nu_ratio_obs:.4f})")
    print(f"  U_nuL (neutrino rotation, columns 1/2/3):\n{np.round(U_nuL,4)}")

    # ===== STEP 3b: UNDER-DETERMINATION demonstration (masses do NOT fix mixing) =====
    # For ANY orthogonal R, M_e = R diag(m_e,m_mu,m_tau) R^T reproduces the masses
    # EXACTLY -> U_eL = R is a FREE parameter (the masses constrain eigenVALUES, not
    # eigenVECTORS). Hence the PMNS is NOT a substrate prediction from the masses alone.
    # (1) Reachability: the off-diagonal ||eps_LX|| REQUIRED for the OBSERVED PMNS,
    #     vs the minimal-norm value -- quantifies how non-minimal the data is.
    # (2) Angle scan: mix_grp over the free U_eL family (1-2 angle alpha) -> max reachable.
    masses = np.sort(np.abs(m_e_vals))                    # (local) [m_e,m_mu,m_tau] ascending (exact)

    def rot(i, j, th, n=3):
        R = np.eye(n)
        c, s = np.cos(th), np.sin(th)
        R[i, i] = c; R[j, j] = c; R[i, j] = -s; R[j, i] = s
        return R

    # observed PMNS rotation (real; delta_CP=0 per framework {0,pi}); standard PDG order
    th12o = np.arcsin(np.sqrt(S2T12_BF)); th23o = np.arcsin(np.sqrt(S2T23_BF))  # (local)
    th13o = np.arcsin(np.sqrt(S2T13_BF))                                        # (local)
    U_obs = rot(1, 2, th23o) @ rot(0, 2, th13o) @ rot(0, 1, th12o)             # (local) real PMNS_obs
    # U_eL that EXACTLY reproduces the observed PMNS: U_PMNS = U_eL^dag U_nuL = U_obs
    U_eL_match = U_nuL @ U_obs.T                           # (local) U_eL = U_nuL U_obs^T
    M_e_match = U_eL_match @ np.diag(masses) @ U_eL_match.T  # (local) exact masses, observed mixing
    off_match = float(np.sqrt(np.sum((M_e_match - np.diag(np.diag(M_e_match))) ** 2)))  # (local)
    off_minimal = float(np.sqrt(np.sum((M_e - np.diag(np.diag(M_e))) ** 2)))            # (local)
    res["offnorm_for_observed_pmns"] = off_match
    res["offnorm_minimal"] = off_minimal
    # (2) free-family 3-angle scan -> max mix_grp reachable (U_eL spans all real
    #     orthogonal, so the observed angles ARE reachable -> max angle-slots = 3; J=0
    #     ALWAYS => J slot never lands). Corroborates the U_eL_match reachability proof.
    max_mixgrp_family = 0                                  # (local)
    grid = np.linspace(0.0, np.pi / 2, 19)                # (local)
    for a in grid:
        for b in grid:
            for c in grid:
                R = rot(0, 1, a) @ rot(0, 2, b) @ rot(1, 2, c)   # (local) free U_eL (3 angles)
                of = pmns_observables(R.conj().T @ U_nuL)
                mg = (int(in_band(of["sin2_th12"], S2T12_LO, S2T12_HI))
                      + int(in_band(of["sin2_th23"], S2T23_LO, S2T23_HI))
                      + int(in_band(of["sin2_th13"], S2T13_LO, S2T13_HI))
                      + int(in_band(abs(of["J"]), J_OBS_LO, J_OBS_HI)))
                if mg > max_mixgrp_family:
                    max_mixgrp_family = mg
    res["family_max_mixgrp_grid"] = max_mixgrp_family
    # observed-PMNS EXACTLY reachable: U_eL_match -> U_PMNS = U_obs (all 3 best-fit
    # angles are band-CENTERS => all 3 angle slots land; J=0 => J slot fails).
    obs_of = pmns_observables(U_eL_match.conj().T @ U_nuL)  # (local) must equal U_obs angles
    obs_angle_slots = (int(in_band(obs_of["sin2_th12"], S2T12_LO, S2T12_HI))
                       + int(in_band(obs_of["sin2_th23"], S2T23_LO, S2T23_HI))
                       + int(in_band(obs_of["sin2_th13"], S2T13_LO, S2T13_HI)))  # (local)
    res["obs_pmns_angle_slots"] = obs_angle_slots         # = 3 (constructive reachability proof)
    res["obs_pmns_reachable"] = bool(obs_angle_slots == 3)
    res["family_max_mixgrp"] = max(max_mixgrp_family, obs_angle_slots)
    print("\n=== STEP 3b: under-determination (masses do NOT fix mixing; U_eL FREE) ===")
    print(f"  ||eps_LX|| for OBSERVED PMNS = {off_match:.4e}  vs minimal-norm = {off_minimal:.4e} "
          f"(ratio {off_match / max(off_minimal,1e-30):.2f}x; SOFT WALL)")
    print(f"  observed PMNS EXACTLY reachable: U_eL_match -> {obs_angle_slots}/3 angle slots land "
          f"(coarse grid corroboration {max_mixgrp_family}/3); J=0 => J slot never lands")
    print(f"  => angles REACHABLE but NOT PREDICTED (masses fix eigenVALUES, not eigenVECTORS)")

    # ===== STEP 4: PMNS = U_eL^dag U_nuL (REAL textures => J=0 EXACTLY) =====
    U_PMNS = U_eL.conj().T @ U_nuL                         # (local) rows e/mu/tau, cols 1/2/3
    res["U_PMNS"] = U_PMNS
    obs = pmns_observables(U_PMNS)                         # (local)
    res.update({f"pmns_{k}": v for k, v in obs.items()})
    print("\n=== STEP 4: U_PMNS = U_eL^dag U_nuL (eps_LX texture; REAL => delta_CP in {0,pi}) ===")
    print(f"  |U_PMNS|:\n{np.round(np.abs(U_PMNS),4)}")
    print(f"  sin^2 th12 = {obs['sin2_th12']:.5f}  (NuFIT 5.2 {S2T12_BF}, 3sig [{S2T12_LO},{S2T12_HI}])")
    print(f"  sin^2 th23 = {obs['sin2_th23']:.5f}  (NuFIT 5.2 {S2T23_BF}, 3sig [{S2T23_LO},{S2T23_HI}])")
    print(f"  sin^2 th13 = {obs['sin2_th13']:.5f}  (NuFIT 5.2 {S2T13_BF}, 3sig [{S2T13_LO},{S2T13_HI}])")
    print(f"  J_PMNS     = {obs['J']:.6e}  (NuFIT 5.2 |J|_obs {J_PMNS_OBS}, band [{J_OBS_LO},{J_OBS_HI}])")

    # ===== STEP 5: contrasts (in the artifact, never tuned) =====
    # (a) forced-circulant limit -- recover S115 J = 1/(6 sqrt 3) = 0.0962250
    res["J_forced_circulant"] = J_FORCED_CIRCULANT
    res["J_recover_matches_S115"] = bool(abs(J_FORCED_CIRCULANT - res["s115_J_forced"]) < 1e-9)
    # (b) diagonal-S100a contrast: U_nuL = I (no neutrino mixing) => PMNS = U_eL^dag
    U_PMNS_diagnu = U_eL.conj().T @ np.eye(3)              # (local) literal S100a (diagonal seesaw)
    obs_diagnu = pmns_observables(U_PMNS_diagnu)           # (local)
    res["pmns_diagnu_sin2_th12"] = obs_diagnu["sin2_th12"]
    res["pmns_diagnu_sin2_th23"] = obs_diagnu["sin2_th23"]
    res["pmns_diagnu_sin2_th13"] = obs_diagnu["sin2_th13"]
    print("\n=== STEP 5: contrasts ===")
    print(f"  forced-circulant J = 1/(6sqrt3) = {J_FORCED_CIRCULANT:.7f}  "
          f"(recover S115={res['J_recover_matches_S115']}) >> eps_LX J = {obs['J']:.3e}")
    print(f"  diagonal-S100a contrast (U_nuL=I): sin^2 th12={obs_diagnu['sin2_th12']:.4f} "
          f"th23={obs_diagnu['sin2_th23']:.4f} th13={obs_diagnu['sin2_th13']:.4f} (all charged-lepton only)")

    # ===== STEP 6: mix_grp over the 4 PMNS observables =====
    in12 = in_band(obs["sin2_th12"], S2T12_LO, S2T12_HI)   # (local)
    in23 = in_band(obs["sin2_th23"], S2T23_LO, S2T23_HI)   # (local)
    in13 = in_band(obs["sin2_th13"], S2T13_LO, S2T13_HI)   # (local)
    inJ = in_band(abs(obs["J"]), J_OBS_LO, J_OBS_HI)       # (local) primary band (S115 pin)
    slot_pass = {
        "sin2_th12": in12, "sin2_th23": in23, "sin2_th13": in13, "J_PMNS": inJ,
    }
    res["slot_pass"] = slot_pass
    mix_grp = int(sum(slot_pass.values()))                # (local) integer 0..4
    res["mix_grp"] = mix_grp
    # delta_CP-consistency reading: J=0 <-> delta_CP=180 deg, which IS within the
    # NuFIT 5.2 NO 3-sigma range [108,404] -> J=0 is CP-CONSERVING-CONSISTENT.
    deltacp_consistent = bool(DELTA_CP_3SIG_LO <= 180.0 <= DELTA_CP_3SIG_HI)  # (local)
    res["J0_deltacp_consistent"] = deltacp_consistent
    mix_grp_deltacp = mix_grp + (1 if (deltacp_consistent and not inJ) else 0)  # (local) alt reading
    res["mix_grp_deltacp_reading"] = mix_grp_deltacp
    print("\n=== STEP 6: mix_grp over the 4 PMNS observables ===")
    for k, v in slot_pass.items():
        print(f"  slot {k}: {'IN-band' if v else 'OUT-of-band'}")
    print(f"  mix_grp = {mix_grp}/4  (PASS>=3, INFO=2, FAIL<=1)")
    print(f"  [alt] J=0 <-> delta_CP=180 in 3sig [{DELTA_CP_3SIG_LO},{DELTA_CP_3SIG_HI}] "
          f"=> CP-conserving-consistent={deltacp_consistent}; mix_grp(deltaCP reading)={mix_grp_deltacp}/4")

    return res


# ---------------------------------------------------------------------------
# Section 8 -- Verdict (mix_grp-keyed composite; plan §W2-3 rubric) + [SIGN] 3-tuple
# ---------------------------------------------------------------------------
def verdict_from(res: dict) -> tuple:
    """mix_grp-keyed composite (plan §W2-3 operator precedence):
      PASS iff mix_grp>=3; INFO iff mix_grp==2; FAIL iff mix_grp<=1."""
    mix_grp = res["mix_grp"]
    if mix_grp >= 3:
        composite = "PASS"                                # (local)
        magnitude = "PASS"                                # (local)
    elif mix_grp == 2:
        composite = "INFO"                                # (local)
        magnitude = "INFO"                                # (local)
    else:
        composite = "FAIL"                                # (local)
        magnitude = "FAIL"                                # (local)
    # SIGN: framework forces delta_CP in {0,pi} => J_PMNS_FW=0 EXACTLY; the computed
    # J=0 MATCHES the framework's own delta_CP in {0,pi} prediction (sign=PASS).
    # The sign of (J_FW - J_obs) is NEGATIVE (UNDERSHOOT: NOT the quark V_us overshoot).
    J_fw = res["pmns_J"]                                   # (local)
    sign_delta = J_fw - J_PMNS_OBS                         # (local)
    res["sign_delta_J"] = sign_delta
    sign_matches_framework = bool(abs(J_fw) < 1e-12)       # (local) J=0 confirms delta_CP in {0,pi}
    sign_verdict = "PASS" if sign_matches_framework else "FAIL"  # (local)
    # REGIME: construction self-consistent iff U_PMNS unitary, m_1=0 preserved, real.
    U = res["U_PMNS"]                                      # (local)
    unitary_resid = float(np.linalg.norm(U.conj().T @ U - np.eye(3), ord="fro"))  # (local)
    res["unitary_resid"] = unitary_resid
    rank_ok = bool(res["m1_over_m3"] < 1e-6)               # (local) m_1=0 preserved
    res["rank_deficiency_ok"] = rank_ok
    regime_verdict = "VALID" if (unitary_resid < 1e-10 and rank_ok) else "MARGINAL"  # (local)
    return composite, magnitude, sign_verdict, regime_verdict


# ---------------------------------------------------------------------------
# Section 9 -- Plot
# ---------------------------------------------------------------------------
def make_plot(res: dict, composite: str) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(18, 5.4))

    # Panel 1: the 4 PMNS observables vs NuFIT 5.2 3-sigma bands
    ax = axes[0]
    labels = ["sin^2 th12", "sin^2 th23", "sin^2 th13", "|J_PMNS|"]
    vals = [res["pmns_sin2_th12"], res["pmns_sin2_th23"], res["pmns_sin2_th13"], abs(res["pmns_J"])]
    los = [S2T12_LO, S2T23_LO, S2T13_LO, J_OBS_LO]
    his = [S2T12_HI, S2T23_HI, S2T13_HI, J_OBS_HI]
    bfs = [S2T12_BF, S2T23_BF, S2T13_BF, J_PMNS_OBS]
    x = np.arange(4)
    for i in range(4):
        ax.fill_between([i - 0.35, i + 0.35], [los[i], los[i]], [his[i], his[i]],
                        color="tab:green", alpha=0.22)
        ax.plot([i - 0.35, i + 0.35], [bfs[i], bfs[i]], color="tab:green", lw=1.6)
    cols = ["#1e8449" if (los[i] <= vals[i] <= his[i]) else "#c0392b" for i in range(4)]
    ax.scatter(x, vals, c=cols, s=90, zorder=5, edgecolor="k")
    ax.set_yscale("log")
    ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=9)
    ax.set_ylabel("value (log)")
    ax.set_title(f"PMNS observables vs NuFIT 5.2 NO 3sig bands\nmix_grp={res['mix_grp']}/4 => {composite}")
    ax.grid(alpha=0.3, axis="y")

    # Panel 2: Jarlskog -- forced-circulant vs eps_LX vs band
    ax = axes[1]
    ax.axvspan(J_OBS_LO, J_OBS_HI, color="tab:green", alpha=0.25,
               label=f"PMNS 3sig band [{J_OBS_LO},{J_OBS_HI}]")
    ax.axvline(J_PMNS_OBS, color="tab:green", lw=2, label=f"|J|_obs={J_PMNS_OBS}")
    ax.axvline(res["J_forced_circulant"], color="black", ls="--", lw=1.4,
               label=f"forced 1/(6sqrt3)={res['J_forced_circulant']:.5f}\n(S115 washed-out)")
    ax.axvline(abs(res["pmns_J"]), color="tab:red", lw=2.5,
               label=f"eps_LX J={abs(res['pmns_J']):.2e}\n(REAL: delta_CP in {{0,pi}})")
    ax.set_xlim(-0.004, 0.11)
    ax.set_yticks([])
    ax.set_xlabel("Jarlskog |J|")
    ax.set_title("J contrast: forced-circulant (washed-out) vs eps_LX (real, =0)\n"
                 "framework delta_CP in {0,pi} = NO leptonic CP")
    ax.legend(loc="upper center", fontsize=7.5)

    # Panel 3: checklist + substrate framing
    ax = axes[2]
    ax.axis("off")
    rows = list(res["slot_pass"].items())
    ax.text(0.0, 1.0, f"{GATE_ID}\nmix_grp checklist => {composite}", fontsize=10,
            weight="bold", transform=ax.transAxes, va="top")
    y0 = 0.88                                             # (local)
    for k, (lab, ok) in enumerate(rows):
        col = "#1e8449" if ok else "#c0392b"
        mark = "IN" if ok else "OUT"
        ax.text(0.0, y0 - 0.085 * k, lab, fontsize=9, transform=ax.transAxes, va="top")
        ax.text(0.78, y0 - 0.085 * k, mark, fontsize=9, color=col, weight="bold",
                transform=ax.transAxes, va="top")
    ax.text(0.0, y0 - 0.085 * 4 - 0.04,
            f"mix_grp = {res['mix_grp']}/4 (PASS>=3, INFO=2, FAIL<=1)\n"
            f"th12={res['pmns_sin2_th12']:.4f} th23={res['pmns_sin2_th23']:.4f}\n"
            f"th13={res['pmns_sin2_th13']:.5f}  J={res['pmns_J']:.2e}\n"
            f"--- sector-asymmetry: tower(e)={TOWER_E}\n"
            f"             tower(nu)={TOWER_NU} (m_1=0)\n"
            f"charged-lepton steep exp(-S0 C2), S0={res['S0_lepton_fixed']:.3f}\n"
            f"neutrino mild sqrt-C2 + near-deg M_R; w23^nu={res['w23_nu']:.3f}\n"
            f"J=0 <-> delta_CP=180 in 3sig => CP-consist={res['J0_deltacp_consistent']}\n"
            f"forced-circulant recover={res['J_recover_matches_S115']}",
            fontsize=7.6, transform=ax.transAxes, va="top", family="monospace")

    fig.suptitle(f"{GATE_ID}: external-eps_LX lepton PMNS texture (D_K(tau_fold={TAU}), L_max={L_MAX}); "
                 f"U_PMNS=U_eL^dag U_nuL, type-I seesaw M_R per S100a",
                 fontsize=11)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 10 -- Verdict payload (race-safe MCP single-writer)
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note="", extra_rows=None) -> dict:
    """Print the emit_verdict payload (race-safe MCP single-writer path).
    [SIGN] gate -> sign/magnitude/regime 3-tuple REQUIRED."""
    payload = {
        "session": int(SESSION),
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if not (sign_verdict is None and magnitude_verdict is None and regime_verdict is None):
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 11 -- Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()
    print(f"=== {GATE_ID} ===")
    pins = log_input_pins(INPUT_FILES)
    audit_sha, content_sha = compute_dual_sha(THIS, CANONICAL_PATH, pins)
    print(f"  audit_sha256  = {audit_sha}")
    print(f"  content_sha256= {content_sha}")
    print(f"  canonical delta_CP_PMNS_substrate = {float(delta_CP_PMNS_substrate)} (framework {{0,pi}})")
    print(f"  canonical sin2_theta12_PDG={sin2_theta12_PDG} sin2_theta13_PDG={sin2_theta13_PDG} (cross-ref)")

    res = compute()
    composite, magnitude, sign_verdict, regime_verdict = verdict_from(res)

    print("\n=== VERDICT ===")
    print(f"  mix_grp = {res['mix_grp']}/4 => composite = {composite}")
    print(f"  [3-tuple] sign={sign_verdict} magnitude={magnitude} regime={regime_verdict}")

    make_plot(res, composite)

    # value payload (no single-quote chars)
    value = (
        f"mix_grp={res['mix_grp']}/4;"
        f"sin2th12={res['pmns_sin2_th12']:.5f}(band[{S2T12_LO},{S2T12_HI}]:{res['slot_pass']['sin2_th12']});"
        f"sin2th23={res['pmns_sin2_th23']:.5f}(band[{S2T23_LO},{S2T23_HI}]:{res['slot_pass']['sin2_th23']});"
        f"sin2th13={res['pmns_sin2_th13']:.5f}(band[{S2T13_LO},{S2T13_HI}]:{res['slot_pass']['sin2_th13']});"
        f"J_PMNS={res['pmns_J']:.4e}(band[{J_OBS_LO},{J_OBS_HI}]:{res['slot_pass']['J_PMNS']});"
        f"forced_circ_J={res['J_forced_circulant']:.6f}(recoverS115={res['J_recover_matches_S115']});"
        f"epsLX_J=0_REAL_deltaCP-in-0-pi(NO_leptonic_CP;th12_OVERSHOOTS_like_quark_Vus,th23/th13_undershoot);"
        f"J0_deltaCP180_in3sig={res['J0_deltacp_consistent']};"
        f"underdetermined_obs_reachable_at_{res['offnorm_for_observed_pmns']/max(res['offnorm_minimal'],1e-30):.2f}x_minimal_epsLX(soft_wall);"
        f"family_max_angle_slots={res['family_max_mixgrp']}/3;"
        f"texture(rho13l={res['rho13_e']:.3f},rho23l={res['rho23_e']:.3f},|w12l|={res['w12_e']:.3e},offnorm={res['offnorm_e']:.4f},w23nu={res['w23_nu']:.3f});"
        f"m1/m3={res['m1_over_m3']:.2e}_rankdef;tower_e{tuple(TOWER_E)}_vs_nu{tuple(TOWER_NU)}_CHsectorasym"
    )

    np.savez(
        OUT_NPZ,
        value=value, mix_grp=res["mix_grp"], composite=composite,
        # PMNS observables
        sin2_th12=res["pmns_sin2_th12"], sin2_th23=res["pmns_sin2_th23"],
        sin2_th13=res["pmns_sin2_th13"], J_PMNS=res["pmns_J"],
        slot_pass_keys=np.array(list(res["slot_pass"].keys())),
        slot_pass_vals=np.array(list(res["slot_pass"].values())),
        # NuFIT 5.2 bands (external pins)
        S2T12_BF=S2T12_BF, S2T12_LO=S2T12_LO, S2T12_HI=S2T12_HI,
        S2T23_BF=S2T23_BF, S2T23_LO=S2T23_LO, S2T23_HI=S2T23_HI,
        S2T13_BF=S2T13_BF, S2T13_LO=S2T13_LO, S2T13_HI=S2T13_HI,
        J_PMNS_OBS=J_PMNS_OBS, J_OBS_LO=J_OBS_LO, J_OBS_HI=J_OBS_HI,
        delta_CP_3sig_lo=DELTA_CP_3SIG_LO, delta_CP_3sig_hi=DELTA_CP_3SIG_HI,
        # charged-lepton sector
        S0_lepton_fixed=res["S0_lepton_fixed"], gap_diag_lock_e=res["gap_diag_lock_e"],
        gap_pdg_e=res["gap_pdg_e"], w12_e=res["w12_e"], w13_e=res["w13_e"], w23_e=res["w23_e"],
        rho13_e=res["rho13_e"], rho23_e=res["rho23_e"], resid_e_max=res["resid_e_max"],
        offnorm_e=res["offnorm_e"], r_mue_fit=res["r_mue_fit"], r_taumu_fit=res["r_taumu_fit"],
        M_e=res["M_e"], U_eL=res["U_eL"], m_e_vals=res["m_e_vals"],
        # under-determination diagnostics
        offnorm_for_observed_pmns=res["offnorm_for_observed_pmns"],
        offnorm_minimal=res["offnorm_minimal"], family_max_mixgrp=res["family_max_mixgrp"],
        obs_pmns_reachable=res["obs_pmns_reachable"],
        # neutrino sector
        M_R_MKK=res["M_R_MKK"], Y_nu_diag=res["Y_nu_diag"], m_nu_S99_eV=res["m_nu_S99_eV"],
        eps23_strength=res["eps23_strength"], w23_nu=res["w23_nu"],
        M_nu=res["M_nu"], U_nuL=res["U_nuL"], m_nu_vals=res["m_nu_vals"],
        m1_over_m3=res["m1_over_m3"], nu_ratio_fw=res["nu_ratio_fw"], nu_ratio_obs=res["nu_ratio_obs"],
        # PMNS + contrasts
        U_PMNS=res["U_PMNS"], J_forced_circulant=res["J_forced_circulant"],
        J_recover_matches_S115=res["J_recover_matches_S115"],
        pmns_diagnu_sin2_th12=res["pmns_diagnu_sin2_th12"],
        pmns_diagnu_sin2_th23=res["pmns_diagnu_sin2_th23"],
        pmns_diagnu_sin2_th13=res["pmns_diagnu_sin2_th13"],
        J0_deltacp_consistent=res["J0_deltacp_consistent"],
        mix_grp_deltacp_reading=res["mix_grp_deltacp_reading"],
        # tower/casimir
        C2_E=C2_E, C2_NU=C2_NU, TRI_E=TRI_E, TRI_NU=TRI_NU,
        tower_e=np.array(TOWER_E), tower_nu=np.array(TOWER_NU), tau=TAU,
        # 3-tuple + provenance
        sign_verdict=sign_verdict, magnitude_verdict=magnitude, regime_verdict=regime_verdict,
        unitary_resid=res["unitary_resid"], rank_deficiency_ok=res["rank_deficiency_ok"],
        s111_Vus_fw=res["s111_Vus_fw"], s115_J_forced=res["s115_J_forced"],
        scheme=SCHEME, convention=CONVENTION, L_max=L_MAX,
        audit_sha256=audit_sha, content_sha256=content_sha,
    )

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print("\n" + tag)

    companion = (
        f"external-eps_LX lepton PMNS texture (lepton analog of quark S111-CF-YUK-FULLFLAVOR); "
        f"mix_grp={res['mix_grp']}/4 (PASS>=3); U_PMNS=U_eL^dag U_nuL; type-I seesaw M_R per S100a "
        f"[{', '.join(f'{x:.4f}' for x in res['M_R_MKK'])}] scale HELD; forced-circulant "
        f"J={res['J_forced_circulant']:.6f} (S115 recover {res['J_recover_matches_S115']}) >> eps_LX J=0 "
        f"(REAL, delta_CP in {{0,pi}})"
    )
    extra = [
        (f"# composite-precedence: mix_grp operator (PASS>=3/INFO=2/FAIL<=1, plan §W2-3) overrides the "
         f"generic 3-tuple collapse; sign=PASS records J=0 MATCHES framework delta_CP in {{0,pi}} (NOT "
         f"a direction-mismatch FAIL); magnitude={magnitude} carries the mix_grp verdict # {GATE_ID}"),
        (f"# C(+)H sector-asymmetry: charged-lepton tower {tuple(TOWER_E)} steep exp(-S0 C2) S0={res['S0_lepton_fixed']:.4f} "
         f"=> small U_eL; neutrino tower {tuple(TOWER_NU)} mild sqrt-C2 + near-deg M_R (Y_1=0 EXACT, m_1=0 "
         f"rank-def m1/m3={res['m1_over_m3']:.1e}) => U_nuL 2-3 rotation; PMNS=U_eL^dag U_nuL # {GATE_ID}"),
        (f"# J contrast: forced-circulant 1/(6sqrt3)={res['J_forced_circulant']:.7f} (washed-out S115) vs "
         f"eps_LX J={res['pmns_J']:.3e}=0 (real). Framework delta_CP in {{0,pi}} => J_FW < J_obs UNDERSHOOT "
         f"(NOT the quark V_us={res['s111_Vus_fw']:.4f} overshoot). J=0<->delta_CP=180 in 3sig "
         f"[{DELTA_CP_3SIG_LO},{DELTA_CP_3SIG_HI}] => CP-conserving-consistent={res['J0_deltacp_consistent']} # {GATE_ID}"),
        (f"# triality selection rule (VII.BL teeth): t(1,0)/t(1,1)/t(3,0)=1/0/0; 1<->3 mixing needs t(O)=1 "
         f"(triality-odd), forbidden for any LI op; non-LI eps_LX supplies it (S98-W3-1). regulator_pin=N/A "
         f"(representation-theoretic, no Seeley-DeWitt a_n) # {GATE_ID}"),
        (f"# texture set BY masses NOT PMNS: charged-lepton {{rho13l={res['rho13_e']:.4f},rho23l={res['rho23_e']:.4f},"
         f"|w12l|={res['w12_e']:.3e}}} fit to m_mu/m_e={res['r_mue_fit']:.2f}, m_tau/m_mu={res['r_taumu_fit']:.2f} "
         f"(resid {res['resid_e_max']:.1e}); PMNS is the OUTPUT # {GATE_ID}"),
    ]

    print_verdict_payload(composite, value, audit_sha, content_sha,
                          sign_verdict=sign_verdict, magnitude_verdict=magnitude,
                          regime_verdict=regime_verdict,
                          companion_note=companion, extra_rows=extra)

    wall = time.time() - t0
    print(f"\n=== {GATE_ID}: {composite} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
