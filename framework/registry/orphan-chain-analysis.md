---
type: orphan-chain-analysis
ingested-by: /weave --update
---

# Orphan chain-of-custody analysis

**Registry ID**: `orphan-chain-analysis`  
**Owner agent(s)**: `orchestrator` (sole writer)  
**Last updated**: 2026-05-17, Phase 1.1  
**Companion**: `sessions/framework/registry/orphan-content-watchlist.md`  
**Source data**: `tools/_orphan_chain_analysis.json`  
**Generator**: `tools/_orphan_chain_investigator.py` + `tools/_emit_orphan_chain_outputs.py`

---

## Purpose

The Phase 0.9 zero-coverage scan surfaced 156 session markdown files that emit ZERO attribution edges via the production Phase 1 harvester (`tools/harvest_attribution_edges.py`). This document is the per-file investigation output — it tells you, for each orphan, the linked chain (what feeds in, what consumes out, who wrote it) AND the recommended edge set to emit on a future harvester promotion pass.

Each entry below contains:

- **Archetype** — classified file type (synthesis, handoff, way-forward, workshop, etc.) with a one-line description
- **Status** — recommended terminal state per the watchlist's 5-state vocabulary
- **Authors** — every attribution candidate extracted by the investigator, with role (author / participant / synthesizer / reviewer / researcher_contributor / etc.) and the verbatim raw token it derived from
- **Upstream chain** — `**Source**:` / `**Reviewing**:` / `**Predecessor**:` / `**Input**:` references with target session numbers, file paths, or researcher IDs
- **Downstream consumers** — files in the corpus that reference this orphan via markdown link or bare path (corpus-inbound-link-index scan)
- **Recommended edges** — per-edge `(type, source, target, in_whitelist)` tuples. Edges with `in_whitelist=True` can be auto-emitted on the next harvester pass; edges with `in_whitelist=False` (none in this run, but reserved for future extensions) would require adding the type to `tools/extract_entities.py::EDGE_TYPE_CANONICAL`

**Synthesis / summary qualification**: per the user's directive, every synthesis-archetype file is explicitly qualified as such by its primary edge type. Synthesis docs emit `synthesized_by` (file → orchestrator/synthesist) + `participates_in` (researcher → file) for every named contributor. Summary docs (handoffs, quicklooks, results-summary) emit `summarizes_session` (file → session) + `authored_by` (file → primary author).

---

## Reading guide for the chain blocks

```
### N. <file basename>
- Path: <full path>
- Generation, Session, Size
- Archetype, Status, Primary edge type
- Authors:  [role] canonical-id  <- raw extracted token
- Upstream: [kind] -> targets
- Downstream: file_path
- Edges (whitelisted): N total
```

---

## Status: `REGEX-FIXED` (43 files)

Attribution successfully extracted — patterns ready to promote into production harvester at `tools/harvest_attribution_edges.py`. Re-running the harvester with these patterns will move these files from 0 edges to N edges per file.

### 1. `s87-cf29-substantive-reading-carve-out.md`

- **Path**: `sessions/archive/session-87/workshops/s87-cf29-substantive-reading-carve-out.md`
- **Session**: S87 | **Generation**: G7 | **Size**: 115,452 B
- **Archetype**: `workshop` — Workshop transcript or output
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `discussed_in`
- **Authors extracted** (2):
    - `[participant]` **`connes-ncg-theorist`** ← raw token: `connes-ncg-theorist`
    - `[participant]` **`sagan-empiricist`** ← raw token: `sagan-empiricist`
- **Upstream chain refs** (6):
    - `[source]` → `87`, `sessions/archive/session-87/session-87-results-workingpaper.md`, `sessions/archive/session-87/workshops/_seed-2.md`
    - `[input]` → `86`, `computations/s84_spectrum_cache_L12_tau019.npz`, `sessions/archive/session-86/session-86-w4-workingpaper.md`
    - `[input]` → `87`
    - `[input]` → `87`
    - `[input]` → `88`, `86`, `computations/s84_spectrum_cache_L12_tau019.npz`, `sessions/archive/session-86/session-86-w4-workingpaper.md`
    - `[input]` → `88`
- **Downstream consumers** (2):
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-88-context.md`
- **Recommended edges** (17 total; 17 whitelist-ready, 0 need extension):
    - `feeds_into`: 10
    - `derived_from`: 3
    - `participates_in`: 2
    - `cited_in`: 2

### 2. `session-74-tgf-pre-registration.md`

- **Path**: `sessions/archive/session-74/session-74-tgf-pre-registration.md`
- **Session**: S74 | **Generation**: G5 | **Size**: 101,661 B
- **Archetype**: `pre_registration` — Pre-registration document
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `pre_registers`
- **Authors extracted** (1):
    - `[author]` **`transit-dynamics-theorist`** ← raw token: `Transit-Dynamics-Theorist`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (2 total; 2 whitelist-ready, 0 need extension):
    - `authored_by`: 1
    - `cited_in`: 1

### 3. `s87-a0-r-protection-m2-biconditional.md`

- **Path**: `sessions/archive/session-87/workshops/s87-a0-r-protection-m2-biconditional.md`
- **Session**: S87 | **Generation**: G7 | **Size**: 87,016 B
- **Archetype**: `workshop` — Workshop transcript or output
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `discussed_in`
- **Authors extracted** (2):
    - `[participant]` **`connes-ncg-theorist`** ← raw token: `connes-ncg-theorist`
    - `[participant]` **`volovik-superfluid-universe-theorist`** ← raw token: `volovik-superfluid-universe-theorist`
- **Upstream chain refs** (8):
    - `[source]` → `87`, `sessions/archive/session-87/session-87-results-workingpaper.md`, `sessions/archive/session-87/workshops/_seed-1.md`
    - `[input]` → `ainur-panel`
    - `[input]` → `86`
    - `[input]` → `ainur-panel`, `connes-ncg-theorist`
    - `[input]` → `ainur-panel`
    - `[input]` → `86`
    - `[input]` → `ainur-panel`
    - `[input]` → `computations/s84_spectrum_cache_L12_tau019.npz`
- **Downstream consumers** (3):
    - `sessions/archive/session-88/session-88-w4a-workingpaper.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-88-context.md`
- **Recommended edges** (16 total; 16 whitelist-ready, 0 need extension):
    - `feeds_into`: 8
    - `derived_from`: 3
    - `cited_in`: 3
    - `participates_in`: 2

### 4. `session-19-primer.md`

- **Path**: `sessions/archive/session-19/session-19-primer.md`
- **Session**: S19 | **Generation**: G3 | **Size**: 63,600 B
- **Archetype**: `session_primer` — Session primer / opening framing
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `primes_session`
- **Authors extracted** (2):
    - `[participant]` **`baptista-spacetime-analyst`** ← raw token: `Baptista`
    - `[participant]` **`tesla-resonance`** ← raw token: `Tesla`
- **Upstream chain refs** (1):
    - `[predecessor]` → `18`, `sessions/session-18/session-18-wrapup.md`
- **Downstream consumers** (6):
    - `sessions/archive/session-20/session-20b-baptista-collab.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-19a-prompt.md`
    - `sessions/session-plan/archive/session-19c-prompt.md`
    - `sessions/session-plan/archive/session-20c-prompt.md`
    - `tools/equation-audit-findings.md`
- **Recommended edges** (10 total; 10 whitelist-ready, 0 need extension):
    - `cited_in`: 6
    - `participates_in`: 2
    - `cites_prior_session`: 2

### 5. `session-44-quicklook-sp-collab.md`

- **Path**: `sessions/archive/session-44/session-44-quicklook-sp-collab.md`
- **Session**: S44 | **Generation**: G4 | **Size**: 57,935 B
- **Archetype**: `solo_collab_review` — Solo collaborative review of session quicklook
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `reviews`
- **Authors extracted** (1):
    - `[filename_derived]` **`schwarzschild-penrose-geometer`** ← raw token: `filename:sp`
- **Upstream chain refs** (2):
    - `[source]` → `44`, `sessions/session-44/session-44-quicklook.md`
    - `[predecessor]` → `44`
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (5 total; 5 whitelist-ready, 0 need extension):
    - `derived_from`: 2
    - `authored_by`: 1
    - `cites_prior_session`: 1
    - `cited_in`: 1

### 6. `session-44-quicklook-connes-collab.md`

- **Path**: `sessions/archive/session-44/session-44-quicklook-connes-collab.md`
- **Session**: S44 | **Generation**: G4 | **Size**: 50,941 B
- **Archetype**: `solo_collab_review` — Solo collaborative review of session quicklook
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `reviews`
- **Authors extracted** (1):
    - `[filename_derived]` **`connes-ncg-theorist`** ← raw token: `filename:connes`
- **Upstream chain refs** (1):
    - `[reviewing]` → `44`
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (3 total; 3 whitelist-ready, 0 need extension):
    - `authored_by`: 1
    - `reviewed_by`: 1
    - `cited_in`: 1

### 7. `session-85-4a-elimination-bulletins-kaku.md`

- **Path**: `sessions/archive/session-85/session-85-4a-elimination-bulletins-kaku.md`
- **Session**: S85 | **Generation**: G7 | **Size**: 49,098 B
- **Archetype**: `uncategorized` — Uncategorized file type
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `authored_by`
- **Authors extracted** (1):
    - `[filename_derived]` **`kaku-speculative-theorist`** ← raw token: `filename:kaku`
- **Upstream chain refs** (1):
    - `[source]` → `85`, `sessions/archive/session-85/session-85-w6-workingpaper.md`
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (4 total; 4 whitelist-ready, 0 need extension):
    - `derived_from`: 2
    - `authored_by`: 1
    - `cited_in`: 1

### 8. `s88-mack-arxiv-2511-07517-desi-review.md`

- **Path**: `sessions/archive/session-88/workshops/s88-mack-arxiv-2511-07517-desi-review.md`
- **Session**: S88 | **Generation**: G7 | **Size**: 44,519 B
- **Archetype**: `workshop` — Workshop transcript or output
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `discussed_in`
- **Authors extracted** (1):
    - `[filename_derived]` **`mack-cosmic-bridge`** ← raw token: `filename:mack`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (3):
    - `sessions/framework/registry/falsifier-master-inventory.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/framework/registry/pre-registered-observations.md`
- **Recommended edges** (4 total; 4 whitelist-ready, 0 need extension):
    - `cited_in`: 3
    - `authored_by`: 1

### 9. `session-16-round-3b-theoretical.md`

- **Path**: `sessions/archive/session-16/session-16-round-3b-theoretical.md`
- **Session**: S16 | **Generation**: G2 | **Size**: 42,755 B
- **Archetype**: `round_discussion` — Multi-round discussion transcript
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `discussed_in`
- **Authors extracted** (3):
    - `[primary]` **`quantum-acoustics-theorist`** ← raw token: `QA-Theorist`
    - `[primary]` **`baptista-spacetime-analyst`** ← raw token: `Baptista-Analyst`
    - `[primary]` **`paasch-mass-quantization-analyst`** ← raw token: `Paasch-Analyst`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (3):
    - `sessions/archive/session-16/session-16-orchestration-state.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-16-workshop-agenda.md`
- **Recommended edges** (6 total; 6 whitelist-ready, 0 need extension):
    - `authored_by`: 3
    - `cited_in`: 3

### 10. `session-85-s1-regulator-boundary-van-den-dungen.md`

- **Path**: `sessions/archive/session-85/session-85-s1-regulator-boundary-van-den-dungen.md`
- **Session**: S85 | **Generation**: G7 | **Size**: 41,537 B
- **Archetype**: `slot_anchored_solo` — G7 slot-anchored solo synthesis
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `authored_by`
- **Authors extracted** (1):
    - `[filename_derived]` **`van-den-dungen-bridge-theorist`** ← raw token: `filename:van-den-dungen`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (3):
    - `sessions/permanent-results-registry.md`
    - `sessions/framework/registry/layer1-layer2-retroactive-audit.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (4 total; 4 whitelist-ready, 0 need extension):
    - `cited_in`: 3
    - `authored_by`: 1

### 11. `s44_sagan_assessment.md`

- **Path**: `sessions/archive/session-44/s44_sagan_assessment.md`
- **Session**: S44 | **Generation**: G4 | **Size**: 39,415 B
- **Archetype**: `single_agent_audit` — Single-agent audit / assessment
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `audits`
- **Authors extracted** (1):
    - `[filename_derived]` **`sagan-empiricist`** ← raw token: `filename:sagan`
- **Upstream chain refs** (1):
    - `[predecessor]` → `43`
- **Downstream consumers** (3):
    - `sessions/archive/session-44/session-44-results-workingpaper.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-44-wave7.md`
- **Recommended edges** (5 total; 5 whitelist-ready, 0 need extension):
    - `cited_in`: 3
    - `authored_by`: 1
    - `cites_prior_session`: 1

### 12. `session-16-round-2d-giants-eval-ii.md`

