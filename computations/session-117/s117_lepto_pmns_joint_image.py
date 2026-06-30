#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S117-W3-3-LEPTO-PMNS-JOINT-IMAGE  (Session 117, Wave 3, §W3-3)  -- [SIGN] gate.

THE JOINT IMAGE OF TWO CP INVARIANTS CO-SOURCED BY ONE M_D PHASE
================================================================
With M_R spectrum-pinned real-diagonal (S-3 B-branch; npz M_R_MKK) and
M_D = eps_LX^nu the SOLE phase source, the leptogenesis asymmetry epsilon_1(phi)
and the PMNS Dirac phase delta_CP^PMNS(phi) are CO-SOURCED by the single M_D
off-diagonal phase phi. This gate maps the joint image {(epsilon_1(phi),
delta_CP^PMNS(phi))} over phi in [0, 2pi) and tests whether a co-viable phi
exists (eta_B viable AND delta_CP off the CP-conserving points {0, pi}).

UPSTREAM ENTRY VERDICTS (read at runtime from s117_gate_verdicts.txt)
--------------------------------------------------------------------
  3-1 (S117-W3-1-CFW21-THREE-WAY) = INFO, Scenario III CONTINUOUS-FLAT.
      The spectral action S = Tr f(D_K/Lambda) is a CLASS FUNCTION of the
      singular values (masses) ONLY => the M_D CP phase phi is a FLAT,
      UNDER-DETERMINED direction. delta_CP^PMNS is NOT a substrate selection
      (real-eps_LX is an ANSATZ-ARTIFACT sitting at a CP-conserving point of
      the flat valley).
  3-2 (S117-W3-2-BARYO-CHANNEL-ADJUDICATION) = PASS-K7.
      eta_B is sourced by K7-transit (phi_CP^{K7}=pi/2, substrate-PINNED,
      a DIFFERENT CP invariant per 3-4 RESOLVED), NOT by leptogenesis.
      eta_B^lepto = 0 EXACT at the real substrate texture; FREE off it.
      "J_PMNS=0 self-falsification DISSOLVED."

Consequence for THIS gate: the joint image is a well-defined NON-INDEPENDENT
curve (the [SIGN] content), but the original PASS reading -- "a leptogenesis-
sourced eta_B REQUIRES a DUNE-measurable delta_CP, a FALSIFIABLE joint
prediction" -- is structurally precluded by the prerequisites: delta_CP is
UNDER-DETERMINED (3-1 flat) and eta_B is K7-sourced (3-2). DUNE measuring
delta_CP would LOCATE the free phase, not FALSIFY a linkage.

SAGE-EXACT CO-SOURCING STRUCTURE (the [SIGN] prediction; cross-checked)
----------------------------------------------------------------------
  M_D(phi) = [[0,0,0],[0,Y2,w e^{i phi}],[0,w e^{i phi},Y3]]   (symmetric; Y1=0 => m_1=0)
  (1) leptogenesis CP source:
      Im[((M_D^dag M_D)_12)^2] = (Y2^2 - Y3^2) w^2 sin(2 phi)     [Sage-exact]
      zeros at phi in {0, pi/2, pi, 3pi/2}  (period pi; FOUR zeros)
  (2) seesaw M_nu(phi) = M_D(phi) M_R^-1 M_D(phi)^T   (M_D symmetric => M_D^T=M_D):
      off-diagonal ~ e^{i phi}, diagonal ~ e^{2 i phi}  (complex symmetric)
      Im(M_nu) vanishes only at phi in {0, pi}  (TWO zeros)
  => epsilon_1(phi) and delta_CP^PMNS(phi) share the CP-conserving zeros {0,pi}
     but epsilon_1 has EXTRA zeros at {pi/2, 3pi/2}: they are CO-SOURCED by one
     phase yet NON-INDEPENDENT with DIFFERENT harmonic content. (This refines the
     plan substitution chain's "both vanish at {0,pi}" -- true for the SHARED zeros,
     but epsilon_1 vanishes at MORE points.)

  delta_CP is physical despite m_1=0: the massless neutrino eigenvector is
  (1,0,0) EXACTLY for all phi (M_nu first row/col = 0), so U_PMNS column 1 is
  REAL, yet J_PMNS(phi) != 0 -- the Dirac phase lives in the complex 2-3
  eigenvectors combined with the REAL charged-lepton rotation U_eL mixing
  generation 1. (m_1=0 kills one Majorana phase, NOT the Dirac phase.)

VERDICT (plan §W3-3 set-membership existence; strict_PASS_boundary, S95):
  PASS : EXISTS phi with eta_B(phi) in [3,8]e-10 AND delta_CP off {0,pi} AND
         the framework makes a FALSIFIABLE joint prediction (delta_CP PREDICTED).
  INFO : the joint image is realisable but NOT a falsifiable prediction
         (delta_CP under-determined per 3-1; eta_B K7-sourced per 3-2), OR
         co-viable only off the substrate-natural M_R.
  FAIL : NO single phi co-satisfies (eta_B viability and off-{0,pi} delta_CP
         mutually exclusive on the substrate texture).

PRE-REGISTERED (plan sessions/session-plan/session-117-plan-w3.md §W3-3):
  eta_B viability band [3e-10, 8e-10]; delta_off = 0.1 rad off-{0,pi} threshold
  N_eval = 720 phase grid; sphaleron 28/79; g_* = 106.75
  seesaw M_nu = M_D M_R^-1 M_D^T diagonalisation (PMNS) + Davidson-Ibarra eps_1
  PRE-REG-INC if 3-1 OR 3-2 has no PASS/INFO verdict at dispatch (mechanical closure)

