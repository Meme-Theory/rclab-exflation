"""
S50 Resonance Lever: Phi-crossing enhanced SA-Goldstone coupling

The "Archimedes lever" hypothesis: the phi crossing at tau=0.2117
acts as a resonance that couples the spectral action correlator
(which breaks the O-Z identity) to the Goldstone propagator
(which generates the CMB power spectrum).

The lever arm is Q = 670,000 (Leggett undamped).
The fulcrum is the phi crossing (omega_L2/omega_L1 = phi_paasch exactly).
The force is the spectral action gradient dS/dtau = 58,673.

Three ingredients combine:
1. SA correlator has effective alpha = 1.21 (sub-quadratic, breaks identity)
2. Phi crossing provides resonance-enhanced coupling at tau = 0.2117
3. Leggett Q-factor amplifies the coupling at resonance by 10^5

The question: does the resonance-weighted SA contribution to P(K)
produce n_s in [0.950, 0.980] and alpha_s in [-0.040, 0]?
"""
import numpy as np
import sys
sys.path.insert(0, '.')
from canonical_constants import *

print("=" * 70)
print("THE RESONANCE LEVER: PHI-CROSSING ENHANCED SA-GOLDSTONE COUPLING")
print("=" * 70)

# =====================================================================
# PART 1: Gather all ingredients from prior computations
# =====================================================================

# From W1-D: Leggett quality factor
Q_Leggett = 6.7e5
omega_L1 = 0.0696  # M_KK
omega_L2 = 0.1074  # M_KK
Gamma_L = omega_L1 / (2 * Q_Leggett)  # damping rate

# From W1-E: phi crossing data
tau_fold = 0.19
tau_phi = 0.2117  # phi crossing
phi_paasch = 1.531580
dR_dtau = -0.553  # d(omega_L2/omega_L1)/dtau at crossing (monotone, transverse)

# Resonance width in tau-space
# At the crossing, R(tau) = phi. The resonance condition is satisfied within
# |R - phi| < Gamma_L/omega_L (fractional linewidth). Since R varies linearly:
# delta_tau_res = (Gamma_L/omega_L) / |dR/dtau| = (1/2Q) / |dR/dtau|
delta_tau_res = (1.0 / (2 * Q_Leggett)) / abs(dR_dtau)
print(f"\nResonance width in tau: delta_tau_res = {delta_tau_res:.2e}")
print(f"  = {delta_tau_res/0.030 * 100:.4f}% of transit window (0.030)")

# From S36: spectral action gradient
dS_dtau = 58673.0  # at fold
d2S_dtau2 = 317862.0  # at fold (convex)

# Transit parameters from S36/S38
v_terminal = 26.5  # M_KK
dt_transit = 0.00113  # M_KK^{-1}
delta_tau_transit = 0.030  # total tau traversed

# From Route 1: SA correlator data
# Reload and compute
d = np.load('s44_dos_tau.npz', allow_pickle=True)
omega_15 = d['tau0.15_all_omega']
omega_19 = d['tau0.19_all_omega']
dim2_19 = d['tau0.19_all_dim2']
domega_dtau = (omega_19 - omega_15) / 0.04

def casimir_su3(p, q):
    return (p**2 + q**2 + p*q + 3*p + 3*q) / 3.0

rep_catalog = {}
for p in range(7):
    for q in range(7-p):
        dim_val = (p+1)*(q+1)*(p+q+2)//2
        rep_catalog[(p,q)] = {'dim2': dim_val**2, 'C2': casimir_su3(p, q)}

Lambda_SA = 3.0
f_prime = np.exp(-omega_19**2 / Lambda_SA**2)
weight_SA = dim2_19 * f_prime * domega_dtau**2
total_weight_SA = weight_SA.sum()

