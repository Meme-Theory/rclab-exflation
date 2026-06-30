# Session 96 Synthesis: D5 Seesaw-vs-Direct Reading-Divergence — M_R-Internal Settles the Mass Axis, Not the Yukawa Axis

**Date**: 2026-05-30
**Agent**: neutrino-detection-specialist (Neutrino-Detection-Specialist)
**Slot**: Workshop campaign S-1 (Slot-1 review)
**Source Documents**:
- `sessions/archive/session-96/session-96-w4-workingpaper.md` (§W4-6 R-HIERARCHY, §W4-7 SEESAW-D5, Wave-4 synthesis)
- `computations/session-96/s96_gate_verdicts.txt` (lines 72–89; S96-MATTER-SEESAW-D5 INFO line 86, audit_sha256 `e58ecfba0895d798…`)
- `sessions/archive/session-96/session-96-w8-workingpaper.md §"(a) Claim-level reconciliation table"` row #6 (D5 UNRECONCILED Q1-YES → §7.3 → W4 D5)
- `.claude/agent-memory/neutrino-detection-specialist/MEMORY.md`

---

## I. Session Outcome

The D5 dissonance — S60's seesaw light-neutrino spectrum (which uses a right-handed Majorana scale M_R) vs the capstone §0 "no seesaw" claim — is adjudicated here against the W4 gate results. **The structural verdict splits the §0 claim onto two orthogonal axes.** On the **mass-scale axis**, reading (A) is SETTLED: the RH Majorana masses M_R = {1.004, 1.079, 1.170} M_KK ARE D_K eigenvalues (S96-MATTER-SEESAW-D5 PART 1: 2/3 strict-1% PASS, all three < 2% against the L_max=12 cache at τ=0.19), so the seesaw imports **no external mass parameter** and §0's reworded "no external seesaw parameter" is final for the mass axis. On the **Yukawa axis**, neither reading is settled: the R_seesaw=31.57 vs R_direct=9.86 divergence (reldiff 2.2016, the INFO verdict value) is carried **entirely by the Yukawa ratio Y_3/Y_2** (S60: Y_2=4.793566, Y_3 implied), which the framework does not yet derive from D_K. **Reading (B) is therefore the live one**: until the CF-S97-W4-YUKAWA-FAMILY gate derives that ratio, the seesaw retains an irreducible residual Yukawa freedom, and §0 must carry a scoped pointer ("no external *mass* parameter; Yukawa structure OPEN"), not an unqualified "no external seesaw parameter." This is a constraint on §0's scoping corridor, not a recomputation of either gate's permanent verdict.

---

## II. Key Results

### II.1 The D5 divergence is dimensionally localized to the Yukawa ratio Y_3/Y_2 — NOT to the D_K spectrum

**Result**: `R_seesaw / R_direct` divergence factor = `2.2016` (the INFO verdict value, Sage QQ-exact `|R_seesaw − R_direct|/R_direct` from `594428775/18826921`); the entire divergence is carried by `(Y_3/Y_2)²`. **PARTICLE.**

The two R-routes read the same D_K spectrum through different maps. Write the seesaw light masses with units explicit (all from `s60_lepto_cp_log.txt`, verified in W4-7 CC1):

```
m_i = Y_i² v² / (2 M_i)        [seesaw, dimension: GeV²·GeV⁰ / GeV = GeV; CHECK]
  Y_i  dimensionless;  v = 246 GeV;  M_i = (D_K B-branch fold eigenvalue) × M_KK
```

Then, with m_1 = 0 (normal ordering):

```
R_seesaw = m_3²/m_2² − 1
         = [ (Y_3²/(2M_3)) / (Y_2²/(2M_2)) ]² − 1
         = (Y_3/Y_2)⁴ · (M_2/M_3)² − 1                            [substituted form]
```

The `(M_2/M_3)²` factor is **fixed by the D_K spectrum** (M_2, M_3 are eigenvalues, PART-1 INTERNAL). The `(Y_3/Y_2)⁴` factor is **free** — it is the back-solved Yukawa ratio S60 chose so the light spectrum matches a NuFit-like hierarchy. The direct route carries NO Yukawa:

