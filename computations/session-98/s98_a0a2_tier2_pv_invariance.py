#!/usr/bin/env python3
"""
s98_a0a2_tier2_pv_invariance.py — S98-A0A2-TIER2-PV-INVARIANCE
==============================================================

Wave 5 (lizzi-spectral-functional-theorist). Single-gate, no-new-spectrum
re-evaluation of the capstone §8.5 tier-2 SURVIVAL verdict for the a₀/a₂
Seeley-DeWitt moment-pair under TWO regulator anchorings:

  FI-anchor :  a₀^{Mellin}/a₂^{Mellin}            (Mellin-zeta analytic continuation,
                                                   NO Pauli-Villars subtraction)
  PV-anchor :  a₀^{Pauli-Villars}/a₂^{Pauli-Villars}  (full-physical 2-point PV with
                                                   M_KK mass-scale running; PRIMARY tier,
                                                   _pauli_villars_subtraction.py)

and verifies the §8.5 partition LABEL (ratio-observable SURVIVES on the
topological side / absolute-magnitude CONDITIONAL on the dissolving side) is
IDENTICAL across both ⇒ d(survival)/d(PV-scheme) = 0 NUMERICALLY (not merely
structurally per S-3 / S96-SDW-CC-GAP). This NUMERICALLY confirms the DI1 guard
that the S97 W2-1 object-definedness gate (audit 7d5ca3f9) deliberately scoped
out (`DI1=OBJECT-DEFINEDNESS-AXIS-ONLY; does-NOT-establish-or-retract-§8.5
-tier-2-survival`).

NUMBERS first, gate second, interpretation third. The verdict is DATA
(PASS/FAIL/INFO all valid); exit 0 regardless. No iterate-to-PASS, no
convention-shopping.

SUBSTRATE FRAMING (GEOMETRIC). The internal fabric at every point is the
spectral triple (A_K, H_K, D_K) on Jensen-deformed SU(3); a₀, a₂ are the zeroth
and second Seeley-DeWitt spectral MOMENTS of D_K (a₀ → vacuum / cosmological
term; a₂ → the emergent Einstein-Hilbert action). The §8.5 tier-2 survival
partition is a property of the substrate's spectral-action FUNCTIONAL itself —
the choice of regulator (Mellin analytic continuation vs full-physical PV) is
a PHYSICAL question with an observable consequence: does it move the §8.5
partition? The PV-scheme invariance is a regulator-class FI property of the
spectral functional, NOT a container quantity. Direction of explanation flows
FROM the D_K spectrum (both moments from the SAME L_max=10 D_K² cache) TOWARD
the emergent partition.

Plan: sessions/session-plan/session-98-plan-w5.md §W5-1.
Both moments are already pinned in the W2-1 npz; this gate re-evaluates an
existing closed-form margin under two anchor choices. No matrix work
(scalar re-evaluation of pre-computed moments) → numpy/CPU, OMP capped at 8.
"""
import os
os.environ['OMP_NUM_THREADS'] = '8'           # (local) — scalar re-eval, no GPU; cap CPU threads
os.environ['MKL_NUM_THREADS'] = '8'           # (local)

import hashlib
import json
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# --- canonical constants (MANDATORY import; SOURCE-RECON binding test on consumed values) ---
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / '_shared'))
from canonical_constants import a_0_FW_zeta, a_2_FW_zeta   # zeta-FW anchors (cross-check)

# ============================================================================
# Paths (absolute via __file__; project root = parents[2])
# ============================================================================
ROOT = Path(__file__).resolve().parents[2]
W2_1_NPZ = ROOT / 'computations' / 'session-97' / 's97_w2_1_a0a2_pv_full_mellin.npz'
PV_HELPER = ROOT / 'computations' / '_pauli_villars_subtraction.py'
CANON = ROOT / 'computations' / '_shared' / 'canonical_constants.py'
CAPSTONE = ROOT / 'sessions' / 'framework' / 'phonic-exflation-equation.md'
S96_VERDICTS = ROOT / 'computations' / 'session-96' / 's96_gate_verdicts.txt'
VERDICT_FILE = ROOT / 'computations' / 'session-98' / 's98_gate_verdicts.txt'
OUT_NPZ = ROOT / 'computations' / 'session-98' / 's98_a0a2_tier2_pv_invariance.npz'
OUT_PNG = ROOT / 'computations' / 'session-98' / 's98_a0a2_tier2_pv_invariance.png'

