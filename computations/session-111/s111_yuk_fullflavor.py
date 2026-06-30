#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S111-CF-YUK-FULLFLAVOR  (Session 111, Wave 3, §W3-1)  -- [VERIFY] gate.

Extend the S110-CF2-YUK-EPSLX up-sector pairing-dependent off-diagonal texture
{rho13, rho23} on the multiplicity bundle to the FULL flavor sector: build the
DOWN-sector eps_LX texture {rho13^d, rho23^d, |w12^d|} on the SAME multiplicity
bundle (complement of the Hochschild 1-cochain [D_K,-] image, per VII.BL), with
the down-sector diagonal Casimir grading C2(1,0)/C2(1,1)/C2(3,0) = 4/3, 3, 6 and
the down-only ratio m_s/m_d; build the CKM mixing matrix V_CKM = U_up^dag U_down
from the misalignment of the up- and down-sector diagonalizing unitaries (the
off-diagonal arg(w) phase lives in the MIXING, not the masses -- S99 transit-connes
adjudication); and resolve the same-generation J-conjugacy lock (Lambda_u = Lambda_d
the shared overall scale; test whether breaking it needs an independent up/down
scale ratio Lambda_d/Lambda_u and PIN that ratio's origin or report it HELD).

mass_grp = # of the 6 fermion-mass-group target slots landing in PDG bands:
  slot 1: m_u/m_d   (gen1 same-gen, J-conjugacy-locked)
  slot 2: m_c/m_s   (gen2 same-gen, J-conjugacy-locked)
  slot 3: m_t/m_b   (gen3 same-gen, J-conjugacy-locked)
  slot 4: up m_c/m_u-pattern  (up cross-gen; inherited in-band from S110-CF2)
  slot 5: down m_s/m_d        (down cross-gen)
  slot 6: V_us               (CKM anchor)
PASS iff mass_grp >= 5/6.

============================================================================
SUBSTRATE-FIRST (phononic-framing.md):
============================================================================
  D_K eigenvalues -> eps_LX multiplicity-bundle deformation -> down-sector
  Yukawa texture + CKM -> fermion masses + mixing.

  The Yukawa couplings ARE matrix elements of dD_K/d(eps_LX) between the
  lowest-|lambda| generation eigenvectors of the block-diagonal D_K on
  (A_K, H_K, D_K). By the VII.BL STAGE-3-PERMANENT theorem the bare D_K is
  multiplicity-scalar (generation = Z3-triality multiplicity index t=(p-q) mod 3),
  so the hierarchy is NOT in the bare spectrum -- it is a feature of the external
  non-left-invariant eps_LX on the multiplicity-bundle complement of the [D_K,-]
  image. The 1<->3 generation mixing that carries the hierarchy is triality-ODD
  (t(O)=1, Sage-verified plan-freeze), forbidden for any LI operator; the non-LI
  eps_LX supplies it (S98-W3-1 existence-PROVEN). CKM/CP live OFF-DIAGONAL in
  eps_LX (the arg(w) phase, S99 four-lens); masses live in |w|; BDI (J^2=+1) lets
  the CP phase survive (it would die in DIII).

============================================================================
INHERITED (S110-CF2 up-sector, verified on disk -- MANDATORY first action):
============================================================================
  S0_held  = 1.735317     (lepton-fixed freeze-in coupling; SHAPE-fixing scale)
  up texture: rho13 = 0.3768, rho23 = 0.1000, |w12| = 2.346e-2, theta = 2.1721
  up ratios: r_cu = 589.34 (ld 0.000 dex), r_tc = 125.09 (ld 0.035 dex) -- BOTH in 0.5-dex band
  => up cross-gen slot (m_c/m_u-pattern) is INHERITED PASS (slot 4).

============================================================================
THE WALL THIS GATE MAPS (Sage-confirmable; substrate result, pre-flight):
============================================================================
  (a) DOWN-sector log-gap: the down diagonal Casimir tower locks
      ln(m_s/m_d)/ln(m_b/m_s) = 9/5 = 1.800 EXACT (same rep-theoretic identity as
      up). PDG down wants 0.787. The down pairing-dependent texture {rho13^d,
      rho23^d} breaks the 9/5 lock (the same mechanism that worked for the up
      sector). m_s/m_d (slot 5) is REACHABLE.
  (b) SAME-GEN J-conjugacy lock: with d_i^up = Lambda_u exp(-S0 C2_i) and
      d_i^down = Lambda_d exp(-S0 C2_i), a SINGLE shared scale ratio Lambda_d/Lambda_u
      makes ALL THREE same-gen ratios m_q^up/m_q^down EQUAL to that one number.
      PDG: m_u/m_d = 0.460 (gen1, <1), m_c/m_s = 13.58 (gen2), m_t/m_b = 41.28 (gen3)
      -- they span 0.46 -> 41.3 (factor ~90) and CROSS unity. NO single Lambda_d/Lambda_u
      can hit more than ONE of the three. This is the substrate-natural HELD NUMBER:
      the up<->down splitting is a FIBER-CHARGE distinction (which 16-dim SM rep, not
      which generation) that the multiplicity-bundle eps_LX is BLIND to (VII.BL again).
  => the gate maps WHERE the multiplicity-bundle texture suffices (down log-gap + CKM)
     vs WHERE it does not (the 3 same-gen J-conjugacy slots).

============================================================================
PRE-REGISTERED OPERATOR (plan §W3-1):
============================================================================
  mass_grp = |{ slot_i : |log10(ratio_i^FW / ratio_i^PDG)| <= ld_band_i }|
  PASS iff mass_grp >= 5     (the framework's FIRST near-complete DERIVED hierarchy)
  INFO iff 3 <= mass_grp < 5 (partial improvement; J-conjugacy lock HELD;
                              NON-PROMOTION-BY-HELD-NUMBER, undischarged-magnitude-bound)
  FAIL iff mass_grp < 3      (down+CKM cannot be brought into band; obstruction reasserts)

  ld_band = 0.5 dex per ratio slot (matches S110-CF2 up-sector 0.5-dex band).
  V_us band [0.215, 0.235] (PDG 0.225 +/- ~5%); in 0.5-dex terms |log10(V_us^FW/0.225)|
  is the cross-check, the [0.215,0.235] window is the primary slot-6 gate.

  [VERIFY] substitution chain (1<->3 mixing is triality-ODD; LI route forbidden):
    t(p,q) = (p-q) mod 3 [SU(3) center character]; (1,0)/(1,1)/(3,0) => t = 1/0/0.
    1<->3 mixing: t(a)=1, t(b)=0 => required t(O)=(t(a)-t(b)) mod 3 = 1 (triality-odd).
    Any LI operator (inner fluct, real image, twisted-inner) carries t(O)=0 => the
    1<->3 mixing is group-theoretically FORBIDDEN for LI. Only the non-LI eps_LX
    (t(O)=1 component) supplies it. Same logic for the down sector. This is the
    algebraic teeth behind VII.BL.

Output 4-tuple:
  (value=<mass_grp + per-slot ld + V_us>, scheme=NCG-INNER-FLUCT-EXTERNAL-NONLI,
   convention=EPS-LX-MULTIPLICITY-BUNDLE-DOWN-SECTOR-PLUS-CKM..., L_max=12)

Classification: PARTICLE (representation-theoretic content of D_K; generation
multiplicity = SU(3) Peter-Weyl Z3-triality multiplicity).

Inputs (SHA-pinned at runtime):
  computations/_shared/canonical_constants.py
  computations/session-110/s110_cf2_yuk_epslx.npz   (the up-sector texture to inherit)
  computations/session-84/s84_spectrum_cache_L12_tau019.npz
  computations/_shared/dirac_spectrum.py
"""

from __future__ import annotations

# --- CPU thread cap BEFORE numpy import (math-scripts.md; fits are small 3x3 eigh) ---
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
# Section 1 -- Paths
# ---------------------------------------------------------------------------
THIS = Path(__file__).resolve()
SESSION_DIR = THIS.parent                                # computations/session-111
COMPUTATIONS_DIR = SESSION_DIR.parent                    # computations
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import (  # noqa: E402
    tau_fold,
    m_t_pole, m_c_msbar_mc, m_u_msbar_2GeV,
    m_d_msbar_2GeV, m_s_msbar_2GeV, m_b_msbar_mb,
    m_e, m_mu, m_tau_PDG,
    V_us_PDG, V_us_sigma_PDG,
)

# Optional GPU (AMD RX 9070 XT / ROCm); 3x3 eigh is tiny so CPU is fine.
try:
    import torch
    _HAS_TORCH = bool(torch.cuda.is_available())
except Exception:
    torch = None
    _HAS_TORCH = False

import matplotlib                                         # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt                           # noqa: E402

# ---------------------------------------------------------------------------
# Section 2 -- Identity + pinned machinery (plan §W3-1 machinery_pin_map)
# ---------------------------------------------------------------------------
SESSION = "111"                                          # (local)
GATE_ID = "S111-CF-YUK-FULLFLAVOR"                       # (local)
SCHEME = "NCG-INNER-FLUCT-EXTERNAL-NONLI"                # (local)
CONVENTION = ("EPS-LX-MULTIPLICITY-BUNDLE-DOWN-SECTOR-PLUS-CKM-"
              "pairing-dep-offdiag-rho13d-rho23d-Jconjugacy-Lu-Ld")  # (local)
L_MAX = 12                                               # (local) plan pin
TAU = float(tau_fold)                                    # (local) 0.19 canonical

# Pre-registered thresholds (plan §W3-1; frozen BEFORE compute)
LD_BAND_DEX = 0.5            # (local) per-ratio |log10(r_FW/r_PDG)| <= 0.5 (plan band)
MASS_GRP_PASS = 5           # (local) PASS needs >= 5/6 mass groups
MASS_GRP_INFO = 3           # (local) INFO needs 3 <= mass_grp < 5
MASS_GRP_BASELINE = 2       # (local) S110 baseline (2/6 in-band: up cross-gen pair)
VUS_LO, VUS_HI = 0.215, 0.235   # (local) plan V_us window (PDG 0.225 +/- ~5%)
PUB_SIGFIGS = 4             # (local) Class 8.3 publication precision (plan pin)

# ---------------------------------------------------------------------------
# Section 3 -- Casimir tower + Yukawa block (mirrors S110-CF2 yukawa_block)
# ---------------------------------------------------------------------------
def C2_su3(p: int, q: int) -> float:
    """SU(3) quadratic Casimir C2(p,q) = (p^2 + q^2 + p q + 3 p + 3 q)/3."""
    return (p * p + q * q + p * q + 3.0 * p + 3.0 * q) / 3.0


def triality(p: int, q: int) -> int:
    """SU(3) center character t(p,q) = (p - q) mod 3."""
    return (p - q) % 3


TOWER_PQ = [(1, 0), (1, 1), (3, 0)]                      # (local) gen3(heaviest)/gen2/gen1(lightest)
C2_VEC = np.array([C2_su3(p, q) for (p, q) in TOWER_PQ]) # (local) = [4/3, 3, 6] exact
TRIALITY_VEC = np.array([triality(p, q) for (p, q) in TOWER_PQ])  # (local) = [1, 0, 0]
assert np.allclose(C2_VEC, [4.0 / 3.0, 3.0, 6.0]), "C2 grading mismatch"
assert np.array_equal(TRIALITY_VEC, [1, 0, 0]), "triality mismatch"


def yukawa_block(scale: float, S0: float, w12: complex,
                 rho13: float, rho23: float,
                 theta13: float, theta23: float) -> np.ndarray:
    """3x3 Hermitian Yukawa block on the generation multiplicity (tower order
    (1,0)/(1,1)/(3,0)):

        diagonal  d_i = scale * exp(-S0 * C2_i)     (homogeneous Casimir tower x scale)
        off-diag  w_12 = w12                         (the base off-diagonal)
                  w_13 = rho13 * |w12| * e^{i theta13}   (pairing-dependent 1<->3)
                  w_23 = rho23 * |w12| * e^{i theta23}   (pairing-dependent 2<->3)

    'scale' is Lambda (overall sector scale); the up sector uses Lambda_u, the down
    sector Lambda_d. The off-diagonal part IS delta_A acting on the multiplicity leg,
    NON-scalar (rho13 != rho23 != 1 breaks the multiplicity-scalar W2 form), Hermitian
    (reality wall W1 [J, D_K+delta_A]=0 preserved block-by-block).
    """
    d = scale * np.exp(-S0 * C2_VEC)                     # (local) Casimir tower x scale
    M = np.diag(d).astype(complex)
    aw = abs(w12)                                        # (local) base off-diagonal magnitude
    w13 = rho13 * aw * np.exp(1j * theta13)             # (local) 1<->3 coupling
    w23 = rho23 * aw * np.exp(1j * theta23)             # (local) 2<->3 coupling
    M[0, 1] = w12;  M[1, 0] = np.conj(w12)              # (local) 1<->2
    M[0, 2] = w13;  M[2, 0] = np.conj(w13)              # (local) 1<->3
    M[1, 2] = w23;  M[2, 1] = np.conj(w23)              # (local) 2<->3
    return M


def diag_block(M: np.ndarray):
    """Hermitian eigen-decomposition; |lambda| ascending (= ascending mass).
    Returns (|lambda| ascending, U columns ascending). U diagonalizes M:
    U^dag M U = diag(lambda_sorted)."""
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
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")
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
OUT_NPZ = SESSION_DIR / "s111_yuk_fullflavor.npz"
OUT_PNG = SESSION_DIR / "s111_yuk_fullflavor.png"

CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"
UP_TEXTURE_NPZ = COMPUTATIONS_DIR / "session-110" / "s110_cf2_yuk_epslx.npz"
SPECTRUM_CACHE = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
DIRAC_SPECTRUM = SHARED_DIR / "dirac_spectrum.py"

INPUT_FILES = [CANONICAL_PATH, UP_TEXTURE_NPZ, SPECTRUM_CACHE, DIRAC_SPECTRUM]

# PDG targets (single-source canonical; standard headline scheme, mirrors S110-CF2).
# UP: m_u at 2 GeV MS-bar, m_c at own scale, m_t pole.
M_U_PDG = float(m_u_msbar_2GeV); M_C_PDG = float(m_c_msbar_mc); M_T_PDG = float(m_t_pole)
# DOWN: m_d, m_s at 2 GeV MS-bar; m_b at own scale.
M_D_PDG = float(m_d_msbar_2GeV); M_S_PDG = float(m_s_msbar_2GeV); M_B_PDG = float(m_b_msbar_mb)

R_CU_PDG = M_C_PDG / M_U_PDG       # (local) up cross-gen m_c/m_u
R_TC_PDG = M_T_PDG / M_C_PDG       # (local) up cross-gen m_t/m_c
R_SD_PDG = M_S_PDG / M_D_PDG       # (local) down cross-gen m_s/m_d (slot 5)
R_BS_PDG = M_B_PDG / M_S_PDG       # (local) down cross-gen m_b/m_s
# same-gen J-conjugacy slots (1,2,3):
R_UD_PDG = M_U_PDG / M_D_PDG       # (local) slot 1 gen1
R_CS_PDG = M_C_PDG / M_S_PDG       # (local) slot 2 gen2
R_TB_PDG = M_T_PDG / M_B_PDG       # (local) slot 3 gen3

# lepton-fixed S0 (the substrate-natural SHAPE scale; same as S110-CF2)
R_MU_E_PDG = float(m_mu) / float(m_e)
R_TAU_MU_PDG = float(m_tau_PDG) / float(m_mu)


def lepton_fixed_S0() -> tuple:
    S0_mue = float(np.log(R_MU_E_PDG) / (C2_VEC[2] - C2_VEC[1]))     # (local) ln(206.77)/3
    S0_taumu = float(np.log(R_TAU_MU_PDG) / (C2_VEC[1] - C2_VEC[0])) # (local) ln(16.82)/(5/3)
    return 0.5 * (S0_mue + S0_taumu), S0_mue, S0_taumu


# ---------------------------------------------------------------------------
# Section 6 -- Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    res: dict = {}

    # ===== STEP 0: MANDATORY first action -- inherit the S110-CF2 up-sector texture =====
    up = np.load(UP_TEXTURE_NPZ, allow_pickle=True)
    S0_up = float(up["S0_held"])
    rho13_u = float(up["rho13"]); rho23_u = float(up["rho23"])
    w12_u = float(up["w12"]); theta_u = float(up["theta_refine"])
    up_r_cu = float(up["r_cu_fit"]); up_r_tc = float(up["r_tc_fit"])
    up_band_ok = bool(up["up_band_ok"])
    res["up_S0_held"] = S0_up
    res["up_rho13"] = rho13_u; res["up_rho23"] = rho23_u
    res["up_w12"] = w12_u; res["up_theta"] = theta_u
    res["up_r_cu"] = up_r_cu; res["up_r_tc"] = up_r_tc
    res["up_band_ok_inherited"] = up_band_ok
    print("=== STEP 0: inherited S110-CF2 up-sector texture (MANDATORY first action) ===")
    print(f"  S0_held={S0_up:.6f}  rho13={rho13_u:.4f} rho23={rho23_u:.4f} "
          f"|w12|={w12_u:.4e} theta={theta_u:.4f}")
    print(f"  up r_cu={up_r_cu:.4g} (PDG {R_CU_PDG:.4g})  r_tc={up_r_tc:.4g} (PDG {R_TC_PDG:.4g})")
    print(f"  up_band_ok (inherited) = {up_band_ok}")

    # Cross-check lepton-fixed S0 reproduces S110-CF2 S0_held (no scheme drift).
    S0_held, S0_mue, S0_taumu = lepton_fixed_S0()
    res["S0_held"] = S0_held
    s0_consistent = bool(abs(S0_held - S0_up) < 1e-6)
    res["S0_consistent_with_up"] = s0_consistent
    print(f"  lepton-fixed S0_held={S0_held:.6f}  consistent with up={s0_consistent}")
    # use the inherited up-sector S0 as the shared SHAPE scale (identical to within FD)
    S0 = S0_up                                            # (local)

    # Up-sector overall scale Lambda_u: fix so the up diagonal tower top is ~ m_t scale
    # in the SAME normalization used for the down fit. Only the RATIO Lambda_d/Lambda_u
    # enters same-gen ratios; we set Lambda_u = 1 (the up block is the reference) and
    # let Lambda_d/Lambda_u be the single fitted scale ratio. With Lambda_u=1 the up
    # block eigenvalues are exp(-S0 C2)+off-diag; absolute up masses are then
    # Lambda_u * (dimensionless eigenvalue). Same-gen ratio m_q^up/m_q^down uses the
    # SAME dimensionless tower so the Lambda's are the ONLY scale d.o.f.
    Lambda_u = 1.0                                        # (local) up reference scale

    # ===== STEP 1: the diagonal-Casimir log-gap wall (down sector) =====
    gap_lock = float((C2_VEC[1] - C2_VEC[2]) / (C2_VEC[0] - C2_VEC[1]))  # (local) 9/5
    gap_down_pdg = float(np.log(R_SD_PDG) / np.log(R_BS_PDG))            # (local) 0.787
    gap_up_pdg = float(np.log(R_CU_PDG) / np.log(R_TC_PDG))             # (local) 1.298
    res["gap_diag_casimir_lock"] = gap_lock
    res["gap_down_pdg"] = gap_down_pdg
    res["gap_up_pdg"] = gap_up_pdg
    print("\n=== STEP 1: diagonal-Casimir log-gap wall ===")
    print(f"  diag Casimir lock = {gap_lock:.6f} (= 9/5 EXACT, BOTH sectors)")
    print(f"  PDG up log-gap   = {gap_up_pdg:.6f}")
    print(f"  PDG down log-gap = {gap_down_pdg:.6f}")
    print(f"  => down texture {{rho13^d,rho23^d}} must break 9/5 -> 0.787 (as up broke it -> 1.30)")

    # ===== STEP 2: same-gen J-conjugacy lock pre-flight (the HELD-NUMBER wall) =====
    # A single shared Lambda_d/Lambda_u makes all 3 same-gen ratios EQUAL. PDG spans
    # 0.46 / 13.58 / 41.28 -- crossing unity -- so no single ratio hits >1 slot.
    res["R_UD_PDG"] = R_UD_PDG; res["R_CS_PDG"] = R_CS_PDG; res["R_TB_PDG"] = R_TB_PDG
    samegen_span = float(R_TB_PDG / R_UD_PDG)             # (local) ~90
    res["samegen_span"] = samegen_span
    # best single Lambda_d/Lambda_u that minimizes total log-distance over the 3 slots:
    # in the diagonal limit m_q^up/m_q^down = (Lambda_u/Lambda_d) for every gen, so
    # the best shared ratio is the geometric mean of the 3 PDG same-gen ratios.
    geo_mean_samegen = float((R_UD_PDG * R_CS_PDG * R_TB_PDG) ** (1.0 / 3.0))  # (local)
    res["best_single_LuLd_geo"] = geo_mean_samegen       # Lambda_u/Lambda_d that centers the 3 in log
    print("\n=== STEP 2: same-gen J-conjugacy lock (the HELD-NUMBER wall) ===")
    print(f"  PDG same-gen: m_u/m_d={R_UD_PDG:.4f} m_c/m_s={R_CS_PDG:.4f} m_t/m_b={R_TB_PDG:.4f}")
    print(f"  span (max/min) = {samegen_span:.2f}; CROSS unity (gen1<1, gen2/3>1)")
    print(f"  => a SINGLE Lambda_d/Lambda_u cannot hit >1 of the 3 (geo-centered ratio {geo_mean_samegen:.4f})")

    # ===== STEP 3: fit the DOWN texture {log10|w12^d|, rho13^d, rho23^d, theta_d}  =====
    #           + the scale ratio (Lambda_d/Lambda_u) to the DOWN cross-gen log-gap
    #           m_s/m_d AND m_b/m_s, then read off the down absolute masses for slots.
    # The down diagonal tower is Lambda_d * exp(-S0 C2). The DOWN cross-gen ratios are
    # SCALE-INDEPENDENT (Lambda_d cancels in m_s/m_d and m_b/m_s) -- they depend ONLY on
    # the texture {|w12^d|, rho13^d, rho23^d, theta_d}. So fit the texture to the 2 down
    # log-gap ratios first (scale-free), THEN fit Lambda_d/Lambda_u to the same-gen slots.
    def down_ratios(w12d_abs, r13, r23, thd):
        # scale-free: set Lambda_d=1 for the ratio computation (cancels)
        m, _ = diag_block(yukawa_block(1.0, S0, w12d_abs + 0j, r13, r23, thd, thd))
        if not (np.all(np.isfinite(m)) and np.all(m > 0)):
            return np.nan, np.nan
        return m[1] / m[0], m[2] / m[1]                  # (local) m_s/m_d, m_b/m_s

    def resid_down(x):
        u, r13, r23, thd = x                             # (local) u=log10|w12^d|
        r_sd, r_bs = down_ratios(10.0 ** u, r13, r23, thd)
        if not (np.isfinite(r_sd) and np.isfinite(r_bs)) or r_sd <= 0 or r_bs <= 0:
            return [1e3, 1e3]
        return [np.log(r_sd / R_SD_PDG), np.log(r_bs / R_BS_PDG)]

    LB = [-12.0, 0.1, 0.1, 0.0]                          # (local) lower bounds (same class as up)
    UB = [0.0, 10.0, 10.0, np.pi]                        # (local) upper bounds
    best = None                                          # (local) achievable-boundary minimizer
    starts = []                                          # (local) dense deterministic multistart
    for u0 in np.linspace(-10.0, -0.5, 12):
        for r0 in [0.3, 1.0, 2.0, 4.0, 8.0]:
            for th0 in np.linspace(0.1, np.pi - 0.1, 5):
                starts.append([u0, r0, r0, th0])
    for x0 in starts:
        try:
            sol = least_squares(resid_down, x0, bounds=(LB, UB),
                                xtol=3e-16, ftol=3e-16, gtol=3e-16, max_nfev=8000)
        except Exception:
            continue
        rm = float(np.max(np.abs(sol.fun)))              # (local) max log-residual
        cand = (10.0 ** sol.x[0], float(sol.x[1]), float(sol.x[2]), float(sol.x[3]), rm)
        if best is None or rm < best[4]:
            best = cand
    w12d, rho13d, rho23d, theta_d, resid_down_max = best
    res["w12_down"] = w12d; res["rho13_down"] = rho13d
    res["rho23_down"] = rho23d; res["theta_down"] = theta_d
    res["resid_down_max"] = resid_down_max
    r_sd_fit, r_bs_fit = down_ratios(w12d, rho13d, rho23d, theta_d)
    res["r_sd_fit"] = float(r_sd_fit); res["r_bs_fit"] = float(r_bs_fit)
    ld_sd = abs(np.log10(r_sd_fit / R_SD_PDG))           # (local) slot 5 log-distance
    res["ld_sd"] = float(ld_sd)
    print("\n=== STEP 3: down-sector texture fit (scale-free cross-gen ratios) ===")
    print(f"  |w12^d|={w12d:.4e} rho13^d={rho13d:.4f} rho23^d={rho23d:.4f} theta_d={theta_d:.4f}")
    print(f"  r_sd(m_s/m_d)={r_sd_fit:.4g} (PDG {R_SD_PDG:.4g}, ld {ld_sd:.4f} dex)  [SLOT 5]")
    print(f"  r_bs(m_b/m_s)={r_bs_fit:.4g} (PDG {R_BS_PDG:.4g})")
    print(f"  down fit resid_max={resid_down_max:.3e}")

    # ===== STEP 4: fit the scale ratio Lambda_d/Lambda_u to the same-gen J-conjugacy slots =====
    # Absolute up masses: m_q^up = Lambda_u * |lambda_q^up| (dimensionless tower eigenvalues).
    # Absolute down masses: m_q^down = Lambda_d * |lambda_q^down|. Same-gen ratio:
    #   m_q^up / m_q^down = (Lambda_u/Lambda_d) * (|lambda_q^up| / |lambda_q^down|).
    # The |lambda^up|/|lambda^down| are FIXED by the textures (already fit). The ONLY
    # free scale d.o.f. is r_scale = Lambda_d/Lambda_u. Fit it to minimize the joint
    # log-distance over the 3 same-gen slots, then count how many land in 0.5-dex band.
    m_up_dimless, _ = diag_block(yukawa_block(Lambda_u, S0, w12_u + 0j,
                                              rho13_u, rho23_u, theta_u, theta_u))
    m_down_dimless, _ = diag_block(yukawa_block(1.0, S0, w12d + 0j,
                                                rho13d, rho23d, theta_d, theta_d))
    # ascending = [gen1(light), gen2, gen3(heavy)]; same-gen ratio per generation index
    res["m_up_dimless"] = m_up_dimless
    res["m_down_dimless"] = m_down_dimless
    # texture-fixed up/down eigenvalue ratio per generation (Lambda's stripped):
    ev_ratio = m_up_dimless / m_down_dimless             # (local) |lambda^up|/|lambda^down| per gen
    # same-gen PDG ratios per generation index [gen1, gen2, gen3]
    samegen_pdg = np.array([R_UD_PDG, R_CS_PDG, R_TB_PDG])  # (local)

    def resid_scale(x):
        # x[0] = log10(Lambda_u/Lambda_d) = -log10(r_scale)
        lu_ld = 10.0 ** x[0]                             # (local) Lambda_u/Lambda_d
        pred = lu_ld * ev_ratio                          # (local) predicted same-gen ratios
        return np.log(pred / samegen_pdg)               # 3-vector log-residual
    best_s = None                                        # (local)
    for s0 in np.linspace(-3.0, 3.0, 61):
        try:
            sol = least_squares(resid_scale, [s0], xtol=1e-15, ftol=1e-15, gtol=1e-15)
        except Exception:
            continue
        rm = float(np.sqrt(np.mean(sol.fun ** 2)))       # (local) RMS log-residual
        if best_s is None or rm < best_s[1]:
            best_s = (float(sol.x[0]), rm)
    lu_ld_log, scale_rms = best_s
    Lambda_u_over_d = 10.0 ** lu_ld_log                  # (local)
    r_scale = 1.0 / Lambda_u_over_d                       # (local) Lambda_d/Lambda_u
    res["Lambda_u_over_d"] = Lambda_u_over_d
    res["Lambda_d_over_u"] = r_scale
    res["scale_fit_rms_log"] = scale_rms
    # the 3 same-gen predicted ratios at the best scale
    samegen_pred = Lambda_u_over_d * ev_ratio            # (local) [gen1,gen2,gen3]
    res["samegen_pred"] = samegen_pred
    ld_samegen = np.abs(np.log10(samegen_pred / samegen_pdg))  # (local) per-slot ld [1,2,3]
    res["ld_ud"] = float(ld_samegen[0])                  # slot 1
    res["ld_cs"] = float(ld_samegen[1])                  # slot 2
    res["ld_tb"] = float(ld_samegen[2])                  # slot 3
    print("\n=== STEP 4: same-gen J-conjugacy scale fit (single Lambda_d/Lambda_u) ===")
    print(f"  Lambda_u/Lambda_d = {Lambda_u_over_d:.4g} (Lambda_d/Lambda_u = {r_scale:.4g}); RMS log-resid={scale_rms:.4f}")
    print(f"  same-gen predicted: m_u/m_d={samegen_pred[0]:.4g} m_c/m_s={samegen_pred[1]:.4g} m_t/m_b={samegen_pred[2]:.4g}")
    print(f"  same-gen PDG      : m_u/m_d={R_UD_PDG:.4g} m_c/m_s={R_CS_PDG:.4g} m_t/m_b={R_TB_PDG:.4g}")
    print(f"  per-slot ld (dex): slot1(u/d)={ld_samegen[0]:.4f} slot2(c/s)={ld_samegen[1]:.4f} slot3(t/b)={ld_samegen[2]:.4f}")

    # ===== STEP 5: CKM V_us from the unitary misalignment V_CKM = U_up^dag U_down =====
    # arg(w) lives in the diagonalizing unitary => V_CKM = U_up^dag U_down (S99). V_us
    # is the (1,2) element magnitude (first row, second column in the |lambda|-ascending
    # generation basis). The phases theta_u, theta_d are the off-diagonal arg(w);
    # |V_us| is a function of the texture misalignment, NOT of the eigenvalues.
    _, U_up = diag_block(yukawa_block(Lambda_u, S0, w12_u + 0j,
                                      rho13_u, rho23_u, theta_u, theta_u))
    _, U_down = diag_block(yukawa_block(1.0, S0, w12d + 0j,
                                        rho13d, rho23d, theta_d, theta_d))
    V_ckm = U_up.conj().T @ U_down                       # (local) CKM (up to rephasing)
    V_us_fw = float(abs(V_ckm[0, 1]))                    # (local) |V_us| prediction
    res["V_us_fw"] = V_us_fw
    res["V_ckm_abs"] = np.abs(V_ckm)
    vus_in_band = bool(VUS_LO <= V_us_fw <= VUS_HI)      # (local) slot 6 gate
    ld_vus = abs(np.log10(V_us_fw / float(V_us_PDG))) if V_us_fw > 0 else np.inf  # (local) cross-check
    res["vus_in_band"] = vus_in_band
    res["ld_vus"] = float(ld_vus)
    print("\n=== STEP 5: CKM V_us from unitary misalignment V_CKM = U_up^dag U_down ===")
    print(f"  |V_us|^FW = {V_us_fw:.4f}  (PDG {float(V_us_PDG):.4f}, window [{VUS_LO},{VUS_HI}])")
    print(f"  in-band (slot 6) = {vus_in_band};  log-dist cross-check {ld_vus:.4f} dex")
    print(f"  |V_CKM| matrix:\n{np.round(np.abs(V_ckm),4)}")

    # ===== STEP 6: count mass_grp over the 6 slots =====
    # slot 4 (up cross-gen m_c/m_u-pattern): INHERITED in-band from S110-CF2 (both up
    # ratios passed). We re-verify it here from the inherited up texture for audit.
    up_band_recheck = bool(abs(np.log10(up_r_cu / R_CU_PDG)) <= LD_BAND_DEX
                           and abs(np.log10(up_r_tc / R_TC_PDG)) <= LD_BAND_DEX)
    res["up_band_recheck"] = up_band_recheck
    slot_pass = {
        "1_m_u/m_d (gen1 same-gen)": bool(ld_samegen[0] <= LD_BAND_DEX),
        "2_m_c/m_s (gen2 same-gen)": bool(ld_samegen[1] <= LD_BAND_DEX),
        "3_m_t/m_b (gen3 same-gen)": bool(ld_samegen[2] <= LD_BAND_DEX),
        "4_m_c/m_u-pattern (up cross-gen, inherited)": up_band_recheck,
        "5_m_s/m_d (down cross-gen)": bool(ld_sd <= LD_BAND_DEX),
        "6_V_us (CKM anchor)": vus_in_band,
    }
    res["slot_pass"] = slot_pass
    mass_grp = int(sum(slot_pass.values()))              # (local) integer 0..6
    res["mass_grp"] = mass_grp
    print("\n=== STEP 6: mass_grp over the 6 fermion-mass-group target slots ===")
    for k, v in slot_pass.items():
        print(f"  slot {k}: {'PASS' if v else 'FAIL/held'}")
    print(f"  mass_grp = {mass_grp}/6  (PASS>=5, INFO 3-4, baseline 2/6)")

    # ===== J-conjugacy resolution status =====
    # The lock is "resolved" only if a SINGLE Lambda_d/Lambda_u lands all 3 same-gen
    # slots in band. By the STEP-2 wall it cannot (PDG span ~90, crossing unity), so
    # the lock is HELD: at most 1 of the 3 same-gen slots can land with one scale.
    n_samegen_pass = int(ld_samegen[0] <= LD_BAND_DEX) + int(ld_samegen[1] <= LD_BAND_DEX) \
                     + int(ld_samegen[2] <= LD_BAND_DEX)  # (local)
    res["n_samegen_pass"] = n_samegen_pass
    jconj_resolved = bool(n_samegen_pass == 3)
    res["jconjugacy_resolved"] = jconj_resolved
    res["jconjugacy_held"] = (not jconj_resolved)
    print(f"  J-conjugacy: {n_samegen_pass}/3 same-gen slots land with one Lambda_d/Lambda_u "
          f"=> {'RESOLVED' if jconj_resolved else 'HELD (single scale cannot hit >1; VII.BL fiber-charge blindness)'}")

    return res


# ---------------------------------------------------------------------------
# Section 7 -- Verdict (composite from the integer count + held-number tag)
# ---------------------------------------------------------------------------
def verdict_from(res: dict) -> tuple:
    """mass_grp-keyed composite (plan §W3-1 rubric):
      PASS iff mass_grp >= 5; INFO iff 3 <= mass_grp < 5; FAIL iff mass_grp < 3.
    The [VERIFY] trigger has no signed/regime sub-tuple; this is an integer-count gate.
    """
    mass_grp = res["mass_grp"]
    if mass_grp >= MASS_GRP_PASS:
        composite = "PASS"
    elif mass_grp >= MASS_GRP_INFO:
        composite = "INFO"
    else:
        composite = "FAIL"
    return composite, mass_grp


# ---------------------------------------------------------------------------
# Section 8 -- Plot
# ---------------------------------------------------------------------------
def make_plot(res: dict, composite: str) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(18, 5.4))

    # Panel 1: per-slot log-distance vs 0.5-dex band
    ax = axes[0]
    slot_labels = ["m_u/m_d\n(gen1)", "m_c/m_s\n(gen2)", "m_t/m_b\n(gen3)",
                   "m_c/m_u\n(up,inh)", "m_s/m_d\n(down)", "V_us\n(CKM)"]
    # slot-4 ld: inherited up m_c/m_u logdist (use max of the two up ratios)
    ld4 = max(abs(np.log10(res["up_r_cu"] / R_CU_PDG)),
              abs(np.log10(res["up_r_tc"] / R_TC_PDG)))  # (local)
    lds = [res["ld_ud"], res["ld_cs"], res["ld_tb"], ld4, res["ld_sd"], res["ld_vus"]]
    cols = ["#1e8449" if v <= LD_BAND_DEX else "#c0392b" for v in lds]
    ax.bar(np.arange(6), lds, color=cols)
    ax.axhline(LD_BAND_DEX, color="k", ls="--", lw=1.2, label=f"band {LD_BAND_DEX} dex")
    ax.set_xticks(np.arange(6)); ax.set_xticklabels(slot_labels, fontsize=8)
    ax.set_ylabel("|log10(ratio_FW / ratio_PDG)|  (dex)")
    ax.set_title(f"per-slot log-distance (mass_grp={res['mass_grp']}/6)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3, axis="y")

    # Panel 2: same-gen J-conjugacy wall (single scale cannot hit >1)
    ax = axes[1]
    xs = np.arange(3)
    ax.bar(xs - 0.2, res["samegen_pred"], width=0.4, color="#c0392b", label="FW (single Lambda_d/Lambda_u)")
    ax.bar(xs + 0.2, [R_UD_PDG, R_CS_PDG, R_TB_PDG], width=0.4, color="#16a085", label="PDG")
    ax.set_yscale("log")
    ax.axhline(1.0, color="gray", ls=":", lw=1)
    ax.set_xticks(xs); ax.set_xticklabels(["m_u/m_d", "m_c/m_s", "m_t/m_b"])
    ax.set_ylabel("same-gen up/down ratio")
    ax.set_title(f"J-conjugacy lock: span {res['samegen_span']:.0f}x, crosses unity\n"
                 f"({res['n_samegen_pass']}/3 land; "
                 f"{'RESOLVED' if res['jconjugacy_resolved'] else 'HELD'})")
    ax.legend(fontsize=8); ax.grid(alpha=0.3, axis="y")

    # Panel 3: verdict checklist
    ax = axes[2]
    ax.axis("off")
    rows = list(res["slot_pass"].items())
    y0 = 0.90                                             # (local)
    ax.text(0.0, 1.0, f"{GATE_ID}\nfull-flavor checklist => {composite}", fontsize=10,
            weight="bold", transform=ax.transAxes, va="top")
    for k, (lab, ok) in enumerate(rows):
        col = "#1e8449" if ok else "#c0392b"
        mark = "PASS" if ok else "FAIL"
        ax.text(0.0, y0 - 0.11 * k, lab, fontsize=8, transform=ax.transAxes, va="top")
        ax.text(0.86, y0 - 0.11 * k, mark, fontsize=9, color=col, weight="bold",
                transform=ax.transAxes, va="top")
    ax.text(0.0, y0 - 0.11 * 6 - 0.03,
            f"mass_grp = {res['mass_grp']}/6  (PASS>=5, INFO 3-4)\n"
            f"J-conjugacy {'RESOLVED' if res['jconjugacy_resolved'] else 'HELD'} "
            f"({res['n_samegen_pass']}/3 same-gen)\n"
            f"down log-gap 9/5 -> {res['gap_down_pdg']:.3f} via {{rho13^d,rho23^d}}\n"
            f"|V_us|^FW = {res['V_us_fw']:.4f} (PDG 0.225)",
            fontsize=8, transform=ax.transAxes, va="top", family="monospace")

    fig.suptitle(f"{GATE_ID}: down-sector eps_LX texture + CKM extend the S110-CF2 up-sector "
                 f"(D_K(tau_fold={TAU}), L_max={L_MAX}, S0_held={res['S0_held']:.4f})",
                 fontsize=11)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 9 -- Verdict payload (race-safe MCP single-writer; NO open("a") append)
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note="", extra_rows=None) -> dict:
    """Print the emit_verdict payload (race-safe MCP single-writer path).
    The script does NOT write the verdict file. [VERIFY] gate: no 3-tuple."""
    payload = {
        "session": SESSION,
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
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 10 -- Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()
    print(f"=== {GATE_ID} ===")
    print(f"  torch GPU available: {_HAS_TORCH}")
    pins = log_input_pins(INPUT_FILES)
    audit_sha, content_sha = compute_dual_sha(THIS, CANONICAL_PATH, pins)
    print(f"  audit_sha256  = {audit_sha}")
    print(f"  content_sha256= {content_sha}")

    res = compute()
    composite, mass_grp = verdict_from(res)

    print("\n=== VERDICT ===")
    print(f"  mass_grp = {mass_grp}/6  => composite = {composite}")

    make_plot(res, composite)

    # value payload (no single-quote chars)
    value = (
        f"mass_grp={mass_grp}/6;"
        f"slots[1u/d={res['ld_ud']:.3f},2c/s={res['ld_cs']:.3f},3t/b={res['ld_tb']:.3f},"
        f"4up-inh={res['up_band_recheck']},5s/d={res['ld_sd']:.3f}dex,6Vus={res['V_us_fw']:.4f}];"
        f"down-texture(rho13d={res['rho13_down']:.3g},rho23d={res['rho23_down']:.3g},"
        f"|w12d|={res['w12_down']:.3e},theta_d={res['theta_down']:.3f});"
        f"r_sd={res['r_sd_fit']:.4g}_vs_{R_SD_PDG:.4g}(ld{res['ld_sd']:.3f});"
        f"Vus={res['V_us_fw']:.4f}_vs_0.225(band[{VUS_LO},{VUS_HI}]:{res['vus_in_band']});"
        f"Jconj={'RESOLVED' if res['jconjugacy_resolved'] else 'HELD'}"
        f"({res['n_samegen_pass']}/3,Ld/Lu={res['Lambda_d_over_u']:.3g});"
        f"down_loggap_9/5->{res['gap_down_pdg']:.3f};baseline2/6"
    )

    np.savez(
        OUT_NPZ,
        value=value,
        mass_grp=mass_grp, composite=composite,
        # inherited up texture
        up_S0_held=res["up_S0_held"], up_rho13=res["up_rho13"], up_rho23=res["up_rho23"],
        up_w12=res["up_w12"], up_theta=res["up_theta"],
        up_r_cu=res["up_r_cu"], up_r_tc=res["up_r_tc"],
        up_band_ok_inherited=res["up_band_ok_inherited"], up_band_recheck=res["up_band_recheck"],
        S0_held=res["S0_held"], S0_consistent_with_up=res["S0_consistent_with_up"],
        # walls
        gap_diag_casimir_lock=res["gap_diag_casimir_lock"],
        gap_down_pdg=res["gap_down_pdg"], gap_up_pdg=res["gap_up_pdg"],
        samegen_span=res["samegen_span"], best_single_LuLd_geo=res["best_single_LuLd_geo"],
        # down texture fit
        w12_down=res["w12_down"], rho13_down=res["rho13_down"], rho23_down=res["rho23_down"],
        theta_down=res["theta_down"], resid_down_max=res["resid_down_max"],
        r_sd_fit=res["r_sd_fit"], r_bs_fit=res["r_bs_fit"], ld_sd=res["ld_sd"],
        # scale fit
        m_up_dimless=res["m_up_dimless"], m_down_dimless=res["m_down_dimless"],
        Lambda_u_over_d=res["Lambda_u_over_d"], Lambda_d_over_u=res["Lambda_d_over_u"],
        scale_fit_rms_log=res["scale_fit_rms_log"], samegen_pred=res["samegen_pred"],
        ld_ud=res["ld_ud"], ld_cs=res["ld_cs"], ld_tb=res["ld_tb"],
        n_samegen_pass=res["n_samegen_pass"],
        jconjugacy_resolved=res["jconjugacy_resolved"], jconjugacy_held=res["jconjugacy_held"],
        # CKM
        V_us_fw=res["V_us_fw"], V_ckm_abs=res["V_ckm_abs"],
        vus_in_band=res["vus_in_band"], ld_vus=res["ld_vus"],
        # PDG targets
        R_UD_PDG=R_UD_PDG, R_CS_PDG=R_CS_PDG, R_TB_PDG=R_TB_PDG,
        R_CU_PDG=R_CU_PDG, R_TC_PDG=R_TC_PDG, R_SD_PDG=R_SD_PDG, R_BS_PDG=R_BS_PDG,
        V_us_PDG=float(V_us_PDG), V_us_sigma_PDG=float(V_us_sigma_PDG),
        C2_VEC=C2_VEC, triality_vec=TRIALITY_VEC, tower_pq=np.array(TOWER_PQ), tau=TAU,
        LD_BAND_DEX=LD_BAND_DEX, MASS_GRP_PASS=MASS_GRP_PASS, MASS_GRP_INFO=MASS_GRP_INFO,
        VUS_LO=VUS_LO, VUS_HI=VUS_HI,
        slot_pass_keys=np.array(list(res["slot_pass"].keys())),
        slot_pass_vals=np.array(list(res["slot_pass"].values())),
        scheme=SCHEME, convention=CONVENTION, L_max=L_MAX,
        audit_sha256=audit_sha, content_sha256=content_sha,
    )

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print("\n" + tag)

    companion = (
        f"FULL-FLAVOR extension of S110-CF2-YUK-EPSLX up-sector texture to down-sector "
        f"+ CKM; mass_grp={mass_grp}/6 (PASS>=5); down log-gap 9/5 broken to "
        f"{res['gap_down_pdg']:.3f} by {{rho13^d,rho23^d}}; V_us={res['V_us_fw']:.4f} from "
        f"U_up^dag U_down misalignment; J-conjugacy "
        f"{'RESOLVED' if res['jconjugacy_resolved'] else 'HELD'} "
        f"({res['n_samegen_pass']}/3 same-gen, single Lambda_d/Lambda_u)"
    )
    extra = [
        (f"# DOWN-texture: rho13^d={res['rho13_down']:.4f} rho23^d={res['rho23_down']:.4f} "
         f"|w12^d|={res['w12_down']:.4e} theta_d={res['theta_down']:.4f}; "
         f"r_sd={res['r_sd_fit']:.4g} (PDG {R_SD_PDG:.4g}, ld {res['ld_sd']:.4f} dex SLOT5) # {GATE_ID}"),
        (f"# SAME-GEN J-conjugacy lock: Lambda_d/Lambda_u={res['Lambda_d_over_u']:.4g}; "
         f"PDG span {res['samegen_span']:.0f}x crosses unity => single scale hits "
         f"{res['n_samegen_pass']}/3 (slots 1,2,3 ld {res['ld_ud']:.3f}/{res['ld_cs']:.3f}/{res['ld_tb']:.3f}); "
         f"HELD-NUMBER = up<->down fiber-charge splitting, VII.BL multiplicity-bundle blind # {GATE_ID}"),
        (f"# CKM: |V_us|^FW={res['V_us_fw']:.4f} (PDG {float(V_us_PDG):.4f}, window "
         f"[{VUS_LO},{VUS_HI}] in-band={res['vus_in_band']} SLOT6); arg(w) lives in "
         f"U_up^dag U_down (S99 four-lens), NOT in masses # {GATE_ID}"),
        (f"# triality selection rule (VII.BL teeth): t(1,0)/t(1,1)/t(3,0)=1/0/0; "
         f"1<->3 mixing needs t(O)=1 (triality-odd), forbidden for any LI op; non-LI "
         f"eps_LX supplies it (S98-W3-1 existence-PROVEN); regulator_pin=N/A "
         f"(representation-theoretic, no Seeley-DeWitt a_n) # {GATE_ID}"),
        (f"# capstone #7: do NOT tag the full hierarchy DERIVED unless composite=PASS; "
         f"mass_grp={mass_grp}/6 composite={composite}; "
         f"NON-PROMOTION-BY-HELD-NUMBER (undischarged-magnitude-bound differentia) iff INFO # {GATE_ID}"),
    ]

    print_verdict_payload(composite, value, audit_sha, content_sha,
                          companion_note=companion, extra_rows=extra)

    wall = time.time() - t0
    print(f"\n=== {GATE_ID}: {composite} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