- **Path**: `sessions/archive/session-16/session-16-round-2d-giants-eval-ii.md`
- **Session**: S16 | **Generation**: G2 | **Size**: 38,865 B
- **Archetype**: `round_discussion` — Multi-round discussion transcript
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `discussed_in`
- **Authors extracted** (1):
    - `[filename_derived]` **`giants-pair`** ← raw token: `filename:giants`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (2):
    - `sessions/archive/session-16/session-16-orchestration-state.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (3 total; 3 whitelist-ready, 0 need extension):
    - `cited_in`: 2
    - `authored_by`: 1

### 13. `session-85-s3-alphas-registry-mack.md`

- **Path**: `sessions/archive/session-85/session-85-s3-alphas-registry-mack.md`
- **Session**: S85 | **Generation**: G7 | **Size**: 38,067 B
- **Archetype**: `slot_anchored_solo` — G7 slot-anchored solo synthesis
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `authored_by`
- **Authors extracted** (1):
    - `[filename_derived]` **`mack-cosmic-bridge`** ← raw token: `filename:mack`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (2 total; 2 whitelist-ready, 0 need extension):
    - `authored_by`: 1
    - `cited_in`: 1

### 14. `session-16-round-2a-veff.md`

- **Path**: `sessions/archive/session-16/session-16-round-2a-veff.md`
- **Session**: S16 | **Generation**: G2 | **Size**: 37,891 B
- **Archetype**: `round_discussion` — Multi-round discussion transcript
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `discussed_in`
- **Authors extracted** (2):
    - `[primary]` **`kaluza-klein-theorist`** ← raw token: `KK-Theorist`
    - `[primary]` **`gen-physicist`** ← raw token: `Gen-Physicist`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (3):
    - `sessions/archive/session-16/session-16-orchestration-state.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-16-workshop-agenda.md`
- **Recommended edges** (5 total; 5 whitelist-ready, 0 need extension):
    - `cited_in`: 3
    - `authored_by`: 2

### 15. `session-85-s2-k-corridor-landau.md`

- **Path**: `sessions/archive/session-85/session-85-s2-k-corridor-landau.md`
- **Session**: S85 | **Generation**: G7 | **Size**: 32,657 B
- **Archetype**: `slot_anchored_solo` — G7 slot-anchored solo synthesis
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `authored_by`
- **Authors extracted** (1):
    - `[filename_derived]` **`landau-condensed-matter-theorist`** ← raw token: `filename:landau`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (2 total; 2 whitelist-ready, 0 need extension):
    - `authored_by`: 1
    - `cited_in`: 1

### 16. `session-16-round-1e-hawking-sagan.md`

- **Path**: `sessions/archive/session-16/session-16-round-1e-hawking-sagan.md`
- **Session**: S16 | **Generation**: G2 | **Size**: 32,423 B
- **Archetype**: `round_discussion` — Multi-round discussion transcript
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `discussed_in`
- **Authors extracted** (2):
    - `[filename_derived]` **`hawking-theorist`** ← raw token: `filename:hawking`
    - `[filename_derived]` **`sagan-empiricist`** ← raw token: `filename:sagan`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (3):
    - `sessions/archive/session-16/session-16-orchestration-state.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-16-workshop-agenda.md`
- **Recommended edges** (5 total; 5 whitelist-ready, 0 need extension):
    - `cited_in`: 3
    - `authored_by`: 2

### 17. `session-44-quicklook-nazarewicz-collab.md`

- **Path**: `sessions/archive/session-44/session-44-quicklook-nazarewicz-collab.md`
- **Session**: S44 | **Generation**: G4 | **Size**: 31,846 B
- **Archetype**: `solo_collab_review` — Solo collaborative review of session quicklook
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `reviews`
- **Authors extracted** (1):
    - `[filename_derived]` **`nazarewicz-nuclear-structure-theorist`** ← raw token: `filename:nazarewicz`
- **Upstream chain refs** (1):
    - `[reviewed]` → `44`
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (3 total; 3 whitelist-ready, 0 need extension):
    - `authored_by`: 1
    - `reviewed_by`: 1
    - `cited_in`: 1

### 18. `session-85-s1-regulator-boundary-connes.md`

- **Path**: `sessions/archive/session-85/session-85-s1-regulator-boundary-connes.md`
- **Session**: S85 | **Generation**: G7 | **Size**: 31,670 B
- **Archetype**: `slot_anchored_solo` — G7 slot-anchored solo synthesis
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `authored_by`
- **Authors extracted** (1):
    - `[filename_derived]` **`connes-ncg-theorist`** ← raw token: `filename:connes`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (2):
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/archive/session-86/seeds/_seed-w5b.md`
- **Recommended edges** (3 total; 3 whitelist-ready, 0 need extension):
    - `cited_in`: 2
    - `authored_by`: 1

### 19. `session-16-round-2d-giants-eval.md`

- **Path**: `sessions/archive/session-16/session-16-round-2d-giants-eval.md`
- **Session**: S16 | **Generation**: G2 | **Size**: 31,068 B
- **Archetype**: `round_discussion` — Multi-round discussion transcript
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `discussed_in`
- **Authors extracted** (1):
    - `[filename_derived]` **`giants-pair`** ← raw token: `filename:giants`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (3):
    - `sessions/archive/session-16/session-16-orchestration-state.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-16-workshop-agenda.md`
- **Recommended edges** (4 total; 4 whitelist-ready, 0 need extension):
    - `cited_in`: 3
    - `authored_by`: 1

### 20. `session-29-observational-excursion.md`

- **Path**: `sessions/archive/session-29/session-29-observational-excursion.md`
- **Session**: S29 | **Generation**: G3 | **Size**: 30,815 B
- **Archetype**: `excursion` — Session excursion / deep-investigation
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `authored_by`
- **Authors extracted** (4):
    - `[team_member]` **`einstein-theorist`** ← raw token: `Einstein`
    - `[team_member]` **`cosmic-web-theorist`** ← raw token: `Cosmic-Web`
    - `[team_member]` **`hawking-theorist`** ← raw token: `Hawking`
    - `[designated_writer]` **`einstein-theorist`** ← raw token: `Einstein`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (5 total; 5 whitelist-ready, 0 need extension):
    - `participates_in`: 3
    - `synthesized_by`: 1
    - `cited_in`: 1

### 21. `session-72-audit-gen-physicist.md`

- **Path**: `sessions/archive/session-72/session-72-audit-gen-physicist.md`
- **Session**: S72 | **Generation**: G5 | **Size**: 30,250 B
- **Archetype**: `audit` — Audit document
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `audits`
- **Authors extracted** (1):
    - `[filename_derived]` **`gen-physicist`** ← raw token: `filename:gen-physicist`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (2 total; 2 whitelist-ready, 0 need extension):
    - `authored_by`: 1
    - `cited_in`: 1

### 22. `session-16-round-2a-hawking-thermodynamics.md`

- **Path**: `sessions/archive/session-16/session-16-round-2a-hawking-thermodynamics.md`
- **Session**: S16 | **Generation**: G2 | **Size**: 29,317 B
- **Archetype**: `round_discussion` — Multi-round discussion transcript
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `discussed_in`
- **Authors extracted** (1):
    - `[filename_derived]` **`hawking-theorist`** ← raw token: `filename:hawking`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (3):
    - `sessions/archive/session-16/session-16-orchestration-state.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `tools/equation-audit-findings.md`
- **Recommended edges** (4 total; 4 whitelist-ready, 0 need extension):
    - `cited_in`: 3
    - `authored_by`: 1

### 23. `session-44-quicklook-einstein-collab.md`

- **Path**: `sessions/archive/session-44/session-44-quicklook-einstein-collab.md`
- **Session**: S44 | **Generation**: G4 | **Size**: 28,788 B
- **Archetype**: `solo_collab_review` — Solo collaborative review of session quicklook
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `reviews`
- **Authors extracted** (1):
    - `[filename_derived]` **`einstein-theorist`** ← raw token: `filename:einstein`
- **Upstream chain refs** (1):
    - `[predecessor]` → `43`
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (3 total; 3 whitelist-ready, 0 need extension):
    - `authored_by`: 1
    - `cites_prior_session`: 1
    - `cited_in`: 1

### 24. `session-43-quicklook-hawking-collab.md`

- **Path**: `sessions/archive/session-43/session-43-quicklook-hawking-collab.md`
- **Session**: S43 | **Generation**: G4 | **Size**: 27,754 B
- **Archetype**: `solo_collab_review` — Solo collaborative review of session quicklook
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `reviews`
- **Authors extracted** (1):
    - `[filename_derived]` **`hawking-theorist`** ← raw token: `filename:hawking`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (2 total; 2 whitelist-ready, 0 need extension):
    - `authored_by`: 1
    - `cited_in`: 1

### 25. `session-46-quicklook-dirac-collab.md`

- **Path**: `sessions/archive/session-46/session-46-quicklook-dirac-collab.md`
- **Session**: S46 | **Generation**: G4 | **Size**: 25,983 B
- **Archetype**: `solo_collab_review` — Solo collaborative review of session quicklook
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `reviews`
- **Authors extracted** (1):
    - `[filename_derived]` **`dirac-antimatter-theorist`** ← raw token: `filename:dirac`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (2 total; 2 whitelist-ready, 0 need extension):
    - `authored_by`: 1
    - `cited_in`: 1

### 26. `session-16-round-1d-einstein-feynman.md`

- **Path**: `sessions/archive/session-16/session-16-round-1d-einstein-feynman.md`
- **Session**: S16 | **Generation**: G2 | **Size**: 25,491 B
- **Archetype**: `round_discussion` — Multi-round discussion transcript
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `discussed_in`
- **Authors extracted** (2):
    - `[participant]` **`einstein-theorist`** ← raw token: `Einstein-Theorist`
    - `[participant]` **`feynman-theorist`** ← raw token: `Feynman`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (3):
    - `sessions/archive/session-16/session-16-orchestration-state.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-16-workshop-agenda.md`
- **Recommended edges** (5 total; 5 whitelist-ready, 0 need extension):
    - `cited_in`: 3
    - `participates_in`: 2

### 27. `session-43-quicklook-einstein-collab.md`

- **Path**: `sessions/archive/session-43/session-43-quicklook-einstein-collab.md`
- **Session**: S43 | **Generation**: G4 | **Size**: 24,318 B
- **Archetype**: `solo_collab_review` — Solo collaborative review of session quicklook
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `reviews`
- **Authors extracted** (1):
    - `[filename_derived]` **`einstein-theorist`** ← raw token: `filename:einstein`
- **Upstream chain refs** (1):
    - `[reference_corpus]` → `43`, `42`
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (4 total; 4 whitelist-ready, 0 need extension):
    - `cites_prior_session`: 2
    - `authored_by`: 1
    - `cited_in`: 1

### 28. `session-16-orchestration-state.md`

- **Path**: `sessions/archive/session-16/session-16-orchestration-state.md`
- **Session**: S16 | **Generation**: G2 | **Size**: 24,059 B
- **Archetype**: `orchestration_state` — Orchestration tracking state
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `tracks_session`
- **Authors extracted** (7):
    - `[participant]` **`kaluza-klein-theorist`** ← raw token: `kaluza-klein-specialist`
    - `[participant]` **`baptista-spacetime-analyst`** ← raw token: `baptista-specialist`
    - `[participant]` **`gen-physicist`** ← raw token: `gen-physicist`
    - `[participant]` **`paasch-mass-quantization-analyst`** ← raw token: `paasch-specialist`
    - `[participant]` **`quantum-acoustics-theorist`** ← raw token: `quantum-acoustics-theorist`
    - `[participant]` **`einstein-theorist`** ← raw token: `Einstein`
    - `[participant]` **`feynman-theorist`** ← raw token: `Feynman`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (8 total; 8 whitelist-ready, 0 need extension):
    - `participates_in`: 7
    - `cited_in`: 1

### 29. `session-26-priority-1.md`

- **Path**: `sessions/archive/session-26/session-26-priority-1.md`
- **Session**: S26 | **Generation**: G3 | **Size**: 23,463 B
- **Archetype**: `priority_computation` — Numbered priority computation
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `authored_by`
- **Authors extracted** (2):
    - `[participant]` **`phonon-first-cosmologist`** ← raw token: `phonon-exflation-sim`
    - `[primary]` **`phonon-first-cosmologist`** ← raw token: `phonon-exflation-sim`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (2):
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-26-plan.md`
- **Recommended edges** (4 total; 4 whitelist-ready, 0 need extension):
    - `cited_in`: 2
    - `participates_in`: 1
    - `authored_by`: 1

### 30. `session-29Ac-workshop.md`

- **Path**: `sessions/archive/session-29/session-29Ac-workshop.md`
- **Session**: S29 | **Generation**: G3 | **Size**: 22,204 B
- **Archetype**: `workshop` — Workshop transcript
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `discussed_in`
- **Authors extracted** (5):
    - `[team_member]` **`hawking-theorist`** ← raw token: `hawking`
    - `[team_member]` **`orchestrator`** ← raw token: `coordinator`
    - `[team_member]` **`baptista-spacetime-analyst`** ← raw token: `baptista`
    - `[participant]` **`baptista-spacetime-analyst`** ← raw token: `baptista`
    - `[primary]` **`baptista-spacetime-analyst`** ← raw token: `baptista`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (3):
    - `sessions/archive/session-29/session-29-wrapup.md`
    - `sessions/archive/session-29/session-29Ac-synthesis.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (8 total; 8 whitelist-ready, 0 need extension):
    - `participates_in`: 4
    - `cited_in`: 3
    - `authored_by`: 1

### 31. `session-52-qfoam-collab.md`

- **Path**: `sessions/archive/session-52/session-52-qfoam-collab.md`
- **Session**: S52 | **Generation**: G4 | **Size**: 21,425 B
- **Archetype**: `solo_collab_review` — Solo collaborative review
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `reviews`
- **Authors extracted** (1):
    - `[filename_derived]` **`quantum-foam-theorist`** ← raw token: `filename:qfoam`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (3):
    - `sessions/archive/session-52/session-52-master-collab.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `summary/session-52-final.md`
- **Recommended edges** (4 total; 4 whitelist-ready, 0 need extension):
    - `cited_in`: 3
    - `authored_by`: 1

### 32. `session-43-quicklook-quantum-foam-collab.md`

- **Path**: `sessions/archive/session-43/session-43-quicklook-quantum-foam-collab.md`
- **Session**: S43 | **Generation**: G4 | **Size**: 20,655 B
- **Archetype**: `solo_collab_review` — Solo collaborative review of session quicklook
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `reviews`
- **Authors extracted** (1):
    - `[filename_derived]` **`quantum-foam-theorist`** ← raw token: `filename:quantum-foam`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (2 total; 2 whitelist-ready, 0 need extension):
    - `authored_by`: 1
    - `cited_in`: 1

### 33. `session-35-KK-NCG-Excursion.md`

- **Path**: `sessions/archive/session-35/session-35-KK-NCG-Excursion.md`
- **Session**: S35 | **Generation**: G3 | **Size**: 19,999 B
- **Archetype**: `excursion` — Session excursion / deep-investigation
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `authored_by`
- **Authors extracted** (1):
    - `[filename_derived]` **`kaluza-klein-theorist`** ← raw token: `filename:kk`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (2):
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `summary/Archives/session-35-final.md`
- **Recommended edges** (3 total; 3 whitelist-ready, 0 need extension):
    - `cited_in`: 2
    - `authored_by`: 1

### 34. `session-43-quicklook-quantum-acoustics-collab.md`

- **Path**: `sessions/archive/session-43/session-43-quicklook-quantum-acoustics-collab.md`
- **Session**: S43 | **Generation**: G4 | **Size**: 18,900 B
- **Archetype**: `solo_collab_review` — Solo collaborative review of session quicklook
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `reviews`
- **Authors extracted** (1):
    - `[filename_derived]` **`quantum-acoustics-theorist`** ← raw token: `filename:quantum-acoustics`
- **Upstream chain refs** (1):
    - `[reviewed]` → `43`
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (3 total; 3 whitelist-ready, 0 need extension):
    - `authored_by`: 1
    - `reviewed_by`: 1
    - `cited_in`: 1

### 35. `session-19d-tesla-quantum-acoustics-collab.md`

- **Path**: `sessions/archive/session-19/session-19d-tesla-quantum-acoustics-collab.md`
- **Session**: S19 | **Generation**: G3 | **Size**: 17,628 B
- **Archetype**: `solo_collab_review` — Solo collaborative review
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `reviews`
- **Authors extracted** (2):
    - `[filename_derived]` **`quantum-acoustics-theorist`** ← raw token: `filename:quantum-acoustics`
    - `[filename_derived]` **`tesla-resonance`** ← raw token: `filename:tesla`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (3 total; 3 whitelist-ready, 0 need extension):
    - `authored_by`: 2
    - `cited_in`: 1

### 36. `session-16-einstein-feynman-review.md`

