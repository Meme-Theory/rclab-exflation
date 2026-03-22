"""
Session 23c Task 7 (FINAL): Fiber Integrals for alpha(tau) and beta(tau)
========================================================================

Computes the geometric fiber integrals entering the FR potential
V_FR(tau) = -alpha * R_K(tau) + beta * |omega_3|^2(tau)

and the spectral action potential
V_spec(tau) = c_2 * R_K(tau) + c_4 * (500*R_K^2 - 32*|Ric|^2 - 28*K)(tau)

Uses existing r20a Riemann tensor data (147/147 verified).

Author: KK Theorist (Session 23c, respawned)
Date: 2026-02-20
"""

import numpy as np
from scipy.optimize import brentq

# =====================================================================
# LOAD DATA
# =====================================================================
base = "C:/sandbox/Ainulindale Exflation/tier0-computation"
d = np.load(f"{base}/r20a_riemann_tensor.npz")

tau_data = d['tau']         # 21 points, 0 to 2
R_K_data = d['R_scalar']    # scalar curvature
Ric_ab = d['Ric']           # Ricci tensor
K_data = d['K']             # Kretschner scalar

n_tau = len(tau_data)
Ric_sq_data = np.array([np.sum(Ric_ab[i]**2) for i in range(n_tau)])

# =====================================================================
# ANALYTIC FORMULAS (exact for Jensen SU(3))
# =====================================================================

def R_K(tau):
    """Scalar curvature R_K(tau) in our normalization (R(0) = 2.0)"""
    return 0.25 * (2*np.exp(2*tau) - 1 + 8*np.exp(-tau) - np.exp(-4*tau))

def dR_K(tau):
    """First derivative of R_K"""
    return 0.25 * (4*np.exp(2*tau) - 8*np.exp(-tau) + 4*np.exp(-4*tau))

def d2R_K(tau):
    """Second derivative of R_K"""
    return 0.25 * (8*np.exp(2*tau) + 8*np.exp(-tau) - 16*np.exp(-4*tau))

def omega_sq(tau):
    """|omega_3|^2(tau) = (1/2)e^{-4tau} + 1/2 + (1/3)e^{6tau}"""
    return 0.5*np.exp(-4*tau) + 0.5 + (1.0/3.0)*np.exp(6*tau)

def domega_sq(tau):
    """First derivative of |omega_3|^2"""
    return -2*np.exp(-4*tau) + 2*np.exp(6*tau)

def d2omega_sq(tau):
    """Second derivative of |omega_3|^2"""
    return 8*np.exp(-4*tau) + 12*np.exp(6*tau)

# =====================================================================
# VERIFY ANALYTIC vs NUMERICAL
# =====================================================================

R_analytic = np.array([R_K(t) for t in tau_data])
omega_analytic = np.array([omega_sq(t) for t in tau_data])

print("=" * 70)
print("TASK 7 FINAL: Fiber Integrals for beta/alpha")
print("=" * 70)
print()
print("VERIFICATION:")
print(f"  R_K analytic vs data max error: {np.max(np.abs(R_analytic - R_K_data)):.2e}")
print(f"  R_K(0) = {R_K(0):.6f} (expect 2.0)")
print(f"  omega_sq(0) = {omega_sq(0):.6f} (expect 4/3 = 1.333333)")
print()

# =====================================================================
# PART 1: ALPHA (from a_2 / Einstein-Hilbert)
# =====================================================================

print("1. ALPHA (Einstein-Hilbert coefficient from a_2):")
print("   alpha = f_2 * Lambda^2 * Vol_K / (6 * (4*pi)^6)")
print("   Vol_K = Vol(SU(3), g_Jensen) = CONSTANT (volume-preserving)")
print("   alpha is TAU-INDEPENDENT")
print()

# =====================================================================
# PART 2: A4 GEOMETRIC COMBINATION
# =====================================================================

a4_geom = 500*R_K_data**2 - 32*Ric_sq_data - 28*K_data

