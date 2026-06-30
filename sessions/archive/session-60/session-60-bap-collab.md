# Baptista Spacetime Analyst -- Collaborative Feedback on Session 60

**Author**: Baptista Spacetime Analyst
**Date**: 2026-03-27
**Re**: Session 60 Results (29 computations, 20 FAIL / 4 PASS / 5 INFO)

---

## 1. Key Observations from the KK Geometry Perspective

I ran 8 of the 27 completed computations: A4-TRACE-60, UNIMOD-GRAV-60, PW-H0-CONV-60, HESSIAN-3D-60, SECTOR-DIM-REDUCT-60, LICHNEROWICZ-DW-60, COMPOUND-MECH-60, and Q-THEORY-GEODESIC-60. Five returned FAIL, two INFO, one FAIL-by-construction (compound of two FAILs). Every one of these results traces directly to the Riemannian geometry of SU(3) with left-invariant metrics as developed in Papers 13-15, and I want to lay out the geometric skeleton beneath the numerical verdicts.

### 1.1 The Riemannian Submersion Factorization Is Load-Bearing

UNIMOD-GRAV-60 was closed by the volume element factorization theorem for Riemannian submersions: $\mathrm{vol}(g_P) = \mathrm{vol}(g_K) \wedge \mathrm{vol}(g_4)$. This is not a numerical observation but a theorem of differential geometry (O'Neill 1966). The Jensen deformation preserves $\mathrm{Vol}(K)$ to machine epsilon ($4.4 \times 10^{-16}$ across 10,000 samples), which stabilizes $G_4 = G_{12}/V_K$ exactly. But it cannot propagate to $\det(g_4)$ because fiber and base are geometrically independent objects in the submersion structure. Five independent arguments (factorization, constraint on different objects, O'Neill tensor analysis, Einstein frame triviality, 12D unimodular requirement) converge on this closure.

The positive structural legacy is substantial. The Jensen line projects out the breathing mode exactly ($\phi < 4.2 \times 10^{-16}$), eliminates the moduli problem, and gives $dG/dt = 0$ identically. These are non-trivial consequences of Baptista's choice of deformation (Paper 13, eq 2.37) that distinguish SU(3) with Jensen metrics from generic KK compactifications. The framework has NO light moduli from the volume sector -- a feature that most string/KK constructions struggle to achieve.

### 1.2 The Peter-Weyl Spectral Sum Is Not the Heat Kernel Coefficient

PW-H0-CONV-60 is the most consequential computation of the session. The quantity previously called "$a_2$" -- the Peter-Weyl spectral sum $\sum_{(p,q)} \dim(p,q)^2 \sum_i |\lambda_i^{(p,q)}|$ -- is $\mathrm{Tr}(|D_K|)$, the trace of the absolute value of the Dirac operator on deformed SU(3). This quantity diverges as $L^{6.2}$ with the PW truncation level $L = \max(p+q)$.

The divergence is structural. Weyl's law for a Dirac operator on a compact $d$-manifold gives $|\lambda_n| \sim n^{1/d}$, and the PW multiplicities grow as $\dim(p,q)^2 \sim (p+q)^4$. The total sum $\sum |\lambda| \sim \sum_{L=0}^{\infty} L^4 \cdot L^{8/d}$ diverges for $d = 8$. The true Seeley-DeWitt coefficient $a_2(D_K^2)$ is a different mathematical object: it is a finite local curvature integral,

$$a_2(D_K^2) = \frac{1}{(4\pi)^{d/2}} \int_K \mathrm{tr}\left(\frac{R}{6} \cdot \mathbf{1} + E\right) \, \mathrm{dvol}_K$$

where $R$ is the scalar curvature of the Jensen metric and $E$ is the endomorphism from the Lichnerowicz-Schr\"odinger decomposition $D_K^2 = -\nabla^2 + E$ (Paper 19, eq 2.14-2.16; Gilkey 1975). This integral is finite on any compact Riemannian manifold -- no PW truncation is needed.

The S44 data bug (missing the $(1,2)$ irrep, originating in S27) is a secondary issue. Even with the complete $L \leq 3$ data, $N(L=3) = 4.859$, not 3.920. But the fundamental problem is not the bug -- it is the identification of a divergent spectral trace with a finite geometric integral. The corrected $N(L=4) = 13.4$, $N(L=7) = 121$ establishes that no convergence was ever occurring.

