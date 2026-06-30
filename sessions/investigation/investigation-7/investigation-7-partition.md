# Investigation 7 — Wave Partition Manifest

**Date**: 2026-06-14
**Seed**: `investigation-7-seed.md` (3-agent survey batch: cosmic-web-theorist + little-red-dots-jwst-analyst + loop-quantum-gravity-theorist)
**Shape**: fanout (4 per-wave plan files + thin plan-index)
**Source**: `investigation-7-seed.md §"Candidate gate table"` — this manifest re-buckets that table into the per-wave planner-swarm input.

Per-wave planners read this manifest's "assigned items" rows + the seed file. Owner = the wave's domain-survey author (reviewer-origin owner), except W4 whose owner is a NEUTRAL planner (`gen-physicist`) because it carries the two adjudication workshops where the W2/W3 owners are participants. Gate executors (`agent_type` in each gate block) are suggested per gate; the per-wave planner finalizes by substrate match.

**Cross-investigation dedup (carried from seed §"DEDUP")**: every adjacency to the inv-4 GR batch and the four prior A_s-wall routes is **complementary (distinct machinery / distinct observable), NOT duplicate** — but each gate block MUST carry its cross-reference so `/rclab-coordinate` does not see redundancy. Load-bearing cross-links: INV7-W3-1 ↔ inv-4 W1-1/W1-2 + inv-5 W1-4 (same crossed product / same observable, distinct functional); INV7-W3-2 ↔ inv-3 W2-3 / inv-4 W1-4 / inv-5 W2-1 / inv-6 W2-2 (FIFTH A_s route); INV7-W4-1 ↔ inv-4 W3-1 (same a(t)-clock target, distinct machinery); INV7-W3-1 + W2-2 ↔ inv-6 (same Row #88 compact-object cell).

---

## Wave 1 — cosmic-web LSS observables

- **Owner-planner**: `cosmic-web-theorist` (seed author; owns the large-scale-structure / cosmic-web-topology / void-statistics / BAO / peculiar-velocity cluster)
- **Types**: compute × 6
- **Theme**: the cosmic-web survey's through-line — "the framework is observationally SAFE but not SHARP." Its LSS predictions match ΛCDM on σ₈/f(z)/the primary BAO peak; its ONE distinctive feature (the first-sound ring, Row #72) is amplitude-fragile (C1: the A_FS=0.204 pin reuses the standard recombination sound speed 1/[3(1+R*)]). This wave (a) tests whether that one sharp feature is real (W1-1 c₂² substrate-first + W1-2 VSF disambiguation), (b) closes the cleanest unfinished LSS verdict (W1-3 raw-BAO χ² vs the canonical w₀), and (c) is where the sector could BECOME sharp (W1-4 timescape Hubble relief; W1-5 persistent-homology web fingerprint; W1-6 f·σ₈ joint-bin test).

| # | Gate ID | gate_type | Suggested exec | One-line scope |
|:--|:--------|:----------|:---------------|:---------------|
| 1 | INV7-W1-1 | compute | cosmic-web-theorist | c₂² substrate-first from the S44 second-sound dispersion (Q=75,989); A_FS=c₂²/c₁² genuinely 0.204 or standard-formula stand-in? (resolve C1 flagship contradiction) |
| 2 | INV7-W1-2 | compute | cosmic-web-theorist | Void Size Function with the second-sound feature; VSF bump at r₁=325 Mpc vs DESI/SDSS catalogs (disambiguate C1: real-in-voids vs aliased) |
| 3 | INV7-W1-3 | compute | cosmic-web-theorist | raw-DESI-BAO χ²/N against canonical w₀=−0.918 (NOT the superseded −0.509, NOT the derived CPL parameter); FAIL-threshold 4 (resolve C2) |
| 4 | INV7-W1-4 | compute | cosmic-web-theorist | KBC void (6.04σ) as low-τ substrate region; local H₀ enhancement vs ~9% Hubble relief, w₀-orthogonal (B2/timescape) |
| 5 | INV7-W1-5 | compute | cosmic-web-theorist | persistent-homology β₁/β₂ of the second-sound ring vs ΛCDM mocks; distinct from S43 k~10²⁴ closure (B4/G1 distinctiveness) |
| 6 | INV7-W1-6 | compute | cosmic-web-theorist (mack on any falsifier row) | f·σ₈(z) per-z-bin curve + joint χ² vs ΛCDM across DESI/Euclid bins (f_FW=0.525492 vs 0.527130; −4.058% @ z=0.51) |

- **Natural-split candidates** (if the wave stalls): {INV7-W1-1, INV7-W1-2} ring-distinctiveness sub-wave (c₂² + VSF disambiguator — W1-2 consumes W1-1's P(k) feature) | {INV7-W1-3, INV7-W1-6} BAO/growth-verdict sub-wave (raw-BAO χ² + f·σ₈, both DESI-public observational comparisons) | {INV7-W1-4, INV7-W1-5} make-it-sharp sub-wave (timescape H₀ + persistent-homology topology).
- **Shared inputs**: S44 W6-2 second-sound mode Q=75,989 + c₁=v_F/√3 (`s86-r-dual-pathway`) + A_FS=0.204=100/489 target (W1-1); the framework P(k) with the W1-1 feature + excursion-set void kernel + DESI/SDSS VIDE/ZOBOV catalogs (W1-2); canonical w₀=−0.918 + DESI DR2 raw BAO distances + atlas-09 Item-25 FAIL-threshold 4 (W1-3); `project_substrate-compaction-timescape` τ(ρ) + KBC params (6.04σ, ~300 Mpc, Haslbauer+20) + ~9% relief target (W1-4); the framework field generator (Gaussian + second-sound + f_NL=1.5 Row #69) + ΛCDM mocks (W1-5); f_FW(z) (eq_4727/4728) + DESI DR2 public f·σ₈ + Euclid per-bin σ (W1-6).
- **Cross-track note**: any `falsifier-master-inventory.md` row or `canonical_constants.py` pin from these gates (A_FS_substrate, the w₀ raw-BAO verdict, the timescape H₀, the f·σ₈ joint-χ²) is session-promotion + `mack` sole-writer (NOT an investigation edit). W1-4 (KBC timescape) and LRD C3 (compaction vanishes at high z) are the two epochs of one τ(ρ) mechanism — cross-reference inv-7 W2 but NOT a shared gate.

## Wave 2 — little-red-dots high-z observational computes

- **Owner-planner**: `little-red-dots-jwst-analyst` (seed author; JWST high-z observer — fluxes, virial masses, selection functions, non-detections)
- **Types**: compute × 2, solo × 1
- **Theme**: the LRD survey's adversarial headline — the framework built an n_PBH bridge + a `proven_1450` "seed-mass spectrum" promissory note on top of an LRD anchor (M_BH~10⁷ M_⊙ → L_pix_LRD) that the OBSERVERS now dispute by 1–3 dex, while having NO compact-object sector at all (Row #88). This wave executes the survey's TWO substrate-physics computes (the seeds→envelope pivot, B2/B4/B5; the GGE-clustering test, B3) + the one mechanical precision band (R2). The two hygiene reconciliations (proven_1450 down-tag, lrd-constraints refresh) are session-track, routed OUT (seed HY1/HY2). The n_PBH tautology adjudication is the W4-2 workshop (LRD is a participant, so neutral-planned).

| # | Gate ID | gate_type | Suggested exec | One-line scope |
|:--|:--------|:----------|:---------------|:---------------|
| 1 | INV7-W2-1 | compute | little-red-dots-jwst-analyst (or cosmic-web) | ξ_GGE(r) two-point clustering of GGE-relic overdensities; slope + oscillatory feature vs LRD clustering excess (Paper 21) — GGE-interference-vs-ΛCDM at z~5 |
| 2 | INV7-W2-2 | compute | landau-condensed-matter-theorist (or volovik / spectral-geometer) | substrate accretion-photosphere temperature from the τ_fold van Hove fixed-point; ~5000 K Balmer-break + dust-free + non-variable package (seeds→envelope pivot) |
| 3 | INV7-W2-3 | solo | little-red-dots-jwst-analyst (or gen-physicist) | L_pix_LRD ∈ r_s([10⁵,10⁸] M_⊙) band propagated through n_PBH∝1/L_pix³ into the 7.28e-23 anchor (Class-8.3 precision-vs-systematic; INFO-by-construction) |

- **Natural-split candidates** (if the wave stalls): the three gates are already independently dispatchable (W2-1 observational-comparison compute; W2-2 substrate-fixed-point compute; W2-3 mechanical solo). If a split is needed: {INV7-W2-1, INV7-W2-2} the two substrate computes (both "fill the cement" of an LRD observable) | {INV7-W2-3} the solo precision band (no subagent spawn).
- **Shared inputs**: the post-transit GGE field correlation structure (co-machinery with W1-1/W1-5 field generator) + LRD clustering excess / dual-LRD scale (Paper 21 Tanaka, Paper 50, Paper 65) (W2-1); τ_fold=0.190 van Hove fold + an a₄/a₂-type spectral-moment ratio at the local Jensen deformation + the ~5000 K Balmer-break (Paper 52/25) + dust-free (ALMA M_dust<10⁶, Paper 19/60) + 97.5%-non-variable (Paper 18) (W2-2); the §VII.AX.OP-PROJ n_PBH formula (Row #65) + the virial-mass dispute range (Rusakov 10⁵-10⁷ / naive 10⁷-10⁸ / de Graaff black-hole-star length-caveat) (W2-3).
- **Cross-track note**: W2-1's GGE-clustering and W1-5's persistent-homology are complementary halves of convergence #3 (GGE-interference-vs-ΛCDM at two scales) — cross-reference, NOT a shared gate. W2-2 (compact-object envelope) and W3-1 (LQG compact-object entropy) are the two routes into the Row #88 empty cell (convergence #2). HY1/HY2/HY3 (proven_1450 down-tag, lrd-constraints refresh, Tier-2-loudness) are session-track hygiene — routed OUT to `/rclab-investigate --investigation 7` close, NOT investigation gates. W2-3's band-pin (if promoted) = session-track + mack.

## Wave 3 — loop-quantum-gravity cross-framework computes

- **Owner-planner**: `loop-quantum-gravity-theorist` (seed author; the structural-mirror programme — loop quantum cosmology, group field theory, isolated-horizon entropy)
- **Types**: compute × 3
- **Theme**: the LQG survey's discipline — distinguish STRUCTURAL (mathematical content isomorphic under an explicit dictionary) from ANALOGICAL (surface-similar, distinct dynamics) parallels, and import the loop-quantum-gravity machinery exactly where the framework has assembled everything except the closure. This wave executes the three importable computes: the modular-horizon entropy (UB-2/UB-4, type-III von-Neumann cousin of isolated-horizon entropy → seed the compact-object sector), the group-field-theory condensate resummation of the SDW sum (UB-3, the controlled-sum technology for the A_s/a₀ convergence wall), and the loop-quantum-cosmology pre-inflationary low-ℓ overlay (UB-5, same-instrument cross-check). The #1-leverage effective-Friedmann import (UB-1) is the W4-1 workshop (LQG is a participant, so neutral-planned). The two hygiene items (proven_493 down-scope, α_LIV leading-order) are session-track, routed OUT (seed HY4/HY5).

| # | Gate ID | gate_type | Suggested exec | One-line scope |
|:--|:--------|:----------|:---------------|:---------------|
| 1 | INV7-W3-1 | compute | loop-quantum-gravity-theorist (connes co-option for modular machinery) | modular-horizon entropy S=⟨−ln ρ_ω⟩ on A_hor=A_K⋊ℝ (§VII.BZ) vs a₂-area; test S∝A/(4 G_eff) (seed compact-object sector; entropy-matching M_KK pin) |
| 2 | INV7-W3-2 | compute | loop-quantum-gravity-theorist (or transit-dynamics) | GFT-condensate hydrodynamics over the GGE relic (59.8 pairs, P_exc=1, S_ent=0) → resummed convergent a₀ magnitude (SDW-convergence / JACOBSON-NONLOCAL-64); revive CF-S93-GFT-BLV-DICTIONARY |
| 3 | INV7-W3-3 | compute | loop-quantum-gravity-theorist (mack on CMB-datum comparison) | LQC pre-inflationary P(k) at ℓ∈[2,30] overlaid on framework n_s=0.9590/A_s, same instrument (Planck-low-ℓ/CMB-S4/LiteBIRD); revive CF-S93-LQG-CMB-CROSS-CHECK |

- **Natural-split candidates** (if the wave stalls): {INV7-W3-1} the modular-entropy compact-object compute (crossed-product machinery; connes co-option) | {INV7-W3-2, INV7-W3-3} the two CF-S93 revivals (GFT-condensate a₀ resummation + LQC-CMB overlay — both made tractable by the S101-S102 rank-1/condensate results).
- **Shared inputs**: §VII.BZ BDI Horizon-Faithfulness crossed product A_K⋊ℝ (S105-S106 STAGE-3-PERMANENT, modular flow σ_t^ω) + a₂→G_eff (C8) + Bekenstein-Hawking 1/(4 G_eff) slope (W3-1); the post-fold GGE relic (59.8 pairs, P_exc=1, S_ent=0, product state) + Tr f(D_K²/Λ²) generating functional + JACOBSON-NONLOCAL-64 + CF-S93-GFT-BLV-DICTIONARY (W3-2); the LQC bounce low-ℓ spectrum (Agullo-Ashtekar-Nelson) + framework n_s=0.9590 + A_s floor + matched low-ℓ window + CF-S93-LQG-CMB-CROSS-CHECK (W3-3).
- **Cross-track note**: INV7-W3-1 is COMPLEMENTARY to inv-4 W1-1/W1-2 (modular-flow vs Euclidean-replica/microstate-count — same observable S∝A/4G, distinct machinery) and to inv-5 W1-4 (entropy-area-scaling vs twist-scalarity — same crossed product, distinct functional). INV7-W3-2 is the FIFTH A_s/absolute-magnitude route (alongside inv-3 W2-3, inv-4 W1-4, inv-5 W2-1, inv-6 W2-2) — distinct controlled-sum machinery. INV7-W3-1 + W2-2 are the two routes into the Row #88 compact-object cell (which inv-6 kaluza-klein also touches). Each cross-reference MUST appear in the gate block.

## Wave 4 — cross-vantage adjudications (the two genuine Q1a workshops)

- **Owner-planner**: `gen-physicist` (NEUTRAL — not a participant in either workshop; writes balanced adjudication specs, NO orchestrator angle per `feedback_review-dispatch-no-orchestrator-angle.md`; mirrors the inv-3 W4 / inv-4 W3 / inv-5 W3 neutral-planner precedent for adjudication workshops)
- **Types**: workshop × 2
- **Theme**: the cluster's two genuine math/physics adjudications, each with opposed first-principles readings and essential cross-rebuttal. W4-1 is the cluster's #1-leverage item (the framework's #1 frontier, the effective-Friedmann functional form). W4-2 is the structural check on the framework's one quantitative LRD result.

| # | Gate ID | gate_type | Agents (EXACTLY 2, 2 rounds) | One-line scope |
|:--|:--------|:----------|:-----------------------------|:---------------|
| 1 | INV7-W4-1 | workshop | loop-quantum-gravity-theorist ↔ transit-dynamics-theorist | effective-Friedmann H²(ρ) from S_SA homogeneous reduction: LQC `(1−ρ/ρ_c)` bounce-form vs monotone-transit-form; "no bounce" general truth or scoped to monotone-RAMP? STRUCTURAL VERDICT on functional form. |
| 2 | INV7-W4-2 | workshop | little-red-dots-jwst-analyst ↔ lizzi-spectral-functional-theorist | n_PBH g-independence: sage_simplify factorization of §VII.AX.OP-PROJ as shared evidence; physical structural identity (lizzi: κ carries L_max-flowing content) vs convention tautology (LRD: 2^g and L_pix³ both DEFINED). STRUCTURAL VERDICT. |

- **gate_type rationale**: both are genuine Q1a per `Investigating-Workshops.md` — TWO+ agents, opposed first-principles readings of a SPECIFIC tension, multi-round (R1 steelman / R2 rebuttal / converge), output a STRUCTURAL VERDICT. W4-1: loop-quantum-gravity holds the LQC-effective-Friedmann template ("singularity-resolution role realized by a bounce at ρ_c"), transit-dynamics holds the supersonic-transit reading ("monotone dS/dτ, irreversible quench, no turning point") — the reduction of S_SA is the shared substrate both reason over, the bounce-vs-monotone functional form is the contested deliverable. W4-2: little-red-dots holds Reading B (convention tautology), lizzi holds Reading A (physical structural identity, and owns the `math-scripts.md` multiplicative-cancellation machinery) — the sage_simplify factorization is the shared evidence both read oppositely.
- **Natural-split candidates**: the two workshops are independent and independently dispatchable; no split needed. Each runs as a 2-agent / 2-round `/rclab-workshop`.
- **Shared inputs**: (W4-1) LQG UB-1/G-1/U-1/C-3 survey sections + capstone §6.3 (names the missing "H²=f(ρ_relic, S_SA)") + §VII.BS rank-1 NNU (a(t) shape DERIVED) + transit data (Mach 13.75, P_exc=1) + the loop-quantum-cosmology effective-Friedmann reference H²=(8πG/3)ρ(1−ρ/ρ_c), ρ_c≈0.41ρ_Pl. (W4-2) LRD R3/A3 survey sections + Row #65 §0 (the cancellation claim) + `math-scripts.md §"Multiplicative-normalization cancellation invariants"` (K=3 MANDATORY adjudication machinery) + the §VII.AX.OP-PROJ Tier-2-dimensionful-held status.
- **Independence note (both workshops)**: these are EXPLORATORY adjudications (domain advocates argue their case) — NOT Stage-2 joint-theorem cross-checks, so the no-prior-context rule does NOT apply; the advocates are SUPPOSED to bring their domain reading. The neutral planner (gen-physicist) writes the balanced spec and is NOT a participant in either. W4-1's transit-dynamics and W4-2's lizzi are NOT the wave-owners of W3/W2, which is precisely why a neutral planner authors the specs (the LQG/LRD owners are participants).
- **Wave-order dependency**: W4 runs alongside or after W1/W2/W3. W4-1 is independent of all compute verdicts (it adjudicates the functional FORM; the reduction is the shared reasoning substrate). W4-2's sage_simplify pre-flight is internal to the workshop (the §VII.AX.OP-PROJ producing script is on disk); independent of W1/W2/W3 verdicts. Both may run in the same batch as the compute waves.

---

## Dispatch summary

| Wave | Theme | Owner-planner | Types | Gates | Plan file |
|:----:|:------|:--------------|:------|:-----:|:----------|
| 1 | cosmic-web LSS observables | cosmic-web-theorist | compute×6 | 6 | investigation-7-plan-w1.md |
| 2 | little-red-dots high-z observational computes | little-red-dots-jwst-analyst | compute×2, solo×1 | 3 | investigation-7-plan-w2.md |
| 3 | loop-quantum-gravity cross-framework computes | loop-quantum-gravity-theorist | compute×3 | 3 | investigation-7-plan-w3.md |
| 4 | cross-vantage adjudications | gen-physicist (neutral) | workshop×2 | 2 | investigation-7-plan-w4.md |

4 per-wave planners dispatched in ONE parallel batch (≤8 concurrent). Total **14 gates** (11 compute + 1 solo + 2 workshop). Honest workshop count: **2** (the effective-Friedmann functional-form adjudication INV7-W4-1; the n_PBH physical-identity-vs-tautology adjudication INV7-W4-2). Compute/solo gates (W1/W2/W3, 12 gates) emit verdict lines to `computations/investigation-7/inv7_gate_verdicts.txt`; workshop gates (W4) close by artifact-existence.
