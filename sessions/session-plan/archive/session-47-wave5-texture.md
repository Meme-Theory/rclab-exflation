# Session 47 Wave 5: Texture Spectrum on the Fabric

**Author**: Volovik (Superfluid Universe Theorist)
**Date**: 2026-03-16
**Status**: PLAN (not computation). Target execution: S48.
**Objective**: Compute the power spectrum of inter-cell condensate variations across the 32-cell tessellation, and extract the spectral index n_s from the texture correlation function.

---

## 0. Why This Is the Last Path Standing

Eleven single-cell n_s routes are closed (S44-S47). The universal obstruction: any readout of the single-cell BdG spectrum gives a steep power law from the factor-2.5 eigenvalue span and flat BCS gap. The spectral index |beta_k|^2 ~ (Delta/omega_k)^4 is a property of the temporal quench profile, not of spatial structure.

The surviving path rests on a physical distinction that no session has yet computed: the primordial perturbation spectrum is not the pair creation spectrum within a single cell, but the correlation spectrum of the condensate field ACROSS cells. In superfluid 3He, the CMB analog is the texture power spectrum -- the statistical properties of the order parameter l(r) across many domains -- not the quasiparticle spectrum within a single coherent volume (Paper 01, Ch. 7; Paper 14, Sec. I-III; Paper 27, Sec. on phonon production).

The distinction is between:
- **Microscopic**: |beta_k|^2 at each KK momentum k within one cell (steep, closed)
- **Macroscopic**: P(K) at each spatial wavenumber K across the fabric (unknown, computable)

where K = 2*pi/L is the fabric-scale wavenumber, not the internal KK momentum.

---

## 1. The Order Parameter Field Across the Tessellation

### What is the texture variable?

In 3He-A, the order parameter is the l-vector: a unit vector on S^2 that specifies the orbital angular momentum direction of the Cooper pairs. The texture l(r) varies smoothly across the sample. Its power spectrum P_l(k) determines the correlation of orientation fluctuations (Paper 01, Ch. 7.3; Paper 14, Sec. II).

In 3He-B, the order parameter is a rotation matrix R in SO(3): the Leggett angle theta that specifies the relative rotation between spin and orbital spaces. The texture theta(r) has a correlation length set by the dipole length xi_D.

In the framework, the Jensen deformation makes tau the natural scalar order parameter -- the single modulus parametrizing the volume-preserving shape change of SU(3). However, tau is the SAME for all cells by construction (it parametrizes the global Jensen deformation, not a local field). The cell-to-cell variation is not in tau itself, but in:

**(a) The condensate amplitude Delta_cell.** After the quench (S38: P_exc = 1.000), each cell independently produces a GGE relic with quasiparticle occupation numbers n_k determined by the local quench dynamics. The total condensate depletion Delta_cell/Delta_0 varies cell-to-cell because the quench is causal -- separated cells make independent quantum choices (Paper 14, Sec. III.A; Paper 27, Sec. 2).

**(b) The condensate phase phi_cell.** The U(1)_7 phase of the BCS condensate is spontaneously chosen at each cell. Cells separated by more than xi_KZ choose independently. The phase texture phi(r) is the Goldstone field of the broken U(1)_7.

**(c) The sector-resolved gap vector (Delta_B1, Delta_B2, Delta_B3)_cell.** Each cell has three BCS gaps. Their RATIOS may differ cell-to-cell if the quench dynamics is sensitive to local fluctuations.

**Physical choice**: The condensate phase phi_cell is the dominant texture variable. Here is the argument from 3He:

1. In 3He-B, the dominant texture is the phase theta(r) (Leggett angle), not the gap amplitude |Delta|. The reason: amplitude fluctuations are massive (they cost condensation energy ~ Delta^2 * N(0)), while phase fluctuations are massless (Goldstone mode, cost only gradient energy ~ rho_s * (nabla phi)^2). The phase texture dominates the long-wavelength correlation spectrum.

2. The framework's Cooper pairs carry K_7 = +/-1/4 (S35). The condensate spontaneously breaks U(1)_7. The Goldstone boson is the phase mode of this broken symmetry. Post-quench (S38: NG mode ceases to exist), the phase is FROZEN -- the GGE relic has a fixed phase at each cell, with no dynamics to homogenize it.

