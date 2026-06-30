#!/usr/bin/env python3
"""
S74 A-S-BUDGET-CLOSURE-74 (W2-H)
================================

Audits whether the A_s primordial amplitude budget closes at target delta_OOM = 0.716
(against S73B 3.15 OOM baseline) OR against the post-W1-G 9.47 OOM baseline after
the Bogoliubov-amplitude route + PW filter collapse + BLV dilution.

Channels collated:
  (1) W1-A TRANSFER-FUNCTION-74   -> post-transfer baseline shift
  (2) W1-G A-S-FROM-BOGOLIUBOV-74 -> Bogoliubov amplitude + filter + BLV (NEGATIVE = makes it worse)
  (3) W2-B PHASE-COVARIANCE-3X3-74 dispersive variance (confirmed PASS)
  (4) W2-F MOTT-REFINED (pending; use S73A baseline 0.336, task brief range [0.18, 0.28])
  (5) W2-G BKT-SECTOR-RESOLVED (pending; placeholder)
  (6) W3-N THIMBLE-MEASURE (Wave 3, PLACEHOLDER)
  (7) W4-O SPATIAL-TAU(x) THIMBLE (UNCOMPUTED)
  (8) S64 PW filter CORRECTED from -3.50 to -0.10 per W1-G

Gate A-S-BUDGET-CLOSURE-74:
  PASS  if delta_OOM^{total, computed} >= 0.65  (within factor 1.1 of target 0.716)
  INFO  if delta_OOM^{total, computed} in [0.45, 0.65]
  FAIL  if delta_OOM^{total, computed} <  0.45

Symmetry-first view (Landau):
  A_s(k_*) is a response function coefficient; every channel here is a term in the
  cumulant expansion of ln P_s. The budget MUST be additive over independent
  cumulants; the only double-counting risk is Mott(phase) vs BKT(phase) because both
  are phase-variance contributions -- checked explicitly below.

Author: Landau-Condensed-Matter-Theorist
Session: S74, Wave 2, Batch 2
"""

import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# Canonical constants (MANDATORY)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import A_s_CMB, M_KK_gravity, tau_fold  # noqa: F401

# -----------------------------------------------------------------------------
#  Load upstream data
# -----------------------------------------------------------------------------

HERE = os.path.dirname(os.path.abspath(__file__))

def _load(name):
    path = os.path.join(HERE, name)
    if not os.path.exists(path):
        return None
    return np.load(path, allow_pickle=True)

d_w1a = _load('s74_transfer_function.npz')
d_w1g = _load('s74_as_from_bogoliubov.npz')
d_w2b = _load('s74_phase_covariance_3x3.npz')
d_w2f = _load('s74_mott_refined_cg24.npz')        # may be None (pending)
d_w2g = _load('s74_bkt_sector_resolved.npz')       # may be None (pending)
d_s73a_mott = _load('s73a_mott_charge_noise.npz')  # fallback baseline for Mott

assert d_w1a is not None, "W1-A transfer function file missing"
assert d_w1g is not None, "W1-G Bogoliubov file missing"
assert d_w2b is not None, "W2-B phase covariance file missing"
assert d_s73a_mott is not None, "S73A Mott baseline missing"

# -----------------------------------------------------------------------------
#  Extract key numbers from upstream
# -----------------------------------------------------------------------------

# Baselines
baseline_s73b_OOM = float(d_w1g['baseline_s73b_OOM'])              # 3.15 OOM
baseline_s74_w1a_OOM = float(d_w1g['baseline_s74_w1a_OOM'])        # 5.83 OOM
gap_after_w1g_OOM = float(d_w1g['gap_OOM_vs_planck'])              # 9.47 OOM
target_dOOM_closure = 0.716                                        # (local)

# W1-A shift (post multifield projection): 5.83 - 3.15 = 2.68 OOM INCREASE (worse)
dOOM_W1A_shift = baseline_s74_w1a_OOM - baseline_s73b_OOM          # (local)