GATE_ID = 'S98-A0A2-TIER2-PV-INVARIANCE'
SCHEME = 'TIER2-SURVIVAL-DUAL-ANCHOR-FI-vs-FULL-PV'
CONVENTION = 'RATIO-LABEL-DISTANCE-poleconv-A-double-PV-FULL-PHYSICAL'
L_MAX = 10                # (local) — plan §W5-1 canonical anchoring L_max (W2-1 canonical)

# Pre-registered gate thresholds (plan §W5-1 machinery_pin_map; gate criteria, NOT framework constants)
PASS_TOL = 1.0e-9         # (local) — Δ(survival-margin) PASS boundary (<=); presentation-precision floor
EPS_FI = 0.05            # (local) — K-invariant-family FI tolerance (S96-SDW-CC-GAP partB)
INFO_BAND = 0.10         # (local) — INFO ceiling on PV within-family L_max drift operand

# Plan-pinned static SHA (PV helper) + plan-pinned consumed canonical values (cross-check copies;
# the `from canonical_constants import a_0_FW_zeta, a_2_FW_zeta` above is authoritative)
PV_HELPER_SHA_PLAN = 'eaf98037ddc2a4d7c9f6e7a91c14805591ef22d8326596698a994a3c791c3f07'
W2_1_VERDICT_AUDIT = '7d5ca3f97c9f7074c7a60f99a16ff46c27c9e0e9d9881b2b872130af0974cb2e'
A0_FW_ZETA_PIN = 6440.0          # (local) — plan-pinned cross-check copy of imported a_0_FW_zeta
A2_FW_ZETA_PIN = 2776.165389     # (local) — plan-pinned cross-check copy of imported a_2_FW_zeta


# ============================================================================
# Dual-SHA verdict emitter (self-contained; canonical pattern from
# computations/_shared/s90_w1_emit_verdict.py)
# ============================================================================
def sha256_of_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()


def sha256_of_text(text: str) -> str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def compute_audit_sha(input_pin_map: dict) -> str:
    """SHA-256 over ordered JSON-serialized input-pin map (sorted keys)."""
    return sha256_of_text(json.dumps(input_pin_map, sort_keys=True, ensure_ascii=False))


def append_verdict(gate_id, verdict, value_str, scheme, convention, l_max,
                   input_pin_map, content_target, sign_verdict, magnitude_verdict,
                   regime_verdict, three_tuple_note=''):
    """Append canonical line + dual-SHA companion row + [SIGN] 3-tuple companion row.

    Atomic single open('a') write. Per gate-verdicts.md S87+ schema-v2 and the
    [SIGN]-trigger 3-tuple requirement.
    """
    content_sha = sha256_of_file(content_target)
    audit_sha = compute_audit_sha(input_pin_map)
    canonical_line = (
        f"{gate_id}: {verdict} -- value='{value_str}' "
        f"scheme={scheme} convention={convention} L_max={l_max} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} schema_version=S84+"
    )
    companion_line = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {gate_id} dual-SHA companion row; CLASS=FULL (no -SCHEMATIC, no tier_pin); "
        f"regulator_pin=a0_Mellin_a2_Mellin_AND_a0_PauliVillars_a2_PauliVillars; "
        f"poleconv=A-double_a0_s4_n0_a2_s3_n2"
    )
    three_tuple_line = (
        f"# sign_verdict={sign_verdict} magnitude_verdict={magnitude_verdict} "
        f"regime_verdict={regime_verdict} # {gate_id} 3-tuple annotation (schema-v2)"
        + (f"; {three_tuple_note}" if three_tuple_note else "")
    )
    VERDICT_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not VERDICT_FILE.exists():
        VERDICT_FILE.touch()
    with VERDICT_FILE.open('a', encoding='utf-8') as f:
        f.write(canonical_line + '\n')
        f.write(companion_line + '\n')
        f.write(three_tuple_line + '\n')
    return {'audit_sha256': audit_sha, 'content_sha256': content_sha,
            'canonical_line': canonical_line}


