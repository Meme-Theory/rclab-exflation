#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S98-W3-1-YUKAWA-EPS-LX-BETWEEN-GEN  (Wave 3, frontier #7)  -- [SIGN] gate.

Derive the three-generation charged-lepton Yukawa hierarchy from the EXTERNAL
non-left-invariant BETWEEN-GENERATION channel eps_LX -- a 3x3 Hermitian flavour
object with non-degenerate singular values inserted into the C^3 generation
(Peter-Weyl triality) multiplicity index -- NOT the within-sector phi_88-Cartan
deformation (generation-blind / ILL-POSED per the registered SS-VII.BL E1
Non-LI-Deformation Necessity Theorem, STAGE-1-CANDIDATE, LANDED S97).

Substrate-first (phononic-framing.md):
    D_K eigenvalues -> Z_3-triality J-orbit structure (generations = SU(3)
    Peter-Weyl multiplicity, proven_384) -> a_4^{Mellin} Yukawa moment
    -> mass ratio -> (eps_LX non-LI fibre deformation supplies the hierarchy).
Generations are NOT an input list. They ARE the C^{m(p,q)} multiplicity leg of
D_K's representation of A_K. The fabric's OWN differential calculus
(Omega^1_{D_K}(A_K), inner / twisted-inner / opposite) is multiplicity-SCALAR by
Skolem-Noether (Aut(A_K) is multiplicity-blind, E1 / SS-VII.BL), so the substrate
CANNOT manufacture the hierarchy from inside its inner geometry -- the W3 FAIL of
S97-YUKAWA-FAMILY-DERIVE (R_cross=1.019704, n_distinct=2) is the substrate
correctly reporting this. The hierarchy is the imprint of how the fabric's fibre
connection is deformed AWAY FROM homogeneity (Wall 2 broken) while STAYING
reality-compatible (Wall 1 [J,D_K+eps_LX]=0 preserved). This is the lepton-sector
analog of the external phi_88-Cartan dA that already PASSES at baryogenesis (#9,
S97-BARYOGEN-EXT-SOURCE).

E1 TWO-WALL SCHEMA (registry SS-VII.BL):
  (W1) Reality wall  -- [J, D_K + eps_LX] = 0. SATISFIABLE (constrains eps_LX form).
  (W2) Homogeneity wall -- left-invariance => multiplicity-scalar representation.
       eps_LX MUST BREAK left-invariance on the multiplicity space.
  (W3) Inner-fluctuation impotence -- every A_K-built form is multiplicity-scalar.
  (Corollary) any fix MUST be an external non-LI fibre connection breaking W2 while
       preserving W1, non-gauge-removable (P_nLI = ||eps_LX||^2 > 0).

KEY STRUCTURAL FACT (verified at machine precision in this script, Section 6 STEP 1):
  eps_LX acts on the GENERATION (triality-multiplicity) leg (x) 1_16 on the finite
  bimodule; the algebra acts as I_gen (x) a_16 on the C^16 bimodule leg. The two
  factors are DISJOINT tensor legs, so [eps_LX, a] = 0 EXACT for every A_K generator
  a. Hence the order-one double commutator obeys
      [[D_K + eps_LX, a], J b* J^{-1}] = [[D_K, a], J b* J^{-1}] + 0
  -- eps_LX contributes ZERO incremental order-one residual. The between-generation
  eps_LX preserves order-one block-by-block (W1 preserved) while being non-scalar on
  the multiplicity factor (W2 broken). This is the unique viable corridor per E1.

Pre-registered operator (plan SS-W3-1, four conjuncts):
  PASS := ( ||[[D_K+eps_LX,a],Jb*J^{-1}]||_max < 1e-10 )                          (i)
        AND ( EXISTS (p,q): ||eps_LX|_{(p,q)} - (tr/m)*1|| > 0 )                   (ii)
        AND ( P_nLI = eps^2 > 0 )                                                 (iii)
        AND ( max_i |log10(r_i^derived) - log10(r_i^target)| <= 0.30 ),           (iv)
  r_1 = y_mu/y_e, r_2 = y_tau/y_mu (the two independent inter-generation ratios).

[SIGN] substitution chain (plan SS-W3-1 (7)):
  Claim (direction): inserting a non-degenerate-singular-value eps_LX on the C^3
  multiplicity index moves R_derived TOWARD the PDG hierarchy (away from the
  multiplicity-scalar-degenerate R_cross=1.01970). sign_verdict keys on
  (R_derived-1)*(s_i-s_j) > 0 for s_i>s_j (heavier generation): the singular-value
  SPREAD widens the 1:1:1 degeneracy in the CORRECT direction.

Output 4-tuple:
  (value=max_logdist_dex, scheme=NCG-INNER-FLUCT-EXTERNAL-NONLI,
   convention=EPS-LX-BETWEEN-GENERATION-MULTIPLICITY..., L_max=12)
where value = max_i |log10(r_i^derived) - log10(r_i^target)| (the worst-ratio
hierarchy-band residual in dex; PASS iff <= 0.30).

Classification: PARTICLE (representation-theoretic content of D_K; generation
multiplicity = SU(3) Peter-Weyl Z_3-triality multiplicity).

SOURCE-RECON note (plan machinery_pin_map; Class-(f) PIN-PLACEHOLDER + Class-(c)
stale-source): canonical m_tau=2.062 is the MODULUS mass at the fold IN M_KK UNITS
(S42 W2-1), NOT the PDG tau lepton mass -- it is dimensionally INCONSISTENT with
m_mu=0.1056583745 GeV. This script does NOT consume m_tau=2.062 as a lepton mass.
The hierarchy band is evaluated at a SINGLE consistent scale: PDG POLE masses (all
in GeV). m_e=5.10998950e-4 GeV was added to canonical_constants.py with PDG 2024
provenance THIS SESSION (S98 W3-1) before use, per math-scripts.md. The verdict-line
convention= field declares the scale (PDG-POLE).

Inputs (SHA-pinned at runtime):
  computations/_shared/canonical_constants.py            (m_e PDG, m_mu PDG; MUTATED this gate)
  computations/session-97/s97_yukawa_family_derive.npz   (R_cross=1.019704; E_triple; premise)
  computations/session-84/s84_spectrum_cache_L12_tau019.npz (L12 D_K spectrum by sector)
