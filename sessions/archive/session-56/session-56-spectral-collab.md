# Session 56 Collaborative Review: Spectral-Geometer

**Session**: S56 -- Z Warriors Assemble: The Fabric Partition Function
**Reviewer**: spectral-geometer (opus)
**Date**: 2026-03-22
**Source**: `session-56-results-workingpaper.md` (20 computations, 4 waves)
**Focus**: PH breaking at the fabric level (MU-SHIFT-56 PASS), its spectral-geometric content, consequences for heat kernel asymptotics at finite mu, and the spectral dimension flow (SPECTRAL-DIM-FLOW-56).

---

## 1. The One Pass in Wave 1: What PH Breaking Means for the Spectrum

I computed W1-4 (MU-SHIFT-56). The result: mu_eff = -0.201 M_KK at the fold, PASS against the |mu_eff| > 0.1 threshold. This is the sole PASS in Wave 1. The other three gates returned FAIL (W1-1: F_fabric monotone, W1-2: integrability preserved, W1-3: N_pair=3 still integrable). The question assigned to me is precise: what does PH breaking at the fabric level mean for the spectral geometry?

**The single-cell PH theorem (S34, PERMANENT)**: The Dirac operator D_K on (SU(3), g_Jensen) satisfies {gamma_9, D_K} = 0, where gamma_9 is the chirality operator on the 8-dimensional fiber. This forces the single-cell spectrum to be exactly symmetric: for every eigenvalue +lambda, there exists -lambda with equal multiplicity. The immediate consequence is mu = 0 in both canonical and grand canonical ensembles (S34 MU-35a, GC-35a). The heat trace

K(t) = Tr exp(-t D_K^2) = sum_n exp(-t lambda_n^2)      ... (1)

depends only on lambda_n^2, and the pairing lambda <-> -lambda is invisible to K(t). The Seeley-DeWitt expansion reads the geometry correctly: a_0 gives Vol(SU(3)), a_2 gives (1/6) integral R dV, a_4 gives the curvature-squared invariants. PH symmetry is transparent to the heat kernel because K(t) involves D_K^2, which has the same spectrum regardless of PH pairing.

**The fabric Hamiltonian breaks PH**: The tight-binding Hamiltonian H_TB on the 32-cell Voronoi graph has two PH-breaking sources:

(i) The graph is non-bipartite: adjacency eigenvalue skewness = 1.084. A bipartite graph has spectrum symmetric about zero (if E is an eigenvalue, so is -E). The 32-cell CG graph with 93 bonds (50 C2 + 24 su2 + 19 u1) has odd cycles, violating this. Skewness 1.084 means the distribution of eigenvalues has a fat right tail.

(ii) The Casimir on-site energies C_2(p,q)/3 range from 0 to 20, with std/mean = 0.56. This potential disorder is the representation-theoretic analog of Anderson on-site disorder, except it is deterministic -- set by the (p,q) labels of each Peter-Weyl sector.

These two sources are GEOMETRIC. They follow from the topology and Casimir structure of the CG graph, independent of BCS pairing or dynamics. The result is a spectral asymmetry at the fabric level: the half-filling chemical potential mu_half differs from the PH-symmetric midpoint mu_PH by mu_eff = -0.201 M_KK at the fold.

**What this means for the Dirac operator**: The single-cell D_K has PH-exact spectrum. The fabric effective Hamiltonian H_TB is NOT a Dirac operator -- it is a discrete Laplacian on the CG graph, dressed by Casimir potentials and bond-type-specific hopping (J_C2 = 0.933, J_su2 = 0.059, J_u1 = 0.038). The fabric Dirac operator D_fabric -- if one could construct the full spectral triple on the 32-cell array -- would need to account for the graph structure. The PH breaking is a property of THIS object, not of the continuum D_K.

The structural content: the single cell preserves PH because D_K is a first-order differential operator on a homogeneous space with a chirality grading. The fabric breaks PH because the inter-cell coupling introduces a graph Laplacian (second-order, discrete) with non-bipartite topology. The passage from D_K to H_TB is the passage from first-order Dirac to second-order Schrodinger, and PH symmetry does not survive this passage generically.

