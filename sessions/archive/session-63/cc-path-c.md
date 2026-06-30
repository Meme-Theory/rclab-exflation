# CC Path C: Transit-as-Relaxation

**Author**: Landau (Condensed Matter Theorist)
**Date**: 2026-04-01
**Status**: Investigation document -- detailed derivation and assessment

---

## 0. Executive Summary

Path C proposes that the Jensen transit through the fold IS Volovik's cosmological relaxation rho_vac(t) ~ omega^2/t^2, realized through the tau-dependence of the spectral action. The estimate Lambda_obs ~ S_fold * (t_fold/t_0)^{-2} ~ 2.5 x 10^{-116} M_KK lands within 2 OOM of observation with zero free parameters. However, Theorem T14 (a_0 = const under volume-preserving Jensen) creates a tau-independent floor that blocks FULL relaxation. The investigation below derives the relaxation mechanism from first principles, classifies the a_0 obstruction, maps the transit to Kibble-Zurek quench dynamics, designs the decisive computation S-ASYMPTOTIC-64, and assesses the path's viability.

The central finding: Path C decomposes into two structurally independent problems. The curvature-dependent part rho_curv(tau) = f_2 Lambda^2 a_2(tau) + f_4 a_4(tau) + ... is accessible to transit relaxation, and the Kibble-Zurek universality class fixes the relaxation exponent. The curvature-independent floor rho_0 = f_0 Lambda^4 a_0 is NOT accessible to the transit and requires a separate mechanism (Volovik equilibrium theorem or K-class transition). The two-component CC decomposition (CC-17 from the OOM document) is structurally forced.

---

## 1. The Relaxation Mechanism: Derivation from Volovik's q-Theory

### 1.1. Volovik's Relaxation in the q-Theory Framework

The starting point is Volovik's Paper 04 (2005) and Paper 25 (2013). The quantum vacuum is treated as a self-sustained medium characterized by a conserved vacuum variable q. The vacuum energy in the Gibbs-Duhem formulation is:

    rho_vac = epsilon(q) - q * d(epsilon)/dq                                (C-1)

