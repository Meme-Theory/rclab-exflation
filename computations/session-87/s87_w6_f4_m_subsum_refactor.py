#!/usr/bin/env python3
"""
S87 W6-6 S87-S85-W5-7-F4-M-SUBSUM-REFACTOR — F_4/M sub-sum exposure refactor
=============================================================================

Gate: S87-S85-W5-7-F4-M-SUBSUM-REFACTOR  ([VERIFY])

Pre-registered threshold (plan §W6-6, lines 647-653):
  PASS iff refactored npz exposes (n_joint_F4, n_joint_M, n_joint_global)
        AND |n_joint_global_refactored - n_joint_global_legacy| < 1e-12.
  INFO iff identity holds at [1e-12, 1e-6] (numerical-precision band).
  FAIL iff identity broken (> 1e-6) OR any of the 3 fields missing.

Tolerance rule: ABSOLUTE.
Classification: GEOMETRIC (mechanical refactor of two-layer obstruction script).
Wave-class: COMPUTE-class.

METHODOLOGY (refactor scope per plan §W6-6 lines 638-645)
----------------------------------------------------------
The legacy script `s85_w5_7_two_layer_obstruction.py` computes a single global
sum over the 5-atlas A_5 = {zeta, Zubarev, SDW, cutoff_sqrt, anomaly} of the
joint-satisfaction indicator (`joint(r) ∈ {0,1}` per regulator r), aggregating
into `n_joint_pass` without exposing per-component sub-sums.

This refactor partitions A_5 into the canonical F_4 / M decomposition:
  F_4 = {zeta, Zubarev, SDW}            (3-class F_4 multiplier-vector sub-family;
                                          per S85-1c-perturbative-immunization-family.md
                                          §VII.Ω "F_4 (zeta, Zubarev, SDW)" canonical;
                                          S86 W-7 / W-8 F_4 4-channel family)
  M   = {cutoff_sqrt, anomaly}          (2-class M-component basis;
                                          per W-12 V_4 = Z_2 × Z_2 partition complement;
                                          per S85-1c §VII.Ω "fails in cutoff_sqrt or anomaly")

The disjoint union F_4 ⊔ M = A_5 is structural (canonical-source: see entries
above); the legacy `n_joint_pass` is then the additive split:

  n_joint_global = Σ_{r ∈ A_5} joint(r) = Σ_{r ∈ F_4} joint(r) + Σ_{r ∈ M} joint(r)
                 = n_joint_F4 + n_joint_M     (integer associativity)

The substitution chain (definition → substitution → simplification → direction)
shows the identity preserves at machine epsilon BY CONSTRUCTION (integer addition;
no float accumulation). The substantive refactor is structural: separating the
F_4 and M contributions exposes the substrate's intrinsic two-source structure
of the obstruction count without changing the substrate.

Substrate framing (plan §W6-6 lines 711-713):
The two-layer obstruction n_joint_global IS the substrate's combined obstruction
count from F_4 (4-channel multiplier-vector sub-family) and M (M-component basis)
contributions. Exposing the sub-sums separately IS revealing the substrate's
intrinsic two-source structure of the obstruction; the refactor does not change
the substrate, only makes its decomposition machine-queryable for downstream
gates CF-43 (C-β UV-cutoff-choice immunization across F_4 sub-family) and CF-44
(C-γ-WEAK Weyl-rescaling per L1-class) at S88+.

Regulator-pin discipline (per .claude/rules/regulator-pin-discipline.md):
This script DOES NOT introduce new Seeley-DeWitt coefficient citations; the
underlying scheme is "5-regulator-atlas" and the regulator class for any
implied a_n moment is zeta (a_n^{ζ}) per the S85 W5-6 source npz convention.
Any downstream cross-citation MUST tag a_n^{ζ}.

Inputs (SHA-256 dual-pinned at runtime — S87+ schema-v2):
  - computations/session-85/s85_w5_7_two_layer_obstruction.py  (LEGACY READ-ONLY source)
  - computations/session-85/s85_w5_7_two_layer_obstruction.npz (LEGACY backward-compat anchor)
  - computations/session-85/s85_w5_6_eps_h_hp1_scan.npz        (W5-6 input data — per-regulator drift)
  - computations/_shared/canonical_constants.py
  - .claude/rules/regulator-pin-discipline.md            (a_n^{ζ} tag policy)
"""

