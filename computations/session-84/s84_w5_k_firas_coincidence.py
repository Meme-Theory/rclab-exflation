#!/usr/bin/env python3
"""
S84 W5-65: GATE-K-FIRAS-COINCIDENCE
=====================================================================
Does K_FIRAS := 2.035 * mu_FIRAS / mu(K=2.035) equal S_IC^cap = 3.556e5
as a structural identity, or is the L_max=5 coincidence at 3.43%
a numerical coincidence that fails to tighten under L_max scan?

Gate: S84-W5-65  [VERIFY-THEOREM] [AUDIT]
Classification: PHONONIC (structural vs coincidence test)
Owner: volovik-superfluid-universe-theorist
Pre-reg anchor: sessions/session-plan/session-84-plan-w5.md §W5-65

Phononic framing:
  K_FIRAS and S_IC^cap are two independently motivated scales in the
  K-corridor.  K_FIRAS is set by: (i) the CMB mu-distortion FIRAS bound,
  (ii) the framework-predicted mu(K=2.035), (iii) linear K-dependence of
  mu(K) (gamma=1 exact under S82 W2-4 matched-IC).  S_IC^cap is set by
  energy conservation at the fold: total Parker-mode energy divided by
  N_modes * omega_soft gives the B3 saturation cap.

  If these land at 3.68e5 vs 3.56e5 (3.43% residual at L_max=5), two
  alternatives are possible:
    (a) STRUCTURAL IDENTITY: residual is a truncation signature that
        monotonically shrinks as L_max: 5 -> 7 -> 9.  A closed-form
        identity K_FIRAS = S_IC^cap would follow as a new Volovik-style
        vacuum-energy/saturation-cap correspondence.
    (b) NUMERICAL COINCIDENCE: residual stays flat ~3% across L_max,
        reflecting the fact that K_FIRAS and S_IC^cap share only the
        K-scale parameter and are otherwise derivatively uncoupled.
        Two independently-motivated O(1e5) quantities happen to agree
        at 2 sig figs.

PRE-REGISTERED THRESHOLDS (plan §W5-65):
  PASS (structural):
    |K_FIRAS - S_IC^cap| / S_IC^cap <= 0.01 at L_max=5
    AND drift <= 0.5% per L-step (L=5 -> L=7 -> L=9)
  FAIL (not coincident):
    |K_FIRAS - S_IC^cap| / S_IC^cap >= 0.10 at L_max=5
  INFO (coincidence, not structural):
    Residual at L_max=5 in (0.01, 0.10) but drift > 5% under scan,
    OR residual flat across L_max (drift < 0.5%) but above 1% band.

SUBSTITUTION CHAIN (MANDATORY, [AUDIT]):

  Step 1 (definitions):
    mu_FIRAS := 9.0e-5              (Fixsen+ 1996 FIRAS 95% CL bound)
    mu(K=2.035, L=5) := 4.9758503926e-10   (from S84 W5-57 MU-K-CORRIDOR PASS)
    K_FIRAS(L) := K_base * mu_FIRAS / mu(K_base, L)     (inversion relation)
    S_IC^cap(L) := 1 + 2 * E_budget(L) / (N_modes * omega_soft)   (S82 W3-6)
      E_budget = S_fold (condensation energy, R-SF reading, L-pinned at S42)
      omega_soft = Delta_B3 (softest-band B3 gap, L-independent BDI-protected)
      N_modes = 8 (3 + 3 + 2 = mult_B2 + mult_B1 + mult_B3)
    residual(L) := |K_FIRAS(L) - S_IC^cap(L)| / S_IC^cap(L)
    drift(L_a, L_b) := |residual(L_b) - residual(L_a)|

  Step 2 (substitution - L_max dependence source):
    S_IC^cap(L): S_fold, Delta_B3, multiplicities are ALL L-pinned canonical
       constants from S42 (S_fold = 250360.68, Delta_B3 = 0.176,
       mult_{B2,B1,B3} = 3,3,2).  Per plan §W5-65 note ("If S79 UV-extrap
       is L-invariant by construction, say so and use the same value for
       all L"), S_IC^cap is L-invariant: S_IC^cap(L) = 3.556e5 for all L.
    mu(K=2.035, L): Plan directive says "the L-dependence comes from the
       mu side via the Chluba kernel acting on the L-truncated spectrum".
       Two pre-registered interpretations:

       Interp A (primary, plan default - "UV-extrapolated L-invariant"):
         mu envelope S_IC_0_base = 1.636e5 is UV-extrapolated and
         L-independent by construction (S79 P2-B C1 fit).  Chluba integrand
         is dominated by the envelope shape in the physical k-window
         k in [46, 1e4] Mpc^-1, which does not couple to the substrate
         spectrum truncation.
           mu(K=2.035, L) = mu_L5 = 4.9758503926e-10 for all L.

       Interp B (diagnostic - "Zubarev-energy-weighted mode sum"):
         mu amplitude is proportional to the Zubarev energy-weighted
         spectral sum S_Zubarev_E(L) = sum_n d_n exp(-lambda_n^2) * lambda_n
         (R-Zubarev scheme, energy-weighted).  Under this ansatz:
           mu(K=2.035, L) = mu_L5 * S_Zubarev_E(L) / S_Zubarev_E(L=5).
         This tests sensitivity to the spectral-sum interpretation of mu.

  Step 3 (canonical form):
    Under Interp A:
      ratio_A(L) = K_FIRAS(L=5) / S_IC^cap = 3.6808e5 / 3.556e5 = 1.0351
      residual_A(L) = 3.43% for all L. drift_A = 0% (structurally zero).
    Under Interp B:
      ratio_B(L) = (K_base * mu_FIRAS / mu_L5) / (S_Zubarev_E(L)/S_Zubarev_E(5))
                 / S_IC^cap, i.e., ratio_B(L) = ratio_B(L=5) *
                 S_Zubarev_E(5)/S_Zubarev_E(L).
      (UV modes increase S_Zubarev_E(L), driving ratio_B(L) DOWN and
       residual_B UP as L grows.)

  Step 4 (direction, PASS/INFO/FAIL classification):
    PASS iff residual(L=5) <= 0.01 AND |drift(L=5,L=9)| <= 0.005.
    FAIL iff residual(L=5) >= 0.10, or drift(L=5,L=9) grows past 5%.
    INFO otherwise.

    PRIMARY (Interp A):
      residual(L=5) = 3.43% -> outside PASS band (>1%), below FAIL (<10%).
      drift = 0 (by construction L-invariance).
      CLASSIFICATION: INFO (coincidence, L-stable but residual > 1%).

    DIAGNOSTIC (Interp B):
      residual(L=5) = 3.43%; residual(L=9) ~ 39.5% per Zubarev mode-sum.
      CLASSIFICATION under B: FAIL (residual grows past 10%).

    COMBINED VERDICT: The PRIMARY interpretation (A) governs the gate per
    plan directive; B is reported as diagnostic sensitivity.
    Final verdict depends on whether the 3.43% residual at L_max=5 is a
    structural truncation signature (would require Interp B-type drift
    that SHRINKS with L, which does not happen here under either Interp)
    or a pure numerical coincidence at 2 sig figs.

References:
  - plan: sessions/session-plan/session-84-plan-w5.md §W5-65 L761-822
  - S82 W3-6 SIC-PHYSICAL-CAP: s82_w3_6_sic_physical_cap.py (S_IC^cap derivation)
  - S82 W2-14 FIRAS-CHLUBA-FULL: s82_w2_14_firas_chluba_full.py (mu baseline)
  - S84 W5-57 MU-K-CORRIDOR: s84_w5_mu_k_corridor.py (mu@K=2.035 to 6 sig fig)
  - S84 W4-G51 LMAX-CONVERGENCE: s84_w4_g51_lmax_convergence.py (L=5,7,9 spectral sums)
  - S83 W3-G51: S_zeta(5) = 159936; baseline spectral counts
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

import torch

HERE = os.path.dirname(os.path.abspath(__file__))                    # (local)
sys.path.insert(0, HERE)

# Canonical constants (MANDATORY)
from canonical_constants import (
    S_fold,            # 250360.68  fold condensation energy (S42, L-pinned)
    Delta_B3,          # 0.176      softest band gap (BDI-protected, L-invariant)
    Delta_0_GL,        # 0.7704     B2 gap
    Delta_0_OES,       # 0.4643     B1 gap
)

# ============================================================
# SECTION 0: Input SHA-256 pins (MANDATORY in first 20 lines)
# ============================================================


def _sha256(path):
    if not os.path.exists(path):
        return 'MISSING'
    with open(path, 'rb') as h:
        return hashlib.sha256(h.read()).hexdigest()


INPUT_FILES = [                                                      # (local)
    os.path.join(HERE, 'canonical_constants.py'),
    os.path.join(HERE, 's82_w3_6_sic_physical_cap.py'),
    os.path.join(HERE, 's82_w2_14_firas_chluba_full.py'),
    os.path.join(HERE, 's82_w2_4_ps_substrate_matched_ic.py'),
    os.path.join(HERE, 's84_w5_mu_k_corridor.py'),
    os.path.join(HERE, 's74_spectrum_cache_L9_tau019.npz'),
]

print("=" * 76)
print("S84 W5-65: GATE-K-FIRAS-COINCIDENCE  (structural vs numerical coincidence)")
print("=" * 76)
print("\n[SEC 0] Input SHA-256 pins")
INPUT_SHAS = {}                                                      # (local)
for _f in INPUT_FILES:
    _h = _sha256(_f)                                                 # (local)
    INPUT_SHAS[os.path.basename(_f)] = _h
    _tag = (_h[:16] + '...' + _h[-8:]) if _h != 'MISSING' else 'MISSING'
    print(f"  {os.path.basename(_f):46s} sha256={_tag}")

print("\n[SEC 0.1] GPU backend check")
_gpu_available = torch.cuda.is_available()                           # (local)
_device = 'cuda' if _gpu_available else 'cpu'                        # (local)
print(f"  torch.cuda.is_available() = {_gpu_available}")
print(f"  torch version             = {torch.__version__}")
print(f"  device                    = {_device}")

# ============================================================
# SECTION 1: Anchors from sub-wave-A (pre-registered constants)
# ============================================================
print("\n[SEC 1] Anchors from plan §W5-65 + sub-wave-A")

K_base = 2.035                                                       # (local) R3 band-weighted K, S82 W2-4
mu_FIRAS = 9.0e-5                                                    # (local) Fixsen+ 1996 FIRAS bound
mu_base_L5 = 4.9758503926e-10                                        # (local) from S84 W5-57 MU-K-CORRIDOR mu(K_base)

# S_IC^cap from S82 W3-6 (R-SF at B3, CMB-pivot softest band)
N_modes_total = 3 + 3 + 2                                            # (local) mult_B2+mult_B1+mult_B3 = 8
omega_soft = float(Delta_B3)                                         # (local) 0.176 M_KK
E_budget_SF = float(S_fold)                                          # (local) 250360.68
n_cap_B3 = E_budget_SF / (N_modes_total * omega_soft)                # (local)
S_IC_cap_canonical = 1.0 + 2.0 * n_cap_B3                            # (local) ~3.556e5

print(f"  K_base              = {K_base:.6f}  (R3 band-weighted squeezing anchor)")
print(f"  mu_FIRAS            = {mu_FIRAS:.3e}  (Fixsen+ 1996)")
print(f"  mu(K=2.035, L=5)    = {mu_base_L5:.10e}  (S84 W5-57)")
print(f"  S_fold (L-pinned)   = {E_budget_SF:.4f}  (S42 canonical)")
print(f"  Delta_B3            = {omega_soft:.4f}  M_KK  (BDI-protected)")
print(f"  N_modes_total       = {N_modes_total}  (= 3+3+2)")
print(f"  n_cap_B3            = {n_cap_B3:.4e}")
print(f"  S_IC^cap (canon)    = {S_IC_cap_canonical:.4e}")
print(f"  plan anchor         = 3.556e5")

# Consistency check vs plan anchor
_cap_err = abs(S_IC_cap_canonical - 3.556e5) / 3.556e5               # (local)
print(f"  rel err vs plan     = {_cap_err:.4e}   (should be <1e-3)")
assert _cap_err < 1e-3, "S_IC^cap drift vs plan anchor >0.1%"

# ============================================================
# SECTION 2: Load L=9 spectrum cache and compute spectral sums at
# L_max in {5, 7, 9}. These drive Interp-B (diagnostic).
# ============================================================
print("\n[SEC 2] Load L=9 spectrum cache; compute Zubarev energy-weighted sums")

cache_path = os.path.join(HERE, 's74_spectrum_cache_L9_tau019.npz')  # (local)
cache = np.load(cache_path, allow_pickle=True)                       # (local)
sec = cache['sector_evals'].item()                                   # (local)
print(f"  cache sectors loaded    : {len(sec)}  (p+q <= 9)")


def flatten_L(sector_dict, Lmax):
    """Flatten per-sector abs_evals into (flat_lams, flat_mults) for p+q <= Lmax."""
    lam_list = []                                                    # (local)
    mult_list = []                                                   # (local)
    n_sectors = 0                                                    # (local)
    for (p, q), rec in sector_dict.items():
        if (p + q) > Lmax:
            continue
        n_sectors += 1
        d_pq = (p + 1) * (q + 1) * (p + q + 2) // 2                  # (local) SU(3) irrep dim
        ae = np.asarray(rec['abs_evals'], dtype=np.float64)
        lam_list.append(ae)
        mult_list.append(np.full(len(ae), d_pq, dtype=np.float64))
    flat_lam = np.concatenate(lam_list)                              # (local)
    flat_mult = np.concatenate(mult_list)                            # (local)
    return flat_lam, flat_mult, n_sectors


L_max_grid = [5, 7, 9]                                               # (local)
spec_by_L = {}                                                       # (local)

for Lmax in L_max_grid:
    flat_lam, flat_mult, n_sec = flatten_L(sec, Lmax)

    # GPU path (torch.linalg-class sums; ship arrays to device)
    lam_t = torch.tensor(flat_lam, dtype=torch.float64, device=_device)     # (local)
    mult_t = torch.tensor(flat_mult, dtype=torch.float64, device=_device)   # (local)
    w_zeta_t = torch.ones_like(lam_t)                                # (local)
    w_zubarev_t = torch.exp(-lam_t ** 2)                             # (local) Lambda_Z = 1 M_KK

    S_zeta = (mult_t * w_zeta_t).sum().item()                        # (local)
    S_Zubarev = (mult_t * w_zubarev_t).sum().item()                  # (local)
    S_zeta_E = (mult_t * w_zeta_t * lam_t).sum().item()              # (local)
    S_Zubarev_E = (mult_t * w_zubarev_t * lam_t).sum().item()        # (local)

    # CPU cross-check on a small slice (first 50 modes)
    S_zub_E_cpu_test = float(np.sum(flat_mult[:50] *
                                    np.exp(-flat_lam[:50]**2) *
                                    flat_lam[:50]))                  # (local)
    S_zub_E_gpu_test = (mult_t[:50] * torch.exp(-lam_t[:50]**2) *
                         lam_t[:50]).sum().item()                    # (local)
    _gpu_cpu_err = abs(S_zub_E_cpu_test - S_zub_E_gpu_test)          # (local)

    spec_by_L[Lmax] = dict(
        n_sectors=n_sec,
        n_modes=len(flat_lam),
        S_zeta=S_zeta,
        S_Zubarev=S_Zubarev,
        S_zeta_E=S_zeta_E,
        S_Zubarev_E=S_Zubarev_E,
    )
    print(f"  L_max={Lmax}: sectors={n_sec:2d}  n_modes={len(flat_lam):5d}  "
          f"S_zeta={S_zeta:.3f}  S_Zubarev={S_Zubarev:.3f}")
    print(f"           S_zeta_E={S_zeta_E:.3f}  S_Zubarev_E={S_Zubarev_E:.3f}  "
          f"GPU-CPU err={_gpu_cpu_err:.2e}")

# Cross-check vs S83 W3-G51 baseline at L=5
_S_zeta_L5_ref = 159936.0                                            # (local) S83 W3-G51
_S_Zubarev_L5_ref = 3805.668                                         # (local) S83 W3-G51
_err_Szeta_L5 = abs(spec_by_L[5]['S_zeta'] - _S_zeta_L5_ref)         # (local)
_err_SZub_L5 = abs(spec_by_L[5]['S_Zubarev'] - _S_Zubarev_L5_ref)    # (local)
print(f"\n  [VERIFY] L=5 matches S83 W3-G51:")
print(f"    S_zeta    L=5 err = {_err_Szeta_L5:.6e} (ref {_S_zeta_L5_ref})")
print(f"    S_Zubarev L=5 err = {_err_SZub_L5:.6e} (ref {_S_Zubarev_L5_ref})")
assert _err_Szeta_L5 < 1e-3, "L=5 S_zeta mismatch vs S83 W3-G51"
assert _err_SZub_L5 < 1e-2, "L=5 S_Zubarev mismatch vs S83 W3-G51"

# ============================================================
# SECTION 3: Compute mu(K=2.035, L), K_FIRAS(L), S_IC^cap(L), and
# residual(L) under two interpretations (primary A, diagnostic B)
# ============================================================
print("\n[SEC 3] Compute K_FIRAS(L), S_IC^cap(L), residual(L) under Interps A and B")

# S_IC^cap(L): Per plan directive, L-invariant canonical pin.
# Document the pin source: S_fold and Delta_B3 are S42-pinned,
# mult 3/3/2 is S43 gge-temp-43 result; all predate L_max scan.
S_IC_cap_by_L = {L: S_IC_cap_canonical for L in L_max_grid}          # (local)

# Interp A: mu(K=2.035, L) = mu_base_L5 for all L (UV-extrapolated envelope L-invariant)
mu_by_L_A = {L: mu_base_L5 for L in L_max_grid}                      # (local)

# Interp B (diagnostic): mu(K=2.035, L) rescaled by S_Zubarev_E(L)/S_Zubarev_E(5)
S_Zub_E_L5 = spec_by_L[5]['S_Zubarev_E']                             # (local)
mu_by_L_B = {                                                        # (local)
    L: mu_base_L5 * spec_by_L[L]['S_Zubarev_E'] / S_Zub_E_L5
    for L in L_max_grid
}

# K_FIRAS(L) = K_base * mu_FIRAS / mu(K_base, L)
K_FIRAS_A = {L: K_base * mu_FIRAS / mu_by_L_A[L] for L in L_max_grid}  # (local)
K_FIRAS_B = {L: K_base * mu_FIRAS / mu_by_L_B[L] for L in L_max_grid}  # (local)

# residual(L) = |K_FIRAS(L) - S_IC^cap(L)| / S_IC^cap(L)
resid_A = {L: abs(K_FIRAS_A[L] - S_IC_cap_by_L[L]) / S_IC_cap_by_L[L]
           for L in L_max_grid}                                      # (local)
resid_B = {L: abs(K_FIRAS_B[L] - S_IC_cap_by_L[L]) / S_IC_cap_by_L[L]
           for L in L_max_grid}                                      # (local)

# ratio(L) = K_FIRAS(L) / S_IC^cap(L)
ratio_A = {L: K_FIRAS_A[L] / S_IC_cap_by_L[L] for L in L_max_grid}   # (local)
ratio_B = {L: K_FIRAS_B[L] / S_IC_cap_by_L[L] for L in L_max_grid}   # (local)

print("\n  --- Interp A (primary, plan-default UV-extrapolated L-invariant) ---")
print("   L      mu(K,L)            K_FIRAS(L)        S_IC^cap(L)   ratio   residual")
for L in L_max_grid:
    print(f"   {L}  {mu_by_L_A[L]:.6e}   {K_FIRAS_A[L]:.4e}   "
          f"{S_IC_cap_by_L[L]:.4e}   {ratio_A[L]:.4f}  {resid_A[L]:.4%}")

print("\n  --- Interp B (diagnostic, Zubarev-energy-weighted mu rescaling) ---")
print("   L      mu(K,L)            K_FIRAS(L)        S_IC^cap(L)   ratio   residual")
for L in L_max_grid:
    print(f"   {L}  {mu_by_L_B[L]:.6e}   {K_FIRAS_B[L]:.4e}   "
          f"{S_IC_cap_by_L[L]:.4e}   {ratio_B[L]:.4f}  {resid_B[L]:.4%}")

# Drift: |residual(L_a) - residual(L_b)|
drift_A_5_7 = abs(resid_A[7] - resid_A[5])                           # (local)
drift_A_7_9 = abs(resid_A[9] - resid_A[7])                           # (local)
drift_A_5_9 = abs(resid_A[9] - resid_A[5])                           # (local)
drift_B_5_7 = abs(resid_B[7] - resid_B[5])                           # (local)
drift_B_7_9 = abs(resid_B[9] - resid_B[7])                           # (local)
drift_B_5_9 = abs(resid_B[9] - resid_B[5])                           # (local)

print("\n  Drift summary:")
print(f"    Interp A: drift(5->7)={drift_A_5_7:.4%}  drift(7->9)={drift_A_7_9:.4%}  "
      f"drift(5->9)={drift_A_5_9:.4%}")
print(f"    Interp B: drift(5->7)={drift_B_5_7:.4%}  drift(7->9)={drift_B_7_9:.4%}  "
      f"drift(5->9)={drift_B_5_9:.4%}")

# ============================================================
# SECTION 4: Verdict evaluation per plan §W5-65 thresholds
# ============================================================
print("\n[SEC 4] Verdict evaluation (PASS / FAIL / INFO)")

# Primary is Interp A (per plan note "use the same value for all L").
resid_L5 = resid_A[5]                                                # (local)
resid_L9 = resid_A[9]                                                # (local)
drift_5_9 = drift_A_5_9                                              # (local)

# Thresholds (plan §W5-65):
PASS_RESID = 0.01                                                    # (local) 1%
PASS_DRIFT_PER_STEP = 0.005                                          # (local) 0.5%/L-step
FAIL_RESID = 0.10                                                    # (local) 10%
INFO_DRIFT_LIMIT = 0.05                                              # (local) 5% drift above which INFO->FAIL per plan INFO band

print(f"  Thresholds:")
print(f"    PASS: residual(L=5) <= {PASS_RESID:.2%}  AND  drift/step <= {PASS_DRIFT_PER_STEP:.2%}")
print(f"    FAIL: residual(L=5) >= {FAIL_RESID:.2%}")
print(f"    INFO: otherwise")

print(f"\n  Primary measurements (Interp A):")
print(f"    residual(L=5)    = {resid_L5:.4%}")
print(f"    residual(L=9)    = {resid_L9:.4%}")
print(f"    drift(5->9)      = {drift_5_9:.4%}")
print(f"    per-step max     = {max(drift_A_5_7, drift_A_7_9):.4%}")

pass_resid = (resid_L5 <= PASS_RESID)                                # (local)
pass_drift = (max(drift_A_5_7, drift_A_7_9) <= PASS_DRIFT_PER_STEP)  # (local)
fail_resid = (resid_L5 >= FAIL_RESID)                                # (local)

if pass_resid and pass_drift:
    verdict = "PASS"                                                 # (local)
    band = (f"structural identity: residual={resid_L5:.4%}<=1% and drift "
            f"{drift_5_9:.4%}<=0.5%/step")                           # (local)
elif fail_resid:
    verdict = "FAIL"                                                 # (local)
    band = (f"residual={resid_L5:.4%}>=10%: K_FIRAS and S_IC^cap disconnected") # (local)
else:
    verdict = "INFO"                                                 # (local)
    # Sub-classify: flat coincidence vs growing residual
    if drift_5_9 <= PASS_DRIFT_PER_STEP * 2:  # essentially flat
        band = (f"numerical coincidence (flat): residual={resid_L5:.4%} "
                f"in (1%, 10%) band; drift={drift_5_9:.4%} stable under L; "
                f"NOT structural identity")                          # (local)
    else:
        band = (f"coincidence with L-drift: residual={resid_L5:.4%} "
                f"in (1%, 10%) band, drift={drift_5_9:.4%} grows; "
                f"NOT truncation signature")                         # (local)

print(f"\n  Verdict: {verdict}  [{band}]")

# Sensitivity report (Interp B) -- diagnostic only
print(f"\n  Sensitivity (Interp B, Zubarev-mode-sum ansatz - DIAGNOSTIC ONLY):")
print(f"    residual(L=5)={resid_B[5]:.4%}, residual(L=9)={resid_B[9]:.4%}, "
      f"drift(5->9)={drift_B_5_9:.4%}")
if resid_B[9] >= FAIL_RESID:
    print(f"    Under Interp B, residual grows past 10% -> diagnostic FAIL signal.")
    print(f"    Primary verdict (A) unchanged; plan directive gives A priority.")

# ============================================================
# SECTION 5: Cross-checks
# ============================================================
print("\n[SEC 5] Cross-checks")

# CC1: K_FIRAS(L=5) reproduces plan anchor 3.678e5 to <0.1%
K_FIRAS_plan = 3.678e5                                               # (local) plan §W5-65 Step 2
CC1 = abs(K_FIRAS_A[5] - K_FIRAS_plan) / K_FIRAS_plan < 1e-3          # (local)
print(f"  CC1 K_FIRAS(L=5) matches plan 3.678e5: {CC1}  "
      f"(computed {K_FIRAS_A[5]:.4e})")

# CC2: S_IC^cap canonical matches plan 3.556e5 to <0.1%
CC2 = _cap_err < 1e-3                                                # (local)
print(f"  CC2 S_IC^cap matches plan 3.556e5: {CC2}  "
      f"(computed {S_IC_cap_canonical:.4e}, rel err {_cap_err:.2e})")

# CC3: residual(L=5) matches plan 3.43%
resid_plan = 0.03431                                                 # (local) (3.678-3.556)/3.556
CC3 = abs(resid_L5 - resid_plan) < 1e-3                              # (local)
print(f"  CC3 residual(L=5) matches plan 3.43%: {CC3}  "
      f"(computed {resid_L5:.4%})")

# CC4: L=5 spectral sum reproduces S83 W3-G51 baseline
CC4 = _err_Szeta_L5 < 1e-3                                           # (local)
print(f"  CC4 L=5 spectrum vs S83 W3-G51: {CC4}  (S_zeta err {_err_Szeta_L5:.2e})")

# CC5: Interp A L-invariance (drift identically zero)
CC5 = (drift_A_5_9 == 0.0)                                           # (local)
print(f"  CC5 Interp A drift(5->9) == 0: {CC5}  (drift {drift_A_5_9:.2e})")

# CC6: S_Zubarev_E(L) monotone increasing (spectrum adding UV modes)
CC6 = (spec_by_L[5]['S_Zubarev_E'] < spec_by_L[7]['S_Zubarev_E'] <
       spec_by_L[9]['S_Zubarev_E'])                                  # (local)
print(f"  CC6 S_Zubarev_E monotone in L: {CC6}")

# CC7: Under Interp B, residual monotone INCREASING (not shrinking)
CC7 = (resid_B[5] < resid_B[7] < resid_B[9])                         # (local)
print(f"  CC7 Interp B residual grows with L: {CC7}  "
      f"({resid_B[5]:.4%}<{resid_B[7]:.4%}<{resid_B[9]:.4%})")

cross_checks_all = CC1 and CC2 and CC3 and CC4 and CC5 and CC6 and CC7  # (local)
print(f"  ALL cross-checks pass: {cross_checks_all}")

# ============================================================
# SECTION 6: Save NPZ + plot
# ============================================================
print("\n[SEC 6] Save NPZ + plot")

npz_path = os.path.join(HERE, 's84_w5_65_data.npz')                  # (local)
np.savez(npz_path,
         # anchors
         K_base=K_base,
         mu_FIRAS=mu_FIRAS,
         mu_base_L5=mu_base_L5,
         S_fold=E_budget_SF,
         Delta_B3=omega_soft,
         N_modes_total=N_modes_total,
         S_IC_cap_canonical=S_IC_cap_canonical,
         # L-grid arrays
         L_max_grid=np.array(L_max_grid, dtype=np.int32),
         # Interp A
         mu_A=np.array([mu_by_L_A[L] for L in L_max_grid]),
         K_FIRAS_A=np.array([K_FIRAS_A[L] for L in L_max_grid]),
         S_IC_cap_A=np.array([S_IC_cap_by_L[L] for L in L_max_grid]),
         ratio_A=np.array([ratio_A[L] for L in L_max_grid]),
         resid_A=np.array([resid_A[L] for L in L_max_grid]),
         # Interp B (diagnostic)
         mu_B=np.array([mu_by_L_B[L] for L in L_max_grid]),
         K_FIRAS_B=np.array([K_FIRAS_B[L] for L in L_max_grid]),
         ratio_B=np.array([ratio_B[L] for L in L_max_grid]),
         resid_B=np.array([resid_B[L] for L in L_max_grid]),
         # Spectral sums
         S_zeta=np.array([spec_by_L[L]['S_zeta'] for L in L_max_grid]),
         S_Zubarev=np.array([spec_by_L[L]['S_Zubarev'] for L in L_max_grid]),
         S_zeta_E=np.array([spec_by_L[L]['S_zeta_E'] for L in L_max_grid]),
         S_Zubarev_E=np.array([spec_by_L[L]['S_Zubarev_E'] for L in L_max_grid]),
         n_sectors=np.array([spec_by_L[L]['n_sectors'] for L in L_max_grid]),
         n_modes=np.array([spec_by_L[L]['n_modes'] for L in L_max_grid]),
         # Drift
         drift_A_5_9=drift_A_5_9,
         drift_B_5_9=drift_B_5_9,
         # Verdict metadata
         verdict=verdict,
         scheme='Zubarev',
         convention='R3',
         )
print(f"  NPZ: {npz_path}")

# Plot: ratio vs L_max with PASS/INFO/FAIL bands
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

# Panel 1: ratio vs L_max
L_arr = np.array(L_max_grid)                                         # (local)
r_A_arr = np.array([ratio_A[L] for L in L_max_grid])                 # (local)
r_B_arr = np.array([ratio_B[L] for L in L_max_grid])                 # (local)

ax1.plot(L_arr, r_A_arr, 'o-', color='blue', ms=11, lw=2,
         label='Interp A (primary): UV-extrap L-inv')
ax1.plot(L_arr, r_B_arr, 's--', color='red', ms=9, lw=1.5, alpha=0.7,
         label='Interp B (diagnostic): Zubarev-mode-sum')

# PASS band: ratio within 1% of 1.0
ax1.axhspan(0.99, 1.01, alpha=0.2, color='green',
            label='PASS band (ratio in [0.99, 1.01])')
# INFO band: ratio within 10% of 1.0
ax1.axhspan(0.90, 1.10, alpha=0.10, color='orange',
            label='INFO band (ratio in [0.90, 1.10])')
# FAIL region (shaded light red below 0.90 and above 1.10): implicit
ax1.axhline(1.0, color='k', ls=':', alpha=0.5, label='identity ratio = 1')
ax1.axhline(0.90, color='red', ls='--', lw=0.8, alpha=0.5)
ax1.axhline(1.10, color='red', ls='--', lw=0.8, alpha=0.5)

# Annotate points
for L in L_max_grid:
    ax1.annotate(f'{ratio_A[L]:.4f}', xy=(L, ratio_A[L]),
                 xytext=(5, 10), textcoords='offset points', fontsize=9, color='blue')
    ax1.annotate(f'{ratio_B[L]:.4f}', xy=(L, ratio_B[L]),
                 xytext=(5, -14), textcoords='offset points', fontsize=9, color='red')

ax1.set_xlabel('L_max', fontsize=12)
ax1.set_ylabel(r'$K_{\mathrm{FIRAS}}(L) / S_{\mathrm{IC}}^{\mathrm{cap}}(L)$', fontsize=12)
ax1.set_title(f'W5-65 ratio vs L_max (verdict={verdict})', fontsize=11)
ax1.grid(True, alpha=0.3)
ax1.legend(fontsize=8, loc='best')
ax1.set_xticks(L_max_grid)

# Panel 2: residual vs L_max
resid_A_arr = np.array([resid_A[L] for L in L_max_grid]) * 100.0     # (local) percent
resid_B_arr = np.array([resid_B[L] for L in L_max_grid]) * 100.0     # (local) percent
ax2.plot(L_arr, resid_A_arr, 'o-', color='blue', ms=11, lw=2,
         label='Interp A (primary)')
ax2.plot(L_arr, resid_B_arr, 's--', color='red', ms=9, lw=1.5, alpha=0.7,
         label='Interp B (diagnostic)')
ax2.axhspan(0, 1.0, alpha=0.20, color='green', label='PASS band (<= 1%)')
ax2.axhspan(1.0, 10.0, alpha=0.10, color='orange', label='INFO band (1-10%)')
ax2.axhline(10.0, color='red', ls='--', lw=1.0, label='FAIL threshold (>= 10%)')
ax2.axhline(1.0, color='green', ls=':', lw=1.0, alpha=0.5)

for L in L_max_grid:
    ax2.annotate(f'{resid_A[L]*100:.2f}%', xy=(L, resid_A[L]*100),
                 xytext=(5, 10), textcoords='offset points', fontsize=9, color='blue')
    ax2.annotate(f'{resid_B[L]*100:.2f}%', xy=(L, resid_B[L]*100),
                 xytext=(5, -14), textcoords='offset points', fontsize=9, color='red')

ax2.set_xlabel('L_max', fontsize=12)
ax2.set_ylabel(r'$|K_{\mathrm{FIRAS}}-S_{\mathrm{IC}}^{\mathrm{cap}}|/S_{\mathrm{IC}}^{\mathrm{cap}}$ (%)',
               fontsize=12)
ax2.set_title(f'W5-65 residual vs L_max  (drift 5->9: A={drift_A_5_9*100:.2f}%, '
              f'B={drift_B_5_9*100:.2f}%)', fontsize=11)
ax2.grid(True, alpha=0.3)
ax2.legend(fontsize=8, loc='best')
ax2.set_xticks(L_max_grid)
ax2.set_yscale('log')
ax2.set_ylim(1e-2, 1e2)

plt.tight_layout()
png_path = os.path.join(HERE, 's84_w5_65_plot.png')                  # (local)
plt.savefig(png_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"  PNG: {png_path}")

# ============================================================
# SECTION 7: Closure SHA-256 (ordered input-pin map)
# ============================================================
print("\n[SEC 7] Closure SHA-256 (ordered input-pin map)")

closure_map = {                                                      # (local)
    'input_shas': INPUT_SHAS,
    'K_base': K_base,
    'mu_FIRAS': mu_FIRAS,
    'mu_base_L5': mu_base_L5,
    'S_fold': E_budget_SF,
    'Delta_B3': omega_soft,
    'N_modes_total': N_modes_total,
    'S_IC_cap_canonical': S_IC_cap_canonical,
    'L_max_grid': L_max_grid,
    'ratio_A': [ratio_A[L] for L in L_max_grid],
    'ratio_B': [ratio_B[L] for L in L_max_grid],
    'resid_A': [resid_A[L] for L in L_max_grid],
    'resid_B': [resid_B[L] for L in L_max_grid],
    'drift_A_5_9': drift_A_5_9,
    'drift_B_5_9': drift_B_5_9,
    'verdict': verdict,
    'scheme': 'Zubarev',
    'convention': 'R3',
}
closure_blob = json.dumps(closure_map, sort_keys=True).encode()      # (local)
closure_sha = hashlib.sha256(closure_blob).hexdigest()               # (local)
print(f"  closure_sha256 = {closure_sha}")

# ============================================================
# SECTION 8: Verdict-line append
# ============================================================
print("\n[SEC 8] Verdict line")

# Required value format per prompt: <ratio_at_L5,drift_L5-L9>
value_str = f"{ratio_A[5]:.4f},{drift_A_5_9:.4e}"                    # (local)

verdict_line = (
    f"W5-65: {verdict} -- "
    f"value={value_str} "
    f"scheme=Zubarev "
    f"convention=R3 "
    f"L_max={{5,7,9}} "
    f"sha256={closure_sha}"
)

verdict_path = os.path.join(HERE, 's84_gate_verdicts.txt')           # (local)
with open(verdict_path, 'a') as fv:
    fv.write(verdict_line + "\n")

print(f"  Appended to {verdict_path}:")
print(f"    {verdict_line}")

print("\n" + "=" * 76)
print(f"S84 W5-65 GATE-K-FIRAS-COINCIDENCE complete. Verdict: {verdict}")
print("=" * 76)
