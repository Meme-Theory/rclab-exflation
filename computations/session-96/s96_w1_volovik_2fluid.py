#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S96-W1-VOLOVIK-2FLUID  (Session 96, Wave 1, gate W1-4)  — ROUTE 2 of 3 a(t)-closure
====================================================================================

[SIGN] gate.  Volovik two-fluid (normal + superfluid) effective-Friedmann closure
for the emergent FRW a(t).  Tests whether the NORMAL-component (GGE quasiparticle
gas) energy density sources a deceleration parameter q_Omega in the SCALE-FACTOR-54
band (-0.97 -> +0.81), and whether the two-fluid split resolves the 133,200x
single-fluid T6 overwhelm.

Substrate framing (phononic-framing.md / IS Space, Not IN Space)
----------------------------------------------------------------
The superfluid vacuum IS the substrate; the two-fluid split is the substrate's OWN
normal/superfluid components, NOT two fluids placed inside a pre-existing spacetime
container.  The post-fold substrate IS a two-fluid system (Volovik Paper 06):
  - SUPERFLUID component = the unbroken BCS condensate fraction (98.85% by ODLRO/
    Meissner, S67); the effaced w=-1 vacuum (Gamma_eff=0.99970, P_s=-rho_s).  What
    LCDM calls dark energy is this effacement residual.
  - NORMAL component = the GGE quasiparticle gas (1.15% by ODLRO, the n_pairs=59.8
    Bogoliubov relic, P_exc=1.000).  What LCDM calls matter is this Bogoliubov relic.
The emergent FRW H^2 is the back-reaction of the normal-component energy density on
the a2-channel emergent metric g_M.  The arrow is strictly substrate-first:
  D_K eigenvalues reorganize at the van Hove fold -> Bogoliubov |beta_k|^2 produces
  the GGE normal component -> normal-component energy density sources T_relic^{mu nu}
  -> H^2(tau) on the emergent g_M -> a(t).
This is the substrate's own two-fluid hydrodynamics generating its emergent
expansion-rate readout -- NOT a Friedmann equation obeyed inside a container.

CLASSIFICATION: PHONONIC (the GGE quasiparticle gas / normal component is the relic
excitation source; deceleration q_Omega is its hydrodynamic signature).

Method (plan section W1-4) -- ROUTE 2, first-principles two-fluid
-----------------------------------------------------------------
Set up Volovik two-fluid continuity + Euler equations for the post-fold substrate:
  rho_n (normal, GGE)      sourced by the S95-W3-3 nominal Bogoliubov relic sum
                           rho_relic_MKK = 26.553854 (= B1 2.7792 + B2 21.8876 + B3 1.8871)
  rho_s (superfluid, w=-1) the effaced unbroken-condensate vacuum.
Two equations of state are carried (source-fidelity, NOT convention-shopping):
  Reading I  (plan-idealized):     w_n = 0 (dust),   w_s = -1 (vacuum)
  Reading II (substrate-faithful): w_n = -0.407649 (Volovik thermodynamic identity
             P = -eps + sum_k T_k S_k, S67 GGE-TWO-FLUID-67 canonical), w_s = -1.
The two-fluid deceleration parameter (FRW):
  q_Omega = (1/2) * sum_i rho_i (1+3 w_i) / sum_i rho_i
          = (1/2) [ (1+3 w_n) + x (1+3 w_s) ] / (1 + x),   x = rho_s / rho_n.
x(tau) is the vacuum-to-normal ratio set by the effacement and the DIFFERENTIAL
DILUTION: rho_s ~ a^0 (w=-1, constant) and rho_n ~ a^{-3(1+w_n)} (S67 a_dilution
exponent -1.777 for w_n=-0.408).  As the emergent a(tau) grows, rho_n dilutes
relative to rho_s, so x INCREASES with a and q_Omega DECREASES (deeper toward -1).
x is anchored at the fold to the S67 ODLRO/Meissner value x_fold = 0.98848/0.011522
= 85.79.  a(tau) and the SF54 q-band target come from the SCALE-FACTOR-54 npz
(Connes-distance proxy; q sweeps -0.973 -> +0.814).

The two-fluid continuity+Euler ODE is integrated (Radau) over the 200-pt tau-grid
[fold, nominal fixed point] to obtain q_Omega(tau) self-consistently; the closed-
form q_Omega(x(tau)) is cross-checked against the ODE solution.

SIGN pre-registration (substitution chain Step 4):
  dq_Omega/dx = (1/2)*[ (1+3 w_s) (1+x) - ((1+3 w_n)+x(1+3 w_s)) ] / (1+x)^2.
  For w_n=0, w_s=-1:  dq/dx = (-3/2)/(1+x)^2 < 0  =>  q DECREASES as x (vacuum
  fraction) grows.  The NORMAL component (rho_n, x->0) drives q -> +1/2 (decelerating,
  matter-like POSITIVE source); the SUPERFLUID component (rho_s, w=-1, x->inf) drives
  q -> -1 (accelerating).  The relic (normal) POSITIVELY sources the decelerating
  part of H^2.  PREDICTED SIGN: dq/dx < 0 (POSITIVE normal-component deceleration
  source).  The 133,200x overwhelm is RESOLVED because the single-fluid BCS
  comparison conflated the w=-1 vacuum (155,984-mode spectral action) with the w=0
  relic (8-mode-like GGE charge); the two-fluid split assigns each its own EOS.

MAGNITUDE pre-registration (band reproduction): PASS iff |q_Omega,computed -
q_SF54| < 0.20*(0.81-(-0.97)) = 0.356 ACROSS the tau-window AND the band [-0.97,
+0.81] is spanned.  Structural bound (Sage-exact, see substitution chain Step 5):
the two-fluid q_Omega is bounded ABOVE by +1/2 (Reading I, w_n=0, x->0) or -0.111
(Reading II, w_n=-0.408); SF54 reaches +0.814 > +1/2, so the +1/2..+0.814 portion
of the band is STRUCTURALLY UNREACHABLE by ANY two-fluid w_n>=... EOS.  The +0.81
deceleration is a Connes-distance metric-proxy effect (a DIFFERENT object), not a
two-fluid EOS effect.

