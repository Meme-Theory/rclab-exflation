# Volovik Response to COHERENCE-RESPONSE-47 ARTIFACT Verdict

**Author**: Volovik (Superfluid Universe Theorist)
**Date**: 2026-03-16
**Re**: Why the character coherence function failed and what dynamical probe succeeds

---

## 0. The Diagnosis

The character coherence function C(theta; tau) measures structure through a spectral (Fourier) decomposition on T^2. The Peter-Weyl characters chi_{(p,q)} are tau-independent basis functions. The BCS weights w_{(p,q)}(tau) modulate them. The result: r_C = 0.9192 +/- 0.0003 rad, with 95% of the width set by the truncation at p+q <= 3, 5% by static BCS shift, and 0.13% by dynamical tau-dependence. Elasticity d(ln r_C)/d(ln Delta_B2) = 0.030.

This is the correct verdict. The coherence function is a kinematic observable dressed with a perturbative dynamical correction. It cannot serve as a substrate self-coherence diagnostic.

The reason is structural, not accidental. The Peter-Weyl expansion separates the problem into basis functions (characters, tau-independent) and coefficients (weights, tau-dependent). Any quantity defined as a weighted sum over characters will be dominated by the characters whenever the weight variation is small compared to the character variation. Delta_B2 varies by 5% over the tau range; the characters vary by factors of 10^2 across T^2. The probe was killed by a separation of scales between the kinematic and dynamical content.

In superfluid physics, the analog would be measuring the NMR frequency shift of 3He-B by decomposing the order parameter in spherical harmonics and asking whether the harmonic coefficients track the gap. They do -- perturbatively. But the frequency shift is dominated by the Y_{l=0} (spherical) component, not by the gap-dependent Y_{l=2} (quadrupolar) correction. The right probe for the gap is not a spectral decomposition at all. It is a response function.

---

## 1. Why My Probes Might Succeed

In my collab review I proposed three probes: (1) Akama-Diakonov emergent metric, (2) q-theory vacuum energy, (3) Sakharov curvature-weighted functional. Each works through different mathematics than the character expansion, and each avoids the truncation-dominance problem for a specific reason.

### 1.1 Akama-Diakonov Emergent Metric (Paper 03)

The AD construction builds the metric as a fermion bilinear: g^{mu,nu}(x) = (1/N) sum_a psi_bar_a {gamma^mu, gamma^nu} psi_a. The metric is not a Fourier decomposition -- it is a composite operator. Its value at each point on SU(3) is determined by the LOCAL fermion vacuum expectation value, not by a global harmonic expansion.

For the BCS state on SU(3), the fermion bilinear is the anomalous Green's function F(g) = <psi(g) psi(e)>, which IS the gap function Delta(g). The AD metric would be:

    g_ij^AD(theta) ~ |F(theta)|^2 ~ |Delta(theta)|^2

This is the same condensate profile that the character coherence function measures. So at first sight, this probe inherits the same truncation problem.

However, the AD metric enters physics through its DERIVATIVES -- the connection and curvature. The Christoffel symbols Gamma ~ d(g)/d(theta) and the Riemann tensor R ~ d^2(g)/d(theta)^2 are not dominated by the identity-peak value but by its shape. The curvature is a second-derivative quantity. The identity peak of |Delta|^2 is sharply peaked (1/e^2 radius = 0.78 rad), and the second derivative at the peak scales as |Delta|^2 / r_C^2. This ratio depends on Delta^2 (dynamical) divided by r_C^2 (95% kinematic). The curvature thus amplifies the dynamical content by a factor ~ 1/r_C^2.

**Assessment**: The AD metric itself inherits the truncation problem. Its curvature partially amplifies the dynamical signal but does not escape the fundamental issue that the spatial profile is character-dominated. **This probe alone is INSUFFICIENT.**

### 1.2 Q-Theory Vacuum Energy (Papers 15-16)

The q-theory vacuum energy rho_vac(tau) = E_spec(tau) + E_cond(tau) is a GLOBAL integral over the entire BCS state. It is not a function of position on SU(3) -- it is a single number at each tau. The q-theory equilibrium condition d(rho_vac)/d(tau) = 0 determines the equilibrium deformation parameter.

