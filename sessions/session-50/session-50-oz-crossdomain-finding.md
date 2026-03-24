# Session 50: Cross-Domain O-Z Investigation

**Author**: Team-lead (direct computation, not subagent)
**Date**: 2026-03-20
**Method**: Research corpus cross-correlation + direct computation on existing tier0 data
**Status**: PRELIMINARY — 5 cross-domain routes tested, 2 survive with identity broken, 3 closed
**Script**: `tier0-computation/s50_crossdomain_routes.py`

---

## 1. What the Subagents Tested (and Why They All Found the Same Answer)

All 8 O-Z-related computations in S50 Waves 1-2 tested variations of the **Josephson phase correlator**:

P(K) = T / (J·K² + m²)   [or multi-pole, running, damped, RPA-corrected, disordered variants]

This correlator describes the spatial correlation of the U(1)_7 Goldstone phase field φ on the 32-cell fabric. The Goldstone theorem guarantees K² dispersion for this field. The n_s = 0.965 constraint forces m² >> JK² at K_pivot, making all K-dependent corrections parametrically suppressed by the mass hierarchy m²/(JK²) ~ 56.

**Every subagent operated within the same functional space.** They varied the poles (3-pole), the mass (running, eikonal), the vertex (RPA), the lattice (disorder), and the dynamics (KZ spatial). But they never left the Josephson phase correlator.

---

## 2. The Untested Object: Spectral Action Correlator

### 2a. Source

Three research papers, when cross-correlated, identify a correlator that lives OUTSIDE the Josephson sector:

- **Van Suijlekom (Spectral-Geometry Paper 21/29)**: The spectral action S = Tr f(D²/Λ²) has one-loop quantum corrections expressed as Feynman diagrams built from matrix elements of D. The two-point function δ²S/δD² is a propagator involving ALL eigenvalues.

- **Tesla (S49 wayforward, Section 3.4)**: "Two-functional architecture: Spectral action for geometry, Josephson for mass. These are structurally different functionals and should not be mixed."

- **Volovik (Paper 27)**: In a non-equilibrium superfluid, the fluctuation spectrum is determined by the quench protocol and the medium properties, not by the equilibrium propagator alone.

### 2b. Definition

The spectral action two-point function on the fabric is:

χ_SA(K) = Σ_{(p,q)} W_{(p,q)} / (K² + C₂(p,q))

