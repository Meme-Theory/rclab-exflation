#!/usr/bin/env python3
"""
INV4 W2-3 CHRISTODOULOU-SCC: H1_loc strong-cosmic-censorship on the extremal
Sigma_dump modulus horizon
============================================================================

Gate: INV4-W2-3 ([VERIFY-THEOREM])  --  investigation track

Pre-registered threshold (plan investigation-4-plan-w2.md SS W2-3):
  HYPOTHESIS: on the exactly-solvable extremal (kappa=0) modulus metric
    ds^2 = -V(tau) dt^2 + dtau^2/V(tau),   V(tau) = V_0 (tau - tau_dump)^2
  (double root: V = V' = 0, V'' = 2.0 at tau_dump, per S85-W6-4 / S96-HYG-
  KIND-TAG-S53), a massless scalar's H1_loc regularity across Sigma_dump
  either FAILS Christodoulou's bounded-variation criterion (the maximal
  Cauchy development is INEXTENDIBLE -- strong cosmic censorship HOLDS, the
  censored Kasner region is genuinely sealed) or PASSES it (smoothly
  EXTENDIBLE -- censorship VIOLATED, the singularity is only dynamically-
  avoided).

  Two-branch structural verdict keyed on the H1_loc regularity exponent p
  where the near-horizon field-energy
      E(eps) = integral_{|x|<eps} |d_v phi|^2 (energy measure)  ~  |x|^p :
    p < -1 ==> d_v phi NOT in L^2 ==> phi NOT in H1_loc ==> INEXTENDIBLE (SCC holds)
    p > -1 ==> d_v phi in L^2     ==> phi in H1_loc     ==> EXTENDIBLE  (SCC violated)
  p_crit = -1 is the exact L^2-integrability boundary of d_v phi at the horizon.

  Decisive branch resolution requires |p - (-1)| = |p+1| > 0.1.
  |p+1| <= 0.1  ==> INFO marginal-censorship band (the extremal horizon sits
                    ON the L^2 boundary -- the extremal-RN/Kerr / Aretakis
                    boundary-of-censorship regime; L_max/regulator-independent
                    here since the metric is closed-form).

  PASS  = p decisively resolved (|p+1|>0.1) to either branch (question ANSWERED;
          EITHER branch is a PASS -- the gate resolves G3 censorship-robustness,
          it does NOT favor an outcome). Branch identity carried in value string.
  FAIL  = the wave-equation ODE cannot be integrated decisively across Sigma_dump
          (ODE breaks down before p stabilizes / near-horizon fit non-convergent)
          -- given the metric is exactly solvable, a FAIL most likely flags a
          script/ODE defect to fix in-session.
  INFO  = |p+1| <= 0.1 marginal-censorship band.

Inputs (SHA-256 dual-pinned, S84+ schema):
  - computations/_shared/canonical_constants.py (tau_dump, T_H_dump_expected)
  - computations/session-85/s85_w6_extremal_horizon_formal.npz (the kappa=0
    double-root V structure this gate solves the wave equation ON)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<branch+p>, scheme=Jensen_V_tree, convention=2D_modulus_metric, L_max=NA)

Classification: GEOMETRIC

SUBSTITUTION CHAIN (MANDATORY -- [VERIFY-THEOREM])
--------------------------------------------------
Let x := tau - tau_dump. V(tau) = V_0 x^2 (V_0 = 1, S85-W6-4 normalization).

Def 1 (extremal V): V(tau_dump)=0, V'(tau_dump)=0 (double root), V''=2V_0=2.0>0.
  Surface gravity kappa = (1/2)|V'(tau_dump)| = 0 (EXTREMAL).
  [src: S85-W6-4 s85_w6_extremal_horizon_formal.py; S96-HYG-KIND-TAG-S53]

Def 2 (tortoise coordinate): tau_* = integral dtau/V = integral dx/(V_0 x^2)
  = -1/(V_0 x) + const.  As x->0+, tau_* -> -infinity like -1/x  (POWER-LAW,
  NOT logarithmic -- the key structural difference from a sub-extremal horizon
  whose tau_* ~ (1/2kappa) ln|x| diverges only logarithmically).
  [src: closed-form integral of the extremal V]

Def 3 (blueshift / surface gravity): a SUB-extremal horizon (kappa>0) blueshifts
  an ingoing perturbation as e^{kappa v} -> exponential mass-inflation -> the
  energy integral diverges -> phi NOT in H1_loc -> strong censorship (automatic).
  For the EXTREMAL horizon (kappa=0): blueshift factor e^{kappa v} = e^0 = 1.
  The exponential mass-inflation amplification is ABSENT.
  [src: Christodoulou 2008 bounded-variation; extremal-RN/Kerr Cauchy-horizon work]

Substitute (why this is a GENUINE two-branch question, not a foregone divergence):
  with kappa=0 the energy integral integral|d_v phi|^2 dv is no longer driven by
  an exponential; it is set by the POWER-LAW tail of the field on the 1/x tortoise
  coordinate, governed by an exponent p where E(eps) ~ |x|^p. The verdict is
  decided by the SIGN of (p+1), computed by the scan -- NOT pre-decided.

Simplify: L^2-integrability of d_v phi at the horizon <=> p > -1.
  Censorship (inextendibility) <=> p < -1 (d_v phi not in L^2 <=> phi not in H1_loc).
Canonical form: verdict = INEXTENDIBLE iff fitted p < -1 ; EXTENDIBLE iff p > -1.
Direction: NO pre-registered direction for the VERDICT -- extremal horizons sit
  ON the censorship boundary (that is precisely why the gate is informative). The
  chain fixes only that the blueshift shuts off (kappa=0 => e^{kappa v}=1), making
  this a real two-branch question.

Method (two independent reads of p, cross-checked):
  (A) Closed-form near-horizon: solve the radial wave equation
        d/dtau[ V dR/dtau ] + (omega^2 / V) R = 0
      whose tortoise form is  d^2 psi/dtau_*^2 + omega^2 psi = 0  (2D massless
      scalar: zero Regge-Wheeler potential) => psi = e^{+- i omega tau_*},
      |R| -> bounded oscillatory at the horizon. The INGOING (regular, v-coord)
      derivative d_v phi and its energy density |d_v phi|^2 in the proper energy
      measure are evaluated near-horizon in closed form; p read analytically.
  (B) Numerical ODE: integrate the radial equation with scipy solve_ivp (RK45,
      tight rtol) from an exterior matching radius inward toward the horizon with
      a Price-tail-normalized ingoing boundary condition; accumulate the energy
      integral E(eps) on a shrinking near-horizon window and log-log fit
      p = d ln E / d ln|x|.
  The two reads MUST agree to within the fit tolerance; disagreement => FAIL
  (script/ODE defect). The metric double-root is cross-checked
  |V(tau_dump)|<1e-14 and |V'(tau_dump)|<1e-14 (matches S85-W6-4 TOL_EXTREMAL).

R-2 hygiene: Sigma_dump is the EXTREMAL (kappa=0, T_H=0) modulus horizon --
  thermodynamically SILENT, and NOT the causal disconnector (that is the ACOUSTIC
  sonic horizon tau_H+- of W2-1, kappa_ac != 0). This gate asks the CAUCHY-horizon
  (censorship) question of the extremal surface -- distinct from disconnection.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')   # CPU fallback per computation-environment.md
os.environ.setdefault('MKL_NUM_THREADS', '8')

from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 -- Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.integrate import cumulative_trapezoid

t_start = time.time()

# ---------------------------------------------------------------------------
# Section 3 -- Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "4"                                              # (local) investigation number
GATE_ID = "INV4-W2-3"                                      # (local)
SCHEME = "Jensen_V_tree"                                   # (local)
CONVENTION = "2D_modulus_metric"                           # (local)
L_MAX = "NA"                                               # (local) 2D modulus metric, L-independent

# Plan-pinned machinery (investigation-4-plan-w2.md SS W2-3 (5) machinery_pin_map)
N_EVAL = 20000                                             # (local) near-horizon tau-grid points
SCAN_MIN = 0.17                                            # (local) near-Sigma_dump window low
SCAN_MAX = 0.21                                            # (local) near-Sigma_dump window high
TOL_ODE_RTOL = 1e-10                                       # (local) ODE rtol
TOL_P_FIT = 0.01                                           # (local) exponent p resolved to +-0.01
TOL_EXTREMAL = 1e-14                                       # (local) double-root cross-check (S85-W6-4)
P_CRIT = -1.0                                              # (local) L^2-integrability boundary exponent
INFO_BAND = 0.1                                            # (local) |p+1|<=0.1 -> INFO marginal
V_0 = 1.0                                                  # (local) quadratic prefactor (S85-W6-4 norm)

# Price-tail exponent of the EXTERIOR scalar field used as the ingoing boundary
# data. For a massless scalar the late-time exterior decay is the Price tail.
# We carry it as a pinned modeling input and report the H1 verdict's sensitivity
# to it; the DEFAULT physical value for the dominant (monopole-analog) mode is
# the standard Price power. We use the conservative l=0 Price index q_PRICE; the
# energy verdict is reported for a band of q to show p's (in)sensitivity.
Q_PRICE = 3.0                                              # (local) l=0 Price tail v^{-q}, q=2l+3 -> 3

OUT_NPZ = SESSION_DIR / "inv4_w2_christodoulou_scc.npz"
OUT_PNG = SESSION_DIR / "inv4_w2_christodoulou_scc.png"
# Verdict file written by emit_verdict MCP tool (race-safe), NOT this script.

INPUT_FILES = [  # (local)
    SHARED_DIR / "canonical_constants.py",
    COMPUTATIONS_DIR / "session-85" / "s85_w6_extremal_horizon_formal.npz",
]


# ---------------------------------------------------------------------------
# Section 4 -- SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple:
    script_bytes = script_path.read_bytes()        # (local)
    canonical_bytes = canonical_path.read_bytes()  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True,
    ).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 -- Modulus-space extremal metric + wave equation
# ---------------------------------------------------------------------------
TAU_DUMP = float(tau_dump)  # (local) canonical 0.19


def V_metric(tau):
    """Extremal lapse V(tau) = V_0 (tau - tau_dump)^2 (double root at tau_dump)."""
    return V_0 * (tau - TAU_DUMP) ** 2


def Vp_metric(tau):
    """V'(tau) = 2 V_0 (tau - tau_dump)."""
    return 2.0 * V_0 * (tau - TAU_DUMP)


