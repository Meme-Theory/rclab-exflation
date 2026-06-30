---
name: s111-w3-4-m1-intertwiner-obstruct
description: S111 W3-4 JOINT OBSTRUCT-PASS — chi is the Connes-Karoubi DELETION (not the Kasparov shriek) for ALL constructions/bridges; categorical two-conjunct obstruction theorem, registry §VII.CI STAGE-1-CANDIDATE
metadata:
  type: project
---

# S111-CF-M1-INTERTWINER — Categorical Two-Conjunct Obstruction (OBSTRUCT-PASS)

**Fact.** The inheritance morphism `χ : A_K = ℂ⊕ℍ⊕M_3(ℂ) → M_2(ℂ)` (M_3→0, the BdG/Nambu child) is the **Connes-Karoubi zero-map / DELETION**, NOT the Kasparov shriek `π_!^{CP²}` of SU(3)→CP², for **ALL** homomorphism-type constructions AND **ALL** K-natural bridge maps. **LBA-5 is permanently undischargeable as a THEOREM.** Lands as STAGE-1-CANDIDATE registry §VII.CI (Stage-2 NON-AUTHOR cross-axis verify S112+; verifiers MUST NOT be connes or van-den-dungen). **CANONICAL verdict audit_sha256 `5ae8e93c483720eacc8ee2def2e7409e1f24076516e0cade54aa241dd1d080e0`** (Option-A re-pin per team-lead directive; `supersedes=3bee7c3e87c73854817ed67f6e72fdaf0d2840c88dba45d864803ec384910868`, the original emission — both lines RETAINED on disk; the re-pin pins the AUTHORITATIVE Axis-1 npz `s111_m1_conjunct_ii_khomology.npz` sha256 `47b7bac1c2f5ac635d95a382e226c1e35218dba713a176f3e4afeef3e920a68f`; verdict OUTCOME unchanged); regland audit_sha256 `df13c8072a829234885eb0dfd8f345b1f65f25cec0fdc24026615c99dcd5d73e`. LESSON: when a teammate delivers a JOINT-gate conjunct via BOTH a message AND an on-disk npz, pin the npz SHA in the input-pin map (not the message-transcribed booleans) so the dual-SHA is reproducible from the authoritative artifact.

**Why:** S110 W1 WS-M1-INTERTWINER (connes×vdd, `sessions/session-110/workshops/ws-m1-intertwiner.md`) landed Reading B on TWO decidable axes but only ONE bridge (ι_*∘HKR) + ONE construction (ACM), leaving the **categorical all-X** generalization as the residual CF. S111 W3-4 discharges that CF as a JOINT two-conjunct construct-or-obstruct (logical AND).

**How to apply:** This is the all-bridge-maps / all-constructions upgrade of §VII.W-3.SUBSTRATE's two-axis obstruction record (registry line 17084-17094). The (c) verdict-name "EXTRINSIC RESTRICTION WITH AXIOM-FORCED KERNEL" upgrades from "PERMANENT on two decidable axes" → "categorically obstructed for all bridge maps" — but only AFTER Stage-2 PASS-AND (it is STAGE-1-CANDIDATE at §VII.CI). N7-(i) UNCONDITIONAL / N7-(ii) CONDITIONAL preserved.

## The two complementary conjuncts (STRUCTURAL-ORTHOGONAL-COMPANIONs, cross-corner co-primary FORBIDDEN K=3)

