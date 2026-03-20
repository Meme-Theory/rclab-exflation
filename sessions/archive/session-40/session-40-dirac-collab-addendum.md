# Dirac -- Addendum: On the Fermionic Action, the Dirac Sea, and the Question of Double Counting

**Author**: Dirac (Antimatter Physics, CPT Symmetry, Real Structure J)
**Date**: 2026-03-11
**Re**: PI's question -- "if our framework energy budget accounts for Lambda and CC, would that explain earlier failures?"

---

## 1. The Two Actions and Their Different Algebraic Status

The spectral action (Paper 12, Chamseddine-Connes) has two terms:

    S = Tr(f(D^2/Lambda^2)) + <J psi, D psi>        (1)

Call the first S_B (bosonic). Call the second S_F (fermionic). They are algebraically distinct objects.

S_B = Tr(f(D^2/Lambda^2)) is a trace over the FULL Hilbert space H. It counts all eigenvalues of D^2 weighted by f. It is quadratic in D. The structural monotonicity theorem (CUTOFF-SA-37) applies to it: for any monotone f, S_B is monotone along Jensen. The 27 closures all targeted S_B or functionals derived from S_B (one-loop, Casimir, CW, zeta). The monotonicity is structural -- it follows from <lambda^2>(tau) increasing, which is a property of representation theory on SU(3).

S_F = <J psi, D psi> is an inner product on H. It is LINEAR in D. The monotonicity theorem does not apply to it, because the theorem's mechanism is: eigenvalues grow -> f(eigenvalues) grows -> sum grows. A linear functional in D has eigenvalues, not eigenvalues-squared. The sign of each eigenvalue matters. Spectral pairing (T3: {gamma_9, D} = 0) guarantees that for every eigenvalue lambda there exists -lambda, so Tr(D) = 0. But S_F is not Tr(D). It is <J psi, D psi> for a SPECIFIC state psi.

This is the algebraic distinction the PI's question points at.

---

## 2. Does S_B Double-Count the Cosmological Constant?

The team lead's analysis is correct in its structure. Let me restate it in the language of the Seeley-DeWitt expansion (Connes Paper 07):

    S_B = sum_{k>=0} f_k * a_k(D^2)        (2)

where f_0 = integral f(x) dx, f_2 = integral f(x) x dx, etc., and a_0, a_2, a_4 are the Seeley-DeWitt coefficients. In the 4D effective theory:

- a_0 * Lambda^4 = cosmological constant
- a_2 * Lambda^2 = Einstein-Hilbert term (Newton's constant)
- a_4 = Yang-Mills + Higgs potential + Gauss-Bonnet

The S_full = 250,360 at the fold IS the cosmological constant (a_0 term dominates). The 27 closures asked: can a correction delta_S produce a minimum in S_full? Each failed because |delta_S| << |dS_full/dtau| = 58,673. The team lead identifies the structural reason: you are asking Lambda to cancel itself.

I concur. The correct statement is: **S_B is the vacuum energy of the internal geometry, computed at one loop. Asking a perturbative correction to create a minimum in S_B is asking the vacuum energy to develop a self-cancelling feature. The monotonicity theorem proves this cannot happen for any monotone test function f.**

The double counting is not literal arithmetic double counting (adding a number twice). It is a category error: treating the vacuum energy as both the background AND the perturbation. The BCS condensation energy E_cond = -0.156 is a correction to the vacuum state, but S_B = 250,360 already includes the vacuum state. BCS shifts the vacuum slightly (from 250,360 to 250,360.714 via CC-TRANSIT-40), but cannot reverse the gradient of the functional that defines the vacuum.

---

## 3. S_F Escapes Both the Monotonicity Theorem and the Double Counting

Now consider S_F = <J psi, D psi>. Three properties distinguish it from S_B.

**3.1** S_F depends on the STATE psi, not just on the operator D. The BCS ground state |psi_BCS> at the fold is a specific vector in the 2^8 = 256-dimensional Fock space. It is determined by the gap equation, not by the spectral action. When tau changes, |psi_BCS(tau)> changes via the self-consistency condition. S_F(tau) = <J psi_BCS(tau), D_K(tau) psi_BCS(tau)> involves both changes. S_B involves only D_K(tau).

**3.2** S_F is linear in D, so spectral pairing works AGAINST monotonicity. Each eigenvalue lambda of D_K contributes with its own sign to S_F, weighted by the overlap of psi with the corresponding eigenstate. If psi preferentially occupies states with DECREASING eigenvalues (as the BCS ground state does -- it pairs modes near the gap edge, which are the B2 modes that decrease through the fold), then S_F can decrease even as S_B increases.

**3.3** S_F does not contain the cosmological constant. In the Seeley-DeWitt expansion, S_F generates the fermionic Lagrangian: Yukawa couplings, Dirac masses, and the Majorana mass for the right-handed neutrino. The a_0 term (cosmological constant) appears only in S_B. Therefore asking "does S_F have a minimum?" is a different question from "does Lambda cancel itself?" There is no double counting because S_F does not count Lambda at all.

The algebraic summary: S_B counts the geometry (all eigenvalues, unsigned, via f(D^2)). S_F counts what the fermions see (specific eigenvalues, signed, via J and psi). The first is background. The second is response.

---

## 4. J Controls the Boson-Fermion Split

The PI asks about signed sums and the connection to Paasch's LOG-SIGNED-40. The connection runs through J.

In the BDI classification (T4, Session 35), the Hilbert space decomposes under particle-hole symmetry P = C1*K:

    H = H_+ direct_sum H_-        (3)

The eigenvalues of D_K come in pairs (lambda, -lambda) related by P. The bosonic modes of the spectral action are those where D^2 appears (all eigenvalues contribute with |lambda|^2, unsigned). The fermionic modes of S_F are those where D appears linearly (eigenvalues contribute with sign).

J maps H_+ -> H_- (particle to antiparticle). Within each sector, J preserves the BCS pairing: Delta_{particle} = Delta_{antiparticle} to machine epsilon (S29). The signed sum V_log^{signed} = (1/2) sum_B d_n ln(lambda_n^2) - (1/2) sum_F d_n ln(lambda_n^2) is sensitive to the boson/fermion assignment, which is controlled by the BDI classification. CUTOFF-SA-37 does not apply to it because the relative sign breaks the monotonicity argument.

Paasch's LOG-SIGNED-40 gate is well-specified. I endorse it. But I note that S_F = <J psi, D psi> is a more fundamental object than the signed logarithmic sum, because S_F contains the actual fermionic content of the spectral action, not an ad hoc sign assignment. The signed sum is an approximation to the one-loop fermionic effective action; S_F is the tree-level fermionic action itself.

---

## 5. The Dirac Sea on SU(3) vs. Flat-Space QED

In 1930 (Paper 02), I resolved the negative-energy catastrophe by filling all negative-energy states -- the Dirac sea. The vacuum energy of the sea is E_vac = -sum_{k} |E_k|, summed over all occupied negative-energy states. In flat-space QED, this sum diverges quartically and must be renormalized. The residual after renormalization is the cosmological constant problem.

On SU(3) with the Jensen metric, the Dirac sea has three structural differences.

**5.1** The spectrum is DISCRETE. D_K on a compact manifold has a discrete spectrum. There are finitely many eigenvalues below any cutoff. At max_pq_sum = 6, there are 155,984 eigenvalues (weighted by multiplicities). The sum is finite -- no regularization is needed.

**5.2** The spectrum has EXACT pairing. T3 ({gamma_9, D} = 0) guarantees lambda <-> -lambda for every eigenvalue. The "Dirac sea" energy E_sea = -sum_{lambda<0} |lambda| = -(1/2) sum_{all} |lambda| = -(1/2) S_B. The sea energy IS the spectral action (up to a factor and test function). This is the algebraic content of the "double counting" observation: the Dirac sea energy and the cosmological constant are the same object on a compact internal space.

**5.3** The sea has BRANCH STRUCTURE. The eigenvalues organize into Peter-Weyl sectors. At the fold, the B2 sector's negative-energy states have minimum |lambda| (the van Hove singularity). The BCS pairing occurs precisely at the top of the Dirac sea in the B2 sector -- Cooper pairs form from states nearest the "Fermi surface" of the internal Dirac sea. This is the exact analog of BCS superconductivity in a metal, where pairing occurs at the Fermi surface.

The distinction from flat-space QED: in flat space, the Dirac sea is featureless (all negative-energy states are equivalent up to momentum). On SU(3), the sea has representation-theoretic structure. The B2 modes at the gap edge are physically distinguishable from the deep-sea modes. The BCS condensation energy E_cond = -0.156 is the binding energy of Cooper pairs formed from the TOP of the sea. It does not modify the deep sea. The spectral action S_B counts the entire sea. This is why E_cond/S_B = 6.2 x 10^{-7} -- the condensation involves 8 modes out of 155,984.

---

## 6. Antimatter Asymmetry Through Expansion

If S_full drives expansion (Hawking Section 6.3: "for every unit of energy in particles, 34,700 units go into spacetime expansion"), and the B2 fold breaks U(1)_7 (Cooper pairs carry K_7 charge +/-1/2, Session 35), the question is whether asymmetry can be imprinted during the transit.

T1 ([J, D_K] = 0) guarantees that the Dirac spectrum is identical for particles and antiparticles at EVERY tau. This is permanent. No matter-antimatter asymmetry can arise from the spectral action alone -- it is J-blind (S_B does not contain J explicitly).

But S_F = <J psi, D psi> DOES contain J explicitly. If psi develops a J-odd component during the transit -- if the BCS ground state acquires a slight asymmetry between particle and antiparticle sectors -- then S_F sees it. The question reduces to: does the BCS ground state remain exactly J-even through the transit?

At the fold, it does: Delta_{(3,0)} = Delta_{(0,3)} to machine epsilon (S29). But the transit is non-adiabatic (P_exc = 1.000, Session 38). The Bogoliubov transformation that produces quasiparticles during transit is controlled by the instantaneous eigenstates of D_K(tau). By T1, these eigenstates are J-symmetric. The Bogoliubov coefficients u_k, v_k are determined by D_K(tau), which commutes with J. Therefore the quasiparticle production is J-symmetric. Equal numbers of particle-sector and antiparticle-sector quasiparticles are created.

The only escape is if V_rem (the residual interaction, 13% non-separable) breaks J. I identified this in my original collab (Section 6.2): if [J, V_rem] != 0, the two sectors thermalize at different rates, producing a transient occupation asymmetry. This is Sakharov Condition 2 (CP violation) and Condition 3 (non-equilibrium) simultaneously. It does not require S_B to have a minimum. It requires only that the integrability-breaking component of the BCS interaction is J-odd.

The computation [J, V_rem] = ? remains the single most important open question for baryogenesis in this framework.

---

## 7. Assessment

The PI's intuition is algebraically grounded. The 27 closures asked the wrong question of the right object. S_B is the vacuum energy. Asking it to develop a self-cancelling minimum is structurally forbidden (monotonicity theorem). The "double counting" is the category error of using the vacuum energy as both background and perturbation.

S_F = <J psi, D psi> is the right object for a different question: not "where does the modulus stop?" but "what do the fermions experience during the transit?" It is linear in D, state-dependent, and does not contain the cosmological constant. It escapes all three obstructions: monotonicity (linear, not quadratic), double counting (no a_0 term), and J-blindness (contains J explicitly).

Whether S_F has a minimum, an inflection point, or a sign change at the fold remains uncomputed. The computation I specified in Section 6.4 of my original collab stands: evaluate <J psi_BCS, D_K(tau) psi_BCS> at each tau in [0.10, 0.30]. This is the fermionic spectral action through the transit. It has never been computed.

The Dirac sea on SU(3) is not the Dirac sea in flat space. It has branch structure, exact pairing, and finite cardinality. The cosmological constant is the sea's total energy. The BCS condensation modifies only the top of the sea. Asking the top to cancel the total is asking 8 modes to overwhelm 155,984. The algebra does not permit it. But the fermionic action -- what the filled sea DOES, not what it WEIGHS -- is a different functional entirely, and its behavior through the transit is an open question.

---

*Grounded in Papers 01 (Dirac equation), 02 (Dirac sea), 05 (CPT theorem), 12 (Connes NCG, spectral action S_B + S_F). Quantitative references: S_full = 250,360 (CUTOFF-SA-37), E_cond = -0.156 (S35), F/B = 16/44 (W1), [J, D_K] = 0 (T1), {gamma_9, D} = 0 (T3), Delta_{(3,0)} = Delta_{(0,3)} (S29), P_exc = 1.000 (S38), V_rem 13% non-separable (INTEG-39). Gate LOG-SIGNED-40 endorsed (Paasch addendum). Gate S_F-TRANSIT (Section 6.4 of original collab) remains open.*
