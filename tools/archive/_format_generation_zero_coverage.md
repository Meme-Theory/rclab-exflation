# Zero-coverage report (Phase 0.9)

Scanned **1328** session .md files. **281** emit zero attribution edges (21.2%).

## Distribution by category

| Category | Count | Meaning |
|:---------|------:|:--------|
| FORMAT-MISS | 203 | File SHOULD have attribution but no regex fires. Regex-refinement OR orphan-content candidate. |
| SHELL | 7 | File is a pre-allocated empty shell (e.g., S91 W4 `awaiting runtime compute dispatch`). Attribution will land when compute runs. |
| DATA-ONLY | 1 | File is mostly tables / short stub / data-listing. No attribution by design. |
| SYSTEM-FILE | 57 | Project-scaffolding (plans, schedules, indexes, ledgers, seeds). Attribution is project-level, not file-level. |
| PRE-G3-NARRATIVE | 13 | G1 session file. Pre-formal-attribution era; expected. |

## FORMAT-MISS sub-classification

The FORMAT-MISS pool splits into TWO distinct sub-classes:

**(A) Master-aggregator pattern (design-correct)** — Files where authorship is offloaded to sister files. The aggregator (`session-N-results-workingpaper.md`, `session-N-master-collab.md`, `session-N-master-synthesis.md`) is orchestrator-aggregated; the per-author content lives in `session-N-{agent}-{topic}.md` siblings. The session as a whole IS attributed; only the roll-up file individually has no per-file author marker.

**(B) Orphan-content candidates (the 'lost ideas' pool)** — Files matching no recognized archetype. These are peculiar one-offs: cross-session reviews, special audits, way-forward planning docs, named meta-documents. Worth manual inspection.

- **(A) Master-aggregator pattern**: 47 files
- **(B) Orphan-content candidates**: 156 files

## (B) Orphan-content candidates (156 files) — the 'lost ideas' surface

These are FORMAT-MISS files that DON'T match any standard aggregator archetype. Sorted by size (largest first). Each is a candidate for one of: (i) genuine orphan content worth re-surfacing, (ii) a one-off format the regex doesn't catch yet, (iii) an unusual review/audit pattern.

