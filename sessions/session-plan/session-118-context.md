# Session 118 — Carry-Forward Context & Scope

**Date**: 2026-06-29
**Built by**: `/rclab-plan --session 118` (fanout). Partition: `sessions/session-plan/session-118-partition.md`. Dispatch: `/rclab-coordinate sessions/session-plan/session-118-plan-index.md`.
**Source**: the ten S117 per-wave working-paper `## Carry-Forward Computations` sections (`sessions/session-117/session-117-w{0..9}-workingpaper.md`) + `session-117-housekeeping.md §B/§D/§F` + forward registers (`evoi-framework.md §6/§1–§4`, `atlas-08-open-questions.md` LIVE DASHBOARD, `open-channel-ledger.md §A`).

This file is the **authoritative scope** for the S118 per-wave planners. Planners read THIS file (not S117 plan/synthesis files — watchdog-stall risk). Query the knowledge MCP directly for prior verdicts / constants.

---

## Source manifest (S117 carry-forward provenance)

| WP source | CF block disposition |
|:----------|:---------------------|
| `session-117-w0-workingpaper.md` | "No carry-forwards" (wave closed) + investigator-surfaced **CF-W0-1** (Q2 hygiene) |
| `session-117-w1-workingpaper.md` | **CF-S118-AS-CS-SUBSTRATE-FIRST** (physics) + investigator **CF-W1-1** (physics), **CF-W1-2** (Q2 EVOI-fold) |
| `session-117-w2-workingpaper.md` | "No carry-forwards" (wave closed) + investigator **CF-W2-1** (physics), **CF-W2-2** (Q2 hygiene) |
| `session-117-w3-workingpaper.md` | "No carry-forwards" (lepton-CP under-determined; deep residual → atlas-08 Q18b standing) |
| `session-117-w4-workingpaper.md` | "No carry-forwards" (all PASS) + investigator **CF-W4-1** (Q2 hygiene + EVOI-fold) |
| `session-117-w5-workingpaper.md` | **CF-S118-WDW-S0-ONGRID** (physics; OPTIONAL/cosmetic) |
| `session-117-w6-workingpaper.md` | **CF-S118-LEMP-OQ4-VACUUM-FERMI-PIN** (physics) + investigator **CF-W6-1** (Q2 EVOI-fold; LOW) |
| `session-117-w7-workingpaper.md` | "No carry-forwards" (w0 settled all axes) |
| `session-117-w8-workingpaper.md` | "No carry-forwards" (STATE-PROJ substrate-first; no-A-sector = standing gap) |
| `session-117-w9-workingpaper.md` | "No carry-forwards" (flatness PASS; scale-range amplitude rides W1 CF-S118-AS-CS) |
| `session-117-housekeeping.md §B` | "(none)" — confirms the 3 physics CFs above are the genuine forward computes; §A is ledger-only (do NOT re-dispatch) |

**Dedup**: the conditional `CF-S118-AS-PREFACTOR-SOURCE` is NOT a standalone item — it is the FAIL-branch pointer inside `CF-S118-AS-CS-SUBSTRATE-FIRST`'s Gate field (the planner picks it up only if the primary FAILs). No cross-WP title collisions.

---

## Deduplicated carry-forward table

Two classes: **PHYSICS computes** (forward gates → S118 compute waves) and **Q2 registry-hygiene / EVOI-fold** items (mack-surface patches → W0 gates; EVOI prose folds → effected by the orchestrator at 1c-REGISTERS.MAINTAIN, NOT dispatched gates).

### PHYSICS computes (→ compute waves)

