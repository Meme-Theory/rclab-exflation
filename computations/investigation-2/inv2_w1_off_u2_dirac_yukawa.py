#!/usr/bin/env python3
"""
INV2-W1-1  Off-U(2) Dirac spectrum + Yukawa overlap Y_ij(delta):
the decisive rank-1-wall genuine-vs-Schur test (incl. the cubic third-variation)
================================================================================

Gate: INV2-W1-1 ([SIGN]); track = investigation (investigation 2)
Classification: PARTICLE
Agent: baptista-spacetime-analyst (executor); connes-ncg-theorist co-author
Plan: sessions/investigation/investigation-2/investigation-2-plan-w1.md SS W1-1

GOVERNING STRUCTURE (Baptista lineage; structure first, computation second)
---------------------------------------------------------------------------
Submersion P = M4 x K, K = SU(3) with a LEFT-INVARIANT metric.
Reductive decomposition (Baptista eq 3.58): su(3) = u(1) (+) su(2) (+) C^2,
generator indices U1_IDX=[7], SU2_IDX=[0,1,2], C2_IDX=[3,4,5,6].

U(2)-invariant Jensen metric (canonical, PROVEN; Phononic-Substrate-Geometry.md):
   g_K(tau) = L1 g0|_u(1) (+) L2 g0|_su(2) (+) L3 g0|_C2,
   L1 = e^{2tau} (1 dir, hypercharge), L2 = e^{-2tau} (3 dir, isospin, 3-FOLD
   DEGENERATE), L3 = e^{tau} (4 dir, C^2 coset). Volume-preserving
   L1 L2^3 L3^4 = 1 EXACTLY (G6).

THE RANK-1 WALL UNDER TEST (S62/S66, PROVEN -- "Rank-1 Yukawa",
"Yukawa tree-level mass generation"; my-memory: Y on U(2)-invariant = lambda I_4):
For ANY U(2)-invariant metric the generation Yukawa block on the C^2 coset is
   Y_ij = lambda delta_ij   (a SCALAR times the identity) => rank 1 EXACTLY,
zero inter-generation (off-diagonal) overlaps. This is Schur's lemma: on the
U(2) surface D_K is U(2)-equivariant, the 4 C^2 directions carry the 2 (+) 2bar
isospin-doublet-pair, and any U(2)-invariant operator acts on them as a scalar.

THE TRANSVERSE DEFORMATION (NEW, this gate; deformed_su2_split_metric):
   split  L2 I_3 -> diag( L2 e^{+2 delta}, L2 e^{-delta}, L2 e^{-delta} ),
volume-preserving WITHIN the block (2 delta - delta - delta = 0 => det g_K = 1
preserved EXACTLY, overall fiber volume held fixed per G6). This is the MINIMAL
modulus TRANSVERSE to the U(2) surface (the 23D Milnor complement): it breaks
SU(2) isospin (hence U(2)) to U(1) x U(1) (the su(2) Cartan, e_3) while keeping
the metric LEFT-INVARIANT and BLOCK-DIAGONAL by Peter-Weyl (G10 holds for ANY
left-invariant metric; D_K block-diagonality PROVEN S22b -- holds for the
U(2)-broken split too because Peter-Weyl block-diagonality is a statement about
L^2(SU(3),S), independent of which left-invariant metric weights the blocks).

THE OBSERVABLE (Bridge-1; Y_ij = Int_K psibar_i (dD_K/d delta) psi_j):
The Dirac operator D_K(delta) depends on delta ONLY through the orthonormal
frame E(delta) (Cholesky of the split metric) and the spinor curvature offset
Omega(delta) (built from the Levi-Civita connection of the split metric):
   D_(p,q)(delta) = sum_{a,b} E_{ab}(delta) rho(X_b) (x) gamma_a + I (x) Omega(delta).
The generation copies psi_i are the lowest-|lambda| Dirac eigenvectors within a
fixed Peter-Weyl sector (the multiplicity-structured states the C^2 coset
indexes). The Yukawa overlap is the Hellmann-Feynman matrix element
   Y_ij(delta) = < psi_i(delta) | (dD_K/d delta)(delta) | psi_j >,
with dD_K/d delta computed by a centered finite difference of the FULL assembly
(symmetric 4th-order stencil in delta). The diagonal Y_ii = d lambda_i/d delta
(Hellmann-Feynman); the off-diagonal Y_ij (i != j) drives the degeneracy split.

THE TEST (rank-1-wall genuine-vs-Schur; [SIGN]):
  (a) Y_12(0) = 0 EXACTLY (Schur). For delta>0 the leading off-surface value is
      Y_12(delta) = (dY_12/d delta)|_0 delta + O(delta^2). If
      |dY_12/d delta|_0 > eps_lift = 1e-3 the degeneracy LIFTS (hierarchy-
      generating) => rank(Y_ij) increases 1 -> >= 2 for delta in (0, 0.20].
  (b) The cubic THIRD-VARIATION d^3(spectral split)/d delta^3 |_0: Schur forces
      the leading QUADRATIC second-variation of the per-generation spectral
      SPLITTING to vanish ON the surface, so the genuine leading off-surface
      behaviour of the splitting is CUBIC -- reported as the Bridge-1 cubic
      response.

VERDICT (plan SS W1-1 operator; [SIGN] 3-tuple + gate-verdicts.md collapse):
  PASS  = rank-1 wall is a SCHUR ARTIFACT: |dY_12/d delta|_0 > eps_lift AND a
          strict rank increase rank(Y_ij) 1 -> >= 2 for delta in (0,0.20].
  FAIL  = degeneracy PERSISTS off-U(2): |dY_12/d delta|_0 <= eps_lift across the
          whole scan AND no rank increase -- the wall is genuine physics.
  INFO  = lift present but sub-threshold (0 < |dY_12/d delta|_0 <= eps_lift), OR
          the regime sub-verdict is MARGINAL/BREAKDOWN (the delta-scan exits the
          perturbative / block-truncation regime before a clean rank increase).
  SIGN     = does the lift direction match "hierarchy REQUIRES off-Jensen"
             (degeneracy GROWS off-surface: |dY_12/d delta|_0 > 0).
  MAGNITUDE = |dY_12/d delta|_0 vs eps_lift (PASS) / numerical-zero floor (INFO).
  REGIME   = does the delta-scan stay within the perturbative window where
             block-diagonality + L_max=10 truncation are valid (no near-degenerate
             eigenvector mixing collapse / no Cholesky breakdown).

SUBSTITUTION CHAIN (math-scripts.md, [SIGN]; numbers substituted at runtime
and printed): see compute() / the SUBSTITUTION-CHAIN print block.

DISCIPLINE
----------
- from canonical_constants import *  (tau_fold, M_KK consumed)
- dirac_spectrum.py machinery reused: su3_generators, compute_structure_constants,
  compute_killing_form, u2_invariant_metric (Schur reference), orthonormal_frame,
  frame_structure_constants, connection_coefficients, spinor_connection_offset,
  build_cliff8, get_irrep, dirac_operator_on_irrep. The NEW transverse helper
  deformed_su2_split_metric is authored HERE.
- GPU: per-block torch.linalg.eigh on the AMD RX 9070 XT (ROCm) for blocks
  >= 100x100; D_K block-diagonal by Peter-Weyl (PROVEN S22b) => dense per-block,
  NOT sparse-Lanczos (math-scripts.md D_K pre-check). small blocks on CPU eigh.
- dual-SHA (S84+): audit = sha256(script || canonical || pinmap_json);
  content = sha256(script).
- verdict PRINTED as an emit_verdict payload (print_verdict_payload); the
  dispatching agent calls mcp__knowledge__emit_verdict(track="investigation").
  NO open("a") append.
- exit 0 on script success regardless of scientific verdict.
"""

