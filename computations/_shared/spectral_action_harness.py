"""
T3 harness for spectral_action.py (GATE: T3-SPECTRAL-ACTION)

Purpose: Exercise the core spectral action machinery at the pinned
L_max = max_pq_sum = 3, capture Seeley-DeWitt coefficients (a_0, a_2, a_4),
exact Levi-Civita R(s) at s in {0, tau_fold, 1.0}, and the spectral action
values at the canonical cutoff Lambda=5.0.

Reads from:
  - spectral_action.py  (heat kernel, SD extraction, scalar curvature)
  - dirac_spectrum.py   (SU(3) generators, Dirac spectrum on Jensen metric)
  - canonical_constants.py    (tau_fold, Vol_SU3_Haar)

Substitution chain for R/a_2 direction (Einstein-Hilbert link):
  Step 1: a_2 = (spinor_rank) * R * Vol / (6 * (4pi)^(d/2))   [Gilkey, spin bundle, d=8]
  Step 2: a_0 = (spinor_rank) * Vol       / (4pi)^(d/2)
  Step 3: a_2/a_0 = R/6                                         [cancellation]
  Step 4: R(s) from Levi-Civita connection (exact, no truncation)
  Step 5: Einstein-Hilbert S_EH = (1/(16 pi G)) * integral R * sqrt(g) dvol,
          so a_2 proportional to Newton-constant coefficient (gravity is the
          SECOND spectral moment, not the zeroth).
  Direction: R(fold=0.19) > R(0)  =>  a_2(fold) > a_2(0) for fixed volume.
"""
import os
import sys
import hashlib
import json
import numpy as np

# Cap CPU threads — script uses numpy.linalg.eigvalsh on small (48x48) blocks
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

ROOT = r'C:\sandbox\Ainulindale Exflation\computations'
sys.path.insert(0, ROOT)

from canonical_constants import tau_fold, Vol_SU3_Haar

from dirac_spectrum import (
    su3_generators, compute_structure_constants, build_cliff8,
    validate_clifford, su2_benchmark, collect_spectrum
)
from spectral_action import (
    compute_heat_kernel, extract_seeley_dewitt, extract_seeley_dewitt_robust,
    spectral_action_smooth_cutoff, scalar_curvature_from_connection,
    scalar_curvature_analytical, check_volume_preservation, weyl_law_check,
    dim_su3_irrep
)

# =============================================================================
# T3 PIN BLOCK — log input SHAs first (first 20 lines of stdout)
# =============================================================================
PIN_FILES = [
    'spectral_action.py',
    'dirac_spectrum.py',
    'canonical_constants.py',
]

pin_map = {}
for f in PIN_FILES:
    with open(os.path.join(ROOT, f), 'rb') as fh:
        pin_map[f] = hashlib.sha256(fh.read()).hexdigest()

print('=' * 80)
print('T3-SPECTRAL-ACTION HARNESS')
print('=' * 80)
print('INPUT SHA-256 PINS:')
for f, h in pin_map.items():
    print(f'  {f}: {h}')

# Parameter pins
MAX_PQ_SUM = 3           # (local) L_max pin for SU(3) irrep truncation
LAMBDA_CUT = 5.0         # (local) spectral action cutoff (matches main script)
T_RANGE = (0.01, 0.5)    # (local) Seeley-DeWitt fit range
N_POINTS_SD = 200        # (local) grid density for SD fit
S_PROBE = [0.0, tau_fold, 0.50, 1.0]  # (local) s-values for R(s) probe

print('PARAMETER PINS:')
print(f'  max_pq_sum (L_max)    = {MAX_PQ_SUM}')
print(f'  Lambda (cutoff)       = {LAMBDA_CUT}')
print(f'  SD fit t-range        = {T_RANGE}')
print(f'  SD fit grid points    = {N_POINTS_SD}')
print(f'  s-probe               = {S_PROBE}')
print(f'  tau_fold (canonical)  = {tau_fold}')
print(f'  Vol_SU3_Haar          = {Vol_SU3_Haar:.6f}')
print('=' * 80)