---

## 2. Does mu_eff Feed Back into the Heat Kernel Asymptotics?

The heat kernel on the single cell is

K_cell(t) = Tr exp(-t D_K^2)                             ... (2)

and its Seeley-DeWitt expansion gives geometric invariants of (SU(3), g_Jensen) that are independent of mu. This is a structural fact: the heat kernel of D_K^2 encodes the geometry through the local curvature of the manifold and the connection on the spinor bundle. There is no chemical potential in this object.

The fabric heat trace is a different object. Define

K_fabric(t) = Tr exp(-t H_TB)                            ... (3)

where H_TB is the 32x32 tight-binding Hamiltonian. This is the return probability on the CG graph, and I computed it in W3-4 (SPECTRAL-DIM-FLOW-56). The Seeley-DeWitt expansion for a graph Laplacian is not the standard continuum expansion -- on a finite graph, the heat kernel is an entire function with convergent Taylor series, not an asymptotic expansion (HEAT-KERNEL-AUDIT-45, Level 3). The expansion

K_fabric(t) = sum_n exp(-E_n t) = N + t * sum_n (-E_n) + (t^2/2) * sum_n E_n^2 + ...   ... (4)

converges to machine epsilon in finitely many terms. The "a_0" is N = 32 (vertex count). The "a_2" analog is -sum E_n = -M_total = -96.20 M_KK at the fold (from W3-8). These are not geometric Seeley-DeWitt coefficients -- they are spectral moments of the graph Hamiltonian.

Now, mu_eff enters when we consider the OCCUPIED heat trace:

K_occ(t; mu) = Tr [f(H_TB - mu) * exp(-t H_TB)]         ... (5)

where f is the Fermi-Dirac distribution. At T_GH = 0.590 M_KK, f(E - mu) is a smooth step function. The occupied trace is the generating function for occupied spectral moments:

K_occ(t; mu) = sum_n f(E_n - mu) exp(-E_n t)             ... (6)

At mu = 0 (PH-symmetric case), f(E_n) is nearly symmetric about the midpoint of the spectrum, and K_occ has the same symmetry properties as K_fabric up to O(exp(-E_gap/T)) corrections. At mu = mu_eff = -0.201 M_KK, the occupation shifts: the asymmetric graph spectrum is sampled asymmetrically. The first occupied moment becomes

sum_n f(E_n - mu_eff) E_n =/= sum_n f(E_n) E_n           ... (7)

and the difference is the source of the dS_f/dtau sign change found in S55 (SF-SIGN-55 PASS) and confirmed in W2-1 at the physical mu_eff.

**The feedback loop that does not close**: The mu_eff correction shifts dF_cells/dtau by -3.70 M_KK at the fold (W2-1). The Josephson slope to overcome is +1711 M_KK. The ratio is 0.22%. The spectral moments of the occupied fabric Hamiltonian are different from the unoccupied ones, but the difference is structurally insufficient. The reason is dimensional: mu_eff = -0.201 M_KK shifts O(2) modes in a spectrum of O(32) modes. The spectral moments change by O(mu_eff / BW) ~ 3%, not O(1).

For the heat kernel specifically: the Seeley-DeWitt coefficients of the CONTINUUM D_K are independent of mu because D_K^2 has no chemical potential parameter. The fabric H_TB does have an effective mu, but its "heat kernel coefficients" are spectral moments, not geometric curvature invariants. The feedback of mu_eff into spectral geometry is real but operates through a different channel (occupation-weighted spectral sums) than the continuum heat kernel (curvature polynomials).

**Structural classification**: The PH breaking is GEOMETRIC (graph topology + Casimir disorder). Its spectral-geometric content is a shift in the occupied spectral moments, not a modification of the underlying curvature. The heat kernel of the manifold (SU(3), g_Jensen) is unaffected. The heat kernel of the fabric graph H_TB is affected, but the effect is 0.22% of the Josephson slope.

