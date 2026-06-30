# Dark Energy and Stabilization of Extra Dimensions

**Author(s):** Brian R. Greene, Janna Levin

**Year:** 2007

**Journal/ArXiv:** arXiv:0707.1062

---

## Abstract

The authors discuss the role Casimir energies may play in addressing issues of moduli stabilization and dark energy. In particular, they examine a non-supersymmetric brane-world scenario with toroidal extra dimensions in which Casimir energies of bulk fields generate a stabilizing potential for the toroidal volume while driving accelerated expansion in the non-compact directions.

The work speculates that such a scenario might establish a link between asymmetric topology and asymmetric geometry; that is, asymmetric topology could be linked to the hierarchy between large and small dimensions. The authors show that Casimir energies from balanced contributions of fields with different masses and spins can develop a non-trivial minimum stabilizing extra dimension size, while the large dimensions experience accelerated expansion from the Casimir energy density.

---

## Historical Context

Extra dimensions have been proposed for nearly a century in attempts to unify gravity with electromagnetism (Kaluza-Klein theory). Although the original unification goal was abandoned, the fundamental question remains: Why are precisely three spatial dimensions observably large?

Modern unification attempts, notably supergravity and string theory, revived extra dimensions in promising theoretical contexts but left the "why three?" question unanswered. Additionally, these theories highlight two significant subtleties: the need to stabilize the size of extra dimensions (moduli stabilization) and the need to drive periods of accelerated expansion (dark energy).

One approach treats these as part of the larger string/M-theory vacuum degeneracy problem, invoking anthropic arguments. A more satisfying solution would identify a dynamical mechanism that ensures three spatial dimensions grow large while others remain unobservably small.

This work proposes that Casimir energies--quantum mechanical energy densities arising from boundary conditions on finite spaces--may play a crucial role in addressing both moduli stabilization and dark energy simultaneously.

---

## Key Arguments and Derivations

### Casimir Energies and Quantum Boundary Conditions

Whenever finite spatial extent exists for any dimensions, quantum field fluctuations contribute to a purely quantum mechanical energy density determined by the boundary conditions imposed on the finite space. The Casimir energy density in an (N+1)-dimensional spacetime with all spatial sections compact at characteristic size b has the form:

<T_μν> = diag(-rho, p_vector)

where the energy density ρ ∝ b^(-(N+1)) and the pressure in each dimension is p_b = ρ/N.

For small extra dimensions, Casimir energies can be correspondingly large. By balancing Casimir energy contributions from fields with different masses and spins, the total Casimir energy as a function of the extra dimension radius can develop a non-trivial minimum that stabilizes the dimension size.

### Anisotropic Cosmologies and Casimir Energy

For an anisotropic spacetime with metric:

ds^2 = -dt^2 + a^2(t) dx^2_i + b^2(t) dy^2

where a is the scale factor of 3 large directions and b is the scale factor of n small (compact) directions, the Einstein equations reduce to:

H_dot_a + 3H_a^2 + nH_a H_b = 8πG/(2+n) * [ρ + (n-1)p_a - np_b]

H_dot_b + nH_b^2 + 3H_a H_b = 8πG/(2+n) * [ρ + 2p_b - 3p_a]

For stability, dimensional analysis requires ρ ∝ b^(-(n+4)). If ρ is independent of a (as required by conservation of energy with w_a = -1), then for a massless field w_b = 4/n. This equation of state neither stabilizes dimensions nor acts as dark energy.

However, suppose:

ρ = α/b^(4+n) * [1 - β b^2 + γ b^4]

This is the basic form of Casimir energy for a light field with flat compact directions and periodic boundary conditions. By adjusting parameters, dimensions stabilize when:

w_b = -2

giving the condition on b:

b^2_max,min = β(n+1) ± sqrt[(n+1)^2 β^2 - 4n(n+2)γ] / (2nγ)

### Casimir Energy from Multiple Fields

For Casimir contributions from multiple fields with different masses and spins, the energy density in (3+n+1)-dimensional spacetime compactified on T^n with periodic boundary conditions is:

ρ = m^(N+1) / (2π)^((N+1)/2) * sum_j K_(N+1)/2(bm sqrt(j1^2 + ... + jn^2)) / (bm sqrt(j1^2 + ... + jn^2))^((N+1)/2)

where N = 3 + n is the total number of spatial dimensions and m is the mass of the contributing field. The j_1 = ... = j_n = 0 term is infinite and subtracted in renormalization.

By superposing contributions from fermions and bosons of different masses, a total Casimir energy with the desired polynomial form can be constructed. For example, with sterile Dirac neutrinos of masses m_ν1, m_ν2 = λm_ν1, plus additional species with anti-periodic boundary conditions, a potential minimum emerges at specific parameter values.

### Effective Field Theory and Radion Picture

In the 4D effective field theory perspective, integrating over extra dimensions and performing a conformal transformation to Einstein frame yields:

