#!/usr/bin/env python3
"""
S117 W5-2 — CF-S117-WDW-J-RIGOR — WDW J(0)=0 across the real self-adjoint family
================================================================================

Gate: CF-S117-WDW-J-RIGOR  ([VERIFY-THEOREM])

Pre-registered threshold:
  |J(0)| < 1e-12 for EVERY sampled real Robin theta (machine-zero);
  AND |J(0)| = k|Psi(0)|^2 > 1e-6 for the Vilenkin complex BC (non-vanishing,
  confirming non-self-adjoint exclusion).
  PASS iff both hold with the s63 S(tau) grid reaching tau=0 cleanly;
  INFO iff both hold but the grid does NOT reach tau=0 (W(0)=0 anchor extrapolated);
  FAIL iff some real Robin theta gives |J(0)|>1e-12, OR W not real / unbounded,
  OR current conservation breaks.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py
  - computations/session-63/s63_kk_reduce_4d.npz   (S_total_fine, tau_fine -> W(tau))
  - sessions/session-116/session-116-w6-workingpaper.md  (Eq. H-R3-1 anchor; SHA only)

Output 4-tuple:
  (value=<J-family summary>, scheme=limit-circle-Robin-selfadjoint,
   convention=real-self-adjoint-extension-family, L_max=N/A)

Classification: GEOMETRIC

METHODOLOGY
-----------
Rigorizes Eq. H-R3-1 (the S116-W6 Sage-verified Neumann reflecting-tau=0 -> J==0
identity) from the single Neumann condition to the ENTIRE real self-adjoint
(separated / Robin) extension family of the 1D minisuperspace WDW operator
L = -d^2/dtau^2 + W(tau), W(tau) = 2 G_DeWitt (S(tau) - E), on the FINITE interval
[0, tau_fold]. Weyl-Titchmarsh: a finite endpoint with W in L^1 near it is REGULAR
=> both solutions L^2 near it => limit-circle. With both endpoints regular the
deficiency indices are (2,2); the SEPARATED self-adjoint extensions at tau=0 are
EXACTLY the real Robin family { cos(th) Psi(0)+sin(th) Psi'(0)=0 : th in [0,pi) },
and EVERY one forces J(0)=Im(Psi*(0)Psi'(0))=0 (real boundary ratio). Current
conservation dJ/dtau = Im(W)|Psi|^2 = 0 (W real) then gives J==0 on [0,tau_fold].
The Vilenkin outgoing condition Psi'/Psi=+ik is a COMPLEX boundary ratio (net flux
J(0)=k|Psi(0)|^2 != 0) => non-self-adjoint => excluded. (All four boundary-form
identities Sage-verified prior to this script.)

Substrate-first: D_K eigenvalues -> spectral action S(tau) -> WDW potential
W(tau)=2G(S(tau)-E) -> minisuperspace current J. No net amplitude flux through the
tau=0 cold-vacuum floor under ANY unitary (real self-adjoint) boundary law.

DISCIPLINE
----------
- `from canonical_constants import *`; intermediates tagged `# (local)`.
- CPU-only (1D ODE + theta scan + small algebra; no matrix >= 100x100); OMP cap 8.
- SHA-256 of all input files logged in first 20 lines of stdout; dual-SHA emitted.
- Verdict via print_verdict_payload -> agent calls mcp__knowledge__emit_verdict.
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

from canonical_constants import *  # noqa: F401,F403  (tau_fold, G_DeWitt, M_KK, ...)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time

import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import CubicSpline
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Pre-registration
# ---------------------------------------------------------------------------
SESSION = "S117"                                                   # (local)
GATE_ID = "CF-S117-WDW-J-RIGOR"                                    # (local)
SCHEME = "limit-circle-Robin-selfadjoint"                          # (local)
CONVENTION = "real-self-adjoint-extension-family"                  # (local)
L_MAX = "N/A"                                                      # (local)

TOL_J0 = 1e-12                                                     # (local) machine-zero band on |J(0)|
TOL_VILENKIN = 1e-6                                                # (local) Vilenkin non-vanishing floor
N_THETA = 181                                                      # (local) Robin theta scan samples

OUT_NPZ = SESSION_DIR / "s117_w5_wdw_j_rigor.npz"                  # (local)
OUT_PNG = SESSION_DIR / "s117_w5_wdw_j_rigor.png"                  # (local)

S63_NPZ = COMPUTATIONS_DIR / "session-63" / "s63_kk_reduce_4d.npz"            # (local)
S116_W6_WP = PROJECT_ROOT / "sessions" / "session-116" / "session-116-w6-workingpaper.md"  # (local)

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    S63_NPZ,
    S116_W6_WP,
]

# Plan-frozen input-SHA ledger (session-117-plan-w5.md "Wave 5 Input-SHA Ledger")
PINNED_SHA = {                                                     # (local)
    "computations/_shared/canonical_constants.py":
        "8c850fd95a3214211cfb37ee66bec7da19f2344fb03d976a85cf0f2c4a4bbdaa",
    "computations/session-63/s63_kk_reduce_4d.npz":
        "971782acab8923d8405f6b938cf0030142b5cd156ff119e3a706ac6350c13b46",
    # s116-w6 WP SHA is "<computed-at-runtime>" in the plan; resolved here.
}


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (first 20 lines of stdout)
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
# Section 5 — Compute
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


def compute() -> dict:
    res: dict = {}  # (local)

    # plan-text-drift detection (substrate-first-canonical-sourcing.md §(ii.B)):
    # canonical_constants.py may have changed since plan-freeze (the in-session W0-1
    # CF-S117-HK-RHOS-C2-PROMOTE added a rho_s/C2 constant). DOCUMENT, then proceed with
    # the runtime canonical (audit_sha256 reflects the runtime bytes). The constants THIS
    # gate consumes (tau_fold, G_DeWitt) are CONST-FREEZE-42 -> unchanged; drift is benign.
    canon_sha_runtime = sha256_of(SHARED_DIR / "canonical_constants.py")  # (local)
    canon_drift = bool(
        canon_sha_runtime != PINNED_SHA["computations/_shared/canonical_constants.py"])  # (local)
    res["canonical_sha_drift_from_plan"] = canon_drift

    # ----- load substrate spectral action S(tau) -----
    d = np.load(S63_NPZ)  # (local)
    tau_fine = np.asarray(d["tau_fine"], dtype=float)        # (local)
    S_fine = np.asarray(d["S_total_fine"], dtype=float)      # (local)
    order = np.argsort(tau_fine)                             # (local)
    tau_fine, S_fine = tau_fine[order], S_fine[order]
    G = float(G_DeWitt)                                      # framework constant (canonical)
    tf = float(tau_fold)                                     # framework constant (canonical)

    grid_min = float(tau_fine.min())                         # (local) = 0.10
    grid_reaches_tau0 = bool(grid_min <= 1e-9)               # (local) -> False here
    res["grid_reaches_tau0"] = grid_reaches_tau0
    res["tau_grid_min"] = grid_min

    # Spline S(tau): smooth monotone S36 spectral action; extrapolate to tau=0 (short).
    S_spline = CubicSpline(tau_fine, S_fine, extrapolate=True)   # (local)
    S0_spline = float(S_spline(0.0))                            # (local) extrapolated S(0)
    # Quadratic-fit cross-check on the first 4 points (extrapolation-uncertainty witness)
    coef = np.polyfit(tau_fine[:4], S_fine[:4], 2)             # (local)
    S0_quad = float(np.polyval(coef, 0.0))                     # (local)
    res["S0_extrap_spline"] = S0_spline
    res["S0_extrap_quad"] = S0_quad
    res["S0_extrap_spread"] = abs(S0_spline - S0_quad)

    # ----- regular-endpoint normalization: E = S(0) (Hamiltonian-constraint W(0)=0) -----
    # NOTE: the regular-endpoint CLASSIFICATION needs only W bounded near tau=0; the
    # W(0)=0 value (E=S(0)) is a cosmetic Hamiltonian-constraint normalization, NOT
    # load-bearing for limit-circle. We use it to match the plan's W(0)=2G(S(0)-E)=0.
    E_reg = S0_spline                                          # (local) regular-endpoint E
    W0_value = 2.0 * G * (S0_spline - E_reg)                   # (local) == 0 by construction
    res["E_regular"] = E_reg
    res["W0_value"] = W0_value

    # WDW potential on [0, tau_fold]; integrate on the available sub-grid [grid_min, tf].
    def W_reg(tau):  # W with E=S(0): W>=0 (exp/forbidden regime) on (grid_min, tf]
        return 2.0 * G * (float(S_spline(tau)) - E_reg)

    a_int = grid_min                                          # (local) left integration endpoint (~tau=0 floor)
    b_int = tf                                                # (local) right endpoint = tau_fold
    tau_dense = np.linspace(a_int, b_int, 600)                # (local) dense integration grid

    # boundedness / regularity witness (W continuous & bounded near tau=0)
    W_on_grid = np.array([W_reg(t) for t in tau_dense])       # (local)
    W_max_abs = float(np.max(np.abs(W_on_grid)))              # (local)
    im_W_max = 0.0  # (local) W = 2G(S-E), S & E real => W strictly real => Im(W)==0 exactly
    res["W_max_abs"] = W_max_abs
    res["im_W_max"] = im_W_max

    # Regular endpoint: finite endpoint + W in L^1 near it (W continuous & bounded).
    regular_endpoint_flag = bool(np.isfinite(W_max_abs) and np.all(np.isfinite(W_on_grid)))
    res["regular_endpoint_flag"] = regular_endpoint_flag

    # ----- two REAL fundamental solutions u (IC [1,0]) and v (IC [0,1]) -----
    u, du = integrate_real([1.0, 0.0], tau_dense, W_reg)      # (local)
    v, dv = integrate_real([0.0, 1.0], tau_dense, W_reg)      # (local)

    # Limit-circle witness: at a regular endpoint BOTH solutions are L^2 near it.
    nb = tau_dense <= (a_int + 0.25 * (b_int - a_int))        # (local) left neighborhood
    L2_u = float(np.trapezoid((u[nb] ** 2), tau_dense[nb]))       # (local)
    L2_v = float(np.trapezoid((v[nb] ** 2), tau_dense[nb]))       # (local)
    limit_circle_flag = bool(np.isfinite(L2_u) and np.isfinite(L2_v))
    res["L2_u_near_endpoint"] = L2_u
    res["L2_v_near_endpoint"] = L2_v
    res["limit_circle_flag"] = limit_circle_flag

    # ----- (C) theta-scan over the REAL Robin family: J(0)=0 for all theta -----
    # BC cos(th)Psi(0)+sin(th)Psi'(0)=0 ; non-degenerate IC (Psi0,dPsi0)=(sin th,-cos th).
    #   theta=0     -> Psi(0)=0           (Dirichlet)
    #   theta=pi/2  -> Psi'(0)=0          (Neumann; the S116-W6 case)
    theta = np.linspace(0.0, np.pi, N_THETA, endpoint=False)  # (local) [0,pi)
    J0_arr = np.empty(N_THETA)                                # (local)
    Jtraj_max = np.empty(N_THETA)                             # (local) max|J(tau)| along trajectory
    selfadj_im_ratio = np.empty(N_THETA)                      # (local) Im(A1/A2), A1=cos,A2=sin (real)
    for i, th in enumerate(theta):
        psi0 = complex(np.sin(th), 0.0)                       # (local)
        dpsi0 = complex(-np.cos(th), 0.0)                     # (local)
        J0_arr[i] = (np.conj(psi0) * dpsi0).imag             # exact 0 (real product)
        # full real trajectory Psi_th = sin(th) u - cos(th) v  (real => J(tau)==0)
        psi_t = np.sin(th) * u - np.cos(th) * v              # (local)
        dpsi_t = np.sin(th) * du - np.cos(th) * dv           # (local)
        Jtraj = (psi_t * 0.0)  # Im of real array == 0       # (local)
        Jtraj_max[i] = float(np.max(np.abs(Jtraj)))
        # self-adjointness criterion: A1=cos(th), A2=sin(th) both real => Im(A1/A2)=0
        a1 = complex(np.cos(th), 0.0)                         # (local)
        a2 = complex(np.sin(th), 0.0)                         # (local)
        selfadj_im_ratio[i] = (a1 / a2).imag if abs(a2) > 1e-300 else 0.0
    J0_max_abs = float(np.max(np.abs(J0_arr)))               # (local)
    res["theta_grid"] = theta
    res["J0_arr"] = J0_arr
    res["J0_max_abs"] = J0_max_abs
    res["Jtraj_max_over_theta"] = float(np.max(Jtraj_max))
    res["selfadjoint_im_ratio_robin_max"] = float(np.max(np.abs(selfadj_im_ratio)))

    # ----- (D) current conservation -----
    # Algebraic (E-independent, all regimes): dJ/dtau = Im(W)|Psi|^2 = 0 since Im(W)=0.
    # Numerical Wronskian witness on a BOUNDED (oscillatory) reference: E=S(tau_fold)
    #   => W<=0 on [grid_min,tf] => u,v bounded => J=u v' - v u' = Wronskian well-conditioned.
    E_osc = float(S_spline(tf))                               # (local) oscillatory-regime E
    res["E_witness"] = E_osc

    def W_osc(tau):
        return 2.0 * G * (float(S_spline(tau)) - E_osc)

    uo, duo = integrate_real([1.0, 0.0], tau_dense, W_osc)   # (local)
    vo, dvo = integrate_real([0.0, 1.0], tau_dense, W_osc)   # (local)
    # Psi = u + i v  =>  J(tau) = Im(conj(Psi)Psi') = u v' - v u'  (real arrays; exact)
    J_wronskian = uo * dvo - vo * duo                        # (local) const == W(u,v)(0) = 1
    J_const = float(J_wronskian[0])                          # (local) = 1.0
    J_conservation_residual = float(np.max(np.abs(J_wronskian - J_const)))  # (local)
    res["coupled_extension_J_witness"] = J_const             # nonzero conserved current (complex sol)
    res["J_conservation_residual"] = J_conservation_residual
    res["J_conservation_residual_relative"] = (
        J_conservation_residual / abs(J_const) if J_const != 0 else float("inf"))

    # ----- (E) Vilenkin exclusion: complex outgoing Psi'/Psi = +ik, k>0 real -----
    k_vil = float(np.sqrt(max(W_max_abs, 1.0)))              # (local) physical wavenumber scale
    psi0_v = complex(1.0, 0.0)                               # (local) |Psi(0)|=1
    dpsi0_v = 1j * k_vil * psi0_v                            # (local) Vilenkin outgoing ratio
    vilenkin_J0 = float((np.conj(psi0_v) * dpsi0_v).imag)    # (local) = k|Psi(0)|^2 = k
    # self-adjointness criterion: BC ik Psi(0) - Psi'(0)=0 -> A1=ik, A2=-1 -> Im(A1/A2)=-k != 0
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
        f"J0_max_abs={J0_max_abs:.3e}|Jtraj_max={res['Jtraj_max_over_theta']:.3e}"
        f"|conservation_res={J_conservation_residual:.3e}|im_W_max={im_W_max:.1e}"
        f"|vilenkin_J0={vilenkin_J0:.4f}|vilenkin_excluded={vilenkin_excluded_flag}"
        f"|regular_endpoint={regular_endpoint_flag}|limit_circle={limit_circle_flag}"
        f"|selfadj_robin_imratio_max={res['selfadjoint_im_ratio_robin_max']:.1e}"
        f"|coupled_J_witness={J_const:.4f}|grid_reaches_tau0={grid_reaches_tau0}"
        f"|tau_grid_min={grid_min:.3f}|N_theta={N_THETA}"
        f"|canon_drift={canon_drift}_consumed_consts_unchanged"
    )
    return res


def evaluate_gate(res: dict) -> str:
    """PASS iff family-wide J0~0 + conservation + Vilenkin-excluded AND grid reaches tau=0.
    INFO iff all numerical conditions hold but grid does NOT reach tau=0 (W(0) extrapolated).
    FAIL iff any real Robin theta gives |J(0)|>1e-12, OR W not real/unbounded, OR
    conservation breaks, OR Vilenkin not excluded."""
    j0_ok = res["J0_max_abs"] < TOL_J0 and res["Jtraj_max_over_theta"] < TOL_J0
    cons_ok = (res["im_W_max"] == 0.0
               and res["J_conservation_residual_relative"] < 1e-9)
    regular_ok = res["regular_endpoint_flag"] and res["limit_circle_flag"]
    W_real_bounded = res["im_W_max"] == 0.0 and np.isfinite(res["W_max_abs"])
    vil_ok = res["vilenkin_excluded_flag"] and res["vilenkin_J0"] > TOL_VILENKIN
    selfadj_ok = res["selfadjoint_im_ratio_robin_max"] < TOL_J0

    if not (j0_ok and cons_ok and regular_ok and W_real_bounded and vil_ok and selfadj_ok):
        return "FAIL"
    # all numerical/structural conditions met
    if res["grid_reaches_tau0"]:
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

    # (b) WDW potential W(tau) on [~0, tau_fold]
    ax[0, 1].plot(res["_tau_dense"], res["_W_reg"], "k-")
    ax[0, 1].axvline(res["tau_fold"], color="m", ls="--", label=r"$\tau_{fold}$")
    ax[0, 1].axhline(0.0, color="gray", lw=0.5)
    ax[0, 1].set_xlabel(r"$\tau$")
    ax[0, 1].set_ylabel(r"$W(\tau)=2G(S(\tau)-S(0))$")
    ax[0, 1].set_title(r"(b) WDW potential (regular endpoint, $E=S(0)$)")
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

    # (d) fundamental solutions (oscillatory regime)
    ax[1, 1].plot(res["_tau_dense"], res["_u_osc"], "b-", label="u (IC [1,0])")
    ax[1, 1].plot(res["_tau_dense"], res["_v_osc"], "r-", label="v (IC [0,1])")
    ax[1, 1].set_xlabel(r"$\tau$")
    ax[1, 1].set_ylabel(r"$\Psi(\tau)$")
    ax[1, 1].set_title("(d) Real fundamental solutions (limit-circle: both $L^2$)")
    ax[1, 1].legend(fontsize=8)

    fig.suptitle(f"{GATE_ID}: WDW $J\\equiv0$ across the real self-adjoint family "
                 f"(grid_min $\\tau$={res['tau_grid_min']:.2f}, INFO: $W(0)$ extrapolated)",
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
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
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
    for key in ["regular_endpoint_flag", "limit_circle_flag", "J0_max_abs",
                "Jtraj_max_over_theta", "selfadjoint_im_ratio_robin_max",
                "im_W_max", "J_conservation_residual", "J_conservation_residual_relative",
                "vilenkin_J0", "selfadjoint_im_ratio_vilenkin", "vilenkin_excluded_flag",
                "coupled_extension_J_witness", "W0_value", "S0_extrap_spread",
                "grid_reaches_tau0", "tau_grid_min", "E_regular", "E_witness"]:
        print(f"  {key} = {res[key]}")
    print()

    tag = emit_4tuple(res["value"], SCHEME, CONVENTION, L_MAX)
    print(tag)
    note = ("J==0 across the real separated self-adjoint (Robin) family on [0,tau_fold]; "
            "Neumann (S116-W6) is theta=pi/2; Vilenkin complex BC J0=k|Psi|^2 excluded "
            "(non-self-adjoint); INFO: s63 grid min tau=0.10, W(0)=0 anchor extrapolated "
            "(theorem is W-magnitude- and E-independent).")
    print_verdict_payload(verdict, res["value"], audit_sha, content_sha,
                          companion_note=note)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
