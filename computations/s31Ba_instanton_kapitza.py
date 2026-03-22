#!/usr/bin/env python3
"""
Session 31A — I-1: Instanton-Kapitza Frequency Ratio

Computes the instanton tunneling rate Gamma_inst(tau) and compares it
to the modulus rolling frequency omega_tau = sqrt(|d^2V/dtau^2|).

The instanton action on Jensen-deformed SU(3):
  S_inst(tau) = alpha_grav * (-R(tau)) + alpha_YM * K(tau)

where R(tau) is the scalar curvature and K(tau) is the Kretschner scalar
(exact analytic formulas from Permanent Results Registry Section III).

The tunneling rate:
  Gamma_inst(tau) ~ exp(-S_inst(tau))

Gate I-1: PASS if Gamma_inst/omega_tau > 3 at some tau in [0.05, 0.55]
          for any coupling ratio alpha_YM/alpha_grav.

Inputs:
  - Analytic curvature formulas (R, K from Session 17b)
  - s30b_grid_bcs.npz (V_total for omega_tau)

Outputs:
  - s31a_instanton_kapitza.npz
  - s31a_instanton_kapitza.png

Author: phonon-exflation-sim agent (Session 31A)
Date: 2026-03-02
"""

import numpy as np
from scipy.interpolate import RectBivariateSpline
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

# ── Paths ────────────────────────────────────────────────────────────────
ROOT = r"C:\sandbox\Ainulindale Exflation"
T0 = os.path.join(ROOT, "tier0-computation")

# ── Exact curvature invariants (Permanent Results Registry, Section III) ─
# Verified at machine epsilon across 51 tau-values. Session 17b.

def R_scalar(tau):
    """Scalar curvature on Jensen-deformed SU(3). R(0) = 2."""
    t = np.asarray(tau, dtype=float)
    return (-(1.0/4)*np.exp(-4*t) + 2*np.exp(-t) - 1.0/4 + (1.0/2)*np.exp(2*t))

def K_kretschner(tau):
    """Kretschner scalar K = R_{abcd} R^{abcd} on Jensen SU(3). K(0) = 0.5."""
    t = np.asarray(tau, dtype=float)
    return ((23.0/96)*np.exp(-8*t) - np.exp(-5*t) + (5.0/16)*np.exp(-4*t)
            + (11.0/6)*np.exp(-2*t) - (3.0/2)*np.exp(-t) + 17.0/32
            + (1.0/12)*np.exp(4*t))

def Ric_sq(tau):
    """|Ric|^2 on Jensen SU(3). |Ric|^2(0) = 0.5."""
    t = np.asarray(tau, dtype=float)
    return ((1.0/12)*np.exp(-8*t) - (1.0/2)*np.exp(-5*t) + (1.0/8)*np.exp(-4*t)
            + (13.0/12)*np.exp(-2*t) - (1.0/2)*np.exp(-t) + 1.0/8
            + (1.0/12)*np.exp(4*t))

def Weyl_sq(tau):
    """|C|^2 (Weyl squared) on Jensen SU(3)."""
    t = np.asarray(tau, dtype=float)
    return ((377.0/2016)*np.exp(-8*t) - (5.0/7)*np.exp(-5*t)
            + (79.0/336)*np.exp(-4*t) + (325.0/252)*np.exp(-2*t)
            - (17.0/14)*np.exp(-t) + 101.0/224
            + (2.0/21)*np.exp(t) - (1.0/84)*np.exp(2*t)
            + (5.0/126)*np.exp(4*t))


# ── Load V_total for omega_tau ───────────────────────────────────────────
print("Loading prerequisite data...")
bcs = np.load(os.path.join(T0, "s30b_grid_bcs.npz"), allow_pickle=True)
tau_grid = bcs['tau']
eps_grid = bcs['eps']
V_total = bcs['V_total_1p20']

spl_V = RectBivariateSpline(tau_grid, eps_grid, V_total, kx=3, ky=3)

# ── Compute on fine tau grid ─────────────────────────────────────────────
n_tau = 201
tau = np.linspace(0.01, 0.59, n_tau)

