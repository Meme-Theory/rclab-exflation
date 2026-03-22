# Session 26 Priority 2: Coupled Cooling-Trajectory ODE System

## Design Document for Modulus Lock via Transient BCS Condensation

---

## 1. Physical Setup

At the Planck epoch, the internal manifold SU(3) sits at some initial modulus value
tau_i and the substrate chemical potential mu is large (mu >> lambda_min). As the
universe expands, mu dilutes. When mu passes through the condensation window
[mu_c, mu_upper] * lambda_min(tau), a BCS condensate forms in the (0,0) singlet
sector of D_K, generating a tau-dependent free energy F_cond(tau, mu). The question
is whether this transient condensate produces sufficient gradient dF_cond/dtau to
trap (lock) the modulus before mu drops below mu_c and the condensate evaporates.

**Variables:**
- tau(t): Jensen deformation parameter (internal geometry modulus)
- Delta(t): BCS gap magnitude (condensate order parameter)
- mu(t): substrate chemical potential (dilutes with expansion)
- H(t): Hubble parameter (set by total energy density)

**Time coordinate:** Cosmic time t, with H = (da/dt)/a = d(ln a)/dt.

---

## 2. The Coupled ODE System

### 2.1 Modulus equation: tau(t)

The modulus tau is a scalar field on M^4 with kinetic term (1/2) G_{tau,tau} (dtau/dt)^2.
From the Session 22a/22d computations, the moduli space metric is:

    G_{tau,tau} = 5

(Stored in `s22d_rolling_trajectories.npz` and `s22a_slow_roll.npz` as `G_tt = 5`.)

This is the normalization from the Connes-Chamseddine spectral action: the tau kinetic
term in 4D appears as (G_{tau,tau}/2) * g^{mu nu} partial_mu tau partial_nu tau, so
the homogeneous-mode equation of motion is:

    G_{tau,tau} * [d^2 tau/dt^2 + 3H dtau/dt] = - dV_eff/dtau

Equivalently:

    d^2 tau/dt^2 = -(1/G_{tau,tau}) * dV_eff/dtau - 3H * dtau/dt      ... (EOM-tau)

Rewrite as first-order system. Define pi_tau = dtau/dt:

    dtau/dt = pi_tau                                                     ... (ODE-1)

    dpi_tau/dt = -(1/5) * dV_eff/dtau - 3H * pi_tau                     ... (ODE-2)

where V_eff(tau, mu, Delta) = V_spec(tau) + V_BCS(tau, mu, Delta).


### 2.2 Gap equation: Delta(t)

The BCS gap evolves on the scale of the inverse gap frequency ~ 1/|Delta|.
In TDGL (time-dependent Ginzburg-Landau) formulation:

    gamma_Delta * dDelta/dt = -delta F_BCS / delta Delta

where gamma_Delta is the dissipative coefficient. For a BCS system, the relaxation
rate toward the instantaneous equilibrium gap is:

    tau_GL ~ hbar / (k_B T_c)    (Ginzburg-Landau relaxation time)

In natural units (hbar = c = k_B = 1) with T_c ~ 0.03 * lambda_min:

    tau_GL ~ 1 / T_c ~ 33 / lambda_min

The gap equation at each instant defines the "target" gap Delta_eq(tau, mu, T):

    Delta_eq = self-consistent solution of:
    Delta_n = sum_m V_{nm} * [tanh(E_m/2T) / (2 E_m)] * Delta_m

    where E_m = sqrt((lambda_m(tau) - mu)^2 + Delta_m^2)

For the ODE system, we use TDGL relaxation toward the instantaneous equilibrium:

    dDelta/dt = -(1/tau_GL) * (Delta - Delta_eq(tau, mu, T))            ... (ODE-3)

**Implementation note:** Delta here is the scalar norm |Delta| of the 16-component
gap vector. The direction in gap-vector space is slaved to the instantaneous
equilibrium direction (which is set by the V_{nm} eigenvector structure). This
is justified because the angular relaxation in gap space is fast compared to
the radial relaxation.

**Alternative (adiabatic) limit:** If H * tau_GL << 1 (gap relaxes much faster
than Hubble), then Delta adiabatically follows Delta_eq(tau, mu):

    Delta(t) = Delta_eq(tau(t), mu(t))      [adiabatic]

We will implement both: the full TDGL ODE-3 and the adiabatic limit for comparison.


### 2.3 Chemical potential: mu(t)

The substrate provides chemical potential mu. For a relativistic species in an
expanding FRW background, the number density dilutes as n ~ a^{-3} and the
chemical potential of a relativistic Fermi gas scales as:

    mu ~ n^{1/3} ~ a^{-1}

Therefore:

    dmu/dt = -H * mu                                                    ... (ODE-4)

This gives mu(t) = mu_0 * (a_0/a(t)), exact for relativistic dilution.

