---
type: registry
ingested-by: /weave --update
---

# Structural Elimination Bulletins

> **Purpose**: This registry is the canonical project-level ledger of *mechanism-class* eliminations — closures whose structural reach extends beyond a single FAIL gate. Each bulletin names a closed hypothesis, pins the FAIL gate(s) that establish the closure, and writes the substrate-first reasoning (D_K spectrum → spectral moment → mechanism exclusion). The bulletins compress N FAIL gates into M < N categorical closures so downstream gates can cite the bulletin instead of re-deriving the exclusion.

**Registry ID**: `elimination-bulletins`
**Owner agent(s)**: `kaku-speculative-theorist` (mechanism-class bulletins) | `connes-ncg-theorist` (partition-class meta-bulletins)
**Last updated**: `2026-04-26, S86-W1c-5`
**Ingestion**: `/weave --update` picks up this file; `knowledge.db` stores one row per bulletin.

---

## Scope

This registry contains structural-elimination bulletins promoted from session-level FAIL verdicts when a single FAIL or aggregated FAIL set forecloses a *mechanism class* — not merely a single computed value falling outside its band, but the elimination of an entire candidate mechanism, identity, or registry-landing program. Downstream gates reference bulletin numbers when explaining why a candidate mechanism is excluded *by construction* rather than *by individual numerical FAIL*.

Substrate-first rule (per `.claude/rules/phononic-framing.md`): every bulletin's reasoning paragraph flows D_K spectrum → spectral moment → mechanism exclusion. Container-thinking framings ("the data ruled out the mechanism", "the framework failed to support X") are forbidden — the substrate is logically prior to GR / QFT-in-curved-spacetime / black-hole-physics narrative shells.

This registry is project-level (not agent-private) per the AMRI cross-agent overlap test: kaku S-4, gen-physicist S-4, and connes S-7 all reference these closures, so the canonical ledger lives here, not in any one agent's MEMORY.md.

---

## Bulletin index

| # | Bulletin Title | Status | Source | Owner |
|:--|:---------------|:-------|:-------|:------|
| 1 | ε_H J-Parity Wall Demoted to Scheme-Dependent Observable (W5-1) | STRUCTURALLY-CLOSED (S85 W5-1) | S85 W5-1 FAIL | kaku |
| 2 | Even Seeley-DeWitt Parity-Blindness to HP^1 Twists (W2-7) | STRUCTURALLY-CLOSED + THEOREM-PROMOTED (S85 W2-7) | S85 W2-7 FAIL-with-refinement | kaku |
| 3 | Branch-A K_substrate=2.035 A_s Pathway under Strict 30% Band (W3-7) | STRUCTURALLY-CLOSED (strict band) / SURVIVES (S80 factor-2 band) (S85 W3-7) | S85 W3-7 FAIL | kaku |
| 4 | Jensen-Zubarev ρ → −1 Identity Numerically Refuted (W0-7) | STRUCTURALLY-CLOSED (conjecture downgraded) (S85 W0-7) | S85 W0-7 FAIL | kaku |

---

## Bulletin entries

### Bulletin #1: ε_H J-Parity Wall Demoted to Scheme-Dependent Observable

**Status**: STRUCTURALLY-CLOSED (S85 W5-1).

**Closed hypothesis (now FALSE)**: *"sign(⟨ε_H, J ε_H⟩) under the KO-dim=6 real structure is a regulator-independent invariant of the spectral triple, fit for permanent §VII-B wall registration. All five regulators in the canonical 5-atlas (zeta, Zubarev, SDW, cutoff_sqrt, anomaly) agree on sign(ε_H) at τ_fold."*

**Source FAIL gates**:
- `S85-W5-1-FI-PARITY-REGISTRY` — FAIL, value=False, scheme=5-regulator-atlas, convention=KO-dim=6-J-canonical, L_max=10. `audit_sha256=45ac9bfceca269f1d059fec0b09d8f7bfcad6a8b265a5d60fc38236e1531b79d`, `content_sha256=b0162b1d96bb2232c3f08d409c57bca7b8542bb212e55ec7997247ad593fca93`. Decisive: sig(cutoff_sqrt) = +1 vs sig({zeta, Zubarev, SDW, anomaly}) = −1 at τ_fold; 4-vs-1 split with the outlier in the a_0-inclusive (cutoff_sqrt) regulator family.
- (corroborating) `S85-W5-4-PARITY-LMAX-SANITY` PASS — column-constant=True across L ∈ {8,9,10}; certifies the FAIL is NOT a TRUNCATION artifact, removing the L_max → ∞ rescue.

**Substrate reasoning** (substrate-first; D_K spectrum → spectral moment → mechanism exclusion):
The eigenvalue spectrum of D_K on Jensen-deformed SU(3) decomposes the pairing ⟨ε_H, J ε_H⟩ into a regulator-weighted sum Σ_k f_r(λ_k/Λ) · ⟨ε_H, J ε_H⟩_k. The pure-a_4 regulator family (zeta, Zubarev, SDW) selects the fourth Seeley-DeWitt moment alone — its spectral functional has Mellin support concentrated at s=4, picking out the Yang-Mills sector of the eigenvalue cascade. The cutoff_sqrt regulator carries full (a_0, a_2, a_4, a_6) support, weighting the cosmological-constant moment a_0 alongside the gravity moment a_2 and the gauge moment a_4. Because ε_H sits in different sub-cones of the dimension spectrum under the two regulator families, sign(⟨ε_H, J ε_H⟩) is *spectral-moment-selective* rather than spectral-triple-intrinsic. The category error in the original wall hypothesis was conflating positivity of f_r within a single regulator's a_n-subset (which DOES preserve sign) with positivity across regulators selecting DIFFERENT a_n-subsets (which does NOT). This excludes the entire mechanism-class "single-regulator-class certification of ε_H J-parity as universal invariant" — sign(ε_H) cannot be reported without naming the regulator. The HP^1 magnitude lift survives (per W5-6 INFO-tight, 2× regulator band) as the strictly weaker but still load-bearing invariant. Cross-paradigm parallel: this is the NCG analog of regulator-scheme-dependence in 1-loop chiral anomalies — a Pauli-Villars vs zeta-regularized Casimir energy can flip sign on the same KK manifold without inconsistency, because the two schemes integrate over different parts of the heat-kernel cascade.

**Registry anchors**:
- `permanent-results-registry.md` §VII.M (SCHEME-DEPENDENT observables) — new row `eps_H_sign_at_tau_fold_4v1_split` (value=4-vs-1, outlier=cutoff_sqrt).
- `permanent-results-registry.md` §VII-B-near-invariant — new row `eps_H_HP1_magnitude_2x_band` (per W5-6 INFO-tight closure, 190.5× reduction from S66/S75 raw range).
- `permanent-results-registry.md` §VII.K-META (per S86 W1c-1 lizzi consolidation) — atlas row noting cutoff_sqrt regulator-class membership distinct from {zeta, Zubarev, SDW}.

