#!/usr/bin/env python3
"""
S83 Wave 3 Gate G29 -- MULTIPAIR-N3-SATURATION
==============================================

Gate: S83-MULTIPAIR-N3-SATURATION  [VERIFY-THEOREM]
Classification: PARTICLE + PHONONIC
Owner: landau-condensed-matter-theorist

Purpose:
  Verify that the canonical 8-mode Bogoliubov Hilbert space can host
  N_pair = 3 Cooper pairs without violating Pauli exclusion. This is
  the natural extension of the S59/S60/S61 multipair pair-transfer
  construction (N_pair in {1, 2}) to the next admissible fermion-
  parity sector.

Phononic framing:
  Each Cooper pair is a phononic composite excitation: a bound
  (k, -k) / (spin_up, spin_down) pattern on the substrate. Two pairs
  cannot share the same k-level (Pauli), so the maximum number of
  non-overlapping pairs on an N_mode Bogoliubov space is N_mode / 2.
  For the canonical 8-mode basis (S36: 4 B2 + 1 B1 + 3 B3), the
  saturation bound is floor(8/2) = 4. N_pair = 3 lies one step below
  saturation, and the space of Pauli-compatible 3-pair configurations
  should have dimension C(4, 3) = 4.

Substitution chain [VERIFY-THEOREM]:
  Step 1 (definitions):
    N_modes = 8  (canonical BCS Bogoliubov basis, S36 E_cond_ED_8mode)
    Each mode = one (k, spin) fermion slot.
    A Cooper pair occupies a doublet {(k, up), (k, down)} -- two
    modes. Let K = N_modes / 2 = 4 be the number of k-levels.
  Step 2 (Pauli rule):
    Let C = (c_1, ..., c_{N_pair}) be a pair configuration, where
    each c_i in {1, ..., K} is the k-level occupied by pair i.
    Pauli exclusion <=> all c_i distinct.
  Step 3 (substitution):
    configs_count = # { C : |C| = N_pair, c_i distinct in {1,...,K} }
                  = K * (K-1) * ... * (K - N_pair + 1) / N_pair!   [unordered]
                  = C(K, N_pair)                                   (unordered)
  Step 4 (plug in):
    N_pair = 3, K = 4:
    configs_count = C(4, 3) = 4
  Step 5 (direction):
    configs_count >= 1 <=> at least one Pauli-compatible arrangement
    Since 4 >= 1, Pauli exclusion is STRUCTURALLY RESPECTED.
    Therefore: saturation_N3 = True -> PASS.
  Step 6 (saturation bound cross-check):
    N_pair_max(N_modes) = floor(N_modes / 2) = floor(8/2) = 4
    N_pair = 3 <= 4, so we are below saturation by exactly one slot.
    Residual free k-levels after N_pair = 3: K - 3 = 1.
    Residual free modes: N_modes - 2*N_pair = 8 - 6 = 2.

Passes / fails:
  PASS: configs_count >= 1 AND 2*N_pair <= N_modes (no overflow).
  FAIL: Pauli violation (impossible to place 3 pairs without overlap).

Output 4-tuple: (configs_count=4, scheme=8-mode-Bogoliubov,
                 convention=N=3-pair, L_max=N/A)
"""

from __future__ import annotations

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import hashlib
import itertools
import math
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# --- Canonical constants import (MANDATORY; S34+) ---
sys.path.insert(0, str(Path(__file__).resolve().parent))
from canonical_constants import E_cond_ED_8mode, n_Bog  # (framework pins)

# ----------------------------------------------------------------------------
# Local pins (machinery, [VERIFY-THEOREM])
# ----------------------------------------------------------------------------
N_modes      = 8                 # (local) canonical BCS 8-mode Bogoliubov basis (S36)
N_pair       = 3                 # (local) target pair count for G29
K_levels     = N_modes // 2      # (local) number of k-doublets
OUTPUT_STEM  = Path(__file__).with_suffix('')  # (local) npz/png basename

print(f"=== S83 Wave 3 Gate G29 -- MULTIPAIR-N3-SATURATION ===")
print(f"N_modes      = {N_modes}")
print(f"N_pair       = {N_pair}")
print(f"K_levels     = {K_levels}  (pair doublets)")
print(f"Canonical anchor: E_cond_ED_8mode = {E_cond_ED_8mode}")
print()