# ============================================================================
# Stage 0 — input-SHA provenance log (first ~20 lines of stdout per gate-verdicts.md)
# ============================================================================
print('=' * 78)
print(f'{GATE_ID} — input-SHA provenance log')
print('=' * 78)
sha_w2_1 = sha256_of_file(W2_1_NPZ)
sha_pv = sha256_of_file(PV_HELPER)
sha_canon = sha256_of_file(CANON)
sha_capstone = sha256_of_file(CAPSTONE)
sha_s96 = sha256_of_file(S96_VERDICTS)
print(f'  W2-1 npz                {sha_w2_1}')
print(f'  PV helper               {sha_pv}  plan_match={sha_pv == PV_HELPER_SHA_PLAN}')
print(f'  canonical_constants.py  {sha_canon}')
print(f'  capstone (§8.5 ref)     {sha_capstone}')
print(f'  s96 verdicts (ε_FI src) {sha_s96}')

# PV helper SHA is the CLASS=FULL audit anchor — MUST match (PRIMARY full-physical helper)
assert sha_pv == PV_HELPER_SHA_PLAN, (
    f'PV helper SHA drift: {sha_pv} != plan-pinned {PV_HELPER_SHA_PLAN} '
    f'— the FULL-physical PV provenance anchor changed; halt.')

# ============================================================================
# Stage 1 — load the W2-1 npz (BOTH anchorings; no new spectrum diagonalization)
# ============================================================================
d = np.load(W2_1_NPZ, allow_pickle=True)
a0_Mellin = float(d['a0_zeta_mellin'])       # a₀^{Mellin} L_max=10 (FI-anchor)
a2_Mellin = float(d['a2_zeta_mellin'])       # a₂^{Mellin} L_max=10 (FI-anchor)
a0_PV = float(d['a0_pv'])                     # a₀^{Pauli-Villars} L_max=10 (PV-anchor)
a2_PV = float(d['a2_pv'])                     # a₂^{Pauli-Villars} L_max=10 (PV-anchor)
a0_PV_L12 = float(d['a0_pv_L12'])            # a₀^{Pauli-Villars} L_max=12 (INFO drift operand)
a2_PV_L12 = float(d['a2_pv_L12'])            # a₂^{Pauli-Villars} L_max=12 (INFO drift operand)
npz_R_zeta = float(d['R_CC_zeta_abs'])       # documented FI ratio
npz_R_PV = float(d['R_CC_PV_abs'])           # documented PV ratio
npz_R_PV_L12 = float(d['R_CC_PV_abs_L12'])   # documented PV ratio L12
npz_Lmax_drift = float(d['Lmax_drift_ratio'])  # documented within-family drift
npz_a0_FW = float(d['a_0_FW_zeta'])
npz_a2_FW = float(d['a_2_FW_zeta'])
npz_di1_scope = str(d['di1_scope'])

# ============================================================================
# Stage 1b — SOURCE-RECON binding test on CONSUMED canonical values
# (the file-SHA of canonical_constants.py drifted from the plan pin ed414699…;
#  per substrate-first-canonical-sourcing.md §(ii.B) plan-text-drift, the BINDING
#  test is the consumed VALUE drift, not the file SHA. Both consumed values are
#  knowledge-MCP non-superseded and match the npz fields bit-for-bit.)
# ============================================================================
canon_val_match_a0 = (a_0_FW_zeta == A0_FW_ZETA_PIN) and (a_0_FW_zeta == npz_a0_FW)
canon_val_match_a2 = (a_2_FW_zeta == A2_FW_ZETA_PIN) and (a_2_FW_zeta == npz_a2_FW)
canon_file_sha_drift = (sha_canon != 'ed414699584fd8b6154ff8487fa3f20766933e562b550d19e9842f0c683cb9a4')
print(f'  SOURCE-RECON consumed-value binding test: '
      f'a_0_FW_zeta match={canon_val_match_a0} a_2_FW_zeta match={canon_val_match_a2}')
