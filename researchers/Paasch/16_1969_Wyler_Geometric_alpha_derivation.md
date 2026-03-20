# L'espace symetrique du groupe des equations de Maxwell
# (The Symmetric Space of the Maxwell Equations Group)

**Authors**: Wyler A.
**Year**: 1969
**Journal**: Comptes Rendus de l'Academie des Sciences Paris, Serie A-B, vol. 269, pp. A743-A745
**Source**: https://mathworld.wolfram.com/WylersConstant.html

---

## Abstract

Wyler proposes a geometric derivation of the fine structure constant from the theory of
symmetric spaces. By analyzing the symmetric space associated with the conformal group of
Maxwell's equations, he obtains a specific numerical expression:

$$\alpha_W = \frac{9}{8\pi^4}\left(\frac{\pi^5}{2^4 \cdot 5!}\right)^{1/4} = \frac{1}{137.0360824\ldots}$$

This agrees with the experimentally measured fine structure constant to within $\pm 1.5$ ppm,
making it one of the most numerically accurate derivation attempts in the history of physics.

---

## Historical Context

Armand Wyler (1939-) was a Swiss mathematician working at the Institute for Advanced Study
in Princeton when he published this remarkable result in 1969. His approach was entirely
different from Eddington's algebraic counting: rather than counting degrees of freedom,
Wyler computed a GEOMETRIC invariant of the symmetric space associated with the symmetry
group of electromagnetism.

The paper created a sensation in the physics community. It was discussed in a 1971 article
in Physics Today, prompting wider interest. Robertson (1971) analyzed the result in Physical
Review Letters, noting that while the derivation contained questionable steps, the numerical
agreement was striking. Adler (1972) provided the most memorable assessment, calling it
"a number in search of a theory."

