# On the Vibrations of the Electronic Plasma

**Author:** Lev Davidovich Landau
**Year:** 1946
**Journal:** J. Phys. USSR, 10, 25-34 (also Zh. Eksp. Teor. Fiz., 16, 574)

---

## 1. Historical Context

### 1.1 The Plasma Oscillation Problem

In the 1930s-40s, plasma physics faced a fundamental puzzle. Tonks and Langmuir
(1929) had established that plasmas support collective oscillations at the
plasma frequency:

    omega_p = sqrt(4 * pi * n_e * e^2 / m_e)

where n_e is the electron density, e the electron charge, and m_e the electron
mass. The Vlasov equation (1938) described these oscillations in a collisionless
plasma via a self-consistent field approach:

    df/dt + v . grad_x(f) + (e/m_e) * E . grad_v(f) = 0

coupled with Poisson's equation:

    div(E) = 4 * pi * e * (n_i - integral f d^3v)

### 1.2 The Paradox

The Vlasov equation, being time-reversible, seemingly could not produce
damping. Yet physical intuition suggested that oscillations in a warm plasma
should decay even without collisions. The resolution required Landau's insight
into the proper mathematical treatment of the initial value problem.

---

## 2. Landau's Analysis

### 2.1 Linearization

Consider small perturbations about a uniform equilibrium:

    f(x, v, t) = f_0(v) + f_1(x, v, t)
    E(x, t) = E_1(x, t)

where f_0(v) is the equilibrium velocity distribution (e.g., Maxwellian). The
linearized Vlasov equation for a single Fourier mode with wavevector k is:

    df_1/dt + i*k*v*f_1 + (e/m_e) * E_1 * df_0/dv = 0

with E_1 determined self-consistently from:

    i * k * E_1 = -4 * pi * e * integral f_1 dv

### 2.2 The Initial Value Approach

Previous workers (Vlasov himself) had sought normal modes -- solutions
proportional to exp(-i*omega*t) -- and found only real frequencies (no damping).
Landau recognized that the correct approach is the **initial value problem**:
given f_1(x, v, t=0), solve for f_1(x, v, t) at later times.

Using Laplace transforms in time (not Fourier transforms, which presuppose
oscillatory behavior):

    f_1(k, v, s) = integral_0^{infinity} f_1(k, v, t) * exp(-s*t) dt

where s is complex with Re(s) > 0 for convergence, the transformed Vlasov
equation gives:

    f_1(k, v, s) = [f_1(k, v, 0) - (e/(m_e)) * E_1(k, s) * (df_0/dv)] / (s + i*k*v)

### 2.3 The Dielectric Function

Substituting into Poisson's equation yields:

    E_1(k, s) = (4*pi*e / (i*k)) * [integral f_1(k,v,0)/(s + i*k*v) dv] / epsilon(k, s)

where the dielectric function is:

    epsilon(k, s) = 1 + (omega_p^2 / (k^2)) * integral [(df_0/dv) / (v - i*s/k)] dv

The zeros of epsilon(k, s) determine the time-asymptotic behavior of E_1(t).

### 2.4 The Landau Contour

Here is Landau's crucial mathematical insight. The integral:

    I(z) = integral_{-infinity}^{+infinity} g(v) / (v - z) dv

where z = i*s/k, is well-defined for Im(z) > 0 (corresponding to Re(s) > 0).
To find the long-time behavior, we need to analytically continue epsilon(k, s)
to Re(s) < 0 (damped modes).

As z crosses the real axis from above, the pole at v = z encounters the
integration contour. Landau showed that the correct analytic continuation
requires deforming the contour to pass **below** the pole:

    I(z) = P integral g(v)/(v-z) dv + i*pi*g(z)    (for Im(z) = 0)

where P denotes the Cauchy principal value. This is the **Landau prescription**
for the contour.

The resulting dielectric function for real omega = -i*s is:

    epsilon(k, omega) = 1 - (omega_p^2/k^2) * [P integral (df_0/dv)/(v - omega/k) dv + i*pi*(df_0/dv)|_{v=omega/k}]

---

## 3. Landau Damping

### 3.1 The Damping Rate

For a Maxwellian equilibrium:

    f_0(v) = n_e / (sqrt(2*pi) * v_th) * exp(-v^2 / (2 * v_th^2))

where v_th = sqrt(k_B * T / m_e), the dispersion relation omega(k) = omega_r + i*gamma
has:

    omega_r^2 = omega_p^2 * (1 + 3*k^2*lambda_D^2 + ...)    (Bohm-Gross)

    gamma = -sqrt(pi/8) * (omega_p / (k * lambda_D)^3) * exp(-1/(2*k^2*lambda_D^2) - 3/2)

where lambda_D = v_th / omega_p is the Debye length.

Key features:
- gamma < 0 always (damping, not growth) for monotonically decreasing f_0
- gamma is exponentially small for k*lambda_D << 1 (long wavelengths)
- gamma becomes comparable to omega_r for k*lambda_D ~ 1
- For k*lambda_D >> 1, the collective mode is overdamped (no propagation)

