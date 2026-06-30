# Seed file — sessions/archive/session-86/session-86-w2-workingpaper.md

**Date**: 2026-04-26
**Investigator**: phonon-first-cosmologist
**Source WP**: `sessions/archive/session-86/session-86-w2-workingpaper.md` (678 lines read in full)

## Substrate of the wave

W2 was a Mellin-Barnes infrastructure wave with four gates: C9 (FAIL by both ratio and chi^2 branches), C10 (INFO — `analytic_zeta(s, L_max)` API delivered, callable), C11 (PASS at iter-2 — Zubarev infinite-vector classification + `Lambda_Z^{2s}·Γ(s)` closed form), C12 (FAIL with diagnostic — `cluster_span(L_max)` module published despite verdict-line FAIL by precision-floor mismatch).

The structurally weightiest finding: C9 closes the entire `F_4 ∘ MB ∘ SD-subtraction` corridor for cosmological-constant suppression on the truncated D_K cache at L_max=10 — by *both* a ratio test (ratio_min = 9.456 across {ζ, Zubarev, SDW}, all 19 OOM above the 5e-1 PASS bound) and a chi^2/dof test (1.47e+04 vs PASS 5, FAIL 20). CC3 cross-check PASSes at machine ε across all three regulators (rel_err ~ 2-4 × 10^-16, four OOM tighter than the 1e-12 threshold), which proves the Mellin-Barnes integrator is functioning correctly — the FAIL is a *substrate* signature, not a numerical artifact. The Mellin lens worked; the substrate does not admit F_4 CC suppression.

This converts three prior S85 truncation-hypothesis FAILs (W0-7 ρ → -0.81 conjecture, W0-11 CC-3 Connes-Moscovici residue, W0-20 Mellin-cone s=3 R_inf at L_max=12) to **STRUCTURAL FAILs**, and cascade-FAILs five downstream gates (W3 T9 REPLACEMENT-B, W3 W0-7/W0-11/W0-20 re-emissions, W10 C37 ZFP discharge ζ-at-interior route).

## Candidates

### Candidate 1 — Surviving CC-suppression corridor map after F_4 closure

**What it would do**: With F_4 ∘ MB ∘ SD-subtraction now formally closed by both branches, an explicit map of the surviving CC-suppression corridors is needed before S87 compute commits. The W2 wave-synthesis names three families: (i) C-regulator class outside F_4 (cutoff_sqrt, anomaly per S86 plan-w14 §1 atlas decomposition `{ζ, Zubarev, SDW, cutoff_sqrt, anomaly}`); (ii) the Mellin-Strip / Convergence-Cone Theorem T5 boundary (different analytic-continuation mechanism, not relying on F_4 multiplier algebra); (iii) non-MB mechanisms — Friedmann two-layer gravity, dilution-CC, substrate-density-driven mechanisms outside the spectral-functional class. The workshop would (a) for each surviving corridor, state the formal mechanism explicitly (algebraic structure, regime of validity, what gate would test it), (b) produce a constraint-priority ranking with EVOI estimates, (c) identify which corridors are mutually exclusive and which can run in parallel.

**Why it's worthwhile**: C9's closure absorbs substantial S85 work (W0-7, W0-11, W0-20 conversions). Without an explicit corridor map, S87 risks either chasing a partially-closed corridor or duplicating effort across the three families. The WP §6 item lists these three corridors but does not rank or formalize them; the §VII-table promises future investigation but the priority order is not pinned. The constraint map gain from C9 is genuine; capitalizing it requires a deliberate planning step before the next compute wave. Cross-pillar bridges exist: dilution-CC connects to Pillar VIII (KK on Lie groups, S65 SCALE-TRANSFER-65); Friedmann two-layer gravity connects to Pillar I (acoustic gravity / BLV metric); substrate-density-driven mechanisms connect to Pillar II (Volovik program, q-theory); cutoff_sqrt + anomaly connect to Pillar III (NCG regulator algebra). Each corridor has a different cross-pillar anchor; the map should reflect that.

**Type**: 3-agent workshop

**Suggested agents**: connes-ncg-theorist, volovik-superfluid-universe-theorist, gen-physicist