sector_weights = {}
for d2 in np.unique(dim2_19):
    mask = (dim2_19 == d2)
    w = weight_SA[mask].sum()
    matching = [(p,q) for (p,q), info in rep_catalog.items() if info['dim2'] == d2]
    if matching and w > 0:
        c2 = rep_catalog[matching[0]]['C2']
        sector_weights[c2] = sector_weights.get(c2, 0) + w

print(f"\nSA sector weights (Lambda={Lambda_SA}):")
for c2 in sorted(sector_weights.keys()):
    frac = sector_weights[c2] / total_weight_SA
    if frac > 0.001:
        print(f"  C2={c2:5.2f}: {frac:.4f}")

# =====================================================================
# PART 2: The resonance-enhanced coupling model
# =====================================================================

print("\n" + "=" * 70)
print("PART 2: RESONANCE-ENHANCED COUPLING MODEL")
print("=" * 70)

print("""
Model: The physical power spectrum is generated during the transit from
tau=0.19 to tau~0.22. At each tau, the local correlator has two components:
  (a) Goldstone (O-Z): P_G(K, tau) = 1/(J*K^2 + m_L^2)
  (b) SA response: chi_SA(K, tau) = sum_sectors W_s/(K^2 + C2_s)

The coupling between them depends on how strongly the SA response feeds
into the Goldstone. At generic tau, the coupling is weak (the trace theorem
says SA is blind to U(1)_7). BUT at the phi crossing (tau=0.2117), the
Leggett mode resonates with the spectral geometry, creating a channel.

The resonance coupling:
  g_eff(tau) = g_0 * L(tau)
  L(tau) = (Gamma_L/2)^2 / [(R(tau) - phi)^2 + (Gamma_L/2)^2]

This is a Lorentzian in tau centered at tau_phi with width delta_tau_res.
At resonance: L = 1. Away from resonance: L ~ (delta_tau_res/|tau-tau_phi|)^2.
""")

# The coupling constant g_0 must be determined.
# Physical estimate: g_0 = (dS/dtau) * (dDelta/dtau) / (S * Delta)
# This is the fractional coupling between SA and BCS through tau.

# dDelta/dtau at fold (from S49: Delta varies 2.9% over delta_tau=0.30)
dDelta_dtau = 0.084 * 0.029 / 0.30  # ~ 0.0081 M_KK per unit tau
S_fold = 250361  # S_full at fold (from S36)
Delta_fold = 0.084  # M_KK

g_0 = (dS_dtau / S_fold) * (dDelta_dtau / Delta_fold)
print(f"\nCoupling constant g_0:")
print(f"  dS/dtau / S = {dS_dtau/S_fold:.6f}")
print(f"  dDelta/dtau / Delta = {dDelta_dtau/Delta_fold:.6f}")
print(f"  g_0 = {g_0:.6f}")

# Alternatively: g_0 from the inner fluctuation breaking
# epsilon_inner = 0.052 (from S49 DIPOLAR-CATALOG)
# This is the coupling between the trace-free (SA) and trace (Goldstone) sectors
epsilon_inner = 0.052
g_0_inner = epsilon_inner**2  # coupling goes as epsilon^2
print(f"\nAlternative g_0 from inner fluctuations:")
print(f"  epsilon_inner = {epsilon_inner}")
print(f"  g_0_inner = epsilon^2 = {g_0_inner:.6f}")

# Use the inner fluctuation coupling (more physical: it's the actual
# symmetry-breaking parameter for U(1)_7)
g_0_use = g_0_inner

# =====================================================================
# PART 3: Compute the resonance-weighted power spectrum
# =====================================================================

print("\n" + "=" * 70)
print("PART 3: RESONANCE-WEIGHTED POWER SPECTRUM")
print("=" * 70)

K_values = np.logspace(-2, 1.5, 1000)
K_pivot = 2.0
J_eff = 0.641
m_L = 0.070

# Goldstone propagator
P_G = 1.0 / (J_eff * K_values**2 + m_L**2)

# SA correlator
chi_SA = np.zeros_like(K_values)
for c2, w in sector_weights.items():
    chi_SA += w / (K_values**2 + c2 + 1e-10)
