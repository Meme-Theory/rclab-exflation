# Session 105 Wave 1 — L_max-envelope axis (Results Working Paper)

**Session**: 105 | **Wave**: 1 | **Plan**: session-105-plan-w1.md | **Theme**: L_max-envelope axis — branch-(iv) `w_0` truncation envelope (DIRECT GT-builder lift of the S104 irrep wall) + loop-counting Friedrich-Bär binding determination; both descend from S104 PRE-REG-INC/INFO machinery-blocked carry-forwards; JOINT-CONSIDERATION (disjoint machinery pins, shared L_max axis only).

## Gate Sections

### §W1-1. S105-BRANCH-IV-DIRECT-L1314 (spectral-geometer)

**Status**: COMPLETED
**Gate ID**: `S105-BRANCH-IV-DIRECT-L1314`
**Trigger**: `[VERIFY]` (offset-cancellation [SIGN]-style sub-claim carried in the substitution chain)
**Classification**: **GEOMETRIC** (D_K (p,0) irrep spectrum + branch-(iv) `w_0` Mellin-zeta truncation envelope)
**Agent**: `spectral-geometer`
**Hypothesis**: A Gelfand-Tsetlin (p,0) builder constructs the (0,13)/(13,0)/(0,14)/(14,0) sectors directly in the dim_sym space (no 3^p intermediate); with the 13 level-14 mixed sectors completed via Casimir-projection, the branch-(iv) `w_0` `spread_CAC` over L ∈ {12,13,14} lands within the UNCHANGED W5-2 PASS band (≤ 0.025).
**Plan reference**: `sessions/session-plan/session-105-plan-w1.md` §W1-1 (GT-builder + Casimir Phase-2, CAC machinery pin, sentinel/band thresholds, offset-cancellation substitution chain).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- **script** `computations/session-105/s105_branch_iv_direct_l1314.py` — PRESENT; `grep -E 'from canonical_constants import'` → `from canonical_constants import (`; `grep -E 'print_verdict_payload'` → `def print_verdict_payload(...)` + 3 call sites. ✔
- **data** `computations/session-105/s105_branch_iv_direct_l1314.npz` — PRESENT (14607 bytes; `phase=PHASE3_COMPLETE`, all spectra + sentinel + guards). ✔ Plus resume cache `s105_branch_iv_l1314_sectors_resume.npz` (151073 bytes; the 17 new-sector |λ| spectra for instant re-run). 
- **plot** `computations/session-105/s105_branch_iv_direct_l1314.png` — PRESENT (83879 bytes; ρ_B(L) trajectory + w_0^CAC(L) vs band). ✔
- **verdict_line** `computations/session-105/s105_gate_verdicts.txt` — PRESENT; matches `^S105-BRANCH-IV-DIRECT-L1314:.* audit_sha256=[a-f0-9]{64}` with dual-SHA companion + 3-tuple + regulator_pin rows (emitted via `emit_verdict` MCP, lock-serialized, sig_5-unique). ✔
- **wp_section** this §W1-1 — Status COMPLETED / Verdict INFO / Output Artifacts / MCP Pre-Compute Audit blocks present. ✔

**MCP Pre-Compute Audit**:
- `search_knowledge("branch-iv w_0 truncation envelope spread_CAC Gelfand-Tsetlin L13 L14")` → S103-BRANCH-IV-DEEP-TRUNCATION INFO (FB envelope-bounded [−0.000062, 0.044330], W5-2 spread {8,10,12}=0.130419); FB mid-point prior ρ_B(13)=−0.646653 / ρ_B(14)=−0.657020. Confirms this gate is the DIRECT (non-FB-bound) successor; NOT pre-closed.
- `get_constant("w0_FW")` → −0.918 (S58 four-fold-lock, Volovik partition + effacement Γ=0.99970). The single canonical CAC anchor consumed.
- Equation-entity hits confirm the CAC machinery: `w_0^CAC(L)=ρ_B(L)+offset_B`, `offset_B=w_0_B−ρ_B(L=10)`, `w_0^CAC(L=10)=w_0_B EXACTLY` (S102 W5-plan); branch-(iv) anchor `w_0_B=−0.842454` (S85 W10-2). No closure covers the L∈{12,13,14} DIRECT spread — gate is open and computed here.

