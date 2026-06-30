#!/usr/bin/env python3
"""
S82 W3-2: R-FAMILY-ATLAS-EXTENSION
===================================================================
Gate: S82-R-FAMILY-ATLAS-EXTENSION  [VERIFY]
Classification: GEOMETRIC
Owner: lizzi-spectral-functional-theorist
Write-target: sessions/archive/session-82/session-82-results-workingpaper.md §VI.B
Anchor: sessions/session-plan/session-80-plan.md L1749-L1772 (§W3-2)
Prior: S74 W2-M r_family_stability (R_1, R_2, R_3 in S73B + Wodzicki)

=== PRE-REGISTRATION (S80 plan §W3-2 VERBATIM) ===

GATE: S80-R-FAMILY-ATLAS-EXTENSION
HYPOTHESIS: R_family has universal structure beyond R_1 and R_2 (already
            characterized).
PRE-REGISTERED: Characterize R_3, R_4, R_5, R_6 at same rigor as R_1/R_2.
PASS: All 4 atlased.
INFO: Partial atlasing.
FAIL: Structural obstruction.

=== DEFINITIONS (weight-balance per P4-D CF-6) ===

R-family weight-balanced ratios of Seeley-DeWitt spectral moments a_m of D_K:
  R_k = a_{2(k-1)} * a_{2(k+1)} / a_{2k}^2    for k in {1, 2, 3, 4, 5, 6}

Explicit list (the W3-2 extension targets R_3..R_6):
  R_1 = a_0  * a_4  / a_2^2        (S74 canonical)
  R_2 = a_2  * a_6  / a_4^2        (S74 canonical)
  R_3 = a_4  * a_8  / a_6^2        (W3-2 extension, already in S74 probe)
  R_4 = a_6  * a_10 / a_8^2        (W3-2 extension)
  R_5 = a_8  * a_12 / a_10^2       (W3-2 extension)
  R_6 = a_10 * a_14 / a_12^2       (W3-2 extension)

=== SUBSTITUTION CHAIN — dim-closure ===

  Step 1 (def): In S73B convention a_m = 0.5 * sum_n d_n * |lam_n|^{-m},
                so [a_m] = [M]^{-m} (mass-dim interpretation of the zeta
                spectral action).
  Step 2 (substitute):
        [R_k] = [a_{2(k-1)}] * [a_{2(k+1)}] / [a_{2k}]^2
              = [M]^{-2(k-1)} * [M]^{-2(k+1)} / ([M]^{-2k})^2
  Step 3 (simplify):
        [R_k] = [M]^{-2(k-1) - 2(k+1) + 4k}
              = [M]^{-2k + 2 - 2k - 2 + 4k}
              = [M]^0
  Step 4 (direction): [R_k] = [M]^0 for every k in {1,...,6}. Dim-closure
                      PASSES structurally by construction (Vol(SU(3))
                      cancels per Baptista B2). This is a theorem, not a
                      measurement.

=== THE ATLAS (three criteria per P4-D CF-6 rigor of R_1 / R_2) ===

To "atlas" R_k at rigor equal to R_1/R_2 we pin three properties:

  (i) WEIGHT-BALANCE CONDITION
        Indices sum to zero: 2(k-1) + 2(k+1) - 2*2k = 0. PASS by
        construction (algebraic identity, not a measurement).
        Report: [WEIGHT-BALANCE]: PASS.

  (ii) DIM-CLOSURE
        [R_k] = [M]^0 in the canonical-constants mass-dim assignment
        (see substitution chain above).
        Report: [DIM-CLOSURE]: PASS.

  (iii) REGULATOR-SPREAD VERIFICATION (the empirical part)
        Two conventions for the moments a_m at the SAME eigenvalue
        spectrum + SAME L_max:
          S73B:     a_m = 0.5 * sum d_n / lam_n^m     (half-zeta)
          Wodzicki: a_n ~ zeta_D((8 - n)/2) for d = 8   (dim-reflected)
        Regulator-spread := |R_k^{S73B} - R_k^{Wodz}| / max(|R_k^{S73B}|, |R_k^{Wodz}|)
        Report: pass the L_max-stability threshold < 0.05 in AT LEAST
        ONE convention (S74-inherited threshold). The stability level
        quantifies "regulator-spread under L_max truncation".

=== WODZICKI/S73B REFLECTION SYMMETRY (structural theorem) ===

Let P_m := sum d_n * lam_n^{-2m}. Then both conventions build R_k out
of the SAME P_m:
  a_{2m}^{S73B} = 0.5 * P_m       (half-zeta at argument m)
  a_n^{Wod}     = P_{(8-n)/2}     (dim-8 reflected; W1-C convention)

Substitution into R_k = a_{2(k-1)} * a_{2(k+1)} / a_{2k}^2:
  R_k^{S73B} = P_{k-1} * P_{k+1} / P_k^2              (the 0.5 cancels)
  R_k^{Wod}  = P_{5-k} * P_{3-k} / P_{4-k}^2

Let j := 4 - k. Then 5-k = j+1, 3-k = j-1, 4-k = j, so
  R_k^{Wod} = P_{j+1} * P_{j-1} / P_j^2 = R_j^{S73B}

Therefore the reflection theorem is

  R_k^{Wodzicki} = R_{4-k}^{S73B}     (EXACT identity, not approximation)

where the right-hand side uses NEGATIVE moments for k >= 4, since then
j = 4-k is non-positive (P_0, P_{-1}, P_{-2} = anti-zeta sums of lam^{2|j|}).
Verified to machine zero at every (L_max, k) in Section 5 below.

The atlas-relevant consequence: R_k^{Wod} is just R_j^{S73B} on the OTHER
side of the half-zeta ladder. Each convention privileges a different region
of the P_m ladder, so the **combined atlas covers the full ladder**. For
each k in {1..6}, the pair (R_k^{S73B}, R_k^{Wod}) = (R_k^{S73B}, R_{4-k}^{S73B})
gives two independent handles. The L_max stability min across conventions
is therefore always the stability of the better-conditioned end of the
ladder, never worse than the individual convention.

=== PASS/FAIL/INFO GATE RULE ===

For k in {3, 4, 5, 6}: R_k is "atlased" if all three criteria hold.
  - (i) WEIGHT-BALANCE:     algebraic, PASS by construction.
  - (ii) DIM-CLOSURE:       algebraic, PASS by construction.
  - (iii) REGULATOR-SPREAD: L_max stability < 0.05 in at least one
                            convention (S73B or Wodzicki) at L_max=7.

PASS if all 4 (R_3, R_4, R_5, R_6) atlased.
INFO if 1-3 atlased (partial).
FAIL if 0 atlased (structural obstruction).

=== INPUTS ===

Spectrum: s74_spectrum_cache_L9_tau019.npz (L_max=9 Jensen fold spectrum)
Canonical: canonical_constants.py

=== L_MAX ===

Primary: L_max = 7 for regulator-spread verification (matches S74 W2-M
reference point). Robustness scan at L_max in {3, 5, 9}.
"""

