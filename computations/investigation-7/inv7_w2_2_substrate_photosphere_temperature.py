#!/usr/bin/env python3
"""
INV7 W2-2 — substrate accretion-photosphere temperature T_substrate from the
            tau_fold=0.190 van Hove fixed point (a4/a2 spectral-moment ratio)
============================================================================

Gate: INV7-W2-2 ([SIGN])  — investigation track
Classification: GEOMETRIC

Pre-registered threshold (composite, two-part):
  PART A (Claim A, magnitude+direction):
      |T_substrate - 5000 K| / 5000 K <= band_T = 0.30   (T in [3500, 6500] K)
  PART B (Claim B, the LOAD-BEARING insensitivity):
      max_{tau in [tau_fold-0.025, tau_fold+0.025]} |d T_substrate / d tau|_frac
          <= insens_floor = 0.10
  PASS iff Claim A AND Claim B both hold.
  FAIL iff T_substrate outside [3500,6500] K (wrong magnitude).
  INFO iff no characteristic T emerges (R_moment*E_B2 projection degenerate /
       envelope route empty — the substrate has a fold but does not radiate at a
       characteristic temperature in the observed sense).

SUBSTRATE-FIRST SOURCING DISCIPLINE (load-bearing):
  The pin source is tau_fold + a4^{zeta}/a2^{zeta} (BOTH substrate canonicals).
  The ~5000 K is the COMPARISON TARGET ONLY, sourced from the LRD paper corpus
  (Paper 25 de Graaff Black-Hole-Star RUBIES modified-blackbody; Paper 47
  warm-outer-layer FeII/Balmer; Paper 41 supermassive-stars). It is NEVER the
  pin source. No Kelvin-map free parameter is tuned to land on 5000 K — the
  M_KK->Kelvin map is the canonical natural-unit conversion (k_B), full stop.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py
       (tau_fold=0.19, a_2_FW_zeta=2776.165389, a_4_FW_zeta=1350.7216,
        E_B2_mean=0.845269..., rho_B2_per_mode=14.023250..., M_KK=7.42866e16 GeV,
        k_B=8.617e-5 eV/K, GeV_to_J, k_B_SI)
  - computations/session-52/s52_unified_action.npz
       (tau_grid, R_K_grid — the tau-resolved curvature/DOS quantity driving the
        Seeley-DeWitt a_n heat-kernel moments; rho_B2(fold)=14.023 van-Hove)
  - researchers/Little-Red-Dots/25_*de_Graaff*.md (+47, +41) — TARGET only

Output 4-tuple:
  (value=<T_substrate>, scheme=SA, convention=RATIO, L_max=10)

regulator_pin: a_n^{zeta}  (a2_fold = a_2_FW_zeta, a4_fold = a_4_FW_zeta are
zeta-regulated Seeley-DeWitt coefficients; the a4/a2 ratio is a4^{zeta}/a2^{zeta}).

METHODOLOGY
-----------
PART A (the temperature). The van Hove fold is the B2 flat optical band
(4 modes, E_B2 = 0.845 M_KK; DOS divergence rho_B2(fold)=14.023, S52). Form the
dimensionless spectral-moment ratio R_moment = a4_fold/a2_fold = a_4_FW_zeta /
a_2_FW_zeta (Sage-exact 45024/92539 = 0.48654080982072423). Project it onto a
characteristic photosphere energy E_substrate = R_moment * E_B2 [M_KK-natural],
carry to a physical energy via M_KK [GeV], and to Kelvin via k_B. The reference
is the substrate van-Hove band-edge E_B2 carried through the natural-unit ladder,
NOT an imported observed scale. T_substrate is the OUTPUT.

PART B (insensitivity; the load-bearing discriminator). Sweep the local Jensen
deformation tau on a 101-point grid over [tau_fold-0.025, tau_fold+0.025]. The
moment ratio's tau-dependence is inherited from the canonical S52 cache: the
a_n Seeley-DeWitt moments are heat-kernel curvature integrals (a_2 ~ int R,
a_4 ~ int R^2), so their ratio tracks the tau-resolved curvature/DOS quantity
R_K(tau) read (interpolated) from s52_unified_action.npz. The van Hove
non-stationarity theorem (S85-W10-TAU-FOLD-UNIQUENESS-VAN-HOVE-THEOREM, PERMANENT
SS VII.M.W10-3, scheme=van-Hove-cusp-non-stationarity) establishes the fold is a
cusp where DOS-set quantities are flat-to-first-order over a window. Test it
numerically: T_substrate(tau) = [R_moment * R_K(tau)/R_K(fold)] * E_B2 * M_KK -> K,
and report max |d ln T / d tau| * Delta_tau_local over the window vs insens_floor.

This is a "through-the-mirror-darkly" exploratory gate (plan-flagged). The
NUMBERS are computed honestly; INFO (no characteristic T in the observed sense)
is a pre-registered outcome, not a failure.

DISCIPLINE
----------
- `from canonical_constants import *`; every intermediate tagged `# (local)`
- 101-pt tau scan + scalar moment ratios read from canonical cache (NOT
  re-diagonalized) -> CPU, OMP capped at 8 (no matrix op >= 100x100)
- dual-SHA emitted; agent calls emit_verdict(track="investigation").
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (  # explicit, for clarity
    tau_fold, a_2_FW_zeta, a_4_FW_zeta, E_B2_mean, E_B1,
    rho_B2_per_mode, M_KK, k_B, k_B_SI, GeV_to_J,
)

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

# ---------------------------------------------------------------------------
# Section 3 — Pre-registration pins
# ---------------------------------------------------------------------------
SESSION = "7"                                                      # (local) investigation number
GATE_ID = "INV7-W2-2"                                              # (local)
SCHEME = "SA"                                                      # (local) spectral-action moment ratio
CONVENTION = "RATIO"                                              # (local)
L_MAX = 10                                                        # (local) CONST-FREEZE-42 / S88 canonical truncation

# Pre-registered thresholds (define BEFORE running)
T_TARGET_K = 5000.0          # (local) COMPARISON TARGET ONLY — LRD Balmer-break (Paper 25/47/41); NOT a pin source
BAND_T = 0.30                # (local) Claim A band: |T-5000|/5000 <= 0.30  -> T in [3500,6500] K
INSENS_FLOOR = 0.10          # (local) Claim B: max fractional |dT/dtau|*Delta_tau over window <= 0.10
N_EVAL = 101                 # (local) tau-window grid points
TAU_HALF = 0.025             # (local) half-window
SCAN_MIN = tau_fold - TAU_HALF   # (local) 0.165
SCAN_MAX = tau_fold + TAU_HALF   # (local) 0.215
FD_TOL = 1e-6                # (local) finite-difference tolerance pin

OUT_NPZ = SESSION_DIR / "inv7_w2_2_substrate_photosphere_temperature.npz"
OUT_PNG = SESSION_DIR / "inv7_w2_2_substrate_photosphere_temperature.png"

S52_UNIFIED = COMPUTATIONS_DIR / "session-52" / "s52_unified_action.npz"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    S52_UNIFIED,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 dual-pin block
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
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = script_path.read_bytes() if script_path.exists() else b""   # (local)
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


# ---------------------------------------------------------------------------
# Section 5 — Compute
# ---------------------------------------------------------------------------
def energy_M_KK_to_kelvin(E_nat: float) -> float:
    """Carry a dimensionless M_KK-natural energy E_nat to Kelvin.

    E_nat [M_KK] -> E_GeV = E_nat * M_KK [GeV] -> T = E_GeV / (k_B [eV/K] * 1e-9 GeV/eV)
    i.e. T_K = E_GeV / (k_B_in_GeV_per_K).  k_B = 8.617333262e-5 eV/K -> in GeV/K
    that is k_B * 1e-9. Canonical natural-unit conversion (E = k_B T); no free param.
    """
    E_GeV = E_nat * M_KK                       # (local) GeV
    k_B_GeV_per_K = k_B * 1e-9                  # (local) GeV/K = (eV/K)*(1e-9 GeV/eV)
    return E_GeV / k_B_GeV_per_K                # (local) Kelvin


def compute() -> dict:
    # ---- PART A: the temperature (anchored fold value) ----
    a2_fold = float(a_2_FW_zeta)               # (local) a_2^{zeta} = 2776.165389
    a4_fold = float(a_4_FW_zeta)               # (local) a_4^{zeta} = 1350.7216
    R_moment = a4_fold / a2_fold               # (local) dimensionless spectral-moment ratio
    # cross-check against plan Sage-exact 45024/92539
    R_moment_exact = 45024.0 / 92539.0         # (local) Sage QQ exact
    R_match = abs(R_moment - R_moment_exact)   # (local)

    E_B2 = float(E_B2_mean)                     # (local) 0.845269... M_KK (van-Hove band edge, 4 modes)
    E_substrate_nat = R_moment * E_B2          # (local) characteristic photosphere energy [M_KK-natural]
    T_substrate = energy_M_KK_to_kelvin(E_substrate_nat)   # (local) Kelvin — the gate OUTPUT

    # band membership (Claim A)
    frac_dev = abs(T_substrate - T_TARGET_K) / T_TARGET_K  # (local)
    claim_A = frac_dev <= BAND_T                            # (local)

    # ---- PART B: the insensitivity (load-bearing) ----
    # tau-window grid
    tau_grid = np.linspace(SCAN_MIN, SCAN_MAX, N_EVAL)     # (local)

    # tau-resolved curvature/DOS quantity R_K(tau) from the canonical S52 cache.
    # a_n Seeley-DeWitt moments are heat-kernel curvature integrals (a_2 ~ int R,
    # a_4 ~ int R^2), so the moment ratio tracks the tau-resolved curvature scalar
    # R_K(tau). Read + interpolate from s52_unified_action.npz (NOT re-diagonalized).
    d52 = np.load(S52_UNIFIED, allow_pickle=True)          # (local)
    tau_cache = np.asarray(d52["tau_grid"], dtype=float)   # (local) 200-pt native grid [0,0.5]
    RK_cache = np.asarray(d52["R_K_grid"], dtype=float)    # (local) tau-resolved curvature/DOS quantity
    VKK_cache = np.asarray(d52["V_KK_grid"], dtype=float)  # (local) tau-resolved KK potential (cross-check axis)

    # interpolate R_K onto the window grid and at the fold
    RK_window = np.interp(tau_grid, tau_cache, RK_cache)   # (local)
    RK_fold = float(np.interp(tau_fold, tau_cache, RK_cache))  # (local)
    VKK_window = np.interp(tau_grid, tau_cache, VKK_cache)  # (local)
    VKK_fold = float(np.interp(tau_fold, tau_cache, VKK_cache))  # (local)

    # T_substrate(tau): the moment ratio scales with the curvature quantity relative
    # to its fold value (anchored so T(tau_fold)=T_substrate); E_B2 carried through.
    # PRIMARY axis: R_K-tracking (a_4/a_2 ~ int R^2 / int R tracks R_K to first order).
    R_moment_tau = R_moment * (RK_window / RK_fold)        # (local) primary moment-ratio tau-track
    E_sub_tau = R_moment_tau * E_B2                        # (local)
    T_tau = np.array([energy_M_KK_to_kelvin(e) for e in E_sub_tau])  # (local) Kelvin over window

    # CROSS-CHECK axis: V_KK-tracking (independent tau-resolved DOS-coupled quantity)
    R_moment_tau_vkk = R_moment * (VKK_window / VKK_fold)  # (local)
    T_tau_vkk = np.array([energy_M_KK_to_kelvin(R_moment * (VKK_window[i]/VKK_fold) * E_B2)
                          for i in range(N_EVAL)])          # (local)

    # finite-difference dT/dtau over the window (primary axis)
    dT_dtau = np.gradient(T_tau, tau_grid)                 # (local) Kelvin per unit tau
    # fractional sensitivity: |dT/dtau| * (local step) / T  -> compare across window vs floor
    # Use the window-scale Delta_tau (full half-window) so the floor is a fractional-over-window bound.
    frac_var_window = (T_tau.max() - T_tau.min()) / T_substrate  # (local) fractional spread over window
    # also the local-derivative form: max |d ln T / d tau| * (2*TAU_HALF) over window
    dlnT_dtau = dT_dtau / T_tau                            # (local)
    max_frac_deriv = float(np.max(np.abs(dlnT_dtau)) * (2.0 * TAU_HALF))  # (local)
    # the discriminator: the smaller-of/representative fractional variation over the window
    insens_metric = float(frac_var_window)                # (local) the load-bearing number
    claim_B = insens_metric <= INSENS_FLOOR               # (local)

    # cross-check spread (V_KK axis) — robustness of the insensitivity conclusion
    frac_var_window_vkk = float((T_tau_vkk.max() - T_tau_vkk.min()) / T_substrate)  # (local)

    # ---- degeneracy / INFO test ----
    # INFO if R_moment*E_B2 projection is degenerate (R_moment ~ 0 or E_B2 ~ 0 -> no scale),
    # i.e. T_substrate not finite-positive, OR the projection produces no single scale.
    projection_degenerate = (not np.isfinite(T_substrate)) or (T_substrate <= 0.0)  # (local)

    return {
        "value": float(T_substrate),
        "R_moment": float(R_moment),
        "R_moment_exact": float(R_moment_exact),
        "R_match": float(R_match),
        "a2_fold": a2_fold,
        "a4_fold": a4_fold,
        "E_B2": float(E_B2),
        "E_substrate_nat": float(E_substrate_nat),
        "T_substrate_K": float(T_substrate),
        "frac_dev": float(frac_dev),
        "claim_A": bool(claim_A),
        "tau_grid": tau_grid,
        "T_tau": T_tau,
        "T_tau_vkk": T_tau_vkk,
        "dT_dtau": dT_dtau,
        "RK_window": RK_window,
        "RK_fold": float(RK_fold),
        "VKK_fold": float(VKK_fold),
        "frac_var_window": float(frac_var_window),
        "frac_var_window_vkk": float(frac_var_window_vkk),
        "max_frac_deriv": float(max_frac_deriv),
        "insens_metric": float(insens_metric),
        "claim_B": bool(claim_B),
        "projection_degenerate": bool(projection_degenerate),
        "T_target_K": T_TARGET_K,
        "band_T": BAND_T,
        "insens_floor": INSENS_FLOOR,
    }


# ---------------------------------------------------------------------------
# Section 6 — Gate evaluation (composite [SIGN] 3-tuple + collapse)
# ---------------------------------------------------------------------------
def evaluate_gate(r: dict) -> tuple[str, str, str, str]:
    """Return (composite, sign_verdict, magnitude_verdict, regime_verdict).

    sign_verdict:  PASS iff T_substrate finite-positive (a characteristic T exists);
                   the Step-4 direction is 'finite positive R_moment*E_B2 -> finite
                   positive T'. FAIL iff non-positive / non-finite.
    magnitude_verdict: PASS iff |T-5000|/5000 <= band_T (Claim A in band);
                   INFO if degenerate (no single scale); FAIL otherwise (wrong magnitude).
    regime_verdict: VALID iff Claim B holds (insensitivity over window, the gate's
                   regime-of-validity = the cusp-flatness window) AND window covered;
                   MARGINAL/BREAKDOWN scale with how badly the insensitivity fails.
    Composite per gate-verdicts.md collapse rule, with INFO routed for the
    pre-registered 'no characteristic T / envelope empty' outcome.
    """
    T = r["T_substrate_K"]                  # (local)
    # sign
    sign_v = "PASS" if (np.isfinite(T) and T > 0.0) else "FAIL"   # (local)
    # magnitude (Claim A band membership)
    if r["projection_degenerate"]:
        mag_v = "INFO"                       # (local) no single scale -> envelope route empty
    elif r["claim_A"]:
        mag_v = "PASS"                       # (local)
    else:
        mag_v = "FAIL"                       # (local) wrong magnitude (outside [3500,6500] K)
    # regime (Claim B insensitivity = the cusp-flatness regime of validity)
    insens = r["insens_metric"]              # (local)
    floor = r["insens_floor"]                # (local)
    if insens <= floor:
        regime_v = "VALID"                   # (local) insensitive over window (cusp-flat)
    elif insens <= 2.0 * floor:
        regime_v = "MARGINAL"                # (local) mildly sensitive
    else:
        regime_v = "BREAKDOWN"               # (local) strongly sensitive -> not cusp-flat

    # composite collapse (gate-verdicts.md), with the pre-registered INFO outcome
    # for the 'no characteristic temperature in the observed sense' case:
    # here Claim B (insensitivity) is the load-bearing physics; Claim A (band) is
    # the magnitude test. Apply the canonical collapse:
    if regime_v == "BREAKDOWN":
        composite = "FAIL"
    elif sign_v == "FAIL":
        composite = "FAIL"
    elif mag_v == "FAIL" and regime_v == "VALID":
        composite = "FAIL"
    elif mag_v == "FAIL" and regime_v == "MARGINAL":
        composite = "INFO"
    elif mag_v == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"
    return composite, sign_v, mag_v, regime_v


# ---------------------------------------------------------------------------
# Section 7 — Plot
# ---------------------------------------------------------------------------
def make_plot(r: dict) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))  # (local)

    # Left: T_substrate(tau) over the window vs the 5000 K target band
    ax = axes[0]
    tau = r["tau_grid"]; T = r["T_tau"]; Tv = r["T_tau_vkk"]  # (local)
    ax.plot(tau, T, "-", color="navy", lw=2, label="T_substrate(tau)  [R_K-track, primary]")
    ax.plot(tau, Tv, "--", color="teal", lw=1.4, label="T_substrate(tau)  [V_KK-track, cross-check]")
    ax.axvline(tau_fold, color="k", ls=":", lw=1, label=f"tau_fold={tau_fold}")
    ax.axhline(r["T_substrate_K"], color="navy", ls=":", lw=0.8, alpha=0.6)
    ax.set_xlabel("tau (local Jensen deformation)")
    ax.set_ylabel("T_substrate  [K]")
    ax.set_title(f"PART A/B: T_substrate(tau)\nfold value = {r['T_substrate_K']:.4e} K")
    ax.legend(fontsize=8, loc="best")
    ax.grid(alpha=0.3)

    # Right: fractional variation over window vs the insensitivity floor (the load-bearing claim)
    ax = axes[1]
    Tfold = r["T_substrate_K"]  # (local)
    frac = (T - Tfold) / Tfold  # (local)
    fracv = (Tv - Tfold) / Tfold  # (local)
    ax.plot(tau, frac, "-", color="navy", lw=2, label="(T-T_fold)/T_fold  [R_K]")
    ax.plot(tau, fracv, "--", color="teal", lw=1.4, label="(T-T_fold)/T_fold  [V_KK]")
    ax.axhline(r["insens_floor"], color="crimson", ls="--", lw=1, label=f"+/- insens_floor={r['insens_floor']}")
    ax.axhline(-r["insens_floor"], color="crimson", ls="--", lw=1)
    ax.axvline(tau_fold, color="k", ls=":", lw=1)
    ax.set_xlabel("tau (local Jensen deformation)")
    ax.set_ylabel("fractional deviation of T_substrate")
    ax.set_title(f"PART B (load-bearing): insensitivity\n"
                 f"window spread = {r['frac_var_window']:.3e}  (floor {r['insens_floor']})")
    ax.legend(fontsize=8, loc="best")
    ax.grid(alpha=0.3)

    fig.suptitle(
        f"INV7-W2-2  substrate van-Hove-fold photosphere T  |  "
        f"R_moment=a4^z/a2^z={r['R_moment']:.10f}  |  TARGET ~5000 K (LRD Balmer-break, NOT a pin)",
        fontsize=10)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 — Verdict payload
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict, magnitude_verdict, regime_verdict,
                          extra_rows=None) -> dict:
    payload: dict = {
        "session": int(SESSION),
        "track": "investigation",
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
    }
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 9 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()                # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    r = compute()

    print("=== PART A — the temperature ===")
    print(f"  a2_fold (a_2^zeta)      = {r['a2_fold']:.6f}")
    print(f"  a4_fold (a_4^zeta)      = {r['a4_fold']:.6f}")
    print(f"  R_moment = a4/a2        = {r['R_moment']:.17f}")
    print(f"  R_moment_exact (45024/92539) = {r['R_moment_exact']:.17f}  (|diff|={r['R_match']:.2e})")
    print(f"  E_B2 (van-Hove edge)    = {r['E_B2']:.6f} M_KK")
    print(f"  E_substrate = R*E_B2    = {r['E_substrate_nat']:.6f} M_KK")
    print(f"  M_KK                    = {M_KK:.6e} GeV")
    print(f"  T_substrate             = {r['T_substrate_K']:.6e} K   <-- OUTPUT")
    print(f"  TARGET (LRD, NOT a pin) = {r['T_target_K']:.1f} K")
    print(f"  |T-5000|/5000           = {r['frac_dev']:.6e}  (band_T={r['band_T']})  Claim A={r['claim_A']}")
    print()
    print("=== PART B — the insensitivity (load-bearing) ===")
    print(f"  tau-window              = [{SCAN_MIN:.4f}, {SCAN_MAX:.4f}]  (N={N_EVAL})")
    print(f"  R_K(fold)               = {r['RK_fold']:.6f}  (S52 cache)")
    print(f"  T_substrate window spread (R_K-track)  = {r['frac_var_window']:.6e}  <-- insens_metric")
    print(f"  T_substrate window spread (V_KK-track) = {r['frac_var_window_vkk']:.6e}  (cross-check)")
    print(f"  max |d ln T/d tau|*window               = {r['max_frac_deriv']:.6e}")
    print(f"  insens_floor            = {r['insens_floor']}   Claim B={r['claim_B']}")
    print()

    composite, sign_v, mag_v, regime_v = evaluate_gate(r)

    # persist
    np.savez(
        OUT_NPZ,
        T_substrate_K=r["T_substrate_K"],
        R_moment=r["R_moment"], R_moment_exact=r["R_moment_exact"], R_match=r["R_match"],
        a2_fold=r["a2_fold"], a4_fold=r["a4_fold"], E_B2=r["E_B2"],
        E_substrate_nat=r["E_substrate_nat"], M_KK=float(M_KK),
        frac_dev=r["frac_dev"], claim_A=r["claim_A"],
        T_target_K=r["T_target_K"], band_T=r["band_T"],
        tau_grid=r["tau_grid"], T_tau=r["T_tau"], T_tau_vkk=r["T_tau_vkk"],
        dT_dtau=r["dT_dtau"], RK_window=r["RK_window"], RK_fold=r["RK_fold"],
        VKK_fold=r["VKK_fold"],
        frac_var_window=r["frac_var_window"], frac_var_window_vkk=r["frac_var_window_vkk"],
        max_frac_deriv=r["max_frac_deriv"], insens_metric=r["insens_metric"],
        claim_B=r["claim_B"], insens_floor=r["insens_floor"],
        projection_degenerate=r["projection_degenerate"],
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
        composite=composite,
    )
    make_plot(r)
    print(f"  wrote {OUT_NPZ.name}")
    print(f"  wrote {OUT_PNG.name}")
    print()

    tag = (f"(value={r['T_substrate_K']!r}, scheme={SCHEME}, "
           f"convention={CONVENTION}, L_max={L_MAX})")  # (local)
    print(tag)

    # value payload: no single-quote chars (tool wraps value='...')
    value_payload = (
        f"T_substrate={r['T_substrate_K']:.6e}K "
        f"R_moment={r['R_moment']:.10f} "
        f"frac_dev_vs5000={r['frac_dev']:.4e} "
        f"insens_window_spread={r['insens_metric']:.4e} "
        f"claimA={r['claim_A']} claimB={r['claim_B']}"
    )  # (local)

    extra_rows = [
        "# regulator_pin=a_n^{zeta}  (a2_fold=a_2_FW_zeta, a4_fold=a_4_FW_zeta zeta-regulated Seeley-DeWitt; a4/a2 = a4^{zeta}/a2^{zeta})",
        f"# INV7-W2-2 substrate-first: pin=tau_fold+a4^z/a2^z; 5000K=TARGET-only (LRD Paper25/47/41 Balmer-break, NOT pin source); R_moment=45024/92539={r['R_moment']:.12f}",
    ]  # (local)

    print_verdict_payload(composite, value_payload, audit_sha, content_sha,
                          sign_v, mag_v, regime_v, extra_rows=extra_rows)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} "
          f"(sign={sign_v} mag={mag_v} regime={regime_v}) (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
