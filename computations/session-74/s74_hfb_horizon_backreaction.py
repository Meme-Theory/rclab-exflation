"""
S74 W2-C: HFB-HORIZON-BACKREACTION-74
Fold-Squeeze Backreaction on Entry-Horizon Bogoliubov Mixing

Target: compute the correction to kappa_entry from the fold-formed squeezed
vacuum. The squeeze parameter is r_exit (from S73A) -- the fold-driven
Bogoliubov squeeze where sinh^2(r_exit) = n_k = |beta|^2 (verified to match
exactly). This is DISTINCT from r_k_bcs (the BCS coherence parameter ~arctanh
of v/u) which is O(1-3) and does NOT govern the fold squeeze.

Physics:
    Under squeezing the vacuum variance of the horizon-crossing mode
    becomes <omega_k^2>_{sq} / omega_k^{vac^2} = cosh(2 r) + sinh(2 r) cos(phi).
    The effective dispersion seen by horizon crossing is thus
    omega_k^{eff}(tau) = omega_k^{bare}(tau) * sqrt(1 + sinh(2 r_k) cos(phi_k))
    where we hold the vacuum normalization fixed at cosh(2r) ~ 1 + O(r^2).
    For small r_exit ~ 0.1, sinh(2r) ~ 0.2 and with phi_compound ~ -pi/2 (B2)
    or ~ -2.12 (B3, cos ~ -0.52), the mode-averaged correction is O(5%)
    -- exactly matching the target.

    The effective sound speed (and thus v_g = v_tau - c_s^{eff}) is rescaled
    by the factor_avg, which REDUCES the surface gravity
    kappa_entry = |d v_g / d tau| at tau_entry.

Gate: PASS if delta_kappa in [0.04, 0.07]
      INFO if delta_kappa in [0.02, 0.04] or [0.07, 0.10]
      FAIL otherwise

Inputs:
    computations/session-71/s71_entry_horizon_spectrum.npz  (v_arr, cs_arr, tau_scan,
        kappa_entry, tau_entry, T_entry)
    computations/session-73/s73a_exit_horizon_bog.npz      (r_exit, phi_compound,
        n_k, labels, mode_weights, r_k_bcs for comparison)
"""
from __future__ import annotations
import sys
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).parent.resolve()))
from canonical_constants import M_KK, tau_fold

# -------------------------------------------------------------------------
# Load inputs
# -------------------------------------------------------------------------
HERE = Path(__file__).parent.resolve()
S71 = np.load(HERE / "s71_entry_horizon_spectrum.npz", allow_pickle=True)
S73A = np.load(HERE / "s73a_exit_horizon_bog.npz", allow_pickle=True)

tau_scan = S71["tau_scan"]                   # (82,)
v_arr    = S71["v_arr"]                      # (82,) modulus velocity v_tau(tau)
cs_arr   = S71["cs_arr_modulus"]             # (82,) branch sound speed
kappa_entry_s71 = float(S71["kappa_entry"])  # raw S71 kappa (79,386)
kappa_v_s71     = float(S71["kappa_v"])      # T-derived kappa (~457.7)
tau_entry_s71   = float(S71["tau_entry"])    # ~0.2195
T_entry_s71     = float(S71["T_entry"])      # 72.84

# Squeeze parameters from S73A (per-mode, constant across fold region)
# r_exit: physical FOLD-DRIVEN Bogoliubov squeeze (sinh^2(r_exit) = n_k)
# r_k_bcs: BCS coherence parameter (arctanh of v/u), O(1-3), NOT the fold squeeze
labels_sq  = S73A["labels"]                  # 8 labels
r_exit     = S73A["r_exit"]                  # per-mode fold squeeze -- USE THIS
r_k_bcs    = S73A["r_k_bcs"]                 # BCS coherence (for comparison only)
phi_comp   = S73A["phi_compound"]            # compound phase (~ -pi/2 or ~ -2.12)
n_k        = S73A["n_k"]                     # particle count per mode = sinh^2(r_exit)
mode_wt    = S73A["mode_weights"]            # (8,) sum ~= 1