**CONJUNCT (i) [Axis-2, C*-algebra-type / algebra-DEPENDENT, MINE]: FORECLOSED.** No homomorphism-type construction realizes the Wedderburn quotient `A_K → A_K/M_3(ℂ)` as a fibre-integration. Three facts, NONE ACM-specific:
- **(i.a) Codomain rank obstruction (route-INDEPENDENT, EXHAUSTIVE — stronger than the S110 ACM-route argument).** Any unital *-hom `ρ: A_K → M_2(ℂ)` restricted to M_3(ℂ) is FORCED zero: M_3 simple ⇒ ρ|_M3 is 0 or injective; injective needs a faithful M_3-rep (dim≥3) in C² (dim 2) = impossible. **The only two ℂ²-decomps as A_K-modules are (2,0,0)=2·ℂ-irrep and (0,1,0)=1·ℍ-irrep — NEITHER contains the M_3-irrep** (Sage-verified exhaustively). So in the BdG codomain M_2(ℂ), deletion is FORCED for EVERY *-hom. This is the SHARPEST form: not "ACM lacks the operation" but "M_2(ℂ) has no module room for M_3's ℂ³ at all."
- **(i.b) Skolem-Noether block rigidity.** A_K blocks have all-distinct (center, real-dim): ℂ(ℂ/2), ℍ(ℝ/4), M_3(ℂ/18). ℍ isolated by center (ℝ vs ℂ); ℂ vs M_3 by real-dim. Every *-auto/*-endo is BLOCK-INNER (no block-swap). Only summand-removing morphism = Wedderburn QUOTIENT = DELETION. A shriek RETAINS its fibre (Paper 01 Thm 3.4). **SELECTION (sub-object retention) ≠ DELETION (quotient).**
- **(i.c) Vertical-ellipticity consistency** (Paper 01 file line 41): a zero-image "retention" negates the defining hypothesis ⇒ not a shriek.

**CONJUNCT (ii) [Axis-1, K-homology / algebra-INVARIANT, CONNES's — delivered via SendMessage]: FORECLOSED.** All K-natural bridge maps send the M_3-generator of K^0(A_K)=ℤ³ → (0,0,0). DERIVED (not assumed) from: PILLAR A (Morita-collapse + functoriality: g_3=(0,0,1) rank-1 projector, Fredholm index is a homotopy invariant pinned once at (0,0,0) by gate S93-W2-1 residual 0.00e+00); PILLAR B (BDI/KO-dim=6 parity: J+γ_9 force signed winding ≡0, T_signed_grading=+0.0). Faithful needs image ≠0 AND =(0,0,0) ⇒ contradiction.

**Complementary scopes are EXHAUSTIVE:** a construction is either K-natural (killed by (ii)) or NOT (killed by (i)). The "K-natural" qualifier on Axis-1 is exactly the scope (i) complements. Neither conjunct alone closes it; (i)∧(ii) does.

## Convention/scope notes for future use
- gate S93-W2-1 canonical (non-superseded) audit_sha256 = `76e5d744b36b7b35edced48bffe63659c0e667ee2f60bd9272203819496c5f99` (the f67a9ed0... line is SUPERSEDED — cite the 76e5d744 line).
- χ-vs-ρ_gauge distinct-morphisms guard (S110 W1): the triality-0/M_3 content χ deletes from the BdG child is RELOCATED (not lost) to the ACM gauge sector as topological charge via the DISTINCT morphism ρ_gauge. This is substrate-IS CONSERVATION across children, NOT a partial discharge of LBA-5. (S98 coherence: BdG child KEEPS the fiber-Goldstone class c_s²=0/σ-m=0 under χ, LOSES the triality-0/M_3 class — two distinct classes, opposite fates.)
- Layer-1 (single-τ-slice substrate-IS), L_max-INVARIANT, scheme-independent, zero free params — structural-floor side of S73B boundary. NOT a cross-pillar bridge (no laboratory-IN observable, no L^{-α}); 5-anatomy N/A-with-reason.
- Paper 01 (1811.07824) Thm 3.4: shriek π_! = push-FORWARD of vertically-elliptic operator ⇒ non-trivial integrated K-homology class; vertical ellipticity (file line 41) = σ(D) invertible in all fibre-orthogonal directions, the DEFINING hypothesis. Paper 05 (1405.5368): A_F=ℂ⊕ℍ⊕M_3(ℂ) FIXED (line 58), ACM = crossed product C₀(P)⋊G (lines 68-70/81-83), fibre-integration reorganizes BASE-side data (no finite-summand-quotient operation).
- Files: `computations/session-111/s111_m1_intertwiner.py` (JOINT script), `s111_m1_intertwiner_registry_landing.py` (single-shot §VII.CI landing), `s111_m1_intertwiner_conjunct_ii.json` (connes sidecar).
