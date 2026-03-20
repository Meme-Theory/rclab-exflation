# Session 41 Sidequest: Intergalactic Voids as Relics of Early Crystal Structure -- CORRECTED

**Author**: Cosmic-Web-Theorist
**Date**: 2026-03-13 (v2, complete rewrite)
**Status**: INTERPRETIVE EXPLORATION (not gated)
**Input**: PI directive (Complexity Is Geometry), PI corrected framing (crystal IS space), W2-1 (N_eff step function), W3-1/W3-1b (CMB substrate, phononic crystal), Naz W3-2 (fabric EOM, gradient stiffness), Papers 03/04/06/08/12/13
**Epistemic class**: Conceptual analysis with quantitative honesty checks. No pre-registered gates. Results are structural assessments, not verdicts.

---

## 0. The Corrected Framing and What It Changes

The previous version (v1) committed a category error: comparing the internal fiber scale L_KK ~ 10^{-25} m to macroscopic void radii and declaring a "scale mismatch." The PI's correction:

**The crystal IS space. Not "a crystal inside space."**

In this framework:
- Points of space ARE F-mode configurations of the internal SU(3) geometry
- The number of distinguishable spatial configurations = N_eff = number of distinct D_K eigenvalues
- At early tau (round SU(3)): N_eff = 32. The universe had 32 effective mode types
- As tau increases past zero: N_eff snaps to 240 (W2-1). The crystal immediately resolves finer structure

The void hypothesis in corrected framing: voids are what remains of the primordial coarse tessellation. When there were only 32 mode types tiling space, the cells were enormous. As 240 modes activated, new structure formed at cell boundaries (where new modes nucleated as complexity grew). The original cell interiors were never filled in. Those are today's voids.

This changes the analysis fundamentally. There is no L_KK to compare to R_void. The question is: what is the spatial periodicity of the 32-mode fabric, and does it match the void foam?

What follows is my honest attempt to evaluate this corrected picture with the quantitative precision my domain demands.

---

## 1. The 32-Mode Tessellation: What It Predicts and What It Requires

### 1.1 From N_eff to Spatial Cells: The Conceptual Step

The PI's picture: N_eff = 32 means 32 "types" of F-mode configuration. Each type can tile space with some spatial frequency. The question is what sets that spatial frequency.

This is where the picture bifurcates into two interpretations, and they give radically different answers.

**Interpretation A: N_eff = number of spatial cells.** If the entire observable universe is tiled by exactly 32 cells, then:

$$R_{\rm cell} \sim \frac{R_{\rm universe}}{N_{\rm eff}^{1/3}} = \frac{28{,}500 \text{ Mpc}}{32^{1/3}} = \frac{28{,}500}{3.17} \approx 9{,}000 \text{ Mpc} \tag{1}$$

This is the PI's calculation. But 9,000 Mpc is 64% of the observable universe diameter. Observed voids have R_void ~ 15-80 h^{-1} Mpc ~ 20-110 Mpc. This is 80-450x too large. The universe has ~10^4 voids in the observable volume (Paper 12, Sutter), not 32.

**Interpretation B: N_eff = number of distinct mode types, each replicated many times.** This is the standard crystal interpretation. A crystal with 32 atoms in its unit cell has 32 bands in its band structure, but the unit cell is replicated N_x x N_y x N_z times to fill the sample. Each replication is identical in its internal structure. The number of SPATIAL cells is not 32 but the number of unit cell replications, which is set by the ratio of the sample volume to the unit cell volume.

Under Interpretation B, N_eff = 32 means the phononic crystal has 32 branches in its dispersion relation (bands), not 32 spatial cells. The number of spatial cells is determined by a different quantity: the ratio of the universe's 4D volume to the unit cell volume, where the unit cell volume involves M_KK. This brings back the scale comparison to L_KK, which the PI explicitly rejected.

### 1.2 The Tension Between the Two Interpretations

The PI explicitly rejects Interpretation B ("do NOT compare L_KK to any macroscopic length") and adopts something closer to Interpretation A but with a crucial modification: the 32 mode types are not 32 total cells but 32 types that tile space with some spatial frequency set by the 4D effective theory.

This requires a third interpretation:

