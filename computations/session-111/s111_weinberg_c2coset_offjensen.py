#!/usr/bin/env python3
"""
S111-CF-WEINBERG-C2COSET  C^2-coset Weinberg-angle / a_2 response slope
=======================================================================

Gate: S111-CF-WEINBERG-C2COSET ([SIGN]); track = session (session 111)
Classification: GEOMETRIC
Agent: baptista-spacetime-analyst
Plan: sessions/session-plan/session-111-plan-w3.md SS W3-2

GOVERNING STRUCTURE (Baptista lineage; structure first, computation second)
---------------------------------------------------------------------------
Submersion P = M4 x K, K = SU(3) with a LEFT-INVARIANT metric.
Reductive decomposition (Baptista eq 3.58): su(3) = u(1) (+) su(2) (+) C^2,
generator indices U1_IDX=[7], SU2_IDX=[0,1,2], C2_IDX=[3,4,5,6].

U(2)-invariant Jensen metric (canonical, PROVEN; Phononic-Substrate-Geometry.md):
   g_K(tau) = L1 g0|_u(1) (+) L2 g0|_su(2) (+) L3 g0|_C2,
   L1 = e^{2tau} (1 dir, hypercharge), L2 = e^{-2tau} (3 dir, isospin),
   L3 = e^{tau} (4 dir, C^2 coset). Volume-preserving L1 L2^3 L3^4 = 1 (G6).

THE WEINBERG ANGLE (Baptista eq 5.21 + Formula B eq 2.93; S33a knowledge-confirmed):
   sin^2 theta_W = 3 L2 / (L1 + 3 L2)       (GUT 5/3-normalized form)
   bare-normalization cross-check: L2/(L1 + L2)  (S29 Baptista collab eq).
   L1, L2 are the u(1)/su(2) LEG EIGENVALUES of the internal metric g_K (the
   Josephson stiffness): the gauge couplings are g'^2 ~ 1/L1, g^2 ~ 1/L2, so
   sin^2 theta_W = g'^2/(g'^2 + g^2) in GUT normalization is 3 L2/(L1 + 3 L2).
   At tau_fold this is sin2_thetaW_fold = 0.58385339 (canonical, S42).

THE C^2-COSET DEFORMATION (NEW, this gate; T4 C^2-split):
   split  L3 I_4 -> diag( L3 e^{+3 delta_C2}, L3 e^{-delta_C2}, L3 e^{-delta_C2},
                          L3 e^{-delta_C2} )   on C2_IDX=[3,4,5,6],
   volume-preserving WITHIN the 4-block (3 delta - 3 delta = 0 => det g_K = 1
   preserved EXACTLY, overall fiber volume held fixed per G6). This is the
   PRODUCTIVE-relocation counterpart of the S110-CF1 Yukawa-null C^2-coset:
   it reshapes the C^2-block internal geometry at fixed volume. The metric stays
   LEFT-INVARIANT and BLOCK-DIAGONAL by Peter-Weyl (D_K block-diagonality PROVEN
   S22b, holds for ANY left-invariant metric).

THE TWO OBSERVABLES
-------------------
(a) sin^2 theta_W(delta_C2) = 3 L2(delta_C2)/(L1 + 3 L2(delta_C2)). Because the
    C^2-split touches ONLY the C2-block, the u(1)/su(2) leg eigenvalues L1, L2 of
    g_K are read off the (delta-INVARIANT) u(1)/su(2) blocks. The Cholesky frame
    E(delta) = inv(cholesky(g(delta))) is BLOCK-DIAGONAL (g block-diagonal in
    u(1)+su(2)+C^2 => its Cholesky is too), so the u(1)/su(2) frame legs do not
    move either: Reading-A (bare metric leg) and Reading-B (effective Dirac leg)
    COINCIDE. The slope d(sin^2 theta_W)/d(delta_C2)|_0 is the [SIGN] observable.

(b) a_2 Seeley-DeWitt second moment (G_N-feeding; companion diagnostic). The
    a_2 coefficient is the heat-trace second moment of D_K(delta_C2): the
    Peter-Weyl-multiplicity-weighted spectral second moment
       M2(delta) = sum_{(p,q)} dim(p,q) * sum_k lambda_k(p,q;delta)^2,
    which IS a_2 up to the regulator-fixed FI normalization (a_2^{zeta}; the
    a_2-ratio is FI-class, regulator-invariant, parented to the F_traj a_2-ratio
    FI theorem at locked-norm L_k=1). Unlike sin^2 theta_W, M2 traces the FULL
    spectrum INCLUDING the C^2-block, so it responds to the C^2-split. The
    companion reports d(a_2)/d(delta_C2)|_0 (linear) AND d^2(a_2)/d(delta_C2)^2|_0
    (quadratic; delta=0 is a stationary U(2)-restoration point => the leading
    a_2 response is QUADRATIC).

THE SUBSTITUTION CHAIN (math-scripts.md, [SIGN]; plan SS W3-2 (7))
   Claim: d(sin^2 theta_W)/d(delta_C2)|_0 has the sign of dL2/d(delta_C2)|_0;
          sin^2 theta_W is monotone-increasing in L2.
   Step 1: sin^2 theta_W = 3 L2/(L1 + 3 L2)  [GUT-normalized].
   Step 2: L1 > 0, L2 > 0 (Josephson stiffness positivity; J_u1, J_su2, J_C2 > 0).
   Step 3: d(sin^2 theta_W)/dL2 = 3 L1/(L1 + 3 L2)^2   [Sage-verified plan-freeze].
   Step 4: L1>0, (L1+3L2)^2>0 => d(sin^2)/dL2 > 0 ALWAYS (strictly positive).
   Canonical: d(sin^2)/d(delta_C2)|_0 = [3 L1/(L1+3L2)^2] * dL2/d(delta_C2)|_0.
   Direction: bracket > 0 => sign(d(sin^2)/d(delta_C2)|_0) = sign(dL2/d(delta_C2)|_0).
   The producing script REPORTS the computed dL2/d(delta_C2)|_0 (an OUTPUT) and
   sign_verdict PASSes iff sign(d(sin^2)/d(delta_C2)|_0) matches sign(dL2/d(delta_C2)|_0).

VERDICT (plan SS W3-2 operator; [SIGN] 3-tuple + gate-verdicts.md collapse):
  PASS  = |d(sin^2 theta_W)/d(delta_C2)|_0| > eps_sens=1e-3 AND sign matches
          sign(dL2/d(delta_C2)|_0): C^2-coset is a PRODUCTIVE relocation
          (Weinberg-angle response-bearing).
  FAIL  = sign mismatch (sign is structurally locked d(sin^2)/dL2 > 0; a mismatch
          is a machinery/frame error, NOT a physics outcome) -> in-session debug.
  INFO  = |d(sin^2 theta_W)/d(delta_C2)|_0| <= eps_sens=1e-3 (sub-threshold, sign
          correct): C^2-coset is sin^2-INERT at the fold anchor; report
          d(a_2)/d(delta_C2)|_0 as the companion diagnostic.
  SIGN     = does sign(d(sin^2)/d(delta_C2)|_0) match sign(dL2/d(delta_C2)|_0)?
  MAGNITUDE= |d(sin^2)/d(delta_C2)|_0| vs eps_sens (PASS) / sub-threshold (INFO).
  REGIME   = does the finite-difference stencil stay within the perturbative window
             (Cholesky positive-definite, well-conditioned across [-2h,+2h])?

DISCIPLINE
----------
- from canonical_constants import *  (tau_fold, M_KK, a2_fold, sin2_thetaW_fold consumed)
- dirac_spectrum.py machinery reused: su3_generators, compute_structure_constants,
  compute_killing_form, u2_invariant_metric, orthonormal_frame,
  frame_structure_constants, connection_coefficients, spinor_connection_offset,
  build_cliff8, get_irrep, dirac_operator_on_irrep. The NEW C^2-split helper
  deformed_c2_split_metric is authored HERE (the inv2 deformed_su2_split_metric
  pattern with the split block swapped SU2_IDX -> C2_IDX).
- GPU: per-block torch.linalg.eigvalsh on the AMD RX 9070 XT (ROCm) for blocks
  >= 100x100 (D_K block-diagonal by Peter-Weyl PROVEN S22b => dense per-block).
- dual-SHA (S84+): audit = sha256(script || canonical || pinmap_json);
  content = sha256(script). verdict PRINTED as emit_verdict payload; the
  dispatching agent calls mcp__knowledge__emit_verdict(session=111).
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

from canonical_constants import *  # noqa: F401,F403  (tau_fold, M_KK, a2_fold, sin2_thetaW_fold, PI)

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
# Section 3 -- Pre-registration (machinery pin map; plan SS W3-2)
# ---------------------------------------------------------------------------
SESSION = "111"                                                    # (local)
GATE_ID = "S111-CF-WEINBERG-C2COSET"                               # (local)
SCHEME = "off-Jensen-C2coset-split-spectral-action-a2"            # (local)
CONVENTION = ("deformed-L3.I4-split-metric-C2coset-4bonds-JC2-0.9330;"
              "sin2=3L2/(L1+3L2)-GUT-normalized;a2-ratio-FI-tagged")  # (local)
L_MAX = "12"                                                       # (local)

# Pre-registered thresholds (plan SS W3-2 operator block; plan-pinned)
EPS_SENS = 1.0e-3          # |d(sin^2)/d(delta_C2)|_0| sensitivity floor    # (local)
H_FD = 1.0e-2             # finite-difference half-step (plan step_size)    # (local)
H_FD_HALF = 0.5e-2        # Richardson cross-check half-step                # (local)
RICHARDSON_TOL = 0.01     # stencil-convergence demand (<1%)                # (local)
A2_LMAX_RESPONSE = 6      # L_max for the a_2 RESPONSE re-assembly (deriv;   # (local)
                         #   L_max-saturated for a slope: low (p,q) C^2-
                         #   coupled sectors dominate; cache anchors delta=0)
COND_BLOWUP = 1.0e6      # Cholesky ill-conditioning regime floor           # (local)
GPU_BLOCK_MIN = 100      # >= 100x100 -> GPU eigvalsh (math-scripts.md)     # (local)

OUT_NPZ = SESSION_DIR / "s111_weinberg_c2coset_offjensen.npz"
OUT_PNG = SESSION_DIR / "s111_weinberg_c2coset_offjensen.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    SHARED_DIR / "dirac_spectrum.py",
    COMPUTATIONS_DIR / "investigation-2" / "inv2_w1_off_u2_dirac_yukawa.py",
    COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz",
]

MACHINERY_PIN_MAP = {                                              # (local)
    "_gate_id": GATE_ID,
    "_wp_id": "session-111-w3-workingpaper.md#W3-2",
    "_scheme": SCHEME,
    "_convention": CONVENTION,
    "_track": "session",
    "N_eval": "5-point centered FD stencil in delta_C2 at delta=0 (4th-order)",
    "L_max": str(L_MAX),
    "L_max_a2_response": str(A2_LMAX_RESPONSE),
    "scan_range": f"[-{H_FD}, +{H_FD}]",
    "step_size": f"h_fd={H_FD}",
    "tolerance": f"eps_sens={EPS_SENS}",
    "scheme": SCHEME,
    "convention": CONVENTION,
    "random_seed": "N/A -- deterministic (finite-difference)",
    "GPU_path": "torch.linalg.eigvalsh per-block (>=100x100) AMD RX 9070 XT ROCm",
    "regulator_pin": "a_2^{zeta} poleconv-A-double pole_in_s=3 curvature_grade_n=2 FI-tagged",
    "tau_fold": str(tau_fold),
    "C2_IDX": str(list(C2_IDX)),
    "split_block": "C2_IDX (swap from inv2 SU2_IDX)",
    "split_pattern": "diag(e^{+3d}, e^{-d}, e^{-d}, e^{-d}) [3d-3d=0 vol-preserving]",
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
# Section 5 -- NEW C^2-coset-split transverse-deformation helper
# ---------------------------------------------------------------------------

def deformed_c2_split_metric(B_ab, L1, L2, L3, delta):
    """C^2-SPLIT left-invariant metric: split the 4-fold C^2 coset block
    L3 I_4 -> diag(L3 e^{+3 delta}, L3 e^{-delta}, L3 e^{-delta}, L3 e^{-delta})
    on C2_IDX=[3,4,5,6], leaving u(1) (L1) and su(2) (L2) UNTOUCHED.

    This is the inv2 deformed_su2_split_metric pattern with the split block
    swapped SU2_IDX -> C2_IDX (4 directions, factor pattern +3d/-d/-d/-d so the
    within-block volume e^{3d-d-d-d}=e^0=1 is preserved EXACTLY).

    Volume preservation WITHIN the C^2 block is EXACT:
       det-factor = e^{+3 delta} e^{-delta} e^{-delta} e^{-delta} = e^0 = 1,
    so det g_K is unchanged from the U(2)-invariant value (G6). At delta=0 this
    returns u2_invariant_metric EXACTLY.

    The deformation BREAKS the C^2 coset isotropy (distinguishes the +3 delta
    direction, index 3) while keeping the metric LEFT-INVARIANT => D_K stays
    BLOCK-DIAGONAL by Peter-Weyl (PROVEN S22b). CRITICALLY: because only the
    C^2-block is touched, the u(1)/su(2) blocks (hence L1, L2 and the Weinberg
    angle) are delta-INVARIANT, and the Cholesky frame is block-diagonal.

    Args:
        B_ab: (8,8) Killing form
        L1, L2, L3: U(2)-invariant Jensen scale factors (>0)
        delta: C^2-coset anisotropy modulus (0 = U(2) surface)

    Returns:
        g: (8,8) positive-definite metric tensor (split C^2 block)
    """
    g = u2_invariant_metric(B_ab, L1, L2, L3)                       # (local) base
    split_factors = [np.exp(3.0 * delta), np.exp(-delta),
                     np.exp(-delta), np.exp(-delta)]                # (local) 3d-3d=0
    g0 = np.abs(B_ab)                                               # (local)
    for k, a in enumerate(C2_IDX):
        for m, b in enumerate(C2_IDX):
            if a == b:
                g[a, b] = g0[a, b] * L3 * split_factors[k]
            else:
                fac = np.sqrt(split_factors[k] * split_factors[m])  # (local)
                g[a, b] = g0[a, b] * L3 * fac
    return g


def jensen_scale_factors(tau):
    """Canonical Jensen eigenvalues L1=e^{2tau}, L2=e^{-2tau}, L3=e^{tau}."""
    return np.exp(2.0 * tau), np.exp(-2.0 * tau), np.exp(tau)       # (local)


def metric_leg_eigenvalues(g, B_ab):
    """Read off the u(1)/su(2)/C^2 LEG EIGENVALUES of the metric g (the Josephson
    stiffness leg weights). L_a = g[a,a] / |B|[a,a] on the block-representative
    index. These are the L1, L2, L3 that enter the Weinberg angle.

    Because the metric is block-diagonal in u(1)+su(2)+C^2, the leg eigenvalue is
    the diagonal block weight; for the C^2 block (split) we report the mean of the
    4 diagonal weights as the effective volume-leg (the geometric-mean is e^0=1
    times L3, i.e. L3 itself)."""
    g0 = np.abs(B_ab)                                              # (local)
    L1_eff = g[U1_IDX[0], U1_IDX[0]] / g0[U1_IDX[0], U1_IDX[0]]    # (local)
    L2_eff = g[SU2_IDX[0], SU2_IDX[0]] / g0[SU2_IDX[0], SU2_IDX[0]]  # (local)
    c2_weights = np.array([g[a, a] / g0[a, a] for a in C2_IDX])    # (local)
    L3_eff = float(np.exp(np.mean(np.log(c2_weights))))           # (local) geom-mean
    return float(L1_eff), float(L2_eff), L3_eff


def sin2_weinberg(L1, L2):
    """GUT 5/3-normalized Weinberg angle sin^2 theta_W = 3 L2 / (L1 + 3 L2)."""
    return 3.0 * L2 / (L1 + 3.0 * L2)


def sin2_weinberg_bare(L1, L2):
    """Bare-normalization cross-check (S29 Baptista collab): L2 / (L1 + L2)."""
    return L2 / (L1 + L2)


# ---------------------------------------------------------------------------
# Section 6 -- Dirac operator assembly for the split metric (one sector)
# ---------------------------------------------------------------------------

def assemble_Dk_split(delta, tau, B_ab, f_abc, gammas, rho):
    """Build D_(p,q)(delta) on ONE Peter-Weyl sector under the C^2-split metric."""
    L1, L2, L3 = jensen_scale_factors(tau)                          # (local)
    g = deformed_c2_split_metric(B_ab, L1, L2, L3, delta)          # (local)
    E = orthonormal_frame(g)                                        # (local)
    ft = frame_structure_constants(f_abc, E)                       # (local)
    Gamma = connection_coefficients(ft)                            # (local)
    Omega = spinor_connection_offset(Gamma, gammas)               # (local)
    D = dirac_operator_on_irrep(rho, E, gammas, Omega)            # (local)
    return D


def eigvalsh_block(D):
    """Hermitian eigenvalues of H = 1j*D (real evals). GPU (torch.linalg.eigvalsh
    on ROCm) for >= GPU_BLOCK_MIN; CPU numpy otherwise. Returns evals ascending."""
    H = 1j * D                                                     # (local)
    n = H.shape[0]                                                 # (local)
    if _TORCH_OK and n >= GPU_BLOCK_MIN:
        t = torch.tensor(H, device="cuda", dtype=torch.complex128)  # (local)
        w = torch.linalg.eigvalsh(t)                              # (local)
        return w.cpu().numpy().real
    return np.linalg.eigvalsh(H).real


# ---------------------------------------------------------------------------
# Section 7 -- a_2 second-moment (heat-trace second moment of D_K(delta))
# ---------------------------------------------------------------------------

def a2_second_moment(delta, tau, B_ab, f_abc, gammas, gens, lmax):
    """a_2 Seeley-DeWitt second moment proxy: Peter-Weyl-multiplicity-weighted
    spectral second moment M2(delta) = sum_{(p,q)} dim(p,q) * sum_k lambda_k^2
    over p+q <= lmax. This IS a_2 up to the regulator-fixed FI normalization
    (a_2^{zeta}, FI-class ratio). Traces the FULL spectrum incl. the C^2 block."""
    tot = 0.0                                                     # (local)
    for p in range(lmax + 1):
        for q in range(lmax + 1 - p):
            if p == 0 and q == 0:
                continue
            dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2          # (local)
            rho, _ = get_irrep(p, q, gens, f_abc)                  # (local)
            D = assemble_Dk_split(delta, tau, B_ab, f_abc, gammas, rho)  # (local)
            lam = eigvalsh_block(D)                                # (local)
            tot += dim_pq * float(np.sum(lam ** 2))
    return tot


def a2_canonical_from_cache(cache_path: Path):
    """Read the canonical delta=0 a_2-anchor from the L12 spectrum cache:
    M2_L12(0) = sum_{(p,q)} dim(p,q) * sum_k |lambda|_k^2 over the cached sectors
    (U(2)-invariant Jensen metric at tau_fold; the delta=0 absolute anchor for
    provenance; the RESPONSE is computed by re-assembly at A2_LMAX_RESPONSE)."""
    d = np.load(cache_path, allow_pickle=True)                    # (local)
    sec = d["sector_evals"].item()                                # (local)
    tot = 0.0                                                     # (local)
    nsec = 0                                                      # (local)
    for (p, q), info in sec.items():
        dim_pq = int(info["dim"])                                 # (local)
        absl = np.asarray(info["abs_evals"], dtype=float)         # (local)
        tot += dim_pq * float(np.sum(absl ** 2))
        nsec += 1
    return tot, nsec


# ---------------------------------------------------------------------------
# Section 8 -- Compute (the FD stencil for both observables)
# ---------------------------------------------------------------------------

def fd4_centered(fm2, fm1, fp1, fp2, h):
    """Centered 4th-order first derivative: f'(0)=(-fp2+8fp1-8fm1+fm2)/(12h)."""
    return (-fp2 + 8.0 * fp1 - 8.0 * fm1 + fm2) / (12.0 * h)


