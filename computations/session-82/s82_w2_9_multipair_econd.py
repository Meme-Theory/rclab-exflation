#!/usr/bin/env python3
"""
S82 W2-9: MULTIPAIR-ECOND -- BCS condensation energy E_cond(N_pair) for N=1,2,3
================================================================================

Gate: S82-MULTIPAIR-ECOND  (Trigger [VERIFY])
Classification: PHONONIC
Plan anchor: sessions/session-plan/session-80-plan.md lines L1491-L1520
Shell: sessions/archive/session-82/session-82-results-workingpaper.md Section V.I

Substrate framing (PHONONIC):
  E_cond is the BCS ground-state binding of N Cooper pairs in the 8-mode Fock
  space at the van Hove fold (tau = 0.190).  Each Cooper pair is a fiber-bound
  two-phonon condensate (Kramers-paired pair-creation excitation of the fiber
  eigenvalue spectrum of D_K).  The N-dependence probes whether multi-pair
  binding is additive (ratio ~ N), sub-additive (ratio < N), super-additive
  (ratio > N), or saturating.  Pre-registered hypothesis: ratio N=2/N=1 >= 10
  is required for N_pair=2 to be a distinct A_s-closure path via E_excite/E_gs
  = 0.258 accessibility (from P3-A W1-D).

Pre-registered thresholds (S80 L1498-L1504):
  PASS : E_cond(N=2) / E_cond(N=1) >= 10
  INFO : ratio in [3, 10]
  FAIL : ratio < 3

Output 4-tuple:
  (value=<ratio>, scheme=BCS-ED, convention=SORTED-NORMAL-FILL, L_max=8-mode)

Substitution chain (MANDATORY for [VERIFY]):
  Step 1 [definition]:
    E_gs^{BCS}(N) = ground-state energy of the N-pair BCS Hamiltonian in the
      canonical (fixed-N) Fock subspace via exact diagonalization (S52 method)
    E_normal(N) = reference energy of N Kramers pairs filling the N lowest-
      energy modes WITHOUT pairing interaction, using the canonical
      single-particle energies sorted ascending:
          E_normal(N) = 2 * sum_{k=0..N-1} E_sp_sorted[k]
      (factor 2 = Kramers pair of spinless fermions per mode)
    E_cond(N) = E_gs^{BCS}(N) - E_normal(N)
      (Bardeen 1957 / S43 convention; nuclear-structure Paper 03)
    ratio = E_cond(N=2) / E_cond(N=1)   (both negative; ratio positive)

  Step 2 [substitution]:
    E_sp_sorted (at tau_fold = 0.190, M_KK units):
      [ E_B1        = 0.81914,
        E_B2        = 0.84527  (x4),
        E_B3        = 0.97822  (x3) ]
    E_gs(N=1) = 1.4398416902  (S52 ED, 8-state C(8,1) subspace)
    E_gs(N=2) = 3.0111200211  (S52 ED, 28-state C(8,2) subspace)
    E_gs(N=3) = 4.6835927814  (S52 ED, 56-state C(8,3) subspace)
    E_normal(1) = 2 * 0.81914 = 1.63828
    E_normal(2) = 2 * (0.81914 + 0.84527) = 3.32882
    E_normal(3) = 2 * (0.81914 + 2*0.84527) = 5.01936

  Step 3 [simplification]:
    E_cond(1) = 1.43984 - 1.63828 = -0.19844 M_KK
    E_cond(2) = 3.01112 - 3.32882 = -0.31770 M_KK
    E_cond(3) = 4.68359 - 5.01936 = -0.33576 M_KK
    ratio_21 = E_cond(2)/E_cond(1) = -0.31770/-0.19844 = 1.601
    ratio_31 = E_cond(3)/E_cond(1) = -0.33576/-0.19844 = 1.692

  Step 4 [direction]:
    All E_cond < 0 (binding, required for Cooper pairing).
    The ratio is POSITIVE and below 2 (sub-additive binding) for both N=2 and
    N=3.  Direction conclusion: multi-pair binding is SATURATING in the 8-mode
    window -- the second and third pair add progressively LESS binding than
    the first (Pauli blocking of the B1 fermi level beyond N=1).
    Threshold readout: ratio_21 = 1.601 < 3 => FAIL.

Inputs (SHA-256 pinned):
  - canonical_constants.py
  - computations/session-48/s48_hfb_selfconsist.npz  (V_bare 8x8, E_sp, S48 HFB setup)

Author: landau-condensed-matter-theorist (S82 W2-9)
"""
from __future__ import annotations

