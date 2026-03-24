# Substrate Self-Coherence: A Nuclear Theorist's Reframe

**Author**: Nazarewicz (Nuclear Structure Theorist)
**Date**: 2026-03-16
**Re**: User reframe of Section 1.1 critique -- is the 3.14 x 10^6 contrast a substrate self-coherence function?

---

## 1. Engaging the Reframe Honestly

My critique was correct on its own terms: the 3.14 x 10^6 contrast is not a spatial BCS phenomenon. The self-consistency loop does not close through the torus coordinate. No nuclear system produces a six-order-of-magnitude pairing contrast because nuclear Cooper pairs live on a pre-existing spatial background whose density profile is fixed by the nuclear potential. The pairing field Delta(r) inherits the smoothness of the density rho(r), and that smoothness limits the contrast.

The user's reframe accepts all of this and then inverts the logic. The argument: the nuclear comparison fails not because the 10^6 is too large, but because the nuclear system is the wrong comparison class. In a nucleus, the spatial background is given and the pairing field is a perturbation on it. For the substrate, there IS no pre-existing spatial background. The SU(3) geometry is the object itself, and the character coherence function measures how strongly the geometry prefers self-agreement.

This is physically defensible if -- and only if -- the following condition is met: the character-weighted BCS amplitude must be interpretable as a genuine two-point correlation function of the substrate, not merely as a Fourier decomposition artifact.

Let me make this precise. On any compact Lie group G, the Peter-Weyl theorem gives a complete orthonormal basis for L^2(G). Any function f(g) can be expanded in matrix elements of irreducible representations. The character chi_{(p,q)}(g) is the trace of rho_{(p,q)}(g), and it satisfies chi_{(p,q)}(e) = dim(p,q). This is representation theory -- it holds for ANY compact group and ANY set of weights. The identity peak is kinematic.

But the user is not claiming the identity peak is surprising. The user is claiming it is the substrate's coherence length. The question is whether the BCS weights w_{(p,q)} -- which encode the dynamical content (pairing gaps, Gaussian suppression, sector structure) -- produce a decay profile from the identity that has physical meaning as a correlation function.

The answer is: **yes, conditionally**. The BCS weights are not arbitrary. They are determined by solving the gap equation on the 16-mode Dirac spectrum. The Gaussian suppression exp(-(eps - eps_0)^2 / (2*Delta_B2^2)) is set by the BCS coherence energy Delta_B2 = 0.732. This energy scale converts, through the character expansion, into an angular coherence scale on T^2. The 1/e^2 radius of 0.78 rad = pi/4 is the angular width of the BCS coherence patch on SU(3), as seen through the lens of the character expansion. This is a physical quantity -- it is set by the pairing interaction, not by an arbitrary truncation.

Where the reframe becomes genuinely interesting is the magnitude. In nuclear BCS, the pairing coherence length xi ~ hbar*v_F / (pi*Delta) is always LARGER than the system size for light nuclei (the 0D regime) and comparable to it for heavy nuclei. The coherence function C(r, 0) = <Delta(r)Delta*(0)> decays over a length xi, and the contrast ratio C(0,0)/C(R, 0) for r = R (the nuclear radius) is at most exp(2*R/xi) ~ 10^1 to 10^3. The 10^6 on SU(3) arises because the character expansion adds a GEOMETRIC amplification factor: at the identity, all dim(p,q) representations interfere constructively, while at generic points they destructively interfere with essentially random phases. The BCS weights modulate this, but the dominant effect is the geometric coherence of the group.

The user's interpretation: this geometric amplification IS the substrate's self-coherence. The substrate is not a material with a pairing field on it. It is a geometry whose internal self-consistency is measured by how coherently its representations add at any given point. The identity is the point of maximum coherence -- every mode agrees. The 10^6 measures the dynamic range of that agreement.

