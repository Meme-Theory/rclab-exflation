# S87 Workshop — Bulletin #3 / Bulletin #4 corridor independence

**Date**: 2026-05-02
**Agent**: connes-ncg-theorist (solo, 1-agent task per `_seed-5.md` Workshop 3 §"Rounds: 2 routine adjudication")
**Source documents** (verified to exist):
1. `sessions/archive/session-87/session-87-results-workingpaper.md` §W10-1 (lines 8439–8597; FAIL on `S87-BULLETIN-#3-RESCUE-RESIDUAL`) and §W10-2 (lines 8601–8654; PASS on `S87-BULLETIN-#4-IRRATIONAL-RHO-PERMANENT-WALL-LANDING`)
2. `sessions/permanent-results-registry.md` §VII.N (lines 6121–6717; the canonical Three-Layer Regulator Theorem — note: the seed file refers to this as "§VII.M" but the Three-Layer Regulator Theorem actually landed at §VII.N due to W2a-11 slot collision; §VII.M is occupied by the DR3-RESPONSE-PROTOCOL family) and §VII.K-PROP.W10-4 (lines 15905–15943; the 4-level registry-mechanic schema)
3. `sessions/archive/session-87/workshops/_seed-5.md` Workshop 3 (lines 60–76; corridor-independence task framing)

## Task definition

Bulletins #3 and #4 both touch the substrate's Mellin-cone, but at different distance poles: Bulletin #3 (W10-1) at substrate-distance-1 (s=3 family with the s_eff = 11/2 candidate), Bulletin #4 (W10-2) at substrate-distance-2 (s=4 pole). The structural question is whether substrate-Mellin-cone irrationality (proven `PERMANENT-WALL` at substrate-distance-2 by W10-2 PASS) is UNIVERSAL across all integer-distance poles s ∈ {2, 3, 4, …} (TWO-FACES-ONE-WALL — making W10-1's FAIL a corollary of W10-2's PASS), or whether the two corridors are INDEPENDENT (substrate-pole-by-substrate-pole rationality classification, with W10-1 and W10-2 evaluated at non-overlapping spectral observables). The verdict re-scopes the S88 carry-forward `S88-CF-A` (`S88-BULLETIN-#3-RESCUE-RESIDUAL-REMEDIATION`) — TWO-FACES-ONE-WALL retracts the W-10 R3-B EMERGENCE E1 entry en bloc; INDEPENDENT-CORRIDORS retains the S52–S77 SOURCE-RECON class-(c) PIN-DRIFT scope.

## Substitution chain through §VII.N composition law

Following the mandate of `.claude/rules/math-scripts.md` §"Double-Check Logic Before Compute": the substitution chain is written in full BEFORE any direction claim is made.

**Step 1 — Definition (substrate-first per `phononic-framing.md` §"IS Space, Not IN Space")**:

Let (A, H, D) be the spectral triple of the framework with A_F = C ⊕ H ⊕ M_3(C), H_F = C^32, D = đ_M ⊗ 1 + γ^5 ⊗ D_F(τ_fold) at τ_fold = 0.190. The substrate IS this spectral triple; "Mellin-cone" is the family of finite-rank spectral observables built from D_K's eigenvalue spectrum {|λ_k|} via:

  (1)  K_substrate(s)  :=  Σ_k |λ_k|^{-s}     (substrate-distance-N pole at s = d − 2N for KO-dim d=6, i.e. s ∈ {6, 4, 2, 0, …} for integer N ∈ {0, 1, 2, 3, …})

By the §VII.N stratification, for FIXED s the regulator axis admits a unique three-layer ordering:
- L1 = ζ-canonical (axiomatic, Connes-Marcolli 2008 Thm 1.31)
- L2 = Zubarev (heat-kernel substrate-action minimum at τ_fold)
- L3 = per-Q span (residual freedom; CC-5 partition-of-unity recovers L1)

Define the regulator-axis ratios at fixed substrate-distance pole s:

  (2)  r_L1L2(s; L) := f_conv_L1(s; L) / f_conv_L2(s; L)
  (3)  r_L2L3(s; L) := f_conv_L2(s; L) / f_conv_L3(s; L)
  (4)  r_L1L3(s; L) := f_conv_L1(s; L) / f_conv_L3(s; L)

