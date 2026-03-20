# The Spectral Action Principle

**Author(s):** Ali Chamseddine, Alain Connes
**Year:** 1997
**Journal:** Communications in Mathematical Physics, Vol. 186, pp. 731-750; arXiv:hep-th/9606001

---

## Abstract

We propose a new action principle for gravity coupled to gauge theories and matter, formulated in the language of noncommutative geometry. The action functional is defined as $S = \text{Trace}(\chi(D / \Lambda))$, where $D$ is the Dirac operator of a spectral triple and $\chi$ is a cutoff function at the scale $\Lambda$. When applied to the standard model, the spectral action automatically yields Einstein-Cartan gravity coupled to the electroweak and strong nuclear forces, along with a Higgs potential. Remarkably, the framework predicts relations between gauge coupling constants identical to those of SU(5) grand unification—achieved WITHOUT assuming grand unification a priori. The approach unifies particle physics and gravity geometrically, replacing the separate Lagrangians of the SM and general relativity with a single spectral functional.

---

## Historical Context

The Standard Model (SM) is phenomenologically successful but conceptually unsatisfying. It treats gravity (general relativity) and quantum fields (SM gauge theories, Higgs, fermions) as separate theories, glued together by hand. Why are there three separate gauge groups (SU(3) × SU(2) × U(1))? Why these specific coupling strengths? Why is there a Higgs potential with that particular shape?

In the 1990s, grand unified theories (GUTs) like SU(5) and SO(10) proposed that the three gauge groups unify at ultra-high energies (10^14 - 10^16 GeV). The coupling constants become equal at the unification scale, and some fermion multiplets merge (e.g., electron + right-handed neutrino into a 5-plet of SU(5)). However, GUTs introduce new problems: proton decay, the doublet-triplet Higgs splitting, and the hierarchy problem (why is the GUT scale so much higher than the weak scale?).

Connes and Chamseddine's 1997 proposal is radical: instead of unifying at high energy, unify in **geometry**. The SM and gravity are not separate theories but two manifestations of a single geometric structure—the spectrum of a Dirac operator on a noncommutative space. This paper establishes the framework and shows that:

1. The SM Lagrangian emerges from spectral geometry.
2. Einstein gravity emerges.
3. GUT-like coupling relations (sin²θ_W = 3/8) emerge WITHOUT assuming SU(5).

---

## Key Arguments and Derivations

### Spectral Triples and Noncommutative Geometry

A **spectral triple** is a triple $(\mathcal{A}, \mathcal{H}, \mathcal{D})$:
- **Algebra**: $\mathcal{A}$ is a unital *-algebra (C*-algebra) representing functions on the noncommutative space.
- **Hilbert space**: $\mathcal{H}$ is a Hilbert space where $\mathcal{A}$ acts.
- **Dirac operator**: $\mathcal{D}$ is a self-adjoint operator with compact resolvent, bounded commutators with elements of $\mathcal{A}$.

**Example**: For ordinary Riemannian manifolds, $\mathcal{A} = C^\infty(M)$ (smooth functions), $\mathcal{H} = L^2(S)$ (spinors), $\mathcal{D} = $ Dirac operator. The spectral triple is commutative.

**For noncommutative spaces**: Geometry is encoded in a spectral triple where $\mathcal{A}$ is noncommutative. The "space" has no points; only the spectrum of $\mathcal{D}$ matters.

### The Spectral Action

The action is defined as the **trace of the spectral density**:

$$ S[\mathcal{D}] = \text{Trace}(\chi(D / \Lambda)) $$

where:
- $\chi : \mathbb{R} \to \mathbb{R}$ is a cutoff function (e.g., $\chi(x) = \theta(1 - x)$, the Heaviside function, or a smooth approximation).
- $\Lambda$ is the UV cutoff scale (related to the Planck mass or compositeness scale).
- $\text{Trace}(\cdot)$ is the functional trace, summing contributions from all spectral modes $\lambda$ of $\mathcal{D}$: $\text{Trace}(\chi(D/\Lambda)) = \sum_{\lambda} \chi(\lambda / \Lambda)$.

This is geometrically natural: it is the simplest invariant one can write down from a Dirac operator. It does not require extraneous Lagrangian terms; it is the action, period.

### Application to the Standard Model

The authors define a spectral triple $(\mathcal{A}_\text{SM}, \mathcal{H}_\text{SM}, \mathcal{D}_\text{SM})$ encoding the SM:

**Algebra**:
$$\mathcal{A}_\text{SM} = C^\infty(\mathbb{R}^4) \otimes M_3(\mathbb{C})$$

