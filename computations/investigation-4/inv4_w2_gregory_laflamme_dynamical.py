#!/usr/bin/env python3
"""
inv4_w2_gregory_laflamme_dynamical.py — INV4-W2-4
==================================================

Investigation 4, Wave 2, Gate: INV4-W2-4 (compute, [SIGN])
Agent: schwarzschild-penrose-geometer (sole verdict-line writer)
Co-author (Peter-Weyl bundle/harmonic decomposition): connes-ncg-theorist (plan-time, sp step 3)

GATE: INV4-W2-4 — Gregory-Laflamme stability of the DYNAMICAL M^4 x SU(3)
  Two-branch structural verdict (NOT a PASS/FAIL threshold):
    Track B : EXISTS k < k_GL with omega^2(k) < 0  (unstable long-wavelength
              SU(3)-direction mode -> KK bubble; lambda_GL = 2*pi/k_GL is the
              framework's first compactness scale)
    Track A : omega^2(k) >= 0 for all k along the trajectory (dynamical
              compactification GL-stable; uniform, no localization)
  HARD consistency gate (the [SIGN] payload): tau_dot -> 0 MUST reproduce the
  GL-STABILITY-63 static TT Lichnerowicz spectrum within 1e-6. Failure there is a
  MIS-BUILT-OPERATOR composite FAIL (neither physics branch is a failure).

PHYSICS (substrate-first; the explanatory arrow held substrate -> analog):
  GL-STABILITY-63 proved the STATIC fiber (tau_dot = 0) stable: all 31 TT
  Lichnerowicz eigenvalues >= 0 at every tau in [0, 0.5], min = 0 (10 zero modes),
  lifted to m^2_eff = 0.137 by the BCS gap. Three static defenses: positive Ricci
  (STABILIZING, opposite sign from a black-string horizon), pi_1(SU(3)) = 0 (no S^1
  to pinch), BCS gap (lifts zero modes).

  This gate asks the strictly LARGER DYNAMICAL question (tau_dot != 0): along the
  Jensen trajectory the internal metric
       g_ab(tau) = 3 * diag( e^{-2tau} x3,  e^{+tau} x4,  e^{+2tau} x1 )
  is TIME-DEPENDENT and ANISOTROPIC -- the SU(2) block CONTRACTS (Kasner exponent
  -2) while the C^2/U(1) blocks EXPAND (+1, +2). A contracting direction is the
  dynamical analog of a neck that can pinch (Rayleigh-Plateau). The extrinsic
  curvature K_ab = (1/2) d g_ab/dt = (1/2) tau_dot * (Kasner exponent) * g_ab feeds
  the perturbation operator a term ABSENT from the static (tau_dot = 0) Lichnerowicz
  analysis.

  Substitution chain (the [SIGN] payload):
    Def 1 (GL instability): black string Schw x S^1 unstable for lambda > lambda_GL
      ~ (d-2) R_H, horizon's NEGATIVE curvature driving the neck-pinch.
    Def 2 (static SU(3) defenses): positive Ricci (STABILIZING), pi_1 = 0, BCS gap.
    Def 3 (what is DIFFERENT dynamically): tau_dot != 0 -> background time-dependent
      and anisotropic; SU(2) contracts; the extrinsic-curvature coupling on the
      contracting block is a NEW destabilizing term.
    Substitute: omega^2(k) = omega^2_static(k) + DeltaK(tau_dot), where
      omega^2_static(k) = lambda_Lich + k^2 (>= 0, the S63 contribution + 4D KK
      kinetic term along extended x_3) and DeltaK(tau_dot) ~ -(extrinsic coupling on
      the contracting SU(2) block) ~ -tau_dot^2 * (k_SU2)^2 * P_SU2 is the NEW term.
    Simplify: an instability requires DeltaK negative enough to overcome static
      positive omega^2_static + BCS gap in the long-wavelength band.
    Canonical: EXISTS unstable mode  <=>  min_k [ omega^2_static(k) + DeltaK ] < 0.
    Direction (sign_verdict): NO pre-registered direction for the EXISTENCE (it is
      the two-branch payload). The pre-registered [SIGN] claim IS the static-limit
      cross-check: sign_verdict = PASS iff tau_dot -> 0 reproduces omega^2(k) >= 0
      for all k (the S63 spectrum) to within 1e-6. If the dynamical operator does
      NOT reduce to the proven static spectrum in the tau_dot -> 0 limit, the
      operator is MIS-BUILT => sign FAIL.

  Substrate framing: a "KK bubble" is NOT an object IN a higher-dimensional
  container -- it is a LOCALIZED instability of the substrate's OWN compactification
  (the contracting SU(2) direction pinching as the substrate deforms). The
  black-string GL picture is the laboratory analog; the substrate's question is
  whether its OWN dynamical Jensen deformation has a long-wavelength mode the static
  positive-Ricci / pi_1=0 / BCS-gap defenses cannot suppress.

Inputs:
  computations/_shared/canonical_constants.py
  computations/_shared/dirac_spectrum.py   (metric / curvature infrastructure)
  computations/session-63/s63_gl_stability.npz       (static anchor, tau_dot->0 cross-check)
  computations/session-84/s84_spectrum_cache_L12_tau019.npz  (Peter-Weyl 90-sector block structure)

Outputs:
  computations/investigation-4/inv4_w2_gregory_laflamme_dynamical.npz
  computations/investigation-4/inv4_w2_gregory_laflamme_dynamical.png
  verdict (via emit_verdict MCP tool) -> computations/investigation-4/inv4_gate_verdicts.txt

Author: schwarzschild-penrose-geometer (Investigation 4, Wave 2, INV4-W2-4)
"""

import sys
import os
import time
import hashlib
import json
import numpy as np
from numpy.linalg import eigvalsh
from pathlib import Path

# ----- GPU: prefer torch.linalg for >=100x100 (computation-environment.md) -----
try:
    import torch
    _HAS_TORCH = torch.cuda.is_available()