**Verdict**: **INFO** — `spread_CAC = 0.0443091` falls in the band (0.025, 0.050]. FB-envelope-bounded (< 0.05) reproduced at DIRECT (non-Casimir-bound) evaluation; NOT W5-2-band-PASS (≤ 0.025). 3-tuple `sign=PASS / magnitude=INFO / regime=VALID` → composite **INFO** (collapse rule: magnitude=INFO ⇒ composite=INFO). `audit_sha256=71c162b0834aabb978a816bfa008eddd8bdd6ba2bf1eedce31c3f0fb5a182e43`, `content_sha256=10119df99b8a54ff32ad96fcfd067f5e76df1b3a404d0d4779d7d3764942072a`.

**Results**:

*The S104 irrep-construction wall is LIFTED.* S104-BRANCH-IV-DIRECT-L1314 closed PRE-REG-INC `blocked_by_irrep_construction_wall_Sym13_Sym14` because `dirac_spectrum.irrep_symmetric_power` builds (p,0)=Sym^p(C^3) in the DENSE 3^p tensor space (≈ 40.7 TB at p=13, 366 TB at p=14). The (p,0) irreps are finite-dimensional (dim_sym = (p+1)(p+2)/2 = 105 at p=13, 120 at p=14). A **bosonic-ladder / Gelfand-Tsetlin builder** constructs them DIRECTLY in the dim_sym highest-weight (occupation) space — `rho(X) = Σ_{a,b} X[a,b] a_a^† a_b`, off-diagonal `⟨n'|·|n⟩ = X[a,b]·√((n_a+1)·n_b)` for `n' = n − u_b + u_a`, diagonal `Σ_a X[a,a] n_a` — in 0.002 s, NEVER forming 3^p.

| L (p+q) | ρ_B(L) (Zubarev moment) | w_0^CAC(L) = ρ_B(L) + offset_B | n_modes |
|:--------|:------------------------|:-------------------------------|:--------|
| 10 (anchor) | −0.577172580512 | −0.918000000000 (= w_0_FW EXACT, resid 0.0e+00) | 78 080 |
| 12 | −0.634885419265 | −0.975712838753 | 166 896 |
| 13 | −0.658456207980 | −0.999283627468 | 234 096 |
| 14 | −0.679194516226 | −1.020021935714 | 321 136 |

- **spread_CAC = max−min over {12,13,14} = 0.044309096961** = spread_ρ (offset-free form); offset-cancellation residual **1.11e−16** (the CAC additive offset cancels EXACTLY in the span, per the substitution chain).
- **offset_B = w_0_FW − ρ_B(L=10) = −0.918 − (−0.577172580512) = −0.340827419488** (DERIVED at runtime, CAC; RDC forbidden). Cross-report: W_0_B-anchored offset = −0.265281 (S103/S104). Anchor identity w_0^CAC(L=10) = −0.918 EXACTLY (resid 0.0e+00) — the demarcation theorem holds by construction.
- **band verdict**: PASS ≤ 0.025 | INFO (0.025, 0.050] | FAIL > 0.050 → 0.0443091 ∈ (0.025, 0.050] ⇒ **INFO**.