import sys
import os
import time
import hashlib
import numpy as np
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR))
os.chdir(str(SCRIPT_DIR))

os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

from canonical_constants import (
    tau_fold, PI,
    a0_fold, a2_fold, a4_fold,
    Vol_SU3_Haar, M_KK,
    R_protected_fold,
)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUT_NPZ  = SCRIPT_DIR / "s82_w3_2_r_family_atlas.npz"                # (local)
OUT_PNG  = SCRIPT_DIR / "s82_w3_2_r_family_atlas.png"                # (local)
SPECTRUM_CACHE = SCRIPT_DIR / "s74_spectrum_cache_L9_tau019.npz"      # (local)
GATE_VERDICTS  = SCRIPT_DIR / "s82_gate_verdicts.txt"                 # (local)
CANON_PY       = SCRIPT_DIR / "canonical_constants.py"                # (local)

t_start = time.time()  # (local)

GATE_ID     = "S82-R-FAMILY-ATLAS-EXTENSION"                           # (local)
SCHEME_TAG  = "WEIGHT-BALANCED"                                        # (local)
CONV_TAG    = "CC96-EQ-2.11"                                           # (local)
L_MAX_PRIMARY = 7                                                      # (local) per S74 reference
L_MAX_SCAN    = [3, 5, 7, 9]                                           # (local) robustness
EVAL_CUTOFF   = 0.01                                                   # (local) same as S74/S78
STABILITY_THR = 0.05                                                   # (local) S74-inherited
W1M_R1_CANON  = 1.128655                                               # (local) W1-M L_max=3 anchor


