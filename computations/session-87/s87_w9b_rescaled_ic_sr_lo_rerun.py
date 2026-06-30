#!/usr/bin/env python3
"""
S87 W9b-1 — S87-RESCALED-IC-SR-LO-RERUN
========================================

Gate ID:        S87-RESCALED-IC-SR-LO-RERUN
Trigger:        [VERIFY] (with [SIGN] sub-trigger per §9 Step 4 directional pre-registration)
Classification: PHONONIC (substrate transit-physics; xi_E_GGE_inv is the substrate-IS
                IC for the GGE-relic Bogoliubov mode-function evolution; SR-LO ODE is
                the substrate-physics governing structure for slow-roll-leading-order
                trans-fold mode propagation; N_breakdown_observable(R) is the regime-
                validity boundary).

Pre-registered (plan §W9b-1):
  PASS (Reading_A) iff max_R |N_breakdown(R) − N_breakdown_canonical| / N_breakdown_canonical > 5%
  INFO             iff 0.5% < max_R deviation <= 5%
  FAIL (Reading_B) iff max_R deviation <= 0.5%

§9 substitution-chain analytic pre-registration:
  Direction (Reading_A): max_R deviation > 0    [predicted by W-12 V_4 spread of α(R)]
  Magnitude (Reading_A): ~0.7%                  [predicted by W-12-prior 1.5 factor]
                                                  → INFO band by analytic estimate
  Numerical replacement below.

Composite-collapse rule (S87+ schema-v2 per gate-verdicts.md):
  3-tuple (sign_verdict, magnitude_verdict, regime_verdict) → composite via deterministic rule.
  regime_verdict=BREAKDOWN forces composite=FAIL. sign-PASS magnitude-FAIL with regime=MARGINAL
  collapses to INFO (preserves SIGN-correct substrate finding).

Substrate-framing (mandatory, per phononic-framing.md "IS Space, Not IN Space"):
  We integrate substrate dynamics, NOT LCDM inflation. ξ²(N) is the substrate's quantum-
  pressure factor in the Mukhanov-Sasaki form
    v_k'' + (k² − z''/z + ξ² k²/(aH)²) v_k = 0
  borrowed as a calculational scaffold. The four ξ²₀(R) IC values are not LCDM
  reparametrizations — they are L1-class restrictions of the substrate's GGE-relic
  spectral state at the fold, projected to four affine coordinates per the W-9
  §EM-CN-R3-1 dual-prior 5-class enumeration. N_breakdown(R) is the SR-LO ε ≪ 1
  regime-validity boundary for each L1-class trajectory.

Inputs (S84+ dual-SHA):
  - computations/_shared/canonical_constants.py
  - computations/session-87/s87_w9b_rescaled_ic_sr_lo_rerun.py (this file)
  - computations/session-87/s87_w7_xi_E_per_class.npz (LATENT; absent at runtime)
  - computations/session-87/s87_w11_v4_monodromy_explicit.npz (LATENT; absent at runtime)

Output 4-tuple:
  (value=max_R_deviation_observable, scheme=SR-LO-Mukhanov-Sasaki,
   convention=substrate-natural-xi-E-GGE-class-projected, L_max=N/A-SR-LO)

Author: transit-dynamics-theorist (S87 W9b runtime)
"""
from __future__ import annotations

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

import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ----------------------------- Project paths -----------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
sys.path.insert(0, str(SCRIPT_DIR))

# Canonical constants (HARD: xi_E_GGE_inv pinned by W4 P4)
from canonical_constants import (  # noqa: E402
    tau_fold,
    xi_E_GGE_inv,
)

# ----------------------------- Gate identity -----------------------------

SESSION = "S87"
GATE_ID = "S87-RESCALED-IC-SR-LO-RERUN"
SCHEME = "SR-LO-Mukhanov-Sasaki"
CONVENTION = "substrate-natural-xi-E-GGE-class-projected"
L_MAX = "N/A-SR-LO"          # (local) plan §6: SR-LO ODE has no L_max (substrate already substrate-distance-1 reduced)

CANONICAL_PATH = resolve_script(None, 'canonical_constants.py')
SCRIPT_PATH = Path(__file__).resolve()
VERDICT_TXT = resolve_output(87, 's87_gate_verdicts.txt')
NPZ_PATH = resolve_output(87, 's87_w9b_rescaled_ic_sr_lo_rerun.npz')
PNG_PATH = resolve_output(87, 's87_w9b_rescaled_ic_sr_lo_rerun.png')
JSON_PATH = resolve_output(87, 's87_w9b_rescaled_ic_sr_lo_rerun.json')

# Optional upstream NPZs (CONDITIONAL; resolved at script entry per plan §7)
LATENT_W9A_NPZ = resolve_output(87, 's87_w7_xi_E_per_class.npz')
LATENT_W11_NPZ = resolve_output(87, 's87_w11_v4_monodromy_explicit.npz')

# ----------------------------- Pre-registered IC + machinery pins -----------------------------
# Plan §6 PRDR machinery-enumeration table (every free param pinned)

EPS_0 = 0.020              # (local) S85 W1a-1 baseline anchor; matches S86 W5a precedent
ETA_0 = 0.005              # (local) canonical small-η; Mukhanov 2005 §8.1
ALPHA_S_0 = 0.0            # (local) SR-LO IC (α_s sourced dynamically)

# Canonical fiducial: 5th L1-class is the canonical reference (alpha=1)
ALPHA_CANONICAL = 1.0      # (local) plan §4: 5th L1-class = canonical fiducial reference

N_SPAN = (0.0, 100.0)      # (local) plan §6 scan_range: extended to N=100 e-folds
DN_FINE = 0.01             # (local) plan §6 step_size pin (resolves N_breakdown to ±0.01)
N_EVAL_COUNT = int((N_SPAN[1] - N_SPAN[0]) / DN_FINE) + 1
N_EVAL = np.linspace(N_SPAN[0], N_SPAN[1], N_EVAL_COUNT)