- **Path**: `sessions/archive/session-16/session-16-einstein-feynman-review.md`
- **Session**: S16 | **Generation**: G2 | **Size**: 16,738 B
- **Archetype**: `review` — Review document
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `reviews`
- **Authors extracted** (2):
    - `[filename_derived]` **`einstein-theorist`** ← raw token: `filename:einstein`
    - `[filename_derived]` **`feynman-theorist`** ← raw token: `filename:feynman`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (4):
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-17a-prompt.md`
    - `sessions/session-plan/archive/session-17b-prompt.md`
    - `sessions/session-plan/archive/session-17c-prompt.md`
- **Recommended edges** (6 total; 6 whitelist-ready, 0 need extension):
    - `cited_in`: 4
    - `authored_by`: 2

### 37. `session-56-string-collab.md`

- **Path**: `sessions/archive/session-56/session-56-string-collab.md`
- **Session**: S56 | **Generation**: G4 | **Size**: 15,996 B
- **Archetype**: `solo_collab_review` — Solo collaborative review
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `reviews`
- **Authors extracted** (1):
    - `[filename_derived]` **`string-theory-theorist`** ← raw token: `filename:string`
- **Upstream chain refs** (1):
    - `[source]` → `56`
- **Downstream consumers** (3):
    - `sessions/archive/session-56/session-56-workshop-2-cc-formula.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `summary/session-56-final.md`
- **Recommended edges** (5 total; 5 whitelist-ready, 0 need extension):
    - `cited_in`: 3
    - `authored_by`: 1
    - `derived_from`: 1

### 38. `session-34-exploration-addendum.md`

- **Path**: `sessions/archive/session-34/session-34-exploration-addendum.md`
- **Session**: S34 | **Generation**: G3 | **Size**: 10,959 B
- **Archetype**: `addendum` — Session addendum
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `addendum_to`
- **Authors extracted** (2):
    - `[participant]` **`user`** ← raw token: `User`
    - `[participant]` **`orchestrator`** ← raw token: `Team-Lead`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (4):
    - `sessions/archive/session-34/session-34-master-synthesis.md`
    - `sessions/archive/session-34/session-34-synthesis.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `summary/Archives/session-34-final.md`
- **Recommended edges** (6 total; 6 whitelist-ready, 0 need extension):
    - `cited_in`: 4
    - `participates_in`: 2

### 39. `session-41-pi-directive-complexity-is-geometry.md`

- **Path**: `sessions/archive/session-41/session-41-pi-directive-complexity-is-geometry.md`
- **Session**: S41 | **Generation**: G4 | **Size**: 7,672 B
- **Archetype**: `pi_artifact` — PI artifact
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `directs_session`
- **Authors extracted** (1):
    - `[filename_derived]` **`meme-pi`** ← raw token: `filename:pi`
- **Upstream chain refs** (1):
    - `[source]` → `41`, `meme-pi`
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (4 total; 4 whitelist-ready, 0 need extension):
    - `derived_from`: 2
    - `authored_by`: 1
    - `cited_in`: 1

### 40. `session-41-pi-narrative-spectral-cosmology.md`

- **Path**: `sessions/archive/session-41/session-41-pi-narrative-spectral-cosmology.md`
- **Session**: S41 | **Generation**: G4 | **Size**: 6,894 B
- **Archetype**: `pi_artifact` — PI artifact
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `directs_session`
- **Authors extracted** (1):
    - `[filename_derived]` **`meme-pi`** ← raw token: `filename:pi`
- **Upstream chain refs** (1):
    - `[source]` → `41`, `meme-pi`
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (4 total; 4 whitelist-ready, 0 need extension):
    - `derived_from`: 2
    - `authored_by`: 1
    - `cited_in`: 1

### 41. `session-29-wrapup-reviewplan.md`

- **Path**: `sessions/archive/session-29/session-29-wrapup-reviewplan.md`
- **Session**: S29 | **Generation**: G3 | **Size**: 6,229 B
- **Archetype**: `wrapup_reviewplan` — Wrapup review plan
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `plans_session`
- **Authors extracted** (4):
    - `[designated_writer]` **`baptista-spacetime-analyst`** ← raw token: `Baptista`
    - `[designated_writer]` **`connes-ncg-theorist`** ← raw token: `Connes`
    - `[designated_writer]` **`landau-condensed-matter-theorist`** ← raw token: `Landau`
    - `[designated_writer]` **`dirac-antimatter-theorist`** ← raw token: `Dirac`
- **Upstream chain refs** (1):
    - `[input]` → `29`
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (6 total; 6 whitelist-ready, 0 need extension):
    - `synthesized_by`: 4
    - `feeds_into`: 1
    - `cited_in`: 1

### 42. `s43_computation_audit.md`

- **Path**: `sessions/archive/session-43/s43_computation_audit.md`
- **Session**: S43 | **Generation**: G4 | **Size**: 6,041 B
- **Archetype**: `single_agent_audit` — Single-agent audit / assessment
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `audits`
- **Authors extracted** (1):
    - `[auditor]` **`dirac-antimatter-theorist`** ← raw token: `Dirac-Antimatter-Theorist`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (2):
    - `sessions/archive/session-43/session-43-results-workingpaper.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (3 total; 3 whitelist-ready, 0 need extension):
    - `cited_in`: 2
    - `reviewed_by`: 1

### 43. `sagan-dismissal-ack.md`

- **Path**: `sessions/archive/session-69/sagan-dismissal-ack.md`
- **Session**: S69 | **Generation**: G5 | **Size**: 3,919 B
- **Archetype**: `dismissal_acknowledgment` — Agent dismissal acknowledgment
- **Status**: `REGEX-FIXED`
- **Primary edge type**: `acknowledges`
- **Authors extracted** (1):
    - `[filename_derived]` **`sagan-empiricist`** ← raw token: `filename:sagan`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (2 total; 2 whitelist-ready, 0 need extension):
    - `authored_by`: 1
    - `cited_in`: 1

## Status: `MULTI-AUTHOR` (60 files)

Synthesis-archetype files where attribution is either extracted (per-section `**Researcher**:` or bracket-tag) or implicit (file is multi-author by design). Recommended edges: `synthesized_by` + per-contributor `participates_in`.

### 44. `session-60-wayforward.md`

- **Path**: `sessions/archive/session-60/session-60-wayforward.md`
- **Session**: S60 | **Generation**: G4 | **Size**: 168,290 B
- **Archetype**: `wayforward` — Way-forward computation extraction
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `plans_next_session`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (53):
    - `[source]` → `60`, `connes-ncg-theorist`, `van-den-dungen-bridge-theorist`, `nazarewicz-nuclear-structure-theorist`
    - `[source_files]` → `60`, `sessions/archive/session-60/session-60-sp-collab.md`
    - `[source_files]` → `60`, `sessions/archive/session-60/session-60-hawking-collab.md`
    - `[source_files]` → `60`, `sessions/archive/session-60/session-60-vol-collab.md`, `sessions/archive/session-60/framework-3HeB-comparison.md`
    - `[source_files]` → `60`, `sessions/archive/session-60/session-60-bap-collab.md`
    - `[source_files]` → `60`, `sessions/archive/session-60/session-60-tesla-collab.md`
    - `[source_files]` → `60`, `sessions/archive/session-60/session-60-qa-collab.md`
    - `[source_files]` → `60`, `sessions/archive/session-60/session-60-landau-collab.md`
    - _(+45 more refs omitted for readability — see full JSON)_
- **Downstream consumers** (7):
    - `sessions/archive/session-61/session-61-wave1-workingpaper.md`
    - `sessions/archive/session-61/session-61-wave2-workingpaper.md`
    - `sessions/archive/session-61/session-61-wave3-workingpaper.md`
    - `sessions/archive/session-61/session-61-wave4-workingpaper.md`
    - `sessions/archive/session-61/session-61-wave5-workingpaper.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-61-plan.md`
- **Recommended edges** (101 total; 101 whitelist-ready, 0 need extension):
    - `feeds_into`: 63
    - `derived_from`: 31
    - `cited_in`: 7

### 45. `session-25-Investigation-Collaborate-Efforts.md`

- **Path**: `sessions/archive/session-25/session-25-Investigation-Collaborate-Efforts.md`
- **Session**: S25 | **Generation**: G3 | **Size**: 161,045 B
- **Archetype**: `synergy_index` — Multi-researcher synergy/investigation index
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (22):
    - `[primary]` **`einstein-theorist`** ← raw token: `Einstein`
    - `[primary]` **`landau-condensed-matter-theorist`** ← raw token: `Landau`
    - `[primary]` **`sagan-empiricist`** ← raw token: `Sagan`
    - `[primary]` **`connes-ncg-theorist`** ← raw token: `Connes`
    - `[primary]` **`berry-geometric-phase-theorist`** ← raw token: `Berry`
    - `[primary]` **`tesla-resonance`** ← raw token: `Tesla`
    - `[primary]` **`dirac-antimatter-theorist`** ← raw token: `Dirac`
    - `[primary]` **`paasch-mass-quantization-analyst`** ← raw token: `Paasch`
    - `[primary]` **`neutrino-detection-specialist`** ← raw token: `Neutrino`
    - `[primary]` **`feynman-theorist`** ← raw token: `Feynman`
    - `[primary]` **`hawking-theorist`** ← raw token: `Hawking`
    - `[primary]` **`kaluza-klein-theorist`** ← raw token: `Kaluza-Klein`
    - `[primary]` **`baptista-spacetime-analyst`** ← raw token: `Baptista`
    - `[primary]` **`schwarzschild-penrose-geometer`** ← raw token: `Schwarzschild-Penrose`
    - `[researcher_contributor]` **`kaluza-klein-theorist`** ← raw token: `[KK]`
    - `[researcher_contributor]` **`dirac-antimatter-theorist`** ← raw token: `[D]`
    - `[researcher_contributor]` **`landau-condensed-matter-theorist`** ← raw token: `[L]`
    - `[researcher_contributor]` **`cosmic-web-theorist`** ← raw token: `[C]`
    - `[researcher_contributor]` **`feynman-theorist`** ← raw token: `[F]`
    - `[researcher_contributor]` **`hawking-theorist`** ← raw token: `[H]`
    - `[researcher_contributor]` **`einstein-theorist`** ← raw token: `[E]`
    - `[researcher_contributor]` **`quantum-acoustics-theorist`** ← raw token: `[QA]`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (3):
    - `sessions/archive/session-25/session-25-graceful-handoff.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `summary/Archives/session-25-final.md`
- **Recommended edges** (25 total; 25 whitelist-ready, 0 need extension):
    - `authored_by`: 14
    - `participates_in`: 8
    - `cited_in`: 3

### 46. `session-25-Investigation-Question-Efforts.md`

- **Path**: `sessions/archive/session-25/session-25-Investigation-Question-Efforts.md`
- **Session**: S25 | **Generation**: G3 | **Size**: 136,476 B
- **Archetype**: `synergy_index` — Multi-researcher synergy/investigation index
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (2):
    - `[researcher_contributor]` **`kaluza-klein-theorist`** ← raw token: `[KK]`
    - `[researcher_contributor]` **`quantum-acoustics-theorist`** ← raw token: `[QA]`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (3 total; 3 whitelist-ready, 0 need extension):
    - `participates_in`: 2
    - `cited_in`: 1

### 47. `session-25-Investigation-Assessment-Efforts.md`

- **Path**: `sessions/archive/session-25/session-25-Investigation-Assessment-Efforts.md`
- **Session**: S25 | **Generation**: G3 | **Size**: 98,960 B
- **Archetype**: `synergy_index` — Multi-researcher synergy/investigation index
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (2):
    - `sessions/archive/session-25/session-25-Investigation-Closing.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (2 total; 2 whitelist-ready, 0 need extension):
    - `cited_in`: 2

### 48. `session-27-wrapup.md`

- **Path**: `sessions/archive/session-27/session-27-wrapup.md`
- **Session**: S27 | **Generation**: G3 | **Size**: 58,682 B
- **Archetype**: `handoff` — Session-level handoff or wrap-up document
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `summarizes_session`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (3):
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-27-plan.md`
    - `sessions/session-plan/archive/session-28-prompt-a.md`
- **Recommended edges** (3 total; 3 whitelist-ready, 0 need extension):
    - `cited_in`: 3

### 49. `session-21c-phase0-synthesis.md`

- **Path**: `sessions/archive/session-21/session-21c-phase0-synthesis.md`
- **Session**: S21 | **Generation**: G3 | **Size**: 51,570 B
- **Archetype**: `synthesis` — Synthesis document
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (1):
    - `[designated_writer]` **`orchestrator`** ← raw token: `coordinator`
- **Upstream chain refs** (1):
    - `[source]` → `berry-geometric-phase-theorist`
- **Downstream consumers** (4):
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-22a-prompt.md`
    - `sessions/session-plan/archive/session-22b-prompt.md`
    - `sessions/session-plan/archive/session-22c-prompt.md`
- **Recommended edges** (6 total; 6 whitelist-ready, 0 need extension):
    - `cited_in`: 4
    - `synthesized_by`: 1
    - `derived_from`: 1

### 50. `session-21a-ainur-synthesis.md`

- **Path**: `sessions/archive/session-21/session-21a-ainur-synthesis.md`
- **Session**: S21 | **Generation**: G3 | **Size**: 48,451 B
- **Archetype**: `synthesis` — Synthesis document
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (7):
    - `[participant]` **`tesla-resonance`** ← raw token: `tesla`
    - `[participant]` **`landau-condensed-matter-theorist`** ← raw token: `landau`
    - `[participant]` **`connes-ncg-theorist`** ← raw token: `connes`
    - `[participant]` **`feynman-theorist`** ← raw token: `feynman`
    - `[participant]` **`quantum-acoustics-theorist`** ← raw token: `quantum-acoustics`
    - `[participant]` **`orchestrator`** ← raw token: `coordinator`
    - `[filename_derived]` **`ainur-panel`** ← raw token: `filename:ainur`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (2):
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-21c-prompt.md`
- **Recommended edges** (9 total; 9 whitelist-ready, 0 need extension):
    - `participates_in`: 6
    - `cited_in`: 2
    - `authored_by`: 1

### 51. `session-25-Investigation-Closing.md`

- **Path**: `sessions/archive/session-25/session-25-Investigation-Closing.md`
- **Session**: S25 | **Generation**: G3 | **Size**: 45,855 B
- **Archetype**: `synergy_index` — Multi-researcher synergy/investigation index
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (1 total; 1 whitelist-ready, 0 need extension):
    - `cited_in`: 1

### 52. `session-61-midsession-review.md`

- **Path**: `sessions/archive/session-61/session-61-midsession-review.md`
- **Session**: S61 | **Generation**: G5 | **Size**: 44,495 B
- **Archetype**: `midsession_review` — Mid-session review
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `reviews_session`
- **Authors extracted** (1):
    - `[assessor]` **`sagan-empiricist`** ← raw token: `Sagan-Empiricist`
- **Upstream chain refs** (1):
    - `[reviewed]` → `61`
- **Downstream consumers** (2):
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `summary/session-61-final.md`
- **Recommended edges** (4 total; 4 whitelist-ready, 0 need extension):
    - `reviewed_by`: 2
    - `cited_in`: 2

### 53. `session-20c-synthesis.md`

- **Path**: `sessions/archive/session-20/session-20c-synthesis.md`
- **Session**: S20 | **Generation**: G3 | **Size**: 42,761 B
- **Archetype**: `synthesis` — Synthesis document
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (7):
    - `[participant]` **`gen-physicist`** ← raw token: `gen-physicist`
    - `[participant]` **`sagan-empiricist`** ← raw token: `sagan-empiricist`
    - `[participant]` **`orchestrator`** ← raw token: `coordinator`
    - `[participant]` **`connes-ncg-theorist`** ← raw token: `connes`
    - `[participant]` **`kaluza-klein-theorist`** ← raw token: `kk-theorist`
    - `[participant]` **`baptista-spacetime-analyst`** ← raw token: `baptista`
    - `[participant]` **`dirac-antimatter-theorist`** ← raw token: `dirac`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (4):
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-21a-prompt.md`
    - `sessions/session-plan/archive/session-21b-prompt.md`
    - `sessions/session-plan/archive/session-21c-prompt.md`