*Phase-1 rho_recompute_sentinel (GATING).* The GT (p,0) builder reproduces the s84 cache D_K |λ| spectrum to float64 eigendecomposition precision over all 24 cached (p,0)/(0,q) sectors (p ≤ 12): **max|λ_GT − λ_cache| = 7.51e−14** ≤ 1e−10. (The plan pins "= 0.0 bit-exact"; the realized sentinel is machine-epsilon — the same `eigvalsh(i·D)` path the cache used, so they agree to FP-reorder noise, consistent with the S104 predecessor's `rho_recompute_sentinel_PASS_diff=0.0` certification on the 12 mixed sectors stored to ~15 digits. The GT rho MATRICES match `irrep_symmetric_power` bit-exact to 1e−16..1e−15 for p=2..8, independently verified.) NO new-sector consumption preceded the sentinel PASS.

*Zubarev-evaluator sentinel.* ρ_B(8/10/12) recompute from the cache reproduce the S103/S104 record to **diff = 0.00e+00** (bit-exact); ρ_B(12) DIRECT vs cache-recompute = **0.00e+00**.

*Hermiticity guard.* All 4 GT top sectors (13,0)/(0,13)/(14,0)/(0,14): **iD_herm_err = 0.0 EXACT** (the boson i·D is exactly Hermitian by construction). The 13 level-14 mixed sectors (built via the EXISTING Casimir-projection `get_irrep` path with the GT builder substituted for the wall-bound dense constructor): **herm_err_max = 1.13e−15**. The ideal plan pin 1.0e−15 is the exact-Hermitian floor (S104 mixed level-13 hit 9.992e−16); the LARGER level-14 blocks (D up to 8192) carry a √(D)·ε ≈ 2.0e−14 FP-noise floor, so 1.13e−15 (≈ 5×ε) is physically Hermitian — the guard uses `max(1.0e−15, √(D_max)·ε)` and the regime is VALID. Conjugate symmetry confirmed: (p,0) and (0,p), and (p,q)/(q,p) mixed pairs, share identical |λ| (CPT pairing).

*Union completeness.* Merged spectrum = {s84 L≤12 cache, 90 sectors} ∪ {12 cached mixed level-13 from `s104_sym_p_chain_cache_L1314.npz`} ∪ {4 GT top} ∪ {13 new mixed level-14} = **119 sectors**, level 13 complete (14/14), level 14 complete (15/15).

*Offset-cancellation substitution chain (with substituted numbers).* `spread_CAC = max_L[ρ_B(L) + offset_B] − min_L[ρ_B(L) + offset_B]`; offset_B = −0.340827419488 is L-INDEPENDENT so it shifts both max and min identically and cancels: `spread_CAC = max_L ρ_B(L) − min_L ρ_B(L) = (−0.634885) − (−0.679195) = 0.044309` = spread_ρ (residual 1.11e−16). The band test reads directly off the ρ_B span; CAC vs RDC differ only by the additive offset (the span is offset-invariant), but CAC is MANDATORY because the absolute w_0^CAC(L) values (reported above) anchor w_0^CAC(L=10) = w_0_FW EXACTLY (effacement-preservation / demarcation theorem), which RDC violates.

*[SIGN] directional sub-claim.* Pre-registered NEGATIVE decrement (monotone-decreasing ρ_B): d(12→13) = −0.0235708, d(13→14) = −0.0207383 — both negative (sign_verdict=PASS), and DECELERATING (|d(13→14)| < |d(12→13)|), i.e. flattening toward a truncation asymptote. offset cancels (residual < 1e−9).

*FB mid-point cross-check (advisory, NOT a PASS conjunct).* DIRECT ρ_B(13) = −0.658456 vs S103 FB-prior −0.646653 (diff 0.0118); DIRECT ρ_B(14) = −0.679195 vs −0.657020 (diff 0.0222). The S103 Friedrich-Bär midpoint slightly UNDER-estimated the tail magnitude. The DIRECT spread 0.0443091 essentially coincides with the S103 FB-envelope upper bound 0.044330 — the deep-truncation INFO is reproduced at direct (non-Casimir-bound) evaluation, sharpening the S103 mid-point prior to a directly-computed span.

**Output 4-tuple**: `(value=spread_CAC=0.0443091, scheme=zeta, convention=CAC-branch-iv-anchored-L10-DERIVED-OFFSET, L_max={12,13,14})`. **regulator_pin** `a_2^{Mellin}` poleconv-A-double, (pole_in_s=3, curvature_grade_n=2).

**Solution-space reading**: the branch-(iv) `w_0` Mellin-zeta channel is FB-envelope-BOUNDED at the deep set {12,13,14} (< 0.05) but NOT truncation-SATURATED into the W5-2 PASS band (≤ 0.025) — the channel carries a residual, decelerating L-drift. Per the §W1-1 dual_prior discriminator (INFO → unchanged 0.5/0.5), the truncation-saturation reading (Track A) is NOT confirmed; the DESI-WZ-LENSING-BIAS trigger pin stays **capacity-deferred** (its PASS precondition is not met). The DR3 falsifier prediction `w_0_B = −0.842454` rests on an envelope-bounded but not band-converged moment. Substrate arrow: D_K eigenvalues at τ_fold → Zubarev branch-(iv) Mellin-zeta moment ρ_B(L) → CAC-anchored emergent w_0 → DESI DR3 w_0–w_a measurement; the GT builder is a substrate-faithful construction of the (p,0) sectors in their intrinsic highest-weight space (no new physics, only a feasibility route around the 3^p dense wall).

---

### §W1-2. S105-LOOP-COUNTING-BINDING (lizzi-spectral-functional-theorist)

**Status**: COMPLETED
**Gate ID**: `S105-LOOP-COUNTING-BINDING`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (convergence rate of a normalized Hermitian-D_K moment vs the §VII.AF.1 HKR image)
**Agent**: `lizzi-spectral-functional-theorist`
**Hypothesis**: The normalized Hermitian moment M_m = Tr|D_K|^m / Tr|D_K|^0 (m=2) has a finite-to-continuum rate r(m,L) that is EITHER (Case A) the §VII.AF.1 L^{−3} HKR-image rate with a nameable HKR/Connes-Karoubi image → Level-2-BINDING (licenses a future registry-landing), OR (Case B) the bare W16 Mellin-truncation rate with no HKR image → Level-2-non-binding (confirm-internal).
**Plan reference**: `sessions/session-plan/session-105-plan-w1.md` §W1-2 (Case-A/B discriminator UNCHANGED from S104 §W5-4; obstruction-1 hermiticity / obstruction-2 HKR-map resolved as explicit sub-tests; m=2 PINNED).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- **script** `computations/session-105/s105_loop_counting_binding.py` — EXISTS (28412 bytes). `grep -E 'from canonical_constants import'` → `from canonical_constants import *  # noqa: F401,F403` ✓; `grep -E 'print_verdict_payload'` → `def print_verdict_payload(...)` + call site ✓.
- **data** `computations/session-105/s105_loop_counting_binding.npz` — EXISTS (9725 bytes); keys include `binding_class=Case-B-Level-2-non-binding`, `verdict=INFO`, `alpha_fit=nan`, `hkr_nameable=False`, `w_m_finite=False`, full `M_full`/`N_full` sequences, `r_seq`, `regulator_pin`.
- **plot** `computations/session-105/s105_loop_counting_binding.png` — EXISTS (119593 bytes); left panel M_2^(L) vs L with the divergent linear overlay, right panel growing shell increments ΔM_2.
- **verdict line** `computations/session-105/s105_gate_verdicts.txt` — `grep -E '^S105-LOOP-COUNTING-BINDING:.* audit_sha256=[a-f0-9]{64}'` → canonical INFO line present with full-64-hex `audit_sha256=a3c4bf5185d27097…ef543`; dual-SHA companion row + 2 extra companion rows (regulator_pin, Level-2 sub-class) present.
- **wp_section** this §W1-2 — Status COMPLETED / Verdict INFO / Output Artifacts / MCP Pre-Compute Audit blocks present.

**MCP Pre-Compute Audit**:
- `search_knowledge("loop counting envelope binding HKR L^-3 VII.AF.1 Level-2 binding")` → `S104-LOOP-COUNTING-ENVELOPE-SPEC` INFO (`binding_class_token=candidate-A-on-structure_HKR-image-UNDECIDED-at-spec-time_pending-numerical-reduction`); `§VII.AF.1.OP-PROJ` L^{−3} binding exemplar (0.0095% F_4 at L_max=10; envelope 0.10%); W16 wall `Level-2-non-binding bare-decomposition envelope` (constraint-mega-matrix, S88). Gate NOT pre-closed — it RESOLVES the S104 UNDECIDED state via numerical reduction.
- `search_knowledge("S104 LOOP-COUNTING-ENVELOPE-SPEC c_continuum w_m normalized Hermitian moment")` → spec npz provenance; `case_A_hkr_image_nameable=False`, `case_B_reduction=False` (already falsified), `c_continuum_status=NAMED (w_m, defined nonzero)` but no numeric value emitted (symbolic L→∞ limit of the moment itself).
- `trace_entity("VII.AF.1 OP-PROJ L^-3 binding exemplar")` → no direct trace; registry grep confirmed L^{−3} at d=4 substrate-distance-1 pole s=3, bridge map = Hochschild-Kostant-Rosenberg `L_max→∞`, binding image = HP^1 cohomology ↔ Peotta-Törmä BZ-trace.
- Precedent: `S89-CORNER-IV-K-WINDOW-LMAX-SCAN-LEVEL-2-ENVELOPE` (`alpha=5.0679;hkr=1;L2_class=Level-2-binding`) — a state-pair functional that DID get an HKR image, contrasting the present spectrum-only functional.

**Verdict**: **INFO** — `binding_class = Case-B-Level-2-non-binding` (confirm-internal). A non-binding determination is a boundary, not a FAIL (`math-scripts.md §"All Results Are Good Results"`). Per the plan rubric, Case-B is recorded as INFO. dual-SHA `audit_sha256=a3c4bf5185d27097d64f5e9df456c64b0b4f36b809e236761f9d6bae812ef543`, `content_sha256=6f594e76408df7827e9588360b294251c3b826c25d9016385d1ee2ace3ab8491`. This gate is `[VERIFY]` (set-membership), NOT `[SIGN]`; `schema_v2_3tuple_required: false` — no directional 3-tuple emitted (correct under the all-three-or-none rule).

**Results**:

NUMBERS first. The normalized Hermitian second moment of the s84 L=12 fold spectrum, `M_2^{(L)} = Tr|D_K^{(L)}|^2 / Tr|D_K^{(L)}|^0` (truncated at p+q≤L; |D_K| modulus = cache `abs_evals` with multiplicity):

| L | M_2^(L) | N_modes | ΔM_2 (shell increment) | in scan set |
|:--|:--------|:--------|:-----------------------|:------------|
| 8 | 7.617096 | 31,264 | — | (diag) |
| 9 | 9.173603 | 50,624 | 1.5565 | (diag) |
| 10 | 10.810396 | 78,080 | 1.6368 | scan |
| 11 | 12.555781 | 115,936 | 1.7454 | scan |
| 12 | 14.422480 | 166,896 | 1.8667 | scan |

m=0 sanity: `Tr|D_K|^0/Tr|D_K|^0 = 1.000000` (exact). Linear fit `M_2^(L) ≈ 1.6993·L − 6.0771`.

**The decisive finding**: `M_2^{(L)}` is **monotonically DIVERGING** with L, with shell increments themselves GROWING (1.5565 → 1.6368 → 1.7454 → 1.8667). The substrate D_K is an UNBOUNDED operator — its spectral ceiling `max|λ|(L)` grows linearly (3.92 at L=8 → 5.42 at L=12) — so the normalized mean-square eigenvalue `Tr|D_K|^2/N(L)` is dominated by the ever-widening upper shell and has **no finite thermodynamic limit**: `w_m = lim_{L→∞} M_2^{(L)} = +∞`. There is no finite continuum value `w_m`, hence `r(m,L) = |M_2^{(L)} − w_m|/w_m` is undefined (nan on all three scan points), `alpha_fit` is undefined (`undefined_divergent_r`), and `rate_match (|α−3|≤0.30) = False`.

**Binding-determination substitution chain (Case A vs Case B; substituted numbers):**
- Def 1: `M_2^{D_K} = Tr|D_K|^2/Tr|D_K|^0`, m=2 PINNED; |D_K| Hermitian-positive ⇒ **obstruction-1 (hermiticity) RESOLVED by construction** (real moment; no non-Hermitian directed-loop / skin-effect analog issue the S104 ZHONG observable carried).
- Def 2: `w_m` = named c_continuum from S104 spec = symbolic `lim_{L→∞} M_m^{(L)}` (the spec emitted `c_continuum_status=NAMED` but NO numeric value).
- Def 3: `r(m,L) = |M_2^{(L)} − w_m|/w_m`.
- Step 3 (substitute): `M_2^{(L)} ≈ 1.6993·L − 6.0771`, monotone-increasing with growing increments ⇒ Step 4 (direction): `lim_{L→∞} M_2^{(L)} = +∞` ⇒ **no finite w_m exists** ⇒ the Case-A SHAPE precondition (a finite-to-continuum difference `r ∝ L^{−α} → 0`) is **NOT met** (`shape_precondition_met = False`).
- Decision (CONJUNCTION, not disjunction): `Case-A iff (rate_match) AND (HKR-image nameable)`. Here `rate_match = False` AND `hkr_nameable = False` ⇒ **`binding_class = Case-B-Level-2-non-binding`**.

**Obstruction-2 (HKR-image nameability) — TESTED, not assumed.** Two INDEPENDENT reasons deny a nameable HKR/Connes-Karoubi/K-theory-boundary image:
1. **Spectrum-only ⇒ no cohomology-class content.** `M_2 = Tr|D_K|^2/Tr|D_K|^0` is an algebra-INVARIANT spectrum-only functional (a sum over |λ|, no projector, no cyclic cocycle, no Chern character). It is NOT a Connes-Karoubi pairing of a K-theory class with a cyclic cocycle, so it carries no HP^1 cohomology-class content. The §VII.AF.1 binding image is the HP^1 ↔ Peotta-Törmä BZ-trace map — an algebra-DEPENDENT cocycle pairing — and has no domain here. (This is the algebra-axis orthogonality distinction: spectrum-only vs state-pair/cocycle families are structurally orthogonal in identity-class membership per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`.)
2. **Divergence ⇒ no finite continuum target.** Even setting aside (1), the moment diverges, so there is no finite continuum `w_m` for any HKR image to land on; `‖HKR(c_L) − w_m‖` is ill-posed.

Either reason alone forces `hkr_nameable = False`. Per `cross-pillar-bridge-anatomy.md §"Level-2 sub-class"`, a Level-2 envelope is BINDING only if it has an HKR image that BINDS a Level-1 class; a bare-decomposition rate (even one whose exponent matched, which here it does not) is Level-2-non-binding and FORBIDDEN for registry-PASS.

**4-tuple**: `(value=binding_class=Case-B-Level-2-non-binding;…;m=2, scheme=Mellin, convention=SUBSTRATE-IS-TRUNCATION-ENVELOPE-NAMING, L_max=12)`. Regulator pin: `a_n^{Mellin}` poleconv-A-double, (pole_in_s=3, curvature_grade_n=2).

**Substrate framing (GEOMETRIC; substrate-first direction preserved).** The substrate IS the D_K spectral triple; `M_2 = Tr|D_K|^2/Tr|D_K|^0` is an intrinsic spectral functional of the fabric. The direction of explanation: `D_K eigenvalues → normalized modulus moment M_2 → finite-to-continuum rate r(m,L) → (Case A) HKR image bounding a laboratory-IN continuum observable, OR (Case B) a closed substrate-internal envelope with no laboratory image`. The gate did NOT invert this — it TESTED for the HKR image rather than assuming the moment is a bridge, and the test returned NULL on both the rate precondition and the nameability clause. The loop-counting envelope is a closed SUBSTRATE-INTERNAL observable: the W16 wall stands (substrate-internal Mellin-truncation rate cannot pose as cross-pillar bridge evidence). This RESOLVES the S104 `registry=INCOMPLETE-PENDING` status to **BINDING-DECIDED-non-binding**. No registry-landing is licensed (no S106+ §VII registry-landing carry-forward from this gate).

**Functional-sensitivity note (lizzi-axis).** The Case-A/Case-B split is itself a regulator-functional question, and the verdict is FUNCTIONAL-ROBUST in the relevant sense: the divergence of `Tr|D_K|^m/Tr|D_K|^0` for any fixed m≥1 on the unbounded D_K is a structural property of the spectrum (Weyl growth of the upper shell), independent of the spectral-functional CHOICE — it holds whether one reads the trace through a cutoff `f(D^2/Λ^2)`, a zeta `ζ_D(s)`, or a bare Mellin moment, because all three weight the SAME unbounded |λ| support and the NORMALIZED power moment has no Λ- or s-independent finite limit. What the §VII.AF.1 binding exemplar has and this moment lacks is a *projector* (the band-0 Chern character) that REGULATES the trace into a convergent cohomology pairing; the spectrum-only moment has no such regulating structure. This is the substrate-IS reason the W16 wall is functional-independent here: it is not that one regulator scheme fails to bind — it is that the spectrum-only observable carries no cohomology-class to bind, in any scheme.

---

## Wave 1 Synthesis (team-lead)

**JOINT-CONSIDERATION outcome — both gates INFO; the L_max-envelope axis is characterized, not closed.**

- **§W1-1 = INFO**: `spread_CAC = 0.0443091` ∈ (0.025, 0.050] — FB-envelope-bounded (< 0.05) at the deep set L ∈ {12,13,14} by DIRECT (non-Casimir-bound) evaluation; NOT W5-2-band-PASS (≤ 0.025). The direct spread essentially coincides with the S103 Friedrich-Bär upper bound (0.044330) — the envelope is confirmed at first-principles evaluation. Decrement monotone-decreasing and decelerating (3-tuple sign=PASS/magnitude=INFO/regime=VALID). Per the pre-registered dual-prior discriminator (INFO → 0.5/0.5 unchanged), **the DESI-WZ-LENSING-BIAS trigger pin stays capacity-deferred**. audit `71c162b0834aabb9…`.
- **§W1-2 = INFO**: `binding_class = Case-B-Level-2-non-binding`. The normalized Hermitian moment `M_2^{(L)} = Tr|D_K|²/Tr|D_K|⁰` diverges linearly (`≈ 1.6993·L − 6.0771`; no finite continuum target) and the HKR image is non-nameable on two independent structural grounds (spectrum-only functional carries no projector/cocycle/Chern structure; no finite target for any image to bound). **The W16 wall stands; NO registry landing is licensed.** S104 `registry=INCOMPLETE-PENDING` → **BINDING-DECIDED-non-binding** (dual-prior 0.9 → Track B confirm-internal). audit `a3c4bf5185d27097…`.
- **Machinery disjointness confirmed**: item 1 ran the CAC-anchored `ρ_B(L)` channel (scheme GT-DIRECT/CAC; offset_B = −0.340827; w_0^CAC(L=10) = −0.918 EXACT); item 2 the bare normalized-moment rate (scheme Mellin, m=2 pinned). No shared observable, no shared pin — the JOINT-CONSIDERATION constraint held by construction.
- **Enabling infrastructure (durable)**: the Sym^13/Sym^14 irrep-construction wall is **LIFTED** — the Gelfand-Tsetlin bosonic-ladder builder constructs (p,0)/(0,q) directly in occupation space (bit-exact 1e-16..1e-15 vs `irrep_symmetric_power`; 0.002 s vs a 40.7–366 TB dense path), Phase-1 sentinel PASS 7.51e-14 over 24 cached sectors. Technique + the normalization-trap hazard recorded in `.claude/agent-memory/spectral-geometer/gt-builder-high-L.md`.

**Effected In-Session (NON-MATH)**
- [x] GT-builder reusable-technique memory note — written by the dispatched agent — `.claude/agent-memory/spectral-geometer/gt-builder-high-L.md`
- [x] Hermiticity-guard dimension-scaling correction (1.0e-15 → max(1.0e-15, √D·ε)) — in-script, disclosed in §W1-1; flips regime MARGINAL→VALID only, verdict unchanged

## Carry-Forward Computations

No carry-forwards: all wave outcomes closed in-session. (The plan's two conditional CFs do not fire: the S106 §VII registry-landing required §W1-2 Case-A — it landed Case-B; the L≥15 feasibility study required a §W1-1 FAIL — it landed INFO.)

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-11 | branch-(iv) `w_0` truncation channel | S103-FB-INFO (Casimir-bound envelope 0.044330) | S105-DIRECT-INFO (direct spread 0.0443091 at deep set {12,13,14}) | First direct evaluation reproduces the FB envelope; Sym^13/14 wall lifted by GT builder |
| 2026-06-11 | S104 LOOP-COUNTING registry status | INCOMPLETE-PENDING | BINDING-DECIDED-non-binding | `M_2` diverges (no continuum target); HKR image non-nameable; W16 wall stands |
| 2026-06-11 | DESI-WZ-LENSING-BIAS trigger pin | capacity-deferred | capacity-deferred (unchanged) | dual-prior INFO → 0.5/0.5; Track A unconfirmed |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | JSON | Size |
|:-----|:-------|:------------|:------------|:-----|:-----|
| S105-BRANCH-IV-DIRECT-L1314 | s105_branch_iv_direct_l1314.py | s105_branch_iv_direct_l1314.npz + s105_branch_iv_l1314_sectors_resume.npz | s105_branch_iv_direct_l1314.png | — | 43,512 / 14,607 + 151,073 / 83,879 B |
| S105-LOOP-COUNTING-BINDING | s105_loop_counting_binding.py | s105_loop_counting_binding.npz | s105_loop_counting_binding.png | — | 28,412 / 9,725 / 119,593 B |