# Curvature invariants
R_vals = R_scalar(tau)
K_vals = K_kretschner(tau)
Ric_vals = Ric_sq(tau)
Weyl_vals = Weyl_sq(tau)

print(f"\nCurvature invariants at key points:")
for t_check in [0.0, 0.10, 0.15, 0.21, 0.35, 0.50]:
    print(f"  tau={t_check:.2f}: R={R_scalar(t_check):.6f}, K={K_kretschner(t_check):.6f}, "
          f"|Ric|^2={Ric_sq(t_check):.6f}, |C|^2={Weyl_sq(t_check):.6f}")

# Cross-check against s23c data
fiber = np.load(os.path.join(T0, "s23c_fiber_integrals.npz"), allow_pickle=True)
tau_23c = fiber['tau']
R_23c = fiber['R_scalar']
K_23c = fiber['K_kretschner']
for t_val, R_ref, K_ref in zip(tau_23c[:5], R_23c[:5], K_23c[:5]):
    R_ours = R_scalar(t_val)
    K_ours = K_kretschner(t_val)
    print(f"  Cross-check tau={t_val:.2f}: R_diff={abs(R_ours-R_ref):.2e}, K_diff={abs(K_ours-K_ref):.2e}")

# ── V_total along Jensen (eps=0) for omega_tau ──────────────────────────
V_jensen = spl_V(tau, 0.0, grid=False).ravel()
dV = np.gradient(V_jensen, tau)
d2V = np.gradient(dV, tau)

# omega_tau = sqrt(|d2V/dtau2|)  [modulus rolling frequency]
omega_tau = np.sqrt(np.abs(d2V))

print(f"\nomega_tau range: [{omega_tau.min():.4f}, {omega_tau.max():.4f}]")
print(f"d2V range: [{d2V.min():.4f}, {d2V.max():.4f}]")

# ── Instanton action and tunneling rate ──────────────────────────────────
# S_inst(tau) = alpha_grav * (-R(tau)) + alpha_YM * K(tau)
#
# We parametrize by the ratio r = alpha_YM / alpha_grav.
# Absorb alpha_grav by writing S_inst = alpha_grav * [-R + r*K]
# Gamma_inst ~ exp(-alpha_grav * [-R + r*K])
#
# For the rate comparison, we set alpha_grav = 1 (natural units where
# the KK radius sets the scale). This gives S_inst = -R + r*K.
#
# If S_inst < 0, the "instanton" is unsuppressed (anti-instanton dominates).
# The physically meaningful quantity is |S_inst| and sign.

coupling_ratios = np.array([0.1, 0.3, 0.5, 1.0, 2.0, 5.0])

print("\n" + "="*70)
print("I-1 INSTANTON-KAPITZA FREQUENCY RATIO")
print("="*70)

results = {}

for r in coupling_ratios:
    S_inst = -R_vals + r * K_vals
    Gamma_inst = np.exp(-S_inst)  # Tunneling rate (unnormalized)

    # Ratio Gamma_inst / omega_tau
    # Guard against omega_tau = 0 (at inflection points of V)
    ratio = Gamma_inst / (omega_tau + 1e-30)

    # Find maximum ratio in interior
    mask = (tau > 0.05) & (tau < 0.55)
    max_ratio = ratio[mask].max()
    idx_max = np.where(mask)[0][np.argmax(ratio[mask])]
    tau_at_max = tau[idx_max]
    S_at_max = S_inst[idx_max]
    Gamma_at_max = Gamma_inst[idx_max]
    omega_at_max = omega_tau[idx_max]

    # Find minimum of S_inst (maximum tunneling)
    idx_Smin = np.argmin(S_inst[mask])
    tau_Smin = tau[np.where(mask)[0][idx_Smin]]
    S_min = S_inst[mask].min()

    results[r] = {
        'S_inst': S_inst,
        'Gamma_inst': Gamma_inst,
        'ratio': ratio,
        'max_ratio': max_ratio,
        'tau_at_max_ratio': tau_at_max,
        'S_at_max': S_at_max,
        'S_min': S_min,
        'tau_Smin': tau_Smin,
    }

    gate_pass = max_ratio > 3.0

    print(f"\n  r = alpha_YM/alpha_grav = {r:.1f}:")
    print(f"    S_inst range: [{S_inst[mask].min():.4f}, {S_inst[mask].max():.4f}]")
    print(f"    S_inst minimum at tau = {tau_Smin:.4f}: S = {S_min:.4f}")
    print(f"    Gamma_inst at S_min: {np.exp(-S_min):.4f}")
    print(f"    Max Gamma/omega_tau = {max_ratio:.4f} at tau = {tau_at_max:.4f}")
    print(f"    At max ratio: S = {S_at_max:.4f}, Gamma = {Gamma_at_max:.4f}, omega = {omega_at_max:.4f}")
    if gate_pass:
        print(f"    >>> I-1 PASSES at r = {r:.1f}")
    else:
        print(f"    >>> I-1 does not pass (ratio < 3)")