### 1.3 The Hessian Regime Dependence Reveals Two Spectral Actions

HESSIAN-3D-60 computed the full 3D Hessian of the spectral action from actual Dirac eigenvalues (12,880 per grid point, 125 grid points). The key structural finding: $H_{a_2}$ and $H_{a_4}$ have opposite definite signatures.

- $H_{a_2}$: all eigenvalues negative. The fold maximizes the curvature integral $\int R \, \mathrm{dvol}$.
- $H_{a_4}$: all eigenvalues positive. The fold minimizes the Gauss-Bonnet integral.

The spectral action $S = \alpha \cdot a_2 + a_4$ (with $\alpha = f_2 \Lambda^2 / f_0$) undergoes a sharp signature transition at $\alpha_{\mathrm{crit}} \approx 55$. Below this threshold, the fold is a local minimum (topological regime). Above it, the fold is a local maximum (mode-counting regime). The physical heat kernel ($f(x) = e^{-x}$) gives effective $\alpha \gg 55$, placing the framework squarely in the mode-counting regime where the fold is unstable.

This corrects two prior results:
- S58's $(1+, 1-)$ signature was from a curvature-volume proxy, not the actual spectral action.
- S59's $\cos(\vec{v}_{SA,\mathrm{neg}}, \vec{v}_{EJ,\mathrm{neg}}) = 0.114$ was an artifact of comparing the proxy's eigenvectors against the E_J Hessian. The true alignment is $\cos = 0.991$ -- SA and E_J have nearly parallel unstable directions in the heat-kernel regime.

### 1.4 The Screening Ratio Is a Fold Constant

SECTOR-DIM-REDUCT-60 tested whether the Riemannian submersion structure provides screening between $\delta G/G$ and $\delta\alpha/\alpha$. It does not. Both quantities track the same one-parameter Jensen deformation $\tau$. The screening ratio

$$R_{\mathrm{screen}} = \frac{|\delta N/N|}{|\delta\alpha/\alpha|} = \frac{1}{2}\frac{|\mathrm{frac}_{da_2}|}{|\mathrm{clock}_{\mathrm{coeff}}|} = \frac{1}{2}\frac{99.13}{3.08} = 16.1$$

is independent of $\delta\tau$ because $\delta\tau$ cancels in the ratio. This is a fold constant, not a fine-tuning issue. The consequence is immediate: the timescape mechanism and ALPHA-ENV-43 are structurally incompatible on the Jensen line. Achieving $\delta\alpha/\alpha < 10^{-6}$ requires $\delta\tau < 3.25 \times 10^{-7}$, giving $\delta N/N = 1.6 \times 10^{-5}$ -- five orders below the $\sim 0.08$ needed for $w_a$ from DESI.

### 1.5 The Lichnerowicz Spectrum Knows About the Domain Wall

LICHNEROWICZ-DW-60 tracked all 31 TT eigenvalues through the domain wall at $\tau_{DW} = 0.1135$ on a fine grid (41 points, $\Delta\tau = 0.001$). The global minimum $\lambda_{\min} = +0.3150$ occurs at $\tau = 0.116$, just 0.0025 from $\tau_{DW}$. The minimum is in the HARD(su2) sector (degeneracy 5) -- the Jensen deformation modes themselves. The gap does not close. This extends the stability result of Papers 28-29 (Lauret-Will) through the domain wall region: the SU(3) fiber remains Lichnerowicz-stable against G-invariant TT perturbations at all $\tau$.

### 1.6 The Topological Layer of q-Theory Survives

Q-THEORY-GEODESIC-60 separated the topological and dynamical claims about Cooper pair charge. The topological layer is permanent: each Cooper pair carries $K_7$ charge $q_7 = \pm 1/2$, which IS a weight-lattice winding number. Total winding $Q = \pm 29.9$ for 59.8 pairs. This is representation theory, independent of dynamics. The dynamical layer (Paper 16, eq 1.2 geodesic mass variation) fails quantitatively: 44x energy mismatch, transit covers 0.06% of one $K_7$ circumference. The many-body pair counting and single-particle geodesics operate at fundamentally different scales.

---

## 2. Assessment of Critical Results

### 2.1 The PW Divergence and Missing (1,2) Irrep