The §VII.N composition law (registry §VII.N C1):

  (5)  r_L1L2(s; L) · r_L2L3(s; L)  =  r_L1L3(s; L)         [WITHIN L3 stratum, AT FIXED s]

**Step 2 — Substitution at substrate-distance-1 (W10-1 substrate-physics observables, s in the substrate-distance-1 family s ∈ {3, 11/2 candidate} per W10-1 §"CC2"):**

At L_max = 12, τ_fold = 0.190 (W10-1 reported values):
  r_L1L2(s_d1; L=12) = 6.6691951571
  r_L2L3(s_d1; L=12) = 0.1499431305
  r_L1L3(s_d1; L=12) = 1.0000000000   (CC-5 partition-of-unity, exact by L3 = L1)

Composition-law residual (Python-verified, IEEE 754 float64):
  r_L1L2 · r_L2L3 = 6.6691951571 × 0.1499431305 = 0.99999999977 (residual 2.29×10⁻¹⁰ from float64 cancellation)

**Step 3 — Substitution at substrate-distance-2 (W10-2 substrate-physics observable, s = 4 pole per W10-2 §"Substitution chain" Step 1):**

At L_max ∈ {8, 9, 10, 11, 12} (W10-2 reported series ρ(L=8..12)):
  ρ(L=8)  = -0.504466
  ρ(L=9)  = -0.542440
  ρ(L=10) = -0.577173
  ρ(L=11) = -0.607950
  ρ(L=12) = -0.634885
  ρ_∞    = -0.8103647022669215  (full float64; canonical_constants.py:781 promoted entry `rho_inf_FW`)

ρ_∞ is the L2-Zubarev signed-residue at s=4 in the L_max → ∞ limit. It is a SINGLE-AXIS (L2-only) trace, NOT a regulator-axis ratio.

**Step 4 — Simplification (substrate-distance-pole vs regulator-axis decomposition)**:

The §VII.N composition law (Step 1, eq. 5) is a relation AT FIXED s ACROSS THE THREE REGULATOR AXES (L1, L2, L3). Substituting the W10-1 values:

  6.6691951571 × 0.1499431305 = 1.0000000000       (s_d1 fixed; cycles within L1↔L2↔L3 axes)

This is an INTRA-POLE equation. The composition law does NOT relate values at s = s_d1 to values at s = 4 (the substrate-distance-2 pole where ρ_∞ lives). The §VII.N statement (registry §VII.N L1/L2/L3 derivations) is silent on cross-pole structure: L1 declares ζ unique at each fixed pole; L2 declares Zubarev unique at each fixed pole; L3 enumerates per-Q residual freedom at each fixed pole. The three-layer stratification is by REGULATOR AXIS not by Mellin-distance pole.

Algebraic check: the "machine-exact PASS" is structurally tautological under the W10-1 implementation. r_L1L3 = 1 by CC-5 partition-of-unity (L3 ≡ L1 reconstruction); therefore r_L2L3 = 1/r_L1L2 by definition; therefore r_L1L2 · r_L2L3 = r_L1L2 · (1/r_L1L2) = 1 = r_L1L3 IDENTICALLY. The W10-1 §"Co-sign considerations" (iii) explicitly notes this: "the cascade clean is structurally tautological under the L3-as-CC-5-partition implementation." The composition law's machine-exact PASS at substrate-distance-1 carries ZERO information about ρ_∞ at substrate-distance-2.

**Step 5 — Direction (substrate-pole independence)**:

A counter-example by analogy reinforces the structural reading. For the Riemann zeta function (a generic spectral function), Python-verified:
  ζ(2)  = π²/6 ≈ 1.6449340668     (IRRATIONAL, by Lindemann–Weierstrass)
  ζ(−1) = −1/12                   (RATIONAL, by Bernoulli-number identity)

Cross-pole rationality classification is INDEPENDENT for general spectral functions: the same operator (or same Riemann zeta) can have rational trace values at one s and irrational trace values at another. The substrate's spectral cascade is no different a priori — without an EXPLICIT structural theorem forcing cross-pole inheritance of irrationality (which §VII.N does NOT supply, and which no other registered theorem in `permanent-results-registry.md` supplies), the rationality classification at one substrate-distance pole does NOT determine the classification at any other substrate-distance pole.

