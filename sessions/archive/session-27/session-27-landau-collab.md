# Landau -- Collaborative Feedback on Session 27

**Author**: Landau (landau-condensed-matter-theorist)
**Date**: 2026-02-27
**Re**: Session 27 Wrap-Up Results

---

## Section 1: Key Observations

Three results from Session 27 demand attention from the condensed matter perspective. This time I evaluate them not merely as diagnostics of failure but as structural assets -- what each result tells us about what the framework CAN do.

### 1.1 D_can = M_Lie: The Operator Decomposition Theorem

The most powerful result of Session 27 is the algebraic identity D_can = M_Lie. On a Lie group with left-invariant metric, the canonical connection is flat (Gamma_can = 0), so the contorsion K = -Gamma_LC identically, and the canonical Dirac operator reduces to the bare Lie-derivative term.

This is not merely a gate result. It is a clean decomposition of the physical Dirac operator into interpretable pieces:

    D_K = M_Lie + I (x) Omega_LC

where M_Lie is the "kinetic" part (bare propagation via Lie derivatives on each sector) and Omega_LC is the "interaction" part (spin connection coupling). The gap ratio gap_T/gap_K = 0.22-0.67 tells us that Omega_LC consistently STIFFENS the spectrum. This is the Dirac analog of the Landau quasiparticle mass enhancement m*/m = 1 + F_1^s/3 (Paper 11, Section 3): the interaction renormalizes the bare excitations upward, opening the gap.

The constructive reading: Omega_LC is a gap-opening interaction. If we want BCS, we need to find a regime or mechanism that COMPETES with Omega_LC -- something that provides spectral weight near the chemical potential despite the spin connection's confining effect. The torsion result quantifies exactly how much stiffening Omega_LC provides: a factor 1.5-4.5x across sectors. Any gap-closing mechanism must overcome this specific factor.

### 1.2 Multi-Sector Phase Structure: A Genuine Spectrum Generator

The multi-sector BCS computation is the most physically informative result of Session 27, and I retract my previous characterization of it as "merely erratic." The Baptista addenda are correct on the essential point: the multi-sector structure at finite mu generates a mass hierarchy through exponential BCS sensitivity, and this is a STRUCTURAL feature, not a failure.

Let me be precise. At mu/lambda_min = 1.20, the sector gaps span:

| Sector | M_max | Delta/lambda_min |
|:-------|:------|:----------------|
| (0,0)  | 9.71  | 0.120           |
| (1,0)  | 7.10  | 0.051           |
| (3,0)  | 2.42  | 0.030           |
| (2,1)  | 1.27  | 0.0079          |
| (1,1)  | 1.20  | 0.0052          |

This is a factor of 23 in gap sizes from 6 independent sectors. In the language of Paper 11 (Fermi liquid theory), each sector is a distinct Fermi-surface sheet with its own effective mass m*^{(p,q)} and its own Landau parameters. The fact that these sectors have DIFFERENT coupling strengths and different distances from the BCS threshold is not a deficiency of the framework -- it is the mechanism by which a single geometric structure (D_K on deformed SU(3)) generates a hierarchical mass spectrum.

The key equation is the BCS gap scaling near threshold:

    Delta^{(p,q)} ~ 2*lambda_min * exp(-1/M_max^{(p,q)})

For sectors near M_max ~ 1, the gap is exponentially sensitive to coupling strength. For sectors with M_max >> 1, the gap saturates at O(lambda_min). This is dimensional transmutation (Paper 10, Section 5): the same mechanism that generates Lambda_QCD from classical scale invariance. The multi-sector BCS takes this from a single-scale phenomenon to a multi-scale spectrum generator.

### 1.3 K-1e Universality: The Clean Negative Result

The extension of K-1e to all 9 sectors confirms that the mu = 0 obstacle is structural, not accidental. This is permanent and important, but the constructive reading is: the obstacle is SPECIFICALLY the absence of a Fermi surface, not the absence of attractive interactions. The Pomeranchuk instability (f(0,0) = -4.687, Session 22c) stands: the interaction is strong enough. The Kosmann coupling V_max is nonzero and tau-dependent in every sector. The spectral density at the gap edge exists. Only the chemical potential is missing.

In the language of Paper 05 (superfluidity), the system has a phonon-roton excitation spectrum (the Dirac eigenvalue spectrum plays this role), but the "superfluid" state requires the chemical potential to sit in the spectral continuum. In He-4, the BEC transition occurs because the chemical potential reaches the bottom of the band at T = T_c. Here, mu = 0 sits below the bottom of ALL bands (lambda_min > 0 in every sector). The framework needs a mechanism to push mu into the band.