**Important:** lambda_min(tau) itself depends on tau. The condensation window is
defined in terms of mu/lambda_min(tau), so the effective parameter is the ratio
r(t) = mu(t) / |lambda_min(tau(t))|. The system enters the condensation window
when r drops below ~1.2-1.5 and exits when r drops below ~0.76-0.80.


### 2.4 Hubble parameter: H(t)

The Friedmann equation gives:

    H^2 = (8 pi G / 3) * rho_total

In natural units with M_Pl = 1/sqrt(8 pi G):

    H^2 = rho_total / (3 M_Pl^2)

The total energy density has four contributions:

    rho_total = rho_rad + rho_tau + rho_spec + rho_BCS

where:

    rho_rad = rho_{rad,0} * (a_0/a)^4          [radiation bath]

    rho_tau = (G_{tau,tau}/2) * pi_tau^2        [modulus kinetic energy]

    rho_spec = V_spec(tau)                       [spectral action potential]

    rho_BCS = V_BCS(tau, mu, Delta)             [BCS condensation energy]

The Hubble equation is algebraic, not differential:

    H = sqrt(rho_total / (3 M_Pl^2))                                   ... (EQ-H)

We do NOT need a separate dH/dt ODE. Instead, H is evaluated from the
instantaneous state (tau, pi_tau, mu, Delta) at each timestep.

**Simplification for the Planck-era:** Near the Planck time, rho_rad dominates
and H ~ 1/(2t) (radiation era). The spectral action contributions V_spec and
V_BCS are subdominant to rho_rad by construction (they are loop-level effects
in the spectral action, suppressed by powers of the cutoff).

The ODE system is therefore **3-variable** (tau, pi_tau, mu) plus an algebraic
equation for H and an instantaneous lookup for Delta_eq:

**Final system:**

    dtau/dt   = pi_tau
    dpi_tau/dt = -(1/5) * dV_eff/dtau(tau, mu) - 3H(tau, pi_tau, mu) * pi_tau
    dmu/dt    = -H(tau, pi_tau, mu) * mu

**Or, with explicit TDGL dynamics for Delta (4-variable system):**

    dtau/dt     = pi_tau
    dpi_tau/dt  = -(1/5) * dV_eff/dtau(tau, mu, Delta) - 3H * pi_tau
    dmu/dt      = -H * mu
    dDelta/dt   = -(1/tau_GL) * (Delta - Delta_eq(tau, mu))

---

## 3. V_spec(tau): Spectral Action Potential

### 3.1 Available Data

From `s24a_vspec.npz`, V_spec(tau) is available at 9 rho (cutoff) values on a
21-point tau grid [0.0, 0.1, ..., 2.0]:

| rho   | V_spec(tau=0) | V_spec(tau=0.5) | Character      |
|-------|---------------|-----------------|----------------|
| 0.001 | -0.030        | 0.279           | nearly flat     |
| 0.01  | 17.7          | 23.39           | monotone up     |
| 0.05  | 96.5          | 126.1           | monotone up     |
| 0.1   | 195.0         | 254.5           | monotone up     |
| 0.5   | 983.0         | 1281.6          | monotone up     |

**CRITICAL FACT (V-1 closure):** V_spec(tau) is monotonically increasing for ALL rho
values. There is no Starobinsky minimum. The a_4 (quadratic curvature) term
dominates a_2 (linear curvature) by a factor of 1000:1 at tau=0.

### 3.2 Choice of rho

The physical cutoff rho sets the UV scale of the spectral action. For the
Planck-era dynamics, we need rho ~ Lambda_Pl^{-2} in appropriate units. The
precise rho value enters as an overall scale of V_spec. Since V_spec is monotonically
increasing regardless of rho, the qualitative dynamics are rho-independent.

**For the ODE integration, use rho = 0.01 as the reference.** This gives
V_spec(tau=0) = 17.7, V_spec(tau=0.5) = 23.39.

### 3.3 Interpolation

V_spec is given on 21 tau points [0.0, 0.1, ..., 2.0]. We need:
1. V_spec(tau) for arbitrary tau (use cubic spline interpolation)
2. dV_spec/dtau for the force term (use spline derivative)

**From `s22a_slow_roll.npz`:** V_prime and V_double_prime are available on the
same 21-point grid. These can be used as cross-checks. V_prime(tau=0) = 1.09e7
and V_double_prime(tau=0) = 2.41e8 from the full CW potential, which includes
the one-loop contribution. For the spectral action alone:

    dV_spec/dtau at tau=0 ~ (V_spec(0.1) - V_spec(0)) / 0.1
                           = (17.75 - 17.70) / 0.1 = 0.50   (rho=0.01)

This is many orders of magnitude smaller than the CW V_prime because V_spec at
rho=0.01 is the bare spectral action, not the CW effective potential.

**Implementation:** Use `scipy.interpolate.CubicSpline` on the V_spec_rho_0p010
array vs tau array. Evaluate V and dV/dtau from the spline object.

---

## 4. V_BCS(tau, mu, Delta): BCS Condensation Free Energy

### 4.1 Definition