The S44 data bug is a cautionary tale about sector counting. The 10 irreps at $L \leq 3$ are: $(0,0), (1,0), (0,1), (1,1), (2,0), (0,2), (3,0), (0,3), (2,1), (1,2)$. The S27 sector list omitted $(1,2)$ -- the conjugate of $(2,1)$. The missing contribution is $a_2 = 87{,}376$, which is 54% of the incomplete total. Every computation that used the S44 eigenvalue data for full PW sums requires audit.

The singlet-sector results are unaffected. $(0,0)$ quantities -- BCS condensation energy, gap function, Leggett mode, pair transfer, Richardson-Gaudin integrals -- are safe. The contamination affects only total PW spectral sums: $\mathrm{Tr}(|D_K|)$, $\mathrm{Tr}(D_K^2)$, and ratios thereof.

The deeper issue transcends the bug. Even with complete data, the truncated PW trace diverges. The framework has been computing the wrong mathematical object for the gravitational sector. The correct object is the local heat kernel coefficient, which involves the Ricci scalar of the Jensen metric (known analytically from Paper 13, eq 2.40 and Paper 15, eq 3.70) integrated over the volume form. This is a finite, well-defined geometric integral.

### 2.2 The $a_2$ vs $\mathrm{Tr}(|D_K|)$ Distinction

Let me be precise about the mathematical distinction, because the notation has been a source of confusion across sessions.

**What we have been computing**: $\tilde{a}_2 \equiv \sum_{(p,q)} \dim(p,q)^2 \sum_i |\lambda_i^{(p,q)}|$. This is $\mathrm{Tr}(|D_K|)$ in the PW basis. It diverges as $L^{6.2}$.

**What the spectral action needs** (Paper 19, eq 2.14-2.16): The Seeley-DeWitt coefficient $a_2(D_K^2)$, defined through the asymptotic expansion of the heat trace:

$$\mathrm{Tr}(e^{-t D_K^2}) \sim \sum_{n \geq 0} t^{(n-d)/2} \, a_n(D_K^2) \quad \text{as } t \to 0^+$$

For $n = 2$ on a $d = 8$ manifold, $a_2$ is the coefficient of $t^{-3}$ in the heat trace expansion. It is given by Gilkey's formula:

$$a_2 = \frac{1}{(4\pi)^4} \int_{K} \left[\frac{R}{6}\,\mathrm{tr}(\mathbf{1}) + \mathrm{tr}(E)\right] \mathrm{dvol}_K$$

where $E$ is the endomorphism in the Lichnerowicz decomposition $D_K^2 = -\Delta + E$, and the trace is over the spinor bundle. On SU(3), $\mathrm{tr}(\mathbf{1}) = 16$ (spinor dimension), $R$ is the scalar curvature of the Jensen metric, and $E$ involves the Ricci curvature through the Lichnerowicz-Weitzenb\"ock formula.

These are two completely different mathematical objects. The first diverges; the second is finite and computable from the local curvature. The confusion arose because for a FINITE-dimensional spectral triple (as in standard NCG), both reduce to finite sums and are related by moments of the spectral measure. On a manifold, the spectral sum requires regularization (zeta function or heat kernel) to produce finite answers.

### 2.3 The Trace Factor Non-Cancellation

A4-TRACE-60 established that $N_{a_4}/N_{a_2} = 1.823$ -- an 82% deviation from unity that is nearly $\tau$-independent (spread $< 0.5\%$). The monotonic hierarchy $N_{a_0} < N_{a_2} < N_{a_4} < N_{a_6}$ arises because higher Casimir representations have larger Dirac eigenvalues, and higher spectral moments amplify larger eigenvalues more.

This means the Chamseddine-Connes Higgs mass formula, which uses $a_4/a_2$ from the full trace, cannot simply divide out $\dim(\Delta_8) = 16$. Gravity (which uses $a_2$ alone) and Higgs physics (which uses $a_4/a_2$) require different treatment of PW sector multiplicities. The 35% Higgs mass shift $\sqrt{1.823} = 1.35$ between total and singlet conventions is a new systematic.

However, this result inherits the same caveat as PW-H0-CONV-60: the ratio $a_4/a_2$ as computed from truncated PW spectral sums may differ from the ratio of true Seeley-DeWitt coefficients. The proper heat kernel computation would resolve both issues simultaneously.