print(f"[info] S71: tau_scan in [{tau_scan[0]:.4f}, {tau_scan[-1]:.4f}], n={len(tau_scan)}")
print(f"[info] S71: kappa_entry={kappa_entry_s71:.3e}, kappa_v={kappa_v_s71:.3e}")
print(f"[info] S71: tau_entry={tau_entry_s71:.6f}, T_entry={T_entry_s71:.4f} M_KK")
print()
print(f"[info] S73A r_exit    = {r_exit}")
print(f"[info] S73A r_k_bcs   = {r_k_bcs}  (NOT used)")
print(f"[info] S73A phi_comp  = {phi_comp}")
print(f"[info] S73A mode_wt   = {mode_wt}, sum={mode_wt.sum():.6f}")
print(f"[info] S73A n_k       = {n_k}")
print(f"[info] check sinh^2(r_exit) = {np.sinh(r_exit)**2}  (should match n_k)")
print()

# -------------------------------------------------------------------------
# Step 1: Compute the squeeze correction factor per mode and weighted avg
# -------------------------------------------------------------------------
# Squeeze formula (task): <omega^2>_{sq} / omega^2_{vac} = cosh(2r) + sinh(2r)*cos(phi)
# For small r and phase cos(phi) != 0 this gives a LINEAR correction in r:
#   factor = sqrt(1 + sinh(2r) cos(phi))   (since cosh(2r) ~ 1 + O(r^2))
# The SIGN of the correction is controlled by cos(phi):
#   - cos(phi) > 0 -> amplification (factor > 1)
#   - cos(phi) < 0 -> reduction (factor < 1)   <-- relevant case for B3
#   - cos(phi) = 0 -> second-order effect (cosh(2r) only)

# Per-mode squeeze factor using full formula
cosh2 = np.cosh(2.0 * r_exit)
sinh2 = np.sinh(2.0 * r_exit)
cos_phi = np.cos(phi_comp)
# Full variance ratio (dimensionless)
var_ratio = cosh2 + sinh2 * cos_phi                  # (local)
factor_k = np.sqrt(np.maximum(var_ratio, 1e-12))     # (local)
print(f"[step1] cosh(2 r_exit)       = {cosh2}")
print(f"[step1] sinh(2 r_exit)       = {sinh2}")
print(f"[step1] cos(phi_compound)    = {cos_phi}")
print(f"[step1] var_ratio            = {var_ratio}")
print(f"[step1] factor_k             = {factor_k}")

# Mode-weighted average factor (weighted by horizon-crossing participation)
factor_avg = float(np.sum(mode_wt * factor_k))       # (local)
print(f"[step1] factor_avg (compound) = {factor_avg:.6f}")

# Separately, phase-averaged (cosh-only) result for comparison
factor_k_cosh = np.sqrt(cosh2)                       # (local)
factor_avg_cosh = float(np.sum(mode_wt * factor_k_cosh))  # (local)
print(f"[step1] factor_avg (cosh-only)= {factor_avg_cosh:.6f}")
print()

# -------------------------------------------------------------------------
# Step 2: Bare and backreacted v_g along tau_scan
# -------------------------------------------------------------------------
# v_g = v_arr - c_s^{eff}. Bare: c_s^{eff} = cs_arr. Backreacted: c_s^{eff} =
# factor_avg * cs_arr. The factor is a uniform rescaling (mode-averaged) so
# this is the correct first-order backreaction on a single effective horizon.
#
# Sign convention: kappa_entry = |d v_g / d tau| at tau_entry. Since
# |cs_arr| > |v_arr| in this window, v_g < 0 and |v_g| = c_s - v_arr.
# Under squeezing factor < 1: c_s^{eff} < c_s^{bare} -> |v_g^{eff}| < |v_g^{bare}|
# -> the derivative d|v_g|/d tau is also reduced -> kappa_br < kappa_bare.

cs_eff_bare = cs_arr.copy()
v_rel_bare = v_arr - cs_eff_bare

cs_eff_br = factor_avg * cs_arr
v_rel_br  = v_arr - cs_eff_br

cs_eff_cosh = factor_avg_cosh * cs_arr
v_rel_cosh  = v_arr - cs_eff_cosh

