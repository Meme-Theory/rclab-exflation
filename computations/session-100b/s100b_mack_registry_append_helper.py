# -*- coding: utf-8 -*-
"""
S100b mack-cosmic-bridge sole-writer registry append helper (plan-freeze batch).

Single-shot open("a") append-helper per registry-write hygiene
(.claude/rules/epistemic-discipline.md s"Registry-Write Hygiene"): appends the
S99-litreview-derived sections to the two mack sole-writer registries.

NOT a computation gate: no verdict line is emitted, no framework prediction
VALUE is produced (canonical write-order verdict->constants->inventory does
NOT apply -- these are qualitative falsifier rows + annotations on existing
canonicals). No canonical_constants import needed: this script computes
nothing; every number in the appended text is an EXISTING pinned value cited
with its provenance (knowledge-MCP verified 2026-06-06 in-session).

Targets (mack-cosmic-bridge sole writer per feedback_mack-bridge-role.md):
  1. sessions/framework/registry/falsifier-master-inventory.md
       - NEW Row #78 (S100-SMDS-DARK-STAR-FORK registry row)
       - S100b litreview-batch annotations (Row #70.audit KiDS-Legacy +
         VII.AF.1/VII.W index-legend caveat)
  2. sessions/framework/registry/falsifier-watchlist.md
       - S100b anchor-currency annotations (w_0/w_a post-Dovekie audit-pin +
         H_0 LIVE-PENDING/TDCOSMO-2025 audit-pin)

Idempotency guard: refuses to append if the section marker already exists.
"""

import io
import os
import sys

ROOT = r"C:\sandbox\Ainulindale Exflation"  # (local)
INVENTORY = os.path.join(ROOT, "sessions", "framework", "registry",
                         "falsifier-master-inventory.md")  # (local)
WATCHLIST = os.path.join(ROOT, "sessions", "framework", "registry",
                         "falsifier-watchlist.md")  # (local)

INVENTORY_MARKER = "## NEW Row #78 "  # (local)
WATCHLIST_MARKER = "## S100b litreview anchor-currency annotations"  # (local)

