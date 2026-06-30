#!/usr/bin/env python3
"""
S87 W8-2 — S87-W4-2-RE-RUN-UNDER-A_4 (CF-48)
=============================================

Gate: re-derive the W4-2 max_pair_ratio gate on the cascaded A_4 atlas
      (cutoff_sqrt removed); verify cluster-span canonical-metric identity
      |ratio − 2| < 1e-14 at L_max=12 where ratio = b_pow(span_2)/b_pow(span_3).

Pre-registration source: `sessions/session-plan/session-87-plan-w8.md` §W8-2.
Anchor source for max_pair_ratio_A_5: `sessions/archive/session-86/session-86-w4-workingpaper.md`
  §W4-2 — pole_R table at L_max=10, all-pairs deviation table, max-pair = (ζ, Zubarev)
  with RATIO = 9.240439e-01.

Substitution chain (per plan §9 — verbatim):

  Step 1 (definitions):
    cluster_span(L_max)     := the b_pow function returned by `_cluster_span_extract.py`
                               cluster_span(L_max), evaluated at the two spans 2 and 3
    ratio                   := b_pow(span_2) / b_pow(span_3)
    canonical_metric        := |ratio − 2|              (W0-3 CC-5 anchor metric)
    max_pair_ratio_A_n      := max over unordered pairs {r_i, r_j} ⊂ A_n of
                               |pole_R_i − pole_R_j| / max(|pole_R_i|, |pole_R_j|)
                               evaluated on the n-column atlas at L_max=10
    delta_pr                := |max_pair_ratio_A_4 − max_pair_ratio_A_5|

  Step 2 (substitute):
    Algebraic identity: ratio − 2 = (b_pow(span_2) − 2·b_pow(span_3)) / b_pow(span_3)
                  ⇒ canonical_metric = |b_pow(span_2) − 2·b_pow(span_3)| / |b_pow(span_3)|
    Identity ratio:    normalized_metric / canonical_metric ≈ 1/2 at PASS
                  ⇒ canonical_metric ≈ 2 × normalized_metric at the float-cancellation floor.

  Step 3 (simplify):
    PASS predicate (a):  delta_pr < 1e-15
    PASS predicate (b):  canonical_metric < 1e-14   (= 45 × float_eps refactor band)
    Joint PASS:          (a) AND (b)

  Step 4 (direction):
    A_4 ⊂ A_5 (set-theoretic subset; cutoff_sqrt removed) ⇒
    max_pair_ratio_A_4 ≤ max_pair_ratio_A_5 (any pair in A_4 is a pair in A_5;
    the max over a subset cannot exceed the max over the superset).
    Equality holds iff the A_5 extremal pair did NOT involve cutoff_sqrt.
    Strict inequality ⇒ the A_5 extremum involved cutoff_sqrt; A_4 returns
    the next-largest A_5 pair.

    Cluster-span: W0-3 PASS at L_max=12 reports |ratio − 2| = 2.220e-15
    (≈ 10 × float_eps); refactor preservation requires ≤ 45 × float_eps = 1e-14.

S87+ schema-v2 verdict-line writer mirrors the canonical pattern in
s87_w7_warrant_check_queue.py (audit_sha256 + content_sha256 + dual-SHA
companion + 3-tuple annotation).
"""
from __future__ import annotations

# -----------------------------------------------------------------
# Section 0 - CPU thread cap BEFORE numpy import (env discipline)
# -----------------------------------------------------------------
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

# -----------------------------------------------------------------
# Section 1 - Imports + path resolution
# -----------------------------------------------------------------
import hashlib
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_PATH = Path(__file__).resolve()
SCRIPT_DIR = SCRIPT_PATH.parent
PROJECT_ROOT = SCRIPT_DIR.parent

# Sibling import: _cluster_span_extract lives alongside this script.
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import PI  # noqa: E402,F401  imported for canonical-discipline
from _cluster_span_extract import cluster_span  # noqa: E402