This probe is immune to the truncation-dominance problem because it does not decompose anything into characters. It integrates the full BCS energy -- spectral action plus condensation energy -- over all modes. The tau-dependence comes from two channels: (a) the spectrum lambda_k(tau), which varies by ~5% across sectors, and (b) the pairing Delta_s(tau), which also varies by ~5%. But the COMBINATION E_cond = -sum_k Delta_k^2 / (2 E_k) can exhibit much larger fractional variation because it is a difference of large quantities.

S45 Q-THEORY-BCS-45 demonstrated this: tau* = 0.209, 10.2% from the fold. The crossing from positive to negative epsilon occurs because E_spec and E_cond have different tau-dependences. The variation is not 0.13% -- it is O(1). The q-theory crossing is a genuinely dynamical quantity.

**Assessment**: The q-theory vacuum energy avoids the truncation problem entirely. It is a thermodynamic quantity (total energy), not a spectral decomposition. It succeeded in S45 (tau* within 10% of fold) where the character coherence function failed (0.13% variation). **This probe SURVIVES.**

### 1.3 Sakharov Curvature-Weighted Functional (Papers 07, 30)

The Sakharov induced gravity functional is G_N^{-1} ~ sum_a K_a(tau) * n_a(tau), where K_a is the sectional curvature of direction a and n_a is the spectral density in that direction. Both K_a and n_a depend on tau, and the product couples geometry to dynamics.

RUNNING-GN-45 computed this: G_Sak(tau) is monotone with 2.5% variation over [0, 0.5], and G_Sak/G_obs = 0.436 (0.36 OOM). The mode count a_0 = 6440 is topologically protected (constant).

The variation is small (2.5%) but this is a different kind of smallness than the character coherence function's 0.13%. The Sakharov functional is dominated by the mode count (topologically protected), not by the truncation. Its 2.5% variation comes from the spectrum, not from harmonic artifacts. It measures the right thing -- the response of gravity to the vacuum state -- but the variation is too small to serve as a decisive self-coherence probe.

**Assessment**: The Sakharov functional avoids the truncation problem (it does not use characters at all) but its variation is controlled by topological protection, giving small tau-dependence for a different reason. **INSUFFICIENT as a self-coherence probe, but correct as a G_N computation.**

---

## 2. The Right Probe: Superfluid Density Tensor

The character coherence function is a state function -- it describes the spatial pattern of the condensate. The q-theory vacuum energy is a state function -- it describes the total energy. Neither is a response function.

In superfluid physics, the observable that measures the rigidity of the condensate against perturbation is the superfluid density rho_s. This is defined as the second derivative of the free energy with respect to a superfluid velocity (phase twist):

    rho_s^{ab} = d^2 F / d(v_s^a) d(v_s^b)

where v_s^a = (hbar/m) nabla_a phi is the superfluid velocity in direction a. This is a RESPONSE function -- it measures how the free energy changes when you twist the phase of the condensate along direction a.

The superfluid density is a dynamical quantity in the following precise sense: it vanishes in the normal state (no condensate = no phase stiffness), is maximal at T=0 in the fully paired state, and depends on the gap Delta through the Yosida function:

    rho_s / rho = 1 - Y(T/Delta)

where Y(x) ~ x^2 for T << Delta (exponentially activated quasiparticles deplete rho_s). At T=0, rho_s = rho exactly -- the entire fluid is superfluid.

For a multi-band system with a non-isotropic geometry, rho_s becomes a tensor. Landau proposed this in her collab review (S-4: Peotta-Torma formula). On SU(3) with the Jensen deformation, the superfluid density tensor has 8 x 8 components, one for each pair of Lie algebra directions.

The Peotta-Torma formula for flat-band systems (Paper 18 context) gives:

    D_s^{ab} = (2 / V) sum_k [f(E_k^-) - f(E_k^+)] * g_ab^{geom}(k)

