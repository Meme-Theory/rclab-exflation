#!/usr/bin/env python3
"""
S100a W3-9 — S100a-FREEZEIN-OVERCONSTRAINED
===========================================

Gate: S100a-FREEZEIN-OVERCONSTRAINED ([SIGN])
Plan: sessions/session-plan/session-100a-plan-w3.md §W3-9 (R3 YAML block)
Classification: PHONONIC
Agent: transit-dynamics-theorist

HYPOTHESIS
----------
The substrate squeezed-vacuum freeze-in amplitude exp(-S0*C2(p,q)) on the
[[d,w],[w*,d]] inter-sector block is over-constrained: fitting {S0,|w|} to the
three charged-lepton masses and arg(w) to ONE CKM datum (3 real inputs)
PREDICTS the six quark mass ratios + three CKM angles + J_CP (~12 held-out
PDG observables) with no further freedom. PASS = mass+mixing SHAPE (not
scale) is a substrate prediction; FAIL = the over-constraint breaks, closing
the dynamical-freeze-in corridor cleanly (a valid informative boundary).

PRE-REGISTERED THRESHOLDS (plan §W3-9, frozen before compute)
-------------------------------------------------------------
  quark ratio : |log10(pred/PDG)| <= 0.5 dex (OOM-correct)
  CKM angle   : |theta_pred - theta_PDG| <= 1 sigma_plan
                (th12: 0.13 deg, th13: 0.013 deg, th23: 0.4 deg)
  J_CP        : |J_pred| in [2.0e-5, 4.0e-5] (PDG 2024 central 3.08e-5;
                sign two-valued under the single-|V_us|-anchor protocol,
                documented below)
  magnitude_verdict: PASS = all 12 slots in-band; INFO = mass-group XOR
                mixing-group all-pass; FAIL = neither group all-passes.
  dual-prior discriminator: gross miss = ratio dev > 1 OOM or angle > 3 sigma.

CANONICAL STRUCTURE (declared BEFORE compute; inherited from the S99
fermion-mass panel session-99-fermion-mass-transit.md §2.2/§3-B/§5 + the
plan §W3-9 substitution chain + the W2 Item-6 Z3 data):
  (D1) The 3x3 Hermitian freeze-in block is the assembly of the 2x2
       pairing blocks [[d_i, w],[w*, d_j]] over all three generation
       pairings with ONE shared complex w:
           M_F = [[d1, w_F, w_F], [w_F*, d2, w_F], [w_F*, w_F*, d3]]
       (sector rows ordered (1,0)/(1,1)/(3,0); d_i = exp(-S0*C2_i),
        C2 = (4/3, 3, 6), SU(3) quadratic Casimir, analytic).
  (D2) Generation <-> sector map: mass ASCENDS as C2 DESCENDS (the deepest
       freeze = the lightest fermion): gen1(e,u,d) <-> (3,0) C2=6;
       gen2(mu,c,s) <-> (1,1) C2=3; gen3(tau,t,b) <-> (1,0) C2=4/3.
       This is the plan Step-5 "C2-ordered sign" and is independently
       confirmed by the W2 Item-6 npz key e_sector=(3,0) and by the
       diagonal log-gap ratio (6-3)/(3-4/3) = 9/5 = 1.800 vs the observed
       ln(m_mu/m_e)/ln(m_tau/m_mu) = 1.889 (the S100a-CASIMIR-WIDENING
       plan-frozen PASS band [1.80, 1.89]).
  (D3) Tower phase assignment from the W2 Z3 triple {pi, +2pi/3, -2pi/3}
       (s100a_yukawa_overlap_offdiag.npz arg_w_M2_phi): the lepton tower
       sits at the unique SELF-CONJUGATE point (w_lep = |w| e^{i pi}
       = -|w|, real) and the up/down quark towers at mutually CONJUGATE
       phases w_u = |w| e^{+i Theta}, w_d = |w| e^{-i Theta} = w_u*
       (BDI J-conjugacy (p,q)<->(q,p); the W2 conjugate pair +-2pi/3 is
       the discrete seed, Theta is the continuous fit). This is FORCED by
       the plan 2+1 split fit protocol: {S0,|w|} from lepton ratios
       requires phase-free lepton masses (w_lep real); arg(w) -> |V_us|
       requires conjugate quark towers (else V_CKM = 1 identically).
  (D4) Lambda_u = Lambda_d (the J-conjugate towers share the freeze-in
       normalization) => the same-generation ratios m_u/m_d, m_c/m_s,
       m_t/m_b are ABSOLUTE predictions of the block (M_d = M_u* makes
       them exactly 1 — that IS the structural prediction under test).
       The overall lepton-vs-quark scale M0^sector is NOT fitted (SHAPE
       not scale; hawking threshold per S100a-M0-MH-INHERITANCE).
  (D5) If the lepton fit has multiple roots, the canonical root is the
       DIAGONAL-DOMINANT branch (smallest |w|; continuously connected to
       the w->0 diagonal limit, the S99 perturbative reading).
  Diagnostic variants (reported, NOT gated): V2 = lepton sign +|w|;
  V3 = nearest-neighbor coupling only (w_13 = 0).

FIT PROTOCOL (3 real inputs, plan stage 2)
------------------------------------------
  Stage A: {S0, |w|} from m_mu/m_e = 206.7683 and m_tau/m_mu = 16.8170
           (canonical m_mu/m_e/m_tau_PDG; PDG-POLE-scale lepton values).
           Deterministic multi-start least_squares on log residuals;
           convergence max|res| < 1e-10 (plan tolerance).
  Stage B: Theta = arg(w) from |V_us| = 0.22500 (V_us_PDG; plan anchor).
           Dense deterministic grid + bounded refine. If the anchor is
           UNREACHABLE the fit converges to the achievable boundary and
           the theta12 slot fails its 1-sigma band honestly (model
           shortfall = magnitude failure, NOT a regime failure).
           Theta -> -Theta degeneracy (V -> V*, J -> -J): primary branch
           Theta >= 0; J reported two-valued +-|J|.

SUBSTITUTION CHAIN (plan §W3-9 item 7; sign read-off)
-----------------------------------------------------
  Step 1: d_i = exp(-S0*C2_i); C2 = (4/3, 3, 6) for (1,0)/(1,1)/(3,0).
  Step 2: m_j/m_i = d_j/d_i = exp(-S0*C2_j)/exp(-S0*C2_i)   [diag limit]
  Step 3: = exp(-S0*(C2_j - C2_i)); ln(m_j/m_i) = -S0*(C2_j - C2_i)
  Step 4: N_fit = 3 < N_pred ~= 12 => over-constrained by ~9 dof.
  Step 5: m_t/m_u = exp(-S0*(C2_(1,0) - C2_(3,0))) = exp(+S0*14/3) >> 1
          for S0 > 0: heavier REP (larger C2) = deeper freeze = lighter
          fermion; predicted hierarchy direction matches PDG ordering
          iff m_t/m_u_pred > 1 with masses ascending as C2 descends.
          sign_verdict = PASS iff that direction holds in the computed
          spectrum (and the lepton fit ratios are > 1 as ordered).

DIABATIC REGIME WITNESS: P_exc_kz = 1.000, R_therm = 5251.82 >> 1
(canonical), delta_t/T_L = 1.25e-5 << 1 (plan seed) — the freeze-in
amplitude is the Bogoliubov |beta|-weighted production of a deeply
diabatic transit, not an equilibrium Yukawa.

Output 4-tuple:
  (value=<computed>, scheme=FW,
   convention=EPS-LX-BETWEEN-GENERATION-MULTIPLICITY-PDG-POLE,
   L_max=N/A-algebraic-block)

DISCIPLINE
----------
- from canonical_constants import * (lepton/quark/CKM PDG pins added with
  provenance at S100a before this run; m_tau_PDG NOT m_tau=2.062 modulus)
- locals tagged # (local); GPU not needed (3x3 eigh; OMP capped at 8)
- SHA-256 of inputs logged in first 20 lines; S84+ dual-SHA
- verdict PRINTED as emit_verdict payload (race-safe MCP single-writer);
  NO open("a") append; exit 0 on script success regardless of verdict
- W2 npz consumed as 4th pinned input alongside the plan-listed verdict
  file (honest-disclosure, math-scripts.md plan-authorship item 4): the
  |w| seed values live in the npz; the verdict file carries the line.
"""