A second piece of evidence from the knowledge index: the only "Mellin-cone universal" theorem in the framework is `S85-W6-5-MELLIN-CONE-EXT` PASS at `apex_universal_s3/dev=0.00e+00` — which is explicitly POLE-SPECIFIC TO s=3 (Mellin-cone apex universal at substrate-distance-1 pole). The framework's existing structural identity is "universality at ONE pole", not "universality across poles."

**Direction**: cross-pole INDEPENDENCE is STRUCTURALLY UNFORCED by §VII.N as registered; cross-pole INDEPENDENCE is the default classification under the existing registry; cross-pole inheritance of irrationality from s=4 to s=3 is NOT predicted by §VII.N composition law nor by any sister registry entry.

## Question (a) verdict

**Is the substrate's Mellin-cone irrationality (W10-2 PERMANENT-WALL at substrate-distance-2) UNIVERSAL across all integer-distance poles, or pole-specific to s=4?**

**Verdict (a): POLE-SPECIFIC to s=4 (substrate-distance-2)** — UNIVERSAL classification is structurally UNFORCED.

Derivation:

(i) §VII.N stratifies regulator-AXIS choice (L1=ζ vs L2=Zubarev vs L3=per-Q). It does not stratify substrate-distance poles. Reading §VII.N §L1 lines 6249–6309 verbatim: "the canonical summation measure on the spectrum of |D| is Tr_ω(T) = Res_{s=d} Tr(T |D|^{-s}) (Connes-Marcolli 2008 Thm 1.31)." The d here is KO-dim = 6, corresponding to substrate-distance-N=0 pole at s=6. §L1 supplies UNIQUENESS OF MEASURE at ONE pole (s=6 for d=6); it does not propagate across substrate-distances.

(ii) §VII.N §L3 lines 6389–6461 enumerates the residual per-Q span partition: span_Q ∈ [1.0, 1.5] (R-protected) vs [2.5, ∞) (NOT-R-protected); the gap [1.5, 2.5] is EMPTY at L_max=5 (S83 G58 meta-principle). This partition is PER-OBSERVABLE Q at FIXED REGULATOR AXIS; it implicitly assumes a fixed Mellin-distance pole. Cross-pole identification of partitions is not registered.

(iii) The only registered "Mellin-cone universal" theorem is `S85-W6-5-MELLIN-CONE-EXT` (knowledge MCP returns its verdict line `apex_universal_s3/dev=0.00e+00` PASS). Its scheme tag `Connes_Moscovici_1995` and convention `zeta_regularization` are at substrate-distance-1 pole only (s=3). Universality of the cone-apex value is an INTRA-POLE property, not a cross-pole property.

(iv) The W10-2 §"Substrate framing" line 8622 anchors ρ_∞ to "the substrate's dimension-spectrum residue at s = −1 evaluated via Mellin-cone truncation" — a SINGLE-POLE characterization (the s = −1 signed-residue, equivalently the s=4 multiplicative-pole framing per the dimension-spectrum convention). The PERMANENT-WALL classification is built on the simple-pole fit `ρ(L) = c0 + α/L² + β/L⁴` whose coefficients (α=29.92, β=−662.24) are SPECIFIC to the s=4 pole; the irrationality of c0 = ρ_∞ does not constrain c0' at any other pole.

(v) Counter-example by analogy (verified): Riemann ζ has rational ζ(−1) = −1/12 and irrational ζ(2) = π²/6. Cross-pole rationality classification is INDEPENDENT for generic spectral zeta functions absent a forcing theorem. No such forcing theorem is registered for the framework's K_substrate(s).