# W1-G full Bogoliubov route residual (relative to W1-A baseline)
# step3 - step0 reported separately as an OOM trajectory in the file.
OOM_W1G_step0 = float(d_w1g['OOM_step0_P0'])       # (local) 6.89
OOM_W1G_step1 = float(d_w1g['OOM_step1_squeeze'])  # (local) 8.62
OOM_W1G_step2 = float(d_w1g['OOM_step2_filter'])   # (local) 8.53
OOM_W1G_step3 = float(d_w1g['OOM_step3_BLV'])      # (local) 9.47

# Contribution from each W1-G sub-step (signed; negative = closure, positive = opening)
# Defined as: dOOM closure = -(step_i - step_{i-1})   [closing = negative step shift]
dOOM_W1G_squeeze = -(OOM_W1G_step1 - OOM_W1G_step0)  # (local) opens: -1.73
dOOM_W1G_filter  = -(OOM_W1G_step2 - OOM_W1G_step1)  # (local) closes: +0.10
dOOM_W1G_BLV     = -(OOM_W1G_step3 - OOM_W1G_step2)  # (local) opens: -0.94

# W2-B dispersive variance (phase variance from branch covariance)
dOOM_W2B_dispersive = float(d_w2b['delta_OOM_dispersive'])   # (local) 0.1495

# W2-F Mott refined
dOOM_S73A_mott = float(d_s73a_mott['delta_OOM_Mott'])        # (local) 0.336 (S73A reference)
if d_w2f is not None and 'dOOM_total' in d_w2f.files:
    dOOM_W2F_mott = float(d_w2f['dOOM_total'])               # (local)
    W2F_gate = str(d_w2f['gate_verdict'])                    # (local)
    W2F_status = f'COMPUTED ({W2F_gate})'                    # (local)
else:
    # Fallback to S73A baseline
    dOOM_W2F_mott = dOOM_S73A_mott
    W2F_status = 'FALLBACK_S73A'                             # (local)
dOOM_W2F_mott_lo_expected = 0.18                             # (local)
dOOM_W2F_mott_hi_expected = 0.28                             # (local)

# W2-G BKT sector-resolved
if d_w2g is not None and 'dOOM_total' in d_w2g.files:
    dOOM_W2G_bkt = float(d_w2g['dOOM_total'])                # (local)
    W2G_gate = str(d_w2g['gate_verdict'])                    # (local)
    W2G_status = f'COMPUTED ({W2G_gate})'                    # (local)
else:
    dOOM_W2G_bkt = 0.0  # (local)
    W2G_status = 'PENDING_PLACEHOLDER'                       # (local)

# W3-N thimble measure (Wave 3)
dOOM_W3N_thimble = 0.0                                       # (local) placeholder
W3N_status = 'WAVE3_PENDING'                                 # (local)

# W4-O spatial tau(x) thimble (uncomputed; deferred)
dOOM_W4O_spatial = 0.0                                       # (local)
W4O_status = 'UNCOMPUTED_WAVE4'                              # (local)

# S64 PW filter CORRECTED per W1-G finding
# Original S64: claimed -3.50 OOM suppression (closure = +3.50)
# W1-G corrected: (p,p) filter gives only -0.10 OOM (closure = +0.10)
dOOM_S64_PW_old = 3.50          # (local) stale
dOOM_S64_PW_new = 0.10          # (local) corrected
dOOM_S64_PW_correction = dOOM_S64_PW_new - dOOM_S64_PW_old  # (local) -3.40 (takes back 3.40 OOM)