# Normalize to same scale as P_G at K=0
chi_SA_norm = chi_SA / chi_SA[0] * P_G[0]

# The transit integral: integrate the coupled propagator over tau
# P_total(K) = integral_transit P_G(K) * [1 + g_eff(tau) * chi_SA(K)/P_G(K)] dtau

# Discretize the transit
N_tau = 10000
tau_transit = np.linspace(tau_fold, tau_fold + delta_tau_transit, N_tau)
dtau_step = tau_transit[1] - tau_transit[0]

# The Lorentzian resonance profile
def lorentzian(tau, tau_0, gamma):
    return gamma**2 / ((tau - tau_0)**2 + gamma**2)

L_profile = lorentzian(tau_transit, tau_phi, delta_tau_res)

# Coupling as function of tau
g_eff_tau = g_0_use * L_profile

# The effective power spectrum: P(K) = P_G(K) * [1 + integral g_eff(tau) * f(K,tau) dtau]
# where f(K,tau) = chi_SA(K)/P_G(K) - 1 is the fractional SA correction

# The SA/Goldstone ratio as function of K
f_SA = chi_SA_norm / P_G - 1  # fractional correction from SA

# The resonance integral
# integral g_eff(tau) dtau = g_0 * integral L(tau) dtau = g_0 * pi * delta_tau_res
resonance_integral = g_0_use * np.pi * delta_tau_res
print(f"Resonance integral: g_0 * pi * delta_tau_res = {resonance_integral:.6e}")

# But we need to normalize by the TOTAL transit integral
# The Goldstone contributes at all tau: integral dtau = delta_tau_transit = 0.030
total_transit_weight = delta_tau_transit

# Effective coupling: resonance contributes a fraction of the total
alpha_coupling = resonance_integral / total_transit_weight
print(f"Effective coupling alpha = resonance/total = {alpha_coupling:.6e}")

# The combined power spectrum
P_combined = P_G * (1.0 + alpha_coupling * f_SA)

# But also consider: the Q-factor means the resonance is AMPLIFIED
# The resonance contribution is g_0 * Q * delta_tau_res (not g_0 * delta_tau_res)
# because the Lerentzian peak has height 1 and width delta_tau_res,
# while the integral is pi * delta_tau_res
# The Q enhancement enters through the peak height vs background ratio

# Model A: simple Lorentzian integral (no extra Q enhancement)
alpha_A = resonance_integral / total_transit_weight
P_A = P_G * (1.0 + alpha_A * f_SA)

# Model B: Q-enhanced coupling (resonance energy builds over Q cycles)
# At resonance, the system oscillates Q times before decaying
# Each oscillation transfers energy g_0 from SA to Goldstone
# Total transfer: g_0 * Q (coherent buildup)
alpha_B = g_0_use * Q_Leggett * delta_tau_res / total_transit_weight
P_B = P_G * (1.0 + alpha_B * f_SA)

# Model C: Critical coupling (the resonance exactly matches the
# SA and Goldstone impedances, like matched transmission lines)
# In this limit: alpha = sqrt(chi_SA(K_res) * P_G(K_res)) / max(chi_SA, P_G)
# This is the geometric mean coupling
idx_pivot = np.argmin(np.abs(K_values - K_pivot))
alpha_C = np.sqrt(abs(f_SA[idx_pivot])) * epsilon_inner
P_C = P_G * (1.0 + alpha_C * f_SA)

print(f"\nThree coupling models:")
print(f"  Model A (Lorentzian integral): alpha = {alpha_A:.6e}")
print(f"  Model B (Q-enhanced): alpha = {alpha_B:.6e}")
print(f"  Model C (impedance match): alpha = {alpha_C:.6e}")

# =====================================================================
# PART 4: Extract n_s and alpha_s for each model
# =====================================================================

print("\n" + "=" * 70)
print("PART 4: n_s AND alpha_s EXTRACTION")
print("=" * 70)

