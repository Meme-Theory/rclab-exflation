# Seed file — Chunk 1 (lines 7-2271, waves W1a + W1b)

**Date**: 2026-05-02
**Investigator**: phonon-first-cosmologist
**Source**: `C:\sandbox\Ainulindale Exflation\sessions\archive\session-87\session-87-results-workingpaper.md` lines 7-2271
**Plan files**: `C:\sandbox\Ainulindale Exflation\sessions\session-plan\session-87-plan-w1a.md`, `C:\sandbox\Ainulindale Exflation\sessions\session-plan\session-87-plan-w1b.md`
**Verdict file cross-checked**: `C:\sandbox\Ainulindale Exflation\computations/_shared\s87_gate_verdicts.txt`
**Authoritative spec read**: `.claude/rules/Investigating-Workshops.md` (4-condition workshop definition + S82 calibration corpus)

**Wave summary**:
- **W1a** (7 gates: §W1a-1 .. §W1a-7) — strict count 4 PASS / 1 INFO / 2 FAIL. Gates landed §VII.U.6 (Mellin-Strip Level-3 anchor 8.07e-28), §VII.V (CM-1995 inadmissibility + Corollary A), §VII.U.7 (per-eval finiteness, INFO at deg-cap), §VII.U.1 (Mellin-Dirichlet bit-exact at L=12), §VII.W-2 (A0-R-protection ⟺ M2 biconditional FAIL on P4 backward direction), §VII.X.2-NECESSITY (M2-Λ_SA meta-aggregation FAIL on 2/6 anchor SHA availability), §VII.PROP.A + .B (P_MB/P_CM un-bundling + Lens vs Prescription, ρ_unbundled = 0 EXACT).
- **W1b** (6 gates: §W1b-1 .. §W1b-6, plus 7 in-session HK-1..HK-7 housekeeping closures) — strict count 0 PASS / 3 FAIL / 3 INFO. The headline finding is **W1b-3's bulk-Weyl falsification of d_eff=8** (Richardson L^{-3} clean at residual 2.5e-6 with L_max ∈ {10,12,14}; both Conv-A 10.122 and Conv-B 5.061 outside the [7.5, 8.5] band). HK-3 PASS-canonical pinned d_eff=8 to the bare-SU(3)-manifold sub-axis under Conv-B-slope; HK-5 PASS pinned the Jensen-deformed bulk slope to the closed-form 5/(1−τ_fold/(5π)) at |delta|=1.72e-5; HK-4 retroactively annotated 4 in-scope §VII.U/§VII.W d_spec=8 citation lines with `(convention pin pending S87-W1B-HK-3; scope: bulk-Weyl-falsified per W1b-3 — may survive at per-stratum / per-cluster sub-axis)`.

The wave-pair is structurally rich. **Three workshop seeds** survive the four-condition test of `.claude/rules/Investigating-Workshops.md`. The remainder of W1a/W1b substance feeds carry-forwards (route to `/rclab-plan`).

---

## Workshops

### Workshop 1 — d_eff anchor adjudication: bare-manifold (HK-3) vs Jensen-pole-shift (HK-5) vs registry-canonical-replacement (W1b-3 propagation)

**Tension**: W1b-3 (`S87-LMAX-WEYL-CONVERGENCE-SWEEP`, FAIL, audit_sha `40448d69279dad87…`, value=2.495e-6 Richardson residual) decisively falsifies d_eff=8 as a bulk-Weyl substrate-canonical identity at L→∞: Richardson L^{-3} extrapolation clean (residuals 2.5e-6 / 1.2e-6 / 1.0e+04 across d_eff Conv-A / d_eff Conv-B / PV residue), with `slope_∞ = 5.061193` matching W1b-HK-5's closed-form `5/(1−τ_fold/(5π))` at |delta|=1.72e-5 (PASS at 4 OOM below the 1e-3 threshold). Three structurally inequivalent readings of the FAIL coexist in the WP at session close, each with its own canonical-constants promotion path:

- **Reading A (HK-3, gen-physicist solo PASS-canonical)**: d_eff=8 IS substrate-faithful but only on the **bare-SU(3)-manifold-dim sub-axis under Conv-B-slope** (Lie-algebra cardinality of su(3) generators). The pin `D_EFF_CANONICAL_CONVENTION = "Conv-B-slope-on-bare-SU(3)-manifold-dim"` was added to `canonical_constants.py` line 768. Under this reading, the s28c "d_s = 8" claim survives, but it is logically prior to Jensen deformation; the substrate-IS observable is the Jensen-deformed value, NOT the bare value.

