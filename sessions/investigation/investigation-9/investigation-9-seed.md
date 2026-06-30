# Investigation 9 — Seed Digest

**Date**: 2026-06-14 (S108–109 plateau)
**Mode**: investigation (`/rclab-plan --investigation 9`)
**Seed (`--from`)**: four investigation-1 survey outputs —
`investigation-1/kaku-speculative-theorist.md` + `investigation-1/string-theory-theorist.md` + `investigation-1/loop-quantum-gravity-theorist.md` + `investigation-1/kitaev-quantum-chaos-theorist.md`
(4-agent survey batch). Direct-seeded (no inv-1 `_synthesis.md` exists yet).
**Invocation note (flag → `--from`)**: the command was typed `--investigation 9 --context <4 files joined by &&>` (files 2–4 inherit the `investigation-1/` directory prefix). In investigation mode the seed IS the scope and is supplied via `--from`; `--context` is supplementary planner context only, and a bare `--context` with no `--from` is a hard-stop. The four files are investigation-1 **agent survey outputs** — the canonical `--from` seed shape. Unambiguous intent: seed investigation-9 from these four surveys. Treated as `--from`. (No separate `--context` files were supplied.) Identical precedent: inv-3, inv-4, inv-5, inv-6, inv-7, inv-8, inv-10 — all typed `--context`, all resolved to `--from`.
**Number note**: the index carries rows 1–8 + 10 (investigation-10 was registered concurrently while inv-9 was being planned — a parallel inv-1 fanout; the 9 slot was left for this invocation). investigation-9 fills the open 9 slot; the sequence is gap-free 1-…-10. Numbering honored as typed.
**Shape**: fanout (3 per-wave plan files + thin plan-index).
**Driver**: investigation-1 (the wholesale S108/S109 survey). The **cross-framework quantum-gravity + holography/information** cluster: the cross-domain structural pattern detector (kaku), the cross-framework string/M-theory walls specialist (string-theory), the *other* background-independent quantum-gravity programme held as a structural mirror (loop-quantum-gravity, REUSED — consumed by inv-7), and the chaos/integrability diagnostician (kitaev, REUSED — consumed by inv-10). A 4-agent batch; **two of the four are reused agents whose computes are consumed elsewhere, so their fresh inv-9 role is workshop-only** (see DEDUP).

**Scope discipline**: the seed IS the scope (Safety rule 7). Every candidate gate below traces to a specific seed finding (gap G-x · contradiction C-x · assumption A-x/U-x · refinement R-x · bridge B-x/UB-x · highest-leverage-next-step). No invented items. Training knowledge is NOT a source — every numeric anchor below is lifted from a seed agent's own in-session MCP query and is RE-verified at plan-freeze by the per-wave planner.

---

## Source manifest (each agent is sole writer of its inv-1 file)

| Seed file | Vantage | Next-steps mined | Convergence flags |
|:----------|:--------|:-----------------|:------------------|
| `kaku-speculative-theorist.md` | cross-domain structural pattern detector — God-equation unification, matrix/IKKT models, KK, swampland, dimensional transmutation, second-quantization (SFT) | 5 (NS 1–5; lines 200-214) — **all 5 FRESH, all gated** | modular-flavor B-1 ↔ string B-1 (IDENTICAL); GGE-Fock-sum B-5 ↔ string G-1/C-1 (OPPOSED); swampland B-2 ↔ string R-3; zeta-Brody B-4 ↔ kitaev U2/U3 |
| `string-theory-theorist.md` | cross-framework specialist — string/M-theory walls, dualities, swampland, holography, K-theory, the Q7 SUM-vs-NO-SUM verdict | 5 (NS 1–5; lines 152-164) — **all FRESH; NS-1 = kaku NS-1 (one gate), NS-4 → W3-1 workshop** | modular-flavor B-1 ↔ kaku B-1 (IDENTICAL); SUM-vs-NO-SUM / two-roads C-1 ↔ kaku B-5 (OPPOSED); swampland refresh R-3 ↔ kaku B-2; species-count dS entropy B-4 |
| `loop-quantum-gravity-theorist.md` | the *other* background-independent QG programme. **REUSED AGENT — all 5 next-steps consumed by inv-7.** | 5 (NS 1–5; lines 113-121) — **ALL consumed by inv-7 (see DEDUP); workshop-only role (W3-2)** | discrete-vs-continuous-spacetime C-2 ↔ kitaev C3; semiclassical-limit G-3; QG-character lens ↔ kitaev |
| `kitaev-quantum-chaos-theorist.md` | chaos/integrability diagnostician — ⟨r⟩, OTOC λ_L, SFF, Krylov, RP resonances, ETH, GGE. **REUSED AGENT — 4 integrability computes consumed by the concurrent inv-10.** | 5 (NS 1–5; lines 137-147) — **NS-2/3/4/5 (U1/U2/U3/U4) consumed by inv-10 (see DEDUP); NS-1 = HY1; workshop-only role (W3-2)** | GGE-emergence U1 ↔ kaku B-5 / string C-1; zeta/integrability U2/U3 ↔ kaku B-4; black-hole-machinery-import C3 ↔ LQG / string holography |