# Section 1: Canonical constants (MANDATORY first import)
import os
import sys
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

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
from canonical_constants import (                                # noqa: F401
    tau_fold,
    E_B1, E_B2_mean, E_B3_mean,
    M_KK, M_KK_gravity,
    E_cond as E_cond_canonical_N1,
    E_cond_ED_8mode,
)

# Section 2: Standard imports
import hashlib
import json
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Section 3: Paths and pre-registration
PROJECT_ROOT = Path(_HERE).parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
ARCHIVE_DIR = PROJECT_ROOT / "computations" / "_shared"

SESSION = "S82"                                                   # (local)
GATE_ID = "S82-MULTIPAIR-ECOND"                                   # (local)
SCHEME = "BCS-ED"                                                 # (local)
CONVENTION = "SORTED-NORMAL-FILL"                                 # (local)
L_MAX_TAG = "8-mode"                                              # (local) N_modes=4B2+1B1+3B3
N_MODES = 8                                                       # (local)
N_PAIR_VALUES = [1, 2, 3]                                         # (local)

# Pre-registered thresholds (plan L1502-L1504)
PASS_THRESHOLD = 10.0                                             # (local)
INFO_LOWER = 3.0                                                  # (local)

# Output destinations
OUT_NPZ = resolve_output(82, 's82_w2_9_multipair_econd.npz')
OUT_PNG = resolve_output(82, 's82_w2_9_multipair_econd.png')
VERDICT_TXT = resolve_output(82, 's82_gate_verdicts.txt')

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    ARCHIVE_DIR / "s48_hfb_selfconsist.npz",
]


# Section 4: SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                          # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}                                                     # (local)
    for p in inputs:
        sha = sha256_of(p)                                        # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/") # (local)
        print(f"  {rel}: {sha}")
        pins[rel] = sha
    return pins


def closure_hash(pins):
    items = sorted(pins.items())                                  # (local)
    h = hashlib.sha256()                                          # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


# Section 5: Fock-space exact diagonalization (S52 method, reproduced)
def build_fock_states(n_modes: int, n_pair: int) -> np.ndarray:
    """All bit-strings of length n_modes with exactly n_pair ones."""
    states = []                                                   # (local)
    for s in range(1 << n_modes):
        if bin(s).count('1') == n_pair:
            states.append(s)
    return np.array(states, dtype=np.int64)


def build_canonical_hamiltonian(E_sp: np.ndarray, V: np.ndarray,
                                n_pair: int) -> tuple:
    """BCS Hamiltonian on fixed-N canonical subspace.

    H = sum_k 2*eps_k * n_k - sum_{kk'} V_{kk'} P^+_k P_{k'}
    where P^+_k creates a Kramers pair at mode k (one pair = two fermions).
    """
    n_modes = len(E_sp)                                           # (local)
    states = build_fock_states(n_modes, n_pair)
    dim = len(states)                                             # (local)
    state_idx = {int(s): i for i, s in enumerate(states)}
    H = np.zeros((dim, dim), dtype=np.float64)                    # (local)

    for i, state_i in enumerate(states):
        # Diagonal (kinetic term, 2*eps per occupied pair)
        for k in range(n_modes):
            if state_i & (1 << k):
                H[i, i] += 2.0 * E_sp[k]

        # Off-diagonal pair scattering V_{kk'} P^+_k P_{k'}
        for k in range(n_modes):
            for kp in range(n_modes):
                if V[k, kp] == 0.0:
                    continue
                if (state_i & (1 << kp)) and not (state_i & (1 << k)):
                    new_state = (state_i ^ (1 << kp)) | (1 << k)  # (local)
                    j = state_idx.get(int(new_state))
                    if j is not None:
                        H[j, i] -= V[k, kp]

    return H, states


