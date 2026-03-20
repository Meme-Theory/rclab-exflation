# A Fermion-Boson Composite Model of Quarks and Leptons

**Authors**: Koide Y.
**Year**: 1983 (original version 1982, Lett. Nuovo Cim. 34, 201)
**Journal**: Physics Letters B, vol. 120, pp. 161-165
**DOI**: 10.1016/0370-2693(83)90644-5
**Source**: https://en.wikipedia.org/wiki/Koide_formula

---

## Abstract

Koide proposes a composite (preon) model of quarks and leptons in which the charged lepton
masses are constrained by a simple algebraic relation. The model predicts that the ratio
$Q = (m_e + m_\mu + m_\tau) / (\sqrt{m_e} + \sqrt{m_\mu} + \sqrt{m_\tau})^2 = 2/3$
exactly. Using the known electron and muon masses, this formula predicts the tau mass with
remarkable accuracy, confirmed by later precision measurements.

---

## Historical Context

The "Koide formula" is one of the most striking unexplained numerical relations in particle
physics. First derived in 1981 and published in its mature form in 1983, it relates the
three charged lepton masses through a simple algebraic expression that holds to better
than 0.001% accuracy.

The formula emerged from a specific theoretical context -- a preon (composite) model of
quarks and leptons, popular in the early 1980s. While the preon model itself has been
ruled out (preon models generally predict excited states and compositeness signals not
observed at the LHC), the mass formula SURVIVES as a purely empirical relation. This is
a pattern familiar in physics: Balmer's formula for hydrogen spectral lines (1885) preceded
Bohr's model (1913) by 28 years. The formula was correct; the underlying mechanism was
unknown.

The Koide formula is directly relevant to Paasch's work because Paasch's Paper 03 cites it
as [2] and compares his own tau mass prediction with Koide's. Both frameworks predict the
tau mass from the electron and muon masses, but through completely different mechanisms:
Koide via an algebraic constraint on mass ratios, Paasch via integer mass numbers on a
logarithmic spiral.

---

## Key Arguments and Derivations

### The Koide Formula

The central result is the dimensionless ratio:

$$Q = \frac{m_e + m_\mu + m_\tau}{(\sqrt{m_e} + \sqrt{m_\mu} + \sqrt{m_\tau})^2} = \frac{2}{3}$$

### Mathematical Properties

The ratio $Q$ is bounded:

$$\frac{1}{3} \leq Q \leq 1$$

The lower bound $Q = 1/3$ is achieved when all three masses are equal ($m_e = m_\mu = m_\tau$).
The upper bound $Q = 1$ is achieved when only one mass is nonzero.

The observed value $Q = 2/3$ sits exactly at the MIDPOINT of the allowed range. This is a
highly non-generic value -- for three random positive numbers, $Q$ is uniformly distributed
on $[1/3, 1]$, so hitting the midpoint to 0.001% precision is a $\sim 10^{-5}$ coincidence
if accidental.

### Numerical Verification

Using current PDG mass values:
- $m_e = 0.510999$ MeV/c$^2$
- $m_\mu = 105.6584$ MeV/c$^2$
- $m_\tau = 1776.86$ MeV/c$^2$

Computing:
- Numerator: $m_e + m_\mu + m_\tau = 1883.03$ MeV/c$^2$
- $\sqrt{m_e} + \sqrt{m_\mu} + \sqrt{m_\tau} = 0.7149 + 10.279 + 42.153 = 53.147$
- Denominator: $(53.147)^2 = 2824.6$
- $Q = 1883.03 / 2824.6 = 0.666661$

Compare with $2/3 = 0.666667$. The discrepancy is $6 \times 10^{-6}$, or about **0.0009%**.

### Predictive Power

The formula's most impressive feature is its PREDICTIVE capacity. Using it to solve for
$m_\tau$ given $m_e$ and $m_\mu$:

Given $Q = 2/3$, the formula becomes:
$$m_e + m_\mu + m_\tau = \frac{2}{3}(\sqrt{m_e} + \sqrt{m_\mu} + \sqrt{m_\tau})^2$$

This is a quadratic equation in $\sqrt{m_\tau}$, yielding:

$$m_\tau^{\text{predicted}} = 1776.97 \text{ MeV/c}^2$$

**Timeline of validation:**
- 1982: Koide predicts $m_\tau = 1776.97$ MeV/c$^2$
- 1984: First precision measurement gives $1784.2 \pm 3.2$ MeV/c$^2$ (apparent discrepancy)
- 1992: Remeasurement gives $1776.99 \pm 0.28$ MeV/c$^2$ (spectacular agreement)
- 2024: Current best value $1776.86 \pm 0.12$ MeV/c$^2$ (agreement persists)

