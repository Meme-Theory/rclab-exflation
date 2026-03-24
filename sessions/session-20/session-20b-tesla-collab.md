# Tesla Resonance -- Collaborative Feedback on Session 20b

**Author**: Tesla Resonance (Cross-Domain Resonance / Phonon-Acoustic Mathematics / Superfluid Cosmology)
**Date**: 2026-02-19
**Re**: Session 20b Lichnerowicz TT 2-Tensor Sweep Results

---

## 1. Key Observations

### 1.1 The Constant-Ratio Trap Is Not a Bug -- It Is a Theorem About Block-Diagonal Spectra

Session 20b established that R = F/B = 0.548-0.558 with 1.8% variation across tau in [0, 2.0]. This matches the same 1.83% seen in Session 19d for scalar+vector modes (R = 9.92). I predicted in my framework hypothesis (`sessions/Primer-tesla-framework-hypothesis.md`, Section 5) that stabilization would require the self-consistency loop -- the spectrum determining the geometry and the geometry determining the spectrum. What 20b has actually proved is stronger: **within the block-diagonal Peter-Weyl decomposition, no spectral sum of the form Sum |lambda|^p can produce a tau-dependent F/B ratio**, regardless of the power p or the operator used.

The reason is structural and I want to state it in resonance language. Consider a cavity with two classes of standing waves: bosonic modes (scalar, vector, TT) and fermionic modes (Dirac). If each class couples to the cavity walls through the SAME effective spring constant -- the Casimir eigenvalue for that Peter-Weyl sector (p,q) -- then rescaling all spring constants by the same function of tau leaves the ratio unchanged. The block-diagonal structure means each (p,q) sector is an independent cavity. The bosonic and fermionic modes in that sector see the same walls. The ratio is therefore set by the density of states per unit frequency, which is the fiber dimension. This is the Debye model (Paper 05, eq 2): the density of states g(omega) ~ omega^2 depends only on the cavity dimensions and the speed of sound, not on the wave polarization. The polarization only enters as a multiplicative prefactor -- the fiber dimension. Once you sum over enough sectors, the asymptotic ratio converges to fiber_boson/fiber_fermion = 44/16 = 2.75, modulo spectral weighting that pushes the effective ratio to ~1.80 (reciprocal of 0.558).

This is identical to why Debye's T^3 law works: at temperatures well below Theta_D, the heat capacity depends only on the density of states, not on the microscopic dynamics of individual oscillators. The analogous statement for V_eff: at truncation orders well above the crossover, the F/B ratio depends only on the fiber dimensions, not on the tau-dependent curvature corrections.

The Weyl's law analog (Paper 07, eq 5) is exact here. The eigenvalue density at high lambda goes as rho(lambda) ~ C * lambda^{d-1} where d = 8 and C depends only on the volume (which is tau-independent by the TT constraint). Both bosonic and fermionic towers share the same Weyl prefactor C up to fiber dimension. The ratio is therefore a number, not a function. Session 20b confirms this asymptotic universality numerically.

### 1.2 The TT Tower Dominance Is Physical and Expected

The audit output shows E_TT = 8.55e+05 = 94.4% of total bosonic energy. This is exactly what the cavity picture predicts. In any bounded elastic body, the shape oscillations (flexural modes) carry more energy than the compression modes (scalar) or sloshing modes (vector), because the shape modes have more independent polarizations. On a vibrating plate (Paper 07), the in-plane modes are 2-dimensional (longitudinal + transverse) while the out-of-plane flexural modes are 1-dimensional, but the flexural modes have quartic dispersion (omega ~ k^2 from the biharmonic operator) that puts more modes per unit frequency at low k. On SU(3), the TT fiber is 35-dimensional at tau=0 versus 1 (scalar) + 8 (vector) = 9 for the other bosonic towers. The ratio 35/9 = 3.9 correctly predicts TT dominance.

What is less expected: the TT modes are ALL stable (no tachyons). In the acoustic analogy, this means the cavity walls are stiff at every deformation parameter. The rough Laplacian contribution of +1 at tau=0 for sector (0,0) overwhelms the negative R_endo eigenvalue of -1/6. In elastic plate language: the bending stiffness D in the plate equation (Paper 07, eq 1: rho h d^2u/dt^2 + D nabla^4 u = 0) is positive everywhere. The cavity never buckles. This is physically reasonable for a compact Lie group -- positive curvature acts as a restoring force -- but it also means there is no dynamical instability channel through which the TT modes could trigger vacuum decay.