def compute():
    # --- Load canonical Fock-space operators from S48 archive ---
    d48 = np.load(ARCHIVE_DIR / "s48_hfb_selfconsist.npz", allow_pickle=True)
    V_bare = d48['V_bare'].astype(np.float64).copy()              # (local) 8x8
    E_sp_raw = d48['E_sp'].astype(np.float64).copy()              # (local)
    labels = [str(x) for x in d48['labels']]                      # (local)

    # --- Consistency checks against canonical_constants ---
    # E_sp at mode indices 0-3 = B2, index 4 = B1, indices 5-7 = B3
    b2_match = np.allclose(E_sp_raw[0:4], E_B2_mean)               # (local)
    b1_match = np.isclose(E_sp_raw[4], E_B1)                       # (local)
    b3_match = np.allclose(E_sp_raw[5:8], E_B3_mean)               # (local)
    v_sym = float(np.max(np.abs(V_bare - V_bare.T)))               # (local)

    print("--- Input consistency ---")
    print(f"  E_sp bare: {E_sp_raw}")
    print(f"  Labels: {labels}")
    print(f"  B2[0..3] == E_B2_mean (canonical): {b2_match}")
    print(f"  B1 == E_B1 (canonical): {b1_match}")
    print(f"  B3[5..7] == E_B3_mean (canonical): {b3_match}")
    print(f"  V_bare symmetry |V - V^T|_max = {v_sym:.3e}")
    print(f"  V_bare Frobenius norm = {np.linalg.norm(V_bare):.6f}")
    assert b2_match and b1_match and b3_match, "E_sp drift from canonical"
    assert v_sym < 1e-15, "V_bare not symmetric"

    # --- Sorted single-particle energies (for consistent normal-state reference) ---
    E_sp_sorted = np.sort(E_sp_raw)                                # (local)
    print(f"  E_sp_sorted (ascending): {E_sp_sorted}")
    print()

    # --- Exact diagonalization at each N_pair ---
    results = {}                                                   # (local)
    print("--- Exact diagonalization (BCS fixed-N subspace) ---")
    for n_pair in N_PAIR_VALUES:
        H, states = build_canonical_hamiltonian(E_sp_raw, V_bare, n_pair)
        assert np.allclose(H, H.T), f"H not symmetric at N_pair={n_pair}"
        # Small matrices (<= 56 for N=3) -- numpy.linalg.eigh is fine
        evals = np.linalg.eigh(H)[0]                                # (local)
        E_gs = float(evals[0])                                      # (local)
        E_normal = float(2.0 * np.sum(E_sp_sorted[:n_pair]))        # (local)
        E_cond_N = E_gs - E_normal                                  # (local)
        results[n_pair] = {
            "E_gs": E_gs,
            "E_normal": E_normal,
            "E_cond": E_cond_N,
            "dim": len(states),
            "gap_E1_minus_E0": float(evals[1] - evals[0]),
        }
        print(f"  N_pair={n_pair}: dim={len(states):3d}  "
              f"E_gs={E_gs:.10f}  E_normal={E_normal:.10f}  "
              f"E_cond={E_cond_N:+.10f} M_KK")
    print()

    # --- Ratios (with sign; both E_cond negative => ratio positive) ---
    ec1 = results[1]["E_cond"]                                      # (local)
    ec2 = results[2]["E_cond"]                                      # (local)
    ec3 = results[3]["E_cond"]                                      # (local)
    ratio_21 = ec2 / ec1                                            # (local)
    ratio_31 = ec3 / ec1                                            # (local)
    ratio_32 = ec3 / ec2                                            # (local)

    print("--- Ratios ---")
    print(f"  E_cond(N=2)/E_cond(N=1) = {ratio_21:.6f}  (PASS threshold >= 10.0)")
    print(f"  E_cond(N=3)/E_cond(N=1) = {ratio_31:.6f}")
    print(f"  E_cond(N=3)/E_cond(N=2) = {ratio_32:.6f}")

    # --- Cross-check vs S52 stored values (method parity) ---
    # S52 reports E_gs(N=1)=1.4398416902, E_gs(N=2)=3.0111200211,
    #             E_gs(N=3)=4.6835927814 to 10 digits (see s52_hfb_full_output.txt).
    s52_E_gs = {1: 1.4398416902, 2: 3.0111200211, 3: 4.6835927814}  # (local)
    print()
    print("--- S52 parity cross-check ---")
    for n_pair, ref in s52_E_gs.items():
        diff = abs(results[n_pair]["E_gs"] - ref)                   # (local)
        print(f"  N_pair={n_pair}: |E_gs - S52| = {diff:.2e}")
        assert diff < 5e-9, f"Parity drift at N={n_pair}: {diff:.2e}"

    # --- Cross-check vs canonical E_cond constant (N_pair=1 only) ---
    # canonical E_cond = E_cond_ED_8mode = -0.13685... was the S36 computation
    # using a DIFFERENT reference (relative to vacuum/different normal state);
    # our SORTED-NORMAL-FILL convention yields -0.1984 for N=1.  These differ
    # by convention, not by physics.  Report both.
    print()
    print("--- E_cond convention comparison (N=1) ---")
    print(f"  This script (SORTED-NORMAL-FILL)     : {ec1:+.10f}")
    print(f"  canonical_constants.E_cond (S36 ED)  : {E_cond_canonical_N1:+.10f}")
    print(f"  (difference = {ec1 - E_cond_canonical_N1:+.6f}; conventions "
          f"differ on reference state)")

    # --- Package results ---
    return {
        "value": float(ratio_21),
        "ratio_21": float(ratio_21),
        "ratio_31": float(ratio_31),
        "ratio_32": float(ratio_32),
        "E_cond_N1": float(ec1),
        "E_cond_N2": float(ec2),
        "E_cond_N3": float(ec3),
        "E_gs_N1": float(results[1]["E_gs"]),
        "E_gs_N2": float(results[2]["E_gs"]),
        "E_gs_N3": float(results[3]["E_gs"]),
        "E_normal_N1": float(results[1]["E_normal"]),
        "E_normal_N2": float(results[2]["E_normal"]),
        "E_normal_N3": float(results[3]["E_normal"]),
        "dim_N1": int(results[1]["dim"]),
        "dim_N2": int(results[2]["dim"]),
        "dim_N3": int(results[3]["dim"]),
        "E_sp_sorted": E_sp_sorted,
        "labels": np.array(labels),
    }