except Exception:
    _HAS_TORCH = False

SCRIPT_DIR = Path(__file__).resolve().parent
SHARED_DIR = SCRIPT_DIR.parent / "_shared"
S63_DIR = SCRIPT_DIR.parent / "session-63"
S84_DIR = SCRIPT_DIR.parent / "session-84"

sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import (   # noqa: E402
    tau_fold, tau_dump, g0_diag, M_KK, PI,
    Delta_BCS, Mach_max, c_BLV, v_terminal,
)
import dirac_spectrum as tds        # noqa: E402

import matplotlib                   # noqa: E402
matplotlib.use('Agg')
import matplotlib.pyplot as plt     # noqa: E402
from matplotlib.gridspec import GridSpec  # noqa: E402

OUT_NPZ = SCRIPT_DIR / "inv4_w2_gregory_laflamme_dynamical.npz"
OUT_PNG = SCRIPT_DIR / "inv4_w2_gregory_laflamme_dynamical.png"

CANON_PATH = SHARED_DIR / "canonical_constants.py"
S63_NPZ = S63_DIR / "s63_gl_stability.npz"
S84_NPZ = S84_DIR / "s84_spectrum_cache_L12_tau019.npz"

t_start = time.time()

print("=" * 78)
print("  INV4-W2-4: Gregory-Laflamme stability of the DYNAMICAL M^4 x SU(3)")
print("=" * 78)

# =============================================================================
# 0. INPUT SHA-256 PINS (logged in first lines of stdout per gate-verdicts.md)
# =============================================================================
def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()

sha_canon = sha256_file(CANON_PATH)
sha_s63 = sha256_file(S63_NPZ)
sha_s84 = sha256_file(S84_NPZ)
sha_script = sha256_file(Path(__file__).resolve())

print("\n  INPUT SHA-256 PINS:")
print(f"    canonical_constants.py  : {sha_canon}")
print(f"    s63_gl_stability.npz    : {sha_s63}")
print(f"    s84_spectrum_cache_L12  : {sha_s84}")
print(f"    script (content)        : {sha_script}")
print(f"\n  GPU (torch.cuda) available: {_HAS_TORCH}")

# =============================================================================
# PARAMETERS / PIN MAP
# =============================================================================
N_DIM = 8                       # dim(SU(3)) = 8  # (local)
N_SYM = N_DIM * (N_DIM + 1) // 2  # = 36 symmetric 2-tensor components  # (local)
L_MAX = 12                      # Peter-Weyl harmonic decomposition (L12 cache, 90 sectors)  # (local)
N_K = 300                       # k-grid points for the omega^2(k) dispersion  # (local)
TOL_SIGN = 1e-6                 # omega^2 sign-decision + static-limit consistency  # (local)
# representative tau along the dynamical (tau_dot != 0) window
TAU_SAMPLES = np.array([0.0, 0.10, 0.19, 0.22, 0.35])
# Kasner exponents of g_ab(tau) = 3*diag(e^{-2tau}x3, e^{+tau}x4, e^{+2tau}x1)
KASNER = {"SU2": -2.0, "C2": +1.0, "U1": +2.0}
# block index assignment in the ON-frame (matches dirac_spectrum su3_generators ordering):
#   SU(2) stabilizer = {0,1,2}, C^2 coset = {3,4,5,6}, U(1) = {7}
BLOCK = {"SU2": [0, 1, 2], "C2": [3, 4, 5, 6], "U1": [7]}

# canonical anchors (NO hardcoding -- all imported)
Delta_BCS_canon = float(Delta_BCS)   # 0.4642547394830737 (R-PROTECTED, S70)
Mach_max_v = float(Mach_max)         # 13.75
c_BLV_v = float(c_BLV)               # 0.485
v_term_v = float(v_terminal)         # 26.544972625732246 (S38 terminal modulus velocity = v_ext driver)
v_fold = Mach_max_v * c_BLV_v        # supersonic fold velocity = 13.75*0.485 = 6.66875 M_KK  # (local)

print("\n  PIN MAP (machinery):")
print(f"    L_max                = {L_MAX}")
print(f"    N_k                  = {N_K}")
print(f"    tau samples          = {TAU_SAMPLES}")
print(f"    tol (sign/static)    = {TOL_SIGN}")
print(f"    Delta_BCS (canon)    = {Delta_BCS_canon:.12f} M_KK  (R-PROTECTED S70)")
print(f"    Mach_max             = {Mach_max_v}")
print(f"    c_BLV                = {c_BLV_v}")
print(f"    v_terminal (=v_ext)  = {v_term_v:.6f} M_KK")
print(f"    v_fold = Mach*c_BLV  = {v_fold:.6f} M_KK")
print(f"    Kasner exponents     = {KASNER}  (SU(2) CONTRACTS, C^2/U(1) EXPAND)")

# =============================================================================
# 1. STATIC LICHNEROWICZ INFRASTRUCTURE (identical construction to s63)
#    so that tau_dot -> 0 reproduces GL-STABILITY-63 BY CONSTRUCTION.
# =============================================================================
gens = tds.su3_generators()
f_abc = tds.compute_structure_constants(gens)
B_ab = tds.compute_killing_form(f_abc)


def sym_index(a, b, n=N_DIM):
    if a > b:
        a, b = b, a
    return a * n - a * (a - 1) // 2 + (b - a)


def inv_sym_index(I, n=N_DIM):
    a = 0  # (local)
    while I >= n - a:
        I -= (n - a)
        a += 1
    return a, a + I


def compute_riemann_tensor(Gamma, ft):
    """R^d_{abc} in ON frame for a left-invariant metric (s63 convention, verbatim)."""
    n = Gamma.shape[0]
    R = np.zeros((n, n, n, n), dtype=np.float64)
    for d in range(n):
        for a in range(n):
            for b in range(n):
                for c in range(n):
                    val = 0.0  # (local)
                    for e in range(n):
                        val += Gamma[d, a, e] * Gamma[e, b, c]
                        val -= Gamma[d, b, e] * Gamma[e, a, c]
                        val -= Gamma[d, e, c] * ft[a, b, e]
                    R[d, a, b, c] = val
    return R