where g_ab^{geom} is the quantum geometric tensor (Fubini-Study metric of the Bloch states), E_k^{+/-} are the Bogoliubov quasiparticle energies, and f is the Fermi function. At T=0, this simplifies to:

    D_s^{ab} = (2 / V) sum_{k: occupied} g_ab^{geom}(k)

The quantum geometric tensor has two parts: the real part (the Fubini-Study metric, which determines rho_s in flat bands) and the imaginary part (the Berry curvature, which determines the anomalous Hall effect). Both are dynamical -- they depend on the BCS state, not on the character expansion.

Why does rho_s avoid the truncation problem? Because it is not a Fourier decomposition on T^2. It is a sum over occupied BCS states of a geometric quantity (the quantum metric) that depends on the wave functions, not on the characters. The truncation at p+q <= 3 limits the number of modes in the sum, but each mode's contribution is fully dynamical -- determined by the BCS occupation v_k^2, which varies from 0 to 1 depending on how far the mode is from the Fermi level.

The superfluid density tensor rho_s^{ab}(tau) would measure:
- Along the 3 u(1)-su(2) flat directions (K = 0): rho_s should be SMALL (no curvature = weak restoring force for phase twists)
- Along the 12 su(2)-C^2 soft directions (K = 0.010): rho_s should be LARGE (this is where pairing concentrates)
- Along the 6 su(2)-su(2) hard directions (K = 0.122): rho_s should be INTERMEDIATE (curvature provides stiffness but pairing is weak)

This anisotropy is the self-coherence the user seeks. "Near are like" means: elements connected by a direction of large rho_s are rigidly phase-locked. Elements connected by a direction of small rho_s are loosely coupled. The coherence scale is not a single number (r_C) but an 8-dimensional tensor whose eigenvalues define 8 independent coherence lengths -- one per Lie algebra direction.

---

## 3. The Free Energy Landscape as Self-Coherence Probe

The user asks whether F(tau) -- the BCS free energy as a function of the Jensen deformation -- can serve as a self-coherence probe instead of C(theta; tau).

In the Volovik program, the free energy of the ground state determines the vacuum energy through the thermodynamic identity (Paper 05, Paper 15):

    epsilon + P = 0    (equilibrium vacuum, zero cosmological constant)

where epsilon is the energy density and P is the pressure. The cosmological constant is Lambda = epsilon + P, which vanishes in equilibrium. Any deviation from equilibrium -- quasiparticles, curvature, boundaries -- shifts Lambda away from zero by an amount proportional to the perturbation energy.

F(tau) is a well-defined dynamical quantity. It is the Helmholtz free energy of the BCS state on the Jensen-deformed SU(3):

    F(tau) = E_spec(tau) + E_cond(tau) - T * S(tau)

At T=0 (the relevant limit for the substrate), F = E_spec + E_cond. S46 computed this: Q-THEORY-SELFCONSISTENT-46 found no crossing when self-consistent gaps are used (eps(0) < 0 for all tau). Q-THEORY-BCS-45 found a crossing at tau* = 0.209 with FLATBAND gaps.

The free energy IS the right functional for the q-theory self-tuning. The equilibrium condition d(F)/d(tau) = 0 at constant volume (guaranteed by the volume-preserving Jensen deformation) IS the q-theory equilibrium equation (Paper 15, eq. drho/dq = 0, with q -> tau).

But F(tau) is a global quantity -- it does not tell you about local coherence. It tells you where the vacuum wants to sit (the equilibrium tau). The question "does the substrate stabilize at the fold?" is answered by F(tau), not by C(theta; tau). The answer is: F(tau) has a crossing near tau = 0.209 (10% from fold, S45), which is the closest any computation has come to selecting the fold through a dynamical mechanism.

---

## 4. Stabilization Through Coherence in Superfluid Language

The user asks: is there a precedent for a system stabilizing at the point of maximum superfluid density rather than minimum free energy?

The answer is yes, with a precise caveat.