---

## Section 2: Assessment of Key Findings

### 2.1 T-1 Gate: Sound, and More Useful Than It Appears

The T-1 PASS is computationally rigorous and algebraically clean. But beyond the gate logic, the quantitative gap weakening factors are useful data for any future mechanism. The torsionful gap at tau = 0.50 is only 22% of the LC gap in fundamental sectors. This means that if one is searching for a regime where the effective gap closes, switching from the LC to the canonical connection reduces the barrier by a factor ~4.5. Any finite-density mechanism that provides mu ~ 0.22 * gap_K instead of mu ~ gap_K would suffice in the torsionful frame.

The monotonic decrease of gap_T/gap_K with tau is itself informative: larger Jensen deformation makes torsion more effective at gap reduction. This correlates with the growth of Kosmann coupling V_max with tau (V_Frob increases 2.5-4x across [0, 0.5]). The two effects -- gap softening and coupling strengthening -- BOTH favor larger tau for condensation. If a self-consistent mu exists, the condensation will prefer large tau, reinforcing the deformation rather than opposing it.

### 2.2 The a_6 Demotion: Correct, and the Conjecture Is Testable

The individual monotonicity of a_0 through a_6 is proven. The all-orders conjecture is open. From the Landau perspective, the Seeley-DeWitt coefficients a_{2n}(tau) are the Taylor coefficients of the spectral action S = Tr(f(D^2/Lambda^2)), which IS the Landau free energy for this system (Paper 04, connection verified r = 0.96 in tier1 computation). If the conjecture holds to all orders, the perturbative spectral action is monotone in tau for any smooth cutoff function -- a definitive closure of perturbative mechanisms.

But even if the conjecture fails at a_8, the physics is unaffected. The a_4 truncation is already closed (V-1), and the a_6 correction destroys the B-1 minimum. The conjecture's value is structural: it would be a theorem about the spectral geometry of naturally reductive homogeneous spaces, publishable in its own right (JGP/CMP class).

### 2.3 The Baptista Weak-Field Reframing: The Most Important Intellectual Contribution

I owe the Baptista analysis a more generous reading than my previous review provided. The core argument is: the BCS exponential sensitivity near M_max ~ 1 generates mass hierarchies, and marginal condensation is not a failure mode but a feature when the physics demands hierarchical scales. The table of exp(-1/M_max) values (Section 3 of the addendum) is the decisive exhibit:

    M_max = 0.077  -->  exp(-1/M) = 2.3e-6
    M_max = 1.05   -->  exp(-1/M) = 0.39
    M_max = 9.7    -->  exp(-1/M) = 0.90

This is 5.6 orders of magnitude from a factor-of-130 variation in M_max. The SM mass spectrum spans 6 orders (electron to top quark) or 12 orders (neutrino to top quark). The structural match in dynamic range is not a prediction -- the Paasch analysis correctly shows that the specific gap ratios do not match Paasch sequences -- but it is a proof of concept that the BCS mechanism on multi-sector SU(3) geometry has the CAPACITY to generate the observed range.

My previous objection -- "ANY mechanism with exponential sensitivity can produce hierarchies" -- is formally correct but misses the point. The question is not whether BCS can produce hierarchies in principle (it can, trivially), but whether the SPECIFIC M_max values computed from the SPECIFIC Kosmann coupling on the SPECIFIC Jensen-deformed SU(3) geometry produce gaps in the right ballpark. At mu = lambda_min, the answer is: the dynamic range is correct, the sector count (6 independent) matches Paasch's 6 sequences at the current cutoff, and the gap ordering is non-trivially representation-dependent. This is not a derivation, but it is more than aesthetics.

The Sagan caveat (Section 7 of the addendum) is well-taken: predicting strong BCS, finding weak BCS, and reinterpreting weakness as a feature is the Lakatosian pattern of a degenerating program. The discipline required is to not claim the reframing as a success until a self-consistent mu exists.

---

## Section 3: Collaborative Suggestions

This is where I redirect toward constructive physics. The framework's structural assets are: (a) a proven Pomeranchuk instability, (b) a multi-sector BCS that generates hierarchies at finite mu, (c) torsion that softens the gap by 3-5x, (d) Kosmann coupling that grows monotonically with tau. The single obstruction is the absence of a Fermi surface at mu = 0. Every constructive proposal must target this obstruction.