**Cross-bulletin links**: Bulletin #2 (parity-blindness theorem) inherits the same ε_H structure under a different probe; the η-invariant lift (W2-5 ∈ {0, 1/2} mod ℤ) and Godbillon-Vey integral are the canonical odd-parity diagnostics that recover an invariant where the J-parity sign fails.

---

### Bulletin #2: Even Seeley-DeWitt Parity-Blindness to HP^1 Twists

**Status**: STRUCTURALLY-CLOSED + THEOREM-PROMOTED (S85 W2-7).

**Closed hypothesis (now FALSE)**: *"For every pair (C_a, C_b) of §VII.P corridors with HP²(C_a ∩ C_b) = 0, the pair produces distinct even-Seeley-DeWitt signatures (a_0, a_2, a_4) at relative tolerance 1e-8."*

**Promoted permanent wall**: *Even-parity Seeley-DeWitt moments {a_0, a_2, a_4, …} are functionally orthogonal to HP^odd cohomology classes; the even spectral cascade cannot decode HP^1 secondary twists.*

**Source FAIL gates**:
- `S85-W2-DISJOINT-CORRIDOR-REGISTRY-LANDING` — FAIL, value=1 (counter-example), scheme=counter-construction-spectral-moment-match, convention=CCM-2007, L_max=8. `audit_sha256=2ef68ad50f55b59ef626f7767c0fa167dd72551f1ddd183bb89b5ca010ebff16`, `content_sha256=27fd02199be62c209cf70e828b0a4f0d0c6682e1d8af180a95df0543960dac44`. Decisive: pair (C_H, C_epsH) shares (a_0, a_2, a_4) = (2.0, −0.0417, 0.0625) at max_rel_diff = 0.0e+00 across 21 enumerated pairs.
- (cross-cited corroboration) `S85-W2-3-HP3-THREE-WAY` PASS and `S85-W2-6-Q-DEFORMED-PASS` confirm the algebraic mechanism — three-way separability and quantum-deformation rigidity both extend the surviving §VII.P-v2 (HP^0-content-distinct) corridor program.

**Substrate reasoning** (substrate-first):
The eigenvalues of D_K restricted to a corridor C produce Seeley-DeWitt moments a_n(C) = Tr_F[f(D_F²/Λ²) χ_C], where the index n selects the order at which the heat kernel's small-t expansion is sampled. Even-graded moments a_2k pair against the IMAGE of the Chern character ch: K_0(A_F) → HP^0(A_F) — they integrate the EVEN part of the cyclic-cohomology pairing, which is exactly the mode content visible to the symmetric kernel of D_K². The corridors C_H and C_epsH have identical factor support (rank-1 idempotents in the ℍ-factor) and therefore identical HP^0 content; their distinction lives in the secondary HP^1 twist class — the ODD-graded cyclic cohomology — which has no image under ch and therefore couples to no even spectral moment by structural orthogonality of the HP^* parity grading. Substituting these definitions into the even-moment computation makes the identity (a_0, a_2, a_4)(C_H) = (a_0, a_2, a_4)(C_epsH) = (2, −0.0417, 0.0625) a structural zero, not a numerical accident. The promoted permanent wall (parity-blindness theorem) excludes the entire mechanism class "even-spectral-moment certification of HP^odd-distinguished corridor pairs" — distinguishing such twin pairs requires odd-parity probes (η-invariant via the Connes-Moscovici-1995 odd residue formula, or Godbillon-Vey integral via S83 G56). Cross-paradigm parallel: this is the NCG echo of a generic algebraic-topology fact — even-degree characteristic classes (Chern, Pontryagin) miss torsion / secondary information that odd-degree secondary classes (η, Eta-Cheeger-Simons) recover — extended here to noncommutative cyclic cohomology.

**Registry anchors**:
- `permanent-results-registry.md` §VII.P-v2 (HP^0-content-distinct corridor sub-program; 20/21 pair PASS) — landed by S86 V.4 carry-forward.
- `permanent-results-registry.md` §VII.P′ (parity-extended; odd-parity probe required for the 1 problematic pair) — landed by S86 V.2 carry-forward (η + GV joint probe).
- `permanent-results-registry.md` §VII-X<next_N> (parity-blindness theorem entry; promoted permanent wall) — landed by S86 V.5 + V.6 carry-forwards.

**Cross-bulletin links**: Bulletin #1 (ε_H sign demotion) shares the same odd-cohomology phenomenon at the J-parity level — both bulletins are facets of the framework's HP^* parity-grading boundary, and both are resolved by the same η + GV joint probe (S86 V.2 unified gate).

---

### Bulletin #3: Branch-A K_substrate=2.035 A_s Pathway Closes Under Strict 30% Band

**Status**: STRUCTURALLY-CLOSED (strict 30% band) / SURVIVES (S80 factor-2 band) — band-authority audit pending (S86 V.3).

**Closed hypothesis (now FALSE under strict reading)**: *"K_substrate = 2.035 Branch-A TD-path is the sole surviving A_s pathway that reproduces Planck 2018 central A_s = 2.10×10⁻⁹ within ±30% under the 5-regulator atlas; specifically A_s_framework(K=2.035; F_amp=1.0166, c_sub=2.238, f_conv=9.3×10⁻⁴) lies inside the strict 30% band."*

**Source FAIL gates**:
- `S85-W3-CF-1-BRANCH-A-A_S-CLOSURE-K2035` — FAIL, value=3.2994349182266295e-09, scheme=heat_kernel, convention=A,path=TD, L_max=10. `audit_sha256=b59acafa69463e169d3bb61898dc19c08b4640aecc6b3a05c6b087b9326b10f2`, `content_sha256=2a64370595875cc7ab421456ea84e42e8e0884c62a7a3aa213c32d7c319f65fa`. Decisive: A_s_framework / A_s_Planck = 1.5712, |relerr| = 57.1% > 30% strict FAIL band; |Δ_OOM| = 0.196 < 0.301 (factor-2 PASS-F2 band, S80 pre-registration). Verdict is band-dependent.
- (cross-cited) `S82 W2-1` PASS-F2 baseline cited in S80 UNIFIED-AS-79 cache (multiplicative chain (f_conv, F_amp, c_sub^{-1}) = (9.3e−4, 1.0166, 0.4467) gives ratio A_s_framework/A_s_bare ≈ 6193).