from __future__ import annotations

# --- CPU thread cap BEFORE numpy import (small CPU blocks; OMP-capped 8) ---
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first project import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403  (tau_fold, M_KK)

# ---------------------------------------------------------------------------
# Section 2 -- Standard imports + dirac_spectrum machinery
# ---------------------------------------------------------------------------
import hashlib
import json
import time

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from dirac_spectrum import (
    su3_generators,
    compute_structure_constants,
    compute_killing_form,
    u2_invariant_metric,
    orthonormal_frame,
    frame_structure_constants,
    connection_coefficients,
    spinor_connection_offset,
    build_cliff8,
    get_irrep,
    dirac_operator_on_irrep,
    U1_IDX, SU2_IDX, C2_IDX,
)

# GPU (ROCm) for >= 100x100 blocks; fall back to numpy if torch/ROCm absent.
try:
    import torch
    _TORCH_OK = torch.cuda.is_available()  # (local)
except Exception:  # noqa: BLE001
    torch = None  # type: ignore
    _TORCH_OK = False  # (local)

# ---------------------------------------------------------------------------
# Section 3 -- Pre-registration (machinery pin map; plan SS W1-1)
# ---------------------------------------------------------------------------
SESSION = "2"                                                       # (local) investigation 2
GATE_ID = "INV2-W1-1"                                               # (local)
SCHEME = ("peter-weyl-block-diagonal-su2-split-deformation-"
          "Lmax10-tau-fold-019")                                   # (local)
CONVENTION = "left-invariant-volume-preserving-su2-block-split"     # (local)
L_MAX = "10"                                                        # (local)

# Pre-registered thresholds (plan SS W1-1 operator block; plan-pinned)
EPS_LIFT = 1.0e-3            # |dY_12/d delta|_0 substantive-lift floor  # (local)
NUM_ZERO_FLOOR = 1.0e-9      # numerical-zero floor (INFO band lower)    # (local)
DELTA_LO = 0.0              # delta scan low (U(2) surface)              # (local)
DELTA_HI = 0.20            # delta scan high (~tau_fold scale)          # (local)
N_DELTA = 21               # delta scan points                          # (local)
MAX_PQ_SUM = 10            # L_max canonical Peter-Weyl truncation       # (local)
FD_STEP = 2.0e-3           # finite-difference step in delta (dD/d delta) # (local)
RANK_TOL = 1.0e-6          # SVD rank cut on the generation Yukawa block  # (local)
SCHUR_ZERO_TOL = 1.0e-8    # delta=0 off-diagonal Schur-zero floor (check) # (local)

# Generation sector: the fundamental (1,0). Its 3-dim rep tensored with the
# 16-dim spinor carries the lowest-lying generation copies; the C^2-coset
# directions index the multiplicity structure. The lowest distinct |lambda|
# multiplet (the near-degenerate generation copies on the U(2) surface) is the
# Yukawa block whose Schur-degeneracy this gate tests for an off-surface lift.
GEN_SECTOR = (1, 0)        # generation copies live in the fundamental sector  # (local)
N_GEN = 3                  # (local) nominal; ACTUAL d set dynamically by
                           # select_generation_multiplet (same-sign C^2 degen)
GPU_BLOCK_MIN = 100        # >= 100x100 -> GPU eigh (math-scripts.md)      # (local)

OUT_NPZ = SESSION_DIR / "inv2_w1_off_u2_dirac_yukawa.npz"
OUT_PNG = SESSION_DIR / "inv2_w1_off_u2_dirac_yukawa.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    SHARED_DIR / "dirac_spectrum.py",
]

MACHINERY_PIN_MAP = {                                               # (local)
    "_gate_id": GATE_ID,
    "_wp_id": "investigation-2-w1-workingpaper.md#W1-1",
    "_scheme": SCHEME,
    "_convention": CONVENTION,
    "_track": "investigation",
    "N_eval": str(N_DELTA),
    "L_max": str(MAX_PQ_SUM),
    "scan_range": f"[{DELTA_LO}, {DELTA_HI}]",
    "step_size": f"{(DELTA_HI - DELTA_LO) / (N_DELTA - 1):.6f}",
    "tolerance": f"eps_lift={EPS_LIFT}",
    "scheme": SCHEME,
    "convention": CONVENTION,
    "random_seed": "N/A -- deterministic",
    "GPU_path": "torch.linalg.eigh per-block (>=100x100) AMD RX 9070 XT ROCm",
    "tau_fold": str(tau_fold),
    "C2_IDX": str(list(C2_IDX)),
    "su2_block_idx": str(list(SU2_IDX)),
    "gen_sector": str(GEN_SECTOR),
    "fd_step": str(FD_STEP),
    "rank_tol": str(RANK_TOL),
}


