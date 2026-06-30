# Topological Superfluids

**Author(s):** G.E. Volovik
**Year:** 2016 (published 2019 in JETP)
**Journal:** JETP 129, 618-641 (2019)
**arXiv:** 1602.02595
**Relevance:** CRITICAL

---

## Abstract

There are many topological faces of the superfluid phases of 3He. These superfluids contain various topological defects and textures. The momentum space topology of these superfluids is also nontrivial, as well as the topology in the combined (p, r) phase space, giving rise to topologically protected Dirac, Weyl and Majorana fermions living in bulk, on the surface and within the topological objects. The nontrivial topology leads to different types of anomalies, which extended in many different directions the Landau-Khalatnikov theory of superfluidity.

---

## Key Arguments and Derivations

### 1. Real-Space Topology of Defects

The superfluid phases of 3He contain a rich zoo of topological objects:
- Vortex-skyrmions (N=2) in chiral 3He-A
- Half-quantum vortices (Alice strings) in polar phase
- Spin-mass vortices in 3He-B
- Hedgehog-monopoles terminated by strings
- Kibble walls terminated by Alice strings
- Witten superconducting strings (twist of asymmetric vortex core)

The Mermin-Ho relation connects the orbital texture to the superfluid velocity:
v_s = (hbar/4m) epsilon_{ijk} l-hat_i nabla l-hat_j x nabla l-hat_k

### 2. Momentum Space Topology

Three superfluid phases represent three types of topological materials:
- **3He-A (Weyl superfluid)**: Weyl points at K^(a) = +/- p_F l-hat, topological charge N = +/-2 (degenerate over spin). The Weyl point is a hedgehog/Berry monopole in p-space.
- **Polar phase (Dirac nodal ring)**: E = 0 when p_z = 0 and p_x^2 + p_y^2 = p_F^2. Protected by discrete symmetry (H anticommutes with tau_2).
- **3He-B (topological superfluid)**: Fully gapped with N_K = 2. Majorana surface states.

### 3. Weyl Fermions and Emergent Gauge Fields

Near the Weyl point, the Hamiltonian: H^(a) = e^i_alpha tau^alpha (p_i - q^(a) A_i)

with effective electromagnetic field A = p_F l-hat and effective charge q^(a) = +/-1. The emergent Weyl fermions lead to T^4 thermodynamic behavior (experimentally observed).

### 4. 3He-B Phase Diagram

The topological phase transition at mu = 0 separates:
- Weak coupling 3He-B (mu > 0, m* > 0, N_K = 2): topological
- Strong coupling 3He-B (mu < 0, m* > 0, N_K = 0): non-topological

The interface between N_K = +2 and N_K = -2 hosts a single Majorana fermion. The real 3He-B lives in the limit Delta_B << mu (weak coupling corner).

### 5. Chiral Anomaly Experiments

The generalized ABJ equation for 3He-A with skyrmion texture:

partial_t (n_R - n_L) = (1/4pi^2) sum_a (q^(a))^2 N_a C^(a) (E_eff . B_eff)

The chiral anomaly has been experimentally verified in Manchester/Helsinki through:
- Vortex dynamics (spectral flow force on ATC vortex)
- Skyrmion creation via helical instability (chiral magnetic effect analog)

### 6. Majorana Surface States in 3He-B

Surface states found by the method of trajectories. The Hamiltonian along trajectory decomposes into H_0 = -i v_F tau_3 partial_z + tau_1 sigma_x Delta_perp(x) (supersymmetric, with Delta_perp as superpotential). The surface spectrum:

E(p_parallel) = Delta_B (sigma_y p_y + sigma_z p_z) / p_F (with sigma_x dropped by surface boundary)

These Majorana states have been probed through anomalous transverse sound attenuation, surface specific heat, and magnon BEC (NMR experiments).

### 7. Flat Bands in Vortex Cores

For N=1 vortex in Weyl superfluid 3He-A, the spectrum has EXACT zero-energy states:
E_n = -n omega_0(p_z)

The n=0 states form a dispersionless (flat) band. The flat band region in p_z is bounded by the projections of Weyl points: |p_z| < p_F |cos lambda|. This is a bulk-defect correspondence.

### 8. Condensation of Andreev-Majorana Fermions

In the polar phase, the nodal ring produces ω_0(p_z) ~ p_z^2 ln(p_F/p_z), causing all energy levels to squeeze toward zero at p_z = 0. This is "condensation" of Andreev-Majorana fermions, giving divergent density of states at low energy.

---

## Key Results

