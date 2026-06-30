# Seed file — sessions/archive/session-86/session-86-w6-workingpaper.md

**Date**: 2026-04-26
**Investigator**: phonon-first-cosmologist
**Source WP**: `sessions/archive/session-86/session-86-w6-workingpaper.md` (551 lines)

## Candidates

### Candidate 1 — Mellin-cone projector as dual-discharge for §VII.S.B + §VII.S.D

**What it would do**: Test whether the STRONG-form Mellin-cone projector regulator class — which annihilates the smooth-cutoff `Σ_n x_n · f'(x_n)` tree-level term by conformal-projection identity — simultaneously (a) restores σ²-scaling for C-γ-WEAK at L_max=10 (current LHS/σ rel-var 1.69% vs LHS/σ² rel-var 52.21%) and (b) recovers slot-saturated p_k(Symanzik) ≈ 4 for C-α-LATTICE (current empirical p_k = [6.052, 8.517, 7.863, 8.266] all > 5.5 FAIL boundary). Both empirical FAILs in W6 share a common smooth-cutoff regulator-class diagnosis per the W6 synthesis §3 substitution chain. The workshop adjudicates whether ONE piece of W2 machinery actually does discharge BOTH refinements, or whether the two FAILs decouple under projector-class change.

**Why it's worthwhile**: The W6 synthesis §3 substitution chain explicitly identifies the Mellin-cone projector as the leading refinement candidate for `S86-LATTICE-SPACING-IMMUNIZATION-CANDIDATE` AND `S86-WEYL-RESCALING-IMMUNIZATION-WEAK-FORM` simultaneously (Step 4 direction (a)). W6-3 carry-forward #1 specifies the C-γ-STRONG-FORM lift (s73a / s78 W2-F precedent for the integration kernel). W6-2 carry-forward calls for perturbation-operator refinement but does not connect it to the Mellin-cone route. Whether the SAME projector clears both is a non-trivial cross-corollary claim — if it does, S87 gets a single piece of machinery for two §VII.S.* corollaries; if it doesn't, the smooth-cutoff diagnosis isn't actually common, and W6 §3 Step 3 ("contribution structure does not match the corollary's expected leading-term structure") needs decomposition. This is the highest-leverage workshop outcome from W6.

**Type**: 2-agent workshop

**Suggested agents**: lizzi-spectral-functional-theorist, connes-ncg-theorist