3. Amplitude fluctuations delta|Delta| are O(|Delta|) for a completely quenched system (P_exc = 1.000), so both phase and amplitude textures are order-one. But the phase is the one with long-range correlations set by gradient energy, while the amplitude is locally determined.

**Conclusion**: The texture field is phi(r) -- the U(1)_7 phase of the BCS condensate at each tessellation cell. The power spectrum P_phi(K) of this phase texture is the primordial perturbation spectrum.

---

## 2. What Sets the Domain Size

### Kibble-Zurek length

From S38: xi_KZ = 0.152 L_total (where L_total = circumference of the tessellation in M_KK^{-1} units). From s46_fabric_tessellation.npz: L_total = 4.864, N_domains = 32, so the cell size is:

    l_cell = L_total / N_domains = 4.864 / 32 = 0.152 M_KK^{-1}

This is a coincidence that needs scrutiny: xi_KZ = l_cell exactly? From s42_fabric_wz.npz: xi_KZ_MKK = 0.269, xi_BCS_MKK = 1.118. The tessellation cell size R_cell = 4488 Mpc in physical units. The 32-cell tessellation was established in S42 from the requirement that the Kibble-Zurek correlation length fits exactly N times into the observable volume (Paper 14, Eq. 5; Paper 02, Sec. 4.2):

    N_domains = (L_total / xi_KZ)^d

where d = 3 for volume tessellation. With xi_KZ = 0.152 and L_total = 4.864: N = (4.864/0.152)^1 = 32 in the 1D case (or (4.864/0.152)^3 ~ 32768 in 3D). The S42 computation used the 1D count. Whether this is correct depends on the dimensionality of the fabric.

**For S48**: The computation should parametrize N_domains as an input (testing N = 8, 16, 32, 64) rather than fixing it at 32. The spectral index should be robust to the number of domains if the physics is correct.

### What determines 32?

The number 32 comes from the S42 Kibble-Zurek tessellation: xi_KZ is set by the transit speed and the healing time, and the number of domains is the ratio of system size to xi_KZ. The specific value 32 is a 1D estimate (linear chain of domains along one dimension of the fabric). In 3D, the domain count would be much larger.

For the power spectrum, what matters is not the exact number but the RATIO K * xi_KZ: modes with K * xi_KZ >> 1 are in the white-noise regime, and modes with K * xi_KZ << 1 have correlated texture.

---

## 3. What Sets the Inter-Domain Coupling

### Gradient energy

The texture gradient energy for phase fluctuations on the tessellation is (Paper 01, Ch. 7.3; Paper 22, Eq. 12):

    E_grad = (1/2) Sum_{ab} rho_s^{ab} integral (nabla_a phi)(nabla_b phi) d^8x

where rho_s^{ab} is the superfluid density tensor (W3-4: 24x anisotropic) and nabla_a is the spatial gradient in the a-th su(3) direction.

For the INTER-CELL gradient, the relevant variable is not the gradient within the internal SU(3) but the gradient across the fabric in the external spatial directions. The stiffness for inter-cell phase variations is the Josephson coupling:

    E_J = J * Sum_{<ij>} cos(phi_i - phi_j)

where J is the Josephson energy between neighboring cells and the sum runs over adjacent cell pairs.

The Josephson coupling J is determined by the overlap of condensate wavefunctions between cells. From W2-1 (CONDENSATE-T2-47): the condensate has a 1/e^2 radius of 0.78 rad on the maximal torus. In the 0D limit (L/xi_GL = 0.031, S38), the coherence length vastly exceeds the cell size, so the overlap between adjacent cells is near-maximal.

**The key physics**: J is set by the BCS condensation energy modulated by the geometric overlap. An estimate:

    J ~ |E_cond| * f_overlap

where E_cond = -0.137 (S38) and f_overlap depends on the boundary geometry. For cells sharing a full face of the Voronoi tessellation, f_overlap ~ 1. For the 32-cell tessellation, each cell has approximately 2d = 6 neighbors (d=3 spatial dimensions).

### Connection length

The Josephson coupling J sets the phase stiffness. Combined with the inter-cell distance l_cell, the texture has a Josephson length:

    lambda_J = l_cell * sqrt(J / E_elastic)

where E_elastic is the on-site elastic energy cost of deforming the condensate. For J/E_elastic >> 1, lambda_J >> l_cell and the texture is smooth (long-range correlated). For J/E_elastic << 1, lambda_J << l_cell and the texture is uncorrelated (white noise).

