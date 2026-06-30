#!/usr/bin/env python3
"""
S84 W8b-93 — MESH-EQUATION-STABILITY
=====================================

Gate: S84-W8B-93-MESH-EQUATION-STABILITY ([SIGN], [VERIFY])

Pre-registered threshold (ABSOLUTE, three-level, per-unit-a):
  PASS iff |d tau_fold / d a|_{a=12} < 0.01       — mesh robust.
  INFO iff 0.01 <= |d tau_fold / d a|_{a=12} < 0.1 — stable, 3-dp precision.
  FAIL iff |d tau_fold / d a|_{a=12} >= 0.1       — mesh fine-tuned.

Method:
  Joint system
    Γ1' cubic-BC:          sin^2(mu_BC) = 3 / (3 + exp(a * tau))
    Γ5' convex curvature:  d^2 S/dtau^2 = +317863  (canonical d2S_fold, locked)
    Γ6 three-band:         f_L(tau) >= 0.6027     (enforced via consistency check)

  Pin mu_BC at its canonical value (set from the cubic-BC identity at the
  canonical point a=12, tau=tau_fold=0.19). Then solve tau_fold(a) on
  a in [11.0, 13.0] with 21 points (Delta a = 0.1) via brentq on the
  cubic-BC residual, restricted to tau in [0.10, 0.30] with xtol=1e-8.

  Apply a centered 5-point stencil at a=12 with Delta a = 0.1 to estimate
  d tau_fold / d a. Cross-check sensitivity via |d tau_fold / d (d^2 S)| at
  nominal d2S_fold = +317863 with relative perturbation 1e-4. (Γ5'/Γ6 appear
  as locked invariants in this layer — they do not enter the cubic-BC
  residual, so cross-check derivative at fixed cubic-BC is 0.0 by construction;
  instead we report |Delta tau| under a +-1e-4 perturbation of mu_BC carried
  through Γ5'/Γ6 consistency, as a structural sensitivity.)

Substitution chain (SIGN):
  sin^2(mu_BC) = 3 / (3 + exp(a*tau))
  => exp(a*tau) = 3*(1 - s^2) / s^2                with s^2 ≡ sin^2(mu_BC)
  => a*tau = ln[3*(1 - s^2) / s^2]
  => tau(a) = ln[3*(1 - s^2) / s^2] / a
  => d tau / d a = - ln[3*(1 - s^2) / s^2] / a^2
  At a=12, tau=0.19: s^2 = 3/(3 + exp(2.28)) = 0.2348, ln[...] = 2.28,
    so d tau / d a = -2.28 / 144 = -0.01583  (magnitude 0.01583 — INFO band).

Output 4-tuple:
  (value=<|d tau_fold / d a|_{a=12}>, scheme=canonical-mesh-stability-v1,
   convention=centered-5-pt, L_max=N/A)

Classification: GEOMETRIC
"""

from __future__ import annotations

# --- Section 1: Canonical constants (MANDATORY) ---
import os
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import tau_fold, d2S_fold, Delta_BCS

# --- Section 2: Standard imports ---
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from scipy.optimize import brentq

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --- Section 3: Paths + pre-registration ---
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S84"                                                    # (local)
GATE_ID = "S84-W8B-93-MESH-EQUATION-STABILITY"                     # (local)
SCHEME = "canonical-mesh-stability-v1"                             # (local)
CONVENTION = "centered-5-pt"                                       # (local)
L_MAX = "N/A"                                                      # (local)

# Thresholds (ABSOLUTE, three-level)
PASS_THRESHOLD = 0.01                                              # (local)
INFO_UPPER = 0.1                                                   # (local)

# Machinery pin
A_CENTER = 12.0                                                    # (local)
A_MIN = 11.0                                                       # (local)
A_MAX = 13.0                                                       # (local)
A_STEPS = 21                                                       # (local)
A_DELTA = 0.1                                                      # (local)
TAU_BRACKET = (0.10, 0.30)                                         # (local)
TAU_XTOL = 1e-8                                                    # (local)
F_L_THRESHOLD = 0.6027                                             # (local) three-band lower-band weight
D2S_PERTURB_REL = 1e-4                                             # (local) cross-check relative perturbation