S_eff = integral d^4 x sqrt(-g_E) * [m_p^2/(16π) * R[g_E] - 1/2 g^μν_E D_μ Ψ D_ν Ψ - U(Ψ)]

where Ψ is the radion field (the modulus of the extra dimension size b), and U(Ψ) = V b^n Ω^(-2) with Ω = [M^(2+n) b^n / m_p^2].

At the extremum of the potential (∂U/∂Ψ = 0), which corresponds to ρ = -ρp_b/2, the radion stabilizes. The potential U(Ψ) depends on the Casimir energy of all bulk fields and exhibits a minimum at b_min that provides stable moduli stabilization.

### Connection to Dark Energy

With b stabilized at b_min, the large dimensions experience an energy density:

ρ_4D = ρ(b_min) * b_min^n

which acts like a cosmological constant for 4D observers (equation of state w = -1). This Casimir energy density, when matched to the observed dark energy, gives:

α / b^4 = ρ_DE ~ (2.3 × 10^-3 eV)^4

For example, with n = 2 extra dimensions and properly chosen bulk field spectrum:

b_min ~ O(0.2 mm)

corresponding to a Planck scale M ~ 3 TeV, consistent with the ADD model for addressing the hierarchy problem.

---

## Key Results

1. **Moduli Stabilization**: Casimir energies from bulk fields can generate a stabilizing potential for extra dimensions with a well-defined minimum, solving the moduli stabilization problem dynamically.

2. **Dual Role**: The same Casimir energy that stabilizes extra dimensions simultaneously provides an effective dark energy in large directions, with equation of state w_a = -1 and w_b = -2.

3. **Hierarchical Geometry**: Extra dimensions can be stabilized at scales (b ~ 10^-5 m) consistent with experimental bounds on gravity deviations and neutrino mass scales, establishing a possible connection between dark energy and small massive scale fields.

4. **Field Spectrum Requirement**: Stabilization requires careful tuning of bulk field masses and degrees of freedom to produce Casimir contributions that sum to the required potential form. Parameter ranges are narrow (e.g., 0.4 < λ < 0.42 for n=2).

5. **TeV-Scale Planck Mass**: For n=2 extra dimensions with b_min ~ 1/(10^-3 eV), the natural Planck scale is M ~ 3 TeV, linking dark energy to the electroweak hierarchy problem.

6. **Topological Link**: Because Casimir energies depend sensitively on topology, different topologies of large vs. small dimensions will produce different stabilization conditions, suggesting that topology may determine geometry (why 3 large dimensions).

---

## Impact and Legacy

This work established Casimir effects as a serious mechanism for addressing two of cosmology's deepest problems simultaneously: moduli stabilization and dark energy. The framework demonstrated that quantum mechanics on compact spaces naturally produces effects with magnitude comparable to observed dark energy.

The connection between moduli stability and dark energy became influential in string theory cosmology. The work's insight that topology and geometry interrelation might explain the dimension count shaped subsequent research on string landscape and anthropic reasoning.

---

## Connection to Phonon-Exflation Framework

The phonon-exflation framework embeds the Standard Model in M4 x SU(3) spectral geometry with compactified SU(3) fiber. Several aspects of Greene-Levin's work resonate deeply with phonon-exflation:

- **Casimir Energy and Spectral Action**: The framework's spectral action naturally includes Casimir-like contributions from internal geometry. The stabilization mechanism for the SU(3) fold parallels Casimir energy stabilization of KK dimensions.

- **Dark Energy from Internal Geometry**: Both frameworks propose dark energy emerges from the internal space geometry. Greene-Levin's Casimir mechanism and phonon-exflation's spectral geometry evolution both predict w ~ -1 for large-scale expansion.

- **Moduli as Observable**: In phonon-exflation, the internal geometry's size evolution (parameterized by τ) acts as a "modulus" shaping both particle spectra and cosmic expansion. Like Greene-Levin's radion, this modulus stabilizes and drives acceleration.

- **Hierarchy Problem Connection**: Greene-Levin's TeV-scale Planck mass from extra dimension geometry parallels phonon-exflation's KK scale. Both frameworks suggest the hierarchy problem and dark energy share geometric origins.

- **Field Spectrum Sensitivity**: Just as Greene-Levin shows that careful field spectrum balance produces Casimir potential minima, phonon-exflation predicts that internal geometry evolution depends sensitively on spectral properties of the Dirac operator--making particle content determining geometry.

- **Topology and Cosmology**: Greene-Levin's insight that topology determines which dimensions grow large extends to phonon-exflation: the SU(3) topology determines which compactification modes are active and how they affect cosmic expansion.

This work provides a concrete realization of how quantum geometry (through Casimir effects) can stabilize extra dimensions and drive dark energy--a mechanism closely parallel to phonon-exflation's spectral geometry approach.
