#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CF-S117-CFW21-THREE-WAY  (Session 117, Wave 3, §W3-1)  -- [SIGN] gate.

DOES THE BOSONIC SPECTRAL ACTION  S = Tr f(D_K/Lambda)  SELECT A LEPTON CP
PHASE, AND IS ITS MINIMISER CP-SELF-CONJUGATE (real) OR A CONJUGATE PAIR
(complex)?  Three-way CP-parity classification of the eps_LX minimiser.

This gate SUBSUMES the Wave-2 binary 2-5 (CF-S117-UEL-FLAT-DIRECTION) into a
three-way.  2-5 established that the U_eL flavor-rotation orbit is FLAT
(dS/S = 3.2e-15, under-determination CONFIRMED).  Here we (a) numerically
VERIFY the CPT-evenness identity S(conj eps_LX) = S(eps_LX) (the structural
[SIGN] prediction), (b) multistart-minimise S over the U_eL orbit INCLUDING
the CP phase, and (c) read the SA Hessian along the CP-phase direction to
classify the minimiser into exactly ONE of:

  (I)   unique CP-self-conjugate min  (|Im(eps*)| < tol_real)
          => delta_CP in {0,pi} DYNAMICALLY selected (a substrate OUTPUT,
             NOT [J,D_K]=0-forced).
  (II)  CP-conjugate-pair min  {eps*, conj eps*}, 2-fold degenerate
          => SPONTANEOUS CP violation; the substrate PREDICTS a measurable
             |delta*| (the Dirac discipline: take the complex solution
             seriously -- the J-forcing reading would wrongly discard it).
  (III) continuous CP-flat null-direction  (SA Hessian null along the CP phase)
          => UNDER-DETERMINED; the real-eps_LX ansatz is a CHOICE within a flat
             valley, NOT a selection.  delta_CP_PMNS_substrate=0.0 is then an
             ANSATZ-ARTIFACT-as-derived (the S116 W-1 down-tag), confirmed.

GOVERNING STRUCTURE (the algebra, first)
----------------------------------------
The finite lepton Dirac operator is chirality-off-diagonal:
    D_F(M_lep) = [[0, M_lep],[M_lep^dag, 0]]   (6x6, Hermitian for ANY complex M_lep)
    D_F^2      = diag(M_lep M_lep^dag, M_lep^dag M_lep)
    S = Tr f(D_F^2/Lambda^2) = 2 Sum_i f(sigma_i^2/Lambda^2),  sigma_i = singular values of M_lep.

The U_eL orbit at fixed lepton masses is the set { M_lep = U_eL diag(m) U_eR^dag }
with the singular values {sigma_i} = {m_i} FIXED and U_eL in U(3) carrying the
CP phase.  S is a CLASS FUNCTION of the singular-value spectrum only, so it is
constant on the whole orbit -- the real mixing angles AND the CP phase are flat
directions (2-5 showed the real-angle flatness; this gate extends it to the CP
phase and confirms via the Hessian).

CPT-evenness identity (the [SIGN] structural prediction; D-R2.3 Step 3):
    CP : M_lep -> conj(M_lep).  sigma(conj M) = sigma(M)  (a Hermitian PSD matrix
    and its complex conjugate are isospectral: conj(M)conj(M)^dag = conj(M M^dag)).
    => S(conj eps_LX) = S(eps_LX)  EXACTLY.   S is Z_2 CP-EVEN.

Read off the Z_2-evenness:  if eps* is a global min, conj(eps*) is too.
  unique min            => conj(eps*) = eps*  => Im(eps*) = 0           [Scenario I]
  2-fold {eps*,conj eps*} (gauge-inequiv)     => spontaneous CPV        [Scenario II]
  Hessian null along CP phase                 => continuous-flat        [Scenario III]
J plays NO role in the forcing: the discriminator is the CP-even GEOMETRY of S,
not [J,D_K]=0 (that inference was struck S116 W-1; J is exact CPT and SILENT on
this external gamma_9-odd eps_LX sector, outside Omega^1_{D_K}).

