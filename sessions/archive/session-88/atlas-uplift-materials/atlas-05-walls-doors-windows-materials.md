# Atlas-05 Walls / Doors / Windows — S52-S88 Uplift Materials

**Source**: registry extraction packet for orchestrator atlas-refresh dispatch.
**Target atlas**: `sessions/framework/Atlas/atlas-05-walls-doors-windows.md` (mtime 2026-04-04; 36,619 bytes).
**Gap covered**: S52-S88 (sessions S60-S88 dominate the S52-S88 substrate; pre-S60 closures are largely already in atlas-05).
**Compiler**: sagan-empiricist (registry extraction; no new derivations).
**Date compiled**: 2026-05-09.

---

## Section 1: What's currently in atlas-05 (baseline state at 2026-04-04)

Atlas-05 (lines 5-282) catalogues the substrate's structural-exclusion topology in three categories: 10 numbered walls (W1–W10), 13 numbered doors (Door 1–Door 13; the count ran past the atlas-00 line-17 "10 doors" estimate when S62 + S66 added Doors 8–13), 6 numbered windows (Window 1–Window 6; Window 2 is permanently closed), plus one transitional "Candidate Walls (S64-S66) — Not Yet Numbered" section with 3 unnumbered candidates (R-Monotonicity, a_0/a_2 Trap, Frustration Triangle). The wall labels are:

- **W1** Weyl Asymptotic F/B Ratio (S20b/S22c) — F/B = 16/44 tau-independent in UV; closes 6 perturbative spectral functionals
- **W2** Peter-Weyl Block-Diagonality (S22b) — D_K block-diagonal exact; closes 3 cross-sector mechanisms
- **W3** Spectral Gap at mu=0 (S17a/S30Ab) — gap > 0 at all tau; closes 5 mu=0 BCS mechanisms
- **W4** Spectral Action Monotonicity (S37 CUTOFF-SA-37) — definitive monotonicity; closes 13+ single-trace SA mechanisms
- **W5** Berry Curvature Vanishing (S25) — K_a anti-Hermitian to 1.12e-16; preempts topological tau-stabilization
- **W6** NCG-KK Scale Irreconcilability (S30Bb/S31Ba) — Lambda_SA/M_KK = 10^6–10^15 OOM gap
- **W7** alpha_s = n_s^2 - 1 Structural Identity (S50) — 5 independent proofs; closes 3 Josephson-sector n_s mechanisms
- **W8** Anderson-Higgs Impossibility for U(1)_7 (S51) — 3 independent proofs; closes Goldstone mass loophole
- **W9** Convex Combination Theorem for Additive Mixing (S51) — bounds n_s in mixed correlator at K_pivot=2.0
- **W10** Zero-Mode Protection on T^2 (S50/S51) — all-orders Born; closes 2 position-diagonal scattering mechanisms

The 6 windows enumerated are: Window 1 (SA-Goldstone Mixing at K<K*; PRELIMINARY PASS, EFOLD-MAPPING-52); Window 2 (Q-Theory CC Crossing; CLOSED S62 by monotonicity theorem); Window 3 (Off-Jensen 5D Moduli Landscape; UNTESTED); Window 4 (Higher PW Truncation Spectrum; INFO partial); Window 5 (Strutinsky Shell Correction; FAIL at current truncation, depends on Window 4); Window 6 (KK Threshold Corrections for m_H; OPEN). The atlas closes with a Section IV cross-reference between walls and doors (8 entries) and a Section V ASCII constraint-surface diagram (lines 299-336). The atlas mtime predates S86 R3, S87, and S88 — it does not contain any structural-exclusion content from the S86–S88 era.

---

## Section 2: What to add (S52–S88 walls / doors / windows)

### 2a. New walls (W11+)

Each row below has a registry slot or rule-file citation. Walls are STRUCTURAL EXCLUSIONS in the substrate's solution space (not laboratory closures); the impact column states which substrate-IS region is excluded.