# ----------------------------------------------------------------------------
# Input-pin SHA-256 chain (S81+ standard)
# ----------------------------------------------------------------------------
# This gate is a structural theorem -- there are no dynamic input files.
# Pin the STATIC machinery vector instead.
input_pins = {                                               # (local)
    "N_modes":    str(N_modes),
    "N_pair":     str(N_pair),
    "K_levels":   str(K_levels),
    "scheme":     "8-mode-Bogoliubov",
    "convention": "N=3-pair",
    "L_max":      "N/A",
    "anchor":     f"E_cond_ED_8mode={E_cond_ED_8mode:.14e}",
}
pin_blob = "\n".join(f"{k}={v}" for k, v in sorted(input_pins.items()))  # (local)
closure_sha = hashlib.sha256(pin_blob.encode('utf-8')).hexdigest()       # (local)
print("Input pin map (sorted):")
for k, v in sorted(input_pins.items()):
    print(f"  {k}: {v}")
print(f"Closure SHA-256: {closure_sha}")
print()

# ----------------------------------------------------------------------------
# Core construction: enumerate Pauli-compatible 3-pair configurations
# ----------------------------------------------------------------------------
def enumerate_pauli_compatible_configs(N_modes: int, N_pair: int) -> list[tuple[int, ...]]:
    """Return the list of unordered k-level tuples (i_1<i_2<...<i_{N_pair})
    that place N_pair Cooper pairs on K = N_modes/2 k-levels without Pauli
    exclusion violation.

    Physics:
      - Each pair occupies a doublet {(k, up), (k, down)}.
      - Pauli: no two pairs may share the same k-level.
      - Hence admissible configs = unordered N_pair-subsets of {1,...,K}.
    """
    if N_modes % 2 != 0:
        raise ValueError("N_modes must be even (k-doublet pairing).")
    K = N_modes // 2                                        # (local)
    if N_pair > K:
        return []
    return list(itertools.combinations(range(1, K + 1), N_pair))


# Enumerate
pair_configs = enumerate_pauli_compatible_configs(N_modes, N_pair)   # (local)
n_configs    = len(pair_configs)                                     # (local)

# Theoretical closed-form
n_theory = math.comb(K_levels, N_pair)                               # (local)

print(f"Enumerated Pauli-compatible configs (k-level tuples):")
for cfg in pair_configs:
    modes_used = sorted(2 * k - 2 for k in cfg) + sorted(2 * k - 1 for k in cfg)  # (local)
    print(f"  k-levels = {cfg}  -> modes occupied = {modes_used}")
print(f"\nn_configs (enumerated)    = {n_configs}")
print(f"n_theory  = C({K_levels},{N_pair}) = {n_theory}")
assert n_configs == n_theory, "Enumeration disagrees with C(K, N_pair) closed form."

# ----------------------------------------------------------------------------
# Explicit Pauli-violation check
# ----------------------------------------------------------------------------
# For each config, verify no k-level is duplicated (Pauli).
pauli_violations = 0                                                  # (local)
for cfg in pair_configs:
    if len(set(cfg)) != len(cfg):
        pauli_violations += 1

print(f"\nPauli exclusion audit:")
print(f"  configs checked          = {n_configs}")
print(f"  Pauli violations found   = {pauli_violations}")
assert pauli_violations == 0, "Pauli violation in enumerated configuration set."

# ----------------------------------------------------------------------------
# Saturation analysis
# ----------------------------------------------------------------------------
N_pair_max        = N_modes // 2                                      # (local)
modes_used_by_N3  = 2 * N_pair                                        # (local)
modes_residual    = N_modes - modes_used_by_N3                        # (local)
klevels_residual  = K_levels - N_pair                                 # (local)
below_saturation  = N_pair < N_pair_max                               # (local)
at_saturation     = N_pair == N_pair_max                              # (local)