The rho_s tensor provides the elastic cost. From W3-4:

    E_elastic ~ rho_s * (Delta_phi / l_cell)^2 * l_cell^8

The power spectrum depends on the ratio rho_s / J, which determines the correlation length of the texture.

---

## 4. The Power Spectrum

### Gaussian random texture

For a texture field phi(r) produced by the Kibble-Zurek mechanism, the standard result (Paper 14, Eq. 5-8; Paper 02, Sec. 4.3; Zurek 1985) is a Gaussian random field with correlation function:

    <phi(r) phi(r')> = sigma^2 * exp(-|r-r'|^2 / (2*xi_KZ^2))

This gives a power spectrum:

    P_phi(K) = sigma^2 * xi_KZ^d * (2*pi)^{d/2} * exp(-K^2 * xi_KZ^2 / 2)

For K * xi_KZ << 1: P_phi(K) ~ const (scale-invariant, n_s = 1)
For K * xi_KZ >> 1: P_phi(K) ~ exp(-K^2 * xi_KZ^2 / 2) (suppressed)

**This is the Harrison-Zeldovich spectrum (n_s = 1) on scales larger than xi_KZ.**

The near-scale-invariance follows from a deep principle: the Kibble-Zurek mechanism produces domains of random, uncorrelated orientations. A collection of uncorrelated domains has a white-noise power spectrum in configuration space. In Fourier space, white noise is P(K) ~ const, which corresponds to n_s = 1. The red tilt (n_s < 1) must come from correlations BETWEEN domains -- i.e., from the Josephson coupling J and the stiffness rho_s.

### Correction from inter-domain coupling

When the Josephson coupling is turned on, the free energy of the texture is:

    F[phi] = Sum_{<ij>} (rho_s / 2) * (phi_i - phi_j)^2 / l_cell^2  +  V(phi_i)

where V is the on-site potential (from anisotropy energy in 3He, from the spectral action here). The partition function Z = integral D[phi] exp(-F/T_eff) gives the correlation function:

    <|phi_K|^2> = T_eff / (rho_s * K^2 + m^2)

where m^2 = d^2V/dphi^2 is the mass from the on-site potential. This is the ORNSTEIN-ZERNIKE form (Paper 01, Ch. 6.2; Paper 37, Sec. 3):

    P(K) ~ 1 / (K^2 + m^2)    =>    n_s = 1 - 2 * (K*xi)^2 / (1 + (K*xi)^2)

For K*xi << 1 (super-Hubble modes), n_s = 1 (scale-invariant).
For corrections at finite K*xi, n_s = 1 - 2*(K*xi)^2 to leading order.

**The red tilt comes from the K^2 dependence of the stiffness.**

For n_s = 0.965 at the pivot scale K_pivot:

    0.035 = 2 * (K_pivot * xi)^2    =>    K_pivot * xi = 0.132

This is a specific prediction: the Kibble-Zurek length xi and the pivot scale K_pivot must satisfy this relationship. In the framework:

- K_pivot = 0.05 Mpc^{-1} (Planck pivot scale)
- xi_KZ in physical units: from s42_fabric_wz.npz, xi_KZ_MKK = 0.269, and M_KK ~ 10^{19} GeV ~ 10^{-35} m
- xi_KZ ~ 0.269 * 10^{-35} m ~ 10^{-35} m ~ 10^{-61} Mpc

So K_pivot * xi_KZ ~ 0.05 * 10^{-61} ~ 10^{-63}. This is catastrophically far from the required 0.132.

### The Scale Hierarchy Problem (Again)

The Ornstein-Zernike spectrum gives the RIGHT shape (n_s = 1 - corrections) but the WRONG scale. The Kibble-Zurek length on the internal manifold is Planck-scale, while the CMB pivot scale is Hubble-scale. The ratio K_pivot * xi_KZ ~ 10^{-63} means the texture is white noise at all observable scales.

**This is the same 56-order suppression identified in the transfer function (S46) and confirmed in NS-REASSESS-47 Sec. 4.** The texture spectrum approach does NOT circumvent this hierarchy.

### Can the Tessellation Circumvent the Hierarchy?

