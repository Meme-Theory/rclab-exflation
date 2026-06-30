# S85 W11-2 Reconciliation Table

**Verdict**: PASS
**n_substantive_disagreements**: 0
**Delta-class counts**: (a)=4, (b)=6, (c-reconciled)=4, (c-unreconciled)=0, (d)=0

| # | Claim | Connes | Lizzi | VdD | Δ-class | Reconciliation |
|:--|:------|:-------|:------|:----|:--------|:---------------|
| 1 | HP^0(A_F) ∩ HP^1(A_F) = {0} by Z/2-grading | II.2: Parity Exclusion Theorem, HP^*(A) = HP^even ⊕ HP^odd as Z/2 direct sum | Result 1: FI by Z/2-grading, parity is algebraic (cyclic bicomplex (b,B)) | II.1: parity disjointness, Z/2-grading of HP* | **a** | Identical; same algebraic statement, three framings |
| 2 | image(ch: K_0(A_F) → HP^*) ⊂ HP^0 (rank-3 sublattice, generators (1,1,3)) | II.1: rank-3 sublattice, explicit ch generators (1,1,3) via Karoubi | Result 1: image(ch) rank-3 lattice disjoint from HP^1 by parity | II.1, II.3: image(ch^0) ⊂ HP^0, rank-3 generators | **a** | Identical rank; connes provides the most explicit generator list |
| 3 | ‖[ε_H]‖_{HP^1} = 16.197719, 5.21 OOM above 1e-4 threshold | II.2: heitsch_ratio = 16.197719, 5.21 OOM PASS margin | Result 1: heitsch_ratio = 16.197719 PASS 5.21 OOM safety | II.1: ‖[ε_H]‖_{HP^1} = 16.197719 at S83 anchor | **a** | Identical value to 6 significant figures |
| 4 | Origin of Z/2-grading (HKR vs cyclic bicomplex vs Connes periodicity) | II.1: HKR + S/B/I periodicity collapsing on finite-dim semisimple | Result 1: cyclic bicomplex (A_F, b, B) upstream of any regulator | II.1: Z/2-grading of periodic cyclic cohomology (Connes NCG 1994 §III.1-2) | **b** | All three arrive at the same parity; notational emphasis differs (HKR / bicomplex / periodicity) |
| 5 | Kasparov product [D] = [D_F] ⊗_{C(M)} [D_M] preserves HP-parity | Not explicit; scope at finite A_F primarily | Not emphasized; parity is L0 algebraic, product-structure implicit | II.2: explicit 4-step substitution chain; even base ⇒ no parity flip | **c-reconciled** | vdd provides the submersion-specific derivation; connes/lizzi accept submersion invariance as a consequence of Z/2-grading and Paper 01 factorization (cited by both); scope subsumption not conflict |
| 6 | Shriek map π_! preserves HP-parity (dim_R SU(3) = 8 even) | Not raised | Not raised | II.4: explicit substitution chain; even-dim fiber ⇒ π_! is parity-preserving | **c-reconciled** | Only vdd explicitly addresses π_!; lizzi's Result 1 subsumes this by 'no spectral weighting changes parity' (π_! is a degree-0 spectral-triple operation on HP*); scope subsumption, no disagreement |
| 7 | Load-bearing axiom set for HP^0/HP^1 disjointness | II.3: {Finiteness, Orientability, KO-dim 6, First-order} | FI/RD: parity is algebraic upstream of regulator, not axiom-listed | II.2: Paper 01 compactness + connection-compatibility + Z/2-grading | **b** | connes lists axioms; lizzi rephrases as 'upstream of L1 axiomatic'; vdd rephrases as Paper 01 hypotheses. All three agree the parity wall is axiom-forced. |
| 8 | Falsifier construction (what would break disjointness) | IV.C: CM-2008 twist gate S85-DISJOINT-CORRIDOR-COUNTER-CONSTRUCTION (violate first-order ⇒ twisted Chern into odd parity) | Result 5: admissible regulator that flips parity (unfalsifiable by admissibility class by construction; would break KO-dim=6) | Not explicitly titled; implicit in IV.4 scope-limits discussion (Jensen-survival test is W11-1; wider falsifier in V.3 meta-theorem) | **c-reconciled** | Three different falsifiers (twist / regulator / Jensen deformation) proposed, all converge on 'no admissible extension breaks parity'. Not conflicting -- different routes into the same unfalsifiability wall. |
| 9 | Meta-family unifying parity-exclusion with rank/other structural exclusions | IV.B: §VII.J (rank via Cartan) + §VII.P (parity) as distinct theorems in same family | Result 4: L0-algebraic (W10-114 parity) vs L3-per-observable (W6-67 RD) two-layer stacked | II.5: NCG-STRUCTURAL-EXCLUSION META-THEOREM — parity + rank as corollaries of single categorical statement in bivariant KK | **b** | All three propose unification; connes uses 'theorem family' language, lizzi uses 'L0/L3 layer' language, vdd uses 'categorical skeleton (bivariant KK / six-term exact)' language. Same meta-claim under three notational systems. |
| 10 | Permanent-registry landing target section | V.1: §VII.P (slot-allocation cascade to §VII.Q if occupied) | V.1: §VII-B registration (ε_H permanent wall) | V.6: HP-PARITY-DISJOINT-CORRIDORS entry, IV.1 canonical entry proposed | **b** | Different section labels (§VII.P / §VII-B / named-entry) but identical registration content; consolidation is V.5-lizzi / V.7-vdd / V.6-connes carry-forward |
| 11 | W10-114 verdict SHA citation fidelity | 577a90daa52514e9... (cited verbatim; matches verdict file) | Gate-name reference only; no SHA quoted | Gate-name reference only; no SHA quoted | **b** | Connes cites SHA verbatim (matches s84_gate_verdicts.txt); lizzi/vdd cite by gate name -- conventional difference in rigor, not disagreement |
| 12 | Cross-reference to S82 ABELIAN-SUBFACTOR-LACKS-L2-R-PROTECTION theorem | IV.B: §VII.J Cartan Level-2 explicit cross-reference | Not cross-referenced (focuses on W6-67 RD, not S82) | II.5 Structural comparison table: S82 W2-3 vs S84-W10-114 with 8-axis comparison | **c-reconciled** | lizzi scopes L0 at cyclic-bicomplex (parity) but notes same mechanism could house rank-exclusion; connes and vdd treat S82 explicitly. Scope difference reconciled: L0-layer (lizzi) is broader than parity-only; admits rank as co-member. |
| 13 | Scope limitations (what the triad does NOT prove) | IV.D: HP^3 class registration, HP-odd Chern domain, q-deformation all open | Result 2: RD magnitude is regulator-dressed (not structural wall at magnitude level) | II.6: HP^1(A_F) dimension/exhaustion, Heitsch uniqueness, Jensen survival all open | **a** | All three carefully list what is NOT proven; items overlap and are complementary (connes: extensions; lizzi: magnitude-RD; vdd: dimension and survival). No conflicts. |
| 14 | Corridor label convention (primary HP^0 vs secondary HP^1) | Primary K-theoretic (HP^0) / Secondary odd-cocycle (HP^1, H^3) | Primary HP^0 KK / Secondary HP^1/H^3 GV | Primary-KK / GV-SECONDARY (atlas tag) | **b** | Three notational schemes for the same two corridors; the meaning is identical under vdd-canonical-NCG-translation |

## Cross-check SHAs

- Connes W10-113 SHA ok: True
- Connes W10-114 SHA ok: True
- Connes W10-115 SHA ok: False
- Lizzi gate-name references: 3/3
- VdD gate-name references:  3/3
- S82 W2-3 cross-ref (connes): True
- S82 W2-3 cross-ref (vdd):    True
- S82 W2-3 cross-ref (lizzi):  False

Audit SHA: `6920eaefe192f72d399ba7185224b6a0cc1aa50ad2fabdca0310551a865a24d8`
Content SHA: `f5119a49dd5a8016ebd6b3b8adad1c6c4f61f768fa115447e48528384d28710e`