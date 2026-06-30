---
type: orphan-watchlist
ingested-by: /weave --update
---

# Orphan-content watchlist

**Registry ID**: `orphan-content-watchlist`  
**Owner agent(s)**: `orchestrator` (sole writer)  
**Last updated**: 2026-05-17, Phase 1.1 / orphan-chain investigation  
**Source**: `tools/_format_generation_zero_coverage.json` (generator: `tools/_format_generation_zero_coverage.py`)  
**Chain data source**: `tools/_orphan_chain_analysis.json` (generator: `tools/_orphan_chain_investigator.py`)  
**Per-orphan detail**: `sessions/framework/registry/orphan-chain-analysis.md`

---

## Scope

This registry lists session markdown files that emitted ZERO attribution edges in the Phase 1 harvester run (`tools/harvest_attribution_edges.py`). The Phase 1.1 investigation (`tools/_orphan_chain_investigator.py`) ran against all 156 orphans and produced:

- **Archetype classification** for each file (synthesis, handoff, way-forward, workshop, etc. — 33 distinct archetypes)
- **Author extraction** via extended regex set covering patterns the production harvester misses (H2 `## Author:` lines, `**Team**:` / `**Synthesist**:` / `**Designated Writer**:` / `[E]S-1` bracket-tag forms, bullet-prefixed `- **Agents**:` em-dash lists)
- **Upstream chain refs** via `**Source**:` / `**Reviewing**:` / `**Predecessor**:` / `**Extracted from**:` / `**Source files**:` / `**Reference corpus**:` patterns
- **Downstream consumers** via corpus-wide inbound-link index (6,467 unique basenames scanned across `sessions/`, `computations/`, `tools/`, `summary/`)
- **Recommended edges** per the canonical `EDGE_TYPE_CANONICAL` vocabulary (all 839 recommended edges resolve to whitelist-approved types)

---

## How to use this list

Each row carries the investigator's status recommendation. The five terminal states are:

- `UNREVIEWED` (legacy default before chain investigation)
- `REGEX-FIXED` (attribution extracted — patterns to add to Phase 1 harvester for promotion)
- `MULTI-AUTHOR` (synthesis-archetype with implicit or extracted multi-author attribution — emit `synthesized_by` + per-author `participates_in` edges)
- `ORPHAN-PROMOTED` (no author extracted, but the file has upstream/downstream chain — emit `derived_from` / `cited_in` edges; surface to next-session planner if content is substantively novel)
- `HISTORICAL-ONLY` (no authors, no chain, low-value — leave in archive)

Per-orphan detail blocks (extracted authors, upstream refs, downstream consumers, recommended edges) live in `sessions/framework/registry/orphan-chain-analysis.md`.

---

## Distribution

**By recommended status**:
- `REGEX-FIXED`: 43 files
- `MULTI-AUTHOR`: 60 files
- `ORPHAN-PROMOTED`: 52 files
- `HISTORICAL-ONLY`: 1 files

**By archetype** (top 15):
- `synthesis`: 28
- `round_discussion`: 14
- `solo_collab_review`: 13
- `handoff`: 9
- `team_synthesis`: 9
- `wave_subdocument`: 9
- `workshop`: 6
- `synergy_index`: 5
- `wayforward`: 5
- `extraction`: 5
- `results_summary`: 4
- `quicklook`: 4
- `slot_anchored_solo`: 4
- `excursion`: 3
- `addendum`: 3

---

## (B) Orphan-content candidates (156 files)

Sorted by size (largest first).

