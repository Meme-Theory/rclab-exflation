# Spectral Noncommutative Geometry, Standard Model and all that

**Authors:** A. Devastato, M.A. Kurkov, Fedele Lizzi
**Year:** 2019
**arXiv:** 1906.09583v2
**Journal:** Lecture Notes in Physics / Conference Proceedings

---

## Abstract

Comprehensive review of spectral noncommutative geometry approach to the Standard Model. Covers mathematical foundations, bosonic and fermionic spectral actions, phenomenological predictions, and open problems. Discusses both Euclidean and Lorentzian formulations, fermion doubling, and how to go beyond the Standard Model within the spectral framework.

---

## Contents Overview

### Part I: Mathematical Foundations
- Spectral triples and Dirac operators
- Algebraic geometry of spectral spaces
- Heat kernel expansions and Seeley-DeWitt coefficients
- Connection between geometry and operator spectra

### Part II: Spectral Action Principle
- Classical and quantum aspects
- Fermionic action: $S_F = \langle \psi | D | \psi \rangle$
- Bosonic action: $S_B = \text{Tr}[\phi(D^2/\Lambda^2)]$ (cutoff version reviewed, with caveats from Paper 05)
- Zeta function regularization (Papers 01, 04) discussed as alternative

### Part III: Standard Model Application
- Almost commutative geometry: $C^\infty(M) \otimes \mathcal{A}_F$
- Fermion spectrum and Yukawa couplings from D_F matrix
- Higgs mechanism from spectral perspective
- Gauge bosons and their origins
- Neutrino masses and majorana terms

### Part IV: Phenomenology
- Higgs mass predictions (125-140 GeV range)
- Gauge coupling unification at spectral scale
- Cosmological constant and dark energy
- Running couplings and RG equations
- Proton stability constraints

### Part V: Beyond Standard Model
- Grand symmetry and Pati-Salam unification
- Extended scalar sector (from Paper 08)
- Constraints from electroweak precision tests
- LHC predictions and experimental status

### Part VI: Open Issues
- Lorentz signature (Wick rotation problems)
- Fermion doubling interpretation
- Quantum gravity aspects
- Connection to loop quantum gravity and causal sets

---

## Key Review Points

### 1. Unique Successes of Spectral Approach

**Predictive power**: Given only:
- Fermion masses (Yukawa couplings)
- Gauge group structure (matter representations)
- Spacetime dimension (4)

**The framework predicts**:
- Higgs mass (within 5-10% of observed 125 GeV)
- Electroweak scale and vev (v = 246 GeV)
- Gauge coupling magnitudes at unification
- Presence of neutrino Majorana masses

No other framework makes such predictions from geometric first principles.

### 2. Critical Limitations

**Lorentz signature problem**: The framework naturally lives in Euclidean spacetime (Wick rotation issues are non-trivial). Recovering physical Lorentzian signature requires additional structure (Paper 14: twisted spectral triples).

**Cosmological constant problem**: a₀/a₂ ratio is set by spectral geometry but does NOT match observations. The framework predicts Λ ~ 10¹²¹ Planck units; observed is ~ 10⁻¹²⁰. This is the "worst prediction in physics" (cosmological constant problem).

**Fermion doubling**: While Paper 08 reinterprets doubling as beneficial (extended scalars), it adds complexity. The interpretation (necessary vs. artifact) remains somewhat ambiguous.

### 3. Connection to Contemporary Physics

**Higgs portal dark matter**: New scalars from extended sector (Paper 08) can be dark matter candidates. The framework naturally couples them to Higgs.

**Inflation**: Dilaton-Higgs dynamics (Paper 04) have inflationary implications. However, the slow-roll parameters are not naturally small (problem for matching observations).

**Quantum gravity**: The framework is background-independent (no metric fixed a priori). This is conceptually closer to loop quantum gravity than string theory.

---

## Key Equations and Results

**Spectral action at unification scale**:
$$S_\text{total} = S_F + S_B = \langle \psi | D | \psi \rangle + \int d^4x \sqrt{g} \mathcal{L}_\text{spectral}$$

where $\mathcal{L}_\text{spectral}$ contains (from zeta formulation):
- Einstein-Hilbert term: $\frac{M_P^2}{16\pi} R$
- Yang-Mills: $(1/4) g_i^{-2} F_i^{\mu\nu} F_{i\mu\nu}$
- Higgs: $|D_\mu H|^2 + \lambda H^4 + \cdots$
- Yukawa: $y_t \bar{\psi}_L H \psi_R + \text{h.c.}$

**Unification condition** (automatic from spectral geometry):
$$g_1(\Lambda_U) = g_2(\Lambda_U) = g_3(\Lambda_U) / \sqrt{5/3}$$

at $\Lambda_U \sim 10^{16}$ GeV (not $10^{15}$ like SU(5)).

**Higgs mass formula** (spectral):
$$m_H^2 \propto (y_t^2 + y_b^2 + y_\tau^2) \times (\text{spectral factor})$$

---

## Impact and Legacy

Most comprehensive review to date of spectral NCG. Establishes:
1. Spectral action is **mathematically rigorous and conceptually coherent**
2. Phenomenology is **successful at unification scale** (coupling matching, Higgs mass ballpark)
3. **Open problems are well-defined**: Lorentz signature, CC, cosmology
4. **Experimental tests possible**: LHC searches for extended scalars, precision tests, proton decay limits

This review became the standard reference for physicists entering the field (2019 onwards).

---

## Connection to Phonon-Exflation

**Framework checklist**: The framework must address all items in this comprehensive review:

1. ✓ Does it have a well-defined Dirac operator D_K on M⁴ × SU(3)?
2. ✓ Does D_K have the correct spectrum (SM quantum numbers)?
3. ✓ Are Yukawa couplings derivable from D_K structure?
4. ✓ Is the extended scalar sector predicted by D_K determined?
5. ✓ What is the Lorentz signature structure (twisted spectral triple)?
6. ✗ How does cosmological constant emerge (CC problem)?
7. ✗ How does expansion dynamics work (inflation or alternative)?
8. ✗ How are dark matter and dark energy explained?

The framework addresses points 1-3 but is **incomplete on points 5-8**. This review clarifies what remains to be done.

**Critical gap**: The phonon-exflation program claims to solve the CC problem (point 6) by mapping it to a₀/a₂ ratio being a spectral quantity. But Devastato-Kurkov-Lizzi's comprehensive review shows this ratio still depends on regularization choice and cutoff scale. The framework must explain how it overcomes this.