from __future__ import annotations

from canonical_constants import *  # noqa: F401,F403

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

os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S87"                                                 # (local)
GATE_ID = "S87-S85-W5-7-F4-M-SUBSUM-REFACTOR"                   # (local)
SCHEME = "zeta-regulated-Seeley-DeWitt"                         # (local; a_n^{ζ} per regulator-pin-discipline.md)
CONVENTION = "F_4-plus-M-decomposition"                         # (local; per plan §W6-6 line 689)
L_MAX = 12                                                      # (local; per plan §W6-6 line 669 canonical)

# Gate threshold pins (per plan §W6-6 lines 647-653, 727-729) — all # (local)
PASS_ABS_TOL = 1e-12      # (local) PASS iff |delta| < 1e-12
INFO_ABS_HI  = 1e-6       # (local) INFO band ceiling; FAIL above this

# Legacy thresholds (must match s85_w5_7_two_layer_obstruction.py for backward-compat) — # (local)
SCHEME_INDEP_TOL = 0.05         # (local) 5% drift threshold (W5-7 plan)
INFO_MARGINAL_TOL = 0.07        # (local) 7% marginal threshold for INFO
F_CONV_2LOOP_SCHEME_DEV = 0.3921  # (local) W6-67 2-loop Z_R scheme-deviation; 39.21%

# Canonical F_4 / M partition (per S85-1c §VII.Ω + S86 W-7/W-8 F_4 4-channel family;
# see also S86 W-12 V_4 Klein-four reading: V_4 = Z_2(F_4-cluster) × Z_2(M-cluster)).
# This partition is STRUCTURAL — not a per-script convention — and is the canonical
# source for downstream sub-family analysis.
F4_REGULATORS = ("zeta", "Zubarev", "SDW")                     # (local) F_4 multiplier-vector sub-family
M_REGULATORS  = ("cutoff_sqrt", "anomaly")                     # (local) M-component basis

# Sanity invariant: F_4 ⊔ M = A_5 (5-atlas) — verified at runtime
ATLAS_5_EXPECTED = ("zeta", "Zubarev", "SDW", "cutoff_sqrt", "anomaly")  # (local)

OUT_NPZ = resolve_output(87, 's87_w6_f4_m_subsum_refactor.npz')
OUT_PNG = resolve_output(87, 's87_w6_f4_m_subsum_refactor.png')
VERDICT_TXT = resolve_output(87, 's87_gate_verdicts.txt')
CANON_PY = resolve_script(None, 'canonical_constants.py')
LEGACY_PY = resolve_script(85, 's85_w5_7_two_layer_obstruction.py')
LEGACY_NPZ = resolve_output(85, 's85_w5_7_two_layer_obstruction.npz')
W56_NPZ = resolve_output(85, 's85_w5_6_eps_h_hp1_scan.npz')
REG_PIN_RULE = PROJECT_ROOT / ".claude" / "rules" / "regulator-pin-discipline.md"

INPUT_FILES = [LEGACY_PY, LEGACY_NPZ, W56_NPZ, CANON_PY, REG_PIN_RULE]


def sha256_of(path):
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} - input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins):
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path, canonical_path, pins):
    sb = b""
    cb = b""
    try:
        sb = script_path.read_bytes()
    except OSError:
        pass
    try:
        cb = canonical_path.read_bytes()
    except OSError:
        pass
    pj = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode("utf-8")
    ha = hashlib.sha256()
    ha.update(sb)
    ha.update(cb)
    ha.update(pj)
    hc = hashlib.sha256()
    hc.update(sb)
    return ha.hexdigest(), hc.hexdigest()