| Gen | Session | File | Size | First header | Head preview |
|:---|:--------|:-----|-----:|:-------------|:-------------|
| G7 | S84 | `session-84-w10-workingpaper.md` | 172,920 | Session 84 — Wave 10 Working Paper | # Session 84 — Wave 10 Working Paper **Session**: 84 **Wave**: 10 (consolidated from sub-waves W10a and W10b) **Theme**: |
| G4 | S60 | `session-60-wayforward.md` | 168,290 | Session 60 Way Forward: Extracted Computation Agenda | # Session 60 Way Forward: Extracted Computation Agenda **Date**: 2026-03-27 **Source**: S60 collab reviews (9 reviewers) |
| G3 | S25 | `session-25/session-25-Investigation-Collaborate-Efforts.md` | 161,045 | CollaborativeSynergy: Session 25 Collaborative Suggestions | # CollaborativeSynergy: Session 25 Collaborative Suggestions ## 15 Researchers, Full Contribution Index **Date**: 2026-0 |
| G7 | S84 | `session-84-w2-workingpaper.md` | 154,137 | Session 84 Wave 2 — Three-Layer Regulator Theorem Family (Results Working Paper) | # Session 84 Wave 2 — Three-Layer Regulator Theorem Family (Results Working Paper) **Session**: 84 \| **Wave**: 2 \| **Pla |
| G7 | S84 | `session-84-w4-workingpaper.md` | 152,321 | Session 84 Wave 4 — Observational & Detector Forecasts (Results Working Paper) | # Session 84 Wave 4 — Observational & Detector Forecasts (Results Working Paper) **Session**: 84 \| **Wave**: 4 \| **Plan* |
| G7 | S84 | `session-84-w7-workingpaper.md` | 146,712 | Session 84 — Wave 7 Working Paper | # Session 84 — Wave 7 Working Paper ## String / M-theory / Matrix-Model / KK Extensions (13 gates) **Session**: 84 **Wav |
| G3 | S25 | `session-25/session-25-Investigation-Question-Efforts.md` | 136,476 | QuestionSynergy: Session 25 Open Questions | # QuestionSynergy: Session 25 Open Questions ## The Deepest Questions from 15 Perspectives **Date**: 2026-02-21 --- ## S |
| G7 | S87 | `workshops/s87-cf29-substantive-reading-carve-out.md` | 115,452 | Workshop W-3 — CF-29 substantive-reading carve-out vs rule-strict mechanical closure | # Workshop W-3 — CF-29 substantive-reading carve-out vs rule-strict mechanical closure **Date**: 2026-05-02 **Format**:  |
| G7 | S86 | `session-86-w0c-workingpaper.md` | 115,375 | Session 86 Wave W0c — canonical_constants.py consolidation + computation lifts (Results Working Paper) | # Session 86 Wave W0c — canonical_constants.py consolidation + computation lifts (Results Working Paper) **Session**: 86 |
| G4 | S52 | `session-52-phonon-workshop.md` | 109,880 | Session 52 Phonon Workshop: Correcting the Course | # Session 52 Phonon Workshop: Correcting the Course **Date**: 2026-03-20 **Format**: 2-agent solo workshop (QA + Tesla), |
| G7 | S84 | `session-84-w3-workingpaper.md` | 106,906 | Session 84 Wave 3 — CC-5 Propagation Atlas (Results Working Paper) | # Session 84 Wave 3 — CC-5 Propagation Atlas (Results Working Paper) **Session**: 84 \| **Wave**: 3 \| **Plan**: session-8 |
| G7 | S84 | `session-84-w6-workingpaper.md` | 104,923 | Session 84 Wave 6 — Field-Theory Dressing + CGWB + Sibling Observables (Results Working Paper) | # Session 84 Wave 6 — Field-Theory Dressing + CGWB + Sibling Observables (Results Working Paper) **Session**: 84 \| **Wav |
| G5 | S74 | `session-74-tgf-pre-registration.md` | 101,661 | TGF Pre-Registered Framework Prediction | # TGF Pre-Registered Framework Prediction ## Session 74, 2026-04-11 ## Author: Transit-Dynamics-Theorist (non-equilibriu |
| G3 | S25 | `session-25/session-25-Investigation-Assessment-Efforts.md` | 98,960 | AssessmentSynergy: Session 25 Goal Assessments | # AssessmentSynergy: Session 25 Goal Assessments ## 15 Researchers, 8 Goals **Date**: 2026-02-21 --- ## Goal 1: Graded M |
| G7 | S87 | `workshops/s87-a0-r-protection-m2-biconditional.md` | 87,016 | Workshop W-1 — A0-R-protection ⟺ M2 biconditional sufficiency | # Workshop W-1 — A0-R-protection ⟺ M2 biconditional sufficiency **Date**: 2026-05-02 **Format**: 3-round iterative 2-age |
| G3 | S19 | `session-19/session-19-primer.md` | 63,600 | Session 19 Primer: Spectral Complexity as Vacuum Selection | # Session 19 Primer: Spectral Complexity as Vacuum Selection **Date**: 2026-02-15 **Team**: session-19-primer (2 agents) |
| G5 | S74 | `session-74-rf-analysis.md` | 59,396 | Session 74 — RF / Coherent-Array Retrospective-Analysis Dossier | # Session 74 — RF / Coherent-Array Retrospective-Analysis Dossier ## Looking For Substrate Pair Production Hiding In Exi |
| G3 | S27 | `session-27/session-27-wrapup.md` | 58,682 | Session 27 Wrap-Up | # Session 27 Wrap-Up **Date**: 2026-02-26 **Priorities**: 3 (serial execution: P1 → P2 → P3) **Motivation**: Baptista au |
| G7 | S91 | `DIA-investigation-schedule.md` | 57,946 | Session 91 — DIA Investigation Schedule | # Session 91 — DIA Investigation Schedule **Date drafted**: 2026-05-17 **Scope**: Three-workshop investigation track sur |
| G4 | S44 | `session-44/session-44-quicklook-sp-collab.md` | 57,935 | Schwarzschild-Penrose -- Collaborative Feedback on Session 44 | # Schwarzschild-Penrose -- Collaborative Feedback on Session 44 **Date**: 2026-03-15 **Source**: `sessions/session-44/se |
| G3 | S21 | `session-21/session-21c-phase0-synthesis.md` | 51,570 | Session 21c: Phase 0 Execution + Flux-Spectral Synthesis | # Session 21c: Phase 0 Execution + Flux-Spectral Synthesis **Date**: 2026-02-19 **Session Type**: Computation + Live Syn |
| G4 | S44 | `session-44/session-44-quicklook-connes-collab.md` | 50,941 | Connes -- Collaborative Feedback on Session 44 | # Connes -- Collaborative Feedback on Session 44 **Date**: 2026-03-15 **Reviewing**: Session 44 Quicklook (31 computatio |
| G7 | S85 | `session-85-4a-elimination-bulletins-kaku.md` | 49,098 | S85 Row 4A — Structural-Elimination Bulletins (kaku-speculative-theorist) | # S85 Row 4A — Structural-Elimination Bulletins (kaku-speculative-theorist) **Session**: 85 \| **Slot**: 1b Row 4A \| **Tr |
| G3 | S21 | `session-21/session-21a-ainur-synthesis.md` | 48,451 | Session 21a: The Resonance Interpretation — Ainur Panel Synthesis | # Session 21a: The Resonance Interpretation — Ainur Panel Synthesis **Date**: 2026-02-19 **Session Type**: Theoretical I |
| G4 | S54 | `session-54-extraction-collabs.md` | 48,372 | Session 54 Collaborative Review -- Computation Extraction | # Session 54 Collaborative Review -- Computation Extraction All computation suggestions, recommendations, and proposed c |
| G7 | S88 | `workshops/s88-w3-w1b1-63-3branch.md` | 46,086 | S88 Workshop W3 — §W1b1-63 FAIL 3-Branch Interpretation: L_pix-convention vs cascade-depth-internal-entropy vs Bekenstei | # S88 Workshop W3 — §W1b1-63 FAIL 3-Branch Interpretation: L_pix-convention vs cascade-depth-internal-entropy vs Bekenst |
| G3 | S25 | `session-25/session-25-Investigation-Closing.md` | 45,855 | Session 25 Closing: The Post-Trial Verdict | # Session 25 Closing: The Post-Trial Verdict **Date**: 2026-02-22 (rewritten from pre-computation skeleton of 2026-02-21 |
| G4 | S43 | `session-43/session-43-quicklook.md` | 45,059 | Session 43 Quicklook: Cold Big Bang | # Session 43 Quicklook: Cold Big Bang **Date**: 2026-03-14 **Prior**: 18% (S42, 68% CI 11-30%) **Master gate**: QFIELD-4 |
| G7 | S88 | `workshops/s88-mack-arxiv-2511-07517-desi-review.md` | 44,519 | Mack solo synthesis — DES-Dovekie reanalysis (arXiv:2511.07517v3) | # Mack solo synthesis — DES-Dovekie reanalysis (arXiv:2511.07517v3) > **Author**: mack-cosmic-bridge (solo, off-wave SOL |
| G5 | S61 | `session-61-midsession-review.md` | 44,495 | Session 61 Mid-Session Review | # Session 61 Mid-Session Review **Date**: 2026-03-28 **Assessor**: Sagan-Empiricist (sole probability estimator) **Sessi |
| G3 | S20 | `session-20/session-20c-synthesis.md` | 42,761 | Session 20c: Synthesis + Hanging Task Triage + Session 21 Gate | # Session 20c: Synthesis + Hanging Task Triage + Session 21 Gate **Date**: 2026-02-19 **Session Type**: Review + Plannin |
| G2 | S16 | `session-16/session-16-round-3b-theoretical.md` | 42,755 | Session 16, Round 3b: Theoretical Action Items — Executable Specifications | # Session 16, Round 3b: Theoretical Action Items — Executable Specifications ## QA-Theorist + Baptista-Analyst + Paasch- |
| G3 | S33 | `session-33/session-33-w1-math-permanence.md` | 42,111 | Session 33 Workshop 1: Mathematical Permanence | # Session 33 Workshop 1: Mathematical Permanence **Date**: 2026-03-06 **Type**: Panel (exploratory workshop, 2 rounds) * |
| G2 | S16 | `session-16/session-16-round-3a-computational.md` | 41,987 | Session 16, Round 3a: Computational Action Items (Executable Specifications) | # Session 16, Round 3a: Computational Action Items (Executable Specifications) ## KK-Theorist + Sim-Specialist Joint Spe |
| G7 | S85 | `session-85-s1-regulator-boundary-van-den-dungen.md` | 41,537 | Session 85 Slot S-1 — Regulator-Family Boundary Theorem (van den Dungen / Kasparov-KK track) | # Session 85 Slot S-1 — Regulator-Family Boundary Theorem (van den Dungen / Kasparov-KK track) **Session**: 85 \| **Slot* |
| G2 | S16 | `session-16/session-16-round-3c-priorities.md` | 39,467 | Session 16, Round 3c: Master Priority Ranking and Pre-Registration | # Session 16, Round 3c: Master Priority Ranking and Pre-Registration ## Gen-Physicist (writer) + Sagan-Empiricist (Venus |
| G4 | S44 | `session-44/s44_sagan_assessment.md` | 39,415 | Session 44 Sagan Assessment | # Session 44 Sagan Assessment **Date**: 2026-03-15 **Prior**: 12% (68% CI: 8-16%) from S43 Redux **Session**: 44 (31 com |
| G2 | S16 | `session-16/session-16-round-2d-giants-eval-ii.md` | 38,865 | Session 16, Round 2d-ii: Evidence Standards and Updated Assessment | # Session 16, Round 2d-ii: Evidence Standards and Updated Assessment ## Hawking-Theorist + Sagan Joint Evaluation ## Dat |
| G4 | S45 | `session-45/session-45-quicklook.md` | 38,763 | Session 45 Quicklook | # Session 45 Quicklook **Date**: 2026-03-15 **Prior session**: S44 (7-agent collaboration, P_prior = 23%) **Format**: Pa |
| G3 | S28 | `session-28/session-28-fusion-synthesis.md` | 38,317 | Session 28 Grand Fusion Synthesis | # Session 28 Grand Fusion Synthesis ## Four-Way Deliberation Across All Team Syntheses **Date**: 2026-02-27 **Fusion Tea |
| G7 | S85 | `session-85-s3-alphas-registry-mack.md` | 38,067 | Session 85 — Slot S-3 Solo Synthesis (mack-cosmic-bridge) | # Session 85 — Slot S-3 Solo Synthesis (mack-cosmic-bridge) **Angle**: Observational falsifier ledger — consolidate §VII |
| G2 | S16 | `session-16/session-16-round-2a-veff.md` | 37,891 | Session 16, Round 2a: V_eff Deep Dive | # Session 16, Round 2a: V_eff Deep Dive ## KK-Theorist + Gen-Physicist + Sim-Specialist ## Date: 2026-02-13 ## Status: D |
| G7 | S90 | `session-90-connes-s5-pin-derivative-synthesis.md` | 35,586 | Executive verdict | --- title: S90 Slot 1 Entry S-5 — Connes Independent Synthesis on the 6× Class-(d) PIN-DERIVATIVE Recurrence in W6 sessi |
| G7 | S88 | `workshops/s88-w1-substrate-clock-cancellation.md` | 34,389 | Substrate-clock cardinality-vs-dilution-cubic cancellation: substrate-IS theorem vs convention-tautology — STRUCTURAL VE | # Substrate-clock cardinality-vs-dilution-cubic cancellation: substrate-IS theorem vs convention-tautology — STRUCTURAL  |
| G2 | S16 | `session-16/session-16-round-2b-dk-generations.md` | 34,062 | Session 16, Round 2b: D_K and Generations | # Session 16, Round 2b: D_K and Generations ## Baptista-Analyst + KK-Theorist Joint Assessment ## Date: 2026-02-13 ## St |
| G4 | S52 | `session-52-way-forward.md` | 33,789 | Session 52 — Way Forward | # Session 52 — Way Forward **Date**: 2026-03-21 (post-session synthesis) **Source**: Exhaustive extraction from 12 sessi |
| G4 | S60 | `session-60-synthesis.md` | 33,450 | Session 60 Synthesis: The Audit | # Session 60 Synthesis: The Audit **Date**: 2026-03-27 **Session type**: SYNTHESIS **Synthesizer**: mack-cosmic-bridge ( |
| G4 | S54 | `session-54-extraction-workshops.md` | 33,161 | Session 54 Workshop Extraction: All Computation Suggestions, Gates, and Open Questions | # Session 54 Workshop Extraction: All Computation Suggestions, Gates, and Open Questions **Date**: 2026-03-22 **Extracte |
| G7 | S85 | `session-85-s2-k-corridor-landau.md` | 32,657 | Session 85 — Slot S-2 Solo Synthesis | # Session 85 — Slot S-2 Solo Synthesis ## K-Corridor Structural Geometry Phenomenology (landau-condensed-matter-theorist |
| G2 | S16 | `session-16/session-16-round-1e-hawking-sagan.md` | 32,423 | Session 16, Round 1e: Thermodynamics and Evidence | # Session 16, Round 1e: Thermodynamics and Evidence ## Hawking-Theorist + Sagan Joint Assessment ## Date: 2026-02-13 --- |
| G4 | S44 | `session-44/session-44-quicklook-nazarewicz-collab.md` | 31,846 | Nazarewicz -- Collaborative Feedback on Session 44 | # Nazarewicz -- Collaborative Feedback on Session 44 **Date**: 2026-03-15 **Session reviewed**: S44 Quicklook (31 comput |
| G7 | S85 | `session-85-s1-regulator-boundary-connes.md` | 31,670 | Session 85 Slot S-1 — Regulator-Family Boundary Theorem (Connes K-theory / cyclic-cohomology track) | # Session 85 Slot S-1 — Regulator-Family Boundary Theorem (Connes K-theory / cyclic-cohomology track) **Session**: 85 \|  |
| G3 | S33 | `session-33/session-33a-synthesis.md` | 31,485 | Session 33a Synthesis: Five Zero-Cost Diagnostics | # Session 33a Synthesis: Five Zero-Cost Diagnostics **Date**: 2026-03-06 **Sub-session**: 33a (of 33a + 33b) **Agents**: |
| G2 | S16 | `session-16/session-16-round-2c-theory.md` | 31,165 | Session 16, Round 2c: Theoretical Frontiers | # Session 16, Round 2c: Theoretical Frontiers ## QA-Theorist + Paasch-Analyst Joint Assessment ## Date: 2026-02-13 ## St |
| G2 | S16 | `session-16/session-16-round-2d-giants-eval.md` | 31,068 | Session 16, Round 2d-i: Giants Evaluate Everything | # Session 16, Round 2d-i: Giants Evaluate Everything ## Einstein-Theorist + Feynman Joint Assessment ## Date: 2026-02-13 |
| G7 | S88 | `workshops/s88-w2-kz-universality-class.md` | 31,065 | S88 W1a Workshop 2 — K-Z Saturation Cap Dominance ~332 OOM: Substrate-Physics Structural Prediction vs Loose-ξ_KZ-Pin Co | # S88 W1a Workshop 2 — K-Z Saturation Cap Dominance ~332 OOM: Substrate-Physics Structural Prediction vs Loose-ξ_KZ-Pin  |
| G3 | S29 | `session-29/session-29-observational-excursion.md` | 30,815 | Observational Excursion: What Can We See and When | # Observational Excursion: What Can We See and When **Team**: Einstein, Cosmic-Web, Little Red Dots, Hawking **Date**: 2 |
| G3 | S25 | `session-25/session-25-Investigation-Framework.md` | 30,674 | FrameworkSynergy: Session 25 Framework — Post-Trial Verdict | # FrameworkSynergy: Session 25 Framework — Post-Trial Verdict ## 57 Computations, 10 Workshop Agents, 6 Walls **Date**:  |
| G3 | S29 | `session-29/session-29-team-A-synthesis.md` | 30,520 | Team A Synthesis: Geometric Foundations | # Team A Synthesis: Geometric Foundations **Team**: Einstein, Baptista, Schwarzschild-Penrose, Kaluza-Klein **Designated |
| G3 | S29 | `session-29/session-29-team-E-synthesis.md` | 30,396 | Team E Synthesis: Observational Contact & Empirical Tests | # Team E Synthesis: Observational Contact & Empirical Tests **Team**: Sagan, Cosmic Web, Little Red Dots **Designated Wr |
| G5 | S72 | `session-72-audit-gen-physicist.md` | 30,250 | Session 72 Project Audit: General Physics | # Session 72 Project Audit: General Physics **Date**: 2026-04-10 **Scope**: Sessions 1-72, all atlas documents, EVOI fra |
| G5 | S64 | `s64-collab-extraction.md` | 29,951 | S64 Collab + Investigation Extraction for S65 Planning | # S64 Collab + Investigation Extraction for S65 Planning **Generated**: 2026-04-02 **Sources**: 7 collaborative reviews  |
| G4 | S54 | `session-54-qa-hawking-workshop-synthesis.md` | 29,931 | QA x Hawking Workshop Synthesis: Session 54 | # QA x Hawking Workshop Synthesis: Session 54 ## Quantum Acoustics Meets Semiclassical Gravity on the 32-Cell Lattice ** |
| G6 | S79 | `session-79-final.md` | 29,797 | Session 79 — Final Handoff | # Session 79 — Final Handoff **Format**: 7-section handoff per `.claude/rules/output-standards.md` **Closing date**: 202 |
| G4 | S44 | `session-44/session-44-quicklook.md` | 29,779 | Session 44 Quicklook: Sakharov-GN, CDM-Construct, Trace-Log CC, Spectral Diagnostics | # Session 44 Quicklook: Sakharov-GN, CDM-Construct, Trace-Log CC, Spectral Diagnostics **Date**: 2026-03-15 **Prior**: 1 |
| G3 | S29 | `session-29/session-29-fusion-synthesis.md` | 29,478 | Session 29 Fusion Synthesis | # Session 29 Fusion Synthesis ## Cross-Document Deliberation: Team Syntheses + Observational Excursion + Connes NCG Excu |
| G2 | S16 | `session-16/session-16-round-2a-hawking-thermodynamics.md` | 29,317 | Session 16, Round 2a: Thermodynamic Framework for V_eff | # Session 16, Round 2a: Thermodynamic Framework for V_eff ## Hawking-Theorist Contribution ## Date: 2026-02-13 --- ## PR |
| G3 | S29 | `session-29/session-29-wrapup.md` | 29,155 | Session 29 Wrapup | # Session 29 Wrapup **Date**: 2026-02-28 **Sub-sessions**: 29Aa, 29Ab, 29Ac, 29Ba, 29Bb **Total computations**: 17 (29a- |
| G4 | S44 | `session-44/session-44-quicklook-einstein-collab.md` | 28,788 | Einstein -- Collaborative Feedback on Session 44 | # Einstein -- Collaborative Feedback on Session 44 **Date**: 2026-03-15 **Prior session**: S43 (12%, 68% CI 8-16%) **Spe |
| G3 | S28 | `session-28/session-28-team-synthesis-b.md` | 28,341 | Team Synthesis B: Einstein + Hawking + Cosmic-Web | # Team Synthesis B: Einstein + Hawking + Cosmic-Web ## Session 28 Collaborative Review -- 3-Round Deliberation **Partici |
| G5 | S64 | `s64-synthesis-extraction.md` | 28,221 | S64 Synthesis + Working Paper Extraction for S65 Planning | # S64 Synthesis + Working Paper Extraction for S65 Planning **Date**: 2026-04-02 **Source files**: session-64-results-wo |
| G5 | S68 | `session-68-phonon-vs-data-plan.md` | 28,084 | PHONON-VS-DATA: Framework Stress Test Suite Against Astronomical Data | # PHONON-VS-DATA: Framework Stress Test Suite Against Astronomical Data **Author:** Katie Mack (Cosmic Bridge Agent) **D |
| G4 | S43 | `session-43/session-43-quicklook-hawking-collab.md` | 27,754 | Hawking Theorist -- Collaborative Feedback on Session 43 | # Hawking Theorist -- Collaborative Feedback on Session 43 **Date**: 2026-03-14 **Session**: 43 (Cold Big Bang) **My com |
| G3 | S29 | `session-29/session-29-team-B-synthesis.md` | 27,318 | Team B Synthesis: Spectral Geometry & Topology | # Team B Synthesis: Spectral Geometry & Topology **Team**: Connes, Berry, Paasch **Designated Writer**: Connes **Date**: |
| G3 | S29 | `session-29/session-29-team-C-synthesis.md` | 26,639 | Team C Synthesis: BCS Mechanism & Condensed Matter | # Team C Synthesis: BCS Mechanism & Condensed Matter **Team**: Landau, Feynman, Quantum Acoustics, Tesla **Designated Wr |
| G4 | S54 | `session-54-master-workshop-synthesis.md` | 26,481 | Session 54 Master Workshop Synthesis | # Session 54 Master Workshop Synthesis ## Three Workshops, Six Specialists, One Lattice **Date**: 2026-03-22 **Synthesis |
| G3 | S28 | `session-28/session-28-team-synthesis-d.md` | 26,288 | Team Synthesis D: KK + Baptista + Berry + Connes | # Team Synthesis D: KK + Baptista + Berry + Connes ## Session 28 Collaborative Review -- 4-Round Deliberation **Particip |
| G4 | S46 | `session-46/session-46-quicklook-dirac-collab.md` | 25,983 | Session 46 Collaborative Review — Dirac Antimatter Theorist | # Session 46 Collaborative Review — Dirac Antimatter Theorist **Date**: 2026-03-15 **Perspective**: Charge conjugation,  |
| G3 | S24 | `session-24/session-24b-synthesis.md` | 25,773 | Session 24b Synthesis: Sagan Verdict + Einstein Interpretation — V-1 CLOSED confirmed | # Session 24b Synthesis: Sagan Verdict + Einstein Interpretation — V-1 CLOSED confirmed **Date**: 2026-02-21 **Session t |
| G3 | S29 | `session-29/session-29Ac-synthesis.md` | 25,623 | Session 29Ac Synthesis: Observational Predictions | # Session 29Ac Synthesis: Observational Predictions **Date**: 2026-02-28 **Sub-session**: 29Ac (observational prediction |
| G2 | S16 | `session-16/session-16-round-1d-einstein-feynman.md` | 25,491 | Session 16, Round 1d: Einstein-Feynman Discussion | # Session 16, Round 1d: Einstein-Feynman Discussion ## Date: 2026-02-13 ## Participants: Einstein-Theorist + Feynman (Gi |
| G4 | S54 | `session-54-phonon-landau-workshop-synthesis.md` | 25,392 | Phonon x Landau Workshop Synthesis: Session 54 | # Phonon x Landau Workshop Synthesis: Session 54 ## Cross-Domain Patterns Meet Condensed Matter Precision **Date**: 2026 |
| G4 | S46 | `session-46/session-46-quicklook.md` | 25,339 | Session 46 Quicklook | # Session 46 Quicklook **Date**: 2026-03-15 **Prior**: S45 -- Q-THEORY-BCS PASS (tau* = 0.209), ALPHA-EFF 0.410 (1.06x), |
| G3 | S29 | `session-29/session-29Bb-synthesis.md` | 24,567 | Session 29Bb Synthesis: Jensen Stability + Thermal Goldilocks + Josephson Coupling | # Session 29Bb Synthesis: Jensen Stability + Thermal Goldilocks + Josephson Coupling **Date**: 2026-02-28 **Session type |
| G3 | S33 | `session-33/session-33b-synthesis.md` | 24,404 | Session 33b Synthesis: TRAP-33b PASS, NUC-33b FAIL, and the Complete Mechanism Chain | # Session 33b Synthesis: TRAP-33b PASS, NUC-33b FAIL, and the Complete Mechanism Chain **Date**: 2026-03-06 **Sub-sessio |
| G2 | S16 | `session-16/session-16-round-1c-computation.md` | 24,394 | Session 16, Round 1c: Computation Coffee | # Session 16, Round 1c: Computation Coffee ## QA-Theorist + Sim-Specialist Joint Assessment ## Date: 2026-02-13 --- ## F |
| G4 | S43 | `session-43/session-43-quicklook-einstein-collab.md` | 24,318 | Einstein Theorist -- Collaborative Feedback on Session 43 | # Einstein Theorist -- Collaborative Feedback on Session 43 **Date**: 2026-03-14 **Basis**: Session 43 quicklook, workin |
| G2 | S16 | `session-16/session-16-orchestration-state.md` | 24,059 | Session 16 Orchestration State | # Session 16 Orchestration State ## Last Updated **Final Synthesis** in progress (2026-02-13 ~late UTC) --- ## Session O |
| G3 | S29 | `session-29/session-29-team-D-synthesis.md` | 24,028 | Team D Synthesis: Particle Physics & CPT | # Team D Synthesis: Particle Physics & CPT **Team**: Dirac, Neutrino, Hawking **Designated Writer**: Dirac **Date**: 202 |
| G4 | S47 | `session-47/session-47-wayforward.md` | 23,896 | Session 47 Way Forward → Session 48 Planning | # Session 47 Way Forward → Session 48 Planning ## Purpose Exhaustive extraction of all recommendations, collaborative su |
| G3 | S26 | `session-26/session-26-priority-1.md` | 23,463 | Session 26 -- Priority 1: Multi-Mode BCS Gap Equation | # Session 26 -- Priority 1: Multi-Mode BCS Gap Equation **Date**: 2026-02-23 **Agent**: phonon-exflation-sim **Data Sour |
| G3 | S29 | `session-29/session-29A-synthesis.md` | 23,397 | Session 29A Synthesis: Constraint Chain Completion + Backreaction | # Session 29A Synthesis: Constraint Chain Completion + Backreaction **Date**: 2026-02-28 **Sub-sessions**: 29Aa (KC-3 cl |
| G5 | S65 | `s65-collab-extraction-for-s66.md` | 23,182 | S65 Extraction for S66 Planning | # S65 Extraction for S66 Planning **Generated**: 2026-04-03 **Sources**: 8 collab reviews, master synthesis, Lizzi synth |
| G5 | S63 | `session-63-wrapup.md` | 22,830 | Session 63 Handoff | # Session 63 Handoff ## 1. Session Metadata - **Date**: 2026-03-30 to 2026-03-31 - **Format**: 7 computation waves (W1-W |
| G2 | S16 | `session-16/session-16-round-1b-spectrum.md` | 22,723 | Session 16, Round 1b: Spectrum Coffee | # Session 16, Round 1b: Spectrum Coffee ## Gen-Physicist + Paasch-Analyst Joint Assessment ## Date: 2026-02-13 --- ## PH |
| G4 | S56 | `session-56-vol-collab.md` | 22,497 | Session 56 Collaborative Review: Volovik Superfluid Universe Theorist | # Session 56 Collaborative Review: Volovik Superfluid Universe Theorist **Date**: 2026-03-22 **Scope**: 20 computations  |
| G3 | S29 | `session-29/session-29Ac-workshop.md` | 22,204 | Session 29Ac Synthesis: Observational Predictions and Scrutiny | # Session 29Ac Synthesis: Observational Predictions and Scrutiny **Date**: 2026-02-28 **Sub-session**: 29Ac (observation |
| G3 | S23 | `session-23/session-23b-synthesis.md` | 21,651 | Session 23b Synthesis: Post-Mortem, Sagan Verdict, and 23c Trigger Decision | # Session 23b Synthesis: Post-Mortem, Sagan Verdict, and 23c Trigger Decision **Date**: 2026-02-20 **Session type**: SYN |
| G4 | S52 | `session-52-qfoam-collab.md` | 21,425 | Quantum-Foam-Theorist -- Collaborative Feedback on Session 52 | # Quantum-Foam-Theorist -- Collaborative Feedback on Session 52 **Date**: 2026-03-20 **Review Lens**: *"We should be pro |
| G4 | S43 | `session-43/session-43-quicklook-quantum-foam-collab.md` | 20,655 | Quantum Foam Theorist -- Collaborative Feedback on Session 43 | # Quantum Foam Theorist -- Collaborative Feedback on Session 43 **Date**: 2026-03-14 **Session**: 43 (Cold Big Bang) **R |
| G3 | S19 | `session-19/session-19d-LeadResearcher-Collab.md` | 20,344 | Tesla-Resonance Assessment: The Lead Researcher's Raw Intuition | # Tesla-Resonance Assessment: The Lead Researcher's Raw Intuition ## Session 19d -- The Inside-Out View ### Date: 2026-0 |
| G3 | S28 | `session-28/session-28-team-synthesis-c.md` | 20,280 | Session 28 Team Synthesis C: Neutrino / Condensed Matter / Mass Quantization | # Session 28 Team Synthesis C: Neutrino / Condensed Matter / Mass Quantization **Date**: 2026-02-27 **Team**: Neutrino ( |
| G3 | S35 | `session-35/session-35-KK-NCG-Excursion.md` | 19,999 | Session 35 Excursion: KK-NCG Bridge Theorem | # Session 35 Excursion: KK-NCG Bridge Theorem **Date**: 2026-03-07 **Format**: Single-agent deep investigation (main age |
| G3 | S29 | `session-29/session-29Ab-synthesis.md` | 19,871 | Session 29Ab Synthesis: Backreaction + Free Energy Comparison | # Session 29Ab Synthesis: Backreaction + Free Energy Comparison **Date**: 2026-02-28 **Sub-session**: 29Ab (backreaction |
| G3 | S28 | `session-28/session-28-team-synthesis-a.md` | 19,682 | Team Synthesis A: Dirac + Feynman + SP | # Team Synthesis A: Dirac + Feynman + SP ## Session 28 Collaborative Review -- 3-Round Deliberation **Participants**: Di |
| G3 | S34 | `session-34/session-34a-synthesis.md` | 19,295 | Session 34a Synthesis: D_phys Fold Survival and Trap 1 Confirmation | # Session 34a Synthesis: D_phys Fold Survival and Trap 1 Confirmation **Date**: 2026-03-06 **Format**: 3-agent team (bap |
| G3 | S19 | `session-19/session-19d-casimir-energy.md` | 19,117 | Session 19d: Casimir Energy vs Coleman-Weinberg -- The IR/UV Stabilization Test | # Session 19d: Casimir Energy vs Coleman-Weinberg -- The IR/UV Stabilization Test ## Date: 2026-02-15 ## Team: phonon-ex |
| G5 | S66 | `session-66-wrapup.md` | 19,116 | Session 66 Wrapup: Spectral Ops. Engagement | # Session 66 Wrapup: Spectral Ops. Engagement **Date**: 2026-04-04 **Session**: 66 **Format**: 8-wave parallel computati |
| G4 | S43 | `session-43/session-43-quicklook-quantum-acoustics-collab.md` | 18,900 | Quantum Acoustics Theorist -- Collaborative Feedback on Session 43 | # Quantum Acoustics Theorist -- Collaborative Feedback on Session 43 **Date**: 2026-03-14 **Session reviewed**: Session  |
| G3 | S30 | `session-30/session-30Bb-synthesis.md` | 18,871 | Session 30Bb Synthesis: Frozen-State Observables at Candidate Points | # Session 30Bb Synthesis: Frozen-State Observables at Candidate Points **Date**: 2026-03-01 **Session type**: COMPUTATIO |
| G3 | S29 | `session-29/session-29ba-synthesis.md` | 18,503 | Session 29Ba Synthesis: 3-Sector Depth + PMNS Extraction | # Session 29Ba Synthesis: 3-Sector Depth + PMNS Extraction **Date**: 2026-02-28 **Session type**: COMPUTATION (3 pre-reg |
| G3 | S19 | `session-19/session-19d-synthesis.md` | 17,708 | Session 19d Synthesis: Casimir Energy vs Coleman-Weinberg | # Session 19d Synthesis: Casimir Energy vs Coleman-Weinberg ## The Twenty-Seven Silent Drums ### Date: 2026-02-15 \| 14 A |
| G3 | S19 | `session-19/session-19d-tesla-quantum-acoustics-collab.md` | 17,628 | Tesla-Resonance: Blind Evaluation of QA Review + Feynman Critique (Session 19d) | # Tesla-Resonance: Blind Evaluation of QA Review + Feynman Critique (Session 19d) ## The Standing Wave Between Two Frame |
| G4 | S50 | `session-50/session-50-oz-investigation-prompts.md` | 17,573 | Session 50: O-Z Investigation — Computation Prompts | # Session 50: O-Z Investigation — Computation Prompts **Purpose**: All prompts dispatched to agents testing the O-Z iden |
| G3 | S19 | `session-19/session-19a-spectral-diagnostics.md` | 17,162 | Session 19a: Spectral Complexity Diagnostics | # Session 19a: Spectral Complexity Diagnostics ## Date: 2026-02-15 ## Team: phonon-exflation-sim (sim), tesla-resonance  |
| G3 | S28 | `session-28/session-28b-results.md` | 17,110 | Session 28b Results: Landau Diagnostics + NCG Axiom Gates | # Session 28b Results: Landau Diagnostics + NCG Axiom Gates **Date**: 2026-02-27 **Computations**: 8 (1 NCG axiom + 5 La |
| G2 | S16 | `session-16/session-16-einstein-feynman-review.md` | 16,738 | Session 16: Einstein-Feynman Joint Closing Review | # Session 16: Einstein-Feynman Joint Closing Review ## Phonon-Exflation Cosmology -- Final Assessment ## Date: 2026-02-1 |
| G3 | S26 | `session-26/session-26-priority-3.md` | 16,114 | Session 26 Priority 3: Higher-Order Seeley-DeWitt (a_6) | # Session 26 Priority 3: Higher-Order Seeley-DeWitt (a_6) ## Date: 2026-02-25 ## Agent: Gen-Physicist (3-phase serial wo |
| G3 | S26 | `session-26/session-26-wrapup.md` | 16,051 | Session 26 Wrap-Up | # Session 26 Wrap-Up **Date**: 2026-02-26 **Assembled by**: Coordinator (from Baptista computation review + Gen-Physicis |
| G4 | S56 | `session-56-string-collab.md` | 15,996 | Session 56 Collaborative Review: String Theory Perspective | # Session 56 Collaborative Review: String Theory Perspective **Agent**: `string-theory-theorist` \| **Model**: opus **Dat |
| G5 | S67 | `session-67-synthesis.md` | 15,956 | Session 67 Synthesis: Exposing Exflation | # Session 67 Synthesis: Exposing Exflation **Date**: 2026-04-04 **Format**: 32 parallel single-agent computations across |
| G3 | S25 | `session-25/session-25-graceful-handoff.md` | 15,776 | Session 25 Graceful Handoff — Collaboration Annotation Sprint | # Session 25 Graceful Handoff — Collaboration Annotation Sprint **Date**: 2026-02-22 **Outgoing Model**: Claude Opus 4.6 |
| G3 | S28 | `session-28/session-28a-results.md` | 15,619 | Session 28a Results: Zero-Cost Diagnostics + Torsionful BCS | # Session 28a Results: Zero-Cost Diagnostics + Torsionful BCS **Date**: 2026-02-27 **Computations**: 7 (6 zero-cost post |
| G3 | S29 | `session-29/session-29Aa-synthesis.md` | 14,876 | Session 29Aa Synthesis: KC-3 Closure + Entropy Balance | # Session 29Aa Synthesis: KC-3 Closure + Entropy Balance **Date**: 2026-02-28 **Sub-session**: 29Aa (gateway sub-session |
| G3 | S28 | `session-28/session-28c-results.md` | 14,691 | Session 28c Results: Constraint Chain Completion + Structural Gates | # Session 28c Results: Constraint Chain Completion + Structural Gates **Date**: 2026-02-27 **Computations**: 8 (5 Constr |
| G2 | S16 | `session-16/session-16-round-1a-geometry.md` | 13,192 | Session 16, Round 1a: Geometry Coffee | # Session 16, Round 1a: Geometry Coffee ## KK-Theorist + Baptista-Analyst Joint Assessment ## Date: 2026-02-13 --- ## 3  |
| G2 | S16 | `session-16/session-16-combined-handout.md` | 13,061 | Session 16 Combined Handout: Everything We Know | # Session 16 Combined Handout: Everything We Know ## Date: 2026-02-13 ## Author: Meme (PI) + Claude (Sessions 15-15.5) # |
| G4 | S37 | `session-37/session-37-handoff.md` | 12,320 | Session 37 Handoff | # Session 37 Handoff ## 1. Session Metadata - **Date**: 2026-03-08 - **Format**: Parallel single-agent computations (com |
| G4 | S54 | `session-54-nazarewicz-connes-workshop-synthesis.md` | 12,302 | Nazarewicz x Connes Workshop Synthesis: Session 54 | # Nazarewicz x Connes Workshop Synthesis: Session 54 ## Nuclear Structure Meets Noncommutative Geometry on the 32-Cell L |
| G3 | S34 | `session-34/session-34-exploration-addendum.md` | 10,959 | Session 34 Framework Exploration Addendum | # Session 34 Framework Exploration Addendum **Date**: 2026-03-06 **Participants**: User (Ryan) + Team-Lead **Context**:  |
| G3 | S19 | `session-19/session-19d-LeadResearcher-Collab (raw).md` | 10,918 |  | ❯ Here is my analogy - not yet shared. Take everything single plank-point in the universe and connect them ALL with rubb |
| G4 | S48 | `session-48/session-48-wayforward.md` | 10,403 | Session 48 Way Forward | # Session 48 Way Forward **Source**: 4 collaborative reviews (Volovik, Einstein, Schwarzschild-Penrose, Nazarewicz, Tesl |
| G4 | S40 | `session-40/session-40-handoff.md` | 10,089 | Session 40 Handoff: Structural Cartography | # Session 40 Handoff: Structural Cartography **Date**: 2026-03-11 **Format**: Parallel single-agent computations, 4 wave |
| G5 | S62 | `session-62-two-wrongs-excursion.md` | 9,953 | Session 62 Excursion: Two Wrongs Make a Right | # Session 62 Excursion: Two Wrongs Make a Right **Date**: 2026-03-29 **Method**: Cross-referencing all closed mechanisms |
| G5 | S71 | `session-71-synthesis.md` | 9,262 | Session 71 Synthesis: Spectral Zeta Threshold + S70 Carry-Forward | # Session 71 Synthesis: Spectral Zeta Threshold + S70 Carry-Forward **Date**: 2026-04-09 **Format**: 4-wave parallel com |
| G4 | S56 | `session-56-workshop-teams.md` | 8,970 | Session 56 Workshop Teams: Four Tribunals | # Session 56 Workshop Teams: Four Tribunals **Date**: 2026-03-22 **Source**: 26 individual collab reviews of S56 results |
| G5 | S61 | `session-61-results.md` | 8,876 | Session 61 Results — Complete | # Session 61 Results — Complete **Date**: 2026-03-28 **Computations**: 91 (Waves 1-6) **Verdicts**: 37 PASS \| 31 INFO \|  |
| G2 | S17 | `session-17/session-17b-verification.md` | 8,760 | Session 17b: Verification Gate -- Geometry Audit + D_K Signoff | # Session 17b: Verification Gate -- Geometry Audit + D_K Signoff ## Date: 2026-02-14 ## Status: COMPLETE (3/3 deliverabl |
| G4 | S45 | `session-45/s45_tinfoil_minus068.md` | 8,613 | Why Does -0.68 Keep Showing Up? | # Why Does -0.68 Keep Showing Up? **Session 45 -- Tesla-Resonance investigation** **Date**: 2026-03-15 --- ## The Data S |
| G3 | S34 | `session-34/session-34-scratchpad.md` | 8,527 | Session 34 Investigation Scratchpad | # Session 34 Investigation Scratchpad **Date**: 2026-03-06 **Focus**: D_phys spectrum, mechanism chain survival, 11% BCS |
| G4 | S53 | `session-53-connes-nazarewicz-workshop-synthesis.md` | 8,305 | Workshop Synthesis: Connes × Nazarewicz — Session 53 | # Workshop Synthesis: Connes × Nazarewicz — Session 53 **Date**: 2026-03-21 **Workshop**: 2 rounds, 4 turns, 653 lines * |
| G4 | S53 | `session-53-baptista-volovik-workshop-synthesis.md` | 8,178 | Workshop Synthesis: Baptista × Volovik — Session 53 | # Workshop Synthesis: Baptista × Volovik — Session 53 **Date**: 2026-03-21 **Workshop**: 2 rounds, 4 turns, 565 lines ** |
| G4 | S41 | `session-41/session-41-pi-directive-complexity-is-geometry.md` | 7,672 | PI Directive: Complexity Is Geometry (And It's Still Happening) | # PI Directive: Complexity Is Geometry (And It's Still Happening) **Date**: 2026-03-12 **Source**: PI insight during Ses |
| G4 | S49 | `session-49/session-49-wayforward.md` | 7,566 | Session 49 Way Forward | # Session 49 Way Forward **Source**: 6 collaborative reviews (Tesla, Volovik, SP, QA, Cosmic-Web, Landau) **Date**: 2026 |
| G4 | S53 | `session-53-phonon-hawking-workshop-synthesis.md` | 7,558 | Workshop Synthesis: Phonon-First × Hawking — Session 53 | # Workshop Synthesis: Phonon-First × Hawking — Session 53 **Date**: 2026-03-21 **Workshop**: 2 rounds, 4 turns, ~539 lin |
| G6 | S79 | `s79-pause-resume.md` | 7,535 | Session 79 — CLOSED 2026-04-16 | # Session 79 — CLOSED 2026-04-16 **SESSION STATUS**: CLOSED. All 13 workshops in the S78-oddities EVOI closure series co |
| G2 | S17 | `session-17/session-17a-foundation.md` | 6,903 | Session 17a: Foundation Layer — Independent Parallel Calculations | # Session 17a: Foundation Layer — Independent Parallel Calculations ## Date: 2026-02-14 ## Status: COMPLETE (7/7 deliver |
| G4 | S41 | `session-41/session-41-pi-narrative-spectral-cosmology.md` | 6,894 | PI Narrative: Spectral Cosmology Sequence | # PI Narrative: Spectral Cosmology Sequence **Date**: 2026-03-12 **Source**: PI directive during Session 41, post-W2 res |
| G6 | S79 | `s79-phase-plan.md` | 6,776 | Session 79 Phase Plan — S78 Oddities Workshop Series | # Session 79 Phase Plan — S78 Oddities Workshop Series **Date**: 2026-04-16 **Trigger**: S78 post-hoc analysis surfaced  |
| G3 | S24 | `session-24/session-24a-synthesis.md` | 6,379 | Session 24a Synthesis: The Computation Sprint — Gate Verdicts | # Session 24a Synthesis: The Computation Sprint — Gate Verdicts **Date**: 2026-02-21 **Session type**: COMPUTATION (7 ch |