- **Recommended edges** (11 total; 11 whitelist-ready, 0 need extension):
    - `participates_in`: 7
    - `cited_in`: 4

### 54. `session-28-fusion-synthesis.md`

- **Path**: `sessions/archive/session-28/session-28-fusion-synthesis.md`
- **Session**: S28 | **Generation**: G3 | **Size**: 38,317 B
- **Archetype**: `fusion_synthesis` — Fusion synthesis across teams
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (5):
    - `[designated_writer]` **`baptista-spacetime-analyst`** ← raw token: `Baptista`
    - `[lead]` **`tesla-resonance`** ← raw token: `Tesla`
    - `[lead]` **`baptista-spacetime-analyst`** ← raw token: `Baptista`
    - `[lead]` **`landau-condensed-matter-theorist`** ← raw token: `Landau`
    - `[lead]` **`dirac-antimatter-theorist`** ← raw token: `Dirac`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (10):
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-29Aa-prompt.md`
    - `sessions/session-plan/archive/session-29Ab-prompt.md`
    - `sessions/session-plan/archive/session-29Ba-prompt.md`
    - `sessions/session-plan/archive/session-29Bb-prompt.md`
    - `sessions/session-plan/archive/session-30B-prompt.md`
    - `sessions/session-plan/archive/session-30Ba-prompt.md`
    - `sessions/session-plan/archive/session-30Bb-prompt.md`
    - _(+2 more consumers omitted — see full JSON)_
- **Recommended edges** (15 total; 15 whitelist-ready, 0 need extension):
    - `cited_in`: 10
    - `synthesized_by`: 5

### 55. `session-90-connes-s5-pin-derivative-synthesis.md`

- **Path**: `sessions/archive/session-90/session-90-connes-s5-pin-derivative-synthesis.md`
- **Session**: S90 | **Generation**: G7 | **Size**: 35,586 B
- **Archetype**: `synthesis` — Synthesis document
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (1):
    - `[filename_derived]` **`connes-ncg-theorist`** ← raw token: `filename:connes`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (3):
    - `sessions/archive/session-90/session-90-gen-physicist-s8-combined-landscape-synthesis.md`
    - `sessions/session-plan/session-91-context.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (4 total; 4 whitelist-ready, 0 need extension):
    - `cited_in`: 3
    - `authored_by`: 1

### 56. `session-52-way-forward.md`

- **Path**: `sessions/archive/session-52/session-52-way-forward.md`
- **Session**: S52 | **Generation**: G4 | **Size**: 33,789 B
- **Archetype**: `wayforward` — Way-forward computation extraction
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `plans_next_session`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (2):
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-53-plan.md`
- **Recommended edges** (2 total; 2 whitelist-ready, 0 need extension):
    - `cited_in`: 2

### 57. `session-60-synthesis.md`

- **Path**: `sessions/archive/session-60/session-60-synthesis.md`
- **Session**: S60 | **Generation**: G4 | **Size**: 33,450 B
- **Archetype**: `synthesis` — Synthesis document
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (1):
    - `[synthesizer]` **`mack-cosmic-bridge`** ← raw token: `mack-cosmic-bridge`
- **Upstream chain refs** (1):
    - `[source]` → `60`
- **Downstream consumers** (3):
    - `sessions/archive/session-60/session-60-vdd-framework-review.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `summary/session-60-final.md`
- **Recommended edges** (5 total; 5 whitelist-ready, 0 need extension):
    - `cited_in`: 3
    - `synthesized_by`: 1
    - `derived_from`: 1

### 58. `session-33a-synthesis.md`

- **Path**: `sessions/archive/session-33/session-33a-synthesis.md`
- **Session**: S33 | **Generation**: G3 | **Size**: 31,485 B
- **Archetype**: `synthesis` — Synthesis document
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (2):
    - `[participant]` **`phonon-first-cosmologist`** ← raw token: `sim`
    - `[participant]` **`baptista-spacetime-analyst`** ← raw token: `baptista`
- **Upstream chain refs** (5):
    - `[source]` → `phonon-first-cosmologist`, `baptista-spacetime-analyst`
    - `[source]` → `phonon-first-cosmologist`, `baptista-spacetime-analyst`
    - `[source]` → `phonon-first-cosmologist`, `baptista-spacetime-analyst`
    - `[source]` → `phonon-first-cosmologist`, `baptista-spacetime-analyst`
    - `[source]` → `baptista-spacetime-analyst`
- **Downstream consumers** (7):
    - `sessions/archive/session-33/session-33-tesla-collab.md`
    - `sessions/archive/session-33/session-33b-synthesis.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-33a-prompt.md`
    - `sessions/session-plan/archive/session-33b-prompt.md`
    - `sessions/session-plan/archive/session-34-plan.md`
    - `summary/Archives/session-33-final.md`
- **Recommended edges** (18 total; 18 whitelist-ready, 0 need extension):
    - `derived_from`: 9
    - `cited_in`: 7
    - `participates_in`: 2

### 59. `session-25-Investigation-Framework.md`

- **Path**: `sessions/archive/session-25/session-25-Investigation-Framework.md`
- **Session**: S25 | **Generation**: G3 | **Size**: 30,674 B
- **Archetype**: `synergy_index` — Multi-researcher synergy/investigation index
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (1 total; 1 whitelist-ready, 0 need extension):
    - `cited_in`: 1

### 60. `session-29-team-A-synthesis.md`

- **Path**: `sessions/archive/session-29/session-29-team-A-synthesis.md`
- **Session**: S29 | **Generation**: G3 | **Size**: 30,520 B
- **Archetype**: `team_synthesis` — Multi-agent team synthesis
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (5):
    - `[team_member]` **`einstein-theorist`** ← raw token: `Einstein`
    - `[team_member]` **`baptista-spacetime-analyst`** ← raw token: `Baptista`
    - `[team_member]` **`schwarzschild-penrose-geometer`** ← raw token: `Schwarzschild-Penrose`
    - `[team_member]` **`kaluza-klein-theorist`** ← raw token: `Kaluza-Klein`
    - `[designated_writer]` **`baptista-spacetime-analyst`** ← raw token: `Baptista`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (6 total; 6 whitelist-ready, 0 need extension):
    - `participates_in`: 4
    - `synthesized_by`: 1
    - `cited_in`: 1

### 61. `session-29-team-E-synthesis.md`

- **Path**: `sessions/archive/session-29/session-29-team-E-synthesis.md`
- **Session**: S29 | **Generation**: G3 | **Size**: 30,396 B
- **Archetype**: `team_synthesis` — Multi-agent team synthesis
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (2):
    - `[team_member]` **`sagan-empiricist`** ← raw token: `Sagan`
    - `[designated_writer]` **`sagan-empiricist`** ← raw token: `Sagan`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (3 total; 3 whitelist-ready, 0 need extension):
    - `participates_in`: 1
    - `synthesized_by`: 1
    - `cited_in`: 1

### 62. `session-54-qa-hawking-workshop-synthesis.md`

- **Path**: `sessions/archive/session-54/session-54-qa-hawking-workshop-synthesis.md`
- **Session**: S54 | **Generation**: G4 | **Size**: 29,931 B
- **Archetype**: `synthesis` — Synthesis document
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (2):
    - `[participant]` **`quantum-acoustics-theorist`** ← raw token: `QA`
    - `[participant]` **`hawking-theorist`** ← raw token: `Hawking`
- **Upstream chain refs** (1):
    - `[source]` → `54`
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (4 total; 4 whitelist-ready, 0 need extension):
    - `participates_in`: 2
    - `derived_from`: 1
    - `cited_in`: 1

### 63. `session-79-final.md`

- **Path**: `sessions/archive/session-79/session-79-final.md`
- **Session**: S79 | **Generation**: G6 | **Size**: 29,797 B
- **Archetype**: `handoff` — Session-level handoff or wrap-up document
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `summarizes_session`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (6):
    - `sessions/archive/session-79/s79-pause-resume.md`
    - `sessions/archive/session-80/session-80-results-workingpaper.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-80-context.md`
    - `summary/session-79-final.md`
    - `summary/session-80-final.md`
- **Recommended edges** (6 total; 6 whitelist-ready, 0 need extension):
    - `cited_in`: 6

### 64. `session-29-fusion-synthesis.md`

- **Path**: `sessions/archive/session-29/session-29-fusion-synthesis.md`
- **Session**: S29 | **Generation**: G3 | **Size**: 29,478 B
- **Archetype**: `fusion_synthesis` — Fusion synthesis across teams
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (9):
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-30B-prompt.md`
    - `sessions/session-plan/archive/session-30Ba-prompt.md`
    - `sessions/session-plan/archive/session-30Bb-prompt.md`
    - `sessions/session-plan/archive/session-31-baptista-plan.md`
    - `sessions/session-plan/archive/session-31Aa-prompt.md`
    - `sessions/session-plan/archive/session-31B-plan.md`
    - `sessions/session-plan/archive/session-31Ba-prompt.md`
    - _(+1 more consumers omitted — see full JSON)_
- **Recommended edges** (9 total; 9 whitelist-ready, 0 need extension):
    - `cited_in`: 9

### 65. `session-29-wrapup.md`

- **Path**: `sessions/archive/session-29/session-29-wrapup.md`
- **Session**: S29 | **Generation**: G3 | **Size**: 29,155 B
- **Archetype**: `handoff` — Session-level handoff or wrap-up document
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `summarizes_session`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (3):
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-30B-prompt.md`
    - `sessions/session-plan/archive/session-30Ba-prompt.md`
- **Recommended edges** (3 total; 3 whitelist-ready, 0 need extension):
    - `cited_in`: 3

### 66. `session-28-team-synthesis-b.md`

- **Path**: `sessions/archive/session-28/session-28-team-synthesis-b.md`
- **Session**: S28 | **Generation**: G3 | **Size**: 28,341 B
- **Archetype**: `team_synthesis` — Multi-agent team synthesis
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (4):
    - `[participant]` **`einstein-theorist`** ← raw token: `Einstein`
    - `[participant]` **`hawking-theorist`** ← raw token: `Hawking`
    - `[participant]` **`cosmic-web-theorist`** ← raw token: `Cosmic-Web`
    - `[designated_writer]` **`orchestrator`** ← raw token: `Coordinator`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (3):
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-29Aa-prompt.md`
    - `sessions/session-plan/archive/session-29Ab-prompt.md`
- **Recommended edges** (7 total; 7 whitelist-ready, 0 need extension):
    - `participates_in`: 3
    - `cited_in`: 3
    - `synthesized_by`: 1

### 67. `session-29-team-B-synthesis.md`

- **Path**: `sessions/archive/session-29/session-29-team-B-synthesis.md`
- **Session**: S29 | **Generation**: G3 | **Size**: 27,318 B
- **Archetype**: `team_synthesis` — Multi-agent team synthesis
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (4):
    - `[team_member]` **`connes-ncg-theorist`** ← raw token: `Connes`
    - `[team_member]` **`berry-geometric-phase-theorist`** ← raw token: `Berry`
    - `[team_member]` **`paasch-mass-quantization-analyst`** ← raw token: `Paasch`
    - `[designated_writer]` **`connes-ncg-theorist`** ← raw token: `Connes`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (5 total; 5 whitelist-ready, 0 need extension):
    - `participates_in`: 3
    - `synthesized_by`: 1
    - `cited_in`: 1

### 68. `session-29-team-C-synthesis.md`

- **Path**: `sessions/archive/session-29/session-29-team-C-synthesis.md`
- **Session**: S29 | **Generation**: G3 | **Size**: 26,639 B
- **Archetype**: `team_synthesis` — Multi-agent team synthesis
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (4):
    - `[team_member]` **`landau-condensed-matter-theorist`** ← raw token: `Landau`
    - `[team_member]` **`feynman-theorist`** ← raw token: `Feynman`
    - `[team_member]` **`tesla-resonance`** ← raw token: `Tesla`
    - `[designated_writer]` **`landau-condensed-matter-theorist`** ← raw token: `Landau`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (5 total; 5 whitelist-ready, 0 need extension):
    - `participates_in`: 3
    - `synthesized_by`: 1
    - `cited_in`: 1

### 69. `session-54-master-workshop-synthesis.md`

- **Path**: `sessions/archive/session-54/session-54-master-workshop-synthesis.md`
- **Session**: S54 | **Generation**: G4 | **Size**: 26,481 B
- **Archetype**: `synthesis` — Synthesis document
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (1 total; 1 whitelist-ready, 0 need extension):
    - `cited_in`: 1

### 70. `session-28-team-synthesis-d.md`

- **Path**: `sessions/archive/session-28/session-28-team-synthesis-d.md`
- **Session**: S28 | **Generation**: G3 | **Size**: 26,288 B
- **Archetype**: `team_synthesis` — Multi-agent team synthesis
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (5):
    - `[participant]` **`kaluza-klein-theorist`** ← raw token: `KK`
    - `[participant]` **`baptista-spacetime-analyst`** ← raw token: `Baptista`
    - `[participant]` **`berry-geometric-phase-theorist`** ← raw token: `Berry`
    - `[participant]` **`connes-ncg-theorist`** ← raw token: `Connes`
    - `[designated_writer]` **`baptista-spacetime-analyst`** ← raw token: `Baptista`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (6 total; 6 whitelist-ready, 0 need extension):
    - `participates_in`: 4
    - `synthesized_by`: 1
    - `cited_in`: 1

### 71. `session-24b-synthesis.md`

- **Path**: `sessions/archive/session-24/session-24b-synthesis.md`
- **Session**: S24 | **Generation**: G3 | **Size**: 25,773 B
- **Archetype**: `synthesis` — Synthesis document
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (3):
    - `[participant]` **`sagan-empiricist`** ← raw token: `sagan`
    - `[participant]` **`einstein-theorist`** ← raw token: `einstein`
    - `[participant]` **`orchestrator`** ← raw token: `coordinator`
- **Upstream chain refs** (1):
    - `[predecessor]` → `23`, `ainur-panel`, `sagan-empiricist`
- **Downstream consumers** (5):
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-31B-plan.md`
    - `sessions/session-plan/archive/session-31Bb-prompt.md`
    - `tools/equation-audit-findings.md`
    - `summary/Archives/session-24-final.md`
