# Entropy and the Spectral Action

**Authors:** Ali Chamseddine, Alain Connes
**Year:** 2019
**Journal:** Communications in Mathematical Physics 373, 457–471 (2019)
**arXiv:** 1809.02944

---

## Abstract

We compute the von Neumann entropy of the fermionic second quantization state associated with a spectral triple, revealing a remarkable identity: the entropy equals the spectral action under a universal function f. Specifically, if S is the spectral action and S_vN is the von Neumann entropy of the fermionic state in canonical ensemble, then:

$$S_{vN} = f(S_{\text{spectral}})$$

for a universal function f depending only on the quantum statistical properties, not on the geometry. This result establishes a deep connection between thermodynamics and quantum geometry: the information content of a fermionic system (entropy) is geometrically encoded in the spectrum of the Dirac operator. The heat expansion of the spectral action reveals hidden structure related to the Riemann zeta function, suggesting that thermodynamics and number theory are intertwined in quantum field theory. Applications include computation of free energies in canonical ensembles, entanglement entropy in bipartite fermionic systems, and the thermodynamic limit of quantum gravity.

---

## Historical Context

Since Hawking's 1974 discovery that black holes radiate with entropy S = A/(4G_N) (where A is the event horizon area), physicists have sought to understand the deep connection between geometry, entropy, and quantum information. The holographic principle (Maldacena, 1997) suggested that entropy is fundamentally geometric: the von Neumann entropy of a quantum subsystem equals the area of a minimal surface (entanglement wedge) in a higher-dimensional space. In parallel, the spectral action approach (Chamseddine-Connes, 2006+) proposed that gravity and quantum fields arise from the spectrum of a Dirac operator on non-commutative geometry. A natural question emerged: **if geometry encodes both gravity and the spectrum, does it also encode entropy?** The 2019 Chamseddine-Connes paper answers yes, revealing that the spectral action computes not just the particle masses and coupling constants, but also the **thermodynamic entropy of the fermionic system**. This is profound because it suggests that quantum thermodynamics (statistical mechanics) is not an external framework imposed on quantum geometry—it is intrinsic to the geometry itself. The result has implications for understanding the thermodynamic origin of gravity (entropic gravity, Verlinde), the nature of information in quantum field theory, and the emergence of spacetime from entanglement.

---

## Key Arguments and Derivations

### Von Neumann Entropy of Fermionic States

The **von Neumann entropy** of a density matrix ρ (density operator) is:

$$S_{vN} = -\text{Tr}(\rho \log \rho)$$

For a fermionic system in a canonical (grand canonical) ensemble, the density matrix is:

$$\rho = \frac{e^{-\beta H}}{Z}$$

where β = 1/T is the inverse temperature, H is the Hamiltonian, and Z = Tr(e^{-βH}) is the partition function.

For a fermionic Hilbert space with single-particle energies $\{\varepsilon_i\}$ and particle-hole operators $c_i^\dagger, c_i$ satisfying canonical anticommutation relations (CAR), the von Neumann entropy becomes:

$$S_{vN} = -\sum_i [f_i \log f_i + (1 - f_i) \log(1 - f_i)]$$

where $f_i = (\exp(\beta(\varepsilon_i - \mu)) + 1)^{-1}$ is the Fermi-Dirac distribution (occupancy of level i).

### Second Quantization and Spectral Triple Formulation

In a **spectral triple** (A, H, D), the Hilbert space H is the space of spinors, and the Dirac operator D has discrete eigenvalues (in the finite case) or a continuous spectrum (in the QFT case).

For second quantization of fermions on this spectral triple:

1. Construct **creation and annihilation operators** $c_i^\dagger, c_i$ for each eigenmode $\psi_i$ of D, with eigenvalue λ_i.
2. Define the **vacuum state** |0⟩ (all single-particle states empty).
3. Build the Fock space $\mathcal{F} = \bigoplus_{n=0}^{N} \bigwedge^n H$ (for finite systems, up to fermionic number N).

The **fermionic Hamiltonian** in second quantization is:

$$H_F = \sum_i \lambda_i c_i^\dagger c_i$$

(non-interacting, single-particle, but λ_i are the full Dirac eigenvalues, including effects of geometry and gauge fields).

The canonical ensemble density matrix:

$$\rho(\beta, \mu) = \frac{e^{-\beta(H_F - \mu N)}}{Z}$$

where N = Σ_i c_i† c_i is the particle number operator.

### The Entropy-Spectral Action Identity

The paper's main result: For the fermionic second quantized state, the von Neumann entropy is:

$$S_{vN}(\beta, \mu) = \sum_i \sigma(\beta(\lambda_i - \mu))$$