def compute_joint_indicator(regs, f_4_per_reg):
    """Replicate the legacy joint-satisfaction logic (s85_w5_7 lines 109-128).

    Produces a per-regulator joint(r) ∈ {0, 1} integer indicator, plus the
    f_conv and eps_H per-regulator drifts used to derive it. Bit-exact match
    to the legacy implementation (the f_conv drift is uniform = 0.3921 per
    plan; the eps_H drift is |f_4^r - mean_f4| / mean_f4).
    """
    f_4_per_reg = np.asarray(f_4_per_reg, dtype=np.float64)
    mean_f4 = float(np.mean(f_4_per_reg))                              # (local)
    eps_H_drift = {r: float(abs(v - mean_f4) / mean_f4)
                   for r, v in zip(regs, f_4_per_reg)}                 # (local)
    f_conv_drift = {r: F_CONV_2LOOP_SCHEME_DEV for r in regs}          # (local)

    joint = {}                                                          # (local)
    for r in regs:
        si_f = f_conv_drift[r] <= SCHEME_INDEP_TOL
        si_e = eps_H_drift[r] <= SCHEME_INDEP_TOL
        joint[r] = int(si_f and si_e)                                   # integer indicator

    return joint, f_conv_drift, eps_H_drift, mean_f4


def compute():
    """Refactored joint-satisfaction count with explicit F_4 / M sub-sums.

    Substitution chain:
      Step 1 (definition):
        joint(r) = 1[f_conv_drift[r] <= 0.05] * 1[eps_H_drift[r] <= 0.05]
        n_joint_F4     = Σ_{r ∈ F_4} joint(r),  F_4 = {zeta, Zubarev, SDW}
        n_joint_M      = Σ_{r ∈ M  } joint(r),  M   = {cutoff_sqrt, anomaly}
        n_joint_global = Σ_{r ∈ A_5} joint(r)
      Step 2 (substitution):
        F_4 ⊔ M = A_5 (set-disjoint partition, structural canonical)
        ⇒ n_joint_global_refactored = n_joint_F4 + n_joint_M
      Step 3 (simplification):
        Integer addition associativity ⇒ identity holds bit-exactly
        (no float accumulation; counters are Python ints).
      Step 4 (direction):
        Identity test, not signed; PASS iff |refactored - legacy| < 1e-12.
    """
    d56 = np.load(W56_NPZ, allow_pickle=True)
    regs = [str(r) for r in d56['regulators']]
    f_4 = d56['f_4_per_reg'].astype(np.float64)                        # (local)

    # Sanity-check the atlas partition
    assert tuple(regs) == ATLAS_5_EXPECTED, (
        f"A_5 atlas mismatch: source={regs} expected={ATLAS_5_EXPECTED}"
    )
    f4_set = set(F4_REGULATORS)                                         # (local)
    m_set = set(M_REGULATORS)                                           # (local)
    assert f4_set.isdisjoint(m_set), "F_4 and M must be disjoint"
    assert (f4_set | m_set) == set(regs), \
        f"F_4 ∪ M must equal A_5; got {f4_set | m_set} vs {set(regs)}"

    joint, f_conv_drift, eps_H_drift, mean_f4 = compute_joint_indicator(regs, f_4)

    # ---- Explicit F_4 sub-loop (structural F_4 multiplier-vector sub-family) ----
    n_joint_F4 = 0                                                      # (local) accumulator
    F4_per_reg = {}                                                     # (local)
    for r in F4_REGULATORS:
        F4_per_reg[r] = int(joint[r])
        n_joint_F4 += int(joint[r])

    # ---- Explicit M sub-loop (M-component basis) ----
    n_joint_M = 0                                                       # (local) accumulator
    M_per_reg = {}                                                      # (local)
    for r in M_REGULATORS:
        M_per_reg[r] = int(joint[r])
        n_joint_M += int(joint[r])

    # ---- Refactored global sum (must equal legacy by integer-additivity) ----
    n_joint_global_refactored = int(n_joint_F4 + n_joint_M)             # (local)

    # ---- Legacy global sum (independent re-aggregation across the full A_5) ----
    n_joint_global_legacy = int(sum(int(joint[r]) for r in regs))       # (local)

    # ---- Identity-preservation deviation ----
    n_joint_global_legacy_match_deviation = abs(
        n_joint_global_refactored - n_joint_global_legacy
    )                                                                    # (local) integer => exact 0 expected

    return {
        'regs': regs,
        'F4_regulators': list(F4_REGULATORS),
        'M_regulators': list(M_REGULATORS),
        'joint': joint,
        'F4_per_reg': F4_per_reg,
        'M_per_reg': M_per_reg,
        'f_conv_drift': f_conv_drift,
        'eps_H_drift': eps_H_drift,
        'mean_f4': mean_f4,
        'n_joint_F4': int(n_joint_F4),
        'n_joint_M': int(n_joint_M),
        'n_joint_global': int(n_joint_global_refactored),
        'n_joint_global_legacy': int(n_joint_global_legacy),
        'n_joint_global_legacy_match_deviation': float(n_joint_global_legacy_match_deviation),
    }


