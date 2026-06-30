#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CF-S117-UEL-FLAT-DIRECTION  (Session 117, Wave 2, §W2-5)  -- [VERIFY] gate.

DOES THE SPECTRAL ACTION S = Tr f(D_K/Lambda) DEPEND ON THE LEPTON FLAVOR
ROTATION U_eL?  Binary flat-vs-lifted test.

  flat   (ΔS/S_total <= eps_flat)  => U_eL is a FREE direction => under-determination
                                      CONFIRMED (the SA does NOT single out the mixing).
  lifted (ΔS/S_total >  eps_flat)  => U_eL substrate-SELECTED (the §VII.BL eps_LX
                                      texture coupling makes S U_eL-dependent).

WHAT THIS GATE DOES
-------------------
The s116 lepton texture (s116_lepton_pmns_texture.npz) builds the charged-lepton
mass matrix as a REAL-SYMMETRIC Yukawa M_e = U_eL diag(m_e_vals) U_eL^T, where U_eL
is DERIVED by diagonalizing M_e (M_e = diag(exp(-S0 C2_E)) + eps_LX off-diagonal).
The under-determination corollary (S116-W2-PMNS-RESCUE): at FIXED charged-lepton
masses {m_e_vals}, U_eL is FREE -- M_e(R) = R diag(m_e_vals) R^T reproduces the masses
for ANY R in SO(3).  This gate asks whether the SPECTRAL ACTION (not just the masses)
selects a particular R = U_eL.

  PRIMARY (canonical, the substrate-faithful finite spectral triple):
     The finite lepton Dirac operator is the chirality-off-diagonal
       D_F(R) = [[0, M_e(R)], [M_e(R)^dag, 0]]   (6x6, real-symmetric).
     Then D_F^2 = diag(M_e M_e^dag, M_e^dag M_e), so EVERY spectral functional
       S = Tr f(D_F^2/Lambda^2) = 2 Σ_i f(m_i^2/Lambda^2)
     is a function of the SINGULAR VALUES (masses) m_i ONLY.  Under the U_eL orbit
     at fixed masses, the spectrum {±m_i} is INVARIANT (trace cyclicity), so ΔS = 0
     EXACTLY -- for cutoff f*, for zeta S_zeta = a_4, AND for the anomaly-derived
     action.  This flatness is FUNCTIONAL-INDEPENDENT.

  LIFT-CANDIDATE PROBE (scheme/construction-dependent alternative):
     The ONLY way S becomes U_eL-dependent is a CROSS TERM with a FIXED non-scalar
     reference G in the flavor basis:  H(R) = s_geom * diag(sqrt(C2_E)) + M_e(R).
     a_2 = Tr(H^2) then carries 2 Tr(G M_e(R)), R-dependent.  We scan s_geom (the
     bare-grading / Yukawa relative scale) and show the lift DECAYS as 1/s_geom and
     is BELOW eps_flat at the PHYSICAL scale s_geom ~ M_KK/m_tau ~ 4e16 -- AND it
     requires a non-scalar bare grading, which contradicts the §VII.BL
     multiplicity-SCALAR theorem (G ∝ I on the generation triple => cross term
     collapses to an invariant => flat).  So the lift is a non-physical O(1)-rescale
     artifact, not substrate physics.

SPECTRAL-FUNCTIONAL SENSITIVITY (lizzi deliverable)
---------------------------------------------------
  Reported in THREE functionals (regulator_pin a_n^{zeta} canonical; cutoff f*
  cross-check; the a_2 Einstein-Hilbert moment):
    a_0 = Tr(1)        : U_eL-INDEPENDENT exactly (mode count); ABSENT in zeta scheme.
    a_2 = Tr(D_F^2)    : function of masses only => FLAT.
    a_4 = Tr(D_F^4)    : function of masses only => FLAT == S_zeta (the zeta action).
    S_cutoff (f*)      : Σ f*(λ^2/Λ^2) => FLAT.
  FLAT-vs-LIFTED binary: FUNCTIONAL-INDEPENDENT (flat in cutoff AND zeta).
  Lift MAGNITUDE / SA-min U_eL: SCHEME-DEPENDENT (lift-probe; physical-scale-suppressed).