From the P1 computation (`s26_multimode_bcs.py`, function `free_energy_bcs`):

    F_cond = -sum_n [sqrt(xi_n^2 + Delta_n^2) - |xi_n|]
             + (1/2) sum_{n,m} Delta_n * [V^{-1}]_{nm} * Delta_m

where xi_n = lambda_n(tau) - mu.

The BCS contribution to the effective potential is:

    V_BCS(tau, mu, Delta) = F_cond(tau, mu, Delta)

At the self-consistent solution Delta = Delta_eq:

    V_BCS(tau, mu) = F_cond(tau, mu, Delta_eq(tau, mu))

### 4.2 Available Discrete Data

The P1 computation provides:

1. **M_max_phase_diagram** (9 tau x 201 mu points): Linearized M_max. The
   condensation boundary is where M_max first exceeds 1.0.

2. **Self-consistent F_cond** at 9 tau x 12 mu/lmin values:
   mu/lmin in {0.00, 0.50, 0.80, 0.90, 0.95, 1.00, 1.05, 1.10, 1.20, 1.50, 2.00, 3.00}

   Nonzero F_cond exists only in the window mu/lmin ~ [0.90, 1.20]:

   | tau  | mu/lmin=0.95 | 1.00   | 1.05   | 1.10   |
   |------|-------------|--------|--------|--------|
   | 0.00 | -0.094      | -0.375 | -0.094 | 0.000  |
   | 0.10 | -0.035      | -0.457 | -0.304 | -0.084 |
   | 0.15 | -0.040      | -0.193 | -0.166 | -0.039 |
   | 0.20 | -0.055      | -0.158 | -0.168 | -0.040 |
   | 0.25 | -0.082      | -0.148 | -0.210 | -0.040 |
   | 0.30 | -0.123      | -0.068 | -0.197 | -0.157 |
   | 0.35 | -0.075      | -0.196 | -0.226 | -0.081 |
   | 0.40 | -0.082      | -0.210 | -0.243 | -0.111 |
   | 0.50 | -0.143      | -0.283 | -0.282 | -0.127 |

3. **|Delta| at self-consistency** at same grid points:

   | tau  | mu/lmin=0.95 | 1.00  | 1.05  | 1.10  |
   |------|-------------|-------|-------|-------|
   | 0.00 | 0.134       | 0.184 | 0.134 | 0.000 |
   | 0.20 | 0.112       | 0.172 | 0.186 | 0.113 |
   | 0.50 | 0.218       | 0.278 | 0.293 | 0.230 |

4. **Eigenvalues** (16 modes per tau):
   lambda_min increases monotonically from 0.866 (tau=0) to 1.243 (tau=0.50).

5. **Critical mu** (where linearized M_max diverges):
   mu_c/lambda_min ~ 0.75-0.80 at all tau.

6. **Critical temperature**: T_c/lambda_min ~ 0.017-0.052.

### 4.3 Interpolation Strategy for V_BCS

The ODE integrator will request V_BCS(tau, mu) at arbitrary (tau, mu). We need to
build a 2D interpolant from the discrete data.

**Step 1: Define the condensation boundary.**
Outside the window [mu_c, mu_upper] * lambda_min(tau), set V_BCS = 0 identically.

The window boundaries from M_max > 1.0:
- Lower: mu/lmin ~ 0.875-0.925 (tau-dependent, use M_max_phase_diagram)
- Upper: mu/lmin ~ 1.075-1.425 (tau-dependent, widens at large tau)

**Step 2: Interpolate within the window.**
The 12 discrete mu/lmin values give sparse coverage of the condensation window.
Only 4-5 mu points fall in the nonzero-F_cond region for each tau. Options:

**(A) Direct 2D spline on the (tau, mu/lmin) grid.** Use
`scipy.interpolate.RegularGridInterpolator` with the 9x12 F_cond table, padding
zeros outside the window. Drawback: 12 mu points is coarse.

**(B) Parametric model.** Fit F_cond to a Gaussian-in-mu profile at each tau:

    F_cond(tau, mu) = A(tau) * exp(-(mu/lmin - mu_peak(tau))^2 / (2 sigma_mu(tau)^2))

where A(tau), mu_peak(tau), sigma_mu(tau) are interpolated from the 9 tau values.
This respects the physical shape (peaked near mu = lambda_min, zero far away).

**(C) Reconstruct from BdG on finer grid at runtime.** Too expensive for ODE RHS.

**RECOMMENDED: Option (B)** with a cross-check against Option (A). The physical
shape of F_cond vs mu is approximately Gaussian, peaked near mu/lmin ~ 1.0-1.05,
with width sigma ~ 0.05-0.10 in mu/lmin units. Fit at each of the 9 tau values,
then use cubic spline interpolation in tau for A, mu_peak, sigma.

**Step 3: Compute dV_BCS/dtau.**
Two contributions:

    dV_BCS/dtau = (partial F_cond / partial tau)|_{mu fixed}
                + (partial F_cond / partial lambda_min) * (d lambda_min / d tau)

