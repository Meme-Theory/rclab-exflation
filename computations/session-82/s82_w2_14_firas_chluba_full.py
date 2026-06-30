#!/usr/bin/env python3
"""
S82 W2-14: FIRAS-CHLUBA-FULL (mu-distortion full-kernel)
==========================================================

Gate: S82-FIRAS-CHLUBA-FULL  [VERIFY]
Classification: PHONONIC
Owner: mack-cosmic-bridge
Write-target: Section V.N of session-82-results-workingpaper.md

Phononic framing:
  mu-distortion is the substrate's residual thermal signature from GGE
  relic physics. Post-transit GGE acoustic quasiparticle pairs (Parker
  pair production, 59.8 pairs) deposit energy into the photon bath
  across k ~ 46-10^4 Mpc^-1 (the Chluba diffusion-damping window).
  Outside this band, modes either free-stream (k < 46) or thermalize
  fully (k > 10^4). The Chluba kernel IS the matching-impedance
  between the framework's B3 acoustic envelope and the FIRAS observable.

Pre-registration (S80 plan L1663-L1669, VERBATIM):
  GATE: S80-FIRAS-CHLUBA-FULL
  HYPOTHESIS: The mu-distortion PASS (5.16 OOM margin; sign fixed via
    Chluba kernel) per P2-B is robust under full Chluba-kernel-
    weighted FIRAS integral.
  PRE-REGISTERED: mu = int dN/dE * kernel(E) dE with correct Chluba
    kernel (fixing the S78 wrong-sign FLAT-KERNEL artifact).
  PASS: mu within factor-3 of S79 P2-B value 6.17e-10.
  INFO: factor-3 to factor-10.
  FAIL: >factor-10.

Substitution chain (MANDATORY per math-scripts.md):

  Step 1: Definition (Chluba 2012 ApJ 758 76 Eq. 10).
    W_mu(k) = exp(-k^2 / k_D(z_th)^2) - exp(-k^2 / k_D(z_mu)^2)
    where k_D(z_mu) ~ 46 Mpc^-1 (y/mu boundary: modes below free-stream
    before dissipation; y-distortion regime, not mu) and
    k_D(z_th) ~ 10^4 Mpc^-1 (thermalization cutoff: modes above
    erased by double-Compton scattering to BE equilibrium).

    The task's "mu = int dN/dE * kernel(E) dE" language maps to the
    native k-space formulation: Chluba mu-distortion physics is
    k-space (silk-diffusion damping), with the framework's acoustic
    pair density per mode (dN/dk) given by the Bogoliubov
    occupation |alpha + beta|^2 ~ S_IC(k). E-space and k-space
    descriptions are related by E = hbar c k and are
    transformation-equivalent for the integral shape.

  Step 2: Substitute framework UV-extrapolated envelopes at k_pivot:
    P_zeta(k) = A_s_obs * (k/k_pivot)^(n_s - 1)
    S_IC(k)   = S_IC_0 * (k/k_pivot)^(alpha_S_IC)
      with S_IC_0 = 1.636e5 (anchored at k_pivot from s79_w1e_k_scan)
      and alpha_S_IC = -2.192 (empirical UV slope, S79 P2-B C1)
      and A_s_obs = 2.1e-9 (Planck 2018 observed).

  Step 3: Integrate (S79 P2-B C2 canonical form):
    mu = 2.27 * integral[ d(ln k) * P_zeta(k) * S_IC(k)
                         * W_mu(k) / W_peak ] over k in [10, 3e4] Mpc^-1

  Step 4: Direction read-off (OUTPUT, not asserted):
    PASS:  |log10(mu/6.17e-10)| < log10(3)  ~= 0.477
    INFO:  log10(3) < |log10(mu/6.17e-10)| < log10(10) = 1.0
    FAIL:  |log10(mu/6.17e-10)| >= 1.0 (factor-10)

Verdict thresholds (S80 plan L1667-L1669):
  PASS : mu within factor-3 of 6.17e-10
  INFO : factor-3 to factor-10
  FAIL : > factor-10

References:
  - Chluba & Sunyaev 2012 ApJ 758 76, Eq. 10 (W_mu kernel)
  - Chluba 2013 MNRAS 434 352 (analytic window function)
  - S79 P2-B workshop (p2-b-pbh-prefold-wrong-sign.md: L630-L690)
  - S79 P2-B C1 envelope table (L641-L649)
  - S79 P2-B C2 integral definition (L653-L662)
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

# Canonical constants (MANDATORY per CLAUDE.md)
from canonical_constants import (
    A_s_CMB,                 # Planck observed A_s ~ 2.1e-9
    k_pivot_planck,          # 0.05 Mpc^-1 (Planck CMB pivot)
    planck_ns,               # 0.9649 Planck scalar tilt
    sigma_FIRAS,             # 1.0e-6 (narrow) for reference
    FIRAS_dT_bound,          # 3.0e-6
)

# ============================================================
# SECTION 0: Input SHA-256 pins (MANDATORY in first 20 lines)
# ============================================================
HERE = os.path.dirname(os.path.abspath(__file__))                  # (local)


def _sha256(path):
    with open(path, 'rb') as h:
        return hashlib.sha256(h.read()).hexdigest()


INPUT_FILES = [                                                    # (local)
    os.path.join(HERE, 'canonical_constants.py'),
    os.path.join(HERE, 's82_gate_verdicts.txt'),
]

print("=" * 70)
print("S82 W2-14: FIRAS-CHLUBA-FULL (mu-distortion full-kernel)")
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
# SECTION 1: Chluba 2012 kernel definition
# ============================================================
print("\n[SEC 1] Chluba 2012 ApJ 758 76 Eq. 10 kernel")

# Diffusion scales (Chluba 2012; values per S79 P2-B C1, L635-L637)
k_D_mu = 46.0         # (local) lower cutoff: y/mu boundary, Mpc^-1
k_D_th = 1.0e4        # (local) upper cutoff: thermalization (dbl-Compton), Mpc^-1


def W_mu(k):
    """Chluba 2012 Eq. 10 mu-distortion window function."""
    return np.exp(-k**2 / k_D_th**2) - np.exp(-k**2 / k_D_mu**2)


# Exact peak: d/dk[W_mu] = 0 gives
#   k_peak^2 = 2 ln(k_D_th/k_D_mu) / (1/k_D_mu^2 - 1/k_D_th^2)
k_peak_sq = 2.0 * np.log(k_D_th / k_D_mu) / (1.0/k_D_mu**2 - 1.0/k_D_th**2)  # (local)
k_peak = float(np.sqrt(k_peak_sq))                                           # (local)
W_peak = float(W_mu(k_peak))                                                 # (local)

print(f"  k_D_mu (y/mu boundary)     = {k_D_mu:.1f} Mpc^-1")
print(f"  k_D_th (thermalization)    = {k_D_th:.1e} Mpc^-1")
print(f"  k_peak (exact, W_mu max)   = {k_peak:.3f} Mpc^-1  (expected ~151)")
print(f"  W_peak                     = {W_peak:.6f}  (~unity, broad plateau)")

# Kernel diagnostic table (verifies against S79 P2-B C1 Table L641-L649)
print("\n  Kernel diagnostic table (W_mu at probe k values):")
for k_probe in [46.0, 100.0, 150.0, 300.0, 740.0, 1000.0, 3000.0, 1.0e4]:
    print(f"    k={k_probe:>7.1f} Mpc^-1:  W_mu={W_mu(k_probe):.4f}")

# ============================================================
# SECTION 2: Framework UV-extrapolated envelopes (S79 P2-B C1)
# ============================================================
print("\n[SEC 2] Framework envelopes (UV-extrapolated, anchored at k_pivot)")

# Framework k_pivot convention (S79 P2-B uses 0.056, Planck canonical 0.05).
# Use the S79 P2-B anchor for reproducibility; document both.
k_pivot = 0.056                    # (local) S79 P2-B anchor, Mpc^-1
k_pivot_canonical = k_pivot_planck # (local) Planck 2018 canonical 0.05 Mpc^-1

# UV-extrapolated envelopes from s79_w1e_k_scan_fixed_eta (S79 P2-B C1, L639)
S_IC_0 = 1.636e5                   # (local) S_IC(k_pivot), POWER-RATIO, |alpha+beta|^2
alpha_S_IC = -2.192                # (local) empirical UV slope, S79 P2-B C1
beta_sq_0 = 4.26e4                 # (local) |beta|^2(k_pivot), for diagnostic
alpha_beta = -1.331                # (local) |beta|^2 UV slope (B1 impulse)


def P_zeta(k, ns=planck_ns):
    """Scalar power spectrum with Planck tilt (reduces to flat at ns=1)."""
    return A_s_CMB * (k / k_pivot)**(ns - 1.0)


def S_IC(k):
    """Post-fold B3 Bogoliubov occupation envelope |alpha+beta|^2(k)."""
    return S_IC_0 * (k / k_pivot)**alpha_S_IC


def beta_sq(k):
    """B1 Parker-pair production envelope |beta|^2(k)."""
    return beta_sq_0 * (k / k_pivot)**alpha_beta


print(f"  k_pivot (S79 P2-B anchor)  = {k_pivot:.3f} Mpc^-1")
print(f"  k_pivot_canonical (Planck) = {k_pivot_canonical:.3f} Mpc^-1")
print(f"  A_s_obs (Planck)           = {A_s_CMB:.3e}")
print(f"  n_s (Planck)               = {planck_ns:.4f}")
print(f"  S_IC(k_pivot)              = {S_IC_0:.3e}")
print(f"  alpha_S_IC (UV slope)      = {alpha_S_IC:.3f}")
print(f"  |beta|^2(k_pivot)          = {beta_sq_0:.3e}")
print(f"  alpha_beta (B1 slope)      = {alpha_beta:.3f}")

# Envelope diagnostic at probe k values (for §V.N table)
print("\n  Envelope diagnostic table (at probe k values, Planck tilt):")
print("    k [Mpc^-1] | P_zeta(k)   | S_IC(k)     | W_mu(k) | W_mu*S_IC")
probe_ks = [46.0, 100.0, 150.0, 300.0, 740.0, 1000.0, 3000.0]                # (local)
for k_probe in probe_ks:
    print(f"    {k_probe:>9.1f} | {P_zeta(k_probe):.3e}  | "
          f"{S_IC(k_probe):.3e}  | {W_mu(k_probe):.3f}  | "
          f"{W_mu(k_probe) * S_IC(k_probe):.3e}")

# ============================================================
# SECTION 3: Chluba-kernel-weighted mu-distortion integral
# ============================================================
print("\n[SEC 3] Chluba-kernel-weighted mu integral")
print("  Formula (S79 P2-B C2, L655):")
print("    mu = 2.27 * int d(ln k) * P_zeta(k) * S_IC(k) * W_mu(k)/W_peak")
print("    over k in [10, 3e4] Mpc^-1 (S79 P2-B C2 integration range)")

# Integration grid
k_min_int = 10.0                   # (local) IR edge of Chluba plateau shoulder
k_max_int = 3.0e4                  # (local) UV edge of Chluba plateau shoulder
N_grid = 5000                      # (local) dense for trapezoid convergence
lnk_arr = np.linspace(np.log(k_min_int), np.log(k_max_int), N_grid)          # (local)
k_arr = np.exp(lnk_arr)                                                      # (local)

# Integrand with tilt (canonical Planck n_s)
P_arr = P_zeta(k_arr)                                                        # (local)
S_arr = S_IC(k_arr)                                                          # (local)
W_arr = W_mu(k_arr)                                                          # (local)
W_norm_arr = W_arr / W_peak                                                  # (local)
integrand = P_arr * S_arr * W_norm_arr                                       # (local)

mu_tilted = 2.27 * float(np.trapezoid(integrand, lnk_arr))                   # (local)

# Flat P_zeta case (reproduces S79 P2-B exact reference: 6.17e-10)
integrand_flat = A_s_CMB * S_arr * W_norm_arr                                # (local)
mu_flat = 2.27 * float(np.trapezoid(integrand_flat, lnk_arr))                # (local)

# S79 P2-B reference value
mu_S79_ref = 6.17e-10                                                        # (local) canonical P2-B C2

print(f"\n  mu (Planck tilt, n_s={planck_ns:.4f})  = {mu_tilted:.3e}")
print(f"  mu (flat P_zeta = A_s_obs)       = {mu_flat:.3e}")
print(f"  S79 P2-B reference value          = {mu_S79_ref:.3e}")
print(f"  ratio (tilted / S79 ref)          = {mu_tilted/mu_S79_ref:.4f}")
print(f"  ratio (flat    / S79 ref)         = {mu_flat/mu_S79_ref:.4f}")

# ============================================================
# SECTION 4: Contribution by decade (for E-space/k-space diagnostic)
# ============================================================
print("\n[SEC 4] Contribution by k-decade (mu density per d(ln k))")
decades = [(10, 100), (100, 1000), (1000, 10000), (10000, 30000)]            # (local)
mu_by_decade = {}                                                            # (local)
for k_lo, k_hi in decades:
    mask = (k_arr >= k_lo) & (k_arr <= k_hi)                                 # (local)
    if mask.sum() > 1:
        mu_contrib = 2.27 * float(np.trapezoid(
            integrand[mask], lnk_arr[mask]))                                 # (local)
        mu_by_decade[f"{k_lo}-{k_hi}"] = mu_contrib
        pct = 100.0 * mu_contrib / mu_tilted                                 # (local)
        print(f"  k in [{k_lo:>5d}, {k_hi:>5d}] Mpc^-1: "
              f"delta_mu = {mu_contrib:.3e}  ({pct:5.1f}% of total)")

# ============================================================
# SECTION 5: Verdict evaluation
# ============================================================
print("\n[SEC 5] Pre-registered gate verdict")
print(f"  PASS band: factor 3 around 6.17e-10 -> mu in [{mu_S79_ref/3:.3e}, "
      f"{mu_S79_ref*3:.3e}]")
print(f"  INFO band: factor 3-10              -> mu in [{mu_S79_ref/10:.3e}, "
      f"{mu_S79_ref*10:.3e}] \\ PASS band")
print(f"  FAIL band: > factor 10")

# Use tilted result as canonical value (physical: Planck-like tilt)
mu_canonical = mu_tilted                                                     # (local)
ratio = mu_canonical / mu_S79_ref                                            # (local)
log10_ratio = np.log10(ratio)                                                # (local)
abs_log10_ratio = abs(log10_ratio)                                           # (local)
log10_3 = np.log10(3.0)                                                      # (local)

if abs_log10_ratio < log10_3:
    verdict = "PASS"                                                         # (local)
    band = f"within factor 3 (|log10|={abs_log10_ratio:.3f} < {log10_3:.3f})"  # (local)
elif abs_log10_ratio < 1.0:
    verdict = "INFO"                                                         # (local)
    band = f"factor 3-10 (|log10|={abs_log10_ratio:.3f})"                    # (local)
else:
    verdict = "FAIL"                                                         # (local)
    band = f"> factor 10 (|log10|={abs_log10_ratio:.3f})"                    # (local)

print(f"\n  mu_canonical (Planck tilt) = {mu_canonical:.4e}")
print(f"  mu/mu_ref                  = {ratio:.4f}")
print(f"  |log10(mu/mu_ref)|         = {abs_log10_ratio:.4f}")
print(f"  Verdict                    = {verdict}  [{band}]")

# FIRAS margin (for contextual reporting)
FIRAS_bound = 9.0e-5                                                         # (local) Fixsen+ 1996
firas_margin_oom = np.log10(FIRAS_bound / mu_canonical)                      # (local)
print(f"\n  FIRAS bound (Fixsen 1996)  = {FIRAS_bound:.1e}")
print(f"  FIRAS margin (OOM)         = {firas_margin_oom:.2f}  "
      f"(mu is {firas_margin_oom:.2f} decades below bound)")

# ============================================================
# SECTION 6: Save NPZ + generate plot
# ============================================================
print("\n[SEC 6] Save NPZ + plot")

npz_path = os.path.join(HERE, 's82_w2_14_firas_chluba_full.npz')             # (local)
np.savez(npz_path,
         # Kernel
         k_D_mu=k_D_mu,
         k_D_th=k_D_th,
         k_peak=k_peak,
         W_peak=W_peak,
         # Envelopes (anchors)
         k_pivot=k_pivot,
         A_s_obs=A_s_CMB,
         n_s=planck_ns,
         S_IC_0=S_IC_0,
         alpha_S_IC=alpha_S_IC,
         beta_sq_0=beta_sq_0,
         alpha_beta=alpha_beta,
         # Integration grid
         k_arr=k_arr,
         lnk_arr=lnk_arr,
         P_arr=P_arr,
         S_arr=S_arr,
         W_arr=W_arr,
         integrand=integrand,
         # Results
         mu_tilted=mu_tilted,
         mu_flat=mu_flat,
         mu_S79_ref=mu_S79_ref,
         mu_canonical=mu_canonical,
         ratio=ratio,
         log10_ratio=log10_ratio,
         firas_margin_oom=firas_margin_oom,
         FIRAS_bound=FIRAS_bound,
         # Decade-by-decade
         mu_by_decade=json.dumps(mu_by_decade),
         # Verdict metadata
         verdict=verdict,
         scheme='CHLUBA-2012',
         convention='FIRAS',
         L_max='N/A',
         )
print(f"  NPZ: {npz_path}")

# ---- Plot: kernel + S_IC envelope + integrand vs k (3 stacked panels) ----
fig, axes = plt.subplots(3, 1, figsize=(9, 10), sharex=True)

# Panel 1: Chluba kernel W_mu(k)
ax = axes[0]
ax.semilogx(k_arr, W_arr, 'b-', lw=2, label=r'$W_\mu(k)$ (Chluba 2012)')
ax.axvline(k_peak, color='k', ls=':', alpha=0.5,
           label=rf'$k_{{peak}}$ = {k_peak:.1f} Mpc$^{{-1}}$')
ax.axvline(k_D_mu, color='gray', ls='--', alpha=0.5,
           label=rf'$k_D^\mu$ = {k_D_mu:.0f}')
ax.axvline(k_D_th, color='gray', ls='--', alpha=0.5,
           label=rf'$k_D^{{th}}$ = {k_D_th:.0e}')
ax.set_ylabel(r'$W_\mu(k)$')
ax.set_title('Chluba 2012 Eq. 10 mu-distortion window function')
ax.legend(fontsize=9, loc='lower center')
ax.grid(alpha=0.3)
ax.set_ylim(-0.05, 1.1)

# Panel 2: Framework envelopes S_IC(k) and P_zeta(k)
ax = axes[1]
ax.loglog(k_arr, S_arr, 'r-', lw=2, label=r'$S_{IC}(k)$ (B3 occupation)')
ax.loglog(k_arr, beta_sq(k_arr), 'm--', lw=1.5,
          label=r'$|\beta|^2(k)$ (B1 impulse)')
ax.loglog(k_arr, P_arr * 1e9, 'g:', lw=1.5,
          label=r'$P_\zeta(k) \times 10^9$ (Planck tilt)')
ax.axhline(1.0, color='k', ls=':', alpha=0.3, label=r'$S_{IC} = 1$ crossover')
ax.set_ylabel('Amplitude')
ax.set_title('Framework envelopes (S79 P2-B C1 UV-extrapolated, anchored at k_pivot)')
ax.legend(fontsize=9)
ax.grid(alpha=0.3, which='both')

# Panel 3: Integrand P_zeta * S_IC * W_mu/W_peak vs k
ax = axes[2]
ax.loglog(k_arr, integrand, 'purple', lw=2,
          label=r'$P_\zeta(k) \cdot S_{IC}(k) \cdot W_\mu(k)/W_{peak}$')
# Mark kernel plateau
ax.axvspan(100, 3000, alpha=0.15, color='blue',
           label='Chluba plateau (W_mu > 0.99)')
ax.axvline(k_peak, color='k', ls=':', alpha=0.5)
ax.set_xlabel(r'$k$ [Mpc$^{-1}$]')
ax.set_ylabel('integrand')
ax.set_title(rf'mu integrand: total mu = {mu_canonical:.3e} '
             rf'(ratio to S79 = {ratio:.3f}, verdict = {verdict})')
ax.legend(fontsize=9)
ax.grid(alpha=0.3, which='both')

plt.tight_layout()
png_path = os.path.join(HERE, 's82_w2_14_firas_chluba_full.png')             # (local)
plt.savefig(png_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"  PNG: {png_path}")

# ============================================================
# SECTION 7: Closure SHA-256 and 4-tuple output tag
# ============================================================
print("\n[SEC 7] Closure SHA-256 (ordered input-pin map)")

# Ordered input-pin map (canonical closure over inputs)
closure_map = {k: INPUT_SHAS.get(k, '') for k in sorted(INPUT_SHAS.keys())}   # (local)
closure_blob = json.dumps(closure_map, sort_keys=True).encode()               # (local)
closure_sha = hashlib.sha256(closure_blob).hexdigest()                        # (local)

print(f"  closure_sha256 = {closure_sha}")

# ============================================================
# SECTION 8: 4-tuple output tag + verdict line
# ============================================================
print("\n[SEC 8] Final 4-tuple output tag (canonical)")
print(f"  value      = {mu_canonical:.6e}")
print(f"  scheme     = CHLUBA-2012")
print(f"  convention = FIRAS")
print(f"  L_max      = N/A")
print(f"  sha256     = {closure_sha}")
print(f"  verdict    = {verdict}")

verdict_line = (
    f"S82-FIRAS-CHLUBA-FULL: {verdict} -- "
    f"value={mu_canonical:.6e} "
    f"scheme=CHLUBA-2012 "
    f"convention=FIRAS "
    f"L_max=N/A "
    f"sha256={closure_sha}"
)

verdict_path = os.path.join(HERE, 's82_gate_verdicts.txt')                    # (local)
with open(verdict_path, 'a') as fv:
    fv.write(verdict_line + "\n")

print(f"\n  Verdict appended to {verdict_path}:")
print(f"    {verdict_line}")

print("\n" + "=" * 70)
print("S82 W2-14 FIRAS-CHLUBA-FULL complete.")
print("=" * 70)