1. Three phases of 3He represent three universality classes of topological matter: Weyl (A), Dirac nodal (polar), fully gapped (B)
2. Half-quantum vortices experimentally observed in polar phase (2016)
3. Chiral anomaly experimentally confirmed via spectral flow and helical instability
4. Majorana surface states in 3He-B probed in multiple experiments
5. Flat bands in vortex cores of Weyl superfluids (dispersionless E_n = -n omega_0)
6. 3He-B phase transition at mu=0 is topological quantum phase transition
7. Witten string analog: asymmetric vortex core with superconducting twist mode
8. Combined (p,r) phase-space topology connects bulk and defect properties

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Mermin-Ho relation | $\mathbf{v}_s = \frac{\hbar}{4m}\epsilon_{ijk}\hat{l}_i\nabla\hat{l}_j\times\nabla\hat{l}_k$ | Eq.(3) |
| Skyrmion charge | $m_l = \frac{1}{4\pi}\int dx\,dy\;\hat{l}\cdot\left(\frac{\partial\hat{l}}{\partial x}\times\frac{\partial\hat{l}}{\partial y}\right)$ | Eq.(4) |
| Fermi surface invariant | $N = \text{tr}\oint_C \frac{dl}{2\pi i}G\partial_l G^{-1}$ | Eq.(13) |
| Weyl point invariant | $N_3 = \frac{1}{24\pi^2}\epsilon^{\mu\nu\lambda\sigma}\text{tr}\oint dS_\sigma\; G\partial_\mu G^{-1}G\partial_\nu G^{-1}G\partial_\lambda G^{-1}$ | Eq.(15) |
| BN Hamiltonian | $H = \boldsymbol{\tau}\cdot\mathbf{g}(\mathbf{p})$ | Eq.(16) |
| Hedgehog charge | $N = \frac{1}{8\pi}\epsilon_{ikl}\int dS_i\;\hat{g}\cdot(\partial_{p_k}\hat{g}\times\partial_{p_l}\hat{g})$ | Eq.(18) |
| Emergent Weyl | $H^{(a)} = e^i_\alpha\tau^\alpha(p_i - q^{(a)}A_i)$ | Eq.(20) |
| Polar phase | $H = \tau_3(p^2/2m-\mu) + cp_z(\boldsymbol{\sigma}\cdot\hat{d})\tau_1$ | Eq.(23) |
| Nodal line invariant | $N = \text{tr}\oint_C \frac{dl}{4\pi i}\tau_2 H^{-1}\partial_l H$ | Eq.(24) |
| 3He-B topology | $N_K = \text{sign}(M) = \text{sign}(-\mu)$ | Eq.(28) |
| CdGM (non-topological) | $E_n = -(n+\frac{1}{2})\omega_0(p_z)$ | Eq.(60) |
| Weyl vortex (topological) | $E_n = -n\omega_0(p_z)$ (exact zero at n=0) | Eq.(61) |
| Chiral anomaly (general) | $\partial_t(n_R - n_L) = \frac{1}{4\pi^2}\sum_a (q^{(a)})^2 N_a C^{(a)}(\mathbf{E}_{\text{eff}}\cdot\mathbf{B}_{\text{eff}})$ | Sec.5 |

---

## Relevance to Phonon-Exflation

This is a CRITICAL paper for the framework -- it is Volovik's most comprehensive review of the topological properties that the phonon-exflation framework implements on M4 x SU(3).

1. **Three universality classes**: The framework's D_K spectrum on SU(3) must belong to one of these classes. The BCS instability at the fold (Session 35) suggests the relevant transition is between the Weyl-point class (with Fermi points) and the fully-gapped class, exactly as in the 3He-A to 3He-B transition.

2. **Flat bands and Van Hove**: The flat bands in vortex cores (E_n = -n omega_0) are the physical origin of the Van Hove singularity that drives the BCS instability in the framework (M_max = 1.674 from Session 35). The divergent DOS from Andreev-Majorana condensation in the polar phase is another realization.

3. **Majorana surface states**: The Majorana states at the interface between topologically distinct phases (N_K = +2 and N_K = -2) are the analog of the boundary states at the framework's fold, where the spectral gap structure changes topology.

4. **Experimental confirmation of anomaly**: The experimental verification of the chiral anomaly in 3He-A (both Manchester and Helsinki) provides the strongest evidence that the emergent physics program actually works. This is the physical process that the framework's quasiparticle creation during transit implements.

5. **Half-quantum vortices and Alice strings**: The observation of HQVs in the polar phase demonstrates that topological objects predicted by the emergent physics program exist in nature. The framework's U(1)_7 breaking by BCS condensation produces analogs of these objects.
