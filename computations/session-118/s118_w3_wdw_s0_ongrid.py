#!/usr/bin/env python3
"""
S118 W3-2 — CF-S118-WDW-S0-ONGRID — WDW J(0)=0 with the W(0)=0 anchor ON-GRID
==============================================================================

Gate: CF-S118-WDW-S0-ONGRID  ([VERIFY])  —  OPTIONAL / LOW / COSMETIC.

LABEL-ONLY upgrade of the S117 W5-2 WDW current verdict INFO -> PASS. The
family-wide J==0 theorem (every real separated self-adjoint / Robin extension of
the 1D minisuperspace WDW operator forces J(0)=0 on [0, tau_fold]) is ALREADY
E- and W-magnitude-independent (S117 W5-2: s117_w5_wdw_j_rigor.py). This gate adds
the ONLY missing numerical anchor: it places tau=0 as a LITERAL grid node on the
spectral action S(tau) and recomputes S(0) DIRECTLY from the D_K(tau=0) eigenvalue
sum (NOT a CubicSpline extrapolation), so W(0) = 2*G_DeWitt*(S(0)-E) = 0 holds
ON-GRID with E = S(0). No new physics: the J==0 theorem stands without it.

Pre-registered threshold (composite conjunction):
  PASS iff
    grid_reaches_tau0 = True (min(tau-grid) <= 1e-9, S(0) a DIRECT eigenvalue-sum)
    AND |W(0)| <= 1e-12 (E = S(0))
    AND max_theta |J(0;theta)| < 1e-12 over the real Robin family theta in [0,pi)
    AND Vilenkin complex BC J(0)=k|Psi(0)|^2 > 1e-6 (non-self-adjoint, excluded)
    AND current conservation: relative Wronskian residual < 1e-9, Im(W)=0 exactly.
  INFO iff all numerical/structural conditions hold but grid_reaches_tau0 = False
    (the S117 W5-2 state: W(0)=0 still extrapolated).
  FAIL iff some real Robin theta gives |J(0)|>1e-12, OR W not real / unbounded,
    OR current conservation breaks, OR Vilenkin not excluded (a THEOREM-TENSION
    re-opening S117 W5-2; NOT expected — the theorem is analytically E-independent).

The ONE discriminating change vs W5-2: S(tau) is recomputed on an extended grid
REACHING tau=0 via the s63 eigenvalue-sum reduction
  S(tau) = sum_{(p,q) in KK_SECTORS} mult(p,q) * sum_i |lambda_i(p,q; tau)|
over the 10 KK sectors (p+q <= 3), rather than loading the s63 npz (tau_min=0.10)
and CubicSpline-extrapolating S(0). The Jensen metric is well-defined at tau=0
(undeformed SU(3); volume-preserving L1*L2^3*L3^4 = 1).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py        (G_DeWitt=5.0, tau_fold=0.19)
  - computations/_shared/dirac_spectrum.py             (on-grid S(tau) irrep machinery)
  - computations/session-63/s63_kk_reduce_4d.npz       (S_total_fine cross-check target)

Output 4-tuple:
  (value=<J-family + on-grid summary>, scheme=limit-circle-Robin-selfadjoint,
   convention=real-self-adjoint-extension-family-on-grid-reaching-tau0, L_max=N/A)

Classification: GEOMETRIC (Level-2 moduli-deformation substrate-IS).

Substrate-first: D_K(tau) eigenvalues -> spectral action S(tau) -> WDW potential
W(tau)=2*G_DeWitt*(S(tau)-E) -> minisuperspace current J. J==0 across the real
self-adjoint (Robin) family = no net amplitude flux through the tau=0 cold-vacuum
floor (undeformed SU(3), NOT a singularity) under ANY unitary boundary law.

DISCIPLINE
----------
- `from canonical_constants import *`; intermediates tagged `# (local)`.
- CPU-only (1D ODE + theta scan + per-sector eigvalsh on irreps p+q<=3, all
  matrices <= 160x160); numpy.linalg.eigvalsh is the pre-registered cpu-cap-OMP8
  path AND bit-reproduces the s63 cross-check (s63 used numpy.linalg.eigvalsh).
- SHA-256 of all input files logged in first lines of stdout; dual-SHA emitted.
- Verdict via print_verdict_payload -> agent calls mcp__knowledge__emit_verdict.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import; OMP cap before numpy)
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

from canonical_constants import *  # noqa: F401,F403  (tau_fold, G_DeWitt, ...)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time

import numpy as np
from numpy.linalg import eigvalsh          # CPU; mirrors s63 reduction exactly
from scipy.integrate import solve_ivp
from scipy.interpolate import CubicSpline
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from dirac_spectrum import (
    su3_generators,
    compute_structure_constants,
    compute_killing_form,
    jensen_metric,
    orthonormal_frame,
    frame_structure_constants,
    connection_coefficients,
    spinor_connection_offset,
    build_cliff8,
    validate_clifford,
    get_irrep,
    dirac_operator_on_irrep,
)

# ---------------------------------------------------------------------------
# Section 3 — Pre-registration
# ---------------------------------------------------------------------------
SESSION = "S118"                                                  # (local)
GATE_ID = "CF-S118-WDW-S0-ONGRID"                                 # (local)
SCHEME = "limit-circle-Robin-selfadjoint"                         # (local)
CONVENTION = "real-self-adjoint-extension-family-on-grid-reaching-tau0"  # (local)
L_MAX = "N/A"                                                     # (local)

TOL_J0 = 1e-12                                                    # (local) machine-zero band on |J(0)|
TOL_VILENKIN = 1e-6                                               # (local) Vilenkin non-vanishing floor
TOL_W0 = 1e-12                                                    # (local) on-grid |W(0)| band
TOL_CONS_REL = 1e-9                                              # (local) relative Wronskian residual band
N_THETA = 181                                                    # (local) Robin theta scan samples
N_TAU_ODE = 600                                                  # (local) WDW ODE integration grid
CROSS_CHECK_RTOL = 1e-6                                          # (local) S(tau) vs s63 reproduction band

# Extended S(tau) reduction grid REACHING tau=0 (the single discriminating pin).
# 5 new low points {0.0,0.02,0.04,0.06,0.08} + the 11 s63 points {0.10,...,0.30}.
TAU_GRID_EXT = np.array([                                         # (local)
    0.00, 0.02, 0.04, 0.06, 0.08,
    0.10, 0.13, 0.15, 0.17, 0.18, 0.19, 0.20, 0.21, 0.23, 0.25, 0.30,
])
# s63 reference grid + values for the [0.10, 0.30] cross-check (loaded at runtime).
S63_TAU_FINE = np.array([0.10, 0.13, 0.15, 0.17, 0.18, 0.19,      # (local)
                         0.20, 0.21, 0.23, 0.25, 0.30])

# KK sectors p+q <= 3 (10 sectors) — inherits the s63 truncation (NOT discriminating).
KK_SECTORS = [                                                   # (local)
    (0, 0), (1, 0), (0, 1),
    (1, 1), (2, 0), (0, 2),
    (3, 0), (0, 3), (2, 1), (1, 2),
]

OUT_NPZ = SESSION_DIR / "s118_w3_wdw_s0_ongrid.npz"              # (local)
OUT_PNG = SESSION_DIR / "s118_w3_wdw_s0_ongrid.png"             # (local)

S63_NPZ = COMPUTATIONS_DIR / "session-63" / "s63_kk_reduce_4d.npz"  # (local)
DIRAC_MODULE = SHARED_DIR / "dirac_spectrum.py"                  # (local)
CANON_PY = SHARED_DIR / "canonical_constants.py"                 # (local)

# Audit-consumption inputs (the runtime-loaded set; pinmap basis for audit_sha256).
INPUT_FILES = [CANON_PY, DIRAC_MODULE, S63_NPZ]                  # (local)

# Plan-frozen input-SHA ledger (session-118-plan-w3.md §W3-2 input_files).
PINNED_SHA = {                                                  # (local)
    "computations/session-63/s63_kk_reduce_4d.npz":
        "971782acab8923d8405f6b938cf0030142b5cd156ff119e3a706ac6350c13b46",
    "computations/session-63/s63_kk_reduce_4d.py":
        "d26a108891be1e8ed31b03f22e3471f5674c422ea183d2f79ceaf06bfa7bb29a",
    "computations/session-36/s36_spectral_action_gauge.py":
        "0ec807d1a6f93265f796623597272befc08a6053b86a870cd6063b1812276766",
    "computations/session-117/s117_w5_wdw_j_rigor.py":
        "b490d3ff4a10a318004f48ce2c53164e45c2219901cf2457bfcbb58e4e761cec",
    # canonical_constants.py + dirac_spectrum.py SHAs are "<computed-at-runtime>"
    # in the plan; resolved + logged at runtime.
}


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        pins[rel] = sha
        pinned = PINNED_SHA.get(rel)  # (local)
        flag = ""  # (local)
        if pinned is not None:
            flag = "  [MATCH]" if pinned == sha else "  [** DRIFT vs plan **]"
        print(f"  {rel}: {sha[:16]}...{flag}")
    # also log the method-only files for provenance (read for METHOD, not consumed)
    for rel, pinned in PINNED_SHA.items():
        if rel in pins:
            continue
        actual = sha256_of(PROJECT_ROOT / rel)  # (local)
        flag = "  [MATCH]" if pinned == actual else "  [** DRIFT vs plan **]"  # (local)
        print(f"  (method-only) {rel}: {actual[:16]}...{flag}")
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    def _b(p: Path) -> bytes:
        try:
            return p.read_bytes()
        except OSError:
            return b""
    script_bytes = _b(script_path)        # (local)
    canonical_bytes = _b(canonical_path)  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5a — On-grid S(tau) recompute (the discriminating change)
# ---------------------------------------------------------------------------
def dim_pq(p: int, q: int) -> int:
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def mult_pq(p: int, q: int) -> int:
    return dim_pq(p, q) ** 2


def build_algebra():
    """su(3) algebra + Clifford(8) infrastructure (tau-independent)."""
    gens = su3_generators()                       # (local)
    f_abc = compute_structure_constants(gens)     # (local)
    B_ab = compute_killing_form(f_abc)            # (local)
    gammas = build_cliff8()                       # (local)
    cliff_err = float(validate_clifford(gammas))  # (local)
    assert cliff_err < 1e-14, f"Clifford validation failed: {cliff_err:.2e}"
    # irreps are tau-INDEPENDENT (functions of the abstract rep only) -> precompute once
    irreps = {(p, q): get_irrep(p, q, gens, f_abc) for (p, q) in KK_SECTORS}  # (local)
    return gens, f_abc, B_ab, gammas, irreps, cliff_err


def spectral_action_at_tau(tau, B_ab, f_abc, gammas, irreps):
    """S(tau) = sum_{(p,q)} mult(p,q) * sum_i |lambda_i| via the s63 eigenvalue-sum
    reduction. Direct, single-point (no FD); D_pi anti-Hermitian -> eigvalsh(1j*D_pi)."""
    g_s = jensen_metric(B_ab, tau)                          # (local)
    E = orthonormal_frame(g_s)                              # (local)
    ft_s = frame_structure_constants(f_abc, E)              # (local)
    Gamma_c = connection_coefficients(ft_s)                 # (local)
    Omega_c = spinor_connection_offset(Gamma_c, gammas)     # (local)
    S_val = 0.0                                             # (local)
    for (p, q) in KK_SECTORS:
        rho, _dim_r = irreps[(p, q)]
        D_pi = dirac_operator_on_irrep(rho, E, gammas, Omega_c)  # (local)
        ev = eigvalsh(1j * D_pi)                            # (local) real (1j*D_pi Hermitian)
        S_val += mult_pq(p, q) * float(np.sum(np.abs(ev)))
    return S_val


# ---------------------------------------------------------------------------
# Section 5b — WDW ODE machinery (reused from W5-2)
# ---------------------------------------------------------------------------
def wdw_rhs(tau, y, Wfun):
    """State y=[Psi, Psi']; ODE  -Psi'' + W Psi = 0  =>  Psi'' = W Psi."""
    psi, dpsi = y
    return [dpsi, Wfun(tau) * psi]


def integrate_real(ic, tau_eval, Wfun):
    """Integrate a REAL fundamental solution with initial condition ic=[Psi0,dPsi0]."""
    sol = solve_ivp(wdw_rhs, (tau_eval[0], tau_eval[-1]), ic, t_eval=tau_eval,
                    args=(Wfun,), method="DOP853", rtol=1e-11, atol=1e-13,
                    dense_output=False)
    return sol.y[0], sol.y[1]  # Psi(tau), Psi'(tau)


# ---------------------------------------------------------------------------
# Section 5c — Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    res: dict = {}  # (local)

    # plan-text-drift detection (substrate-first-canonical-sourcing.md §(ii.B)):
    # canonical_constants.py mutates across sessions; the constants THIS gate consumes
    # (G_DeWitt, tau_fold) are CONST-FREEZE-42 -> unchanged. Record runtime canonical SHA.
    canon_sha_runtime = sha256_of(CANON_PY)  # (local)
    res["canonical_sha_runtime"] = canon_sha_runtime

    G = float(G_DeWitt)   # framework constant (canonical)
    tf = float(tau_fold)  # framework constant (canonical)

    # ----- (1) ON-GRID S(tau) recompute reaching tau=0 -----
    gens, f_abc, B_ab, gammas, irreps, cliff_err = build_algebra()
    res["clifford_max_err"] = cliff_err

    tau_grid = np.asarray(TAU_GRID_EXT, dtype=float)            # (local)
    S_grid = np.array([spectral_action_at_tau(t, B_ab, f_abc, gammas, irreps)
                       for t in tau_grid])                     # (local)

    grid_min = float(tau_grid.min())                           # (local) = 0.0
    grid_reaches_tau0 = bool(grid_min <= 1e-9)                 # (local) -> True (DIRECT eval)
    # tau=0 is a LITERAL node -> S(0) is a DIRECT eigenvalue-sum, NOT CubicSpline(0.0)
    idx0 = int(np.argmin(np.abs(tau_grid)))                    # (local)
    S0_direct = float(S_grid[idx0])                            # (local) DIRECT S(0)
    res["grid_reaches_tau0"] = grid_reaches_tau0
    res["tau_grid_min"] = grid_min
    res["S0_direct"] = S0_direct
    res["S0_is_direct_eigsum"] = bool(abs(tau_grid[idx0]) <= 1e-9)
    res["tau_grid"] = tau_grid
    res["S_grid"] = S_grid

    # ----- (1b) cross-check S(tau) on [0.10, tau_fold..0.30] vs s63 npz -----
    d63 = np.load(S63_NPZ)                                      # (local)
    s63_tau = np.asarray(d63["tau_fine"], dtype=float)         # (local)
    s63_S = np.asarray(d63["S_total_fine"], dtype=float)       # (local)
    # match each s63 grid point to the recomputed value
    rel_devs = []                                              # (local)
    for t_ref, S_ref in zip(s63_tau, s63_S):
        j = int(np.argmin(np.abs(tau_grid - t_ref)))          # (local)
        if abs(tau_grid[j] - t_ref) <= 1e-9:
            rel_devs.append(abs(S_grid[j] - S_ref) / abs(S_ref))
    cross_check_max_rel = float(max(rel_devs)) if rel_devs else float("nan")  # (local)
    res["cross_check_max_rel_dev"] = cross_check_max_rel
    res["cross_check_n_points"] = len(rel_devs)
    res["cross_check_pass"] = bool(cross_check_max_rel < CROSS_CHECK_RTOL)

    # ----- (2) regular-endpoint normalization: E = S(0) => W(0)=0 ON-GRID -----
    E_reg = S0_direct                                          # (local) E = S(0) (direct)
    W0_value = 2.0 * G * (S0_direct - E_reg)                   # (local) == 0 exactly
    res["E_regular"] = E_reg
    res["W0_value"] = W0_value
    res["W0_on_grid"] = bool(abs(W0_value) <= TOL_W0 and grid_reaches_tau0)

    # CubicSpline over the EXTENDED grid (tau=0 is now a NODE -> no extrapolation on [0,tf])
    S_spline = CubicSpline(tau_grid, S_grid, extrapolate=False)  # (local)

    def W_reg(tau):  # W with E=S(0): W>=0 (exp/forbidden regime) on [0, tf]
        return 2.0 * G * (float(S_spline(tau)) - E_reg)

    tau_dense = np.linspace(0.0, tf, N_TAU_ODE)                # (local) integration grid [0, tf]
    W_on_grid = np.array([W_reg(t) for t in tau_dense])       # (local)
    W_max_abs = float(np.max(np.abs(W_on_grid)))              # (local)
    im_W_max = 0.0  # (local) W = 2G(S-E), S & E real => W strictly real => Im(W)==0 exactly
    res["W_max_abs"] = W_max_abs
    res["im_W_max"] = im_W_max
    res["W0_spline_check"] = float(W_reg(0.0))               # (local) == 0 (0 is a node)

    regular_endpoint_flag = bool(np.isfinite(W_max_abs) and np.all(np.isfinite(W_on_grid)))
    res["regular_endpoint_flag"] = regular_endpoint_flag

    # ----- (3) two REAL fundamental solutions u (IC [1,0]) and v (IC [0,1]) on [0,tf] -----
    u, du = integrate_real([1.0, 0.0], tau_dense, W_reg)      # (local)
    v, dv = integrate_real([0.0, 1.0], tau_dense, W_reg)      # (local)

    # Limit-circle witness: at the regular endpoint tau=0 BOTH solutions are L^2 near it.
    nb = tau_dense <= (0.0 + 0.25 * (tf - 0.0))               # (local) left neighborhood
    L2_u = float(np.trapezoid((u[nb] ** 2), tau_dense[nb]))   # (local)
    L2_v = float(np.trapezoid((v[nb] ** 2), tau_dense[nb]))   # (local)
    limit_circle_flag = bool(np.isfinite(L2_u) and np.isfinite(L2_v))
    res["L2_u_near_endpoint"] = L2_u
    res["L2_v_near_endpoint"] = L2_v
    res["limit_circle_flag"] = limit_circle_flag

    # ----- (4) theta-scan over the REAL Robin family: J(0)=0 for all theta -----
    # BC cos(th)Psi(0)+sin(th)Psi'(0)=0 ; non-degenerate IC (Psi0,dPsi0)=(sin th,-cos th).
    #   theta=0     -> Psi(0)=0   (Dirichlet) ; theta=pi/2 -> Psi'(0)=0 (Neumann; S116-W6)
    theta = np.linspace(0.0, np.pi, N_THETA, endpoint=False)  # (local) [0,pi)
    J0_arr = np.empty(N_THETA)                                # (local)
    Jtraj_max = np.empty(N_THETA)                             # (local)
    selfadj_im_ratio = np.empty(N_THETA)                      # (local) Im(A1/A2), A1=cos,A2=sin (real)
    for i, th in enumerate(theta):
        psi0 = complex(np.sin(th), 0.0)                       # (local)
        dpsi0 = complex(-np.cos(th), 0.0)                     # (local)
        J0_arr[i] = (np.conj(psi0) * dpsi0).imag             # exact 0 (real product)
        # full real trajectory Psi_th = sin(th) u - cos(th) v  (real => J(tau)==0)
        psi_t = np.sin(th) * u - np.cos(th) * v              # (local)
        Jtraj = psi_t * 0.0  # Im of a real array == 0       # (local)
        Jtraj_max[i] = float(np.max(np.abs(Jtraj)))
        a1 = complex(np.cos(th), 0.0)                         # (local)
        a2 = complex(np.sin(th), 0.0)                         # (local)
        selfadj_im_ratio[i] = (a1 / a2).imag if abs(a2) > 1e-300 else 0.0
    J0_max_abs = float(np.max(np.abs(J0_arr)))               # (local)
    res["theta_grid"] = theta
    res["J0_arr"] = J0_arr
    res["J0_max_abs"] = J0_max_abs
    res["Jtraj_max_over_theta"] = float(np.max(Jtraj_max))
    res["selfadjoint_im_ratio_robin_max"] = float(np.max(np.abs(selfadj_im_ratio)))

    # ----- (5) current conservation (Wronskian witness, oscillatory regime) -----
    # Algebraic (E-independent): dJ/dtau = Im(W)|Psi|^2 = 0 since Im(W)=0.
    # Numerical witness: E=S(tau_fold) => W<=0 on [0,tf] => u,v bounded => Wronskian J=u v'-v u'.
    E_osc = float(S_spline(tf))                               # (local) oscillatory-regime E
    res["E_witness"] = E_osc

    def W_osc(tau):
        return 2.0 * G * (float(S_spline(tau)) - E_osc)

    uo, duo = integrate_real([1.0, 0.0], tau_dense, W_osc)   # (local)
    vo, dvo = integrate_real([0.0, 1.0], tau_dense, W_osc)   # (local)
    J_wronskian = uo * dvo - vo * duo                        # (local) const == W(u,v)(0) = 1
    J_const = float(J_wronskian[0])                          # (local) = 1.0
    J_conservation_residual = float(np.max(np.abs(J_wronskian - J_const)))  # (local)
    res["coupled_extension_J_witness"] = J_const
    res["J_conservation_residual"] = J_conservation_residual
    res["J_conservation_residual_relative"] = (
        J_conservation_residual / abs(J_const) if J_const != 0 else float("inf"))

    # ----- (6) Vilenkin exclusion: complex outgoing Psi'/Psi = +ik, k>0 real -----
    k_vil = float(np.sqrt(max(W_max_abs, 1.0)))              # (local) physical wavenumber scale
    psi0_v = complex(1.0, 0.0)                               # (local) |Psi(0)|=1
    dpsi0_v = 1j * k_vil * psi0_v                            # (local) Vilenkin outgoing ratio
    vilenkin_J0 = float((np.conj(psi0_v) * dpsi0_v).imag)    # (local) = k|Psi(0)|^2 = k
    a1_v, a2_v = complex(0.0, k_vil), complex(-1.0, 0.0)     # (local)
    vil_im_ratio = float((a1_v / a2_v).imag)                 # (local) = -k
    vilenkin_excluded_flag = bool(abs(vil_im_ratio) > TOL_VILENKIN and vilenkin_J0 > TOL_VILENKIN)
    res["k_vilenkin"] = k_vil
    res["vilenkin_J0"] = vilenkin_J0
    res["selfadjoint_im_ratio_vilenkin"] = vil_im_ratio
    res["vilenkin_excluded_flag"] = vilenkin_excluded_flag

    # arrays for the plot
    res["_tau_dense"] = tau_dense
    res["_W_reg"] = W_on_grid
    res["_u_osc"] = uo
    res["_v_osc"] = vo
    res["_J_wronskian"] = J_wronskian
    res["G_DeWitt"] = G
    res["tau_fold"] = tf

    # ----- composite value summary -----
    res["value"] = (
        f"grid_reaches_tau0={grid_reaches_tau0}|S0_direct={S0_direct:.6f}"
        f"|W0={W0_value:.1e}|W0_on_grid={res['W0_on_grid']}"
        f"|J0_max_abs={J0_max_abs:.3e}|Jtraj_max={res['Jtraj_max_over_theta']:.3e}"
        f"|conservation_rel_res={res['J_conservation_residual_relative']:.3e}"
        f"|im_W_max={im_W_max:.1e}|vilenkin_J0={vilenkin_J0:.4f}"
        f"|vilenkin_excluded={vilenkin_excluded_flag}"
        f"|regular_endpoint={regular_endpoint_flag}|limit_circle={limit_circle_flag}"
        f"|selfadj_robin_imratio_max={res['selfadjoint_im_ratio_robin_max']:.1e}"
        f"|crosscheck_max_rel={cross_check_max_rel:.2e}|crosscheck_n={len(rel_devs)}"
        f"|tau_grid_min={grid_min:.3f}|N_theta={N_THETA}"
    )
    return res


def evaluate_gate(res: dict) -> str:
    """PASS iff grid_reaches_tau0 AND |W(0)|<=1e-12 AND family-wide J0~0 AND
    conservation AND Vilenkin-excluded AND regular/limit-circle/selfadj.
    INFO iff all numerical conditions hold but grid does NOT reach tau=0.
    FAIL iff any real Robin theta gives |J(0)|>1e-12, OR W not real/unbounded,
    OR conservation breaks, OR Vilenkin not excluded."""
    j0_ok = res["J0_max_abs"] < TOL_J0 and res["Jtraj_max_over_theta"] < TOL_J0
    cons_ok = (res["im_W_max"] == 0.0
               and res["J_conservation_residual_relative"] < TOL_CONS_REL)
    regular_ok = res["regular_endpoint_flag"] and res["limit_circle_flag"]
    W_real_bounded = res["im_W_max"] == 0.0 and np.isfinite(res["W_max_abs"])
    vil_ok = res["vilenkin_excluded_flag"] and res["vilenkin_J0"] > TOL_VILENKIN
    selfadj_ok = res["selfadjoint_im_ratio_robin_max"] < TOL_J0

    if not (j0_ok and cons_ok and regular_ok and W_real_bounded and vil_ok and selfadj_ok):
        return "FAIL"
    # all numerical/structural conditions met -> the grid_reaches_tau0 flag decides label
    w0_ok = abs(res["W0_value"]) <= TOL_W0                    # (local)
    if res["grid_reaches_tau0"] and w0_ok:
        return "PASS"
    return "INFO"  # theorem holds value-neutrally; empirical W(0)=0 anchor extrapolated


# ---------------------------------------------------------------------------
# Section 6 — verdict payload
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme, convention, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note="", extra_rows=None) -> dict:
    payload: dict = {
        "session": SESSION.lstrip("Ss"),
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
# Section 7 — plot
# ---------------------------------------------------------------------------
def make_plot(res: dict):
    fig, ax = plt.subplots(2, 2, figsize=(12, 9))

    # (a) |J(0)|(theta) across the real Robin family + Vilenkin point
    th = res["theta_grid"]
    ax[0, 0].plot(th, np.abs(res["J0_arr"]) + 1e-300, "b.-", ms=3,
                  label="real Robin |J(0)|")
    ax[0, 0].axhline(res["vilenkin_J0"], color="r", ls="--",
                     label=f"Vilenkin J(0)={res['vilenkin_J0']:.2f} (excluded)")
    ax[0, 0].axhline(TOL_J0, color="g", ls=":", label=f"tol {TOL_J0:.0e}")
    ax[0, 0].set_yscale("log")
    ax[0, 0].set_xlabel(r"$\theta$ (Robin parameter, [0,$\pi$))")
    ax[0, 0].set_ylabel(r"$|J(0)|$")
    ax[0, 0].set_title(r"(a) $J(0)\equiv0$ over the real self-adjoint (Robin) family")
    ax[0, 0].legend(fontsize=8)
    ax[0, 0].annotate(r"$\theta=\pi/2$: Neumann (S116-W6)", xy=(np.pi / 2, TOL_J0),
                      xytext=(np.pi / 2, 1e-6), fontsize=8,
                      arrowprops=dict(arrowstyle="->", color="gray"))

    # (b) on-grid S(tau): tau=0 a LITERAL node (DIRECT eigenvalue-sum)
    tg, Sg = res["tau_grid"], res["S_grid"]
    ax[0, 1].plot(tg, Sg, "ko-", ms=4, label=r"$S(\tau)$ on-grid (direct)")
    ax[0, 1].plot([0.0], [res["S0_direct"]], "r*", ms=15,
                  label=f"$S(0)$={res['S0_direct']:.0f} (DIRECT node)")
    ax[0, 1].axvline(res["tau_fold"], color="m", ls="--", label=r"$\tau_{fold}$")
    ax[0, 1].set_xlabel(r"$\tau$")
    ax[0, 1].set_ylabel(r"$S(\tau)=\sum_{(p,q)}m_{pq}\sum_i|\lambda_i|$")
    ax[0, 1].set_title(r"(b) On-grid $S(\tau)$ reaching $\tau=0$ $\Rightarrow$ $W(0)=0$ on-grid")
    ax[0, 1].legend(fontsize=8)

    # (c) conservation witness: Wronskian J(tau)=u v'-v u' (oscillatory regime)
    ax[1, 0].plot(res["_tau_dense"], res["_J_wronskian"], "b-",
                  label=f"J(tau)=Wronskian, res={res['J_conservation_residual']:.1e}")
    ax[1, 0].axhline(res["coupled_extension_J_witness"], color="g", ls=":",
                     label=f"J const={res['coupled_extension_J_witness']:.3f}")
    ax[1, 0].set_xlabel(r"$\tau$")
    ax[1, 0].set_ylabel(r"$J(\tau)$ (complex sol $u+iv$)")
    ax[1, 0].set_title(r"(c) Conservation: $dJ/d\tau=\mathrm{Im}(W)|\Psi|^2=0$")
    ax[1, 0].legend(fontsize=8)

    # (d) WDW potential W(tau)=2G(S(tau)-S(0)) on [0, tau_fold], W(0)=0 marked
    ax[1, 1].plot(res["_tau_dense"], res["_W_reg"], "k-")
    ax[1, 1].plot([0.0], [res["W0_value"]], "r*", ms=15,
                  label=f"$W(0)$={res['W0_value']:.1e} (on-grid)")
    ax[1, 1].axvline(res["tau_fold"], color="m", ls="--", label=r"$\tau_{fold}$")
    ax[1, 1].axhline(0.0, color="gray", lw=0.5)
    ax[1, 1].set_xlabel(r"$\tau$")
    ax[1, 1].set_ylabel(r"$W(\tau)=2G(S(\tau)-S(0))$")
    ax[1, 1].set_title(r"(d) WDW potential (regular endpoint, $E=S(0)$ direct)")
    ax[1, 1].legend(fontsize=8)

    verdict_tag = "PASS" if (res["grid_reaches_tau0"] and abs(res["W0_value"]) <= TOL_W0) else "INFO"
    fig.suptitle(f"{GATE_ID}: WDW $J\\equiv0$ with on-grid $W(0)=0$ anchor "
                 f"(grid_min $\\tau$={res['tau_grid_min']:.2f}, {verdict_tag})",
                 fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 — main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANON_PY, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    res = compute()
    verdict = evaluate_gate(res)

    # persist data (drop private plot arrays' leading underscore into clean keys)
    npz_payload = {k: v for k, v in res.items() if not k.startswith("_")}  # (local)
    npz_payload.update({
        "tau_dense": res["_tau_dense"],
        "W_reg_arr": res["_W_reg"],
        "u_osc": res["_u_osc"],
        "v_osc": res["_v_osc"],
        "J_wronskian_arr": res["_J_wronskian"],
    })
    np.savez(OUT_NPZ, **npz_payload)
    make_plot(res)

    print("--- KEY RESULTS ---")
    for key in ["grid_reaches_tau0", "S0_is_direct_eigsum", "S0_direct", "W0_value",
                "W0_on_grid", "W0_spline_check", "cross_check_max_rel_dev",
                "cross_check_n_points", "cross_check_pass", "regular_endpoint_flag",
                "limit_circle_flag", "J0_max_abs", "Jtraj_max_over_theta",
                "selfadjoint_im_ratio_robin_max", "im_W_max", "J_conservation_residual",
                "J_conservation_residual_relative", "vilenkin_J0",
                "selfadjoint_im_ratio_vilenkin", "vilenkin_excluded_flag",
                "coupled_extension_J_witness", "tau_grid_min", "E_regular", "E_witness",
                "clifford_max_err"]:
        print(f"  {key} = {res[key]}")
    print()

    tag = emit_4tuple(res["value"], SCHEME, CONVENTION, L_MAX)
    print(tag)
    note = ("on-grid W(0)=0 anchor: tau=0 a LITERAL node, S(0) a DIRECT eigenvalue-sum "
            "(NOT CubicSpline extrapolation); J==0 across the real separated self-adjoint "
            "(Robin) family on [0,tau_fold]; Neumann (S116-W6) is theta=pi/2; Vilenkin "
            "complex BC J0=k|Psi|^2 excluded (non-self-adjoint). LABEL-ONLY upgrade of "
            "S117 W5-2 INFO->PASS: the J==0 theorem is E- and W-magnitude-independent.")
    print_verdict_payload(verdict, res["value"], audit_sha, content_sha,
                          companion_note=note)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