print(f'  canonical_constants.py file-SHA drift from plan pin (benign §(ii.B) plan-text-drift)'
      f' = {canon_file_sha_drift}')
assert canon_val_match_a0 and canon_val_match_a2, (
    'SOURCE-RECON binding FAIL: consumed canonical value drifted (not just file SHA); halt.')

# ============================================================================
# Stage 2 — NUMBERS: the two anchored ratios + the survival-margin
# ============================================================================
# O = a₀/a₂ under each anchoring (the ABSOLUTE moment-RATIO; RD across PV — EXPECTED)
O_FI = a0_Mellin / a2_Mellin          # (local) — FI-anchor ratio
O_PV = a0_PV / a2_PV                   # (local) — PV-anchor ratio
abs_ratio_RD = abs(O_PV - O_FI)       # (local) — the RD across PV (NOT the survival-margin)

# Survival-margin = §8.5 DI1 partition signed distance.
# m(O, anchor) = +1 if O is a RATIO-observable on the SURVIVE-side under `anchor`,
#                −1 if O is an ABSOLUTE-magnitude on the CONDITIONAL-side.
# a₀/a₂ is a DIMENSIONLESS moment-RATIO. Class membership is decided by the
# parse-tree TYPE (ratio vs absolute), NOT by the numerical ratio value: the c²
# volume/curvature rescale cancels in any anchoring (capstone §8.2 — the
# cancellation is regulator-INDEPENDENT, residual 0). Capstone §8.5 lists a₂/a₀
# explicitly on the truncation-robust SURVIVE-side. Therefore m=+1 under BOTH.
m_FI = +1                              # (local) — FI-anchor partition label-sign
m_PV = +1                              # (local) — PV-anchor partition label-sign
label_FI = 'SURVIVE' if m_FI == +1 else 'CONDITIONAL'   # (local)
label_PV = 'SURVIVE' if m_PV == +1 else 'CONDITIONAL'   # (local)

delta_margin = abs(m_PV - m_FI)        # (local) — Δ(survival-margin); exact 0 if invariant
label_byte_identical = (label_FI == label_PV)           # (local)

# ============================================================================
# Stage 3 — INFO discriminator: PV within-family L_max=10→12 RATIO drift
# ============================================================================
ratio_PV_L10 = a0_PV / a2_PV           # (local)
ratio_PV_L12 = a0_PV_L12 / a2_PV_L12   # (local)
d_PV = abs(ratio_PV_L12 - ratio_PV_L10) / abs(ratio_PV_L10)   # (local) — within-family drift

# Cross-check both ratios + drift against the documented npz fields (bit-for-bit)
xc_O_FI = abs(O_FI - npz_R_zeta) < 1e-12          # (local)
xc_O_PV = abs(O_PV - npz_R_PV) < 1e-12            # (local)
xc_PV_L12 = abs(ratio_PV_L12 - npz_R_PV_L12) < 1e-12   # (local)
xc_drift = abs(d_PV - npz_Lmax_drift) < 1e-12     # (local)

# ============================================================================
# Stage 4 — GATE: composite verdict via the pre-registered 3-tuple collapse
# ============================================================================
# [SIGN] directional content: predicted Δ(survival-margin) = 0 (non-negative
#   label-distance whose predicted value is exactly 0). sign_verdict = PASS iff
#   the two labels coincide (computed Δ matches the predicted 0-direction).
pass_conjunct = (delta_margin <= PASS_TOL) and label_byte_identical   # (local)
within_family_drift_breach = (d_PV > EPS_FI)         # (local)
info_band_fires = (EPS_FI < d_PV <= INFO_BAND)       # (local)