The 32-cell tessellation operates at a DIFFERENT scale: the cell size R_cell ~ 4488 Mpc (physical, from s42_fabric_wz.npz). This is comparable to the Hubble radius (14250 Mpc). If the texture spectrum is defined over the TESSELLATION cells (not the internal manifold), then:

    K_pivot * l_cell ~ 0.05 * 4488 = 224

This is K*l >> 1, meaning the CMB pivot scale is INSIDE a single cell, well below the tessellation scale. The tessellation texture P(K) has support only at K < 2*pi/l_cell ~ 0.0014 Mpc^{-1}, far below the Planck pivot scale.

**The tessellation cells are TOO LARGE to produce CMB-scale perturbations.**

### The Structural Obstruction

The texture spectrum approach has a scale problem in BOTH directions:

1. Internal (KK) texture: xi_KZ ~ 10^{-61} Mpc, white noise at K_pivot = 0.05 Mpc^{-1}
2. External (tessellation) texture: l_cell ~ 4500 Mpc, structure only at K < 0.001 Mpc^{-1}

The CMB pivot scale sits in the gap between these two scales. Neither the internal texture nor the external tessellation produces structure at the right scale.

---

## 5. Honest Assessment: Does This Path Have a Structural Obstruction?

**Yes.** The texture spectrum approach, as formulated above, has the SAME scale hierarchy problem that killed the transfer function route (S46) and the inter-cell propagation route (NS-REASSESS-47 Sec. 4). The problem is not computational but physical: there is no mechanism in the framework to generate spatial correlations at the CMB scale from either internal (Planck-scale) or external (Hubble-scale) physics.

In 3He, this problem does not arise because there is only one spatial scale: the superfluid occupies a laboratory vessel, and the texture covers the entire vessel. The correlation length, domain size, and experimental probe all operate at the same scale (micrometers to centimeters). The 56-order gap between internal and external scales is unique to the cosmological setting.

**However**: there is one channel that the above analysis does NOT address. The analysis assumes the texture is produced by the Kibble-Zurek mechanism operating on the internal manifold. But the S38 result shows that the quench is a 0D process (L/xi_GL = 0.031) -- the entire internal space is ONE coherent domain. There is no internal texture. The texture, if it exists, must be generated by a DIFFERENT mechanism operating at a different scale.

### The Intermediate Scale Channel

The framework has three scales:
- M_KK ~ M_Pl ~ 10^{19} GeV (internal)
- M_BCS ~ E_cond ~ 0.14 M_KK ~ 10^{18} GeV (pairing)
- H_inf ~ 10^{13} GeV (inflation)

The ratio M_BCS / H_inf ~ 10^5. If the texture is generated not by internal Kibble-Zurek but by the dynamical interplay between BCS pairing and inflationary expansion, the correlation length could be set by the BCS coherence length in PHYSICAL (4D) space:

    xi_BCS_phys = v_F / Delta_BCS

where v_F is the "Fermi velocity" in the 4D emergent spacetime and Delta_BCS is the pairing gap. In the framework:

- Delta_BCS = 0.732 M_KK (B2 gap)
- v_F is set by the emergent Lorentz invariance (c_fabric = 1, from s42_fabric_dispersion.npz)

So xi_BCS_phys = 1 / Delta_BCS ~ 1.37 M_KK^{-1} ~ 1.37 * l_Pl.

This is still Planck-scale. The BCS coherence length does not bridge the gap.

### What Would Be Needed

For the texture spectrum to produce n_s = 0.965 at K_pivot = 0.05 Mpc^{-1}, one needs a correlation length:

    xi_texture = 1 / (K_pivot * sqrt(0.035/2)) = 1 / (0.05 * 0.132) = 151 Mpc

This is a specific, falsifiable number: the texture correlation length must be 151 Mpc. No known mechanism in the framework produces this scale. It would need to come from a NEW scale -- perhaps the sound horizon at the BCS transition, or a secondary instability of the GGE relic.

---

## 6. Revised Plan: What IS Computable

Given the structural obstruction, the original plan (compute the texture power spectrum and extract n_s) would produce a trivially white-noise result. Instead, I propose a more targeted computation:

### TASK 1: TEXTURE-CORR-48 (Volovik + Landau)

**What**: Compute the phase-phase correlation function of the BCS condensate between tessellation cells, using the Josephson coupling derived from the rho_s tensor and the condensate profile.

