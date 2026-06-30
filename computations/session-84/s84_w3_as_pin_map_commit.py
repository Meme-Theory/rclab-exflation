"""
S84 W3-34: S84-AS-PIN-MAP-COMMIT

Commit the A_s pin-map JSON + SHA-256 as a canonical audit-integrity artifact.

Gate: S84-AS-PIN-MAP-COMMIT
Trigger: [VERIFY]
Classification: NON-PHONONIC (audit integrity; pin-map reproducibility commit)

Hypothesis (pre-registered, plan §W3-34 line ~1182):
    The A_s closure at A_s = 5.08e-9 (S83 G16 PASS, TD-framework / zeta /
    Conv A, L_max=5) reproduces to within 1e-8 relative when re-executed
    against a fully-committed pin-map covering all input slot pins
    (H_tilde_TD, eps_H, F_amp_3PI_pivot, k_a2, c_sub, f_conv, M_KK, tau_fold,
    scheme, convention, L_max, A_F).

Thresholds (pre-registered, plan line ~1228-1230):
    PASS:  rel_err < 1e-8
    INFO:  rel_err in [1e-9, 1e-8] (tolerance-floor / double-precision regime)
    FAIL:  rel_err >= 1e-8

Machinery pin (PRDR):
    N_eval=1 target (A_s); L_max=5; scan_range=N/A (pin-map fully fixed);
    tolerance=1e-8; scheme=zeta-canonical; convention=TD-branch canonical;
    random_seed=N/A (deterministic pin-map); GPU=CPU.

Audit-finding remediation (S84):
    Earlier gates (W3-26 / W3-28) produced colliding closure SHAs because
    their input-pin maps were narrow (only data-file hashes). Per the S84
    audit, this script includes `__script__` SHA and `__gate_id__` in the
    input-pin dict BEFORE SHA-256 closure, ensuring uniqueness even for
    gates whose data-file inputs coincide.

Substitution chain [VERIFY][CHAIN] (mandatory, per .claude/rules/math-scripts.md):

    Step 1 (Definition). A_s ledger formula (G16 PASS baseline, TD-framework
        branch, line 211 of s83_w2_g16_unified_as79_3pi_subst.py):
            A_s = (H_tilde_TD^2 / (8 pi^2)) * (1/eps_H)
                  * F_amp_composite * (1/c_sub) * f_conv
        where  F_amp_composite = F_amp_3PI_pivot * k_a2_A_primary.

    Step 2 (Substitution of pinned inputs). All values from the pin-map JSON
        constructed in SECTION 2 below:
            H_tilde_TD       = 5.90760e-03
            eps_H            = 0.02163
            c_sub            = 2.238
            f_conv           = 9.30e-4
            F_amp_3PI_pivot  = 1.02578407761463
            k_a2_A_primary   = 0.58297862384968670

    Step 3 (Simplification). Evaluated algebraically in double precision:
            F_amp_composite  = 0.598010189934697
            prefactor_H      = H_tilde_TD^2 / (8 pi^2) = 4.42010342331e-07
            A_s_rep          = prefactor_H * (1/eps_H) * F_amp_composite
                               * (1/c_sub) * f_conv
                             = 5.07817148502e-09

    Step 4 (Direction of rel_err). Since the pin-map floating-point ops here
        are BIT-IDENTICAL to the ops used in s83_w2_g16_unified_as79_3pi_subst.py
        (same operand order, same double-precision arithmetic), rel_err should
        be exactly 0.0 against the G16 stored full-precision A_s_new_primary.
        The rel_err sign/magnitude direction:
            rel_err := |A_s_rep - A_s_target| / A_s_target >= 0
            rel_err  = 0  iff  A_s_rep == A_s_target (bit-identical).
            PASS iff  rel_err < 1e-8.

Output 4-tuple: (value=A_s_reproduced, scheme=zeta, convention=TD-canonical, L_max=5)
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import hashlib
import json
from pathlib import Path

import numpy as np

# Canonical constants (MANDATORY per .claude/rules/math-scripts.md)
from canonical_constants import (
    M_KK_gravity,
    M_Pl_reduced,
    a0_fold,
    tau_fold,
)

SCRIPT_DIR = Path(__file__).resolve().parent
GATE_ID    = 'S84-AS-PIN-MAP-COMMIT'  # (local) gate identifier (audit-unique)

# =============================================================================
# SECTION 0 — INPUT-PIN SHA-256 MAP (must run BEFORE constructing pin-map JSON)
# =============================================================================

def _sha256_file(path: Path) -> str:
    """SHA-256 hex of file contents, or 'MISSING' if not found."""
    if not path.is_file():
        return 'MISSING'
    h = hashlib.sha256()                    # (local)
    with open(path, 'rb') as fh:
        for chunk in iter(lambda: fh.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()

# Files whose SHAs enter the closure. Per S84 audit, include this script's own
# SHA (`__script__`) and the gate ID (`__gate_id__`) so that pin-maps for
# different gates with overlapping data inputs produce distinct closure SHAs.
input_pins = {
    # Upstream data artifacts
    's83_w2_g16_unified_as79_3pi_subst.npz':
        _sha256_file(SCRIPT_DIR / 's83_w2_g16_unified_as79_3pi_subst.npz'),
    's83_w2_g16_unified_as79_3pi_subst.py':
        _sha256_file(SCRIPT_DIR / 's83_w2_g16_unified_as79_3pi_subst.py'),
    's83_w2_g7_cc7_dynamical.npz':
        _sha256_file(SCRIPT_DIR / 's83_w2_g7_cc7_dynamical.npz'),
    's83_w2_g15_k_a2_canonical_range.npz':
        _sha256_file(SCRIPT_DIR / 's83_w2_g15_k_a2_canonical_range.npz'),
    's80_unified_as_79_full.py':
        _sha256_file(SCRIPT_DIR / 's80_unified_as_79_full.py'),
    's84_w3_meta_composition_rule.json':
        _sha256_file(SCRIPT_DIR / 's84_w3_meta_composition_rule.json'),
    'canonical_constants.py':
        _sha256_file(SCRIPT_DIR / 'canonical_constants.py'),
    # Audit-unique fields (S84 remediation for W3-26 / W3-28 SHA collisions)
    '__script__':  _sha256_file(Path(__file__)),
    '__gate_id__': GATE_ID,
}

# =============================================================================
# SECTION 1 — A_s LEDGER INPUTS (verbatim G16 TD-framework / zeta / Conv A)
# =============================================================================
# All inputs sourced from s83_w2_g16_unified_as79_3pi_subst.py and npz.

H_tilde_TD       = 5.90760e-03          # (local) G16 TD-framework H_tilde (zeta, L_max=3)
eps_H            = 0.02163              # (local) S80 one-loop slow-roll eps_H
c_sub            = 2.238                # (local) S78 W2-E central (zeta/Zubarev/SDW range)
f_conv           = 9.30e-4              # (local) (M_KK/M_Pl_red)^2 hierarchy conversion
F_amp_3PI_pivot  = 1.02578407761463     # (local) G7 CC7-dynamical PASS, zeta, N_pivot=64.08
k_a2_A_primary   = 0.58297862384968670  # (local) G15 zeta under Conv A (Lambda_Z=M_KK), primary slot

# Target A_s (G16 PASS value at full stored precision — A_s_new_primary in npz)
A_s_target       = 5.07817148502282144670e-09  # (local) G16 npz A_s_new_primary (full float64)

# Tolerance (plan line 1189)
TOL              = 1e-8                 # (local) PASS threshold: rel_err < TOL
INFO_FLOOR       = 1e-9                 # (local) INFO band lower bound

# Scheme / convention / L_max tags
SCHEME           = 'zeta'                                   # (local) G16 headline scheme
CONVENTION       = 'TD-canonical'                           # (local) plan-specified convention tag
L_MAX            = 5                                        # (local) plan §W3-34 machinery pin

# A_F component list (plan §W3-34 line 1217)
A_F              = 'C+H+M_3(C)'                             # (local) plan A_F pin

# =============================================================================
# SECTION 2 — CONSTRUCT THE PIN-MAP JSON
# =============================================================================

pin_map = {
    # Ledger inputs
    'k_a2':             k_a2_A_primary,
    'f_conv':           f_conv,
    'H_tilde_TD':       H_tilde_TD,
    'H_tilde_TD_note':  'S80 W1-1 TD-framework verdict (zeta, L_max=3)',
    'eps_H':            eps_H,
    'c_sub':            c_sub,
    'F_amp_3PI_pivot':  F_amp_3PI_pivot,
    'F_amp_composite':  F_amp_3PI_pivot * k_a2_A_primary,  # (derived, but stored for reproducibility audit)
    # Framework-scale pins (canonical constants, included for audit completeness)
    'M_KK':             float(M_KK_gravity),
    'M_Pl_reduced':     float(M_Pl_reduced),
    'tau_fold':         float(tau_fold),
    'a0_fold':          float(a0_fold),
    # Scheme / convention / truncation
    'scheme':           SCHEME,
    'convention':       CONVENTION,
    'L_max':            L_MAX,
    'A_F':              A_F,
    # Target value (G16 PASS)
    'A_s_target':       A_s_target,
    'A_s_target_source':'s83_w2_g16_unified_as79_3pi_subst.npz[A_s_new_primary]',
    # Input SHA-256 closure map (includes __script__ + __gate_id__ per S84 audit)
    'input_pins':       input_pins,
    # Gate metadata
    '__gate_id__':      GATE_ID,
    '__script__':       input_pins['__script__'],
    '__tolerance__':    TOL,
    '__branch__':       'TD-framework',
    '__ledger_formula__': '(H_tilde^2/(8*pi^2)) * (1/eps_H) * F_amp_composite * (1/c_sub) * f_conv',
}

# Canonical serialization of pin-map (sort_keys, compact separators) for SHA
pin_map_canonical = json.dumps(pin_map, sort_keys=True, separators=(',', ':'))
sha_pin = hashlib.sha256(pin_map_canonical.encode('utf-8')).hexdigest()

# Deterministic closure SHA (ordered input-pin dict):
#   This is the verdict-line sha256. We derive it from the SAME sorted map
#   (without the self-embedding of sha_pin, to avoid circularity).
_ordered_pin_string = ';'.join(f'{k}={v}' for k, v in sorted(input_pins.items()))
closure_sha = hashlib.sha256(_ordered_pin_string.encode('utf-8')).hexdigest()

print('=' * 78)
print('S84 W3-34: S84-AS-PIN-MAP-COMMIT')
print('=' * 78)
print(f'Gate ID: {GATE_ID}')
print('INPUT PINS (SHA-256):')
for k, v in sorted(input_pins.items()):
    short = v[:16] if isinstance(v, str) and len(v) >= 16 else v
    print(f'  {k:<45s} = {short}...' if len(v) > 16 else f'  {k:<45s} = {v}')
print(f'Closure SHA (verdict-line sha256) = {closure_sha}')
print(f'Pin-map JSON SHA (sha_pin)        = {sha_pin}')
print(f'Convention = {CONVENTION}   Scheme = {SCHEME}   L_max = {L_MAX}')
print('-' * 78)

# =============================================================================
# SECTION 3 — REPRODUCTION (SUBSTITUTION CHAIN EXECUTION)
# =============================================================================

print('\nSUBSTITUTION CHAIN [VERIFY][CHAIN]:')
print('-' * 78)

# Step 1 — Definition
prefactor_H = H_tilde_TD**2 / (8.0 * np.pi**2)          # (local)
print('Step 1  Definition:')
print('  A_s = (H_tilde_TD^2 / (8 pi^2)) * (1/eps_H) * F_amp_comp * (1/c_sub) * f_conv')
print(f'  prefactor_H = H_tilde_TD^2 / (8 pi^2) = {prefactor_H:.15e}')

# Step 2 — Substitute
F_amp_composite = F_amp_3PI_pivot * k_a2_A_primary      # (local)
print('\nStep 2  Substitute pinned inputs:')
print(f'  H_tilde_TD       = {H_tilde_TD:.8e}')
print(f'  eps_H            = {eps_H:.8f}')
print(f'  c_sub            = {c_sub:.6f}')
print(f'  f_conv           = {f_conv:.8e}')
print(f'  F_amp_3PI_pivot  = {F_amp_3PI_pivot:.15f}')
print(f'  k_a2_A_primary   = {k_a2_A_primary:.15f}')
print(f'  F_amp_composite  = {F_amp_composite:.15e}')

# Step 3 — Simplify
A_s_rep = prefactor_H * (1.0 / eps_H) * F_amp_composite * (1.0 / c_sub) * f_conv  # (local)
print('\nStep 3  Simplify:')
t1 = prefactor_H                                                                   # (local)
t2 = t1 * (1.0 / eps_H)                                                            # (local)
t3 = t2 * F_amp_composite                                                          # (local)
t4 = t3 * (1.0 / c_sub)                                                            # (local)
t5 = t4 * f_conv                                                                   # (local)
print(f'  (H^2/8 pi^2)                                   = {t1:.15e}')
print(f'  * (1/eps_H)                                     = {t2:.15e}')
print(f'  * F_amp_composite                               = {t3:.15e}')
print(f'  * (1/c_sub)                                     = {t4:.15e}')
print(f'  * f_conv                                        = {t5:.15e}')
print(f'  A_s_rep                                         = {A_s_rep:.15e}')

# Step 4 — Direction (rel_err)
abs_err = abs(A_s_rep - A_s_target)                     # (local)
rel_err = abs_err / A_s_target                          # (local)
print('\nStep 4  Direction / rel_err:')
print(f'  A_s_target (G16 npz full precision) = {A_s_target:.15e}')
print(f'  A_s_rep                             = {A_s_rep:.15e}')
print(f'  abs_err  = |A_s_rep - A_s_target|   = {abs_err:.6e}')
print(f'  rel_err  = abs_err / A_s_target      = {rel_err:.6e}')

# Step 5 — Verdict
if rel_err < INFO_FLOOR:
    verdict = 'PASS'
elif rel_err < TOL:
    verdict = 'INFO'
else:
    verdict = 'FAIL'
print(f'\n  Thresholds: PASS rel_err<{TOL}, INFO in [{INFO_FLOOR},{TOL}], FAIL rel_err>={TOL}')
print(f'  VERDICT: {verdict}')

# =============================================================================
# SECTION 4 — CROSS-CHECKS
# =============================================================================

print('\n' + '=' * 78)
print('SECTION 4  Cross-checks')
print('=' * 78)

# CC-1: Identity d(ln A_s)/d(ln c_sub) = -1 (c_sub enters via (1/c_sub) factor)
#   Chain:  A_s = K / c_sub  =>  ln A_s = ln K - ln c_sub
#           d(ln A_s) / d(ln c_sub) = -1
c_sub_pert = c_sub * 1.01                                                  # (local)
A_s_pert1  = prefactor_H * (1.0/eps_H) * F_amp_composite * (1.0/c_sub_pert) * f_conv  # (local)
d_csub     = np.log(A_s_pert1 / A_s_rep) / np.log(c_sub_pert / c_sub)      # (local)
CC1_ok     = abs(d_csub + 1.0) < 1e-10                                     # (local)
print(f'  CC-1  d(ln A_s)/d(ln c_sub) = {d_csub:.12f}  (expected -1.0),  ok={CC1_ok}')

# CC-2: Identity d(ln A_s)/d(ln F_amp) = +1
F_amp_pert = F_amp_composite * 1.01                                        # (local)
A_s_pert2  = prefactor_H * (1.0/eps_H) * F_amp_pert * (1.0/c_sub) * f_conv # (local)
d_Famp     = np.log(A_s_pert2 / A_s_rep) / np.log(F_amp_pert / F_amp_composite)  # (local)
CC2_ok     = abs(d_Famp - 1.0) < 1e-10                                     # (local)
print(f'  CC-2  d(ln A_s)/d(ln F_amp) = {d_Famp:.12f}  (expected +1.0),  ok={CC2_ok}')

# CC-3: Identity d(ln A_s)/d(ln H_tilde) = +2 (H_tilde enters squared)
H_pert  = H_tilde_TD * 1.01                                                # (local)
pf_pert = H_pert**2 / (8.0 * np.pi**2)                                     # (local)
A_s_pert3 = pf_pert * (1.0/eps_H) * F_amp_composite * (1.0/c_sub) * f_conv # (local)
d_H    = np.log(A_s_pert3 / A_s_rep) / np.log(H_pert / H_tilde_TD)         # (local)
CC3_ok = abs(d_H - 2.0) < 1e-10                                            # (local)
print(f'  CC-3  d(ln A_s)/d(ln H_tilde) = {d_H:.12f}  (expected +2.0),  ok={CC3_ok}')

# CC-4: Bit-level identity: A_s_rep must equal G16 A_s_new_primary exactly
#   (same ops, same operands, same double precision)
g16_npz = np.load(SCRIPT_DIR / 's83_w2_g16_unified_as79_3pi_subst.npz',
                  allow_pickle=True)
A_s_g16 = float(g16_npz['A_s_new_primary'])                                # (local)
bit_match = (A_s_rep == A_s_g16)                                           # (local)
CC4_ok = bit_match                                                         # (local)
print(f'  CC-4  Bit-level equality vs G16 npz:')
print(f'        A_s_rep = {A_s_rep!r}')
print(f'        A_s_g16 = {A_s_g16!r}')
print(f'        exact equality = {CC4_ok}')

# CC-5: Pin-map completeness — every variable used in the ledger formula
#       appears as a key in the pin-map JSON.
required_keys = {'H_tilde_TD', 'eps_H', 'c_sub', 'f_conv',
                 'F_amp_3PI_pivot', 'k_a2', 'F_amp_composite'}            # (local)
missing = required_keys - set(pin_map.keys())                              # (local)
CC5_ok = (len(missing) == 0)                                               # (local)
print(f'  CC-5  Pin-map completeness:  missing keys = {sorted(missing)},  ok={CC5_ok}')

# CC-6: Pin-map JSON SHA is stable under re-serialization
pin_map_reserial = json.dumps(pin_map, sort_keys=True, separators=(',', ':'))  # (local)
sha_pin_reserial = hashlib.sha256(pin_map_reserial.encode('utf-8')).hexdigest() # (local)
CC6_ok = (sha_pin_reserial == sha_pin)                                     # (local)
print(f'  CC-6  Pin-map JSON SHA-256 stability under re-serialize: {CC6_ok}')

# CC-7: Verdict-line closure SHA uniqueness vs W3-26 / W3-28 (S84 audit remediation)
#   The __script__ + __gate_id__ embedding guarantees the closure SHA is
#   distinct from any other gate's closure even on identical data-file inputs.
#   Test: synthesize a narrow-pin closure (data-only, no __script__/__gate_id__)
#   and confirm it DIFFERS from the current closure.
narrow_pins = {k: v for k, v in input_pins.items()
               if not k.startswith('__')}                                  # (local)
narrow_string = ';'.join(f'{k}={v}' for k, v in sorted(narrow_pins.items()))  # (local)
narrow_sha = hashlib.sha256(narrow_string.encode('utf-8')).hexdigest()     # (local)
CC7_ok = (narrow_sha != closure_sha)                                       # (local)
print(f'  CC-7  Audit-unique closure SHA (w/ __script__, __gate_id__):')
print(f'        narrow   sha = {narrow_sha[:16]}...')
print(f'        canonical sha = {closure_sha[:16]}...')
print(f'        distinct = {CC7_ok}')

cross_checks_all_ok = bool(CC1_ok and CC2_ok and CC3_ok and CC4_ok
                           and CC5_ok and CC6_ok and CC7_ok)               # (local)
print(f'\n  ALL cross-checks ok:  {cross_checks_all_ok}')

# =============================================================================
# SECTION 5 — COMMIT PIN-MAP JSON
# =============================================================================

pin_map_json_path = SCRIPT_DIR / 's84_w3_as_pin_map.json'

# Include the computed SHA within the JSON itself (per task instruction:
# "SHA-256 recorded inside the JSON itself"). We embed it as a companion
# field so it is discoverable, while keeping the sha_pin_canonical field
# distinct as the hash of the pre-sha serialization.
pin_map_with_sha = dict(pin_map)
pin_map_with_sha['__sha_pin_canonical__'] = sha_pin
pin_map_with_sha['__closure_sha256__'] = closure_sha
pin_map_with_sha['__serialization_note__'] = (
    'sha_pin_canonical is sha256(json.dumps(pin_map, sort_keys=True, '
    "separators=(',',':'))) for the pin_map WITHOUT these three self-"
    'referential fields. Closure SHA is the ordered-input-pins-string hash '
    'used in the gate verdict line.'
)

with open(pin_map_json_path, 'w', encoding='utf-8') as fh:
    json.dump(pin_map_with_sha, fh, indent=2, sort_keys=True)

print('\n' + '=' * 78)
print('SECTION 5  Pin-map JSON committed')
print('=' * 78)
print(f'  Path      = {pin_map_json_path.name}')
print(f'  sha_pin   = {sha_pin}')
print(f'  closure   = {closure_sha}')

# =============================================================================
# SECTION 6 — VERDICT LINE
# =============================================================================

verdict_line = (
    f'{GATE_ID}: {verdict} -- '
    f'value=A_s_rep={A_s_rep:.6e},rel_err={rel_err:.3e},'
    f'bit_match=G16={CC4_ok},sha_pin={sha_pin[:16]} '
    f'scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} '
    f'sha256={closure_sha}'
)

print('\n' + '=' * 78)
print('SECTION 6  Verdict line')
print('=' * 78)
print(verdict_line)

# =============================================================================
# SECTION 7 — SAVE NPZ + APPEND VERDICT
# =============================================================================

out_npz = SCRIPT_DIR / 's84_w3_as_pin_map_commit.npz'

np.savez(
    out_npz,
    # Ledger inputs
    H_tilde_TD=H_tilde_TD,
    eps_H=eps_H,
    c_sub=c_sub,
    f_conv=f_conv,
    F_amp_3PI_pivot=F_amp_3PI_pivot,
    k_a2_A_primary=k_a2_A_primary,
    F_amp_composite=F_amp_composite,
    prefactor_H=prefactor_H,
    # Framework constants
    M_KK_val=float(M_KK_gravity),
    M_Pl_red=float(M_Pl_reduced),
    tau_fold_val=float(tau_fold),
    a0_fold_val=float(a0_fold),
    # Reproduction
    A_s_target=A_s_target,
    A_s_rep=A_s_rep,
    abs_err=abs_err,
    rel_err=rel_err,
    verdict=verdict,
    # Cross-checks
    CC1_d_csub=d_csub, CC1_ok=CC1_ok,
    CC2_d_Famp=d_Famp, CC2_ok=CC2_ok,
    CC3_d_H=d_H, CC3_ok=CC3_ok,
    CC4_bit_match=CC4_ok,
    CC5_missing_keys=np.array(sorted(missing), dtype=object),
    CC5_ok=CC5_ok,
    CC6_ok=CC6_ok,
    CC7_narrow_sha=narrow_sha, CC7_distinct=CC7_ok,
    cross_checks_all_ok=cross_checks_all_ok,
    # Closure metadata
    scheme=SCHEME,
    convention=CONVENTION,
    L_max=L_MAX,
    A_F=A_F,
    gate_id=GATE_ID,
    sha_pin=sha_pin,
    closure_sha=closure_sha,
    tolerance=TOL,
    info_floor=INFO_FLOOR,
    # JSON path
    pin_map_json=str(pin_map_json_path.name),
)
print(f'\nSaved: {out_npz.name}')

# Append verdict line to s84_gate_verdicts.txt
verdicts_path = SCRIPT_DIR / 's84_gate_verdicts.txt'
with open(verdicts_path, 'a') as fh:
    fh.write('\n' + verdict_line + '\n')
print(f'Appended verdict to: {verdicts_path.name}')

print('\n' + '=' * 78)
print(f'S84 W3-34 complete. Verdict: {verdict}')
print('=' * 78)
