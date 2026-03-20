# Level Spacing Statistics in Integrable Quantum Systems: The Berry-Tabor Conjecture

**Author(s):** Michael V. Berry and Marek Tabor
**Year:** 1977
**Journal:** Proceedings of the Royal Society A, Vol. 356, p. 375
**Citation:** Often called the "Berry-Tabor conjecture" or "Berry-Tabor hypothesis"

---

## Abstract

Berry and Tabor made a complementary conjecture to the Bohigas-Giannoni-Schmit (BGS) result on chaotic systems. While BGS showed that chaotic quantum systems exhibit random-matrix-like level statistics, Berry and Tabor conjectured that **classically integrable systems** exhibit **Poisson-distributed level spacings** --- the opposite extreme.

For an integrable classical system (one with enough conserved quantities to be completely solvable), the quantum version should have eigenvalue spacings following:

```
P(s) = exp(-s)  (Poisson distribution)
```

where s is the normalized spacing. This means:
- No level repulsion (P(0) = 1)
- Uncorrelated spacings
- No anomalous spectral rigidity

The conjecture provided a complete dichotomy: **Chaos -> RMT statistics, Integrability -> Poisson statistics**.

---

## Historical Context

The 1977 Berry-Tabor conjecture was made just before the 1984 BGS paper on chaotic systems. Together, they established the fundamental connection between classical dynamics (chaos vs. integrability) and quantum spectral statistics.

The Berry-Tabor conjecture was more difficult to verify than BGS, because:

1. **Exact integrable systems are rare** in nature (most systems are generically chaotic)
2. **Integrable systems are more delicate** --- adding any perturbation destroys integrability
3. **Numerical verification is harder** --- quantum integrable systems are small (integrable billiards have integer or rational geometry)

By the 1990s-2000s, the Berry-Tabor conjecture had been rigorously proven for certain classes of systems (e.g., integrable billiards with rectangular/rational tables) but remains a conjecture for generic integrable systems.

---

## Key Arguments and Derivations

### Poisson Distribution for Integrable Systems

For an integrable classical system, the phase space is foliated by tori (KAM tori). Each torus carries conserved quantum numbers (action variables J_i), and the quantum energy levels are:

```
E_n1,n2,...,n_f = sum_i (omega_i * n_i) + quantum corrections
```

where omega_i = dE/dJ_i are the classical frequencies and f is the number of degrees of freedom.

The density of states is:

```
rho(E) ~ integral product dJ_i delta(E(J) - E)
```

For generic (non-resonant) frequency ratios omega_i/omega_j, this produces a uniform density of states with **no correlations** between nearby levels.

The nearest-neighbor spacing distribution becomes:

```
P(s) ~ Poisson(s) = exp(-s)
```

### Derivation via Weyl Formula

Berry and Tabor used the Weyl asymptotic formula:

```
N(E) ~ volume of phase space with E' < E
```

For an integrable system, this is a smooth function of E with no oscillations (unlike chaotic systems where periodic orbits cause oscillations). The level density is:

```
rho(E) = dN/dE ~ generic, non-oscillating function
```

With no long-range correlations built in, spacings appear Poisson.

### Nearest-Neighbor and Two-Level Correlations

The two-level correlation function for integrable systems should be:

```
R_2(omega) = 1  (no correlations)
```

This contrasts with chaotic systems where:

```
R_2(omega) = 1 - (sin(pi*omega)/(pi*omega))^2
```

The flat R_2 reflects the independence of energy spacings.

### Spectral Rigidity: Delta_3

For integrable systems, the spectral rigidity should follow:

```
Delta_3(L) ~ L  (linear in L)
```

reflecting that the spectrum has no long-range order beyond the mean density.

For chaotic (GOE) systems:

```
Delta_3(L) ~ (1/pi^2) * ln(L)
```

logarithmic (better than linear).

---

## Key Results

1. **Poisson Conjecture for Integrable Systems**: Classically integrable quantum systems should exhibit Poisson-distributed level spacings, the opposite of chaotic systems.

2. **No Level Repulsion**: Integrable spectra allow small spacings and even coincidences (degeneracies), unlike chaotic spectra where level repulsion suppresses P(0).

3. **Uncorrelated Spacings**: In the Poisson limit, spacings are statistically independent, reflecting the non-interacting nature of quantum tori.

4. **Linear Spectral Rigidity**: Delta_3(L) ~ L for integrable systems (vs. logarithmic for chaotic).

5. **Dichotomy Principle**: Classical integrability <= -> quantum Poisson; Classical chaos <- -> quantum RMT.

---

## Impact and Legacy

The Berry-Tabor conjecture became the basis for:

- **Spectral Classification**: Using level statistics to classify systems as chaotic or integrable
- **Localization Theory**: Understanding Anderson localization as an intermediate regime between Poisson and RMT
- **Integrable Systems Research**: Motivating study of exactly solvable quantum models (XXX spin chains, quantum KdV, etc.)
- **KAM Theory**: Rigorous proofs of KAM theorem motivating quantumversions (quantale chaos)

---

## Connection to Phonon-Exflation Framework

The **Berry-Tabor Poisson vs. RMT dichotomy** provides a crucial test for distinguishing integrable vs. chaotic instanton dynamics.

In Session 37, two regimes were identified:

1. **Near τ=0** (integrable BCS limit): gap ~ Delta_BCS ~ 0.3 au, few pair vibrations
2. **At fold** (van Hove singularity): gap opens at ~0.819 au, 85.5% of pair strength in single mode

**Berry-Tabor Test for S38**:

Compute level spacing distribution P(s) for:

1. **Pre-fold spectrum** (integrable BCS): should match Poisson
   ```
   P(s) ~ exp(-s)
   ```

2. **At-fold spectrum** (instanton gas): transitions toward RMT
   ```
   P(s) ~ s*exp(-pi*s^2/4)  (Wigner surmise, chaotic)
   ```

3. **Post-fold spectrum** (scrambled state): should plateau at RMT

The transition timescale from Poisson -> RMT would establish the **integrability-breaking timescale** of the instanton ensemble.

**Interpretation**: If the spectrum transitions Poisson -> RMT during fold crossing, then:
- The instanton gas **breaks integrability** of the bare BCS system
- The fold crossing is a **chaos-inducing transition**
- The timescale is the Berry-Tabor transition time, not spectral action relaxation

This directly tests whether the framework undergoes an **integrable-to-chaotic phase transition** during van Hove crossing.