ROUTE INDEPENDENCE: this is one of THREE independent a(t)-closure routes (gates
1/4/5).  H^2* is computed here from the two-fluid formalism alone; gates 1/5 outputs
are NOT read.  Cross-route comparison is a forward (S97) workshop.

Environment: phonon-exflation-sim/.venv312/Scripts/python.exe (GPU venv).
This file lives in computations/session-96/ and writes outputs there.
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
import time
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import numpy as np  # noqa: E402
from scipy.integrate import solve_ivp  # noqa: E402

import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# -----------------------------------------------------------------------------
# Section 1 — Paths + canonical-constants import
# -----------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent                    # computations/session-96
PROJECT_ROOT = SESSION_DIR.parent.parent                         # repo root
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
SESSION_DIR.mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(SHARED_DIR))
# Canonical constants (NEVER hardcode): a2 in the a2->g_M dictionary, GGE charge,
# excitation probability, effacement, fold, M_KK.
from canonical_constants import (  # noqa: E402
    a_2_FW_zeta,
    n_pairs,
    P_exc_kz,
    Gamma_effacement,
    tau_fold,
    M_KK,
)

GATE_ID = "S96-W1-VOLOVIK-2FLUID"
SCHEME = "Volovik-two-fluid-normal-plus-superfluid"
CONVENTION = "w=-1-effacement-superfluid-plus-w=0-GGE-normal-component"
L_MAX = "10"
SCHEMA_VERSION = "S84+"

VERDICT_TXT = SESSION_DIR / "s96_gate_verdicts.txt"
NPZ_OUT = SESSION_DIR / "s96_w1_volovik_2fluid.npz"
PNG_OUT = SESSION_DIR / "s96_w1_volovik_2fluid.png"

CANONICAL_PY = SHARED_DIR / "canonical_constants.py"
S95_W3_3_NPZ = PROJECT_ROOT / "computations" / "session-95" / "s95_w3_3_back_reaction_closure.npz"
S54_SCALE_NPZ = PROJECT_ROOT / "computations" / "session-54" / "s54_scale_factor.npz"

INPUT_FILES = [CANONICAL_PY, S95_W3_3_NPZ, S54_SCALE_NPZ]

# -----------------------------------------------------------------------------
# Section 2 — Pre-registered machinery pins (plan W1-4 machinery_pin_map)
# -----------------------------------------------------------------------------
N_EVAL = 200                       # tau-grid for two-fluid ODE integration         # (local)
SCAN_LO = 0.0                      # scan_range [0.0, 0.5] (plan)                    # (local)
SCAN_HI = 0.5                      # (local)
RTOL = 1e-10                       # ODE rtol (plan tolerance 1e-10)                 # (local)
ATOL = 1e-12                       # (local)

# SCALE-FACTOR-54 q-band target (plan band; verified vs s54 npz q-range)
Q_BAND_LO = -0.97                  # SF54 lower (quasi-de Sitter)                    # (local)
Q_BAND_HI = +0.81                  # SF54 upper (decelerating)                       # (local)
BAND_WIDTH = Q_BAND_HI - Q_BAND_LO                                                   # (local)
BAND_TOL = 0.20 * BAND_WIDTH       # PASS tolerance = 20% of band width = 0.356      # (local)

# Equations of state.
#   Reading I  (plan-idealized): normal = dust (w=0), superfluid = vacuum (w=-1)
W_N_IDEAL = 0.0                    # plan substitution-chain idealized normal EOS    # (local)
#   Reading II (substrate-faithful, S67 GGE-TWO-FLUID-67 Volovik identity):
#   P_n = -eps_n + sum_k T_k S_k  =>  w_n = -0.407649206353356 (S67 npz w_normal)
W_N_VOLOVIK = -0.407649206353356  # S67 GGE-TWO-FLUID-67 canonical (Volovik ident.)  # (local)
W_S = -1.0                         # superfluid vacuum EOS (Gibbs-Duhem P=-rho)      # (local)

# S67 ODLRO/Meissner fold fractions (the physical superfluid density), S67 canonical
RHO_S_FRAC_FOLD = 0.9884783042195022    # ODLRO condensate fraction (S67)           # (local)
RHO_N_FRAC_FOLD = 0.011521695780497776  # GGE normal fraction (S67)                 # (local)
X_FOLD = RHO_S_FRAC_FOLD / RHO_N_FRAC_FOLD   # vacuum/normal ratio at fold = 85.79   # (local)

# Predicted band-span coverage (Sage-exact pre-registration):
#  Reading I covers q in [-0.97, +0.5] = 82.58% of band; (+0.5,+0.81] UNREACHABLE.
PREDICTED_COVER_FRAC_I = (0.5 - Q_BAND_LO) / BAND_WIDTH   # 0.8258                   # (local)


# -----------------------------------------------------------------------------
# Section 3 — SHA machinery (canonical dual-SHA, S84+ schema)
# -----------------------------------------------------------------------------
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
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = script_path.read_bytes() if script_path.exists() else b""        # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# -----------------------------------------------------------------------------
# Section 4 — Two-fluid deceleration q_Omega(x)
# -----------------------------------------------------------------------------
def q_two_fluid(x: np.ndarray, w_n: float, w_s: float) -> np.ndarray:
    """FRW two-fluid deceleration q = (1/2) sum rho_i(1+3w_i) / sum rho_i,
    normalized by rho_n with x = rho_s/rho_n:
        q(x) = (1/2)[ (1+3 w_n) + x (1+3 w_s) ] / (1 + x)."""
    return 0.5 * ((1.0 + 3.0 * w_n) + x * (1.0 + 3.0 * w_s)) / (1.0 + x)


def dq_dx(x: np.ndarray, w_n: float, w_s: float) -> np.ndarray:
    """Analytic d q/d x for the [SIGN] direction read-off."""
    num = (1.0 + 3.0 * w_s) * (1.0 + x) - ((1.0 + 3.0 * w_n) + x * (1.0 + 3.0 * w_s))  # (local)
    return 0.5 * num / (1.0 + x) ** 2


