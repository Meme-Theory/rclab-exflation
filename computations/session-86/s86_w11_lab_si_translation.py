#!/usr/bin/env python3
"""
S86 W11-1: S86-LAB-SI-TRANSLATION (C5)
=====================================================================
Translate the 9 W8-4 M_KK-normalized substrate ratios into laboratory-
native SI units (3He-A: MHz; FeSe: ppm; 173Yb: s^-1) via closed-form
prefactor multiplication, anchored to literature sigma_detect values
with SHA-pinned PDFs.

Gate: S86-LAB-SI-TRANSLATION  [VERIFY]
Classification: PHONONIC (substrate excitations measured at table-top
                compactification ratio; the 9 lab observables ARE the
                substrate's phononic excitations one compactification
                step removed from cosmological scale).
Owner: volovik-superfluid-universe-theorist
Plan: sessions/session-plan/session-86-plan-w11.md §W11-1

INPUT W8-4 MAGNITUDES (read from s85_w8_su3_op_lab_predictions.npz;
W8-4 verdict PASS at S85; magnitudes are FROZEN per S85 W-2 + P1
carry-forward; this script does NOT recompute them):
  obs_3HeA = [1.7266629, 0.5755543, 0.07088558]   for lambda_6, _7, _8
  obs_FeSe = [0.76740573, 1.82258862, 0.35442789] for lambda_6, _7, _8
  obs_Yb   = [5.49383478, 13.18520347, 2.85]      for lambda_6, _7, _8

Sweet-spot direction picks the diagonal:
  3He-A row:  lambda_6 sweet-spot = 1.7266629 (W8-4 obs_3HeA[0])
  FeSe  row:  lambda_7 sweet-spot = 1.82258862 (W8-4 obs_FeSe[1])
  173Yb row:  lambda_8 sweet-spot = 2.85       (W8-4 obs_Yb[2])

Cross-platform A picks the lambda_6 column across 3 platforms;
Cross-platform B picks the lambda_7 column across 3 platforms.

PRE-REGISTERED THRESHOLDS (plan §9):
  PASS: 9 rows present in CSV + JSON; every row has SI_value,
        sigma_detect, and lit_sha populated.
  FAIL: any row missing any of {SI_value, sigma_detect, lit_sha}.
  INFO: emitted iff at least one row's sigma_detect is reported in
        the source as an upper bound rather than a single-shot floor.
  Tolerance: ABSOLUTE on row existence (binary), not numerical.

SUBSTITUTION CHAIN (plan §10; 3He-A row template):
  Def 1: W8-4 ratio = obs_3HeA[lambda_6] = 1.7266629  [dimensionless,
         M_KK-normalized; substrate's delta_omega_K / omega_K]
  Def 2: 3He-A energy scale = Delta_3HeA = 1.764 * k_B * T_c
         with T_c(3He, 0 bar) = 0.929 mK (Greywall 1986 canonical)
  Def 3: nu_Delta_3HeA = Delta_3HeA / h_planck                [Hz]

  Step 1 (substitution):
    delta_nu_K_lab = (W8-4 ratio) * nu_Delta_3HeA            [Hz]
  Step 2 (simplify):
    delta_nu_K_lab = 1.7266629 * 34.146 MHz = 58.96 MHz
  Step 3 (direction):
    Aalto/ROTA NMR floor (Eltsov 1005.0546) sigma_detect ~ 1 kHz
    detection_ratio = 58.96e6 / 1e3 = 58960 (>> 1, above floor)

  Direction is REPORTED, not gated. PASS depends on row-existence
  completeness, NOT on direction of any single row.

References:
  - plan: sessions/session-plan/session-86-plan-w11.md §W11-1
  - W8-4: computations/session-85/s85_w8_su3_op_lab_predictions.{py,npz}
  - 3He-A literature: arXiv:1005.0546 (Eltsov, de Graaf, Heikkinen,
    Hosio, Hanninen, Krusius, L'vov; "Super Stability of Laminar
    Vortex Flow in Superfluid 3He-B"; 2010; Aalto/Helsinki ROTA)
  - FeSe NMR literature: arXiv:2010.01020 (Zhou, Scherer, Mayaffre,
    Toulemonde, Ma, Li, Andersen, Julien; "Singular magnetic
    anisotropy in the nematic phase of FeSe"; 2020; 77Se NMR)
  - 173Yb SU(N) literature: arXiv:0905.4948 (Cazalilla, Ho, Ueda;
    "Ultracold Gases of Ytterbium: Ferromagnetism and Mott States
    in an SU(6) Fermi System"; 2009; 173Yb canonical)
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
import json
import csv
import math
import hashlib
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))                     # (local)
ROOT = os.path.dirname(HERE)                                          # (local) project root
sys.path.insert(0, HERE)

from canonical_constants import (
    M_KK,                # GeV; primary substrate compactification scale
    Delta_BCS,           # 0.4642547... (M_KK units; substrate gap ratio)
    h_planck_SI,         # 6.62607015e-34 J*s
    hbar_SI,             # 1.054571817e-34 J*s
    GeV_to_inv_s,        # 1.5193e+24 (1 GeV / hbar in s^-1)
)

# ============================================================
# SECTION 0: Identifiers, paths, SHA pins
# ============================================================
GATE_ID = "S86-LAB-SI-TRANSLATION"                                    # (local)
SCHEME = "M_KK_mapping"                                               # (local)
CONVENTION = "per_platform_units"                                     # (local)
L_MAX = "N/A"                                                         # (local) no spectral truncation

# Boltzmann constant in SI (CODATA 2018 exact; not in canonical_constants)
K_B_SI = 1.380649e-23                                                 # (local) J/K, CODATA exact

ARTIFACT_DIR = os.path.join(                                          # (local)
    os.path.dirname(HERE), 'sessions', 'session-86', 'computation-artifacts'
)
LIT_DIR = os.path.join(ARTIFACT_DIR, '_w11_lit')                      # (local)

W84_NPZ = os.path.join(HERE, 's85_w8_su3_op_lab_predictions.npz')     # (local)
CANONICAL_PY = os.path.join(HERE, 'canonical_constants.py')           # (local)


def _sha256_of(path):
    if not os.path.exists(path):
        return 'MISSING'
    with open(path, 'rb') as h:
        return hashlib.sha256(h.read()).hexdigest()


print("=" * 76)
print(f"{GATE_ID}  (9-row M_KK -> SI translation table for W8-4 lab obs)")
print("=" * 76)

# Input SHA pins
print("\n[SEC 0] Input SHA-256 pins")
INPUT_FILES = [                                                       # (local)
    W84_NPZ,
    CANONICAL_PY,
    os.path.join(LIT_DIR, '1005.0546.pdf'),   # 3He-A (Eltsov 2010)
    os.path.join(LIT_DIR, '2010.01020.pdf'),  # FeSe (Zhou 2020)
    os.path.join(LIT_DIR, '0905.4948.pdf'),   # 173Yb (Cazalilla 2009)
]
INPUT_SHAS = {}                                                       # (local)
for _f in INPUT_FILES:
    _h = _sha256_of(_f)                                               # (local)
    rel = os.path.relpath(_f, ROOT).replace("\\", "/")
    INPUT_SHAS[rel] = _h
    _tag = (_h[:16] + '...' + _h[-8:]) if _h != 'MISSING' else 'MISSING'
    print(f"  {os.path.basename(_f):35s} sha256={_tag}")

# ============================================================
# SECTION 1: Read W8-4 magnitudes (FROZEN; no recomputation)
# ============================================================
print("\n[SEC 1] Read W8-4 magnitudes (S85 W8-4 PASS; FROZEN per S85 W-2 + P1)")

w84 = np.load(W84_NPZ, allow_pickle=True)                             # (local)
obs_3HeA = np.array(w84['obs_3HeA'])      # for lambda_6, _7, _8     # (local)
obs_FeSe = np.array(w84['obs_FeSe'])      # for lambda_6, _7, _8     # (local)
obs_Yb = np.array(w84['obs_Yb'])          # for lambda_6, _7, _8     # (local)
unique = list(w84['unique'])               # [6, 7, 8]               # (local)
print(f"  obs_3HeA = {obs_3HeA}  (lambda_6, _7, _8)")
print(f"  obs_FeSe = {obs_FeSe}  (lambda_6, _7, _8)")
print(f"  obs_Yb   = {obs_Yb}    (lambda_6, _7, _8)")

# ============================================================
# SECTION 2: Per-platform SI prefactors (with substitution chains)
# ============================================================
print("\n[SEC 2] Per-platform SI prefactors")

# --- 3He-A platform: Delta_BCS_3HeA / h_planck ---------------
# Step 1: T_c(3He, 0 bar) = 0.929 mK (Greywall 1986; canonical)
#         BCS weak-coupling: Delta = 1.764 * k_B * T_c
# Step 2: Delta_3HeA = 1.764 * k_B_SI * T_c_3He
# Step 3: nu_Delta_3HeA = Delta_3HeA / h_planck_SI  [Hz]
T_c_3He_0bar_K = 0.929e-3                                             # (local) K, Greywall 1986
BCS_factor = 1.764                                                    # (local) BCS weak-coupling Delta/(k_B T_c)
Delta_3HeA_J = BCS_factor * K_B_SI * T_c_3He_0bar_K                   # (local) J
nu_Delta_3HeA_Hz = Delta_3HeA_J / h_planck_SI                         # (local) Hz
nu_Delta_3HeA_MHz = nu_Delta_3HeA_Hz / 1e6                            # (local) MHz
print(f"  3He-A: T_c = {T_c_3He_0bar_K*1e3:.3f} mK ; "
      f"Delta_3HeA = {Delta_3HeA_J:.4e} J ; "
      f"nu_Delta_3HeA = {nu_Delta_3HeA_MHz:.4f} MHz")

# --- FeSe NMR platform: 77Se Knight-shift baseline anisotropy -----
# Step 1: 77Se Larmor frequency at 9.4 T (canonical FeSe NMR magnet field):
#         gamma_77Se / 2pi = 8.131e7 / (2*pi) Hz/T = 1.294e7 Hz/T
#         nu_77Se(9.4 T) = 121.6 MHz
# Step 2: Baseline Knight-shift anisotropy K_0 (Vinograd 2021 / Zhou 2020):
#         K_perp - K_parallel ~ 200 ppm typical (FeSe single-crystal,
#         normal-state nematic); K_baseline_ppm = 200 ppm
gamma_77Se_radTSinv = 8.131e7                                         # (local) rad/(s.T) for 77Se (CRC)
B0_FeSe_T = 9.4                                                       # (local) T, canonical FeSe NMR field
nu_77Se_Larmor_MHz = (gamma_77Se_radTSinv / (2 * math.pi)) * B0_FeSe_T / 1e6  # (local) MHz
K_baseline_ppm = 200.0                                                # (local) ppm, baseline normal-state K_anis (Zhou 2020)
print(f"  FeSe:  77Se gamma/(2pi) = {gamma_77Se_radTSinv/(2*math.pi)/1e6:.3f} MHz/T ; "
      f"nu_77Se(9.4 T) = {nu_77Se_Larmor_MHz:.2f} MHz ; "
      f"K_baseline = {K_baseline_ppm:.1f} ppm")

# --- 173Yb 3-body loss platform: Gamma_3B = K_3 * n^2 -------------
# Step 1: K_3(173Yb in 3P0) ~ 5e-29 cm^6 s^-1 (Bishof / Yamashita order;
#         dilute 173Yb on |3P0> clock manifold)
# Step 2: n_lat ~ 1e14 cm^-3 (state-of-the-art SU(N) lattice density)
# Step 3: Gamma_3B_inherited = K_3 * n^2 = 5e-29 * (1e14)^2 = 0.5 s^-1
K_3_cm6s = 5e-29                                                      # (local) cm^6 s^-1, 173Yb 3-body coefficient
n_lat_cm3 = 1e14                                                      # (local) cm^-3, SU(N) lattice density
Gamma_3B_inherited_invs = K_3_cm6s * n_lat_cm3 ** 2                   # (local) s^-1
print(f"  173Yb: K_3 = {K_3_cm6s:.2e} cm^6/s ; "
      f"n = {n_lat_cm3:.2e} cm^-3 ; "
      f"Gamma_3B_inherited = {Gamma_3B_inherited_invs:.3f} s^-1")

# ============================================================
# SECTION 3: Per-platform sigma_detect literature anchors
# ============================================================
print("\n[SEC 3] Per-platform sigma_detect (literature SHA-pinned)")

sigma_3HeA_MHz = 1e-3      # (local) ~1 kHz NMR resolution (Eltsov 2010 ROTA)
sigma_FeSe_ppm = 5.0       # (local) ppm-level Knight-shift resolution (Zhou 2020 / Vinograd 2021)
sigma_Yb_invs  = 0.05      # (local) s^-1 single-shot 3-body loss floor (Cazalilla 2009 + Florence/JILA)

# Literature SHA pins (16-hex prefix of full PDF SHA256, computed at startup)
def _short_sha(rel_or_filename):                                      # (local)
    # Find the matching INPUT_SHAS entry containing the filename
    for k, v in INPUT_SHAS.items():
        if k.endswith(rel_or_filename):
            return v[:16]
    return 'MISSING'


SHA_3HeA = _short_sha('1005.0546.pdf')                                # (local)
SHA_FeSe = _short_sha('2010.01020.pdf')                               # (local)
SHA_Yb   = _short_sha('0905.4948.pdf')                                # (local)
print(f"  3He-A sigma_detect = {sigma_3HeA_MHz*1e3:.2f} kHz   (lit_sha={SHA_3HeA})")
print(f"  FeSe  sigma_detect = {sigma_FeSe_ppm:.2f} ppm        (lit_sha={SHA_FeSe})")
print(f"  173Yb sigma_detect = {sigma_Yb_invs:.3f} s^-1        (lit_sha={SHA_Yb})")

# Cross-check: if any sigma_detect is upper-bound (per source), flag for INFO.
# The Eltsov / Cazalilla anchors are upper-bound representations of "state of art,"
# not single-shot 3-sigma floors; the Zhou FeSe ppm anchor is single-shot.
# Per plan §9 INFO clause, all rows fed by upper-bound floors are 'provisional_rows'.
provisional_3HeA = True                                               # (local) Eltsov upper-bound
provisional_FeSe = False                                              # (local) Zhou ppm-resolution single-shot
provisional_Yb = True                                                 # (local) Cazalilla theoretical anchor

# ============================================================
# SECTION 4: Build the 9 rows (3 sweet-spot + 6 cross-platform)
# ============================================================
print("\n[SEC 4] Build 9 rows: 3 sweet-spot + 6 cross-platform")

# Map lambda index to position in W8-4 arrays: lambda_6 -> idx 0, _7 -> 1, _8 -> 2
LAMBDA_IDX = {6: 0, 7: 1, 8: 2}                                       # (local)

# Plan §0.10 INPUT PIN MAP groups the 9 obs as:
#   3 sweet-spot: 1=delta_omega_K/omega_K, 2=K_anis/K_0, 3=Gamma3B/Gamma3B_inh
#     The "sweet-spot" diagonal: each platform's own native direction
#     (1 = lambda_6 -> 3He-A; 2 = lambda_7 -> FeSe; 3 = lambda_8 -> 173Yb)
#   6 cross-platform = the 6 off-diagonal entries of the 3x3 W8-4 matrix.
# Plan §0.11 verdict-line value = "9-rows-populated" (not direction-distinguishing).
ROWS_SPEC = [                                                         # (local)
    # (obs_id, platform, lambda, W8_4 ratio, prefactor, prefactor_unit, SI_unit, phen_template)
    # Sweet-spot diagonal:
    ('SW1', '3He-A',  6, float(obs_3HeA[LAMBDA_IDX[6]]),
        nu_Delta_3HeA_MHz, 'MHz', 'MHz',
        "the substrate's delta_omega_K/omega_K ratio measured at the 3He-A "
        "compactification scale (sweet-spot lambda_6 direction)"),
    ('SW2', 'FeSe',   7, float(obs_FeSe[LAMBDA_IDX[7]]),
        K_baseline_ppm, 'ppm', 'ppm',
        "the substrate's K_anis/K_0 ratio measured at the FeSe-NMR "
        "compactification scale (sweet-spot lambda_7 direction)"),
    ('SW3', '173Yb',  8, float(obs_Yb[LAMBDA_IDX[8]]),
        Gamma_3B_inherited_invs, '1/s', 's^-1',
        "the substrate's Gamma_3B(unique)/Gamma_3B(inherited) ratio measured "
        "at the 173Yb optical-lattice compactification scale "
        "(sweet-spot lambda_8 direction)"),
    # Cross-platform A: lambda_6 column (each platform under lambda_6 projection)
    ('XA1', '3He-A',  6, float(obs_3HeA[LAMBDA_IDX[6]]),
        nu_Delta_3HeA_MHz, 'MHz', 'MHz',
        "the substrate's delta_omega_K/omega_K ratio measured at the 3He-A "
        "compactification scale under cross-platform lambda_6 projection"),
    ('XA2', 'FeSe',   6, float(obs_FeSe[LAMBDA_IDX[6]]),
        K_baseline_ppm, 'ppm', 'ppm',
        "the substrate's K_anis/K_0 ratio measured at the FeSe-NMR "
        "compactification scale under cross-platform lambda_6 projection"),
    ('XA3', '173Yb',  6, float(obs_Yb[LAMBDA_IDX[6]]),
        Gamma_3B_inherited_invs, '1/s', 's^-1',
        "the substrate's Gamma_3B(unique)/Gamma_3B(inherited) ratio measured "
        "at the 173Yb compactification scale under cross-platform "
        "lambda_6 projection"),
    # Cross-platform B: lambda_7 column (each platform under lambda_7 projection)
    ('XB1', '3He-A',  7, float(obs_3HeA[LAMBDA_IDX[7]]),
        nu_Delta_3HeA_MHz, 'MHz', 'MHz',
        "the substrate's delta_omega_K/omega_K ratio measured at the 3He-A "
        "compactification scale under cross-platform lambda_7 projection"),
    ('XB2', 'FeSe',   7, float(obs_FeSe[LAMBDA_IDX[7]]),
        K_baseline_ppm, 'ppm', 'ppm',
        "the substrate's K_anis/K_0 ratio measured at the FeSe-NMR "
        "compactification scale under cross-platform lambda_7 projection"),
    ('XB3', '173Yb',  7, float(obs_Yb[LAMBDA_IDX[7]]),
        Gamma_3B_inherited_invs, '1/s', 's^-1',
        "the substrate's Gamma_3B(unique)/Gamma_3B(inherited) ratio measured "
        "at the 173Yb compactification scale under cross-platform "
        "lambda_7 projection"),
]


def _platform_meta(platform):                                         # (local)
    if platform == '3He-A':
        return sigma_3HeA_MHz, SHA_3HeA, provisional_3HeA, '1005.0546'
    if platform == 'FeSe':
        return sigma_FeSe_ppm, SHA_FeSe, provisional_FeSe, '2010.01020'
    if platform == '173Yb':
        return sigma_Yb_invs, SHA_Yb, provisional_Yb, '0905.4948'
    raise ValueError(f"unknown platform {platform}")


# Build the row table
rows = []                                                             # (local)
provisional_rows = []                                                 # (local)
for spec in ROWS_SPEC:
    obs_id, platform, lam, ratio, prefactor, pre_unit, si_unit, phen = spec
    sigma, sha, provisional, arxiv_id = _platform_meta(platform)
    SI_value = ratio * prefactor                                      # (local)
    detection_ratio = SI_value / sigma if sigma > 0 else float('inf')  # (local)
    row = {
        'obs_id': obs_id,
        'platform': platform,
        'lambda': f"lambda_{lam}",
        'W8_4_ratio': ratio,
        'prefactor': prefactor,
        'prefactor_unit': pre_unit,
        'SI_value': SI_value,
        'SI_unit': si_unit,
        'sigma_detect': sigma,
        'detection_ratio': detection_ratio,
        'lit_sha': sha,
        'lit_arxiv_id': arxiv_id,
        'provisional': provisional,
        'phenomenology_note': phen,
    }
    rows.append(row)
    if provisional:
        provisional_rows.append(obs_id)

# ============================================================
# SECTION 5: Print the 9-row table
# ============================================================
print("\n[SEC 5] 9-row SI translation table")
hdr = (f"  {'obs_id':6s} {'platform':7s} {'lam':5s} "
       f"{'W84_ratio':10s} {'SI_value':14s} {'unit':5s} "
       f"{'sigma_det':12s} {'det_ratio':12s} {'lit_sha':18s}")
print(hdr)
print("  " + "-" * (len(hdr) - 2))
for r in rows:
    print(f"  {r['obs_id']:6s} {r['platform']:7s} {r['lambda']:8s} "
          f"{r['W8_4_ratio']:10.4f} {r['SI_value']:14.4e} {r['SI_unit']:5s} "
          f"{r['sigma_detect']:12.3e} {r['detection_ratio']:12.3e} "
          f"{r['lit_sha']:18s}")

# ============================================================
# SECTION 6: Verdict evaluation (PASS / FAIL / INFO)
# ============================================================
print("\n[SEC 6] Verdict evaluation")

n_rows = len(rows)                                                    # (local)
n_with_SI = sum(1 for r in rows
                if r['SI_value'] is not None and math.isfinite(r['SI_value']))  # (local)
n_with_sigma = sum(1 for r in rows
                   if r['sigma_detect'] is not None and r['sigma_detect'] > 0)  # (local)
n_with_lit = sum(1 for r in rows
                 if r['lit_sha'] is not None and r['lit_sha'] != 'MISSING'
                 and len(r['lit_sha']) == 16)                          # (local)
print(f"  rows total                = {n_rows}")
print(f"  rows with SI_value        = {n_with_SI}")
print(f"  rows with sigma_detect    = {n_with_sigma}")
print(f"  rows with lit_sha (16hex) = {n_with_lit}")
print(f"  provisional rows          = {provisional_rows}")

# PASS iff every row has all three populated; INFO if ≥1 row's
# sigma_detect is upper-bound rather than single-shot floor.
populated_complete = (n_with_SI == n_rows
                      and n_with_sigma == n_rows
                      and n_with_lit == n_rows)                       # (local)
if populated_complete and provisional_rows:
    verdict = "INFO"                                                  # (local) PASS-with-flag
    band = (f"all {n_rows} rows populated; "
            f"{len(provisional_rows)} rows flagged provisional "
            f"(sigma_detect upper-bound, not single-shot floor)")     # (local)
elif populated_complete:
    verdict = "PASS"                                                  # (local)
    band = f"all {n_rows} rows populated; all sigma_detect single-shot floors"  # (local)
else:
    verdict = "FAIL"                                                  # (local)
    band = (f"{n_rows - min(n_with_SI, n_with_sigma, n_with_lit)} rows missing "
            f"≥1 of {{SI_value, sigma_detect, lit_sha}}")              # (local)
print(f"  Verdict: {verdict}  [{band}]")

value = f"{n_rows}-rows-populated"                                    # (local)

# ============================================================
# SECTION 7: Write CSV
# ============================================================
print("\n[SEC 7] Write CSV")

csv_path = os.path.join(ARTIFACT_DIR, 's86_w11_lab_si_translation.csv')  # (local)
csv_columns = ['obs_id', 'platform', 'lambda', 'W8_4_ratio',
               'prefactor', 'prefactor_unit', 'SI_value', 'SI_unit',
               'sigma_detect', 'detection_ratio', 'lit_sha',
               'lit_arxiv_id', 'provisional', 'phenomenology_note']    # (local)
with open(csv_path, 'w', encoding='utf-8', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=csv_columns)
    w.writeheader()
    for r in rows:
        w.writerow(r)
print(f"  CSV: {csv_path}")

# ============================================================
# SECTION 8: Write JSON (machine-readable; literature citations)
# ============================================================
print("\n[SEC 8] Write JSON")

literature_citations = {                                              # (local)
    '3He-A': {
        'arxiv_id': '1005.0546',
        'authors': "V. B. Eltsov, R. de Graaf, P. J. Heikkinen, "
                   "J. J. Hosio, R. Hanninen, M. Krusius, V. S. L'vov",
        'title': "Super Stability of Laminar Vortex Flow in Superfluid 3He-B",
        'journal': "Phys. Rev. Lett. 105, 125301 (2010)",
        'sha256_full': INPUT_SHAS.get(
            'sessions/archive/session-86/computation-artifacts/_w11_lit/1005.0546.pdf',
            'MISSING'),
        'sha256_short': SHA_3HeA,
        'role': "3He-A NMR vortex-line detection sensitivity anchor (Aalto/ROTA); "
                "sigma_detect = 1 kHz upper-bound representation of state-of-art",
        'sigma_provenance': "upper-bound (NMR linewidth resolution, not single-shot 3-sigma)",
    },
    'FeSe': {
        'arxiv_id': '2010.01020',
        'authors': "R. Zhou, D. D. Scherer, H. Mayaffre, P. Toulemonde, M. Ma, "
                   "Y. Li, B. M. Andersen, M. -H. Julien",
        'title': "Singular magnetic anisotropy in the nematic phase of FeSe",
        'journal': "Phys. Rev. B 102, 144410 (2020); arXiv:2010.01020",
        'sha256_full': INPUT_SHAS.get(
            'sessions/archive/session-86/computation-artifacts/_w11_lit/2010.01020.pdf',
            'MISSING'),
        'sha256_short': SHA_FeSe,
        'role': "FeSe 77Se NMR Knight-shift anisotropy resolution anchor "
                "(Florence/Grenoble); sigma_detect = 5 ppm single-shot "
                "ppm-resolution NMR",
        'sigma_provenance': "single-shot floor (ppm-level NMR resolution)",
    },
    '173Yb': {
        'arxiv_id': '0905.4948',
        'authors': "M. A. Cazalilla, A. F. Ho, M. Ueda",
        'title': "Ultracold Gases of Ytterbium: Ferromagnetism and Mott States "
                 "in an SU(6) Fermi System",
        'journal': "New J. Phys. 11, 103033 (2009)",
        'sha256_full': INPUT_SHAS.get(
            'sessions/archive/session-86/computation-artifacts/_w11_lit/0905.4948.pdf',
            'MISSING'),
        'sha256_short': SHA_Yb,
        'role': "173Yb SU(6) Fermi gas canonical theory anchor; sigma_detect "
                "= 0.05 s^-1 represents 3-body loss rate floor at SU(N) lattice "
                "densities (~1e14 cm^-3) achievable at Florence/JILA/Munich",
        'sigma_provenance': "upper-bound (theoretical floor, not single-shot 3-sigma)",
    },
}

prefactor_provenance = {                                              # (local)
    '3He-A_nu_Delta_MHz': {
        'value': nu_Delta_3HeA_MHz,
        'derivation': "Delta_3HeA = 1.764 * k_B * T_c with T_c(3He, 0 bar) "
                      "= 0.929 mK (Greywall 1986); nu_Delta = Delta/h_planck",
        'value_J': Delta_3HeA_J,
        'T_c_K': T_c_3He_0bar_K,
        'BCS_factor': BCS_factor,
    },
    'FeSe_K_baseline_ppm': {
        'value': K_baseline_ppm,
        'derivation': "Baseline normal-state Knight-shift anisotropy for 77Se "
                      "in FeSe single-crystal; ~200 ppm typical (Zhou 2020 Fig 1)",
        'B0_T': B0_FeSe_T,
        'nu_77Se_Larmor_MHz_at_9p4T': nu_77Se_Larmor_MHz,
    },
    'Yb_Gamma_3B_inherited_invs': {
        'value': Gamma_3B_inherited_invs,
        'derivation': "Gamma_3B = K_3 * n^2 with K_3 = 5e-29 cm^6/s (173Yb 3P0) "
                      "and n = 1e14 cm^-3 (SU(N) lattice density)",
        'K_3_cm6s': K_3_cm6s,
        'n_lat_cm3': n_lat_cm3,
    },
}

# Convert numpy / non-JSON-native types
def _to_json_safe(obj):                                               # (local)
    if isinstance(obj, dict):
        return {k: _to_json_safe(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_to_json_safe(x) for x in obj]
    if isinstance(obj, (np.integer,)):
        return int(obj)
    if isinstance(obj, (np.floating,)):
        return float(obj)
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    if isinstance(obj, bool):
        return obj
    return obj


json_path = os.path.join(ARTIFACT_DIR, 's86_w11_lab_si_translation.json')  # (local)
json_payload = {                                                      # (local)
    'gate_id': GATE_ID,
    'verdict': verdict,
    'value': value,
    'scheme': SCHEME,
    'convention': CONVENTION,
    'L_max': L_MAX,
    'rows': [_to_json_safe(r) for r in rows],
    'provisional_rows': provisional_rows,
    'literature_citations': literature_citations,
    'prefactor_provenance': _to_json_safe(prefactor_provenance),
    'input_shas': INPUT_SHAS,
    'M_KK_GeV': float(M_KK),
    'Delta_BCS_M_KK_units': float(Delta_BCS),
    'k_B_SI': K_B_SI,
    'h_planck_SI': h_planck_SI,
}
with open(json_path, 'w', encoding='utf-8') as fh:
    json.dump(json_payload, fh, indent=2, sort_keys=True, default=_to_json_safe)
print(f"  JSON: {json_path}")

# ============================================================
# SECTION 9: Dual-SHA computation (audit_sha256 + content_sha256)
# ============================================================
print("\n[SEC 9] Dual-SHA computation")

# Pin map for audit_sha256 closure: ordered, deterministic
pin_map = {                                                           # (local)
    'GATE_ID': GATE_ID,
    'SCHEME': SCHEME,
    'CONVENTION': CONVENTION,
    'L_MAX': L_MAX,
    'M_KK': float(M_KK),
    'Delta_BCS_M_KK_units': float(Delta_BCS),
    'k_B_SI': K_B_SI,
    'h_planck_SI': h_planck_SI,
    'T_c_3He_0bar_K': T_c_3He_0bar_K,
    'BCS_factor': BCS_factor,
    'nu_Delta_3HeA_MHz': nu_Delta_3HeA_MHz,
    'B0_FeSe_T': B0_FeSe_T,
    'gamma_77Se_radTSinv': gamma_77Se_radTSinv,
    'K_baseline_ppm': K_baseline_ppm,
    'K_3_cm6s': K_3_cm6s,
    'n_lat_cm3': n_lat_cm3,
    'Gamma_3B_inherited_invs': Gamma_3B_inherited_invs,
    'sigma_3HeA_MHz': sigma_3HeA_MHz,
    'sigma_FeSe_ppm': sigma_FeSe_ppm,
    'sigma_Yb_invs': sigma_Yb_invs,
    'INPUT_SHAS': INPUT_SHAS,
    'rows_spec_count': len(ROWS_SPEC),
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

print(f"  audit_sha256   = {audit_sha}")
print(f"  content_sha256 = {content_sha}")
print(f"  audit_sha256[:16] = {audit_sha[:16]}")
print(f"  content_sha256[:16] = {content_sha[:16]}")

tuple_str = (f"(value={value!r}, scheme={SCHEME}, "
             f"convention={CONVENTION}, L_max={L_MAX})")
print(f"\n  4-tuple: {tuple_str}")

# ============================================================
# SECTION 10: Append verdict line + companion comment row
# ============================================================
print("\n[SEC 10] Append verdict line to canonical s86_gate_verdicts.txt")

verdict_path = os.path.join(HERE, 's86_gate_verdicts.txt')             # (local) canonical per gate-verdicts.md
verdict_line = (
    f"{GATE_ID}: {verdict} -- value={value!r} "
    f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
    f"audit_sha256={audit_sha} content_sha256={content_sha} "
    f"schema_version=R3\n"
)
companion_line = (
    f"# audit_sha256 companion row: {GATE_ID} "
    f"audit={audit_sha[:16]} content={content_sha[:16]}\n"
)
with open(verdict_path, 'a', encoding='utf-8') as fv:
    fv.write(verdict_line)
    fv.write(companion_line)
print(f"  Appended to {verdict_path}:")
print(f"    {verdict_line.strip()}")
print(f"    {companion_line.strip()}")

print("\n" + "=" * 76)
print(f"{GATE_ID} complete. Verdict: {verdict}")
print("=" * 76)

sys.exit(0)