from __future__ import annotations

# --- CPU thread cap BEFORE numpy import (math-scripts.md; 3x3 CPU path) ---
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first project import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

import hashlib
import json
import re
import time

import numpy as np
from scipy.optimize import least_squares, minimize_scalar
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 2 — Identity + pre-registered machinery pins (plan §W3-9)
# ---------------------------------------------------------------------------
SESSION = "100a"                                                   # (local)
GATE_ID = "S100a-FREEZEIN-OVERCONSTRAINED"                         # (local)
SCHEME = "FW"                                                      # (local)
CONVENTION = "EPS-LX-BETWEEN-GENERATION-MULTIPLICITY-PDG-POLE"     # (local)
L_MAX = "N/A-algebraic-block"                                      # (local)

TOL_QUARK_DEX = 0.5         # (local) plan §W3-9 operator: |log10(pred/PDG)| <= 0.5 (pre-registered gate band)
SIG_TH12_DEG = 0.13         # (local) plan §W3-9 strict_PASS_boundary: 1-sigma band theta12 (pre-registered)
SIG_TH13_DEG = 0.013        # (local) plan §W3-9 strict_PASS_boundary: 1-sigma band theta13 (pre-registered)
SIG_TH23_DEG = 0.4          # (local) plan §W3-9 strict_PASS_boundary: 1-sigma band theta23 (pre-registered)
J_CP_BAND_LO = 2.0e-5       # (local) plan §W3-9 operator: J_CP band lower edge (pre-registered)
J_CP_BAND_HI = 4.0e-5       # (local) plan §W3-9 operator: J_CP band upper edge (pre-registered)
GROSS_OOM = 1.0             # (local) plan dual_prior discriminator: >1 OOM gross miss (pre-registered)
GROSS_NSIG = 3.0            # (local) plan dual_prior discriminator: >3 sigma gross miss (pre-registered)
FIT_TOL = 1e-10             # (local) plan machinery_pin_map tolerance: fit-stage residual (NOT the gate band)
S0_LO, S0_HI = 1.0, 6.0     # (local) plan scan_range: S0 in [1.0, 6.0]
W_LO, W_HI = 0.0, 1.0       # (local) plan scan_range: |w| in [0.0, 1.0]
N_EVAL = 12                 # (local) plan machinery_pin_map N_eval

S0_seed = 3.2               # (local) plan seed; (eps_LX-split)/(horizon kappa) ratio; the FIT re-derives S0
delta_t_over_T_L = 1.25e-5  # (local) diabatic transit-fraction seed witness (plan pin; NOT canonical)

# --- Casimir grading: SU(3) quadratic Casimir, representation-theoretic ---
def C2_su3(p: int, q: int) -> float:
    """SU(3) quadratic Casimir C2(p,q) = (p^2 + q^2 + pq + 3p + 3q)/3."""
    return (p * p + q * q + p * q + 3.0 * p + 3.0 * q) / 3.0


TOWER_PQ = [(1, 0), (1, 1), (3, 0)]                                # (local) plan-pinned triality tower
C2_VEC = np.array([C2_su3(p, q) for (p, q) in TOWER_PQ])           # (local) = [4/3, 3, 6] exact
assert np.allclose(C2_VEC, [4.0 / 3.0, 3.0, 6.0]), "C2 grading mismatch"

# --- PDG targets (all from canonical_constants imports; PDG-POLE-scale) ---
R_MU_E_PDG = m_mu / m_e                                            # (local) 206.7683 charged-lepton fit target 1
R_TAU_MU_PDG = m_tau_PDG / m_mu                                    # (local) 16.8170 charged-lepton fit target 2

QR_LABELS = ["m_u/m_d", "m_c/m_s", "m_t/m_b",
             "m_c/m_u", "m_s/m_d", "m_t/m_c"]                      # (local) 6 gated quark ratios (3 same-gen + 3 cross-gen)
QR_PDG = np.array([
    m_u_msbar_2GeV / m_d_msbar_2GeV,    # 0.4596
    m_c_msbar_mc / m_s_msbar_2GeV,      # 13.615
    m_t_pole / m_b_msbar_mb,            # 41.284
    m_c_msbar_mc / m_u_msbar_2GeV,      # 589.35
    m_s_msbar_2GeV / m_d_msbar_2GeV,    # 19.894
    m_t_pole / m_c_msbar_mc,            # 135.66
])                                                                  # (local) PDG headline-scheme targets
QR_PDG_POLEVAR = np.array([
    m_u_msbar_2GeV / m_d_msbar_2GeV,    # light: MS-bar (no pole exists)
    m_c_pole / m_s_msbar_2GeV,
    m_t_pole / m_b_pole,
    m_c_pole / m_u_msbar_2GeV,
    m_s_msbar_2GeV / m_d_msbar_2GeV,
    m_t_pole / m_c_pole,
])                                                                  # (local) PDG-POLE heavy-quark scheme variant (diagnostic)
R_BS_PDG = m_b_msbar_mb / m_s_msbar_2GeV                            # (local) extra cross-gen ratio (diagnostic, NOT gated)