- **Reading B (HK-5, gen-physicist solo PASS at |delta|=1.72e-5)**: The substrate's actual bulk-Weyl exponent IS `5/(1−τ_fold/(5π)) = 5.0612` (Conv-B) / `10/(1−τ_fold/(5π)) = 10.122` (Conv-A) — a Connes-Mellin pole-shift on the bare value of 5 (NOT 8). HK-5 promoted `BULK_WEYL_EXPONENT_CONV_A_FW`, `BULK_WEYL_EXPONENT_CONV_B_FW`, `_L14` measured variants to `canonical_constants.py`. Under this reading, the bare manifold's slope is **5**, not **8**; the "10" in Conv-A is `2 · 5`, and the geometric series is on 5/(1−τ/(5π)), making the τ=0 baseline `slope = 5`, not the Lie-algebra count 8. The HK-5 substitution chain (WP §1395-1402) writes: `slope_∞_A = 10 / (1 − τ_fold/(5π))` with the "10" baseline as the substrate-counting dimension at the SU(3) Casimir-eigenvalue scaffold; the HK-3 "8" baseline as Lie-algebra cardinality.

- **Reading C (W1b-3 propagation, HK-4 retroactive annotation, 4 in-scope §VII.U/§VII.W lines)**: d_eff=8 should be DROPPED as substrate-canonical wherever cited, with the convention-pin sentinel propagated as a permanent marker until S88-VII-U-VII-W-CONVENTION-AUDIT lands. `regime_verdict=VALID` on W1b-3 means "the FAIL is decisive, not a finite-L truncation artifact" — the registry citations cannot be rescued by L=15+ extension.

**Concrete numeric divergence under the three readings**: for the same Richardson L^{-3} fit at L_max ∈ {10, 12, 14}, the substrate's "d_eff" headline value pinnable to `canonical_constants.py` is one of {8 (HK-3 bare), 5.061 (HK-5 Jensen Conv-B), 10.122 (HK-5 Jensen Conv-A), DROPPED (Reading C)} — four mutually exclusive canonical pins on a single substrate-IS observable.

The HK-3 vs HK-5 split is genuine ledger-dissonance: HK-3 says the substrate's d_eff baseline = 8 (Lie-algebra count), HK-5 says the substrate's d_eff baseline = 5 (Casimir-counting-dim / Conv-B-on-D-spectrum-pre-Jensen) before pole-shifting to 5.061. Only one can be the canonical bare-manifold baseline; the other must be a per-stratum or KO-modulus sub-axis. HK-5's "10" Conv-A baseline is not derived from any first-principles substitution chain in the WP — it is asserted at line 1395 ("the substrate-counting dimension for D's spectrum at the SU(3) Casimir-eigenvalue scaffold"), without a closed-form derivation tying it to either the Casimir spectrum or the Lie-algebra count. HK-3 names this gap and pins `8` to the bare manifold; HK-5 asserts `10` for the same object pre-Jensen. The two cannot both be the substrate-canonical pre-Jensen Weyl exponent.

**Agents**: connes (NCG-axiomatic; primary M_n(C) ⊃ A_F structure of A_K = C ⊕ H ⊕ M_3(C) on D_can = M_Lie; can adjudicate whether "10" or "8" is the canonical bare-Weyl exponent on the bare SU(3) Lie-group spectral triple) + lizzi (spectral-functional; primary regulator-class classification + Mellin-cone substrate-distance counting at d=4 vs d=8 vs d=10; can adjudicate whether the bulk-Weyl exponent corresponds to the substrate-distance-1 pole structure that §VII.U Mellin-Dirichlet identity already pins).

