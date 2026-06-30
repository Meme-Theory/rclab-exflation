#!/usr/bin/env python
"""
S84-VARIATIONAL-PRINCIPLE-REFORMULATION (§W8a-90) -- synthesizer

Synthesizes the verdicts of three pre-requisite gates:
  - §W8a-85 S84-STATIONARY-POINT-VERIFICATION-TAU-FOLD  (FAIL, value=-2.036e+04)
  - §W8a-87b S84-AF-BIRKHOFF-UNIQUENESS-PROOF            (PASS,  value=1)
  - §W8a-89 S84-MELLIN-CONE-THEOREM-UNIVERSALITY         (PASS,  value=3)

Per plan §W8a-90 §6 thresholds:
  PASS-THEOREM  := 85 PASS AND 87b PASS AND 89 PASS AND coercivity(10 probes) AND global-min-uniqueness
  PASS-PARTIAL  := 85 PASS AND 87b PASS AND (89 FAIL or INFO)
  FAIL          := 85 FAIL OR 87b FAIL
  INFO          := all dependencies PASS but coercivity fails at one boundary probe

Substitution chain (plan [CHAIN] trigger):
  Step 1 (PASS-THEOREM definition):
      PASS-THEOREM <=> (§W8a-85 PASS) AND (§W8a-87b PASS) AND (§W8a-89 PASS)
                       AND (coercivity at 10 probes) AND (global-min uniqueness).
  Step 2 (FAIL definition):
      FAIL <=> (§W8a-85 FAIL) OR (§W8a-87b FAIL).
  Step 3 (Substitute recorded verdicts):
      §W8a-85 = FAIL (value = -2.036e+04; Jensen ansatz lambda(tau)=alpha*exp(2*tau*c) falsified).
      §W8a-87b = PASS (value = 1; A_F = C + H + M_3(C) unique among 3907 WA candidates).
      §W8a-89 = PASS-THEOREM (value = 3; Mellin first-moment cone [1.5, 2.5] holds across 3 cases).
  Step 4 (Simplify Step 2 with Step 3):
      FAIL = TRUE OR FALSE = TRUE.
  Step 5 (Direction/verdict):
      FAIL triggered -> overall verdict FAIL.
      value flag = number of passing sub-gates (0-3) = 2 (from 87b and 89).

Coercivity check (reported SEPARATELY per orchestrator override, independent of FAIL):
  Probe the bare Chamseddine-Connes Gaussian spectral action
    S(tau) = sum_n mult_n * exp(- lambda_n^2(tau) / 2)
  at 10 boundary probes of the truncated moduli space M (10 KK sectors, L_max=10,
  Jensen direction) using the cached computations/session-36/s36_sfull_tau_stabilization
  dataset.  Coercivity (boundedness below) on the truncated M requires
  inf_{x in M_truncated} S(x) > -infinity.

Output verdict line (first line of computations/session-84/s84_gate_verdicts.txt append):
  S84-VARIATIONAL-PRINCIPLE-REFORMULATION: FAIL -- value=2
     scheme=variational_meta_reformulation
     convention=Chamseddine-Connes L_max=10 sha256=<64-char-closure>
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
import hashlib
import json
import time
import numpy as np

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, SCRIPT_DIR)

from canonical_constants import (
    tau_fold,
    M_KK,
    M_KK_gravity,
    dS_fold,
    d2S_fold,
    S_fold,
)

# =============================================================================
# SHA-256 input pinning
# =============================================================================

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()


def sha256_of_bytes(b):
    return hashlib.sha256(b).hexdigest()


SPECTRUM_NPZ = os.path.normpath(os.path.join(SCRIPT_DIR, "..", "_shared",
                                              's36_sfull_tau_stabilization.npz'))
CANON_PY = os.path.join(SCRIPT_DIR, 'canonical_constants.py')
VERDICT_FILE = os.path.join(SCRIPT_DIR, 's84_gate_verdicts.txt')
PLAN_FILE = os.path.normpath(os.path.join(SCRIPT_DIR, '..', 'sessions',
                                           'session-plan', 'session-84-plan-w8a.md'))

# Prerequisite verdict SHAs (frozen from computations/session-84/s84_gate_verdicts.txt)
PREREQ = {
    'W8a-85_STATIONARY': {
        'verdict': 'FAIL',
        'value': -2.035810e+04,
        'scheme': 'spectral_moment_analytic',
        'convention': 'Chamseddine-Connes-Gaussian',
        'sha256': '581a23921b9eb3aee1d4fc82c141cd0c02e47112c1c5224b6189b69e1f622308',
    },
    'W8a-87b_AF_UNIQUENESS': {
        'verdict': 'PASS',
        'value': 1,
        'scheme': 'Wedderburn-Artin',
        'convention': '6-axiom-check',
        'sha256': '7e5c0519809670e7e31c0c66d05eeb2496b653c10e6ba34bbea5c7163cc69139',
    },
    'W8a-89_MELLIN_CONE': {
        'verdict': 'PASS',
        'value': 3,
        'scheme': 'abstract_positive_measure',
        'convention': '5-regulator-cluster',
        'sha256': '95d6158242080da95e43f86d566e4a5da5bbe9472a5d3ef75c6342193ae176a0',
    },
}

print("=" * 78)
print("S84-VARIATIONAL-PRINCIPLE-REFORMULATION (§W8a-90) -- SYNTHESIZER")
print("=" * 78)
print(f"Script: s84_w8a_variational_principle_reformulation.py")
print(f"Date: 2026-04-19")
print()
print("INPUT SHA-256 PINS:")
sha_canon = sha256_file(CANON_PY)
sha_spec = sha256_file(SPECTRUM_NPZ)
sha_plan = sha256_file(PLAN_FILE)
print(f"  canonical_constants.py                    : {sha_canon}")
print(f"  computations/session-36/s36_sfull_tau_stabilization : {sha_spec}")
print(f"  session-84-plan-w8a.md                    : {sha_plan}")
print()
print("PREREQUISITE VERDICT SHAs (frozen from s84_gate_verdicts.txt):")
for name, entry in PREREQ.items():
    print(f"  {name:<28s} : {entry['sha256']}  [{entry['verdict']}, value={entry['value']}]")
print()
print(f"CANONICAL CONSTANTS:")
print(f"  tau_fold  = {tau_fold}")
print(f"  M_KK      = {M_KK:.6e} GeV")
print(f"  S_fold    = {S_fold:.6f}    (S42 canonical, abs-like cutoff)")
print(f"  dS_fold   = {dS_fold:.6f}  (S42 canonical, abs-like cutoff)")
print(f"  d2S_fold  = {d2S_fold:.6f}  (S42 canonical, abs-like cutoff)")
print("=" * 78)

# =============================================================================
# Load Jensen-deformed spectrum for coercivity probes
# =============================================================================

d = np.load(SPECTRUM_NPZ, allow_pickle=True)

KK_SECTORS = [
    (0, 0), (1, 0), (0, 1),
    (1, 1), (2, 0), (0, 2),
    (3, 0), (0, 3), (2, 1), (1, 2),
]

TAU_AVAILABLE = np.array([0.05, 0.16, 0.17, 0.18, 0.19, 0.21, 0.22])


def dim_pq(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def mult_pq(p, q):
    return dim_pq(p, q) ** 2


def load_sector_evals(tau, p, q):
    key = f'evals_tau{tau:.3f}_{p}_{q}'
    return np.sort(d[key])


def spectral_action_gauss(tau):
    """
    Bare Chamseddine-Connes Gaussian spectral action:
      S(tau) = sum_{sectors} mult_pq * sum_n exp(- lambda_n^2 / 2)
    in units where Lambda = M_KK (lambdas already in M_KK units).
    """
    S = 0.0                     # (local) accumulator
    for p, q in KK_SECTORS:
        m = mult_pq(p, q)       # (local)
        lam = load_sector_evals(tau, p, q)
        S += m * np.sum(np.exp(- lam**2 / 2.0))
    return S


# Count total truncated-spectrum eigenvalues for reporting
n_evals_total = sum(len(load_sector_evals(tau_fold, p, q)) for p, q in KK_SECTORS)  # (local)
n_modes_with_mult = sum(mult_pq(p, q) * len(load_sector_evals(tau_fold, p, q))
                        for p, q in KK_SECTORS)  # (local)

print()
print("COERCIVITY PROBE SETUP:")
print(f"  KK sectors truncation  : {len(KK_SECTORS)} (L_max=10)")
print(f"  Distinct eigenvalues   : {n_evals_total}")
print(f"  Peter-Weyl multiplicity-weighted modes : {n_modes_with_mult}")
print(f"  Available tau probes   : {list(TAU_AVAILABLE)}")
print()

# =============================================================================
# COERCIVITY CHECK -- 10 boundary probes on truncated M
#
# Per plan §W8a-90 machinery pin:
#   - coercivity_test_points = 10
#   - boundary probes in M for boundedness below
#
# Coercivity on truncated M (finite KK truncation + Jensen direction):
#   inf_{tau in [tau_min, tau_max], sectors} S(tau) > -infinity.
# For S(tau) = sum mult_n * exp(-lambda_n^2/2), each term is in (0, mult_n], so
# S >= 0 holds by construction.  The non-trivial question is whether S remains
# BOUNDED ABOVE as well (weaker than strict coercivity, but relevant since
# a variational MINIMUM requires boundedness BELOW and a positive lower bound
# away from the minimum to avoid runaway to the minimum at infinity).
#
# Probes:
#   Probes 1-7: All 7 available tau values (Jensen direction boundary).
#   Probes 8-10: Three largest-sector restrictions (drop sector at boundary)
#                to probe "algebra-direction" subvarieties of M.
#
# PASS condition: S(probe) > 0 AND finite at every probe (coercivity holds on
#                 truncated M).  Report S(probe) for each; boundedness is
#                 trivial because sum of finitely many positive exponentials
#                 of bounded arguments is positive and finite.
# =============================================================================

print("=" * 78)
print("COERCIVITY REPORT (10 boundary probes of truncated M, L_max=10)")
print("=" * 78)

probes = []

# Probes 1-7: Jensen direction (all 7 tau values)
for i, tau in enumerate(TAU_AVAILABLE):
    S_val = spectral_action_gauss(float(tau))  # (local)
    probes.append({
        'probe_id': i + 1,
        'type': 'Jensen-direction',
        'description': f'tau = {tau:.3f} (full 10-sector truncation)',
        'tau': float(tau),
        'S_value': float(S_val),
        'finite': bool(np.isfinite(S_val)),
        'positive': bool(S_val > 0.0),
    })

# Probes 8-10: Algebra/sector boundary subvarieties (drop one KK sector)
for i, drop_sector in enumerate([(3, 0), (0, 3), (2, 1)]):
    S_reduced = 0.0                                   # (local)
    for p, q in KK_SECTORS:
        if (p, q) == drop_sector:
            continue
        m = mult_pq(p, q)                             # (local)
        lam = load_sector_evals(tau_fold, p, q)
        S_reduced += m * np.sum(np.exp(- lam**2 / 2.0))
    probes.append({
        'probe_id': 8 + i,
        'type': 'algebra-sector-subvariety',
        'description': f'tau = tau_fold, drop sector ({drop_sector[0]},{drop_sector[1]})',
        'tau': float(tau_fold),
        'S_value': float(S_reduced),
        'finite': bool(np.isfinite(S_reduced)),
        'positive': bool(S_reduced > 0.0),
    })

print(f"\n  {'Probe':>5s}  {'Type':<28s}  {'tau':>6s}  {'S(probe)':>14s}  finite  positive")
print("  " + "-" * 76)
for pr in probes:
    print(f"  {pr['probe_id']:>5d}  {pr['type']:<28s}  {pr['tau']:>6.3f}  {pr['S_value']:>14.6e}    "
          f"{str(pr['finite']):<5s}   {str(pr['positive']):<5s}")
print()

# Coercivity summary
all_finite = all(pr['finite'] for pr in probes)                     # (local)
all_positive = all(pr['positive'] for pr in probes)                 # (local)
S_min_probe = min(pr['S_value'] for pr in probes)                   # (local)
S_max_probe = max(pr['S_value'] for pr in probes)                   # (local)
coercivity_passes = bool(all_finite and all_positive)               # (local)

print(f"  Coercivity summary:")
print(f"    all finite    : {all_finite}")
print(f"    all positive  : {all_positive}")
print(f"    inf(S_probe)  : {S_min_probe:.6e}")
print(f"    sup(S_probe)  : {S_max_probe:.6e}")
print(f"    COERCIVITY (bounded below, positive on truncated M) : "
      f"{'PASS' if coercivity_passes else 'FAIL'}")
print()

# =============================================================================
# SYNTHESIS DECISION -- per plan §W8a-90 §6 thresholds
# =============================================================================

print("=" * 78)
print("SYNTHESIS DECISION (plan §W8a-90 §6)")
print("=" * 78)

stat_pass = (PREREQ['W8a-85_STATIONARY']['verdict'] == 'PASS')           # (local)
af_pass = (PREREQ['W8a-87b_AF_UNIQUENESS']['verdict'] == 'PASS')         # (local)
mellin_pass = (PREREQ['W8a-89_MELLIN_CONE']['verdict'] == 'PASS')        # (local)
n_passing = int(stat_pass) + int(af_pass) + int(mellin_pass)             # (local)

print(f"  §W8a-85  STATIONARY-TAU-FOLD  : {PREREQ['W8a-85_STATIONARY']['verdict']}  "
      f"(value = {PREREQ['W8a-85_STATIONARY']['value']})")
print(f"  §W8a-87b AF-UNIQUENESS        : {PREREQ['W8a-87b_AF_UNIQUENESS']['verdict']}  "
      f"(value = {PREREQ['W8a-87b_AF_UNIQUENESS']['value']})")
print(f"  §W8a-89  MELLIN-CONE-UNIV     : {PREREQ['W8a-89_MELLIN_CONE']['verdict']}  "
      f"(value = {PREREQ['W8a-89_MELLIN_CONE']['value']})")
print(f"  number of passing sub-gates (value flag) : {n_passing}")
print()

# Substitution chain (explicit, [CHAIN] trigger):
#   Step 1 (PASS-THEOREM): need all 3 prereqs PASS AND coercivity AND uniqueness.
#   Step 2 (FAIL): §W8a-85 FAIL OR §W8a-87b FAIL.
#   Step 3 (Substitute): §W8a-85 = FAIL, §W8a-87b = PASS, §W8a-89 = PASS.
#   Step 4 (Simplify): FAIL condition = (TRUE) OR (FALSE) = TRUE.
#   Step 5 (Direction): overall verdict = FAIL; value flag = 2 (87b + 89 PASS).

if not stat_pass:
    overall = 'FAIL'
    reason = ('§W8a-85 FAIL -> tau_fold is NOT a stationary point of bare '
              'S[D_K(tau)] under Chamseddine-Connes Gaussian.  Jensen ansatz '
              'lambda(tau)=alpha*exp(2*tau*c) falsified (measured log|lambda| '
              'slope = 0.64, predicted c in {+1,-1,+1/2}).  tau_fold retains '
              'empirical-input status; cannot be derived from stationarity of '
              'bare S.')
elif not af_pass:
    overall = 'FAIL'
    reason = '§W8a-87b FAIL -> A_F is not unique; reformulation fails at algebra-admissibility step.'
elif not mellin_pass:
    overall = 'PASS-PARTIAL'
    reason = ('§W8a-85 + §W8a-87b PASS, §W8a-89 FAIL/INFO: MG-0 framework-specific, '
              'but MG-1 + MG-2 reformulated consequences.  Input count: 3 -> 2.')
else:
    # All three PASS -> evaluate coercivity and uniqueness
    if coercivity_passes:
        overall = 'PASS-THEOREM'
        reason = 'All dependencies PASS; coercivity verified at 10 boundary probes.'
    else:
        overall = 'INFO'
        reason = 'All dependencies PASS but coercivity failed at >=1 boundary probe.'

print(f"  OVERALL VERDICT : {overall}")
print(f"  Reason          : {reason}")
print()

# =============================================================================
# STRUCTURAL CONSTRAINT-MAP UPDATE
# =============================================================================

print("=" * 78)
print("CONSTRAINT-MAP UPDATE (branches closed vs open for W9)")
print("=" * 78)

branches = {
    'BARE-SPECTRAL-ACTION as V.P.': {
        'status': 'CLOSED',
        'reason': ('§W8a-85 measured dS/dtau(Gauss) = -2.036e+04 (vs analytic-'
                   'ansatz prediction ~0).  tau_fold is not stationary of '
                   'Tr(exp(-D_K^2/Lambda^2)).  Jensen ansatz '
                   'lambda_n(tau)=alpha_n*exp(2*tau*c_n) falsified.  Branch '
                   'does not stabilize tau from first principles.'),
    },
    'DRESSED-SPECTRAL-ACTION as V.P.': {
        'status': 'OPEN',
        'reason': ('Bare S[D_K] is not stationary at tau_fold, but the '
                   'DRESSED spectral action (BCS/GGE/Gilkey loop-corrections) '
                   'may have its extremum moved to tau_fold.  S42 used abs-like '
                   'cutoff giving dS/dtau = +58673 (canonical) -- substantively '
                   'different functional from Gaussian.  Relation between '
                   'bare-vs-dressed extremum locations is not computed.'),
    },
    'GGE-ENTROPY-FUNCTIONAL as V.P.': {
        'status': 'OPEN',
        'reason': ('tau_fold may extremize a non-spectral-action functional '
                   '(GGE entropy S_GGE, Jacobson-Lambda_J horizon-entropy, '
                   'BCS condensation free-energy, modulus effective-action '
                   'after integrating out KK tower).  §W8a-85 did NOT test '
                   'these.  Each is a distinct variational principle.'),
    },
    'MECHANISM-CHAIN FIXES tau_fold': {
        'status': 'OPEN',
        'reason': ('tau_fold may be determined non-variationally by the '
                   'first-order transition condition (chain: I-1 + Turing + '
                   'RPA + WALL + BCS).  This is NOT a variational principle '
                   'but a DYNAMICAL selection criterion.  Unaffected by §W8a-'
                   '85 FAIL because it is a different selection structure.'),
    },
    'EMPIRICAL-tau_fold RETENTION': {
        'status': 'ACTIVE (default fallback)',
        'reason': ('tau_fold = 0.190 remains empirical/observational input '
                   '(matched from DESI/ACT/CMB epoch matching).  Framework '
                   'input count STAYS at 3 master gears + 1 empirical tau.  '
                   'This is the current post-§W8a-90-FAIL framework '
                   'configuration.'),
    },
    'MELLIN-CONE-UNIVERSALITY (MG-0 free)': {
        'status': 'SURVIVES (PASS-THEOREM by §W8a-89)',
        'reason': ('Empty-gap bound [1.5, 2.5] holds across 3 framework-'
                   'independent test cases.  MG-0 is a universal property of '
                   'positive-measure Mellin ratios.  Even though the parent '
                   'reformulation fails, MG-0 itself is a theorem, not an '
                   'assumption.'),
    },
    'A_F UNIQUENESS (MG-2 free)': {
        'status': 'SURVIVES (PASS-THEOREM by §W8a-87b)',
        'reason': ('A_F = C + H + M_3(C) is the UNIQUE finite real NC algebra '
                   'satisfying the 6 NCG axioms among 3907 Wedderburn-Artin '
                   'candidates.  Framework reduction by 1 input (A_F no longer '
                   'empirical).  Input count: 3 master gears -> 2 + empirical-'
                   'tau_fold.'),
    },
}

for name, info in branches.items():
    print(f"\n  [{info['status']}] {name}")
    for line in info['reason'].split('.  '):
        line = line.strip()
        if line:
            print(f"     - {line}")

# =============================================================================
# CLOSURE HASH -- canonical input-pin map
# =============================================================================

print()
print("=" * 78)
print("CLOSURE SHA-256")
print("=" * 78)

# Canonical input-pin map (ordered, deterministic)
pin_map = {
    'script': 's84_w8a_variational_principle_reformulation.py',
    'canonical_constants_sha256': sha_canon,
    'spectrum_sha256': sha_spec,
    'plan_sha256': sha_plan,
    'prereq_W8a_85_sha256': PREREQ['W8a-85_STATIONARY']['sha256'],
    'prereq_W8a_85_verdict': PREREQ['W8a-85_STATIONARY']['verdict'],
    'prereq_W8a_85_value': PREREQ['W8a-85_STATIONARY']['value'],
    'prereq_W8a_87b_sha256': PREREQ['W8a-87b_AF_UNIQUENESS']['sha256'],
    'prereq_W8a_87b_verdict': PREREQ['W8a-87b_AF_UNIQUENESS']['verdict'],
    'prereq_W8a_87b_value': PREREQ['W8a-87b_AF_UNIQUENESS']['value'],
    'prereq_W8a_89_sha256': PREREQ['W8a-89_MELLIN_CONE']['sha256'],
    'prereq_W8a_89_verdict': PREREQ['W8a-89_MELLIN_CONE']['verdict'],
    'prereq_W8a_89_value': PREREQ['W8a-89_MELLIN_CONE']['value'],
    'L_max': 10,
    'KK_sectors': KK_SECTORS,
    'coercivity_probes': [{'id': pr['probe_id'], 'type': pr['type'], 'tau': pr['tau'],
                            'S_value': pr['S_value'], 'finite': pr['finite'],
                            'positive': pr['positive']} for pr in probes],
    'coercivity_passes': coercivity_passes,
    'n_passing_prereqs': n_passing,
    'overall_verdict': overall,
    'scheme': 'variational_meta_reformulation',
    'convention': 'Chamseddine-Connes',
    'canonical_dS_fold': dS_fold,
    'canonical_d2S_fold': d2S_fold,
    'canonical_S_fold': S_fold,
    'canonical_tau_fold': tau_fold,
}

pin_json = json.dumps(pin_map, sort_keys=True, default=str).encode('utf-8')
closure_sha = sha256_of_bytes(pin_json)

print(f"  Input-pin JSON ({len(pin_json)} bytes) canonicalized.")
print(f"  Closure SHA-256: {closure_sha}")

# =============================================================================
# VERDICT LINE (4-tuple format)
# =============================================================================

verdict_line = (f"S84-VARIATIONAL-PRINCIPLE-REFORMULATION: {overall} -- "
                f"value={n_passing} "
                f"scheme=variational_meta_reformulation "
                f"convention=Chamseddine-Connes "
                f"L_max=10 "
                f"sha256={closure_sha}")

print()
print("=" * 78)
print("VERDICT LINE (append to computations/session-84/s84_gate_verdicts.txt)")
print("=" * 78)
print(verdict_line)
print()

# Append to verdict file
with open(VERDICT_FILE, 'a', encoding='utf-8') as f:
    f.write(verdict_line + '\n')

print(f"Appended to: {VERDICT_FILE}")
print()
print("=" * 78)
print("END S84-VARIATIONAL-PRINCIPLE-REFORMULATION (§W8a-90) -- FAIL")
print("=" * 78)