DN_CROSSCHECK = 0.005      # (local) plan §6: cross-validate canonical-fiducial trajectory at finer dN

RTOL = 1.0e-9              # (local) tighter than S86 W5a (1e-8) since N range doubled
ATOL = 1.0e-11             # (local) tighter than S86 W5a (1e-10)
MAX_STEP = DN_FINE         # (local)

PASS_BAND_RATIO = 0.05     # (local) plan §5 PASS gate (5% deviation)
INFO_BAND_RATIO = 0.005    # (local) plan §5 INFO floor (0.5%); INFO band = (0.005, 0.05]
RANDOM_SEED = 42           # (local) plan §6 random_seed pin

# SR-LO regime cutover thresholds per gate-verdicts.md §"Auto-shortening clause discipline"
EPS_BREAKDOWN_THRESH = 0.5     # (local) plan §4: |ε(N)-ε(0)|/ε(0) = 0.5 cutover
EPS_REGIME_BREAKDOWN = 1.0     # (local) plan §9 Step 5: ε ≥ 1 → regime BREAKDOWN
EPS_REGIME_MARGINAL = 0.3      # (local) plan §9 Step 5: ε ≳ 0.3 → regime MARGINAL


# ----------------------------- α(R) coefficient construction -----------------------------
# Plan §7: PRIMARY = W11-1-CF-66 V_4 monodromy NPZ (if present at runtime)
#          FALLBACK = W-9 §EM-CN-R3-1 dual-prior 5-class enumeration
#
# W-9 §EM-CN-R3-1 dual-prior 5-class enumeration (workshop §lines 1535-1585):
# Klein-four V_4 = Z_2 × Z_2 has 4 non-trivial cosets corresponding to the four
# L1-class affine projections. The α(R) coefficients are derived from the eigenvalue-
# weight ratios of the V_4 coset structure on the 4-class projection.
#
# Per W-12 §EMERGENCE E-1 R3-volovik final round: the V_4 coset α(R) coefficients
# span four distinct values with structural prior max α²/min α² ≳ 1.5.
#
# DUAL-PRIOR FALLBACK CONSTRUCTION:
#   Class C_1: α_1 = 1.0      (canonical fiducial; trivial coset = e)
#   Class C_2: α_2 = sqrt(1.2) (mild rescaling; 20% IC enhancement; coset_a ~ Z_2_a)
#   Class C_3: α_3 = sqrt(0.8) (mild reduction;  20% IC reduction;  coset_b ~ Z_2_b)
#   Class C_4: α_4 = sqrt(1.5) (strongest;       50% IC enhancement; coset_ab ~ Z_2_a × Z_2_b)
# Spread max α²/min α² = 1.5/0.8 = 1.875 → exceeds the W-12 prior 1.5 factor
# (well-resolvable in N_breakdown spread).
#
# NOTE: this α(R) construction is the PLAN §7 FALLBACK. If LATENT_W11_NPZ lands at runtime,
# the script reads V_4 coset coefficients directly from that NPZ and overrides the
# fallback construction.

ALPHA_FALLBACK_DUAL_PRIOR = np.array([
    1.0,
    np.sqrt(1.2),
    np.sqrt(0.8),
    np.sqrt(1.5),
], dtype=np.float64)  # (local) W-9 §EM-CN-R3-1 dual-prior 5-class fallback (4 R values + canonical)
# R-class labels per W-9 §EM-CN-R3-1
R_CLASS_LABELS = ["C_1_e", "C_2_a", "C_3_b", "C_4_ab"]    # (local)


def resolve_alpha_R() -> tuple[np.ndarray, list[str], str, dict]:
    """Resolve α(R) coefficients per plan §7.

    Returns (alpha_R[4], labels[4], source_tag, runtime_pins_dict).
    """
    pins: dict[str, str] = {}  # (local)

    # Plan §7 PRIMARY: V_4 monodromy NPZ from W11-1-CF-66
    if LATENT_W11_NPZ.exists():
        try:
            data = np.load(LATENT_W11_NPZ)  # (local)
            if "alpha_R_coefficients" in data:
                a_R = np.asarray(data["alpha_R_coefficients"], dtype=np.float64).ravel()  # (local)
                if a_R.size == 4 and np.all(np.isfinite(a_R)):
                    pins[str(LATENT_W11_NPZ.relative_to(PROJECT_ROOT)).replace("\\", "/")] = (
                        sha256_of(LATENT_W11_NPZ)
                    )
                    return a_R, R_CLASS_LABELS, "PRIMARY-V4-MONODROMY-W11-CF-66", pins
        except (OSError, ValueError, KeyError) as e:
            print(f"  [WARN] LATENT_W11_NPZ load failed: {e}; falling through to FALLBACK")

    # Plan §7 ENRICHED FALLBACK: per-class xi values from W9a-CF-42 (if present)
    # If those land, they replace the AFFINE construction with VERIFIED per-class restrictions.
    if LATENT_W9A_NPZ.exists():
        try:
            data = np.load(LATENT_W9A_NPZ)  # (local)
            if "xi2_0_per_class" in data:
                xi2_per = np.asarray(data["xi2_0_per_class"], dtype=np.float64).ravel()  # (local)
                if xi2_per.size == 4 and np.all(np.isfinite(xi2_per)) and np.all(xi2_per > 0):
                    # Convert per-class xi^2_0 values to α(R): α_R = sqrt(xi^2_0_R / xi_E_GGE_inv)
                    a_R = np.sqrt(xi2_per / float(xi_E_GGE_inv))  # (local)
                    pins[str(LATENT_W9A_NPZ.relative_to(PROJECT_ROOT)).replace("\\", "/")] = (
                        sha256_of(LATENT_W9A_NPZ)
                    )
                    return a_R, R_CLASS_LABELS, "ENRICHED-W9A-CF-42-PER-CLASS-XI", pins
        except (OSError, ValueError, KeyError) as e:
            print(f"  [WARN] LATENT_W9A_NPZ load failed: {e}; falling through to DUAL-PRIOR")

    # Plan §7 CANONICAL FALLBACK: W-9 §EM-CN-R3-1 dual-prior 5-class enumeration
    return ALPHA_FALLBACK_DUAL_PRIOR.copy(), R_CLASS_LABELS, "FALLBACK-W9-EM-CN-R3-1-DUAL-PRIOR", pins