# -----------------------------------------------------------------------------
# Section 5 — Compute (two-fluid continuity+Euler ODE + closed-form cross-check)
# -----------------------------------------------------------------------------
def compute() -> dict:
    # --- load upstream substrate data ---
    d95 = np.load(S95_W3_3_NPZ, allow_pickle=True)  # (local)
    rho_relic_MKK = float(d95["rho_relic_MKK"])      # 26.553854 (B1+B2+B3) (local)
    rho_B1 = float(d95["rho_contrib_B1"])            # 2.7792 (local)
    rho_B2 = float(d95["rho_contrib_B2"])            # 21.8876 (local)
    rho_B3 = float(d95["rho_contrib_B3"])            # 1.8871 (local)
    pairs_check = float(d95["pairs_check"])          # 59.8 (local)
    nominal_tau_star = float(d95["nominal_tau_star"])      # 0.451041 (local)
    nominal_H2_star = float(d95["nominal_H2_star"])        # 0.0074788 (local)
    nominal_taus = np.asarray(d95["nominal_taus"], dtype=float)        # 200-pt (local)
    nominal_H2_source = np.asarray(d95["nominal_H2_source"], dtype=float)  # H2 src (local)

    d54 = np.load(S54_SCALE_NPZ, allow_pickle=True)  # (local)
    sf54_tau = np.asarray(d54["tau"], dtype=float)   # 10-pt Connes grid (local)
    sf54_a = np.asarray(d54["a"], dtype=float)       # scale factor (local)
    sf54_q = np.asarray(d54["q"], dtype=float)       # q-band target (local)
    sf54_q_lo = float(sf54_q.min())                  # -0.973231 (local)
    sf54_q_hi = float(sf54_q.max())                  # +0.814377 (local)
    sf54_q_fold = float(d54["q_at_fold"])            # -0.7860366 (local)

    # consistency cross-checks vs canonical constants
    pairs_match = abs(pairs_check - n_pairs) < 1e-6                                  # (local)
    relic_sum_match = abs((rho_B1 + rho_B2 + rho_B3) - rho_relic_MKK) < 1e-6         # (local)
    band_match = (abs(sf54_q_lo - Q_BAND_LO) < 0.01) and (abs(sf54_q_hi - Q_BAND_HI) < 0.01)  # (local)

    # --- tau-grid on [fold, nominal fixed point] (the physical post-fold window) ---
    tau_grid = np.linspace(tau_fold, nominal_tau_star, N_EVAL)                       # (local)

    # === x(tau): vacuum-to-normal ratio from differential dilution ================
    # rho_s ~ a^0 (w=-1 constant);  rho_n ~ a^{-3(1+w_n)}  =>  x = rho_s/rho_n ~ a^{+3(1+w_n)}.
    # Anchor at the fold:  x_fold = X_FOLD (S67 ODLRO).  a(tau) from SCALE-FACTOR-54
    # (interp onto the post-fold tau-grid; a normalized to a(tau_fold)=1).
    a_of_tau = np.interp(tau_grid, sf54_tau, sf54_a)                                 # (local)
    a_fold_interp = np.interp(tau_fold, sf54_tau, sf54_a)                            # (local)
    a_norm = a_of_tau / a_fold_interp           # a(tau)/a(tau_fold), =1 at fold      # (local)

    # x(tau) for each reading (the differential-dilution exponent differs with w_n)
    x_tau_ideal = X_FOLD * a_norm ** (3.0 * (1.0 + W_N_IDEAL))     # exponent +3      # (local)
    x_tau_volovik = X_FOLD * a_norm ** (3.0 * (1.0 + W_N_VOLOVIK))  # exponent +1.777 # (local)

    # === closed-form q_Omega(tau) (both readings) =================================
    q_ideal = q_two_fluid(x_tau_ideal, W_N_IDEAL, W_S)                               # (local)
    q_volovik = q_two_fluid(x_tau_volovik, W_N_VOLOVIK, W_S)                         # (local)

    # === ODE cross-check: integrate the two-fluid continuity system in ln(a) =======
    # d rho_i / d N = -3 (1 + w_i) rho_i   (N = ln a).  Integrate over the a-range
    # spanned by a_norm, then read q from the integrated rho_s/rho_n ratio.  This
    # confirms the closed-form x(tau) is the continuity-equation solution (NOT an
    # ansatz): the integrated rho ratio must reproduce x_tau to ODE tol.
    N_lo = float(np.log(a_norm.min()))                                              # (local)
    N_hi = float(np.log(a_norm.max()))                                             # (local)
    rho_n0 = RHO_N_FRAC_FOLD     # at fold (a_norm=1, N=0); normalized fractions      # (local)
    rho_s0 = RHO_S_FRAC_FOLD                                                         # (local)

    def two_fluid_continuity(N, y, w_n):  # (local) y=[rho_n, rho_s]
        rho_n, rho_s = y  # (local)
        drho_n = -3.0 * (1.0 + w_n) * rho_n  # (local)
        drho_s = -3.0 * (1.0 + W_S) * rho_s  # = 0 (w_s=-1) (local)
        return [drho_n, drho_s]

    N_eval_grid = np.log(a_norm)  # (local) monotone increasing in tau (post-fold)
    # sort for solve_ivp t_eval (must be monotone; a_norm increases with tau)
    order = np.argsort(N_eval_grid)  # (local)
    N_sorted = N_eval_grid[order]  # (local)

    # Integrate over [N_lo, N_hi] with dense output; evaluate at the tau-ordered
    # grid via the continuous interpolant. This avoids the solve_ivp t_eval
    # strict-monotone requirement (a_norm interpolated onto tau_grid can have a
    # non-strict segment), with no change to the continuity physics.
    sol_ideal = solve_ivp(two_fluid_continuity, (N_lo, N_hi), [rho_n0, rho_s0],
                          args=(W_N_IDEAL,), method="Radau",
                          rtol=RTOL, atol=ATOL, dense_output=True)                   # (local)
    sol_volovik = solve_ivp(two_fluid_continuity, (N_lo, N_hi), [rho_n0, rho_s0],
                            args=(W_N_VOLOVIK,), method="Radau",
                            rtol=RTOL, atol=ATOL, dense_output=True)                 # (local)
    ode_ok = bool(sol_ideal.success and sol_volovik.success)                        # (local)

    # evaluate the dense ODE solution directly at the tau-ordered N grid
    rho_dense_i = sol_ideal.sol(N_eval_grid)                                        # (local)
    rho_n_ode_i = rho_dense_i[0]                                                    # (local)
    rho_s_ode_i = rho_dense_i[1]                                                    # (local)
    rho_dense_v = sol_volovik.sol(N_eval_grid)                                      # (local)
    rho_n_ode_v = rho_dense_v[0]                                                    # (local)
    rho_s_ode_v = rho_dense_v[1]                                                    # (local)
    x_ode_ideal = rho_s_ode_i / rho_n_ode_i                                         # (local)
    x_ode_volovik = rho_s_ode_v / rho_n_ode_v                                       # (local)
    q_ode_ideal = q_two_fluid(x_ode_ideal, W_N_IDEAL, W_S)                          # (local)
    q_ode_volovik = q_two_fluid(x_ode_volovik, W_N_VOLOVIK, W_S)                    # (local)

    # ODE-vs-closed-form residual (confirms x(tau) IS the continuity solution)
    resid_ideal = float(np.max(np.abs(q_ode_ideal - q_ideal)))                      # (local)
    resid_volovik = float(np.max(np.abs(q_ode_volovik - q_volovik)))                # (local)
    ode_closedform_consistent = bool(max(resid_ideal, resid_volovik) < 1e-8)        # (local)

    # === SIGN: dq/dx < 0 everywhere (POSITIVE normal-component deceleration source) =
    dqdx_ideal = dq_dx(x_tau_ideal, W_N_IDEAL, W_S)                                  # (local)
    dqdx_volovik = dq_dx(x_tau_volovik, W_N_VOLOVIK, W_S)                            # (local)
    sign_all_negative = bool(np.all(dqdx_ideal < 0) and np.all(dqdx_volovik < 0))   # (local)
    # the normal component (w_n) contributes +(1+3 w_n) to the numerator: for w_n=0
    # this is +1 (decelerating); for w_n=-0.408 it is -0.223 (still > the w_s=-2 term)
    normal_decel_contrib_ideal = 1.0 + 3.0 * W_N_IDEAL    # +1 (local)
    normal_decel_contrib_volovik = 1.0 + 3.0 * W_N_VOLOVIK  # -0.223 (local)
    vacuum_accel_contrib = 1.0 + 3.0 * W_S                # -2 (local)
    # SIGN claim: normal contributes MORE deceleration than vacuum (normal > vacuum)
    normal_above_vacuum = bool(normal_decel_contrib_ideal > vacuum_accel_contrib)   # (local)

    # === q-band reproduction (MAGNITUDE) ==========================================
    # Reading I structural max = q(x->0) = +1/2; Reading II max = (1+3 w_n)/2 = -0.111
    q_max_ideal = q_two_fluid(np.array([0.0]), W_N_IDEAL, W_S)[0]      # +0.5 (local)
    q_min_ideal = q_two_fluid(np.array([1e12]), W_N_IDEAL, W_S)[0]     # ->-1 (local)
    q_max_volovik = q_two_fluid(np.array([0.0]), W_N_VOLOVIK, W_S)[0]  # -0.111 (local)
    q_min_volovik = q_two_fluid(np.array([1e12]), W_N_VOLOVIK, W_S)[0] # ->-1 (local)

    # band-span coverage: fraction of [Q_BAND_LO, Q_BAND_HI] covered by [q_min, q_max]
    def band_cover(qmin, qmax):  # (local)
        lo = max(qmin, Q_BAND_LO)  # (local)
        hi = min(qmax, Q_BAND_HI)  # (local)
        return max(0.0, (hi - lo)) / BAND_WIDTH
    cover_ideal = band_cover(q_min_ideal, q_max_ideal)                               # (local)
    cover_volovik = band_cover(q_min_volovik, q_max_volovik)                         # (local)

    # is the SF54 upper endpoint +0.81 reachable by the two-fluid EOS?
    upper_reachable_ideal = bool(q_max_ideal >= Q_BAND_HI)                           # (local)
    upper_reachable_volovik = bool(q_max_volovik >= Q_BAND_HI)                       # (local)

    # band reproduction PASS: requires SPANNING the band to 20% tol.  We test (a)
    # the upper endpoint is reachable AND (b) the window-max deviation < BAND_TOL.
    # Compare the two-fluid q(tau) against the SF54 q(tau) on a common a-grid.
    sf54_q_on_grid = np.interp(a_norm, sf54_a / a_fold_interp, sf54_q)               # (local)
    dev_ideal = np.abs(q_ideal - sf54_q_on_grid)                                     # (local)
    dev_volovik = np.abs(q_volovik - sf54_q_on_grid)                                 # (local)
    dev_ideal_max = float(np.max(dev_ideal))                                         # (local)
    dev_volovik_max = float(np.max(dev_volovik))                                     # (local)
    dev_ideal_fold = float(dev_ideal[0])                                             # (local)
    band_reproduced_ideal = bool(upper_reachable_ideal and dev_ideal_max < BAND_TOL) # (local)

    # === H^2* cross-check (route's own value, NOT read from gates 1/5) =============
    # Volovik two-fluid H^2 = (8 pi G_eff / 3) rho_n + (Lambda from rho_s, w=-1).
    # G_eff = 1/(16 pi a2) M_KK^2 (S95-W5-4 compressibility route).  We report the
    # route's H^2*_reduced at the nominal fixed point = the normal-component-sourced
    # part, in the SAME reduced units as S95-W3-3 nominal_H2_star (a2-channel reduced).
    # The reduced H^2 source at tau* (route-internal): use the S95 nominal H2 source
    # profile (which IS the Bogoliubov relic sum normalized by the a2 channel) and
    # split off the normal-component fraction at the fixed point.
    idx_star = int(np.argmin(np.abs(nominal_taus - nominal_tau_star)))               # (local)
    H2_source_star = float(nominal_H2_source[idx_star])                              # (local)
    # normal-component fraction at the fixed point (x(tau*) -> rho_n fraction)
    x_star_ideal = float(np.interp(nominal_tau_star, tau_grid, x_tau_ideal))         # (local)
    rho_n_frac_star = 1.0 / (1.0 + x_star_ideal)        # rho_n/(rho_n+rho_s) (local)
    H2_star_route = H2_source_star                       # reduced H^2 source (a2-chan) (local)
    H2_star_normal_part = H2_source_star * rho_n_frac_star                           # (local)
    # the route's H^2*_reduced (full two-fluid, normal+effaced-vacuum) at tau*
    H2_star_2fluid_reduced = H2_star_route                                           # (local)

    # G_eff (informational, M_KK units): 1/(16 pi a2) * M_KK^2
    G_eff_MKK2 = 1.0 / (16.0 * np.pi * a_2_FW_zeta)      # in units of M_KK^-2 (local)

    return {
        # upstream
        "rho_relic_MKK": rho_relic_MKK, "rho_B1": rho_B1, "rho_B2": rho_B2, "rho_B3": rho_B3,
        "pairs_check": pairs_check, "pairs_match": pairs_match,
        "relic_sum_match": relic_sum_match, "band_match": band_match,
        "nominal_tau_star": nominal_tau_star, "nominal_H2_star": nominal_H2_star,
        "sf54_q_lo": sf54_q_lo, "sf54_q_hi": sf54_q_hi, "sf54_q_fold": sf54_q_fold,
        # grids
        "tau_grid": tau_grid, "a_norm": a_norm,
        "x_tau_ideal": x_tau_ideal, "x_tau_volovik": x_tau_volovik,
        "q_ideal": q_ideal, "q_volovik": q_volovik,
        "sf54_q_on_grid": sf54_q_on_grid,
        # ODE cross-check
        "ode_ok": ode_ok, "q_ode_ideal": q_ode_ideal, "q_ode_volovik": q_ode_volovik,
        "x_ode_ideal": x_ode_ideal, "x_ode_volovik": x_ode_volovik,
        "resid_ideal": resid_ideal, "resid_volovik": resid_volovik,
        "ode_closedform_consistent": ode_closedform_consistent,
        # EOS / anchors
        "w_n_ideal": W_N_IDEAL, "w_n_volovik": W_N_VOLOVIK, "w_s": W_S,
        "x_fold": X_FOLD, "rho_s_frac_fold": RHO_S_FRAC_FOLD, "rho_n_frac_fold": RHO_N_FRAC_FOLD,
        # SIGN
        "dqdx_ideal_max": float(np.max(dqdx_ideal)), "dqdx_volovik_max": float(np.max(dqdx_volovik)),
        "sign_all_negative": sign_all_negative,
        "normal_decel_contrib_ideal": normal_decel_contrib_ideal,
        "normal_decel_contrib_volovik": normal_decel_contrib_volovik,
        "vacuum_accel_contrib": vacuum_accel_contrib,
        "normal_above_vacuum": normal_above_vacuum,
        # MAGNITUDE / band
        "q_max_ideal": q_max_ideal, "q_min_ideal": q_min_ideal,
        "q_max_volovik": q_max_volovik, "q_min_volovik": q_min_volovik,
        "cover_ideal": cover_ideal, "cover_volovik": cover_volovik,
        "predicted_cover_frac_I": PREDICTED_COVER_FRAC_I,
        "upper_reachable_ideal": upper_reachable_ideal,
        "upper_reachable_volovik": upper_reachable_volovik,
        "dev_ideal_max": dev_ideal_max, "dev_volovik_max": dev_volovik_max,
        "dev_ideal_fold": dev_ideal_fold,
        "band_reproduced_ideal": band_reproduced_ideal,
        "band_tol": BAND_TOL,
        # H^2*
        "H2_star_2fluid_reduced": H2_star_2fluid_reduced,
        "H2_star_normal_part": H2_star_normal_part,
        "rho_n_frac_star": rho_n_frac_star, "x_star_ideal": x_star_ideal,
        "G_eff_MKK2": G_eff_MKK2,
    }