where epsilon(q) is the total energy density as a function of q (Volovik Paper 04, Section III). In equilibrium, the condition d(epsilon)/dq = mu (chemical potential, an integration constant) gives rho_vac = epsilon(q_0) - mu * q_0 = 0 at T = 0 for an isolated self-sustained system (Volovik's equilibrium theorem).

Out of equilibrium, the vacuum variable q is displaced from q_0, and the system relaxes. Paper 25, Section V, gives the late-time dynamics after an impulsive perturbation (a "kick" displacing q from equilibrium):

    q(t) - q_0 ~ q_0 * sin(omega * t) / (omega * t)                        (C-2)

where omega ~ E_Planck is the microscopic oscillation frequency. The vacuum energy density then relaxes as:

    rho_vac(t) ~ omega^2 / t^2 * sin^2(omega * t)                          (C-3)

At the present cosmic epoch (t ~ t_0 ~ 10^{17} s ~ 10^{60} t_Planck), the time-averaged vacuum energy is:

    <rho_vac>(t_0) ~ omega^2 / t_0^2 ~ E_Planck^2 * H_0^2                  (C-4)

This is the Volovik result: the vacuum energy density at late times is naturally of order E_Planck^2 * H_0^2, which matches the observed CC to within an order-of-magnitude. The CC is small because the universe is OLD -- the vacuum has had time to relax.

### 1.2. Mapping to Spectral Action Dynamics

In the phonon-exflation framework, the vacuum variable q is not an abstract thermodynamic quantity but has a concrete spectral realization. The spectral action on the Jensen-deformed SU(3) fiber is:

    S(tau) = Tr f(D_K(tau)^2 / Lambda^2) = sum_n d_n f(lambda_n(tau)^2 / Lambda^2)    (C-5)

where {lambda_n(tau)} are the D_K eigenvalues with multiplicities {d_n}, and f is the cutoff function (framework-cc-oom.md, Eq. CC-1). The Jensen deformation parameter tau is the substrate's internal degree of freedom that evolves during the transit.

The mapping between Volovik's q-theory and the spectral action is:

| Volovik q-theory | Spectral action framework |
|:-----------------|:--------------------------|
| Vacuum variable q | Jensen parameter tau |
| Energy epsilon(q) | Spectral action S(tau) |
| Equilibrium q_0 | Asymptotic tau -> infinity (if S -> 0) |
| Oscillation frequency omega | Transit frequency omega_tau = 8.27 M_KK (S38) |
| Kick at t = 0 | First-order transit through the fold at tau = 0.190 |
| Relaxation rho ~ 1/t^2 | S(tau(t)) decreasing as tau increases beyond fold |

The critical identification: the Jensen parameter tau(t) increases monotonically during and after the transit. The spectral action gradient dS/dtau = +58,673 at the fold (S42) DRIVES this increase. The spectral action S(tau) evaluated along the transit trajectory gives the vacuum energy as a function of cosmic time.

### 1.3. The Relaxation Estimate

If S(tau) ~ tau^{-alpha} for large tau (with alpha > 0), and if tau(t) ~ t^{beta} (power-law relation between Jensen parameter and cosmic time), then:

    rho_vac(t) = S(tau(t)) ~ t^{-alpha * beta}                              (C-6)

For the Volovik relaxation rate alpha * beta = 2, we need the product of the spectral action decay exponent and the tau-time scaling exponent to equal 2.

The numerical estimate proceeds as follows. At the fold:

    S_fold = 250,360.68 M_KK     (S42, canonical_constants.py)              (C-7)

The fold occurs at cosmic time t_fold. From the transit dynamics (S38):

    t_fold ~ 1/H_fold ~ 1/(586.5 M_KK) ~ 1.7 x 10^{-3} M_KK^{-1}         (C-8)

Converting to seconds with M_KK = 7.429 x 10^{16} GeV:

    t_fold ~ 1/(586.5 * 7.429e16 * 1.52e24 s^{-1}) ~ 1.5 x 10^{-44} s     (C-9)

where 1 GeV = 1.52 x 10^{24} s^{-1} in natural units. The present age:

    t_0 = 1/H_0 ~ 4.4 x 10^{17} s                                          (C-10)

Therefore:

    t_fold / t_0 ~ 3.4 x 10^{-62}                                          (C-11)

For alpha * beta = 2:

    Lambda_obs ~ S_fold * (t_fold/t_0)^2 ~ 250,361 * (3.4e-62)^2           (C-12)
              ~ 250,361 * 1.16e-123 ~ 2.9 x 10^{-118} M_KK                 (C-13)

The observed CC in M_KK units:

    rho_obs / M_KK^4 = 2.7e-47 / (7.429e16)^4 = 2.7e-47 / 3.05e67 = 8.9 x 10^{-115}    (C-14)

Comparison:

    Lambda_predicted / Lambda_obs ~ 2.9e-118 / 8.9e-115 ~ 3.3 x 10^{-4}    (C-15)

This is a factor of ~3000 too SMALL -- or equivalently, 3.5 OOM below observed. The estimate in the Volovik-VdD workshop (E2) quoted 2 OOM agreement; the more careful calculation here gives 3.5 OOM, but this is sensitive to the precise value of t_fold and the meaning of S_fold (whether it enters as a density or as a dimensionless ratio).

The sign of the discrepancy matters: the predicted CC is TOO SMALL, not too large. In the standard CC problem, the prediction is 114 OOM too large. Path C, if it works, OVERSHOOTS the relaxation by ~3.5 OOM. This is a qualitatively different situation from the standard CC problem -- an overshoot of the relaxation can potentially be corrected by the a_0 floor (which adds back a positive constant).

### 1.4. What Sets the Relaxation Exponent?

The product alpha * beta = 2 in Volovik's treatment arises from a specific dynamical assumption: the vacuum variable q oscillates with frequency omega (set by microscopic physics) and decays through radiative damping into gravity waves or quasiparticle creation, giving an envelope ~ 1/t. Since rho_vac ~ (q - q_0)^2 (to leading order in the Landau expansion about equilibrium), the energy decays as 1/t^2.

In the spectral action framework, the two exponents have independent origins:

**The spectral exponent alpha.** This is the rate at which a_2(tau) and a_4(tau) approach zero (or their asymptotic values) as tau -> infinity. From the Seeley-DeWitt structure:

    a_2(tau) = (4pi)^{-4} integral_SU(3) [R(tau)/6 - E(tau)] dvol           (C-16)

where R(tau) is the scalar curvature of the Jensen metric on SU(3) and E(tau) is the Lichnerowicz endomorphism (VdD workshop E2). The Jensen deformation at large tau stretches some metric components and compresses others (subject to det g = const from volume preservation). The curvature has contributions from BOTH stretched and compressed directions.

For a left-invariant metric on a compact Lie group with structure constants f^c_{ab}, the scalar curvature is (see, e.g., Milnor 1976):

    R = -(1/2) sum_{a,b,c} f^c_{ab} f^{ab}_c * g_{cc}                      (C-17)
        + (1/4) sum_{a,b,c} f^{ab}_c g^{cc} g_{aa} g_{bb}

(schematic -- the full expression involves contractions with the inverse metric). For the Jensen metric with anisotropy parameter tau, the metric on SU(3) has eigenvalues that scale differently in the Cartan and root directions. At large tau, some directions scale as tau and others as 1/tau (volume preservation). The curvature contributions from the compressed directions diverge as tau^2, while those from the stretched directions vanish as 1/tau^2.

The key structural question: does the INTEGRAL of R over SU(3) diverge, vanish, or remain finite as tau -> infinity?

For a volume-preserving anisotropic deformation of a compact group:

- If R ~ tau^2 locally in compressed directions, but the volume element in those directions scales as 1/tau (from the metric determinant being fixed), then integral R dvol ~ tau^2 * (1/tau) = tau. This would give a_2(tau) ~ tau for large tau -- INCREASING, not decreasing.

- If the compressed and stretched contributions cancel in the integral (by group symmetry), the integral could decrease. For SU(3) with the specific Jensen deformation (which preserves the left-invariant structure), the Cartan-Killing metric has 8 directions. The Jensen deformation selects a Cartan direction (the 7th generator, corresponding to the Jensen parameter) and scales it differently from the remaining 7 directions. The group symmetry constrains the curvature integral, but it does NOT force cancellation.

VdD's structural bound (workshop E2) states a_2(tau) cannot approach zero FASTER than 1/tau, because the curvature is bounded below by the inverse of the largest metric coefficient. This gives:

    alpha <= 1     (structural upper bound on spectral decay exponent)        (C-18)

**The time-scaling exponent beta.** This is the relationship between the Jensen parameter tau and cosmic time t. From the transit dynamics (S38), the spectral action gradient drives tau(t):

    d(tau)/dt = (2/3) * S'(tau) / S(tau) * tau                              (C-19)

(Friedmann-moduli coupling, schematic). During the transit, tau increases rapidly (Mach 13.75 at the fold). After the transit, in the deceleration phase, the spectral action gradient decreases and tau(t) approaches power-law growth. In a radiation-dominated universe:

    a(t) ~ t^{1/2},     H(t) = 1/(2t)                                      (C-20)

If the modulus tau is overdamped by Hubble friction (as expected for a massive modulus with m_tau = 2.062 M_KK >> H at all post-transit times), then tau freezes at its transit value. This gives beta = 0 -- NO relaxation.

This is the critical dynamical issue. The Volovik relaxation requires the vacuum variable to continue evolving at late times. If tau freezes after the transit (as Hubble friction demands for a massive modulus), the spectral action evaluates at the frozen tau value and the CC is simply S(tau_frozen), with no further relaxation.

The escape from frozen modulus: if the spectral action gradient dS/dtau provides a force that exceeds Hubble friction at all times, tau continues to evolve. The condition is:

    |dS/dtau| > 3H(t) * m_tau^2 * (tau - tau_0)                            (C-21)

At the fold, dS/dtau = 58,673 M_KK and H_fold = 586.5 M_KK. The ratio dS/dtau / (H * m_tau^2) = 58,673 / (586.5 * 4.25) ~ 23.5. The spectral action gradient overwhelms Hubble friction by a factor of ~24 at the fold. This is the Mach 13.75 transit: the driving force is enormous.

After the transit, S(tau) and dS/dtau both decrease (for monotonically increasing S, the gradient decreases as tau increases beyond the inflection point). Whether the gradient remains large enough to overcome Hubble friction at late times is precisely what S-ASYMPTOTIC-64 must determine. If dS/dtau ~ tau^{-(1+alpha)} while H ~ 1/t ~ 1/tau^{1/beta}, the condition for continued evolution is:

    alpha + 1 < 1/beta     =>     beta < 1/(alpha + 1)                      (C-22)

For alpha = 1 (the VdD structural bound), this requires beta < 1/2. In a radiation-dominated universe with tau ~ t^{beta}, this corresponds to tau growing SLOWER than t^{1/2}. This is self-consistent: a decelerating modulus with power-law growth beta < 1/2 is physically reasonable.

The product alpha * beta = 1 * (1/2) = 1/2 would give rho_vac ~ t^{-1/2}, far too slow (the CC at the present epoch would still be enormous). To get alpha * beta = 2, we need alpha * beta = 2, which requires alpha > 2 if beta < 1 -- violating the structural bound alpha <= 1.

**This is a tension.** The Volovik relaxation rate alpha * beta = 2 appears inconsistent with the structural bound alpha <= 1 from the Jensen metric curvature scaling, unless beta > 2 (tau growing faster than t^2, which is not physical for a decelerating modulus).

Resolution candidates:

(a) The structural bound alpha <= 1 applies to a_2(tau) individually, but the FULL spectral action S(tau) = sum_n d_n f(lambda_n^2/Lambda^2) may decrease faster than any individual a_n because the cutoff function f suppresses the contribution of eigenvalues that grow with tau. If eigenvalues spread as |lambda_n| ~ tau^{gamma_n} with different gamma_n for different modes, and f is Gaussian (f(x) = exp(-x)), then f(lambda_n^2/Lambda^2) ~ exp(-tau^{2*gamma_n}/Lambda^2). The modes with the fastest-growing eigenvalues are exponentially suppressed, and the sum could decrease much faster than 1/tau.

(b) The relationship tau(t) may not be a simple power law. If the modulus dynamics produce logarithmic growth (tau ~ ln(t)), then beta = 0 in the power-law sense but the spectral action decreases as S ~ exp(-alpha * ln(t)) = t^{-alpha} for exponential S(tau) dependence. This would give rho_vac ~ t^{-alpha}, and alpha = 2 directly from the spectral action profile. The logarithmic tau-time mapping arises naturally if the driving force dS/dtau decreases exponentially with tau.

(c) The Volovik alpha * beta = 2 is NOT the correct exponent for the spectral action framework. The actual relaxation rate is determined by the specific eigenvalue dynamics of D_K under Jensen deformation, which may give a different exponent. The 2 OOM estimate was an ORDER-OF-MAGNITUDE comparison that happened to work; the actual exponent may differ and the agreement may be coincidental.

---

## 2. The a_0 Floor Obstruction

### 2.1. Theorem T14: Volume-Preserving Jensen Implies a_0 = const

The zeroth Seeley-DeWitt coefficient for the Dirac operator on a compact Riemannian manifold (M, g) without boundary is:

    a_0(D^2) = (4pi)^{-d/2} * rank(S) * Vol(M, g)                          (C-23)

where d = dim(M), rank(S) is the rank of the spinor bundle (= 2^{[d/2]} for a spin manifold), and Vol(M, g) = integral_M dvol_g is the Riemannian volume.

For the Jensen deformation of SU(3) (dim = 8), the volume-preservation condition is:

    Vol(SU(3), g_Jensen(tau)) = Vol(SU(3), g_biinvariant) = const            (C-24)

for all tau. This is Theorem T14 (proven S42, verified multiple sessions). The Jensen metric is defined as a left-invariant metric that preserves the total volume of SU(3) while introducing anisotropy.

Therefore:

    a_0(tau) = (4pi)^{-4} * rank(S_8) * Vol(SU(3)) = const                 (C-25)

independent of tau. At the fold: a_0 = 6440.0 (canonical_constants.py). This is EXACT and PERMANENT.

### 2.2. Consequences for the Spectral Action

The Seeley-DeWitt expansion (CC-3 from framework-cc-oom.md):

    S(tau) = f_0 Lambda^4 a_0 + f_2 Lambda^2 a_2(tau) + f_4 a_4(tau) + O(Lambda^{-2})    (C-26)

The f_0 Lambda^4 a_0 term is tau-INDEPENDENT. For any finite Lambda, this term provides a floor below which S(tau) cannot descend. Specifically:

    S(tau) >= f_0 Lambda^4 a_0     for all tau                              (C-27)

since the higher-order terms (f_2 Lambda^2 a_2 + f_4 a_4 + ...) can at most approach zero but not become arbitrarily negative (assuming f_k >= 0 for the Gaussian cutoff, and a_k bounded below, which follows from compactness).

The magnitude of the floor. With f_0 = 9.817 (S62, Gaussian cutoff for alpha_GUT = 1/25), Lambda = M_KK, and a_0 = 6440:

    S_floor = f_0 * M_KK^4 * a_0 = 9.817 * 6440 * M_KK^4 = 63,221 M_KK^4  (C-28)

As a fraction of S_fold:

    S_floor / S_fold ~ 63,221 / 250,361 ~ 0.253                            (C-29)

The floor is ~25% of the total spectral action at the fold. The transit can at most relax the remaining ~75% (the curvature-dependent part). This is NOT a small correction.

### 2.3. The Unexpanded Spectral Action

The Seeley-DeWitt expansion is an ASYMPTOTIC expansion in powers of 1/Lambda^2. For finite Lambda, the full (unexpanded) spectral action:

    S(tau) = sum_n d_n f(lambda_n(tau)^2 / Lambda^2)                        (C-30)

does not suffer from the same floor. Each term f(lambda_n^2/Lambda^2) depends on tau through lambda_n(tau). At large tau, eigenvalues spread: some grow (|lambda_n| ~ tau^{gamma_n}), and f suppresses those with lambda_n >> Lambda. Others may shrink toward zero, with f(0) = 1 for the Gaussian cutoff (f(x) = exp(-x), f(0) = 1).

The asymptotic behavior of S(tau) as tau -> infinity in the UNEXPANDED sum:

    S(tau -> inf) -> sum_{n: lambda_n -> 0} d_n * f(0) + sum_{n: lambda_n -> inf} d_n * f(lambda_n^2/Lambda^2)    (C-31)

The second sum is exponentially suppressed. The first sum counts the modes whose eigenvalues approach zero under extreme Jensen deformation. If k modes approach zero:

    S(tau -> inf) -> k * f(0) = k                                           (C-32)

(for f(0) = 1, Gaussian cutoff). The value k is the number of "zero modes" in the asymptotic Jensen metric.

For the bi-invariant metric on SU(3), the zero modes of D_K are those in the trivial (0,0) representation. Their count (with spinor degeneracy) is a topological invariant -- the index-related quantity. For the Jensen deformation, which is continuously connected to the bi-invariant metric, the number of modes approaching zero is BOUNDED BELOW by the modes that are already zero at tau = 0.

VdD's analysis (workshop E2) confirms: S(tau) -> a_0 * f(0) = a_0 from below at large tau. The eigenvalue density concentrates near zero (more modes have small eigenvalues), and the cutoff suppresses the rest. The asymptotic value is a_0, exactly the floor predicted by the SDW expansion.

**Structural conclusion**: Whether we use the SDW expansion or the full unexpanded sum, S(tau) approaches a NONZERO constant at large tau. The floor is a_0 (up to f(0) normalization). Full relaxation to S = 0 is BLOCKED.

### 2.4. Can the Floor Be Circumvented?

Three logical escapes from the a_0 floor:

**(A) Volume non-preservation.** If the Jensen deformation does NOT preserve volume, a_0(tau) itself depends on tau and could approach zero. However, the framework's Jensen metric is DEFINED to be volume-preserving (Theorem T14 is a definition, not a dynamic result). Abandoning volume preservation means changing the spectral geometry -- this would modify ALL predictions, not just the CC. The n_s prediction (which passes at 0.9561 vs Planck's 0.9649) depends on the spectral action profile, which depends on the volume normalization. Changing the volume normalization to fix the CC would likely break n_s. This is not viable unless a self-consistent modified Jensen metric can be found.

