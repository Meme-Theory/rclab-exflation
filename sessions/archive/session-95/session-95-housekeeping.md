# Session 95 Housekeeping Ledger

**Date**: 2026-05-28
**Session**: 95
**Authoritative scope**: `.claude/rules/Investigating-Workshops.md §"Q2"`

> Incremental: written per-wave at wave-close (`/rclab-coordinate` Step 6). Waves 2–7 append to §A and add §B–E entries as they close; §F counts updated per wave.

## Q2 marker (citation)

A candidate is Q2 iff its resolution is a status-tag edit / mechanical promotion / rule-file diff / audit-script extension / mechanical re-run, rather than a derivation that produces a new structural claim. See `Investigating-Workshops.md §"Q2"` for the full marker list.

---

## §A. In-session resolutions (already effected; ledger only)

Per `feedback_fix-in-session-never-defer.md`: items below were FIXED during S95 wave compute.

| # | Source wave / gate | Item | Resolution (file:section) | Verified at (audit_sha256 short) |
|:--|:-------------------|:-----|:--------------------------|:---------------------------------|
| A1 | W1 §W1-1 `CF-S95-HK-1` (PASS) | §VII.BG α_s T5 Connes-Karoubi transport bridge **STAGE-1-CANDIDATE → STAGE-3-PERMANENT** (canonical two-agent Stage-2 cross-axis PASS-AND: lizzi+volovik, non-connes; JOINT Δ_scheme=0 bit-exact) | `sessions/permanent-results-registry.md §VII.BG` (header + Status + Stage-2-status section) | `ad229035` |
| A2 | W1 §W1-3 `CF-S95-VII-BE-TIER2-REANCHOR` (PASS) | §VII.BE FWD-C4 Pati-Salam bridge STAGE-1-CANDIDATE → STAGE-3-PERMANENT (numerical Level-3 re-anchored at convergent pole s=6 + structural Stage-2 PASS-AND S93 W6-4) — **SUPERSEDED by S95 S-1 (see A24): promotion REVERTED to STAGE-1-CANDIDATE; the S93 W6-4 Stage-2 was composite INFO on BOTH axes (STAYS-STAGE-1-CANDIDATE), so Stage-3 requires a FRESH two-blind-axis Stage-2 (`CF-S96-VII-BE-STAGE-2-RE-VERIFY`, §B). The s=6 re-anchor PHYSICS stands; only the promotion-route inference is corrected.** | `sessions/permanent-results-registry.md §VII.BE` (header + Status + S95 W1-3 promotion annotation + deferred-pending row (i) + ladder Level-3 row) | `71aea792` (superseded by S-1) |
| A3 | W1 §W1-3 (PASS) | canonical constant `residue_s6_PS_Linf = 9.393639575775e-4` (SU(4)_PS s=6 residue L→∞) added with PROVENANCE | `computations/_shared/canonical_constants.py` SECTION E | `71aea792` |
| A4 | W1 §W1-3 (PASS) | canonical constant `alpha_PS_residue_tail_s6 = 2.803571` (empirical residue tail; tag FI; DISTINCT from HH¹ α=8) added with PROVENANCE | `computations/_shared/canonical_constants.py` SECTION E | `71aea792` |
| A5 | W1 §W1-2 `CF-S95-K-CSUB-R-RE-ANCHOR` (FAIL/boundary) | K_csub_R Tier-2-DIMENSIONFUL-held — **§25 K-counter K=1 → K=2** (structurally-distinct exponential-divergence instance; §25.1's explicit K=2 criterion met) | `sessions/framework/registry/cross-pillar-bridge-corpus.md §25.2` (new) + §25 header | `84c5ec48` |
| A6 | W1 §W1-2 (FAIL/boundary) | K_csub_R **§26 companion** (ENRICH Member A dimensionful-slot-collision; NO §26 K-counter advance, per §24.4 ENRICH precedent) | `sessions/framework/registry/cross-pillar-bridge-corpus.md §26` (companion note) | `84c5ec48` |
| A7 | W1 §W1-2 (FAIL/boundary) | rule-file sync — Tier-1/Tier-2 dimensional-re-anchorability gate status **SUGGESTION K=1 → K=2** (pointer-table row + inline directive), consistent with §25.2 | `.claude/rules/cross-pillar-bridge-anatomy.md` (pointer-table row + inline `### Tier-1/Tier-2 …` directive) | `84c5ec48` |
| A8 | W1 §W1-4 `TES-R1-FI-TRUNCATION-ROBUST` (FAIL/boundary) | provenance clarification recorded — the tesla §8.2 raw triple (a₀=155984, a₂=64308.24, a₄=29086.18) is the d²-weighted mode count at Peter-Weyl **p+q≤3**, NOT p+q≤10; flagged for the `phonic-exflation-equation` §8.5 doc-workshop (no `canonical_constants.py` pin exists for the raw triple — clarification only, no constant edit) | `sessions/archive/session-95/session-95-w1-workingpaper.md §"Effected In-Session"` + this ledger | `622ab243` |
| A9 | W2 §W2-2 `S95-W2-2-EXHAUSTION-FALSIFIER` (PASS) | Inner-Fluctuation Exhaustion Theorem dim HH¹(A_K,A_K)=dim HH²(A_K,A_K)=0 recorded **STAGE-1-CANDIDATE** (constructive symbolic-exact; inner fluctuation FORCED; structural falsifier). PERMANENT registration deferred to §B `CF-S96-HH1-HH2-INDEPENDENT-VERIFY` (single-agent proof) | `sessions/archive/session-95/session-95-w2-workingpaper.md §"Effected In-Session"` + Synthesis | `2bc553db` |
| A10 | W2 §W2-3 `S95-W2-3-NO-WELL-ONE-LOOP` (PASS) | E7 no-landscape/no-well corollary recorded ONE-LOOP-ROBUST (was tree-level; dΓ/dτ>0, 0 interior sign changes, 3 routes); §1.3a framework-doc note strengthening **EFFECTED via S95 doc-incorporation** (see `session-95-phonic-equation-incorporation-log.md`; §1.3a now carries the one-loop-robust + GHY-boundary-domination + exhaustion HH¹=HH²=0 + τ/q-flow distinction) | `session-95-w2-workingpaper.md §"Effected In-Session"` + Constraint-Map | `14dbd362` |
| A11 | W2 §W2-1 `S95-W2-1-T-STAR-ONELOOP-ORIGIN` (FAIL/boundary) | t\* empirical-irreducibility recorded — corridor "t\* is one-loop" CLOSED; t\* confirmed the sole empirical functional coupling (ledger {τ,Λ,f₀,f₂,f₄}+t\* unchanged) | `session-95-w2-workingpaper.md §"Effected In-Session"` + Constraint-Map | `1c9102f3` |
| A12 | W3 §W3-3 `S95-W3-3-BACK-REACTION-CLOSURE` (INFO) | band-gap constants `Delta_B1=0.371795`, `Delta_B2=0.732026`, `Delta_B3_s53=0.084152` (M_KK, s53/s52 at τ_fold) added with full PROVENANCE by the W3-3 agent; resolves the W3-5-flagged band-gap hygiene | `computations/_shared/canonical_constants.py:431-433` | `64c55958` |
| A13 | W3 §W3-1/§W3-5 (PASS) + §W3-2 (INFO) | capstone-frontier findings recorded — frontier #8 (emergent EP) supported INFO→structural (W3-1+W3-5 both exact-PASS); frontier #1 (a(t)) reframed "structure-closed, magnitude-normalization-open." Frontier-tracker promotion + §6.3 a(t) doc-note **EFFECTED via S95 doc-incorporation** (see `session-95-phonic-equation-incorporation-log.md`; §6.3 now carries the back-reaction-closure framing + Jacobson EoS + #1=#8 EIH-lift unification + Connes-proxy correction; §9 frontier #1 links to #8). W6-routed constant hygiene: `Delta_B3=0.176` PROVENANCE gap + `f₂≈92` CC-dictionary pin (conditional). **GENERICITY-QUALIFIED (S95 Slot-1/S-2, connes-ncg-theorist, `session-95-connes-ncg-theorist-genericity-synthesis.md`)**: both PASSes are GENERIC-IDENTITY-CORED — `κ_EP=1` IS the Lichnerowicz–Weitzenböck `R/4` coefficient of any spin Dirac operator (E5); `noether_ratio=½` IS the Brans–Dicke diffeomorphism Noether contraction factor (cancellation holds for ANY φ/V/G_DeWitt). Substrate content = object-IDENTIFICATION (φ=a₂ Seeley–DeWitt moment; B1/B3 = eigenspaces of ONE D_K, band-independence FORCED by single-operator-ness) + R-monotonicity (S64) obstruction SIGN — NOT the PASS values. Frontier-#8 doc-workshop MUST adopt "structurally-inevitable-on-single-operator-postulate, value-generic," NOT "substrate-uniquely-predicted." Genuine substrate EP prediction deferred to NNLO (`CF-S96-EP-NNLO-CASIMIR-DISCRIMINATOR`). `phonic-exflation-equation.md §9` item #8 updated in-session with this qualification | `session-95-w3-workingpaper.md §"Effected In-Session"` + Synthesis + `session-95-connes-ncg-theorist-genericity-synthesis.md` | `1662b455`/`bb8b14e5` |
| A14 | W4 §W4-1 `S95-W4-1-WHITE-HOLE-KINEMATIC-CONSISTENCY` (PASS) | **Conflict C1 RESOLVED → ASYMMETRIC** (one entry horizon, open supersonic exit; monotone dS/dτ forbids 2nd crossing); transit V.6 "two distinct horizons" STRENGTHEN clause DROPPED. **§6.2 white-hole SYMMETRY EFFECTED via S95 W-1 (C1→ASYMMETRIC STANDS; §6.2 + analog-T KIND-column applied; see workshop + change-log)**: the W-1 workshop (`sessions/archive/session-95/workshops/c1-cs-softening-completeness.md`) CONVERGED — C1→ASYMMETRIC STANDS, over-determined at SIX independent walls; the c_s-softening lives in the condensate band-edge channel (`c_B2`, rho-pinned to 0.0227, finite — not zero), NOT the scalar transit channel the discriminant is built on. The master-doc §6.2 PENDING marker was REMOVED and replaced with the ASYMMETRIC resolution (Effect 1); the analog-T ledger gained a KIND column (`a₂` THERMODYNAMIC-kinematic / `a₄` THERMODYNAMIC-spectral OBSERVED / S63-BLV SONIC — Effects 2+3); a₂-observability HELD pending falsifier F1 (COMPOSITE form locked). PENDING-marker count `1→0` (grep-verified). (The rest of §6.2 — greybody, bi-metric, BAO effacement — was EFFECTED earlier via S95 doc-incorporation, see `session-95-phonic-equation-incorporation-log.md` §"§6.2 follow-up".) | `session-95-w4-workingpaper.md §"Effected In-Session"` + Synthesis + W-1 workshop | `5d1ac75a` (W4-1 anchor; W-1 verdict applied) |
| A15 | W4 §W4-5/§W4-4/§W4-2/§W4-3 | W4 doc-corrections bundle **EFFECTED via S95 doc-incorporation** (see `session-95-phonic-equation-incorporation-log.md`): §5.2/§6.3 "singularity-free"→"censored anisotropic singularity at τ→∞" (W4-5 SP-V1, 12D lift of S49); §6.3 conformal factor = Connes-distance proxy NOT a_eff (W4-4 proxy-distinction correction of the plan's conflation); §6.2 analog-T 3-surface ledger (W4-2 HAW-V1) + "A_s = produced-squeeze × exit-greybody" (W4-3 HAW-V3 STRENGTHEN) | `session-95-w4-workingpaper.md §"Effected In-Session"` + Synthesis | `9ffb4aea`/`7b2093b9`/`e5030430`/`98cb1ed4` |
| A16 | W5 §W5-6 `TAU-FLOW-Q-FLOW-REGISTRY-NOTE` (METHODOLOGY-PASS) | τ-flow/q-flow distinct-axes registry note LANDED **orchestrator-direct** (METHODOLOGY-class): E7 (dS/dτ>0, geometric modulus) ⊥ S62 #19 (dE_ZP/dq>0, conserved charge q=N_pair); CC layer rests on q-flow NOT τ-ramp. Note + WP §W5-6 COMPLETED + verdict line + dual-SHA closure helper | `sessions/framework/correspondence/tau-flow-vs-q-flow-note.md` + `computations/session-95/s95_w5_6_registry_note_closure.py` | `eb5cc45f` |
| A17 | W5 §W5-1/§W5-2 (PASS/INFO) + §W5-3 (PASS) | **Conflict C2 RESOLVED** (diabaticity R_therm=5252≫1 + purity S_ent=0, both integrability-independent of retracted Claim B). §5.3 Ordered-Veil rewrite (diabatic transit-freeze, not integrability permanence; drop t_Hubble) + W5-3 CC-warrant clause-R4 two-clause split (Clause A non-inheritance EXACT / Clause B observed-magnitude re-scoped to C10; thermodynamic not topological) **EFFECTED via S95 doc-incorporation** (see `session-95-phonic-equation-incorporation-log.md`; §5.3 + §7.1 CC box + §9 frontier #5 match the S-4-sharpened volovik-collab wording) | `session-95-w5-workingpaper.md §"Effected In-Session"` + Synthesis | `5ad898fa`/`b7d769be`/`397cf449` |
| A18 | W5 (multi-wave process observation) | recurring **parallel-writer-race** recorded: the shared per-wave WP under 5–6 concurrent writers → Edit mtime races; agents work around with atomic `os.replace` single-shot writers (no data lost). **S96-planning note**: `/rclab-plan` should consider per-agent WP files (or a designated single writer) in high-fanout (≥5-gate) waves | `session-95-w5-workingpaper.md §"Effected In-Session"` (process observation) | (multi-wave; no single SHA) |
| A19 | W6 §W6-6 `F-NL-ROW` (PASS) | f_NL falsifier-inventory **Row #69 LANDED** orchestrator-as-mack-delegate (the transit W6-6 agent computed the value + canonical `max_f_NL_FW=1.505` and flagged Step-3 as a mack follow-up): f_NL=−1.505, 0.47σ vs Planck, squeezed-vacuum Gaussian by Wick; RETIRES the S66 Mack complex-squeezing prediction. (ALSO incorporated as a new §7.1 table row + §7.3/§9 mentions in `phonic-exflation-equation.md` via S95 doc-incorporation — see `session-95-phonic-equation-incorporation-log.md`.) | `sessions/framework/registry/falsifier-master-inventory.md` Row #69 | `077fde64` |
| A20 | W6 §W6-4 `W0-MKK-PROVENANCE` (PASS) | mack A4 + W3/W5-routed constant hygiene CLOSED: `M_KK`/`w0_FW`/`Delta_B3` PROVENANCE-dict entries added (values bit-unchanged); `f₂≈92` noted-unpinned (no consumer = clutter, correctly NOT pinned). The W3-A13/W5-routed `Delta_B3=0.176` + `f₂` items are now RESOLVED (no orchestrator follow-up). (The `phonic-exflation-equation.md` verification-ledger line-506 hygiene flag is now CLOSED via S95 doc-incorporation — `M_KK`/`w0_FW` PROVENANCE present; see `session-95-phonic-equation-incorporation-log.md`.) | `computations/_shared/canonical_constants.py` (SECTION F-hygiene) | `8298cea9` |
| A21 | W6 §W6-3/§W6-2 + process | doc-corrections **EFFECTED via S95 doc-incorporation** (see `session-95-phonic-equation-incorporation-log.md`): §7.1 DE joint-posterior fix (W6-3, two-compilation→one joint posterior, Popovic arXiv:2511.07517v3, ρ≈−0.85, + daggers + pivot caption) + §6.2 BAO effacement-suppression / S43-ring-live-channel (W6-2). §W6-1 clobber-recovery VERIFIED on disk (W6-2's overwrite of the §W6-1 stub was repaired; W6-1 refilled to COMPLETED — a REALIZED clobber, strengthening the A18 parallel-writer note). `_canonical_audit.py` ruff-missing TOOLING NOTE for the session-close `/weave --update` (env issue: missing `ruff` binary, independent of any gate) | `session-95-w6-workingpaper.md §"Effected In-Session"` | `e0ae2393` (W6-2) + W6-3 §7.1 |
| A22 | W7 §W7-3 `CF-S95-W7-23-NARROW-PATH-REGIME-II` (PASS) | `lqg-narrow-path-bridge-class.md` PROMOTED **orchestrator-direct** (correspondence edit): workshop-internal-pending → DOCUMENTED substrate-OWN Regime-II effective geometry (γ_emergent=398.08; √(C₂+1) area ladder slope≈½ R²=0.993; j_equiv closed-form map; 0/10 incommensurate rungs vs SU(2) — rank-2 SU(3) vs rank-1 SU(2)). Frontmatter type + title + status-tag + refinement-pathway item 7 updated. Stage-2 verify → STAGE-3 = §B CF-S96-LQG-REGIME-II-STAGE-2-VERIFY | `sessions/framework/correspondence/lqg-narrow-path-bridge-class.md` | `70b2c5e2` |
| A23 | W7 §W7-2 (FAIL) + §W7-1 (INFO) | W7-2 van-Hove-noun FAIL → `Classification-of-phonon-exflation.md:59` proven_1086 re-word ("van Hove" → "maximal-multiplicity DOS edge") ROUTED to the doc-`/rclab-workshop` (curated-doc track; physics rho_smooth=14.02 invariant). W7-1 methodology note recorded: dispersion-order gates should CV-stabilize c_1 (or |c_2|W/|c_1|→0), NOT order_ratio (1/W-divergent non-invariant); Class-8.2-adjacent S96-planning note | `session-95-w7-workingpaper.md §"Effected In-Session"` | `a1f54312` (W7-2) / `b0a0e174` (W7-1) |
| A24 | S95 S-1 workshop (connes-ncg-theorist solo verdict) | §VII.BE STAGE-3-PERMANENT promotion-route correction: the S95 W1-3 in-session promotion (A2) is **REVERTED to STAGE-1-CANDIDATE — STAGE-3-ELIGIBLE**. The S93 W6-4 Stage-2 was composite **INFO on BOTH axes** (`VII-BE-STAYS-STAGE-1-CANDIDATE`; J2 Level-3<Level-2 SYMBOLIC-only); per `joint-theorem-promotion.md §"Stage 2" INFO criterion` an INFO is STAGE-1-RETAINING, and `§"Stage 3"` needs a Stage-2 PASS (none on disk). The W1-3 numerical Level-3 discharges the deferred clause's NUMBER but via a SINGLE agent — joint clauses require two-blind-axis verify. Registry §VII.BE header + Status + ladder Level-3 row corrected; fresh Stage-2 queued (§B `CF-S96-VII-BE-STAGE-2-RE-VERIFY`). S=6 re-anchor PHYSICS + W1-3 PASS verdict RETAINED. | `sessions/permanent-results-registry.md §VII.BE` (header + Status + ladder Level-3 row) + `sessions/archive/session-95/session-95-connes-ncg-theorist-synthesis.md` | (status-tag correction; no new gate SHA — see W1-3 `71aea792` for the underlying physics verdict) |

---

## §B. Hygiene-promotion compute carry-forwards (4-field spec; mirrored to WP CF)

### CF-S96-HH1-HH2-INDEPENDENT-VERIFY — independent verify of the Inner-Fluctuation Exhaustion Theorem → PERMANENT [Q2-hygiene]

> **Routing note**: Q2-class per `Investigating-Workshops.md §"Q2"` (mechanical re-run / mechanical promotion). Identified at S95 W2 wave-synthesis. NOT a workshop (single non-kaku reviewer first-principles re-derivation; not adversarial). Mirrored to `sessions/archive/session-95/session-95-w2-workingpaper.md §"Carry-Forward Computations"`.

> **Why not §A (fix-in-session)**: the PERMANENT promotion requires a NON-kaku NCG reviewer to re-derive HH¹=HH²=0 from first principles (an independent COMPUTE per `epistemic-discipline.md §"What Counts as Evidence"`); an orchestrator edit cannot supply independent confirmation. The STAGE-1-CANDIDATE record is effected in §A9 now; PERMANENT awaits the verify.

1. **What**: non-kaku reviewer re-derives dim HH¹(A_K,A_K)=dim HH²(A_K,A_K)=0 (per-summand rank counts + Gerstenhaber HH² rigidity Z²=B² + Leibniz-closure reduction of the 3 candidate deformation classes); on PASS, promote to a PERMANENT structural-theorem row in `permanent-results-registry.md` + register the structural falsifier in `falsifier-master-inventory.md` (mack, sole writer).
2. **Inputs**: `computations/session-95/s95_w2_2_exhaustion_falsifier.{py,npz}` (W2-2 PASS, audit `2bc553db…`); `canonical_constants.py`; A_K=ℂ⊕ℍ⊕M₃(ℂ).
3. **Gate**: `S96-HH1-HH2-INDEPENDENT-VERIFY` PASS iff the reviewer reproduces HH¹=HH²=0 (both dims exactly 0; out-of-orbit residual=0) WITHOUT reading the W2-2 script.
4. **Effort**: ~0.5 wave-equivalent.

### CF-S96-LQG-REGIME-II-STAGE-2-VERIFY — Stage-2 cross-axis verify of the substrate-OWN Regime-II effective geometry → STAGE-3-PERMANENT [Q2-hygiene]

> **Routing note**: Q2-class per `Investigating-Workshops.md §"Q2"` (mechanical promotion via the `joint-theorem-promotion.md` 4-stage pathway). Identified at S95 W7 wave-synthesis. NOT a workshop (two BLIND cross-reviewers on opposite axes, not adversarial). Mirrored to `sessions/archive/session-95/session-95-w7-workingpaper.md §"Carry-Forward Computations"`.

> **Why not §A (fix-in-session)**: the STAGE-3-PERMANENT promotion requires a Stage-2 two-agent cross-axis independent-verify (Axis-A connes + Axis-B volovik, both WITHOUT prior workshop context); an orchestrator edit cannot supply independent confirmation. The W7-3 Regime-II characterization (the documented entry) is effected in §A22 now; the Stage-3 promotion awaits the verify.

1. **What**: Stage-2 cross-axis verify of the W7-3 Regime-II characterization — Axis-A `connes-ncg-theorist` (Hochschild-cocycle + HKR-Cheeger-Simons class), Axis-B `volovik-superfluid-universe-theorist` (a_4 BCS-condensation + Bogoliubov-covariance); on PASS-AND crystallize `lqg-narrow-path-bridge-class.md` STAGE-3-PERMANENT.
2. **Inputs**: `sessions/framework/correspondence/lqg-narrow-path-bridge-class.md`; `computations/session-95/s95_w7_3_narrow_path_regime_ii.npz` (audit `70b2c5e2…`); frozen S94 W7-23 cocycle npz (`60e06590…`); `canonical_constants.py`.
3. **Gate**: `S96-LQG-REGIME-II-STAGE-2-VERIFY` PASS iff both reviewers PASS-AND every clause (Hochschild/HKR + BCS/Bogoliubov) WITHOUT the S92 workshop transcript.
4. **Effort**: ~0.5 wave-equivalent.

### CF-S96-VII-BE-STAGE-2-RE-VERIFY — fresh two-agent blind Stage-2 on the now-complete §VII.BE entry → STAGE-3-PERMANENT [Q2-hygiene]

> **Routing note**: Q2-class per `Investigating-Workshops.md §"Q2"` (mechanical promotion via the `joint-theorem-promotion.md` 4-stage pathway), structurally identical to `CF-S96-LQG-REGIME-II-STAGE-2-VERIFY` above. Identified at S95 S-1 (connes-ncg-theorist solo promotion-route verdict; see §A24 + `session-95-connes-ncg-theorist-synthesis.md`). NOT a workshop (two BLIND cross-reviewers on opposite axes; not adversarial). Mirror to `sessions/archive/session-95/session-95-w1-workingpaper.md §"Carry-Forward Computations"`.

> **Why this exists**: the S95 W1-3 in-session STAGE-3-PERMANENT promotion (A2) was REVERTED at S-1. The S93 W6-4 Stage-2 was composite INFO on BOTH axes (`VII-BE-STAYS-STAGE-1-CANDIDATE`); the `joint-theorem-promotion.md §"Stage 2" INFO criterion` is STAGE-1-RETAINING and `§"Stage 3"` requires a Stage-2 PASS. The W1-3 numerical Level-3 (ratio 0.831<1 at s=6) discharges the deferred clause's NUMBER but via a SINGLE forward-compute agent (`lizzi`); joint clauses (J2/J3) require two-blind-axis verification. The §VII.BG W1-1 route (fresh two-agent Stage-2) and the W7-3 reservation both obey this; §VII.BE must too.

1. **What**: Stage-2 two-agent parallel cross-axis independent-verify of the NOW-COMPLETE §VII.BE entry (convergent-pole s=6, empirical `L^{−2.882}` envelope, numerical Level-3 = 7.687e-4 < Level-2 = 9.252e-4, ratio 0.831). Both reviewers BLIND (read ONLY the registered §VII.BE entry + cited inputs; NOT the S91 W7 workshop, NOT the S93 W6-4 reviews, NOT the W1-3 WP). **EXCLUSIONS**: `connes-ncg-theorist` (S93 axis-A author + S-1 adjudicator), `lizzi-spectral-functional-theorist` (W1-3 numerical-clause author), `volovik-superfluid-universe-theorist` (§W9-12 co-author). Axis-A = a spectral/NCG reviewer other than connes; Axis-B = a substrate/condensed-matter reviewer (`landau-condensed-matter-theorist` admissible — entry re-anchored after his S93 review). PASS-AND every single-axis clause (A1-A4 / B1-B4) + every JOINT clause (J1, J2/J3 NUMERICAL Level-3<Level-2 at s=6) across both axes.
2. **Inputs**: `sessions/permanent-results-registry.md §VII.BE` (now-complete, REVERTED-to-STAGE-1-CANDIDATE); `computations/session-95/s95_w1_3_vii_be_tier2_reanchor.npz` (W1-3 PASS, `71aea792…`); `canonical_constants.py` (`residue_s6_PS_Linf`, `alpha_PS_residue_tail_s6`); S94 W3-9 SU(4)_PS full-spectrum npz (`697fe532…`) for the s=4-diverge / s=6-converge cross-check.
3. **Gate**: `S96-VII-BE-STAGE-2-RE-VERIFY` PASS iff BOTH reviewers return composite PASS on single-axis clauses AND all JOINT clauses PASS-AND (logical AND), with the NUMERICAL (not symbolic) Level-3<Level-2 at s=6 PASS-AND'd across both axes, WITHOUT either reviewer reading the workshop/W1-3 transcripts. On PASS-AND → §VII.BE STAGE-1-CANDIDATE → STAGE-3-PERMANENT (mack effects the flip). On INFO/FAIL → stays STAGE-1-CANDIDATE.
4. **Effort**: ~0.5 wave-equivalent (two parallel blind reviewers + one PASS-AND aggregator; identical machinery to S95 W1-1 §VII.BG `CF-S95-HK-1`).

(Note: W1's `CF-S96-K-CSUB-R-EXTERNAL-CHANNEL-SCALE` is NOT a §B item — it is a genuine NEW-physics computation (re-source a scale from a non-IR channel), so it lives in the W1 WP `## Carry-Forward Computations` as a math CF, not here.)

---

## §C. Parallel-compute-wave carry-forwards (Q3 wave-together; mirrored to WP CF)

(none in W1.)

---

## §D. Methodology-rule extensions (M1-M4 + allowlist; mirrored to WP CF)

(none in W1 — the Tier-1/Tier-2 K=2 status sync (§A7) was a bare-status edit effected in-session, not a deferred M1-M4 rule extension.)

---

## §E. Pre-compute shell waves (upstream escalation; NOT a CF)

(none — ALL 7 waves (W1–W7) were dispatched and CLOSED this S95 `/rclab-coordinate` run; no wave left un-dispatched, no pre-compute shells. Session-end confirmed.)

---

## §F. Structural counts (artifact shape; not length)

| Category | Count (through W1–W7 + S-1) |
|:---------|------:|
| §A In-session resolutions | 24 (A1–A24; A24 = S-1 promotion-route correction) |
| §B Hygiene compute CFs (mirrored to WP) | 3 (incl. `CF-S96-VII-BE-STAGE-2-RE-VERIFY` from S-1) |
| §C Q3 parallel-wave CFs (mirrored to WP) | 0 |
| §D Methodology rule extensions (mirrored to WP) | 0 (S-1's `CF-S96-JTP-INFO-CLAUSE-DIRECTIVE` flagged in the S-1 synthesis §8; routes at S96 plan-freeze via M4) |
| §E Pre-compute shell waves (escalation only) | 0 |
| **Total Q2-class items surfaced (S95 complete, W1–W7 + S-1 workshop)** | 27 |

---

## Consumption pointers

- **`/rclab-investigate` (S95)**: read this file BEFORE producing candidates. Every §A entry is a non-workshop (already effected).
- **`/rclab-plan` (S96)**: §A is ledger-only — do NOT re-dispatch. The W1 math CF (`CF-S96-K-CSUB-R-EXTERNAL-CHANNEL-SCALE`, CONDITIONAL) is in `sessions/archive/session-95/session-95-w1-workingpaper.md §"Carry-Forward Computations"`.

---

*S95 housekeeping ledger — COMPLETE (W1–W7 all closed). 25 Q2-class items: 23 §A in-session resolutions + 2 §B hygiene-compute CFs (CF-S96-HH1-HH2-INDEPENDENT-VERIFY, CF-S96-LQG-REGIME-II-STAGE-2-VERIFY; both mirrored to their WP CF blocks). Session-close `/weave --update` pending (W6-1/W6-6 new-constant promotions `n_PBH_FW_saturated_tail` + `max_f_NL_FW`, the S95 W1-3 `residue_s6_PS_Linf`/`alpha_PS_residue_tail_s6`, + the W6-5 `ruff`-missing tooling note for `_canonical_audit.py`).*
