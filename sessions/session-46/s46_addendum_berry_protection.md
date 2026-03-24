# Addendum: The Thirteen Pi Phases -- Topological Skeleton of the Transit

**Author**: Berry Geometric Phase Theorist
**Session**: 46, addendum to W4-2 (BAND-INVERSION-BERRY-46)
**Date**: 2026-03-15
**Status**: INTERPRETIVE + STRUCTURAL. Reconciles S25 ERRATUM with S46 result. No new computation.

---

## 1. Reconciliation: Zero Berry Curvature Does Not Mean Zero Zak Phase

The central geometric paradox of this framework -- large quantum metric (g = 982.5) with identically vanishing Berry curvature (Permanent Result #7, S25) -- acquires a new dimension with the S46 result. Thirteen eigenstates carry gamma = pi Berry phase along the open path tau = 0.001 to tau = 0.190. This appears to contradict the S25 ERRATUM, which established Omega = 0 identically, Berry connection A = 0, Wilson loop trivial, Chern numbers = 0.

It does not contradict it. The two results measure geometrically distinct objects.

The S25 result addresses the Berry curvature 2-form Omega_n = -Im sum_{m != n} (<n|dH|m> x <m|dH|n>) / (E_n - E_m)^2, which is the INFINITESIMAL measure of eigenstate rotation. For real eigenstates (guaranteed by Kosmann anti-Hermiticity of K_a on any compact Lie group with left-invariant metric), all matrix elements <n|dH/dtau|m> are real. The imaginary part vanishes identically. The Berry connection A_n(tau) = i <n(tau)|d/dtau|n(tau)> = 0 pointwise. Integrating zero gives zero: any CLOSED loop in the one-dimensional tau-parameter space gives gamma = 0.

The S46 result computes something different: the discrete Pancharatnam phase gamma_n = -Im sum_j log <u_n(tau_j)|u_n(tau_{j+1})> along an OPEN path. For real eigenstates, each overlap <u(j)|u(j+1)> is real. The log of a positive real number has Im = 0. The log of a NEGATIVE real number has Im = pi. The question becomes: does the sign of the overlap ever flip?

This is the Zak phase (Berry 1984, Zak 1989). In band theory, the Zak phase is the Berry phase accumulated across the Brillouin zone -- an open path with identified endpoints. It is quantized to 0 or pi for systems with inversion symmetry (real Bloch functions). The Zak phase is a Z_2 invariant: it counts the parity of the number of sign flips in the eigenvector overlap as the parameter traverses the path. It can be pi even when the Berry curvature is identically zero at every point, because it detects GLOBAL topology (the Mobius twist) rather than local curvature.

The geometric picture: the eigenvector bundle over the tau interval [0.001, 0.190] is a real line bundle (each fiber is a real 1D subspace of R^D spanned by a real eigenvector). A real line bundle over an interval is trivial -- it can always be trivialized by a smooth choice of sign. But the CANONICAL sign choice from eigh (which diagonalizes at each tau independently) may not be smooth. The gauge-fixing procedure in s46_berry_phase.py (maximize overlap at each step) constructs the smooth gauge. A pi phase then means: the smooth gauge-fixed eigenvector at tau_max has OPPOSITE sign from the canonical eigenvector. The eigenvector has rotated through a half-turn in its eigenspace while remaining real throughout.

This is precisely the Mobius strip: a real line bundle over an interval that, when the endpoints are identified, would be non-orientable. The bundle over the open interval is trivial, but the TRANSITION FUNCTION between the canonical gauge and the smooth gauge has a sign flip. This is the Z_2 obstruction.

**Structural theorem (reconciliation)**: Berry curvature Omega = 0 (S25, PERMANENT) and Zak phase gamma = pi (S46, 13 states) are simultaneously valid. The first is a statement about the local differential geometry of the eigenvector bundle. The second is a statement about the global topology of the bundle over the transit interval. The Zak phase detects a Z_2 invariant invisible to the curvature.

---

## 2. What Pi Means Physically: The Eigenvector Half-Rotation

A state with gamma = pi has undergone the following evolution during the transit tau: 0.001 -> 0.190:

The eigenvector |u_n(tau)> is real at every tau (Kosmann anti-Hermiticity guarantees this). As tau increases, the eigenvector rotates smoothly in D-dimensional real space. At some point(s) along the path, the projection of the evolved eigenvector onto its initial direction passes through zero -- the eigenvector has rotated perpendicular to its starting direction -- and continues rotating until, at tau = 0.190, it points in the OPPOSITE direction from where it started.

This is not a level crossing. The eigenvalue ordering is preserved (zero band inversions in every sector). The eigenvector rotates while the eigenvalue stays in place. The eigenvalue is the shadow on the wall; the eigenvector is the object casting it. The shadow never crosses another shadow, but the object has turned upside down.

In Berry's original 1984 paper (Paper 01, Section on diabolical points), the pi phase arises when a closed loop encircles a degeneracy in parameter space. The degeneracy acts as a monopole source of Berry flux, and the enclosed flux is pi. Here, we have an OPEN path -- no loop, no enclosed area. But the mechanism is related: the tau path passes BETWEEN two degeneracies (the round-metric degeneracies at tau = 0 and the fold degeneracies at tau ~ 0.190), and the eigenvector must resolve the conflicting symmetry structures at these two endpoints. The half-rotation is the price of this resolution.

In condensed matter, the direct analog is the Zak phase of a 1D band. Rice and Mele (1982) showed that a 1D insulator with inversion symmetry has Zak phase quantized to 0 or pi, and the pi value signals a topologically nontrivial band -- one that cannot be smoothly deformed to an atomic limit without closing the gap. The 13 pi-phase states on SU(3) are the internal-space analog: these are eigenstates of D_K whose eigenvector structure cannot be smoothly deformed to the round-metric structure without passing through a degeneracy.

---

## 3. Why One Per Sector (Mostly): The BDI Z_2 Invariant

Eight of nine sectors carry exactly one pi-phase state. The (0,0) singlet carries zero; the (2,1) sector carries five. The pattern of "one per sector" has a structural explanation in the BDI symmetry classification (S17c: T^2 = +1, C^2 = +1, AZ class BDI).

In the BDI class, the topological invariant over a 1D parameter space is Z (the winding number). Session 36 computed nu = 0 (trivial winding, WIND-36). But the winding number is a MANY-BODY invariant of the BCS Hamiltonian at fixed chemical potential mu. The per-eigenstate Zak phase is a SINGLE-PARTICLE Z_2 invariant -- a coarser diagnostic that counts whether each individual eigenstate has a topological twist.

The BDI classification guarantees that each non-degenerate eigenstate carries a well-defined Z_2 index (the parity of its Zak phase). In a sector with D non-degenerate eigenstates, each carries Z_2 = 0 or 1 independently. The total Z_2 of the sector (sum mod 2) is the sector's topological parity.

For the 8 sectors with exactly 1 pi-phase state: sector Z_2 = 1. Each sector has an ODD number of topologically twisted eigenstates. This is the Kramers-like theorem for BDI: the combination of time-reversal and particle-hole symmetry forces the eigenstates to come in pairs of opposite Z_2, except for one unpaired state that carries the topological index. That unpaired state is the pi-phase state.

For (0,0) with zero pi-phase states: sector Z_2 = 0. The singlet sector is topologically trivial. This is consistent with the singlet being the "vacuum" sector -- it has no topological twist because the round-metric structure and the fold structure are smoothly connected within this sector.

For (2,1) with five pi-phase states: sector Z_2 = 1 (5 mod 2 = 1). The total parity is still odd, consistent with the pattern. But five individual twists, rather than one, indicates a richer internal structure. The (2,1) sector is the largest (D = 240) and has the most near-degeneracies. Multiple eigenstates undergo half-rotations because multiple degeneracy pairs are being resolved simultaneously. The Z_2 parity is preserved (odd), but the distribution is more complex.

---

## 4. The Topological Channel Count and the 2.19x Ratio

The PW-weighted pi count is 131. The BCS pair count is 59.8. The ratio is 2.19.

The geometric interpretation: each pi-phase state in sector (p,q) represents a topologically available channel for pair creation. The Peter-Weyl theorem says the sector appears dim(p,q) times in L^2(SU(3)). So the total number of topologically available channels is sum_sectors n_pi(p,q) * dim(p,q) = 131.

Not all channels participate in BCS pairing. The block-diagonal theorem (S22b) restricts pairing to within sectors. The K_7 selection rules (S34: Cooper pairs carry K_7 charge +/- 1/2) further restrict which states can pair. The V(B1,B1) = 0 selection rule (Trap 1, S34) eliminates B1 pairing entirely. The B3 sector has 10 pi-phase states but only those with compatible K_7 charges can form Cooper pairs.

The 2.19x ratio is therefore the ratio of TOPOLOGICALLY AVAILABLE to DYNAMICALLY REALIZED channels. The topology provides the menu (131 channels). The dynamics (BCS selection rules, K_7 quantum numbers, Schur orthogonality) select the meal (59.8 pairs). The menu is always larger than the meal. The ratio 2.19 measures the selectivity of the BCS pairing relative to the topological availability.

This is a known phenomenon in condensed matter: in a topological insulator, the bulk topological invariant (Chern number) counts the number of topologically protected edge modes, but the number of CONDUCTING edge channels may be smaller due to disorder, interactions, or symmetry-breaking. The topological count is an upper bound on the dynamical count. Here, 131 >= 59.8.

---

## 5. Self-Protection: The Substrate's Topological Skeleton

The 13 pi-phase states (131 PW-weighted) have the following properties:

**(a) Immune to smooth perturbation.** The Zak phase is a Z_2 topological invariant. It can change only if a gap closes (two eigenvalues become degenerate). Along the Jensen line, the spectral flow theorem (Permanent Result #10: lambda^2 >= R_K/4 >= 3 > 0) guarantees no eigenvalue crosses zero, and the zero band inversions (S46) confirm no eigenvalues cross each other. The pi phases are LOCKED by the spectral gap.

**(b) Present throughout the transit.** The pi phase is a property of the eigenvector bundle over the ENTIRE interval [0.001, 0.190], not a property at any single tau. It is the integrated rotation accumulated along the path. Removing any interior portion of the path and reconnecting smoothly cannot change the Z_2 index (homotopy invariance). The topological structure is carried by the path as a whole.

**(c) Sector-universal.** One pi-phase state per sector (8 of 9 sectors, Z_2 = 1) regardless of sector size. The (1,0) sector with D = 48 and the (3,0) sector with D = 160 each contribute exactly one. The topological index per sector is a PROPERTY OF THE SECTOR, not of its size. This is the fiber bundle at work: each sector is a fiber over the tau base, and the fiber's topology is intrinsic.

**(d) Invariant under BCS condensation and destruction.** The Zak phase is a single-particle property of the Dirac operator's eigenstates. BCS pairing is a many-body phenomenon in Fock space. The single-particle topological structure survives because the BDI classification (T^2 = +1) is preserved by the BCS Hamiltonian -- the particle-hole symmetry that quantizes the Zak phase is the SAME symmetry that classifies the BCS state. The condensate forms within the topological framework; it does not alter the framework.

**(e) Survive the quench.** The sudden quench at the fold (P_exc = 1.000, S38) destroys the BCS condensate. But the single-particle eigenstates and their Zak phases are properties of D_K(tau), not of the many-body state. Post-quench, the GGE distributes occupation across eigenstates according to the 8 Richardson-Gaudin conserved integrals (S38 PERMANENT). The pi-phase states remain topologically distinct within the GGE -- their Z_2 index is a spectral property, unaffected by the occupation distribution.

These five properties identify the 13 pi-phase states as the TOPOLOGICAL SKELETON of the transit. They are the features of the eigenvector bundle that cannot be destroyed by any smooth process -- not by the Jensen deformation, not by BCS pairing, not by condensate destruction, not by the quench. They are permanent structural features of D_K on SU(3).

---

## 6. Connection to Spectral Flow and Homotopy of SU(3)

The total Zak phase summed over all non-degenerate eigenstates is 13 * pi = 13pi. The 492 states with non-quantized phases (states in degenerate multiplets where the Abelian Zak phase is ill-defined) contribute an unknown amount that can only be resolved by computing the non-Abelian Wilson loop (open gate, S46 item 1).

For the 13 non-degenerate pi-phase states, the sum 13pi is odd in units of pi. This means the total Z_2 parity of the non-degenerate sector is 1 (nontrivial). Is this related to a topological invariant of SU(3)?

The homotopy groups of SU(3) are: pi_1(SU(3)) = 0, pi_2(SU(3)) = 0, pi_3(SU(3)) = Z, pi_4(SU(3)) = 0, pi_5(SU(3)) = Z, pi_8(SU(3)) = Z_3. The pi_3 = Z is the instanton number; the pi_5 = Z is the Wess-Zumino-Witten winding; the pi_8 = Z_3 relates to the triality partition (Z_3 = (p - q) mod 3).

The number 13 does not directly match any of these. But the SECTOR-RESOLVED structure is suggestive. By BCS branch: B1 carries 2 pi-phases, B2 carries 1, B3 carries 10. Total: 2 + 1 + 10 = 13. By triality:

- Z_3 = 0 sectors: (0,0), (1,1), (3,0), (0,3). Pi counts: 0, 1, 1, 2. Total: 4.
- Z_3 = 1 sectors: (1,0), (2,0), (2,1). Pi counts: 1, 1, 5. Total: 7.
- Z_3 = 2 sectors: (0,1), (0,2). Pi counts: 1, 1. Total: 2.

The distribution 4, 7, 2 does not exhibit a simple pattern. The (2,1) anomaly (5 pi-phases) dominates the Z_3 = 1 class. If the (2,1) sector had 1 pi-phase like most sectors, the distribution would be 4, 3, 2 -- closer to uniform but still not symmetric.

The relation to particle counting is also inconclusive. The SM has 15 Weyl fermions per generation (6 quarks x 2 chiralities + 3 charged leptons + 3 neutrinos, counting L and R separately). Or 16 if the right-handed neutrino is included -- which matches dim(spinor) = 16 = C^16, the NCG input (S7-8). The number 13 is neither 15 nor 16. It is 16 - 3, which would correspond to removing one SU(2)_L triplet (three components) from the spinor. Whether this is meaningful or numerological cannot be determined without the non-Abelian Wilson loop computation for the 492 remaining states.

---

## 7. The (2,1) Anomaly

The (2,1) sector has 5 pi-phase states where most sectors have 1. The (2,1) representation has dim = 15 (the adjoint of SU(3) has dim = 8, but (2,1) is a different representation with 15 components). It is the largest representation at truncation p + q <= 3, and belongs to the B3 branch.

Three structural factors may explain the multiplicity:

First, the (2,1) sector has the richest degeneracy structure at the round metric. With D = 240, the number of distinct eigenvalues at tau = 0 is much smaller than 240 (high degeneracy). As tau increases, these degeneracies split. Each splitting event creates a pair of states that must resolve their relative orientation -- and each such resolution is a potential site for a pi-phase flip. More splittings means more potential flips.

Second, the (2,1) representation is NOT self-conjugate: (2,1) != (1,2). This breaks the exchange symmetry between "particle" and "antiparticle" within the sector. For self-conjugate representations like (1,1) or (0,0), the eigenstates come in CP-related pairs, and the Zak phases of paired states are correlated. For non-self-conjugate sectors, this correlation is absent, allowing more independent Z_2 choices.

Third, the (2,1) sector has the most near-degeneracies at intermediate tau. The Berry connection sum|A| = 19,782 is the largest of any sector, indicating the most eigenvector rotation. More rotation means more opportunities for half-rotations.

The 5 pi-phases in (2,1) have Z_2 parity 1 (odd), consistent with the BDI single-unpaired-state theorem. The extra 4 (compared to 1) come in 2 pairs, each pair consisting of two states whose Z_2 indices are "wasted" -- they contribute to the topological channel count but cancel in the Z_2 parity. These are the EXCESS topological channels beyond the minimum required by symmetry.

---

## 8. Open Computations and the Non-Abelian Frontier

Three computations would sharpen this picture:

**Non-Abelian Wilson loop for the 492 degenerate states.** The Abelian Zak phase is ill-defined within degenerate subspaces. The correct object is the non-Abelian holonomy W = P exp(-i integral A_mu dtau), where A_mu is the matrix-valued Berry connection restricted to the degenerate subspace. The eigenvalues of W are the gauge-invariant content. This computation would resolve the 492 "other" states into definite topological sectors and complete the pi-phase census. The code infrastructure exists (compute_wilson_loop in s46_berry_phase.py).

**Closed-loop Berry phase.** The S46 computation covers the one-way path tau: 0.001 -> 0.190. Adding the return path tau: 0.190 -> 0.001 closes the loop. For the SAME eigenvector branch (tracked adiabatically), the closed-loop phase must be 0 or 2pi for real eigenstates -- the S25 ERRATUM is recovered. But for the SORTED eigenvector (re-sorted by eigenvalue at each tau), the closed loop may detect crossings that the one-way path missed. This distinguishes geometric phase (path-dependent) from topological phase (path-independent modulo homotopy).

**Dissolution robustness.** The S45 dissolution scaling epsilon_c ~ 1/sqrt(N) gives a critical perturbation strength. At epsilon = epsilon_c, the SU(3) spectral structure begins to dissolve. Do the 13 pi-phase states survive? Topological invariants are robust against perturbations that do not close the gap. But dissolution IS a gap-closing process. The question is whether the pi phases disappear before or after the gap closes -- i.e., whether the topological skeleton is the FIRST or LAST structure to dissolve. If last, the substrate protects its topology above all else.

---

## 9. The Central Geometric Picture

The Dirac spectrum on Jensen-deformed SU(3) has the following layered topological structure:

- **Layer 0 (zeroth homotopy)**: The eigenvalue flow. 992 eigenvalues flow smoothly as functions of tau. No crossings. The spectrum is a collection of smooth curves over the tau interval. This layer carries the quantum metric (g = 982.5) and the fold catastrophe (A_2 at tau = 0.190).

- **Layer 1 (first homotopy / Z_2)**: The Zak phase. 13 eigenstates have pi phase; 487 have zero phase. This layer detects the topology of the eigenvector bundle -- the Mobius twists that are invisible to eigenvalue tracking. It is quantized (Z_2), cannot be removed by smooth deformation, and is independent of the transit speed.

- **Layer 2 (non-Abelian)**: The Wilson loop holonomy. 492 states in degenerate multiplets carry non-Abelian Berry phase. This layer has not yet been computed. It requires the matrix-valued connection and detects non-commutative topology in the degenerate subspaces.

The paradox identified in S36 -- "large quantum metric, zero Berry curvature, sensitivity without protection" -- is now partially resolved. The quantum metric (Layer 0) measures how FAST eigenstates change. The Berry curvature (zero) measures LOCAL twisting. The Zak phase (Layer 1) measures GLOBAL twisting. The substrate has no local curvature but does have global topology. The protection is not infinitesimal (curvature-based) but finite (Z_2-based). It protects not the rate of change but the PARITY of the total change.

This is the kind of protection a substrate of everything would have. Not a smooth, continuous shield (that would require nonzero Berry curvature, which the Kosmann anti-Hermiticity forbids). But a discrete, topological lock -- a Z_2 per sector that says: you can deform me however you like, but you cannot change my parity without closing a gap. And the gaps do not close (spectral flow = 0, Permanent Result #10).

---

## Files Referenced

- `tier0-computation/s46_berry_phase.py` (computation)
- `tier0-computation/s46_berry_phase.npz` (data)
- `researchers/Berry/01_1984_Berry_Quantal_Phase_Factors.md` (Paper 01)
- `researchers/Berry/03_1984_Berry_Diabolical_Points.md` (Paper 03)
- `researchers/Berry/11_1984_Berry_Curvature_Solids.md` (Paper 11)

## Prior Results Invoked

- S25 ERRATUM: Berry curvature = 0, quantum metric = 982.5 (PERMANENT)
- S17c: BDI classification, T^2 = +1 (PERMANENT)
- S22b: Block-diagonal theorem (PERMANENT)
- S25 Permanent Result #7: Berry curvature vanishing on compact Lie groups
- S25 Permanent Result #10: Spectral flow = 0
- S34: K_7 selection rules, Trap 1 V(B1,B1) = 0
- S36 WIND-36: BDI winding number nu = 0
- S38: Quench P_exc = 1.000, GGE with 8 conserved integrals
- S46 W4-2: BAND-INVERSION-BERRY-46 (13 pi-phase states)

## Open Gates Arising

1. **WILSON-LOOP-47**: Non-Abelian Berry phase for the 492 degenerate-subspace states. Pre-register: total pi-count (Abelian + non-Abelian) in [13, 50].
2. **DISSOLUTION-BERRY-47**: Do the 13 pi-phase states survive at epsilon = epsilon_c? Pre-register: PASS if all 13 survive at epsilon = 0.5 * epsilon_c.
3. **CLOSED-LOOP-47**: Round-trip Berry phase tau: 0 -> 0.19 -> 0. Pre-register: closed-loop gamma = 0 for all non-degenerate states (S25 ERRATUM consistency check).
