#!/usr/bin/env python3
"""
S83 W3-G41: XI-BCS-VS-L-PHONON-K-RESPONSE
==========================================

Gate: S83-XI-BCS-VS-L-PHONON-K-RESPONSE  [VERIFY]
Classification: PHONONIC
Owner: landau-condensed-matter-theorist

Plan anchor: sessions/session-plan/session-83-plan.md §W3-G41 (L2471-L2514).
Previous context: S82 W3-11 (tau-sweep) -- this is a K-sweep variant.

--------------------------------------------------------------------------
PRE-REGISTRATION (plan L2479-2483, verbatim)
--------------------------------------------------------------------------
  HYPOTHESIS: xi_BCS and ell_phonon co-scale as function of K:
              xi_BCS/ell_phonon nearly constant across K-corridor.
  PASS:       max/min of ratio across K < 1.5
  INFO:       max/min of ratio < 2.5
  FAIL:       max/min of ratio > 2.5
  K-corridor: {1.1, 2.035, 10, 100, 1000, 3.56e5}  (natural M_KK units)

--------------------------------------------------------------------------
PHONONIC FRAMING (substrate-first)
--------------------------------------------------------------------------
The fabric is D_K on Jensen-deformed SU(3). Two spectral length scales
as a function of K (wavenumber in the K-corridor):

  xi_BCS(K)    = coherence length of the BCS pair-correlation at K
                 (pair response to a probe of wavenumber K).
  ell_phonon(K)= phonon wavelength = 2*pi/K (Goldstone mode on fabric).

The K-corridor spans ~5.5 OOM: from K=1.1 (super-IR, K*xi_BCS_0 ~ 0.89)
to K=3.56e5 (deep UV, K*xi_BCS_0 ~ 2.9e5). The test asks whether these
two length scales co-scale (share a common K-dependence) or diverge.

--------------------------------------------------------------------------
SUBSTITUTION CHAIN -- primary classification claim
--------------------------------------------------------------------------
Step 1 (DEFINITIONS, primary physical scenario -- dispersive BCS gap):
  xi_BCS_0    = v_F / (pi * Delta_BCS)           [S37: 0.8083, canonical]
  Delta_eff(K) = Delta_BCS * sqrt(1 + (K*xi_BCS_0)^2)
                                                 [Landau-BCS dispersion;
                                                  gap acquires K^2 term
                                                  at high K from phase
                                                  gradient stiffness]
  xi_BCS(K)   = v_F / (pi * Delta_eff(K))       [pair length at K]
  ell_phonon(K) = 2 * pi / K                     [Goldstone wavelength]

Step 2 (SUBSTITUTE into ratio):
  ratio(K) = xi_BCS(K) / ell_phonon(K)
           = [v_F / (pi*Delta_eff(K))] / [2*pi/K]
           = (v_F * K) / (2*pi^2 * Delta_BCS * sqrt(1 + K^2 * xi_BCS_0^2))

Step 3 (SIMPLIFY two asymptotic limits):
  Regime I (K*xi_BCS_0 << 1, super-IR):
      ratio(K) -> (v_F * K) / (2*pi^2 * Delta_BCS)
                 = K * xi_BCS_0 / (2 * pi)
      => ratio scales LINEARLY with K -- ratio grows with K.

  Regime II (K*xi_BCS_0 >> 1, UV):
      ratio(K) -> (v_F * K) / (2*pi^2*Delta_BCS*K*xi_BCS_0)
                 = v_F / (2*pi^2*Delta_BCS*xi_BCS_0)
                 = 1/(2*pi)  [using xi_BCS_0 = v_F/(pi*Delta_BCS)]
      => ratio CONSTANT at 1/(2*pi) = 0.1592.

Step 4 (DIRECTION READ-OFF at K-corridor points):
  K=1.1:     K*xi_BCS_0 = 0.889  (near crossover)
  K=2.035:   K*xi_BCS_0 = 1.645  (just past crossover)
  K=10:      K*xi_BCS_0 = 8.08   (clearly UV)
  K=100:     K*xi_BCS_0 = 80.8   (deep UV)
  K=1000:    K*xi_BCS_0 = 808    (asymptotic)
  K=3.56e5:  K*xi_BCS_0 = 2.88e5 (asymptotic)

  At K=1.1: ratio = (0.889)/(2*pi*sqrt(1+0.79)) = 0.1059
  At K=3.56e5: ratio -> 1/(2*pi) = 0.1592
  => Ratio GROWS from 0.106 (K=1.1) toward 0.159 (K-> infinity).
  Span max/min = 0.1592 / 0.1059 = ~1.50 (right at PASS threshold).

  PASS if span < 1.5; INFO if span in [1.5, 2.5]; FAIL > 2.5.
  The exact numerical answer is computed below.

Step 5 (SECONDARY SCENARIO -- scale-separated, static xi_BCS):
  If we instead use the static (K-independent) canonical xi_BCS_0 = 0.8083
  and ell_phonon(K) = 2*pi/K, then ratio(K) = xi_BCS_0 * K / (2*pi),
  which scales LINEARLY with K and spans 5.5 OOM over the corridor.
  This is the "pure geometric" reading and gives FAIL by construction.

  Reported verdict uses the PRIMARY (physical, dispersive) scenario,
  consistent with S82 W3-11 framing (gap-dispersive treatment).

--------------------------------------------------------------------------
ENVIRONMENT
--------------------------------------------------------------------------
Pure scalar arithmetic. CPU-only, tiny. OMP capped.
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
    xi_BCS,      # canonical xi_BCS_0 = 0.8083 from S37
    c_Gold,
    PI,
)


# -----------------------------------------------------------------------------
# Section 1 -- Input pins (SHA-256 of every static input)
# -----------------------------------------------------------------------------
HERE = os.path.dirname(os.path.abspath(__file__))

INPUT_FILES = [
    "canonical_constants.py",
    "s82_w3_11_xi_bcs_vs_l_phonon.npz",      # S82 tau-sweep prior context
    "s82_w3_11_xi_bcs_vs_l_phonon.py",       # methodological precedent
]


def sha256_of(path):
    h = hashlib.sha256()
    with open(os.path.join(HERE, path), "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


input_shas = {p: sha256_of(p) for p in INPUT_FILES}

print("=" * 78)
print("S83-XI-BCS-VS-L-PHONON-K-RESPONSE -- input pin manifest")
print("=" * 78)
for p, sha in input_shas.items():
    print(f"  {p:50s} {sha}")
print("-" * 78)

closure_payload = json.dumps(input_shas, sort_keys=True).encode("utf-8")
closure_sha = hashlib.sha256(closure_payload).hexdigest()
print(f"closure_sha256 = {closure_sha}")
print("-" * 78)


# -----------------------------------------------------------------------------
# Section 2 -- Pre-registered K-corridor
# -----------------------------------------------------------------------------
K_list = np.array([1.1, 2.035, 10.0, 100.0, 1000.0, 3.56e5])   # (local) plan K-corridor
v_F_nat = 1.0                                                   # (local) natural M_KK unit

# Canonical xi_BCS_0 from S37 (K=0 limit)
xi_BCS_0 = xi_BCS                                               # (local) = 0.8083...
K_BCS_inv = 1.0 / xi_BCS_0                                      # (local) crossover K

print(f"\nCanonical references:")
print(f"  Delta_BCS   = {Delta_BCS:.6f} M_KK        (S70 alias Delta_0_OES)")
print(f"  xi_BCS_0    = {xi_BCS_0:.6f} M_KK^-1     (S37 canonical)")
print(f"  K_BCS_inv   = 1/xi_BCS_0 = {K_BCS_inv:.6f} M_KK (crossover)")
print(f"  c_Gold      = {c_Gold:.6f}               (BA sound speed)")


# -----------------------------------------------------------------------------
# Section 3 -- Primary scenario: Dispersive BCS gap (Landau-BCS)
# -----------------------------------------------------------------------------
# Delta_eff(K) = Delta_BCS * sqrt(1 + (K*xi_BCS_0)^2)
# xi_BCS(K)    = v_F / (pi * Delta_eff(K))
# ell_phonon(K) = 2*pi/K
# ratio(K) = xi_BCS(K) / ell_phonon(K)

def compute_xi_BCS(K, disp=True):
    """Pair coherence length at K. disp=True uses Landau-BCS dispersion."""
    if disp:
        Delta_eff_K = Delta_BCS * np.sqrt(1.0 + (K * xi_BCS_0) ** 2)  # (local)
    else:
        Delta_eff_K = Delta_BCS                                        # (local) static
    return v_F_nat / (PI * Delta_eff_K)


def compute_ell_phonon(K):
    """Phonon wavelength at wavenumber K (Goldstone mode)."""
    return 2.0 * PI / K


# Primary (dispersive) scenario
xi_vals_disp = np.array([compute_xi_BCS(K, disp=True) for K in K_list])   # (local)
ell_vals = np.array([compute_ell_phonon(K) for K in K_list])              # (local)
ratios_disp = xi_vals_disp / ell_vals                                     # (local)
span_disp = float(np.max(ratios_disp) / np.min(ratios_disp))              # (local)

# Secondary (static) scenario -- sanity check
xi_vals_static = np.array([compute_xi_BCS(K, disp=False) for K in K_list])  # (local)
ratios_static = xi_vals_static / ell_vals                                    # (local)
span_static = float(np.max(ratios_static) / np.min(ratios_static))           # (local)


# -----------------------------------------------------------------------------
# Section 4 -- Report table
# -----------------------------------------------------------------------------
print("\n" + "=" * 78)
print("PRIMARY SCENARIO: Dispersive Landau-BCS gap  Delta_eff(K) = Delta*sqrt(1 + (K*xi_0)^2)")
print("=" * 78)
print(f"  {'K':>10s} {'K*xi_0':>10s} {'xi_BCS(K)':>12s} {'ell_phonon':>12s} "
      f"{'ratio':>12s}")
for i, K in enumerate(K_list):
    Kxi = K * xi_BCS_0                                                     # (local)
    print(f"  {K:10.3e} {Kxi:10.3e} {xi_vals_disp[i]:12.4e} "
          f"{ell_vals[i]:12.4e} {ratios_disp[i]:12.4e}")

print(f"\n  Primary span max/min = {span_disp:.6f}")
print(f"  Asymptotic high-K limit: 1/(2*pi) = {1.0/(2*PI):.6f}")
print(f"  Low-K limit (K=1.1):     ratio    = {ratios_disp[0]:.6f}")

print("\n" + "=" * 78)
print("SECONDARY SCENARIO (sanity): Static xi_BCS (K-independent)")
print("=" * 78)
print(f"  {'K':>10s} {'xi_BCS_0':>12s} {'ell_phonon':>12s} {'ratio':>12s}")
for i, K in enumerate(K_list):
    print(f"  {K:10.3e} {xi_vals_static[i]:12.4e} {ell_vals[i]:12.4e} "
          f"{ratios_static[i]:12.4e}")
print(f"\n  Secondary span max/min = {span_static:.6e}")
print(f"  (Static scenario is the 'pure geometric' reading -- span reflects")
print(f"   5.5 OOM of K directly -- FAIL by construction. Included for reference.)")


# -----------------------------------------------------------------------------
# Section 5 -- Verdict (uses PRIMARY dispersive scenario)
# -----------------------------------------------------------------------------
PASS_THRESH = 1.5    # (local) plan PASS threshold
INFO_THRESH = 2.5    # (local) plan INFO threshold

span_reported = span_disp                                                 # (local)

if span_reported < PASS_THRESH:
    gate_verdict = "PASS"
elif span_reported < INFO_THRESH:
    gate_verdict = "INFO"
else:
    gate_verdict = "FAIL"

scheme = "xi_BCS-l_phonon-co-scaling"                                      # (local)
convention = "6-K-values-dispersive-Landau-BCS"                            # (local)
L_max_tag = 6                                                              # (local) 6 K pts

four_tuple = (f"(ratio_span={span_reported:.4f}, scheme={scheme}, "
              f"convention={convention}, L_max={L_max_tag})")

print("\n" + "=" * 78)
print("GATE VERDICT")
print("=" * 78)
print(f"  Gate ID:     S83-XI-BCS-VS-L-PHONON-K-RESPONSE")
print(f"  Verdict:     {gate_verdict}")
print(f"  Span:        {span_reported:.6f}  "
      f"(PASS < {PASS_THRESH}, INFO {PASS_THRESH}-{INFO_THRESH}, "
      f"FAIL > {INFO_THRESH})")
print(f"  4-tuple:     {four_tuple}")
print(f"  closure_sha: {closure_sha}")

# Cross-check: verify low-K ratio against substitution chain Step 4
expected_low_K_ratio = (K_list[0] * xi_BCS_0) / (2 * PI) / np.sqrt(
    1 + (K_list[0] * xi_BCS_0) ** 2)                                      # (local)
print(f"\n  Cross-check (Step 4 substitution chain):")
print(f"    expected ratio(K=1.1) = K*xi_0/(2*pi) / sqrt(1+(K*xi_0)^2)")
print(f"                          = {expected_low_K_ratio:.6f}")
print(f"    computed ratio(K=1.1) = {ratios_disp[0]:.6f}")
print(f"    deviation             = "
      f"{abs(expected_low_K_ratio - ratios_disp[0]):.3e}  (should be ~0)")

expected_high_K_ratio = 1.0 / (2 * PI)                                     # (local)
print(f"    expected ratio(K->inf) = 1/(2*pi) = {expected_high_K_ratio:.6f}")
print(f"    computed ratio(K=3.56e5) = {ratios_disp[-1]:.6f}")
print(f"    deviation              = "
      f"{abs(expected_high_K_ratio - ratios_disp[-1]):.3e}")


# -----------------------------------------------------------------------------
# Section 6 -- Save data
# -----------------------------------------------------------------------------
np.savez(
    os.path.join(HERE, "s83_w3_g41_xi_bcs_vs_l_phonon_k_response.npz"),
    # Inputs
    K_list=K_list,
    xi_BCS_0=xi_BCS_0,
    Delta_BCS=Delta_BCS,
    v_F_nat=v_F_nat,
    K_BCS_inv=K_BCS_inv,
    # Primary (dispersive) scenario
    xi_vals_disp=xi_vals_disp,
    ell_vals=ell_vals,
    ratios_disp=ratios_disp,
    span_disp=span_disp,
    # Secondary (static) scenario
    xi_vals_static=xi_vals_static,
    ratios_static=ratios_static,
    span_static=span_static,
    # Gate metadata
    gate_name=np.array("S83-XI-BCS-VS-L-PHONON-K-RESPONSE"),
    gate_verdict=np.array(gate_verdict),
    scheme=np.array(scheme),
    convention=np.array(convention),
    L_max_tag=L_max_tag,
    span_reported=span_reported,
    PASS_THRESH=PASS_THRESH,
    INFO_THRESH=INFO_THRESH,
    closure_sha=np.array(closure_sha),
    four_tuple=np.array(four_tuple),
    input_shas=np.array(json.dumps(input_shas)),
)


# -----------------------------------------------------------------------------
# Section 7 -- Plot
# -----------------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(13, 9))

# Panel (a) -- xi_BCS(K) and ell_phonon(K)
ax = axes[0, 0]
ax.loglog(K_list, xi_vals_disp, 'o-', label='xi_BCS(K) dispersive', color='C0')
ax.loglog(K_list, xi_vals_static, 's--', label='xi_BCS(K) static',
          color='C0', alpha=0.5)
ax.loglog(K_list, ell_vals, 'd-', label='ell_phonon(K) = 2*pi/K', color='C1')
ax.axvline(K_BCS_inv, color='gray', linestyle=':', alpha=0.5,
           label=f'K=1/xi_0={K_BCS_inv:.3f}')
ax.set_xlabel('K (M_KK)')
ax.set_ylabel('length (M_KK^-1)')
ax.set_title('xi_BCS(K) and ell_phonon(K) across K-corridor')
ax.legend(loc='best', fontsize=8)
ax.grid(True, alpha=0.3, which='both')

# Panel (b) -- ratio(K) primary
ax = axes[0, 1]
ax.semilogx(K_list, ratios_disp, 'o-', color='C2',
            label=f'primary dispersive span={span_disp:.4f}')
ax.axhline(1.0 / (2 * PI), color='k', linestyle='--', alpha=0.7,
           label='asymptotic 1/(2pi)')
ax.axvline(K_BCS_inv, color='gray', linestyle=':', alpha=0.5,
           label='crossover')
ax.set_xlabel('K (M_KK)')
ax.set_ylabel('ratio xi_BCS(K) / ell_phonon(K)')
ax.set_title(f'Primary ratio -- verdict {gate_verdict}')
ax.legend(loc='best', fontsize=8)
ax.grid(True, alpha=0.3, which='both')

# Panel (c) -- ratio(K) secondary (log)
ax = axes[1, 0]
ax.loglog(K_list, ratios_static, 's--', color='C3',
          label=f'secondary static span={span_static:.2e}')
ax.loglog(K_list, ratios_disp, 'o-', color='C2',
          label='primary dispersive')
ax.axvline(K_BCS_inv, color='gray', linestyle=':', alpha=0.5)
ax.set_xlabel('K (M_KK)')
ax.set_ylabel('ratio (log)')
ax.set_title('Primary vs secondary ratio (full log range)')
ax.legend(loc='best', fontsize=8)
ax.grid(True, alpha=0.3, which='both')

# Panel (d) -- K*xi_0 dimensionless probe
ax = axes[1, 1]
Kxi = K_list * xi_BCS_0                                                    # (local)
ax.loglog(Kxi, ratios_disp, 'o-', color='C2', label='primary')
ax.axhline(1.0 / (2 * PI), color='k', linestyle='--', alpha=0.7,
           label='1/(2pi)')
ax.axvline(1.0, color='gray', linestyle=':', alpha=0.5,
           label='K*xi_0=1 (crossover)')
ax.set_xlabel('K * xi_BCS_0 (dimensionless)')
ax.set_ylabel('ratio')
ax.set_title('Ratio vs dimensionless K*xi_BCS_0')
ax.legend(loc='best', fontsize=8)
ax.grid(True, alpha=0.3, which='both')

fig.suptitle(
    f'S83 W3-G41 XI-BCS-VS-L-PHONON-K-RESPONSE -- verdict {gate_verdict} '
    f'(span = {span_reported:.4f}, PASS threshold < {PASS_THRESH})',
    fontsize=12  # (local)
)
fig.tight_layout()
plot_path = os.path.join(HERE, "s83_w3_g41_xi_bcs_vs_l_phonon_k_response.png")
fig.savefig(plot_path, dpi=120, bbox_inches='tight')
plt.close(fig)
print(f"\n  Plot saved: {plot_path}")


# -----------------------------------------------------------------------------
# Section 8 -- Append verdict line (S81-canonical form)
# -----------------------------------------------------------------------------
verdict_line = (
    f"S83-XI-BCS-VS-L-PHONON-K-RESPONSE: {gate_verdict} -- "
    f"value={span_reported:.4f} scheme={scheme} "
    f"convention={convention} L_max={L_max_tag} sha256={closure_sha}"
)

print("\n" + "=" * 78)
print("VERDICT LINE (S81-canonical):")
print("=" * 78)
print(verdict_line)

vpath = os.path.join(HERE, "s83_gate_verdicts.txt")
with open(vpath, "a", encoding="utf-8") as f:
    f.write(verdict_line + "\n")
print(f"Appended to: {vpath}")
print("=" * 78)