# Section 6: Gate verdict + plot
def evaluate_gate(ratio: float) -> str:
    if ratio >= PASS_THRESHOLD:
        return "PASS"
    if ratio >= INFO_LOWER:
        return "INFO"
    return "FAIL"


def emit_4tuple(value, scheme: str, convention: str, L_max: str) -> str:
    return (f"(value={value:.6f}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict: str, value: float, closure_sha: str) -> None:
    line = (
        f"{GATE_ID}: {verdict} -- value={value:.6f} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX_TAG} sha256={closure_sha}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def make_plot(results: dict, verdict: str, ratio_21: float) -> None:
    Ns = np.array(N_PAIR_VALUES, dtype=float)                      # (local)
    E_cond_vals = np.array([results["E_cond_N1"],
                            results["E_cond_N2"],
                            results["E_cond_N3"]])                  # (local)
    E_gs_vals = np.array([results["E_gs_N1"],
                          results["E_gs_N2"],
                          results["E_gs_N3"]])                      # (local)
    E_norm_vals = np.array([results["E_normal_N1"],
                            results["E_normal_N2"],
                            results["E_normal_N3"]])                # (local)

    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))               # (local)

    ax0 = axes[0]
    ax0.plot(Ns, E_gs_vals, 'o-', label='E_gs (ED)', color='#1f77b4')
    ax0.plot(Ns, E_norm_vals, 's--', label='E_normal (ref)',
             color='#ff7f0e')
    ax0.set_xlabel('N_pair')
    ax0.set_ylabel('Energy (M_KK units)')
    ax0.set_title('Ground state vs. normal-state reference')
    ax0.legend()
    ax0.grid(alpha=0.3)

    ax1 = axes[1]
    ax1.plot(Ns, E_cond_vals, 'o-', color='#2ca02c',
             label='E_cond = E_gs - E_normal')
    ax1.axhline(0.0, color='k', linewidth=0.8)
    ax1.set_xlabel('N_pair')
    ax1.set_ylabel('E_cond (M_KK units)')
    title_main = (f'BCS condensation energy vs N_pair\n'
                  f'ratio N=2/N=1 = {ratio_21:.3f}  (thresholds: '
                  f'PASS>=10, INFO 3-10, FAIL<3)')                   # (local)
    ax1.set_title(title_main)
    ax1.legend()
    ax1.grid(alpha=0.3)

    # Annotate each point
    for N, ec in zip(Ns, E_cond_vals):
        ax1.annotate(f'{ec:+.4f}', (N, ec), textcoords='offset points',
                     xytext=(8, -4), fontsize=9)

    fig.suptitle(f'{GATE_ID}: {verdict}', y=1.02, fontsize=12)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=120, bbox_inches='tight')
    plt.close(fig)


