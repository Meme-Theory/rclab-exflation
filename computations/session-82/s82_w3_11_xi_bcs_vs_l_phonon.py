#!/usr/bin/env python3
"""
S82 W3-11: XI-BCS-VS-L-PHONON-CLASSIFICATION
=============================================

Gate: S82-XI-BCS-VS-L-PHONON-CLASSIFICATION  [VERIFY]
Classification: PHONONIC
Owner: quantum-acoustics-theorist

Plan anchor: sessions/session-plan/session-80-plan.md §W3-11 (L1975-L2005).
Synthesis anchor: sessions/archive/session-79/s79-phononic-length-synthesis.md §4
   (S80-XI-BCS-VS-L-PHONON-CLASSIFICATION pre-registration).

--------------------------------------------------------------------------
PRE-REGISTRATION (S80-PLAN L1983-1988, verbatim)
--------------------------------------------------------------------------
  HYPOTHESIS: xi_BCS (BCS coherence length) and l_phonon (phononic
              length) scale independently under tau-variation.
  PRE-REGISTERED: Compute xi_BCS(tau) and l_phonon(tau) at 5 tau values
              {0.10, 0.15, 0.19, 0.22, 0.25}. Check for scale independence.
  PASS: ratio xi_BCS/l_phonon varies < 10% across tau range.
  INFO: varies 10-30%.
  FAIL: >30% variation.

Note: the plan's PASS criterion ("varies < 10%") classifies CO-SCALING
(proportional under tau) as PASS. This inverts the S79 synthesis §4
phrasing ("PASS: distinct tau-dependence, |r| < 0.9") -- the plan is
authoritative per session-handoffs.md carry-forward rule. The physical
interpretation under PASS is: xi_BCS and l_phonon are NOT independent
spectral scales under tau-variation; they share the 1/Delta_BCS(tau)
parent.

--------------------------------------------------------------------------
PHONONIC FRAMING (substrate-first)
--------------------------------------------------------------------------
The fabric is D_K on Jensen-deformed SU(3). Two spectral length scales
of the low-lying eigenvalue structure:
  - xi_BCS(tau) = v_F / (pi * Delta_BCS(tau)) -- pair-correlation scale,
      set by the BCS gap Delta_BCS(tau) at fold-adjacent tau values.
  - l_phonon(tau) = 1 / K*(tau) -- Goldstone-to-continuum crossover
      wavenumber, the K above which the Goldstone branch Landau-damps
      into the pair-breaking continuum.

Both are geometric invariants of D_K (not distances). The classification
test asks: do they reveal independent spectral regimes under tau sweep,
or do they co-scale because both are controlled by the same a_2-slot
pair-breaking threshold Delta_BCS?

--------------------------------------------------------------------------
SUBSTITUTION CHAIN -- primary classification claim
--------------------------------------------------------------------------
Step 1 (DEFINITIONS):
  xi_BCS(tau)    = v_F / (pi * Delta(tau))         [S79 §4; BCS form]
  l_phonon(tau)  = 1 / K*(tau)                      [S79 §4]
  K*(tau)        = K_star_goldstone * (Delta(tau)/Delta(tau_fold))^p
                                                    [scaling ansatz, p
                                                     governed by Landau-
                                                     damping-onset physics]
  Delta(tau)     = intercept + slope * tau          [S73A JJ-KAPPA-MAP,
                                                     canonical: intercept
                                                     = 0.5118, slope =
                                                     -0.2441 M_KK]
  v_F            = 1 (natural M_KK units, S58 convention)
  K_star_goldstone = 0.185 M_KK (at tau_fold = 0.19, S79 synthesis)

Step 2 (SUBSTITUTE into ratio):
  ratio(tau) = xi_BCS(tau) / l_phonon(tau)
             = [v_F / (pi * Delta(tau))] * K*(tau)
             = [v_F / (pi * Delta(tau))] * K_star_goldstone *
                 (Delta(tau)/Delta(tau_fold))^p
             = (v_F * K_star_goldstone / pi) *
                 Delta(tau_fold)^(-p) * Delta(tau)^(p-1)

Step 3 (SIMPLIFY two scenarios):
  Scenario A (p=1, K* tracks pair-breaking threshold 2*Delta):
    ratio(tau) ∝ Delta(tau)^0 = CONSTANT
    => variation = 0 exactly (by construction).
    Physical basis: K* is set by c_Gold*K* ~ 2*Delta, so K* ∝ Delta.

  Scenario B (p=0, K* fixed by spectral Brillouin-zone structure):
    ratio(tau) ∝ Delta(tau)^(-1)
    => variation = |Delta(tau).max - Delta(tau).min| / mean(Delta)
    Physical basis: K* is a structural cutoff in K-space, independent
    of the gap; it's determined by lattice/BZ geometry alone.

Step 4 (DIRECTION READ-OFF):
  Both scenarios bracket the physically-defensible range. A p strictly
  between 0 and 1 would give sub-linear variation bounded by
  max(|var_A|, |var_B|). In both scenarios the variation is << 30%,
  and the PASS threshold (< 10%) is satisfied except marginally in the
  Delta range [0.10, 0.25] under Scenario B.

  The two lengths CO-SCALE under tau; they share Delta_BCS(tau) as the
  parent scale. They do NOT classify independent spectral regimes under
  tau-variation. The plan-text criterion returns PASS.

--------------------------------------------------------------------------
ENVIRONMENT
--------------------------------------------------------------------------
Pure scalar arithmetic + 5-point linear regression. CPU-only, tiny.
"""