# ── Additional analysis: what alpha_grav rescaling is needed? ────────────
print("\n" + "="*70)
print("ALPHA_GRAV SENSITIVITY ANALYSIS")
print("="*70)
print("Testing S_inst = alpha_grav * [-R + r*K] for different alpha_grav")

r_test = 1.0  # Most physically motivated coupling ratio
for alpha_g in [0.1, 0.5, 1.0, 2.0, 5.0, 10.0]:
    S_inst = alpha_g * (-R_vals + r_test * K_vals)
    Gamma_inst = np.exp(-S_inst)
    ratio = Gamma_inst / (omega_tau + 1e-30)
    mask = (tau > 0.05) & (tau < 0.55)
    max_ratio = ratio[mask].max()
    idx_max = np.where(mask)[0][np.argmax(ratio[mask])]

    print(f"  alpha_grav={alpha_g:.1f}, r=1.0: S_range=[{S_inst[mask].min():.3f}, {S_inst[mask].max():.3f}], "
          f"max Gamma/omega = {max_ratio:.4f} at tau={tau[idx_max]:.3f}")


# ── Additional: 3-channel instanton (grav + YM + Weyl) ──────────────────
print("\n" + "="*70)
print("3-CHANNEL INSTANTON: S = -alpha_R*R + alpha_K*K + alpha_W*|C|^2")
print("="*70)

# Test: can Weyl contribution help?
for alpha_W in [0.0, 0.5, 1.0, 2.0]:
    S_3ch = -R_vals + 1.0 * K_vals + alpha_W * Weyl_vals
    Gamma_3ch = np.exp(-S_3ch)
    ratio_3ch = Gamma_3ch / (omega_tau + 1e-30)
    mask = (tau > 0.05) & (tau < 0.55)
    max_r = ratio_3ch[mask].max()
    idx_max = np.where(mask)[0][np.argmax(ratio_3ch[mask])]

    S_min_3ch = S_3ch[mask].min()
    tau_Smin_3ch = tau[np.where(mask)[0][np.argmin(S_3ch[mask])]]

    print(f"  alpha_W={alpha_W:.1f}: S_min={S_min_3ch:.4f} at tau={tau_Smin_3ch:.3f}, "
          f"max Gamma/omega={max_r:.4f}")


# ── Gate Verdict ─────────────────────────────────────────────────────────
print("\n" + "="*70)
print("GATE I-1 VERDICT")
print("="*70)

any_pass = False
best_ratio = 0
best_r = None
for r, res in results.items():
    if res['max_ratio'] > best_ratio:
        best_ratio = res['max_ratio']
        best_r = r

if best_ratio > 3.0:
    print(f"  I-1 PASS: max Gamma_inst/omega_tau = {best_ratio:.4f} > 3 at r = {best_r:.1f}")
    any_pass = True
    gate_verdict = "PASS"