**(B) Cutoff function with f(0) = 0.** If the cutoff function vanishes at x = 0 (e.g., f(x) = x * exp(-x) instead of f(x) = exp(-x)), then the zero-mode contribution to S vanishes and the floor is zero. However, f(0) = 0 means the spectral action does not count modes with zero eigenvalue. This changes the physical content: the a_0 coefficient (which gives the CC) requires f(0) > 0. With f(0) = 0, the leading term in the SDW expansion is f_2 Lambda^2 a_2, and the CC is determined by a_2, not a_0. This shifts the problem from "why is a_0 * Lambda^4 large?" to "why is a_2 * Lambda^2 large?" -- a 2 OOM improvement (Lambda^2 vs Lambda^4), but not a resolution.

More fundamentally, the cutoff function f is a physical choice in the spectral action principle, and changing it to fix the CC is tantamount to fine-tuning. The framework should predict the CC for ANY reasonable cutoff, or at least for the Gaussian cutoff that reproduces the gauge couplings.

**(C) Two-component decomposition (the correct approach).** Accept the floor as real. The vacuum energy has two components:

    rho_vac(tau) = rho_0 + rho_curv(tau)                                    (C-33)

where rho_0 = f_0 Lambda^4 a_0 is the tau-independent floor (the "bare" CC from mode counting) and rho_curv(tau) = f_2 Lambda^2 a_2(tau) + f_4 a_4(tau) + ... is the curvature-dependent, tau-varying part.