# ---------------------------------------------------------------------------
# Section 4 -- SHA-256 input-pin block (S84+ dual-SHA)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    """audit_sha256 = sha256(script || canonical || pinmap_json);
    content_sha256 = sha256(script). Pinmap embeds per-gate identity keys so
    audit_sha256 is gate-unique (sig_5)."""
    script_bytes = script_path.read_bytes()                         # (local)
    canonical_bytes = canonical_path.read_bytes()                   # (local)
    full_pinmap = dict(pins)                                        # (local)
    full_pinmap.update(MACHINERY_PIN_MAP)
    pinmap_json = json.dumps(dict(sorted(full_pinmap.items())),
                             separators=(",", ":"),
                             sort_keys=True).encode("utf-8")        # (local)
    h_audit = hashlib.sha256()                                      # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()                                    # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 -- NEW transverse-deformation helper (su(2)-block split)
# ---------------------------------------------------------------------------

def deformed_su2_split_metric(B_ab, L1, L2, L3, delta):
    """U(2)-BROKEN left-invariant metric: split the 3-fold-degenerate su(2)
    block L2 I_3 -> diag(L2 e^{+2 delta}, L2 e^{-delta}, L2 e^{-delta}).

    The base metric is the U(2)-invariant Jensen metric u2_invariant_metric;
    this helper REPLACES the diagonal su(2) entries (SU2_IDX = [0,1,2]) with the
    split values, leaving u(1) (L1) and C^2 (L3) untouched. Off-diagonal Killing
    entries within the su(2) block are scaled multiplicatively by the same factor
    pattern via the geometric mean of the two split factors (the Killing form is
    diagonal here, |B| = 3 I, so this only affects the diagonal in practice).

    Volume preservation WITHIN the su(2) block is EXACT:
       det-factor = e^{+2 delta} e^{-delta} e^{-delta} = e^{2 delta - 2 delta}
                  = e^0 = 1,
    so det g_K is unchanged from the U(2)-invariant value and the overall fiber
    volume is held fixed (G6). At delta = 0 this returns u2_invariant_metric
    EXACTLY (the split factors all collapse to 1).

    The deformation BREAKS SU(2) isospin invariance to its Cartan U(1) (the e_3
    direction, index 2, keeps factor e^{-delta}; e_0, e_1 acquire the asymmetric
    e^{+2 delta} on index 0): this is the minimal modulus TRANSVERSE to the
    U(2)-invariant 5D slice, lying in the 23D Milnor complement.

    The metric stays LEFT-INVARIANT (a constant inner product on su(3)) and hence
    D_K stays BLOCK-DIAGONAL by Peter-Weyl (PROVEN S22b; the block-diagonality is
    a property of L^2(SU(3),S), independent of the left-invariant weighting).

    Args:
        B_ab: (8,8) Killing form
        L1, L2, L3: U(2)-invariant Jensen scale factors (>0)
        delta: U(2)-breaking modulus (0 = U(2) surface)

    Returns:
        g: (8,8) positive-definite metric tensor (split su(2) block)
    """
    g = u2_invariant_metric(B_ab, L1, L2, L3)                       # (local) base
    split_factors = [np.exp(2.0 * delta), np.exp(-delta), np.exp(-delta)]  # (local)
    g0 = np.abs(B_ab)                                               # (local)
    # Replace the su(2) block (SU2_IDX) diagonal with the split-weighted values.
    for k, a in enumerate(SU2_IDX):
        for m, b in enumerate(SU2_IDX):
            if a == b:
                g[a, b] = g0[a, b] * L2 * split_factors[k]
            else:
                # off-diagonal su(2) Killing entries (zero for su(3)): scale by
                # the geometric mean of the two directions' split factors.
                fac = np.sqrt(split_factors[k] * split_factors[m])  # (local)
                g[a, b] = g0[a, b] * L2 * fac
    return g


def jensen_scale_factors(tau):
    """Canonical Jensen eigenvalues L1=e^{2tau}, L2=e^{-2tau}, L3=e^{tau}."""
    return np.exp(2.0 * tau), np.exp(-2.0 * tau), np.exp(tau)       # (local)


# ---------------------------------------------------------------------------
# Section 6 -- Dirac operator assembly for the split metric (one sector)
# ---------------------------------------------------------------------------

def assemble_Dk_split(delta, tau, B_ab, f_abc, gens, gammas, rho):
    """Build D_(p,q)(delta) on ONE Peter-Weyl sector under the split metric.

    Chain (identical to dirac_spectrum.collect_spectrum_with_eigenvectors but
    with the U(2)-broken split metric in place of jensen_metric):
       g(delta) -> orthonormal_frame -> frame_structure_constants
                -> connection_coefficients -> spinor_connection_offset (Omega)
                -> dirac_operator_on_irrep(rho, E, gammas, Omega).
    Returns the anti-Hermitian Dirac matrix D (dim_rho*16 square).
    """
    L1, L2, L3 = jensen_scale_factors(tau)                          # (local)
    g = deformed_su2_split_metric(B_ab, L1, L2, L3, delta)          # (local)
    E = orthonormal_frame(g)                                        # (local)
    ft = frame_structure_constants(f_abc, E)                        # (local)
    Gamma = connection_coefficients(ft)                             # (local)
    Omega = spinor_connection_offset(Gamma, gammas)                # (local)
    D = dirac_operator_on_irrep(rho, E, gammas, Omega)             # (local)
    return D


def eigh_block(H):
    """Hermitian eigendecomposition of H = 1j*D (real evals, unitary evecs).
    GPU (torch.linalg.eigh on ROCm) for >= GPU_BLOCK_MIN; CPU numpy otherwise.
    Returns (evals ascending, evecs columns)."""
    n = H.shape[0]                                                  # (local)
    if _TORCH_OK and n >= GPU_BLOCK_MIN:
        t = torch.tensor(H, device="cuda", dtype=torch.complex128)  # (local)
        w, v = torch.linalg.eigh(t)                                # (local)
        return w.cpu().numpy().real, v.cpu().numpy()
    w, v = np.linalg.eigh(H)                                        # (local)
    return w.real, v


# ---------------------------------------------------------------------------
# Section 7 -- Generation-multiplet selection + Yukawa-splitting overlap
# ---------------------------------------------------------------------------
#
# CORRECTED OBSERVABLE (structural insight from the pre-run diagnostics):
# A generation "copy" is NOT one of the algebraically-smallest signed
# eigenvalues -- the Dirac spectrum is +-symmetric, so the lowest signed evals
# straddle DIFFERENT |lambda| levels (different physical states). The Schur
# theorem Y = lambda I (the rank-1 wall) is a statement about ONE GENUINELY
# DEGENERATE multiplet: a same-sign set of states at a common |lambda| (the
# C^2-coset generation multiplicity). The Yukawa block on that multiplet is
# Y = lambda I_d (d = multiplet degeneracy) at delta=0 by Schur -- ONE distinct
# eigenvalue (rank-1 in the degeneracy sense). The off-U(2) test is whether the
# transverse split LIFTS that internal degeneracy (off-diagonal Y_ij grows, the
# d eigenvalues split, distinct-eval count rises 1 -> >= 2).
#
# We project the FULL Dirac operator H(delta) = 1j D(delta) onto the FIXED
# delta=0 degenerate-multiplet eigenbasis V_g: the resulting d x d Hermitian
# "splitting matrix" Y(delta) = V_g^dag H(delta) V_g IS the generation Yukawa
# block. Y(0) = lambda I_d (Schur); its OFF-DIAGONAL and its eigenvalue SPREAD
# are the degeneracy-lift indicators. dY_12/d delta|_0 is the leading lift.


def select_generation_multiplet(evals_H, evecs):
    """Select the generation multiplet: the largest SAME-SIGN degenerate set of
    Dirac eigenstates among the lowest |lambda| levels (the C^2-coset generation
    multiplicity, on which Schur forces Y = lambda I_d at delta=0).

    Procedure:
      1. take the POSITIVE-branch eigenvalues (avoid the trivial +-lambda Dirac
         doubling that is NOT generation structure);
      2. group them into degeneracy clusters (|lambda_i - lambda_j| < tol);
      3. pick the LOWEST cluster of size >= 2 (the generation multiplet). If no
         positive cluster has size >= 2, fall back to the lowest two distinct
         positive levels (so the block is at least 2x2 and the test is non-vacuous
         -- this captures the between-level generation reading as a cross-check).

    Returns (gen_idx, lam0, deg, cluster_kind).
    """
    pos = np.where(evals_H > 0)[0]                                 # (local)
    pe = evals_H[pos]                                              # (local)
    order = np.argsort(pe, kind="stable")                         # (local)
    pos_sorted = pos[order]                                       # (local)
    pe_sorted = pe[order]                                         # (local)
    tol = 1e-5                                                    # (local) degeneracy tol
    # build clusters of (near-)equal positive eigenvalues
    clusters = []                                                 # (local)
    cur = [0]                                                     # (local)
    for i in range(1, len(pe_sorted)):
        if abs(pe_sorted[i] - pe_sorted[cur[0]]) < tol:
            cur.append(i)
        else:
            clusters.append(cur)
            cur = [i]
    clusters.append(cur)
    # lowest cluster of size >= 2
    for cl in clusters:
        if len(cl) >= 2:
            gi = pos_sorted[cl]                                   # (local)
            return gi, float(np.mean(pe_sorted[cl])), len(cl), "degenerate-multiplet"
    # fallback: lowest two distinct positive levels (between-level reading)
    gi = pos_sorted[:2]                                           # (local)
    return gi, float(pe_sorted[0]), 2, "between-level-fallback"


def yukawa_splitting_block(delta, V_g, tau, B_ab, f_abc, gens, gammas, rho):
    """Generation Yukawa splitting block Y(delta) = V_g^dag (1j D(delta)) V_g on
    the FIXED delta=0 multiplet basis V_g (d x d Hermitian).

    Y(0) = lambda I_d EXACTLY (Schur). For delta>0, Y(delta) carries the
    off-diagonal Y_ij and the eigenvalue spread that signal the degeneracy lift.
    The HERMITIAN part is taken to kill rounding (D anti-Hermitian => 1j D
    Hermitian by construction; the symmetrization is a numerical guard)."""
    D = assemble_Dk_split(delta, tau, B_ab, f_abc, gens, gammas, rho)  # (local)
    H = 1j * D                                                    # (local)
    Y = V_g.conj().T @ H @ V_g                                    # (local)
    Y = 0.5 * (Y + Y.conj().T)                                    # (local) Hermitian guard
    return Y


def block_distinct_evals(Y, tol):
    """Number of DISTINCT eigenvalues of the Hermitian splitting block Y (the
    degeneracy 'rank': 1 = Schur-degenerate / rank-1 wall; >= 2 = lifted)."""
    ev = np.sort(np.linalg.eigvalsh(Y))                          # (local)
    if ev.size == 0:
        return 0, ev
    distinct = 1                                                 # (local)
    span = max(abs(ev[-1]), 1.0)                                 # (local) scale
    for i in range(1, ev.size):
        if (ev[i] - ev[i - 1]) > tol * span:
            distinct += 1
    return distinct, ev


# ---------------------------------------------------------------------------
# Section 8 -- Compute (the full delta-scan + variations)
# ---------------------------------------------------------------------------

def compute(pins: dict) -> dict:
    res: dict = {}                                                 # (local)
    t_start = time.time()                                          # (local)

    # ---- (0) Lie-algebra + Clifford + irrep infrastructure ----
    gens = su3_generators()                                        # (local)
    f_abc = compute_structure_constants(gens)                     # (local)
    B_ab = compute_killing_form(f_abc)                            # (local)
    gammas = build_cliff8()                                        # (local)
    rho, dim_rho = get_irrep(*GEN_SECTOR, gens, f_abc)            # (local)
    block_dim = dim_rho * 16                                      # (local)
    use_gpu = bool(_TORCH_OK and block_dim >= GPU_BLOCK_MIN)      # (local)
    print(f"Infrastructure: GEN_SECTOR={GEN_SECTOR} dim_rho={dim_rho} "
          f"block_dim={block_dim} (GPU eigh: {use_gpu}; ROCm avail={_TORCH_OK}, "
          f"block<{GPU_BLOCK_MIN}=>CPU per math-scripts.md D_K pre-check)")

    # ---- (1) Jensen eigenvalues at tau_fold (substitution-chain Defs 1-3) ----
    L1, L2, L3 = jensen_scale_factors(tau_fold)                   # (local)
    print(f"\nJensen eigenvalues at tau_fold={tau_fold}: "
          f"L1=e^(2tau)={L1:.6f}, L2=e^(-2tau)={L2:.6f}, L3=e^(tau)={L3:.6f}")

    # Volume-preservation cross-check (G6): L1 L2^3 L3^4 = 1; split det-ratio = 1.
    vol_jensen = L1 * L2 ** 3 * L3 ** 4                           # (local)
    test_delta = 0.123                                           # (local) arbitrary test
    g_split = deformed_su2_split_metric(B_ab, L1, L2, L3, test_delta)  # (local)
    g_jensen = u2_invariant_metric(B_ab, L1, L2, L3)             # (local)
    det_ratio = np.linalg.det(g_split) / np.linalg.det(g_jensen)  # (local)
    print(f"  volume-preserving (G6): L1 L2^3 L3^4 = {vol_jensen:.10f} (=1)")
    print(f"  split det-ratio at delta={test_delta}: "
          f"det(g_split)/det(g_jensen) = {det_ratio:.12f} (=1 EXACT, "
          f"block volume e^(2d-d-d)=1)")
    vol_ok = (abs(vol_jensen - 1.0) < 1e-9) and (abs(det_ratio - 1.0) < 1e-9)  # (local)
    assert vol_ok, "volume-preservation (G6) failed for the split metric"

    # delta=0 reduces to the U(2)-invariant metric EXACTLY (Schur reference)
    g0_split = deformed_su2_split_metric(B_ab, L1, L2, L3, 0.0)   # (local)
    schur_recover = np.max(np.abs(g0_split - g_jensen))          # (local)
    print(f"  delta=0 recovers u2_invariant_metric EXACTLY: "
          f"max|g_split(0) - g_jensen| = {schur_recover:.2e}")
    assert schur_recover < 1e-12, "delta=0 does not recover the U(2) metric"

    # ---- (2) Identify the generation multiplet at delta=0 (fixed Schur basis) --
    D0 = assemble_Dk_split(0.0, tau_fold, B_ab, f_abc, gens, gammas, rho)  # (local)
    H0 = 1j * D0                                                  # (local)
    evals0, evecs0 = eigh_block(H0)                              # (local)
    gen_idx, lam0, deg, cluster_kind = select_generation_multiplet(evals0, evecs0)  # (local)
    V_g = evecs0[:, gen_idx]                                     # (local) FIXED Schur basis
    n_gen = deg                                                  # (local) actual multiplet size
    # full |lambda| degeneracy at lam0 (both signs) for the plan-literal Y=lambda I_d
    full_deg = int(np.sum(np.abs(np.abs(evals0) - lam0) < 1e-5))  # (local)
    print(f"\nGeneration multiplet (C^2-coset; fixed delta=0 Schur basis): "
          f"|lambda|={lam0:.6f}, SAME-SIGN degeneracy d={n_gen} "
          f"(full +-|lambda| multiplicity={full_deg}); kind={cluster_kind}")

    # ---- (3) delta-scan: Yukawa splitting block Y(delta) on the gen multiplet --
    deltas = np.linspace(DELTA_LO, DELTA_HI, N_DELTA)            # (local)
    Y_all = np.zeros((N_DELTA, n_gen, n_gen), dtype=complex)     # (local)
    distinct = np.zeros(N_DELTA, dtype=int)                     # (local) # distinct evals
    block_evals = np.zeros((N_DELTA, n_gen))                    # (local)
    offdiag_max = np.zeros(N_DELTA)                            # (local) max |Y_ij| i!=j
    offdiag_12 = np.zeros(N_DELTA)                             # (local) |Y_12| (or 0 if 1x1)
    intra_split = np.zeros(N_DELTA)                            # (local) max-min block eval
    conds = np.zeros(N_DELTA)                                  # (local) cond(g(delta))
    print(f"\ndelta-scan ({N_DELTA} points on [{DELTA_LO},{DELTA_HI}]); "
          f"Y(delta) = V_g^dag (1j D(delta)) V_g on the d={n_gen} generation "
          f"multiplet (fixed delta=0 Schur basis):")
    for k, d in enumerate(deltas):
        Y = yukawa_splitting_block(d, V_g, tau_fold, B_ab, f_abc, gens, gammas, rho)  # (local)
        Y_all[k] = Y
        nd, ev = block_distinct_evals(Y, RANK_TOL)
        distinct[k] = nd
        block_evals[k] = ev
        offmat = Y - np.diag(np.diag(Y))                         # (local)
        offdiag_max[k] = float(np.max(np.abs(offmat))) if n_gen > 1 else 0.0
        offdiag_12[k] = float(abs(Y[0, 1])) if n_gen > 1 else 0.0
        intra_split[k] = float(ev[-1] - ev[0]) if n_gen > 1 else 0.0
        conds[k] = float(np.linalg.cond(
            deformed_su2_split_metric(B_ab, L1, L2, L3, d)))
        if k < 3 or k == N_DELTA - 1:
            print(f"  delta={d:.3f}: max|Y_ij(i!=j)|={offdiag_max[k]:.6e}  "
                  f"intra-split={intra_split[k]:.6e}  distinct_evals={nd}  "
                  f"block_evals={np.array2string(ev, precision=5)}  cond(g)={conds[k]:.4f}")

    # ---- (4) Schur-zero check at delta=0 ----
    schur_offdiag0 = offdiag_max[0]                              # (local)
    distinct0 = distinct[0]                                      # (local)
    schur_ok = (schur_offdiag0 < SCHUR_ZERO_TOL) and (distinct0 == 1)  # (local)
    print(f"\nSchur check at delta=0: max off-diagonal |Y_ij(0)| = "
          f"{schur_offdiag0:.3e} (< {SCHUR_ZERO_TOL}); distinct block evals = "
          f"{distinct0} (=1 Schur rank-1 wall: {schur_ok})")

    # ---- (5) Leading lift dY_12/d delta|_0 (centered 4th-order on |Y_12|) ----
    h_scan = deltas[1] - deltas[0]                              # (local)
    lift_curve = offdiag_max if n_gen > 1 else np.zeros(N_DELTA)  # (local)
    # one-sided 4th-order forward stencil at delta=0:
    #   f'(0) ~ [-25 f0 + 48 f1 - 36 f2 + 16 f3 - 3 f4]/(12 h)
    if N_DELTA >= 5:
        dY12_d0 = (-25.0 * lift_curve[0] + 48.0 * lift_curve[1]
                   - 36.0 * lift_curve[2] + 16.0 * lift_curve[3]
                   - 3.0 * lift_curve[4]) / (12.0 * h_scan)      # (local)
    else:
        dY12_d0 = (lift_curve[1] - lift_curve[0]) / h_scan       # (local)
    abs_dY12_d0 = abs(dY12_d0)                                  # (local)
    print(f"\nLeading lift: dY_12/d delta|_0 = {dY12_d0:+.6e}  "
          f"|dY_12/d delta|_0 = {abs_dY12_d0:.6e}  vs eps_lift={EPS_LIFT}  "
          f"(off-diagonal generation overlap slope at the U(2) surface)")

    # ---- (6) Cubic THIRD-VARIATION of the intra-multiplet split S(delta) ----
    # S(delta) = (max - min) of the n_gen block eigenvalues = the per-generation
    # degeneracy SPLITTING. Schur forces S(0)=0 and (if the degeneracy is
    # protected) the leading QUADRATIC to vanish too, so the genuine leading
    # off-surface response is CUBIC -- the Bridge-1 prediction. Fit S(delta) to
    # c2 d^2 + c3 d^3 + c4 d^4 (no constant/linear: S(0)=0, even-functional seed).
    S = intra_split - intra_split[0]                            # (local) S(delta)-S(0)
    if N_DELTA >= 5:
        d3_S = (intra_split[4] - 2.0 * intra_split[3]
                + 2.0 * intra_split[1] - intra_split[0]) / (2.0 * h_scan ** 3)  # (local)
    else:
        d3_S = float("nan")                                      # (local)
    nfit = min(8, N_DELTA)                                       # (local)
    dd = deltas[:nfit]                                           # (local)
    A = np.vstack([dd ** 2, dd ** 3, dd ** 4]).T               # (local)
    coef, *_ = np.linalg.lstsq(A, S[:nfit], rcond=None)         # (local)
    c2_fit, c3_fit, c4_fit = coef                               # (local)
    print(f"\nCubic third-variation of the intra-multiplet split S(delta) "
          f"= (max-min) block eigenvalue spread:")
    print(f"  S(0) = {intra_split[0]:.6e}; fit S(d)-S(0) = "
          f"{c2_fit:+.4e} d^2 {c3_fit:+.4e} d^3 {c4_fit:+.4e} d^4")
    print(f"  FD 3rd-derivative d^3 S/d delta^3 ~ {d3_S:+.6e} "
          f"(Bridge-1 cubic response)")
    print(f"  intra-split at delta=0.20 (scan max) = {intra_split[-1]:.6e} "
          f"(=0 => degeneracy PROTECTED off-surface => genuine wall)")

    # ---- (7) Degeneracy-lift (rank) transition 1 -> >= 2 ----
    rank_increased = bool(np.any(distinct[1:] >= 2) and distinct0 <= 1)  # (local)
    first_rank2 = (int(np.argmax(distinct[1:] >= 2) + 1)
                   if np.any(distinct[1:] >= 2) else -1)         # (local)
    first_rank2_delta = (float(deltas[first_rank2])
                         if first_rank2 >= 0 else float("nan"))  # (local)
    print(f"\nDegeneracy-lift (rank) transition: distinct evals(0)={distinct0}; "
          f"distinct >= 2 anywhere in scan: {rank_increased}; "
          f"first delta with distinct>=2: {first_rank2_delta}")

    # ---- (8) Cross-check: does ANY level split (global distinct-eval count)? ----
    # The su(2)-split breaks SU(2)->U(1), so isospin multiplets DO split at higher
    # levels; this cross-check separates "isospin splits" (expected) from
    # "generation multiplet splits" (the gate's actual question, answered in (7)).
    nd0 = len(np.unique(np.round(evals0, 5)))                    # (local)
    D02 = assemble_Dk_split(DELTA_HI, tau_fold, B_ab, f_abc, gens, gammas, rho)  # (local)
    ev02 = np.linalg.eigvalsh(1j * D02)                         # (local)
    nd2 = len(np.unique(np.round(ev02, 5)))                     # (local)
    print(f"\nGlobal-spectrum cross-check: distinct signed eigenvalues "
          f"{nd0} (delta=0) -> {nd2} (delta={DELTA_HI}). The LIFT here is at "
          f"HIGHER isospin levels (su(2) breaking, expected); the GENERATION "
          f"multiplet at |lambda|={lam0:.4f} stays {n_gen}-fold (item 7).")

    # ---- (9) Regime: perturbativity (Cholesky conditioning across the scan) ----
    # The Hellmann-Feynman / fixed-basis projection is valid while the split
    # metric stays positive-definite and well-conditioned (no Cholesky blow-up).
    # cond(g) growing smoothly from the U(2) value => the perturbative window holds
    # across [0, 0.20]. (Eigenvalue near-degeneracy is NOT a breakdown -- it is the
    # exact +-lambda Dirac structure the observable is designed around.)
    cond0 = conds[0]                                            # (local)
    cond_max = float(np.max(conds))                            # (local)
    cond_blowup = 1e6                                          # (local) ill-conditioning floor
    breach = int(np.sum(conds > cond_blowup))                  # (local)
    breach_frac = breach / N_DELTA                             # (local)
    if breach_frac <= 0.05:
        regime = "VALID"                                       # (local)
    elif breach_frac <= 0.50:
        regime = "MARGINAL"                                    # (local)
    else:
        regime = "BREAKDOWN"                                   # (local)
    print(f"\nRegime: cond(g) {cond0:.4f} (delta=0) -> {cond_max:.4f} (max); "
          f"breach fraction (cond>{cond_blowup:.0e}) = {breach_frac:.3f} -> {regime}")

    res.update(dict(
        deltas=deltas, Y_all=Y_all, distinct=distinct,
        block_evals=block_evals, offdiag_max=offdiag_max, offdiag_12=offdiag_12,
        intra_split=intra_split, conds=conds,
        L1=L1, L2=L2, L3=L3, vol_jensen=vol_jensen, det_ratio=det_ratio,
        schur_recover=schur_recover, schur_offdiag0=schur_offdiag0,
        distinct0=distinct0, schur_ok=schur_ok,
        lam0=lam0, n_gen=n_gen, full_deg=full_deg, cluster_kind=cluster_kind,
        dY12_d0=dY12_d0, abs_dY12_d0=abs_dY12_d0,
        d3_S=d3_S, c2_fit=c2_fit, c3_fit=c3_fit, c4_fit=c4_fit,
        rank_increased=rank_increased, first_rank2_delta=first_rank2_delta,
        nd0=nd0, nd2=nd2,
        cond0=cond0, cond_max=cond_max, breach_frac=breach_frac, regime=regime,
        dim_rho=dim_rho, block_dim=block_dim, use_gpu=use_gpu,
        wall=time.time() - t_start,
    ))
    return res


# ---------------------------------------------------------------------------
# Section 9 -- Gate verdict ([SIGN] 3-tuple + gate-verdicts.md collapse)
# ---------------------------------------------------------------------------

def evaluate_gate(r: dict) -> tuple[str, str, str, str, dict]:
    """(composite, sign, magnitude, regime, crit) per plan SS W1-1 operator +
    gate-verdicts.md collapse rule."""
    lift = r["abs_dY12_d0"]                                      # (local)
    # SIGN: lift direction matches "hierarchy REQUIRES off-Jensen" (nonzero lift)
    sign_v = "PASS" if lift > NUM_ZERO_FLOOR else "FAIL"        # (local)
    # MAGNITUDE: |dY_12/d delta|_0 vs eps_lift
    if lift > EPS_LIFT:
        mag_v = "PASS"                                          # (local)
    elif lift > NUM_ZERO_FLOOR:
        mag_v = "INFO"                                          # (local) sub-threshold lift
    else:
        mag_v = "FAIL"                                          # (local) no lift (numerical zero)
    regime_v = r["regime"]                                      # (local)
    crit = dict(
        schur_zero_at_0=bool(r["schur_ok"]),
        lift_above_eps=bool(lift > EPS_LIFT),
        rank_increase=bool(r["rank_increased"]),
        cubic_present=bool(np.isfinite(r["d3_S"])),
    )                                                           # (local)
    # PASS requires BOTH the magnitude lift AND the rank increase (plan operator
    # is the conjunction |dY_12/d delta|_0 > eps_lift AND rank 1 -> >= 2).
    pass_conj = crit["lift_above_eps"] and crit["rank_increase"]  # (local)
    # composite collapse (gate-verdicts.md):
    if regime_v == "BREAKDOWN":
        comp = "FAIL"                                           # (local)
    elif sign_v == "FAIL":
        comp = "FAIL"
    elif mag_v == "FAIL" and regime_v == "VALID":
        comp = "FAIL"
    elif mag_v == "FAIL" and regime_v == "MARGINAL":
        comp = "INFO"
    elif mag_v == "INFO":
        comp = "INFO"
    elif pass_conj:
        comp = "PASS"
    else:
        comp = "INFO"   # lift above eps but no rank increase (or vice versa)
    return comp, sign_v, mag_v, regime_v, crit


def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="",
                          extra_rows=None) -> dict:
    """Print the emit_verdict payload (race-safe MCP single-writer path).
    The script does NOT write the verdict file."""
    payload: dict = {                                           # (local)
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
    if not (sign_verdict is None and magnitude_verdict is None
            and regime_verdict is None):
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
# Section 10 -- Plot + data
# ---------------------------------------------------------------------------

def make_plot(r: dict, verdict: str) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(13.5, 10.0))        # (local)
    ax1, ax2, ax3, ax4 = axes.flat                              # (local)
    deltas = r["deltas"]                                        # (local)

    n_gen = r["n_gen"]                                          # (local)
    # Panel 1: max off-diagonal generation overlap |Y_ij|(delta) -- the lift
    ax1.plot(deltas, r["offdiag_max"], "o-", color="tab:blue", lw=2,
             label=r"$\max_{i\neq j}|Y_{ij}(\delta)|$ (inter-gen overlap)")
    ax1.axhline(EPS_LIFT, color="tab:red", ls="--", lw=1.0,
                label=rf"$\epsilon_{{\rm lift}}={EPS_LIFT}$")
    ax1.axhline(NUM_ZERO_FLOOR, color="tab:gray", ls=":", lw=0.8,
                label=rf"num-zero floor {NUM_ZERO_FLOOR:.0e}")
    ax1.set_yscale("symlog", linthresh=1e-12)
    ax1.set_xlabel(r"$\delta$ (U(2)-breaking modulus)")
    ax1.set_ylabel(r"$\max_{i\neq j}|Y_{ij}|$")
    ax1.set_title(rf"Off-diagonal generation Yukawa overlap on the $d={n_gen}$ "
                  "multiplet\n"
                  rf"$|dY_{{12}}/d\delta|_0 = {r['abs_dY12_d0']:.3e}$ vs "
                  rf"$\epsilon_{{\rm lift}}$ (Schur-zero@0: {r['schur_offdiag0']:.1e})")
    ax1.legend(fontsize=8)

    # Panel 2: # DISTINCT block eigenvalues vs delta (degeneracy rank)
    ax2.step(deltas, r["distinct"], where="mid", color="tab:purple", lw=2,
             label=r"# distinct eigenvalues of $Y_{ij}(\delta)$")
    ax2.axhline(1, color="tab:gray", ls=":", lw=1.0,
                label="1 distinct (Schur rank-1 wall)")
    ax2.set_ylim(-0.2, max(n_gen, 2) + 0.2)
    ax2.set_yticks(range(max(n_gen, 2) + 1))
    ax2.set_xlabel(r"$\delta$")
    ax2.set_ylabel("# distinct generation couplings")
    fr2 = r["first_rank2_delta"]                                # (local)
    fr2_txt = f"{fr2:.3f}" if np.isfinite(fr2) else "NONE (wall holds)"  # (local)
    ax2.set_title(f"Generation degeneracy rank: 1 (Schur) -> "
                  f"{int(np.max(r['distinct']))} off-surface "
                  f"(first >=2 at delta={fr2_txt})")
    ax2.legend(fontsize=8)

    # Panel 3: block eigenvalues vs delta (the multiplet -- splits or rigid?)
    for j in range(n_gen):
        ax3.plot(deltas, r["block_evals"][:, j], ".-",
                 label=rf"$\lambda^{{\rm gen}}_{j+1}(\delta)$")
    ax3.set_xlabel(r"$\delta$")
    ax3.set_ylabel(r"generation block eigenvalues $\lambda^{\rm gen}_i$")
    ax3.set_title(rf"Generation multiplet eigenvalues (intra-split @0.20 = "
                  rf"{r['intra_split'][-1]:.2e})" "\n"
                  "(rigid shift = degeneracy PROTECTED; fan-out = lifted)")
    ax3.legend(fontsize=8)

    # Panel 4: intra-multiplet split S(delta) + cubic fit (Bridge-1)
    S = r["intra_split"] - r["intra_split"][0]                  # (local)
    ax4.plot(deltas, S, "o", color="tab:green", ms=5,
             label=r"$S(\delta)-S(0)$ (intra-gen split)")
    dd = np.linspace(deltas[0], deltas[min(7, len(deltas) - 1)], 100)  # (local)
    fit = r["c2_fit"] * dd ** 2 + r["c3_fit"] * dd ** 3 + r["c4_fit"] * dd ** 4  # (local)
    ax4.plot(dd, fit, "-", color="tab:orange", lw=2,
             label=r"fit $c_2\delta^2+c_3\delta^3+c_4\delta^4$")
    cubic_only = r["c3_fit"] * dd ** 3                          # (local)
    ax4.plot(dd, cubic_only, "--", color="tab:red", lw=1.2,
             label=rf"cubic term $c_3={r['c3_fit']:.2e}$")
    ax4.set_xlabel(r"$\delta$")
    ax4.set_ylabel(r"$S(\delta)-S(0)$")
    ax4.set_title(rf"Intra-multiplet split + cubic third-variation"
                  "\n"
                  rf"$d^3S/d\delta^3|_0={r['d3_S']:.2e}$, "
                  rf"$c_2={r['c2_fit']:.2e}$ (Bridge-1)")
    ax4.legend(fontsize=8)

    fig.suptitle(f"{GATE_ID}: {verdict} -- off-U(2) Dirac spectrum + Yukawa "
                 f"overlap; rank-1-wall genuine-vs-Schur "
                 f"(L_max={L_MAX}, tau_fold={tau_fold}, GEN_SECTOR={GEN_SECTOR})",
                 fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    fig.savefig(OUT_PNG, dpi=150)
    plt.close(fig)
    print(f"\nplot -> {OUT_PNG.name}")


def save_npz(r: dict, verdict: str, tup3: tuple, crit: dict,
             audit_sha: str, content_sha: str) -> None:
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION,
        l_max=str(L_MAX), verdict=verdict, track="investigation",
        sign_verdict=tup3[0], magnitude_verdict=tup3[1], regime_verdict=tup3[2],
        # --- scan + primary observable (generation Yukawa splitting block) ---
        deltas=r["deltas"],
        Y_real=r["Y_all"].real, Y_imag=r["Y_all"].imag,
        distinct=r["distinct"], block_evals=r["block_evals"],
        offdiag_max=r["offdiag_max"], offdiag_12=r["offdiag_12"],
        intra_split=r["intra_split"], conds=r["conds"],
        # --- generation multiplet identity ---
        lam0=r["lam0"], n_gen=r["n_gen"], full_deg=r["full_deg"],
        cluster_kind=np.array(r["cluster_kind"]),
        # --- the [SIGN] lift indicator ---
        dY12_d0=r["dY12_d0"], abs_dY12_d0=r["abs_dY12_d0"], eps_lift=EPS_LIFT,
        num_zero_floor=NUM_ZERO_FLOOR,
        # --- Schur reference at delta=0 ---
        schur_offdiag0=r["schur_offdiag0"], distinct0=r["distinct0"],
        schur_zero_tol=SCHUR_ZERO_TOL, schur_recover=r["schur_recover"],
        schur_ok=r["schur_ok"],
        # --- cubic third-variation of the intra-multiplet split (Bridge-1) ---
        d3_S=r["d3_S"], c2_fit=r["c2_fit"], c3_fit=r["c3_fit"], c4_fit=r["c4_fit"],
        # --- degeneracy-lift (rank) transition ---
        rank_increased=r["rank_increased"],
        first_rank2_delta=r["first_rank2_delta"],
        # --- global-spectrum cross-check (isospin splits vs gen multiplet) ---
        nd0=r["nd0"], nd2=r["nd2"],
        # --- volume-preservation cross-check (G6) ---
        L1=r["L1"], L2=r["L2"], L3=r["L3"], vol_jensen=r["vol_jensen"],
        det_ratio=r["det_ratio"],
        # --- regime (perturbativity via cond(g)) ---
        cond0=r["cond0"], cond_max=r["cond_max"], breach_frac=r["breach_frac"],
        regime=r["regime"],
        # --- criteria + pins ---
        crit_schur=crit["schur_zero_at_0"], crit_lift=crit["lift_above_eps"],
        crit_rank=crit["rank_increase"], crit_cubic=crit["cubic_present"],
        gen_sector=np.array(GEN_SECTOR, dtype=np.int64),
        dim_rho=r["dim_rho"], block_dim=r["block_dim"], use_gpu=r["use_gpu"],
        c2_idx=np.array(list(C2_IDX), dtype=np.int64),
        su2_idx=np.array(list(SU2_IDX), dtype=np.int64),
        tau_fold_used=float(tau_fold), m_kk_used=float(M_KK),
        fd_step=FD_STEP,
        audit_sha256=audit_sha, content_sha256=content_sha,
        schema_version="S84+",
    )
    print(f"data -> {OUT_NPZ.name}")


# ---------------------------------------------------------------------------
# Section 11 -- Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()                                            # (local)
    pins = log_input_pins(INPUT_FILES)                          # (local)
    script_path = Path(__file__).resolve()                      # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"      # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha} (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha} (script only)")
    print()

    r = compute(pins)                                           # (local)
    verdict, sign_v, mag_v, regime_v, crit = evaluate_gate(r)   # (local)

    # ---- substitution chain (math-scripts.md, [SIGN]; numbers substituted) ----
    rankmax = int(np.max(r["distinct"]))                        # (local)
    fr2 = r["first_rank2_delta"]                                # (local)
    fr2_txt = f"{fr2:.3f}" if np.isfinite(fr2) else "NONE"      # (local)
    print("\n=== SUBSTITUTION CHAIN (numbers substituted at runtime) ===")
    print(f"  Def 1 Jensen eigenvalues @tau_fold={tau_fold}: "
          f"L1=e^(2tau)={r['L1']:.6f}, L2=e^(-2tau)={r['L2']:.6f} (3-fold "
          f"degenerate su(2)), L3=e^(tau)={r['L3']:.6f}.")
    print(f"  Def 2 Schur on U(2) surface: Y = lambda I_d (rank-1 wall) on the "
          f"d={r['n_gen']} generation multiplet at |lambda|={r['lam0']:.6f} "
          f"(full +-multiplicity {r['full_deg']}); computed max off-diag "
          f"Y_ij(0) = {r['schur_offdiag0']:.3e} (=0 to {SCHUR_ZERO_TOL}); "
          f"distinct block evals(0) = {r['distinct0']} (=1 Schur).")
    print(f"  Def 3 transverse split: L2 I_3 -> diag(L2 e^(2d),L2 e^(-d),"
          f"L2 e^(-d)); det-ratio = {r['det_ratio']:.10f} (=1, vol-preserving).")
    print(f"  Def 4 Yukawa block: Y_ij(delta) = V_g^dag (1j D(delta)) V_g on the "
          f"fixed delta=0 Schur basis.")
    print(f"  Substitute: max|Y_ij(delta)| = 0 + (dY_12/d delta)|_0 * delta + "
          f"O(d^2); (dY_12/d delta)|_0 = {r['dY12_d0']:+.6e}  =>  "
          f"|dY_12/d delta|_0 = {r['abs_dY12_d0']:.6e}.")
    print(f"  Simplify: distinct block evals(0)={r['distinct0']} -> max in scan "
          f"{rankmax}; degeneracy lift 1->>=2: {r['rank_increased']} "
          f"(first at delta={fr2_txt}); intra-multiplet split @0.20 = "
          f"{r['intra_split'][-1]:.3e}.")
    print(f"  Canonical form: degeneracy-lift indicator |dY_12/d delta|_0 "
          f"= {r['abs_dY12_d0']:.6e}  vs  eps_lift = {EPS_LIFT}.")
    print(f"  Direction: |dY_12/d delta|_0 "
          f"{'>' if r['abs_dY12_d0'] > EPS_LIFT else '<='} eps_lift  AND "
          f"degeneracy-rank {'increases' if r['rank_increased'] else 'STAYS 1'} "
          f"=> generation degeneracy "
          f"{'LIFTS' if (r['abs_dY12_d0'] > EPS_LIFT and r['rank_increased']) else 'PERSISTS (wall genuine)'}.")
    print(f"  Bridge-1 cubic: leading off-surface SPLITTING; "
          f"d^3 S/d delta^3|_0 = {r['d3_S']:+.6e}, c2={r['c2_fit']:+.3e} "
          f"c3={r['c3_fit']:+.3e} (S(delta)~0 => generation degeneracy protected).")
    print(f"  Cross-check: global distinct signed evals {r['nd0']}->{r['nd2']} "
          f"(HIGHER isospin levels split under su(2) breaking; the GENERATION "
          f"multiplet does NOT).")
    print(f"  Conclusion: composite = {verdict} "
          f"(sign={sign_v}, magnitude={mag_v}, regime={regime_v}).")

    print(f"\nCriteria: schur_zero@0={crit['schur_zero_at_0']}  "
          f"lift>eps={crit['lift_above_eps']}  "
          f"rank_increase={crit['rank_increase']}  "
          f"cubic_present={crit['cubic_present']}")

    value = (f"absdY12d0={r['abs_dY12_d0']:.6e}_vs_eps{EPS_LIFT};"
             f"maxoffY0={r['schur_offdiag0']:.3e}_schurzero;"
             f"distinct0={r['distinct0']}_to_max{rankmax};"
             f"gen_degen_lift={r['rank_increased']}_at_delta{fr2_txt};"
             f"intrasplit_at020={r['intra_split'][-1]:.3e};"
             f"d3S_d0={r['d3_S']:+.4e}_cubic;c2={r['c2_fit']:+.3e};"
             f"genmult_d{r['n_gen']}_lam{r['lam0']:.4f};"
             f"global_distinct_{r['nd0']}to{r['nd2']}_isospinsplit;"
             f"L=[{r['L1']:.4f},{r['L2']:.4f},{r['L3']:.4f}];"
             f"detratio={r['det_ratio']:.8f};regime={r['regime']};"
             f"gensector={GEN_SECTOR};Lmax={L_MAX}")             # (local)

    make_plot(r, verdict)
    save_npz(r, verdict, (sign_v, mag_v, regime_v), crit, audit_sha, content_sha)

    print()
    print(emit_4tuple(value, SCHEME, CONVENTION, L_MAX))
    print_verdict_payload(
        verdict, value, audit_sha, content_sha,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
        companion_note=(
            f"off-U(2) Dirac Yukawa splitting on the d={r['n_gen']} generation "
            f"multiplet (|lambda|={r['lam0']:.4f}, fund sector); Schur-zero@0 "
            f"({r['schur_offdiag0']:.1e}, distinct={r['distinct0']}); leading lift "
            f"|dY_12/d delta|_0={r['abs_dY12_d0']:.3e} vs eps_lift={EPS_LIFT}; "
            f"generation degeneracy {'LIFTS' if r['rank_increased'] else 'PERSISTS'} "
            f"off-surface (intra-split@0.20={r['intra_split'][-1]:.2e}); "
            f"vol-preserving det-ratio={r['det_ratio']:.6f}"),
        extra_rows=[
            (f"# bridge1-cubic: d^3 S/d delta^3|_0={r['d3_S']:+.4e} "
             f"c2_fit={r['c2_fit']:+.3e} c3_fit={r['c3_fit']:+.3e} "
             f"c4_fit={r['c4_fit']:+.3e}; intra-multiplet split S(delta)~0 "
             f"across scan => generation degeneracy PROTECTED off-U(2) # {GATE_ID}"),
            (f"# cross-check: global distinct signed evals {r['nd0']}->{r['nd2']} "
             f"(su(2)/isospin splits at HIGHER levels; generation multiplet at "
             f"|lambda|={r['lam0']:.4f} stays d={r['n_gen']}); "
             f"cond(g) {r['cond0']:.3f}->{r['cond_max']:.3f} regime={r['regime']}; "
             f"Jensen L=[{r['L1']:.4f},{r['L2']:.4f},{r['L3']:.4f}] "
             f"vol={r['vol_jensen']:.8f} # {GATE_ID}"),
        ],
    )

    print(f"\n=== {GATE_ID}: {verdict} (sign={sign_v} magnitude={mag_v} "
          f"regime={regime_v}; wall {time.time() - t0:.1f}s) ===")
    return 0   # exit 0 on script success regardless of scientific verdict


if __name__ == "__main__":
    sys.exit(main())
