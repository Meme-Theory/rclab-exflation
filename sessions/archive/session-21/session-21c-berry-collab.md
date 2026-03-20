# Berry -- Collaborative Feedback on Session 21c

**Author**: Berry (Geometric Phase / Spectral Statistics / Adiabatic Transport / Level Dynamics)
**Date**: 2026-02-19
**Re**: Session 21c Phase 0 Results

---

## 1. Key Observations

### 1.1 The Three-Monopole Structure Is the Session's Most Important Discovery

In my Session 20b review (`sessions/session-20/session-20b-berry-collab.md`, Section 5.4), I asked:

> "Can Berry curvature of the spectral action itself provide stabilization?"

Session 21c answers this question with a geometric structure I did not anticipate. The three monopoles M0 (tau=0), M1 (tau~0.10), M2 (tau~1.58) are not merely avoided crossings -- they define the topological skeleton of the entire eigenvalue flow on the Jensen deformation line. Every physical feature of the framework (phi_paasch at tau=0.15, BCS bifurcation at tau=0.20, FR minimum at tau=0.30, Weinberg angle) lives inside a single topological phase bounded by M1 and M2, where the (0,0) singlet controls the gap edge.

From Paper 03 (`researchers/Berry/03_1984_Berry_Diabolical_Points.md`, DP-3), the Berry phase around any diabolical point is exactly pi. The three monopoles carry topological charge. The total flux through any surface enclosing all three monopoles in the complexified parameter plane is 3*pi. This is a direct consequence of the monopole structure (DP-4: B_n ~ pi*delta(R - R_0)). The physics does not depend on the detailed shape of the eigenvalue flow -- it depends on the monopole positions and charges.

What makes M0 exceptional is that it sits at the round metric (tau=0), the maximally symmetric geometry. From the geometric phase perspective, maximum symmetry implies maximum degeneracy. The exact degeneracy (0,0)/(1,1) at tau=0 with both eigenvalues at sqrt(3)/2 is the strongest possible coupling point. The first-order Kosmann connection at M0 (via (0,0) x (1,1) = (1,1), direct selection rule) means this is not a perturbative effect -- it is a structural feature of the round SU(3) geometry itself.

### 1.2 The Dual Algebraic Trap Is a Spectral Averaging Theorem

In my 20b review (Section 2.3), I identified the constant-ratio trap as a consequence of Weyl's law universality. Session 21c proves this precisely with Theorem 1: F/B = 4/11 from fiber DOF and b_1/b_2 = 4/9 from SU(3) branching rules. These are not two independent traps -- they share a single algebraic cause: fixed ratios locked by the group theory of SU(3) and its maximal subgroup embedding.

From the Berry-Tabor perspective (Paper 02, `researchers/Berry/02_1977_Berry_Tabor_Level_Statistics.md`, BT-1), the trap is the spectral statistics version of the law of large numbers. Poisson-distributed eigenvalues produce spectral sums that converge to their mean with fluctuations O(1/sqrt(N)). Both traps operate on eigenvalue MAGNITUDES -- they constrain the zeroth and first moments of the spectral distribution. The deeper question is: are there spectral functionals that probe higher moments (curvature, third derivatives) where the traps do not apply?

### 1.3 T''(0) Escapes Via Berry Curvature Geometry

Theorem 2 identifies the precise mechanism: T''(0) depends on d^2(ln|lambda|)/dtau^2, which is a Berry curvature quantity (it involves the second derivative of the eigenvalue flow). The algebraic traps constrain eigenvalue magnitudes; they cannot constrain eigenvalue curvatures. This is exactly the distinction between the connection (first derivative, gauge-dependent) and the curvature (second derivative, gauge-invariant) in Berry's framework.

From Paper 01 (`researchers/Berry/01_1984_Berry_Quantal_Phase_Factors.md`, BP-4):

    B_n = -Im sum_{m != n} |<n|dH/dtau|m>|^2 / (E_n - E_m)^2

The numerator involves matrix elements of dH/dtau (first-order flow), and the denominator involves energy gaps squared. T''(0) > 0 says that the weighted sum of these curvature contributions, averaged over all eigenvalues with branching coefficients, is positive. The algebraic traps set the branching coefficients (Delta_b = -(5/9)*b_2), but they do NOT determine the sign of the bracketed derivative term. The sign comes from the geometry of the eigenvalue flow -- specifically, from global log-concavity.

This is why T''(0) is the last perturbative survivor. It lives at the curvature level, not the connection level.