### 3.2 The Physical Mechanism

The damping arises from resonant energy exchange between the wave and particles
whose velocity v matches the phase velocity omega/k of the wave:

- Particles slightly slower than omega/k are accelerated by the wave electric
  field (they "surf" the wave, gaining energy)
- Particles slightly faster than omega/k are decelerated (they give energy to
  the wave)
- For a Maxwellian distribution, df_0/dv < 0 at v = omega/k > 0, meaning there
  are more slow particles gaining energy than fast particles losing energy
- Net result: energy flows from wave to particles -- the wave damps

This is purely kinetic -- no collisions are involved. The damping rate depends
on the slope of the distribution function at the resonant velocity.

### 3.3 Landau Growth (Inverse Damping)

If the distribution function has a positive slope at v = omega/k (i.e.,
df_0/dv > 0, a "bump on tail"), then gamma > 0 and the wave grows
exponentially. This is the basis of:
- Beam-plasma instabilities
- Two-stream instability
- Laser-plasma interactions
- Particle accelerator collective effects

---

## 4. Phase Mixing and Reversibility

### 4.1 Not True Dissipation

A profound subtlety: Landau damping is NOT irreversible dissipation. The
Vlasov equation is time-reversible and preserves all Casimir invariants
(integral C(f) d^3x d^3v for any function C). The entropy:

    S = -integral f * ln(f) d^3x d^3v

is exactly conserved. No entropy is produced.

What happens is **phase mixing**: the perturbation f_1(v, t) develops
increasingly fine structure in velocity space. The electric field E_1 (which
depends on the velocity integral of f_1) decays because the oscillations in
v-space average to zero -- but the information is still present in f_1.

### 4.2 Plasma Echo