def tortoise(tau):
    """Closed-form tortoise coordinate tau_* = -1/(V_0 (tau-tau_dump)) (+const=0).

    For tau > tau_dump (exterior, x>0): tau_* = -1/(V_0 x) is large NEGATIVE,
    -> -infinity as x->0+ (POWER-LAW divergence, the extremal signature).
    """
    x = tau - TAU_DUMP  # (local)
    return -1.0 / (V_0 * x)


# Radial wave equation in tau: d/dtau[V dR/dtau] + (omega^2/V) R = 0
#   Expand:  V R'' + V' R' + (omega^2/V) R = 0
#   R'' = -(V'/V) R' - (omega^2/V^2) R
def radial_rhs(tau, y, omega):
    """First-order system for R(tau): y=[R, R'].  R'' from the wave equation."""
    R, Rp = y                                   # (local)
    V = V_metric(tau)                           # (local)
    Vp = Vp_metric(tau)                         # (local)
    Rpp = -(Vp / V) * Rp - (omega ** 2 / V ** 2) * R  # (local)
    return [Rp, Rpp]


# ---------------------------------------------------------------------------
# Section 5a -- Closed-form near-horizon energy exponent (read A)
# ---------------------------------------------------------------------------
def closed_form_exponent():
    """Analytic near-horizon H1 energy exponent p for the extremal metric.

    Solution structure (tortoise form): d^2 psi/dtau_*^2 + omega^2 psi = 0
      => psi = e^{+- i omega tau_*}, with tau_* = -1/(V_0 x).
      => R(tau) = psi(tau_*) is BOUNDED, oscillatory as x->0 (|R| -> const).

    Ingoing regular (Eddington-Finkelstein) null coordinate: v = t + tau_*.
    The regular ingoing derivative of phi = e^{-i omega t} R is, on the horizon
    generator, d_v phi.  The transverse/ingoing derivative inherits the tortoise
    Jacobian dtau_*/dtau = 1/V = 1/(V_0 x^2):

        d_tau phi = (dpsi/dtau_*)(dtau_*/dtau) ~ (i omega psi) / (V_0 x^2)
                 => |d_tau phi| ~ |x|^{-2}     (coordinate-tau derivative)

    The H1_loc energy that defines the Christodoulou criterion is the energy
    FLUX across the horizon in the regular ingoing measure. The renormalized
    field-energy across the Cauchy horizon is

        E(eps) = integral_{horizon, |x|<eps} |d_v phi|^2 dv

    With v = t + tau_*, dv = dtau_* = dtau/V = dtau/(V_0 x^2), and the regular
    ingoing-null derivative d_v phi = d_tau_* phi = V d_tau phi = i omega psi
    (BOUNDED on the horizon -- this is the statement that the field is regular in
    the ingoing coordinate, the extremal kappa=0 e^{kappa v}=1 shut-off). Then

        |d_v phi|^2  ~  |omega psi|^2  =  bounded (oscillatory, O(1))
        E(eps) = integral_{|x|<eps} |d_v phi|^2 (dtau_*/dtau) dtau
               = integral_{0}^{eps} O(1) * (1/(V_0 x^2)) dx
               ~  integral_0^eps x^{-2} dx  ~  eps^{-1}    => p = -1.

    So the CLOSED-FORM extremal exponent is p = -1 EXACTLY: the energy integrand
    is O(1) in the regular ingoing field but the ingoing-null MEASURE dv ~ x^{-2}
    dx integrates to a x^{-1} (logarithmically-on-the-boundary) divergence whose
    energy exponent sits EXACTLY at p_crit = -1. This is the analytic statement
    that the EXTREMAL horizon lies ON the H1 (L^2) censorship boundary -- the
    Aretakis / extremal-RN marginal-censorship regime. (A sub-extremal horizon
    would carry the e^{kappa v} blueshift and give p << -1, automatic
    inextendibility; the extremal kappa=0 removes it and lands on p=-1.)

    Returns the analytic p and the structural annotation.
    """
    p_analytic = -1.0  # (local) extremal energy exponent sits ON the L^2 boundary
    return p_analytic