S13_PDG = V_ub_PDG                                                  # (local) standard-param s13 = |V_ub|
S12_PDG = V_us_PDG / np.sqrt(1.0 - S13_PDG ** 2)                    # (local) s12 = |V_us|/sqrt(1-|V_ub|^2)
S23_PDG = V_cb_PDG / np.sqrt(1.0 - S13_PDG ** 2)                    # (local) s23 = |V_cb|/sqrt(1-|V_ub|^2)
TH12_PDG_DEG = np.degrees(np.arcsin(S12_PDG))                       # (local) 13.00 deg
TH13_PDG_DEG = np.degrees(np.arcsin(S13_PDG))                       # (local) 0.2189 deg
TH23_PDG_DEG = np.degrees(np.arcsin(S23_PDG))                       # (local) 2.339 deg

OUT_NPZ = SESSION_DIR / "s100a_freezein_overconstrained.npz"
OUT_PNG = SESSION_DIR / "s100a_freezein_overconstrained.png"

W2_NPZ = SESSION_DIR / "s100a_yukawa_overlap_offdiag.npz"
VERDICT_FILE = SESSION_DIR / "s100a_gate_verdicts.txt"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    VERDICT_FILE,           # plan input_files: w2_yukawa_overlap_verdict (SOFT)
    W2_NPZ,                 # 4th pinned input: W2 |w| seed data (honest-disclosure)
]


# ---------------------------------------------------------------------------
# Section 3 — SHA-256 input-pin block (S84+ dual-SHA)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    script_bytes = script_path.read_bytes()                        # (local)
    canonical_bytes = canonical_path.read_bytes()                  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"),
                             sort_keys=True).encode("utf-8")       # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 4 — Freeze-in block, masses, CKM
# ---------------------------------------------------------------------------
def freeze_block(S0: float, w_complex: complex, nn_only: bool = False) -> np.ndarray:
    """3x3 Hermitian freeze-in block: diagonal d_i = exp(-S0*C2_i) on the
    sector order (1,0)/(1,1)/(3,0); one shared off-diagonal w on every
    generation pairing (D1). nn_only=True is the V3 diagnostic variant
    (w_13 = 0, nearest-neighbor pairings only)."""
    d = np.exp(-S0 * C2_VEC)                                       # (local) diagonal diabatic amplitudes
    M = np.diag(d).astype(complex)                                 # (local)
    pairs = [(0, 1), (1, 2)] if nn_only else [(0, 1), (1, 2), (0, 2)]  # (local)
    for i, j in pairs:
        M[i, j] = w_complex
        M[j, i] = np.conj(w_complex)
    return M


def masses_and_basis(M: np.ndarray):
    """Eigen-decompose Hermitian M; return (|lam| ascending, signed lam,
    eigenvector columns) ordered by ascending |lam| (= ascending mass;
    S96 ascending-mass flavor-basis convention)."""
    lam, U = np.linalg.eigh(M)                                     # (local)
    order = np.argsort(np.abs(lam))                                # (local)
    return np.abs(lam)[order], lam[order], U[:, order]


def lepton_ratios(S0: float, w_abs: float, lep_sign: float = -1.0):
    """Charged-lepton mass ratios (m_mu/m_e, m_tau/m_mu) of the lepton
    block at the self-conjugate Z3 point w_lep = lep_sign*|w| (D3;
    canonical lep_sign = -1 = e^{i pi}, the W2 seed point)."""
    m, _, _ = masses_and_basis(freeze_block(S0, lep_sign * w_abs))  # (local)
    return m[1] / m[0], m[2] / m[1]


def lepton_resid(x, lep_sign: float = -1.0):
    S0, u = x                                                      # (local) u = log10(|w|)
    r12, r23 = lepton_ratios(S0, 10.0 ** u, lep_sign)              # (local)
    return [np.log(r12 / R_MU_E_PDG), np.log(r23 / R_TAU_MU_PDG)]


def fit_leptons(lep_sign: float = -1.0):
    """Stage A: deterministic multi-start least_squares for {S0, |w|}.
    Returns (S0, w_abs, max|res|, n_roots_found, all_roots)."""
    starts = []  # (local)
    for s0 in np.linspace(S0_LO + 0.2, S0_HI - 0.2, 6):
        for u in [-6.0, -5.0, -4.0, -3.0, -2.0, -1.0, -0.3]:
            starts.append((s0, u))
    roots = []  # (local)
    for x0 in starts:
        try:
            sol = least_squares(lepton_resid, x0, args=(lep_sign,),
                                bounds=([S0_LO, -12.0], [S0_HI, 0.0]),
                                xtol=3e-16, ftol=3e-16, gtol=3e-16,
                                x_scale="jac", max_nfev=2000)      # (local)
        except Exception:
            continue
        res_max = float(np.max(np.abs(sol.fun)))                   # (local)
        if res_max < 1e-8:
            roots.append((float(sol.x[0]), 10.0 ** float(sol.x[1]), res_max))
    # dedupe (S0, w) to 6 decimals
    uniq = []  # (local)
    for r in sorted(roots, key=lambda t: t[1]):
        if not any(abs(r[0] - q[0]) < 1e-6 and abs(r[1] - q[1]) / max(q[1], 1e-30) < 1e-4
                   for q in uniq):
            uniq.append(r)
    if not uniq:
        return np.nan, np.nan, np.inf, 0, []
    best = uniq[0]  # (local) D5: smallest-|w| diagonal-dominant branch
    return best[0], best[1], best[2], len(uniq), uniq


def ckm_from(S0: float, w_abs: float, theta: float, nn_only: bool = False):
    """Quark towers (D3/D4): M_u at w_u = |w| e^{+i theta}, M_d = M_u*
    (J-conjugate). Returns (V, m_up, m_down, lam_up, lam_down)."""
    wu = w_abs * np.exp(1j * theta)                                # (local)
    Mu = freeze_block(S0, wu, nn_only)                             # (local)
    Md = freeze_block(S0, np.conj(wu), nn_only)                    # (local)
    mu_, lamu, Uu = masses_and_basis(Mu)                           # (local)
    md_, lamd, Ud = masses_and_basis(Md)                           # (local)
    V = Uu.conj().T @ Ud                                           # (local) V_CKM = U_up^dag U_down
    return V, mu_, md_, lamu, lamd


def ckm_angles_J(V: np.ndarray):
    """Standard-parametrization angles (deg) + Jarlskog from a unitary V."""
    s13 = abs(V[0, 2])                                             # (local)
    c13 = np.sqrt(max(1.0 - s13 ** 2, 0.0))                        # (local)
    s12 = abs(V[0, 1]) / c13 if c13 > 0 else 0.0                   # (local)
    s23 = abs(V[1, 2]) / c13 if c13 > 0 else 0.0                   # (local)
    th = [np.degrees(np.arcsin(min(s, 1.0))) for s in (s12, s13, s23)]  # (local)
    J = float(np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1])))  # (local)
    return th[0], th[1], th[2], J