```
R_direct = (E_3² − E_2²) / (E_2² − E_1²) = 9.86183     [bare D_K bottom triple, zero Yukawa]
```

So the 2.20× gap is **not** a disagreement about D_K — both routes agree on the spectrum. It is a measure of how far the back-solved Y_3/Y_2 pulls the light spectrum away from the bare-spacing light spectrum. **The divergence IS the residual Yukawa freedom, made numerical.** This is the load-bearing observation for the (A)-vs-(B) adjudication: the question "does a D_K-derived Yukawa block reconcile the routes?" reduces exactly to "does the framework predict Y_3/Y_2?"

### II.2 M_R-INTERNAL settles the mass axis (reading A on the mass sub-question)

**Result**: 2/3 M_i strict-1% PASS, all three < 2% against the L_max=12 cache (M_1: 1.773e-2; M_2: 1.343e-4; M_3: 4.983e-3). **PARTICLE.** `part1_internal_2pct = True`.

The S60 RH Majorana triple {M_1=1.004396, M_2=1.078573, M_3=1.170003} M_KK is the B-branch fold spectrum of D_K(τ) read along the S52 MSW-transit trajectory at the fold (τ_fold_ed = 0.193878). The single near-miss — M_1 at 1.773% — is the steepest-moving B1 branch's residual from the τ=0.19 ↔ 0.193878 fold offset, an internal trajectory artifact, NOT an external parameter. This is decisive and one-directional: a seesaw whose heavy scale is a spectral object of the operator it is meant to extend imports no mass scale from outside the operator. The mass-axis content of §0 — "the RH Majorana scale is not a free input" — is correct, final, and registry-grounded (M_R is the D_K B-branch fold spectrum; "Leptogenesis (real M_R)" CLOSED, S60).

### II.3 The Yukawa axis is OPEN — reading B is the live reading on the Yukawa sub-question

**Result**: the framework supplies M_R (spectral) but NOT Y_i (S60 Y_2=4.793566 is back-solved, not derived). **PARTICLE.**

The seesaw round-trip `m_2 = Y_2²v²/(2M_2) = 0.008678 eV` (`s60_lepto_cp_log.txt`) is an *input-matched* identity: Y_2 was set to `sqrt(2·m_2·M_2)/v = 4.793566` so that the light mass reproduces a chosen value, not derived from D_K. The W4-1 gate (S96-MATTER-A4-YUKAWA-RATIO, INFO) established that the bare a₄ Yukawa block IS non-empty (`R_Yuk = 1.588`, 11 distinct mass-bilinears, spread 0.49 ≫ 1e-12) — so a D_K-internal Yukawa structure EXISTS — but its zero-free-parameter ratio is OOM-only (`|log10(R_Yuk/(m_τ/m_μ))| = 1.025`, just outside the ≤1.0 band) and does NOT yet pin Y_3/Y_2. Therefore: the object that would close reading B (a parameter-free Y_3/Y_2 from D_K) is **demonstrated to exist structurally but not yet extracted numerically.** Reading B ("residual Yukawa freedom is irreducible") is not refuted; it is UNTESTED pending CF-S97. Until tested, §0 cannot claim the Yukawa freedom is reducible.

### II.4 δ_CP ∈ {0, π} EXACT — the falsifiable structural sub-result, independent of the R-route divergence

**Result**: `δ_CP ∈ {0, π}` EXACT; `ε₁ = 0` EXACT; `η_B^internal = 0` EXACT. **PARTICLE.** Self-contained (T11 / "Leptogenesis (real M_R)" CLOSED).