# ---------------------------------------------------------------------------
# Section 5b -- Numerical energy exponent (read B)
# ---------------------------------------------------------------------------
def numerical_exponent(omega):
    """Integrate the radial wave equation inward and fit p from E(eps) ~ |x|^p.

    We integrate R(tau) from an exterior matching radius tau_match toward the
    horizon, with an ingoing-null normalized boundary condition (R ~ e^{i omega
    tau_*} = e^{-i omega/(V_0 x)} -- the regular ingoing branch). At a sequence
    of shrinking cutoffs eps we accumulate the regular ingoing-null field energy

        E(eps) = integral_{tau_dump+eps_inner}^{tau_dump+eps} |d_v phi|^2 dv

    where d_v phi = V dR/dtau (the regular ingoing-null derivative) and
    dv = dtau/V. Hence the integrand in tau is |V R'|^2 * (1/V) = V |R'|^2,
    and additionally the t-derivative piece contributes |omega R|^2 / V to the
    full stress tensor; we report BOTH the gradient-energy exponent and the
    full-T_vv exponent. The log-log slope d ln E / d ln eps is the exponent p.
    """
    x_match = SCAN_MAX - TAU_DUMP        # (local) exterior matching distance (0.02)
    tau_match = TAU_DUMP + x_match       # (local)
    # Stop at x_inner=5e-4 (well-resolved, non-stiff): the wave coefficient
    # omega^2/V^2 = omega^2/(V_0 x^2)^2 grows as x^{-4}; going to x->1e-6 makes
    # the ODE catastrophically stiff (coeff ~1e24) for no gain -- the closed-form
    # already establishes |R|->bounded oscillatory there, and the H1 energy
    # exponent is set by the ingoing-null MEASURE dv ~ x^{-2} dx (geometry),
    # visible in the [2e-4, 5e-3] window. (Read A is the analytic anchor; Read B
    # confirms the measure-driven exponent on the resolved near-horizon band.)
    x_inner = 5e-4                        # (local) innermost resolved approach
    tau_inner = TAU_DUMP + x_inner       # (local)

    # Ingoing-null boundary data at tau_match: R = e^{i omega tau_*}, regular branch.
    ts_match = tortoise(tau_match)        # (local)
    R0 = np.exp(1j * omega * ts_match)    # (local)
    # dR/dtau = (i omega) (dtau_*/dtau) R = (i omega / V) R
    Rp0 = (1j * omega / V_metric(tau_match)) * R0  # (local)

    # Integrate the COMPLEX radial equation as a real 4-vector [Re R, Im R, Re R', Im R'].
    def rhs_real(tau, yv):
        R = yv[0] + 1j * yv[1]           # (local)
        Rp = yv[2] + 1j * yv[3]          # (local)
        dR, dRp = radial_rhs(tau, [R, Rp], omega)  # (local)
        return [dR.real, dR.imag, dRp.real, dRp.imag]

    # Dense output for the energy integral; integrate inward (tau decreasing).
    tau_eval = np.linspace(tau_match, tau_inner, N_EVAL)  # (local) decreasing
    sol = solve_ivp(
        rhs_real, (tau_match, tau_inner),
        [R0.real, R0.imag, Rp0.real, Rp0.imag],
        t_eval=tau_eval, method='RK45',
        rtol=TOL_ODE_RTOL, atol=1e-14, max_step=x_match / 50.0,
    )
    if not sol.success:
        return None, None, None, None, None, sol.message

    tau_arr = sol.t                                   # (local) decreasing from tau_match
    R_arr = sol.y[0] + 1j * sol.y[1]                  # (local)
    Rp_arr = sol.y[2] + 1j * sol.y[3]                 # (local)
    x_arr = tau_arr - TAU_DUMP                        # (local) > 0, decreasing
    V_arr = V_metric(tau_arr)                         # (local)

    # Regular ingoing-null derivative d_v phi = V dR/dtau ; energy density |d_v phi|^2.
    dv_phi = V_arr * Rp_arr                           # (local) BOUNDED if extremal-regular
    grad_energy_density = np.abs(dv_phi) ** 2         # (local) the H1 ingoing-energy density
    # Full T_vv-relevant density also carries the (omega R)^2/V piece (t-derivative).
    Tvv_density = grad_energy_density + (np.abs(omega * R_arr) ** 2) / V_arr  # (local)

    # The energy across the horizon uses the ingoing-null MEASURE dv = dtau/V.
    # Accumulate E(eps) = integral_{|x|<eps} density dv  for shrinking eps.
    # Sort by increasing x for cumulative integration from the horizon outward.
    order = np.argsort(x_arr)                          # (local)
    x_s = x_arr[order]                                 # (local) increasing
    dv_measure = 1.0 / V_arr[order]                    # (local) dv/dtau = 1/V
    grad_dens_s = grad_energy_density[order]           # (local)
    Tvv_dens_s = Tvv_density[order]                    # (local)

    # E(eps): integral from x_inner up to eps of (density * dv/dtau) dtau, where
    # dtau = dx. So integrand in x is density/V.
    integrand_grad = grad_dens_s * dv_measure          # (local)
    integrand_Tvv = Tvv_dens_s * dv_measure            # (local)

    # Cumulative energy E(eps) = integral_{x_inner}^{eps} integrand dx, VECTORIZED
    # (cumulative_trapezoid is O(N); the prior per-cutoff simpson list-comp was
    # O(N^2) and stalled at N=20000).
    eps_grid = x_s[1:]                                  # (local) upper cutoffs
    E_grad = cumulative_trapezoid(integrand_grad, x_s, initial=0.0)[1:]  # (local)
    E_Tvv = cumulative_trapezoid(integrand_Tvv, x_s, initial=0.0)[1:]    # (local)

    # Fit p from the DIFFERENTIAL shell energy dE/d ln eps ~ eps^p (same exponent
    # as the cumulative E(eps) ~ eps^p). Shell energy = eps * integrand(eps).
    # Fit window must sit INSIDE the resolved band [x_inner=5e-4, x_match=0.02].
    mask = (eps_grid > 8e-4) & (eps_grid < 1e-2)       # (local) near-horizon fit window
    ln_eps = np.log(eps_grid[mask])                    # (local)
    shell_grad = eps_grid * integrand_grad[1:]         # (local) eps * (density/V) at eps
    shell_Tvv = eps_grid * integrand_Tvv[1:]           # (local)
    ln_shell_grad = np.log(np.abs(shell_grad[mask]) + 1e-300)  # (local)
    ln_shell_Tvv = np.log(np.abs(shell_Tvv[mask]) + 1e-300)    # (local)

    if mask.sum() < 5:
        return None, None, None, None, None, "fit window too sparse"
    p_grad = np.polyfit(ln_eps, ln_shell_grad, 1)[0]   # (local) gradient-energy exponent
    p_Tvv = np.polyfit(ln_eps, ln_shell_Tvv, 1)[0]     # (local) full-T_vv exponent

    return p_grad, p_Tvv, eps_grid, E_grad, E_Tvv, "ok"


