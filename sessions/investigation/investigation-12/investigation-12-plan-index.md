# Investigation 12 — Plan Index (fanout)

**Date**: 2026-06-14
**Seed (`--from`)**: three investigation-1 agent surveys — `lizzi-spectral-functional-theorist.md` + `van-den-dungen-bridge-theorist.md` + `transit-dynamics-theorist.md` (digest: `investigation-12-seed.md`). All three FRESH (none consumed by a prior investigation).
**Mode**: INVESTIGATION (track-local). compute/solo verdicts → `computations/investigation-12/inv12_gate_verdicts.txt` via `emit_verdict(session=12, track="investigation")`; the W4 workshop/review gates close by artifact-existence (NO verdict line).
**Plan-freeze validation**: R3 YAML PRDR validator **PASS 15/15** (all compute/solo gates, w1/w2/w3 — every gate carries all 8 PRDR keys + `schema_version="R3"` + `output_artifacts`); upstream-pin validator **PASS** (verdict=PASS, n_mismatches=0, n_missing_npz=0 — every gate NO-UPSTREAM-NPZ; the foundational W3-1 npz is pinned `<computed-at-runtime>` and the static caches are runtime-verified, so there is nothing to cross-check at plan-freeze). The W4 gates (2 workshop + 1 review) are artifact-existence-ready (workshop blocks complete — EXACTLY 2 agents each, rounds, sources, output_path, adjudication_question + must_contain; review block complete — 1 neutral agent, sources, output_path, must_contain; 0 `verdict_line:` YAML keys). `[SIGN]` gates (W2-1, W2-4, W2-5, W3-3) carry the schema-v2 3-tuple pre-registration.

## Waves

| Wave | Theme | Owner-planner | Types | Gates | Plan file |
|:----:|:------|:--------------|:------|:-----:|:----------|
| 1 | Spectral-functional: selection, A_s reference-state, n_s coherence | lizzi-spectral-functional-theorist | compute×4 + solo×1 | 5 | `investigation-12-plan-w1.md` |
| 2 | NCG bridge: factorization bounds, pole-audit, Krein, FWD-C1 | van-den-dungen-bridge-theorist | compute×3 + solo×2 | 5 | `investigation-12-plan-w2.md` |
| 3 | Transit dynamics: lock the relic, Floquet, back-reaction, greybody, H̃ | transit-dynamics-theorist | compute×5 | 5 | `investigation-12-plan-w3.md` |
| 4 | Cross-agent adjudication & A_s synthesis | gen-physicist (neutral) | workshop×2 + review×1 | 3 | `investigation-12-plan-w4.md` |

**Total: 18 gates** (12 compute + 3 solo + 2 workshop + 1 review).

## Gate roster (what `/rclab-coordinate` dispatches)

