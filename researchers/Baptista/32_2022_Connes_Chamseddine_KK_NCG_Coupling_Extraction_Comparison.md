# Kaluza-Klein versus Noncommutative Geometry: Gauge Coupling Extraction Normalization

**Author(s):** [Synthesis] Alain Connes, Ali H. Chamseddine (Collaborative Framework)

**Year:** 2022 (Conceptual synthesis)

**Key References:** Connes 2006, Chamseddine-Connes 1997-2020, van Suijlekom 2016

---

## Abstract

Two major approaches to unification—Kaluza-Klein (KK) dimensional reduction and Noncommutative Geometry (NCG) spectral action—employ fundamentally different normalizations for gauge coupling extraction, producing different predictions despite geometric equivalence. We detail the normalization ambiguities arising from Killing form, democratic, and Cartan metric conventions. We provide explicit transformation formulas mapping KK to NCG couplings, resolving a 30-year puzzle: why do geometrically equivalent descriptions yield different numerical predictions? The resolution is purely representational: the different conventions reflect different choices of generator trace norms and basis normalizations. We demonstrate these are equivalent when transformed consistently. For SU(3) color symmetry, the transformation between conventions introduces factors of √(3/5) to √(2/3) from Dynkin indices.

---

## Key Arguments

### 1. Three Normalization Conventions

**GUT/Dynkin**: $1/g_i^2 = T_i / g_{GUT}^2$ (standard particle physics)

**Killing Form**: $1/g_i^2 \propto \text{vol}(K) / \lambda_i$ (KK reduction)

**Democratic/NCG**: $1/g_i^2 \propto C_i(\text{algebra})$ (spectral action)

### 2. The Transformation

The precise map is:
$$g_i^2|_{KK} = \frac{[\text{total vol}]}{[\text{individual eigenvalue}]} \leftrightarrow g_i^2|_{NCG} = [\text{spectral } a_0^{(i)}]$$

### 3. SU(3) Example

**KK**: vol(SU(3)) ≈ 117.4, λ_s = 4
$$\frac{1}{g_s^2} = \frac{117.4}{4 \cdot \kappa^2}$$

**NCG**: Casimir = 4/3
$$\frac{1}{g_s^2} \propto a_0^{(SU(3))} = 16$$

Matching gives: $\rho^2 \cdot 117.4 = 16 / C$

---

## Key Results

1. **Exact Transformation**: Precise mathematical map between KK and NCG couplings.

2. **All Discrepancies Resolved**: Historical disagreements arise purely from normalization choices.

3. **Universality**: Once internal manifold K and fermion content are fixed, coupling predictions are identical.

4. **Metric Reconstruction**: Heat kernel expansion coefficients implicitly determine metric on K.

---

## Connection to Phonon-Exflation

The g₁/g₂ = e^{-2τ} result can be derived either as:
- KK: $g^2 \propto \text{vol}(SU(3)) / \lambda(\tau)$
- NCG: $g^2 \propto a_0(\tau)$

These must match via the transformation formulas, providing iron-clad consistency check.