# =============================================================================
# [1] Infrastructure
# =============================================================================
gens = su3_generators()
f_abc = compute_structure_constants(gens)
gammas = build_cliff8()

cliff_err = validate_clifford(gammas)
su2_ok, su2_err = su2_benchmark()
print(f'[1] Clifford error: {cliff_err:.2e}')
print(f'[1] SU(2) Dirac benchmark: {"PASS" if su2_ok else "FAIL"} (err={su2_err:.2e})')

# =============================================================================
# [2] Volume preservation (should be exactly 1.0)
# =============================================================================
s_test = np.linspace(-0.5, 1.0, 7)
det_ratios = check_volume_preservation(s_test, f_abc, verbose=False)
vol_max_err = float(np.max(np.abs(det_ratios - 1.0)))  # (local)
print(f'[2] Volume preservation max |det(g_s)/det(g_0) - 1| = {vol_max_err:.2e}')

# =============================================================================
# [3] Exact scalar curvature R(s) at pinned s-values
# =============================================================================
print('[3] Exact Levi-Civita scalar curvature R(s) (no truncation):')
R_values = {}
for s in S_PROBE:
    R, _ = scalar_curvature_from_connection(float(s), f_abc)
    R_values[s] = float(R)
    R_analytic = scalar_curvature_analytical(float(s))  # (local) Baptista ratio
    print(f'  s={s:.4f}: R_exact={R:.6f}   R(s)/R(0)_analytic={R_analytic:.6f}')

R_fold_ratio = R_values[tau_fold] / R_values[0.0]  # (local) direction check
print(f'  R(fold)/R(0) = {R_fold_ratio:.6f}   (analytic: '
      f'{scalar_curvature_analytical(tau_fold):.6f})')

# =============================================================================
# [4] Dirac spectrum + heat kernel at s=0 and s=tau_fold
# =============================================================================
print('[4] Computing Dirac spectrum (max_pq_sum=%d) at s in {0, tau_fold}...' % MAX_PQ_SUM)
_, eval_data_0 = collect_spectrum(0.0, gens, f_abc, gammas,
                                   max_pq_sum=MAX_PQ_SUM, verbose=False)
_, eval_data_fold = collect_spectrum(tau_fold, gens, f_abc, gammas,
                                      max_pq_sum=MAX_PQ_SUM, verbose=False)

n_evals_0 = sum(len(ed[2]) for ed in eval_data_0)  # (local)
n_evals_fold = sum(len(ed[2]) for ed in eval_data_fold)  # (local)
n_sectors = len(eval_data_0)  # (local)
print(f'  Sectors: {n_sectors}')
print(f'  Eigenvalues per s: s=0 -> {n_evals_0}, s=tau_fold -> {n_evals_fold}')

# Heat kernel sample
t_probe = np.array([0.01, 0.05, 0.1, 0.5, 1.0])
K_t_0, _ = compute_heat_kernel(eval_data_0, t_probe)
print('[4] Heat kernel K(t) at s=0:')
for i, t in enumerate(t_probe):
    print(f'  t={t:.3f}: K={K_t_0[i]:.6e}, t^4*K={t**4 * K_t_0[i]:.6e}')

# =============================================================================
# [5] Seeley-DeWitt coefficient extraction (s=0 and s=tau_fold)
# =============================================================================
print('[5] Seeley-DeWitt coefficient extraction (s=0):')
coeffs_0, fit_q_0 = extract_seeley_dewitt(eval_data_0, t_range=T_RANGE,
                                          n_points=N_POINTS_SD, verbose=False)
for name in ['a_0', 'a_2', 'a_4', 'a_6', 'a_8']:
    print(f'  {name} = {coeffs_0[name]:.6e}')
print(f'  fit RMS residual: {fit_q_0["residual"]:.2e}')
print(f'  fit condition#:   {fit_q_0["condition_number"]:.2e}')

