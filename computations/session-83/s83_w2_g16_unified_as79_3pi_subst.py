"""
S83 W2-G16: S83-UNIFIED-AS-79-WITH-3PI-SUBSTITUTION

Re-run UNIFIED-AS-79 with CC7-HIERARCHY substitution  F_amp := F_amp^{3PI} * k_a2
under Convention A (Lambda_Z = M_KK), the headline regulator convention for
S83 W2 consistent with the G1 Zubarev-canonical carry-forward and the G15 FAIL
(k_a2 not R-protected, span_A=14.69).

Gate: S83-UNIFIED-AS-79-WITH-3PI-SUBSTITUTION
Trigger: [VERIFY][CHAIN] (composite ledger re-assembly)
Classification: PHONONIC + PARTICLE (composite A_s ledger)

Hypothesis (pre-registered, plan line 1287):
    Substituting  F_amp := F_amp^{3PI} * k_a2  into UNIFIED-AS-79 reproduces
    the W1-2 A_s = 3.30e-9 verdict within a factor-3 band.

Thresholds (pre-registered, plan line 1290 / line 1311):
    PASS: A_s in [1.10e-9, 9.90e-9]  ( |log10(A_s / 3.30e-9)| < 0.477 )
    INFO: A_s in [3.30e-10, 1.10e-9] U [9.90e-9, 3.30e-8] (borderline)
    FAIL: A_s outside [3.30e-10, 3.30e-8]

Convention declaration:
    CONVENTION A — Lambda_Z = M_KK for the Zubarev-family 5-regulator scan.
    This is the S83 W2 HEADLINE convention (matches G7 zeta, G14 Zubarev
    consistency, G15 span_A=14.69 FAIL headline, and G1 Zubarev-canonical
    IC scheme). Convention B (Lambda_Z=matched-scale) is provided as a
    supplementary cross-check but is NOT the verdict driver.

Wave 1-2 carry-forward used here:
    G1  PASS:  Branch-B Zubarev-canonical IC scheme.
    G7  PASS:  F_amp^{3PI}(N_pivot) = F_amp_lin_numerical = 1.02578408
               (S83 W2-G7 zeta, Mukhanov BD->pivot, sha=0ea13ce9...).
    G14 PASS:  c_sub regulator-robust across zeta/Zubarev/SDW (factor 1.227).
    G15 FAIL:  k_a2 NOT R-protected under Conv A  (span_A=14.69).
               Primary k_a2 slot under Conv A = zeta value = 0.582979.
               Full 5-regulator scan reported as regulator-sensitivity band.

SUBSTITUTION CHAIN ([VERIFY][CHAIN], mandatory):

    Step 1 (Definition). From s80_unified_as_79_full.py L89-95:
        A_s(F_amp)
          = ( H_tilde^2 / (8 pi^2) ) * (1/eps_H) * F_amp * (1/c_sub) * f_conv
        with  F_amp = F_amp_slot_adjusted = F_amp_canonical * k_a2.

    Step 1b (Branch pin).  The S80 W1-2 PASS-F2 A_s=3.30e-9 verdict is the
        TD-FRAMEWORK branch (zeta, substrate-native, L_max=3, N_pivot=55) with
        H_tilde_TD_framework = 5.90760e-03.  The LI branch (SDW, L_max=5)
        yields A_s=5.74e-14 (FAIL-GT15).  G1 Zubarev-canonical selects the IC
        scheme but the G7 dynamical F_amp^{3PI} is computed in zeta, so the
        substrate-native zeta-TD branch is the track to which F_amp^{3PI}
        substitutes.  We therefore use  H_tilde = H_tilde_TD_framework.

    Step 2 (Substitute).  F_amp -> F_amp^{3PI}(pivot) * k_a2(pivot, Conv A).
        F_amp^{3PI}_pivot   = 1.0257840776      (G7 PASS, zeta, dynamical)
        k_a2(Conv A, zeta)  = 0.582978623849687 (G15 primary slot, Lambda_Z=M_KK)
        F_amp_composite     = F_amp^{3PI} * k_a2 = 0.5980101899

    Step 3 (Simplify).
        prefactor = H_tilde_TD^2 / (8 pi^2)  = 5.90760e-03^2 / (8 pi^2)
        A_s_new   = prefactor * (1/eps_H) * F_amp_composite * (1/c_sub) * f_conv

    Step 4 (Direction).  PASS iff |log10( A_s_new / 3.30e-9 )| < 0.477.

    Step 5 (Regulator sensitivity).  k_a2 is G15-FAIL (span_A=14.69) under
        Conv A, so the A_s_new headline is inherently R-sensitive.  We report:
            (a) primary: zeta-zeta (F_amp^{3PI} zeta * k_a2 zeta-under-A)
            (b) 5-regulator band: F_amp_composite in [k_a2_min, k_a2_max] * F_amp^{3PI}
        The primary is used for the verdict line.  The band is the INFO flag.

Output 4-tuple: (A_s_new=<v>, scheme=zeta, convention=F_amp-3PI-times-k_a2-Conv-A, L_max=5)
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import hashlib
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Canonical constants (MANDATORY per .claude/rules/math-scripts.md)
from canonical_constants import (
    A_s_CMB,            # 2.1e-9 Planck 2018 scalar amplitude
    M_KK_gravity,
    M_Pl_reduced,
    a0_fold,
    tau_fold,
)

SCRIPT_DIR = Path(__file__).resolve().parent

# =============================================================================
# SECTION 0 — INPUT PINS
# =============================================================================
# All input values are sourced from S80 (UNIFIED-AS-79 ledger) and S83 W2 G7,
# G15 verdicts. Every literal that is not a framework canonical constant is
# tagged `# (local)` with session/provenance.

# --- UNIFIED-AS-79 ledger inputs (s80_unified_as_79_full.py L44-68) ---------
# BRANCH PIN: the S80 W1-2 PASS-F2 A_s=3.30e-9 canonical is produced by the
# TD-FRAMEWORK branch (zeta, substrate-native, L_max=3, H_tilde=5.9076e-03),
# NOT by the LI branch (which is FAIL-GT15 at 5.74e-14).  G16 substitutes
# F_amp^{3PI} (computed in zeta, G7 PASS) into the ledger, so the TD-framework
# (zeta) branch is the matching track.
H_tilde_TD       = 5.90760e-03   # (local) S80 W1-1 TD-framework verdict (zeta, substrate-native, L_max=3)
H_tilde_LI       = 2.46411e-05   # (local) S80 W1-1 LI verdict (SDW, epoch-resolved-a_2, L_max=5; reference only)
eps_H            = 0.02163       # (local) S80 plan line 895, one-loop slow-roll
c_sub            = 2.238         # (local) S78 W2-E central (zeta/Zubarev/SDW range)
f_conv           = 9.30e-4       # (local) (M_KK/M_Pl_red)^2 hierarchy conversion
F_amp_canonical  = 1.0166        # (local) S80 W1-B-REMED Method B pin (S80 W1-2 baseline)
k_a2_canonical   = 0.3822        # (local) W0-5 slot factor at S80 W1-2 baseline
A_s_canonical    = 3.30e-9       # (local) S80 W1-2 PASS-F2 TD-framework headline (plan line 1287)

# --- G7 CC7-DYNAMICAL PASS (zeta, Mukhanov BD->pivot) -----------------------
# Source: computations/session-83/s83_w2_g7_cc7_dynamical.npz (verdict PASS, sha=0ea13ce9...)
F_amp_3PI_pivot  = 1.02578407761463   # (local) G7 F_amp_lin_numerical at N_pivot=64.08

# --- G15 K-A2-CANONICAL-RANGE (Convention A HEADLINE, Lambda_Z=M_KK) --------
# Source: computations/session-83/s83_w2_g15_k_a2_canonical_range.npz (verdict FAIL, sha=5de7db1d...)
# Conv A values for the 5 regulators at L_max=5:
k_a2_A_zeta       = 0.58297862384968670  # (local) G15 zeta, Conv A (PRIMARY slot for verdict)
k_a2_A_Zubarev    = 0.07417974456744407  # (local) G15 Zubarev, Conv A (Lambda_Z=M_KK)
k_a2_A_SDW        = 1.08933353341893100  # (local) G15 SDW, Conv A
k_a2_A_dimreg     = 0.58297862384968670  # (local) G15 dim-reg, Conv A (ties zeta)
k_a2_A_lattice_BR = 0.58297862384968670  # (local) G15 lattice Ball-Radzikowski, Conv A (ties zeta)
span_A_reference  = 14.68505371339627    # (local) G15 headline span_A (INFO band is 1.5-2.5)

k_a2_A_primary = k_a2_A_zeta             # (local) zeta is primary slot (matches G7 zeta scheme)

# --- Gate thresholds (factor-3, plan line 1290) -----------------------------
PASS_LOG10_FACTOR3 = float(np.log10(3.0))  # (local) 0.477
INFO_LOG10_FACTOR3 = 0.30                   # (local) 0.30 INFO/PASS boundary (between factor-2 and factor-3)

A_s_PASS_LO = 1.10e-9   # (local) A_s PASS lower bound (A_s_canonical / 3)
A_s_PASS_HI = 9.90e-9   # (local) A_s PASS upper bound (A_s_canonical * 3)
A_s_FAIL_LO = 3.30e-10  # (local) A_s FAIL lower bound (A_s_canonical / 10)
A_s_FAIL_HI = 3.30e-8   # (local) A_s FAIL upper bound (A_s_canonical * 10)

CONVENTION = "F_amp-3PI-times-k_a2-Conv-A"  # (local) output convention tag
SCHEME     = "zeta"                         # (local) G7+G15-primary both zeta
L_MAX      = 5                              # (local) G15 regulator scan L_max

# =============================================================================
# SECTION 1 — INPUT-PIN SHA-256 MAP (for closure pin, per gate-verdicts.md §4)
# =============================================================================

def _sha256_file(path: Path) -> str:
    """SHA-256 hex of file contents (empty string if not found)."""
    if not path.is_file():
        return 'MISSING'
    h = hashlib.sha256()                   # (local)
    with open(path, 'rb') as fh:
        for chunk in iter(lambda: fh.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()

input_pins = {
    's83_w2_g7_cc7_dynamical.npz':   _sha256_file(SCRIPT_DIR / 's83_w2_g7_cc7_dynamical.npz'),
    's83_w2_g15_k_a2_canonical_range.npz': _sha256_file(
        SCRIPT_DIR / 's83_w2_g15_k_a2_canonical_range.npz'),
    's80_unified_as_79_full.py':     _sha256_file(SCRIPT_DIR / 's80_unified_as_79_full.py'),
    'canonical_constants.py':        _sha256_file(SCRIPT_DIR / 'canonical_constants.py'),
}

# Deterministic closure SHA = sha256 of ordered JSON-like string of input pins
_ordered_pin_string = ';'.join(f'{k}={v}' for k, v in sorted(input_pins.items()))
closure_sha = hashlib.sha256(_ordered_pin_string.encode('utf-8')).hexdigest()

print('=' * 78)
print('S83 W2-G16: UNIFIED-AS-79-WITH-3PI-SUBSTITUTION')
print('=' * 78)
print('INPUT PINS (SHA-256):')
for k, v in input_pins.items():
    print(f'  {k:<45s} = {v[:16]}...')
print(f'Closure SHA = {closure_sha}')
print(f'Convention  = {CONVENTION}  (headline: Lambda_Z = M_KK)')
print(f'Scheme      = {SCHEME}')
print(f'L_max       = {L_MAX}')
print('-' * 78)

# =============================================================================
# SECTION 2 — SUBSTITUTION CHAIN (verbatim, Steps 1-4)
# =============================================================================

print('\nSUBSTITUTION CHAIN [VERIFY][CHAIN]:')
print('-' * 78)

# Step 1 — Definition (branch: TD-framework zeta, the PASS-F2 track from S80 W1-2)
prefactor_H = H_tilde_TD**2 / (8.0 * np.pi**2)     # (local)
print('Step 1  Definition:')
print('  A_s(F_amp) = (H_tilde^2 / (8 pi^2)) * (1/eps_H) * F_amp * (1/c_sub) * f_conv')
print(f'  BRANCH = TD-framework (zeta, substrate-native, L_max=3)  -- matches PASS-F2 track')
print(f'  H_tilde_TD = {H_tilde_TD:.5e},  eps_H = {eps_H:.5f},  c_sub = {c_sub:.4f},  f_conv = {f_conv:.3e}')
print(f'  prefactor H_tilde^2/(8 pi^2) = {prefactor_H:.6e}')
print(f'  (For reference: H_tilde_LI = {H_tilde_LI:.5e} yields FAIL-GT15 at 5.74e-14 in S80.)')

# Step 2 — Substitute F_amp -> F_amp^{3PI} * k_a2
F_amp_composite_primary = F_amp_3PI_pivot * k_a2_A_primary   # (local) zeta-zeta, Conv A
print('\nStep 2  Substitute  F_amp -> F_amp^{3PI}(pivot) * k_a2(Conv A):')
print(f'  F_amp^{{3PI}}_pivot  = {F_amp_3PI_pivot:.10f}   (G7 PASS, zeta, dynamical)')
print(f'  k_a2(Conv A, zeta) = {k_a2_A_primary:.10f}   (G15 primary, Lambda_Z=M_KK)')
print(f'  F_amp_composite     = {F_amp_composite_primary:.10f}  (PRIMARY)')

# Step 3 — Simplify (compute A_s_new)
def compute_unified_as_79_with_3PI_substitution(F_amp_comp):
    """Full UNIFIED-AS-79 ledger with F_amp := F_amp_comp."""
    return prefactor_H * (1.0 / eps_H) * F_amp_comp * (1.0 / c_sub) * f_conv  # (local)

A_s_new_primary = compute_unified_as_79_with_3PI_substitution(F_amp_composite_primary)   # (local)
term_prefac = prefactor_H                                                                # (local)
term_inv_eps = 1.0 / eps_H                                                               # (local)
term_Famp = F_amp_composite_primary                                                      # (local)
term_inv_csub = 1.0 / c_sub                                                              # (local)
term_fconv = f_conv                                                                      # (local)

print('\nStep 3  Simplify A_s_new (PRIMARY, zeta-zeta, Conv A):')
print(f'  term 1  (H^2/8 pi^2)   = {term_prefac:.6e}')
print(f'  term 2  (1/eps_H)      = {term_inv_eps:.6f}  => {term_prefac*term_inv_eps:.6e}')
print(f'  term 3  F_amp_comp     = {term_Famp:.6f}  => {term_prefac*term_inv_eps*term_Famp:.6e}')
print(f'  term 4  (1/c_sub)      = {term_inv_csub:.6f}  => {term_prefac*term_inv_eps*term_Famp*term_inv_csub:.6e}')
print(f'  term 5  f_conv         = {term_fconv:.3e}  => {A_s_new_primary:.6e}')
print(f'  A_s_new (PRIMARY) = {A_s_new_primary:.6e}')

# Step 4 — Direction
log_ratio_primary = float(np.log10(A_s_new_primary / A_s_canonical))   # (local)
abs_log_primary = abs(log_ratio_primary)                               # (local)
print('\nStep 4  Direction (PRIMARY):')
print(f'  A_s_canonical       = {A_s_canonical:.4e}  (S80 W1-2 PASS-F2 headline, plan L1287)')
print(f'  A_s_new (PRIMARY)   = {A_s_new_primary:.4e}')
print(f'  log10(new/canon)    = {log_ratio_primary:+.4f}  (PASS: |.|<{PASS_LOG10_FACTOR3:.4f})')

if A_s_PASS_LO <= A_s_new_primary <= A_s_PASS_HI:
    verdict_primary = 'PASS'
elif A_s_FAIL_LO <= A_s_new_primary <= A_s_FAIL_HI:
    verdict_primary = 'INFO'
else:
    verdict_primary = 'FAIL'

print(f'  verdict (PRIMARY)   = {verdict_primary}')

# =============================================================================
# SECTION 3 — 5-REGULATOR SENSITIVITY BAND (G15 carry-forward)
# =============================================================================

print('\n' + '=' * 78)
print('SECTION 3  5-regulator k_a2 scan (G15 FAIL => regulator-sensitivity band)')
print('=' * 78)

reg_labels = ['zeta', 'Zubarev-A', 'SDW', 'dim-reg', 'lattice-BR']             # (local)
reg_k_a2 = np.array([k_a2_A_zeta, k_a2_A_Zubarev, k_a2_A_SDW,
                     k_a2_A_dimreg, k_a2_A_lattice_BR])                        # (local)

F_amp_scan  = F_amp_3PI_pivot * reg_k_a2                                       # (local)
A_s_scan    = np.array([compute_unified_as_79_with_3PI_substitution(f)
                        for f in F_amp_scan])                                  # (local)
log_ratio_scan = np.log10(A_s_scan / A_s_canonical)                            # (local)

print(f'  reg            k_a2           F_amp_comp     A_s_new        log10(new/canon)')
for lab, ka, fa, aa, lr in zip(reg_labels, reg_k_a2, F_amp_scan, A_s_scan, log_ratio_scan):
    print(f'  {lab:<12s}   {ka:.10f}   {fa:.10f}   {aa:.4e}    {lr:+.4f}')

A_s_scan_min = float(np.min(A_s_scan))                                          # (local)
A_s_scan_max = float(np.max(A_s_scan))                                          # (local)
A_s_scan_median = float(np.median(A_s_scan))                                    # (local)
A_s_scan_span = A_s_scan_max / A_s_scan_min                                     # (local)

print(f'\n  A_s scan min     = {A_s_scan_min:.4e}')
print(f'  A_s scan max     = {A_s_scan_max:.4e}')
print(f'  A_s scan median  = {A_s_scan_median:.4e}')
print(f'  A_s scan span    = {A_s_scan_span:.4f}  (same as span_A = {span_A_reference:.4f}, G15 headline)')

# Count how many regulators individually land in PASS / INFO / FAIL
count_pass = int(np.sum((A_s_scan >= A_s_PASS_LO) & (A_s_scan <= A_s_PASS_HI)))  # (local)
count_info = int(np.sum(((A_s_scan >= A_s_FAIL_LO) & (A_s_scan < A_s_PASS_LO)) |
                        ((A_s_scan > A_s_PASS_HI) & (A_s_scan <= A_s_FAIL_HI))))  # (local)
count_fail = int(np.sum((A_s_scan < A_s_FAIL_LO) | (A_s_scan > A_s_FAIL_HI)))    # (local)
print(f'\n  PASS regulators = {count_pass}/5')
print(f'  INFO regulators = {count_info}/5')
print(f'  FAIL regulators = {count_fail}/5')

# =============================================================================
# SECTION 4 — BENCHMARK (plan Step-5 Python snippet, verbatim)
# =============================================================================

print('\n' + '=' * 78)
print('SECTION 4  Plan-mandated verification snippet')
print('=' * 78)

A_s_original = 3.30e-9                                                           # (local) plan line 1314
A_s_new = compute_unified_as_79_with_3PI_substitution(F_amp_composite_primary)  # (local)
log_ratio = float(np.log10(A_s_new / A_s_original))                              # (local)
print(f'  A_s new (3PI subst) = {A_s_new:.4e}')
print(f'  A_s original        = {A_s_original:.4e}')
print(f'  log ratio           = {log_ratio:.4f}')
snippet_verdict = 'PASS' if abs(log_ratio) < 0.477 else 'FAIL'                   # (local) plan-snippet 2-way
print(f'  Verdict (snippet 2-way)  = {snippet_verdict}')
print(f'  Verdict (3-way full)     = {verdict_primary}')

# =============================================================================
# SECTION 5 — CROSS-CHECKS
# =============================================================================

print('\n' + '=' * 78)
print('SECTION 5  Cross-checks')
print('=' * 78)

# CC-1: reproduce S80 W1-2 TD-framework PASS-F2 baseline (F_amp_slot_adjusted = 0.3885)
# Expected: A_s = 3.2994e-9 (machine-equal to 3.30e-9 canonical at 4 sig figs)
F_amp_S80 = F_amp_canonical * k_a2_canonical                                     # (local)
A_s_S80_reproduce = compute_unified_as_79_with_3PI_substitution(F_amp_S80)       # (local)
log_ratio_S80 = float(np.log10(A_s_S80_reproduce / A_s_canonical))               # (local)
CC1_reproduce_ok = abs(log_ratio_S80) < 0.01                                     # (local) tight identity check
print(f'  CC-1  Reproduce S80 W1-2 TD-framework baseline (F_amp={F_amp_S80:.4f}):')
print(f'        A_s = {A_s_S80_reproduce:.4e} (expected 3.2994e-9 from S80 npz)')
print(f'        log10(/canon)={log_ratio_S80:+.6f},  ok={CC1_reproduce_ok}')

# CC-2: BD limit (F_amp^{3PI} -> 1, k_a2 -> 1) should give bare ledger value
A_s_BD_limit = compute_unified_as_79_with_3PI_substitution(1.0)                  # (local)
log_ratio_BD = float(np.log10(A_s_BD_limit / A_s_canonical))                     # (local)
print(f'  CC-2  BD limit (F_amp=1.0000, no amplification, no slot):')
print(f'        A_s = {A_s_BD_limit:.4e}, log10(/canon)={log_ratio_BD:+.4f}')

# CC-3: Direction chain — c_sub identity d(lnA_s)/d(ln c_sub) = -1
c_sub_pert = c_sub * 1.01                                                        # (local)
A_s_pert = prefactor_H * (1.0/eps_H) * F_amp_composite_primary * (1.0/c_sub_pert) * f_conv  # (local)
dlnAs_dlncsub = np.log(A_s_pert / A_s_new_primary) / np.log(c_sub_pert / c_sub)  # (local)
CC3_identity_ok = abs(dlnAs_dlncsub + 1.0) < 1e-10                               # (local)
print(f'  CC-3  d(lnA_s)/d(ln c_sub) = {dlnAs_dlncsub:.10f}  (expected -1),  ok={CC3_identity_ok}')

# CC-4: Direction chain — F_amp_composite identity d(lnA_s)/d(ln F_amp) = +1
F_amp_pert = F_amp_composite_primary * 1.01                                      # (local)
A_s_pert2 = prefactor_H * (1.0/eps_H) * F_amp_pert * (1.0/c_sub) * f_conv        # (local)
dlnAs_dlnFamp = np.log(A_s_pert2 / A_s_new_primary) / np.log(F_amp_pert / F_amp_composite_primary)  # (local)
CC4_identity_ok = abs(dlnAs_dlnFamp - 1.0) < 1e-10                               # (local)
print(f'  CC-4  d(lnA_s)/d(ln F_amp) = {dlnAs_dlnFamp:.10f}  (expected +1),  ok={CC4_identity_ok}')

# CC-5: G15 span_A reproducibility (A_s span should equal k_a2 span exactly)
A_s_span_check = A_s_scan_max / A_s_scan_min                                     # (local)
CC5_span_match_ok = abs(A_s_span_check - span_A_reference) / span_A_reference < 1e-10  # (local)
print(f'  CC-5  A_s_scan span       = {A_s_span_check:.6f}  vs  G15 span_A = {span_A_reference:.6f},  ok={CC5_span_match_ok}')

# CC-6: log-ratio direction check under F_amp SUPPRESS (slot value < 1):
#   F_amp_composite = 1.0258 * 0.5830 = 0.5980 < 1 -> A_s_new < A_s_bare_ledger
#   where A_s_bare_ledger = prefactor*(1/eps)*1*(1/c_sub)*f_conv
A_s_bare_ledger = prefactor_H * (1.0/eps_H) * 1.0 * (1.0/c_sub) * f_conv         # (local)
suppress_direction_ok = (A_s_new_primary < A_s_bare_ledger)                      # (local)
print(f'  CC-6  F_amp_comp = {F_amp_composite_primary:.4f} < 1  =>  A_s_new < A_s_bare:')
print(f'        A_s_new = {A_s_new_primary:.4e}, A_s_bare = {A_s_bare_ledger:.4e},  ok={suppress_direction_ok}')

cross_checks_all_ok = bool(CC1_reproduce_ok and CC3_identity_ok and
                           CC4_identity_ok and CC5_span_match_ok and suppress_direction_ok)
print(f'\n  ALL cross-checks ok:  {cross_checks_all_ok}')

# =============================================================================
# SECTION 6 — VERDICT ASSEMBLY
# =============================================================================

print('\n' + '=' * 78)
print('SECTION 6  Verdict (S83-UNIFIED-AS-79-WITH-3PI-SUBSTITUTION)')
print('=' * 78)

# Primary verdict (zeta-zeta under Conv A) drives the verdict line.
# Span band from the 5-regulator scan is the regulator-sensitivity flag.

verdict_line = (
    f'S83-UNIFIED-AS-79-WITH-3PI-SUBSTITUTION: {verdict_primary} -- '
    f'value=A_s_new={A_s_new_primary:.4e},log10/canon={log_ratio_primary:+.4f},'
    f'F_amp_comp={F_amp_composite_primary:.4f}=F_amp_3PI*{k_a2_A_primary:.4f},'
    f'scan_span={A_s_scan_span:.2f},PASS_reg={count_pass}/5,'
    f'FAIL_reg={count_fail}/5 '
    f'scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} sha256={closure_sha}'
)
print(verdict_line)

# =============================================================================
# SECTION 7 — SAVE
# =============================================================================

out_npz = SCRIPT_DIR / 's83_w2_g16_unified_as79_3pi_subst.npz'
out_png = SCRIPT_DIR / 's83_w2_g16_unified_as79_3pi_subst.png'

np.savez(
    out_npz,
    # Inputs
    H_tilde_TD=H_tilde_TD,
    H_tilde_LI=H_tilde_LI,
    eps_H=eps_H,
    c_sub=c_sub,
    f_conv=f_conv,
    A_s_canonical=A_s_canonical,
    F_amp_3PI_pivot=F_amp_3PI_pivot,
    k_a2_A_primary=k_a2_A_primary,
    F_amp_composite_primary=F_amp_composite_primary,
    # Primary result (verdict driver)
    A_s_new_primary=A_s_new_primary,
    log_ratio_primary=log_ratio_primary,
    abs_log_primary=abs_log_primary,
    verdict_primary=verdict_primary,
    # 5-regulator scan
    reg_labels=np.array(reg_labels),
    reg_k_a2=reg_k_a2,
    F_amp_scan=F_amp_scan,
    A_s_scan=A_s_scan,
    log_ratio_scan=log_ratio_scan,
    A_s_scan_min=A_s_scan_min,
    A_s_scan_max=A_s_scan_max,
    A_s_scan_median=A_s_scan_median,
    A_s_scan_span=A_s_scan_span,
    span_A_reference=span_A_reference,
    count_pass=count_pass,
    count_info=count_info,
    count_fail=count_fail,
    # Cross-checks
    CC1_reproduce_S80_ok=CC1_reproduce_ok,
    CC1_log_ratio_S80=log_ratio_S80,
    CC2_A_s_BD_limit=A_s_BD_limit,
    CC2_log_ratio_BD=log_ratio_BD,
    CC3_dlnAs_dlncsub=dlnAs_dlncsub,
    CC3_identity_ok=CC3_identity_ok,
    CC4_dlnAs_dlnFamp=dlnAs_dlnFamp,
    CC4_identity_ok=CC4_identity_ok,
    CC5_span_match_ok=CC5_span_match_ok,
    CC6_suppress_direction_ok=suppress_direction_ok,
    cross_checks_all_ok=cross_checks_all_ok,
    # Plan-snippet
    A_s_new_snippet=A_s_new,
    log_ratio_snippet=log_ratio,
    snippet_verdict=snippet_verdict,
    # Closure
    scheme=SCHEME,
    convention=CONVENTION,
    L_max=L_MAX,
    closure_sha=closure_sha,
    PASS_LOG10_FACTOR3=PASS_LOG10_FACTOR3,
    A_s_PASS_LO=A_s_PASS_LO,
    A_s_PASS_HI=A_s_PASS_HI,
    A_s_FAIL_LO=A_s_FAIL_LO,
    A_s_FAIL_HI=A_s_FAIL_HI,
)
print(f'\nSaved: {out_npz.name}')

# =============================================================================
# SECTION 8 — PLOT
# =============================================================================

fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))

# Left panel: 5-regulator A_s with PASS/INFO/FAIL bands (log scale)
ax = axes[0]
x_positions = np.arange(len(reg_labels))
colors = []
for a in A_s_scan:
    if A_s_PASS_LO <= a <= A_s_PASS_HI:
        colors.append('C2')   # green = PASS
    elif A_s_FAIL_LO <= a <= A_s_FAIL_HI:
        colors.append('C1')   # orange = INFO
    else:
        colors.append('C3')   # red = FAIL
ax.bar(x_positions, A_s_scan, color=colors, alpha=0.7, edgecolor='k')
ax.set_yscale('log')
ax.axhline(A_s_canonical, color='k', linestyle='--', linewidth=1.0,
           label=f'A_s canon = {A_s_canonical:.2e}')
ax.axhspan(A_s_PASS_LO, A_s_PASS_HI, color='g', alpha=0.12, label='PASS (factor-3)')
ax.axhspan(A_s_FAIL_LO, A_s_FAIL_HI, color='y', alpha=0.08, label='INFO (factor-10)')
ax.axhline(A_s_FAIL_LO, color='orange', linestyle=':', linewidth=0.8)
ax.axhline(A_s_FAIL_HI, color='orange', linestyle=':', linewidth=0.8)
ax.set_xticks(x_positions)
ax.set_xticklabels(reg_labels, rotation=20, ha='right')
ax.set_ylabel(r'$A_s^{\rm new}$ (log scale)')
ax.set_title(f'G16: A_s under 5-regulator $k_{{a_2}}$ scan (Conv A, $\\Lambda_Z=M_{{KK}}$)')
ax.legend(loc='best', fontsize=8)
ax.grid(True, alpha=0.3, which='both', axis='y')

# Mark primary (zeta) result
ax.annotate(f'PRIMARY = {A_s_new_primary:.2e}\n({verdict_primary})',
            xy=(0, A_s_new_primary),
            xytext=(0.5, A_s_new_primary * 3),
            fontsize=8,
            arrowprops=dict(arrowstyle='->', color='C0', linewidth=0.8))

# Right panel: factor-by-factor cumulative product (PRIMARY branch)
ax = axes[1]
step_labels = [r'$H^2/8\pi^2$', r'$\cdot 1/\varepsilon_H$', r'$\cdot F_{\rm amp}^{3PI}\cdot k_{a_2}$',
               r'$\cdot 1/c_{\rm sub}$', r'$\cdot f_{\rm conv}$']
acc = 1.0  # (local) accumulator initializer for factor-by-factor trace
vals = [prefactor_H]
vals.append(vals[-1] * (1.0/eps_H))
vals.append(vals[-1] * F_amp_composite_primary)
vals.append(vals[-1] * (1.0/c_sub))
vals.append(vals[-1] * f_conv)
xs = np.arange(len(step_labels))
ax.semilogy(xs, vals, 'o-', color='C0', linewidth=2.0, markersize=7,
            label=f'PRIMARY zeta-zeta,  final = {A_s_new_primary:.2e}')
ax.axhline(A_s_canonical, color='k', linestyle='--', linewidth=1.0,
           label=f'A_s canon = {A_s_canonical:.2e}')
ax.axhspan(A_s_PASS_LO, A_s_PASS_HI, color='g', alpha=0.12)
ax.axhspan(A_s_FAIL_LO, A_s_FAIL_HI, color='y', alpha=0.08)
ax.set_xticks(xs)
ax.set_xticklabels(step_labels, rotation=25, ha='right', fontsize=9)
ax.set_ylabel('Cumulative product (log scale)')
ax.set_title(f'G16: Factor-by-factor (PRIMARY, $\\Delta_{{\\rm OOM}}$ = {log_ratio_primary:+.3f})')
ax.legend(loc='lower right', fontsize=8)
ax.grid(True, alpha=0.3, which='both', axis='y')

plt.tight_layout()
plt.savefig(out_png, dpi=140, bbox_inches='tight')
plt.close()
print(f'Saved: {out_png.name}')

# =============================================================================
# SECTION 9 — APPEND VERDICT LINE TO s83_gate_verdicts.txt
# =============================================================================

verdicts_path = SCRIPT_DIR / 's83_gate_verdicts.txt'
with open(verdicts_path, 'a') as fh:
    fh.write('\n' + verdict_line + '\n')
print(f'Appended verdict to: {verdicts_path.name}')

print('\n' + '=' * 78)
print(f'S83 W2-G16 complete. Verdict (PRIMARY, zeta-zeta, Conv A): {verdict_primary}')
print('=' * 78)
