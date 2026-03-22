"""
Session 33 W3 Round 2: Einstein-Bergmann Modulus Equation for tau(x)
=====================================================================
KK Theorist — Task #1

Derives:
1. The modulus field equation Box(tau) + V'_eff(tau) = 0 from the 12D action
2. Solitonic domain wall solutions tau(x)
3. Wall width, profile, and energy density
4. Analysis of whether domain walls break U(2)

Inputs (all from established sessions):
- G_{tau tau} = 5  (Baptista eq 3.79, Session 21b, confirmed by einstein B-3)
- R_K(tau) = (3/(2*alpha)) * [2*e^{2tau} - 1 + 8*e^{-tau} - e^{-4tau}]  (Baptista eq 3.70)
- |omega_3|^2(tau) = (1/2)*e^{-4tau} + 1/2 + (1/3)*e^{6tau}  (Session 21b EXACT)
- Spectral action curvature d^2S/dtau^2 = 20.43 at tau=0.20  (Session 32b RPA-32b)
- V_spec(tau) monotonically increasing  (Session 24a V-1)
- Kerner: R_P = R_M4 + R_K(tau) + (1/4)*F^2(tau)  (Paper 06, eq 26-30)

Convention: alpha in R_K is the overall scale set by the Baptista metric normalization.
For the Jensen metric at tau=0 (round SU(3)): R_K(0) = 12 (Baptista convention).
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ===========================================================================
# 1. GEOMETRIC INGREDIENTS
# ===========================================================================

def R_K(tau):
    """Scalar curvature of Jensen-deformed SU(3). Baptista eq 3.70.

    R(s) = (3*alpha/2)*(2*e^{2s} - 1 + 8*e^{-s} - e^{-4s})

    With Baptista normalization: at s=0, R=12.
    So alpha = 4/3 to get R(0) = (3*4/3/2)*(2-1+8-1) = 2*8 = ...
    Let's verify: (3*alpha/2)*(2-1+8-1) = (3*alpha/2)*8 = 12*alpha.
    For R(0)=12: alpha = 1.  So R(s) = (3/2)*(2*e^{2s} - 1 + 8*e^{-s} - e^{-4s}).
    Check: (3/2)*(2+8-1-1) = (3/2)*8 = 12.  Yes.
    """
    s = tau
    return 1.5 * (2*np.exp(2*s) - 1 + 8*np.exp(-s) - np.exp(-4*s))


def dR_K_dtau(tau):
    """First derivative of R_K(tau)."""
    s = tau
    return 1.5 * (4*np.exp(2*s) - 8*np.exp(-s) + 4*np.exp(-4*s))


def d2R_K_dtau2(tau):
    """Second derivative of R_K(tau)."""
    s = tau
    return 1.5 * (8*np.exp(2*s) + 8*np.exp(-s) - 16*np.exp(-4*s))


def omega_sq(tau):
    """|omega_3|^2(tau) = Cartan 3-form norm squared. Session 21b EXACT."""
    s = tau
    return 0.5*np.exp(-4*s) + 0.5 + (1.0/3.0)*np.exp(6*s)


def d_omega_sq_dtau(tau):
    """First derivative of |omega_3|^2."""
    s = tau
    return -2*np.exp(-4*s) + 2*np.exp(6*s)


def d2_omega_sq_dtau2(tau):
    """Second derivative of |omega_3|^2."""
    s = tau
    return 8*np.exp(-4*s) + 12*np.exp(6*s)


# Metric on moduli space (DeWitt metric on Jensen deformations)
G_TAU_TAU = 5.0  # Baptista eq 3.79, Session 21b

# Volume of SU(3) with the round metric (normalization)
# Jensen deformations are volume-preserving, so Vol_K is constant.
# We work in units where Vol_K = 1 for simplicity (it factors out).

# ===========================================================================
# 2. THE MODULUS FIELD EQUATION — DERIVATION
# ===========================================================================
#
# Starting from the 12D Einstein-Hilbert action (Kerner, Paper 06):
#
#   S_12 = (1/(2*kappa_12^2)) * int R_P * sqrt(g_P) * d^12x
#
# where P = M^4 x K^8 with K = SU(3) carrying Jensen metric g_K(tau).
#
# Using Kerner's decomposition (Paper 06, eq 26-30):
#   R_P = R_M4 + R_K(tau) + (1/4)*F^2(tau)
#
# When tau is promoted to a field tau(x) on M^4, we must include
# the kinetic term from the variation of g_K(tau(x)):
#
#   R_P = R_M4 + R_K(tau) + (1/4)*F^2(tau)
#          - G_{tau tau} * g^{mu nu} * partial_mu(tau) * partial_nu(tau)
#
# The minus sign arises because spatial variation of the fiber metric
# costs curvature energy (this is the standard sigma-model kinetic term
# in KK reductions — see DeWitt Paper 05, also Einstein-Bergmann Paper 04).
#
# After integrating over K (using Vol_K = const from volume-preserving Jensen):
#
#   S_4 = (Vol_K / (2*kappa_12^2)) * int [R_M4 + R_K(tau)
#          - G_{tau tau} * (partial tau)^2 + (1/4)*F^2(tau)] * sqrt(-g_4) d^4x
#
# Adding the spectral action correction (one-loop, from Connes-Chamseddine):
#
#   S_spec = Tr f(D_K^2/Lambda^2) = S_spec(tau)
#
# The total effective action for the modulus is:
#
#   S_eff = int [ (1/2)*G_{tau tau}*(partial tau)^2 - V_eff(tau) ] * sqrt(-g_4) d^4x
#
# where V_eff(tau) = V_FR(tau) + V_spec(tau) with:
#   V_FR(tau) = -alpha_FR * R_K(tau) + beta_FR * |omega_3|^2(tau)
#   V_spec(tau) = spectral action contribution (monotonically increasing, Session 24a V-1)
#
# The CANONICALLY NORMALIZED field is:
#   sigma(x) = sqrt(G_{tau tau}) * tau(x) = sqrt(5) * tau(x)
#
# The equation of motion is:
#
#   Box(tau) + (1/G_{tau tau}) * dV_eff/dtau = 0           ... (MODULUS EQ)
#
# For a static 1D domain wall along x-direction:
#
#   d^2(tau)/dx^2 = (1/G_{tau tau}) * dV_eff/dtau          ... (WALL EQ)
#
# This is the mechanical analog: particle at position tau rolling in
# INVERTED potential -V_eff(tau) / G_{tau tau}.

print("="*70)
print("EINSTEIN-BERGMANN MODULUS EQUATION FOR tau(x)")
print("="*70)

# ===========================================================================
# 3. FREUND-RUBIN POTENTIAL: V_FR(tau)
# ===========================================================================

# V_FR(tau) = -alpha_FR * R_K(tau) + beta_FR * |omega_3|^2(tau)
#
# From Session 21b: the critical ratio beta_FR/alpha_FR = 0.313
# determines whether the true minimum is at tau=0 or tau>0.
#
# For the Weinberg angle prediction: sin^2(theta_W) = 0.231
# requires tau_0 = 0.2994, which needs beta_FR/alpha_FR ~ 0.28.
#
# We parametrize by the ratio r = beta_FR / alpha_FR and set alpha_FR = 1.

def V_FR(tau, r_ba):
    """Freund-Rubin potential. r_ba = beta/alpha."""
    return -R_K(tau) + r_ba * omega_sq(tau)

def dV_FR_dtau(tau, r_ba):
    """dV_FR/dtau."""
    return -dR_K_dtau(tau) + r_ba * d_omega_sq_dtau(tau)

def d2V_FR_dtau2(tau, r_ba):
    """d^2 V_FR / dtau^2."""
    return -d2R_K_dtau2(tau) + r_ba * d2_omega_sq_dtau2(tau)


# Verify V_FR properties
print("\n--- Freund-Rubin Potential ---")
print(f"V_FR(0, r=0.28) = {V_FR(0, 0.28):.4f}")
print(f"V_FR'(0, r=0.28) = {dV_FR_dtau(0, 0.28):.6f}")
print(f"V_FR''(0, r=0.28) = {d2V_FR_dtau2(0, 0.28):.4f}")

# Find the minimum for beta/alpha = 0.28
tau_scan = np.linspace(0, 1.5, 10000)
vfr_scan = np.array([V_FR(t, 0.28) for t in tau_scan])
dvfr_scan = np.array([dV_FR_dtau(t, 0.28) for t in tau_scan])

# Find zero crossings of dV_FR/dtau
sign_changes = np.where(np.diff(np.sign(dvfr_scan)))[0]
print(f"\ndV_FR/dtau = 0 at tau values:")
tau_extrema = []
for idx in sign_changes:
    tau_zero = brentq(lambda t: dV_FR_dtau(t, 0.28), tau_scan[idx], tau_scan[idx+1])
    v_zero = V_FR(tau_zero, 0.28)
    d2v = d2V_FR_dtau2(tau_zero, 0.28)
    nature = "MIN" if d2v > 0 else "MAX" if d2v < 0 else "INFLECTION"
    tau_extrema.append((tau_zero, v_zero, nature))
    print(f"  tau = {tau_zero:.4f}, V = {v_zero:.4f}, d2V = {d2v:.2f} ({nature})")


# ===========================================================================
# 4. SPECTRAL ACTION CORRECTION
# ===========================================================================
#
# From Session 24a V-1: V_spec(tau) is MONOTONICALLY INCREASING.
# From Session 32b RPA-32b: d^2 V_spec / dtau^2 = 20.43 at tau = 0.20.
#
# We model V_spec(tau) as a function that is:
# - Zero at tau = 0 (reference point)
# - Monotonically increasing
# - Has curvature 20.43 at tau = 0.20
#
# The simplest consistent model: V_spec(tau) ~ c_spec * (cosh(k*tau) - 1)
# with c_spec * k^2 * cosh(k * 0.20) = 20.43
#
# But we also know from Session 23c that the spectral action is dominated
# by the a_4 Seeley-DeWitt coefficient. A more physically motivated model
# uses the ACTUAL spectral action functional form.
#
# For the modulus equation, what matters is the DERIVATIVE dV_spec/dtau.
# We can reconstruct this from the curvature data.
#
# Key constraint: V_spec is monotonically increasing AND V_spec''(0.20) = 20.43.
#
# Model: V_spec(tau) = A * tau + B * tau^2 + C * tau^3
# With V_spec(0) = 0, V_spec'(0) > 0, V_spec''(0.20) = 20.43.
# We have from the spectral action slope at tau=0:
# The bare spectral action slope (Session 24a) is ~500x F_BCS at tau=0.
# V_spec'(0) is large and positive.
#
# Actually, let's use the known data points more carefully.
# From Session 24a: the spectral action S(tau) increases from S(0) by
# approximately 0.4 per unit tau for small tau (from eigenvalue sum data).
# From RPA-32b: S''(0.20) = 20.43.
#
# Let's parametrize: V_spec(tau) = v1*tau + (1/2)*v2(tau)*tau^2
# where v2 is approximately v2(0.20) = 20.43.
#
# For the domain wall analysis, we need V_eff = V_FR + lambda_spec * V_spec
# where lambda_spec controls the relative strength of the spectral vs FR terms.
# This is the ONE free parameter: lambda_spec = f_4 / (f_8 * Lambda^4)
# from the spectral action expansion (Session 23c).

# We model V_spec using a quadratic approximation around the dump point:
# V_spec(tau) ~ V_spec(tau_0) + V_spec'(tau_0)*(tau-tau_0) + (1/2)*20.43*(tau-tau_0)^2

# But for the FULL potential, we need the absolute normalization.
# Let's compute V_eff = V_FR + eta * V_spec for various eta values.

# From the Session 21b notes: the spectral action slope at tau=0 gives
# dS/dtau|_0 ~ sum d|lambda_k|/dtau. Session 24a established this is
# monotonically positive. The EXACT slope from eigenvalue data:

# V_spec model: fit to monotonic increasing with known curvature
# Use: V_spec(tau) = A * (exp(k*tau) - 1) where k, A > 0
# V_spec'(tau) = A*k*exp(k*tau)
# V_spec''(tau) = A*k^2*exp(k*tau)
# At tau=0.20: A*k^2*exp(0.20*k) = 20.43
# We need another constraint. From the monotonicity and the a_4/a_2 = 1000:1
# ratio at tau=0, the slope at tau=0 is substantial.
#
# Use: A*k = V_spec'(0). From the spectral action data, the slope is
# approximately proportional to dR_K/dtau (through a_2 coefficient),
# giving V_spec'(0) ~ c * dR_K/dtau(0) = 0 (!!!)
#
# Wait - dR_K/dtau(0) = 1.5*(4 - 8 + 4) = 0. The slope AT tau=0 is zero
# for R_K. And for the spectral action, V_spec'(0) = 0 as well (by symmetry
# of the round metric under infinitesimal Jensen deformation at first order).
#
# Actually this is a subtle point. The spectral action Tr f(D_K^2) at the
# round metric tau=0 is at a SADDLE: it's a local minimum along the Jensen
# direction (V_spec''(0) > 0) but the overall V_spec is increasing monotonically
# for tau > 0. This means V_spec'(0) = 0 and V_spec''(0) > 0.
#
# So the correct model near tau=0:
# V_spec(tau) ~ (1/2) * chi_0 * tau^2 + (1/6) * chi_1 * tau^3 + ...
# where chi_0 = V_spec''(0).

# From the data: at tau=0, the round metric is a critical point of the spectral
# action (by SO(8) symmetry). V_spec'(0) = 0.
# V_spec''(0) is the second derivative at the round metric.
# The RPA-32b value 20.43 is at tau=0.20, not at tau=0.

# Let's compute V_spec''(0) from the eigenvalue data structure.
# The spectral action S = sum |lambda_k(tau)|.
# At tau=0, by SO(8) symmetry, dS/dtau = 0.
# d^2S/dtau^2|_0 = sum d^2|lambda_k|/dtau^2|_0

# For now, use a polynomial fit: V_spec(tau) = c2*tau^2 + c3*tau^3 + c4*tau^4
# with V_spec''(0.20) = 2*c2 + 6*c3*0.20 + 12*c4*0.04 = 20.43
# and V_spec being monotonically increasing for tau > 0.

# Simplest model consistent with all constraints:
# V_spec(tau) = (chi/2) * tau^2  (quadratic, symmetric)
# This gives V_spec''(tau) = chi for all tau.
# Then chi = 20.43 everywhere (crude but captures the key physics).

# Better: use the ACTUAL spectral action from Seeley-DeWitt.
# S_spec = f_0 * Lambda^8 * a_0 + f_2 * Lambda^6 * a_2 + f_4 * Lambda^4 * a_4
# where a_n = a_n(tau) are the heat kernel coefficients.
# a_0 = Vol_K (constant for Jensen)
# a_2 = (1/6) * int R_K * sqrt(g_K) d^8y = (1/6) * R_K(tau) * Vol_K
# a_4 = int [500*R^2 - 32*|Ric|^2 - 28*K] * sqrt(g_K) d^8y / (360 * (4pi)^4)
#       (from Gilkey for D_K^2, dim_spinor=16, Session 23c)

# The relative coefficient eta = V_spec / V_FR depends on f_4/(f_8*Lambda^4).
# We parametrize this as a single free parameter.

# For the MODULUS EQUATION derivation, we keep eta as a parameter and
# show the structure for all physical values.

print("\n" + "="*70)
print("4. SPECTRAL ACTION MODEL")
print("="*70)

# Model V_spec with quadratic + cubic to capture both V_spec'(0)=0 and
# the monotonic increase:
# V_spec(tau) = (chi_0/2)*tau^2 + (chi_1/6)*tau^3
# V_spec'(tau) = chi_0*tau + (chi_1/2)*tau^2
# For monotonicity: V_spec'(tau) > 0 for tau > 0 => chi_0 > 0 and chi_1 > -2*chi_0/tau_max
# V_spec''(tau) = chi_0 + chi_1*tau
# V_spec''(0.20) = chi_0 + 0.20*chi_1 = 20.43

# From the known behavior: V_spec is steep for large tau (a_4 dominates).
# A reasonable fit: chi_0 ~ 18, chi_1 ~ 12 gives V_spec''(0.20) = 18 + 2.4 = 20.4.

chi_0 = 18.0
chi_1 = 12.15  # tuned to give V_spec''(0.20) = 20.43

def V_spec(tau, eta=1.0):
    """Spectral action potential (model). eta = relative coupling."""
    return eta * (0.5 * chi_0 * tau**2 + (1.0/6.0) * chi_1 * tau**3)

def dV_spec_dtau(tau, eta=1.0):
    """dV_spec/dtau."""
    return eta * (chi_0 * tau + 0.5 * chi_1 * tau**2)

def d2V_spec_dtau2(tau, eta=1.0):
    """d^2 V_spec / dtau^2."""
    return eta * (chi_0 + chi_1 * tau)

print(f"V_spec model: V = (chi_0/2)*tau^2 + (chi_1/6)*tau^3")
print(f"chi_0 = {chi_0:.2f}, chi_1 = {chi_1:.2f}")
print(f"V_spec''(0.00) = {d2V_spec_dtau2(0):.2f}")
print(f"V_spec''(0.20) = {d2V_spec_dtau2(0.20):.2f} (target: 20.43)")
print(f"V_spec'(0.00) = {dV_spec_dtau(0):.4f} (must be 0)")
print(f"V_spec'(0.20) = {dV_spec_dtau(0.20):.4f}")

# ===========================================================================
# 5. TOTAL EFFECTIVE POTENTIAL AND MODULUS EQUATION
# ===========================================================================

print("\n" + "="*70)
print("5. TOTAL EFFECTIVE POTENTIAL")
print("="*70)

def V_eff(tau, r_ba, eta):
    """Total effective potential: V_FR + V_spec."""
    return V_FR(tau, r_ba) + V_spec(tau, eta)

def dV_eff_dtau(tau, r_ba, eta):
    """dV_eff/dtau."""
    return dV_FR_dtau(tau, r_ba) + dV_spec_dtau(tau, eta)

def d2V_eff_dtau2(tau, r_ba, eta):
    """d^2 V_eff / dtau^2."""
    return d2V_FR_dtau2(tau, r_ba) + d2V_spec_dtau2(tau, eta)


# The MODULUS FIELD EQUATION is:
#
#   G_{tau tau} * Box(tau) + dV_eff/dtau = 0
#
# or equivalently:
#
#   Box(tau) = -(1/G_{tau tau}) * dV_eff/dtau
#
# For canonically normalized sigma = sqrt(G_{tau tau}) * tau:
#
#   Box(sigma) = -dV_eff/dsigma = -(1/sqrt(G_{tau tau})) * dV_eff/dtau

print("\nMODULUS FIELD EQUATION:")
print("  G_tt * Box(tau) + dV_eff/dtau = 0")
print(f"  G_tt = {G_TAU_TAU:.1f}")
print(f"  Box(tau) = -(1/{G_TAU_TAU:.1f}) * dV_eff/dtau")
print(f"  Canonical field: sigma = sqrt({G_TAU_TAU:.1f}) * tau = {np.sqrt(G_TAU_TAU):.4f} * tau")

# ===========================================================================
# 6. SOLITONIC DOMAIN WALL SOLUTIONS
# ===========================================================================
#
# For a static, planar domain wall along x, the modulus equation reduces to:
#
#   d^2(tau)/dx^2 = (1/G_{tau tau}) * dV_eff/dtau           ... (WALL ODE)
#
# This is the equation of a classical particle in the INVERTED potential
#   U(tau) = -V_eff(tau) / G_{tau tau}
#
# A SOLITONIC (kink) solution exists if V_eff has two critical points
# tau_1 < tau_2 with V_eff(tau_1) = V_eff(tau_2) (degenerate minima)
# or if there is a metastable minimum.
#
# For the FR double-well (beta/alpha < 0.313):
# tau=0 is a local min, tau_0 > 0 is the true min.
# A domain wall interpolates between them.

print("\n" + "="*70)
print("6. SOLITONIC DOMAIN WALL SOLUTIONS")
print("="*70)

# Scan parameter space to find domain wall solutions
r_ba_values = [0.20, 0.25, 0.28, 0.30]
eta_values = [0.0, 0.05, 0.10, 0.20, 0.50]

print("\n--- Scanning (beta/alpha, eta) for domain wall structure ---")
print(f"{'r_ba':>8} {'eta':>8} {'tau_min':>10} {'V_min':>10} {'tau_bar':>10} {'V_bar':>10} {'DeltaV':>10}")

wall_params = []
for r_ba in r_ba_values:
    for eta in eta_values:
        tau_s = np.linspace(0, 1.5, 20000)
        v_s = np.array([V_eff(t, r_ba, eta) for t in tau_s])
        dv_s = np.array([dV_eff_dtau(t, r_ba, eta) for t in tau_s])

        # Find extrema
        sc = np.where(np.diff(np.sign(dv_s)))[0]
        extrema = []
        for idx in sc:
            try:
                t0 = brentq(lambda t: dV_eff_dtau(t, r_ba, eta), tau_s[idx], tau_s[idx+1])
                extrema.append((t0, V_eff(t0, r_ba, eta), d2V_eff_dtau2(t0, r_ba, eta)))
            except:
                pass

        if len(extrema) >= 2:
            # Find the minimum and the barrier
            mins = [e for e in extrema if e[2] > 0]
            maxs = [e for e in extrema if e[2] < 0]
            if mins and maxs:
                deepest_min = min(mins, key=lambda e: e[1])
                barrier = maxs[0]
                delta_v = barrier[1] - deepest_min[1]
                print(f"{r_ba:8.2f} {eta:8.2f} {deepest_min[0]:10.4f} {deepest_min[1]:10.4f} "
                      f"{barrier[0]:10.4f} {barrier[1]:10.4f} {delta_v:10.4f}")
                wall_params.append({
                    'r_ba': r_ba, 'eta': eta,
                    'tau_min': deepest_min[0], 'V_min': deepest_min[1],
                    'tau_bar': barrier[0], 'V_bar': barrier[1],
                    'delta_V': delta_v
                })
            elif len(mins) >= 1:
                m = mins[0]
                print(f"{r_ba:8.2f} {eta:8.2f} {m[0]:10.4f} {m[1]:10.4f} {'--':>10} {'--':>10} {'--':>10}")
        elif len(extrema) == 1:
            e = extrema[0]
            nature = "MIN" if e[2] > 0 else "MAX"
            print(f"{r_ba:8.2f} {eta:8.2f} {e[0]:10.4f} {e[1]:10.4f} {'--':>10} {'--':>10} {nature:>10}")
        else:
            print(f"{r_ba:8.2f} {eta:8.2f} {'none':>10} {'--':>10} {'--':>10} {'--':>10} {'--':>10}")


# ===========================================================================
# 7. DOMAIN WALL PROFILE: tau(x)
# ===========================================================================
#
# For a kink solution between tau_1 (false vacuum at tau=0) and
# tau_2 (true vacuum at tau_0), the first integral gives:
#
#   (1/2) * G_{tau tau} * (dtau/dx)^2 = V_eff(tau) - V_eff(tau_2)
#
# => dtau/dx = sqrt(2 * (V_eff(tau) - V_eff(tau_2)) / G_{tau tau})
#
# The wall width is:
#   w = integral from tau_1 to tau_2 of dtau / sqrt(2*(V-V_2)/G_tt)
#
# The wall tension (energy per unit area) is:
#   sigma_wall = integral of G_tt * (dtau/dx)^2 dx
#              = integral sqrt(2 * G_tt * (V(tau) - V(tau_2))) dtau

print("\n" + "="*70)
print("7. DOMAIN WALL PROFILES")
print("="*70)

# Use beta/alpha = 0.28 (Weinberg angle prediction) as the primary case
r_ba_primary = 0.28

# For each eta, solve the wall ODE
for eta in [0.0, 0.05, 0.10, 0.20]:
    print(f"\n--- r_ba = {r_ba_primary}, eta = {eta:.2f} ---")

    # Find the two minima and the barrier
    tau_s = np.linspace(0, 1.5, 50000)
    v_s = np.array([V_eff(t, r_ba_primary, eta) for t in tau_s])
    dv_s = np.array([dV_eff_dtau(t, r_ba_primary, eta) for t in tau_s])

    # Find extrema
    sc = np.where(np.diff(np.sign(dv_s)))[0]
    extrema = []
    for idx in sc:
        try:
            t0 = brentq(lambda t: dV_eff_dtau(t, r_ba_primary, eta), tau_s[idx], tau_s[idx+1])
            v0 = V_eff(t0, r_ba_primary, eta)
            d2v = d2V_eff_dtau2(t0, r_ba_primary, eta)
            extrema.append((t0, v0, d2v))
        except:
            pass

    mins = sorted([e for e in extrema if e[2] > 0], key=lambda e: e[1])
    maxs = [e for e in extrema if e[2] < 0]

    if not mins:
        print("  No minimum found.")
        continue

    print(f"  Minima: {[(f'{e[0]:.4f}', f'{e[1]:.4f}') for e in mins]}")
    print(f"  Maxima: {[(f'{e[0]:.4f}', f'{e[1]:.4f}') for e in maxs]}")

    if len(mins) >= 2 or (len(mins) >= 1 and maxs):
        # Solve the wall ODE: d^2 tau / dx^2 = (1/G_tt) * dV/dtau
        # with boundary conditions tau(-inf) = tau_left, tau(+inf) = tau_right

        if len(mins) >= 2:
            tau_left = mins[0][0]
            tau_right = mins[1][0]
            V_ref = max(mins[0][1], mins[1][1])
        elif maxs:
            tau_left = 0.0  # tau=0 local min
            tau_right = mins[0][0]
            V_ref = V_eff(tau_left, r_ba_primary, eta)
        else:
            continue

        # Wall width estimate from thin-wall approximation:
        # w ~ delta_tau / sqrt(2 * Delta_V / G_tt)
        delta_tau = abs(tau_right - tau_left)

        if maxs:
            V_barrier = maxs[0][1]
            V_low = min(mins[0][1], mins[-1][1])
            delta_V = V_barrier - V_low

            if delta_V > 0:
                # Wall width
                w_est = delta_tau * np.sqrt(G_TAU_TAU / (2 * delta_V))

                # Wall tension (thin-wall approximation)
                sigma_est = delta_tau * np.sqrt(2 * G_TAU_TAU * delta_V)

                # Canonical mass of the modulus at the true minimum
                m_tau_sq = d2V_eff_dtau2(mins[0][0], r_ba_primary, eta) / G_TAU_TAU
                m_tau = np.sqrt(abs(m_tau_sq))

                print(f"  Wall parameters:")
                print(f"    tau_left = {tau_left:.4f}, tau_right = {tau_right:.4f}")
                print(f"    Delta_tau = {delta_tau:.4f}")
                print(f"    Barrier height Delta_V = {delta_V:.4f}")
                print(f"    Wall width estimate w ~ {w_est:.4f} (in M_KK^{-1} units)")
                print(f"    Wall tension sigma ~ {sigma_est:.4f}")
                print(f"    Modulus mass m_tau = {m_tau:.4f} M_KK")
                print(f"    Compton wavelength 1/m_tau = {1/m_tau:.4f} M_KK^{-1}")

    # Solve the wall ODE numerically
    if maxs and mins:
        tau_true = mins[0][0] if mins[0][1] < mins[-1][1] else mins[-1][0] if len(mins) > 1 else mins[0][0]
        tau_false = 0.0 if abs(mins[0][0]) > 0.01 else (mins[1][0] if len(mins) > 1 else mins[0][0])

        # Solve as initial value problem from near the unstable maximum
        if maxs:
            tau_top = maxs[0][0]
            V_top = maxs[0][1]

            # Perturbation from the top
            eps = 1e-4

            # Solve going right (toward true minimum)
            def wall_ode(x, y):
                tau, dtau_dx = y
                d2tau = (1.0 / G_TAU_TAU) * dV_eff_dtau(tau, r_ba_primary, eta)
                return [dtau_dx, d2tau]

            # Right-going solution
            y0_right = [tau_top + eps, eps * np.sqrt(abs(d2V_eff_dtau2(tau_top, r_ba_primary, eta)) / G_TAU_TAU)]
            sol_right = solve_ivp(wall_ode, [0, 50], y0_right, max_step=0.01,
                                  events=None, dense_output=True)

            # Left-going solution
            y0_left = [tau_top - eps, -eps * np.sqrt(abs(d2V_eff_dtau2(tau_top, r_ba_primary, eta)) / G_TAU_TAU)]
            sol_left = solve_ivp(wall_ode, [0, 50], y0_left, max_step=0.01,
                                 events=None, dense_output=True)

            # Combine into full wall profile
            x_left = -sol_left.t[::-1]
            tau_left_sol = sol_left.y[0][::-1]
            x_right = sol_right.t
            tau_right_sol = sol_right.y[0]

            x_wall = np.concatenate([x_left, x_right])
            tau_wall = np.concatenate([tau_left_sol, tau_right_sol])

            # Measure wall width at 10%-90% of full transition
            tau_range = [np.min(tau_wall), np.max(tau_wall)]
            t10 = tau_range[0] + 0.1 * (tau_range[1] - tau_range[0])
            t90 = tau_range[0] + 0.9 * (tau_range[1] - tau_range[0])

            idx10 = np.argmin(np.abs(tau_wall - t10))
            idx90 = np.argmin(np.abs(tau_wall - t90))
            if idx10 != idx90:
                w_numerical = abs(x_wall[idx90] - x_wall[idx10])
                print(f"    Numerical wall width (10-90%): {w_numerical:.4f}")

            # Does the wall straddle the dump point tau=0.19?
            if tau_range[0] < 0.19 < tau_range[1]:
                print(f"    WALL STRADDLES DUMP POINT tau=0.19: YES")
                # Find x position where tau = 0.19
                idx_dump = np.argmin(np.abs(tau_wall - 0.19))
                print(f"    tau(x_dump) = {tau_wall[idx_dump]:.4f} at x = {x_wall[idx_dump]:.4f}")
            else:
                print(f"    Wall straddles dump point: NO (range [{tau_range[0]:.3f}, {tau_range[1]:.3f}])")


# ===========================================================================
# 8. U(2) BREAKING ANALYSIS
# ===========================================================================

print("\n" + "="*70)
print("8. U(2) BREAKING FROM MODULUS EQUATION")
print("="*70)

print("""
STRUCTURAL ANALYSIS: Does the modulus equation break U(2)?

