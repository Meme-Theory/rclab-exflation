# The Charge of an Electron

**Authors**: Eddington A.S.
**Year**: 1929
**Journal**: Proceedings of the Royal Society of London A, vol. 122, pp. 358-369
**DOI**: 10.1098/rspa.1929.0025
**Source**: https://royalsocietypublishing.org/doi/10.1098/rspa.1929.0025

---

## Abstract

Eddington argues that the fine structure constant $\alpha = e^2/(4\pi\epsilon_0\hbar c)$
can be determined by "pure deduction" from the algebraic structure of quantum mechanics.
He initially derives $\alpha^{-1} = 136$ from the number of independent components of a
symmetric tensor in Dirac's relativistic electron theory, later revising to
$\alpha^{-1} = 137$ to account for the exclusion principle. The argument represents the
most famous attempt to derive a fundamental constant from pure mathematics.

---

## Historical Context

Arthur Stanley Eddington (1882-1944) was one of the most prominent astrophysicists of the
early 20th century, famous for his 1919 solar eclipse expedition that confirmed Einstein's
General Relativity. By the late 1920s, he had turned his attention to an even more ambitious
project: deriving the fundamental constants of physics from pure mathematical reasoning.

The fine structure constant $\alpha \approx 1/137$ had been identified by Sommerfeld (1916)
in the context of the hydrogen atom's fine structure -- the small splitting of spectral lines
due to relativistic effects. By 1929, its value was known experimentally to be approximately
$\alpha^{-1} \approx 137.0$.

Eddington's attempt to derive this number was the first of its kind and set the pattern for
all subsequent "derivations" of $\alpha$ from first principles. The attempt is universally
regarded as a failure, but it raised a profound question that remains unanswered: IS $\alpha$
derivable from more fundamental principles, or is it a contingent parameter of our universe?

---

## Key Arguments and Derivations

### The Algebraic Argument for 136

Eddington's starting point is the Dirac equation for the relativistic electron:

$$(i\gamma^\mu \partial_\mu - m)\psi = 0$$

The four Dirac gamma matrices $\gamma^\mu$ ($\mu = 0,1,2,3$) satisfy the Clifford algebra:

$$\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$$

From four $4 \times 4$ gamma matrices, one can construct a basis for all $4 \times 4$
matrices using products of gamma matrices. The complete basis has $2^4 = 16$ elements:

- 1 scalar ($I$)
- 4 vectors ($\gamma^\mu$)
- 6 bivectors ($\gamma^\mu\gamma^\nu$, $\mu < \nu$)
- 4 pseudovectors ($\gamma^\mu\gamma^5$)
- 1 pseudoscalar ($\gamma^5$)

Total: 16 independent elements.

Eddington then considers a system of TWO electrons. The combined algebra involves products
of two sets of gamma matrices, generating a $16 \times 16 = 256$-dimensional algebra. But
Eddington argued that the PHYSICAL degrees of freedom are fewer, because some combinations
are equivalent under symmetry.

He counted the independent SYMMETRIC combinations of two-electron products and obtained:

$$N = \frac{16 \times 17}{2} = 136$$

(The formula $n(n+1)/2$ counts symmetric pairs.) Hence his initial claim: $\alpha^{-1} = 136$.

### The Revision to 137