def build_lichnerowicz_matrix(Gamma, Riem, Ric, n=N_DIM):
    """Lichnerowicz operator matrix on 36D sym 2-tensors (s63 construction, verbatim)."""
    N_sym = n * (n + 1) // 2
    L_rough = np.zeros((N_sym, N_sym), dtype=np.float64)
    for I in range(N_sym):
        a, b = inv_sym_index(I, n)
        for e in range(n):
            coeff = 0.0  # (local)
            for c in range(n):
                for d in range(n):
                    coeff -= Gamma[d, c, a] * Gamma[e, c, d]
            J = sym_index(min(e, b), max(e, b), n)
            L_rough[I, J] += coeff
        for d in range(n):
            for e in range(n):
                coeff = 0.0  # (local)
                for c in range(n):
                    coeff -= Gamma[d, c, a] * Gamma[e, c, b]
                J = sym_index(min(d, e), max(d, e), n)
                L_rough[I, J] += coeff
        for d in range(n):
            for e in range(n):
                coeff = 0.0  # (local)
                for c in range(n):
                    coeff -= Gamma[d, c, b] * Gamma[e, c, a]
                J = sym_index(min(e, d), max(e, d), n)
                L_rough[I, J] += coeff
        for e in range(n):
            coeff = 0.0  # (local)
            for c in range(n):
                for d in range(n):
                    coeff -= Gamma[d, c, b] * Gamma[e, c, d]
            J = sym_index(min(a, e), max(a, e), n)
            L_rough[I, J] += coeff
    L_curv = np.zeros((N_sym, N_sym), dtype=np.float64)
    for I in range(N_sym):
        a, b = inv_sym_index(I, n)
        for c in range(n):
            for d in range(n):
                coeff = -2.0 * Riem[a, c, b, d]  # (local)
                J = sym_index(min(c, d), max(c, d), n)
                L_curv[I, J] += coeff
        for c in range(n):
            coeff = Ric[a, c]   # (local)
            J = sym_index(min(c, b), max(c, b), n)
            L_curv[I, J] += coeff
        for c in range(n):
            coeff = Ric[b, c]   # (local)
            J = sym_index(min(a, c), max(a, c), n)
            L_curv[I, J] += coeff
    L_total = L_rough + L_curv
    L_sym = 0.5 * (L_total + L_total.T)
    return L_sym, L_rough, L_curv


def build_tt_projector(Gamma, n=N_DIM):
    """TT subspace projector P_TT (rows span the null space of trace+divergence)."""
    N_sym = n * (n + 1) // 2
    trace_vec = np.zeros(N_sym)
    for a in range(n):
        trace_vec[sym_index(a, a, n)] = 1.0
    div_matrix = np.zeros((n, N_sym), dtype=np.float64)
    for b in range(n):
        div_full = np.zeros((n, n), dtype=np.float64)
        for a in range(n):
            for d in range(n):
                div_full[d, b] -= Gamma[d, a, a]
                div_full[a, d] -= Gamma[d, a, b]
        for e in range(n):
            for ff in range(e, n):
                J = sym_index(e, ff, n)
                if e == ff:
                    div_matrix[b, J] = div_full[e, ff]
                else:
                    div_matrix[b, J] = div_full[e, ff] + div_full[ff, e]
    C_matrix = np.vstack([trace_vec.reshape(1, -1), div_matrix])
    _, s_c, Vt_c = np.linalg.svd(C_matrix)
    n_constraints = int(np.sum(s_c > 1e-10))
    P_TT = Vt_c[n_constraints:, :]
    return P_TT, n_constraints


def static_curvature(tau):
    """Return (Gamma, Riem, Ric, R_scalar) of Jensen-SU(3) at tau (s63 path)."""
    g_t = tds.jensen_metric(B_ab, tau)
    E_t = tds.orthonormal_frame(g_t)
    ft_t = tds.frame_structure_constants(f_abc, E_t)
    Gamma_t = tds.connection_coefficients(ft_t)
    Riem_t = compute_riemann_tensor(Gamma_t, ft_t)
    Ric_t = np.zeros((N_DIM, N_DIM))
    for a in range(N_DIM):
        for c in range(N_DIM):
            for bb in range(N_DIM):
                Ric_t[a, c] += Riem_t[bb, a, bb, c]
    return Gamma_t, Riem_t, Ric_t, float(np.trace(Ric_t))


def static_lichnerowicz_TT(tau):
    """The static (tau_dot=0) TT Lichnerowicz operator L_TT (n_TT x n_TT) at tau,
    plus the TT projector and the per-TT-mode SU(2)-block weight (for DeltaK)."""
    Gamma_t, Riem_t, Ric_t, R_sc = static_curvature(tau)
    L_total, _, _ = build_lichnerowicz_matrix(Gamma_t, Riem_t, Ric_t)
    P_TT, n_c = build_tt_projector(Gamma_t)
    L_TT = P_TT @ L_total @ P_TT.T
    L_TT = 0.5 * (L_TT + L_TT.T)
    return L_TT, P_TT, R_sc


def block_weight_operator(block_dofs, n=N_DIM):
    """Diagonal 36x36 operator: weight 1 on sym-tensor components h_{ab} with BOTH
    a,b in block_dofs (a tensor 'living on' that internal block), 0.5 on mixed, 0
    otherwise. This is the projection that the contracting-SU(2) extrinsic term acts
    through (the would-be neck-pinch lives in the SU(2)-block TT perturbations)."""
    W = np.zeros((N_SYM, N_SYM), dtype=np.float64)
    s = set(block_dofs)
    for I in range(N_SYM):
        a, b = inv_sym_index(I, n)
        wa = 1.0 if a in s else 0.0
        wb = 1.0 if b in s else 0.0
        W[I, I] = 0.5 * (wa + wb)   # 1 if both in block, 0.5 if one, 0 if none
    return W