# Section 7: Main
def main() -> int:
    t0 = time.time()                                                # (local)

    # 1. Input pins
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)                                    # (local)
    print(f"  closure: {closure}")
    print()

    # 2. Compute
    result = compute()
    value = result["value"]                                         # (local) = ratio_21

    # 3. Evaluate gate
    verdict = evaluate_gate(value)                                  # (local)

    # 4. Save artifacts
    save_kwargs = {                                                 # (local)
        "value": np.float64(value),
        "ratio_21": np.float64(result["ratio_21"]),
        "ratio_31": np.float64(result["ratio_31"]),
        "ratio_32": np.float64(result["ratio_32"]),
        "E_cond_N1": np.float64(result["E_cond_N1"]),
        "E_cond_N2": np.float64(result["E_cond_N2"]),
        "E_cond_N3": np.float64(result["E_cond_N3"]),
        "E_gs_N1": np.float64(result["E_gs_N1"]),
        "E_gs_N2": np.float64(result["E_gs_N2"]),
        "E_gs_N3": np.float64(result["E_gs_N3"]),
        "E_normal_N1": np.float64(result["E_normal_N1"]),
        "E_normal_N2": np.float64(result["E_normal_N2"]),
        "E_normal_N3": np.float64(result["E_normal_N3"]),
        "dim_N1": np.int64(result["dim_N1"]),
        "dim_N2": np.int64(result["dim_N2"]),
        "dim_N3": np.int64(result["dim_N3"]),
        "E_sp_sorted": result["E_sp_sorted"],
        "labels": result["labels"],
        "N_pair_values": np.array(N_PAIR_VALUES, dtype=np.int64),
        "pass_threshold": np.float64(PASS_THRESHOLD),
        "info_lower": np.float64(INFO_LOWER),
        "scheme": np.array(SCHEME),
        "convention": np.array(CONVENTION),
        "L_max_tag": np.array(L_MAX_TAG),
        "verdict": np.array(verdict),
        "closure_sha256": np.array(closure),
        "input_pins_json": np.array(json.dumps(pins)),
        "tau_fold": np.float64(tau_fold),
    }
    np.savez(OUT_NPZ, **save_kwargs)
    print(f"Saved: {OUT_NPZ}")

    # 5. Plot
    make_plot(result, verdict, result["ratio_21"])
    print(f"Saved: {OUT_PNG}")

    # 6. Emit 4-tuple + append verdict
    print()
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX_TAG)         # (local)
    print(tag)
    append_verdict(verdict, value, closure)
    print(f"Appended verdict to {VERDICT_TXT.name}")

    # 7. Final summary
    wall = time.time() - t0                                         # (local)
    print()
    print("=" * 78)
    print(f"{GATE_ID}: {verdict}")
    print(f"  ratio N=2/N=1 = {result['ratio_21']:.6f}")
    print(f"  ratio N=3/N=1 = {result['ratio_31']:.6f}")
    print(f"  ratio N=3/N=2 = {result['ratio_32']:.6f}")
    print(f"  PASS threshold >= {PASS_THRESHOLD}")
    print(f"  INFO window    [{INFO_LOWER}, {PASS_THRESHOLD})")
    print(f"  FAIL below     {INFO_LOWER}")
    print(f"  Closure SHA    {closure}")
    print(f"  Wall time      {wall:.2f}s")
    print("=" * 78)
    return 0 if verdict != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