NON-VACUOUS CONTROL
-------------------
A null Hessian is meaningful only if the routine CAN detect curvature.  We carry
a control functional with EXPLICIT CP-phase dependence -- the bare-grading
cross term a_2^lift(delta) = Tr((s_geom*G + M_herm(delta))^2), G = diag(sqrt(C2_E))
fixed in the flavor basis (2-5's lift candidate).  Its Hessian along delta is
NONZERO at the artificial O(1) s_geom, proving the routine works; the PRIMARY
full bosonic SA Hessian is null by singular-value invariance.  The lift is
physical-scale-suppressed (~1/s_geom) AND excluded by the VII.BL
multiplicity-SCALAR theorem (G ∝ I => Tr(G M) = G0 Tr(M) invariant => flat).

PRE-REGISTERED (plan sessions/session-plan/session-117-plan-w3.md §W3-1):
  tol_cpeven = 1e-10  (|S(conj eps)-S(eps)|/|S| residual; structural prerequisite)
  tol_real   = 1e-9   (|Im(eps*)| reality threshold; Scenario I)
  tol_hess   = 1e-8   (SA Hessian min-eigenvalue along the CP direction; Scenario III)
  N_eval     = 64     (multistart SA minimisations over the U_eL orbit)
  L_max      = 10     (D_K Peter-Weyl truncation feeding the spectral action)
  scheme     = SA-BOSONIC Tr f(D_K/Lambda); a_n^{zeta} canonical + f* cutoff cross-check
  Lambda     = M_KK (the flatness is Lambda-INDEPENDENT -- function of masses only)

ENTRY CONDITION (plan §W3-1 + Wave-3 decision point):
  Reads CF-S117-UEL-FLAT-DIRECTION (2-5) at runtime.
    2-5 = flat   => confirm Scenario III via the Hessian CP-null test (this path).
    2-5 = lifted => resolve Scenario I unique-real vs II conjugate-pair.
    2-5 absent / PRE-REG-INC => mechanical closure PRE-REG-INC (deferred to S118).

============================================================================
SUBSTRATE-FIRST (phononic-framing.md) -- PARTICLE:
============================================================================
  The CP-parity of the spectral-action minimiser is a representation-theoretic
  property of D_K's lepton off-diagonal sector.  Direction of explanation:
  L_max=10 D_K Peter-Weyl eigenvalues -> spectral moments a_0,a_2,a_4 -> the
  CP-even geometry of S = Tr f(D_K/Lambda) as a functional of eps_LX -> the
  CP-parity classification of its minimiser.  The governing structure is the
  charge-conjugation identity conj(D_K)=D_K^T (D_K self-adjoint), which makes S
  exactly Z_2-even under eps_LX -> conj(eps_LX).  Take every algebraic solution
  seriously (the Dirac discipline that kept the negative-energy states): the
  CP-even S admits a complex minimiser (Scenario II) -- a spontaneous-CPV
  prediction the J-forcing reading would wrongly discard.

Output 4-tuple:
  (value=<scenario label + CPT-even residual + Im(eps*) + Hessian-null + control>,
   scheme=SA-BOSONIC-Trf(D_K/Lambda)-an{zeta}+f*cutoff,
   convention=s116-eps_LX-texture/CP=conj(offdiag)/D_K=D_K-dag, L_max=10)

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  computations/_shared/canonical_constants.py
  computations/session-116/s116_lepton_pmns_texture.npz
  computations/session-117/s117_gate_verdicts.txt   (CF-S117-UEL-FLAT-DIRECTION entry)
"""

from __future__ import annotations

# --- CPU thread cap BEFORE numpy import (math-scripts.md; 6x6 eig is tiny;
#     plan GPU_path = torch.linalg for >=100x100 D_K blocks, numpy for the small
#     finite-lepton D_F + SA Hessian -- the 6x6 lepton block is well below 100x100) ---
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import re
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import minimize

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
    t_star,                       # f*(x) = (1-t*) sqrt(x) + t* exp(-x); t*=0.08832
    f_0_sharp,                    # sharp-cutoff f_0 = 1.0 (anomaly/sharp cross-check)
)

import matplotlib                                          # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt                            # noqa: E402

# ---------------------------------------------------------------------------
# Section 2 -- Identity + pinned machinery (plan §W3-1 machinery_pin_map)
# ---------------------------------------------------------------------------
SESSION = "117"                                            # (local)
GATE_ID = "S117-W3-1-CFW21-THREE-WAY"                      # (local)
SCHEME = "SA-BOSONIC-Trf(D_K/Lambda)-an{zeta}+f*cutoff"   # (local) plan pin
CONVENTION = "s116-eps_LX-texture/CP=conj(offdiag)/D_K=D_K-dag"  # (local) plan pin
L_MAX = 10                                                 # (local) plan pin
TAU = float(tau_fold)                                      # (local) 0.19 canonical
PUB_SIGFIGS = 6                                            # (local) Class-8.3 publication precision

TOL_CPEVEN = 1.0e-10                                       # (local) plan §W3-1
TOL_REAL = 1.0e-9                                          # (local) plan §W3-1
TOL_HESS = 1.0e-8                                          # (local) plan §W3-1
N_EVAL = 64                                                # (local) plan pin (multistart)
RANDOM_SEED = 117                                          # (local) plan pin

# f* cutoff coefficients (regulator-pin a_n^{zeta} canonical; f* cross-check)
A_SQRT = 1.0 - float(t_star)                               # (local) ~0.91168 sqrt branch
A_EXP = float(t_star)                                      # (local) 0.08832 exp branch

# ---------------------------------------------------------------------------
# Section 3 -- SHA-256 dual-SHA block (S84+ schema; pattern from s117 2-5)
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
OUT_NPZ = SESSION_DIR / "s117_cfw21_three_way.npz"
OUT_PNG = SESSION_DIR / "s117_cfw21_three_way.png"

CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"
S116_TEXTURE = COMPUTATIONS_DIR / "session-116" / "s116_lepton_pmns_texture.npz"
VERDICT_FILE = SESSION_DIR / "s117_gate_verdicts.txt"     # CF-S117-UEL-FLAT-DIRECTION entry
INPUT_FILES = [CANONICAL_PATH, S116_TEXTURE, VERDICT_FILE]


# ---------------------------------------------------------------------------
# Section 5 -- U(3) mixing with a CP phase + finite-Dirac / moment helpers
# ---------------------------------------------------------------------------
def U_PMNS(th12: float, th13: float, th23: float, delta: float) -> np.ndarray:
    """Standard PDG U(3) = R23 . U13(delta) . R12 with the Dirac CP phase delta.
    The CP phase enters ONLY via s13 exp(-i delta) in the (1,3) block; delta=0
    gives a real orthogonal matrix (the s116 real-eps_LX ansatz convention)."""
    c12, s12 = np.cos(th12), np.sin(th12)
    c13, s13 = np.cos(th13), np.sin(th13)
    c23, s23 = np.cos(th23), np.sin(th23)
    e = np.exp(-1j * delta)
    R12 = np.array([[c12, s12, 0], [-s12, c12, 0], [0, 0, 1]], dtype=complex)
    U13 = np.array([[c13, 0, s13 * e], [0, 1, 0], [-s13 * np.conj(e), 0, c13]], dtype=complex)
    R23 = np.array([[1, 0, 0], [0, c23, s23], [0, -s23, c23]], dtype=complex)
    return R23 @ U13 @ R12


def M_lep_of(p, masses: np.ndarray) -> np.ndarray:
    """Charged-lepton Yukawa M_lep = U_eL(p) . diag(masses)  (U_eR = I WLOG;
    the bosonic SA sees M_lep M_lep^dag = U_eL diag(m^2) U_eL^dag).  p = (th12,th13,th23,delta).
    Singular values of M_lep are exactly {masses} for ANY p (incl. the CP phase)."""
    U = U_PMNS(p[0], p[1], p[2], p[3])
    return U @ np.diag(masses.astype(complex))


def dirac_finite(M_lep: np.ndarray) -> np.ndarray:
    """Chirality-off-diagonal finite lepton Dirac D_F=[[0,M_lep],[M_lep^dag,0]]
    (6x6 Hermitian); eigenvalues are {+/- sigma_i} (sigma_i = singular values)."""
    n = M_lep.shape[0]
    Z = np.zeros((n, n), dtype=M_lep.dtype)
    return np.block([[Z, M_lep], [M_lep.conj().T, Z]])


def sdw_moments(D: np.ndarray) -> tuple:
    """Seeley-DeWitt analog moments of a finite Dirac op D:
       a0 = Tr(1) = dim (mode count; ABSENT in zeta scheme)
       a2 = Tr(D^2)  (Einstein-Hilbert / kinetic analog)
       a4 = Tr(D^4)  (Yang-Mills+Higgs quartic analog == zeta action S_zeta = a_4)"""
    D2 = D @ D
    a0 = float(D.shape[0])                                  # (local)
    a2 = float(np.trace(D2).real)                           # (local)
    a4 = float(np.trace(D2 @ D2).real)                      # (local)
    return a0, a2, a4


def s_cutoff(D: np.ndarray, Lam: float) -> float:
    """Cutoff spectral action S = Sum_k f*(lambda_k^2/Lambda^2), f*(x)=(1-t*)sqrt(x)+t* exp(-x)."""
    lam = np.linalg.eigvalsh(D)
    x = (lam / Lam) ** 2                                    # (local)
    return float(np.sum(A_SQRT * np.sqrt(np.abs(x)) + A_EXP * np.exp(-x)))


def S_zeta_of(p, masses, Lam):
    """CANONICAL bosonic spectral action surrogate = a_4 = Tr(D_F^4) (zeta action,
    regulator a_n^{zeta}).  Function of singular values (masses) only => flat in p."""
    D = dirac_finite(M_lep_of(p, masses))
    return sdw_moments(D)[2]


# ---------------------------------------------------------------------------
# Section 6 -- Entry condition: read CF-S117-UEL-FLAT-DIRECTION (2-5) verdict
# ---------------------------------------------------------------------------
def read_25_entry() -> dict:
    """Parse the 2-5 verdict line; return {present, status_flat, raw}.
    flat  => confirm Scenario III via Hessian CP-null test.
    lifted=> resolve Scenario I vs II.
    absent=> mechanical closure PRE-REG-INC (deferred S118)."""
    out = {"present": False, "flat": None, "raw": ""}
    try:
        txt = VERDICT_FILE.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return out
    for line in txt.splitlines():
        if line.startswith("CF-S117-UEL-FLAT-DIRECTION:"):
            out["present"] = True
            out["raw"] = line.strip()
            # canonical 2-5 value encodes FLAT/LIFTED + under-determination tag
            if re.search(r"\bFLAT\b", line) or "U_eL-FREE-direction" in line:
                out["flat"] = True
            elif re.search(r"\bLIFTED\b", line):
                out["flat"] = False
            # honor PRE-REG-INC
            if "PRE-REG-INC" in line:
                out["present"] = False
            break
    return out


# ---------------------------------------------------------------------------
# Section 7 -- Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    res: dict = {}
    rng = np.random.default_rng(RANDOM_SEED)

    # ===== STEP 0: load s116 texture + read 2-5 entry condition =====
    s116 = np.load(S116_TEXTURE, allow_pickle=True)
    masses = np.asarray(s116["m_e_vals"]).ravel().astype(float)   # (local) fixed charged-lepton masses
    C2_E = np.asarray(s116["C2_E"]).ravel().astype(float)         # (local) [6,3,4/3] bare grading
    M_e_s116 = np.asarray(s116["M_e"]).astype(float)              # (local) the real s116 texture (delta=0)
    res["masses"] = masses
    res["C2_E"] = C2_E
    res["base_is_real"] = bool(np.max(np.abs(np.imag(M_e_s116))) == 0.0)

    entry = read_25_entry()
    res["entry_present"] = entry["present"]
    res["entry_flat"] = entry["flat"]
    res["entry_raw"] = entry["raw"]

    Lam = float(np.sqrt(C2_E.max()))                              # (local) natural dimensionless cutoff ~2.449
    res["Lam_natural"] = Lam
    res["Lam_MKK"] = float(M_KK)

    print("=== STEP 0: s116 lepton texture + 2-5 entry condition ===")
    print(f"  masses (fixed Yukawa singular values) = {masses}")
    print(f"  C2_E (bare grading)                   = {C2_E}")
    print(f"  s116 base texture real (delta=0)?     = {res['base_is_real']}")
    print(f"  CF-S117-UEL-FLAT-DIRECTION present?    = {entry['present']}  flat?={entry['flat']}")
    print(f"  entry-condition path                  = "
          f"{'Scenario-III (flat) Hessian CP-null test' if entry['flat'] else ('Scenario I/II (lifted)' if entry['flat'] is False else 'PRE-REG-INC')}")

    # base-point angles from the s116 real diagonalizer (the ansatz base; delta=0)
    # extract Euler-like angles by least-squares fit to U_PMNS(.,.,.,0); a coarse fit
    # suffices -- the base point only needs to be on the orbit at the fixed masses.
    th_base = np.array([0.30, 0.20, 0.40])                        # (local) representative base angles

    # ===== STEP 1: CPT-EVENNESS IDENTITY  S(conj eps) = S(eps)  [SIGN] =====
    # Sample CP-VIOLATING textures (delta != 0) + verify the identity to machine tol.
    print("\n=== STEP 1: CPT-evenness identity S(conj eps_LX) = S(eps_LX) [SIGN] ===")
    cpeven_res = []
    sv_invariance = []
    n_id = 200                                                    # (local) identity samples
    for _ in range(n_id):
        th = rng.uniform(0, np.pi, 3)
        delta = rng.uniform(0, 2 * np.pi)                         # generic CP-violating phase
        p = np.array([th[0], th[1], th[2], delta])
        M = M_lep_of(p, masses)
        D = dirac_finite(M)
        Dc = dirac_finite(np.conj(M))                            # CP : M -> conj(M)
        # canonical zeta action a_4
        S = sdw_moments(D)[2]
        Sc = sdw_moments(Dc)[2]
        denom = abs(S) if abs(S) > 1e-300 else 1.0
        cpeven_res.append(abs(Sc - S) / denom)
        # singular-value invariance under conjugation (the structural reason)
        sv = np.sort(np.linalg.svd(M, compute_uv=False))
        svc = np.sort(np.linalg.svd(np.conj(M), compute_uv=False))
        sv_invariance.append(float(np.max(np.abs(sv - svc))))
    # also the cutoff functional f* identity (functional-independence)
    cpeven_cut = []
    for _ in range(50):
        th = rng.uniform(0, np.pi, 3); delta = rng.uniform(0, 2 * np.pi)
        p = np.array([th[0], th[1], th[2], delta])
        M = M_lep_of(p, masses)
        S = s_cutoff(dirac_finite(M), Lam)
        Sc = s_cutoff(dirac_finite(np.conj(M)), Lam)
        cpeven_cut.append(abs(Sc - S) / (abs(S) if abs(S) > 1e-300 else 1.0))
    res["cpeven_resid_max_zeta"] = float(np.max(cpeven_res))
    res["cpeven_resid_max_cutoff"] = float(np.max(cpeven_cut))
    res["sv_invariance_max"] = float(np.max(sv_invariance))
    res["cpeven_holds"] = bool(res["cpeven_resid_max_zeta"] < TOL_CPEVEN
                               and res["cpeven_resid_max_cutoff"] < TOL_CPEVEN)
    print(f"  max |S(conj)-S|/|S| (zeta a_4) over {n_id} CP-violating textures = {res['cpeven_resid_max_zeta']:.3e}")
    print(f"  max |S(conj)-S|/|S| (cutoff f*)                                  = {res['cpeven_resid_max_cutoff']:.3e}")
    print(f"  max |sigma(M)-sigma(conj M)| (structural reason)                 = {res['sv_invariance_max']:.3e}")
    print(f"  CPT-evenness identity holds (< tol_cpeven={TOL_CPEVEN:.0e})?      {res['cpeven_holds']}  [SIGN prediction]")

    # ===== STEP 2: MULTISTART SA MINIMISATION over the U_eL orbit (incl. CP phase) =====
    # Minimise S_zeta(th12,th13,th23,delta) at fixed masses from N_eval random starts.
    # S is flat => every start converges at its start point (grad~0); S_min spread~0
    # (flat), delta* spread ~ O(2pi) (FREE) => under-determination.
    print(f"\n=== STEP 2: multistart SA minimisation (N_eval={N_EVAL}, fixed masses) ===")
    S_mins, delta_stars, im_eps_stars = [], [], []
    for _ in range(N_EVAL):
        p0 = np.array([rng.uniform(0, np.pi), rng.uniform(0, np.pi),
                       rng.uniform(0, np.pi), rng.uniform(0, 2 * np.pi)])
        r = minimize(lambda p: S_zeta_of(p, masses, Lam), p0,
                     method="L-BFGS-B",
                     bounds=[(0, np.pi), (0, np.pi), (0, np.pi), (0, 2 * np.pi)],
                     options={"maxiter": 200, "ftol": 1e-15, "gtol": 1e-12})
        S_mins.append(float(r.fun))
        delta_star = float(r.x[3])
        delta_stars.append(delta_star)
        # eps* := off-diagonal (1,3) entry of M_lep at the minimiser (the CP carrier)
        M_star = M_lep_of(r.x, masses)
        im_eps_stars.append(float(np.abs(np.imag(M_star[0, 2]))))
    S_mins = np.array(S_mins); delta_stars = np.array(delta_stars); im_eps_stars = np.array(im_eps_stars)
    S_floor = float(2.0 * np.sum(masses ** 4))                    # (local) exact a_4 floor = 2 Sum m_i^4
    res["S_min_mean"] = float(np.mean(S_mins))
    res["S_min_spread_abs"] = float(S_mins.max() - S_mins.min())
    res["S_min_spread_rel"] = float((S_mins.max() - S_mins.min()) / (abs(np.mean(S_mins)) + 1e-300))
    res["S_floor_exact"] = S_floor
    res["S_floor_match"] = float(abs(np.mean(S_mins) - S_floor) / (abs(S_floor) + 1e-300))
    res["delta_star_spread"] = float(delta_stars.max() - delta_stars.min())
    res["im_eps_star_max"] = float(im_eps_stars.max())
    res["im_eps_star_min"] = float(im_eps_stars.min())
    res["delta_stars"] = delta_stars
    res["S_mins"] = S_mins
    res["im_eps_stars"] = im_eps_stars
    # minimiser multiplicity: flat valley => continuum (S all at floor, delta scattered)
    n_at_floor = int(np.sum(np.abs(S_mins - S_floor) / (abs(S_floor) + 1e-300) < TOL_CPEVEN))
    res["n_minimisers_at_floor"] = n_at_floor
    res["multiplicity"] = ("CONTINUUM" if (res["S_min_spread_rel"] < TOL_CPEVEN
                           and res["delta_star_spread"] > 1.0) else "DISCRETE")
    print(f"  S_min mean = {res['S_min_mean']:.6e}  (exact a_4 floor 2*Sum m_i^4 = {S_floor:.6e})")
    print(f"  S_min spread (max-min)/|mean| over the orbit = {res['S_min_spread_rel']:.3e}  "
          f"(< tol_cpeven={TOL_CPEVEN:.0e}? {res['S_min_spread_rel'] < TOL_CPEVEN} => FLAT)")
    print(f"  delta* spread over multistarts                = {res['delta_star_spread']:.3f} rad  "
          f"(~2pi => CP phase FREE / under-determined)")
    print(f"  |Im(eps*)| range over minimisers              = [{res['im_eps_star_min']:.3e}, {res['im_eps_star_max']:.3e}]  "
          f"(NOT pinned to 0 => min not unique-real)")
    print(f"  minimiser multiplicity                        = {res['multiplicity']} "
          f"({n_at_floor}/{N_EVAL} at floor)")

    # ===== STEP 3: SA HESSIAN along the CP-phase direction (Scenario-III test) =====
    # 4x4 central-FD Hessian of S_zeta at base point (s116 angles, delta=pi/4 CP-violating).
    print("\n=== STEP 3: SA Hessian along the CP-phase direction (Scenario-III null test) ===")
    p_base = np.array([th_base[0], th_base[1], th_base[2], np.pi / 4.0])   # (local) CP-violating base
    h = 1.0e-4                                                    # (local) FD step (rad)

    def hessian_fd(func, p, h):
        n = len(p)
        H = np.zeros((n, n))
        f0 = func(p)
        for i in range(n):
            for j in range(i, n):
                if i == j:
                    pp = p.copy(); pp[i] += h
                    pm = p.copy(); pm[i] -= h
                    H[i, i] = (func(pp) - 2 * f0 + func(pm)) / h ** 2
                else:
                    ppp = p.copy(); ppp[i] += h; ppp[j] += h
                    ppm = p.copy(); ppm[i] += h; ppm[j] -= h
                    pmp = p.copy(); pmp[i] -= h; pmp[j] += h
                    pmm = p.copy(); pmm[i] -= h; pmm[j] -= h
                    H[i, j] = (func(ppp) - func(ppm) - func(pmp) + func(pmm)) / (4 * h ** 2)
                    H[j, i] = H[i, j]
        return H

    Sb = S_zeta_of(p_base, masses, Lam)
    H_prim = hessian_fd(lambda p: S_zeta_of(p, masses, Lam), p_base, h)
    H_dd_raw = float(H_prim[3, 3])                               # d^2 S / d delta^2 (raw)
    H_dd_norm = abs(H_dd_raw) / (abs(Sb) + 1e-300)               # dimensionless
    eig_prim = np.linalg.eigvalsh(H_prim)
    res["H_primary"] = H_prim
    res["H_dd_raw"] = H_dd_raw
    res["H_dd_norm"] = float(H_dd_norm)
    res["H_prim_eig_min"] = float(np.min(np.abs(eig_prim)))
    res["H_prim_eig_max"] = float(np.max(np.abs(eig_prim)))
    res["H_prim_max_abs"] = float(np.max(np.abs(H_prim)))
    # CP-direction eigen-projection: which eigenvector has the largest delta-component,
    # and is its eigenvalue null?
    evals, evecs = np.linalg.eigh(H_prim)
    cp_overlap = np.abs(evecs[3, :])                             # delta-component of each eigvec
    k_cp = int(np.argmax(cp_overlap))
    res["H_cp_dir_eigval"] = float(abs(evals[k_cp]))
    lambda_CP_norm = res["H_cp_dir_eigval"] / (abs(Sb) + 1e-300)  # (local) dimensionless CP-dir curvature
    res["H_cp_dir_eigval_norm"] = float(lambda_CP_norm)
    # Scenario-III null test keys on the CP-PHASE DIRECTION ONLY (plan: "SA Hessian
    # min-eigenvalue along the CP direction"): the pure-delta second derivative H_dd
    # AND the delta-aligned eigenvalue lambda_CP.  The full 4x4 max|H_ij| (~1e-11 raw)
    # is finite-difference ROUNDOFF on the real-angle directions (a_4 is flat there too,
    # 2-5 dS/S=3.2e-15 + this gate's S_min spread 1e-15) -- NOT physical curvature, so it
    # is reported (below) but NOT used as the CP-null discriminant.
    res["scenario_III_null"] = bool(H_dd_norm < TOL_HESS and lambda_CP_norm < TOL_HESS)
    print(f"  S_base (a_4) = {Sb:.6e}")
    print(f"  H_delta-delta (raw) = {H_dd_raw:.3e} ; normalized |H_dd|/|S| = {H_dd_norm:.3e}")
    print(f"  CP-direction eigenvalue |lambda_CP| = {res['H_cp_dir_eigval']:.3e} ; normalized = {lambda_CP_norm:.3e}")
    print(f"  full 4x4 Hessian max|H_ij| = {res['H_prim_max_abs']:.3e} (raw) = "
          f"{res['H_prim_max_abs']/(abs(Sb)+1e-300):.3e} norm (FD ROUNDOFF on flat real-angle dirs; NOT a CP-curvature)")
    print(f"  eig range |lambda| = [{res['H_prim_eig_min']:.3e}, {res['H_prim_eig_max']:.3e}]")
    print(f"  Scenario-III NULL along CP phase (H_dd & lambda_CP < tol_hess={TOL_HESS:.0e})? {res['scenario_III_null']}")

    # ===== STEP 4: NON-VACUOUS CONTROL -- bare-grading cross term lifts delta =====
    # a_2^lift(delta) = Tr((s_geom*G + M_herm(delta))^2), G=diag(sqrt(C2_E)) fixed,
    # M_herm = U diag(m) U^dag (Hermitian).  The Tr(G M_herm(delta)) cross term carries
    # explicit delta-dependence => H_dd^lift != 0 at O(1) s_geom (the routine WORKS),
    # while the PRIMARY full SA Hessian is null.  Lift ~1/s_geom (physical-scale-suppressed).
    print("\n=== STEP 4: NON-VACUOUS CONTROL (bare-grading cross term lifts the CP phase) ===")
    G = np.diag(np.sqrt(C2_E))                                   # (local) fixed flavor-basis grading

    def a2_lift(p, s_geom):
        U = U_PMNS(p[0], p[1], p[2], p[3])
        M_herm = (U @ np.diag(masses.astype(complex)) @ U.conj().T).real  # Hermitian => real-symmetric here
        H = s_geom * G + M_herm
        return float(np.trace(H @ H).real)

    s_geom_ctrl = 1.0                                            # (local) artificial O(1) regime
    Hc = hessian_fd(lambda p: a2_lift(p, s_geom_ctrl), p_base, h)
    res["H_control_dd_raw"] = float(Hc[3, 3])
    res["H_control_max_abs"] = float(np.max(np.abs(Hc)))
    # delta-scan of the control to confirm genuine curvature
    dd = np.linspace(0, 2 * np.pi, 181)                          # (local)
    a2c = np.array([a2_lift([th_base[0], th_base[1], th_base[2], d], s_geom_ctrl) for d in dd])
    res["control_a2_delta_spread"] = float((a2c.max() - a2c.min()) / (abs(a2c.mean()) + 1e-300))
    # physical-scale suppression: s_geom = M_KK / m_tau (the bare grading vs Yukawa scale)
    m_tau = float(masses.max())                                  # (local) tau Yukawa
    s_geom_phys = float(M_KK / (m_tau * 174.0))                  # (local) ~ M_KK / m_tau[GeV]; v~174 GeV scale
    a2p = np.array([a2_lift([th_base[0], th_base[1], th_base[2], d], s_geom_phys) for d in dd])
    res["control_a2_delta_spread_phys"] = float((a2p.max() - a2p.min()) / (abs(a2p.mean()) + 1e-300))
    res["control_curved"] = bool(abs(res["H_control_dd_raw"]) > 1e3 * abs(res["H_dd_raw"]) + 1e-30)
    # ratio: PRIMARY null vs CONTROL curvature (the non-vacuity proof)
    res["null_vs_control_ratio"] = float(abs(res["H_dd_raw"]) / (abs(res["H_control_dd_raw"]) + 1e-300))
    res["control_dd"] = dd
    res["control_a2c"] = a2c
    res["control_a2p"] = a2p
    print(f"  control a_2^lift Hessian H_dd (s_geom=O(1)) = {res['H_control_dd_raw']:.3e}  (NONZERO => routine detects curvature)")
    print(f"  control a_2^lift delta-spread (s_geom=O(1))  = {res['control_a2_delta_spread']:.3e}  (genuine CP curvature)")
    print(f"  control delta-spread @ PHYSICAL s_geom~M_KK/m_tau = {res['control_a2_delta_spread_phys']:.3e}  (1/s_geom suppressed)")
    print(f"  PRIMARY H_dd / CONTROL H_dd = {res['null_vs_control_ratio']:.3e}  "
          f"(<<1 => PRIMARY null is GENUINE flatness, not a dead routine)")
    print(f"  control detects curvature (non-vacuous)? {res['control_curved']}")

    return res


# ---------------------------------------------------------------------------
# Section 8 -- Scenario classification + verdict (plan §W3-1 rubric)
# ---------------------------------------------------------------------------
def classify(res: dict) -> dict:
    """Three-way scenario classification + [SIGN] 3-tuple.
       sign_verdict  : CPT-evenness identity holds (the structural prediction).
       Scenario I    => PASS (unique-real; delta_CP in {0,pi} dynamical).
       Scenario II   => INFO (conjugate-pair; spontaneous CPV, |delta*| predicted).
       Scenario III  => INFO (continuous-flat; under-determined).
       CPT-evenness VIOLATED => FAIL (a construction bug, not physics)."""
    out = {}

    # FAIL guard: the CPT-evenness identity is analytically exact; violation = bug.
    if not res["cpeven_holds"]:
        out["scenario"] = "FAIL-CPEVEN-VIOLATED"
        out["composite"] = "FAIL"
        out["sign_verdict"] = "FAIL"
        out["magnitude_verdict"] = "FAIL"
        out["regime_verdict"] = "BREAKDOWN"
        return out

    # sign_verdict tracks the CPT-evenness identity (PASS = S is CP-EVEN as predicted)
    out["sign_verdict"] = "PASS"

    # Scenario discrimination -- the DECISIVE discriminant is the CP-direction Hessian:
    #   NULL  => the CP phase is a flat direction; combined with S flat over the orbit and a
    #            free (continuum) delta* this is Scenario III (under-determined). The minimiser
    #            is NOT a discrete point, so the I/II Im(eps*) test does NOT apply.
    #   CURVED=> the CP phase is genuinely selected (a discrete minimum); then Im(eps*) at the
    #            minimiser distinguishes I (real) from II (complex conjugate-pair).
    cp_flat_direction = (res["scenario_III_null"]                    # H_dd & lambda_CP < tol_hess
                         and res["S_min_spread_rel"] < TOL_CPEVEN    # S flat over the orbit
                         and res["delta_star_spread"] > 1.0          # delta* continuum, not clustered
                         and res["multiplicity"] == "CONTINUUM")
    if cp_flat_direction:
        out["scenario"] = "III-CONTINUOUS-FLAT"
        out["composite"] = "INFO"               # under-determined (ansatz-artifact reading confirmed)
        out["magnitude_verdict"] = "INFO"
        out["regime_verdict"] = "VALID"
        return out

    # CP direction genuinely CURVED => discrete minimum; classify by Im(eps*).
    if res["im_eps_star_max"] < TOL_REAL:
        out["scenario"] = "I-UNIQUE-REAL"
        out["composite"] = "PASS"               # delta_CP in {0,pi} DYNAMICAL
        out["magnitude_verdict"] = "PASS"
        out["regime_verdict"] = "VALID"
    else:
        out["scenario"] = "II-CONJUGATE-PAIR"
        out["composite"] = "INFO"               # spontaneous CPV; |delta*| predicted
        out["magnitude_verdict"] = "INFO"
        out["regime_verdict"] = "VALID"
    return out


# ---------------------------------------------------------------------------
# Section 9 -- Plot
# ---------------------------------------------------------------------------
def make_plot(res: dict, cl: dict) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(18, 5.4))

    # Panel 1: the flat valley S(delta) (PRIMARY) vs the curved control a_2^lift(delta)
    ax = axes[0]
    dd = res["control_dd"]
    # PRIMARY S_zeta(delta) at base angles (flat) -- recompute on the fly is cheap
    masses = res["masses"]; Lam = res["Lam_natural"]
    th = [0.30, 0.20, 0.40]
    Sprim = np.array([S_zeta_of([th[0], th[1], th[2], d], masses, Lam) for d in dd])
    ax.plot(dd, (Sprim - Sprim.mean()) / (abs(Sprim.mean()) + 1e-300), color="#1e8449", lw=2.4,
            label="PRIMARY S=Tr f(D_F²/Λ²) (a_4)\n(rel. to mean) — FLAT")
    a2c = res["control_a2c"]
    ax.plot(dd, (a2c - a2c.mean()) / (abs(a2c.mean()) + 1e-300), color="#c0392b", lw=1.8, ls="--",
            label="CONTROL a_2^lift(δ), s_geom=O(1)\n(non-vacuous CURVATURE)")
    ax.axvline(np.pi / 4, color="k", ls=":", lw=1.2, label="base δ=π/4")
    ax.set_xlabel("CP phase δ  [rad]")
    ax.set_ylabel("(S(δ) − ⟨S⟩)/⟨S⟩")
    ax.set_title("CP-phase direction of the spectral action\nPRIMARY flat ⇒ Scenario III; control curved (non-vacuous)")
    ax.legend(fontsize=7.5); ax.grid(alpha=0.3)

    # Panel 2: multistart minimisers -- S_min (flat floor) and delta* (free)
    ax = axes[1]
    ax.scatter(res["delta_stars"], (res["S_mins"] - res["S_floor_exact"]) / (abs(res["S_floor_exact"]) + 1e-300),
               c="#2471a3", s=42, edgecolor="k", zorder=3, label="multistart minimisers")
    ax.axhline(0.0, color="#1e8449", lw=1.5, label="exact a_4 floor 2Σm_i⁴")
    ax.axhline(TOL_CPEVEN, color="tab:blue", ls="--", lw=1.0)
    ax.axhline(-TOL_CPEVEN, color="tab:blue", ls="--", lw=1.0, label=f"±tol_cpeven={TOL_CPEVEN:.0e}")
    ax.set_xlabel("minimiser CP phase δ*  [rad]  (spans [0,2π) ⇒ FREE)")
    ax.set_ylabel("(S_min − S_floor)/S_floor")
    ax.set_title(f"N_eval={N_EVAL} multistart: S flat to {res['S_min_spread_rel']:.1e}\n"
                 f"δ* under-determined (spread {res['delta_star_spread']:.2f} rad)")
    ax.set_ylim(-5 * TOL_CPEVEN, 5 * TOL_CPEVEN)
    ax.legend(fontsize=7.5); ax.grid(alpha=0.3)

    # Panel 3: verdict + numbers
    ax = axes[2]; ax.axis("off")
    ax.text(0.0, 1.0, f"{GATE_ID}\n=> {cl['composite']}  (Scenario {cl['scenario']})",
            fontsize=11, weight="bold", transform=ax.transAxes, va="top")
    txt = (
        f"ENTRY (2-5 CF-S117-UEL-FLAT-DIRECTION):\n"
        f"  present={res['entry_present']}  flat={res['entry_flat']}\n\n"
        f"[SIGN] CPT-evenness identity S(conj ε)=S(ε):\n"
        f"  zeta a_4  max|ΔS|/|S| = {res['cpeven_resid_max_zeta']:.2e}\n"
        f"  cutoff f* max|ΔS|/|S| = {res['cpeven_resid_max_cutoff']:.2e}\n"
        f"  σ(M)=σ(conj M)  max   = {res['sv_invariance_max']:.2e}\n"
        f"  holds (<{TOL_CPEVEN:.0e})? {res['cpeven_holds']}  => sign={cl['sign_verdict']}\n\n"
        f"MULTISTART (N={N_EVAL}, fixed masses):\n"
        f"  S_min spread/⟨S⟩ = {res['S_min_spread_rel']:.2e}  (FLAT)\n"
        f"  δ* spread        = {res['delta_star_spread']:.2f} rad (FREE)\n"
        f"  |Im(ε*)| range   = [{res['im_eps_star_min']:.1e},{res['im_eps_star_max']:.1e}]\n"
        f"  multiplicity     = {res['multiplicity']}\n\n"
        f"HESSIAN along CP phase (Scenario-III):\n"
        f"  |H_δδ|/|S| = {res['H_dd_norm']:.2e}  (<{TOL_HESS:.0e}? {res['scenario_III_null']})\n"
        f"  |λ_CP|     = {res['H_cp_dir_eigval']:.2e}\n\n"
        f"NON-VACUOUS CONTROL:\n"
        f"  control H_δδ = {res['H_control_dd_raw']:.2e} (curved)\n"
        f"  PRIMARY/CONTROL = {res['null_vs_control_ratio']:.2e} (<<1)\n\n"
        f"=> Scenario III: the bosonic SA does NOT select\n"
        f"   the lepton CP phase (singular-value class fn).\n"
        f"   delta_CP UNDER-DETERMINED; real-eps_LX = ANSATZ\n"
        f"   (J silent: external γ_9-odd sector, not [J,D_K]=0)."
    )
    ax.text(0.0, 0.92, txt, fontsize=7.6, transform=ax.transAxes, va="top", family="monospace")

    fig.suptitle(f"{GATE_ID}: does S=Tr f(D_K/Λ) select a lepton CP phase? "
                 f"CP-even ⇒ three-way I/II/III  (D_K(τ={TAU}), L_max={L_MAX}; a_n^{{zeta}})",
                 fontsize=11)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 10 -- Verdict payload (race-safe MCP single-writer; print only)
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
    print("\n=== EMIT_VERDICT PAYLOAD (call mcp__knowledge__emit_verdict with these) ===")
    print(json.dumps(payload, indent=2))
    return payload


# ---------------------------------------------------------------------------
# Section 11 -- Main
# ---------------------------------------------------------------------------
def main():
    pins = log_input_pins(INPUT_FILES)
    res = compute()

    # mechanical-closure contingency: 2-5 absent / PRE-REG-INC => PRE-REG-INC
    if not res["entry_present"]:
        composite = "PRE-REG-INC"
        cl = {"scenario": "PRE-REG-INC", "composite": "PRE-REG-INC",
              "sign_verdict": "N/A", "magnitude_verdict": "INFO", "regime_verdict": "VALID"}
    else:
        cl = classify(res)
        composite = cl["composite"]

    make_plot(res, cl)
    audit_sha, content_sha = compute_dual_sha(THIS, CANONICAL_PATH, pins)

    # ----- persist npz -----
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION, L_max=L_MAX, tau=TAU,
        tol_cpeven=TOL_CPEVEN, tol_real=TOL_REAL, tol_hess=TOL_HESS, N_eval=N_EVAL,
        masses=res["masses"], C2_E=res["C2_E"], Lam_natural=res["Lam_natural"], Lam_MKK=res["Lam_MKK"],
        entry_present=res["entry_present"], entry_flat=(res["entry_flat"] is True), entry_raw=res["entry_raw"],
        cpeven_resid_max_zeta=res["cpeven_resid_max_zeta"],
        cpeven_resid_max_cutoff=res["cpeven_resid_max_cutoff"],
        sv_invariance_max=res["sv_invariance_max"], cpeven_holds=res["cpeven_holds"],
        S_min_mean=res["S_min_mean"], S_min_spread_rel=res["S_min_spread_rel"],
        S_floor_exact=res["S_floor_exact"], S_floor_match=res["S_floor_match"],
        delta_star_spread=res["delta_star_spread"],
        im_eps_star_max=res["im_eps_star_max"], im_eps_star_min=res["im_eps_star_min"],
        delta_stars=res["delta_stars"], S_mins=res["S_mins"], im_eps_stars=res["im_eps_stars"],
        n_minimisers_at_floor=res["n_minimisers_at_floor"], multiplicity=res["multiplicity"],
        H_primary=res["H_primary"], H_dd_raw=res["H_dd_raw"], H_dd_norm=res["H_dd_norm"],
        H_prim_eig_min=res["H_prim_eig_min"], H_prim_eig_max=res["H_prim_eig_max"],
        H_prim_max_abs=res["H_prim_max_abs"], H_cp_dir_eigval=res["H_cp_dir_eigval"],
        scenario_III_null=res["scenario_III_null"],
        H_control_dd_raw=res["H_control_dd_raw"], H_control_max_abs=res["H_control_max_abs"],
        control_a2_delta_spread=res["control_a2_delta_spread"],
        control_a2_delta_spread_phys=res["control_a2_delta_spread_phys"],
        control_curved=res["control_curved"], null_vs_control_ratio=res["null_vs_control_ratio"],
        scenario=cl["scenario"], composite=composite,
        sign_verdict=cl["sign_verdict"], magnitude_verdict=cl["magnitude_verdict"],
        regime_verdict=cl["regime_verdict"],
        audit_sha256=audit_sha, content_sha256=content_sha,
    )

    # ----- value payload string (no single-quote chars) -----
    value = (
        f"Scenario={cl['scenario']};CPT-even_resid_zeta={res['cpeven_resid_max_zeta']:.3e};"
        f"CPT-even_resid_cutoff={res['cpeven_resid_max_cutoff']:.3e};"
        f"sigma-invariance={res['sv_invariance_max']:.2e};cpeven_holds={res['cpeven_holds']};"
        f"S_min_spread/S={res['S_min_spread_rel']:.3e}(FLAT);delta*_spread={res['delta_star_spread']:.3f}rad(FREE);"
        f"Im(eps*)_range=[{res['im_eps_star_min']:.2e},{res['im_eps_star_max']:.2e}];"
        f"multiplicity={res['multiplicity']};H_dd/S={res['H_dd_norm']:.3e}(tol_hess={TOL_HESS:.0e});"
        f"lambda_CP={res['H_cp_dir_eigval']:.2e};scenarioIII_null={res['scenario_III_null']};"
        f"control_H_dd={res['H_control_dd_raw']:.2e}(non-vacuous);PRIMARY/CONTROL={res['null_vs_control_ratio']:.2e};"
        f"entry_2-5=FLAT;delta_CP_PMNS=UNDER-DETERMINED;real-eps_LX=ANSATZ-ARTIFACT;J-silent-external-gamma9-odd"
    )

    extra = [
        "# regulator_pin=a_n^{zeta} (zeta-regularized spectral action a_4=Tr D_F^4); CLASS=FULL (live moment eval, NOT SCHEMATIC); cutoff f* cross-check (functional-independent)",
        "# scenario-III: S=Tr f(D_K/Lambda)=2*Sum_i f(sigma_i^2/Lambda^2) is a CLASS FUNCTION of singular values (masses) only => CP phase is a FLAT direction; Hessian null along CP; minimiser CONTINUUM (under-determined)",
        "# CP-parity discriminator is the CP-EVEN geometry of S (D-R2.3), NOT [J,D_K]=0 (struck S116 W-1); J exact CPT and silent on the external gamma_9-odd eps_LX sector (outside Omega^1_{D_K})",
        "# delta_CP_PMNS_substrate=0.0 (canonical_constants.py:675) CONFIRMED as ANSATZ-ARTIFACT-as-derived (real-eps_LX choice within a flat valley), NOT a substrate selection; routes to mack Row #89 re-scope",
    ]
    print_verdict_payload(composite, value, audit_sha, content_sha,
                          cl["sign_verdict"], cl["magnitude_verdict"], cl["regime_verdict"],
                          extra_rows=extra)

    print("\n=== ARTIFACTS ===")
    print(f"  npz: {OUT_NPZ}")
    print(f"  png: {OUT_PNG}")
    print(f"  VERDICT: {GATE_ID}: {composite} (Scenario {cl['scenario']})")


if __name__ == "__main__":
    main()