---

## Thesis (cross-agent convergence)

The four vantages converge on **how the substrate relates to the mature quantum-gravity / holography / quantum-chaos programmes** — and the headline finding is that *the framework's relationship to its sibling programmes is more closed than the framework as a whole*, so the leverage is overwhelmingly in **importing their MECHANISMS as substrate-fillers** (kaku's "mine it as a toolbox"; string's "the wall tells us what cement to pour"), not in seeking new correspondences. After the inv-7 (LQG) and inv-10 (kitaev) dedup, inv-9's FRESH spine is carried by kaku + string, with kitaev and LQG supplying the adversarial workshop voices. Two fresh structural convergences organize the investigation:

1. **Modular flavor symmetry is the single highest-leverage bridge, flagged #1 by TWO independent vantages.** kaku **B-1** (NS-1) and string **B-1** (NS-1) propose the *identical* compute: expand the generation-relevant matrix elements of `D_K(τ)` near `τ_fold = 0.190` and test whether they organize as a Dedekind-η-like modular form, with the hierarchy an `ε`-power expansion `ε = f(τ − τ_critical)` weighted per-generation by the Casimir `C₂(p,q)`. Both name it as the route that closes the rank-1 Yukawa wall (G-2) from geometry. The framework's own S103 gem-triage already flagged arXiv:2506.23343 here. → **one** compute gate (INV9-W1-1), NOT two.

2. **The "sum-over-geometries" / information-paradox question is the cluster's sharpest *adversarial* tension — kaku and string explicitly DISAGREE.** string **G-1/C-1**: the framework has one fixed `D_K`, no `∫ Dg`, a "legitimate different road," and "the information story is incomplete where string theory's is not." kaku **G-3/B-5**: "I am less willing to concede that" — the GGE relic is a many-body Bogoliubov Fock space, so the framework's "sum" is the *Fock trace over quasiparticle occupations* `Z = Tr_Fock e^{−βH_BdG}`, finite and well-defined, which could produce a Page-curve turnover with no `∫ Dg`. kitaev **U1** supplies the decisive shared evidence: λ_L = 0 across 4 functionals (S38–S104) ⇒ the substrate *cannot scramble*, so any Page curve must come from integrable-GGE *dephasing*, not scrambling. → the kaku compute that produces the evidence (INV9-W1-5 Fock partition function) + the **adjudication workshop** (INV9-W3-1, kaku ↔ string). *(The companion Born-rule-from-GGE-projection compute is inv-10 W3-1, kitaev — consumed there, cross-referenced here.)*