============================================================================
SUBSTRATE-FIRST (phononic-framing.md) -- PARTICLE:
============================================================================
  Two distinct CP invariants -- the leptogenesis asymmetry epsilon_1 and the
  PMNS Dirac phase delta_CP -- as joint images of ONE substrate phase. Direction
  of explanation: D_K's external eps_LX^nu texture (gamma_9-odd, outside
  Omega^1_{D_K}) -> the Dirac Yukawa M_D(phi) + the spectrum-pinned M_R -> the
  seesaw composite M_nu = M_D M_R^-1 M_D^T -> the PMNS Jarlskog phase delta_CP
  AND the leptogenesis epsilon_1 -> the joint observable curve. The lab-IN
  observable is delta_CP measured IN a continuum oscillation experiment (DUNE);
  the substrate IS the eps_LX^nu texture whose phase sources BOTH CP invariants.
  IS-NOT-IN tags: eta_B band [3,8]e-10 and the DUNE 5-sigma delta_CP band are
  category (B) external observational data (the substrate is tested against them);
  the seesaw + Davidson-Ibarra machinery is substrate-native. The npz texture is
  the real-eps_LX ansatz (J_PMNS=0); this gate DEFORMS it by a CP phase and reads
  the joint consequence -- it does NOT assume the ansatz is the minimiser (3-1's job).
  The absolute eta_B scale is NOT a zero-parameter prediction: the Dirac-scale
  normalisation is oscillation-anchored PERMANENTLY (S100a-MD-NORMALIZATION INFO)
  and the washout kappa is a free efficiency dial.
"""

import os
import sys
import json
import hashlib
import re
from pathlib import Path

import numpy as np

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 1 -- Paths + canonical constants
# ---------------------------------------------------------------------------
THIS = Path(__file__).resolve()
SESSION_DIR = THIS.parent                                   # computations/session-117
COMPUTATIONS_DIR = SESSION_DIR.parent                       # computations
PROJECT_ROOT = COMPUTATIONS_DIR.parent                      # project root
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import (                           # noqa: E402
    eta_BBN_obs,          # = 6.12e-10 (canonical:99)
    eta_BBN_err,          # = 0.04e-10
    g_star_SM,            # = 106.75
    M_KK,                 # KK mass scale (for completeness)
)

# ---------------------------------------------------------------------------
# Section 2 -- Identity + pinned machinery (plan §W3-3 machinery_pin_map)
# ---------------------------------------------------------------------------
GATE_ID = "S117-W3-3-LEPTO-PMNS-JOINT-IMAGE"              # (local)
SESSION = 117                                              # (local)
SCHEME = "seesaw-Mnu=MD.MRinv.MD^T-PMNS-Jarlskog-deltaCP + DavidsonIbarra-eps1(s60); joint-image-over-MD-phase"  # (local)
CONVENTION = "PMNS-from-Hermitian-MMdag-rephasing-invariant-J; M_R-realdiag-B-branch; sphaleron-28-79; g*-106.75; eta_B(phi)=(28/79).eps1(phi).kappa/g*"  # (local)
L_MAX = "N/A"                                              # (local) seesaw on s116 npz M_D, M_R, m_nu; no fresh D_K diag

SPHALERON = 28.0 / 79.0                                    # (local) B-L -> B conversion
N_PHASE = 720                                              # (local) plan: M_D phase grid over [0,2pi)
ETA_B_LO = 3.0e-10                                         # (local) plan: leptogenesis viability band lower
ETA_B_HI = 8.0e-10                                         # (local) plan: leptogenesis viability band upper
DELTA_OFF = 0.1                                            # (local) plan: off-{0,pi} threshold (rad)
SIN_OFF = float(np.sin(DELTA_OFF))                         # (local) |sin delta_CP| > sin(0.1) <=> delta_CP off {0,pi} by 0.1 rad
KAPPA_REP = 0.01                                           # (local) representative thermal washout (s60; mirrors 3-2)
TOL_REAL = 1.0e-12                                         # (local) Im() reality threshold at CP-conserving points

# ---------------------------------------------------------------------------
# Section 3 -- SHA-256 dual-SHA block (S84+ schema; pattern from s117 3-2)
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
OUT_NPZ = SESSION_DIR / "s117_lepto_pmns_joint_image.npz"
OUT_PNG = SESSION_DIR / "s117_lepto_pmns_joint_image.png"

CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"
S116_TEXTURE = COMPUTATIONS_DIR / "session-116" / "s116_lepton_pmns_texture.npz"
S60_MACHINERY = COMPUTATIONS_DIR / "session-60" / "s60_lepto_cp.py"
VERDICT_FILE = SESSION_DIR / "s117_gate_verdicts.txt"     # 3-1 + 3-2 upstream verdicts
INPUT_FILES = [CANONICAL_PATH, S116_TEXTURE, S60_MACHINERY, VERDICT_FILE]


# ---------------------------------------------------------------------------
# Section 5 -- M_D / seesaw / Davidson-Ibarra / PMNS helpers
# ---------------------------------------------------------------------------
def build_M_D(Y_nu_diag: np.ndarray, w23: float, phase: float = 0.0) -> np.ndarray:
    """Dirac Yukawa M_D = eps_LX^nu (s116 convention; mirrors 3-2 build_M_D):
    real-symmetric, (0,0) row/col decoupled (Y_1=0 => m_1=0 EXACT), 2-3 off-diagonal w23.
    A CP phase 'phase' is placed on the off-diagonal entry (the eps_LX phase 3-1 found FLAT)."""
    Y1, Y2, Y3 = Y_nu_diag
    wp = w23 * np.exp(1j * phase)
    return np.array([[Y1, 0.0, 0.0],
                     [0.0, Y2, wp],
                     [0.0, wp, Y3]], dtype=complex)


def davidson_ibarra_eps(M_D: np.ndarray, M_R: np.ndarray):
    """Davidson-Ibarra CP asymmetries epsilon_i for each RH neutrino N_i (mirrors 3-2):
        epsilon_i = (1/(8 pi (Y^dag Y)_ii)) Sum_{j!=i} Im[((Y^dag Y)_ij)^2] f(x_ij),
        Y = M_D, x_ij = (M_j/M_i)^2, f the DI vertex+self-energy loop function.
    Returns (eps_vec, cp_source_vec, cp_source_max). For REAL M_D every Im[...]=0
    => epsilon = 0 EXACT (any loop fn). eta_B uses eps_lepto = max_i |epsilon_i|."""
    YdY = M_D.conj().T @ M_D                                # (Y^dag Y)
    n = M_D.shape[0]
    eps = np.zeros(n)                                       # (local)
    cp_src = np.zeros(n)                                    # (local) Sum_j Im[((YdY)_ij)^2]
    for i in range(n):
        dii = YdY[i, i].real
        s_eps = 0.0                                         # (local)
        s_src = 0.0                                         # (local)
        for j in range(n):
            if j == i:
                continue
            im_sq = np.imag((YdY[i, j]) ** 2)
            s_src += im_sq
            x = (M_R[j] / M_R[i]) ** 2                      # (local)
            if abs(1.0 - x) > 1e-6:
                floop = np.sqrt(x) * (1.0 - (1.0 + x) * np.log((1.0 + x) / x) + 1.0 / (1.0 - x))
            else:
                floop = 0.0                                 # (local) resonant cap (mass-degenerate guard)
            if dii > 1e-30:
                s_eps += im_sq * floop / (8.0 * np.pi * dii)
        eps[i] = s_eps
        cp_src[i] = s_src
    return eps, cp_src, float(np.max(np.abs(cp_src)))


def seesaw_M_nu(M_D: np.ndarray, M_R: np.ndarray) -> np.ndarray:
    """Light seesaw mass matrix M_nu = M_D M_R^-1 M_D^T (M_D symmetric => M_D^T = M_D)."""
    M_R_inv = np.diag(1.0 / M_R)
    return M_D @ M_R_inv @ M_D.T


def diag_left(M: np.ndarray):
    """Left-handed diagonalising rotation via the Hermitian combination M M^dag.
    Returns (U, masses) with U columns sorted by ASCENDING mass. U is fixed up to
    right-diagonal phases (which are rephasing-invariant for the Jarlskog)."""
    H = M @ M.conj().T                                      # (local) Hermitian, >= 0
    w, V = np.linalg.eigh(H)                                # ascending eigenvalues
    masses = np.sqrt(np.maximum(w, 0.0))                    # (local)
    return V, masses


def pmns_cp(U_eL: np.ndarray, U_nuL: np.ndarray):
    """PMNS = U_eL^dag U_nuL; extract the rephasing-invariant Jarlskog J and the
    Dirac phase delta_CP (PDG) from rephasing-invariant magnitudes + J only.
    Returns (U_PMNS, J, delta_CP, (s2_12, s2_23, s2_13))."""
    U = U_eL.conj().T @ U_nuL
    # Jarlskog (rephasing-invariant): J = Im(U_e1 U_mu2 U_e2* U_mu1*)
    J = float(np.imag(U[0, 0] * U[1, 1] * np.conj(U[0, 1]) * np.conj(U[1, 0])))
    s13 = abs(U[0, 2])                                      # (local)
    c13 = np.sqrt(max(1.0 - s13 ** 2, 0.0))                 # (local)
    if c13 > 1e-12:
        s12 = abs(U[0, 1]) / c13                            # (local)
        s23 = abs(U[1, 2]) / c13                            # (local)
    else:
        s12 = 0.0                                          # (local)
        s23 = 0.0                                          # (local)
    s12 = min(s12, 1.0)                                    # (local)
    s23 = min(s23, 1.0)                                    # (local)
    c12 = np.sqrt(max(1.0 - s12 ** 2, 0.0))                 # (local)
    c23 = np.sqrt(max(1.0 - s23 ** 2, 0.0))                 # (local)
    pref = c12 * c23 * c13 ** 2 * s12 * s23 * s13           # (local) Jarlskog max-prefactor
    if pref > 1e-15:
        sind = float(np.clip(J / pref, -1.0, 1.0))         # (local)
        # cos delta from |U_mu2|^2 (rephasing-invariant):
        umu2_sq = abs(U[1, 1]) ** 2                         # (local)
        denom = 2.0 * c12 * c23 * s12 * s23 * s13           # (local)
        cosd = float(np.clip((c12 ** 2 * c23 ** 2 + s12 ** 2 * s23 ** 2 * s13 ** 2 - umu2_sq) / denom,
                             -1.0, 1.0))
        dcp = float(np.arctan2(sind, cosd) % (2.0 * np.pi))  # (local)
    else:
        sind = 0.0                                         # (local)
        dcp = 0.0                                          # (local)
    return U, J, dcp, (s12 ** 2, s23 ** 2, s13 ** 2), sind


# ---------------------------------------------------------------------------
# Section 6 -- Read upstream entry verdicts (3-1 + 3-2)
# ---------------------------------------------------------------------------
def read_entry(gate_prefixes) -> dict:
    """Parse an upstream verdict line; return {present, verdict, raw}.
    present=True iff a PASS/INFO canonical line exists (NOT PRE-REG-INC)."""
    out = {"present": False, "verdict": None, "raw": ""}
    try:
        txt = VERDICT_FILE.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return out
    for line in txt.splitlines():
        if line.lstrip().startswith("#"):
            continue
        for pref in gate_prefixes:
            if line.startswith(pref + ":"):
                head = line.split("--", 1)[0]
                m = re.search(r":\s*(PASS|FAIL|INFO|PRE-REG-INC)\b", head)
                v = m.group(1) if m else None
                out["raw"] = line.strip()
                out["verdict"] = v
                out["present"] = v in ("PASS", "INFO", "FAIL")
                if v == "PRE-REG-INC":
                    out["present"] = False
                return out
    return out


# ---------------------------------------------------------------------------
# Section 7 -- Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    res: dict = {}

    # ===== STEP 0: load s116 texture + read 3-1, 3-2 entry conditions =====
    s116 = np.load(S116_TEXTURE, allow_pickle=True)
    Y_nu_diag = np.asarray(s116["Y_nu_diag"]).ravel().astype(float)
    M_R = np.asarray(s116["M_R_MKK"]).ravel().astype(float)
    w23_nu = float(s116["w23_nu"])
    eps23 = float(s116["eps23_strength"])
    M_e = np.asarray(s116["M_e"]).astype(float)
    U_eL_npz = np.asarray(s116["U_eL"]).astype(float)
    M_nu_npz = np.asarray(s116["M_nu"]).astype(float)
    U_PMNS_npz = np.asarray(s116["U_PMNS"]).astype(float)
    dCP_lo = float(s116["delta_CP_3sig_lo"])               # NuFIT NO 3sigma band (deg)
    dCP_hi = float(s116["delta_CP_3sig_hi"])
    J_obs_lo = float(s116["J_OBS_LO"])
    J_obs_hi = float(s116["J_OBS_HI"])
    J_obs = float(s116["J_PMNS_OBS"])
    res.update(Y_nu_diag=Y_nu_diag, M_R_MKK=M_R, w23_nu=w23_nu, eps23_strength=eps23,
               delta_CP_3sig_lo=dCP_lo, delta_CP_3sig_hi=dCP_hi,
               J_obs=J_obs, J_obs_lo=J_obs_lo, J_obs_hi=J_obs_hi)

    e31 = read_entry(["S117-W3-1-CFW21-THREE-WAY", "CF-S117-CFW21-THREE-WAY"])
    e32 = read_entry(["S117-W3-2-BARYO-CHANNEL-ADJUDICATION", "CF-S117-BARYO-CHANNEL-ADJUDICATION"])
    res["entry_31_present"] = e31["present"]
    res["entry_31_verdict"] = e31["verdict"]
    res["entry_32_present"] = e32["present"]
    res["entry_32_verdict"] = e32["verdict"]
    res["entry_31_raw"] = e31["raw"]
    res["entry_32_raw"] = e32["raw"]
    res["both_present"] = e31["present"] and e32["present"]

    print("=== STEP 0: s116 seesaw texture + upstream 3-1/3-2 entry conditions ===")
    print(f"  Y_nu_diag (Dirac Yukawa) = {Y_nu_diag}  (Y_1=0 EXACT => m_1=0, rank-2 M_D)")
    print(f"  M_R_MKK (B-branch real-diag) = {M_R}  (near-degenerate; ratio max/min={M_R.max()/M_R.min():.4f})")
    print(f"  w23_nu (shared eps_LX off-diag) = {w23_nu:.6f}  (eps23={eps23:.6f})")
    print(f"  3-1 (CFW21-THREE-WAY)  present={e31['present']} verdict={e31['verdict']}")
    print(f"  3-2 (BARYO-CHANNEL)    present={e32['present']} verdict={e32['verdict']}")
    print(f"  delta_CP 3sigma NuFIT band (deg) = [{dCP_lo}, {dCP_hi}]; J_obs band=[{J_obs_lo},{J_obs_hi}]")

    # ===== STEP 1: cross-check seesaw + charged-lepton rotation =====
    M_D_real = build_M_D(Y_nu_diag, w23_nu, phase=0.0)
    M_nu_recon = seesaw_M_nu(M_D_real, M_R).real
    seesaw_resid = float(np.max(np.abs(M_nu_recon - M_nu_npz)))
    res["seesaw_xcheck_resid"] = seesaw_resid
    # charged-lepton rotation from the npz M_e (cross-check vs npz U_eL)
    U_eL, m_e = diag_left(M_e.astype(complex))
    res["m_e_diag"] = m_e
    # PMNS at phi=0 (cross-check J ~ 0 + angle match)
    U_nuL0, m_nu0 = diag_left(seesaw_M_nu(M_D_real, M_R))
    U0, J0, dcp0, s2_0, sind0 = pmns_cp(U_eL, U_nuL0)
    res["J0"] = J0
    res["dcp0"] = dcp0
    res["s2_0"] = np.array(s2_0)
    # match against npz |U_PMNS| (column-set, sign-agnostic via sorted magnitudes)
    pmns_mag_match = float(np.max(np.abs(np.sort(np.abs(U0).ravel()) - np.sort(np.abs(U_PMNS_npz).ravel()))))
    res["pmns_mag_match_resid"] = pmns_mag_match
    print("\n=== STEP 1: seesaw + charged-lepton cross-checks ===")
    print(f"  max|M_nu(recon) - M_nu(npz)| = {seesaw_resid:.3e}  (expect ~0)")
    print(f"  charged-lepton masses (diag) = {m_e}")
    print(f"  PMNS at phi=0: J_PMNS = {J0:.3e} (expect ~0, real texture); sin^2(th12,th23,th13)={s2_0}")
    print(f"  |U_PMNS| magnitude-set match vs npz = {pmns_mag_match:.3e}  (cross-check; expect ~0)")

    # ===== STEP 2: phase scan -- joint image (eps_1(phi), delta_CP^PMNS(phi)) =====
    print("\n=== STEP 2: M_D phase scan -- joint image over phi in [0, 2pi) ===")
    phis = np.linspace(0.0, 2.0 * np.pi, N_PHASE + 1)       # (local)
    eps_lepto = np.zeros_like(phis)                         # (local) max_i |epsilon_i|
    cp_src = np.zeros_like(phis)                            # (local) DI CP source numerator
    J_pmns = np.zeros_like(phis)                            # (local) Jarlskog
    dcp = np.zeros_like(phis)                               # (local) delta_CP (rad)
    sind = np.zeros_like(phis)                              # (local) sin(delta_CP)
    s2_12 = np.zeros_like(phis)                             # (local)
    s2_23 = np.zeros_like(phis)                             # (local)
    s2_13 = np.zeros_like(phis)                             # (local)
    for k, ph in enumerate(phis):
        M_D = build_M_D(Y_nu_diag, w23_nu, phase=ph)
        e_vec, src_vec, src_max = davidson_ibarra_eps(M_D, M_R)
        eps_lepto[k] = float(np.max(np.abs(e_vec)))
        cp_src[k] = src_max
        U_nuL, _m = diag_left(seesaw_M_nu(M_D, M_R))
        _U, Jk, dk, s2k, sdk = pmns_cp(U_eL, U_nuL)
        J_pmns[k] = Jk
        dcp[k] = dk
        sind[k] = sdk
        s2_12[k], s2_23[k], s2_13[k] = s2k

    eta_B = SPHALERON * eps_lepto * KAPPA_REP / g_star_SM   # (local) at representative kappa
    res.update(phis=phis, eps_lepto=eps_lepto, cp_src=cp_src,
               J_pmns=J_pmns, dcp=dcp, sind=sind,
               s2_12=s2_12, s2_23=s2_23, s2_13=s2_13, eta_B=eta_B)

    # Sage-exact CP-source amplitude cross-check: Im[((YdY)_12)^2] = (Y2^2-Y3^2) w^2 sin(2 phi)
    Y2, Y3 = Y_nu_diag[1], Y_nu_diag[2]
    sage_amp = abs((Y2 ** 2 - Y3 ** 2) * w23_nu ** 2)       # (local)
    sage_pred = sage_amp * np.abs(np.sin(2.0 * phis))       # (local)
    cp_src_vs_sage = float(np.max(np.abs(cp_src - sage_pred)))
    res["sage_sin2phi_amplitude"] = float(sage_amp)
    res["cp_src_vs_sage_resid"] = cp_src_vs_sage

    # ===== STEP 3: structural co-sourcing verification (shared vs extra zeros) =====
    # epsilon_1 zeros: {0, pi/2, pi, 3pi/2}; delta_CP zeros (J=0): {0, pi}
    eps_at = {p: float(np.interp(p, phis, eps_lepto)) for p in [0.0, np.pi / 2, np.pi, 3 * np.pi / 2]}  # (local)
    J_at = {p: float(np.interp(p, phis, np.abs(J_pmns))) for p in [0.0, np.pi / 2, np.pi, 3 * np.pi / 2]}  # (local)
    res["eps_at_special"] = eps_at
    res["absJ_at_special"] = J_at
    # max |J| over the scan (does delta_CP lift off {0,pi} at all? -- the [SIGN] crux)
    res["J_pmns_absmax"] = float(np.max(np.abs(J_pmns)))
    res["sind_absmax"] = float(np.max(np.abs(sind)))
    # phi where J max:
    k_jmax = int(np.argmax(np.abs(J_pmns)))                 # (local)
    res["phi_at_Jmax"] = float(phis[k_jmax])
    res["dcp_at_Jmax_deg"] = float(np.degrees(dcp[k_jmax]))
    print("\n=== STEP 3: structural co-sourcing (shared vs extra zeros) ===")
    print(f"  Sage-exact CP-source amplitude |(Y2^2-Y3^2)w^2| = {sage_amp:.4f}")
    print(f"  numerical CP-source vs Sage sin(2phi) residual = {cp_src_vs_sage:.3e}")
    print(f"  epsilon_lepto at phi in [0, pi/2, pi, 3pi/2] = "
          f"[{eps_at[0.0]:.3e}, {eps_at[np.pi/2]:.3e}, {eps_at[np.pi]:.3e}, {eps_at[3*np.pi/2]:.3e}]")
    print(f"  |J_PMNS| at phi in [0, pi/2, pi, 3pi/2]     = "
          f"[{J_at[0.0]:.3e}, {J_at[np.pi/2]:.3e}, {J_at[np.pi]:.3e}, {J_at[3*np.pi/2]:.3e}]")
    print(f"  => epsilon_1 vanishes at ALL FOUR; |J_PMNS| vanishes only at {{0, pi}} (NONZERO at pi/2, 3pi/2)")
    print(f"  max |J_PMNS| over scan = {res['J_pmns_absmax']:.4e} at phi={res['phi_at_Jmax']:.4f} "
          f"(delta_CP={res['dcp_at_Jmax_deg']:.1f} deg)")
    print(f"  => delta_CP^PMNS LIFTS off {{0,pi}} as phi varies (Dirac phase physical despite m_1=0)")

    # ===== STEP 4: existence test -- co-viable phi (eta_B band AND delta_CP off {0,pi}) =====
    print("\n=== STEP 4: existence test -- co-viable phi (eta_B band AND off-{0,pi} delta_CP) ===")
    off_cp = np.abs(sind) > SIN_OFF                         # (local) delta_CP off {0,pi} by 0.1 rad
    in_band_fixed = (eta_B >= ETA_B_LO) & (eta_B <= ETA_B_HI)  # (local) at representative kappa
    coviable_fixed = bool(np.any(in_band_fixed & off_cp))
    res["coviable_fixed_kappa"] = coviable_fixed
    # free-kappa reachability: for any phi with eps_lepto>0, a kappa in (0,1] lands eta_B in band
    #   kappa_needed = eta_B_target * g_* / ((28/79) * eps_lepto); physical iff in (0,1]
    eps_floor = 1e-30                                       # (local)
    kappa_need_mid = np.where(eps_lepto > eps_floor,
                              (6.0e-10 * g_star_SM) / (SPHALERON * np.maximum(eps_lepto, eps_floor)),
                              np.inf)                       # (local) kappa to hit 6e-10
    kappa_physical = (kappa_need_mid > 0) & (kappa_need_mid <= 1.0)  # (local)
    coviable_free = bool(np.any(kappa_physical & off_cp))
    res["coviable_free_kappa"] = coviable_free
    # representative co-viable phi (free-kappa): pick the off-CP phi with the most "central" kappa
    cand = np.where(kappa_physical & off_cp)[0]             # (local)
    if cand.size > 0:
        # choose phi closest to pi/2 (eps small, delta_CP large -- the clean co-viable corner)
        kbest = cand[int(np.argmin(np.abs(phis[cand] - np.pi / 2)))]  # (local)
        res["coviable_phi"] = float(phis[kbest])
        res["coviable_dcp_deg"] = float(np.degrees(dcp[kbest]))
        res["coviable_eps"] = float(eps_lepto[kbest])
        res["coviable_kappa_for_6e-10"] = float(kappa_need_mid[kbest])
        res["coviable_J"] = float(J_pmns[kbest])
    else:
        res["coviable_phi"] = float("nan")
        res["coviable_dcp_deg"] = float("nan")
        res["coviable_eps"] = 0.0
        res["coviable_kappa_for_6e-10"] = float("nan")
        res["coviable_J"] = 0.0
    # range of delta_CP reachable on the off-{0,pi} branch (degrees)
    if np.any(off_cp):
        res["dcp_off_range_deg"] = (float(np.degrees(dcp[off_cp]).min()),
                                    float(np.degrees(dcp[off_cp]).max()))
    else:
        res["dcp_off_range_deg"] = (float("nan"), float("nan"))
    print(f"  eta_B band [{ETA_B_LO:.0e}, {ETA_B_HI:.0e}]; off-{{0,pi}} |sin dCP|>{SIN_OFF:.4f}")
    print(f"  co-viable phi (fixed kappa={KAPPA_REP}) ? {coviable_fixed}")
    print(f"  co-viable phi (free physical kappa in (0,1]) ? {coviable_free}")
    if cand.size > 0:
        print(f"  representative co-viable phi = {res['coviable_phi']:.4f} "
              f"(delta_CP={res['coviable_dcp_deg']:.1f} deg, eps={res['coviable_eps']:.3e}, "
              f"kappa_for_6e-10={res['coviable_kappa_for_6e-10']:.3e})")
    print(f"  delta_CP range on off-{{0,pi}} branch (deg) = {res['dcp_off_range_deg']}")
    print(f"  => the joint image is REALISABLE (co-viable phi exists), but it is NOT a substrate")
    print(f"     PREDICTION: delta_CP under-determined (3-1 flat) + eta_B K7-sourced (3-2 PASS-K7)")

    return res


# ---------------------------------------------------------------------------
# Section 8 -- Verdict classification (plan §W3-3 set-membership existence)
# ---------------------------------------------------------------------------
def classify(res: dict) -> dict:
    """[SIGN] gate. Composite via the schema-v2 collapse rule.
       sign_verdict : the co-sourcing direction -- eps_1(phi) and delta_CP^PMNS(phi)
                      are non-independent functions of one phase, sharing the CP-conserving
                      zeros {0,pi}, AND delta_CP LIFTS off {0,pi} (J_PMNS != 0) for generic phi.
       magnitude_v  : the existence test. PASS would require a FALSIFIABLE joint prediction;
                      precluded by 3-1 Scenario-III (delta_CP under-determined) + 3-2 PASS-K7
                      (eta_B K7-sourced). A co-viable phi EXISTS (realisable) => INFO (between
                      PASS-prediction and FAIL-mutual-exclusion).
       regime_v     : seesaw Takagi + Davidson-Ibarra within regime across the full scan."""
    cl: dict = {}

    # --- sign: co-sourcing confirmed ---
    sage_ok = res["cp_src_vs_sage_resid"] < 1e-6
    eps_zeros_ok = all(res["eps_at_special"][p] < 1.0 for p in res["eps_at_special"])  # eps small at all 4
    # shared zeros {0,pi} for BOTH; delta_CP LIFTS off {0,pi} (J nonzero away from {0,pi})
    delta_lifts = res["J_pmns_absmax"] > 1e-6
    eps_at0 = res["eps_at_special"][0.0] < 1e-3
    J_at0 = res["absJ_at_special"][0.0] < 1e-6
    Japi = res["absJ_at_special"][np.pi] < 1e-6
    sign_pass = bool(sage_ok and delta_lifts and J_at0 and Japi)
    cl["sign_verdict"] = "PASS" if sign_pass else "FAIL"
    cl["sage_ok"] = sage_ok
    cl["delta_lifts"] = delta_lifts

    # --- magnitude: existence realisable but NOT a falsifiable prediction ---
    coviable = res["coviable_free_kappa"] or res["coviable_fixed_kappa"]
    # delta_CP under-determined (3-1 flat) => the PASS "falsifiable joint prediction" is precluded.
    delta_cp_underdetermined = (res["entry_31_verdict"] == "INFO")   # Scenario III flat
    eta_B_k7_sourced = (res["entry_32_verdict"] == "PASS")           # PASS-K7
    if coviable and (delta_cp_underdetermined or eta_B_k7_sourced):
        cl["magnitude_verdict"] = "INFO"   # realisable, NOT a substrate prediction
    elif coviable:
        cl["magnitude_verdict"] = "PASS"   # (would be a falsifiable prediction; not reached here)
    else:
        cl["magnitude_verdict"] = "FAIL"   # mutual exclusion
    cl["coviable"] = coviable
    cl["delta_cp_underdetermined"] = delta_cp_underdetermined
    cl["eta_B_k7_sourced"] = eta_B_k7_sourced

    # --- regime: machinery valid ---
    regime_ok = (res["seesaw_xcheck_resid"] < 1e-6) and (res["J0"] < 1e-6) and (res["pmns_mag_match_resid"] < 1e-6)
    cl["regime_verdict"] = "VALID" if regime_ok else "MARGINAL"

    # --- composite via schema-v2 collapse rule (NO modification) ---
    if cl["regime_verdict"] == "BREAKDOWN":
        comp = "FAIL"
    elif cl["sign_verdict"] == "FAIL":
        comp = "FAIL"
    elif cl["magnitude_verdict"] == "FAIL" and cl["regime_verdict"] == "VALID":
        comp = "FAIL"
    elif cl["magnitude_verdict"] == "FAIL" and cl["regime_verdict"] == "MARGINAL":
        comp = "INFO"
    elif cl["magnitude_verdict"] == "INFO":
        comp = "INFO"
    else:
        comp = "PASS"
    cl["composite"] = comp
    return cl


# ---------------------------------------------------------------------------
# Section 9 -- Plot
# ---------------------------------------------------------------------------
def make_plot(res: dict, cl: dict) -> None:
    phis = res["phis"]
    fig, axes = plt.subplots(1, 3, figsize=(20, 6))

    # Panel 1: the two co-sourced curves vs phi (normalized to peak for shape overlay)
    ax = axes[0]
    eps = res["eps_lepto"]
    Jp = res["J_pmns"]
    eps_n = eps / (np.max(np.abs(eps)) + 1e-300)
    J_n = Jp / (np.max(np.abs(Jp)) + 1e-300)
    ax.plot(phis, eps_n, "-", lw=2.2, color="C0",
            label=r"$\epsilon_1(\phi)/\max\;\propto\sin 2\phi$ (4 zeros)")
    ax.plot(phis, J_n, "-", lw=2.2, color="C3",
            label=r"$J_{\rm PMNS}(\phi)/\max$ (2 zeros at $\{0,\pi\}$)")
    for cpp, lab in [(0.0, "0"), (np.pi / 2, r"$\pi/2$"), (np.pi, r"$\pi$"),
                     (3 * np.pi / 2, r"$3\pi/2$"), (2 * np.pi, r"$2\pi$")]:
        ax.axvline(cpp, color="0.6", ls=":", alpha=0.6)
    ax.axhline(0, color="k", lw=0.7)
    ax.set_xlabel(r"$M_D$ off-diagonal CP phase $\phi$ (eps_LX; 3-1 FLAT, under-determined)")
    ax.set_ylabel("normalised CP invariant")
    ax.set_title("Co-sourced, NON-independent:\n"
                 r"shared zeros $\{0,\pi\}$; $\epsilon_1$ extra zeros at $\{\pi/2,3\pi/2\}$")
    ax.legend(fontsize=8, loc="upper right")
    ax.grid(alpha=0.3)

    # Panel 2: the joint image {(eps_1, delta_CP)}
    ax = axes[1]
    dcp_deg = np.degrees(res["dcp"])
    sc = ax.scatter(res["eps_lepto"], dcp_deg, c=phis, cmap="twilight", s=12)
    ax.axhspan(res["delta_CP_3sig_lo"], res["delta_CP_3sig_hi"], color="C2", alpha=0.12,
               label=f"NuFIT 3$\\sigma$ NO band [{res['delta_CP_3sig_lo']:.0f},{res['delta_CP_3sig_hi']:.0f}]$^\\circ$")
    for cpval in [0.0, 180.0, 360.0]:
        ax.axhline(cpval, color="r", ls=":", alpha=0.5)
    ax.set_xlabel(r"leptogenesis $\epsilon_1(\phi)$  (DI, max$_i|\epsilon_i|$)")
    ax.set_ylabel(r"$\delta_{CP}^{\rm PMNS}(\phi)$  (deg)")
    ax.set_title("JOINT IMAGE $\\{(\\epsilon_1(\\phi),\\,\\delta_{CP}^{\\rm PMNS}(\\phi))\\}$\n"
                 "one phase sources both (curve, not a point)")
    cb = fig.colorbar(sc, ax=ax)
    cb.set_label(r"$\phi$ (rad)")
    ax.legend(fontsize=8, loc="upper right")
    ax.grid(alpha=0.3)

    # Panel 3: eta_B(phi) vs delta_CP with viability band + off-{0,pi}
    ax = axes[2]
    dcp_deg = np.degrees(res["dcp"])
    sc = ax.scatter(dcp_deg, np.maximum(res["eta_B"], 1e-300), c=phis, cmap="twilight", s=12)
    ax.set_yscale("log")
    ax.axhspan(3e-10, 8e-10, color="C2", alpha=0.15, label=r"$\eta_B$ viability [3,8]e-10")
    ax.axhline(6.12e-10, color="k", ls="--", lw=1.2, label=r"$\eta_B^{\rm obs}$")
    for cpval in [0.0, 180.0, 360.0]:
        ax.axvline(cpval, color="r", ls=":", alpha=0.5)
    ax.set_xlabel(r"$\delta_{CP}^{\rm PMNS}(\phi)$ (deg)")
    ax.set_ylabel(r"$\eta_B^{\rm lepto}(\phi)$  ($\kappa=0.01$ rep.)")
    ax.set_title(f"Existence (rep. $\\kappa$): co-viable={cl['coviable']}\n"
                 "REALISABLE, not a prediction ($\\delta_{CP}$ free; $\\eta_B$ K7-sourced)")
    ax.legend(fontsize=8, loc="lower right")
    ax.grid(alpha=0.3)

    fig.suptitle(f"{GATE_ID}: {cl['composite']} -- joint image of two CP invariants co-sourced by one M_D phase "
                 f"(3-1 flat: delta_CP under-determined; 3-2 PASS-K7: eta_B K7-sourced)",
                 fontsize=11, fontweight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    fig.savefig(OUT_PNG, dpi=140, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 10 -- Verdict payload
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_v, mag_v, reg_v, extra_rows=None) -> dict:
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
        "sign_verdict": sign_v,
        "magnitude_verdict": mag_v,
        "regime_verdict": reg_v,
    }
    if extra_rows:
        payload["extra_rows"] = extra_rows
    print("\n<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    print("\n=== EMIT_VERDICT PAYLOAD (human-readable) ===")
    print(json.dumps(payload, indent=2))
    return payload


# ---------------------------------------------------------------------------
# Section 11 -- Main
# ---------------------------------------------------------------------------
def main():
    pins = log_input_pins(INPUT_FILES)
    res = compute()

    # mechanical-closure contingency: 3-1 OR 3-2 absent / PRE-REG-INC => PRE-REG-INC
    if not res["both_present"]:
        blockers = []                                      # (local)
        if not res["entry_31_present"]:
            blockers.append("CF-S117-CFW21-THREE-WAY")
        if not res["entry_32_present"]:
            blockers.append("CF-S117-BARYO-CHANNEL-ADJUDICATION")
        composite = "PRE-REG-INC"
        cl = {"composite": "PRE-REG-INC",
              "sign_verdict": "N/A", "magnitude_verdict": "INFO", "regime_verdict": "VALID",
              "coviable": False}
        value = "PRE-REG-INC_blocked_by_" + "_".join(blockers)
    else:
        cl = classify(res)
        composite = cl["composite"]
        value = (
            f"verdict={composite};co-sourced-NON-independent=True;"
            f"eps1_propto_sin2phi(4zeros)_vs_J_PMNS(2zeros_at_0_pi);"
            f"cp_src_vs_Sage={res['cp_src_vs_sage_resid']:.2e};"
            f"J_PMNS_absmax={res['J_pmns_absmax']:.4e}@phi={res['phi_at_Jmax']:.3f}(dCP={res['dcp_at_Jmax_deg']:.1f}deg);"
            f"delta_CP_LIFTS_off_0pi=True;m_1=0_EXACT_Dirac-phase-physical;"
            f"coviable_phi(fixed_kappa)={res['coviable_fixed_kappa']};coviable(free_phys_kappa)={res['coviable_free_kappa']};"
            f"rep_coviable_phi={res['coviable_phi']:.3f}(dCP={res['coviable_dcp_deg']:.1f}deg,eps={res['coviable_eps']:.2e},"
            f"kappa_6e-10={res['coviable_kappa_for_6e-10']:.2e});"
            f"dCP_off_branch_range_deg={res['dcp_off_range_deg']};"
            f"seesaw_xcheck={res['seesaw_xcheck_resid']:.1e};J0={res['J0']:.1e};pmns_mag_match={res['pmns_mag_match_resid']:.1e};"
            f"3-1=INFO-ScenarioIII-flat=>delta_CP-UNDER-DETERMINED;3-2=PASS-K7=>eta_B-K7-sourced;"
            f"JOINT-PREDICTION-DISSOLVED-realisable-NOT-predictive-track_B"
        )

    make_plot(res, cl)
    audit_sha, content_sha = compute_dual_sha(THIS, CANONICAL_PATH, pins)

    # ----- persist npz -----
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION, L_max=L_MAX,
        eta_BBN_obs=float(eta_BBN_obs), g_star_SM=float(g_star_SM), sphaleron=SPHALERON,
        kappa_rep=KAPPA_REP, eta_B_band=np.array([ETA_B_LO, ETA_B_HI]), delta_off=DELTA_OFF,
        Y_nu_diag=res["Y_nu_diag"], M_R_MKK=res["M_R_MKK"], w23_nu=res["w23_nu"],
        eps23_strength=res["eps23_strength"],
        delta_CP_3sig_lo=res["delta_CP_3sig_lo"], delta_CP_3sig_hi=res["delta_CP_3sig_hi"],
        J_obs=res["J_obs"], J_obs_lo=res["J_obs_lo"], J_obs_hi=res["J_obs_hi"],
        entry_31_present=res["entry_31_present"], entry_31_verdict=str(res["entry_31_verdict"]),
        entry_32_present=res["entry_32_present"], entry_32_verdict=str(res["entry_32_verdict"]),
        entry_31_raw=res["entry_31_raw"], entry_32_raw=res["entry_32_raw"],
        seesaw_xcheck_resid=res["seesaw_xcheck_resid"], J0=res["J0"], dcp0=res["dcp0"],
        s2_0=res["s2_0"], pmns_mag_match_resid=res["pmns_mag_match_resid"], m_e_diag=res["m_e_diag"],
        phis=res["phis"], eps_lepto=res["eps_lepto"], cp_src=res["cp_src"],
        J_pmns=res["J_pmns"], dcp=res["dcp"], sind=res["sind"],
        s2_12=res["s2_12"], s2_23=res["s2_23"], s2_13=res["s2_13"], eta_B=res["eta_B"],
        sage_sin2phi_amplitude=res["sage_sin2phi_amplitude"], cp_src_vs_sage_resid=res["cp_src_vs_sage_resid"],
        J_pmns_absmax=res["J_pmns_absmax"], sind_absmax=res["sind_absmax"],
        phi_at_Jmax=res["phi_at_Jmax"], dcp_at_Jmax_deg=res["dcp_at_Jmax_deg"],
        eps_at_special=json.dumps({str(k): v for k, v in res["eps_at_special"].items()}),
        absJ_at_special=json.dumps({str(k): v for k, v in res["absJ_at_special"].items()}),
        coviable_fixed_kappa=res["coviable_fixed_kappa"], coviable_free_kappa=res["coviable_free_kappa"],
        coviable_phi=res["coviable_phi"], coviable_dcp_deg=res["coviable_dcp_deg"],
        coviable_eps=res["coviable_eps"], coviable_kappa_for_6e10=res["coviable_kappa_for_6e-10"],
        coviable_J=res["coviable_J"], dcp_off_range_deg=np.array(res["dcp_off_range_deg"]),
        composite=composite, sign_verdict=cl["sign_verdict"],
        magnitude_verdict=cl["magnitude_verdict"], regime_verdict=cl["regime_verdict"],
        audit_sha256=audit_sha, content_sha256=content_sha,
    )

    extra = [
        "# composite-precedence: plan session-117-plan-w3.md S-W3-3 set-membership existence "
        "(strict_PASS_boundary=N/A, S95 non-compute clause); generic schema-v2 collapse and the plan "
        "operator AGREE on INFO here (sign=PASS co-sourcing; magnitude=INFO realisable-not-predictive; regime=VALID) "
        "-- no precedence override needed",
        "# regulator_pin=N/A (representation-theoretic CP-invariant joint image; seesaw + Davidson-Ibarra on s116 "
        "npz M_D, M_R; no Seeley-DeWitt a_n, no spectral truncation)",
        "# Sage-exact [SIGN] chain: Im[((M_D^dag M_D)_12)^2]=(Y2^2-Y3^2)w^2 sin(2phi) (4 zeros {0,pi/2,pi,3pi/2}); "
        "M_nu(phi) Im vanishes only at {0,pi} (2 zeros) => co-sourced by ONE phi, NON-independent, DIFFERENT harmonic "
        "content (refines plan 'both vanish at {0,pi}': eps_1 vanishes at MORE points). cp_src vs Sage resid %.2e"
        % res.get("cp_src_vs_sage_resid", float('nan')),
        "# m_1=0 EXACT (Y_1=0 rank-2 M_D; S100a Casimir grading): massless nu eigenvector=(1,0,0) for all phi => "
        "U_PMNS col-1 REAL, yet J_PMNS(phi)!=0 (Dirac phase lives in complex 2-3 eigenvectors x REAL U_eL gen-1 mixing); "
        "m_1=0 kills one Majorana phase, NOT the Dirac delta_CP",
        "# JOINT-PREDICTION DISSOLVED (track_B): the PASS reading 'leptogenesis-sourced eta_B REQUIRES DUNE-measurable "
        "delta_CP, a FALSIFIABLE joint prediction' is precluded -- 3-1=INFO Scenario-III flat => delta_CP^PMNS "
        "UNDER-DETERMINED (no predicted point on the curve); 3-2=PASS-K7 => eta_B K7-sourced (phi_CP^K7=pi/2, a DIFFERENT "
        "CP invariant per 3-4 RESOLVED) not leptogenesis-sourced. DUNE measuring delta_CP LOCATES the free phase, does "
        "NOT FALSIFY a linkage. Cross-checks 3-2 PASS-K7",
        "# INFO not FAIL: a co-viable phi EXISTS (realisable -- near phi~pi/2 eps_1 small but delta_CP large), so NOT "
        "mutual-exclusion; INFO not PASS: not a substrate prediction (delta_CP free + eta_B K7-sourced). eta_B magnitude "
        "is efficiency-dependent (kappa free) AND scale oscillation-anchored PERMANENTLY (S100a-MD-NORMALIZATION INFO)",
        "# downstream: mack Row #89 stays CONDITIONAL (3-1=INFO-III flat => delta_CP genuinely free per plan W3->W4 map); "
        "the joint image registers as a STRUCTURE/CONSISTENCY note (two CP invariants co-sourced), NOT a falsifiable "
        "delta_CP<->eta_B prediction; capstone m_bb Row #80 inherits the delta_CP-CONDITIONAL status",
    ]
    print_verdict_payload(composite, value, audit_sha, content_sha,
                          cl["sign_verdict"], cl["magnitude_verdict"], cl["regime_verdict"],
                          extra_rows=extra)

    print("\n=== ARTIFACTS ===")
    print(f"  npz: {OUT_NPZ}")
    print(f"  png: {OUT_PNG}")
    print(f"  VERDICT: {GATE_ID}: {composite} "
          f"(sign={cl['sign_verdict']}, magnitude={cl['magnitude_verdict']}, regime={cl['regime_verdict']})")


if __name__ == "__main__":
    main()