**Rounds (workshops only)**: 2 (lizzi authors the C-γ-STRONG ↔ C-α-LATTICE projector-lift derivation in R1 with explicit annihilation argument; connes responds in R2 with NCG-side check that the projector lives in the regulator-restricted observable algebra `Tr f(D_K²/Λ²)` and doesn't violate spectral-action axioms — both rounds end with a falsifiable single-projector dual-discharge prediction)

**Context the workshop will need**:
- W6-3 verdict line: `S86-WEYL-RESCALING-IMMUNIZATION-WEAK-FORM: FAIL value=3.621380e+07` (max r over Λ_cut ∈ [M_KK, 10·M_KK] sweep; 6-7 OOM gap)
- W6-3 CC2 σ-scaling diagnostic table: LHS/σ rel-var 1.69%, LHS/σ² rel-var 52.21% (linear dominates over quadratic at smooth-cutoff regulator)
- W6-2 verdict line (run-2 canonical): `S86-LATTICE-SPACING-IMMUNIZATION-CANDIDATE: FAIL value=6.052263` with Symanzik p_k = [6.052, 8.517, 7.863, 8.266] vs PASS-band [3.5, 4.5]
- W6 synthesis §3 Step 4 substitution chain: smooth-cutoff regulator's tree-level Σ_n x_n·f'(x_n) Weyl-shift dominates AC-2010 chiral-anomaly by 6-7 OOM at actual D_K eigenvalue density (mean λ ≈ 3.23, max ≈ 4.67 in M_KK units)
- Mellin-cone projector machinery precedent: s73a, s78 W2-F (cited in W6-3 carry-forward #1)
- AC-2010 §V Eq. (5.3) for b_DK = 0.006241291006 (now canonical, registered in canonical_constants.py L422)
- Regulator-restricted observable algebra: spectral triple `(A, H, D_K)` with `A_F = C ⊕ H ⊕ M_3(C)` and L_max=10 D_K spectrum (78,080 eigenvalues across 65 SU(3) sectors)
- Adjudication rule: workshop produces one of three outcomes — (i) single Mellin-cone projector discharges both (predict p_k ≈ 4 AND r ≤ 1 under projector regulator at same L_max=10); (ii) projector discharges one but not the other (decouples the regulator-class diagnosis; specify which); (iii) projector discharges neither (the W6 §3 common diagnosis is wrong; both corollaries need independent refinement routes — specify what differentiates them)

### Candidate 2 — Substrate-determined regulator class: what does the D_K eigenvalue density admit?

**What it would do**: Investigate whether the substrate's actual D_K eigenvalue distribution (mean λ ≈ 3.23, max ≈ 4.67 in M_KK units, 78,080 eigenvalues at L_max=10 across 65 SU(3) sectors) inherently selects a preferred regulator class — i.e., whether the substrate "tells" us which regulator's leading term will dominate at the actual spectral density, rather than the regulator being an external choice. Connect this to Pillar VII (spectral dimension flow): in CDT / asymptotic-safety, d_s flow is regulator-dependent and the physically-meaningful d_s is the one robust to regulator-class change. If the smooth-cutoff regulator's tree-level Weyl shift dominates by 6-7 OOM AT THIS SPECIFIC EIGENVALUE DENSITY, what changes if the substrate's spectral content shifts (e.g., post-fold vs pre-fold)? Is there a structural reason the smooth-cutoff is the WRONG regulator class for the substrate, beyond C-γ-WEAK?

**Why it's worthwhile**: W6-3's CC2 σ-scaling diagnostic (linear-not-quadratic) identifies a STRUCTURAL feature of the smooth-cutoff regulator at the actual D_K spectrum that holds independent of the C-γ-WEAK gate question. The W6-3 carry-forward #3 already proposes promoting σ²-scaling to a §VII.S.* default audit clause — but the deeper question is WHY the substrate exhibits this signature, and whether it's a permanent property or a regime-dependent one. This is a phononic-framing workshop in the literal sense: the regulator-class admissibility is a property of the FABRIC (eigenvalue density of D_K), not an external regularization choice. Cross-pillar relevance to Pillar VII — the spectral dimension d_s of the substrate is regulator-dependent and the regulator-robustness criterion in CDT/AS literature (Calcagni, Oriti) is structurally analogous. If the substrate self-selects a regulator class via its eigenvalue density, that is a phononic prediction, not a methodological choice. The W6 dual-FAIL is the empirical surface on which this question becomes concrete.

**Type**: solo (2 agents) — independent reads, no coordination, written reports

**Suggested agents**: lizzi-spectral-functional-theorist, volovik-superfluid-universe-theorist

**Rounds (workshops only)**: n/a (solo, independent)

**Context the workshop will need**:
- W6-3 CC2 σ-scaling diagnostic table at Λ_cut = M_KK (LHS scales linearly with σ, not quadratically)
- W6-3 D_K eigenvalue distribution summary statistics (mean 3.23, max 4.67 in M_KK units; 78,080 eigenvalues; 65 SU(3) sectors via Peter-Weyl block decomposition)
- W6-3 §M.0 b_DK derivation: y_t = 0.7019918699, Tr_F(Y†Y) = 1.4783, b_DK = 0.006241291006
- W6 synthesis §3 substitution chain identifying smooth-cutoff regulator-class as common bottleneck
- Pillar VII references: CDT/asymptotic-safety regulator-dependence of d_s flow; the project's S63 spectral dimension result (`s63_spectral_dimension.md`: d_s peak 4.97 PW / 2.78 MC, truncation-limited)
- Question to each agent: "Does the substrate's actual spectral content (D_K eigenvalue density at L_max=10, mean 3.23, max 4.67) inherently select a preferred regulator class, and if so, what is the substrate-level criterion for that selection? What would change if the spectral content shifts (pre/post-fold)? Is the W6-3 σ-scaling diagnostic a regime-dependent measurement or a permanent substrate property?"
- Adjudication rule: each agent produces an independent written report; consolidator (separate dispatch, not part of this workshop) compares whether they converge on a substrate-level regulator-admissibility criterion or diverge, and what each criterion predicts for the 6 DEFERRED-S87 corollaries

### Candidate 3 — §VII.S DEFERRED-S87 cascade pre-flight

**What it would do**: Pre-flight the 6 DEFERRED-S87 corollaries (A gauge-fixing, C non-perturbative instanton residue, E KMS state, F finite-rank K, G twisted spectral triple, ι heat-kernel regulator-shift) as a single triage exercise. For each corollary: (a) state the statement form (X / Y / Z per the family-level Theorem), (b) identify which regulator class the test will use, (c) predict whether the W6 dual-FAIL diagnosis applies (i.e., does the smooth-cutoff regulator's tree-level term contaminate this corollary too?), (d) assign each to a wave classification — direct compute (quantitative gate), zero-compute proof (structural identity argument), or dependent-on-Mellin-cone (need Candidate 1's outcome first). Output is a 6-row pre-flight table with effort estimates, machinery prereqs, and dispatch-readiness flags.

**Why it's worthwhile**: The W6-1 §VII.S landing has 6 pre-allocated DEFERRED-S87 slots with documented status tags but no per-corollary triage. The S87 plan will need to allocate these into waves; doing the triage in S86 closeout (before S87 plan-write) prevents the S87 planner from re-deriving the per-corollary regulator-class question from scratch. The W6 dual-FAIL identifies a class of contamination (smooth-cutoff tree-level dominance) that may apply to some but not all of the 6 — for instance, C (instanton residue) and E (KMS state) are EXTENSIVE corollaries while A, F, G, ι are INTENSIVE; the IEP class might predict which inherit the contamination. A 1-2 hour solo synthesis converts the §VII.S 10-row atlas from a registry-landed inventory into a S87 dispatch-ready cascade. Without it, the S87 plan re-derives the regulator-class question per corollary.

**Type**: solo (1 agent)

**Suggested agents**: connes-ncg-theorist (the §VII.S registry author + author of the W6-1 landing; has the corollary-class structure already loaded)

**Rounds (workshops only)**: n/a (solo)

**Context the workshop will need**:
- §VII.S 10-row corollary atlas at `permanent-results-registry.md` line 12940+ (60-line addendum)
- 6 DEFERRED-S87 rows: §VII.S.A C-α (gauge-fixing, INTENSIVE), §VII.S.C C-β (instanton residue, EXTENSIVE), §VII.S.E C-δ (KMS state, EXTENSIVE), §VII.S.F C-ε (finite-rank K, EXTENSIVE), §VII.S.G C-ζ (twisted spectral triple, INTENSIVE), §VII.S.ι C-ι (heat-kernel regulator-shift, INTENSIVE)
- W6 synthesis §3 dual-FAIL diagnosis: smooth-cutoff regulator tree-level dominance at actual D_K eigenvalue density
- IEP classification rule: which IEP class (INTENSIVE vs EXTENSIVE) is more vulnerable to the smooth-cutoff tree-level contamination?
- Source-of-truth references per corollary: lizzi 9A §6.8 (B-2) for the 1C 6-Φ-branch enumeration; AC-2010 §V Eq. (5.3) for b_DK family; eq_6446 (k_W=0 representation-content); eq_6457 (a_DK Euler density); eq_6458 (b_DK Duff cancellation) per W6-1 trace_entity result
- W6-3 carry-forward #1 (C-γ-STRONG Mellin-cone): if Candidate 1 lands, which of the 6 DEFERRED corollaries inherit the projector machinery?
- Output template: 6-row table with columns {Branch, Corollary ID, Statement form X/Y/Z, Regulator class, Smooth-cutoff vulnerable?, Wave class (direct/zero-compute/Mellin-cone-dependent), Effort estimate (h), Machinery prereqs}
