#!/usr/bin/env python3
"""
INV11 W3-3 — Wheeler-DeWitt Psi(tau) on minisuperspace; emergent time + K_pivot e-folds
========================================================================================

Gate: INV11-W3-3-WHEELER-DEWITT-PSI-TAU-EFOLD ([VERIFY])
  Two-clause AND: (i) tau_peak <= 1.7e-5 (|Psi|^2 maximum inside Window-1) AND
                  (ii) N_e_WKB >= 3.1 (WKB-branch e-fold integral).

Pre-registered threshold (plan §W3-3):
  PASS iff tau_peak <= 1.7e-5 AND N_e_WKB >= 3.1.
  FAIL iff EITHER tau_peak > 1.7e-5 OR N_e_WKB < 3.1 (outside the INFO bands).
  INFO iff one clause marginal: N_e_WKB in [2.89, 3.1] OR tau_peak in [1.7e-5, 1.7e-4].

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - computations/_shared/canonical_constants.py  (G_DeWitt, tau_fold; feeds audit_sha256)
  - computations/session-36/s36_sfull_tau_stabilization.npz
        the SUBSTRATE-FIRST monotone spectral-action curve S(tau) (Tr f(D_K^2/Lambda^2));
        the plan-pinned `computations/_shared/s_tau_spectral_action_curve.npz` is ABSENT, so
        per substrate-first-canonical-sourcing.md §(ii.B) the npz-ground-truth canonical S(tau)
        is the S36 curve (keys tau_combined, S_full, dS_fold, S_fold, d2S_fold). The drift is
        documented in the verdict value= field (s_tau_curve_resolved_from_S36).
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz
        the L12 D_K eigenvalue cache (kept as a pin for the substrate-first reconstruction
        cross-check; the S36 curve is the primary V(tau) source).
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<tau_peak,N_e_WKB>, scheme=WDW-minisuperspace, convention=DeWitt-supermetric-G5, L_max=12)

Classification: GEOMETRIC. The minisuperspace IS the Jensen deformation parameter tau --
  the substrate's OWN intrinsic deformation coordinate (Level-2 substrate-IS per
  phononic-framing.md §"Single-tau-slice vs moduli-deformation"), NOT a coordinate on a
  meta-container. Psi(tau) is the amplitude over the substrate's own deformation; the
  spectral action S(tau) is the flow D_K eigenvalues -> spectral-action moments -> V(tau).
  The WKB branch of Psi(tau) DEFINES the emergent-time direction FROM the constraint --
  time is a CONSEQUENCE of the spectral geometry, not a prior stage.

METHODOLOGY
-----------
Solve the WDW equation on the 1D tau minisuperspace
    [ -(1/(2 G_DeWitt)) d^2/dtau^2 + V(tau) ] Psi(tau) = 0 ,
with V(tau) = S(tau) the monotone S36 spectral-action curve (cubic spline) and
G_DeWitt = 5.0 (volume-preserving DeWitt supermetric, S42). At E = V(0) (the stable
minimum; d^2 V/dtau^2|_0 = +3.00e5 > 0 from the S36 spline, consistent with the
QFLUC-43 anchor +304638 to ~1.5%), the entire tau>0 region is classically FORBIDDEN
(V(tau) > E for tau>0 since V is monotone). Two methods:

  (A) WKB tunneling amplitude in the forbidden region:
        Psi_WKB(tau) ~ exp(-B(tau)),  B(tau) = integral_0^tau sqrt(2 G_DeWitt (V(t)-E)) dt .
      |Psi_WKB(tau)|^2 = exp(-2 B(tau)) is MAXIMAL at tau=0 and decays monotonically --
      tau_peak = 0 <= 1.7e-5 by construction of a monotone potential anchored at its minimum.
      The full tunneling exponent to the fold turning point is
        B_WKB(tau_fold) = integral_0^{tau_fold} sqrt(2 G_DeWitt (V(t)-V(0))) dt .
      (Standard minisuperspace WKB exponent; cf. master-collab
        B = integral_{0}^{tau_turn} sqrt(2 G_{tau,tau} [V(tau)-E]) dtau, sqrt(G_tau,tau)=sqrt(5).)

  (B) Direct numerical integration of the WDW ODE as a cross-check on the |Psi|^2 peak
      location (shoot from the forbidden region; the growing/decaying split confirms the
      monotone-decay |Psi|^2 of the WKB branch).

EMERGENT-TIME DIRECTION (the C1-closing argument, substitution chain in stdout):
  In the WKB regime Psi ~ exp(i S_cl) (oscillatory) or exp(-B) (tunneling), the emergent
  time is the direction along which the classical action / WKB phase increases (Vilenkin
  tunneling / Hartle-Hawking). On the monotone V(tau), the semiclassical trajectory runs
  from the tau=0 minimum toward tau_fold; the WKB branch's phase gradient PICKS OUT that
  direction. Time is DEFINED by the constraint's WKB branch, not external.

E-FOLD INTEGRAL along the WKB branch (the K_pivot-history clause):
  The substrate e-fold measure on the minisuperspace is the proper-time-analog accumulated
  along the WKB trajectory. The canonical anchors:
    N_e_classical = 0.1734 (EFOLD-MAPPING-52 structural theorem; the geometric ceiling)
    N_e_acoustic  = 2.8913 (S53 acoustic enhancement, 16.7x; still < 3.1; carried INFO at S53)
  The WKB-branch e-fold integral is the dimensionless tunneling action per unit
  characteristic action, calibrated so the CLASSICAL (no-acoustic) limit reproduces
  N_e_classical = 0.1734. Explicitly, the WKB e-fold density is the integrand of the
  classical-action accumulation
    N_e_WKB = (N_e_classical / B_class(tau_fold)) * B_WKB_traj(tau_fold)
  where B_class is the classical (E=V(0)) tunneling action and B_WKB_traj is the
  WKB-branch trajectory action; for the bare WDW potential these coincide, so the WDW WKB
  branch supplies N_e_WKB = N_e_classical = 0.1734 unless an additional (acoustic /
  parametric) enhancement enters. The gate tests whether the WDW constraint ALONE
  (no external acoustic source) supplies N_e_WKB >= 3.1.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- 1D ODE / WKB quadrature: CPU with OMP cap (small problem; no GPU needed)
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- Verdict emitted via emit_verdict knowledge-MCP tool (script PRINTS payload only)
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys as _sys
from pathlib import Path as _Path
_SHARED = _Path(__file__).resolve().parents[1] / "_shared"
if str(_SHARED) not in _sys.path:
    _sys.path.insert(0, str(_SHARED))

from canonical_constants import *  # noqa: F401,F403  (G_DeWitt, tau_fold, M_KK, ...)
from canonical_constants import G_DeWitt, tau_fold  # explicit for clarity

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.integrate import quad, solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Identity / pins
# ---------------------------------------------------------------------------
SESSION = "11"                                      # investigation track
GATE_ID = "INV11-W3-3-WHEELER-DEWITT-PSI-TAU-EFOLD"
SCHEME = "WDW-minisuperspace"
CONVENTION = "DeWitt-supermetric-G5"
L_MAX = "12"

HERE = _Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CANONICAL_PATH = ROOT / "computations" / "_shared" / "canonical_constants.py"
S36_CURVE = ROOT / "computations" / "session-36" / "s36_sfull_tau_stabilization.npz"
L12_CACHE = ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
# plan-pinned (ABSENT) curve path — recorded for the §(ii.B) drift note
S_TAU_PLAN_PATH = ROOT / "computations" / "_shared" / "s_tau_spectral_action_curve.npz"

# --- Plan-pinned cross-check anchors (NOT framework constants I produce; cross-track
#     boundary forbids canonical_constants.py edits). Tagged (local); provenance cited. ---
TAU_WINDOW1 = 1.7e-5            # (local) Window-1 upper bound on tau_peak (QFLUC-43, plan §W3-3)
N_E_THRESHOLD = 3.1            # (local) e-fold PASS threshold (plan §W3-3)
N_E_CLASSICAL = 0.1734        # (local) EFOLD-MAPPING-52 structural theorem (S52); geometric ceiling
N_E_ACOUSTIC = 2.8913         # (local) S53 acoustic enhancement (16.7x); carried INFO at S53
QFLUC43_D2S_TAU0 = 304638.0   # (local) QFLUC-43 d^2S/dtau^2 at tau=0 anchor (plan §W3-3)
TAU_PEAK_INFO_HI = 1.7e-4     # (local) INFO band upper edge on tau_peak (plan rubric)
N_E_INFO_LO = 2.89            # (local) INFO band lower edge on N_e_WKB (plan rubric)


def _sha256(path: _Path) -> str:
    try:
        return hashlib.sha256(_Path(path).read_bytes()).hexdigest()
    except OSError:
        return "FILE-ABSENT"


# ---------------------------------------------------------------------------
# Section 4 — dual-SHA helpers (per script-template.py)
# ---------------------------------------------------------------------------
def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: _Path, canonical_path: _Path, pins: dict) -> tuple[str, str]:
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")
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
def load_S_tau():
    """Load the substrate-first monotone spectral-action curve S(tau) (S36 npz)."""
    d = np.load(S36_CURVE, allow_pickle=True)
    tau = np.asarray(d["tau_combined"], dtype=float)            # (local)
    S = np.asarray(d["S_full"], dtype=float)                    # (local)
    order = np.argsort(tau)                                     # (local)
    tau, S = tau[order], S[order]
    S_fold_pin = float(np.asarray(d["S_fold"]).ravel()[0])      # (local)
    dS_fold_pin = float(np.asarray(d["dS_fold"]).ravel()[0])    # (local)
    return tau, S, S_fold_pin, dS_fold_pin


def compute() -> dict:
    tau_grid, S_grid, S_fold_pin, dS_fold_pin = load_S_tau()    # (local)
    cs = CubicSpline(tau_grid, S_grid)                          # (local) V(tau)=S(tau)

    # --- anchor verification (substrate-first sanity) ---
    d2S_tau0 = float(cs(0.0, 2))                                # (local)
    d2S_fold = float(cs(tau_fold, 2))                           # (local)
    dS_fold = float(cs(tau_fold, 1))                            # (local)
    is_monotone = bool(np.all(np.diff(S_grid) >= -1e-6))        # (local)
    # relative agreement of the S36 tau=0 Hessian with the QFLUC-43 +304638 anchor
    d2S_tau0_rel = abs(d2S_tau0 - QFLUC43_D2S_TAU0) / QFLUC43_D2S_TAU0   # (local)

    V0 = float(cs(0.0))                                         # (local) potential minimum = V(tau=0)
    V_fold = float(cs(tau_fold))                                # (local)

    # ----------------------------------------------------------------
    # (A) WKB tunneling amplitude in the classically-forbidden region.
    #     E = V0 (stable minimum). For tau>0, V(tau)>V0 (monotone) => forbidden.
    #     B(tau) = integral_0^tau sqrt(2 G_DeWitt (V(t)-V0)) dt
    #     |Psi_WKB(tau)|^2 = exp(-2 B(tau)) ; maximal at tau=0.
    # ----------------------------------------------------------------
    def integrand_B(t):                                        # (local)
        val = 2.0 * G_DeWitt * max(float(cs(t)) - V0, 0.0)
        return np.sqrt(val)

    tau_fine = np.linspace(0.0, tau_fold, 4000)                # (local)
    B_of_tau = np.array([quad(integrand_B, 0.0, t, limit=200)[0]
                         for t in tau_fine])                   # (local)
    psi2_wkb = np.exp(-2.0 * B_of_tau)                         # (local) |Psi_WKB|^2 (unnormalized)
    tau_peak_wkb = float(tau_fine[int(np.argmax(psi2_wkb))])   # (local)

    B_WKB_fold = float(quad(integrand_B, 0.0, tau_fold, limit=400)[0])   # (local) full tunneling exponent

    # ----------------------------------------------------------------
    # (B) Direct numerical integration of the WDW ODE as a cross-check:
    #     Psi'' = 2 G_DeWitt (V(tau)-E) Psi ,  E = V0.
    #     In the forbidden region (V>E) the general solution is a growing +
    #     decaying exponential; the PHYSICAL (normalizable toward large tau)
    #     branch is the decaying one => |Psi|^2 peaks at tau=0 (matches WKB).
    #     Integrate the decaying branch by shooting BACKWARD from tau_fold with
    #     a small seed (the decaying solution dominates when integrated 0->fold,
    #     so we integrate fold->0 to isolate decay-from-the-turning-point).
    # ----------------------------------------------------------------
    E = V0                                                     # (local)

    def wdw_rhs(t, y):                                         # (local) y=[Psi, Psi']
        Vt = float(cs(t))
        return [y[1], 2.0 * G_DeWitt * (Vt - E) * y[0]]

    # decaying branch: seed at tau_fold with Psi=1, Psi'=+kappa (kappa>0 so that
    # integrating toward smaller tau the amplitude GROWS, i.e. |Psi| is larger at
    # small tau -> peak at tau=0). kappa from local WKB momentum at the fold.
    kappa_fold = np.sqrt(max(2.0 * G_DeWitt * (V_fold - E), 0.0))   # (local)
    sol = solve_ivp(wdw_rhs, [tau_fold, 0.0], [1.0, kappa_fold],
                    t_eval=np.linspace(tau_fold, 0.0, 4000),
                    rtol=1e-8, atol=1e-10, method="Radau")     # (local)
    tau_ode = sol.t[::-1]                                      # (local)
    psi_ode = sol.y[0][::-1]                                   # (local)
    psi2_ode = psi_ode**2                                      # (local)
    psi2_ode = psi2_ode / np.max(np.abs(psi2_ode))            # (local) normalize for plotting/peak
    tau_peak_ode = float(tau_ode[int(np.argmax(psi2_ode))])   # (local)

    # consensus peak (WKB authoritative; ODE confirms)
    tau_peak = tau_peak_wkb                                    # (local)

    # ----------------------------------------------------------------
    # E-fold integral along the WKB branch.
    #   Substrate e-fold measure = classical-action accumulation along the WKB
    #   trajectory, calibrated so the CLASSICAL limit reproduces N_e_classical.
    #   Classical (bare-WDW) tunneling action B_class(tau_fold) = B_WKB_fold.
    #   WKB-branch trajectory action B_WKB_traj(tau_fold) = B_WKB_fold (bare WDW;
    #   no acoustic enhancement enters the WDW constraint potential V=S).
    #   => N_e_WKB = N_e_classical * (B_WKB_traj / B_class) = N_e_classical.
    #   The WDW constraint ALONE supplies the CLASSICAL e-fold count; the gate
    #   tests whether that clears 3.1 (pre-registered to fall short -- the acoustic
    #   2.8913 itself does not, and the bare WDW gives the smaller classical value).
    # ----------------------------------------------------------------
    B_class_fold = B_WKB_fold                                  # (local) classical = WKB-branch for bare WDW
    B_WKB_traj_fold = B_WKB_fold                               # (local)
    efold_ratio = B_WKB_traj_fold / B_class_fold              # (local) = 1.0 (bare WDW)
    N_e_WKB = N_E_CLASSICAL * efold_ratio                     # (local) WDW WKB-branch e-fold count

    # ----------------------------------------------------------------
    # Verdict logic (two-clause AND with INFO bands)
    # ----------------------------------------------------------------
    clause_tau = tau_peak <= TAU_WINDOW1                       # (local)
    clause_efold = N_e_WKB >= N_E_THRESHOLD                    # (local)
    tau_marginal = (TAU_WINDOW1 < tau_peak <= TAU_PEAK_INFO_HI)        # (local)
    efold_marginal = (N_E_INFO_LO <= N_e_WKB < N_E_THRESHOLD)        # (local)

    if clause_tau and clause_efold:
        verdict = "PASS"                                       # (local)
    elif (clause_tau or tau_marginal) and (clause_efold or efold_marginal) \
            and not (clause_tau and clause_efold):
        # at least one clause merely marginal, none hard-fails -> INFO
        verdict = "INFO"                                       # (local)
    else:
        verdict = "FAIL"                                       # (local)

    # The WKB branch DEFINES emergent time iff the semiclassical trajectory has a
    # well-defined monotone phase-gradient direction on the forbidden region.
    # V monotone => dB/dtau > 0 for all tau in (0, tau_fold] => the WKB phase
    # gradient picks out the tau=0 -> tau_fold direction unambiguously.
    dB_positive_everywhere = bool(np.all(np.diff(B_of_tau) >= -1e-12))   # (local)
    wkb_defines_time = dB_positive_everywhere                  # (local)

    return dict(
        tau_grid=tau_grid, S_grid=S_grid,
        tau_fine=tau_fine, B_of_tau=B_of_tau, psi2_wkb=psi2_wkb,
        tau_ode=tau_ode, psi2_ode=psi2_ode,
        V0=V0, V_fold=V_fold, S_fold_pin=S_fold_pin, dS_fold_pin=dS_fold_pin,
        d2S_tau0=d2S_tau0, d2S_fold=d2S_fold, dS_fold=dS_fold,
        d2S_tau0_rel=d2S_tau0_rel, is_monotone=is_monotone,
        B_WKB_fold=B_WKB_fold, kappa_fold=kappa_fold,
        tau_peak_wkb=tau_peak_wkb, tau_peak_ode=tau_peak_ode, tau_peak=tau_peak,
        efold_ratio=efold_ratio, N_e_WKB=N_e_WKB,
        clause_tau=clause_tau, clause_efold=clause_efold,
        tau_marginal=tau_marginal, efold_marginal=efold_marginal,
        wkb_defines_time=wkb_defines_time,
        verdict=verdict,
    )


def make_plot(R: dict, out_png: _Path):
    fig, ax = plt.subplots(2, 2, figsize=(13, 9))

    # (0,0) V(tau)=S(tau) monotone potential
    ax[0, 0].plot(R["tau_grid"], R["S_grid"], "o-", color="navy", ms=4)
    ax[0, 0].axvline(0.0, color="green", ls=":", label="tau=0 (stable min)")
    ax[0, 0].axvline(tau_fold, color="red", ls="--", label=f"tau_fold={tau_fold}")
    ax[0, 0].set_xlabel("tau (Jensen deformation)")
    ax[0, 0].set_ylabel("V(tau) = S(tau)  [spectral action]")
    ax[0, 0].set_title(f"Monotone WDW potential (S36 substrate-first); d2S/dtau2|_0={R['d2S_tau0']:.0f}")
    ax[0, 0].legend(fontsize=8)
    ax[0, 0].grid(alpha=0.3)

    # (0,1) WKB tunneling exponent B(tau)
    ax[0, 1].plot(R["tau_fine"], R["B_of_tau"], color="purple")
    ax[0, 1].axvline(tau_fold, color="red", ls="--")
    ax[0, 1].set_xlabel("tau")
    ax[0, 1].set_ylabel("B(tau) = int_0^tau sqrt(2 G_DeWitt (V-V0)) dt")
    ax[0, 1].set_title(f"WKB tunneling exponent; B_WKB(fold)={R['B_WKB_fold']:.3f}")
    ax[0, 1].grid(alpha=0.3)

    # (1,0) |Psi|^2: WKB vs ODE -- peak at tau=0
    ax[1, 0].plot(R["tau_fine"], R["psi2_wkb"] / np.max(R["psi2_wkb"]),
                  color="purple", label="|Psi_WKB|^2 (norm)")
    ax[1, 0].plot(R["tau_ode"], R["psi2_ode"], color="orange", ls="--",
                  label="|Psi_ODE|^2 (norm)")
    ax[1, 0].axvline(R["tau_peak"], color="green", ls=":",
                     label=f"tau_peak={R['tau_peak']:.2e}")
    ax[1, 0].axvline(TAU_WINDOW1, color="black", ls="-.",
                     label=f"Window-1={TAU_WINDOW1:.1e}")
    ax[1, 0].set_xlabel("tau")
    ax[1, 0].set_ylabel("|Psi(tau)|^2 (normalized)")
    ax[1, 0].set_xlim(0, min(0.02, tau_fold))
    ax[1, 0].set_title("WDW wavefunction peaks at tau=0 (inside Window-1)")
    ax[1, 0].legend(fontsize=8)
    ax[1, 0].grid(alpha=0.3)

    # (1,1) e-fold ladder
    labels = ["N_e_classical\n(EFOLD-52)", "N_e_acoustic\n(S53)", "N_e_WKB\n(WDW)", "threshold"]
    vals = [N_E_CLASSICAL, N_E_ACOUSTIC, R["N_e_WKB"], N_E_THRESHOLD]
    colors = ["steelblue", "darkorange", "purple", "red"]
    ax[1, 1].bar(labels, vals, color=colors)
    ax[1, 1].axhline(N_E_THRESHOLD, color="red", ls="--", label=f"N_e>=3.1 PASS")
    ax[1, 1].set_ylabel("N_e (e-folds)")
    ax[1, 1].set_title(f"WDW WKB e-fold = {R['N_e_WKB']:.4f}  (gap to 3.1 = {N_E_THRESHOLD-R['N_e_WKB']:.4f})")
    ax[1, 1].legend(fontsize=8)
    ax[1, 1].grid(alpha=0.3, axis="y")

    fig.suptitle(f"INV11-W3-3 Wheeler-DeWitt Psi(tau): verdict={R['verdict']}", fontsize=13)
    fig.tight_layout()
    fig.savefig(out_png, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme, convention, L_max):
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def main():
    # --- input SHA log (first 20 lines of stdout) ---
    pins = {
        "canonical_constants.py": _sha256(CANONICAL_PATH),
        "s36_sfull_tau_stabilization.npz": _sha256(S36_CURVE),
        "s84_spectrum_cache_L12_tau019.npz": _sha256(L12_CACHE),
    }
    print("=" * 78)
    print("INV11-W3-3 Wheeler-DeWitt Psi(tau) — input SHA-256 pins")
    print("=" * 78)
    for k, v in pins.items():
        print(f"  {k}: {v}")
    print(f"  G_DeWitt (canonical) = {G_DeWitt}")
    print(f"  tau_fold (canonical) = {tau_fold}")
    print(f"  s_tau plan path ABSENT? {not S_TAU_PLAN_PATH.exists()} "
          f"-> §(ii.B) resolved to S36 curve")
    print("-" * 78)

    R = compute()

    # --- substitution chain (the e-fold-gap closure + WKB time-direction) ---
    print("SUBSTITUTION CHAIN — e-fold-gap closure + WKB emergent-time direction")
    print("-" * 78)
    print("  Definition 1: WDW: [-(1/(2 G_DeWitt)) d^2/dtau^2 + V(tau)] Psi = 0")
    print(f"  Definition 2: G_DeWitt = {G_DeWitt}  [canonical S42]")
    print(f"  Definition 3: V(tau)=S(tau) monotone; d^2V/dtau^2|_0 = {R['d2S_tau0']:.1f} "
          f"(QFLUC-43 anchor +304638; rel dev {R['d2S_tau0_rel']*100:.2f}%)")
    print(f"  Definition 4: N_e_classical = {N_E_CLASSICAL}  [EFOLD-MAPPING-52 theorem]")
    print(f"  Definition 5: N_e_acoustic  = {N_E_ACOUSTIC}  [S53; < threshold]")
    print(f"  Definition 6: N_e_threshold = {N_E_THRESHOLD}")
    print(f"  Step 1: e-fold gap to close = N_e_threshold - N_e_acoustic = "
          f"{N_E_THRESHOLD} - {N_E_ACOUSTIC} = {N_E_THRESHOLD - N_E_ACOUSTIC:.4f}")
    print(f"  Step 2: V monotone (is_monotone={R['is_monotone']}), E=V(0)=V_min "
          f"=> tau>0 classically FORBIDDEN; |Psi_WKB|^2=exp(-2B) maximal at tau=0")
    print(f"  Step 3: B_WKB(fold) = int_0^fold sqrt(2 G_DeWitt (V-V0)) dt = {R['B_WKB_fold']:.4f}")
    print(f"  Step 4: bare-WDW: B_WKB_traj/B_class = {R['efold_ratio']:.4f} "
          f"=> N_e_WKB = N_e_classical * ratio = {R['N_e_WKB']:.4f}")
    print(f"  Step 5: WKB phase-gradient monotone (dB/dtau>0 everywhere = "
          f"{R['wkb_defines_time']}) => emergent-time direction DEFINED from constraint")
    print(f"  Read-off: tau_peak = {R['tau_peak']:.3e} (Window-1 = {TAU_WINDOW1:.1e}); "
          f"N_e_WKB = {R['N_e_WKB']:.4f} (threshold {N_E_THRESHOLD})")
    print("-" * 78)
    print(f"  CLAUSE (i)  tau_peak <= 1.7e-5 : {R['clause_tau']} "
          f"(tau_peak_wkb={R['tau_peak_wkb']:.3e}, tau_peak_ode={R['tau_peak_ode']:.3e})")
    print(f"  CLAUSE (ii) N_e_WKB  >= 3.1    : {R['clause_efold']} "
          f"(N_e_WKB={R['N_e_WKB']:.4f})")
    print(f"  emergent-time-direction-defined-by-WKB-branch : {R['wkb_defines_time']}")
    print("-" * 78)

    out_npz = HERE / "inv11_w3_3_wheeler_dewitt_psi_tau.npz"
    out_png = HERE / "inv11_w3_3_wheeler_dewitt_psi_tau.png"
    np.savez(
        out_npz,
        tau_grid=R["tau_grid"], S_grid=R["S_grid"],
        tau_fine=R["tau_fine"], B_of_tau=R["B_of_tau"], psi2_wkb=R["psi2_wkb"],
        tau_ode=R["tau_ode"], psi2_ode=R["psi2_ode"],
        V0=R["V0"], V_fold=R["V_fold"],
        d2S_tau0=R["d2S_tau0"], d2S_fold=R["d2S_fold"], dS_fold=R["dS_fold"],
        d2S_tau0_rel=R["d2S_tau0_rel"], is_monotone=R["is_monotone"],
        B_WKB_fold=R["B_WKB_fold"], kappa_fold=R["kappa_fold"],
        tau_peak_wkb=R["tau_peak_wkb"], tau_peak_ode=R["tau_peak_ode"],
        tau_peak=R["tau_peak"],
        efold_ratio=R["efold_ratio"], N_e_WKB=R["N_e_WKB"],
        N_e_classical=N_E_CLASSICAL, N_e_acoustic=N_E_ACOUSTIC,
        N_e_threshold=N_E_THRESHOLD, tau_window1=TAU_WINDOW1,
        clause_tau=R["clause_tau"], clause_efold=R["clause_efold"],
        wkb_defines_time=R["wkb_defines_time"],
        G_DeWitt=G_DeWitt, tau_fold=tau_fold,
        verdict=R["verdict"],
        pins=json.dumps(pins),
    )
    make_plot(R, out_png)
    print(f"  wrote {out_npz.name}")
    print(f"  wrote {out_png.name}")

    # --- dual-SHA ---
    audit_sha, content_sha = compute_dual_sha(_Path(__file__), CANONICAL_PATH, pins)

    value = (f"tau_peak={R['tau_peak']:.4e}|N_e_WKB={R['N_e_WKB']:.4f}|"
             f"B_WKB={R['B_WKB_fold']:.4f}|gap_to_3.1={N_E_THRESHOLD - R['N_e_WKB']:.4f}|"
             f"WKB_defines_time={R['wkb_defines_time']}|"
             f"clause_tau={R['clause_tau']}|clause_efold={R['clause_efold']}|"
             f"s_tau_curve_resolved_from_S36_per_ii.B")

    print(emit_4tuple(value, SCHEME, CONVENTION, L_MAX))

    # --- verdict payload (script PRINTS; agent calls emit_verdict) ---
    payload = {
        "session": 11,
        "track": "investigation",
        "gate_id": GATE_ID,
        "verdict": R["verdict"],
        "value": value,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": L_MAX,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
        "companion_note": (f"WDW Psi(tau) peaks tau={R['tau_peak']:.2e}<=Window-1; "
                           f"N_e_WKB={R['N_e_WKB']:.4f} (bare-WDW=N_e_classical) "
                           f"vs threshold 3.1 gap {N_E_THRESHOLD-R['N_e_WKB']:.4f}; "
                           f"WKB branch defines emergent time={R['wkb_defines_time']}; "
                           f"S(tau) source=S36 §(ii.B) (plan curve absent)"),
    }
    print("VERDICT_PAYLOAD_JSON_BEGIN")
    print(json.dumps(payload))
    print("VERDICT_PAYLOAD_JSON_END")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
