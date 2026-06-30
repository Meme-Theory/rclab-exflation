# Session 107 — Workshop / Synthesis Schedule

**Date drafted**: 2026-06-14
**Scope**: Refinement and pre-screening of Session 107 results before planning Session 108. S107 was a deliberately thin session (4 mutually-independent waves, 8 gates: W1 §VII.CB Level-3 magnitude discharge FAIL · W2 Stage-2 cohort K2/K7/K9/K11 all INFO · W3 SDW-2nd-moment + ⟨r⟩-trend both INFO · W4 DESI-DR3 PRE-REG-INC). The campaign carries exactly ONE solo pre-screen and ZERO adversarial workshops — the honest count after the 3-question discriminator.
**Rationale**: Only one S107 item warrants a dedicated synthesis pass. The W1 §VII.CB working paper ASSERTS but does not ESTABLISH that the magnitude channel's failure to bind is STRUCTURAL (the partial-sum↔ζ-sum gap), and it routes the discriminating test to an S108 compute (`CF-S108-VIICB-MAGNITUDE-REMEDIATION`). A first-principles spectral-zeta pre-screen can determine analytically — before that compute runs — whether the truncated `Σ_{k≤L}|λ_k|⁻⁶` partial moment can ever reach the ζ-regularized `a_2_FW_zeta = 2776.165389` at the binding `L⁻³` rate, and if not, name the ζ-native re-anchor target. No competing-reading adjudication surfaced anywhere in S107: the housekeeping ledger (`session-107-housekeeping.md §"Q2 marker"`) records "No adversarial-physics workshops surfaced," and the one borderline candidate it names (grandfathered/audit-substituted Element-2 completeness gap vs a Stage-2-structurally-PASS bridge's STAGE-3 promotion, K2/K7/K9/K11) was resolved conservatively in-session by applied precedent and surfaces as a workshop ONLY if that precedent is contested — which has not occurred.

**Source documents (authoritative; do not re-adjudicate)**:
- `sessions/session-107/session-107-w1-workingpaper.md` (§W1-1 §VII.CB magnitude-convergence FAIL; the partial-sum↔ζ-sum structural claim)
- `sessions/session-plan/session-107-plan-w1.md` (§W1-1 substitution chains Claim A/B; PASS/FAIL/INFO rubric; `g_M = a_2_FW_zeta = 2776.165389`; `Level2(L=10)=1e-3`)
- `sessions/permanent-results-registry.md` (§VII.CB master row; §VII.AF.1.OP-PROJ over-performance precedent lines 14918–14951; §VII.AU under-performance sibling)
- `computations/session-107/s107_gate_verdicts.txt` (8 gates; W1 line 15, W2 lines 19/24/27/31, W3 lines 1/6, W4 line 10)
- `sessions/session-107/session-107-housekeeping.md` (the CANONICAL Q2 ledger — `/rclab-investigate` filter source)

**All workshop + synthesis outputs land inside `sessions/session-107/`**. The Session 108 plan is OPEN (not yet authored); this campaign's Slot-1 output and the four already-pinned S108 WP carry-forwards are its inputs.

---

## Dispatch Strategy