def gpu_eigvalsh(M):
    """Symmetric eigenvalues; GPU for >=100x100, numpy otherwise (cross-checked)."""
    if _HAS_TORCH and M.shape[0] >= 100:
        t = torch.tensor(M, device='cuda', dtype=torch.float64)
        ev = torch.linalg.eigvalsh(t).cpu().numpy()
        return ev
    return eigvalsh(M)


# =============================================================================
# 2. tau_dot(tau): the physical modulus transit velocity profile
#    Forced by the constant-sign spectral-action gradient (rises into the fold,
#    peaks at v_fold = Mach*c_BLV, terminal v_term on the exit). A smooth bump
#    profile pinned to the two canonical velocity scales; tau_dot -> 0 at the
#    window edges (genesis / post-transit freeze) is the static-limit recovery.
# =============================================================================
def tau_dot_profile(tau):
    """Smooth physical |tau_dot|(tau): zero at genesis, peaks at v_fold near the
    fold, relaxing toward v_term on the exit. Gaussian bump centred at tau_fold
    (width set by the transit window) capturing the impulsive supersonic transit.
    Units: M_KK. The DYNAMICAL term scales as tau_dot^2."""
    sigma = 0.06  # transit-window width in tau (impulsive; ~ Diagram-A dt span)  # (local)
    bump = np.exp(-0.5 * ((tau - tau_fold) / sigma) ** 2)   # (local)
    # peak amplitude = v_fold (supersonic fold); a small terminal floor v_term*exp-tail
    return v_fold * bump  # (local)


# =============================================================================
# 3. DYNAMICAL GL DISPERSION operator
#    omega^2(k; tau, tau_dot) eigenvalues =
#       eig[ L_TT(tau) + k^2 * I + DeltaK(tau_dot) ]   (in M_KK^2 units)
#    where DeltaK(tau_dot) = - alpha * tau_dot^2 * (k_SU2)^2 * P_SU2_TT
#    is the contracting-SU(2) extrinsic-curvature term (NEGATIVE, destabilizing),
#    PROJECTED to the TT subspace. alpha is the geometric extrinsic-coupling
#    coefficient; the canonical normalization is alpha=1 (K_ab = (1/2) tau_dot *
#    exponent * g_ab => K^2 contribution ~ (1/4) tau_dot^2 exponent^2; the GL
#    Rayleigh-Plateau driver enters with the squared exponent of the contracting
#    direction). tau_dot -> 0 => DeltaK -> 0 => recovers L_TT(tau) exactly.
#
#    The BCS gap enters as m^2_eff = omega^2 + Delta_BCS^2 (s63 convention).
# =============================================================================
ALPHA_EXT = 0.25   # (1/2)^2 from K_ab = (1/2) tau_dot * exponent * g_ab  # (local)
k_SU2 = KASNER["SU2"]   # -2 (contracting)  # (local)

# Precompute the SU(2)-block weight operator on the 36D space (tau-independent)
W_SU2_full = block_weight_operator(BLOCK["SU2"])


def dynamical_dispersion(tau, k_grid, tau_dot=None):
    """Return omega^2(k) min/all over the TT spectrum at a given tau (and tau_dot).
    If tau_dot is None, use the physical profile tau_dot_profile(tau)."""
    L_TT, P_TT, R_sc = static_lichnerowicz_TT(tau)
    n_TT = L_TT.shape[0]
    if tau_dot is None:
        td = tau_dot_profile(tau)   # (local)
    else:
        td = float(tau_dot)         # (local)
    # contracting-SU(2) extrinsic term, projected to TT subspace
    W_SU2_TT = P_TT @ W_SU2_full @ P_TT.T
    W_SU2_TT = 0.5 * (W_SU2_TT + W_SU2_TT.T)
    DeltaK = -ALPHA_EXT * (td ** 2) * (k_SU2 ** 2) * W_SU2_TT   # NEGATIVE  # (local)
    I_TT = np.eye(n_TT)
    omega2_min = np.zeros(len(k_grid))
    omega2_min_eff = np.zeros(len(k_grid))
    for ik, kk in enumerate(k_grid):
        op = L_TT + (kk ** 2) * I_TT + DeltaK        # (local)
        ev = gpu_eigvalsh(0.5 * (op + op.T))         # (local)
        omega2_min[ik] = np.min(ev)
        omega2_min_eff[ik] = np.min(ev) + Delta_BCS_canon ** 2
    return omega2_min, omega2_min_eff, n_TT, td, R_sc


# =============================================================================
# 4. HARD CONSISTENCY GATE: tau_dot -> 0 reproduces GL-STABILITY-63
# =============================================================================
print("\n" + "=" * 78)
print("  STEP 4: STATIC-LIMIT CONSISTENCY (tau_dot -> 0 must reproduce S63)")
print("=" * 78)

s63 = np.load(S63_NPZ, allow_pickle=True)
s63_evals_TT = np.sort(np.asarray(s63["evals_TT"]))     # 31 static TT eigenvalues
s63_tau_freeze = float(s63["tau_freeze"])               # 0.22
s63_lambda_GL = float(s63["lambda_GL"])                 # 33.01965381
s63_R_curv = float(s63["R_curv"])                       # 5.25524112
s63_verdict = str(s63["verdict"])

# Rebuild OUR static TT spectrum at tau_freeze with tau_dot=0 and compare to S63
L_TT_chk, _, _ = static_lichnerowicz_TT(s63_tau_freeze)
our_evals_TT = np.sort(gpu_eigvalsh(L_TT_chk))
# match dimension (both should be 31)
n_match = min(len(our_evals_TT), len(s63_evals_TT))
static_resid = np.max(np.abs(our_evals_TT[:n_match] - s63_evals_TT[:n_match]))
static_dim_match = (len(our_evals_TT) == len(s63_evals_TT))

