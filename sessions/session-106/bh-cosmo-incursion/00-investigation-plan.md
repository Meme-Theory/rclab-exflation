> **⚠ §8 (T1–T10) + the verdict vocabulary are SUPERSEDED STEERING.** Those were orchestrator-supplied (pre-drawn questions + a pre-paired GR-claim↔substrate-anchor map + a grading rubric) and biased the v1 run into a confirmation exercise. The corrected investigation (`*-v2.md`) has the agents derive their own throughlines/classifications under a hard falsification mandate; substrate-first stance retained (user direction, 2026-06-13). §0–§7 (objective, corpus map, prior anchors, framing law) remain valid; §8 is retained for provenance only.

# Black-Hole Cosmology & Universal Gravastar ↔ Exflation — Multi-Agent Investigation Plan

**Status**: PLAN (pre-launch). **Date**: 2026-06-13. **Corpus**: `downloads/bh-cosmo/` (55 PDFs, 3 pillars + 3 curator INDEX files).
**Leads**: `hawking-theorist` (Lead A), `mack-cosmic-bridge` (Lead B). **Recursive sub-agents**: per `.claude/templates/agent-roster.md`.

---

## 0. Objective

A **framework-level deep dive** into Black-Hole Cosmology and the "universal gravastar / gravitational vacuum condensate star" (GVCS) family, answering one question:

> How does this body of GR-side physics — universe-inside-a-black-hole, torsion bounce, condensate-vacuum compact objects, cosmologically-coupled black holes, horizon-vs-surface observational tests — **conceptually interlock with the Exflation engine**, and what genuinely new throughlines, correlations, and structural similarities does that interlock expose?

The deliverable is **conceptual integration + a structured throughline/discriminator map**, NOT new gate computations. Where a genuine new computational gate surfaces, it lands as a 4-field carry-forward (what / inputs / gate / effort), never as an in-campaign recompute of a closed result.

---

## 1. Corpus map (55 PDFs)