INVENTORY_APPEND = '''

## NEW Row #78 — S100-SMDS-DARK-STAR-FORK: annihilating-DM supermassive-dark-star LRD seeding channel CLOSED-to-framework (S99 litreview G8 seeding fork; PHYSICS-level discriminator; mack-cosmic-bridge sole-writer landing)

> **Origin**: S99 litreview campaign, G8 JWST-LRD sweep — consolidation `sessions/archive/session-99/session-99-litreview-consolidated-gen-physicist.md` §III.F (Tension F) + §II G8-1 + §V routing row ("G8-1 → registry/inventory row → mack-cosmic-bridge"); source reports `sessions/archive/session-99/session-99-litrev-jwst-lrd-mack.md` §II.1 + §IV + §V.1 (mack) and the little-red-dots pair report (CONVERGENT). Landed at S100b plan-freeze per `sessions/session-100b/session-100b-housekeeping.md` capstone-hygiene Q2/Q5 routing (mack-cosmic-bridge sole-writer batch per `feedback_mack-bridge-role.md`, AMRI-PROMOTED 2026-04-28).
> **REGISTRY ROW, NOT a compute gate**: `S100-SMDS-DARK-STAR-FORK` is the consolidation's row label, not a gate ID — the litreview campaign produced review reports only (NO verdict line exists or is emitted), and NO new framework prediction VALUE is produced, so the canonical write-order (verdict → canonical_constants → inventory; `math-scripts.md`) does NOT apply. The row surfaces EXISTING PROVEN DM-interaction properties (`LEGGETT-MOMENT-70`; baseline `Annihilation = 0` PASS, `baseline-findings-s66.md`) at a NEW observational channel: the seed-formation-epoch dark-star spectral signature. Knowledge-MCP anchors verified non-superseded 2026-06-06: `Mass_LeggettDM_over_Delta_BCS = 11.97` (S70 LEGGETT-MOMENT-70, S96-pinned; CONDITIONAL on Γ_grav < H_0 per Row #68); `LRD_demographics_not_discriminating` (closed_mechanism, STAGING, `closed-gw-channels.md`).
> **PHYSICS-level declaration (MANDATORY per the consolidation)**: this is the ONE LRD-group channel that ESCAPES the `LRD_demographics_not_discriminating` z < 10²⁸ demographics wall, because it tests the DM INTERACTION property (annihilating vs non-annihilating), NOT an assembly/demographics count. Every other G8 channel (papers 01–05, 07–10) is a consistency CEILING under the wall, not a discriminator.

| # | Observable | Falsifier function | Channel(s) | Prediction value(s) | Live-watch envelope | Internal-consistency split | Detector / horizon | scheme | convention | L_max | content_sha256 | audit_sha256 | notes |
|:-:|:-----------|:-------------------|:-----------|:--------------------|:--------------------|:----------------------------|:--------------------|:-------|:-----------|:------|:----------------|:--------------|:------|
| 78 | SMDS (supermassive dark star) LRD-progenitor seeding channel — a DM-annihilation-POWERED hydrostatic seed (Ilie: zero-metallicity cloud whose luminosity is supplied predominantly by ~100 GeV WIMP annihilation heating, MESA-evolved to the GR-instability onset, pressure-averaged ⟨Γ₁⟩_P crossing Γ_crit ≈ 4/3 + C·GM/(Rc²), C ~ 2–3 for n=3 polytropes; prompt BH mass ≳ 10% of progenitor) | **NON-channel forward falsifier (asymmetric fork)**: the substrate predicts **NO SMDS-powered seeds** — the Leggett-channel GGE quasiparticle DM is PROVEN non-annihilating (CPT-neutral inter-band coherence mode; `LEGGETT-MOMENT-70`; baseline `Annihilation = 0` PASS), so the SMDS power source does not exist in the framework's dark sector. **Falsifier fires**: a CONFIRMED DM-annihilation-powered SMDS LRD progenitor (cool/extended spectral signature, T_eff ≲ few×10⁴ K, paper-06 MESA template) ⇒ the non-annihilating-DM property is CHALLENGED. **Corroborator**: SMDS-signature null + heavy seeds forming gas-dynamically (DCBH class) | JWST LRD-progenitor spectroscopy at the seed-formation epoch — structurally adjacent to the existing non-annihilating-DM property (LEGGETT-MOMENT-70) but at a NEW observational channel (genuinely additive, not a restatement) | **Annihilation luminosity = 0** (substrate property; `Annihilation = 0` PASS, `baseline-findings-s66.md` + `Mass_LeggettDM_over_Delta_BCS = 11.97`, CONDITIONAL on Γ_grav < H_0 per Row #68). The closure is one-directional and PARTIAL: the framework's DM contributes NO annihilation thermostat but DOES contribute gravitational adiabatic-contraction / dynamical-friction to a collapsing halo — silent on the dark-star POWER source, participating in the gas-dynamical collapse | **PHYSICS-level channel — NOT subject to `LRD_demographics_not_discriminating`** (the z < 10²⁸ wall caps demographics channels only; this row tests the interaction property). Live-watch: any published claimed SMDS spectral identification in a confirmed LRD progenitor | **The fork asymmetry IS the framework's position**: if LRD heavy seeds form, they form by the gas-dynamical route (DCBH / a₂-channel relay-pattern attractor; Pacucci 6-puzzle benchmark = the framework-COMPATIBLE branch), NOT the dark-star route — falsifiable in BOTH directions (an annihilation-SMDS detection challenges the DM property; SMDS-null with gas-dynamical seeding corroborates it) | JWST progenitor spectroscopy (now–2030s); no dedicated detector horizon — the falsifier fires on a published confirmed SMDS-progenitor identification, the corroborator accumulates with each gas-dynamically-seeded LRD progenitor | LRD-seeding-fork-DM-interaction-property | non-annihilating-Leggett-DM-predicts-NO-SMDS-seeds | N/A (property-level row; no L_max truncation enters) | (no producing script — S99 litreview registry capture; provenance = consolidation §III.F + paired G8 reports) | (no compute gate — existing-property audit pins: `LEGGETT-GRAV-DECAY-67`/`-73a` chain via Row #68 `ceb8746c…`/`93b275ba…`; baseline `Annihilation = 0` PASS) | NEW S100b plan-freeze landing (S99 litreview G8-1 / §III.F); row label `S100-SMDS-DARK-STAR-FORK`; sources: Ilie et al. arXiv:2606.02539 (paper 06, SMDS/MESA/GR-instability) + Pacucci arXiv:2601.14368 (paper 10, DCBH — the framework-compatible OPEN branch); the ONE LRD channel escaping the z<10²⁸ wall |

- **Fork structure (two branches, one substrate position)**: **(CLOSED branch)** annihilating-DM SMDS — requires an annihilation luminosity the Leggett-channel DM cannot supply (N_pair superselection forbids the annihilation channel; `framework-dm-properties.md`). **(OPEN branch)** gas-dynamical DCBH — RHD accretion onto M_• ≈ 10⁵ M⊙ in a pristine atomic-cooling halo, Compton-thick self-screened, framework-COMPATIBLE conditional on the substrate independently sourcing the collapse-site abundance; that conditional is the structure-timing question and sits BELOW the z<10²⁸ wall (observationally degenerate, per the consolidation's honest-count discipline). The a₂-channel abundance benchmark is the forward compute `S100-A2-HEAVY-SEED-ABUNDANCE` (consolidation G8-2, routed to the S101 plan via §V — NOT this row).
- **Capstone §7.2 decision (declared for §7-surface sync)**: NO capstone §7.2 anchor-row is landed for this fork — §7.2 carries detector-decisive scheduled-instrument channels; the SMDS fork is a property-level NON-channel whose falsifier fires on a publication event, not an instrument datum. The inventory row is the canonical surface; the capstone §7.2 table inherits via this inventory.

**Substrate-IS framing (PHONONIC).** The fork is read FORWARD from the substrate's dark sector: D_K eigenvalue spectrum on Jensen-deformed SU(3) → Leggett inter-band coherence mode (gap-massed, CPT-neutral, N_pair-superselection-protected ⇒ NO annihilation channel) → zero annihilation luminosity → NO SMDS power source. Where heavy seeds form, they ARE the post-transit GGE acoustic-excitation interference pattern self-organizing through the a₂ (gravity) channel into a compact relay-pattern attractor — the gas-dynamical DCBH picture (contracted gas envelope, reprocessed UV) is the laboratory-IN restatement of that substrate-IS coherent collapse. The substrate's DM participates gravitationally (adiabatic contraction / dynamical friction) while contributing no annihilation thermostat. Direction: `D_K eigenvalues → Leggett channel (non-annihilating) → seeding fork → JWST progenitor spectroscopy` (per `phononic-framing.md §"IS Space, Not IN Space"`); "dark-matter annihilation" vocabulary is used only when quoting the source papers' own framing.

**Cross-references**: consolidation §III.F + §II G8-1 + §V (routing row); `sessions/archive/session-99/session-99-litrev-jwst-lrd-mack.md` §II.1/§IV/§V.1 (the 4-field spec this row lands); `LRD_demographics_not_discriminating` (closed_mechanism STAGING — the wall this row ESCAPES; every other G8 channel is a consistency ceiling under it); Row #68 (the same Leggett-channel DM relic's gravitational-stability conditional — together the two rows carry the DM-sector property suite: non-annihilating + Γ_grav < H_0); Row #63 (J3 pixelation lock — the other LRD-scale row, demographics-class, wall-capped); `framework-dm-properties.md`; forward computes `S100-A2-HEAVY-SEED-ABUNDANCE` + `S100-SELECTION-FUNCTION-FLOOR` (consolidation G8-2/G8-3, S101-plan routed — the OPEN-branch benchmark + methodology wrapper, distinct from this registry row). Per `feedback_mack-bridge-role.md` mack-cosmic-bridge sole writer for `falsifier-master-inventory.md` (AMRI-PROMOTED 2026-04-28).


## S100b litreview-batch annotations (S99 litreview campaign → S100b plan-freeze; mack-cosmic-bridge sole-writer)

> **Origin**: S99 litreview campaign (19 paired review reports; consolidation `session-99-litreview-consolidated-gen-physicist.md` §II G2-3 / §III.E / §V hygiene-routing rows naming mack) routed to the mack-cosmic-bridge sole-writer batch at S100b plan-freeze (`session-100b-housekeeping.md` capstone-hygiene Q2/Q5). ANNOTATIONS ONLY — no value changes, no status re-adjudications, no verdict lines (the review campaign ran no compute gate; the canonical write-order does not apply — no new framework prediction value is produced).

### Row #70.audit-S100b-KIDS-LEGACY — σ₈/S₈ tension-direction REVERSAL annotation (KiDS-Legacy repositioning; S99 litrev G2 paper 07)

- **External event**: KiDS-Legacy reports **S₈ = 0.815 (+0.016/−0.021)**, **0.73σ from Planck** — the historical KiDS-low S₈ was substantially a methodology artifact (redshift-distribution calibration, survey area, image reduction; `session-99-litrev-dark-energy-mack.md` §II.5, both G2 reports CONVERGENT). The low-lensing anchor motivating Row #70's "VIABLE middle / ~2σ between the two ENDS" framing is substantially GONE from the KiDS side.
- **Repositioning (axis-matched per Row #70's own σ₈/S₈ labeling resolution)**: σ₈ axis — BOTH framework channels (`sigma8_OZ_50 = 0.799` O-Z headline, `sigma8_growth_a2 = 0.79317` a₂-growth partner; knowledge-MCP verified non-superseded 2026-06-06) sit BELOW the Planck-CMB anchor 0.811 (2.00σ on the O-Z headline, Row #70 pin). S₈ axis — `S₈_FW = 0.8128` (S69, zero-free-parameter, Row #70) sits BELOW BOTH high anchors: S₈(Planck) = 0.8310 ± 0.016 (1.14σ below, Row #70 pin) AND S₈(KiDS-Legacy) = 0.815 (+0.016/−0.021) (0.10σ below on the relevant lower bar: |0.8128 − 0.815|/0.021 = 0.105). **Both framework channels now sit below BOTH high anchors** — the "intermediate between Planck-CMB and lensing" framing is RETIRED.
- **Honest scope (annotation, not a value change)**: the framework σ₈/S₈ are substrate outputs, not fits — the VALUES do not move; only the observational POSITIONING moves. The low side is not universally gone (DES-Y3 + HSC retain somewhat lower S₈), so the framework is NOT excluded; it is favored only if the residual low side persists. The two σ₈ channels are channel-distinct substrate-IS readouts (~0.7% apart) and are NOT an uncertainty band (Row #70 discipline preserved verbatim).
- **Forward**: the S₈-axis conversion for both channels under the framework Ω_m is the consolidation's G2 lower-EVOI registry-update item (S99-SIGMA8-REPOSITION class, §V) — this audit-pin is its registry-annotation half; no compute is run here. Capstone §7.1 σ₈ cells (Register-B Notes + flat-table Status) carry the matching one-line tag (same S100b batch, same provenance).

### Index-legend caveat — historical "W-5 §VII.W" bridge citations resolve to §VII.AF.1 (slot-reroute legend; S99 litrev G7-1)

Legend for downstream sweeps: historical citations of the S86 W-5 Pillar III ↔ Pillar IV quantum-metric bridge as "W-5 §VII.W" (e.g., Row #9b Level-1 + internal-consistency cells, "LQT-inherited from W-5 §VII.W") resolve BY CONTENT to **§VII.AF.1(.OP-PROJ)** — the W-5 REGISTRY-1 bridge was rerouted §VII.W → §VII.AF per the UD-18 slot-allocation decision (`permanent-results-registry.md` slot-allocation note; refined S88 W11 V.4 into §VII.AF.1.OP-PROJ landed + §VII.AF.1.STATE-PROJ pending-verification) — while bare **§VII.W today = the HP_*(A_F) Parity-Grading Orthogonality Theorem (Slot 1a-S7)**, a DIFFERENT theorem (correctly cited as such at Rows #37/#38). Registry VERIFIED-CORRECT at S100b (2026-06-06): the §VII.AF.1/§VII.W conflation lives in the S99 litreview INDEX, not in `permanent-results-registry.md` (consolidation §III.E / G7-1, both G7 reports CONVERGENT). Resolve slot labels by CONTENT, never by historical plan-line labels.
'''

