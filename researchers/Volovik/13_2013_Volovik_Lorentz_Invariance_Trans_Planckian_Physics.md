# Lorentz Invariance Without Trans-Planckian Physics?

**Author(s):** Grigory E. Volovik
**Year:** 2013
**Journal:** Physics Letters B, 718(1), 93-97
**arXiv:** 1303.1914

---

## Abstract

This paper addresses a fundamental paradox in quantum gravity: How can low-energy physics exhibit perfect Lorentz invariance when the microscopic (trans-Planckian) physics is Galilean and fundamentally different? The paper demonstrates that:

- **Lorentz invariance emerges near gapless fermion nodes** (Dirac/Weyl points) in the spectrum, as a consequence of the linearized dispersion relation and isotropy symmetries.

- **Trans-Planckian physics is invisible to low-energy observers**: The effective low-energy theory depends only on topological invariants and symmetries near the Fermi point, not on microscopic details of the dispersion relation at high energy.

- **Superfluid and condensed matter models with Galilean microscopy naturally produce relativistic effective theories**: The cross-over from Galilean (high-energy) to Lorentzian (low-energy) dynamics is automatic for systems with gapless fermionic excitations.

- **CPT, Lorentz, and gauge symmetries are all emergent**: They are not fundamental, but arise at low energy from the topological structure of the vacuum.

- **Testable predictions for Lorentz violation searches**: The framework predicts that any Lorentz violation should be exponentially suppressed (or absent) at low energy, consistent with current experimental bounds ($\Delta v/c < 10^{-18}$).

The paper resolves the "trans-Planckian problem" by showing that it is not a problem — low-energy physics is robustly decoupled from trans-Planckian details.

---

## Historical Context

### The Trans-Planckian Problem

High-energy physics faces a fundamental difficulty:

1. **Planck scale**: $E_P = \sqrt{\hbar c^5 / G} \approx 1.22 \times 10^{19}$ GeV corresponds to length $\ell_P \approx 1.6 \times 10^{-35}$ m.

2. **Experimental reach**: Current experiments (LHC) probe energies $\sim 10$ TeV $\approx 10^{-3} E_P$, leaving a gap of 16 orders of magnitude.

3. **Effective field theory**: EFT assumes that low-energy physics is insensitive to UV (high-energy) physics. But quantum gravity effects accumulate, potentially violating this assumption.

4. **Unknown physics at Planck scale**: We have no direct knowledge of microscopic physics at $E \sim E_P$. Yet some frameworks (string theory, LQG) require precise knowledge of this regime.

### Lorentz Invariance Violation Searches

Motivated by quantum gravity considerations, several research programs search for tiny violations of Lorentz symmetry:

- **GRB time delays**: Photons of different energies traveling from distant gamma-ray bursts should arrive at different times if Lorentz invariance is violated at high energy. Observations constrain the effect to $\Delta E / E_P < 10^{-18}$.

- **Neutrino oscillations**: CPT and Lorentz violation would modify oscillation probabilities. Super-Kamiokande and other experiments constrain the effect.

- **Atomic spectroscopy**: Precision tests of the fine structure constant, muon g-2, and other atomic properties constrain Lorentz violation to parts per $10^{21}$.

All current bounds are consistent with exact Lorentz invariance.

### Volovik's Resolution

The paradox is: How is Lorentz invariance so precise if it emerges from Galilean microscopy?

Volovik's answer: **It's not a paradox. Emergence is precisely the reason Lorentz invariance is so stable.** The robust topological structure protects it.

---

## Key Arguments and Derivations

### Part I: Emergent Lorentz Invariance from Fermi Points

#### Linearization Near Fermi Points

In a quantum liquid (superfluid, Fermi gas, lattice model), the single-particle Hamiltonian is:

$$H_{sp}({\bf k}) = \epsilon_{\mathbf{k}} = \frac{k^2}{2m} + V({\bf k}) + \ldots$$

The microscopic dispersion (kinetic term $k^2 / 2m$) is **Galilean**, not relativistic.

However, if the Hamiltonian has gapless excitations at momentum ${\bf k}_0$, expand around this point:

$$H({\bf k}) = H({\bf k}_0) + \mathbf{v}_F \cdot ({\bf k} - {\bf k}_0) + \frac{1}{2m^*} ({\bf k} - {\bf k}_0)^2 + \ldots$$

where $\mathbf{v}_F = \nabla H / \hbar |_{{\bf k}_0}$ is the Fermi velocity and the quadratic term is subleading.

To lowest order (linear in ${\bf k} - {\bf k}_0$):

$$H({\bf k}) \approx \mathbf{v}_F \cdot ({\bf k} - {\bf k}_0)$$

This is the **Dirac equation** with $\mathbf{v}_F \to c$ and ${\bf k} \to \mathbf{p} / \hbar$.

Crucially: the Lorentz-invariant form emerges automatically because:
1. The dispersion is linearized near the gap node.
2. Rotational symmetry (assumed for isotropic fermions) forces $|\mathbf{v}_F|$ to be independent of direction.