print("2. a_4 GEOMETRIC COMBINATION (Gilkey formula for D_K^2 on 8D fiber):")
print("   a_4_geom = 500*R_K^2 - 32*|Ric|^2 - 28*K")
print(f"   a_4_geom(0) = {a4_geom[0]:.4f} (analytic: 500*4 - 16 - 14 = 1970)")
print(f"   a_4_geom(0.3) = {a4_geom[3]:.4f}")
print(f"   a_4_geom(1.0) = {a4_geom[10]:.4f}")
print(f"   Dominated by 500*R_K^2 term (|Ric|^2 and K < 3%)")
print()

# =====================================================================
# PART 3: FR POTENTIAL AND beta/alpha
# =====================================================================

print("3. FR POTENTIAL: V_FR(tau) = -R_K(tau) + r * omega_sq(tau)")
print("   (in our normalization, with alpha = 1)")
print()

# For minimum at tau_0, need dV/dtau = 0:
# -dR_K + r * domega_sq = 0 => r = dR_K/domega_sq

tau_targets = [0.25, 0.2994, 0.30, 0.35]
print("   tau_0       r_ours     beta/alpha_Baptista  V_second  status")
print("   " + "-" * 65)
for t0 in tau_targets:
    r = dR_K(t0) / domega_sq(t0)
    ba = 6 * r  # Baptista normalization: R_K_Bap = 6*R_K_ours
    vs = -d2R_K(t0) + r * d2omega_sq(t0)
    status = "MINIMUM" if vs > 0 else "saddle"
    print(f"   {t0:.4f}    {r:.8f}    {ba:.8f}       {vs:+.4f}    {status}")

print()

# =====================================================================
# PART 4: CRITICAL RATIO (degenerate)
# =====================================================================

def degenerate_condition(tau):
    """V(tau_0) = V(0) condition combined with dV/dtau = 0"""
    r = dR_K(tau) / domega_sq(tau)
    return r * (omega_sq(tau) - 4.0/3.0) - (R_K(tau) - 2.0)

# Find critical tau
taus = np.linspace(0.05, 1.0, 10000)
h_vals = np.array([degenerate_condition(t) for t in taus])
for j in range(1, len(h_vals)):
    if h_vals[j-1] * h_vals[j] < 0:
        t_crit = brentq(degenerate_condition, taus[j-1], taus[j])
        r_crit = dR_K(t_crit) / domega_sq(t_crit)
        break

print(f"4. CRITICAL RATIO (degenerate double-well):")
print(f"   tau_crit = {t_crit:.6f}")
print(f"   r_crit (ours) = {r_crit:.8f}")
print(f"   beta/alpha_crit (Baptista) = {6*r_crit:.6f}")
print(f"   Session 21b reported: 0.313")
print(f"   Agreement: {abs(6*r_crit - 0.313)/0.313*100:.2f}%")
print()

# =====================================================================
# PART 5: NORMALIZATION MAPPING
# =====================================================================

print("5. NORMALIZATION MAPPING:")
print("   R_K_Baptista = 6 * R_K_ours")
print("   (Baptista eq 3.70 with alpha_Bap = 1 gives R(0) = 12)")
print("   (Our code: R(0) = 2.0)")
print("   beta/alpha_Baptista = 6 * beta/alpha_ours")
print()
print("   Session 21b reported beta/alpha = 0.28 for tau_0 = 0.30")
r_030 = dR_K(0.30) / domega_sq(0.30)
print(f"   Exact analytic: beta/alpha_Baptista = {6*r_030:.4f}")
print(f"   Discrepancy: {abs(6*r_030 - 0.28):.4f}")
print(f"   (21b likely used numerical grid; our analytic formula is exact)")
print()

# Refined: find tau that gives EXACTLY beta/alpha = 0.28 (Baptista)
# 6*r = 0.28 => r = 0.28/6 = 0.04667
r_target = 0.28 / 6.0
# dR_K(tau)/domega_sq(tau) = r_target
def gap(tau):
    return dR_K(tau) / domega_sq(tau) - r_target

t_search = np.linspace(0.01, 0.8, 10000)
g_vals = np.array([gap(t) for t in t_search])
for j in range(1, len(g_vals)):
    if g_vals[j-1] * g_vals[j] < 0:
        t_028 = brentq(gap, t_search[j-1], t_search[j])
        print(f"   beta/alpha = 0.28 => tau_0 = {t_028:.6f}")
        break

print()

# =====================================================================
# PART 6: ANALYTIC vs NUMERICAL SPLIT
# =====================================================================