**Secondary convergence (swampland / dimensional-transmutation sector):** kaku's God-equation reading collapses M_KK, τ_fold, K_pivot, A_s into ONE missing sector — *dimensional transmutation + quintessence-rolling moduli dynamics* — and string theory built exactly that sector for forty years. kaku **B-2** (swampland gradient-bound on the monotonic `S(τ)` + Volovik `V(q)`; the framework's "no minimum" weakness IS the swampland-mandated structure) + string **R-3/B-5** (modern swampland refresh; the framework's `w0_FW = −0.918` is already refined-dS-aligned) + kaku **B-3** (BCS gap as the dimensional-transmutation event fixing `Δ_BCS/M_KK`).

**Third theme (cross-framework QG-character), carried by the W3-2 workshop:** the substrate is *measured-integrable / non-chaotic / non-holographic* (kitaev: λ_L=0 across 4 functionals; a hard structural result) — is that ordered character the right lens (integrability machinery), or is the substrate better read as the background-independent-QG cousin (LQG: continuous-g_M, internal-discreteness)? This is the genuine fresh role for the two reused agents (kitaev ↔ LQG).

### Cross-agent convergence map

| Convergence | kaku | string | kitaev | LQG | Investigation route |
|:------------|:-----|:-------|:-------|:----|:--------------------|
| **Modular flavor → Yukawa wall** (#1, IDENTICAL) | B-1 / NS-1 | B-1 / NS-1 | — | — | INV9-W1-1 (one compute; flagship convergence) |
| **Sum-over-geometries / Page-curve / information** (OPPOSED readings) | B-5 / G-3 / NS-5 | G-1 / C-1 / NS-4 | U1 (λ_L=0 evidence; compute → inv-10 W3-1) | (G-3 semiclassical) | INV9-W1-5 (kaku compute) + **INV9-W3-1 workshop** (kaku ↔ string) |
| **Substrate QG-character lens** (integrable vs background-indep-QG) | R-1 (matrix/fuzzy) | A-3 (non-holography a choice) | C3 (no black-hole import) | C-2 (discrete-vs-continuous) | **INV9-W3-2 workshop** (kitaev ↔ LQG) |
| **Swampland / dimensional-transmutation sector** | B-2, B-3 | R-3, B-5 | — | U-4 (Immirzi prior) | INV9-W1-2 (gradient-bound compute) + INV9-W1-3 (BCS transmutation) + INV9-W2-3 (swampland refresh review) |
| **Integrability / zeta / spectral-statistics** | B-4 (zeta-Brody) | — | U2, U3, U4 (computes → inv-10 W3-2/3/4) | — | INV9-W1-4 (kaku zeta-Brody; the integrability-suite computes are inv-10's) |
| **Cross-framework mechanism imports** (Sen, species-count) | — | B-2, B-4 / NS-2,3 | — | (UB-1..5 consumed inv-7) | INV9-W2-1 (Sen K-theory) + INV9-W2-2 (dS species-count) |

---

## DEDUP — cross-investigation overlap (load-bearing; read before the candidate table)

**Two of inv-9's four agents are reused agents whose computes are consumed by sibling investigations.** This is the dominant dedup fact of inv-9 and the reason it has no kitaev wave and no LQG wave — only kaku + string compute waves + two cross-framework workshops.

### (A) LQG — all five next-steps consumed by investigation-7

inv-7 (cosmic-web + little-red-dots + loop-quantum-gravity) lifted LQG's entire top-5 (`investigation-7-seed.md §"Candidate gate table"` + §"Non-gate items"):

| LQG inv-1 next-step | inv-7 disposition | inv-9 action |
|:--------------------|:------------------|:-------------|
| **NS-1 / UB-1** — LQC effective-Friedmann `H²(ρ)` back-reaction closure | **INV7-W4-1** workshop | NOT re-planned. Cross-ref only. |
| **NS-4 / UB-2 + UB-4** — modular-horizon entropy `S ∝ A/4G_eff` | **INV7-W3-1** compute | NOT re-planned. Cross-ref only. |
| **NS-5a / UB-3** — GFT condensate → resummed `a₀` | **INV7-W3-2** compute | NOT re-planned. Cross-ref only. |
| **NS-5b / UB-5** — LQC pre-inflationary low-ℓ overlay | **INV7-W3-3** compute | NOT re-planned. Cross-ref only. |
| **NS-2/NS-3/C-3** — proven_493, α_LIV, no-bounce hygiene | **inv-7 HY4/HY5/HY6** (routed out) | Already captured. NOT re-routed. |

### (B) kitaev — four integrability computes consumed by the concurrent investigation-10

investigation-10 (tesla-resonance + quantum-acoustics + **kitaev**) was registered + seed + partitioned CONCURRENTLY while inv-9 was being planned (the index changed mid-plan). Its `investigation-10-seed.md §"Wave 3"` + `investigation-10-partition.md §"Wave 3"` claim kitaev's ENTIRE integrability suite, with a superset of the seed anchors:

| kitaev inv-1 next-step | inv-10 gate | inv-9 action |
|:-----------------------|:------------|:-------------|
| **NS-2 / U1 / G1 / A1** — GGE-projection origin of QM (modular flow σ_t^ω, K₇=0, Born-rule structure) | **INV10-W3-1** compute | NOT re-planned. Cross-ref only. |
| **NS-3 / U2 / R2 / A4** — RP-resonance spectrum across the fold (power-law C(t)~t^{−1/2}) | **INV10-W3-2** compute | NOT re-planned. Cross-ref only. |
| **NS-4 / U3 / R3 / G2 / A3** — Σ²(L) + connected SFF deep-truncation rigidity | **INV10-W3-3** compute | NOT re-planned. Cross-ref only. |
| **NS-5 / U4 / C2** — ETH-violation test on the L12 cache | **INV10-W3-4** compute | NOT re-planned. Cross-ref only. |
| **NS-1 / C1 / R1** — chaotic-instantons down-tag (scrambling-origin CLOSED) | **inv-10 HY1** (routed out) | Cross-ref; inv-9 records HY1 too (both close to session-promotion). |

inv-10 is the RIGHT home for kitaev's computes: its theme is *the post-fold GGE acoustic power spectrum + the integrability of the relic* (kitaev's integrability suite is CORE there), whereas in inv-9 kitaev's computes were tangential to the kaku/string cross-framework-QG theme. The dedup is exact (identical U1/U2/U3/U4 anchors).

### (C) Consequence (honest scoping, `feedback_fix-in-session-never-defer.md` no-padding)

Both LQG and kitaev contribute to inv-9 **only as cross-framework workshop voices** (INV9-W3-2). Manufacturing fresh LQG/kitaev compute gates would duplicate inv-7 / inv-10 or pad below top-5 — both forbidden. This is the **inv-5 spectral-geometer precedent** (reused agent → reduced role) applied twice. inv-9's fresh compute content is carried entirely by **kaku (W1, 5 gates) + string (W2, 3 gates)**; the two waves of the originally-anticipated kitaev/LQG computes are owned by inv-10/inv-7. kaku and string are NOT used by any other investigation — inv-9 remains a fresh, high-value investigation, just smaller (3 waves, 10 gates).

### (D) Cross-investigation adjacencies for the FRESH agents (complementary, NOT duplicate)

Each adjacency is **complementary (distinct machinery / distinct observable)**; each gate block MUST carry its cross-reference so `/rclab-coordinate` does not see redundancy.

| inv-9 gate | Adjacent prior gate | Disposition |
|:-----------|:--------------------|:------------|
| **INV9-W1-1** (modular-flavor form of `D_K(τ)`) | **inv-2** (off-U(2) Yukawa) + **inv-5 W1-3/W1-4** (connes ε_LX, lepton ladder, modular twist) | **Complementary — same G-2 Yukawa wall, distinct machinery.** W1-1 tests the *modular-form weight structure* (ε=f(τ−τ_critical), C₂-graded); inv-2 is off-U(2) *geometry*; inv-5 is connes *machinery* (ε_LX residual). The modular-form route DERIVES what inv-5's ε_LX backs out. NOT a re-plan. |
| **INV9-W1-4** (substrate-zeta off-critical-zero distance vs Brody β) | **inv-3 W1-1/W1-2** (berry SFF + number-variance, low-L) + **inv-10 W3-2/W3-3** (kitaev RP + Σ²/SFF) | **Complementary — same spectral-statistics family, distinct observable.** W1-4 is the zeta-zero↔Brody-β number-theoretic bridge (Berry-Tabor⟺Hilbert-Pólya); inv-3 is low-L level-statistics; inv-10 W3-2/W3-3 are RP-resonances + rigidity (kitaev's consumed computes). W1-4 is kaku's distinct number-theoretic angle. NOT a re-plan. |
| **INV9-W1-5** (GGE Fock partition function, Page-curve) | **inv-10 W3-1** (kitaev GGE-projection Born rule) + **inv-8 W2-3** (Born rule via 8-RG trace) + **inv-8 W4-1** (Bell) | **Complementary — same GGE object, distinct observable.** W1-5 is the Fock *partition function* Page-curve turnover (kaku); inv-10 W3-1 is *Born-rule emergence* from modular flow (kitaev); inv-8 W2-3 is the RDM-trace Born rule; inv-8 W4-1 adjudicates classical-vs-quantum. NOT a re-plan. |
| **INV9-W2-2** (dS entropy as substrate species-count) | **inv-4 W3-1** + **inv-5 W1-5** + **inv-7 W3-1** + **inv-8 W2-1** | **Complementary — same CC/dS-entropy target, distinct functional.** W2-2 is the *finite species-count* reading (count modes below Λ_sp/M_KK=2.06) — distinct from first-law / entropy-functional / modular-flow / entanglement-variation. Cross-reference all four. |
| **INV9-W1-3** (BCS gap: is Δ_BCS/M_KK geometry-fixed?) | **inv-3 W4-1** + **inv-6 W4-1** (M_KK derivability / determination-route) | **Complementary — same M_KK gap, distinct mechanism.** W1-3 is the *dimensional-transmutation* reading (condensate-as-transmutation-scale). NOT a re-plan. |
| **INV9-W2-1** (Sen-tachyon K-theory descent) | — | **FRESH.** No prior investigation touched Sen condensation / K_0(A_F) transit-change. |
| **INV9-W1-2 + INV9-W2-3** (swampland gradient-bound + refresh) | — | **FRESH.** falsifier-inventory has NO swampland rows; kaku's CF14 opened S47, never revisited. |
| **INV9-W3-1** (sum-over-geometries adjudication, kaku↔string) | — | **FRESH adjudication.** string's "two roads" was a never-run Q7 seed; subsumed + sharpened here. |
| **INV9-W3-2** (substrate QG-character lens, kitaev↔LQG) | inv-7 (LQG computes) / inv-10 (kitaev computes) | **FRESH.** No prior/concurrent investigation adjudicates the integrability-vs-background-independent-QG LENS; this workshop does NOT re-open the consumed computes — it adjudicates the reading. Carry the inv-7/inv-10 cross-refs. |

---

## Candidate gate table (10 gates → 3 waves)

Naming `INV9-W{wave}-{n}`. `gate_type` per `r3-yaml-gate-block.yaml`. "Exec" = suggested gate-executor `agent_type` (the per-wave planner finalizes by substrate match); "Owner" = wave planner. Effort estimates are the survey authors' own. All numeric anchors are seed-author values, RE-verified by the per-wave planner at plan-freeze against the knowledge MCP.

### Wave 1 — kaku-speculative-theorist: cross-domain structural bridges / the dimensional-transmutation sector (owner-planner: `kaku-speculative-theorist`)

| Gate | type | Exec | Scope | Seed anchor |
|:-----|:-----|:-----|:------|:------------|
| INV9-W1-1 | compute | connes-ncg-theorist (+ string co-option) | **FLAGSHIP CONVERGENCE (kaku NS-1 = string NS-1).** Expand the generation-relevant matrix elements of `D_K(τ)` around τ_fold=0.190; test whether they organize as a Dedekind-η-like modular form in (τ−τ_critical); C₂(p,q)-graded couplings reproduce the Yukawa hierarchy as ε-powers (ε=f(τ−τ_fold)) ⇒ close the rank-1 wall from geometry AND supply a principled τ↔K e-fold map. | kaku B-1/NS-1 · string B-1/NS-1 · G-2 · A1/K_pivot |
| INV9-W1-2 | compute | kaku-speculative-theorist (+ volovik co-option) | Swampland gradient-bound: \|S'(τ)\|/S(τ) at τ_fold (dS/dτ=+58,673) AND \|V'(q)\|/V(q) (Volovik k=+3586.5 M_KK, S97); both > c~O(1) ⇒ swampland-consistent AND τ-dynamics forced quintessence-rolling (resolves the A4 fork). Data-already-exists, low effort. | kaku B-2/NS-2 · C-3 · A4 |
| INV9-W1-3 | compute | kaku-speculative-theorist (+ nazarewicz/landau co-option for HFB) | BCS dimensional transmutation: close the BCS gap equation self-consistently from the Kosmann coupling alone (scale-free SU(3)); is Δ_BCS/M_KK=0.4642547 geometry-FIXED ⇒ M_KK reinterpreted as a Λ_QCD-like transmutation anchor, strengthening §VII.BS rank-1. Needs full HFB (mean-field overestimates ~60%, B4). | kaku B-3/NS-3 · G-1/M_KK · G-2 |
| INV9-W1-4 | compute | kaku-speculative-theorist (+ kitaev co-option for Brody β) | Substrate-zeta off-critical-zero distance vs Brody β(τ): compute the S105 FAILS-OWN-RH zero distribution (`5243d76d`) at several τ, correlate distance-from-critical-line with β=0.633 (Berry-Tabor⟺Hilbert-Pólya); monotone ⇒ off-critical spread is a window onto GGE thermalization (non-`∫Dg` Page-curve input). | kaku B-4/NS-4 · G-4 · C-1 |
| INV9-W1-5 | compute | kaku-speculative-theorist (+ transit/connes co-option) | GGE Fock partition function Z=Tr_Fock exp(−βH_BdG) (finite spectrum ⇒ well-defined); test for an entanglement-entropy Page-curve turnover as the integrable GGE thermalizes (t_therm~6 nat-units, T3) ⇒ a Page-curve analog WITHOUT `∫Dg` (the "sum over geometries" IS the Fock trace). Cross-ref inv-10 W3-1 (kitaev GGE-projection Born rule, distinct observable). | kaku B-5/NS-5 · G-3 · C-1 |

### Wave 2 — string-theory-theorist: cross-framework walls / mechanism imports (owner-planner: `string-theory-theorist`)

| Gate | type | Exec | Scope | Seed anchor |
|:-----|:-----|:-----|:------|:------------|
| INV9-W2-1 | compute | string-theory-theorist (+ connes co-option for K-theory) | Sen-tachyon K-theory descent: does the supersonic transit change the K-theory class K_0(A_F) (rank-3, S85 W10)? The framework HAS the tachyon (TRANSIT-279: 279 scalar fluctuations tachyonic at all τ/cutoffs = the NCG analog of Sen open-string condensation). PASS = K_0 class changes ⇒ a genuine Sen condensation, importing a unitary info-preserving dynamics (fills G-1, mechanism for the Ordered-Veil C-1). | string B-2/NS-2 · G-1 · C-1 |
| INV9-W2-2 | compute | string-theory-theorist (+ hawking co-option for horizon thermodynamics) | dS entropy as substrate species-count: count D_K eigenvalues in the species shell [M_KK, 2.06 M_KK] at the fold (Λ_sp/M_KK=2.06 THIN, S36); compare log(count) to Gibbons-Hawking S_dS=3π/(Λℓ_P²) with Λ from the a₀ moment. PASS = match to O(1) ⇒ a FINITE, non-holographic species-counting CC mechanism. | string B-4/NS-3 · C-2 · A-3 |
| INV9-W2-3 | review | string-theory-theorist (solo + paper-search fetch) | Modern swampland refresh: re-run the swampland audit (pre-2018, 38 closures) against 2018–2025 conjectures — refined dS (OPSV 2018; w0_FW=−0.918 alignment), sharpened Distance, Emergent String (LLW 2019), species scale; classify the τ→0 / large-τ infinite-distance limits against the Emergent-String dichotomy. `researchers/String-Theory/` has ZERO 2018-2025 papers — fetch required. | string R-3/B-5/NS-5 |

### Wave 3 — cross-framework adjudications (owner-planner: `gen-physicist`, NEUTRAL)

| Gate | type | Agents (EXACTLY 2, 2 rounds) | Scope | Seed anchor |
|:-----|:-----|:-----------------------------|:------|:------------|
| INV9-W3-1 | workshop | kaku-speculative-theorist ↔ string-theory-theorist | **Sum-over-geometries / Page-curve / information.** STRUCTURAL VERDICT: does the framework have a sum-over-geometries, or categorically forgo it? kaku (B-5/G-3): the GGE Bogoliubov Fock space IS the sum (`Z=Tr_Fock e^{−βH_BdG}`, a finite trace over occupations of the FIXED D_K), and can produce a Page-curve turnover with no `∫Dg`. string (G-1/C-1): one fixed D_K, no `∫Dg`, a legitimate "different road," information story incomplete. Shared evidence both read oppositely: kitaev's λ_L=0 (no scrambling) + the INV9-W1-5 (Fock partition function) compute + inv-10 W3-1 (GGE-projection Born rule). | kaku G-3/B-5/NS-5 · string G-1/C-1/NS-4 · kitaev U1 |
| INV9-W3-2 | workshop | kitaev-quantum-chaos-theorist ↔ loop-quantum-gravity-theorist | **Substrate QG-character lens.** STRUCTURAL VERDICT: through which lens is the substrate's horizon/emergence physics correctly read, and which imported machinery is legitimate? kitaev (C3): the substrate is measured-integrable (λ_L=0), non-holographic, no SYK/JT dual — importing black-hole/Hayden-Preskill/Page/holographic machinery is illegitimate; emergence lives in integrability machinery (GGE/RP/ETH/Type III₁). LQG (C-2/G-3): the substrate is the continuous-g_M, internal-discreteness cousin of background-independent QG — SOME cross-QG imports ARE structural (effective-Friedmann, isolated-horizon entropy, GFT), on the opposite side of the discrete-vs-continuous-spacetime divide. The genuine fresh inv-9 role for the two reused agents; does NOT re-open their consumed computes (inv-7 / inv-10). | kitaev C3/A2 · LQG C-2/G-3/R-3 |

---

## 4-field specs

**Wave 1 (kaku):**
- **INV9-W1-1** — *What*: modular-form weight test of the bottom-N D_K(τ) generation-matrix-elements near τ_fold; ε-power Yukawa hierarchy weighted by C₂(p,q). *Inputs*: D_K(τ) spectrum + eigenvectors near τ_fold=0.190 (L12 cache / GT-builder); C₂(p,q) Peter-Weyl gradings; the Yukawa-hierarchy target (10⁵; `S96-MATTER-R-HIERARCHY`=9.86); the Dedekind-η threshold structure (R-3, latent); arXiv:2506.23343 (gem-triage). *Gate*: couplings organize as a definite-weight modular form reproducing the hierarchy as ε^{C₂}-powers with ε=f(τ−τ_fold) PASS / no modular structure FAIL / partial INFO. *Effort*: ~2 sessions. (Any §VII landing / canonical pin = session-promotion + designated writer.)
- **INV9-W1-2** — *What*: \|S'(τ)\|/S(τ) at τ_fold and \|V'(q)\|/V(q), vs swampland c~O(1). *Inputs*: dS/dτ=+58,673 + spectral-action value; Volovik V(q)=ε(q)−μq with k=+3586.5 M_KK (S97 W2-2). *Gate*: both ratios > c~O(1) PASS / either below FAIL / one-sided INFO. *Effort*: ~1 session (data exists). Lowest-effort, high-information.
- **INV9-W1-3** — *What*: self-consistent BCS gap-equation solution from the Kosmann coupling; is Δ_BCS/M_KK geometry-fixed? *Inputs*: the Kosmann interaction (scale-free SU(3)); 1D BCS theorem (B1); Δ_BCS=0.4642547 M_KK; the Q15 HFB iteration (never run). *Gate*: dimensionless ratio reproduced from geometry alone PASS / scale-dependent residual FAIL / approximate INFO. *Effort*: ~2 sessions (HFB).
- **INV9-W1-4** — *What*: substrate-zeta off-critical-zero distance vs Brody β(τ) correlation. *Inputs*: `S105-W7-5-SUBSTRATE-ZETA-ZEROS` (`5243d76d`); ζ_{D_K}(s)=Σ m_k λ_k^{−s}; Brody β=0.633 (T3) at several τ; Mellin-Dirichlet identity (N5). *Gate*: monotone distance↔β relationship PASS / no correlation FAIL / weak INFO. *Effort*: ~1-2 sessions. Cross-ref inv-10 W3-2/W3-3 (kitaev RP/rigidity — distinct observable).
- **INV9-W1-5** — *What*: GGE Fock partition function Z=Tr_Fock e^{−βH_BdG}; entanglement-entropy Page-curve turnover. *Inputs*: the GGE relic Fock space (59.8 Bogoliubov pairs, T2-T4); H_BdG on the finite spectrum; t_therm~6 nat-units (T3, INTEG-39). *Gate*: EE turnover present PASS (non-`∫Dg` Page curve) / monotone EE FAIL / ambiguous INFO. *Effort*: ~2 sessions. Cross-ref inv-10 W3-1 (GGE-projection Born rule, distinct observable) + INV9-W3-1 (the workshop this feeds).

**Wave 2 (string):**
- **INV9-W2-1** — *What*: K_0(A_F) class of the pre- vs post-transit configuration (Sen descent). *Inputs*: TRANSIT-279 (`s48_qa_tachyon.py`); rank K_0(A_F)=3 (S85 W10); the 2D landscape S(τ,φ) saddle; Witten 1998 K-theory. *Gate*: K_0 class changes across the transit PASS / unchanged FAIL / ambiguous INFO. *Effort*: ~1-2 sessions.
- **INV9-W2-2** — *What*: log(eigenvalue-count in [M_KK, 2.06 M_KK]) vs Gibbons-Hawking S_dS. *Inputs*: the L_max=10 spectrum (155,984 eigenvalues); Λ_sp/M_KK=2.06 (S36); the a₀ moment → Λ; S_dS=3π/(Λℓ_P²). *Gate*: log(count) matches S_dS to O(1) PASS / OOM mismatch FAIL / order-right INFO. *Effort*: ~1-2 sessions. Cross-ref inv-4 W3-1 / inv-5 W1-5 / inv-7 W3-1 / inv-8 W2-1 (same target, distinct functional).
- **INV9-W2-3** (review) — *What*: swampland audit refresh against 2018-2025 conjectures + Emergent-String classification of the τ-limits. *Inputs*: the pre-2018 swampland audit (`cross-framework-comparisons.md`, 38 closures); w0_FW=−0.918; Δτ/M_Pl=0.170; Λ_sp/M_KK=2.06; a paper-search fetch (OPSV 2018, LLW 2019, Dvali species-scale). *Output*: one synthesis md (no verdict line — artifact-existence closure); each conjecture tagged CONSISTENT / TENSION / classified. *Effort*: ~1 session + fetch. Cross-ref INV9-W1-2 (the gradient-bound compute is the specific instance of this broad audit).

**Wave 3 (adjudications — neutral planner, EXACTLY 2 agents each):**
- **INV9-W3-1** (workshop) — *adjudication_question*: (a) Does the framework possess a sum-over-geometries? kaku: YES — the GGE Bogoliubov Fock space is the sum (`Z=Tr_Fock e^{−βH_BdG}`, a finite trace over occupations of the FIXED D_K). string: NO — one fixed D_K, no `∫Dg`, legitimate "different road," information story incomplete. (b) Can the framework produce a Page-curve turnover, given kitaev's λ_L=0 (no scrambling)? (c) STRUCTURAL VERDICT: hidden-Fock-sum vs categorical-no-sum + is the Ordered-Veil information story complete. *Sources*: kaku G-3/B-5 + string G-1/C-1/Q7-workshop SUM-vs-NO-SUM verdict + kitaev U1 (λ_L=0 + GGE-dephasing) + INV9-W1-5 (Fock partition function) + inv-10 W3-1 (GGE-projection Born rule) as shared evidence. *Closure*: artifact-existence; NO verdict line. **Neutral planner (gen-physicist), NO orchestrator angle** (`feedback_review-dispatch-no-orchestrator-angle.md`). Exploratory adjudication (advocates argue their domain reading), NOT a Stage-2 cross-check — the no-prior-context rule does NOT apply.
- **INV9-W3-2** (workshop) — *adjudication_question*: (a) Through which lens is the substrate's horizon/emergence physics correctly read — measured-integrability (kitaev) or background-independent QG (LQG)? (b) Is the framework's import of black-hole/Hayden-Preskill/Page/holographic machinery illegitimate (kitaev: λ_L=0, non-holographic, no SYK/JT dual) or are SOME cross-QG imports structural (LQG: effective-Friedmann, isolated-horizon entropy, GFT are genuine background-independent-QG parallels; continuous-g_M / internal-discreteness on the opposite side of the discrete-vs-continuous divide)? (c) STRUCTURAL VERDICT: the substrate's QG-character classification + a ruling on which imported machinery legitimately applies. *Sources*: kitaev C3/A2 (no-black-hole-import) + LQG C-2/G-3 (discrete-vs-continuous discriminator, semiclassical-limit, the UB-series structural parallels) + the substrate's horizon apparatus (acoustic white hole, KIND-tagged surface gravity, §VII.BZ modular corridor) as shared evidence. *Closure*: artifact-existence; NO verdict line. **Neutral planner (gen-physicist), no orchestrator angle.** Gives the two reused agents (kitaev, LQG) their genuine fresh inv-9 role. Cross-ref inv-7 (LQG's consumed computes) + inv-10 (kitaev's consumed computes) — this workshop adjudicates the LENS, does NOT re-open them.

---

## Routed OUT — Q2 session-track hygiene (NOT investigation gates)

An investigation cannot mutate curated session-track registers (track-local boundary, `gate-verdicts.md §"Investigation-Track Canonical Path"`). These route to session-promotion at `/rclab-investigate --investigation 9` close, NOT to gates in this plan.

| HY | Item | Seed anchor | Session-track target | Note |
|:---|:-----|:------------|:---------------------|:-----|
| HY1 | Down-tag `framework-chaotic-instantons.md` §4/§7.1(B)/§8.2 ("lossy compression marginally viable") → scrambling-origin-of-QM corridor CLOSED, λ_L=0 across 4 functionals (S38–S104); ADD an atlas-09 retraction row. Capstone-hygiene Q3; designated-writer patch. | kitaev C1/R1/NS-1 | `framework-chaotic-instantons.md` + `atlas-09-retractions.md` | **ALSO routed by inv-10 (HY1).** Both close to session-promotion; `/rclab-investigate` dedups at close. |
| HY2 | Register "emergence of QM-form on this substrate" as an explicit **ASSUMED** entry in atlas-04 (currently load-bearing-by-assertion; scrambling mechanism falsified by λ_L=0, Fermi-point inapplicable by N₃=0). | kitaev A1/G1 | `atlas-04-assumptions.md` | The surviving-mechanism COMPUTE is inv-10 W3-1 (GGE-projection); this is the register-tag edit. |
| HY3 | Down-tag the "MSS chaos bound trivially satisfied" framing wherever it is listed as a *passed test* — a bound satisfied with infinite margin (0 ≤ 2πT) constrains nothing. | kitaev A2 | atlas / capstone scorecard | Adjacent to inv-10 HY3 (ADH-vs-t_therm); both session-track. |

**Already captured — NOT re-routed:** LQG hygiene (proven_493, α_LIV, no-bounce) = **inv-7 HY4/HY5/HY6**; kitaev's chaotic-instantons + ADH reconciliation are co-surfaced by **inv-10 HY1/HY3**. These do NOT generate new inv-9 routing beyond the cross-reference above.

---

## Surveyed-but-not-elevated bridges (context cross-refs, NOT gates)

Per the no-padding discipline, these surfaced in the surveys but are EVOI-ordered out of this round (below the authors' top-5, or refinements, or consumed elsewhere). Recorded so they are not lost; not gated:

- **kaku R-3** (Dedekind-η threshold corrections → α_GUT two-loop, Q18a): not in kaku's top-5; adjacent to inv-6 (kaluza-klein threshold running). The Dedekind-η structure is a strong hint the INV9-W1-1 modular structure is latent — cross-ref in W1-1 context.
- **kaku R-1** (re-classify the substrate against finite fuzzy-geometry, not the failed IKKT power-law): folded into INV9-W3-2 (QG-character lens) kaku-context (cross-ref), not a separate gate.
- **kaku R-5** (Leggett/Bogoliubov-mode QNM analog as the one computable compact-object observable): adjacent to the Row #88 compact-object cell (inv-4/6/7/8); deferred — the inv-7/inv-8 compact-object routes are higher-leverage.
- **kaku R-2 (RED-flag, keep closed)**: the "spectral-dimension flow 12→5.65→4 ∥ string 10→2→4" CDT bridge is REFUTED (S31Aa/S92; S_d={0,2,4,6,8} τ-INDEPENDENT). Marked RED so no future agent re-proposes it.
- **string R-2** (intra-sector V_(p,q)–ℂ¹⁶ entanglement loophole, bounded by 2log16): adjacent to the CKM/δ_CP work (§VII.BX); deferred, low-leverage.
- **kitaev integrability suite (U1/U2/U3/U4) + LQG UB-series**: CONSUMED by inv-10 / inv-7 respectively (see DEDUP) — not inv-9 gates. kitaev's G-3 (no compact-object chaos cross-check) + LQG's G-3 (coherent-state semiclassical-limit) are folded into INV9-W3-2 context.

---

## Wave preview (→ partition)

| Wave | Theme | Owner-planner | Types | Gates |
|:----:|:------|:--------------|:------|:-----:|
| 1 | kaku cross-domain structural bridges (modular-flavor flagship, swampland gradient-bound, BCS dimensional-transmutation, zeta-Brody, GGE-Fock Page-curve) | kaku-speculative-theorist | compute×5 | 5 |
| 2 | string cross-framework walls / mechanism imports (Sen-tachyon K-theory descent, dS species-count entropy, modern swampland refresh) | string-theory-theorist | compute×2, review×1 | 3 |
| 3 | cross-framework adjudications (sum-over-geometries kaku↔string; QG-character lens kitaev↔LQG) | gen-physicist (neutral) | workshop×2 | 2 |

Total: **10 gates** (7 compute + 1 review + 2 workshop) across 3 waves. Honest count (`Investigating-Workshops.md`): **2 genuine Q1a workshops** — (W3-1) the sum-over-geometries / Page-curve adjudication (kaku explicitly disagrees with string's "no sum, different road" reading; cross-rebuttal essential; kitaev's λ_L=0 is the shared evidence both read oppositely) and (W3-2) the substrate-QG-character-lens adjudication (kitaev's integrability reading ↔ LQG's background-independent-QG reading). The rest are compute carry-forwards (kaku + string pre-registered next-steps) + 1 review. Compute-heavy outcome expected for domain-survey seeds. The two workshops are split into a single NEUTRAL-planned wave (W3) so no wave-owner plans a workshop they participate in — mirrors the inv-3/4/5/7/8/10 W4 neutral-planner precedent. **Neither kitaev nor LQG owns a compute wave** — kitaev's integrability suite is consumed by inv-10, LQG's by inv-7; both contribute as W3-2 workshop voices (the inv-5 spectral-geometer reduced-role precedent, applied twice). inv-9's fresh compute content is carried by kaku (W1) + string (W2), neither of which is used by any other investigation.
