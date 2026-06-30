# Topology of quantum vacuum

**Author(s):** G.E. Volovik
**Year:** 2012
**Journal:** Lecture Notes in Physics 870, 343-383 (2013)
**arXiv:** 1111.4627
**Relevance:** HIGH

---

## Abstract

Topology in momentum space is the main characteristics of the ground states of a system at zero temperature, the quantum vacua. The gaplessness of fermions in bulk, on the surface or inside the vortex core is protected by topology, and is not sensitive to details of the microscopic physics (atomic or trans-Planckian). Irrespective of the deformation of the parameters of the microscopic theory, the energy spectrum of these fermions remains strictly gapless. This solves the main hierarchy problem in particle physics: for fermionic vacua with Fermi points the masses of elementary particles are naturally small. The quantum vacuum of Standard Model is one of the representatives of topological matter alongside with topological superfluids and superconductors, topological insulators and semi-metals, etc. There is a number of topological invariants in momentum space of different dimensions. They determine universality classes of the topological matter and the type of the effective theory which emerges at low energy. In many cases they also give rise to emergent symmetries, including the effective Lorentz invariance, and emergent phenomena such as effective gauge and gravitational fields. The topological invariants in extended momentum and coordinate space determine the bulk-surface and bulk-vortex correspondence. They connect the momentum space topology in bulk with the real space. These invariants determine the gapless fermions living on the surface of a system or in the core of topological defects.

---

## Key Arguments and Derivations

### Classification of Topological Matter

Volovik provides a comprehensive classification of quantum vacua by momentum-space topology. The three main universality classes for 3+1 dimensional fermionic systems are:

1. **Fully gapped vacua** (topological insulators, 3He-B): characterized by integer invariant N_K in Eq.(15). BDI symmetry class.
2. **Fermi point vacua** (3He-A, Standard Model above EW transition): characterized by N_3 invariant (hedgehog/Chern number). Weyl fermions emerge.
3. **Fermi surface vacua** (normal metals, normal 3He): characterized by N_1 winding number.

Additionally, nodal line systems (polar phase of 3He, cuprate superconductors) represent another class.

### Fermi Surface Topology

The Fermi surface is a topologically protected singularity in the Green's function. In the extended (omega, p)-space, the Fermi surface is a vortex ring:

N = tr oint_C (dl/2pi i) G(omega, p) partial_l G^{-1}(omega, p)

where C is a contour around the Green's function singularity. Even when quasiparticles are not well-defined (no poles in G), the topological singularity survives. Zeroes of G replace poles in strongly interacting systems.

### Weyl Points

The Weyl point in 3He-A is a hedgehog (Berry phase monopole) in p-space. The topological charge is:

N = (1/8pi) epsilon_{ikl} integral_sigma dS_i g-hat . (partial g-hat/partial p_k x partial g-hat/partial p_l)

where g-hat = g/|g| and H = tau . g(p) is the Bogoliubov-Nambu Hamiltonian. Near the Weyl point, the Hamiltonian expands as H = e^i_alpha tau^alpha (p_i - K^(a)_i), giving emergent Weyl fermions.

### 3He-B as Topological Superfluid

3He-B is a fully-gapped topological superfluid with topological charge N_K = 2 in the weak-coupling limit (mu > 0, m* > 0). The phase diagram in (mu, 1/m*) plane shows a topological quantum phase transition at mu = 0 between topological (N_K = 2) and non-topological (N_K = 0) states. This transition is equivalent to the transition between Dirac vacua with opposite mass parameter.

### Bulk-Surface Correspondence

Topologically non-trivial bulk states have protected gapless surface states. In 3He-B, the surface hosts Majorana fermions with linear dispersion E = c(p_y sigma_z - p_z sigma_y) (for surface perpendicular to x). These are the first-ever topologically protected Majorana surface states.

### Flat Bands

Vortices in Weyl superfluids (3He-A) contain dispersionless (flat) bands of Andreev-Majorana fermions. The flat band region is bounded by the projections of the bulk Weyl points onto the vortex axis. This is a bulk-defect correspondence.

---

## Key Results