---

## 3. The Spectral Dimension Flow: What W3-4 Actually Shows

I computed the spectral dimension flow d_s(E) = -2 d(ln P)/d(ln t) from the 32-cell TB spectrum at the fold. The results:

| Quantity | Value |
|:---------|:------|
| Peak d_s | 1.732 |
| E at peak | 1.159 M_KK |
| d_s at omega_J = 0.715 | 1.656 |
| d_s at 2*Delta = 0.929 | 1.713 |
| UV limit d_s | 0.023 |
| IR limit d_s | 0.000 |
| Weyl dimension d_W | 2.154 |
| Hausdorff dimension d_H | 1.934 |

**The assigned question**: Does the spectral dimension flow change at finite mu?

The spectral dimension d_s(t) is defined from the TOTAL heat trace K(t) = sum_n exp(-E_n t), not the occupied trace. It is a geometric property of the graph, independent of occupation. At finite mu, the physical return probability for a diffusing particle on the fabric is

P_occ(t) = (1/N_occ) sum_n f(E_n - mu) exp(-E_n t)      ... (8)

and the "occupied spectral dimension" d_s^occ(t; mu) = -2 d(ln P_occ)/d(ln t) is a different quantity. In the IR (t -> infinity), d_s^occ is dominated by the lowest occupied level, which shifts with mu. In the UV (t -> 0), all modes contribute regardless of occupation (f -> 1/2 at high energy in the Fermi-Dirac tail), so d_s^occ -> d_s.

At mu = -0.201 M_KK (negative, meaning below the spectral midpoint), the occupation shifts weight toward lower eigenvalues. This has two effects:

(i) The IR onset of d_s^occ shifts to slightly lower energy (the lowest heavily occupied mode determines when d_s starts rising from zero).

(ii) The peak d_s^occ could increase slightly if the occupation-weighting concentrates spectral weight in the band center where d_s is maximal.

However, both effects are small. The occupation at mu = -0.201 is N ~ 1.9 out of 32 modes (W2-1). The vast majority of modes are unoccupied (f ~ 0), and P_occ is dominated by the 2 lowest modes. The "occupied spectral dimension" would be d_s^occ ~ 0 for most of the energy range (only 2 levels, no diffusion). This is not a useful geometric probe -- it tells us the fabric is nearly empty at the physical mu, not that the geometry has changed.

**The structural finding of W3-4**: The spectral dimension flow is smooth and featureless at BOTH collective thresholds (omega_J and 2*Delta). The flow d_s(E) increases monotonically from 0 to 1.73, peaks at E = 1.16 M_KK, and decreases back to 0. No kink, plateau change, or inflection point marks the Josephson or pairing scales. The spectral dimension is a kinematic (band-structure) observable, not a dynamical one. It cannot distinguish between the Josephson-coupled and pair-broken regimes.

This is a Level 3 result per HEAT-KERNEL-AUDIT-45: the spectral dimension on a finite graph goes to zero (not the manifold dimension) in both UV and IR limits. The peak d_s = 1.73 reflects the graph connectivity (Hausdorff dimension 1.93, Weyl dimension 2.15), not the 8-dimensional SU(3) manifold. The continuum spectral dimension d_s = 8 requires infinitely many modes; the 32-mode truncation gives d_s^max ~ 2.

**Implication for the CC question**: The spectral dimension flow cannot diagnose adiabatic gap leakage. It is insensitive to: (a) the Josephson gap that protects the vacuum, (b) the BCS pairing gap, (c) the chemical potential, (d) the occupation pattern. All of these are encoded in K_occ(t; mu, Delta), not in K(t). The correct probe for the CC is the occupied spectral action S_f(tau; mu, Delta) = sum_n f(E_n - mu) |E_n|, which does depend on occupation. The spectral dimension is the wrong functional for this question.

---

## 4. The CC as Adiabatic Gap Leakage: The Spectral Geometer's Reading

