# Session-111 — Wave Partition

**Session:** 111.  **Mode:** fanout, COMPUTE (+ Stage-1/Stage-2 registration gates).  **Scope source:** `session-111-context.md` (deduped from S110 per-wave WP `## Carry-Forward Computations` + 8 W1 workshop Wrap-Ups + housekeeping mirror).
**Theme:** harvest the S110 M_KK-keystone session. Spine: the a(t)/Friedmann FORM is now MONOTONE-robust (WS-ATFORM) ⇒ the §6.3 residual = {M_KK magnitude (W2 MKK-RG decider) + the clock-triple well-posedness (W1)}. 22 carry-forwards, EVOI-ordered, 5 compute waves.

## Wave structure (dependency + run order)

```
W1 (a(t)/clock theorems; Tier-1 #1 spine)   ──┐  [planner: hawking-theorist]            ┐ Tier-1 spine
W2 (M_KK keystone + H-sector + CC)          ──┤  [planner: volovik-superfluid-univ]     ┘ (highest EVOI; run first, parallelizable)
W3 (fermion-mass / Yukawa / NCG-categorical)──┤  [planner: connes-ncg-theorist]
W4 (compact-object / black-hole)            ──┤  [planner: schwarzschild-penrose-geometer]
W5 (Floquet confirmatory + Stage-2 verify)  ──┘  [planner: transit-dynamics-theorist]
```
Run order at `/rclab-coordinate`: W1 + W2 (Tier-1 spine, parallelizable) → W3 → W4 → W5. Intra-wave: CLOCKLOC2 → CLOCKLOC1 (corridor scoping). All compute-wave PLANS produced now (Phase 2). S111 ALSO carries a separate workshop schedule (`session-110-s111-workshop-schedule.md`), run via `/rclab-coordinate` workshop-mode — NOT part of this compute plan.

---

## W1 — a(t) / clock theorems  (Tier-1 #1 spine; planner: hawking-theorist)

Per-gate executor in the gate block's `agent_type`. The a(t)/effective-Friedmann FORM is MONOTONE-robust (S110 WS-ATFORM); this wave closes the clock-triple well-posedness leg of the §6.3 residual.

| Gate (S111 ID) | What (1-line) | Executor | EVOI |
|:--|:--|:--|:--|
| S111-CF-CLOCKLOC1-CED | (C,E,D)-triple self-consistency in the substrate-natural frame; `|residual|<1e-6` on `Λ−3H²=0` [PRIME a(t) backbone] | hawking + schwarzschild-penrose (cross-check) | Tier-1 #1 HIGH |
| S111-CF-CLOCKLOC2-MONOTONE | deparametrization monotonicity corridor (τ-window τ̇≠0; first turning point above [0,0.19]) [feeds CLOCKLOC1] | schwarzschild-penrose | Tier-1 #1 (feeder) |
| S111-CF-CLOCKLOC3-R16EPS | r=16ε layer-obstruction theorem — STAGE-1-CANDIDATE registration (Level-1 vs Level-2 typing + distinctness-from-5-args declaration) | schwarzschild-penrose + hawking | structural |
| S111-CF-CLOCKLOC4-UNIQUE | substrate-natural-clock uniqueness (reparam class preserving Λ=3H²) [lower priority] | schwarzschild-penrose | structural (low) |
| S111-CF-NOHOLOFLUX | spectral-triple-no-holonomy-flux root — STAGE-1-CANDIDATE registration (3-projection chain; cites S85 τ_fold cusp) | gen-physicist or connes-ncg | structural |
| S111-CF-TAUCUSP | τ-cusp observable asymmetry (separable n_s/α_s tilt signature vs smooth ramp; CMB-S4/HD axis) | transit-dynamics or lizzi | observational |

Natural split: {CLOCKLOC1, CLOCKLOC2, CLOCKLOC3, CLOCKLOC4} (the WS-CLOCKLOC clock cluster) | {NOHOLOFLUX, TAUCUSP} (the WS-ATFORM pair).

---

## W2 — M_KK keystone + H-sector + CC  (Tier-1 #2 / Tier-2 M_KK-DERIVATION; planner: volovik-superfluid-universe-theorist)

