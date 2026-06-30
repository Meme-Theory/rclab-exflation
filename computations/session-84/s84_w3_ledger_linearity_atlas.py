"""
S84 W3-25 — S84-LEDGER-LINEARITY-ATLAS
Agent: lizzi-spectral-functional-theorist

Hypothesis (per plan §W3-25):
  Every ledger observable O in {A_s, mu, f_NL, r} is a CC-5 composite of the
  4 primary factors {H_tilde, eps_H, k_a2 (a_2 slot), f_conv}, so
    ln O(f_1,...,f_4) is linear in ln f_k
  with integer/half-integer exponents p_k = d ln O / d ln f_k.

PASS: deviation from nearest half-integer < 0.05 on all 16 p-coefficients AND
      predicted span(O) = prod_k span(f_k)^{|p_k|} matches direct span to < 2%.

Substitution chain (pre-compute):
  Step 1. Definitions (UNIFIED-AS-79 branch, TD-framework zeta):
    A_s       = (H_tilde^2 / 8 pi^2) * (1/eps_H) * F_amp * (1/c_sub) * f_conv
                with F_amp = F_amp_3PI_pivot * k_a2
    mu (SR)   := H_tilde               (ledger-level primary mass scale)
    f_NL      := (5/12) * eps_H        (SR local-shape leading)
    r         := 16 * eps_H            (SR tensor-to-scalar)

  Step 2. ln-derivatives at canonical pin:
    p_k(O) := d ln O / d ln f_k

  Step 3. From Step-1 forms (analytic prediction):
    ln A_s  = 2 ln H_tilde + (-1) ln eps_H + 1*ln k_a2 + 1*ln f_conv + const
              => p = ( +2, -1, +1, +1 )
    ln mu   = 1 ln H_tilde + 0 + 0 + 0   => p = ( +1, 0, 0, 0 )
    ln f_NL = 0 + 1 ln eps_H + 0 + 0     => p = ( 0, +1, 0, 0 )
    ln r    = 0 + 1 ln eps_H + 0 + 0     => p = ( 0, +1, 0, 0 )

  Step 4. Direction:
    p>0 => observable inherits span proportionally;
    p<0 => observable inherits inverse span.

  Step 5. Finite-difference numerical extraction verifies Step-3 identity.

Output: 4x4 p-matrix {A_s,mu,f_NL,r} x {H_tilde,eps_H,k_a2,f_conv}.
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import hashlib
import json
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    A_s_CMB,
    M_KK_gravity,
    M_Pl_reduced,
)

SCRIPT_DIR = Path(__file__).resolve().parent

# =============================================================================
# SECTION 0 — CANONICAL PIN (mirrors s83_w2_g16_unified_as79_3pi_subst.py)
# =============================================================================
H_tilde_TD      = 5.90760e-03     # (local) S80 W1-1 TD-framework (zeta, L_max=3)
eps_H           = 0.02163         # (local) S80 plan line 895, 1-loop slow-roll
c_sub           = 2.238           # (local) S78 W2-E central
f_conv_pin      = 9.30e-4         # (local) (M_KK/M_Pl_red)^2 hierarchy
F_amp_3PI_pivot = 1.02578407761463 # (local) G7 PASS
k_a2_pin        = 0.58297862384968670  # (local) G15 Conv A, zeta

# Factor spans from W3-21 atlas + canonical auxiliary ledgers
span_k_a2   = 14.685053713396265  # (local) W3-21 §VII.K slot span (5-regulator)
span_M0     = 42.02573406376081   # (local) W3-21 slot span (used for f_conv)
# f_conv = <sqrt(x)> / (16 pi^2 M_0^2), <sqrt(x)> span=1 under R-protection
# => span(f_conv) = span(M_0)^2 = 42.02573... ^ 2
span_f_conv = span_M0**2          # (local) CC-5 composition
# H_tilde span across 2 canonical branches (TD vs LI): 5.9076e-3 / 2.46411e-5
span_H_tilde = 5.90760e-03 / 2.46411e-05   # (local) S82 W1-1 LI branch split
# eps_H is branch-universal at canonical pin (S80 plan line 895 unique)
# but across Planck prior [0.0067, 0.0217] we take a 1-sigma span:
span_eps_H  = 0.02163 / 0.00670   # (local) Planck 1-sigma SR band

L_MAX      = 5                # (local) plan machinery pin
SCHEME     = 'zeta'
CONVENTION = 'unified-as-79-ledger'
PASS_HALFINT_TOL = 0.05       # (local) plan tolerance
PASS_SPAN_REL    = 0.02       # (local) 2% span match

# =============================================================================
# SECTION 1 — INPUT PINS
# =============================================================================
def _sha256_file(path: Path) -> str:
    if not path.is_file():
        return 'MISSING'
    h = hashlib.sha256()
    with open(path, 'rb') as fh:
        for chunk in iter(lambda: fh.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()

input_pins = {
    's83_w2_g16_unified_as79_3pi_subst.npz': _sha256_file(
        SCRIPT_DIR / 's83_w2_g16_unified_as79_3pi_subst.npz'),
    's84_w3_vii_k_prop_atlas.json': _sha256_file(
        SCRIPT_DIR / 's84_w3_vii_k_prop_atlas.json'),
    'canonical_constants.py': _sha256_file(SCRIPT_DIR / 'canonical_constants.py'),
}
_ordered_pin_string = ';'.join(f'{k}={v}' for k, v in sorted(input_pins.items()))
closure_sha = hashlib.sha256(_ordered_pin_string.encode('utf-8')).hexdigest()

print('=' * 78)
print('S84 W3-25 — LEDGER-LINEARITY-ATLAS')
print('=' * 78)
for k, v in input_pins.items():
    print(f'  {k:<45s} = {v[:16]}...')
print(f'Closure SHA = {closure_sha}')
print('-' * 78)

# =============================================================================
# SECTION 2 — OBSERVABLE DEFINITIONS
# =============================================================================
def A_s_ledger(H_tilde, eps, k_a2, f_conv):
    """A_s(H_tilde, eps_H, k_a2, f_conv) — UNIFIED-AS-79 with 3PI substitution."""
    F_amp = F_amp_3PI_pivot * k_a2                                  # (local)
    return (H_tilde**2 / (8.0 * np.pi**2)) * (1.0/eps) * F_amp * (1.0/c_sub) * f_conv

def mu_ledger(H_tilde, eps, k_a2, f_conv):
    """SR mass scale proxy := H_tilde."""
    return H_tilde

def fNL_ledger(H_tilde, eps, k_a2, f_conv):
    """Local non-Gaussianity leading shape := (5/12) * eps_H."""
    return (5.0/12.0) * eps

def r_ledger(H_tilde, eps, k_a2, f_conv):
    """Tensor-to-scalar ratio, SR consistency := 16 * eps_H."""
    return 16.0 * eps

observables = [
    ('A_s',  A_s_ledger),
    ('mu',   mu_ledger),
    ('f_NL', fNL_ledger),
    ('r',    r_ledger),
]
factors = [
    ('H_tilde', H_tilde_TD, span_H_tilde),
    ('eps_H',   eps_H,      span_eps_H),
    ('k_a2',    k_a2_pin,   span_k_a2),
    ('f_conv',  f_conv_pin, span_f_conv),
]

# =============================================================================
# SECTION 3 — CENTRAL FINITE-DIFFERENCE p-MATRIX
# =============================================================================
# p_k(O) = [ ln O(f_k * 1.01) - ln O(f_k * 0.99) ] / [ ln(1.01) - ln(0.99) ]

DELTA = 0.01  # (local) +/- 1% perturbation per plan
ln_step = np.log(1.0 + DELTA) - np.log(1.0 - DELTA)     # (local)

pin_vals = [H_tilde_TD, eps_H, k_a2_pin, f_conv_pin]    # (local)

p_matrix = np.zeros((len(observables), len(factors)))   # (local)
dev_matrix = np.zeros_like(p_matrix)                    # (local)

print('\nSECTION 3 — Finite-difference p-matrix')
print('-' * 78)
print(f'{"O":<6s} {"H_tilde":>10s} {"eps_H":>10s} {"k_a2":>10s} {"f_conv":>10s}')

for i, (oname, ofunc) in enumerate(observables):
    row_vals = []
    for j, (fname, fpin, fspan) in enumerate(factors):
        args_plus  = list(pin_vals); args_plus[j]  = fpin * (1.0 + DELTA)
        args_minus = list(pin_vals); args_minus[j] = fpin * (1.0 - DELTA)
        O_plus  = ofunc(*args_plus)                    # (local)
        O_minus = ofunc(*args_minus)                   # (local)
        p = (np.log(O_plus) - np.log(O_minus)) / ln_step  # (local)
        p_matrix[i, j] = p
        # Nearest half-integer
        p_half = np.round(p * 2.0) / 2.0               # (local)
        dev = abs(p - p_half)                          # (local)
        dev_matrix[i, j] = dev
        row_vals.append(p)
    print(f'{oname:<6s} ' + ' '.join(f'{v:+10.4f}' for v in row_vals))

print('\nDeviation from nearest half-integer:')
print(f'{"O":<6s} {"H_tilde":>10s} {"eps_H":>10s} {"k_a2":>10s} {"f_conv":>10s}')
for i, (oname, _) in enumerate(observables):
    print(f'{oname:<6s} ' + ' '.join(f'{dev_matrix[i,j]:10.2e}' for j in range(len(factors))))

max_dev = float(dev_matrix.max())                       # (local)
pass_halfint = bool(max_dev < PASS_HALFINT_TOL)         # (local)

# =============================================================================
# SECTION 4 — SPAN PREDICTION VS DIRECT
# =============================================================================
# span_pred(O) = prod_k span(f_k)^{|p_k|}
# span_direct(O): scan each factor across its span range (1-D bounding box)
#   and take max(O)/min(O) across the 4-factor corner scan.

print('\nSECTION 4 — Span prediction vs direct')
print('-' * 78)

factor_spans = np.array([fspan for _, _, fspan in factors])  # (local)

# Direct span: for each observable, scan at corners of the 4-D factor box
# Build box: each factor takes value in [pin / sqrt(span), pin * sqrt(span)]
# so that ratio (max/min) per factor = span.
box_lo = np.array([fpin / np.sqrt(fspan) for _, fpin, fspan in factors])   # (local)
box_hi = np.array([fpin * np.sqrt(fspan) for _, fpin, fspan in factors])   # (local)

span_pred_arr   = np.zeros(len(observables))  # (local)
span_direct_arr = np.zeros(len(observables))  # (local)
span_rel_err    = np.zeros(len(observables))  # (local)

print(f'{"O":<6s} {"span_pred":>14s} {"span_direct":>14s} {"rel_err":>10s} {"verdict":>8s}')
for i, (oname, ofunc) in enumerate(observables):
    p_round = np.round(p_matrix[i, :] * 2.0) / 2.0     # (local) half-int rounded
    span_pred = float(np.prod(factor_spans ** np.abs(p_round)))  # (local)
    # Direct: scan 2^4=16 corners
    vals = []
    for mask in range(16):
        args = [box_hi[k] if (mask >> k) & 1 else box_lo[k] for k in range(4)]
        vals.append(ofunc(*args))
    vals = np.array(vals)
    # Handle sign-definite observables (all positive here)
    vals_pos = vals[vals > 0]
    span_direct = float(vals_pos.max() / vals_pos.min())  # (local)
    rel_err = abs(span_pred - span_direct) / span_direct  # (local)
    verdict = 'PASS' if rel_err < PASS_SPAN_REL else 'FAIL'  # (local)
    span_pred_arr[i]   = span_pred
    span_direct_arr[i] = span_direct
    span_rel_err[i]    = rel_err
    print(f'{oname:<6s} {span_pred:14.4e} {span_direct:14.4e} {rel_err:10.2e} {verdict:>8s}')

max_span_err = float(span_rel_err.max())   # (local)
pass_span = bool(max_span_err < PASS_SPAN_REL)    # (local)

# =============================================================================
# SECTION 5 — OVERALL VERDICT
# =============================================================================
if pass_halfint and pass_span:
    VERDICT = 'PASS'
elif (not pass_halfint) or (not pass_span):
    # INFO if 3/4 observables pass
    per_obs_pass_halfint = (dev_matrix.max(axis=1) < PASS_HALFINT_TOL)   # (local)
    per_obs_pass_span    = (span_rel_err < PASS_SPAN_REL)                # (local)
    per_obs_pass = per_obs_pass_halfint & per_obs_pass_span
    n_pass = int(per_obs_pass.sum())                                     # (local)
    if n_pass == 3:
        VERDICT = 'INFO'
    else:
        VERDICT = 'FAIL'
else:
    VERDICT = 'FAIL'

print('\n' + '=' * 78)
print('SECTION 5 — VERDICT')
print('=' * 78)
print(f'  pass_halfint (max_dev < {PASS_HALFINT_TOL})   = {pass_halfint}  (max_dev={max_dev:.2e})')
print(f'  pass_span    (max_rel_err < {PASS_SPAN_REL})   = {pass_span}  (max_rel_err={max_span_err:.2e})')
print(f'  VERDICT = {VERDICT}')

# =============================================================================
# SECTION 6 — OUTPUT: NPZ + JSON + PLOT
# =============================================================================
np.savez_compressed(
    SCRIPT_DIR / 's84_w3_ledger_linearity_atlas.npz',
    p_matrix=p_matrix,
    dev_matrix=dev_matrix,
    span_pred_arr=span_pred_arr,
    span_direct_arr=span_direct_arr,
    span_rel_err=span_rel_err,
    factor_names=np.array([n for n, _, _ in factors]),
    observable_names=np.array([n for n, _ in observables]),
    factor_spans=factor_spans,
    closure_sha=closure_sha,
    verdict=VERDICT,
)

out_json = {
    'meta': {
        'gate_id': 'S84-LEDGER-LINEARITY-ATLAS',
        'session': 84,
        'agent': 'lizzi-spectral-functional-theorist',
        'scheme': SCHEME,
        'convention': CONVENTION,
        'L_max': L_MAX,
        'verdict': VERDICT,
        'max_halfint_dev': max_dev,
        'max_span_rel_err': max_span_err,
        'closure_sha': closure_sha,
        'input_pins': input_pins,
    },
    'observables': [n for n, _ in observables],
    'factors':    [n for n, _, _ in factors],
    'factor_spans': factor_spans.tolist(),
    'p_matrix':    p_matrix.tolist(),
    'dev_matrix':  dev_matrix.tolist(),
    'span_pred':   span_pred_arr.tolist(),
    'span_direct': span_direct_arr.tolist(),
    'span_rel_err': span_rel_err.tolist(),
}
with open(SCRIPT_DIR / 's84_w3_ledger_linearity_atlas.json', 'w') as fh:
    json.dump(out_json, fh, indent=2)

# Plot: p-matrix heatmap
fig, ax = plt.subplots(figsize=(7, 5))
im = ax.imshow(p_matrix, cmap='RdBu_r', vmin=-2.5, vmax=2.5, aspect='auto')
ax.set_xticks(range(len(factors)))
ax.set_xticklabels([n for n, _, _ in factors])
ax.set_yticks(range(len(observables)))
ax.set_yticklabels([n for n, _ in observables])
for i in range(len(observables)):
    for j in range(len(factors)):
        ax.text(j, i, f'{p_matrix[i,j]:+.2f}', ha='center', va='center',
                color='black' if abs(p_matrix[i,j]) < 1.5 else 'white', fontsize=11)
ax.set_title(f'S84 W3-25 Ledger-Linearity p-matrix\nverdict={VERDICT}  max_dev={max_dev:.2e}')
fig.colorbar(im, ax=ax, label='p_k = d ln O / d ln f_k')
fig.tight_layout()
fig.savefig(SCRIPT_DIR / 's84_w3_ledger_linearity_atlas.png', dpi=120)

# =============================================================================
# SECTION 7 — VERDICT LINE (canonical format)
# =============================================================================
value_tag = f'max_halfint_dev={max_dev:.3e},max_span_rel_err={max_span_err:.3e}'
print('\n' + '-' * 78)
print('4-TUPLE:')
print(f'  (value={value_tag}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})')
print('\nVERDICT LINE:')
print(f'S84-LEDGER-LINEARITY-ATLAS: {VERDICT} -- value={value_tag} '
      f'scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} sha256={closure_sha}')