The second term accounts for the tau-dependence of the condensation window itself.
Both can be computed from the parametric model by differentiating A(tau), mu_peak(tau),
sigma(tau), and lambda_min(tau).

### 4.4 Lambda_min(tau) Interpolation

From eigenvalue data:

| tau  | lambda_min |
|------|-----------|
| 0.00 | 0.8660    |
| 0.10 | 0.9158    |
| 0.15 | 0.9454    |
| 0.20 | 0.9782    |
| 0.25 | 1.0142    |
| 0.30 | 1.0534    |
| 0.35 | 1.0958    |
| 0.40 | 1.1415    |
| 0.50 | 1.2430    |

Use cubic spline on these 9 points. The derivative d(lambda_min)/dtau is needed
for the chain rule in dV_BCS/dtau.

---

## 5. Equation of State and Energy Budget

### 5.1 Radiation Dominance

At the relevant epoch (mu ~ lambda_min in Planck units), the universe is deep
in the radiation era. The radiation energy density is:

    rho_rad = (pi^2 / 30) * g_* * T^4

where g_* ~ 106.75 (SM degrees of freedom). At T ~ M_Pl, rho_rad ~ M_Pl^4.
The spectral action contributions are loop-suppressed:

    V_spec ~ O(10-1000) in Planck units at rho = 0.01
    V_BCS  ~ O(0.1-0.5) in Planck units

Both are negligible compared to rho_rad ~ O(M_Pl^4). This means:

1. H is set almost entirely by radiation: H ~ 1/(2t) (radiation-era Hubble).
2. The modulus dynamics are a test-field problem on a radiation-dominated background.
3. Back-reaction of V_spec + V_BCS on H is negligible.

### 5.2 Simplified Hubble

In the radiation era:

    H(t) = 1/(2t)     =>     a(t) ~ t^{1/2}

Or equivalently, using temperature as clock:

    H = (pi / 3) * sqrt(g_* / 10) * T^2 / M_Pl

The mu dilution equation dmu/dt = -H*mu integrates exactly:

    mu(t) = mu(t_0) * sqrt(t_0 / t)

### 5.3 Dimensionless Formulation

To avoid huge dynamic range, define dimensionless variables. Let lambda_0 = lambda_min(tau=0) = 0.866 be the reference energy scale. Define:

    s = lambda_0 * t          (dimensionless time)
    tilde_tau = tau            (already dimensionless)
    tilde_mu = mu / lambda_0  (dimensionless chemical potential)
    tilde_H = H / lambda_0    (dimensionless Hubble)
    tilde_Delta = Delta / lambda_0  (dimensionless gap)
    tilde_V = V / lambda_0^4  (dimensionless potential, if needed)

The key ratio is:

    r(s) = mu(s) / |lambda_min(tau(s))|

Condensation occurs when r is in the window [~0.76, ~1.4].

**However,** since V_spec and V_BCS are negligible in the Friedmann equation, the
Hubble sector decouples. We can parameterize H externally:

    H(s) = H_0 * (s_0/s)      [radiation era, H ~ 1/t]

and the remaining system is:

    dtau/ds   = pi_tau / lambda_0
    dpi_tau/ds = -(1/(5 lambda_0)) * dV_eff/dtau - 3 * H(s) * pi_tau / lambda_0
    dmu/ds    = -H(s) * mu / lambda_0

With H(s) prescribed, this is a 3-variable non-autonomous system.

---

## 6. Initial Conditions

### 6.1 Physical Motivation

At the Planck time t_Pl ~ 5.4e-44 s:

- **tau(0):** Unknown initial modulus. Scan over tau_i in [0.0, 0.5] with
  emphasis on tau_i near the phi_paasch value (tau ~ 0.15).

- **pi_tau(0):** Initial modulus velocity. Natural scale: pi_tau ~ H_i * tau_i
  (Hubble-drag-limited). Start with pi_tau = 0 (modulus initially at rest)
  as the default, then scan.

- **mu(0):** Initial chemical potential. Must be large: mu_0 >> lambda_min.
  Scan mu_0/lambda_min in [5, 100]. The mu_0 = 5*lambda_min case gives a
  short condensation window; mu_0 = 100*lambda_min gives a long approach.

- **Delta(0):** Initial gap. Zero (no condensate exists above the window).
  Will nucleate as mu enters the window.

### 6.2 Scan Parameters

Primary scan (1D, most diagnostic):
- Fix tau_i = 0.15 (phi_paasch point), pi_tau_i = 0, Delta_i = 0
- Scan mu_0 / lambda_min(tau_i) in [2, 50] (20 values, log-spaced)

Secondary scans (2D):
- Fix mu_0/lmin = 10, scan tau_i in [0.0, 0.5] x pi_tau_i in [-0.1, 0.1]
- Fix tau_i = 0.15, mu_0/lmin = 10, scan H_0 * lambda_0 in [0.01, 1.0]