| ID | What (one-line) | Inputs | Gate | Effort | Wave | Executor | Origin |
|:---|:----------------|:-------|:-----|:-------|:----:|:---------|:-------|
| **CF-S118-AS-CS-SUBSTRATE-FIRST** | Compute the a₂/curvature-channel (hydrodynamic-IR) sound speed `c_s` from substrate first principles (spectral-action a₂ first/second-sound ratio at the post-fold GGE state); test whether it lands in the GS-1 fork-carrying window [0.516, 0.650] M_KK. PASS ⇒ GS-1 PHYSICS-SCALE-SEPARATION fires ⇒ A_s fork resolves to the acoustic-horizon (H̃, +0.196) grid, closing Q23 to a zero-parameter magnitude. | s84 L12 spectrum cache; a₂ Seeley-DeWitt (G_ττ sector); `c_Gold=0.915`, `c_BLV=0.485`; GS-1 window [0.516,0.650] (`s117_gs1_grid_selection.npz`); ξ_KZ=0.01876; (aH)\|_exit=14.311 (s77) | PASS iff substrate-first `c_s ∈ [0.516,0.650]` (⇒ \|2·Δ_scale − 0.668\| ≤ 0.1); FAIL ⇒ route to **CF-S118-AS-PREFACTOR-SOURCE** (identify the greybody knob / c_sub Mellin-weight / F_amp backreaction carrying the 0.40-OOM shortfall) | ~1 wave | **W1** | transit-dynamics-theorist | W1 wave-close (HIGHEST EVOI — the Q23 A_s rate-limiter) |
| **CF-W1-1** (ALT-GREYBODY) | Upgrade the atlas-09 exit-greybody "structural-wall candidate" (1-4 FAIL; 3 knob-free classes failed) toward an actual wall OR falsify it. Route (a): a 4th knob-free substrate-IS greybody bridge map — full BdG S-matrix transmission on the exit-horizon sector. Route (b): a structural no-go that knob-free spectral geometry cannot supply sub-unity Γ at any physical (M_reg ≥ λ_max) scale. | `s117_alt_greybody.py` machinery (audit `649ce244`); 3 failed classes + targets {0.137 box-δ, 0.637 slow-roll, 0.512 fit}; KNOB-LOCATION corollary; exit-horizon BdG sector spectrum (L12/L14 caches); INV12-W3-4 Pöschl-Teller corridor | (a) 4th-class knob-free Γ within rel_dev 0.10 of a target at M_reg ≥ λ_max ⇒ PASS (greybody EXISTS, candidate falsified); miss ⇒ FAIL (wall strengthened to 4 classes). (b) valid no-go ⇒ PASS (candidate → structural wall); invalid ⇒ INFO | medium | **W1** | volovik-superfluid-universe-theorist (BdG S-matrix / analogue horizon) | W1 investigator (first-surfaced) |
| **CF-W2-1** | Joint (R, PMNS-angle) admissibility scan over the FREE U_eL/ε_LX texture family. 2-2 found ε23 texture drives R=113.564 (OUT of NuFIT [17,66]); bare diagonal R_bare=31.576 (in band); 2-5 established U_eL/ε_LX is a genuine FREE direction (ΔS/S=3.22e-15). Scan the texture-admissible family; for each point compute (R, θ12, θ23, θ13); test whether {R∈[17,66] ∧ angles∈3σ} is non-empty + measure admissible-volume fraction. | `computations/session-116/s116_lepton_pmns_texture.npz` (M_D, M_R, ε_LX); 2-4 free-orbit multistart machinery (`s117_quark_ckm_underdetermination.py`, adapt U_dL→U_eL/ε_LX); 2-5 `s117_uel_flat_direction.py`; NuFIT 5.2 NO 3σ bands | Joint region non-empty ⇒ PASS (under-determination survives joint observational constraint); empty ⇒ FAIL (joint over-constraint — framework MORE predictive than "under-determined"); narrow positive-measure ⇒ INFO | medium | **W2** | neutrino-detection-specialist | W2 investigator (first-surfaced; the WP conflated this pinnable observable-constraint scan with the non-pinnable seed-selection MECHANISM) |
| **CF-S118-LEMP-OQ4-VACUUM-FERMI-PIN** | Pin the substrate's BdG Fermi-surface location relative to the \|D_K\| spectral floor (the vacuum structure that sets the a₀-counterterm magnitude), then re-evaluate rel_span to discriminate INFO (suppressed) vs FAIL (physically significant) for the §VII.AV `a_0^{<class>}` qualifier strength. (Robust findings — FI rejected; SD-OPEN genuine — are model-INDEPENDENT; only the magnitude band OQ-4 is open.) | s52 8-mode BdG occupations {0.130×4, 0, 0.0079×3} (constrain ξ_F so the extended vacuum reproduces the gap-IR occupations); L12/L14 caches; `Delta_BCS`; W6-2 `reg_vacuum_variance` machinery | rel_span at the gap-IR-matched ξ_F vs the 0.05 band → INFO-stays (Fermi below floor, conservative) vs FAIL-promote (gap-IR-matched, Δ_R∼κ₀) | low (re-run with pinned ξ_F; no new diagonalization) | **W3** | lizzi-spectral-functional-theorist | W6 wave-close (§VII.AV STATE-PROJ magnitude discriminator) |
| **CF-S118-WDW-S0-ONGRID** | Recompute the S36 spectral action S(τ) on a minisuperspace grid that REACHES τ=0 (s63 currently stops at τ_min=0.10), anchoring W(0)=2G(S(0)−E)=0 on-grid to convert the 5-2 INFO → PASS. | s63 S(τ) reduction machinery; S36 spectral action; `G_DeWitt=5.0`, `tau_fold=0.19` (CONST-FREEZE-42) | PASS iff W(0)=0 on-grid (no extrapolation) AND \|J(0)\|<1e-12 across the real-Robin θ-scan; INFO if grid still short of τ=0 | ~0.5 wave | **W3** | feynman-theorist | W5 wave-close — **OPTIONAL / low / cosmetic** (upgrades only a verdict label; family-wide J≡0 already E-independent; EVOI-last, droppable under capacity) |

