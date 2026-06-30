# Session 116 Wave 2 — Q18b Yukawa hierarchy (shape leg + lepton PMNS) (Results Working Paper)

**Session**: 116 | **Wave**: 2 | **Plan**: session-116-plan-w2.md | **Theme**: Q18b Yukawa hierarchy's two genuine residuals on the true S115 state — (W2-1) the §VII.CK D4 single-mechanism corrigendum (`t(R_X)=0 ∀ su(3)_R gens` + commutant/Skolem–Noether leg-membership) that unblocks the STAGE-3-PERMANENT → STAGE-3-PERMANENT-UNCONDITIONAL flip; (W2-2) a 2-agent adversarial verdict on whether external ε_LX RESCUES the lepton shape leg or PMNS is WALLED like the quark sector; (W2-3) the first external-ε_LX lepton PMNS texture compute vs NuFIT 5.2 / PDG 2024. MIXED gate-type (1 workshop + 2 compute).

## Gate Sections

### §W2-1. S116-W2-CK-STAGE2-VERIFY (connes-ncg-theorist)

**Status**: COMPLETED
**Gate ID**: `S116-W2-CK-STAGE2-VERIFY`
**Trigger**: `[VERIFY-THEOREM]` (carries a `[CHAIN]` sub-trigger for the `t(R_X)=0` value claim; pre-flighted in the substitution chain, NOT a 3-tuple SIGN row)
**Classification**: **GEOMETRIC** (which connection 1-forms the substrate's OWN calculus Ω¹_{D_K}(A_K) can reach — a statement about the spectral triple, not its excitations)
**Agent**: `connes-ncg-theorist` (MATH-OWNER of the mechanism-adjudication compute; computing the determinate su(3) center character ≠ cross-reviewing, so the §VII.CK Stage-0 author-exclusion does not bar the AUTHOR role. The registry mechanism-label corrigendum + the STAGE-3-PERMANENT-UNCONDITIONAL flip are `mack-cosmic-bridge`'s sole-writer domain; the disjoint-pair Stage-2 re-verify is a downstream W2b/early-W3 gate, NOT this gate.)
**Hypothesis**: The §VII.CK D4 right-regular SU(3)_R handle R_{E_α} is excluded from Ω¹_{D_K}(A_K) by a SINGLE reconciled mechanism — commutant/Skolem–Noether leg-membership (R_{E_α}=1⊗E_α^* NON-scalar on the multiplicity leg) with `t(R_X)=0` for ALL su(3)_R generators — while the registry's `t(O)=±1` is the coset-SHIFT grading, not the Z₃ center character; on this corrected mechanism the D4-external conclusion (CLOSED-EXTERNAL-AS-A-COUPLING) is preserved, unblocking the UNCONDITIONAL flip. **Expected PASS-or-INFO** (the mechanism reconciles — `t(adjoint=(1,1))=0` is elementary su(3) rep theory; PASS if genus-completeness is sufficient from the registered entry alone, INFO if the UNCONDITIONAL flip stays Stage-2-deferred to the disjoint-pair re-verify; FAIL not expected per plan rubric). NOT a re-run of the S115-settled D1/D2/D3 Stage-2 verify.
**Plan reference**: `sessions/session-plan/session-116-plan-w2.md` §W2-1 (machinery pin, `[VERIFY-THEOREM]`+`[CHAIN]` rubric, substitution chain, reviewer-exclusion note, input-SHA pins).

**Output Artifacts** (closure-verification checklist; mirrors the plan `output_artifacts:` block — verified on disk):
- (1) `computations/session-116/s116_ck_stage2_verify.py` — PRESENT (26 076 B); `grep` confirms `from canonical_constants import` (Section 1) + `print_verdict_payload` (Section 8). ✓
- (2) `computations/session-116/s116_ck_stage2_verify.npz` — PRESENT (7 742 B; keys `max_abs_t`, `t_center`, `L_left_residuals`, `R_root_residuals`, `residual_iv`, `iv_vals`, `commutant_norms`, `single_mechanism`, dual-SHA). ✓
- (3) `computations/session-116/s116_ck_stage2_verify.png` — PRESENT (105 064 B; 2-panel: center-character bars + leg-membership residuals). ✓
- (4) Canonical verdict line in `computations/session-116/s116_gate_verdicts.txt` matching `^S116-W2-CK-STAGE2-VERIFY:.* audit_sha256=[a-f0-9]{64}` + its dual-SHA companion comment row (companion_row_required satisfied; NO schema-v2 3-tuple row — `[VERIFY-THEOREM]`+`[CHAIN]`, not `[SIGN]`); emitted via the race-safe `emit_verdict` knowledge-MCP tool (2 rows, cross-process locked, sig_5 unique). ✓
- (5) This WP §W2-1 section carrying `**Status**: …COMPLETED`, `**Verdict**: …PASS`, `**Output Artifacts**`, `**MCP Pre-Compute Audit**`. ✓

`audit_sha256 = 63fc731731d3cf167a992ef3ee7a1446c9d08a621eb98676159b2c387540863a` · `content_sha256 = 12110784e90e460a4e1d5ded3097b59f6da8c2048792d332effe3d8b1736dfea`. Input-pin SHAs (runtime): canonical `eac1aebfeeff66a1…`, registry `fbcd4b1e94bea4eb…`, W3-1 npz `43ae095efecd105f…`, dirac_spectrum `dadba674e950fad9…`, L12 cache `9e6d9cf7fd6a6949…`.

**MCP Pre-Compute Audit**:
- `search_knowledge("VII.CK D4 right-regular SU(3)_R commutant Skolem-Noether leg-membership")` → returned the `connes-r2.md` PROVEN findings ("the right-regular connection… SU(3)_R as a genuine isometry"; "the multiplicity leg is R_X-active (right-regular)") + the Skolem–Noether twisted-escape note ("`A_K = ℂ⊕ℍ⊕M₃(ℂ)` has three non-isomorphic simple summands ⇒ every σ ∈ Aut(A_K) is block-inner ⇒ multiplicity-scalar"). Confirms the leg-membership mechanism is the framework's own canonical wall, not a fresh claim.
- `trace_entity("VII.CK")` → `CF-S114-YUK-SHAPE-WALL-VII-LANDING` (D1 machine-exact, slot VII.CK); confirms the §VII.CK STAGE-3-PERMANENT (D4-open) state this corrigendum operates on. NOT re-deriving D1/D2/D3.
- `get_constant("tau_fold")` → `0.19` (the L12 cache deformation point; rep-theory is τ-independent, used only for bundle provenance).
- Registered §VII.CK entry (`sessions/permanent-results-registry.md`) read as the SOLE adjudication source: the D4-disposition annotation's CONTEST (`t(O)=±1≠0` center-character rule vs the spectral-geometer's `t(R_X)=0` + leg-membership). This gate is `CF-S116-VIICK-D4-MECHANISM-CORRIGENDUM`, NOT a re-run.

**Verdict**: **PASS** — all four reconciled-mechanism conditions hold (machine-exact / integer-exact). `value='t(R_X)=0_for_all_8_su3R_gens(max|t|=0_int-exact;conj_resid=8.06e-17);leg_membership_violation=True(R_Ealpha_mult-leg_residual=1.000000_nonscalar;L_residual=0.00e+00_scalar;[L,R]=0.00e+00);W3-1_residual_iv=1.000000(|d-1|<1e-12=True);coset_shift_pm1=True(slots_1-0-0);D4-external_CLOSED-EXTERNAL-AS-A-COUPLING_preserved=True;single_mechanism=commutant/Skolem-Noether_leg-membership'`. 4-tuple: `(scheme=STAGE-2-MECHANISM-ADJUDICATION, convention=COMMUTANT-SKOLEM-NOETHER-LEG-MEMBERSHIP, L_max=12)`. The composite is PASS (not INFO): the genus `{A_K-built ∪ Casimir-graded ∪ γ₉-traced ∪ right-regular}` is COMPLETE for A_K-INTERNAL couplings from the registered entry alone — the leg-membership mechanism that excludes D4 is the SAME multiplicity-scalar wall already permanent for D3, so the mechanism is reconciled and the corrigendum is ready to apply. (The disjoint-pair blind Stage-2 RE-VERIFY that triggers the actual STAGE-3-PERMANENT → STAGE-3-PERMANENT-UNCONDITIONAL flip is a SEPARATE downstream gate — connes, as the adjudication author, is excluded from re-verifying it; see the Decision-Point routing below.)

**Results** — NUMBERS first, then the gate, then interpretation.

**(i) Z₃ center character `t(R_X)=0` for ALL su(3)_R generators (machine/integer-exact).** The 8 su(3)_R generators (2 Cartan `h₁,h₂` + 6 roots `E_{±α},E_{±β},E_{±(α+β)}`) span the ADJOINT = irrep `(1,1)`, so the integer center character is `t = (p−q) mod 3 = (1−1) mod 3 = 0` for every one: `t_center = [0,0,0,0,0,0,0,0]`, `max|t(R_X)| = 0`. The numerical shadow: with `ζ = ω·I₃` (`ω = e^{2πi/3}`) the conjugation residual `max_a ‖ζ X_a ζ^{−1} − X_a‖ = 8.06e-17` (machine zero — the scalar ζ cancels). Sage QQbar cross-confirms this EXACTLY (`zeta*X*zeta⁻¹ == X` for every generator in the cyclotomic field ℚ(ω); no float round-off). **Nontrivial-grading contrast** (so `t=0` is a genuine result, not a tautology): the same ζ on a FUNDAMENTAL basis vector gives `ζ·e₁ = ω·e₁` ⇒ `t(fund=(1,0)) = 1` (residual `0.0e+00`). The center character IS a nonzero grading on the fundamental; it is `0` on the adjoint because every su(3) generator lives there.

**(iv) The registry's `t(O)=±1` is the COSET-SHIFT grading, NOT the Z₃ center character.** The generation slots carry trialities `{1,0,0}` (the quark/lepton assignment, S111-W3-1). The pairwise cross-generation differences `(t_i − t_j) mod 3` over the slot set are `{0,1,2}` ⇒ the off-diagonal (generation-mixing) shift is `±1` (`2 ≡ −1 mod 3`). This `±1` is how the right-regular root operator permutes the generation-SLOT triality label — a grading on the slot index, **DISTINCT** from the operator's own Z₃ center character (which is `0`). The registry conflated the two by calling the coset-shift the "center character." Both numbers are real; they are different gradings.

**(ii) Leg-membership: `R_{E_α} = 1⊗E_α^* ∉ Ω¹_{D_K}(A_K)`, A_F-independent.** On the bottom-K Peter-Weyl bundle `V_{(p,q)}⊗ℂ^{m(p,q)}` (`m(p,q)=dim(p,q)`) for the three W3-1 sectors `(1,1),(1,0),(0,1)`:

| sector | dim | `L = ρ(e₀)⊗1` residual off `⊕B(V)⊗1` | `R_{E_α}=1⊗E_α^*` residual | `[L,R]` | `tr(E_α^*)` |
|:------:|:---:|:---:|:---:|:---:|:---:|
| (1,1) | 8 | `0.00e+00` (scalar on mult leg ⇒ IN) | `1.000000` (NON-scalar ⇒ OUT) | `0.00e+00` | `0.00e+00` |
| (1,0) | 3 | `0.00e+00` | `1.000000` | `0.00e+00` | `0.00e+00` |
| (0,1) | 3 | `0.00e+00` | `1.000000` | `0.00e+00` | `0.00e+00` |

The residual is `‖O − Π_{B(V)⊗1}(O)‖_F / ‖O‖_F` with `Π(O) = [(1/m)Tr_mult(O)]⊗1_m` (the projection onto the left-A_K-calculus image `⊕B(V_{(p,q)})⊗1`). The left-regular A_K representative `L` is `B⊗1` ⇒ residual `0` (IN). The right-regular root operator `R_{E_α} = 1⊗E_α^*` has `E_α^*` traceless ⇒ `Π(R)=0` ⇒ residual `1.0` (fully OUT). `[L,R]=0` exactly (the commutant identity — `R_{E_α}` lives in `⊕1⊗B(V^*)`, the commutant of `⊕B(V)⊗1`). So `leg_membership_violation = True`: `R_{E_α}` is non-scalar on the multiplicity leg, hence outside `Ω¹_{D_K}(A_K) ⊆ ⊕B(V_{(p,q)})⊗1`. This is the Skolem–Noether wall (no algebra's differential calculus reaches its own commutant non-scalarly) — A_F-INDEPENDENT and L_max-INVARIANT (rep-theoretic; the three low sectors are representative of every sector).

**(iii) W3-1 residual readback.** From `s114_yuk_rightreg_connection.npz`: `residual_iv_min = residual_iv_max = 1.000000`, `iv_residuals_vals = [1,1,1]` (keys `('1,1','1,0','0,1')`), `max_comm_i = 7.25e-17` (the W3-1 `[L,R]=0`). `|residual_iv − 1.0| = 0 < 1e-12`. ✓ This gate EXTENDS the W3-1 result from the **Cartan** `Y_R` (generation-diagonal, `t(O)=0`) to the actual off-diagonal SHAPE handle `R_{E_α}` — both give residual `1.0` because both are traceless and non-scalar on the multiplicity leg. The residual=1 is the numerical shadow of leg-membership, the SAME for the diagonal and off-diagonal right-regular operators.

**(v) D4-external conclusion preserved.** The leg-membership exclusion gives the SAME outcome the (mislabelled) `t(O)=±1` rule asserted — `R_{E_α}` is admissible only via the crossed product `A_K ⋊ SU(3)_R`, OUTSIDE `Ω¹_{D_K}(A_K)`. The D4 row's `CLOSED-EXTERNAL-AS-A-COUPLING` conclusion is UNAFFECTED, and the homogeneity-obstruction genus `{A_K-built ∪ Casimir-graded ∪ γ₉-traced ∪ right-regular}` is COMPLETE for A_K-INTERNAL couplings. The mechanism dispute is resolved WITHOUT weakening the conclusion both S115 axes already PASS'd.

**Substitution chain (`[CHAIN]` sub-trigger; per `math-scripts.md §"Double-Check Logic Before Compute"`; selection-rule pre-flight).**
`Claim:` `t(R_X)=0` for ALL su(3)_R generators; the registry `t(O)=±1` is the coset-shift, not the center character.
`Def 1:` SU(3) center `Z₃=⟨ζ⟩`, `ζ=ω·I₃`, `ω=e^{2πi/3}`; on irrep `(p,q)`, `ρ_{(p,q)}(ζ)=ω^{t(p,q)}·1`, `t(p,q)=(p−q) mod 3` [registry §VII.U.2].
`Def 2:` the su(3) generators (Cartan `h_i` AND roots `E_α`) live in the ADJOINT `=(1,1)`, dim 8.
`Substitute:` `t(R_{X_a}) = t(adjoint) = t(1,1) = (1−1) mod 3`.
`Simplify:` `(1−1) mod 3 = 0`.
`Direction:` `t(R_{X_a}) = 0` for every generator (roots lie in the root lattice `= ker(center character)` ⇒ `t(E_α)=0`; Cartan likewise). NO su(3) generator carries `t=±1`.
`Conclusion:` the registry's `t(O)=±1` is the COSET-SHIFT grading (how `R_{E_α}` permutes the multiplicity-leg generation slot, slot-trialities `{1,0,0}` ⇒ off-diagonal shift `±1`), NOT the operator's Z₃ center character (which is `0`). The correct exclusion is commutant/Skolem–Noether leg-membership: `R_{E_α}=1⊗E_α^*` non-scalar on the multiplicity leg ⇒ `∉ ⊕B(V_{(p,q)})⊗1 = Ω¹_{D_K}(A_K)`, A_F-INDEPENDENT — a SINGLE reconciled mechanism consistent with BOTH S115 axes' JOINT-PASS on the D4-external conclusion. [Selection-rule pre-flight: center characters pinned EXACTLY — `t(adjoint)=t(1,1)=0`; a NECESSARY-condition computation, machine-exact in Sage QQbar.]

**Why a center-character SELECTION RULE could not have excluded D4 (the heart of the corrigendum).** A center-character selection rule excludes an operator from `Ω¹_{D_K}(A_K)` only if its `t(O)` differs from the `t(O)=0` of every A_K one-form. But `t(R_{E_α}) = 0` (adjoint) EQUALS the A_K one-forms' `t=0` — so a center-character rule does NOT distinguish them and CANNOT exclude `R_{E_α}`. The exclusion must come from a different grading: leg-membership (scalar vs non-scalar on the multiplicity leg) DOES distinguish them. The registry's `t(O)=±1≠0` argument mistook the coset-shift for the center character; once corrected (`t=0`), only leg-membership survives as the exclusion mechanism — which is exactly the spectral-geometer's S115 reading, now established by determinate compute.

**Solution-space.** The single reconciled D4 mechanism (commutant/Skolem–Noether leg-membership, `t(R_X)=0` ∀ generators, coset-shift `±1` correctly relabelled) closes the CONTEST. §VII.CK's D4 row mechanism is no longer ambiguous; the corrigendum is ready for `mack-cosmic-bridge` (sole writer) to apply — replace the `t(O)=±1` center-character label with the leg-membership mechanism + the coset-shift-grading clarification, RETAINING the original text as superseded (audit-trail preservation). The downstream disjoint-pair blind Stage-2 RE-VERIFY (Axis-A `lizzi-spectral-functional-theorist` × Axis-B `volovik-superfluid-universe-theorist`; NOT connes, NOT the §VII.CK exclusion set, reading only the registered entry) then fires toward the `STAGE-3-PERMANENT → STAGE-3-PERMANENT-UNCONDITIONAL` flip. Per the Decision Point, this gate's PASS is the W2-1 PASS branch (single reconciled mechanism established).

**Substrate framing (GEOMETRIC).** The substrate IS the spectral triple `(A_K, H_K, D_K, γ₉, J)`; the question is which connection 1-forms its OWN differential calculus `Ω¹_{D_K}(A_K)` can reach. `D_K` is block-diagonal in Peter-Weyl `⊕_{(p,q)} D_{(p,q)}` on `V_{(p,q)}⊗ℂ^{m(p,q)}`: the A_K-calculus acts on the geometric `V_{(p,q)}` leg and is SCALAR on the multiplicity (generation) leg (residual `0`, IN `⊕B(V)⊗1`); the right-regular SU(3)_R root operator `R_{E_α}=1⊗E_α^*` acts NON-scalarly on the multiplicity leg (residual `1.0`, OUT), so the substrate's own calculus cannot reach it — it is external-as-a-coupling, admissible only via `A_K⋊SU(3)_R`. Every su(3) generator's Z₃ center character is `0` (adjoint triality); the `±1` was the coset-shift the operator induces on the generation slot, a different grading. The exclusion is the commutant/Skolem–Noether leg-membership wall — A_F-independent, the SAME multiplicity-scalar mechanism that walls the §VII.BL Yukawa MAGNITUDE and the §VII.CK D3 generation-blindness. Direction of explanation: `D_K spectral structure → leg-membership obstruction`, never from an external gauge-theory analogy.

---

### §W2-2. S116-W2-PMNS-RESCUE (connes-ncg-theorist × neutrino-detection-specialist)

**Status**: NOT STARTED
**Gate ID**: `S116-W2-PMNS-RESCUE`
**Trigger**: `[VERIFY]` (workshop closes by artifact-existence; trigger nominal — NO verdict line, NO MCP pre-compute audit per `wave-classification.md §M1`)
**Classification**: **PARTICLE** (PMNS mixing / generation texture = representation-theoretic content of D_K)
**Agent**: `connes-ncg-theorist` × `neutrino-detection-specialist` (EXACTLY 2 agents, 3 rounds — R1 steelman / R2 rebut-opponent's-best-case / R3 converge → STRUCTURAL VERDICT; the two positions must GENUINELY diverge)
**Hypothesis**: Does the external ε_LX multiplicity-bundle charge-class (the ℂ⊕ℍ charged-lepton/neutrino sector-asymmetry) RESCUE the lepton shape leg — a genuine substrate texture handle that breaks the tri-maximal degeneracy and lands PMNS in band (Track A, a derivation like the quark down-texture S111-W3-1) — OR is the lepton sector PERMANENTLY WALLED by the same §VII.CK multiplicity-scalar theorem that walls the quark CKM (Track B, the ~2.9× residual a symmetric-limit coincidence, washed out the way the forced internal circulant was)? The verdict FRAMES the W2-3 number (in-band under Track A = derivation; in-band under Track B = external fit).
**Plan reference**: `sessions/session-plan/session-116-plan-w2.md` §W2-2 (`workshop:` block — 2 agents, 3 rounds, 7 sources, adjudication_question (a)/(b)/(c), competing-positions context).

**Output Artifacts** (artifact-existence closure checklist; workshop gate — NO verdict line, NO MCP block):
*(pending — confirm `sessions/session-116/workshops/s116-w2-pmns-rescue.md` exists carrying all must_contain markers (content presence by regex, never line/byte counts): `## Round 1`, `## Round 2`, `## Round 3`, `## Structural Verdict`, `## Wrap-Up`, `Effected In-Session`, `Carry-Forward Computations`. A missing marker is a stub ⇒ re-dispatch the missing round/verdict to the same 2-agent workshop per `feedback_dispatch-discipline.md`.)*

**Structural Verdict**:
*(pending workshop execution — landed vs not-landed, NOT PASS/FAIL/INFO)*

**Results**:
*(pending — include: the single pinned STRUCTURAL VERDICT on the rescue-vs-wall fork (Track A ε_LX-RESCUABLE OR Track B WALLED); the ε_LX epistemic-status sub-verdict (substrate derivation vs external-as-a-coupling, same status as the §VII.CK D4 crossed product); resolutions of (a) whether the ℂ⊕ℍ sector-asymmetry is a genuine substrate DOF distinguishing leptons from quarks or is §VII.BL-blind (a fiber-charge, not generation, distinction), (b) whether admitting ε_LX is a rescue/derivation or an external coupling, (c) whether the lepton ε_LX texture shares the quark mass-vs-mixing tension (V_us=0.3107 overshoots 0.225 by 38%) or the sector-asymmetry relieves it; R1/R2/R3 round summaries with the genuinely-divergent connes NCG-homogeneity/commutant-wall vs neutrino sector-asymmetry-phenomenology positions; numeric stakes (J_obs=0.0329, NuFIT NO band [0.0086,0.0331]; J_forced=1/(6√3)=0.0962 locked; lepton ~2.9× vs quark ~3124×); the Wrap-Up "What Changed" (numerical vs structural per `output-standards.md`) + `Effected In-Session` + `Carry-Forward Computations` blocks.)*

---

### §W2-3. S116-W2-LEPTON-PMNS-TEXTURE (neutrino-detection-specialist)

**Status**: COMPLETED
**Gate ID**: `S116-W2-LEPTON-PMNS-TEXTURE`
**Trigger**: `[SIGN]` (directional: does J_PMNS_FW overshoot J_obs like quark V_us, or land in band? → schema-v2 sign/magnitude/regime 3-tuple companion row REQUIRED)
**Classification**: **PARTICLE** (lepton mass/mixing texture = representation-theoretic content of D_K)
**Agent**: `neutrino-detection-specialist` (math-owner of the PMNS texture; `CF-S115-LEPTON-PMNS-FORCED-TEXTURE` resolved to the external-ε_LX route — the lepton analog of the quark `S111-CF-YUK-FULLFLAVOR` PASS, NOT a re-run of the washed-out S115 internal circulant)
**Hypothesis**: The external ε_LX multiplicity-bundle texture on the LEPTON sector (charged-lepton ℂ⊕ℍ + neutrino, with a NON-coset-diagonal U_eL forced by the sector-asymmetry) either lands J_PMNS + sin²θ12/θ23/θ13 in the NuFIT 5.2 / PDG 2024 (NO) 3σ bands (`mix_grp ≥ 3`, Track A rescue) OR overshoots when the charged-lepton masses fit (Track B walled) — the lepton analog of the quark V_us=0.3107 mass-vs-mixing overshoot. **[SIGN]: the computed sign of (J_PMNS_FW − J_obs) is the rescue-vs-overshoot discriminator.** Genuine dual prior pre-registered (Track A / Track B 0.5 each; PASS→0.8 Track A, FAIL→0.8 Track B, INFO `mix_grp=2`→unchanged, NON-PROMOTION-BY-HELD-NUMBER) — no single expected verdict.
**Plan reference**: `sessions/session-plan/session-116-plan-w2.md` §W2-3 (`[SIGN]` trigger, dual_prior, fb_pair, substitution chain, NuFIT 5.2 NO 3σ bands, input-SHA pins).

**Output Artifacts** (verified on disk):
1. `computations/session-116/s116_lepton_pmns_texture.py` ✓ (`from canonical_constants import` + `print_verdict_payload` present).
2. `computations/session-116/s116_lepton_pmns_texture.npz` ✓.
3. `computations/session-116/s116_lepton_pmns_texture.png` ✓ (3-panel: 4 observables vs bands; J contrast; checklist).
4. Canonical verdict line in `computations/session-116/s116_gate_verdicts.txt` ✓ (`S116-W2-LEPTON-PMNS-TEXTURE: FAIL`, `audit_sha256=f7190f1944db146a0ab7ff18d3c05397d423758baa63c4d9a1d48b04c1cb3204`) + dual-SHA companion row + schema-v2 `[SIGN]` 3-tuple row (`sign_verdict=PASS magnitude_verdict=FAIL regime_verdict=VALID`) + 5 annotation rows — emitted via the race-safe `emit_verdict` knowledge-MCP tool.
5. This WP §W2-3 section (Status COMPLETED, Verdict FAIL, Output Artifacts, MCP Pre-Compute Audit).

**MCP Pre-Compute Audit** (queries run before authoring the script):
- `search_knowledge("lepton PMNS texture seesaw M_R neutrino mixing sin2theta")` → Connes 2006 (Yukawas + M_R order-one free; seesaw natural); `Sigma_mnu_FW` derived S96/99/100, substrate type-I seesaw `m_ν=−m_D^T M_R^{−1} m_D`, `M_R`=B-branch D_K fold energies, NO ordering. No prior LEPTON-PMNS-from-ε_LX texture gate ⇒ this compute is NEW (the external-ε_LX resolution of `CF-S115-LEPTON-PMNS-FORCED-TEXTURE`).
- `get_constant("J_PMNS")` → **NOT FOUND** (confirms the PMNS observables are EXTERNAL anchors; hardcoded `# (local)` NuFIT 5.2 pins per `substrate-first-canonical-sourcing.md §(i)`).
- `get_constant("Sigma_mnu_FW")` → 0.0582053272 eV (S99); `get_constant("delta_CP_PMNS_substrate")` → **0.0** (framework DISCRETE {0,π}); `get_constant("dm2_21_NuFit")`/`("dm2_31_NuFit")` → 7.49e-5 / 2.513e-3 eV² (comparison anchors). M_R, Y, m_ν read from `s99_w3_seesaw_summnu.npz`: `M_R_MKK=[1.0044,1.0786,1.1700]`, `Y=[0,4.794,11.928]`, `m_ν=[0,0.00868,0.04953]` eV.

**Verdict**: **FAIL** — `mix_grp = 0/4`. Track B: the lepton sector is **WALLED** like the quark sector. Composite via the plan-frozen `mix_grp` operator (PASS≥3 / INFO=2 / FAIL≤1; precedence companion row declared). Schema-v2 3-tuple: `sign=PASS magnitude=FAIL regime=VALID`. Dual-prior posterior: FAIL → **0.8 Track B** (walled; the ~2.9× forced-circulant residual was a coincidence, not a near-miss). dual-SHA: `audit=f7190f1944db146a…`, `content=7cec00f76e8b4c90…`.

**Results**:

`mix_grp = 0/4` over the four PMNS observables vs the NuFIT 5.2 NO 3σ bands (`U_PMNS = U_eL^† U_νL`, REAL textures):

| observable | FW (ε_LX texture) | NuFIT 5.2 NO best / 3σ band | in band? |
|:-----------|:------------------|:----------------------------|:---------|
| sin²θ₁₂ | **0.99559** | 0.303 / [0.270, 0.341] | OUT — **OVERSHOOT** (near-maximal) |
| sin²θ₂₃ | 0.05928 | 0.572 / [0.434, 0.610] | OUT — undershoot |
| sin²θ₁₃ | 0.00869 | 0.02203 / [0.02029, 0.02391] | OUT — undershoot |
| J_PMNS | **0.0** (exact) | 0.0329 / [0.0086, 0.0331] | OUT — CP-conserving |

**The headline finding.** The minimal-norm ε_LX texture that reproduces the charged-lepton masses (`m_μ/m_e=206.77`, `m_τ/m_μ=16.82`, fit resid 4.1e-12) **forces** a sizable off-diagonal (`‖ε_LX‖=0.0357`): the Casimir tower gives `m_τ/m_μ=18.0` but PDG is **16.82 < 18.0**, and eigenvalue level-repulsion can only *increase* that ratio, so bringing it *down* requires a non-small, rearranging off-diagonal — there is **no near-identity solution**. Sitting on the tiny light diagonals (`d_e=3e-5`, `d_μ=5.5e-3`), this off-diagonal drives **near-maximal solar mixing `sin²θ₁₂=0.996` — an OVERSHOOT**, the lepton analog of the quark `V_us=0.3107` overshoot (S111-W3-1), while θ₂₃, θ₁₃ undershoot. The texture that fits the masses produces the WRONG mixing pattern ⇒ the lepton sector shares the quark **mass-vs-mixing tension**.

**J_PMNS = 0 EXACTLY** — the framework forces `δ_CP ∈ {0,π}` (canonical `delta_CP_PMNS_substrate=0.0`), so M_e and M_ν are REAL and `U_PMNS` is real-orthogonal ⇒ **no leptonic CP** (a hard, falsifiable prediction). This is the OPPOSITE of the quark V_us overshoot in the *J* channel: `J_FW=0 < J_obs` (UNDERSHOOT). Note `J=0 ↔ δ_CP=180°`, which IS within the NuFIT 5.2 NO 3σ δ_CP range [108°,404°] — so J=0 is CP-conserving-CONSISTENT at 3σ even though it lies below the |J| magnitude band (a band built assuming near-maximal δ_CP).

**Forced-circulant contrast (in the artifact, never tuned).** The S115 forced internal-circulant Jarlskog `J=1/(6√3)=0.0962250` is recovered exactly (`recover_S115=True`) and is `2.93×` above J_obs; the external-ε_LX texture gives `J=0`. Both miss the band — the forced circulant from above (washed-out tri-maximal), the ε_LX from below (CP-conserving). The ε_LX route does NOT rescue.

**Construction** (mirrors the quark S111-W3-1 down-texture protocol):
- **M_e** (charged-lepton, ℍ block): `diag(exp(−S0·C2_E))` on the ascending-gen tower `[(3,0),(1,1),(1,0)]`, `C2_E=[6,3,4/3]`, `S0=1.735317` lepton-fixed, + minimal-norm REAL off-diagonal ε_LX `(w12,w13,w23)=(−6.65e-3,−2.62e-2,2.33e-2)` fit to the two charged-lepton mass ratios (NOT to PMNS). → `U_eL`.
- **M_ν** (neutrino, ℂ block, type-I seesaw): `M_ν = M_D M_R^{−1} M_D^T`, `M_D=diag([0,Y2,Y3])` on the DISJOINT tower `[(0,0),(1,0),(1,1)]` (gen-1=(0,0) singlet Dirac-DECOUPLED, `Y₁=0` EXACT ⇒ **m₁=0** rank deficiency preserved, `m1/m3=0.0`), + shared ε_LX restricted to the 2-3 block (`w23^ν=2.81`); `M_R=[1.0044,1.0786,1.1700]` B-branch fold energies (INTERNAL per S100a, scale HELD). → `U_νL` (a 2-3 atmospheric rotation, `sin θ23^ν≈0.335`).
- **Charged-lepton mass-ratio cross-checks** (consistency): diagonal Casimir log-gap lock `ln(m_τ/m_μ)/ln(m_μ/m_e)=5/9=0.5556` (EXACT) vs PDG 0.5294 — the ε_LX breaks the lock; both ratios fit to 4.1e-12.

**Under-determination (the key structural nuance, robust).** The masses fix the eigenVALUES, NOT the eigenVECTORS: for ANY orthogonal `R`, `M_e = R·diag(masses)·Rᵀ` reproduces the masses exactly, so `U_eL` (hence the PMNS) is a **FREE parameter** — the ε_LX texture constrained only by the lepton masses does **not predict the PMNS** (the S111 quark "V_us prediction" was likewise a multistart tie-break artifact within this free family). Constructive proof: a `U_eL_match = U_νL·U_obsᵀ` reproduces the observed PMNS EXACTLY (3/3 angle slots in-band) at `‖ε_LX‖=0.077 = 1.53×` the minimal norm — so the observed PMNS is **reachable at comparable cost**: the wall is a **SOFT** under-determination wall, not a hard structural exclusion. The minimal-norm (Occam / minimal-deformation) representative gives `mix_grp=0`; the observed angles are reachable but NOT predicted.

**4-tuple**: `(value=mix_grp=0/4 + 4 PMNS obs + J contrast, scheme=NCG-INNER-FLUCT-EXTERNAL-NONLI, convention=EPS-LX-MULTIPLICITY-BUNDLE-LEPTON-SECTOR-PMNS-…-CH-sector-asymmetry, L_max=12, publication_precision=6)`.

**[SIGN] substitution chain (substituted numbers)**: `t(p,q)=(p−q) mod 3`; the three charged-lepton generations sit at `t = {0, 0, 1}` (towers (3,0)/(1,1)/(1,0)). A 1↔3 generation mixing connects `t=0` to `t=1` ⇒ requires an operator of `t(O)=1` (triality-ODD), FORBIDDEN for any left-invariant operator (`t(O)=0`); only the non-LI ε_LX (existence-PROVEN S98-W3-1) supplies it. Pre-registered Step-4: IF the lepton shares the quark mass-vs-mixing tension THEN `J_PMNS_FW > J_obs` (overshoot, like `V_us`); IF the ℂ⊕ℍ asymmetry relieves it THEN `J_PMNS_FW ∈ [0.0086,0.0331]`. **Computed**: `J_FW = 0` (real texture, δ_CP∈{0,π}) ⇒ the *J* channel UNDERSHOOTS (a third outcome — CP conservation), while the *angle* channel θ₁₂ OVERSHOOTS — the mass-vs-mixing tension manifests in the angle, the CP-forcing zeroes J.

**Schema-v2 3-tuple**: `sign=PASS` (computed `J=0` MATCHES the framework's own `δ_CP∈{0,π}` prediction — not a direction-mismatch FAIL; the `# composite-precedence` row documents that the plan-frozen `mix_grp` operator drives the composite), `magnitude=FAIL` (mix_grp=0), `regime=VALID` (`U_PMNS` unitary to 1e-15, m₁=0 preserved, real texture self-consistent).

**dual_prior + fb_pair**: FAIL → posterior **0.8 Track B** (lepton WALLED; consistent with the §VII.CK/§VII.BL multiplicity-scalar theorem extending to leptons). `fb_pair.forward` = §VII.CK external-channel mechanism (W2-1) + §VII.BL ε_LX existence (S98-W3-1) + S111-CF-YUK-FULLFLAVOR (quark precedent); `fb_pair.backward` = Wave-2 lepton-shape-leg status (→ WALLED) + the capstone Yukawa §.

**Substrate framing (PARTICLE).** D_K eigenvalues → ε_LX multiplicity-bundle deformation → lepton mass/mixing texture → PMNS. The bare D_K is multiplicity-scalar (generation = Z₃-triality index `t=(p−q) mod 3`, §VII.BL STAGE-3-PERMANENT); the hierarchy + mixing live in the external non-LI ε_LX. The distinguishing substrate feature vs quarks is the **ℂ⊕ℍ fiber asymmetry**: the charged-lepton (ℍ-doublet) and neutrino-Dirac (ℂ-singlet) sectors occupy **DISJOINT Peter-Weyl towers** `[(3,0),(1,1),(1,0)]` (steep `exp(−S0·C2)`) vs `[(0,0),(1,0),(1,1)]` (mild `√C2` + near-degenerate `M_R`). That asymmetry is real but does NOT rescue the mixing: the steep charged-lepton hierarchy *forces* a rearranging ε_LX → θ₁₂ overshoot; the seesaw confines neutrino mixing to the 2-3 block (m₁=0). The PMNS observables are EXTERNAL methodological anchors (`get_constant('J_PMNS')`→not-found, hardcoded `# (local)` NuFIT 5.2 pins, NOT framework constants the gate computes). Direction of explanation flows D_K → ε_LX → texture → PMNS, never the reverse.

**Artifacts**: `computations/session-116/s116_lepton_pmns_texture.{py,npz,png}`.

---

## Wave 2 Synthesis (team-lead)

**Wave 2 closed: 3/3 gates (2 compute verdict lines + 1 workshop artifact-existence; all dual-SHA-unique, 5/5 session SHAs distinct).** Q18b (Yukawa hierarchy) had been driven to its structural walls; this wave closed the two genuine residuals and, on the lepton side, surfaced a higher-order epistemic finding the plan did not anticipate.

**Gate-by-gate.**
- **S116-W2-CK-STAGE2-VERIFY** PASS — the §VII.CK D4 **mechanism corrigendum** (`CF-S116-VIICK-D4-MECHANISM-CORRIGENDUM` DISCHARGED). Single reconciled exclusion mechanism = **commutant/Skolem–Noether leg-membership**: `t(R_X)=0` for all 8 su(3)_R generators (machine-exact, adjoint=(1,1), conjugacy residual 8.06e-17), `R_{E_α}` non-scalar on the multiplicity leg ⇒ ∉ Ω¹_{D_K}(A_K), W3-1 residual=1.000000 readback. The registry's `t(O)=±1` is the **coset-shift grading** (confirmed, slots 1-0-0), NOT the Z₃ center character. D4-external conclusion preserved. **The UNCONDITIONAL flip is NOT triggered here** — connes is the §VII.CK Stage-0 author (excluded from cross-review); the flip is owed to a disjoint-pair blind re-verify (CF below). §VII.CK stays STAGE-3-PERMANENT (D4-open) with the mechanism now RECONCILED.
- **S116-W2-LEPTON-PMNS-TEXTURE** FAIL (`sign=PASS magnitude=FAIL regime=VALID`; composite-precedence: mix_grp operator). The external-ε_LX lepton PMNS texture lands `mix_grp=0/4`: `sin²θ₁₂=0.996` OVERSHOOTS 0.303 (the mass-pinned `U_eL` over-rotates — the lepton `V_us` analog; m_τ/m_μ Casimir=18.0 > PDG 16.82 forces a rearranging ε_LX → near-maximal solar mixing), θ₂₃/θ₁₃ undershoot, `J_PMNS=0` (framework forces δ_CP∈{0,π}; J=0↔δ_CP=180° is CP-conserving-CONSISTENT within NuFIT 3σ). **Deepest finding (under-determination)**: the charged-lepton masses fix the eigen*values* of `M_e`, not its eigen*vectors* ⇒ `U_eL` is FREE ⇒ observed PMNS is reachable at 1.53× minimal `‖ε_LX‖` but the minimal-norm texture gives mix_grp=0 — a **soft** wall (reachable-not-predicted), not a hard exclusion.
- **S116-W2-PMNS-RESCUE** (workshop, closed by artifact-existence). Structural Verdict: **WALLED-AS-UNDER-DETERMINED** (Track B, refined). The adversarial exchange CONVERGED on the structure: connes conceded — value-for-value in Sage — that the seesaw reweighting metric (`M_ν = M_D M_R⁻¹ M_D^T`) is **REAL, parameter-free, spectrum-pinned, and quark-inaccessible** (only the ℂ⊕ℍ fiber admits a Majorana `M_R`; `M_R⁻¹` swings θ_ν 1.43°→82°), while holding the seed `M_D` off-diagonal external ("**metricized external coupling**" — a ruler is substrate-supplied, the vector it measures stays ε_LX). The FAIL is on the metric's **sufficiency** at the framework's near-degenerate B-branch `M_R` (`√(B₂/B₁)=1.036`, too flat to resonate the hierarchical mass-fit seed), NOT on its existence.

**Joint W2-2 × W2-3 reading (Decision-Point matrix).** Track B (workshop) + FAIL (mix_grp≤1) → **WALLED** — a consistent verdict (not the Track-A+FAIL "TENSION→CF-S117" row): the lepton shape leg closes as §VII.CK-walled, the registry's "RESONANT-CONDITIONAL ~2.9×" tag superseded.

**Highest-order finding (the workshop's durable output).** The under-determination reframe applies to BOTH sectors: masses fix eigenvalues not eigenvectors ⇒ `U_eL`/`U_dL` free ⇒ the S111 quark `V_us=0.3107` "prediction" is reframed as a multistart tie-break artifact within the same free family. **Neither sector's mixing is derived.** This is an epistemic-type change to a previously-headlined quark result — but it is routed to VERIFICATION (CF-S117-QUARK-CKM-UNDERDETERMINATION-REEXAM), NOT retroactively applied to the S111 verdict (which stays as-emitted; a workshop observation does not edit a permanent verdict).

**What holds.** The §VII.BL/§VII.CK multiplicity-scalar wall on the GENERATION-INDEX channel is untouched (both agents conceded the bare D_K is generation-blind); the wall this wave softens is on the orthogonal MIXING-SELECTION channel. The CP-conserving SKELETON — real diagonal Casimir charged-lepton tower + real-diagonal spectrum-pinned `M_R` (γ₉-even, generation-diagonal, internal) — is spectrum-forced. **`J_PMNS=0` / `δ_CP∈{0,π}` is NOT a hard KO-dim-6-forced prediction** — DOWN-TAGGED by the S116 W-1 forced-vs-artifact workshop (`sessions/session-116/workshops/s116-jpmns-forced-vs-artifact.md`): KO-dim-6 `[J,D_K]=0` is necessary infrastructure but NOT sufficient (the SM finite triple has KO-dim 6 + `J_F` and is CP-violating; the sector-uniform `J` coexists with measured `J_CKM=3.08e-5≠0`; the KO-dim-6 grading sign `ε″=−1` PROTECTS the γ₉-odd phase; `D_K` self-adjointness fixes the Yukawa prescription). The "KO-dim-6 J-self-conjugacy" justification is STRUCK as a non-sequitur (self-conjugacy is the antilinear `C2·conj(D_K)·C2=D_K`, conjugate-to-conjugate, NOT texture-reality). **Verdict: ANSATZ-ARTIFACT-as-derived; CONDITIONAL-PENDING-CF-W2-1** (spectral-action selection of the off-diagonal `ε_LX`); HARD doubly-dead. `δ_CP∈{0,π}` (`J=0`) remains CP-conserving-CONSISTENT with NuFIT 5.2 NO 3σ now; the live falsifiable content is the TWO-SIDED reading-discriminator (a >3σ `δ_CP` away from `{0,π}` falsifies the real-`ε_LX`/Scenario-A reading and CONFIRMS the §VII.BL-external reading, which generically predicts `δ_CP∉{0,π}`), NOT a one-sided framework falsifier. The A2.2 falsifier-inventory Row #89 re-scope is routed to `mack-cosmic-bridge` (sole writer). The §W2-3 FAIL verdict line is UNTOUCHED (verdict permanence).

**Binding open channel.** `R = Δm²₃₂/Δm²₂₁` (S96 peak 6.87 vs NuFIT floor [17,66]) — the eigenvalue-ratio of the same seesaw composite whose eigenvectors the metric helps; W2-3 left it untested at the mass-fit seed.

### Effected In-Session (NON-MATH — executed at wave-synthesis)

The §VII.CK / falsifier-inventory surfaces are `mack-cosmic-bridge`'s sole-writer domain — routed to mack (in-session designated-writer dispatch), all landings verified on disk by the orchestrator:

- [x] **§VII.CK D4 mechanism corrigendum** (STATUS CONTESTED → **RECONCILED**, W2-1 PASS) — `mack-cosmic-bridge` applied via `replace_all` to BOTH the Four-door D4 table row AND the D4-disposition annotation: `Stage-2-INFO-deferred — D4 mechanism CONTESTED` → `D4 mechanism RECONCILED (S116 W2-1 PASS, audit 63fc7317…); single mechanism = commutant/Skolem–Noether leg-membership; t(O)=±1 = coset-shift grading`. CONTESTED narrative + `t(O)=±1` text RETAINED (audit-trail); **NO UNCONDITIONAL flip** (owed to CF-S117-VIICK-UNCONDITIONAL-REVERIFY) — `sessions/permanent-results-registry.md:22439` + `:22460`. Verified: RECONCILED=2, STAGE tag still STAGE-3-PERMANENT (D4-open).
- [x] **§VII.CK lepton-PMNS annotation** (RESONANT-CONDITIONAL ~2.9× → **WALLED-AS-UNDER-DETERMINED**) — mack RETAINed the S114 reading + appended the supersession (mix_grp=0/4, J=0/δ_CP∈{0,π}, under-determination soft wall, → CF-S117-LEPTON-SEESAW-R-CHANNEL) — `sessions/permanent-results-registry.md:22460`. Verified: WALLED supersession=1.
- [x] **falsifier-master-inventory audit-pin** `Row #89.audit-S116-W2-LEPTON-PMNS-TEXTURE` — mack VERIFIED (not assumed) no existing row carried "~2.9×"; the `J_PMNS=0/δ_CP∈{0,π}` prediction is ALREADY Row #89 ([J,D_K]=0-forced), so landed a light audit-pin sub-row recording the SECOND independent route to J_CP=0 (ε_LX-texture reality) + the mixing-angle UNDER-DETERMINED re-scope + the load-bearing split (CP-phase leg HARD+reinforced; mixing-angle texture NOT a framework prediction — the ~2.9× must NOT be cited as a live PMNS-mixing prediction) — `sessions/framework/registry/falsifier-master-inventory.md:2219`.
- [x] **housekeeping ledger** `session-116-housekeeping.md §A2` (spec, neutrino) + `§A2-LANDED` (mack's landing record, line 66) written; §B–§E confirmed (the math carry-forwards are genuine future computation in the WP `## Carry-Forward Computations` block, not §B hygiene).

**Self-audit (orchestrator)**: WP Effected-In-Session unchecked-box count = 0; the §VII.CK STAGE tag remains STAGE-3-PERMANENT (D4-open) — no unauthorized UNCONDITIONAL flip; sig_5 5/5 distinct session SHAs.

## Carry-Forward Computations

### CF-S117-VIICK-UNCONDITIONAL-REVERIFY — §VII.CK D4 disjoint-pair blind Stage-2 re-verify + UNCONDITIONAL flip (the leading Wave-2-internal CF)

1. **What**: Stage-2 blind cross-axis re-verify of the W2-1-reconciled §VII.CK D4 mechanism (commutant/Skolem–Noether leg-membership) by a DISJOINT compliant pair — Axis-A `lizzi-spectral-functional-theorist` × Axis-B `volovik-superfluid-universe-theorist` (candidate; orchestrator finalizes per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"`). Both read ONLY the registered (corrected) §VII.CK entry — NOT the S112/S114/S115/S116 workshop transcripts, NOT connes (the adjudication author), NONE of the §VII.CK Stage-0 exclusion set {connes, paasch, van-den-dungen, baptista, kaluza-klein}. On clean PASS-AND → `mack-cosmic-bridge` flips §VII.CK STAGE-3-PERMANENT → STAGE-3-PERMANENT-UNCONDITIONAL.
2. **Inputs**: the corrected §VII.CK entry (post-W2-1 corrigendum, this session); `S116-W2-CK-STAGE2-VERIFY` PASS (audit 63fc7317…); `computations/session-114/s114_yuk_rightreg_connection.npz` (W3-1 residual=1.0); `joint-theorem-promotion.md §Stage 2`.
3. **Gate**: PASS-AND (both cross-reviewers independently PASS the single-mechanism joint clause, no prior workshop context) → UNCONDITIONAL flip; FAIL (either axis) → §VII.CK stays STAGE-3-PERMANENT (D4-open), flip re-deferred.
4. **Effort**: ~1 wave (2-agent parallel blind verify; no new compute, registry-read + adjudication). **Depends on**: W2-1 PASS (this session) + the corrigendum registry edit (mack, this session).

### CF-S117-LEPTON-SEESAW-R-CHANNEL — the binding mass-spectrum channel
1. **What**: Compute `R = Δm²₃₂/Δm²₂₁` from the eigenvalues of the SAME seesaw composite `M_ν = M_D M_R⁻¹ M_D^T` used in W2-3 (mass-pinned `M_D`; `M_R` diagonal at B-branch [1.0044, 1.0786, 1.1700]); test the spectrum channel the angle-metric does NOT touch.
2. **Inputs**: `computations/session-116/s116_lepton_pmns_texture.npz` (M_D, M_R, M_ν); B-branch M_R (S100a); NuFIT 5.2 NO R-floor [17,66]; S96 peak R=6.87.
3. **Gate**: PASS if R∈[17,66] at mass-pinned M_D + diagonal B-branch M_R; FAIL if R<17 (S96 shortfall persists); INFO if R lands only by rescaling M_R off bare B-branch.
4. **Effort**: ~1 agent, LOW (re-uses W2-3 npz; eigenvalue-ratio of an existing M_ν). **Depends on**: s116_lepton_pmns_texture.npz; S96 R-residual.

### CF-S117-SEESAW-RESONANCE-MR-SEARCH — is the framework's seesaw ruler ANYWHERE non-flat enough?
1. **What**: Scan substrate-natural `M_R` candidates (B-branch fold energies across τ incl. the τ=0.107 crossing; alternative spectrum-pinned forms incl. diag(M_0,M_1,M_1)) to test whether ANY satisfies the resonance condition `M_D[2,2]/M_D[1,1] ≈ √(M_R[2]/M_R[1])` at the mass-fit seed and fires the enhancement to mix_grp≥3.
2. **Inputs**: `dirac_spectrum.py` B-branch fold energies across τ OR the S100a M_R derivation; mass-fit M_D from s116_lepton_pmns_texture.npz; the resonance condition √(B₂/B₁); NuFIT 5.2 NO 3σ bands.
3. **Gate**: PASS if a substrate-natural (spectrum-pinned, NOT free-tuned) M_R fires mix_grp≥3 at the mass-fit seed; FAIL if no substrate-natural M_R resonates (B-branch structurally too flat across the moduli); INFO if resonance fires only off the fold or at a rescaled M_R.
4. **Effort**: ~1 agent, MEDIUM (τ-scan of B-branch fold energies + per-τ seesaw recompute). **Depends on**: dirac_spectrum.py B-branch; s116 mass-fit M_D.

### CF-S117-QUARK-CKM-UNDERDETERMINATION-REEXAM — the corollary's direct test
1. **What**: Re-examine the `S111-CF-YUK-FULLFLAVOR` `V_us=0.3107` "prediction" under the under-determination lens: is `U_dL` free (masses fix singular values not left singular vectors) so V_us spans an interval at fixed quark masses? Quantify the reachable V_us range and the minimal ‖ε_LX‖ to reach PDG 0.2243 (the quark analog of the lepton 1.53× soft wall).
2. **Inputs**: S111 quark texture {ρ13^d, ρ23^d, |w12^d|, θ_d, Λ_d} + npz; quark mass spectrum; the S111 multistart seed protocol; PDG V_us=0.2243.
3. **Gate**: PASS (under-determination CONFIRMED for quarks) if V_us spans an interval at fixed masses with PDG reachable at non-minimal norm; FAIL (V_us genuinely mass-forced) if uniquely pinned to 0.3107 with no free U_dL family; INFO if the family is constrained but narrow.
4. **Effort**: ~1 agent, MEDIUM (re-run the S111 texture fit with a U_dL-freedom scan). **Depends on**: s111 quark texture npz; the lepton U_eL-freedom construction (W2-3, as method analog).

### CF-W2-1 — is the lepton mixing `U_eL` a FLAT DIRECTION of the spectral action, or does the action LIFT it? [Q-other; NEW genuine compute]

1. **What**: Test whether the lepton mixing `U_eL` is a genuine FLAT DIRECTION of the spectral action `S = Tr f(D_K/Λ)`, or whether the action (or the §VII.BL `dD_K/dε_LX` texture-generating structure) LIFTS it. The W2 "under-determination" frame uses minimal-norm-by-fiat as the "substrate-natural" selector but never derived that the substrate USES minimal norm. If the SA lifts the `U_eL` flat direction, the mixing IS substrate-SELECTED and "under-determined" is an artifact of treating `ε_LX` as a free orthogonal `R`. Should accompany/precede `CF-S117-QUARK-CKM-UNDERDETERMINATION-REEXAM`.
2. **Inputs**: `s116_lepton_pmns_texture.npz` (the W2-3 `ε_LX` texture + U_eL-freedom construction); the spectral action `S = Tr f(D_K/Λ)`; the §VII.BL `dD_K/dε_LX` texture-generating structure.
3. **Gate**: flat ⇒ under-determination CONFIRMED (the mixing is genuinely unpredicted, the W2 frame holds); lifted ⇒ mixing substrate-SELECTED (the "under-determination" frame is an artifact, and the observed PMNS is a framework prediction at the SA-minimizing `U_eL`).
4. **Effort**: ~1 agent, MEDIUM (evaluate `S` over the `U_eL` orbit at fixed lepton masses; test for a non-flat minimum). **Depends on**: `s116_lepton_pmns_texture.npz`; the SA assembly.

### CF-W2-2 — anchor `CF-S117-SEESAW-RESONANCE-MR-SEARCH` on the S-3-derived substrate-forced `M_R` form [Q2-hygiene anchoring; NEW]

1. **What**: ANCHOR `CF-S117-SEESAW-RESONANCE-MR-SEARCH` (above) on the substrate-forced `M_R` form derived by the S-3 solo (`session-116-w2-MR-structure-synthesis.md`, this session's workshop schedule), NOT scan both `M_R` forms and report whichever resonates (a PROHIBITED_ACTIONS Class-1 convention-shopping guard). If S-3 lands a determinate form (multiplicity-leg-degenerate vs fold-spectrum-split), the resonance-search scans ONLY substrate-natural `M_R` forms consistent with it; a resonance that fires only on the NON-S-3 form is INFO, not PASS.
2. **Inputs**: the S-3 solo verdict (`sessions/session-116/session-116-w2-MR-structure-synthesis.md`); `CF-S117-SEESAW-RESONANCE-MR-SEARCH` (above, already-minted).
3. **Gate**: the resonance-search's `M_R` scan is anchored to the S-3 form (no convention-shopping); a PASS that requires the non-S-3 `M_R` form is downgraded to INFO.
4. **Effort**: ~0 compute (an anchoring-pin on an already-minted CF; the S-3 solo supplies the form). **Depends on**: the S-3 solo (this schedule); `CF-S117-SEESAW-RESONANCE-MR-SEARCH`.

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:---------|:-------|
| 2026-06-27 | S116-W2-CK-STAGE2-VERIFY (§VII.CK D4 mechanism) | Stage-2-INFO-deferred (S115) — mechanism CONTESTED (t(O)=±1 vs commutant) | **RECONCILED** — single mechanism = commutant/Skolem–Noether leg-membership; t(R_X)=0 ∀ su(3)_R gens; t(O)=±1 = coset-shift grading | PASS; CF-S116-VIICK-D4-MECHANISM-CORRIGENDUM discharged. UNCONDITIONAL flip owed to disjoint-pair re-verify (CF-S117-VIICK-UNCONDITIONAL-REVERIFY) |
| 2026-06-27 | S116-W2-LEPTON-PMNS-TEXTURE (lepton ε_LX PMNS) | open (RESONANT-CONDITIONAL ~2.9×, S114 bare-circulant) | **WALLED (mix_grp=0/4)** — θ₁₂ overshoot (V_us analog), J=0 (δ_CP∈{0,π}); UNDER-DETERMINED (U_eL free, reachable at 1.53× minimal norm) | FAIL; deformed ε_LX texture does not fire the seesaw resonance at B-branch M_R |
| 2026-06-27 | S116-W2-PMNS-RESCUE (lepton shape leg) | RESONANT-CONDITIONAL ~2.9× (§VII.CK D4-disposition) | **WALLED-AS-UNDER-DETERMINED** — seesaw metric REAL+quark-inaccessible (connes-conceded) but sufficiency-FAILED at near-degenerate B-branch M_R; ε_LX = metricized external coupling | Workshop Track B + W2-3 FAIL joint reading (consistent) |
| 2026-06-27 | (corollary) S111-CF-YUK-FULLFLAVOR quark V_us | "prediction" V_us=0.3107 (headlined) | **under-determination flagged** — likely a multistart artifact (U_dL free); routed to CF-S117-QUARK-CKM-UNDERDETERMINATION-REEXAM for verification (S111 verdict UNCHANGED pending) | Under-determination corollary; NOT retroactively applied to the permanent S111 verdict |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Workshop md |
|:-----|:-------|:------------|:------------|:------------|
| S116-W2-CK-STAGE2-VERIFY | `s116_ck_stage2_verify.py` | `…_ck_stage2_verify.npz` | `…_ck_stage2_verify.png` | — |
| S116-W2-PMNS-RESCUE | — | — | — | `sessions/session-116/workshops/s116-w2-pmns-rescue.md` |
| S116-W2-LEPTON-PMNS-TEXTURE | `s116_lepton_pmns_texture.py` | `…_lepton_pmns_texture.npz` | `…_lepton_pmns_texture.png` | — |

*(Compute scripts/data/plots under `computations/session-116/`. Verdict lines in `computations/session-116/s116_gate_verdicts.txt` — CK-STAGE2-VERIFY PASS, LEPTON-PMNS-TEXTURE FAIL, both dual-SHA-unique.)*