def vus_of_theta(S0: float, w_abs: float, theta: float) -> float:
    V, _, _, _, _ = ckm_from(S0, w_abs, theta)                     # (local)
    return abs(V[0, 1])


def fit_theta(S0: float, w_abs: float):
    """Stage B: arg(w) from |V_us| anchor. Dense deterministic grid +
    bounded refine; the +-theta branches are |V_us|-degenerate, primary
    branch theta >= 0."""
    grid = np.linspace(0.0, np.pi, 4097)                           # (local) theta>=0 branch (degeneracy exact)
    vus = np.array([vus_of_theta(S0, w_abs, t) for t in grid])     # (local)
    k = int(np.argmin(np.abs(vus - V_us_PDG)))                     # (local)
    lo = grid[max(k - 1, 0)]                                       # (local)
    hi = grid[min(k + 1, len(grid) - 1)]                           # (local)
    ref = minimize_scalar(lambda t: (vus_of_theta(S0, w_abs, t) - V_us_PDG) ** 2,
                          bounds=(lo, hi), method="bounded",
                          options={"xatol": 1e-14})                # (local)
    theta_star = float(ref.x)                                      # (local)
    vus_star = vus_of_theta(S0, w_abs, theta_star)                 # (local)
    kmax = int(np.argmax(vus))                                     # (local)
    refmax = minimize_scalar(lambda t: -vus_of_theta(S0, w_abs, t),
                             bounds=(grid[max(kmax - 1, 0)], grid[min(kmax + 1, len(grid) - 1)]),
                             method="bounded", options={"xatol": 1e-14})  # (local)
    vus_max = -float(refmax.fun)                                   # (local)
    theta_at_max = float(refmax.x)                                 # (local)
    return theta_star, vus_star, vus_max, theta_at_max, grid, vus