### Q2 registry-hygiene / EVOI-fold items

| ID | What | Route | Effort | Origin |
|:---|:-----|:------|:-------|:-------|
| **CF-W0-1** | α_s-family scale-channel label-consistency: verify SCALE-AND-CHANNEL-TAGGING labels are mutually consistent across the four α_s observables (W0-2 produced-spectrum primordial ≈0; W9-2 CMB-pivot `α_s_pivot=0.0` EXACT; bare-BZ `α_s_substrate=−0.08587279`; Row #3 `alpha_s_inflation_framework=−0.06896799` "pivot-local"). Determine whether Row #3's "pivot-local" = W9's "CMB-pivot" (⇒ disambiguation annotation needed) or a pre-transport substrate scale (⇒ family coherent, no edit). | **W0 gate** (mack sole-writer; `falsifier-master-inventory.md` label check) | low | W0 investigator (first-surfaced) |
| **CF-W2-2** | §VII.CK D4 scope-token hygiene: carry the corrected coset-shift scope INSIDE the bare `t(O)=±1` center-character token wherever it appears in the D4 surface (registry ~22451/~22472), per `regulator-pin-discipline.md §"Channel-Scope Suffix Discipline"` (scope-inside-the-token; separable parentheticals do not survive aggregation) — so a future skim cannot regenerate the blind-reviewer-REJECTED center-character mis-reading. | **W0 gate** (mack sole-writer of §VII.CK; designated-writer patch) | low | W2 investigator (first-surfaced) |
| **CF-W4-1** | Row #79 "discharge owed" reconciliation: the S116 Row #79 family pre-registered all three S117 W4 gates as forward/owed discharge gates ("discharge owed / NOT asserted-closed") — all three have now PASSED (x^⊥=2.530217 dev 0.0e+00; cold λ_fs^4D=0; frac170=0.0704), but no S117 discharge sub-row was landed. Land a `Row #79.audit-S117-W4` discharge-confirmation sub-row ("discharge owed → discharged on three orthogonal axes") OR record the explicit latest-synthesis-wins no-row decision. **EVOI pair (same closure):** mark the "170× DM-mass" standing gap RESOLVED at the S118 re-stamp (→ effected at 1c-REGISTERS.MAINTAIN). | **W0 gate** (mack Row #79) **+ EVOI fold** (orchestrator) | low | W4 investigator (first-surfaced; LOW-STAKES — survival stays Reading A) |
| **CF-W1-2** | §EVOI.BF A_s-liability freshness-fold: fold the S117 W1 A_s refinements into §EVOI.BF prose (currently references only through S114) — the 3-member magnitude plurality {+0.196,+0.384,+0.864} OOM (full 5-route band [+0.196,+1.527]); the GS-1 c_s scale-separation window [0.516,0.650] M_KK (straddled by c_BLV=0.485, c_Gold=0.915); the 3-construction-class greybody-wall candidate. | **EVOI fold** (orchestrator; `/rclab-plan` Step 1c-REGISTERS) | low | W1 investigator |
| **CF-W6-1** | §EVOI.BF lizzi-d.o.f.-cohort note: add L_emp's a₀-grade UV-regulator {ζ,PV,Mellin} SD-OPEN (6-2, §VII.AV.STATE-PROJ; FI rejected, rel_span=3.118e-02) as a THIRD cohort member alongside {A_s, a_0/a_2-CC}, WITH the explicit axis-distinction (UV-regulator-selection ⊥ functional-selection — DISTINCT axes per `regulator-pin-discipline.md` 4-axis orthogonality; a sibling of A_s functional-pluralism but NOT the same d.o.f.). | **EVOI fold** (orchestrator; `/rclab-plan` Step 1c-REGISTERS) | low | W6 investigator — **LOW EVOI** (magnitude-band refinement on an already-permanent §VII.AV anchor; the planner may fold or drop) |

---

## Phase 1c-REGISTERS.CONSUME (S118) — determination

**NO additional tractable register candidate beyond the WP CFs above.** Every S117-opened tractable item already surfaced as a WP carry-forward (A_s/GS-1 → CF-S118-AS-CS; L_emp OQ-4 → CF-S118-LEMP-OQ4; greybody wall → CF-W1-1; PMNS joint scan → CF-W2-1; WDW S0 → CF-S118-WDW-S0). Every atlas-08 "actionable-now" dashboard Q (Q23/Q18b/Q3/Q8/Q12/Q33/Q30/Q36) routes either to an S117-closed status or to one of these CFs. This re-confirms the S108–S117 pattern.

**Standing gaps UNCHANGED** (high-leverage, NO tractable pre-registrable gate — leverage ≠ tractability):
- **M_KK-DERIVATION** — the incumbent-ceiling-lift keystone; CV2A transmutation corridor exists (S110), no clean gate.
- **atlas-04 C2 K_pivot** — the single largest *observational* load-bearing gap (`open-channel-ledger §A1`).
- **residual-3% CC** (Tier-1 #2 live edge) + **BBN-epoch arm Q29**.
- **τ_fold = 0.190 moduli selection** — one-loop + variational corridors dead S95; dynamical-relaxation OR empirical.
- **Born-rule L²-weight** — INPUT no-go (`open-channel-ledger §A5`).
- **170× DM-mass anchor** — kinematic survival DISCHARGED 3 axes (S117 W4); the mass-anchor derivation stays gate-less (→ EVOI 170× gap marked RESOLVED-on-kinematics this re-stamp via CF-W4-1).
- **branch-iv w₀(L) DR3** + **DESI-WZ-LENSING-BIAS** — capacity-deferred (~2027 DR3 horizon).
- **K8 §VII.AF.1.STATE-PROJ** — PENDING-VERIFICATION (empty companion slot ⇒ a Stage-1 derivation, no dispatch-ready Stage-2 gate).
- **`CF-S94-W5-3-FWDC1-ASYMPTOTIC`** (L>14 irrep-construction wall) · **`CF-S117-STATEPROJ-SC-FROM-SUBSTRATE`** (no-A-sector, single BDI N₃=0).

A full §1–§4 numeric P(pass) re-rank remains the separate elicitation pass per the §EVOI honesty caveat.

---

## Phase 1c-REGISTERS.MAINTAIN (S118 plan-freeze) — effected by the orchestrator

- **EVOI** (`evoi-framework.md`): currency S117→S118; §6 S118 stamp (this queue + the CONSUME determination); §5 S117 closure row appended; folds CF-W1-2 (§EVOI.BF A_s 3-member plurality + GS-1 window + greybody wall), CF-W6-1 (L_emp UV-regulator SD cohort-note), CF-W4-1 EVOI part (170× DM-mass gap RESOLVED-on-kinematics). Staleness audit re-run → PASS (lag 0).
- **atlas-08** (`atlas-08-open-questions.md`): S117 freshness fold into the LIVE DASHBOARD (Q23 A_s 3-member plurality + GS-1 window; Q8 a₄ order-separated; Q12 WDW J≡0 real-self-adjoint family; Q33 §VII.AJ.STATE-PROJ substrate-first; Q36/w0 deg=0 transport, substrate=pivot=−0.918; Q18b mixing under-determined both sectors; Q3-DM 170× discharged 3 axes; e-fold/flatness Row #93 PASS; lepton-CP under-determined); header re-stamp S114→S117; backing audit `atlas-08-freshness-S117.md`.
- **atlas-04** (`atlas-04-assumptions.md`): NO forced status change (S117 capstone-hygiene gate Q3 = all strengthenings; DM survival stays Reading A / C11-conditional UNCHANGED). Recorded no-change in the freshness audit.
- **open-channel-ledger**: §E EVOI/atlas-08 freshness cells refreshed to S117/S118.
- **mack-surface S117 closures** (falsifier inventory Rows #89/#93/#12/#3 + w0 DR3 + §VII.CK): ALREADY effected in-session via the S117 mack-close batch (`housekeeping §A` A3–A12) — NOT re-done here. The CF-W0-1/CF-W2-2/CF-W4-1 mack patches are the NEW first-surfaced gaps, routed as W0 gates.

---

## Wave partition (summary; full manifest in `session-118-partition.md`)

| Wave | Theme | Owner / planner | Gates |
|:----:|:------|:----------------|:-----:|
| 0 | Registry-hygiene (mack-surface patches) | mack-cosmic-bridge | 3 |
| 1 | A_s amplitude closure | transit-dynamics-theorist | 2 |
| 2 | Lepton-PMNS joint admissibility | neutrino-detection-specialist | 1 |
| 3 | Spectral-functional + WDW residuals | gen-physicist | 2 |

8 dispatched gates / 4 waves. Plus 3 EVOI prose-folds effected at 1c-REGISTERS.MAINTAIN (not dispatched gates).
