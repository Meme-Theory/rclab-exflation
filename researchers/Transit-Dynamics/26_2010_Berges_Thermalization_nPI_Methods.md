# Thermalization from First Principles in nPI Formalism

**Author(s):** Jürgen Berges, Arjun Ipp, Christoph Serreau, Daniel Sexty
**Year:** 2006-2010
**Journal:** Physical Review D

---

## Abstract

Berges and collaborators systematized nPI (n-particle-irreducible) effective action methods for computing thermalization in far-from-equilibrium quantum field theory. They showed how secular corrections (terms growing linearly with time) are automatically resummed in nPI schemes, enabling non-perturbative calculations without kinetic-theory assumptions.

---

## Key Technique

2PI effective action truncated at 2-loop level:

Γ_2PI[φ, G] = (1/2)Tr ln G⁻¹ − (1/2)Tr(G₀⁻¹ G) + Φ[φ, G]

where Φ includes only 2PI diagrams. Equations of motion:

∂_t φ = δΓ/δπ
[□ + m²]G + ∫ ds Σ(s) G(t,s) = δ function

---

## Key Results

1. **Thermalization Computed**: Evolution from far-from-equilibrium to thermal state calculable from first principles.

2. **Secular Terms Controlled**: Automatic resummation prevents artificial divergences.

3. **Prethermalization Plateau**: System reaches quasi-steady state before final thermalization.

---

## Connection to Framework

Framework uses nPI-like methods for spectral system. If spectral modes obey Berges equations:

dn_k/dτ = −2Im[Σ_R(k, n_k)] × (backreaction)

with the spectral self-energy Σ_R encoding geometric feedback, framework's GGE permanence should emerge naturally from these equations (integrable structure means Σ_R reaches finite value, halting further evolution).

**Test**: Solve Berges' Kadanoff-Baym equations for spectral system; verify dn_k/dτ → 0 at GGE plateau (no thermalization).