This is the one part of D5 that is parameter-free AND falsifiable regardless of how the Yukawa axis resolves. The chain is clean: `[J, D_K] = 0` at all τ (T11, PROVEN S43; 79,968 pairs, max dev 3.29e-13) ⇒ the natural-basis M_R is real symmetric (`M_R = O·diag(M_i)·Oᵀ`, O real orthogonal) ⇒ no complex phase enters leptonic mixing ⇒ **δ_CP ∈ {0, π} EXACTLY**. The detector mapping is sharp: NuFit-6.0 best fit δ_CP ≈ 177° ≈ π, with CP-conserving values inside the band — *consistent* with the framework's {0,π} forcing. DUNE and Hyper-K target δ_CP at ~10–20° precision; **a high-significance exclusion of both {0, π} would falsify the real-M_R / [J,D_K]=0 structure.** This is a genuine non-detection-constrains-as-detection axis: confirmation that δ_CP sits at {0,π} adds nothing the framework didn't predict, while exclusion kills it. Note the divergence with my working-memory NuFit anchor (δ_CP ≈ 230°): the W4-3/W4-7 gates use δ_CP ≈ 177° ≈ π as the NuFit-6.0 (Sept 2024) value; the framework's {0,π} prediction is consistent with the π-proximate fit either way, but the exact NuFit central value is library-gap-dependent and should be verified against a current NuFit-6.0 pin before any σ-distance is published.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| S96-MATTER-SEESAW-D5 (W4-7) | INFO | reldiff `2.2016`; M_R 2/3 strict-1% PASS, all <2%; δ_CP∈{0,π} EXACT |
| S96-MATTER-R-HIERARCHY (W4-6) | FAIL | `R_direct = 9.86183` (bare D_K spacing; ∉[17,66]; F=0.027≤1 moves R wrong way) |
| S96-MATTER-A4-YUKAWA-RATIO (W4-1) | INFO | `R_Yuk = 1.588` (non-empty a₄ block, OOM-only) |