# ---------------------------------------------------------------------------
# Section 5 — Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    out = {}  # (local)

    # ---- diabatic regime witnesses (canonical pins) ----
    print("--- diabatic regime witnesses ---")
    print(f"  P_exc_kz = {P_exc_kz}  (Kibble-Zurek saturated excitation)")
    print(f"  R_therm  = {R_therm}  (>> 1: transit-freeze, no thermalization)")
    print(f"  delta_t/T_L = {delta_t_over_T_L}  (<< 1: deep-sudden; plan seed)")
    regime_witness_ok = (abs(P_exc_kz - 1.0) < 1e-12) and (R_therm > 100.0)  # (local)

    # ---- W2 seed (SOFT input; branch (a) of the plan prereq table) ----
    w2_present = W2_NPZ.exists()  # (local)
    w_seed_abs, w_seed_args = np.nan, np.array([np.nan])           # (local)
    if w2_present:
        with np.load(W2_NPZ, allow_pickle=True) as z:
            w_seed_abs = float(np.atleast_1d(z["abs_w_phi"])[0])   # (local) 0.408248 = 1/sqrt(6)
            w_seed_args = np.array(z["arg_w_M2_phi"], dtype=float) # (local) {pi, +2pi/3, -2pi/3}
    verdict_text = VERDICT_FILE.read_text(encoding="utf-8", errors="replace")  # (local)
    w2_line_present = bool(re.search(r"^S100a-YUKAWA-OVERLAP-OFFDIAG:", verdict_text, re.M))  # (local)
    print(f"--- W2 seed: npz_present={w2_present} verdict_line={w2_line_present} "
          f"|w|_seed={w_seed_abs:.6f} args={np.round(w_seed_args, 6)}")

    # ---- Stage A: lepton fit {S0, |w|} (canonical lep_sign = -1, D3) ----
    S0_fit, w_fit, res_max, n_roots, roots = fit_leptons(lep_sign=-1.0)  # (local)
    print("--- Stage A (lepton fit, w_lep = -|w| self-conjugate Z3 point) ---")
    print(f"  targets: m_mu/m_e = {R_MU_E_PDG:.6f}, m_tau/m_mu = {R_TAU_MU_PDG:.6f}")
    print(f"  S0_fit = {S0_fit:.6f}, |w|_fit = {w_fit:.6e}, max|res| = {res_max:.3e}, roots = {n_roots}")
    for r in roots:
        print(f"    root: S0={r[0]:.6f} |w|={r[1]:.6e} res={r[2]:.2e}")
    fit_converged = res_max < FIT_TOL                              # (local)
    print(f"  fit_converged (max|res| < {FIT_TOL}): {fit_converged}")

    r12_fit, r23_fit = lepton_ratios(S0_fit, w_fit, -1.0)          # (local)
    m_lep, lam_lep, _ = masses_and_basis(freeze_block(S0_fit, -w_fit))  # (local)

    # variant V2 (diagnostic): lepton sign +|w|
    S0_v2, w_v2, res_v2, n_v2, _ = fit_leptons(lep_sign=+1.0)      # (local)
    print(f"  [V2 diag, w_lep=+|w|]: S0={S0_v2:.6f} |w|={w_v2:.6e} res={res_v2:.2e}")

    # diagonal-limit cross-check (per-leg S0; substitution chain step 3)
    S0_leg_mue = np.log(R_MU_E_PDG) / (C2_VEC[2] - C2_VEC[1])      # (local) ln(206.77)/3 = 1.7773
    S0_leg_taumu = np.log(R_TAU_MU_PDG) / (C2_VEC[1] - C2_VEC[0])  # (local) ln(16.82)/(5/3) = 1.6931
    print(f"  diag-limit legs: S0(mu/e)={S0_leg_mue:.6f}, S0(tau/mu)={S0_leg_taumu:.6f} "
          f"(5% spread closed by |w|)")

    # ---- Stage B: theta fit to |V_us| ----
    theta_fit, vus_fit, vus_max, theta_at_max, th_grid, vus_grid = fit_theta(S0_fit, w_fit)  # (local)
    anchor_reachable = abs(vus_max - V_us_PDG) >= 0.0 and vus_max >= V_us_PDG - V_us_sigma_PDG  # (local)
    print("--- Stage B (theta fit to |V_us|) ---")
    print(f"  anchor |V_us| = {V_us_PDG} +/- {V_us_sigma_PDG}")
    print(f"  theta_fit = {theta_fit:.6f} rad, |V_us|(theta_fit) = {vus_fit:.6f}")
    print(f"  max reachable |V_us| = {vus_max:.6f} at theta = {theta_at_max:.6f}")
    print(f"  anchor_reachable_within_1sigma = {anchor_reachable}")

    # ---- Predict stage: quark masses + CKM (zero further freedom) ----
    V, m_up, m_dn, lam_up, lam_dn = ckm_from(S0_fit, w_fit, theta_fit)  # (local)
    th12, th13, th23, J = ckm_angles_J(V)                          # (local)
    # theta -> -theta branch: V -> V*, J -> -J (verified below)
    V_m, m_up_m, m_dn_m, _, _ = ckm_from(S0_fit, w_fit, -theta_fit)  # (local)
    _, _, _, J_minus = ckm_angles_J(V_m)                           # (local)
    branch_check = abs(J + J_minus) < 1e-18 + 1e-9 * abs(J)        # (local)

    unitarity_dev = float(np.max(np.abs(V @ V.conj().T - np.eye(3))))  # (local)
    spec_conj_dev = float(np.max(np.abs(m_up - m_dn) / np.maximum(m_up, 1e-300)))  # (local) M_d=M_u* identity

    # same-generation ratios (D4: Lambda_u = Lambda_d, structural)
    r_ud_pred = m_up[0] / m_dn[0]                                  # (local)
    r_cs_pred = m_up[1] / m_dn[1]                                  # (local)
    r_tb_pred = m_up[2] / m_dn[2]                                  # (local)
    # cross-generation ratios
    r_cu_pred = m_up[1] / m_up[0]                                  # (local)
    r_sd_pred = m_dn[1] / m_dn[0]                                  # (local)
    r_tc_pred = m_up[2] / m_up[1]                                  # (local)
    r_bs_pred = m_dn[2] / m_dn[1]                                  # (local) extra diagnostic
    qr_pred = np.array([r_ud_pred, r_cs_pred, r_tb_pred,
                        r_cu_pred, r_sd_pred, r_tc_pred])          # (local)

    print("--- Predict stage ---")
    print(f"  quark ratios pred: {dict(zip(QR_LABELS, np.round(qr_pred, 6)))}")
    print(f"  quark ratios PDG : {dict(zip(QR_LABELS, np.round(QR_PDG, 4)))}")
    print(f"  CKM angles pred (deg): th12={th12:.6f} th13={th13:.6f} th23={th23:.6f}")
    print(f"  CKM angles PDG  (deg): th12={TH12_PDG_DEG:.4f} th13={TH13_PDG_DEG:.4f} th23={TH23_PDG_DEG:.4f}")
    print(f"  J_CP pred = {J:.6e} (branch-degenerate +-; PDG {J_CP_PDG:.3e}, band [{J_CP_BAND_LO},{J_CP_BAND_HI}])")
    print(f"  unitarity dev = {unitarity_dev:.3e}; up/down spectrum conj identity dev = {spec_conj_dev:.3e}")
    print(f"  J branch antisymmetry check (J(+th)=-J(-th)): {branch_check}")

    # ---- limits cross-checks (Bogoliubov discipline) ----
    m_w0, _, _ = masses_and_basis(freeze_block(S0_fit, 1e-12 + 0j))  # (local) w->0 diagonal limit
    diag_r12 = np.exp(S0_fit * (C2_VEC[2] - C2_VEC[1]))            # (local)
    diag_r23 = np.exp(S0_fit * (C2_VEC[1] - C2_VEC[0]))            # (local)
    lim_dev = max(abs(m_w0[1] / m_w0[0] / diag_r12 - 1.0),
                  abs(m_w0[2] / m_w0[1] / diag_r23 - 1.0))         # (local)
    V0, _, _, _, _ = ckm_from(S0_fit, 1e-12, theta_fit)            # (local)
    ckm_id_dev = float(np.max(np.abs(np.abs(V0) - np.eye(3))))     # (local) w->0: V -> identity
    print(f"  [limit] w->0 ratio dev = {lim_dev:.3e}; w->0 |V|-I dev = {ckm_id_dev:.3e}")

    # ---- V3 diagnostic variant: nearest-neighbor only ----
    V_nn, m_up_nn, m_dn_nn, _, _ = ckm_from(S0_fit, w_fit, theta_fit, nn_only=True)  # (local)
    th12_nn, th13_nn, th23_nn, J_nn = ckm_angles_J(V_nn)           # (local)
    print(f"  [V3 diag, nn-only]: th12={th12_nn:.4f} th13={th13_nn:.6f} th23={th23_nn:.4f} J={J_nn:.3e}")

    # ---- per-observable bands (the 12-slot vector, pre-declared) ----
    labels = ["m_mu/m_e(fit)", "m_tau/m_mu(fit)", "theta12(anchor)",
              "m_u/m_d", "m_c/m_s", "m_t/m_b", "m_c/m_u", "m_s/m_d", "m_t/m_c",
              "theta13", "theta23", "J_CP"]                        # (local)
    pred_vals = np.array([r12_fit, r23_fit, th12,
                          *qr_pred, th13, th23, abs(J)])           # (local)
    pdg_vals = np.array([R_MU_E_PDG, R_TAU_MU_PDG, TH12_PDG_DEG,
                         *QR_PDG, TH13_PDG_DEG, TH23_PDG_DEG, J_CP_PDG])  # (local)

    dev_dex = np.abs(np.log10(pred_vals / pdg_vals))               # (local) ratio-type deviations
    per_obs_pass = np.zeros(12, dtype=bool)                        # (local)
    per_obs_pass[0] = dev_dex[0] <= TOL_QUARK_DEX
    per_obs_pass[1] = dev_dex[1] <= TOL_QUARK_DEX
    per_obs_pass[2] = abs(th12 - TH12_PDG_DEG) <= SIG_TH12_DEG
    for k in range(6):
        per_obs_pass[3 + k] = dev_dex[3 + k] <= TOL_QUARK_DEX
    per_obs_pass[9] = abs(th13 - TH13_PDG_DEG) <= SIG_TH13_DEG
    per_obs_pass[10] = abs(th23 - TH23_PDG_DEG) <= SIG_TH23_DEG
    per_obs_pass[11] = (J_CP_BAND_LO <= abs(J) <= J_CP_BAND_HI)

    # pole-scheme variant flips (diagnostic)
    dev_dex_pole = np.abs(np.log10(qr_pred / QR_PDG_POLEVAR))      # (local)
    pole_flips = int(np.sum((dev_dex_pole <= TOL_QUARK_DEX)
                            != (dev_dex[3:9] <= TOL_QUARK_DEX)))   # (local)

    nsig = np.array([abs(th12 - TH12_PDG_DEG) / SIG_TH12_DEG,
                     abs(th13 - TH13_PDG_DEG) / SIG_TH13_DEG,
                     abs(th23 - TH23_PDG_DEG) / SIG_TH23_DEG])     # (local)

    mass_group_pass = bool(np.all(per_obs_pass[3:9]))              # (local)
    mixing_group_pass = bool(per_obs_pass[2] and np.all(per_obs_pass[9:12]))  # (local)
    gross_ratio = bool(np.any(dev_dex[3:9] > GROSS_OOM))           # (local)
    gross_angle = bool(np.any(nsig > GROSS_NSIG))                  # (local)
    gross_J = bool(abs(np.log10(max(abs(J), 1e-300) / J_CP_PDG)) > GROSS_OOM)  # (local)
    gross_miss = gross_ratio or gross_angle or gross_J             # (local)

    print("--- per-observable bands ---")
    for i, lab in enumerate(labels):
        if i in (2, 9, 10):
            band = {2: SIG_TH12_DEG, 9: SIG_TH13_DEG, 10: SIG_TH23_DEG}[i]  # (local)
            print(f"  [{i:2d}] {lab:16s} pred={pred_vals[i]:12.6g} PDG={pdg_vals[i]:12.6g} "
                  f"|d|={abs(pred_vals[i]-pdg_vals[i]):.4g} deg (band {band}) -> {'PASS' if per_obs_pass[i] else 'FAIL'}")
        elif i == 11:
            print(f"  [{i:2d}] {lab:16s} pred={pred_vals[i]:12.6g} PDG={pdg_vals[i]:12.6g} "
                  f"band [{J_CP_BAND_LO},{J_CP_BAND_HI}] -> {'PASS' if per_obs_pass[i] else 'FAIL'}")
        else:
            print(f"  [{i:2d}] {lab:16s} pred={pred_vals[i]:12.6g} PDG={pdg_vals[i]:12.6g} "
                  f"dev={dev_dex[i]:.4f} dex (band {TOL_QUARK_DEX}) -> {'PASS' if per_obs_pass[i] else 'FAIL'}")
    print(f"  mass_group(6 quark ratios) all-pass: {mass_group_pass} "
          f"({int(np.sum(per_obs_pass[3:9]))}/6)")
    print(f"  mixing_group(th12,th13,th23,J) all-pass: {mixing_group_pass} "
          f"({int(per_obs_pass[2]) + int(np.sum(per_obs_pass[9:12]))}/4)")
    print(f"  gross_miss(>1 OOM / >3sigma): {gross_miss} "
          f"(ratio:{gross_ratio} angle:{gross_angle} J:{gross_J})")
    print(f"  pole-scheme variant band flips: {pole_flips}/6 (diagnostic)")

    # ---- [SIGN] 3-tuple ----
    mt_over_mu_pred = m_up[2] / m_up[0]                            # (local) substitution-chain step 5
    hierarchy_dir_ok = (mt_over_mu_pred > 1.0) and (r12_fit > 1.0) and (r23_fit > 1.0)  # (local)
    sign_verdict = "PASS" if hierarchy_dir_ok else "FAIL"          # (local)

    if mass_group_pass and mixing_group_pass:
        magnitude_verdict = "PASS"                                 # (local)
    elif mass_group_pass != mixing_group_pass:
        magnitude_verdict = "INFO"                                 # (local)
    else:
        magnitude_verdict = "FAIL"                                 # (local)

    in_domain = (S0_LO < S0_fit < S0_HI) and (W_LO < w_fit < W_HI) and (-np.pi <= theta_fit <= np.pi)  # (local)
    if fit_converged and regime_witness_ok and in_domain:
        regime_verdict = "VALID"                                   # (local)
    elif fit_converged and regime_witness_ok:
        regime_verdict = "MARGINAL"                                # (local)
    else:
        regime_verdict = "BREAKDOWN"                               # (local)

    # composite collapse rule (gate-verdicts.md, pre-registered)
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"                                         # (local)
    elif sign_verdict == "FAIL":
        composite = "FAIL"                                         # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"                                         # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"                                         # (local)
    elif magnitude_verdict == "INFO":
        composite = "INFO"                                         # (local)
    else:
        composite = "PASS"                                         # (local)

    print("--- [SIGN] 3-tuple ---")
    print(f"  sign_verdict={sign_verdict} (m_t/m_u_pred={mt_over_mu_pred:.4g} >> 1, C2-ordered)")
    print(f"  magnitude_verdict={magnitude_verdict} regime_verdict={regime_verdict}")
    print(f"  composite={composite}")

    # ---- dual-prior posterior (plan discriminator) ----
    if composite == "PASS":
        track_note = "trackA_0.90"                                 # (local)
    elif composite == "FAIL":
        track_note = "trackB_0.90"                                 # (local)
    else:
        track_note = "tracks_unchanged_0.45_0.55"                  # (local)

    # ---- seed_vs_fit_agreement (W2 present branch) ----
    if w2_present and np.isfinite(w_seed_abs):
        w_ratio = w_fit / w_seed_abs                               # (local)
        dth = np.abs(np.angle(np.exp(1j * (theta_fit - w_seed_args))))  # (local) wrapped
        dtheta_min = float(np.min(dth))                            # (local)
        seed_vs_fit_agreement = np.array([w_ratio, dtheta_min])    # (local)
    else:
        seed_vs_fit_agreement = np.array([np.nan, np.nan])         # (local)
    print(f"--- seed_vs_fit (diagnostic, NOT a gate): |w|_fit/|w|_seed = {seed_vs_fit_agreement[0]:.4e}, "
          f"min|dtheta| = {seed_vs_fit_agreement[1]:.4f} rad")

    # ---- value payload (no single quotes) ----
    worst_idx = int(np.argmax(np.where(np.arange(12) >= 3,
                                       np.where(np.arange(12) <= 8, dev_dex, 0.0), 0.0)))  # (local)
    value = (f"S0={S0_fit:.4f};|w|={w_fit:.4e};argw={theta_fit:+.4f};"
             f"Vus_fit={vus_fit:.4f}_vs_{V_us_PDG}(max_reach={vus_max:.4f});"
             f"mass_grp={int(np.sum(per_obs_pass[3:9]))}/6;mix_grp={int(per_obs_pass[2]) + int(np.sum(per_obs_pass[9:12]))}/4;"
             f"npass={int(np.sum(per_obs_pass))}/12;"
             f"worst_ratio={labels[worst_idx]}_dev{dev_dex[worst_idx]:.2f}dex;"
             f"th12={th12:.2f}deg_{nsig[0]:.1f}sig;th23={th23:.2f}deg_{nsig[2]:.1f}sig;"
             f"J=+-{abs(J):.2e};gross={gross_miss};"
             f"updown_spec_conj_identity_dev={spec_conj_dev:.1e};"
             f"seedvsfit_w={seed_vs_fit_agreement[0]:.2e};{track_note}")  # (local)

    out.update(dict(
        S0_fit=S0_fit, w_abs_fit=w_fit, arg_w_fit=theta_fit,
        quark_ratio_pred=qr_pred, ckm_angle_pred=np.array([th12, th13, th23]),
        J_CP_pred=J, per_obs_pass=per_obs_pass, S0_seed=S0_seed,
        seed_vs_fit_agreement=seed_vs_fit_agreement,
        labels=np.array(labels), pred_vals=pred_vals, pdg_vals=pdg_vals,
        dev_dex=dev_dex, nsig_angles=nsig,
        quark_ratio_pdg=QR_PDG, quark_ratio_pdg_polevar=QR_PDG_POLEVAR,
        dev_dex_polevar=dev_dex_pole, pole_scheme_band_flips=pole_flips,
        r_bs_pred=r_bs_pred, r_bs_pdg=R_BS_PDG,
        ckm_angle_pdg=np.array([TH12_PDG_DEG, TH13_PDG_DEG, TH23_PDG_DEG]),
        ckm_sigma_plan=np.array([SIG_TH12_DEG, SIG_TH13_DEG, SIG_TH23_DEG]),
        J_CP_band=np.array([J_CP_BAND_LO, J_CP_BAND_HI]), J_CP_pdg=J_CP_PDG,
        V_abs=np.abs(V), V_real=np.real(V), V_imag=np.imag(V),
        unitarity_dev=unitarity_dev, spec_conj_dev=spec_conj_dev,
        m_lep=m_lep, lam_lep=lam_lep, m_up=m_up, m_dn=m_dn,
        lam_up=lam_up, lam_dn=lam_dn,
        lepton_fit_resid_max=res_max, lepton_fit_nroots=n_roots,
        lepton_roots=np.array([(r[0], r[1], r[2]) for r in roots]) if roots else np.zeros((0, 3)),
        S0_leg_mue=S0_leg_mue, S0_leg_taumu=S0_leg_taumu,
        S0_v2=S0_v2, w_v2=w_v2, res_v2=res_v2,
        vus_fit=vus_fit, vus_max_reachable=vus_max, theta_at_vus_max=theta_at_max,
        anchor_reachable=anchor_reachable,
        theta_grid=th_grid, vus_grid=vus_grid,
        ckm_nn_variant=np.array([th12_nn, th13_nn, th23_nn, J_nn]),
        limit_w0_ratio_dev=lim_dev, limit_w0_ckm_dev=ckm_id_dev,
        J_branch_antisym_ok=branch_check, J_minus_branch=J_minus,
        mass_group_pass=mass_group_pass, mixing_group_pass=mixing_group_pass,
        gross_miss=gross_miss, gross_ratio=gross_ratio, gross_angle=gross_angle, gross_J=gross_J,
        mt_over_mu_pred=mt_over_mu_pred,
        C2_vec=C2_VEC, tower_pq=np.array(TOWER_PQ),
        R_mu_e_pdg=R_MU_E_PDG, R_tau_mu_pdg=R_TAU_MU_PDG,
        P_exc_kz_used=P_exc_kz, R_therm_used=R_therm,
        delta_t_over_T_L_seed=delta_t_over_T_L,
        w2_seed_abs=w_seed_abs, w2_seed_args=w_seed_args,
        w2_npz_present=w2_present, w2_verdict_line_present=w2_line_present,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict, verdict=composite,
        value=value, track_note=track_note,
        N_fit=3, N_eval=N_EVAL,
    ))
    return out