print(f"\nSaturation analysis:")
print(f"  N_pair_max (= N_modes/2)      = {N_pair_max}")
print(f"  modes occupied by N_pair=3   = {modes_used_by_N3}")
print(f"  modes residual               = {modes_residual}")
print(f"  k-levels residual            = {klevels_residual}")
print(f"  below saturation?            = {below_saturation}")
print(f"  at saturation?               = {at_saturation}")

# ----------------------------------------------------------------------------
# Cross-check 1: full 8-mode Fock space dimension = 2^8 = 256; count of
# states with exactly N_pair fully-occupied doublets
# ----------------------------------------------------------------------------
# A k-level is "fully occupied by a pair" iff both its modes (k,up) and
# (k,down) are filled.
def count_fockstates_with_n_full_doublets(N_modes: int, N_pair: int) -> int:
    """Count 8-mode Fock basis states |n_1 ... n_8> (n_i in {0,1}) having
    exactly N_pair k-levels with BOTH modes occupied.

    Modes are paired: (0,1) = k=1, (2,3) = k=2, (4,5) = k=3, (6,7) = k=4.
    """
    K = N_modes // 2                                                  # (local)
    total = 0                                                         # (local)
    for state in range(2 ** N_modes):
        bits = [(state >> i) & 1 for i in range(N_modes)]             # (local)
        # For each k-level, check both bits
        n_full = 0                                                    # (local)
        for k_idx in range(K):
            if bits[2 * k_idx] == 1 and bits[2 * k_idx + 1] == 1:
                n_full += 1
        if n_full == N_pair:
            # Also require that no k-level is HALF occupied
            n_half = 0                                                # (local)
            for k_idx in range(K):
                if bits[2 * k_idx] != bits[2 * k_idx + 1]:
                    n_half += 1
            if n_half == 0:
                total += 1
    return total


fock_count_N3 = count_fockstates_with_n_full_doublets(N_modes, N_pair)   # (local)
print(f"\nCross-check 1 (full Fock enumeration, 2^8 = 256 states):")
print(f"  # of states with exactly 3 full doublets & 0 half-doublets = {fock_count_N3}")
assert fock_count_N3 == n_theory, "Fock enumeration disagrees with C(4,3)."

# ----------------------------------------------------------------------------
# Cross-check 2: Spectrum of pair-number operator N_pair_op = sum_k b_k^dag b_k
# with b_k^dag = c_{k,up}^dag c_{k,down}^dag.  In the pair-coherent subspace
# (states with no half-filled k-levels), N_pair_op has spectrum {0, 1, ..., K}.
# Dim of the N_pair-eigenspace = C(K, N_pair).
# ----------------------------------------------------------------------------
# Build the coherent-pair subspace: basis states indexed by K-bit strings,
# bit j = 1 iff k-level j is fully occupied.
pair_subspace_dim = 2 ** K_levels                                    # (local)
pair_number_spectrum = np.zeros(pair_subspace_dim, dtype=int)        # (local)
for s in range(pair_subspace_dim):
    pair_number_spectrum[s] = bin(s).count('1')

dim_N3_eigenspace = int(np.sum(pair_number_spectrum == N_pair))      # (local)
print(f"\nCross-check 2 (pair-coherent subspace, dim = 2^K = {pair_subspace_dim}):")
print(f"  dim(N_pair = 3 eigenspace) = {dim_N3_eigenspace}")
assert dim_N3_eigenspace == n_theory, "Pair-coherent eigenspace dim mismatch."

# ----------------------------------------------------------------------------
# Cross-check 3: confirm scan over N_pair in {0,1,2,3,4,5}
# (N_pair > K = 4 MUST give 0)
# ----------------------------------------------------------------------------
scan_N        = list(range(0, K_levels + 2))                         # (local)
scan_configs  = [len(enumerate_pauli_compatible_configs(N_modes, n)) for n in scan_N]  # (local)
scan_theory   = [math.comb(K_levels, n) if n <= K_levels else 0 for n in scan_N]       # (local)

print(f"\nCross-check 3 (N_pair scan 0..{K_levels + 1}):")
print(f"  {'N_pair':>6} | {'enum':>6} | {'C(K,N)':>6}")
for n, e, t in zip(scan_N, scan_configs, scan_theory):
    print(f"  {n:>6d} | {e:>6d} | {t:>6d}")
    assert e == t, f"Scan mismatch at N_pair={n}"