### 2.4 The Hessian Regime Dependence

The transition at $\alpha_{\mathrm{crit}} = 55$ is a concrete numerical target. If the physical cutoff satisfies $f_2 \Lambda^2 / f_0 < 55$, the fold IS a local minimum. The $a_4$ (Gauss-Bonnet) regime is the topological regime of the spectral action where it functions as an index rather than an action counting modes. Whether nature selects this regime is not determined by the internal geometry alone -- it depends on the UV completion.

---

## 3. Collaborative Suggestions

### 3.1 Heat Kernel $a_2$ from Local Curvature (HIGHEST PRIORITY)

The proper Seeley-DeWitt $a_2$ on the Jensen metric is a finite computation. From Paper 13, eq 2.40 (or equivalently Paper 15, eq 3.70 for the general three-parameter case), the scalar curvature of the Jensen metric is known analytically:

$$R(\tau) = \frac{3(4 - 25||\phi||^2 + 33||\phi||^4 - 8||\phi||^6)}{\lambda(1-||\phi||^2)^2(1-4||\phi||^2)}$$

where the substitution $||\phi||^2 = 1 - e^{-2\tau}$ converts to the Jensen parameter. For the Gilkey formula, we also need the endomorphism $E$ from $D_K^2 = -\Delta + E$. On a group manifold with left-invariant metric, $E$ can be computed explicitly from the Ricci tensor and the spinor connection (Lichnerowicz formula: $E = R/4$ for the standard Dirac operator, where $R$ is the scalar curvature). The integral over SU(3) with the Jensen volume form gives a finite number.

This computation requires no PW truncation, no eigenvalue data, and no numerical diagonalization. It is a closed-form calculation from the geometry of Papers 13-15.

### 3.2 Off-Jensen Multi-Parameter Deformation

SECTOR-DIM-REDUCT-60 identified the only escape route for the timescape mechanism: a multi-parameter deformation where $\lambda_1, \lambda_2, \lambda_3$ evolve independently. Paper 13, eq 2.37 already provides the general three-parameter metric on SU(3) with left-invariant metrics. Paper 15, eq 3.70 gives the scalar curvature in this general setting. The Jensen line is the one-parameter subfamily $\lambda_1 = e^{2\tau}, \lambda_2 = e^{-2\tau}, \lambda_3 = e^{\tau}$ (volume-preserving). Off-Jensen directions would allow $G$ and $\alpha$ to decouple.

The full moduli space is 5-dimensional (breaking U(2) to the identity), but the 3D volume-preserving subspace ($\lambda_1 \lambda_2^3 \lambda_3^4 = 1$) is the physically relevant restriction. Computing the screening ratio $R_{\mathrm{screen}}$ as a function on this 2D surface (parameterized by, say, $\sigma$ and $\delta_1$) would determine whether any direction exists with $R_{\mathrm{screen}} > 10^4$.

### 3.3 Zeta-Function Regularization

As an independent check on the heat kernel computation, the spectral zeta function $\zeta_{D_K^2}(s) = \sum_n \lambda_n^{-2s}$ is well-defined for $\mathrm{Re}(s) > d/2 = 4$ and has meromorphic continuation. The $a_2$ coefficient is related to the residue at $s = 3$: $a_2 = (4\pi)^4 \cdot \mathrm{Res}_{s=3} \zeta_{D_K^2}(s)$. With 48 irreps computed (L=0 through L=7), the convergence of $\zeta_{D_K^2}(s)$ for $s > 4$ could be tested directly, and the analytic continuation to $s = 3$ attempted via Richardson extrapolation or Shanks transformation. The PW spectral sum $\mathrm{Tr}(D_K^{-2s})$ converges rapidly for $s > 4$ because the summand decays as $L^{8-2 \cdot 2s}$, which is negative for $s > 4$.

### 3.4 Domain Wall Connection to Ricci Anisotropy

The near-coincidence of $\lambda_{\min}^{Lich}$ with $\tau_{DW}$ (within 0.0025) deserves further investigation. From S59 RICCI-DW-59, the domain wall $\tau_{DW} = 0.1135$ coincides with the transition $K_{\mathrm{sec}}^{\min} = 0$ to machine precision. Paper 28 (Lauret) proves that ALL Jensen Einstein metrics on compact Lie groups are G-unstable in the Lichnerowicz sense. The fact that the Lichnerowicz gap reaches its minimum near the sectional curvature sign change suggests a geometric mechanism: the onset of negative sectional curvature weakens the TT stability margin, even though it does not reach zero.

