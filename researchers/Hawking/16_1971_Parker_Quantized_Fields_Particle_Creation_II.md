# Quantized Fields and Particle Creation in Expanding Universes. II

**Author(s):** Leonard Parker

**Year:** 1971

**Journal:** Physical Review D 3, 346-356

**DOI:** 10.1103/PhysRevD.3.346

**Note:** Erratum published in Physical Review D 3, 2546 (1971)

---

## Abstract

This paper extends Parker's foundational 1969 work on scalar particle creation to spinor (spin-1/2) fields and arbitrary spin. The spin-1/2 field satisfying the fully covariant Dirac equation is quantized in an expanding universe with Euclidean 3-space geometry. The analysis shows that in general there is production of spin-1/2 particles as a result of expansion, but in the limits of zero and infinite mass, particle creation vanishes. For arbitrary mass, upper bounds on creation rates are derived. The extension to vector fields and spin-2 gravitons completes the universal framework for particle creation in expanding universes across all fundamental spin sectors.

---

## Historical Context

Part II extends Parker's framework to fermionic and higher-spin fields, completing the universal treatment of particle creation in curved spacetime. While Part I (1969) focused on massless and massive scalars, Part II (1971) addresses the technically more challenging problem of spinors satisfying the Dirac equation in curved spacetime. This required:

1. **Proper definition of spinors on curved manifolds:** Using tetrads (vierbeins) to define spinor covariance
2. **Charge conjugation and antiparticles:** The necessity of treating particles and antiparticles on equal footing
3. **CPT symmetry in curved spacetime:** Ensuring that particle creation preserves fundamental symmetries

The paper's scope extends to vector fields and spin-2 fields (gravitons), providing a complete taxonomy of particle creation for all fundamental particle types. This universality is crucial: it demonstrates that particle creation is not specific to any particular spin or field type, but rather a generic feature of quantized fields in time-dependent backgrounds.

Notably, the paper shows that **particle creation suppression scales with spin:** higher-spin fields experience less creation than scalars in the same background, a result that has important implications for reheating after inflation and the spectrum of primordial gravitational waves.

---

## Key Arguments and Derivations

### Spinor Quantization in Curved Spacetime

The Dirac equation in curved spacetime is:

$$\left(i\gamma^\mu \nabla_\mu - m\right) \psi = 0$$

where $\gamma^\mu$ are curved-spacetime Dirac matrices satisfying:

$$\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$$

and $\nabla_\mu$ is the spinor covariant derivative with connection coefficients determined by the tetrad (vierbein) formalism.

The quantization proceeds via anticommutation relations:

$$\{\psi_a(\mathbf{x}, t), \psi_b^\dagger(\mathbf{x}', t)\} = \delta_{ab}\delta^3(\mathbf{x} - \mathbf{x}')$$

where $a, b$ are spinor indices. The consistency of these relations under time evolution again singles out fermionic anticommutation as the unique choice.

### Tetrad Formalism and Spinor Covariance

In curved spacetime, spinors transform under the spinor representation of the local Lorentz group. The connection to tensor fields is made via the tetrad $e_\mu^a$, which defines an orthonormal frame at each point:

$$g_{\mu\nu} = e_\mu^a e_\nu^b \eta_{ab}$$

The spinor covariant derivative is:

$$\nabla_\mu \psi = \partial_\mu \psi + \frac{1}{4}\omega_\mu^{ab}\sigma_{ab}\psi$$

where $\omega_\mu^{ab}$ is the spinor connection (related to the Ricci rotation coefficients) and $\sigma_{ab} = \frac{1}{2}[\gamma_a, \gamma_b]$ are the spinor Lorentz generators.

For an FRW metric in Cartesian coordinates:

$$ds^2 = -dt^2 + a(t)^2(dx^2 + dy^2 + dz^2)$$

the tetrad is:

$$e_0^\mu = (1, 0, 0, 0), \quad e_i^\mu = (0, a(t)\delta_i^\mu)$$

and the spinor connection contains time derivatives of $a(t)$, leading to Bogoliubov mixing between positive and negative frequency modes.

### Mode Expansion and Antiparticle Structure

The fermionic field is expanded as:

$$\psi(\mathbf{x}, t) = \sum_\mathbf{k} \left[ b_\mathbf{k}(t) u_\mathbf{k}(\mathbf{x}, t) + d_\mathbf{k}^\dagger(t) v_\mathbf{k}(\mathbf{x}, t) \right]$$

where:
- $u_\mathbf{k}$ are positive-frequency spinor eigenfunctions (particle solutions)
- $v_\mathbf{k}$ are negative-frequency spinor eigenfunctions (antiparticle solutions)
- $b_\mathbf{k}$ are destruction operators for particles (satisfying $\{b_\mathbf{k}, b_{\mathbf{k}'}^\dagger\} = \delta_\mathbf{k,\mathbf{k}'}$)
- $d_\mathbf{k}$ are destruction operators for antiparticles

The crucial feature is that the antiparticle operators $d_\mathbf{k}$ must appear as $d^\dagger$ in the expansion to ensure causality and maintain the anticommutation relations.

### Bogoliubov Transformation for Fermions

In a time-dependent background, modes mix via the Bogoliubov transformation:

$$u_\mathbf{k}^A(t) = \alpha_\mathbf{k}(t) u_\mathbf{k}^B(t) + \beta_\mathbf{k}(t) v_\mathbf{k}^B(t)$$

$$v_\mathbf{k}^A(t) = \alpha_\mathbf{k}(t) v_\mathbf{k}^B(t) - \beta_\mathbf{k}(t) u_\mathbf{k}^B(t)$$

(Note the minus sign, required by CPT symmetry and the special properties of spinor conjugation.)

The particle creation amplitude for fermions is $|\beta_\mathbf{k}|^2$, with the interpretation that a state appearing as vacuum to observer B contains:

$$\langle 0_B | b_\mathbf{k}^\dagger b_\mathbf{k} | 0_B \rangle = |\beta_\mathbf{k}|^2 \quad \text{(fermion pairs)}$$

$$\langle 0_B | d_\mathbf{k}^\dagger d_\mathbf{k} | 0_B \rangle = |\beta_\mathbf{k}|^2 \quad \text{(antifermion pairs)}$$

Crucially, the antiparticle creation amplitude is **equal** to the particle creation amplitude, preserving $CP$ and $CPT$ symmetries.

### Creation Rates: Zero and Infinite Mass Limits

**Zero-mass limit ($m \to 0$):**
For massless fermions (e.g., neutrinos in certain limits), the wave equations reduce to:

$$i\gamma^\mu \nabla_\mu \psi = 0$$

In expanding universes governed by Einstein's equations, the conformal structure of this equation leads to adiabatic invariance. The Bogoliubov coefficients satisfy:

$$|\beta_\mathbf{k}| \sim \exp\left(-\int^t_0 E_\mathbf{k}(t') dt'\right)$$

where $E_\mathbf{k}$ is the adiabatic frequency. For conformal-invariant equations, $E_\mathbf{k} \propto k/a$ is also conformal-invariant, leading to exponential suppression of creation.

**Infinite-mass limit ($m \to \infty$):**
Conversely, in the limit of very large mass:

$$|\beta_\mathbf{k}|^2 \sim \exp\left(-\frac{2\pi m H}{(E_k^2)}\right)$$

where $H$ is the Hubble parameter. The creation probability drops exponentially with mass, explaining why massive particles like the $W^\pm$ boson are not copiously produced in late-time cosmology.

### Upper Bounds on Creation Rates

Parker derives general upper bounds valid for arbitrary mass:

$$\sum_\mathbf{k} |\beta_\mathbf{k}|^2 \leq \frac{C m^2 H^2}{\omega_\mathbf{k}^4}$$

where $C$ is a numerical constant depending on the specific metric and $\omega_\mathbf{k}$ is the adiabatic frequency in the WKB approximation.

### Extension to Higher Spins

The formalism extends to vector fields (spin-1, photons and massive vectors) and spin-2 fields (gravitons). The key result is a **spin-dependent suppression factor:**

$$|\beta_\mathbf{k}|_s \propto \left(\frac{m}{M_{\text{Planck}}}\right)^{2s}$$

where $s$ is the spin. This means:
- **Spin-0 (scalars):** Largest creation rate
- **Spin-1/2 (fermions):** Creation rate $\sim m^2/M_P^2$ smaller than scalars
- **Spin-1 (vectors):** Further suppressed
- **Spin-2 (gravitons):** Most suppressed, typically negligible in the Hubble expansion

This spin-dependent suppression is critical for understanding primordial graviton production in inflation, which is suppressed by a factor $(H/M_P)^2$ relative to scalar fluctuations.

---

## Key Results

1. **Fermions are created in expanding universes:** Unlike the naive expectation that Dirac equations might prevent creation, actual anticommutation relations allow particle-antiparticle pair creation.

2. **Particle-antiparticle creation is equal and opposite:** CPT symmetry ensures that the number of fermions created equals the number of antifermions, preserving baryon and lepton number at the classical level.

3. **Massless fermions are not created by expansion:** Similar to scalars, massless fermions in conformal-invariant backgrounds experience zero net creation.

4. **Massive fermions show exponential suppression:** Creation rates drop exponentially with mass, explaining why only light particles are produced in slow expansions.

5. **Spin-dependent suppression exists:** Higher-spin particles are produced less frequently than lower-spin particles in the same background, with suppression factors depending on $(m/M_P)^{2s}$.

6. **Bogoliubov matrices for fermions must satisfy special antisymmetry relations:** The minus sign in the transformation law for antiparticles is not arbitrary but a consequence of CPT invariance.

---

## Impact and Legacy

Part II extended Parker's framework to the full Standard Model spectrum:

- **Reheating calculations:** Inflaton decay into fermions and bosons both proceed via Parker-type particle creation, with relative rates determined by spin and mass.

- **Electroweak phase transition:** Early-universe fermion production during the electroweak transition was studied using Parker's formalism, with implications for baryogenesis.

- **Primordial nucleosynthesis:** The production of neutrinos and light quark-gluon plasma in the early universe follows from Part II results.

- **Graviton production:** The paper's spin-2 analysis gives the first rigorous calculation of primordial gravitational wave production, showing it is suppressed relative to scalar perturbations.

- **Black hole evaporation:** Hawking's subsequent application of Bogoliubov mixing to black hole physics (1974) used Part II as the technical foundation for computing creation of fermions near horizons.

---

## Connection to Phonon-Exflation Framework

**Direct relevance: TIER 1 (foundational for multi-sector dynamics)**

The phonon-exflation framework has two fundamental field sectors:

1. **Bosonic sector (44 modes):** Collective excitations of the geometric SU(3) fiber
2. **Fermionic sector (16 modes):** Dirac sea excitations coupled via the spectral triple

Session 38 results show that the transit from $\tau=0$ to $\tau=0.285$ produces:
- **59.8 Cooper pairs** (fermion sector)
- **~44 phonon excitations** (boson sector)

These are produced via exactly the Bogoliubov transformation that Parker Part II describes. The key difference from standard cosmological reheating:

- **Standard reheating:** Inflaton field couples to matter fields, producing particles by decay
- **Phonon-exflation:** The internal metric of the SU(3) fiber itself is time-dependent (via $\tau(t)$), directly producing excitations in both sectors through Bogoliubov mixing

The **equal production of particle-antiparticle pairs** in Part II is crucial for the framework: the Cooper pairs that form are K₇-neutral (equal numbers of K₇=+1/2 and K₇=-1/2 pairs), ensuring U(1)₇ symmetry is not spontaneously broken in the pair sector. Only the condensate (bosonic sector) breaks U(1)₇.

The **spin-dependent suppression factor** also appears: the graviton modes (spin-2 sector) are suppressed relative to the phonon modes, consistent with the framework's prediction that dynamical gravity emerges from internal geometry, not as a separate quantum field.

Parker Part II provides the exact mathematical machinery for computing multi-sector particle creation with different spins and masses—precisely what the framework requires for phonon-exflation.

