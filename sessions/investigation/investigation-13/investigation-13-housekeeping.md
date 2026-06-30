# Investigation 13 Housekeeping Ledger

**Date**: 2026-06-17
**Investigation**: 13 (INVESTIGATION track — verdict ledger `computations/investigation-13/inv13_gate_verdicts.txt`)
**Authoritative scope**: `.claude/rules/Investigating-Workshops.md §"Q2"`
**Template**: `.claude/templates/session-housekeeping.md` (adapted for the investigation track)

## Track-local boundary (load-bearing for this ledger)

Investigation verdicts are track-local (`gate-verdicts.md §"Investigation-Track Canonical Path"`): they are NOT swept into the knowledge index, and **curated session-track register mutations (EVOI tables, `falsifier-master-inventory.md`, `permanent-results-registry.md`, Atlas docs, `canonical_constants.py` promotions of new investigation results) MUST NOT be performed in-investigation**. In a session, such edits would be §A (orchestrator-direct, fixed-in-session); in an investigation they are deferred as **lift candidates** to the `/rclab-investigate --investigation 13` close (§G below). This is the structural reason §A here is narrow and §G is populated.

## Q2 marker (citation)

A candidate is Q2 iff its resolution is a status-tag edit / mechanical promotion / rule-file diff / audit-script extension / mechanical re-run, rather than a derivation that produces a new structural claim (`Investigating-Workshops.md §"Q2"`).

---

## §A. In-session resolutions (already effected; ledger only)

Within-track non-math items effected by the team-lead orchestrator at wave-close (per `feedback_fix-in-session-never-defer.md`; these do NOT cross the track-local boundary):