Einstein identifies the CC as an adiabaticity problem (his Section 2). Hawking frames it as exponential suppression through the Josephson gap (his eq. 1). Baptista traces the monotonicity to J_C2(tau)^2 and the C^2 Casimir eigenvalue. I provide the spectral geometry reading.

The heat kernel K(t) = Tr exp(-t D^2) encodes the spectrum through its Taylor coefficients. The spectral action S(Lambda) = Tr f(D^2/Lambda^2) encodes it through a smooth cutoff. Both are sums over eigenvalues weighted by a non-negative kernel. The S37 Structural Monotonicity Theorem established that ANY such sum, if the squared eigenvalues <lambda^2>(tau) are monotonically increasing, produces a monotone functional. This was the wall that closed all spectral action stabilization routes.

S56 adds a new layer: the FABRIC spectral action includes the Josephson term, which is NOT a sum over eigenvalues of a single operator. F_Josephson = -N * E_J * m involves the pair-transfer matrix element (E_J), the graph connectivity (N = 50 bonds), and the order parameter (m). This is NOT a heat kernel functional. It is a many-body correlation function.

The Josephson Monotonicity Theorem (stated precisely by Einstein in his review) says that in the deeply ordered regime, F_Josephson dominates and inherits the monotonicity of E_J(tau). But E_J(tau) = J_C2(tau)^2 * F_anom(tau), where J_C2 is the hopping amplitude (a SINGLE eigenvalue of the fiber Laplacian restricted to the C^2 sector) and F_anom is a spectral sum (sum over quasiparticle energies). The spectral sum F_anom is nearly constant (~4.6 at fold, varying 15% over [0, 0.5]), while J_C2 varies 7.4x. The product is controlled by the single eigenvalue J_C2, not by the spectral sum.

This is the inversion of the heat kernel hierarchy. In the standard Seeley-DeWitt framework, a_0 (volume, sum over ALL modes) dominates a_2 (curvature, selective weighting) dominates a_4 (curvature-squared, highly selective). Each higher coefficient picks out finer geometric detail. The Josephson term inverts this: a SINGLE representation-theoretic quantity (J_C2, the C^2 Casimir hopping) controls the entire thermodynamics. The spectral sum F_anom, which involves all 992 modes, is the subdominant correction.

This inversion is WHY the fold is invisible to F_fabric. The fold lives in the collective eigenvalue structure -- the B2 minimum at tau = 0.190, the van Hove singularity, the shell corrections. All of these are encoded in the FINE structure of the spectrum (differences between nearby eigenvalues, density of states at the Fermi surface). J_C2 is a coarse spectral quantity -- it is the lowest non-trivial C^2 eigenvalue, insensitive to fine structure. The gap between coarse and fine spectral information is the gap between |F_J| = 347 M_KK and |F_BA| = 7 M_KK. The fold, as a fine spectral feature, cannot overcome the coarse spectral dominance.

**The mu_eff correction in this language**: mu_eff = -0.201 M_KK shifts the occupation f(E_n - mu) in the spectral sum F_anom. This modifies F_anom by O(mu/BW) ~ 3%, which propagates to E_J as a 3% shift, which produces a 3% change in dF_J/dtau. Against a Josephson slope of +1711, this is 0.22%. The chemical potential correction is a fine spectral effect trying to overcome a coarse spectral dominance. It cannot.

---

## 5. What Survives and What Is Closed

### Structural results (PERMANENT)

**SR-1**: PH symmetry of D_K does NOT extend to the fabric Hamiltonian H_TB. The 32-cell CG graph is non-bipartite (skewness 1.084) with Casimir disorder (std/mean = 0.56). mu_eff = -0.201 M_KK at the fold. This is GEOMETRIC (graph topology, deterministic).

**SR-2**: The spectral dimension of the 32-cell fabric is d_s^max = 1.73, smooth and featureless at all collective thresholds. d_s is insensitive to occupation, pairing, and chemical potential. Level 3 (HEAT-KERNEL-AUDIT-45 classification applies to the graph heat kernel identically).