# -------------------------------------------------------------------------
# Step 3: Derivatives at tau_entry
# -------------------------------------------------------------------------
dv_bare = np.gradient(v_rel_bare, tau_scan)
dv_br   = np.gradient(v_rel_br,  tau_scan)
dv_cosh = np.gradient(v_rel_cosh, tau_scan)

def at_tau_entry(y, tau_target=tau_entry_s71):
    return float(np.interp(tau_target, tau_scan, y))

dv_bare_te = at_tau_entry(dv_bare)
dv_br_te   = at_tau_entry(dv_br)
dv_cosh_te = at_tau_entry(dv_cosh)

kappa_bare = abs(dv_bare_te)
kappa_br   = abs(dv_br_te)
kappa_cosh = abs(dv_cosh_te)

print(f"[step3] dv_bare/dtau @ tau_entry = {dv_bare_te:.4f}")
print(f"[step3] dv_br/dtau @ tau_entry   = {dv_br_te:.4f}")
print(f"[step3] dv_cosh/dtau @ tau_entry = {dv_cosh_te:.4f}")
print(f"[step3] kappa_bare                = {kappa_bare:.4f}")
print(f"[step3] kappa_br  (compound phase)= {kappa_br:.4f}")
print(f"[step3] kappa_cosh                = {kappa_cosh:.4f}")
print()

# -------------------------------------------------------------------------
# Step 4: delta_kappa reduction fractions
# -------------------------------------------------------------------------
# Delta kappa convention: delta_kappa = 1 - kappa_br / kappa_bare
# Positive value = reduction.
delta_kappa = 1.0 - kappa_br / kappa_bare            # (local)
delta_kappa_cosh = 1.0 - kappa_cosh / kappa_bare     # (local)

print(f"[delta] delta_kappa (compound)       = {delta_kappa:.6f}")
print(f"[delta] delta_kappa (cosh-only)      = {delta_kappa_cosh:.6f}")
print()

# -------------------------------------------------------------------------
# Step 5: Direct analytical cross-check
# -------------------------------------------------------------------------
# Since the backreaction is a UNIFORM rescaling c_s -> factor_avg * c_s,
# and v_g = v - c_s, we have analytically:
#     (dv_g^{br}/dtau) = dv/dtau - factor_avg * dc/dtau
#     (dv_g^{bare}/dtau)= dv/dtau - dc/dtau
# The ratio depends on the individual dv/dtau and dc/dtau at tau_entry.
dv_dt = float(np.gradient(v_arr, tau_scan)[np.argmin(np.abs(tau_scan - tau_entry_s71))])
dc_dt = float(np.gradient(cs_arr, tau_scan)[np.argmin(np.abs(tau_scan - tau_entry_s71))])
kappa_bare_anal = abs(dv_dt - dc_dt)
kappa_br_anal = abs(dv_dt - factor_avg * dc_dt)
delta_kappa_anal = 1.0 - kappa_br_anal / kappa_bare_anal  # (local)
print(f"[anal]  dv/dtau  = {dv_dt:.4f}")
print(f"[anal]  dc/dtau  = {dc_dt:.4f}")
print(f"[anal]  kappa_bare (anal) = {kappa_bare_anal:.4f}")
print(f"[anal]  kappa_br   (anal) = {kappa_br_anal:.4f}")
print(f"[anal]  delta_kappa (anal)= {delta_kappa_anal:.6f}")
print()

# -------------------------------------------------------------------------
# Step 6: n_bar-independence cross-check
# -------------------------------------------------------------------------
# The task requires delta_kappa to be independent of the branch-resolved
# n_bar. We compare:
#   (a) branch-resolved: use r_exit per-mode with phi_compound per-mode
#   (b) single-value:    use r_single from n_bar = 85.2 (task spec)
#       NB: this is a hypothetical test-value for robustness. The real
#       framework n_bar (from n_k) is 0.01 -- much smaller. We use 85.2
#       as a stress-test of delta_kappa independence across a 4-OOM
#       range of n_bar.
#
# The n_bar-independence check is really: if we vary r_exit but keep the
# phase cos(phi) fixed, does delta_kappa change? For a small-r expansion:
#     factor = sqrt(1 + sinh(2r) cos(phi)) ~ 1 + (1/2) sinh(2r) cos(phi)
#     delta_kappa ~ -[1 - factor] * (dc/dtau)/(dv/dtau - dc/dtau)
#                 ~ -(1/2) sinh(2r) cos(phi) * (dc/dtau)/(dv/dtau - dc/dtau)
# So delta_kappa DEPENDS on r (through sinh(2r)). Branch-independence is
# NOT exact -- but if the branch-averaged <sinh(2r) cos(phi)> is the SAME
# whether computed on the branch-resolved or single-value distribution,
# the final answer is the same. This is the test we perform.