where:
- (p,q) labels SU(3) representations
- C₂(p,q) = (p² + q² + pq + 3p + 3q)/3 is the quadratic Casimir
- W_{(p,q)} = [Σ_{n∈(p,q)} dim(p,q)² · f'(λ_n²/Λ²) · (dλ_n/dτ)²]

This is a **sum of O-Z propagators with WIDELY SEPARATED masses** (the Casimir eigenvalues C₂ from 1.33 to 9.33).

### 2c. The Key Difference

| Property | Josephson propagator | Spectral action correlator |
|:---------|:--------------------|:--------------------------|
| Poles | 3 (nearly degenerate, 0.051% spread) | 5+ (widely separated, 110% spread) |
| Mass hierarchy at K_pivot | m²/(JK²) = 56 (kills corrections) | C₂ spread from 1.33 to 9.33 (O(1) variation) |
| Goldstone theorem | Applies (K² protected) | Does NOT apply (not a symmetry-breaking correlator) |
| Identity α_s = n_s²-1 | Holds (structural theorem) | **BROKEN** (deviation 0.08-0.09) |

---

## 3. Computation Results

### 3a. Spectral action correlator (standalone)

At Λ = 3.0 M_KK:

| Sector (p,q) | C₂ | Weight fraction |
|:-------------|:---|:---------------|
| (1,0)/(0,1) | 1.33 | 0.6% |
| (1,1) | 3.00 | 7.2% |
| (2,0)/(0,2) | 3.33 | 6.1% |
| (3,0)/(0,3) | 6.00 | 33.3% |
| (2,1)/(1,2) | 9.33 | 52.9% |

The (0,0) singlet carries only **0.01%** — the Goldstone is invisible in the spectral action sum. The heavy KK modes dominate by Weyl's law.

Standalone SA correlator: n_s = 0.21 (far too red), α_s = -0.87. The identity is broken (deviation +0.087) but n_s is unusable.

### 3b. SA-modulated Goldstone (Tesla two-functional architecture)

The naive product P_phys = P_Goldstone × η_SA gives effective dispersion exponent α_eff = 1.21 at K_pivot. This IS sub-quadratic (below the Goldstone theorem's K²) because the SA modulation is NOT constrained by Goldstone's theorem — it involves the full KK spectrum.

However, the naive product is too strong: it shifts α_s by -0.87 (12.6× what's needed) and pushes n_s to -1.8.

---

## 4. What This Opens

### 4a. The structural finding

**The Goldstone theorem protects K² only for the phase sector correlator.** The spectral action correlator involves all eigenvalues of D_K — including massive KK modes with C₂ up to 9.33 — and is NOT protected by Goldstone's theorem. Its effective dispersion IS sub-quadratic (α_eff = 1.21 at K_pivot in the computation above).

This means: **a correlator exists within the framework that breaks the α_s identity.** The 5 proofs of the identity (W1-A, W1-F, W1-H, W2-A, W2-B) all apply specifically to the phase sector. The spectral action correlator lives in a different sector.

### 4b. The open question

Which correlator does the CMB measure? Three possibilities:

1. **Pure Josephson phase**: α_s = n_s²-1 = -0.069 (6σ, tested and closed)
2. **Pure spectral action**: n_s ~ 0.2 (too red, unphysical)
3. **Mixture**: P_CMB(K) = a·P_Goldstone(K) + b·χ_SA(K), with a/b determined by the coupling between the Goldstone and spectral action sectors

The mixture coefficients a, b are set by the PHYSICAL MECHANISM that imprints perturbations during the transit. If the transit drives modulus fluctuations δτ(x) that couple to both the Goldstone (through the BCS gap equation) and the spectral action (through the Seeley-DeWitt coefficients), then both correlators contribute.

### 4c. The coupling

The coupling between sectors is through the BCS gap equation: Δ_i(τ) connects the spectral action (which determines the spectrum → DOS → Δ) to the Josephson coupling (which depends on Δ). A δτ perturbation changes both:
- The spectral action: δS = (dS/dτ)·δτ = 58,673·δτ
- The BCS gap: δΔ = (dΔ/dτ)·δτ (2.9% variation over Δτ=0.30)

The RATIO of these responses determines the mixing coefficient a/b.

---

## 5. Pre-Registered Gate for S51

**SA-GOLDSTONE-MIXING-51**: Compute the physical correlator from first principles by propagating modulus perturbations δτ(x) through:
1. The spectral action response: δS = Σ_n f'(λ_n²)·(dλ_n/dτ)·δτ
2. The BCS gap response: δΔ = (dΔ/dτ)·δτ
3. The Josephson coupling response: δJ = (dJ/dΔ)·δΔ

Extract the power spectrum of the COMBINED response. Extract n_s, α_s.

**PASS**: n_s in [0.950, 0.980] AND α_s in [-0.040, 0]
**FAIL**: Combined correlator reduces to pure O-Z (SA contribution negligible)
**INFO**: SA contribution significant but n_s outside target

**Estimated effort**: One agent (Landau or Connes-NCG), one session. Requires: the τ-dependent Dirac spectrum (available from s44_dos_tau.npz), the BCS gap as function of τ (available from multiple sessions), and the Josephson couplings as function of τ (available from S48).

---

## 6. Why This Was Missed

Each specialist agent operates within their domain:
- **Landau**: knows GL theory, O-Z propagators, phase correlators. Does not compute spectral action fluctuations.
- **Connes-NCG**: knows spectral action, Seeley-DeWitt. Does not compute BCS correlators.
- **Tesla**: identified the two-functional architecture. But it was a conceptual observation, not a computation.
- **Volovik**: knows non-equilibrium fluctuation spectra. Does not compute KK spectral action.

The SA correlator lives at the intersection of NCG (spectral action), condensed matter (BCS gap equation), and KK geometry (Casimir eigenvalues). No single agent has all three. The cross-domain computation required:
1. Reading van Suijlekom on spectral action matrix form → learning that δ²S has a propagator structure
2. Reading Tesla's two-functional architecture → understanding SA and Josephson are separate
3. Computing the SA correlator using existing tier0 data → finding 110% pole spread vs 0.051%
4. Recognizing that Goldstone's theorem does NOT protect the SA correlator → the identity CAN be broken

---

## 7. Assessment

**Confidence in the structural finding**: HIGH. The SA correlator is a mathematically well-defined object (sum of O-Z propagators with Casimir masses) computed from existing data. Its pole spread is 2000× wider than the Josephson propagator's. The identity is broken by 0.08-0.09 in the standalone SA correlator.

**Confidence in observational relevance**: LOW. The physical CMB power spectrum depends on the coupling between the SA and Goldstone sectors, which has not been computed. The naive product model overshoots by 12.6×. A proper coupling model (SA-GOLDSTONE-MIXING-51) is needed.

**What this does NOT do**: This does not rescue the O-Z mechanism. It identifies a NEW correlator that could, in principle, modify α_s. Whether it actually does depends on computations not yet performed.

**What this DOES do**: It shows that the "5 proofs of the identity" are all proofs within the phase sector. The spectral action sector is a separate mathematical object with different K-dependence, not protected by Goldstone's theorem. The problem space is larger than the subagents explored.