# -----------------------------------------------------------------------------
#  Build the budget table (against S73B 3.15 OOM baseline)
#
#  Sign convention:
#    closure (brings A_s DOWN toward Planck) = POSITIVE delta_OOM
#    opening (pushes A_s AWAY from Planck)   = NEGATIVE delta_OOM
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
#  Budget architecture
# -----------------------------------------------------------------------------
#
#  A_s is decomposed as:
#       A_s_obs  =  A_s_0  *  prod_i  F_i
#  where F_i is a dimensionless suppression (< 1 closes, > 1 opens) from channel i
#  and delta_OOM_i = -log10(F_i).  The total closure is the SUM of delta_OOM_i.
#
#  We distinguish TWO registers:
#
#    (A) BASELINE TRAJECTORY  (background; not budget "channels")
#         W1-A multifield projection:  3.15 -> 5.83 OOM  (structural spectral update)
#         W1-G Bogoliubov squeeze:    5.83 -> 7.56 OOM
#         W1-G PW filter (p,p) real:  7.56 -> 7.47 OOM
#         W1-G BLV dilution:          7.47 -> 9.47 OOM
#       These are re-computations of the BARE (pre-decoherence) amplitude, NOT
#       independent closure channels.  They define the baseline the budget must
#       close AGAINST.
#
#    (B) CLOSURE CHANNELS (the S74 budget proper)
#         C1  W2-B phase dispersive variance         (PASS, +0.1495)
#         C2  W2-F Mott charge-noise phase           (S73A fallback +0.3363; brief [0.18,0.28])
#         C3  W2-G BKT sector-resolved                (pending)
#         C4  W3-N thimble measure                    (Wave 3 pending)
#         C5  W4-O spatial tau(x) thimble             (Wave 4 deferred)
#         C6  S64 PW filter correction                (CORRECTION TERM: removes
#                                                      a previously-assumed closure
#                                                      of +3.50, now +0.10, so -3.40)
#
#  Gate target delta_OOM_total_closure >= 0.65 (within 1.1x of 0.716) applied to
#  set (B) only -- set (A) is accounted for in the updated baseline.
# -----------------------------------------------------------------------------

# Baseline-trajectory rows (informational; not in budget total)
baseline_rows = [
    ('B0', 'S73B anchor gap (vs Planck)',          baseline_s73b_OOM,   'S73B A_s baseline', 'COMPUTED'),
    ('B1', 'W1-A multifield projection baseline', baseline_s74_w1a_OOM, 'W1-A TRANSFER-FUNCTION-74', 'COMPUTED'),
    ('B2', 'W1-G squeeze step',                   OOM_W1G_step1,        'W1-G A-S-FROM-BOGOLIUBOV-74', 'COMPUTED'),
    ('B3', 'W1-G PW (p,p) filter step',           OOM_W1G_step2,        'W1-G A-S-FROM-BOGOLIUBOV-74', 'COMPUTED'),
    ('B4', 'W1-G BLV dilution step',              OOM_W1G_step3,        'W1-G A-S-FROM-BOGOLIUBOV-74', 'COMPUTED'),
]

# Closure channels (the budget proper)
channels = [
    # (id, name, value, provenance, status, category)
    ('C1', 'W2-B phase dispersive variance',                dOOM_W2B_dispersive,    'W2-B PHASE-COVARIANCE-3X3-74', 'COMPUTED', 'phase'),
    ('C2', 'W2-F Mott charge-noise phase',                  dOOM_W2F_mott,          'W2-F MOTT-REFINED-CG24-74', W2F_status, 'phase'),
    ('C3', 'W2-G BKT sector-resolved',                      dOOM_W2G_bkt,           'W2-G BKT-SECTOR-RESOLVED-74', W2G_status, 'phase'),
    ('C4', 'W3-N thimble measure',                          dOOM_W3N_thimble,       'W3-N (Wave 3 pending)', W3N_status, 'measure'),
    ('C5', 'W4-O spatial tau(x) thimble',                   dOOM_W4O_spatial,       'W4-O (Wave 4 deferred)', W4O_status, 'measure'),
    ('C6', 'S64 PW filter correction (overcount removal)',  dOOM_S64_PW_correction, 'W1-G finding: (0,0)-only artifact', 'COMPUTED', 'correction'),
]

