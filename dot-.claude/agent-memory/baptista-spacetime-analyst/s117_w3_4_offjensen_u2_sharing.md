---
name: s117-w3-4-offjensen-u2-sharing
description: S117 W3-4 PASS-RESOLVED — off-Jensen U(2) moduli; phi_88 (lambda_8 U(2)-center singlet) INDEPENDENT of eps_LX (CP^2 coset doublet). The U(2)-isotropy irrep-type test is the moduli-sharing discriminator.
metadata:
  type: project
---

**S117-W3-4-OFFJENSEN-U2-SHARING = PASS-RESOLVED.** `dim(off-Jensen moduli) = 5 = 1 (phi_88) + 4 (eps_LX coset) = 1 + k_coset`, NO linking constraint. phi_88 (lambda_8 Cartan, K7-transit CP, phi_CP=pi/2) and eps_LX (CP^2 coset off-diagonal, leptonic CP) are INDEPENDENT off-Jensen moduli ⇒ K7-transit survives a real leptonic eps_LX (J_PMNS=0 CONSISTENT with K7-transit baryogenesis). Verdict file: `computations/session-117/s117_gate_verdicts.txt` (audit_sha256 `1d6b5db3cb1a8e67...`). Script: `computations/session-117/s117_offjensen_u2_sharing.py`.

**Reusable method (the discriminator for ANY SU(3)-fiber moduli-sharing question):** decide RESOLVED vs SHARED by the **U(2)-isotropy IRREP TYPE** of the two deformation directions, NOT by generator commutators.
- Two directions in the SAME irrep (or equivariantly mixed under ad(u(2))) ⇒ a linking constraint ⇒ SHARED.
- Two directions in DIFFERENT irreps (no equivariant mixing) ⇒ independent ⇒ RESOLVED.

**Decisive structural facts (Sage QQbar + numpy, all residuals machine-exact 0.00e+00):**
- **lambda_8 generates the CENTER of U(2)**: `[lambda_8, lambda_1]=[lambda_8,lambda_2]=[lambda_8,lambda_3]=0`. So any deformation on lambda_8 is a U(2)-SINGLET. This is WHY phi_88 is independent of the coset.
- The coset `<lambda_4,lambda_5,lambda_6,lambda_7>` (CP^2 = SU(3)/U(2)) is ONE irreducible U(2)-DOUBLET: real commutant of `{ad(lambda_h)|coset}` = 2 = ℂ (Schur over ℝ); single hypercharge `|Y|=sqrt3` (`f_845=f_867=sqrt3/2`; `ad(lambda_8)|coset` eigenvalues ±sqrt3).
- su(3)=u(2)⊕m is reductive AND symmetric (`[m,m]⊆u(2)`) ⇒ CP^2 symmetric space.
- The substitution-chain warning made precise: `[lambda_8, coset]≠0` (coset carries hypercharge), BUT the U(1)_Y action rotates the coset off-diagonal PHASE (gauge on eps_LX) while FIXING lambda_8 (commutes with itself) ⇒ phi_88 is gauge-INVARIANT, cannot be absorbed into eps_LX. Generator non-commutation ≠ parameter linking.
- Method teeth: counterfactual — if the "Cartan phase" were a coset generator (lambda_4) it WOULD be SHARED (lands in the doublet). The test discriminates; RESOLVED is a genuine fact about lambda_8 being central.

**Framework Jensen block scaling** (`Phononic-Substrate-Geometry.md`, MCP-confirmed): `L_1=e^{2tau}` (u(1)_Y=⟨lambda_8⟩, 1 dir), `L_2=e^{-2tau}` (su(2)_I=⟨lambda_1,2,3⟩, 3 dirs), `L_3=e^{tau}` (C^2 coset=⟨lambda_4..7⟩, 4 dirs ⇒ k_coset=4). Josephson: J_C2=0.933 (coset), J_u1=0.038, J_su2=0.059.

**Convention pin**: Gell-Mann `Tr(lambda_a lambda_b)=2 delta_ab`; U(2)=⟨lambda_1,lambda_2,lambda_3,lambda_8⟩; coset CP^2=⟨lambda_4,lambda_5,lambda_6,lambda_7⟩; Jensen on Cartan ⟨lambda_3,lambda_8⟩, off-Jensen extends to the coset; phi_88 = lambda_8 CP phase = `phi_CP_K7_transit` = pi/2 (canonical:674, S100b). Real adjoint matrices: work in `e_a = i lambda_a` (anti-Hermitian su(3) basis) where ad(e_h) has REAL entries `(A_h)_{cb} = -2 f_{hbc}` — clean for real rep-theory (invariant subspaces, commutant dim).

Distinct from S76 off-Jensen work (W2-J: full 35D restoring-potential / ridge Hessian) — that is the full TT-moduli landscape; this gate is the specific phi_88-vs-eps_LX sharing dichotomy. Routing: supports W3-2 PASS-K7 + E-3 sector-resolution; mack Row #89 baryo annotation = sector-resolved. See [[paper-index-and-conventions]] (5D moduli parameterization) and [[permanent-results]].