The transit relaxes rho_curv toward zero. The Volovik equilibrium theorem (Paper 04) states that rho_0 = 0 in true equilibrium -- the trans-Planckian cancellation between UV and sub-Planckian modes. But the GGE relic is NOT in equilibrium, and the Gibbs-Duhem relation at N_pair = 1 gives rho_0 = E(0) (the zero-point energy of the empty system), which is nonzero.

The two-component structure means Path C alone cannot solve the CC problem. It can relax the curvature part; something else must handle the floor. This is VdD's conclusion from the workshop (Gap 2), endorsed by Volovik.

### 2.5. What Would a_2(tau) and a_4(tau) Approaching Zero Look Like?

If the transit-as-relaxation works for the curvature part, we expect:

    a_2(tau) -> 0     as tau -> infinity                                    (C-34)
    a_4(tau) -> 0     as tau -> infinity                                    (C-35)

Physically, this means the scalar curvature and the curvature-squared invariants of the Jensen metric on SU(3) both vanish in the extreme deformation limit. For a_2:

    a_2(tau) = (4pi)^{-4} integral_SU(3) [R(tau)/6 - E(tau)] dvol_g(tau)    (C-36)

This integral vanishes if either (a) R(tau) -> 0 pointwise, or (b) the integral of R cancels by symmetry despite local curvature divergences.

For SU(3) with a left-invariant metric, the scalar curvature of the Cartan-Killing metric is R = -dim(G)/4 = -8/4 = -2 (in appropriate units). Under Jensen deformation, R(tau) evolves as the anisotropy changes. At extreme anisotropy (tau -> infinity), the metric degenerates along one direction, and the sectional curvatures in planes containing that direction diverge while others vanish. The integral is a competition between these contributions.

For a_4, the situation is analogous but with curvature-SQUARED invariants (R^2, Ric^2, Riem^2), which are always non-negative. The integral of R^2 over a compact manifold with R = 0 everywhere is zero, but R cannot be zero everywhere on a compact Lie group with nonzero structure constants. At best, a_4(tau) can be SMALL relative to a_4(tau_fold), but whether it approaches zero depends on the specific cancellation pattern.

The computation S-ASYMPTOTIC-64 directly answers these questions.