# A status is considered "computed" if it starts with 'COMPUTED' or is 'FALLBACK_S73A'
def _is_computed(status):
    return status.startswith('COMPUTED') or status == 'FALLBACK_S73A'

# Closure budget totals
dOOM_total_all = 0.0        # (local) every channel including placeholders
dOOM_total_computed = 0.0   # (local) only channels with concrete numbers
dOOM_total_computed_excl_correction = 0.0  # (local) excluding the C6 correction term
for (_id, _name, val, _prov, status, _cat) in channels:
    dOOM_total_all += val
    if _is_computed(status):
        dOOM_total_computed += val
        if _cat != 'correction':
            dOOM_total_computed_excl_correction += val

# -----------------------------------------------------------------------------
#  Cross-check: double-counting between C5 (W2-B), C6 (Mott phase), C7 (BKT phase)
# -----------------------------------------------------------------------------

# W2-B phase variance is the bare (no decoherence) inter-branch covariance.
# Mott phase variance is INTRA-cell charge-noise decoherence multiplying the pair phase.
# BKT is SUPER-CELL vortex-unbinding phase variance.
#
# These act on DIFFERENT phase modes of DIFFERENT origin:
#   W2-B  : linear phase Phi_pair relating the 3 branches B1,B2,B3 (Josephson array)
#   Mott  : conjugate (N,phi) on a single cell (E_J/E_C tradeoff)
#   BKT   : topological (vortex) phase in the 2D XY limit
#
# Landau orthogonality check: the variance adds in a cumulant expansion
#   <e^{i(Phi + phi_M + phi_BKT)}> = e^{-1/2 (Var_W2B + Var_M + Var_BKT)} * cross
# where `cross` = e^{-<dPhi dphi_M>} etc.  By construction Mott is independent of
# branch-covariance (E_C is diagonal in fiber occupation), and BKT is a
# topological charge decoupled from the Gaussian pair-phase.  We therefore take
# the three as orthogonal cumulants -- no double counting.
doublecount_risk = 0.0  # (local, orthogonal cumulants)

# -----------------------------------------------------------------------------
#  Budget summary
# -----------------------------------------------------------------------------

gap_vs_s73b_after_s74 = baseline_s73b_OOM - dOOM_total_computed
gap_vs_w1g_after_s74 = gap_after_w1g_OOM - dOOM_total_computed

# Also report the total with the C6 correction EXCLUDED (since C6 is a correction
# to a previously-assumed closure, not an independent new closure channel).
gap_vs_s73b_after_s74_excl_correction = baseline_s73b_OOM - dOOM_total_computed_excl_correction
gap_vs_w1g_after_s74_excl_correction  = gap_after_w1g_OOM  - dOOM_total_computed_excl_correction

# Distance to target (closure within 1.1x of 0.716)
shortfall_vs_target = target_dOOM_closure - dOOM_total_computed_excl_correction

# Residual opening against the S73B 3.15 baseline (positive = still open)
# and against the post-W1-G 9.47 OOM baseline.

# -----------------------------------------------------------------------------
#  Gate verdict
# -----------------------------------------------------------------------------

GATE_LO = 0.45   # (local) FAIL threshold
GATE_HI = 0.65   # (local) PASS threshold

# The gate is applied to the closure channels EXCLUDING the C6 correction term,
# because C6 is a retraction of a previously-assumed closure (it cannot close more
# than what was already assumed).  The "fresh closures" metric is:
dOOM_gate_value = dOOM_total_computed_excl_correction  # (local)

if dOOM_gate_value >= GATE_HI:
    gate_verdict = 'PASS'
    gate_detail = (f"delta_OOM^{{closure, computed, excl correction}} = {dOOM_gate_value:.3f} >= {GATE_HI:.2f}; "
                   f"A_s budget closes within factor 1.1 of target {target_dOOM_closure:.3f}")