…and 6 more orphan entries in the JSON.

## (A) Master-aggregator pattern (47 files) — design-correct

These are aggregator files whose authorship is offloaded to sister files. The session as a whole is attributed; only the roll-up file individually has no per-file author marker. Phase 1 harvester could optionally attribute the aggregator to `orchestrator` as the synthesizer.

| Gen | Session | File | Size | First header |
|:---|:--------|:-----|-----:|:-------------|
| G7 | S83 | `session-83-results-workingpaper.md` | 619,032 | Session 83 Results — Working Paper |
| G6 | S80 | `session-80-results-workingpaper.md` | 307,233 | Session 80 Results — Working Paper |
| G4 | S55 | `session-55-results-workingpaper.md` | 151,569 | Session 55 Results Working Paper: Stable State — Three Candidates, One Lattice |
| G4 | S57 | `session-57-results-workingpaper.md` | 150,289 | Session 57 Results: The Shattering |
| G4 | S54 | `session-54-results-workingpaper.md` | 137,066 | Session 54 Results Working Paper |
| G5 | S61 | `session-61-wave5-workingpaper.md` | 133,807 | Session 61 — Wave 5: Extensions + Dependent + Speculative |
| G4 | S56 | `session-56-results-workingpaper.md` | 114,730 | Session 56 Results Working Paper: Z Warriors Assemble -- The Fabric Partition Function |
| G5 | S62 | `session-62-results-workingpaper.md` | 109,636 | Session 62 Results — Working Paper |
| G4 | S50 | `session-50/session-50-results-workingpaper.md` | 99,172 | Session 50 Results Working Paper |
| G4 | S40 | `session-40/session-40-results-workingpaper.md` | 94,445 | Session 40 Results Working Paper: Structural Cartography |
| G4 | S52 | `session-52-results-workingpaper.md` | 83,060 | Session 52: The 12D Reduction — Results Working Paper |
| G5 | S61 | `session-61-wave3-workingpaper.md` | 71,119 | Session 61 — Wave 3: Alpha + Transit + CC + Zeta-Dependent |
| G5 | S61 | `session-61-wave4-workingpaper.md` | 69,278 | Session 61 — Wave 4: Signatures + Deep Theory |
| G5 | S61 | `session-61-wave6-workshop.md` | 63,215 | Session 61 — Wave 6: Lost Treasures Evaluation |
| G4 | S39 | `session-39/session-39-master-synthesis.md` | 63,150 | Session 39 Master Synthesis: Subquantum |
| G3 | S34 | `session-34/session-34-master-synthesis.md` | 57,182 | Session 34 Master Synthesis |
| G4 | S51 | `session-51/session-51-results-workingpaper.md` | 56,723 | Session 51 Results Working Paper |
| G4 | S41 | `session-41/session-41-results-workingpaper.md` | 54,073 | Session 41 Results Working Paper: Spectral Refinement and the Constants |
| G4 | S37 | `session-37/session-37-results-workingpaper.md` | 42,826 | Session 37 Results Working Paper |
| G3 | S21 | `session-21/session-21c-master-collab.md` | 42,099 | Master Collaborative Synthesis: Session 21c |
| G4 | S44 | `session-44/session-44-quicklook-master-collab.md` | 41,360 | Master Collaborative Synthesis: Session 44 (FINAL -- includes W5-5 correction + addenda) |
| G5 | S66 | `session-66-master-collab.md` | 41,034 | Master Collaborative Synthesis: Session 66 — Spectral Ops. Engagement |
| G5 | S72 | `session-72-audit-master-synthesis.md` | 39,735 | Session 72 Master Audit Synthesis |
| G4 | S52 | `session-52-master-collab.md` | 36,946 | Master Collaborative Synthesis: Session 52 |
| G3 | S22 | `session-22/session-22-master-collab.md` | 34,955 | Master Collaborative Synthesis: Session 22 |
| G3 | S21 | `session-21/session-21c-r2-master-collab.md` | 34,310 | Master Collaborative Synthesis: Session 21c Round 2 |
| G3 | S23 | `session-23/session-23-tesla-take-master-collab.md` | 32,549 | Master Collaborative Synthesis: Session 23 Tesla Take |
| G5 | S65 | `session-65-master-collab.md` | 31,486 | Master Collaborative Synthesis: Session 65 |
| G5 | S68 | `session-68-master-collab.md` | 31,417 | Master Collaborative Synthesis: S68 Workshops |
| G4 | S42 | `session-42/session-42-master-collab.md` | 31,065 | Master Collaborative Synthesis: Session 42 |
| G4 | S38 | `session-38/session-38-master-synthesis.md` | 28,664 | Session 38 Master Synthesis: The Ordered Veil |
| G4 | S60 | `session-60-master-collab.md` | 28,422 | Master Collaborative Synthesis: Session 60 |
| G4 | S55 | `session-55-framework-update-master-collab.md` | 25,640 | Master Collaborative Synthesis: Session 55 Framework Update |
| G3 | S20 | `session-20/session-20b-master-collab.md` | 25,554 | Master Collaborative Synthesis: Session 20b -- Lichnerowicz TT 2-Tensor CLOSED |
| G4 | S38 | `session-38/session-38-master-collab.md` | 25,101 | Master Collaborative Review: Session 38 — The Ordered Veil |
| G5 | S69 | `session-69-master-collab.md` | 24,219 | Master Collaborative Synthesis: Session 69 |
| G4 | S41 | `session-41/session-41-master-synthesis.md` | 23,907 | Session 41 Master Synthesis: The Fabric Discovery |
| G4 | S54 | `session-54-master-collab.md` | 23,823 | Master Collaborative Synthesis: Session 54 |
| G3 | S33 | `session-33/session-33-master-collab.md` | 22,538 | Master Collaborative Synthesis: Session 33 |
| G4 | S40 | `session-40/session-40-master-collab.md` | 20,946 | Master Collaborative Synthesis: Session 40 |
| G4 | S57 | `session-57-master-collab.md` | 20,930 | Master Collaborative Synthesis: Session 57 — The Shattering |
| G4 | S53 | `session-53-master-collab.md` | 18,805 | Master Collaborative Synthesis: Session 53 — Phonon In The Road |
| G4 | S50 | `session-50/session-50-master-collab.md` | 16,764 | Master Collaborative Synthesis: Session 50 |
| G3 | S19 | `session-19/session-19d-master-collab.md` | 16,532 | Master Collaborative Synthesis: Session 19d |
| G6 | S81 | `session-81-results-workingpaper.md` | 16,095 | Session 81 — computation Provenance Graph + PRU Audit Closure |
| G3 | S27 | `session-27/session-27-master-collab.md` | 11,572 | Master Collaborative Synthesis: Session 27 |
| G5 | S61 | `session-61-wave10-workingpaper.md` | 2,546 | Session 61 — Wave 10: Framework Document Updates |

## SYSTEM-FILE (57 files) — expected zero attribution

| Kind | Count | Examples |
|:-----|------:|:---------|
| workshop-seed | 37 | _seed-1.md, _seed-2.md |
| workshop-schedule | 10 | session-82-workshop-schedule.md, session-83-workshop-schedule.md |
| results-index | 3 | session-86-results-index.md, session-89-results-index.md |
| OOM-summary | 2 | session-75-OOM.md, session-82-OOM.md |
| evoi-framework | 1 | evoi-framework.md |
| other-system | 1 | c1_GR_proposal.md |
| compute-carryforward | 1 | compute-carryforward.md |
| carry-forward | 1 | session-86-path-b-carry-forward.md |
| pending-edits-ledger | 1 | s88-pending-edits-ledger.md |

## DATA-ONLY (1 files) — short / table-heavy / data stubs

These are largely tables or short stubs. Listed for completeness.

| Session | File | Size |
|:--------|:-----|-----:|
| S78 | `s78_phase_slip_pre_registration.md` | 1,070 |