PRE-REGISTERED OPERATOR (plan sessions/session-plan/session-117-plan-w2.md §W2-5):
  operator: inequality   ΔS(U_eL orbit)/S_total  <= eps_flat (flat)  vs  > eps_flat (lifted)
  strict_PASS_boundary: eps_flat = 1e-6 ; direction "<=" (PASS = flat).
  Labels map the solution space, NOT merit: a LIFTED result would be framework-
  FAVORABLE (mixing substrate-SELECTED); a FLAT result confirms under-determination.

[VERIFY] substitution chain (plan §W2-5):
  Def 1: S = Tr f(D_K/Λ) depends ONLY on the eigenvalues {λ_k} of D_K.
  Def 2: U_eL acting as conjugation D_K -> U_eL D_K U_eL^dag leaves {λ_k} INVARIANT.
  Substitute: S(U_eL D_K U_eL^dag) = Tr(U_eL f(D_K/Λ) U_eL^dag) = Tr f(D_K/Λ) = S
              => ΔS = 0 EXACTLY for spectrum-preserving U_eL (trace cyclicity).
  Lift candidate: the §VII.BL dD_K/d(eps_LX) texture could introduce U_eL via a
              coupling to a FIXED external basis (non-conjugation) => ΔS ≠ 0.
  Direction: PASS (flat) iff ΔS/S_total <= eps_flat; FAIL (lifted) iff > eps_flat.

============================================================================
SUBSTRATE-FIRST (phononic-framing.md) -- GEOMETRIC:
============================================================================
  The spectral action S = Tr f(D_K/Λ) IS a functional of D_K's spectrum -- the
  fabric's action energy.  Trace cyclicity makes S invariant under any
  spectrum-preserving conjugation, so a FLAT result is the DEFAULT: the substrate
  supplies the lepton mass spectrum (the M_R ruler) but NOT the U_eL mixing seed.
  Direction of explanation: D_K spectrum -> spectral action -> (does NOT select) U_eL
  -> PMNS under-determined.  A lift would require the bare D_K to be non-scalar on the
  generation triple at a scale comparable to the Yukawa -- contra the §VII.BL
  multiplicity-scalar theorem and 1e-17-suppressed at the physical M_KK scale.

Output 4-tuple:
  (value=<flat/lifted + ΔS/S per functional + lift-probe physical-scale>,
   scheme=spectral-action-Uel-orbit-variation, convention=ABSOLUTE, L_max=10)

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  computations/_shared/canonical_constants.py
  computations/session-116/s116_lepton_pmns_texture.npz