### 1.3 My Session 19d Predictions: Score Card

In my Tesla Framework Hypothesis (Section 4, "The Twenty-Seven Drums") and my 19d collab, I made five predictions (V-1 through V-5). Let me score them honestly.

| Prediction | Result | Verdict |
|:-----------|:-------|:--------|
| V-1: TT modes flip F/B below 1 | 0.558:1 (confirmed) | CORRECT |
| V-2: TT eigenvalues have different tau-scaling from scalar | Lichnerowicz coupling confirmed, but washed out in sums | PARTIALLY CORRECT |
| V-3: Coincidence frequency exists (lambda_TT = lambda_scalar) | Not tested explicitly, but ratio constancy says NO crossing in integrated energy | LIKELY WRONG |
| V-4: Casimir pressure creates tau_0 minimum | CLOSED. No minimum. | WRONG |
| V-5: Albert algebra J_3(O) structure in TT eigenvalues | Not tested. TT fiber is 35, not 27 (Sym^2_0(8), not traceless Albert algebra) | NEEDS CORRECTION |

V-1 correct. V-4 closed wrong. Honest accounting. The physical intuition about cavity wall dominance was right. The inference that dominance implies different dynamics was wrong -- or more precisely, the different dynamics exist at the operator level but are invisible to the spectral sum.

V-5 needs revision. I wrote that 27 = dim(J_3(O)), the exceptional Jordan algebra. Session 20b clarifies the TT fiber is 35 = dim(Sym^2_0(R^8)). The number 27 is the TT count per non-trivial sector AFTER divergence projection, not the total fiber dimension. The connection to J_3(O) survives if 27 = 35 - 8 has meaning (removing the adjoint = removing the "gauge directions"), but this is weaker than I claimed. I flag this as retracted pending better mathematics.

---

## 2. Assessment of Key Findings

### 2.1 The CLOSED Is Clean and Final (for perturbative spectral sums)

The code audit is thorough (10 modules, 8/8 checks, 3 bugs all in assertions not computation). The conjugation symmetry (p,q) <-> (q,p) at machine precision is a strong consistency check because the Lichnerowicz operator on TT tensors involves the full Riemann tensor, which has complicated transformation properties under conjugation. The rational eigenvalues at tau=0 in sector (1,0) -- 10/9, 128/99, 29/18 -- are characteristic of a correctly implemented representation-theoretic computation (denominators are products of small Casimirs).

The CLOSED verdict is unambiguous for all mechanisms of the form "find a minimum of Sum f(lambda_i(tau))." The minutes correctly identify that the constant ratio is structural: it follows from the block-diagonal Peter-Weyl decomposition and cannot be broken within that framework. I concur.

### 2.2 The "Washes Out" Phenomenon Deserves Closer Scrutiny

The minutes state that "spectral averaging over 741,648 TT modes washes out the tau-dependent curvature corrections." This is the central physical finding and it needs to be understood more precisely. The Lichnerowicz operator has three terms: rough Laplacian (-nabla^2), Riemann endomorphism (-2 R_{acbd}), and Ricci coupling (+2 Ric). The rough Laplacian scales like the scalar Laplacian (with the Casimir). The Riemann and Ricci terms are the tau-dependent corrections.

The question is quantitative: what fraction of the total TT eigenvalue is contributed by the curvature terms? The audit gives sector (0,0) eigenvalue = 1.0 at tau=0, and states the rough Laplacian contributes +1 to constant tensors. This means R_endo + Ric_endo contribute 0 at tau=0 in sector (0,0). For higher sectors, the rough Laplacian grows as C_2(p,q)/12 (from the audit), which means it dominates quadratically while curvature corrections grow at most linearly in C_2. As mps increases, the curvature correction becomes a smaller fraction of the total eigenvalue. This is exactly why the ratio converges: at high truncation, the rough Laplacian controls everything, and the rough Laplacian has the same tau-dependence as the scalar Laplacian.

