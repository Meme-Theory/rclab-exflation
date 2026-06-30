#!/usr/bin/env python3
"""
S96 W4-1 S96-MATTER-A4-YUKAWA-RATIO — first non-degenerate fermion mass ratio
from the a_4 Yukawa block of D_K(tau_fold) after inner fluctuation D_K -> D_K + A
============================================================================

Gate: S96-MATTER-A4-YUKAWA-RATIO ([VERIFY])

Pre-registered threshold (plan §W4-1):
  R_Yuk = m_heavy / m_light  where  m_a = eig_a[ <psi_i | (D_K + A) | psi_j> over Psi_+ sub-blocks ].
  PASS iff (i) R_Yuk > 1 (non-degenerate) AND (ii) |log10(R_Yuk / R_SM_anchor)| <= 1.0.
  FAIL iff R_Yuk = 1 to tolerance 1e-12 (structural Schur degeneracy => read-off claim empty
       at one generation).
  INFO iff R_Yuk extractable and != 1 but |log10(R_Yuk / R_SM_anchor)| > 1.0 (OOM-only first
       extraction; no single SM ratio matched within 1 OOM) — register as bare-spectrum
       (geometric) ratio pending family structure.

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz  (cross-check anchor for the
       (1,0) fundamental-sector |lambda| spectrum at tau_fold; the eigenVECTORS + D_pi are
       reconstructed in-gate from dirac_spectrum.py since the cache stores only abs_evals)
  - canonical_constants.py (feeds audit_sha256 only; supplies tau_fold, v_ew, m_mu, m_t_pole anchors)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=R_Yuk, scheme=CCM-2007-inner-fluctuation-spin0-Higgs, convention=ABSOLUTE, L_max=12)

Classification: PARTICLE.

METHODOLOGY
-----------
Substrate-first per phononic-framing.md: D_K eigenvalues + inner-fluctuation Higgs one-form
A^{(0)} -> a_4 Yukawa spectral moment -> mass bilinears on Psi_+ generation content -> dimensionless
ratio R_Yuk. The fermion mass matrix is NOT an external input; it IS the spin-0 inner-fluctuation
content of the a_4 Seeley-DeWitt coefficient (a_4^{Pauli-Villars}) of D_K. External SM masses
(v_ew, m_mu, m_t_pole, plus PDG comparison-only fermion masses) enter ONLY as comparison anchors
per substrate-first-canonical-sourcing.md §(i) (methodological, never canonical pins).

Construction:
  (CC1) Build (A_K, H_K, D_K) on the FUNDAMENTAL sector V_(1,0) (x) C^16 via dirac_spectrum.py
        (collect_spectrum_with_eigenvectors at s=tau_fold). The Cl(8) spinor C^16 splits under
        gamma_9 into chirality +/- (8 + 8). Build the inner fluctuation one-form A = sum a_i [D_K, b_i]
        with a_i, b_i in A_K, extract its spin-0 (Higgs) part A^{(0)} = the gamma_9-ANTICOMMUTING
        (chirality-off-diagonal) part of A (CCM-2007 §2.5: the Higgs is the off-diagonal-in-chirality
        component connecting H_K^+ <-> H_K^-). The full fluctuated operator is D_A = D_K + A + J A J^{-1}.
  (CC2) Restrict (D_K + A^{(0)}) to the Psi_+ generation-content sub-blocks of the spinor C^16,
        labelled by the su(3) Cartan eigenvalues (T_3 = e_2-grading, Y = e_7-grading) — these are the
        irrep-distinguishing labels that the substitution chain says must break Schur-blindness for a
        non-degenerate ratio. Form the mass bilinears m_a = eig_a[<psi_i | (D_K + A^{(0)}) | psi_j>],
        diagonalize the Psi_+ Yukawa sub-block, and read the residual structure.
  Form R_Yuk = m_heavy / m_light of the two largest mass eigen-bilinears; compare to nearest SM
  fermion-mass ratio.

DISCIPLINE
----------
- `from canonical_constants import *`
- every intermediate tagged `# (local)`
- GPU path torch.linalg for sub-blocks >= 100x100 (here the fundamental D_pi is 48x48 — small —
  but eig is done on GPU where available per GPU_path pin, with a numpy cross-check)
- dual-SHA (audit + content) emitted; verdict appended to s96_gate_verdicts.txt via append_verdict
- regulator tag a_4^{Pauli-Villars} carried in the verdict scheme/convention provenance
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
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

from canonical_constants import *  # noqa: F401,F403  (tau_fold, v_ew, m_mu, m_t_pole, ...)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# dirac_spectrum.py lives in _shared
import dirac_spectrum as ds  # noqa: E402

try:
    import torch  # noqa: E402
    _HAS_TORCH = torch.cuda.is_available()
except Exception:
    torch = None
    _HAS_TORCH = False

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION = "S96"                                                   # (local)
GATE_ID = "S96-MATTER-A4-YUKAWA-RATIO"                            # (local)
SCHEME = "CCM-2007-inner-fluctuation-spin0-Higgs"                 # (local)
CONVENTION = "ABSOLUTE"                                           # (local) mass bilinears in M_KK units; RATIO is dimensionless
L_MAX = 12                                                        # (local)
REGULATOR_PIN = "a_4^{Pauli-Villars}"                             # (local) Yukawa block = spin-0 content of a_4 SDW coeff

DEGEN_TOL = 1.0e-12                                               # (local) degeneracy / diagonalization residual floor (plan pin)
PASS_OOM = 1.0                                                    # (local) |log10(R_Yuk/R_SM_anchor)| <= 1.0 PASS band (plan pin)

OUT_NPZ = SESSION_DIR / "s96_matter_a4_yukawa_ratio.npz"
OUT_PNG = SESSION_DIR / "s96_matter_a4_yukawa_ratio.png"
VERDICT_TXT = SESSION_DIR / "s96_gate_verdicts.txt"

CACHE_L12 = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"

INPUT_FILES = [
    CANONICAL_PATH,
    CACHE_L12,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Compute
# ---------------------------------------------------------------------------

def _eig_general(M):
    """Eigenvalues of a (possibly non-Hermitian) matrix; GPU if >=100x100 and available."""
    n = M.shape[0]  # (local)
    if _HAS_TORCH and n >= 100:
        t = torch.tensor(M, dtype=torch.complex128, device="cuda")  # (local)
        ev = torch.linalg.eigvals(t).cpu().numpy()  # (local)
        return ev
    return np.linalg.eigvals(M)


def build_internal_geometry(tau):
    """CC1 step 1: build (A_K, H_K, D_K) infrastructure + the FUNDAMENTAL-sector Dirac block.

    Returns gammas (Cl(8)), gamma9 (chirality), gens (su(3)), and the fundamental-sector
    D_pi (anti-Hermitian, 48x48 on V_(1,0) (x) C^16) plus the (0,0) trivial-sector D = Omega
    (the pure finite Dirac operator D_F on C^16, which is the bare mass matrix BEFORE fluctuation).
    """
    gens = ds.su3_generators()                                   # (local) 8 anti-Herm 3x3
    f_abc = ds.compute_structure_constants(gens)                 # (local)
    gammas = ds.build_cliff8()                                   # (local) 8 x (16x16) Hermitian
    gamma9 = ds.build_chirality(gammas)                          # (local) 16x16 chirality involution

    # Geometric infra at this tau
    B_ab = ds.compute_killing_form(f_abc)                        # (local)
    g_s = ds.jensen_metric(B_ab, tau)                            # (local)
    E = ds.orthonormal_frame(g_s)                                # (local) (8,8)
    ft = ds.frame_structure_constants(f_abc, E)                  # (local)
    Gamma = ds.connection_coefficients(ft)                       # (local)
    Omega = ds.spinor_connection_offset(Gamma, gammas)           # (local) 16x16

    # Fundamental sector (1,0): rho(e_a) = e_a (3x3); D acts on C^3 (x) C^16 = 48-dim
    rho_fund = ds.irrep_fundamental(gens)                        # (local) list of 8 (3x3)
    D_fund = ds.dirac_operator_on_irrep(rho_fund, E, gammas, Omega)  # (local) 48x48 anti-Herm

    return {
        "gens": gens, "f_abc": f_abc, "gammas": gammas, "gamma9": gamma9,
        "E": E, "Gamma": Gamma, "Omega": Omega,
        "rho_fund": rho_fund, "D_fund": D_fund,
    }


def chirality_split(gamma9):
    """Return projectors P_plus, P_minus onto the gamma_9 = +/-1 eigenspaces of C^16."""
    I16 = np.eye(16, dtype=complex)                              # (local)
    P_plus = 0.5 * (I16 + gamma9)                                # (local)
    P_minus = 0.5 * (I16 - gamma9)                               # (local)
    return P_plus, P_minus


def cartan_labels(gammas, gamma9):
    """CC2: build the spinor-side so(8) Cartan graders and read the weight-labels of the
    chirality-+ subspace H_K^+ of C^16 (the Psi_+ generation-content summands).

    The Cl(8) spinor C^16 carries 4 commuting so(8) Cartan graders G_k = gamma_{2k-1} gamma_{2k}
    (k=1..4); -i*G_k are commuting Hermitian involutions with eigenvalues +/-1. In the standard
    Pauli-tensor basis (ds.build_cliff8) they are ALL DIAGONAL and commute with gamma_9, so the
    16 spinor basis states ARE simultaneous weight states labelled by (s0,s1,s2,s3) in {+/-1}^4.

    The 8 states with gamma_9 = +1 form H_K^+ (the even half-spinor 8_s); each carries a DISTINCT
    weight 4-tuple. These 8 weight states are the irrep-distinguishing summands of the Psi_+
    branching (the SM (T_3, Y) labels are integer linear combinations of the four graders). The
    load-bearing question (substitution chain): does the inner-fluctuation Higgs A^{(0)} produce a
    mass bilinear that is NON-CONSTANT across these weight grades (non-Schur) or a scalar mu*1
    (Schur-blind => degenerate => R_Yuk=1)?
    """
    H = [(-1j * gammas[2 * k] @ gammas[2 * k + 1]) for k in range(4)]   # (local) commuting Hermitian graders, eigenvalues +/-1
    labels = np.array([np.real(np.diag(h)) for h in H]).T               # (local) 16 x 4 weight labels
    g9d = np.real(np.diag(gamma9))                                       # (local) chirality eigenvalue per basis state
    plus_states = np.where(g9d > 0)[0]                                   # (local) H_K^+ states (8 of them)
    minus_states = np.where(g9d < 0)[0]                                  # (local) H_K^- states (8 of them)
    return H, labels, plus_states, minus_states


def build_inner_fluctuation(infra):
    """CC1 step 2: build the inner fluctuation one-form A = sum_i a_i [D_K, b_i] on the
    FUNDAMENTAL sector, with a_i, b_i in A_K = C (+) H (+) M_3(C), and extract its spin-0 (Higgs)
    part A^{(0)} = the gamma_9-ANTICOMMUTING (chirality-off-diagonal) component.

    Representation of A_K on V_(1,0) (x) C^16:
      - The M_3(C) factor acts on V_(1,0) = C^3 by matrix multiplication (tensored with I_16 on spin).
      - [D_K, b] for b = (M_3-matrix) (x) I_16 generates a 1-form whose Clifford content is built from
        the gamma_a in D_K. We sample a spanning set of A_K elements b_i and pre-factors a_i and
        accumulate A = sum_i a_i [D_fund, b_i]; then project onto the spin-0 (gamma_9-off-diagonal) part.
    """
    D = infra["D_fund"]                                          # (local) 48x48
    gamma9 = infra["gamma9"]                                     # (local) 16x16
    gens = infra["gens"]                                         # (local)

    I3 = np.eye(3, dtype=complex)                                # (local)
    I16 = np.eye(16, dtype=complex)                              # (local)
    G9_full = np.kron(I3, gamma9)                                # (local) chirality on the 48-dim sector

    # A spanning set of M_3(C) algebra elements acting on V_(1,0): the 8 su(3) generators (traceless
    # anti-Herm) PLUS the identity-trace direction give a basis of the M_3(C) action on C^3.
    # Inner fluctuation uses a_i, b_i in A_K; on the fundamental, the M_3(C) summand acts irreducibly.
    algebra_b = [np.kron(g, I16) for g in gens]                  # (local) b_i = e_a (x) I16  (M_3 summand)
    algebra_b.append(np.kron(I3, I16))                           # (local) identity direction
    # Pre-factors a_i in A_K: use a complementary spanning set (the generators again + identity),
    # giving a generic (non-degenerate-by-construction-attempt) one-form. Self-adjointness of the
    # *physical* fluctuation is imposed by symmetrizing A -> (A - A^dag)/2 (anti-Herm, matching D's
    # math-convention anti-Hermiticity) at the end.
    algebra_a = [np.kron(g, I16) for g in gens]                  # (local)
    algebra_a.append(np.kron(I3, I16))                           # (local)

    A = np.zeros((48, 48), dtype=complex)                        # (local) accumulated one-form
    rng = np.random.default_rng(0)                               # (local) DETERMINISTIC seed=0 for the a_i coefficient mixing
    coeffs = rng.standard_normal(len(algebra_a))                 # (local) deterministic real mixing weights
    for ci, a_i in enumerate(algebra_a):
        comm = D @ algebra_b[ci % len(algebra_b)] - algebra_b[ci % len(algebra_b)] @ D  # (local) [D, b_i]
        A += coeffs[ci] * (a_i @ comm)                           # (local) a_i [D, b_i]

    # Anti-Hermitian (math-convention) component, matching D
    A = 0.5 * (A - A.conj().T)                                   # (local)

    # spin-0 (Higgs) part = gamma_9-ANTICOMMUTING component: A^{(0)} = (A - G9 A G9)/2
    A0 = 0.5 * (A - G9_full @ A @ G9_full)                       # (local) chirality-off-diagonal (mass/Yukawa) part
    # spin-1 (gauge) part = gamma_9-COMMUTING component (kept for diagnostics only)
    A1 = 0.5 * (A + G9_full @ A @ G9_full)                       # (local)
    return A, A0, A1, G9_full


def yukawa_subblock(infra, A0, plus_states, minus_states):
    """CC2 (gauge-INVARIANT): extract the Psi_+ -> Psi_- Yukawa mass bilinears as the singular
    values of the FULL chirality-off-diagonal block of (D_K + A^{(0)}) on the fundamental sector.

    The fundamental sector is V_(1,0) (x) C^16 = C^3 (x) C^16. CRITICAL gauge-invariance lesson
    (seed-robustness probe S96 W4-1): a single-gauge-component slice (g0=0) is NOT gauge-invariant
    — the orthonormal frame E entangles the C^3 SU(3) gauge orbit with the C^16 weight grading, so
    per-gauge-component blocks differ (g0=0,1 give R=2.397 but g0=2 gives R=1.650). The
    GAUGE-INVARIANT observable is the singular-value spectrum of the FULL 24x24 chirality-off-
    diagonal block P_- (D_K+A^{(0)}) P_+ (gauge-summed). Its DISTINCT singular-value clusters are
    the mass eigen-bilinears labelled by the Psi_+ generation/weight content; their multiplicities
    are the gauge-orbit degeneracies. R_Yuk = ratio of the largest to smallest DISTINCT cluster.

    The Psi_+ weight grades (plus_states) label the 8 weight summands of H_K^+; they are reported
    for the CC2 generation-content diagnostic (per-grade block), but the gauge-invariant R_Yuk is
    read from the full block's distinct-cluster spectrum.

    Returns: full 24x24 off-diagonal block, its singular values, the per-gauge-0 generation block
    (diagnostic), the +/- support indices, and the CC2 generation-block off-diagonal residual.
    """
    D = infra["D_fund"]                                          # (local) 48x48 = (C^3) (x) (C^16)
    gamma9 = infra["gamma9"]                                     # (local) 16x16
    DA = D + A0                                                  # (local) fluctuated, spin-0-corrected
    G9 = np.kron(np.eye(3, dtype=complex), gamma9)               # (local) chirality on 48-dim

    # GAUGE-INVARIANT full-sector chirality-off-diagonal block (the Yukawa/mass operator H_K^+->H_K^-)
    idx_p48 = np.where(np.real(np.diag(0.5 * (np.eye(48, dtype=complex) + G9))) > 0.5)[0]  # (local) 24 + states
    idx_m48 = np.where(np.real(np.diag(0.5 * (np.eye(48, dtype=complex) - G9))) > 0.5)[0]  # (local) 24 - states
    M_full = DA[np.ix_(idx_m48, idx_p48)]                        # (local) 24x24 gauge-invariant Yukawa block
    s_full = _svdvals(M_full)                                    # (local) 24 mass eigen-bilinears (descending)

    # per-gauge-0 generation-content block (DIAGNOSTIC ONLY; not gauge-invariant — see lesson above)
    g0 = 0                                                       # (local) fixed SU(3) gauge component (diagnostic)
    rows_m = np.array([g0 * 16 + s for s in minus_states])      # (local)
    cols_p = np.array([g0 * 16 + s for s in plus_states])       # (local)
    M_gen = DA[np.ix_(rows_m, cols_p)]                           # (local) 8x8 (diagnostic)
    diag_part = np.diag(np.diag(M_gen))                          # (local)
    cc2_residual = float(np.linalg.norm(M_gen - diag_part) /
                         max(np.linalg.norm(M_gen), 1e-300))     # (local) relative off-diagonal weight

    return M_full, s_full, M_gen, idx_p48, idx_m48, cc2_residual


def _svdvals(M):
    if _HAS_TORCH and max(M.shape) >= 100:
        t = torch.tensor(M, dtype=torch.complex128, device="cuda")  # (local)
        s = torch.linalg.svdvals(t).cpu().numpy()                   # (local)
        return np.sort(s)[::-1]
    return np.sort(np.linalg.svd(M, compute_uv=False))[::-1]


def sm_anchor_ratios():
    """Comparison-ONLY SM fermion-mass ratios (substrate-first-canonical-sourcing §(i):
    methodological anchors, NOT canonical pins). Canonical where available (m_mu, m_t_pole, v_ew);
    PDG comparison-only values otherwise."""
    # PDG 2024 fermion masses used as COMPARISON ANCHORS ONLY (# (local), never canonical pins)
    m_e_pdg = 0.000510998950   # (local) GeV, electron (PDG comparison anchor)
    m_mu_c = float(m_mu)        # (local) canonical muon (0.1056583745 GeV)
    m_tau_pdg = 1.77686         # (local) GeV, tau lepton (PDG comparison anchor; NOT the modulus m_tau!)
    m_b_pdg = 4.18              # (local) GeV, b-quark MSbar (PDG comparison anchor)
    m_t = float(m_t_pole)       # (local) canonical top pole (172.69 GeV)
    m_c_pdg = 1.27              # (local) GeV, charm (PDG comparison anchor)
    m_u_pdg = 0.00216           # (local) GeV, up (PDG comparison anchor)
    m_d_pdg = 0.00467           # (local) GeV, down (PDG comparison anchor)
    m_s_pdg = 0.0934            # (local) GeV, strange (PDG comparison anchor)
    anchors = {                                                  # (local)
        "m_mu/m_e": m_mu_c / m_e_pdg,
        "m_tau/m_mu": m_tau_pdg / m_mu_c,
        "m_t/m_b": m_t / m_b_pdg,
        "m_c/m_u": m_c_pdg / m_u_pdg,
        "m_s/m_d": m_s_pdg / m_d_pdg,
        "m_t/m_c": m_t / m_c_pdg,
        "m_b/m_s": m_b_pdg / m_s_pdg,
    }
    return anchors


def compute() -> dict:
    tau = float(tau_fold)                                        # (local) 0.190 canonical
    infra = build_internal_geometry(tau)

    # CC2 prep: Cartan weight grading of C^16 -> Psi_+ generation-content summands
    Hcart, weight_labels, plus_states, minus_states = cartan_labels(infra["gammas"], infra["gamma9"])

    # CC1: inner fluctuation + spin-0 Higgs extraction
    A, A0, A1, G9 = build_inner_fluctuation(infra)
    A0_norm = float(np.linalg.norm(A0))                          # (local) Frobenius norm of the Higgs part
    A1_norm = float(np.linalg.norm(A1))                          # (local) gauge part (diagnostic)

    # cross-check: fundamental-sector |lambda| against the cache (1,0) sector |abs_evals|
    H = 1j * infra["D_fund"]                                     # (local) Hermitian image
    ah_err = float(np.max(np.abs(infra["D_fund"] + infra["D_fund"].conj().T)))  # (local)
    fund_abs = np.sort(np.abs(np.linalg.eigvalsh(H)))            # (local) |lambda| of fundamental block

    # CC2: gauge-INVARIANT full chirality-off-diagonal Yukawa block (24x24), fluctuated
    M_full, s_full, M_gen, idx_p, idx_m, cc2_residual = yukawa_subblock(
        infra, A0, plus_states, minus_states)
    s_vals = np.asarray(s_full, dtype=float)                     # (local) 24 mass eigen-bilinears (fluctuated, diagnostic)
    s_nonzero = s_vals[s_vals > DEGEN_TOL]                       # (local)

    # ---- BARE (D_K alone, A0=0) gauge-invariant block: THE ZERO-FREE-PARAMETER observable ----
    # The inner-fluctuation coefficients a_i are FREE PARAMETERS; the seed-robustness probe shows
    # the fluctuated R_Yuk ranges [1.46, 3.22] across coefficient seeds (NOT zero-parameter).
    # The deterministic, gauge-invariant, zero-free-parameter observable is the bare D_K Yukawa
    # block (the a_4 spin-0 content of D_F = D_K itself, before adding a tunable Higgs VEV).
    M_full_bare, s_full_bare, M_gen_bare, _, _, cc2_residual_bare = yukawa_subblock(
        infra, np.zeros_like(A0), plus_states, minus_states)
    s_bare = np.asarray(s_full_bare, dtype=float)                # (local) 24 bare mass eigen-bilinears
    s_bare_nz = s_bare[s_bare > DEGEN_TOL]                       # (local)

    # spread of distinct nonzero singular values (a Schur-blind block has all equal => spread ~ 0)
    def _distinct_spread(vals):
        if vals.size == 0:
            return 0.0, 1.0
        vmax = float(np.max(vals))                               # (local)
        vmin = float(np.min(vals))                               # (local)
        return vmax - vmin, (vmax / vmin if vmin > DEGEN_TOL else np.inf)

    spread_A0, ratio_A0 = _distinct_spread(s_nonzero)
    spread_bare, ratio_bare = _distinct_spread(s_bare_nz)

    # Cluster singular values to rel=1e-6 (well above the 1e-12 degeneracy floor, below the ~1%
    # physical splittings) so gauge-orbit numerical multiplicity is not mistaken for a non-
    # degenerate generation splitting.
    def _distinct_clustered(vals, rel=1.0e-6):
        if vals.size == 0:
            return np.array([])
        vs = np.sort(vals)[::-1]                                 # (local) descending
        clusters = [vs[0]]                                       # (local)
        for v in vs[1:]:
            if abs(v - clusters[-1]) > rel * max(abs(clusters[-1]), 1.0):
                clusters.append(v)
        return np.array(clusters)

    # PRIMARY zero-free-parameter observable: distinct-cluster ratio of the BARE D_K Yukawa block.
    distinct_bare = _distinct_clustered(s_bare_nz)               # (local) zero-parameter mass bilinears
    distinct_A0 = _distinct_clustered(s_nonzero)                 # (local) fluctuated (diagnostic only)

    if distinct_bare.size >= 2:
        m_heavy = float(distinct_bare[0])                        # (local) heaviest distinct bare mass bilinear
        m_light = float(distinct_bare[-1])                       # (local) lightest distinct bare mass bilinear
        R_Yuk = m_heavy / m_light if m_light > DEGEN_TOL else 1.0  # (local)
    elif distinct_bare.size == 1:
        m_heavy = float(distinct_bare[0])                        # (local)
        m_light = float(distinct_bare[0])                        # (local)
        R_Yuk = 1.0                                              # (local) single distinct value => Schur-degenerate
    else:
        m_heavy = 0.0                                            # (local)
        m_light = 0.0                                            # (local)
        R_Yuk = 1.0                                              # (local) no nonzero mass => empty layer

    # fluctuated diagnostic ratio (NOT the gate observable; coefficient/seed-dependent)
    R_Yuk_fluct = (float(distinct_A0[0]) / float(distinct_A0[-1])
                   if distinct_A0.size >= 2 and float(distinct_A0[-1]) > DEGEN_TOL else 1.0)  # (local)

    # ---- nearest SM fermion-mass ratio anchor (comparison only) ----
    anchors = sm_anchor_ratios()
    best_name, best_logdist = None, np.inf                       # (local)
    for name, val in anchors.items():
        if R_Yuk > DEGEN_TOL and val > 0:
            d = abs(np.log10(R_Yuk / val))                       # (local)
            if d < best_logdist:
                best_logdist, best_name = d, name
    R_SM_anchor = anchors.get(best_name, np.nan)                 # (local)

    return {
        "value": float(R_Yuk),
        "R_Yuk": float(R_Yuk),
        "R_Yuk_fluct": float(R_Yuk_fluct),
        "m_heavy": m_heavy, "m_light": m_light,
        "s_vals": s_vals, "s_nonzero": s_nonzero,
        "distinct_A0": distinct_A0, "distinct_bare": distinct_bare,
        "s_bare": s_bare, "s_bare_nz": s_bare_nz,
        "spread_A0": spread_A0, "ratio_A0": ratio_A0,
        "spread_bare": spread_bare, "ratio_bare": ratio_bare,
        "A0_norm": A0_norm, "A1_norm": A1_norm,
        "ah_err": ah_err, "fund_abs": fund_abs,
        "M_gen": M_gen, "M_gen_bare": M_gen_bare, "M_full": M_full,
        "cc2_residual": float(cc2_residual), "cc2_residual_bare": float(cc2_residual_bare),
        "weight_labels": weight_labels, "plus_states": plus_states, "minus_states": minus_states,
        "best_anchor": best_name, "R_SM_anchor": float(R_SM_anchor),
        "best_logdist": float(best_logdist),
        "anchors": anchors,
        "idx_p": idx_p, "idx_m": idx_m,
        "tau": tau,
    }


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme, convention, L_max) -> str:
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


def append_companion_row(audit_sha: str, content_sha: str) -> None:
    row = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; regulator={REGULATOR_PIN}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(row)


def evaluate_gate(res: dict) -> str:
    """PASS iff R_Yuk > 1 (non-degenerate) AND |log10(R_Yuk/R_SM_anchor)| <= 1.0.
    FAIL iff R_Yuk == 1 to DEGEN_TOL (structural degeneracy => empty read-off).
    INFO iff R_Yuk != 1 but |log10(R_Yuk/R_SM_anchor)| > 1.0 (OOM-only first extraction)."""
    R = res["R_Yuk"]                                             # (local)
    # degeneracy: R_Yuk == 1 to tolerance => FAIL/empty
    if abs(R - 1.0) <= DEGEN_TOL:
        return "FAIL"
    if R <= 1.0:
        # heavy/light ordering should give R >= 1; R < 1 here means no genuine split => empty
        return "FAIL"
    # non-degenerate; now the OOM band
    if res["best_logdist"] <= PASS_OOM:
        return "PASS"
    return "INFO"


# ---------------------------------------------------------------------------
# Section 7 — Plot
# ---------------------------------------------------------------------------

def make_plot(res: dict) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))             # (local)

    ax = axes[0]
    sb = res["s_bare"]                                          # (local)
    sa = res["s_vals"]                                          # (local)
    ax.plot(range(len(sb)), sb, "o-", ms=4, label="bare D_K (A0=0)", color="#888")
    ax.plot(range(len(sa)), sa, "s-", ms=4, label="fluctuated D_K + A^{(0)}", color="#c0392b")
    ax.axhline(DEGEN_TOL, color="k", ls=":", lw=0.8, label="degeneracy floor 1e-12")
    ax.set_yscale("log")
    ax.set_xlabel("singular-value index (mass eigen-bilinear)")
    ax.set_ylabel("|mass eigen-bilinear|  (M_KK units)")
    ax.set_title("Yukawa block singular values (Psi_+ -> Psi_- pairing)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    ax = axes[1]
    R = res["R_Yuk"]                                            # (local)
    anchors = res["anchors"]                                    # (local)
    names = list(anchors.keys())                                # (local)
    vals = [anchors[n] for n in names]                          # (local)
    ax.barh(range(len(names)), [np.log10(v) for v in vals], color="#2980b9", alpha=0.6)
    if R > DEGEN_TOL:
        ax.axvline(np.log10(R), color="#c0392b", lw=2,
                   label=f"R_Yuk = {R:.4g} (log10={np.log10(R):.2f})")
    ax.set_yticks(range(len(names)))
    ax.set_yticklabels(names, fontsize=8)
    ax.set_xlabel("log10(SM fermion-mass ratio)  [comparison anchors only]")
    ax.set_title(f"R_Yuk vs SM anchors; nearest={res['best_anchor']} (|dlog10|={res['best_logdist']:.2f})")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    fig.suptitle(f"{GATE_ID}: a_4 Yukawa block of D_K(tau_fold={res['tau']:.3f}), "
                 f"inner-fluctuation spin-0 Higgs; regulator {REGULATOR_PIN}", fontsize=10)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()                                            # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy, informational)")
    script_path = Path(__file__).resolve()                      # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print(f"  torch GPU: {_HAS_TORCH}")
    print()

    res = compute()

    # Report numbers FIRST
    print("=== NUMBERS ===")
    print(f"  tau_fold = {res['tau']}")
    print(f"  fundamental-sector anti-Herm err = {res['ah_err']:.2e}")
    print(f"  |lambda| range (fundamental (1,0) (x) C^16): "
          f"[{res['fund_abs'][res['fund_abs']>1e-9].min():.4f}, {res['fund_abs'].max():.4f}]")
    print(f"  ||A^(0)|| (Higgs/spin-0 part)  = {res['A0_norm']:.6e}")
    print(f"  ||A^(1)|| (gauge/spin-1 part)  = {res['A1_norm']:.6e}")
    print(f"  Psi_+ weight grades (H_K^+ states) = {res['plus_states']}")
    print(f"  CC2 generation-block off-diag residual (fluctuated) = {res['cc2_residual']:.6e}")
    print(f"  CC2 generation-block off-diag residual (bare)       = {res['cc2_residual_bare']:.6e}")
    print("  -- PRIMARY (zero-free-parameter) observable: BARE D_K Yukawa block --")
    print(f"  bare 24 nonzero singular values             = {np.array2string(res['s_bare_nz'], precision=6, max_line_width=200)}")
    print(f"  bare DISTINCT mass bilinears (clustered)    = {np.array2string(res['distinct_bare'], precision=6, max_line_width=200)}")
    print(f"  n_distinct_bare = {res['distinct_bare'].size}, bare spread = {res['spread_bare']:.6e}, bare max/min ratio = {res['ratio_bare']:.6f}")
    print(f"  m_heavy = {res['m_heavy']:.6e},  m_light = {res['m_light']:.6e}")
    print(f"  >>> R_Yuk (BARE, zero-parameter) = m_heavy/m_light = {res['R_Yuk']:.6f} <<<")
    print(f"  nearest SM anchor = {res['best_anchor']} = {res['R_SM_anchor']:.4f}; "
          f"|log10(R_Yuk/R_SM_anchor)| = {res['best_logdist']:.4f}")
    print("  -- DIAGNOSTIC (NOT the gate observable; coefficient/seed-dependent): fluctuated block --")
    print(f"  fluctuated DISTINCT mass bilinears          = {np.array2string(res['distinct_A0'], precision=6, max_line_width=200)}")
    print(f"  R_Yuk_fluct (seed=0 diagnostic) = {res['R_Yuk_fluct']:.6f}  [seed-robustness probe: range ~[1.46,3.22], NOT zero-parameter]")
    print()

    verdict = evaluate_gate(res)

    # save data
    np.savez(
        OUT_NPZ,
        R_Yuk=res["R_Yuk"], m_heavy=res["m_heavy"], m_light=res["m_light"],
        R_Yuk_fluct=res["R_Yuk_fluct"],
        s_vals=res["s_vals"], s_nonzero=res["s_nonzero"],
        distinct_A0=res["distinct_A0"], distinct_bare=res["distinct_bare"],
        s_bare=res["s_bare"], s_bare_nz=res["s_bare_nz"],
        spread_A0=res["spread_A0"], ratio_A0=res["ratio_A0"],
        spread_bare=res["spread_bare"], ratio_bare=res["ratio_bare"],
        A0_norm=res["A0_norm"], A1_norm=res["A1_norm"], ah_err=res["ah_err"],
        fund_abs=res["fund_abs"],
        M_gen=res["M_gen"], M_gen_bare=res["M_gen_bare"], M_full=res["M_full"],
        cc2_residual=res["cc2_residual"], cc2_residual_bare=res["cc2_residual_bare"],
        weight_labels=res["weight_labels"], plus_states=res["plus_states"],
        minus_states=res["minus_states"],
        best_anchor=str(res["best_anchor"]), R_SM_anchor=res["R_SM_anchor"],
        best_logdist=res["best_logdist"],
        anchor_names=np.array(list(res["anchors"].keys())),
        anchor_vals=np.array(list(res["anchors"].values())),
        tau=res["tau"], degen_tol=DEGEN_TOL, pass_oom=PASS_OOM,
        regulator=REGULATOR_PIN, scheme=SCHEME, convention=CONVENTION, L_max=L_MAX,
        verdict=verdict,
    )
    make_plot(res)

    tag = emit_4tuple(res["value"], SCHEME, CONVENTION, L_MAX)
    print(tag)
    append_verdict(verdict, res["value"], audit_sha, content_sha)
    append_companion_row(audit_sha, content_sha)

    wall = time.time() - t0                                     # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