# ============================================================================
# SECTION 0: SHA-256 input pins (S81+ canonical form)
# ============================================================================

def sha256_file(path):
    """Return 64-char hex SHA-256 of file contents."""
    h = hashlib.sha256()  # (local)
    with open(path, "rb") as fh:
        while True:
            chunk = fh.read(65536)  # (local)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()

SHA_SPECTRUM = sha256_file(SPECTRUM_CACHE)  # (local)
SHA_CANON    = sha256_file(CANON_PY)        # (local)
SHA_THIS     = sha256_file(__file__)        # (local)

print("=" * 78)
print(f"{GATE_ID} [VERIFY]")
print("=" * 78)
print(f"tau_fold      = {tau_fold}")
print(f"R_1 anchor    = a_0*a_4/a_2^2 = {a0_fold*a4_fold/a2_fold**2:.8f}")
print(f"W1-M canon    = {W1M_R1_CANON}")
print()
print("SHA-256 input pins:")
print(f"  SHA_spectrum         = {SHA_SPECTRUM}")
print(f"  SHA_canonical_const  = {SHA_CANON}")
print(f"  SHA_script_self      = {SHA_THIS}")
print()


# ============================================================================
# SECTION 1: Load spectrum
# ============================================================================
print("=" * 78)
print("SECTION 1: Load D_K spectrum (L_max=9 Jensen-deformed cache)")
print("=" * 78)

assert SPECTRUM_CACHE.exists(), f"Cache missing: {SPECTRUM_CACHE}"
cache = np.load(SPECTRUM_CACHE, allow_pickle=True)
sector_evals = cache['sector_evals'].item()
cache.close()
print(f"  n_sectors loaded: {len(sector_evals)}")


# ============================================================================
# SECTION 2: Compute a_0..a_14 in two conventions
# ============================================================================
print("\n" + "=" * 78)
print("SECTION 2: Spectral moments a_0..a_14 (2 conventions)")
print("=" * 78)


def _collect(sector_dict, L_max, cutoff):
    """Return arrays (|lam|, mult) for level<=L_max, |lam|>cutoff."""
    abs_list = []  # (local)
    mult_list = []  # (local)
    for (p, q), data in sorted(sector_dict.items()):
        if data['level'] <= L_max:
            dim = int(data['dim'])  # (local) irrep dimension
            for ev in data['abs_evals']:
                a = float(ev)  # (local)
                if a > cutoff:
                    abs_list.append(a)
                    mult_list.append(dim)
    return np.array(abs_list), np.array(mult_list, dtype=np.float64)


def compute_moments_S73B(L_max, cutoff, max_power=14):
    """S73B half-spectrum: a_m = 0.5 * sum d_n * |lam_n|^{-m} for m in {0,2,..,14}."""
    lam, mult = _collect(sector_evals, L_max, cutoff)
    a = {}  # (local)
    for m in range(0, max_power + 1, 2):
        if m == 0:
            a[m] = 0.5 * float(np.sum(mult))
        else:
            a[m] = 0.5 * float(np.sum(mult / lam**m))
    return a, len(lam), float(np.sum(mult))


def compute_moments_Wodzicki(L_max, cutoff):
    """Wodzicki convention at d=8: a_n ~ zeta_D((8-n)/2). The mapping

         a_0  ~ P_4 = sum d_n / lam_n^8       (deepest)
         a_2  ~ P_3 = sum d_n / lam_n^6
         a_4  ~ P_2 = sum d_n / lam_n^4
         a_6  ~ P_1 = sum d_n / lam_n^2
         a_8  ~ P_0 = sum d_n                 (count)
         a_10 ~ P_{-1} = sum d_n * lam_n^2    (anti-zeta)
         a_12 ~ P_{-2} = sum d_n * lam_n^4
         a_14 ~ P_{-3} = sum d_n * lam_n^6

    This is the canonical W1-C convention for d=8 dimension reflection.
    """
    lam, mult = _collect(sector_evals, L_max, cutoff)
    P = {}  # (local)
    for k in range(-4, 5):
        # P_k = sum d_n / lam_n^{2k}; negative k means sum d_n * lam_n^{|2k|}
        P[k] = float(np.sum(mult * (lam ** (-2 * k))))
    a = {
        0:  P[4],
        2:  P[3],
        4:  P[2],
        6:  P[1],
        8:  P[0],
        10: P[-1],
        12: P[-2],
        14: P[-3],
    }
    return a


