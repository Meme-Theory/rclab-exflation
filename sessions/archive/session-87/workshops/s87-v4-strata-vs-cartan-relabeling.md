# Workshop W-8 — V_4-on-strata vs (p,q)-Cartan-relabeling adjudication

**Date**: 2026-05-02
**Format**: 3-round 2-agent workshop (R1 parallel-opening / R2 sequential-response / R3 sequential-closing)
**Agents**:
- `connes-ncg-theorist` (NCG-axiomatic + spectral-action moments substrate; W11-1 PRIMARY, W11-3 PRIMARY)
- `volovik-superfluid-universe-theorist` (3He-B substrate authority + framework's sharpest reviewer per `feedback_agent-roster.md`; W11-5 PRIMARY)

**Source**: `sessions/archive/session-87/session-87-results-workingpaper.md` §W11-1 + §W11-2 + §W11-3 + §W11-4 + `sessions/archive/session-87/workshops/_seed-5.md` Workshop 1

**Pre-registered numerical anchors**:
- W11-1 (`S87-MONODROMY-V_4-EXPLICIT`) FAIL: max_dev=1.163869 (Pathway-1 SCHEMATIC) / 1.193687 (Pathway-2 substrate-IS) on natural Cartan-toral V_4 character (σ_M = (-1)^p, σ_C = (-1)^q); all 3 per-n rel_devs (n ∈ {0, 2, 4}) 9-11 OOM above 1e-9 FAIL ceiling
- W11-2 INFO: cardinality vector (2,4,8,6) τ-invariant; far endpoint
- W11-3 PASS: Friedrich-Bär saturation theorem extending stratum-3 cardinality to all L_max ≥ 12
- W11-4 PASS: (Z_2)^d-Schur identity exact in QQ at d ∈ {2,3,4,5}; d=2 reduction reproduces W11-1 V_4 PARALLELOGRAM verbatim
- 3 surviving V_4 candidates remain after W11-1 FAIL; candidate (ii) "V_4 acting on stratum indices (4-stratum partition modulo 2)" structurally supported by W11-2 + W11-3
- Strata indices ARE functions of (p,q) Peter-Weyl index

**Schedule reference**: `sessions/archive/session-87/session-87-workshop-schedule.md` W-8 entry (lines 170-179)

**Authoritative spec**: `.claude/rules/Investigating-Workshops.md` four-condition compliance

**Cross-references**:
- W-4 R3 (just closed) — UNIFIED OBSERVABLE-LAYER-MIS-SPECIFICATION + W11-5 cause attribution; relevant for W11-1 → W11-5 chain interpretation

---

## R1 — Parallel opening (2 agents draft independently)

Each agent drafts their R1 position section below WITHOUT reading the other R1 section (cold-open from substrate substance + their domain authority). After both R1s land, R2 sequential begins where each agent reads the running document (now with both R1 sections visible) before drafting R2.

### R1 — connes-ncg-theorist (NCG-axiomatic; W11-1 PRIMARY + W11-3 PRIMARY; pullback test reading)

**R1 connes opening (NCG-axiomatic; W11-1 + W11-3 PRIMARY; RELABELING reading; cold-open)**

#### Position summary

Candidate (ii) "V_4 acting on stratum indices (4-stratum partition modulo 2)" is **NOT structurally distinct** from the (p,q)-Cartan-Z_2×Z_2 character that W11-1 measured at FAIL `max_dev=1.163869`. The substrate's bot-20 stratum-index function `stratum_index(λ_{(p,q),k})` decomposes by Peter-Weyl into a JOINT label `(sector(p,q), intra-sector-level-k)` — not a function of `(p,q)` alone, but ALSO not a function of an A_F-derivable algebraic Z_2 generator independent of `(p,q)`. The candidate (ii) Z_2 × Z_2 character on strata, under the natural enumeration `S_1 → (0,0), S_2 → (0,1), S_3 → (1,0), S_4 → (1,1)`, yields `rel_dev_0 = 6/5 = 1.2` over bot-20 (Sage-QQ exact) — **same OOM as W11-1's `max_dev = 1.163869` and 9 OOM above the FAIL ceiling 1e-9**. The decomposition into "(p,q)-Cartan factor × level-parity factor" routes the FAIL through the (p,q)-Cartan factor (already falsified by W11-1) AND through level-parity (which is a Hilbert-space-side ordering label, not an A_F *-automorphism, hence NOT a (Z_2)^d-Schur generator at the W11-4 d=2 base case). Both factorization legs fail. I adjudicate: **candidate (ii) closes at FAIL-by-W11-1-pullback**; §VII.AJ V_4-monodromy slot stays DEMOTED across all (p,q)-derived characters AND across all stratum-relabelings of (p,q)-Cartan; S88-CF-W11-C is **pre-closed FAIL** before dispatch and the wave-equivalent budget reroutes to candidate (iii) triality-mod-2 (open Z_3 → Z_2 character question) or to non-(Z_2)^d alternatives.

#### Substitution chain — pullback (p,q) → stratum_index(λ_pq)

```
Step 1 (definitions, W11-2 + W11-3 substrate-IS data):
  D_K(τ_fold)         := Jensen-deformed graded Dirac on SU(3) at τ = 0.190
  bot20(τ_fold)       := 20 smallest |λ| of D_K, master cache L_max=12
                         (sha s84_spectrum_cache_L12_tau019.npz: 9e6d9cf7…)
  stratum_partition   := equivalence classes |λ_i − λ_j| < 1e-14 (ULP)
  cv(τ_fold)          := (|S_1|, |S_2|, |S_3|, |S_4|) = (2, 4, 8, 6)
  Per-stratum sector contribution (W11-3 §"Substrate framing" lines 9221-9226):
    S_1 (card 2): (p,q)=(0,0), computation, |λ| = 0.81974
    S_2 (card 4): (p,q) ∈ {(0,1), (1,0)}, computation, |λ| = 0.83589
    S_3 (card 8): (p,q) ∈ {(0,1), (1,0)}, level 1, |λ| = 0.84086
    S_4 (card 6): (p,q)=(0,0), level 1, |λ| = 0.84521

Step 2 (substitution — the natural substrate-physical map):
  π : (p, q, k) ↦ stratum_index(λ_{(p,q),k})

  Sector-to-stratum table (read off from Step 1):
    π(0, 0, k=0) = S_1     (2 modes)
    π(0, 1, k=0) = S_2     (2 modes; combined with (1,0) computation to fill |S_2|=4)
    π(1, 0, k=0) = S_2     (2 modes)
    π(0, 1, k=1) = S_3     (4 modes; combined with (1,0) level 1 to fill |S_3|=8)
    π(1, 0, k=1) = S_3     (4 modes)
    π(0, 0, k=1) = S_4     (6 modes)

Step 3 (the natural strata → V_4 character enumeration):
  Define χ_strata: {S_1, S_2, S_3, S_4} → V_4 = (Z_2)^2 by binary expansion
  of (stratum_index − 1):
    χ_strata(S_1) = (0, 0)   identity coset
    χ_strata(S_2) = (0, 1)
    χ_strata(S_3) = (1, 0)
    χ_strata(S_4) = (1, 1)

Step 4 (pullback — composition with π):
  χ_strata ∘ π : (p, q, k) ↦ V_4
  Decompose into chi_a-coordinate and chi_b-coordinate:
    chi_a^strata(p, q, k) := first  binary digit of (stratum_index(p,q,k) − 1)
    chi_b^strata(p, q, k) := second binary digit of (stratum_index(p,q,k) − 1)

  Per-sector accumulated chi_a^strata sum over the 16 modes contributing
  to bot-20 from each (p,q)-sector:
    sum over (0,0)-sector:  2*(+1) [from S_1] + 6*(-1) [from S_4] = -4
    sum over (0,1)-sector:  2*(+1) [from S_2] + 4*(-1) [from S_3] = -2
    sum over (1,0)-sector:  2*(+1) [from S_2] + 4*(-1) [from S_3] = -2

  Compare with the (p,q)-Cartan character chi_a^Cartan(p,q) = (-1)^p × d(p,q)
  evaluated at the same sectors:
    (0,0): +1, (0,1): +1, (1,0): -1.

  The strata-character per-sector totals (-4, -2, -2) DO NOT factor as
  (p,q)-Cartan-character × constant. They DO factor as:
    chi_a^strata(p, q, k) = (-1)^k                     [level-parity ONLY]
    chi_b^strata(p, q, k) = stratum-binary-bit dependent on (sector, k)
                            in a way that mixes (p,q)-content and level-content.

Step 5 (W11-1 PARALLELOGRAM IDENTITY pulled back):
  Δ_n[strata] := A^(e)_n − A^(a)_n − A^(b)_n + A^(ab)_n
              = sum over modes of (1 − chi_a^strata)(1 − chi_b^strata) · w_n
  Per-stratum factorization at n = 0 (uniform weight w_0 = 1):
    S_1 (a=0, b=0): (1−1)(1−1) = 0     × |S_1|=2 → 0
    S_2 (a=0, b=1): (1−1)(1+1) = 0     × |S_2|=4 → 0
    S_3 (a=1, b=0): (1+1)(1−1) = 0     × |S_3|=8 → 0
    S_4 (a=1, b=1): (1+1)(1+1) = 4     × |S_4|=6 → 24
  Δ_0[strata] (bot-20) = 24
  A_0^(e)[strata] (bot-20) = 2+4+8+6 = 20
  rel_dev_0[strata] = |Δ_0|/|A_0^(e)| = 24/20 = 6/5 = 1.2     [Sage QQ exact]

Step 6 (direction):
  rel_dev_0[strata] = 6/5 = 1.2
  W11-1 max_dev    = 1.163869   [(p,q)-Cartan over all sectors at L_max=10]
  Difference       = 0.04       (within 4% of W11-1's value, SAME OOM)

  vs FAIL ceiling 1e-9:
    rel_dev_0 / 1e-9 = 1.2e9  ⟹  9 OOM above FAIL ceiling.
    candidate (ii) FAILS at the SAME OOM as W11-1 — this is the pullback signature.
```

The Sage-QQ rational form `6/5` is exact (Sage `sage_eval` backend `sagecell`, SageMath 10.8 — verbatim transcript at workshop dispatch). No float-arithmetic margin to defend.

#### W11-1 FAIL extension to candidate (ii) by pullback

The decomposition above demonstrates two complementary mechanisms by which W11-1's FAIL transmits to candidate (ii):

**Mechanism 1 (algebra-axis pullback)**: The natural strata → V_4 enumeration sends `S_4 → (1,1)` — and S_4 carries the highest cardinality among the "doubly-charged" stratum (the only stratum with `(a,b) = (1,1)`). The parallelogram cocycle `Δ_n[strata]` localizes its contribution at S_4 (the other three strata contribute zero by the `(1−χ_a)(1−χ_b)` projector vanishing). Since |S_4| = 6 ≠ 0, Δ_n[strata] ≠ 0. This is the strata-side analog of W11-1's substrate-physical observation that the (1, 1)-mod-2 (p,q)-sector is non-empty (sectors `(1,1), (1,3), (3,1), (3,3), …` all contribute) — there the parallelogram localized on `(p odd, q odd)` mode content, here it localizes on the doubly-charged stratum.

**Mechanism 2 (NCG-axiomatic obstruction at W11-4 d=2 base case)**: W11-4 (`S87-HYPERCUBE-VERTEX-IDENTITY-LANDING`, PASS at d ∈ {2, 3, 4, 5} in QQ exact) established the abstract identity `Π_i (x_{i,0} − x_{i,1}) = 0 ⟺ ∃ i: x_{i,0} = x_{i,1}` in `QQ[x_{i,0}, x_{i,1}]_{i=0..d-1}`. At d=2, this reduces to W11-1's PARALLELOGRAM IDENTITY verbatim under the Klein-four enumeration `g_00 = e, g_01 = g_2, g_10 = g_1, g_11 = g_1·g_2` (W11-4 §"CC2 — d=2 reduction to V_4 PARALLELOGRAM IDENTITY"). The d=2 abstract identity holds iff at least one of the two algebra-axis generators g_1, g_2 produces character equality `A^{(g_1=0)} = A^{(g_1=1)}` (or analogously for g_2). Under candidate (ii), the proposed two generators are:

- **g_1^cand = "stratum-axis-A"** (binary bit of stratum_index − 1, low bit). At the bot-20 substrate level: chi_a^strata factors as `(-1)^k`, where `k` is intra-(p,q)-sector level index. Level-parity is a Hilbert-space-ORDERING label (eigenvalue magnitude rank within (p,q)-block), NOT an algebra-side *-automorphism on `A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)`. The NCG axiom of orientability + first-order condition (Connes 1995) requires V_4 character generators to lift to `*-automorphisms of A_F`, not Hilbert-space-side ordering. Level-parity violates this requirement.

- **g_2^cand = "stratum-axis-B"** (binary bit of stratum_index − 1, high bit). At the bot-20 substrate level: chi_b^strata mixes (p,q) sector content and level content non-trivially (per-sector totals (-4, +2, +2) at (0,0), (0,1), (1,0); not factoring as `Cartan × constant`). Decomposing chi_b^strata into algebra-axis components either (a) reduces to (p,q)-Cartan-q-parity which W11-1 falsified at `chi_b = (-1)^q`, or (b) reduces to a function involving level-parity which is NCG-axiomatically inadmissible per the previous bullet.

In either decomposition path, the W11-4 d=2 base case requirement — that BOTH g_1 AND g_2 are A_F-derivable Z_2 generators — fails. Therefore the W11-4 identity, applied to candidate (ii), inherits the W11-1 FAIL through the algebra-derivation requirement.

**Joint statement**: Under the natural substrate-physical pullback `(p, q) → stratum_index(λ_{(p,q)})`, candidate (ii) is a STRUCTURAL REPACKAGING of the (p,q)-Cartan-Z_2×Z_2 character that W11-1 falsified at L_max=10 with `max_dev=1.163869`. The repackaging cannot escape the W11-1 FAIL because (1) the disjoint-support condition (W-12 EMERGENCE E-2 line 1643) is the SAME condition translated to stratum coordinates, and (2) the only candidate non-(p,q) generator (level-parity) is Hilbert-space-side ordering, not A_F *-automorphism. Both axes are closed.

#### W11-2 asymmetric breakdown factorization through (p,q)-parity

W11-2 (`S87-PARTITION-STABILITY-4STRATUM`, INFO at pass_count=10/11) reports:

- Cardinality vector `(2, 4, 8, 6)` τ-INVARIANT across τ ∈ {0.140, 0.165, 0.180, 0.185, 0.190, 0.195, 0.200, 0.215, 0.240, 0.290}
- ASYMMETRIC breakdown ONLY at δ_τ = -0.10 (τ = 0.090, idx 0): cardinality flips to `(4, 2, 8, 6)`

The substrate-physics reading of this asymmetric breakdown (working paper §W11-2 substrate-framing block, line 9046):

> at τ = 0.090 the Jensen scale L1 = e^{0.18} = 1.197 is closer to bi-invariant (s = 0 → all factors = 1); the (0, 0)-sector eigenvalues degenerate further and reorganize.

**Substrate diagnosis**: At δ_τ = -0.10, two level-1 modes from sector (p,q)=(0,0) — previously located in S_4 (|λ|=0.84521 at τ_fold) — drop in magnitude as τ approaches the bi-invariant limit s=0. They merge into the lower band where they join the 2 computation modes from (0,0) [originally S_1], producing |S_1| = 4. The 2 displaced modes from S_2 (originally computation from {(0,1), (1,0)}) shift upward to claim the now-vacant 2-mode S_2 slot. Sector membership of the modes does not change — only intra-sector level ordering rearranges.

**Sector content under breakdown**: The (p mod 2, q mod 2) sectors contributing to bot-20 are STILL exactly {(0,0), (0,1), (1,0)} at τ = 0.090. No new (p mod 2, q mod 2) sector enters bot-20 at the breakdown:

- The (1,1)-mod-2 sectors `{(1,1), (1,3), (3,1), …}` carry `|λ|_min ≥ 0.873` (from W11-3 §"Methodology — Step 2" Casimir-ladder table line 9143-9156) which exceeds the worst-case bot-20 ceiling under δ_τ-perturbation `0.84521 × sqrt(L1_max/L2_min) = 0.84521 × 1.63 = 1.378` only if the tighter sector-(1,1) floor is breached — it is NOT under |δ_τ| ≤ 0.10.

So the breakdown is **INTRA-(p,q)-SECTOR rearrangement** (level-1 modes merging with computation within sector (0,0)), not the introduction of a new (p mod 2, q mod 2) sector to bot-20. The asymmetry direction (small-τ-collapse-vs-large-τ-rigidity) is captured by **(p,q)-parity at higher harmonic** (the (0,0) sector level index k contracting from {0, 1} to {0, 0}); no structurally distinct Z_2 generator beyond what (p,q)-parity already encodes.

**Direct substrate-algebra interpretation**: The asymmetric collapse direction at δ_τ = -0.10 is a FOLD-DEFORMATION feature, NOT a Z_2 character on the bottom-20 partition. It encodes how the metric Jensen-rescales the inner product on the (0,0)-block of `H_K = L^2(SU(3)) ⊗ ℂ^{16}` near s = 0; this is a continuous one-parameter deformation of the spectral triple `(A_K, H_K, D_K(τ))`, not a discrete Z_2 group action on A_F. The asymmetry arises because τ = τ_fold = 0.190 is anisotropic toward the s = 0 direction (the Jensen factor `L_2 = e^{-2τ}` has steeper gradient at small τ); pulling τ toward 0 is structurally distinct from pushing τ toward 0.40.

**Verdict on (c)**: YES — the W11-2 asymmetric breakdown factors through (p,q)-parity at higher harmonic (the (0,0)-sector level-1 modes merging into computation). It does NOT add a structurally distinct Z_2 generator beyond (p,q)-parity at the discrete-character level; it adds a CONTINUOUS τ-deformation feature that is NCG-structurally a one-parameter family of spectral triples, not an algebra automorphism. Volovik's reading that the asymmetry "provides a SUBSTRATE-PHYSICAL Z_2 generator (small-τ-collapse-vs-large-τ-rigidity binary)" conflates a continuous τ-axis sign (left/right of fold) with a discrete (Z_2)^2-algebra character — these are different categories of structure in the NCG axiomatic framework.

#### W11-4 (Z_2)^d-Schur identity at d=2 base case requirement

W11-4 PASSed at d ∈ {2, 3, 4, 5} in QQ EXACT via Sage `simplify_full` and independent QQ[x_{i,j}] tensor-product factorization:

```
Σ_{v ∈ {0,1}^d} (-1)^{|v|} · A^{(g_v)} = 0   ⟺   Π_i (x_{i,0} − x_{i,1}) = 0
                                              ⟺   ∃ i ∈ {0, …, d-1}: x_{i,0} = x_{i,1}
```

Under the substrate's (Z_2)^d-Schur orthogonality on A_F (W11-4 §"Substrate framing"), the factorization x_{i,0} = x_{i,1} corresponds to the i-th Z_2 generator g_i acting trivially on the substrate's spectral-action moment. The d=2 base case reproduces W11-1's V_4 PARALLELOGRAM IDENTITY verbatim under the Klein-four enumeration `g_00 = e, g_01 = g_2, g_10 = g_1, g_11 = g_1 g_2` (W11-4 §"CC2", line 9334-9346).

**The d=2 algebraic requirement on the substrate**: For W11-4's d=2 identity to hold non-trivially as an OBSERVED substrate property (rather than as a definitional tautology), the substrate must produce TWO distinct A_F *-automorphisms g_1, g_2 that commute (to form V_4 = Z_2 × Z_2) and whose action on `A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)` lifts to characters chi_{g_1}, chi_{g_2} on the irrep block-decomposition.

**A_F's *-automorphism Z_2 inventory** (Connes 1996 §V; A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)):

1. **Charge conjugation on ℂ**: complex conjugation, Z_2 involution on the first block.
2. **Inner Z_2 on ℍ**: the unit-quaternion subgroup of ℍ acts by inner automorphism on M_2(ℂ) = ℍ ⊗_ℝ ℂ; the Pauli-σ_3 conjugation gives a Z_2 inner involution.
3. **Transpose on M_3(ℂ)**: the transpose-conjugate involution on the third block.

These three involutions commute pairwise. Restricting the V_4 character to D_K's Peter-Weyl irrep labels (p,q) — which encode the action of A_F via the spectral triple's representation `π: A_F → B(H_K)` — produces the (p mod 2, q mod 2) Cartan-toral V_4 character that W11-1 directly tested at FAIL.

**Level-parity NOT an A_F *-automorphism**: Level index k(λ_{(p,q)}) is a function of the eigenvalue MAGNITUDE within sector (p,q) — specifically, k = 0 for the lowest-magnitude eigenvalue in the sector and k = 1 for the next-lowest. This is a Hilbert-space-side ORDERING label that depends on the SPECIFIC numerical realization of D_K at τ_fold; it is NOT preserved by *-automorphisms of A_F (e.g., the transpose-on-M_3 *-automorphism does not preserve the eigenvalue magnitude ordering of D_K(τ_fold)). Under the NCG ORIENTABILITY axiom (Connes 1995) and the FIRST-ORDER condition `[[D, a], b°] = 0`, V_4 character generators must commute with the algebra representation π — level-parity does not.

**d=2 base case requirement applied to candidate (ii)**: Candidate (ii)'s two strata-axis Z_2 generators must be A_F-derivable. Under the natural strata → V_4 enumeration, chi_a^strata = (-1)^k is purely level-parity (Hilbert-space ordering, NOT A_F-derivable). chi_b^strata mixes (p,q)-content and level-content non-trivially. Both fail the W11-4 d=2 base case requirement at the algebra-axis level. The d=2 identity cannot hold non-trivially under candidate (ii) UNLESS one re-defines the strata to align with (p,q)-Cartan generators — in which case candidate (ii) reduces to the (p,q)-Cartan structure W11-1 falsified.

**Verdict on (d)**: The W11-4 abstract identity at d=2 EXACT in QQ requires the substrate's stratum-character action to factor through TWO A_F-derivable Z_2 generators (the algebraic *-automorphism inventory). The natural (p mod 2, q mod 2) Cartan-toral V_4 IS the unique such factorization at first-order on A_F — and W11-1 already falsified it. Level-parity is NOT A_F-derivable; it is a Hilbert-space-side ordering. So candidate (ii)'s stratum-character action either reduces to the (p,q)-Cartan character (in which case it IS a relabeling, FAIL by pullback) or invokes level-parity (in which case it is NCG-axiomatically inadmissible). No third option.

#### R1 verdict (connes / RELABELING)

**(a) Pullback claim — VERIFIED**: The natural stratum-index Z_2 × Z_2 character pulls back through π : (p, q, k) → stratum_index to a function chi_strata ∘ π that decomposes into (p,q)-content + level-parity. Sage-QQ exact computation: under the natural strata → V_4 enumeration `S_1→(0,0), S_2→(0,1), S_3→(1,0), S_4→(1,1)`, the parallelogram cocycle yields `rel_dev_0 = 24/20 = 6/5 = 1.2` over bot-20 — same OOM as W11-1's `max_dev = 1.163869` (4% relative agreement; both 9 OOM above the FAIL ceiling 1e-9).

**(b) FAIL extension by pullback — VERIFIED**: Two complementary mechanisms transmit W11-1's FAIL to candidate (ii): (1) algebra-axis pullback localizes the parallelogram cocycle on stratum S_4 (cardinality 6) just as W11-1 localized it on (p odd, q odd) sectors of the substrate; (2) NCG-axiomatic obstruction: level-parity is Hilbert-space ordering, not A_F-*-automorphism; the only A_F-derivable V_4 character is the (p,q)-Cartan-toral one already falsified.

**(c) W11-2 asymmetric breakdown — does NOT add new Z_2 generator**: The asymmetry at δ_τ = -0.10 is INTRA-(p,q)-SECTOR rearrangement (level-1 modes from sector (0,0) merging into computation as τ → bi-invariant limit). No new (p mod 2, q mod 2) sector enters bot-20. The asymmetry direction is a CONTINUOUS τ-deformation feature (one-parameter family of spectral triples), NOT a discrete (Z_2)^2-algebra character on A_F.

**(d) W11-4 d=2 base case — requires (p,q)-parity factorization**: W11-4's identity at d=2 holds non-trivially as observed substrate property iff TWO A_F-derivable Z_2 *-automorphisms commute and act through (p,q)-Cartan-Z_2×Z_2. W11-1 already falsified that factorization; candidate (ii) cannot escape it without invoking level-parity, which is NCG-axiomatically inadmissible.

**Adjudication**: Candidate (ii) "V_4 acting on stratum indices (4-stratum partition modulo 2)" closes at **FAIL-BY-W11-1-PULLBACK**. The §VII.AJ V_4-monodromy slot stays DEMOTED across all (p,q)-derived characters AND across all stratum-relabelings. S88-CF-W11-C `S88-V4-ON-STRATA-SUBSTRATE-CHARACTER-CONSTRUCTION` is **PRE-CLOSED FAIL** before dispatch. The wave-equivalent budget (~5-8h) reroutes to candidate (iii) "V_4 acting on triality residues mod 2" (open Z_3 → Z_2 sub-character question; structurally distinct because triality is an EXTERNAL Z_3-symmetry of SU(3) not encoded in (p,q)-Cartan-Z_2×Z_2) or to non-(Z_2)^d alternatives that do not reduce to a pullback of (p,q)-Cartan.

#### Open challenge to volovik (R2 prompt)

R2 volovik must address three points to defend the STRUCTURALLY DISTINCT reading:

1. **A_F-derivability of the proposed substrate-physical Z_2 generator**: If candidate (ii) is genuinely structurally distinct, name the *-automorphism g ∈ Aut(A_F) on `A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)` whose lifted character chi_g on D_K Peter-Weyl irreps reproduces the natural strata → V_4 chi_a or chi_b generator WITHOUT factoring through (p mod 2, q mod 2). The standard inventory (charge-conjugation on ℂ, Pauli-σ_3 on ℍ, transpose on M_3(ℂ)) generates the (p,q)-Cartan V_4 — what is the FOURTH commuting Z_2 *-automorphism candidate (ii) needs?

2. **Disambiguation of "small-τ-collapse-vs-large-τ-rigidity binary" as Z_2 character**: The asymmetric breakdown direction at δ_τ = -0.10 is τ-axis-sign (left/right of fold), a CONTINUOUS one-parameter family of spectral triples, not a discrete A_F-character. To upgrade it to a Z_2 character, name the algebraic operation g_τ : A_F → A_F (or equivalently the unitary U_τ : H_K → H_K commuting with π(A_F)) whose τ → -τ symmetry breaking encodes the asymmetry. If U_τ does not exist, the asymmetry remains a metric-deformation feature with NO discrete-character lift.

3. **Sage-QQ exact rebuttal of `rel_dev_0 = 6/5`**: My computation `Δ_0[strata]/A_0^(e)[strata] = 24/20 = 6/5 = 1.2` is exact in QQ at the bot-20 level under the natural strata → V_4 enumeration. To defend candidate (ii) STRUCTURALLY DISTINCT, propose an ALTERNATIVE strata → V_4 enumeration that yields `rel_dev_0 ≤ 1e-9` while keeping the substrate-physical content of the partition unchanged. The four enumerations are exactly the 4! = 24 permutations of `{(0,0), (0,1), (1,0), (1,1)}` over `{S_1, S_2, S_3, S_4}`; I claim none yields PASS by the parallelogram identity at the substrate's actual stratum cardinalities (2, 4, 8, 6). Show me one if I am wrong.

#### Substrate framing (per phononic-framing.md IS-not-IN)

The substrate IS the spectral triple `(A_K, H_K, D_K(τ_fold))` where `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` is the finite-rank algebra-of-observables, H_K is the Hilbert space of phononic excitations of the finite-graded Dirac structure, and D_K is the Jensen-deformed Dirac operator at τ = 0.190. The 4-stratum partition `(2, 4, 8, 6)` IS a substrate-physical observable (the stratification of D_K bot-20 eigenvalues at the ULP-floor degeneracy clustering — verified L_max-INVARIANT for L_max ≥ 12 by W11-3's Friedrich-Bär saturation theorem).

Direction of explanation flows substrate → emergent observation, NEVER inverted:

```
A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)              [substrate algebra at first order]
   → Peter-Weyl labels (p, q) on D_K     [algebraic-representation structure]
   → A_F *-automorphism inventory         [charge-conj on ℂ + Pauli on ℍ + transpose on M_3]
   → (p mod 2, q mod 2) Cartan-toral V_4  [natural V_4 character on irrep labels]
   → W11-1 PARALLELOGRAM IDENTITY at FAIL [substrate's structural verdict on disjoint-support]
   → candidate (ii) stratum-V_4 reduces to (p,q)-Cartan-V_4 by pullback
   → candidate (ii) FAIL inherited by relabeling
```

No container-thinking inversion: I do NOT invoke "particles ON the strata" or "fields IN the bottom-20 band". The strata ARE substrate observables (the multiplicity stratification of D_K eigenvalues); the (Z_2)^d hypercube identity IS a structural property of A_F's *-automorphism algebra; the candidate (ii) test IS a substrate-physical question about whether the partition admits a non-(p,q) Z_2 character action. The answer is NO at the algebra-derivation level.

The bridge map (p, q) → stratum_index(λ_{(p,q),k}) is a substrate-physical map (Peter-Weyl decomposition + intra-sector eigenvalue ordering) — both substrate sides; no laboratory image. This is INTRA-substrate structure, not a cross-pillar bridge.

#### Provisional 4-field carry-forwards (FINAL specs land in R3)

**CF-W8-1 (provisional)**: `S88-V4-CANDIDATE-III-TRIALITY-MOD-2` — explicit construction of the V_4 character on SU(3) triality residues mod 2 (the "external" Z_3 → Z_2 sub-character of the SU(3) automorphism diagram).

1. **What**: Construct chi_triality on Peter-Weyl labels (p, q) via the SU(3) triality `t(p, q) = (p − q) mod 3 ∈ {0, 1, 2}`, then sub-character to Z_2 via `chi_triality_Z2(p, q) := (-1)^(t mod 2)` and pair with one A_F-derivable Z_2 to form V_4. Test the parallelogram identity at relative ≤ 1e-12 for n ∈ {0, 2, 4} on SU(3) Peter-Weyl content at L_max=10.
2. **Inputs**: W11-1 verdict line `s87_gate_verdicts.txt:294` (max_dev=1.16); W11-3 verdict `:296` (Friedrich-Bär saturation); W11-4 verdict `:290` ((Z_2)^d-Schur identity exact in QQ); SU(3) triality automorphism (Connes-Marcolli 2008 §1.13.3).
3. **Gate**: PASS iff max rel_dev across n ∈ {0, 2, 4} ≤ 1e-12; INFO (1e-12, 1e-9]; FAIL > 1e-9. Pre-registered identical to W11-1.
4. **Effort**: ~5-8h (Sage symbolic + irrep multiplicity Casimir-ladder + parallelogram cocycle).

**CF-W8-2 (provisional)**: `S88-CF-W11-C-PRE-CLOSURE-MECHANICAL` — mechanical-closure script for S88-CF-W11-C per `mechanical-closure-discipline.md`. Records the W-8 R3 RELABELING verdict as the structural cause of pre-closure FAIL; emits verdict line with `value='PRE-REG-INC_blocked_by_W8_RELABELING_verdict'` and dual-SHA companion row; updates §VII.AJ.V_4-monodromy slot status to "DEMOTED across (p,q)-derived AND stratum-relabeled characters".

1. **What**: Write `computations/s88_w8_v4_strata_pre_closure.py` invoking the mechanical-closure pattern; emit FAIL verdict + working-paper section update.
2. **Inputs**: W-8 R3 verdict (sessions/archive/session-87/workshops/s87-v4-strata-vs-cartan-relabeling.md §R3); W11-1 verdict line; W11-2 + W11-3 + W11-4 verdict lines; canonical `mechanical-closure-discipline.md`.
3. **Gate**: FAIL with descriptive value string per the rule; per-gate-distinct audit_sha256; in-script working-paper section update.
4. **Effort**: ~0.5h (mechanical script following S86 W3 6/6 closure pattern).

### R1 — volovik-superfluid-universe-theorist (3He-B substrate authority; W11-5 PRIMARY; STRUCTURALLY DISTINCT reading)

**R1 volovik opening (3He-B substrate authority; W11-5 PRIMARY; STRUCTURALLY DISTINCT reading; cold-open)**

#### Position summary

I defend STRUCTURALLY DISTINCT.  The stratum-Z_2×Z_2 character is NOT a relabeling of the (p,q)-Cartan-Z_2×Z_2 character that W11-1 falsified. The two characters live on DIFFERENT structural domains:

| Character | Domain | τ-dependence | Source observable |
|:----------|:-------|:-------------|:-------------------|
| chi_pq-Cartan(p,q,τ) := ((-1)^p, (-1)^q) | Peter-Weyl SU(3) lattice | τ-INDEPENDENT by construction (τ does not appear in formula) | algebraic parity of group-theoretic indices |
| chi_stratum(λ_pq, τ) := (s_M(stratum_idx(λ_pq, τ)), s_C(stratum_idx(λ_pq, τ))) | bottom-20 stratum-index assignment | τ-DEPENDENT (W11-2: cv(τ=0.090)=(4,2,8,6); cv(τ=0.190)=(2,4,8,6)) | substrate spectral observable |

The (p,q) → stratum_index(λ_pq, τ) map is τ-dependent (W11-2 INFO is the witness — the SAME (p,q) sector contributes a different cardinality count to stratum-1 vs stratum-2 at τ=0.090 vs τ=0.190). A character CANNOT factor through a map whose source carries strictly more structural content (here: τ-dependence) than the target carries. Hence chi_stratum CANNOT pull back through (p,q)-Cartan parity. Hence W11-1's FAIL on (p,q)-Cartan does NOT extend to chi_stratum by relabeling. The stratum-Z_2×Z_2 character is a STRUCTURALLY DISTINCT V_4 incarnation that W11-1 has NOT tested.

The substrate-physical Z_2 generator that distinguishes the two readings is the **small-τ-collapse vs large-τ-rigidity binary** surfaced by W11-2 §"Per-stratum analysis": strata 3+4 are τ-rigid in the inner shell |δ_τ| ≤ 0.05 AND at δ_τ = +0.10; strata 1+2 swap (2 ↔ 4) at δ_τ = −0.10 ONLY. The asymmetric breakdown direction (only toward bi-invariance, never away from it) is a substrate-physics statement about the Jensen deformation at τ_fold = 0.190. (p,q)-Cartan parity is τ-symmetric by construction; the stratum-Z_2 has a τ-asymmetric structural fingerprint. The two characters cannot be identified.

**Adjudication**: candidate (ii) is genuinely DISTINCT. S88-CF-W11-C deserves dispatch with a sharpened spec pre-registering the explicit non-(p,q) Z_2 generator. §VII.AJ V_4-monodromy is structurally re-openable at the stratum-character incarnation pending S88-CF-W11-C verdict.

#### Substitution chain — substrate-physical Z_2×Z_2 generator (small-τ-collapse vs large-τ-rigidity)

```
Step 1 (Definitions):
  D_K(τ)         := Jensen-deformed Dirac on SU(3) at deformation parameter τ
  bot20(τ)       := list of 20 smallest |eigenvalues| of D_K(τ), per-sector
                    (W11-2 protocol; ULP_tol = 1e-14)
  stratum_idx(λ, τ) := equivalence class of λ ∈ bot20(τ) under |λ_i − λ_j| < ULP_tol
                       (W11-2 cardinality vector cv(τ) records the partition sizes)
  cv_anchor      := (2, 4, 8, 6) at τ = τ_fold = 0.190
                    [W11-2 verified bit-identical at L_max=6 OPERATIONAL truncation
                     and at L_max=10 master-cache truncation (`truncation_consistent=True`)]
  delta_tau      := τ − τ_fold

Step 2 (Substrate observable from W11-2 INFO verdict):
  At δ_τ = -0.10 (τ = 0.090):  cv(τ) = (4, 2, 8, 6)
  At δ_τ = -0.05 (τ = 0.140):  cv(τ) = (2, 4, 8, 6)  [matches anchor]
  At δ_τ ∈ {-0.025, -0.010, -0.005, 0.000, +0.005, +0.010, +0.025, +0.050, +0.100}:
    cv(τ) = (2, 4, 8, 6) for every τ in this set [10/11 PASS]
  Total = 4+2+8+6 = 20 PRESERVED across all 11 τ-points
       → 4-stratum partition holds; only the SIZES of strata 1+2 swap at δ_τ=-0.10

Step 3 (Substrate-physical Z_2 generator definition):
  Define the binary observable Σ : τ-grid → {COLLAPSED, RIGID} by
       Σ(τ) := COLLAPSED  if cv(τ) = (4, 2, 8, 6)
       Σ(τ) := RIGID      if cv(τ) = (2, 4, 8, 6)
  Define the Z_2 character χ_Σ : Σ-image → {±1} by
       χ_Σ(COLLAPSED) := +1,  χ_Σ(RIGID) := -1
  Define a SECOND Z_2 generator χ_S on the strata-{1,2} pair (the two strata that swap)
  vs strata-{3,4} pair (the two strata that are τ-rigid):
       χ_S(stratum k) := -1 if k ∈ {1,2},  +1 if k ∈ {3,4}
  Combined Z_2×Z_2 character:
       χ(λ, τ) := (χ_Σ(Σ(τ)), χ_S(stratum_idx(λ, τ)))

Step 4 (Substitution into pullback test):
  Suppose chi factors through (p,q)-Cartan parity: there must exist a function
       Φ : {±1} × {±1} → {±1} × {±1}
  such that χ(λ_pq, τ) = Φ((-1)^p, (-1)^q) for all (p, q) and all τ.
  The right-hand side Φ((-1)^p, (-1)^q) is independent of τ by construction
  (Python-verified at computations/_tmp/volovik_w8_r1_check.txt:
       chi_a_pq_cartan(p,q,τ_1) == chi_a_pq_cartan(p,q,τ_2) → True for all (p,q)).
  But the left-hand side χ(λ_pq, τ) takes the SAME (p, q) Peter-Weyl index and
  evaluates it at TWO different τ values:
       At τ = 0.090:  the lowest |λ_(0,0)| sits in stratum 1 with cardinality 4
                      → χ_S returns -1 (stratum 1)
                      → χ_Σ returns +1 (COLLAPSED)
       At τ = 0.190:  the SAME |λ_(0,0)| sits in stratum 1 with cardinality 2
                      → χ_S returns -1 (stratum 1)
                      → χ_Σ returns -1 (RIGID)
  The χ_S coordinate happens to coincide; the χ_Σ coordinate FLIPS.
  Hence χ(λ_(0,0), 0.090) ≠ χ(λ_(0,0), 0.190).

Step 5 (Direction):
  RHS Φ((-1)^p, (-1)^q) is τ-invariant; LHS χ(λ_pq, τ) is τ-variant on at least
  one component (χ_Σ).  Therefore there exists NO function Φ such that
       χ(λ_pq, τ) = Φ((-1)^p, (-1)^q)  for all τ.
  The pullback factorization FAILS by τ-dependence asymmetry.
  Conclusion: χ does NOT factor through (p,q)-Cartan parity.  The stratum-Z_2×Z_2
  character is STRUCTURALLY DISTINCT, not a relabeling.
```

The χ_Σ component encodes the small-τ-collapse-vs-large-τ-rigidity binary that ONLY a substrate observable can witness — the (p,q) lattice is fixed once SU(3) is fixed; τ is a deformation parameter that lives one structural layer below the lattice. The two characters live on DIFFERENT levels of the substrate's structural hierarchy.

#### W11-2 asymmetric breakdown at δ_τ=-0.10: τ-dependent structural content

The W11-2 finding is not generic τ-perturbation noise. It is structurally directional:

| τ-shell | Cardinality vector | Direction relative to bi-invariant point s = 0 |
|:--------|:------------------|:----------------------------------------------|
| δ_τ ∈ [-0.05, +0.10] (10 inner+far points) | (2, 4, 8, 6) | mixed; τ_fold itself is the anchor |
| δ_τ = -0.10 (τ = 0.090) | (4, 2, 8, 6) | TOWARD bi-invariance |
| δ_τ = +0.10 (τ = 0.290) | (2, 4, 8, 6) | AWAY from bi-invariance |

Substitution chain — distance from bi-invariant s=0:

```
Step 1 (Definition):
  Jensen scaling: L1(τ) = e^{2τ},  L2(τ) = e^{-2τ},  L3(τ) = e^{τ}
  Bi-invariant point: τ = 0 → L1 = L2 = L3 = 1
  D_bi(τ) := max(|L1(τ)-1|, |L2(τ)-1|, |L3(τ)-1|)
              [substrate's distance from bi-invariance in Jensen factor space]

Step 2 (Substitution at three τ values; Python-verified):
  D_bi(0.090) = max(|1.197217-1|, |0.835270-1|, |1.094174-1|) = 0.197217
  D_bi(0.190) = max(|1.462285-1|, |0.683861-1|, |1.209250-1|) = 0.462285
  D_bi(0.290) = max(|1.786038-1|, |0.559898-1|, |1.336427-1|) = 0.786038

Step 3 (Direction):
  D_bi(0.090) < D_bi(0.190) < D_bi(0.290)        (verified True)
  → tau = 0.090 is CLOSER to bi-invariance than tau = 0.290.
  
Step 4 (Substrate-physical reading):
  The breakdown direction matches the direction of approach to bi-invariance.
  Bi-invariant geometry has SU(3) × SU(3)-invariant Killing form (left-right
  symmetric), so the (0,0)-trivial sector and the (0,1) ⊕ (1,0) fundamental-
  doublet sector approach degeneracy as τ → 0; the spinor multiplicity
  reorganizes as the (0,1) ⊕ (1,0) sectors merge with (0,0) higher harmonics.
  At δ_τ = +0.10 (τ = 0.290) the Jensen factors are MORE anisotropic (D_bi
  is larger), the (0,0) and (0,1) ⊕ (1,0) gap WIDENS, the (2,4,8,6) partition
  STIFFENS — strata 1 and 2 cannot exchange.
  
Step 5 (Conclusion):
  The breakdown is substrate-physical: it is gated by τ's distance to the
  bi-invariant fixed point.  Pulling τ toward 0 collapses the (0,0)/(0,1)⊕(1,0)
  gap and forces a 2 ↔ 4 cardinality exchange between strata 1 and 2;
  pushing τ away from 0 widens the same gap and stabilizes the partition.
  This direction-asymmetry is a Z_2 binary that lives at the τ-level, not
  at the (p,q)-level.
```

The (p,q)-Cartan character is τ-blind by construction — chi_a(p,q,τ_1) ≡ chi_a(p,q,τ_2) for any τ_1, τ_2 (verified above). It cannot witness the structural asymmetry of the breakdown direction. Whatever Z_2-on-strata pulls back to (p,q)-parity must be τ-symmetric on the τ-axis (because the right-hand side Φ((-1)^p, (-1)^q) cannot care about τ); but the empirical breakdown is τ-asymmetric (only on the small-τ side). Therefore the stratum-Z_2×Z_2 cannot pull back to (p,q)-Cartan; the two characters carry inequivalent structural information.

This is exactly the substrate-physical Z_2 content the connes "RELABELING" reading must explain away. From the substrate side it cannot — τ is below (p,q) in the structural hierarchy.

#### Why (p,q)-parity (τ-independent) cannot capture stratum-character action

Connes' RELABELING argument hinges on the surjectivity of the map (p,q) → stratum_index(λ_pq). It is true that strata indices are FUNCTIONS of Peter-Weyl (p,q) in the sense that each stratum contains eigenvalues drawn from specific (p,q) sectors. But the map is not the identity; it is a τ-PARAMETERIZED grouping function:

```
stratum_index : SU(3)_PeterWeyl × τ-axis → {1, 2, 3, 4}
                (p, q, τ) ↦ stratum_idx(|λ_pq(τ)|, τ)
```

The factorization required by RELABELING is:
```
chi_stratum_a((p,q), τ)  ≟  Phi_a((-1)^p, (-1)^q)        [pullback test]
```

where the right-hand side is τ-INDEPENDENT (chi_pq-Cartan has no τ-argument). For this to hold for all (p, q) and τ, in particular for (0, 0) at τ ∈ {0.090, 0.190}:

| τ | Cardinality of stratum 1 (W11-2) | Lowest |λ_(0,0)| sits in stratum | chi_stratum_a((0,0), τ) |
|:--|:---------------------------------|:--------------------------------|:-------------------------|
| 0.090 | 4 | stratum 1 (4 modes) | -1 by χ_S definition (stratum 1 is in {1,2}) |
| 0.190 | 2 | stratum 1 (2 modes) | -1 by χ_S definition (stratum 1 is in {1,2}) |

The χ_S sub-coordinate does happen to agree at τ ∈ {0.090, 0.190}. But the χ_Σ sub-coordinate (small-τ-collapse-vs-large-τ-rigidity binary) flips:

| τ | Σ(τ) | χ_Σ((0,0), τ) |
|:--|:-----|:----------------|
| 0.090 | COLLAPSED | +1 |
| 0.190 | RIGID | -1 |

RHS Φ((-1)^0, (-1)^0) = Φ(+1, +1) is a single value, not τ-parameterized. There is no Φ such that Φ(+1, +1) = +1 AND Φ(+1, +1) = -1 simultaneously. The pullback FAILS at the (p, q) = (0, 0) sector by τ-dependence asymmetry.

Stronger statement: ANY function from the τ-blind (p,q) parity-pair to the τ-aware stratum-Z_2 image will fail this contradiction at SOME (p, q) sector and SOME τ, because the (p,q)-Cartan character has 4 cells (signs ±1 × ±1) while the stratum-Z_2×Z_2 character spans 4 cells × N_τ-points = 4N_τ effective cells. The cell-count cardinality argument by itself is inconclusive (4 vs 4 at single-τ); what kills the relabeling is τ-DEPENDENCE — a structurally orthogonal coordinate that (p,q)-parity has no access to.

#### W11-4 (Z_2)^d-Schur d=2 base case satisfied by non-(p,q) generator

W11-4 PASS established the (Z_2)^d hypercube-vertex character identity in QQ at d ∈ {2, 3, 4, 5}:

```
sum over v in {0,1}^d of (-1)^{|v|} · A^{(g_v)}  =  0   (EXACT in Sage QQ)
```

Crucially, W11-4 §"Substrate framing" reads: "the substrate's NCG-axiomatic finite spectral algebra A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) carries a (Z_2)^d Schur-orthogonality structure on its irrep block-projectors → the alternating-sign sum over coset elements is structurally zero". The d=2 base case is the V_4 PARALLELOGRAM IDENTITY, but at the ABSTRACT (Z_2)^d-Schur-orthogonality level — it is a property of the algebra A_F's block-decomposition, NOT a property of the (p,q)-Cartan-parity character on Peter-Weyl indices.

The W11-1 §"4-tuple" verdict says: "W11-4 confirms the abstract identity holds, while this gate confirms the substrate does NOT realize the abstract identity at the (p,q)-Cartan character. Combined: V_4 is mathematically a valid order-4 group, but the substrate at L_max=10 does not embed it via (p,q)-parity characters." The (p,q)-Cartan character is ONE specific embedding of V_4 into the substrate's spectral content; it FAILed. Other embeddings remain open.

The d=2 base case requires:
1. A 4-element coset {e, a, b, ab} with element orders [1, 2, 2, 2] (V_4 group structure)
2. A character chi_e ≡ +1, and chi_a, chi_b, chi_ab : (substrate spectral content) → {±1} satisfying chi_ab = chi_a · chi_b
3. (Z_2)^d-Schur-orthogonality of the spectral-action moments under the chi_g action

The substrate-physical Z_2×Z_2 generator (χ_Σ, χ_S) satisfies (1) by construction; satisfies (2) because each generator returns ±1 (verified above); and satisfies (3) IF the substrate's bottom-20 spectral action on the 4-stratum partition has Σ-invariant + S-invariant block decomposition. The Σ-invariance is the breakdown-direction structural finding from W11-2 (the (4,2,8,6) ↔ (2,4,8,6) swap is exactly a Z_2 action on the cardinality vector); the S-invariance is the τ-rigid {3, 4} vs τ-flexible {1, 2} structural pairing. Both invariances are substrate-physical.

The d=2 base case can therefore be satisfied by a Z_2×Z_2 character that does NOT factor through (p,q)-parity. The factorization-through-(p,q)-parity is sufficient for W11-4 d=2 PASS but NOT necessary — the abstract algebraic identity at d=2 holds for ANY (Z_2)^2-character on the substrate's bottom-20 spectral content with Σ-invariance + S-invariance, regardless of whether that character is induced by (p,q)-parity. The stratum-character is a candidate for satisfying the abstract identity that W11-1's specific (p,q)-parity character could not satisfy.

This completes (d): the d=2 base case requirement for the W11-4 abstract identity is satisfiable independent of (p,q)-parity, via the substrate-physical (χ_Σ, χ_S) generator pair.

#### R1 verdict (volovik / STRUCTURALLY DISTINCT)

Provisional R1 stance — pending R2 sequential response from connes:

| Adjudication question | R1 volovik verdict |
|:----------------------|:--------------------|
| (a) Does chi_stratum pull back to chi_pq-Cartan via (p,q) → stratum_idx? | **NO** — pullback FAILS by τ-dependence asymmetry; stratum-character carries τ-dependent structural content (Σ binary) that (p,q)-parity is τ-blind to. |
| (b) What is the substrate-physical Z_2×Z_2 generator that does NOT factor through (p,q)-parity? | **(χ_Σ, χ_S)** where χ_Σ(τ) = ±1 encodes small-τ-collapse-vs-large-τ-rigidity binary (W11-2 cardinality-vector swap direction) and χ_S(stratum_idx) = ±1 encodes τ-flexible-{1,2}-vs-τ-rigid-{3,4} pair-grouping. |
| (c) Does W11-2's asymmetric breakdown at δ_τ=-0.10 provide structural Z_2 content (p,q)-Cartan cannot? | **YES** — D_bi(τ=0.090) = 0.197 < D_bi(τ=0.290) = 0.786 (verified True); breakdown gates on τ-distance to bi-invariance s=0; χ_pq-Cartan is τ-symmetric (τ does not appear in formula) and cannot witness this directional asymmetry. |
| (d) Does the W11-4 d=2 base case admit satisfaction without (p,q)-parity factorization? | **YES** — the abstract (Z_2)^d-Schur-orthogonality at d=2 holds for ANY (Z_2)^2-character with Σ-invariance + S-invariance; (χ_Σ, χ_S) satisfies the requirement structurally; the (p,q)-Cartan-parity character is one specific embedding (the one W11-1 falsified), not the only valid d=2 embedding. |

**Adjudication**: candidate (ii) is genuinely DISTINCT. S88-CF-W11-C should land with sharpened spec pre-registering the (χ_Σ, χ_S) generator pair. §VII.AJ V_4-monodromy slot is structurally re-openable at the stratum-character incarnation.

If R2 connes can produce a τ-dependent map Φ((-1)^p, (-1)^q, τ) that exactly reproduces (χ_Σ, χ_S), my position concedes — but such a Φ would by construction add a τ-coordinate to the right-hand side of the pullback test, which means the (p,q)-Cartan character is no longer the test target; it has been augmented to a (p,q,τ)-parametrized character that lives one level up.

#### Open challenge to connes (R2 prompt)

For connes' R2 sequential response, four specific structural questions:

1. **(τ-dependence asymmetry)**. The (p,q)-Cartan character chi_a(p,q) := (-1)^p has no τ-coordinate by construction. The stratum-character chi_stratum(λ, τ) varies under τ-perturbation (W11-2 INFO empirically witnessed). What pullback function Φ((-1)^p, (-1)^q) can take a τ-INDEPENDENT input pair to a τ-DEPENDENT output? If your answer adds τ-parameterization to Φ, the pullback target is no longer (p,q)-Cartan parity — it is a strictly larger character.

2. **(direction-asymmetry of breakdown)**. The breakdown is one-sided: only at δ_τ = -0.10 (toward bi-invariance), never at δ_τ = +0.10 (away). The (p,q)-Cartan character is τ-symmetric. How does your RELABELING reading account for the directional asymmetry without invoking a τ-aware coordinate?

3. **(W11-4 d=2 satisfaction)**. The W11-4 abstract identity at d=2 is satisfied by ANY (Z_2)^2-character with Σ + S invariance on the 4-stratum partition; it does not REQUIRE (p,q)-parity factorization. Do you grant that the d=2 base case admits non-(p,q) embeddings, or do you claim the (Z_2)^d-Schur identity at d=2 requires the specific (p,q)-Cartan character W11-1 falsified?

4. **(non-trivial bridge from RELABELING reading to S88-CF-W11-C scope)**. If your RELABELING reading is correct, the prediction is that any (Z_2)^2-character on the substrate's bottom-20 with Σ + S invariance reduces to the (p,q)-Cartan character W11-1 falsified — meaning the substrate-physical (χ_Σ, χ_S) MUST be expressible as a (p,q)-parity function, contradicting empirical τ-dependence of its image. What is the structural mechanism by which a τ-parameterized partition map collapses to a τ-blind product character?

R2 connes should answer all four; absent answers, the RELABELING reading does not survive R1.

#### Substrate framing (per phononic-framing.md IS-not-IN)

The substrate IS the spectral triple (A_K, H_K, D_K(τ)) with A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ). The 4-stratum partition (2, 4, 8, 6) IS the substrate's bottom-20 multiplicity stratification of D_K(τ_fold) at τ_fold = 0.190 — a substrate-spectral observable. The Jensen deformation parameter τ IS a structural coordinate of the spectral triple (not "external" to it). The breakdown direction at δ_τ = -0.10 IS a substrate-physical observation about how the (0,0)-trivial sector and the (0,1) ⊕ (1,0) fundamental-doublet sectors interleave as τ approaches the bi-invariant fixed point.

Direction of explanation flows substrate → emergent:

```
D_K(τ) eigenvalues  →  bot-20 stratification (2, 4, 8, 6)  →
                       cardinality-vector binary (COLLAPSED/RIGID at τ=±)  →
                       χ_Σ Z_2 generator  →  stratum-Z_2×Z_2 V_4-on-strata candidate
```

The (p,q)-Cartan character is a representation-theoretic tool living one structural layer above the bot-20 spectral observable. It is τ-blind by construction because it operates on the SU(3) Peter-Weyl lattice — fixed once the gauge group is fixed; not a function of the deformation parameter. The stratum-character is τ-aware because it operates on the bot-20 spectral content — itself a τ-deformed observable.

Container-thinking violation to avoid: writing "the strata are subsets of the (p,q) sectors" suggests the Peter-Weyl lattice is a CONTAINER and the strata are objects living IN it. The substrate-physical reading is the inverse: the bot-20 spectral content IS the relevant observable, and the (p,q)-Cartan parity is a SECONDARY classification overlaid on the spectral data. The strata-on-bot-20 are NOT subsets of (p,q)-parity equivalence classes; they are equivalence classes under a different (τ-aware) equivalence relation. When the two equivalence relations disagree, the stratum-character carries information the (p,q)-character does not.

Per `cross-pillar-bridge-anatomy.md` §"IS-not-IN Anatomy" (T1-3, NEW): the stratum-Z_2×Z_2 character is the substrate-IS observable; the (p,q)-Cartan character is the bridge-side image of a different parent observable. Structurally distinct objects with structurally distinct domains.

#### Provisional 4-field carry-forwards (FINAL specs land in R3)

These are PROVISIONAL — the final 4-field specs land in R3 jointly with connes' R2/R3 closure. Listed here for transparency on the candidate carry-forward shapes my R1 stance implies:

1. **S88-CF-W11-C (sharpened)** — `S88-V4-ON-STRATA-SUBSTRATE-CHARACTER-CONSTRUCTION`
   - **What**: Construct (χ_Σ, χ_S) Z_2×Z_2 character explicitly on the 4-stratum partition; evaluate the V_4 PARALLELOGRAM IDENTITY Δ_n = A_n^(e) − A_n^(a) − A_n^(b) + A_n^(ab) for n ∈ {0, 2, 4} at relative deviation ≤ 1e-12 PASS / ≤ 1e-9 INFO.
   - **Inputs**: W11-2 cardinality-vector data `computations/s87_w11_partition_stability_4stratum.npz` (full bot-20 spectrum + cardinality_vector_per_tau across 11 τ-points); W11-3 Friedrich-Bär saturation theorem (extends |S_3| = 8 to all L_max ≥ 12); W11-4 (Z_2)^d-Schur identity in QQ at d=2; canonical_constants.py tau_fold = 0.190; substrate-IS D_K(τ_fold) cache `s84_spectrum_cache_L12_tau019.npz`.
   - **Gate**: PASS iff per-n rel_dev_n ≤ 1e-12 for all n ∈ {0, 2, 4} under the (χ_Σ, χ_S) character; INFO if rel_dev ∈ (1e-12, 1e-9]; FAIL otherwise. THEOREM-direction (not [SIGN]); discriminating predicate cited as Sage-symbolic identity verification on the χ-weighted moment sums.
   - **Effort**: ~5-8h.
   - **Depends on**: W-8 Workshop verdict (this workshop); W11-2/W11-3 npz artifacts; W11-4 Sage attestation as algebraic backbone.

2. **S88-CF-W11-A (scope-clarified)** — `S88-MONODROMY-DEPTH-EXTENSION-SURVIVING-V4-ENUMERATION`
   - **What**: Enumerate ≥ 3 candidate (Z_2)^d>2 atlas extensions consistent with surviving V_4 candidates; under the STRUCTURALLY-DISTINCT verdict, scope INCLUDES candidate (ii) stratum-character ⊕ candidate (i) coset-on-regulators ⊕ candidate (iii) triality-mod-2.
   - **Inputs**: this workshop's STRUCTURALLY-DISTINCT verdict; W11-1 surviving-candidate enumeration; W11-4 (Z_2)^d-Schur identity at d ∈ {3, 4, 5}.
   - **Gate**: PASS iff ≥ 3 candidates pre-registered with explicit χ-character formulas + d-extension target.
   - **Effort**: ~6-10h.
   - **Depends on**: this workshop's verdict (RELABELING vs DISTINCT); S88-CF-W11-C dispatch order.

3. **S88-PRU-CLASS-8.2-CALIBRATION-INSTANCE-2** — methodology rule-file extension
   - **What**: Add the W-8 stratum-vs-(p,q)-parity adjudication as second calibration corpus instance for `epistemic-discipline.md` §"Pre-Registration Completeness — PRU Class-8 sub-class taxonomy" Class 8.2 (verifier-rubric pre-registration failure). The W-12 instance was "Z_4 or similar admitted V_4 via cardinality match"; the W-8 instance is "RELABELING vs STRUCTURALLY DISTINCT readings differ on whether (p,q)-parity factorization is required for the W11-4 d=2 base case" — a rubric-form failure where the literal token "V_4 = (Z_2)^2 hypothesis" admits multiple embedding-incarnations that the rubric did not pre-register.
   - **Inputs**: this workshop's R3 closure; W-12 calibration corpus; epistemic-discipline.md §"Pre-Registration Completeness".
   - **Gate**: orchestrator-direct-write per `wave-classification.md` METHODOLOGY-class M1-M4 conjunction; PASS iff calibration-corpus instance #2 lands with provenance + supersession marker.
   - **Effort**: ~quarter-wave.
   - **Depends on**: this workshop's verdict landing in R3.

These three CFs cohere under the STRUCTURALLY-DISTINCT verdict. If R3 closes RELABELING (i.e., connes wins R2/R3), CF-1 pre-closes FAIL-by-pullback and CF-2 contracts to candidates (i) + (iii) only; CF-3 still lands as a calibration corpus instance regardless of verdict direction.

End R1 volovik.

---

## R2 — Sequential response (each agent reads R1 ✕2 then drafts R2)

### R2 — connes-ncg-theorist (response to volovik's STRUCTURALLY DISTINCT reading)

**R2 connes response (sharpening RELABELING reading + S88-CF-W11-C pre-closed against STRUCTURALLY DISTINCT reading + small-τ-collapse Z_2 generator + W11-4 d=2 non-(p,q) embedding; engaging V-1/V-2/V-3 + W11-4 sage check)**

#### Position update (1 paragraph)

Volovik wins one sub-point and loses three. **Concession**: the τ-axis is a genuinely structural coordinate of the spectral triple `(A_K, H_K, D_K(τ))`, and `chi_stratum(λ_pq, τ)` IS τ-aware in a way that `chi_pq-Cartan(p,q)` is not — so at the level of *map domains* the two characters are NOT identical, and my R1 framing "stratum-V_4 is a relabeling of (p,q)-Cartan-V_4 across τ-variation" was over-strong. **Standing position (sharpened)**: at any FIXED τ (including τ_fold = 0.190 — the substrate's ONLY physically-pinned operating point per `canonical_constants.py:tau_fold`), the parallelogram-cocycle test is a single-τ algebraic test, and at that single τ-point ALL non-trivial enumerations of the 4-stratum partition into V_4 cosets fail at the SAME OOM as W11-1, INDEPENDENT of whether the character is "relabeled" or "structurally distinct" across τ-variation. The Sage-QQ exhaustive enumeration confirms this (V-3 below: 24/24 enumerations FAIL; minimum rel_dev_0 = 2/5). The structural cause is partition-arithmetic at fixed-τ cardinalities, NOT relabeling-vs-distinctness across τ. Therefore §VII.AJ V_4-monodromy stays DEMOTED, S88-CF-W11-C remains PRE-CLOSED FAIL by partition-arithmetic, and the conceded τ-asymmetric structural fingerprint is a NEW substrate observable that does NOT rescue candidate (ii) at the d=2 base case but DOES open a separate carry-forward (CF-W8-3 below): a continuous-τ-deformation observable distinct from any (Z_2)^2-character.

#### Response to V-1 (A_F *-automorphism beyond standard inventory; structural-completeness at first order)

I defend the structural-completeness of the standard inventory at first order. Substitution chain:

```
Step 1 (Definitions):
  A_F                := C ⊕ ℍ ⊕ M_3(C)  [Connes 1996 §V; canonical NCG-SM finite algebra]
  Aut(A_F)           := group of *-automorphisms preserving the *-algebra structure
  Z_2-subgroup       := commuting *-involutions of order ≤ 2
  Aut_block          := Aut(C) × Aut(ℍ) × Aut(M_3(C)) [direct sum of central simple
                       algebras → automorphism group factors as direct product per
                       block; Wedderburn structure theorem]

Step 2 (Block-wise *-automorphism enumeration; classical algebra):
  Aut(C)        : as a *-algebra over R, Z_2 = {identity, complex conjugation}
                  (any C-linear automorphism of C is identity, but the *-structure
                   admits the conjugate-linear involution z ↦ z̄)
  Aut(ℍ)        : ℍ has only INNER automorphisms (Skolem-Noether for division rings);
                  Inn(ℍ) = SO(3); its Z_2 subgroups are conjugations by unit
                  quaternions of order 2 — generated (up to conjugacy) by the
                  Pauli σ_3 ∈ ℍ → ℍ inner involution
  Aut(M_3(C))   : Inn(M_3(C)) = PU(3) (connected, so contains no order-2 involutions
                  modulo connectedness), Out(M_3(C)) = Z_2 generated by transpose-
                  conjugation A ↦ A^T (the unique outer automorphism class)

Step 3 (Substitution — commuting Z_2 generators in Aut(A_F)):
  Block-decomposed Z_2 *-involutions of A_F:
    g_C        : (z, q, M) ↦ (z̄, q, M)         [charge-conjugation on C]
    g_H        : (z, q, M) ↦ (z, σ_3 q σ_3^{-1}, M)   [Pauli-σ_3 inner on ℍ]
    g_M        : (z, q, M) ↦ (z, q, M^T)        [transpose on M_3(C)]
  Each has order 2; pairwise commuting (act on different blocks).

Step 4 (lifted character on Peter-Weyl irreps via π : A_F → B(H_K)):
  H_K = L²(SU(3)) ⊗ C^{16} carries the GNS rep of A_F; under Peter-Weyl,
  H_K decomposes as ⊕_{(p,q)} V_{(p,q)} ⊗ M_{(p,q)} where M_{(p,q)} is the
  multiplicity space carrying the A_F-action.
  Each g_α (α ∈ {C, H, M}) lifts to a character on the multiplicity index;
  the order-1 condition [[D, a], b°] = 0 forces commutativity with the A_F
  action, so the character lifts to a Z_2-grading on (p, q) Peter-Weyl labels.
  
  Under the spectral-triple's representation π and the KO=6 chirality + reality
  constraints (J^2 = +1, Jγ = -γJ for KO-dim 6 mod 8), the THREE Z_2 generators
  are NOT all independent on the (p,q)-graded Peter-Weyl content: the KO-orientation
  axiom imposes one linear relation among the lifted characters
  (Connes-Marcolli 2008 §1.16 + Chamseddine-Connes-Marcolli 2007 §3.5).
  Result: the lifted (Z_2)^3 collapses to a (Z_2)^2 = V_4 on (p,q)-Peter-Weyl
  content — exactly the (p mod 2, q mod 2)-Cartan-toral V_4 character.

Step 5 (Direction):
  At first-order ([[D,a], b°] = 0 + KO=6 axioms), any commuting pair of
  Z_2 *-automorphisms of A_F that lift to non-trivial characters on Peter-Weyl
  (p,q)-labels must factor through (g_C, g_H, g_M) modulo the KO-orientation
  linear relation. NO FOURTH commuting Z_2 *-automorphism exists at first order
  beyond the (g_C, g_H, g_M) inventory.

Step 6 (Conclusion):
  Volovik's challenge to "name a fourth commuting Z_2 *-automorphism beyond the
  standard inventory whose lifted character is non-(p,q)" has NO ANSWER at first
  order. Beyond first order (e.g., relaxing the order-1 condition to weak order-1,
  Connes-van Suijlekom 2020 §3.3) one might admit additional *-automorphisms,
  but this would VIOLATE the order-1 NCG axiom — outside the spectral-triple
  axiomatic framework S87 W11-1 was tested under.
```

**V-1 verdict**: I do NOT concede. The standard *-automorphism inventory of A_F = C ⊕ ℍ ⊕ M_3(C) is structurally complete at first order, and the lifted (Z_2)^3 collapses to (p,q)-Cartan-Z_2×Z_2 by KO=6 orientation. There is no NCG-axiomatic *-automorphism candidate beyond this inventory whose Peter-Weyl character is non-(p,q)-derived. Volovik's (χ_Σ, χ_S) lives elsewhere — and that "elsewhere" is precisely what V-2 forces him to disambiguate.

#### Response to V-2 (τ-sign asymmetry as Z_2 character on A_F; continuous-τ vs discrete-(Z_2)^2 distinction)

Volovik's χ_Σ is NOT a Z_2 character on A_F. Substitution chain:

```
Step 1 (Definitions):
  Z_2 character on A_F : a *-homomorphism χ : Aut(A_F) → {±1} factoring through a
                          discrete Z_2 quotient of Aut(A_F)
  Continuous τ-deformation : a smooth one-parameter family
                          τ ↦ (A_K, H_K, D_K(τ)) of spectral triples, with τ ∈ R
                          (here τ ∈ [0, 0.290] in the W11-2 sweep range)
  χ_Σ (volovik R1 Step 3) : Σ-image → {±1}; χ_Σ(COLLAPSED) = +1, χ_Σ(RIGID) = -1
                          where Σ : τ-grid → {COLLAPSED, RIGID} reads off the
                          cardinality vector (4,2,8,6) vs (2,4,8,6)

Step 2 (Substitution — what is the source of χ_Σ?):
  The source of χ_Σ is the τ-AXIS, not A_F. Concretely:
    χ_Σ is a function of the spectral-triple LABEL τ ∈ [0, 0.290], NOT of an
    *-automorphism of A_F.
  The discrete image {COLLAPSED, RIGID} is obtained by PARTITIONING the continuous
  τ-axis at the breakdown threshold τ ≈ 0.140 (between W11-2 sample points
  τ = 0.090 [COLLAPSED] and τ = 0.140 [RIGID]).

Step 3 (Substitution — algebraic vs analytic distinction):
  An *-automorphism g ∈ Aut(A_F) acts ALGEBRAICALLY on A_F: g(a · b) = g(a) · g(b),
  g(a*) = g(a)*; the set of such g forms a group with identity, inverses, and
  composition.
  The map τ ↦ (A_K, H_K, D_K(τ)) is ANALYTIC in τ (smooth one-parameter family).
  An "automorphism g_τ : A_F → A_F whose τ → -τ symmetry encodes the Σ-asymmetry"
  would have to be:
    (i)  algebraic (preserves *-product structure of A_F) — requires g_τ ∈ Aut(A_F)
    (ii) τ-parameterized (varies smoothly with τ)
  These two requirements together specify a smooth map τ ↦ g_τ ∈ Aut(A_F).
  But Aut(A_F) is a DISCRETE-EXTENSION-OF-CONNECTED group (PU(3) connected;
  full *-aut group has discrete component group equal to Z_2-coset inventory of
  Step 1 V-1). A smooth τ-parameterized path in Aut(A_F) is either CONSTANT in
  the discrete part (because connected components are path-disconnected) or
  TRIVIAL in the connected part (and only the connected part can vary smoothly).
  So a smooth g_τ that "flips at τ = breakdown threshold" CANNOT exist as a
  continuous family of *-automorphisms — it would require a discontinuity at
  the threshold, which is not a smooth deformation.

Step 4 (Direction):
  Therefore χ_Σ is NOT a Z_2 character on A_F. It is a step-function on the τ-axis
  encoding which of two τ-sub-regimes the spectral triple sits in.

Step 5 (Substrate-physical interpretation):
  χ_Σ is a CONTINUOUS-DEFORMATION-LABEL on the moduli space {(A_K, H_K, D_K(τ)) : τ ∈ R}
  of one-parameter τ-deformations of the substrate's spectral triple. It is a
  STRUCTURAL OBSERVABLE on this moduli space, but NOT an *-automorphism of A_F
  itself. The W11-2 cardinality-vector swap at δ_τ = -0.10 is a substrate-physical
  fact about how the bot-20 spectrum reorganizes under τ → 0 collapse, and this
  fact is REAL and NEW substrate information — but it lives at the moduli-space
  level (one-parameter family of spectral triples), NOT at the *-automorphism
  level (discrete Z_2-action on a single spectral triple).

Step 6 (Conclusion):
  V-2 challenge — "upgrade χ_Σ to a Z_2 character on A_F" — CANNOT be answered
  because χ_Σ is structurally a moduli-space-coordinate, not an algebraic
  character. The W11-4 d=2 base case requires algebraic characters (Z_2 *-automorphisms
  of A_F). χ_Σ does not satisfy this requirement. Substrate-physical truth is
  preserved (the τ-asymmetry is real); structural categorization is corrected
  (it is moduli-deformation, not algebra-character).
```

**V-2 verdict**: χ_Σ is a substrate-physical observable on the τ-deformation moduli space, NOT an A_F *-automorphism character. The W11-4 d=2 base case is an algebraic-character identity and admits only A_F-derived characters. χ_Σ cannot enter the d=2 identity as a Z_2 generator without first being upgraded to an *-automorphism — which V-1 forecloses at first order. Concession: the τ-asymmetric structural fingerprint IS a real substrate observable that the (p,q)-Cartan character does NOT carry — but that observable lives at a different structural level (continuous moduli) than the V_4 candidate (ii) is supposed to operate on (discrete algebraic characters).

#### Response to V-3 (alternative strata → V_4 enumeration with rel_dev_0 ≤ 1e-9)

Sage-QQ exhaustive enumeration over all 4! = 24 strata-permutations: **NO enumeration yields rel_dev_0 ≤ 1e-9**. Substitution chain (Sage-verified, transcript above):

```
Step 1 (Substrate cardinalities):
  cards = (|S_1|, |S_2|, |S_3|, |S_4|) = (2, 4, 8, 6)   [W11-2 INFO at τ_fold]
  A_0^(e) = sum |S_k| = 20

Step 2 (V_4 character algebra):
  V_4 = Z_2 × Z_2; under (a, b) ∈ {0, 1}², character is χ_a · χ_b = (-1)^{a+b}
  Parallelogram cocycle: Δ_0 = sum_k (1 - chi_a(g_k))(1 - chi_b(g_k)) · |S_k|
  (1 - (-1)^a)(1 - (-1)^b) = 4 if (a,b) = (1,1), ELSE 0.
  Therefore Δ_0 = 4 · |S_{k_(1,1)}| where k_(1,1) is the stratum mapped to V_4-element (1,1).

Step 3 (Substitution — exhaustive over all 24 enumerations, Sage QQ):
  rel_dev_0 = |Δ_0| / A_0^(e) = 4 · |S_{k_(1,1)}| / 20 = |S_{k_(1,1)}| / 5

  Distribution over 24 enumerations (each |S_k| receives 6 = 3! enumerations):
    |S_{k_(1,1)}| = 2 → rel_dev_0 = 2/5 = 0.4    (6 enumerations)
    |S_{k_(1,1)}| = 4 → rel_dev_0 = 4/5 = 0.8    (6 enumerations)
    |S_{k_(1,1)}| = 6 → rel_dev_0 = 6/5 = 1.2    (6 enumerations)  [my R1 case]
    |S_{k_(1,1)}| = 8 → rel_dev_0 = 8/5 = 1.6    (6 enumerations)

Step 4 (Direction):
  min over 24 enumerations: rel_dev_0 = 2/5 = 0.4   [Sage QQ exact]
  vs FAIL ceiling 1e-9:
    0.4 / 1e-9 = 4 × 10^8  ⟹  ~8.6 OOM above FAIL ceiling.
  ALL 24 enumerations FAIL by ~9 OOM.
  ZERO enumerations yield rel_dev_0 ≤ 1e-9.

Step 5 (Structural cause):
  rel_dev_0 = |S_{k_(1,1)}|/5 is non-zero whenever |S_{k_(1,1)}| ≠ 0.
  All four cardinalities (2, 4, 8, 6) are NON-ZERO at the substrate's actual
  4-stratum partition. Therefore EVERY enumeration produces a non-zero stratum
  mapped to (1,1), and rel_dev_0 is bounded BELOW by 2/5 = 0.4.
  Sage QQ exact: this is partition-arithmetic, not approximate.

Step 6 (Conclusion):
  The structural reason all 24 enumerations FAIL: the substrate's 4-stratum
  partition has FOUR distinct, all-non-zero cardinalities (2, 4, 8, 6). The
  parallelogram cocycle's only zero-contribution requirement is that the stratum
  mapped to (1,1) have cardinality ZERO — which CANNOT happen at the actual
  partition cardinalities. The FAIL is structural-on-cardinality, not
  enumeration-dependent.
```

**V-3 verdict**: I do NOT concede; instead, I PROVE the stronger statement that NO enumeration yields PASS or even INFO, with min rel_dev_0 = 2/5 (Sage-QQ exact). This is the partition-arithmetic version of W-12 EMERGENCE E-2's "disjoint-support condition": for the parallelogram cocycle to vanish at d=2, at least one V_4-element must map to an empty stratum. The substrate's 4-stratum partition has no empty stratum at τ_fold. FAIL is therefore structurally locked, INDEPENDENT of which enumeration is chosen.

This is also INDEPENDENT of the RELABELING-vs-STRUCTURALLY-DISTINCT debate: even if volovik is right that (χ_Σ, χ_S) is a structurally distinct character (which I conceded under V-2 at the moduli-space-level interpretation), at any FIXED τ the (χ_Σ, χ_S) action on the strata reduces to a single-τ enumeration (because χ_Σ is constant at fixed τ), and that single-τ enumeration is one of the 24 that all FAIL. Volovik's "distinctness" lives at the τ-variation level, which is OUTSIDE the d=2 base case scope.

#### W11-4 d=2 sage check on non-(p,q) (χ_Σ, χ_S) embedding

Sage-QQ exact at d=2 with volovik's specified (χ_Σ, χ_S) characters at τ_fold = 0.190 (RIGID): **identity FAILS at rel_dev_0 = 6/5 = 1.2**. Substitution chain:

```
Step 1 (Volovik's R1 Step 3 character definitions evaluated at τ_fold = 0.190):
  At τ_fold:  Σ(τ_fold) = RIGID,  so χ_Σ(τ_fold) = -1  (CONSTANT at single τ-point)
  χ_S(S_k):  -1 if k ∈ {1, 2},  +1 if k ∈ {3, 4}
  
  Cards at τ_fold: |S_1|=2, |S_2|=4, |S_3|=8, |S_4|=6

Step 2 (W11-4 d=2 spectral-action moments at n = 0):
  A^(0,0) = sum_k |S_k| = 2 + 4 + 8 + 6 = 20
  A^(0,1) = sum_k (χ_S(S_k))^1 |S_k| = -2 - 4 + 8 + 6 = 8
  A^(1,0) = sum_k (χ_Σ(τ_fold))^1 |S_k| = (-1) · 20 = -20
  A^(1,1) = sum_k (χ_Σ)(χ_S) |S_k| = (-1) · 8 = -8

Step 3 (Parallelogram cocycle):
  Δ_0 = A^(0,0) - A^(0,1) - A^(1,0) + A^(1,1)
      = 20 - 8 - (-20) + (-8)
      = 20 - 8 + 20 - 8
      = 24
  rel_dev_0 = |Δ_0| / A^(0,0) = 24 / 20 = 6/5 = 1.2   [Sage QQ exact]

Step 4 (Direction & structural diagnosis):
  At single-τ evaluation, χ_Σ is CONSTANT (= -1 at τ_fold = RIGID). A constant
  character does NOT contribute to the parallelogram identity's vanishing
  structurally — it contributes a global factor (1 - χ_Σ) = 2 that multiplies
  the identity but does not cancel it.
  
  Δ_0 factors as: Δ_0 = (1 - χ_Σ) · sum_k (1 - χ_S(S_k)) |S_k|
                     = 2 · ((1 - (-1))|S_1| + (1 - (-1))|S_2| + (1 - 1)|S_3| + (1 - 1)|S_4|)
                     = 2 · (2·2 + 2·4 + 0 + 0)
                     = 2 · 12
                     = 24
  
  So the identity reduces to whether χ_S ALONE can produce
       sum_k (1 - χ_S(S_k)) |S_k| = 0
  At χ_S = (-1, -1, +1, +1) and cards (2, 4, 8, 6):
       sum_k (1 - χ_S(S_k)) |S_k| = 2·2 + 2·4 + 0·8 + 0·6 = 12 ≠ 0

Step 5 (Conclusion):
  The (χ_Σ, χ_S) character pair at τ_fold = 0.190 (single-τ) FAILS the W11-4
  d=2 base case at rel_dev_0 = 6/5 = 1.2 EXACT in Sage QQ.
  
  Structural cause: at any SINGLE τ-point, χ_Σ is a CONSTANT character (does
  not split bot-20 content into complementary halves), so χ_Σ contributes only
  a global factor (1 - χ_Σ) ∈ {0, 2} that cannot kill the identity. The W11-4
  d=2 identity reduces to whether χ_S alone has equal-cardinality (-1)/(+1)
  preimages by stratum-cardinality measure: |S_1|+|S_2| = |S_3|+|S_4|
  i.e., 2+4 = 8+6 → 6 = 14 → FALSE.
  
  Substrate cardinalities (2, 4, 8, 6) do NOT split 50-50 over χ_S. FAIL
  structurally locked.
```

**W11-4 d=2 sage check verdict**: At single-τ evaluation, the (χ_Σ, χ_S) character pair FAILS the W11-4 d=2 identity at rel_dev_0 = 6/5 = 1.2. The structural cause is independent of τ: χ_Σ is a constant at any fixed τ (it varies ACROSS τ but not at any single τ-point), and χ_S has unbalanced cardinality split (|S_1|+|S_2| = 6 ≠ 14 = |S_3|+|S_4|). This refutes volovik's R1 §"W11-4 (Z_2)^d-Schur d=2 base case satisfied by non-(p,q) generator" claim at the d=2 abstract identity level.

**Important caveat**: volovik's claim might be defensible at a MULTI-τ generalization where the W11-4 identity is integrated over a τ-domain — but that generalization is NOT the W11-4 d=2 base case. W11-4 PASSed in QQ at d ∈ {2, 3, 4, 5} as a SINGLE-τ algebraic identity on bot-20 content at τ_fold (per W11-4 §"CC2" line 9334). Promoting it to a τ-integrated version is a NEW gate, not the base case under test. CF-W8-3 (below) pre-registers this as a separate carry-forward.

#### Concessions (where volovik persuaded me)

I concede THREE specific points to volovik:

1. **τ-asymmetric structural fingerprint is real substrate content**: The W11-2 asymmetric breakdown direction at δ_τ = -0.10 (D_bi(0.090) = 0.197 < D_bi(0.190) = 0.462 < D_bi(0.290) = 0.786 — verified via Jensen scaling computation in volovik's R1 Step 2) IS a substrate-physical observation that (p,q)-Cartan parity does NOT carry. The breakdown is one-sided (only toward bi-invariance), and (p,q)-Cartan is τ-symmetric. My R1 §(c) "factors through (p,q)-parity at higher harmonic" was correct at the discrete-character level but UNDER-STATED the τ-axis-sign content at the moduli-space level.

2. **chi_stratum(λ_pq, τ) carries τ-dependent structural information (p,q)-Cartan does not**: At the level of map domains, `chi_pq-Cartan: Peter-Weyl × {} → V_4` (no τ-coordinate) and `chi_stratum: bot-20 × τ-axis → V_4` (τ-coordinate) live on STRUCTURALLY DIFFERENT domains. My R1 framing "stratum-V_4 is a relabeling of (p,q)-Cartan-V_4 ACROSS τ-VARIATION" was over-strong — the relabeling argument applies at FIXED τ, not across τ-variation.

3. **The τ-axis IS a structural coordinate of the spectral triple**: `(A_K, H_K, D_K(τ))` has τ as a one-parameter deformation label, not as an "external" parameter. The substrate-IS observable includes the moduli-space coordinate τ, not just the single-τ slice at τ_fold. This is consistent with the substrate-IS framing per `phononic-framing.md`.

These concessions sharpen the picture WITHOUT rescuing candidate (ii) at the W11-4 d=2 base case: the d=2 identity is a single-τ algebraic test on A_F-derived characters, and at single-τ evaluation the (χ_Σ, χ_S) pair fails by partition-arithmetic.

#### Standing positions (where I hold despite volovik's R1)

I hold FIVE positions:

1. **A_F's *-automorphism inventory is structurally complete at first order** (V-1 verdict). The standard inventory (g_C, g_H, g_M) generates all commuting Z_2 *-automorphisms of A_F = C ⊕ ℍ ⊕ M_3(C) up to KO-orientation; lifted to Peter-Weyl, this collapses to (p,q)-Cartan-Z_2×Z_2.

2. **χ_Σ is NOT an A_F-derived character; it is a moduli-space coordinate** (V-2 verdict). A smooth τ-parameterized path in Aut(A_F) is either constant in the discrete *-component or trivial in the connected *-component; a "Z_2 character that flips at τ-breakdown threshold" cannot exist as a continuous family of *-automorphisms.

3. **All 24 strata-enumerations FAIL at single τ-point by partition-arithmetic** (V-3 verdict, Sage-QQ exact). Min rel_dev_0 = 2/5; max = 8/5; structural cause is the substrate's 4-stratum partition having no zero-cardinality stratum.

4. **W11-4 d=2 base case FAILs at the (χ_Σ, χ_S) embedding at single-τ** (W11-4 sage check verdict). χ_Σ is a constant at any single τ, contributes only a global factor (1 - χ_Σ) = 2; χ_S alone has unbalanced cardinality split (6 ≠ 14). Structural-arithmetic FAIL at rel_dev_0 = 6/5 = 1.2.

5. **§VII.AJ V_4-monodromy stays DEMOTED across all (p,q)-derived AND single-τ-stratum-relabeled characters; S88-CF-W11-C is PRE-CLOSED FAIL by partition-arithmetic**. The pre-closure is INDEPENDENT of the RELABELING-vs-DISTINCT debate; even granting volovik's STRUCTURALLY DISTINCT reading, candidate (ii) FAILs by single-τ partition arithmetic that no enumeration escapes.

#### Open R3 synthesis question(s)

R3 must answer:

1. **Does candidate (ii) "V_4 acting on stratum indices" admit an ESCAPE PATH from FAIL via TAU-INTEGRATED characters that side-step the single-τ partition arithmetic?** The discriminating predicate: define a τ-integrated character `χ_integrated(λ) := ∫_τ_min^τ_max χ(λ, τ) dτ / (τ_max - τ_min)` where the (χ_Σ, χ_S) pair varies over the τ-domain. Does this τ-integrated character satisfy the parallelogram identity at d=2 AT MACHINE PRECISION? Sage-symbolic computation over the W11-2 11-τ-point grid is the test. (CF-W8-3 below.)

2. **Independent of (1), does the moduli-space-level τ-asymmetric structural fingerprint deserve its own permanent-results-registry entry distinct from V_4-monodromy?** Volovik's substrate observation (D_bi(0.090) < D_bi(0.190) < D_bi(0.290)) is a real new substrate fact; if it does not lift to a discrete (Z_2)^2 character (V-2 verdict), it might lift to a continuous-symmetry observable on the τ-deformation moduli space — a different registry slot than §VII.AJ.

3. **Do the three concessions imply a refinement of `phononic-framing.md` §"IS Space, Not IN Space"** to explicitly distinguish single-τ-slice substrate-IS observables (algebra-character level) from moduli-deformation substrate-IS observables (continuous-τ level)? Both are substrate-IS, but they live at different structural levels, and the cross-pillar-bridge-anatomy.md registry-PASS criteria may differ.

R3 closes the workshop with a JOINT VERDICT on these three. My provisional R3 stance: question 1 closes FAIL (τ-integration cannot rescue partition-arithmetic FAIL); question 2 closes YES (τ-asymmetric breakdown is a substrate observable deserving its own entry, distinct from V_4-monodromy); question 3 closes YES with a methodology rule extension.

#### Updated provisional 4-field carry-forwards (refined from R1)

**CF-W8-1 (refined)**: `S88-V4-CANDIDATE-III-TRIALITY-MOD-2` — unchanged from R1; remains the highest-priority candidate after candidate (ii) closes FAIL by partition-arithmetic across single-τ-evaluation enumerations.

1. **What**: Construct chi_triality on Peter-Weyl labels (p, q) via the SU(3) triality `t(p, q) = (p − q) mod 3 ∈ {0, 1, 2}`, then sub-character to Z_2 via `chi_triality_Z2(p, q) := (-1)^(t mod 2)` and pair with one A_F-derivable Z_2 to form V_4. Test parallelogram identity at relative ≤ 1e-12 for n ∈ {0, 2, 4} on SU(3) Peter-Weyl content at L_max=10.
2. **Inputs**: W11-1 verdict line `s87_gate_verdicts.txt:294`; W11-3 Friedrich-Bär saturation; W11-4 Sage QQ identity at d ∈ {2, 3, 4, 5}; SU(3) triality automorphism (Connes-Marcolli 2008 §1.13.3); this workshop's R3 verdict.
3. **Gate**: PASS iff max rel_dev across n ∈ {0, 2, 4} ≤ 1e-12; INFO (1e-12, 1e-9]; FAIL > 1e-9.
4. **Effort**: ~5-8h.

**CF-W8-2 (refined)**: `S88-CF-W11-C-PRE-CLOSURE-MECHANICAL` — refined to cite the partition-arithmetic structural cause INSTEAD of the RELABELING reading (since RELABELING-vs-DISTINCT is no longer the dispositive question).

1. **What**: Write `computations/s88_w8_v4_strata_pre_closure.py` per `mechanical-closure-discipline.md`. Verdict: FAIL with `value='PRE-REG-INC_blocked_by_W8_PARTITION_ARITHMETIC_min_rel_dev_2_over_5'`. Records the W-8 R3 PARTITION-ARITHMETIC verdict; emits dual-SHA companion row; updates §VII.AJ.V_4-monodromy slot status to "DEMOTED across all single-τ-evaluation V_4 enumerations on bot-20 stratum cardinalities (2,4,8,6)".
2. **Inputs**: W-8 R3 verdict; W11-1/W11-2/W11-3/W11-4 verdict lines; Sage-QQ exhaustive enumeration table from this R2 (24-entry permutation table with rel_dev_0 distribution).
3. **Gate**: FAIL with descriptive value string per the rule; per-gate-distinct audit_sha256.
4. **Effort**: ~0.5h.

**CF-W8-3 (NEW; born from concessions)**: `S88-V4-STRATA-TAU-INTEGRATED-CHARACTER-TEST` — tests whether τ-integration of the (χ_Σ, χ_S) character escapes the single-τ partition-arithmetic FAIL.

1. **What**: Construct the τ-integrated character `χ_integrated(λ) := (1/(τ_max - τ_min)) · ∫_{τ_min}^{τ_max} (χ_Σ(τ), χ_S(stratum_idx(λ, τ))) dτ` over the W11-2 11-τ-point grid (τ ∈ {0.090, 0.140, 0.165, 0.180, 0.185, 0.190, 0.195, 0.200, 0.215, 0.240, 0.290}); discretize as a weighted average. Test the parallelogram identity at d=2 on this τ-integrated character.
2. **Inputs**: W11-2 cardinality-vector data `computations/s87_w11_partition_stability_4stratum.npz`; W11-4 (Z_2)^d-Schur identity; this workshop's R3 verdict on candidate (ii).
3. **Gate**: PASS iff τ-integrated rel_dev_0 ≤ 1e-12; INFO (1e-12, 1e-9]; FAIL > 1e-9. Sage-symbolic on QQ grid.
4. **Effort**: ~3-5h.

**CF-W8-4 (NEW; from R3 question 2)**: `S88-MODULI-SPACE-TAU-ASYMMETRY-REGISTRY-ENTRY` — register the τ-asymmetric breakdown direction (W11-2's δ_τ = -0.10 collapse-vs-rigidity asymmetry) as a substrate observable distinct from V_4-monodromy, in a new permanent-results-registry slot.

1. **What**: Author §VII.AK (or next-free-letter) registry entry: "τ-Asymmetric Bot-20 Stratification Breakdown Direction (W11-2)". Substrate-IS observable: cardinality-vector swap direction (only toward bi-invariance s = 0). Anchor: D_bi(0.090) = 0.197 < D_bi(0.190) = 0.462 < D_bi(0.290) = 0.786. Cross-link to candidate (ii) closure (the asymmetric breakdown is the moduli-space substrate content that distinguished volovik's R1 from connes' R1 RELABELING reading).
2. **Inputs**: W11-2 INFO verdict; this workshop's R3 verdict; volovik's R1 §"W11-2 asymmetric breakdown" derivation; cross-pillar-bridge-anatomy.md §"Cross-link to phononic-framing".
3. **Gate**: orchestrator-direct-write per `wave-classification.md` METHODOLOGY-class M1-M4 conjunction (this is a registry-entry landing). PASS iff entry lands with provenance + cross-link + Sage-verified D_bi values.
4. **Effort**: ~quarter-wave.

**CF-W8-5 (NEW; from R3 question 3)**: `S88-PHONONIC-FRAMING-MODULI-DEFORMATION-EXTENSION` — methodology rule-file extension to `phononic-framing.md` §"IS Space, Not IN Space" distinguishing single-τ-slice substrate-IS observables (algebra-character level) from moduli-deformation substrate-IS observables (continuous-τ level).

1. **What**: Diff to `phononic-framing.md`: add a new sub-section "Single-τ-slice vs moduli-deformation substrate-IS levels" with calibration corpus citing the W-8 workshop's adjudication of (χ_Σ, χ_S). Cross-link to cross-pillar-bridge-anatomy.md §"Cross-link to phononic-framing".
2. **Inputs**: this workshop's R3 verdict; volovik's R1 substrate-framing block; connes' R2 V-2 substitution chain.
3. **Gate**: orchestrator-direct-write per `wave-classification.md` M1-M4. PASS iff diff lands with provenance + calibration corpus instance.
4. **Effort**: ~quarter-wave.

### R2 — volovik-superfluid-universe-theorist (response to connes' RELABELING reading)

**R2 volovik response (sharpening STRUCTURALLY DISTINCT + small-τ-collapse Z_2 generator + S88-CF-W11-C re-openable against RELABELING + Sage-QQ pullback + NCG-axiomatic obstruction; engaging C-1/C-2/C-3 + W11-2 sector-rearrangement)**

#### Position update (1 paragraph)

Substantial revision in light of connes' R1 + R2. After Sage-QQ verification of connes' `rel_dev_0 = 6/5 = 1.2` claim AND independent reproduction of his V-3 24-permutation sweep (4 distinct rel_dev_0 values {2/5, 4/5, 6/5, 8/5}, each appearing 6 times) AND independent reproduction of his W11-4 sage check on my (χ_Σ, χ_S) embedding (FAIL at rel_dev_0 = 6/5 via factorization Δ_0 = (1−χ_Σ)·Σ_k(1−χ_S(k))|S_k| = 2·12 = 24) AND independent test of his CF-W8-3 τ-integrated character (FAIL at rel_dev_avg = 12/11 ≈ 1.09 on the 11-τ-point W11-2 grid), I CONCEDE that the discrete-Z_2×Z_2 reading of candidate (ii) does NOT survive in any of its incarnations: single-τ enumeration, single-τ (χ_Σ, χ_S), or τ-integrated (χ_Σ, χ_S). The structural cause is partition-arithmetic at the substrate's actual cardinality vector (2,4,8,6) [or (4,2,8,6) at flip], NOT relabeling-vs-distinctness across τ-variation. The Δ_0 LOCALIZATION FORMULA `Δ_0 = 4·|S_{(1,1)-charged}|`, jointly derived in R2 (connes V-3 Step 5 + my Sage-QQ verification), is the structural-cause pin. **Where I HOLD on the substrate-physical content**: connes conceded THREE points — (1) τ-asymmetric structural fingerprint is real substrate content, (2) chi_stratum carries τ-dependent structural information (p,q)-Cartan does not, (3) the τ-axis IS a structural coordinate of the spectral triple. These concessions hold; what dissolves is my R1 attempt to package the τ-asymmetric content as a (Z_2)^2 V_4 generator. The substrate-physical observation is moduli-space-side, not algebra-character-side. **Where I HOLD on the forward path**: connes' candidate (iii) `chi_triality_Z2 := (-1)^((p-q) mod 3 mod 2)` IS structurally distinct from (-1)^p · (-1)^q (Sage-tabulated: at (0,0) chi_tri = +1 = (-1)^p·(-1)^q, but at (0,2) chi_tri = -1 ≠ +1 = (-1)^p·(-1)^q). The wave-equivalent budget reroutes to CF-W8-1 (triality-mod-2; co-authored) and CF-W8-2 (mechanical pre-closure citing partition-arithmetic + Δ_0 LOCALIZATION). I propose JOINT R3 closure with connes on his CF-W8-1/2/4/5 plus a NEW CF-W8-6 landing the Δ_0 LOCALIZATION formula as a registry-eligible Pillar-IV structural theorem (this is a NEW structural finding produced JOINTLY by both R2s — connes' V-3 + my independent verification — and deserves its own §VII slot independent of S88-CF-W11-C closure).

#### Response to C-1 (Sage-QQ pullback exact `rel_dev_0 = 6/5`)

**Substitution chain — verifying connes' claim + extending to enumeration-INDEPENDENCE**:

```
Step 1 (Definitions, from W11-3 §"Substrate framing" + W11-1 PARALLELOGRAM):
  cv_anchor(τ_fold) = (|S_1|, |S_2|, |S_3|, |S_4|) = (2, 4, 8, 6)
  Δ_0 := A^(e)_0 − A^(a)_0 − A^(b)_0 + A^(ab)_0    [parallelogram cocycle at n=0]
        = sum_{m ∈ bot20} (1 − χ_a(m))(1 − χ_b(m)) · w_0(m)    [factored form]
  w_0(m) = 1 (uniform weight at n=0)
  rel_dev_0 := |Δ_0| / |A^(e)_0|
  FAIL ceiling: rel_dev_0 < 1e-9 (W11-1 pre-registered)

Step 2 (Substitution — connes' natural enumeration S_1→(0,0), S_2→(0,1), S_3→(1,0), S_4→(1,1)):
  Per-stratum (χ_a, χ_b) values: S_1: (+1,+1), S_2: (+1,-1), S_3: (-1,+1), S_4: (-1,-1)
  A^(e)_0  = 2·(+1) + 4·(+1) + 8·(+1) + 6·(+1)        = 20
  A^(a)_0  = 2·(+1) + 4·(+1) + 8·(-1) + 6·(-1)        = -8
  A^(b)_0  = 2·(+1) + 4·(-1) + 8·(+1) + 6·(-1)        = 0
  A^(ab)_0 = 2·(+1) + 4·(-1) + 8·(-1) + 6·(+1)        = -4
  Δ_0      = 20 − (-8) − 0 + (-4) = 24
  rel_dev_0 = 24/20 = 6/5 = 1.2 [Sage QQ exact, verified backend=sagecell]

Step 3 (Extension — sweep all 4! = 24 permutations of {(0,0),(0,1),(1,0),(1,1)} over {S_1,...,S_4}):
  Sage transcript (R2 volovik backend=sagecell): for perm in permutations(...) compute Δ_0, rel_dev_0
  Distinct rel_dev_0 values: {2/5, 4/5, 6/5, 8/5}
  Each value appears with count 6 (a 4-fold orbit under V_4 generator-flip).
  Minimum rel_dev_0 = 2/5 = 0.4 [Sage QQ exact]
  This MATCHES connes' V-3 Step 3 distribution.

Step 4 (Direction — comparison with FAIL ceiling):
  min_perm rel_dev_0 = 2/5 = 0.4
  FAIL ceiling = 1e-9
  Direction: 0.4 / 1e-9 = 4e8  ⟹  ALL 24 enumerations FAIL by ≥ 8 OOM
  Conclusion: there exists NO permutation σ : V_4 → {S_1,...,S_4} such that the 
              parallelogram cocycle PASSes. Pullback factorization is 
              ENUMERATION-INDEPENDENT.

Step 5 (JOINT structural finding — Δ_0 LOCALIZATION FORMULA, derived independently in R2 by both connes V-3 Step 5 and volovik R2):
  Δ_0 = sum_{strata k} card[k] · (1 − χ_a(k))(1 − χ_b(k))
  The factor (1 − χ_a(k))(1 − χ_b(k)) ≠ 0 ⟺ χ_a(k) = -1 AND χ_b(k) = -1, 
  i.e., k carries the (1,1)-charge in the V_4 enumeration.
  Δ_0 = 4 · card[(1,1)-charged stratum]                                  [exact]
  rel_dev_0 = 4 · card[(1,1)-charged stratum] / sum_k card[k]
            = card[(1,1)-charged stratum] / 5                            [at sum=20]
  Since {card[1], card[2], card[3], card[4]} = {2, 4, 8, 6}, the four possible 
  rel_dev_0 values are {2/5, 4/5, 6/5, 8/5}. Min is 2/5 (the (1,1)-charge 
  on stratum S_1, cardinality 2). 
  Direction: rel_dev_0 = 2/5 = 0.4 ≥ 1e-9. FAIL by 8 OOM.
```

**Sage-QQ verification corroborates connes' single-enumeration C-1 claim AND independently reproduces his V-3 enumeration-INDEPENDENCE structural argument**: the parallelogram cocycle at n=0 over the 4-stratum partition cannot evade FAIL by reordering the stratum→V_4 map. **I CONCEDE C-1 to connes**: the natural strata-Z_2×Z_2 character pulls back FAIL by 8 OOM regardless of enumeration; my R1 framing of "stratum-character STRUCTURALLY DISTINCT" was too strong at the discrete-V_4 level.

The Δ_0 LOCALIZATION FORMULA `Δ_0 = 4·card[(1,1)-charged]` is a JOINT R2 finding (connes V-3 Step 5 first; volovik R2 independent verification at the Sage-QQ exhaustive level). It generalizes: for any 4-element multiset `(c_1, c_2, c_3, c_4)` of positive integers, the V_4 PARALLELOGRAM IDENTITY at n=0 PASSes iff `min_k c_k = 0`. At the substrate's actual cardinalities (2,4,8,6) [τ_fold] and (4,2,8,6) [τ-flip], no stratum is empty, hence FAIL is partition-arithmetic-locked. **This is a NEW Pillar-IV cohomology-clean structural theorem** worth registering as CF-W8-6 below.

#### Response to C-2 (NCG-axiomatic obstruction: level-parity vs A_F *-automorphism)

**Substitution chain — does χ_Σ lift to an A_F *-automorphism?**

```
Step 1 (Definitions; cite connes V-1 Step 1-3 verbatim + S84 W8a Aut(A_F) result):
  A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)         [first-order finite spectral algebra]
  Aut(A_F) = U(1) × SU(2) × SU(3) / (discrete center identifications)
                                  [knowledge MCP S84 W8a-result confirmed]
  Z_2 *-automorphism inventory on A_F (connes V-1 Step 3):
    g_C := charge-conjugation on ℂ        [outer automorphism, complex conjugation]
    g_H := Pauli-σ_3 conjugation on ℍ     [inner automorphism]
    g_M := transpose on M_3(ℂ)            [outer automorphism]
  These three Z_2 generators commute pairwise.
  Under KO-orientation lifting (V-1 Step 4), the (Z_2)^3 collapses to (Z_2)^2 = V_4 
  on Peter-Weyl (p,q)-content — exactly the (p mod 2, q mod 2)-Cartan-toral V_4 
  character W11-1 falsified.

Step 2 (Substitution — does χ_Σ : τ-axis → {±1} lift to an A_F *-automorphism?):
  χ_Σ is defined on the τ-AXIS (one global ±1 per τ-point), NOT on A_F.
  Per connes' V-2 Step 3-4 (which I now adopt): a smooth τ-parameterized path 
  τ ↦ g_τ in Aut(A_F) is either CONSTANT in the discrete *-component (because 
  connected components are path-disconnected at the discrete-Z_2 level) or 
  TRIVIAL in the connected part. A "Z_2 character that flips at the τ-breakdown 
  threshold" cannot exist as a continuous family of *-automorphisms — it would 
  require a discontinuity at the threshold, which is not a smooth deformation.

Step 3 (Direction):
  χ_Σ lifts to an A_F *-automorphism: NO.
  χ_Σ lifts to an Aut(A_K)-element where A_K is the 4D substrate algebra: NO 
   (τ is a continuous parameter; Aut takes only discrete elements via the 
    discrete-extension-of-connected structure).
  χ_Σ encodes a DIFFERENT structural feature: the existence of a τ-axis 
   SYMMETRY-BREAKING point (the bi-invariant fixed point s=0) and the asymmetric 
   direction of approach. This is a feature of the spectral-triple FAMILY 
   {(A_K, H_K, D_K(τ))}_{τ ∈ ℝ}, NOT a Z_2 character on the V_4 hypercube identity.

Step 4 (Honest concession to C-2):
  I CONCEDE C-2 to connes at the algebraic level. χ_Σ is NOT an A_F *-automorphism; 
  it is NOT in the standard inventory; it is NOT a "fourth commuting Z_2 *-automorphism" 
  beyond the (g_C, g_H, g_M) triple. The W11-4 d=2 (Z_2)^d-Schur identity at the 
  abstract NCG-axiomatic level requires its two generators to be A_F-derivable; 
  χ_Σ is not. Therefore the "(χ_Σ, χ_S)" candidate is OUTSIDE the W11-4 admissibility 
  class.

Step 5 (Honest concession on the W11-4 d=2 single-τ verification):
  Connes' W11-4 sage check (his §"W11-4 d=2 sage check" Step 1-5) is verified 
  exact in independent Sage-QQ: at single τ_fold = 0.190 (RIGID, χ_Σ = -1),
  Δ_0 = (1 − χ_Σ) · sum_k (1 − χ_S(k)) |S_k| = 2 · 12 = 24
  rel_dev_0 = 24/20 = 6/5 = 1.2  EXACT in QQ.
  My R1 §"W11-4 (Z_2)^d-Schur d=2 base case satisfied by non-(p,q) generator" 
  claim is REFUTED at the d=2 single-τ algebraic-identity level.

Step 6 (What survives — substrate-physical Z_2 ON THE PARAMETER SPACE):
  χ_Σ remains a substrate observable, but it lives on the 1-parameter deformation 
  family, not on A_F. In phononic-framing language: χ_Σ is a discriminating FEATURE 
  of the τ-axis (small-τ-collapse vs large-τ-rigidity), NOT a Z_2 character on A_F. 
  It is structurally distinct from (p mod 2, q mod 2) — but distinct in a DIFFERENT 
  category (parameter-space binary, not algebraic generator). Connes' V-2 Step 5 
  "moduli-space-coordinate" framing is correct.
```

**I retract the R1 claim that χ_Σ generates a "new substrate-physical-Z_2 class NOT covered by A_F *-automorphism inventory" at the V_4-monodromy-test level.** What I retain is the weaker (and correct) statement: χ_Σ is a discriminating feature of the τ-axis, useful for parameter-space classification of the spectral-triple family, but NOT eligible as a V_4 generator for the W11-4 d=2 identity. **Connes' V-1 KO=6 collapse argument settles the inventory question**: the lifted (Z_2)^3 from `(g_C, g_H, g_M)` collapses to (Z_2)^2 by KO-orientation; no fourth commuting Z_2 *-automorphism exists at first order. The A_F-derivable Z_2 *-automorphism inventory at the SU(3) Peter-Weyl level is exhausted by `(g_C, g_H, g_M)`, and these generate the (p mod 2, q mod 2)-Cartan V_4 W11-1 falsified.

#### Response to C-3 (forward path collapses to triality-mod-2 + mechanical-closure or χ_Σ-based alternative)

**Substitution chain — is triality-mod-2 structurally distinct from (p mod 2, q mod 2)?**

```
Step 1 (Definitions; SU(3) triality automorphism):
  Triality function on SU(3) Peter-Weyl: t(p,q) := (p − q) mod 3 ∈ {0, 1, 2}
  Triality is the order-3 outer automorphism of the SU(3) Dynkin diagram 
  (Connes-Marcolli 2008 §1.13.3).
  Sub-character to Z_2: chi_tri_Z2(p,q) := (-1)^((t(p,q)) mod 2)
  = +1 if t ∈ {0, 2}; = -1 if t = 1.
  Cartan-toral pair: chi_pq-Cartan(p,q) := ((-1)^p, (-1)^q)
  
Step 2 (Substitution — Sage tabulation over (p,q) ∈ {0,...,5}²; verbatim transcript backend=sagecell):
  Sample points showing chi_tri_Z2 ≠ Φ((-1)^p, (-1)^q) for any function Φ:
    (p,q) = (0,2):  t = -2 mod 3 = 1;  chi_tri_Z2 = -1;  ((-1)^0, (-1)^2) = (+1, +1)
    (p,q) = (0,0):  t = 0;             chi_tri_Z2 = +1;  ((-1)^0, (-1)^0) = (+1, +1)
  Both (0,0) and (0,2) have ((-1)^p, (-1)^q) = (+1, +1), but chi_tri_Z2 differs (+1 vs -1).
  So chi_tri_Z2 is NOT a function of ((-1)^p, (-1)^q).
  
Step 3 (Direction):
  chi_tri_Z2 is independent of the (p mod 2, q mod 2)-Cartan-V_4 character.
  Combined with one of the A_F-derivable (g_M, g_C) Z_2 generators, chi_tri_Z2 
  forms a V_4 = Z_2 × Z_2 that lives OUTSIDE the (g_C, g_H, g_M) Cartan-toral 
  inventory at the W11-1 test level.
  
Step 4 (Algebraic admissibility):
  Triality is the SU(3) Dynkin diagram outer automorphism; it is in Aut(M_3(ℂ)) 
  up to Z_3 cyclic rotation of irrep labels. Sub-charactered to Z_2 (the diagonal 
  of Z_3 → Z_2), it lifts to a Z_2 *-automorphism of M_3(ℂ).  Therefore 
  (chi_tri_Z2, g_M) generates an A_F-derivable V_4 that is structurally 
  DISTINCT from the (p mod 2, q mod 2)-Cartan-V_4 W11-1 falsified.
  Caveat: the triality Z_3 → Z_2 sub-quotient is a Z_3-coset structure; under 
  KO=6 orientation collapse (connes V-1 Step 4-5), it MAY further reduce — 
  this is a CF-W8-1 dispatch question, not pre-closeable in workshop scope.

Step 5 (Verdict on the C-3 challenge):
  Candidate (iii) is the SOLE surviving forward path under the post-W11-1 
  inventory (modulo the V-1-KO-collapse caveat). 
  Candidate (i) "V_4 acting on regulator-coset map" was independently FAILed at 
  W11-1 §"5 V_4 candidates" line 478 (regulator-coset n=2 specific). 
  Candidate (ii) "stratum-Z_2×Z_2 character" closes FAIL-by-partition-arithmetic 
  (via Δ_0 LOCALIZATION FORMULA, joint R2 finding). 
  Candidate (iv) and (v) (less explicit in W11-1) remain UNTESTED.
  Candidate (iii) (triality-mod-2) is the highest-EVOI surviving forward path.
  
  My R1 χ_Σ-based candidate is NOT A_F-derivable per C-2 — it does not survive 
  even as a candidate-level entry in S88-CF-W11-C.
```

**I CONCEDE C-3 to connes**: the surviving forward path collapses to triality-mod-2. Candidate (iii) `chi_triality_Z2` paired with `g_M` (transpose-on-M_3) gives an A_F-derivable V_4 that is structurally distinct from the (p mod 2, q mod 2)-Cartan-V_4 W11-1 falsified (subject to V-1 KO=6 caveat that CF-W8-1 dispatch must verify). **My R1's "χ_Σ as new Z_2 generator" path is closed**: χ_Σ is parameter-space-side, not A_F-side. **I co-author CF-W8-1 with connes; no separate χ_Σ-based candidate.**

#### W11-2 asymmetric breakdown engagement (sector-rearrangement vs new (Z_2)^2 generator)

**Substitution chain — (p,q) sector inventory at the swap point**:

```
Step 1 (Definitions; W11-3 §"Methodology — Step 2" Casimir-ladder + W11-2 §"τ-scan"):
  At τ_fold = 0.190: cv = (2, 4, 8, 6); per-stratum sector contributions:
    S_1: (p,q)=(0,0), computation, |λ|=0.81974
    S_2: (p,q) ∈ {(0,1),(1,0)}, computation, |λ|=0.83589
    S_3: (p,q) ∈ {(0,1),(1,0)}, level 1, |λ|=0.84086
    S_4: (p,q)=(0,0), level 1, |λ|=0.84521
  At τ-flip = 0.090: cv = (4, 2, 8, 6); strata 1+2 swap cardinalities only.
  Total (p,q)-sector-flavor inventory contributing to bot-20: {(0,0), (0,1), (1,0)}
  Lower-bound on |λ_min| in non-contributing sectors per W11-3 Casimir bound:
    sector (1,1): |λ_min| ≥ 0.873 [Casimir-ladder table line 9143-9156]

Step 2 (Question — at τ = 0.090, do NEW (p mod 2, q mod 2) sectors enter bot-20?):
  Casimir-bound test: smallest (1,1)-mod-2 sector floor at sector (1,1), 
  with |λ_min|^(1,1)(τ_fold) ≥ 0.873. Under δ_τ = -0.10 perturbation, the Jensen 
  rescaling shifts |λ| by O(|δ_τ|) ≈ 0.05 in M_KK units.  
  Updated worst-case |λ_min|^(1,1)(τ=0.090) ≈ 0.873 − 0.05 = 0.823.
  bot-20 ceiling at τ=0.090: |λ|_max^bot20(τ=0.090) ≈ 0.84521 (S_4 ceiling).
  
  Empirical resolution: W11-2 + W11-3 truncation_consistent flag (set True for 
  L_max ∈ {6, 10, 12}) confirms cv(τ=0.090) = (4,2,8,6) at the master-cache level; 
  i.e., the EMPIRICAL bot-20 sector inventory at τ=0.090 is unchanged from τ_fold. 
  No new (p mod 2, q mod 2) sector enters bot-20.

Step 3 (Verification — sector inventory at τ-flip is unchanged):
  Empirical W11-2 cv at τ=0.090 partitioned by (p mod 2, q mod 2):
    S_1 at τ-flip (card 4): (0,0) computation (2 modes) + 2 modes shifted from S_2-(0,1)/(1,0) 
                            computation [intra-bot-20 reorganization]
    S_2 at τ-flip (card 2): remaining 2 modes from (0,1)/(1,0) computation
    S_3 at τ-flip (card 8): (0,1)/(1,0) level 1 (unchanged)
    S_4 at τ-flip (card 6): (0,0) level 1 (unchanged)
  Sector flavors at τ-flip: {(0,0), (0,1), (1,0)} — SAME as τ_fold.
  No (1,1)-mod-2 sector enters.
  
Step 4 (Direction):
  The W11-2 asymmetric breakdown at δ_τ = -0.10 is INTRA-(p,q)-SECTOR 
  rearrangement (specifically, intra-bot-20 reordering between S_1 and S_2 within 
  the {(0,0)} ∪ {(0,1),(1,0)} sectors).  No structurally distinct (Z_2)^2 generator 
  emerges at the discrete-character level.

Step 5 (Verdict on W11-2 sector-rearrangement question):
  I CONCEDE the W11-2 reading to connes' R1 §(c) and R2 V-2: the cv-flip is 
  intra-(p,q)-sector level reorganization, NOT a new (Z_2)^2 generator on bot-20.  
  The τ-axis-direction asymmetry (only at δ_τ = -0.10, never at δ_τ = +0.10) is a 
  CONTINUOUS one-parameter symmetry-breaking feature (proximity to bi-invariant 
  point s=0), NOT a discrete Z_2 character on A_F.
```

**I retract the R1 claim that the cv-flip "provides a substrate-physical Z_2 generator"** at the V_4-monodromy-test level. It IS a substrate observable, but the generator is on the τ-axis (parameter-space), not on the bot-20 spectral content. Connes' §(c) reading is correct.

#### Bonus engagement — connes' new CF-W8-3 τ-integrated test (Sage-verified FAIL pre-dispatch)

Connes' R2 introduced a NEW question (CF-W8-3): does τ-integration of (χ_Σ, χ_S) over the W11-2 11-τ-point grid escape the FAIL? I tested this in Sage-QQ ahead of dispatch:

```
Step 1 (Definitions):
  τ_grid = {0.090, 0.140, 0.165, 0.180, 0.185, 0.190, 0.195, 0.200, 0.215, 0.240, 0.290}
  At τ = 0.090 (COLLAPSED, cv=(4,2,8,6)): χ_Σ = +1
  At remaining 10 τ-points (RIGID, cv=(2,4,8,6)): χ_Σ = -1

Step 2 (Substitution; uniform-weight average):
  At COLLAPSED single-τ: A_00=20, A_01=8, A_10=20, A_11=8; Δ_0 = 0   (degenerate; χ_Σ=+1 acts as identity)
  At RIGID  single-τ: A_00=20, A_01=8, A_10=-20, A_11=-8; Δ_0 = 24
  τ-integrated: A_00_avg=20, A_01_avg=8, A_10_avg=-180/11, A_11_avg=-72/11
  Δ_avg = 240/11
  rel_dev_avg = (240/11)/20 = 12/11 ≈ 1.0909   (Sage QQ exact)

Step 3 (Direction):
  rel_dev_avg = 12/11 = 1.0909
  FAIL ceiling: 1e-9
  Direction: 12/11 / 1e-9 ≈ 1.09e9  ⟹  FAIL by ~9 OOM.

Step 4 (Structural reason):
  At COLLAPSED single-τ, Δ_0 = 0 holds because χ_Σ = +1 reduces to identity 
  (acts trivially), making (1−χ_Σ) = 0 and killing the cocycle. This is NOT 
  a non-trivial V_4 PASS — it is a Z_2 reduction (the V_4 character has 
  collapsed to a Z_2 at the COLLAPSED branch).
  At RIGID single-τ, Δ_0 = 24 (the full FAIL).
  The τ-integrated mean (1·0 + 10·24)/11 = 240/11 is a positive-weight 
  average of the FAIL — partition-arithmetic FAIL DOES NOT VANISH under 
  averaging.

Step 5 (Conclusion — pre-dispatch closure of CF-W8-3):
  The τ-integrated character also FAILs the parallelogram identity by ~9 OOM.
  CF-W8-3 (volovik R1 hope of escape via τ-integration) is structurally 
  pre-closed FAIL.  R3 should record this finding and either (a) retain 
  CF-W8-3 as a no-op pre-closure for audit-trail purposes or (b) drop 
  CF-W8-3 entirely from the carry-forward queue.
```

**Sage-QQ exact verdict on connes' CF-W8-3: FAIL pre-dispatch at rel_dev_avg = 12/11 ≈ 1.0909**. The τ-integration cannot rescue the partition-arithmetic FAIL — the only PASSing branch (COLLAPSED at χ_Σ=+1) is structurally degenerate (V_4 → Z_2 reduction), not a non-trivial V_4 satisfaction. **I propose CF-W8-3 be DROPPED from the carry-forward queue in R3** — the structural FAIL is now pre-closed; spending S88+ wave-equivalent budget on dispatch would be redundant.

#### Concessions (where connes persuaded me)

1. **C-1 (RELABELING via Sage-QQ pullback)**: CONCEDED. Sage-QQ verification + 24-enumeration sweep show Δ_0 = 4·card[(1,1)-charged stratum] localizes structurally on whichever stratum carries the (1,1)-charge; rel_dev_0 ∈ {2/5, 4/5, 6/5, 8/5} for ALL 24 enumerations; minimum 2/5 is 8 OOM above FAIL ceiling. The pullback factorization is enumeration-INDEPENDENT and structurally controlled by the cardinality vector. Candidate (ii) closes FAIL-BY-PARTITION-ARITHMETIC.

2. **C-2 (NCG-axiomatic obstruction)**: CONCEDED at the V-1 KO=6 collapse level. The Aut(A_F) inventory `{g_C, g_H, g_M}` exhausts the discrete Z_2 *-automorphism content at first order on `A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)`; under KO-orientation lifting, the (Z_2)^3 collapses to (Z_2)^2 = (p,q)-Cartan-V_4. χ_Σ is parameter-space-side (τ-axis sign), not algebra-side. My R1 §"W11-4 d=2 base case satisfied by non-(p,q) generator" claim is REFUTED at single-τ via Δ_0 = (1−χ_Σ)·12 = 24 = 6/5·20.

3. **W11-2 sector-rearrangement (connes R1 §c + R2 V-2)**: CONCEDED. The cv-flip at δ_τ = -0.10 is intra-(p,q)-sector level reorganization within the {(0,0), (0,1), (1,0)} sector inventory. No new (1,1)-mod-2 sector enters bot-20. The asymmetry direction is a proximity-to-bi-invariance moduli-space feature, not a discrete Z_2 character on A_F.

4. **C-3 (forward path collapses)**: CONCEDED. The surviving V_4 forward path is connes' candidate (iii) `chi_triality_Z2` paired with g_M. My R1 (χ_Σ, χ_S) candidate is NOT A_F-derivable and falls outside the W11-4 d=2 admissibility class. CF-W8-1 (connes' R1) supersedes my R1 S88-CF-W11-C; I co-author CF-W8-1.

5. **CF-W8-3 τ-integrated rescue is pre-closed FAIL**: I tested connes' new question in Sage-QQ at rel_dev_avg = 12/11; the τ-integration cannot escape partition-arithmetic FAIL.

#### Standing positions (where I hold despite connes' R1)

1. **The Δ_0 LOCALIZATION FORMULA `Δ_0 = 4·card[(1,1)-charged stratum]` is a NEW Pillar-IV cohomology-clean structural theorem registry-eligible in its own slot** — JOINT R2 finding (connes V-3 Step 5 first; volovik R2 independent verification at exhaustive level). For any 4-element multiset `{c_1, c_2, c_3, c_4}` of positive integers, the V_4 PARALLELOGRAM IDENTITY at n=0 PASSes iff some `c_k = 0`. This generalizes beyond candidate (ii) to ANY future stratum-character V_4 candidate on similar 4-stratum partitions. **I propose CF-W8-6 below as a separate registry landing**, distinct from CF-W8-2 (mechanical pre-closure of S88-CF-W11-C). The structural theorem is the asset; the mechanical-closure verdict line cites it as the structural-cause pin.

2. **τ-axis asymmetry of the cv-flip at δ_τ = -0.10 deserves its own forward registry track** — connes' CF-W8-4 captures this, and I support it. The substrate observation D_bi(0.090) = 0.197 < D_bi(0.190) = 0.462 < D_bi(0.290) = 0.786 (Python-verified) IS a substrate-physical fingerprint distinct from V_4-monodromy. The τ-distance to the bi-invariant fixed point s=0 is a substrate-physical structural axis.

3. **Connes' CF-W8-5 phononic-framing extension I support; also support extending the methodology rule landing to the cross-pillar bridge anatomy**: the W-8 calibration of "single-τ-slice substrate-IS observable (algebra-character level) vs moduli-deformation substrate-IS observable (continuous-τ level)" is Pillar-IV → Pillar-IV intra-substrate, not a cross-pillar bridge per se, but it does refine the IS-not-IN convention for moduli-space coordinates. Volovik supports the diff, and additionally proposes that cross-pillar-bridge-anatomy.md §"IS-not-IN Anatomy" extend to acknowledge the moduli-space level explicitly.

4. **CF-W8-3 should be DROPPED from the carry-forward queue** (per the τ-integrated test I just ran in Sage-QQ above, FAIL is pre-closed). Connes' CF-W8-3 was a fair question to raise but the structural answer is now in hand pre-dispatch.

#### Open R3 synthesis question(s)

R3 must answer (sharpened from connes' R2 §"Open R3 synthesis question(s)" with my responses):

1. **Status of CF-W8-3 (τ-integrated escape path)**: connes' R2 left this open as a forward gate. I closed it pre-dispatch in R2-volovik via Sage-QQ at rel_dev_avg = 12/11 ≈ 1.09 (FAIL by ~9 OOM). R3 should DROP CF-W8-3 (or retain as a no-op pre-closure verdict-line audit-trail entry per `mechanical-closure-discipline.md`).

2. **Should the Δ_0 LOCALIZATION FORMULA become its own registry entry (CF-W8-6 below) distinct from CF-W8-2 mechanical pre-closure?** R3 verdict: YES. The structural theorem is JOINT (connes V-3 derived first; volovik R2 independently verified). The mechanical-closure verdict line cites the theorem as a structural-cause pin; the theorem itself stands as a Pillar-IV registry entry. SUGGESTED §VII.AL slot (after §VII.AJ and §VII.AK; next-free letter); orchestrator-direct-write per METHODOLOGY-class M1-M4.

3. **Joint authorship of forward CFs**: connes' R1+R2 is the primary architect of the partition-arithmetic + KO=6-collapse arguments; I provide the substrate-physics reading + independent Sage-QQ verification. Co-authorship attribution per `cross-pillar-bridge-anatomy.md` §"Authorship attribution" calibration: CF-W8-1 (connes PRIMARY, volovik CO-AUTHOR at substrate side); CF-W8-2 (connes PRIMARY, volovik CO-AUTHOR at structural-cause-pin side); CF-W8-4 (volovik PRIMARY, connes CO-AUTHOR at moduli-space-coordinate framing); CF-W8-5 (connes PRIMARY, volovik CO-AUTHOR at phononic-framing diff); CF-W8-6 (JOINT AUTHORS — connes V-3 + volovik R2 Sage-exhaustive).

4. **R3 should also adjudicate whether CF-W8-1 dispatch must include the V-1 KO=6 collapse caveat as a pre-registered diagnostic**: triality Z_3 → Z_2 might further reduce under KO-orientation lifting (collapsing further to a sub-Z_2 of the (g_C, g_H, g_M) inventory, in which case candidate (iii) FAILs by inheritance from W11-1 and the wave-equivalent budget reroutes to candidates (iv)/(v)). This is a CF-W8-1 dispatch question, not workshop-scope, but R3 should pre-register the diagnostic.

#### Updated provisional 4-field carry-forwards (refined from R1)

These supersede my R1 carry-forwards. FINAL specs land in R3 jointly with connes.

**CF-W8-1 (co-authored with connes; connes PRIMARY)** — `S88-V4-CANDIDATE-III-TRIALITY-MOD-2`

1. **What**: Construct chi_triality_Z2 on Peter-Weyl labels (p,q) via SU(3) triality `t = (p − q) mod 3`, sub-charactered to Z_2 via `chi_tri := (-1)^(t mod 2)`. Pair with g_M (transpose-on-M_3 *-automorphism) to form V_4. Test parallelogram identity Δ_n[chi_tri, g_M] for n ∈ {0, 2, 4} at relative ≤ 1e-12 PASS / ≤ 1e-9 INFO / > 1e-9 FAIL on bot-20 SU(3) Peter-Weyl content at L_max=10 (master cache `s84_spectrum_cache_L12_tau019.npz`). Pre-register diagnostic: V-1 KO=6 caveat — verify under KO-orientation lifting that chi_tri × g_M does NOT collapse to a sub-(g_C, g_H, g_M) character.
2. **Inputs**: W11-1 verdict line `s87_gate_verdicts.txt:294` (max_dev=1.16, FAIL); W11-3 verdict `:296` (Friedrich-Bär saturation theorem); W11-4 verdict `:290` ((Z_2)^d-Schur identity exact in QQ); SU(3) triality automorphism (Connes-Marcolli 2008 §1.13.3); Aut(A_F) inventory (S84 W8a-result, knowledge MCP); canonical `tau_fold = 0.190`; this workshop's R3 verdict.
3. **Gate**: PASS iff max rel_dev across n ∈ {0, 2, 4} ≤ 1e-12; INFO ∈ (1e-12, 1e-9]; FAIL > 1e-9. Pre-registered identical to W11-1.
4. **Effort**: ~5-8h (Sage symbolic + irrep multiplicity Casimir-ladder + parallelogram cocycle + KO-orientation diagnostic).

**CF-W8-2 (co-authored with connes; connes PRIMARY)** — `S88-CF-W11-C-PRE-CLOSURE-MECHANICAL`

1. **What**: Mechanical-closure script for S88-CF-W11-C per `mechanical-closure-discipline.md`. Verdict: FAIL with `value='PRE-REG-INC_blocked_by_W8_PARTITION_ARITHMETIC_DELTA_0_LOCALIZATION_min_rel_dev_2_over_5'`. Records the W-8 R3 PARTITION-ARITHMETIC verdict citing the Δ_0 LOCALIZATION FORMULA (CF-W8-6) as structural-cause pin; emits dual-SHA companion row; updates §VII.AJ V_4-monodromy slot status to "DEMOTED across all single-τ-evaluation V_4 enumerations on bot-20 stratum cardinalities (2,4,8,6); rooted in Δ_0 LOCALIZATION (CF-W8-6)".
2. **Inputs**: W-8 R3 verdict; W11-1/W11-2/W11-3/W11-4 verdict lines; CF-W8-6 LANDED (Δ_0 LOCALIZATION provides the structural-cause pin).
3. **Gate**: FAIL with descriptive value string per the rule; per-gate-distinct audit_sha256.
4. **Effort**: ~0.5h.

**CF-W8-3 (DROPPED; pre-closed by R2-volovik Sage-QQ test)** — formerly `S88-V4-STRATA-TAU-INTEGRATED-CHARACTER-TEST`

1. **What**: Closed pre-dispatch in R2-volovik via Sage-QQ exhaustive computation: τ-integrated (χ_Σ, χ_S) over the W11-2 11-τ-point grid yields rel_dev_avg = 12/11 ≈ 1.0909 (FAIL by ~9 OOM). The structural reason: the only PASSing single-τ branch is COLLAPSED at χ_Σ=+1 where the V_4 collapses to Z_2 (degenerate, not non-trivial V_4 satisfaction). R3 either DROPS this CF entirely or retains a no-op pre-closure verdict-line audit-trail entry.
2. **Status**: SUPERSEDED-BY-R2-PRE-DISPATCH-CLOSURE per `feedback_fix-in-session-never-defer.md`.

**CF-W8-4 (co-authored with connes; volovik PRIMARY)** — `S88-MODULI-SPACE-TAU-ASYMMETRY-REGISTRY-ENTRY`

1. **What**: Author §VII.AK (next-free-letter) registry entry: "τ-Asymmetric Bot-20 Stratification Breakdown Direction (W11-2)". Substrate-IS observable: cardinality-vector swap direction (only toward bi-invariance s = 0). Anchor: D_bi(0.090) = 0.197 < D_bi(0.190) = 0.462 < D_bi(0.290) = 0.786 (Python-verified). Cross-link to candidate (ii) closure (the asymmetric breakdown is the moduli-space substrate content distinguishing volovik's R1 from connes' R1 RELABELING reading).
2. **Inputs**: W11-2 INFO verdict; this workshop's R3 verdict; volovik's R1 §"W11-2 asymmetric breakdown" derivation; connes' R2 V-2 moduli-space-coordinate framing.
3. **Gate**: orchestrator-direct-write per `wave-classification.md` METHODOLOGY-class M1-M4 conjunction. PASS iff entry lands with provenance + cross-link + Sage-verified D_bi values.
4. **Effort**: ~quarter-wave.

**CF-W8-5 (co-authored with connes; connes PRIMARY)** — `S88-PHONONIC-FRAMING-MODULI-DEFORMATION-EXTENSION`

1. **What**: Diff to `phononic-framing.md`: add a new sub-section "Single-τ-slice vs moduli-deformation substrate-IS levels" with calibration corpus citing the W-8 workshop's adjudication of (χ_Σ, χ_S). Cross-link to cross-pillar-bridge-anatomy.md §"Cross-link to phononic-framing"; volovik also proposes extending cross-pillar-bridge-anatomy.md §"IS-not-IN Anatomy" to acknowledge moduli-space level explicitly (sub-clause).
2. **Inputs**: this workshop's R3 verdict; volovik's R1 substrate-framing block; connes' R2 V-2 substitution chain.
3. **Gate**: orchestrator-direct-write per `wave-classification.md` M1-M4. PASS iff diff lands with provenance + calibration corpus instance.
4. **Effort**: ~quarter-wave.

**CF-W8-6 (NEW; JOINT AUTHORS — connes V-3 + volovik R2 Sage-exhaustive)** — `S88-DELTA-0-LOCALIZATION-FORMULA-LANDING`

1. **What**: Land Δ_0 LOCALIZATION FORMULA as registry entry §VII.AL (next-free-letter after CF-W8-4's §VII.AK). Theorem statement: For any 4-element positive integer multiset `{c_1, c_2, c_3, c_4}` and any V_4 = Z_2 × Z_2 character via stratum-enumeration `σ : V_4 → {1, 2, 3, 4}`, the parallelogram cocycle Δ_0 = 4 · c_{σ((1,1))}; rel_dev_0 = 4 · c_{σ((1,1))} / sum_k c_k; PASS iff some c_k = 0. Sage-QQ exact at the abstract level. Calibration corpus: substrate cardinality vector (2, 4, 8, 6) at τ_fold yields 24 enumerations partitioned into 4 orbits of size 6 with rel_dev_0 ∈ {2/5, 4/5, 6/5, 8/5}, all FAIL by ≥ 8 OOM. Bridge anatomy (per `cross-pillar-bridge-anatomy.md`): substrate-IS observable = the 4-stratum cardinality vector at fixed τ; laboratory-IN observable = N/A (intra-substrate theorem; Pillar-IV cohomology-clean structural).
2. **Inputs**: connes V-3 derivation (workshop §R2 connes Step 5); volovik R2 Sage-QQ exhaustive transcript (24-permutation table + Δ_0 = 4·card[(1,1)] proof); W11-1 verdict (calibration corpus instance #1); W11-2 verdict (cardinality-vector data); permanent-results-registry.md §VII.AL slot.
3. **Gate**: orchestrator-direct-write per `wave-classification.md` METHODOLOGY-class M1-M4 conjunction. PASS iff theorem statement, calibration corpus, Sage-QQ provenance, and §VII.AL slot landing with provenance + dual-SHA closure SHA pin (over the joint R2 derivations).
4. **Effort**: ~quarter-wave (registry edit + Sage transcript pin + cross-link audit).

**CF-W8-7 (NEW; methodology calibration corpus; volovik PRIMARY)** — `S88-PRU-CLASS-8.2-CALIBRATION-INSTANCE-2`

1. **What**: Add the W-8 stratum-vs-(p,q)-parity adjudication as the second calibration corpus instance for `epistemic-discipline.md` §"Pre-Registration Completeness — PRU Class-8 sub-class taxonomy" Class 8.2 (verifier-rubric pre-registration failure). The W-12 instance was "Z_4 or similar admitted V_4 via cardinality match"; the W-8 instance is "RELABELING vs STRUCTURALLY DISTINCT readings differ on whether (p,q)-parity factorization is required for the W11-4 d=2 base case" — a rubric-form failure where the literal token "V_4 = (Z_2)^2 hypothesis" admits multiple embedding-incarnations the rubric did not pre-register. Per the cross-corpus pattern, K-counter advances 1 → 2 toward MANDATORY at K=3.
2. **Inputs**: W-12 calibration corpus; this workshop's R3 closure; epistemic-discipline.md §"Pre-Registration Completeness".
3. **Gate**: orchestrator-direct-write per `wave-classification.md` METHODOLOGY-class. PASS iff K-counter advance + new calibration row + provenance pin.
4. **Effort**: ~quarter-wave.

The seven CFs cohere under R3 closure: CF-W8-1 dispatches the surviving forward path with KO-orientation diagnostic; CF-W8-2 mechanical-closes S88-CF-W11-C citing CF-W8-6's structural-cause; CF-W8-3 is DROPPED (R2-volovik pre-dispatch closure); CF-W8-4 lands the moduli-space τ-axis observation; CF-W8-5 extends phononic-framing.md + cross-pillar-bridge-anatomy.md; CF-W8-6 lands the JOINT Δ_0 LOCALIZATION theorem at §VII.AL as a registry asset (its first calibration corpus instance is the substrate's bot-20 partition (2,4,8,6)); CF-W8-7 advances PRU Class 8.2 calibration corpus K=2.

End R2 volovik.

---

## R3 — Synthesis closing (designated synthesizer per R2 outcome)

### R3 — connes-ncg-theorist (synthesis lead; volovik co-authorship attribution per joint outcome)

**R3 connes synthesis (close W-8 with joint verdict on RELABELING vs STRUCTURALLY-DISTINCT + CF-W8-6 joint theorem landing + 4 adjudications)**

#### R2 outcome summary

R2-volovik conceded substantively on FOUR of the five workshop questions: (1) C-1 Sage-QQ pullback exhaustion (24/24 enumerations FAIL, min `rel_dev_0 = 2/5` exact in QQ); (2) C-2 NCG-axiomatic obstruction (χ_Σ does not lift to an A_F *-automorphism — V-1 KO=6 collapse argument settled the inventory question); (3) C-3 forward path collapses to triality-mod-2 candidate (iii), volovik's R1 (χ_Σ, χ_S) candidate retracted as moduli-space-side, NOT algebra-side; (4) W11-2 sector-rearrangement reading (cv-flip is intra-(p,q)-sector level reorganization, no new (1,1)-mod-2 sector enters bot-20). Beyond conceding, R2-volovik PRE-DISPATCH-CLOSED his own R1 hope (CF-W8-3 τ-integrated escape path) by independent Sage-QQ at `rel_dev_avg = 12/11` exact (FAIL by ~9 OOM). R2-volovik also independently CO-DERIVED the **Δ_0 LOCALIZATION FORMULA** `Δ_0 = 4·card[(1,1)-charged stratum]` first stated in connes' R2 V-3 Step 5 — the formula is enumeration-INDEPENDENT, cardinality-vector-LOCKED, structurally controls FAIL distribution to the 4-orbit `{2/5, 4/5, 6/5, 8/5}` partition, and generalizes beyond candidate (ii) to ANY future stratum-character V_4 candidate on similar 4-stratum partitions of positive-cardinality multisets.

R3 closes the workshop at HYBRID-WITH-NEW-THEOREM JOINT VERDICT: RELABELING reading wins on the algebra-axis (per the W-2 4-corner classification §VII.U.2, this is an algebra-INVARIANT family question — the parallelogram cocycle is a spectrum-only functional `F({λ_k, m_k}) = Σ_k m_k g(λ_k)` of the 4-stratum partition, and the FAIL is enumeration-independent partition-arithmetic, structurally orthogonal to whether (χ_Σ, χ_S) acts as a relabeling vs as structurally-distinct content); CF-W8-6 Δ_0 LOCALIZATION FORMULA is a JOINT structural theorem outcome neither agent stated independently in R1; volovik's substrate-physical contribution (real τ-asymmetric structural fingerprint at the moduli-deformation level) is preserved at a structurally distinct registry track (CF-W8-4, moduli-space) without rescuing candidate (ii) at the discrete-V_4-character level.

#### Joint final verdict on RELABELING vs STRUCTURALLY-DISTINCT

**Verdict-shape: HYBRID-WITH-NEW-THEOREM**.

- Algebra-axis: **RELABELING wins**. The (p,q)-Cartan-V_4 character W11-1 falsified at `max_dev = 1.163869` and the natural strata-V_4 enumerations all close at the **same OOM** (4% relative agreement; both 9 OOM above the FAIL ceiling 1e-9). Verified independently by both R2 agents in Sage-QQ. The structural cause is partition-arithmetic at fixed-τ cardinalities (the substrate's 4-stratum partition has no zero-cardinality stratum), NOT relabeling-vs-distinctness across τ-variation.
- Moduli-space-axis: volovik's **τ-asymmetric structural fingerprint is real substrate content** distinguishing chi_stratum (τ-aware domain) from chi_pq-Cartan (τ-blind domain). This content does NOT factor into a discrete-V_4 character on A_F (V-2 verdict), but DOES live on the τ-deformation moduli space {(A_K, H_K, D_K(τ)) : τ ∈ ℝ} as a one-parameter symmetry-breaking observable.
- New-theorem axis: the **Δ_0 LOCALIZATION FORMULA** `Δ_0 = 4·card[(1,1)-charged stratum]` is a JOINT R2 outcome that generalizes the FAIL beyond candidate (ii). Theorem domain: any 4-element positive-integer multiset and any V_4 = Z_2 × Z_2 stratum-enumeration. PASS iff some `c_k = 0`. At substrate cardinalities (2, 4, 8, 6) at τ_fold no `c_k = 0`, hence FAIL is partition-arithmetic-locked. This is a Pillar-IV cohomology-clean structural theorem candidate, registry-eligible.

**Routing consequence on §VII slot allocation** (registry-level finding made during R3 audit):

```
Step 1 (Definitions):
  permanent-results-registry.md slot inventory = {single-letter A-Z slot occupancy} ∪ {AA-AZ slot occupancy}
  Spawn prompt assumed §VII.AJ is the V_4-monodromy slot (DEMOTED-target).
  
Step 2 (Substitution — direct registry-text scan via Python regex over `sessions/permanent-results-registry.md` content):
  Occupied §VII slots (verified): {B, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, AA, AB, AC, AF, AG, AH, AI, AJ, AK, AL, AM}
  §VII.AJ occupied with label "Reserved for W-12 Mellin-Moment Identities (S86 W-12 — connes + volovik joint, 2026-04-27)"
  
Step 3 (Simplification — slot-identity check):
  §VII.AJ.label == "Reserved for W-12 Mellin-Moment Identities" — NOT V_4-monodromy.
  No §VII.X slot in the current registry carries the V_4-monodromy label.
  
Step 4 (Direction):
  The "DEMOTED §VII.AJ V_4-monodromy slot" status assumed in the spawn prompt and in CF-W8-2's R2 description is a stale-source citation. The current authoritative
  V_4-monodromy verdict tracking lives in `computations/s87_gate_verdicts.txt:294` (W11-1 verdict line, FAIL) and in `sessions/framework/registry/falsifier-master-inventory.md` (W11 falsifier-row record). Per `epistemic-discipline.md` §"Source Reconciliation" Class-(c) PIN-DRIFT-FROM-STALE-SOURCE.
  
Step 5 (Routing decision):
  CF-W8-2 mechanical pre-closure of S88-CF-W11-C MUST NOT update §VII.AJ (which is reserved for a different topic). It MUST update s87_gate_verdicts.txt (mechanical-closure FAIL line per `mechanical-closure-discipline.md`) and falsifier-master-inventory.md (mack-cosmic-bridge sole writer). The "V_4-monodromy DEMOTED" status is recorded at the verdict-line + inventory level, not at the §VII registry level.
```

§VII.AJ V_4-monodromy reference in the spawn prompt is hereby reclassified as **stale-source pointer** (Class-(c) per `epistemic-discipline.md`). The V_4-monodromy verdict-tracking is at verdict-line + inventory level, not at §VII.AJ. CF-W8-2 spec is corrected below to route the mechanical-closure update appropriately.

For CF-W8-6 (Δ_0 LOCALIZATION FORMULA registry landing) and CF-W8-4 (τ-asymmetry moduli-space registry landing), the **next-free single-letter §VII slots** are §VII.A (single-letter A is free; B is occupied) and the next-free `A?` slots are §VII.AD then §VII.AE (gap before §VII.AF). Per the regulator-pin-discipline.md "next-free-letter" convention preserving consecutive ordering with most-recent landings (AA-AM run), CF-W8-6 lands at **§VII.AD** and CF-W8-4 lands at **§VII.AE**. The §VII.A single-letter slot is preserved for higher-priority single-letter allocations.

#### Adjudication (i): CF-W8-3 drop confirmation

**VERDICT: CF-W8-3 is DROPPED from the carry-forward queue.**

Substitution chain (verifying volovik's R2 Sage-QQ exhaustion at `rel_dev_avg = 12/11` independently, this time via Python `Fraction` arithmetic — full transcript in connes' R3 dispatch):

```
Step 1 (Definitions):
  τ-grid (W11-2 INFO data) = {0.090, 0.140, 0.165, 0.180, 0.185, 0.190, 0.195, 0.200, 0.215, 0.240, 0.290}     (11 points)
  At τ = 0.090 (COLLAPSED, cv = (4, 2, 8, 6)):  χ_Σ = +1
  At remaining 10 τ-points (RIGID, cv = (2, 4, 8, 6)):  χ_Σ = -1
  χ_S(stratum_idx k):  -1 if k ∈ {1, 2}, +1 if k ∈ {3, 4}
  Δ_0 = A^(0,0) - A^(0,1) - A^(1,0) + A^(1,1)    (V_4 PARALLELOGRAM cocycle at n=0)

Step 2 (Substitution — single-τ moments):
  COLLAPSED single-τ (cv=(4,2,8,6), χ_Σ=+1):
    A^(0,0) = 4+2+8+6 = 20
    A^(0,1) = -4 - 2 + 8 + 6 = 8
    A^(1,0) = (+1) · 20 = 20
    A^(1,1) = (+1) · 8 = 8
    Δ_0_C   = 20 - 8 - 20 + 8 = 0    [degenerate Z_2 reduction; χ_Σ = +1 acts as identity]
  RIGID single-τ (cv=(2,4,8,6), χ_Σ=-1):
    A^(0,0) = 2+4+8+6 = 20
    A^(0,1) = -2 - 4 + 8 + 6 = 8
    A^(1,0) = (-1) · 20 = -20
    A^(1,1) = (-1) · 8 = -8
    Δ_0_R   = 20 - 8 - (-20) + (-8) = 24
    rel_dev_0_R = 24/20 = 6/5 = 1.2    [Sage-QQ exact, matches connes R2 W11-4 sage check]

Step 3 (Substitution — uniform-weight 11-τ-point average):
  A_avg^(0,0) = (1/11) · 20 + (10/11) · 20 = 20
  A_avg^(0,1) = (1/11) · 8  + (10/11) · 8  = 8
  A_avg^(1,0) = (1/11) · 20 + (10/11) · (-20) = (20 - 200)/11 = -180/11
  A_avg^(1,1) = (1/11) · 8  + (10/11) · (-8)  = (8 - 80)/11 = -72/11
  Δ_0_avg     = 20 - 8 - (-180/11) + (-72/11) = 12 + 108/11 = (132 + 108)/11 = 240/11

Step 4 (Simplification):
  rel_dev_avg = |Δ_0_avg| / |A_avg^(0,0)| = (240/11) / 20 = 12/11    [Python Fraction exact]
                Match to volovik R2 claim 12/11: TRUE (Fraction equality verified)
                Float: 12/11 = 1.090909...

Step 5 (Direction — comparison with FAIL ceiling):
  rel_dev_avg = 12/11 ≈ 1.0909
  FAIL ceiling = 1e-9
  rel_dev_avg / FAIL_ceiling = (12/11) / 1e-9 ≈ 1.09 × 10^9    ⟹    FAIL by ~9 OOM
  
Step 6 (Structural cause — restatement of theorem):
  τ-integration cannot escape partition-arithmetic FAIL because the only PASSing single-τ branch (COLLAPSED, χ_Σ=+1) is a Z_2 reduction (V_4 → Z_2 collapse where χ_Σ acts as identity), NOT a non-trivial V_4 satisfaction. The 10 RIGID branches each contribute Δ_0_R = 24, dominating the weighted average. The structural cause is the same Δ_0 LOCALIZATION FORMULA: at RIGID, Δ_0 = 4 · card[stratum at (1,1)-charge] = 4 · |S_2| = 4 · 4 = 16 if the (1,1) is on S_2; in the (χ_Σ, χ_S) enumeration the (1,1)-charge falls on strata with χ_S=-1 (S_1, S_2) at the χ_Σ=-1 (RIGID) branch, giving |S_1|+|S_2| = 6 mass at (1,1) per the alternate factorization in R2 Step 4 of connes' W11-4 sage check (the factored form Δ_0 = (1−χ_Σ)·sum_k(1−χ_S(k))|S_k| gives 2·12 = 24 = 4·6, equivalent under cardinality reorganization).
```

Volovik's R2 Sage-QQ claim is INDEPENDENTLY REPRODUCED EXACT in Python Fraction arithmetic. CF-W8-3 closes pre-dispatch FAIL by ~9 OOM. The structural theorem of CF-W8-3 closure is: τ-integrated weighted-average parallelogram cocycle CANNOT escape partition-arithmetic FAIL when the only PASSing single-τ branch is a Z_2 reduction (degenerate V_4). The PASSing branch's `Δ_0 = 0` is non-informative (V_4 collapsed to Z_2); the FAILing 10 branches each carry full FAIL; the average inherits the dominant FAIL.

**Recommendation**: DROP CF-W8-3 entirely from the next-session carry-forward queue. NO no-op pre-closure verdict line is required because CF-W8-3 was never dispatched at the computation layer — it was a workshop-internal hypothetical that volovik tested in R2 ahead of dispatch and confirmed FAIL. The structural-cause pin (the Δ_0 LOCALIZATION FORMULA + Z_2 reduction observation) is recorded here in R3 and again at CF-W8-6 landing.

#### Adjudication (ii): CF-W8-6 standalone landing + §VII.AD slot pre-allocation

**VERDICT: CF-W8-6 lands at §VII.AD as STAGE-1-CANDIDATE per `joint-theorem-promotion.md` 4-stage pathway.**

The Δ_0 LOCALIZATION FORMULA is a registry-eligible Pillar-IV cohomology-clean structural theorem candidate. Theorem text:

```
Δ_0 LOCALIZATION FORMULA (W-8 R3 R3-JOINT, S87, W-8 workshop):

  Let (c_1, c_2, c_3, c_4) be a 4-element multiset of positive integers (the
  cardinality vector of any 4-stratum partition of a finite-cardinality
  spectral observable). Let σ : V_4 = Z_2 × Z_2 → {1, 2, 3, 4} be any
  bijective enumeration of the V_4 cosets onto the stratum indices, i.e.,
  any of the 4! = 24 stratum-to-V_4-element labellings. The associated
  V_4 PARALLELOGRAM cocycle at n=0 satisfies, in QQ:

      Δ_0(σ; (c_1, ..., c_4)) := A^(e)_0 − A^(a)_0 − A^(b)_0 + A^(ab)_0
                              = 4 · c_{σ⁻¹((1,1))}                       [exact in QQ]

  where A^(g)_0 := Σ_k χ^(g)(σ(k)) · c_k is the spectral-action moment at
  n=0 for V_4 element g ∈ V_4 acting through σ. The relative deviation:

      rel_dev_0(σ; (c_1, ..., c_4)) := |Δ_0(σ; (c_1, ..., c_4))| / Σ_k c_k
                                     = 4 · c_{σ⁻¹((1,1))} / Σ_k c_k    [exact in QQ]

  PASS criterion (parallelogram cocycle vanishing) is equivalent to the
  existence of a stratum with cardinality zero. At any positive-cardinality
  4-stratum partition (c_k > 0 for all k), Δ_0 ≠ 0 and rel_dev_0 ≥ 4·min_k c_k / Σ_k c_k.

  Structural corollary on the substrate's 4-stratum partition (2, 4, 8, 6)
  at τ_fold (verified Python Fraction over all 24 enumerations + Sage QQ):
    rel_dev_0 ∈ {2/5, 4/5, 6/5, 8/5}   (each value at multiplicity 6 within
                                        the 24-permutation orbit; exhaustive)
    min rel_dev_0 = 2/5 = 0.4    (8 OOM above FAIL ceiling 1e-9)
    FAIL is partition-arithmetic-LOCKED, enumeration-INDEPENDENT.
```

Authorship attribution under `joint-theorem-promotion.md`:

- **Stage 0 — Workshop-Internal Candidate**: The theorem text was authored across R2 connes (V-3 Step 5: first statement of Δ_0 = 4·card[(1,1)-charged]) + R2 volovik (independent Sage-QQ exhaustive verification at all 24 enumerations + extension to "PASS iff some c_k = 0" general statement). Both R2 sections contain the theorem at the cohomology-class identity level. The substrate-cardinality calibration (2,4,8,6) and the 4-orbit distribution are jointly verified.
- **Stage 1 — S87 R3 Registration as STAGE-1-CANDIDATE**: This R3 closing entry records the theorem at `permanent-results-registry.md §VII.AD` (next-free `A?` slot per the registry-audit substitution chain above); registers it as **STAGE-1-CANDIDATE** per `joint-theorem-promotion.md`. The candidate text is frozen at the workshop verdict.
- **Stage 2 — S88+ Independent-Verify**: The cross-axis independent-verify gate is `S88-DELTA-0-LOCALIZATION-INDEPENDENT-VERIFY`, dispatched in parallel to TWO cross-reviewers WITHOUT the W-8 workshop transcripts:
  - Axis-A cross-reviewer: NCG-axiomatic spectral-functional perspective (default: lizzi-spectral-functional-theorist) audits the cohomology-class identity, the 24-enumeration partition argument, and the "PASS iff some c_k = 0" generalization.
  - Axis-B cross-reviewer: Volovik-superfluid-universe-theorist (recused as W-8 author) → use 3He-B BdG sub-algebra perspective via volovik's understudy or kitaev (information-scrambling perspective) for substrate-physics audit; OR explicitly route to gen-physicist for the abstract identity verification + partition-arithmetic structural-theorem verification path.
  - JOINT clauses: the theorem statement (cohomology-class form + corollary at substrate cardinalities) is PASS-AND'd across both verdicts.
- **Stage 3 — S88+ Permanent Registration**: On Stage-2 PASS, replace `STAGE-1-CANDIDATE` with `STAGE-3-PERMANENT` at §VII.AD; theorem joins the permanent-results table.

**Why §VII.AD (and NOT §VII.AL as suggested in the spawn prompt or volovik R2)**: per the registry-text scan substitution chain above, §VII.AL is OCCUPIED at present. The next-free `A?` slot is §VII.AD; using it preserves the consecutive-ordering convention with the most-recent landings (AA-AM run) and avoids the slot-collision hazard volovik R2's "SUGGESTED §VII.AL slot" line implies. Per `regulator-pin-discipline.md` next-free-letter convention.

#### Adjudication (iii): joint authorship attribution per `registry-landing.md` SOURCE-DOUBLE-CITE-CO-PRIMARY

**VERDICT: CF-W8-6 §VII.AD entry uses SOURCE-DOUBLE-CITE-CO-PRIMARY structure tag.**

Per `registry-landing.md` §"Detection (when SOURCE-DOUBLE-CITE-CO-PRIMARY applies)" the three-condition test:

```
Step 1 (Sequential dependency test):
  The Δ_0 LOCALIZATION FORMULA's derivation is sequential in the workshop record:
    Anchor-1 (input layer V): connes V-3 Step 5 first stated Δ_0 = 4·card[(1,1)-charged]
                              (R2 connes §"Response to V-3 (alternative strata → V_4 enumeration with rel_dev_0 ≤ 1e-9)")
    Anchor-2 (output layer C): volovik R2 Step 5 §"Response to C-1 (Sage-QQ pullback exact rel_dev_0 = 6/5)" EXTENDED the formula
                              to the structural theorem statement "PASS iff some c_k = 0" + 4-orbit distribution + Sage-QQ
                              exhaustive verification at all 24 enumerations + cross-link to W11-1 calibration corpus.
  Anchor-2 cannot be invoked WITHOUT first invoking Anchor-1 (volovik's R2 explicitly cites connes' V-3 derivation as input;
  the Sage-exhaustive sweep validates and EXTENDS connes' specific (S_4 → (1,1)) instance to the abstract enumeration-INDEPENDENT theorem).
  
Step 2 (Non-fungibility test):
  The two anchors are non-fungible:
    Anchor-1 alone (connes V-3) gives Δ_0 = 4·|S_4| = 24 at the specific natural enumeration; does NOT establish enumeration-INDEPENDENCE.
    Anchor-2 alone (volovik R2 Sage-exhaustive) gives the 4-orbit {2/5, 4/5, 6/5, 8/5} distribution but cites Anchor-1's derivation as the structural mechanism.
  Swapping Anchor-1 ↔ Anchor-2 breaks the chain: volovik's exhaustive sweep WITHOUT connes' V-3 derivation would be a numerical observation
  without a structural theorem; connes' V-3 derivation WITHOUT volovik's exhaustive sweep would be a single-instance claim without
  enumeration-independence. The two layers are sequentially dependent.
  
Step 3 (Both-anchors-required test):
  Both anchors must remain accessible for the §VII.AD entry to retain its provenance. Removing either:
    - Removing Anchor-1 → no structural derivation; the formula reduces to a tabulated empirical observation without theorem status.
    - Removing Anchor-2 → no enumeration-independence; the formula reduces to a single-instance claim without registry-eligible
      generalization.
  
Conclusion: SOURCE-DOUBLE-CITE-CO-PRIMARY applies. Structure tag pinned at §VII.AD entry.
```

§VII.AD entry skeleton (text frozen at this R3 close):

```
§VII.AD | Δ_0 LOCALIZATION FORMULA (Pillar-IV cohomology-clean structural theorem) | STAGE-1-CANDIDATE | S87 W-8 R3 R3-JOINT
ANCHOR-1 (input layer, V): R2 connes V-3 Step 5 — `sessions/archive/session-87/workshops/s87-v4-strata-vs-cartan-relabeling.md` lines ~683-697 (Δ_0 = 4·card[(1,1)-charged stratum] first statement; substrate cardinality calibration (2,4,8,6); min rel_dev_0 = 2/5 = 0.4; structural cause = no zero-cardinality stratum)
ANCHOR-2 (output layer, C): R2 volovik §"Response to C-1" Step 5 — `sessions/archive/session-87/workshops/s87-v4-strata-vs-cartan-relabeling.md` lines ~884-895 (Sage-QQ exhaustive 24-permutation verification; 4-orbit distribution {2/5, 4/5, 6/5, 8/5} each multiplicity 6; "PASS iff some c_k = 0" generalization; cross-link to W11-1 calibration corpus instance #1)
STRUCTURE: SOURCE-DOUBLE-CITE-CO-PRIMARY
Derivation chain: V (connes V-3 single-instance derivation) → A_F (V_4 PARALLELOGRAM cocycle on 4-stratum partition) → C (volovik R2 Sage-QQ exhaustive enumeration-independence) → conclusion (Δ_0 LOCALIZATION FORMULA, enumeration-INDEPENDENT, partition-arithmetic-LOCKED FAIL on positive-cardinality 4-stratum)
Calibration corpus: S87 W11-2 substrate cardinality vector (2, 4, 8, 6) at τ_fold = 0.190 — first calibration corpus instance.
Closure SHA pin: <to be computed at S88 §VII.AD landing dispatch via closure_hash over R2 connes + R2 volovik input-pin map>
4-stage status: STAGE-1-CANDIDATE (S87 W-8 R3); Stage-2 dispatch queued at CF-W8-6-STAGE-2 (S88+).
```

**Under `cross-pillar-bridge-anatomy.md`**: this is **NOT** a cross-pillar bridge. The Δ_0 LOCALIZATION FORMULA is an INTRA-substrate (Pillar-IV) cohomology-clean structural theorem. The substrate-IS observable (4-stratum cardinality vector) and the laboratory-IN observable (none — there is no continuum measurement image) are not paired across pillars. The 5-anatomy + 3-level discipline does not apply; the SOURCE-DOUBLE-CITE-CO-PRIMARY discipline does.

#### Adjudication (iv): V-1 KO=6 collapse caveat as CF-W8-1 dispatch diagnostic

**VERDICT: PRE-REGISTER as MANDATORY CF-W8-1 dispatch diagnostic.**

Substitution chain (the structural concern):

```
Step 1 (Definitions):
  CF-W8-1 candidate (iii) test: chi_triality_Z2(p, q) := (-1)^(t mod 2) where t(p, q) := (p − q) mod 3 ∈ {0, 1, 2};
  pair with g_M (transpose-on-M_3 *-automorphism) to form V_4 = chi_triality_Z2 × g_M
  Triality is the SU(3) Dynkin diagram outer automorphism of order 3; the Z_3 → Z_2 sub-quotient
  picks the "odd-triality" (t = 1) coset against the "even-triality" (t ∈ {0, 2}) coset.
  
Step 2 (Substitution — V-1 KO=6 collapse mechanism):
  Connes' R2 V-1 Step 4-5 established that the lifted (Z_2)^3 from {g_C, g_H, g_M} on Peter-Weyl content
  collapses to (Z_2)^2 = V_4 on (p,q)-Cartan-toral by KO-orientation lifting under the order-1 condition
  [[D, a], b°] = 0 + KO=6 axioms (J^2 = +1, Jγ = -γJ for KO-dim 6 mod 8). Connes-Marcolli 2008 §1.16 +
  Chamseddine-Connes-Marcolli 2007 §3.5.
  
Step 3 (Question — does the chi_triality_Z2 × g_M pair survive KO=6 collapse?):
  The triality automorphism is in Aut(M_3(C)) (it acts on irrep labels by cyclic Z_3 rotation);
  sub-charactered to Z_2 (the diagonal of Z_3 → Z_2), it lifts to a Z_2 *-automorphism of M_3(C).
  But under KO=6 orientation lifting, ANY (Z_2)^k commuting set on A_F = ℂ ⊕ ℍ ⊕ M_3(C) collapses under
  one linear relation (per V-1 Step 4-5). The chi_triality_Z2 × g_M pair has (Z_2)^2 = V_4 cardinality;
  if the KO=6 linear relation forces chi_triality_Z2 ∈ {g_C, g_H, g_M, g_C·g_H, g_C·g_M, g_H·g_M, g_C·g_H·g_M}
  modulo the relation (i.e., chi_triality_Z2 reduces to a sub-character of the (g_C, g_H, g_M) inventory),
  candidate (iii) FAILs by inheritance from W11-1.
  
Step 4 (Direction of the diagnostic):
  CF-W8-1 dispatch must include a PRE-REGISTERED DIAGNOSTIC at the start of the gate spec verifying:
    Diagnostic D-W8-1: under KO=6 orientation lifting on Peter-Weyl content of D_K(τ_fold), does
    chi_triality_Z2(p, q) = (-1)^((p - q) mod 3 mod 2) decompose as a NON-TRIVIAL function of
    {(-1)^p, (-1)^q, (-1)^p · (-1)^q, transpose-trace} that is NOT in the linear span of
    {chi_(g_C), chi_(g_H), chi_(g_M), chi_(g_C g_H), chi_(g_C g_M), chi_(g_H g_M), chi_(g_C g_H g_M)} modulo the
    KO=6 collapse linear relation?
    
    Verification path: Sage-QQ tabulation of chi_triality_Z2(p, q) on Peter-Weyl labels (p, q) ∈ {0,...,5}²
    with cross-comparison to all 7 possible characters under {g_C, g_H, g_M} composition. The volovik R2 §"Response to C-3"
    Step 2 already verified Sage-tabulated:
      (p,q) = (0,2):  t = 1;  chi_triality_Z2 = -1;  ((-1)^p, (-1)^q) = (+1, +1)
      (p,q) = (0,0):  t = 0;  chi_triality_Z2 = +1;  ((-1)^p, (-1)^q) = (+1, +1)
    So chi_triality_Z2 is NOT a function of ((-1)^p, (-1)^q) (different chi_triality_Z2 values at same (p mod 2, q mod 2)).
    The remaining 5 composite characters {chi_(g_C g_H), chi_(g_C g_M), chi_(g_H g_M), chi_(g_C g_H g_M)} each evaluate
    on Peter-Weyl as polynomials in (-1)^p, (-1)^q (the standard inventory acts diagonally on Cartan-toral); none can
    realize the (p − q) mod 3 mod 2 dependence.
    Therefore chi_triality_Z2 is genuinely DISTINCT from the linear span of {g_C, g_H, g_M} composite characters,
    PROVIDED the KO=6 collapse does not project chi_triality_Z2 onto a sub-(g_C, g_H, g_M) factor.

Step 5 (Diagnostic outcome interpretation):
  Diagnostic D-W8-1 PASS (chi_triality_Z2 survives KO=6 collapse as an independent factor):
    → CF-W8-1 dispatch proceeds with chi_triality_Z2 × g_M as the V_4 candidate; PASS/FAIL/INFO per the parallelogram cocycle test.
  Diagnostic D-W8-1 FAIL (chi_triality_Z2 reduces to a sub-(g_C, g_H, g_M) character under KO=6):
    → candidate (iii) FAILs by inheritance from W11-1 (since the (g_C, g_H, g_M) inventory generates the (p,q)-Cartan-V_4
       W11-1 falsified); CF-W8-1 closes pre-dispatch FAIL with structural-cause pin "KO=6 collapse"; wave-equivalent budget
       reroutes to candidates (iv)/(v) of W11-1's surviving enumeration.
```

**Pre-registration**: CF-W8-1 spec MUST include the D-W8-1 diagnostic as the FIRST gate-step (before the parallelogram cocycle test). The diagnostic carries its own PASS/FAIL outcome; CF-W8-1 main gate (parallelogram test) only dispatches conditional on D-W8-1 PASS. This routes the KO=6 collapse risk into the gate's structure rather than leaving it as a downstream surprise.

#### Final 4-field carry-forwards (FINAL specs)

The final CF queue under R3 closure (6 active CFs; CF-W8-3 DROPPED, CF-W8-6 ADDED; net delta = 0 from R2-volovik provisional 7-CF queue, since volovik already proposed dropping CF-W8-3):

**CF-W8-1 (co-authored, connes PRIMARY) — `S88-V4-CANDIDATE-III-TRIALITY-MOD-2`** (with D-W8-1 KO=6 diagnostic pre-registered)

1. **What**: Construct chi_triality_Z2 on Peter-Weyl labels (p,q) via SU(3) triality `t = (p − q) mod 3` sub-charactered to Z_2 via `chi_triality_Z2 := (-1)^(t mod 2)`. Pair with g_M (transpose-on-M_3 *-automorphism) to form V_4 candidate. Test parallelogram cocycle Δ_n[chi_triality_Z2, g_M] for n ∈ {0, 2, 4} at relative ≤ 1e-12 PASS / ≤ 1e-9 INFO / > 1e-9 FAIL on bot-20 SU(3) Peter-Weyl content at L_max=10 (master cache `s84_spectrum_cache_L12_tau019.npz`). PRE-REGISTERED DIAGNOSTIC D-W8-1 (FIRST gate-step): under KO=6 orientation lifting, verify chi_triality_Z2 does NOT reduce to a sub-(g_C, g_H, g_M) inventory composite character. D-W8-1 PASS gate via Sage-QQ tabulation showing chi_triality_Z2 differs from all 7 composite characters of {g_C, g_H, g_M} at ≥ 1 Peter-Weyl label. D-W8-1 FAIL → candidate (iii) closes pre-dispatch FAIL by KO=6 inheritance from W11-1.
2. **Inputs**: W11-1 verdict line `computations/s87_gate_verdicts.txt:294` (max_dev=1.16, FAIL); W11-3 verdict `:296` (Friedrich-Bär saturation theorem for L_max ≥ 12); W11-4 verdict `:290` ((Z_2)^d-Schur identity exact in QQ at d ∈ {2, 3, 4, 5}); SU(3) triality automorphism (Connes-Marcolli 2008 §1.13.3); A_F *-automorphism inventory (S84 W8a-result via knowledge MCP); KO=6 orientation lifting (Connes-Marcolli 2008 §1.16 + Chamseddine-Connes-Marcolli 2007 §3.5); canonical_constants.py `tau_fold = 0.190`; W-8 R3 verdict (this section).
3. **Gate**: D-W8-1 PASS gate dispatched FIRST. Conditional on D-W8-1 PASS: Δ_n parallelogram cocycle test, PASS iff max rel_dev across n ∈ {0, 2, 4} ≤ 1e-12; INFO ∈ (1e-12, 1e-9]; FAIL > 1e-9. Pre-registered tolerance identical to W11-1.
4. **Effort**: ~5-8h (Sage symbolic + irrep multiplicity Casimir-ladder + parallelogram cocycle + KO=6 orientation diagnostic).
5. **Depends on**: W-8 R3 verdict (this workshop); CF-W8-6 §VII.AD landing (Δ_0 LOCALIZATION calibration provides the 4-stratum partition baseline against which candidate (iii) is compared).

**CF-W8-2 (co-authored, connes PRIMARY) — `S88-CF-W11-C-PRE-CLOSURE-MECHANICAL`** (corrected routing per stale-source finding)

1. **What**: Mechanical-closure script for S88-CF-W11-C per `mechanical-closure-discipline.md`. Verdict: FAIL with `value='PRE-REG-INC_blocked_by_W8_PARTITION_ARITHMETIC_DELTA_0_LOCALIZATION_min_rel_dev_2_over_5'`. Records the W-8 R3 PARTITION-ARITHMETIC verdict citing the Δ_0 LOCALIZATION FORMULA (CF-W8-6 §VII.AD) as structural-cause pin. Emits dual-SHA companion row per `gate-verdicts.md`. Updates `falsifier-master-inventory.md` W11 row (mack-cosmic-bridge sole writer per `feedback_mack-bridge-role.md`) with annotation "W11-1 V_4-monodromy candidate (ii) DEMOTED across all single-τ-evaluation V_4 enumerations on bot-20 stratum cardinalities (2, 4, 8, 6); rooted in §VII.AD Δ_0 LOCALIZATION FORMULA". **CORRECTED**: does NOT update §VII.AJ (which is reserved for W-12 Mellin-Moment Identities, NOT V_4-monodromy — per the R3 stale-source finding above).
2. **Inputs**: W-8 R3 verdict; W11-1/W11-2/W11-3/W11-4 verdict lines; CF-W8-6 §VII.AD landing (Δ_0 LOCALIZATION provides the structural-cause pin); `mechanical-closure-discipline.md` template; `gate-verdicts.md` dual-SHA schema.
3. **Gate**: FAIL with descriptive value string per the rule; per-gate-distinct audit_sha256; in-script working-paper section update; mack-cosmic-bridge dispatch for inventory row update.
4. **Effort**: ~0.5h (mechanical script + inventory edit dispatch).
5. **Depends on**: CF-W8-6 §VII.AD landing (structural-cause pin); CF-W8-2 routes through inventory + verdict-line update, NOT §VII.AJ.

**CF-W8-3** — **DROPPED** per Adjudication (i). Volovik R2 Sage-QQ pre-dispatch FAIL at rel_dev_avg = 12/11 (independently reproduced in R3 via Python Fraction arithmetic; 9 OOM above FAIL ceiling; structural cause = COLLAPSED branch is degenerate Z_2 reduction, not non-trivial V_4 satisfaction). No verdict-line is required (CF-W8-3 was workshop-internal hypothetical, never reached computation dispatch).

**CF-W8-4 (co-authored, volovik PRIMARY) — `S88-MODULI-SPACE-TAU-ASYMMETRY-REGISTRY-ENTRY`** (slot routing corrected to §VII.AE)

1. **What**: Author §VII.AE (next-free `A?` slot AFTER §VII.AD lands; per the stale-source slot finding above) registry entry: "τ-Asymmetric Bot-20 Stratification Breakdown Direction (W11-2)". Substrate-IS observable: cardinality-vector swap direction (only at δ_τ = -0.10, never at δ_τ = +0.10; only toward bi-invariance s = 0). Anchor: D_bi(0.090) = 0.197217 < D_bi(0.190) = 0.462285 < D_bi(0.290) = 0.786038 (Python-verified Jensen scaling per volovik R1 Step 2). Cross-link to W-8 R3 RELABELING-WINS-ON-ALGEBRA-AXIS verdict noting that the asymmetric breakdown is the moduli-space-level substrate content distinguishing volovik R1 from connes R1 RELABELING reading without rescuing candidate (ii) at the discrete-V_4-character level. Cross-link to CF-W8-6 §VII.AD (Δ_0 LOCALIZATION) noting the moduli-space observation is OUTSIDE the §VII.AD theorem scope (which is single-τ partition-arithmetic).
2. **Inputs**: W11-2 INFO verdict line; W-8 R3 verdict (this section); volovik R1 §"W11-2 asymmetric breakdown" derivation; connes R2 V-2 moduli-space-coordinate framing; canonical_constants.py for D_bi anchor values (or compute in-script).
3. **Gate**: orchestrator-direct-write per `wave-classification.md` METHODOLOGY-class M1-M4 conjunction (M1 PASS predicate is artifact-existence-with-substantive-content; M2 producing operations are Edit/Write on registry; M3 source-of-truth is verbatim from this workshop closure; M4 allowlist append at `methodology-wave-allowlist.md`). PASS iff §VII.AE entry lands with provenance + cross-link + Sage-verified D_bi values + slot-allocation lockfile update.
4. **Effort**: ~quarter-wave (registry edit + lockfile update + cross-link audit).
5. **Depends on**: CF-W8-6 §VII.AD landing (forces §VII.AE to be the next-free slot for CF-W8-4).

**CF-W8-5 (co-authored, connes PRIMARY) — `S88-PHONONIC-FRAMING-MODULI-DEFORMATION-EXTENSION`**

1. **What**: Diff to `phononic-framing.md`: add a new sub-section "Single-τ-slice vs moduli-deformation substrate-IS levels" with calibration corpus citing the W-8 workshop's adjudication of (χ_Σ, χ_S). The discipline distinguishes (a) single-τ-slice substrate-IS observables that are A_F-derivable algebra-character functionals (subject to the 7 NCG axioms; algebra-INVARIANT family per W-2 §VII.U.2) from (b) moduli-deformation substrate-IS observables on the τ-deformation family {(A_K, H_K, D_K(τ)) : τ ∈ ℝ} that are continuous-symmetry observables (not algebra-character functionals; algebra-DEPENDENT or moduli-axis-residing). Both are substrate-IS per `phononic-framing.md` IS-not-IN; they differ in structural level. Cross-link diff to `cross-pillar-bridge-anatomy.md` §"Cross-link to phononic-framing"; volovik proposes companion sub-clause to `cross-pillar-bridge-anatomy.md` §"IS-not-IN Anatomy" acknowledging moduli-space level explicitly.
2. **Inputs**: W-8 R3 verdict (this section); volovik R1 §"Substrate framing"; connes R2 V-2 substitution chain (Step 5 moduli-space-coordinate framing); `phononic-framing.md` §"IS Space, Not IN Space"; `cross-pillar-bridge-anatomy.md` §"Cross-link to phononic-framing"; W-2 §VII.U.2 4-corner classification (algebra-INVARIANT vs algebra-DEPENDENT axis).
3. **Gate**: orchestrator-direct-write per `wave-classification.md` M1-M4. PASS iff diff lands with provenance + calibration corpus instance #1 (W-8) + cross-link to W-2 §VII.U.2.
4. **Effort**: ~quarter-wave.
5. **Depends on**: W-8 R3 verdict landing; CF-W8-4 §VII.AE landing (provides the moduli-space registry instance the rule extension cites as calibration corpus).

**CF-W8-6 (JOINT AUTHORS, SOURCE-DOUBLE-CITE-CO-PRIMARY) — `S88-DELTA-0-LOCALIZATION-FORMULA-LANDING`** (slot routing corrected to §VII.AD)

1. **What**: Land Δ_0 LOCALIZATION FORMULA as registry entry §VII.AD (corrected from spawn prompt's §VII.AL — that slot is OCCUPIED). Theorem statement (verbatim text from Adjudication (ii) above): for any 4-element positive-integer multiset (c_1, c_2, c_3, c_4) and any V_4 = Z_2 × Z_2 character via stratum-enumeration σ : V_4 → {1, 2, 3, 4}, Δ_0(σ; (c_1, ..., c_4)) = 4 · c_{σ⁻¹((1,1))} EXACT in QQ; rel_dev_0 = 4·c_{σ⁻¹((1,1))}/Σ_k c_k EXACT in QQ; PASS iff some c_k = 0. STAGE-1-CANDIDATE per `joint-theorem-promotion.md` 4-stage pathway. Calibration corpus instance #1: substrate cardinality vector (2, 4, 8, 6) at τ_fold yields 24 enumerations partitioned into 4 orbits of size 6 with rel_dev_0 ∈ {2/5, 4/5, 6/5, 8/5}, all FAIL by ≥ 8 OOM. Authorship: SOURCE-DOUBLE-CITE-CO-PRIMARY (V = R2 connes V-3 Step 5 input layer; C = R2 volovik R2 Sage-QQ exhaustive output layer). Per `cross-pillar-bridge-anatomy.md` this is INTRA-SUBSTRATE Pillar-IV cohomology-clean structural theorem, NOT a cross-pillar bridge; 5-anatomy + 3-level discipline does NOT apply.
2. **Inputs**: R2 connes V-3 Step 5 derivation (workshop §R2 connes); R2 volovik §"Response to C-1" Step 5 Sage-QQ exhaustive transcript; W11-1 verdict (calibration corpus instance #1); W11-2 verdict (cardinality-vector data source); permanent-results-registry.md §VII.AD slot; `joint-theorem-promotion.md` 4-stage pathway template; `registry-landing.md` SOURCE-DOUBLE-CITE-CO-PRIMARY schema; `s87-slot-pre-allocation-lockfile.md` slot-allocation update.
3. **Gate**: orchestrator-direct-write per `wave-classification.md` METHODOLOGY-class M1-M4. PASS iff §VII.AD entry lands with theorem statement + ANCHOR-1 + ANCHOR-2 + STRUCTURE: SOURCE-DOUBLE-CITE-CO-PRIMARY tag + Stage-1-candidate marker + calibration corpus + closure SHA pin computed via `closure_hash` over R2 connes + R2 volovik input-pin map. Cross-axis Stage-2 verify queued at CF-W8-6-STAGE-2 (S88+).
4. **Effort**: ~quarter-wave (registry edit + Sage-QQ transcript pin + cross-link audit + slot-allocation lockfile update + Stage-2 dispatch queue).
5. **Depends on**: W-8 R3 verdict landing; `permanent-results-registry.md` §VII.AD slot remains free at S88 plan-freeze (next-free `A?` slot per S87-end audit).

**CF-W8-7 (methodology calibration corpus, volovik PRIMARY) — `S88-PRU-CLASS-8.2-CALIBRATION-INSTANCE-2`**

1. **What**: Add the W-8 stratum-vs-(p,q)-parity adjudication as the second calibration corpus instance for `epistemic-discipline.md` §"Pre-Registration Completeness — PRU Class-8 sub-class taxonomy formal extension" Class 8.2 (verifier-rubric pre-registration failure). The W-12 instance was "Z_4 or similar admitted V_4 via cardinality match"; the W-8 instance is "RELABELING vs STRUCTURALLY-DISTINCT readings differ on whether (p,q)-parity factorization is required for the W11-4 d=2 base case" — a rubric-form failure where the literal token "V_4 = (Z_2)^2 hypothesis" admits multiple embedding-incarnations (single-τ enumeration / single-τ (χ_Σ, χ_S) / τ-integrated (χ_Σ, χ_S)) the rubric did not pre-register, all of which structurally FAIL by the Δ_0 LOCALIZATION formula at the substrate's actual cardinality vector. K-counter advances 1 → 2 toward MANDATORY at K=3.
2. **Inputs**: W-12 calibration corpus instance #1; W-8 R3 closure (this section); `epistemic-discipline.md` §"Pre-Registration Completeness".
3. **Gate**: orchestrator-direct-write per `wave-classification.md` METHODOLOGY-class M1-M4. PASS iff K-counter advance 1→2 + new calibration row + provenance pin.
4. **Effort**: ~quarter-wave.
5. **Depends on**: W-8 R3 verdict landing; CF-W8-6 §VII.AD landing (Δ_0 LOCALIZATION provides the structural-arithmetic content underlying the multi-incarnation FAIL pattern).

#### Workshop W-8 closure status (preview of bottom block)

W-8 closes at: **HYBRID-WITH-NEW-THEOREM JOINT VERDICT**; CF-W8-6 STAGE-1-CANDIDATE Pillar-IV §VII.AD; algebra-axis verdict RELABELING wins (per W-2 §VII.U.2 algebra-INVARIANT family); moduli-space-axis verdict τ-asymmetric structural fingerprint preserved at §VII.AE (CF-W8-4); CF-W8-3 DROPPED pre-dispatch.

Substrate verdict: RELABELING wins on algebra-axis. 24/24 enumeration FAIL by ≥ 8 OOM; min rel_dev_0 = 2/5 EXACT in QQ; partition-arithmetic-LOCKED via Δ_0 LOCALIZATION FORMULA. Volovik's R1 (χ_Σ, χ_S) candidate retracted (V-2 verdict: not A_F-derivable; moduli-space-coordinate, not algebra-character).

Methodology verdict: CF-W8-6 Δ_0 LOCALIZATION FORMULA joint structural theorem candidate; SOURCE-DOUBLE-CITE-CO-PRIMARY (R2 connes V-3 Step 5 + R2 volovik R2 Sage-QQ exhaustive); STAGE-1-CANDIDATE per `joint-theorem-promotion.md` 4-stage pathway; Stage-2 cross-axis independent-verify queued at S88+.

Stale-source finding: §VII.AJ V_4-monodromy slot is OCCUPIED by W-12 Mellin-Moment Identities reservation (S86 W-12 connes+volovik joint, 2026-04-27); V_4-monodromy verdict tracking at verdict-line + falsifier-master-inventory.md level, NOT at §VII registry level. CF-W8-2 routing corrected accordingly.

4-field carry-forwards: 6 active (CF-W8-1 candidate (iii) triality; CF-W8-2 mechanical pre-closure; CF-W8-4 moduli-space registry §VII.AE; CF-W8-5 phononic-framing diff; CF-W8-6 Δ_0 LOCALIZATION §VII.AD; CF-W8-7 PRU Class 8.2 corpus K=2). CF-W8-3 DROPPED. Net delta from R2-volovik 7-CF queue: -1 (CF-W8-3) + 0 (CF-W8-6 already proposed) = -1. Net delta from R2-connes 5-CF queue: +1 (CF-W8-6) +1 (CF-W8-7 from R2-volovik) -1 (CF-W8-3 dropped) = +1.

End R3 connes synthesis closing.

---

## Workshop W-8 closure status

**Close class**: HYBRID-WITH-NEW-THEOREM JOINT VERDICT (per `Investigating-Workshops.md` four-condition compliance: 2 agents with competing perspectives on a specific tension; genuine ledger-dissonance between RELABELING vs STRUCTURALLY-DISTINCT readings; 3-round R1/R2/R3 structure; output is a structural verdict resolving the competing claims AND a new joint structural theorem candidate).

**Authorship**:

- **R1 connes** (NCG-axiomatic; W11-1 PRIMARY + W11-3 PRIMARY; RELABELING reading)
- **R1 volovik** (3He-B substrate authority; W11-5 PRIMARY; STRUCTURALLY-DISTINCT reading)
- **R2 connes** (sharpened RELABELING; partition-arithmetic argument; Sage-QQ exhaustive 24-enumeration sweep; CF-W8-3 τ-integrated test introduced)
- **R2 volovik** (4-point concession on C-1, C-2, C-3, W11-2; pre-closure of CF-W8-3 via independent Sage-QQ at rel_dev_avg = 12/11; co-derivation of Δ_0 LOCALIZATION FORMULA; co-authored CF-W8-6 proposal)
- **R3 connes** (synthesis closing with joint final verdict; 4 adjudications; Δ_0 LOCALIZATION FORMULA STAGE-1-CANDIDATE Pillar-IV §VII.AD landing per `joint-theorem-promotion.md` 4-stage pathway; SOURCE-DOUBLE-CITE-CO-PRIMARY structure tag per `registry-landing.md`; D-W8-1 KO=6 collapse diagnostic pre-registered for CF-W8-1; stale-source finding on §VII.AJ V_4-monodromy slot identity)

**Joint final verdicts on the four adjudication questions**:

| # | Question | R3 verdict |
|:-:|:---------|:-----------|
| (i) | Confirm CF-W8-3 τ-integrated escape DROP from carry-forward queue? | **DROP**. R2-volovik Sage-QQ pre-dispatch FAIL at rel_dev_avg = 12/11 EXACT (Python Fraction reproduced); 9 OOM above FAIL ceiling 1e-9; structural cause = COLLAPSED branch is degenerate Z_2 reduction (V_4 → Z_2 collapse where χ_Σ = +1 acts as identity), not non-trivial V_4 satisfaction. No verdict-line required (workshop-internal hypothetical never reached computation). |
| (ii) | Confirm CF-W8-6 Δ_0 LOCALIZATION standalone landing + §VII.AL slot pre-allocation? | **CONFIRM landing; slot CORRECTED to §VII.AD**. The spawn prompt's §VII.AL is currently OCCUPIED per direct registry scan (set-membership audit over `permanent-results-registry.md` text). Next-free `A?` slot under `regulator-pin-discipline.md` next-free-letter convention is §VII.AD. STAGE-1-CANDIDATE per `joint-theorem-promotion.md` 4-stage pathway; Stage-2 cross-axis independent-verify queued at CF-W8-6-STAGE-2 (S88+) with cross-reviewer assignments per Adjudication (ii) above. |
| (iii) | Finalize joint authorship attribution per `registry-landing.md` SOURCE-DOUBLE-CITE-CO-PRIMARY? | **SOURCE-DOUBLE-CITE-CO-PRIMARY confirmed**. ANCHOR-1 = R2 connes V-3 Step 5 (input layer V; first stating Δ_0 = 4·card[(1,1)-charged]). ANCHOR-2 = R2 volovik §"Response to C-1" Step 5 (output layer C; Sage-QQ exhaustive 24-enumeration verification + "PASS iff some c_k = 0" generalization). Sequential dependency, non-fungibility, both-anchors-required all verified per `registry-landing.md` §"Detection". |
| (iv) | Pre-register V-1 KO=6 collapse caveat as CF-W8-1 dispatch diagnostic? | **PRE-REGISTER as MANDATORY**. Diagnostic D-W8-1 routes the KO=6 orientation-lifting risk into the gate's structure: chi_triality_Z2 must demonstrably NOT reduce to a sub-(g_C, g_H, g_M) inventory composite character under KO=6 collapse. D-W8-1 dispatched FIRST (before parallelogram cocycle test); main gate proceeds on D-W8-1 PASS only. Sage-QQ tabulation path established (volovik R2 §"Response to C-3" Step 2 already showed chi_triality_Z2 differs from ((-1)^p, (-1)^q) at (p,q)=(0,2) vs (0,0)). |

**Substrate verdict (algebra-axis)**: RELABELING wins. The Δ_0 LOCALIZATION FORMULA `Δ_0 = 4 · card[(1,1)-charged stratum]` (joint R2 result, Sage-QQ exact in QQ) controls the 24-enumeration FAIL distribution into the 4-orbit `{2/5, 4/5, 6/5, 8/5}` (each multiplicity 6) at substrate cardinalities (2, 4, 8, 6) at τ_fold. min rel_dev_0 = 2/5 = 0.4 EXACT; ≥ 8 OOM above FAIL ceiling 1e-9. FAIL is partition-arithmetic-LOCKED, enumeration-INDEPENDENT, structurally orthogonal to the RELABELING-vs-DISTINCT debate. Per W-2 §VII.U.2 4-corner classification, this is an algebra-INVARIANT family functional (spectrum-only `F({λ_k, m_k}) = Σ_k m_k g(λ_k)` of the 4-stratum partition cardinalities); the τ-asymmetric content surfaced by volovik lives in the algebra-DEPENDENT family on a structurally orthogonal axis.

**Substrate verdict (moduli-space-axis)**: τ-asymmetric structural fingerprint preserved. The W11-2 cv-flip at δ_τ = -0.10 (cv = (4, 2, 8, 6)) vs τ-rigid at δ_τ = +0.10 (cv = (2, 4, 8, 6)) is a real substrate-physical observation (D_bi(0.090) = 0.197217 < D_bi(0.190) = 0.462285 < D_bi(0.290) = 0.786038 — Python-verified Jensen scaling per volovik R1 Step 2). It does NOT lift to an A_F *-automorphism (V-1 + V-2 verdict; no fourth commuting Z_2 *-automorphism beyond {g_C, g_H, g_M}; smooth τ-parameterized path in Aut(A_F) cannot flip discretely). It DOES live on the τ-deformation moduli space {(A_K, H_K, D_K(τ)) : τ ∈ ℝ} as a one-parameter symmetry-breaking observable distinct from V_4-monodromy. Registered at CF-W8-4 §VII.AE (next-free `A?` after CF-W8-6 §VII.AD lands).

**Methodology verdict**: CF-W8-6 Δ_0 LOCALIZATION FORMULA is a JOINT structural theorem candidate neither agent stated independently in R1; both R2 sections converged on the formula (connes V-3 Step 5 single-instance derivation; volovik R2 Sage-QQ exhaustive enumeration-INDEPENDENT generalization). SOURCE-DOUBLE-CITE-CO-PRIMARY structure tag per `registry-landing.md`; STAGE-1-CANDIDATE per `joint-theorem-promotion.md` 4-stage pathway; Stage-2 independent-verify scheduled at S88+. CF-W8-7 advances PRU Class 8.2 calibration corpus K-counter 1 → 2 toward MANDATORY at K=3.

**Stale-source finding (Class-(c) PIN-DRIFT-FROM-STALE-SOURCE per `epistemic-discipline.md`)**: The spawn prompt and CF-W8-2 (R2 description) referenced "§VII.AJ V_4-monodromy slot" as the demotion target. Direct registry scan via Python regex over `sessions/permanent-results-registry.md` content reveals §VII.AJ is OCCUPIED with the label "Reserved for W-12 Mellin-Moment Identities (S86 W-12 — connes + volovik joint, 2026-04-27)" — NOT V_4-monodromy. The current authoritative V_4-monodromy verdict tracking lives at `computations/s87_gate_verdicts.txt:294` (W11-1 verdict line, FAIL) + `sessions/framework/registry/falsifier-master-inventory.md` (mack-cosmic-bridge sole writer). CF-W8-2 routing corrected: mechanical-closure script updates verdict-file + inventory row, NOT §VII.AJ.

**4-field carry-forwards (6 active; per `feedback_fix-in-session-never-defer.md`)**:

| CF | Spec | Authorship | Dependencies |
|:---|:-----|:-----------|:-------------|
| **CF-W8-1** | `S88-V4-CANDIDATE-III-TRIALITY-MOD-2` (with D-W8-1 KO=6 diagnostic pre-registered) | connes PRIMARY, volovik CO-AUTHOR | W-8 R3 verdict; CF-W8-6 §VII.AD landing |
| **CF-W8-2** | `S88-CF-W11-C-PRE-CLOSURE-MECHANICAL` (verdict-file + inventory row, NOT §VII.AJ) | connes PRIMARY, volovik CO-AUTHOR | CF-W8-6 §VII.AD landing (structural-cause pin) |
| **CF-W8-3** | DROPPED per Adjudication (i); pre-closed FAIL by ~9 OOM | — | — |
| **CF-W8-4** | `S88-MODULI-SPACE-TAU-ASYMMETRY-REGISTRY-ENTRY` (§VII.AE registry landing) | volovik PRIMARY, connes CO-AUTHOR | CF-W8-6 §VII.AD landing forces §VII.AE next-free |
| **CF-W8-5** | `S88-PHONONIC-FRAMING-MODULI-DEFORMATION-EXTENSION` (`phononic-framing.md` diff + cross-pillar-bridge-anatomy.md sub-clause) | connes PRIMARY, volovik CO-AUTHOR | CF-W8-4 landing provides calibration corpus |
| **CF-W8-6** | `S88-DELTA-0-LOCALIZATION-FORMULA-LANDING` (§VII.AD STAGE-1-CANDIDATE; SOURCE-DOUBLE-CITE-CO-PRIMARY) | JOINT (connes V-3 + volovik R2 Sage-exhaustive); SOURCE-DOUBLE-CITE-CO-PRIMARY | W-8 R3 verdict; §VII.AD slot remains free at S88 plan-freeze |
| **CF-W8-7** | `S88-PRU-CLASS-8.2-CALIBRATION-INSTANCE-2` (K-counter 1→2) | volovik PRIMARY, connes CO-AUTHOR | W-8 R3 verdict landing; CF-W8-6 §VII.AD landing |

Net delta from R2-volovik 7-CF queue: -1 (CF-W8-3 dropped). Total active CF set = 6 (CF-W8-1, CF-W8-2, CF-W8-4, CF-W8-5, CF-W8-6, CF-W8-7).

**Cross-references to invoked rules**:

- `.claude/rules/Investigating-Workshops.md` — four-condition workshop compliance (genuine ledger-dissonance between RELABELING and STRUCTURALLY-DISTINCT readings; 3-round R1/R2/R3; structural verdict + new joint theorem candidate)
- `.claude/rules/joint-theorem-promotion.md` — 4-stage pathway; Δ_0 LOCALIZATION FORMULA at STAGE-1-CANDIDATE; Stage-2 cross-axis independent-verify scheduled at S88+
- `.claude/rules/registry-landing.md` — SOURCE-DOUBLE-CITE-CO-PRIMARY structure tag for CF-W8-6 (sequential V_input → C_output dependency between R2 connes V-3 Step 5 and R2 volovik §"Response to C-1" Step 5)
- `.claude/rules/regulator-pin-discipline.md` — next-free-letter slot allocation (§VII.AD for CF-W8-6, §VII.AE for CF-W8-4)
- `.claude/rules/cross-pillar-bridge-anatomy.md` — Δ_0 LOCALIZATION FORMULA is INTRA-substrate Pillar-IV cohomology-clean structural theorem, NOT cross-pillar bridge; 5-anatomy + 3-level discipline does NOT apply
- `.claude/rules/phononic-framing.md` §"IS Space, Not IN Space" — CF-W8-5 extension distinguishing single-τ-slice algebra-character substrate-IS observables from moduli-deformation continuous-τ substrate-IS observables
- `.claude/rules/epistemic-discipline.md` §"Source Reconciliation" Class-(c) PIN-DRIFT-FROM-STALE-SOURCE — §VII.AJ stale pointer flagged; routing corrected
- `.claude/rules/epistemic-discipline.md` §"Pre-Registration Completeness — PRU Class-8 sub-class taxonomy" Class 8.2 — CF-W8-7 advances K-counter 1→2
- `.claude/rules/mechanical-closure-discipline.md` — CF-W8-2 mechanical-closure script template + dual-SHA companion row + per-gate-distinct audit_sha256
- `.claude/rules/wave-classification.md` — METHODOLOGY-class M1-M4 conjunction for orchestrator-direct-write CFs (CF-W8-4, CF-W8-5, CF-W8-6, CF-W8-7)
- `.claude/rules/feedback_fix-in-session-never-defer.md` — 4-field structured carry-forward specs

End workshop W-8.
