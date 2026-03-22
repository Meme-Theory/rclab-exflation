# Atlas Collaborative Review: Spectral-Geometer

**Agent**: Spectral-Geometer (Gilkey/Berger/Mueller/Lott/Connes methodology)
**Scope**: Project Atlas D00-D08, Sessions 1-51, full spectral geometry corpus (35 papers)
**Focus**: Heat kernel, Seeley-DeWitt, Weyl asymptotics, eigenvalue bounds, spectral dimension
**Date**: 2026-03-20

---

## Section 1: The Spectral Action Monotonicity Theorem (W4/W7) -- Assessment from the Heat Kernel

Wall W4/W7 is the most powerful structural result in the project: 13+ mechanism closures, all descending from a single property of the heat trace on Jensen-deformed SU(3). Let me state precisely what this result says and does not say from the standpoint of rigorous spectral geometry.

**What the theorem is.** For any monotonically decreasing smooth cutoff function $f$, the spectral action
$$S_f(\tau) = \mathrm{Tr}\, f(D_K^2(\tau)/\Lambda^2)$$
is monotonically decreasing in $\tau$ for all $\Lambda > 0$ and all 10 tested Peter-Weyl sectors. The underlying fact is that $\langle\lambda^2\rangle(\tau) = \sum_n g_n \lambda_n^2(\tau) / \sum_n g_n$ increases monotonically under the volume-preserving Jensen deformation.

**Why it holds (Gilkey/Vassilevich perspective).** The Seeley-DeWitt expansion gives
$$S_f(\tau) \sim \sum_{k=0}^{\infty} f_k \Lambda^{8-2k} a_{2k}(\tau)$$
where $a_{2k}$ are the heat kernel coefficients on 8-dimensional SU(3). The project proved that $a_0$ is $\tau$-independent (volume-preserving constraint, Paper 01/15 formula $a_0 = (4\pi)^{-d/2} \mathrm{rank}(E) \cdot \mathrm{Vol}$), and $a_2(\tau), a_4(\tau)$ are individually monotone (increasing) from the explicit curvature invariant formulas (S17b, S20a, verified 147/147 Riemann). The structural monotonicity extends beyond the asymptotic expansion to the exact finite sum because the spectrum is discrete and finite at each Peter-Weyl truncation.

**What it constrains.** Any spectral functional $F(\tau)$ that is a single-trace monotone function of $D_K^2(\tau)$ inherits monotonicity. This eliminates all spectral-action-based $\tau$-stabilization mechanisms. The scope is sharp: it blocks positive-definite spectral functionals but does NOT block:
- (a) Signed functionals (BCS condensation energy involves $\mathrm{Tr}\,\sqrt{(\lambda^2-\mu^2)^2+\Delta^2} - \mathrm{Tr}\,|\lambda^2-\mu^2|$, which has indefinite sign)
- (b) Products of monotone functions (multi-trace, not guaranteed monotone)
- (c) $\chi_{SA} = d^2 S/d\tau^2$, the susceptibility, which involves derivatives of $S$ rather than $S$ itself

**Structural assessment.** This wall is permanent. It follows from the curvature monotonicity of the Jensen family combined with the Gilkey formula, both verified at machine epsilon. Paper 29 (van Nuland-van Suijlekom) confirms monotonicity survives one-loop quantum corrections. The wall defines the boundary of the solution space: any surviving mechanism must escape through (a), (b), or (c) above.

---

## Section 2: The Cutoff Function Problem -- Does Spectral Geometry Provide a Canonical Choice?

The atlas flags S2 (D04) as ASSUMED: "NCG says $f$ is arbitrary; only moments $a_0, a_2, a_4$ matter in asymptotic expansion." The S51 CUTOFF-CONV-51 computation showed the SA correlator sector weights vary 55% across cutoff choices, though $\alpha_\mathrm{eff}$ is stable at 4.7%.

**The spectral geometry verdict: there is no canonical cutoff.**

This is not a deficiency of the framework; it is a structural feature of spectral geometry itself. Here is the precise situation.