"""

from __future__ import annotations

# --- CPU thread cap BEFORE numpy import (math-scripts.md; 3x3/6x6 eig is tiny;
#     GPU path N/A per plan pin "torch.linalg if block >= 100x100; else numpy") ---
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# Section 1 -- Paths + canonical constants (MANDATORY import)
# ---------------------------------------------------------------------------
THIS = Path(__file__).resolve()
SESSION_DIR = THIS.parent                                 # computations/session-117
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
SESSION_DIR.mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import (  # noqa: E402
    tau_fold,
    M_KK,
    v_ew,
    m_e, m_mu, m_tau_PDG,
    t_star,                       # f*(x) = (1-t*) sqrt(x) + t* exp(-x); t*=0.08832
    mellin_f_star_f0, mellin_f_star_f2, mellin_f_star_f4,  # Mellin moments of f*
    f_0_sharp,                    # sharp-cutoff f_0 = 1.0 (anomaly/sharp cross-check)
)

import matplotlib                                          # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt                            # noqa: E402

# ---------------------------------------------------------------------------
# Section 2 -- Identity + pinned machinery (plan §W2-5 machinery_pin_map)
# ---------------------------------------------------------------------------
SESSION = "117"                                            # (local)
GATE_ID = "CF-S117-UEL-FLAT-DIRECTION"                     # (local)
SCHEME = "spectral-action-Uel-orbit-variation"            # (local) plan pin
CONVENTION = "ABSOLUTE-Uel-orbit-fixed-Me-masses-zeta-an"  # (local) ABSOLUTE; a_n^{zeta} regulator
L_MAX = 10                                                 # (local) plan pin
EPS_FLAT = 1.0e-6                                          # (local) plan §W2-5 strict_PASS_boundary
TAU = float(tau_fold)                                      # (local) 0.19 canonical
PUB_SIGFIGS = 6                                            # (local) Class-8.3 publication precision

# f* cutoff function coefficients (regulator-pin: a_n^{zeta} canonical; f* cross-check)
A_SQRT = 1.0 - float(t_star)                               # (local) ~0.91168 (sqrt branch weight)
A_EXP = float(t_star)                                      # (local) 0.08832 (exp branch weight)

# ---------------------------------------------------------------------------
# Section 3 -- SHA-256 dual-SHA block (S84+ schema; pattern from s116)
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
# Section 4 -- Paths/targets + inputs
# ---------------------------------------------------------------------------
OUT_NPZ = SESSION_DIR / "s117_uel_flat_direction.npz"
OUT_PNG = SESSION_DIR / "s117_uel_flat_direction.png"

CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"
S116_TEXTURE = COMPUTATIONS_DIR / "session-116" / "s116_lepton_pmns_texture.npz"
INPUT_FILES = [CANONICAL_PATH, S116_TEXTURE]


# ---------------------------------------------------------------------------
# Section 5 -- SO(3) rotation + finite-Dirac / moment helpers
# ---------------------------------------------------------------------------
def givens(i: int, j: int, th: float, n: int = 3) -> np.ndarray:
    R = np.eye(n)
    c, s = np.cos(th), np.sin(th)
    R[i, i] = c; R[j, j] = c; R[i, j] = -s; R[j, i] = s
    return R


def U_of(a: float, b: float, c: float) -> np.ndarray:
    """Real SO(3) rotation from 3 Givens angles (spans SO(3) as (a,b,c) range [0,pi))."""
    return givens(0, 1, a) @ givens(0, 2, b) @ givens(1, 2, c)


def dirac_finite(M_e: np.ndarray) -> np.ndarray:
    """Chirality-off-diagonal finite lepton Dirac operator D_F=[[0,M_e],[M_e^dag,0]]
    (6x6, real-symmetric); eigenvalues are {+/- m_i} (m_i = singular values of M_e)."""
    n = M_e.shape[0]
    Z = np.zeros((n, n))
    return np.block([[Z, M_e], [M_e.conj().T, Z]])


def sdw_moments(D: np.ndarray) -> tuple:
    """Seeley-DeWitt analog moments of a finite Dirac op D:
       a0 = Tr(1) = dim (mode count; ABSENT in zeta scheme)
       a2 = Tr(D^2)   (Einstein-Hilbert / kinetic analog)
       a4 = Tr(D^4)   (Yang-Mills+Higgs quartic analog == zeta action S_zeta = a_4)"""
    D2 = D @ D
    a0 = float(D.shape[0])                                 # (local)
    a2 = float(np.trace(D2).real)                          # (local)
    a4 = float(np.trace(D2 @ D2).real)                     # (local)
    return a0, a2, a4


def s_cutoff(D: np.ndarray, Lam: float) -> float:
    """Cutoff spectral action S = Σ_k f*(λ_k^2/Λ^2), f*(x)=(1-t*)sqrt(x)+t* exp(-x)."""
    lam = np.linalg.eigvalsh(D)
    x = (lam / Lam) ** 2                                   # (local)
    return float(np.sum(A_SQRT * np.sqrt(x) + A_EXP * np.exp(-x)))


def s_sharp(D: np.ndarray, Lam: float) -> float:
    """Sharp-cutoff cross-check S = #{|λ| <= Λ}*f_0_sharp (anomaly-axis sanity)."""
    lam = np.linalg.eigvalsh(D)
    return float(f_0_sharp * np.sum(np.abs(lam) <= Lam))


