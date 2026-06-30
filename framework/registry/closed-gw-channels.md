# Closed GW-Detection Channels (LRD-origin)

**Registry ID**: `closed-gw-channels`
**Owner agent(s)**: `little-red-dots-jwst-analyst` (origin), `tesla-resonance` (GW-physics), `mack-cosmic-bridge` (detector-reach)
**Last updated**: `2026-04-23, S85-W4 AMRI migration`
**Ingestion**: `/weave --update`; entries are `closed` mechanisms (structural eliminations of GW-detection channels).
**Status**: **STAGING** — this file is a migration-target for AMRI content that needs formal promotion into `sessions/permanent-results-registry.md` § V (Closed Mechanisms) with full source-SHA pins. Future session should formalize each row with the originating gate verdict.

---

## Scope

Gravitational-wave-detection channels that have been eliminated (structurally, observationally, or by parameter exclusion) for the framework. Promoted from `.claude/agent-memory/little-red-dots-jwst-analyst/MEMORY.md` § Closed Channels (factual) (AMRI — content is project-level closure data accumulated by the LRD analyst but never registered to `permanent-results-registry.md`).

The Anderson-Higgs row is already represented as Item 16 in `sessions/permanent-results-registry.md`; this file cites the derived consequence for GW discussion.

---

## Summary table

| Channel | Closure type | Basis | Registry status |
|:--------|:-------------|:------|:----------------|
| `cosmic_strings_Gmu_exclusion` | observational | Gμ ~ 10^{−4} excluded by Planck (limit 1.5 × 10^{−7}); BKT suppresses vortex production (exp(−708)) | STAGING — add to permanent-results-registry § V |
| `U(1)_7_global_Goldstone_not_GW` | structural consequence | U(1)_7 is global (Anderson-Higgs closed S51, permanent-results-registry Item 16) → strings radiate Goldstone, not GW | derived from permanent-results-registry Item 16 |
| `domain_wall_GW_GUT_GHz` | frequency mismatch | GUT-scale annihilation → GHz; LISA requires TeV-scale; no mechanism | STAGING |
| `KZ_defects_0D_quench` | structural | 0D quench (L/ξ_GL = 0.031); spatially homogeneous; no structure seeding | STAGING |
| `internal_domain_walls_not_4D` | structural | CG(24) fiber objects, not 4D-spacetime objects | STAGING |
| `PBH_from_strings_light_seeds` | parameter-bound consequence | At CMB-allowed Gμ, M_PBH ~ 200 M_⊙ (light seeds only) | STAGING |
| `LRD_demographics_not_discriminating` | observational degeneracy | Cannot discriminate framework from ΛCDM at z < 10^28 | STAGING |

---

## Entry detail

### `cosmic_strings_Gmu_exclusion`
- **Claim**: cosmic-string tension Gμ ~ 10^{−4} excluded
- **Basis**: Planck upper limit 1.5 × 10^{−7} on Gμ; BKT suppression factor exp(−708) on vortex production
- **Consequence**: cosmic-string GW background from the framework's candidate mechanism is below all current and planned detector sensitivities

### `U(1)_7_global_Goldstone_not_GW`
- **Claim**: U(1)_7 is a global symmetry, not gauge
- **Basis**: Anderson-Higgs Impossibility Theorem, S51 — see `sessions/permanent-results-registry.md` Item 16 and § V row W8
- **Consequence**: strings radiate massless Goldstone bosons, not gravitational waves

### `domain_wall_GW_GUT_GHz`
- **Claim**: framework's domain-wall annihilation produces GW at GHz frequencies
- **Basis**: energy-scale argument (GUT-scale annihilation ↦ peak f ~ GHz via f_0 ~ T_ann · T_0 / M_Pl)
- **Consequence**: LISA/PTA band requires T_ann ~ TeV (LISA) or ~MeV (PTA); framework has no mechanism at these scales

### `KZ_defects_0D_quench`
- **Claim**: Kibble-Zurek defect formation produces 0D (point-like) defects, not extended structure
- **Basis**: L/ξ_GL = 0.031 (correlation-length ratio); quench is spatially homogeneous
- **Consequence**: no cosmic structure seeding from KZ channel

### `internal_domain_walls_not_4D`
- **Claim**: internal domain walls are CG(24) fiber-geometric objects, not 4D-spacetime objects
- **Consequence**: do not participate in 4D gravitational dynamics; cannot produce detectable GW

### `PBH_from_strings_light_seeds`
- **Claim**: PBH formation from cosmic strings at CMB-allowed Gμ produces only light seeds
- **Basis**: at Gμ bound, M_PBH ~ 200 M_⊙
- **Consequence**: does not solve supermassive-BH seeding; does not contribute to LRD demographics at required scales

### `LRD_demographics_not_discriminating`
- **Claim**: LRD observational demographics cannot distinguish framework from ΛCDM
- **Basis**: discrimination threshold z > 10^28, far beyond any observable redshift
- **Consequence**: LRD data cannot falsify or confirm framework DM/structure predictions

---

## Surviving GW channel (cross-reference, NOT closed)

- **CASCADE-DYN-37** — if cascade saddle maps to T ~ 1–100 TeV, LISA-band GW possible. UNCOMPUTED since S37. Tracked in `sessions/framework/framework-bbn-hypothesis.md` and `sessions/evoi-framework.md`.

---

## Consumer gates

| Gate ID | Session | Role | Notes |
|:--------|:--------|:-----|:------|
| (none current) | — | — | Registry used as project-level reference; no live S85 gate reads as Input-SHA |

---

## Change log

| Date | Session | Change | Author |
|:-----|:--------|:-------|:-------|
| 2026-04-23 | S85-W4 AMRI | Initial migration from LRD agent memory § Closed Channels (factual) | orchestrator |

---

## Migration notes

- Pre-migration path: `.claude/agent-memory/little-red-dots-jwst-analyst/MEMORY.md` § Closed Channels (factual)
- AMRI tests fired: cross-agent potential overlap (Tesla, Mack would cite these closures) + content-scope
- Pointer installed in memory: `> See sessions/framework/registry/closed-gw-channels.md (AMRI-promoted 2026-04-23; was § Closed Channels (factual))`
- **Follow-up**: future session to promote each row into `sessions/permanent-results-registry.md` § V with originating-session SHA pins