| Gate (S111 ID) | What (1-line) | Executor | EVOI |
|:--|:--|:--|:--|
| S111-CF-MKK-RG-INVARIANCE | M_KK τ-RG-invariant-transmutation-scale vs bare-import discriminator; τ-spread of `Λ_eff(τ)·exp(−1/(λ_eff N₀))` < 5e-2 [PRIME Topic-1 decider; gated on CV2A, landed] | nazarewicz (BCS machinery; volovik/einstein framing) | Tier-2 M_KK HIGH |
| S111-CF3-H0-RESIDUAL | residual H₀-relief at the dimensionless-Ô layer; pre-register `49/800=6.125%` honest partial; dimensionless-morphism channels only (d_A=0) [∥ MKK-RG] | mack + volovik (a₀-orthogonality) | Tier-2 H₀ HIGH |
| S111-CF-AS3 | A_s magnitude pin + all-frozen-superhorizon regime + nazarewicz FB-temp per-sector decisive sub-compute (POINT-vs-BAND); canonical write-order | transit-dynamics + nazarewicz (FB-temp) | Tier-1 #1 consumer |
| S111-CF-VIICE-NW | derive the n-occupation↔w-EoS dictionary (relic occupation → barotropic w); sharpen §VII.CE clause-(a) author-side identification | volovik + einstein (cross-check) | structural |

Natural split: {MKK-RG-INVARIANCE, CF3-H0-RESIDUAL} (the M_KK/H-sector scale axis) | {AS3, VIICE-NW} (the amplitude/EoS axis). AS3 planner MAY further split AS3a (transit, magnitude) / AS3b (nazarewicz, FB-temp per-sector).

---

## W3 — fermion-mass / Yukawa / NCG-categorical  (Tier-2 #9b; planner: connes-ncg-theorist)

| Gate (S111 ID) | What (1-line) | Executor | EVOI |
|:--|:--|:--|:--|
| S111-CF-YUK-FULLFLAVOR | full-flavor Yukawa: down-sector ε_LX texture + CKM angles + same-gen J-conjugacy lock; mass_grp ≥ 5/6 | connes-ncg (+ baptista/vdd support) | Tier-2 #9b HIGH |
| S111-CF-WEINBERG-C2COSET | off-Jensen Weinberg-angle / a₂-response SLOPE `d(sin²θ_W)/dδ_C²|_0`; FI-tagged; the productive C²-coset relocation [prime candidate] | baptista or connes-ncg | MED |
| S111-CF-YUK-C2COSET-CONFIRM | C²-coset Yukawa-rank confirmation witness; dual-prior 0.90 FAIL / 0.10 PASS-as-§VII.BL-CONTRADICTION; folds into this wave | baptista or van-den-dungen | MED-LOW |
| S111-CF-M1-INTERTWINER | categorical construct-or-obstruct for the M1 intertwiner (NON-ACM σ_v two-conjunct, OR the obstruction theorem) [HIGH; multi-wave] | van-den-dungen (Axis-2/conj i) + connes-ncg (Axis-1/conj ii) JOINT | structural HIGH |

Natural split: {YUK-FULLFLAVOR, WEINBERG-C2COSET, YUK-C2COSET-CONFIRM} (the Yukawa/Weinberg compute cluster) | {M1-INTERTWINER} (the HIGH-effort categorical KK-theory gate, vdd+connes joint — may be its own sub-wave).

---

## W4 — compact-object / black-hole  (Tier-2/3; planner: schwarzschild-penrose-geometer)

| Gate (S111 ID) | What (1-line) | Executor | EVOI |
|:--|:--|:--|:--|
| S111-CF-B5A-ISLAND | QES/island boundary-entropy on the white-hole exit slice; `|S_island/(A/4)−1| ≤ 0.10` (deeper construction the edge-mode count FAILed) | hawking | MED-HIGH |
| S111-CF-CO34A-12D-BUBBLE | full-12D Gregory-Laflamme bubble maturation; `N_efold = ∫ growth_rate dτ ≥ 1` (lift the reduced 4+8 sub-critical N=0.232) | schwarzschild-penrose | MED |
| S111-CF-CO34B-LRDT | LRD photosphere-T transport degree; pin deg=+1 a priori + κ-sign-consistency predicate (expected FALSE); HELD/INFO dimensionful-slot-collision∧sign-lock | mack + little-red-dots (band) | MED |