The Jensen deformation preserves U(2) by construction — it is the most
general SU(3) x SU(3)-invariant metric on SU(3) that factors through
the Cartan decomposition su(3) = u(2) + C^2.

The modulus equation Box(tau) + (1/G_tt) * dV'/dtau = 0 governs tau(x),
which parametrizes ONLY the Jensen family. Domain wall solutions tau(x)
are spatially varying tau along this family. At every spacetime point,
the internal geometry remains Jensen-deformed with the LOCAL value tau(x).

CONCLUSION: Domain wall solutions of the modulus equation do NOT break U(2).

The U(2) symmetry is preserved at EVERY point of the domain wall.
Schur orthogonality holds at every point. V_12/V_23 = 2.7 is locked
at every point. The wall modifies the LOCAL tau value but not the
representation-theoretic structure.

U(2) breaking requires departing from the Jensen family entirely:
1. Inner fluctuations phi (NEW-1): D_phys = D_K + phi + J*phi*J^{-1}
   This introduces a perturbation that breaks U(2) -> SU(2).
2. Off-Jensen transverse deformations (B-29d T2 direction):
   eps_T2 != 0 breaks U(2) -> smaller subgroup.

NEITHER of these is captured by the 1D modulus equation for tau(x).
The modulus equation describes shape-preserving (within Jensen)
spatial variation. To break U(2), one needs ADDITIONAL modulus fields
parametrizing the transverse directions in the full metric space.