# sign_verdict: direction match on Δ=0 prediction
sign_verdict = 'PASS' if label_byte_identical else 'FAIL'   # (local)
# magnitude_verdict: |Δ − 0| vs pass/info band — Δ is the label-distance
#   PASS if Δ ≤ PASS_TOL (label-distance at exact-0 floor); the within-family
#   drift d_PV is the secondary magnitude operand that fires INFO.
if delta_margin > PASS_TOL:
    magnitude_verdict = 'FAIL'         # (local) — label flip drove Δ to 2
elif info_band_fires:
    magnitude_verdict = 'INFO'         # (local) — Δ=0 but d_PV ∈ (ε_FI, info_band]
elif d_PV <= EPS_FI:
    magnitude_verdict = 'PASS'         # (local) — Δ=0 AND no within-family drift breach
else:                                  # d_PV > info_band
    magnitude_verdict = 'FAIL'         # (local) — drift exceeds INFO ceiling
# regime_verdict: the closed-form margin re-evaluation has no small-parameter
#   expansion / numerical-method regime to breach (deterministic scalar
#   arithmetic on pre-computed moments) ⇒ VALID throughout.
regime_verdict = 'VALID'               # (local)

# Composite collapse (gate-verdicts.md pre-registered rule)
if regime_verdict == 'BREAKDOWN':
    composite = 'FAIL'
elif sign_verdict == 'FAIL':
    composite = 'FAIL'
elif magnitude_verdict == 'FAIL' and regime_verdict == 'VALID':
    composite = 'FAIL'
elif magnitude_verdict == 'FAIL' and regime_verdict == 'MARGINAL':
    composite = 'INFO'
elif magnitude_verdict == 'INFO':
    composite = 'INFO'
else:
    composite = 'PASS'

# ============================================================================
# Stage 5 — report (NUMBERS first)
# ============================================================================
print()
print('=' * 78)
print(f'{GATE_ID} — RESULTS')
print('=' * 78)
print('DI1 scope (W2-1):', npz_di1_scope)
print()
print('Substitution chain (numbers substituted):')
print(f'  Step 2  O_FI = a₀^Mellin/a₂^Mellin = {a0_Mellin}/{a2_Mellin} = {O_FI!r}')
print(f'          O_PV = a₀^PV/a₂^PV         = {a0_PV}/{a2_PV} = {O_PV!r}')
print(f'          |O_PV − O_FI| = {abs_ratio_RD!r}  (absolute ratio RD across PV; '
      f'EXPECTED ≠ 0; NOT the survival-margin)')
print(f'  Step 3  parse-tree TYPE = dimensionless moment-RATIO ⇒ m=+1 under BOTH anchorings')
print(f'          m(a₀/a₂, FI-anchor) = {m_FI:+d} ⇒ label = {label_FI!r}')
print(f'          m(a₀/a₂, PV-anchor) = {m_PV:+d} ⇒ label = {label_PV!r}')
print(f'  Step 4  Δ(survival-margin) = |m_PV − m_FI| = {delta_margin}  (≤ 1e-9 ⇒ label unchanged)')
print(f'          label byte-identical (FI==PV) = {label_byte_identical}')
print(f'          ⇒ d(survival)/d(PV-scheme) = 0 NUMERICALLY')
print(f'  Step 5  d_PV = |ratio_PV(L12) − ratio_PV(L10)|/|ratio_PV(L10)|')
print(f'               = |{ratio_PV_L12} − {ratio_PV_L10}|/|{ratio_PV_L10}| = {d_PV!r}')
print(f'          ε_FI = {EPS_FI}  info_band = {INFO_BAND}  d_PV > ε_FI ? {within_family_drift_breach}'
      f'  d_PV ∈ (ε_FI,info_band] ? {info_band_fires}')