# -----------------------------------------------------------------
# Section 2 - Gate identity + threshold pins (PRE-REGISTRATION; per plan §5/§6)
# -----------------------------------------------------------------
GATE_ID = "S87-W4-2-RE-RUN-UNDER-A_4"            # (local) per plan §1
SCHEME = "cluster_span_canonical_metric"          # (local) per plan §8
CONVENTION = "A_4_post_cascade_4col"              # (local) per plan §8
L_MAX_CLUSTER_SPAN = 12                           # (local) per plan §6
L_MAX_MAX_PAIR_RATIO = 10                         # (local) per plan §6 (W4-2 original)

# Sub-gate (a) tolerances per plan §5
PASS_TOL_A = 1e-15                                # (local) bit-identical preservation
FAIL_TOL_A = 1e-12                                # (local)

# Sub-gate (b) tolerances per plan §5 + epistemic-discipline.md §"Canonical-metric pin extension"
PASS_TOL_B = 1e-14                                # (local) ≈ 45 × float_eps refactor band
FAIL_TOL_B = 1e-13                                # (local)
W0_3_CANONICAL_DEVIATION = 2.220e-15              # (local) S85 W0-3 verdict anchor

# -----------------------------------------------------------------
# Section 3 - W4-2 anchor table (verbatim from session-86-w4-workingpaper.md
#             §W4-2 — pole_R values at L_max=10)
# -----------------------------------------------------------------
# Per-regulator pole values (substrate-distance-1 K_substrate(s=3, R)):
W4_2_POLE_R_A5 = {
    "zeta":         1.581013447264e-01,    # (local) zeta_a_n on positive Casimir spectrum
    "Zubarev":      1.200875443266e-02,    # (local) heat-kernel
    "SDW":          1.581013447264e-01,    # (local) mellin_a_n (= zeta on positive-spectrum)
    "cutoff_sqrt":  1.110026437499e-01,    # (local) hard-cutoff (REMOVED in A_4)
    "anomaly":      3.184675917801e-02,    # (local) Pauli-Villars
}

# A_4 = A_5 \ {cutoff_sqrt}
A_5_COLUMNS = ("zeta", "Zubarev", "SDW", "cutoff_sqrt", "anomaly")
A_4_COLUMNS = ("zeta", "Zubarev", "SDW", "anomaly")

# W4-2 published anchor for max_pair_ratio_A_5 (from s86_gate_verdicts.txt
# verdict line `S86-SECTOR-2-MELLIN-KERNEL-K-INVARIANT`):
W4_2_MAX_PAIR_RATIO_A5 = 9.240439e-01              # (local) at (zeta, Zubarev)
W4_2_MAX_PAIR_PAIR_A5 = ("zeta", "Zubarev")        # (local)

# -----------------------------------------------------------------
# Section 4 - SHA-256 utilities
# -----------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()        # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def closure_hash(pins_dict: dict) -> str:
    """Deterministic SHA-256 over sorted-key input-pin map."""
    items = sorted(pins_dict.items())   # (local)
    h = hashlib.sha256()                # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


# -----------------------------------------------------------------
# Section 5 - max_pair_ratio computation (RATIO = |a-b|/max(|a|,|b|))
# -----------------------------------------------------------------
def compute_max_pair_ratio(pole_dict: dict, columns: tuple) -> tuple:
    """Return (max_ratio, (col_i, col_j)) over unordered pairs in `columns`.

    RATIO definition matches W4-2 working paper: |pole_i - pole_j| / max(|pole_i|, |pole_j|).
    """
    n = len(columns)                    # (local)
    if n < 2:
        return (0.0, (None, None))
    max_ratio = -1.0                    # (local)
    max_pair = (None, None)             # (local)
    pair_ratios = {}                    # (local)
    for i in range(n):
        for j in range(i + 1, n):
            r_i = columns[i]
            r_j = columns[j]
            v_i = pole_dict[r_i]
            v_j = pole_dict[r_j]
            denom = max(abs(v_i), abs(v_j))     # (local)
            if denom == 0.0:
                ratio = 0.0                     # (local)
            else:
                ratio = abs(v_i - v_j) / denom  # (local)
            pair_ratios[(r_i, r_j)] = ratio
            if ratio > max_ratio:
                max_ratio = ratio
                max_pair = (r_i, r_j)
    return (max_ratio, max_pair, pair_ratios)