- **Recommended edges** (11 total; 11 whitelist-ready, 0 need extension):
    - `cited_in`: 5
    - `participates_in`: 3
    - `cites_prior_session`: 3

### 72. `session-29Ac-synthesis.md`

- **Path**: `sessions/archive/session-29/session-29Ac-synthesis.md`
- **Session**: S29 | **Generation**: G3 | **Size**: 25,623 B
- **Archetype**: `synthesis` — Synthesis document
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (4):
    - `[team_member]` **`hawking-theorist`** ← raw token: `hawking`
    - `[team_member]` **`orchestrator`** ← raw token: `coordinator`
    - `[team_member]` **`baptista-spacetime-analyst`** ← raw token: `baptista`
    - `[team_member]` **`tesla-resonance`** ← raw token: `Tesla-Resonance`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (3):
    - `sessions/archive/session-29/session-29-wrapup.md`
    - `sessions/archive/session-29/session-29Ac-workshop.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (7 total; 7 whitelist-ready, 0 need extension):
    - `participates_in`: 4
    - `cited_in`: 3

### 73. `session-54-phonon-landau-workshop-synthesis.md`

- **Path**: `sessions/archive/session-54/session-54-phonon-landau-workshop-synthesis.md`
- **Session**: S54 | **Generation**: G4 | **Size**: 25,392 B
- **Archetype**: `synthesis` — Synthesis document
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (2):
    - `[participant]` **`phonon-first-cosmologist`** ← raw token: `Phonon-First`
    - `[participant]` **`landau-condensed-matter-theorist`** ← raw token: `Landau`
- **Upstream chain refs** (1):
    - `[source]` → `54`, `nazarewicz-nuclear-structure-theorist`, `connes-ncg-theorist`
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (6 total; 6 whitelist-ready, 0 need extension):
    - `derived_from`: 3
    - `participates_in`: 2
    - `cited_in`: 1

### 74. `session-29Bb-synthesis.md`

- **Path**: `sessions/archive/session-29/session-29Bb-synthesis.md`
- **Session**: S29 | **Generation**: G3 | **Size**: 24,567 B
- **Archetype**: `synthesis` — Synthesis document
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (3):
    - `[participant]` **`baptista-spacetime-analyst`** ← raw token: `baptista`
    - `[participant]` **`landau-condensed-matter-theorist`** ← raw token: `landau`
    - `[participant]` **`orchestrator`** ← raw token: `coordinator`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (5):
    - `sessions/archive/session-29/session-29-wrapup.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-30B-prompt.md`
    - `sessions/session-plan/archive/session-30Ba-prompt.md`
    - `sessions/session-plan/archive/session-30Bb-prompt.md`
- **Recommended edges** (8 total; 8 whitelist-ready, 0 need extension):
    - `cited_in`: 5
    - `participates_in`: 3

### 75. `session-33b-synthesis.md`

- **Path**: `sessions/archive/session-33/session-33b-synthesis.md`
- **Session**: S33 | **Generation**: G3 | **Size**: 24,404 B
- **Archetype**: `synthesis` — Synthesis document
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (1):
    - `[participant]` **`sagan-empiricist`** ← raw token: `sagan`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (5):
    - `sessions/archive/session-33/session-33-tesla-collab.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-33b-prompt.md`
    - `sessions/session-plan/archive/session-34-plan.md`
    - `summary/Archives/session-33-final.md`
- **Recommended edges** (6 total; 6 whitelist-ready, 0 need extension):
    - `cited_in`: 5
    - `participates_in`: 1

### 76. `session-29-team-D-synthesis.md`

- **Path**: `sessions/archive/session-29/session-29-team-D-synthesis.md`
- **Session**: S29 | **Generation**: G3 | **Size**: 24,028 B
- **Archetype**: `team_synthesis` — Multi-agent team synthesis
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (4):
    - `[team_member]` **`dirac-antimatter-theorist`** ← raw token: `Dirac`
    - `[team_member]` **`neutrino-detection-specialist`** ← raw token: `Neutrino`
    - `[team_member]` **`hawking-theorist`** ← raw token: `Hawking`
    - `[designated_writer]` **`dirac-antimatter-theorist`** ← raw token: `Dirac`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (5 total; 5 whitelist-ready, 0 need extension):
    - `participates_in`: 3
    - `synthesized_by`: 1
    - `cited_in`: 1

### 77. `session-47-wayforward.md`

- **Path**: `sessions/archive/session-47/session-47-wayforward.md`
- **Session**: S47 | **Generation**: G4 | **Size**: 23,896 B
- **Archetype**: `wayforward` — Way-forward computation extraction
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `plans_next_session`
- **Authors extracted** (6):
    - `[participant]` **`landau-condensed-matter-theorist`** ← raw token: `Landau`
    - `[participant]` **`spectral-geometer`** ← raw token: `Spectral-Geometer`
    - `[participant]` **`volovik-superfluid-universe-theorist`** ← raw token: `Volovik`
    - `[primary]` **`landau-condensed-matter-theorist`** ← raw token: `Landau`
    - `[primary]` **`spectral-geometer`** ← raw token: `Spectral-Geometer`
    - `[primary]` **`volovik-superfluid-universe-theorist`** ← raw token: `Volovik`
- **Upstream chain refs** (5):
    - `[source]` → `47`
    - `[source]` → `47`
    - `[source]` → `47`
    - `[source]` → `47`
    - `[source]` → `nazarewicz-nuclear-structure-theorist`, `landau-condensed-matter-theorist`
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (13 total; 13 whitelist-ready, 0 need extension):
    - `derived_from`: 6
    - `participates_in`: 3
    - `authored_by`: 3
    - `cited_in`: 1

### 78. `session-29A-synthesis.md`

- **Path**: `sessions/archive/session-29/session-29A-synthesis.md`
- **Session**: S29 | **Generation**: G3 | **Size**: 23,397 B
- **Archetype**: `synthesis` — Synthesis document
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (1):
    - `[source]` → `einstein-theorist`
- **Downstream consumers** (3):
    - `sessions/archive/session-29/session-29-wrapup.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-29Ac-prompt.md`
- **Recommended edges** (4 total; 4 whitelist-ready, 0 need extension):
    - `cited_in`: 3
    - `derived_from`: 1

### 79. `session-63-wrapup.md`

- **Path**: `sessions/archive/session-63/session-63-wrapup.md`
- **Session**: S63 | **Generation**: G5 | **Size**: 22,830 B
- **Archetype**: `handoff` — Session-level handoff or wrap-up document
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `summarizes_session`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (2):
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `summary/session-63-final.md`
- **Recommended edges** (2 total; 2 whitelist-ready, 0 need extension):
    - `cited_in`: 2

### 80. `session-23b-synthesis.md`

- **Path**: `sessions/archive/session-23/session-23b-synthesis.md`
- **Session**: S23 | **Generation**: G3 | **Size**: 21,651 B
- **Archetype**: `synthesis` — Synthesis document
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (2):
    - `[participant]` **`sagan-empiricist`** ← raw token: `sagan-empiricist`
    - `[participant]` **`orchestrator`** ← raw token: `coordinator`
- **Upstream chain refs** (1):
    - `[predecessor]` → `ainur-panel`, `sagan-empiricist`
- **Downstream consumers** (10):
    - `sessions/archive/session-23/session-23-tesla-take-quantum-acoustics-collab.md`
    - `sessions/archive/session-23/session-23c-synthesis.md`
    - `sessions/archive/session-24/session-24b-synthesis.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-23b-prompt.md`
    - `sessions/session-plan/archive/session-23c-prompt.md`
    - `sessions/session-plan/archive/session-24-prompt.md`
    - `sessions/session-plan/archive/session-24b-prompt.md`
    - _(+2 more consumers omitted — see full JSON)_
- **Recommended edges** (14 total; 14 whitelist-ready, 0 need extension):
    - `cited_in`: 10
    - `participates_in`: 2
    - `cites_prior_session`: 2

### 81. `session-28-team-synthesis-c.md`

- **Path**: `sessions/archive/session-28/session-28-team-synthesis-c.md`
- **Session**: S28 | **Generation**: G3 | **Size**: 20,280 B
- **Archetype**: `team_synthesis` — Multi-agent team synthesis
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (4):
    - `[team_member]` **`neutrino-detection-specialist`** ← raw token: `Neutrino`
    - `[team_member]` **`landau-condensed-matter-theorist`** ← raw token: `Landau`
    - `[team_member]` **`paasch-mass-quantization-analyst`** ← raw token: `Paasch`
    - `[team_member]` **`orchestrator`** ← raw token: `Coordinator`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (5 total; 5 whitelist-ready, 0 need extension):
    - `participates_in`: 4
    - `cited_in`: 1

### 82. `session-29Ab-synthesis.md`

- **Path**: `sessions/archive/session-29/session-29Ab-synthesis.md`
- **Session**: S29 | **Generation**: G3 | **Size**: 19,871 B
- **Archetype**: `synthesis` — Synthesis document
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (4):
    - `[team_member]` **`phonon-first-cosmologist`** ← raw token: `phonon-exflation-sim`
    - `[team_member]` **`einstein-theorist`** ← raw token: `einstein-theorist`
    - `[team_member]` **`landau-condensed-matter-theorist`** ← raw token: `landau-condensed-matter-theorist`
    - `[team_member]` **`orchestrator`** ← raw token: `coordinator`
- **Upstream chain refs** (2):
    - `[source]` → `einstein-theorist`
    - `[source]` → `einstein-theorist`
- **Downstream consumers** (5):
    - `sessions/archive/session-29/session-29-wrapup.md`
    - `sessions/archive/session-29/session-29A-synthesis.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-29Ab-prompt.md`
    - `sessions/session-plan/archive/session-29Ac-prompt.md`
- **Recommended edges** (11 total; 11 whitelist-ready, 0 need extension):
    - `cited_in`: 5
    - `participates_in`: 4
    - `derived_from`: 2

### 83. `session-28-team-synthesis-a.md`

- **Path**: `sessions/archive/session-28/session-28-team-synthesis-a.md`
- **Session**: S28 | **Generation**: G3 | **Size**: 19,682 B
- **Archetype**: `team_synthesis` — Multi-agent team synthesis
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (4):
    - `[participant]` **`dirac-antimatter-theorist`** ← raw token: `Dirac`
    - `[participant]` **`feynman-theorist`** ← raw token: `Feynman`
    - `[participant]` **`schwarzschild-penrose-geometer`** ← raw token: `Schwarzschild-Penrose`
    - `[designated_writer]` **`feynman-theorist`** ← raw token: `Feynman`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (3):
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-29Aa-prompt.md`
    - `sessions/session-plan/archive/session-29Ab-prompt.md`
- **Recommended edges** (7 total; 7 whitelist-ready, 0 need extension):
    - `participates_in`: 3
    - `cited_in`: 3
    - `synthesized_by`: 1

### 84. `session-34a-synthesis.md`

- **Path**: `sessions/archive/session-34/session-34a-synthesis.md`
- **Session**: S34 | **Generation**: G3 | **Size**: 19,295 B
- **Archetype**: `synthesis` — Synthesis document
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (7):
    - `sessions/archive/session-34/session-34-master-synthesis.md`
    - `sessions/archive/session-34/session-34-synthesis.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-34a-prompt.md`
    - `sessions/session-plan/archive/session-34b-prompt.md`
    - `sessions/session-plan/archive/session-34c-prompt.md`
    - `summary/Archives/session-34-final.md`
- **Recommended edges** (7 total; 7 whitelist-ready, 0 need extension):
    - `cited_in`: 7

### 85. `session-66-wrapup.md`

- **Path**: `sessions/archive/session-66/session-66-wrapup.md`
- **Session**: S66 | **Generation**: G5 | **Size**: 19,116 B
- **Archetype**: `handoff` — Session-level handoff or wrap-up document
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `summarizes_session`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (2):
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `summary/session-66-final.md`
- **Recommended edges** (2 total; 2 whitelist-ready, 0 need extension):
    - `cited_in`: 2

### 86. `session-30Bb-synthesis.md`

- **Path**: `sessions/archive/session-30/session-30Bb-synthesis.md`
- **Session**: S30 | **Generation**: G3 | **Size**: 18,871 B
- **Archetype**: `synthesis` — Synthesis document
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (2):
    - `[participant]` **`einstein-theorist`** ← raw token: `einstein`
    - `[participant]` **`orchestrator`** ← raw token: `coordinator`
- **Upstream chain refs** (1):
    - `[source]` → `einstein-theorist`
- **Downstream consumers** (2):
    - `sessions/framework/Collabs/string-theory-synthesis.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (5 total; 5 whitelist-ready, 0 need extension):
    - `participates_in`: 2
    - `cited_in`: 2
    - `derived_from`: 1

### 87. `session-29ba-synthesis.md`

- **Path**: `sessions/archive/session-29/session-29ba-synthesis.md`
- **Session**: S29 | **Generation**: G3 | **Size**: 18,503 B
- **Archetype**: `synthesis` — Synthesis document
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (2):
    - `[participant]` **`neutrino-detection-specialist`** ← raw token: `neutrino`
    - `[participant]` **`orchestrator`** ← raw token: `coordinator`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (5):
    - `sessions/archive/session-29/session-29-wrapup.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-30B-prompt.md`
    - `sessions/session-plan/archive/session-30Ba-prompt.md`
    - `sessions/session-plan/archive/session-30Bb-prompt.md`
- **Recommended edges** (7 total; 7 whitelist-ready, 0 need extension):
    - `cited_in`: 5
    - `participates_in`: 2

### 88. `session-19d-synthesis.md`

- **Path**: `sessions/archive/session-19/session-19d-synthesis.md`
- **Session**: S19 | **Generation**: G3 | **Size**: 17,708 B
- **Archetype**: `synthesis` — Synthesis document
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (4):
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-20a-prompt.md`
    - `sessions/session-plan/archive/session-20b-prompt.md`
    - `sessions/session-plan/archive/session-20c-prompt.md`
- **Recommended edges** (4 total; 4 whitelist-ready, 0 need extension):
    - `cited_in`: 4

### 89. `session-26-wrapup.md`

- **Path**: `sessions/archive/session-26/session-26-wrapup.md`
- **Session**: S26 | **Generation**: G3 | **Size**: 16,051 B
- **Archetype**: `handoff` — Session-level handoff or wrap-up document
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `summarizes_session`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (1 total; 1 whitelist-ready, 0 need extension):
    - `cited_in`: 1

### 90. `session-67-synthesis.md`

- **Path**: `sessions/archive/session-67/session-67-synthesis.md`
- **Session**: S67 | **Generation**: G5 | **Size**: 15,956 B
- **Archetype**: `synthesis` — Synthesis document
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (4):
    - `sessions/archive/session-67/session-67-transit-phonon-first-workshop.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-68-context.md`
    - `summary/session-67-final.md`