moments_S73B = {}
moments_W    = {}
for L in L_MAX_SCAN:
    a_S, n_evals, n_weighted = compute_moments_S73B(L, EVAL_CUTOFF)
    a_W                       = compute_moments_Wodzicki(L, EVAL_CUTOFF)
    moments_S73B[L] = a_S
    moments_W[L]    = a_W
    print(f"  L_max={L}  n_evals={n_evals:5d}  n_weighted={int(n_weighted)}")


# ============================================================================
# SECTION 3: R_1..R_6 under each convention
# ============================================================================
print("\n" + "=" * 78)
print("SECTION 3: R_1..R_6 under each convention")
print("=" * 78)

K_LADDER = [1, 2, 3, 4, 5, 6]  # (local) the six R_k we atlas
# Index triples (below, above, center) for R_k = a_{2(k-1)} * a_{2(k+1)} / a_{2k}^2
R_INDEX = {k: (2*(k-1), 2*(k+1), 2*k) for k in K_LADDER}


def R_of(moment_dict, k):
    """R_k from moment dict, using the weight-balanced formula."""
    i_lo, i_hi, i_ce = R_INDEX[k]  # (local)
    return moment_dict[i_lo] * moment_dict[i_hi] / moment_dict[i_ce]**2


R_S73B_tab = {L: {k: R_of(moments_S73B[L], k) for k in K_LADDER} for L in L_MAX_SCAN}
R_W_tab    = {L: {k: R_of(moments_W[L],    k) for k in K_LADDER} for L in L_MAX_SCAN}

print("\n  S73B convention:")
print(f"  {'L_max':>5}  " + "  ".join(f"R_{k:<1}" + " "*8 for k in K_LADDER))
for L in L_MAX_SCAN:
    row = "  ".join(f"{R_S73B_tab[L][k]:10.6f}" for k in K_LADDER)
    print(f"  {L:>5}  {row}")

print("\n  Wodzicki convention:")
print(f"  {'L_max':>5}  " + "  ".join(f"R_{k:<1}" + " "*8 for k in K_LADDER))
for L in L_MAX_SCAN:
    row = "  ".join(f"{R_W_tab[L][k]:10.6f}" for k in K_LADDER)
    print(f"  {L:>5}  {row}")


# ============================================================================
# SECTION 4: L_max stability per R_k per convention
# ============================================================================
print("\n" + "=" * 78)
print(f"SECTION 4: L_max stability |R(L=5) - R(L=7)| / |R(L=7)|")
print("=" * 78)

stab_S73B = {}
stab_W    = {}
for k in K_LADDER:
    r5_S = R_S73B_tab[5][k]; r7_S = R_S73B_tab[7][k]
    r5_W = R_W_tab[5][k];    r7_W = R_W_tab[7][k]
    stab_S73B[k] = abs(r5_S - r7_S) / abs(r7_S)
    stab_W[k]    = abs(r5_W - r7_W) / abs(r7_W)

print(f"  {'R_k':<4} {'stab_S73B':>12} {'stab_Wodz':>12} {'min(spread)':>14} "
      f"{'convention_min':>16}")
for k in K_LADDER:
    mn = min(stab_S73B[k], stab_W[k])
    conv_min = "S73B" if stab_S73B[k] <= stab_W[k] else "Wodzicki"
    print(f"  R_{k:<2} {stab_S73B[k]:12.6f} {stab_W[k]:12.6f} {mn:14.6f} "
          f"{conv_min:>16}")