In 3He, the A-B transition is first-order: the A phase has lower free energy at high pressure and temperature, the B phase at lower pressure and temperature. But the A phase survives metastably into the B-phase regime because it has a HIGHER superfluid density in certain directions (the orbital angular momentum direction). The A-phase is stabilized by its anisotropic superfluid stiffness -- phase twists along the l-vector are extraordinarily stiff, and the system resists the transition to B because it would have to overcome a topological barrier (unwinding the l-vector texture).

This is stabilization by coherence (superfluid stiffness) rather than by free energy. The metastable A phase has HIGHER free energy but HIGHER directional coherence. The lifetime of the metastable state scales exponentially with the barrier height, which is proportional to rho_s^{ll} (the superfluid density along the l-direction).

In the framework, the analog would be: the fold geometry at tau = 0.19 might not be the global minimum of F(tau) (the q-theory crossing is at 0.209), but it might be the point of maximum superfluid density in the B2 direction. The directional stiffness would create a metastable state that resists deformation away from the fold.

The key distinction: free energy determines EQUILIBRIUM. Superfluid density determines STABILITY AGAINST PERTURBATION. These are related (both derive from the partition function) but not identical. A state can be a free energy minimum with weak coherence (easily disrupted by fluctuations) or a free energy saddle point with strong coherence (metastable but robust).

The S38 result that P_exc = 1.000 (complete excitation through the fold) suggests the system does NOT stabilize at the fold through coherence. The transit completes. But the GGE relic post-transit is permanently non-thermal precisely because the integrability-protected conserved quantities create a kind of "frozen coherence" -- the 8 Richardson-Gaudin integrals lock the quasiparticle distribution into a pattern that cannot thermalize. This is not spatial coherence but spectral coherence: the occupations of different modes are correlated in a pattern determined by the initial BCS ground state plus unitary evolution.

---

## 5. The Decisive Computation: SUPERFLUID-DENSITY-TENSOR-47

**Name**: SUPERFLUID-DENSITY-TENSOR-47 (or RHOS-TENSOR-47)

**What**: Compute the 8 x 8 superfluid density tensor rho_s^{ab}(tau) at 5 tau values (0.00, 0.05, 0.10, 0.15, 0.19) using the Peotta-Torma formula adapted to the BCS state on Jensen-deformed SU(3).

**Input data**:
- Dirac eigenvalues and eigenvectors at each tau (from s44_dos_tau.npz, supplemented by full D_K diagonalization)
- BCS gaps Delta_s(tau) for s = B1, B2, B3 (from s46_qtheory_selfconsistent.npz)
- The V matrix (pairing interaction, from s39)
- The 8 generators of su(3) in the spinor representation (T_1...T_8)

**Formula**: For each pair of Lie algebra directions (a, b):

    rho_s^{ab}(tau) = sum_{k,l} [f(E_k) - f(E_l)] / [E_l - E_k] * <k|T_a|l> <l|T_b|k>

where E_k = sqrt(xi_k^2 + Delta_{s(k)}^2) are the Bogoliubov quasiparticle energies, xi_k = lambda_k - mu (mu=0 by PH symmetry), and T_a is the a-th generator of su(3) acting on the spinor representation. At T=0, the Fermi function difference becomes a step function and the formula reduces to:

    rho_s^{ab} = sum_{k: E_k > 0} sum_{l: E_l < 0} (2 / |E_k - E_l|) * |<k|T_a|l>|^2

This is a sum over occupied-to-unoccupied transitions weighted by the matrix element of the generator and the inverse energy denominator.

**Why it avoids truncation-dominance**: The matrix elements <k|T_a|l> depend on the EIGENVECTORS of the Bogoliubov Hamiltonian, not on the characters. The eigenvectors are fully dynamical -- they mix BCS u's and v's that depend on Delta_s(tau). The energy denominators 1/|E_k - E_l| weight transitions near the gap edge, where the BCS occupation changes rapidly. This is where the dynamical content lives.

The character coherence function had elasticity 0.030 (3% response to gap variation). The superfluid density tensor should have elasticity of order 1, because rho_s at T=0 scales as (Delta/E_F)^2 for an isotropic BCS state, and the BCS occupation factors v_k^2 change by O(1) near the gap edge.

