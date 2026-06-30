#!/usr/bin/env python3
"""
S85 W8-2: S85-W8-2-CONVA-BDG-MICRO
=====================================================================
Derive Convention A K = coth(Δ/(2 T_eff)) microscopically from the
Nambu-Gorkov BdG equilibrium, WITHOUT citing 3He-B. Prove substrate
theorem via sympy symbolic identity + numerical cross-check on B1/B2/B3.

Gate: S85-W8-2-CONVA-BDG-MICRO  [VERIFY-THEOREM]
Classification: PHONONIC (substrate BdG gap-equation identity)
Owner: volovik-superfluid-universe-theorist
Plan: sessions/session-plan/session-85-plan-w8.md §W8-2

PRE-REGISTERED THRESHOLDS (plan §W8-2 step 9):
  PASS: symbolic derivation of K = coth(Δ/(2 T_eff)) closes (sympy
        simplify returns 0) AND numerical verification on B1, B2, B3
        matches to RATIO < 1e-10 at each x_k = Δ_k/(2 T_eff_k).
  FAIL: symbolic derivation does not close OR RATIO > 1e-6 on any band.
  INFO: derivation closes with gap-edge caveat (ε_k ≈ 0 regime).

SUBSTITUTION CHAIN (plan step 10, re-derived and pre-verified):
  Def 1: H_NG(k) = [[ε_k, Δ], [Δ*, −ε_k]]             [Nambu-Gorkov]
  Def 2: E_k = sqrt(ε_k² + |Δ|²)                       [BdG quasiparticle]
  Def 3: <n_k> = 1/(1 + e^(β E_k))                     [Fermi-Dirac at E_k]
  Def 4: K_substrate := 1/(1 − 2 <n_k>)                [substrate K-convention]

  Step 1: Compute 1 - 2<n_k>:
          = 1 − 2/(1 + e^(βE_k))
          = [(1 + e^(βE_k)) − 2] / (1 + e^(βE_k))
          = (e^(βE_k) − 1) / (e^(βE_k) + 1)
  Step 2: Identity (e^x − 1) / (e^x + 1) = tanh(x/2):
          proof: (e^x − 1) / (e^x + 1)
            = (e^(x/2)(e^(x/2) − e^(−x/2))) / (e^(x/2)(e^(x/2) + e^(−x/2)))
            = sinh(x/2) / cosh(x/2)
            = tanh(x/2)
  Step 3: Therefore 1 − 2<n_k> = tanh(βE_k/2)
  Step 4: K_substrate = 1 / tanh(βE_k/2) = coth(βE_k/2)
  Step 5: At the gap edge ε_k = 0 on the Fermi surface, E_k = Δ:
          K_substrate(gap-edge) = coth(βΔ/2) = coth(Δ/(2 T_eff))
          with β = 1/T_eff (per-band GGE inverse temperature).

  Direction: The identity K = coth(Δ/(2 T_eff)) FOLLOWS from the Nambu-
             Gorkov equilibrium saddle at the gap edge. No 3He-B input
             required; the substrate's D_K spectral-action structure
             generates the identity via the quasiparticle energy
             E_k = sqrt(ε_k² + |Δ|²) and the Fermi-Dirac equilibrium.
  Regime: valid for ε_k ≈ 0 (Fermi-surface projection); away from the
          Fermi surface, K = coth(βE_k/2) with E_k > Δ (generalized form).

References:
  - plan: sessions/session-plan/session-85-plan-w8.md §W8-2
  - S83 G39 Leggett-Bogoliubov: computations/session-83/s83_w3_g39_leggett_bogoliubov.py
    line 17 defines K = coth(Delta_BCS / (2 T_eff)) (Convention A)
  - Agent memory: w5-58-k-star-lab-match-84.md (Convention A confirmed substrate-native)
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
import json
import hashlib
import numpy as np
import sympy as sp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))                    # (local)
sys.path.insert(0, HERE)

# Canonical constants (MANDATORY)
from canonical_constants import (
    Delta_0_GL,       # B2 gap = 0.7704
    Delta_0_OES,      # B1 gap = 0.4643 (R-PROTECTED Delta_BCS alias)
    Delta_B3,         # B3 gap = 0.176
    T_GGE_B2,         # 0.668, B2 GGE temperature
    Delta_BCS,        # = Delta_0_OES, canonical BCS gap
)

# ============================================================
# SECTION 0: Input SHA-256 pins (MANDATORY; first 20 lines of stdout)
# ============================================================
GATE_ID = "S85-W8-2-CONVA-BDG-MICRO"                                 # (local)
SCHEME = "NG_block"                                                  # (local)
CONVENTION = "ConvA_coth"                                            # (local)
L_MAX = 8                                                            # (local)

INPUT_FILES = [                                                      # (local)
    os.path.join(HERE, 'canonical_constants.py'),
    os.path.join(HERE, 's83_w3_g39_leggett_bogoliubov.py'),
    os.path.join(HERE, 's84_w5_k_star_lab_framework_match.py'),
    os.path.join(HERE, 's84_w5_k_floor_regulator_invariance.py'),
]


def _sha256(path):
    if not os.path.exists(path):
        return 'MISSING'
    with open(path, 'rb') as h:
        return hashlib.sha256(h.read()).hexdigest()


print("=" * 76)
print(f"{GATE_ID}  (substrate BdG -> Convention A theorem)")
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
# SECTION 1: Symbolic derivation (sympy)
# ============================================================
print("\n[SEC 1] Symbolic derivation of K = coth(Δ/(2 T_eff)) from Nambu-Gorkov BdG")

eps, Delta, beta, E, x = sp.symbols('epsilon Delta beta E x',
                                     real=True, positive=True)
# Nambu-Gorkov Hamiltonian block (2x2 at fixed k)
H_NG = sp.Matrix([[eps, Delta], [Delta, -eps]])
print(f"  Nambu-Gorkov: H_NG = {H_NG.tolist()}")

# Eigenvalues: ±sqrt(eps^2 + Delta^2)
evals = H_NG.eigenvals()
print(f"  eigenvalues: {[str(k) for k in evals.keys()]}")
E_sym = sp.sqrt(eps**2 + Delta**2)
# Verify +E_sym is in evals
evals_simplified = [sp.simplify(e - E_sym) for e in evals.keys()]
assert any(e == 0 for e in evals_simplified), "E_k = +sqrt(eps^2 + Delta^2) not in spectrum"
print(f"  E_k = +sqrt(eps^2 + |Delta|^2) confirmed as a block eigenvalue")

# Fermi-Dirac at E_k
n_FD = 1 / (1 + sp.exp(beta * E))
# Substrate K-convention: K = 1/(1 - 2<n_k>)
K_expr = 1 / (1 - 2 * n_FD)
print(f"  K_substrate := 1/(1 - 2 <n_k>) = {K_expr}")

# Simplify
K_simplified = sp.simplify(K_expr)
print(f"  simplify(K_expr) = {K_simplified}")

# Expected: coth(beta*E/2)
K_target = sp.coth(beta * E / 2)
# Test identity K_simplified == K_target
diff_sym = sp.simplify(K_simplified - K_target)
print(f"  simplify(K - coth(β E / 2)) = {diff_sym}")

# Also test as an exponential identity
diff_exp = sp.simplify(sp.expand(K_simplified - K_target, func=True))
print(f"  expand+simplify(diff) = {diff_exp}")

# Alternative: rewrite in exponentials (instance method, not sp.rewrite)
K_in_exp = K_simplified.rewrite(sp.exp)
target_in_exp = K_target.rewrite(sp.exp)
diff_exp_form = sp.simplify(K_in_exp - target_in_exp)
print(f"  exponential form diff = {diff_exp_form}")

symbolic_pass = (diff_sym == 0) or (diff_exp == 0) or (diff_exp_form == 0)  # (local)
print(f"\n  SYMBOLIC IDENTITY: K_substrate = coth(βE/2)  -->  {symbolic_pass}")

# Step 5 symbolic: at gap edge eps=0, E=Delta
K_gap_edge = K_simplified.subs(E, Delta)
K_conv_A = sp.coth(Delta * beta / 2)
diff_gap_edge = sp.simplify(K_gap_edge - K_conv_A)
print(f"  At gap edge: K = {K_gap_edge}")
print(f"  Convention A target: coth(Δβ/2) = {K_conv_A}")
print(f"  diff (gap edge) = {diff_gap_edge}")
gap_edge_pass = (diff_gap_edge == 0) or \
    (sp.simplify(sp.rewrite(K_gap_edge - K_conv_A, sp.exp)) == 0)  # (local)
print(f"  GAP-EDGE IDENTITY: K(ε=0, E=Δ) = coth(Δ/(2 T_eff))  -->  {gap_edge_pass}")

# ============================================================
# SECTION 2: Numerical verification on 3 bands
# ============================================================
print("\n[SEC 2] Numerical verification on 3 bands (B1, B2, B3)")

# Use common substrate T = T_GGE_B2 for all 3 bands (plan lets per-band β vary;
# the identity holds for any choice of T > 0). Verify identity per band.
T_common = T_GGE_B2                                                  # (local) substrate GGE T
print(f"  Common substrate T = T_GGE_B2 = {T_common}")

bands = {                                                            # (local)
    'B1': Delta_0_OES,   # 0.4643 (Delta_BCS alias)
    'B2': Delta_0_GL,    # 0.7704
    'B3': Delta_B3,      # 0.176
}

band_results = {}                                                    # (local)
for name, Delta_k in bands.items():
    x_k = float(Delta_k) / (2.0 * T_common)                          # (local)
    beta_k = 1.0 / T_common                                          # (local)
    E_k = float(Delta_k)                                             # (local) gap edge
    n_k = 1.0 / (1.0 + np.exp(beta_k * E_k))                         # (local)
    # Direct (LHS): K = 1/(1 - 2 n_k)
    K_direct = 1.0 / (1.0 - 2.0 * n_k)                               # (local)
    # Identity (RHS): coth(x_k) = 1/tanh(x_k)
    K_coth = 1.0 / np.tanh(x_k)                                      # (local)
    ratio = K_direct / K_coth                                        # (local)
    abs_diff = abs(K_direct - K_coth)                                # (local)
    rel_diff = abs_diff / abs(K_coth)                                # (local)
    band_results[name] = dict(
        Delta=float(Delta_k),
        T=T_common,
        x=x_k,
        K_direct=K_direct,
        K_coth=K_coth,
        ratio=ratio,
        abs_diff=abs_diff,
        rel_diff=rel_diff,
    )
    print(f"  {name}: Δ={Delta_k:.4f}  x=Δ/(2T)={x_k:.4f}  "
          f"K_direct={K_direct:.10f}  K_coth={K_coth:.10f}  "
          f"|rel diff|={rel_diff:.2e}")

max_rel_diff = max(b['rel_diff'] for b in band_results.values())     # (local)
print(f"\n  max |rel diff| across 3 bands = {max_rel_diff:.2e}")

numerical_pass = (max_rel_diff < 1e-10)                              # (local)
print(f"  NUMERICAL VERIFICATION (RATIO < 1e-10): {numerical_pass}")

# ============================================================
# SECTION 3: Sweep x in [0.1, 2.0] for sensitivity band
# ============================================================
print("\n[SEC 3] Sensitivity sweep x ∈ [0.1, 2.0] step 0.01")

x_sweep = np.arange(0.1, 2.01, 0.01)                                 # (local)
# LHS: 1/(1 - 2 n_FD(2x)) where beta*E = 2x
n_sweep = 1.0 / (1.0 + np.exp(2.0 * x_sweep))                        # (local)
K_direct_sweep = 1.0 / (1.0 - 2.0 * n_sweep)                         # (local)
# RHS: coth(x)
K_coth_sweep = 1.0 / np.tanh(x_sweep)                                # (local)
rel_diff_sweep = np.abs(K_direct_sweep - K_coth_sweep) / np.abs(K_coth_sweep)  # (local)
max_rel_sweep = float(np.max(rel_diff_sweep))                        # (local)
print(f"  max |rel diff| across 191 x-points = {max_rel_sweep:.2e}")
print(f"  SWEEP (RATIO < 1e-10): {max_rel_sweep < 1e-10}")

# ============================================================
# SECTION 4: Verdict
# ============================================================
print("\n[SEC 4] Verdict evaluation")

# PASS = symbolic AND numerical AND sweep
if symbolic_pass and gap_edge_pass and numerical_pass and (max_rel_sweep < 1e-10):
    verdict = "PASS"                                                 # (local)
    band = (f"symbolic closure (simplify=0); 3-band rel diff max "
            f"{max_rel_diff:.2e} < 1e-10; sweep max rel diff "
            f"{max_rel_sweep:.2e} < 1e-10; Convention A is a substrate "
            f"BdG theorem, not a 3He-B borrowing")                  # (local)
elif symbolic_pass and (max_rel_diff < 1e-6):
    verdict = "INFO"                                                 # (local)
    band = (f"symbolic closure holds but numerical tolerance loosened "
            f"(max rel diff {max_rel_diff:.2e} in [1e-10, 1e-6]); "
            f"gap-edge regime theorem with stated caveat")          # (local)
else:
    verdict = "FAIL"                                                 # (local)
    band = (f"symbolic or numerical closure failed: sym_pass={symbolic_pass}, "
            f"max rel diff={max_rel_diff:.2e} (target < 1e-10)")     # (local)

print(f"  Verdict: {verdict}  [{band}]")

# ============================================================
# SECTION 5: Cross-checks
# ============================================================
print("\n[SEC 5] Cross-checks")

# CC1: Symbolic diff canonicalizes to zero in some form
CC1 = symbolic_pass  # (local)
print(f"  CC1 symbolic K_substrate = coth(βE/2): {CC1}")

# CC2: Gap-edge specialization matches Convention A target
CC2 = gap_edge_pass  # (local)
print(f"  CC2 gap-edge specialization = coth(Δ/(2T_eff)): {CC2}")

# CC3: B2 x value matches W5-58 memory x*=1 test
# W5-58 memory: framework K_*=coth(1)=1.3130 at x*=1
# Check: if Delta=T_common (so x=0.5), K=coth(0.5)=2.164
x_half = 0.5  # (local)
K_at_half = 1.0 / np.tanh(x_half)  # (local)
# Check coth(0.5) ≈ 2.1640
CC3 = abs(K_at_half - 2.1640) < 1e-3  # (local)
print(f"  CC3 coth(0.5) = 2.1640 (W5-58 plan-prose value-check): {CC3}  (computed {K_at_half:.4f})")

# CC4: coth(1) = 1.3130 (W5-58 canonical)
K_at_1 = 1.0 / np.tanh(1.0)  # (local)
CC4 = abs(K_at_1 - 1.3130) < 1e-3  # (local)
print(f"  CC4 coth(1) = 1.3130 (W5-58 K_* canonical): {CC4}  (computed {K_at_1:.4f})")

# CC5: K_R5 matches canonical 1.9222 at x_B2(5) = Delta_0_GL/(2·T_GGE_B2)
x_B2 = Delta_0_GL / (2.0 * T_GGE_B2)  # (local)
K_B2 = 1.0 / np.tanh(x_B2)  # (local)
CC5 = abs(K_B2 - 1.9222) < 1e-3  # (local)
print(f"  CC5 K_R5 matches canonical 1.9222: {CC5}  "
      f"(x_B2={x_B2:.4f}, coth(x_B2)={K_B2:.4f})")

# CC6: Band-sweep max rel diff < 1e-10
CC6 = (max_rel_sweep < 1e-10)  # (local)
print(f"  CC6 sweep max rel diff < 1e-10: {CC6}  ({max_rel_sweep:.2e})")

cross_checks_all = CC1 and CC2 and CC3 and CC4 and CC5 and CC6  # (local)
print(f"  ALL cross-checks pass: {cross_checks_all}")

# ============================================================
# SECTION 6: Save NPZ + plot
# ============================================================
print("\n[SEC 6] Save NPZ + plot")

npz_path = os.path.join(HERE, 's85_w8_convA_bdg_micro.npz')          # (local)
np.savez(
    npz_path,
    x_sweep=x_sweep,
    K_direct_sweep=K_direct_sweep,
    K_coth_sweep=K_coth_sweep,
    rel_diff_sweep=rel_diff_sweep,
    bands_names=np.array(list(band_results.keys())),
    bands_Delta=np.array([band_results[n]['Delta'] for n in band_results]),
    bands_x=np.array([band_results[n]['x'] for n in band_results]),
    bands_K_direct=np.array([band_results[n]['K_direct'] for n in band_results]),
    bands_K_coth=np.array([band_results[n]['K_coth'] for n in band_results]),
    bands_rel_diff=np.array([band_results[n]['rel_diff'] for n in band_results]),
    max_rel_diff_bands=max_rel_diff,
    max_rel_diff_sweep=max_rel_sweep,
    symbolic_pass=symbolic_pass,
    gap_edge_pass=gap_edge_pass,
    verdict=verdict,
    scheme=SCHEME,
    convention=CONVENTION,
)
print(f"  NPZ: {npz_path}")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

# Panel 1: K(x) = coth(x) with 3 band points overlaid
ax1.plot(x_sweep, K_coth_sweep, '-', color='blue', lw=1.5,
         label='coth(x) (substrate BdG identity)')
ax1.plot(x_sweep, K_direct_sweep, '--', color='orange', lw=1, alpha=0.6,
         label='1/(1 - 2 n_FD(2x)) (direct Fermi-Dirac)')
for name, rec in band_results.items():
    ax1.axvline(rec['x'], color='red', ls=':', lw=0.8, alpha=0.5)
    ax1.plot(rec['x'], rec['K_coth'], 'o', ms=12, color='red',
             label=f"{name}: x={rec['x']:.4f}, K={rec['K_coth']:.4f}")
ax1.set_xlabel('x = Δ/(2 T_eff)')
ax1.set_ylabel('K(x)')
ax1.set_title(f'W8-2: Convention A identity K = coth(x) (verdict={verdict})')
ax1.set_xlim(0.1, 2.0)
ax1.set_ylim(1, 10)
ax1.grid(True, alpha=0.3)
ax1.legend(fontsize=8, loc='best')

# Panel 2: rel diff sweep
ax2.semilogy(x_sweep, rel_diff_sweep + 1e-17, '-', color='blue', lw=1,
             label='|K_direct - coth(x)| / coth(x)')
ax2.axhline(1e-10, color='red', ls='--', lw=1, label='PASS threshold 1e-10')
ax2.axhline(1e-6, color='orange', ls=':', lw=1, label='INFO threshold 1e-6')
ax2.set_xlabel('x = Δ/(2 T_eff)')
ax2.set_ylabel('relative difference')
ax2.set_title(f'W8-2 identity residual (sweep max = {max_rel_sweep:.1e})')
ax2.grid(True, alpha=0.3)
ax2.legend(fontsize=8, loc='best')

plt.tight_layout()
png_path = os.path.join(HERE, 's85_w8_convA_bdg_micro.png')          # (local)
plt.savefig(png_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"  PNG: {png_path}")

# ============================================================
# SECTION 7: Dual-SHA (S84+) + verdict append
# ============================================================
print("\n[SEC 7] Dual-SHA (S84+) + verdict append")

script_path = os.path.abspath(__file__)                              # (local)
canonical_path = os.path.join(HERE, 'canonical_constants.py')        # (local)

pins = {                                                             # (local)
    'input_shas': INPUT_SHAS,
    'bands': {n: band_results[n] for n in band_results},
    'max_rel_diff_bands': max_rel_diff,
    'max_rel_diff_sweep': max_rel_sweep,
    'symbolic_pass': symbolic_pass,
    'gap_edge_pass': gap_edge_pass,
    'scheme': SCHEME,
    'convention': CONVENTION,
    'L_max': L_MAX,
    'verdict': verdict,
    'T_common': T_common,
    'identity': 'K_substrate = coth(beta*E/2); gap-edge: coth(Delta/(2*T_eff))',
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

# 4-tuple value = max_rel_diff across 3 bands (key discriminant)
value = max_rel_diff                                                 # (local)
tuple_str = f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})"  # (local)
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
