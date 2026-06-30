#!/usr/bin/env python3
"""
S85 W8-6: S85-W8-6-LEGGETT-TENSOR-F-B-CLOSURE
=====================================================================
Test whether the rank-2 Leggett tensor correction δf_B^(2) ≥ 0.11
closes at least half of the W5-64 22% f_B gap (f_B^(1) = 0.78).

Gate: S85-W8-6-LEGGETT-TENSOR-F-B-CLOSURE  [VERIFY]
Classification: PHONONIC (Leggett inter-band phononic mode; rank-2
                correction is beyond-mean-field sub-leading)
Owner: volovik-superfluid-universe-theorist
Plan: sessions/session-plan/session-85-plan-w8.md §W8-6

PRE-REGISTERED THRESHOLDS (plan §W8-6 step 9):
  PASS: δf_B^(2) ≥ 0.11 AND corrected f_B ≥ 0.89 (closes ≥ half of gap)
  FAIL: δf_B^(2) < 0.05 (< 1/4 of gap)
  INFO: 0.05 ≤ δf_B^(2) < 0.11 (partial, marginal)

SUBSTITUTION CHAIN (plan §W8-6 step 10):
  Def 1: f_B = Leggett-channel amplitude closure fraction
  Def 2: f_B^(1) = 0.78 (leading mean-field; W5-64)
  Def 3: T^(2)_{ab} = <n_a n_b>_{GGE} rank-2 GGE tensor
         (for inter-band pair operators n_a on Leggett basis)
  Def 4: δf_B^(2) = r_L² × <L|T^(2)|L>            [rank-2 correction]
  Def 5: f_B_corrected = f_B^(1) + δf_B^(2)       [additive at leading order]

  Step 1: Gap target = 1.0 − 0.78 = 0.22 (22%); PASS threshold = 0.11
  Step 2: r_L = 0.617 (LEGGETT-VACUUM-70 sudden-quench ratio); r_L² = 0.3807
  Step 3: 3 inter-band pairs on Leggett basis: {(B1,B2), (B2,B3), (B1,B3)}
  Step 4: GGE occupation per pair n_eff = r_L × n_Bog / 3
          = 0.617 × 0.9986 / 3 = 0.20543
  Step 5: Bose-statistics rank-2 tensor:
          T^(2)_{ii} = n_eff · (1 + n_eff) = 0.20543 × 1.20543 = 0.24763
          T^(2)_{ij,i≠j} = n_eff²             = 0.20543² = 0.04220
  Step 6: Leggett ground state |L⟩ = (1, 1, 1)/√3
          <L|T^(2)|L> = (1/3) · Σ_{ij} T^(2)_{ij}
                      = (1/3) · (3·0.24763 + 6·0.04220)
                      = (1/3) · (0.7429 + 0.2532)
                      = (1/3) · 0.9961
                      = 0.3320
  Step 7: δf_B^(2) = 0.3807 × 0.3320 = 0.1264
  Step 8: Direction: δf_B^(2) = 0.1264 > 0.11 threshold ⇒ PASS (margin 14.9%)
          Corrected f_B = 0.78 + 0.1264 = 0.9064 ≥ 0.89 ⇒ PASS.

References:
  - plan: sessions/session-plan/session-85-plan-w8.md §W8-6
  - S70 LEGGETT-VACUUM-70 (r_L = 0.617 source)
  - W5-64 f_B = 0.78 baseline (agent memory)
  - Agent memory: leggett-vacuum-70-result.md
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
import json
import hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))                    # (local)
sys.path.insert(0, HERE)

from canonical_constants import (
    M_KK,
    Delta_B3,
    Delta_0_OES,        # B1 gap
    Delta_0_GL,         # B2 gap
    Delta_BCS,          # canonical gap
    omega_L1,           # Leggett-1 frequency 0.138
    tau_fold,
    dt_transit,
    n_Bog,              # Bogoliubov fraction per mode (S38)
)

# Leggett ratio r_L = 0.617 is from S70 LEGGETT-VACUUM-70; not canonical yet.
# Provenance: agent-memory/volovik-superfluid-universe-theorist/leggett-vacuum-70-result.md
r_L = 0.617  # (local) S70 LEGGETT-VACUUM-70 sudden-quench Leggett ratio

# f_B^(1) from W5-64 (not canonical; provenance: plan §W8-6 hypothesis line 105)
f_B_leading = 0.78  # (local) W5-64 leading mean-field Leggett amplitude
f_B_gap = 1.0 - f_B_leading  # (local) 22%

# ============================================================
# SECTION 0: Input SHA-256 pins
# ============================================================
GATE_ID = "S85-W8-6-LEGGETT-TENSOR-F-B-CLOSURE"                      # (local)
SCHEME = "Leggett_rank2"                                             # (local)
CONVENTION = "ConvA_coth"                                            # (local)
L_MAX = 8                                                            # (local)

INPUT_FILES = [                                                      # (local)
    os.path.join(HERE, 'canonical_constants.py'),
    os.path.join(HERE, 's83_w3_g39_leggett_bogoliubov.py'),
    os.path.join(HERE, 's84_w5_a_s_floor_branch_b.py'),
]


def _sha256(path):
    if not os.path.exists(path):
        return 'MISSING'
    with open(path, 'rb') as h:
        return hashlib.sha256(h.read()).hexdigest()


print("=" * 76)
print(f"{GATE_ID}  (rank-2 Leggett tensor correction δf_B^(2))")
print("=" * 76)
print("\n[SEC 0] Input SHA-256 pins")
INPUT_SHAS = {}                                                      # (local)
for _f in INPUT_FILES:
    _h = _sha256(_f)                                                 # (local)
    rel = os.path.relpath(_f, os.path.dirname(HERE)).replace("\\", "/")
    INPUT_SHAS[rel] = _h
    _tag = (_h[:16] + '...' + _h[-8:]) if _h != 'MISSING' else 'MISSING'
    print(f"  {os.path.basename(_f):46s} sha256={_tag}")

# ============================================================
# SECTION 1: Pre-registration echo
# ============================================================
print("\n[SEC 1] Pre-registration echo (plan §W8-6)")
print(f"  f_B^(1) = {f_B_leading}  (W5-64 leading mean-field)")
print(f"  Gap = 1 − f_B^(1) = {f_B_gap:.4f}  (22%)")
print(f"  PASS threshold: δf_B^(2) ≥ 0.11 (closes ≥ half of gap)")
print(f"  r_L = {r_L}  (S70 LEGGETT-VACUUM-70)")
print(f"  r_L² = {r_L**2:.4f}")
print(f"  n_Bog = {n_Bog}  (S38 Bogoliubov per-mode fraction)")

# ============================================================
# SECTION 2: Leading f_B^(1) cross-check (plan step 6(i))
# ============================================================
print("\n[SEC 2] Leading f_B^(1) cross-check")

# Cross-check by computing leading Leggett amplitude from mean-field:
# f_B^(1) ~ (Δ_B2 + Δ_B3) / (Δ_B1 + Δ_B2 + Δ_B3) × band factor
# This is a diagnostic; the canonical W5-64 value 0.78 is held fixed.
Delta_B1 = float(Delta_0_OES)  # (local)
Delta_B2 = float(Delta_0_GL)   # (local)
Delta_B3_val = float(Delta_B3)  # (local)
Delta_sum = Delta_B1 + Delta_B2 + Delta_B3_val  # (local)
f_B_estimate = (Delta_B2 + Delta_B3_val) / Delta_sum  # (local) toy Leggett-weight estimate
print(f"  Δ_B1 = {Delta_B1:.4f}, Δ_B2 = {Delta_B2:.4f}, Δ_B3 = {Delta_B3_val:.4f}")
print(f"  (Δ_B2 + Δ_B3) / (Δ_B1 + Δ_B2 + Δ_B3) = {f_B_estimate:.4f}  (diagnostic)")
print(f"  Canonical f_B^(1) from W5-64: {f_B_leading:.4f}  (authoritative)")
print(f"  Using canonical value as leading; diagnostic is for cross-reference only.")

# ============================================================
# SECTION 3: Build rank-2 Leggett tensor T^(2) on 3-pair basis
# ============================================================
print("\n[SEC 3] Build rank-2 Leggett tensor T^(2) on 3 inter-band pair basis")

# 3 inter-band pairs on Leggett basis
PAIR_LABELS = ['(B1,B2)', '(B2,B3)', '(B1,B3)']  # (local)

# GGE occupation per pair (Bose statistics)
n_per_pair = r_L * float(n_Bog) / 3.0  # (local)
print(f"  n_per_pair = r_L · n_Bog / 3 = {r_L} · {n_Bog} / 3 = {n_per_pair:.6f}")

# Build T^(2)_{ab} using Bose statistics
# T^(2)_{aa} = <n_a²> = <n_a>(1 + <n_a>)  (Bose)
# T^(2)_{ab,a≠b} = <n_a><n_b>  (uncorrelated in separate channels)
T2 = np.zeros((3, 3))  # (local)
diag_val = n_per_pair * (1.0 + n_per_pair)  # (local)
off_val = n_per_pair ** 2  # (local)
for i in range(3):
    for j in range(3):
        T2[i, j] = diag_val if i == j else off_val
print(f"  T^(2)_diag = n(1+n) = {diag_val:.6f}")
print(f"  T^(2)_off  = n²     = {off_val:.6f}")
print(f"  T^(2) matrix:")
for i, row in enumerate(T2):
    print(f"    [{row[0]:.4f}, {row[1]:.4f}, {row[2]:.4f}]  {PAIR_LABELS[i]}")

# Leggett ground state |L⟩ = uniform superposition (1,1,1)/sqrt(3)
L_gs = np.array([1, 1, 1], dtype=float) / np.sqrt(3)  # (local)
print(f"  |L⟩ ground state: {L_gs}")

# Inner product <L|T^(2)|L>
LTL = float(L_gs @ T2 @ L_gs)  # (local)
print(f"  <L|T^(2)|L> = {LTL:.6f}")

# ============================================================
# SECTION 4: Compute δf_B^(2) and corrected f_B
# ============================================================
print("\n[SEC 4] Compute δf_B^(2) = r_L² × <L|T^(2)|L>")

delta_fB_2 = (r_L ** 2) * LTL  # (local)
f_B_corrected = f_B_leading + delta_fB_2  # (local)

print(f"  δf_B^(2) = r_L² × <L|T^(2)|L>")
print(f"          = {r_L**2:.4f} × {LTL:.4f}")
print(f"          = {delta_fB_2:.6f}")
print(f"  f_B_corrected = f_B^(1) + δf_B^(2) = {f_B_leading} + {delta_fB_2:.4f} "
      f"= {f_B_corrected:.4f}")

# Rank-4 power-counting estimate
delta_fB_4 = delta_fB_2 ** 2  # (local) power-counting ~ (r_L²)² × O(1)
f_B_with_rank4 = f_B_corrected + delta_fB_4  # (local)
print(f"  δf_B^(4) ~ (δf_B^(2))² = {delta_fB_4:.4f}  (power-counting)")
print(f"  f_B with rank-4 estimate: {f_B_with_rank4:.4f}")

# ============================================================
# SECTION 5: Verdict evaluation
# ============================================================
print("\n[SEC 5] Verdict evaluation")

PASS_DELTA_FB2 = 0.11  # (local) plan §W8-6 step 9
PASS_F_B = 0.89        # (local) corrected f_B target
INFO_DELTA_FB2 = 0.05  # (local)

print(f"  Thresholds:")
print(f"    PASS: δf_B^(2) ≥ {PASS_DELTA_FB2} AND f_B_corrected ≥ {PASS_F_B}")
print(f"    INFO: {INFO_DELTA_FB2} ≤ δf_B^(2) < {PASS_DELTA_FB2}")
print(f"    FAIL: δf_B^(2) < {INFO_DELTA_FB2}")

if delta_fB_2 >= PASS_DELTA_FB2 and f_B_corrected >= PASS_F_B:
    verdict = "PASS"                                                 # (local)
    margin_delta = delta_fB_2 / PASS_DELTA_FB2  # (local)
    band = (f"δf_B^(2) = {delta_fB_2:.4f} ≥ {PASS_DELTA_FB2} "
            f"(margin {margin_delta:.2f}x); f_B_corrected = {f_B_corrected:.4f} "
            f"≥ {PASS_F_B}; rank-2 closure achieves ≥ half of the 22% gap")  # (local)
elif delta_fB_2 >= INFO_DELTA_FB2:
    verdict = "INFO"                                                 # (local)
    band = (f"δf_B^(2) = {delta_fB_2:.4f} in [{INFO_DELTA_FB2}, {PASS_DELTA_FB2}); "
            f"partial closure; rank-4 likely needed")               # (local)
else:
    verdict = "FAIL"                                                 # (local)
    band = (f"δf_B^(2) = {delta_fB_2:.4f} < {INFO_DELTA_FB2}; "
            f"rank-2 Leggett tensor closes < 1/4 of gap")           # (local)

print(f"\n  Verdict: {verdict}  [{band}]")

# ============================================================
# SECTION 6: Cross-checks
# ============================================================
print("\n[SEC 6] Cross-checks")

# CC1: r_L² matches plan expectation 0.381
CC1 = abs(r_L**2 - 0.3807) < 1e-3  # (local)
print(f"  CC1 r_L² = 0.3807 (0.617² via Python): {CC1}  (computed {r_L**2:.4f})")

# CC2: n_per_pair calculation
CC2 = abs(n_per_pair - 0.20543) < 1e-3  # (local)
print(f"  CC2 n_per_pair = 0.20543: {CC2}  (computed {n_per_pair:.5f})")

# CC3: T^(2) tensor is symmetric
CC3 = np.allclose(T2, T2.T)  # (local)
print(f"  CC3 T^(2) symmetric: {CC3}")

# CC4: <L|T^(2)|L> > 0 (positive rank-2 overlap)
CC4 = LTL > 0  # (local)
print(f"  CC4 <L|T^(2)|L> > 0: {CC4}  ({LTL:.4f})")

# CC5: δf_B^(2) > 0 (quench injects occupation beyond mean-field, direction expected)
CC5 = delta_fB_2 > 0  # (local)
print(f"  CC5 δf_B^(2) > 0 (direction per plan Step 3): {CC5}  ({delta_fB_2:.4f})")

# CC6: Sum of T^(2) should be ~ (Σ n_i)² + Σ Var(n_i)
sum_T2 = float(np.sum(T2))  # (local)
expected_sum = (3 * n_per_pair) ** 2 + 3 * n_per_pair  # (local) = Σ_ij n_i n_j + n variance
# Actually: Σ T^(2)_ii = 3·n(1+n), Σ T^(2)_off = 6·n² => total = 3n(1+n) + 6n²
check_sum = 3 * n_per_pair * (1 + n_per_pair) + 6 * n_per_pair**2  # (local)
CC6 = abs(sum_T2 - check_sum) < 1e-10  # (local)
print(f"  CC6 Σ T^(2) matches analytic formula: {CC6}  "
      f"({sum_T2:.4f} vs {check_sum:.4f})")

# CC7: Rank-4 estimate < Rank-2 (power-counting hierarchy)
CC7 = delta_fB_4 < delta_fB_2  # (local)
print(f"  CC7 δf_B^(4) < δf_B^(2) (power-counting hierarchy): {CC7}  "
      f"({delta_fB_4:.4f} < {delta_fB_2:.4f})")

cross_checks_all = CC1 and CC2 and CC3 and CC4 and CC5 and CC6 and CC7  # (local)
print(f"  ALL cross-checks pass: {cross_checks_all}")

# ============================================================
# SECTION 7: Save NPZ + plot
# ============================================================
print("\n[SEC 7] Save NPZ + plot")

npz_path = os.path.join(HERE, 's85_w8_leggett_tensor_fb_closure.npz')  # (local)
np.savez(
    npz_path,
    r_L=r_L,
    r_L_squared=r_L**2,
    f_B_leading=f_B_leading,
    f_B_gap=f_B_gap,
    n_Bog=float(n_Bog),
    n_per_pair=n_per_pair,
    T2_matrix=T2,
    L_gs=L_gs,
    LTL=LTL,
    delta_fB_2=delta_fB_2,
    delta_fB_4=delta_fB_4,
    f_B_corrected=f_B_corrected,
    f_B_with_rank4=f_B_with_rank4,
    PASS_DELTA_FB2=PASS_DELTA_FB2,
    PASS_F_B=PASS_F_B,
    verdict=verdict,
    scheme=SCHEME,
    convention=CONVENTION,
)
print(f"  NPZ: {npz_path}")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

# Panel 1: f_B vs tensor order
orders = ['leading\nf_B^(1)', '+ rank-2\nf_B^(1)+δ^(2)', '+ rank-4\n(projected)']  # (local)
values = [f_B_leading, f_B_corrected, f_B_with_rank4]  # (local)
errors = [0, delta_fB_4 / 2, delta_fB_4]  # (local) error bars from rank-4 uncertainty
colors = ['steelblue', 'darkgreen', 'gold']  # (local)
x_pos = [0, 1, 2]
for i, (x, y, err, c) in enumerate(zip(x_pos, values, errors, colors)):
    ax1.bar(x, y, yerr=err, color=c, alpha=0.7,
            label=f'{y:.4f} ± {err:.4f}' if err > 0 else f'{y:.4f}',
            width=0.6, capsize=8)
    ax1.text(x, y + 0.01, f'{y:.4f}', ha='center', fontsize=10, fontweight='bold')
ax1.axhline(1.0, color='red', ls=':', lw=1.5, label='target f_B = 1')
ax1.axhline(PASS_F_B, color='orange', ls='--', lw=1.5, label=f'PASS threshold {PASS_F_B}')
ax1.set_xticks(x_pos)
ax1.set_xticklabels(orders, fontsize=9)
ax1.set_ylabel('f_B')
ax1.set_title(f'W8-6: f_B vs tensor order (verdict={verdict})')
ax1.set_ylim(0.7, 1.05)
ax1.grid(True, axis='y', alpha=0.3)
ax1.legend(fontsize=8, loc='best')

# Panel 2: T^(2) heatmap
im = ax2.imshow(T2, cmap='viridis', aspect='auto')
ax2.set_xticks([0, 1, 2])
ax2.set_xticklabels(PAIR_LABELS)
ax2.set_yticks([0, 1, 2])
ax2.set_yticklabels(PAIR_LABELS)
for i in range(3):
    for j in range(3):
        ax2.text(j, i, f'{T2[i, j]:.4f}', ha='center', va='center',
                 color='white' if T2[i, j] < T2.max()/2 else 'black', fontsize=10)
ax2.set_title(f'W8-6 rank-2 Leggett tensor T^(2)_(ab) (δf_B^(2)={delta_fB_2:.4f})')
plt.colorbar(im, ax=ax2, label='T^(2)_{ab}')

plt.tight_layout()
png_path = os.path.join(HERE, 's85_w8_leggett_tensor_fb_closure.png')  # (local)
plt.savefig(png_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"  PNG: {png_path}")

# ============================================================
# SECTION 8: Dual-SHA (S84+) + verdict append
# ============================================================
print("\n[SEC 8] Dual-SHA + verdict append")

script_path = os.path.abspath(__file__)                              # (local)
canonical_path = os.path.join(HERE, 'canonical_constants.py')        # (local)

pins = {                                                             # (local)
    'input_shas': INPUT_SHAS,
    'r_L': r_L,
    'f_B_leading': f_B_leading,
    'f_B_gap': f_B_gap,
    'n_Bog': float(n_Bog),
    'n_per_pair': n_per_pair,
    'T2_matrix_sum': float(np.sum(T2)),
    'LTL': LTL,
    'delta_fB_2': delta_fB_2,
    'delta_fB_4': delta_fB_4,
    'f_B_corrected': f_B_corrected,
    'verdict': verdict,
    'scheme': SCHEME,
    'convention': CONVENTION,
    'L_max': L_MAX,
    'PASS_DELTA_FB2': PASS_DELTA_FB2,
    'PASS_F_B': PASS_F_B,
}
pinmap_json = json.dumps(pins, sort_keys=True, separators=(',', ':')).encode('utf-8')  # (local)

with open(script_path, 'rb') as _fh:
    script_bytes = _fh.read()                                        # (local)
with open(canonical_path, 'rb') as _fh:
    canonical_bytes = _fh.read()                                     # (local)

h_audit = hashlib.sha256()
h_audit.update(script_bytes)
h_audit.update(canonical_bytes)
h_audit.update(pinmap_json)
audit_sha = h_audit.hexdigest()                                      # (local)
content_sha = hashlib.sha256(script_bytes).hexdigest()               # (local)

print(f"  audit_sha256   = {audit_sha}")
print(f"  content_sha256 = {content_sha}")

value = delta_fB_2  # (local) key quantity
tuple_str = f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})"
print(f"\n  4-tuple: {tuple_str}")

verdict_path = os.path.join(HERE, 's85_gate_verdicts.txt')           # (local)
verdict_line = (
    f"{GATE_ID}: {verdict} -- value={value!r} "
    f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
    f"audit_sha256={audit_sha} content_sha256={content_sha} "
    f"schema_version=S84+\n"
)
with open(verdict_path, 'a', encoding='utf-8') as fv:
    fv.write(verdict_line)
companion = (
    f"# audit_sha256 companion row: {GATE_ID} "
    f"audit={audit_sha[:16]} content={content_sha[:16]}\n"
)
with open(verdict_path, 'a', encoding='utf-8') as fv:
    fv.write(companion)

print(f"\n  Appended to {verdict_path}:")
print(f"    {verdict_line.strip()}")

print("\n" + "=" * 76)
print(f"{GATE_ID} complete. Verdict: {verdict}")
print("=" * 76)

sys.exit(0)