# ---------------------------------------------------------------------------
# Section 6 — Plot
# ---------------------------------------------------------------------------
def make_plot(r: dict) -> None:
    fig = plt.figure(figsize=(15, 10))                             # (local)
    gs = fig.add_gridspec(2, 2, hspace=0.32, wspace=0.26)          # (local)

    # (a) predicted vs PDG, ratio-type observables (log-log)
    ax = fig.add_subplot(gs[0, 0])                                 # (local)
    idx_r = [0, 1, 3, 4, 5, 6, 7, 8]                               # (local)
    x = r["pdg_vals"][idx_r]                                       # (local)
    y = np.maximum(r["pred_vals"][idx_r], 1e-12)                   # (local)
    span = np.array([1e-1, 1e3])                                   # (local)
    ax.fill_between(span, span * 10 ** -0.5, span * 10 ** 0.5,
                    color="tab:green", alpha=0.15, label="±0.5 dex band")
    ax.plot(span, span, "k--", lw=0.8)
    cols = ["tab:blue" if i < 2 else "tab:red" for i in range(len(idx_r))]  # (local)
    ax.scatter(x, y, c=cols, s=60, zorder=3)
    for xi, yi, lab in zip(x, y, r["labels"][idx_r]):
        ax.annotate(str(lab), (xi, yi), fontsize=7, xytext=(4, 4),
                    textcoords="offset points")
    ax.set_xscale("log"); ax.set_yscale("log")
    ax.set_xlim(span); ax.set_ylim(1e-1, 1e3)
    ax.set_xlabel("PDG ratio"); ax.set_ylabel("predicted ratio")
    ax.set_title("(a) mass ratios: fit (blue) + held-out (red) vs PDG")
    ax.legend(fontsize=8)

    # (b) normalized deviations
    ax = fig.add_subplot(gs[0, 1])                                 # (local)
    norm_dev = np.empty(12)                                        # (local)
    for i in range(12):
        if i in (2, 9, 10):
            s = {2: r["ckm_sigma_plan"][0], 9: r["ckm_sigma_plan"][1],
                 10: r["ckm_sigma_plan"][2]}[i]                    # (local)
            norm_dev[i] = abs(r["pred_vals"][i] - r["pdg_vals"][i]) / s
        elif i == 11:
            jv = max(abs(r["J_CP_pred"]), 1e-300)                  # (local)
            norm_dev[i] = abs(np.log10(jv / r["J_CP_pdg"])) / 0.11  # band half-width in dex ~0.11
        else:
            norm_dev[i] = r["dev_dex"][i] / 0.5
    colors = ["tab:green" if p else "tab:red" for p in r["per_obs_pass"]]  # (local)
    ax.barh(np.arange(12), np.maximum(norm_dev, 1e-3), color=colors)
    ax.axvline(1.0, color="k", ls="--", lw=1, label="band edge")
    ax.set_yticks(np.arange(12)); ax.set_yticklabels([str(s) for s in r["labels"]], fontsize=8)
    ax.set_xscale("log"); ax.set_xlabel("|deviation| / band")
    ax.set_title("(b) per-observable deviation vs pre-registered band")
    ax.invert_yaxis(); ax.legend(fontsize=8)

    # (c) |V_us|(theta) sweep
    ax = fig.add_subplot(gs[1, 0])                                 # (local)
    ax.plot(r["theta_grid"], r["vus_grid"], "b-", lw=1.2, label="|V_us|(θ) model")
    ax.axhline(V_us_PDG, color="k", ls="--", lw=1, label=f"PDG anchor {V_us_PDG}")
    ax.axhspan(V_us_PDG - V_us_sigma_PDG, V_us_PDG + V_us_sigma_PDG,
               color="k", alpha=0.12)
    ax.plot([r["arg_w_fit"]], [r["vus_fit"]], "r*", ms=14,
            label=f"fit θ*={r['arg_w_fit']:.3f}, |V_us|={r['vus_fit']:.4f}")
    ax.set_xlabel("θ = arg(w) [rad]"); ax.set_ylabel("|V_us|")
    ax.set_title("(c) Stage-B anchor: |V_us| reachability over θ ∈ [0, π]")
    ax.legend(fontsize=8)

    # (d) summary text
    ax = fig.add_subplot(gs[1, 1]); ax.axis("off")                 # (local)
    txt = (
        f"{GATE_ID}\n"
        f"composite = {r['verdict']}   [sign={r['sign_verdict']} "
        f"mag={r['magnitude_verdict']} regime={r['regime_verdict']}]\n\n"
        f"fit (3 real inputs):\n"
        f"  S0 = {r['S0_fit']:.4f}   |w| = {r['w_abs_fit']:.4e}\n"
        f"  arg(w) = {r['arg_w_fit']:+.4f} rad  (|V_us| anchor"
        f"{'' if r['anchor_reachable'] else ' UNREACHABLE'})\n"
        f"  max|V_us| reachable = {r['vus_max_reachable']:.4f} vs {V_us_PDG}\n\n"
        f"held-out: mass {int(np.sum(r['per_obs_pass'][3:9]))}/6, "
        f"mixing {int(r['per_obs_pass'][2]) + int(np.sum(r['per_obs_pass'][9:12]))}/4, "
        f"total {int(np.sum(r['per_obs_pass']))}/12\n"
        f"gross miss (>1 OOM / >3σ): {r['gross_miss']}\n"
        f"up/down spectrum conj-identity dev: {r['spec_conj_dev']:.1e}\n"
        f"J_CP = ±{abs(r['J_CP_pred']):.2e}  (band [2e-5, 4e-5])\n\n"
        f"seed_vs_fit (W2, diagnostic): |w|_fit/|w|_seed = "
        f"{r['seed_vs_fit_agreement'][0]:.2e}\n"
        f"  min|Δθ| vs Z3 = {r['seed_vs_fit_agreement'][1]:.3f} rad\n"
        f"S0 diag-legs: {r['S0_leg_mue']:.4f} (μ/e), {r['S0_leg_taumu']:.4f} (τ/μ)\n"
        f"regime: P_exc={r['P_exc_kz_used']:.3f}, R_therm={r['R_therm_used']:.1f}\n"
        f"{r['track_note']}"
    )                                                              # (local)
    ax.text(0.02, 0.98, txt, va="top", ha="left", fontsize=10, family="monospace")
    fig.suptitle("S100a W3-9 — transit squeezed-vacuum freeze-in: over-constrained flavor predictor test",
                 fontsize=13)
    fig.savefig(OUT_PNG, dpi=140, bbox_inches="tight")
    plt.close(fig)
    print(f"  plot -> {OUT_PNG.name}")