- **Recommended edges** (4 total; 4 whitelist-ready, 0 need extension):
    - `cited_in`: 4

### 91. `session-25-graceful-handoff.md`

- **Path**: `sessions/archive/session-25/session-25-graceful-handoff.md`
- **Session**: S25 | **Generation**: G3 | **Size**: 15,776 B
- **Archetype**: `handoff` — Session-level handoff or wrap-up document
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `summarizes_session`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (1 total; 1 whitelist-ready, 0 need extension):
    - `cited_in`: 1

### 92. `session-29Aa-synthesis.md`

- **Path**: `sessions/archive/session-29/session-29Aa-synthesis.md`
- **Session**: S29 | **Generation**: G3 | **Size**: 14,876 B
- **Archetype**: `synthesis` — Synthesis document
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (3):
    - `[team_member]` **`phonon-first-cosmologist`** ← raw token: `phonon-exflation-sim`
    - `[team_member]` **`hawking-theorist`** ← raw token: `hawking-theorist`
    - `[team_member]` **`orchestrator`** ← raw token: `coordinator`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (6):
    - `sessions/archive/session-29/session-29-wrapup.md`
    - `sessions/archive/session-29/session-29A-synthesis.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-29Aa-prompt.md`
    - `sessions/session-plan/archive/session-29Ab-prompt.md`
    - `sessions/session-plan/archive/session-29Ac-prompt.md`
- **Recommended edges** (9 total; 9 whitelist-ready, 0 need extension):
    - `cited_in`: 6
    - `participates_in`: 3

### 93. `session-16-combined-handout.md`

- **Path**: `sessions/archive/session-16/session-16-combined-handout.md`
- **Session**: S16 | **Generation**: G2 | **Size**: 13,061 B
- **Archetype**: `combined_handout` — Combined handout (multi-format synthesis)
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (2):
    - `[author]` **`meme-pi`** ← raw token: `Meme`
    - `[author]` **`claude`** ← raw token: `Claude`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (3 total; 3 whitelist-ready, 0 need extension):
    - `authored_by`: 2
    - `cited_in`: 1

### 94. `session-37-handoff.md`

- **Path**: `sessions/archive/session-37/session-37-handoff.md`
- **Session**: S37 | **Generation**: G4 | **Size**: 12,320 B
- **Archetype**: `handoff` — Session-level handoff or wrap-up document
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `summarizes_session`
- **Authors extracted** (6):
    - `[participant]` **`spectral-geometer`** ← raw token: `spectral-geometer`
    - `[participant]` **`neutrino-detection-specialist`** ← raw token: `neutrino`
    - `[participant]` **`nazarewicz-nuclear-structure-theorist`** ← raw token: `nazarewicz`
    - `[participant]` **`feynman-theorist`** ← raw token: `feynman`
    - `[participant]` **`einstein-theorist`** ← raw token: `einstein`
    - `[participant]` **`landau-condensed-matter-theorist`** ← raw token: `landau`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (2):
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `summary/Archives/session-37-final.md`
- **Recommended edges** (8 total; 8 whitelist-ready, 0 need extension):
    - `participates_in`: 6
    - `cited_in`: 2

### 95. `session-54-nazarewicz-connes-workshop-synthesis.md`

- **Path**: `sessions/archive/session-54/session-54-nazarewicz-connes-workshop-synthesis.md`
- **Session**: S54 | **Generation**: G4 | **Size**: 12,302 B
- **Archetype**: `synthesis` — Synthesis document
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (2):
    - `[participant]` **`nazarewicz-nuclear-structure-theorist`** ← raw token: `Nazarewicz`
    - `[participant]` **`connes-ncg-theorist`** ← raw token: `Connes`
- **Upstream chain refs** (1):
    - `[source]` → `54`
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (4 total; 4 whitelist-ready, 0 need extension):
    - `participates_in`: 2
    - `derived_from`: 1
    - `cited_in`: 1

### 96. `session-48-wayforward.md`

- **Path**: `sessions/archive/session-48/session-48-wayforward.md`
- **Session**: S48 | **Generation**: G4 | **Size**: 10,403 B
- **Archetype**: `wayforward` — Way-forward computation extraction
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `plans_next_session`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (1 total; 1 whitelist-ready, 0 need extension):
    - `cited_in`: 1

### 97. `session-40-handoff.md`

- **Path**: `sessions/archive/session-40/session-40-handoff.md`
- **Session**: S40 | **Generation**: G4 | **Size**: 10,089 B
- **Archetype**: `handoff` — Session-level handoff or wrap-up document
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `summarizes_session`
- **Authors extracted** (1):
    - `[participant]` **`gen-physicist`** ← raw token: `gen-physicist`
- **Upstream chain refs** (1):
    - `[source]` → `39`
- **Downstream consumers** (4):
    - `sessions/archive/session-40/session-40-results-workingpaper.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-40-plan.md`
    - `summary/Archives/session-40-final.md`
- **Recommended edges** (6 total; 6 whitelist-ready, 0 need extension):
    - `cited_in`: 4
    - `participates_in`: 1
    - `derived_from`: 1

### 98. `session-71-synthesis.md`

- **Path**: `sessions/archive/session-71/session-71-synthesis.md`
- **Session**: S71 | **Generation**: G5 | **Size**: 9,262 B
- **Archetype**: `synthesis` — Synthesis document
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (2):
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `summary/session-71-final.md`
- **Recommended edges** (2 total; 2 whitelist-ready, 0 need extension):
    - `cited_in`: 2

### 99. `session-53-connes-nazarewicz-workshop-synthesis.md`

- **Path**: `sessions/archive/session-53/session-53-connes-nazarewicz-workshop-synthesis.md`
- **Session**: S53 | **Generation**: G4 | **Size**: 8,305 B
- **Archetype**: `synthesis` — Synthesis document
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (3):
    - `[synthesizer]` **`orchestrator`** ← raw token: `Team-lead`
    - `[filename_derived]` **`connes-ncg-theorist`** ← raw token: `filename:connes`
    - `[filename_derived]` **`nazarewicz-nuclear-structure-theorist`** ← raw token: `filename:nazarewicz`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (2):
    - `sessions/archive/session-53/session-53-phonon-hawking-workshop.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (5 total; 5 whitelist-ready, 0 need extension):
    - `authored_by`: 2
    - `cited_in`: 2
    - `synthesized_by`: 1

### 100. `session-53-baptista-volovik-workshop-synthesis.md`

- **Path**: `sessions/archive/session-53/session-53-baptista-volovik-workshop-synthesis.md`
- **Session**: S53 | **Generation**: G4 | **Size**: 8,178 B
- **Archetype**: `synthesis` — Synthesis document
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (3):
    - `[synthesizer]` **`orchestrator`** ← raw token: `Team-lead`
    - `[filename_derived]` **`baptista-spacetime-analyst`** ← raw token: `filename:baptista`
    - `[filename_derived]` **`volovik-superfluid-universe-theorist`** ← raw token: `filename:volovik`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (3):
    - `sessions/archive/session-53/session-53-connes-nazarewicz-workshop.md`
    - `sessions/archive/session-53/session-53-phonon-hawking-workshop.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (6 total; 6 whitelist-ready, 0 need extension):
    - `cited_in`: 3
    - `authored_by`: 2
    - `synthesized_by`: 1

### 101. `session-49-wayforward.md`

- **Path**: `sessions/archive/session-49/session-49-wayforward.md`
- **Session**: S49 | **Generation**: G4 | **Size**: 7,566 B
- **Archetype**: `wayforward` — Way-forward computation extraction
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `plans_next_session`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (2):
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-50-plan.md`
- **Recommended edges** (2 total; 2 whitelist-ready, 0 need extension):
    - `cited_in`: 2

### 102. `session-53-phonon-hawking-workshop-synthesis.md`

- **Path**: `sessions/archive/session-53/session-53-phonon-hawking-workshop-synthesis.md`
- **Session**: S53 | **Generation**: G4 | **Size**: 7,558 B
- **Archetype**: `synthesis` — Synthesis document
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (2):
    - `[synthesizer]` **`orchestrator`** ← raw token: `Team-lead`
    - `[filename_derived]` **`hawking-theorist`** ← raw token: `filename:hawking`
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (3 total; 3 whitelist-ready, 0 need extension):
    - `synthesized_by`: 1
    - `authored_by`: 1
    - `cited_in`: 1

### 103. `session-24a-synthesis.md`

- **Path**: `sessions/archive/session-24/session-24a-synthesis.md`
- **Session**: S24 | **Generation**: G3 | **Size**: 6,379 B
- **Archetype**: `synthesis` — Synthesis document
- **Status**: `MULTI-AUTHOR`
- **Primary edge type**: `synthesizes`
- **Authors extracted** (1):
    - `[participant]` **`orchestrator`** ← raw token: `coordinator`
- **Upstream chain refs** (1):
    - `[predecessor]` → `23`, `ainur-panel`, `sagan-empiricist`
- **Downstream consumers** (3):
    - `sessions/archive/session-24/session-24b-synthesis.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `summary/Archives/session-24-final.md`
- **Recommended edges** (7 total; 7 whitelist-ready, 0 need extension):
    - `cites_prior_session`: 3
    - `cited_in`: 3
    - `participates_in`: 1

## Status: `ORPHAN-PROMOTED` (52 files)

No author extracted but the file has a chain (upstream sources OR downstream consumers). The chain edges (`derived_from` / `cited_in` / `feeds_into`) are recommended for emission. Filename-pattern attribution may be derivable for some (e.g., `*-connes.md` → `connes-ncg-theorist`).

### 104. `session-84-w10-workingpaper.md`

- **Path**: `sessions/archive/session-84/session-84-w10-workingpaper.md`
- **Session**: S84 | **Generation**: G7 | **Size**: 172,920 B
- **Archetype**: `wave_subdocument` — Wave-prefixed sub-document
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `discussed_in`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (13):
    - `sessions/archive/session-84/session-84-s1-connes-alpha_s-synthesis.md`
    - `sessions/archive/session-84/session-84-s1-landau-alpha_s-synthesis.md`
    - `sessions/archive/session-84/session-84-s1-mack-alpha_s-synthesis.md`
    - `sessions/archive/session-84/session-84-s3-kaku-elimination-synthesis.md`
    - `sessions/archive/session-84/session-84-s4-lrd-falsifier-synthesis.md`
    - `sessions/archive/session-84/session-84-s5-connes-cohomology-synthesis.md`
    - `sessions/archive/session-84/session-84-s5-lizzi-cohomology-synthesis.md`
    - `sessions/archive/session-84/session-84-s5-vdd-cohomology-synthesis.md`
    - _(+5 more consumers omitted — see full JSON)_
- **Recommended edges** (13 total; 13 whitelist-ready, 0 need extension):
    - `cited_in`: 13

### 105. `session-84-w2-workingpaper.md`

- **Path**: `sessions/archive/session-84/session-84-w2-workingpaper.md`
- **Session**: S84 | **Generation**: G7 | **Size**: 154,137 B
- **Archetype**: `wave_subdocument` — Wave-prefixed sub-document
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `discussed_in`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (5):
    - `sessions/archive/session-84/session-84-synthesis-collation.md`
    - `sessions/archive/session-84/session-84-workshop-schedule.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `computations/session-84/s84_w2b_pin_derivation_census.md`
    - `summary/session-84-final.md`
- **Recommended edges** (5 total; 5 whitelist-ready, 0 need extension):
    - `cited_in`: 5

### 106. `session-84-w4-workingpaper.md`

- **Path**: `sessions/archive/session-84/session-84-w4-workingpaper.md`
- **Session**: S84 | **Generation**: G7 | **Size**: 152,321 B
- **Archetype**: `wave_subdocument` — Wave-prefixed sub-document
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `discussed_in`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (7):
    - `sessions/permanent-results-registry.md`
    - `sessions/archive/session-84/session-84-s3-kaku-elimination-synthesis.md`
    - `sessions/archive/session-84/session-84-s4-lrd-falsifier-synthesis.md`
    - `sessions/archive/session-84/session-84-synthesis-collation.md`
    - `sessions/archive/session-84/session-84-workshop-schedule.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `summary/session-84-final.md`
- **Recommended edges** (7 total; 7 whitelist-ready, 0 need extension):
    - `cited_in`: 7

### 107. `session-84-w7-workingpaper.md`

- **Path**: `sessions/archive/session-84/session-84-w7-workingpaper.md`
- **Session**: S84 | **Generation**: G7 | **Size**: 146,712 B
- **Archetype**: `wave_subdocument` — Wave-prefixed sub-document
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `discussed_in`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (7):
    - `sessions/permanent-results-registry.md`
    - `sessions/archive/session-84/session-84-s3-kaku-elimination-synthesis.md`
    - `sessions/archive/session-84/session-84-synthesis-collation.md`
    - `sessions/archive/session-84/session-84-workshop-schedule.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `computations/session-84/s84_w7b_83_landing_block.md`
    - `summary/session-84-final.md`
- **Recommended edges** (7 total; 7 whitelist-ready, 0 need extension):
    - `cited_in`: 7

### 108. `session-86-w0c-workingpaper.md`

- **Path**: `sessions/archive/session-86/session-86-w0c-workingpaper.md`
- **Session**: S86 | **Generation**: G7 | **Size**: 115,375 B
- **Archetype**: `workingpaper` — Wave working paper (gate-anchored)
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `authored_by`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (5):
    - `sessions/archive/session-86/session-86-workshop-schedule.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/archive/session-86/seeds/_seed-w0c.md`
    - `sessions/archive/session-86/workshops/s86-r-dual-pathway-bk-array-and-nT.md`
    - `sessions/archive/session-86/workshops/session-86-1a-s3-lizzi.md`
- **Recommended edges** (5 total; 5 whitelist-ready, 0 need extension):
    - `cited_in`: 5

### 109. `session-52-phonon-workshop.md`

- **Path**: `sessions/archive/session-52/session-52-phonon-workshop.md`
- **Session**: S52 | **Generation**: G4 | **Size**: 109,880 B
- **Archetype**: `workshop` — Workshop transcript
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `discussed_in`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (1 total; 1 whitelist-ready, 0 need extension):
    - `cited_in`: 1

### 110. `session-84-w3-workingpaper.md`

- **Path**: `sessions/archive/session-84/session-84-w3-workingpaper.md`
- **Session**: S84 | **Generation**: G7 | **Size**: 106,906 B
- **Archetype**: `wave_subdocument` — Wave-prefixed sub-document
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `discussed_in`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (6):
    - `sessions/permanent-results-registry.md`
    - `sessions/archive/session-84/session-84-synthesis-collation.md`
    - `sessions/archive/session-84/session-84-tesla-phononic-engine-precursor.md`
    - `sessions/archive/session-84/session-84-workshop-schedule.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `summary/session-84-final.md`
- **Recommended edges** (6 total; 6 whitelist-ready, 0 need extension):
    - `cited_in`: 6

### 111. `session-84-w6-workingpaper.md`