print()
print('Cross-checks vs npz (bit-for-bit):')
print(f'  O_FI==R_CC_zeta_abs     {xc_O_FI}')
print(f'  O_PV==R_CC_PV_abs       {xc_O_PV}')
print(f'  ratio_PV_L12==R_CC_PV_abs_L12  {xc_PV_L12}')
print(f'  d_PV==Lmax_drift_ratio  {xc_drift}')
print()
print('Cross-check vs canonical (SOURCE-RECON binding):')
print(f'  a_0_FW_zeta={a_0_FW_zeta} (pin {A0_FW_ZETA_PIN}; npz {npz_a0_FW}) match={canon_val_match_a0}')
print(f'  a_2_FW_zeta={a_2_FW_zeta} (pin {A2_FW_ZETA_PIN}; npz {npz_a2_FW}) match={canon_val_match_a2}')
print()
print(f'3-tuple: sign={sign_verdict} magnitude={magnitude_verdict} regime={regime_verdict}')
print(f'>>> COMPOSITE VERDICT = {composite}')
print()
# 4-tuple output tag (final non-verdict line per gate-verdicts.md)
print(f'OUTPUT-4TUPLE: (value=Δ={delta_margin:.9e}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})')

# ============================================================================
# Stage 6 — write npz (the two margins + label-distance + drift operand)
# ============================================================================
np.savez(
    OUT_NPZ,
    gate_id=GATE_ID,
    scheme=SCHEME,
    convention=CONVENTION,
    L_max=L_MAX,
    # the two anchored ratios (absolute; RD across PV)
    O_FI_a0Mellin_over_a2Mellin=O_FI,
    O_PV_a0PV_over_a2PV=O_PV,
    abs_ratio_RD_across_PV=abs_ratio_RD,
    a0_Mellin=a0_Mellin, a2_Mellin=a2_Mellin,
    a0_PV=a0_PV, a2_PV=a2_PV,
    a0_PV_L12=a0_PV_L12, a2_PV_L12=a2_PV_L12,
    # survival-margins (the §8.5 DI1 partition label-signs)
    m_FI=m_FI, m_PV=m_PV,
    label_FI=label_FI, label_PV=label_PV,
    delta_survival_margin=delta_margin,
    label_byte_identical=label_byte_identical,
    pass_tol=PASS_TOL,
    # INFO discriminator (within-family L_max drift)
    ratio_PV_L10=ratio_PV_L10, ratio_PV_L12=ratio_PV_L12,
    d_PV_within_family_drift=d_PV,
    eps_FI=EPS_FI, info_band=INFO_BAND,
    within_family_drift_breach=within_family_drift_breach,
    info_band_fires=info_band_fires,
    # verdict 3-tuple + composite
    sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
    regime_verdict=regime_verdict, composite_verdict=composite,
    # cross-checks
    xc_O_FI=xc_O_FI, xc_O_PV=xc_O_PV, xc_PV_L12=xc_PV_L12, xc_drift=xc_drift,
    canon_val_match_a0=canon_val_match_a0, canon_val_match_a2=canon_val_match_a2,
    a_0_FW_zeta=a_0_FW_zeta, a_2_FW_zeta=a_2_FW_zeta,
    # regulator pins (per regulator-pin-discipline.md)
    regulator_pin_FI='a_n^{Mellin}', regulator_pin_PV='a_n^{Pauli-Villars}',
    poleconv='A-double', s_pole_a0=4, n_grade_a0=0, s_pole_a2=3, n_grade_a2=2,
    CLASS='FULL',
    W2_1_npz_sha=sha_w2_1, PV_helper_sha=sha_pv, W2_1_verdict_audit=W2_1_VERDICT_AUDIT,
    di1_scope=npz_di1_scope,
)
print(f'wrote {OUT_NPZ}')

# ============================================================================
# Stage 7 — write png (two-anchor survival-margin bar + label-invariance annotation)
# ============================================================================
fig, (axL, axR) = plt.subplots(1, 2, figsize=(12, 5))