---

## 3. Phase Transition Analogy: The Transit as a Quench

### 3.1. Kibble-Zurek Framework

The transit through the fold at tau = 0.190 is a QUENCH -- a rapid passage through a symmetry-breaking phase transition. The BCS condensate forms as the system cools through the van Hove singularity, and the GGE relic is the frozen-out state of the quench.

In the Kibble-Zurek framework (Paper 29 of the Landau corpus, Zurek 1985/1995), the key dynamical parameters are:

**Relaxation time.** Near the phase transition, the order parameter relaxation time diverges:

    tau_relax = tau_0 / |epsilon|^{nu*z}                                    (C-37)

where epsilon = (T - T_c)/T_c is the reduced temperature, nu is the correlation length exponent, and z is the dynamic critical exponent. For the Landau-Khalatnikov (Model A) dynamics (Paper 09, Landau-Khalatnikov 1954):

    z = 2,     nu = 1/2 (mean field)                                        (C-38)

giving nu * z = 1.

**Freeze-out condition.** When the relaxation time exceeds the rate at which external conditions change, the order parameter freezes:

    tau_relax(t-hat) = t-hat                                                (C-39)

For a linear quench epsilon(t) = t/tau_Q (where tau_Q is the quench timescale):

    t-hat = sqrt(tau_0 * tau_Q)                                             (C-40)

**Frozen correlation length.** The domain size at freeze-out:

    xi-hat = xi_0 * (tau_Q / tau_0)^{nu/(1 + nu*z)}                         (C-41)

**Defect density.** Topological defects (vortices, domain walls) form at domain boundaries:

    n_defect ~ 1/xi-hat^d ~ (tau_0/tau_Q)^{d*nu/(1 + nu*z)}                (C-42)

### 3.2. The Transit as a Quench: Parameter Identification

For the phonon-exflation transit:

**The order parameter.** The BCS gap Delta(tau). This is zero for tau << tau_fold (no pairing in the disordered phase) and nonzero for tau near tau_fold (BCS condensate forms). The gap vanishes again for tau >> tau_fold (BCS destroyed by excitation energy E_exc = 60.625 M_KK >> E_cond = 0.137 M_KK). The transit is a double quench: BCS forms and is immediately destroyed.

**The quench timescale.** From the transit dynamics (S38):

    tau_Q = dt_transit = 1.13 x 10^{-3} M_KK^{-1}                          (C-43)

(canonical_constants.py, dt_transit). The transit speed is Mach 13.75, making this an IMPULSIVE quench (omega_tau * tau_Q >> 1 is not satisfied -- the system passes through in one oscillation period, so the quench is impulse-regime, not adiabatic).

**The relaxation time.** The Landau-Khalatnikov relaxation time for the BCS gap is:

    tau_0 ~ 1/Delta ~ 1/0.464 M_KK ~ 2.16 M_KK^{-1}                       (C-44)

(the gap sets the fastest relaxation scale for pair excitations). The ratio:

    tau_Q / tau_0 ~ 1.13e-3 / 2.16 ~ 5.2 x 10^{-4}                        (C-45)

The quench is MUCH FASTER than the relaxation time: tau_Q / tau_0 << 1. This is deep in the impulse regime. The order parameter has NO TIME to respond to the changing thermodynamic conditions during the transit. This confirms the transit paradigm: the BCS condensate is created in a state far from equilibrium and immediately freezes into the GGE.

**The freeze-out time.** From (C-40):

    t-hat = sqrt(tau_0 * tau_Q) = sqrt(2.16 * 1.13e-3) = 0.049 M_KK^{-1}   (C-46)

This is the timescale at which the BCS order parameter freezes. It is much shorter than the transit time and much longer than the microscopic oscillation period.

### 3.3. Post-Quench Relaxation Dynamics

After the quench, the standard Kibble-Zurek theory predicts that the frozen domain structure evolves through coarsening dynamics. The characteristic length scale grows as:

    L(t) ~ (t/tau_0)^{1/z}                                                  (C-47)

where z is the dynamic critical exponent. For Model A (non-conserved order parameter, appropriate for the BCS gap which is not a conserved density):

    z = 2,     L(t) ~ sqrt(t)     (diffusive coarsening)                    (C-48)

The vacuum energy stored in the domain structure (domain walls, topological defects) relaxes as the domains coarsen. The vacuum energy per unit volume from domain walls of thickness xi and spacing L(t) is:

    rho_domain(t) ~ sigma / L(t) ~ sigma * sqrt(tau_0 / t)                  (C-49)

where sigma is the domain wall surface tension. This gives rho ~ t^{-1/2}, much slower than the Volovik 1/t^2.

For MODEL B (conserved order parameter, appropriate if the total pair number N_pair is conserved):

    z = 3 (Lifshitz-Slyozov),     L(t) ~ t^{1/3}                           (C-50)

giving rho_domain ~ t^{-1/3}, even slower.

Neither standard coarsening exponent gives 1/t^2.

### 3.4. Is alpha * beta = 2 the Right Value?

The Volovik relaxation rho ~ 1/t^2 comes from the vacuum variable q oscillating with microscopic frequency omega and damping as 1/t (Eq. C-2). In the condensed matter language, this is the relaxation of a MACROSCOPIC ORDER PARAMETER with both inertial and dissipative dynamics:

    m * d^2(q)/dt^2 + gamma * d(q)/dt + k * (q - q_0) = 0                  (C-51)

(damped harmonic oscillator with mass m, friction gamma, and restoring force k). At late times, the underdamped solution gives:

    q(t) - q_0 ~ (q_initial / t) * sin(omega * t + phi)                    (C-52)

where the 1/t envelope comes from the 3D radiation damping (the oscillating vacuum variable radiates gravitational waves into 3+1D spacetime, with power ~ |d^2q/dt^2|^2 ~ omega^4 * |q|^2, giving d|q|/dt ~ -omega^2 * |q| / t -- dimensional analysis in 3+1D gives the 1/t damping).

This gives rho ~ (q - q_0)^2 ~ 1/t^2, the Volovik exponent.

