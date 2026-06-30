# Framework Dark-Matter Properties (Leggett-channel)

**Registry ID**: `framework-dm-properties`
**Owner agent(s)**: `little-red-dots-jwst-analyst` (origin), `mack-cosmic-bridge` (cosmological-liaison)
**Last updated**: `2026-04-23, S85-W4 AMRI migration`
**Ingestion**: `/weave --update`; entries are framework-derived properties (not raw observational data).

---

## Scope

The Leggett-channel dark-matter properties the framework produces — f_DM partition, transfer function T(k), effective warm-DM mass, free-streaming horizon. Promoted from `.claude/agent-memory/little-red-dots-jwst-analyst/MEMORY.md` § Framework DM Properties (AMRI per project-scope content classification; no framework file currently canonicalized these values).

---

## Summary table

| Property | Value | Basis |
|:---------|:------|:------|
| `f_DM` (two-channel) | Leggett + dimer_Z2 = 0.006 + 0.27 = **0.276** ≈ Ω_DM (0.2657) | S74 mack-landau workshop two-channel partition (supersedes the stale 3-channel→0.844 framing) |
| `T(k)` | 1.0000 at all observable scales | CDM-like transfer function across probed range |
| `m_WDM` | ~10^20 keV | 19 OOM above Lyman-α floor |
| `z_tr` (free-streaming horizon) | 6.75 × 10^29 | 22 OOM margin above any structure-formation relevant scale |

---

## Entry detail

### Two-channel `f_DM` partition (S74 mack-landau workshop; S110 W0a refresh)

**The DM-channel partition is TWO channels, summing NEAR Ω_DM** (supersedes the stale "f_DM = 0.209 Leggett-only vs 0.844 observed / SOLE BOTTLENECK" framing — that framing used the WRONG observed target 0.844 and omitted the dimer_Z2 channel):

| Channel | f-contribution | Mechanism |
|:--------|:---------------|:----------|
| **Leggett** | f_Leggett ≈ 0.006 | Leggett inter-band coherence mode (gap-massed, CPT-neutral, non-annihilating, N_pair-superselection-protected); the PROVEN DM mass anchor (LEGGETT-MOMENT-70) |
| **dimer_Z2** | f_dimer_Z2 ≈ 0.27 | Z₂ dimer Parker-pair production (the dominant DM-abundance channel) |
| **DM total** | **f_DM = 0.006 + 0.27 = 0.276** | two-channel sum |

- **Observed target**: `Ω_DM = 0.2657` (Planck 2018, `canonical_constants.py`; `get_constant` verified).
- **Match**: the two-channel sum `0.276` lands **~3.9% above** Ω_DM (0.2657) — NEAR-saturation, NOT an exact match (the dimer_Z2 `≈ 0.27` is itself an approximate channel-fraction; the ~3.9% residual is honest, not claimed-exact). This is a substantial improvement over the stale "factor ≈ 4× shortfall" reading, which was an artifact of the wrong-target (0.844) + missing-channel framing.
- **The soft-hair channel goes to DARK ENERGY, NOT dark matter**: `f_DE = f_soft-hair + f_effacement = 0.20 + 0.03 = 0.23` (the soft-hair contribution is a DE channel; the old framing that lumped a soft-hair term toward a "3-channel→0.844 DM" reconstruction conflated the DM and DE sectors). The exploratory 3-channel reconstruction `f_DM = f_Leggett + f_soft-hair + f_dimer_Z2` (investigation-8-plan-w1) is the EXPLORATORY form; the S74 workshop two-channel partition (Leggett+dimer for DM, soft-hair for DE) is the corrected reading.
- **Abundance vs density-parameter**: the Leggett-channel relic abundance `Ω_DM h² = 0.120` (0.6% from Planck 0.1186±0.0020; LEGGETT-MOMENT-70) is the ABUNDANCE statement; the two-channel `f_DM = 0.276 ≈ Ω_DM = 0.2657` is the DENSITY-PARAMETER partition statement — distinct quantities (the h²-weighted relic abundance vs the fractional density).
- **Session anchor**: S58 (Volovik partition origin) → S74 (two-channel mack-landau partition) → S110 W0a (this refresh, supersedes the stale single-channel framing). Source: `sessions/archive/session-74/session-74-mack-landau-workshop.md` (`f_DM = f_Leggett + f_dimer_Z2 = 0.006 + 0.27 = 0.276`; `f_DE = f_soft-hair + f_effacement = 0.20 + 0.03 = 0.23`).

### `T(k) = 1.0000` across observable scales
- **Interpretation**: the Leggett channel is CDM-like on probed scales; no small-scale transfer suppression
- **Falsifier absence**: no small-scale cut in T(k) means the channel is currently indistinguishable from CDM on observable k

### `m_WDM ~ 10^20 keV` and `z_tr = 6.75 × 10^29`
- Effective WDM mass is 19 orders above Lyman-α bound (10 keV floor); free-streaming horizon is 22 orders above structure-formation scales
- **Consequence**: the Leggett channel does not behave as warm DM for any observational purpose

---

## Consumer gates

| Gate ID | Session | Role | Notes |
|:--------|:--------|:-----|:------|
| (none current) | — | — | Referenced implicitly in framework docs; not a live Input-SHA for any S85 gate |

---

## Change log

| Date | Session | Change | Author |
|:-----|:--------|:-------|:-------|
| 2026-04-23 | S85-W4 AMRI | Initial migration from LRD agent memory | orchestrator |

---

## Migration notes

- Pre-migration path: `.claude/agent-memory/little-red-dots-jwst-analyst/MEMORY.md` § Framework DM Properties
- AMRI tests fired: content-scope analysis (framework-derived values, not LRD-specific methodology)
- Pointer installed in memory: `> See sessions/framework/framework-dm-properties.md (AMRI-promoted 2026-04-23; was § Framework DM Properties)`