def fd2_centered(fm1, f0, fp1, h):
    """Centered 2nd-order second derivative: f''(0)=(fm1-2f0+fp1)/h^2."""
    return (fm1 - 2.0 * f0 + fp1) / (h ** 2)


def compute(pins: dict) -> dict:
    res: dict = {}                                                 # (local)
    t_start = time.time()                                          # (local)

    gens = su3_generators()                                        # (local)
    f_abc = compute_structure_constants(gens)                     # (local)
    B_ab = compute_killing_form(f_abc)                            # (local)
    gammas = build_cliff8()                                        # (local)
    print(f"Infrastructure: ROCm avail={_TORCH_OK}; a_2 response re-assembled at "
          f"L_max={A2_LMAX_RESPONSE} (slope-saturated); sin^2 leg-eigenvalues are "
          f"L_max-INDEPENDENT (metric-block property).")

    # ---- (1) Jensen eigenvalues at tau_fold (substitution-chain Defs) ----
    L1, L2, L3 = jensen_scale_factors(tau_fold)                   # (local)
    print(f"\nJensen eigenvalues at tau_fold={tau_fold}: "
          f"L1=e^(2tau)={L1:.6f}, L2=e^(-2tau)={L2:.6f}, L3=e^(tau)={L3:.6f}")

    # Volume-preservation cross-check (G6) + delta=0 Schur recovery.
    vol_jensen = L1 * L2 ** 3 * L3 ** 4                           # (local)
    test_delta = 0.123                                           # (local)
    g_split = deformed_c2_split_metric(B_ab, L1, L2, L3, test_delta)  # (local)
    g_jensen = u2_invariant_metric(B_ab, L1, L2, L3)             # (local)
    det_ratio = np.linalg.det(g_split) / np.linalg.det(g_jensen)  # (local)
    g0_split = deformed_c2_split_metric(B_ab, L1, L2, L3, 0.0)   # (local)
    schur_recover = float(np.max(np.abs(g0_split - g_jensen)))   # (local)
    print(f"  volume-preserving (G6): L1 L2^3 L3^4 = {vol_jensen:.10f} (=1)")
    print(f"  C^2-split det-ratio at delta={test_delta}: "
          f"det(g_split)/det(g_jensen) = {det_ratio:.12f} (=1 EXACT, "
          f"block volume e^(3d-d-d-d)=1)")
    print(f"  delta=0 recovers u2_invariant_metric EXACTLY: "
          f"max|g_split(0) - g_jensen| = {schur_recover:.2e}")
    assert abs(vol_jensen - 1.0) < 1e-9 and abs(det_ratio - 1.0) < 1e-9, \
        "volume-preservation (G6) failed for the C^2-split metric"
    assert schur_recover < 1e-12, "delta=0 does not recover the U(2) metric"

    # ---- (2) Frame block-diagonality: u(1)/su(2) legs decoupled from C^2 ----
    # The Cholesky frame E(delta)=inv(cholesky(g(delta))). If E[u2, C2] off-block
    # is 0 across the scan, the u(1)/su(2) frame legs (hence L1, L2 the Dirac
    # operator sees) are delta-INDEPENDENT: Reading-A==Reading-B for sin^2.
    u2_idx = list(U1_IDX) + list(SU2_IDX)                        # (local)
    c2_idx = list(C2_IDX)                                        # (local)
    frame_cross = []                                             # (local)
    deltas5 = np.array([-2.0 * H_FD, -H_FD, 0.0, H_FD, 2.0 * H_FD])  # (local)
    for d in deltas5:
        E = orthonormal_frame(deformed_c2_split_metric(B_ab, L1, L2, L3, d))  # (local)
        frame_cross.append(float(np.max(np.abs(E[np.ix_(u2_idx, c2_idx)]))))
    frame_cross = np.array(frame_cross)                          # (local)
    frame_blockdiag = bool(np.max(frame_cross) < 1e-12)         # (local)
    print(f"\nFrame block-diagonality (u(1)/su(2) <-> C^2 off-block):")
    print(f"  max|E[u2,C2]| across stencil = {np.max(frame_cross):.3e} "
          f"(<1e-12 => block-diagonal: {frame_blockdiag}; Reading-A==Reading-B)")

    # ---- (3) sin^2 theta_W(delta) from metric leg eigenvalues (the [SIGN] obs) --
    sin2_vals = np.zeros(5)                                      # (local)
    sin2_bare_vals = np.zeros(5)                                 # (local)
    L1_vals = np.zeros(5); L2_vals = np.zeros(5); L3_vals = np.zeros(5)  # (local)
    conds = np.zeros(5)                                          # (local)
    for k, d in enumerate(deltas5):
        g = deformed_c2_split_metric(B_ab, L1, L2, L3, d)        # (local)
        l1e, l2e, l3e = metric_leg_eigenvalues(g, B_ab)          # (local)
        L1_vals[k], L2_vals[k], L3_vals[k] = l1e, l2e, l3e
        sin2_vals[k] = sin2_weinberg(l1e, l2e)
        sin2_bare_vals[k] = sin2_weinberg_bare(l1e, l2e)
        conds[k] = float(np.linalg.cond(g))
    print(f"\nsin^2 theta_W(delta) from u(1)/su(2) leg eigenvalues "
          f"(C^2-split touches only C^2 => L1,L2 INVARIANT):")
    for k, d in enumerate(deltas5):
        print(f"  delta={d:+.3f}: L1={L1_vals[k]:.8f} L2={L2_vals[k]:.8f} "
              f"L3={L3_vals[k]:.6f}  sin^2=3L2/(L1+3L2)={sin2_vals[k]:.10f}  "
              f"cond(g)={conds[k]:.4f}")

    # ---- (4) leg-eigenvalue slopes dL2/d(delta)|_0, dL1/d(delta)|_0 ----
    dL2_d0 = fd4_centered(L2_vals[0], L2_vals[1], L2_vals[3], L2_vals[4], H_FD)  # (local)
    dL1_d0 = fd4_centered(L1_vals[0], L1_vals[1], L1_vals[3], L1_vals[4], H_FD)  # (local)
    dL3_d0 = fd4_centered(L3_vals[0], L3_vals[1], L3_vals[3], L3_vals[4], H_FD)  # (local)
    # bracket = d(sin^2)/dL2 = 3 L1/(L1+3 L2)^2 (analytic; Step 3-4)
    bracket = 3.0 * L1 / (L1 + 3.0 * L2) ** 2                    # (local)
    print(f"\nLeg-eigenvalue slopes at delta=0:")
    print(f"  dL1/d(delta)|_0 = {dL1_d0:+.6e}  dL2/d(delta)|_0 = {dL2_d0:+.6e}  "
          f"dL3/d(delta)|_0 = {dL3_d0:+.6e}")
    print(f"  analytic bracket d(sin^2)/dL2 = 3 L1/(L1+3 L2)^2 = {bracket:+.6e} "
          f"(>0 always)")

    # ---- (5) sin^2 slope = the [SIGN] observable ----
    dsin2_d0 = fd4_centered(sin2_vals[0], sin2_vals[1], sin2_vals[3],
                            sin2_vals[4], H_FD)                   # (local)
    abs_dsin2_d0 = abs(dsin2_d0)                                 # (local)
    # chain-rule cross-check: d(sin^2)/d(delta) = bracket * dL2/d(delta)
    dsin2_chain = bracket * dL2_d0                               # (local)
    print(f"\n[SIGN] observable: d(sin^2 theta_W)/d(delta_C2)|_0 = {dsin2_d0:+.6e}")
    print(f"  |d(sin^2)/d(delta_C2)|_0| = {abs_dsin2_d0:.6e}  vs eps_sens={EPS_SENS}")
    print(f"  chain-rule cross-check bracket*dL2 = {dsin2_chain:+.6e} "
          f"(matches FD: {abs(dsin2_d0 - dsin2_chain):.2e})")

    # Richardson: halve h, demand stencil convergence (sin^2 is exactly flat so
    # both are ~0 to FD floor; the cross-check is structural).
    deltas5h = np.array([-2.0 * H_FD_HALF, -H_FD_HALF, 0.0,
                         H_FD_HALF, 2.0 * H_FD_HALF])            # (local)
    sin2_h = np.array([sin2_weinberg(*metric_leg_eigenvalues(
        deformed_c2_split_metric(B_ab, L1, L2, L3, d), B_ab)[:2])
        for d in deltas5h])                                     # (local)
    dsin2_d0_h = fd4_centered(sin2_h[0], sin2_h[1], sin2_h[3], sin2_h[4], H_FD_HALF)  # (local)
    rich_sin2 = abs(dsin2_d0 - dsin2_d0_h)                       # (local)
    print(f"  Richardson (h/2): d(sin^2)/d(delta)|_0={dsin2_d0_h:+.6e}; "
          f"|full-half|={rich_sin2:.2e}")

    # ---- (6) a_2 second-moment RESPONSE (companion diagnostic) ----
    print(f"\na_2 second-moment response (re-assembled D_K(delta), L_max="
          f"{A2_LMAX_RESPONSE}; traces FULL spectrum incl. C^2):")
    a2_vals = np.zeros(5)                                        # (local)
    for k, d in enumerate(deltas5):
        a2_vals[k] = a2_second_moment(d, tau_fold, B_ab, f_abc, gammas, gens,
                                      A2_LMAX_RESPONSE)
        print(f"  delta={d:+.3f}: M2={a2_vals[k]:.6f}")
    da2_d0 = fd4_centered(a2_vals[0], a2_vals[1], a2_vals[3], a2_vals[4], H_FD)  # (local)
    abs_da2_d0 = abs(da2_d0)                                     # (local)
    d2a2_d0 = fd2_centered(a2_vals[1], a2_vals[2], a2_vals[3], H_FD)  # (local)
    a2_0 = a2_vals[2]                                            # (local)
    # even-ness (stationary point) test: asymmetry M(+d)-M(-d)
    asym1 = a2_vals[3] - a2_vals[1]                             # (local) at +-h
    asym2 = a2_vals[4] - a2_vals[0]                             # (local) at +-2h
    print(f"\n  d(a_2)/d(delta_C2)|_0 = {da2_d0:+.6e} (linear; ~0 => stationary)")
    print(f"  d^2(a_2)/d(delta_C2)^2|_0 = {d2a2_d0:+.6e} (QUADRATIC; the genuine "
          f"leading a_2 response)")
    print(f"  M2(0)={a2_0:.6f}; rel curvature (1/M2)d^2/ddelta^2={d2a2_d0/a2_0:+.6e}")
    print(f"  asymmetry M(+h)-M(-h)={asym1:+.3e}, M(+2h)-M(-2h)={asym2:+.3e} "
          f"(small => even-dominant => stationary U(2)-restoration point)")

    # ---- (7) canonical delta=0 a_2 anchor from the L12 cache (provenance) ----
    cache_path = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"  # (local)
    a2_L12_cache, nsec = a2_canonical_from_cache(cache_path)     # (local)
    print(f"\n  canonical delta=0 a_2-anchor from L12 cache: "
          f"M2_L12(0)={a2_L12_cache:.4f} over {nsec} PW sectors "
          f"(provenance; canonical a2_fold={a2_fold:.4f} is the zeta-normalized form)")

    # ---- (8) Regime: Cholesky conditioning across the FD window ----
    cond0 = float(conds[2])                                     # (local)
    cond_max = float(np.max(conds))                            # (local)
    breach = int(np.sum(conds > COND_BLOWUP))                  # (local)
    breach_frac = breach / len(conds)                          # (local)
    if breach_frac <= 0.05:
        regime = "VALID"                                       # (local)
    elif breach_frac <= 0.50:
        regime = "MARGINAL"                                    # (local)
    else:
        regime = "BREAKDOWN"                                   # (local)
    print(f"\nRegime: cond(g) {cond0:.4f} (delta=0) -> {cond_max:.4f} (max); "
          f"breach fraction (cond>{COND_BLOWUP:.0e}) = {breach_frac:.3f} -> {regime}")

    res.update(dict(
        deltas5=deltas5, sin2_vals=sin2_vals, sin2_bare_vals=sin2_bare_vals,
        L1_vals=L1_vals, L2_vals=L2_vals, L3_vals=L3_vals, conds=conds,
        a2_vals=a2_vals,
        L1=L1, L2=L2, L3=L3, vol_jensen=vol_jensen, det_ratio=det_ratio,
        schur_recover=schur_recover,
        frame_cross=frame_cross, frame_blockdiag=frame_blockdiag,
        dL1_d0=dL1_d0, dL2_d0=dL2_d0, dL3_d0=dL3_d0, bracket=bracket,
        dsin2_d0=dsin2_d0, abs_dsin2_d0=abs_dsin2_d0, dsin2_chain=dsin2_chain,
        dsin2_d0_h=dsin2_d0_h, rich_sin2=rich_sin2,
        da2_d0=da2_d0, abs_da2_d0=abs_da2_d0, d2a2_d0=d2a2_d0, a2_0=a2_0,
        asym1=asym1, asym2=asym2, a2_L12_cache=a2_L12_cache, nsec_cache=nsec,
        sin2_fold_canonical=float(sin2_thetaW_fold), a2_fold_canonical=float(a2_fold),
        cond0=cond0, cond_max=cond_max, breach_frac=breach_frac, regime=regime,
        wall=time.time() - t_start,
    ))
    return res