#### Robustness to Microscopic Details

The coefficient $\mathbf{v}_F$ is determined by the microscopic Hamiltonian. For a Fermi surface in 3D, $v_F \sim k_F / m$ (Fermi velocity). This is a microscopic parameter.

But the **shape** of the low-energy spectrum (linear, relativistic) depends only on the fact that there is a gapless node, not on the specific microscopic potential $V({\bf k})$ or the form of the kinetic energy.

Thus, perturbations that deform $V({\bf k})$ or the kinetic energy without closing the gap node cannot destroy the Lorentz-invariant form. The relativistic dispersion is **topologically protected**.

#### Renormalization Group Flow

In many systems, the Fermi velocity renormalizes as we flow to lower energy scales. For a system with Galilean microscopy but relativistic low-energy effective theory:

$$v_F(\mu) = v_F^0 - \beta_1 \ln(\mu / \mu_0) + \ldots$$

where $\beta_1$ is the beta function (depends on interactions and dimensionality).

However, the **functional form** $E \propto v_F(\mu) |\mathbf{k}|$ remains unchanged. Only the coefficient $v_F(\mu)$ changes. Thus, Lorentz invariance (as a symmetry of the spectrum) survives RG flow.

### Part II: Trans-Planckian Insensitivity

#### What Changes at High Energy?

At energy scales comparable to or exceeding the microscopic scale (the analog of the Planck scale), the dispersion becomes non-linear:

$$E({\bf k}) = \sqrt{(v_F k)^2 + (\Delta k^2 / 2m)^2} \quad \text{for } k \gtrsim k_0$$

where the second term (quadratic, Galilean) becomes comparable to the first (linear, relativistic).

Processes at these high energies violate Lorentz invariance — particles no longer obey $E = pc$.

However, these high-energy processes are **invisible to low-energy observers**. Here's why:

1. **Energy conservation**: A low-energy observer measures only energy $E < E_{trans-Planckian}$. High-energy modes are virtual (short-lived).

2. **Decoupling theorem**: In EFT, vertices coupling high-energy and low-energy modes are suppressed by powers of $E_{trans-Planckian}^{-n}$.

3. **Topological protection**: Topological invariants (winding numbers, Chern numbers) ensure that the gap node structure is stable against high-energy deformations that respect protecting symmetries.

#### Explicit Example: Lattice Fermi Liquid

Consider fermions on a 3D cubic lattice with hopping $-t$ between nearest neighbors:

$$H = -t \sum_{\langle i,j \rangle} c_i^\dagger c_j + U \sum_i n_i (n_i - 1) / 2 + \mu \sum_i n_i$$

At the Fermi surface (with $\mu$ chosen appropriately), the dispersion is:

$$E_{\bf k} = -2t (\cos k_x + \cos k_y + \cos k_z) - \mu$$

Near $\mathbf{k} = 0$:

$$E_{\bf k} \approx -6t + t(k_x^2 + k_y^2 + k_z^2) - \mu$$

This is **quadratic** (Galilean) — not linear!

But at the edge of the Brillouin zone (e.g., $\mathbf{k} = (\pi, 0, 0)$), the dispersion can be linearized:

$$E_{\bf k} \approx 2t (\pi - |\mathbf{k} - (\pi, 0, 0)|)$$

A gapless fermion node at $\mathbf{k} = (\pi, 0, 0)$ with **linear** dispersion naturally emerges.

The full lattice dispersion has both the nonlinear Galilean form (micro-scale) and the emergent linear Lorentzian form (low-energy).

**A low-energy observer near the Fermi point sees Lorentz invariance; a high-energy observer sees the lattice.**

### Part III: CPT and Gauge Symmetries are Also Emergent

#### CPT Symmetry

The CPT theorem (Lüders, Pauli, 1954) states that any local, Lorentz-invariant QFT conserves CPT. But if Lorentz invariance emerges, so must CPT.

In the BCS/Bogoliubov framework, the particle-hole transformation:

$$c_k \to c_k^\dagger, \quad c_k^\dagger \to -c_k$$

swaps particles and holes. This is an emergent symmetry that protects the spectral properties near the Fermi surface.

For a general superfluid with order parameter $\Delta_k$, the Bogoliubov Hamiltonian is:

$$H_{Bog} = \sum_k \xi_k (c_k^\dagger c_k) + \frac{1}{2} (\Delta_k c_k^\dagger c_{-k}^\dagger + \text{h.c.})$$

The CPT transformation (particle-hole + hermitian conjugate) exchanges the two terms, leaving the spectrum invariant. This is **exact** at the microscopic level, independent of the details of $\Delta_k$.

Thus, CPT is protected by the underlying particle-hole symmetry of the condensate.

#### Gauge Symmetries

The U(1) gauge symmetry of electromagnetism (the photon) emerges from the phase of the condensate:

$$\Delta_k = |\Delta| e^{i\theta({\bf r})}$$

A local phase rotation $\theta({\bf r}) \to \theta({\bf r}) + \alpha({\bf r})$ requires a compensating gauge field:

$$\mathbf{A}({\bf r}) \to \mathbf{A}({\bf r}) + \nabla \alpha({\bf r})$$

to preserve the equation of motion. This is the emergence of the photon and U(1) gauge invariance.

Similarly, non-abelian gauge symmetries (SU(2), SU(3)) can emerge from the textures and fluctuations of more complex condensates.

### Part IV: Implications for Lorentz Violation Searches

#### Suppression of Lorentz Violation

If Lorentz invariance emerges from a topologically protected structure at low energy, then Lorentz violations are suppressed by the UV scale:

$$\Delta v / c \sim \left( \frac{E_{low}}{E_{trans-Planckian}} \right)^n$$

where $n \geq 1$ is an exponent depending on the coupling and dimension.

For typical models:
- $E_{low} \sim 1$ GeV (scale of particle physics)
- $E_{trans-Planckian} \sim E_P \approx 10^{19}$ GeV

Thus:

$$\Delta v / c \sim 10^{-19} \text{ to } 10^{-60}$$

depending on $n$. This is far below current observational bounds ($\Delta v / c < 10^{-18}$).

**The framework predicts that Lorentz violation, if it exists, is unobservably small.**

#### Alternative: Exact Lorentz Invariance

If the microscopic system has a symmetry that **exactly** protects Lorentz invariance (not just approximately), then there is no violation at any scale.

Volovik argues that superfluid vacuum may be such a system: the particle-hole symmetry and topological protection may enforce **exact** Lorentz invariance at all energies (up to the UV cutoff of the theory).

---

## Key Results

1. **Lorentz invariance emerges near gapless Fermi points**: The linearized dispersion relation, protected by topology, naturally produces relativistic kinematics.

2. **Emergence explains its robustness**: Because Lorentz symmetry depends only on topological structure, not microscopic details, it is stable against perturbations.

3. **Trans-Planckian physics decouples automatically**: Effective field theory naturally suppresses high-energy contributions; topological protection ensures low-energy theory is independent of UV details.

4. **CPT and gauge symmetries are emergent too**: Particle-hole symmetry (CPT) and condensate textures (gauge fields) give rise to fundamental symmetries.

5. **Lorentz violation is suppressed exponentially**: If Lorentz invariance emerges, any violation is suppressed by powers of the low-energy / trans-Planckian energy ratio, consistent with observations.

6. **No mysterious fine-tuning needed**: Contrary to conventional wisdom, Lorentz invariance's precision is explained by emergence, not coincidence.

---

## Impact and Legacy

This 2013 paper synthesized decades of Volovik's work on emergent gravity and symmetries. It influenced:

- **Effective field theory perspective**: Recognizing that emergent Lorentz invariance is the norm in quantum systems with gapless excitations.

- **Quantum simulation**: Using ultracold atoms and condensates to simulate relativistic QFT with controllable Lorentz violation (e.g., by tuning lattice parameters).

- **Swampland program**: Understanding which low-energy EFTs can emerge from UV-complete theories (like superfluid QCD or string theory).

- **Lorentz violation searches**: Interpreting experimental bounds not as constraints on fundamental physics, but as precision tests of the emergence mechanism.

---

## Connection to Phonon-Exflation Framework

This paper is central to phonon-exflation's consistency:

1. **Exact Lorentz invariance is natural**: The BCS condensate on SU(3) should exhibit exact (or nearly exact) Lorentz invariance at low energy, emerging from the particle-hole structure. No fine-tuning.

2. **No trans-Planckian problem**: The Planck scale (compactification scale of SU(3)) is Galilean and unknown; low-energy particle physics depends only on topological structure, not microscopy.

3. **CPT from particle-hole symmetry**: The fundamental CPT symmetry protecting the spectral action [iK_7, D_K] = 0 is a manifestation of particle-hole symmetry in the condensate.

4. **Gauge symmetries from textures**: The SU(2) x U(1) x SU(3) gauge symmetries of the Standard Model emerge from the internal geometry (SU(3)) and its fluctuations.

5. **Robustness to microscopic details**: The framework's predictions (particle masses, coupling constants, cosmological parameters) depend only on topological invariants of the condensate, not on trans-Planckian microphysics.

6. **Testability despite Unknown UV**: Even though the microscopic physics at the compactification scale is unknown, low-energy predictions are precise and falsifiable — a feature, not a bug.

---

## References

- Volovik, G. E. (2013). "Lorentz invariance without trans-Planckian physics?" *Physics Letters B*, 718(1), 93-97. arXiv:1303.1914.

- Kostelecký, V. A., & Russell, N. (2011). "Data tables for Lorentz and CPT violation." *Reviews of Modern Physics*, 83(1), 11.

- Jacobson, T., Liberati, S., & Mattingly, D. (2006). "Lorentz violation at high energies: concepts, phenomena, and astrophysical signatures." *Annals of Physics*, 321(1), 150-196.

- Mattingly, D. (2005). "Modern tests of Lorentz invariance." *Living Reviews in Relativity*, 8(1), 1-84.