**The question is whether this dynamics applies to the spectral action.** The Jensen parameter tau is NOT a simple oscillator. It is a modulus field with:

- A potential V(tau) = -S(tau) (the spectral action is the negative of the effective potential because it enters the action with a positive sign)
- Hubble friction 3H * d(tau)/dt
- No radiation damping (tau is not coupled to a radiation field in the standard spectral action)

Without radiation damping, the modulus tau does not oscillate with a 1/t damping envelope. Instead, it rolls in its potential subject to Hubble friction:

    d^2(tau)/dt^2 + 3H * d(tau)/dt = -dV/dtau                              (C-53)

In a matter-dominated universe (H = 2/(3t)) or radiation-dominated (H = 1/(2t)):

- If V(tau) has a minimum at tau_0, the modulus oscillates about tau_0 with damping ~ 1/t (from Hubble friction), giving q ~ 1/t * sin(omega * t), exactly the Volovik form.

- If V(tau) is monotonically decreasing (which the spectral action IS -- S(tau) monotonically increasing means V = -S monotonically decreasing), there is NO minimum and NO oscillation. The modulus tau rolls forever down the potential, slowed by Hubble friction.

The framework's spectral action is MONOTONICALLY INCREASING (Structural Monotonicity Theorem, S37). There is no minimum in V(tau). The modulus does not oscillate. The Volovik damped-oscillator derivation of 1/t^2 does NOT directly apply.

**What replaces it?** For a monotonic potential V(tau) ~ -tau^p (power-law for large tau), the modulus dynamics with Hubble friction in a radiation-dominated universe gives:

    tau(t) ~ t^{2/(p+2)}     (attractor solution)                           (C-54)

For S(tau) ~ tau^{-alpha} (i.e., V ~ tau^{alpha} with reversed sign), the attractor gives:

    tau(t) ~ t^{2/(alpha+2)}                                                (C-55)

and therefore:

    S(tau(t)) ~ tau^{-alpha} ~ t^{-2*alpha/(alpha+2)}                       (C-56)

The effective relaxation exponent is:

    rho_vac ~ t^{-gamma},     gamma = 2*alpha/(alpha + 2)                   (C-57)

For alpha = 1 (VdD bound): gamma = 2/3.
For alpha = 2: gamma = 1.
For alpha -> infinity: gamma -> 2.

To get gamma = 2 (the Volovik value), we need alpha -> infinity -- exponential or faster-than-power-law decrease of S(tau). This is NOT excluded: if the eigenvalues of D_K grow linearly with tau and f is Gaussian, then S(tau) ~ exp(-c * tau^2) for large tau, which is faster than any power law.

This is the key theoretical prediction to test in S-ASYMPTOTIC-64: is the decrease of S(tau) for large tau power-law or exponential?

### 3.5. Universality Class of the Transit

The transit through the fold is a first-order phase transition (S38 paradigm: impulsive transit, not quasi-static). For first-order transitions, the Kibble-Zurek scaling is modified:

- The correlation length does NOT diverge (the transition is discontinuous)
- The domain size is set by the nucleation dynamics, not by critical slowing down
- The defect density is set by the nucleation rate, not by freeze-out

The transit at Mach 13.75 is supersonic, creating an acoustic white hole (pre/post-transit causally disconnected). This is NOT a standard Kibble-Zurek scenario but rather a spinodal decomposition -- the system is driven through the instability so fast that fluctuations have no time to develop. The GGE relic reflects the INITIAL CONDITIONS of the transit, not the equilibrium properties of either phase.

For the post-transit relaxation of the vacuum energy, the universality class is therefore NOT determined by the phase transition itself but by the SUBSEQUENT coarsening dynamics. In the framework, the post-transit state is the GGE relic, which is INTEGRABLE (Richardson-Gaudin). Integrable systems do NOT coarsen -- they preserve their initial domain structure forever (Paper 22, Rigol 2006; Paper 23, Vidmar-Rigol 2016). This is the ordered veil.

**Conclusion on the relaxation exponent.** The transit universality class does NOT determine the CC relaxation exponent. The relaxation is governed by the spectral action profile S(tau) and the modulus dynamics tau(t), not by critical phenomena. The Volovik alpha * beta = 2 is a SPECIFIC PREDICTION of the q-theory damped oscillator model, which may or may not map onto the spectral action dynamics. The mapping fails if S(tau) is monotonic (no oscillation). The correct exponent must be computed from the actual S(tau) profile at large tau.

---

## 4. S-ASYMPTOTIC-64: Computation Design

### 4.1. Objective

Compute the spectral action S(tau) and its Seeley-DeWitt coefficients a_0(tau), a_2(tau), a_4(tau) at tau values well beyond the fold, to determine:

(a) Whether a_2(tau) and a_4(tau) approach zero as tau -> infinity.
(b) If they do, the functional form (power law, exponential, or other).
(c) Whether the full (unexpanded) spectral action S(tau) approaches a_0 * f(0) or some other value.
(d) The effective relaxation exponent gamma in rho_curv ~ tau^{-gamma}.

### 4.2. Tau Values

    tau = 0.190 (fold -- calibration point, known values)
    tau = 0.500 (post-transit, already partially explored in earlier sessions)
    tau = 1.000 (significant deformation, 5x fold)
    tau = 2.000 (extreme deformation, 10x fold)
    tau = 5.000 (deep asymptotic regime)
    tau = 10.000 (terminal asymptotic)

Rationale: The fold is at tau = 0.190. The transit dynamics carry tau beyond the fold rapidly (Mach 13.75). By tau = 0.5, the system is well past the fold. By tau = 5 and 10, the Jensen metric is extremely anisotropic and the asymptotic scaling should be visible.

### 4.3. Quantities to Compute

At each tau value:

1. **D_K eigenvalues** {lambda_n(tau), d_n} (full 992 eigenvalues at L_max = 6, or 155,984 at L_max = 10 if computationally feasible).

2. **a_0(tau)** = sum_n d_n. Should be EXACTLY constant (= 6440) for all tau by Theorem T14. This is the calibration check.