| wall-id | name | structural reason | landing session | registry slot / rule cite | impact |
|:--------|:-----|:------------------|:----------------|:--------------------------|:-------|
| W11 | Volovik CC Tracking Wall (DILUTION-CC-66) | Volovik q-theory thermodynamic relaxation: rho_vac ~ M_Pl^2 H^2; rho_vac/rho_obs = 1.032 at present epoch (0.01 OOM from observation); FUNCTIONAL-INDEPENDENT (Gibbs-Duhem rho_vac = epsilon(q) − mu*q → 0 holds for any spectral functional); the 114 OOM gap IS the expansion history, NOT a fine-tuning problem | S66 W1-A + Workshop 4 | atlas-05 line 188-194 (Door 12; PROMOTE TO WALL on framing-revision) + `framework-cc-oom.md` (see Grep theorem proven_17/18) | Excludes the substrate-IS region where CC is treated as a static vacuum-energy fine-tuning problem; converts the 114 OOM gap from "open problem" to "misidentified expansion history" |
| W12 | Eps_H Spectral Functional Sign-Reversal (S66 functional crisis) | The Hubble slow-roll parameter eps_H = (1/2)(dS/dtau)^2/(S * d^2S/dtau^2) sign reverses across cutoff functions: sqrt(x) gives +0.022 (red tilt n_s = 0.9595), zeta/exponential gives negative (blue tilt n_s > 1); n_s spread across functionals 0.164 (39× Planck error); SCHEME-DEPENDENT pending FUNCTIONAL-SELECT-67 | S66 (functional crisis surfaced); S67-S70 era refinements | atlas-05 line 162-165 (Door 8 caveat); §VII.AB.1 Substrate Sign-Lock (S86 W-2; permanent-results-registry.md:14911); FUNCTIONAL-SELECT-67 carry-forward | Excludes the substrate-IS region where a single bare eps_H reading can fix n_s without functional-class declaration; forces every n_s prediction to declare its regulator class |
| W13 | F_4-MB Structural Wall Family (a_0-Unsuppressed-at-LMAX10) | At L_max=10 on the canonical D_K spectrum cache, the substrate's a_0 Seeley-DeWitt slot under {ζ, Zubarev, SDW} ∘ Mellin-Barnes residue ∘ CM-1995-SD-subtraction CANNOT be suppressed below \|Λ_CC^MB\|/\|a_0^trunc\| ≤ 0.5; worst-case ratio 9.4557 (Zubarev); 4 constituent FAILs (S85-W0-7, S85-W0-11, S85-W0-20, S86-W2-1) on shared lens; F_4 = {ζ, Zubarev, SDW} closed on Axis_F4_MB | S86 1a-S1 (volovik+connes+gen-physicist co-signed) | §VII.Z (permanent-results-registry.md:15210); §VII.V WEYL-NON-ASYMP-F_4-MB-NO-GO Corollary A (line 16024) | Excludes the substrate-IS Pillar-III multiplier-algebra route to CC-suppression on F_4; 3 surviving corridors (q-theory C-Q, dilution C-D, Friedmann two-layer C-2L) all on disjoint axes |
| W14 | Algebra-Axis Orthogonality Wall (W-2 R3) | Algebra-INVARIANT vs algebra-DEPENDENT functional families are STRUCTURALLY ORTHOGONAL in identity-class membership: no closed-form {λ_n}-only identity reproduces any algebra-DEPENDENT functional, and conversely no state-functional-only identity reproduces any algebra-INVARIANT spectral moment; conjecture promoted MANDATORY at K=3 calibration corpus instances | S87 W-2 R3 close (lizzi PRIMARY + connes CO-AUTHOR + mack CO-AUTHOR) | `.claude/rules/cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`; `pru-class-corpus.md §6` | Excludes the substrate-IS region where a substrate observable can be cited in single-axis form when both algebra-axes are admissible; forces every theorem text to declare its axis (corner-cell + pole) |
| W15 | Cross-Corner Co-Primary Wall (S88 W-15 V.6) | Two anchors on different algebra-axes (one on Cell I `n_s²−1` algebra-INVARIANT spectrum-only-functional cell, one on Cell IV variance theorem algebra-DEPENDENT state-pair-functional cell) cannot enter a single non-fungible SOURCE-DOUBLE-CITE-CO-PRIMARY chain; the two cells live on orthogonal algebra-axes (subordinate to W14) | S88 W-15 V.6 (W5a-44 surfacing of §VII.AN cross-corner conflation) | `.claude/rules/registry-landing.md §"Detection (when SOURCE-DOUBLE-CITE-CO-PRIMARY applies)"` clause 4; `_registry_landing_audit.py` Class-(g) extension (S89-CROSS-CORNER-CO-PRIMARY-AUDIT) | Excludes the substrate-IS region where one CO-PRIMARY chain spans two structurally orthogonal cells; forces orthogonal-companion structure when both projections are independently registry-eligible |
| W16 | Layer-2-Non-Binding Bare-Decomposition Wall (S88 W8-88) | Bare-decomposition envelopes (Level-2-non-binding: substrate-internal Mellin-truncation rates with no HKR image to a continuum laboratory observable) DO NOT bind Level-1 cohomology classes; cannot count toward registry-PASS regardless of how tightly the Level-3 anchor satisfies the numerical bound; false-PASS pathway closed by construction | S88 W8-88 (gen-physicist PRIMARY + connes-ncg-theorist CO-AUTHOR rationale review) | `.claude/rules/cross-pillar-bridge-anatomy.md §"Level-2 Layer Distinction"` (MANDATORY at K=3 promotion at S88 W-22 W7a-74 V.5 close) | Excludes the substrate-IS region where a `L^{-α}` algebraic envelope on a substrate-internal Tr(D_K^{-2s}) can pose as cross-pillar bridge evidence; routes to plan-freeze halt with HKR map citation requirement |
| W17 | Bare-Eigenvalue Parity-Blindness Wall (S85 W2-7 Bulletin #2) | Even Seeley-DeWitt theorem: even-grading regulator-weighted Mellin moments (η-invariant alone) cannot decode odd-grading HP^1 content on the (C_H, C_epsH) parity-twin pair; canonical (η = 0, GV ≠ 0) signature on parity-twin pair structurally excludes η-only protocols | S85 W2-7 (Bulletin #2 promotion); reinforced S86 W-11 RULE-2 | `.claude/rules/regulator-pin-discipline.md §"Class-(c) PIN-DRIFT-FROM-STALE-SOURCE — W-11 Calibration Corpus Extension"`; §VII.W (permanent-results-registry.md:15003) | Excludes the substrate-IS region where η-detection alone discriminates parity-twin pairs; forces odd-grading observables (GV-Heitsch, K-theoretic torsion, η-Cheeger-Simons secondary classes) on HP^1 detection |
| W18 | Mechanical-Closure Type-F/Type-S Layer-Separability Wall (S88 W8-89) | Type-F (single-summand-projection trace; algebra-INVARIANT) and Type-S (state-pair functional; algebra-DEPENDENT) sub-observables are structurally separated under the algebra-axis orthogonality 4-corner classification; mechanical closure on Type-F is admissible-with-conditions L1-L4 ONLY; mechanical closure on Type-S is NEVER admissible | S88 W8-89 (gen-physicist orchestrator-direct-write; Stage-2 PASS-AND required from connes-spectral + volovik-substrate cross-reviewers) | `.claude/rules/mechanical-closure-discipline.md §"Layer-separability carve-out (admissible-with-conditions)"` (SUGGESTION at K=1) | Excludes the substrate-IS region where state-pair functionals can be silently mechanically closed via Type-F partition admissibility; the convention-tag honesty discipline L4 is the boundary against PROHIBITED_ACTIONS Class 1 |
| W19 | PRU Class 8.0–8.6 Sub-Class Walls (plan-authorship pathologies) | Pre-Registration Underspecification class taxonomy: Class 8.0/8.1 machinery-pin cardinality (S78); Class 8.2 verifier-rubric (S86 W-12, MANDATORY at K=4 S88 W7a-74); Class 8.3 publication-precision (S86 W1c-8, MANDATORY at K=4 S87 W8); Class 8.4 representation-convention-pin (S88 W-16 W5b-50); Class 8.5 joint-hypersurface-pre-registration-form (S88 W-15 W4c-36); Class 8.6 layered-substitution-chain-audit (S88 W-17 W5b-47); each sub-class is a wall against a specific plan-authorship pathology that produced FAILs in pre-S86 sessions | Multiple S78–S88 sessions; Class 8.0/8.1 origin S78; full taxonomy tabulated S88 | `.claude/rules/epistemic-discipline.md §"Pre-Registration Completeness — PRU Class-8 sub-class taxonomy formal extension"`; `pru-class-corpus.md §1-§7` | Excludes the methodology-layer regions where rubric-form failure / precision-floor mismatch / convention-pin drift / hypersurface-form drift / layered-substitution-chain-audit failure can produce false-PASS verdicts; subclasses MANDATORY-at-K=3 promotion threshold |
| W20 | Joint-Theorem Single-Axis Promotion Wall (S86 W-9 RULE-1) | Joint cross-axis theorems CANNOT enter `permanent-results-registry.md` STAGE-3-PERMANENT without 4-stage pathway (Stage 0 workshop-internal → Stage 1 STAGE-1-CANDIDATE registry → Stage 2 two-agent parallel cross-axis verify WITHOUT prior workshop context → Stage 3 PERMANENT); single-agent verification on joint clauses is structurally INSUFFICIENT (audit script `_joint_theorem_independent_verify_audit.py` REFUSES single-agent firings) | S86 W-9 RULE-1 (lizzi+transit, Path-(c) reassessment workshop) | `.claude/rules/joint-theorem-promotion.md` (MANDATORY); first calibration instance §VII.AH (S87 W9a-1) | Excludes the methodology-layer region where shared-context-produced agreement among workshop authors can be mistaken for independent confirmation; the 4-stage pathway is the sole admissible route for joint cross-axis theorems |
| W21 | Cross-Pillar Bridge 5-Anatomy + 3-Level Wall (S86 W-5 RULE-1+2; MANDATORY at K=3 S88 W4a-17) | Every cross-pillar bridge entry MUST declare ALL 5 IS-not-IN anatomy elements (substrate-IS observable / laboratory-IN observable / bridge map / algebraic envelope / empirical anchor) AND the 3-level structural-confidence ladder (Level-1 cohomology-class identity / Level-2 algebraic envelope / Level-3 empirical anchor); Level-3 must satisfy Level-2 at canonical L_max for registry-PASS; entries lacking the structure are registry-incomplete and route to plan-freeze halt | S86 W-5 RULE-1+2 (volovik+connes); MANDATORY at K=3 promoted S88 W4a-17 (3 calibration corpus instances: §VII.AF.1 LANDED + §VII.AH STAGE-1-CANDIDATE + §VII.W-3.LAB STAGE-1-CANDIDATE) | `.claude/rules/cross-pillar-bridge-anatomy.md` (MANDATORY); §VII.AF.1 (permanent-results-registry.md:14690); §VII.W-3.LAB (permanent-results-registry.md:16693) | Excludes the methodology-layer region where ad-hoc cross-pillar bridge claims (without explicit HKR/K-theory boundary/Connes-Karoubi pairing citation) can enter the registry; forces the substrate→laboratory direction of explanation |

**Aggregate**: 11 new walls (W11–W21). Combined with the existing W1–W10 atlas baseline, total wall count is **21**. The atlas-00 line-17 estimate of "10 walls" is exceeded by 11 (the post-S52 era added more structural exclusions than the entire pre-S52 history).

#### Notes on wall boundary distinctions

- W11 (Volovik CC Tracking) is currently ALSO listed as Door 12 in atlas-05. The wall framing (it excludes the fine-tuning interpretation) and door framing (Volovik tracking is a permanently-open mechanism) are non-redundant — promoting W11 to wall status preserves Door 12 as the mechanistic anchor while making the structural exclusion explicit.
- W19 (PRU Class 8 sub-class walls) and W20 (Joint-Theorem Single-Axis) and W21 (Cross-Pillar Bridge 5+3) are METHODOLOGY-layer walls. Atlas-05 has been substrate-physics walls only; the post-S86 era introduced rule-file walls that bind plan-freeze admissibility. Decision deferred to orchestrator: keep methodology walls in atlas-05 OR partition them into a new atlas-05B "methodology walls" companion section.

### 2b. Doors closed S52-S88

A "door closing" event = a constraint that became fixed (a pre-registered question's answer landed PERMANENT) OR a structural identity proven that converts an open mechanism into a permanent one. These are not "doors closed" in the wall-sense (excluded regions) but doors-becoming-fixed (mechanism class converted from open to permanently established).

| door-id | what was constrained | closing session | registry / rule cite |
|:--------|:---------------------|:----------------|:---------------------|
| Door-S58 | Volovik partition w_0 = -0.918 derivation; substrate compaction observable established as PRIMARY CC mechanism | S58 final synthesis | `falsifier-watchlist.md` w_0 row; canonical_constants.py:1243 `w0_FW = -0.918`; `permanence-map.md` Pillar II anchor |
| Door-S62 | n_s = 0.9567-0.9595 from Hubble slow-roll (KZ-NS-62 PASS); first viable n_s prediction in 62 sessions; eps_H methodology established (caveats W12 above) | S62 W2-01 (KZ-NS-62) | atlas-05 line 160-165 (Door 8); `falsifier-master-inventory.md` row 1.a |
| Door-S62-Meissner | Meissner Permanence Under GGE (D_s(GGE)/D_s(fold) = 0.9885); DM-SM decoupling permanent; Type-I classification preserved | S62 W2-02 | atlas-05 line 174-179 (Door 10) |
| Door-S62-CFq | CF-9 Algebraic Identity (BERRY-PROJECTION-62 PASS; \|A_coset\|² = 3/2 + (3/2)e^{-4τ} EXACT to 2e-14); Berry/NCG/KK triple identification | S62 W1-02 | atlas-05 line 167-172 (Door 9) |
| Door-S66 | DILUTION-CC-66 PASS at 0.01 OOM (Volovik tracking); 114 OOM gap converted from open problem to expansion-history reading | S66 W1-A + Workshop 4 | atlas-05 line 188-194 (Door 12); `framework-cc-oom.md` |
| Door-S66-Leggett | Leggett-only DM Omega_DM h^2 = 0.120 at 0.6% from Planck; z_eq = 3425 at 0.88σ; 5 channels PASS; LEGGETT-MOMENT closing as Type-F observable per S70 era refinement | S66 (consolidated S58 Volovik + S66 Leggett) | atlas-05 line 196-201 (Door 13) |
| Door-S70 | LEGGETT-MOMENT closing as Type-F (single-summand-projection trace) observable; algebra-INVARIANT classification; mechanically closed under §VII.U.2 4-corner rule | S70 era (cited at `mechanical-closure-discipline.md §"Layer-separability carve-out"` calibration corpus instance #1) | `mechanical-closure-discipline.md §"Layer-separability carve-out"` |
| Door-S86-3HeB | 3He-B inheritance closing (rank-2 cocycle generators of ker(ι_*) characterized; 4-gate falsifier protocol pre-registered: Gate 1 NULL on F1+F2+F5; Gate 2 ratio 7.3250±0.1%; Gate 3 NULL on F3+F4; Gate 4 F4 multi-pressure slope) | S86 W-5 | `.claude/rules/inheritance-falsifier-protocol.md`; §VII.AF.1 (permanent-results-registry.md:14690) |
| Door-S86-JTP | Joint Theorem Promotion Pathway closing as 4-stage MANDATORY structural rule; replaces ad-hoc multi-author cross-citation | S86 W-9 | `.claude/rules/joint-theorem-promotion.md`; calibration corpus §VII.AH |
| Door-S86-CPB | Cross-pillar bridge closing as 5-anatomy + 3-level ladder MANDATORY at K=3; first registered bridge §VII.W (Pillar III ↔ Pillar IV) | S86 W-5 + S88 W4a-17 | `.claude/rules/cross-pillar-bridge-anatomy.md`; §VII.AF.1 + §VII.W-3.LAB |
| Door-S87-S88 | α_s 11.31σ Tension + S50-51 Sign-AND-Magnitude Lock (under C1 identity α_s = n_s² - 1; sign and magnitude are the SAME lock; not separate-stage upgrade pathway); Triple-Protection Reading at CMB pivot (K-homogeneity + GAP-ANTIJENSEN-65 + sub-threshold inter-band coupling) | S86 W-2 (mack+volovik+connes co-signed) | §VII.AB.1–§VII.AB.7 (permanent-results-registry.md:14911-14982) |
| Door-S87-PathC | Joint F_2-Class Path-(c) Theorem (lizzi+transit; 6-clause statement; 4 corrigenda incorporated); SOURCE-DOUBLE-CITE-CO-PRIMARY structure registered; STAGE-1-CANDIDATE per joint-theorem-promotion.md (Stage-2 cross-axis verify queued) | S86 W-9 → S87 W9a-1 LANDED | §VII.AH (permanent-results-registry.md:15522) |
| Door-S88-UniLock | Universal Lock Condition (Substrate Horizon-Trigger Theorem) STAGE-1-CANDIDATE; 3-clause joint theorem unifying J3 BH-horizon-pixelation-lock + S58 fold-effacement Γ_eff=0.99970 + W1b2-64 cascade-tail Page-time non-activation; calibration corpus instance #2 of joint-theorem-promotion.md | S88 W1b2-65 (hawking-theorist primary; orchestrator-direct write) | §VII.AM (permanent-results-registry.md:16367) |
| Door-S88-WedderburnFrobenius | Wedderburn-Artin Frobenius Rescue Class Theorem promoted STAGE-3-PERMANENT; A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) realizes the rescue class | S88 W4a-17 | §VII.W-3.ALGEBRAIC + §VII.W-3.SUBSTRATE (permanent-results-registry.md:16590, 16657) |

**Aggregate**: 14 new doors closed S52–S88. Combined with 13 existing doors in atlas-05, total door count is **27**. The atlas-00 line-17 "10 doors" estimate is now exceeded by 17.

### 2c. Windows opened S52-S88

A window is a constraint currently traversable: a conditional PASS pending one more computation, a live-watch detector horizon, or an open observational gate.

| window-id | conditional-PASS condition | falsifier protocol | detection horizon (years from 2026-05-09) | current σ |
|:----------|:---------------------------|:-------------------|:-------------------------------------------|:----------|
| Window-7 | FUNCTIONAL-SELECT-67: which spectral functional generates n_s? Resolution determines whether n_s = 0.9595 (sqrt(x) cutoff) is canonical OR scheme-dependence persists across regulators (eps_H sign reversal) | S67 carry-forward; bracket FAIL if no functional family yields n_s ∈ [0.9550, 0.9700] | 0 yr (computational; deferred since S67) | n/a (computational gate; not σ-distance) |
| Window-8 | BBN-VOLOVIK-67: can Volovik tracking vacuum reproduce BBN constraints at z ~ 10^9? Door-S66 enabled CC at present epoch but rho_vac/rho_rad = 0.67 at nucleosynthesis is the open question | S67 carry-forward | 0 yr (computational; deferred since S67) | n/a (computational gate) |
| Window-9 | TRANSIT-PS-67: transit power spectrum vs A_s mismatch; α_s prediction adjudication | S67 carry-forward; falsified by absence of consistent dynamical pathway | 0 yr (computational; deferred since S67) | n/a (computational gate) |
| Window-10 | Cross-pillar K=3 Stage-2 verify: §VII.W-3.LAB STAGE-1-CANDIDATE → STAGE-3-PERMANENT promotion via 3-axis cross-reviewer dispatch (volovik transit-side + connes spectral-side + landau condensed-matter-side) WITHOUT prior workshop context | S88+ carry-forward (`S89-W4A-17-W3-LAB-STAGE-2-CROSS-AXIS-VERIFY`) | 0 yr (computational; queued S89) | n/a (computational gate) |
| Window-11 | 3He-B vortex spectroscopy (W11-C5): Caroli-Matricon ladder asymmetry at φ_67-clean; Gate 1 NULL on F1+F2+F5; Gate 2 ratio 7.3250±0.1%; Lancaster MCT-3 / Helsinki ROTA cells | `inheritance-falsifier-protocol.md` 4-gate; FAIL on any non-NULL detection on F1/F2/F5 OR ratio outside 7.3250±0.1% | ~5 yr (MCT-3 horizon 2026–2031 per `falsifier-master-inventory.md` row #13) | not yet observed (lab-falsifier; SI value 58.9589 MHz at SW1) |
| Window-12 | LISA Ω_GW (CGWB): Companion-null prediction Ω_GW = 8.299e-58 (5+ OOM null) at LISA mHz band; (A)/(C) regulator-class discriminator | `falsifier-master-inventory.md` row #7; PASS if h_c observed within (A) band 11 OOM above LISA-PLS; FAIL if (C) null confirmed | ~9 yr (LISA 2035) | n/a (LISA forecast pending; 11 OOM PASS-margin to LISA-PLS sensitivity) |
| Window-13 | LiteBIRD n_T (decisive 4.250σ): Path-H r=0.00745 vs Path-C r=0.0117 internal-consistency split (36.3% Path-C-relative split); LiteBIRD 4.250σ decisive over BK-Array 2026 1.417σ marginal | `falsifier-master-inventory.md` row #2; Path-H/Path-C internal-consistency adjudication | ~4 yr (LiteBIRD 2030) | 4.250σ decisive |
| Window-14 | DESI DR3 w₀-wₐ: framework prediction w_0 = -0.918 (canonical) or -0.842454 (R_842 branch-(iv)) vs LCDM w_0 = -1.0; post-Dovekie 2.130σ for canonical, 0.731σ for branch-(iv) | `falsifier-watchlist.md` w_0 row; null result w_0 = -1.000 ± 0.015 closes Volovik-partition branch at ~5σ | ~1 yr (DESI DR3 2027) | 2.130σ (canonical, post-Dovekie) / 0.731σ (R_842 branch-iv) |
| Window-15 | CMB-S4 α_s (CANONICAL update §W13-5): framework prediction α_s = +0.00117 (S63 RUNNING-NS-63) — diverges from pre-S85 falsifier-watchlist row -0.069 ± 0.008 (PLAN-DRIFT); CMB-S4 σ = 2.1e-3 / CMB-HD σ = 1.1e-3 | `falsifier-watchlist.md` α_s row; CMB-S4 PASS if α_s ∈ [+0.00117 ± 0.002], FAIL if α_s = -0.0045 ± 0.0067 (Planck central) confirmed | ~4 yr (CMB-S4 2030) / ~9 yr (CMB-HD 2035) | +2.70σ (CMB-S4) / +5.15σ (CMB-HD) against LCDM=Planck central -0.0045 |
| Window-16 | CMB-HD α_s: tighter σ on CMB-S4 measurement; same canonical prediction as Window-15 | `falsifier-watchlist.md` α_s row; redundant with Window-15 but instrument-distinct | ~9 yr (CMB-HD 2035) | +5.15σ |
| Window-17 | Hyper-K proton lifetime: framework prediction ~10^36 yr (one-parameter from M_KK); current bound ~10^35 yr at Hyper-K Yr-10 | `falsifier-watchlist.md` proton_lifetime row | ~9 yr (Hyper-K 2030s) | one-sided lower-bound test |
| Window-18 | g_1/g_2 RGE convergence: framework prediction 0.684 at τ=0.19; observed 0.709; 3.5% below — pending RGE running refinement | `falsifier-watchlist.md` g_1/g_2 row | 0 yr (computational; refinement queued) | <observational uncertainty dominates> |
| Window-19 | H_0 spinor-factor resolution: framework prediction 65.4 km/s/Mpc CONTINGENT on spinor-factor resolution; LIVE-PENDING | `falsifier-watchlist.md` H_0 row | 0 yr (computational; structural unresolved through S85) | pending |
| Window-20 | 3He-A NMR sweet-spot (SW1 in lab-falsifier suite): 58.9589 MHz at λ_6 direction; detection_ratio 58958.86 over σ_detect 0.001 MHz; LAB-FALSIFIER-A class | `falsifier-master-inventory.md` row #13 + lab-falsifier suite §13–21; 5-yr decision tree pointer `s86_w11_lab_falsifier_evoi_tree.json:rows[0]` | ~5 yr (2031 per W11-C6 EVOI level ladder) | lab-falsifier (P_decisive 0.30–0.50 at 5-yr 2031 horizon) |
| Window-21 | FeSe NMR sweet-spot (SW2): 364.5177 ppm at λ_7 direction; detection_ratio 72.90 over σ_detect 5.0 ppm | `falsifier-master-inventory.md` row #14 | ~5 yr (2031) | lab-falsifier |
| Window-22 | 173Yb optical-lattice sweet-spot (SW3, UNIQUE λ_8 channel): 1.4250 s^{-1} at λ_8 direction; FAIL-AT-LAB on SW3 is the framework's strongest single-row substrate-direction-falsification trigger | `falsifier-master-inventory.md` row #15 | ~5 yr (2031) | lab-falsifier (single λ_8 measurement) |
| Window-23 | f_NL_folded laboratory-IN observable (CMB / 21-cm bispectrum): 3-pathway GGE-coupling discriminator with pin range [0.0547, 0.7685] (~14× span); SUBSTRATE-IS counterpart at φ_3 ∈ HC^3(A_K) is Window-24 | `falsifier-master-inventory.md` row #9a (LAB-IN) + #9b (SUBSTRATE-IS); CF-28 split | ~9 yr (CMB-S4 σ=6.9 / SKA-1 σ~0.15 in 2035s) | n/a (forecast pending) |
| Window-24 | φ_3 substrate cocycle in HC^3(A_K) (rank-3 Hochschild; 3-pt-connected vertex): substrate-IS structural anchor for laboratory-IN Window-23; HKR-bridge image; analytic-extrapolation 1.0e-6 at L_max=10 | CF-25 STAGE-1-CANDIDATE; Level-3/Level-2 = 1/L = 0.10 universally (LQT rank-inheritance) | 0 yr (substrate-side; computational; STAGE-1-CANDIDATE pending Stage-2 verify) | n/a (computational gate) |

**Aggregate**: 18 new windows opened S52–S88. Combined with the 6 existing windows in atlas-05 (one of which — Window 2 — is permanently CLOSED), total window count is **24**, with **23 currently OPEN** and 1 permanently CLOSED.

#### Note on detection-horizon urgency (Sagan-empiricist flag)

Of the 18 new windows: 8 are computational (0 yr) and either pending S87+ carry-forward closure (Window-7/8/9/10/24) or methodology-resolution-blocked (Window-18/19); 4 are 1–4 yr live-watch (Window-13 LiteBIRD 2030; Window-14 DESI DR3 2027; Window-15 CMB-S4 2030); 6 are 5+ yr (Window-11 MCT-3 2031; Window-12 LISA 2035; Window-16 CMB-HD 2035; Window-17 Hyper-K 2030s; Window-20–22 lab-falsifier 2031; Window-23 SKA-1 2035). The Window-14 DESI DR3 binding event (2027) is the framework's nearest decisive observational test. Per `falsifier-master-inventory.md` row 1.dovekie-2026-update, the R_842 binding event has NOT YET been triggered — DR3 is the binding instrument, not the DES-Dovekie reanalysis on DR2 BAO.

#### Atlas aggregate after uplift (proposed totals)

| Category | atlas-05 baseline | S52–S88 additions | Proposed total | atlas-00 line-17 estimate |
|:---------|:-----------------:|:------------------:|:---------------:|:--------------------------:|
| Walls | 10 | +11 | 21 | 10 (exceeded by 11) |
| Doors | 13 | +14 | 27 | 10 (exceeded by 17) |
| Windows | 6 (5 open + 1 closed) | +18 | 24 (23 open + 1 closed) | 6 (exceeded by 18) |

The atlas-00 line-17 totals were the post-S51 estimate; the S52–S88 era added ~3× the structural-exclusion content the framework had accumulated through its first 51 sessions. This is consistent with the post-S58 paradigm shift (Volovik partition → DILUTION-CC → cross-pillar bridges → joint-theorem-promotion methodology), which substantially expanded the registry's structural reach.

---

## Section 3: Cross-atlas dependencies

### `atlas-02-mechanism-lifecycle.md`

Every wall in §2a corresponds to a closed mechanism class. The wall→closed-mechanism mapping for S52–S88 additions:

- W11 (Volovik CC Tracking) → closes the fine-tuning interpretation; converts pre-existing 25 closed CC mechanisms into a unified "misidentified expansion history" class.
- W12 (Eps_H sign reversal) → closes the single-functional-eps_H mechanism class; partitions n_s mechanisms by regulator class.
- W13 (F_4-MB structural) → closes 4 constituent F_4-MB mechanism FAILs into one wall class (S85-W0-7, S85-W0-11, S85-W0-20, S86-W2-1).
- W14 (Algebra-axis orthogonality) → closes single-axis identity claims; promotes 4-corner classification to MANDATORY.
- W15 (Cross-corner co-primary) → closes cross-corner anchor-conflation mechanism class.
- W16 (Layer-2-non-binding) → closes bare-decomposition envelope-as-bridge-evidence mechanism class.
- W17 (Bare-eigenvalue parity-blindness) → closes η-only HP^1 detection mechanism class.
- W18 (Type-F/Type-S layer-separability) → closes silent-mechanical-closure of state-pair functional class.
- W19 (PRU 8.0–8.6) → closes 7 plan-authorship pathology classes.
- W20 (Joint-theorem single-axis) → closes ad-hoc cross-axis citation mechanism class.
- W21 (Cross-pillar 5+3) → closes ad-hoc cross-pillar bridge mechanism class.

`atlas-02` should add a "S52–S88 wall→mechanism-class closure" cross-table on the same row-pattern as the existing entries.

### `atlas-07-permanent-results.md`

Every S52–S88 wall landed via a §VII slot or rule-file citation; cross-link table:

| Wall | §VII slot or rule cite |
|:-----|:-----------------------|
| W11 | `framework-cc-oom.md`; pre-VII (Volovik partition era; promote to §VII slot in S89+ housekeeping) |
| W12 | §VII.AB.1 (S86 W-2; permanent-results-registry.md:14911) |
| W13 | §VII.Z (S86 1a-S1; permanent-results-registry.md:15210); §VII.V.A (line 16024) |
| W14 | `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3 |
| W15 | `registry-landing.md §"Detection (when SOURCE-DOUBLE-CITE-CO-PRIMARY applies)"` clause 4 |
| W16 | `cross-pillar-bridge-anatomy.md §"Level-2 Layer Distinction"` MANDATORY at K=3 |
| W17 | `regulator-pin-discipline.md §"Class-(c) PIN-DRIFT-FROM-STALE-SOURCE — W-11 Calibration Corpus Extension"`; §VII.W (line 15003) |
| W18 | `mechanical-closure-discipline.md §"Layer-separability carve-out"` SUGGESTION at K=1 |
| W19 | `epistemic-discipline.md §"Pre-Registration Completeness — PRU Class-8 sub-class taxonomy formal extension"`; `pru-class-corpus.md §1-§7` |
| W20 | `joint-theorem-promotion.md`; first calibration §VII.AH (line 15522) |
| W21 | `cross-pillar-bridge-anatomy.md`; §VII.AF.1 (line 14690), §VII.AH, §VII.AM (line 16367), §VII.W-3.LAB (line 16693) |

### `atlas-04-assumptions.md`

Windows correspond to "conditional" assumptions; doors correspond to former assumptions now broken/proven. The S52–S88 mapping:

- **Doors (former assumptions now proven)**: Door-S58 (Volovik partition assumed → derived); Door-S62 (Hubble slow-roll n_s assumed → KZ-NS-62 PASS); Door-S66 (CC fine-tuning assumed → DILUTION-CC-66 PASS at 0.01 OOM closes the assumption); Door-S86-3HeB (rank-2 ker(ι_*) cocycle structure conjectured → 4-gate falsifier protocol pre-registered); Door-S88-WedderburnFrobenius (A_F realization of rescue class assumed → STAGE-3-PERMANENT).
- **Windows (current conditional assumptions)**: Window-7/8/9 (FUNCTIONAL-SELECT, BBN-VOLOVIK, TRANSIT-PS — three CRITICAL S67 assumptions still open as carry-forwards through S87); Window-14 DESI DR3 (assumes Volovik partition; binding event 2027); Window-23/24 (f_NL substrate-IS / lab-IN assumes HKR rank-inheritance; STAGE-1-CANDIDATE pending Stage-2 verify).

`atlas-04` should add: (a) a "former-assumption-now-proven" subsection citing Door-S58/S62/S66/S86-3HeB/S88-WedderburnFrobenius; (b) a "conditional-assumption-pending-window-closure" subsection citing the S67 critical computational gates and the multi-year observational windows.

### `atlas-06-probability-trajectory.md`

Wall landings are inflection points in probability trajectory. Sagan-empiricist scorecard timeline (from MEMORY.md probability tracking through S69):

- S22d 27% → S24a 10% (Venus Moment; Trap 3 wall hardening, atlas-05 W2 precursor) — pre-S52, atlas-05 baseline.
- S35 32% (mechanism chain unconditional, atlas-05 Door 1).
- S40 8–12% (lava deficit). S43redux 12% (scorekeeper-corrected). S44 23% (G_N triple, CDM algebraic).
- S57 22% (BF=4.0, first DM bracket from geometry).
- S61 24% (Higgs 134 GeV, BF=1.50).
- S65 ~24% (n_s, CC permanent — Door-S66 inflection point landed here). S69 22% (neutral; accommodations).

The S52–S88 walls/doors/windows added since the last atlas-05 update introduced multiple inflection points NOT yet reflected in atlas-06:

- **Door-S62 (KZ-NS-62)** → first viable n_s in 62 sessions; positive inflection.
- **Door-S66 (DILUTION-CC-66)** → 114 OOM gap closed; major positive inflection.
- **W12 (eps_H sign reversal)** → SCHEME-DEPENDENT caveat on Door-S62; partial negative inflection.
- **W13 (F_4-MB structural)** → 4-FAIL consolidation into one wall; informational (closes path while strengthening surviving corridors).
- **Door-S86-3HeB / W14 / W21** → cross-pillar bridge methodology landed; structural strengthening (BF≥1 from substrate-derived rank-2 cocycle ratio 7.3250).
- **Door-S87-PathC + Door-S88-UniLock** → joint-theorem-promotion calibration corpus N=2; structural; STAGE-2 verify pending S89+.

`atlas-06` should add an "S52–S88 inflection point timeline" sub-section keyed off the walls/doors/windows enumerated here; the sagan-empiricist probability through S69 (22%, neutral) should be re-evaluated post-S86–S88 wall accumulation.

---

## Substrate-framing audit

Per `.claude/rules/phononic-framing.md §"IS Space, Not IN Space"`, every wall in §2a is stated as a STRUCTURAL EXCLUSION in the substrate's solution space (NOT a laboratory closure). Audit:

- W11 — "excludes the substrate-IS region where CC is treated as a static vacuum-energy" — substrate-IS framing ✓
- W12 — "excludes the substrate-IS region where a single bare eps_H reading can fix n_s" — substrate-IS framing ✓
- W13 — "excludes the substrate-IS Pillar-III multiplier-algebra route" — substrate-IS framing ✓
- W14 — "excludes the substrate-IS region where a substrate observable can be cited in single-axis form" — substrate-IS framing ✓
- W15 — "excludes the substrate-IS region where one CO-PRIMARY chain spans two structurally orthogonal cells" — substrate-IS framing ✓
- W16 — "excludes the substrate-IS region where a `L^{-α}` algebraic envelope on a substrate-internal Tr(D_K^{-2s}) can pose as cross-pillar bridge evidence" — substrate-IS framing ✓
- W17 — "excludes the substrate-IS region where η-detection alone discriminates parity-twin pairs" — substrate-IS framing ✓
- W18 — "excludes the substrate-IS region where state-pair functionals can be silently mechanically closed" — substrate-IS framing ✓
- W19, W20, W21 — methodology-layer walls; substrate-framing N/A (methodology layer is DOWNSTREAM image of the substrate-IS region under the layer-functor F per `epistemic-discipline.md §"Layer-Decomposition"`)

Methodology walls (W19/W20/W21) are NOT substrate-framing violations — they live at the methodology layer of F by construction; their substrate-physics counterparts (the substrate observables they protect) are the §VII slots cited in §2a (e.g., W21 protects §VII.AF.1, §VII.AH, §VII.AM, §VII.W-3.LAB).

---

## Compiler notes for orchestrator

1. **Promotion gap candidates** (walls without §VII slots; route to housekeeping):
   - W11 (Volovik CC Tracking) — currently anchored at `framework-cc-oom.md`; promote to §VII slot in S89+ housekeeping. Suggested slot allocation: §VII.AT (next free letter post-§VII.AS Geometric-Resummation Closure at S88 W18 W6a-51).
   - The other 10 new walls have rule-file citations + corresponding §VII slots.

2. **Window-detection-horizon flags** (route to falsifier-watchlist update):
   - Window-7/8/9 (S67 carry-forwards) — 0 yr / no detection horizon; computational; the carry-forwards have been deferred since S67 (~22 sessions). Recommend orchestrator flag for S89 plan W0 priority audit per `feedback_fix-in-session-never-defer.md`.
   - Window-14 DESI DR3 — 1 yr horizon (2027); R_842 binding event NOT triggered per `falsifier-master-inventory.md` row 1.dovekie-2026-update — the binding instrument is DESI DR3 itself (not DES-Dovekie). Watch closely.
   - Window-18/19 (g_1/g_2, H_0) — both LIVE-PENDING / structural unresolved through S85; route to S89+ structural resolution queue.
   - Window-15 CMB-S4 α_s — PLAN-DRIFT flagged: pre-S85 falsifier-watchlist row cited α_s = -0.069 ± 0.008; post-§W13-5 canon update is +0.00117 (S63 RUNNING-NS-63). The plan-drift is documented in `falsifier-watchlist.md` α_s row but the S52–S88 atlas uplift should record the canon-shift as a pre-2026-04 atlas-05 informational gap.

3. **Methodology-vs-substrate-physics partition** (orchestrator decision):
   - W19/W20/W21 are methodology-layer walls. atlas-05 has historically been substrate-physics walls only. Decision: (a) keep all walls in atlas-05 with explicit "(methodology layer)" tag, or (b) split into atlas-05B "methodology walls" companion section. Recommend (a) for cohesion; the layer-functor F linking methodology ↔ substrate makes a clean split unnecessary.

4. **Atlas-00 line-17 estimate revision** (proposed): atlas-00 currently states "10 walls, 10 doors, 6 windows". Post-uplift totals are 21 walls, 27 doors, 24 windows. Recommend atlas-00 update to reflect the post-S88 totals as part of the same orchestrator dispatch.

---

## Report-format summary

(1) **Packet path**: `C:\sandbox\Ainulindale Exflation\sessions\archive\session-88\atlas-uplift-materials\atlas-05-walls-doors-windows-materials.md`

(2) **Counts** (S52–S88 additions; baseline + new):
- Walls: 10 baseline + 11 new = **21 total**
- Doors: 13 baseline + 14 new = **27 total**
- Windows: 6 baseline + 18 new = **24 total** (23 OPEN, 1 permanently CLOSED — Window 2 from atlas-05)

(3) **Promotion-gap walls** (no §VII slot or rule citation; route to orchestrator triage):
- W11 (Volovik CC Tracking, S66 DILUTION-CC-66) — currently anchored only at `framework-cc-oom.md` (Door 12 in atlas-05) and falsifier-watchlist; lacks dedicated §VII slot. Recommend §VII.AT allocation.

(4) **Detection-horizon flags** (route to falsifier-watchlist update):
- Window-7/8/9 (FUNCTIONAL-SELECT-67, BBN-VOLOVIK-67, TRANSIT-PS-67) — 0 yr horizon; computational; deferred since S67 (~22 sessions); recommend S89 W0 priority audit per `feedback_fix-in-session-never-defer.md`.
- Window-15 CMB-S4 α_s — PLAN-DRIFT documented in falsifier-watchlist (pre-S85: -0.069 ± 0.008; post-§W13-5: +0.00117); atlas-05 currently does not contain the canon shift. Recommend atlas-05 explicit note + falsifier-watchlist alignment audit.
- Window-14 DESI DR3 — R_842 binding event NOT triggered (DR3 = binding instrument, not DR2/Dovekie); 1 yr horizon (2027); recommend explicit "binding-event-pending" tag in atlas-05 entry.
- Window-18 g_1/g_2 + Window-19 H_0 — structural-unresolved-through-S85 LIVE-PENDING; recommend S89+ structural resolution queue.