Wyler published a follow-up paper in 1971 ("Les groupes des potentiels de Coulomb et de
Yukawa"), extending his approach to other coupling constants. However, the extensions were
less successful, and the work did not lead to a complete theory.

Despite its controversial status, Wyler's constant remains the MOST ACCURATE formula for
$\alpha$ from any geometric or algebraic derivation attempt.

---

## Key Arguments and Derivations

### Symmetric Spaces and Group Theory

A symmetric space is a Riemannian manifold $M = G/K$ where $G$ is a Lie group and $K$ is
the stabilizer of a point. Symmetric spaces have the special property that every point has
an involutive isometry (a "mirror symmetry"), and their geometry is completely determined by
the Lie algebra of $G$.

Wyler's argument involves the following chain of mathematical structures:

**Step 1: The conformal group of Maxwell's equations**

Maxwell's equations in vacuum are invariant under the conformal group $SO(4,2)$, which is
larger than the Poincare group $ISO(3,1)$. The conformal group includes:
- Lorentz transformations ($SO(3,1)$)
- Translations ($\mathbb{R}^4$)
- Dilations (scale transformations)
- Special conformal transformations (inversions)

**Step 2: The associated symmetric space**

The relevant symmetric space is:

$$D_5 = SO(5,2) / (SO(5) \times SO(2))$$

This is a bounded symmetric domain of type IV (in Cartan's classification), embedded in
$\mathbb{C}^5$. It has complex dimension 5 and real dimension 10.

**Step 3: The volume computation**

Wyler computes the ratio of two volumes associated with this symmetric space:

- The volume of the Shilov boundary $\hat{D}_5$ (a compact manifold that forms the
  "boundary" of the bounded domain)
- A normalization volume related to the group structure

The key formula involves the ratio:

$$\alpha_W = \frac{9}{8\pi^4} \cdot V(\hat{D}_5)^{1/4}$$

where

$$V(\hat{D}_5) = \frac{\pi^5}{2^4 \cdot 5!} = \frac{\pi^5}{1920}$$

is the volume of the Shilov boundary of $D_5$.

### The Numerical Computation

Substituting:

$$\alpha_W = \frac{9}{8\pi^4}\left(\frac{\pi^5}{1920}\right)^{1/4}$$

$$= \frac{9}{8\pi^4} \cdot \frac{\pi^{5/4}}{(1920)^{1/4}}$$

$$= \frac{9\pi^{5/4}}{8\pi^4 \cdot (1920)^{1/4}}$$

$$= \frac{9}{8\pi^{11/4} \cdot (1920)^{1/4}}$$

Numerically:

$$\alpha_W = 0.00729735253\ldots = \frac{1}{137.0360824\ldots}$$

Compare with the modern experimental value:

$$\alpha_{exp} = 0.0072973525693(11) = \frac{1}{137.035999084(51)}$$

The agreement:

$$\frac{|\alpha_W - \alpha_{exp}|}{\alpha_{exp}} \approx 6.1 \times 10^{-7} \approx 0.6 \text{ ppm}$$

This is a sub-ppm match. (Note: older sources cite ~1.1 ppm based on less precise 1970s-era $\alpha$ measurements.)

### Questionable Steps

Robertson (1971) and subsequent critics identified several weak points in Wyler's derivation:

1. **Why $D_5$?** The choice of the specific symmetric domain $D_5$ is motivated by the
   conformal group, but the connection to the COUPLING CONSTANT (rather than, say, the
   group volume or some other invariant) is not rigorously justified.

2. **Why the Shilov boundary?** The Shilov boundary is a specific compact submanifold of
   the boundary of a bounded domain. Its use is mathematically natural but physically
   unmotivated.

3. **Why the 1/4 power?** The fourth root of the boundary volume appears without clear
   physical justification.

4. **Missing dynamics**: There is no Lagrangian, no equation of motion, no quantization
   procedure. The formula comes from pure geometry without a dynamical framework.

---

## Key Results

1. $\alpha_W = (9/8\pi^4)(\pi^5/(2^4 \cdot 5!))^{1/4} = 1/137.0360824\ldots$
2. Agreement with experiment: ~0.6 ppm vs CODATA 2018 $\alpha$ (~1.1 ppm vs 1970s-era measurements)
3. The formula involves the symmetric space $D_5 = SO(5,2)/(SO(5) \times SO(2))$
4. The volume of the Shilov boundary of $D_5$ enters through a fourth root
5. The derivation uses the conformal group of Maxwell's equations
6. No dynamical framework is provided
7. Extensions to other coupling constants (1971) were less successful
8. The formula has been called "a number in search of a theory" (Adler 1972)

---

## Impact and Legacy

Wyler's formula occupies a unique place in the history of physics:

**The positive view:**
- Most numerically accurate "derivation" of $\alpha$ ever produced
- Uses legitimate mathematical structures (symmetric spaces, conformal groups)
- The conformal group IS the symmetry group of Maxwell's equations
- Inspired subsequent geometric approaches to coupling constants
- Robertson (1971): "appears to have better chances to be derived from a theory than any
  of the other numbers that also agree with experiment"

**The negative view:**
- No physical mechanism connects symmetric space volumes to coupling constants
- The specific steps (choice of domain, Shilov boundary, 1/4 power) are ad hoc
- Extensions to other couplings don't work as well
- Adler (1972): "whether the agreement has a basis in physics, or is purely fortuitous,
  remains completely open"
- Modern renormalization group understanding makes a fixed-value derivation suspect

**Modern status:**
Wyler's formula has neither been derived from a complete physical theory nor definitively
refuted as coincidental. It remains in the liminal space of "suggestive but unproven" --
much like Paasch's mass numbers.

---

## Relevance to Paasch Framework

Wyler's derivation is directly relevant to evaluating Paasch's Paper 04 (derivation of the
fine structure constant):

1. **Historical parallel**: Both Wyler and Paasch claim to derive $\alpha$ from mathematical
   structures. Wyler uses symmetric space geometry; Paasch uses mass numbers and the golden
   ratio. Both face the same fundamental criticism (no dynamical derivation).

2. **Numerical accuracy**: Wyler's formula matches $\alpha$ to ~0.6 ppm (CODATA 2018). Paasch's
   match (~0.9 ppm) is comparable but slightly less accurate. Both are noteworthy.

3. **Geometric origin**: Wyler's approach is explicitly geometric (symmetric spaces of Lie
   groups). This connects naturally to the phonon-exflation framework, where coupling
   constants emerge from the GEOMETRY of the internal space.

4. **The same open question**: Both Wyler and Paasch face the same fundamental question --
   is the numerical agreement physics or coincidence? The answer requires a DYNAMICAL
   framework that PREDICTS the formula from first principles.

---

## Relevance to Phonon-Exflation Project

Wyler's approach has deep connections to the phonon-exflation framework:

1. **Symmetric spaces and NCG**: The symmetric space $G/K$ structure that Wyler uses is
   closely related to the homogeneous space $SU(3)/U(1) \times SU(2)$ that appears in the
   phonon-exflation framework. Both are analyzing the geometry of Lie group quotients.

2. **Conformal group and spectral action**: In Connes' NCG framework, the spectral action
   naturally produces gauge coupling constants from the Dirac spectrum. Wyler's conformal
   group approach may be a SPECIAL CASE of the spectral action computation restricted to
   the electromagnetic sector.

3. **Volume ratios**: Wyler computes a RATIO OF VOLUMES of geometric objects. The spectral
   action computes $\text{Tr}(f(D^2/\Lambda^2))$, which is also a sum over eigenvalues
   weighted by a geometric function. These may be mathematically related.

4. **Potential unification**: If the phonon-exflation framework's $V_{\text{eff}}(s_0)$
   determines the deformation parameter, and the gauge couplings at $s_0$ are given by
   $g_1/g_2 = e^{-2s_0}$, then $\alpha$ would be derived from geometry. The question is
   whether this geometric derivation reproduces Wyler's formula as a special case.
