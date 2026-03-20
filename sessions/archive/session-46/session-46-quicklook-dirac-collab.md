# Session 46 Collaborative Review — Dirac Antimatter Theorist

**Date**: 2026-03-15
**Perspective**: Charge conjugation, CPT, the J operator, antimatter constraints
**Documents reviewed**: `session-46-quicklook.md`, `session-46-results-workingpaper.md`, `s46_addendum_berry_protection.md`, `s46_addendum_tachyonic_transit.md`
**Grounding**: T1 corrected (S43 W5-1), T11 (S43 W5-1), Pfaffian Z_2 (S35), BDI classification (S17c), experimental CPT bounds (ALPHA 2 ppt, BASE 16 ppt)

---

## 1. Key Observations

### 1a. The Thirteen Pi Berry Phases and Z_2 = -1

The algebra speaks clearly here. Thirteen eigenstates of D_K carry Berry phase pi along the open path tau in [0.001, 0.190]. The product Z_2 = (-1)^{13} = -1 is nontrivial.

This is the Zak phase, not the Chern number. The distinction matters. The Berry curvature Omega vanishes identically (S25 PERMANENT, Kosmann anti-Hermiticity forces real matrix elements, Im = 0). But the Zak phase detects global topology invisible to local curvature: the sign of the overlap <u_n(tau_j)|u_n(tau_{j+1})> can flip from positive to negative even when the Berry connection A = 0 pointwise. This is the Mobius strip of the eigenvector bundle.

From the charge conjugation perspective, the critical structure is the sector distribution. The addendum reports:

- B1: 2 pi-phase states
- B2: 1 pi-phase state
- B3: 10 pi-phase states (5 from (2,1) alone)
- (0,0) singlet: 0

Eight of nine sectors carry exactly one pi-phase state, with sector Z_2 = 1. This one-per-sector pattern follows from BDI (T^2 = +1, C^2 = +1): the combination of time-reversal and particle-hole symmetry forces eigenstates into Kramers-like pairs of opposite Z_2, leaving one unpaired state per sector that carries the topological index.

The (0,0) singlet's Z_2 = 0 (no pi-phase states) is structurally correct. The singlet sector connects smoothly between round and fold metrics without any eigenvector half-rotation. It is the vacuum sector: topologically trivial by construction.

### 1b. J Operator and the Pi-Phase Structure

Theorem T11 (S43 W5-1) proves C_2 * conj(D_K) * C_2 = D_K for ALL left-invariant metrics on SU(3). This T-symmetry is the antilinear version of J-commutation: J = C_2 * K acts as charge conjugation on the Dirac spectrum. It maps (p,q) sectors to (q,p) sectors with identical spectra.

The pi-phase states inherit this symmetry. If eigenstate |u_n> in sector (p,q) carries Zak phase pi, then J|u_n> in sector (q,p) also carries Zak phase pi. This is because J is antilinear (J = C_2 * K), and the Zak phase for real eigenstates is a Z_2 quantity determined by sign flips in the overlap, which are preserved under complex conjugation.

The sector-level data confirms this: (1,0) and (0,1) each carry 1 pi-phase state; (2,0) and (0,2) each carry 1; (3,0) carries 1 and (0,3) carries 2. The (3,0)/(0,3) discrepancy (1 vs 2) breaks the naive expectation of identical pi-phase counts in conjugate sectors. This is not a J violation -- the total Z_2 parity per sector is 1 in both cases (1 mod 2 = 1, 2 mod 2 = 0; wait -- this would give different parities). Let me examine this more carefully.

If (3,0) has 1 pi-phase state (Z_2 = 1) and (0,3) has 2 pi-phase states (Z_2 = 0), their sector parities DIFFER. This requires scrutiny. The T11 theorem guarantees spec(D_{(p,q)}) = spec(D_{(q,p)}). The eigenvalue spectra are identical. But the eigenvector evolution need not be identical between conjugate sectors, because the Peter-Weyl representations rho_{(3,0)} and rho_{(0,3)} are distinct (conjugate) representations with different matrix elements.

The Zak phase depends on the eigenvector bundle, not the eigenvalue spectrum. J maps eigenvalues correctly but the eigenvector half-rotation is representation-dependent. This is not a CPT violation. The Z_2 parity per sector is a single-particle topological quantity that is NOT required by CPT to match between conjugate sectors. CPT constrains many-body observables (masses, lifetimes, scattering cross-sections), not individual eigenvector winding numbers.