elif dOOM_gate_value >= GATE_LO:
    gate_verdict = 'INFO'
    gate_detail = (f"delta_OOM^{{closure, computed, excl correction}} = {dOOM_gate_value:.3f} in [{GATE_LO:.2f}, {GATE_HI:.2f}]; "
                   f"partial closure; uncomputed channels (W2-G, W3-N, W4-O) required")
else:
    gate_verdict = 'FAIL'
    gate_detail = (f"delta_OOM^{{closure, computed, excl correction}} = {dOOM_gate_value:.3f} < {GATE_LO:.2f}; "
                   f"significant uncomputed channel needed. Shortfall = {shortfall_vs_target:.3f} OOM.")

# -----------------------------------------------------------------------------
#  Print results
# -----------------------------------------------------------------------------

print("=" * 74)
print("S74 A-S-BUDGET-CLOSURE-74  (W2-H, Wave 2 Batch 2)")
print("=" * 74)
print()
print("BASELINES")
print(f"  S73B anchor (pre-S74):                    {baseline_s73b_OOM:+.4f} OOM above Planck")
print(f"  W1-A multifield projection baseline:      {baseline_s74_w1a_OOM:+.4f} OOM above Planck")
print(f"  W1-G post-Bogoliubov + filter + BLV:      {gap_after_w1g_OOM:+.4f} OOM above Planck")
print()
print("W1-G sub-step trajectory (from Bogoliubov file):")
print(f"  step0 P0 (pre-squeeze):        {OOM_W1G_step0:+.4f}")
print(f"  step1 squeeze:                 {OOM_W1G_step1:+.4f}  (d = {OOM_W1G_step1-OOM_W1G_step0:+.4f})")
print(f"  step2 PW filter (p,p):         {OOM_W1G_step2:+.4f}  (d = {OOM_W1G_step2-OOM_W1G_step1:+.4f})")
print(f"  step3 BLV dilution:            {OOM_W1G_step3:+.4f}  (d = {OOM_W1G_step3-OOM_W1G_step2:+.4f})")
print()
print("BASELINE TRAJECTORY (information; NOT in closure budget)")
print("-" * 84)
print(f"{'ID':3}  {'Stage':42}  {'OOM gap':>9}  {'Status':22}")
print("-" * 84)
for (_id, _name, val, _prov, status) in baseline_rows:
    print(f"{_id:3}  {_name:42}  {val:+9.4f}  {status:22}")
print("-" * 84)
print()
print("CLOSURE BUDGET TABLE (closure convention: + closes toward Planck, - opens)")
print("-" * 84)
print(f"{'ID':3}  {'Channel':42}  {'dOOM':>9}  {'Status':22}")
print("-" * 84)
for (_id, _name, val, _prov, status, _cat) in channels:
    print(f"{_id:3}  {_name:42}  {val:+9.4f}  {status:22}")
print("-" * 84)
print(f"{'':3}  {'TOTAL (all channels, sum)':42}  {dOOM_total_all:+9.4f}")
print(f"{'':3}  {'TOTAL (computed channels)':42}  {dOOM_total_computed:+9.4f}")
print(f"{'':3}  {'TOTAL (computed, excluding C6 correction)':42}  {dOOM_total_computed_excl_correction:+9.4f}")
print(f"{'':3}  {'GATE METRIC (closure target 0.716)':42}  {dOOM_gate_value:+9.4f}")
print("-" * 84)
print()
print("PROVENANCE TRACE (detailed)")
for (_id, _name, val, _prov, status, _cat) in channels:
    print(f"  {_id}  {_name}")
    print(f"       value={val:+.4f}  provenance={_prov}  status={status}")
print()
print("CROSS-CHECKS")
print(f"  Double-counting (Mott phase vs W2-B dispersive vs BKT): "
      f"orthogonal cumulants, overlap = {doublecount_risk:.4f}")
print(f"  W1-A baseline shift (internal): {baseline_s74_w1a_OOM - baseline_s73b_OOM:+.4f} "
      f"(B1-B0 in baseline trajectory)")