print('[5] Seeley-DeWitt coefficient extraction (s=tau_fold):')
coeffs_f, fit_q_f = extract_seeley_dewitt(eval_data_fold, t_range=T_RANGE,
                                          n_points=N_POINTS_SD, verbose=False)
for name in ['a_0', 'a_2', 'a_4', 'a_6', 'a_8']:
    print(f'  {name} = {coeffs_f[name]:.6e}')

# Ratios
R_spec_0 = 6.0 * coeffs_0['a_2'] / coeffs_0['a_0']  # (local) spectral R at s=0
R_spec_f = 6.0 * coeffs_f['a_2'] / coeffs_f['a_0']  # (local) spectral R at fold
print(f'[5] R_spectral(s=0)      = 6*a_2/a_0 = {R_spec_0:.4f}   '
      f'(exact Levi-Civita: {R_values[0.0]:.4f})')
print(f'[5] R_spectral(s=fold)   = 6*a_2/a_0 = {R_spec_f:.4f}   '
      f'(exact Levi-Civita: {R_values[tau_fold]:.4f})')

# Robust extraction (multi-range)
print('[5] Robust SD extraction (s=0, 3 t-ranges):')
coeffs_rob, coeffs_unc = extract_seeley_dewitt_robust(eval_data_0, verbose=False)
for name in ['a_0', 'a_2', 'a_4']:
    v = coeffs_rob[name]
    u = coeffs_unc[name]
    rel = abs(u / v) if abs(v) > 1e-30 else float('inf')  # (local)
    print(f'  {name}={v:.4e} +/- {u:.2e} ({rel:.1%} rel.)')

# =============================================================================
# [6] Spectral action S(s) = Tr(exp(-D^2/Lambda^2)) — scheme: heat kernel cutoff
# =============================================================================
print(f'[6] Spectral action S(s) with Lambda={LAMBDA_CUT} (heat cutoff):')
S_0, _ = spectral_action_smooth_cutoff(eval_data_0, LAMBDA_CUT, f_type='heat')
S_fold, _ = spectral_action_smooth_cutoff(eval_data_fold, LAMBDA_CUT, f_type='heat')
S_ratio = S_fold / S_0  # (local) direction indicator
print(f'  S(s=0)        = {S_0:.4f}')
print(f'  S(s=tau_fold) = {S_fold:.4f}')
print(f'  S(fold)/S(0)  = {S_ratio:.6f}')

# Substitution chain confirmation: spectral action decreases with s
#   a_0(fold) < a_0(0) and a_2(fold) > a_2(0) [from Gilkey: a_2 proportional R, rises]
#   So S = a_0/t^4 + a_2/t^3 + ... at small t is NOT monotone trivially.
#   Direction: S(fold)/S(0) computed numerically from full truncated sum.

# Lorentzian cutoff cross-check
S_0_lor, _ = spectral_action_smooth_cutoff(eval_data_0, LAMBDA_CUT, f_type='lorentz')
S_fold_lor, _ = spectral_action_smooth_cutoff(eval_data_fold, LAMBDA_CUT, f_type='lorentz')
print(f'  S_lorentz(0)      = {S_0_lor:.4f}')
print(f'  S_lorentz(fold)   = {S_fold_lor:.4f}')
print(f'  S_lorentz(fold)/S_lorentz(0) = {S_fold_lor/S_0_lor:.6f}')

# =============================================================================
# [7] Weyl law check (d=8 expected)
# =============================================================================
d_eff, C_eff = weyl_law_check(eval_data_0, verbose=False)
print(f'[7] Weyl law d_eff = {d_eff:.3f}   (expected d=8.0, deviation expected at L_max=3)')

# =============================================================================
# [8] Output 4-tuple — primary gate value is a_2(s=0) in Gilkey normalization
# =============================================================================
# Use a_2(s=0) as the decisive spectral-action value. Scheme: heat-kernel
# polynomial fit on t in [0.01, 0.5] with 200 points (SD convention per script).
value_a2_0 = coeffs_0['a_2']  # (local) primary verdict value
value_a0_0 = coeffs_0['a_0']  # (local) volume reference
value_a4_0 = coeffs_0['a_4']  # (local) gauge coefficient