WATCHLIST_APPEND = '''

## S100b litreview anchor-currency annotations (S99 litreview campaign → S100b plan-freeze; mack-cosmic-bridge sole-writer)

> **Origin**: S99 litreview campaign G2 dark-energy sweep (`sessions/archive/session-99/session-99-litrev-dark-energy-mack.md` §II.2 + §II.6; `…-dark-energy-sagan.md` σ-distance correction; consolidation `session-99-litreview-consolidated-gen-physicist.md` §II G2-3 + §V hygiene-routing). Append-only audit-pin sub-entries on the EXISTING `w_0` / `w_a` / `H_0` rows above — NO value changes, NO status changes (H_0 stays LIVE-PENDING), NO verdict lines (the review campaign produced reports only; the canonical write-order does not apply — no new framework prediction value).

### w_0 / w_a — post-Dovekie anchor-currency audit-pin (supplements the DR2-era σ-figures above)

- The summary-table + entry-detail + unified-schema `w_0` figures above ("2.9σ from DR2", "+3.28σ vs the LCDM null") and the `w_a` "~0.3σ vs the near-constant-DE null" are DR2-era σ-from-LCDM-null readings — historical, PRESERVED VERBATIM above. The registry-live EXTERNAL anchor has moved to **post-Dovekie 2026** (Popovic et al., arXiv:2511.07517v3 — DES-Dovekie SN + DESI DR2 BAO + Planck/ACT/SPT joint Flat w₀wₐCDM: w_0 = −0.803 ± 0.054, w_a = −0.72 ± 0.21, ρ(w_0, w_a) ≈ −0.85).
- **Post-Dovekie measured-central σ-distances** (source of record: `falsifier-master-inventory.md` Row #1.dovekie-2026-update, S88 W5; atlas-08 Q37 / Window-14 cited for consistency — atlas-08 NOT edited here): canonical `w0_FW = −0.918` → **2.130σ**; branch-(iv) `w0_FW_R842 = −0.842454` → **0.731σ**; `w_a = 0` four-fold lock → **3.429σ** (tension ADVANCED; Atlas D04 C5 = BROKEN — the framework's live wager).
- **Superseded-headline guard (anchor-currency)**: the **0.081σ** "R_842 vs DR2 Pantheon+ (−0.838 ± 0.055)" coincidence is the historically-tightest but SUPERSEDED comparison — do NOT cite it as the live state (S99 litrev G2-3, both reports CONVERGENT on the anchor-currency flag). The binding anchor is post-Dovekie; the binding INSTRUMENT remains DESI DR3 (window-open 2026-04-23 with hard lockouts A–F; data-release 2027; the R_842 binding event is NOT triggered by any SN reanalysis on DR2 BAO).
- **Branch-resolution guard**: the w_0 branch choice (canonical −0.918 vs R_842 −0.842454) must be resolved on INDEPENDENT geometric grounds (`w0-primary-decision-rule.md`; consolidation G2-3, S101-plan routed). Until then the 0.731σ branch-(iv) proximity is NOT scored as a PASS — branch-shopping guard.

### H_0 — LIVE-PENDING contingency + TDCOSMO-2025 anchor audit-pin

- **Status UNCHANGED: LIVE-PENDING.** H_0 = 65.4 km/s/Mpc is CONTINGENT on the √16 spinor-factor resolution (atlas-08 Q27 / Window-19, structurally unresolved since S58 — the "unresolved through S85" wording above extends through S99). The S99 litreview INDEX over-stated 65.4 as a firm prediction; THIS watchlist's contingency framing is the correct register (litrev G2 §II.6 honesty correction — both G2 reports flag it).
- **First-principles resolution QUEUED**: gate `S100-H0-SPINOR-FACTOR` (S100a plan, W4) — derives the spinor normalization √16 = 4 from the d_spec=8 16-component spinor (Tr = 16) vs the empirical 3.92 (rel ≈ 2.04%). On resolution, `evoi_class` CONTINGENT → FLAGSHIP per the unified entry above.
- **New external anchor (annotation only — nothing becomes binding while LIVE-PENDING)**: TDCOSMO-2025 H_0 = **71.6 (+3.9/−3.3)** km/s/Mpc (mass-sheet-degeneracy-marginalized, blinded; litrev G2 paper 08). 65.4 sits **1.88σ below** on the relevant lower error bar ((71.6 − 65.4)/3.3 = 1.879; 1.59σ on the +3.9 upper bar) — NOT excluded, but the central value pulls away from 65.4. Against the Planck-anchored DESI+CMB ΛCDM H_0 = 67.34 ± 0.54: **3.59σ below** — the framework's most exposed Hubble-sector claim (it predicts BELOW the CMB anchor, on neither side of the standard Hubble tension). σ-distances Sage-verified in the G2 source report (`…-litrev-dark-energy-mack.md` §II.6; sagan's lower-bar 1.88σ correction adopted).
'''


def append_once(path, marker, text):
    """Append text to path unless marker already present. Returns status string."""
    with io.open(path, "r", encoding="utf-8") as f:
        existing = f.read()  # (local)
    if marker in existing:
        return "SKIP (marker already present): %s" % path
    chunk = text if existing.endswith("\n") else "\n" + text  # (local)
    if not chunk.endswith("\n"):
        chunk += "\n"
    with io.open(path, "a", encoding="utf-8", newline="") as f:
        f.write(chunk)
    return "APPENDED %d chars: %s" % (len(chunk), path)


def main():
    print(append_once(INVENTORY, INVENTORY_MARKER, INVENTORY_APPEND))
    print(append_once(WATCHLIST, WATCHLIST_MARKER, WATCHLIST_APPEND))
    print("DONE (registry append batch; no verdict line by design)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