**Rounds**: 3 (R1 each agent steelmans one of the three surviving families with formal mechanism + EVOI estimate; R2 each agent responds to the other two — including identifying mutual exclusivity and shared structural floor; R3 converge to a ranked corridor map with carry-forward gate specs)

**Context the workshop will need**: C9 verdict (`S86-MELLIN-HEAT-KERNEL-INFRA: FAIL value=9.455686e+00`); C9 wave-synthesis text especially the "investigate" list (WP lines 154-156); C9's CC2 NON-monotonicity (a_0 grew 239× L=5→L=10 in ζ-class); the F_4 / M / F_4-INF 3-class partition from C11 `sessions/framework/registry/lizzi-finite-infinite-vector-classification.md`; S65 SCALE-TRANSFER-65 verdict (dilution-CC anchor); S60 q-theory verdict (sole CC survivor at S60); cross-pillar connection to S46 a_2 split (geometric SD ≈ 0.728 vs ζ_D(1) ≈ 2776, factor 3812). Adjudication rule: each surviving corridor must be (a) named with formal mechanism, (b) given an EVOI estimate, (c) tested against the constraint that ALL F_4 regulators FAILed by both branches at L_max=10.

---

### Candidate 2 — Substrate signature decomposition: why a_0 grew 239× while a_4, a_6 converged

**What it would do**: The C9 CC2 cross-check is the most physically informative output of W2. Per-regulator at L_max ∈ {5, 6, 7, 8, 10}, the n=0 (a_0 / CC slot) Mellin moment grew 3.93e+05 → 9.38e+07 in ζ-class (factor 239×), while n=4 and n=6 slots converged monotonically (high-n moments are dominated by smallest eigenvalues, which freeze early). The 46,816 new eigenvalue rows added by sectors (p+q) ∈ {9, 10} contribute Mellin weight at the bottom slot that outweighs truncation residual. The workshop would (a) decompose the n=0 growth by Weyl-dim sector contribution: which (p, q) sectors carry the dominant a_0 weight, and how does the Weyl-dim growth d(p,q) = (1/2)(p+1)(q+1)(p+q+2) propagate into the Mellin slot; (b) extrapolate at what L_max the n=0 slot enters the asymptotic Weyl regime (or whether it never does on a finite truncation); (c) tie the a_0/a_4/a_6 split to the S46 SD a_2 vs ζ_D(1) factor-3812 result, which already showed geometric vs spectral moments differ structurally on this substrate.

**Why it's worthwhile**: The framework's CC content on the substrate is now demonstrably *not* an artifact of a particular regulator class — the substrate genuinely carries large a_0 weight. But that's a wall, not an explanation. Knowing WHICH eigenvalues drive the n=0 growth is decision-relevant: if it's the lowest eigenvalues (gap structure), the suppression mechanism must address the gap. If it's the bulk eigenvalues (continuum approach), a different regulator class might suppress. If it's the highest sectors, the truncation will eventually saturate and a_0 will converge — but at what L_max? The C9 verdict says "the substrate's a_0 spectral content is finite and the prior FAILs were truncation artifacts" was FALSIFIED at L_max=10, but it does NOT say a_0 is divergent — only that L_max=10 is below saturation. This is a quantitative question about Weyl asymptotics on the truncated D_K, structurally different from a CC-suppression mechanism search.

**Type**: solo (1 agent) initial decomposition + structural argument; results will inform Candidate 1's corridor map

**Suggested agents**: spectral-geometer (the C9 author has the cache loaded and the residue extractor)

**Rounds**: 1 (informational synthesis; not adversarial)

**Context the workshop will need**: C9 cache `computations/s86_w2_c9_residues.npz` (per-regulator, per-L_max Mellin moments at slots {0, 2, 4, 6}); the L_max sweep {5, 6, 7, 8, 10} numerical values from WP §W2-1; Weyl-dim formula d(p,q) = (1/2)(p+1)(q+1)(p+q+2); SU(3) representation theory for which (p,q) sectors are added at L_max=9, 10; S46 SD a_2 vs ζ_D(1) factor-3812 result; the WP claim "the substrate's a_0 spectral content is genuinely large in this regulator class" (line 156). The synthesis should produce: (a) sector-by-sector breakdown of n=0 contributions at L_max=10, (b) extrapolation slope for L_max → infinity (does a_0 saturate or diverge), (c) classification of the 4 SD slots {a_0, a_2, a_4, a_6} by their substrate signature (sensitive to gap, sensitive to bulk, sensitive to UV).