where $M_3(\mathbb{C})$ is the algebra of 3 × 3 complex matrices (the internal symmetry space; the 3 colors of QCD). The 15 Weyl fermions per generation sit in the spinor representation, and gauge fields live in the off-diagonal components.

**Dirac operator**:
$$\mathcal{D} = \gamma^\mu (\partial_\mu + A_\mu) + M$$

where:
- $\gamma^\mu$ are Dirac matrices.
- $A_\mu$ is the gauge field 1-form.
- $M$ is the mass matrix (contains the Yukawa couplings and the Higgs field).

The mass matrix is NOT a separate input; it emerges as the **geometry of the finite space** (the 3 × 3 matrix structure of $M_3(\mathbb{C})$).

### Heat Kernel Expansion and the Seeley-DeWitt Coefficients

The spectrum is computed via the heat kernel. The trace $\text{Trace}(e^{-t D^2})$ is expanded in powers of $t$:

$$ \text{Trace}(e^{-t D^2}) = \sum_{k} a_k t^{(k - 4)/2} $$

For a 4D manifold, the leading terms are:

$$\text{Trace}(e^{-tD^2}) = a_0 + a_2 t + a_4 t^2 + \ldots$$

where:
- $a_0 \propto \int d^4 x \, \sqrt{g}$ (volume)
- $a_2 \propto \int d^4 x \sqrt{g} R$ (Ricci scalar, Einstein action)
- $a_4 \propto \int d^4 x \sqrt{g} (c_1 R^2 + c_2 R_{\mu\nu}^2 + c_3 F^2 + c_4 |\phi|^4 + \ldots)$ (higher-order invariants)

The spectral action is:

$$S = \int_0^\infty \frac{dt}{t} \phi(t) \text{Trace}(e^{-tD^2}) = \sum_k \phi_k a_k$$

where $\phi_k = \int_0^\infty \phi(t) t^{k/2} dt$ are moments of the cutoff function.

**Critical result**: When the Dirac operator is the SM Dirac operator (with gauge fields and Higgs), the $a_4$ coefficient contains:
1. Einstein-Cartan action
2. Yang-Mills action for all three gauge groups
3. Higgs potential
4. Fermionic Yukawa couplings

All in ONE term, derived from geometry alone.

### GUT-like Coupling Ratios

In the SM, the three coupling constants $g_1, g_2, g_3$ (hypercharge, weak, strong) are independent at low energy. However, the NCG spectral action predicts a relation.

From the $a_4$ coefficient, the Yang-Mills term is:

$$\text{Tr}(F_\mu^\nu F^{\mu\nu}) = \frac{1}{g_1^2} F_1^2 + \frac{1}{g_2^2} F_2^2 + \frac{1}{g_3^2} F_3^2 + \text{(mixing terms)}$$

The spectrum of the Dirac operator determines the ratios. The authors show:

$$\frac{g_1}{g_2} = \frac{g_2}{g_3} \text{ (approximately)} \quad \text{at the unification scale}$$

And the Weinberg angle:

$$\sin^2(\theta_W) = \frac{3}{8}$$

These are **identical to SU(5) grand unification** predictions, even though the spectral action never assumed SU(5). This is remarkable: the geometry of $M_3(\mathbb{C})$ automatically encodes the structure of GUT.

### Free Parameters and Falsifiability

The spectral action has several parameters:
1. The cutoff scale $\Lambda$ (related to the Planck mass or compositeness scale; the size of the finite geometry).
2. The test function $\chi$ (the shape of the UV cutoff).
3. The Yukawa matrix (the off-diagonal mass matrix $M$, which encodes how fermions couple to the Higgs).

However, these are NOT arbitrary:
- The Yukawa matrix must satisfy certain constraints to avoid anomalies (triangle diagrams that make the theory inconsistent).
- The cutoff scale is the only independent energy scale (beyond the geometry itself); all other scales (Higgs mass, W and Z masses, etc.) are derived from it.
- The test function $\chi$ can be any smooth cutoff; the physics is insensitive to its shape (as verified by the "uncanny precision" 2010 paper).

**Predictive power**: The framework makes very few predictions because most SM parameters (masses, couplings) can be absorbed into the Yukawa matrix and the cutoff scale. However, the coupling ratios (sin²θ_W = 3/8, GUT-like structure) are genuine predictions that can be tested.

---

## Key Results

1. **Spectral Action Defines Quantum Field Theory**: The trace $\text{Trace}(\chi(D/\Lambda))$ is sufficient to define a complete action for gravity plus the SM. No additional Lagrangian terms are needed.