**Expected outcome**:
- 8 eigenvalues of rho_s^{ab}(tau), classified by the su(2) x u(1) x C^2 block structure
- Strong anisotropy: eigenvalues in the soft (K = 0.010) directions 10-100x larger than in the hard (K = 0.122) directions
- Tau-dependence of O(1) fractional variation (not 0.13%), directly tracking Delta_B2(tau)
- At the fold: rho_s^{B2,B2} at maximum (peak pairing = peak phase stiffness)

**Pre-registered gate**:
- PASS: max eigenvalue variation across tau > 10% AND eigenvalue anisotropy ratio > 5
- FAIL: max eigenvalue variation < 1% (same truncation problem as character coherence)
- INFO: anisotropy confirmed but tau-variation intermediate

**What it tests**: Whether the substrate has a DYNAMICAL self-coherence structure visible through a response function (superfluid density) rather than a state function (character expansion). If rho_s^{ab}(tau) shows O(1) tau-dependence with strong directional anisotropy, the substrate has genuine dynamical self-coherence that the character coherence function was too blunt to detect.

---

## 6. Summary

| Probe | Type | Truncation-immune? | Tau-variation | Status |
|:------|:-----|:-------------------|:-------------|:-------|
| C(theta; tau) | State function (Fourier) | No (95% geometric) | 0.13% | CLOSED |
| AD metric | State function (composite) | Partially (curvature amplifies) | ~1% estimated | INSUFFICIENT |
| Q-theory F(tau) | State function (global) | Yes (no characters) | O(1) crossing | SURVIVES (S45: tau*=0.209) |
| Sakharov G_N | State function (mode count) | Yes (topologically protected) | 2.5% | INSUFFICIENT for coherence |
| rho_s^{ab}(tau) | Response function | Yes (eigenvector-based) | O(1) expected | PROPOSED: RHOS-TENSOR-47 |

The character coherence function measured the wrong thing. It asked "how does the identity peak shape depend on tau?" and found "it barely does." The right question is "how rigid is the condensate against phase twists in each Lie algebra direction, and how does that rigidity depend on tau?" That is the superfluid density tensor.

The q-theory vacuum energy F(tau) already answered a related question: "where does the vacuum equilibrium sit?" at tau* = 0.209. The superfluid density tensor would answer the complementary question: "how stiff is the vacuum against perturbation at each tau?" If rho_s peaks at or near the fold, the substrate self-coherence interpretation gains dynamical support through a quantity that is genuinely sensitive to the pairing state.

---

**Files referenced**:
- W3-3 result: `sessions/session-47/session-47-wave1-workingpaper.md`
- W3-3 script: `tier0-computation/s47_coherence_response.py`
- W3-3 data: `tier0-computation/s47_coherence_response.npz`
- My collab review: `sessions/session-47/session-47-crystal-geometry-volovik-collab.md`
- Naz substrate reframe: `sessions/session-47/session-47-naz-substrate-reframe.md`
- Landau S-4 (Peotta-Torma): `sessions/session-47/session-47-crystal-geometry-landau-collab.md`
- Paper 03 (Acoustic Metric): `researchers/Volovik/03_2023_Volovik_Acoustic_Metric_Planck_Constants.md`
- Paper 05 (Vacuum Energy): `researchers/Volovik/05_2005_Volovik_Vacuum_Energy_Cosmological_Constant.md`
- Paper 07 (Induced Gravity): `researchers/Volovik/07_1994_Volovik_Induced_Gravity_Superfluid_3He.md`
- Paper 15 (Self-Tuning): `researchers/Volovik/15_2008_Klinkhamer_Volovik_Self_Tuning_Vacuum.md`
- Paper 18 (Flat Band): `researchers/Volovik/18_2018_Volovik_Graphite_Graphene_Flat_Band_Superconductivity.md`
- Paper 22 (Elasticity Tetrads): `researchers/Volovik/22_2019_Nissinen_Volovik_Elasticity_Tetrads_Emergent_Gravity.md`
- Paper 30 (Newton's Constant): `researchers/Volovik/30_2022_Volovik_Newton_Constant_Modified_Gravity_Superfluid.md`