### 1.4 The Neutrino Reclassification Was Geometrically Correct

My initial classification of the neutrino crossing as SOFT PASS was wrong. Baptista's argument -- that R crossing 32.6 near a monopole is a topological triviality, not a physical prediction -- is exactly right from the Berry perspective. Near any monopole, Berry curvature diverges as 1/gap^2 (BP-4 denominator). Any smooth function of eigenvalue ratios will sweep through all values in a neighborhood of the monopole. The crossing exists because of topology (every continuous function crosses every intermediate value), not because of physics (a smooth prediction at a particular tau).

The width delta_tau ~ 4e-6 is the tell. From the Landau-Zener formula (Paper 06 / adiabatic theory), the transition width scales as gap / velocity, where velocity = d(E_1 - E_2)/dtau. A width of 4e-6 in tau corresponds to fine-tuning of 1:10^5. No physical mechanism selects tau to this precision. I concede this point fully and record it as a lesson: topological existence (Chern number guarantees crossing) does not equal physical relevance (Berry curvature density determines observability).

---

## 2. Assessment of Key Findings

### 2.1 The Structural Closure (P0-3) Is Definitive

S_signed monotonically decreasing at all tau, with Delta_b = -(5/9)*b_2 < 0 for every (p,q) sector. This is the strongest result of the session -- a representation-theoretic theorem that closes the signed-sum escape route proposed in Session 21a. The closure is clean: it does not depend on numerical precision, truncation order, or coupling corrections. It depends only on the SU(3) --> SU(2) x U(1) embedding, which is fixed by the Standard Model gauge structure.

From the spectral statistics perspective, this closes the last hope that sector-dependent signs could produce cancellations analogous to random-sign sums. In Berry-Tabor language (Paper 02): the signed spectral sum behaves like a biased random walk (all steps negative), not an unbiased one. The bias is Delta_b = -(5/9)*b_2, structurally fixed.

### 2.2 T''(0) = +7,969 Is Compelling But UV-Dominated