When experiments showed $\alpha^{-1} \approx 137.0$ rather than 136, Eddington revised his
argument. He claimed that the exclusion principle (Pauli's principle for identical fermions)
introduces one additional degree of freedom -- an overall phase or sign that distinguishes
the two electrons as a system from two independent particles.

Thus:

$$\alpha^{-1} = 136 + 1 = 137$$

This "+1" correction was widely seen as ad hoc, and critics (including Pauli himself) were
not convinced.

### The Fundamental Theory (Posthumous, 1946)

Eddington spent the last decade of his life (1934-1944) developing an elaborate
"Fundamental Theory" that attempted to derive ALL fundamental constants from pure algebra.
Published posthumously in 1946, it claims to derive:

- The fine structure constant: $\alpha^{-1} = 137$
- The proton-electron mass ratio: $m_p/m_e = 1847.6$ (vs. experiment 1836.2)
- The Eddington number: $N = 136 \times 2^{256} \approx 1.575 \times 10^{79}$ (total number
  of protons in the universe)
- The cosmological constant

The theory was received with deep skepticism by the physics community. Eddington's
colleague E.A. Milne called it "speculative." Others were less polite.

### Why It Failed

Modern understanding identifies several fatal problems with Eddington's approach:

1. **$\alpha$ runs**: The fine structure constant is NOT a fixed number. It depends on the
   energy scale through the renormalization group: $\alpha(0) \approx 1/137.036$ but
   $\alpha(M_Z) \approx 1/128$. Any derivation of a fixed value ignores this running.

2. **$\alpha$ encodes all particles**: The measured low-energy value of $\alpha$ includes
   contributions from virtual loops of ALL charged particles (e, $\mu$, $\tau$, quarks).
   A derivation from electron algebra alone cannot capture these contributions.

3. **Electroweak mixing**: The elementary charge $e$ is not fundamental. It emerges from
   the electroweak couplings $g$ and $g'$ through $e = g\sin\theta_W$. Deriving $\alpha$
   requires understanding the ELECTROWEAK sector, not just electromagnetism.

4. **Ad hoc corrections**: The "+1" correction for the exclusion principle was not derived
   from any principle -- it was added to match experiment.

---

## Key Results

1. Eddington proposed $\alpha^{-1} = 136$ from the symmetric algebra of two Dirac electrons
2. Revised to $\alpha^{-1} = 137$ with an exclusion principle correction
3. The proton-electron mass ratio was "derived" as 1847.6 (actual: 1836.2, error 0.6%)
4. The Eddington number $N \approx 1.575 \times 10^{79}$ was proposed as the total number
   of particles in the universe
5. The approach is universally considered a failure, but the QUESTION it raised (is $\alpha$
   derivable?) remains open
6. The "+1" correction is considered ad hoc
7. Modern understanding of renormalization group running makes any fixed-value derivation
   suspect

---

## Impact and Legacy

Despite its failure, Eddington's program had lasting impact:

**Positive legacy:**
- Established the question of whether fundamental constants are derivable or contingent
- Inspired subsequent derivation attempts (Wyler 1969, Atiyah 2018, and many others)
- Connected the fine structure constant to the algebraic structure of quantum mechanics
  (specifically Clifford algebras and Dirac theory)
- The Eddington number connected microphysics to cosmology, anticipating Dirac's LNH (1937)

**Cautionary legacy:**
- Became the canonical example of numerological physics
- The phrase "Eddington's number" is sometimes used pejoratively for spurious derivations
- Pauli famously mocked Eddington's approach
- Modern physicists (including Sean Carroll) cite Eddington as a warning against deriving
  constants from counting exercises

**The open question:**
The SM has 25+ free parameters. If the landscape/multiverse picture is correct, these are
environmentally selected. If a deeper theory exists (string theory, NCG, etc.), some or all
of these parameters should be derivable. The question Eddington raised -- derivable or
contingent? -- is the question that modern theoretical physics is still trying to answer.

---

## Relevance to Paasch Framework

Paasch's Paper 04 (2016) "Derivation of the Fine Structure Constant" is squarely in the
Eddington tradition. The connections and contrasts are:

1. **Both derive $\alpha$ from algebra**: Eddington uses Clifford algebra (gamma matrices),
   Paasch uses his mass number scheme and golden ratio
2. **Both face the running objection**: $\alpha$ runs with energy, so any derivation of a
   fixed value must specify at which scale it applies
3. **Eddington's specific numerical approach failed**: His 136+1 counting is not physically
   justified
4. **Paasch's approach is different**: Paasch connects $\alpha$ to the golden ratio and mass
   numbers, not to Clifford algebra dimensions. This is a different strategy but faces
   similar objections about renormalization group running.

The Eddington example serves as both PRECEDENT (it's legitimate to ask if $\alpha$ is
derivable) and CAUTIONARY TALE (simple counting arguments are insufficient; the physics of
$\alpha$ involves all of the electroweak sector and all charged particles).

---

## Relevance to Phonon-Exflation Project

The phonon-exflation framework approaches the derivation of $\alpha$ through a completely
different route than either Eddington or Paasch:

1. **Spectral action**: In Connes' NCG, gauge coupling constants emerge as coefficients
   in the spectral action expansion. The fine structure constant would be determined by
   the spectrum of the Dirac operator $D_K$ on the internal space.

2. **Geometry not counting**: The phonon-exflation framework would derive $\alpha$ from the
   GEOMETRY of the deformed SU(3), not from counting algebraic elements. This automatically
   incorporates the correct gauge group structure (electroweak mixing via $g_1/g_2 = e^{-2s}$,
   derived in Session 17a).

3. **Running from V_eff**: The spectral action naturally produces coupling constants that
   run with energy (the UV cutoff $\Lambda$ in the spectral action plays the role of the
   renormalization scale). This addresses the main objection to Eddington's approach.

4. **KO-dimension 6**: The algebraic structure that determines $\alpha$ in the NCG
   framework is the KO-dimension = 6 spectral triple (Session 8), which is far richer than
   Eddington's simple gamma matrix counting.