Therefore: substrate-Mellin-cone irrationality is POLE-SPECIFIC at s=4 as established. Forward-extension to UNIVERSAL CROSS-POLE WALL would require a NEW structural theorem (e.g., a "transcendence-degree-of-Mellin-residue-monotonicity" theorem applied to the substrate's spectral cascade) that does not currently exist.

## Question (b) verdict

**Under the §VII.N composition law machine-exact PASS at L_max=12, what is the structural relationship between r_L1L2 (substrate-distance-1 regulator-axis ratio) and ρ_∞ (substrate-distance-2 single-axis residue)?**

**Verdict (b): NO STRUCTURAL RELATIONSHIP IS FORCED. r_L1L2 and ρ_∞ are INDEPENDENT** — different substrate-distance poles AND different observable types (ratio across regulator axes vs. single-axis trace).

Derivation:

(i) Type mismatch. r_L1L2 is a RATIO across the L1 and L2 regulator AXES at FIXED substrate-distance. ρ_∞ is a SINGLE-AXIS (L2-Zubarev only) signed-residue at FIXED substrate-distance. The two are objects of different categories: r_L1L2 ∈ {regulator-axis ratios at s_d1}, ρ_∞ ∈ {L2-only traces at s_d2}. The §VII.N composition law (eq. 5) closes within the regulator-axis-ratio family at fixed s; it does not connect an axis-ratio to a single-axis trace at a different s.

(ii) Pole mismatch. r_L1L2 lives at substrate-distance-1 (s ∈ {3, 11/2 candidate per W10-1 §"CC2"}); ρ_∞ lives at substrate-distance-2 (s=4 per W10-2 §"Substitution chain" Step 1). The §VII.N composition law is intra-pole (Step 4 above). No cross-pole identity is asserted.

(iii) Algebraic tautology of the W10-1 PASS. Since r_L1L3 = 1 by CC-5 partition-of-unity (L3 ≡ L1 reconstruction) and r_L2L3 = 1/r_L1L2 follows by definition, the composition law r_L1L2 · r_L2L3 = r_L1L3 reduces to r_L1L2 · (1/r_L1L2) = 1 — an algebraic identity true for any r_L1L2 ≠ 0. The composition-law PASS therefore PLACES NO CONSTRAINT on r_L1L2's specific value, let alone on ρ_∞'s value at a different pole.

(iv) Independence test. If ρ_∞ were structurally LINKED to r_L1L2(s_d1), then irrationality of ρ_∞ would force r_L1L2(s_d1) into an irrational range — and the failure of r_L1L2(L=12) = 6.6692 to match 11/7 ≈ 1.5714 would be a COROLLARY of ρ_∞'s irrationality. But the composition-law structure does NOT supply this link, and the framework registers no other theorem that does. r_L1L2(s_d1) failing to reach 11/7 is a substrate-distance-1 fact about the L1-Zubarev × L2-zeta regulator-pair identification; ρ_∞ at substrate-distance-2 being irrational is a substrate-distance-2 fact about the L2-Zubarev signed-residue limit. The two facts are co-emitted by the same substrate (D_K eigenvalue spectrum) but at non-overlapping spectral observables.

The composition law CONSTRAINT on r_L1L2 reaching a rational target is therefore: NONE forced by §VII.N alone. The W10-1 FAIL is an identification-level fact specific to the substrate-distance-1 spectral content; W10-2's PASS at substrate-distance-2 does not forbid r_L1L2 from reaching 11/7 at any L_max nor force it.

## Question (c) verdict

**Should `S88-CF-A` (`S88-BULLETIN-#3-RESCUE-RESIDUAL-REMEDIATION`) be re-scoped to TWO-FACES-ONE-WALL retraction, or retain its current INDEPENDENT-CORRIDORS S52-S77 SOURCE-RECON class-(c) scope?**

**Verdict (c): RETAIN current S52-S77 chain SOURCE-RECON class-(c) PIN-DRIFT scope (INDEPENDENT-CORRIDORS reading)**.

Derivation:

(i) Verdicts (a) and (b) close the structural justification for retraction. Cross-pole inheritance of irrationality is NOT forced by §VII.N nor by any other registered theorem; therefore the W10-1 FAIL is NOT a structural corollary of the W10-2 PASS. Retracting W-10 R3-B EMERGENCE E1 en bloc on the basis of "rational identification was structurally incompatible from the start" is NOT supported by the registry as it currently stands.

(ii) The W10-1 §"Solution-space interpretation" (line 8581-8585) and §"Negative result as constraint" (line 8596-8597) both characterize the FAIL as identification-level (which scalar = 11/7 under canonical L1-Zubarev × L2-zeta) rather than substrate-Mellin-cone-fundamentally-incompatible. The W10-1 §"Carry-forward for S88" 4-field spec (lines 8589-8594) targets the PASS-B spectral-moment-realization claim (W-10 R3-B EMERGENCE E1) as the candidate STALE-SOURCE pin — examining which S52-S77 chain element drifted between c_sub correction (PASS-B coupling-anchor at s_d1) and the spectral-moment realization (Γ(11/4) ≈ 11/7 at 2.35% proximity claim).

(iii) Even under TWO-FACES-ONE-WALL hypothesis, the audit of S52-S77 chain elements would still be structurally informative (it surfaces convention drift independent of the Bulletin #3/#4 corridor question). Under INDEPENDENT-CORRIDORS reading (verdicts a, b), the audit is NECESSARY rather than merely informative — the FAIL is identification-level, so the surviving substrate-physics question is "which convention pin determined the rational identification", which is exactly what `_l1_l2_pipeline_audit.py` SCAFFOLD `DERIV_CHAIN_SCRIPTS` TODO targets.

(iv) Retraction-without-audit risks losing the PASS-B residual finding's structural content — `c_sub^{corrected}/c_sub_baseline = 11/7` IS a c_sub multiplicative anchor at the COUPLING level (W-10 R2-B) regardless of whether the spectral-moment realization (W-10 R3-B EMERGENCE E1) is structurally compatible. Retracting both simultaneously would discard the PASS-B coupling-anchor result. The SOURCE-RECON class-(c) audit isolates which sub-claim drifted and preserves the PASS-B coupling-anchor.

S88-CF-A scope is RETAINED at the SOURCE-RECON class-(c) PIN-DRIFT-FROM-STALE-SOURCE audit on the W-10 R3-B EMERGENCE E1 spectral-moment-realization claim across the S52-S77 chain. Effort estimate ~1 wave (per W10-1 §"Carry-forward for S88" item 4).

## Question (d) verdict

**§VII.K-PROP.W10-4 4-level registry-mechanic schema — does Level-1 wall (irrationality at L → ∞) extend to a CROSS-DISTANCE wall covering all integer Mellin-cone poles, or remain pole-specific?**

**Verdict (d): REMAIN POLE-SPECIFIC at substrate-distance-2 (s=4). Cross-distance extension is STRUCTURALLY UNFORCED at S87 closure.**

Derivation:

(i) The §VII.K-PROP.W10-4 Level-1 paragraph (registry line 15911 verbatim) reads: "ρ_∞ is structurally IRRATIONAL — Sage-exact rational form is unattainable in the L_max → ∞ limit. The simple-pole fit form ρ(L) = c0 + α/L² + β/L⁴ on the L=8..12 cache (per CM-1995 audit Step 4 line 535-549) yields ρ_∞_full_f64 = -0.8103647022669215 ... ρ_∞ is canonicalized as a PERMANENT substrate-feature, NOT a missing-correction signal." The Level-1 statement is anchored by the simple-pole fit at the substrate-distance-2 (s=4) pole specifically. Coefficients α=29.92, β=−662.24 are SPECIFIC to s=4. Extension to s ∈ {3, 5, …} would require independent simple-pole fits with their own coefficients and their own irrationality demonstrations.

(ii) Level-2 envelope (registry line 15913): the structural form |ρ(L_max) − ρ_∞| ≤ C · L_max^{−α} with α ≥ 2 is the substrate-distance-2 convergence rate. It is NOT pre-registered as a cross-pole envelope. At a different substrate-distance pole the convergence rate could differ (different spectral weight, different α coefficient, different envelope tightness).

(iii) Level-4 OPEN paragraph (registry line 15917) explicitly enumerates four sub-questions all PARAMETRIZED at s=4: "(c) does the L2-IRRATIONAL classification extend to the deep-IR limit Λ_Z → 0+ (where rho_inf_zubarev_deep_ir = -0.918 per S86-W10-CANON-EXTRACT band-estimate); (d) the cross-pillar bridge anatomy — does ρ_∞ map to a laboratory-IN observable on a sister pillar." Sub-question (c) is a deep-IR extension AT THE SAME POLE; sub-question (d) is a cross-pillar map AT THE SAME POLE. Cross-distance generalization (s=4 → s ∈ {3, 5, …}) is NOT among the four open questions, indicating the original W10-2 author scoped Level-1 explicitly to the s=4 pole.

(iv) The cross-distance extension would require a NEW structural theorem — e.g., "the substrate's Mellin-cone admits no rational simple-pole residue at any integer distance pole" or the strictly weaker "the substrate's K_substrate(s) values at integer s ∈ ℕ are mutually transcendental over ℚ." Neither of these is registered. Without such a theorem, Level-1's PERMANENT-WALL classification at s=4 stands as a SINGLE-POLE WALL.

§VII.K-PROP.W10-4 Level-1 description STAYS pole-specific at S87 closure. Cross-distance extension is queued as a CONDITIONAL future carry-forward only IF such a theorem becomes available; absent that, future Bulletin landings at adjacent substrate-distances (e.g., a hypothetical Bulletin #N at substrate-distance-3 / s=2) would land their own Level-1 wall classifications independently.

## STRUCTURAL VERDICT

**Bulletins #3 and #4 are INDEPENDENT CORRIDORS.**

The §VII.N Three-Layer Regulator Theorem composition law is INTRA-POLE — it stratifies the regulator-axis choice (L1 ζ-canonical vs L2 Zubarev vs L3 per-Q span) at FIXED substrate-distance pole s, and supplies no cross-pole identity. The W10-1 composition-law machine-exact PASS at substrate-distance-1 is, in fact, algebraically tautological under the W10-1 implementation (L3 ≡ L1 by CC-5 partition-of-unity ⇒ r_L2L3 = 1/r_L1L2 ⇒ product = 1 = r_L1L3 identically, for any non-zero r_L1L2); the PASS therefore places ZERO constraint on r_L1L2's specific value or on ρ_∞ at a different pole.

Cross-pole inheritance of irrationality is NOT forced by any registered theorem. The framework's only registered "Mellin-cone universal" entry (S85-W6-5-MELLIN-CONE-EXT, knowledge MCP verdict `apex_universal_s3/dev=0.00e+00`) is explicitly POLE-SPECIFIC at s=3, not cross-distance. Riemann zeta supplies the canonical counter-example (rational ζ(−1) coexisting with irrational ζ(2)): cross-pole rationality classification is INDEPENDENT for generic spectral functions absent a forcing theorem.

W10-1's FAIL at substrate-distance-1 (r_L1L2(L=12) = 6.6692 vs 11/7 anchor; deviation 324%) is therefore an identification-level fact about which scalars the canonical L1-Zubarev × L2-zeta regulator pair realizes at substrate-distance-1; it is NOT a corollary of W10-2's PERMANENT-WALL at substrate-distance-2. The two corridors carry independent solution-space implications:

- W10-1 corridor closed: the c_sub-PASS-B rational identification `r_L1L2 ≡ 11/7` does NOT realize through the canonical L1-Zubarev × L2-zeta regulator pair at substrate-distance-1. Future r_L1L2 ≡ 11/7 narratives at substrate-distance-1 must specify a NON-canonical regulator pair AND reconcile against §VII.N composition law.
- W10-2 corridor registered: ρ_∞ at substrate-distance-2 is a PERMANENT-WALL substrate constant at full float64 −0.8103647022669215. Level-1 classification stays pole-specific.

The wave-synthesis decomposition of W10's "What Changed" into separate (a) numerical revisions and (b) structural changes bullets is structurally CORRECT under this verdict — Bulletins #3 and #4 are independent corridor states, not dual faces of one wall.

## Solution-space implication

Under INDEPENDENT-CORRIDORS verdict:

(i) `S88-CF-A` (`S88-BULLETIN-#3-RESCUE-RESIDUAL-REMEDIATION`) RETAINS its current SOURCE-RECON class-(c) PIN-DRIFT-FROM-STALE-SOURCE scope across the S52-S77 chain. The audit targets the W-10 R3-B EMERGENCE E1 spectral-moment-realization claim (`Γ(11/4) ≈ 11/7 at 2.35%` proximity elevated to structural identity candidate). PASS predicate per `.claude/rules/epistemic-discipline.md` 4-band SOURCE-RECON taxonomy; FAIL branch retracts the W-10 R3-B EMERGENCE E1 entry from `elimination-bulletins.md` per W10-1 §"Carry-forward for S88" item 3.

(ii) `S88-CF-B` (`S88-BULLETIN-#3-LIZZI-OBSERVABLE-PROMOTION-RE-EMIT`) remains CONDITIONAL on `S88-CF-A` ∈ {PASS, INFO} per `_seed-5.md` line 84 dependency.

(iii) §VII.K-PROP.W10-4 Level-1 description stays POLE-SPECIFIC at substrate-distance-2 (s=4). NO new permanent-results-registry sub-row §VII.K-PROP.MELLIN-CONE-IRRATIONALITY-UNIVERSAL is queued for S88; the cross-distance generalization theorem is NOT structurally supported at S87 closure and is NOT promoted to STAGE-1-CANDIDATE per `joint-theorem-promotion.md`.

(iv) Methodological pin (forward-looking): future Bulletin landings at adjacent substrate-distances (e.g., hypothetical Bulletin #N at substrate-distance-3 / s=2) DO NOT collapse into preceding Bulletins by default. Each Bulletin landing is evaluated at its own substrate-distance pole, with its own Level-1 wall classification, its own Level-2 envelope, and its own Level-3 corridor. Cross-distance generalization across Bulletins is admitted ONLY by an explicit cross-pole structural theorem (none currently registered). This pin extends the §VII.K-PROP.W10-4 4-level schema's per-pole organization across all future Mellin-cone Bulletin landings.

(v) The §VII.N Three-Layer Regulator Theorem composition-law cycle (eq. 5 above) carries forward as the canonical INTRA-POLE structural identity. Future cross-pole identifications (if any) require a DIFFERENT theorem — §VII.N is silent on cross-pole structure and does not need to be amended.

## 4-field carry-forward (forward-looking S88+ items)

### Carry-forward CF-VERDICT-1 (methodological pin)

1. **What**: Pin the per-Bulletin-per-pole Level-1 wall classification convention into `.claude/rules/registry-landing.md` or a sister rule file as the canonical pattern for future Mellin-cone Bulletin landings — each Bulletin's PERMANENT-WALL classification is anchored at its specific substrate-distance pole and is NOT extended cross-distance unless a forcing theorem is registered.
2. **Inputs**: this workshop verdict file (`s87-bulletin-3-4-corridor.md`); §VII.K-PROP.W10-4 entry text (registry lines 15905–15943); §VII.N statement (registry lines 6121–6717); `S85-W6-5-MELLIN-CONE-EXT` apex-universal-at-s=3 verdict from `computations/s85_gate_verdicts.txt`.
3. **Gate**: PASS iff the methodological pin lands in a forward-looking rule file with audit cross-link to the W10-2 §VII.K-PROP.W10-4 4-level schema; auditable at plan-freeze for any S88+ Bulletin-landing gate.
4. **Effort**: ~quarter-wave (rule-file edit + cross-link audit; classify as METHODOLOGY-class per `.claude/rules/wave-classification.md` M1-M4 conjunction; allowlist append required).

### Carry-forward CF-VERDICT-2 (conditional cross-distance theorem dispatch)

1. **What**: IF S88+ surfaces a Bulletin at a different substrate-distance pole (e.g., a hypothetical s=2 pole landing) AND the Bulletin lands a Level-1 PERMANENT-WALL irrationality classification, dispatch a meta-workshop to test whether substrate-Mellin-cone irrationality CAN be promoted to a cross-pole structural theorem at that point. Pre-registered scope: substrate's K_substrate(s) Mellin transform values at integer s ∈ ℕ are mutually transcendental over ℚ (or a strictly weaker compound predicate).
2. **Inputs**: the new Bulletin's data file + verdict line; `rho_inf_FW = -0.8103647022669215` (s=4 pole) from canonical_constants.py:781; the §S85-W6-5-MELLIN-CONE-EXT s=3 apex-universal anchor; any future registered theorems on substrate-spectral-zeta transcendence.
3. **Gate**: STAGE-1-CANDIDATE per `.claude/rules/joint-theorem-promotion.md` IF and ONLY IF a cross-axis (Connes algebraic-axiomatic + lizzi-spectral-functional + transit-dynamics) joint workshop converges on the cross-pole forcing predicate at R3 verdict-freeze; STAGE-2 cross-axis independent verify queued for the session after.
4. **Effort**: undefined at S87 closure — this carry-forward is CONDITIONAL on a new Bulletin landing at a different substrate-distance, not yet scheduled. Absent that trigger, this CF stays dormant.

---

**Status**: STRUCTURAL VERDICT delivered as INDEPENDENT-CORRIDORS. S88-CF-A scope unchanged. §VII.K-PROP.W10-4 Level-1 description stays pole-specific. Forward-looking pole-by-pole evaluation discipline pinned for S88+ Bulletin landings.