# -----------------------------------------------------------------
# Section 6 - Main driver
# -----------------------------------------------------------------
def main() -> int:
    t0 = time.time()                            # (local)

    print("=" * 78)
    print(f"{GATE_ID}")
    print("=" * 78)
    print(f"  plan reference : sessions/session-plan/session-87-plan-w8.md §W8-2")
    print(f"  cluster-span L_max = {L_MAX_CLUSTER_SPAN}")
    print(f"  max_pair_ratio L_max = {L_MAX_MAX_PAIR_RATIO}")
    print(f"  A_5 columns : {A_5_COLUMNS}")
    print(f"  A_4 columns : {A_4_COLUMNS} (cutoff_sqrt removed)")
    print()

    # -------------------------------------------------------------
    # Step 1: Input SHA-256 pins (per plan §7)
    # -------------------------------------------------------------
    INPUT_FILES = [
        SCRIPT_DIR / "s84_spectrum_cache_L12_tau019.npz",
        SCRIPT_DIR / "_cluster_span_extract.py",
        SCRIPT_DIR / "canonical_constants.py",
        PROJECT_ROOT / "sessions" / "session-86" / "session-86-w4-workingpaper.md",
        SCRIPT_DIR / "s86_gate_verdicts.txt",
        PROJECT_ROOT / "sessions" / "framework" / "registry" / "cutoff-sqrt-adjudication.md",
    ]

    print("=== Input SHA-256 pins ===")
    pins = {}                       # (local)
    for p in INPUT_FILES:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        if sha == "":
            print(f"  {rel}: MISSING (sha256 = '')")
        else:
            print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha

    audit_sha = closure_hash(pins)
    print(f"  audit_sha256 (closure) = {audit_sha[:16]}...")
    print()

    # -------------------------------------------------------------
    # Step 2: Sub-gate (b) — cluster-span canonical-metric identity at L_max=12
    # -------------------------------------------------------------
    print("=" * 78)
    print("SUB-GATE (b): cluster-span canonical-metric identity at L_max=12")
    print("=" * 78)
    b_pow_span_2, b_pow_span_3 = cluster_span(L_MAX_CLUSTER_SPAN)
    print(f"  b_pow(span_2) = {b_pow_span_2:.16e}")
    print(f"  b_pow(span_3) = {b_pow_span_3:.16e}")

    # Canonical metric per epistemic-discipline.md §"Canonical-metric pin extension":
    #   canonical_metric = |ratio − 2|  where  ratio = b_pow(span_2) / b_pow(span_3)
    # NOT the normalized form |b2 − 2·b3| / |b2|.
    if b_pow_span_3 == 0.0:
        print("  ABORT: b_pow(span_3) = 0 — cannot form ratio.")
        return 1
    ratio_2_3 = b_pow_span_2 / b_pow_span_3                                # (local)
    canonical_metric = abs(ratio_2_3 - 2.0)                                # (local)
    # Cross-record: normalized form factor-2 below the canonical (PROHIBITED form).
    normalized_metric = abs(b_pow_span_2 - 2.0 * b_pow_span_3) / abs(b_pow_span_2)  # (local)

    print(f"  ratio = b_pow(span_2)/b_pow(span_3) = {ratio_2_3:.16e}")
    print(f"  canonical_metric = |ratio − 2|     = {canonical_metric:.3e}")
    print(f"  normalized_metric (PROHIBITED)     = {normalized_metric:.3e}")
    print(f"  ratio (canonical/normalized)       = {canonical_metric / max(normalized_metric, 1e-30):.3f}  "
          f"(expected ≈ 2 at PASS — canonical = 2 × normalized at float floor)")
    print(f"  W0-3 canonical anchor (S85)        = {W0_3_CANONICAL_DEVIATION:.3e}")
    print()

    # Sub-gate (b) verdict
    if canonical_metric < PASS_TOL_B:
        verdict_b = "PASS"
    elif canonical_metric < FAIL_TOL_B:
        verdict_b = "INFO"
    else:
        verdict_b = "FAIL"
    print(f"  Sub-gate (b) verdict: {verdict_b} (PASS_TOL = {PASS_TOL_B:.0e})")
    print()

    # -------------------------------------------------------------
    # Step 3: Sub-gate (a) — max_pair_ratio invariance under A_5 → A_4
    # -------------------------------------------------------------
    print("=" * 78)
    print("SUB-GATE (a): max_pair_ratio invariance under A_5 → A_4 reduction")
    print("=" * 78)

    # max_pair_ratio on A_5 (as a SELF-CONSISTENCY reproduction; should match anchor)
    max_pair_ratio_A5_recomputed, max_pair_A5, pair_ratios_A5 = compute_max_pair_ratio(
        W4_2_POLE_R_A5, A_5_COLUMNS
    )
    print(f"  max_pair_ratio_A_5 (recomputed) = {max_pair_ratio_A5_recomputed:.6e} "
          f"at pair {max_pair_A5}")
    print(f"  max_pair_ratio_A_5 (W4-2 anchor)= {W4_2_MAX_PAIR_RATIO_A5:.6e} "
          f"at pair {W4_2_MAX_PAIR_PAIR_A5}")
    A5_recompute_match = abs(max_pair_ratio_A5_recomputed - W4_2_MAX_PAIR_RATIO_A5) < 1e-6  # (local)
    print(f"  A_5 self-consistency (within 1e-6) : {A5_recompute_match}")
    print()

    # max_pair_ratio on A_4
    max_pair_ratio_A4, max_pair_A4, pair_ratios_A4 = compute_max_pair_ratio(
        W4_2_POLE_R_A5, A_4_COLUMNS  # use the same pole table; A_4 is set-subset
    )
    print(f"  max_pair_ratio_A_4              = {max_pair_ratio_A4:.6e} "
          f"at pair {max_pair_A4}")

    # Was cutoff_sqrt the extremal pair on A_5?
    was_cutoff_sqrt_extremal_in_A5 = ("cutoff_sqrt" in max_pair_A5)              # (local)
    print(f"  Was cutoff_sqrt in A_5 extremal pair? {was_cutoff_sqrt_extremal_in_A5}")
    delta_pr = abs(max_pair_ratio_A4 - W4_2_MAX_PAIR_RATIO_A5)                   # (local)
    print(f"  delta_pr = |max_pair_ratio_A_4 − max_pair_ratio_A_5_anchor| "
          f"= {delta_pr:.6e}")
    print()

    # Direction check (substitution-chain Step 4):
    # A_4 ⊂ A_5 ⇒ max_pair_ratio_A_4 ≤ max_pair_ratio_A_5_recomputed (substrate-set bound).
    direction_ok = max_pair_ratio_A4 <= max_pair_ratio_A5_recomputed + 1e-15     # (local)
    print(f"  Direction check: max_pair_ratio_A_4 ≤ max_pair_ratio_A_5 ? {direction_ok}")
    print()

    # Sub-gate (a) verdict per plan §5
    if not was_cutoff_sqrt_extremal_in_A5:
        # Bit-identical reproduction expected: the same extremal pair survives in A_4.
        if delta_pr < PASS_TOL_A:
            verdict_a = "PASS"
            verdict_a_note = "non-extremal cutoff_sqrt; bit-identical preservation"  # (local)
        elif delta_pr < FAIL_TOL_A:
            verdict_a = "INFO"
            verdict_a_note = "non-extremal cutoff_sqrt; precision-floor band"        # (local)
        else:
            verdict_a = "FAIL"
            verdict_a_note = "non-extremal cutoff_sqrt; loss of bit-identity"        # (local)
    else:
        # cutoff_sqrt WAS extremal in A_5; per plan §5 this routes to sub-case (a-bis):
        # max_pair_ratio_A_4 must produce the next-largest A_5 ratio (which it does
        # by construction — A_4 = A_5 \ {cutoff_sqrt}, so the max over A_4 IS the
        # next-largest A_5 ratio after removing any cutoff_sqrt-involving pairs).
        # PASS the gate with explicit DIAGNOSTIC tag; the new A_4 max becomes canonical.
        verdict_a = "PASS-DIAGNOSTIC"
        verdict_a_note = "cutoff_sqrt WAS extremal in A_5; A_4 returns next-largest pair (canonical re-anchor)"  # (local)
    print(f"  Sub-gate (a) verdict: {verdict_a} ({verdict_a_note})")
    print()

    # -------------------------------------------------------------
    # Step 4: Joint composite verdict (per plan §5)
    # -------------------------------------------------------------
    # PASS iff (a) PASS AND (b) PASS; INFO if either INFO and neither FAIL; FAIL otherwise.
    verdict_a_normalized = "PASS" if verdict_a in ("PASS", "PASS-DIAGNOSTIC") else verdict_a  # (local)
    if verdict_a_normalized == "PASS" and verdict_b == "PASS":
        composite_verdict = "PASS"
    elif "FAIL" in (verdict_a_normalized, verdict_b):
        composite_verdict = "FAIL"
    else:
        composite_verdict = "INFO"

    print("=" * 78)
    print("COMPOSITE VERDICT")
    print("=" * 78)
    print(f"  sub-gate (a) [max_pair_ratio invariance] = {verdict_a}")
    print(f"  sub-gate (b) [cluster-span identity]     = {verdict_b}")
    print(f"  COMPOSITE                                = {composite_verdict}")
    print()

    # -------------------------------------------------------------
    # Step 5: Save .npz artifact (per plan §13)
    # -------------------------------------------------------------
    OUT_NPZ = SCRIPT_DIR / "s87_w8_w4_2_re_run_under_a_4.npz"

    # Convert pair-ratio dicts to flat arrays for npz portability.
    A5_pair_keys = ["|".join(k) for k in pair_ratios_A5.keys()]               # (local)
    A5_pair_vals = np.array(list(pair_ratios_A5.values()), dtype=np.float64)  # (local)
    A4_pair_keys = ["|".join(k) for k in pair_ratios_A4.keys()]               # (local)
    A4_pair_vals = np.array(list(pair_ratios_A4.values()), dtype=np.float64)  # (local)

    np.savez(
        OUT_NPZ,
        # max_pair_ratio sub-gate
        max_pair_ratio_A4=max_pair_ratio_A4,
        max_pair_ratio_A5=W4_2_MAX_PAIR_RATIO_A5,
        max_pair_ratio_A5_recomputed=max_pair_ratio_A5_recomputed,
        delta_pr=delta_pr,
        atlas_extremal_pair=np.array(list(max_pair_A4)),
        atlas_extremal_pair_A5=np.array(list(max_pair_A5)),
        was_cutoff_sqrt_extremal_in_A5=was_cutoff_sqrt_extremal_in_A5,
        A4_columns=np.array(list(A_4_COLUMNS)),
        A5_columns=np.array(list(A_5_COLUMNS)),
        A4_pair_keys=np.array(A4_pair_keys),
        A4_pair_ratios=A4_pair_vals,
        A5_pair_keys=np.array(A5_pair_keys),
        A5_pair_ratios=A5_pair_vals,
        pole_R_zeta=W4_2_POLE_R_A5["zeta"],
        pole_R_Zubarev=W4_2_POLE_R_A5["Zubarev"],
        pole_R_SDW=W4_2_POLE_R_A5["SDW"],
        pole_R_cutoff_sqrt=W4_2_POLE_R_A5["cutoff_sqrt"],
        pole_R_anomaly=W4_2_POLE_R_A5["anomaly"],
        # cluster-span sub-gate
        L_max_cluster_span=L_MAX_CLUSTER_SPAN,
        b_pow_span_2=b_pow_span_2,
        b_pow_span_3=b_pow_span_3,
        ratio=ratio_2_3,
        canonical_metric=canonical_metric,
        normalized_metric=normalized_metric,
        W0_3_canonical_anchor=W0_3_CANONICAL_DEVIATION,
        # span identifiers (for the npz consumer)
        span_2=2,
        span_3=3,
        # verdicts
        verdict_a=verdict_a,
        verdict_b=verdict_b,
        composite_verdict=composite_verdict,
        PASS_TOL_A=PASS_TOL_A,
        PASS_TOL_B=PASS_TOL_B,
    )
    print(f"wrote {OUT_NPZ}")
    print()

    # -------------------------------------------------------------
    # Step 6: Plot — pair-ratios A_5 vs A_4 side-by-side
    # -------------------------------------------------------------
    OUT_PNG = SCRIPT_DIR / "s87_w8_w4_2_re_run_under_a_4.png"
    fig, ax = plt.subplots(2, 1, figsize=(11, 8.5))

    # Top panel: A_5 vs A_4 pair ratios (bar)
    A5_pairs_sorted = sorted(pair_ratios_A5.items(), key=lambda kv: -kv[1])    # (local)
    A4_pairs_sorted = sorted(pair_ratios_A4.items(), key=lambda kv: -kv[1])    # (local)

    A5_labels = [f"{p[0]} ↔ {p[1]}" for p, _ in A5_pairs_sorted]               # (local)
    A5_vals = [v for _, v in A5_pairs_sorted]                                  # (local)
    A4_labels = [f"{p[0]} ↔ {p[1]}" for p, _ in A4_pairs_sorted]               # (local)
    A4_vals = [v for _, v in A4_pairs_sorted]                                  # (local)

    ax[0].barh(range(len(A5_labels)), A5_vals, color='#1f77b4', alpha=0.65, label=f'A_5 (5 cols, 10 pairs)')
    ax[0].set_yticks(range(len(A5_labels)))
    ax[0].set_yticklabels(A5_labels, fontsize=8)
    ax[0].axvline(W4_2_MAX_PAIR_RATIO_A5, color='red', linestyle='--', linewidth=1.0,
                  label=f'W4-2 anchor max = {W4_2_MAX_PAIR_RATIO_A5:.4e}')
    ax[0].set_xlabel('pair-ratio = |pole_i - pole_j| / max(|pole_i|, |pole_j|)')
    ax[0].set_title(f'A_5 atlas pair-ratios (max at {W4_2_MAX_PAIR_PAIR_A5})')
    ax[0].legend(loc='lower right', fontsize=8)
    ax[0].invert_yaxis()
    ax[0].grid(True, axis='x', alpha=0.3)

    ax[1].barh(range(len(A4_labels)), A4_vals, color='#2ca02c', alpha=0.65, label=f'A_4 (4 cols, 6 pairs)')
    ax[1].set_yticks(range(len(A4_labels)))
    ax[1].set_yticklabels(A4_labels, fontsize=8)
    ax[1].axvline(max_pair_ratio_A4, color='red', linestyle='--', linewidth=1.0,
                  label=f'A_4 max = {max_pair_ratio_A4:.4e} at {max_pair_A4}')
    ax[1].set_xlabel('pair-ratio = |pole_i - pole_j| / max(|pole_i|, |pole_j|)')
    ax[1].set_title(f'A_4 atlas pair-ratios (cutoff_sqrt removed); '
                    f'cutoff_sqrt-extremal-in-A_5 = {was_cutoff_sqrt_extremal_in_A5}')
    ax[1].legend(loc='lower right', fontsize=8)
    ax[1].invert_yaxis()
    ax[1].grid(True, axis='x', alpha=0.3)

    fig.suptitle(f'{GATE_ID}: max_pair_ratio invariance + cluster-span identity '
                 f'(canonical_metric = {canonical_metric:.2e}, '
                 f'PASS_TOL_B = {PASS_TOL_B:.0e})', fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)
    print(f"wrote {OUT_PNG}")
    print()

    # -------------------------------------------------------------
    # Step 7: Compute final SHAs and append S87+ schema-v2 verdict line
    # -------------------------------------------------------------
    content_sha = sha256_of(OUT_NPZ)
    print(f"content_sha256 = {content_sha[:16]}... ({content_sha})")
    print(f"audit_sha256   = {audit_sha[:16]}... ({audit_sha})")
    print()

    # Verdict 4-tuple
    value_str = f"max_pair_ratio_A4={max_pair_ratio_A4:.6e};canonical_metric={canonical_metric:.3e}"  # (local)
    L_max_tag = f"{L_MAX_CLUSTER_SPAN}_b/{L_MAX_MAX_PAIR_RATIO}_a"                                    # (local)
    print(f"4-tuple: (value=\"{value_str}\", scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_max_tag})")
    print()

    # S81+ canonical verdict line
    primary_line = (
        f"{GATE_ID}: {composite_verdict} -- "
        f"value='{value_str}' "
        f"scheme={SCHEME} "
        f"convention={CONVENTION} "
        f"L_max={L_max_tag} "
        f"audit_sha256={audit_sha} "
        f"content_sha256={content_sha} "
        f"schema_version=S87+"
    )
    # W9a-99 dual-SHA companion row
    companion_line = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)"
    )
    # S87+ schema-v2 3-tuple annotation
    # sign_verdict   = PASS  (substitution-chain Step 4 predicts max_pair_ratio_A_4 ≤
    #                          max_pair_ratio_A_5; computed direction matches.)
    # magnitude_verdict per sub-gate composite:
    #   - PASS if delta_pr satisfies bit-identity tolerance AND canonical_metric < PASS_TOL_B
    #   - INFO if precision-floor band crossed
    #   - FAIL otherwise
    # regime_verdict = VALID  (cluster-span operates within its declared L_max=12 regime;
    #                          max_pair_ratio operates within its declared 4-column atlas.)
    sign_verdict = "PASS" if direction_ok else "FAIL"        # (local)
    magnitude_verdict = composite_verdict                    # (local) collapse-rule alias
    regime_verdict = "VALID"                                 # (local)
    annotation_line = (
        f"# sign_verdict={sign_verdict} "
        f"magnitude_verdict={magnitude_verdict} "
        f"regime_verdict={regime_verdict} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)"
    )

    VERDICT_TXT = SCRIPT_DIR / "s87_gate_verdicts.txt"
    with open(VERDICT_TXT, 'a', encoding='utf-8') as f:
        f.write("\n")
        f.write(primary_line + "\n")
        f.write(companion_line + "\n")
        f.write(annotation_line + "\n")

    print("=" * 78)
    print("VERDICT LINES (appended to computations/session-87/s87_gate_verdicts.txt)")
    print("=" * 78)
    print(primary_line)
    print(companion_line)
    print(annotation_line)
    print("=" * 78)

    elapsed = time.time() - t0                                # (local)
    print(f"\nelapsed: {elapsed:.2f} s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