**SR-3**: The Josephson term F_J inverts the heat kernel hierarchy: a single representation-theoretic quantity (J_C2) controls the thermodynamics, while spectral sums over all modes (F_anom) enter as O(15%) corrections. This is structurally distinct from the Seeley-DeWitt hierarchy where sums-over-all-modes (a_0) dominate.

### Closed channels

**CL-1**: Spectral dimension as CC probe -- CLOSED. d_s cannot distinguish Josephson-coupled from pair-broken regimes. It is kinematic, not dynamical.

**CL-2**: mu_eff feedback into heat kernel -- STRUCTURALLY INSUFFICIENT. The 0.22% contribution to the Josephson slope cannot produce a minimum. This is closed within the current 32-cell model.

### Open channels

**OP-1**: The PH breaking is real (mu_eff = -0.201, PASS) and grows with graph size (more non-bipartite cycles, more Casimir variance). On a LARGER fabric, mu_eff could approach mu_half, where the S55 SF-SIGN-55 non-monotonicity is dramatic. But the Josephson slope also grows extensively with bond count. The scaling question: does mu_eff/mu_half grow faster or slower than N_bonds? This is uncomputed.

**OP-2**: The Connes distance on the truncated Jensen SU(3) crystal (S45 Way Forward #14, still open). The spectral triple (C(SU(3)), D_K, J) restricted to the 32-cell Peter-Weyl lattice defines a finite noncommutative geometry with a Connes metric. The W1-4 result shows this metric has PH-asymmetric structure. Computing the actual Connes distances d(x,y) = sup{|a(x) - a(y)| : ||[D,a]|| <= 1} on this lattice would characterize the geometric content of the PH breaking beyond the crude mu_eff observable.

**OP-3**: The spectral zeta function at non-integer s (S45 Way Forward #5). zeta_fabric(s) = sum_n E_n^{-s} at s > 4 suppresses the UV and may reveal fold structure that the heat kernel (s = infinity limit) cannot access. With 32 eigenvalues, this is a convergent sum at any s > 0. Uncomputed on the fabric.

---

## Closing: The Spectral Geometer's Verdict on S56

The session asked a well-posed question and received a definitive answer. F_fabric is monotone. The master gate FAILS. The fold -- that exquisite fine spectral feature with its van Hove singularity, its B2 minimum, its shell corrections -- is invisible to the fabric free energy because the Josephson coupling J_C2(tau)^2 is a coarse spectral quantity that overwhelms all fine structure by a factor of 50.

My own computation (W1-4, MU-SHIFT-56 PASS) establishes that the fabric Dirac spectrum differs qualitatively from the single-cell Dirac spectrum: PH is broken, mu is nonzero, the occupied moments shift. But the quantitative consequence is 0.22% of what is needed. This is the recurring structural pattern of the project: the fold generates O(1%) spectral anomalies (shell corrections 6.5%, van Hove enhancement 2.6x, spectral dimension depression 13%), but the leading-order monotonicity is always O(100%) from a coarser spectral quantity (a_0 for volume, J_C2 for Josephson, <lambda^2> for spectral action).

The heat kernel asymptotics at finite mu are well-defined but irrelevant for stabilization. The spectral dimension at finite mu is ill-defined (only ~2 modes occupied) and would show d_s ~ 0 everywhere. Both probes confirm that mu_eff is too small to matter in the current model.

The surviving open question from my perspective is OP-1: the scaling of mu_eff with fabric size. If the PH breaking scales faster than the Josephson dominance, larger fabrics could enter a qualitatively different regime. If not, the mu_eff channel is closed at all scales.

I note for the record: 47 closures and counting. The constraint surface is extremely narrow. The fold, the most distinctive geometric feature of (SU(3), g_Jensen), remains invisible to every thermodynamic functional tested. The spectral geometry of the single cell is rich and well-characterized (proven monotonicity theorems, exact Seeley-DeWitt coefficients, eigenvalue bounds, spectral flow, Kirchberg bounds). The spectral geometry of the fabric is a coarser object, dominated by a single number (J_C2). The passage from fine to coarse is irreversible in the current model.
