# Papers Review Campaign — post-S103 (2026-06-12)

**Trigger**: user directive — `papers/` content is out of date (written ~S50-S53 / S87 by a legacy model); needs dramatic review + rewrite of all items, plus a search for new paper topics in the current framework results.

**Structure**: two-phase. Phase 1 (this directory) = REVIEW ONLY — one specialist reviewer per item, sole-writer reports, no paper edits. Phase 2 = rewrite dispatches executed against the §6 rewrite plans in these reports.

## Phase 1 roster (one sole-writer report per row)

| Item under review | Era | Reviewer agent | Report file |
|:------------------|:----|:---------------|:------------|
| `papers/alpha-s-ns/main.tex` (456 ln) | ~S50-S53 | mack-cosmic-bridge | `review-alpha-s-ns.md` |
| `papers/anderson-higgs/main.tex` (423 ln) | ~S50-S53 | connes-ncg-theorist | `review-anderson-higgs.md` |
| `papers/cmpp-classification/main.tex` (604 ln) | ~S50-S53 | schwarzschild-penrose-geometer | `review-cmpp-classification.md` |
| `papers/monotonicity/main.tex` (1304 ln) | ~S50-S53 | spectral-geometer | `review-monotonicity.md` |
| `papers/methodology/orchestrated-ai-research.tex` (441 ln) | S51 | coordinator | `review-methodology.md` |
| `papers/s87-3he-b-alpha-s-equivalent.md` (606 ln) | S87 | volovik-superfluid-universe-theorist | `review-s87-3he-b.md` |
| `papers/s87-path-h-path-c-interpolation.md` (151 ln) | S87 | lizzi-spectral-functional-theorist | `review-s87-path-h-path-c.md` |
| (new-topic scout — no source paper) | post-S103 | phonon-first-cosmologist | `new-paper-topics.md` |

## Report contract (all reviews)

§1 claim-audit table (paper value vs current canonical + source, status ∈ {CURRENT, DRIFTED, SUPERSEDED, RETRACTED, STILL-OPEN}) · §2 what survives · §3 what must change · §4 new results since paper era · §5 bibliography/anchor audit · §6 mechanically-executable rewrite plan · §7 verdict ∈ {REWRITE-IN-PLACE, RESTRUCTURE, RETIRE-AND-REPLACE}.

## Orchestrator-verified staleness anchors (seeded into prompts)

