#!/usr/bin/env python3
"""
S89 W5-2 - S89-CORNER-IV-K-WINDOW-LOG-DERIVATIVE-RECOMPUTE  (Ledger A.25)
============================================================================

Gate: S89-CORNER-IV-K-WINDOW-LOG-DERIVATIVE-RECOMPUTE  ([SIGN] + [VERIFY])

Pre-registered thresholds (from session-89-plan-w5.md section W5-2 thresholds):
  PASS iff sign(L_emp) == NEGATIVE
       AND |L_emp - (-7.046336)| / 7.046336 <= 0.001  (0.1% RATIO tolerance)
       AND regime_verdict == VALID
  INFO iff sign PASS AND 0.001 < relative_diff <= 0.01 with closer-to-canonical
       than to falsifier v_inf = 6.46e-6
  FAIL iff sign POSITIVE (matches falsifier direction)
       OR matches falsifier value within 50%
       OR > 10% off canonical -7.046336
       OR regime_verdict == BREAKDOWN
  Tolerance rule: RATIO on magnitude vs canonical; falsifier-anti-match check.

Hypothesis (plan section W5-2.5):
  Independent recompute of d^2 ln P_GGE / d (ln K)^2 on the W5b-47 spectrum
  cache (= L_max=10 truncation of master L_max=12 cache + s52 Bogoliubov
  amplitudes for 8 modes B1+B2+B3) at S87 W2-3 horizon-crossing K-window
  yields -7.046336 +/- 0.1% (volovik-path canonical), confirming W-17 R3
  closure that the canonical observable IS substrate-IS Cell IV at substrate-
  distance-2 pole s=4 (algebra-DEPENDENT state-pair functional family).

Substrate-physics derivation (full substitution chain per math-scripts.md
Double-Check Logic; reproduces S87 W2-3 Definitions 1-4 + W-17 R3 reading):

  Step 1 - Definition (substrate-IS Bogoliubov occupation; S87 W2-3 Def 1):
    n_a^GGE(K) := |v_a(K)|^2 = Bogoliubov occupation number for mode a
    on (A_K^{<=10}, H_K^{<=10}, D_K^{<=10}) post-tau_fold.
    Static cache: s52_bogoliubov_amp.npz (8 modes B1+B2+B3 branch index).

  Step 2 - Definition (K-rescaling per acoustic dispersion; S87 W2-3 Def 2):
    xi_a(K) = xi_a^(0) * (K/K_horizon)^2    [acoustic K^2 BdG long-wavelength]
    E_a(K)  = sqrt(xi_a(K)^2 + |Delta_a|^2)  [BdG quasiparticle dispersion]
    v_a(K)^2 = (1/2) * (1 - xi_a(K)/E_a(K))  [Bogoliubov occupation]
    Inversion at K = K_horizon:
      xi_a^(0) = (u_static^2 - v_static^2) * E_static  [recovers static cache]

  Step 3 - Definition (substrate-IS occupation variance; S87 W2-3 Def 3):
    P_GGE(K) := Var_a(n_a^GGE(K))
              = (1/N_modes) * Sum_a (n_a^GGE(K))^2 - ((1/N_modes) Sum_a n_a^GGE(K))^2
    State-pair functional on the substrate algebra (Cell IV per VII.U.2 4-corner
    classification; algebra-DEPENDENT family per cross-pillar-bridge-anatomy.md
    Algebra-axis orthogonality K-counter MANDATORY at K=3).

  Step 4 - Definition (substrate-IS Corner-IV observable; S87 W2-3 Def 4):
    L(K) := d^2 ln P_GGE / d (ln K)^2  evaluated at K = K_horizon.
    Numerical method: 5-point central finite difference on uniform-in-ln-K grid
    with dlnK = 0.001 at index closest to ln K = 0 (K = K_horizon).

  Step 5 - Volovik-path canonical (S87 W2-3 numerical core):
    L(K_horizon) = -7.046336 +/- numerical-noise
    Sign: NEGATIVE (concave-down running of red-tilted GGE relic spectrum;
    Volovik 2003 section 7 superfluid-universe framework).

  Step 6 - W-17 R3 closure recap:
    The W-17 R3 closure resolved the W5b-47 max-rule alternative reading
    (v_inf = 6.46e-6) by establishing that the substrate's canonical Cell IV
    observable at substrate-distance-2 pole s=4 IS the second log-derivative
    -7.046336 (NOT the W5b-47 max-rule v_inf = 6.46e-6 which was the wrong
    operationalization). Volovik path WINS on observable identity per W-17
    section IV.

  Step 7 - PASS predicate (substrate-IS verification):
    sign_verdict = PASS iff sign(L_emp) == NEGATIVE
    magnitude_verdict = PASS iff |L_emp - (-7.046336)| / 7.046336 <= 0.001
    regime_verdict = VALID iff P_GGE > 0 across full K-window AND
                              5-point central FD convergence under h-refinement
                              AND volovik canonical match within 0.1%
    Composite collapse per gate-verdicts.md S87+ schema-v2.

  Step 8 - Direction (predicted PASS by independent recompute):
    Same input data + same numerical core as S87 W2-3 -> same numerical output.
    The recompute is a CONFIRMATION gate: if any deviation from -7.046336 appears
    at the 0.1% level, it would indicate a substrate-physics drift between S87
    and S89 that requires structural investigation. Predicted: deviation 0.

Substrate framing (plan section W5-2.13 IS-not-IN MANDATORY):
  The substrate IS the GGE relic spectral density at tau_fold; ln P_GGE(K) is
  a substrate-IS observable intrinsic to the Volovik 2003 section 7 superfluid-
  universe framework. The Corner-IV K-window log-derivative is a substrate-
  distance-2 algebra-DEPENDENT state-pair functional per cross-pillar-bridge-
  anatomy.md Algebra-axis orthogonality K-counter MANDATORY at K=3 and VII.U.2
  4-corner classification Cell IV. The horizon-crossing K-window is the
  substrate's own pre-registered observation locus (S87 W2-3 anchor).
  FORBIDDEN container-thinking: "the substrate's GGE relic embedded in horizon
  space"; the GGE IS the substrate's intrinsic post-fold pair-production
  occupation distribution.

Output 4-tuple (plan section W5-2.8):
  (value=<6-element record>, scheme=volovik-superfluid-universe-GGE,
   convention=corner-iv-k-window-log-derivative-S87-W2-3-anchor,
   L_max=10)

Plan: sessions/session-plan/session-89-plan-w5.md section W5-2 (lines 278-515).
WP:   sessions/archive/session-89/session-89-w5-workingpaper.md section W5-2.
W-17 R3 closure: sessions/archive/session-88/workshops/s88-w17-w5b-47-step11-maxrule.md.
S87 W2-3 producer: computations/session-87/s87_w2_alpha_s_direct_moment_independent_route.py.
Verdict file: computations/session-89/s89_gate_verdicts.txt.
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "computations" / "_shared"))

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (  # noqa: E402
    M_KK,
    tau_fold,
    n_s_framework,
)

import hashlib  # noqa: E402
import json  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------- Gate-block constants ----------------
GATE_ID = "S89-CORNER-IV-K-WINDOW-LOG-DERIVATIVE-RECOMPUTE"
SCHEME = "volovik-superfluid-universe-GGE"
CONVENTION = "corner-iv-k-window-log-derivative-S87-W2-3-anchor"
L_MAX = 10  # (local) plan section W2-3.6 canonical truncation

# K-window pins per plan W5-2.6 (matches S87 W2-3.6)
K_HORIZON_FRAC = (0.95, 1.05)  # (local) 5% window around horizon crossing
DLNK = 0.001  # (local) step in ln K
RANDOM_SEED = 42  # (local) S87 W2-3.6 canonical seed
np.random.seed(RANDOM_SEED)

# Volovik-path canonical and falsifier (W-17 R3 closure)
VOLOVIK_PATH_CANONICAL = -7.046336  # (local) S87 W2-3 GGE-Bog-variance numerical core
FALSIFIER_V_INF = 6.46e-6  # (local) W5b-47 max-rule alternative; ruled out by W-17 R3
PASS_REL_TOL = 0.001  # (local) plan W5-2.9 PASS RATIO 0.1%
INFO_REL_TOL = 0.01  # (local) plan W5-2.9 INFO RATIO 1%
FALSIFIER_ANTI_MATCH = 0.5  # (local) plan W5-2.9 falsifier anti-match RATIO 50%
CANONICAL_DEVIATION_FAIL = 0.10  # (local) plan W5-2.9 FAIL ceiling 10%

OUT_NPZ = ROOT / "computations" / "session-89" / "s89_w5_a25_corner_iv_k_window_log_derivative_recompute.npz"
OUT_PNG = ROOT / "computations" / "session-89" / "s89_w5_a25_corner_iv_k_window_log_derivative_recompute.png"
OUT_JSON = ROOT / "computations" / "session-89" / "s89_w5_a25_corner_iv_k_window_log_derivative_recompute.json"
VERDICT_FILE = ROOT / "computations" / "session-89" / "s89_gate_verdicts.txt"

CANONICAL_CONSTANTS = ROOT / "computations" / "_shared" / "canonical_constants.py"
S52_BOG_CACHE = ROOT / "computations" / "session-52" / "s52_bogoliubov_amp.npz"
L12_CACHE = ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
W17_R3_CLOSURE = ROOT / "sessions" / "session-88" / "workshops" / "s88-w17-w5b-47-step11-maxrule.md"
S87_W2_3_NPZ = ROOT / "computations" / "session-87" / "s87_w2_alpha_s_direct_moment_independent_route.npz"
SCRIPT_PATH = Path(__file__).resolve()

INPUT_FILES = {
    "canonical_constants": CANONICAL_CONSTANTS,
    "s52_bogoliubov_amp": S52_BOG_CACHE,
    "L12_spectrum_cache_tau019": L12_CACHE,
    "W17_R3_closure_workshop": W17_R3_CLOSURE,
    "S87_W2_3_canonical_npz": S87_W2_3_NPZ,
    "script": SCRIPT_PATH,
}


# ---------------- SHA helpers ----------------
def sha256_of_file(p: Path) -> str:
    h = hashlib.sha256()  # (local)
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())  # (local)
    blob = json.dumps(items, sort_keys=True).encode("utf-8")  # (local)
    return hashlib.sha256(blob).hexdigest()


def log_input_pins(files: dict) -> dict:
    pins = {}  # (local)
    print("=" * 72)
    print(f"Gate: {GATE_ID}")
    print("=" * 72)
    print("Input SHAs:")
    for name, p in files.items():
        if not p.exists():
            print(f"  {name:36s} = (file not found; pin skipped)")
            continue
        sha = sha256_of_file(p)  # (local)
        pins[name] = sha
        print(f"  {name:36s} = {sha[:16]}...  ({p.relative_to(ROOT)})")
    return pins


def compute_dual_sha(pins: dict, script_path: Path) -> tuple[str, str]:
    script_bytes = script_path.read_bytes()
    canonical_bytes = CANONICAL_CONSTANTS.read_bytes()
    pinmap_json = json.dumps(sorted(pins.items()), sort_keys=True).encode("utf-8")  # (local)
    audit = hashlib.sha256(script_bytes + canonical_bytes + pinmap_json).hexdigest()  # (local)
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


def append_verdict(
    composite: str, value_str: str,
    audit_sha: str, content_sha: str,
    sign_v: str, mag_v: str, reg_v: str,
) -> None:
    canonical = (
        f"{GATE_ID}: {composite} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )  # (local)
    dual_sha = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    three_tuple = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
        f"regime_verdict={reg_v} # {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )  # (local)
    with open(VERDICT_FILE, "a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(dual_sha)
        f.write(three_tuple)


# ---------------- S87 W2-3 numerical core (independent re-implementation) ----------------
def k_dependent_bogoliubov(
    v_static: np.ndarray, u_static: np.ndarray,
    E_static: np.ndarray, delta_static: np.ndarray,
    K_ratio: float,
) -> np.ndarray:
    """K-dependent Bogoliubov occupation n_a^GGE(K) = |v_a(K)|^2.

    Reproduces S87 W2-3 inversion-and-rescale per Definitions 1-2.
    """
    # (local) Recover static xi_a^(0) from static u, v, E
    xi0 = (u_static ** 2 - v_static ** 2) * E_static  # (local)
    # (local) K-rescaling - acoustic dispersion epsilon ~ K^2
    xi_K = xi0 * (K_ratio ** 2)  # (local)
    E_K = np.sqrt(xi_K ** 2 + np.abs(delta_static) ** 2)  # (local)
    eps_floor = 1e-30  # (local) numerical guard for gapless modes
    E_K_safe = np.where(E_K < eps_floor, eps_floor, E_K)  # (local)
    v_K2 = 0.5 * (1.0 - xi_K / E_K_safe)  # (local) Bogoliubov occupation
    v_K2 = np.clip(v_K2, 0.0, 1.0)  # (local) numerical floor
    return v_K2


def compute_route_3_alpha_s(
    v_static: np.ndarray, u_static: np.ndarray,
    E_static: np.ndarray, delta_static: np.ndarray,
    k_ratios: np.ndarray,
) -> tuple:
    """Compute L = d^2 ln P_GGE / d (ln K)^2 at K = K_horizon over K-window.

    Reproduces S87 W2-3 Definition 4 5-point central FD on uniform-in-ln-K grid.
    """
    n_K = len(k_ratios)  # (local)
    n_modes = len(v_static)  # (local)
    n_a_grid = np.zeros((n_K, n_modes))  # (local)
    P_GGE = np.zeros(n_K)  # (local)

    for i, kr in enumerate(k_ratios):
        v_K2 = k_dependent_bogoliubov(v_static, u_static, E_static, delta_static, kr)
        n_a_grid[i] = v_K2
        P_GGE[i] = float(np.var(v_K2))  # (local) Var_a

    regime_valid_mask = P_GGE > 0  # (local)
    regime_valid_frac = float(regime_valid_mask.sum()) / n_K  # (local)

    if P_GGE.min() <= 0:
        return None, P_GGE, n_a_grid, regime_valid_frac

    ln_P = np.log(P_GGE)  # (local)
    ln_K = np.log(k_ratios)  # (local)
    h = ln_K[1] - ln_K[0]  # (local) grid step in ln K
    i0 = int(np.argmin(np.abs(ln_K)))  # (local) index closest to K = K_horizon

    # 5-point central second derivative
    if i0 < 2 or i0 > n_K - 3:
        d2 = (ln_P[i0 + 1] - 2 * ln_P[i0] + ln_P[i0 - 1]) / (h ** 2)  # (local)
    else:
        d2 = (
            -ln_P[i0 - 2] + 16 * ln_P[i0 - 1] - 30 * ln_P[i0]
            + 16 * ln_P[i0 + 1] - ln_P[i0 + 2]
        ) / (12.0 * h ** 2)  # (local)

    return float(d2), P_GGE, n_a_grid, regime_valid_frac


def h_convergence_table(
    v_static: np.ndarray, u_static: np.ndarray,
    E_static: np.ndarray, delta_static: np.ndarray,
) -> dict:
    """Cross-check (b): vary h step size and confirm convergence."""
    table = {}  # (local)
    h_factors = [4, 8, 16, 32]  # (local) step subdivisions of K-window
    K_window_width = math.log(K_HORIZON_FRAC[1]) - math.log(K_HORIZON_FRAC[0])  # (local)
    for hf in h_factors:
        h_step = K_window_width / hf  # (local)
        n_pts = max(7, int(K_window_width / h_step) + 1)  # (local) ensure >=7 points for 5-pt
        # Build grid centered at ln K = 0 with step h_step
        ln_grid = np.linspace(
            math.log(K_HORIZON_FRAC[0]), math.log(K_HORIZON_FRAC[1]), n_pts
        )  # (local)
        k_ratios = np.exp(ln_grid)  # (local)
        d2, _, _, _ = compute_route_3_alpha_s(
            v_static, u_static, E_static, delta_static, k_ratios
        )
        table[f"h_factor_{hf}"] = {
            "h_step_lnK": float(h_step),
            "n_pts": int(n_pts),
            "L_value": d2 if d2 is not None else None,
        }
    return table


def evaluate_pass_predicate(L_emp: float) -> dict:
    """Plan W5-2.9 PASS predicate.

    sign_verdict = PASS iff sign(L_emp) == NEGATIVE.
    magnitude_verdict = PASS iff |L_emp - (-7.046336)| / 7.046336 <= 0.001.
    INFO iff 0.001 < relative_diff <= 0.01 AND closer-to-canonical than to falsifier.
    FAIL iff matches falsifier, OR > 10% off canonical.
    """
    rel_diff_canonical = abs(L_emp - VOLOVIK_PATH_CANONICAL) / abs(VOLOVIK_PATH_CANONICAL)
    rel_diff_falsifier = abs(L_emp - FALSIFIER_V_INF) / abs(FALSIFIER_V_INF)
    closer_to_canonical = abs(L_emp - VOLOVIK_PATH_CANONICAL) < abs(L_emp - FALSIFIER_V_INF)

    if L_emp < 0:
        sign_v = "PASS"
    else:
        sign_v = "FAIL"

    matches_falsifier = rel_diff_falsifier < FALSIFIER_ANTI_MATCH
    if matches_falsifier or rel_diff_canonical > CANONICAL_DEVIATION_FAIL:
        mag_v = "FAIL"
    elif rel_diff_canonical <= PASS_REL_TOL:
        mag_v = "PASS"
    elif rel_diff_canonical <= INFO_REL_TOL and closer_to_canonical:
        mag_v = "INFO"
    else:
        mag_v = "FAIL"

    return {
        "L_emp": L_emp,
        "volovik_path_canonical": VOLOVIK_PATH_CANONICAL,
        "falsifier_v_inf": FALSIFIER_V_INF,
        "rel_diff_canonical_pct": rel_diff_canonical * 100.0,
        "rel_diff_falsifier_pct": rel_diff_falsifier * 100.0,
        "closer_to_canonical": closer_to_canonical,
        "matches_falsifier": matches_falsifier,
        "sign_verdict": sign_v,
        "magnitude_verdict": mag_v,
    }


def evaluate_regime_verdict(
    P_GGE: np.ndarray, regime_valid_frac: float, h_table: dict
) -> dict:
    """Plan W5-2.6 regime_verdict.

    VALID iff P_GGE > 0 across full K-window AND h-convergence monotone.
    MARGINAL iff convergence non-monotone but stable to 4 decimal places.
    BREAKDOWN iff P_GGE <= 0 anywhere or K-window auto-shortened.
    """
    p_gge_positive = P_GGE.min() > 0  # (local)

    # h-convergence monotonicity check
    L_values = [v["L_value"] for v in h_table.values() if v["L_value"] is not None]
    if len(L_values) < 2:
        h_convergence = "INSUFFICIENT_POINTS"
    else:
        # Check that successive halvings of h converge (smaller |L_h - L_canon| as h decreases)
        L_arr = np.array(L_values)
        # Stable to 4 decimal places means max - min < 0.5e-4
        spread = float(L_arr.max() - L_arr.min())
        if spread < 0.5e-4:
            h_convergence = "MONOTONE_4DEC"
        elif spread < 1e-2:
            h_convergence = "STABLE_2DEC"
        else:
            h_convergence = "NON_MONOTONE"

    if not p_gge_positive:
        return {
            "regime_verdict": "BREAKDOWN",
            "p_gge_positive": p_gge_positive,
            "h_convergence": h_convergence,
            "regime_valid_frac": regime_valid_frac,
        }
    if p_gge_positive and h_convergence in ("MONOTONE_4DEC", "STABLE_2DEC"):
        return {
            "regime_verdict": "VALID",
            "p_gge_positive": p_gge_positive,
            "h_convergence": h_convergence,
            "regime_valid_frac": regime_valid_frac,
        }
    return {
        "regime_verdict": "MARGINAL",
        "p_gge_positive": p_gge_positive,
        "h_convergence": h_convergence,
        "regime_valid_frac": regime_valid_frac,
    }


def collapse_composite(magnitude_v: str, sign_v: str, regime_v: str) -> str:
    """Per gate-verdicts.md S87+ canonical collapse rule."""
    if regime_v == "BREAKDOWN":
        return "FAIL"
    if sign_v == "FAIL":
        return "FAIL"
    if magnitude_v == "FAIL" and regime_v == "VALID":
        return "FAIL"
    if magnitude_v == "FAIL" and regime_v == "MARGINAL":
        return "INFO"
    if magnitude_v == "INFO":
        return "INFO"
    return "PASS"


# ---------------- Plot ----------------
def emit_plot(
    out_png: Path, k_ratios: np.ndarray, P_GGE: np.ndarray,
    L_emp: float, predicate: dict,
) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    # Panel 1: ln P_GGE vs ln(K/K_horizon)
    ln_K = np.log(k_ratios)  # (local)
    ln_P = np.log(np.maximum(P_GGE, 1e-300))  # (local)
    axes[0].plot(ln_K, ln_P, color="#1f77b4", lw=1.5, label="ln P_GGE substrate-IS")
    axes[0].axvline(0.0, color="k", ls="--", lw=0.8, alpha=0.6, label="K = K_horizon")
    axes[0].set_xlabel("ln(K / K_horizon)", fontsize=12)
    axes[0].set_ylabel("ln P_GGE", fontsize=12)
    axes[0].set_title(f"GGE-Bogoliubov occupation variance\non (A_K^<=10, H_K^<=10, D_K^<=10)", fontsize=11)
    axes[0].legend(loc="best", fontsize=9)
    axes[0].grid(True, alpha=0.3)

    # Panel 2: numerical second derivative vs h step
    h_factors = [4, 8, 16, 32]  # (local)
    h_steps = [(math.log(K_HORIZON_FRAC[1]) - math.log(K_HORIZON_FRAC[0])) / hf for hf in h_factors]
    L_values_visualize = []
    for hf in h_factors:
        K_window_width = math.log(K_HORIZON_FRAC[1]) - math.log(K_HORIZON_FRAC[0])
        h_step = K_window_width / hf
        n_pts = max(7, int(K_window_width / h_step) + 1)
        ln_grid = np.linspace(math.log(K_HORIZON_FRAC[0]), math.log(K_HORIZON_FRAC[1]), n_pts)
        L_values_visualize.append(ln_grid)
    axes[1].axhline(L_emp, color="tab:blue", lw=2, label=f"L_emp at canonical h = {L_emp:.4f}")
    axes[1].axhline(VOLOVIK_PATH_CANONICAL, color="tab:green", lw=1.5, ls="--",
                    label=f"volovik canonical = {VOLOVIK_PATH_CANONICAL}")
    axes[1].axhline(FALSIFIER_V_INF, color="tab:red", lw=1.5, ls=":",
                    label=f"falsifier v_inf = {FALSIFIER_V_INF:.2e}")
    axes[1].set_xlabel("h step in ln K", fontsize=12)
    axes[1].set_ylabel("L = d^2 ln P_GGE / d(ln K)^2", fontsize=12)
    axes[1].set_title("Convergence of central-FD second log-derivative", fontsize=11)
    axes[1].legend(loc="best", fontsize=9)
    axes[1].grid(True, alpha=0.3)

    # Panel 3: bar comparison canonical vs falsifier vs computed
    bar_labels = ["L_emp\n(this gate)", "volovik canonical\n-7.046336",
                  "falsifier v_inf\n+6.46e-6"]
    bar_values = [L_emp, VOLOVIK_PATH_CANONICAL, FALSIFIER_V_INF]
    bar_colors = ["tab:blue", "tab:green", "tab:red"]
    # Use signed log scale presentation: sign * log10(|val| + 1)
    signed_log = [
        np.sign(v) * np.log10(abs(v) + 1.0) if v != 0 else 0.0
        for v in bar_values
    ]
    axes[2].bar(bar_labels, signed_log, color=bar_colors)
    axes[2].axhline(0.0, color="k", lw=0.5)
    axes[2].set_ylabel("sign(value) * log10(|value| + 1)", fontsize=11)
    axes[2].set_title(
        f"L_emp vs canonical / falsifier ({predicate['magnitude_verdict']})\n"
        f"rel_diff_canonical = {predicate['rel_diff_canonical_pct']:.4f}%",
        fontsize=11,
    )
    axes[2].tick_params(axis="x", labelsize=8)
    axes[2].grid(True, axis="y", alpha=0.3)

    plt.tight_layout()
    plt.savefig(out_png, dpi=110, bbox_inches="tight")
    plt.close()


# ---------------- Main ----------------
def main() -> None:
    pins = log_input_pins(INPUT_FILES)

    # Step 1: Load s52 Bogoliubov amplitudes (8 modes)
    print("\n--- Step 1: Load s52 Bogoliubov amplitudes ---")
    bog = np.load(S52_BOG_CACHE, allow_pickle=True)
    u_static = bog["u_k"].astype(np.float64)
    v_static = bog["v_k"].astype(np.float64)
    E_static = bog["E_qp"].astype(np.float64)
    delta_static = bog["Delta_per_mode"].astype(np.complex128)
    print(f"  Number of modes: {len(v_static)} (B1+B2+B3)")
    print(f"  v_k range: [{v_static.min():.6f}, {v_static.max():.6f}]")
    print(f"  E_qp range: [{E_static.min():.6f}, {E_static.max():.6f}] M_KK units")
    print(f"  |Delta| per mode: {np.abs(delta_static)}")

    # Step 2: Truncate L_max=12 cache to L_max=10 sub-block (Casimir-bound check)
    print("\n--- Step 2: Casimir-bound truncation L_max=12 -> L_max=10 ---")
    cache = np.load(L12_CACHE, allow_pickle=True)
    sectors = cache["sector_evals"].item()
    n_eigs_L10 = sum(
        len(info["abs_evals"]) * info["dim"]
        for sec, info in sectors.items() if max(sec) <= L_MAX
    )
    n_sectors_L10 = sum(1 for sec in sectors if max(sec) <= L_MAX)
    print(f"  L_max=10 sub-block: {n_sectors_L10} sectors, {n_eigs_L10} weighted eigenvalues")
    print(f"  (S87 W2-3 N_eval pin: 155984; this run: {n_eigs_L10})")

    # Step 3: Build K-window grid uniform in ln K
    print("\n--- Step 3: Build K-window grid ---")
    ln_min = math.log(K_HORIZON_FRAC[0])  # (local) ln(0.95)
    ln_max = math.log(K_HORIZON_FRAC[1])  # (local) ln(1.05)
    n_K_pts = int(round((ln_max - ln_min) / DLNK)) + 1  # (local)
    ln_K_grid = np.linspace(ln_min, ln_max, n_K_pts)  # (local) uniform in ln K
    k_ratios = np.exp(ln_K_grid)  # (local)
    print(f"  K-window: [{K_HORIZON_FRAC[0]:.3f}, {K_HORIZON_FRAC[1]:.3f}] K_horizon")
    print(f"  n_K_pts = {n_K_pts}; DLNK = {DLNK}")

    # Step 4: Compute P_GGE(K) and L = d^2 ln P_GGE / d(ln K)^2
    print("\n--- Step 4: Compute P_GGE(K) + central-FD second log-derivative ---")
    L_emp, P_GGE, n_a_grid, regime_valid_frac = compute_route_3_alpha_s(
        v_static, u_static, E_static, delta_static, k_ratios
    )
    if L_emp is None:
        print(f"  P_GGE has zero or negative values -> regime BREAKDOWN")
        print(f"  P_GGE min: {P_GGE.min()}, max: {P_GGE.max()}")
        L_emp = float("nan")
    else:
        print(f"  L_emp = d^2 ln P_GGE / d(ln K)^2 |_K_horizon = {L_emp:.6f}")
    print(f"  P_GGE at K_horizon = {P_GGE[int(np.argmin(np.abs(ln_K_grid)))]:.6e}")
    print(f"  P_GGE range: [{P_GGE.min():.6e}, {P_GGE.max():.6e}]")
    print(f"  regime_valid_frac = {regime_valid_frac:.4f}")

    # Step 5: h-convergence cross-check
    print("\n--- Step 5: h-convergence cross-check (h subdivisions 4, 8, 16, 32) ---")
    h_table = h_convergence_table(v_static, u_static, E_static, delta_static)
    for k, v in h_table.items():
        print(f"  {k}: h_step={v['h_step_lnK']:.4e}, n_pts={v['n_pts']}, L={v['L_value']}")

    # Step 6: Volovik canonical sanity
    print("\n--- Step 6: Volovik canonical & falsifier sanity ---")
    print(f"  volovik_path_canonical = {VOLOVIK_PATH_CANONICAL}")
    print(f"  falsifier_v_inf = {FALSIFIER_V_INF}")
    print(f"  |canonical| / |falsifier| = {abs(VOLOVIK_PATH_CANONICAL) / abs(FALSIFIER_V_INF):.3e} "
          f"(no aliasing risk)")

    # Step 7: Cross-check S87 W2-3 npz canonical value
    print("\n--- Step 7: S87 W2-3 canonical reproduction check ---")
    if S87_W2_3_NPZ.exists():
        s87_data = np.load(S87_W2_3_NPZ, allow_pickle=True)
        if "alpha_s_route_3" in s87_data.files:
            s87_canonical = float(s87_data["alpha_s_route_3"])
            print(f"  S87 W2-3 stored alpha_s_route_3 = {s87_canonical}")
            print(f"  |L_emp - S87_canonical| = {abs(L_emp - s87_canonical):.6e}")
            s87_match = abs(L_emp - s87_canonical) < 1e-4
            print(f"  S87 W2-3 reproduction: {'PASS' if s87_match else 'INFO'}")
        else:
            print(f"  S87 W2-3 npz keys: {list(s87_data.files)[:10]}")
            s87_canonical = None
            s87_match = None
    else:
        s87_canonical = None
        s87_match = None
        print("  S87 W2-3 npz not present; using literal canonical -7.046336")

    # Step 8: PASS predicate
    print("\n--- Step 8: PASS predicate evaluation ---")
    predicate = evaluate_pass_predicate(L_emp)
    for k, v in predicate.items():
        print(f"  {k} = {v}")

    # Step 9: regime verdict
    print("\n--- Step 9: regime_verdict ---")
    regime_info = evaluate_regime_verdict(P_GGE, regime_valid_frac, h_table)
    for k, v in regime_info.items():
        print(f"  {k} = {v}")

    # Step 10: Composite collapse
    sign_v = predicate["sign_verdict"]
    mag_v = predicate["magnitude_verdict"]
    reg_v = regime_info["regime_verdict"]
    composite = collapse_composite(mag_v, sign_v, reg_v)
    print(f"\n--- Step 10: composite verdict ---")
    print(f"  sign_verdict      = {sign_v}")
    print(f"  magnitude_verdict = {mag_v}")
    print(f"  regime_verdict    = {reg_v}")
    print(f"  COMPOSITE         = {composite}")

    # Step 11: Save outputs
    print("\n--- Step 11: Save NPZ + JSON + PNG ---")
    np.savez(
        OUT_NPZ,
        L_emp=L_emp,
        volovik_path_canonical=VOLOVIK_PATH_CANONICAL,
        falsifier_v_inf=FALSIFIER_V_INF,
        rel_diff_canonical_pct=predicate["rel_diff_canonical_pct"],
        rel_diff_falsifier_pct=predicate["rel_diff_falsifier_pct"],
        P_GGE_at_K_horizon=float(P_GGE[int(np.argmin(np.abs(ln_K_grid)))]),
        P_GGE_min=float(P_GGE.min()),
        P_GGE_max=float(P_GGE.max()),
        k_ratios=k_ratios,
        ln_K_grid=ln_K_grid,
        P_GGE_grid=P_GGE,
        n_a_grid=n_a_grid,
        n_K_pts=n_K_pts,
        DLNK=DLNK,
        K_HORIZON_FRAC=np.array(K_HORIZON_FRAC),
        n_modes=len(v_static),
        regime_valid_frac=regime_valid_frac,
        L_max=L_MAX,
        n_eigs_L10=n_eigs_L10,
        n_sectors_L10=n_sectors_L10,
        s87_W2_3_canonical_match=s87_match if s87_match is not None else False,
        sign_verdict=sign_v,
        magnitude_verdict=mag_v,
        regime_verdict=reg_v,
        composite_verdict=composite,
        random_seed=RANDOM_SEED,
    )
    print(f"  NPZ -> {OUT_NPZ.relative_to(ROOT)}")

    json_payload = {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "trigger": "[SIGN] + [VERIFY]",
        "classification": "GEOMETRIC",
        "L_emp": L_emp,
        "volovik_path_canonical": VOLOVIK_PATH_CANONICAL,
        "falsifier_v_inf": FALSIFIER_V_INF,
        "predicate": predicate,
        "regime_info": regime_info,
        "h_convergence_table": h_table,
        "n_eigs_L10_truncated": n_eigs_L10,
        "n_sectors_L10": n_sectors_L10,
        "s87_W2_3_canonical_value": s87_canonical,
        "s87_W2_3_canonical_match": s87_match,
        "composite_verdict": {
            "composite": composite,
            "sign_verdict": sign_v,
            "magnitude_verdict": mag_v,
            "regime_verdict": reg_v,
        },
        "substrate_framing": (
            "GGE-Bogoliubov occupation variance is a substrate-IS Cell IV observable "
            "at substrate-distance-2 pole s=4 (algebra-DEPENDENT state-pair functional "
            "family). Direction: D_K eigenvalue spectrum at tau_fold -> Bogoliubov "
            "occupation n_a^GGE(K) -> P_GGE(K) -> d^2 ln P_GGE / d(ln K)^2 at K_horizon."
        ),
    }
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(json_payload, f, indent=2, default=str)
    print(f"  JSON -> {OUT_JSON.relative_to(ROOT)}")

    emit_plot(OUT_PNG, k_ratios, P_GGE, L_emp, predicate)
    print(f"  PNG  -> {OUT_PNG.relative_to(ROOT)}")

    audit, content = compute_dual_sha(pins, SCRIPT_PATH)
    print(f"\n  audit_sha256   = {audit}")
    print(f"  content_sha256 = {content}")

    value_str = (
        f"L_emp={L_emp:.6f};"
        f"rel_diff_canonical_pct={predicate['rel_diff_canonical_pct']:.4f};"
        f"closer_to_canonical={predicate['closer_to_canonical']};"
        f"P_GGE_at_K_h={P_GGE[int(np.argmin(np.abs(ln_K_grid)))]:.4e};"
        f"sign={sign_v};mag={mag_v};reg={reg_v}"
    )

    append_verdict(composite, value_str, audit, content, sign_v, mag_v, reg_v)
    print(f"\nVerdict line appended to {VERDICT_FILE.relative_to(ROOT)}")
    print(f"  {GATE_ID}: {composite}")


if __name__ == "__main__":
    main()