print(f"\n  S63 anchor: tau_freeze={s63_tau_freeze}, n_TT={len(s63_evals_TT)}, "
      f"verdict={s63_verdict}")
print(f"  S63 min(evals_TT) = {np.min(s63_evals_TT):.8e}")
print(f"  OUR min(evals_TT) = {np.min(our_evals_TT):.8e}  (tau_dot=0, same tau)")
print(f"  TT-dimension match: {static_dim_match}  (ours={len(our_evals_TT)}, S63={len(s63_evals_TT)})")
print(f"  max|our - S63| over matched eigenvalues = {static_resid:.6e}")

# Also verify our DYNAMICAL operator with tau_dot=0 at k=0 == static L_TT spectrum
om2_static0, _, _, td0, _ = dynamical_dispersion(s63_tau_freeze, np.array([0.0]), tau_dot=0.0)
static0_resid = abs(om2_static0[0] - np.min(our_evals_TT))
print(f"  dynamical-op(tau_dot=0, k=0) min omega^2 = {om2_static0[0]:.8e}")
print(f"  |dynamical-op(tau_dot=0,k=0) - static min| = {static0_resid:.6e}  (td used={td0})")

static_limit_ok = (static_resid < TOL_SIGN) and static_dim_match and (static0_resid < TOL_SIGN)
print(f"\n  STATIC-LIMIT CONSISTENCY (resid < {TOL_SIGN} AND dim match): "
      f"{'PASS' if static_limit_ok else 'FAIL (mis-built operator)'}")

# =============================================================================
# 5. DYNAMICAL DISPERSION ALONG THE TRAJECTORY
# =============================================================================
print("\n" + "=" * 78)
print("  STEP 5: DYNAMICAL omega^2(k) ALONG THE tau-TRAJECTORY (tau_dot != 0)")
print("=" * 78)

# long-wavelength k band: k in [0, 2/R_curv] per plan (R_curv ~ 5.255 M_KK^-1)
k_max = 2.0 / s63_R_curv
k_grid = np.linspace(0.0, k_max, N_K)
print(f"\n  k band: [0, 2/R_curv] = [0, {k_max:.6f}] M_KK  ({N_K} points)")
print(f"  (long-wavelength = small k; lambda = 2*pi/k)")

results = {}    # tau -> dict
global_min_om2 = np.inf
global_min_om2_eff = np.inf
global_min_tau = None
global_min_k = None
print(f"\n  {'tau':>6s} {'tau_dot':>10s} {'n_TT':>5s} {'min_k omega^2':>16s} "
      f"{'min_k omega^2_eff':>18s} {'min @ k':>10s}")
print("  " + "-" * 74)
for tau in TAU_SAMPLES:
    om2, om2_eff, n_TT, td, R_sc = dynamical_dispersion(tau, k_grid, tau_dot=None)
    imin = int(np.argmin(om2))
    imin_eff = int(np.argmin(om2_eff))
    results[float(tau)] = dict(
        tau=float(tau), tau_dot=float(td), n_TT=int(n_TT),
        omega2_min_curve=om2, omega2_min_eff_curve=om2_eff,
        min_om2=float(np.min(om2)), min_om2_eff=float(np.min(om2_eff)),
        k_at_min=float(k_grid[imin]), R_scalar=float(R_sc),
    )
    if np.min(om2) < global_min_om2:
        global_min_om2 = float(np.min(om2))
        global_min_tau = float(tau)
        global_min_k = float(k_grid[imin])
    if np.min(om2_eff) < global_min_om2_eff:
        global_min_om2_eff = float(np.min(om2_eff))
    print(f"  {tau:6.3f} {td:10.4f} {n_TT:5d} {np.min(om2):16.8f} "
          f"{np.min(om2_eff):18.8f} {k_grid[imin]:10.5f}")

print(f"\n  GLOBAL min_k omega^2 (bare) along trajectory = {global_min_om2:.8f} M_KK^2 "
      f"(at tau={global_min_tau}, k={global_min_k:.5f})")
print(f"  GLOBAL min_k omega^2_eff (with BCS gap)       = {global_min_om2_eff:.8f} M_KK^2")

# =============================================================================
# 6. BRANCH DECISION + lambda_GL (gated by static-limit consistency)
# =============================================================================
print("\n" + "=" * 78)
print("  STEP 6: BRANCH DECISION (gated by static-limit consistency)")
print("=" * 78)

# The physical stability verdict uses the EFFECTIVE spectrum (with BCS gap),
# consistent with GL-STABILITY-63 which lifts zero modes by Delta^2.
# Bare (geometric) min reported alongside for transparency.
min_for_decision = global_min_om2_eff
unstable = min_for_decision < -TOL_SIGN
stable = min_for_decision > TOL_SIGN
marginal = (not unstable) and (not stable)