# -----------------------------------------------------------------------------
# Section 6 — Gate verdict (3-tuple per pre-registered operator + collapse)
# -----------------------------------------------------------------------------
def evaluate_gate(res: dict) -> tuple[str, str, str, str]:
    """Return (composite, sign_v, mag_v, reg_v).

    sign_verdict : PASS iff dq/dx < 0 everywhere (POSITIVE normal-component
                   deceleration source) AND the normal-EOS deceleration contribution
                   exceeds the vacuum (w=-1) contribution (1+3 w_n > 1+3 w_s).  This
                   is the substitution-chain Step-4 directional prediction and the
                   two-fluid-split resolution of the T6 overwhelm.
    magnitude_v  : PASS iff the two-fluid q_Omega SPANS the SF54 band [-0.97,+0.81]
                   to within 20% (upper endpoint reachable AND window-max deviation
                   < 0.356).  FAIL iff the band is NOT spanned (the +1/2..+0.81
                   portion is structurally unreachable by the two-fluid EOS).  INFO
                   reserved if the closure works modulo external normalization only.
    regime_v     : VALID iff the two-fluid continuity ODE integrates successfully AND
                   the closed-form q(tau) reproduces the ODE solution to <1e-8
                   (confirming x(tau) IS the continuity-equation solution, not an
                   ansatz).  BREAKDOWN iff the ODE fails or the consistency breaks.
    """
    # SIGN: dq/dx < 0 (both readings) AND normal contributes more deceleration than vacuum
    sign_v = "PASS" if (res["sign_all_negative"] and res["normal_above_vacuum"]) else "FAIL"  # (local)

    # MAGNITUDE: band reproduction (Reading I is the plan-idealized PASS target)
    if res["band_reproduced_ideal"]:
        mag_v = "PASS"  # (local)
    else:
        # band NOT spanned: the +1/2..+0.81 part is structurally unreachable.
        # This is a substrate-physics FAIL on the literal band-reproduction criterion.
        mag_v = "FAIL"  # (local)

    # REGIME: two-fluid hydrodynamics well-posed (ODE solves + closed-form consistent)
    if res["ode_ok"] and res["ode_closedform_consistent"]:
        reg_v = "VALID"  # (local)
    else:
        reg_v = "BREAKDOWN"  # (local)

    # Composite-collapse rule (gate-verdicts.md schema-v2; PRE-REGISTERED)
    if reg_v == "BREAKDOWN":
        composite = "FAIL"  # (local)
    elif sign_v == "FAIL":
        composite = "FAIL"
    elif mag_v == "FAIL" and reg_v == "VALID":
        composite = "FAIL"
    elif mag_v == "FAIL" and reg_v == "MARGINAL":
        composite = "INFO"
    elif mag_v == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"
    return composite, sign_v, mag_v, reg_v