| Gate ID | gate_type | Executor | One-line |
|:--------|:----------|:---------|:---------|
| INV12-W1-1-MODULAR-FUNCTIONAL-EXTREMIZATION | compute | lizzi-spectral-functional-theorist | does the §VII.BZ (K12) faithful normal modular weight ω extremize `S_modular = Tr(D_K² ρ_ω)` at τ_fold=0.190? → the missing substrate-derived SELECTION principle |
| INV12-W1-2-A-S-GGE-MODULAR-REFERENCE | compute | lizzi-spectral-functional-theorist | re-derive A_s vs the GGE modular reference state (not Bunch-Davies); does the BD-referenced 3.02× wall lift? **[5th A_s route]** |
| INV12-W1-3-N-S-FUNCTIONAL-COHERENCE | compute | lizzi-spectral-functional-theorist | n_s(f*) ≈ n_s(√x) to σ-budget OR an {√x, f*} band — COHERENCE check, NOT re-selection (re-shop FORBIDDEN) |
| INV12-W1-4-R1-SAME-REGULATOR-AUDIT | solo | lizzi-spectral-functional-theorist | R_1 = a_0·a_4/a_2² = 1.128653: all-ζ_D-residues vs mixed-normalization (ζ_D(1)=2776.17 / Gilkey 0.728, ratio 3812) |
| INV12-W1-5-KRAJEWSKI-TILT-CENSUS | compute | lizzi-spectral-functional-theorist | is ℂ⊕ℍ⊕M_3(ℂ) the UNIQUE SM-compatible finite geometry admitting red-tilt under an anomaly-forced functional? |
| INV12-W2-1-S-CROSS-OFF-JENSEN-BOUND | compute | van-den-dungen-bridge-theorist | `|S_cross|/S_base < 10⁻²` at one off-Jensen point (O'Neill A,T → Gilkey a₂ remainder); discharges the on-Jensen-only conditional on G_N/n_s |
| INV12-W2-2-A-N-POLE-CONVERGENCE-AUDIT | solo | van-den-dungen-bridge-theorist | (pole_in_s, n=d−2s, convergent? s>d/2) ledger for every canonical a_n; §VII.CB S109 a₂-canary separates cache-deliverable from residue-subtracted-only |
| INV12-W2-3-PAPER10-BCS-DRESSING-INVARIANCE | solo | van-den-dungen-bridge-theorist | promote S69 W5-G: BdG dressing (\|Δ_BCS\|=0.464 bounded) ⇒ K-homology EXACT (mass-order/c_s²=0/w_a=0 safe off-Jensen) while a_n shifts bounded |
| INV12-W2-4-KREIN-LORENTZIAN-A0 | compute | van-den-dungen-bridge-theorist | pseudo-Riemannian submersion triple (Paper 04, Krein J²=+1); does Krein-a₀ = Euclidean-a₀ (the a₀ DILUTION-CC's Λ uses)? |
| INV12-W2-5-FWD-C1-BISMUT-CHEEGER-ETA | compute | van-den-dungen-bridge-theorist | FWD-C1 η-form of {D_K(τ)} ↔ integrated Bogoliubov pair-production; NEW bridge-map class (adiabatic-limit, NOT HKR). **[6th A_s route + FIRST FWD-C1 landing]** |
| INV12-W3-1-RELIC-SPECTRUM-ODE-LOCK | compute | transit-dynamics-theorist | lock the relic {β_k} to ONE ODE (Radau/DOP853, rtol≤1e-10, GPU per-block); N_seg-independent. **FOUNDATIONAL — feeds W3-2/3/4 + W1-2 + W2-5** |
| INV12-W3-2-FLOQUET-ORDERED-VEIL-RESONANCE | compute | transit-dynamics-theorist | Floquet Re μ(k) for the post-fold modulus Hill equation across the pair band: resonance bands vs stability gaps — does the Ordered Veil survive its own in-band resonance? |
| INV12-W3-3-BACK-REACTION-CLOSURE-HSQ | compute | transit-dynamics-theorist | back-reaction closure H²_eff(τ)=(8πG_eff/3)ρ_relic(τ)+Λ vs the SCALE-FACTOR-54 band, ρ_relic=Σ_k E_k|β_k|² (NOT the 8-mode BCS source). **[SIGN]** |
| INV12-W3-4-GREYBODY-FROM-BDG | compute | transit-dynamics-theorist | derive the exit greybody Γ(ω) from the linearized BdG fluctuation potential (analog-gravity); collapse the A_s band; cross-check vs fitted 0.512 |
| INV12-W3-5-CF21-HTILDE-RECONCILE | compute | transit-dynamics-theorist | reconcile CF21 H̃ to one canonical horizon-exit reading (TD 5.9076e-3 vs baseline centre 4.714e-3, factor 1.57); via CC3 (+2) this IS the A_s overproduction |
| INV12-W4-1 | workshop (lizzi-spectral-functional-theorist ↔ transit-dynamics-theorist, 2 rounds) | gen-physicist (neutral planner) | A_s wall reading: REAL structural overproduction (transit) vs wrong-reference-state ARTIFACT (lizzi) — STRUCTURAL VERDICT + decisive forward gate |
| INV12-W4-2 | workshop (lizzi-spectral-functional-theorist ↔ van-den-dungen-bridge-theorist, 2 rounds) | gen-physicist (neutral planner) | SA-failure diagnosis: WRONG FUNCTIONAL (lizzi: modular/entropy) vs WRONG SIGNATURE (vdd: Krein/Lorentzian) — compose or compete? STRUCTURAL VERDICT + forward gate |
| INV12-W4-3 | review (gen-physicist, 1 neutral agent) | gen-physicist | A_s three-route synthesis: integrate lizzi-modular-reference (W1-2) + vdd-η-form (W2-5) + transit-lock/greybody/back-reaction/CF21 (W3-1/3/4/5) → wall dissolved, relocated, or confirmed? |

## Dispatch

- **Per-wave**: `/rclab-coordinate sessions/investigation/investigation-12/investigation-12-plan-w{i}.md`
- **Full investigation**: `/rclab-coordinate sessions/investigation/investigation-12/investigation-12-plan-index.md`

`/rclab-coordinate` juggles the gate types directly: the 15 compute/solo gates dispatch as background subagents (each emits a dual-SHA verdict line to the investigation track — compute via subagent, solo inline by the orchestrator); the W4-1/W4-2 workshops run as 2-agent, 2-round sequential exchanges closing by artifact-existence; the W4-3 review runs as a single neutral-reviewer synthesis closing by artifact-existence.

### FOUNDATIONAL dispatch-order directive (load-bearing — cross-wave data dependency)

**INV12-W3-1 (RELIC-SPECTRUM-ODE-LOCK) MUST be dispatched FIRST**, ahead of its cross-wave consumers. Its npz output (the locked {β_k} relic spectrum) is consumed by:
- intra-wave: INV12-W3-2, INV12-W3-3, INV12-W3-4
- **cross-wave**: INV12-W1-2 (lizzi A_s GGE-modular reference) + INV12-W2-5 (vdd η-form pair-production identification)

The consuming gates pin the W3-1 npz as `<computed-at-runtime>` and carry a mechanical-closure fallback (honest PRE-REG-INC close if W3-1 has not landed; re-run after). To AVOID the inefficient PRE-REG-INC-then-rerun cycle on the two cross-wave consumers, `/rclab-coordinate` SHOULD run INV12-W3-1 before INV12-W1-2 and INV12-W2-5 — either by dispatching W3 (or just W3-1) ahead of W1/W2, or by treating W3-1 as a wave-0 foundational gate. There is no hard validator dependency (the forward pins are runtime sentinels, not concrete missing paths — upstream-pin validator PASS); the ordering is a wall-clock-efficiency directive, not a correctness gate.

## Cross-investigation dedup (load-bearing — do not collide)

- **The A_s cluster** (5 prior routes + 2 new): inv-3 W2-3 (near-floor-DOS / ζ'(0)), inv-4 W1-4 (exit-horizon greybody, **hawking**), inv-5 W2-1 (impulse-quench), inv-6 W2-2 (Parker-Bogoliubov + K_pivot). inv-12 adds **INV12-W1-2** (5th — GGE-modular reference state, NEVER used before) + **INV12-W2-5** (6th — Bismut-Cheeger η-form, a NEW bridge-map class). **CRITICAL: INV12-W3-4 (greybody-from-BdG) is the SAME object as inv-4 W1-4 (hawking exit-horizon greybody) via DIFFERENT machinery** (analog-gravity BdG-fluctuation-potential vs black-hole-thermodynamics) — cross-reference, do NOT merge.
- **INV12-W2-5 (FWD-C1)**: the FIRST FWD-C1 landing (Q30 / cross-pillar-bridge-anatomy.md "Three forward bridge candidates" — FWD-C1 was never dispatched; FWD-C3 landed §VII.W-3.LAB S100a, FWD-C2 landed §VII.AV). NEW bridge-map class (adiabatic-limit η-form, NOT HKR) advances the Hybrid-Independence-Test K-counter per criterion (iii).
- **INV12-W4-2 (SA-replacement adjudication) vs inv-5 W3-2**: inv-5 W3-2 = "is Tr f(D²) the substrate's free energy?" (connes ↔ landau, the 93× tension). INV12-W4-2 = "WHAT is the correct REPLACEMENT — a modular functional (lizzi) or a Krein-signature reformulation (vdd)?" Different agents, different machinery, different question. Cross-cite at both closes; do NOT merge.
- **INV12-W1-1 (modular extremization) vs inv-5 W1-4/W1-5**: same modular machinery (Tomita-Takesaki / entropy-functional), different observable (functional-SELECTION at τ_fold vs ε_LX fermion mass / entropy-functional CC). Cross-reference.
- **INV12-W3-3 (back-reaction) vs inv-7 / inv-8**: the a(t) gap is also touched by inv-7 (LQG bounce / effective-Friedmann) + inv-8 (Jacobson entanglement-equilibrium / quantum-metric stiffness H(τ)). INV12-W3-3 is DISTINCT machinery (GGE-relic-energy back-reaction source ρ_relic=Σ E_k|β_k|²). Cross-reference.
- **INV12-W2-1 (S_cross off-Jensen) vs inv-2**: same off-the-U(2)-invariant-slice region, different observable (spectral-action cross-term vs Yukawa rank). Cross-reference.

## Non-gate items (recorded, NOT dispatched)

6 session-track curated-register hygiene items (HY1–HY6, `investigation-12-seed.md §"Non-gate items"`) are quarantined from this plan — an investigation cannot mutate curated session-track registers (track-local boundary). They route to session-promotion at `/rclab-investigate --investigation 12` close: HY1 (FI/RD manifest authoring, gated on the W1-4 verdict), HY2 (a_2^ζ≡a_2^SDW canonical_constants label disambiguation, gated on W1-4), HY3 (m_H FI/RD reconciliation note, capstone designated-writer), HY4 (S103 n_s √x commit A_6-scope caveat, gated on W1-3), HY5 (n_T=+0.4676 blue-floor falsifier-row promotion, **mack sole-writer**), HY6 (Baptista↔Connes↔project convention-table AMRI migration + the W2-2 pole-tag registry-lift). Plus 7 surveyed-but-not-elevated bridges (lizzi B-L2 dilaton-Higgs; vdd B-4 Fredholm-complex; transit B1 cosmological-collider / B2 Fano-statistics / B4 observer-dependent-S_ent / B6 prethermalization-BBN / B7 finite-rate-KZ).