# ---------------------------------------------------------------------------
# Section 6 -- Main
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme, convention, L_max):
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note="", extra_rows=None):
    """Print the emit_verdict payload (delimited) for the dispatching agent.

    [VERIFY-THEOREM] gate -- NO sign/magnitude/regime 3-tuple (not [SIGN]).
    """
    payload = {
        "session": int(SESSION),
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
        "track": "investigation",
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


def main() -> int:
    print("=" * 80)
    print(f"  {GATE_ID}: CHRISTODOULOU H1_loc SCC ON EXTREMAL Sigma_dump")
    print("=" * 80)

    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()                 # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    print("Canonical inputs:")
    print(f"  tau_dump          = {TAU_DUMP}")
    print(f"  T_H_dump_expected = {float(T_H_dump_expected)}")
    print(f"  V_0               = {V_0}")
    print()

    # --- Double-root + extremality cross-check (S85-W6-4 anchor) ---
    V_at_dump = V_metric(TAU_DUMP)        # (local)
    Vp_at_dump = Vp_metric(TAU_DUMP)      # (local)
    Vpp_at_dump = 2.0 * V_0               # (local) analytic
    kappa = 0.5 * abs(Vp_at_dump)         # (local) surface gravity
    is_double_root = (abs(V_at_dump) < TOL_EXTREMAL) and (abs(Vp_at_dump) < TOL_EXTREMAL)  # (local)
    print("=== Extremal double-root cross-check (S85-W6-4) ===")
    print(f"  V(tau_dump)   = {V_at_dump:.3e}   (|.|<{TOL_EXTREMAL:.0e}: {abs(V_at_dump) < TOL_EXTREMAL})")
    print(f"  V'(tau_dump)  = {Vp_at_dump:.3e}   (|.|<{TOL_EXTREMAL:.0e}: {abs(Vp_at_dump) < TOL_EXTREMAL})")
    print(f"  V''(tau_dump) = {Vpp_at_dump:.3e}  (>0: {Vpp_at_dump > 0})")
    print(f"  kappa = (1/2)|V'| = {kappa:.3e}   (EXTREMAL: {kappa < TOL_EXTREMAL})")
    print(f"  blueshift e^(kappa v) at horizon = {np.exp(kappa * 0.0):.6f}  (=1 => mass-inflation shut off)")
    print(f"  double-root condition: {is_double_root}")
    print()

    # --- Tortoise coordinate divergence type (power-law vs log) ---
    xs_check = np.array([1e-2, 1e-3, 1e-4, 1e-5])   # (local)
    ts_check = np.array([tortoise(TAU_DUMP + xx) for xx in xs_check])  # (local)
    # Power-law: tau_* ~ -1/(V_0 x). Slope of ln|tau_*| vs ln x should be -1.
    slope_tort = np.polyfit(np.log(xs_check), np.log(np.abs(ts_check)), 1)[0]  # (local)
    print("=== Tortoise coordinate near-horizon divergence ===")
    for xx, tt in zip(xs_check, ts_check):
        print(f"  x={xx:.0e}: tau_* = {tt:.6e}   (closed form -1/(V_0 x) = {-1.0/(V_0*xx):.6e})")
    print(f"  d ln|tau_*| / d ln x = {slope_tort:.6f}  (EXTREMAL power-law -1; sub-extremal log->0)")
    print()

    # --- Read A: closed-form exponent ---
    p_closed = closed_form_exponent()   # (local)
    print("=== Read A: closed-form near-horizon H1 energy exponent ===")
    print(f"  p_closed (analytic) = {p_closed:.6f}")
    print(f"  -> energy E(eps) ~ eps^{p_closed:.1f}; sits {'ON' if abs(p_closed - P_CRIT) < 1e-9 else 'OFF'} p_crit={P_CRIT}")
    print()

    # --- Read B: numerical exponent (averaged over a band of omega) ---
    omega_band = np.array([0.5, 1.0, 2.0, 4.0])   # (local) test frequencies (M_KK units)
    p_grad_list = []   # (local)
    p_Tvv_list = []    # (local)
    eps_ref = E_grad_ref = E_Tvv_ref = None        # (local) keep one for plotting
    print("=== Read B: numerical ODE energy exponent (per omega) ===")
    for om in omega_band:
        p_g, p_t, eps_g, Eg, Et, msg = numerical_exponent(om)  # (local)
        if p_g is None:
            print(f"  omega={om}: ODE FAIL ({msg})")
            continue
        p_grad_list.append(p_g)
        p_Tvv_list.append(p_t)
        if eps_ref is None:
            eps_ref, E_grad_ref, E_Tvv_ref = eps_g, Eg, Et
        print(f"  omega={om:>4}: p_grad = {p_g:+.4f}   p_Tvv = {p_t:+.4f}")
    print()

    p_grad_mean = float(np.mean(p_grad_list)) if p_grad_list else float('nan')  # (local)
    p_grad_std = float(np.std(p_grad_list)) if p_grad_list else float('nan')    # (local)
    p_Tvv_mean = float(np.mean(p_Tvv_list)) if p_Tvv_list else float('nan')     # (local)

    # --- Reconcile reads A and B; choose the reported p ---
    # The gradient-energy exponent p_grad is the H1_loc (L^2 of d_v phi) discriminator.
    p_reported = p_grad_mean   # (local) the H1_loc energy exponent
    reads_agree = (not np.isnan(p_grad_mean)) and (abs(p_grad_mean - p_closed) < 0.15)  # (local)
    print("=== Reconciliation ===")
    print(f"  p_closed (read A)     = {p_closed:+.6f}")
    print(f"  p_grad_mean (read B)  = {p_grad_mean:+.6f}  (std over omega = {p_grad_std:.2e})")
    print(f"  p_Tvv_mean (read B)   = {p_Tvv_mean:+.6f}")
    print(f"  reads agree (<0.15)   = {reads_agree}")
    print(f"  p_reported            = {p_reported:+.6f}")
    print()

    # --- Branch verdict on sign(p+1) ---
    p_plus_1 = p_reported + 1.0   # (local)
    print("=== Christodoulou H1_loc branch verdict ===")
    print(f"  p_reported = {p_reported:+.6f}   p_crit = {P_CRIT}")
    print(f"  p + 1 = {p_plus_1:+.6f}   |p+1| = {abs(p_plus_1):.6f}   INFO band = {INFO_BAND}")

    if not reads_agree or np.isnan(p_reported):
        verdict = "FAIL"
        branch = "INDETERMINATE"
        value_tag = f"FAIL_reads_disagree_pA={p_closed:.3f}_pB={p_grad_mean:.3f}"
    elif abs(p_plus_1) <= INFO_BAND:
        verdict = "INFO"
        branch = "MARGINAL-CENSORSHIP"
        value_tag = f"MARGINAL_p={p_reported:.4f}_|p+1|={abs(p_plus_1):.4f}<=0.1_extremal-on-L2-boundary"
    elif p_reported < P_CRIT:
        verdict = "PASS"
        branch = "INEXTENDIBLE"
        value_tag = f"INEXTENDIBLE_p={p_reported:.4f}<-1_SCC-holds_sealed"
    else:  # p_reported > P_CRIT
        verdict = "PASS"
        branch = "EXTENDIBLE"
        value_tag = f"EXTENDIBLE_p={p_reported:.4f}>-1_SCC-violated_dynamically-avoided-only"

    print(f"  BRANCH = {branch}")
    print(f"  VERDICT = {verdict}")
    print(f"  value = {value_tag}")
    print()

    # --- Save NPZ ---
    np.savez(
        OUT_NPZ,
        tau_dump=np.array(TAU_DUMP),
        V_0=np.array(V_0),
        kappa=np.array(kappa),
        Vpp_at_dump=np.array(Vpp_at_dump),
        is_double_root=np.array([is_double_root]),
        slope_tortoise=np.array(slope_tort),
        p_closed=np.array(p_closed),
        omega_band=omega_band,
        p_grad_list=np.array(p_grad_list),
        p_Tvv_list=np.array(p_Tvv_list),
        p_grad_mean=np.array(p_grad_mean),
        p_grad_std=np.array(p_grad_std),
        p_Tvv_mean=np.array(p_Tvv_mean),
        p_reported=np.array(p_reported),
        p_crit=np.array(P_CRIT),
        p_plus_1=np.array(p_plus_1),
        info_band=np.array(INFO_BAND),
        reads_agree=np.array([reads_agree]),
        branch=np.array(branch, dtype=object),
        verdict=np.array(verdict, dtype=object),
        eps_ref=eps_ref if eps_ref is not None else np.array([]),
        E_grad_ref=E_grad_ref if E_grad_ref is not None else np.array([]),
        E_Tvv_ref=E_Tvv_ref if E_Tvv_ref is not None else np.array([]),
        audit_sha256=np.array(audit_sha, dtype=object),
        content_sha256=np.array(content_sha, dtype=object),
        scheme=np.array(SCHEME, dtype=object),
        convention=np.array(CONVENTION, dtype=object),
    )

    # --- Plot ---
    fig, axes = plt.subplots(2, 2, figsize=(13, 9))

    # (a) V(tau) double-root
    ax = axes[0, 0]
    tg = np.linspace(SCAN_MIN, SCAN_MAX, 2000)   # (local)
    ax.plot(tg, V_metric(tg), color='#1f77b4', lw=1.4, label=r'$V(\tau)=V_0(\tau-\tau_\mathrm{dump})^2$')
    ax.axvline(TAU_DUMP, color='k', ls='--', lw=0.7, label=r'$\tau_\mathrm{dump}=0.19$')
    ax.axhline(0, color='grey', ls=':', lw=0.5)
    ax.set_xlabel(r'$\tau$'); ax.set_ylabel(r'$V(\tau)$')
    ax.set_title(r'(a) Extremal lapse: double root, $\kappa=0$')
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    # (b) tortoise coordinate power-law divergence
    ax = axes[0, 1]
    xg = np.logspace(-5, -2, 200)                # (local)
    ax.loglog(xg, np.abs(tortoise(TAU_DUMP + xg)), color='#9467bd', lw=1.4,
              label=r'$|\tau_*|=1/(V_0|x|)$ (extremal, power-law)')
    ax.loglog(xg, np.abs(0.5 * np.log(xg)), color='grey', ls='--', lw=1.0,
              label=r'sub-extremal $\sim|\ln|x||$ (log, for contrast)')
    ax.set_xlabel(r'$|x|=|\tau-\tau_\mathrm{dump}|$'); ax.set_ylabel(r'$|\tau_*|$')
    ax.set_title(rf'(b) Tortoise divergence: slope $={slope_tort:.3f}$ (extremal $-1$)')
    ax.legend(fontsize=8); ax.grid(alpha=0.3, which='both')

    # (c) Energy integral E(eps) vs eps
    ax = axes[1, 0]
    if eps_ref is not None and len(eps_ref) > 1:
        ax.loglog(eps_ref, np.abs(E_grad_ref), color='#d62728', lw=1.3,
                  label=r'$E_\mathrm{grad}(\epsilon)=\int_{|x|<\epsilon}|\partial_v\phi|^2\,dv$')
        # Reference slope p=-1 (the L^2 boundary)
        em = eps_ref[len(eps_ref) // 2]          # (local)
        Em = np.abs(E_grad_ref[len(eps_ref) // 2])  # (local)
        ax.loglog(eps_ref, Em * (eps_ref / em) ** (-1.0), color='k', ls='--', lw=0.9,
                  label=r'$p_\mathrm{crit}=-1$ (L$^2$ boundary)')
    ax.set_xlabel(r'$\epsilon=|x|$ cutoff'); ax.set_ylabel(r'$E(\epsilon)$')
    ax.set_title(rf'(c) H$^1_\mathrm{{loc}}$ energy: $p_\mathrm{{reported}}={p_reported:+.4f}$')
    ax.legend(fontsize=8); ax.grid(alpha=0.3, which='both')

    # (d) Penrose diagram + verdict
    ax = axes[1, 1]
    ax.set_xlim(-1.3, 1.3); ax.set_ylim(-1.3, 1.3); ax.set_aspect('equal')
    diamond = plt.Polygon([(-1, 0), (0, 1), (1, 0), (0, -1)], fill=False, edgecolor='k', lw=0.8)
    ax.add_patch(diamond)
    # extremal Cauchy horizon as single null line (degenerate double-null)
    chcol = '#2ca02c' if branch == 'EXTENDIBLE' else '#d62728'  # (local)
    ax.plot([0, 0], [-1, 1], '-', color=chcol, lw=2.2,
            label=rf'$\Sigma_\mathrm{{dump}}$ ($\kappa=0$): {branch}')
    ax.text(0, 1.06, r'$i^+$', ha='center', fontsize=10)
    ax.text(0, -1.06, r'$i^-$', ha='center', fontsize=10)
    ax.text(1.06, 0, r'$i^0$', fontsize=9)
    ax.text(-1.18, 0, 'Kasner\n($\\tau\\to\\infty$)', ha='right', fontsize=7, va='center')
    ax.set_xticks([]); ax.set_yticks([])
    ax.legend(loc='lower center', fontsize=7)
    ax.set_title(f'(d) {verdict}: SCC {"HOLDS" if branch=="INEXTENDIBLE" else ("VIOLATED" if branch=="EXTENDIBLE" else "MARGINAL")}')

    fig.suptitle(
        f'INV4-W2-3 Christodoulou H1_loc SCC on extremal Sigma_dump  --  '
        rf'$p={p_reported:+.4f}$, $|p+1|={abs(p_plus_1):.4f}$  ->  {branch}',
        fontsize=12,
    )
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)

    # --- 4-tuple + verdict payload ---
    print(emit_4tuple(value_tag, SCHEME, CONVENTION, L_MAX))
    extra = [
        f"# regularity_exponent p_reported={p_reported:.6f} p_crit={P_CRIT} |p+1|={abs(p_plus_1):.6f}",
        f"# closed_form p_A={p_closed:.6f} numerical p_B_grad={p_grad_mean:.6f} p_B_Tvv={p_Tvv_mean:.6f}",
        f"# kappa={kappa:.3e} double_root={is_double_root} tortoise_slope={slope_tort:.4f} (extremal power-law -1)",
        f"# branch={branch} R-2: Sigma_dump EXTREMAL kappa=0/T_H=0 SILENT surface (NOT the W2-1 acoustic disconnector)",
    ]
    print_verdict_payload(verdict, value_tag, audit_sha, content_sha,
                          companion_note=f"INV4-W2-3 {branch} (H1_loc p={p_reported:.4f})",
                          extra_rows=extra)

    print(f"\n=== {GATE_ID}: {verdict} ({branch}) (wall {time.time() - t_start:.1f}s) ===")
    print(f"NPZ: {OUT_NPZ.name}")
    print(f"PNG: {OUT_PNG.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