### 6.3 H_0 Setting

In the radiation era at temperature T:

    H = sqrt(pi^2 g_* / 90) * T^2 / M_Pl

When mu = mu_0 >> lambda_min, the temperature is T ~ mu_0 (for a relativistic
species). So:

    H_0 / lambda_0 ~ (lambda_0 / M_Pl) * (mu_0 / lambda_0)^2 * sqrt(g_*)

Since lambda_0 << M_Pl (the eigenvalue is O(1) in Planck units while M_Pl is the
Planck mass), we have H_0 << lambda_0 for any reasonable mu_0. This means the
Hubble damping is weak compared to the gap dynamics timescale.

**Parametric exploration:** Treat H_0 * tau_GL as the key dimensionless parameter.

    H_0 * tau_GL ~ (H_0 / lambda_0) * (lambda_0 / T_c) ~ (H_0 / T_c)

If H_0 * tau_GL << 1: gap is adiabatic (tracks equilibrium).
If H_0 * tau_GL >> 1: gap cannot form before mu dilutes past the window.

---

## 7. Constraint Condition

### 7.1 Mathematical Statement

The condensate evaporates when mu drops below the critical threshold:

    mu(t) < mu_c(tau(t))

where mu_c(tau) = 0.76-0.80 * |lambda_min(tau)| (from P1 data, `mu_critical` array).

Define the critical ratio:

    r_c(tau) = mu_c(tau) / |lambda_min(tau)| ~ 0.76  (weakly tau-dependent)

**CLOSED closes if:** At the moment mu(t_exit) = mu_c(tau(t_exit)):
- |Delta(t_exit)| < Delta_threshold (condensate did not form or is too weak)
- AND/OR tau(t_exit) is not trapped (d^2 V_eff/dtau^2 < 0 at tau(t_exit))

**LOCK succeeds if:** Before t_exit:
- tau settles to a value tau_lock where d^2 V_eff/dtau^2 > 0
- The saxion mass m_saxion^2 = (1/G_{tau,tau}) * d^2 V_eff/dtau^2 > H^2 (oscillation faster than expansion)
- The condensate free energy |F_cond| is large enough to overcome V_spec slope

### 7.2 Quantitative Estimate: Can V_BCS Overcome V_spec?

Cubic spline interpolation of the P1 data gives the following gradient comparison
at mu/lmin = 1.00:

| tau  | dV_spec/dtau | dV_BCS/dtau | Net dV_eff/dtau |
|------|-------------|-------------|-----------------|
| 0.00 | -0.100      | -13.32      | -13.42 (BCS dominates, pushes tau UP) |
| 0.10 | +1.51       | +6.06       | +7.57 (both push tau DOWN)             |
| 0.15 | +3.26       | +3.10       | +6.35 (comparable, both push DOWN)     |
| 0.20 | +5.63       | -0.50       | +5.12 (V_spec dominates)               |
| 0.30 | +12.20      | -0.57       | +11.64 (V_spec dominates)              |

The sign convention: dV_eff/dtau > 0 means V_eff increases with tau, producing
a restoring force toward tau = 0 (via dpi_tau/dt = -(1/5)*dV_eff/dtau).

**Key observation:** F_cond at mu/lmin=1.0 has a deep minimum near tau=0.10
(F=-0.457), with the gradient pattern:
- tau < 0.10: dF_BCS/dtau < 0 (F_cond becomes more negative, BCS deepens)
- tau > 0.10: dF_BCS/dtau > 0 (F_cond becomes less negative, BCS weakens)

This creates a tau-attraction toward tau ~ 0.10 from the BCS sector. However,
V_spec is monotonically increasing with dV_spec/dtau > 0 for tau > 0, so the
net force pushes tau DOWN (toward tau=0) everywhere except near tau=0 where
V_spec is nearly flat.

The net gradient is POSITIVE (restoring toward tau=0) at all tau > 0 when
mu/lmin = 1.0, meaning V_eff(tau) is an increasing function. There is NO local
minimum -- the BCS contribution deepens the well at low tau but does not create
a new minimum at finite tau.

**Preliminary assessment:** Lock requires either:
1. A tau region where dV_BCS/dtau is sufficiently negative to overcome dV_spec/dtau,
   creating a local minimum. From the table, this does NOT happen at mu/lmin=1.00
   (the BCS gradient has the SAME sign as V_spec for tau > 0.10).
2. A different mu/lmin value where the F_cond profile has stronger tau-gradients.
3. The dynamical interplay: as tau evolves, mu/lmin changes (because lambda_min
   depends on tau), shifting the F_cond profile. This nonlinear coupling could
   create transient trapping not visible in the static analysis.

**The ODE integration is needed to resolve case (3).**

---

## 8. Numerical Integration Strategy

### 8.1 Stiffness Analysis

The system has two timescales:
1. **Hubble time** t_H = 1/H: cosmological expansion
2. **Gap relaxation** tau_GL = 1/T_c ~ 33/lambda_min: BCS dynamics