The reversibility of Landau damping was dramatically confirmed by the **plasma
echo** phenomenon (Malmberg, Wharton, Gould, O'Neil, 1968):

1. Launch wave 1 with wavevector k_1 at t = 0. It Landau damps.
2. Launch wave 2 with wavevector k_2 at t = tau. It also Landau damps.
3. At t = tau * k_2 / (k_2 - k_1), a third wave spontaneously appears with
   wavevector k_2 - k_1.

This echo proves that the phase information from wave 1 persists in the velocity
distribution long after the electric field has decayed.

### 4.3 Mathematical Structure

The field energy decays as:

    |E_1(t)|^2 ~ exp(2 * gamma * t)

But the total energy (field + kinetic) is conserved:

    d/dt [|E_1|^2 / (8*pi) + (m_e/2) * integral v^2 * f_1 dv] = 0

The field energy is transferred to coherent phase-space structures in f_1(v),
not to thermal energy. This is energy transfer without entropy production.

---

## 5. Mathematical Rigor

### 5.1 The Controversy

Landau's original derivation was questioned for decades. Van Kampen (1955)
showed that the Vlasov equation has a continuous spectrum of undamped normal
modes (the "Case-Van Kampen modes"), each localized at a single velocity.
These are not square-integrable and form a complete set only in a distributional
sense.

The resolution (Case 1959, Lenard 1961): Landau damping of the electric field
is correct as an initial value problem. The normal mode expansion converges to
the same result -- the E-field decays because the Van Kampen modes dephase.
Both pictures are mathematically equivalent.

### 5.2 Nonlinear Landau Damping

The nonlinear theory is dramatically more subtle:

- O'Neil (1965): particles trapped in the wave potential bounce back and forth,
  leading to saturation of damping and nonlinear oscillations
- For large amplitude waves, the damping rate decreases as the trapped particle
  fraction grows
- The trapping time tau_B = 1 / sqrt(e*k*E_0/m_e) sets the boundary between
  linear (t << tau_B) and nonlinear (t >> tau_B) regimes

### 5.3 Mouhot-Villani Theorem (2011)

Cedric Villani (Fields Medal 2010, partly for this work) and Clement Mouhot
proved that nonlinear Landau damping occurs for the full Vlasov-Poisson system
near stable equilibria, provided the initial perturbation is sufficiently
small and analytic. This was one of the landmark results in mathematical
physics of the 21st century, placing Landau's 1946 intuition on rigorous
footing after 65 years.

---

## 6. Experimental Verification

### 6.1 Laboratory Plasmas

Landau damping was first observed experimentally by Malmberg and Wharton (1964)
in a magnetized plasma column. They measured:
- The dispersion relation omega(k) -- agreeing with Bohm-Gross
- The damping rate gamma(k) -- agreeing quantitatively with Landau's formula
  over two decades of variation

### 6.2 Space Plasmas

In space, Landau damping is ubiquitous:
- Solar wind: ion-acoustic wave damping regulates the electron-ion temperature
  ratio
- Earth's magnetosphere: Landau damping of whistler waves controls electron
  precipitation
- Astrophysical shocks: collisionless shock structure involves Landau damping
  at the kinetic scale

### 6.3 Beyond Classical Plasmas

The Landau damping mechanism appears in:
- Gravitational systems (Lynden-Bell 1962): "violent relaxation" of stellar
  systems is the gravitational analog
- Quark-gluon plasma: color Landau damping of gluon fields
- Neutrino transport: collisionless damping in the early universe
- Ultracold atomic gases: quantum Landau damping of collective modes in BEC

---

## 7. Connection to Phonon-Exflation Cosmology

### 7.1 Collisionless Energy Transfer

Landau damping demonstrates that energy can be transferred between collective
wave modes and individual particles without any collision or scattering event.
The mechanism is purely kinematic -- resonant phase-velocity matching.

In the phonon-exflation picture, particle creation from the vacuum condensate
involves a closely analogous process:
- The condensate (ground state) carries collective modes (phonons/rotons)
- Particles (massive excitations) can be created when the "flow" of the
  expanding condensate provides sufficient energy
- The resonance condition v = omega/k maps to the condition that the expansion
  rate matches the excitation gap: H ~ m*c^2/hbar

### 7.2 Phase Mixing and Decoherence

The phase mixing that produces Landau damping has a direct analog in the
quantum-to-classical transition during cosmological evolution:
- Fine-grained phase space information is preserved (unitarity)
- Coarse-grained observables show apparent dissipation (decoherence)
- The "plasma echo" analog would be recoherence -- potentially observable
  in carefully prepared condensate experiments

### 7.3 Distribution Function and the Vacuum

The Vlasov distribution f(x, v, t) in Landau's treatment plays the role of
the Wigner function of the quantum field in the phonon-exflation context.
The slope df_0/dv at the resonance determines whether modes grow or decay --
analogous to the occupation number determining stimulated emission vs
absorption in the quantum field theory.

### 7.4 Stability of the Condensate

Landau damping of collective modes in a BEC (quantum Landau damping) determines
the lifetime of phonon excitations in the condensate. In the GPE simulation:
- Long-wavelength phonons are Landau-stable (c*k > 0 means no resonance with
  thermal particles at T = 0)
- The damping rate of excitations near the roton minimum determines the
  effective "particle lifetime"
- Non-equilibrium evolution during simulated expansion creates transient
  populations subject to Landau-type damping and growth

### 7.5 The Bump-on-Tail Instability

The inverse Landau damping (beam instability) has a cosmological analog: if the
excitation spectrum develops a population inversion (more particles at high
energy than expected from thermal equilibrium), collective modes can grow
spontaneously. This maps to:
- Parametric resonance during preheating (in standard cosmology)
- Phonon amplification during the exflation phase transition
- The mechanism by which the condensate converts coherent energy into particle
  excitations

---

## 8. Legacy

### 8.1 Conceptual Impact

Landau damping changed how physicists think about collective phenomena:
1. Energy transfer does not require collisions
2. Time-reversible equations can produce apparently irreversible behavior
3. The initial value problem and the normal mode problem are distinct
4. Phase space structure below the coarse-graining scale stores information

### 8.2 Mathematical Impact

The Landau contour prescription became a standard technique in:
- Kinetic theory (BGK, Balescu-Lenard equations)
- Quantum field theory (retarded/advanced propagators, i*epsilon prescription)
- Dispersive wave theory (causality and analytic continuation)
- Financial mathematics (pricing under incomplete information)

The connection to QFT is particularly noteworthy: Landau's i*epsilon
prescription for going around the pole is identical in mathematical structure
to the Feynman propagator's i*epsilon. Both enforce causality through the same
analytic continuation.

---

## 9. Summary

Landau's 1946 paper established:

1. The initial value approach to plasma oscillations (not normal mode analysis)
2. The Landau contour for analytic continuation of the dielectric function
3. Collisionless (Landau) damping at the rate set by df_0/dv at the resonance
4. The physical mechanism: resonant wave-particle energy exchange
5. The distinction between phase mixing and true dissipation

The paper is arguably the founding work of modern plasma kinetic theory. Its
influence extends far beyond plasma physics to any system where collective
modes interact resonantly with a continuum of individual degrees of freedom --
which is precisely the situation in phonon-exflation cosmology.

---

## References

- L.D. Landau, "On the Vibrations of the Electronic Plasma," J. Phys. USSR 10, 25 (1946)
- A.A. Vlasov, "On Vibration Properties of an Electron Gas," Zh. Eksp. Teor. Fiz. 8, 291 (1938)
- N.G. Van Kampen, "On the Theory of Stationary Waves in Plasmas," Physica 21, 949 (1955)
- K.M. Case, "Plasma Oscillations," Ann. Phys. 7, 349 (1959)
- J.H. Malmberg, C.B. Wharton, "Collisionless Damping of Electrostatic Plasma Waves," Phys. Rev. Lett. 13, 184 (1964)
- T.M. O'Neil, "Collisionless Damping of Nonlinear Plasma Oscillations," Phys. Fluids 8, 2255 (1965)
- J.H. Malmberg et al., "Plasma Wave Echo Experiment," Phys. Rev. Lett. 20, 95 (1968)
- C. Mouhot, C. Villani, "On Landau Damping," Acta Math. 207, 29 (2011)
