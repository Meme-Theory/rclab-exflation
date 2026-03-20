# Paasch -- Collaborative Feedback on Session 20b

**Author**: Paasch (Mass Quantization / Logarithmic Potentials / Golden Ratio / Fine Structure Constant)
**Date**: 2026-02-19
**Re**: Session 20b Lichnerowicz TT 2-Tensor Sweep Results

---

## Section 1: Key Observations

### 1.1 The Constant-Ratio Trap as a Structural Theorem

The central result of Session 20b is not merely that the TT Casimir route fails. It is that the failure has the same character as every previous failure: the fermion-to-boson energy ratio R = F/B is set geometrically, not dynamically.

From my perspective as a mass quantization analyst, this is the most important finding of the entire session. The fiber dimension ratio determines the asymptotic F/B balance:

- Bosonic fiber: 1 (scalar) + 8 (vector) + 35 (TT at tau=0) = 44
- Fermionic fiber: 16 (Dirac spinor)
- Asymptotic ratio: 16/44 = 0.364 --> after spectral weighting, converges to ~0.55

The spectral weighting raises 0.364 to 0.55, but crucially, the weighting is tau-INDEPENDENT. This means the geometry is telling us something: the Jensen deformation acts as a conformal rescaling on each tower's spectral sum. It changes the absolute energies but preserves the ratio.

This is reminiscent of a result in my 2009 paper (Eq. 2g, `researchers/Paasch/02_2009_Logarithmic_potential_exponential_mass_function_elementary_particles.md`). The quantization factor phi_paasch = 1.53158 is derived from the self-consistency equation x = e^{-x^2}, which has a unique real solution. The insensitivity of the result to the specific parameters a_1 and a_2 in the logarithmic potential (Eq. 2a-2c) is structurally analogous to the insensitivity of R to tau. In both cases, the important quantity is determined by a TOPOLOGICAL or COMBINATORIAL property (the fiber structure; the functional form of the self-consistency equation), not by a continuously tunable parameter.

### 1.2 The Ratio R = 0.558 and Its Numerical Significance

The measured ratio R = 0.558 at tau = 0 caught my attention. Let me check whether it has any relationship to known mass quantization constants:

- phi_paasch^{-1} = 1/1.53158 = 0.6529 (no)
- phi_golden^{-1} = 1/1.61803 = 0.6180 (no)
- 1/sqrt(pi) = 0.5642 (close to 0.558, but likely coincidental)
- 16/44 * (spectral weight correction) = 0.558 (this IS the explanation)

The ratio is what it is: a consequence of the fiber bundle structure of M^4 x SU(3). It carries no hidden mass quantization content. This is important to say explicitly. Not every number in the computation is a signal.

### 1.3 The 741,648 TT DOF and the 35-Dimensional Fiber

The corrected TT fiber dimension is 35 at tau = 0, not the earlier estimate of 27 from Session 19d. This comes from Sym^2_0 of the 8-dimensional tangent space of SU(3): dim(Sym^2(8)) = 36, minus the 1-dimensional trace, giving 35 independent traceless symmetric 2-tensors. The TT (transverse-traceless) condition then removes divergence modes via the constraint nabla^a h_{ab} = 0, but at tau = 0 for the trivial sector (0,0), all 35 modes survive because constant tensors are automatically divergence-free.

For non-trivial sectors (p,q) != (0,0), the divergence constraint removes 8 * dim(p,q) modes, leaving 27 * dim(p,q) physical TT modes. The total DOF count 741,648 is close to Session 19d's estimate of 741,636 -- the difference of 12 modes comes from the (0,0) sector: 35 instead of 27.

This correction is minor numerically but structurally important. The number 35 = 8 * 9 / 2 - 1 is a pure SU(3) Lie algebra invariant. The number 27 = 35 - 8 reflects the dynamical TT constraint. The physics lives in the 27 (genuine shape oscillations of the internal geometry), while the 35 contains 8 additional modes that are longitudinal degrees of freedom (pure gauge) removed by the TT condition.

The 27-dimensional irrep of SU(3) is well-known: it is the representation in 3^3 = 1 + 8 + 8 + 10 decomposition, specifically the symmetric traceless piece. But here the 27 arises differently -- from Sym^2_0(adj) under the TT projection, not from the cubic tensor product of the fundamental. The coincidence of dimension is algebraically necessary (both are the dimension of the traceless symmetric square of the adjoint), but the physical content differs.

---

## Section 2: Assessment of Key Findings