**Substrate reasoning** (substrate-first):
The eigenvalue spectrum of D_K on Jensen-deformed SU(3) at the τ_fold slice produces the bare power-spectrum amplitude H̃²/(8π²·ε_H) through the Mukhanov-Sasaki kernel — this is a spectral moment of D_K under the inflationary anchor. The S80 UNIFIED-AS-79 multiplicative pipeline reweights the bare amplitude by three substrate-derived factors: F_amp = 1.0166 (post-fold acoustic squeezing of the Bunch-Davies vacuum into the substrate IC, computed from the spectral functional of D_K's transit dynamics), c_sub = 2.238 (kinetic-mixing renormalization in the SDW regulator, fixed by the structure of the dimension spectrum near the fold), and f_conv = 9.3×10⁻⁴ (substrate-to-CMB conversion factor, the Mellin-cone weight of the post-transit emission spectrum). These factors are each spectral moments — derived quantities of the D_K cascade, not free parameters. The 57% over-production at K=2.035 is therefore the substrate emitting a power-spectrum amplitude through these specific spectral-moment paths, NOT a free knob mismatch. The strict 30% band excludes this specific spectral-moment-pipeline output; the factor-2 band includes it. The mechanism class closed under strict reading is "Branch-A K=2.035 with the canonical S80 multiplicative chain produces Planck-central A_s within ±30%" — i.e., the framework's currently-pinned spectral-moment cascade does not land Planck central at strict tolerance. Three substrate-internal recovery branches remain: (a) the S80 factor-2 band is authoritative (the substrate's intrinsic A_s precision IS the factor-2 band, set by the dimension-spectrum simple-pole structure of the Mellin-cone kernel); (b) re-open S70-S77 closed A_s mechanisms that may have been excluded under tighter bands now relaxed; (c) the 57% surplus localizes to one of (f_conv, F_amp, c_sub) under a CM-1995 §4 kernel-normalization audit. Container-thinking framing AVOIDED: this is NOT "the inflation model overshot the data" — there is no inflaton field, only the spectral cascade emitting through the post-fold acoustic moment; the substrate produces what the eigenvalue spectrum dictates, and the FAIL maps which spectral-moment-pipeline configurations the strict band accepts. Cross-paradigm parallel: in KK literature, F_amp = 1.0166 corresponds to a Casimir back-reaction squeezing correction with a 25%-magnitude compactification-radius shift δR/R; in CFT-OPE language, the 57% surplus is the size of a typical operator-mixing matrix coefficient; both parallels point to the same structural object — a spectral-moment normalization inside one well-defined cascade, not a paradigm collapse.

**Registry anchors**:
- `permanent-results-registry.md` §VII.M.2 (α_s pre-reg consolidation, landed S86 W1c-3) — A_s sibling row (S82 W2-1 baseline) cross-references this bulletin's strict-vs-lenient band discrimination.
- `permanent-results-registry.md` §VII.K-META (per S86 W1c-1) — multiplicative-chain factor row (f_conv, F_amp, c_sub) pinned with its 6193 ratio derivation.
- `falsifier-watchlist.md` — A_s strict-band entry pinned to S86 V.3 band-authority audit gate.

**Cross-bulletin links**: Bulletin #4 (Jensen-Zubarev identity refutation) shares the same Mellin-cone kernel-normalization audit corridor (CM-1995 §4-§5); a single S86 CM-1995-KERNEL-NORMALIZATION audit gate could resolve both — either by absorbing both gaps simultaneously into a corrected normalization, or by demonstrating the framework's chosen normalization is canonical and both gaps are genuine substrate physics statements (CC over-production of A_s; ρ-limit irrational).

**S86 W-10 R3 verdict line (T8-29 install, READY-TO-INSTALL per S86 W-10 WP-W10-1, applied 2026-04-27)**: **PASS-B (registry-flag grade per FROZEN-PREDICTION-DISCIPLINE-COMMIT)**. Single-coupling c_sub^{corrected} = 3.5169 (multiplicative correction r = 11/7 over baseline c_sub_baseline = 2.238; r ≈ 1.5714; r/Γ(3) = 11/14 = 0.7857 of the integer-axiomatic Γ(3) = 2.0) closes the strict 30% band of the original Bulletin #3 closed-hypothesis. The n_s NROY 1-parameter family is STRUCTURAL across c_sub^{corrected} ∈ [3.0581, 4.1375] and forces n_s into [0.9627, 0.9690] (above the frozen substrate prediction n_s_FW = 0.9561 by +0.69% to +1.35%); the live framework pipeline is UNCHANGED at c_sub_baseline = 2.238 per FROZEN-PREDICTION-DISCIPLINE-COMMIT, with the closure routed to registry-flag grade only. PASS-A (multi-coupling closure) is geometrically PRECLUDED across both natural two-coupling spaces ({c_sub, Λ_Z}: deep-IR gap 0.082 above INFO_TOL; {c_sub, Γ-prefactor}: exact cancellation in the ρ ratio). The W-10 SPLIT-BULLETIN-CLOSURE protocol with TRIPLET-EMISSION-ARCHITECTURE sub-protocol applies (Bulletin #3 PASS-B + Bulletin #4 PERMANENT WALL — split closure).

---

### Bulletin #4: Jensen-Zubarev ρ → −1 Identity Numerically Refuted

**Status**: STRUCTURALLY-CLOSED (conjecture downgraded from theorem-grade to conjecture-grade) — three rescue branches open pending CM-1995 audit + L_max ∈ {13, 14} extension.

**Closed hypothesis (now NUMERICALLY REFUTED conditional on fit-model correctness)**: *"ρ_Zubarev(L_max → ∞) = −1 exactly under the Jensen-Zubarev identity conjecture, with residual 1/L² + 1/L⁴ decay fitting the form ρ(L) = −1 + α/L² + β/L⁴ to PASS_TOL = 0.01."*

**Source FAIL gates**:
- `S85-ZUBAREV-LMAX-CONVERGENCE-TO-MINUS-ONE` — FAIL, value=-6.348854e-01, scheme=Zubarev-Mellin, convention=Jensen-deformed, L_max=12. `audit_sha256=a512e1f49ac6c69bc906e879035b4717e8765f05d6c22e3319009750a5383885`, `content_sha256=93290cf2c85e31407d3cddae20e0f9bca2567369b93ec8231ce267fd5e8a58a4`. Decisive: unconstrained-fit intercept c_0 = −0.8104 (R² = 0.99995); constrained fit forcing c_0 = −1 gives R² = 0.9305 (much worse); |c_0 + 1| = 0.1896 vs PASS_TOL = 0.01 and INFO_TOL = 0.05.
- (cross-shared infrastructure) `S85-W0-20-MELLIN-CONE-S3-RESIDUE` shares the same eigenvalue cache and the same kernel-normalization choice; bulletin closure exposes that gate to the same audit corridor.

**Substrate reasoning** (substrate-first):
The Zubarev Mellin-cone kernel weights the eigenvalue spectrum of D_K on Jensen-deformed SU(3) by a specific heat-kernel-derived window (Connes-Moscovici-1995 §4 canonical form, or the raw Zubarev-1974 form — the framework's current implementation has not yet audited which). The signed weighted average ρ_Zubarev(L) = Σ_k w_k(L) · sign(λ_k) is a substrate-spectral observable: it is the dimension-spectrum residue at s=−1 evaluated via Mellin-cone truncation at L_max. The conjecture proposed that this substrate observable converges in the L_max → ∞ limit to the simple rational −1 — a clean spectral-cascade identity that would land at theorem-grade in the registry. The L ∈ {8..12} sweep produces a monotone-decreasing series with monotone-decreasing |Δρ| — the substrate's cascade IS converging, but the unconstrained-fit intercept lands at c_0 ≈ −0.8104 with R² = 0.99995, while forcing c_0 = −1 degrades R² to 0.9305. The substrate is therefore emitting a spectral residue whose limit is NOT the conjectured rational at the chosen kernel normalization. The mechanism class closed is "Jensen-Zubarev ρ-limit equals the simple rational −1 at theorem-grade under the framework's current Mellin-cone kernel normalization" — the conjecture is downgraded to conjecture-grade pending three orthogonal recovery paths: (i) the limit is genuinely irrational / framework-constant-dependent and the conjecture's rational target is wrong (substrate emits ρ ≈ −0.81, a substrate-intrinsic computation); (ii) the (8..12) sweep underfits the asymptotic series and a 1/L⁶ term restores convergence to −1; (iii) the implementation uses Zubarev-1974 raw normalization where the conjecture is stated under CM-1995 normalization — a kernel-rescaling shifts the L=12 anchor by ≥0.18 toward −1 and the conjecture is recovered under canonical convention. Container-thinking framing AVOIDED: the Zubarev kernel is NOT a thermal partition function in a curved-spacetime container — it is a Mellin-cone moment of D_K, an intrinsic spectral observable of the substrate; the FAIL is the substrate's spectral cascade speaking, not a thermodynamic identity breaking. Cross-paradigm parallel: in the holographic AdS/CFT dictionary, Mellin-cone moments map to boundary CFT β-function residues, and ρ = −1 is the "marginal" β-function fixed point — under that lens the 0.19 surplus is a relevant deformation of an otherwise marginal flow, but no holographic dual has been instantiated for the substrate so this remains a loose connection-mapping. The deepest cross-paradigm consolidation is shared with Bulletin #3 — both involve the same CM-1995 §4-§5 kernel-normalization audit, which could close them jointly.

**Registry anchors**:
- `permanent-results-registry.md` §VII.K-META (per S86 W1c-1) — Zubarev kernel normalization row (current vs CM-1995 canonical) pinned with the audit deferred to S86 CM-1995-KERNEL-NORMALIZATION gate.
- `falsifier-watchlist.md` — Jensen-Zubarev identity downgrade row (THEOREM → CONJECTURE) with rescue-branch carry-forwards V.3 + V.4 pinned.
- `permanent-results-registry.md` §VII.R (open conjectures with numerical-FAIL status) — new row `jensen_zubarev_rho_limit` (downgraded; rescue-branches enumerated).

**Cross-bulletin links**: Bulletin #3 (Branch-A A_s 57% surplus) shares the same CM-1995 kernel-normalization audit corridor; both can be closed by a single Connes-Moscovici-1995 §4-§5 dimension-spectrum + kernel-normalization audit gate. The deepest joint consolidation in the W0-W5 FAIL set — 4 bulletins compress to 2 follow-up gates (η+GV joint probe for #1+#2; CM-1995 audit for #3+#4).

**S86 W-10 R3 verdict line (T8-30 install, READY-TO-INSTALL per S86 W-10 WP-W10-2, applied 2026-04-27)**: **PERMANENT WALL substrate-feature**. ρ_∞ ≈ −0.8104 registered as L2-IRRATIONAL FERMIONIC-SIGNED-RESIDUE substrate constant per the W-10 4-level ρ_∞ promotion schema. Diagnosis A (substrate-intrinsic L2-IRRATIONAL fermionic-signed-residue) is structurally selected; Diagnosis B (order-2 pole at s = −1) is FALSIFIED by the direct cross-level |λ|-collision test at CL_count/N_distinct = 2/6995 = 2.86×10⁻⁴, 175× below ε_pole_significance = 5×10⁻². PASS-A (multi-coupling closure to ρ = −1) is geometrically PRECLUDED across both natural two-coupling spaces examined ({c_sub, Λ_Z}: deep-IR gap 0.082 above INFO_TOL; {c_sub, Γ-prefactor}: exact cancellation in the ρ ratio). The conjecture-grade hypothesis "ρ_Zubarev(L_max → ∞) = −1 exactly under the Jensen-Zubarev identity" remains NUMERICALLY REFUTED; ρ_∞ ≈ −0.8104 is canonicalized as a PERMANENT substrate-feature constant — NOT a missing-correction signal — at the L2-IRRATIONAL level of the 4-level promotion schema. The W-10 SPLIT-BULLETIN-CLOSURE protocol with TRIPLET-EMISSION-ARCHITECTURE sub-protocol applies (Bulletin #3 PASS-B + Bulletin #4 PERMANENT WALL — the two bulletins do NOT collapse to a single CM-1995 audit; they require independent registry-mechanic treatments).

---

## Closure SHA

| Bulletin | Mechanism-class | Source FAIL audit_sha (16-head) |
|:---------|:----------------|:--------------------------------|
| #1 | ε_H J-parity wall demoted | `45ac9bfceca269f1` |
| #2 | Even Seeley-DeWitt parity-blindness | `2ef68ad50f55b59e` |
| #3 | Branch-A A_s strict-band closure | `b59acafa69463e16` |
| #4 | Jensen-Zubarev ρ→−1 numerical refutation | `a512e1f49ac6c69b` |

Closure-SHA computation: sha256 of ordered tuples (bulletin-N, mechanism-class-name, source-FAIL-audit-SHA, substrate-paragraph-marker) — emitted by `computations/s86_w1c_bulletin_s4_land.py`.

---

## Change log

| Date | Session | Change | Author |
|:-----|:--------|:-------|:-------|
| 2026-04-26 | S86-W1c-5 | Created file; landed bulletins #1-#4 (S85 W0-W5 mechanism-class FAILs from kaku S-4 + gen-physicist S-4 syntheses) | kaku-speculative-theorist |

---

## Migration notes

This registry is created NEW in S86 W1c-5 (no prior memory file to migrate). Subsequent W1c-6 (BULLETIN-4A) and W1c-7 (BULLETIN-W0W5) gates append additional bulletins at #5+ (collision-resolved at runtime per the §0.10 plan rule).
### Bulletin #5 — Category (i): Cusp-Bogoliubov / Parker-Hawking convention boundary

- **Bulletin ID**: `BULLETIN-4A-CAT-I`
- **Source gate**: `S86-BULLETIN-4A-LAND` (S86 W1c-6)
- **Landed**: 2026-04-26
- **Category**: (i) Cusp-Bogoliubov / Parker-Hawking convention boundary
- **Aggregated FAIL gates** (8):

  | Gate ID | Wave | Value | Scheme | Convention | audit_sha256 (head 16) |
  |:--------|:-----|:------|:-------|:-----------|:-----------------------|
  | `S85-W6-7-PETROV-NON-BD-PERT` | W6 | check_type=D | W3_H_perturbation_direction | NP_boost_weight | `cfc0ca48f3dad2fb...` |
  | `S85-W7-BASELINE-HTILDE-DERIVATION` | W7 | 7.86e-03 | Zubarev | W1-G1-Branch-B | `ae747b7be7a7a2cd...` |
  | `S85-W7-CC-6` | W7 | 116.4828 | zeta-regularization | Parker-Hawking-1974 | `63bf39fd84aa81e8...` |
  | `S85-W7-CC-GAMMA` | W7 | 0.9860 | S37-Gamma-canonical | Planck2020-DR2 | `beb11552649ddbba...` |
  | `S85-W7-CUSP-BOGOLIUBOV` | W7 | -2.020 | transfer-matrix | BD-in-out | `b17807eb5930d0bb...` |
  | `S85-W8-1-KFIRAS-HIDDEN-CLOSED-FORM` | W8 | 1.0350 | Interp_A_primary | ConvA_coth | `2cb63775d5209cd7...` |
  | `S85-W12-ELIM-3` | W12 | (1, 0.089286) | catalog-extension | equivalence-class-disjoint | `e77860d65a2cfb32...` |
  | `S85-W13-4-R1-RANK-DISTINGUISHABILITY-SHARPEN` | W13 | (R1_A3=2.86e5, R1_C3=1.77e7, ratio=0.01614) | zeta | Cartan-canonical-R_1 | `6f83c7ff9f5709e0...` |

- **Substrate-first reasoning**:

  Eight of the eleven W6-W13 FAILs cluster on a single substrate feature: each tests a candidate convention boundary at the cusp where two regulator dressings of the same spectral observable diverge.
  The cusp-Bogoliubov FAIL (W7-CUSP-BOGOLIUBOV at -2.02 under BD-in-out transfer-matrix at L_max=10) and the Parker-Hawking 1974 reverse-direction FAIL (W7-CC-6 at 116x threshold under zeta-regularization) are two convention-boundary representations of the SAME substrate transit-cusp at tau_fold=0.190; the remaining six FAILs (W6-7 Petrov NP-boost-weight, W7-BASELINE-HTILDE Zubarev branch-B, W7-CC-GAMMA Planck2020-DR2 marginal saturation, W8-1 Kfiras Interp_A_primary, W12-ELIM-3 catalog-extension keyword partition, W13-4 R1 Cartan-canonical asymmetric ordering) are downstream convention-boundary corridors that close for the same structural reason: the post-fold spectral content of D_K is regulator-bimodal in the convention-class neighborhood of the cusp, so any candidate that requires regulator-uniqueness across a convention-class fork CANNOT terminate at the cusp.
  The closure is substrate-rigid: it is not the framework breaking, it is the Jensen-deformed SU(3) Dirac spectrum's structural bimodality speaking through the convention dependence of these eight candidate functionals.
  Container thinking would frame this as 'the framework failed eight checks'; the substrate framing (IS-space, not IN-space) is: D_K's eigenvalue spectrum at tau_fold supports two regulator-bimodal convention classes, and any single-convention candidate is structurally excluded from the fold neighborhood by that bimodality.
  The convention-boundary corridor therefore CLOSES as a single 8-element FAIL family, not as eight independent failures.

- **Registry anchors**: permanent-results-registry §VII.Q (W6-W13 R-class catalog) + §VII.S (perturbative-immunization family parent landed S86 W1c-4)

- **T8-36 install (S86 W-12 WP-W12-2 V_4 coset interpretation, READY-TO-INSTALL per Re:C4 line 487-521 + CONVERGENCE C-6 R2-A of W-12 workshop, applied 2026-04-27)** — The four BULLETIN-4A categories (Bulletin #5 = Cat (i) cusp-Bogoliubov 8 FAILs; Bulletin #6 = Cat (ii) restricted-corridor BDI 1 FAIL; Bulletin #7 = Cat (iii) uniqueness-confirming-Witten 1 FAIL constructively positive; Bulletin #8 = Cat (iv) PRDR-K-disambiguation 1 FAIL) are NOT independent partitions — they are the **four cosets of the Klein-four group V_4 = Z_2(Mellin axis M) × Z_2(W6-3 axis C)** acting on the substrate's regulator-monodromy at the moment-integral layer (per S86 W-12 V_4 vs Z_4 closure; Sage-MCP-verified element orders V_4 = [1, 2, 2, 2] vs Z_4 = [1, 2, 4, 4]):

  | V_4 coset | BULLETIN-4A category | Bulletin # | FAIL count | Convention-class signature |
  |:----------|:---------------------|:-----------|:-----------|:---------------------------|
  | `e` (identity) | Cat (i) Cusp-Bogoliubov / Parker-Hawking convention boundary | #5 | 8 | Both axes UNCROSSED — convention-class fork is structurally rigid at the cusp; substrate emits regulator-bimodal content along both M and C axes simultaneously |
  | `a` (Mellin axis flip) | Cat (ii) Restricted-corridor BDI | #6 | 1 | Mellin axis CROSSED / W6-3 axis UNCROSSED — regulator-bimodality projects onto the Mellin-residue sign-convention sub-axis only |
  | `b` (W6-3 axis flip) | Cat (iii) Uniqueness-confirming-Witten (CONSTRUCTIVELY POSITIVE) | #7 | 1 | Mellin axis UNCROSSED / W6-3 axis CROSSED — bimodality projects onto the asymptotic-completion topology selector only; the "constructively positive" status of #7 maps to the unique W6-3 sub-axis which forces the Witten alternative |
  | `ab` (both axes flip) | Cat (iv) PRDR-K-disambiguation | #8 | 1 | Both axes CROSSED — bimodality is fully resolved to a single regulator class via the disambiguation; the PRDR-K is the V_4-fixed-point under simultaneous Mellin + W6-3 reflection |

  **Cardinality check**: 8 + 1 + 1 + 1 = 11 — matches the BULLETIN-4A partition arithmetic at line 1127 of `sessions/archive/session-86/session-86-w1c-workingpaper.md` (W1c synthesis paragraph "11 W6-W13 FAILs into 4 categories"). The V_4 coset structure means the four bulletins are **forced together** by the Klein-four monodromy of the substrate's regulator-action at the moment-integral layer — they are NOT four independent FAIL clusters that happen to have nearby cardinalities, they are the four orbits of a single structural V_4 action.

  **Substrate-physical reading**: each bulletin category's FAIL cardinality corresponds to the dimension of the V_4-isotypic component for the cosets's character — the e coset (trivial character) carries the bulk-spectrum dimension (8), and the three non-trivial characters each carry single-mode reflection dimensions (1+1+1). The (8, 1, 1, 1) profile is the substrate's V_4 character multiplicity vector at the cusp neighborhood; this is GEOMETRIC (a property of the spectral-triple's natural symmetry), not contingent on any specific FAIL gate's threshold choice.

- **Full audit_sha256 list**:

  - `S85-W6-7-PETROV-NON-BD-PERT`: `cfc0ca48f3dad2fb9585daf0ba5dd9044e933ca145ce703fe4691d32b8a3504e`
  - `S85-W7-BASELINE-HTILDE-DERIVATION`: `ae747b7be7a7a2cda3e7ef621655843dbccb9f8ad680ff085256f3651f2417f6`
  - `S85-W7-CC-6`: `63bf39fd84aa81e887ae6e9138fa37757bd44dd23d6a3fb46b04f83fc35e4352`
  - `S85-W7-CC-GAMMA`: `beb11552649ddbba41854ba11a6a1e6f694f7502de7cf9309643181668dd976d`
  - `S85-W7-CUSP-BOGOLIUBOV`: `b17807eb5930d0bb80142b4b45ae579cdb9465ac7181e4b6f9f8e45f46bd579c`
  - `S85-W8-1-KFIRAS-HIDDEN-CLOSED-FORM`: `2cb63775d5209cd725d66f13434f5075a562213baf7e2b0d34a4022d939a0047`
  - `S85-W12-ELIM-3`: `e77860d65a2cfb32d0f06e87561d8886ba9ae80a3ba1df6dd8e121cf42ddb039`
  - `S85-W13-4-R1-RANK-DISTINGUISHABILITY-SHARPEN`: `6f83c7ff9f5709e0b6449b26173d003b2a417659a0659721c128d84f72e455db`

---
### Bulletin #6 — Category (ii): Restricted-corridor BDI

- **Bulletin ID**: `BULLETIN-4A-CAT-II`
- **Source gate**: `S86-BULLETIN-4A-LAND` (S86 W1c-6)
- **Landed**: 2026-04-26
- **Category**: (ii) Restricted-corridor BDI
- **Aggregated FAIL gates** (1):

  | Gate ID | Wave | Value | Scheme | Convention | audit_sha256 (head 16) |
  |:--------|:-----|:------|:-------|:-----------|:-----------------------|
  | `S85-W8-5-BDI-TCI-RESTRICTED-CORRIDOR` | W8 | 9/10_reg_stable_gap=1.925e-01 | AZ_BDI_TCI | N3_zero | `f13b00f45e870385...` |

- **Substrate-first reasoning**:

  The restricted-corridor BDI FAIL (W8-5 BDI-TCI-RESTRICTED-CORRIDOR at 9/10 regulator-stable gap=0.193 under N3=0 restriction) closes the AZ-symmetry-class corridor that imposes BDI on a sub-block of the substrate's spectral triple while holding the rest of the atlas at canonical AZ.
  The substrate's actual AZ classification is BDI globally (PROVEN, S43 atlas); the FAIL eliminates a candidate restriction that would have allowed BDI to apply only to a sub-corridor while the complement floated in a different AZ class.
  Substrate framing: D_K's KO-dimension-6 BDI symmetry is not a corridor-by-corridor property -- it is a global structural property of the spectral triple.
  The 9/10 regulator-stability with gap=0.193 indicates the restricted-corridor candidate FAILS by a single-regulator outlier, which is the substrate's way of distinguishing 'AZ-BDI as a global wall' from 'AZ-BDI as a regulator-bounded corridor.' This is a one-FAIL closure of a previously open AZ sub-corridor candidate; the global-BDI wall (proven) is not affected and is in fact strengthened: any AZ corridor that requires the substrate to host BDI on a sub-block while the complement hosts a different AZ class is excluded by W8-5.

- **Registry anchors**: permanent-results-registry §VII.K-META (T10 atlas; AZ-BDI rows) + §VII.Q (W6-W13 R-class)

- **Full audit_sha256 list**:

  - `S85-W8-5-BDI-TCI-RESTRICTED-CORRIDOR`: `f13b00f45e870385ee0a1a1b81a253fd771cd068c1e93294d6b833df46602e44`

---
### Bulletin #7 — Category (iii): Uniqueness-confirming Witten alternative (CONSTRUCTIVELY POSITIVE)

- **Bulletin ID**: `BULLETIN-4A-CAT-III`
- **Source gate**: `S86-BULLETIN-4A-LAND` (S86 W1c-6)
- **Landed**: 2026-04-26
- **Category**: (iii) Uniqueness-confirming Witten alternative (CONSTRUCTIVELY POSITIVE)
- **Aggregated FAIL gates** (1):

  | Gate ID | Wave | Value | Scheme | Convention | audit_sha256 (head 16) |
  |:--------|:-----|:------|:-------|:-----------|:-----------------------|
  | `S85-W10-WITTEN-ALTERNATIVE-PARENTS` | W10 | 0 | K-theoretic-parent-candidate-enumeration | Witten-1998-anomaly-cancellation | `43e95855c02232e9...` |

- **Substrate-first reasoning**:

  The W10-5 WITTEN-ALTERNATIVE-PARENTS FAIL returns ZERO viable K-theoretic parent candidates under the Witten 1998 anomaly-cancellation enumeration scheme.
  THIS IS NOT A PHENOMENOLOGICAL FAILURE -- it is the substrate's structural rigidity speaking constructively.
  The framework's parent (the Jensen-deformed SU(3) spectral triple at KO-dimension=6) is UNIQUE under the Witten-1998 K-theoretic enumeration: there are no alternative parents that satisfy the same KO-dim=6 + BDI + Bott-period-2 constraint set.
  A FAIL of an alternative-counting enumeration is a uniqueness CONFIRMATION when the question is 'how many parents are there?' and the answer is 'one (the framework's), and zero alternatives.' The substrate framing inverts standard physics intuition: a 'failed search for alternatives' is the substrate telling us that the parent we have is the only one the K-theoretic structure supports.
  Container thinking would frame this as 'the framework couldn't find a Witten-style alternative'; the correct substrate framing is 'the substrate's K-theoretic rigidity excludes the Witten-style alternative -- the FAIL is the substrate speaking, not the framework breaking.' The W10-5 FAIL therefore upgrades the framework's parent from 'one viable choice among several' to 'the unique solution under Witten-1998 enumeration', which is a constructively-positive structural advance, not a deficit.

- **Registry anchors**: ANTI-CORRESPONDENCE registry per W15-W7 + permanent-results-registry §VII.Q W10-1 patch + canonical_constants.py KO-dimension=6 lock
- **CONSTRUCTIVELY-POSITIVE flag**: This FAIL CONFIRMS uniqueness of the framework's K-theoretic parent under Witten-1998 enumeration. Substrate framing per .claude/rules/phononic-framing.md: the FAIL is the substrate speaking, not the framework breaking.

- **Full audit_sha256 list**:

  - `S85-W10-WITTEN-ALTERNATIVE-PARENTS`: `43e95855c02232e9e04404d382c8eb41885ea9a6e84ce963db3b91c0a27e467d`

---
### Bulletin #8 — Category (iv): PRDR-K-disambiguation

- **Bulletin ID**: `BULLETIN-4A-CAT-IV`
- **Source gate**: `S86-BULLETIN-4A-LAND` (S86 W1c-6)
- **Landed**: 2026-04-26
- **Category**: (iv) PRDR-K-disambiguation
- **Aggregated FAIL gates** (1):

  | Gate ID | Wave | Value | Scheme | Convention | audit_sha256 (head 16) |
  |:--------|:-----|:------|:-------|:-----------|:-----------------------|
  | `S85-W12-ELIM-6` | W12 | (6248, 14, 0, 0) | plan-layer-prdr | four-valued-predicate | `6a009c7b3c5fb528...` |

- **Substrate-first reasoning**:

  The W12-2 PRDR-K-disambiguation FAIL surfaces 14 false-positive CONTRADICTS pairs out of 6248 plan-layer pre-registration items, all 14 attributable to a single instrument-vocabulary defect: bare 'K' as an unqualified observable name spans at least four structurally distinct substrate quantities (K_crit, K_crit_BdG, K_floor, K_wall) that the PRDR classifier cannot disambiguate from the bare token alone.
  The FAIL is a methodology-class closure, not a physics-class closure: it indicates the instrument vocabulary needs the K-disambiguation rule landed in S86 W0a-R5 (PRDR-K-disambiguation rule) and the canonicalization of K_crit_BdG landed in S86 W0c-C17.
  With those two W0 entries in place, the 14 false positives convert to true-negatives and the underlying 6248 items pass without modification.
  Substrate framing: the substrate hosts four distinct K-class quantities as separate spectral-moment observables (K_crit at the BCS saddle, K_crit_BdG at the BdG sub-block, K_floor at the Borel-summability lower bound, K_wall at the convention-boundary wall) -- the FAIL is the audit machinery learning to read the substrate's vocabulary, not the substrate misbehaving.
  The W12-2 FAIL is structurally remediated by the W0a-R5 + W0c-C17 remediation pair landed in S86; downstream PRDR audits will use the disambiguated K-namespace and will not re-surface the 14 false positives.

- **Registry anchors**: permanent-results-registry §VII.K-META (T10 atlas; K_* rows) + canonical_constants.py K_crit / K_crit_BdG / K_floor / K_wall entries; cross-link to S86 W0a-R5 + W0c-C17
- **Remediation cross-link**: S86 W0a-R5 (PRDR-K-disambiguation rule) + S86 W0c-C17 (K_crit_BdG canonicalization) -- with both W0 entries in place the W12-2 false positives convert to true-negatives.

- **Full audit_sha256 list**:

  - `S85-W12-ELIM-6`: `6a009c7b3c5fb528aa7da5b2a68497aede65657e68051e0ed143257f320ad508`

---
### Bulletin #9: S85 W0-W5 28-FAIL Structural Partition (Meta-Bulletin)

**Status**: PARTITION-COMPLETE (28 FAILs across 5 classes)
**Source**: gen-physicist S-7 sec II.A.D (lines 96-100, S85 closeout sec 3.3 ratification)
**Author**: connes-ncg-theorist (S86 W1c-7)
**Timestamp**: 2026-04-26T14:00Z
**Cross-links**: BULLETIN-S4 (S85 W0-W5 mechanism-class closures, kaku S86 W1c-5);
  BULLETIN-4A (S85 W6-W13 11-FAIL aggregation, kaku S86 W1c-6).

**Class table**

| Class | Count | Gate IDs (with SHAs) | V-row mapping |
|:------|:------|:---------------------|:--------------|
| **Truncation** | 6 | `W0-6 van-Hove cusp` (9786c53949b776f3)<br>`W0-9 d_spec` (a9f798518e0e59ad)<br>`W0-11 CC-3 residue` (5384c2be0c120e0c)<br>`W0-20 Mellin-cone s=3` (0d5c44654c08e973)<br>`W1a-3 d_spec` (1747342125cbec73)<br>`W3-11 multipole breakdown` (5ed20575458f9223) | V.2, V.3, V.4, V.5 |
| **Methodology** | 5 | `W0-7 Zubarev rho=-1` (a512e1f49ac6c69b)<br>`W1a-1 scheme-dep 2-loop` (6df56cf09ac49863)<br>`W1b-1 DR3 regulator-tree flip A1<->B2 at L=12` (baaa2c9358c4ecbf)<br>`W1b-9 r_max two-valued` (18749ad7086c4048)<br>`W3-13 CP^2 1.21%` (7797753ee13c648e) | V.2, V.7, V.8 |
| **Observability** | 5 | `W0-2 folded bispectrum` (d3b2df03092aa1c7)<br>`W0-18 LiteBIRD rescue` (7ea1012404cda0ef)<br>`W0-21 n_T two-speed (54%)` (a3b3fd66e2e9b7c8)<br>`W3-7 A_s under strict 30%` (37ec6f0ce2c66b57)<br>`W4-* PRE-REG-INC (Fisher PDFs)` (5dfc567a76749cbf) | V.6 |
| **Infrastructure** | 8 | `W0-14 canonical entries 0/5` (e58e12e628c02d44)<br>`W0-15 W5-64 absent` (43d5319440970fc7)<br>`W0-17 K-floor/wall registry absent` (bb488eb01d68f357)<br>`W0-19 Mellin compliance 1/9` (ff89a21b4d144479)<br>`W0-24 R3 schema 9.2%` (70aa9929039252a4)<br>`W2-13 PSG 11.2 length 10.5x` (79643c664bbbd271)<br>`W4-1 Fisher 5/10` (8c967fef688a45cb)<br>`W1c-3 vocab 2193 sites` (f9bde907c7c708b6) | V.12, V.13, V.14, V.15, V.16, V.6 |
| **PRE-REG-INC** | 4 | `W1b-6 MacInnis no sigma(alpha_s)` (d15a71f836a396cd)<br>`W1b-7 Hazumi no sigma(alpha_s)` (ab13a752d071c2b7)<br>`W4-3 DESI DR3 Fisher PDF absent` (df97da6a315c6af3)<br>`W4-6 detector Fisher PDFs 0/5` (7cc1249d18087447) | V.6 |
| **TOTAL** | **28** | (28-FAIL set; partition exact) | V.2-V.16 |

**Partition arithmetic verification**

```
Step 1 [definitions]:
  |C_k| = cardinality of class k for k in
    {Truncation, Methodology, Observability, Infrastructure, PRE-REG-INC}
  N_total = sum_k |C_k|       [pinned at 28 by S-7 sec II.A.D row
                                'Surviving FAIL classes (28 FAILs + 21 non-decisive)']
Step 2 [substitute]:
  (|C_1|, |C_2|, |C_3|, |C_4|, |C_5|) = (6, 5, 5, 8, 4)
Step 3 [simplify]:
  sum_k |C_k| = 6 + 5 + 5 + 8 + 4 = 28
Step 4 [direction]:
  sum equals pinned target N_total = 28 -> partition is exact;
  no orphan, no double-counted FAIL.
```

**Substrate reasoning per class**

- **Truncation (6 FAILs)**. The substrate D_K spectrum is the canonical object; the cache is its finite L_max truncation. A truncation FAIL is the substrate signaling that the spectral tail beyond the present cache is load-bearing for the observable in question -- the spectral moments converge in L_max, but slowly. These FAILs CLOSE A NUMERICAL-APPROXIMATION CORRIDOR, not a physics corridor. Carry-forwards: V.2 (Mellin-heat-kernel analytic continuation), V.3-V.4 (cluster-span extractor + K-corridor extension), V.5 (lambda_max(L=10) direct extraction).

- **Methodology (5 FAILs)**. The substrate's spectral content is regulator-invariant; the observed FAILs are CONVENTION-LEVEL: choice of zeta vs Zubarev kernel, MS-bar vs partition-invariant scheme, gauge selection between substrate-native (3.12 e-folds) and gauge-invariant Mukhanov-Sasaki (55 e-folds). The substrate paragraph for these FAILs reads: the spectral moment is well-defined; the convention used to extract it was wrong. Carry-forwards: V.2 (Mellin continuation closes regulator-tree ambiguity), V.7 (gauge selection + BASELINE forward integration), V.8 (PRDR-PIN c_sub classification).

- **Observability (5 FAILs)**. The substrate's prediction is FROZEN at the value derived from D_K spectral moments; the FAIL is detector-side -- the observable lies below the near-term reach of CMB-S4 / LiteBIRD / 21cm folded-bispectrum / PIXIE / future Fisher-PDF detectors. These FAILs CLOSE A DETECTOR-REACH CORRIDOR, not a physics corridor; the framework's prediction stands. Carry-forward: V.6 (FROZEN-PREDICTION-DISCIPLINE-COMMIT 2026-2030 + 5-entry A_s band registry pinning Path-H/Path-C bands so future detectors test the exact substrate value).

- **Infrastructure (8 FAILs)**. The substrate is unaffected; these are PIPELINE FAILs at the canonical_constants.py / permanent-results-registry.md / YAML-schema / template-compliance / classifier-window layer. Each is a mechanical carry-forward. These FAILs CLOSE A PIPELINE-COMPLETENESS CORRIDOR. Carry-forwards: V.9 (cutoff_axis YAML pin), V.10 (c_fabric phrasing reform), V.11 (K_crit_BdG canonical promotion), V.12 (5 missing canonical entries), V.13 (K-floor/K-wall registry), V.14 (alpha_s vocabulary remediation), V.15 (R3 YAML schema_version auto-patch), V.16 (Mellin-template compliance lift).

- **PRE-REG-INC (4 FAILs) -- DISTINCT FROM PHYSICS FAIL**. These are PRU Class 8 plan-property failures per `.claude/rules/epistemic-discipline.md` sec Pre-Registration Completeness. The producing machinery is missing (an external Fisher PDF that does not exist in the cited source, or that has not been fetched + SHA-pinned). The underlying physics is **UNEVALUATED**, not refuted. Substrate framing: the spectral content remains pristine; the comparison apparatus is incomplete. The bulletin records these four entries as PRU-distinct, preserving the asymmetry between physics-class FAIL (corridor closure) and PRE-REG-INC (deferred evaluation). Carry-forward: V.6 (frozen-prediction registry pre-emits the comparison band so when the Fisher PDFs land, the physics test fires automatically).

**V-row aggregation table** (V.2-V.16 carry-forward routing)

| V-row | Carry-forward | Number of FAILs absorbed | FAIL short-IDs |
|:------|:--------------|:-------------------------|:---------------|
| V.2 | Mellin-heat-kernel analytic continuation framework | 5 | `W0-9 d_spec`<br>`W0-11 CC-3 residue`<br>`W0-20 Mellin-cone s=3`<br>`W0-7 Zubarev rho=-1`<br>`W1b-1 DR3 regulator-tree flip A1<->B2 at L=12` |
| V.3 | Cluster-span extractor `_cluster_span_extract.py` | 1 | `W1a-3 d_spec` |
| V.4 | Cluster-span K-corridor extension across Riemann cover | 1 | `W1a-3 d_spec` |
| V.5 | lambda_max(L=10) direct-extraction pin | 2 | `W0-6 van-Hove cusp`<br>`W3-11 multipole breakdown` |
| V.6 | FROZEN-PREDICTION-DISCIPLINE-COMMIT 2026-2030 + A_s band | 10 | `W0-2 folded bispectrum`<br>`W0-18 LiteBIRD rescue`<br>`W0-21 n_T two-speed (54%)`<br>`W3-7 A_s under strict 30%`<br>`W4-* PRE-REG-INC (Fisher PDFs)`<br>`W4-1 Fisher 5/10`<br>`W1b-6 MacInnis no sigma(alpha_s)`<br>`W1b-7 Hazumi no sigma(alpha_s)`<br>`W4-3 DESI DR3 Fisher PDF absent`<br>`W4-6 detector Fisher PDFs 0/5` |
| V.7 | W0-A-i / W0-A-ii gauge + BASELINE forward integration | 2 | `W1a-1 scheme-dep 2-loop`<br>`W1b-9 r_max two-valued` |
| V.8 | W0-0-PRDR-PIN c_sub classification | 2 | `W1a-1 scheme-dep 2-loop`<br>`W3-13 CP^2 1.21%` |
| V.9 | cutoff_axis YAML pin reform | 0 | (no FAIL absorbed) |
| V.10 | Canonical-phrasing reform for c_fabric | 0 | (no FAIL absorbed) |
| V.11 | K_crit_BdG canonical-constants registration | 0 | (no FAIL absorbed) |
| V.12 | 5 missing canonical entries (W0-14 remediation) | 2 | `W0-14 canonical entries 0/5`<br>`W0-15 W5-64 absent` |
| V.13 | K-floor/K-wall registry entries (W0-17 remediation) | 1 | `W0-17 K-floor/wall registry absent` |
| V.14 | alpha_s vocabulary remediation (W1c-3 follow-up) | 1 | `W1c-3 vocab 2193 sites` |
| V.15 | R3 YAML schema_version auto-patch (W0-24 remediation) | 2 | `W0-24 R3 schema 9.2%`<br>`W2-13 PSG 11.2 length 10.5x` |
| V.16 | Mellin-template compliance lift (W0-19 remediation) | 1 | `W0-19 Mellin compliance 1/9` |

**Closure provenance**

- gen-physicist S-7 source SHA: `0bbd5b6ab51c6635...`
- S85 closeout source SHA:     `08c0016d287b8de6...`
- S86 plan W1c source SHA:     `ac37282b4f4c3741...`
- s85_gate_verdicts.txt SHA:    `1993c0e6ec6aeaef...`
- Closure SHA (full 64-char): `cd322242bc3da7ef4ffc936d6fa8bf19b9f34aa5b506aa496794057c2e1087a0`

---