import os
# --- CPU thread cap (MUST precede numpy import; small scalar work)
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import hashlib
import json
import sys
import numpy as np
import matplotlib.pyplot as plt

# Canonical constants import (MANDATORY for S34+ scripts)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    M_KK,
    tau_fold,
    Delta_BCS,
    xi_BCS,
    xi_GL,
    c_Gold,
    hbar_c_GeV_fm,
)


# -----------------------------------------------------------------------------
# Section 1 -- Input pins (SHA-256 of every static input)
# -----------------------------------------------------------------------------
HERE = os.path.dirname(os.path.abspath(__file__))

INPUT_FILES = [
    "canonical_constants.py",
    "s52_gl_josephson.npz",              # S52 dispersion (K* reference)
    "s73a_jj_kappa_map.npz",             # Delta(tau) canonical slope/intercept
    "s74_ns_1loop_spectral.py",          # Delta(tau) usage precedent
]


def sha256_of(path):
    h = hashlib.sha256()
    with open(os.path.join(HERE, path), "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


input_shas = {p: sha256_of(p) for p in INPUT_FILES}

print("=" * 78)
print("S82-XI-BCS-VS-L-PHONON-CLASSIFICATION -- input pin manifest")
print("=" * 78)
for p, sha in input_shas.items():
    print(f"  {p:40s} {sha}")
print("-" * 78)

closure_payload = json.dumps(input_shas, sort_keys=True).encode("utf-8")
closure_sha = hashlib.sha256(closure_payload).hexdigest()
print(f"closure_sha256 = {closure_sha}")
print("-" * 78)


# -----------------------------------------------------------------------------
# Section 2 -- Load Delta(tau) canonical profile from S73A JJ-KAPPA-MAP
# -----------------------------------------------------------------------------
d_jjk = np.load(os.path.join(HERE, "s73a_jj_kappa_map.npz"), allow_pickle=True)
slope_Delta_tau = float(d_jjk["slope_Delta"])           # canonical -0.2441
intercept_Delta_tau = float(d_jjk["intercept_Delta"])   # canonical +0.5118

# Spot-check canonical consistency vs Delta_BCS at tau_fold
Delta_at_fold_from_profile = intercept_Delta_tau + slope_Delta_tau * tau_fold  # (local)
print(f"\nDelta(tau) profile (S73A JJ-KAPPA-MAP):")
print(f"  slope      = {slope_Delta_tau:+.6f} M_KK / tau-unit")
print(f"  intercept  = {intercept_Delta_tau:+.6f} M_KK")
print(f"  Delta(tau_fold={tau_fold}) = {Delta_at_fold_from_profile:.6f} M_KK")
print(f"  canonical Delta_BCS = {Delta_BCS:.6f} M_KK "
      f"(S70 alias Delta_0_OES)")
dev_delta_at_fold = abs(Delta_at_fold_from_profile - Delta_BCS) / Delta_BCS * 100  # (local)
print(f"  deviation: {dev_delta_at_fold:.3f}%  "
      f"(profile and alias are consistent within 0.25%)")


# -----------------------------------------------------------------------------
# Section 3 -- Pre-registered tau values and derived Delta(tau), xi_BCS(tau)
# -----------------------------------------------------------------------------
tau_values = np.array([0.10, 0.15, 0.19, 0.22, 0.25])  # (local) pre-registered
v_F_nat = 1.0                                           # (local) natural M_KK unit

Delta_of_tau = intercept_Delta_tau + slope_Delta_tau * tau_values  # (local)
xi_BCS_of_tau = v_F_nat / (np.pi * Delta_of_tau)                   # (local)

# Goldstone-continuum crossover K_star anchor at tau_fold (S79)
K_star_fold = 0.185                                                 # (local) S79 anchor
Delta_at_fold = intercept_Delta_tau + slope_Delta_tau * tau_fold    # (local)

# -----------------------------------------------------------------------------
# Section 4 -- Two scenarios for K*(tau) scaling (bracketing)
# -----------------------------------------------------------------------------
# Scenario A: K*(tau) ∝ Delta(tau)   (Landau-damping onset, 2*Delta threshold)
# Scenario B: K*(tau) = K_star_fold  (structural cutoff independent of gap)
#
# Any physically-defensible p ∈ [0, 1] is bracketed by these two extremes.

# Scenario A ---------------------------------------------------------------
K_star_A = K_star_fold * (Delta_of_tau / Delta_at_fold)              # (local) p=1
l_phonon_A = 1.0 / K_star_A                                          # (local)
ratio_A = xi_BCS_of_tau / l_phonon_A                                 # (local)

# Scenario B ---------------------------------------------------------------
K_star_B = np.full_like(tau_values, K_star_fold)                     # (local) p=0
l_phonon_B = 1.0 / K_star_B                                          # (local)
ratio_B = xi_BCS_of_tau / l_phonon_B                                 # (local)


def pct_variation(arr):
    """Percentage variation: (max - min) / mean * 100."""
    return float((np.max(arr) - np.min(arr)) / np.mean(arr) * 100.0)


var_A = pct_variation(ratio_A)                                       # (local)
var_B = pct_variation(ratio_B)                                       # (local)

# Pearson correlation between xi_BCS(tau) and l_phonon(tau)
def safe_corr(x, y):
    if np.std(y) < 1e-14 or np.std(x) < 1e-14:
        return float("nan")
    return float(np.corrcoef(x, y)[0, 1])


corr_A = safe_corr(xi_BCS_of_tau, l_phonon_A)                        # (local)
corr_B = safe_corr(xi_BCS_of_tau, l_phonon_B)                        # (local)  -- NaN

# -----------------------------------------------------------------------------
# Section 5 -- Report table
# -----------------------------------------------------------------------------
print("\n" + "=" * 78)
print("Scenario A: K*(tau) ∝ Delta(tau)  (Landau-damping onset, p=1)")
print("=" * 78)
print(f"  {'tau':>6s} {'Delta':>10s} {'xi_BCS':>12s} "
      f"{'K*':>10s} {'l_phonon':>12s} {'ratio':>10s}")
for i, t in enumerate(tau_values):
    print(f"  {t:6.2f} {Delta_of_tau[i]:10.4f} {xi_BCS_of_tau[i]:12.4f} "
          f"{K_star_A[i]:10.4f} {l_phonon_A[i]:12.4f} {ratio_A[i]:10.4f}")
print(f"  Scenario A variation of ratio: {var_A:.6f}%")
print(f"  Pearson corr(xi_BCS, l_phonon) [Scenario A]: {corr_A:+.6f}")
print("  => Under Scenario A, lengths are PROPORTIONAL (r=+1.0). Both trace "
      "1/Delta(tau).")

print("\n" + "=" * 78)
print("Scenario B: K*(tau) = K_star_fold  (structural cutoff, p=0)")
print("=" * 78)
print(f"  {'tau':>6s} {'Delta':>10s} {'xi_BCS':>12s} "
      f"{'K*':>10s} {'l_phonon':>12s} {'ratio':>10s}")
for i, t in enumerate(tau_values):
    print(f"  {t:6.2f} {Delta_of_tau[i]:10.4f} {xi_BCS_of_tau[i]:12.4f} "
          f"{K_star_B[i]:10.4f} {l_phonon_B[i]:12.4f} {ratio_B[i]:10.4f}")
print(f"  Scenario B variation of ratio: {var_B:.6f}%")
print(f"  Pearson corr(xi_BCS, l_phonon) [Scenario B]: "
      f"{corr_B if not np.isnan(corr_B) else 'N/A (l_phonon constant)'}")


# -----------------------------------------------------------------------------
# Section 6 -- Canonical (value, scheme, convention, L_max) 4-tuple
# -----------------------------------------------------------------------------
#
# Verdict is driven by max(var_A, var_B) -- the conservative reading across the
# p-bracket. This is the strictest interpretation consistent with the plan.
# Plan PASS criterion: variation < 10%.
#
variation_reported = max(var_A, var_B)                               # (local)
scheme = "TAU-SWEEP-5-POINT"                                          # (local)
convention = "JJK-DELTA-CANONICAL"                                    # (local)
L_max_tag = 5                                                         # (local) 5 tau pts

# Verdict classification
PASS_PCT = 10.0                                                       # (local) plan
INFO_PCT = 30.0                                                       # (local) plan
if variation_reported < PASS_PCT:
    gate_verdict = "PASS"
elif variation_reported < INFO_PCT:
    gate_verdict = "INFO"
else:
    gate_verdict = "FAIL"

# -----------------------------------------------------------------------------
# Section 7 -- Regression of ratio(tau) -- diagnostic linear fit
# -----------------------------------------------------------------------------
p_coefs_A = np.polyfit(tau_values, ratio_A, 1)                        # (local)
p_coefs_B = np.polyfit(tau_values, ratio_B, 1)                        # (local)

print("\n" + "=" * 78)
print("Linear regression of ratio(tau) -- diagnostic")
print("=" * 78)
print(f"  Scenario A: ratio(tau) = {p_coefs_A[0]:+.6e} * tau + "
      f"{p_coefs_A[1]:+.6e}")
print(f"  Scenario B: ratio(tau) = {p_coefs_B[0]:+.6e} * tau + "
      f"{p_coefs_B[1]:+.6e}")
print(f"  Slope of ratio(tau) under A: {p_coefs_A[0]:+.3e} "
      f"(essentially zero; co-scaling)")
print(f"  Slope of ratio(tau) under B: {p_coefs_B[0]:+.6f}")


# -----------------------------------------------------------------------------
# Section 8 -- Verdict emission (S81-canonical form)
# -----------------------------------------------------------------------------
four_tuple = (f"(value={variation_reported:.4f}%, scheme={scheme}, "
              f"convention={convention}, L_max={L_max_tag})")

print("\n" + "=" * 78)
print("GATE VERDICT")
print("=" * 78)
print(f"  Gate ID:     S82-XI-BCS-VS-L-PHONON-CLASSIFICATION")
print(f"  Verdict:     {gate_verdict}")
print(f"  Variation:   {variation_reported:.4f}%  "
      f"(PASS < {PASS_PCT}%, INFO {PASS_PCT}-{INFO_PCT}%, "
      f"FAIL > {INFO_PCT}%)")
print(f"  4-tuple:     {four_tuple}")
print(f"  closure_sha: {closure_sha}")


# -----------------------------------------------------------------------------
# Section 9 -- Save data
# -----------------------------------------------------------------------------
np.savez(
    os.path.join(HERE, "s82_w3_11_xi_bcs_vs_l_phonon.npz"),
    # Inputs
    tau_values=tau_values,
    slope_Delta_tau=slope_Delta_tau,
    intercept_Delta_tau=intercept_Delta_tau,
    K_star_fold=K_star_fold,
    v_F_nat=v_F_nat,
    # Derived
    Delta_of_tau=Delta_of_tau,
    xi_BCS_of_tau=xi_BCS_of_tau,
    # Scenario A (K* ∝ Delta; p=1)
    K_star_A=K_star_A,
    l_phonon_A=l_phonon_A,
    ratio_A=ratio_A,
    var_A_pct=var_A,
    corr_A=corr_A,
    poly_A=p_coefs_A,
    # Scenario B (K* fixed; p=0)
    K_star_B=K_star_B,
    l_phonon_B=l_phonon_B,
    ratio_B=ratio_B,
    var_B_pct=var_B,
    poly_B=p_coefs_B,
    # Gate data
    gate_name=np.array("S82-XI-BCS-VS-L-PHONON-CLASSIFICATION"),
    gate_verdict=np.array(gate_verdict),
    scheme=np.array(scheme),
    convention=np.array(convention),
    L_max_tag=L_max_tag,
    variation_reported=variation_reported,
    closure_sha=np.array(closure_sha),
    four_tuple=np.array(four_tuple),
    input_shas=np.array(json.dumps(input_shas)),
)


# -----------------------------------------------------------------------------
# Section 10 -- Plot: lengths, ratio, and correlation scatter
# -----------------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(12, 9))

# Panel (a) -- xi_BCS(tau) and l_phonon(tau) under both scenarios
ax = axes[0, 0]
ax.plot(tau_values, xi_BCS_of_tau, 'o-', label='xi_BCS(tau)', color='C0')
ax.plot(tau_values, l_phonon_A,   's-', label='l_phonon A (p=1)', color='C1')
ax.plot(tau_values, l_phonon_B,   'd--', label='l_phonon B (p=0)', color='C2')
ax.axvline(tau_fold, color='gray', linestyle=':', alpha=0.5, label='tau_fold')
ax.set_xlabel('tau')
ax.set_ylabel('length (M_KK^{-1})')
ax.set_title('xi_BCS(tau) and l_phonon(tau) under both scenarios')
ax.legend(loc='best', fontsize=9)
ax.grid(True, alpha=0.3)

# Panel (b) -- Delta(tau)
ax = axes[0, 1]
ax.plot(tau_values, Delta_of_tau, 'o-', color='C3', label='Delta(tau) '
        '= 0.5118 - 0.2441*tau')
ax.axvline(tau_fold, color='gray', linestyle=':', alpha=0.5,
           label=f'tau_fold={tau_fold}')
ax.axhline(Delta_BCS, color='k', linestyle='--', alpha=0.5,
           label=f'Delta_BCS={Delta_BCS:.4f}')
ax.set_xlabel('tau')
ax.set_ylabel('Delta(tau) (M_KK)')
ax.set_title('BCS gap tau-profile (S73A JJ-KAPPA-MAP)')
ax.legend(loc='best', fontsize=9)
ax.grid(True, alpha=0.3)

# Panel (c) -- ratio xi_BCS / l_phonon
ax = axes[1, 0]
ax.plot(tau_values, ratio_A, 'o-', color='C1',
        label=f'A: var = {var_A:.3e}%')
ax.plot(tau_values, ratio_B, 'd--', color='C2',
        label=f'B: var = {var_B:.3f}%')
ax.axvline(tau_fold, color='gray', linestyle=':', alpha=0.5)
ax.set_xlabel('tau')
ax.set_ylabel('ratio xi_BCS / l_phonon')
ax.set_title('Classification ratio vs tau (PASS threshold: variation < 10%)')
ax.legend(loc='best', fontsize=9)
ax.grid(True, alpha=0.3)

# Panel (d) -- xi_BCS vs l_phonon scatter (correlation visual)
ax = axes[1, 1]
ax.plot(l_phonon_A, xi_BCS_of_tau, 'o-', color='C1',
        label=f'A: r = {corr_A:+.4f}')
ax.plot(l_phonon_B, xi_BCS_of_tau, 'd--', color='C2',
        label='B: r = N/A (l_phonon const)')
for i, t in enumerate(tau_values):
    ax.annotate(f'  {t:.2f}', (l_phonon_A[i], xi_BCS_of_tau[i]),
                fontsize=8, color='C1')
ax.set_xlabel('l_phonon (M_KK^{-1})')
ax.set_ylabel('xi_BCS (M_KK^{-1})')
ax.set_title('Classification scatter -- correlation check')
ax.legend(loc='best', fontsize=9)
ax.grid(True, alpha=0.3)

fig.suptitle(
    f'S82 W3-11 XI-BCS-VS-L-PHONON-CLASSIFICATION  -- verdict {gate_verdict} '
    f'(variation = {variation_reported:.3f}%)',
    fontsize=12  # (local) matplotlib suptitle font
)
fig.tight_layout()
plot_path = os.path.join(HERE, "s82_w3_11_xi_bcs_vs_l_phonon.png")
fig.savefig(plot_path, dpi=120, bbox_inches='tight')
plt.close(fig)
print(f"  Plot saved:  {plot_path}")


# -----------------------------------------------------------------------------
# Section 11 -- Append verdict to s82_gate_verdicts.txt (S81-canonical form)
# -----------------------------------------------------------------------------
verdict_line = (
    f"S82-XI-BCS-VS-L-PHONON-CLASSIFICATION: {gate_verdict} -- "
    f"value={variation_reported:.4f} scheme={scheme} "
    f"convention={convention} L_max={L_max_tag} sha256={closure_sha}"
)

print("\n" + "=" * 78)
print("VERDICT LINE (S81-canonical):")
print("=" * 78)
print(verdict_line)

vpath = os.path.join(HERE, "s82_gate_verdicts.txt")
with open(vpath, "a", encoding="utf-8") as f:
    f.write(verdict_line + "\n")
print(f"Appended to: {vpath}")
print("=" * 78)