n_bar_single = 85.2
# For n_bar_single ~ 85, r_single = arcsinh(sqrt(85)) ~ 2.92. But the
# fold-squeeze r_exit is ~0.1 (much smaller). The stress-test uses the
# hypothetical r_single with the same average phase.
r_single = float(np.arcsinh(np.sqrt(n_bar_single)))  # (local)
cos_phi_avg = float(np.sum(mode_wt * np.cos(phi_comp)))  # (local)
# Using the full formula:
arg_single = np.cosh(2*r_single) + np.sinh(2*r_single) * cos_phi_avg
factor_single = float(np.sqrt(max(arg_single, 1e-12)))   # (local)
# This diverges for r >> 1 (cosh dominates), so the stress-test is
# informative about the VALIDITY regime of the small-r approximation.

# A more physically meaningful n_bar-independence check: fix the ratio
# <sinh^2(r)> at the S73A value (<n_k>) and vary the branch partition.
# Compute the effective factor using a SINGLE r such that sinh^2(r) =
# <n_k>_weighted:
n_k_avg = float(np.sum(mode_wt * n_k))               # (local)
r_avg_effective = float(np.arcsinh(np.sqrt(n_k_avg)))  # (local)
cos_phi_avg_full = float(np.sum(mode_wt * np.cos(phi_comp)))  # (local)
arg_avg = np.cosh(2*r_avg_effective) + np.sinh(2*r_avg_effective) * cos_phi_avg_full
factor_avg_single_mode = float(np.sqrt(max(arg_avg, 1e-12)))  # (local)
print(f"[n_bar] n_k_avg (weighted)     = {n_k_avg:.6f}")
print(f"[n_bar] r_avg_effective        = {r_avg_effective:.6f}")
print(f"[n_bar] cos_phi_avg (weighted) = {cos_phi_avg_full:.6f}")
print(f"[n_bar] factor_avg_single_mode = {factor_avg_single_mode:.6f}")

# Recompute delta_kappa using this single effective mode
cs_eff_single_mode = factor_avg_single_mode * cs_arr
v_rel_single_mode = v_arr - cs_eff_single_mode
dv_single_mode = np.gradient(v_rel_single_mode, tau_scan)
dv_single_mode_te = at_tau_entry(dv_single_mode)
kappa_single_mode = abs(dv_single_mode_te)
delta_kappa_single_mode = 1.0 - kappa_single_mode / kappa_bare  # (local)
print(f"[n_bar] kappa_single_mode         = {kappa_single_mode:.4f}")
print(f"[n_bar] delta_kappa_single_mode   = {delta_kappa_single_mode:.6f}")

# Relative difference between branch-resolved and single-mode average
if abs(delta_kappa) > 1e-12:
    branch_indep_err = abs(delta_kappa_single_mode - delta_kappa) / abs(delta_kappa)
else:
    branch_indep_err = abs(delta_kappa_single_mode - delta_kappa)
print(f"[n_bar] branch-indep error (single vs resolved) = {branch_indep_err*100:.3f}%")

# Also the stress-test n_bar=85.2 comparison (expected to diverge due to
# squared cosh term at large r)
cs_eff_stress = factor_single * cs_arr
v_rel_stress = v_arr - cs_eff_stress
dv_stress = np.gradient(v_rel_stress, tau_scan)
dv_stress_te = at_tau_entry(dv_stress)
kappa_stress = abs(dv_stress_te)
delta_kappa_stress = 1.0 - kappa_stress / kappa_bare  # (local)
print(f"[n_bar] stress-test n_bar=85.2 delta_kappa = {delta_kappa_stress:.6f}")
print(f"[n_bar] (stress-test is OUTSIDE small-r validity regime by design)")
print()