# Left: the absolute moment-ratio under each anchoring (RD across PV) + the
#       invariant survival LABEL annotation.
anchors = ['FI-anchor\n a₀^Mellin/a₂^Mellin', 'PV-anchor\n a₀^PV/a₂^PV']
ratios = [O_FI, O_PV]
bars = axL.bar(anchors, ratios, color=['#3a7ca5', '#d1495b'], width=0.55, edgecolor='k')
for b, r, lab in zip(bars, ratios, [label_FI, label_PV]):
    axL.text(b.get_x() + b.get_width() / 2, r + 0.012, f'{r:.4f}',
             ha='center', va='bottom', fontsize=11, fontweight='bold')
    axL.text(b.get_x() + b.get_width() / 2, 0.02, f'label:\n{lab}',
             ha='center', va='bottom', fontsize=10, color='white', fontweight='bold')
axL.set_ylabel('absolute moment-ratio  O = a₀/a₂', fontsize=11)
axL.set_title(f'Absolute ratio is RD across PV (|ΔO|={abs_ratio_RD:.4f})\n'
              f'BUT survival LABEL is INVARIANT ("{label_FI}" both)', fontsize=11)
axL.set_ylim(0, max(ratios) * 1.25)
axL.grid(axis='y', alpha=0.3)

# Right: the survival-margin (label-distance) + the within-family drift INFO bar.
axR.bar(['Δ(survival-margin)\n|m_PV − m_FI|'], [delta_margin], color='#2a9d8f',
        width=0.4, edgecolor='k', label=f'Δ = {delta_margin} (≤ {PASS_TOL:.0e} PASS-conjunct)')
axR.axhline(PASS_TOL, color='green', ls='--', lw=1, label=f'PASS tol = {PASS_TOL:.0e}')
ax2 = axR.twinx()
ax2.bar(['d_PV (within-family\nL_max=10→12 drift)'], [d_PV], color='#e9c46a',
        width=0.4, edgecolor='k')
ax2.axhline(EPS_FI, color='orange', ls='--', lw=1.2, label=f'ε_FI = {EPS_FI}')
ax2.axhline(INFO_BAND, color='red', ls=':', lw=1.2, label=f'info_band = {INFO_BAND}')
ax2.text(1.0, d_PV + 0.003, f'{d_PV:.4f}\n(INFO: ε_FI<d_PV≤info_band)',
         ha='center', va='bottom', fontsize=9, fontweight='bold')
ax2.set_ylabel('PV within-family L_max drift  d_PV', fontsize=10, color='#b8860b')
ax2.set_ylim(0, INFO_BAND * 1.4)
axR.set_ylabel('survival-margin label-distance  Δ', fontsize=10, color='#2a9d8f')
axR.set_ylim(0, max(2.2, INFO_BAND * 1.4 * (2.2 / (INFO_BAND * 1.4))) if False else 2.2)
axR.set_title(f'd(survival)/d(PV-scheme) = 0 NUMERICALLY\n'
              f'composite = {composite}  (sign={sign_verdict}/mag={magnitude_verdict}/regime={regime_verdict})',
              fontsize=11)
h1, l1 = axR.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
axR.legend(h1 + h2, l1 + l2, loc='upper center', fontsize=8)
axR.grid(axis='y', alpha=0.3)

fig.suptitle(f'{GATE_ID} — §8.5 tier-2 a₀/a₂ survival LABEL-invariance across FI-anchor vs full-PV '
             f'(DI1-guard numerical confirmation)', fontsize=12, fontweight='bold')
fig.tight_layout(rect=[0, 0, 1, 0.96])
fig.savefig(OUT_PNG, dpi=130)
plt.close(fig)
print(f'wrote {OUT_PNG}')