1. Three universality classes of fermionic vacua in 3+1D: fully gapped, Fermi point, and Fermi surface
2. The Standard Model vacuum above EW transition belongs to the Fermi point universality class
3. Topological protection of gapless spectrum solves the hierarchy problem
4. 3He-B is a topological superfluid (N_K = 2) with Majorana surface states
5. Weyl points are Berry phase monopoles in momentum space
6. Bulk-surface correspondence connects p-space topology to real-space boundary states
7. Flat bands in vortex cores of Weyl superfluids
8. Topological quantum phase transition at mu = 0 in 3He-B phase diagram
9. Zeroes of the Green's function (not just poles) carry topological charge

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Fermi surface invariant | $N = \text{tr}\oint_C \frac{dl}{2\pi i}G(\omega,\mathbf{p})\partial_l G^{-1}(\omega,\mathbf{p})$ | Eq.(13) |
| Weyl point invariant (3D) | $N_3 = \frac{1}{24\pi^2}\epsilon^{\mu\nu\lambda\sigma}\text{tr}\oint_\Sigma dS_\sigma\; G\partial_\mu G^{-1}G\partial_\nu G^{-1}G\partial_\lambda G^{-1}$ | Eq.(15) |
| BN Hamiltonian | $H = \boldsymbol{\tau}\cdot\mathbf{g}(\mathbf{p})$ | Eq.(16) |
| 3He-A vector components | $g_1 = \hat{e}_1\cdot\mathbf{p},\; g_2 = \hat{e}_2\cdot\mathbf{p},\; g_3 = p^2/2m - \mu$ | Eq.(17) |
| Hedgehog charge | $N = \frac{1}{8\pi}\epsilon_{ikl}\int_\sigma dS_i\,\hat{g}\cdot\left(\frac{\partial\hat{g}}{\partial p_k}\times\frac{\partial\hat{g}}{\partial p_l}\right)$ | Eq.(18) |
| Emergent Weyl Hamiltonian | $H^{(a)} = e^i_\alpha\tau^\alpha(p_i - K^{(a)}_i)$ | Eq.(19) |
| Nodal line invariant | $N = \text{tr}\oint_C \frac{dl}{4\pi i}\tau_2 H^{-1}(\mathbf{p})\partial_l H(\mathbf{p})$ | Eq.(24) |
| 3He-B Hamiltonian | $H = \tau_3\left(\frac{p^2}{2m^*} - \mu\right) + c_B(\boldsymbol{\sigma}\cdot\mathbf{p})\tau_1$ | Eq.(25) |
| 3He-B topological charge | $N_K = \text{sign}(M) = \text{sign}(-\mu)$ (for Dirac limit) | Eq.(28) |
| CdGM bound states | $E_n = -\left(n + \frac{1}{2}\right)\omega_0(p_z)$ | Eq.(60) |
| Weyl vortex zero modes | $E_n = -n\omega_0(p_z)$ (with n=0 exact zero) | Eq.(61) |

---

## Relevance to Phonon-Exflation

1. **Universality classes and D_K spectrum**: The classification of vacua by momentum-space topology directly informs the framework's analysis of the Dirac operator D_K on SU(3). The framework's BDI symmetry class (T^2=+1) and topological invariants are the SU(3) fiber versions of the invariants classified here.

2. **Weyl points and SM emergence**: The Weyl point as hedgehog/Berry monopole is the topology underlying the framework's D_K spectrum. The framework's [iK_7, D_K] = 0 result, which breaks SU(3) to U(1)_7, is a specific instance of how Weyl points emerge from the full Dirac spectrum.

3. **Bulk-surface correspondence**: The framework's interface between different tau regions (the "fold") is the geometric analog of the bulk-boundary interface where topological surface states appear. The framework's BCS instability at the fold is the dynamical version of the topological quantum phase transition at mu = 0.

4. **Flat bands and Van Hove singularity**: The flat bands in vortex cores of Weyl superfluids have a direct analog in the framework's Van Hove singularity at the fold (M_max = 1.674 from Session 35), which provides the divergent density of states driving the BCS instability.

5. **3He-B phase diagram**: The topological phase transition at mu = 0 maps to the framework's fold transition as tau crosses the critical value, where the spectral gap structure changes topology.