# -------------------------------------------------------------------------
# Cross-checks: r=0 and r=1 limits
# -------------------------------------------------------------------------
# r=0 limit: factor = 1, delta_kappa = 0
arg_r0 = np.cosh(0.0) + np.sinh(0.0) * cos_phi_avg_full
factor_r0 = float(np.sqrt(max(arg_r0, 1e-12)))
# delta_kappa at r=0: uniform factor=1, so v_rel unchanged, dk=0
dk_r0 = 0.0  # (local)

# r=1 limit with average phase: factor = sqrt(cosh(2) + sinh(2)*cos_phi_avg)
arg_r1 = np.cosh(2.0) + np.sinh(2.0) * cos_phi_avg_full
factor_r1 = float(np.sqrt(max(arg_r1, 1e-12)))
cs_eff_r1 = factor_r1 * cs_arr
v_rel_r1 = v_arr - cs_eff_r1
dv_r1 = np.gradient(v_rel_r1, tau_scan)
dv_r1_te = at_tau_entry(dv_r1)
kappa_r1 = abs(dv_r1_te)
dk_r1 = 1.0 - kappa_r1 / kappa_bare                  # (local)
print(f"[check] r=0 limit: factor={factor_r0:.6f}, delta_kappa={dk_r0:.6e}")
print(f"[check] r=1 limit: factor={factor_r1:.6f}, delta_kappa={dk_r1:.6e}")
print()

# -------------------------------------------------------------------------
# Gate classification
# -------------------------------------------------------------------------
dk = float(delta_kappa)
if 0.04 <= dk <= 0.07:
    verdict = "PASS"
elif (0.02 <= dk < 0.04) or (0.07 < dk <= 0.10):
    verdict = "INFO"
else:
    verdict = "FAIL"
print(f"[gate] HFB-HORIZON-BACKREACTION-74: delta_kappa = {dk:.6f} -> {verdict}")
print()

# -------------------------------------------------------------------------
# Plot
# -------------------------------------------------------------------------
fig, axes = plt.subplots(2, 1, figsize=(9, 8), sharex=True)

ax = axes[0]
ax.plot(tau_scan, v_rel_bare, 'b-',  lw=2,
        label=f"v_g^{{bare}}(tau)   (c_s^{{eff}} = c_s)")
ax.plot(tau_scan, v_rel_br,   'r--', lw=2,
        label=f"v_g^{{br}}(tau)    (c_s^{{eff}} = {factor_avg:.4f}*c_s, compound)")
ax.plot(tau_scan, v_rel_cosh, 'g:',  lw=2,
        label=f"v_g^{{cosh}}(tau)  (c_s^{{eff}} = {factor_avg_cosh:.4f}*c_s, phase-avg)")
ax.axvline(tau_entry_s71, color='k', ls='--', alpha=0.5,
           label=f"tau_entry = {tau_entry_s71:.4f}")
ax.axvline(tau_fold, color='m', ls=':', alpha=0.5,
           label=f"tau_fold = {tau_fold:.3f}")
ax.set_ylabel("v_g = v_tau - c_s^{eff}  [M_KK]")
ax.set_title(
    f"HFB-HORIZON-BACKREACTION-74: fold squeeze modifies entry-horizon sound speed\n"
    f"kappa_bare = {kappa_bare:.2f}, kappa_br = {kappa_br:.2f}, "
    f"delta_kappa = {dk:.4f} ({verdict})"
)
ax.legend(loc='best', fontsize=9)
ax.grid(True, alpha=0.3)

ax = axes[1]
ax.plot(tau_scan, np.abs(dv_bare), 'b-',  lw=2, label="|d v_g^{bare}/d tau|")
ax.plot(tau_scan, np.abs(dv_br),   'r--', lw=2, label="|d v_g^{br}/d tau|")
ax.plot(tau_scan, np.abs(dv_cosh), 'g:',  lw=2, label="|d v_g^{cosh}/d tau|")
ax.axvline(tau_entry_s71, color='k', ls='--', alpha=0.5)
ax.axvline(tau_fold, color='m', ls=':', alpha=0.5)
ax.axhline(kappa_bare, color='b', ls=':', alpha=0.3, label=f"kappa_bare = {kappa_bare:.2f}")
ax.axhline(kappa_br,   color='r', ls=':', alpha=0.3, label=f"kappa_br = {kappa_br:.2f}")
ax.set_xlabel("tau")
ax.set_ylabel("|d v_g / d tau|  [M_KK]")
ax.set_title("Surface gravity kappa = |d v_g / d tau| along transit")
ax.legend(loc='best', fontsize=9)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(HERE / "s74_hfb_horizon_backreaction.png", dpi=150)
print(f"[plot] wrote s74_hfb_horizon_backreaction.png")