If tau_GL << t_H (likely for Planck-era H), the gap is adiabatic and the system
is NOT stiff. Use the adiabatic approximation (Delta = Delta_eq) as default.

If we include explicit TDGL dynamics, the stiffness ratio is:

    t_H / tau_GL ~ H * tau_GL

which could be large near the Planck time. In this case, use a stiff integrator.

### 8.2 Recommended Integrator

**Primary:** `scipy.integrate.solve_ivp` with method `'Radau'` (implicit Runge-Kutta,
L-stable, handles stiff systems). Adaptive step control with rtol=1e-10, atol=1e-12.

**Fallback:** `'RK45'` (explicit, non-stiff) for the adiabatic limit where
Delta is slaved to equilibrium and the system is 3-variable.

### 8.3 Event Detection

Use `solve_ivp` events to detect:

1. **Window entry:** mu(t) = mu_upper * lambda_min(tau(t))
   Direction: mu decreasing (terminal=False).

2. **Window exit (CLOSED):** mu(t) = mu_c(tau(t))
   Direction: mu decreasing (terminal=True). Stops integration.

3. **Lock detection:** dV_eff/dtau = 0 (force balance)
   Direction: any (terminal=False). Record for diagnostics.

### 8.4 Interpolation Infrastructure (Pre-computation)

Before integration, build all interpolants:

1. `V_spec_spline`: CubicSpline(tau_grid, V_spec_rho_0p010)
2. `lambda_min_spline`: CubicSpline(tau_bcs_grid, |lambda_min_values|)
3. `F_cond_interp`: 2D interpolant of F_cond(tau, mu/lmin) from P1 data
4. `Delta_eq_interp`: 2D interpolant of |Delta_eq|(tau, mu/lmin) from P1 data
5. `mu_c_spline`: CubicSpline(tau_bcs_grid, mu_critical_values)

**Grid alignment issue:** V_spec is on a 21-point grid (tau = 0.0 to 2.0, step 0.1).
BCS data is on a 9-point grid (tau = 0.0, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50).
The BCS grid is a subset of the V_spec grid (except for the non-round-number values
0.15, 0.25, 0.35). This is fine for interpolation -- the cubic splines handle different
input grids independently.

**WARNING: F_cond tau-interpolation artifacts.** Cubic spline interpolation of
F_cond on the 9-point tau grid produces multiple spurious oscillatory extrema
(5-7 sign changes in dF/dtau between tau=0 and 0.5). The raw F_cond data is
non-monotonic but smooth on the scale of the tau spacing (0.05-0.10). The
oscillations are Runge-phenomenon artifacts from the irregular grid spacing.

**Mitigation:** Use monotone piecewise cubic Hermite interpolation
(`scipy.interpolate.PchipInterpolator`) instead of CubicSpline for F_cond(tau)
and Delta_eq(tau). PCHIP preserves monotonicity between data points and does not
introduce spurious extrema. Alternatively, use linear interpolation as a robust
fallback and report sensitivity to interpolation method.

---

## 9. Diagnostic Extraction

### 9.1 Saxion Mass

At any point along the trajectory where a tau minimum exists:

    m_saxion^2 = (1/G_{tau,tau}) * d^2 V_eff / dtau^2 |_{tau=tau_lock}
               = (1/5) * [d^2 V_spec/dtau^2 + d^2 V_BCS/dtau^2]

Evaluate from the spline second derivatives. Compare to H^2: if m_saxion > H,
the modulus oscillates (trapped). If m_saxion < H, Hubble friction prevents
oscillation (no lock).

### 9.2 Q_tau of Lock

The quality factor of the tau trap is defined as:

    Q_tau = tau_lock / FWHM

where FWHM is the full width at half maximum of the potential well V_eff(tau)
around the lock point. Compute by finding the tau values where:

    V_eff(tau) = V_eff(tau_lock) + (1/2) * |V_eff(tau_lock)|

If no well exists, Q_tau = 0 (no lock).

### 9.3 Landau-Zener Probability

As tau evolves, the D_K eigenvalues lambda_n(tau) change. Near an avoided crossing
between levels n and m (spacing delta_nm(tau)), the adiabatic approximation can
fail. The Landau-Zener transition probability is:

    P_LZ = exp(-2 pi * delta_nm^2 / (|d(lambda_n - lambda_m)/dtau| * |dtau/dt|))

From the eigenvalue data, identify the minimum level spacings:

    delta_nm(tau) = min_{n != m} |lambda_n(tau) - lambda_m(tau)|

The eigenvalue velocity is:

    d(lambda_n - lambda_m)/dtau ~ [delta_nm(tau+epsilon) - delta_nm(tau-epsilon)] / (2 epsilon)

Evaluate P_LZ along the trajectory. If P_LZ ~ 1 at any point, the adiabatic
gap assignment breaks down and non-adiabatic transitions scramble the BCS channel.