3. **a_2(tau)** = (1/6) * sum_n d_n * lambda_n(tau)^{-2} (for the heat kernel on compact manifold, a_2 involves the inverse-squared eigenvalue sum weighted by curvature -- the precise formula depends on the heat kernel expansion, but the numerical computation sums over the spectrum directly).

    Operationally: a_2 is extracted from the heat kernel K(t) = sum_n d_n exp(-lambda_n^2 * t) via the small-t expansion K(t) = a_0 * t^{-4} + a_2 * t^{-3} + a_4 * t^{-2} + ..., fitting the first few coefficients.

4. **a_4(tau)** = extracted from the same heat kernel fit.

5. **S(tau)** = sum_n d_n f(lambda_n(tau)^2 / Lambda^2) for Gaussian cutoff f(x) = exp(-x) with Lambda = M_KK.

6. **dS/dtau** = numerical derivative (finite difference between adjacent tau values, cross-checked with analytical derivative if available).

### 4.4. Pass/Fail Criteria

**Gate: S-ASYMPTOTIC-64**

Pre-registered criteria:

**PASS (Path C viable for rho_curv)**:
- a_2(tau) is monotonically decreasing for all tau > 0.19.
- a_2(tau) fits a power law a_2 ~ tau^{-alpha} with alpha > 0 (R^2 > 0.9 on log-log plot).
- S(tau) approaches a_0 * f(0) = 6440 from above as tau increases.
- The excess S(tau) - 6440 decreases with tau.

**FAIL (Path C blocked)**:
- a_2(tau) is NOT monotonically decreasing (it increases or oscillates for tau > 0.19).
- a_2(tau) asymptotes to a nonzero constant: a_2(10)/a_2(0.19) > 0.5.
- S(tau) does NOT approach a_0 * f(0) -- it approaches a different constant or diverges.

**INFO (partial relaxation, exponent determination)**:
- a_2(tau) decreases but the exponent alpha < 1 (VdD bound saturated or violated).
- S(tau) decreases but the effective relaxation exponent gamma < 1 (insufficient for CC resolution).
- a_4(tau) behaves differently from a_2(tau) (different asymptotic exponents for different moments).

### 4.5. Computational Method

The D_K eigenvalues at arbitrary tau are computed from the Jensen-deformed Dirac operator on SU(3), using the Peter-Weyl decomposition into (p,q) sectors. The existing code (s42_gradient_stiffness.py and related scripts) computes eigenvalues at tau = 0.190. The computation must be extended to arbitrary tau by modifying the Jensen deformation parameter in the metric tensor.

The critical code requirement: the Jensen metric g(tau) enters the Dirac operator through the spin connection, which enters the Dirac operator through the covariant derivative. The tau-dependence is in the metric coefficients (Cartan and root direction eigenvalues of g), and these propagate to the eigenvalues through the structure constants of su(3).

Expected computational cost: each tau value requires diagonalizing the D_K operator in each (p,q) sector up to L_max. At L_max = 6, the largest sector has dimension ~100, so the diagonalization is cheap. The full computation at 6 tau values should take minutes, not hours.

---

## 5. Assessment

### 5.1. Constraint Map Position

Path C occupies the following position in the CC constraint map:

**Walls it respects:**
- Structural Monotonicity Theorem (S37): S(tau) is monotonically increasing for smooth cutoffs. Path C does not require S(tau) to have a minimum -- it requires S(tau) to DECREASE beyond the fold, which is not excluded by the theorem (the theorem proves monotonicity for the forward sweep tau increasing from 0 to 0.19, not for the full range).

    CORRECTION: The Structural Monotonicity Theorem (CUTOFF-SA-37) states S_f(tau) is monotone for ALL smooth monotone cutoffs, ALL Lambda, ALL tau in [0, 0.5]. The domain is [0, 0.5], not [0, infinity]. The theorem does not constrain S(tau) for tau > 0.5. Path C operates in the tau > 0.5 regime and is NOT in conflict with the theorem.

- Block-Diagonal Theorem (S22b): Path C does not require inter-sector coupling.
- Theorem T14: Path C explicitly acknowledges the a_0 floor and works within it (two-component CC).
- 9 CC closures: All 9 closures address mechanisms for relaxing the FULL CC. Path C concedes the floor and addresses only rho_curv. This is a different (weaker) claim that does not conflict with the closures.

**Gates it has passed:** None (no computation yet).

**Gates remaining:**
- S-ASYMPTOTIC-64 (CRITICAL): the decisive computation.
- Modulus dynamics computation: tau(t) for the Friedmann-coupled spectral action beyond the fold.
- Two-component decomposition quantification: what fraction of the CC is rho_curv vs rho_0?

### 5.2. Best-Case Outcome

S-ASYMPTOTIC-64 returns PASS. The curvature coefficients a_2(tau) and a_4(tau) decrease as power laws (or faster) beyond the fold. The full spectral action approaches a_0 * f(0) = 6440 from above. The excess S(tau) - 6440 relaxes as tau^{-alpha} with alpha >= 1. Combined with modulus dynamics giving tau ~ t^{beta} with alpha * beta >= 2, the curvature part of the CC relaxes to zero at the present epoch.

The remaining problem: the floor rho_0 = f_0 Lambda^4 a_0 is still 114 OOM too large. Path C has split the CC problem into two pieces:
- rho_curv: SOLVED (transit relaxation)
- rho_0: OPEN (requires Volovik equilibrium theorem, K-class transition, or new mechanism)