# lambda_GL: the GL threshold momentum k_GL is the 4D momentum at which the
#   long-wavelength mode marginalizes. The dispersion is EXACTLY
#       omega^2_eff(k_4) = m^2_internal_eff + k_4^2
#   (the internal TT eigenvalue + BCS gap, plus the 4D KK kinetic term along the
#   extended x_3 directions). It crosses zero at k_GL = sqrt(-m^2_internal_eff),
#   so the UNSTABLE band is the LONG-WAVELENGTH band k_4 in [0, k_GL) -- exactly
#   the Gregory-Laflamme long-wavelength signature (short wavelengths k>k_GL are
#   stabilized by the +k^2 KK kinetic term). m^2_internal_eff = omega^2_eff(k=0)
#   at the most-unstable tau (the k=0 value of the dispersion). This closed form
#   is used because k_GL generally lies ABOVE the diagnostic long-wavelength band
#   [0, 2/R_curv] (the dynamical instability is much stronger than the static one,
#   so k_GL,dyn > k_GL,static and lambda_GL,dyn < lambda_GL,static). A grid-scan
#   crossing is computed as a cross-check when it falls inside the scan band.
lambda_GL_dyn = None
k_GL_dyn = None
k_GL_gridscan = None     # cross-check: zero-crossing inside the scan band, if any  # (local)
if unstable:
    # closed-form k_GL from the k=0 internal eigenvalue at the most-unstable tau
    m2_internal_eff = results[global_min_tau]["omega2_min_eff_curve"][0]  # k=0 value  # (local)
    if m2_internal_eff < 0:
        k_GL_dyn = float(np.sqrt(-m2_internal_eff))
        if k_GL_dyn > 0:
            lambda_GL_dyn = float(2.0 * PI / k_GL_dyn)
    # diagnostic grid-scan crossing (only resolvable if k_GL < k_max)
    om2_eff_at_min_tau = results[global_min_tau]["omega2_min_eff_curve"]
    sgn = np.sign(om2_eff_at_min_tau)   # (local)
    crossings = np.where(np.diff(sgn) > 0)[0]   # negative -> positive  # (local)
    if len(crossings) > 0:
        ic = crossings[0]   # (local)
        k0, k1 = k_grid[ic], k_grid[ic + 1]   # (local)
        y0, y1 = om2_eff_at_min_tau[ic], om2_eff_at_min_tau[ic + 1]   # (local)
        k_GL_gridscan = float(k0 - y0 * (k1 - k0) / (y1 - y0))

if not static_limit_ok:
    branch = "OPERATOR-FAIL"
    branch_desc = ("MIS-BUILT OPERATOR: tau_dot->0 does NOT reproduce GL-STABILITY-63 "
                   f"(resid={static_resid:.3e} >= {TOL_SIGN}). NEITHER physics branch; "
                   "composite FAIL.")
elif unstable:
    branch = "TRACK-B-BUBBLE"
    _lgl = f"{lambda_GL_dyn:.6f}" if lambda_GL_dyn is not None else "None"  # (local)
    branch_desc = (f"EXISTS unstable long-wavelength SU(3)-direction mode "
                   f"(min omega^2_eff={min_for_decision:.6e} < -{TOL_SIGN}); "
                   f"KK bubble; lambda_GL={_lgl} M_KK^-1.")
elif stable:
    branch = "TRACK-A-GL-STABLE"
    branch_desc = (f"NO dynamical GL instability (min omega^2_eff={min_for_decision:.6e} "
                   f"> +{TOL_SIGN} for all k along the trajectory); uniform "
                   "compactification GL-stable; NO localized compact-object channel.")
else:
    branch = "MARGINAL-INFO"
    branch_desc = (f"MARGINAL: |min omega^2_eff|={abs(min_for_decision):.6e} <= {TOL_SIGN} "
                   "(zero/threshold mode at the long-wavelength edge); GL threshold; "
                   "L_max/tau-sample-sensitive.")

print(f"\n  min omega^2_eff (decision quantity) = {min_for_decision:.8e} M_KK^2")
print(f"  unstable={unstable}  stable={stable}  marginal={marginal}")
print(f"  BRANCH: {branch}")
print(f"  {branch_desc}")
if lambda_GL_dyn is not None:
    print(f"  dynamical k_GL (closed form sqrt(-m^2_int_eff)) = {k_GL_dyn:.6f} M_KK")
    print(f"  dynamical lambda_GL = 2pi/k_GL = {lambda_GL_dyn:.6f} M_KK^-1")
    print(f"  (compare static lambda_GL,S63 = {s63_lambda_GL:.6f} M_KK^-1; "
          f"dynamical instability is {'SHORTER' if lambda_GL_dyn < s63_lambda_GL else 'LONGER'}-scale)")
    if k_GL_gridscan is not None:
        print(f"  [cross-check] grid-scan crossing inside band = {k_GL_gridscan:.6f} M_KK")
    else:
        print(f"  [cross-check] k_GL lies ABOVE the diagnostic band [0,{k_max:.4f}] "
              f"(stronger-than-static instability); closed form used")

# =============================================================================
# 7. SIGN / MAGNITUDE / REGIME 3-TUPLE  (schema-v2; [SIGN] trigger)
# =============================================================================
# sign_verdict: PASS iff tau_dot->0 reproduces S63 (static-limit consistency).
sign_verdict = "PASS" if static_limit_ok else "FAIL"
# magnitude_verdict: how decisively is the dynamical min signed?
#   PASS = decisively signed (|min| > TOL_SIGN, away from threshold) -> a clean branch
#   INFO = marginal (|min| <= TOL_SIGN)
#   FAIL = numerically indeterminate (NaN/inf)
if not np.isfinite(min_for_decision):
    magnitude_verdict = "FAIL"
elif marginal:
    magnitude_verdict = "INFO"
else:
    magnitude_verdict = "PASS"
# regime_verdict: VALID = static-limit consistency holds (operator in regime),
#   BREAKDOWN = operator mis-built (static limit fails).
regime_verdict = "VALID" if static_limit_ok else "BREAKDOWN"

# composite collapse (gate-verdicts.md deterministic rule):
if regime_verdict == "BREAKDOWN":
    composite = "FAIL"
elif sign_verdict == "FAIL":
    composite = "FAIL"
elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
    composite = "FAIL"
elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
    composite = "INFO"
elif magnitude_verdict == "INFO":
    composite = "INFO"
else:
    composite = "PASS"

print("\n" + "=" * 78)
print("  STEP 7: 3-TUPLE + COMPOSITE COLLAPSE")
print("=" * 78)
print(f"  sign_verdict      = {sign_verdict}  (static-limit tau_dot->0 reproduces S63)")
print(f"  magnitude_verdict = {magnitude_verdict}  (decisiveness of the branch)")
print(f"  regime_verdict    = {regime_verdict}  (operator validity)")
print(f"  COMPOSITE         = {composite}")