**My verdict**: The reframe elevates the 10^6 from "mathematical artifact of Fourier analysis on a compact group" to "the substrate's coherence dynamic range, physically set by BCS weights." The distinction is whether you view the character expansion as spectroscopy (measuring the weight of each harmonic -- an observer's decomposition) or as a physical correlation function (the substrate measuring itself). The user is proposing the latter. This is defensible but requires a self-consistency argument I develop in Section 2.

---

## 2. What Self-Consistency Means at the Substrate Level

In nuclear HFB, self-consistency has a precise operational definition. You start with a trial density rho_0(r). You compute the mean-field potential U[rho_0]. You solve the HFB eigenvalue problem to get quasiparticle wave functions (u_k, v_k). You compute the new density rho_1 = sum_k |v_k|^2 and pair tensor kappa_1 = sum_k u_k v_k*. You iterate until rho_n = rho_{n-1} to desired precision. The loop closes through position space: the density determines the potential determines the wave functions determine the density.

For the substrate, the analogous loop must close through the GEOMETRY. The proposed structure:

1. **Metric g_{ij}(tau) determines the Dirac spectrum.** This is computed: the Jensen metric at each tau gives D_K(tau), whose eigenvalues are the single-particle spectrum.

2. **The Dirac spectrum determines the BCS state.** This is computed: given eigenvalues and the interaction V, solve the gap equation to get (u_k, v_k, Delta_s).

3. **The BCS state determines an energy functional E[g_{ij}].** This is the MISSING STEP. The total energy of the paired state -- kinetic + pairing -- is a functional of the metric g_{ij} through its dependence on the spectrum. In Connes' spectral action framework, this functional is Tr f(D^2/Lambda^2) plus a pairing correction. In the nuclear analog, it is E[rho, kappa] = Tr[h*rho] + (1/2)*Tr[Delta*kappa*].

4. **Minimization of E[g_{ij}] over the space of metrics determines g_{ij}.**

The nuclear DFT analog is exact: replace "density rho(r)" with "metric g_{ij}" and "mean-field potential U[rho]" with "Dirac operator D_K[g]." The self-consistency condition becomes:

    delta E_total / delta g_{ij} = 0

where E_total = E_spectral[g] + E_BCS[Delta(g), g] + E_geometric[g].

This is not merely an analogy. It is the SAME variational principle in a different space. Nuclear HFB minimizes over the space of Slater determinants (which parametrize densities). Substrate HFB would minimize over the space of left-invariant metrics on SU(3) (which parametrize the single-particle basis through D_K).

The Jensen metric is a 2D subspace of the full 36D space of left-invariant metrics (after the volume constraint). Current computations fix the metric at each tau and solve BCS on that fixed background. This is the analog of computing BCS gaps at a fixed deformation beta_2 WITHOUT allowing the deformation to respond to the pairing. In nuclear physics, this is called "constrained HFB" -- you get the potential energy surface E(beta_2), not the self-consistent ground state. What we have is E(tau), not the self-consistent tau.

The fold tau = 0.19 was identified from geometric considerations (the spectral action or q-theory crossing). The substrate self-consistency question is: does the BCS pairing energy, added to the geometric energy, shift the minimum? In nuclear terms: does the pairing correlation energy change the equilibrium deformation?

The answer, from S46 GCM-ZERO-POINT-46, is that the BCS state is extremely rigid in tau: Delta_B2 = 1.334 >> delta_E_sp ~ 0.06, giving a GOA width sigma_tau = 3.34 >> the variation scale. The pairing does NOT select a different tau. This is the nuclear analog of a closed-shell nucleus (like ^208Pb) where the mean field is so stiff that pairing does not change the shape. The substrate at the fold is self-consistent in the trivial sense: pairing does not break the geometric self-consistency because the geometry is too rigid for pairing to deform.

This actually SUPPORTS the user's interpretation. A self-consistent substrate should be rigid -- its geometry should not be distorted by the pairing field that lives on it. The 10^6 coherence contrast is a property of the rigid geometry, not of the pairing. The pairing adapts to the geometry; the geometry does not care about the pairing. This is what "neutral" means: the substrate imposes no structure because it IS the structure, and it is too stiff for anything living on it to push back.

---

## 3. "Near Are Like": The Two-Point Correlation Function

The user's phrase "near are like" is a statement about the two-point correlation function of the substrate. Let me formalize it.

Define the character coherence function on SU(3):

    C(g_1, g_2) = sum_{(p,q)} w_{(p,q)}^2 * chi_{(p,q)}(g_1^{-1} * g_2)

where w_{(p,q)} are the BCS weights from W2-1. This is a class function of the "separation" g_1^{-1} * g_2, so it depends only on the conjugacy class of the relative group element. On the maximal torus, this reduces to:

    C(theta, 0) = sum_{(p,q)} w_{(p,q)}^2 * chi_{(p,q)}(theta)

The contrast ratio is:

    C(0, 0) / C(theta_far, 0) = 3.14 x 10^6

where theta_far is the farthest point on T^2 from the identity.

The correlation length xi_C is defined by:

    C(theta, 0) ~ C(0, 0) * exp(-|theta|^2 / (2*xi_C^2))

near the identity. From W2-1: the 1/e^2 radius is 0.78 rad, so xi_C = 0.78 / sqrt(2) = 0.55 rad.

The "diameter" of SU(3) in the bi-invariant metric is pi (the farthest geodesic distance from the identity on the maximal torus). The ratio:

    xi_C / d_SU(3) = 0.55 / pi = 0.18

So the correlation length is about 1/6 of the SU(3) diameter. This is a SHORT-range correlation function. "Near are like" is precise: elements within 0.55 rad of each other (roughly 1/6 of the manifold) share strong coherence. Elements farther apart are incoherent by factors of 10^3 to 10^6.

But now compare this to the BCS coherence length in the system. The 0D limit gives L/xi_GL = 0.031, meaning xi_GL ~ 32 * L_SU(3). The BCS coherence length is 32 times the size of the manifold. So:

    xi_BCS >> L_SU(3) >> xi_C

The BCS coherence length is enormous (the pairing is perfectly coherent across the entire manifold). The CHARACTER coherence length is short (the geometric self-similarity decays over 1/6 of the diameter). These are measuring different things.

xi_BCS measures: "how far apart can two paired fermions be and still contribute to the condensate?" Answer: across the entire manifold. The condensate is spatially uniform in the pairing sense.

xi_C measures: "how far from the identity do characters remain coherent (constructively interfering)?" Answer: about 1/6 of the diameter. This is the substrate's geometric self-similarity scale.

The user's reframe conflates these two, and -- here is the key insight -- it may be correct to do so for a substrate that IS the geometry. In a nucleus, xi_BCS and the nuclear radius R are physically independent quantities (one measures pair coherence, the other measures the spatial extent of the confining potential). For the substrate, there IS no confining potential separate from the geometry. The geometry's self-coherence IS the "potential well" in which the pairing lives. The character coherence function C(g_1, g_2) is not a correlation function OF something living ON the geometry -- it is the geometry's own auto-correlation.

The separation of xi_BCS >> xi_C then has a clean interpretation: the BCS condensate is perfectly coherent across the entire substrate (0D limit, single coherence patch), but the substrate itself has internal geometric texture (xi_C = 0.18 * diameter) that the condensate does not smooth out. The condensate sees the geometry; the geometry does not see the condensate.

---

## 4. What Transfers from Nuclear DFT

Let me be concrete about which nuclear DFT methods survive the transition to "geometry as the dynamical object."

### 4.1 What Transfers Directly

**The Bogoliubov quasiparticle picture.** The Bogoliubov transformation a_k = u_k gamma_k + v_k* gamma_bar_k* is purely algebraic. It requires a single-particle basis (we have one: D_K eigenvalues) and an attractive interaction in at least one channel (we have V(B2,B2) = 0.256). The quasiparticle spectrum E_k = sqrt((epsilon_k - lambda)^2 + Delta_k^2) is computed from the same data regardless of whether the single-particle states live in a nuclear potential well or are eigenvalues of a Dirac operator on a Lie group. THIS IS WHAT WAS DONE in Sessions 34-46, and it works. Paper 03's entire formalism transfers because it is algebraic, not spatial.

**The pairing functional E_pair[Delta].** In nuclear DFT, E_pair = Tr[Delta * kappa*] where Delta is the gap and kappa is the pair tensor. On SU(3), the same functional applies with the identification: Delta_s = the sector-resolved gap, kappa_s = u_s * v_s for each spinor mode. S46 computed this. The functional form is basis-independent.

**Number projection (PBCS).** Paper 03 Sec IV warns that BCS breaks down for small systems. S46 confirmed: PBCS matches ED to 0.1% while BCS overestimates by 60%. The Lipkin-Nogami approximate number projection transfers directly because it is a correction to the BCS wave function, not a statement about the spatial structure.

**Bayesian UQ (Paper 06).** The methodology -- GP emulators for the gap model, posterior distributions over parameters, KL divergence for information content -- is entirely agnostic to the underlying physics. S46 BAYESIAN-GP-46 demonstrated this: tau* = 0.221 +/- 0.117 with 99.2% of variance from gap model choice. Paper 06's central lesson ("no single parametrization unambiguously preferred") transferred verbatim.

### 4.2 What Transfers With Modification

**The Kohn-Sham mapping.** In nuclear DFT, the Kohn-Sham strategy maps the interacting many-body problem onto a non-interacting system in an effective potential, such that the density of the non-interacting system equals the exact density. This requires an external potential (the nuclear mean field) to define "the system."

For the substrate, there is no external potential. The "mean field" IS the metric. The Kohn-Sham mapping would become: find a free Dirac operator on some reference metric g_0 such that its spectral density equals the interacting spectral density on the physical metric g. This is a SPECTRAL inverse problem, not a density inverse problem. It is well-defined mathematically (Connes' reconstruction theorem says the metric is determined by the Dirac spectrum up to isometry). But it is computationally different from nuclear Kohn-Sham: instead of adjusting a potential, you adjust a metric. The cost functional would be:

    min_{g_0} || rho[D_{g_0}] - rho[D_g + V_pair] ||

where rho is the spectral density (eigenvalue distribution function). This has never been implemented, but the mathematical framework exists.

**The self-consistency iteration.** In nuclear HFB, you iterate rho -> U[rho] -> HFB -> rho until convergence. For the substrate, the iteration would be: g -> D_K[g] -> BCS -> E[g, Delta] -> delta E / delta g = 0 -> g. The first three steps are already computed. The fourth requires computing the gradient of E_total with respect to the metric parameters. Within the Jensen 2-parameter family, this is a 1D minimization (after the volume constraint). Within the full 36D space, it is a high-dimensional optimization that Paper 06's GP emulator methodology is designed to handle.

### 4.3 What Does Not Transfer

**The density-dependent pairing functional.** In nuclear DFT, Delta(r) = -G_0[1 - eta*rho(r)] * kappa(r), where the density dependence captures the saturation of the nuclear force at high density (Paper 02, Paper 03). For the substrate, there is no analog of "local nucleon density" at a point on SU(3). The pairing interaction V_{kk'} is defined in the representation basis (sectors B1, B2, B3), not in position space. A "density-dependent" pairing on SU(3) would have to be a pairing interaction that depends on the local spectral density -- a functional of the eigenvalue distribution, not of the position-space density. This is a qualitatively different object.

**Continuum coupling.** Paper 02's central innovation was treating the nuclear continuum (unbound scattering states). The substrate on compact SU(3) has no continuum -- the spectrum is purely discrete (compact manifold, no scattering states). The Berggren contour, the extended pair amplitudes at the drip line, the coupling to particle-emission channels -- none of this has a substrate analog. The 0D limit is the opposite extreme: everything is bound, everything is discrete, the coherence length is infinite.

**Cranking and rotation.** Paper 08's cranking Hamiltonian H_rot = H_0 - omega*J_x describes a nucleus rotating with angular velocity omega. The substrate does not rotate. There is no external torque, no broken rotational symmetry to restore. The analog would be a "deformation-dependent" computation (varying tau), which IS what we do -- but the cranking interpretation (rotating frame) does not apply.

---

## 5. The Decisive Computation

The user asks for ONE computation that tests whether the character coherence function is genuinely a substrate self-coherence measure versus a Fourier artifact.

Here is the test.

**DEFORMATION RESPONSE OF THE CHARACTER COHERENCE FUNCTION**

Compute C(theta, 0; tau) -- the character coherence function on T^2 -- at 26 tau values in [0, 0.50]. Extract the 1/e^2 radius r_C(tau) at each tau. Two predictions:

**If C is a Fourier artifact (null hypothesis)**: the 1/e^2 radius will track the truncation level, not the physics. Specifically, r_C will be determined primarily by the highest representation included (max_pq_sum), and will converge to a value that depends on the truncation but not on tau. The contrast ratio will be approximately dim(max_rep)^2 / dim(min_rep)^2 at every tau, because the identity peak is kinematic. The BCS weights will modulate this weakly (a factor of 2-3) but will not produce qualitatively different behavior at different tau.

**If C is a substrate self-coherence measure (alternative hypothesis)**: the 1/e^2 radius will track the BCS coherence energy Delta_B2(tau), not the truncation. Specifically, r_C(tau) should scale as 1/Delta_B2(tau) -- wider coherence patch when pairing is weaker (less spectral weight in higher representations means slower character decay), narrower when pairing is stronger. The contrast ratio will vary by orders of magnitude across tau, reflecting the changing strength of the substrate's self-coherence. At the critical point tau_c where BCS pairing vanishes, the coherence function should flatten to a truncation-dominated pattern -- the substrate loses its self-coherence when it loses its condensate.

The decisive criterion: plot r_C(tau) versus Delta_B2(tau). If they anti-correlate with a correlation coefficient |r| > 0.9 across the 26 tau values, the coherence function is dynamically determined (substrate self-coherence). If |r| < 0.3, it is kinematically determined (Fourier artifact).

This computation requires only infrastructure that already exists: the Dirac spectrum at 26 tau values (from s44_dos_tau.npz), the BCS gaps at each tau (computable from s39 V matrix), and the character evaluation code (from s47_condensate_torus.py). The extension is to run the condensate torus computation at all 26 tau values instead of just the fold.

The nuclear analog is direct. In a deformed nucleus, the pairing field Delta(r) changes shape when the deformation changes. At spherical shape (beta_2 = 0), Delta(r) follows the spherical density. At large deformation, Delta(r) becomes prolate or oblate. The RESPONSE of the pairing field to deformation is the test of self-consistency -- a truly self-consistent solution has the pairing field track the density, not the external potential. Here, the RESPONSE of C(theta; tau) to the Jensen deformation parameter tau is the test of whether the coherence function tracks the BCS physics (substrate interpretation) or the truncation (artifact interpretation).

---

## 6. Closing

The user is right that I was applying the wrong scale. Nuclear BCS has low contrast because it is a perturbation on a pre-existing spatial background whose smoothness limits the dynamic range. The substrate has no pre-existing background -- it IS the background. The 10^6 measures the dynamic range of the geometry's self-agreement, amplified by the group-theoretic fact that all representations constructively interfere at the identity.

My self-consistency critique stands but is reframed: the question is not whether the condensate profile is self-consistent on SU(3) (it cannot be, in the 0D limit -- the condensate is the system), but whether the GEOMETRY is self-consistent with the pairing it supports. The S46 GCM result says yes, trivially: the geometry is too rigid for the pairing to deform it. This is what a neutral substrate should do. It should be indifferent to what lives on it.

What transfers from nuclear DFT: the Bogoliubov algebra, the pairing functional, number projection, Bayesian UQ, and the variational principle delta E / delta g = 0. What does not: density-dependent pairing, continuum coupling, cranking. The spectral inverse problem (finding a reference metric whose free spectrum matches the interacting spectrum) is the substrate analog of Kohn-Sham, and it is mathematically well-defined but unimplemented.

The decisive test is the deformation response of the character coherence function. If r_C(tau) anti-correlates with Delta_B2(tau), the 10^6 is dynamical. If it does not, it is kinematic. This computation uses existing infrastructure and can be run as a single script.

The substrate thinks in characters, not in coordinates. That is the reframe. My job is to make sure the characters close the self-consistency loop.

---

**Files referenced**:
- My review: `sessions/session-47/session-47-crystal-geometry-nazarewicz-collab.md`
- Tesla crystal geometry: `sessions/session-47/session-47-crystal-geometry.md`
- W2-1 condensate: `sessions/session-47/session-47-wave1-workingpaper.md` (W2-1 section)
- Paper 02: `researchers/Nazarewicz/02_1996_Dobaczewski_Mean_Field_Drip_Line_Pairing.md`
- Paper 03: `researchers/Nazarewicz/03_2013_Dobaczewski_HFB_Pairing_Hamiltonian.md`
- Paper 06: `researchers/Nazarewicz/06_2015_McDonnell_Uncertainty_Quantification_DFT.md`
