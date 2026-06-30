# LRD Observational Constraints Registry

**Registry ID**: `lrd-observational-constraints`
**Owner agent(s)**: `little-red-dots-jwst-analyst`
**Last updated**: `2026-04-23, S85-W4 AMRI migration`
**Ingestion**: `/weave --update`; `knowledge.db` stores rows under `closed | open` per entry status.

---

## Scope

Observational constraints on Little Red Dots (LRDs) extracted from the `researchers/Little-Red-Dots/` paper corpus. Project-level observational data — any framework agent (mack, hawking, sagan, tesla, phononic-engine analysts) may consume these when modeling high-redshift compact sources.

Promoted from `.claude/agent-memory/little-red-dots-jwst-analyst/MEMORY.md` § Key Observational Constraints (AMRI per cross-agent-overlap potential + table-content heuristic; no live consumer gate currently cites the memory location, but content is project-scope by nature).

---

## Summary table

| Constraint | Value | Source paper(s) |
|:-----------|:------|:----------------|
| LRD number density | 10^{−5} to 10^{−4} cMpc^{−3}, z ≈ 4–8 | Papers 01, 04, 14 |
| BH masses (virial, naive) | 10^6 – 10^9 M_⊙ | Papers 01, 03, 05 |
| BH masses (e-scattering corrected) | 10^5 – 10^7 M_⊙ | Paper 15 (Rusakov) |
| X-ray weakness | 100 – 10,000× below L_X–L_Hα | Paper 06 |
| Radio non-detections | ~95% undetected | Paper 10 |
| ALMA dust upper limit | M_dust < 10^6 M_⊙ | Paper 19 |
| Variability | 97.5% non-variable | Paper 18 |
| Host galaxies | 1/8 detected, 10–100× below local scaling | Paper 22 |
| "Too massive too early" tension | 1–2σ after Rusakov + Li corrections | Papers 15, 38, 40 |

Paper corpus: `researchers/Little-Red-Dots/` (66 papers + `AGENTS.md` + `index.md`). Full structured index at `researchers/Little-Red-Dots/index.md`.

---

## Consumer gates

| Gate ID | Session | Role | Notes |
|:--------|:--------|:-----|:------|
| (none current) | — | — | No live S85 gate reads this registry as Input-SHA; project-level reference only |

---

## Change log

| Date | Session | Change | Author |
|:-----|:--------|:-------|:-------|
| 2026-04-23 | S85-W4 AMRI | Initial migration from LRD agent memory | orchestrator |

---

## Migration notes

- Pre-migration path: `.claude/agent-memory/little-red-dots-jwst-analyst/MEMORY.md` § Key Observational Constraints
- AMRI tests fired: content-scope analysis (observational data sourced from cited papers, multi-agent consumable)
- Pointer installed in memory: `> See sessions/framework/registry/lrd-observational-constraints.md (AMRI-promoted 2026-04-23; was § Key Observational Constraints)`

---

## Post-S85 refresh (S110 W0a; mack-cosmic-bridge cosmological-liaison annotation; investigation-distillation HK-LRD-REFRESH, inv-7 HY2)

The S85-W4 migration table above is the baseline observational snapshot. Post-S85 (the S99 JWST-LRD literature campaign + the S100 LRD seeding-fork work) sharpens the LRD constraint picture along five axes — these are observational REFINEMENTS (not value retractions of the baseline table), surfaced by the S99-S100 investigation distillation:

| Refinement axis | Post-S85 status | Source |
|:----------------|:----------------|:-------|
| **Split-state tension** | The "too massive too early" tension is now read as a SPLIT-STATE: the virial-naive BH masses (10⁶–10⁹ M_⊙) vs the e-scattering-corrected masses (10⁵–10⁷ M_⊙, Rusakov) span ~2 dex; the tension is 1–2σ after the Rusakov + Li corrections, NOT the order-of-magnitude crisis the naive masses imply | Papers 15, 38, 40 (baseline rows); S99 litrev-jwst-lrd-mack |
| **Compton-thick** | The X-ray weakness (100–10,000× below L_X–L_Hα) is consistent with heavily Compton-thick obscuration (a buried AGN), NOT necessarily a missing/under-massive BH — a degenerate interpretation the X-ray null alone cannot break | Paper 06 (baseline); S99 litrev |
| **Dust-free** | The ALMA dust upper limit (M_dust < 10⁶ M_⊙) + the optical/UV continuum shape favor a DUST-FREE or dust-poor interpretation — disfavoring the "dusty starburst masquerading as AGN" reading for the population | Paper 19 (baseline); S99 litrev |
| **Non-variable** | The 97.5% non-variability is a strong constraint: it disfavors a standard luminous-accretion-disk AGN (which would vary) for most of the population — consistent with either super-Eddington slim-disk states or non-AGN interpretations | Paper 18 (baseline); S99 litrev |
| **Three-interpretation triage** | The population is best read as a THREE-way triage — (i) genuinely overmassive BHs (heavy seeds), (ii) Compton-thick obscured normal-mass AGN, (iii) non-AGN (dense stellar / dust-reprocessed) — no single interpretation fits all LRDs; the framework's heavy-seed channel (a₂-channel gas-dynamical collapse, gravitational only, NO annihilation thermostat) addresses interpretation (i) | S99 litrev consolidation §III.F; S100b W7-2 OPEN-side |

**Framework liaison note (substrate-first).** The framework's LRD-seeding contribution is the a₂-channel gas-dynamical heavy-seed route (Row #78 SMDS-fork CLOSED-to-framework on the annihilating-DM side; Row #72/#78 OPEN-side gas-dynamical consistency at S100b W7-2 PASS — `M_seed = 1.993e5 M_⊙`, atomic-cooling-halo). The framework participates in interpretation (i) gravitationally (the Leggett-channel DM is non-annihilating, CPT-neutral — NO super-massive-dark-star annihilation thermostat); it makes NO claim on interpretations (ii)/(iii). Direction (`phononic-framing.md`): `D_K → Leggett channel (non-annihilating) → a₂ gravitational collapse → heavy seed → JWST LRD progenitor` — the gas-dynamical DCBH picture is the laboratory-IN restatement of the substrate-IS coherent collapse.

## n_PBH-vs-LRD citation discipline (S110 W0a; HK-ROW88 cross-annotation; mack-cosmic-bridge sole-writer for the falsifier-surface side)

The framework's substrate-IS PBH number density `n_PBH` (`falsifier-master-inventory.md` Row #65 + §VII.AX.OP-PROJ) must NOT be conflated with the LRD-population observational constraints in the table above:

- **`n_PBH = 7.2761e-23 m⁻³` (T1.13, L_max=14) is NOT a clean LRD prediction** — it is the HELD dimensionful Level-3 magnitude on a truncation-DIVERGENT cardinality channel (NON-PROMOTION-BY-HELD-NUMBER, `dimensionful-slot-collision`; §VII.AX.OP-PROJ). Cite it ONLY with the held qualifier, NEVER as a clean substrate-derived LRD-population density.
- **`n_PBH = 1.758e-23 m⁻³` is the honest saturation-freeze provisional** (g-saturation, L_max-independent) — the value to cite when a single number is needed.
- The LRD number density (10⁻⁵–10⁻⁴ cMpc⁻³, baseline table) is the OBSERVATIONAL LRD constraint; the substrate `n_PBH` is a DISTINCT PBH-formation prediction (the cascade-tail channel), not a fit to the LRD density.
- **"Row #88"** in the falsifier inventory is the COMPACT-OBJECT-SECTOR GAP record (S107), NOT an n_PBH/LRD forward label — do not cite it as a live LRD prediction row.

Provenance: HK-ROW88 + HK-LRD-REFRESH investigation-distillation (S110 W0a); cross-refs `falsifier-master-inventory.md` Row #65.audit-S110-HELD-NUMBER-HYGIENE + `permanent-results-registry.md §VII.AX.OP-PROJ`. Per `feedback_mack-bridge-role.md` (mack-cosmic-bridge sole writer of the falsifier-surface; this LRD-registry annotation is the cosmological-liaison cross-reference, with `little-red-dots-jwst-analyst` the primary owner of the observational table).
