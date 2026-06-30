#!/usr/bin/env python3
"""
S83 W3-G38 — K-MATCHING-5-CONVENTIONS
=====================================

Gate: S83-K-MATCHING-5-CONVENTIONS ([VERIFY])

Pre-registered threshold (session-83-results-workingpaper.md L4349):
  PASS: min_R |A_s_R - A_s_Planck| / A_s_Planck < 0.05  (within factor-1.05)
  INFO: 0.05 <= min_R |...| < 0.20
  FAIL: otherwise (>= 0.20)

4-tuple slot: (min_rel_err=?, scheme=Landau-V.1-R1-R5,
               convention=A_s_Planck=2.10e-9, L_max=N/A)

Classification: PHONONIC (A_s = scalar power spectrum amplitude sourced by
GGE occupation of BCS quasiparticles = substrate phonon excitations; K is
the unique dial controlling the BCS occupation factor).

CONTEXT
-------
Landau S82 synthesis §V.1 (sessions/archive/session-82/session-82-landau-synthesis.md
L240-L245) enumerates 5 reading conventions (R1-R5) for extracting the
dimensionless corridor coordinate K from the 3/3/2 B1/B2/B3 band multiplicity
structure (S43):

  R1 (band-summed B3, vacuum-dominated reading):     K_R1 = 2.185
  R2 (3/3/2-weighted geometric-mean):                K_R2 = 2.049
  R3 (3/3/2 primary, S82 W2-4 canonical):            K_R3 = 2.035
  R4 (naive n_pairs/N_modes = 59.8/8, Fock-counting):K_R4 = 15.95
  R5 (energy-weighted B2, Bogoliubov-primary):       K_R5 = 1.922

The dynamics layer (S82 §V.7 carry-forward; proven at W1-2) provides the
linear response:

  A_s(K) = A_s_{W1-2,TD} * K           with  A_s_{W1-2,TD} = 3.299e-9

The 5 readings differ only in the convention layer (band-weighting to
extract K); the K -> A_s map itself is Mukhanov-Sasaki + BCS-squeezing
and is convention-invariant.

SUBSTITUTION CHAIN [VERIFY]
---------------------------
Step 1 (definitions):
  A_s_Planck = 2.10e-9           [canonical_constants.A_s_CMB, Planck 2018]
  A_s_W1_2   = 3.299e-9          [S82 W1-2 TD-branch Mukhanov-Sasaki baseline]
  A_s(K_R)   = A_s_W1_2 * K_R    [S82 §V.7 linear-response theorem]
  K_R        = {2.185, 2.049, 2.035, 15.95, 1.922}  [R1..R5 per Landau V.1]

Step 2 (substitution):
  A_s_R = A_s_W1_2 * K_R   for each R in {R1,R2,R3,R4,R5}
  rel_err_R = |A_s_R - A_s_Planck| / A_s_Planck

Step 3 (simplification):
  rel_err_R = |(A_s_W1_2 * K_R - A_s_Planck)| / A_s_Planck
            = |K_R * (A_s_W1_2 / A_s_Planck) - 1|
            = |K_R / K_match - 1|   where K_match = A_s_Planck / A_s_W1_2

  K_match = 2.10e-9 / 3.299e-9 = 0.63656 (Python-verified offline)

Step 4 (direction):
  Since all K_R > 0: A_s_R > 0.
  min(K_R) = K_R5 = 1.922 > K_match = 0.637 ==> EVERY A_s_R > A_s_Planck
  (amplification-only regime under the 5 conventions).
  The minimum relative error is at the SMALLEST K_R:
     min_rel_err = K_R5 / K_match - 1 = 1.922 / 0.63656 - 1 = 2.0195
  2.020 >> 0.20  ==> pre-registered FAIL expected.

Step 5 (Python verification — this script):
  Compute rel_err_R for each R, find argmin, compare against thresholds,
  emit the 4-tuple verdict + SHA-256 closure.

  Offline-verified expectation (from direct calculation):
    A_s_R1 = 3.299e-9 * 2.185  = 7.208e-9   rel_err = 2.433
    A_s_R2 = 3.299e-9 * 2.049  = 6.760e-9   rel_err = 2.219
    A_s_R3 = 3.299e-9 * 2.035  = 6.714e-9   rel_err = 2.197
    A_s_R4 = 3.299e-9 * 15.95  = 5.262e-8   rel_err = 24.06
    A_s_R5 = 3.299e-9 * 1.922  = 6.341e-9   rel_err = 2.020
  argmin = R5 with rel_err = 2.020 ==> FAIL (>> 0.20)

Inputs (SHA-256 pinned at runtime):
  - canonical_constants.py        (closure hash)
  - sessions/archive/session-82/session-82-landau-synthesis.md (K_R values)
  - sessions/archive/session-82/session-82-results-workingpaper.md (A_s_W1_2)
  - this script                   (self-pin)

Output 4-tuple:
  (min_rel_err=<v>, scheme=Landau-V.1-R1-R5,
   convention=A_s_Planck=2.10e-9, L_max=N/A)

STRUCTURAL CONSEQUENCE
----------------------
This gate tests ONE precise claim: does any of the 5 convention layers allow
an exact Planck match to factor-1.05? The pre-verified answer is NO, which
is the symmetric dual of the S82 V.1 finding "K_match = 0.637 < 1 under every
convention". Here we invert the question (given K_R from each convention, do
any land A_s on Planck?) and confirm the structural wall from the other side:
the 5-convention cluster is OVER-shooting, not under-shooting. The floor
K >= 1 (W2-4 positivity wall) combined with A_s_W1_2 > A_s_Planck places
Planck below the convention cluster — no convention choice rescues an exact
match. The gate's PASS-EXCLUSION status is thus a convention-independent
structural statement about the linear-response dial K, not a
parameter-tuning failure.
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403
from canonical_constants import A_s_CMB

# ---------------------------------------------------------------------------
# Section 2 — Standard imports (CPU thread cap)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import hashlib
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent

SESSION = "S83"                                          # (local)
GATE_ID = "S83-K-MATCHING-5-CONVENTIONS"                 # (local)
SCHEME = "Landau-V.1-R1-R5"                              # (local)
CONVENTION = "A_s_Planck=2.10e-9"                        # (local)
L_MAX_TAG = "N/A"                                        # (local) not spectral

OUT_NPZ = SCRIPT_DIR / "s83_w3_g38_k_matching_5_conventions.npz"
OUT_PNG = SCRIPT_DIR / "s83_w3_g38_k_matching_5_conventions.png"
VERDICT_TXT = SCRIPT_DIR / "s83_gate_verdicts.txt"

LANDAU_SYNTH = PROJECT_ROOT / "sessions/archive/session-82/session-82-landau-synthesis.md"  # (local)
S82_WP = PROJECT_ROOT / "sessions/archive/session-82/session-82-results-workingpaper.md"    # (local)

INPUT_FILES = [
    SCRIPT_DIR / "canonical_constants.py",
    LANDAU_SYNTH,
    S82_WP,
    SCRIPT_DIR / "s83_w3_g38_k_matching_5_conventions.py",
]

# Pre-registered gate thresholds (plan L4349)
PASS_THRESHOLD = 0.05                                    # (local) factor-1.05 band
INFO_THRESHOLD = 0.20                                    # (local) factor-1.20 upper

# Pre-registered inputs (pinned at plan-time, Landau S82 §V.1 L242)
A_s_PLANCK = A_s_CMB                                     # 2.10e-9, canonical
A_s_W1_2_TD = 3.299e-9                                   # (local) S82 W1-2 TD baseline

# R1..R5 K-values from Landau S82 §V.1 L242, Python-verified there
K_CONVENTIONS = {                                        # (local) Landau V.1 table
    'R1': 2.185,   # band-summed B3 (vacuum-dominated)
    'R2': 2.049,   # 3/3/2-weighted geometric-mean
    'R3': 2.035,   # 3/3/2 primary (S82 W2-4 canonical)
    'R4': 15.95,   # naive n_pairs/N_modes = 59.8/8 (Fock-counting)
    'R5': 1.922,   # energy-weighted B2 (Bogoliubov-primary)
}
R_LABELS = {                                             # (local)
    'R1': 'R1: band-summed B3',
    'R2': 'R2: 3/3/2 geo-mean',
    'R3': 'R3: 3/3/2 primary',
    'R4': 'R4: n_pair/N_mode',
    'R5': 'R5: energy-wtd B2',
}


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input pinning
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        except ValueError:
            rel = str(p)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins):
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()          # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — Convention evaluator
# ---------------------------------------------------------------------------

def compute_A_s_from_convention(R_label):
    """Linear-response map A_s(K_R) = A_s_W1_2 * K_R (S82 §V.7)."""
    if R_label not in K_CONVENTIONS:
        raise ValueError(f"Unknown convention: {R_label}")
    K_R = K_CONVENTIONS[R_label]                         # (local)
    A_s_R = A_s_W1_2_TD * K_R                            # (local)
    return A_s_R


# ---------------------------------------------------------------------------
# Section 6 — Main evaluation
# ---------------------------------------------------------------------------

def main():
    pins = log_input_pins(INPUT_FILES)
    closure_sha = closure_hash(pins)
    print()
    print(f"=== {GATE_ID} — pre-registration ===")
    print(f"  A_s_Planck    = {A_s_PLANCK:.4e}")
    print(f"  A_s_W1_2_TD   = {A_s_W1_2_TD:.4e}")
    print(f"  K_match_need  = {A_s_PLANCK / A_s_W1_2_TD:.4f}  "
          "(dial needed to land exactly on Planck)")
    print(f"  PASS band     : rel_err < {PASS_THRESHOLD}")
    print(f"  INFO band     : {PASS_THRESHOLD} <= rel_err < {INFO_THRESHOLD}")
    print(f"  FAIL band     : rel_err >= {INFO_THRESHOLD}")
    print()

    conventions = list(K_CONVENTIONS.keys())             # (local)
    A_s_vals = {c: compute_A_s_from_convention(c) for c in conventions}  # (local)
    rels = {c: abs(A_s_vals[c] - A_s_PLANCK) / A_s_PLANCK
            for c in conventions}                        # (local)
    log10_ratio = {c: np.log10(A_s_vals[c] / A_s_PLANCK)
                   for c in conventions}                 # (local)

    min_rel = min(rels.values())                         # (local)
    best_c = min(rels, key=rels.get)                     # (local)
    max_rel = max(rels.values())                         # (local)
    worst_c = max(rels, key=rels.get)                    # (local)

    # Substitution-chain verification (machine-epsilon cross-check)
    for c in conventions:
        expected = abs(K_CONVENTIONS[c] / (A_s_PLANCK / A_s_W1_2_TD) - 1.0)  # (local)
        assert abs(rels[c] - expected) < 1e-12, \
            f"Substitution-chain cross-check failed at {c}"
    print("  substitution-chain cross-check: OK (machine epsilon)")
    print()

    print("=== 5-convention A_s evaluation ===")
    print(f"  {'Conv':<5} {'K_R':>10} {'A_s_R':>14} "
          f"{'rel_err':>12} {'log10(A_s_R/P)':>16}")
    print("  " + "-" * 60)
    for c in conventions:
        print(f"  {c:<5} {K_CONVENTIONS[c]:>10.4f} {A_s_vals[c]:>14.4e} "
              f"{rels[c]:>12.4f} {log10_ratio[c]:>16.4f}")
    print()
    print(f"  Best (min rel_err): {best_c} -> {min_rel:.4f} "
          f"(K_R = {K_CONVENTIONS[best_c]:.3f})")
    print(f"  Worst (max rel_err): {worst_c} -> {max_rel:.4f} "
          f"(K_R = {K_CONVENTIONS[worst_c]:.3f})")
    print()

    # Verdict
    if min_rel < PASS_THRESHOLD:
        verdict = "PASS"                                  # (local)
    elif min_rel < INFO_THRESHOLD:
        verdict = "INFO"                                  # (local)
    else:
        verdict = "FAIL"                                  # (local)
    print(f"  Verdict: {verdict}")
    print()

    # --- 4-tuple output ---
    value_str = (f"min_rel_err={min_rel:.4f}_at={best_c}_"
                 f"K={K_CONVENTIONS[best_c]:.3f}_"
                 f"A_s_min={A_s_vals[best_c]:.4e}_"
                 f"A_s_max={A_s_vals[worst_c]:.4e}_"
                 f"max_rel_err={max_rel:.4f}_at={worst_c}_"
                 f"all_amplify={int(all(A_s_vals[c] > A_s_PLANCK for c in conventions))}_"
                 f"K_match_need={A_s_PLANCK/A_s_W1_2_TD:.4f}")  # (local)
    tuple_line = (f"({value_str} scheme={SCHEME} convention={CONVENTION} "
                  f"L_max={L_MAX_TAG})")                  # (local)
    print(f"4-tuple: {tuple_line}")
    print()

    # --- Save NPZ ---
    K_arr = np.array([K_CONVENTIONS[c] for c in conventions], dtype=np.float64)
    A_s_arr = np.array([A_s_vals[c] for c in conventions], dtype=np.float64)
    rel_arr = np.array([rels[c] for c in conventions], dtype=np.float64)
    log10_arr = np.array([log10_ratio[c] for c in conventions], dtype=np.float64)

    np.savez(OUT_NPZ,
             conventions=np.array(conventions),
             K_values=K_arr,
             A_s_values=A_s_arr,
             rel_errs=rel_arr,
             log10_ratios=log10_arr,
             A_s_Planck=A_s_PLANCK,
             A_s_W1_2_TD=A_s_W1_2_TD,
             K_match_needed=A_s_PLANCK / A_s_W1_2_TD,
             min_rel_err=min_rel,
             best_convention=best_c,
             max_rel_err=max_rel,
             worst_convention=worst_c,
             verdict=verdict,
             closure_sha=closure_sha,
             pass_threshold=PASS_THRESHOLD,
             info_threshold=INFO_THRESHOLD)
    print(f"  Saved NPZ: {OUT_NPZ.name}")

    # --- Plot ---
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

    x = np.arange(len(conventions))                      # (local)
    colors = ['#1f77b4', '#2ca02c', '#ff7f0e', '#d62728', '#9467bd']  # (local)

    # Panel 1: A_s per convention vs Planck line
    ax1.bar(x, A_s_arr, color=colors, alpha=0.75, edgecolor='black')
    ax1.axhline(A_s_PLANCK, color='k', ls='--', lw=1.5,
                label=f'Planck: {A_s_PLANCK:.2e}')
    ax1.axhline(A_s_PLANCK * 1.05, color='k', ls=':', lw=1,
                label='±5% band (PASS)')
    ax1.axhline(A_s_PLANCK * 0.95, color='k', ls=':', lw=1)
    ax1.axhline(A_s_PLANCK * 1.20, color='grey', ls=':', lw=1,
                label='±20% band (INFO/FAIL)')
    ax1.axhline(A_s_PLANCK * 0.80, color='grey', ls=':', lw=1)
    ax1.set_yscale('log')
    ax1.set_xticks(x)
    ax1.set_xticklabels(conventions)
    ax1.set_ylabel('A_s(K_R)')
    ax1.set_title('A_s under Landau V.1 5 conventions vs Planck')
    ax1.legend(loc='upper left', fontsize=9)
    ax1.grid(True, alpha=0.3, which='both')
    for i, c in enumerate(conventions):
        ax1.annotate(f'{A_s_vals[c]:.2e}', (x[i], A_s_vals[c]),
                     textcoords='offset points', xytext=(0, 5),
                     ha='center', fontsize=8)

    # Panel 2: relative error per convention
    ax2.bar(x, rel_arr, color=colors, alpha=0.75, edgecolor='black')
    ax2.axhline(PASS_THRESHOLD, color='g', ls='--', lw=1.5,
                label=f'PASS: rel_err < {PASS_THRESHOLD}')
    ax2.axhline(INFO_THRESHOLD, color='orange', ls='--', lw=1.5,
                label=f'INFO: rel_err < {INFO_THRESHOLD}')
    ax2.set_yscale('log')
    ax2.set_xticks(x)
    ax2.set_xticklabels(conventions)
    ax2.set_ylabel('|A_s_R - A_s_Planck| / A_s_Planck')
    ax2.set_title(f'Relative error: min={min_rel:.3f} at {best_c} '
                  f'[verdict: {verdict}]')
    ax2.legend(loc='upper left', fontsize=9)
    ax2.grid(True, alpha=0.3, which='both')
    for i, c in enumerate(conventions):
        ax2.annotate(f'{rels[c]:.3f}', (x[i], rel_arr[i]),
                     textcoords='offset points', xytext=(0, 5),
                     ha='center', fontsize=8)

    plt.suptitle(f'{GATE_ID} — PHONONIC | verdict: {verdict} | '
                 f'K_match_need = {A_s_PLANCK/A_s_W1_2_TD:.4f} < min(K_R)',
                 fontsize=11)
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=130)
    plt.close()
    print(f"  Saved PNG: {OUT_PNG.name}")

    # --- Verdict line (append) ---
    verdict_line = (f"{GATE_ID}: {verdict} -- value={value_str} "
                    f"scheme={SCHEME} convention={CONVENTION} "
                    f"L_max={L_MAX_TAG} sha256={closure_sha}\n")  # (local)
    print()
    print("=== Appending verdict line ===")
    print(f"  {verdict_line.strip()}")
    with open(VERDICT_TXT, 'a', encoding='utf-8') as f:
        f.write(verdict_line)
    print(f"  appended to {VERDICT_TXT.name}")

    print()
    print("=== DONE ===")
    return 0


if __name__ == '__main__':
    sys.exit(main())