# ---------------------------------------------------------------------------
# Section 6 -- Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    res: dict = {}

    # ===== STEP 0: load s116 texture (substrate-fixed masses + sector grading) =====
    s116 = np.load(S116_TEXTURE, allow_pickle=True)
    m_e_vals = np.asarray(s116["m_e_vals"]).ravel().astype(float)   # (local) [3.19e-5,6.60e-3,0.111]
    C2_E = np.asarray(s116["C2_E"]).ravel().astype(float)           # (local) [6,3,4/3]
    U_eL_s116 = np.asarray(s116["U_eL"]).astype(float)              # (local) the s116 diagonalizer
    M_e_s116 = np.asarray(s116["M_e"]).astype(float)                # (local) the s116 texture
    res["m_e_vals"] = m_e_vals
    res["C2_E"] = C2_E
    res["U_eL_s116"] = U_eL_s116
    # consistency: M_e_s116 must diagonalize to m_e_vals (the under-determination base point)
    ev = np.sort(np.abs(np.linalg.eigvalsh(M_e_s116)))             # (local)
    res["m_e_recon_resid"] = float(np.max(np.abs(ev - np.sort(m_e_vals))))
    print("=== STEP 0: s116 lepton texture (substrate-fixed inputs) ===")
    print(f"  m_e_vals (masses, dimensionless Yukawa) = {m_e_vals}")
    print(f"  C2_E (bare sector Casimir grading)      = {C2_E}  (sqrt = {np.sqrt(C2_E)})")
    print(f"  M_e->eigval recon resid                 = {res['m_e_recon_resid']:.3e} (==0 => masses match)")

    diag_m = np.diag(m_e_vals)                              # (local) the fixed mass spectrum
    G = np.diag(np.sqrt(C2_E))                              # (local) fixed bare sector grading (flavor basis)

    # ===== STEP 1: U_eL ORBIT SCAN -- PRIMARY (finite Dirac = Yukawa only) =====
    # D_F(R) = [[0, M_e(R)],[M_e(R),0]], M_e(R)=R diag(m_e_vals) R^T; masses FIXED, R free.
    # The cutoff Λ is the natural dimensionless scale (max bare grading); ΔS/S is the
    # tested quantity and the flatness is Λ-independent (function of masses only).
    Lam = float(np.sqrt(C2_E.max()))                       # (local) natural cutoff ~ sqrt(6)=2.449

    # structured Euler grid (8^3=512) PLUS a 50-point 1-param fine scan (>= N_eval pin 50)
    ng = 8                                                  # (local)
    grid = np.linspace(0.0, np.pi, ng, endpoint=False)     # (local) [0,pi)
    fine = np.linspace(0.0, np.pi, 50, endpoint=False)     # (local) >=50 angles (plan pin)

    def scan_operator(build_op):
        """Scan the U_eL orbit; return arrays of (a0,a2,a4,S_cutoff) over all R samples."""
        a0s, a2s, a4s, scs = [], [], [], []
        # broad 3-angle Euler grid
        for a in grid:
            for b in grid:
                for c in grid:
                    R = U_of(a, b, c)
                    D = build_op(R)
                    m0, m2, m4 = sdw_moments(D)
                    a0s.append(m0); a2s.append(m2); a4s.append(m4)
                    scs.append(s_cutoff(D, Lam))
        # fine 1-param scan (vary first angle; >=50 points)
        for a in fine:
            R = U_of(a, 0.31, 1.07)
            D = build_op(R)
            m0, m2, m4 = sdw_moments(D)
            a0s.append(m0); a2s.append(m2); a4s.append(m4)
            scs.append(s_cutoff(D, Lam))
        return (np.array(a0s), np.array(a2s), np.array(a4s), np.array(scs))

    def rel_spread(x):
        x = np.asarray(x, float)
        denom = abs(float(np.mean(x)))
        if denom < 1e-300:
            return 0.0
        return float((x.max() - x.min()) / denom)          # (local) ΔS/S_total

    # PRIMARY: finite Dirac = Yukawa only (M_e(R))
    primA0, primA2, primA4, primSC = scan_operator(lambda R: dirac_finite(R @ diag_m @ R.T))
    res["N_eval"] = int(primA2.size)
    dS_a0 = rel_spread(primA0)                              # (local) == 0 (mode count)
    dS_a2 = rel_spread(primA2)                              # (local)
    dS_a4 = rel_spread(primA4)                              # (local) == zeta action spread
    dS_cut = rel_spread(primSC)                             # (local) cutoff f* spread
    res["dS_a0_over_S"] = dS_a0
    res["dS_a2_over_S"] = dS_a2
    res["dS_a4_over_S_ZETA"] = dS_a4
    res["dS_cutoff_over_S"] = dS_cut
    res["S_zeta_value"] = float(np.mean(primA4))            # (local) a_4 (zeta action)
    res["S_cutoff_value"] = float(np.mean(primSC))
    print("\n=== STEP 1: PRIMARY U_eL-orbit scan (finite Dirac = Yukawa only) ===")
    print(f"  N_eval = {res['N_eval']} U_eL orbit samples (>=50 pin)")
    print(f"  a_0=Tr(1)  ΔS/S = {dS_a0:.3e}  (mode count; ABSENT in zeta scheme)")
    print(f"  a_2=Tr(D^2) ΔS/S = {dS_a2:.3e}  (Einstein-Hilbert moment)")
    print(f"  a_4=Tr(D^4) ΔS/S = {dS_a4:.3e}  == S_zeta (zeta action; CANONICAL verdict)")
    print(f"  S_cutoff(f*) ΔS/S = {dS_cut:.3e}  (cutoff cross-check functional)")
    print(f"  => all <= eps_flat={EPS_FLAT:.0e}? "
          f"{all(v <= EPS_FLAT for v in (dS_a2, dS_a4, dS_cut))}  (FLAT: trace cyclicity)")

    # ===== STEP 2: CONTROL -- pure conjugation of the FIXED s116 D_F =====
    # If U_eL conjugates the WHOLE operator, ΔS = 0 EXACTLY (verifies code + trace
    # cyclicity).  R D_F R^T (R acts on the full 6x6 via flavor-block conjugation).
    DF0 = dirac_finite(M_e_s116)                            # (local) the fixed s116 Dirac op
    conj_a4 = []
    for a in fine:
        R3 = U_of(a, 0.7, 1.9)
        Rfull = np.block([[R3, np.zeros((3, 3))], [np.zeros((3, 3)), R3]])  # (local) chirality-block
        Dc = Rfull @ DF0 @ Rfull.T
        conj_a4.append(sdw_moments(Dc)[2])
    res["control_conj_a4_spread"] = rel_spread(conj_a4)
    print("\n=== STEP 2: CONTROL -- pure conjugation R D_F R^T (trace-cyclicity check) ===")
    print(f"  a_4 ΔS/S under full conjugation = {res['control_conj_a4_spread']:.3e} "
          f"(== machine eps => trace cyclicity verified)")

    # ===== STEP 3: LIFT-CANDIDATE PROBE (scheme/construction-dependent alternative) =====
    # H(R) = s_geom * G + M_e(R), G = diag(sqrt(C2_E)) FIXED in flavor basis.
    # The U_eL-dependent lift enters via the cross term Tr(G M_e(R)).  Scan s_geom
    # (bare-grading / Yukawa relative scale) and locate the eps_flat crossing; mark the
    # PHYSICAL scale s_geom ~ M_KK/m_tau (where the bare KK grading dominates).
    s_geoms = np.logspace(-2, 18, 80)                      # (local) scale knob, incl. physical
    probe_a2, probe_a4, probe_cut = [], [], []
    for sg in s_geoms:
        Gs = sg * G                                        # (local) scaled fixed grading
        a2v, a4v, cutv = [], [], []
        for a in fine:                                     # 50-pt 1-param U_eL orbit (sufficient for spread)
            R = U_of(a, 0.31, 1.07)
            H = Gs + R @ diag_m @ R.T                       # (local) 3x3 Hermitian probe op
            _, m2, m4 = sdw_moments(H)
            a2v.append(m2); a4v.append(m4)
            cutv.append(s_cutoff(H, max(Lam, sg * np.sqrt(C2_E.max()))))
        probe_a2.append(rel_spread(a2v))
        probe_a4.append(rel_spread(a4v))
        probe_cut.append(rel_spread(cutv))
    probe_a2 = np.array(probe_a2); probe_a4 = np.array(probe_a4); probe_cut = np.array(probe_cut)
    res["probe_s_geoms"] = s_geoms
    res["probe_a2_spread"] = probe_a2
    res["probe_a4_spread"] = probe_a4
    res["probe_cut_spread"] = probe_cut

    # physical scale: bare grading ~ M_KK, Yukawa ~ m_tau (GeV) => ratio
    s_geom_phys = float(M_KK / m_tau_PDG)                   # (local) ~4.18e16
    res["s_geom_phys"] = s_geom_phys
    # interpolate the a_4 (zeta) probe spread at the physical scale (log-log)
    lift_a4_phys = float(np.interp(np.log10(s_geom_phys), np.log10(s_geoms), probe_a4))
    res["lift_a4_phys"] = lift_a4_phys
    # peak lift over the scan (the artificial O(1) regime)
    res["lift_a4_peak"] = float(probe_a4.max())
    res["lift_a4_peak_sgeom"] = float(s_geoms[int(np.argmax(probe_a4))])
    # eps_flat crossing on the large-scale (1/s_geom) tail of the zeta probe
    above = probe_a4 > EPS_FLAT                             # (local)
    if np.any(above):
        last_above = np.where(above)[0].max()
        s_cross = float(s_geoms[last_above])
    else:
        s_cross = 0.0                                      # (local) no crossing (always below floor)
    res["lift_a4_eps_crossing_sgeom"] = s_cross
    print("\n=== STEP 3: LIFT-CANDIDATE PROBE (H = s_geom*G + M_e(R); scheme-dependent) ===")
    print(f"  zeta a_4 lift PEAK   = {res['lift_a4_peak']:.3e} at s_geom={res['lift_a4_peak_sgeom']:.2e} "
          f"(artificial O(1) rescale)")
    print(f"  zeta a_4 lift CROSSES eps_flat below s_geom ~ {s_cross:.2e} (lift decays as 1/s_geom)")
    print(f"  PHYSICAL s_geom = M_KK/m_tau = {s_geom_phys:.3e}")
    print(f"  zeta a_4 lift @ PHYSICAL scale = {lift_a4_phys:.3e}  "
          f"(<= eps_flat={EPS_FLAT:.0e}? {lift_a4_phys <= EPS_FLAT}  => FLAT at physical scale)")
    print("  NOTE: lift also requires NON-SCALAR bare grading; §VII.BL multiplicity-scalar")
    print("        theorem => G ∝ I on the generation triple => cross term collapses => FLAT.")

    # ===== STEP 4: functional-sensitivity classification =====
    flat_zeta = res["dS_a4_over_S_ZETA"] <= EPS_FLAT
    flat_cutoff = res["dS_cutoff_over_S"] <= EPS_FLAT
    res["FI_flat_binary"] = bool(flat_zeta and flat_cutoff)  # FLAT in BOTH => FUNCTIONAL-INDEPENDENT
    res["lift_physical_below_floor"] = bool(lift_a4_phys <= EPS_FLAT)
    print("\n=== STEP 4: functional-sensitivity classification ===")
    print(f"  flat in zeta (a_4)?   {flat_zeta}")
    print(f"  flat in cutoff (f*)?  {flat_cutoff}")
    print(f"  => FLAT-vs-LIFTED binary FUNCTIONAL-INDEPENDENT: {res['FI_flat_binary']}")
    print(f"  lift MAGNITUDE / SA-min U_eL: SCHEME-DEPENDENT (physical-scale lift below floor: "
          f"{res['lift_physical_below_floor']})")

    return res