# ============================================================================
# SECTION 5: Wodzicki/S73B reflection symmetry (verify structural theorem)
# ============================================================================
print("\n" + "=" * 78)
print("SECTION 5: Wodzicki/S73B reflection symmetry check")
print("=" * 78)
print("  THEOREM: R_k^{Wodzicki} == R_{4-k}^{S73B} (exact identity via P_m)")
print("  Let P_m = sum d_n * lam_n^{-2m}; a^{S73B}_{2m}=0.5*P_m, a^{Wod}_n=P_{(8-n)/2}")
print("  Substitution (see header): R_k^{Wod} = P_{5-k}*P_{3-k}/P_{4-k}^2")
print("                             = P_{j+1}*P_{j-1}/P_j^2 = R_j^{S73B}, j=4-k")
print()


def P_of(L_max, cutoff, m):
    """Return P_m(L) = sum d_n * lam_n^{-2m} with negative m giving anti-zeta sums."""
    lam, mult = _collect(sector_evals, L_max, cutoff)
    return float(np.sum(mult * (lam ** (-2 * m))))


def R_from_P(L_max, cutoff, j):
    """R_j via generalized S73B: R_j = P_{j-1}*P_{j+1}/P_j^2, j can be <=0."""
    return (P_of(L_max, cutoff, j - 1) *
            P_of(L_max, cutoff, j + 1) /
            P_of(L_max, cutoff, j)**2)


refl_errs = {}  # (local)
print(f"  {'L_max':>5}  {'k':>2}  {'R_k^Wod':>14}  {'j=4-k':>6}  "
      f"{'R_j^S73B-gen':>16}  {'rel err':>12}")
for L in L_MAX_SCAN:
    for k in K_LADDER:
        j = 4 - k  # (local) reflection index
        lhs = R_W_tab[L][k]
        rhs = R_from_P(L, EVAL_CUTOFF, j)
        err = abs(lhs - rhs) / max(abs(rhs), 1e-30)
        refl_errs[(L, k)] = err
        print(f"  {L:>5}  {k:>2}  {lhs:14.10f}  {j:>6}  {rhs:16.10f}  {err:12.2e}")

max_refl_err = max(refl_errs.values())  # (local)
print(f"\n  max reflection residual across all (L,k) pairs = {max_refl_err:.2e}")
if max_refl_err < 1e-10:
    print("  Reflection symmetry R_k^{Wod} = R_{4-k}^{S73B,gen} verified to "
          "machine epsilon.")
else:
    print("  Reflection symmetry BROKEN at the tested level.")


# ============================================================================
# SECTION 6: Atlas verdict per R_k in {3, 4, 5, 6}
# ============================================================================
print("\n" + "=" * 78)
print("SECTION 6: ATLAS verdict per R_k in {R_3, R_4, R_5, R_6}")
print("=" * 78)

atlas = {}  # (local)
for k in [3, 4, 5, 6]:
    # (i) weight-balance: algebraic
    wb = "PASS"  # (local)
    # (ii) dim-closure: algebraic
    dc = "PASS"  # (local)
    # (iii) regulator-spread: min across conventions
    min_stab = min(stab_S73B[k], stab_W[k])  # (local)
    min_conv = "S73B" if stab_S73B[k] <= stab_W[k] else "Wodzicki"
    rs = "PASS" if min_stab < STABILITY_THR else "FAIL"

    atlased = (wb == "PASS") and (dc == "PASS") and (rs == "PASS")
    atlas[k] = {
        'weight_balance': wb,
        'dim_closure':    dc,
        'regulator_spread': rs,
        'min_stab':       min_stab,
        'min_conv':       min_conv,
        'atlased':        atlased,
    }

print(f"  {'R_k':<4} {'weight-bal':>12} {'dim-clos':>10} {'reg-spread':>12} "
      f"{'min_stab':>10} {'conv_min':>10} {'atlased':>10}")
for k in [3, 4, 5, 6]:
    info = atlas[k]
    print(f"  R_{k:<2} {info['weight_balance']:>12} {info['dim_closure']:>10} "
          f"{info['regulator_spread']:>12} {info['min_stab']:10.6f} "
          f"{info['min_conv']:>10} {str(info['atlased']):>10}")