ln_K = np.log(K_values)

results = {}
for name, P_model, alpha_val in [
    ("Bare O-Z", P_G, 0),
    ("Model A (Lorentzian)", P_A, alpha_A),
    ("Model B (Q-enhanced)", P_B, alpha_B),
    ("Model C (impedance)", P_C, alpha_C),
]:
    ln_P = np.log(np.maximum(np.abs(P_model), 1e-30))
    dln = np.gradient(ln_P, ln_K)
    d2ln = np.gradient(dln, ln_K)

    n_s = 1 + dln[idx_pivot]
    alpha_s = d2ln[idx_pivot]
    identity = n_s**2 - 1
    deviation = alpha_s - identity

    results[name] = {
        'alpha': alpha_val, 'n_s': n_s, 'alpha_s': alpha_s,
        'identity': identity, 'deviation': deviation
    }

    print(f"\n{name} (alpha = {alpha_val:.2e}):")
    print(f"  n_s     = {n_s:.6f}")
    print(f"  alpha_s = {alpha_s:.6f}")
    print(f"  n_s^2-1 = {identity:.6f}")
    print(f"  DEVIATION from identity: {deviation:.6f}")

    # Planck comparison
    planck_tension_ns = abs(n_s - 0.965) / 0.004
    planck_tension_as = abs(alpha_s - 0.000) / 0.008
    print(f"  Tension with Planck: n_s at {planck_tension_ns:.1f}sigma, alpha_s at {planck_tension_as:.1f}sigma")

# =====================================================================
# PART 5: Scan coupling strength to find Planck-compatible region
# =====================================================================

print("\n" + "=" * 70)
print("PART 5: COUPLING SCAN — WHERE IS PLANCK COMPATIBILITY?")
print("=" * 70)

print("\nScanning coupling alpha to find n_s = 0.965 and alpha_s ~ 0:")

alpha_scan = np.logspace(-6, 1, 1000)
n_s_scan = np.zeros_like(alpha_scan)
alpha_s_scan = np.zeros_like(alpha_scan)

for i, a in enumerate(alpha_scan):
    P_test = P_G * (1.0 + a * f_SA)
    # Ensure positive
    P_test = np.maximum(P_test, 1e-30)
    ln_P = np.log(P_test)
    dln = np.gradient(ln_P, ln_K)
    d2ln = np.gradient(dln, ln_K)
    n_s_scan[i] = 1 + dln[idx_pivot]
    alpha_s_scan[i] = d2ln[idx_pivot]

# Find alpha where n_s = 0.965
target_ns = 0.965
idx_ns = np.argmin(np.abs(n_s_scan - target_ns))
alpha_ns = alpha_scan[idx_ns]
as_at_ns = alpha_s_scan[idx_ns]
identity_at_ns = n_s_scan[idx_ns]**2 - 1

print(f"\nn_s = {target_ns} achieved at coupling alpha = {alpha_ns:.6e}")
print(f"  alpha_s at this point: {as_at_ns:.6f}")
print(f"  n_s^2 - 1 = {identity_at_ns:.6f}")
print(f"  DEVIATION from identity: {as_at_ns - identity_at_ns:.6f}")
print(f"  Planck tension (alpha_s): {abs(as_at_ns)/0.008:.1f} sigma")

# Also find where alpha_s = 0
idx_as0 = np.argmin(np.abs(alpha_s_scan))
alpha_as0 = alpha_scan[idx_as0]
ns_at_as0 = n_s_scan[idx_as0]

print(f"\nalpha_s = 0 achieved at coupling alpha = {alpha_as0:.6e}")
print(f"  n_s at this point: {ns_at_as0:.6f}")
print(f"  Planck tension (n_s): {abs(ns_at_as0 - 0.965)/0.004:.1f} sigma")