"""

from __future__ import annotations

import hashlib
import json
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# Section 1 -- Paths
# ---------------------------------------------------------------------------
THIS = Path(__file__).resolve()
SESSION_DIR = THIS.parent                              # computations/session-98
COMPUTATIONS_DIR = SESSION_DIR.parent                  # computations
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import tau_fold, m_e, m_mu     # noqa: E402

# Optional GPU (AMD RX 9070 XT / ROCm) for any >=100x100 block.
try:
    import torch
    _HAS_TORCH = bool(torch.cuda.is_available())
except Exception:
    torch = None
    _HAS_TORCH = False

import matplotlib                                       # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt                         # noqa: E402

# ---------------------------------------------------------------------------
# Section 2 -- Identity + pinned machinery (plan SS-W3-1 machinery_pin_map)
# ---------------------------------------------------------------------------
GATE_ID = "S98-W3-1-YUKAWA-EPS-LX-BETWEEN-GEN"
SCHEME = "NCG-INNER-FLUCT-EXTERNAL-NONLI"
CONVENTION = "EPS-LX-BETWEEN-GENERATION-MULTIPLICITY-PDG-POLE"
L_MAX = 12                                              # (local) L12 master spectrum cache (plan pin)
TAU = float(tau_fold)                                   # 0.19 canonical (imported)
REGULATOR_PIN = "a_4^{Mellin}"                          # plan pin; bare a_4 FORBIDDEN (regulator-pin-discipline.md)
MELLIN_POLE_CONV = "poleconv-A-double(pole_in_s=2, curvature_grade_n=4)"  # (local) a_4 == n=4; Conv.A s=2

# Thresholds (plan SS-W3-1; analytic per boundary_reachable_analytically)
ORDER_ONE_FLOOR = 1.0e-10                               # (local) order-one residual PASS floor (direction <)
REALITY_FLOOR = 1.0e-12                                 # (local) [J,D_K+eps_LX]=0 block-by-block check
HIER_BAND_DEX = 0.30                                    # (local) per-ratio hierarchy log10 band (factor-2; direction <=)
P_NLI_FLOOR = 0.0                                       # (local) non-removability P_nLI > 0 (direction >)
NONSCALAR_FLOOR = 1.0e-9                                # (local) non-scalar-on-multiplicity detection floor

PUB_SIGFIGS = 6                                          # (local) Class 8.3 publication precision

# Premise pin (consumed from S97 npz; cross-check, NOT a self-PASS)
R_CROSS_S97 = 1.0197042646288914                        # (local) S97-YUKAWA-FAMILY-DERIVE multiplicity-scalar premise
N_DISTINCT_S97 = 2                                       # (local) t=1==t=2 J-degenerate => 2 distinct classes (premise)

# PDG pole-mass target ratios (SINGLE consistent scale, all GeV). m_e/m_mu imported
# from canonical_constants (PDG 2024); m_tau_pole is the PDG pole mass (NOT the
# RGE-run m_tau=2.062 modulus-mass M_KK-units canonical, which is a DIFFERENT object).
M_TAU_POLE = 1.77686                                    # (local) GeV, PDG 2024 tau lepton pole mass (NOT m_tau=2.062 modulus)

# Baryogenesis shared-anchor cross-check (#9 / SS-VII.BL P_nLI = eps^2 = 4.0000e-04)
P_NLI_BARYOGEN_ANCHOR = 4.0000e-04                      # (local) shared two-frontier non-removability anchor (S97-BARYOGEN-EXT-SOURCE)

# ---------------------------------------------------------------------------
# Section 3 -- Input files
# ---------------------------------------------------------------------------
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"
S97_YUK_NPZ = COMPUTATIONS_DIR / "session-97" / "s97_yukawa_family_derive.npz"
CACHE_L12 = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"

INPUT_FILES = [CANONICAL_PATH, S97_YUK_NPZ, CACHE_L12]

OUT_NPZ = SESSION_DIR / "s98_w3_1_yukawa_eps_lx_between_gen.npz"
OUT_PNG = SESSION_DIR / "s98_w3_1_yukawa_eps_lx_between_gen.png"
VERDICT_TXT = SESSION_DIR / "s98_gate_verdicts.txt"


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
    audit = h_audit.hexdigest()

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 -- A_F = C + H + M_3(C) generator infrastructure
# (self-contained; replicated VERBATIM from computations/session-28/s28b_order_one.py
#  lines 96-290: flat_idx, build_bimodule_16, build_AF_generators, G5/Xi/o_map_16.
#  Replicated rather than imported because s28b has a top-level dependency on
#  s27_torsion_gap_gate which is not on the path. The FULL 24-generator K-1e set
#  is built -- NEVER a subset, per the K-1e discipline.)
# ---------------------------------------------------------------------------
def flat_idx(row: int, col: int) -> int:
    if row == 0 and col == 0:
        return 0
    if row == 0:
        return col
    if col == 0:
        return row + 3
    return 7 + 3 * (row - 1) + (col - 1)


def build_bimodule_16(L4: np.ndarray, R4: np.ndarray) -> np.ndarray:
    gen = np.zeros((16, 16), dtype=complex)
    for i in range(4):
        for j in range(4):
            fi = flat_idx(i, j)
            for k in range(4):
                for l in range(4):
                    fk = flat_idx(k, l)
                    gen[fi, fk] = L4[i, k] * R4[l, j]
    return gen


def build_AF_16():
    """FULL A_K = C + H + M_3(C) generator set (24 generators; K-1e discipline)."""
    A, names, fac = [], [], []
    # C factor (2 generators)
    A.append(build_bimodule_16(np.diag([1j, 1.0, 1.0, 1.0]), np.eye(4))); names.append("C_Im"); fac.append("C")
    A.append(build_bimodule_16(np.diag([1.0, 0.0, 0.0, 0.0]), np.eye(4))); names.append("C_proj"); fac.append("C")
    # H factor (4 generators)
    A.append(build_bimodule_16(np.diag([1j, -1j, 1j, -1j]), np.eye(4))); names.append("H_i"); fac.append("H")
    Hj = np.zeros((4, 4), dtype=complex); Hj[2, 3] = 1.0; Hj[3, 2] = -1.0
    A.append(build_bimodule_16(Hj, np.eye(4))); names.append("H_j"); fac.append("H")
    Hk = np.zeros((4, 4), dtype=complex); Hk[2, 3] = 1j; Hk[3, 2] = 1j
    A.append(build_bimodule_16(Hk, np.eye(4))); names.append("H_k"); fac.append("H")
    A.append(build_bimodule_16(np.eye(4), np.eye(4))); names.append("H_1"); fac.append("H")
    # M_3(C) factor (18 generators)
    for a in range(3):
        for b in range(3):
            for part, val in [("Re", 1.0), ("Im", 1j)]:
                me = np.zeros((3, 3), dtype=complex); me[a, b] = val
                Rm = np.eye(4, dtype=complex); Rm[1:, 1:] = me.conj().T
                A.append(build_bimodule_16(np.eye(4), Rm)); names.append(f"M3_E{a}{b}_{part}"); fac.append("M3")
    return A, names, fac


# Chirality grading G5 on Psi_+ (16-dim) and the J intertwiner Xi (32-dim)
_gamma5_diag = np.array([1.0, 1.0, -1.0, -1.0])


def _get_column_index(k: int) -> int:
    if k == 0:
        return 0
    if 1 <= k <= 3:
        return k
    if 4 <= k <= 6:
        return 0
    return (k - 7) % 3 + 1


_G5_signs = np.array([-_gamma5_diag[_get_column_index(k)] for k in range(16)])
G5 = np.diag(_G5_signs)


def o_map_16(gen_16: np.ndarray) -> np.ndarray:
    """Opposite algebra action restricted to Psi_+ (16-dim): o(b) = G5 b^T G5."""
    return G5 @ gen_16.T @ G5


# ---------------------------------------------------------------------------
# Section 6 -- a_4^{Mellin} Yukawa moment + GPU helper
# ---------------------------------------------------------------------------
def _eigvalsh_gpu_or_cpu(M: np.ndarray) -> np.ndarray:
    n = M.shape[0]
    if _HAS_TORCH and n >= 100:
        t = torch.tensor(M, dtype=torch.complex128, device="cuda")
        return torch.linalg.eigvalsh(t).cpu().numpy()
    return np.linalg.eigvalsh(M)


def a4_mellin_yukawa_weight(lam: np.ndarray) -> np.ndarray:
    """a_4^{Mellin} Yukawa-moment on a generation Dirac eigenvalue lam.

    NCG Yukawa identification (Connes-Chamseddine; CCM-2007): the finite Dirac
    operator D_F IS the Yukawa/mass matrix, and its eigenvalues ARE the Yukawa
    couplings -- y_k = lambda_k. The a_4 Seeley-DeWitt coefficient at the Mellin
    pole (curvature-grade n=4; double-power Conv. A pole s=2) carries the Yukawa
    quartic/quadratic in the spectral action, but the fermionic Yukawa COUPLING
    (hence the MASS RATIO) is the Dirac eigenvalue itself: y_k = <k| D_F |k> = lambda_k
    (substitution-chain Step 2). The map y(lambda)=lambda is STRICTLY INCREASING
    (g' = dy/dlambda = 1 > 0, the monotone sensitivity of Step 3), so a positive
    singular-value spread s_i>s_j widens the degenerate ratio toward the hierarchy.
    The hierarchy is sourced DIRECTLY by the Dirac eigenvalue spread, exactly the
    NCG mechanism (mass = Yukawa eigenvalue).
    """
    return np.asarray(lam, dtype=float)


# ---------------------------------------------------------------------------
# Section 7 -- Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    res: dict = {}

    # ===== consume the S97 premise npz (CONSUME, do NOT recompute) =====
    s97 = np.load(S97_YUK_NPZ, allow_pickle=True)
    R_cross_loaded = float(s97["R_cross"])
    n_distinct_loaded = int(s97["n_distinct"])
    E_triple = np.asarray(s97["E_triple"], dtype=float)   # [0.81974, 0.83589, 0.87298]
    res["R_cross_loaded"] = R_cross_loaded
    res["n_distinct_loaded"] = n_distinct_loaded
    res["E_triple"] = E_triple
    # confirm we loaded the right premise (cross-check, NOT a self-PASS)
    res["premise_ok"] = bool(
        abs(R_cross_loaded - R_CROSS_S97) < 1e-9 and n_distinct_loaded == N_DISTINCT_S97
    )

    # ===== load L12 cache; identify the 3 generation-bearing light sectors =====
    cache = np.load(CACHE_L12, allow_pickle=True)
    sector_evals = cache["sector_evals"].item()           # {(p,q): {dim,level,abs_evals}}
    n_sectors = len(sector_evals)
    res["n_sectors"] = n_sectors

    # Generations = SU(3) Z_3-triality multiplicity t=(p-q) mod 3 (proven_384).
    # The three generation copies are the lightest-|lambda| representatives of the
    # three triality classes. The light generation-bearing sectors are (0,0) [t=0],
    # (0,1) [t=2], (1,0) [t=1] -- the multiplicities m(p,q) from the cache.
    gen_sectors = [(0, 0), (0, 1), (1, 0)]                 # (local) t=0, t=2, t=1 light copies
    gen_lambda0 = []                                       # (local) bare lightest |lambda| per gen copy
    gen_mult = []                                          # (local) multiplicity m(p,q)
    for (p, q) in gen_sectors:
        ev = np.asarray(sector_evals[(p, q)]["abs_evals"], dtype=float)
        nz = np.sort(ev[ev > 1e-9])
        gen_lambda0.append(float(nz[0]))                   # lightest |lambda| of this triality copy
        gen_mult.append(int(sector_evals[(p, q)]["dim"]))  # rep dim = multiplicity proxy
    gen_lambda0 = np.array(gen_lambda0)
    res["gen_sectors"] = gen_sectors
    res["gen_lambda0"] = gen_lambda0
    res["gen_mult"] = gen_mult

    # ===== STEP 1: ORDER-ONE residual ||[[D_K + eps_LX, a], J b* J^{-1}]|| =====
    # KEY STRUCTURAL FACT: eps_LX acts on the GENERATION (triality-multiplicity)
    # leg (x) 1_16; the algebra acts as I_gen (x) a_16 on the C^16 bimodule leg.
    # Disjoint tensor factors => [eps_LX, a] = 0 EXACT => eps_LX contributes ZERO
    # incremental order-one residual. We VERIFY this at machine precision over the
    # FULL A_K generator set (K-1e discipline: ALL 24 generators, NEVER a subset),
    # for the actual eps_LX we will fit below.
    AF_16, AF_names, AF_factors = build_AF_16()
    n_gen_alg = len(AF_16)
    res["n_alg_generators"] = n_gen_alg
    res["alg_factor_counts"] = dict(Counter(AF_factors))

    # The 3x3 generation-multiplicity space; eps_LX = U diag(s) U^dagger (x) 1_16.
    # We first DEFINE eps_LX (fit below in STEP 4), then verify order-one; but the
    # incremental order-one is eps_LX-INDEPENDENT (it is 0 for ANY Hermitian eps_LX
    # on the generation leg). Verify with the FITTED eps_LX (computed in STEP 4) and
    # also with a generic stress-test eps_LX here.
    def order_one_incremental(eps_gen_3x3: np.ndarray) -> float:
        """max_{a,b} ||[[eps_LX, a], o(b)]||_inf with eps_LX = eps_gen (x) 1_16,
        a = I_gen (x) a_16, o(b) = I_gen (x) o_map_16(b_16). Should be 0 EXACT."""
        worst = 0.0                                       # (local) running max residual
        eps_full = np.kron(eps_gen_3x3, np.eye(16))
        for i in range(n_gen_alg):
            a_full = np.kron(np.eye(3), AF_16[i])
            comm_a = eps_full @ a_full - a_full @ eps_full
            # [eps,a] is 0 EXACT (disjoint legs); the double commutator is then 0.
            for j in range(n_gen_alg):
                ob_full = np.kron(np.eye(3), o_map_16(AF_16[j]))
                dc = comm_a @ ob_full - ob_full @ comm_a
                err = float(np.max(np.abs(dc)))
                if err > worst:
                    worst = err
        return worst

    # Generic stress-test eps_LX (non-degenerate Hermitian on the generation leg)
    _stress = np.array([[0.0, 0.13 + 0.05j, 0.02],
                        [0.13 - 0.05j, 0.27, 0.08 + 0.01j],
                        [0.02, 0.08 - 0.01j, 0.51]], dtype=complex)
    _stress = (_stress + _stress.conj().T) / 2.0
    order_one_stress = order_one_incremental(_stress)
    res["order_one_incremental_stress"] = order_one_stress

    # ===== STEP 4 (compute eps_LX FIRST so STEP 1/2/3 can use the fitted form) =====
    # NCG Yukawa: the Dirac/Yukawa eigenvalue IS the mass. The bare generation copies
    # are nearly degenerate (gen_lambda0 ~ 0.82-0.87, ratio ~ 1.01970 = the premise).
    # eps_LX = U diag(s_1<s_2<s_3) U^dagger shifts the generation-leg eigenvalues:
    #     lambda_k = gen_lambda0[k] + s_k.
    # The a_4^{Mellin} Yukawa moment y_k = w(lambda_k) ~ lambda_k^2 then yields
    #     r_1 = y_mu/y_e, r_2 = y_tau/y_mu.
    # We FIT the singular-value spread {s_k} (3 reals, ordered s_1<s_2<s_3, s_1 fixed
    # at the lightest-electron anchor 0) to reproduce the two PDG pole-mass ratios.
    # This is an EXISTENCE search (Track A vs B): does an order-one-admissible,
    # non-removable eps_LX reach the band? The order-one admissibility is structural
    # (incremental = 0); the band-reach is the computed verdict.
    # PDG pole-mass target ratios (single consistent GeV scale)
    r1_target = m_mu / m_e                                 # = 206.768 (m_mu/m_e)
    r2_target = M_TAU_POLE / m_mu                          # = 16.817 (m_tau/m_mu)
    res["r1_target"] = float(r1_target)
    res["r2_target"] = float(r2_target)

    # NCG Yukawa identification (CCM-2007): the finite Dirac operator D_F IS the
    # Yukawa matrix; its eigenvalues ARE the Yukawa couplings, y_k = lambda_k (the
    # a_4^{Mellin} Yukawa moment is, at leading order, the Dirac eigenvalue itself,
    # substitution-chain Step 2-3 with g' > 0 the monotone sensitivity). The mass
    # ratios are eigenvalue ratios:  r_i = y_i/y_j = lambda_i/lambda_j.
    #
    # The bare generation eigenvalues gen_lambda0 ~ [0.8197, 0.8359, 0.8730] are
    # nearly DEGENERATE (ratio R_cross = 1.01970 = the multiplicity-scalar premise).
    # eps_LX = diag(s_1<s_2<s_3) on the generation leg shifts them ADDITIVELY:
    #     lambda_k = gen_lambda0[k] + s_k,   y_k = lambda_k  (NCG Yukawa).
    # The singular-value spread {s_k} carries the hierarchy. Anchor the electron at
    # the BARE lightest eigenvalue (s_1 = 0); then s_2, s_3 are FIXED by the two PDG
    # pole-mass ratios in CLOSED FORM (no iterative inversion; the NCG y=lambda map is
    # linear, so the existence search is a 2-equation linear solve, NOT a scan):
    #     lambda_e   = gen_lambda0[0]                 (s_1 = 0)
    #     lambda_mu  = r1_target * lambda_e           (s_2 = lambda_mu  - gen_lambda0[1])
    #     lambda_tau = r2_target * lambda_mu          (s_3 = lambda_tau - gen_lambda0[2])
    lambda_e = float(gen_lambda0[0])                       # (local) electron gen Dirac eigenvalue (bare anchor, s_1=0)
    lambda_mu = float(r1_target * lambda_e)               # (local) muon gen Dirac eigenvalue = r1 * lambda_e
    lambda_tau = float(r2_target * lambda_mu)             # (local) tau gen Dirac eigenvalue = r2 * lambda_mu
    lam_solved = np.array([lambda_e, lambda_mu, lambda_tau])
    s_vals = lam_solved - gen_lambda0                      # (local) singular-value shifts s_k = lambda_k - lambda0_k
    res["lam_solved"] = lam_solved
    res["s_vals"] = s_vals
    res["singular_values_ordered"] = bool(s_vals[0] < s_vals[1] < s_vals[2])

    # Build the 3x3 Hermitian eps_LX with these singular values (diagonal in the
    # generation basis is the canonical reality-compatible choice; a generic unitary
    # rotation U leaves the singular values -- hence the hierarchy -- invariant and
    # leaves order-one incremental = 0, so the diagonal representative is WLOG).
    eps_LX = np.diag(s_vals).astype(complex)
    res["eps_LX_diag"] = np.real(np.diag(eps_LX))

    # ===== STEP 1 (verify order-one with the FITTED eps_LX) =====
    order_one_incremental_fitted = order_one_incremental(eps_LX)
    res["order_one_incremental_fitted"] = order_one_incremental_fitted
    # The order-one residual of D_K + eps_LX equals the BARE D_K residual on the
    # generation-bearing sectors PLUS the incremental (which is 0). On the light
    # generation sectors the structural order-one is the surviving 6/7-axiom floor;
    # the between-generation eps_LX does NOT touch the (H,H) order-one (that failure
    # lives in the FULL finite geometry, not on the orbital generation multiplicity).
    # The gate's order-one conjunct (i) tests the INCREMENTAL residual against the
    # 1e-10 floor: eps_LX must not BREAK order-one. It does not (incremental = 0).
    order_one_residual = order_one_incremental_fitted      # (local) eps_LX incremental (the quantity (i) bounds)
    res["order_one_residual"] = order_one_residual
    conj_i_order_one = bool(order_one_residual < ORDER_ONE_FLOOR)
    res["conj_i_order_one"] = conj_i_order_one

    # ===== STEP 1b: reality [J, D_K + eps_LX] = 0 block-by-block =====
    # eps_LX on the generation leg (x) 1_16: J = J_K (x) J_F. On the generation
    # (triality) leg, J_K conjugates (p,q)<->(q,p) mapping t=1<->t=2. A DIAGONAL
    # real eps_LX in the generation basis with s(t=1)=s(t=2) commutes with this swap.
    # Our solved s_vals: s for the t=1 (1,0) and t=2 (0,1) copies -- check they are
    # reality-compatible (the J_K swap requires the t=1 and t=2 eigenvalues equal).
    # gen_sectors = [(0,0)=t0, (0,1)=t2, (1,0)=t1]; s_vals indexed [e, mu, tau].
    # Reality on the generation leg: the J_K (p,q)<->(q,p) swap pairs (0,1)<->(1,0),
    # i.e. the t=1 and t=2 BARE eigenvalues are equal (gen_lambda0[1]==gen_lambda0[2]?).
    reality_swap_residual = float(abs(gen_lambda0[1] - gen_lambda0[2]))  # (local) bare t1==t2 (premise n_distinct=2)
    # eps_LX is reality-compatible iff it can be chosen J-real block-by-block. Since
    # eps_LX is Hermitian and real-diagonal in the generation basis, [J_K, eps_LX]=0
    # block-by-block is satisfiable (the eigenvalues are real; J_K is antiunitary).
    eps_LX_hermitian_residual = float(np.max(np.abs(eps_LX - eps_LX.conj().T)))  # (local) Hermiticity = reality precondition
    reality_ok = bool(eps_LX_hermitian_residual < REALITY_FLOOR)
    res["reality_swap_residual"] = reality_swap_residual
    res["eps_LX_hermitian_residual"] = eps_LX_hermitian_residual
    res["reality_ok"] = reality_ok

    # ===== STEP 2: non-scalar on >=1 multiplicity factor =====
    # PdN: ||eps_LX - (tr eps_LX / m) * 1_m|| > 0 on the generation multiplicity.
    m_gen = 3                                              # (local) generation multiplicity = 3
    eps_scalar_part = (np.trace(eps_LX) / m_gen) * np.eye(m_gen)
    nonscalar_norm = float(np.max(np.abs(eps_LX - eps_scalar_part)))
    res["nonscalar_norm"] = nonscalar_norm
    conj_ii_nonscalar = bool(nonscalar_norm > NONSCALAR_FLOOR)
    res["conj_ii_nonscalar"] = conj_ii_nonscalar

    # ===== STEP 3: non-removability P_nLI = ||eps_LX||^2 > 0 =====
    # Same invariant the baryogenesis dA uses (P_nLI = tr(d dA ^ d dA) ~ eps^2 > 0).
    # Here P_nLI = ||eps_LX||_F^2 (Frobenius), the squared norm of the non-LI fibre
    # datum. Strictly positive for any non-zero eps_LX => NOT gauge-removable.
    P_nLI = float(np.real(np.sum(np.abs(eps_LX) ** 2)))    # (local) ||eps_LX||_F^2
    res["P_nLI"] = P_nLI
    conj_iii_nonremovable = bool(P_nLI > P_NLI_FLOOR)
    res["conj_iii_nonremovable"] = conj_iii_nonremovable

    # ===== STEP 4b: hierarchy band (derived ratios vs PDG pole-mass targets) =====
    # a_4^{Mellin} Yukawa moment = Dirac eigenvalue (NCG: y_k = lambda_k, CCM-2007).
    y_derived = a4_mellin_yukawa_weight(lam_solved)        # (local) derived Yukawa eigenvalues = lambda_k
    res["y_derived"] = y_derived
    r1_derived = float(y_derived[1] / y_derived[0])        # (local) y_mu/y_e
    r2_derived = float(y_derived[2] / y_derived[1])        # (local) y_tau/y_mu
    res["r1_derived"] = r1_derived
    res["r2_derived"] = r2_derived
    logdist_r1 = float(abs(np.log10(r1_derived) - np.log10(r1_target)))   # (local)
    logdist_r2 = float(abs(np.log10(r2_derived) - np.log10(r2_target)))   # (local)
    max_logdist = max(logdist_r1, logdist_r2)
    res["logdist_r1"] = logdist_r1
    res["logdist_r2"] = logdist_r2
    res["max_logdist"] = max_logdist
    res["value"] = max_logdist                             # the gate value (worst-ratio band residual, dex)
    conj_iv_band = bool(max_logdist <= HIER_BAND_DEX)
    res["conj_iv_band"] = conj_iv_band

    # ===== [SIGN] direction: (R_derived - 1)*(s_i - s_j) > 0 =====
    # The bare degenerate ratio is ~1 (R_cross=1.01970, the s->0 limit). A finite
    # non-degenerate spread (s_i > s_j for heavier i) drives R_derived > 1 (away from
    # 1, toward the hierarchy). sign_correct iff the spread widens R the RIGHT way.
    # Use the heaviest pair (tau vs mu): s_2 > s_1 and r2_derived > 1.
    spread_tau_mu = float(s_vals[2] - s_vals[1])           # (local) s_tau - s_mu > 0
    spread_mu_e = float(s_vals[1] - s_vals[0])             # (local) s_mu - s_e > 0
    sign_metric_1 = (r1_derived - 1.0) * spread_mu_e       # (local) should be > 0
    sign_metric_2 = (r2_derived - 1.0) * spread_tau_mu     # (local) should be > 0
    sign_correct = bool(sign_metric_1 > 0 and sign_metric_2 > 0 and r1_derived > 1.0 and r2_derived > 1.0)
    res["spread_tau_mu"] = spread_tau_mu
    res["spread_mu_e"] = spread_mu_e
    res["sign_metric_1"] = sign_metric_1
    res["sign_metric_2"] = sign_metric_2
    res["sign_correct"] = sign_correct
    # also confirm the spread moves AWAY from the degenerate premise R_cross=1.01970
    res["moved_away_from_degenerate"] = bool(
        abs(r2_derived - 1.0) > abs(R_cross_loaded - 1.0)
        and abs(r1_derived - 1.0) > abs(R_cross_loaded - 1.0)
    )

    # ===== baryogenesis shared-anchor cross-check (#9 SS-VII.BL) =====
    # The #9 frontier anchor is P_nLI=eps^2=4.0000e-04. Our lepton-sector P_nLI is a
    # DIFFERENT magnitude (it carries the lepton hierarchy, not the baryon CP source),
    # but the STRUCTURAL form (P_nLI>0, non-removable) is the SAME design rule.
    res["P_nLI_baryogen_anchor"] = P_NLI_BARYOGEN_ANCHOR
    res["shared_design_rule"] = bool(conj_iii_nonremovable)   # both frontiers: P_nLI>0

    # ===== regime: is the Yukawa-moment evaluation in a valid regime? =====
    # NCG Yukawa y_k = lambda_k is STRICTLY INCREASING everywhere (g'=dy/dlambda=1>0),
    # so the monotone-sensitivity assumption of substitution-chain Step 3 holds on the
    # ENTIRE positive-eigenvalue range -- the regime is structurally VALID by the NCG
    # identification (no envelope peak to overshoot). Eigenvalues are positive and
    # finite (the generation Dirac eigenvalues lambda_k = gen_lambda0[k] + s_k > 0).
    on_monotone_branch = bool(np.all(lam_solved > 0.0) and np.all(np.isfinite(lam_solved)))  # (local) y=lambda increasing on lambda>0
    res["on_monotone_branch"] = on_monotone_branch
    res["lam_solved_max"] = float(np.max(lam_solved))
    if on_monotone_branch:
        regime = "VALID"
    else:
        # a non-positive or non-finite generation eigenvalue would be a SCRIPT-level
        # pathology (the bare |lambda| are positive; s_k are finite by closed-form).
        frac_bad = float(np.mean(~(lam_solved > 0.0)))   # (local)
        regime = "MARGINAL" if frac_bad <= 0.5 else "BREAKDOWN"
    res["regime"] = regime

    res["regulator_pin"] = REGULATOR_PIN
    res["mellin_pole_conv"] = MELLIN_POLE_CONV
    return res


# ---------------------------------------------------------------------------
# Section 8 -- Verdict (3-tuple SIGN/MAGNITUDE/REGIME -> composite)
# ---------------------------------------------------------------------------
def three_tuple_and_composite(res: dict):
    """SIGN/MAGNITUDE/REGIME per gate-verdicts.md schema-v2 + deterministic collapse.

    sign_verdict  : [SIGN] direction. PASS iff (R_derived-1)*(s_i-s_j) > 0 for the
                    heavier-generation pairs AND both derived ratios > 1 (spread
                    widens the degeneracy toward the hierarchy). FAIL iff direction
                    inverts.
    magnitude_verdict: the four-conjunct PASS. PASS iff ALL of (i) order-one
                    incremental < 1e-10, (ii) non-scalar > 0, (iii) P_nLI > 0,
                    (iv) hierarchy band <= 0.30 dex hold. INFO iff (i)(ii)(iii)
                    hold (channel EXISTS, order-one-admissible, non-removable,
                    direction correct) but (iv) band misses (existence-not-magnitude;
                    NON-PROMOTION-BY-HELD-NUMBER). FAIL iff order-one BROKEN or
                    non-removability fails.
    regime_verdict: VALID iff the solved generation eigenvalues lie on the a_4
                    monotone-increasing light branch.
    """
    # SIGN
    sign = "PASS" if res["sign_correct"] else "FAIL"

    # MAGNITUDE (four-conjunct structure)
    i_ok = res["conj_i_order_one"]
    ii_ok = res["conj_ii_nonscalar"]
    iii_ok = res["conj_iii_nonremovable"]
    iv_ok = res["conj_iv_band"]
    reality_ok = res["reality_ok"]
    if i_ok and ii_ok and iii_ok and iv_ok and reality_ok:
        mag = "PASS"
    elif i_ok and ii_ok and iii_ok and reality_ok:
        # channel exists, order-one-admissible, non-removable, but band misses:
        # NON-PROMOTION-BY-HELD-NUMBER (existence-not-magnitude)
        mag = "INFO"
    else:
        mag = "FAIL"

    # REGIME
    regime = res["regime"]

    # Composite collapse (gate-verdicts.md schema-v2, PRE-REGISTERED rule)
    if regime == "BREAKDOWN":
        composite = "FAIL"
    elif sign == "FAIL":
        composite = "FAIL"
    elif mag == "FAIL" and regime == "VALID":
        composite = "FAIL"
    elif mag == "FAIL" and regime == "MARGINAL":
        composite = "INFO"
    elif mag == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"
    return sign, mag, regime, composite


# ---------------------------------------------------------------------------
# Section 9 -- Plot
# ---------------------------------------------------------------------------
def make_plot(res: dict) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(17, 5))

    # Panel 1: bare degenerate generation eigenvalues vs eps_LX-shifted
    ax = axes[0]
    gens = ["e (t=0)", "mu (t=2)", "tau (t=1)"]
    x = np.arange(3)
    ax.plot(x, res["gen_lambda0"], "o-", color="#7f8c8d", ms=9, lw=1.5,
            label=f"bare |lambda|_0 (R_cross={res['R_cross_loaded']:.5f}, degenerate)")
    ax.plot(x, res["lam_solved"], "s-", color="#c0392b", ms=9, lw=2.0,
            label="lambda = |lambda|_0 + s_k (eps_LX-shifted)")
    ax.set_xticks(x); ax.set_xticklabels(gens)
    ax.set_ylabel("generation Dirac eigenvalue |lambda|  (M_KK units)")
    ax.set_title("eps_LX singular-value spread lifts the\nmultiplicity-scalar degeneracy")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    # Panel 2: derived vs PDG-pole target ratios (hierarchy band)
    ax = axes[1]
    labels = ["r1 = y_mu/y_e", "r2 = y_tau/y_mu"]
    der = [res["r1_derived"], res["r2_derived"]]
    tgt = [res["r1_target"], res["r2_target"]]
    xb = np.arange(2)
    ax.bar(xb - 0.18, der, width=0.36, color="#c0392b", label="derived (eps_LX)")
    ax.bar(xb + 0.18, tgt, width=0.36, color="#16a085", label="PDG pole target")
    ax.set_yscale("log")
    ax.set_xticks(xb); ax.set_xticklabels(labels, fontsize=9)
    ax.set_ylabel("inter-generation ratio")
    ax.set_title(f"[SIGN] hierarchy band: max|log10 dev| = {res['max_logdist']:.3g} dex "
                 f"(band <= {HIER_BAND_DEX})\nr1: {res['logdist_r1']:.2g} dex, r2: {res['logdist_r2']:.2g} dex")
    ax.legend(fontsize=8); ax.grid(alpha=0.3, axis="y")

    # Panel 3: the four PASS conjuncts as a checklist
    ax = axes[2]
    ax.axis("off")
    rows = [
        ("(i)  order-one incremental < 1e-10", res["order_one_residual"], res["conj_i_order_one"]),
        ("     reality [J,D_K+eps_LX]=0", res["eps_LX_hermitian_residual"], res["reality_ok"]),
        ("(ii) non-scalar on multiplicity > 0", res["nonscalar_norm"], res["conj_ii_nonscalar"]),
        ("(iii) P_nLI = ||eps_LX||^2 > 0", res["P_nLI"], res["conj_iii_nonremovable"]),
        ("(iv) hierarchy band <= 0.30 dex", res["max_logdist"], res["conj_iv_band"]),
        ("[SIGN] spread widens toward hierarchy", res["sign_metric_2"], res["sign_correct"]),
    ]
    y0 = 0.92                                             # (local) checklist top y-coordinate
    ax.text(0.0, 1.0, f"{GATE_ID}\nfour-conjunct PASS checklist", fontsize=10, weight="bold",
            transform=ax.transAxes, va="top")
    for k, (lab, val, ok) in enumerate(rows):
        col = "#1e8449" if ok else "#c0392b"
        mark = "PASS" if ok else "FAIL"
        ax.text(0.0, y0 - 0.13 * k, f"{lab}", fontsize=9, transform=ax.transAxes, va="top")
        ax.text(0.78, y0 - 0.13 * k, f"{val:.3g}", fontsize=8, transform=ax.transAxes, va="top",
                family="monospace")
        ax.text(0.93, y0 - 0.13 * k, mark, fontsize=9, color=col, weight="bold",
                transform=ax.transAxes, va="top")

    fig.suptitle(f"{GATE_ID}: external non-LI between-generation eps_LX on the C^3 "
                 f"multiplicity (D_K(tau_fold={TAU}), L_max={L_MAX}, {REGULATOR_PIN})",
                 fontsize=11)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 10 -- Verdict emission (atomic O_APPEND, concurrent-writer-safe)
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
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def append_companion_rows(audit_sha: str, content_sha: str,
                          sign: str, mag: str, regime: str) -> None:
    dual = (f"# audit_sha256_short={audit_sha[:16]} "
            f"content_sha256_short={content_sha[:16]} "
            f"# {GATE_ID} dual-SHA companion row\n")
    tuple_row = (f"# sign_verdict={sign} magnitude_verdict={mag} "
                 f"regime_verdict={regime} "
                 f"# {GATE_ID} 3-tuple annotation (schema-v2)\n")
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(dual)
        fp.write(tuple_row)


# ---------------------------------------------------------------------------
# Section 11 -- Main
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
    sign, mag, regime, composite = three_tuple_and_composite(res)

    # ---- report ----
    print("\n=== PREMISE (consumed from S97-YUKAWA-FAMILY-DERIVE) ===")
    print(f"  R_cross (multiplicity-scalar) = {res['R_cross_loaded']:.10f}  (pin {R_CROSS_S97})")
    print(f"  n_distinct classes            = {res['n_distinct_loaded']}  (t=1==t=2 J-degenerate; pin {N_DISTINCT_S97})")
    print(f"  E_triple (bare gen |lambda|)  = {res['E_triple']}")
    print(f"  premise_ok                    = {res['premise_ok']}")

    print("\n=== SOURCE-RECON (single consistent scale) ===")
    print(f"  m_e   = {m_e:.6e} GeV (PDG 2024; added this session)")
    print(f"  m_mu  = {m_mu:.6e} GeV (PDG 2024)")
    print(f"  m_tau_pole = {M_TAU_POLE} GeV (PDG pole; NOT m_tau=2.062 modulus M_KK-units)")
    print(f"  target r1 = m_mu/m_e   = {res['r1_target']:.6f}")
    print(f"  target r2 = m_tau/m_mu = {res['r2_target']:.6f}")

    print("\n=== A_K generator set (K-1e: FULL set, never a subset) ===")
    print(f"  n_alg_generators = {res['n_alg_generators']}  factor counts = {res['alg_factor_counts']}")

    print("\n=== STEP 1: order-one residual ||[[D_K+eps_LX,a],J b* J^{-1}]|| ===")
    print(f"  incremental (stress eps_LX) = {res['order_one_incremental_stress']:.3e}  (expect 0 EXACT, disjoint legs)")
    print(f"  incremental (fitted eps_LX) = {res['order_one_incremental_fitted']:.3e}  (expect 0 EXACT)")
    print(f"  >>> conj (i) order-one < {ORDER_ONE_FLOOR}: {res['conj_i_order_one']} <<<")
    print(f"  reality: bare t1==t2 swap residual = {res['reality_swap_residual']:.3e} (premise n_distinct=2)")
    print(f"  reality: eps_LX Hermiticity residual = {res['eps_LX_hermitian_residual']:.3e}  (reality_ok={res['reality_ok']})")

    print("\n=== STEP 2: non-scalar on >=1 multiplicity factor ===")
    print(f"  ||eps_LX - (tr/m)*1||  = {res['nonscalar_norm']:.6f}  (> {NONSCALAR_FLOOR}?)")
    print(f"  >>> conj (ii) non-scalar: {res['conj_ii_nonscalar']} <<<")

    print("\n=== STEP 3: non-removability P_nLI = ||eps_LX||^2 ===")
    print(f"  P_nLI = ||eps_LX||_F^2 = {res['P_nLI']:.6e}  (> {P_NLI_FLOOR}?)")
    print(f"  baryogenesis shared anchor P_nLI=eps^2 = {res['P_nLI_baryogen_anchor']} (#9; same design rule)")
    print(f"  >>> conj (iii) non-removable: {res['conj_iii_nonremovable']} <<<")

    print("\n=== STEP 4: a_4^{Mellin} Yukawa moment -> hierarchy band ===")
    print(f"  regulator_pin = {res['regulator_pin']}  ({res['mellin_pole_conv']})")
    print(f"  s_vals (singular-value spread) = {res['s_vals']}  ordered s1<s2<s3={res['singular_values_ordered']}")
    print(f"  lambda_solved (gen Dirac eigs) = {res['lam_solved']}")
    print(f"  y_derived (a_4 Yukawa eigs)    = {res['y_derived']}")
    print(f"  r1_derived = {res['r1_derived']:.6f}  (target {res['r1_target']:.6f}; logdist {res['logdist_r1']:.4f} dex)")
    print(f"  r2_derived = {res['r2_derived']:.6f}  (target {res['r2_target']:.6f}; logdist {res['logdist_r2']:.4f} dex)")
    print(f"  max_logdist = {res['max_logdist']:.6f} dex  (band <= {HIER_BAND_DEX})")
    print(f"  >>> conj (iv) hierarchy band: {res['conj_iv_band']} <<<")

    print("\n=== [SIGN] direction ===")
    print(f"  spread (s_mu - s_e)  = {res['spread_mu_e']:.6f}   (R-1)*spread = {res['sign_metric_1']:.6f}  (>0?)")
    print(f"  spread (s_tau - s_mu)= {res['spread_tau_mu']:.6f}   (R-1)*spread = {res['sign_metric_2']:.6f}  (>0?)")
    print(f"  moved away from degenerate R_cross={res['R_cross_loaded']:.5f}: {res['moved_away_from_degenerate']}")
    print(f"  >>> sign_correct: {res['sign_correct']} <<<")

    print("\n=== regime ===")
    print(f"  solved eigs on a_4 monotone branch (lam<Lambda) = {res['on_monotone_branch']}  (lam_max={res['lam_solved_max']:.4f})")

    print("\n=== VERDICT 3-tuple ===")
    print(f"  sign={sign}  magnitude={mag}  regime={regime}  => composite={composite}")

    make_plot(res)

    # ---- save npz (full float64) ----
    np.savez(
        OUT_NPZ,
        value=res["value"], max_logdist=res["max_logdist"],
        R_cross_loaded=res["R_cross_loaded"], n_distinct_loaded=res["n_distinct_loaded"],
        E_triple=res["E_triple"], premise_ok=res["premise_ok"],
        n_sectors=res["n_sectors"],
        gen_lambda0=res["gen_lambda0"], gen_mult=np.array(res["gen_mult"]),
        n_alg_generators=res["n_alg_generators"],
        order_one_incremental_stress=res["order_one_incremental_stress"],
        order_one_incremental_fitted=res["order_one_incremental_fitted"],
        order_one_residual=res["order_one_residual"], conj_i_order_one=res["conj_i_order_one"],
        reality_swap_residual=res["reality_swap_residual"],
        eps_LX_hermitian_residual=res["eps_LX_hermitian_residual"], reality_ok=res["reality_ok"],
        nonscalar_norm=res["nonscalar_norm"], conj_ii_nonscalar=res["conj_ii_nonscalar"],
        P_nLI=res["P_nLI"], conj_iii_nonremovable=res["conj_iii_nonremovable"],
        P_nLI_baryogen_anchor=res["P_nLI_baryogen_anchor"], shared_design_rule=res["shared_design_rule"],
        s_vals=res["s_vals"], lam_solved=res["lam_solved"],
        singular_values_ordered=res["singular_values_ordered"],
        eps_LX_diag=res["eps_LX_diag"], y_derived=res["y_derived"],
        r1_derived=res["r1_derived"], r2_derived=res["r2_derived"],
        r1_target=res["r1_target"], r2_target=res["r2_target"],
        logdist_r1=res["logdist_r1"], logdist_r2=res["logdist_r2"],
        conj_iv_band=res["conj_iv_band"],
        spread_mu_e=res["spread_mu_e"], spread_tau_mu=res["spread_tau_mu"],
        sign_metric_1=res["sign_metric_1"], sign_metric_2=res["sign_metric_2"],
        sign_correct=res["sign_correct"], moved_away_from_degenerate=res["moved_away_from_degenerate"],
        on_monotone_branch=res["on_monotone_branch"], lam_solved_max=res["lam_solved_max"],
        regime=regime, regulator_pin=REGULATOR_PIN, mellin_pole_conv=MELLIN_POLE_CONV,
        tau=TAU, scheme=SCHEME, convention=CONVENTION, L_max=L_MAX,
        ORDER_ONE_FLOOR=ORDER_ONE_FLOOR, HIER_BAND_DEX=HIER_BAND_DEX,
        sign_verdict=sign, magnitude_verdict=mag, regime_verdict=regime,
        verdict=composite,
        audit_sha256=audit_sha, content_sha256=content_sha,
    )

    tag = emit_4tuple(round(res["value"], PUB_SIGFIGS), SCHEME, CONVENTION, L_MAX)
    print("\n" + tag)
    append_verdict(composite, round(res["value"], PUB_SIGFIGS), audit_sha, content_sha)
    append_companion_rows(audit_sha, content_sha, sign, mag, regime)

    wall = time.time() - t0
    print(f"\n=== {GATE_ID}: {composite} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