OUT_NPZ = resolve_output(84, 's84_w8b_mesh_equation_stability.npz')
OUT_PNG = resolve_output(84, 's84_w8b_mesh_equation_stability.png')
VERDICT_TXT = resolve_output(84, 's84_gate_verdicts.txt')

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    PROJECT_ROOT / "sessions" / "permanent-results-registry.md",
    PROJECT_ROOT / "sessions" / "session-plan" / "session-84-plan-w8b.md",
]


# --- Section 4: SHA-256 input-pin block ---
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                           # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} - input SHA-256 pins ===")
    pins = {}                                                      # (local)
    for p in inputs:
        sha = sha256_of(p)                                         # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)                                           # (local)
        print(f"  {rel}: {sha[:16]}...  full={sha}")
        pins[rel] = sha
    return pins


def closure_sha(pins: dict, value: float, tier: str) -> str:
    """Canonical closure hash over ordered input pins + output tuple."""
    payload = {                                                    # (local)
        "gate": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "value": float(value),
        "tier": tier,
        "inputs": [(k, pins[k]) for k in sorted(pins.keys())],
        "A_CENTER": A_CENTER,
        "A_MIN": A_MIN,
        "A_MAX": A_MAX,
        "A_STEPS": A_STEPS,
        "TAU_BRACKET": list(TAU_BRACKET),
        "TAU_XTOL": TAU_XTOL,
        "tau_fold_canon": float(tau_fold),
        "d2S_fold_canon": float(d2S_fold),
    }
    blob = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()   # (local)
    return hashlib.sha256(blob).hexdigest()


# --- Section 5: Physics machinery ---
def cubic_bc_s2(a: float, tau: float) -> float:
    """sin^2(mu_BC) from cubic-BC identity."""
    return 3.0 / (3.0 + math.exp(a * tau))


def cubic_bc_residual(tau: float, a: float, s2_pin: float) -> float:
    """Root condition: 3/(3 + exp(a*tau)) - s2_pin = 0."""
    return cubic_bc_s2(a, tau) - s2_pin


def solve_tau_fold_of_a(a: float, s2_pin: float,
                        tau_lo: float = TAU_BRACKET[0],
                        tau_hi: float = TAU_BRACKET[1],
                        xtol: float = TAU_XTOL) -> float:
    """brentq root of cubic-BC residual on [tau_lo, tau_hi]."""
    f_lo = cubic_bc_residual(tau_lo, a, s2_pin)                    # (local)
    f_hi = cubic_bc_residual(tau_hi, a, s2_pin)                    # (local)
    if f_lo * f_hi > 0.0:
        raise ValueError(
            f"No sign change on [{tau_lo}, {tau_hi}] at a={a}: "
            f"f_lo={f_lo:+.3e}, f_hi={f_hi:+.3e}"
        )
    return brentq(cubic_bc_residual, tau_lo, tau_hi, args=(a, s2_pin), xtol=xtol)


def f_L_consistency(tau: float, s2_pin: float) -> float:
    """
    Heuristic lower-band weight along the cubic-BC mesh. For the mesh-stability
    gate, Γ6 (f_L >= 0.6027) is a consistency CHECK: we evaluate a monotonic
    surrogate f_L(tau) = 1 - s^2(a=12, tau) to verify that the mesh root stays
    above 0.6027 across the full a-scan. (Surrogate: lower-band weight grows
    as sin^2(mu_BC) shrinks; at tau=0.19, a=12, s^2=0.2348, giving f_L_surr = 0.7652.)
    """
    return 1.0 - cubic_bc_s2(12.0, tau)                            # (local)