# ---------------------------------------------------------------------------
# Section 7 — Verdict payload + main
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="",
                          extra_rows=None) -> dict:
    """Print the emit_verdict payload (race-safe MCP single-writer path).
    The script does NOT write the verdict file."""
    payload = {                                                    # (local)
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


def main() -> int:
    t0 = time.time()                                               # (local)

    pins = log_input_pins(INPUT_FILES)                             # (local)
    script_path = Path(__file__).resolve()                         # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"         # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    r = compute()                                                  # (local)

    make_plot(r)

    # save npz (REQUIRED keys: S0_fit, w_abs_fit, arg_w_fit, quark_ratio_pred,
    # ckm_angle_pred, J_CP_pred, per_obs_pass, S0_seed, seed_vs_fit_agreement)
    npz_payload = {k: v for k, v in r.items()}                     # (local)
    npz_payload["audit_sha256"] = audit_sha
    npz_payload["content_sha256"] = content_sha
    npz_payload["gate_id"] = GATE_ID
    npz_payload["scheme"] = SCHEME
    npz_payload["convention"] = CONVENTION
    npz_payload["l_max"] = L_MAX
    npz_payload["schema_version"] = "S84+"
    np.savez(OUT_NPZ, **npz_payload)
    print(f"  data -> {OUT_NPZ.name}")

    tag = emit_4tuple(r["value"], SCHEME, CONVENTION, L_MAX)       # (local)
    print(tag)

    companion = ("3 real inputs {S0,|w|,arg w} vs 12-slot held-out set; "
                 "structure D1-D5 pre-declared (S99 panel + W2 Z3 + plan step-5 C2-ordered sign); "
                 f"Lambda_u=Lambda_d J-locked; up/down conj-spectrum identity dev {r['spec_conj_dev']:.1e}")  # (local)
    extra = [
        ("# regulator_pin=N/A (C2(p,q) = SU(3) quadratic Casimir, representation-theoretic; "
         f"no Seeley-DeWitt a_n consumed) # {GATE_ID}"),
        (f"# fit: S0_fit={r['S0_fit']:.6f} |w|_fit={r['w_abs_fit']:.6e} argw_fit={r['arg_w_fit']:+.6f} "
         f"resid_max={r['lepton_fit_resid_max']:.2e} nroots={r['lepton_fit_nroots']} "
         f"diag-legs S0(mu/e)={r['S0_leg_mue']:.4f} S0(tau/mu)={r['S0_leg_taumu']:.4f}; "
         f"Vus_max_reachable={r['vus_max_reachable']:.4f} anchor_reachable={r['anchor_reachable']} # {GATE_ID}"),
        (f"# seed_vs_fit(W2 |w|=1/sqrt6, argZ3): w_ratio={r['seed_vs_fit_agreement'][0]:.3e} "
         f"min_dtheta={r['seed_vs_fit_agreement'][1]:.4f} rad (diagnostic, NOT a gate); "
         f"S0_seed=3.2 fit-seed only; variants: V2(+|w| lepton) S0={r['S0_v2']:.4f}, "
         f"V3(nn-only) th12={r['ckm_nn_variant'][0]:.4f}deg # {GATE_ID}"),
        (f"# diabatic regime: P_exc_kz={r['P_exc_kz_used']:.3f} R_therm={r['R_therm_used']:.2f} "
         f"delta_t/T_L=1.25e-5 (deep-sudden; Bogoliubov production not equilibrium Yukawa) # {GATE_ID}"),
    ]                                                              # (local)

    print_verdict_payload(r["verdict"], r["value"], audit_sha, content_sha,
                          sign_verdict=r["sign_verdict"],
                          magnitude_verdict=r["magnitude_verdict"],
                          regime_verdict=r["regime_verdict"],
                          companion_note=companion,
                          extra_rows=extra)

    wall = time.time() - t0                                        # (local)
    print(f"\n=== {GATE_ID}: {r['verdict']} (wall {wall:.1f}s) ===")
    # exit 0 on script success regardless of scientific verdict
    # (math-scripts.md "Exit Codes and Verdict Semantics")
    return 0


if __name__ == "__main__":
    sys.exit(main())