| # | Status | Gen | Sess | Archetype | File | Size | Chain summary |
|--:|:-------|:----|:-----|:----------|:-----|-----:|:--------------|
| 1 | ORPHAN-PROMOTED | G7 | S84 | wave_subdocument | `session-84-w10-workingpaper.md` | 172,920 | dn=13 edges=13 |
| 2 | MULTI-AUTHOR | G4 | S60 | wayforward | `session-60-wayforward.md` | 168,290 | up=53 dn=7 edges=101 |
| 3 | MULTI-AUTHOR | G3 | S25 | synergy_index | `session-25/session-25-Investigation-Collaborate-Efforts.md` | 161,045 | auth=22 dn=3 edges=25 |
| 4 | ORPHAN-PROMOTED | G7 | S84 | wave_subdocument | `session-84-w2-workingpaper.md` | 154,137 | dn=5 edges=5 |
| 5 | ORPHAN-PROMOTED | G7 | S84 | wave_subdocument | `session-84-w4-workingpaper.md` | 152,321 | dn=7 edges=7 |
| 6 | ORPHAN-PROMOTED | G7 | S84 | wave_subdocument | `session-84-w7-workingpaper.md` | 146,712 | dn=7 edges=7 |
| 7 | MULTI-AUTHOR | G3 | S25 | synergy_index | `session-25/session-25-Investigation-Question-Efforts.md` | 136,476 | auth=2 dn=1 edges=3 |
| 8 | REGEX-FIXED | G7 | S87 | workshop | `workshops/s87-cf29-substantive-reading-carve-out.md` | 115,452 | auth=2 up=6 dn=2 edges=17 |
| 9 | ORPHAN-PROMOTED | G7 | S86 | workingpaper | `session-86-w0c-workingpaper.md` | 115,375 | dn=5 edges=5 |
| 10 | ORPHAN-PROMOTED | G4 | S52 | workshop | `session-52-phonon-workshop.md` | 109,880 | dn=1 edges=1 |
| 11 | ORPHAN-PROMOTED | G7 | S84 | wave_subdocument | `session-84-w3-workingpaper.md` | 106,906 | dn=6 edges=6 |
| 12 | ORPHAN-PROMOTED | G7 | S84 | wave_subdocument | `session-84-w6-workingpaper.md` | 104,923 | dn=10 edges=10 |
| 13 | REGEX-FIXED | G5 | S74 | pre_registration | `session-74-tgf-pre-registration.md` | 101,661 | auth=1 dn=1 edges=2 |
| 14 | MULTI-AUTHOR | G3 | S25 | synergy_index | `session-25/session-25-Investigation-Assessment-Efforts.md` | 98,960 | dn=2 edges=2 |
| 15 | REGEX-FIXED | G7 | S87 | workshop | `workshops/s87-a0-r-protection-m2-biconditional.md` | 87,016 | auth=2 up=8 dn=3 edges=16 |
| 16 | REGEX-FIXED | G3 | S19 | session_primer | `session-19/session-19-primer.md` | 63,600 | auth=2 up=1 dn=6 edges=10 |
| 17 | ORPHAN-PROMOTED | G5 | S74 | retrospective_analysis | `session-74-rf-analysis.md` | 59,396 | dn=5 edges=5 |
| 18 | MULTI-AUTHOR | G3 | S27 | handoff | `session-27/session-27-wrapup.md` | 58,682 | dn=3 edges=3 |
| 19 | ORPHAN-PROMOTED | G7 | S91 | plan | `DIA-investigation-schedule.md` | 57,946 | dn=1 edges=1 |
| 20 | REGEX-FIXED | G4 | S44 | solo_collab_review | `session-44/session-44-quicklook-sp-collab.md` | 57,935 | auth=1 up=2 dn=1 edges=5 |
| 21 | MULTI-AUTHOR | G3 | S21 | synthesis | `session-21/session-21c-phase0-synthesis.md` | 51,570 | auth=1 up=1 dn=4 edges=6 |
| 22 | REGEX-FIXED | G4 | S44 | solo_collab_review | `session-44/session-44-quicklook-connes-collab.md` | 50,941 | auth=1 up=1 dn=1 edges=3 |
| 23 | REGEX-FIXED | G7 | S85 | uncategorized | `session-85-4a-elimination-bulletins-kaku.md` | 49,098 | auth=1 up=1 dn=1 edges=4 |
| 24 | MULTI-AUTHOR | G3 | S21 | synthesis | `session-21/session-21a-ainur-synthesis.md` | 48,451 | auth=7 dn=2 edges=9 |
| 25 | ORPHAN-PROMOTED | G4 | S54 | extraction | `session-54-extraction-collabs.md` | 48,372 | up=78 dn=1 edges=89 |
| 26 | ORPHAN-PROMOTED | G7 | S88 | workshop | `workshops/s88-w3-w1b1-63-3branch.md` | 46,086 | up=1 dn=3 edges=5 |
| 27 | MULTI-AUTHOR | G3 | S25 | synergy_index | `session-25/session-25-Investigation-Closing.md` | 45,855 | dn=1 edges=1 |
| 28 | ORPHAN-PROMOTED | G4 | S43 | quicklook | `session-43/session-43-quicklook.md` | 45,059 | up=1 dn=2 edges=3 |
| 29 | REGEX-FIXED | G7 | S88 | workshop | `workshops/s88-mack-arxiv-2511-07517-desi-review.md` | 44,519 | auth=1 dn=3 edges=4 |
| 30 | MULTI-AUTHOR | G5 | S61 | midsession_review | `session-61-midsession-review.md` | 44,495 | auth=1 up=1 dn=2 edges=4 |
| 31 | MULTI-AUTHOR | G3 | S20 | synthesis | `session-20/session-20c-synthesis.md` | 42,761 | auth=7 dn=4 edges=11 |
| 32 | REGEX-FIXED | G2 | S16 | round_discussion | `session-16/session-16-round-3b-theoretical.md` | 42,755 | auth=3 dn=3 edges=6 |
| 33 | ORPHAN-PROMOTED | G3 | S33 | wave_subdocument | `session-33/session-33-w1-math-permanence.md` | 42,111 | up=1 dn=6 edges=8 |
| 34 | ORPHAN-PROMOTED | G2 | S16 | round_discussion | `session-16/session-16-round-3a-computational.md` | 41,987 | dn=4 edges=4 |
| 35 | REGEX-FIXED | G7 | S85 | slot_anchored_solo | `session-85-s1-regulator-boundary-van-den-dungen.md` | 41,537 | auth=1 dn=3 edges=4 |
| 36 | ORPHAN-PROMOTED | G2 | S16 | round_discussion | `session-16/session-16-round-3c-priorities.md` | 39,467 | dn=3 edges=3 |
| 37 | REGEX-FIXED | G4 | S44 | single_agent_audit | `session-44/s44_sagan_assessment.md` | 39,415 | auth=1 up=1 dn=3 edges=5 |
| 38 | REGEX-FIXED | G2 | S16 | round_discussion | `session-16/session-16-round-2d-giants-eval-ii.md` | 38,865 | auth=1 dn=2 edges=3 |
| 39 | ORPHAN-PROMOTED | G4 | S45 | quicklook | `session-45/session-45-quicklook.md` | 38,763 | up=1 dn=1 edges=2 |
| 40 | MULTI-AUTHOR | G3 | S28 | fusion_synthesis | `session-28/session-28-fusion-synthesis.md` | 38,317 | auth=5 dn=10 edges=15 |
| 41 | REGEX-FIXED | G7 | S85 | slot_anchored_solo | `session-85-s3-alphas-registry-mack.md` | 38,067 | auth=1 dn=1 edges=2 |
| 42 | REGEX-FIXED | G2 | S16 | round_discussion | `session-16/session-16-round-2a-veff.md` | 37,891 | auth=2 dn=3 edges=5 |
| 43 | MULTI-AUTHOR | G7 | S90 | synthesis | `session-90-connes-s5-pin-derivative-synthesis.md` | 35,586 | auth=1 dn=3 edges=4 |
| 44 | ORPHAN-PROMOTED | G7 | S88 | wave_subdocument | `workshops/s88-w1-substrate-clock-cancellation.md` | 34,389 | dn=3 edges=3 |
| 45 | ORPHAN-PROMOTED | G2 | S16 | round_discussion | `session-16/session-16-round-2b-dk-generations.md` | 34,062 | dn=6 edges=6 |
| 46 | MULTI-AUTHOR | G4 | S52 | wayforward | `session-52-way-forward.md` | 33,789 | dn=2 edges=2 |
| 47 | MULTI-AUTHOR | G4 | S60 | synthesis | `session-60-synthesis.md` | 33,450 | auth=1 up=1 dn=3 edges=5 |
| 48 | ORPHAN-PROMOTED | G4 | S54 | extraction | `session-54-extraction-workshops.md` | 33,161 | up=49 dn=1 edges=91 |
| 49 | REGEX-FIXED | G7 | S85 | slot_anchored_solo | `session-85-s2-k-corridor-landau.md` | 32,657 | auth=1 dn=1 edges=2 |
| 50 | REGEX-FIXED | G2 | S16 | round_discussion | `session-16/session-16-round-1e-hawking-sagan.md` | 32,423 | auth=2 dn=3 edges=5 |
| 51 | REGEX-FIXED | G4 | S44 | solo_collab_review | `session-44/session-44-quicklook-nazarewicz-collab.md` | 31,846 | auth=1 up=1 dn=1 edges=3 |
| 52 | REGEX-FIXED | G7 | S85 | slot_anchored_solo | `session-85-s1-regulator-boundary-connes.md` | 31,670 | auth=1 dn=2 edges=3 |
| 53 | MULTI-AUTHOR | G3 | S33 | synthesis | `session-33/session-33a-synthesis.md` | 31,485 | auth=2 up=5 dn=7 edges=18 |
| 54 | ORPHAN-PROMOTED | G2 | S16 | round_discussion | `session-16/session-16-round-2c-theory.md` | 31,165 | dn=4 edges=4 |
| 55 | REGEX-FIXED | G2 | S16 | round_discussion | `session-16/session-16-round-2d-giants-eval.md` | 31,068 | auth=1 dn=3 edges=4 |
| 56 | ORPHAN-PROMOTED | G7 | S88 | wave_subdocument | `workshops/s88-w2-kz-universality-class.md` | 31,065 | up=1 dn=3 edges=4 |
| 57 | REGEX-FIXED | G3 | S29 | excursion | `session-29/session-29-observational-excursion.md` | 30,815 | auth=4 dn=1 edges=5 |
| 58 | MULTI-AUTHOR | G3 | S25 | synergy_index | `session-25/session-25-Investigation-Framework.md` | 30,674 | dn=1 edges=1 |
| 59 | MULTI-AUTHOR | G3 | S29 | team_synthesis | `session-29/session-29-team-A-synthesis.md` | 30,520 | auth=5 dn=1 edges=6 |
| 60 | MULTI-AUTHOR | G3 | S29 | team_synthesis | `session-29/session-29-team-E-synthesis.md` | 30,396 | auth=2 dn=1 edges=3 |
| 61 | REGEX-FIXED | G5 | S72 | audit | `session-72-audit-gen-physicist.md` | 30,250 | auth=1 dn=1 edges=2 |
| 62 | ORPHAN-PROMOTED | G5 | S64 | extraction | `s64-collab-extraction.md` | 29,951 | dn=2 edges=2 |
| 63 | MULTI-AUTHOR | G4 | S54 | synthesis | `session-54-qa-hawking-workshop-synthesis.md` | 29,931 | auth=2 up=1 dn=1 edges=4 |
| 64 | MULTI-AUTHOR | G6 | S79 | handoff | `session-79-final.md` | 29,797 | dn=6 edges=6 |
| 65 | ORPHAN-PROMOTED | G4 | S44 | quicklook | `session-44/session-44-quicklook.md` | 29,779 | up=1 dn=2 edges=3 |
| 66 | MULTI-AUTHOR | G3 | S29 | fusion_synthesis | `session-29/session-29-fusion-synthesis.md` | 29,478 | dn=9 edges=9 |
| 67 | REGEX-FIXED | G2 | S16 | round_discussion | `session-16/session-16-round-2a-hawking-thermodynamics.md` | 29,317 | auth=1 dn=3 edges=4 |
| 68 | MULTI-AUTHOR | G3 | S29 | handoff | `session-29/session-29-wrapup.md` | 29,155 | dn=3 edges=3 |
| 69 | REGEX-FIXED | G4 | S44 | solo_collab_review | `session-44/session-44-quicklook-einstein-collab.md` | 28,788 | auth=1 up=1 dn=1 edges=3 |
| 70 | MULTI-AUTHOR | G3 | S28 | team_synthesis | `session-28/session-28-team-synthesis-b.md` | 28,341 | auth=4 dn=3 edges=7 |
| 71 | ORPHAN-PROMOTED | G5 | S64 | extraction | `s64-synthesis-extraction.md` | 28,221 | up=2 dn=2 edges=5 |
| 72 | ORPHAN-PROMOTED | G5 | S68 | plan | `session-68-phonon-vs-data-plan.md` | 28,084 | dn=3 edges=3 |
| 73 | REGEX-FIXED | G4 | S43 | solo_collab_review | `session-43/session-43-quicklook-hawking-collab.md` | 27,754 | auth=1 dn=1 edges=2 |
| 74 | MULTI-AUTHOR | G3 | S29 | team_synthesis | `session-29/session-29-team-B-synthesis.md` | 27,318 | auth=4 dn=1 edges=5 |
| 75 | MULTI-AUTHOR | G3 | S29 | team_synthesis | `session-29/session-29-team-C-synthesis.md` | 26,639 | auth=4 dn=1 edges=5 |
| 76 | MULTI-AUTHOR | G4 | S54 | synthesis | `session-54-master-workshop-synthesis.md` | 26,481 | dn=1 edges=1 |
| 77 | MULTI-AUTHOR | G3 | S28 | team_synthesis | `session-28/session-28-team-synthesis-d.md` | 26,288 | auth=5 dn=1 edges=6 |
| 78 | REGEX-FIXED | G4 | S46 | solo_collab_review | `session-46/session-46-quicklook-dirac-collab.md` | 25,983 | auth=1 dn=1 edges=2 |
| 79 | MULTI-AUTHOR | G3 | S24 | synthesis | `session-24/session-24b-synthesis.md` | 25,773 | auth=3 up=1 dn=5 edges=11 |
| 80 | MULTI-AUTHOR | G3 | S29 | synthesis | `session-29/session-29Ac-synthesis.md` | 25,623 | auth=4 dn=3 edges=7 |
| 81 | REGEX-FIXED | G2 | S16 | round_discussion | `session-16/session-16-round-1d-einstein-feynman.md` | 25,491 | auth=2 dn=3 edges=5 |
| 82 | MULTI-AUTHOR | G4 | S54 | synthesis | `session-54-phonon-landau-workshop-synthesis.md` | 25,392 | auth=2 up=1 dn=1 edges=6 |
| 83 | ORPHAN-PROMOTED | G4 | S46 | quicklook | `session-46/session-46-quicklook.md` | 25,339 | up=1 dn=6 edges=7 |
| 84 | MULTI-AUTHOR | G3 | S29 | synthesis | `session-29/session-29Bb-synthesis.md` | 24,567 | auth=3 dn=5 edges=8 |
| 85 | MULTI-AUTHOR | G3 | S33 | synthesis | `session-33/session-33b-synthesis.md` | 24,404 | auth=1 dn=5 edges=6 |
| 86 | ORPHAN-PROMOTED | G2 | S16 | round_discussion | `session-16/session-16-round-1c-computation.md` | 24,394 | dn=3 edges=3 |
| 87 | REGEX-FIXED | G4 | S43 | solo_collab_review | `session-43/session-43-quicklook-einstein-collab.md` | 24,318 | auth=1 up=1 dn=1 edges=4 |
| 88 | REGEX-FIXED | G2 | S16 | orchestration_state | `session-16/session-16-orchestration-state.md` | 24,059 | auth=7 dn=1 edges=8 |
| 89 | MULTI-AUTHOR | G3 | S29 | team_synthesis | `session-29/session-29-team-D-synthesis.md` | 24,028 | auth=4 dn=1 edges=5 |
| 90 | MULTI-AUTHOR | G4 | S47 | wayforward | `session-47/session-47-wayforward.md` | 23,896 | auth=6 up=5 dn=1 edges=13 |
| 91 | REGEX-FIXED | G3 | S26 | priority_computation | `session-26/session-26-priority-1.md` | 23,463 | auth=2 dn=2 edges=4 |
| 92 | MULTI-AUTHOR | G3 | S29 | synthesis | `session-29/session-29A-synthesis.md` | 23,397 | up=1 dn=3 edges=4 |
| 93 | ORPHAN-PROMOTED | G5 | S65 | extraction | `s65-collab-extraction-for-s66.md` | 23,182 | up=1 dn=3 edges=4 |
| 94 | MULTI-AUTHOR | G5 | S63 | handoff | `session-63-wrapup.md` | 22,830 | dn=2 edges=2 |
| 95 | ORPHAN-PROMOTED | G2 | S16 | round_discussion | `session-16/session-16-round-1b-spectrum.md` | 22,723 | dn=3 edges=3 |
| 96 | ORPHAN-PROMOTED | G4 | S56 | solo_collab_review | `session-56-vol-collab.md` | 22,497 | dn=3 edges=3 |
| 97 | REGEX-FIXED | G3 | S29 | workshop | `session-29/session-29Ac-workshop.md` | 22,204 | auth=5 dn=3 edges=8 |
| 98 | MULTI-AUTHOR | G3 | S23 | synthesis | `session-23/session-23b-synthesis.md` | 21,651 | auth=2 up=1 dn=10 edges=14 |
| 99 | REGEX-FIXED | G4 | S52 | solo_collab_review | `session-52-qfoam-collab.md` | 21,425 | auth=1 dn=3 edges=4 |
| 100 | REGEX-FIXED | G4 | S43 | solo_collab_review | `session-43/session-43-quicklook-quantum-foam-collab.md` | 20,655 | auth=1 dn=1 edges=2 |
| 101 | ORPHAN-PROMOTED | G3 | S19 | lead_researcher_collab | `session-19/session-19d-LeadResearcher-Collab.md` | 20,344 | dn=1 edges=1 |
| 102 | MULTI-AUTHOR | G3 | S28 | team_synthesis | `session-28/session-28-team-synthesis-c.md` | 20,280 | auth=4 dn=1 edges=5 |
| 103 | REGEX-FIXED | G3 | S35 | excursion | `session-35/session-35-KK-NCG-Excursion.md` | 19,999 | auth=1 dn=2 edges=3 |
| 104 | MULTI-AUTHOR | G3 | S29 | synthesis | `session-29/session-29Ab-synthesis.md` | 19,871 | auth=4 up=2 dn=5 edges=11 |
| 105 | MULTI-AUTHOR | G3 | S28 | team_synthesis | `session-28/session-28-team-synthesis-a.md` | 19,682 | auth=4 dn=3 edges=7 |
| 106 | MULTI-AUTHOR | G3 | S34 | synthesis | `session-34/session-34a-synthesis.md` | 19,295 | dn=7 edges=7 |
| 107 | ORPHAN-PROMOTED | G3 | S19 | sub_session_compute | `session-19/session-19d-casimir-energy.md` | 19,117 | dn=8 edges=8 |
| 108 | MULTI-AUTHOR | G5 | S66 | handoff | `session-66-wrapup.md` | 19,116 | dn=2 edges=2 |
| 109 | REGEX-FIXED | G4 | S43 | solo_collab_review | `session-43/session-43-quicklook-quantum-acoustics-collab.md` | 18,900 | auth=1 up=1 dn=1 edges=3 |
| 110 | MULTI-AUTHOR | G3 | S30 | synthesis | `session-30/session-30Bb-synthesis.md` | 18,871 | auth=2 up=1 dn=2 edges=5 |
| 111 | MULTI-AUTHOR | G3 | S29 | synthesis | `session-29/session-29ba-synthesis.md` | 18,503 | auth=2 dn=5 edges=7 |
| 112 | MULTI-AUTHOR | G3 | S19 | synthesis | `session-19/session-19d-synthesis.md` | 17,708 | dn=4 edges=4 |
| 113 | REGEX-FIXED | G3 | S19 | solo_collab_review | `session-19/session-19d-tesla-quantum-acoustics-collab.md` | 17,628 | auth=2 dn=1 edges=3 |
| 114 | ORPHAN-PROMOTED | G4 | S50 | investigation_prompts | `session-50/session-50-oz-investigation-prompts.md` | 17,573 | dn=2 edges=2 |
| 115 | ORPHAN-PROMOTED | G3 | S19 | sub_session_compute | `session-19/session-19a-spectral-diagnostics.md` | 17,162 | dn=2 edges=2 |
| 116 | ORPHAN-PROMOTED | G3 | S28 | results_summary | `session-28/session-28b-results.md` | 17,110 | dn=1 edges=1 |
| 117 | REGEX-FIXED | G2 | S16 | review | `session-16/session-16-einstein-feynman-review.md` | 16,738 | auth=2 dn=4 edges=6 |
| 118 | ORPHAN-PROMOTED | G3 | S26 | priority_computation | `session-26/session-26-priority-3.md` | 16,114 | dn=1 edges=1 |
| 119 | MULTI-AUTHOR | G3 | S26 | handoff | `session-26/session-26-wrapup.md` | 16,051 | dn=1 edges=1 |
| 120 | REGEX-FIXED | G4 | S56 | solo_collab_review | `session-56-string-collab.md` | 15,996 | auth=1 up=1 dn=3 edges=5 |
| 121 | MULTI-AUTHOR | G5 | S67 | synthesis | `session-67-synthesis.md` | 15,956 | dn=4 edges=4 |
| 122 | MULTI-AUTHOR | G3 | S25 | handoff | `session-25/session-25-graceful-handoff.md` | 15,776 | dn=1 edges=1 |
| 123 | ORPHAN-PROMOTED | G3 | S28 | results_summary | `session-28/session-28a-results.md` | 15,619 | dn=1 edges=1 |
| 124 | MULTI-AUTHOR | G3 | S29 | synthesis | `session-29/session-29Aa-synthesis.md` | 14,876 | auth=3 dn=6 edges=9 |
| 125 | ORPHAN-PROMOTED | G3 | S28 | results_summary | `session-28/session-28c-results.md` | 14,691 | dn=4 edges=4 |
| 126 | ORPHAN-PROMOTED | G2 | S16 | round_discussion | `session-16/session-16-round-1a-geometry.md` | 13,192 | dn=4 edges=4 |
| 127 | MULTI-AUTHOR | G2 | S16 | combined_handout | `session-16/session-16-combined-handout.md` | 13,061 | auth=2 dn=1 edges=3 |
| 128 | MULTI-AUTHOR | G4 | S37 | handoff | `session-37/session-37-handoff.md` | 12,320 | auth=6 dn=2 edges=8 |
| 129 | MULTI-AUTHOR | G4 | S54 | synthesis | `session-54-nazarewicz-connes-workshop-synthesis.md` | 12,302 | auth=2 up=1 dn=1 edges=4 |
| 130 | REGEX-FIXED | G3 | S34 | addendum | `session-34/session-34-exploration-addendum.md` | 10,959 | auth=2 dn=4 edges=6 |
| 131 | HISTORICAL-ONLY | G3 | S19 | lead_researcher_collab | `session-19/session-19d-LeadResearcher-Collab (raw).md` | 10,918 | edges=0 |
| 132 | MULTI-AUTHOR | G4 | S48 | wayforward | `session-48/session-48-wayforward.md` | 10,403 | dn=1 edges=1 |
| 133 | MULTI-AUTHOR | G4 | S40 | handoff | `session-40/session-40-handoff.md` | 10,089 | auth=1 up=1 dn=4 edges=6 |
| 134 | ORPHAN-PROMOTED | G5 | S62 | excursion | `session-62-two-wrongs-excursion.md` | 9,953 | dn=2 edges=2 |
| 135 | MULTI-AUTHOR | G5 | S71 | synthesis | `session-71-synthesis.md` | 9,262 | dn=2 edges=2 |
| 136 | ORPHAN-PROMOTED | G4 | S56 | workshop_teams | `session-56-workshop-teams.md` | 8,970 | up=1 dn=1 edges=2 |
| 137 | ORPHAN-PROMOTED | G5 | S61 | results_summary | `session-61-results.md` | 8,876 | dn=5 edges=5 |
| 138 | ORPHAN-PROMOTED | G2 | S17 | phase_layer | `session-17/session-17b-verification.md` | 8,760 | dn=1 edges=1 |
| 139 | ORPHAN-PROMOTED | G4 | S45 | tinfoil_investigation | `session-45/s45_tinfoil_minus068.md` | 8,613 | dn=2 edges=2 |
| 140 | ORPHAN-PROMOTED | G3 | S34 | scratchpad | `session-34/session-34-scratchpad.md` | 8,527 | dn=4 edges=4 |
| 141 | MULTI-AUTHOR | G4 | S53 | synthesis | `session-53-connes-nazarewicz-workshop-synthesis.md` | 8,305 | auth=3 dn=2 edges=5 |
| 142 | MULTI-AUTHOR | G4 | S53 | synthesis | `session-53-baptista-volovik-workshop-synthesis.md` | 8,178 | auth=3 dn=3 edges=6 |
| 143 | REGEX-FIXED | G4 | S41 | pi_artifact | `session-41/session-41-pi-directive-complexity-is-geometry.md` | 7,672 | auth=1 up=1 dn=1 edges=4 |
| 144 | MULTI-AUTHOR | G4 | S49 | wayforward | `session-49/session-49-wayforward.md` | 7,566 | dn=2 edges=2 |
| 145 | MULTI-AUTHOR | G4 | S53 | synthesis | `session-53-phonon-hawking-workshop-synthesis.md` | 7,558 | auth=2 dn=1 edges=3 |
| 146 | ORPHAN-PROMOTED | G6 | S79 | pause_resume | `s79-pause-resume.md` | 7,535 | dn=5 edges=5 |
| 147 | ORPHAN-PROMOTED | G2 | S17 | phase_layer | `session-17/session-17a-foundation.md` | 6,903 | dn=1 edges=1 |
| 148 | REGEX-FIXED | G4 | S41 | pi_artifact | `session-41/session-41-pi-narrative-spectral-cosmology.md` | 6,894 | auth=1 up=1 dn=1 edges=4 |
| 149 | ORPHAN-PROMOTED | G6 | S79 | plan | `s79-phase-plan.md` | 6,776 | dn=7 edges=7 |
| 150 | MULTI-AUTHOR | G3 | S24 | synthesis | `session-24/session-24a-synthesis.md` | 6,379 | auth=1 up=1 dn=3 edges=7 |
| 151 | REGEX-FIXED | G3 | S29 | wrapup_reviewplan | `session-29/session-29-wrapup-reviewplan.md` | 6,229 | auth=4 up=1 dn=1 edges=6 |
| 152 | REGEX-FIXED | G4 | S43 | single_agent_audit | `session-43/s43_computation_audit.md` | 6,041 | auth=1 dn=2 edges=3 |
| 153 | ORPHAN-PROMOTED | G4 | S45 | addendum | `session-45/s45_addendum_hose_count_ns.md` | 4,516 | up=1 dn=3 edges=6 |
| 154 | REGEX-FIXED | G5 | S69 | dismissal_acknowledgment | `sagan-dismissal-ack.md` | 3,919 | auth=1 dn=1 edges=2 |
| 155 | ORPHAN-PROMOTED | G7 | S84 | settings_diff | `s84-w9a-98-settings-diff.md` | 2,338 | dn=4 edges=4 |
| 156 | ORPHAN-PROMOTED | G4 | S45 | addendum | `session-45/s45_addendum_forward_backward_ns.md` | 2,284 | up=1 dn=1 edges=3 |