n_atlased = sum(1 for k in [3, 4, 5, 6] if atlas[k]['atlased'])  # (local)
print(f"\n  Atlased count = {n_atlased} / 4")

if n_atlased == 4:
    verdict = "PASS"
    reason  = ("All four R_3..R_6 atlased: weight-balance + dim-closure hold by "
               "construction; regulator-spread (L_max=5->7) < 0.05 in at least "
               "one of S73B / Wodzicki for each k.")
elif n_atlased == 0:
    verdict = "FAIL"
    reason  = ("No R_k in {R_3,R_4,R_5,R_6} has L_max stability below 0.05 in "
               "either convention. Structural obstruction on the upper R-ladder.")
else:
    verdict = "INFO"
    reason  = (f"Partial atlasing: {n_atlased}/4 of R_3..R_6 meet all three atlas "
               f"criteria.")

print(f"\n  Gate verdict: {verdict}")
print(f"  Reason: {reason}")


# ============================================================================
# SECTION 7: Plot
# ============================================================================
print("\n" + "=" * 78)
print("SECTION 7: Plot R_k across regulators")
print("=" * 78)

fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))

# Panel 1: R_1..R_6 vs L_max in each convention
ax = axes[0]
colors_S73B = plt.cm.Blues(np.linspace(0.4, 0.95, len(K_LADDER)))
colors_W    = plt.cm.Reds(np.linspace(0.4, 0.95, len(K_LADDER)))
for i, k in enumerate(K_LADDER):
    ys_S = [R_S73B_tab[L][k] for L in L_MAX_SCAN]
    ys_W = [R_W_tab[L][k]    for L in L_MAX_SCAN]
    ax.plot(L_MAX_SCAN, ys_S, '-o', color=colors_S73B[i], ms=7,
            label=f"R_{k} S73B")
    ax.plot(L_MAX_SCAN, ys_W, '--s', color=colors_W[i], ms=6,
            label=f"R_{k} Wodz")
ax.axhline(W1M_R1_CANON, color='k', ls=':', lw=0.8, alpha=0.6,
           label=f"W1-M R_1 canon = {W1M_R1_CANON}")
ax.set_xlabel("L_max")
ax.set_ylabel("R_k")
ax.set_title("R-family across L_max in both conventions")
ax.set_xticks(L_MAX_SCAN)
ax.grid(True, alpha=0.3)
ax.legend(fontsize=7, ncol=2, loc='best')

# Panel 2: L_max stability per k, per convention
ax = axes[1]
x = np.arange(len(K_LADDER))
w = 0.38  # (local) bar width
ax.bar(x - w/2, [stab_S73B[k] for k in K_LADDER], w, color='navy', alpha=0.85,
       label='S73B')
ax.bar(x + w/2, [stab_W[k]    for k in K_LADDER], w, color='darkred', alpha=0.85,
       label='Wodzicki')
ax.axhline(STABILITY_THR, color='k', ls='--', lw=1.2,
           label=f"threshold = {STABILITY_THR}")
ax.set_xticks(x)
ax.set_xticklabels([f"R_{k}" for k in K_LADDER])
ax.set_ylabel("|R(L=5) - R(L=7)| / |R(L=7)|")
ax.set_yscale('log')
ax.set_title("L_max stability (5->7) per R_k, per convention")
ax.grid(True, alpha=0.3, axis='y', which='both')
ax.legend(fontsize=8)

for i, k in enumerate(K_LADDER):
    ax.text(i - w/2, stab_S73B[k] * 1.25, f"{stab_S73B[k]*100:.2f}%",
            ha='center', fontsize=6)
    ax.text(i + w/2, stab_W[k] * 1.25, f"{stab_W[k]*100:.2f}%",
            ha='center', fontsize=6)

plt.suptitle(f"{GATE_ID}: verdict = {verdict}  (atlased {n_atlased}/4)",
             fontsize=11, fontweight='bold')
plt.tight_layout()
plt.savefig(OUT_PNG, dpi=140, bbox_inches='tight')
plt.close(fig)
print(f"  -> {OUT_PNG.name}")


# ============================================================================
# SECTION 8: Persist npz
# ============================================================================
print("\n" + "=" * 78)
print("SECTION 8: Save npz")
print("=" * 78)