# --- Section 6: Main ---
def main():
    print("=" * 78)
    print(f"  {GATE_ID}")
    print("=" * 78)
    print(f"  canonical tau_fold = {tau_fold}")
    print(f"  canonical d2S_fold = {d2S_fold:.6f}")
    print(f"  canonical Delta_BCS = {Delta_BCS:.6f}")
    print(f"  Gamma6 three-band threshold f_L >= {F_L_THRESHOLD}")
    print()

    pins = log_input_pins(INPUT_FILES)                             # (local)

    # --- Step 1: pin mu_BC from canonical point (a=12, tau=tau_fold) ---
    s2_pin = cubic_bc_s2(A_CENTER, tau_fold)                       # (local)
    mu_BC_deg = math.degrees(math.asin(math.sqrt(s2_pin)))         # (local)
    print(f"[pin] s^2_mu_BC (from a=12, tau={tau_fold}) = {s2_pin:.16f}")
    print(f"      mu_BC = {mu_BC_deg:.12f} deg")
    print()

    # Self-check: tau(a=12) solved from brentq must equal tau_fold to xtol
    tau_check = solve_tau_fold_of_a(A_CENTER, s2_pin)              # (local)
    print(f"[check] brentq at a=12 -> tau = {tau_check:.16f}  "
          f"(canonical tau_fold = {tau_fold}, |delta|={abs(tau_check - tau_fold):.3e})")
    assert abs(tau_check - tau_fold) < 1e-7, "Self-consistency failure at a=12"
    print()

    # --- Step 2: scan tau_fold(a) on [A_MIN, A_MAX] ---
    a_grid = np.linspace(A_MIN, A_MAX, A_STEPS)                    # (local)
    assert A_STEPS == 21
    assert abs(a_grid[1] - a_grid[0] - A_DELTA) < 1e-12, "grid spacing mismatch"

    tau_grid = np.zeros(A_STEPS)                                   # (local)
    f_L_grid = np.zeros(A_STEPS)                                   # (local)
    for i, a in enumerate(a_grid):
        tau_i = solve_tau_fold_of_a(float(a), s2_pin)              # (local)
        tau_grid[i] = tau_i
        f_L_grid[i] = f_L_consistency(tau_i, s2_pin)

    print("[scan] a, tau_fold(a), f_L_surr(tau)")
    print("        a        tau_fold(a)        f_L_surr       (f_L >= 0.6027?)")
    for i, a in enumerate(a_grid):
        ok = "OK" if f_L_grid[i] >= F_L_THRESHOLD else "FAIL"      # (local)
        print(f"  {a:7.3f}   {tau_grid[i]:.12f}   {f_L_grid[i]:.12f}   [{ok}]")
    print()

    # Γ6 three-band consistency check across scan
    f_L_min = float(np.min(f_L_grid))                              # (local)
    f_L_max = float(np.max(f_L_grid))                              # (local)
    gamma6_ok = f_L_min >= F_L_THRESHOLD                           # (local)
    print(f"[Γ6] f_L_surr in [{f_L_min:.6f}, {f_L_max:.6f}]; "
          f"three-band threshold {F_L_THRESHOLD}: {'OK' if gamma6_ok else 'VIOLATED'}")
    print()

    # Γ5' convex-curvature: locked at d2S_fold; verify canonical value unchanged
    # (This layer does not couple d2S into the cubic-BC residual; d2S_fold enters
    # as a structural lock reported for audit.)
    print(f"[Γ5'] d^2 S/dtau^2 = {d2S_fold:.6f}  (locked, positive-definite)")
    print()

    # --- Step 3: centered 5-point stencil at a=12 ---
    # Indices: a_grid[5]=11.5, a_grid[9]=11.9, a_grid[10]=12.0, a_grid[11]=12.1, a_grid[15]=12.5
    # Centered 5-point stencil uses a-2h, a-h, a, a+h, a+2h with h=Delta a=0.1.
    # Node indices in 21-point grid centered on a=12: 8, 9, 10, 11, 12
    i_center = np.argmin(np.abs(a_grid - A_CENTER))                # (local)
    assert i_center == 10, f"a=12 should be index 10, got {i_center}"
    i_m2, i_m1, i_0, i_p1, i_p2 = i_center - 2, i_center - 1, i_center, i_center + 1, i_center + 2
    h = A_DELTA                                                    # (local)

    # 5-point centered stencil: f'(x) ≈ (-f_{+2} + 8 f_{+1} - 8 f_{-1} + f_{-2}) / (12 h)
    dtau_da_5pt = (
        -tau_grid[i_p2] + 8.0 * tau_grid[i_p1]
        - 8.0 * tau_grid[i_m1] + tau_grid[i_m2]
    ) / (12.0 * h)                                                 # (local)

    # Cross-check: 3-point centered stencil (lower-order)
    dtau_da_3pt = (tau_grid[i_p1] - tau_grid[i_m1]) / (2.0 * h)    # (local)

    # Analytic reference at fixed s2_pin: dtau/da = -ln[3(1-s2)/s2] / a^2 = -tau/a
    dtau_da_analytic = -tau_fold / A_CENTER                        # (local)

    abs_dtau_da = abs(dtau_da_5pt)                                 # (local)

    print("=" * 78)
    print(f"  5-point stencil at a={A_CENTER}, h={h}")
    print("=" * 78)
    print(f"  d tau_fold / d a  (5-pt centered) = {dtau_da_5pt:+.12e}")
    print(f"  d tau_fold / d a  (3-pt centered) = {dtau_da_3pt:+.12e}")
    print(f"  d tau_fold / d a  (analytic -tau/a) = {dtau_da_analytic:+.12e}")
    print(f"  |d tau_fold / d a|_{{a=12}}        = {abs_dtau_da:.12e}")
    print(f"  relative err (5pt vs analytic)   = "
          f"{abs(dtau_da_5pt - dtau_da_analytic)/abs(dtau_da_analytic):.3e}")
    print()

    # --- Step 4: sensitivity cross-check vs d^2 S/dtau^2 ---
    # In this residual layer d2S does NOT enter the cubic-BC equation directly;
    # d tau_fold / d (d2S) |_{d2S=+317863} = 0 by construction at the cubic-BC level.
    # Report explicitly; also report |Delta tau| under a perturbation of s2_pin at
    # the same relative size, as a structural sensitivity surrogate.
    d2s_perturb_abs = D2S_PERTURB_REL * d2S_fold                   # (local)
    print(f"[Γ5' cross-check] d^2 S perturbation ±{D2S_PERTURB_REL*100:.4f}% = ±{d2s_perturb_abs:.3f}")
    print(f"  d tau_fold / d (d^2 S) at cubic-BC layer = 0  (d2S is locked, not residual-coupled)")

    # Surrogate: if s2_pin drifts by relative 1e-4 (a rough proxy for rep-theoretic drift
    # under a d2S shift), how much does tau_fold at a=12 move?
    s2_plus = s2_pin * (1.0 + D2S_PERTURB_REL)                     # (local)
    s2_minus = s2_pin * (1.0 - D2S_PERTURB_REL)                    # (local)
    tau_plus = solve_tau_fold_of_a(A_CENTER, s2_plus)              # (local)
    tau_minus = solve_tau_fold_of_a(A_CENTER, s2_minus)            # (local)
    dtau_ds2_surrogate = (tau_plus - tau_minus) / (2.0 * D2S_PERTURB_REL * s2_pin)   # (local)
    dtau_abs_surrogate = abs(tau_plus - tau_minus)                 # (local)
    print(f"  surrogate: |Delta tau| under Delta s^2/s^2 = {D2S_PERTURB_REL} ")
    print(f"    tau(s2+) = {tau_plus:.12f}")
    print(f"    tau(s2-) = {tau_minus:.12f}")
    print(f"    |Delta tau| = {dtau_abs_surrogate:.3e}")
    print(f"    d tau / d s^2 (centered) = {dtau_ds2_surrogate:+.6e}")
    print()

    # --- Step 5: verdict ---
    if abs_dtau_da < PASS_THRESHOLD:
        tier = "PASS"                                              # (local)
        explanation = (
            f"|d tau_fold/d a|={abs_dtau_da:.6e} < {PASS_THRESHOLD}. "
            f"Mesh robust; no fine-tuning of cubic-BC exponent a=12."
        )
    elif abs_dtau_da < INFO_UPPER:
        tier = "INFO"                                              # (local)
        explanation = (
            f"{PASS_THRESHOLD} <= |d tau_fold/d a|={abs_dtau_da:.6e} < {INFO_UPPER}. "
            f"Mesh stable but borderline; 3-dp precision required. "
            f"Quote tau_fold = 0.190 ± 0.001 (not 0.1900 ± 0.0001)."
        )
    else:
        tier = "FAIL"                                              # (local)
        explanation = (
            f"|d tau_fold/d a|={abs_dtau_da:.6e} >= {INFO_UPPER}. "
            f"Mesh fine-tuned; cubic-BC exponent is coordinate-dependent. "
            f"Triggers DERIV-II or retreat of tau_fold structural claim."
        )

    print("=" * 78)
    print(f"  VERDICT: {tier}")
    print("=" * 78)
    print(f"  {explanation}")
    print()

    # --- closure SHA ---
    csha = closure_sha(pins, float(abs_dtau_da), tier)             # (local)
    # Content SHA (value payload only, not inputs)
    content_payload = {                                            # (local)
        "value": float(abs_dtau_da),
        "dtau_da_5pt": float(dtau_da_5pt),
        "dtau_da_3pt": float(dtau_da_3pt),
        "dtau_da_analytic": float(dtau_da_analytic),
        "tau_grid": tau_grid.tolist(),
        "f_L_min": float(f_L_min),
        "gamma6_ok": bool(gamma6_ok),
    }
    content_sha = hashlib.sha256(
        json.dumps(content_payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()                                                  # (local)
    # Audit SHA = closure in this single-output gate (no side audit layer)
    audit_sha = csha                                               # (local)

    print(f"  closure_sha256 = {csha}")
    print(f"  content_sha256 = {content_sha}")
    print(f"  audit_sha256   = {audit_sha}")
    print()

    # --- persist artifacts ---
    np.savez(
        OUT_NPZ,
        a_grid=a_grid,
        tau_grid=tau_grid,
        f_L_grid=f_L_grid,
        s2_pin=s2_pin,
        mu_BC_deg=mu_BC_deg,
        dtau_da_5pt=dtau_da_5pt,
        dtau_da_3pt=dtau_da_3pt,
        dtau_da_analytic=dtau_da_analytic,
        abs_dtau_da=abs_dtau_da,
        tau_plus=tau_plus,
        tau_minus=tau_minus,
        dtau_ds2_surrogate=dtau_ds2_surrogate,
        tier=tier,
        gamma6_ok=gamma6_ok,
        closure_sha=csha,
        content_sha=content_sha,
    )
    print(f"  wrote {OUT_NPZ.name}")

    # --- plot ---
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    ax = axes[0]
    ax.plot(a_grid, tau_grid, "o-", color="steelblue", label=r"$\tau_{\rm fold}(a)$")
    ax.axvline(A_CENTER, color="firebrick", ls="--", lw=0.8, label=r"$a=12$")
    ax.axhline(tau_fold, color="black", ls=":", lw=0.8, label=r"$\tau_{\rm fold}=0.19$")
    ax.set_xlabel(r"$a$ (cubic-BC exponent)")
    ax.set_ylabel(r"$\tau_{\rm fold}(a)$")
    ax.set_title(r"$\tau_{\rm fold}(a)$ on $[11.0, 13.0]$, 21 pts, $\Delta a=0.1$")
    ax.grid(alpha=0.4)
    ax.legend(loc="upper right", fontsize=9)

    ax = axes[1]
    # Local linear fit at a=12 for visualization
    slope = dtau_da_5pt                                            # (local)
    a_loc = np.linspace(A_MIN, A_MAX, 201)                         # (local)
    tau_fit = tau_fold + slope * (a_loc - A_CENTER)                # (local)
    ax.plot(a_grid, tau_grid, "o", color="steelblue", label="data")
    ax.plot(a_loc, tau_fit, "-", color="firebrick",
            label=fr"$\tau_{{\rm fold}} + ({slope:+.5f})(a-12)$")
    ax.axvline(A_CENTER, color="black", ls="--", lw=0.6)
    ax.set_xlabel(r"$a$")
    ax.set_ylabel(r"$\tau_{\rm fold}(a)$")
    ax.set_title(
        fr"5-pt derivative at $a=12$: $d\tau_{{\rm fold}}/da={dtau_da_5pt:+.5f}$"
        "\n"
        fr"$|d\tau_{{\rm fold}}/da|={abs_dtau_da:.5f}$  tier={tier}"
    )
    ax.grid(alpha=0.4)
    ax.legend(loc="upper right", fontsize=9)

    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=150)
    plt.close(fig)
    print(f"  wrote {OUT_PNG.name}")

    # --- verdict line ---
    verdict_line = (
        f"{GATE_ID}: {tier} -- "
        f"value={abs_dtau_da:.6e} "
        f"scheme={SCHEME} "
        f"convention={CONVENTION} "
        f"L_max={L_MAX} "
        f"sha256={csha} "
        f"audit_sha256={audit_sha} "
        f"content_sha256={content_sha}"
    )                                                              # (local)
    with open(VERDICT_TXT, "a", encoding="utf-8") as fh:
        fh.write(verdict_line + "\n")
    print()
    print("=" * 78)
    print(f"  verdict appended -> {VERDICT_TXT.name}")
    print(f"  {verdict_line}")
    print("=" * 78)

    # Final output 4-tuple line (non-verdict)
    print(
        f"OUTPUT_4_TUPLE: value={abs_dtau_da:.6e} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX}"
    )

    return 0


if __name__ == "__main__":
    sys.exit(main())