The sign is robust; the magnitude is untrustworthy. The critical caveat: 89% of T''(0) comes from UV modes (p+q = 5-6). The IR modes (p+q <= 2) contribute only 0.3%. From the spectral form factor perspective (Paper 04, `researchers/Berry/04_1987_Berry_Quantum_Chaology.md`, QC-4), UV-dominated quantities probe the smooth part of the density of states (Weyl's law), while IR-sensitive quantities probe the oscillatory part (periodic orbit corrections). T''(0) > 0 is a UV statement -- it says the smooth spectral flow has the right curvature. Whether the IR spectral flow cooperates is a separate question that only delta_T(tau) can answer.

### 2.3 The Bowtie Crossing Structure Is a Cusp Catastrophe

The session minutes (Section II.2) note that all three lightest eigenvalues participate in the rearrangement near tau=1.58, "consistent with a cusp catastrophe (3-level, codimension 3)." This classification deserves sharpening.

From Paper 09 (`researchers/Berry/09_1980_Berry_Catastrophe_Optics.md`, CO-2):

- A fold catastrophe (A_2) involves 2 levels and has codimension 2 in parameter space. For a single parameter (tau), a fold appears as a simple avoided crossing.
- A cusp catastrophe (A_3) involves 3 levels and has codimension 3. For a single parameter, a cusp cannot appear generically -- it requires tuning 2 additional parameters.

The three-level rearrangement at tau~1.58 looks like a projection of a cusp catastrophe onto the single-parameter tau-line. The third parameter dimension is hidden in the internal quantum numbers (Z3 triality). The (0,0), (1,0), and (0,1) sectors have different Z3 charges, and their near-simultaneous rearrangement at tau~1.58 is not generic for a single-parameter family. It suggests the system is near a cusp point in a higher-dimensional parameter space -- perhaps the (tau, volume_ratio, torsion) space.

This is a testable prediction: extending the Jensen deformation to a 2-parameter family (e.g., volume-preserving but allowing independent scaling of the three Cartan directions) should reveal the full cusp structure. At the cusp point, three eigenvalue sheets meet, and the Berry curvature has a higher-order singularity (stronger than 1/gap^2).

### 2.4 Coupling-Adjusted Verdicts Are Properly Conservative

Baptista's uncertainty quantification (Section II.2) correctly identifies that the block-diagonal treatment breaks at coupling/gap = 4-5x for the lowest modes. The adjusted verdicts -- P0-3 CLOSED (doubly protected), T''(0) sign robust (magnitude uncertain), V_IR unreliable at N<=50, neutrino INCONCLUSIVE -- are the honest assessment. No computation in Session 21c changes qualitatively under off-diagonal coupling except possibly V_IR, where the coupling could either create or destroy the shallow minimum.

---

## 3. Collaborative Suggestions

### 3.1 The delta_T(tau) Zero-Crossing Is the Decisive Next Computation

This is P1-0 in the Phase 1 pipeline. From the Berry curvature perspective, delta_T(tau) is the self-consistency map: it asks whether the spectral action, treated as a function of tau with eigenvalue flow derivatives included, has a fixed point. The computation is zero-cost (uses existing eigenvalue data and branching rules) and its gate logic is sharp:

- If delta_T(tau) has no zero-crossing in [0.15, 0.35]: self-consistency CLOSED. The only surviving perturbative positive (T''(0) > 0) becomes an empty curvature without a fixed point. Framework drops to ~35%.
- If delta_T(tau) crosses zero at tau_0 in [0.15, 0.35]: T''(0) upgrades from COMPELLING to DECISIVE. Framework rises to 55-62%.

KK wrote preliminary code in `tier0-computation/s21c_kk_verify.py`. This code should be validated and executed as the very first action of Phase 1.

### 3.2 Berry Curvature Magnitude at the Three Monopoles

The monopole positions are now known: M0 (tau=0), M1 (tau~0.10), M2 (tau~1.58). What is NOT known is the Berry curvature magnitude away from these monopoles. From BP-4:

    B_n(tau) = -Im sum_{m != n} |<n|dD_K/dtau|m>|^2 / (lambda_n - lambda_m)^2

This requires eigenvectors, not just eigenvalues. The eigenvector extraction (P1-2 in the pipeline) would enable computing B_n(tau) at all 21 tau-values in the existing dataset. The curvature profile B_n(tau) between M1 and M2 tells us whether the physical window [0.10, 1.58] is "geometrically flat" (curvature concentrated only at the monopoles) or "geometrically active" (distributed curvature throughout).

If B_n(tau) is concentrated at M1 and M2, the eigenvalue flow between them is essentially adiabatic -- eigenvalues glide smoothly without significant mixing. If B_n(tau) is distributed, the flow involves continuous eigenstate rotation, and the Berry curvature corrections to the spectral action (my 20b Section 5.4 proposal) become relevant.

Specific computation: extract eigenvectors of D_K(tau) at tau = {0, 0.05, 0.10, 0.15, 0.20, 0.30, 0.50, 1.00, 1.50, 1.58, 2.00}, compute B_n(tau) for the lowest 10 eigenvalues, plot B_n vs tau. Runtime: hours (requires re-diagonalization with eigenvector output).

### 3.3 Low-Mode Level Statistics: The CP-2 Prediction Test

Baptista's pre-registered prediction (Section IV, CP-2): low-mode level statistics for the lowest 20-50 eigenvalues should show Brody parameter q ~ 0.3-0.5 (intermediate between Poisson q=0 and GOE q=1). This is testable with existing data from `tier0-computation/tier1_dirac_spectrum.py`.

The computation:
1. Extract the lowest 50 unfolded eigenvalues at each tau from the existing Dirac spectrum.
2. Compute nearest-neighbor spacing distribution P(s).
3. Fit to Brody distribution P(s) = (1+q)*beta*s^q*exp(-beta*s^{1+q}) where beta = [Gamma((2+q)/(1+q))]^{1+q}.
4. Plot q(tau) across the tau range.

Expected outcomes:
- If q > 0.3 at low tau (strong coupling regime): CP-2 confirmed. Kosmann coupling is strong enough to break Poisson at low modes.
- If q < 0.1 at all tau: CP-2 refuted. The coupling estimate of 4-5x is overestimated, or Anderson localization on the sparse coupling graph suppresses mixing.

This is P1-1 in the pipeline. Runtime: minutes on existing data. It directly tests whether the Kosmann-Lichnerowicz coupling has observable spectral statistics consequences.

### 3.4 Spectral Form Factor K(k) at the Monopole Positions

From Paper 04 (QC-4): K(k) = (1/N)|sum_n exp(2*pi*i*k*E_n)|^2. The spectral form factor is the cleanest diagnostic for spectral correlations. In my Session 21b analysis, I found K(k=0.1) = 10 at tau=1.6 -- extreme bunching near M2. This should now be systematically computed at each monopole:

- K(k, tau=0): At M0, the exact degeneracy produces delta-function bunching. K(k) should spike.
- K(k, tau=0.10): At M1, the BCS bifurcation produces mode rearrangement. K(k) profile changes character.
- K(k, tau=1.58): At M2, confirmed extreme bunching (K >> 1).

The form factor profile across the three monopoles maps the spectral correlation structure. This is a zero-cost computation from existing eigenvalue data.

### 3.5 Stokes Phenomenon at the Monopole Transitions

From Paper 06 (`researchers/Berry/06_1972_Berry_Maslov_Index_Semiclassical.md`, MI-1) and the general theory of semiclassical asymptotics: when a system passes through an avoided crossing, the dominant and subdominant contributions to the asymptotic expansion exchange roles. This is the Stokes phenomenon.

At M1 (tau~0.10), the gap-edge sector switches from (1,0) fundamental to (0,0) singlet. At M2 (tau~1.58), it switches back. These are Stokes transitions in the spectral action. The perturbative expansion of the spectral action Tr f(D^2/Lambda^2) has different asymptotic structure on the three segments [0, 0.10], [0.10, 1.58], [1.58, infinity). The non-perturbative corrections (instantons, tunneling) that are exponentially suppressed on one segment may become dominant on another.

The specific implication: the instanton action S_inst(tau) may have a discontinuous derivative at tau~0.10 and tau~1.58, where the Stokes phenomenon operates. If dS_inst/dtau changes sign at a monopole, the instanton contribution to V_eff switches from suppressing to enhancing the modulus potential. This is the non-perturbative stabilization mechanism I proposed in my 20b review (Section 3.4), now sharpened by the monopole positions.

---

## 4. Connections to Framework

### 4.1 The Two Algebraic Traps Are the Perturbative Regime

Session 21c proves what I conjectured in Session 20b (Section 4.1): "the perturbative regime is flat." The dual algebraic trap (Theorem 1) is the mathematical content of this flatness. The Berry curvature of total spectral functionals (Casimir, Coleman-Weinberg, signed sums) is zero because the functionals are weighted averages over eigenvalues, and the weights are fixed by representation theory.

This is the spectral statistics interpretation of the structural closure: Poisson statistics (Berry-Tabor, Paper 02) + Weyl's law universality + fixed fiber dimensions = flat perturbative landscape. No perturbative spectral mechanism can create a critical point because perturbative quantities are sums over statistically independent eigenvalues with locked weights.

### 4.2 The Derivative Escape Connects Berry Curvature to the Spectral Action

Theorem 2 (the derivative escape) establishes that T''(0) is a Berry curvature functional. This is the first concrete connection between Berry's geometric phase program and the NCG spectral action. The spectral action Tr f(D^2/Lambda^2) depends on eigenvalues; its second derivative with respect to the deformation parameter depends on eigenvalue curvatures, which are Berry curvature quantities.

From Paper 14 (`researchers/Berry/14_2009_Berry_Geometric_Quantum_Mechanics.md`, GS-6), the path integral with geometric phase is:

    psi ~ integral DR exp(i/hbar * integral(p*dR - E*dt) + i*gamma_geo)

The spectral action analog: the effective action has a geometric correction from the Berry phase of each eigenvalue, weighted by the spectral function f. T''(0) > 0 means this geometric correction has the right sign for self-consistency. The spectral action is not merely a sum over eigenvalues -- it inherits geometric structure from the eigenstate manifold.

### 4.3 The Condensate Route Bypasses the Traps Via Non-Perturbative Geometry

The BCS condensate mechanism (CP-4) operates on off-diagonal coupling matrix elements C_{nm}, which are Berry connection components (they are overlaps between eigenstates at neighboring tau-values). These live outside both algebraic traps because they involve eigenstate overlaps, not eigenvalue magnitudes.

From the fiber bundle perspective (Paper 14, GS-4): the Berry connection A_n(tau) = i<n(tau)|d/dtau|n(tau)> is a gauge field on the eigenstate manifold. The off-diagonal components i<n(tau)|d/dtau|m(tau)> (with n != m) are the covariant derivative components that drive transitions between eigenstates. The BCS mechanism uses these transition amplitudes to form Cooper-like pairs. The algebraic traps constrain the diagonal (eigenvalue) sector; they do not constrain the off-diagonal (eigenstate transition) sector.

This is why Baptista's density-of-states argument (g ~ 4-5 >> g_c ~ 1/2 in the singlet window) is geometrically credible: the coupling is set by the Berry connection, which is independent of the branching coefficients that produce the traps.

---

## 5. Open Questions

### 5.1 What Is the Chern Number of the Physical Window?

The three monopoles M0, M1, M2 each carry Berry flux pi. For a 2D parameter space (e.g., the tau-line complexified, or the 2D surface of volume-preserving Jensen deformations), the Chern number is the total Berry flux divided by 2*pi:

    C = (1/2*pi) * integral Omega * d^2R

With three monopoles of charge pi each, the maximum possible Chern number is 3/2 -- which is not an integer. This means either: (a) the monopoles have different charges (not all pi), or (b) the 2D parameter space has boundary terms that contribute additional flux, or (c) some monopoles are paired (total charge 2*pi -> C = 1 integer).

From Paper 11 (`researchers/Berry/11_1984_Berry_Curvature_Solids.md`, QH-3), Chern numbers MUST be integers. The resolution determines the topological classification of the eigenvalue flow. If C = 1, there is a single topologically protected mode transition. If C = 0 (monopoles cancel), the topology is trivial. Computing the Chern number requires the 2D parameter extension mentioned in my 19d review (Section 3) and remains a high-priority open computation.

### 5.2 Does Log-Concavity of Eigenvalue Flow Persist Beyond tau=0?

T''(0) > 0 is proven at tau=0. The self-consistency argument requires T''(tau) or delta_T(tau) to maintain a specific sign structure across the physical window [0.15, 0.35]. From the Berry curvature perspective, the log-concavity d^2(ln|lambda_n|)/dtau^2 < 0 that drives T''(0) > 0 is a property of the eigenvalue flow near the round metric. As tau increases and the system moves away from M0 toward M1, the curvature structure may change.

The key question: does the log-concavity persist through M1 (tau~0.10)? The BCS bifurcation at tau~0.20 involves a mode rearrangement that could flip the sign of the curvature contribution. If T''(tau) changes sign between tau=0 and tau=0.15, the self-consistency fixed point cannot exist in the physical window.

This is testable by computing T''(tau) at a few additional tau-values (tau = 0.05, 0.10, 0.15, 0.20) using finite differences on the existing eigenvalue data. The cost is minutes of analysis.

### 5.3 Is the BCS Condensate Adiabatically Connected to the Round Metric?

M0 at tau=0 is the exact degeneracy -- maximum coupling, first-order Kosmann connection. If a BCS condensate forms, it is strongest at tau=0 and weakens as tau increases (coupling scales as e^{-2*tau} from the coupling strength table in CP-4). The condensate at tau=0.30 (FR minimum) is adiabatically connected to the condensate at tau=0 IF there are no phase transitions in between.

M1 at tau~0.10 is the candidate for such a phase transition. The mode rearrangement ((1,0) --> (0,0) gap edge) could be the BCS bifurcation itself -- the point where the condensate order parameter switches from one symmetry sector to another. From Landau theory, such a switch is generically first-order (it breaks a discrete symmetry between the singlet and fundamental channels).

If the M1 transition is first-order, the condensate at tau=0.30 is NOT adiabatically connected to the round metric. It would form as a separate phase, nucleated by the first-order transition at M1. This has implications for the cosmological evolution: the system must tunnel through M1, and the tunneling rate is set by the instanton action.

### 5.4 What Is the Physical Meaning of M0 at Maximum Symmetry?

The exact (0,0)/(1,1) degeneracy at the round metric (tau=0) has a profound physical interpretation. At maximum SU(3) symmetry, the singlet and adjoint sectors are exactly degenerate. Breaking the symmetry (tau > 0) splits them. The singlet drops below the adjoint for 0 < tau < 1.58, then the fundamental drops below both.

From Paper 14 (gauge emergence from eigenstate geometry): the gauge structure of the Standard Model is encoded in the eigenstate manifold of D_K(tau). At tau=0, the exact degeneracy means the gauge structure is enhanced -- the singlet and adjoint are indistinguishable at the spectral level. The Jensen deformation is the symmetry-breaking mechanism that separates them.

This connects to the NCG spectral triple philosophy (Connes Paper 14): geometry IS spectrum. The round metric is the point of maximum spectral degeneracy. The physical geometry (tau_0 > 0) is the geometry where the degeneracy is resolved, and the resolution pattern encodes the Standard Model.

---

## Closing Assessment

Session 21c achieves a rare combination: a clean structural theorem (dual algebraic trap), a compelling positive (T''(0) > 0 escapes via Berry curvature), and a new geometric discovery (three-monopole topology). The session closes ALL perturbative spectral routes at the structural level -- not empirically but mathematically.

From my perspective as a geometric phase specialist, the most significant result is Theorem 2: the derivative escape. This establishes that Berry curvature geometry is the ONLY perturbative quantity that escapes the algebraic traps. Eigenvalue magnitudes are trapped; eigenvalue curvatures are free. This is a deep statement about the geometry of parameter-dependent spectra: the topology (Chern numbers, monopoles) and the curvature (Berry curvature, log-concavity) contain information that no algebraic analysis of eigenvalue magnitudes can access.

**Framework probability**: 39-45%, median 41%. The S_signed structural closure (-5 pp) partially offsets T''(0) COMPELLING (+3 pp from my conservative assessment; I weight the UV-dominance caveat more heavily than the panel). The three-monopole topology is a structural discovery but does not by itself shift the probability -- it organizes existing information rather than producing new evidence. The next decisive computation is delta_T(tau): if the zero-crossing falls in [0.15, 0.35], I would revise upward to 52-58%.

*The algebraic traps are the walls of a canyon carved by representation theory. The perturbative spectral action flows along the canyon floor, unable to rise. T''(0) > 0 is a Berry curvature updraft -- it shows the air currents favor uplift. But whether the landscape has a summit between the canyon walls requires seeing the full curvature map, not just the initial updraft. That map is delta_T(tau).*

---

**Paper references cited:**

| Label | Paper | File |
|:------|:------|:-----|
| Paper 01 | Berry Phase (1984) | `researchers/Berry/01_1984_Berry_Quantal_Phase_Factors.md` |
| Paper 02 | Berry-Tabor (1977) | `researchers/Berry/02_1977_Berry_Tabor_Level_Statistics.md` |
| Paper 03 | Diabolical Points (1984) | `researchers/Berry/03_1984_Berry_Diabolical_Points.md` |
| Paper 04 | Quantum Chaology (1987) | `researchers/Berry/04_1987_Berry_Quantum_Chaology.md` |
| Paper 06 | Maslov Index (1972) | `researchers/Berry/06_1972_Berry_Maslov_Index_Semiclassical.md` |
| Paper 09 | Catastrophe Optics (1980) | `researchers/Berry/09_1980_Berry_Catastrophe_Optics.md` |
| Paper 11 | QHE/Chern (1984) | `researchers/Berry/11_1984_Berry_Curvature_Solids.md` |
| Paper 14 | Synthesis (2009) | `researchers/Berry/14_2009_Berry_Geometric_Quantum_Mechanics.md` |

**Key equations referenced:**

| Label | Equation | Source |
|:------|:---------|:-------|
| BP-4 | B_n = -Im sum_{m!=n} \|<n\|dH/dtau\|m>\|^2 / (E_n - E_m)^2 | Paper 01 |
| DP-3 | gamma(C encircling diab. pt.) = pi (exact) | Paper 03 |
| DP-4 | B_n ~ pi*delta(R - R_0) (monopole curvature) | Paper 03 |
| BT-1 | P(s) = e^{-s} (Poisson, integrable) | Paper 02 |
| QC-4 | K(k) = (1/N)\|sum_n exp(2*pi*i*k*E_n)\|^2 | Paper 04 |
| CO-2 | Cusp: x^4 + lambda*x^2 + mu*x = 0 (codimension 3) | Paper 09 |
| QH-3 | C_n = (1/2*pi) integral Omega d^2k in Z (integer) | Paper 11 |
| GS-6 | Path integral with geometric phase correction | Paper 14 |

**Computational data referenced:**

| File | Description |
|:-----|:-----------|
| `tier0-computation/tier1_dirac_spectrum.py` | Dirac spectrum, 28 irreps, mps=6 |
| `tier0-computation/s21c_V_IR.npz` | V_IR data at multiple N cutoffs |
| `tier0-computation/s21c_neutrino_fine_grid.npz` | Neutrino R(tau) fine grid |
| `tier0-computation/s21c_T_double_prime_result.txt` | T''(0) = +7,969 |
| `tier0-computation/s21c_S_signed.npz` | S_signed monotonically decreasing |
| `tier0-computation/s21c_kk_verify.py` | Preliminary delta_T(tau) code (P1-0) |