Natural split: {B5A-ISLAND} (the white-hole/island gate) | {CO34A-12D-BUBBLE, CO34B-LRDT} (the compact-object maturation/transport pair). All three are heavy-but-MED; no split forced unless a planner stalls.

---

## W5 — Floquet confirmatory + Stage-2 verify  (planner: transit-dynamics-theorist)

| Gate (S111 ID) | What (1-line) | Executor | EVOI / class |
|:--|:--|:--|:--|
| S111-CF-FLOQUET1 | per-mode monodromy print at A=0.965 (`\|Tr M − 1.98756\| < 1e-3` ∧ `\|Tr M\| < 2`) [trivial, confirmatory] | transit-dynamics or berry | confirmatory |
| S111-CF-FLOQUET2 | exact DTC counterfactual-depth threshold `h_par_crit=0.0725` + miss-factor 84.34× + δτ_amp map (Sage-exact) [trivial] | transit-dynamics or berry | INFO registration |
| S111-CF-FLOQUET3 | first-principles δτ_amp derivation from the diabatic-freeze afterglow; `\|h_par_derived − 8.3e-4\|/8.3e-4 < 0.1` [moderate] | transit-dynamics | structural (upgrade) |
| S111-CF-FLOQUET4 | cutoff-robustness scaling theorem registration (Δa_½^{(n)} ∝ q_M^n exponent; prefactor diagnostic-only) [Stage-1] | transit-dynamics or berry | structural |
| S111-CF-KSIGN-PARITY-STAGE2 | Stage-2 NON-AUTHOR cross-check of §VII.CF κ-sign-lock∧Wodzicki-parity (2 parallel reviewers, axis-distinct, NOT connes/mack) | axis-A lizzi / axis-B volovik (parallel) | §VII Stage-2 |

Natural split: {FLOQUET1, FLOQUET2, FLOQUET3, FLOQUET4} (the WS-FLOQUET confirmatory cluster) | {KSIGN-PARITY-STAGE2} (the §VII.CF Stage-2 dual-dispatch). KSIGN reviewers MUST be NON-AUTHORS of the connes-mack workshop (axis-A lizzi or vdd; axis-B volovik or transit) per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"`.

---

## Gate-ID convention + collision

All S111 gate IDs prefixed `S111-CF-`; verdict file `computations/session-111/s111_gate_verdicts.txt` (canonical per `gate-verdicts.md`; the `_shared/`, `sessions/session-111/`, `sessions/session-plan/` variants are FORBIDDEN). No collision with S110 (`s110_*`). Stage-1 registration gates (CLOCKLOC3, NOHOLOFLUX, FLOQUET4) emit a verdict line (registry-landing PASS = artifact-existence-with-clauses); their Stage-2 verifies are SEPARATE future gates (S112+). KSIGN-PARITY-STAGE2 is itself a Stage-2 verify of the S110-landed §VII.CF.

## Run-order + dependency flags (apply at gate-block authoring)

(i) **Tier-1 spine first** — W1 + W2 are highest-EVOI (the a(t)/Friedmann residual = M_KK magnitude (W2) + clock-triple (W1)); parallelizable.
(ii) **Intra-wave** — CLOCKLOC2 (monotone corridor) feeds CLOCKLOC1's corridor scoping: sequence CLOCKLOC2 → CLOCKLOC1 in W1.
(iii) **Upstream-landed (ready)** — MKK-RG-INVARIANCE gated on CV2A (`s110_cf_cv2a_*.npz`, on disk); KSIGN-PARITY-STAGE2 gated on the §VII.CF Stage-1 entry (landed S110). CF3-H0-RESIDUAL ∥ MKK-RG (independent axes, volovik a₀-audit) — no sequencing.
(iv) **Stage-2 reviewer exclusion** — KSIGN-PARITY-STAGE2 reviewers MUST NOT be connes or mack (the §VII.CF authors); axis-distinct (NCG/spectral ⊥ transport/cosmological-bridge); operate WITHOUT the connes-mack workshop file.
(v) **Sharpenings folded** — CO34B-LRDT (pin deg=+1, κ-sign predicate) + CF3-H0-RESIDUAL (49/800 honest partial, dimensionless-slot) carry the connes-mack workshop sharpenings; CLOCKLOC1 PRDR carries the V_spec-monotone + Level-2-clock tags (ws-clockloc housekeeping §D).