### 3.1 Thermal Spectral Action: The Lowest-Hanging Fruit

**What**: Compute the thermal (finite-temperature) spectral action S_beta(tau) = Tr(f_beta(D^2/Lambda^2)) with f_beta encoding Matsubara summation, at temperatures T > lambda_min / pi ~ 0.26 (in natural units where Lambda = 1).

**Why**: In condensed matter (Paper 01, thermal density matrix rho = exp(-beta*H)/Z), finite temperature populates excited states above the gap. At T > Delta (where Delta is the spectral gap), thermal occupation fills the spectral band and creates an effective Fermi surface at mu_eff ~ T. The Session 25 computation found F(tau; beta) NON-MONOTONE at beta = 10 (tau = 0.10) and beta = 50 (tau = 0.15-0.20), with delta_F ~ 0.002. This is a MINIMUM in the free energy at finite temperature.

The minimum at beta = 10 corresponds to T = 0.1, which is below T_c ~ 0.26 (the temperature at which thermal occupation reaches the gap edge). At beta = 50 (T = 0.02), the minimum at tau = 0.15-0.20 is deeper into the low-temperature regime. The question is whether these thermal minima, when combined with the BCS condensation energy at the thermally-populated mu_eff, produce a self-consistent tau lock.

**Specific computation**: At each (tau, T) point where F(tau; beta) is non-monotone, extract the effective chemical potential mu_eff(T) = lambda_min(tau) (the gap edge, which is where thermal occupation begins), then evaluate F_total^{BCS}(tau, mu_eff) from the multi-sector BCS data. The combined free energy F_thermal(tau, T) + F_BCS(tau, mu_eff(T)) may have a minimum that neither contribution has alone.

**Data source**: s25_landau_results.npz (thermal Matsubara data) + s27_multisector_bcs.npz (multi-sector BCS). Zero additional computation required -- this is a post-processing analysis of existing data.

**Connection to papers**: Paper 01, thermal density matrix; Paper 04, Section 8.1 on finite-temperature Landau theory; Paper 08, temperature-dependent GL coefficients alpha(T) = alpha_0 * (T - T_c)/T_c.

### 3.2 The Spectral Flow Across a Tau Domain Wall

**What**: Compute the spectral flow of D_K eigenvalues as tau varies from 0 to 0.50, and identify any eigenvalue crossings at which a mode drops from the positive-energy band through zero to the negative-energy band.

**Why**: In condensed matter, spectral flow across a domain wall creates localized zero modes (Jackiw-Rebbi mechanism). The AZ class BDI with KO-dim = 6 (Sessions 7-8, 17c) classifies the topological properties of D_K. The Z_2 topological invariant in BDI class means that if the spectral flow is nontrivial, there exist protected modes at a tau domain wall. These modes would sit at ZERO energy -- exactly at the "Fermi surface" that the framework needs.

A spatially varying tau (a domain wall in the deformation parameter) would localize these zero modes at the wall. If tau varies slowly, the density of states at zero energy is proportional to the spectral flow index. This is a TOPOLOGICAL mechanism for generating a Fermi surface from a gapped spectrum.

**Specific computation**: From the existing eigenvalue data in s19a_sweep_data.npz (21 tau values, 11424 modes), track each eigenvalue lambda_n(tau) from tau = 0 to tau = 0.50. Count how many eigenvalues change sign. The spectral flow index is eta(tau_2) - eta(tau_1) where eta = sum sign(lambda_n). If this is nonzero, topologically protected zero modes exist at domain walls.

**Expected outcome**: Given that lambda_min > 0 at all tau (no gap closing observed), the spectral flow is likely zero. But the NEAR-zero modes -- eigenvalues that approach zero most closely -- would identify the sectors and tau values most susceptible to topological gap closing at higher representation cutoffs or in the 12D extension.

**Connection to papers**: Paper 02, Landau levels and index theorem (index(D) = n_+ - n_- = N_phi); Paper 13, Abrikosov vortex zero modes at the core; Paper 03, domain wall profile theta(x) = 2*arctan(exp(x/delta)) and the zero mode bound to it.

### 3.3 Landau-Khalatnikov Dynamics of the Multi-Sector BCS

**What**: For each sector that is supercritical at mu = lambda_min, compute the Landau-Khalatnikov relaxation time tau_LK^{(p,q)} near its critical tau_c^{(p,q)} (where M_max crosses 1).