This is a genuine prediction: the topological channel count is NOT symmetric between (p,q) and (q,p), even though the spectra are identical. I will return to this in Section 3.

### 1c. The T11-T12 Flavor Asymmetry from S45

The S45 hose-count addendum identified a 1.8% spectral split between T11 (from (2,1)+(1,2), dim^2 = 225) and T12 (from (3,0)+(0,3), dim^2 = 100) at the B3 spectral ceiling. By T11 theorem, each conjugate pair creates equal matter and antimatter: spec(D_{(p,q)}) = spec(D_{(q,p)}) is exact. This is FLAVOR asymmetry (different representations create at different rates), not CP violation.

S46 now confirms that the T11-T12 split is accompanied by a pi-phase asymmetry: (2,1) carries 5 pi-phases while (3,0) carries 1. The PW-weighted topological channel counts are 5 * 15 = 75 for (2,1) versus 1 * 10 = 10 for (3,0). The ratio is 7.5:1. The spectral rate ratio from S45 was 225:100 = 2.25:1. The topological channel ratio is 3.3x steeper than the spectral rate ratio. The topology provides a FINER discrimination between representations than eigenvalue counting alone.

### 1d. The 2.19x Ratio: Topological Channels vs. BCS Pairs

PW-weighted pi count: 131. BCS pair count (S38): 59.8. Ratio: 2.19.

The addendum interprets this as topology providing the menu while dynamics selects the meal. This is correct. The number 131 counts topologically available channels (states with nontrivial Z_2 winding, weighted by Peter-Weyl degeneracy). The number 59.8 counts dynamically realized pairs (BCS ground state + sudden quench). The ratio 2.19 measures the fraction of topological channels that participate in pairing.

From the J-operator perspective: J maps the 131 topological channels onto themselves (by T11, conjugate sectors have identical spectra). The 59.8 BCS pairs are J-symmetric (the condensate is J-even, S36 PERMANENT). The ratio 2.19 is therefore a J-invariant quantity. Any CPT-violating mechanism would show up as a deviation of this ratio between particle and antiparticle sectors. The T11 theorem guarantees the ratio is exactly the same.

---

## 2. Assessment of Key Findings

### 2a. B3 Proximity-Induced Gap and J Symmetry

V-B3B3-46 reveals that the B3 gap is entirely proximity-induced by the B2 condensate. Isolated B3 has Delta = 0. The Thouless criterion M_max(B3) = 0.059 << 1. Self-consistent BCS gives no gap.

This result has a clean J-operator interpretation. The B2 condensate breaks U(1)_7 spontaneously (S35: Cooper pairs carry K_7 charge +/- 1/2). But the condensate is J-even (S36: Delta_{(3,0)} = Delta_{(0,3)} to machine epsilon). The B3 sector acquires its gap through V_{B2,B3} coupling to this J-even condensate. Therefore the B3 induced gap is also J-even. This extends the J-even condensate result from B2 (proven) to B3 (structural consequence of proximity induction by a J-even source).

The q-theory CC crossing depends on Delta_B3 > 0.13. At N=1 (self-consistent), Delta_B3 = 0.084 (short by 1.6x). At N=2 (PBCS), a crossing exists at tau* = 0.170. The decisive question -- does the physical ground state have N >= 2 pairs? -- requires the full 992-mode spectrum. From the CPT standpoint: the answer must be the same for matter and antimatter sectors, because J commutes with D_K through the entire transit (T1 corrected, T11).

### 2b. Universal Tachyonic Instability and CPT