**Adjudication question**:
(a) Is the substrate's bare-Weyl exponent (pre-Jensen, Conv-B) equal to **8** (HK-3, Lie-algebra count of su(3) generators) or **5** (HK-5, half of Conv-A's "10" Casimir-counting baseline)? Show the substitution chain on the bare D_can = M_Lie eigenvalue counting function at L→∞, NOT a polyfit at L_MAX=5 with tolerance 2.0 (s28c's loose-numerical-fit reading) and NOT an unjustified assertion. The answer determines which of `D_EFF_CANONICAL_CONVENTION` (HK-3 pin) or `BULK_WEYL_EXPONENT_*_FW` (HK-5 pins) is the durable canonical entry; the other becomes a per-sub-axis or per-stratum derived value.
(b) Does the HK-5 Connes-Mellin pole-shift form `1/(1−τ/(5π))` admit a derivation from substrate first principles (Connes-Moscovici 1995 dimension-spectrum residue at the substrate-distance-1 pole), or is it a 4-family closed-form fit selected by best-residual on the L=10/12/14 trajectory? HK-5's WP §1397 calls the prefactor "the Connes residue at the substrate-distance pole, with the `5` matching the half-rank of the K-graded SU(3) spectral triple" but does not cite a derivation. If the form is fit-selected rather than derivation-pinned, the HK-5 PASS at |delta|=1.72e-5 is a 4-family overfit on 3 data points (4 candidate families, 18 candidates per WP §1404; only one needed to land at |delta|<1e-3 by chance), and the canonical pin is provisional.
(c) Under the §VII.U.6 Mellin-Strip Level-3 anchor (W1a-1 PASS at empirical 8.07e-28, algebraic envelope `L^{-α}` at α≥4 per d=4; WP §131 substrate framing names "the d_spec=8 NCG cone apex sits at Re(s)=4, deep inside Zubarev's strip"), does a bulk-Weyl exponent of 5.061 or 10.122 (NOT 8) preserve the §VII.U.6 cohomology-class identity (Level 1, regulator-invariant), the algebraic envelope (Level 2, L^{-α} at α≥4), and the empirical anchor (Level 3, 8.07e-28)? The Level-2 envelope assumes d_spec=8; if d_spec is now substrate-canonical at a different value, the envelope changes and the §VII.U.6 entry's three-level ladder must be re-validated under cross-pillar-bridge-anatomy.md §"Registry-PASS criterion".
(d) Adjudicate Reading C (drop d_eff=8 from §VII.U / §VII.W with HK-4's permanent annotation): is the HK-4 sentinel `(convention pin pending S87-W1B-HK-3; scope: bulk-Weyl-falsified per W1b-3 — may survive at per-stratum / per-cluster sub-axis)` a sufficient discharge of the falsification, or does the §VII.U.6 entry need a structural revision (drop the d_spec=8 NCG cone apex framing; re-pin to Conv-B `slope=5.061` baseline; or both)?

**Rounds**: 3 (genuine adversarial review — three structurally-distinct competing pins on one canonical entry; closed-form derivation of the HK-5 prefactor 1/(5π) is unsourced in the WP; §VII.U Level-2 envelope dependence on d_spec is registry-level)

**Output**: `permanent-results-registry.md` §VII.U.6 strengthening sub-block AND/OR new §VII.{Y}-D-EFF-CONVENTION-DISAMBIGUATION rule entry pinning **the canonical pre-Jensen bare-Weyl exponent on D_can = M_Lie** with full substitution chain (or registering the open question if neither agent's reading produces a closed-form derivation). Concrete deliverables: (i) one verdict on which of {HK-3 "8", HK-5 "10"-baseline-then-shift-to-10.122, Reading C "drop"} is the canonical entry; (ii) explicit re-validation of §VII.U.6 Level-2 envelope under the surviving d_eff value; (iii) a structural-confidence-ladder annotation on `BULK_WEYL_EXPONENT_*_FW` pins (currently lack the 3-level ladder per cross-pillar-bridge-anatomy.md). Pre-registered numerical falsifier: connes side derives bare-D_can Conv-B slope from first principles and reports the value to 3 sig figs; lizzi side derives the same quantity from the §VII.U.6 substrate-distance-1 dimensional weight at d=4 and reports to 3 sig figs; PASS-converge if the two values match within ±0.01; otherwise the registry entry pins the disagreement explicitly and routes to S88+ third-agent dispatch.

---

### Workshop 2 — A0-R-protection ⟺ M2 biconditional sufficiency: kernel-degenerate counterexample (P4) and richer A_F escape paths

**Tension**: W1a-5 (`S87-A0-R-PROTECTION-FAILURE-IS-M2-AXIOM-FAILURE-LANDING`, FAIL, audit_sha `87f81b3c18c11c5c…`) lands the cross-program biconditional at registry §VII.W-2 with composite FAIL because the P4 perturbation (D ⊕ rank-2 nilpotent N with N²=0) breaks the BACKWARD direction: K_max = 2.000e+00 (M2 fails — `[[N, diag(a)], diag(b)] ≠ 0` from the off-diagonal nilpotent block) BUT R_protection = 2.0000 (no breakdown — the nilpotent block has eigenvalue 0, excluded from the a_0^ζ count by zeta-regulator analytic continuation). The WP cites the asymmetry as REGIME-CONDITIONAL: holds when M2 violation perturbs non-zero eigenvalues (P3); fails when M2 violation lives in the kernel of D (P4). Two structural readings:

- **Reading A (connes-NCG, embodied in the WP P4 counterexample interpretation lines 409-411)**: The biconditional is genuinely BROKEN. The kernel-degenerate escape via nilpotent extension is a structural feature of zeta-regularization on the FULL M_n(C) algebra; richer A_F's (M_2(C) is the smallest non-abelian) may PRECLUDE the escape but only by restricting the algebra such that the kernel-perturbation is off-table. Under this reading, §VII.W-2 should retain the FAIL verdict with explicit "FORWARD-DIRECTION-ONLY" tag; downstream gates citing §VII.W-2 must use only the implication `R-protection breakdown ⇒ M2 fails`, never the reverse.

- **Reading B (richer-A_F escape, embodied in the synthesis carry-forward `S88-A0-M2-BICONDITIONAL-RICHER-A_F-TOY` and the volovik 3He-B inheritance tradition)**: The P4 counterexample is a 2-eigenvalue toy artifact; the actual substrate's A_K = C ⊕ H ⊕ M_3(C) precludes nilpotent-extension escapes by the (Δ_B/Δ_A)^p cancellation theorem (S86 W-5 DONE-5; substrate kernel structure in BdG sector is rank-2 with cocycles φ_67, φ_88 carrying STRUCTURAL norms). Under this reading, the biconditional is RECOVERED on the substrate's actual A_F, and §VII.W-2 should be re-pinned at `STAGE-1-CANDIDATE` per `joint-theorem-promotion.md` 4-stage pathway pending an S88 dispatch on M_2(C) toy.

**The structural divergence is concrete and adjudicable**:
- Forward direction (CC1 in WP): R-protection breakdown ⇒ ω_R off-diagonal ⇒ eigenvectors tilt away from A_F basis ⇒ ∃a∈A_F with [D,a]≠0 ⇒ ∃b with [[D,a],b]≠0 ⇒ M2 fails. Verified on P3: K_max = 1.414e-01 > 0 AND R_protection = 1.9950 < 2.0000.
- Backward direction (CC2 in WP): "[[D,a],b] ≠ 0 ⇒ R-protection breakdown" REFUTED on P4. Connes reads the P4 counterexample as structural; volovik (via the substrate-side BdG structure) reads it as a toy artifact whose substrate analog is precluded by the BDI ↔ DIII Altland-Zirnbauer compatibility theorem.

**Cross-pillar leverage**: this question DIRECTLY couples to W2-1 (`S87-LAB-3HE-B-ALPHA-S-EQUIVALENT`, PASS at registry rows #45 + #46 of `falsifier-master-inventory.md`, paper draft `papers/s87-3he-b-alpha-s-equivalent.md`) — the 3He-B inheritance morphism χ : C ⊕ H ⊕ M_3(C) → M_2(C) sends M_3(C) → 0 with rank-2 ker(ι_*) carrying the φ_67, φ_88 cocycles. If Reading B is correct, the biconditional survives on M_2(C) and the W2-1 inheritance falsifier protocol gains structural bedrock; if Reading A is correct, the kernel-degenerate escape is a generic feature of NCG axiom 2 that propagates through χ to 3He-B, and the W2-1 ratio prediction (||φ_67||/||φ_88||=7.3250 ± 0.1%) acquires a structural caveat that may shift its tolerance band.

**Agents**: connes (NCG-axiomatic side; primary on §VII.W-2 FAIL verdict; sole adjudicator of whether kernel-degenerate escape via nilpotent extension is generic to all algebras containing matrix sub-blocks or specific to free M_n(C) actions) + volovik (substrate-IS / 3He-B inheritance side; primary on (Δ_B/Δ_A)^p cancellation theorem and W-5 cocycle norm framework; can adjudicate whether substrate's actual A_K precludes the P4 escape via algebraic structure rather than convention).

**Adjudication question**:
(a) On A_F = M_2(C) (smallest non-abelian, structurally precludes nilpotent-extension escape iff the algebra acts faithfully on the kernel of D): does the biconditional `R-protection breakdown ⟺ M2 fails` hold or fail? Show the computation analogous to W1a-5's 4-perturbation panel but on the M_2(C) toy.
(b) Is the P4 counterexample STRUCTURAL (intrinsic to a_0^ζ regulator's analytic continuation killing kernel modes) or REGIME-CONDITIONAL (specific to the rank-2 toy and absent on the substrate's A_K = C ⊕ H ⊕ M_3(C))? The WP CC2 calls it "REGIME-CONDITIONAL" but does not derive a structural theorem.
(c) Does the substrate's BDI ↔ DIII inheritance morphism χ from S86 W-5 propagate the kernel-degenerate escape from the substrate's A_K through to the lab's M_2(C) BdG sector, OR does the cancellation theorem (S86 W-5 DONE-5) eliminate the escape on the lab side? If the latter, §VII.W-2 BACKWARD direction is recovered on the lab side even if it fails on the substrate side, and the biconditional is dimension-conditional rather than absolute.
(d) Re-classify §VII.W-2: keep at composite FAIL with FORWARD-ONLY tag (Reading A), promote to STAGE-1-CANDIDATE pending M_2(C) toy verification (Reading B), or split into §VII.W-2-FORWARD (PASS) and §VII.W-2-BACKWARD (deferred-conditional)?

**Rounds**: 3 (genuine cross-program tension; verdict has direct propagation to §VII.W-2 registry classification + W2-1 falsifier protocol's structural bedrock; volovik and connes occupy genuinely-different authority domains here).

**Output**: §VII.W-2 registry edit (one of: maintain FAIL with FORWARD-ONLY caveat / promote to STAGE-1-CANDIDATE / split into FORWARD + BACKWARD sub-rows). If split: explicit cross-link from §VII.W-2-FORWARD to W2-1 falsifier protocol (since FORWARD direction is what 3He-B inheritance falsifier rests on). Concrete pre-registered numerical falsifier: connes + volovik jointly run an M_2(C) 4-perturbation panel analogous to W1a-5; PASS-recover-biconditional iff both directions hold across all 4 perturbations; FAIL-broken iff backward direction fails on any perturbation; INFO-restricted iff backward holds on the substrate's actual rank-2 ker(ι_*) but fails on generic algebra-extensions.

---

### Workshop 3 — Connes-distance functional family orthogonality: CLASS-γ closure scope vs sub-algebra restriction track

**Tension**: W1b-6 (`S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY-CONJECTURE`, INFO/CLASS-γ, audit_sha `b3652c276acec8e1…`, value=0.9800418) closes the conjecture that Connes distance admits a closed-form identity in {λ_n} alone. The WP's structural reading at §2173-2178: "§VII.U.1 Mellin-Dirichlet identity is STRUCTURALLY SPECIFIC to spectral functionals of the form `F({λ_n}) = Σ_k m_k · g(λ_k)` (with g a fixed function); it is NOT generic to all substrate algebraic functionals. The Connes distance is a different functional class." The R-sweep diagnostic at §2138-2147 demonstrates `d_C(R) ≈ 0.9·R` linearly across 3 OOM in R, identifying the divergence as structural (commutant of D contains f(D²) for any polynomial f, leaving algebra-element norm unbounded under Frobenius cap).

Two structurally-distinct readings of the closure scope:

- **Reading A (gen-physicist's WP §2173-2178; "structural orthogonality")**: The two functional families (algebra-INVARIANT spectral moments + algebra-DEPENDENT state-pair commutator norms) are STRUCTURALLY ORTHOGONAL on every finite spectral triple. The CLASS-γ closure is universal — it would persist on any sub-algebra restriction (M_n(C) → A_F = C ⊕ H ⊕ M_3(C)) because the regulator-divergence is intrinsic to the SDP structure on the full algebra, not to the algebra's specific sub-structure. Under this reading, §VII.{letter} stays empty for Connes-distance identities; the orthogonality is itself a structural finding to register at §VII.{Z}-FUNCTIONAL-FAMILY-ORTHOGONALITY (currently NO new entry per W1b synthesis line 2239).

- **Reading B (W1b-6 carry-forward `S88-CONNES-DISTANCE-SUBALGEBRA-RESTRICTION-CONJECTURE`; "different conjecture, different algebra")**: The CLASS-γ closure is SCOPE-LIMITED to the FULL `M_n(C)` algebra. Restricting A_loc to A_F = C ⊕ H ⊕ M_3(C) gives a finite, well-defined Connes distance because A_F has finite K_0 and the f(D²)-commutant escape may be precluded by direct-sum block structure. Under this reading, the conjecture is OPEN at the substrate's actual algebra; the WP's "structural orthogonality" is over-extension from the FULL-algebra closure to the sub-algebra case.

**The divergence has direct registry implications**:
- Under Reading A: §VII.{letter} empty for Connes-distance; the functional-family orthogonality theorem itself becomes a candidate registry entry (analogous to §VII.AF.1 cross-pillar bridge anatomy template).
- Under Reading B: §VII.{letter} reserved for an S88 sub-algebra-restriction conjecture; the W1b-6 CLASS-γ verdict is a precursor finding, not a structural closure of the broader conjecture family.

The W1b-6 spawn-prompt explicitly enumerated the sub-algebra-restriction track as "S88+ optional" and tagged it "different conjecture, different algebra" — but this is a single-agent disposition, not a multi-agent adjudication. The structural orthogonality claim is load-bearing for downstream gates that cite §VII.U.1 as substrate-canonical because it determines whether other algebra-dependent observables (entropy, information geometry, commutator-norm spectral statistics) can ever be Mellin-Dirichlet-identifiable.

**Cross-pillar leverage**: connes-distance is the substrate's STATE-SPACE METRIC; if Reading B holds, then on A_K = C ⊕ H ⊕ M_3(C) the substrate carries a finite, well-defined state-space metric admitting algebraic identities — this is directly relevant to W-3 (Path-H/Path-C multi-valued classification, CF-20) and to the substrate-IS observables in W2-1 inheritance falsifier protocol (which uses cocycle norms on rank-2 ker(ι_*) — those norms ARE state-pair commutator-derived quantities).

**Agents**: connes (NCG-axiomatic; primary on the K_0 structure of A_F and on the f(D²)-commutant argument's algebra-dependence) + lizzi (spectral-functional; primary on regulator-class classification — specifically whether SDP regulator-divergence is intrinsic to all algebra-dependent state-pair functionals or specific to algebras containing M_n(C) infinite-rank embeddings).

**Adjudication question**:
(a) On A_F = C ⊕ H ⊕ M_3(C) (the substrate's actual finite algebra, NOT the FULL M_n(C)), does the SDP regulator-divergence persist? Specifically, does the f(D²)-commutant escape that drove the FULL-algebra divergence at WP §2150-2153 still apply when A_loc is restricted to the direct sum of the three blocks?
(b) Is "structural orthogonality between algebra-INVARIANT and algebra-DEPENDENT functional families" (Reading A) a theorem provable from NCG axioms, OR is it a conjecture with FULL-algebra evidence (W1b-6 verdict) but not generalized to sub-algebras (Reading B's open territory)?
(c) Does §VII.U.1 Mellin-Dirichlet identity admit a sub-algebra restriction analog at substrate's A_K (rather than full M_n(C))? The W1a-4 PASS landed bit-exact on the FULL spectrum at L=12 — but that test summed over `m_k` with no algebra-element decomposition. If A_F constraints on m_k change the Dirichlet sum's convergence in a way detectable by regulator class, the §VII.U.1 entry's "STRUCTURALLY SPECIFIC" claim acquires a sub-algebra dependence.
(d) Re-classify W1b-6 verdict: maintain CLASS-γ at FULL-algebra scope only (Reading B-compatible) or extend the closure to all algebra-dependent functional families on all finite spectral triples (Reading A); register the answer at a new §VII.{letter}-FUNCTIONAL-FAMILY-ORTHOGONALITY slot OR reserve the slot for Reading B's pending S88 conjecture.

**Rounds**: 2 (routine adjudication — both readings are structurally well-defined and the difference is on closure scope; not a deep cross-program tension)

**Output**: One of: (i) §VII.{letter}-FUNCTIONAL-FAMILY-ORTHOGONALITY new registry entry establishing Reading A as a structural theorem (with proof sketch from f(D²)-commutant argument generalized to all finite spectral triples); (ii) §VII.{letter}-RESERVED-FOR-CONNES-DISTANCE-SUBALGEBRA-CONJECTURE pending S88 dispatch (Reading B); (iii) §VII.U.1 strengthening annotation pinning the algebra-INVARIANT specificity of the Mellin-Dirichlet identity. Concrete pre-registered numerical falsifier: connes + lizzi jointly evaluate Connes distance on A_loc = A_F = C ⊕ H ⊕ M_3(C) at the same 3 canonical state-pairs as W1b-6 (vacuum/n=0; B1 acoustic min/max; Cartan α_1/α_2) at L_max=12; PASS-Reading-A iff regulator-divergence persists with d_C(R) ≈ c·R linearly over R-sweep; PASS-Reading-B iff d_C is finite at all R and at least one of the 4 candidate forms (C2/C3/C4 from W1b-6) achieves residual < 1e-3 at any state pair.

---

## Carry-forwards (route to /rclab-plan, NOT this schedule)

These are queued computation follow-ups, solo computes, single-agent verifications, and registry-write maintenance — pre-existing in the W1a/W1b synthesis sections and explicit `Carry-forward to S88` blocks. Each has a 4-field spec already in the WP; the consolidator should NOT label them workshops.

- **`S88-A0-M2-BICONDITIONAL-RICHER-A_F-TOY`** (W1a-5 carry-forward; line 699). Solo connes compute; restricted toy on M_2(C); pre-registered band on biconditional 4-of-4 panel. INPUT to Workshop 2 (above), but as a queue item it is a solo-compute follow-up, NOT itself a workshop. **NOTE: if Workshop 2 fires, this carry-forward is its compute kernel.**
- **`S88-LAMBDA-SA-S46-A2-SPLIT-SUCCESSOR-EMISSION`** through **`S88-LAMBDA-SA-C9-S86-W1-RATIO-EMISSION`** (W1a-6 anchors 1, 2, 3, 4, 6; lines 700-704). Five computation successor-emission gates re-pinning historical gates' SHAs in modern post-S81 verdict-line format. Pure SHA-emission housekeeping; no adjudication possible.
- **`S88-VII-X-2-NECESSITY-PROMOTE-STAGE-3`** (W1a-6; line 705). Mechanical promotion gate after the 5 successor-emissions land. No tension.
- **`S88-MELLIN-CONE-NO-GO-FULL-LMAX10-RETEST`** (W1a-2; line 706). Re-run W1a-2 4-eigenvalue toy at full L_max=10 D_K^2 (155,984 eigvals). Solo compute; pre-registered band.
- **`S88-CM-1995-CUTOFF-SQRT-ATLAS-CROSS-CHECK`** (W1a-2; line 707). Cross-check Corollary A against W-8 cutoff_sqrt atlas; classify each entry PASS/FAIL. Solo registry sweep.
- **`S88-PV-SCHEME-MPMATH-MELLIN-DIRICHLET-VERIFY`** (W1b-1 → CLOSED IN-SESSION by HK-1, PASS at 5.766e-49). Already closed; remove from forward queue.
- **`S88-WINDOWED-PV-SUBTRACTION-AS-SD-REFINEMENT`** (W1b-1 → CLOSED IN-SESSION by HK-2, FAIL across 3 schemes). Already closed; remove from forward queue.
- **`S88-WINDOWED-PV-AT-ALTERNATIVE-MASS-SCALES`** (W1b-1 HK-2 carry-forward; line 972). Re-evaluate 3 PV schemes (A/B/C) at M ∈ {⟨λ⟩, λ_max, √⟨λ²⟩, M_KK·α} for α ∈ {0.1, 0.5, 2, 10}. Solo compute; pre-registered band on ratio_PS_SM at any (scheme, M) pair.
- **`S88-WINDOWED-PV-DEEPER-POLE-AT-S4`** (W1b-1 HK-2 carry-forward; line 973). Extend PV exploration to substrate-distance-2 pole at s=4. Solo compute.
- **`S88-PV-CONTINUUM-POLE-RECONCILIATION`** (W1b-3 carry-forward 3 → CLOSED IN-SESSION by HK-5, PASS). Already closed; remove.
- **`S88-VII-U-VII-W-CONVENTION-AUDIT`** (W1b-3 carry-forward 2; line 1339). Replace HK-4's pending-pin sentinels with definitive convention or drop d_eff=8 anchor. **NOTE: if Workshop 1 fires, its output supersedes this audit; if Workshop 1 does not fire, this remains a registry sweep carry-forward.**
- **`S88-RICHARDSON-FORM-CANONICALIZATION`** (W1b-3 carry-forward 4 → CLOSED IN-SESSION by HK-6, PASS). Already closed; `RICHARDSON_3PT_CANONICAL_FORM` pinned to canonical_constants.py.
- **`S88-D-EFF-ANCHOR-CONVENTION-AUDIT`** (W1b-3 carry-forward 1 → CLOSED IN-SESSION by HK-3, PASS-canonical). Already closed; `D_EFF_CANONICAL_CONVENTION` pinned. **NOTE: if Workshop 1 fires, the HK-3 closure is itself contested and the carry-forward re-opens.**
- **`S88-SD-MASS-RATIO-PAIRED-SLOT-IDENTITY-VERIFY`** (W1b-4 promotion path → CLOSED IN-SESSION by HK-7, PASS-CLASS-B-UNIQUE-AT-L14). Already closed for L=14 disambiguation half.
- **`S88-A-N-FW-CANONICALIZATION`** (W1b-4 HK-7 surface; line 1915). Promote `a_0_FW` and `a_2_FW` to canonical_constants.py per the 3-step canonical write-order rule. Pure registry-write; no adjudication.
- **`S88-PS-AF-L12-RECALIBRATION`** (W1b-5 carry-forward; line 2071). Re-run PS A_F diagnostic at L=12; INFO-band scan only. Solo compute.
- **`S88-CONNES-DISTANCE-SUBALGEBRA-RESTRICTION-CONJECTURE`** (W1b-6 carry-forward; line 2185). Restrict A_loc from M_n(C) to A_F = C ⊕ H ⊕ M_3(C). **NOTE: this is the compute kernel of Workshop 3; if Workshop 3 fires, this becomes its computation; if not, it remains a solo follow-up.**

---

## Wave-by-wave digest (consolidator background)

### W1a (lines 7-720; 7 gates + synthesis)

Theme: REGISTRY-LANDING + algebraic identity verification on cached spectra; 7 carry-forwards CF-1..CF-7 from S86 W-1.

| Gate | ID | Verdict (composite) | Standout finding |
|:-----|:---|:--------------------|:-----------------|
| W1a-1 | `S87-W1B-T5-LANDING` | PASS (5/5 IS-not-IN + 3/3 level markers; 4-row Mellin-Strip identity at machine ε) | §VII.U.6 strengthening landed at 8.07e-28 Level-3 anchor |
| W1a-2 | `S87-MELLIN-CONE-NO-GO-THEOREM-LANDING` | PASS (Class-8.2 PRU surface noted; structural verdict via abs_div_356 = 15.0000 = 2^4 − 1 bit-exact) | §VII.V CM-1995 inadmissibility + §VII.V.A WEYL-NON-ASYMP-F_4-MB-NO-GO Corollary A |
| W1a-3 | `S87-W3-PER-EVAL-FINITENESS-PRE-REG` | INFO (rho_fit_residual 1.19e-04 in [1e-6, 1e-3] band; 2-iter audit trail: bug fix preserved both lines) | §VII.U.7 PASS-evidence-on-disk for per-eval finiteness floor |
| W1a-4 | `S87-FINITE-SPECTRUM-MELLIN-DIRICHLET-IDENTITY-LANDING` | PASS (rel_diff = 0.0e+00 bit-exact at s ∈ {3,4,5} on full L=12 cache) | §VII.U.1 strengthened to L=12; cache integrity confirmed |
| W1a-5 | `S87-A0-R-PROTECTION-FAILURE-IS-M2-AXIOM-FAILURE-LANDING` | FAIL (3/4 perturbations; P4 backward direction broken) | §VII.W-2 registered with FAIL verdict; **FEEDS WORKSHOP 2** |
| W1a-6 | `S87-M2-STRUCTURAL-SOURCE-FOR-LAMBDA-SA-FINITE-L-RESIDUAL-LANDING` | FAIL (necessity 6/6 OK but only 2/6 anchor SHAs full-64-char available) | §VII.X.2-NECESSITY STAGE-1-CANDIDATE; SOURCE-RECON Class-(c) PIN-DRIFT-FROM-STALE-SOURCE diagnosis |
| W1a-7 | `S87-VII-PROP-LANDING` (.A + .B) | PASS × 2 (ρ_unbundled = 0 EXACT on un-bundled 4-regulator atlas; ρ_naive = 0.7071) | §VII.PROP.A (P_MB/P_CM un-bundling) + §VII.PROP.B (Lens vs Prescription) orthogonality at THEOREM tolerance |

**Wave decision point (plan §974-986)**: literal `≤5-of-7 PASS → PAUSE` clause activated by strict count 4 PASS. Both FAILs are SCIENCE corridor closures with seeded carry-forwards; the INFO is structurally honest. User pragmatic-continue path was implicit (W1b proceeded).

### W1b (lines 722-2270; 6 gates + 7 housekeeping HK-1..HK-7 + synthesis)

Theme: PV-finite-L vs continuum-SD reconciliation + d_eff anchor verification + 4-class paired-slot interpretation + PS A_F diagnostic + Connes-distance conjecture audit.

| Gate | ID | Verdict (composite) | Standout finding |
|:-----|:---|:--------------------|:-----------------|
| W1b-1 | `S87-PV-SUBTRACTION-RECALIBRATION` | FAIL (sign_obs = −1, sign_pred = +1; substitution chain INVERTED plan's qualitative narrative) | Canonical PV is SUBTRACTION not additive UV restoration; PV − SD = −1.697e+06 (NOT a small-positive refinement) |
| W1b-2 | `S87-D-EFF-ANCHOR-VERIFICATION` | FAIL (max_deviation 2.29 × 4.57 over 0.50 INFO ceiling; 2/3 ordering inversions) | d_eff_global = 10.07 at L=12; per-stratum spread 0.42; structurally NOT noise around 8 |
| W1b-3 | `S87-LMAX-WEYL-CONVERGENCE-SWEEP` | FAIL (Richardson L^{-3} clean; d_eff_∞ Conv-A 10.122 / Conv-B 5.061 outside [7.5, 8.5]) | **Bulk d_eff=8 anchor FALSIFIED. FEEDS WORKSHOP 1.** 2 verdict-line iterations (Richardson form refinement); both preserved |
| W1b-4 | `S87-PAIRED-SLOT-RATIO-INTERPRETATION` | INFO/CLASS-B-NEAR-UNIQUE (residual 3.45e-05 PASS; A and C in [1e-2, 1e-1] gap) | Promoted to CLASS-B-UNIQUE-AT-L14 by HK-7 (residual 6.82e-07; CLASS-A widens to 13.64) |
| W1b-5 | `S87-PS-AF-RECALIBRATION-DIAGNOSTIC` | INFO (ratio_PS/SM = 1.0050; 0.50% upward shift; 6/6 Connes-Chamseddine axioms PASS) | PS A_F structurally admissible at L=10; non-decisive on n=0 growth at controlled diagnostic |
| W1b-6 | `S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY-CONJECTURE` | INFO/CLASS-γ (best_residual 0.98 ≫ 1e-3; 5 verdict-line iterations preserved; SDP regulator-divergence c·R linear over 3 OOM) | Conjecture CLOSED at FULL M_n(C). **FEEDS WORKSHOP 3.** Sub-algebra restriction track open |

**Housekeeping closures (HK-1..HK-7, lines 855-1924)**: 7 in-session structural follow-ups, 6 PASS + 1 FAIL across alternative-PV-scheme exploration / mpmath identity verification / d_eff convention audit / §VII.U-§VII.W convention recite / Jensen pole-shift closed form / Richardson form canonicalization / paired-slot L=14 disambiguation. Major canonical-constants promotions: `D_EFF_CANONICAL_CONVENTION`, `BULK_WEYL_EXPONENT_CONV_{A,B}_FW`, `BULK_WEYL_EXPONENT_CONV_{A,B}_L14`, `RICHARDSON_3PT_CANONICAL_FORM`. **The HK-3 vs HK-5 split is the heart of Workshop 1 above.**

### Cross-wave structural genealogy

- W1a-1 §VII.U.6 Mellin-Strip Level-3 anchor at 8.07e-28 cites "d_spec=8 NCG cone apex" in substrate framing → annotated by HK-4 with pending-pin sentinel after W1b-3 falsifies bulk d_eff=8. Workshop 1 adjudicates whether the §VII.U.6 entry's three-level ladder survives under the surviving d_eff value.
- W1a-5 §VII.W-2 biconditional FAIL on backward direction couples directly to W2-1 (3He-B inheritance falsifier; outside my range, but the registry coupling is internal to W1a). Workshop 2 adjudicates the kernel-degenerate escape's structural status.
- W1a-4 §VII.U.1 Mellin-Dirichlet identity at L=12 bit-exact (PASS) is the algebra-INVARIANT functional family's substrate-canonical exemplar; W1b-6 CLASS-γ closes the algebra-DEPENDENT counterpart on FULL M_n(C). Workshop 3 adjudicates whether the orthogonality between functional families is theorem or scope-limited closure.

### Honest count

3 workshops surface from the 13 gate-IDs in this chunk's range. The wave-pair has dense substantive content (10,058-line WP partition includes 2,265 lines for waves 1a + 1b alone) and 7 in-session housekeeping closures, but most of the substance closes in-session via solo compute or feeds computation carry-forwards listed above. The 3 workshops above represent genuine ledger-dissonance with cross-pillar bridge implications (Workshop 1: registry §VII.U / §VII.W coupling), substrate-physics scope contests (Workshop 2: §VII.W-2 BACKWARD direction structural status), and structural-classification scope debates (Workshop 3: algebra-INVARIANT vs algebra-DEPENDENT functional family orthogonality). All 3 satisfy the four-condition workshop test (TWO+ agents with COMPETING perspectives / genuine LEDGER-DISSONANCE / multi-round structure / STRUCTURAL VERDICT output) per `.claude/rules/Investigating-Workshops.md`.