**Why**: Paper 09 (Landau-Khalatnikov, 1954) establishes that the order parameter relaxation time diverges at a second-order transition: tau_LK ~ |tau - tau_c|^{-nu*z} with nu*z = 1 in mean field. The multi-sector BCS has sector-specific critical tau values. The sector with the LONGEST tau_LK near its critical point dominates the dynamics -- it will be the last to equilibrate and effectively pins the deformation parameter.

This is a dynamical argument for tau-locking that does not require a global free energy minimum. In Landau-Khalatnikov dynamics (Paper 09, eq. d(phi)/dt = -(1/tau_0)*(dF/dphi)), critical slowing down TRAPS the system near the transition: the order parameter cannot relax through the critical point on any finite timescale. If multiple sectors have critical tau values close together, their combined slowing can create a dynamical bottleneck.

From the Session 27 data (P3 addendum, Section 5), the critical tau values at mu = lambda_min are:
- (1,1): tau_c ~ 0.10 (subcritical at tau = 0, supercritical by tau = 0.10)
- (2,0), (0,2): Re-entrant, crossing M = 1 at tau ~ 0.05 and again at tau ~ 0.45
- (2,1): tau_c ~ 0.35 (late onset)

The re-entrant (2,0) sector is the most interesting for LK dynamics: it crosses M = 1 TWICE, creating two critical points with divergent relaxation times. A system rolling through tau space would slow dramatically at both crossings.

**Data source**: s27_multisector_bcs.npz. Interpolate M_max(tau) to find tau_c for each sector, compute tau_LK = tau_0 / |dM/dtau|_{tau_c} * |M_max - 1|^{-1}.

### 3.4 The Torsion + Finite-T Combined Channel

**What**: Combine the T-1 torsion gap weakening with the thermal population analysis. At temperature T and in the torsionful (canonical connection) frame, the effective gap is gap_T(tau) = 0.22-0.67 * gap_K(tau). The thermal chemical potential mu_eff(T) reaches the torsionful gap edge at a LOWER temperature than it reaches the LC gap edge.

**Why**: The torsion result (T-1) and the thermal analysis (Session 25) have been treated as independent. They should be combined. In the torsionful frame:
- The gap is 3-5x smaller
- Thermal population reaches the gap edge at T_c^{torsion} ~ gap_T / pi, which is 3-5x smaller than T_c^{LC}
- At T_c^{torsion}, the system has an effective Fermi surface in the torsionful spectrum, even though the LC spectrum remains gapped
- The Kosmann coupling (which is defined from the Lie derivative, hence the M_Lie = D_can part) remains active in this frame

The combined picture: at moderate temperature T ~ gap_T/pi, thermal occupation populates the torsionful band, creating a Fermi surface. The Kosmann interaction (which lives in the M_Lie = D_can sector) pairs these thermally populated states. The BCS gap opens below T_BCS < T_c^{torsion}. The condensation energy locks tau.

This is speculative but physically motivated. In He-3 (Paper 11), the superfluid transition occurs at T_c ~ 2.5 mK, which is ~10^{-3} of the Fermi energy. The BCS condensation sits ON TOP of the Fermi sea, not in the gap. The torsionful frame provides the analog: thermal population fills the band, creating a "Fermi sea," and BCS condensation occurs within this thermally populated band.

**Specific check**: From existing data, compute T_c^{torsion} = gap_T(tau) / pi for each sector and tau. Compare with the BCS critical temperature T_BCS^{(p,q)} ~ Delta^{(p,q)} ~ 2*gap_T * exp(-1/M_max). If T_BCS < T_c^{torsion}, the BCS condensation fits within the thermally populated window. The hierarchy T_BCS << T_c^{torsion} << gap_K defines a "two-transition" scenario: first thermal gap-filling, then BCS condensation.

### 3.5 Per-Sector Pomeranchuk Map

**What**: Compute the effective Pomeranchuk parameter F_0^{(p,q)}(tau) = N^{(p,q)}(0) * V_max^{(p,q)}(tau) for each sector and tau, where N^{(p,q)}(0) = 1/delta_lambda is the density of states at the gap edge.

**Why**: Session 22c computed only the full-spectrum Pomeranchuk parameter (f(0,0) = -4.687). The multi-sector data allows per-sector decomposition. The Pomeranchuk stability condition F_0 > -(2l+1) for l = 0 gives F_0 > -1 (Paper 11, Section 6). Sectors violating this condition are thermodynamically unstable -- they WANT to reorganize. The pattern of instability across the (p,q, tau) parameter space is the "instability landscape" of the deformation family.