---

### Candidate 3 — Mellin-Strip / Convergence-Cone Theorem T5 readiness audit

**What it would do**: C11's `Lambda_Z^{2s}·Γ(s)` closed-form lands the analytic anchor for W1b T5 (Mellin-Strip / Convergence-Cone Theorem) — the WP §W2-3 solution-space interpretation explicitly says "the strip Re(s) > 0 of the Zubarev profile is exactly the convergence cone T5 identifies. Zubarev's INFINITE-VECTOR membership is the analytic precondition — the closed-form `Lambda_Z^{2s}·Γ(s)` is the algebraic substrate that lets T5 land at all." But T5 itself is named, not computed. The workshop would (a) state T5's exact claim (what does the convergence cone theorem assert about analytic continuation on D_K's spectral zeta?), (b) verify the C11 closed form satisfies T5's preconditions, (c) identify what additional infrastructure T5 needs beyond `analytic_zeta` (C10) and `Lambda_Z^{2s}·Γ(s)` (C11), (d) produce a gate spec for landing T5 in S87 W1b. Cross-check whether T5 is a viable CC-suppression corridor (per Candidate 1's surviving-corridor list, it's named but unverified).

**Why it's worthwhile**: C11 PASS lands a permanent registry entry in `sessions/framework/registry/lizzi-finite-infinite-vector-classification.md` with three downstream consequences claimed (F_4 sub-atlas heterogeneity is structural; T5 gains its analytic anchor; R-protected observables are stronger under Zubarev than under ζ). The first is registered; the second and third are claimed but not yet computed. T5 in particular is a candidate CC-suppression corridor surviving F_4 closure (the WP §W2-1 explicitly names it as a path forward). Its readiness state is currently "anchor delivered, theorem unstated" — that's a planning gap. Workshop output is a T5 gate spec for S87.

**Type**: 2-agent workshop

**Suggested agents**: lizzi-spectral-functional-theorist (the C11 author, owns the F_4-INF classification), connes-ncg-theorist (NCG side: what does Connes-Moscovici dimension-spectrum theory say about convergence cones)

**Rounds**: 2 (R1 each agent states T5 from their pillar; R2 converge to a single theorem statement + gate spec)