else:
    print(f"  I-1 DOES NOT FIRE: max Gamma_inst/omega_tau = {best_ratio:.4f} < 3")
    print(f"    Best coupling ratio: r = {best_r:.1f}")
    print(f"    At best: tau = {results[best_r]['tau_at_max_ratio']:.4f}, "
          f"S = {results[best_r]['S_at_max']:.4f}")

    # How close are we?
    factor_needed = 3.0 / best_ratio
    print(f"    Factor needed: {factor_needed:.2f}x (need alpha_grav adjustment)")
    print(f"    This requires either:")
    print(f"      (a) alpha_grav < {-np.log(3.0/best_ratio)/results[best_r]['S_at_max']:.3f}")
    print(f"      (b) Multi-instanton gas with collective enhancement")
    print(f"      (c) Instanton prefactor (determinant ratio) > {factor_needed:.2f}")
    gate_verdict = "DOES NOT FIRE"


# ── Save ─────────────────────────────────────────────────────────────────
save_dict = {
    'tau': tau,
    'R_scalar': R_vals,
    'K_kretschner': K_vals,
    'Ric_sq': Ric_vals,
    'Weyl_sq': Weyl_vals,
    'omega_tau': omega_tau,
    'd2V_dtau2': d2V,
    'coupling_ratios': coupling_ratios,
    'gate_verdict': np.array(gate_verdict, dtype='U20'),
}

for r, res in results.items():
    rkey = f"r{r:.1f}".replace('.', 'p')
    save_dict[f'S_inst_{rkey}'] = res['S_inst']
    save_dict[f'Gamma_inst_{rkey}'] = res['Gamma_inst']
    save_dict[f'ratio_{rkey}'] = res['ratio']
    save_dict[f'max_ratio_{rkey}'] = np.array(res['max_ratio'])

outfile = os.path.join(T0, "s31a_instanton_kapitza.npz")
np.savez_compressed(outfile, **save_dict)
print(f"\nSaved: {outfile}")


# ── Plotting ─────────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("I-1: Instanton-Kapitza Frequency Ratio", fontsize=14)

# Panel 1: Instanton action S_inst for different coupling ratios
ax = axes[0, 0]
for r in coupling_ratios:
    ax.plot(tau, results[r]['S_inst'], label=f'r={r:.1f}')
ax.axhline(y=0, color='k', linewidth=0.5, linestyle='--')
ax.set_xlabel('tau')
ax.set_ylabel('S_inst(tau)')
ax.set_title('Instanton action: S = -R + r*K')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 2: Tunneling rate Gamma_inst
ax = axes[0, 1]
for r in coupling_ratios:
    ax.semilogy(tau, results[r]['Gamma_inst'], label=f'r={r:.1f}')
ax.axhline(y=1, color='k', linewidth=0.5, linestyle='--')
ax.set_xlabel('tau')
ax.set_ylabel('Gamma_inst = exp(-S_inst)')
ax.set_title('Instanton tunneling rate')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 3: omega_tau (modulus frequency)
ax = axes[1, 0]
ax.plot(tau, omega_tau, 'k-', linewidth=2)
ax2 = ax.twinx()
ax2.plot(tau, d2V, 'b--', linewidth=1.5, alpha=0.5)
ax.set_xlabel('tau')
ax.set_ylabel('omega_tau = sqrt(|d2V/dtau2|)', color='k')
ax2.set_ylabel('d2V/dtau2', color='b')
ax.set_title('Modulus rolling frequency')
ax.grid(True, alpha=0.3)

# Panel 4: Ratio Gamma_inst / omega_tau
ax = axes[1, 1]
for r in coupling_ratios:
    ax.semilogy(tau, results[r]['ratio'], label=f'r={r:.1f}')
ax.axhline(y=3.0, color='r', linewidth=2, linestyle='--', label='Gate threshold (3.0)')
ax.set_xlabel('tau')
ax.set_ylabel('Gamma_inst / omega_tau')
ax.set_title('I-1 Gate: instanton rate vs modulus frequency')
ax.legend(fontsize=8)
ax.set_ylim(1e-3, 1e3)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plotfile = os.path.join(T0, "s31a_instanton_kapitza.png")
plt.savefig(plotfile, dpi=150, bbox_inches='tight')
print(f"Saved: {plotfile}")
plt.close()

print("\nI-1 computation complete.")