| # | Source wave / gate | Item | Resolution (file:lines) | Verified at |
|:--|:-------------------|:-----|:------------------------|:------------|
| A1 | W1 (all 3 gates) | Wave 1 team-lead synthesis (per-gate constraint-map, numerical-vs-structural split, Files Produced) | `sessions/investigation/investigation-13/investigation-13-w1-workingpaper.md §"Wave 1 Synthesis"` | 3 verdict lines on disk (W1-1/2/3) |
| A2 | W2 (all 3 gates) | Wave 2 team-lead synthesis + the one genuine math CF (CF-INV13-W2-1-FINITE-MU-REFINE) | `sessions/investigation/investigation-13/investigation-13-w2-workingpaper.md §"Wave 2 Synthesis"` + §"Carry-Forward Computations"` | 2 verdict lines (W2-1/2) + synthesis md (W2-3) |
| A3 | W2-3 (review gate) | Gate-finalization gap: review-gate WP §W2-3 left as NOT-STARTED skeleton (review gates write a standalone synthesis, not a WP section). Annotated LANDED + recorded the artifact-existence verification (9/9 must_contain markers, 42 hits). | `investigation-13-w2-workingpaper.md §W2-3` (Status + closure checklist + Verdict + Results) | synthesis md grep (orchestrator-verified) |
| A4 | (session-close) | This housekeeping ledger written | `investigation-13-housekeeping.md` | — |

---

## §B. Hygiene-promotion compute carry-forwards (4-field spec; mirrored to WP CF)

(none) — the wave produced exactly ONE genuine future-compute item, **CF-INV13-W2-1-FINITE-MU-REFINE** (finite-μ CFL EoS refinement, self-consistent μ_eff). It is genuine new substrate-physics compute (NOT Q2-hygiene / mechanical re-run), so it lives natively in `investigation-13-w2-workingpaper.md §"Carry-Forward Computations"` (the surface `/rclab-investigate` → `/rclab-plan` consumes), not as a §B mirror. Pointer only.

---

## §C. Parallel-compute-wave carry-forwards (Q3 wave-together; mirrored to WP CF)

(none)

---

## §D. Methodology-rule extensions (M1-M4 + allowlist; mirrored to WP CF)

(none) — no rule-file extension surfaced; all six gates are COMPUTE/review on substrate-physics axes, not methodology gates.

---

## §E. Pre-compute shell waves (upstream escalation; NOT a CF)

(none — all 6 gates computed; 5 verdict lines on disk + 1 review synthesis md. No `Status: NOT STARTED` compute gate remains.)

---

## §G. Session-track promotion candidates (investigation track-local; route to `/rclab-investigate --investigation 13` close)

These are the investigation's OUTPUT lift candidates. Each WOULD be an §A orchestrator-direct edit in a session, but crosses the track-local boundary (curated-register mutation), so it is deferred to the `/rclab-investigate --investigation 13` close as a turnkey promotion (target + recommended edit). They are NOT math carry-forwards and NOT in-session fixes.

| # | Source gate / outcome | Promotion target | Recommended edit |
|:--|:----------------------|:-----------------|:-----------------|
| G1 | W1-1 INFO (ANALYTIC-LOCAL) | constraint-map / falsifier inventory | Record gen UB-2 (GGE cosmological-collider spectroscopy) CLOSED-as-NULL — no μ~O(1) collider-addressable heavy field in the GGE branch content on either clock anchor; reinforces the Gaussian-by-Wick / f_NL-envelope permanent result. |
| G2 | W1-2 INFO (definite-sign sub-detectable) | `falsifier-master-inventory.md` (mack sole-writer) | Candidate row: a₄ higher-curvature QNM/tidal correction — definite **+** (blue-shift) sign, m≈10⁻⁷⁶ ≪ 10⁻³, zero free params; a future-detector falsifier constraining M_KK from the strong-field side. audit_sha256 `86e848e8…`. |
| G3 | W1-3 FAIL (truncation-divergent) | EVOI register Q37 (DESI DR3 / branch-iv) | Update Q37 from "S105 INFO 0.0443091 / FB-envelope-bounded" → "deep-truncation DIVERGES at L∈{12..16}, spread_CAC=0.0630 > 0.05 FAIL". Scope: L_max axis only; branch-iv derivation-admissibility (S101) UNAFFECTED. audit_sha256 `ffafc349…`. |
| G4 | W2-2 PASS (S8 in-band, bindable) | `falsifier-master-inventory.md` (mack sole-writer) | LSS-flagship row: the f·σ8(z) growth-suppression curve as a DESI-5yr (1.001σ @ z=0.5) / Euclid (1.516σ, 7 bins) bindable S8-tension-relief discriminator; now the LIVE near-term LSS falsifier (GW flagship retired S96). Honest caveat: partial relief, Planck-side. audit_sha256 `435609fc…`. |
| G5 | W2-3 LANDED (review) | `evoi-framework.md` Tier tables + mack/Sagan co-dispatch; atlas-08 Q44 | Re-anchor the EVOI Tier-1/Tier-2 tables with the elicited per-observable P(pass) Bayes factors from `investigation-13-bayesian-reanchor-synthesis.md` (+ currency bump); mack + Sagan co-dispatch on the observational-surface rows (n_s 4.73σ, w_a 3.43σ, A_s wall, w₀ branch-shopping). Closes the standing atlas-08 Q44. The review synthesis IS the input to this promotion. |

---

## §F. Structural counts (artifact shape; not length)

| Category | Count |
|:---------|------:|
| §A In-session resolutions (within-track) | 4 |
| §B Hygiene compute CFs (mirrored to WP) | 0 |
| §C Q3 parallel-wave CFs | 0 |
| §D Methodology rule extensions | 0 |
| §E Pre-compute shell waves | 0 |
| §G Session-track promotion candidates (→ /rclab-investigate) | 5 |
| Genuine math CFs (native to WP CF, not §B) | 1 (CF-INV13-W2-1-FINITE-MU-REFINE) |

---

## Process observations (closed in-session; do NOT propagate)

- **s84 cache (4,4)-sector gap** (W1-3): `computations/session-84/s84_spectrum_cache_L12_tau019.npz` is missing the level-8 (4,4) sector (S84-era gap; S106 rebuilt it, dim=125, 2000 eigenvalues). ρ_B on the complete S106 union differs from the s84-incomplete S105 basis by 1.68e-3 — a sector-set difference (both correct on their own set), NOT an evaluator drift. The complete S106 union is the canonical truncation. Already documented in WP §W1-3 + the lizzi-spectral-functional-theorist agent memory; recorded here for cross-wave visibility only, not as a carry-forward.
- **W1-1 source-first prereq** (W1-1): λ_B1/B2/B3 + f_NL_folded were promoted into `canonical_constants.py` via `update_constant` as the plan-authorized in-script SOURCE-FIRST prerequisite (atlas-07/S39/S83 pre-existing values made import-resolvable, not new investigation results). SHA drift `e6829db0…` → `e5a7587f…` disclosed in the verdict-file extra-row per `substrate-first-canonical-sourcing.md §(ii.B)`. Plan-authorized; no further action.

---

## Consumption pointers

- **`/rclab-investigate --investigation 13`**: read this file BEFORE producing candidates. §A/§B/§C/§D/§E are non-workshops by construction. **§G is the lift-candidate set** — each is a turnkey session-track promotion (target + recommended edit) to route into the next session-mode plan or the housekeeping lift. The genuine math CF (CF-INV13-W2-1-FINITE-MU-REFINE) is consumed from the W2 WP CF block, not from §B.
- **`/rclab-plan` (session-mode, if a §G item is lifted into a session)**: consume CF-INV13-W2-1-FINITE-MU-REFINE from `investigation-13-w2-workingpaper.md §"Carry-Forward Computations"`; the §G promotions are register edits effected at lift, not compute gates.

---

*End of Investigation 13 housekeeping ledger.*