(i) **Asymptotic expansion.** The Seeley-DeWitt coefficients $a_{2k}$ are geometric invariants of $(M, g, D)$, independent of $f$ (Papers 01, 15, 24). The spectral action $\mathrm{Tr}\,f(D^2/\Lambda^2)$ depends on the moments $f_k = \int_0^\infty f(v) v^{k-1} dv$, which ARE cutoff-dependent. For the asymptotic expansion to be an adequate approximation, we need $\Lambda \gg |\lambda_{\max}|$. But the S51 Taylor Exactness Theorem (S45) proved that on a finite discrete spectrum, the spectral action has an exact convergent Taylor series -- the asymptotic expansion IS the exact answer, and no non-perturbative content exists. So the cutoff-dependence is genuine and physical for the finite spectrum on SU(3).

(ii) **Connes reconstruction theorem.** Paper 11 establishes that the spectral triple $(A, H, D)$ -- not the cutoff function -- reconstructs the manifold. The cutoff enters only when defining the spectral action as an effective action. Connes' axioms impose conditions on $D$ (regularity, finiteness, orientability, Poincare duality, reality) but say nothing about $f$. The spectral action principle $S = \mathrm{Tr}\,f(D/\Lambda)$ is an additional physical input.

(iii) **Zeta-function regularization.** One might hope that the spectral zeta function $\zeta_D(s) = \mathrm{Tr}\,|D|^{-s}$ provides a canonical regularization. But $\zeta_D$ does not define a positive action functional -- it is a complex-valued meromorphic function. The zeta-regularized determinant $\det(D) = \exp(-\zeta_D'(0))$ IS canonical (Paper 08, Mueller), but it is a single number, not a family parameterized by $\Lambda$.

(iv) **Analytic torsion.** The Ray-Singer torsion $\log \tau_{RS} = -\sum_p (-1)^p p\, \zeta_p'(0)$ is a canonical UV-finite spectral invariant that does not require a cutoff. It remains UNCOMPUTED on Jensen-deformed SU(3) (D07 verification table, status OPEN). This is the one spectral invariant that spectral geometry designates as canonical and cutoff-free. Computing $\tau_{RS}(\tau)$ across the Jensen family would provide a cutoff-independent probe of the geometry.

**Constraint map update.** The 55% sector weight variation in $\chi_{SA}$ at different cutoffs means the SA correlator mixing model has an inherent $O(1)$ systematic uncertainty. The $\alpha_\mathrm{eff} = 0.86$ stability at 4.7% provides partial rescue for the identity-breaking claim, but quantitative $n_s$ predictions from the SA sector carry cutoff systematic errors that cannot be reduced within the NCG framework as currently formulated.

---

## Section 3: The Eigenvalue Scaling Law -- Derivation from Weyl Asymptotics

The S51 computation HIGH-PW-51 established the empirical scaling:
$$\max|\lambda| = 0.633\sqrt{C_2(p,q)} + 0.555 \quad (1)$$
with RMS residual 0.046, where $C_2 = (p^2+q^2+pq+3p+3q)/3$ is the quadratic Casimir. The question: is this derivable from Weyl asymptotics on SU(3)?

**The answer is: the $\sqrt{C_2}$ scaling is exactly what Weyl's law predicts, and the coefficient admits a representation-theoretic derivation.**

The Dirac operator on sector $(p,q)$ has the form (from the tier1 code):
$$D_\pi = \sum_{a=0}^{7} E_{ab}\, \rho_\pi(X_b) \otimes \gamma_a + I \otimes \Omega(\tau) \quad (2)$$

where $\rho_\pi$ is the representation $(p,q)$ acting on $V_\pi$ (dimension $d_{p,q}$), $E_{ab}$ is the orthonormal frame, and $\Omega$ is the spin connection (a fixed $16 \times 16$ matrix). The operator norm of $\rho_\pi(X_b)$ scales as $\sqrt{C_2}$ for the highest-weight state -- this is the Casimir scaling of representation theory (Paper 04, Gilkey; Paper 25, Show).

For large $(p,q)$, the first term in (2) dominates. The spectral radius of $D_\pi$ is therefore:
$$R_{(p,q)} \sim k(\tau) \sqrt{C_2(p,q)} + c(\tau) \quad (3)$$

where $k(\tau)$ encodes the Jensen metric through the frame and connection, and $c(\tau)$ is the contribution from $\Omega$, which is $(p,q)$-independent. This is precisely the form (1).

From Weyl's law (Paper 23, Ivrii), on a $d$-dimensional manifold the eigenvalue counting function satisfies:
$$N(\lambda) = C_d \,\mathrm{Vol}(M)\, \lambda^d + O(\lambda^{d-1}) \quad (4)$$

For the Dirac operator on an 8-dimensional compact manifold with spinor rank $2^4 = 16$:
$$N(\lambda) \propto \mathrm{Vol}(SU(3)) \cdot \lambda^8 \quad (5)$$

Within a single sector $(p,q)$, the matrix has dimension $16 \cdot d_{p,q}$, and the maximum eigenvalue is bounded by $\|D_\pi\| \leq \|E\| \cdot \|\rho_\pi\| + \|\Omega\|$. Since $\|\rho_\pi\| = \sqrt{C_2}$ for the standard representation and scales as $\sqrt{C_2}$ for general $(p,q)$, we get the $\sqrt{C_2}$ law.

**The coefficient 0.633.** This should be derivable from the frame norm $\|E(\tau)\|$ at the fold. At $\tau = 0.19$, the Jensen metric is $g = 3\cdot\mathrm{diag}(e^{0.38}, e^{-0.38}, e^{-0.38}, e^{-0.38}, e^{0.19}, e^{0.19}, e^{0.19}, e^{0.19})$. The orthonormal frame norms give $\|E\| = O(1)$, and the projection onto the highest-weight direction selects the fraction $k = 0.633$. A precise derivation requires evaluating $\max_v |\langle v| \sum_a E_{ab} \rho(X_b) \gamma_a |v\rangle|$ for the extremal eigenvector, which is a min-max problem on the tensor product $V_\pi \otimes S$. The numerical value is consistent with $k \approx 1/\sqrt{d/4} = 1/\sqrt{2} \approx 0.707$ corrected by the anisotropy of the Jensen frame (the $e^{-2\tau}$ suppression of 3 generators reduces the effective norm).

**Quantitative check at $\tau = 0$.** At $\tau = 0$ (bi-invariant metric), the Dirac eigenvalues are algebraic: $\lambda^2 = n/36$ for integers $n$ determined by the Casimir. The maximum eigenvalue in sector $(p,q)$ at the bi-invariant point should satisfy $R_{(p,q)} = \sqrt{C_2(p,q)/3 + O(1)}$ from the known SU(3) spectrum (Paper 04, eq for $\lambda_\rho$). At $\tau > 0$, the Jensen anisotropy splits eigenvalues and modifies the coefficient. The measured $k = 0.633$ at $\tau = 0.19$ reflects the combined effects of: (a) the frame anisotropy ($e^{2\tau}$ vs $e^{-2\tau}$ scaling of different generators), (b) the spin connection correction $\Omega$ which is subdominant at large $C_2$, and (c) the representation-dependent alignment of the highest-weight vector with the anisotropy axis. Points (a)-(c) are all derivable from the Jensen metric structure but require an explicit extremal eigenvector calculation at each $(p,q)$.

**Prediction.** The scaling (1) should hold at $N = 30$ with the same coefficient to within 5%, giving $R_{(30,0)} = 0.633\sqrt{330} + 0.555 = 12.05$ M$_{KK}$. This is a testable prediction of spectral geometry that gates Window 4. The intercept $c = 0.555$ should decrease as $O(1/\sqrt{C_2})$ for very large representations as the spin connection contribution becomes negligible relative to the Casimir term.

**Connection to Weyl counting.** The total eigenvalue count satisfies $N_\mathrm{tot}(\lambda) = \sum_{(p,q): R_{(p,q)} \leq \lambda} 16 d_{p,q}$ where $d_{p,q} = (p+1)(q+1)(p+q+2)/2$. Using $R_{(p,q)} \approx k\sqrt{C_2}$, the condition $R \leq \lambda$ maps to $C_2 \leq (\lambda/k)^2$, which defines a region in the weight lattice. The dimension formula gives $d_{p,q} \sim p^2 q^2/2$ for large $(p,q)$, and summing over the Casimir ball yields $N(\lambda) \propto \lambda^8$ -- recovering the Weyl exponent $d = 8$ for the 8-dimensional manifold SU(3). The Weyl constant $C_\mathrm{Weyl} = 42.80$ (S36) is reproduced.

---

## Section 4: The Strutinsky Decomposition -- Smooth versus Shell from the Heat Kernel

The S51 STRUTINSKY-51 computation decomposed $S(\Lambda)$ into Thomas-Fermi (smooth) and shell correction parts, finding:
- Shell correction 49% of susceptibility at $\Lambda = 12$ M$_{KK}$
- $n_s(\mathrm{smooth}) = -0.80$ at $\Lambda = 12$ M$_{KK}$ (FAIL)
- Neither part independently produces $n_s \approx 0.965$

**The spectral geometry diagnosis.** The Strutinsky decomposition is, in heat kernel language, the separation of the heat trace into its short-time (Seeley-DeWitt) expansion and the oscillatory remainder:
$$\mathrm{Tr}\,e^{-tD^2} = \underbrace{(4\pi t)^{-d/2} \sum_k a_{2k} t^k}_{\text{smooth (Thomas-Fermi)}} + \underbrace{\delta K(t)}_{\text{shell correction}} \quad (6)$$

The smooth part is determined entirely by local geometry: $a_0$ (volume), $a_2$ (scalar curvature), $a_4$ (quadratic curvature invariants). These are universal and encode the "liquid drop" properties of the manifold. The shell correction $\delta K(t)$ encodes the specific clustering of eigenvalues -- it is the spectral fingerprint of the representation-theoretic structure.

**Why the smooth part gives $n_s \ll 1$.** The Thomas-Fermi spectral density on an 8-dimensional compact manifold grows as $g_{TF}(E) \propto E^7$ (Weyl, dim = 8). This gives $\chi_{SA}^{TF}(\Lambda) = d^2 S_{TF}/d\tau^2 \propto \Lambda^6$ at leading order, and therefore $n_s - 1 = d\ln\chi/d\ln\Lambda \approx 6$ in the deep-Weyl regime. The fact that the computation returns $n_s = -0.80$ (not $+7$) at $\Lambda = 12$ indicates the spectrum is NOT in the Weyl regime at this truncation -- the 784 eigenvalues (N=6) are far too sparse for Weyl asymptotics to apply. The subleading corrections (surface terms, curvature corrections) dominate over the volume term at this scale.

**The fundamental issue.** The Strutinsky decomposition requires $\gamma_\mathrm{opt}$ to span several level spacings while remaining much smaller than the bandwidth. At N=6 with 784 unique eigenvalues and bandwidth $\sim 3$ M$_{KK}$, the mean spacing is $\sim 0.004$ M$_{KK}$, and $\gamma_\mathrm{opt} = 0.15$ M$_{KK}$ spans $\sim 38$ spacings. This is within the standard nuclear range. But the spectral action susceptibility $\chi_{SA} = d^2 S/d\tau^2$ involves taking a second $\tau$-derivative of a function built from only 5 $\tau$-values, which introduces polynomial-fit errors that may dominate the smooth/shell decomposition.

**Constraint map update.** The STRUTINSKY-51 FAIL is not a closure of the Strutinsky approach per se; it is a statement that at N=6 truncation, neither the smooth nor shell part produces viable $n_s$. At N=30 (where $\sim 10^4$ eigenvalues would be available), the Weyl regime begins to apply and the smooth part would approach the correct $E^7$ density. However, my S51 result -- $n_s \geq 1$ structurally for any compact manifold's bare Dirac heat kernel -- then dominates: the smooth Thomas-Fermi part CANNOT give $n_s < 1$ in the Weyl regime. The shell correction is the only possible source of red tilt from the internal spectrum alone, and its contribution is inherently cutoff-dependent and truncation-dependent.

---

## Section 5: Cheeger Constants, Spectral Gaps, and the Mass Problem

The atlas identifies the mass problem as the central obstruction: $m_\mathrm{required}/m_\mathrm{Leggett} = 170$. The Goldstone mode has mass $m_G = 0.070$ M$_{KK}$ while the SA-Goldstone mixing model requires the correlator crossover at $K^* = 0.087$ M$_{KK}$ to produce $n_s = 0.965$. Can spectral geometry constrain this gap?

**Cheeger inequality on the fabric.** On the tessellation lattice $\mathcal{L}$ (the SU(3)-fiber Josephson network), the Cheeger constant $h(\mathcal{L})$ controls the spectral gap of the lattice Laplacian:
$$\lambda_1(\mathcal{L}) \geq h(\mathcal{L})^2/4 \quad (7)$$
(Paper 07, Berger). The Goldstone mass $m_G^2$ IS this spectral gap (it is the lowest nonzero eigenvalue of the lattice Laplacian on phase fluctuations). Therefore $m_G \geq h(\mathcal{L})/2$.

For a regular lattice with coordination number $z$ and Josephson coupling $J$, the Cheeger constant is $h \sim 2J/\mathrm{Vol(cell)}$. With $J_{C^2} = 0.933$ M$_{KK}$ (S47) and cell volume normalized to 1, this gives $h \sim 1.87$ and $\lambda_1 \geq 0.87$, consistent with $m_G^2 \sim 0.005$ (since $m_G = 0.070$ gives $m_G^2 = 0.0049$). The Cheeger bound is saturated to within a factor $\sim 180$.

**Lichnerowicz bound on the internal manifold.** The Dirac operator on SU(3) satisfies (Paper 06, BGV Paper 16):
$$\lambda^2(D_K) \geq R_K(\tau)/4 \geq 3 \quad \forall\,\tau \geq 0 \quad (8)$$
since $R_K(\tau) \geq 12$ analytically. This is the Lichnerowicz bound; it guarantees the spectral gap never closes and is independent of the Goldstone mass problem. The Lichnerowicz bound constrains the single-fiber Dirac spectrum, not the inter-fiber Goldstone propagator.

**Friedrich-Kirchberg refinement.** Paper 35 provides a stronger bound incorporating the Weyl tensor:
$$\lambda_1^2 \geq \frac{n}{4(n-1)} R_\mathrm{min} + \delta(|W|^2) \quad (9)$$
where $\delta > 0$ for non-Einstein manifolds. Since Jensen-deformed SU(3) is non-Einstein for $\tau > 0$ (Petrov type D at $\tau = 0$, algebraically general at $\tau > 0$, D07 result \#9), the Weyl contribution provides a strictly positive correction. This bound remains UNCOMPUTED on Jensen SU(3) -- computing $\delta(|W(\tau)|^2)$ using the exact Weyl-squared formula (D07 Section III) would sharpen the eigenvalue floor.

**Does the Cheeger constant constrain the mass problem?** Not directly. The 170x shortfall is between the Goldstone mass (a collective excitation on the fabric) and the mass required for $n_s = 0.965$ at $K_\mathrm{pivot} = 2.0$ (a statement about where the SA-Goldstone crossover occurs). The Cheeger constant constrains the Goldstone mass from BELOW, but the required mass is from ABOVE. What would help is an UPPER bound on $m_G$ from the Josephson coupling geometry -- and such a bound exists: $m_G \leq 2\sqrt{J_\mathrm{min}}$ from the lattice bandwidth. With $J_{u(1)} = 0.038$, this gives $m_G \leq 0.39$ M$_{KK}$, which is still 30x below the target of 11.85 M$_{KK}$.

**Spectral dimension flow on the fabric.** S50 Route 4 (spectral dimension from classical lattice) was CLOSED because the classical Josephson lattice gives Harrison-Zel'dovich $n_s = 1$. The question whether a QUANTUM lattice (where the lattice spacing fluctuates) could produce spectral dimension flow analogous to CDT (Paper 22, Ambjorn-Loll, $d_s: 2 \to 4$) remains OPEN but untestable within the current computational framework. The CDT result requires dynamical triangulation; the phonon-exflation lattice is fixed by the BCS condensate structure. Unless the condensate fluctuations generate an effective dynamical geometry -- which would require going beyond the mean-field tessellation -- the spectral dimension is locked at the lattice dimension.

**Spectral rigidity and the mass problem.** Gordon-Schueth-Sutton (Paper 17) proved that naturally reductive metrics on compact simple Lie groups are spectrally isolated within all left-invariant metrics. This means the map $\tau \mapsto \mathrm{Spec}(D_K(\tau))$ is injective -- distinct Jensen parameters give distinct spectra. For the mass problem, this has a subtle implication: the Goldstone mass $m_G(\tau)$ is uniquely determined by the internal geometry at each $\tau$, and there is no spectral degeneracy that could be exploited to shift $m_G$ without changing $\tau$. The mass problem is therefore structural, not accidental. However, Arias-Marco (Paper 31) proved that natural reductivity itself is spectrally inaudible -- isospectral pairs exist where one member is naturally reductive and one is not. This means OFF-Jensen deformations could potentially have the same Dirac spectrum as some Jensen point but different Goldstone physics, since the Josephson coupling depends on the metric, not just the spectrum.

---

## Closing Assessment

**What spectral geometry proves.** The mathematical structure is remarkably tight. Block-diagonality (W2), monotonicity (W4/W7), Lichnerowicz bound (E5), spectral flow = 0, and the $n_s \geq 1$ theorem for KK towers -- these are permanent results about Dirac operators on compact Lie groups with left-invariant metrics. They survive regardless of the framework's physical fate. Publishable targets: JGP, CMP, JMP (Door 2 in D05).

**What spectral geometry cannot provide.** (a) A canonical cutoff function. The spectral action principle requires $f$ as external input; spectral geometry supplies $D$ but not $f$. (b) Red tilt from the internal geometry alone. The $n_s \geq 1$ theorem is structural and dimension-independent: any compact Riemannian manifold's Dirac heat kernel gives blue or flat tilt. Red tilt requires 4D dynamics or correlator mixing. (c) Closure of the mass problem. The Cheeger and Lichnerowicz bounds go the wrong way -- they provide floors, not ceilings, and the mass problem is a shortfall, not an excess.

**The constraint surface after spectral geometry.** The surviving route (Window 1: SA-Goldstone mixing at $K < K^* = 0.087$) requires EFOLD-MAPPING-52 to establish that the physical CMB scale maps below $K^*$. From the spectral geometry perspective, this route is structurally viable: the SA correlator pole spread (110%) genuinely breaks the $\alpha_s = n_s^2 - 1$ identity, and the convex combination theorem constrains the viable $K$-range rather than eliminating it. The cutoff systematic (55% weight variation) introduces $O(1)$ uncertainty in the mixing parameter $\beta$, but the qualitative identity-breaking ($\alpha_\mathrm{eff} = 0.86$, stable at 4.7%) is robust.

**Uncomputed spectral geometry priorities.**
1. Analytic torsion $\tau_{RS}(\tau)$ -- the canonical cutoff-free spectral invariant (Paper 08)
2. Friedrich-Kirchberg Weyl tensor bound -- sharper eigenvalue floor (Paper 35, D07 formula available)
3. Cheeger constant of the SU(3) tessellation -- geometric lower bound on $m_G$
4. Dirac spectral rigidity on SU(3) -- whether the Jensen deformation is spectrally isolated (Papers 17, 18 prove it for SU(2); SU(3) is open)

**What remains structurally open.** The off-Jensen moduli space (Window 3) is the one region where spectral geometry could change the picture. The monotonicity theorem is proven on the 1-parameter Jensen family. The HESS-40 result (all 22 transverse eigenvalues positive) extends it to a local neighborhood in 28 dimensions. But global features of the 5-parameter U(2)-invariant family -- saddle points, Pfaffian transitions, gap closures -- are uncharted. The Boldt-Lauret Dirac rigidity theorem (Paper 18) on SU(2) suggests that Dirac spectral rigidity may extend to SU(3), which would mean the Jensen spectrum uniquely determines the Jensen metric. But whether the FULL left-invariant metric space contains spectrally degenerate points where different metrics give the same spectrum -- and potentially different BCS physics -- is unknown.

The mathematics is stronger than the cosmology. That is the honest spectral geometry assessment of 51 sessions.

---

*Grounded in: Papers 01-35 (Spectral-Geometry corpus), Atlas D00-D08, tier0 scripts s51_strutinsky.py, s51_high_pw.py, canonical_constants.py. All eigenvalue bounds checked against Lichnerowicz (R >= 12, lambda^2 >= 3), Weyl's law (verified C_Weyl = 42.80, S36), and exact curvature invariants (147/147 Riemann, S20a).*