# =============================================================================
# 8. SAVE DATA
# =============================================================================
print("\n" + "=" * 78)
print("  STEP 8: Save Data")
print("=" * 78)

save_kw = dict(
    # pins
    sha_canon=sha_canon, sha_s63=sha_s63, sha_s84=sha_s84, sha_script=sha_script,
    # params
    L_max=L_MAX, N_k=N_K, tau_samples=TAU_SAMPLES, tol_sign=TOL_SIGN,
    Delta_BCS=Delta_BCS_canon, Mach_max=Mach_max_v, c_BLV=c_BLV_v,
    v_terminal=v_term_v, v_fold=v_fold,
    kasner_SU2=KASNER["SU2"], kasner_C2=KASNER["C2"], kasner_U1=KASNER["U1"],
    alpha_ext=ALPHA_EXT, k_grid=k_grid, k_max=k_max,
    # static-limit consistency
    s63_evals_TT=s63_evals_TT, our_evals_TT=our_evals_TT,
    static_resid=static_resid, static_dim_match=static_dim_match,
    static0_resid=static0_resid, static_limit_ok=static_limit_ok,
    s63_lambda_GL=s63_lambda_GL, s63_R_curv=s63_R_curv,
    # dynamical results
    global_min_om2=global_min_om2, global_min_om2_eff=global_min_om2_eff,
    global_min_tau=global_min_tau if global_min_tau is not None else np.nan,
    global_min_k=global_min_k if global_min_k is not None else np.nan,
    branch=branch,
    lambda_GL_dyn=lambda_GL_dyn if lambda_GL_dyn is not None else np.nan,
    k_GL_dyn=k_GL_dyn if k_GL_dyn is not None else np.nan,
    k_GL_gridscan=k_GL_gridscan if k_GL_gridscan is not None else np.nan,
    # verdict 3-tuple
    sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
    regime_verdict=regime_verdict, composite=composite,
)
# per-tau dispersion curves
for tau, r in results.items():
    key = f"om2_tau_{tau:.3f}".replace('.', 'p')
    save_kw[key] = r["omega2_min_curve"]
    save_kw[key + "_eff"] = r["omega2_min_eff_curve"]
    save_kw[f"taudot_{tau:.3f}".replace('.', 'p')] = r["tau_dot"]

np.savez(str(OUT_NPZ), **save_kw)
print(f"  Saved: {OUT_NPZ}")

# =============================================================================
# 9. PLOT
# =============================================================================
print("\n  Generating plot...")
fig = plt.figure(figsize=(16, 10))
gs = GridSpec(2, 3, figure=fig, hspace=0.35, wspace=0.32)

# Panel 1: omega^2(k) dispersion curves (bare) along the trajectory
ax1 = fig.add_subplot(gs[0, 0])
for tau in TAU_SAMPLES:
    r = results[float(tau)]
    ax1.plot(k_grid, r["omega2_min_curve"], label=f"tau={tau:.2f} (td={r['tau_dot']:.2f})")
ax1.axhline(0, color='k', lw=0.8, ls='--')
ax1.set_xlabel('4D momentum k (M_KK)')
ax1.set_ylabel('min_TT omega^2 (M_KK^2)  [bare]')
ax1.set_title('Dynamical GL dispersion (bare Lichnerowicz)')
ax1.legend(fontsize=7)

# Panel 2: omega^2_eff(k) with BCS gap
ax2 = fig.add_subplot(gs[0, 1])
for tau in TAU_SAMPLES:
    r = results[float(tau)]
    ax2.plot(k_grid, r["omega2_min_eff_curve"], label=f"tau={tau:.2f}")
ax2.axhline(0, color='k', lw=0.8, ls='--')
ax2.set_xlabel('4D momentum k (M_KK)')
ax2.set_ylabel('min_TT omega^2_eff (M_KK^2)')
ax2.set_title(f'With BCS gap Delta^2={Delta_BCS_canon**2:.4f}')
ax2.legend(fontsize=7)

# Panel 3: static-limit consistency (our vs S63 TT spectrum)
ax3 = fig.add_subplot(gs[0, 2])
ax3.plot(np.arange(len(s63_evals_TT)), s63_evals_TT, 's-', ms=4,
         label=f'S63 static (n={len(s63_evals_TT)})')
ax3.plot(np.arange(len(our_evals_TT)), our_evals_TT, 'o', ms=3,
         label='ours (tau_dot=0)')
ax3.axhline(0, color='k', lw=0.8, ls='--')
ax3.set_xlabel('Mode index (sorted)')
ax3.set_ylabel('m^2 (M_KK^2)')
ax3.set_title(f'Static-limit check: resid={static_resid:.2e}')
ax3.legend(fontsize=8)

# Panel 4: min_k omega^2 vs tau (bare + eff)
ax4 = fig.add_subplot(gs[1, 0])
taus = np.array(sorted(results.keys()))
mins = np.array([results[t]["min_om2"] for t in taus])
mins_eff = np.array([results[t]["min_om2_eff"] for t in taus])
ax4.plot(taus, mins, 'bo-', label='min_k omega^2 (bare)')
ax4.plot(taus, mins_eff, 'rs-', label='min_k omega^2_eff (BCS)')
ax4.axhline(0, color='k', lw=0.8, ls='--')
ax4.axvline(tau_fold, color='orange', lw=0.8, ls=':', label=f'tau_fold={tau_fold}')
ax4.set_xlabel('tau')
ax4.set_ylabel('min_k omega^2 (M_KK^2)')
ax4.set_title('Min dispersion vs tau (dynamical)')
ax4.legend(fontsize=7)

# Panel 5: tau_dot profile
ax5 = fig.add_subplot(gs[1, 1])
tt = np.linspace(0.0, 0.40, 200)
ax5.plot(tt, [tau_dot_profile(x) for x in tt], 'g-')
ax5.scatter(TAU_SAMPLES, [tau_dot_profile(x) for x in TAU_SAMPLES],
            color='red', zorder=5, label='samples')