The 1992 remeasurement is one of the most dramatic validations of an empirical formula in
modern particle physics.

### Brannen's Trigonometric Form (2006)

Carl Brannen discovered that the Koide formula can be rewritten in trigonometric form:

$$m_k = \frac{M}{3}\left(1 + \sqrt{2}\cos\left(\frac{2\pi k}{3} + \delta\right)\right)^2, \quad k = 0,1,2$$

where $M = m_e + m_\mu + m_\tau$ and $\delta = 2/9$ radians. This form:
- Makes the $Z_3$ symmetry manifest (cyclic permutation of the three generations)
- Connects to $SU(3)$ flavor symmetry representations
- Suggests circulant mass matrix structure

### Theoretical Attempts

Multiple theoretical frameworks have attempted to derive the Koide formula:

1. **Preon models** (Koide's original): Ruled out experimentally
2. **Circulant mass matrices**: A $3 \times 3$ mass matrix invariant under cyclic permutations
   naturally produces $Q = 2/3$ if the eigenvalue constraint is imposed
3. **$S_3$ permutation symmetry**: The formula follows from demanding a specific breaking
   pattern of the permutation symmetry of three generations
4. **Waterfall mass matrices**: Koide (2005) showed that $Q = 2/3$ can arise from a specific
   seesaw-like mechanism
5. **Modular symmetry**: Recent work connects the formula to modular forms and finite groups

None of these explanations is considered definitive.

---

## Key Results

1. The Koide ratio $Q = (m_e + m_\mu + m_\tau)/(\sqrt{m_e} + \sqrt{m_\mu} + \sqrt{m_\tau})^2 = 2/3$
   holds to 0.001% accuracy
2. The formula successfully predicted $m_\tau = 1776.97$ MeV/c$^2$, confirmed in 1992
3. $Q = 2/3$ is the midpoint of the allowed range $[1/3, 1]$
4. The formula has a trigonometric reformulation with $Z_3$ structure and angle $\delta = 2/9$
5. Extensions to quarks yield mixed results (some triplets fit, others don't)
6. No universally accepted theoretical derivation exists
7. The formula remains one of the most precise unexplained numerical relations in particle
   physics

---

## Impact and Legacy

The Koide formula occupies a unique position in particle physics: universally acknowledged
as striking, yet widely suspected of being a coincidence. Its impact includes:

- Inspired decades of theoretical work on mass matrix textures
- Demonstrated that empirical mass relations CAN be predictive (the tau mass prediction)
- Motivated searches for similar relations among quarks (with limited success)
- Became a benchmark for any theory claiming to explain the fermion mass spectrum
- Featured in John Baez's mathematical physics blog as a "beautiful mystery"

The formula's survival over 40+ years of increasingly precise measurements makes the
coincidence hypothesis increasingly uncomfortable. As Baez notes: "There's no known reason
for this formula to be true!"

---

## Relevance to Paasch Framework

Paasch's Paper 03 cites Koide's formula as [2] and directly compares their tau mass
predictions. The connection is deep:

1. **Both predict $m_\tau$ from $m_e$ and $m_\mu$**: Koide via $Q = 2/3$, Paasch via
   integer mass numbers on a logarithmic spiral
2. **Both imply inter-generational algebraic structure**: Koide's $Z_3$ symmetry parallels
   Paasch's spiral periodicity across generations
3. **Both are "Kepler-stage" results**: Empirically precise formulas without dynamical
   derivation
4. **The $Z_3$ connection**: Koide's trigonometric form with $2\pi k/3$ structure mirrors
   the $Z_3 = (p-q) \mod 3$ triality labeling found in the Tier 1 Dirac spectrum
   computation (Session 17a, deliverable B-4)

The key question is whether Koide and Paasch are seeing the SAME underlying structure from
different angles, or whether their agreements are independent coincidences.

---

## Relevance to Phonon-Exflation Project

The Koide formula connects to the phonon-exflation framework in several ways:

1. **$Z_3$ triality**: The $Z_3$ structure in Koide's trigonometric form ($2\pi k/3$ phases)
   matches the $Z_3 = (p-q) \mod 3$ partition of SU(3) irreps found in Session 17a (B-4).
   If mass ratios emerge from the Dirac spectrum on deformed SU(3), the $Z_3$ structure
   would naturally appear.
2. **Circulant mass matrices**: The circulant structure underlying $Q = 2/3$ can arise from
   the representation theory of cyclic groups acting on the internal space -- exactly the
   kind of structure that the commutant analysis (Sessions 7-10) explored.
3. **Benchmark**: Any mass prediction from $V_{\text{eff}}(s_0)$ and the Tier 1 eigenvalue
   spectrum must be CONSISTENT with the Koide formula for charged leptons -- this is a
   non-trivial constraint on the framework.