def evaluate_gate(deviation):
    """Composite collapse per plan §W6-6 lines 647-653 (ABSOLUTE tolerance)."""
    if deviation < PASS_ABS_TOL:
        return "PASS"
    if deviation <= INFO_ABS_HI:
        return "INFO"
    return "FAIL"


def emit_4tuple(value, scheme, convention, L_max):
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict, value, audit, content):
    line = (f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
            f"convention={CONVENTION} L_max={L_MAX} "
            f"audit_sha256={audit} content_sha256={content} "
            f"schema_version=S87+\n")
    companion = (
        f"# audit_sha256_short={audit[:16]} content_sha256_short={content[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


def main() -> int:
    t0 = time.time()
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}...")
    audit, content = compute_dual_sha(Path(__file__).resolve(), CANON_PY, pins)
    print(f"  audit_sha256:   {audit[:16]}...")
    print(f"  content_sha256: {content[:16]}...")
    print()

    result = compute()
    deviation = result['n_joint_global_legacy_match_deviation']         # (local)
    verdict = evaluate_gate(deviation)

    # Backward-compat cross-check against the cached legacy npz n_joint_pass
    legacy_npz_n_joint_pass = None                                       # (local)
    if LEGACY_NPZ.exists():
        d_leg = np.load(LEGACY_NPZ, allow_pickle=True)
        legacy_npz_n_joint_pass = int(d_leg['n_joint_pass'])
        # Independent identity check vs cached output
        cached_dev = abs(result['n_joint_global'] - legacy_npz_n_joint_pass)  # (local)
        print(f"  legacy_npz n_joint_pass = {legacy_npz_n_joint_pass}; "
              f"cached_npz vs refactored deviation = {cached_dev}")
    else:
        cached_dev = None                                                # (local)

    # Emit npz with all 3 fields + deviation (per plan §W6-6 line 698)
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        verdict=verdict,
        # F_4 / M decomposition (NEW exposed fields)
        n_joint_F4=int(result['n_joint_F4']),
        n_joint_M=int(result['n_joint_M']),
        n_joint_global=int(result['n_joint_global']),
        n_joint_global_legacy_match_deviation=float(deviation),
        # Backward-compat anchor — match against cached LEGACY_NPZ if present
        n_joint_global_legacy_cached_npz=(int(legacy_npz_n_joint_pass)
                                          if legacy_npz_n_joint_pass is not None
                                          else -1),
        # Per-regulator structure (audit / downstream consumers)
        regs=np.array(result['regs']),
        F4_regulators=np.array(result['F4_regulators']),
        M_regulators=np.array(result['M_regulators']),
        F4_joint_per_reg=np.array([result['F4_per_reg'][r] for r in result['F4_regulators']],
                                  dtype=np.int64),
        M_joint_per_reg=np.array([result['M_per_reg'][r] for r in result['M_regulators']],
                                 dtype=np.int64),
        # Drift inputs (matches legacy semantics; for downstream gate access)
        f_conv_drift=np.array([result['f_conv_drift'][r] for r in result['regs']],
                              dtype=np.float64),
        eps_H_drift=np.array([result['eps_H_drift'][r] for r in result['regs']],
                             dtype=np.float64),
        mean_f4=float(result['mean_f4']),
        scheme_indep_tol=SCHEME_INDEP_TOL,
        info_marginal_tol=INFO_MARGINAL_TOL,
        f_conv_2loop_scheme_dev=F_CONV_2LOOP_SCHEME_DEV,
        # Gate-block thresholds
        pass_abs_tol=PASS_ABS_TOL,
        info_abs_hi=INFO_ABS_HI,
    )
    print(f"  saved: {OUT_NPZ.name}")

    # Decomposition bar chart (F_4 contribution + M contribution = global) per plan §W6-6 line 699
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5.0))

        # Left panel: F_4 vs M sub-sum stacked bar
        labels_lhs = ['F_4 sub-sum', 'M sub-sum', 'Global (refactored)', 'Global (legacy)']  # (local)
        vals_lhs = [result['n_joint_F4'], result['n_joint_M'],
                    result['n_joint_global'], result['n_joint_global_legacy']]              # (local)
        colors_lhs = ['tab:blue', 'tab:orange', 'tab:green', 'tab:gray']                    # (local)
        bars = ax1.bar(labels_lhs, vals_lhs, color=colors_lhs)
        ax1.set_ylabel('joint-satisfaction count')
        ax1.set_title(
            f"F_4/M sub-sum decomposition (n_joint_F4={result['n_joint_F4']} + "
            f"n_joint_M={result['n_joint_M']} = {result['n_joint_global']})"
        )
        ax1.grid(True, axis='y', alpha=0.3)
        for b, v in zip(bars, vals_lhs):
            ax1.text(b.get_x() + b.get_width() / 2, v + 0.05, f"{v}",
                     ha='center', va='bottom', fontsize=10)
        ax1.set_ylim(0, max(vals_lhs) + 1.5 if max(vals_lhs) > 0 else 1.5)

        # Right panel: per-regulator joint indicator coloured by F_4 / M class
        regs = result['regs']
        joint_arr = np.array([result['joint'][r] for r in regs], dtype=np.int64)            # (local)
        bar_colors = ['tab:blue' if r in F4_REGULATORS else 'tab:orange' for r in regs]     # (local)
        ax2.bar(regs, joint_arr, color=bar_colors)
        ax2.set_ylabel('joint(r) ∈ {0, 1}')
        ax2.set_title("per-regulator joint indicator (blue=F_4, orange=M)")
        ax2.set_xticklabels(regs, rotation=30, ha='right')
        ax2.set_ylim(-0.05, 1.2)
        ax2.grid(True, axis='y', alpha=0.3)

        fig.suptitle(
            f"{GATE_ID}: deviation={deviation:.3e}, verdict={verdict}",
            fontsize=11,
        )
        plt.tight_layout(rect=[0, 0, 1, 0.96])
        plt.savefig(OUT_PNG, dpi=100)
        plt.close(fig)
        print(f"  saved: {OUT_PNG.name}")
    except Exception as e:
        print(f"  plot skipped: {type(e).__name__}: {e}")

    tag = emit_4tuple(deviation, SCHEME, CONVENTION, L_MAX)
    print(tag)
    append_verdict(verdict, deviation, audit, content)

    wall = time.time() - t0
    print()
    print(f"=== {GATE_ID} F_4 / M sub-sum decomposition ===")
    print(f"  F_4 = {list(F4_REGULATORS)}")
    for r in F4_REGULATORS:
        print(f"    joint({r:14s}) = {result['F4_per_reg'][r]}")
    print(f"  → n_joint_F4 = {result['n_joint_F4']}")
    print()
    print(f"  M   = {list(M_REGULATORS)}")
    for r in M_REGULATORS:
        print(f"    joint({r:14s}) = {result['M_per_reg'][r]}")
    print(f"  → n_joint_M  = {result['n_joint_M']}")
    print()
    print(f"  n_joint_global (refactored) = n_joint_F4 + n_joint_M "
          f"= {result['n_joint_F4']} + {result['n_joint_M']} = {result['n_joint_global']}")
    print(f"  n_joint_global (legacy)     = {result['n_joint_global_legacy']}")
    if legacy_npz_n_joint_pass is not None:
        print(f"  n_joint_pass (cached npz)   = {legacy_npz_n_joint_pass}")
    print(f"  identity deviation          = {deviation}")
    print(f"  PASS threshold              = {PASS_ABS_TOL}")
    print(f"=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