This is consistent with Round 1 finding: V_12/V_23 = 2.7 LOCKED by
Schur at ALL wall configurations. The modulus equation confirms this
algebraically — the wall is a solution within the Jensen family.
""")


# ===========================================================================
# 9. DUMP POINT IN MODULUS EQUATION CONTEXT
# ===========================================================================

print("="*70)
print("9. DUMP POINT ANALYSIS")
print("="*70)

# At the dump point tau = 0.19, what does the modulus equation predict?
tau_dump = 0.19

for r_ba in [0.28, 0.30, 0.313]:
    for eta in [0.0, 0.10, 0.20]:
        force = dV_eff_dtau(tau_dump, r_ba, eta) / G_TAU_TAU
        curvature = d2V_eff_dtau2(tau_dump, r_ba, eta) / G_TAU_TAU
        print(f"  r_ba={r_ba:.3f}, eta={eta:.2f}: "
              f"Force = {force:.4f}, "
              f"Curvature = {curvature:.4f}, "
              f"{'RESTORING' if curvature > 0 else 'UNSTABLE'}")

# Check: does the FR minimum coincide with the dump point for any beta/alpha?
print(f"\n--- FR minimum vs dump point ---")
for r_ba in np.arange(0.15, 0.40, 0.01):
    tau_s = np.linspace(0.01, 1.0, 10000)
    dv_s = np.array([dV_FR_dtau(t, r_ba) for t in tau_s])
    sc = np.where(np.diff(np.sign(dv_s)))[0]
    for idx in sc:
        t0 = brentq(lambda t: dV_FR_dtau(t, r_ba), tau_s[idx], tau_s[idx+1])
        d2v = d2V_FR_dtau2(t0, r_ba)
        if d2v > 0 and abs(t0 - 0.19) < 0.02:
            print(f"  r_ba = {r_ba:.3f}: FR min at tau = {t0:.4f} (near dump!)")


# ===========================================================================
# 10. FIGURE: POTENTIAL AND WALL PROFILES
# ===========================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel A: V_eff for different beta/alpha with eta=0.10
ax = axes[0, 0]
tau_plot = np.linspace(0, 0.8, 1000)
eta_plot = 0.10
for r_ba in [0.20, 0.25, 0.28, 0.30, 0.313]:
    v_plot = [V_eff(t, r_ba, eta_plot) - V_eff(0, r_ba, eta_plot) for t in tau_plot]
    ax.plot(tau_plot, v_plot, label=f'beta/alpha={r_ba:.3f}')
ax.axvline(0.19, color='red', ls='--', alpha=0.5, label='dump point')
ax.set_xlabel('tau')
ax.set_ylabel('V_eff(tau) - V_eff(0)')
ax.set_title(f'V_eff with eta={eta_plot} (spectral correction)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel B: Effect of spectral action eta
ax = axes[0, 1]
r_ba_plot = 0.28
for eta in [0.0, 0.05, 0.10, 0.20, 0.50]:
    v_plot = [V_eff(t, r_ba_plot, eta) - V_eff(0, r_ba_plot, eta) for t in tau_plot]
    ax.plot(tau_plot, v_plot, label=f'eta={eta:.2f}')
ax.axvline(0.19, color='red', ls='--', alpha=0.5, label='dump point')
ax.set_xlabel('tau')
ax.set_ylabel('V_eff(tau) - V_eff(0)')
ax.set_title(f'V_eff: beta/alpha={r_ba_plot}, varying eta')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel C: Wall profile for best-case scenario
ax = axes[1, 0]
# Use r_ba=0.28, eta=0.10
r_ba_wall = 0.28
eta_wall = 0.10
tau_s = np.linspace(0, 1.0, 50000)
dv_s = np.array([dV_eff_dtau(t, r_ba_wall, eta_wall) for t in tau_s])
sc = np.where(np.diff(np.sign(dv_s)))[0]

if len(sc) >= 2:
    # Find barrier
    tau_bar = brentq(lambda t: dV_eff_dtau(t, r_ba_wall, eta_wall), tau_s[sc[0]], tau_s[sc[0]+1])

    eps = 1e-4
    def wall_ode_plot(x, y):
        tau_val, dtau_dx = y
        d2tau = (1.0 / G_TAU_TAU) * dV_eff_dtau(tau_val, r_ba_wall, eta_wall)
        return [dtau_dx, d2tau]

    curvature_at_bar = d2V_eff_dtau2(tau_bar, r_ba_wall, eta_wall)
    kick = eps * np.sqrt(abs(curvature_at_bar) / G_TAU_TAU) if curvature_at_bar != 0 else eps

    # Right
    y0r = [tau_bar + eps, kick]
    sol_r = solve_ivp(wall_ode_plot, [0, 30], y0r, max_step=0.005, dense_output=True)
    # Left
    y0l = [tau_bar - eps, -kick]
    sol_l = solve_ivp(wall_ode_plot, [0, 30], y0l, max_step=0.005, dense_output=True)

    x_full = np.concatenate([-sol_l.t[::-1], sol_r.t])
    tau_full = np.concatenate([sol_l.y[0][::-1], sol_r.y[0]])

    # Clip to physical range
    mask = (tau_full > -0.5) & (tau_full < 1.5)
    x_full = x_full[mask]
    tau_full = tau_full[mask]

    ax.plot(x_full, tau_full, 'b-', lw=2)
    ax.axhline(0.19, color='red', ls='--', alpha=0.5, label='dump point tau=0.19')
    ax.axhline(0.15, color='orange', ls=':', alpha=0.5, label='phi crossing tau=0.15')
    ax.set_xlabel('x (M_KK^{-1})')
    ax.set_ylabel('tau(x)')
    ax.set_title(f'Domain wall profile (r_ba={r_ba_wall}, eta={eta_wall})')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(-10, 10)

# Panel D: Modulus mass vs eta
ax = axes[1, 1]
eta_range = np.linspace(0, 0.5, 100)
m_tau_values = []
tau_min_values = []
for eta in eta_range:
    tau_s = np.linspace(0.01, 1.0, 10000)
    dv_s = np.array([dV_eff_dtau(t, 0.28, eta) for t in tau_s])
    sc = np.where(np.diff(np.sign(dv_s)))[0]
    found = False
    for idx in sc:
        t0 = brentq(lambda t: dV_eff_dtau(t, 0.28, eta), tau_s[idx], tau_s[idx+1])
        d2v = d2V_eff_dtau2(t0, 0.28, eta)
        if d2v > 0:
            m_sq = d2v / G_TAU_TAU
            m_tau_values.append(np.sqrt(m_sq))
            tau_min_values.append(t0)
            found = True
            break
    if not found:
        m_tau_values.append(np.nan)
        tau_min_values.append(np.nan)

ax2 = ax.twinx()
ax.plot(eta_range, m_tau_values, 'b-', lw=2, label='m_tau (M_KK)')
ax2.plot(eta_range, tau_min_values, 'r--', lw=2, label='tau_min')
ax.set_xlabel('eta (spectral action coupling)')
ax.set_ylabel('m_tau / M_KK', color='b')
ax2.set_ylabel('tau_min', color='r')
ax.set_title('Modulus mass and minimum position vs eta')
ax.axhline(0, color='gray', ls='-', alpha=0.3)
ax2.axhline(0.19, color='red', ls=':', alpha=0.3)
ax.legend(loc='upper left', fontsize=8)
ax2.legend(loc='upper right', fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('C:/sandbox/Ainulindale Exflation/tier0-computation/s33w3_modulus_equation.png', dpi=150)
print("\nFigure saved to tier0-computation/s33w3_modulus_equation.png")


# ===========================================================================
# 11. KEY NUMERICAL RESULTS
# ===========================================================================

print("\n" + "="*70)
print("11. KEY NUMERICAL RESULTS")
print("="*70)

# Summary table: for beta/alpha = 0.28, scan eta
print(f"\n{'eta':>6} {'tau_min':>10} {'m_tau':>10} {'w_wall':>10} {'sigma_w':>10} {'straddle':>10}")
for eta in [0.0, 0.05, 0.10, 0.15, 0.20, 0.30, 0.50]:
    tau_s = np.linspace(0.01, 1.5, 50000)
    v_s = np.array([V_eff(t, 0.28, eta) for t in tau_s])
    dv_s = np.array([dV_eff_dtau(t, 0.28, eta) for t in tau_s])

    sc = np.where(np.diff(np.sign(dv_s)))[0]
    extrema = []
    for idx in sc:
        try:
            t0 = brentq(lambda t: dV_eff_dtau(t, 0.28, eta), tau_s[idx], tau_s[idx+1])
            extrema.append((t0, V_eff(t0, 0.28, eta), d2V_eff_dtau2(t0, 0.28, eta)))
        except:
            pass

    mins = sorted([e for e in extrema if e[2] > 0], key=lambda e: e[0])
    maxs = [e for e in extrema if e[2] < 0]

    if len(mins) >= 1 and maxs:
        true_min = min(mins, key=lambda e: e[1])
        barrier = maxs[0]
        m_sq = true_min[2] / G_TAU_TAU
        m = np.sqrt(abs(m_sq))
        dt = abs(true_min[0] - barrier[0]) if barrier else 0
        dv = barrier[1] - true_min[1] if barrier else 0
        w = dt * np.sqrt(G_TAU_TAU / (2 * max(dv, 1e-10)))
        sigma = dt * np.sqrt(2 * G_TAU_TAU * max(dv, 1e-10))
        straddle = "YES" if (min(0, true_min[0]) <= 0.19 <= max(barrier[0], true_min[0])) else "NO"
        print(f"{eta:6.2f} {true_min[0]:10.4f} {m:10.4f} {w:10.4f} {sigma:10.4f} {straddle:>10}")
    elif len(mins) >= 1:
        true_min = mins[0]
        m_sq = true_min[2] / G_TAU_TAU
        m = np.sqrt(abs(m_sq))
        print(f"{eta:6.2f} {true_min[0]:10.4f} {m:10.4f} {'--':>10} {'--':>10} {'--':>10}")
    else:
        print(f"{eta:6.2f} {'none':>10} {'--':>10} {'--':>10} {'--':>10} {'--':>10}")


# ===========================================================================
# 12. CONNECTIONS TO KK LITERATURE
# ===========================================================================

print("\n" + "="*70)
print("12. KK LITERATURE CONNECTIONS")
print("="*70)

print("""
EINSTEIN-BERGMANN (Paper 04):
  Box(phi) = (phi/4) * F_{mu nu} * F^{mu nu}

  Our analog: Box(tau) = -(1/G_tt) * dV_eff/dtau

  The Einstein-Bergmann dilaton equation sources the scalar from the gauge
  field energy density. In our framework, the source is the TOTAL effective
  potential gradient including Freund-Rubin (classical) and spectral action
  (quantum) contributions.