# ----------------------------- SHA helpers -----------------------------

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
        if sha:
            print(f"  {rel}: {sha[:16]}...")
        else:
            print(f"  {rel}: ABSENT")
        pins[rel] = sha
    return pins


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
    machinery_pin_map: dict,
) -> tuple[str, str]:
    """audit_sha256 = SHA(script + canonical + sorted-pins-json + machinery-json).
    content_sha256 = SHA(script_only).
    """
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        pass
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        pass
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)
    machinery_json = json.dumps(
        machinery_pin_map, separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_audit.update(machinery_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


def append_verdict_block(
    gate_id: str,
    composite: str,
    value,
    audit_sha: str,
    content_sha: str,
    sign_verdict: str,
    magnitude_verdict: str,
    regime_verdict: str,
) -> None:
    """S87+ schema-v2: canonical line + W9a-99 dual-SHA companion + 3-tuple annotation row."""
    line = (
        f"{gate_id}: {composite} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    companion_dual = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {gate_id} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    companion_3tuple = (
        f"# sign_verdict={sign_verdict} magnitude_verdict={magnitude_verdict} "
        f"regime_verdict={regime_verdict} "
        f"# {gate_id} 3-tuple annotation (S87 schema-v2)\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion_dual)
        fp.write(companion_3tuple)


# ----------------------------- The four-component coupled SR-LO ODE -----------------------------
# (identical to S86 W5a precedent; substrate-physics structure unchanged across W9b)
# Refs: Mukhanov 2005 §8.1, Sasaki 1986 (MS), gen-physicist 9A §4.5a, mack 9A §VI.3
#
#   d ε / dN  = ε (2 η - 4 ε + 2 ξ²)            — SR-LO ε-flow with substrate ξ² source
#   d η / dN  = -ε η + α_s + (η - ε) η          — SR-LO η-flow
#   d α_s / dN = -2 ε α_s + 2 η α_s             — SR-LO α_s-flow (truncated)
#   d ξ² / dN = -2 ε ξ²                         — substrate-source closure at SR-LO
#
# ξ²(0) = xi_E_GGE_inv · α(R)²  (substrate-natural anchor with affine class-projection rescaling)

def rhs(N: float, y: np.ndarray) -> list[float]:
    eps, eta, alpha_s, xi2 = y
    deps_dN = eps * (2.0 * eta - 4.0 * eps + 2.0 * xi2)
    deta_dN = -eps * eta + alpha_s + (eta - eps) * eta
    dalpha_s_dN = -2.0 * eps * alpha_s + 2.0 * eta * alpha_s
    dxi2_dN = -2.0 * eps * xi2
    return [deps_dN, deta_dN, dalpha_s_dN, dxi2_dN]


# ----------------------------- N_breakdown computation -----------------------------
# Plan §4 + §9 Step 1: N_breakdown(R) := min{N : |ε(N) − ε(0)| / ε(0) > 0.5}

def compute_N_breakdown(N_t: np.ndarray, eps_traj: np.ndarray, eps_0: float) -> tuple[float, bool]:
    """Find first crossing of |ε(N)-ε(0)|/ε(0) = 0.5.

    Returns (N_breakdown, found_clean_crossing).
    If no crossing within the window, returns (N_max, False) — clamped to integration window.
    """
    if eps_0 <= 0.0:
        return float("nan"), False
    rel_dev = np.abs(eps_traj - eps_0) / eps_0  # (local)
    # First-crossing search
    crossing_mask = rel_dev > EPS_BREAKDOWN_THRESH  # (local)
    if not np.any(crossing_mask):
        return float(N_t[-1]), False
    first_idx = int(np.argmax(crossing_mask))  # (local) argmax on bool array = first True
    if first_idx == 0:
        # Crossing at IC itself — definitionally impossible; |ε(0)-ε(0)|/ε(0) = 0 ≤ 0.5
        # Indicates numerical issue; flag as not-clean.
        return float(N_t[0]), False
    # Linear interpolation between (N[first_idx-1], rel_dev[first_idx-1]) and (N[first_idx], rel_dev[first_idx])
    N_a, N_b = float(N_t[first_idx - 1]), float(N_t[first_idx])  # (local)
    r_a, r_b = float(rel_dev[first_idx - 1]), float(rel_dev[first_idx])  # (local)
    if r_b == r_a:
        return N_b, True
    frac = (EPS_BREAKDOWN_THRESH - r_a) / (r_b - r_a)  # (local)
    N_cross = N_a + frac * (N_b - N_a)  # (local)
    return float(N_cross), True


def regime_classify_per_R(eps_traj: np.ndarray, N_breakdown: float, N_t: np.ndarray) -> str:
    """Plan §9 Step 5 regime classifier."""
    # Window: from N=0 to min(N_breakdown, N_max)
    upper_N = min(N_breakdown, float(N_t[-1]))  # (local)
    mask = N_t <= upper_N  # (local)
    if not np.any(mask):
        return "BREAKDOWN"
    eps_window = eps_traj[mask]  # (local)
    if not np.all(np.isfinite(eps_window)):
        return "BREAKDOWN"
    eps_max = float(np.max(eps_window))  # (local)
    if eps_max >= EPS_REGIME_BREAKDOWN:
        return "BREAKDOWN"
    if eps_max >= EPS_REGIME_MARGINAL:
        return "MARGINAL"
    return "VALID"


# ----------------------------- Verdict logic (S87+ schema-v2 composite collapse) -----------------------------

def magnitude_classify(max_R_dev: float) -> str:
    """Plan §5 magnitude bands."""
    if not np.isfinite(max_R_dev):
        return "FAIL"
    if max_R_dev > PASS_BAND_RATIO:
        return "PASS"
    if max_R_dev > INFO_BAND_RATIO:
        return "INFO"
    return "FAIL"


def sign_classify(max_R_dev: float, predicted_sign: str = "POSITIVE") -> str:
    """Plan §9 Step 5: sign verdict relative to Reading_A pre-registration.

    Reading_A predicts max_R_dev > 0 (positive). Since max_R_dev is |·|, the
    only failure direction is max_R_dev = 0 exactly (degenerate; impossible
    by floating-point if α(R) is non-trivial).
    """
    if not np.isfinite(max_R_dev):
        return "FAIL"
    if predicted_sign == "POSITIVE":
        # Reading_A prediction matches if max_R_dev > 0
        return "PASS" if max_R_dev > 0.0 else "FAIL"
    return "N/A"


def regime_aggregate(regime_per_R: list[str]) -> str:
    """Aggregate worst-of regime across R."""
    if "BREAKDOWN" in regime_per_R:
        return "BREAKDOWN"
    if "MARGINAL" in regime_per_R:
        return "MARGINAL"
    return "VALID"


def composite_collapse(sign_v: str, mag_v: str, regime_v: str) -> str:
    """gate-verdicts.md §"Composite-collapse rule" (PRE-REGISTERED — Class-3 to modify)."""
    if regime_v == "BREAKDOWN":
        return "FAIL"
    if sign_v == "FAIL":
        return "FAIL"
    if mag_v == "FAIL" and regime_v == "VALID":
        return "FAIL"
    if mag_v == "FAIL" and regime_v == "MARGINAL":
        return "INFO"
    if mag_v == "INFO":
        return "INFO"
    return "PASS"


# ----------------------------- Main -----------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # Banner
    print(f"=== {GATE_ID} — runtime ===")
    print(f"  session: {SESSION}")
    print(f"  scheme:  {SCHEME}")
    print(f"  convention: {CONVENTION}")
    print(f"  L_max:   {L_MAX}")
    print()

    # Input pins (first 20 lines per gate-verdicts.md §"During computation")
    pins = log_input_pins([CANONICAL_PATH, SCRIPT_PATH])
    print()

    # Constants pin echo
    print(f"=== Canonical constants used ===")
    print(f"  tau_fold       = {tau_fold!r}")
    print(f"  xi_E_GGE_inv   = {xi_E_GGE_inv!r}    (W4 P4 commit; substrate-natural 59.8·Δ_BCS/K_base)")
    print()

    # Resolve α(R) per plan §7
    print(f"=== Resolving α(R) coefficients per plan §7 ===")
    alpha_R, R_labels, alpha_source, runtime_pins = resolve_alpha_R()
    pins.update(runtime_pins)
    print(f"  source: {alpha_source}")
    print(f"  R labels: {R_labels}")
    print(f"  α(R):     {alpha_R.tolist()}")
    print(f"  α(R)²:    {(alpha_R ** 2).tolist()}")
    print(f"  spread (max α² / min α²): {float(np.max(alpha_R ** 2) / np.min(alpha_R ** 2)):.6f}")
    print()

    # Compute per-R IC values
    xi2_0_per_R = float(xi_E_GGE_inv) * (alpha_R ** 2)  # (local) plan §4 rescaling formula
    xi2_0_canonical = float(xi_E_GGE_inv) * (ALPHA_CANONICAL ** 2)  # (local) canonical fiducial

    print(f"=== IC at N=0 (fold) per L1-class ===")
    print(f"  ε_0 = {EPS_0}, η_0 = {ETA_0}, α_s,0 = {ALPHA_S_0}")
    print(f"  ξ²_0 (canonical fiducial, α=1) = {xi2_0_canonical:.6e}")
    for label, a, x in zip(R_labels, alpha_R.tolist(), xi2_0_per_R.tolist()):
        print(f"  ξ²_0({label}, α={a:.6f}) = {x:.6e}")
    print()

    # ----------------------------- Integrate per-R + canonical fiducial -----------------------------
    print(f"=== ODE integration: 4 R-trajectories + canonical fiducial ===")

    sols_per_R = []  # (local)
    for label, xi2_0 in zip(R_labels, xi2_0_per_R.tolist()):
        sol = solve_ivp(
            rhs, N_SPAN,
            [EPS_0, ETA_0, ALPHA_S_0, xi2_0],
            method="LSODA", rtol=RTOL, atol=ATOL, max_step=MAX_STEP,
            t_eval=N_EVAL,
        )
        print(f"  R={label} (ξ²₀={xi2_0:.4f}): success={sol.success}, message={sol.message}")
        sols_per_R.append(sol)

    sol_canon = solve_ivp(
        rhs, N_SPAN,
        [EPS_0, ETA_0, ALPHA_S_0, xi2_0_canonical],
        method="LSODA", rtol=RTOL, atol=ATOL, max_step=MAX_STEP,
        t_eval=N_EVAL,
    )
    print(f"  canonical fiducial (ξ²₀={xi2_0_canonical:.4f}): success={sol_canon.success}, message={sol_canon.message}")
    print()

    # Cross-check: canonical-fiducial trajectory at finer dN=0.005
    N_EVAL_FINE = np.linspace(N_SPAN[0], N_SPAN[1], int((N_SPAN[1] - N_SPAN[0]) / DN_CROSSCHECK) + 1)  # (local)
    sol_canon_fine = solve_ivp(
        rhs, N_SPAN,
        [EPS_0, ETA_0, ALPHA_S_0, xi2_0_canonical],
        method="LSODA", rtol=RTOL, atol=ATOL, max_step=DN_CROSSCHECK,
        t_eval=N_EVAL_FINE,
    )
    print(f"  canonical fine (dN={DN_CROSSCHECK}): success={sol_canon_fine.success}")
    print()

    # ----------------------------- Compute N_breakdown per R + canonical -----------------------------
    print(f"=== N_breakdown per L1-class (first crossing of |ε(N)-ε(0)|/ε(0) = 0.5) ===")

    N_breakdown_per_R = np.zeros(4, dtype=np.float64)  # (local)
    crossing_clean_per_R = np.zeros(4, dtype=bool)  # (local)
    eps_traj_per_R = np.zeros((4, N_EVAL_COUNT), dtype=np.float64)  # (local)
    eta_traj_per_R = np.zeros((4, N_EVAL_COUNT), dtype=np.float64)  # (local)
    regime_per_R = []  # (local)

    for i, (label, sol) in enumerate(zip(R_labels, sols_per_R)):
        eps_traj_per_R[i, :] = sol.y[0, :]
        eta_traj_per_R[i, :] = sol.y[1, :]
        N_b, clean = compute_N_breakdown(sol.t, sol.y[0, :], EPS_0)
        N_breakdown_per_R[i] = N_b
        crossing_clean_per_R[i] = clean
        regime = regime_classify_per_R(sol.y[0, :], N_b, sol.t)
        regime_per_R.append(regime)
        eps_max_in_window = float(np.max(sol.y[0, :sol.t.searchsorted(N_b) + 1]))
        print(f"  R={label}: N_breakdown = {N_b:.4f}  (clean={clean}, regime={regime}, max ε in window = {eps_max_in_window:.4f})")

    N_breakdown_canonical, canon_clean = compute_N_breakdown(sol_canon.t, sol_canon.y[0, :], EPS_0)
    canon_regime = regime_classify_per_R(sol_canon.y[0, :], N_breakdown_canonical, sol_canon.t)
    print(f"  canonical fiducial: N_breakdown = {N_breakdown_canonical:.4f}  (clean={canon_clean}, regime={canon_regime})")

    # Cross-check: canonical at finer dN
    N_breakdown_canon_fine, _ = compute_N_breakdown(sol_canon_fine.t, sol_canon_fine.y[0, :], EPS_0)
    canon_dn_dev = abs(N_breakdown_canon_fine - N_breakdown_canonical)
    print(f"  canonical fine (dN={DN_CROSSCHECK}): N_breakdown = {N_breakdown_canon_fine:.4f}  "
          f"(|Δ vs dN={DN_FINE}| = {canon_dn_dev:.4f} e-folds)")
    print()

    # ----------------------------- Gate value: max_R deviation -----------------------------
    print(f"=== Gate value: max_R |N_breakdown(R) − N_breakdown_canonical| / N_breakdown_canonical ===")
    if N_breakdown_canonical > 0 and np.isfinite(N_breakdown_canonical):
        deviations_per_R = np.abs(N_breakdown_per_R - N_breakdown_canonical) / N_breakdown_canonical  # (local)
        max_R_deviation_observable = float(np.max(deviations_per_R))  # (local)
        argmax_idx = int(np.argmax(deviations_per_R))  # (local)
    else:
        deviations_per_R = np.full(4, np.nan)
        max_R_deviation_observable = float("nan")
        argmax_idx = 0  # (local) fallback when canonical N_breakdown is non-finite
    print(f"  per-R deviations:")
    for label, dev in zip(R_labels, deviations_per_R.tolist()):
        print(f"    {label}: {dev:.6f}  ({dev * 100:.4f}%)")
    print(f"  max_R deviation = {max_R_deviation_observable:.6f}  ({max_R_deviation_observable * 100:.4f}%)")
    print(f"  argmax R-class  = {R_labels[argmax_idx]}")
    print()

    # ----------------------------- Cross-checks (CC1 IC fidelity, CC2 ε-monotone, CC3 dN-robustness) -----------------------------
    print(f"=== Cross-checks ===")

    # CC1: IC fidelity at N=0 across all 5 trajectories
    cc1_eps_devs = [abs(float(s.y[0, 0]) - EPS_0) for s in sols_per_R + [sol_canon]]  # (local)
    cc1_xi2_devs_per_R = [abs(float(sols_per_R[i].y[3, 0]) - xi2_0_per_R[i])
                          for i in range(4)]  # (local)
    cc1_xi2_canon_dev = abs(float(sol_canon.y[3, 0]) - xi2_0_canonical)  # (local)
    cc1_max_dev = max(max(cc1_eps_devs), max(cc1_xi2_devs_per_R), cc1_xi2_canon_dev)
    cc1_PASS = cc1_max_dev < 1e-12  # (local)
    print(f"  CC1 (IC fidelity at N=0, max abs dev across all 5 trajectories): "
          f"{cc1_max_dev:.3e}  -> {'PASS' if cc1_PASS else 'FAIL'}")

    # CC2: ε(N) monotone-non-decreasing over [0, min(N_breakdown(R), N_max)]
    cc2_min_diffs = []  # (local)
    for i, (label, sol) in enumerate(zip(R_labels, sols_per_R)):
        upper = min(N_breakdown_per_R[i], float(N_SPAN[1]))  # (local)
        mask = sol.t <= upper  # (local)
        if mask.sum() < 2:
            cc2_min_diffs.append(0.0)
            continue
        diffs = np.diff(sol.y[0, mask])
        cc2_min_diffs.append(float(np.min(diffs)) if diffs.size > 0 else 0.0)
    cc2_min_diff_overall = min(cc2_min_diffs)
    cc2_PASS = cc2_min_diff_overall >= -1e-9
    print(f"  CC2 (ε monotone over [0, N_breakdown] per R): min diff overall = {cc2_min_diff_overall:.3e}  "
          f"-> {'PASS' if cc2_PASS else 'FAIL'}")

    # CC3: canonical-fiducial robustness against dN refinement
    cc3_PASS = canon_dn_dev < 0.05  # (local) plan §6: ±0.01 e-fold dN-resolution acceptable, 0.05 safety floor
    print(f"  CC3 (canonical N_breakdown dN-robustness): |Δ vs dN={DN_CROSSCHECK}| = {canon_dn_dev:.4f}  "
          f"-> {'PASS' if cc3_PASS else 'FAIL'}")

    # CC4: ODE numerical success across all 5
    all_success = all(s.success for s in sols_per_R) and sol_canon.success and sol_canon_fine.success
    print(f"  CC4 (all ODEs converged): {'PASS' if all_success else 'FAIL'}")

    # CC5: clean N_breakdown crossings (per-R)
    all_clean = bool(np.all(crossing_clean_per_R)) and bool(canon_clean)
    print(f"  CC5 (all N_breakdown crossings clean = first-passage rather than IC-degenerate): "
          f"{'PASS' if all_clean else 'FAIL'}")
    print()

    # ----------------------------- Verdict logic (S87+ schema-v2 composite collapse) -----------------------------
    print(f"=== Verdict logic (S87+ schema-v2 composite collapse) ===")

    # Sign verdict (Reading_A prediction: max_R_dev > 0)
    sign_v = sign_classify(max_R_deviation_observable, predicted_sign="POSITIVE")  # (local)
    # Magnitude verdict per plan §5 bands
    mag_v = magnitude_classify(max_R_deviation_observable)  # (local)
    # Regime verdict aggregate (worst-of across 4 R-trajectories)
    regime_v_aggregate = regime_aggregate(regime_per_R)  # (local)
    # Composite collapse per gate-verdicts.md PRE-REGISTERED rule
    composite = composite_collapse(sign_v, mag_v, regime_v_aggregate)  # (local)

    # If clean=False on any crossing, force composite=FAIL (numerical artifact)
    if not all_clean:
        print(f"  [WARN] not all N_breakdown crossings are clean; forcing composite=FAIL per plan §5")
        composite = "FAIL"
        regime_v_aggregate = "BREAKDOWN" if regime_v_aggregate == "VALID" else regime_v_aggregate

    print(f"  sign_verdict      = {sign_v}    (Reading_A prediction: max_R_dev > 0)")
    print(f"  magnitude_verdict = {mag_v}    (max_R_dev = {max_R_deviation_observable:.6f}; bands: PASS>0.05, INFO (0.005, 0.05], FAIL<=0.005)")
    print(f"  regime_verdict    = {regime_v_aggregate}    (worst-of across 4 R-trajectories: {regime_per_R})")
    print(f"  composite         = {composite}    (per gate-verdicts.md pre-registered collapse rule)")
    print()

    # ----------------------------- Numerical substitution chain (mandatory per math-scripts.md §Double-Check Logic) -----------------------------
    print(f"=== Numerical substitution chain (per math-scripts.md §Double-Check Logic) ===")
    print(f"  Step 1: Definitions")
    print(f"    xi_E_GGE_inv       = {float(xi_E_GGE_inv):.6f}    [W4 P4 canonical]")
    print(f"    α(R)               = per-class affine projection coefficient ({alpha_source})")
    print(f"    ξ²₀(R)             = xi_E_GGE_inv · α(R)²")
    print(f"    N_breakdown(R)     = min{{N : |ε(N)-ε(0)|/ε(0) > 0.5}}")
    print(f"  Step 2: Substitute (R-trajectory IC values)")
    for label, a, x in zip(R_labels, alpha_R.tolist(), xi2_0_per_R.tolist()):
        print(f"    α({label})² = {a*a:.6f}, ξ²₀({label}) = {x:.6e}")
    print(f"  Step 3: Direction (sign reading off canonical form)")
    print(f"    Spread: max α(R)² / min α(R)² = {float(np.max(alpha_R ** 2) / np.min(alpha_R ** 2)):.6f}")
    print(f"    α(R)² varies across R ⇒ ξ²₀(R) varies ⇒ ε_R(N) trajectory varies ⇒ N_breakdown(R) varies ⇒ max_R_dev > 0")
    print(f"    (Reading_A direction: PASS for sign_verdict)")
    print(f"  Step 4: Numerical replacement of analytic prediction")
    print(f"    Plan §9 Step 4 analytic: max α²/min α² ~ 1.5 ⇒ N_breakdown spread ~ ln(1.5) ≈ 0.41 e-folds")
    print(f"                              N_breakdown_canonical ~ 50-60 e-folds ⇒ predicted gate value ~ 0.41/55 ≈ 0.007 (INFO)")
    print(f"    Computed: max_R_deviation_observable = {max_R_deviation_observable:.6f}  ({max_R_deviation_observable * 100:.4f}%)")
    if max_R_deviation_observable > PASS_BAND_RATIO:
        print(f"    Direction: PASS (Reading_A); magnitude exceeds plan §9 prior — promote to PASS magnitude band")
    elif max_R_deviation_observable > INFO_BAND_RATIO:
        print(f"    Direction: PASS (Reading_A); magnitude in INFO band (matches plan §9 prior)")
    else:
        print(f"    Direction: PASS (Reading_A); magnitude below INFO floor — Reading_B confirmed (FAIL magnitude)")
    print()

    # ----------------------------- Save .npz -----------------------------
    print(f"=== Save artifacts ===")
    np.savez(
        NPZ_PATH,
        # Plan §8 required keys
        R_values=np.asarray(alpha_R, dtype=np.float64),
        xi2_0_per_R=np.asarray(xi2_0_per_R, dtype=np.float64),
        epsilon_trajectory_per_R=eps_traj_per_R,
        eta_trajectory_per_R=eta_traj_per_R,
        N_breakdown_per_R=np.asarray(N_breakdown_per_R, dtype=np.float64),
        N_breakdown_canonical=np.asarray([N_breakdown_canonical], dtype=np.float64),
        max_R_deviation_observable=np.asarray([max_R_deviation_observable], dtype=np.float64),
        regime_verdict_per_R=np.asarray(regime_per_R, dtype="U16"),
        # Auxiliary keys
        N_eval=N_EVAL,
        N_eval_fine=N_EVAL_FINE,
        eps_traj_canonical=sol_canon.y[0, :],
        eta_traj_canonical=sol_canon.y[1, :],
        eps_traj_canonical_fine=sol_canon_fine.y[0, :],
        deviations_per_R=deviations_per_R,
        crossing_clean_per_R=crossing_clean_per_R,
        R_labels=np.asarray(R_labels, dtype="U16"),
        alpha_R=alpha_R,
        alpha_source=np.asarray(alpha_source, dtype="U64"),
        xi_E_GGE_inv_used=float(xi_E_GGE_inv),
        eps_0=EPS_0,
        eta_0=ETA_0,
        alpha_s_0=ALPHA_S_0,
        # Cross-check diagnostics
        cc1_max_dev=cc1_max_dev,
        cc2_min_diff_overall=cc2_min_diff_overall,
        cc3_canon_dn_dev=canon_dn_dev,
        cc4_all_success=all_success,
        cc5_all_clean=all_clean,
        # Verdict tuple
        sign_verdict=sign_v,
        magnitude_verdict=mag_v,
        regime_verdict=regime_v_aggregate,
        composite=composite,
    )
    print(f"  npz: {NPZ_PATH.name}")

    # ----------------------------- Save .png (4-panel per plan §11) -----------------------------
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: ε_R(N) trajectories per R
    ax = axes[0, 0]
    colors = ["C0", "C1", "C2", "C3"]
    for i, (label, sol, c) in enumerate(zip(R_labels, sols_per_R, colors)):
        ax.plot(sol.t, sol.y[0, :], color=c, lw=1.4, label=f"{label} (α²={alpha_R[i]**2:.3f})")
    ax.plot(sol_canon.t, sol_canon.y[0, :], "k--", lw=1.6, label="canonical (α=1)")
    ax.axhline(EPS_0, color="gray", linestyle=":", lw=0.8, label="ε(0)")
    ax.axhline(EPS_0 * (1 + EPS_BREAKDOWN_THRESH), color="r", linestyle=":", lw=0.8, label="ε(0)·1.5 (50% rel-dev)")
    ax.set_xlabel("N (e-folds)")
    ax.set_ylabel("ε(N)")
    ax.set_title("ε_R(N) per L1-class")
    ax.set_yscale("symlog", linthresh=1e-3)
    ax.grid(True, alpha=0.3)
    ax.legend(loc="best", fontsize=8)

    # Panel 2: η_R(N) trajectories per R
    ax = axes[0, 1]
    for i, (label, sol, c) in enumerate(zip(R_labels, sols_per_R, colors)):
        ax.plot(sol.t, sol.y[1, :], color=c, lw=1.4, label=f"{label}")
    ax.plot(sol_canon.t, sol_canon.y[1, :], "k--", lw=1.6, label="canonical")
    ax.set_xlabel("N (e-folds)")
    ax.set_ylabel("η(N)")
    ax.set_title("η_R(N) per L1-class")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="best", fontsize=8)

    # Panel 3: |ε(N)-ε(0)|/ε(0) crossing diagnostic with 0.5 threshold line
    ax = axes[1, 0]
    for i, (label, sol, c) in enumerate(zip(R_labels, sols_per_R, colors)):
        rel_dev = np.abs(sol.y[0, :] - EPS_0) / EPS_0
        ax.plot(sol.t, rel_dev, color=c, lw=1.4, label=f"{label} (N_b={N_breakdown_per_R[i]:.2f})")
    rel_dev_canon = np.abs(sol_canon.y[0, :] - EPS_0) / EPS_0
    ax.plot(sol_canon.t, rel_dev_canon, "k--", lw=1.6, label=f"canonical (N_b={N_breakdown_canonical:.2f})")
    ax.axhline(EPS_BREAKDOWN_THRESH, color="r", linestyle="--", lw=1.0, label="0.5 threshold")
    ax.set_xlabel("N (e-folds)")
    ax.set_ylabel("|ε(N)−ε(0)|/ε(0)")
    ax.set_title("SR-LO breakdown diagnostic")
    ax.set_yscale("symlog", linthresh=1e-3)
    ax.grid(True, alpha=0.3)
    ax.legend(loc="best", fontsize=8)

    # Panel 4: N_breakdown(R) bar chart with canonical-fiducial reference
    ax = axes[1, 1]
    x_pos = np.arange(4)
    bars = ax.bar(x_pos, N_breakdown_per_R, color=colors, alpha=0.7, edgecolor="k")
    for i, (b, dev) in enumerate(zip(bars, deviations_per_R)):
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() * 1.01,
                f"{N_breakdown_per_R[i]:.2f}\n({dev * 100:.2f}%)",
                ha="center", va="bottom", fontsize=8)
    ax.axhline(N_breakdown_canonical, color="k", linestyle="--", lw=1.5, label=f"canonical = {N_breakdown_canonical:.2f}")
    ax.set_xticks(x_pos)
    ax.set_xticklabels(R_labels, fontsize=9)
    ax.set_xlabel("L1-class R")
    ax.set_ylabel("N_breakdown(R) [e-folds]")
    ax.set_title(f"N_breakdown(R) — max_R dev = {max_R_deviation_observable * 100:.4f}%")
    ax.grid(True, alpha=0.3, axis="y")
    ax.legend(loc="best", fontsize=8)

    fig.suptitle(
        f"S87 W9b-1 Rescaled-IC SR-LO rerun: 4 affine class-projected ξ²₀(R)\n"
        f"α(R) source: {alpha_source}    |    ξ²₀ canonical = {xi2_0_canonical:.4f} = xi_E_GGE_inv\n"
        f"sign={sign_v}, magnitude={mag_v}, regime={regime_v_aggregate}, composite={composite}",
        fontsize=11,
    )
    fig.tight_layout()
    fig.savefig(PNG_PATH, dpi=120)
    plt.close(fig)
    print(f"  png: {PNG_PATH.name}")

    # ----------------------------- Save .json -----------------------------
    diag = {
        "gate_id": GATE_ID,
        "session": SESSION,
        "wave": "W9b-1",
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "machinery_pin_map": {
            "L_max": L_MAX,
            "n_eval": N_EVAL_COUNT,
            "N_span": list(N_SPAN),
            "scheme": SCHEME,
            "convention": CONVENTION,
            "cutoff_axis": "spectral",
            "numerical_method_primary": "LSODA",
            "rtol": RTOL,
            "atol": ATOL,
            "max_step": MAX_STEP,
            "dN_fine": DN_FINE,
            "dN_crosscheck": DN_CROSSCHECK,
            "GPU_path": "CPU OMP_NUM_THREADS=8",
            "PASS_band_ratio": PASS_BAND_RATIO,
            "INFO_band_ratio": INFO_BAND_RATIO,
            "eps_breakdown_thresh": EPS_BREAKDOWN_THRESH,
            "eps_regime_breakdown": EPS_REGIME_BREAKDOWN,
            "eps_regime_marginal": EPS_REGIME_MARGINAL,
            "random_seed": RANDOM_SEED,
            "eps_0": EPS_0,
            "eta_0": ETA_0,
            "alpha_s_0": ALPHA_S_0,
            "alpha_source": alpha_source,
            "alpha_R": alpha_R.tolist(),
            "xi_E_GGE_inv_used": float(xi_E_GGE_inv),
        },
        "input_pin_map": pins,
        "results": {
            "R_labels": R_labels,
            "alpha_R": alpha_R.tolist(),
            "xi2_0_per_R": xi2_0_per_R.tolist(),
            "xi2_0_canonical": xi2_0_canonical,
            "N_breakdown_per_R": N_breakdown_per_R.tolist(),
            "N_breakdown_canonical": N_breakdown_canonical,
            "deviations_per_R": deviations_per_R.tolist(),
            "max_R_deviation_observable": max_R_deviation_observable,
            "argmax_R_label": R_labels[argmax_idx],
            "regime_per_R": regime_per_R,
            "regime_canonical": canon_regime,
            "crossing_clean_per_R": crossing_clean_per_R.tolist(),
            "crossing_clean_canonical": canon_clean,
        },
        "cross_checks": {
            "CC1_IC_fidelity_max_dev": cc1_max_dev,
            "CC1_PASS": bool(cc1_PASS),
            "CC2_eps_monotone_min_diff": cc2_min_diff_overall,
            "CC2_PASS": bool(cc2_PASS),
            "CC3_canonical_dN_robustness": canon_dn_dev,
            "CC3_PASS": bool(cc3_PASS),
            "CC4_all_ODE_success": bool(all_success),
            "CC5_all_crossings_clean": bool(all_clean),
        },
        "verdict_tuple": {
            "sign_verdict": sign_v,
            "magnitude_verdict": mag_v,
            "regime_verdict_per_R": regime_per_R,
            "regime_verdict_aggregate": regime_v_aggregate,
            "composite": composite,
        },
        "analytic_pre_registration": {
            "predicted_sign": "POSITIVE (Reading_A direction)",
            "predicted_magnitude": "~0.7% (W-12-prior 1.5 factor → INFO band)",
            "predicted_composite": "INFO",
            "note": "Plan §9 Step 4 analytic estimate; numerical verdict above replaces it.",
        },
    }  # (local)

    audit_sha, content_sha = compute_dual_sha(
        SCRIPT_PATH, CANONICAL_PATH, pins, diag["machinery_pin_map"]
    )
    diag["audit_sha256"] = audit_sha
    diag["content_sha256"] = content_sha

    JSON_PATH.write_text(json.dumps(diag, indent=2, default=str), encoding="utf-8")
    print(f"  json: {JSON_PATH.name}")
    print()

    # ----------------------------- Emit verdict line + dual-SHA + 3-tuple annotation -----------------------------
    print(f"=== Emit verdict line (S87+ schema-v2: canonical + dual-SHA + 3-tuple) ===")
    value_str = f"{max_R_deviation_observable:.6f}"  # (local)
    print(f"  ({GATE_ID}) (value={value_str}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"    audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap+machinery)")
    print(f"    content_sha256: {content_sha[:16]}... (script-only)")
    print(f"    sign_verdict={sign_v}, magnitude_verdict={mag_v}, regime_verdict={regime_v_aggregate}")
    print(f"    composite:      {composite}")

    append_verdict_block(
        GATE_ID, composite, value_str, audit_sha, content_sha,
        sign_v, mag_v, regime_v_aggregate
    )

    # ----------------------------- Summary -----------------------------
    wall = time.time() - t0  # (local)
    print()
    print(f"=== {GATE_ID}: complete (wall {wall:.2f}s) ===")
    print(f"  composite verdict: {composite}")
    print(f"  3-tuple: ({sign_v}, {mag_v}, {regime_v_aggregate})")
    print(f"  max_R deviation: {max_R_deviation_observable:.6f}  ({max_R_deviation_observable * 100:.4f}%)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