# ---------------------------------------------------------------------------
# Section 7 -- Verdict (plan §W2-5: PASS=flat, FAIL=lifted, INFO=regulator-ambiguous)
# ---------------------------------------------------------------------------
def verdict_from(res: dict) -> str:
    """Canonical verdict keyed on the zeta (a_4) scheme per regulator_pin a_n^{zeta}:
       PASS iff ΔS_zeta/S_total <= eps_flat (flat);
       FAIL iff > eps_flat with a definite SA-min U_eL (lifted);
       INFO iff the lift sits within SCHEMATIC-vs-FULL ambiguity (N/A here -- FULL zeta)."""
    dS_zeta = res["dS_a4_over_S_ZETA"]                      # (local) CANONICAL discriminator
    if dS_zeta <= EPS_FLAT:
        return "PASS"                                       # flat: under-determination CONFIRMED
    # lifted: but check the FULL-physical-scale probe is the discriminator, not an
    # O(1)-rescale artifact. (FULL zeta here, so INFO SCHEMATIC-clause does not fire.)
    return "FAIL"


# ---------------------------------------------------------------------------
# Section 8 -- Plot
# ---------------------------------------------------------------------------
def make_plot(res: dict, composite: str) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(18, 5.4))

    # Panel 1: ΔS/S per functional (PRIMARY) vs eps_flat
    ax = axes[0]
    labels = ["a_0=Tr1", "a_2=TrD^2", "a_4=TrD^4\n(=S_zeta)", "S_cutoff\n(f*)"]
    vals = [max(res["dS_a0_over_S"], 1e-18), max(res["dS_a2_over_S"], 1e-18),
            max(res["dS_a4_over_S_ZETA"], 1e-18), max(res["dS_cutoff_over_S"], 1e-18)]
    x = np.arange(4)
    cols = ["#1e8449" if v <= EPS_FLAT else "#c0392b" for v in vals]
    ax.bar(x, vals, color=cols, edgecolor="k", zorder=3)
    ax.axhline(EPS_FLAT, color="tab:blue", ls="--", lw=1.8, label=f"eps_flat={EPS_FLAT:.0e}")
    ax.set_yscale("log")
    ax.set_xticks(x); ax.set_xticklabels(labels, fontsize=8.5)
    ax.set_ylabel("ΔS/S_total over U_eL orbit (log)")
    ax.set_title(f"PRIMARY: finite Dirac = Yukawa(U_eL) only\n"
                 f"ALL functionals FLAT => {composite} (trace cyclicity)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3, axis="y", zorder=0)

    # Panel 2: lift-candidate probe ΔS/S vs s_geom (bare-grading/Yukawa scale)
    ax = axes[1]
    sg = res["probe_s_geoms"]
    ax.loglog(sg, np.maximum(res["probe_a4_spread"], 1e-20), color="tab:purple", lw=2,
              label="zeta a_4 lift")
    ax.loglog(sg, np.maximum(res["probe_a2_spread"], 1e-20), color="tab:orange", lw=1.4,
              ls="--", label="a_2 lift")
    ax.axhline(EPS_FLAT, color="tab:blue", ls="--", lw=1.8, label=f"eps_flat={EPS_FLAT:.0e}")
    ax.axvline(res["s_geom_phys"], color="k", ls=":", lw=1.8,
               label=f"PHYSICAL M_KK/m_tau={res['s_geom_phys']:.1e}")
    ax.scatter([res["s_geom_phys"]], [max(res["lift_a4_phys"], 1e-20)], c="k", s=70, zorder=6)
    ax.set_xlabel("s_geom = bare-grading / Yukawa scale")
    ax.set_ylabel("lift ΔS/S over U_eL orbit (log)")
    ax.set_title("LIFT-CANDIDATE PROBE (scheme-dependent)\n"
                 "lift ~ 1/s_geom => BELOW floor at physical scale")
    ax.legend(fontsize=7.5); ax.grid(alpha=0.3, which="both")

    # Panel 3: checklist + substrate framing
    ax = axes[2]
    ax.axis("off")
    ax.text(0.0, 1.0, f"{GATE_ID}\n=> {composite} (flat)", fontsize=11, weight="bold",
            transform=ax.transAxes, va="top")
    txt = (
        f"PRIMARY (finite spectral triple, FULL zeta):\n"
        f"  S = Tr f(D_F^2/Λ^2) = 2 Σ_i f(m_i^2/Λ^2)\n"
        f"  depends on MASSES only (trace cyclicity)\n"
        f"  a_4 (zeta) ΔS/S = {res['dS_a4_over_S_ZETA']:.2e}\n"
        f"  cutoff f* ΔS/S  = {res['dS_cutoff_over_S']:.2e}\n"
        f"  a_2        ΔS/S = {res['dS_a2_over_S']:.2e}\n"
        f"  a_0=Tr(1)  ΔS/S = {res['dS_a0_over_S']:.2e} (absent in zeta)\n"
        f"  control (full conj) = {res['control_conj_a4_spread']:.2e}\n"
        f"--- FUNCTIONAL-INDEPENDENT flat: {res['FI_flat_binary']}\n"
        f"--- eps_flat = {EPS_FLAT:.0e}\n\n"
        f"LIFT-PROBE (scheme-dependent):\n"
        f"  peak lift = {res['lift_a4_peak']:.2e} @ s_geom={res['lift_a4_peak_sgeom']:.1e}\n"
        f"  @ PHYSICAL s_geom={res['s_geom_phys']:.1e}:\n"
        f"     lift = {res['lift_a4_phys']:.2e} (<= eps_flat: {res['lift_physical_below_floor']})\n\n"
        f"VERDICT: U_eL is a FLAT direction.\n"
        f"Under-determination CONFIRMED: substrate\n"
        f"supplies the M_R ruler, NOT the U_eL seed.\n"
        f"(Wave-3 lepton-CP: J_PMNS=0 is ANSATZ-\n"
        f"ARTIFACT-as-derived within a free family.)"
    )
    ax.text(0.0, 0.90, txt, fontsize=8.0, transform=ax.transAxes, va="top", family="monospace")

    fig.suptitle(f"{GATE_ID}: does S=Tr f(D_K/Λ) select the lepton mixing U_eL? "
                 f"(D_K(tau_fold={TAU}), L_max={L_MAX}); regulator a_n^{{zeta}}",
                 fontsize=11)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 9 -- Verdict payload (race-safe MCP single-writer; print only)
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note="", extra_rows=None) -> dict:
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
        payload["extra_rows"] = extra_rows
    print("\n=== EMIT_VERDICT PAYLOAD (call mcp__knowledge__emit_verdict with these) ===")
    print(json.dumps(payload, indent=2))
    return payload