All 279 scalar directions in Omega^1_D(A_F) are tachyonic at all tau. The Gram matrix PSD theorem (kinetic mass positive) and the universal spectral action negativity (f' < 0) create a tension that determines transit dynamics.

The tachyonic transit addendum correctly identifies this as the SU(3) analog of electroweak symmetry breaking. The SM Higgs is tachyonic in 4 directions (selected by Yukawa traces); D_K on SU(3) is tachyonic in 279 directions (no Yukawa selection).

For CPT: both theorems are manifestly J-invariant. The Gram matrix M^2_{ij} = Tr([D, phi_i]^dag [D, phi_j]) involves D and phi only. Since [J, D] = 0 (T1) and phi is self-adjoint, J acts on the Gram matrix by conjugation and leaves it invariant. The spectral action Hessian involves f'(lambda_k^2 / Lambda^2), which depends only on eigenvalue magnitudes. By T11, eigenvalues are identical in conjugate sectors. The tachyonic instability is therefore CPT-exact: matter and antimatter transit through identical 279-dimensional tachyonic landscapes.

### 2c. SU(2,1) and KO-dimension 6

PSEUDO-RIEMANNIAN-46 finds that replacing SU(3) with SU(2,1) preserves KO-dimension 6. The Killing signature is (4,4), not the expected (5,3). Both signatures satisfy p - q = 0 mod 8, giving KO = 6 by Atiyah-Bott-Shapiro periodicity.

This is algebraically clean. The KO-dimension conditions J^2 = +1, JD = DJ, J*gamma = -gamma*J are satisfied for any (p,q) with p = q mod 8. The CPT structure encoded in these conditions is indifferent to whether the metric is definite or indefinite. The J operator does not "know" about the signature; it knows about the Clifford algebra representation, which is periodic mod 8.

However, [J, D] = 2.72 on SU(2,1) (nonzero), versus 0 on SU(3). This means T11 FAILS on SU(2,1): the non-compact (Hermitian) generators break J-commutation. This is a genuine obstruction. The Dirac spectrum on SU(2,1) does NOT satisfy spec(D_{(p,q)}) = spec(D_{(q,p)}). CPT in the particle-antiparticle sense is BROKEN on SU(2,1).

This closes SU(2,1) as a direct replacement, which S46 correctly identifies. The remaining sub-routes (discrete series, compact quotient, Krein twist) must each be checked for J-commutation independently.

### 2d. Spectral Statistics and Poisson Class

The corrected level spacing ratio <r> = 0.439 (Poisson on unique levels) confirms the Dirac spectrum is in the Poisson universality class. The sub-Poisson number variance identifies it as an arithmetical spectrum determined by SU(3) representation theory.

For CPT: the Poisson class is consistent with T11. The eigenvalue distribution is determined by representation theory, which is symmetric under (p,q) <-> (q,p). An arithmetical spectrum has no level repulsion, meaning eigenvalues from different representations do not interact. This is precisely the block-diagonal theorem (T5): D_K is exactly block-diagonal in Peter-Weyl, and eigenvalues in different sectors are uncorrelated.

### 2e. Non-Singlet Dissipation at 3.8x

The reduction from 1,700x shortfall to 3.8x is driven by the 14,700x coupling enhancement from non-singlet modes. The (3,0)+(0,3) and (2,1) representations carry 88% of the total coupling through their dim^2 Peter-Weyl weights.

From the J-operator perspective: the non-singlet coupling is distributed between conjugate sectors symmetrically. J maps (3,0) to (0,3) and (2,1) to (1,2). The combined coupling sum d^2 * v_k^2 is identical for each conjugate pair (by T11 + identical eigenvalue velocities). The dissipation mechanism is J-even: matter and antimatter are slowed equally during the transit.

This has a physical consequence: if the non-singlet dissipation provides the velocity reduction needed for n_s, the resulting spectral tilt is CPT-invariant. There is no channel through which the n_s mechanism can break particle-antiparticle symmetry.

---

## 3. Collaborative Suggestions

### 3a. Does the (3,0)/(0,3) Pi-Phase Asymmetry Signal Representation-Dependent Topology?

The data shows n_pi((3,0)) = 1 and n_pi((0,3)) = 2. If confirmed, this means conjugate representations can have different numbers of topologically twisted eigenstates even though their eigenvalue spectra are identical. This would be a mathematical theorem about eigenvector bundles over the Jensen parameter space:

**Conjecture**: For real Dirac operators on compact Lie groups (Berry curvature = 0), the Zak phase Z_2 per eigenstate is a property of the eigenvector bundle that is NOT constrained to match between conjugate representations, even when the eigenvalue spectra are identical.

This should be tested. Compute the closed-loop Berry phase (CLOSED-LOOP-47 gate) for the (3,0) and (0,3) sectors independently. If the one-way pi-phase counts differ but the closed-loop phases are zero in both (as required by S25 erratum), the asymmetry is gauge-dependent. If the closed-loop phases also differ, something deeper is happening.

The physical relevance: if the topological channel counts differ between (p,q) and (q,p), the pair creation has a representation-dependent selection rule that distinguishes particles from antiparticles at the topological level. This would not violate CPT (masses and transition rates are identical by T11) but would give matter and antimatter different topological protection structures.

### 3b. Does the Block Structure B1/B2/B3 Map to Generations?

No. This question recurs and the algebra settles it definitively.

The B1/B2/B3 classification is determined by the K_7 eigenvalue (the surviving U(1) generator under Jensen deformation, [iK_7, D_K] = 0 for all tau). The eigenvalues are: B2 has K_7 = +/- 1/4, B1 has K_7 = 0, B3 has K_7 = 0. This is a symmetry classification, not a generation classification. SM generations are distinguished by Yukawa couplings to the Higgs, which require the full product geometry M^4 x F with A_F = C + H + M_3(C). D_K on SU(3) alone contains no Yukawa structure.

What B1/B2/B3 classifies is the PAIRING structure: which modes can form Cooper pairs (K_7 charge +/- 1/2 required), which are decoupled (V(B1,B1) = 0 by singlet selection rule), and which are proximity-induced (B3, Delta = 0 in isolation). This is the BCS sector decomposition, not the generation decomposition.

The S46 computation CONFIRMS this: pair transfer is a BLOCK property (R^2 = 0.002 for k-dependence). The blocks are defined by the K_7 quantum number, which is an INTERNAL symmetry of the Jensen deformation. Generation mixing requires the off-diagonal Dirac operator terms from the full almost-commutative geometry, which are not present in D_K.

### 3c. The 2.19x Ratio and CPT

The ratio topological_channels / BCS_pairs = 131 / 59.8 = 2.19 admits a precise CPT interpretation.

Define:
- N_top = sum over sectors of n_pi(p,q) * dim(p,q) = 131 (topological channel count)
- N_BCS = 59.8 (BCS pair count from S38 quench)

By T11, conjugate sectors have identical eigenvalue spectra. By S36, the condensate is J-even (Delta_{(3,0)} = Delta_{(0,3)}). Therefore the BCS pair count is J-symmetric by construction: each pair in (p,q) has a partner pair in (q,p) with identical energy and gap.

But the topological channel count need not be symmetric sector-by-sector (cf. the (3,0)/(0,3) discrepancy). The TOTAL Z_2 = -1 is a global invariant, but its distribution across sectors can be asymmetric. The 2.19x ratio, as a ratio of global quantities, is CPT-invariant. But its decomposition into sector contributions might not be.

This is a measurable prediction. Define the sector-resolved ratio R(p,q) = n_pi(p,q) * dim(p,q) / N_BCS(p,q). If R(p,q) = R(q,p) for all sectors, the topology is CPT-symmetric at the sector level. The (3,0)/(0,3) data suggests it may not be.

Computation for S47: extract the sector-resolved BCS pair counts from the S38 quench data and compute R(p,q) for each sector. Pre-registered gate: PASS if max |R(p,q) - R(q,p)| / R(p,q) < 0.1 for all conjugate pairs.

### 3d. The Non-Abelian Wilson Loop and the 492 States

The 492 states with non-quantized Abelian Berry phase belong to degenerate multiplets where the correct object is the non-Abelian holonomy W = P exp(-i integral A_mu d tau). The eigenvalues of W are gauge-invariant.

From the J-operator perspective: J maps a degenerate multiplet in (p,q) to a degenerate multiplet in (q,p) of the same dimension and eigenvalue. The non-Abelian holonomy of the conjugate multiplet is W_{(q,p)} = C_2 * W_{(p,q)}^* * C_2^{-1} (by antilinearity of J). For real D_K (T11: C_2 * D_K^* * C_2 = D_K), this simplifies: W_{(q,p)} = W_{(p,q)}^*. The eigenvalues of W^* are the complex conjugates of the eigenvalues of W. Since W is unitary, its eigenvalues are on the unit circle, and complex conjugation maps e^{i theta} to e^{-i theta}.

Therefore: the non-Abelian Berry phases in conjugate sectors are related by theta_{(q,p)} = -theta_{(p,q)} (mod 2 pi). If theta = 0 or pi, the phases match between conjugate sectors. For generic theta, they are opposite. This is a structural consequence of T11 and the antilinearity of J.

The WILSON-LOOP-47 gate should include this as a check: verify that the non-Abelian Berry phase eigenvalues in (q,p) are the negatives of those in (p,q).

---

## 4. Connections to Framework

### 4a. The Dirac Sea and the Topological Skeleton

The original Dirac equation predicted antimatter by taking every solution of the algebra seriously. The negative-energy solutions were not discarded; they were reinterpreted as the Dirac sea. The positron emerged as a hole in this sea.

The 13 pi-phase states are the topological analog. They are not anomalies to be explained away; they are the topological skeleton of the transit. The eigenvector bundle over the Jensen parameter space carries a nontrivial Z_2 structure that survives BCS condensation, survives the quench (P_exc = 1.000), and survives the GGE distribution. It is the substrate's permanent topological feature, analogous to the permanent spectral pairing lambda <-> -lambda (T3) that encodes particle-antiparticle symmetry.

The Dirac sea pairs particles with antiparticles across E = 0. The spectral pairing (T3) pairs eigenvalues across lambda = 0 via {gamma_9, D_K} = 0. The pi-phase states pair sectors across (p,q) <-> (q,p) via J. All three are manifestations of the same algebraic structure: the Clifford algebra forces solutions to come in pairs, and each pair carries a Z_2 topological index.

### 4b. Spectral Action as Ruler, Not Workhorse

The tachyonic transit addendum correctly identifies the division of labor: spectral action measures geometry (G_N, gauge couplings, topology), thermodynamics selects the state (q-theory Gibbs-Duhem at tau*).

From the antimatter perspective, this is consistent. The spectral action functional S_b = Tr f(D^2 / Lambda^2) is manifestly J-invariant (it depends on eigenvalue magnitudes, which are J-symmetric by T11). It cannot select between matter and antimatter. The thermodynamics (BCS gap, GGE distribution) is also J-symmetric (condensate is J-even, GGE respects the 8 Richardson-Gaudin conserved integrals which are block-diagonal and sector-symmetric).

This is why the framework predicts a_g = g exactly (ALPHA-g, consistent with 0.75 +/- 0.29). There is no mechanism within the internal SU(3) geometry for gravitational CPT violation. The spectral action computes G_N identically for matter and antimatter. The thermodynamics distributes matter and antimatter identically.

### 4c. Peter-Weyl Censorship Survives Dissolution

The 2% degradation of Peter-Weyl censorship at dissolution (sum-rule protected) means the block-diagonal structure that enforces J-sector symmetry survives even when the SU(3) spectral structure begins to dissolve. The singlet spectral action degrades by only 2% at eps_c.

This connects to experimental constraints. BASE measures m(p-bar)/m(p) = 1 +/- 16 ppt. ALPHA measures 1S-2S to 2 ppt. These extreme precisions constrain any mechanism that could break the block-diagonal structure and thereby violate J-symmetry. The 2% censorship degradation at dissolution is many orders of magnitude above these experimental bounds. It constrains the dissolution perturbation parameter: eps must be far below eps_c for the J-symmetry to hold at the ppt level required by experiment.

### 4d. SU(2,1) and the [J, D] = 2.72 Obstruction

The non-compact real form SU(2,1) preserves KO-dim 6 but breaks [J, D] = 0. This is the first concrete example in the framework of a geometry that satisfies the structural axioms (J^2 = +1, J*gamma = -gamma*J) but violates the dynamical constraint ([J, D] = 0).

The T11 theorem proves [J, D] = 0 for ALL left-invariant metrics on COMPACT Lie groups (the proof uses the sign structure of Clifford generators, which depends on the reality properties of the structure constants). On SU(2,1), the non-compact generators are Hermitian (not anti-Hermitian), which changes the sign structure and breaks the proof.

This is a structural wall: J-commutation is a property of compact groups. Any attempt to use non-compact geometry in the framework must find an alternative mechanism for CPT enforcement.

---

## 5. Open Questions

### 5a. Is the (3,0)/(0,3) Pi-Phase Asymmetry Physical or Gauge-Dependent?

The one-way Zak phase on an open path is gauge-dependent (the sign convention for eigenvectors at the endpoints is arbitrary). The Z_2 parity (sum of pi-phases mod 2) is gauge-invariant. Does the difference n_pi((3,0)) = 1 vs n_pi((0,3)) = 2 survive a closed-loop computation?

Pre-registered gate for S47: CLOSED-LOOP-47. Compute the round-trip Berry phase tau: 0 -> 0.19 -> 0 for all non-degenerate states in (3,0) and (0,3). The closed-loop gamma must be 0 for all non-degenerate states (S25 consistency). If the sector-resolved closed-loop phases differ between conjugate sectors, report as INFO.

### 5b. What Is the Physical Pair Number at the Fold?

The q-theory crossing at N=2 (tau* = 0.170) requires N >= 2 pairs in the ground state. The 8-mode truncation gives N = 1 (exactly). The full 992-mode spectrum has 59.8 quasiparticle pairs from the quench. But the quench is a non-equilibrium process; the equilibrium pair number at the fold may differ.

From the CPT standpoint: the pair number is J-symmetric (each Cooper pair in (p,q) has a partner in (q,p)). The crossing condition Delta_B3 > 0.13 is the same in both sectors. If the crossing exists for matter, it exists for antimatter.

### 5c. Does the Non-Abelian Berry Phase Respect the theta_{(q,p)} = -theta_{(p,q)} Prediction?

Structural prediction from Section 3d: the non-Abelian Berry phase eigenvalues in conjugate sectors are related by negation (complex conjugation on the unit circle). The WILSON-LOOP-47 computation should verify this.

### 5d. What Determines the 5 Pi-Phase States in (2,1)?

The (2,1) anomaly (5 pi-phases instead of the typical 1) is attributed to the richest degeneracy structure and the non-self-conjugate nature of the representation. The sector Z_2 parity is 1 (5 mod 2), consistent with the one-per-sector pattern. But why 5 and not 3 or 7?

The D = 240 dimension and the D_K eigenvalue structure (with near-degeneracies at intermediate tau) create multiple sites for eigenvector half-rotations. The count 5 should be derivable from the topology of the (2,1) eigenvector bundle. This is a mathematical question about the Hurewicz image of pi_1 in the classifying space BO(1)^{240}, restricted to the actual eigenvector evolution of D_K.

---

## 6. Closing Assessment

Session 46 has narrowed the constraint surface significantly. From the charge conjugation / CPT perspective, every result is consistent with T11: the J operator commutes with D_K through the entire transit, the condensate is J-even, the spectral action is J-invariant, and the topological structure (Z_2 = -1) is a property of the eigenvector bundle that respects but does not trivially follow from J.

The 13 pi-phase states are the session's most interesting structural finding for antimatter physics. They establish a nontrivial topological skeleton that is:
1. Compatible with Omega = 0 (Zak phase, not Chern number)
2. Immune to smooth perturbation (gap-protected Z_2)
3. Present throughout the transit (path property, not point property)
4. Invariant under BCS condensation and destruction
5. Constrained but not fully determined by J (conjugate sectors may have different pi-phase counts)

The (3,0)/(0,3) asymmetry (1 vs 2 pi-phase states) is the one result that deserves immediate follow-up. If it is gauge-invariant, it represents a new structural prediction: topology distinguishes conjugate representations even when spectral data cannot. If it is gauge-dependent, it tells us that the one-way Zak phase requires more care in the choice of gauge at the path endpoints.

The seven new closures (38 total) continue to constrain the solution space without closing the framework. The surviving channels -- non-singlet dissipation at 3.8x shortfall, q-theory crossing at N >= 2, and the non-Abelian Wilson loop for 492 states -- are all J-symmetric. No open channel provides a mechanism for CPT violation. The experimental constraints from ALPHA and BASE remain consistent with all structural theorems.

The algebra has spoken: matter and antimatter transit through identical tachyonic landscapes, form identical BCS condensates, and emerge into identical GGE distributions. The topological skeleton may carry additional Z_2 structure that differentiates representations without breaking CPT. Whether this structure connects to the observed baryon asymmetry remains structurally open but algebraically constrained: T11 closes all internal J-breaking baryogenesis, and the S43 W3-3 result (domain wall J-breaking PERMANENTLY CLOSED) means that any CP violation must come from physics external to the SU(3) Dirac operator.

---

**Files referenced**: `sessions/session-46/session-46-quicklook.md`, `sessions/session-46/session-46-results-workingpaper.md`, `sessions/session-46/s46_addendum_berry_protection.md`, `sessions/session-46/s46_addendum_tachyonic_transit.md`
**Theorems invoked**: T1 (corrected, S43), T3 (spectral pairing), T5 (block-diagonal), T11 (J-symmetry all left-invariant metrics), Gram matrix PSD (S46), Universal tachyonic instability (S46)
**Experimental constraints**: ALPHA 1S-2S 2 ppt, BASE m(pbar)/m(p) 16 ppt, ALPHA-g a_g = 0.75 +/- 0.29