**Input**: s47_rhos_tensor.npz, s47_condensate_torus.npz, s46_fabric_tessellation.npz
**Method**: (a) Compute J_{ij} = overlap integral of condensate wavefunctions between cells i and j, weighted by rho_s. (b) Construct the N_cell x N_cell correlation matrix C_{ij} = <phi_i phi_j> from the inverse of the stiffness matrix. (c) Diagonalize to find the eigenspectrum of the correlation matrix.

**Output**: C_{ij} matrix, its eigenspectrum, and the implied P(K) for the tessellation-scale texture.

**Pre-registered gate**:
- PASS: P(K) has a non-trivial K-dependence (not white noise) with slope in [-3, 0]
- INFO: P(K) is trivially white or trivially peaked at K=0
- FAIL: Computation cannot be completed (missing data)

**Expected result**: INFO. The tessellation scale is 4500 Mpc, far from K_pivot = 0.05 Mpc^{-1}. The correlation matrix will likely show nearest-neighbor correlations decaying over 1-2 cell spacings.

### TASK 2: SCALE-BRIDGE-48 (Volovik + Tesla-Resonance)

**What**: Identify all possible intermediate scales in the framework that could produce a texture at the CMB scale.

**Input**: All session data S35-S47.
**Method**: Systematic enumeration of all energy/length scales in the framework, their physical origin, and whether any combination produces 151 Mpc.

**Output**: Table of scales with assessment of whether any bridges the hierarchy.

**Pre-registered gate**:
- PASS: A scale within factor 10 of 151 Mpc is identified with a physical mechanism
- FAIL: No scale within factor 100 of 151 Mpc exists in the framework

**Expected result**: FAIL. The framework's scales cluster at M_KK (Planck) and H_0^{-1} (Hubble), with no known intermediate.

### TASK 3: ACOUSTIC-HORIZON-48 (Volovik + Hawking)

**What**: Compute the acoustic horizon at the BCS transition -- the distance sound can travel in the emergent spacetime from the onset of BCS pairing to the end of transit.

**Input**: c_fabric = 1 (s42_fabric_dispersion.npz), transit duration from S38, BCS gap evolution from S46.
**Method**: d_acoustic = integral c_s(t) dt over the transit, where c_s is the sound speed in the BCS condensate. In 3He, the second sound speed is c_2 = c_s * sqrt(rho_n / rho_s) (Paper 01, Ch. 6; Paper 37, Sec. 2). In the framework, the analog is the speed of phase fluctuations.

**Output**: d_acoustic in physical units, compared to 151 Mpc.

**Gate**: Same as SCALE-BRIDGE-48 (is d_acoustic within factor 10 of 151 Mpc?).

**Expected result**: d_acoustic ~ l_Pl * (N_transit_steps). If N_transit ~ 10^5 (omega_att * t_transit), d_acoustic ~ 10^5 * l_Pl ~ 10^{-30} m ~ 10^{-56} Mpc. FAIL by 58 orders.

---

## 7. Gate Pre-Registration

### Gate: TEXTURE-NS-48

**The honest pre-registration**: This gate CANNOT PASS given the scale hierarchy.

The texture spectrum approach, the last identified path from the superfluid analogy, has the same structural obstruction as all previous fabric-level approaches: the internal scale (M_KK) and the external scale (R_cell) bracket the CMB pivot scale with a 56-order gap on the small side and a factor-100 gap on the large side. No known mechanism in the framework bridges either gap.

**What I propose instead**: Gate TEXTURE-NS-48 should test whether the SHAPE of the texture power spectrum (independent of overall scale) is compatible with n_s ~ 0.965 once a scale is assumed. This separates the scale problem (unsolved) from the tilt problem (testable).

- PASS: Given xi_texture = 151 Mpc (assumed), the texture power spectrum from rho_s anisotropy and Josephson coupling has the Ornstein-Zernike form with n_s in [0.93, 0.99]
- INFO: The Ornstein-Zernike form gives n_s = 1 exactly (white noise at all scales) or the computation reveals a different functional form
- FAIL: The texture spectrum has n_s < 0.5 or n_s > 1.5 even after scale adjustment

**My prediction**: INFO. The Ornstein-Zernike form P(K) ~ 1/(K^2 + m^2) gives n_s = 1 - 2*(K*xi)^2, which for any xi = 151 Mpc and K_pivot = 0.05 Mpc^{-1} gives n_s = 1 - 0.035 = 0.965 BY CONSTRUCTION. The shape is trivially correct because it is the generic result for any Gaussian random field with an exponential correlation function. The physics is in the SCALE, not the shape.