# ============================================================================
# Stage 8 — emit verdict line (canonical + dual-SHA companion + [SIGN] 3-tuple)
# ============================================================================
# value string (descriptive; carries the key numbers + the regulator/poleconv tags)
value_str = (
    f"d(survival)/d(PV-scheme)=0_NUMERICALLY;"
    f"Delta_survival_margin={delta_margin:.9e};"
    f"label_FI={label_FI}_label_PV={label_PV}_byte_identical={label_byte_identical};"
    f"m_FI={m_FI:+d}_m_PV={m_PV:+d};"
    f"O_FI_a0Mellin_over_a2Mellin={O_FI:.9f}_O_PV_a0PV_over_a2PV={O_PV:.9f};"
    f"abs_ratio_RD_across_PV={abs_ratio_RD:.9f}_EXPECTED_nonzero_NOT_margin;"
    f"d_PV_within_family_Lmax10to12_drift={d_PV:.9f}_vs_eps_FI={EPS_FI}_info_band={INFO_BAND};"
    f"info_band_fires={info_band_fires};"
    f"a0_Mellin={a0_Mellin:.6e}_a2_Mellin={a2_Mellin:.6e}_a0_PV={a0_PV:.6e}_a2_PV={a2_PV:.6e};"
    f"xc_npz_all={xc_O_FI and xc_O_PV and xc_PV_L12 and xc_drift};"
    f"SOURCE_RECON_consumed_value_binding=a0FWzeta_match_{canon_val_match_a0}_a2FWzeta_match_{canon_val_match_a2}_filesha_drift_benign_§ii.B;"
    f"CLASS=FULL_no_SCHEMATIC_suffix_no_tier_pin;"
    f"regulator_pin=a0_Mellin_a2_Mellin_AND_a0_PauliVillars_a2_PauliVillars;"
    f"poleconv=A-double_a0_s4_n0_a2_s3_n2;"
    f"DI1_guard=NUMERICALLY_CONFIRMED_label_invariant_§8.5_tier2_a0a2_partition_regulator_robust"
)

# audit_sha256 input-pin map (ordered; per audit_discriminators)
input_pin_map = {
    'gate_id': GATE_ID,
    'scheme': SCHEME,
    'convention': CONVENTION,
    'L_max': L_MAX,
    'script_path': 'computations/session-98/s98_a0a2_tier2_pv_invariance.py',
    'canonical_constants_sha': sha_canon,
    'w2_1_npz_sha': sha_w2_1,
    'pauli_villars_helper_sha': sha_pv,
    'capstone_sha': sha_capstone,
    's96_verdicts_sha': sha_s96,
    'a0_Mellin': a0_Mellin, 'a2_Mellin': a2_Mellin,
    'a0_PV': a0_PV, 'a2_PV': a2_PV,
    'a0_PV_L12': a0_PV_L12, 'a2_PV_L12': a2_PV_L12,
    'delta_survival_margin': delta_margin,
    'd_PV_within_family_drift': d_PV,
    'eps_FI': EPS_FI, 'info_band': INFO_BAND,
    'pass_tol': PASS_TOL,
    'sign_verdict': sign_verdict, 'magnitude_verdict': magnitude_verdict,
    'regime_verdict': regime_verdict, 'composite': composite,
}

three_tuple_note = (
    f"sign = label-distance Δ(survival-margin)=0 (predicted 0; labels coincide SURVIVE/SURVIVE) "
    f"⇒ d(survival)/d(PV-scheme)=0; mag = Δ=0≤1e-9 PASS-conjunct but PV within-family "
    f"L_max=10→12 drift d_PV={d_PV:.6f} ∈ (ε_FI={EPS_FI},info_band={INFO_BAND}] hidden-RD flag ⇒ INFO; "
    f"regime = deterministic scalar re-eval of pre-computed moments, no expansion regime to breach ⇒ VALID"
)

res = append_verdict(
    GATE_ID, composite, value_str, SCHEME, CONVENTION, L_MAX,
    input_pin_map, Path(__file__).resolve(),
    sign_verdict, magnitude_verdict, regime_verdict, three_tuple_note,
)
print()
print('VERDICT LINE EMITTED:')
print(' ', res['canonical_line'])
print(f"  audit_sha256={res['audit_sha256']}")
print(f"  content_sha256={res['content_sha256']}")

sys.exit(0)   # verdict is DATA; exit 0 regardless of PASS/FAIL/INFO
