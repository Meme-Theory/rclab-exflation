#!/usr/bin/env python3
"""
S91 W1-3 - CF-S91-CF-71-K_CANONICAL-PIN-UNIQUENESS  (T1.2; DRY-RUN DISCRIMINATOR)
==================================================================================

Gate: CF-S91-CF-71-K_CANONICAL-PIN-UNIQUENESS  ([VERIFY-THEOREM])

PLAN-VS-CANONICAL CORRECTION (user directive 2026-05-16; same as W1-1 + W1-2)
-----------------------------------------------------------------------------
Plan sessions/session-plan/session-91-plan-w1.md section W1-3 Field 6 wrote
the substitution chain with the operator:

    L_predict_A = d ln(Tr_{M_2(C)}(P_BdG * D_K^{-2s})) / d ln(K) |_{K=Delta_BCS/M_KK, s=4}
    L_predict_B = same with K = K_canonical(B*) from V4 alignment-config

Same closed-form analysis as W1-1 / W1-2 reveals: d ln(K^{2s}) / d ln K = +2s = +8 for s=4,
independent of K — operator-mismatched against canonical L_emp = -7.046336 anchor.

Per user directive 2026-05-16 ("If the plan used the wrong maths, then
use the right maths"), this script implements the substrate-physics
meaningful K_canonical uniqueness DRY-RUN DISCRIMINATOR via canonical
observable L_emp = d^2 ln P_GGE / d(ln K)^2 of Bogoliubov variance
(per S87 W2-3 / S89 W5-2 / S90 CF-61), with two competing hypotheses
on the substrate's BdG energy gap structural encoding.

K_CANONICAL UNIQUENESS HYPOTHESES (substrate-physical reformulation)
--------------------------------------------------------------------
The §VII.AV Corner-IV K-window log-derivative observable L_emp =
-7.046336 is reproduced by the substrate's intrinsic 8-mode BdG structure.
The substrate's BdG energy gap admits TWO competing structural encodings:

  Hypothesis A (scalar-Δ canonical):
      Delta_per_mode_A = [Delta_BCS, Delta_BCS, Delta_BCS, Delta_BCS, 0,
                          Delta_BCS, Delta_BCS, Delta_BCS]
                       = uniform scalar Δ_BCS for ALL 7 gapped modes;
                         B1 ungapped (structural)
      Substrate-physics: if the substrate's BdG energy gap were uniform
      scalar across the 7 gapped modes (i.e., the multi-branch s52
      structure is REDUCIBLE to a single scalar canonical), then this
      simpler structure should reproduce L_emp.

  Hypothesis B (multi-branch s52 canonical):
      Delta_per_mode_B = [0.7704, 0.7704, 0.7704, 0.7704, 0,
                          0.176,  0.176,  0.176]
                       = canonical s52 8-mode multi-branch structure
                         (B2 deep, B1 ungapped, B3 upper)
      Substrate-physics: the canonical s52 structure IS the substrate's
      intrinsic operational machinery; this reproduces L_emp by construction
      (W1-1 identity-B sanity confirmed at machine epsilon).

4-CLASS UNIQUENESS ADJUDICATION (plan W1-3 Field 9 + Step 3)
------------------------------------------------------------
    Delta_A = (L_predict_A - L_emp_canonical) / |L_emp_canonical|
    Delta_B = (L_predict_B - L_emp_canonical) / |L_emp_canonical|

    Class (a) NON-UNIQUE-degenerate-both-PASS:
        |Delta_A| < REL_TOL  AND  |Delta_B| < REL_TOL
        Both hypotheses recover L_emp at REL_TOL=1e-3
        Substrate's BdG energy gap is informationally EQUIVALENT under
        scalar-Δ vs multi-branch encoding; K_canonical pin is NON-UNIQUE.

    Class (b) UNIQUE-scalar-Δ:
        |Delta_A| < REL_TOL  AND  |Delta_B| >= REL_TOL
        Only scalar-Δ recovers; multi-branch fails.
        Substrate's BdG structure is encoded in the scalar Δ_BCS alone;
        multi-branch s52 fails to reproduce L_emp under canonical observable.
        UNLIKELY (B is by construction canonical s52 = L_emp; would indicate
                  computational defect).
        Routes T1.1 (CF-70) PROXY-REFINEMENT priority.

    Class (c) UNIQUE-multi-branch-B-tensor:
        |Delta_A| >= REL_TOL  AND  |Delta_B| < REL_TOL
        Only multi-branch recovers; scalar-Δ fails.
        The substrate's BdG energy gap structure REQUIRES the full
        s52 8-mode multi-branch encoding; scalar canonical insufficient.
        OPERATIONAL-ALIGNMENT binding sub-class (T2.52 rule extension
        landed S91 W0; advances K-counter K=1 -> K=2 toward MANDATORY).
        Routes T1.1 (CF-70) to secondary verification axis.
        EXPECTED outcome given substrate-IS s52 8-mode structure.

    Class (d) FAIL-both:
        |Delta_A| >= REL_TOL  AND  |Delta_B| >= REL_TOL
        Neither hypothesis recovers; new refinement axis required
        (potentially W5 T1.11 FULL BdG L_max scan).

DRY-RUN 3-TUPLE SCHEMA-V2 EMISSION (volovik s6 §6 CF-71D)
---------------------------------------------------------
Plan W1-3 Field 7 + Field 9 mandate S87+ schema-v2 3-tuple companion row:
  sign_verdict     = PASS iff at least one hypothesis recovers L_emp
                     (i.e., classes a/b/c); FAIL iff class (d)
  magnitude_verdict = PASS iff uniqueness adjudication is decisive (class b/c)
                     INFO iff class (a) degenerate; FAIL iff class (d)
  regime_verdict    = VALID iff P_GGE > 0 across K-window for both hypotheses
                     MARGINAL iff one hypothesis hits P_GGE <= 0 boundary
                     BREAKDOWN iff both hypotheses fail K-window regime

INPUT FILES
-----------
- canonical_constants.py
- s52_bogoliubov_amp.npz (canonical 8-mode B1+B2+B3 structure at L_max=12)
- s91_w1_v4_k_canonical_multi_branch_fossil_test.npz (V4 verdict; W1-1 output)
- script bytes

OUTPUT (plan W1-3 line 581-583)
-------------------------------
- s91_w1_cf71_k_canonical_pin_uniqueness.npz
- s91_w1_cf71_k_canonical_pin_uniqueness.png
- s91_gate_verdicts.txt  (canonical + dual-SHA + 3-tuple + DRY-RUN routing)
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import math
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "computations" / "_shared"))

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import M_KK, tau_fold, Delta_BCS  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ============================ Gate-block constants ============================
GATE_ID = "CF-S91-CF-71-K_CANONICAL-PIN-UNIQUENESS"
SCHEME = "substrate-IS-K_canonical-pin-uniqueness-DRY-RUN-DISCRIMINATOR"
CONVENTION = (
    "VII-AV-OPERATIONAL-ALIGNMENT-substrate-distance-2-pole-s4-"
    "4-class-uniqueness-adjudication-PLAN-OPERATOR-CORRECTED-PER-USER-2026-05-16"
)
L_MAX = 12  # (local) plan W1-3 Field 7

# K-window pins (canonical per S87 W2-3 / S89 W5-2)
K_HORIZON_FRAC = (0.95, 1.05)  # (local) 5% window around horizon crossing
DLNK = 0.001                    # (local) step in ln K
N_K = int(round((math.log(K_HORIZON_FRAC[1]) - math.log(K_HORIZON_FRAC[0])) / DLNK)) + 1  # (local)

# L_emp canonical anchor (substrate-natural)
L_EMP_CANONICAL = -7.046336474406761  # (local) section VII.AV registry line 18092

# Discriminator threshold (plan Field 7 REL_TOL)
REL_TOL = 1e-3  # (local) uniqueness adjudication relative tolerance

# Output paths
OUT_NPZ = ROOT / "computations" / "session-91" / "s91_w1_cf71_k_canonical_pin_uniqueness.npz"
OUT_PNG = ROOT / "computations" / "session-91" / "s91_w1_cf71_k_canonical_pin_uniqueness.png"
VERDICT_FILE = ROOT / "computations" / "session-91" / "s91_gate_verdicts.txt"

# Input file paths
CANONICAL_CONSTANTS = ROOT / "computations" / "_shared" / "canonical_constants.py"
S52_BOG_CACHE = ROOT / "computations" / "session-52" / "s52_bogoliubov_amp.npz"
V4_VERDICT_NPZ = ROOT / "computations" / "session-91" / "s91_w1_v4_k_canonical_multi_branch_fossil_test.npz"
SCRIPT_PATH = Path(__file__).resolve()

INPUT_FILES = {
    "canonical_constants": CANONICAL_CONSTANTS,
    "s52_bogoliubov_amp": S52_BOG_CACHE,
    "V4_verdict_npz": V4_VERDICT_NPZ,
    "script": SCRIPT_PATH,
}


# ============================ SHA helpers ============================
def sha256_of_file(p: Path) -> str:
    h = hashlib.sha256()  # (local)
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


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
    uniqueness_class: str, routing: str,
) -> None:
    """Atomic single-shot append per gate-verdicts.md S87+ canonical form."""
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
    routing_row = (
        f"# uniqueness_class={uniqueness_class} routing={routing} "
        f"# {GATE_ID} DRY-RUN DISCRIMINATOR 4-class adjudication "
        f"(volovik s6 section 6 CF-71D)\n"
    )  # (local)
    with open(VERDICT_FILE, "a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(dual_sha)
        f.write(three_tuple)
        f.write(routing_row)


# ============================ Canonical s52 loader ============================
def load_s52_canonical() -> dict:
    """Load canonical s52 Bogoliubov amplitudes at L_max=12."""
    c = np.load(S52_BOG_CACHE, allow_pickle=True)
    u_static = c["u_k"].astype(np.float64)
    v_static = c["v_k"].astype(np.float64)
    E_static = c["E_qp"].astype(np.float64)
    Delta_per_mode = c["Delta_per_mode"].astype(np.complex128)
    branch_labels = c["branch_labels"]
    branch_indices = {"B1": [], "B2": [], "B3": []}  # (local)
    for i, lbl in enumerate(branch_labels):
        if lbl.startswith("B1"):
            branch_indices["B1"].append(i)
        elif lbl.startswith("B2"):
            branch_indices["B2"].append(i)
        elif lbl.startswith("B3"):
            branch_indices["B3"].append(i)
    for k in branch_indices:
        branch_indices[k] = np.array(branch_indices[k], dtype=np.int64)
    return {
        "u_static": u_static,
        "v_static": v_static,
        "E_static": E_static,
        "Delta_per_mode": Delta_per_mode,
        "branch_labels": branch_labels,
        "branch_indices": branch_indices,
    }


# ============================ Canonical observable ============================
def k_dependent_bogoliubov(xi0: np.ndarray, Delta_pert: np.ndarray,
                           K_ratio: float) -> np.ndarray:
    """K-dependent Bogoliubov occupation n_a^GGE(K) = |v_a(K)|^2 (S87 W2-3 Def 1-2)."""
    xi_K = xi0 * (K_ratio * K_ratio)  # (local) acoustic K^2 dispersion
    E_K = np.sqrt(xi_K * xi_K + np.abs(Delta_pert) ** 2)  # (local)
    eps_floor = 1e-30  # (local)
    E_K_safe = np.where(E_K < eps_floor, eps_floor, E_K)  # (local)
    v_K2 = 0.5 * (1.0 - xi_K / E_K_safe)  # (local)
    v_K2 = np.clip(v_K2, 0.0, 1.0)  # (local)
    return v_K2


def compute_L_emp(xi0: np.ndarray, Delta_pert: np.ndarray,
                  k_ratios: np.ndarray) -> tuple:
    """L_emp = d^2 ln P_GGE / d(ln K)^2 at K=K_horizon (5-point central FD).

    Returns (L_value or None, P_GGE_array, regime_valid_bool).
    """
    n_K = len(k_ratios)  # (local)
    P_GGE = np.zeros(n_K)  # (local)
    for i, kr in enumerate(k_ratios):
        v_K2 = k_dependent_bogoliubov(xi0, Delta_pert, kr)
        P_GGE[i] = float(np.var(v_K2))
    regime_valid = bool(P_GGE.min() > 0)
    if not regime_valid:
        return None, P_GGE, regime_valid
    ln_P = np.log(P_GGE)
    ln_K = np.log(k_ratios)
    h = ln_K[1] - ln_K[0]
    i0 = int(np.argmin(np.abs(ln_K)))
    if i0 < 2 or i0 > n_K - 3:
        d2 = (ln_P[i0 + 1] - 2 * ln_P[i0] + ln_P[i0 - 1]) / (h * h)
    else:
        d2 = (
            -ln_P[i0 - 2] + 16 * ln_P[i0 - 1] - 30 * ln_P[i0]
            + 16 * ln_P[i0 + 1] - ln_P[i0 + 2]
        ) / (12.0 * h * h)
    return float(d2), P_GGE, regime_valid


# ============================ Hypothesis construction ============================
def build_hypothesis_A_uniform_scalar_delta(s52: dict) -> np.ndarray:
    """Hypothesis A: replace canonical s52 multi-branch Delta_per_mode with
    uniform scalar Delta_BCS for ALL 7 gapped modes (B1 stays ungapped).

    Substrate-physics: counterfactual "what if BdG energy gap were uniform
    scalar?" — tests whether the multi-branch s52 structure is reducible
    to a single Delta_BCS canonical pin.
    """
    Delta_pert = np.zeros(8, dtype=np.complex128)  # (local)
    bi = s52["branch_indices"]
    # B1 ungapped: Delta = 0 (structural; pair-symmetry-forced)
    Delta_pert[bi["B1"]] = 0.0
    # B2 + B3: uniform Delta_BCS magnitude (no phase modulation; no per-branch distinction)
    Delta_pert[bi["B2"]] = complex(Delta_BCS, 0.0)
    Delta_pert[bi["B3"]] = complex(Delta_BCS, 0.0)
    return Delta_pert


def build_hypothesis_B_canonical_s52(s52: dict) -> np.ndarray:
    """Hypothesis B: canonical s52 multi-branch Delta_per_mode (unmodified).

    Substrate-physics: the canonical s52 8-mode multi-branch structure IS the
    substrate's intrinsic operational encoding of BdG energy gap. By construction
    reproduces L_emp at machine epsilon (W1-1 identity-B sanity confirmed).
    """
    return s52["Delta_per_mode"].copy()


def reconstruct_xi0(s52: dict) -> np.ndarray:
    """Compute static xi^(0)_a = (u_static^2 - v_static^2) * E_static.

    The static xi0 is structural (unchanged across hypotheses); only the
    Delta_per_mode varies.
    """
    u_s = s52["u_static"]
    v_s = s52["v_static"]
    E_s = s52["E_static"]
    return (u_s * u_s - v_s * v_s) * E_s


# ============================ V4 cross-check ============================
def load_v4_closest_aligned_config(v4_path: Path) -> dict | None:
    """Optional: load V4 closest-aligned config for B-hypothesis cross-check.

    Per plan W1-3 Field 6 Step 2: K_HYP_B inherits from V4 alignment-config
    if T1.3 PASSed (or argmin-closest if FAIL/INFO).

    Returns dict with closest-aligned (theta_1, theta_2, theta_3, b_1, b_2)
    + V4 verdict, or None if V4 npz unavailable.
    """
    if not v4_path.exists():
        return None
    v4 = np.load(v4_path, allow_pickle=True)
    deltas = v4["deltas"]
    configs = v4["configs"]
    idx_best = int(np.argmin(np.abs(deltas)))
    config_best = configs[idx_best]
    return {
        "verdict_composite": str(v4["verdict_composite"]),
        "verdict_sign": str(v4["verdict_sign"]),
        "n_aligned": int(v4["n_aligned"]),
        "idx_best": idx_best,
        "config_best": config_best.tolist(),
        "delta_best": float(deltas[idx_best]),
        "identity_L": float(v4["identity_L"]) if "identity_L" in v4.files else None,
    }


# ============================ 4-class adjudication ============================
def adjudicate_uniqueness(delta_A: float, delta_B: float,
                          regime_A: bool, regime_B: bool) -> dict:
    """Plan W1-3 Field 9 4-class adjudication."""
    pass_A = (abs(delta_A) < REL_TOL) if regime_A else False
    pass_B = (abs(delta_B) < REL_TOL) if regime_B else False

    # Regime adjudication
    if regime_A and regime_B:
        regime_v = "VALID"
    elif regime_A or regime_B:
        regime_v = "MARGINAL"
    else:
        regime_v = "BREAKDOWN"

    # 4-class adjudication
    if pass_A and pass_B:
        uniqueness_class = "a-NON-UNIQUE-degenerate-both-PASS"
        composite = "INFO"
        sign_v = "PASS"
        mag_v = "INFO"
        routing = (
            "K_canonical-degenerate-both-hypotheses-recover-L_emp;"
            "cross-axis-Stage-2-verify-required-for-adjudication"
        )
    elif pass_A and not pass_B:
        uniqueness_class = "b-UNIQUE-scalar-Δ"
        composite = "PASS"
        sign_v = "PASS"
        mag_v = "PASS"
        routing = "ROUTE-T1.1-PROXY-REFINEMENT-priority-scalar-Δ-canonical-binding"
    elif not pass_A and pass_B:
        uniqueness_class = "c-UNIQUE-multi-branch-B-tensor"
        composite = "PASS"
        sign_v = "PASS"
        mag_v = "PASS"
        routing = (
            "OPERATIONAL-ALIGNMENT-binding-T2.52-rule-extension-K-counter-K=1-to-K=2;"
            "ROUTE-T1.1-secondary-verification-axis"
        )
    else:  # not pass_A and not pass_B
        uniqueness_class = "d-BOTH-FAIL-new-refinement-axis-required"
        composite = "FAIL"
        sign_v = "FAIL"
        mag_v = "FAIL"
        routing = (
            "NEW-refinement-axis-required;"
            "W5-T1.11-FULL-BdG-L_max-scan-mandatory"
        )

    return {
        "uniqueness_class": uniqueness_class,
        "composite": composite,
        "sign_verdict": sign_v,
        "magnitude_verdict": mag_v,
        "regime_verdict": regime_v,
        "routing": routing,
        "pass_A": pass_A,
        "pass_B": pass_B,
    }


# ============================ Diagnostic plot ============================
def make_plot(L_A, L_B, delta_A, delta_B, uniqueness_class: str,
              P_GGE_A, P_GGE_B, k_ratios) -> None:
    """Two panels: (1) Delta_A, Delta_B bar chart; (2) P_GGE(K) for both hypotheses."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Panel 1: Delta_A vs Delta_B
    bars = ax1.bar(
        ["Δ_A (scalar-Δ uniform)", "Δ_B (canonical s52)"],
        [delta_A, delta_B],
        color=["coral", "steelblue"],
        edgecolor="black"
    )
    ax1.axhline(+REL_TOL, color="red", linestyle="--", linewidth=1.0,
                label=f"±REL_TOL = ±{REL_TOL:.0e}")
    ax1.axhline(-REL_TOL, color="red", linestyle="--", linewidth=1.0)
    ax1.axhline(0, color="black", linestyle="-", linewidth=0.5, alpha=0.5)
    ax1.set_ylabel("Δ = (L_predict - L_emp) / |L_emp|")
    ax1.set_title(
        f"K_canonical uniqueness 4-class adjudication\n"
        f"L_A = {L_A if L_A is not None else 'N/A':.6f}; L_B = {L_B if L_B is not None else 'N/A':.6f}\n"
        f"class: {uniqueness_class}"
    )
    ax1.legend(loc="best", fontsize=9)
    ax1.grid(True, axis="y", alpha=0.3)
    # Annotate bar values
    for bar, val in zip(bars, [delta_A, delta_B]):
        if val is not None:
            ax1.text(bar.get_x() + bar.get_width() / 2, val,
                     f"{val:+.3e}", ha="center",
                     va="bottom" if val >= 0 else "top", fontsize=8)

    # Panel 2: P_GGE(K) for both hypotheses
    if P_GGE_A is not None:
        ax2.plot(k_ratios, P_GGE_A, color="coral", linewidth=2, label="A: scalar-Δ uniform")
    if P_GGE_B is not None:
        ax2.plot(k_ratios, P_GGE_B, color="steelblue", linewidth=2,
                 linestyle="--", label="B: canonical s52")
    ax2.axvline(1.0, color="black", linestyle=":", linewidth=1.0, alpha=0.5,
                label="K_horizon = 1")
    ax2.set_xlabel("K / K_horizon")
    ax2.set_ylabel("P_GGE(K) = Var_a(|v_a(K)|^2)")
    ax2.set_title("Bogoliubov variance across K-window")
    ax2.set_yscale("log")
    ax2.legend(loc="best", fontsize=9)
    ax2.grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=120)
    plt.close(fig)