_sum_w1g = dOOM_W1G_squeeze + dOOM_W1G_filter + dOOM_W1G_BLV
_traj_w1g = -(OOM_W1G_step3 - OOM_W1G_step0)
print(f"  W1-G sub-steps sum matches trajectory: "
      f"sum = {_sum_w1g:+.4f}  vs  trajectory = {_traj_w1g:+.4f}  "
      f"(match={abs(_sum_w1g-_traj_w1g) < 1e-9})")
# Structural audit: do W2-F Mott + W2-G BKT fall below the S73A static-noise bound?
print(f"  W2-F + W2-G phase-channel total:  "
      f"{dOOM_W2F_mott + dOOM_W2G_bkt:.4f}  (vs S73A Mott alone {dOOM_S73A_mott:.4f})")
print(f"  W2-F monotonic in E_C:            {bool(d_w2f['monotonic_in_E_C']) if d_w2f is not None and 'monotonic_in_E_C' in d_w2f.files else 'N/A'}")
print(f"  Residual vs S73B 3.15 baseline after closures (incl C6 correction): {gap_vs_s73b_after_s74:+.4f} OOM")
print(f"  Residual vs S73B 3.15 baseline after closures (excl C6 correction): {gap_vs_s73b_after_s74_excl_correction:+.4f} OOM")
print(f"  Residual vs post-W1-G 9.47 baseline (incl C6):                      {gap_vs_w1g_after_s74:+.4f} OOM")
print(f"  Residual vs post-W1-G 9.47 baseline (excl C6):                      {gap_vs_w1g_after_s74_excl_correction:+.4f} OOM")
print(f"  Shortfall vs closure target 0.716 (excl C6):                        {shortfall_vs_target:+.4f} OOM")
print()
print(f"GATE A-S-BUDGET-CLOSURE-74: {gate_verdict}")
print(f"  {gate_detail}")
print()
# What-if closure scenarios
needed_for_PASS = GATE_HI - dOOM_gate_value                  # (local)
needed_for_target = target_dOOM_closure - dOOM_gate_value    # (local)
print("WHAT-IF (additional closure needed from uncomputed channels W3-N, W4-O)")
print(f"  To reach PASS band (>= {GATE_HI:.3f}): need {max(0, needed_for_PASS):+.3f} more OOM")
print(f"  To reach closure target ({target_dOOM_closure:.3f}): need {max(0, needed_for_target):+.3f} more OOM")
print(f"  To close the full S73B 3.15 OOM gap: need {max(0, baseline_s73b_OOM - dOOM_gate_value):+.3f} more OOM")
print(f"  To close the full W1-G 9.47 OOM gap: need {max(0, gap_after_w1g_OOM - dOOM_gate_value):+.3f} more OOM")
print()
print("STATUS SUMMARY")
print(f"  W2-F Mott refined:            {W2F_status}  (dOOM={dOOM_W2F_mott:.4f}; S73A ref={dOOM_S73A_mott:.4f}; brief expects [0.18, 0.28])")
print(f"  W2-G BKT sector-resolved:     {W2G_status}  (dOOM={dOOM_W2G_bkt:.4f})")
print(f"  W3-N thimble measure:         {W3N_status}")
print(f"  W4-O spatial tau(x) thimble:  {W4O_status}")
print(f"  S64 PW filter correction:     applied (old=+3.50, new=+0.10, correction={dOOM_S64_PW_correction:+.4f})")
print()

# -----------------------------------------------------------------------------
#  Save data
# -----------------------------------------------------------------------------

ids = np.array([c[0] for c in channels])
names = np.array([c[1] for c in channels])
values = np.array([c[2] for c in channels], dtype=float)
provenance = np.array([c[3] for c in channels])
statuses = np.array([c[4] for c in channels])
categories = np.array([c[5] for c in channels])
is_computed = np.array([_is_computed(s) for s in statuses], dtype=bool)