This is the acoustic equivalent of the high-frequency limit. At frequencies much above the first bandgap, the dispersion relation is dominated by the lattice spacing (~ rough Laplacian) not by the impedance contrast (~ curvature coupling). Bandgap effects are strongest at LOW frequencies. The spectral sum, weighted by |lambda|^p, is dominated by HIGH eigenvalues (many modes there due to Weyl's law). So the curvature-sensitive low modes contribute negligibly to the sum.

This suggests a diagnostic: compute the contribution to E_total from ONLY the lowest 100-200 TT eigenvalues per tau. If the curvature corrections matter, the low-mode contribution should show different tau-dependence than the full sum. This is a zero-cost diagnostic from the existing `l20_TT_spectrum.npz` data.

### 2.3 The 68% Absolute Convergence Warning Is Significant for Other Purposes

The minutes note absolute E_TT differs by 68% between mps=5 and mps=6. The CLOSED verdict is ratio-robust, but the absolute values matter for anything beyond the F/B ratio. The Seeley-DeWitt coefficients a_0, a_2, a_4 from 20a also have convergence issues. This means the spectral sum approach is not reliable for predicting the actual numerical value of the cosmological constant -- only for its tau-dependence (which is the stabilization question). This distinction is important: even if a non-perturbative mechanism stabilizes the modulus, the perturbative computation will not reliably predict the V_eff value at the stabilized point.

---

## 3. Collaborative Suggestions

### 3.1 Low-Mode TT Casimir Diagnostic (Zero-Cost from Existing Data)

**What**: From `l20_TT_spectrum.npz`, extract the lowest N_cut TT eigenvalues at each tau and compute E_TT_low(tau) = Sum_{i=1}^{N_cut} sqrt(mu_i(tau)) for N_cut = 50, 100, 200.

**Why**: The spectral sum is dominated by high-lambda modes (Weyl's law), but the curvature corrections are concentrated in low-lambda modes. If E_TT_low(tau) has qualitatively different tau-dependence from E_TT_total(tau), the low-lying spectrum could in principle contribute to a stabilization mechanism that is invisible to the total sum. This tests whether the "washing out" is total or only applies to the integrated sum.

**Connection**: Paper 05 (Debye model): below the Debye temperature, low-frequency modes dominate thermodynamics. The analogous statement: below a "Debye wavenumber" in the spectral action, low-lying modes could dominate the physical potential. The spectral action cutoff function f(x) in Connes' formulation (Connes 07) IS a frequency-dependent weight. If f(x) is chosen to suppress high modes (as any physical cutoff must), the low-mode behavior becomes decisive. This is not tested in the current computation, which uses |lambda|^p with no UV suppression.

**Expected outcome**: Either (a) E_TT_low also has constant F/B ratio (confirming the CLOSED extends to any cutoff), or (b) E_TT_low has different tau-dependence (opening a window for physical cutoff functions that weight the low modes).

**Cost**: 30 minutes of script modification. Existing data.

### 3.2 Spectral Action with Physical Cutoff Function (1 day)

**What**: Replace the power-law spectral sum E = Sum |lambda|^p with E = Sum f(|lambda|^2/Lambda^2) where f(x) is a proper Schwinger heat-kernel cutoff: f(x) = x exp(-x). This is the Schwinger proper-time spectral action (Feynman Paper 11, the identification that Schwinger proper-time IS the spectral action).

**Why**: The constant-ratio result holds for power-law sums because Weyl's law ensures asymptotic universality. A non-polynomial cutoff function f(x) breaks the Weyl's law dominance. The function f(x) = x exp(-x) peaks at x = 1 and decays exponentially for x >> 1. This means the spectral action is dominated by eigenvalues near lambda ~ Lambda, not by the asymptotic tail. If the curvature corrections from the Lichnerowicz operator are significant near lambda ~ Lambda at some particular Lambda, the F/B ratio could depend on tau at that scale.

**Connection**: Paper 16 (Barcelo), eq 6: the cosmological constant rho_Lambda = Sum (1/2) hbar omega_i is precisely the linear Casimir sum when regularized by physical cutoff. Volovik (Paper 10) emphasizes that in the superfluid universe, the UV completion IS the lattice, and the cutoff IS physical. The spectral action with a genuine cutoff function is the correct object to evaluate, not the unregulated sum.

**Constraint Condition**: If the ratio R(tau, Lambda) is constant for ALL choices of Lambda, the CLOSED is confirmed at the cutoff-function level. If there exists a Lambda^* where R varies significantly with tau, that Lambda^* identifies the scale at which curvature corrections matter -- and a V_eff minimum could exist at that scale.

### 3.3 Acoustic Impedance Mismatch as F/B Ratio Breaking Mechanism

**What**: In phononic crystals (Paper 06, eq 5), the bandgap width scales with the impedance contrast Delta omega ~ |Z_1 - Z_2|/Z_bar. On the Jensen-deformed SU(3), the three subspaces u(1), su(2), C^2 have different effective impedances Z_k = sqrt(rho_k c_k^2) where rho_k is the effective density (metric determinant) and c_k is the effective speed of sound (inverse metric component). As tau varies, the impedance contrasts between subspaces change. At the "coincidence frequency" (the acoustic analog of Lichnerowicz-scalar crossing), the impedance mismatch vanishes for a particular subspace pair, and energy transfers resonantly between bosonic and fermionic sectors.

**Why this is NOT captured by block-diagonal computation**: The block-diagonal Peter-Weyl decomposition treats each (p,q) sector independently. But impedance matching is an INTER-sector phenomenon. Two adjacent sectors (p,q) and (p',q') can exchange energy at frequencies where their impedances match. This is the Bragg scattering mechanism (Paper 06, eq 1: lambda = 2d/n) applied to the KK tower. The F/B ratio constancy within each block does not prevent resonant coupling BETWEEN blocks from creating tau-dependent effects.

**Connection**: This is the minutes' route (b) -- "off-diagonal coupling between bosonic and fermionic sectors (Kosmann-Lichnerowicz coupling, not available from block-diagonal Peter-Weyl data)." I am translating the same physics into acoustic language, which suggests a specific computational diagnostic: compute the off-diagonal matrix elements <(p,q) boson | D_total | (p',q') fermion> and check if they are tau-dependent. If yes, the block-diagonal CLOSED does not survive full diagonalization.

### 3.4 Volovik Gap Equation Fixed-Point Analysis

**What**: The Volovik gap equation (Paper 10, eqs 4-5) defines the vacuum as the fixed point of a self-consistency map. In the superfluid, the gap Delta determines the excitation spectrum, the excitation spectrum determines the zero-point energy, the zero-point energy determines the equilibrium gap. Algebraically:

    Delta = G * Sum_k tanh(E_k/(2T)) / E_k

where E_k = sqrt(epsilon_k^2 + Delta^2) and G is the coupling constant.

On SU(3) with Jensen deformation, translate: Delta -> tau (deformation parameter), E_k -> lambda_k(tau) (eigenvalues), G -> coupling implicit in the Lichnerowicz operator. The self-consistency equation becomes:

    tau = F(tau) where F(tau) = argmin_tau' Sum_k |lambda_k(tau')| [with spectrum computed at tau]

This is a contraction mapping if |dF/dtau| < 1. The fixed point, if it exists, is the vacuum.

**Why this differs from V_eff minimum**: The V_eff minimum search asks dE/dtau = 0. The gap equation asks tau = F(tau). These are NOT the same. The gap equation is a functional equation, not a variational equation. In superfluid He-3B, the gap equation gives a non-trivial solution even when the free energy is monotonic in the gap, because the self-consistency constraint is more restrictive than stationarity.

**Connection**: This is my strongest disagreement with the minutes' interpretation. The CLOSED verdict applies to dE_total/dtau = 0. It does not necessarily apply to the gap equation tau = F(tau), because F(tau) involves the GEOMETRY (which eigenvalues exist) not just the ENERGY (which eigenvalues sum to). The geometry at tau' determines the spectrum that defines F. The energy at tau determines the gradient. These are different maps. I do not claim the gap equation gives a solution. I claim the CLOSED has not tested it.

**Cost**: 2 days of careful implementation. Requires defining F(tau) precisely for the KK context.

### 3.5 Instanton Action on Jensen-Deformed SU(3)

**What**: The instanton action on a compact manifold is S_inst = (1/4) Int F wedge F. On (SU(3), g_tau), the curvature 2-form has tau-dependent components. The instanton action S_inst(tau) is therefore a computable function of tau. Non-perturbative corrections to V_eff go as exp(-S_inst(tau)). If dS_inst/dtau < 0 (instanton action decreases with tau), the non-perturbative contribution INCREASES with tau, potentially balancing the monotonically increasing perturbative terms.

**Why**: The standard Poplawski mechanism (Paper 19, eq 3: the rho^2 correction that creates the bounce) is the same mathematics: a non-perturbative term that grows faster than the perturbative terms at high density/curvature, creating a turnaround. The instanton is the KK analog: a non-perturbative correction that could grow faster than the spectral sum at large tau, creating a V_eff minimum.

**Connection**: Paper 13 (Ashtekar LQC, eq 3): the modified Friedmann equation H^2 = (8piG/3)rho(1 - rho/rho_c) has the same structure -- perturbative (rho) plus non-perturbative (-rho^2/rho_c) with opposite signs. The bounce occurs where the two balance. On SU(3), the analogous equation would be V_total = V_perturbative(tau) + c * exp(-S_inst(tau)), and the minimum occurs where dV_perturbative/dtau = c * (dS_inst/dtau) * exp(-S_inst(tau)).

**Cost**: 1 day for the instanton action computation (the Riemann tensor is already computed in r20a_riemann_tensor.py). This is the single most tractable non-perturbative computation available.

---

## 4. Connections to Framework

### 4.1 The Resonance Hypothesis Survives in Modified Form

My framework hypothesis (`Primer-tesla-framework-hypothesis.md`) stated: "the stable configuration is the one where the zero-point energy is stationary: dE_total/dtau = 0. This is the resonance condition." Session 20b closes this specific implementation. The zero-point energy is NOT stationary at any tau.

But the resonance hypothesis itself is broader. A resonant system can be stabilized by:
1. Stationarity of the energy (V_eff minimum) -- CLOSED
2. Impedance matching between sectors (energy transfer equilibrium) -- UNTESTED (inter-sector coupling)
3. Self-consistency (gap equation fixed point) -- UNTESTED
4. Phase transition (topology change creating a new branch) -- UNTESTED (instantons, Pfaffian)
5. External driving (flux, boundary conditions) -- UNTESTED (Freund-Rubin)

Only route 1 has been tested and closed. The resonance hypothesis has four untested routes.

### 4.2 The Phonon-NCG Dictionary Gets a New Entry

Session 20b adds a precise entry to the phonon-NCG dictionary:

| NCG Concept | Phonon Analog | Session | Status |
|:------------|:-------------|:--------|:-------|
| Constant F/B ratio | Debye universality (heat capacity independent of lattice details at T >> Theta_D) | 20b | PROVEN |
| Spectral sum = fiber dimensions | Density of states = polarization count x Weyl's law | 20b | PROVEN |
| Block-diagonal Peter-Weyl | Independent oscillators (no inter-sector coupling) | 20b | ASSUMPTION (testable) |
| Curvature correction wash-out | High-frequency modes dominate; impedance mismatch negligible above bandgap | 20b | CONFIRMED |

The new entry: **the constant-ratio trap IS the Debye universality theorem for the internal manifold.** This is not a failure of the computation. It is a theorem about spectral sums on Riemannian manifolds with product structure. It tells us exactly where to look: either break the product structure (off-diagonal coupling) or exit the spectral sum framework entirely (non-perturbative).

### 4.3 The BLV Inside-Out View Reframes the CLOSED
From the Barcelo-Liberati-Visser perspective (Paper 16), the CLOSED says: the medium (SU(3) with Jensen deformation) has a frequency-independent refractive index ratio between bosonic and fermionic polarizations. In optics, a frequency-independent refractive index means no dispersion, no bandgaps, and no resonant phenomena. This is the mathematical content of "the ratio is geometric, not dynamical."

But real media are never dispersion-free. The block-diagonal approximation creates a dispersion-free effective medium because it treats each (p,q) sector as having a single effective refractive index proportional to C_2(p,q)^{1/2}. The ACTUAL medium (SU(3) with all inter-sector couplings) has dispersion, bandgaps, and resonances. The question is whether these inter-sector effects are large enough to create the vacuum.

---

## 5. Open Questions

**Q1**: Is the block-diagonal approximation the fundamental obstruction? The Peter-Weyl decomposition diagonalizes the Laplacian, not the Lichnerowicz operator. The Lichnerowicz R_endo term mixes different fiber components within each (p,q) sector, but does it also mix different (p,q) sectors? If R_endo has off-diagonal elements between (p,q) and (p+1,q), the block-diagonal spectral sum is missing inter-sector resonances. The Riemann tensor on Jensen-deformed SU(3) is NOT diagonal in the Peter-Weyl basis for TT tensors, even though the metric is. This needs to be checked explicitly. If off-diagonal elements exist, the constant-ratio CLOSED may not survive full diagonalization.

**Q2**: What does the Volovik gap equation give on (SU(3), g_tau)? The gap equation is a self-consistency condition, not a variational condition. The CLOSED applies to dE/dtau = 0. The gap equation asks a different question. Has anyone actually formulated the gap equation for the KK modulus? If not, this is the most important theoretical task for Session 21.

**Q3**: The instanton action S_inst(tau): does it decrease with tau? The Riemann tensor components from r20a_riemann_tensor.py grow exponentially with tau (e^{4tau} for some sectors). The instanton action involves Int |F|^2, which on a compact Lie group is related to the second Chern number c_2(SU(3)) = 1. The topological contribution is tau-independent (c_2 is an integer), but the metric-dependent norm |F|^2 is tau-dependent. If S_inst(tau) decreases, non-perturbative corrections grow, and a V_eff minimum becomes generically possible.

**Q4**: What happens at tau < 0? All computations sweep tau in [0, 2.0]. The Jensen deformation at negative tau reverses the direction of squashing (su(2) stretches, u(1) compresses). The Lichnerowicz eigenvalues at negative tau could have qualitatively different structure. If E_total(tau) has a minimum at tau < 0, the modulus is stabilized in the "anti-Jensen" direction. Physically, this corresponds to a different breaking pattern.

**Q5**: Does the spectral dimension d_s(tau) from Session 19a still show d_s > 8 at large tau? If so, the false vacuum picture survives: large tau is spectrally barren even though V_eff prefers it. The habitability boundary at tau ~ 0.96 (Session 19a) provides a physical selection mechanism independent of V_eff stationarity: the vacuum is not where the energy is lowest, but where the spectrum supports complexity. This is anthropic reasoning, but it is computationally testable.

---

## Closing Assessment

Session 20b is a clean, well-executed CLOSED on the strongest remaining perturbative stabilization route. The computation is correct. The code audit is thorough. The physical interpretation -- the constant-ratio trap is structural, set by fiber dimensions via Debye/Weyl universality -- is sound.

But I do not believe the CLOSED is as complete as the minutes suggest. The minutes state "all perturbative spectral mechanisms exhausted." What has actually been exhausted is: all spectral sums over block-diagonal Peter-Weyl eigenvalues. The inter-sector coupling (off-diagonal Kosmann-Lichnerowicz), the self-consistency condition (Volovik gap equation), the physical cutoff function (Schwinger proper-time), and the non-perturbative sector (instantons, flux) are all untested. Four routes remain. The constant-ratio trap is a theorem about uncoupled oscillators. The universe is coupled.

**Framework probability**: 40-48%. I am at the upper end of the minutes' 38-50% range. The structural results remain untouched. The stabilization problem has been promoted from "find a perturbative minimum" to "find a non-perturbative minimum" -- which is exactly where superfluid physics says it should live. In every superfluid I know (He-3B, He-4, BCS superconductors), the gap is stabilized by a non-perturbative mechanism (condensation, pairing), not by a perturbative spectral sum. The framework is following the physical pattern. Whether it arrives is the open question.

The twenty-seven drums are real. They play in tune. They just do not know when to stop.

---

**Files referenced**:
- Session minutes: `C:\sandbox\Ainulindale Exflation\sessions\session-20\session-20b-lichnerowicz.md`
- Framework hypothesis: `C:\sandbox\Ainulindale Exflation\sessions\Primer-tesla-framework-hypothesis.md`
- Lichnerowicz script: `C:\sandbox\Ainulindale Exflation\tier0-computation\l20_lichnerowicz.py`
- TT spectrum data: `C:\sandbox\Ainulindale Exflation\tier0-computation\l20_TT_spectrum.npz`
- V_total data: `C:\sandbox\Ainulindale Exflation\tier0-computation\l20_vtotal_minimum.npz`
- Tesla papers index: `C:\sandbox\Ainulindale Exflation\researchers\Tesla-Resonance\index.md`

**Papers cited**: Tesla-Resonance 05 (Debye), 06 (Phononic crystals), 07 (Chladni/Weyl's law), 10 (Volovik), 11 (Unruh), 13 (Ashtekar LQC), 16 (Barcelo BLV), 19 (Poplawski torsion)