(Source-doc gate verdicts are authoritative and are NOT re-adjudicated here. This synthesis adjudicates the *structural reading* of the D5 INFO, per the W8-1 row #6 Q1-YES forward-route — the verdict numbers stand.)

---

## IV. Structural Implications

### IV.1 The structural verdict on (A) vs (B): the §0 claim decomposes; (A) holds on the mass axis, (B) is live on the Yukawa axis

The two readings as posed in the task are NOT mutually exclusive alternatives — they live on **orthogonal axes** of the seesaw, and the existing W4 results decide them separately:

- **(A) "parameter-free D_K-derived Yukawa block CAN reconcile ⇒ residual Yukawa freedom REDUCIBLE ⇒ §0 'no external seesaw parameter' is FINAL."** — SETTLED ONLY on the mass axis. M_R-INTERNAL (II.2) makes the *mass* scale non-external; that much of (A) is final and registry-grounded. But the *Yukawa-reducibility* clause of (A) is **NOT established by any current result** — the W4-1 non-empty a₄ block (II.3) shows the machinery exists, but no gate has shown it lands Y_3/Y_2 such that the routes coincide.
- **(B) "residual Yukawa freedom is IRREDUCIBLE ⇒ §0 must scope to 'no external MASS parameter; Yukawa structure OPEN.'"** — This is the **structurally accurate current state**. The 2.2016 divergence (II.1) is a numerical witness that Y_3/Y_2 is, AT PRESENT, free. (B)'s scoping is the honest §0 wording until CF-S97 resolves the Yukawa axis.

**Verdict: M_R-INTERNAL + the dimensional localization of the divergence (II.1) SETTLE the mass sub-question (A holds there) but FORCE the further scope on the Yukawa sub-question (B holds there).** The two readings are not a binary to be won by one side; they partition. §0 at "no external seesaw parameter" is over-broad *as a single claim* because it lets a reader infer the Yukawa axis is also closed — which it is not. The precise §0 state is: **mass scale internal (settled); Yukawa structure open (pending CF-S97).**

This is NOT a re-adjudication of the INFO verdict — the INFO stands. It is the resolution of the W8-1 row #6 Q1-YES adjudication that the §7.3 capstone pointer routes to the W4 D5 investigator (this report).

### IV.2 Solution-space boundary — which §0-scoping corridor each reading closes

- **Reading (A) closes the corridor**: "§0 may assert the *entire* seesaw (mass + coupling) is parameter-free." Adopting (A) as final would be the over-claim — it forecloses the Yukawa-open corridor that the 2.20 divergence empirically holds OPEN. **(A)-as-final is the corridor that the data CLOSES**: the divergence falsifies "Yukawa freedom already reducible."
- **Reading (B) closes the corridor**: "the seesaw mass scale is an external add-on." M_R-INTERNAL (2/3 strict-1% PASS) falsifies that. (B) correctly retains the mass-internal result while keeping the Yukawa corridor open. **(B) is the surviving scoping**: it closes the "external mass parameter" corridor (via M_R-INTERNAL) without prematurely closing the "Yukawa derived" corridor.

Net: the surviving §0 scoping region is the **intersection** — mass-internal (from A's mass clause, = B's retained result) AND Yukawa-open (from B). The divergence at 2.2016 is the boundary marker: it is `> 0.10` (the would-be reconciliation threshold), so it sits strictly inside the "Yukawa-open" region and strictly outside the "Yukawa-reconciled" region.

### IV.3 Cross-wave consistency — D5 does not conflict with any W4 result; it consolidates four into one frontier

The D5 Yukawa-open verdict is mutually consistent with — indeed, IS the same object as — the frontier-#7 convergence the Wave-4 synthesis identified: W4-1 (R_Yuk OOM-only), W4-2 (PMNS R unreachable, peak 6.868 vs floor 17), W4-6 (R_direct=9.86 FAIL), and W4-7 (this D5 divergence) are **four views of one missing object: a parameter-free D_K-derived family/Yukawa structure.** No cross-wave contradiction exists; the D5 divergence is the seesaw-axis projection of the single open frontier. This strengthens, not weakens, the constraint map: it localizes four scattered shortfalls to one sharply-specified gate (CF-S97-W4-YUKAWA-FAMILY).

One numerical-consistency note (flagged, not a conflict): R_seesaw ≈ 31.57 sits suspiciously near the NuFit target R ≈ 33.8 (registry S35 R = 32.6 ± 1.4) precisely BECAUSE the S60 light masses were back-solved to a NuFit-like spectrum — this near-coincidence is a property of the back-solve, not an independent framework prediction, and must NOT be cited as a §7 falsifier-anchor "R prediction." The framework's *parameter-free* R is R_direct = 9.86 (FAIL), 3.4× below NuFit. Any capstone §7 row citing R must use the parameter-free value with its FAIL status, never the Yukawa-dressed R_seesaw.

---

## V. Carry-Forward Computations

The compute that settles the (A)-vs-(B) Yukawa axis (CF-S97-W4-YUKAWA-FAMILY) is ALREADY a Wave-4 WP carry-forward — it is NOT duplicated here. This section (1) states the **pre-registered discriminator** that a PASS of that gate must show to CLOSE reading B, and (2) adds one MATH-only follow-up that the dimensional localization in II.1 newly motivates. No hygiene padding.

```
V.1. Pre-registered discriminator for CF-S97-W4-YUKAWA-FAMILY (S97-YUKAWA-FAMILY-DERIVE) — what a PASS must show to CLOSE reading B
   - What: A PASS of S97-YUKAWA-FAMILY-DERIVE closes reading B (and promotes reading A to FINAL on the Yukawa axis) IFF the parameter-free D_K-derived Yukawa block delivers BOTH conjuncts SIMULTANEOUSLY from the SAME extraction (no re-tuning between):
       (i)  an SM-matching fermion mass ratio: |log10(R / R_SM)| < 1
            (R_SM = the targeted SM fermion-mass ratio anchor, e.g. m_τ/m_μ = 16.817 per W4-1);
       (ii) route reconciliation: |R_seesaw − R_direct| / R_direct < 0.10,
            where the D_K-derived Yukawa ratio (Y_3/Y_2)_DK REPLACES the S60 back-solved Y_3/Y_2,
            recomputing R_seesaw = (Y_3/Y_2)_DK⁴·(M_2/M_3)² − 1 and testing it against R_direct = 9.86183.
       Decision map:
         PASS (both conjuncts) ⇒ reading B FALSIFIED (Yukawa freedom REDUCIBLE);
                                 §0 → "no external seesaw parameter" FINAL on BOTH axes.
         FAIL/INFO (either conjunct misses) ⇒ reading B STANDS (Yukawa freedom irreducible at this extraction);
                                 §0 retains "no external MASS parameter; Yukawa structure OPEN."
       Load-bearing sub-check (from II.1): conjunct (ii) is NOT independent of (i) — both are functions of the
       single derived ratio (Y_3/Y_2)_DK. A PASS that lands (i) via one Y-ratio and (ii) via a DIFFERENT Y-ratio
       is a convention-shop, not a reconciliation. The gate MUST verify (i) and (ii) read the SAME (Y_3/Y_2)_DK.
   - Inputs: s96_matter_a4_yukawa_ratio.npz (bare a₄ block, R_Yuk=1.588, 11 mass-bilinears); s96_matter_seesaw_d5.npz
            (R_seesaw=31.57, M_i coincidence, mr_reldiff); s96_matter_r_hierarchy.npz (R_direct=9.86183);
            s60_lepto_cp_log.txt (Y_2=4.793566, M_R triple); canonical_constants: M_KK=7.428660036284456e16, v_ew=246,
            tau_fold=0.19; the inner-fluctuation / Peter-Weyl a₄ machinery.
   - Gate: feeds S97-YUKAWA-FAMILY-DERIVE (the existing CF-S97-W4-YUKAWA-FAMILY gate). This entry pins its
            reading-B-closure discriminator; it does NOT create a new gate.
   - Effort: multi-wave (frontier #7; the framework's hardest open matter-sector problem — multi-session campaign).

V.2. Yukawa-ratio sensitivity decomposition of the D5 divergence (MATH-only, newly motivated by II.1)
   - What: Compute the closed-form sensitivity ∂(R_seesaw)/∂(Y_3/Y_2) and invert for the Y_3/Y_2 value that would
       drive |R_seesaw − R_direct|/R_direct below 0.10. Output: (Y_3/Y_2)_reconcile = the target ratio the
       D_K extraction must hit, and the S60 actual (Y_3/Y_2)_S60 = sqrt(2·m_3·M_3)/(sqrt(2·m_2·M_2))·(v/v),
       so CF-S97 has an explicit numerical TARGET (not just a <0.10 band) for the derived ratio.
       Substitution: from R_seesaw = (Y_3/Y_2)⁴·(M_2/M_3)² − 1, set R_seesaw = R_direct = 9.86183 with M_2/M_3
       fixed from the cache ⇒ (Y_3/Y_2)_reconcile = [(R_direct+1)·(M_3/M_2)²]^(1/4). Dimensionless throughout.
   - Inputs: s96_matter_seesaw_d5.npz (M_2=1.078573, M_3=1.170003 M_KK, R_seesaw=31.57);
       s96_matter_r_hierarchy.npz (R_direct=9.86183); s60_lepto_cp_log.txt (Y_2=4.793566, Y_3 implied via m_3, M_3).
   - Gate: S97-YUKAWA-RATIO-TARGET (new, lightweight). INFO-class (diagnostic, no PASS/FAIL physics threshold):
       emits (Y_3/Y_2)_reconcile and (Y_3/Y_2)_S60 as the explicit numerical target + actual for CF-S97;
       PASS-band N/A (this is a target-provisioning compute, classified INFO per gate-verdicts.md).
   - Effort: 1–2 hours, 1 agent session (closed-form algebra + Sage QQ cross-check; no eigensolve, no scan).
```

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | D5 divergence dimensionally = (Y_3/Y_2)⁴ factor; reldiff 2.2016 | PARTICLE | INFO (verdict stands) | The divergence IS the residual Yukawa freedom; (A)-vs-(B) reduces to "is Y_3/Y_2 D_K-derivable?" |
| 2 | M_R = {1.004,1.079,1.170} M_KK ARE D_K eigenvalues (2/3 strict-1%, all <2%) | PARTICLE | settled | Mass axis: reading A FINAL; "no external mass parameter" registry-grounded |
| 3 | Y_i NOT yet D_K-derived (S60 Y_2=4.79 back-solved; W4-1 a₄ block non-empty but OOM-only) | PARTICLE | OPEN | Yukawa axis: reading B LIVE; §0 must scope "Yukawa structure OPEN" |
| 4 | Structural verdict: §0 claim decomposes; (A) on mass axis, (B) on Yukawa axis | PARTICLE | adjudicated | §0 = "mass internal (settled) + Yukawa open (pending CF-S97)" — NOT a single binary |
| 5 | δ_CP ∈ {0,π} EXACT (real M_R, [J,D_K]=0) | PARTICLE | parameter-free, falsifiable | DUNE/Hyper-K {0,π}-exclusion at high σ falsifies real-M_R structure; non-detection constrains |
| 6 | CF-S97 reading-B-closure discriminator pre-registered | PARTICLE | pending | PASS iff |log10(R/R_SM)|<1 AND |R_seesaw−R_direct|/R_direct<0.10 from the SAME derived (Y_3/Y_2)_DK |
| 7 | §0 capstone wording (RECOMMENDATION to designated-writer / mack §7) | — | recommendation only | See §VII below; this report does NOT edit framework docs |

---

## VII. Recommended §0 Capstone Wording (RECOMMENDATION — routed to designated-writer / mack §7; NOT edited here)

Per the task constraint and `feedback_framework-hygiene.md` / `feedback_mack-bridge-role.md`, the following is a **recommendation** for the §0 prose owner (designated writer) and the mack-cosmic-bridge §7 falsifier surface. This report writes ONLY this synthesis file and edits no framework doc, registry, or capstone.

**Recommended §0 wording** (replacing both "no seesaw" and the interim "no external seesaw parameter"):

> *No external seesaw **mass** parameter: the right-handed Majorana scale is the D_K B-branch fold spectrum (M_R = {1.004, 1.079, 1.170} M_KK, ≥98% spectral coincidence; S96-MATTER-SEESAW-D5 PART 1). The seesaw is an internal level-splitting, not an external mass add-on. The **Yukawa** structure Y_i that dresses M_R into the light spectrum is NOT yet derived from D_K — the seesaw-dressed and bare-spacing mass-squared ratios diverge by 2.2× (R_seesaw=31.57 vs R_direct=9.86), the residual measuring the as-yet-underived family/Yukawa freedom (frontier #7, CF-S97-W4-YUKAWA-FAMILY). STATUS: mass axis settled; Yukawa axis open pending S97-YUKAWA-FAMILY-DERIVE.*

**Rationale for the prose owner**:
- Preserves the substrate-first direction (D_K eigenvalues → M_R → seesaw level-splitting → light spectrum); the substrate IS the M_R scale.
- Does NOT supersede S60 (the seesaw round-trip and the real-M_R leptogenesis-null remain CLOSED/PROVEN).
- Carries the explicit `STATUS: ... open pending <forward gate>` pointer the W8-1 row #6 Q1-YES routing requires (the §7.3 cross-reference must point to the W4 D5 adjudication = this report's verdict + the CF-S97 gate), per `capstone-hygiene-gate.md` Q3 routing and `Investigating-Workshops.md` Q1 (unreconciled tension → forward pointer, NOT silent down-tag).

**§7 falsifier-surface companion (mack-cosmic-bridge, sole writer)**: the `δ_CP ∈ {0,π}` EXACT prediction is a clean §7 falsifier row — DUNE/Hyper-K exclusion of both CP-conserving values at high significance falsifies the real-M_R / [J,D_K]=0 structure. (The m_ββ = 4.96–8.27 meV 0νββ row from W4-3 is the companion next-gen-reach falsifier; both are mack's §7 domain, not edited here.) The parameter-free R for any §7 row is R_direct = 9.86 (FAIL, 3.4× below NuFit ≈ 33.8) — NOT the back-solved R_seesaw = 31.57, whose NuFit-proximity is an artifact of the S60 back-solve and is not an independent framework prediction.