# ============================ Main ============================
def main() -> int:
    import time
    t0 = time.time()

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)
    audit_sha, content_sha = compute_dual_sha(pins, SCRIPT_PATH)
    print()
    print(f"  audit_sha256   = {audit_sha[:16]}...  (script+canonical+pinmap)")
    print(f"  content_sha256 = {content_sha[:16]}...  (script only)")
    print()

    # 2. Load s52 canonical
    print("Loading s52 canonical Bogoliubov amplitudes...")
    s52 = load_s52_canonical()
    print(f"  branches: B1 (n={len(s52['branch_indices']['B1'])}), "
          f"B2 (n={len(s52['branch_indices']['B2'])}), "
          f"B3 (n={len(s52['branch_indices']['B3'])})")
    print(f"  Delta_per_mode canonical: {np.abs(s52['Delta_per_mode']).round(6)}")
    print()

    # 3. Load V4 verdict for cross-check
    print("Loading W1-1 V4 verdict for cross-check...")
    v4_info = load_v4_closest_aligned_config(V4_VERDICT_NPZ)
    if v4_info is not None:
        print(f"  V4 verdict_composite: {v4_info['verdict_composite']}")
        print(f"  V4 n_aligned:         {v4_info['n_aligned']}")
        print(f"  V4 identity_L:        {v4_info['identity_L']}")
        print(f"  V4 closest-aligned config (theta_1, theta_2, theta_3, b_1, b_2): "
              f"{tuple(round(x, 6) for x in v4_info['config_best'])}")
        print(f"  V4 closest-aligned delta: {v4_info['delta_best']:+.6e}")
    else:
        print(f"  V4 verdict npz NOT FOUND at {V4_VERDICT_NPZ.relative_to(ROOT)}")
    print()

    # 4. Build K-window grid
    ln_grid = np.linspace(
        math.log(K_HORIZON_FRAC[0]), math.log(K_HORIZON_FRAC[1]), N_K
    )
    k_ratios = np.exp(ln_grid)
    print(f"K-window grid: {N_K} points, K in [{k_ratios.min():.4f}, {k_ratios.max():.4f}]")
    print()

    # 5. Build hypotheses
    print("Building K_canonical uniqueness hypotheses:")
    Delta_A = build_hypothesis_A_uniform_scalar_delta(s52)
    Delta_B = build_hypothesis_B_canonical_s52(s52)
    print(f"  Hypothesis A (scalar-Δ uniform):  Delta_per_mode = {np.abs(Delta_A).round(6)}")
    print(f"  Hypothesis B (canonical s52):     Delta_per_mode = {np.abs(Delta_B).round(6)}")
    print()

    # 6. Compute L for both hypotheses
    xi0 = reconstruct_xi0(s52)
    print(f"Static xi0 (per mode): {xi0.round(6)}")
    print()
    print("Computing L_emp = d^2 ln P_GGE / d(ln K)^2 for both hypotheses...")
    L_A, P_GGE_A, regime_A = compute_L_emp(xi0, Delta_A, k_ratios)
    L_B, P_GGE_B, regime_B = compute_L_emp(xi0, Delta_B, k_ratios)
    print(f"  Hypothesis A: L_A = {L_A!r}  regime_valid = {regime_A}")
    print(f"  Hypothesis B: L_B = {L_B!r}  regime_valid = {regime_B}")
    print()

    # 7. Compute deltas
    if L_A is not None:
        delta_A = (L_A - L_EMP_CANONICAL) / abs(L_EMP_CANONICAL)
    else:
        delta_A = float("nan")
    if L_B is not None:
        delta_B = (L_B - L_EMP_CANONICAL) / abs(L_EMP_CANONICAL)
    else:
        delta_B = float("nan")
    print(f"L_EMP_CANONICAL = {L_EMP_CANONICAL}")
    print(f"  Delta_A = {delta_A:+.6e}  (|Delta_A| = {abs(delta_A):.6e})")
    print(f"  Delta_B = {delta_B:+.6e}  (|Delta_B| = {abs(delta_B):.6e})")
    print(f"  REL_TOL = {REL_TOL:.0e}")
    print()

    # 8. 4-class adjudication
    verdict = adjudicate_uniqueness(delta_A, delta_B, regime_A, regime_B)
    print(f"K_canonical pin uniqueness adjudication:")
    print(f"  uniqueness_class:  {verdict['uniqueness_class']}")
    print(f"  composite:         {verdict['composite']}")
    print(f"  sign_verdict:      {verdict['sign_verdict']}")
    print(f"  magnitude_verdict: {verdict['magnitude_verdict']}")
    print(f"  regime_verdict:    {verdict['regime_verdict']}")
    print(f"  pass_A:            {verdict['pass_A']}")
    print(f"  pass_B:            {verdict['pass_B']}")
    print(f"  routing:           {verdict['routing']}")
    print()

    # 9. Save outputs
    print(f"Saving npz to {OUT_NPZ.relative_to(ROOT)}...")
    np.savez(
        OUT_NPZ,
        L_A=L_A if L_A is not None else float("nan"),
        L_B=L_B if L_B is not None else float("nan"),
        delta_A=delta_A,
        delta_B=delta_B,
        P_GGE_A=P_GGE_A,
        P_GGE_B=P_GGE_B,
        k_ratios=k_ratios,
        Delta_A_pert=Delta_A,
        Delta_B_pert=Delta_B,
        xi0=xi0,
        regime_A=regime_A,
        regime_B=regime_B,
        pass_A=verdict["pass_A"],
        pass_B=verdict["pass_B"],
        uniqueness_class=verdict["uniqueness_class"],
        composite=verdict["composite"],
        L_EMP_CANONICAL=L_EMP_CANONICAL,
        REL_TOL=REL_TOL,
        Delta_BCS=Delta_BCS,
        v4_closest_aligned_config=np.array(v4_info["config_best"]) if v4_info else np.array([]),
        v4_n_aligned=v4_info["n_aligned"] if v4_info else -1,
    )
    print(f"Saving plot to {OUT_PNG.relative_to(ROOT)}...")
    make_plot(L_A, L_B, delta_A, delta_B,
              verdict["uniqueness_class"], P_GGE_A, P_GGE_B, k_ratios)
    print()

    # 10. Emit verdict line
    value_str = (
        f"uniqueness_class={verdict['uniqueness_class']}_"
        f"L_A={L_A if L_A is not None else 'NaN':.6f}_"
        f"L_B={L_B if L_B is not None else 'NaN':.6f}_"
        f"Delta_A={delta_A:+.6e}_Delta_B={delta_B:+.6e}"
    )
    append_verdict(
        composite=verdict["composite"],
        value_str=value_str,
        audit_sha=audit_sha,
        content_sha=content_sha,
        sign_v=verdict["sign_verdict"],
        mag_v=verdict["magnitude_verdict"],
        reg_v=verdict["regime_verdict"],
        uniqueness_class=verdict["uniqueness_class"],
        routing=verdict["routing"],
    )

    # 11. Final summary
    wall = time.time() - t0  # (local)
    print(f"=== {GATE_ID}: {verdict['composite']} (wall {wall:.1f}s) ===")
    print(f"    uniqueness_class: {verdict['uniqueness_class']}")
    print(f"    value: {value_str}")
    print(f"    audit_sha256:   {audit_sha}")
    print(f"    content_sha256: {content_sha}")
    return 0  # All verdicts exit 0 per math-scripts.md section "Exit Codes"


if __name__ == "__main__":
    sys.exit(main())