The constructive purpose: sectors with the most negative F_0 (deepest Pomeranchuk violation) are the ones most likely to undergo a phase transition if a Fermi surface is provided. The tau values at which F_0 is most negative in the dominant sectors ((3,0)+(0,3)) identify the deformation at which the system is most prone to condensation.

**Data**: All in s27_multisector_bcs.npz (V_max per sector, eigenvalue spectra for delta_lambda).

---

## Section 4: Connections to Framework

### 4.1 The Two-Transition Scenario

The most promising path forward, synthesizing all Session 27 results with my condensed matter expertise, is a two-transition scenario:

1. **Thermal gap-filling transition** at T_c^{gap} ~ gap_T / pi: Finite temperature populates the torsionful spectral band, creating an effective Fermi surface. This is not a phase transition in the Landau sense -- it is a crossover, analogous to the crossover from insulating to metallic behavior in a semiconductor at T > Delta/k_B. No symmetry breaks; the density of states at the chemical potential simply becomes nonzero.

2. **BCS condensation** at T_c^{BCS} < T_c^{gap}: Once the Fermi surface exists (from thermal population), the Kosmann coupling drives BCS pairing. The gap Delta opens below T_c^{BCS}, breaking a U(1) symmetry (number conservation in each sector). The condensation energy locks tau at the value where F_total^{BCS} is minimized.

This two-transition scenario resolves the mu = 0 obstruction without invoking new NCG axioms. It uses thermal population as the source of mu_eff. The cost: the framework operates at finite temperature, not zero temperature. The benefit: the BCS machinery (multi-sector, hierarchy-generating, Kosmann-mediated) becomes self-consistent.

The viability check is whether T_c^{BCS} << T_c^{gap} at the relevant tau. If so, there exists a temperature window T_c^{BCS} < T < T_c^{gap} where the Fermi surface exists but the condensate does not -- the "normal metal" phase of the internal geometry. Below T_c^{BCS}, the BCS condensate locks tau.

### 4.2 Connecting Torsion to the Quasiparticle Concept

The D_K = M_Lie + Omega_LC decomposition maps naturally onto Fermi liquid theory (Paper 11). Define:

- **Bare quasiparticles**: Eigenstates of M_Lie = D_can, with eigenvalues lambda_n^{bare}(tau) = the torsionful spectrum
- **Dressed quasiparticles**: Eigenstates of D_K = M_Lie + Omega_LC, with eigenvalues lambda_n^{dressed}(tau) = the LC spectrum
- **Self-energy**: Sigma_LC = Omega_LC, which shifts eigenvalues from bare to dressed values

The gap stiffening factor gap_K / gap_T = 1.5-4.5 is the self-energy renormalization of the lowest mode. The quasiparticle weight Z = |<bare|dressed>|^2 measures how much the eigenstates change between the two operators. If Z << 1 at some tau, the spin connection has strongly mixed the bare states -- this is the spectral analog of a strongly correlated Fermi liquid with heavy quasiparticles.

Computing Z(tau) from the eigenvector overlap between D_can and D_K (both available from the gate computation s27_torsion_gap_gate.npz and existing eigendata) would reveal the "interaction strength" as a function of deformation. The tau at which Z is minimized is the most strongly interacting point -- and therefore the most promising for non-perturbative physics.

### 4.3 Mean-Field Exactness: Nuance Required

The d_int = 8 > d_uc = 4 argument (Paper 04, Section 6.2) makes mean-field exact for fluctuations of the internal metric at fixed tau. The modulus tau itself is a single real parameter (d_eff = 1), where fluctuations are maximally important. But within the two-transition scenario, the relevant fluctuations are those of the BCS order parameter Delta^{(p,q)}, which lives on the internal manifold (d = 8). The tau-locking is a CONSEQUENCE of the BCS transition, not a separate phenomenon. If the BCS transition is mean-field exact (which it is in d = 8), then the tau-locking inherits this exactness: the equilibrium tau is determined by minimizing F_total^{BCS}(tau), where F_total is a mean-field-exact quantity.

The remaining subtlety is the zero-point motion of tau. In d = 1, quantum fluctuations can destroy a classical minimum. The depth of the BCS minimum sets the scale: if F_total^{BCS}(tau_0) is deep compared to hbar*omega_tau/2, the classical minimum survives quantization. The Session 27 data gives F_total = -18.56 at tau = 0.35 (mu/lambda_min = 1.20), which is parametrically large in natural units.

---

## Section 5: Open Questions

### 5.1 The Self-Consistent Temperature