2. **Einstein + SM from Geometry**: Expanding the spectral action in powers of the cutoff yields Einstein-Cartan gravity + Yang-Mills + Higgs + Fermions, all from a single geometric object (the Dirac operator).

3. **GUT-like Coupling Prediction**: The Weinberg angle is predicted as $\sin^2(\theta_W) = 3/8 \approx 0.375$, which matches SU(5) unification predictions but emerges from geometry, not from a high-energy unification scale.

4. **Parameter Reduction**: The SM has ~19 free parameters (three coupling constants, 6 quark masses, 3 lepton masses, 4 CKM angles, Higgs mass, Higgs coupling, cosmological constant). The spectral action reduces this to ~5 (the geometry, the cutoff scale, the test function).

5. **Falsifiability**: The framework makes a clear prediction (sin²θ_W = 3/8) that disagrees with the measured value (~0.231). This is either (a) evidence against the framework, or (b) evidence that quantum corrections (running of coupling constants) modify the tree-level prediction. The framework is falsifiable.

---

## Impact and Legacy

The 1997 spectral action paper is foundational. It established the geometric paradigm for unifying particle physics and gravity. Immediate impacts:

1. **Mathematical Development**: Spectral geometry became a major research area in mathematical physics. The spectral action principle is now the standard framework in noncommutative geometry.

2. **Phenomenological Refinement**: The 2010 "Uncanny Precision" paper (above) showed that tree-level predictions (sin²θ_W, Higgs potential) are numerically accurate but require quantum corrections to match experiment. This opened the door to iterative refinement.

3. **Criticisms and Challenges**:
   - The sin²θ_W = 3/8 prediction is 3.5 sigma away from experiment. This was addressed in later work (Chamseddine-Connes-Marcolli, 2013) by allowing additional geometric terms or running of couplings.
   - The framework requires specifying the finite geometry (the algebra $\mathcal{A}_\text{SM}$) by hand. Some critics argue this is as ad hoc as writing the SM Lagrangian directly.
   - The cosmological constant problem persists: the spectral action does NOT predict a small observed Lambda; instead, it predicts a huge Lambda from quantum loops (Sessions 36-37 of phonon-exflation project).

4. **Alternatives**: The spectral action inspired other attempts at geometric unification (Ashtekar's loop quantum gravity, twistor theory, causal set theory). None have achieved the same level of phenomenological contact.

---

## Connection to Phonon-Exflation Framework

**The 1997 spectral action paper is the FOUNDATION that phonon-exflation builds upon.**

Key connections:

1. **Geometric Unification**: Phonon-exflation adopts the core idea that gravity and particles unify in NCG. The Dirac spectrum encodes the SM quantum numbers and masses.

2. **The Finite Space is M4 x SU(3)**: The 1997 paper uses $C^\infty(\mathbb{R}^4) \otimes M_3(\mathbb{C})$. Phonon-exflation specifies this further: the finite space is the internal SU(3) geometry (the compactified extra dimensions), and the full space is M4 × (SU(3) quotient). The Kaluza-Klein modes are states in the SU(3) sector, with masses ~M_Planck.

3. **The Spectral Action as Cosmological Principle**: The 1997 paper treats the spectral action as a static action principle. Phonon-exflation reinterprets it: the spectral action is the energy landscape, and the dynamics of the system (expansion, cooling) is the flow along this landscape. The "now" is the current state in the landscape (e.g., tau = 0.15).

4. **Addressing sin²θ_W = 3/8 vs. 0.231**: Phonon-exflation proposes that the BCS instability on M4 x SU(3) runs the coupling constants, shifting the tree-level prediction (3/8) toward the measured value. The running is NOT the usual RG running but a geometric running induced by the vacuum structure (the gap).

5. **Sagan's Role**: The 1997 paper makes a falsifiable prediction (sin²θ_W = 3/8). Phonon-exflation modifies this by adding a quantum correction. Sagan asks: "Does the BCS correction actually move the prediction toward 0.231, or does it worsen the disagreement?" This is a concrete test of the framework.

**Empirical Status**: The 1997 spectral action is FOUNDATIONAL but INCOMPLETE. It predicts sin²θ_W incorrectly and does not address the cosmological constant. Phonon-exflation claims to fix both through BCS dynamics and quantum corrections, but these claims are not yet experimentally validated. The 1997 paper is thus a reference point: a prediction to test against (can we improve sin²θ_W?) and a framework to extend (can we add quantum dynamics?).