# ---------------------------------------------------------------------------
# Section 10 -- Main
# ---------------------------------------------------------------------------
def main():
    pins = log_input_pins(INPUT_FILES)
    res = compute()
    composite = verdict_from(res)

    make_plot(res, composite)

    audit_sha, content_sha = compute_dual_sha(THIS, CANONICAL_PATH, pins)

    # ----- persist npz -----
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION, L_max=L_MAX,
        eps_flat=EPS_FLAT, tau=TAU,
        m_e_vals=res["m_e_vals"], C2_E=res["C2_E"],
        N_eval=res["N_eval"],
        dS_a0_over_S=res["dS_a0_over_S"],
        dS_a2_over_S=res["dS_a2_over_S"],
        dS_a4_over_S_ZETA=res["dS_a4_over_S_ZETA"],
        dS_cutoff_over_S=res["dS_cutoff_over_S"],
        S_zeta_value=res["S_zeta_value"], S_cutoff_value=res["S_cutoff_value"],
        control_conj_a4_spread=res["control_conj_a4_spread"],
        probe_s_geoms=res["probe_s_geoms"],
        probe_a2_spread=res["probe_a2_spread"],
        probe_a4_spread=res["probe_a4_spread"],
        probe_cut_spread=res["probe_cut_spread"],
        s_geom_phys=res["s_geom_phys"],
        lift_a4_phys=res["lift_a4_phys"],
        lift_a4_peak=res["lift_a4_peak"],
        lift_a4_peak_sgeom=res["lift_a4_peak_sgeom"],
        lift_a4_eps_crossing_sgeom=res["lift_a4_eps_crossing_sgeom"],
        FI_flat_binary=res["FI_flat_binary"],
        lift_physical_below_floor=res["lift_physical_below_floor"],
        m_e_recon_resid=res["m_e_recon_resid"],
        audit_sha256=audit_sha, content_sha256=content_sha,
    )

    # ----- value payload string -----
    label = "FLAT" if composite == "PASS" else ("LIFTED" if composite == "FAIL" else "AMBIGUOUS")
    value = (
        f"{label};dS_zeta(a4)/S={res['dS_a4_over_S_ZETA']:.3e};"
        f"dS_cutoff(f*)/S={res['dS_cutoff_over_S']:.3e};dS_a2/S={res['dS_a2_over_S']:.3e};"
        f"eps_flat={EPS_FLAT:.0e};FI_flat_binary={res['FI_flat_binary']}(cutoff==zeta==flat);"
        f"trace-cyclicity-control={res['control_conj_a4_spread']:.1e};"
        f"lift-probe_peak={res['lift_a4_peak']:.2e}@sgeom={res['lift_a4_peak_sgeom']:.1e}_"
        f"PHYSICAL@{res['s_geom_phys']:.1e}={res['lift_a4_phys']:.2e}(below_floor="
        f"{res['lift_physical_below_floor']});under-determination-CONFIRMED;U_eL-FREE-direction"
    )

    extra = [
        f"# regulator_pin=a_n^{{zeta}} (zeta-regularized spectral action; a_0^zeta,a_2^zeta,a_4^zeta); CLASS=FULL (live moment eval, NOT SCHEMATIC helper)",
        f"# functional-sensitivity: FLAT-vs-LIFTED binary FUNCTIONAL-INDEPENDENT (flat in cutoff f* AND zeta a_4); lift MAGNITUDE SCHEME-DEPENDENT (physical-scale-suppressed 1/s_geom)",
    ]
    print_verdict_payload(composite, value, audit_sha, content_sha, extra_rows=extra)

    print("\n=== ARTIFACTS ===")
    print(f"  npz: {OUT_NPZ}")
    print(f"  png: {OUT_PNG}")
    print(f"  VERDICT: {GATE_ID}: {composite} (flat={composite=='PASS'})")


if __name__ == "__main__":
    main()