---

## (A) Master-aggregator pattern reference (47 files)

These files have NO attribution by design — authorship is offloaded to sister files (`session-N-{agent}-{topic}.md`). Listed here for reference, not for inspection.

| Gen | Sess | File | Size | First header |
|:----|:-----|:-----|-----:|:-------------|
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

---

## Cross-references

- Per-orphan detail: `sessions/framework/registry/orphan-chain-analysis.md`
- Format-generation spec: `sessions/framework/registry/session-format-generations.md`
- Regex module + self-test: `tools/_format_generation_regex_set.py`
- Phase 0.9 zero-coverage scan: `tools/_format_generation_zero_coverage.py`
- Phase 1 harvester: `tools/harvest_attribution_edges.py`
- Phase 1.1 investigator: `tools/_orphan_chain_investigator.py`
- Per-run audit log: `tools/harvest_attribution_edges.log`
- Per-run summary: `tools/harvest_attribution_edges.summary.json`
- Chain analysis JSON: `tools/_orphan_chain_analysis.json`

## Change log

| Date | Session | Change | Author |
|:-----|:--------|:-------|:-------|
| 2026-05-17 | Phase 0.9 / Task #9 | Initial landing — 156 orphan candidates surfaced from full-corpus zero-coverage scan | orchestrator |
| 2026-05-17 | Phase 1.1 / orphan-chain investigation | Updated Status from UNREVIEWED → recommended class (REGEX-FIXED/MULTI-AUTHOR/ORPHAN-PROMOTED/HISTORICAL-ONLY); added Archetype + Chain summary columns; produced companion `orphan-chain-analysis.md` with per-file detail blocks | orchestrator |
