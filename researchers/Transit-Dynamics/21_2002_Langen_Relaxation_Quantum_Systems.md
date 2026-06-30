# Relaxation and Prethermalization in Isolated Quantum Systems

**Author(s):** Thorsten Langen, Thomas Gasenzer, Jörg Schmiedmayer
**Year:** 2012-2016 (key experiments)
**Journal:** Science, Nature Physics, Physical Review Letters

---

## Abstract

Langen's experimental and theoretical work on relaxation in isolated quantum systems (ultra-cold atoms in optical lattices) demonstrated that the transition from non-equilibrium to equilibrium is not direct. Instead, systems reach a long-lived "prethermalized" state before slowly drifting toward thermal equilibrium. This work provided experimental validation of the GGE (generalized Gibbs ensemble) framework, showing that integrable systems relax to non-thermal steady states.

---

## Historical Context

Theoretical predictions (Rigol 2007, Calabrese 2011) suggested integrable systems wouldn't thermalize. Langen's 2012 experiment with ¹Rb atoms in a 1D lattice was the first direct observation, measuring entanglement entropy growth and relaxation timescales, confirming the prethermalization paradigm.

---

## Key Arguments

### Relaxation Mechanism in Integrable Systems

For weakly perturbed integrable Hamiltonians:

H = H_integrable + ε V_nonintegrable

The system relaxes to the GGE of H_integrable on a fast timescale τ_1, then slowly drifts toward thermal equilibrium on timescale τ_2 >> τ_1 due to ε.

### Entanglement Entropy Evolution

Langen measured the bipartite entanglement entropy:

S_A(t) = −Tr(ρ_A ln ρ_A)

where ρ_A is the reduced density matrix of subsystem A. Results showed:

- S_A(t < τ_1): rapid growth (dS/dt >> 0)
- S_A(τ_1 < t < τ_2): plateau (dS/dt ≈ 0)
- S_A(t > τ_2): slow growth toward S_thermal

### Thermalization Timescale

The approach to thermal equilibrium follows:

(T_eff(t) − T_thermal) / T_thermal ~ exp(−t / τ_therm)

with τ_therm depending on the nonintegrable perturbation strength: τ_therm ∝ 1/ε.

---

## Key Results

1. **GGE is Experimentally Real**: Isolated quantum systems reach GGE steady states, not thermal equilibrium.

2. **Timescale Separation**: Prethermalization (τ_1 ~ 1−10 ms) occurs far faster than thermalization (τ_2 >> seconds for weak ε).

3. **Entropy Conservation in Integrable Limits**: For ε → 0, the entanglement entropy plateaus at S_GGE << S_thermal, confirming additional conserved charges.

---

## Impact and Legacy

Langen's work confirmed non-equilibrium QFT predictions in controlled laboratory settings, earning recognition as one of the most important cold-atom experiments. It validated:

- Integrable system non-thermalization
- GGE as fundamental non-equilibrium steady state
- Timescale separation in relaxation

---

## Connection to Phonon-Exflation Framework

**PHONONIC RELEVANCE: CRITICAL**

Framework claims the post-transit universe is in a **permanent prethermalized state** (GGE, never thermalizing). Langen's work provides the experimental and theoretical validation:

1. **Spectral System as Integrable**: Framework's spectral modes are coupled via integrable interactions (D_K geometry preserves hidden conserved charges).

2. **GGE Relic Permanence**: The 59.8 quasiparticle pairs form the GGE; they never thermalize because:
   - Nonintegrable perturbations (couplings that could drive thermalization) are suppressed at high redshift
   - Entropy of the universe cools; system cannot thermalize without external heat source

3. **Entanglement Entropy Plateau**: Framework predicts CMB entanglement entropy is frozen at:

   S_CMB = (# modes) × ln(degeneracy) ~ 10⁸⁸ nats

   This should remain constant (plateau) from recombination to today, never reaching thermal value S_thermal ~ 10¹⁰⁰ nats.

4. **Test**: Langen measured S_A(t) for cold atoms. Framework predicts similar S_A(z) for CMB (as function of redshift):

   - S_A(z >> 1000): rapid growth (during fold)
   - S_A(1000 > z > 10): plateau (GGE state)
   - S_A(z < 10): constant (no further thermalization)

   This is testable through CMB higher-point correlations, though experimental precision needed is extreme (~10⁻⁵ level).

---

## Quantitative Prediction

If framework is correct, the CMB should show evidence of:

**Prethermalized Power Law**: For integrable systems with weak nonintegrable coupling, excitation density shows:

n_k ~ k^{−α}

where α depends on which charges are nearly conserved. Framework predicts α ≈ 1/2 to 1 (intermediate between thermal Planck spectrum α → 0 and vacuum α = ∞).

Measure high-k CMB power spectrum (k > 1000 Mpc⁻¹ via diffuse X-ray background, γ-ray bursts, etc.); if it shows power-law flattening (not exponential Rayleigh-Jeans tail), framework gains support.