In this best case, Path C is a STRUCTURAL ADVANCE -- it reduces the CC problem from one monolithic 114-OOM gap to a cleaner problem about the bare spectral weight. The a_0 floor is a TOPOLOGICAL quantity (mode count times volume), and its cancellation may have a topological origin (e.g., fermionic sector cancellation with DIFFERENT spectra, evading Closure 9's same-spectrum obstruction).

### 5.3. Worst-Case Outcome

S-ASYMPTOTIC-64 returns FAIL. The curvature coefficients a_2(tau) and a_4(tau) do NOT decrease beyond the fold -- they increase, oscillate, or asymptote to nonzero constants. The spectral action does not relax. The entire CC remains a single 114-OOM problem with no dynamical relaxation mechanism.

This outcome would mean:
- The transit-as-relaxation idea is closed.
- The CC is entirely a static problem: rho_vac = S(tau_frozen) at whatever tau value the modulus freezes.
- The surviving paths reduce to: Path A (Jacobson integration constant), Path B (gravitational integrability breaking, 108 OOM short), Path E (self-consistent BdG spectral triple), and Path F (finite-size insight with no resolution).

### 5.4. Most Likely Outcome (Structural Assessment, Not Probability)

The structural arguments suggest a_2(tau) DOES decrease beyond the fold, because the curvature of a degenerate metric is controlled by the anisotropy, and extreme anisotropy produces cancellations in the curvature integral. The question is the RATE of decrease.

The VdD structural bound alpha <= 1 is a LOWER bound on the decay rate -- it says a_2 cannot decrease faster than 1/tau. But the full (unexpanded) spectral action can decrease faster (exponentially, if eigenvalues grow linearly with tau and the cutoff is Gaussian).

The most likely outcome of S-ASYMPTOTIC-64 is INFO: a_2 decreases, but the exponent alpha and the effective relaxation exponent gamma are determined by the computation, not predicted in advance. The value of gamma determines whether Path C resolves the CC or merely reduces it.

### 5.5. Relationship to Other Paths

Path C is COMPLEMENTARY to, not competing with, other paths:

- **Path B (gravitational integrability breaking)**: Addresses the GGE structure, not the spectral action profile. Can operate alongside Path C.
- **Path E (self-consistent BdG triple)**: The BdG modification of D_K changes the eigenvalues and therefore changes S(tau). The self-consistent BdG spectral action S_{BdG}(tau) may have a DIFFERENT asymptotic profile than the bare S(tau). S-ASYMPTOTIC-64 computes the BARE spectral action; the BdG version is a separate (harder) computation.
- **Path F (finite-size)**: Explains why rho_vac is nonzero but not why it is small. Path C (if it works) explains why the curvature part is small. Together, they give a complete account: nonzero because of finite size, small because of transit relaxation of the curvature part.

### 5.6. The Landau Assessment

From the condensed matter perspective, Path C maps to a well-understood physical scenario: a system quenched through a phase transition, with the order parameter frozen by integrability, and the vacuum energy stored in the curvature of the effective potential.

The analogy is to a superfluid quenched below T_c so fast that the order parameter cannot equilibrate. The vacuum energy stored in the gradient energy of the frozen domain structure relaxes as the domains coarsen -- but ONLY if the dynamics are non-integrable. In an integrable system, the domains do NOT coarsen and the vacuum energy is PERMANENT (the GGE prevents thermalization).

The transit-as-relaxation mechanism proposes that the spectral action S(tau) itself decreases as tau increases, providing a relaxation channel that does not require breaking the GGE. This is different from standard coarsening -- it is the POTENTIAL ENERGY of the modulus decreasing as the modulus rolls, not the KINETIC ENERGY of domain walls being dissipated.

This is physically sound: a modulus rolling in a decreasing potential loses potential energy to the gravitational sector (Hubble friction converts kinetic energy to expansion). The CC relaxes because the potential energy ITSELF decreases. The question is quantitative: does S(tau) decrease fast enough?

The a_0 floor is the analogue of the zero-point energy in a quantum liquid. In a laboratory superfluid (3He, 4He), the zero-point energy is canceled by the microscopic short-range physics (trans-Planckian cancellation -- Volovik Paper 04). In the framework, there is no external microscopic physics to cancel a_0. The floor IS the CC problem, in its most reduced form.

S-ASYMPTOTIC-64 is the decisive computation. Everything in this document is structural argument pending that calculation.

---

## A. Notation and Constants

| Symbol | Value | Units | Source |
|:-------|:------|:------|:-------|
| tau_fold | 0.190 | dimensionless | S12, canonical_constants.py |
| S_fold | 250,360.68 | M_KK | S42, canonical_constants.py |
| a_0 | 6440.0 | -- | S42, canonical_constants.py |
| a_2(fold) | 2776.17 | M_KK^{-2} | S42, canonical_constants.py |
| a_4(fold) | 1350.72 | M_KK^{-4} | S42, canonical_constants.py |
| dS/dtau | +58,672.80 | M_KK | S42, canonical_constants.py |
| M_KK | 7.429 x 10^{16} | GeV | S42, canonical_constants.py |
| f_0 | 9.817 | dimensionless | S62 |
| m_tau | 2.062 | M_KK | S42 |
| omega_tau | 8.27 | M_KK | S38 |
| H_fold | 586.53 | M_KK | S38, canonical_constants.py |
| dt_transit | 1.13 x 10^{-3} | M_KK^{-1} | S38, canonical_constants.py |
| Delta_0 | 0.464 | M_KK | S37, canonical_constants.py |
| E_cond | -0.137 | M_KK | S36, canonical_constants.py |
| E_exc | 60.625 | M_KK | S38, canonical_constants.py |
| rho_obs | 2.7 x 10^{-47} | GeV^4 | Planck 2018 |

## B. Source Documents

- Volovik Paper 04 (2005): Vacuum energy equilibrium theorem. `researchers/Volovik/04_2005_Volovik_Vacuum_Energy_Cosmological_Constant.md`
- Volovik Paper 25 (2013): Cosmology as relaxation to equilibrium. `researchers/Volovik/25_2013_Volovik_Superfluids_Non_Equilibrium_Vacua.md`
- Landau-Khalatnikov Paper 09 (1954): TDGL relaxation dynamics. `researchers/Landau/09_Landau_Khalatnikov_1954_TDGL.md`
- Landau Paper 04 (1937): Phase transition theory. `researchers/Landau/04_Landau_1937_Phase_Transitions.md`
- Zurek Paper 29 (1985/1995): Kibble-Zurek mechanism. `researchers/Landau/29_Zurek_1985_Kibble_Zurek.md`
- Framework CC OOM document: `sessions/archive/session-63/framework-cc-oom.md`
- Volovik-VdD workshop: `sessions/archive/session-63/session-63-volovik-van-den-dungen-workshop.md`