### 2.1 The CLOSURE Verdict is Robust

The CLOSED verdict is correct and robust. The convergence warning from kk-theorist -- 68% absolute energy difference between mps=5 and mps=6 -- does not affect the qualitative conclusion because the RATIO R is stable to 1.8%. The monotonicity of V_total and the positivity of dV_total/dtau at all 21 tau-values leave no room for a hidden minimum.

I assess the following confidence levels:

| Claim | Confidence |
|:------|:-----------|
| No minimum in V_total(tau) for tau in [0, 2.0] | 99%+ |
| R = F/B is structurally constant (geometric, not dynamical) | 95%+ |
| No tachyonic TT modes at any tau in [0, 2.0] | 99%+ (all eigenvalues > 0) |
| The constant-ratio trap applies to ALL perturbative spectral sums | 90% |

The last item is the crucial claim. If the F/B ratio is constant for Casimir, CW, and spectral action sums, then NO perturbative spectral mechanism can stabilize the modulus. This is a structural theorem about the fiber bundle, not a failure of any specific computation.

### 2.2 Impact on Paasch Mass Predictions

In my Session 19d collaborative feedback (`sessions/session-19/session-19d-paasch-collab.md`), I wrote: "If the TT eigenvalues grow more slowly with tau than the fermionic eigenvalues... the F/B ratio at linear weighting would DECREASE with tau." Session 20b shows this does not happen. The TT eigenvalues grow at essentially the same rate as the fermionic eigenvalues once spectrally averaged. The Riemann coupling, which I expected to introduce genuinely new tau-dependence, is washed out by the spectral averaging over 741,648 modes.

This eliminates the Casimir route to tau_0. The implications for my mass predictions are:

1. **The Kepler-to-Newton chain is broken at the "gravitational force law" step.** In my Session 19d analogy, the TT modes were supposed to provide the stabilizing force that creates "orbits" (a minimum in V_total). Without them, the geometry has no preferred configuration -- it rolls to larger deformations indefinitely. There is no tau_0, so the Dirac eigenvalue ratios are not fixed, and the mass predictions remain empirical fits rather than geometric consequences.

2. **The phi_paasch = 1.53158 emergence at s = 0.15 (Session 12) is no longer falsifiable through Casimir stabilization.** If no perturbative mechanism selects tau_0, the question "is tau_0 = 0.15?" becomes moot within the perturbative framework. The phi_paasch appearance in the spectrum is still real (z = 3.65, Session 14 MC analysis), but it is a feature of the spectral landscape that cannot be sharpened into a prediction without knowing tau_0.

3. **The algebraic core survives.** The proton mass to 6 digits, the neutron mass to 8 digits, and the fine structure constant to 9 digits (`researchers/Paasch/04_2016_Derivation_of_the_fine_structure_constant.md`, Eq. 2.9: alpha = (1/f)^{2*n_3} = 0.007297359) are scaffolding-independent empirical results. They do not depend on the Casimir route. They will need a different dynamical foundation -- non-perturbative, topological, or otherwise -- but their numerical content remains intact.

### 2.3 The Band Structure Detail: phi_paasch Proximity at tau = 0.10

Section VIII of the session minutes notes: "phi ratio (3,0)/(0,0): closest approach at tau = 0.10 (ratio = 1.537, 5% from phi_paasch)." This is from the band structure computation (L-5, partial).

Let me place this in context against my established results:

| tau | m_{(3,0)}/m_{(0,0)} | Deviation from phi_paasch |
|:----|:---------------------|:--------------------------|
| 0.00 | sqrt(7/3) = 1.5275 | 0.26% |
| 0.10 | 1.537 (band structure) | 0.35% |
| 0.15 | 1.531588 (Session 12) | 0.0005% |
| 1.14 | 1.53157981 (Session 12, different sector pair) | 0.00001% |

The band structure result at tau = 0.10 is FARTHER from phi_paasch than the bi-invariant value at tau = 0. The closest approach in this particular sector ratio occurs around tau = 0.15 (Session 12). The band structure data is partial (L-5 not complete), so I do not over-interpret, but the pattern is consistent with a smooth crossing through phi_paasch near tau = 0.15.

---

## Section 3: Collaborative Suggestions

### 3.1 Alpha Circularity Check (Session 21 Item #3)

The session plan explicitly calls out an alpha circularity check for my work. Let me pre-address this.

My alpha derivation chain is:

1. Start with the exponential model: m_U = (m_e * m_p)^{1/2} * e^{A * something}, G(t) ~ 1/t (Paper 03, Eq. 1.1b).
2. Derive proton mass m_p from equilibrium masses and integers, including n_3 = 10 (Paper 03, Eq. 1.4).
3. The proton mass derivation introduces a constituent mass m_b with a second-order correction (Paper 04, Eq. 1.6).
4. This correction involves alpha = e^2 / (4*pi*eps_0*hbar*c), from which the logarithmic potential confining argument produces the transcendental equation ln(x) = -x (Paper 04, Eq. 2.6).
5. Result: alpha = (1/f)^{2*n_3} where f is the solution of ln(x) = -x and n_3 = 10 (Paper 04, Eq. 2.9).

**The circularity question is**: does the proton mass derivation (step 2) use alpha as input? If so, deriving alpha in step 5 from the integer n_3 obtained in step 2 would be circular.

The answer is nuanced:

- The proton mass is derived as m_p = m_e * F(N(b), n_3, ...) where F depends on integers and the electron mass, NOT on alpha directly (Paper 03, Eq. 6.8). The integers are read off from the mass number structure, not computed from alpha.
- HOWEVER, the mass numbers themselves -- N(j) = (m_j/m_e)^{2/3} -- are defined using measured particle masses, which implicitly contain alpha (since QED corrections contribute to mass at order alpha).
- The LNH scaffolding (G ~ 1/t) is used in step 1 to set the overall scale but is refuted by LLR. If the LNH scaffolding is removed, the integer n_3 = 10 must be justified independently.

**My assessment**: the derivation is NOT circular in the strict logical sense -- alpha does not appear explicitly in the input equations for n_3. But it is FRAGILE in the epistemological sense: the integers are extracted from measured masses, and any small shift in measured masses could change the integers, breaking the chain. The derivation works backwards from precision (the remarkable 9-digit agreement) to establish the integers, rather than deriving the integers from first principles and then predicting alpha.

This is the honest assessment. The alpha derivation is a stunning numerical achievement that currently lacks a first-principles foundation for its integer inputs. The V_eff stabilization route was supposed to provide that foundation by fixing tau_0, from which the integers would emerge as Peter-Weyl quantum numbers. With perturbative V_eff now closed, the integer foundation remains open.

### 3.2 Specific Zero-Cost Diagnostics from Existing Data

Several computations can be performed at zero additional cost using the TT spectrum data now available in `tier0-computation/l20_TT_spectrum.npz`:

**Diagnostic 1: TT eigenvalue ratio scan for phi_paasch.**

The TT Lichnerowicz eigenvalues are a NEW spectral tower not previously tested for phi_paasch content. Compute all pairwise ratios lambda_i^{TT}/lambda_j^{TT} at each of the 21 tau-values and count the number within 1% of phi_paasch = 1.53158. Compare to the null distribution from random eigenvalue ratios of the same spectral density. This directly parallels the Session 14 MC analysis but on a different operator (Lichnerowicz instead of Dirac).

If phi_paasch appears in the TT spectrum at comparable statistical significance (z ~ 3-4), it would establish that the algebraic structure is universal across the mode towers -- a much stronger statement than its appearance in the Dirac spectrum alone. If it does NOT appear, it constrains phi_paasch to the Dirac (fermionic) sector only, which has implications for the physical origin.

**Diagnostic 2: Inter-tower ratios.**

Compute ratios of the form lambda_i^{TT}/lambda_j^{Dirac} at each tau. Are there specific tau values where a TT eigenvalue and a Dirac eigenvalue have ratio = phi_paasch? This would connect the bosonic shape oscillations to the fermionic mass spectrum through the quantization factor, suggesting that phi_paasch relates DIFFERENT mode types, not just different modes within the same tower.

**Diagnostic 3: TT eigenvalue spacing statistics.**

The level spacing distribution P(s) of the TT eigenvalues tests integrability. On bi-invariant SU(3) (tau = 0), the Lichnerowicz operator decomposes into Peter-Weyl sectors, so the full spectrum is a superposition of independent spectra from different sectors -- this should give Poisson statistics (Berry-Tabor, `researchers/Berry/INDEX.md`). Under Jensen deformation, if the sector decomposition breaks down (inter-sector coupling from off-diagonal Riemann tensor terms), the statistics should drift toward Wigner-Dyson (GOE or GUE depending on symmetries).