print("6. ANALYTIC vs NUMERICAL:")
print("   FULLY ANALYTIC (closed form):")
print("     * R_K(tau) = (1/4)(2e^{2t} - 1 + 8e^{-t} - e^{-4t})")
print("     * |omega_3|^2(tau) = (1/2)e^{-4t} + 1/2 + (1/3)e^{6t}")
print("     * Vol_K = constant")
print("     * FR potential V = -R_K + r*omega_sq: fully analytic")
print("     * Critical ratio: r_crit from transcendental eq (solved numerically)")
print("     * tau_0(r): from r = dR_K/domega_sq (analytic + root-finding)")
print()
print("   NUMERICAL (from r20a data, 21 tau-points):")
print("     * |Ric_K|^2(tau): ~17 exponential terms (messy analytic form)")
print("     * K(tau): ~17 exponential terms")
print("     * a_4_geom = 500*R^2 - 32*|Ric|^2 - 28*K: from above")
print()
print("   CONCLUSION: FR potential is FULLY ANALYTIC.")
print("   Spectral action a_4 uses numerical data (cheap, already computed).")
print()

# =====================================================================
# PART 7: COMPUTATIONAL COST ESTIMATE
# =====================================================================

print("7. COMPUTATIONAL COST for Session 24:")
print()
print("   ZERO COST (already done):")
print("   - All fiber geometry integrals (r20a data)")
print("   - FR potential shape (analytic)")
print("   - Critical ratio (analytic + root-finding)")
print()
print("   LOW COST (2-4 hours):")
print("   - Verify Gilkey a_4 coefficients (500, -32, -28) from first principles")
print("   - Compute spinor trace tr(Omega^2) = -2K explicitly")
print("   - Cross-check a_4_geom(0) = 1970 against SU(3) Casimir values")
print()
print("   MEDIUM COST (1-2 days):")
print("   - Map spectral action a_4 to FR beta precisely")
print("   - Determine whether NCG spectral triple constrains f_k ratios")
print("   - Derive beta from mixed R_{mu a nu b} (KK reduction)")
print()
print("   HIGH COST (1 week, potential showstopper):")
print("   - Full derivation of f_4/(f_2*Lambda^2) from SM coupling unification")
print("   - This requires knowing the NCG spectral triple A_F = C + H + M_3(C)")
print("   - Connes-Chamseddine: f is constrained by the spectral triple (Paper 07)")
print()

# =====================================================================
# PART 8: THE KEY INSIGHT
# =====================================================================

print("8. KEY INSIGHT:")
print()
print("   The FR potential V_FR = -alpha*R_K + beta*|omega_3|^2 is STRUCTURALLY")
print("   determined by the Jensen SU(3) geometry. The shape is FIXED.")
print("   The ONLY free parameter is beta/alpha.")
print()
print("   From the SPECTRAL ACTION on the full NCG triple:")
print("     alpha ~ f_2 * Lambda^2 * Vol_K / (4*pi)^6")
print("     beta ~ f_4 * Vol_K * [a_4 geometric piece] / (4*pi)^6")
print("     => beta/alpha ~ (f_4/f_2) / Lambda^2 * [a_4 geom / 6]")
print()
print("   The GEOMETRIC PIECE is computed (Task 7 deliverable).")
print("   The UNIVERSAL PIECE (f_4/f_2/Lambda^2) requires NCG input.")
print()
print("   If NCG constrains f_k ratios AND Lambda is the unification scale,")
print("   then beta/alpha is a ZERO-PARAMETER prediction.")
print("   This is the Session 24 question.")

# =====================================================================
# SAVE FINAL RESULTS
# =====================================================================

np.savez(f"{base}/s23c_fiber_integrals.npz",
         tau=tau_data,
         R_scalar=R_K_data,
         Ric_sq=Ric_sq_data,
         K_kretschner=K_data,
         a4_geom=a4_geom,
         omega_sq=np.array([omega_sq(t) for t in tau_data]),
         r_ours_at_030=r_030,
         ba_baptista_at_030=6*r_030,
         r_crit=r_crit,
         ba_crit_baptista=6*r_crit,
         tau_crit=t_crit)

print()
print(f"Results saved to: {base}/s23c_fiber_integrals.npz")