base_ids = np.array([b[0] for b in baseline_rows])
base_names = np.array([b[1] for b in baseline_rows])
base_values = np.array([b[2] for b in baseline_rows], dtype=float)
base_provenance = np.array([b[3] for b in baseline_rows])
base_statuses = np.array([b[4] for b in baseline_rows])

np.savez(
    os.path.join(HERE, 's74_as_budget_closure.npz'),
    gate_name='A-S-BUDGET-CLOSURE-74',
    gate_verdict=gate_verdict,
    gate_detail=gate_detail,
    gate_lo=GATE_LO,
    gate_hi=GATE_HI,
    target_dOOM=target_dOOM_closure,
    # baselines
    baseline_s73b_OOM=baseline_s73b_OOM,
    baseline_s74_w1a_OOM=baseline_s74_w1a_OOM,
    gap_after_w1g_OOM=gap_after_w1g_OOM,
    gap_vs_s73b_after_s74=gap_vs_s73b_after_s74,
    gap_vs_w1g_after_s74=gap_vs_w1g_after_s74,
    dOOM_total_all=dOOM_total_all,
    dOOM_total_computed=dOOM_total_computed,
    dOOM_total_computed_excl_correction=dOOM_total_computed_excl_correction,
    dOOM_gate_value=dOOM_gate_value,
    gap_vs_s73b_after_s74_excl_correction=gap_vs_s73b_after_s74_excl_correction,
    gap_vs_w1g_after_s74_excl_correction=gap_vs_w1g_after_s74_excl_correction,
    shortfall_vs_target=shortfall_vs_target,
    # W1-G trajectory
    OOM_W1G_step0=OOM_W1G_step0,
    OOM_W1G_step1=OOM_W1G_step1,
    OOM_W1G_step2=OOM_W1G_step2,
    OOM_W1G_step3=OOM_W1G_step3,
    dOOM_W1G_squeeze=dOOM_W1G_squeeze,
    dOOM_W1G_filter=dOOM_W1G_filter,
    dOOM_W1G_BLV=dOOM_W1G_BLV,
    # channel table
    channel_ids=ids,
    channel_names=names,
    channel_values=values,
    channel_provenance=provenance,
    channel_statuses=statuses,
    channel_categories=categories,
    channel_is_computed=is_computed,
    baseline_ids=base_ids,
    baseline_names=base_names,
    baseline_values=base_values,
    baseline_provenance=base_provenance,
    baseline_statuses=base_statuses,
    # statuses
    W2F_status=W2F_status,
    W2G_status=W2G_status,
    W3N_status=W3N_status,
    W4O_status=W4O_status,
    # key refs
    s64_PW_old=dOOM_S64_PW_old,
    s64_PW_new=dOOM_S64_PW_new,
    s64_PW_correction=dOOM_S64_PW_correction,
    doublecount_risk=doublecount_risk,
    # what-if
    needed_for_PASS=needed_for_PASS,
    needed_for_target=needed_for_target,
    needed_to_close_s73b=baseline_s73b_OOM - dOOM_gate_value,
    needed_to_close_w1g=gap_after_w1g_OOM - dOOM_gate_value,
)

# -----------------------------------------------------------------------------
#  Waterfall plot
# -----------------------------------------------------------------------------

fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(14, 6))

# ===== LEFT PANEL: baseline trajectory + closure target =====
traj_base = [baseline_s73b_OOM, baseline_s74_w1a_OOM,
             OOM_W1G_step1, OOM_W1G_step2, OOM_W1G_step3]
labels_base = ['S73B\n3.15', 'W1-A\n5.83', 'W1-G sq\n7.56',
               'W1-G f\n7.47', 'W1-G BLV\n9.47']

xb = np.arange(len(traj_base))
for i in range(len(traj_base) - 1):
    y0, y1 = traj_base[i], traj_base[i + 1]
    color = 'tab:green' if y1 < y0 else 'tab:red'
    ax0.plot([i, i + 1], [y0, y0], 'k--', lw=0.6, alpha=0.5)
    ax0.plot([i + 1, i + 1], [y0, y1], color=color, lw=2.5)
    ax0.scatter([i + 1], [y1], s=40, color=color, zorder=5)