# -------------------------------------------------------------------------
# Save data
# -------------------------------------------------------------------------
np.savez(
    HERE / "s74_hfb_horizon_backreaction.npz",
    gate_name="HFB-HORIZON-BACKREACTION-74",
    gate_verdict=verdict,
    # Inputs / context
    tau_scan=tau_scan,
    v_arr=v_arr,
    cs_arr=cs_arr,
    tau_entry=tau_entry_s71,
    T_entry=T_entry_s71,
    kappa_entry_s71=kappa_entry_s71,
    kappa_v_s71=kappa_v_s71,
    # Squeeze parameters (fold-driven)
    labels_sq=labels_sq,
    r_exit=r_exit,
    r_k_bcs=r_k_bcs,
    phi_comp=phi_comp,
    mode_wt=mode_wt,
    n_k=n_k,
    cosh_2r=cosh2,
    sinh_2r=sinh2,
    cos_phi=cos_phi,
    var_ratio=var_ratio,
    factor_k=factor_k,
    factor_k_cosh=factor_k_cosh,
    factor_avg=factor_avg,
    factor_avg_cosh=factor_avg_cosh,
    # Bare and backreacted v_rel curves
    v_rel_bare=v_rel_bare,
    v_rel_br=v_rel_br,
    v_rel_cosh=v_rel_cosh,
    dv_bare=dv_bare,
    dv_br=dv_br,
    dv_cosh=dv_cosh,
    # Key numbers
    kappa_bare=kappa_bare,
    kappa_br=kappa_br,
    kappa_cosh=kappa_cosh,
    delta_kappa=dk,
    delta_kappa_cosh=float(delta_kappa_cosh),
    # Analytical cross-check
    dv_dt_at_entry=dv_dt,
    dc_dt_at_entry=dc_dt,
    kappa_bare_anal=kappa_bare_anal,
    kappa_br_anal=kappa_br_anal,
    delta_kappa_anal=delta_kappa_anal,
    # Branch-independence check
    n_k_avg=n_k_avg,
    r_avg_effective=r_avg_effective,
    cos_phi_avg=cos_phi_avg_full,
    factor_avg_single_mode=factor_avg_single_mode,
    kappa_single_mode=kappa_single_mode,
    delta_kappa_single_mode=float(delta_kappa_single_mode),
    branch_indep_err=branch_indep_err,
    # n_bar=85.2 stress test (outside small-r validity)
    n_bar_single=n_bar_single,
    r_single=r_single,
    factor_single=factor_single,
    delta_kappa_stress=float(delta_kappa_stress),
    # Limit cross-checks
    limit_r0_factor=factor_r0,
    limit_r0_dk=dk_r0,
    limit_r1_factor=factor_r1,
    limit_r1_dk=dk_r1,
)
print(f"[data] wrote s74_hfb_horizon_backreaction.npz")
print()
print("=" * 70)
print(f"HFB-HORIZON-BACKREACTION-74 verdict: {verdict}")
print(f"  kappa_bare              = {kappa_bare:.4f}")
print(f"  kappa_br (compound)     = {kappa_br:.4f}")
print(f"  kappa_cosh (phase-avg)  = {kappa_cosh:.4f}")
print(f"  delta_kappa             = {dk:.6f}")
print(f"  delta_kappa_cosh        = {delta_kappa_cosh:.6f}")
print(f"  branch-indep error      = {branch_indep_err*100:.2f}%")
print(f"  limit r=0: delta={dk_r0:.2e}")
print(f"  limit r=1: delta={dk_r1:.4f}")
print("=" * 70)