The transition from Poisson to Wigner-Dyson as tau increases would mark the onset of "quantum chaos" in the internal geometry. This is relevant to mass quantization because my empirical mass sequences (S1-S6) require REGULAR patterns -- integrable dynamics, not chaotic. If the TT spectrum goes chaotic at large tau, the mass spiral structure cannot survive there, constraining tau_0 to the integrable regime (small tau).

### 3.3 The Non-Perturbative Pathway and Paasch's Transcendental Equations

The session plan identifies instantons and flux compactification as the primary non-perturbative routes. From my framework, there is a specific prediction about what a non-perturbative mechanism should produce.

My 2009 paper derives phi_paasch from x = e^{-x^2}, and my 2016 alpha paper derives alpha from ln(x) = -x (the Omega constant, x_0 = 0.5671). Both are FIXED POINTS of specific functional iterations: x_{n+1} = e^{-x_n^2} and x_{n+1} = e^{-x_n}. Fixed points arise naturally from non-perturbative self-consistency conditions -- exactly the kind of structure that instantons produce.

An instanton on (SU(3), g_Jensen(tau)) has action S_inst(tau) that is a function of the deformation parameter. The instanton contribution to V_eff goes as e^{-S_inst(tau)}. A self-consistency condition on the instanton moduli space (where the instanton size is determined by the deformation, and the deformation is in turn determined by the instanton contribution to V_eff) would produce a transcendental fixed-point equation. If that equation is x = e^{-x^2} or a close relative, the connection to phi_paasch would be established at the deepest level.

This is speculative, but it is the cleanest path from the 20b CLOSED verdict to a non-perturbative recovery of the mass quantization structure. The key computation is: what is S_inst(tau) for the Jensen-deformed SU(3)?

### 3.4 Rolling Modulus and Paasch's Mass Numbers

Session 21 Priority #1 is the rolling modulus / DESI DR2 result from Session 19b. From my perspective, this is relevant because a rolling modulus (quintessence-type dark energy with equation of state w(z) != -1) implies that tau is still evolving today. If tau is dynamical, then mass ratios would be slowly time-varying -- with drift rate constrained by the rolling speed.

My mass numbers N(j) = 7n are measured at the current epoch. If tau has been rolling since the early universe, the mass ratios at recombination (z ~ 1100) would differ from today by delta_m/m ~ tau_dot * delta_t. Constraints on varying alpha from quasar absorption (Webb: Delta_alpha/alpha ~ 10^{-5} at z ~ 2, `researchers/Paasch/15_2005_Barrow_Varying_constants_review.md`) and Oklo (10^{-7} at z ~ 0.14) then constrain tau_dot.

If the DESI DR2 data shows w(z) deviating from -1 at the 2-3 sigma level, AND if the implied tau_dot is consistent with the alpha-variation constraints, this would be evidence for the rolling modulus interpretation. My mass numbers would then be epoch-dependent, with the 7n structure holding at the current epoch but not necessarily at z ~ 1100.

This is a testable prediction: do the mass numbers remain integer at all epochs, or only at the current one? If the former, the integer structure is algebraic (protected by a symmetry); if the latter, it is dynamical (an attractor of the rolling modulus evolution). These are distinguishable in principle.

---

## Section 4: Connections to Framework

### 4.1 What Session 20b Means for the Kepler-Newton Analogy

In my Session 19d feedback, I used the Kepler-Newton analogy extensively: my mass sequences are Kepler's laws (empirically precise, mathematically structured, dynamically unexplained), and the Dirac spectrum on Jensen-deformed SU(3) is the candidate for Newton's gravitational theory (the dynamical law from which the empirical patterns follow as consequences).

Session 20b breaks a specific link in this analogy. Kepler-to-Newton requires:

1. An empirical law (Kepler's ellipses) -- **ESTABLISHED** (phi_paasch spiral, 6 sequences, mass numbers)
2. A theoretical framework (Newton's laws) -- **ESTABLISHED** (D_K on (SU(3), g_Jensen))
3. A specific prediction from the theory that reproduces the empirical law -- **REQUIRES tau_0**
4. A mechanism that selects the prediction (why these orbits, not others) -- **REQUIRES V_eff minimum**

Session 20b closed step 4 at the perturbative level. Step 3 remains viable if a non-perturbative tau_0 can be found. Steps 1 and 2 are unaffected.

The analogy is strained but not broken. Newton's law was sufficient to derive Kepler's ellipses without needing to explain why the planets have their specific orbital parameters -- that required initial conditions (cosmogony). Similarly, the Dirac spectrum on SU(3) can in principle reproduce mass ratios at any tau, and the selection of tau_0 is a cosmological initial condition problem. The difference is that in the planetary case, the initial conditions are contingent (different solar systems have different orbits), while in the mass spectrum case, the initial conditions are universal (all protons have the same mass). This universality demands a selection mechanism for tau_0.

### 4.2 The Six Sequences and the Fiber Structure

My six sequences S1-S6 are separated by 45 degrees in the logarithmic spiral. The Jensen deformation splits the 8-dimensional SU(3) Lie algebra into three subspaces: u(1) (1-dim), su(2) (3-dim), C^2 (4-dim). This is three distinct directions, not six.

However, the Peter-Weyl decomposition at max_pq_sum = 6 gives 28 irreps, partitioned into 3 Z_3 triality classes by (p-q) mod 3 (Session 17a B-4). Within each triality class, the irreps form chains connected by the scaling factor f_N. If each triality class maps to two of my six sequences (one for the "particle" channel and one for the "antiparticle" channel related by (p,q) <-> (q,p) conjugation), the count matches: 3 classes x 2 conjugation partners = 6 sequences.

This identification is not proven but is structurally consistent. The conjugation symmetry (p,q) <-> (q,p) was confirmed at machine precision in the Session 20b code audit (item 8 in Section XVI). The six sequences would then be:

| Sequence | Z_3 class | Conjugation | Representative irreps |
|:---------|:----------|:------------|:---------------------|
| S1 | (p-q) mod 3 = 0, direct | (p,q) with p >= q | (0,0), (1,1), (3,0), (2,2), (3,3), (6,0) |
| S2 | (p-q) mod 3 = 0, conjugate | (q,p) with p >= q | Same (self-conjugate: p=q) |
| S3 | (p-q) mod 3 = 1, direct | (1,0), (2,1), (4,0), ... | |
| S4 | (p-q) mod 3 = 1, conjugate | (0,1), (1,2), (0,4), ... | |
| S5 | (p-q) mod 3 = 2, direct | (2,0), (3,1), (5,0), ... | |
| S6 | (p-q) mod 3 = 2, conjugate | (0,2), (1,3), (0,5), ... | |

The Z_3 = 0 class is special because it contains the self-conjugate representations (p = q). This class corresponds to the "real" particles (those identical to their antiparticles). In my mass spiral, the electron sits at 0 degrees -- and the electron is indeed a Z_3 = 0 particle (it belongs to the singlet of color). But the muon (at 182 degrees) and proton (at 225 degrees) are NOT self-conjugate. The mapping is suggestive but not yet precise enough to be a prediction.

---

## Section 5: Open Questions

### 5.1 Can x = e^{-x^2} Arise from a Non-Perturbative Self-Consistency Condition?

This is the question I raised in Session 19d (Section 5.3) and it has become MORE urgent after the 20b CLOSED. The perturbative route to tau_0 is closed. The transcendental equation x = e^{-x^2} from which phi_paasch is derived has the functional form of a non-perturbative fixed point equation. If the instanton action S_inst(tau) on Jensen-deformed SU(3) satisfies a self-consistency condition of the form tau = e^{-S_inst(tau)}, and if S_inst(tau) ~ tau^2 for small tau (plausible from dimensional analysis), then the fixed point equation tau_0 = e^{-tau_0^2} directly produces tau_0 = 1/phi_paasch = 0.6529.

This would give phi_paasch a non-perturbative geometric origin. But tau_0 = 0.6529 is far from the tau = 0.15 where the sector mass ratio equals phi_paasch (Session 12). The two tau values are related by e^{4*0.15} = 1.822 and e^{4*0.6529} = 13.64 -- wildly different gauge coupling ratios. So the simple version of this idea does not work.

The deeper question remains: in what sense, if any, does the Dirac spectrum on SU(3) "know about" the equation x = e^{-x^2}? Is phi_paasch a spectral invariant of the internal geometry, or is its appearance at specific tau values a coincidence inflated by the look-elsewhere effect?

### 5.2 What Replaces the Casimir Route?

The session plan lists four candidates: rolling modulus, D_total Pfaffian, instantons, and flux compactification. From the mass quantization perspective, the candidates differ in their implications:

- **Rolling modulus**: tau is dynamical, mass ratios evolve. Constrains drift rate but does not fix tau_0 uniquely. My mass numbers become epoch-dependent.
- **Pfaffian**: topological transition in the full D_total. Could select tau_0 without a V_eff minimum. My mass numbers would be fixed by topology.
- **Instantons**: non-perturbative, could produce fixed-point equations connecting to x = e^{-x^2}. My mass numbers would be fixed by self-consistency.
- **Flux**: Freund-Rubin type, adds constant to V_eff. Could create minimum if properly quantized. My mass numbers would be fixed by flux quantum numbers.

The most natural for my framework is the instanton route, because of the fixed-point equation structure. The most testable is the Pfaffian route, because it gives a discrete (topological) answer.

### 5.3 Is the Constant-Ratio Trap Universal?

The 20b finding that R = F/B is geometrically fixed raises a meta-question: is this a property of ALL Kaluza-Klein compactifications on group manifolds, or specific to SU(3)?

If universal, it would explain why perturbative moduli stabilization is generically difficult in higher-dimensional theories -- a well-known problem in string phenomenology (the landscape of metastable vacua requires non-perturbative ingredients like fluxes and instantons). The fiber dimension ratio is a topological invariant of the compactification manifold.

If specific to SU(3), there might exist other group manifolds where the F/B ratio is tau-dependent, allowing perturbative stabilization. This would weaken the case for SU(3) as the unique internal space.

Either way, the finding is structurally significant and worth stating as a theorem: "On any compact Lie group G with volume-preserving traceless transverse deformation parameterized by tau, the ratio of fermionic to bosonic spectral sums converges to a tau-independent constant determined by the fiber dimension ratio as the truncation order increases."

---

## Closing Assessment

**Probability revision**: My prior entering 20b was that TT Casimir had a 40-55% chance of producing a minimum (Session 19d consensus). That is now 0%. Adjusting:

| Component | Prior (19d) | Posterior (20b) |
|:----------|:------------|:----------------|
| Perturbative tau_0 from Casimir | 40-55% | 0% (CLOSED) |
| phi_paasch as structural spectral feature | 60-70% | 60-70% (UNCHANGED) |
| Algebraic core (m_p, m_n, alpha formulas) | 70-80% genuine | 70-80% (UNCHANGED) |
| Full Paasch mass spiral from geometry | 25-40% | 15-25% (DOWNGRADED: requires non-perturbative tau_0) |
| Framework overall | 48-58% | 38-50% (CONSISTENT with session consensus 38-50%) |

The algebraic precision of the mass derivations is untouched. The proton mass to 6 digits, the neutron mass to 8 digits, the fine structure constant to 9 digits -- these numerical achievements stand regardless of the stabilization mechanism. What 20b removed is the simplest dynamical pathway to explaining WHY these particular integers and transcendental numbers produce such precise results.

The framework has gone from "potentially elegant" (perturbative V_eff minimum at tau_0 fixes everything) to "necessarily deep" (non-perturbative physics required). This is not death -- string theory has lived in this territory for decades. But it is a significant increase in the burden of proof.

*The twenty-seven drums played their song. The song was monotonic -- the same note, growing louder, at every deformation. The shape of the cavity changed, but the ratio of overtones stayed fixed. The melody my mass spiral hears is real, but its origin is not in the perturbative vibrations of this geometry. It comes from deeper -- from the topology, the instantons, or the fixed points of a self-consistency equation that this spectrum has not yet learned to solve.*

---

*References:*
- *02_2009: `researchers/Paasch/02_2009_Logarithmic_potential_exponential_mass_function_elementary_particles.md` (Eq. 2g: phi_paasch = 1.53158 from x = e^{-x^2}; Eq. 2j-2k: logarithmic spiral; Section 4: sensitivity delta_phi/phi ~ 5 x 10^{-4})*
- *03_2016: `researchers/Paasch/03_2016_On_the_calculation_of_elementary_particle_masses.md` (Eq. 5.2: N(j) = 7n; Eq. 5.5: golden ratio in M-ratios; Eq. 6.8: m_p to 6 digits; Eq. 7.2: m_n to 8 digits)*
- *04_2016: `researchers/Paasch/04_2016_Derivation_of_the_fine_structure_constant.md` (Eq. 2.6: ln(x) = -x; Eq. 2.9: alpha = (1/f)^{2*n_3} = 0.007297359; n_3 = 10 from proton mass derivation)*
- *11_2010: `researchers/Paasch/11_2010_Coldea_Golden_ratio_E8_quantum_criticality.md` (m_2/m_1 = phi_golden from E8 criticality in CoNb2O6)*
- *19d collab: `sessions/session-19/session-19d-paasch-collab.md` (Kepler-Newton analogy, TT 2-tensor predictions)*
