#!/usr/bin/env python3
"""
S82 W3-6: SIC-PHYSICAL-CAP — Physical cap on S_IC from energy conservation
===========================================================================

Gate: S82-SIC-PHYSICAL-CAP  [VERIFY] + [CHAIN]
Classification: PHONONIC
Owner: transit-dynamics-theorist
Pre-reg anchor: sessions/session-plan/session-80-plan.md §W3-6 L1848-L1871

Phononic framing (substrate-direction, per CLAUDE.md phononic-framing rule):
  Parker mode production at the fold deposits energy into per-band GGE
  occupations n_k (phononic excitations of the Ordered Veil).  The SQUEEZING
  factor S_IC(k) = 1 + 2 n_k measures how strongly the phononic two-point
  function is amplified over the Bunch-Davies (vacuum) baseline.  Energy
  conservation at the transit places a HARD UPPER BOUND on how much n_k can
  be produced: the total energy deposited in all phononic modes cannot exceed
  the available substrate energy budget at fold.  That bound is the PHYSICAL
  CAP on S_IC.

  This test asks: is the S78 W1-E observation S_IC ~ 1.636e5 at k_pivot_fold
  KINEMATICALLY ALLOWED by energy conservation?  If the energy-conservation
  cap is vastly smaller than S_IC, then the W1-E value is UNPHYSICAL (arising
  from mode-equation divergence without backreaction).  If the cap is within
  factor-10 of S_IC, the W1-E amplification is physically admissible (but the
  saturation flag is still diagnostic).

Pre-registered gate (S80 plan L1856-L1862):
  GATE: S82-SIC-PHYSICAL-CAP
  HYPOTHESIS: Physical cap on S_IC from energy conservation exists at fold.
  PRE-REGISTERED: S_IC_cap value; compared to S78 W1-E S_IC = 1.636e+05.
  PASS: Cap within factor-10 of observed S_IC.       |log10(cap/obs)| < 1.0
  INFO: factor-10 to factor-100.                     1.0 <= |log10| < 2.0
  FAIL: > factor-100.                                |log10| >= 2.0

Substitution chain (pre-computation, SIGN/DIRECTION rule per math-scripts.md):

  Step 1 (definitions):
    S_IC(k)        = 1 + 2 n_k              [squeezing factor, W2-4 GGE form]
    n_k            = pair occupation per mode (dimensionless, n_k >= 0)
    omega_k        = mode frequency (per-band gap in BCS units, M_KK)
    E_budget       = total energy available to phononic modes at transit
                   = S_fold (condensation-energy density, canonical_constants)
                     OR |dS_fold|*dt_transit (spectral-action work-done reading)
    N_modes        = total number of Bogoliubov modes across 3 bands = 8
                     (per S43 band multiplicity 3+3+2)

  Step 2 (energy conservation):
    sum_modes [omega_k * n_k] <= E_budget       [per-volume, all modes, all bands]

    Equipartition reading (isotropic Haar over N_modes):
    omega_k * n_k^cap  =  E_budget / N_modes       [per mode]
    n_k^cap            =  E_budget / (N_modes * omega_k)

  Step 3 (canonical form):
    S_IC^cap(k)  =  1 + 2 * E_budget / (N_modes * omega_k)
                 =  1 + (2 * E_budget) / (N_modes * omega_k)

  Step 4 (direction):
    n_k^cap is LARGER for SMALLER omega_k (softer modes).  The most soft band
    (B3: Delta_B3 = 0.176 M_KK) has the HIGHEST physical cap.  This is
    consistent with Parker's rule that IR modes dominate particle production.

  Conclusion:
    S_IC^cap is a positive, finite, omega-dependent upper bound.  Whether it
    satisfies the factor-10 gate vs S78 W1-E = 1.636e+05 is a NUMERICAL
    verdict determined by the energy-budget reading.

Two energy-budget readings (both pre-registered):
  R-WD : E_budget = |dS_fold| * dt_transit      (spectral-action work done)
  R-SF : E_budget = S_fold                      (fold condensation energy)

Three band readings (per S43):
  B2 (flat):    Delta_0_GL   = 0.7704 M_KK
  B1 (acoustic):Delta_0_OES  = 0.4643 M_KK
  B3 (softest): Delta_B3     = 0.176  M_KK     [CMB pivot band]

CMB-pivot choice: B3 (softest band) — this is the band that dominates the
S78 W1-E S_IC observation at k_pivot (S79 W1-E confirmed soft-band CMB
correspondence).  The PRIMARY cap reading is therefore R-SF at B3:

    S_IC^cap_primary = S_fold-reading at B3

Compared against S78 W1-E S_IC(k_pivot_fold) = 1.636e+05.

Environment:
  Scalar arithmetic; no linear algebra.  OMP thread cap per computation rule.
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
import json
import hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Canonical constants (MANDATORY)
from canonical_constants import (
    M_KK_gravity,
    M_Pl_reduced,
    A_s_CMB,
    S_fold,            # fold condensation energy density (substrate units)
    dS_fold,           # dS/dtau at fold (spectral-action gradient)
    dt_transit,        # transit duration (M_KK^-1)
    tau_fold,          # 0.190
    T_GGE_B2,          # B2-sector GGE temperature (S43)
    Delta_0_GL,        # B2 gap = 0.7704 M_KK
    Delta_0_OES,       # B1 gap = 0.4643 M_KK
    Delta_B3,          # B3 gap = 0.176  M_KK
    n_pairs,           # 59.8 Bogoliubov pairs from S38 transit
)

# Per-band GGE temperatures (from S43 gge-temp-43-result agent-memory;
# documented in canonical_constants header S43 block)
T_GGE_B1_local = 0.435            # (local) S43 gge-temp-43 result
T_GGE_B3_local = 0.178            # (local) S43 gge-temp-43 result

# Band multiplicities per S43 gge-temp-43 (3/3/2 for B2/B1/B3)
mult_B2 = 3                       # (local) S43 gge-temp-43-result
mult_B1 = 3                       # (local) S43 gge-temp-43-result
mult_B3 = 2                       # (local) S43 gge-temp-43-result
N_modes_total = mult_B2 + mult_B1 + mult_B3  # (local) = 8, S38 Bogoliubov count

# S78 W1-E observed S_IC at k_pivot_fold (cross-check baseline, per S80 plan)
# The three IC principles (SS, ME, AZ) spread within factor 1.13 in the
# oscillatory regime; we use the central value for comparison.
S_IC_W1E_observed = 163574.03353246546    # (local) S78 W1-E spectral_stationarity
S_IC_W1E_SS = 163574.03353246546          # (local) S78 W1-E
S_IC_W1E_ME = 185397.65104763655          # (local) S78 W1-E min_entropy
S_IC_W1E_AZ = 163574.03353246546          # (local) S78 W1-E az_topology

# ============================================================
# SECTION 0: Input SHA-256 pins (MANDATORY in first 20 lines)
# ============================================================
HERE = os.path.dirname(os.path.abspath(__file__))                  # (local)


def _sha256(path):
    with open(path, 'rb') as h:
        return hashlib.sha256(h.read()).hexdigest()


INPUT_FILES = [                                                    # (local)
    os.path.join(HERE, 'canonical_constants.py'),
    os.path.join(HERE, 's82_w2_4_ps_substrate_matched_ic.py'),
    os.path.join(HERE, 's82_w2_4_ps_substrate_matched_ic.npz'),
    os.path.join(HERE, 's78_pre_fold_vacuum.npz'),
]

print("=" * 70)
print("S82 W3-6: SIC-PHYSICAL-CAP (energy-conservation upper bound)")
print("=" * 70)
print("\n[SEC 0] Input SHA-256 pins")
INPUT_SHAS = {}                                                    # (local)
for _f in INPUT_FILES:
    if os.path.exists(_f):
        _h = _sha256(_f)                                           # (local)
        INPUT_SHAS[os.path.basename(_f)] = _h
        print(f"  {os.path.basename(_f):46s} sha256={_h[:16]}...{_h[-8:]}")
    else:
        INPUT_SHAS[os.path.basename(_f)] = None
        print(f"  {os.path.basename(_f):46s} MISSING")

# ============================================================
# SECTION 1: Energy budget readings (both pre-registered)
# ============================================================
print("\n[SEC 1] Energy-budget readings (natural M_KK^4/Vol_SU3 units)")

# R-WD: spectral-action work done over transit time
#   dE/dtau = dS_fold * (dtau/dt)    (rate of spectral-action change)
#   E_WD    = |dS_fold| * dt_transit (total work done during diabatic transit)
E_budget_WD = abs(float(dS_fold)) * float(dt_transit)              # (local)

# R-SF: fold condensation-energy density (substrate-native quantity)
#   This is the TOTAL spectral-action energy stored at the fold configuration
E_budget_SF = float(S_fold)                                        # (local)

print(f"  R-WD: E = |dS_fold| * dt_transit = {abs(float(dS_fold)):.3e} * {float(dt_transit):.3e}")
print(f"          = {E_budget_WD:.4e}")
print(f"  R-SF: E = S_fold                 = {E_budget_SF:.4e}")
print(f"  Ratio R-SF / R-WD                = {E_budget_SF/E_budget_WD:.3e}")

# ============================================================
# SECTION 2: Per-band cap calculation
# ============================================================
print("\n[SEC 2] Per-band physical cap S_IC^cap = 1 + 2 E / (N_modes * omega)")

# Per-band frequencies (gap scale as effective soft-mode energy)
omega_B2 = float(Delta_0_GL)       # (local) 0.7704 M_KK
omega_B1 = float(Delta_0_OES)      # (local) 0.4643 M_KK
omega_B3 = float(Delta_B3)         # (local) 0.176  M_KK

print(f"  omega_B2 = {omega_B2:.4f} M_KK")
print(f"  omega_B1 = {omega_B1:.4f} M_KK")
print(f"  omega_B3 = {omega_B3:.4f} M_KK   [CMB pivot, softest]")
print(f"  N_modes_total = {N_modes_total}  (= mult_B2 + mult_B1 + mult_B3 = 3+3+2)")


def cap_for(E_budget, omega, N_modes=N_modes_total):
    """Physical cap on S_IC from energy conservation: S_IC^cap = 1 + 2 n_cap."""
    n_cap = E_budget / (N_modes * omega)         # (local)
    S_cap = 1.0 + 2.0 * n_cap                     # (local)
    return n_cap, S_cap


# R-WD per-band caps
print("\n  R-WD (work-done reading) per-band caps:")
n_WD_B2, S_WD_B2 = cap_for(E_budget_WD, omega_B2)
n_WD_B1, S_WD_B1 = cap_for(E_budget_WD, omega_B1)
n_WD_B3, S_WD_B3 = cap_for(E_budget_WD, omega_B3)
print(f"    B2: n_cap = {n_WD_B2:.3e}, S_IC^cap = {S_WD_B2:.4e}, log10 = {np.log10(S_WD_B2):+.3f}")
print(f"    B1: n_cap = {n_WD_B1:.3e}, S_IC^cap = {S_WD_B1:.4e}, log10 = {np.log10(S_WD_B1):+.3f}")
print(f"    B3: n_cap = {n_WD_B3:.3e}, S_IC^cap = {S_WD_B3:.4e}, log10 = {np.log10(S_WD_B3):+.3f}")

# R-SF per-band caps
print("\n  R-SF (condensation-energy reading) per-band caps:")
n_SF_B2, S_SF_B2 = cap_for(E_budget_SF, omega_B2)
n_SF_B1, S_SF_B1 = cap_for(E_budget_SF, omega_B1)
n_SF_B3, S_SF_B3 = cap_for(E_budget_SF, omega_B3)
print(f"    B2: n_cap = {n_SF_B2:.3e}, S_IC^cap = {S_SF_B2:.4e}, log10 = {np.log10(S_SF_B2):+.3f}")
print(f"    B1: n_cap = {n_SF_B1:.3e}, S_IC^cap = {S_SF_B1:.4e}, log10 = {np.log10(S_SF_B1):+.3f}")
print(f"    B3: n_cap = {n_SF_B3:.3e}, S_IC^cap = {S_SF_B3:.4e}, log10 = {np.log10(S_SF_B3):+.3f}")

# Structural cross-check: cap monotonic-decreasing in omega within each reading
# n_cap ∝ 1/omega ⇒ n_cap(B3) > n_cap(B1) > n_cap(B2)  since omega ordering is reverse
struct_check_WD = (n_WD_B3 > n_WD_B1 > n_WD_B2)            # (local)
struct_check_SF = (n_SF_B3 > n_SF_B1 > n_SF_B2)            # (local)
print(f"\n  Structural monotonicity n_cap(B3) > n_cap(B1) > n_cap(B2):")
print(f"    R-WD: {struct_check_WD}")
print(f"    R-SF: {struct_check_SF}")
assert struct_check_WD and struct_check_SF, \
    "STRUCTURAL VIOLATION: softer mode should have larger cap"

# ============================================================
# SECTION 3: Primary reading — R-SF at B3 (CMB pivot, softest)
# ============================================================
print("\n[SEC 3] PRIMARY cap: R-SF (condensation-energy) at B3 (CMB pivot)")

S_IC_cap_primary = S_SF_B3                                        # (local)
print(f"  S_IC^cap (primary) = {S_IC_cap_primary:.4e}")
print(f"  log10              = {np.log10(S_IC_cap_primary):+.4f}")

# Cap via the two other bands (conservative floor; acoustic B1 and flat B2)
S_IC_cap_floor_acoustic = S_SF_B1                                 # (local)
S_IC_cap_floor_flat     = S_SF_B2                                 # (local)

# ============================================================
# SECTION 4: Comparison with S78 W1-E observed S_IC
# ============================================================
print("\n[SEC 4] Comparison vs S78 W1-E observed S_IC(k_pivot_fold)")
print(f"  S78 W1-E S_IC (SS principle)     = {S_IC_W1E_SS:.3e}")
print(f"  S78 W1-E S_IC (ME principle)     = {S_IC_W1E_ME:.3e}")
print(f"  S78 W1-E S_IC (AZ principle)     = {S_IC_W1E_AZ:.3e}")
print(f"  Central (SS) used for comparison = {S_IC_W1E_observed:.3e}")

ratio_primary    = S_IC_cap_primary / S_IC_W1E_observed            # (local)
log10_ratio_primary = np.log10(ratio_primary)                      # (local)
abs_log_primary  = abs(log10_ratio_primary)                        # (local)

print(f"\n  Primary (R-SF at B3):")
print(f"    ratio (cap/obs)  = {ratio_primary:.4f}")
print(f"    log10 ratio      = {log10_ratio_primary:+.4f}")
print(f"    |log10 ratio|    = {abs_log_primary:.4f}")

# All 6 (reading x band) comparisons for transparency
print("\n  Full grid (reading x band):")
all_results = []                                                   # (local)
for label, S_cap in [('R-WD-B2', S_WD_B2), ('R-WD-B1', S_WD_B1), ('R-WD-B3', S_WD_B3),
                      ('R-SF-B2', S_SF_B2), ('R-SF-B1', S_SF_B1), ('R-SF-B3', S_SF_B3)]:
    r = S_cap / S_IC_W1E_observed                                  # (local)
    lr = np.log10(r)                                               # (local)
    alr = abs(lr)                                                  # (local)
    if alr < 1.0:
        band_verdict = 'PASS'
    elif alr < 2.0:
        band_verdict = 'INFO'
    else:
        band_verdict = 'FAIL'
    all_results.append(dict(label=label, S_cap=S_cap, ratio=r,
                            log10_ratio=lr, abs_log=alr, verdict=band_verdict))
    print(f"    [{label}] cap={S_cap:.3e}, ratio={r:.3e}, log10={lr:+.3f} -> {band_verdict}")

# ============================================================
# SECTION 5: Pre-registered verdict (primary reading)
# ============================================================
print("\n[SEC 5] Pre-registered verdict (primary = R-SF at B3)")

GATE_PASS_LOG  = 1.0              # (local) S80 plan PASS: cap within factor-10
GATE_INFO_LOG  = 2.0              # (local) S80 plan INFO: factor-10 to factor-100

if abs_log_primary < GATE_PASS_LOG:
    primary_verdict = 'PASS'
elif abs_log_primary < GATE_INFO_LOG:
    primary_verdict = 'INFO'
else:
    primary_verdict = 'FAIL'

print(f"  PASS: |log10 ratio| < {GATE_PASS_LOG} (factor-10)")
print(f"  INFO: {GATE_PASS_LOG} <= |log10 ratio| < {GATE_INFO_LOG} (factor-100)")
print(f"  FAIL: |log10 ratio| >= {GATE_INFO_LOG}")
print(f"  VERDICT: {primary_verdict}  (|log10| = {abs_log_primary:.4f})")

# ============================================================
# SECTION 6: Cross-checks (machine-precision identities)
# ============================================================
print("\n[SEC 6] Cross-checks")

# CC1: cap positivity (S_IC >= 1 for all bands, both readings)
CC1 = all(S >= 1.0 for S in [S_WD_B2, S_WD_B1, S_WD_B3,
                              S_SF_B2, S_SF_B1, S_SF_B3])
print(f"  CC1 (cap positivity: all S_IC^cap >= 1): {CC1}")

# CC2: R-SF > R-WD pointwise (S_fold >> |dS|*dt)
CC2 = (S_SF_B3 > S_WD_B3) and (S_SF_B1 > S_WD_B1) and (S_SF_B2 > S_WD_B2)
print(f"  CC2 (R-SF > R-WD at every band): {CC2}")

# CC3: omega monotonicity implies cap monotonicity within each reading
CC3 = struct_check_WD and struct_check_SF
print(f"  CC3 (cap monotone-decreasing in omega): {CC3}")

# CC4: W2-4 K_substrate (2.035) has n_k O(1) << n_k^cap(B3) (SF reading ~ 1.7e5)
# Hence W2-4 GGE IC is WELL WITHIN the physical cap (consistency check)
n_W24_R3 = (2.0353 - 1.0) / 2.0                                   # (local)
W24_inside_cap = n_W24_R3 < n_SF_B3                                # (local)
print(f"  CC4 (W2-4 n_k={n_W24_R3:.3e} well below cap n_SF_B3={n_SF_B3:.3e}): {W24_inside_cap}")

# CC5: S78 W1-E n_k relative to cap  — is W1-E compatible with conservation?
# W1-E S_IC = 1.636e5 => n_k_W1E = (S_IC - 1)/2 ~ 8.18e4
n_W1E = (S_IC_W1E_observed - 1.0) / 2.0                            # (local)
W1E_inside_SF_cap = n_W1E < n_SF_B3                                # (local)
W1E_inside_WD_cap = n_W1E < n_WD_B3                                # (local)
print(f"  CC5a (S78 W1-E n_k={n_W1E:.3e} within R-SF cap n_SF_B3={n_SF_B3:.3e}): "
      f"{W1E_inside_SF_cap}")
print(f"  CC5b (S78 W1-E n_k={n_W1E:.3e} within R-WD cap n_WD_B3={n_WD_B3:.3e}): "
      f"{W1E_inside_WD_cap}")

# CC6: equipartition energy identity
E_check_SF = sum(mult * omega * n for mult, omega, n in
                  [(mult_B2, omega_B2, n_SF_B2),
                   (mult_B1, omega_B1, n_SF_B1),
                   (mult_B3, omega_B3, n_SF_B3)])                  # (local)
# Each band: mult * omega * n_cap = mult * omega * E_budget / (N_modes * omega) = mult * E/N
# Sum = E_budget * (sum mult) / N_modes = E_budget (since sum mult = N_modes)
# So E_check_SF should equal E_budget_SF exactly
CC6 = abs(E_check_SF - E_budget_SF) / E_budget_SF < 1e-12          # (local)
print(f"  CC6 (equipartition closure: sum omega_b*n_b_cap*mult_b = E_budget): {CC6}")
print(f"    E_check = {E_check_SF:.6e}, E_budget = {E_budget_SF:.6e}, "
      f"rel_dev = {abs(E_check_SF - E_budget_SF)/E_budget_SF:.2e}")

cross_checks_ok = CC1 and CC2 and CC3 and W24_inside_cap and CC6   # (local)
print(f"  ALL critical cross-checks pass: {cross_checks_ok}")

# ============================================================
# SECTION 7: Build closure SHA-256
# ============================================================
print("\n[SEC 7] Closure SHA-256")

closure_map = {
    'input_shas': INPUT_SHAS,
    'E_budget_WD': E_budget_WD,
    'E_budget_SF': E_budget_SF,
    'omega': {'B2': omega_B2, 'B1': omega_B1, 'B3': omega_B3},
    'mult': {'B2': mult_B2, 'B1': mult_B1, 'B3': mult_B3},
    'N_modes_total': N_modes_total,
    'n_cap_WD': {'B2': n_WD_B2, 'B1': n_WD_B1, 'B3': n_WD_B3},
    'n_cap_SF': {'B2': n_SF_B2, 'B1': n_SF_B1, 'B3': n_SF_B3},
    'S_IC_cap_WD': {'B2': S_WD_B2, 'B1': S_WD_B1, 'B3': S_WD_B3},
    'S_IC_cap_SF': {'B2': S_SF_B2, 'B1': S_SF_B1, 'B3': S_SF_B3},
    'S_IC_cap_primary': S_IC_cap_primary,
    'S_IC_W1E_observed': S_IC_W1E_observed,
    'S_IC_W1E_SS': S_IC_W1E_SS,
    'S_IC_W1E_ME': S_IC_W1E_ME,
    'S_IC_W1E_AZ': S_IC_W1E_AZ,
    'ratio_primary': ratio_primary,
    'log10_ratio_primary': log10_ratio_primary,
    'abs_log_primary': abs_log_primary,
    'primary_verdict': primary_verdict,
    'thresholds': {'PASS': GATE_PASS_LOG, 'INFO': GATE_INFO_LOG},
}                                                                  # (local)
closure_json = json.dumps(closure_map, sort_keys=True, default=float)  # (local)
closure_sha = hashlib.sha256(closure_json.encode('utf-8')).hexdigest()  # (local)
print(f"  closure_sha = {closure_sha}")

# ============================================================
# SECTION 8: 4-tuple tag + verdict line
# ============================================================
print("\n[SEC 8] 4-tuple tag + verdict line")

four_tuple = (f"(value={S_IC_cap_primary:.4e}, "
              f"scheme=ENERGY-CONSERVATION-EQUIPARTITION, "
              f"convention=R-SF-B3-SOFTEST-PIVOT, "
              f"L_max=GGE-BAND-MULT-3-3-2)")                      # (local)
print(f"  4-tuple: {four_tuple}")

verdict_line = (f"S82-SIC-PHYSICAL-CAP: {primary_verdict} "
                f"-- value={S_IC_cap_primary:.4e} "
                f"scheme=ENERGY-CONSERVATION-EQUIPARTITION "
                f"convention=R-SF-B3-SOFTEST-PIVOT "
                f"L_max=GGE-BAND-MULT-3-3-2 sha256={closure_sha}")  # (local)
print(f"\n[VERDICT LINE] {verdict_line}")

# ============================================================
# SECTION 9: Save NPZ + plot
# ============================================================
print("\n[SEC 9] Save outputs")

npz_path = os.path.join(HERE, 's82_w3_6_sic_physical_cap.npz')     # (local)
np.savez(npz_path,
         # Energy budgets
         E_budget_WD=E_budget_WD,
         E_budget_SF=E_budget_SF,
         # Frequencies
         omega_B2=omega_B2, omega_B1=omega_B1, omega_B3=omega_B3,
         # Multiplicities
         mult_B2=mult_B2, mult_B1=mult_B1, mult_B3=mult_B3,
         N_modes_total=N_modes_total,
         # Per-band occupation caps
         n_WD_B2=n_WD_B2, n_WD_B1=n_WD_B1, n_WD_B3=n_WD_B3,
         n_SF_B2=n_SF_B2, n_SF_B1=n_SF_B1, n_SF_B3=n_SF_B3,
         # Per-band S_IC caps
         S_WD_B2=S_WD_B2, S_WD_B1=S_WD_B1, S_WD_B3=S_WD_B3,
         S_SF_B2=S_SF_B2, S_SF_B1=S_SF_B1, S_SF_B3=S_SF_B3,
         # Primary verdict
         S_IC_cap_primary=S_IC_cap_primary,
         S_IC_W1E_observed=S_IC_W1E_observed,
         S_IC_W1E_SS=S_IC_W1E_SS,
         S_IC_W1E_ME=S_IC_W1E_ME,
         S_IC_W1E_AZ=S_IC_W1E_AZ,
         ratio_primary=ratio_primary,
         log10_ratio_primary=log10_ratio_primary,
         abs_log_primary=abs_log_primary,
         primary_verdict=primary_verdict,
         GATE_PASS_LOG=GATE_PASS_LOG,
         GATE_INFO_LOG=GATE_INFO_LOG,
         four_tuple=four_tuple,
         verdict_line=verdict_line,
         closure_sha=closure_sha,
         input_shas=np.array([f"{k}={v}" for k, v in INPUT_SHAS.items()]),
         # Cross-check flags
         CC1=CC1, CC2=CC2, CC3=CC3, CC6=CC6,
         W24_inside_cap=W24_inside_cap,
         W1E_inside_SF_cap=W1E_inside_SF_cap,
         W1E_inside_WD_cap=W1E_inside_WD_cap,
         n_W24_R3=n_W24_R3,
         n_W1E=n_W1E,
         # Full grid
         grid_labels=np.array([r['label'] for r in all_results]),
         grid_S_cap=np.array([r['S_cap'] for r in all_results]),
         grid_ratio=np.array([r['ratio'] for r in all_results]),
         grid_log10=np.array([r['log10_ratio'] for r in all_results]),
         grid_verdict=np.array([r['verdict'] for r in all_results]),
         )
print(f"  NPZ saved: {npz_path}")

# Plot: log-scale comparison of per-band caps to S78 W1-E observation
fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))                  # (local)

ax0 = axes[0]
bands = ['B2 (0.7704)', 'B1 (0.4643)', 'B3 (0.176)']               # (local)
x_pos = np.arange(len(bands))                                      # (local)
w = 0.35                                                           # (local)
WD_vals = [S_WD_B2, S_WD_B1, S_WD_B3]                              # (local)
SF_vals = [S_SF_B2, S_SF_B1, S_SF_B3]                              # (local)
ax0.bar(x_pos - w/2, WD_vals, w, label='R-WD (|dS|*dt)',
        color='steelblue', alpha=0.85)
ax0.bar(x_pos + w/2, SF_vals, w, label='R-SF (S_fold)',
        color='darkred', alpha=0.85)
ax0.axhline(S_IC_W1E_observed, color='black', ls='--',
            label=f'S78 W1-E S_IC = {S_IC_W1E_observed:.2e}')
ax0.axhline(1.0, color='gray', ls=':', alpha=0.5, label='BD vacuum (S_IC=1)')
ax0.set_xticks(x_pos); ax0.set_xticklabels(bands)
ax0.set_ylabel('S_IC^cap  (log scale)')
ax0.set_yscale('log')
ax0.set_title(f'Physical cap on S_IC (per band, per reading)\n'
              f'Primary verdict: {primary_verdict} '
              f'(|log10 ratio| = {abs_log_primary:.3f})')
ax0.legend(loc='best', fontsize=9)
ax0.grid(True, alpha=0.3)

ax1 = axes[1]
r_labels = [r['label'] for r in all_results]                       # (local)
r_log10 = [r['log10_ratio'] for r in all_results]                  # (local)
colors_r = ['steelblue' if r['verdict'] == 'PASS' else
            'orange' if r['verdict'] == 'INFO' else 'darkred'
            for r in all_results]                                  # (local)
ax1.bar(r_labels, r_log10, color=colors_r, alpha=0.85)
ax1.axhline(0.0, color='black', ls='-', label='match (log10=0)')
ax1.axhline(+GATE_PASS_LOG, color='green', ls='--',
            label=f'PASS boundary (+/-{GATE_PASS_LOG})')
ax1.axhline(-GATE_PASS_LOG, color='green', ls='--')
ax1.axhline(+GATE_INFO_LOG, color='red', ls=':',
            label=f'INFO/FAIL boundary (+/-{GATE_INFO_LOG})')
ax1.axhline(-GATE_INFO_LOG, color='red', ls=':')
ax1.set_ylabel('log10 (S_IC^cap / S_IC_W1E_obs)')
ax1.set_title('Cap-to-observed ratio across reading x band grid')
ax1.legend(loc='best', fontsize=9)
ax1.grid(True, alpha=0.3)
plt.setp(ax1.xaxis.get_majorticklabels(), rotation=30, ha='right')

plt.tight_layout()
plot_path = os.path.join(HERE, 's82_w3_6_sic_physical_cap.png')    # (local)
plt.savefig(plot_path, dpi=150)
plt.close()
print(f"  Plot saved: {plot_path}")

# ============================================================
# SECTION 10: Append verdict line to s82_gate_verdicts.txt
# ============================================================
verdict_path = os.path.join(HERE, 's82_gate_verdicts.txt')         # (local)
with open(verdict_path, 'a', encoding='utf-8') as fh:
    fh.write(verdict_line + '\n')
print(f"\n[SEC 10] Appended verdict to: {verdict_path}")

# ============================================================
# Final summary
# ============================================================
print("\n" + "=" * 70)
print("S82 W3-6 SUMMARY")
print("=" * 70)
print(f"Primary reading: R-SF (condensation-energy) at B3 (softest/CMB pivot)")
print(f"  Energy budget E_SF   = {E_budget_SF:.3e}  (S_fold)")
print(f"  omega_B3             = {omega_B3:.4f} M_KK")
print(f"  N_modes_total        = {N_modes_total}")
print(f"  n_k^cap              = {n_SF_B3:.3e}")
print(f"  S_IC^cap             = {S_IC_cap_primary:.4e}")
print(f"  S78 W1-E observed    = {S_IC_W1E_observed:.3e}")
print(f"  ratio (cap/obs)      = {ratio_primary:.3f}")
print(f"  |log10 ratio|        = {abs_log_primary:.4f}")
print(f"  VERDICT              = {primary_verdict}")
print(f"  4-tuple              = {four_tuple}")
print(f"  closure_sha          = {closure_sha}")
print("=" * 70)
