# Nonequilibrium Quantum Field Theory

**Author(s):** Esteban A. Calzetta, Bei-Lok B. Hu
**Year:** 2008 (comprehensive monograph); foundational work 1995-2004
**Journal:** Cambridge Monographs on Mathematical Physics

---

## Abstract

Calzetta and Hu develop a rigorous functional formalism for quantum field theory far from equilibrium, using the Schwinger-Keldysh contour technique. Their monograph provides the mathematical framework for computing non-equilibrium evolution, including particle production, thermalization, prethermalization, and transport phenomena. The Schwinger-Keldysh formalism—which uses a closed-time-path contour—allows systematic calculation of expectation values of operators for quantum fields initialized in arbitrary non-thermal states.

---

## Historical Context

By the 1990s, quantum field theory in curved spacetime (Parker, Birrell-Davies) had established that particles are produced in time-dependent backgrounds. However, computing the subsequent evolution (how the created particles interact, thermalize, and reach equilibrium) required new techniques. The Schwinger-Keldysh formalism, developed in 1960-1961 (Schwinger, Keldysh), provides a path-integral method to track this evolution systematically. Calzetta and Hu brought this formalism to cosmology and made it accessible, along with applications to preheating, reheating, and thermalization in the early universe.

---

## Key Arguments and Derivations

### Schwinger-Keldysh Contour and Path Integral

The partition function for a non-equilibrium system is computed using a closed-time path contour C going from t_i → t_f → t_i. The generating functional is:

Z_C[J_+, J_-] = ∫ D[φ_+] D[φ_-] exp(i S_C[φ_+, φ_-])

where the action includes contributions from the forward branch (φ_+) and backward branch (φ_-):

S_C = ∫ d⁴x [L(φ_+) - L(φ_-)]

Green's functions are defined with both forward and backward fields:

G_>(x, x') = ⟨φ_+(x) φ_-(x')⟩
G_<(x, x') = ⟨φ_-(x') φ_+(x)⟩

### Transformation to Retarded/Advanced Basis

The "physical" basis uses retarded (R), advanced (A), and symmetric (F) Green's functions:

G_R(x, x') = θ(t - t')[φ(x), φ(x')]
G_A(x, x') = -θ(t' - t)[φ(x), φ(x')]
G_F(x, x') = (1/2)⟨{φ(x), φ(x')}⟩

The retarded and advanced functions encode causality; the symmetric (Keldysh) function encodes statistical information.

### Dyson Equations and Self-Energy

Non-equilibrium evolution is governed by Dyson equations:

(□ - m² - Σ_R[φ]) G_F = source term

where Σ_R is the retarded self-energy (one-loop contributions, rescattering, etc.). The self-energy includes corrections from interactions and from the created particle background.

### Initial Conditions and Thermal Limit

For an initial thermal state at temperature T_i:

G_F^{(eq)}(t, t'; **k**) = (1 + 2n_B(ω_k, T_i)) sinh(ω_k(t - t'))

where n_B(ω, T) = 1/(exp(ω/T) - 1) is the Bose-Einstein distribution. For a far-from-equilibrium initial state (e.g., coherent inflaton oscillations):

G_F^{(0)}(t, t'; **k**) = φ₀²/2 cos(m(t - t'))

### Prethermalization from Kadanoff-Baym Equations

The Kadanoff-Baym equations for G_< and G_> are:

(□_x - m²)G_<(x, y) = -i ∫ d⁴z Σ_>(x, z) G_<(z, y)

(□_y - m²)G_<(x, y) = i ∫ d⁴z G_<(x, z) Σ_<(z, y)

These coupled equations govern how the occupation number n_k(t) = (i/2)[G_<(t, t; **k**) - G_>(t, t; **k**)] evolves. Remarkably, prethermalization—where n_k reaches a quasi-steady state before final thermalization—emerges naturally from these equations.

### Entropy Production and H-theorem

For a weakly perturbed system starting far from equilibrium, the entropy increases as:

dS/dt = -Tr[ln ρ dρ/dt] ≥ 0

The rate of entropy production is proportional to the deviation from equilibrium:

dS/dt ~ ∫ d⁴k Σ_k [ln n_k + (1 ± n_k)/(1 - n_k)] × dn_k/dt

This formalism guarantees irreversibility while maintaining unitarity (no information loss in principle, though correlations become unobservably fine-grained in practice).

---

## Key Results

1. **Quantum Kinetics**: The evolution of occupation numbers n_k(t) can be extracted from Green's functions without explicitly computing the full quantum state. This makes the problem tractable.

2. **Prethermalization Signatures**: For integrable systems with conserved charges, prethermalization produces plateau-like behavior:

   n_k(t) → n_k^{(plateau)} for t_1 < t < t_2
   n_k(t) → n_B(ω_k, T_final) for t >> t_2

   The plateau occurs because fast processes (elastic scattering) redistribute energy among modes before slower processes (inelastic scattering) thermalize.

3. **H-theorem for Quantum Systems**: Entropy (defined as -Tr(ρ ln ρ)) increases monotonically in non-equilibrium evolution, even for time-reversible microscopic dynamics.

4. **Applicability to Cosmological Reheating**: Calzetta-Hu formalism can compute the evolution of the particle distribution during preheating/reheating, including backreaction effects and thermalization timescales.

---

## Impact and Legacy

Calzetta-Hu's monograph became the standard reference for non-equilibrium QFT:

- **Preheating Simulations**: Their formalism is the basis for numerical studies of preheating dynamics (e.g., Berges, 2002).

- **Thermalization in QCD**: Applied to quark-gluon plasma formation in heavy-ion collisions.

- **Cold Atoms**: Adapted for studying thermalization in isolated quantum systems (ultracold gases).

- **Quantum Computing**: The formalism is used to analyze relaxation and decoherence in quantum information systems.

---

## Connection to Phonon-Exflation Framework

**PHONONIC RELEVANCE: CRITICAL**

Calzetta-Hu provides the mathematical formalism for tracking **non-equilibrium evolution** of **quantum fields**—exactly what is needed to compute GGE relic formation and its dynamics in the framework.

1. **Schwinger-Keldysh for Spectral Modes**: The framework applies Calzetta-Hu's closed-time-path formalism to the 155,984 eigenvalues of D_K. The retarded/advanced Green's functions G_R(τ), G_A(τ) encode the dynamics of mode mixing during the transit.

2. **Dyson Equations for Spectral Evolution**: The spectral self-energy is:

   Σ_spectral(τ) = (geometric backreaction)

   This includes the effect of created pairs (GGE quasiparticles) on the spectral-action potential.

3. **Prethermalization in the GGE**: The framework claims the GGE relic is a **prethermalized state**—it has reached a quasi-equilibrium characterized by the generalized Gibbs ensemble but has NOT yet thermalized to the full thermal distribution. This matches Calzetta-Hu predictions:

   - Initial state: vacuum at τ = 0.189
   - Prethermalized state: GGE at τ = 0.190
   - Final thermal state: achieved at τ ≈ 0.20 (after further expansion)

4. **Entropy Production**: The framework predicts entropy increases during the transit:

   ΔS_transit = (spectral_action_change) × (Bogoliubov_factor)

   According to Calzetta-Hu, this entropy increase is irreversible—a thermodynamic arrow of time emerges from spectral dynamics, not from gravity.

5. **Quantitative Prediction**: Using Calzetta-Hu formalism, compute the occupation numbers n_eigenvalue(τ) for the 155,984 modes of D_K during the transit. The result should show:
   - n_k(τ < 0.190) = 0 (vacuum)
   - n_k(0.190 < τ < 0.195) = plateau (GGE)
   - n_k(τ > 0.20) = Bose-Einstein distribution (thermal)

   If this matches the framework's GGE permanence prediction (no thermalization post-transit), Calzetta-Hu validates the framework's claim to "ordered veil" dynamics (integrable, non-chaotic).

**Key test**: Measure whether CMB power spectrum shows signatures of prethermalization (deviations from blackbody spectrum) vs full thermalization. Framework predicts prethermalization signature: power-law tail at high frequencies (n_k ~ k^p, p < -1 for blackbody), flattening after GGE formation. DESI/Planck sensitivity: ~ 10⁻⁴.