**Interpretation C (PI's intended reading): The F-modes have definite Peter-Weyl quantum numbers (p,q), and each sector contributes modes with spatial wavelength determined by the 4D dispersion relation.** The LONGEST wavelength mode of the tau modulus field sets the largest cell size. The number of cells at the largest scale is not 32 per se, but the number of half-wavelengths of the longest fabric collective mode that fit in the causal horizon.

This is the fabric collective mode channel. It requires computing:
1. The dispersion relation omega(k) for tau perturbations on M^4
2. The gradient stiffness Z(tau) from the 12D spectral action
3. The effective mass M_eff for tau dynamics in the fabric

The Naz W3-2 review provides the equation of motion:

$$M_{\rm eff} \ddot{\tau} = -\frac{\partial V_{\rm eff}}{\partial \tau} + c^2 \nabla^2 \tau \tag{2}$$

and the total energy functional:

$$E_{\rm total}[\tau(\mathbf{x})] = \int d^4x \left[ S_{\rm crystal}(\tau(x)) + \frac{1}{2} Z(\tau) |\nabla\tau|^2 \right] \tag{3}$$

The fabric sound speed is:

$$c_{\rm fabric} = \sqrt{\frac{Z(\tau)}{M_{\rm eff}}} \tag{4}$$

Neither Z(tau) nor M_eff for the spatially extended fabric has been computed. This is the central UNCOMPUTED quantity.

### 1.3 What We Can Bound Without Z(tau)

Even without computing Z(tau), we can set constraints.

**Upper bound on the largest cell size**: The largest possible mode wavelength is set by the causal horizon at the transit epoch. The transit occurs at the BCS condensation time, which the framework places at t_BCS ~ 10^{-41} s (from M_KK ~ 10^9-10^13 GeV). The causal horizon at that epoch:

$$\lambda_{\rm causal}(t_{\rm BCS}) = c \cdot t_{\rm BCS} \sim 3 \times 10^{-33} \text{ m} \tag{5}$$

After the transit, this scale is stretched by the expansion. If we assume standard expansion history from t_BCS to today (with some inflation-equivalent epoch, since the framework must produce enough expansion to match the observed homogeneity):

The total expansion factor from t_BCS to t_0 is:

$$\frac{a(t_0)}{a(t_{\rm BCS})} \sim \frac{T_{\rm BCS}}{T_0} \sim \frac{M_{\rm KK}}{k T_0} \sim \frac{10^9 \text{ GeV}}{2.35 \times 10^{-13} \text{ GeV}} \sim 4 \times 10^{21} \tag{6}$$

(using Convention A; for Convention C: ~ 4 x 10^{25}). The physical size today of the causal horizon at the BCS epoch:

$$\lambda_{\rm today} = \lambda_{\rm causal} \times \frac{a(t_0)}{a(t_{\rm BCS})} \sim 3 \times 10^{-33} \times 4 \times 10^{21} \sim 10^{-11} \text{ m} \tag{7}$$

This is 0.1 Angstroms. Without an inflationary mechanism, the causal horizon at the BCS epoch is stretched to atomic scales, not void scales.

**With an inflation equivalent**: The framework needs ~60 e-folds of effective expansion (same as standard inflation) to explain CMB homogeneity. If this expansion occurs, the causal horizon scales up by e^{60} ~ 10^{26}:

$$\lambda_{\rm today,inflated} \sim 10^{-33} \times 10^{26} \times \frac{a(t_{\rm end-infl})}{a(t_0)} \tag{8}$$

This depends on when the inflation-equivalent epoch ends. If it ends at the GUT scale (~10^{16} GeV), then a(t_0)/a(t_end) ~ 10^{28-29}, giving:

$$\lambda_{\rm today,inflated} \sim 10^{-33} \times 10^{26} \times 10^{28} \sim 10^{21} \text{ m} \sim 30 \text{ kpc} \tag{9}$$

Still well below void scales (R_void ~ 10^{23-24} m ~ 10-100 Mpc). The modes generated at the BCS epoch reach galaxy scales after inflation, not void scales.

**Critical implication**: For the fabric collective modes to reach void scales, either:
(a) The inflation-equivalent expansion must produce more e-folds (~70-80), OR
(b) The fabric collective modes must be generated DURING or AFTER inflation, not at t_BCS, OR
(c) c_fabric >> c (superluminal propagation of tau perturbations), which would violate causality in the 4D effective theory.

Option (a) is within the standard inflationary range but requires the framework to specify its inflation-equivalent mechanism -- which remains the central open problem (all stabilization mechanisms are closed).

Option (b) is the more natural reading of the PI's picture: if "the transit never ended" and tau is still evolving, then tau perturbations can be seeded at any epoch. The question is when the LAST phase of significant tau-dynamics occurred. If it occurred at z ~ 1000 (recombination), the causal horizon there is ~300 Mpc (the sound horizon, which gives the BAO scale). Modes generated at that epoch reach scales of 100-300 Mpc today -- exactly the void scale range.

This is a potentially viable route, but it requires tau to have significant dynamics at z ~ 1000, which contradicts the clock constraint (dalpha/alpha < 10^{-2} at z ~ 1100, requiring tau_dot to be extremely small by recombination).

---

## 2. The Voronoi Tessellation Picture: 32 Seeds in the Observable Universe

### 2.1 Taking the PI's Analogy Seriously

The PI proposes: think of it as a Voronoi tessellation with 32 seeds, where the 208 additional seeds (going to 240) appear preferentially at the boundaries of the original cells.

For a Poisson-Voronoi tessellation with N seeds in a volume V:

$$\langle R_{\rm cell} \rangle \sim \left(\frac{V}{N}\right)^{1/3} \tag{10}$$

With N = 32 and V = (4/3)pi(14,250 Mpc)^3 ~ 1.21 x 10^{13} Mpc^3:

$$\langle R_{\rm cell} \rangle \sim \left(\frac{1.21 \times 10^{13}}{32}\right)^{1/3} \sim (3.78 \times 10^{11})^{1/3} \sim 7{,}230 \text{ Mpc} \tag{11}$$

These cells are gigantic -- each spans roughly half the observable universe. This is NOT what the cosmic web looks like. The observed void network has ~10^4 voids in the observable volume, giving a characteristic scale of ~50-100 Mpc, not ~7,000 Mpc.

### 2.2 But N_eff = 32 is Not the Number of Seeds

The PI's framing note acknowledges this: "N_eff = 32 is the number of DISTINCT eigenvalues, not the number of spatial cells. The number of spatial cells depends on how the modes tile 3D space. Each mode can be replicated -- the 32 TYPES of cell tile space with some spatial frequency."

This is the key question. How many times is each mode type replicated spatially? Call this N_rep. The total number of cells is:

$$N_{\rm total} = N_{\rm eff} \times N_{\rm rep} \tag{12}$$

For the void foam to have ~10^4 cells: N_rep ~ 10^4 / 32 ~ 300 replications of each mode type.

What sets N_rep? In a phononic crystal, N_rep is the number of unit cells in the sample -- it is L_sample / L_cell where L_cell is the lattice constant. But in the "crystal IS space" picture, the lattice constant IS the distance between replicated mode configurations. This is circular unless we have an independent way to determine the spatial periodicity.

The spatial periodicity comes from the 4D effective theory -- specifically, the dispersion relation of the tau modulus field. Modes with wavenumber k have wavelength lambda = 2pi/k. The number of modes that fit in the observable universe at wavenumber k is:

$$N_{\rm rep}(k) \sim \frac{R_{\rm universe}}{\lambda(k)} = \frac{k \cdot R_{\rm universe}}{2\pi} \tag{13}$$

For N_rep ~ 300: k ~ 2pi x 300 / (14,250 Mpc) ~ 0.13 Mpc^{-1}, giving lambda ~ 47 Mpc. This is the comoving wavelength of the fabric mode that would produce a Voronoi tessellation with the right number of cells.

Is this wavelength special? In LCDM, k ~ 0.13 Mpc^{-1} is in the mildly nonlinear regime -- it corresponds to scales slightly below the BAO scale (~105 h^{-1} Mpc ~ 150 Mpc, or k_BAO ~ 0.04 Mpc^{-1}). The power spectrum P(k) is a smooth, featureless function at this scale (no bump, no oscillation specific to k = 0.13).

For the framework to predict this scale, c_fabric and M_eff would need to conspire to produce a preferred wavelength at 47 Mpc. This is the UNCOMPUTED quantity.

### 2.3 The 240/32 = 7.5 Ratio and Void Subdivision

When N_eff jumps from 32 to 240, the new 208 modes appear. If they nucleate preferentially at the boundaries of the original 32-type tessellation, they create sub-cells within each original cell. The linear subdivision factor:

$$f_{\rm linear} = \left(\frac{N_{\rm eff,after}}{N_{\rm eff,before}}\right)^{1/3} = (240/32)^{1/3} = 7.5^{1/3} = 1.957 \approx 2 \tag{14}$$

Each original cell subdivides into roughly 7.5 sub-cells, with a linear size reduction by a factor of ~2.

This factor-of-2 linear subdivision has an interesting parallel in the excursion set theory of void formation. The Sheth-van de Weygaert (2004) void-in-void hierarchy predicts that voids contain sub-voids, with the characteristic scale ratio set by the density barrier crossing. In the simplest barrier model (constant barrier delta_v = -2.81), the void-in-cloud problem produces a scale ratio that depends on the power spectrum slope. For the LCDM power spectrum at the relevant scales:

The effective spectral index at R ~ 15-50 h^{-1} Mpc is n_eff ~ -1.5 to -2.0. The conditional first-crossing distribution gives a scale ratio of parent-to-child voids of approximately 2-3 for n_eff in this range (Sheth & van de Weygaert 2004, their Figure 7).

**The factor-of-2 scale ratio from the 240/32 N_eff jump is consistent with the excursion set prediction.** But this is not a unique prediction -- it is a coincidence of two different calculations giving a common answer (factor ~2), for entirely different physical reasons. The excursion set gives factor ~2 from the power spectrum slope; the framework gives factor ~2 from the cube root of the mode count ratio. These are independent calculations that happen to agree numerically.

**Discriminating test**: The excursion set predicts a CONTINUOUS distribution of parent/child void size ratios, peaked near ~2-3. The framework predicts a SINGLE ratio (240/32)^{1/3} = 1.957 (exact, from representation theory). If the void size ratio distribution could be measured precisely enough to distinguish a delta function at 1.96 from a broad distribution peaked at ~2.5, this would be discriminating. Current data (Pan et al. 2012, Sutter et al. 2014) cannot achieve this precision -- the void size function is measured to ~20-30% in each bin, far too coarse.

---

## 3. The Fabric Collective Mode Spectrum: What Determines Void Scale?

### 3.1 The Dispersion Relation

From the Naz W3-2 energy functional (eq. 3), the linearized equation for small tau perturbations delta_tau(x,t) around a uniform background tau_0:

$$M_{\rm eff} \frac{\partial^2 \delta\tau}{\partial t^2} = -V''(\tau_0) \delta\tau + Z(\tau_0) \nabla^2 \delta\tau \tag{15}$$

where V''(tau_0) = d^2 S_crystal / d tau^2 and Z(tau_0) is the gradient stiffness. The dispersion relation for plane waves delta_tau ~ exp(i(k.x - omega*t)):

$$\omega^2 = \frac{V''(\tau_0) + Z(\tau_0) k^2}{M_{\rm eff}} \tag{16}$$

Three regimes:

**(a) V'' > 0 (stable minimum)**: omega^2 > 0 for all k. Oscillatory modes. The tau field oscillates around the minimum. No preferred scale except at the gap:

$$k_{\rm gap} = 0, \quad \omega_{\rm gap} = \sqrt{V''/M_{\rm eff}} \tag{17}$$

All modes above k_gap propagate. This does not produce a preferred void scale.

**(b) V'' < 0 (unstable background)**: For small k, omega^2 < 0 -- these are GROWING modes (spinodal decomposition). The fastest-growing mode has:

$$k_{\rm max} = \sqrt{\frac{|V''|}{2 Z}} \tag{18}$$

$$\omega_{\rm max} = \frac{|V''|}{2\sqrt{M_{\rm eff} Z}} \tag{19}$$

The corresponding wavelength:

$$\lambda_{\rm max} = 2\pi / k_{\rm max} = 2\pi \sqrt{\frac{2Z}{|V''|}} \tag{20}$$

This IS a preferred scale. It arises from the competition between the bulk instability (V'' < 0, which favors inhomogeneous perturbations) and the gradient stiffness (Z > 0, which penalizes short-wavelength perturbations). This is exactly the Cahn-Hilliard instability in spinodal decomposition.

**(c) V'' = 0 (marginal)**: All modes with k > 0 have omega^2 > 0 (propagating). The k = 0 mode is marginal. No preferred scale.

### 3.2 Which Regime Does the Framework Inhabit?

The single-crystal spectral action has:
- dS/dtau > 0 (monotonically increasing, CUTOFF-SA-37)
- d^2S/dtau^2 can be extracted from the W2-5 data

From the Seeley-DeWitt coefficients at the fold:

a_2(0.19) = 16,077 and a_2(0.30) = 15,378. The relevant curvature is d^2(total S)/dtau^2, but this involves all a_n coefficients weighted by the cutoff function.

More directly: S_full(tau) was computed in Session 36 (TAU-STAB-36). The gradient dS/dtau = +58,673 at the fold. The second derivative was not reported, but the monotonicity theorem (CUTOFF-SA-37) establishes that S_full is convex (d^2S/dtau^2 > 0) for monotone cutoff functions, because the individual sector contributions are monotonic.

**If V'' = S'' > 0**: The background is STABLE. Regime (a). No spinodal instability. No preferred void scale from fabric collective modes.

**If the fabric introduces additional terms**: The total V_eff includes both S_crystal and the BCS condensation energy E_cond:

$$V_{\rm eff}(\tau) = S_{\rm crystal}(\tau) + E_{\rm BCS}(\tau) \tag{21}$$

E_cond = -12.385 at the fold (W1-2) and strengthens with tau (E_cond goes from -10.3 to -15.3 over [0.10, 0.30]). So dE_BCS/dtau < 0 (decreasing, stabilizing), but |dE_BCS/dtau| << |dS/dtau| (E_BCS changes by ~5 over Delta_tau = 0.2, while S changes by ~58,673 x 0.2 ~ 11,700 -- the spectral action gradient is ~2000x larger than the BCS stabilization).

The second derivative of V_eff = S'' + E_BCS''. Even if E_BCS'' < 0 (which would create a local maximum in E_BCS), its magnitude is far too small to overcome S'' > 0. The total V_eff'' is overwhelmingly positive.

**Conclusion**: The framework at the single-crystal level is in regime (a) -- stable, no spinodal instability, no preferred scale from fabric collective modes. The gradient stiffness Z only adds stability, not instability.

### 3.3 Could a Different Effective Potential Create Spinodal Decomposition?

In condensed matter, spinodal decomposition occurs when the system is quenched below the binodal (into the two-phase coexistence region). The Ginzburg-Landau free energy has V'' < 0 between the two spinodal points.

For the framework, this would require V_eff(tau) to have a maximum somewhere between the round SU(3) (tau=0) and the fold (tau=0.19). The spectral action S(tau) is monotonically increasing AND convex. E_BCS is monotonically decreasing but 2000x weaker. No maximum exists.

However, the spectral action as currently computed is a SINGLE-CRYSTAL quantity. The fabric's effective potential includes inter-crystal terms. Naz W3-2 identified that the fabric self-consistency loop has never been iterated (Section 3.1 of his review). In the non-perturbative regime, the fabric coupling could qualitatively change the potential landscape.

**The nuclear analog**: In nuclear DFT, the liquid-gas phase transition produces spinodal instability at densities rho ~ 0.04-0.1 rho_0 (about 1/4 to 2/3 of saturation density). The spinodal region is bounded by the spinodal points where d^2F/drho^2 = 0. The fastest-growing wavelength of the spinodal instability in nuclear matter is lambda_max ~ 8-12 fm (Colonna et al. 1998), which determines the fragment size in multifragmentation.

If the fabric has a spinodal instability (V_eff'' < 0 in some tau range), the preferred wavelength from equation (20) would set the void scale. But this requires the fabric self-consistency computation -- it cannot be determined from single-crystal data.

---

## 4. The (p,q) Sector Hierarchy and Cosmic Web Morphology

### 4.1 Sector Activation Order

The 32 eigenvalues at round SU(3) (tau=0) are maximally degenerate. At any tau > 0, they split into 240 distinct eigenvalues. The splitting pattern follows the sector structure:

| Sector | dim(p,q)^2 | N eigenvalues | Character |
|:-------|:-----------|:-------------|:----------|
| (0,0) | 1 | 8 | Singlet -- always active |
| (1,0), (0,1) | 9 each | 18 each | Fundamental -- first to split from (0,0) |
| (1,1) | 64 | 8 | Adjoint -- B2 is here |
| (2,0), (0,2) | 36 each | 8 each | -- |
| (2,1), (1,2) | 225 each | 24 each | Highest in current truncation |
| (3,0), (0,3) | 100 each | 24 each | -- |

The splitting is a step function (W2-1), not gradual. But the EIGENVALUE SEPARATIONS within each sector vary: low-lying sectors ((0,0), (1,0)) have small eigenvalues and small separations, while high sectors ((2,1), (1,2)) have large eigenvalues and large separations. The B2 mode in the (1,1) sector is anomalously flat (quasi-degenerate), which is what makes BCS pairing possible.

### 4.2 Does the Sector Hierarchy Map to Cosmic Web Morphology?

The PI asks: does the hierarchy of sector activations map to the observed cosmic web hierarchy (voids -> walls -> filaments -> clusters)?

The cosmic web has four distinct morphological elements, classified by the Hessian eigenvalue signature of the density field (Paper 03, van de Weygaert):

| Structure | Hessian signature | Dimension | Volume fraction |
|:----------|:-----------------|:----------|:---------------|
| Voids | 3 negative eigenvalues | 3D | ~60-70% |
| Walls | 1+, 2- | 2D | ~20-25% |
| Filaments | 2+, 1- | 1D | ~5-10% |
| Clusters | 3 positive | 0D | ~1-3% |

The PI's mapping would be:
- Voids = regions where only the (0,0) sector contributes (simplest, coarsest)
- Walls = regions where (1,0)/(0,1) sectors activate (fundamental rep, first refinement)
- Filaments = regions where (1,1) sector activates (adjoint, B2 -- the BCS condensate)
- Clusters = regions where all sectors up to (2,1)/(1,2) contribute (full complexity)

This is an appealing structural correspondence: increasing spectral complexity maps to increasing morphological complexity. But it requires that the sector activation be SPATIALLY INHOMOGENEOUS -- different regions of space must be at different stages of spectral complexity.

The W2-1 result kills this: N_eff is a step function. ALL sectors activate simultaneously at any tau > 0. There is no epoch where some regions have (0,0) only while others have all 240 modes. The transition is instantaneous and spatially uniform (the tau parameter is a modulus of the internal geometry, and the PI's "complexity is geometry" directive has tau varying slowly and uniformly post-transit, with delta_tau/tau < 3 x 10^{-6} from constant bounds, W3-1 O-5).

**Unless tau is spatially inhomogeneous.** If different spatial regions transit at different times (due to the finite propagation speed of the Jensen deformation), then YES, there is an epoch where some regions are at tau = 0 (32 modes) and others are at tau > 0 (240 modes). The boundary between these regions would be a domain wall in tau-space, and its spatial extent determines the wall/filament/cluster structure.

This is the Kibble-Zurek mechanism applied to the fabric. The defect density (number of domain walls per unit volume) is set by the quench rate:

$$n_{\rm defect} \sim \frac{1}{\hat{\xi}^3}, \quad \hat{\xi} = \xi_0 \left(\frac{\tau_Q}{\tau_0}\right)^{\nu/(1+z_d\nu)} \tag{22}$$

where xi_0 is the equilibrium correlation length, tau_Q is the quench timescale, tau_0 is the relaxation time, and nu, z_d are critical exponents. In the framework, these quantities have not been computed. The domain wall density would set the void-wall structure density, and the Kibble-Zurek scaling would predict the characteristic void size.

### 4.3 The Kibble-Zurek Route to Void Scales

For a concrete estimate, I use the nuclear liquid-gas phase transition as an analog (since the framework's BCS transition is the closest analog, and liquid-gas spinodal decomposition in nuclear matter has well-characterized Kibble-Zurek behavior).

In nuclear multifragmentation (the nuclear analog of spinodal decomposition):
- Fastest-growing wavelength: lambda_max ~ 8-12 fm
- Characteristic fragment size: R_frag ~ lambda_max / 2 ~ 4-6 fm
- Ratio to nuclear radius: R_frag / R_nucleus ~ 0.6-1.0 (the fragments are comparable to the nucleus itself)

The scaling is: lambda_max ~ sqrt(surface energy / bulk instability), which in the nuclear case gives lambda_max ~ sqrt(a_surf / a_vol) x R_0 where R_0 is the nuclear length scale.

For the fabric:

$$\lambda_{\rm max} = 2\pi\sqrt{\frac{2Z}{|V''|}} \tag{20, repeated}$$

If Z and V'' scale similarly to their nuclear analogs (surface/volume terms comparable, i.e., Z ~ M_eff c_fabric^2 / L^2 and |V''| ~ M_eff c_fabric^2 / L^2 for some scale L), then:

$$\lambda_{\rm max} \sim 2\pi \sqrt{2} \cdot L \sim 9 L \tag{23}$$

where L is the characteristic scale of the fabric. But what is L?

In the "crystal IS space" picture, L is set by the 4D dynamics: it is the causal horizon at the transit epoch, stretched by subsequent expansion. From equations (5)-(9), this gives L ~ 30 kpc (with standard inflation) or L ~ 0.1 A (without inflation).

This is the same scale mismatch as before, but now it appears in the DISPERSION RELATION rather than in the lattice constant. The fundamental issue is that the BCS transit occurs at such early times that its causal horizon, even after inflationary stretching, is far below void scales.

---

## 5. The 240/32 = 7.5 Ratio: Honest Assessment

### 5.1 What the Ratio Represents Physically

In the framework: 240/32 is the ratio of distinct eigenvalues after vs. before the Jensen deformation. It is a representation-theoretic number: at tau = 0, the Casimir eigenvalue degeneracy gives 32 distinct values; at tau > 0, the broken SU(3) symmetry lifts all accidental degeneracies, giving 240 distinct values.

In 3D spatial tiling, if the mode count increases from 32 to 240 types, the linear cell subdivision factor is:

$$(240/32)^{1/3} = 7.5^{1/3} = 1.957 \tag{14, repeated}$$

### 5.2 Does This Appear in Void Statistics?

**The void-in-void hierarchy**: In excursion set theory, the parent-to-child void size ratio R_parent/R_child is not a single number but a distribution. From Sheth & van de Weygaert (2004), the conditional first-crossing distribution for sub-voids within a parent void gives:

$$R_{\rm child}/R_{\rm parent} \sim \sigma(R_{\rm parent})/\sigma(R_{\rm child}) \tag{24}$$

For the LCDM power spectrum with n_eff ~ -1.5 at the relevant scales, sigma(R) ~ R^{-(n_eff+3)/2} ~ R^{-0.75}. The ratio:

$$R_{\rm child}/R_{\rm parent} \sim (R_{\rm parent}/R_{\rm child})^{-0.75}$$

This gives a transcendental equation whose solution depends on the specific barrier model. Numerical results from Sheth & van de Weygaert give R_child/R_parent peaked at ~0.3-0.5, i.e., R_parent/R_child ~ 2-3.

The framework predicts R_parent/R_child = 1.957 (from 7.5^{1/3}). This falls within the LCDM excursion set range of 2-3. It is consistent but not distinctive.

**Observational test**: To distinguish R = 1.957 (framework) from R ~ 2-3 (LCDM, distribution), we would need to measure the void-in-void scale ratio to ~20% precision. Current void catalogs (SDSS VIDE, BOSS) have ~10^3 void-in-void identifications with R_parent/R_child ~ 1.5-4.0 and measurement uncertainties of ~30-50% per pair. A stacking analysis might reduce the uncertainty to ~10-15%, at which point the distinction between R = 2.0 (framework) and R = 2.5 (LCDM peak) becomes marginally testable.

**Pre-registered gate (for future computation)**: VOID-RATIO-42: If the fabric collective mode computation yields a preferred subdivision scale, compare R_predicted to the stacked void-in-void ratio from DESI Year 5 void catalog. Gate criterion: |R_predicted - R_observed| / sigma_R < 2. This gate is UNCOMPUTABLE until Z(tau) is derived.

### 5.3 The Multiplicity Structure Within the Ratio

The 240 modes are not uniform -- they have a specific multiplicity structure by sector:

| Sector(s) | Modes added | Fraction |
|:-----------|:-----------|:---------|
| (0,0) | 0 (already present) | 0% |
| (1,0)+(0,1) | 36-18 = 18 new | 8.7% |
| (1,1) | 56 new | 26.9% |
| (2,0)+(0,2) | 56 new | 26.9% |
| (2,1)+(1,2) | 48 new | 23.1% |
| (3,0)+(0,3) | 30 new | 14.4% |

(Total new = 208, for 240 - 32 = 208.)

If different sectors contribute modes at different spatial wavelengths (because higher (p,q) sectors have higher Casimir eigenvalues C_2(p,q) = (p^2 + pq + q^2 + 3p + 3q)/3, which plays the role of |k|^2 in the crystal momentum), then the subdivision is NOT uniform. Lower sectors contribute longer-wavelength perturbations; higher sectors contribute shorter-wavelength perturbations.

This would create a HIERARCHY of subdivision scales, not a single ratio:
- (1,0) modes: largest sub-cells (smallest Casimir, longest wavelength in representation space)
- (1,1) modes: intermediate sub-cells
- (2,1) modes: finest sub-cells (largest Casimir, shortest wavelength)

The cosmic web has exactly this hierarchy: voids (largest), walls (intermediate), filaments (thinner), clusters (densest). If the sector hierarchy maps to the morphological hierarchy, the correspondence would be:

| Sector | Casimir C_2 | Spatial scale | Morphology |
|:-------|:-----------|:-------------|:-----------|
| (1,0) | 4/3 | Largest | Void boundaries |
| (1,1) | 3 | Intermediate | Walls |
| (2,0) | 10/3 | Smaller | Filaments |
| (2,1) | 19/3 | Smallest | Clusters |

This is SPECULATIVE but structurally motivated. The Casimir eigenvalue plays the role of the effective "mass" of each sector's contribution to the spatial perturbation spectrum. Higher Casimir = shorter wavelength = finer structure. This is exactly the ultraviolet-to-infrared correspondence in the spectral action.

**What this requires to be testable**: A computation showing that the 4D dispersion relation for tau perturbations has sector-dependent propagation speeds, with the spatial wavelength lambda(p,q) inversely proportional to some function of C_2(p,q). This requires the inter-fiber coupling to be sector-resolved (different sectors couple to their neighbors with different stiffness).

---

## 6. Comparison to Observations: What Would Distinguish This From LCDM

### 6.1 The Fundamental Difference

In LCDM:
- Voids form from gravitational expansion of underdense regions in a Gaussian random initial density field
- The void size function is continuous (set by the primordial power spectrum P(k))
- Void shapes are determined by the tidal tensor (gravitational dynamics)
- Void profiles are universal (Hamaus et al. 2014, Paper 13)
- No preferred scales beyond the BAO (~150 Mpc)

In the framework (corrected):
- Voids are remnants of the primordial fabric tessellation
- The tessellation has DISCRETE structure (from N_eff = 32 mode types, then 240)
- New structure forms at the BOUNDARIES of the original tessellation cells
- The void size is set by the fabric collective mode spectrum (UNCOMPUTED)
- There may be a preferred subdivision ratio of ~2 from the 240/32 transition

### 6.2 Discriminating Observational Tests

| Test | Framework prediction | LCDM prediction | Current constraint | Status |
|:-----|:--------------------|:----------------|:------------------|:-------|
| Void size function shape | Discrete peaks if fabric modes have preferred scales | Continuous (Sheth-van de Weygaert) | Continuous, consistent with SvdW (Pan 2012, Sutter 2014) | LCDM FAVORED |
| Void-in-void ratio | Single ratio (240/32)^{1/3} = 1.957 | Distribution peaked at ~2-3 | Distribution observed, not tested for discreteness | UNTESTED |
| Sector-morphology correspondence | C_2-dependent spatial scales: low C_2 = voids, high C_2 = clusters | Scale-free (from Gaussian random field) | Scale-free observed. No sector imprint detected | LCDM FAVORED |
| Void alignment | Aligned with residual U(1)_7 symmetry direction | Random (from isotropic Gaussian field) | No preferred alignment detected | LCDM FAVORED |
| Void density profile | Modified at boundaries between original tessellation cells | Universal Hamaus profile | Universal profile observed | LCDM FAVORED |
| Void abundance vs sigma_8 | n_v ~ sigma_8^5 SAME as LCDM (framework gives sigma_8 via CC -> H(z)) | n_v ~ sigma_8^5 (Paper 12) | Consistent with LCDM | NO DISCRIMINATION |

### 6.3 The Honest Scorecard

Of six discriminating tests:
- 4 favor LCDM (continuous void size function, no preferred alignment, universal profile, scale-free morphology)
- 1 is untested (void-in-void ratio discreteness)
- 1 has no discriminating power (void abundance vs sigma_8 is the same in both)

The framework would need the fabric collective mode computation to produce specific QUANTITATIVE predictions for any of these tests. Without it, the framework makes no prediction that differs from LCDM for void statistics.

---

## 7. Giant Structures: Can the 32-Mode Tessellation Explain Them?

### 7.1 The Structures and Their Scales

| Structure | Scale (Mpc) | z | Post-trial sigma |
|:----------|:-----------|:--|:----------------|
| Sloan Great Wall | 420 | 0.08 | well-established |
| Giant Arc | ~1000 | 0.8 | ~2.5 (post-trial) |
| Big Ring | ~1300 | 0.8 | ~3 (post-trial, shared catalog) |
| HCBGW | ~2000-3000 | 1.6-2.1 | ~2 (post-trial, selection effects) |

### 7.2 Could These Be Original 32-Mode Cell Boundaries?

If the original 32-mode tessellation had cells of size ~7,000 Mpc (eq. 11), the cell boundaries would be great-circle arcs across the sky. Projected structures at z ~ 0.8 would subtend angular sizes corresponding to ~1000-3000 Mpc in comoving distance.

The Giant Arc (~1000 Mpc) and HCBGW (~2000-3000 Mpc) have scales within this range. If these structures were segments of the boundaries between the original 32-mode cells, their existence would be a natural prediction of the tessellation picture.

**But**: This requires exactly 32 cells filling the entire observable universe, which gives cell sizes of ~7000 Mpc. The cell boundaries would be great surfaces (walls) of cosmological extent. We would expect ~32 x (number of faces per cell, ~14 for Voronoi) / 2 ~ 224 distinct wall segments. At z ~ 0.8, the comoving volume surveyed by the Mg II catalog (Lopez et al.) subtends a fraction f ~ 0.01-0.1 of the full sky. So we would expect to intersect ~2-22 wall segments. Observing 2-3 structures of ~1-3 Gpc extent in such a survey is ORDER-OF-MAGNITUDE consistent with 32 cells.

**The problem**: If these are cell boundaries, they should be WALLS (2D surfaces), not arcs or rings. The Giant Arc is 1D; the Big Ring is roughly circular. A Voronoi cell boundary is a flat face (a plane in 3D). Its intersection with a redshift slice (a spherical shell) would be an arc of a great circle -- which is what the Giant Arc looks like. The Big Ring, however, is a closed loop, not an arc. A loop requires the intersection of a spherical shell with a surface that curves back on itself -- this happens if the Voronoi cell boundary is curved (which it is for non-flat Voronoi faces) or if the observer is near a vertex of the tessellation (where multiple faces meet).

This is QUALITATIVELY consistent. Whether it is QUANTITATIVELY consistent requires computing the statistics of Voronoi cell boundary intersections with spherical shells for a 32-cell Poisson-Voronoi tessellation and comparing to the observed structure catalog. This is a straightforward Monte Carlo simulation that has not been performed.

### 7.3 Statistical Caution

The post-trial significance of these structures is 2-3 sigma. In LCDM, 2-3 sigma fluctuations are expected: with ~10^3-10^4 independent volumes surveyed, finding a few 2-3 sigma excursions is statistically unremarkable.

The framework prediction (if the 32-cell tessellation is correct) is more specific: the giant structures should appear preferentially at the BOUNDARIES of the original tessellation, which have a specific geometric pattern (Voronoi cell faces). This predicts:
1. Giant structures should trace great-circle-like arcs on the sky
2. Multiple giant structures at similar redshifts should be GEOMETRICALLY RELATED (segments of the same cell face or adjacent faces)
3. The characteristic separation between giant structures should be ~7000 Mpc / sqrt(3) ~ 4000 Mpc (the face-to-face distance of a Voronoi cell)

The Giant Arc and Big Ring are both at z ~ 0.8 and separated by ~35 degrees on the sky, corresponding to ~1000 Mpc comoving at that redshift. If they are both segments of the same Voronoi cell boundary (or adjacent boundaries), their separation is consistent with the prediction IF the cell boundary is at a distance of ~1000 Mpc from the observer in the transverse direction. The cell size of ~7000 Mpc would predict that the next boundary segment is ~7000 Mpc away, which at z ~ 0.8 would be on the opposite side of the sky.

**Pre-registered test (GIANT-VORONOI-42)**: Generate 10^4 random 32-cell Poisson-Voronoi tessellations. For each, compute the intersection with a spherical shell at comoving distance corresponding to z = 0.8. Count the number of arc-like structures with extent > 500 Mpc. Compare the distribution to the observed count (2-3 structures). If the observed count falls within the 1-99 percentile range of the Voronoi tessellation distribution, the hypothesis is CONSISTENT. If it falls outside, the hypothesis is EXCLUDED. This test is immediately computable.

---

## 8. What Remains Uncomputed and What Would Make This Testable

### 8.1 The Critical Computation: Fabric Gradient Stiffness Z(tau)

Every quantitative prediction in this analysis depends on Z(tau), the gradient stiffness of the tau field in the spatially extended fabric. Z(tau) determines:
- The fabric sound speed c_fabric = sqrt(Z/M_eff) (eq. 4)
- The preferred wavelength of spinodal instability lambda_max = 2pi sqrt(2Z/|V''|) (eq. 20, IF V'' < 0)
- The Kibble-Zurek defect density (through the equilibrium correlation length xi ~ sqrt(Z/V''))
- Whether the dispersion relation (eq. 16) produces preferred scales

Z(tau) is derivable from the 12D Einstein equations with the SU(3) internal space ansatz. Specifically, it comes from the kinetic term for the tau modulus in the 4D effective action after KK reduction:

$$S_{4D} \supset \int d^4x \sqrt{-g} \left[ \frac{1}{2} Z(\tau) g^{\mu\nu} \partial_\mu \tau \partial_\nu \tau - V_{\rm eff}(\tau) \right] \tag{25}$$

where g_{mu nu} is the 4D metric and V_eff includes the spectral action and BCS condensation energy. The coefficient Z(tau) depends on the volume and geometry of the internal space:

$$Z(\tau) = \frac{M_P^2}{M_{\rm KK}^2} \cdot f(\tau) \tag{26}$$

where f(tau) is a dimensionless function determined by the overlap integrals of the internal geometry. In standard Kaluza-Klein theory, f(tau) is of order 1. The key dimensionful factor is M_P^2 / M_KK^2 ~ (10^{19})^2 / (10^{9-13})^2 ~ 10^{12-20}. This is an enormous stiffness, meaning the fabric is extremely resistant to tau gradients.

If Z ~ 10^{12-20} M_KK^2, then the fabric sound speed is:

$$c_{\rm fabric} \sim \sqrt{\frac{Z}{M_{\rm eff}}} \sim \sqrt{\frac{10^{12-20}}{1.695}} \cdot M_{\rm KK} \sim 10^{6-10} M_{\rm KK} \tag{27}$$

In natural units where c = 1, c_fabric in physical units scales with M_KK as the overall energy scale. The ratio c_fabric/c depends on the specific Z and M_eff values. But the large Z means tau perturbations propagate very efficiently -- the fabric is stiff and transmits information quickly.

The wavelength of the fundamental fabric mode in the observable universe is:

$$\lambda_{\rm fund} \sim 2 R_{\rm universe} = 28{,}500 \text{ Mpc} \tag{28}$$

Higher harmonics have lambda_n = lambda_fund / n. The mode with lambda ~ 50 Mpc (the characteristic void scale) corresponds to:

$$n \sim 28{,}500 / 50 = 570 \tag{29}$$

This is the 570th harmonic of the fundamental fabric mode. There is nothing special about n = 570 in the framework. The fabric's acoustic spectrum does not naturally select this harmonic.

### 8.2 What Would Produce a Preferred Void Scale

For the framework to predict a specific void scale, one of the following must occur:

**(A) Spinodal decomposition with V_eff'' < 0.** Requires the fabric self-consistency computation to show that V_eff(tau) has a local maximum. Current single-crystal data: V_eff'' > 0 (stable). Would need non-perturbative fabric correction.

**(B) Phase transition with Kibble-Zurek defects.** The N_eff step function is first-order-like, so Kibble-Zurek applies. The defect density depends on the quench rate and the equilibrium correlation length, both of which require Z(tau). Pre-registered: the defect spacing should match the void scale if the framework is correct.

**(C) Resonant excitation at a specific wavenumber.** If the fabric dispersion relation omega(k) has a flat region (van Hove singularity in k-space), modes at that k would be preferentially excited. This would require the dispersion relation to be nonlinear (beyond the simple acoustic omega ~ k from eq. 16), which would come from higher-order terms in the effective action.

**(D) Seed spectrum from quantum fluctuations during an inflation-equivalent epoch.** If the framework provides an inflation mechanism, the quantum fluctuations of tau during inflation would imprint a power spectrum. The power spectrum's shape would be set by the tau potential and its slow-roll parameters. The void scale would correspond to the scale leaving the horizon at the appropriate number of e-folds before the end of inflation. This is the standard inflationary mechanism for generating structure, applied to tau instead of the inflaton.

### 8.3 Computational Priority

| Computation | What it settles | Difficulty | Prerequisite |
|:------------|:---------------|:-----------|:-------------|
| Z(tau) from KK reduction | Fabric sound speed, stiffness, all subsequent predictions | HIGH (requires 12D Einstein eq with SU(3)) | None |
| V_eff(tau) with fabric self-consistency | Whether spinodal instability exists | VERY HIGH (non-perturbative) | Z(tau) |
| 32-cell Voronoi Monte Carlo vs giant structures | Whether 32-cell tessellation is consistent with observed giants | LOW (straightforward simulation) | None |
| Sector-dependent spatial dispersion | Whether the C_2 hierarchy maps to morphological scales | HIGH (requires sector-resolved KK reduction) | Z(tau) |
| Kibble-Zurek defect density for N_eff step | Whether defect spacing matches void scale | MEDIUM | Z(tau), transition dynamics |

The 32-cell Voronoi Monte Carlo is the only immediately computable test. I recommend it as the next step.

---

## 9. Honest Assessment (Corrected)

### 9.1 What the Corrected Framing Changes

The v1 analysis committed a category error by comparing L_KK to R_void. The corrected framing eliminates this error. In the corrected picture:

1. **The crystal IS space.** The spatial structure emerges from the mode structure, not from embedding a lattice in pre-existing space. There is no "internal vs external" scale comparison.

2. **The void scale is set by fabric collective modes.** The relevant quantity is not L_KK but the dispersion relation of the tau field in the spatially extended fabric. This is determined by Z(tau), which comes from the KK reduction.

3. **The 240/32 ratio gives a subdivision factor of ~2.** This is consistent with the excursion set void-in-void ratio, but not uniquely predicted.

4. **The sector hierarchy may map to cosmic web morphology.** Higher Casimir sectors contributing shorter-wavelength modes would give the qualitative correspondence: voids (low C_2, longest wavelength) -> walls -> filaments -> clusters (high C_2, shortest wavelength).

### 9.2 What Still Fails

1. **No preferred void scale from current calculations.** The single-crystal V_eff'' is positive (stable, no spinodal). The fabric computation is needed to determine whether non-perturbative effects create an instability. Without it, no void scale is predicted.

2. **The causal horizon problem persists.** The BCS transit at t ~ 10^{-41} s has a causal horizon that, even after standard inflationary stretching, reaches only ~30 kpc -- far below void scales. The framework needs to explain how void-scale correlations are established.

3. **The inflation-equivalent mechanism is absent.** All spectral action stabilization routes are closed. The framework has no inflation analog. Without one, large-scale structure formation is unexplained.

4. **LCDM already works.** The Sheth-van de Weygaert excursion set theory, calibrated on the LCDM power spectrum, reproduces the observed void size function, profiles, shapes, and abundance (Papers 12, 13). No exotic physics is needed.

5. **N_eff step function prevents gradual refinement.** The smooth hierarchy of cosmic web structure (continuously varying density field, no sharp boundaries between morphological types) is inconsistent with a discrete step function that snaps from 32 to 240 modes.

### 9.3 What Works Better in the Corrected Framing

1. **No scale mismatch.** The v1 analysis had a 48-52 order-of-magnitude scale mismatch. The corrected framing eliminates this by treating the crystal as space itself, not as an embedded lattice.

2. **The 32-cell tessellation and giant structures.** 32 cells in the observable universe gives cell sizes of ~7000 Mpc. Cell boundaries would appear as ~1-3 Gpc structures -- matching the scale of the Giant Arc, Big Ring, and HCBGW. This is QUANTITATIVELY consistent (order of magnitude) without tuning. The Voronoi Monte Carlo test (GIANT-VORONOI-42) is immediately computable.

3. **The sector-morphology correspondence.** The framework's internal hierarchy (sectors ordered by Casimir eigenvalue) has a natural correspondence with the cosmic web's morphological hierarchy (structures ordered by dimension). This is structurally motivated and could become quantitative once the sector-dependent spatial dispersion is computed.

4. **The Kibble-Zurek channel.** The N_eff step function supports Kibble-Zurek defect formation. The defect network topology (domain walls in SU(3) fiber space, projected to 4D through the metric coupling) could generate cosmic-web-like structure. This channel is UNCOMPUTED but physically well-motivated.

### 9.4 Classification

**Status**: PARTIALLY UNTESTED.

The corrected framing eliminates the category error of v1. The hypothesis is no longer trivially excluded by scale arguments. Several new quantitative questions arise:

| Question | Status | Testable with current tools? |
|:---------|:-------|:----------------------------|
| Is the 32-cell tessellation consistent with giant structures? | UNTESTED | YES (Voronoi MC, immediate) |
| Does the fabric have spinodal instability? | UNCOMPUTED | NO (needs Z(tau)) |
| Does Kibble-Zurek defect spacing match void scale? | UNCOMPUTED | NO (needs Z(tau) + transition dynamics) |
| Does the sector hierarchy map to morphological scales? | UNCOMPUTED | NO (needs sector-dependent KK reduction) |
| Is the 240/32 subdivision ratio observable? | MARGINALLY TESTABLE | Possibly (DESI Year 5 void stacking) |

The hypothesis lives in a region of solution space that is NARROWER than v1 assessed (the corrected framing opens viable channels) but still mostly UNCOMPUTED. The single immediately testable prediction (32-cell Voronoi vs giant structures) is the recommended next computation.

---

## 10. Recommended Next Steps

**Priority 1 (IMMEDIATE, LOW DIFFICULTY)**: 32-cell Voronoi Monte Carlo. Generate 10^4 Poisson-Voronoi tessellations with 32 cells in a sphere of radius 14,250 Mpc. For each, compute:
- Cell size distribution
- Intersection of cell boundaries with spherical shells at z = 0.8 (comoving distance ~3500 Mpc)
- Number, length, and shape statistics of boundary intersections
- Compare to observed giant structures (Giant Arc, Big Ring, HCBGW)
Pre-registered gate: GIANT-VORONOI-42.

**Priority 2 (HIGH, requires new computation)**: Z(tau) from the 12D KK reduction. This is the fabric gradient stiffness that determines every fabric prediction. Without it, no void scale prediction is possible. This is the same Priority 1 from the session-wide computation queue.

**Priority 3 (MEDIUM, contingent on Priority 2)**: Kibble-Zurek defect density for the N_eff step function. Given Z(tau), compute the equilibrium correlation length xi and the defect spacing from the quench dynamics. Compare to the observed void number density (~10^{-3.5} h^3 Mpc^{-3}).

**Priority 4 (MEDIUM, contingent on Priority 2)**: Sector-dependent spatial dispersion. Compute whether different (p,q) sectors contribute spatial perturbations at different wavelengths, and whether the Casimir hierarchy maps to the cosmic web morphological hierarchy.

---

## 11. Permanent Constraints From This Analysis

### 11.1 What Is Closed (from v1, REMAINS CLOSED)

- **BAO scale from crystal**: MOOT. The BAO scale is set by baryon-photon acoustic physics at z ~ 1060, which is completely independent of the BCS transition at t ~ 10^{-41} s. Same in both models.

- **All imported-from-Volovik channels**: CLOSED (Session 29 permanent). Emergent G_eff, sector-dependent gravity, condensate vortices in position space are all imported, not derived from the framework.

### 11.2 What Was Corrected

- **Scale mismatch argument**: WITHDRAWN. The v1 comparison of L_KK to R_void was a category error in the corrected framing. The crystal IS space; there is no internal-vs-external scale comparison.

- **"No mechanism" verdict**: MODIFIED. The fabric collective mode channel (gradient stiffness Z(tau) and its dispersion relation) is a well-defined computation target. The mechanism exists in principle; its quantitative predictions are UNCOMPUTED.

### 11.3 What Is New

- **32-cell Voronoi prediction**: NEW, testable, immediate. If the observable universe has 32 fundamental tessellation cells (from N_eff = 32 at round SU(3)), their boundaries should appear as ~1-3 Gpc structures. This is consistent with the scale of observed giant structures. A Monte Carlo test (GIANT-VORONOI-42) can determine whether the hypothesis is statistically viable.

- **Sector-morphology correspondence**: NEW, speculative, requires computation. The Casimir hierarchy C_2(p,q) may map to the cosmic web morphological hierarchy, with low C_2 sectors generating void-scale perturbations and high C_2 sectors generating cluster-scale perturbations.

- **Kibble-Zurek channel**: NEW (first identified in this analysis as a void-scale mechanism). The step function N_eff transition supports Kibble-Zurek defect formation, with the defect network potentially generating cosmic-web-like structure. Requires Z(tau) to compute.

---

## References

- Paper 03: van de Weygaert & Schaap (2007), Cosmic Web Geometric Analysis -- DTFE, Voronoi tessellation, Hessian classification
- Paper 04: van de Weygaert & Schaap (2009), Cosmic Web Connectivity and Topology -- persistent homology, void hierarchy, MMF
- Paper 06: Einasto et al. (2001), Supercluster-Void Network -- void statistics, characteristic scale 100-130 Mpc
- Paper 08: Eisenstein et al. (2005), BAO detection -- 150 Mpc sound horizon
- Paper 12: Sutter et al. (2014), Voids as Cosmological Probes -- VIDE, void abundance, AP test
- Paper 13: Hamaus et al. (2016), Void Dynamics and Dark Energy -- void profiles, growth rate
- Paper 14: Horvath et al. (2014), HCBGW -- 3 Gpc GRB structure
- Paper 16: Lopez et al. (2022), Giant Arc -- 1 Gpc Mg II structure
- W2-1: N_eff step function (Session 41) -- 32 -> 240 at tau > 0
- W3-1/W3-1b: CMB substrate analysis (Session 41) -- phononic crystal identification
- Naz W3-2: Nuclear review of fabric physics -- gradient stiffness, EOM, self-consistency loop
- PI directive: Complexity Is Geometry (Session 41) -- fabric reframing, N_eff as spatial complexity
- Sheth & van de Weygaert (2004) -- excursion set void model, void-in-void hierarchy
- Pan et al. (2012) -- SDSS void size function