| Pillar | Dir | n | Spine |
|:--|:--|:--|:--|
| **A. Black-Hole Cosmology** | `black-hole-cosmology/` | 19 | Poplawski ECSK torsion-bounce series (#03–07,09–11,17–18); Easson–Brandenberger limiting-curvature (#01); Smolin CNS (#02); Gaztañaga "CC-as-event-horizon / Big-Bang-inside-a-BH / bounce relics" (#12–14,19); cosmological-coupling claim/rebuttal Croker→Farrah→Rodriguez (#08,15,16) |
| **B. Gravastar / Condensate Stars** | `gravastar-condensate-stars/` | 21 | Mazur–Mottola founding (#01,04); stability core Visser–Wiltshire / Cattoen–Faber–Visser / Martin-Moruno (#02,06,08,11); dark-energy-star branch Mazur/Chapline/Lobo/Beltracchi (#03,05,07,14); Mottola trace-anomaly effective-theory line (#09,10,12,16,19,20); rotation/formation (#13,15,17,21); regular-BH↔gravastar bridge (#18) |
| **C. ECO Phenomenology** | `eco-phenomenology/` | 15 | gravastar-vs-BH discriminators (#01–04); echo theory (#05,08,09,13); echo observational claim/rebuttal chain Abedi-Afshordi↔Ashton (#06,07,10,12); status + modern probes Cardoso-Pani LRR / SgrA* flares / spectral instability (#11,14,15) |

Each dir's `00-INDEX.md` already carries verified arXiv IDs + a substrate-first framework cross-link block. **Leads read INDEX first**, then the papers (via `read_arxiv_paper(paper_id=...)` using the INDEX IDs — fast — or the `pdf` skill for on-disk files).

---

## 2. Prior framework work — **READ FIRST** (anti-rediscovery)

This territory is **half-explored**. The leads MUST anchor on these before forming any "new" throughline. Re-deriving any of them is a rediscovery failure per CLAUDE.md query-first discipline.

| Anchor | Where | What it already settles |
|:--|:--|:--|
| **S42 BH-Cosmology Incursion** | `sessions/framework/Collabs/blackhole-cosmology-incursion.md` | Universe-embedded-in-parent-BH ⇒ `P_ext = P_parent(q_parent)`; recursive CC-stabilization hypothesis; child de Sitter Gibbons-Hawking `T_GH = H_child/2π`. **Direct prior on Pillar A.** |
| **Acoustic white hole — PROVEN** | `s85_w6_acoustic_white_hole_formal.py` (theorem, S85); S95 `w4_1_white_hole_kinematic_consistency` | Pre/post-fold causal disconnection FORMALIZED. Transit `dτ/dt = 6.67 M_KK` vs `c_s = 0.485 M_KK` → Mach 13.75. **This is the framework's "universe-behind-a-horizon."** |
| **Hawking-collab lineage** | `sessions/archive/session-73b/...-phonon-first-hawking-workshop.md`; `sessions/framework/Collabs/framework-mechanism-discussion-hawking-collab.md`, `atlas-hawking-collab.md`, `phonic-exflation-equation-hawking-collab.md` | The "Hawking-1975 bifurcation": raw horizon physics vs observable asymptotic spectrum. Greybody `Γ_l(ω)~(ωr_s)^{2l+2}`. |
| **`c-compare` skill** | `.claude/skills/c-compare/skill.md` | Deterministic 6-step classifier: PROPAGATION (c-bounded, on g_M) vs SUBSTRATE DYNAMICS (not c-bounded) vs MIXED vs CONTRADICTION. **The tool for "is a horizon real or acoustic?"** |
| **Vacuum w₀** | `w0_FW = −0.918` (S58 Volovik partition + effacement `Γ_eff=0.99970`); DILUTION-CC closed S66 | The substrate vacuum's equation of state. Gravastar interior is `p=−ρ` (w=−1). |
| **R_842 rectangle** | late-time Penrose-branch: ζ→`w₀≈−0.494` de-Sitter-like, Zubarev→`w₀≈−0.997` | Which late-time de Sitter branch the regulator selects. **Direct seam to gravastar dS interior.** |
| **CC = a₀ zeroth SDW moment** | `a₀^ζ = 6440`; `Λ_cc = (2 f_0/f_2)·a_0` | The framework's cosmological constant IS a spectral moment — the bridge target for Mottola's trace-anomaly→DE. |
| **GW falsifier RETIRED** | walls=0 EXACT (S96); falsifier migrated GW→LSS (inventory Rows #71/#72) | **ECO/echo papers inform GR-side discrimination, NOT a live framework gate.** Mack must not resurrect a dead falsifier. |
| **Gravastar = genuinely new** | only 4 framework files mention it, all Volovik dS-thermodynamics refs | The Mazur-Mottola GVCS program has **never** been engaged framework-side. Pillar B is the highest-novelty surface. |

**Framing law (non-negotiable, per `phononic-framing.md`)**: every GR model here is a **GEOMETRIC-class laboratory-IN analog**. The substrate is logically prior. Explanation flows `D_K eigenvalues → spectral moments → emergent physics → measured GR observable`. A throughline reads "GR model X is the laboratory-IN shadow of substrate-IS mechanism Y" — **never** "the framework is a kind of black-hole cosmology." Inverting the arrow is a container-thinking violation.

---

## 3. Architecture — two recursive leads + joint synthesis

```
Phase 0  Orchestrator pre-flight (THIS DOC) — context pack + prior anchors
            │
Phase 1  ┌──────────────────────────────┐   ┌──────────────────────────────┐
(parallel)│ LEAD A — hawking-theorist    │   │ LEAD B — mack-cosmic-bridge   │
          │ Pillar A + horizon-physics    │   │ Pillar B + DE + ECO-obs       │
          │ recursively spawns ≤4 subs    │   │ recursively spawns ≤4 subs    │
          │ → WP-A working paper          │   │ → WP-B working paper          │
          └──────────────┬───────────────┘   └───────────────┬──────────────┘
                         └──────────────┬────────────────────┘
Phase 2  Joint synthesis (leads converge OR consolidator): cross-pillar
         throughline table + falsifier/discriminator map + c-compare table
         → SYNTHESIS doc
```

Each lead is a **sub-orchestrator**: it reads its corpus slice + prior anchors, decides which roster specialists it needs, dispatches them via the `Agent` tool (`subagent_type` from `agent-roster.md`), waits for on-disk artifacts, verifies them (per `agent-standards.md` completion verification), and folds them into its working paper. Leads cap their own recursive fan-out at **≤4 concurrent** and roll in batches.

---

## 4. LEAD A — `hawking-theorist` · Black-Hole Cosmology + Horizon Physics

**Owns**: Pillar A (all 19 BH-cosmology papers) + the horizon-reality half of Pillar C (Cardoso-Pani horizon tests #08, Mathur causality #13, echo theory #05/#09).

**Why Hawking**: singularity theorems, global causal structure (Penrose diagrams, trapped surfaces), Hawking radiation / Bogoliubov / information paradox, de Sitter `T=H/2π`, and analog-horizon kinematics — exactly the toolkit for "is our universe inside a horizon, and what replaces the singularity."

**Prior anchors to load**: S42 incursion; S85 acoustic-white-hole theorem; the Hawking-collab lineage; `c-compare`.

**Recursive sub-targets** (Lead A picks from these per need, ≤4):
- `schwarzschild-penrose` (sp) — **near-certain**: exact-solution causal structure, Penrose diagrams of universe-in-BH, junction conditions, trapped-surface analysis of the torsion bounce vs the acoustic boundary.
- `dirac-antimatter-theorist` — Poplawski's mechanism IS spinor-torsion (Einstein-Cartan-Sciama-Kibble: Dirac spin sources torsion); baryon-asymmetry-from-torsion angle.
- `transit-dynamics-theorist` — bounce dynamics ↔ first-order transit; Parker particle production at a bounce vs GGE relic at the fold; Gaztañaga bounce relics (#19).
- `kaluza-klein-theorist` / `baptista-spacetime-analyst` — torsion / Einstein-Cartan gravity vs the framework's KK geometry on SU(3) (do they share dynamical-compactification structure?).
- `kitaev-quantum-chaos-theorist` — information/scrambling, if the information-paradox throughline (T8) goes deep.

**Deliverable**: `sessions/bh-cosmo-incursion/wp-A-bh-cosmology-hawking.md` — answers throughlines T1, T2, T8, T9 (lead) + contributes to T7, T10; a `c-compare` classification of every horizon/boundary feature in Pillar A; a Penrose-diagram comparison (universe-in-BH vs acoustic-white-hole transit, ASCII).

---

## 5. LEAD B — `mack-cosmic-bridge` · Gravastar Condensate Stars + Dark Energy + Observational Discriminators

**Owns**: Pillar B (all 21 GVCS papers) + the observational-discriminator half of Pillar C (shadows #03, QNM #01/#04, echo claim/rebuttal #06/#07/#10/#12, status LRR #11, SgrA* flares #14, spectral instability #15) + the cosmological-coupling thread (#08/#15/#16, which physically sits in Pillar A but is a dark-energy claim).

**Why Mack**: dark-energy `w(z)`, vacuum decay / phase transitions, observational fidelity (Planck/DESI/JWST), and **sole writer of `falsifier-master-inventory.md`** — so the discriminator/falsifier map is hers. She is the guardian against overstating GR-side agreement and against resurrecting the retired GW falsifier.

**Prior anchors to load**: `w0_FW=−0.918` + DILUTION-CC (S66); R_842 dS-branch rectangle; CC=a₀ moment; the retired-GW-falsifier note; S99 dark-energy litreviews (`session-99-litrev-dark-energy-mack.md`).

**Recursive sub-targets** (Lead B picks, ≤4):
- `volovik-superfluid-universe-theorist` — **essential**: the gravastar `p=−ρ` de Sitter condensate interior IS the GR-side image of the Volovik q-theory vacuum; de Sitter decay thermodynamics; emergent-horizon-as-acoustic-feature. The framework's #1 theorist on exactly this.
- `lizzi-spectral-functional-theorist` — Mottola's **trace anomaly → dynamical dark energy** ↔ the framework's CC = a₀ zeroth spectral moment; does Mottola's effective-theory-of-gravity mechanism map onto spectral-action moment structure?
- `sagan-empiricist` — **essential** adversarial: the echo claim (Abedi-Afshordi 2.5σ/4.2σ) vs the Ashton/LVC rebuttal; Farrah k≈3 vs Rodriguez NGC3201 counter-constraint. Keeps the observational chain honest.
- `landau-condensed-matter-theorist` — gravastar = gravitational BEC; Ginzburg-Landau order parameter at the `p=+ρ` shell; condensate phase-boundary physics.
- `little-red-dots-jwst-analyst` — Farrah cosmological coupling ↔ overmassive BHs / JWST LRD demographics.

**Deliverable**: `sessions/bh-cosmo-incursion/wp-B-gravastar-de-mack.md` — answers throughlines T3, T4, T5, T6 (lead) + contributes to T7, T10; a **falsifier/discriminator table** (which ECO observable distinguishes condensate-surface from true-horizon, with current σ-status and detector horizon, framed as GR-side discrimination NOT a live framework gate); a `w(z)` / vacuum-EoS comparison table (gravastar dS interior vs `w0_FW` vs R_842 branches).

---

## 6. Recursive dispatch protocol (how leads use `agent-roster.md`)

Each lead, after its own first read, executes:

1. **Select** ≤4 specialists from `agent-roster.md` whose domain a throughline genuinely needs (domain-routing, not padding). Resolve name → `subagent_type` via the roster table.
2. **Dispatch** each sub via the `Agent` tool with a **complete, self-contained prompt**: the specific throughline question, the exact corpus papers to read (by INDEX path + arXiv ID), the prior-anchor it must respect, the substrate-first framing law, and the explicit write-target (a named section the lead will fold in OR a short return payload). One concrete deliverable per sub.
3. **Wait** for completion, then **verify on disk** — do not trust the sub's self-report (per `agent-standards.md` + `team-lead-behavior.md`). Re-read the artifact; check it answers the question and respects the framing.
4. **Fold** the verified sub-result into the lead's working paper with attribution (`[via <agent>]`).

**Neutrality guard** (`feedback_review-dispatch-no-orchestrator-angle.md`): the lead routes by *domain*, not by *desired conclusion*. A sub prompt states the question + sources + framing; it does NOT say "push on X" or "confirm Y." Where two readings genuinely diverge (e.g. T1, T7 below), the lead frames it as an **open adversarial question** and may stage a 2-agent micro-workshop, not a steered answer.

---

## 7. Joint synthesis (Phase 2)

After both WPs land, the two leads converge (or a consolidator agent does) into `sessions/bh-cosmo-incursion/SYNTHESIS-bh-cosmo-exflation.md`:

- **Cross-pillar throughline table** (T1–T10): for each, the GR-side claim, the substrate-IS anchor, the verdict (same-structure / GR-shadow-of-substrate / genuinely-distinct / open-tension), and the supporting sub-agent work.
- **`c-compare` master table**: every horizon/boundary/surface in the corpus classified PROPAGATION vs SUBSTRATE-DYNAMICS vs MIXED.
- **Discriminator/falsifier map** (Mack, sole writer): GR-side observational tests (echo, shadow, QNM, spectral-instability, cosmological-coupling) — what each would distinguish, current status, detector horizon — explicitly tagged GR-side-discrimination, with the retired-GW-framework-falsifier caveat.
- **Carry-forwards**: any genuine new framework gate (4-field spec) routed to `/rclab-plan`; any adversarial tension routed to a workshop.

---

## 8. The 10 pre-registered throughline questions (the campaign spine)

| # | Question | GR side | Substrate anchor | Lead (+subs) |
|:--|:--|:--|:--|:--|
| **T1** | Is "universe inside a black hole" the **same causal structure** as the acoustic-white-hole transit, or distinct? | Poplawski/Gaztañaga interior; r_S=√(3/Λ) | S85 PROVEN pre/post-fold causal disconnect; Mach 13.75 | A (sp) |
| **T2** | Torsion **bounce** vs first-order **transit** — what's preserved, what differs? | ECSK spinor-torsion nonsingular bounce (#04,06) | tau-fold transit = instanton gas, NOT potential well | A (dirac, transit) |
| **T3** | Gaztañaga "**CC as event horizon**" vs CC as **a₀ zeroth moment** — reconcile or contrast. | Λ as causal-boundary term (#13) | `Λ_cc=(2f_0/f_2)a_0`, `a₀^ζ=6440` | B (lizzi, connes) |
| **T4** | Gravastar **de Sitter interior** (p=−ρ) vs **Volovik q-theory vacuum** (w₀=−0.918) — is the gravastar the GR shadow of the substrate vacuum? | Mazur-Mottola dS condensate (#01,04) | w0_FW; R_842 dS branches | B (volovik) |
| **T5** | Mottola **trace anomaly → DE** vs framework **spectral-action moment** structure. | Trace-anomaly effective theory (#09,16,20) | a₀/a₂/a₄ Seeley-DeWitt; DILUTION-CC | B (lizzi) |
| **T6** | Farrah **cosmological coupling** (k≈3) vs **substrate compaction / DILUTION-CC** — same physics? where does NGC3201 land? | Farrah #15; Rodriguez counter #16 | Volovik tracking vacuum; w_a compaction | B (sagan, little-red-dots) |
| **T7** | Horizon as **causal boundary** vs **acoustic phase boundary** — the ECO discriminator. | echoes/shadows/QNM (Pillar C) | horizons-as-acoustic-features; c-compare | A+B (sagan) |
| **T8** | **Information paradox** under condensate-surface substitution (no horizon ⇒ no loss). | GVCS/ECO horizonless (#11,18) | substrate-IS; no Bekenstein-Hawking interior | A (kitaev) |
| **T9** | Smolin **CNS / cosmic reproduction** vs measurement=vacuum-decay=baby-universe lore — falsifiable? | Smolin CNS (#02); Easson-Brandenberger (#01) | `project_cosmic-reproduction.md` | A+B |
| **T10** | Gaztañaga **bounce relics** (BH/GW/DM #19) vs **GGE relic** formation at the fold. | bounce-relic populations (#19) | 59.8 GGE pairs, Parker production at fold | B (transit) |

---

## 9. Outputs & file layout

```
sessions/bh-cosmo-incursion/
  00-investigation-plan.md                  (this file)
  wp-A-bh-cosmology-hawking.md              (Lead A working paper)
  wp-B-gravastar-de-mack.md                 (Lead B working paper)
  subs/                                      (recursive sub-agent return artifacts, if file-based)
  SYNTHESIS-bh-cosmo-exflation.md           (Phase 2 cross-pillar synthesis)
```

(Outputs are an active investigation, NOT curated framework docs — they do not land in `sessions/framework/` until reviewed. Genuine new constants/gates route through the canonical write-order + `/rclab-plan`.)

---

## 10. Sequencing, concurrency, cost

- **Phase 1**: Lead A ∥ Lead B (independent pillars). Each lead spawns ≤4 recursive subs in batches; peak global concurrency managed by the leads (queue if the harness caps at 8).
- **Phase 2**: after both WPs verified on disk.
- **Estimated fleet**: 2 leads + ~6–8 recursive subs + (0–1) consolidator ≈ **9–11 agents**, all Opus-tier (physics depth, per `feedback_max-effort-full-fidelity.md`).
- **Verification gate**: orchestrator verifies each WP + each sub artifact on disk before advancing phases (no advancing on self-reports).

## 11. Launch checklist (orchestrator)

- [ ] User approves architecture / scope.
- [ ] Confirm leads load prior anchors (§2) before forming throughlines.
- [ ] Dispatch Lead A + Lead B with full self-contained prompts (question set + corpus slice + anchors + framing law + write-target).
- [ ] Verify WP-A, WP-B on disk; spot-check sub artifacts.
- [ ] Dispatch Phase-2 synthesis; verify.
- [ ] Route carry-forwards (new gates → `/rclab-plan`; tensions → workshop).