# Confirm overflow at N_pair = 5 (= K+1) returns 0
assert scan_configs[-1] == 0, "Expected zero configs at N_pair = K+1."

# ----------------------------------------------------------------------------
# Verdict
# ----------------------------------------------------------------------------
saturation_N3 = (n_configs > 0) and (modes_used_by_N3 <= N_modes)    # (local)
verdict = "PASS" if saturation_N3 else "FAIL"                         # (local)

print(f"\n=== Verdict Summary ===")
print(f"Pauli-compatible 3-pair configs on 8 modes: {n_configs}")
print(f"Closed-form C(4,3):                         {n_theory}")
print(f"Modes used / total:                         {modes_used_by_N3} / {N_modes}")
print(f"Residual free modes:                        {modes_residual}")
print(f"Pauli violations:                           {pauli_violations}")
print(f"below_saturation:                           {below_saturation}")
print(f"at_saturation:                              {at_saturation}")
print(f"\nVerdict: {verdict}")
print(f"4-tuple: (configs_count={n_configs}, scheme=8-mode-Bogoliubov, "
      f"convention=N=3-pair, L_max=N/A)")
print(f"sha256={closure_sha}")

# ----------------------------------------------------------------------------
# Persist: npz + png
# ----------------------------------------------------------------------------
npz_path = OUTPUT_STEM.with_suffix('.npz')                            # (local)
png_path = OUTPUT_STEM.with_suffix('.png')                            # (local)

np.savez(
    npz_path,
    N_modes=N_modes,
    N_pair=N_pair,
    K_levels=K_levels,
    n_configs=n_configs,
    n_theory=n_theory,
    pauli_violations=pauli_violations,
    fock_count_N3=fock_count_N3,
    dim_N3_eigenspace=dim_N3_eigenspace,
    N_pair_max=N_pair_max,
    modes_used_by_N3=modes_used_by_N3,
    modes_residual=modes_residual,
    klevels_residual=klevels_residual,
    below_saturation=below_saturation,
    at_saturation=at_saturation,
    scan_N=np.array(scan_N),
    scan_configs=np.array(scan_configs),
    scan_theory=np.array(scan_theory),
    saturation_N3=saturation_N3,
    verdict=verdict,
    closure_sha=closure_sha,
    configs_flat=np.array(pair_configs, dtype=int),
)

# Plot: scan_configs and scan_theory vs N_pair
fig, ax = plt.subplots(1, 1, figsize=(6.0, 4.0))
ax.plot(scan_N, scan_configs, marker='o', linestyle='-', color='tab:blue',
        label='enumerated C(K,N)', markersize=8)
ax.plot(scan_N, scan_theory, marker='x', linestyle='--', color='tab:red',
        label=r'closed form $\binom{K}{N_{\mathrm{pair}}}$', markersize=10)
ax.axvline(N_pair, linestyle=':', color='k', alpha=0.6,
           label=f'$N_{{\\rm pair}}={N_pair}$ (target)')
ax.axvline(K_levels, linestyle=':', color='tab:green', alpha=0.6,
           label=f'saturation $N_{{\\rm pair}}^{{\\rm max}}={K_levels}$')
ax.set_xlabel(r'$N_{\rm pair}$')
ax.set_ylabel('Pauli-compatible configurations')
ax.set_title(r'S83 G29: Pauli saturation of $N_{\rm pair}$ on 8 modes '
             f'(verdict: {verdict})')
ax.legend(loc='upper right', fontsize=9)
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(png_path, dpi=120)
plt.close(fig)

print(f"\nSaved: {npz_path}")
print(f"Saved: {png_path}")

# ----------------------------------------------------------------------------
# Verdict line emission (caller appends to s83_gate_verdicts.txt)
# ----------------------------------------------------------------------------
verdict_line = (
    f"S83-MULTIPAIR-N3-SATURATION: {verdict} -- "
    f"value=configs_count={n_configs} "
    f"scheme=8-mode-Bogoliubov "
    f"convention=N=3-pair "
    f"L_max=N/A "
    f"sha256={closure_sha}"
)
print(f"\n{verdict_line}")