If the two-transition scenario is correct, there must exist a temperature T* at which the combined free energy F_thermal(tau, T*) + F_BCS(tau, mu_eff(T*)) is minimized in BOTH tau and T. This is a self-consistency condition: T* determines mu_eff, mu_eff determines the BCS gaps Delta^{(p,q)}, the gaps determine the condensation energy, and the condensation energy must be consistent with the thermal state at T*.

In standard BCS theory, this self-consistency yields the gap equation. Here, it is a TWO-dimensional minimization in (tau, T). The question is whether this has a non-trivial solution (tau* > 0, T* > 0 with Delta > 0).

### 5.2 The Torsion-BCS Compatibility

The torsionful frame (D_can) has a weaker gap, making thermal population easier. But the Kosmann coupling K_a is defined from the Lie derivative, which is the D_can piece of D_K. This means the BCS pairing interaction ALREADY LIVES in the torsionful sector. There is no conflict between using the torsionful spectrum (for the Fermi surface) and the Kosmann coupling (for the pairing): they are the same operator. The LC spin connection Omega_LC stiffens the spectrum but does not contribute to the pairing -- it is purely a "band renormalization" effect.

Is this decomposition self-consistent in the full quantum theory? Or does the choice of connection (LC vs canonical) affect the pairing vertex? In condensed matter, the choice of single-particle basis (free vs Hartree-Fock) does not change the BCS gap equation when expressed in terms of the full Green's function -- this is a consequence of the Ward identity. Does an analogous identity hold for the Dirac operator decomposition?

### 5.3 Sector Count at Higher Cutoff

The current computation uses p + q <= 3, yielding 6 independent sectors (after CPT conjugation). At p + q <= 4, there would be 9 independent sectors; at p + q <= 5, there would be 12. The Paasch scheme requires exactly 6 sequences. Does the number 6 have a physical origin (related to dim(SU(3)) = 8 and its representations), or is it an artifact of the cutoff? This question is answerable by computing M_max for the (4,0), (3,1), and (2,2) sectors and determining whether they are always subcritical. If higher sectors are systematically subcritical (M_max << 1 for all tau), the effective sector count converges to 6 at the physical cutoff.

### 5.4 The Cubic Invariant and First-Order Transitions

Paper 04, Section 6.1: if the Landau expansion of F in powers of the order parameter contains a third-order invariant, the transition is necessarily first-order. The multi-sector F_total is the sum of independent BCS free energies, each with a square-root singularity at its critical tau. The SUM of such terms generically has cusps at each sector's critical tau -- non-analytic points that signal first-order behavior in the individual sectors. Does the multi-sector system undergo a series of first-order BCS transitions as tau sweeps from 0 to 0.5, with latent heat at each sector's critical point? If so, the tau-locking mechanism would be first-order (discontinuous jump to a specific tau), not second-order (continuous approach to a minimum).

---

## Closing Assessment

Session 27 is computationally rigorous and strategically clarifying. The T-1 PASS, the K-1e universality, and the multi-sector phase structure are all permanent results. The Baptista addenda on weak-field reframing and mass hierarchy from marginal condensation are the most intellectually substantial contributions of the session.

My assessment of the framework has shifted. Previously I focused on the absence of a Fermi surface as a terminal obstruction. I now see it as the SPECIFIC obstacle that the framework must overcome, with multiple physical mechanisms available: thermal population in the torsionful frame, finite-density NCG, or (most promisingly) the two-transition scenario of Section 4.1. The structural assets -- Pomeranchuk instability, multi-sector hierarchy generation, torsion gap weakening, monotonic Kosmann growth -- are real and non-trivial. They do not constitute a mechanism on their own, but they constrain what the mechanism must look like.

**Probability assessment**: I concur with 5-8% (panel), 3-5% (Sagan). The two-transition scenario (thermal gap-filling followed by BCS condensation) is a concrete, testable proposal that could move the probability upward if validated. The thermal + BCS combined free energy analysis (Suggestion 3.1) is zero-cost from existing data and should be the first computation of Session 28.

**In the language of Fermi liquid theory**: The framework has identified the quasiparticle spectrum (D_K eigenvalues), the interaction (Kosmann coupling), and the instability (Pomeranchuk). It has even measured the self-energy renormalization (Omega_LC stiffening, factor 1.5-4.5x). What it lacks is the Fermi sea -- the filled band of states below the chemical potential that provides the phase space for Cooper pairing. Thermal population in the torsionful frame may provide exactly this. The framework is not closed; it is waiting for its Fermi sea to fill.