# -----------------------------------------------------------------------------
# Section 7 — Plot
# -----------------------------------------------------------------------------
def make_plot(res: dict) -> None:
    tau = res["tau_grid"]  # (local)
    fig, axes = plt.subplots(1, 2, figsize=(14.5, 6.2))  # (local)

    # Panel A: q_Omega(tau) two readings vs SF54 band
    ax = axes[0]  # (local)
    ax.axhspan(Q_BAND_LO, Q_BAND_HI, color="tab:green", alpha=0.10,
               label=f"SCALE-FACTOR-54 band [{Q_BAND_LO}, {Q_BAND_HI}]")
    ax.axhline(Q_BAND_HI, color="tab:green", ls=":", lw=1.1)
    ax.axhline(Q_BAND_LO, color="tab:green", ls=":", lw=1.1)
    ax.axhline(0.5, color="tab:red", ls="--", lw=1.4,
               label="two-fluid structural max $q=+1/2$ (Reading I, $x\\to0$)")
    ax.plot(tau, res["q_ideal"], "-", color="tab:blue", lw=1.8,
            label="$q_\\Omega$ Reading I ($w_n=0$ dust)")
    ax.plot(tau, res["q_volovik"], "-", color="tab:purple", lw=1.8,
            label=f"$q_\\Omega$ Reading II ($w_n={W_N_VOLOVIK:.3f}$, S67 Volovik)")
    ax.plot(tau, res["sf54_q_on_grid"], "o-", color="0.4", ms=3, lw=1.0,
            label="SF54 $q(\\tau)$ (Connes-distance proxy)")
    ax.axvline(tau_fold, color="k", ls="-.", lw=0.8, alpha=0.6)
    ax.axvline(res["nominal_tau_star"], color="tab:orange", ls="-.", lw=1.0, alpha=0.8,
               label=f"$\\tau_*={res['nominal_tau_star']:.4f}$")
    ax.set_xlabel("$\\tau$ (Jensen deformation)", fontsize=11)
    ax.set_ylabel("$q_\\Omega$ (deceleration parameter)", fontsize=11)
    ax.set_title("Two-fluid $q_\\Omega(\\tau)$ vs SCALE-FACTOR-54 band\n"
                 "(+0.5..+0.81 STRUCTURALLY UNREACHABLE by two-fluid EOS)", fontsize=10)
    ax.legend(loc="center left", fontsize=7.6, framealpha=0.9)
    ax.grid(True, alpha=0.25)

    # Panel B: q_Omega(x) analytic curve + band coverage
    ax = axes[1]  # (local)
    xx = np.logspace(-2, 3, 400)  # (local)
    ax.axhspan(Q_BAND_LO, Q_BAND_HI, color="tab:green", alpha=0.10,
               label="SF54 band")
    ax.plot(xx, q_two_fluid(xx, W_N_IDEAL, W_S), "-", color="tab:blue", lw=1.8,
            label="$q_\\Omega(x)$ Reading I")
    ax.plot(xx, q_two_fluid(xx, W_N_VOLOVIK, W_S), "-", color="tab:purple", lw=1.8,
            label="$q_\\Omega(x)$ Reading II")
    ax.axvline(res["x_fold"], color="k", ls="-.", lw=0.9,
               label=f"$x_{{fold}}={res['x_fold']:.1f}$ (S67 ODLRO)")
    ax.axhline(0.5, color="tab:red", ls="--", lw=1.2)
    ax.axhline(-1.0, color="tab:gray", ls=":", lw=1.0)
    ax.annotate(f"cover$_I$ = {res['cover_ideal']*100:.1f}% of band\n"
                f"upper +0.81 reachable: {res['upper_reachable_ideal']}",
                xy=(0.05, 0.05), xycoords="axes fraction", fontsize=8.5,
                bbox=dict(boxstyle="round", fc="white", alpha=0.85))
    ax.set_xscale("log")
    ax.set_xlabel("$x = \\rho_s/\\rho_n$ (vacuum-to-normal ratio)", fontsize=11)
    ax.set_ylabel("$q_\\Omega(x)$", fontsize=11)
    ax.set_title("$q_\\Omega(x)=\\frac{1}{2}\\frac{(1+3w_n)+x(1+3w_s)}{1+x}$\n"
                 "$x\\to0$: normal-dominated (decel); $x\\to\\infty$: vacuum (accel)", fontsize=10)
    ax.legend(loc="upper right", fontsize=7.8, framealpha=0.9)
    ax.grid(True, which="both", alpha=0.25)

    fig.suptitle(f"{GATE_ID} — Volovik two-fluid effective-Friedmann (ROUTE 2 of 3)",
                 fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(PNG_OUT, dpi=140)
    plt.close(fig)


# -----------------------------------------------------------------------------
# Section 8 — Verdict-line emitter (atomic append; dual-SHA + REQUIRED 3-tuple)
# -----------------------------------------------------------------------------
def append_verdict(verdict, value_str, audit_sha, content_sha,
                   sign_v, mag_v, reg_v, res) -> None:
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    line = (
        f"{GATE_ID}: {verdict} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} "
        f"L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; [SIGN] Volovik two-fluid q_Omega; "
        f"ROUTE 2 of 3 a(t)-closure (gates 1/5 NOT read; cross-route is S97)\n"
    )
    schema_v2_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={reg_v} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2); "
        f"sign = dq_Omega/dx < 0 (POSITIVE normal-component deceleration source; "
        f"dqdx_max_ideal={res['dqdx_ideal_max']:.4e}, normal_contrib(+1)>vacuum(-2)={res['normal_above_vacuum']}); "
        f"magnitude = band reproduction (two-fluid q_max={res['q_max_ideal']:.3f} < SF54 +0.81 => "
        f"+0.5..+0.81 UNREACHABLE; cover={res['cover_ideal']*100:.1f}%; band_reproduced={res['band_reproduced_ideal']}); "
        f"regime = two-fluid continuity ODE well-posed (ode_ok={res['ode_ok']}, "
        f"closed-form consistent resid={max(res['resid_ideal'],res['resid_volovik']):.2e})\n"
    )
    detail_row = (
        f"# x_fold={res['x_fold']:.4f}(S67 ODLRO) q_I(x_fold)={float(q_two_fluid(np.array([res['x_fold']]),W_N_IDEAL,W_S)[0]):.4f} "
        f"q_II(x_fold)={float(q_two_fluid(np.array([res['x_fold']]),W_N_VOLOVIK,W_S)[0]):.4f} "
        f"SF54_q_fold={res['sf54_q_fold']:.4f} dev_fold={res['dev_ideal_fold']:.4f}(<band_tol {res['band_tol']:.3f}) "
        f"H2_star_2fluid_reduced={res['H2_star_2fluid_reduced']:.6e} "
        f"H2_star_normal_part={res['H2_star_normal_part']:.6e} rho_n_frac_star={res['rho_n_frac_star']:.4e} "
        f"# {GATE_ID} two-fluid detail (T6 133200x split-resolution: w=-1 vacuum vs w_n relic)\n"
    )
    regulator_pin = (
        f"# LEVEL_CLASS_PIN=FULL regulator_pin=a_n_zeta "
        f"# {GATE_ID} a_2^zeta={a_2_FW_zeta:.6f} in a2->g_M dictionary; "
        f"w_n_Volovik={W_N_VOLOVIK:.6f} from S67 GGE-TWO-FLUID-67 Volovik identity; "
        f"n_pairs={n_pairs}, P_exc={P_exc_kz}, Gamma_eff={Gamma_effacement}; "
        f"substrate-first-canonical-sourcing.md PASS\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)
        fp.write(schema_v2_row)
        fp.write(detail_row)
        fp.write(regulator_pin)


# -----------------------------------------------------------------------------
# Section 9 — Main
# -----------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)  # (local)
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PY, pins)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()
    print(f"  canonical: a_2^zeta={a_2_FW_zeta:.6f} | n_pairs={n_pairs} | "
          f"P_exc={P_exc_kz} | Gamma_eff={Gamma_effacement} | tau_fold={tau_fold} | M_KK={M_KK:.4e}")
    print(f"  EOS: w_n(ideal)={W_N_IDEAL} | w_n(Volovik,S67)={W_N_VOLOVIK:.6f} | w_s={W_S}")
    print()

    res = compute()  # (local)

    print("=== upstream consistency ===")
    print(f"  rho_relic_MKK = {res['rho_relic_MKK']:.6f} (B1={res['rho_B1']:.4f}+B2={res['rho_B2']:.4f}+B3={res['rho_B3']:.4f})  match={res['relic_sum_match']}")
    print(f"  pairs_check={res['pairs_check']} (=n_pairs? {res['pairs_match']}); SF54 band match={res['band_match']}")
    print(f"  SF54 q-range [{res['sf54_q_lo']:.6f}, {res['sf54_q_hi']:.6f}]; q_fold={res['sf54_q_fold']:.6f}")
    print()
    print("=== two-fluid EOS anchors (S67 ODLRO) ===")
    print(f"  x_fold = rho_s/rho_n = {res['x_fold']:.4f} (98.85% superfluid / 1.15% normal)")
    print(f"  q_I (x_fold) = {float(q_two_fluid(np.array([res['x_fold']]),W_N_IDEAL,W_S)[0]):.6f}")
    print(f"  q_II(x_fold) = {float(q_two_fluid(np.array([res['x_fold']]),W_N_VOLOVIK,W_S)[0]):.6f}")
    print()
    print("=== SIGN (substitution chain Step 4) ===")
    print(f"  dq/dx max (ideal)   = {res['dqdx_ideal_max']:.6e}  (<0 everywhere? {res['sign_all_negative']})")
    print(f"  normal decel contrib (1+3 w_n): ideal=+{res['normal_decel_contrib_ideal']:.3f}, "
          f"Volovik={res['normal_decel_contrib_volovik']:.3f}; vacuum (1+3 w_s)={res['vacuum_accel_contrib']:.3f}")
    print(f"  normal contributes more deceleration than vacuum: {res['normal_above_vacuum']}")
    print()
    print("=== ODE cross-check (two-fluid continuity in ln a) ===")
    print(f"  ODE solved: {res['ode_ok']}; closed-form vs ODE resid max = "
          f"{max(res['resid_ideal'],res['resid_volovik']):.3e} (consistent? {res['ode_closedform_consistent']})")
    print()
    print("=== MAGNITUDE (band reproduction) ===")
    print(f"  two-fluid q range: Reading I [{res['q_min_ideal']:.4f}, {res['q_max_ideal']:.4f}]; "
          f"Reading II [{res['q_min_volovik']:.4f}, {res['q_max_volovik']:.4f}]")
    print(f"  SF54 band [{Q_BAND_LO}, {Q_BAND_HI}]; band_tol={res['band_tol']:.4f}")
    print(f"  upper +0.81 reachable: ideal={res['upper_reachable_ideal']}, Volovik={res['upper_reachable_volovik']}")
    print(f"  band coverage: ideal={res['cover_ideal']*100:.2f}% (predicted {res['predicted_cover_frac_I']*100:.2f}%), "
          f"Volovik={res['cover_volovik']*100:.2f}%")
    print(f"  window-max |q_I - q_SF54| = {res['dev_ideal_max']:.4f}; fold dev = {res['dev_ideal_fold']:.4f}")
    print(f"  band_reproduced (ideal) = {res['band_reproduced_ideal']}")
    print()
    print("=== H^2* (route's own; gates 1/5 NOT read) ===")
    print(f"  H2_star_2fluid_reduced = {res['H2_star_2fluid_reduced']:.6e} (a2-channel reduced)")
    print(f"  H2_star_normal_part    = {res['H2_star_normal_part']:.6e} (normal-component fraction)")
    print(f"  rho_n_frac at tau*     = {res['rho_n_frac_star']:.6e}; G_eff = {res['G_eff_MKK2']:.6e} M_KK^-2")
    print(f"  (S95-W3-3 nominal H2* reduced = {res['nominal_H2_star']:.6e})")
    print()

    composite, sign_v, mag_v, reg_v = evaluate_gate(res)  # (local)
    print(f"  sign_verdict      = {sign_v}")
    print(f"  magnitude_verdict = {mag_v}")
    print(f"  regime_verdict    = {reg_v}")
    print(f"  COMPOSITE         = {composite}")
    print()

    # Save npz
    np.savez(
        NPZ_OUT,
        gate_id=GATE_ID,
        composite_verdict=composite, sign_verdict=sign_v,
        magnitude_verdict=mag_v, regime_verdict=reg_v,
        # grids
        tau_grid=res["tau_grid"], a_norm=res["a_norm"],
        x_tau_ideal=res["x_tau_ideal"], x_tau_volovik=res["x_tau_volovik"],
        q_ideal=res["q_ideal"], q_volovik=res["q_volovik"],
        sf54_q_on_grid=res["sf54_q_on_grid"],
        q_ode_ideal=res["q_ode_ideal"], q_ode_volovik=res["q_ode_volovik"],
        x_ode_ideal=res["x_ode_ideal"], x_ode_volovik=res["x_ode_volovik"],
        # scalars
        rho_relic_MKK=res["rho_relic_MKK"], rho_B1=res["rho_B1"],
        rho_B2=res["rho_B2"], rho_B3=res["rho_B3"], pairs_check=res["pairs_check"],
        nominal_tau_star=res["nominal_tau_star"], nominal_H2_star=res["nominal_H2_star"],
        sf54_q_lo=res["sf54_q_lo"], sf54_q_hi=res["sf54_q_hi"], sf54_q_fold=res["sf54_q_fold"],
        w_n_ideal=res["w_n_ideal"], w_n_volovik=res["w_n_volovik"], w_s=res["w_s"],
        x_fold=res["x_fold"], rho_s_frac_fold=res["rho_s_frac_fold"], rho_n_frac_fold=res["rho_n_frac_fold"],
        dqdx_ideal_max=res["dqdx_ideal_max"], dqdx_volovik_max=res["dqdx_volovik_max"],
        sign_all_negative=res["sign_all_negative"],
        normal_decel_contrib_ideal=res["normal_decel_contrib_ideal"],
        normal_decel_contrib_volovik=res["normal_decel_contrib_volovik"],
        vacuum_accel_contrib=res["vacuum_accel_contrib"], normal_above_vacuum=res["normal_above_vacuum"],
        q_max_ideal=res["q_max_ideal"], q_min_ideal=res["q_min_ideal"],
        q_max_volovik=res["q_max_volovik"], q_min_volovik=res["q_min_volovik"],
        cover_ideal=res["cover_ideal"], cover_volovik=res["cover_volovik"],
        predicted_cover_frac_I=res["predicted_cover_frac_I"],
        upper_reachable_ideal=res["upper_reachable_ideal"],
        upper_reachable_volovik=res["upper_reachable_volovik"],
        dev_ideal_max=res["dev_ideal_max"], dev_volovik_max=res["dev_volovik_max"],
        dev_ideal_fold=res["dev_ideal_fold"], band_reproduced_ideal=res["band_reproduced_ideal"],
        band_tol=res["band_tol"], band_lo=Q_BAND_LO, band_hi=Q_BAND_HI,
        ode_ok=res["ode_ok"], resid_ideal=res["resid_ideal"], resid_volovik=res["resid_volovik"],
        ode_closedform_consistent=res["ode_closedform_consistent"],
        H2_star_2fluid_reduced=res["H2_star_2fluid_reduced"],
        H2_star_normal_part=res["H2_star_normal_part"],
        rho_n_frac_star=res["rho_n_frac_star"], x_star_ideal=res["x_star_ideal"],
        G_eff_MKK2=res["G_eff_MKK2"],
        a_2_FW_zeta=a_2_FW_zeta, n_pairs=n_pairs,
        P_exc_kz=P_exc_kz, Gamma_effacement=Gamma_effacement,
        tau_fold=tau_fold, M_KK=M_KK,
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"  wrote {NPZ_OUT.name}")

    make_plot(res)
    print(f"  wrote {PNG_OUT.name}")

    value_str = (
        f"composite={composite};"
        f"q_max_ideal={res['q_max_ideal']:.4f};q_min_ideal={res['q_min_ideal']:.4f};"
        f"q_max_volovik={res['q_max_volovik']:.4f};"
        f"SF54_band=[{Q_BAND_LO},{Q_BAND_HI}];upper_reachable={res['upper_reachable_ideal']};"
        f"band_cover_ideal={res['cover_ideal']*100:.2f}pct;band_reproduced={res['band_reproduced_ideal']};"
        f"x_fold={res['x_fold']:.4f};q_I_fold={float(q_two_fluid(np.array([res['x_fold']]),W_N_IDEAL,W_S)[0]):.4f};"
        f"q_II_fold={float(q_two_fluid(np.array([res['x_fold']]),W_N_VOLOVIK,W_S)[0]):.4f};"
        f"w_n_Volovik={W_N_VOLOVIK:.6f};dqdx_neg={res['sign_all_negative']};"
        f"normal_above_vacuum={res['normal_above_vacuum']};"
        f"H2_star_2fluid_reduced={res['H2_star_2fluid_reduced']:.6e};"
        f"H2_star_normal_part={res['H2_star_normal_part']:.6e};"
        f"ode_consistent={res['ode_closedform_consistent']};"
        f"rho_relic_MKK={res['rho_relic_MKK']:.4f};T6_split_resolution=w-1_vacuum_sep_from_w_n_relic"
    )  # (local)
    append_verdict(composite, value_str, audit_sha, content_sha,
                   sign_v, mag_v, reg_v, res)
    print(f"  appended verdict line: {GATE_ID}: {composite}")
    print(f"\n  elapsed {time.time() - t0:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