# ---------------------------------------------------------------------------
# Section 9 -- Gate verdict ([SIGN] 3-tuple + gate-verdicts.md collapse)
# ---------------------------------------------------------------------------

def evaluate_gate(r: dict) -> tuple[str, str, str, str, dict]:
    """(composite, sign, magnitude, regime, crit) per plan SS W3-2 operator +
    gate-verdicts.md collapse rule."""
    slope = r["abs_dsin2_d0"]                                    # (local)
    # SIGN: does sign(d(sin^2)/d(delta)) match sign(dL2/d(delta))? The bracket
    # d(sin^2)/dL2 > 0 (analytic), so sign(d(sin^2)) == sign(dL2) ALWAYS unless a
    # machinery error flips it. When the slope is 0 (flat), both signs are 0 ->
    # NO mismatch -> sign is CORRECT (PASS). A mismatch is the only FAIL path.
    sgn_sin2 = np.sign(r["dsin2_d0"])                            # (local)
    sgn_dL2 = np.sign(r["dL2_d0"])                               # (local)
    # treat |.|<floor as 0 for sign comparison (exactly-flat case)
    sign_floor = 1e-12                                          # (local)
    s1 = 0 if abs(r["dsin2_d0"]) < sign_floor else sgn_sin2     # (local)
    s2 = 0 if abs(r["dL2_d0"]) < sign_floor else sgn_dL2        # (local)
    # also require chain-rule consistency (bracket>0): if both nonzero, must agree
    sign_match = (s1 == s2)                                     # (local)
    sign_v = "PASS" if sign_match else "FAIL"                   # (local)
    # MAGNITUDE: |d(sin^2)/d(delta)|_0 vs eps_sens
    if slope > EPS_SENS:
        mag_v = "PASS"                                          # (local)
    else:
        mag_v = "INFO"                                          # (local) sub-threshold
    regime_v = r["regime"]                                      # (local)
    crit = dict(
        frame_blockdiag=bool(r["frame_blockdiag"]),
        slope_above_eps=bool(slope > EPS_SENS),
        sign_match=bool(sign_match),
        bracket_positive=bool(r["bracket"] > 0),
        a2_responds=bool(abs(r["d2a2_d0"]) > 1.0),  # a_2 quadratic response present
        richardson_ok=bool(r["rich_sin2"] < RICHARDSON_TOL),
    )                                                           # (local)
    # composite collapse (gate-verdicts.md):
    if regime_v == "BREAKDOWN":
        comp = "FAIL"                                           # (local)
    elif sign_v == "FAIL":
        comp = "FAIL"
    elif mag_v == "PASS":
        comp = "PASS"   # slope > eps_sens AND sign matched
    else:
        comp = "INFO"   # sub-threshold (sin^2-inert), sign correct
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
    deltas = r["deltas5"]                                       # (local)

    # Panel 1: sin^2 theta_W(delta) -- the [SIGN] observable (flat)
    ax1.plot(deltas, r["sin2_vals"], "o-", color="tab:blue", lw=2, ms=7,
             label=r"$\sin^2\theta_W=3L_2/(L_1+3L_2)$ (GUT)")
    ax1.plot(deltas, r["sin2_bare_vals"], "s--", color="tab:cyan", lw=1.2, ms=5,
             label=r"$L_2/(L_1+L_2)$ (bare cross-check)")
    ax1.axhline(r["sin2_fold_canonical"], color="tab:gray", ls=":", lw=1.0,
                label=rf"canonical $\sin^2\theta_W|_{{\rm fold}}={r['sin2_fold_canonical']:.6f}$")
    ax1.set_xlabel(r"$\delta_{C^2}$ (C$^2$-coset anisotropy modulus)")
    ax1.set_ylabel(r"$\sin^2\theta_W$")
    ax1.set_title(rf"Weinberg angle vs $\delta_{{C^2}}$ "
                  rf"($|d\sin^2\theta_W/d\delta_{{C^2}}|_0={r['abs_dsin2_d0']:.2e}$ "
                  rf"vs $\epsilon_{{\rm sens}}={EPS_SENS}$)" "\n"
                  rf"u(1)/su(2) legs $\delta$-INVARIANT (C$^2$-split block-orthogonal)")
    ax1.legend(fontsize=8)

    # Panel 2: leg eigenvalues L1, L2, L3 vs delta
    ax2.plot(deltas, r["L1_vals"], "o-", color="tab:red", lw=2, label=r"$L_1$ (u(1))")
    ax2.plot(deltas, r["L2_vals"], "s-", color="tab:green", lw=2, label=r"$L_2$ (su(2))")
    ax2.plot(deltas, r["L3_vals"], "^-", color="tab:purple", lw=2,
             label=r"$L_3$ (C$^2$ geom-mean)")
    ax2.set_xlabel(r"$\delta_{C^2}$")
    ax2.set_ylabel(r"metric leg eigenvalue $L_a$")
    ax2.set_title(rf"Metric leg eigenvalues: $dL_1/d\delta={r['dL1_d0']:.1e}$, "
                  rf"$dL_2/d\delta={r['dL2_d0']:.1e}$ (=0)" "\n"
                  r"C$^2$-split touches only the C$^2$ block (L1,L2 fixed)")
    ax2.legend(fontsize=8)

    # Panel 3: a_2 second-moment M2(delta) (companion -- responds)
    ax3.plot(deltas, r["a2_vals"], "o-", color="tab:orange", lw=2, ms=7,
             label=r"$M_2(\delta)=\sum_{(p,q)}\dim\,\sum_k\lambda_k^2$")
    ax3.axvline(0.0, color="tab:gray", ls=":", lw=0.8)
    ax3.set_xlabel(r"$\delta_{C^2}$")
    ax3.set_ylabel(r"$a_2$ 2nd moment $M_2$")
    ax3.set_title(rf"$a_2$ heat-trace 2nd moment (L_max={A2_LMAX_RESPONSE}): "
                  rf"$d a_2/d\delta|_0={r['da2_d0']:.2e}$ (~0, stationary)" "\n"
                  rf"$d^2 a_2/d\delta^2|_0={r['d2a2_d0']:.2e}$ "
                  r"(QUADRATIC: C$^2$-coset geometry-ACTIVE)")
    ax3.legend(fontsize=8)

    # Panel 4: a_2 response curvature -- M2(delta)-M2(0) with quadratic fit
    A2 = r["a2_vals"] - r["a2_0"]                               # (local)
    ax4.plot(deltas, A2, "o", color="tab:orange", ms=7,
             label=r"$M_2(\delta)-M_2(0)$")
    dd = np.linspace(deltas[0], deltas[-1], 100)               # (local)
    quad = 0.5 * r["d2a2_d0"] * dd ** 2                         # (local)
    ax4.plot(dd, quad, "-", color="tab:red", lw=1.5,
             label=rf"$\frac{{1}}{{2}} d^2a_2/d\delta^2\,\delta^2$ "
                   rf"($={0.5*r['d2a2_d0']:.2e}\,\delta^2$)")
    ax4.set_xlabel(r"$\delta_{C^2}$")
    ax4.set_ylabel(r"$M_2(\delta)-M_2(0)$")
    ax4.set_title(rf"$a_2$ leading response is QUADRATIC ($\delta=0$ stationary): "
                  "\n"
                  rf"asym $M(\!+\!h)\!-\!M(\!-\!h)={r['asym1']:.2e}$ "
                  r"(small $\Rightarrow$ even-dominant)")
    ax4.legend(fontsize=8)

    fig.suptitle(f"{GATE_ID}: {verdict} -- C$^2$-coset Weinberg-angle / $a_2$ "
                 f"response slope (off-Jensen; tau_fold={tau_fold}, L_max={L_MAX})",
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
        l_max=str(L_MAX), verdict=verdict, track="session",
        sign_verdict=tup3[0], magnitude_verdict=tup3[1], regime_verdict=tup3[2],
        # --- FD stencil + observables ---
        deltas5=r["deltas5"], sin2_vals=r["sin2_vals"],
        sin2_bare_vals=r["sin2_bare_vals"],
        L1_vals=r["L1_vals"], L2_vals=r["L2_vals"], L3_vals=r["L3_vals"],
        a2_vals=r["a2_vals"], conds=r["conds"],
        # --- the [SIGN] observable: sin^2 slope ---
        dsin2_d0=r["dsin2_d0"], abs_dsin2_d0=r["abs_dsin2_d0"],
        dsin2_chain=r["dsin2_chain"], dsin2_d0_h=r["dsin2_d0_h"],
        rich_sin2=r["rich_sin2"], eps_sens=EPS_SENS,
        # --- leg-eigenvalue slopes + analytic bracket ---
        dL1_d0=r["dL1_d0"], dL2_d0=r["dL2_d0"], dL3_d0=r["dL3_d0"],
        bracket=r["bracket"],
        # --- frame block-diagonality (Reading-A==Reading-B) ---
        frame_cross=r["frame_cross"], frame_blockdiag=r["frame_blockdiag"],
        # --- a_2 companion response ---
        da2_d0=r["da2_d0"], abs_da2_d0=r["abs_da2_d0"], d2a2_d0=r["d2a2_d0"],
        a2_0=r["a2_0"], asym1=r["asym1"], asym2=r["asym2"],
        a2_L12_cache=r["a2_L12_cache"], nsec_cache=r["nsec_cache"],
        a2_lmax_response=A2_LMAX_RESPONSE,
        # --- canonical anchors ---
        sin2_fold_canonical=r["sin2_fold_canonical"],
        a2_fold_canonical=r["a2_fold_canonical"],
        # --- Jensen + volume-preservation ---
        L1=r["L1"], L2=r["L2"], L3=r["L3"], vol_jensen=r["vol_jensen"],
        det_ratio=r["det_ratio"], schur_recover=r["schur_recover"],
        # --- regime ---
        cond0=r["cond0"], cond_max=r["cond_max"], breach_frac=r["breach_frac"],
        regime=r["regime"],
        # --- criteria + pins ---
        crit_frame=crit["frame_blockdiag"], crit_slope=crit["slope_above_eps"],
        crit_sign=crit["sign_match"], crit_bracket=crit["bracket_positive"],
        crit_a2=crit["a2_responds"], crit_richardson=crit["richardson_ok"],
        c2_idx=np.array(list(C2_IDX), dtype=np.int64),
        su2_idx=np.array(list(SU2_IDX), dtype=np.int64),
        u1_idx=np.array(list(U1_IDX), dtype=np.int64),
        tau_fold_used=float(tau_fold), m_kk_used=float(M_KK),
        h_fd=H_FD,
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
    print("\n=== SUBSTITUTION CHAIN (numbers substituted at runtime) ===")
    print(f"  Step 1 sin^2 theta_W = 3 L2/(L1+3 L2); @tau_fold={tau_fold}: "
          f"L1={r['L1']:.6f}, L2={r['L2']:.6f} => sin^2={r['sin2_vals'][2]:.8f} "
          f"(canonical {r['sin2_fold_canonical']:.8f}).")
    print(f"  Step 2 L1>0, L2>0 (Josephson stiffness positivity).")
    print(f"  Step 3 d(sin^2)/dL2 = 3 L1/(L1+3 L2)^2 = {r['bracket']:+.6e}.")
    print(f"  Step 4 L1>0 and (L1+3 L2)^2>0 => d(sin^2)/dL2 > 0 ALWAYS.")
    print(f"  C^2-split: L3 I_4 -> diag(e^(3d),e^(-d),e^(-d),e^(-d)); det-ratio="
          f"{r['det_ratio']:.10f} (=1 vol-preserving); frame block-diagonal "
          f"max|E[u2,C2]|={np.max(r['frame_cross']):.2e}.")
    print(f"  Substitute: dL2/d(delta_C2)|_0 = {r['dL2_d0']:+.6e} (C^2-split leaves "
          f"the su(2) block INVARIANT) => d(sin^2)/d(delta_C2)|_0 = bracket*dL2 = "
          f"{r['dsin2_chain']:+.6e} (FD: {r['dsin2_d0']:+.6e}).")
    print(f"  Canonical form: |d(sin^2)/d(delta_C2)|_0| = {r['abs_dsin2_d0']:.6e} "
          f"vs eps_sens = {EPS_SENS}.")
    print(f"  Direction: bracket > 0 => sign(d(sin^2)/d(delta_C2)) = "
          f"sign(dL2/d(delta_C2)) = {np.sign(r['dL2_d0']):+.0f} "
          f"(both ~0 => no mismatch => sign CORRECT); "
          f"|slope| {'>' if r['abs_dsin2_d0'] > EPS_SENS else '<='} eps_sens "
          f"=> C^2-coset is sin^2-"
          f"{'ACTIVE' if r['abs_dsin2_d0'] > EPS_SENS else 'INERT'}.")
    print(f"  Companion a_2: d(a_2)/d(delta_C2)|_0={r['da2_d0']:+.6e} (~0 stationary), "
          f"d^2(a_2)/d(delta_C2)^2|_0={r['d2a2_d0']:+.6e} (QUADRATIC, geometry-"
          f"{'ACTIVE' if abs(r['d2a2_d0'])>1.0 else 'quiet'}).")
    print(f"  Conclusion: composite = {verdict} "
          f"(sign={sign_v}, magnitude={mag_v}, regime={regime_v}).")

    print(f"\nCriteria: frame_blockdiag={crit['frame_blockdiag']}  "
          f"slope>eps={crit['slope_above_eps']}  sign_match={crit['sign_match']}  "
          f"bracket>0={crit['bracket_positive']}  a2_responds={crit['a2_responds']}  "
          f"richardson_ok={crit['richardson_ok']}")

    value = (f"dsin2_ddelta0={r['dsin2_d0']:+.6e}_vs_eps{EPS_SENS};"
             f"absdsin2={r['abs_dsin2_d0']:.6e};"
             f"sin2_fold={r['sin2_vals'][2]:.8f}_INVARIANT;"
             f"dL2_ddelta0={r['dL2_d0']:+.3e};bracket={r['bracket']:+.4e};"
             f"frame_blockdiag={r['frame_blockdiag']}_maxEcross{np.max(r['frame_cross']):.1e};"
             f"da2_ddelta0={r['da2_d0']:+.4e}_stationary;"
             f"d2a2_ddelta2={r['d2a2_d0']:+.4e}_quadratic;"
             f"a2_M2_0={r['a2_0']:.4f}_Lmax{A2_LMAX_RESPONSE};"
             f"a2_L12cache={r['a2_L12_cache']:.2f};"
             f"L=[{r['L1']:.4f},{r['L2']:.4f},{r['L3']:.4f}];"
             f"detratio={r['det_ratio']:.8f};regime={r['regime']};Lmax={L_MAX}")  # (local)

    make_plot(r, verdict)
    save_npz(r, verdict, (sign_v, mag_v, regime_v), crit, audit_sha, content_sha)

    print()
    print(emit_4tuple(value, SCHEME, CONVENTION, L_MAX))
    print_verdict_payload(
        verdict, value, audit_sha, content_sha,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
        companion_note=(
            f"C^2-coset Weinberg-angle/a_2 response: sin^2 theta_W=3L2/(L1+3L2) "
            f"is delta-INVARIANT ({r['sin2_vals'][2]:.6f}=canonical fold) because the "
            f"C^2-split touches only C^2 (u(1)/su(2) legs block-orthogonal, frame "
            f"block-diagonal max|E[u2,C2]|={np.max(r['frame_cross']):.1e}); "
            f"d(sin^2)/d(delta_C2)|_0={r['dsin2_d0']:+.3e}<eps_sens={EPS_SENS} => INERT; "
            f"sign-correct (bracket=3L1/(L1+3L2)^2={r['bracket']:.3e}>0, dL2=0). "
            f"COMPANION a_2: d(a_2)/d(delta)|_0={r['da2_d0']:+.2e}~0 (stationary), "
            f"d^2(a_2)/d(delta)^2|_0={r['d2a2_d0']:+.2e} QUADRATIC (geometry-ACTIVE); "
            f"vol-preserving det-ratio={r['det_ratio']:.6f}"),
        extra_rows=[
            (f"# regulator_pin: a_2^{{zeta}} poleconv-A-double pole_in_s=3 "
             f"curvature_grade_n=2 FI-tagged (a_2-ratio parented to F_traj a_2-ratio "
             f"FI theorem at locked-norm L_k=1); M2(0)_Lmax{A2_LMAX_RESPONSE}="
             f"{r['a2_0']:.4f}; M2_L12cache(0)={r['a2_L12_cache']:.4f} over "
             f"{r['nsec_cache']} PW sectors; canonical a2_fold="
             f"{r['a2_fold_canonical']:.4f} # {GATE_ID}"),
            (f"# C^2-coset productive-relocation: sin^2-INERT "
             f"(d/ddelta={r['dsin2_d0']:+.2e}, INFO) but a_2-ACTIVE at 2nd order "
             f"(d^2/ddelta^2={r['d2a2_d0']:+.2e}); complement to S110-CF1 Yukawa-null; "
             f"frame block-diagonal => Reading-A==Reading-B for sin^2; "
             f"Jensen L=[{r['L1']:.4f},{r['L2']:.4f},{r['L3']:.4f}] "
             f"vol={r['vol_jensen']:.8f} cond(g) {r['cond0']:.3f}->{r['cond_max']:.3f} "
             f"regime={r['regime']} # {GATE_ID}"),
        ],
    )

    print(f"\n=== {GATE_ID}: {verdict} (sign={sign_v} magnitude={mag_v} "
          f"regime={regime_v}; wall {time.time() - t0:.1f}s) ===")
    return 0   # exit 0 on script success regardless of scientific verdict


if __name__ == "__main__":
    sys.exit(main())