**Context the workshop will need**: C11 framework note `sessions/framework/registry/lizzi-finite-infinite-vector-classification.md`; the closed-form `M[exp(-x/Λ_Z²)](s) = Λ_Z^{2s}·Γ(s)` and the recurrence M[f_Z](s+1) / M[f_Z](s) = Λ_Z²·s; S86 W1b plan reference for T5 (the planner's expected statement); Connes-Moscovici 1995 dimension-spectrum theorem (Sd = {8, 6, 4, 2, 0}); C10 `analytic_zeta(s, L_max)` API and its truncation-stability INFO (61.1% L=8→L=10 shift at s=3) — does T5 absorb this signature or amplify it; cross-pillar Pillar III NCG anchor.

---

### Candidate 4 — Three structural-FAIL-conversion review (S85 W0-7 / W0-11 / W0-20)

**What it would do**: C9 converted three prior S85 FAILs from "TRUNCATION-HYPOTHESIS FAIL" to "STRUCTURAL FAIL" (W0-7 ρ → -0.81 conjecture value=-0.132 at L_max=8; W0-11 CC-3 Connes-Moscovici residue; W0-20 Mellin-cone s=3 R_inf value=1.81e6 at L_max=12). All three share the F_4 ∘ MB lens; their structural cause is now named ("F_4 cannot suppress") but not characterized in detail. The workshop would (a) for each of the three FAILs, identify whether its specific mechanism (which slot, which contour, which convention) is a separate substrate signature or a single phenomenon viewed three ways, (b) determine whether any of them survive in a non-F_4 regulator class (i.e., do they fail under cutoff_sqrt or anomaly too?), (c) produce an explicit registry entry recording the three FAILs as a single structural family with a shared physical interpretation. This is constraint-map hygiene with physics content.

**Why it's worthwhile**: Three structural FAILs of this magnitude need a shared registry record, not three orphan entries. The framework's permanent results registry is sharpened by recognizing these as one phenomenon. The pattern detector frame: when three results in different sub-domains share the same algebraic origin (F_4 ∘ MB lens), they should be filed as one structural finding, not three. This is the structural thinking imperative — find isomorphism, not coincidence. Cross-pillar connection: this also informs Candidate 1 (the corridor map) by clarifying whether searches outside F_4 are independent of the three structural FAILs or correlated.

**Type**: solo (1 agent)

**Suggested agents**: lizzi-spectral-functional-theorist (owns the C10/C11 spectral-functional context and the framework note registry)

**Rounds**: 1 (informational; produces a registry entry, not a verdict)

**Context the workshop will need**: S85 W0-7 verdict `S85-CC-3-CONNES-MOSCOVICI-RESIDUE: FAIL value=-0.132 L_max=8`; S85 W0-11 verdict; S85 W0-20 verdict `S85-W0-L-MELLIN-CONE-S3-RESIDUE: FAIL value=1.81e6 L_max=12`; C9 explicit conversion text (WP §W2-1 line 146-147); the three S85 plan blocks for original mechanism statements; F_4 / M / F_4-INF 3-class partition; existing `sessions/framework/permanent-results-registry.md` to identify where the new family entry lands.

---

### Candidate 5 — Cross-pillar cross-check on F_4 closure: Volovik / q-theory CC anchor

**What it would do**: The F_4 closure tightens the constraint surface. The remaining CC-suppression candidates per the WP include "non-MB mechanisms entirely — Friedmann two-layer gravity, dilution-CC, or substrate-density-driven mechanisms outside the spectral-functional class." S60 already established q-theory as the sole CC survivor at that round (per agent memory). The workshop would (a) ask whether q-theory's CC suppression mechanism is independent of F_4 (likely yes — q-theory is a substrate-density mechanism, not an analytic-continuation mechanism), (b) verify the substrate-density framing is structurally compatible with the C9 finding (a_0 unsuppressed under F_4 does NOT contradict q-theory; q-theory operates on a different observable axis), (c) update the EVOI prioritization given C9's elimination of the F_4 corridor. This is cross-pillar: Pillar II (Volovik) ↔ Pillar III (NCG / spectral functional).

**Why it's worthwhile**: The C9 closure is one of the largest single corridor closures of S86; its impact on the EVOI table needs reflection. If q-theory was already the sole survivor at S60 (CC #7 closure), then F_4 closure is the eighth — but the framework needs to know whether that eighth closure tightens or relaxes the q-theory pressure. Specifically: does F_4 closure increase the EVOI of substrate-density mechanisms, or does it simply remove a competitor? Cross-pillar pattern detection: the same structure (CC suppression failure under spectral-action class regulators) appears in three pillars (NCG, q-theory, Friedmann) — workshop maps the isomorphism if it exists.

**Type**: 2-agent workshop

**Suggested agents**: volovik-superfluid-universe-theorist (q-theory CC mechanism), lizzi-spectral-functional-theorist (spectral-functional CC observation post-C9)

**Rounds**: 2 (R1 each agent states whether C9 changes their CC corridor; R2 converge to an updated EVOI ranking + a candidate gate for S87)

**Context the workshop will need**: C9 verdict; S60 q-theory CC closure (the eighth CC closure if F_4 is added); MEMORY.md entry "DILUTION-CC priority" (project memory); EVOI table at `sessions/evoi-framework.md`; the WP §W2-1 §6 surviving-corridor list; Pillar II Volovik program references especially q-theory papers; cross-pillar Volovik ↔ NCG isomorphism check (does q-theory's free-parameter axis project into a spectral moment?).