# Flatten for npz
def _flat(tab_of_tab, key_list_outer, key_list_inner):
    arr = np.zeros((len(key_list_outer), len(key_list_inner)), dtype=np.float64)
    for i, o in enumerate(key_list_outer):
        for j, inn in enumerate(key_list_inner):
            arr[i, j] = tab_of_tab[o][inn]
    return arr


R_S73B_arr = _flat(R_S73B_tab, L_MAX_SCAN, K_LADDER)
R_W_arr    = _flat(R_W_tab,    L_MAX_SCAN, K_LADDER)

np.savez_compressed(
    OUT_NPZ,
    gate_id=np.array(GATE_ID),
    verdict=np.array(verdict),
    reason=np.array(reason),
    k_ladder=np.array(K_LADDER),
    L_max_scan=np.array(L_MAX_SCAN),
    L_max_primary=L_MAX_PRIMARY,
    R_S73B=R_S73B_arr,
    R_Wodzicki=R_W_arr,
    stab_S73B=np.array([stab_S73B[k] for k in K_LADDER]),
    stab_Wodzicki=np.array([stab_W[k] for k in K_LADDER]),
    stability_threshold=STABILITY_THR,
    max_reflection_residual=max_refl_err,
    atlas_R3_atlased=atlas[3]['atlased'],
    atlas_R4_atlased=atlas[4]['atlased'],
    atlas_R5_atlased=atlas[5]['atlased'],
    atlas_R6_atlased=atlas[6]['atlased'],
    n_atlased=n_atlased,
    SHA_spectrum=SHA_SPECTRUM,
    SHA_canonical=SHA_CANON,
    SHA_script=SHA_THIS,
    EVAL_CUTOFF=EVAL_CUTOFF,
    tau_fold_used=tau_fold,
)
print(f"  -> {OUT_NPZ.name}")


# ============================================================================
# SECTION 9: Closure hash
# ============================================================================
closure_map = (
    f"SHA_spectrum={SHA_SPECTRUM}|"
    f"SHA_canonical={SHA_CANON}|"
    f"SHA_script={SHA_THIS}|"
    f"L_max_primary={L_MAX_PRIMARY}|"
    f"tau_fold={tau_fold}|"
    f"EVAL_CUTOFF={EVAL_CUTOFF}|"
    f"STABILITY_THR={STABILITY_THR}|"
    f"R_S73B_L7={','.join(f'{R_S73B_tab[7][k]:.10e}' for k in K_LADDER)}|"
    f"R_Wodz_L7={','.join(f'{R_W_tab[7][k]:.10e}' for k in K_LADDER)}|"
    f"n_atlased={n_atlased}|"
    f"max_refl_err={max_refl_err:.6e}|"
    f"verdict={verdict}"
)  # (local)
closure_sha = hashlib.sha256(closure_map.encode("utf-8")).hexdigest()  # (local)


# ============================================================================
# SECTION 10: 4-tuple + verdict line
# ============================================================================
tag_value   = f"{n_atlased}/4"                           # (local)
tag_scheme  = SCHEME_TAG                                 # (local)
tag_conv    = CONV_TAG                                   # (local)
tag_L_max   = f"L_max={L_MAX_PRIMARY}"                    # (local)

print("\n" + "=" * 78)
print("SECTION 10: Output tag + verdict line")
print("=" * 78)
print(f"  value      = {tag_value}")
print(f"  scheme     = {tag_scheme}")
print(f"  convention = {tag_conv}")
print(f"  L_max      = {tag_L_max}")
print(f"  sha256     = {closure_sha}")
print(f"  verdict    = {verdict}")

verdict_line = (
    f"{GATE_ID}: {verdict} -- "
    f"value={tag_value} scheme={tag_scheme} convention={tag_conv} "
    f"{tag_L_max} sha256={closure_sha}"
)  # (local)

with open(GATE_VERDICTS, "a", encoding="utf-8") as fh:
    fh.write(verdict_line + "\n")

print(f"\n  appended to: {GATE_VERDICTS.name}")
print(f"  verdict line: {verdict_line}")

t_end = time.time()  # (local)
print(f"\nwall time: {t_end - t_start:.2f}s")