---

## 8. Summary Assessment

The texture spectrum approach, the sole surviving path from my NS-REASSESS-47 assessment, encounters a structural scale hierarchy that I should have identified earlier. The hierarchy was already visible in S46 (56-order transfer function suppression) and was re-confirmed in NS-REASSESS-47 Sec. 4 (inter-cell propagation). My error was in failing to recognize that the texture spectrum IS the inter-cell propagation -- same physics, same obstruction, different name.

The n_s crisis is now deeper than any single-mechanism failure. It is a SCALE crisis: the framework has no spatial scale between the Planck length and the Hubble radius that could serve as the Kibble-Zurek correlation length for CMB perturbations. This is not a fine-tuning problem -- it is the absence of a mechanism.

**What this means for the framework**: n_s requires physics that generates correlations at 151 Mpc. This could come from:
1. A secondary instability of the GGE relic at a macroscopic scale (no known mechanism)
2. Coupling between the internal BCS transition and the external expansion (the Friedmann-BCS channel, S38, shortfall 38,600x)
3. A completely different origin of perturbations (not from the BCS transition at all)

The three tasks above (TEXTURE-CORR, SCALE-BRIDGE, ACOUSTIC-HORIZON) are designed to confirm this assessment computationally and close the texture path definitively, or to reveal an unexpected intermediate scale that I have missed.

---

## 9. Files and Data Available

| File | Contents | Relevant keys |
|:-----|:---------|:-------------|
| s47_rhos_tensor.npz | Superfluid density tensor (8x8) at 16 tau values | rho_s_fold, rho_s_all, tau_sweep |
| s47_condensate_torus.npz | BCS condensate on T^2, 200x200 grid | (check keys) |
| s46_fabric_tessellation.npz | Tessellation structure, xi_KZ, N_domains | xi_KZ=0.152, N_domains=32, L_total=4.864, k_grid, M_k |
| s42_fabric_wz.npz | Fabric wall structure, physical scales | R_cell_Mpc=4488, xi_KZ_MKK=0.269, delta_tau_KZ=0.00166 |
| s42_fabric_dispersion.npz | Fabric dispersion, c_fabric=1 | c_fabric_value=1, E_fold, Delta_fold |

### Missing data (needs computation):
- Josephson coupling J_{ij} between tessellation cells (not yet computed)
- Condensate overlap integrals between adjacent cells
- Sound speed in the BCS phase as function of tau
- Transit duration in physical units

---

## 10. Agents and Assignments

| Task | Agent(s) | Input | Output | Format |
|:-----|:---------|:------|:-------|:-------|
| TEXTURE-CORR-48 | Volovik + Landau | s47_rhos_tensor, s47_condensate_torus, s46_fabric_tessellation | C_{ij}, P(K), eigenspectrum | s48_texture_corr.npz |
| SCALE-BRIDGE-48 | Volovik + Tesla | All session data | Scale table with assessments | table in working paper |
| ACOUSTIC-HORIZON-48 | Volovik + Hawking | s42_fabric_dispersion, S38 transit data | d_acoustic in Mpc | s48_acoustic_horizon.npz |

---

## References

- Paper 01, Ch. 7.3: Texture formation in 3He-A, domain structure, l-vector correlations
- Paper 01, Ch. 6.2: Second sound, Ornstein-Zernike correlations
- Paper 02, Sec. IV: Kibble-Zurek mechanism, defect formation in superfluid phase transitions
- Paper 14, Sec. I-III: Topological defects, domain walls, cosmic string analogs, defect power spectrum
- Paper 22: Elasticity tetrads, strain = curvature, phonon coupling to metric
- Paper 27: Non-equilibrium vacuum, phonon production during quench, vortex dynamics
- Paper 37: Two-fluid model, superfluid density, second sound in de Sitter
- Zurek 1985: Kibble-Zurek mechanism, domain size scaling
- S38: Transit dynamics, P_exc=1.000, GGE relic, 0D limit
- S42: 32-cell tessellation, fabric scales
- S46: Transfer function 56-order suppression, n_s crisis
- S47 W3-4: rho_s tensor, 24x anisotropy, curvature anti-correlation