# Gate criteria (INFO — legacy benchmark script, no formal PASS threshold):
#   Cross-check 1: R_spectral(s=0) vs R_exact(s=0) = 2.000
#     (individual SD coeffs have >100% uncertainty at L_max=3 per script caveat)
#   Cross-check 2: Volume preservation |det-1| < 1e-10
#   Cross-check 3: Clifford algebra check < 1e-12
#   Cross-check 4: SU(2) Dirac benchmark PASS

cross_checks = {
    'clifford_err_below_1e-12': bool(cliff_err < 1e-12),
    'su2_benchmark_passed': bool(su2_ok),
    'volume_preserved_below_1e-10': bool(vol_max_err < 1e-10),
    'R_exact_s0_equals_2': bool(abs(R_values[0.0] - 2.0) < 1e-10),
    'R_fold_ratio_matches_analytic': bool(
        abs(R_fold_ratio - scalar_curvature_analytical(tau_fold)) < 1e-10
    ),
}  # (local)

print('[8] Cross-checks:')
for k, v in cross_checks.items():
    print(f'  {k}: {"PASS" if v else "FAIL"}')

all_cross_checks_passed = all(cross_checks.values())  # (local)

# =============================================================================
# [9] Save npz
# =============================================================================
out_path = os.path.join(ROOT, 't3-intake', 'spectral_action.npz')
np.savez(out_path,
         pin_map=json.dumps(pin_map),
         max_pq_sum=MAX_PQ_SUM,
         Lambda=LAMBDA_CUT,
         tau_fold=tau_fold,
         Vol_SU3_Haar=Vol_SU3_Haar,
         R_exact_s0=R_values[0.0],
         R_exact_fold=R_values[tau_fold],
         R_fold_ratio=R_fold_ratio,
         a_0_s0=coeffs_0['a_0'],
         a_2_s0=coeffs_0['a_2'],
         a_4_s0=coeffs_0['a_4'],
         a_6_s0=coeffs_0['a_6'],
         a_8_s0=coeffs_0['a_8'],
         a_0_fold=coeffs_f['a_0'],
         a_2_fold=coeffs_f['a_2'],
         a_4_fold=coeffs_f['a_4'],
         a_6_fold=coeffs_f['a_6'],
         a_8_fold=coeffs_f['a_8'],
         S_heat_0=S_0,
         S_heat_fold=S_fold,
         S_heat_ratio=S_ratio,
         S_lorentz_0=S_0_lor,
         S_lorentz_fold=S_fold_lor,
         d_eff_weyl=d_eff,
         fit_residual_s0=fit_q_0['residual'],
         fit_condition_s0=fit_q_0['condition_number'],
         cross_checks=json.dumps(cross_checks),
         clifford_err=cliff_err,
         vol_max_err=vol_max_err,
         )
print(f'[9] Saved npz: {out_path}')

# =============================================================================
# [10] Closure SHA — hash of ordered pin-map
# =============================================================================
# Per gate-verdicts.md: the closure SHA is the SHA-256 of the ordered input-pin map
closure_digest = hashlib.sha256()
for f in sorted(pin_map.keys()):
    closure_digest.update(f.encode('utf-8'))
    closure_digest.update(b':')
    closure_digest.update(pin_map[f].encode('utf-8'))
    closure_digest.update(b'\n')
closure_sha = closure_digest.hexdigest()  # (local) 64-char
print(f'[10] Closure SHA-256: {closure_sha}')

# =============================================================================
# 4-tuple output (final non-verdict line)
# =============================================================================
print('=' * 80)
print(f'OUTPUT-4TUPLE: value=a_2(s=0)={value_a2_0:.6e} '
      f'scheme=heat-kernel-polyfit convention=Gilkey-spin8 L_max={MAX_PQ_SUM} '
      f'sha256={closure_sha}')
print('=' * 80)