- **Path**: `sessions/archive/session-84/session-84-w6-workingpaper.md`
- **Session**: S84 | **Generation**: G7 | **Size**: 104,923 B
- **Archetype**: `wave_subdocument` — Wave-prefixed sub-document
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `discussed_in`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (10):
    - `sessions/archive/session-84/session-84-s1-connes-alpha_s-synthesis.md`
    - `sessions/archive/session-84/session-84-s1-landau-alpha_s-synthesis.md`
    - `sessions/archive/session-84/session-84-s1-mack-alpha_s-synthesis.md`
    - `sessions/archive/session-84/session-84-s2-volovik-kcorridor-synthesis.md`
    - `sessions/archive/session-84/session-84-s3-kaku-elimination-synthesis.md`
    - `sessions/archive/session-84/session-84-s4-lrd-falsifier-synthesis.md`
    - `sessions/archive/session-84/session-84-synthesis-collation.md`
    - `sessions/archive/session-84/session-84-workshop-schedule.md`
    - _(+2 more consumers omitted — see full JSON)_
- **Recommended edges** (10 total; 10 whitelist-ready, 0 need extension):
    - `cited_in`: 10

### 112. `session-74-rf-analysis.md`

- **Path**: `sessions/archive/session-74/session-74-rf-analysis.md`
- **Session**: S74 | **Generation**: G5 | **Size**: 59,396 B
- **Archetype**: `retrospective_analysis` — Retrospective analysis dossier
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `analyzes`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (5):
    - `sessions/archive/session-74/session-74-luxe-pre-registration.md`
    - `sessions/archive/session-74/session-74-tgf-pre-registration.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `tools/mcp-servers/madrigal-mcp/README.md`
    - `summary/session-74-final.md`
- **Recommended edges** (5 total; 5 whitelist-ready, 0 need extension):
    - `cited_in`: 5

### 113. `DIA-investigation-schedule.md`

- **Path**: `sessions/archive/session-91/DIA-investigation-schedule.md`
- **Session**: S91 | **Generation**: G7 | **Size**: 57,946 B
- **Archetype**: `plan` — Session phase plan
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `plans_session`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (1 total; 1 whitelist-ready, 0 need extension):
    - `cited_in`: 1

### 114. `session-54-extraction-collabs.md`

- **Path**: `sessions/archive/session-54/session-54-extraction-collabs.md`
- **Session**: S54 | **Generation**: G4 | **Size**: 48,372 B
- **Archetype**: `extraction` — Extraction document
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `extracted_from`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (78):
    - `[source]` → `tesla-resonance`
    - `[source]` → `tesla-resonance`
    - `[source]` → `tesla-resonance`
    - `[source]` → `tesla-resonance`
    - `[source]` → `tesla-resonance`
    - `[source]` → `tesla-resonance`
    - `[source]` → `tesla-resonance`
    - `[source]` → `tesla-resonance`
    - _(+70 more refs omitted for readability — see full JSON)_
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (89 total; 89 whitelist-ready, 0 need extension):
    - `derived_from`: 65
    - `feeds_into`: 23
    - `cited_in`: 1

### 115. `s88-w3-w1b1-63-3branch.md`

- **Path**: `sessions/archive/session-88/workshops/s88-w3-w1b1-63-3branch.md`
- **Session**: S88 | **Generation**: G7 | **Size**: 46,086 B
- **Archetype**: `workshop` — Workshop transcript or output
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `discussed_in`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (1):
    - `[source]` → `88`, `computations/session-88/s88_gate_verdicts.txt`
- **Downstream consumers** (3):
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/archive/session-89/workshops/s89-w1-alpha-m-corridor-selection.md`
    - `sessions/session-plan/archive/session-89-plan-w1.md`
- **Recommended edges** (5 total; 5 whitelist-ready, 0 need extension):
    - `cited_in`: 3
    - `derived_from`: 2

### 116. `session-43-quicklook.md`

- **Path**: `sessions/archive/session-43/session-43-quicklook.md`
- **Session**: S43 | **Generation**: G4 | **Size**: 45,059 B
- **Archetype**: `quicklook` — Quicklook session summary
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `summarizes_session`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (1):
    - `[predecessor]` → `42`
- **Downstream consumers** (2):
    - `sessions/archive/session-43/s43_cc_113_workshop.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (3 total; 3 whitelist-ready, 0 need extension):
    - `cited_in`: 2
    - `cites_prior_session`: 1

### 117. `session-33-w1-math-permanence.md`

- **Path**: `sessions/archive/session-33/session-33-w1-math-permanence.md`
- **Session**: S33 | **Generation**: G3 | **Size**: 42,111 B
- **Archetype**: `wave_subdocument` — Wave-prefixed sub-document
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `discussed_in`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (1):
    - `[source]` → `33`, `32`
- **Downstream consumers** (6):
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-33-plan.md`
    - `sessions/session-plan/archive/session-33-w1-math-permanence-prompt.md`
    - `sessions/session-plan/archive/session-33a-prompt.md`
    - `sessions/session-plan/archive/session-33b-prompt.md`
    - `sessions/session-plan/archive/session-34-plan.md`
- **Recommended edges** (8 total; 8 whitelist-ready, 0 need extension):
    - `cited_in`: 6
    - `derived_from`: 2

### 118. `session-16-round-3a-computational.md`

- **Path**: `sessions/archive/session-16/session-16-round-3a-computational.md`
- **Session**: S16 | **Generation**: G2 | **Size**: 41,987 B
- **Archetype**: `round_discussion` — Multi-round discussion transcript
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `discussed_in`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (4):
    - `sessions/archive/session-16/session-16-orchestration-state.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-16-workshop-agenda.md`
    - `tools/math-issues-audit.md`
- **Recommended edges** (4 total; 4 whitelist-ready, 0 need extension):
    - `cited_in`: 4

### 119. `session-16-round-3c-priorities.md`

- **Path**: `sessions/archive/session-16/session-16-round-3c-priorities.md`
- **Session**: S16 | **Generation**: G2 | **Size**: 39,467 B
- **Archetype**: `round_discussion` — Multi-round discussion transcript
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `discussed_in`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (3):
    - `sessions/archive/session-16/session-16-orchestration-state.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-16-workshop-agenda.md`
- **Recommended edges** (3 total; 3 whitelist-ready, 0 need extension):
    - `cited_in`: 3

### 120. `session-45-quicklook.md`

- **Path**: `sessions/archive/session-45/session-45-quicklook.md`
- **Session**: S45 | **Generation**: G4 | **Size**: 38,763 B
- **Archetype**: `quicklook` — Quicklook session summary
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `summarizes_session`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (1):
    - `[predecessor]` → `44`
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (2 total; 2 whitelist-ready, 0 need extension):
    - `cites_prior_session`: 1
    - `cited_in`: 1

### 121. `s88-w1-substrate-clock-cancellation.md`

- **Path**: `sessions/archive/session-88/workshops/s88-w1-substrate-clock-cancellation.md`
- **Session**: S88 | **Generation**: G7 | **Size**: 34,389 B
- **Archetype**: `wave_subdocument` — Wave-prefixed sub-document
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `discussed_in`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (3):
    - `sessions/archive/session-89/session-89-w3-workingpaper.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-89-plan-w3.md`
- **Recommended edges** (3 total; 3 whitelist-ready, 0 need extension):
    - `cited_in`: 3

### 122. `session-16-round-2b-dk-generations.md`

- **Path**: `sessions/archive/session-16/session-16-round-2b-dk-generations.md`
- **Session**: S16 | **Generation**: G2 | **Size**: 34,062 B
- **Archetype**: `round_discussion` — Multi-round discussion transcript
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `discussed_in`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (6):
    - `sessions/archive/session-16/session-16-orchestration-state.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-16-workshop-agenda.md`
    - `sessions/session-plan/archive/session-17a-prompt.md`
    - `sessions/session-plan/archive/session-17b-prompt.md`
    - `tools/equation-audit-findings.md`
- **Recommended edges** (6 total; 6 whitelist-ready, 0 need extension):
    - `cited_in`: 6

### 123. `session-54-extraction-workshops.md`

- **Path**: `sessions/archive/session-54/session-54-extraction-workshops.md`
- **Session**: S54 | **Generation**: G4 | **Size**: 33,161 B
- **Archetype**: `extraction` — Extraction document
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `extracted_from`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (49):
    - `[source]` → `nazarewicz-nuclear-structure-theorist`, `connes-ncg-theorist`, `landau-condensed-matter-theorist`, `quantum-acoustics-theorist`, `hawking-theorist`
    - `[source]` → `nazarewicz-nuclear-structure-theorist`, `connes-ncg-theorist`, `landau-condensed-matter-theorist`
    - `[source]` → `nazarewicz-nuclear-structure-theorist`, `connes-ncg-theorist`, `landau-condensed-matter-theorist`
    - `[source]` → `nazarewicz-nuclear-structure-theorist`, `connes-ncg-theorist`, `landau-condensed-matter-theorist`
    - `[source]` → `nazarewicz-nuclear-structure-theorist`, `connes-ncg-theorist`
    - `[source]` → `nazarewicz-nuclear-structure-theorist`, `connes-ncg-theorist`
    - `[source]` → `nazarewicz-nuclear-structure-theorist`, `connes-ncg-theorist`
    - `[source]` → `quantum-acoustics-theorist`, `hawking-theorist`
    - _(+41 more refs omitted for readability — see full JSON)_
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (91 total; 91 whitelist-ready, 0 need extension):
    - `derived_from`: 84
    - `feeds_into`: 6
    - `cited_in`: 1

### 124. `session-16-round-2c-theory.md`

- **Path**: `sessions/archive/session-16/session-16-round-2c-theory.md`
- **Session**: S16 | **Generation**: G2 | **Size**: 31,165 B
- **Archetype**: `round_discussion` — Multi-round discussion transcript
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `discussed_in`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (4):
    - `sessions/archive/session-16/session-16-orchestration-state.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-16-workshop-agenda.md`
    - `tools/equation-audit-findings.md`
- **Recommended edges** (4 total; 4 whitelist-ready, 0 need extension):
    - `cited_in`: 4

### 125. `s88-w2-kz-universality-class.md`

- **Path**: `sessions/archive/session-88/workshops/s88-w2-kz-universality-class.md`
- **Session**: S88 | **Generation**: G7 | **Size**: 31,065 B
- **Archetype**: `wave_subdocument` — Wave-prefixed sub-document
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `discussed_in`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (1):
    - `[source]` → `88`
- **Downstream consumers** (3):
    - `sessions/archive/session-89/session-89-w3-workingpaper.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-89-plan-w3.md`
- **Recommended edges** (4 total; 4 whitelist-ready, 0 need extension):
    - `cited_in`: 3
    - `derived_from`: 1

### 126. `s64-collab-extraction.md`

- **Path**: `sessions/archive/session-64/s64-collab-extraction.md`
- **Session**: S64 | **Generation**: G5 | **Size**: 29,951 B
- **Archetype**: `extraction` — Extraction document
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `extracted_from`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (2):
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-65-context.md`
- **Recommended edges** (2 total; 2 whitelist-ready, 0 need extension):
    - `cited_in`: 2

### 127. `session-44-quicklook.md`

- **Path**: `sessions/archive/session-44/session-44-quicklook.md`
- **Session**: S44 | **Generation**: G4 | **Size**: 29,779 B
- **Archetype**: `quicklook` — Quicklook session summary
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `summarizes_session`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (1):
    - `[predecessor]` → `43`
- **Downstream consumers** (2):
    - `sessions/archive/session-44/session-44-quicklook-sp-collab.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (3 total; 3 whitelist-ready, 0 need extension):
    - `cited_in`: 2
    - `cites_prior_session`: 1

### 128. `s64-synthesis-extraction.md`

- **Path**: `sessions/archive/session-64/s64-synthesis-extraction.md`
- **Session**: S64 | **Generation**: G5 | **Size**: 28,221 B
- **Archetype**: `extraction` — Extraction document
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `extracted_from`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (2):
    - `[source]` → `61`, `64`
    - `[source_files]` → `64`
- **Downstream consumers** (2):
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-65-context.md`
- **Recommended edges** (5 total; 5 whitelist-ready, 0 need extension):
    - `derived_from`: 3
    - `cited_in`: 2

### 129. `session-68-phonon-vs-data-plan.md`

- **Path**: `sessions/archive/session-68/session-68-phonon-vs-data-plan.md`
- **Session**: S68 | **Generation**: G5 | **Size**: 28,084 B
- **Archetype**: `plan` — Session phase plan
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `plans_session`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (3):
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-69-plan.md`
    - `summary/session-68-final.md`
- **Recommended edges** (3 total; 3 whitelist-ready, 0 need extension):
    - `cited_in`: 3

### 130. `session-46-quicklook.md`

- **Path**: `sessions/archive/session-46/session-46-quicklook.md`
- **Session**: S46 | **Generation**: G4 | **Size**: 25,339 B
- **Archetype**: `quicklook` — Quicklook session summary
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `summarizes_session`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (1):
    - `[predecessor]` → `45`
- **Downstream consumers** (6):
    - `sessions/archive/session-46/session-46-quicklook-dirac-collab.md`
    - `sessions/archive/session-46/session-46-quicklook-hawking-collab.md`
    - `sessions/archive/session-46/session-46-quicklook-paasch-collab.md`
    - `sessions/archive/session-46/session-46-quicklook-qa-collab.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-46-wave5.md`
- **Recommended edges** (7 total; 7 whitelist-ready, 0 need extension):
    - `cited_in`: 6
    - `cites_prior_session`: 1

### 131. `session-16-round-1c-computation.md`

- **Path**: `sessions/archive/session-16/session-16-round-1c-computation.md`
- **Session**: S16 | **Generation**: G2 | **Size**: 24,394 B
- **Archetype**: `round_discussion` — Multi-round discussion transcript
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `discussed_in`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (3):
    - `sessions/archive/session-16/session-16-orchestration-state.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-16-workshop-agenda.md`
- **Recommended edges** (3 total; 3 whitelist-ready, 0 need extension):
    - `cited_in`: 3

### 132. `s65-collab-extraction-for-s66.md`

- **Path**: `sessions/archive/session-65/s65-collab-extraction-for-s66.md`
- **Session**: S65 | **Generation**: G5 | **Size**: 23,182 B
- **Archetype**: `extraction` — Extraction document
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `extracted_from`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (1):
    - `[source]` → `lizzi-spectral-functional-theorist`
- **Downstream consumers** (3):
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-66-context.md`
    - `summary/session-65-final.md`
- **Recommended edges** (4 total; 4 whitelist-ready, 0 need extension):
    - `cited_in`: 3
    - `derived_from`: 1

### 133. `session-16-round-1b-spectrum.md`

- **Path**: `sessions/archive/session-16/session-16-round-1b-spectrum.md`
- **Session**: S16 | **Generation**: G2 | **Size**: 22,723 B
- **Archetype**: `round_discussion` — Multi-round discussion transcript
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `discussed_in`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (3):
    - `sessions/archive/session-16/session-16-orchestration-state.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-16-workshop-agenda.md`
- **Recommended edges** (3 total; 3 whitelist-ready, 0 need extension):
    - `cited_in`: 3

### 134. `session-56-vol-collab.md`

- **Path**: `sessions/archive/session-56/session-56-vol-collab.md`
- **Session**: S56 | **Generation**: G4 | **Size**: 22,497 B
- **Archetype**: `solo_collab_review` — Solo collaborative review
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `reviews`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (3):
    - `sessions/archive/session-56/session-56-workshop-2-cc-formula.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `summary/session-56-final.md`