**From existing data:** The Berry curvature B = 982.5 at tau=0.10 (from Session 24a)
indicates strong level repulsion. At tau=0 the spectrum is degenerate (lambda_min
has multiplicity 3), and degeneracies break as tau increases. The avoided crossings
are in the regime tau ~ 0.0-0.1.

Compute from the 9-point eigenvalue arrays: at each tau, find the smallest gap
between distinct |lambda| levels.

---

## 10. Complete Data Dependencies

### 10.1 Files Required

| File | Keys Used | Purpose |
|------|-----------|---------|
| `s24a_vspec.npz` | `tau`, `V_spec_rho_0p010` | V_spec(tau) spline |
| `s26_multimode_bcs.npz` | `tau_values`, `eigenvalues_{i}`, `mu_critical` | lambda_min(tau), mu_c(tau) |
| `s26_multimode_bcs.npz` | `sc_Fcond_{i}_{mu}`, `sc_Dnorm_{i}_{mu}` | F_cond and Delta_eq tables |
| `s26_multimode_bcs.npz` | `M_max_phase_diagram`, `mu_scan_ratios` | Condensation window boundaries |
| `s26_multimode_bcs.npz` | `T_critical` | T_c for tau_GL estimate |
| `s22a_slow_roll.npz` | `G_tt` | Moduli space metric G_{tau,tau} = 5 |

### 10.2 Interpolation/Fitting Tasks (Pre-integration)

1. **V_spec(tau) cubic spline** from 21-point tau grid.
   Output: V_spec(tau), dV_spec/dtau, d^2V_spec/dtau^2 callable.

2. **lambda_min(tau) cubic spline** from 9-point tau grid.
   Output: lambda_min(tau), d(lambda_min)/dtau callable.

3. **mu_c(tau) cubic spline** from 9-point tau grid.
   Output: mu_c(tau) callable.

4. **F_cond(tau, r) 2D interpolant** where r = mu/lambda_min.
   Build from the 9x12 self-consistent F_cond table. Pad zeros outside the
   condensation window.

   **Recommended method:** At each of 9 tau values, fit F_cond(r) to:

       F_cond(r) = A * exp(-(r - r_peak)^2 / (2 sigma^2))     for r in [r_c, r_max]
                 = 0                                             otherwise

   where A < 0 (condensation lowers energy). This gives A(tau), r_peak(tau),
   sigma(tau) as 9-point arrays, then interpolate each with a cubic spline.

5. **Delta_eq(tau, r) 2D interpolant** with same structure as F_cond.

6. **Level spacings** for Landau-Zener: compute min |lambda_n - lambda_m| at each tau
   from the eigenvalue arrays.

### 10.3 Quantities NOT Available (Must Be Modeled)

1. **H_0:** The initial Hubble rate. Parameterized, not computed from first principles.
   Physical range: H_0/lambda_0 in [1e-6, 1e-1] (Planck-era to sub-Planckian).

2. **Radiation density rho_rad:** Sets H. Since V_spec, V_BCS << rho_rad, treat H
   as externally prescribed (radiation-dominated).

3. **tau_GL:** The TDGL relaxation time. Estimated as 1/T_c from BCS theory. The
   exact prefactor depends on microscopic details not captured in the static BCS
   computation. Parameterize as tau_GL = C_GL / T_c with C_GL in [1, 10].

---

## 11. Summary: Integration Workflow

```
STEP 1: Load all .npz files
STEP 2: Build interpolants (V_spec, lambda_min, mu_c, F_cond, Delta_eq)
STEP 3: Define ODE RHS function

    def rhs(t, y):
        tau, pi_tau, mu = y[0], y[1], y[2]

        # Hubble (radiation era, prescribed)
        H = H_0 * (t_0 / t)

        # Effective potential gradient
        dV_spec = V_spec_spline(tau, 1)  # first derivative

        r = mu / lambda_min_spline(tau)
        F, dF_dtau = evaluate_F_cond(tau, r)  # from parametric model
        dV_BCS = dF_dtau  # total dV_BCS/dtau including chain rule

        dV_eff = dV_spec + dV_BCS

        # Equations of motion
        dtau_dt = pi_tau
        dpi_dt = -(1.0/5.0) * dV_eff - 3.0 * H * pi_tau
        dmu_dt = -H * mu

        return [dtau_dt, dpi_dt, dmu_dt]

STEP 4: Define events (window entry, window exit = CLOSED)
STEP 5: Integrate with solve_ivp (Radau method)
STEP 6: Post-process: extract m_saxion, Q_tau, P_LZ
STEP 7: Scan over initial conditions
```

---

## 12. Expected Outcomes and Closure Logic

### 12.1 Optimistic Scenario (Lock)

If V_BCS creates a local minimum in V_eff(tau) within the condensation window,
AND the modulus reaches this minimum before mu exits the window, THEN:

- tau_lock is the minimum location
- m_saxion > 0 (real mass)
- Q_tau > 1 (measurable trap)
- The condensate evaporates at t_exit but tau remains locked if m_saxion > H

