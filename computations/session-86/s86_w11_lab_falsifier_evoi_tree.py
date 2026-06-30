#!/usr/bin/env python3
"""
S86 W11-2: S86-LAB-FALSIFIER-EVOI-TREE (C6)
=====================================================================
EVOI-tier ladder + 4-branch 5-yr decision tree for the 9 W8-4 lab
observables, using C5's per-row detection_ratio = SI_value / sigma_detect.

Gate: S86-LAB-FALSIFIER-EVOI-TREE  [AUDIT]
Classification: PHONONIC (5-yr decision-tree pre-registration over
                substrate excitations measured at table-top scale).
Owner: sagan-empiricist
Plan: sessions/session-plan/session-86-plan-w11.md §W11-2

INPUT (from C5 outputs; this script READS but does NOT recompute):
  - sessions/archive/session-86/computation-artifacts/s86_w11_lab_si_translation.csv
    (sha256 = bf78cdb4bc9d7b28e1023249eb08ba15deaa653aee8b55f0b908327a0d09ec9a)
  - sessions/archive/session-86/computation-artifacts/s86_w11_lab_si_translation.json
    (sha256 = cee9552d51101958abbe7397d35a0df3e3d2cf308e96a60cb06dd841d48ac218)

PRE-REGISTERED TIER LADDER (plan §W11-2 Step B; FROZEN, no scheme-shop):
  detection_ratio >= 10        -> LAB-FALSIFIER-A  (decisive)
  3 <= detection_ratio < 10    -> LAB-FALSIFIER-B  (strong)
  1 <= detection_ratio < 3     -> LAB-FALSIFIER-C  (marginal)
  detection_ratio < 1          -> LAB-FALSIFIER-D  (sub-floor)

PRE-REGISTERED 4-BRANCH DECISION TREE (plan §W11-2 Step C; FROZEN):
  Branch 1 detect-strong:    s_obs/sigma >= max(3, 0.5*detection_ratio)
  Branch 2 detect-marginal:  1 <= s_obs/sigma < 3
  Branch 3 null-strong:      s_obs/sigma < 1  AND  detection_ratio >= 3
  Branch 4 null-marginal:    s_obs/sigma < 1  AND  detection_ratio < 3

EXPERIMENT FAMILY PIN (plan §7 PRDR; literature-anchored, from C5):
  3He-A:  Aalto/Helsinki ROTA NMR        (arXiv:1005.0546)
  FeSe :  Florence/Grenoble 77Se NMR     (arXiv:2010.01020)
  173Yb:  Florence/JILA/Munich SU(N) lat (arXiv:0905.4948)

DECISION HORIZON: 2026-2031 (5-yr terrestrial-lab horizon per
                  partition manifest §1 W14-W6 NEW row class).

SUBSTITUTION CHAIN (plan §10 reproduced with C5's actual ratios):
  All 9 rows have detection_ratio >> 10:
    SW1=58958.86, SW2=72.90, SW3=28.50,
    XA1=58958.86, XA2=30.70, XA3=54.94,
    XB1=19652.95, XB2=72.90, XB3=131.85
  Step B threshold (>=10) is satisfied by all 9 rows -> 9x A-tier.
  EVOI(A) > EVOI(B) > EVOI(C) > EVOI(D)~0 (plan §10 ordering);
  hence the lab-falsifier portfolio sits at the MAXIMAL EVOI tier
  for the 5-yr horizon at fixed cost (one experiment family per row).

PASS / FAIL / INFO (plan §9):
  PASS iff: 9 rows in CSV+JSON; every row has tier_assignment in {A,B,C,D};
            every row has all 4 branch_conditions populated as explicit
            numerical inequalities; every row has experiment_family_pinned.
  FAIL iff: any row missing tier or branch or experiment_family.
  INFO iff: at least one row tier=D AND no SHA-pinned R&D roadmap.
            (Predicted: 0x D-tier given C5 ratios all >> 10.)

NO GPU. NO FIT. NO SCAN. CPU-only with OMP_NUM_THREADS=8.
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
import json
import csv
import hashlib

# ============================================================
# SECTION 0: Canonical-constant import (per CLAUDE.md, math-scripts.md)
# ============================================================
HERE = os.path.dirname(os.path.abspath(__file__))                     # (local)
sys.path.insert(0, HERE)
from canonical_constants import M_KK  # noqa: E402

PROJECT_ROOT = os.path.abspath(os.path.join(HERE, os.pardir))         # (local)

# ============================================================
# SECTION 1: Constants -- gate metadata + pre-registered pins
# ============================================================
GATE_ID = "S86-LAB-FALSIFIER-EVOI-TREE"                               # (local)
SCHEME = "LAB_FALSIFIER_ladder"                                       # (local)
CONVENTION = "2026_2031_horizon"                                      # (local)
L_MAX = "N/A"                                                         # (local)

# Pre-registered tier-ladder thresholds (plan §W11-2 Step B; FROZEN)
TIER_THRESH_A = 10.0                                                  # (local) detection_ratio >= 10
TIER_THRESH_B = 3.0                                                   # (local) detection_ratio in [3, 10)
TIER_THRESH_C = 1.0                                                   # (local) detection_ratio in [1, 3)

# Pre-registered branch thresholds on s_obs/sigma_detect (plan §W11-2 Step C)
BRANCH_DETECT_STRONG_FLOOR = 3.0                                      # (local) Branch 1: s/sigma >= 3
BRANCH_DETECT_MARG_LOW = 1.0                                          # (local) Branch 2: s/sigma in [1, 3)
BRANCH_NULL_FLOOR = 1.0                                               # (local) Branch 3/4: s/sigma < 1
BRANCH_NULL_STRONG_DR_FLOOR = 3.0                                     # (local) Branch 3: detection_ratio >= 3

DECISION_HORIZON_YEAR = 2031                                          # (local) 5-yr horizon end

# Per-platform experiment-family pin (plan §7 PRDR)
EXPERIMENT_FAMILY = {                                                 # (local)
    '3He-A': 'Aalto/Helsinki ROTA NMR (arXiv:1005.0546)',
    'FeSe':  'Florence/Grenoble 77Se NMR (arXiv:2010.01020)',
    '173Yb': 'Florence/JILA/Munich SU(N) optical lattice (arXiv:0905.4948)',
}

# Detector R&D roadmap registry (SHA-pinned). For LAB-FALSIFIER-D rows only.
# Plan §9 INFO clause: INFO fires iff a tier-D row LACKS a SHA-pinned roadmap.
DETECTOR_RD_ROADMAP_REGISTRY = {                                      # (local)
    # No tier-D rows expected (all C5 ratios >> 10); registry empty by design.
}

# Pre-registered orchestrator-pinned input SHAs (echo-check; hard-fail mismatch)
EXPECTED_SHA_C5_CSV = (                                               # (local)
    "bf78cdb4bc9d7b28e1023249eb08ba15deaa653aee8b55f0b908327a0d09ec9a"
)
EXPECTED_SHA_C5_JSON = (                                              # (local)
    "cee9552d51101958abbe7397d35a0df3e3d2cf308e96a60cb06dd841d48ac218"
)
EXPECTED_C5_AUDIT_SHA = (                                             # (local) for verdict-trace cross-cite
    "6a2d523920c340321fe537672a39aa6d971a81c330236d78aee59138900628ce"
)

# Path pins
C5_CSV_PATH = os.path.join(                                           # (local)
    PROJECT_ROOT, 'sessions', 'session-86', 'computation-artifacts',
    's86_w11_lab_si_translation.csv'
)
C5_JSON_PATH = os.path.join(                                          # (local)
    PROJECT_ROOT, 'sessions', 'session-86', 'computation-artifacts',
    's86_w11_lab_si_translation.json'
)
CANONICAL_PY = os.path.join(HERE, 'canonical_constants.py')           # (local)
OUT_CSV_PATH = os.path.join(                                          # (local)
    PROJECT_ROOT, 'sessions', 'session-86', 'computation-artifacts',
    's86_w11_lab_falsifier_evoi_tree.csv'
)
OUT_JSON_PATH = os.path.join(                                         # (local)
    PROJECT_ROOT, 'sessions', 'session-86', 'computation-artifacts',
    's86_w11_lab_falsifier_evoi_tree.json'
)
VERDICT_PATH = os.path.join(HERE, 's86_gate_verdicts.txt')            # (local) canonical per gate-verdicts.md

# ============================================================
# SECTION 2: Header banner
# ============================================================
print("=" * 76)
print(f"{GATE_ID} (C6)")
print("=" * 76)
print(f"Scheme: {SCHEME}")
print(f"Convention: {CONVENTION}")
print(f"L_max: {L_MAX}")
print(f"Decision horizon: 2026-{DECISION_HORIZON_YEAR}")
print(f"M_KK (canonical): {M_KK:.6e} GeV  (imported, unused in C6 logic)")
print()

# ============================================================
# SECTION 3: Input-SHA echo-check (MANDATORY; first 20 lines per gate-verdicts.md)
# ============================================================
print("[SEC 3] Input-SHA echo-check (orchestrator pin assertion)")


def _sha256_of_file(path):                                            # (local)
    h = hashlib.sha256()                                              # (local)
    with open(path, 'rb') as fh:
        for chunk in iter(lambda: fh.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()


csv_sha = _sha256_of_file(C5_CSV_PATH)                                # (local)
json_sha = _sha256_of_file(C5_JSON_PATH)                              # (local)
canonical_sha = _sha256_of_file(CANONICAL_PY)                         # (local)

print(f"  C5 CSV  : {C5_CSV_PATH}")
print(f"            sha256 = {csv_sha}")
print(f"            expect = {EXPECTED_SHA_C5_CSV}")
csv_match = (csv_sha == EXPECTED_SHA_C5_CSV)                          # (local)
print(f"            MATCH  = {csv_match}")

print(f"  C5 JSON : {C5_JSON_PATH}")
print(f"            sha256 = {json_sha}")
print(f"            expect = {EXPECTED_SHA_C5_JSON}")
json_match = (json_sha == EXPECTED_SHA_C5_JSON)                       # (local)
print(f"            MATCH  = {json_match}")

print(f"  canonical_constants.py : {canonical_sha}")
print(f"  C5 audit_sha256 (cross-cite) = {EXPECTED_C5_AUDIT_SHA}")

INPUT_SHAS = {                                                        # (local)
    'sessions/archive/session-86/computation-artifacts/s86_w11_lab_si_translation.csv': csv_sha,
    'sessions/archive/session-86/computation-artifacts/s86_w11_lab_si_translation.json': json_sha,
    'computations/_shared/canonical_constants.py': canonical_sha,
}

if not (csv_match and json_match):
    print("\n[SEC 3] HARD HALT: input SHA mismatch on at least one C5 artifact.")
    fail_value = 'input-sha-mismatch'                                 # (local)
    fail_pin = {                                                      # (local)
        'GATE_ID': GATE_ID,
        'SCHEME': SCHEME,
        'CONVENTION': CONVENTION,
        'L_MAX': L_MAX,
        'csv_sha': csv_sha,
        'json_sha': json_sha,
        'expected_csv_sha': EXPECTED_SHA_C5_CSV,
        'expected_json_sha': EXPECTED_SHA_C5_JSON,
        'verdict': 'FAIL',
        'value': fail_value,
    }
    fail_pin_json = json.dumps(fail_pin, sort_keys=True,              # (local)
                               separators=(',', ':')).encode('utf-8')
    with open(os.path.abspath(__file__), 'rb') as _fh:
        fail_script_bytes = _fh.read()                                # (local)
    fail_audit = hashlib.sha256()                                     # (local)
    fail_audit.update(fail_script_bytes)
    fail_audit.update(fail_pin_json)
    fail_audit_sha = fail_audit.hexdigest()                           # (local)
    fail_content_sha = hashlib.sha256(                                # (local)
        fail_script_bytes
    ).hexdigest()
    fail_verdict_line = (                                             # (local)
        f"{GATE_ID}: FAIL -- value={fail_value!r} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={fail_audit_sha} content_sha256={fail_content_sha} "
        f"schema_version=R3\n"
    )
    fail_companion = (                                                # (local)
        f"# audit_sha256 companion row: {GATE_ID} "
        f"audit={fail_audit_sha[:16]} content={fail_content_sha[:16]}\n"
    )
    with open(VERDICT_PATH, 'a', encoding='utf-8') as fv:
        fv.write(fail_verdict_line)
        fv.write(fail_companion)
    sys.exit(0)  # script ran cleanly; verdict is FAIL (data, not exit code)

print("  All input SHAs match. Proceeding.\n")

# ============================================================
# SECTION 4: Read C5 row data (CSV is canonical for row-data ingest;
#            JSON used for provisional flags + literature anchors)
# ============================================================
print("[SEC 4] Ingest C5 9-row table from CSV + JSON")

with open(C5_CSV_PATH, 'r', encoding='utf-8', newline='') as fh:
    reader = csv.DictReader(fh)                                       # (local)
    c5_rows = list(reader)                                            # (local)
print(f"  CSV rows ingested: {len(c5_rows)} (expect 9)")
assert len(c5_rows) == 9, f"C5 CSV must have 9 rows; got {len(c5_rows)}"

with open(C5_JSON_PATH, 'r', encoding='utf-8') as fh:
    c5_json = json.load(fh)                                           # (local)
provisional_set = set(c5_json.get('provisional_rows', []))            # (local)
print(f"  JSON provisional_rows: {sorted(provisional_set)} "
      f"({len(provisional_set)} of 9)")

# ============================================================
# SECTION 5: Tier ladder definition (top-level JSON field; W14-citable)
# ============================================================
print("\n[SEC 5] Pre-registered LAB-FALSIFIER tier ladder")

TIER_LADDER_DEFINITION = {                                            # (local)
    'class_name': 'LAB-FALSIFIER',
    'introduced_in_session': 'S86',
    'introduced_by_gate': GATE_ID,
    'p_decisive_band': [0.30, 0.50],
    'p_decisive_provenance': (
        "partition manifest §1 W14-W6 NEW row class entry "
        "(5-yr terrestrial-lab horizon)"
    ),
    'horizon_years': [2026, DECISION_HORIZON_YEAR],
    'is_new_class': True,
    'is_shuffle_of_existing_tier': False,
    'tiers': {
        'LAB-FALSIFIER-A': {
            'detection_ratio_rule': 'detection_ratio >= 10',
            'detection_ratio_lower_inclusive': 10.0,
            'detection_ratio_upper_inclusive': None,
            'descriptor': 'decisive (signal >= 10x above floor)',
        },
        'LAB-FALSIFIER-B': {
            'detection_ratio_rule': '3 <= detection_ratio < 10',
            'detection_ratio_lower_inclusive': 3.0,
            'detection_ratio_upper_inclusive': 10.0,
            'descriptor': 'strong (signal 3-10x above floor)',
        },
        'LAB-FALSIFIER-C': {
            'detection_ratio_rule': '1 <= detection_ratio < 3',
            'detection_ratio_lower_inclusive': 1.0,
            'detection_ratio_upper_inclusive': 3.0,
            'descriptor': 'marginal (signal at floor to 3x above)',
        },
        'LAB-FALSIFIER-D': {
            'detection_ratio_rule': 'detection_ratio < 1',
            'detection_ratio_lower_inclusive': None,
            'detection_ratio_upper_inclusive': 1.0,
            'descriptor': ('sub-floor (signal below current sigma_detect; '
                           'watch detector R&D)'),
        },
    },
    'branch_thresholds_on_s_obs_over_sigma': {
        'detect_strong_floor': 3.0,
        'detect_marginal_low': 1.0,
        'null_floor': 1.0,
        'null_strong_detection_ratio_floor': 3.0,
    },
}
print(f"  Tier ladder fields: {sorted(TIER_LADDER_DEFINITION['tiers'].keys())}")

# ============================================================
# SECTION 6: Per-row tier assignment + 4-branch decision tree
#            (Steps A-D of plan §W11-2 Method)
# ============================================================
print("\n[SEC 6] Per-row tier + 4-branch decision-tree assignment")


def _assign_tier(detection_ratio):                                    # (local)
    """Pre-registered tier ladder (plan §W11-2 Step B). NO scheme-shop."""
    if detection_ratio >= TIER_THRESH_A:
        return 'LAB-FALSIFIER-A'
    if detection_ratio >= TIER_THRESH_B:
        return 'LAB-FALSIFIER-B'
    if detection_ratio >= TIER_THRESH_C:
        return 'LAB-FALSIFIER-C'
    return 'LAB-FALSIFIER-D'


def _branch_conditions(detection_ratio):                              # (local)
    """4-branch decision tree (plan §W11-2 Step C). Conditions on
    s_obs/sigma_detect; numerical inequalities, not free-text."""
    half_dr = 0.5 * detection_ratio                                   # (local)
    branch_1_floor = max(BRANCH_DETECT_STRONG_FLOOR, half_dr)         # (local)
    return {
        'branch_1_condition': (
            f"s_obs/sigma_detect >= {branch_1_floor:.6g} "
            f"(== max({BRANCH_DETECT_STRONG_FLOOR:.0f}, "
            f"0.5*detection_ratio={half_dr:.6g})); "
            f"verdict_on_trigger = PASS-AT-LAB; "
            f"register_to = permanent_lab_falsifier_confirmation_register"
        ),
        'branch_2_condition': (
            f"{BRANCH_DETECT_MARG_LOW:.0f} <= s_obs/sigma_detect "
            f"< {BRANCH_DETECT_STRONG_FLOOR:.0f}; "
            f"verdict_on_trigger = REGISTERED-NO-CLOSE; "
            f"register_to = second_generation_experiment_queue"
        ),
        'branch_3_condition': (
            f"s_obs/sigma_detect < {BRANCH_NULL_FLOOR:.0f} "
            f"AND detection_ratio (={detection_ratio:.6g}) "
            f">= {BRANCH_NULL_STRONG_DR_FLOOR:.0f}; "
            f"verdict_on_trigger = FAIL-AT-LAB; "
            f"register_to = permanent_FAIL_corridor_register"
        ),
        'branch_4_condition': (
            f"s_obs/sigma_detect < {BRANCH_NULL_FLOOR:.0f} "
            f"AND detection_ratio (={detection_ratio:.6g}) "
            f"< {BRANCH_NULL_STRONG_DR_FLOOR:.0f}; "
            f"verdict_on_trigger = UNINFORMATIVE-NULL; "
            f"register_to = LAB-FALSIFIER-D_pending_detector_RD"
        ),
    }


tree_rows = []                                                        # (local)
tier_distribution = {                                                 # (local)
    'LAB-FALSIFIER-A': 0,
    'LAB-FALSIFIER-B': 0,
    'LAB-FALSIFIER-C': 0,
    'LAB-FALSIFIER-D': 0,
}
info_d_rows = []                                                      # (local) tier-D rows lacking R&D roadmap

for row in c5_rows:
    obs_id = row['obs_id']                                            # (local)
    platform = row['platform']                                        # (local)
    detection_ratio = float(row['detection_ratio'])                   # (local)
    SI_value = float(row['SI_value'])                                 # (local)
    SI_unit = row['SI_unit']                                          # (local)
    sigma_detect = float(row['sigma_detect'])                         # (local)
    lambda_dir = row['lambda']                                        # (local)
    lit_arxiv_id = row['lit_arxiv_id']                                # (local)
    lit_sha = row['lit_sha']                                          # (local)
    phenomenology_note = row['phenomenology_note']                    # (local)

    tier = _assign_tier(detection_ratio)                              # (local)
    branches = _branch_conditions(detection_ratio)                    # (local)
    experiment_family = EXPERIMENT_FAMILY.get(platform, 'UNPINNED')   # (local)
    provisional = (obs_id in provisional_set)                         # (local)

    tier_distribution[tier] += 1

    if tier == 'LAB-FALSIFIER-D':
        roadmap = DETECTOR_RD_ROADMAP_REGISTRY.get(obs_id)            # (local)
        if roadmap is None:
            info_d_rows.append(obs_id)

    out_row = {                                                       # (local)
        'obs_id': obs_id,
        'platform': platform,
        'lambda_direction': lambda_dir,
        'SI_value': SI_value,
        'SI_unit': SI_unit,
        'sigma_detect': sigma_detect,
        'detection_ratio': detection_ratio,
        'tier_assignment': tier,
        'branch_1_condition': branches['branch_1_condition'],
        'branch_2_condition': branches['branch_2_condition'],
        'branch_3_condition': branches['branch_3_condition'],
        'branch_4_condition': branches['branch_4_condition'],
        'experiment_family_pinned': experiment_family,
        'decision_horizon_year': DECISION_HORIZON_YEAR,
        'provisional': provisional,
        'lit_arxiv_id': lit_arxiv_id,
        'lit_sha': lit_sha,
        'phenomenology_note': phenomenology_note,
    }
    tree_rows.append(out_row)

    print(f"  {obs_id:>4s} ({platform:>5s}, {lambda_dir}): "
          f"detection_ratio={detection_ratio:>13.4f}  ->  {tier}  "
          f"(provisional={provisional})")

print()
print("[SEC 6] Tier distribution:")
for tier_name in ('LAB-FALSIFIER-A', 'LAB-FALSIFIER-B',
                  'LAB-FALSIFIER-C', 'LAB-FALSIFIER-D'):
    print(f"  {tier_name}: {tier_distribution[tier_name]}")

# ============================================================
# SECTION 7: PASS / FAIL / INFO determination (plan §9 thresholds)
# ============================================================
print("\n[SEC 7] PASS/FAIL/INFO determination per plan §9")

required_fields = (                                                   # (local)
    'tier_assignment',
    'branch_1_condition', 'branch_2_condition',
    'branch_3_condition', 'branch_4_condition',
    'experiment_family_pinned',
)
all_populated = True                                                  # (local)
missing_report = []                                                   # (local)
for r in tree_rows:
    for f in required_fields:
        v = r.get(f, None)                                            # (local)
        if v in (None, '', 'UNPINNED'):
            all_populated = False
            missing_report.append((r['obs_id'], f, v))

valid_tiers = {'LAB-FALSIFIER-A', 'LAB-FALSIFIER-B',
               'LAB-FALSIFIER-C', 'LAB-FALSIFIER-D'}
all_valid_tier = all(r['tier_assignment'] in valid_tiers              # (local)
                     for r in tree_rows)
nine_rows_present = (len(tree_rows) == 9)                             # (local)

if not (nine_rows_present and all_populated and all_valid_tier):
    verdict = 'FAIL'                                                  # (local)
    info_flag = False                                                 # (local)
elif info_d_rows:
    # PASS criteria met but LAB-FALSIFIER-D rows lack R&D roadmap -> INFO
    verdict = 'INFO'                                                  # (local)
    info_flag = True                                                  # (local)
else:
    verdict = 'PASS'                                                  # (local)
    info_flag = False                                                 # (local)

value = '9-rows-tiered-and-treed'                                     # (local)
print(f"  9 rows present                : {nine_rows_present}")
print(f"  All required fields populated : {all_populated}")
print(f"  All tiers in {{A,B,C,D}}       : {all_valid_tier}")
print(f"  Tier-D rows lacking R&D roadmap: {info_d_rows}")
print(f"  Verdict: {verdict}")

if missing_report:
    print(f"  Missing-field report: {missing_report}")

# ============================================================
# SECTION 8: Write CSV output (per plan §6 OUTPUT FILES)
# ============================================================
print("\n[SEC 8] Write CSV + JSON")

csv_columns = (                                                       # (local)
    'obs_id', 'platform', 'lambda_direction',
    'SI_value', 'SI_unit', 'sigma_detect', 'detection_ratio',
    'tier_assignment',
    'branch_1_condition', 'branch_2_condition',
    'branch_3_condition', 'branch_4_condition',
    'experiment_family_pinned',
    'decision_horizon_year',
    'provisional',
    'lit_arxiv_id', 'lit_sha',
    'phenomenology_note',
)
with open(OUT_CSV_PATH, 'w', encoding='utf-8', newline='') as fh:
    writer = csv.DictWriter(fh, fieldnames=csv_columns)               # (local)
    writer.writeheader()
    for r in tree_rows:
        writer.writerow({k: r[k] for k in csv_columns})
print(f"  CSV  : {OUT_CSV_PATH}")

json_payload = {                                                      # (local)
    'gate_id': GATE_ID,
    'verdict': verdict,
    'value': value,
    'scheme': SCHEME,
    'convention': CONVENTION,
    'L_max': L_MAX,
    'decision_horizon_year': DECISION_HORIZON_YEAR,
    'tier_ladder_definition': TIER_LADDER_DEFINITION,
    'tier_distribution': tier_distribution,
    'rows': tree_rows,
    'provisional_rows_inherited_from_C5': sorted(provisional_set),
    'info_d_rows_lacking_rd_roadmap': info_d_rows,
    'detector_rd_roadmap_registry': DETECTOR_RD_ROADMAP_REGISTRY,
    'experiment_family_pin_per_platform': EXPERIMENT_FAMILY,
    'input_shas': INPUT_SHAS,
    'C5_audit_sha256_cross_cite': EXPECTED_C5_AUDIT_SHA,
    'M_KK_GeV_cross_cite': float(M_KK),
    'evoi_ordering_substitution_chain_summary': (
        "EVOI(A) > EVOI(B) > EVOI(C) > EVOI(D) ~ 0; per plan §10. "
        "All 9 C5 detection_ratios >= 10 -> all 9 rows in tier A."
    ),
}
with open(OUT_JSON_PATH, 'w', encoding='utf-8') as fh:
    json.dump(json_payload, fh, indent=2, sort_keys=True)
print(f"  JSON : {OUT_JSON_PATH}")

# ============================================================
# SECTION 9: Dual-SHA computation (audit_sha256 + content_sha256)
# ============================================================
print("\n[SEC 9] Dual-SHA computation")

pin_map = {                                                           # (local)
    'GATE_ID': GATE_ID,
    'SCHEME': SCHEME,
    'CONVENTION': CONVENTION,
    'L_MAX': L_MAX,
    'TIER_THRESH_A': TIER_THRESH_A,
    'TIER_THRESH_B': TIER_THRESH_B,
    'TIER_THRESH_C': TIER_THRESH_C,
    'BRANCH_DETECT_STRONG_FLOOR': BRANCH_DETECT_STRONG_FLOOR,
    'BRANCH_DETECT_MARG_LOW': BRANCH_DETECT_MARG_LOW,
    'BRANCH_NULL_FLOOR': BRANCH_NULL_FLOOR,
    'BRANCH_NULL_STRONG_DR_FLOOR': BRANCH_NULL_STRONG_DR_FLOOR,
    'DECISION_HORIZON_YEAR': DECISION_HORIZON_YEAR,
    'EXPERIMENT_FAMILY': EXPERIMENT_FAMILY,
    'INPUT_SHAS': INPUT_SHAS,
    'C5_audit_sha256_cross_cite': EXPECTED_C5_AUDIT_SHA,
    'M_KK_GeV_cross_cite': float(M_KK),
    'tier_distribution': tier_distribution,
    'rows_count': len(tree_rows),
    'verdict': verdict,
    'value': value,
}
pinmap_json = json.dumps(pin_map, sort_keys=True,
                         separators=(',', ':')).encode('utf-8')        # (local)

script_path = os.path.abspath(__file__)                                # (local)
with open(script_path, 'rb') as _fh:
    script_bytes = _fh.read()                                          # (local)
with open(CANONICAL_PY, 'rb') as _fh:
    canonical_bytes = _fh.read()                                       # (local)

h_audit = hashlib.sha256()                                             # (local)
h_audit.update(script_bytes)
h_audit.update(canonical_bytes)
h_audit.update(pinmap_json)
audit_sha = h_audit.hexdigest()                                        # (local)
content_sha = hashlib.sha256(script_bytes).hexdigest()                 # (local)

print(f"  audit_sha256       = {audit_sha}")
print(f"  content_sha256     = {content_sha}")
print(f"  audit_sha256[:16]  = {audit_sha[:16]}")
print(f"  content_sha256[:16] = {content_sha[:16]}")

tuple_str = (f"(value={value!r}, scheme={SCHEME}, "                   # (local)
             f"convention={CONVENTION}, L_max={L_MAX})")
print(f"\n  4-tuple: {tuple_str}")

# ============================================================
# SECTION 10: Append verdict line + companion comment row
# ============================================================
print("\n[SEC 10] Append verdict line to canonical s86_gate_verdicts.txt")

verdict_line = (                                                      # (local)
    f"{GATE_ID}: {verdict} -- value={value!r} "
    f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
    f"audit_sha256={audit_sha} content_sha256={content_sha} "
    f"schema_version=R3\n"
)
companion_line = (                                                    # (local)
    f"# audit_sha256 companion row: {GATE_ID} "
    f"audit={audit_sha[:16]} content={content_sha[:16]}\n"
)
with open(VERDICT_PATH, 'a', encoding='utf-8') as fv:
    fv.write(verdict_line)
    fv.write(companion_line)
print(f"  Appended to {VERDICT_PATH}:")
print(f"    {verdict_line.strip()}")
print(f"    {companion_line.strip()}")

print("\n" + "=" * 76)
print(f"{GATE_ID} complete. Verdict: {verdict}")
print("=" * 76)

sys.exit(0)
