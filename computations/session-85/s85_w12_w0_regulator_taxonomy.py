#!/usr/bin/env python3
"""
S85 W12-ELIM-8 — W0-regulator-invariance taxonomy of 16 registry observables
============================================================================

Gate: S85-W12-ELIM-8 ([VERIFY])

Pre-registered threshold (plan §W12-4 line 167-170):
  PASS  iff  all 16 observables assigned to exactly one of {a, b, c, d} with
            no ambiguity (coverage = 16/16, partition exhaustive-and-disjoint).
  FAIL  iff  ≥ 1 observable is structurally unclassifiable under the 4-class
            partition (bimodal-no-majority spread — needs 5th class "POLYMODAL").
  INFO  iff  1 ≤ observables_in_class_(b) ≤ 3 (conditional-invariants surfacing;
            schedule mid-session regulator-remediation pass).

Output 4-tuple:
  (value=<n_a, n_b, n_c, n_d>, scheme=regulator-invariance-taxonomy,
   convention=5-regulator-atlas-W0, L_max=10)

Classification: GEOMETRIC (spectral-action regulator-invariance structural
probe — companion to the ELIM-4 reduction catalog).

METHODOLOGY
-----------
For each of the 16 permanent-results-registry spectral-action observables,
evaluate under each of the 5 pinned regulators:
    R_atlas = [heat-kernel, zeta, Mellin, hard-cutoff, Pauli-Villars]

Canonical scalars (pinned PDG / framework constants that are NOT direct
spectral-moment evaluations) return the same value under any regulator —
they are regulator-invariant by construction, class (a). The 3 genuine
spectral moments {a_0, a_2, a_4} are evaluated via the Casimir-schematic
spectrum under each regulator (see `_spectral_action_regulators.py`).

Per-observable spread:
    spread(O_k) = (max_r v_r - min_r v_r) / mean_r v_r

Class assignment (plan §W12-4 line 190-193):
    (a) INVARIANT            iff  spread < 0.001
    (b) CONDITIONALLY-INVARIANT
                             iff  spread ∈ [0.001, 0.01) AND 4/5 regulators
                                  cluster within 0.001 of each other
    (c) SCHEME-DEPENDENT     iff  spread ∈ [0.001, 0.1) AND cluster predicate
                                  FAILS
    (d) STRUCTURALLY-DIVERGENT
                             iff  spread ≥ 0.1

The cluster predicate disambiguates the overlap [0.001, 0.01) region.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 - Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 - Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import os
import sys
import time
from pathlib import Path
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
from computation_root import resolve_script, resolve_output, resolve_glob, resolve_dynamic, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===


os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Helper — 5-regulator atlas
from _spectral_action_regulators import (
    REGULATOR_NAMES,
    REGULATOR_EVALUATORS,
)

# ---------------------------------------------------------------------------
# Section 3 - Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
ART_DIR = resolve_script(None, 'artifacts')
ART_DIR.mkdir(parents=True, exist_ok=True)

SESSION = "S85"                                                     # (local)
GATE_ID = "S85-W12-ELIM-8"                                          # (local)
SCHEME = "regulator-invariance-taxonomy"                            # (local)
CONVENTION = "5-regulator-atlas-W0"                                 # (local)
L_MAX = 10                                                          # (local) canonical anchor

# Pre-registered class boundaries (plan §W12-4 line 174)
CLASS_THRESH_A = 0.001                                              # (local) ABS spread
CLASS_THRESH_B_UPPER = 0.01                                         # (local) ABS spread
CLASS_THRESH_C_UPPER = 0.1                                          # (local) ABS spread
CLUSTER_TOL = 0.001                                                 # (local) 4/5 cluster radius

# Pre-registered 16 observables (plan §W12-4 line 173)
# Each observable is a (name, evaluator_kind, payload) tuple:
#   evaluator_kind = "scalar" → constant regardless of regulator
#   evaluator_kind = "spectral_moment" → payload is n in a_n
OBSERVABLES = (                                                     # (local)
    ("a_0", "spectral_moment", 0),
    ("a_2", "spectral_moment", 1),     # a_2 = (1/Vol) Σ d / C^1
    ("a_4", "spectral_moment", 2),     # a_4 = (1/Vol) Σ d / C^2
    ("m_H",             "scalar", float(m_H_obs)),
    ("m_t",             "scalar", float(m_t_pole)),
    ("alpha_s_MZ",      "scalar", float(alpha_s_MZ_obs)),
    ("w0_FW",           "scalar", float(w0_FW)),
    ("n_s",             "scalar", float(n_s_framework)),
    ("tau_fold",        "scalar", float(tau_fold)),
    ("dS_fold",         "scalar", float(dS_fold)),
    ("d2S_fold",        "scalar", float(d2S_fold)),
    ("S_fold",          "scalar", float(S_fold)),
    ("Delta_BCS",       "scalar", float(Delta_BCS)),
    ("K_substrate",     "scalar", float(K_base)),    # K_substrate (plan) = K_base (canonical)
    ("K_R5",            "scalar", float(K_R5)),
    ("K_crit",          "scalar", float(K_crit)),
)

assert len(OBSERVABLES) == 16, f"OBSERVABLES must be 16, got {len(OBSERVABLES)}"

INPUT_FILES = [                                                     # (local)
    resolve_script(None, 'canonical_constants.py'),
    resolve_script(None, '_spectral_action_regulators.py'),
    PROJECT_ROOT / "sessions/archive/session-84/session-84-s3-gen-elimination-synthesis.md",
]

VERDICT_TXT = resolve_output(SESSION[1:], f's{SESSION[1:]}_gate_verdicts.txt')
OUT_NPZ = ART_DIR / "s85_w12_elim8_regulator_matrix.npz"
OUT_PNG = ART_DIR / "s85_w12_elim8_spread_histogram.png"
OUT_JSON = ART_DIR / "s85_w12_elim8_classifications.json"


# ---------------------------------------------------------------------------
# Section 4 - SHA-256 input-pin block
# ---------------------------------------------------------------------------
def sha256_of(path):
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return ""


def log_input_pins(inputs):
    print(f"=== {GATE_ID} - input SHA-256 pins ===")
    pins = {}                                                       # (local)
    for p in inputs:
        sha = sha256_of(p)                                          # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")   # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
    script_bytes = script_path.read_bytes() if script_path.exists() else b""   # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")                   # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes); h_audit.update(canonical_bytes); h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                     # (local)
    content = hashlib.sha256(script_bytes).hexdigest()              # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 - Per-observable evaluator + classifier
# ---------------------------------------------------------------------------
def evaluate_observable(obs_name, kind, payload, regulator_name):
    """Return the value of observable `obs_name` under `regulator_name`."""
    if kind == "scalar":
        # Canonical scalar: regulator-independent by definition
        return payload
    if kind == "spectral_moment":
        evaluator = REGULATOR_EVALUATORS[regulator_name]
        return evaluator(payload, L_MAX, Vol_SU3_Haar)
    raise ValueError(f"unknown evaluator kind: {kind}")


def compute_spread_and_cluster(values):
    """Return (spread, has_4of5_cluster)."""
    arr = np.asarray(values, dtype=np.float64)                      # (local)
    mean = np.mean(arr)                                             # (local)
    if np.abs(mean) < 1e-300:
        # Zero-mean observable (should not happen for any of the 16).
        return 0.0, True
    spread = (np.max(arr) - np.min(arr)) / np.abs(mean)             # (local)
    # 4-of-5 cluster predicate: exists a sub-array of 4 values within
    # CLUSTER_TOL (relative) of each other.
    has_cluster = False                                             # (local)
    for exclude_idx in range(len(arr)):
        subset = np.delete(arr, exclude_idx)                        # (local)
        submean = np.mean(subset)                                   # (local)
        subspread = (np.max(subset) - np.min(subset)) / np.abs(submean) if np.abs(submean) > 1e-300 else 0.0  # (local)
        if subspread < CLUSTER_TOL:
            has_cluster = True
            break
    return float(spread), has_cluster


def classify(spread, has_cluster):
    """4-class partition per plan §W12-4 Step 2."""
    if spread < CLASS_THRESH_A:
        return "a_INVARIANT"
    if spread < CLASS_THRESH_B_UPPER and has_cluster:
        return "b_CONDITIONALLY-INVARIANT"
    if spread < CLASS_THRESH_C_UPPER:
        return "c_SCHEME-DEPENDENT"
    return "d_STRUCTURALLY-DIVERGENT"


# ---------------------------------------------------------------------------
# Section 6 - Compute
# ---------------------------------------------------------------------------
def compute():
    n_obs = len(OBSERVABLES)                                        # (local)
    n_reg = len(REGULATOR_NAMES)                                    # (local)
    print(f"  evaluating {n_obs} observables × {n_reg} regulators = "
          f"{n_obs * n_reg} cells")
    print()

    value_matrix = np.zeros((n_obs, n_reg), dtype=np.float64)       # (local)
    spread_arr = np.zeros(n_obs, dtype=np.float64)                  # (local)
    cluster_arr = np.zeros(n_obs, dtype=bool)                       # (local)
    class_arr = []                                                  # (local)

    print(f"  {'observable':16s}  " + "  ".join(f"{r:>13s}" for r in REGULATOR_NAMES) +
          f"  {'spread':>10s}  class")
    for i, (name, kind, payload) in enumerate(OBSERVABLES):
        row = []                                                    # (local)
        for j, reg in enumerate(REGULATOR_NAMES):
            v = evaluate_observable(name, kind, payload, reg)
            value_matrix[i, j] = v
            row.append(v)
        spread, has_cluster = compute_spread_and_cluster(row)
        spread_arr[i] = spread
        cluster_arr[i] = has_cluster
        cls = classify(spread, has_cluster)                         # (local)
        class_arr.append(cls)
        print(f"  {name:16s}  " +
              "  ".join(f"{v:.6e}" for v in row) +
              f"  {spread:.4e}  {cls}")

    # Class populations
    class_pop = {                                                   # (local)
        "a_INVARIANT": 0,
        "b_CONDITIONALLY-INVARIANT": 0,
        "c_SCHEME-DEPENDENT": 0,
        "d_STRUCTURALLY-DIVERGENT": 0,
    }
    for cls in class_arr:
        class_pop[cls] += 1
    coverage = sum(class_pop.values()) / n_obs                      # (local)
    unclassifiable = n_obs - sum(class_pop.values())                # (local)

    return {
        "value_matrix": value_matrix,
        "spread_arr": spread_arr,
        "cluster_arr": cluster_arr,
        "class_arr": class_arr,
        "class_pop": class_pop,
        "coverage": coverage,
        "unclassifiable": unclassifiable,
        "n_obs": n_obs,
        "n_reg": n_reg,
    }


def evaluate_gate(r):
    pop = r["class_pop"]                                            # (local)
    if r["unclassifiable"] >= 1:
        return "FAIL"
    # PASS iff coverage = 16/16 AND no INFO conditions fire
    if r["coverage"] >= 1.0:
        n_b = pop["b_CONDITIONALLY-INVARIANT"]                      # (local)
        if 1 <= n_b <= 3:
            return "INFO"
        return "PASS"
    return "FAIL"


# ---------------------------------------------------------------------------
# Section 7 - Verdict append
# ---------------------------------------------------------------------------
def append_verdict(verdict, value, audit_sha, content_sha):
    val_str = (f"(n_a={value[0]},n_b={value[1]},"
               f"n_c={value[2]},n_d={value[3]})")                   # (local)
    line = (f"{GATE_ID}: {verdict} -- value={val_str} scheme={SCHEME} "
            f"convention={CONVENTION} L_max={L_MAX} "
            f"audit_sha256={audit_sha} content_sha256={content_sha} "
            f"schema_version=S84+\n")                               # (local)
    companion = (f"# audit_sha256 companion row: {GATE_ID} "
                 f"audit={audit_sha[:16]} content={content_sha[:16]}\n")  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


# ---------------------------------------------------------------------------
# Section 8 - Main
# ---------------------------------------------------------------------------
def main():
    t0 = time.time()                                                # (local)
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()                          # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')           # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    r = compute()
    verdict = evaluate_gate(r)
    pop = r["class_pop"]
    value = (pop["a_INVARIANT"], pop["b_CONDITIONALLY-INVARIANT"],
             pop["c_SCHEME-DEPENDENT"], pop["d_STRUCTURALLY-DIVERGENT"])

    print()
    print("  Class populations:")
    for cls, n in pop.items():
        print(f"    {cls:30s}  {n:3d}")
    print(f"  coverage = {r['coverage']:.4f}  ({sum(pop.values())}/{r['n_obs']})")
    print()
    print(f"(value=(n_a={value[0]},n_b={value[1]},n_c={value[2]},n_d={value[3]}), "
          f"scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")

    # Save NPZ
    np.savez_compressed(
        OUT_NPZ,
        value_matrix=r["value_matrix"],
        spread_arr=r["spread_arr"],
        cluster_arr=r["cluster_arr"],
        class_arr=np.array(r["class_arr"], dtype=object),
        observable_names=np.array([o[0] for o in OBSERVABLES], dtype=object),
        regulator_names=np.array(REGULATOR_NAMES, dtype=object),
    )

    # Save JSON
    with OUT_JSON.open("w", encoding="utf-8") as fp:
        json.dump({
            "gate_id": GATE_ID,
            "verdict": verdict,
            "value": value,
            "scheme": SCHEME,
            "convention": CONVENTION,
            "L_max": L_MAX,
            "observables": [
                {"name": name, "kind": kind,
                 "values_by_regulator": dict(zip(REGULATOR_NAMES,
                                                  r["value_matrix"][i].tolist())),
                 "spread": float(r["spread_arr"][i]),
                 "has_4of5_cluster": bool(r["cluster_arr"][i]),
                 "class": r["class_arr"][i]}
                for i, (name, kind, _) in enumerate(OBSERVABLES)
            ],
            "class_populations": pop,
            "coverage": r["coverage"],
            "audit_sha256": audit_sha,
            "content_sha256": content_sha,
            "pins": pins,
        }, fp, indent=2)

    # Spread histogram
    fig, ax = plt.subplots(figsize=(10, 6))
    log_spread = np.log10(np.maximum(r["spread_arr"], 1e-16))       # (local)
    colors = []                                                     # (local)
    for cls in r["class_arr"]:
        if cls.startswith("a"):
            colors.append("#1f77b4")
        elif cls.startswith("b"):
            colors.append("#2ca02c")
        elif cls.startswith("c"):
            colors.append("#ff7f0e")
        else:
            colors.append("#d62728")
    names = [o[0] for o in OBSERVABLES]                             # (local)
    ax.bar(range(len(names)), log_spread, color=colors)
    for thresh, label in [
        (np.log10(CLASS_THRESH_A), "class (a) / (b-c) boundary (log₁₀ 0.001)"),
        (np.log10(CLASS_THRESH_B_UPPER), "(b) / (c) boundary (log₁₀ 0.01)"),
        (np.log10(CLASS_THRESH_C_UPPER), "(c) / (d) boundary (log₁₀ 0.1)"),
    ]:
        ax.axhline(thresh, color="k", ls="--", lw=0.7)
        ax.text(len(names) - 0.5, thresh, label, fontsize=7, va="bottom", ha="right")
    ax.set_xticks(range(len(names)))
    ax.set_xticklabels(names, rotation=45, ha="right", fontsize=8)
    ax.set_ylabel(r"$\log_{10}$(regulator spread)", fontsize=11)
    ax.set_title(f"{GATE_ID}: 16-observable regulator-spread taxonomy "
                 f"(verdict={verdict}; blue=(a), green=(b), orange=(c), red=(d))",
                 fontsize=11)
    ax.grid(True, alpha=0.3, axis="y")
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=120)
    plt.close(fig)

    append_verdict(verdict, value, audit_sha, content_sha)

    wall = time.time() - t0                                         # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