# Find Planck-compatible region: n_s in [0.957, 0.973] AND alpha_s in [-0.016, 0.016]
mask_planck = (n_s_scan > 0.957) & (n_s_scan < 0.973) & \
              (alpha_s_scan > -0.016) & (alpha_s_scan < 0.016)
if np.any(mask_planck):
    alpha_planck = alpha_scan[mask_planck]
    print(f"\nPlanck-compatible region (2sigma):")
    print(f"  alpha in [{alpha_planck.min():.6e}, {alpha_planck.max():.6e}]")
    print(f"  Span: {np.log10(alpha_planck.max()/alpha_planck.min()):.1f} decades")

    # Where do our physical models land?
    for name, r in results.items():
        if r['alpha'] > 0:
            in_range = alpha_planck.min() <= r['alpha'] <= alpha_planck.max()
            print(f"  {name}: alpha={r['alpha']:.2e} — {'IN RANGE' if in_range else 'OUT OF RANGE'}")
else:
    print("\nNo Planck-compatible region found in scan range.")
    # Find closest approach
    dist = np.sqrt(((n_s_scan - 0.965)/0.004)**2 + ((alpha_s_scan)/0.008)**2)
    idx_closest = np.argmin(dist)
    print(f"  Closest approach at alpha = {alpha_scan[idx_closest]:.6e}:")
    print(f"    n_s = {n_s_scan[idx_closest]:.6f}, alpha_s = {alpha_s_scan[idx_closest]:.6f}")
    print(f"    Combined tension: {dist[idx_closest]:.1f} sigma")

# =====================================================================
# PART 6: Physical interpretation
# =====================================================================

print("\n" + "=" * 70)
print("PART 6: PHYSICAL INTERPRETATION")
print("=" * 70)

print(f"""
The resonance lever computation reveals the following structure:

1. BARE O-Z: n_s = {results['Bare O-Z']['n_s']:.4f} (at m = omega_L = 0.070 M_KK)
   This is n_s ~ -1 because m << J*K^2 at K_pivot. The Goldstone is in the
   kinetic-dominated regime. To get n_s = 0.965 from O-Z alone, you need
   m_star = 11.87 M_KK (170x the Leggett mass).

2. SA MODULATION breaks the O-Z form. The effective propagator is:
   P(K) = P_G(K) * [1 + alpha * f_SA(K)]
   where f_SA has structure from the multi-Casimir pole decomposition.

3. The coupling alpha has three physical estimates:
   A (Lorentzian resonance): {alpha_A:.2e} — too weak
   B (Q-enhanced):           {alpha_B:.2e}
   C (impedance match):      {alpha_C:.2e}

4. n_s = 0.965 requires alpha = {alpha_ns:.2e}
   alpha_s at that coupling: {as_at_ns:.6f}
   Planck tension: {abs(as_at_ns)/0.008:.1f} sigma
""")

# Key diagnostic: is the required coupling physically achievable?
print(f"Required coupling / Model B: {alpha_ns / alpha_B:.2f}")
print(f"Required coupling / Model C: {alpha_ns / alpha_C:.2f}")
print(f"Required coupling / epsilon_inner^2: {alpha_ns / epsilon_inner**2:.2f}")
print(f"Required coupling / epsilon_inner: {alpha_ns / epsilon_inner:.2f}")

# Save results
np.savez('s50_resonance_lever.npz',
    K_values=K_values,
    P_G=P_G, P_A=P_A, P_B=P_B, P_C=P_C,
    chi_SA_norm=chi_SA_norm, f_SA=f_SA,
    n_s_scan=n_s_scan, alpha_s_scan=alpha_s_scan, alpha_scan=alpha_scan,
    alpha_ns=alpha_ns, as_at_ns=as_at_ns,
    Q_Leggett=Q_Leggett, delta_tau_res=delta_tau_res,
    g_0=g_0_use, epsilon_inner=epsilon_inner,
    tau_phi=tau_phi, tau_fold=tau_fold
)
print("\nData saved to s50_resonance_lever.npz")