---

## 4. Connections to the Baptista Framework

### 4.1 Riemannian Submersion Structure

Papers 13-15 develop the KK reduction of $M^4 \times K$ as a Riemannian submersion. The O'Neill tensors $A$ (integrability obstruction) and $T$ (mean curvature) encode the coupling between base and fiber. S60 tested three consequences of this structure:

1. **Volume factorization** (UNIMOD-GRAV-60): The fiber volume $V_K$ enters the 4D action as a multiplicative constant in $G_4 = G_{12}/V_K$. Jensen volume-preservation gives $dG/dt = 0$ exactly -- a structural stability result stronger than what most KK models achieve. But it does not constrain $\det(g_4)$.

2. **Curvature coupling** (SECTOR-DIM-REDUCT-60): The O'Neill $A$-tensor provides curvature coupling between base and fiber (Paper 15, eq 1.5: $R_P = R_M + R_K - |F|^2 - |\mathring{S}|^2 - |N|^2 - 2\check{\delta}N$). Both $G$ and $\alpha$ trace back to the same fiber metric $g_\phi(\tau)$, so the $A$-tensor cannot provide independent screening.

3. **Product topology** (from S54 GEODESIC-DEVIATION-54): On a product $M^4 \times K$ with no gauge fields, $A = 0$ identically (integrable horizontal distribution). The $A$-tensor becomes nonzero only when gauge fields are activated or when the bundle is nontrivial. The internal coset $A$-tensor (S55 ATENSOR-GAUGE-55, $|A|^2 = 3/2 + 3/2 \, e^{-4\tau}$) is always nonzero but acts within the fiber, not between fiber and base.

### 4.2 Spectral Action on SU(3)

Paper 19 (Chamseddine-Connes 1996) provides the heat kernel expansion framework; Papers 13-14 provide the geometric input (metric, Dirac operator, curvature). The S60 results establish three structural facts about this combination:

1. The raw PW spectral sum $\mathrm{Tr}(|D_K|^n)$ is NOT the Seeley-DeWitt coefficient $a_n$. The former diverges; the latter is a finite curvature integral. This distinction was invisible at $L \leq 3$ (where truncation effects were mistaken for convergence).

2. The spectral action has two distinct regimes separated by $\alpha_{\mathrm{crit}} = 55$. The mode-counting regime ($\alpha > 55$) has the fold as a maximum. The topological regime ($\alpha < 55$) has the fold as a minimum. Paper 33's factorization $a_4^{M \times K} = a_4^M \cdot a_0^K + a_2^M \cdot a_2^K + a_0^M \cdot a_4^K$ (from the product formula for heat kernels) shows that the $a_4$ contribution to the 4D action involves the internal $a_0^K$ (mode count) and $a_2^K$ (curvature), and these enter with different signs in the Hessian.

3. The trace factor non-cancellation ($N_{a_4}/N_{a_2} = 1.823$) means the spectral action on $M^4 \times K$ cannot be treated as a single effective action with uniform spinor normalization. The sector decomposition must be carried through to the particle physics predictions. This is a consequence of the SU(3) representation theory: Casimir growth causes higher PW sectors to contribute more to higher spectral moments.

### 4.3 Fiber Integration and the q-Theory Connection

Paper 14, Section V introduces the q-theory interpretation: the cosmological constant is controlled by the equilibrium value of a conserved charge $q$, with $\Lambda = \epsilon(q_0)$ where $q_0$ is selected by $d\epsilon/dq = 0$. S60 confirms that Cooper pair charge $q_7$ IS a weight-lattice topological quantum number (Q-THEORY-GEODESIC-60, topological layer). The block-diagonal theorem (S22b, confirmed by INTER-SECTOR-ZUBAREV-60) ensures each PW sector has its own independent q-theory equilibrium with $\Lambda_{\mathrm{eq}} = 0$. The CC problem reduces to: why is the physical vacuum at $\Lambda = \Lambda_{\mathrm{obs}}$ rather than $\Lambda = 0$?

---

## 5. Open Questions