- **Recommended edges** (3 total; 3 whitelist-ready, 0 need extension):
    - `cited_in`: 3

### 135. `session-19d-LeadResearcher-Collab.md`

- **Path**: `sessions/archive/session-19/session-19d-LeadResearcher-Collab.md`
- **Session**: S19 | **Generation**: G3 | **Size**: 20,344 B
- **Archetype**: `lead_researcher_collab` — Lead researcher solo collab
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `authored_by`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (1 total; 1 whitelist-ready, 0 need extension):
    - `cited_in`: 1

### 136. `session-19d-casimir-energy.md`

- **Path**: `sessions/archive/session-19/session-19d-casimir-energy.md`
- **Session**: S19 | **Generation**: G3 | **Size**: 19,117 B
- **Archetype**: `sub_session_compute` — Sub-session computation
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `authored_by`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (8):
    - `sessions/archive/session-19/session-19d-baptista-collab.md`
    - `sessions/archive/session-19/session-19d-berry-collab.md`
    - `sessions/archive/session-19/session-19d-connes-collab.md`
    - `sessions/archive/session-19/session-19d-einstein-collab.md`
    - `sessions/archive/session-19/session-19d-landau-collab.md`
    - `sessions/archive/session-19/session-19d-sagan-collab.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-20-thesis.md`
- **Recommended edges** (8 total; 8 whitelist-ready, 0 need extension):
    - `cited_in`: 8

### 137. `session-50-oz-investigation-prompts.md`

- **Path**: `sessions/archive/session-50/session-50-oz-investigation-prompts.md`
- **Session**: S50 | **Generation**: G4 | **Size**: 17,573 B
- **Archetype**: `investigation_prompts` — Investigation prompts catalog
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `indexes`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (2):
    - `sessions/permanent-results-registry.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (2 total; 2 whitelist-ready, 0 need extension):
    - `cited_in`: 2

### 138. `session-19a-spectral-diagnostics.md`

- **Path**: `sessions/archive/session-19/session-19a-spectral-diagnostics.md`
- **Session**: S19 | **Generation**: G3 | **Size**: 17,162 B
- **Archetype**: `sub_session_compute` — Sub-session computation
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `authored_by`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (2):
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-19d-prompt.md`
- **Recommended edges** (2 total; 2 whitelist-ready, 0 need extension):
    - `cited_in`: 2

### 139. `session-28b-results.md`

- **Path**: `sessions/archive/session-28/session-28b-results.md`
- **Session**: S28 | **Generation**: G3 | **Size**: 17,110 B
- **Archetype**: `results_summary` — Session results summary
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `summarizes_session`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (1 total; 1 whitelist-ready, 0 need extension):
    - `cited_in`: 1

### 140. `session-26-priority-3.md`

- **Path**: `sessions/archive/session-26/session-26-priority-3.md`
- **Session**: S26 | **Generation**: G3 | **Size**: 16,114 B
- **Archetype**: `priority_computation` — Numbered priority computation
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `authored_by`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (1 total; 1 whitelist-ready, 0 need extension):
    - `cited_in`: 1

### 141. `session-28a-results.md`

- **Path**: `sessions/archive/session-28/session-28a-results.md`
- **Session**: S28 | **Generation**: G3 | **Size**: 15,619 B
- **Archetype**: `results_summary` — Session results summary
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `summarizes_session`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (1 total; 1 whitelist-ready, 0 need extension):
    - `cited_in`: 1

### 142. `session-28c-results.md`

- **Path**: `sessions/archive/session-28/session-28c-results.md`
- **Session**: S28 | **Generation**: G3 | **Size**: 14,691 B
- **Archetype**: `results_summary` — Session results summary
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `summarizes_session`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (4):
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-29Aa-prompt.md`
    - `sessions/session-plan/archive/session-30A-prompt.md`
    - `sessions/session-plan/archive/session-30Aa-prompt.md`
- **Recommended edges** (4 total; 4 whitelist-ready, 0 need extension):
    - `cited_in`: 4

### 143. `session-16-round-1a-geometry.md`

- **Path**: `sessions/archive/session-16/session-16-round-1a-geometry.md`
- **Session**: S16 | **Generation**: G2 | **Size**: 13,192 B
- **Archetype**: `round_discussion` — Multi-round discussion transcript
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `discussed_in`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (4):
    - `sessions/archive/session-16/session-16-orchestration-state.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-16-workshop-agenda.md`
    - `tools/equation-audit-findings.md`
- **Recommended edges** (4 total; 4 whitelist-ready, 0 need extension):
    - `cited_in`: 4

### 144. `session-62-two-wrongs-excursion.md`

- **Path**: `sessions/archive/session-62/session-62-two-wrongs-excursion.md`
- **Session**: S62 | **Generation**: G5 | **Size**: 9,953 B
- **Archetype**: `excursion` — Session excursion / deep-investigation
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `authored_by`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (2):
    - `sessions/archive/session-62/session-62-sp-phonon-workshop.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (2 total; 2 whitelist-ready, 0 need extension):
    - `cited_in`: 2

### 145. `session-56-workshop-teams.md`

- **Path**: `sessions/archive/session-56/session-56-workshop-teams.md`
- **Session**: S56 | **Generation**: G4 | **Size**: 8,970 B
- **Archetype**: `workshop_teams` — Workshop team assignment
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `organizes_workshops`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (1):
    - `[source]` → `56`
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (2 total; 2 whitelist-ready, 0 need extension):
    - `derived_from`: 1
    - `cited_in`: 1

### 146. `session-61-results.md`

- **Path**: `sessions/archive/session-61/session-61-results.md`
- **Session**: S61 | **Generation**: G5 | **Size**: 8,876 B
- **Archetype**: `results_summary` — Session results summary
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `summarizes_session`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (5):
    - `sessions/archive/session-61/session-61-string-shadow-review.md`
    - `sessions/archive/session-61/session-61-wave7-workingpaper.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-62-plan.md`
    - `summary/session-61-final.md`
- **Recommended edges** (5 total; 5 whitelist-ready, 0 need extension):
    - `cited_in`: 5

### 147. `session-17b-verification.md`

- **Path**: `sessions/archive/session-17/session-17b-verification.md`
- **Session**: S17 | **Generation**: G2 | **Size**: 8,760 B
- **Archetype**: `phase_layer` — Phase 1/2 layer artifact (S17 era)
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `authored_by`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (1 total; 1 whitelist-ready, 0 need extension):
    - `cited_in`: 1

### 148. `s45_tinfoil_minus068.md`

- **Path**: `sessions/archive/session-45/s45_tinfoil_minus068.md`
- **Session**: S45 | **Generation**: G4 | **Size**: 8,613 B
- **Archetype**: `tinfoil_investigation` — Tinfoil-hat investigation
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `investigates`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (2):
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/session-plan/archive/session-46-wave2.md`
- **Recommended edges** (2 total; 2 whitelist-ready, 0 need extension):
    - `cited_in`: 2

### 149. `session-34-scratchpad.md`

- **Path**: `sessions/archive/session-34/session-34-scratchpad.md`
- **Session**: S34 | **Generation**: G3 | **Size**: 8,527 B
- **Archetype**: `scratchpad` — Investigation scratchpad
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `scratchpad_for`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (4):
    - `sessions/archive/session-34/session-34-master-synthesis.md`
    - `sessions/archive/session-34/session-34-synthesis.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `summary/Archives/session-34-final.md`
- **Recommended edges** (4 total; 4 whitelist-ready, 0 need extension):
    - `cited_in`: 4

### 150. `s79-pause-resume.md`

- **Path**: `sessions/archive/session-79/s79-pause-resume.md`
- **Session**: S79 | **Generation**: G6 | **Size**: 7,535 B
- **Archetype**: `pause_resume` — Pause/resume artifact
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `continues_session`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (5):
    - `sessions/archive/session-79/session-79-final.md`
    - `sessions/archive/session-80/session-80-results-workingpaper.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `summary/session-79-final.md`
    - `summary/session-80-final.md`
- **Recommended edges** (5 total; 5 whitelist-ready, 0 need extension):
    - `cited_in`: 5

### 151. `session-17a-foundation.md`

- **Path**: `sessions/archive/session-17/session-17a-foundation.md`
- **Session**: S17 | **Generation**: G2 | **Size**: 6,903 B
- **Archetype**: `phase_layer` — Phase 1/2 layer artifact (S17 era)
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `authored_by`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (1 total; 1 whitelist-ready, 0 need extension):
    - `cited_in`: 1

### 152. `s79-phase-plan.md`

- **Path**: `sessions/archive/session-79/s79-phase-plan.md`
- **Session**: S79 | **Generation**: G6 | **Size**: 6,776 B
- **Archetype**: `plan` — Session phase plan
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `plans_session`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (7):
    - `sessions/archive/session-79/s79-pause-resume.md`
    - `sessions/archive/session-79/session-79-final.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `sessions/archive/session-79/workshops/p2-a-as-ledger-dissonance.md`
    - `sessions/archive/session-79/workshops/p2-b-pbh-prefold-wrong-sign.md`
    - `sessions/archive/session-79/workshops/p2-c-desi-mechanism-split.md`
    - `summary/session-79-final.md`
- **Recommended edges** (7 total; 7 whitelist-ready, 0 need extension):
    - `cited_in`: 7

### 153. `s45_addendum_hose_count_ns.md`

- **Path**: `sessions/archive/session-45/s45_addendum_hose_count_ns.md`
- **Session**: S45 | **Generation**: G4 | **Size**: 4,516 B
- **Archetype**: `addendum` — Session addendum
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `addendum_to`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (1):
    - `[source]` → `45`, `user`, `orchestrator`
- **Downstream consumers** (3):
    - `sessions/archive/session-45/session-45-quicklook.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `summary/Archives/session-45-quicklook.md`
- **Recommended edges** (6 total; 6 whitelist-ready, 0 need extension):
    - `derived_from`: 3
    - `cited_in`: 3

### 154. `s84-w9a-98-settings-diff.md`

- **Path**: `sessions/archive/session-84/s84-w9a-98-settings-diff.md`
- **Session**: S84 | **Generation**: G7 | **Size**: 2,338 B
- **Archetype**: `settings_diff` — Settings.json wiring diff
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `configures`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (4):
    - `sessions/archive/session-84/session-84-w9-workingpaper.md`
    - `sessions/archive/session-84/session-84-workshop-schedule.md`
    - `sessions/framework/registry/orphan-chain-analysis.md`
    - `summary/session-84-final.md`
- **Recommended edges** (4 total; 4 whitelist-ready, 0 need extension):
    - `cited_in`: 4

### 155. `s45_addendum_forward_backward_ns.md`

- **Path**: `sessions/archive/session-45/s45_addendum_forward_backward_ns.md`
- **Session**: S45 | **Generation**: G4 | **Size**: 2,284 B
- **Archetype**: `addendum` — Session addendum
- **Status**: `ORPHAN-PROMOTED`
- **Primary edge type**: `addendum_to`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (1):
    - `[source]` → `45`, `user`
- **Downstream consumers** (1):
    - `sessions/framework/registry/orphan-chain-analysis.md`
- **Recommended edges** (3 total; 3 whitelist-ready, 0 need extension):
    - `derived_from`: 2
    - `cited_in`: 1

## Status: `HISTORICAL-ONLY` (1 files)

No author, no chain detected. Likely scratchpad / one-off artifact / early-format fragment with no current consumer. Leave in archive.

### 156. `session-19d-LeadResearcher-Collab (raw).md`

- **Path**: `sessions/archive/session-19/session-19d-LeadResearcher-Collab (raw).md`
- **Session**: S19 | **Generation**: G3 | **Size**: 10,918 B
- **Archetype**: `lead_researcher_collab` — Lead researcher solo collab
- **Status**: `HISTORICAL-ONLY`
- **Primary edge type**: `authored_by`
- **Authors extracted** (0):
    - _(none extracted; attribution may be implicit per archetype or absent by design)_
- **Upstream chain refs** (0):
    - _(no upstream refs detected)_
- **Downstream consumers** (0):
    - _(no downstream consumers detected via corpus inbound-link index)_
- **Recommended edges** (0 total; 0 whitelist-ready, 0 need extension):

---

## Promotion guidance

To promote the REGEX-FIXED + MULTI-AUTHOR attributions into the production graph:

1. **Sync patterns**: copy the extended attribution regex set from `tools/_orphan_chain_investigator.py` (`RE_TEAM`, `RE_AGENTS_LIST`, `RE_PARTICIPANTS`, `RE_DESIGNATED_WRITER`, `RE_SYNTH`, `RE_ASSESSOR`, `RE_AUDITOR`, `RE_LEAD`, `RE_RESEARCHER`, `RE_TAG_BRACKET`, `RE_H2_AUTHOR`, `RE_H2_PARTICIPANTS`, `RE_H2_MULTI_AUTHOR`) into `tools/_format_generation_regex_set.py::FIXTURES` with verbatim positive-test snippets. Self-test must stay PASS.
2. **Sync aliases**: merge the orphan-only canonical aliases (`meme-pi`, `claude`, `ainur-panel`, `team-lead` → `orchestrator`, etc.) into `tools/_format_generation_regex_set.py::AGENT_ALIASES`. Watch for the `sim-specialist`/`team-lead` parity gotchas documented in the investigator.
3. **Allow bullet-prefix attribution lines**: update the harvester's per-pattern anchors from `^\s*\*\*` to `^[-*\s]*\*\*` to permit bullet-list forms like `- **Agents**: ...`.
4. **Scan window extension**: for synthesis-archetype files (synergy_index, framework_synergy, team_synthesis, fusion_synthesis, master_collab), scan the FULL FILE for attribution rather than head-N lines. Per-section `**Researcher**:` and bracket-tag attributions live in the body, not the header.
5. **Re-run the harvester** (`tools/harvest_attribution_edges.py`) and verify edge count growth.
6. **Run `/weave --update`** to ingest the new edges into `knowledge.db`.

Per-orphan edge proposals are recorded in `tools/_orphan_chain_analysis.json::results[*].recommended_edges`. Each carries `in_whitelist: bool` indicating whether the type is currently auto-emittable.

---

## Cross-references

- Watchlist row table: `sessions/framework/registry/orphan-content-watchlist.md`
- Investigator JSON: `tools/_orphan_chain_analysis.json`
- Investigator source: `tools/_orphan_chain_investigator.py`
- Format-generation spec: `sessions/framework/registry/session-format-generations.md`
- Production harvester: `tools/harvest_attribution_edges.py`
- Edge-type whitelist: `tools/extract_entities.py::EDGE_TYPE_CANONICAL`