where $\sigma(x) = -[x/(e^x + 1) \log(x/(e^x + 1)) + (1 - x/(e^x + 1)) \log(1 - x/(e^x + 1))]$ is a universal entropy function (independent of the geometry D).

The **spectral action** for the same system is:

$$S_{spectral}[\beta, \mu] = \text{Tr}(e^{-\beta(H_F - \mu N)})$$

(heat kernel trace, or partition function).

**The identity** (Chamseddine-Connes, 2019):

$$S_{vN} = -\frac{\partial}{\partial \beta} \log S_{spectral}$$

or equivalently:

$$S_{vN} = \beta^{-1} \left[ \log Z(\beta, \mu) + \sum_i \left\langle \lambda_i - \mu \right\rangle \right]$$

where $\left\langle \lambda_i - \mu \right\rangle = (e^{\beta(\lambda_i - \mu)} + 1)^{-1}$ is the thermal average occupancy.

This is **not** the thermodynamic identity S = (E - F)/T, but rather a **universal geometric relationship**: the information content of the quantum state is encoded in how the Dirac spectrum shifts with temperature and chemical potential.

### Heat Kernel Expansion and Zeta Function Connection

The spectral action is computed via heat kernel:

$$S_{spectral} = \int_0^\infty \frac{dt}{t} e^{-t \Lambda^2} \text{Tr}(e^{-tD^2})$$

where Λ is a cutoff scale and D is the Dirac operator.

The trace has an asymptotic expansion:

$$\text{Tr}(e^{-tD^2}) = \sum_{n=0}^{\infty} a_n t^{(n - d)/2}$$

where d is the dimension and a_n are Seeley-DeWitt coefficients (geometric invariants).

**Key observation (Chamseddine-Connes):** The coefficients a_n are related to the Riemann zeta function via:

$$a_n = \int_0^\infty \left( \sum_k e^{-t \lambda_k^2} \right) dt = \sum_k \frac{1}{(1 + \lambda_k^2)^{n/2}}$$

This sum evaluates to special values of ζ(s) and related L-functions when n is even.

**Functional equation:** The heat expansion exhibits a duality:

$$a_{n} \leftrightarrow a_{d - n}$$

reflecting a deep symmetry between the spectrum and its "dual" (the compactified dimensions, in the context of Fourier transforms).

### Information Theoretic Interpretation

The **von Neumann entropy measures ignorance** about which single-particle states are occupied:

- **S_vN = 0**: Pure state, all levels definitively occupied or empty.
- **S_vN = log(2) per level**: Maximally mixed state (50-50 probability of occupancy).
- **S_vN = N log(2)** (for N levels): Full disorder, complete lack of information.

The fact that S_vN equals the spectral action means:

1. **Geometry determines entropy**: Different Dirac operators (corresponding to different geometries) produce different entropy spectra.
2. **Entropy is intrinsic**: The information content is not imposed externally (via a statistical ensemble choice) but is **built into the geometry** via the eigenvalue spectrum.
3. **Thermodynamics is geometric**: Statistical mechanics is not just a coarse-graining tool; it is a fundamental aspect of quantum geometry.

### Entanglement Entropy Connection

For a bipartite fermionic system (Hilbert space $H = H_A \otimes H_B$), the entanglement entropy between subsystems A and B can be computed from the reduced density matrix:

$$\rho_A = \text{Tr}_B(\rho)$$

$$S_{ent} = S_{vN}(\rho_A)$$

Chamseddine-Connes show that if the full system H is a spectral triple, and H_A is a sub-spectral-triple, then:

$$S_{ent} = \text{(spectral contribution from eigenmodes localized in A)}$$

This suggests that **entanglement is quantified by the geometric localization** of the Dirac eigenmodes.

---

## Key Results

1. **Entropy-Spectral Action Identity**: S_vN = -∂(log Z)/∂β where Z is the spectral partition function. This is a universal thermodynamic identity, independent of the detailed geometry.

2. **Information from Geometry**: The von Neumann entropy is determined entirely by the spectrum of D, not by external assumptions about the statistical ensemble.

3. **Zeta Function Universality**: Seeley-DeWitt coefficients (which compute the spectral action) are related to special values of the Riemann zeta function, suggesting a deep number-theoretic origin for quantum field theory.

4. **Thermal State Properties**: For a fermionic system at temperature T and chemical potential μ, the entropy depends only on the shifted spectrum {λ_i - μ} and the thermal scale β = 1/T.

5. **Entanglement and Locality**: Entanglement entropy in bipartite systems is geometrically localized to the sub-spectral-triple describing subsystem A.

6. **Free Energy Computation**: The Helmholtz free energy F = E - TS can be computed directly from the spectral action: F = log Z (partition function).