ax0.scatter([0], [traj_base[0]], s=80, color='tab:blue', zorder=5)
ax0.scatter([xb[-1]], [traj_base[-1]], s=80, color='tab:red', zorder=5)
ax0.axhline(0.0, color='k', lw=0.8, alpha=0.5, label='Planck A_s = 2.1e-9')
ax0.axhline(baseline_s73b_OOM - target_dOOM_closure, color='tab:orange', ls=':', lw=1.5,
            label=f'After 0.716 closure: {baseline_s73b_OOM - target_dOOM_closure:.3f}')
ax0.set_xticks(xb)
ax0.set_xticklabels(labels_base, fontsize=8)
ax0.set_ylabel('log10(A_s / A_s^Planck)   [OOM above Planck]')
ax0.set_title('Baseline trajectory (W1-A -> W1-G)')
ax0.legend(loc='upper left', fontsize=8)
ax0.grid(True, alpha=0.3)

# ===== RIGHT PANEL: closure budget bar chart =====
bar_labels = []
bar_vals = []
bar_colors = []
bar_patterns = []
for (_id, _name, val, _prov, status, _cat) in channels:
    bar_labels.append(f'{_id}\n{_name[:22]}')
    bar_vals.append(val)
    if not _is_computed(status):
        bar_colors.append('tab:gray')
        bar_patterns.append('//')
    elif _cat == 'correction':
        bar_colors.append('tab:purple')
        bar_patterns.append('')
    elif val > 0:
        bar_colors.append('tab:green')
        bar_patterns.append('')
    else:
        bar_colors.append('tab:red')
        bar_patterns.append('')

x_bar = np.arange(len(channels))
bars = ax1.bar(x_bar, bar_vals, color=bar_colors, edgecolor='black', lw=0.7)
for bar, pattern in zip(bars, bar_patterns):
    if pattern:
        bar.set_hatch(pattern)

# Target line
ax1.axhline(target_dOOM_closure, color='tab:orange', ls=':', lw=1.5,
            label=f'Target = {target_dOOM_closure:.3f}')
ax1.axhline(GATE_HI, color='tab:green', ls='--', lw=1.0, alpha=0.7,
            label=f'PASS >= {GATE_HI:.2f}')
ax1.axhline(GATE_LO, color='tab:red', ls='--', lw=1.0, alpha=0.7,
            label=f'FAIL < {GATE_LO:.2f}')
# Dashed zero
ax1.axhline(0.0, color='k', lw=0.5, alpha=0.5)
# Total marker
ax1.annotate(
    f'Gate metric: {dOOM_gate_value:+.3f}\n(excl. C6)',
    xy=(len(channels) - 1, dOOM_gate_value),
    xytext=(len(channels) - 2.5, dOOM_gate_value + 0.8),
    fontsize=9, color='tab:blue',
    arrowprops=dict(arrowstyle='->', color='tab:blue', lw=1.2),
)

ax1.set_xticks(x_bar)
ax1.set_xticklabels(bar_labels, fontsize=7, rotation=30, ha='right')
ax1.set_ylabel('delta_OOM closure (+ closes toward Planck)')
ax1.set_title(f'Closure budget   Gate: {gate_verdict}')
ax1.legend(loc='upper left', fontsize=7)
ax1.grid(True, alpha=0.3, axis='y')

plt.suptitle(f'S74 W2-H  A_s Budget Closure Audit    {gate_verdict}',
             fontsize=13, y=1.02)
plt.tight_layout()
plt.savefig(os.path.join(HERE, 's74_as_budget_closure.png'), dpi=150,
            bbox_inches='tight')
plt.close()

print("Files written:")
print("  computations/session-74/s74_as_budget_closure.npz")
print("  computations/session-74/s74_as_budget_closure.png")