This requires |dV_BCS/dtau| > |dV_spec/dtau| at some tau, which from Section 7.2
appears marginal.

### 12.2 Pessimistic Scenario (Closure)

If V_BCS only partially reduces the V_spec slope without creating a minimum,
the modulus continues rolling uphill (V_spec is monotone increasing), and the
transient condensate merely slows the roll. After evaporation, V_spec resumes
its monotone push and no lock occurs.

**This is the EXPECTED outcome** given:
- V_spec gradient ~ 3.4 (at tau=0.15, rho=0.01)
- V_BCS gradient ~ 1.4-3.0 (from F_cond tau-dependence)
- The competition is close but V_spec likely wins globally

### 12.3 Closure Verdict Format

```
P2-LOCK:  PASS   if tau_lock exists with m_saxion > H and Q_tau > 1
P2-LOCK: CLOSED   if no tau_lock or m_saxion < H or Q_tau < 1
P2-LOCK:  MARGINAL  if lock exists but is fragile (m_saxion ~ H)
```

---

## 13. Potential Subtleties

### 13.1 Lambda_min(tau) Feedback

As tau evolves, lambda_min changes. This shifts the condensation window in absolute
mu units. If tau increases, lambda_min increases, and the window mu_c * lambda_min
moves to higher mu. This means the condensate could persist LONGER than expected
if tau moves in the direction of increasing lambda_min, because the window "chases"
the dropping mu.

Quantitatively: d(lambda_min)/dtau > 0 (lambda_min increases with tau). If tau
is pushed to larger values (which V_spec does), the window boundary mu_c * lambda_min
increases. The race is between mu dropping (as a^{-1}) and the window boundary
rising (as lambda_min(tau) increases).

### 13.2 Temperature Effects

The BCS gap closes at T > T_c. In the radiation era, T ~ mu (for the relevant
species). So:

    T / lambda_min ~ mu / lambda_min

When mu/lambda_min ~ 1 (condensation window), T ~ lambda_min. But T_c ~ 0.03 * lambda_min.
Therefore T >> T_c inside the condensation window, and the BCS condensate is
thermally destroyed.

**THIS IS A POTENTIAL SHOW-STOPPER.** If the ambient temperature exceeds T_c,
no condensation occurs regardless of mu. The T=0 gap equation used in P1 is only
valid if T << T_c.

**Resolution options:**
1. The "temperature" of the substrate modes may differ from the radiation temperature.
   If the D_K modes are decoupled from the radiation bath (plausible: they are
   internal-space degrees of freedom), their effective temperature could be much
   lower.
2. Scan over T/T_c as a free parameter in the ODE integration.
3. Include finite-T BCS in the gap equation (P1 already computed M_max_vs_T).

### 13.3 Backreaction Consistency

If V_BCS ~ 0.3 in Planck units while rho_rad ~ M_Pl^4, the backreaction on H
is O(V_BCS/M_Pl^4) ~ negligible. The test-field approximation is self-consistent.

### 13.4 Multi-Mode vs Single-Mode Gap

The P1 computation uses all 16 modes in the (0,0) singlet. The self-consistent
Delta has structure across modes (different components for different eigenvalue
levels). The scalar |Delta| used in the ODE is the norm of this vector. This
is accurate if the gap-vector direction does not change significantly as tau
and mu evolve along the trajectory. From the P1 data, the direction is dominated
by the gap-edge modes (indices 8-15, the positive-eigenvalue modes closest to mu),
so this approximation is reasonable.

---

## 14. Code Structure for Implementation

```
s26_p2_cooling_trajectory.py

Functions:
    build_interpolants(npz_paths) -> dict of splines/interpolants
    V_eff_and_gradient(tau, mu, interpolants) -> (V, dV_dtau)
    Delta_equilibrium(tau, mu, interpolants) -> Delta_eq
    ode_rhs(t, y, params, interpolants) -> dy_dt
    kill_event(t, y, params, interpolants) -> mu - mu_c(tau)
    integrate_trajectory(tau_i, pi_i, mu_i, H_0, params, interpolants) -> solution
    extract_diagnostics(solution, interpolants) -> (m_saxion, Q_tau, P_LZ)
    scan_initial_conditions(param_ranges, interpolants) -> results_table

Main execution:
    1. Load data, build interpolants
    2. Single diagnostic run at fiducial parameters
    3. 1D scan over mu_0
    4. 2D scan over (tau_i, pi_tau_i)
    5. Output: s26_p2_cooling_trajectory.npz + s26_p2_cooling_trajectory.png
```

---

## 15. Estimated Runtime

- ODE integration per trajectory: ~0.01-0.1s (simple 3-variable system)
- Interpolant construction: ~0.1s
- 1D scan (20 points): ~2s
- 2D scan (20x20 points): ~40s
- Total including diagnostics: < 2 minutes

GPU not needed — this is a low-dimensional ODE problem. CPU is sufficient.