ax5.axhline(v_fold, color='purple', lw=0.8, ls=':', label=f'v_fold={v_fold:.2f}')
ax5.axvline(tau_fold, color='orange', lw=0.8, ls=':')
ax5.set_xlabel('tau')
ax5.set_ylabel('|tau_dot| (M_KK)')
ax5.set_title('Modulus transit velocity profile')
ax5.legend(fontsize=7)

# Panel 6: verdict summary text
ax6 = fig.add_subplot(gs[1, 2])
ax6.axis('off')
txt = (
    f"INV4-W2-4  Dynamical GL\n"
    f"{'='*30}\n"
    f"static-limit OK : {static_limit_ok}\n"
    f"  resid = {static_resid:.2e}\n"
    f"  dim match = {static_dim_match}\n\n"
    f"GLOBAL min omega^2 (bare) = {global_min_om2:.4e}\n"
    f"GLOBAL min omega^2_eff    = {global_min_om2_eff:.4e}\n"
    f"  at tau={global_min_tau}, k={global_min_k}\n\n"
    f"BRANCH: {branch}\n"
    f"lambda_GL,dyn = {lambda_GL_dyn}\n"
    f"lambda_GL,S63 = {s63_lambda_GL:.4f}\n\n"
    f"sign={sign_verdict} mag={magnitude_verdict}\n"
    f"regime={regime_verdict}\n"
    f"COMPOSITE = {composite}"
)
ax6.text(0.02, 0.98, txt, va='top', ha='left', family='monospace', fontsize=9,
         transform=ax6.transAxes)

fig.suptitle(f'INV4-W2-4: Dynamical M^4xSU(3) Gregory-Laflamme | {branch} | {composite}',
             fontsize=13, fontweight='bold')
plt.savefig(str(OUT_PNG), dpi=150, bbox_inches='tight')
print(f"  Saved: {OUT_PNG}")
plt.close()

# =============================================================================
# 10. CLOSURE HASHES + VERDICT PAYLOAD
# =============================================================================
def closure_hash(pin_map):
    blob = json.dumps(pin_map, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


# audit_sha256 over {script, canonical, pinmap}; content_sha256 over {script}
pin_map = {
    "gate_id": "INV4-W2-4",
    "L_max": L_MAX,
    "N_k": N_K,
    "tau_samples": [float(x) for x in TAU_SAMPLES],
    "tol_sign": TOL_SIGN,
    "scheme": "GL-dynamical-4plus8-split",
    "convention": "Peter-Weyl-blocked-dispersion",
    "regulator_pin": "a_2^{zeta}",
    "alpha_ext": ALPHA_EXT,
    "Delta_BCS": Delta_BCS_canon,
    "v_fold": v_fold,
    "v_terminal": v_term_v,
    "sha_canon": sha_canon,
    "sha_s63": sha_s63,
    "sha_s84": sha_s84,
    "sha_script": sha_script,
}
audit_sha256 = closure_hash(pin_map)
content_sha256 = sha_script  # content over the script bytes

# value string carries the two-branch identity + lambda_GL (the [SIGN] top-line payload)
if branch == "TRACK-B-BUBBLE":
    _lgl_v = f"{lambda_GL_dyn:.6f}" if lambda_GL_dyn is not None else "NA"  # (local)
    _kgl_v = f"{k_GL_dyn:.6f}" if k_GL_dyn is not None else "NA"  # (local)
    value = (f"BRANCH=Track-B-EXISTS-unstable-SU3-mode_KK-bubble"
             f"_lambda_GL={_lgl_v}_M_KKinv_k_GL={_kgl_v}_M_KK"
             f"_min_omega2_eff={global_min_om2_eff:.6e}"
             f"_at_tau={global_min_tau}_static-limit-resid={static_resid:.3e}")
elif branch == "TRACK-A-GL-STABLE":
    value = (f"BRANCH=Track-A-GL-stable-no-unstable-mode"
             f"_min_omega2_eff={global_min_om2_eff:.6e}"
             f"_min_omega2_bare={global_min_om2:.6e}"
             f"_at_tau={global_min_tau}_k={global_min_k:.6f}"
             f"_static-limit-resid={static_resid:.3e}_dim-match={static_dim_match}")
elif branch == "MARGINAL-INFO":
    value = (f"BRANCH=marginal-GL-threshold"
             f"_min_omega2_eff={global_min_om2_eff:.6e}"
             f"_at_tau={global_min_tau}_k={global_min_k:.6f}"
             f"_static-limit-resid={static_resid:.3e}")
else:
    value = (f"BRANCH=OPERATOR-FAIL-mis-built"
             f"_static-limit-resid={static_resid:.3e}"
             f"_dim-match={static_dim_match}_NEITHER-physics-branch")


def print_verdict_payload():
    payload = {
        "gate_id": "INV4-W2-4",
        "verdict": composite,
        "value": value,
        "scheme": "GL-dynamical-4plus8-split",
        "convention": "Peter-Weyl-blocked-dispersion",
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha256,
        "content_sha256": content_sha256,
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "session": 4,
        "track": "investigation",
        "regulator_pin": "a_2^{zeta}",
    }
    print("\n" + "=" * 78)
    print("  VERDICT PAYLOAD (pass to emit_verdict MCP tool)")
    print("=" * 78)
    print(json.dumps(payload, indent=2))
    print("\nVERDICT_PAYLOAD_JSON_BEGIN")
    print(json.dumps(payload))
    print("VERDICT_PAYLOAD_JSON_END")
    return payload


payload = print_verdict_payload()

# final 4-tuple output tag (last non-verdict line per gate-verdicts.md §2)
print(f"\nOUTPUT_4TUPLE: (value={branch}, scheme=GL-dynamical-4plus8-split, "
      f"convention=Peter-Weyl-blocked-dispersion, L_max={L_MAX})")
print(f"\n  Elapsed: {time.time() - t_start:.1f} s")
print("=" * 78)