- `alpha_s_inflation_framework = n_s²−1 @ observed pivot` → SUPERSEDED (S92 AH-TR-1); canonical is the two-observable split `alpha_s_pivot_goldstone = 0.0` (+0.67σ Planck) / `alpha_s_substrate_distance_1 = −0.08587279` (Mellin s=3, FI-class, sign-walled), separated 54.04 decades, discriminated by `deg(T_BZ→pivot) = +2` NON-SCALAR (S93 W7-1). Source: `canonical_constants.py` lines 511, 623-624, 2299-2300.
- `n_s_framework = 0.9561`; `n_s_FW_exact = 9561/10000` bit-exact (α_s = −8587279/10⁸ exactly in ℚ); `n_s_FW_sqrt_cutoff = 0.9590` S103 COMMIT branch (Row #85). Source: lines 704, 2404-2405.
- `r_PathH = 0.0074705` (S86 forward-derivation; the draft-cited "S85 W2 OQ-7" provenance was a label-confusion error per the constants PROVENANCE); `r_CMB_framework = 0.011731522176014426` (S83 G46). Source: lines 31, 575-576.
- 3He-B: inheritance DIRECTION = post-hoc stipulation (S97-S99 re-audit); universality-class membership (BDI/N₃=0/χ) is the load-bearing strength; CF-35 (7.324992 provenance) OPEN; BBN ³He/H closed FAIL S73A/B.
- Monotonicity: theorem PERMANENT (S36, re-derived S77 — see `sessions/framework/registry/spectral-post-mortem.md`); one-loop τ-selection corridor CLOSED S95 (T-STAR-ONELOOP-ORIGIN FAIL, NO-WELL-ONE-LOOP PASS).
- Methodology paper stats are S51-era (51 sessions / 29 agents / 630 scripts / 392 theorems / 82k entities) — all require recount at S103.
- Unresolved `\cite{needed:…}` placeholders: alpha-s-ns 10, anderson-higgs 27, methodology 6, cmpp 0, monotonicity 0.

## Phase 2 — EXECUTED (2026-06-12, same day)

All seven verdicts executed. Reviewers were resumed as their own rewriters (context-intact); the orchestrator handled the retirement, register fixes, and builds.

| Item | Verdict | Outcome |
|:-----|:--------|:--------|
| alpha-s-ns | RESTRUCTURE | Retitled "Two Scale-Separated Running Observables…"; §3 math kept verbatim + exact-ℚ remark; confrontation rebuilt on the S93 transport-degree resolution; 10 `needed:` keys → real refs; SCALE-AND-CHANNEL compliant. Build: 18 pp, **0 issues** |
| anderson-higgs | REWRITE-IN-PLACE | 27 TODO prefixes stripped (entries were real); 3 bib repairs (Baptista → arXiv:2306.01049 / 2506.09126); Killing/non-Killing dichotomy + isometry-obstruction duality + m_H=131.8 consistency added; npz-reverified numbers. Build: 16 pp, **0 issues** |
| cmpp-classification | REWRITE-IN-PLACE | 10⁷ → 2.27×10⁷ canonical; S77 overshoot τ=1.614 + S85 dense-grid 171/171 + S95 NEC censor + S96 Weyl-fraction peak integrated; bib repairs (Koiso 1980, Ortaggio 2013, Milson 2004 added); internal `@misc` cites → Data Availability. Build: 23 pp, **0 issues** |
| monotonicity | REWRITE-IN-PLACE | Transit-engine reframe (stabilization-hunt removed; Fock-space suggestion deleted — closed wrong-sign); f-orientation convention pinned; **real error fixed: da₄/dτ(0) = 0 exactly, not +0.312** (Sage closed form); L-uniform sign lemma + one-loop robustness added; Bernstein completely-monotone restriction kept; bib repairs (Slebarski Bull. LMS, CCvS 2013 inner fluctuations, Gordon-Sutton 2010). Build: 23 pp, **0 issues** |
| methodology | RESTRUCTURE | Recounted to S106 (sessions ≥106, theorems 2,301, scripts 3,128, gates 3,241, entities 103,767, closed 195 post-dedup, retractions 49, breakthroughs 39, equations corrected DOWN to 19,713); probability-honesty fixed (2-4% scoped as S51-historical; post-S66 suspension stated); new §6 Methodology Floor (13-item spine from atlas-12); rclab pipeline + 34 agents; attribution Opus 4.6-4.8 + Fable 5 revision; framework_paper cite → Berry. Build: 22 pp, **0 issues** |
| s87-3he-b | RESTRUCTURE | Demoted to exposition COMPANION of falsifier-master-inventory; §VII.W-3.LAB STAGE-3-PERMANENT (S100a, 11/11 PASS-AND) added as keystone; α_s re-scoped to substrate-distance with full scale/channel tags; F-table replaced with landed rows (F1/F5 Class-B pairing); canonical ratio 7.324992 (114453/15625); T_pc 2.273 mK; §6 NMR running-of-running deleted (in no register); S97-S99 post-hoc-stipulation caveat + CF-35 caveat explicit |
| s87-path-h-path-c | RETIRE-AND-ABSORB | Archived to `papers/_archive/` with 4-line frontmatter; **atlas-09 Item 50** (design-note SUPERSESSION, not a retraction) records it; residue already canonical at §VII.AB.6 + phononic-framing |

### Register-side fixes applied in-session (orchestrator + mack)

- atlas-07 A6: "Three independent proofs" → two-arguments+verification (matches the 2026-03-20 peer-review restructure); recommended-paper #3 retitled. Registry §index row 16: same correction.
- atlas-07 §XVI: **three unsupported "PERMANENT" tags down-corrected to STAGE-1-CANDIDATE** — §VII.AC.1, §VII.AD, §VII.X.2-NECESSITY (registry tags + atlas-04 K2/K3/K9 "Stage-2 pending" are the register-of-record; the one-off "post-Stage-2 eq" phrase had no Stage-2 PASS-AND anywhere; atlas-04's S106-plan-freeze reconciliation consciously left these pending).
- falsifier-master-inventory (mack, sole writer): band-center Sage-exact annotation; Row #46 ratio-form superseded-by-#47-#51 note; CF-15 cross-rank refreshed from superseded −0.0690 to canonical −0.08587279 with scale/channel tags.
- canonical_constants: m_H_obs PROVENANCE added — **value 125.1 is the ATLAS+CMS Run-1 combination (arXiv:1503.07589), NOT PDG 2024 as the old comment claimed**; load-bearing as exact-rational denominator (67/1251, 89/1251); value unchanged.
- CMB-S4 Science Book (1610.02743) σ(α_s) citation VERIFIED against the fetched source: "σ(n_run) = 0.002–0.003" — the paper's 2.3e-3 is inside the band. PASS, no edit.
- Root-level PDFs regenerated from the rewritten sources; duplicate `Spectral-Index-for-Ornstein-Zernike-Operators.pdf` and the in-dir anderson PDF copy removed; stray `papers/cmpp-classification/.claude/` legacy memory tree removed (content mined into Phase-1 reviews; git history preserves it).

### Carry-forwards (genuine future work; 4-field specs at their cited homes)

1. **CF-S104-MH-OBS-REPIN** — re-pin m_H_obs to PDG-2024 125.25±0.17 OR split into construction-denominator (125.1) + observational-comparison constant. Spec in mack's provenance note at `canonical_constants.py` (m_H_obs PROVENANCE entry). Gated on migrating the exact ratios 67/1251, 89/1251 consistently.
2. **Monotone-f scope adjudication (Q1 workshop candidate)** — register says "S_f monotone for ALL monotone f" (S37, 9,600 checks; E7/A2/CUTOFF-SA-37 rows); the paper's proof covers completely-monotone f (Bernstein), with the general-monotone case computationally supported but structurally open (23.4% of bare eigenvalues individually decrease). Two genuine readings of proof-class scope → workshop per `Investigating-Workshops.md` Q1, NOT a wording edit. Inputs: monotonicity review §2/register flags; S37 closure; the rewritten paper §5. Gate: structural proof for general monotone f OR register down-scope to "completely monotone (proven) + monotone (computational)". Effort: 1 workshop (2-agent, 2-3 rounds).
3. **atlas-07 §XVI status-cell audit (hygiene compute)** — cross-check every §XVI.C-I status cell against registry tags (the campaign verified and fixed 3 rows + found §VII.AC.4 listed as both PERMANENT and STAGE-1-CANDIDATE within atlas-07). Inputs: atlas-07 §XVI tables, registry slot-index + entry Status blocks, atlas-04 §X cohort. Gate: every cell equals its registry tag or carries a dated down-correction. Effort: 1 mechanical pass (~30 rows).
4. **Inventory registry meta-entry (low)** — the framework-reindex hook reports "registry meta-entry not found" on every falsifier-master-inventory edit (pre-existing index-shape note). Adding the meta-block silences it. mack's call.

## Housekeeping noted for Phase 2

- Stray legacy dir `papers/cmpp-classification/.claude/agent-memory/` (orphaned agent memory from the original paper effort; reviewers read it for known-issue leads, then it gets removed).
- `papers/Scrachpad` is the user's 5-paper vision note — input to the topic scout, NOT a rewrite target.
- Root-level PDFs (`oz-spectral-index-identity.pdf`, `spectral-action-monotonicity-su3.pdf`, `ungaugeability-kosmann-dirac.pdf`, `weyl-tensor-cmpp-su3.pdf`, `orchestrated-ai-research.pdf`, `Spectral-Index-for-Ornstein-Zernike-Operators.pdf`) are stale builds of the per-directory sources — to be regenerated from rewritten sources in Phase 2.