**Q1. What is the true $a_2(D_K^2)$ on the Jensen metric?** This is computable from Gilkey's formula using the known scalar curvature (Paper 13, eq 2.40) and the Lichnerowicz endomorphism. The integral over SU(3) with Jensen volume form requires no PW truncation. If $a_2(D_K^2)/(16 \cdot (4\pi)^4 \cdot V_K)$ yields $M_{\mathrm{Pl}}^2/(2 M_{\mathrm{KK}}^2)$ at $\tau = 0.19$, the H_0 prediction is recoverable. If not, the framework's gravitational coupling is a free parameter.

**Q2. Does the topological regime ($\alpha < 55$) have a physical interpretation?** In this regime the fold IS a minimum, stabilized by the $a_4$ (Gauss-Bonnet) contribution. This is the regime where the spectral action counts topology rather than modes. Is there a UV completion of the framework where $f_2 \Lambda^2 / f_0 < 55$ is natural? Paper 21 (entropy-spectral action duality) connects $f$ to the Riemann zeta function; does that particular test function sit in the topological regime?

**Q3. Can multi-parameter deformation decouple $G$ and $\alpha$?** The Jensen line is volume-preserving and one-parameter, so $G$ and $\alpha$ are locked. Paper 13's general three-parameter metric ($\lambda_1, \lambda_2, \lambda_3$) has two additional volume-preserving directions. Computing the screening ratio $R_{\mathrm{screen}}(\sigma, \delta_1)$ on this 2D surface would determine whether timescape remains viable. Preliminary data from HESSIAN-3D-60 (which computed in this 3D space) could be repurposed.

**Q4. Does the Lichnerowicz minimum near $\tau_{DW}$ have a geometric explanation?** The near-coincidence (0.0025) of the TT spectral gap minimum with the domain wall is suggestive. Paper 28 proves G-instability for Einstein metrics; the Jensen deformation breaks Einstein but the instability mechanism (related to $K_{\mathrm{sec}}^{\min} = 0$) persists in attenuated form. Is there a general theorem relating Lichnerowicz spectral gaps to sectional curvature sign transitions?

**Q5. What is the physical meaning of the $a_4$ regime transition at $\alpha_{\mathrm{crit}} = 55$?** The transition from mode-counting (fold = maximum) to topological (fold = minimum) spectral action is a sharp phenomenon. Does it correspond to a known physical transition in NCG? Paper 23 (spectral Pati-Salam) uses the spectral action at the GUT scale, where $\Lambda$ is large -- is this in the mode-counting or topological regime?

---

## Closing Assessment

S60 is a session of structural clarifications, not framework-ending failures. The most important result is recognizing that the truncated PW spectral sum is not the Seeley-DeWitt heat kernel coefficient. This distinction should have been caught earlier -- the divergence of $\mathrm{Tr}(|D_K|)$ is a textbook result for Dirac operators on compact manifolds. The S27-S44-S59 chain of artifacts propagated through 33 sessions because the convergence at $L = 3$ was mistaken for a genuine limit, when it was a coincidence of the truncation level.

The retraction of $H_0 = 68.8$ km/s/Mpc is painful but honest. The framework's gravitational coupling must come from the proper heat kernel computation, which involves the analytically known scalar curvature of the Jensen metric (Paper 13, eq 2.40) integrated over SU(3). This computation has not been attempted. Until it is completed, the framework's $H_0$ prediction is undefined, not wrong.

The structural results from the Riemannian submersion analysis (UNIMOD-GRAV-60, SECTOR-DIM-REDUCT-60), the Lichnerowicz tracking (LICHNEROWICZ-DW-60), and the topological pair charge (Q-THEORY-GEODESIC-60) are permanent additions to the constraint map. The geometry of SU(3) with Jensen metrics continues to be remarkably rich -- the near-coincidence of the Lichnerowicz minimum with the domain wall, the regime transition in the spectral action Hessian, the exact cancellation of the breathing mode -- but these geometric features constrain rather than solve the CC problem. The walls of the solution space are now more precisely mapped, and the remaining open region is the proper heat kernel computation plus the multi-parameter deformation that could decouple $G$ from $\alpha$.

The immediate priority from the KK geometry perspective is HEAT-KERNEL-A2-61: compute $a_2(D_K^2)$ from Gilkey's local formula using the known curvature of Papers 13-15. This is the only path to a defensible $H_0$ prediction.