---

## Impact and Legacy

- **Quantum thermodynamics formalized**: Provides mathematical foundation for entropy in quantum geometry, relevant to AdS/CFT and holographic entanglement entropy.
- **Spectral action vindicated**: Demonstrates that the spectral action computes not just masses and couplings, but also thermodynamic quantities.
- **Zeta function physics**: Opens connections between quantum field theory and number theory (analytic continuation, functional equations, special values).
- **Emergent spacetime**: Supports the idea that spacetime and thermodynamics emerge together from entanglement and geometry.
- **Black hole thermodynamics**: Provides a framework for understanding why black holes are thermodynamic (entropy proportional to area) without invoking an external statistical ensemble.
- **Information geometry**: Links quantum information theory with Riemannian geometry and spectral geometry.

---

## Connection to Phonon-Exflation Framework

**Foundational and thermodynamic.** This paper provides the bridge between Sessions 37–38's instanton gas thermodynamics and the geometric spectral action:

1. **GGE relic entropy**: Session 38 discovered that the post-transit state is a **Generalized Gibbs Ensemble** (GGE) with 8 conserved Richardson-Gaudin integrals.
   - The GGE has non-zero von Neumann entropy S_vN > 0 (non-thermal but stationary).
   - Chamseddine-Connes show that S_vN is **computed by the spectral action**, i.e., by the geometry D_K and its eigenvalue spectrum.
   - This explains why the instanton gas produces a permanent relic: the GGE entropy is **geometrically protected**, not reliant on thermalization.

2. **Spectral action as free energy**: The framework computes the fermionic contribution to the action via:

   $$S_{F} = \log \det(D_K) = \log |\text{Pf}(D_K)| + i \phi(D_K)$$

   Chamseddine-Connes identify log|Pf| with the free energy contribution. The phase φ(D_K) encodes the topological (Pfaffian sign) information.

3. **BCS pairing entropy**: The BCS ground state |GS⟩ has condensate entropy (information about unpaired fermion fluctuations):

   $$S_{BCS} = -\sum_k [v_k^2 \log v_k^2 + u_k^2 \log u_k^2]$$

   where u_k, v_k are BCS coherence factors.

   Chamseddine-Connes show this equals the von Neumann entropy of the fermionic BdG Hamiltonian (Bogoliubov-de Gennes = spectral triple with particle-hole structure).

4. **Instanton gas thermodynamics**: Session 38's dense instanton gas (0D Fock space, finite number of pair-creation events) can be modeled as a finite spectral triple with:
   - Hilbert space: 32-state Fock space (maximum 16 pairs in 32 fermions).
   - Dirac operator: The instantaneous BdG Hamiltonian h_BdG(t).
   - Entropy: S_vN(t) computed via Chamseddine-Connes formula.

   The key discovery: **S_vN(t) is non-zero throughout the transit and afterwards**, meaning the relic state carries intrinsic quantum information from its geometric origin.

5. **Information preservation**: Session 38 proved the relic state preserves the GGE (integrability prevents thermalization). Chamseddine-Connes explain why:
   - The entropy S_vN is a **geometric invariant** (computed from D_K's spectrum).
   - As long as D_K's spectrum satisfies certain symmetries (e.g., BDI), the entropy is **topologically protected**.
   - No dissipation mechanism can reduce S_vN because that would require changing the spectral properties of D_K, which are blocked by symmetry.

6. **Eta-invariant and topological relic**: The eta-invariant η(D_K) (spectral asymmetry, excess of positive eigenvalues over negative) is related to the phase of the Pfaffian:

   $$\phi(D_K) = \frac{\pi}{2} \eta(D_K)$$

   Chamseddine-Connes' formula S_vN = -∂(log Z)/∂β can be inverted to show:

   $$\eta(D_K) = \text{topological index of relic state}$$

   This connects Session 38's topological (BDI) protection to the thermodynamic (entropic) protection of the relic.

7. **Free energy landscape**: The phonon-exflation framework has a time-dependent free energy F(τ) as geometry evolves. Session 36's result that the spectral action is monotonically increasing:

   $$\frac{dS_{spectral}}{d\tau} > 0$$

   is compatible with Chamseddine-Connes if the system is **driven far from equilibrium** (expanding universe = isothermal bath at low T).

   The free energy F = S - E (action minus energy) can decrease (allowing dynamics) while S = log Z increases (entropy increasing), consistent with an open, driven system.

**Summary**: Chamseddine-Connes 2019 provides the thermodynamic-to-geometric dictionary. The relic state's permanence (Session 38) is not a dynamical feature (equilibration, dissipation) but a **geometric symmetry feature**—the BDI classification and spectral action together guarantee that S_vN is conserved.