KERNER (Paper 06):
  R_P = R_M4 + R_K + (1/4)*F^2

  R_K(tau) is constant in Kerner (Killing metric). In our framework,
  Jensen deformation makes R_K tau-dependent, giving a non-trivial
  potential V_FR = -R_K(tau) + beta/alpha * |omega_3|^2(tau).

  The domain wall tau(x) makes R_K position-dependent on M^4.
  This is Kerner's fiber bundle with a SPATIALLY VARYING fiber metric.

FREUND-RUBIN (Paper 10):
  Flux F drives opposite-sign stress-energy in spacetime and internal dims.
  V_FR(tau) = -R_K(tau) + (beta/alpha)*|omega_3|^2(tau) is the generalization
  to Jensen-deformed SU(3). The critical ratio beta/alpha = 0.313 separates
  round-metric stability from spontaneous Jensen deformation.

DUFF-NILSSON-POPE (Paper 11):
  Stability: L >= 3*m^2 for TT tensor perturbations.
  Our spectral action curvature d^2S/dtau^2 = 20.43 at tau=0.20 is the
  quantum analog of the Lichnerowicz stability criterion.
  The modulus mass m_tau^2 = V_eff''(tau_min) / G_tt gives the KK scale
  of the modulus excitation.
""")

# ===========================================================================
# 13. SAVE RESULTS
# ===========================================================================

np.savez('C:/sandbox/Ainulindale Exflation/tier0-computation/s33w3_modulus_equation.npz',
         G_tau_tau=G_TAU_TAU,
         chi_0=chi_0,
         chi_1=chi_1,
         r_ba_primary=r_ba_primary,
         tau_dump=tau_dump,
         wall_params=np.array([(wp['r_ba'], wp['eta'], wp['tau_min'], wp['tau_bar'], wp['delta_V'])
                               for wp in wall_params]) if wall_params else np.array([]))

print("\nResults saved to tier0-computation/s33w3_modulus_equation.npz")
print("\nDONE.")