Ordered by criticality and cross-dependency. With one Slot-1 entry and zero Slot-2 entries, the campaign is a single parallel-cap-trivial dispatch. The Slot-1 `/rclab-review` solo launches immediately (no cross-deps). Slot 2 is empty (no competing-reading adjudication surfaced). Slot 3 is empty-with-rationale (no Slot-2 verdicts to close out, and the Slot-1 solo's downstream is a SHARPEN of an already-pinned WP carry-forward consumed directly by `/rclab-plan`, not a closeout synthesis).

| Slot | ID | Title | Skill | Agents | Rounds | Depends on |
|:----:|:---|:------|:------|:-------|:------:|:-----------|
| 1 | S-1 | §VII.CB partial-sum↔ζ-sum gap: STRUCTURAL or slow-convergence artifact? (S108 remediation pre-screen) | `/rclab-review` | 1 (`spectral-geometer`) | — | — |
| 2 | — | (none — no competing-reading adjudication; see Slot 2 rationale) | — | — | — | — |
| 3 | — | (none — no Slot-2 verdicts to close out; see Slot 3 rationale) | — | — | — | — |

---

## Slot 1 — Independent Solo Syntheses (`/rclab-review`; parallel dispatch up to ≤8 concurrent)

### S-1 — §VII.CB partial-sum↔ζ-sum gap: STRUCTURAL or slow-convergence artifact? (analytic pre-screen for the S108 remediation)

**Why**: The W1 working paper makes a substantive interpretive claim it asserts but does NOT establish — that the §VII.CB magnitude channel's failure to bind is STRUCTURAL ("the partial-sum vs zeta-sum gap is structural, not a slow-convergence artifact", W1 WP §"Solution-space consequence" + Wave-1 Synthesis). The evidence on disk is suggestive only: the truncated curvature-degree-2 moment `Z(L) = Σ_{k≤L}|λ_k|⁻⁶ ≈ 383–431` at L∈{8,10,12} (Richardson limit ≈632, own exponent p≈0.52) sits 4–7× below the ζ-regularized target `g_M = a_2_FW_zeta = 2776.165389`. The discriminating question — can a *truncated* partial moment of `D_K²` at the s=3 curvature grade EVER reach the *ζ-regularized* (analytically-continued) a₂ at the binding `L⁻³` rate, or is the ζ-value irreducibly tail-dominated? — is a heat-kernel / Seeley-DeWitt / spectral-zeta analysis answerable analytically, INDEPENDENT of running the S108 compute. This pre-screen determines whether the S108 remediation's higher-L mesh {12,14,16} / Abel-Richardson route has any chance of binding below 1e-3, or whether the correct route is a ζ-NATIVE Level-3 observable (so §VII.CB's Level-3 row is permanently held on the partial-sum channel and re-anchored). It could save the S108 wave from running toward a foregone conclusion AND name the ζ-native re-anchor target if the gap is structural.

**Why solo-not-workshop**: There is no competing-reading divergence on disk. The W1 WP gives ONE reading (structural gap, asserted) and routes the discriminating test to a compute (`CF-S108-VIICB-MAGNITUDE-REMEDIATION`); no second agent holds an opposing position, and the housekeeping ledger explicitly records "No adversarial-physics workshops surfaced" for S107. The task is an independent first-principles assessment (spectral-zeta analytic-continuation tail vs Weyl partial-sum truncation asymptotics), not an adjudication between two agents who must rebut each other. This is exactly the rule's "EXISTING claims that need ADVERSARIAL TESTING — audit what we already claimed" (`Investigating-Workshops.md §"How to identify a real workshop"`), which the rule classifies as solo synthesis, not a 2-agent workshop. The 3-question discriminator lands Q1=NO (no math/physics adjudication between competing readings — there is one reading + a compute route), and the surviving routing is a solo pre-screen.

**Agents**: `spectral-geometer` (owns heat-kernel asymptotics, Seeley-DeWitt coefficients, spectral-zeta regularization vs Weyl partial-sum truncation — the primary author of the partial-sum↔ζ-sum reachability question)
*Default: 1 agent (the primary author). A second agent adds no independent multi-perspective value here — the question is a single-domain spectral-geometry assessment, not a cross-domain composition.*

**Invocation** (NO `--type`, NO `--rounds` — `/rclab-review` is solo-only):
```
/rclab-review sessions/session-107/session-107-w1-workingpaper.md sessions/session-plan/session-107-plan-w1.md sessions/permanent-results-registry.md --agents spectral-geometer --session 107 --context "S107 W1 ran ONE gate, S107-VIICB-MAGNITUDE-CONVERGENCE-ANCHOR (verdict file line 15), to discharge the single HELD Level-3 row of the EXISTING §VII.CB cross-pillar bridge (Pillar I↔VI↔IV; theorem-STRUCTURE STAGE-3-PERMANENT at S106). Verdict: FAIL (robust, direction-neutral). The gate measured the magnitude channel M(L)=Tr_{M_2(C)}(P_a2·T^{(IV)})|_L against the binding L^{-3} Level-2 envelope. NUMBERS: res(L=10)=2.941453e-01 (~294x above the 1e-3 envelope, PRIMARY FALSE); alpha_fit=-0.954042 (decreasing — sign correct — but |alpha|=0.954<2.0, far below the [2,4] FLOWING band, SECONDARY FALSE); composite FAIL = PRIMARY-FALSE AND SECONDARY-FALSE. M(L) series: M_L8=1774.0457, M_L10=1959.5694, M_L12=2095.9052; g_M=a_2_FW_zeta=2776.165389 (canonical_constants.py line 610, gate S88-A-N-FW-CANONICALIZATION, regulator a_2^{zeta}). Lift-robust: all three lift dictionaries FAIL both sub-criteria (D1 exterior-only res=0.294/|alpha|=0.954; D2 core-only res=1.885/|alpha|=0.241; D3 band-centered res=2.207/|alpha|=0.016; D2/D3 even DIVERGE) — a genuine gate closure, not a lift-dependent INFO. C1 sign=-1 (delta_L10=M(L=10)-g_M=-816.60<0; §VII.AF.1-negative fork; diagnostic only, dual-prior left at 50/50, NOT chained). The W1 WP ASSERTS BUT DOES NOT ESTABLISH the discriminating interpretive claim: that the partial-sum vs zeta-sum gap is STRUCTURAL ('not a slow-convergence artifact', WP §'Solution-space consequence' + Wave-1 Synthesis). Its own evidence is suggestive only: the truncated curvature-degree-2 moment Z(L)=Sigma_{k<=L}|lambda_k|^{-6} ~ 383-431 at L in {8,10,12} (Richardson limit ~632, own exponent p~0.52) sits 4-7x below the zeta-regularized target g_M=2776.165389. TASK (independent first-principles analytic assessment — do NOT run the S108 compute): determine whether a TRUNCATED partial moment Sigma_{k<=L}|lambda_k|^{-6} of D_K^2 at the s=3 curvature grade can EVER reach the ZETA-REGULARIZED (analytically-continued) a_2 at the binding L^{-3} rate, OR whether the zeta-value is irreducibly tail-dominated (the analytic-continuation contribution lives in the spectral tail the L<=12 partial sum cannot reach at L^{-3}). Ground the verdict in spectral-zeta analytic-continuation tail structure vs Weyl partial-sum truncation asymptotics — Seeley-DeWitt / heat-kernel reasoning, NOT a numerical re-run. DELIVERABLE: (1) an analytic STRUCTURAL-vs-ARTIFACT verdict on the partial-sum -> zeta-sum reachability at L^{-3}; (2) if STRUCTURAL, NAME the zeta-NATIVE Level-3 re-anchor observable §VII.CB should use (so its Level-3 row is permanently held on the partial-sum channel and re-anchored to a zeta-native quantity); (3) if ARTIFACT, predict the L at which res<1e-3 and confirm the S108 {12,14,16}/Abel route is worth running. Cross-reference the §VII.AF.1.OP-PROJ over-performance precedent (d=4 substrate-distance-1 pole, err_STRICT=0.0095%, 10x INSIDE envelope, registry lines 14918-14951) and the §VII.AU under-performance sibling (d=4,s=3, empirical exponent 2.6926<3) — these bracket the (d=4,s=3) finite-L behavior §VII.CB inherits. Apply substrate-first framing: the substrate IS the spectral-zeta a_2 (the a_2 Seeley-DeWitt coefficient generates the emergent metric g_M); the partial moment is the finite-L truncation of that substrate-IS quantity, NOT a container the zeta-value lives in. STRUCTURED MATH CARRY-FORWARD (4-field what/inputs/gate/effort) MANDATORY per feedback_fix-in-session-never-defer.md: emit a CF that SHARPENS or SUPERSEDES the existing CF-S108-VIICB-MAGNITUDE-REMEDIATION (already in session-107-w1-workingpaper.md §'Carry-Forward Computations') — e.g., re-pointing it at a zeta-native Level-3 observable instead of a higher-L partial-sum mesh if the gap is structural — and route the sharpened CF to /rclab-plan via the W1 WP CF block (it is NOT a workshop and does NOT belong in this schedule). Do NOT re-derive the FAIL; it is a settled, lift-robust, direction-neutral gate closure. The §VII.CB theorem-STRUCTURE (STAGE-3-PERMANENT, S106) and the Level-1 cohomology-class identity [T^{(IV)}]_{a2,HKR}=[g_M]_{a2,HKR} are UNAFFECTED by this FAIL — only the finite-L numerical Level-3 anchor on the magnitude channel fails."
```

*Source seeds: w1 (sole originator). The w2/w3/w4 cross-wave flags reference this §VII.CB discharge only as a surface-only "feeds the S108 registry-completeness/§VII-hygiene queue" note (no contradiction, no shared gate); they add no second perspective and do not promote this to a workshop.*

---

## Slot 2 — Workshops (`/rclab-workshop`)

**(none.)**

Zero Slot-2 workshops is the honest, expected S107 output. The 3-question discriminator (`Investigating-Workshops.md`; first YES wins) was re-applied to every candidate the four investigators surfaced and to every `## Cross-wave flags` entry:

- **The four W2 Stage-2 gates** (K2 §VII.AC.1, K7 §VII.X.W4-1, K9 §VII.X.2-NECESSITY, K11 §VII.AC.4) are `[VERIFY-THEOREM]` blind cross-axis verifies — exactly `Investigating-Workshops.md §"is NOT a workshop"` item 2 ("Verification gates ... have pre-specified protocol; nothing to adjudicate"). Per gate, both blind reviewers AGREED on the structural PASS-AND AND on the single pre-registered INFO locus (Q1=NO); each resolution is a registry-state / gate-finalization / provenance-hygiene move (Q2=YES) with a named S108 forward CF. The plan and EVOI §6 both classify the cohort as Q3 (structurally-orthogonal axes; reviewer-A cannot meaningfully rebut reviewer-B).
- **The one ledger-noted borderline** — *does a grandfathered/audit-substituted Element-2 completeness gap block a Stage-2-structurally-PASS bridge's STAGE-3 promotion?* (symmetric across K2/K7/K9/K11) — is Q2, not Q1: a registry-state-classification choice per `Investigating-Workshops.md §"is NOT a workshop"` item 7. Both reviewers and the team-lead AGREE on the substrate physics; only the promotion bookkeeping is at issue, and it is already settled by applied precedent (hold the promotion; record the structural PASS-AND; route the completeness fix to S108). The housekeeping ledger (`session-107-housekeeping.md:10`) states it surfaces as a workshop ONLY if the conservative precedent is contested — and no contestation has occurred. All four chunk investigators independently declined to promote it; the consolidator concurs. (If the user/orchestrator later judges the precedent contested, the natural panel is a METHODOLOGY adjudication — a registry-anatomy reviewer vs a joint-theorem-promotion reviewer — but that is a future contingency, not a current candidate.)
- **W3** (SDW-2nd-moment INFO-marginal; ⟨r⟩-trend flat-Poisson INFO) — both gates closed INFO at their pre-registered most-likely dispositions (Q1=NO; the marginal r_2nd=0.1604 is a pre-assigned posterior re-allocation, not a ~0.5σ–1σ detection-vs-noise split). The lizzi functional-sensitivity contrast (Gaussian AMP 0.673 vs Mellin CRUSH 0.0053) is settled by the multiplicative-normalization cancellation invariant (only the FUNCTIONAL-INVARIANT a-ratio driver is gated), not contested. Both lands at Q2 (EVOI-register maintenance / status edits).
- **W4** (DESI-DR3 PRE-REG-INC, blocked-pending-external-data) — Q1/Q2/Q3 all NO: the directional content is a Sage-exact closed arithmetic (δ_wa=+0.730, 73/25=2.92σ vs DR2), the four sub-rules are FROZEN at registration (the gate FIRES them, it does not contest them), the only nonzero-w_a route (substrate compaction) is already CLOSED wrong-sign (S66 PROVEN), and the block is a data-availability state (no public DR3 until ~2027), not a physics disagreement.

**Cross-wave CONTRADICTION scan**: zero. Every cross-wave flag is a dependency/dedupe note (K2/K11 are companion rows of one SOURCE-DOUBLE-CITE-CO-PRIMARY pattern sharing the AC-family s=3 Mellin-pole root → sequence together under one CF; the L4-reversibility-band ↔ branch-iv-evaluator forward-coupling → already pinned at EVOI #7c) or a surface-only "the one candidate lives in another chunk" pointer. No flag names a genuine cross-wave contradiction (no PASS↔INFO/FAIL conflict between waves on a shared observable). Nothing promotes to a workshop from the flags.

---

## Slot 3 — Closeout (`/rclab-review`; depends on Slot 1 + Slot 2 outputs)

**(none.)**

With zero Slot-2 workshops there are no workshop verdicts to close out into a combined-landscape synthesis. The single Slot-1 solo (S-1) is itself a self-contained analytic pre-screen whose downstream is a SHARPEN of the already-pinned `CF-S108-VIICB-MAGNITUDE-REMEDIATION` (W1 WP `## Carry-Forward Computations`) — consumed directly by `/rclab-plan` at S108 plan-freeze, NOT by a closeout synthesis. A Slot-3 entry here would be padding (`Investigating-Workshops.md §"'No workshops' is a valid output"` + `feedback_max-effort-full-fidelity.md` length-is-not-quality). The honest output is empty-with-rationale.

---

## Post-Campaign Deliverable Summary

After the single synthesis lands, the following file exists in `sessions/session-107/`:

| File | Produced by | Feeds into next session as |
|:-----|:------------|:----------------------------|
| `sessions/session-107/session-107-spectral-geometer-synthesis.md` | S-1 solo (`spectral-geometer`) | An analytic STRUCTURAL-vs-ARTIFACT verdict on the §VII.CB partial-sum↔ζ-sum reachability at the `L⁻³` rate; if STRUCTURAL, the named ζ-native Level-3 re-anchor observable for §VII.CB; if ARTIFACT, the predicted L for `res<1e-3` confirming the S108 {12,14,16}/Abel route; a 4-field math carry-forward SHARPENING/SUPERSEDING `CF-S108-VIICB-MAGNITUDE-REMEDIATION` (routed to `/rclab-plan` via the W1 WP CF block, NOT this schedule) |

**Total expected outputs**: 0 workshop MDs + 1 per-agent solo MD = **1 file**.

---

## Planning Input Checklist (populated by this campaign)

Items this campaign produces that the Session 108 planner needs:

- The analytic STRUCTURAL-vs-ARTIFACT verdict on whether the truncated `Σ_{k≤L}|λ_k|⁻⁶` partial moment can reach the ζ-regularized `g_M = a_2_FW_zeta = 2776.165389` at the binding `L⁻³` rate (from S-1) — determines the SHAPE of the S108 §VII.CB remediation wave (higher-L partial-sum mesh vs ζ-native re-anchor).
- If STRUCTURAL: the named ζ-native Level-3 re-anchor observable §VII.CB should adopt (re-points `CF-S108-VIICB-MAGNITUDE-REMEDIATION` away from a higher-L partial-sum mesh).
- If ARTIFACT: the predicted L at which `res<1e-3`, confirming the S108 {12,14,16}/Abel-Richardson route is worth the ~1.0-wave effort.
- A 4-field math carry-forward SHARPENING/SUPERSEDING `CF-S108-VIICB-MAGNITUDE-REMEDIATION` (consumed by `/rclab-plan` via the W1 WP CF block).

**Carry-forwards already pinned at S107 session-close (NOT produced by this campaign; consumed by `/rclab-plan` directly from the WP CF blocks + housekeeping ledger §A/§B — confirmed present on disk, append-only preserved, NOT re-appended here)**:
- `CF-S108-VIICB-MAGNITUDE-REMEDIATION` (W1 WP) — §VII.CB magnitude-channel re-test under alternative lift / higher-L / ζ-reconstruction. *(S-1 SHARPENS this; the sharpened spec still routes to `/rclab-plan`, not the schedule.)*
- `CF-S108-ACFAMILY-S3-MELLIN-PARSE-TREE` (W2 WP, line 283) — resolves K2 §VII.AC.1 single-axis-A-2 + K11 §VII.AC.4 JOINT-3 (shared AC-family s=3 Mellin-pole audit-substituted root); dispatch K2/K11 together.
- `CF-S108-VIIXW41-W7A75-OEFORM` (W2 WP, line 289) — resolves K7 §VII.X.W4-1 q=II Element-2 projector-trace OE-form retrofit; pairs with `CF-S108-VIIAG1-ELEMENT2-OE-FORM-RETROFIT`.
- `CF-S108-VIIX2NEC-STAGE2to3-PROMOTION` (W2 WP, line 295) — resolves K9 §VII.X.2-NECESSITY (verify 6/6 anchor SHAs + reconcile entry-text + 4-surface tag-flip).
- `CF-S108-VIIAG1-ELEMENT2-OE-FORM-RETROFIT` (W2 WP, line 301; canonical Q2 home `session-107-housekeeping.md §B`) — §VII.AG.1 Element-2 OE-form retrofit; pairs with `CF-S108-VIIXW41-W7A75-OEFORM`.

---

## Operational Notes

- **Session ID pinning**: the S-1 invocation uses `--session 107` explicitly. Skill auto-detect may pick up a different session from the first source doc; the explicit pin prevents mis-routing.
- **Output path**: the S-1 solo uses the skill default `sessions/session-107/session-107-spectral-geometer-synthesis.md`. No `workshops/` outputs (Slot 2 empty).
- **Dispatch count**: Slot 1 = 1 agent (single dispatch). Slot 2 = 0 workshops × 0 turns = 0. Slot 3 = 0. **Total = 1 agent dispatch.**
- **Concurrency cap**: not binding (1 dispatch ≪ 8-concurrent cap).
- **Length targets**: none — the S-1 context specifies content requirements (analytic verdict, ζ-native re-anchor name if structural, predicted-L if artifact, 4-field CF) only.
- **Structured carry-forward (math-only)**: the S-1 context includes the 4-field carry-forward mandate (what/inputs/gate/effort) per `feedback_fix-in-session-never-defer.md`. ONLY a 4-field-complete item propagates forward; S-1's CF SHARPENS the existing `CF-S108-VIICB-MAGNITUDE-REMEDIATION` and routes to `/rclab-plan` via the W1 WP CF block.
- **Honest count**: 1 Slot-1 solo, 0 Slot-2 workshops, 0 Slot-3 closeout. A near-empty schedule is the correct S107 output — S106 + the bh-cosmo-incursion adjudication both closed cleanly, the four W2 INFO outcomes are pre-registered structured dispositions, and the housekeeping ledger (authoritative Q2 filter) records "No adversarial-physics workshops surfaced." No padding per `feedback_fix-in-session-never-defer.md` + `Investigating-Workshops.md §"Honest count discipline"`.
- **No net-new carry-forward appended**: every CF the seeds reference is already in the WP CF blocks (W1: CF-S108-VIICB-MAGNITUDE-REMEDIATION; W2: the four CFs at lines 283/289/295/301) and mirrored in `session-107-housekeeping.md §A/§B`. Verified present on disk; append-only preserved them; nothing net-new surfaced by any investigator. No CF append owed.

---

*End of S107 workshop schedule. Draft 2026-06-14.*
