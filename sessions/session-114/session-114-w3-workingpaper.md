# Session 114 Wave 3 — Fermion / DM / NCG-categorical (Results Working Paper)

**Session**: 114 | **Wave**: 3 | **Plan**: session-114-plan-w3.md | **Theme**: Closing the SHAPE-branch homogeneity-obstruction genus — the D4 right-regular SU(3)_R-connection decider (W3-1) + the D1–D3 §VII permanent-wall landing (W3-3) + the one open dimensionless DM corridor (W3-2 Leggett B2⊕B3 inter-band coherence mode). Fermion-mass SHAPE branch + dark-matter Leggett channel + NCG-categorical obstruction registry.

## Gate Sections

### §W3-1. CF-S114-YUK-RIGHTREG-CONNECTION (connes-ncg-theorist)

**Status**: COMPLETED
**Gate ID**: `CF-S114-YUK-RIGHTREG-CONNECTION`
**Trigger**: `[SIGN]`
**Classification**: **PARTICLE** (the generation index is the SU(3) representation-theoretic content of D_K; discriminator-ii is a sign-changing per-generation eigenvalue pattern across t=0,1,2)
**Agent**: `connes-ncg-theorist`
**Hypothesis**: The right-regular generation operator `Y_R = Σ_a c_a R_{X_a}` on the multiplicity leg `ℂ^{m(p,q)}` is left/G-invariant, sign-changing on the t=0,1,2 generation copies, BDI-reality-compatible (off-diagonal, evading the diagonal J-lock), AND substrate-INTERNAL (a connection on the substrate's own SU(3)_R isometry bundle reachable from (A_K,H_K,D_K,J) without enlarging A_K or dropping Axiom 5) — Reading-A — OR `Y_R ∈ closure(Ω¹_{D_K}(A_K))`, the external ε_LX in new dress, D4 closed — Reading-B. Dual prior 0.40 internal / 0.60 external.
**Plan reference**: `sessions/session-plan/session-114-plan-w3.md` §W3-1 (4-part discriminator spec, machinery pin, substitution chain source, dual-prior re-allocation).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- **Script**: `computations/session-114/s114_yuk_rightreg_connection.py` — present; `grep -E "from canonical_constants import|print_verdict_payload"` → both present (`from canonical_constants import *` line 75; `def print_verdict_payload` + its call in `main()`).
- **Data**: `computations/session-114/s114_yuk_rightreg_connection.npz` — present (per-Cartan-c-family `eig_repr`/`sign_flip` arrays, the three `residual_iv` per triality class, positive-control residuals, `is_external`/`is_internal_candidate`, dual-SHA, verdict fields).
- **Plot**: `computations/session-114/s114_yuk_rightreg_connection.png` — present (left: per-generation representative right-Cartan eigenvalue `c·w(t)` across the 6-member Cartan c-family, circle=sign-flip/square=uniform-sign; right: membership-residual_iv per sector vs the internal/external floors, log scale).
- **Verdict line**: `computations/session-114/s114_gate_verdicts.txt` — `CF-S114-YUK-RIGHTREG-CONNECTION: INFO …` matches `^CF-S114-YUK-RIGHTREG-CONNECTION:.* audit_sha256=[a-f0-9]{64}`; dual-SHA companion row + the `[SIGN]` 3-tuple companion row (`sign=PASS magnitude=INFO regime=VALID`) + 2 extra annotation rows all landed via the race-safe `emit_verdict` MCP tool (5 rows; sig_5-unique, cross-process locked). Full audit_sha256 `e392b832483e8f75c6cbd87086c3a10bfb19f3d242ba9f873de3a9434997d49b` — readable by the downstream W3-3 D4-scope qualifier.
- **WP §W3-1**: this section, carrying Status / Verdict / Output Artifacts / MCP Pre-Compute Audit markers. Verification by content-presence regex, never line/byte counts.

**MCP Pre-Compute Audit**:
- `search_knowledge("right-regular SU(3) generation multiplicity leg Yukawa shape obstruction Generation-Blindness")` → surfaced **§VII.BL Generation-Blindness Obstruction** (STAGE-3-PERMANENT, S99 W3-1; `R_cross=1.019704`), the multiplicity-leg generation id `t=(p−q) mod 3` (`proven_384`, registry line 21124), and `S97-YUKAWA-FAMILY-DERIVE: FAIL` (`1:1:1`, multiplicity-scalar democratic masses). Established the closed context: A_K-built operators are multiplicity-SCALAR ⇒ democratic.
- `search_knowledge("Omega1 D_K inner fluctuation one-form A_K left module Skolem-Noether leg-membership multiplicity scalar")` → surfaced the **(W2) Homogeneity wall** ("left-invariance ⇒ multiplicity-scalar ⇒ the entire differential calculus `Ω¹_{D_K}(A_K) = span{a_0[D_K,a_1]}` is valued in the multiplicity-SCALAR commutant; `ε_LX` MUST BREAK left-invariance on the multiplicity space") and the **Skolem–Noether** lemma (`A_K = ℂ⊕ℍ⊕M₃(ℂ)` has three non-isomorphic simple summands ⇒ every `σ∈Aut(A_K)` is block-inner ⇒ multiplicity-scalar). This is the wall D4 tries to route around with a RIGHT-regular (NOT A_K-built) operator.
- `search_knowledge("VII.BV slope handle crossing sign-changing G-invariant tau derivative wall")` → `S103-NO-SIGN-HANDLE-REGISTRY-LANDING: PASS` (§VII.BV; `uniform_sign=(plus,plus,plus); crossing_realized=False; sign_flip=False`) — the LEFT-regular slope-handle wall. The D4 decider tests a DIFFERENT operator class (right-regular), so §VII.BV does NOT pre-close it.
- `get_constant("tau_fold")` → `0.19` (S12/S42, CONST-FREEZE-42).
- **Sage verification** (`mcp__sage__sage_eval`, A2 WeylCharacterRing): the multiplicity leg of sector (p,q) carries the conjugate irrep (q,p), triality `(q−p) mod 3 = −t(p,q)`; the three generation copies carry distinct right-SU(3)_R weights in distinct triality cosets. Confirmed the (ii) substitution-chain weight structure before coding.
- **Not PRE-CLOSED**: the right-regular SU(3)_R multiplicity-leg construction + the `Y_R ∈ closure(Ω¹_{D_K}(A_K))` membership projection is a NEW compute — §VII.BL/§VII.BV close the LEFT/A_K-built and left-Casimir-slope classes; D4 is the explicitly-OPEN right-regular door per the WS-7 YUKSHAPE §3 D4-row.

**Verdict**: **INFO** (composite). `sign_verdict=PASS`, `magnitude_verdict=INFO`, `regime_verdict=VALID` (collapse rule → INFO). The right-regular Cartan `Y_R` is left-invariant (machine-exact), genuinely sign-changing on the generation index, and **provably NOT in the left A_K-differential calculus** (membership residual = 1.000000 EXACT) — so it is **NOT the external ε_LX "in new dress" (NOT Reading-B/FAIL)**. But it is **generation-DIAGONAL** (center-neutral Cartan, `t(O)=0`), so it does NOT cleanly evade the diagonal J-lock the way an off-diagonal SHAPE handle would (NOT Reading-A/PASS either). Whether the right-regular SU(3)_R fermion action is an admissible substrate DOF is a representation-pinning choice NOT fixed by the 7 NCG axioms ⇒ INFO; dual priors **UNCHANGED**; D4 stays **OPEN** (neither closed-external nor PASS-internal); a representation-pinning workshop is owed.

**Results**:

*Headline.* The four-part discriminator, on the single-τ-slice triple at τ_fold = 0.190 with the LEFT-regular machinery extended to the RIGHT-regular SU(3)_R multiplicity leg:

| Discriminator | Result | Pre-reg criterion | Outcome |
|:--------------|:-------|:------------------|:--------|
| **(i) left/G-invariance** `‖[L_g,Y_R]‖_F` | **7.25e-17** (over rep sectors × 8 generators) | < 1e-12 | **PASS** |
| **(ii) sign-flip on the t-leg** | **sign_flip=True for 4/6 Cartan directions** (every direction with an H_8 component) | boolean: eig_t NOT uniform-sign | **PASS (admissible AND realized)** |
| **(iii) BDI / off-diagonal J-lock evasion** | Cartan `Y_R` is **generation-DIAGONAL** (`t(O)=0`) | off-diagonal to evade the diagonal `d_1=d_2` J-lock | **does NOT evade** |
| **(iv) LOAD-BEARING membership** `‖Y_R − P_Ω¹(Y_R)‖/‖Y_R‖` | **1.000000 EXACT** (all 3 triality classes) | ≤1e-9 external(FAIL) / >1e-3 internal-candidate | **NOT external; internal-candidate** |

*Positive control (proves the (iv) test discriminates):* a genuine `Ω¹` form `a_0[D_K,a_1]` (lifted with `I_leg`) projected onto `span(Ω¹)` returns residual **≤ 1.01e-14** on every tested sector — the membership projector finds it bit-exactly. The right-regular `Y_R` returns residual **exactly 1** on the same projector. The test is not vacuous: it cleanly separates the in-calculus class (residual 0) from the right-regular class (residual 1).

*(i) — left/G-invariance by tensor-factor disjointness.* On `V_{(p,q)} ⊗ ℂ^{m(p,q)}`, `L_g = ρ_left(e_a) ⊗ I_leg` and `Y_R = I_carrier ⊗ R_H`. The commutator `[L_g, Y_R]` vanishes identically because the two operators act on disjoint tensor factors — confirmed numerically at **7.25e-17** (machine zero) across the representative sectors {(1,1),(2,2),(1,0),(2,1),(0,1),(1,2)} and all 8 left generators. This is the standard left-right commutativity of the regular representation (`SU(3)_L × SU(3)_R` on `L²(SU(3))`).

*(ii) — the sign-changing pattern (the SHAPE handle), per Cartan c-direction:*

| c-direction (c3, c8) | eig_t = [t=0, t=1, t=2] | signs | sign_flip |
|:---------------------|:------------------------|:------|:----------|
| H3_only (1, 0) | [−1.0000, −0.5000, −0.5000] | [−,−,−] | False |
| **H8_only (0, 1)** | **[−0.8660, +0.5774, −0.5774]** | **[−,+,−]** | **True** |
| **H3+H8 (1, 1)** | **[−1.3660, −0.7887, +0.7887]** | **[−,−,+]** | **True** |
| **H3−H8 (1, −1)** | **[−1.3660, +0.7887, −0.7887]** | **[−,+,−]** | **True** |
| hypercharge-like (0.5, √3/2) | [−1.0000, −0.5000, −0.5000] | [−,−,−] | False |
| **H3+2H8 (1, 2)** | **[−2.2321, +1.1547, −1.1547]** | **[−,+,−]** | **True** |

The sign-flip is REALIZED for every Cartan direction carrying a nonzero H_8 (hypercharge) component (4 of 6). Pure-H_3 (isospin-z) directions give uniform sign because the representative highest weights happen to align in isospin; hypercharge distinguishes the three triality cosets with opposite signs. The handle is real and is NOT a tuned artifact — it is robust across the structurally-natural BDI-real Cartan family (the c-vector-ROBUST pin is satisfied: the discriminator outcome is reported for the full family, not one c).

*(iii) — generation-diagonal, NOT off-diagonal (the decisive nuance).* The sign-flip in (ii) is **INTER-sector** (comparing the representative right-Cartan eigenvalue of three DIFFERENT sectors, one per triality class). But WITHIN any single sector's multiplicity leg `= conj irrep (q,p)`, EVERY weight shares the SAME triality `(q−p) mod 3` — verified explicitly: leg(1,0)=conj(0,1) all-triality-2, leg(0,1)=conj(1,0) all-triality-1, leg(1,1)=conj(1,1) all-triality-0. So `Y_R` restricted to a leg acts WITHIN one generation class and is block-diagonal across the triality grading — it is **generation-DIAGONAL**. A genuine off-diagonal cross-generation matrix element would need a ROOT generator (`t(O)=±1`), which the center-neutral Cartan combination (`t(O)=0`) does NOT contain. So `Y_R` is reality-compatible but caught by the same diagonal J-lock that pins the reality-locked generation kernel `d_1=d_2` (S99 §4.0) — it does not evade it.

*(iv) — LOAD-BEARING membership, the structural core.* On the full three-factor space `V_{(p,q)} ⊗ ℂ^{m(p,q)} ⊗ ℂ^16`, every `Ω¹_{D_K}(A_K)` form is `(operator on carrier⊗spinor) ⊗ I_leg` (A_K acts LEFT-only on the spinor fiber, IDENTITY on the carrier AND the right-regular leg). The target `Y_R = I_carrier ⊗ R_H_leg ⊗ I_spinor` acts NON-trivially ONLY on the leg. Therefore `Y_R ∈ span(Ω¹)` iff `R_H_leg ∝ I_leg` — but `R_H_leg` is a **traceless** Cartan generator (`Tr R_H_leg = 0` to machine ε, confirmed), so it is never proportional to the identity. The membership residual is **1.000000 EXACT** on every triality class. This is the rigorous statement of why the LEFT differential calculus cannot reach the RIGHT-regular generation leg.

*4-tuple:* `(value='reading=conv-dependent; …; residual_iv=1.000 EXACT; is_external=False; is_internal_candidate=True; posterior=UNCHANGED', scheme=FW, convention=RIGHT-REGULAR-SU3R-MULTIPLICITY-LEG, L_max=10)`.

*Center-character / selection-rule pre-flight (MANDATORY per `math-scripts.md`).* The right-regular Cartan `R_{H_a}` is an SU(3)_R isometry generator (NOT a squared-modulus `|f|²` dressing). Its center character is `t(R_{H_a}) = t(H_a) = 0` (the Cartan torus is in the maximal torus, triality-preserving). Admissibility `t(copy_i) == t(copy_i) + 0 (mod 3)` holds trivially ⇒ the Cartan right-generator CAN act non-zero on each generation copy. The pre-flight PASSES (the sign-changing claim is NOT group-theoretically inadmissible — unlike an A_K-built `|f|²`, which is also `t(O)=0` but is ALWAYS Schur-scalar on the multiplicity commutant; `R_H` is genuinely right-regular, NOT in the A_K-image, so the D1–D3 multiplicity-scalar lock does NOT apply). The pre-flight CONFIRMS admissibility (necessary, not sufficient); the numerical eigenvalue computation (ii) decides the realized sign-flip — and it occurs.

*Substitution chain (discriminator-ii, with substituted numbers — the [SIGN] directional claim):*

- **Step 1 (definitions):** `ℂ^{m(p,q)}` = Peter-Weyl multiplicity leg of sector (p,q), dim = dim(p,q), carrying the conjugate irrep (q,p) under right-translation [dirac_spectrum.py docstring lines 11, 1367-1369; Sage A2 WeylCharacterRing]. `R_{H_a}` = right-regular Cartan generator = `i·ρ_{(q,p)}(e_a)` (Hermitian; real eigenvalues). `eig_t(Y_R)` = right-Cartan eigenvalue-handle on the t-th generation copy. `sign_flip := TRUE iff sign(eig_0), sign(eig_1), sign(eig_2) NOT all equal`.
- **Step 2 (substitution):** `Y_R |t-copy⟩ = (Σ_a c_a R_{H_a})|t-copy⟩ = (Σ_a c_a · w_a(t))|t-copy⟩`, where `w_a(t)` is the a-th right-SU(3)_R Cartan weight of copy t.
- **Step 3 (simplify):** `eig_t(Y_R) = Σ_a c_a w_a(t) = c · w(t)`. The three copies t=0,1,2 carry DISTINCT right-SU(3)_R weights `w(0), w(1), w(2)` in distinct triality cosets [Sage-confirmed: highest-weight Cartan labels of the legs are (1,1)/(1,0)/(0,1) for t=0/2/1 respectively].
- **Step 4 (direction read-off):** for the BDI-real Cartan c-vector with nonzero H_8 component, `c·w(0)=−0.866, c·w(1)=+0.577, c·w(2)=−0.577` (H8_only) — three distinct reals with NON-uniform signs ⇒ sign_flip=True. For pure isospin-H3, signs align (uniform). **Conclusion:** the sign-flip is ADMISSIBLE (center-character pre-flight PASSES; not Schur-locked because `R_H ∉ A_K`-image) AND realized for the H_8-bearing directions — `sign_verdict=PASS` (the predicted "admissible sign-flip" direction matches the computed pattern). The flip does NOT pre-determine the (iv) verdict; (iv) is the load-bearing call.

*Dual-prior posterior re-allocation.* Pre-registration: PASS→0.90 Track-A; FAIL→0.90 Track-B; INFO→priors UNCHANGED. Result = **INFO** (sign-flip holds but membership-iv internal-vs-external resolves to "outside the left calculus AND generation-diagonal", a representation-pinning convention not fixed by the 7 axioms) ⇒ **priors UNCHANGED (0.40 internal / 0.60 external)**, route to a representation-pinning workshop.

*Solution-space interpretation (the boundary this maps).* D4 is the last open door of the SHAPE-branch homogeneity-obstruction genus. The result sharpens it but does NOT close it:
- It RULES OUT the simplest Reading-B reduction: the right-regular `Y_R` is **provably not** the external ε_LX dressed up — residual=1 EXACT shows it is genuinely outside `closure(Ω¹_{D_K}(A_K))`, so the "external in new dress" collapse does NOT happen (FAIL is not the verdict).
- It RULES OUT the simplest Reading-A claim: `Y_R` is generation-DIAGONAL (center-neutral Cartan), so it is not the clean off-diagonal SHAPE handle that would evade the J-lock and supply a 3×3 mixing texture from the substrate's own isometry.
- What survives is a genuinely-open representation-pinning question: a 3×3 cross-generation operator built from the right-regular SU(3)_R would require its ROOT generators (`t(O)=±1`, off-diagonal across triality classes), and whether those right-root generators are admissible substrate fermion couplings — i.e. whether `H_K`'s representation includes the right-regular action on the multiplicity leg as a coupling-eligible DOF without enlarging `A_K` or dropping Axiom 5 — is NOT decided by the 7 NCG axioms. This is the representation-pinning workshop the INFO verdict routes to. **For W3-3**: D4 stays OPEN; the SHAPE-wall §VII entry's scope qualifier remains "{A_K-built ∪ Casimir-graded ∪ γ₉-traced}; the right-regular SU(3)_R connection (D4) is NOT covered and is OPEN" — neither upgraded to unconditional (would require a FAIL = D4 closed) nor scoped to A_K-LEFT-built-only (would require a PASS = internal route named).

---

### §W3-2. CF-S114-LEGGETT-INTERBAND-25P5 (landau-condensed-matter-theorist)

**Status**: COMPLETED
**Gate ID**: `CF-S114-LEGGETT-INTERBAND-25P5`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (Leggett-channel inter-band relative-phase coherence mode = substrate excitation of the BdG fabric)
**Agent**: `landau-condensed-matter-theorist`
**Hypothesis**: There is a Leggett-branch (B2–B3 inter-band relative-phase) BdG coherence mode `ω_Leggett^{B2-B3}` on the FULL B2⊕B3 sector at τ_fold with `ω/Δ_BCS ∈ [24,27]` (corrected target 25.5×, NOT the R1 [12,16]), Z₂-gauge-invariant on the full sector, preserving the Leggett (Z₂-odd, abundance-conserving Ω_DM h²=0.120) identity — Reading-A — OR the only mode at 25.5× is the Higgs amplitude branch (omega_H3/Δ_BCS = 24.70) — Reading-B (FAIL) — OR 25.5× is solely the n_s Wall-W9 transplant with no independent DM free-streaming requirement — INFO (clause-α mis-attribution).
**Plan reference**: `sessions/session-plan/session-114-plan-w3.md` §W3-2 (Z₂ HARD-GATE pre-flight, ω_Leggett closed form, clause-α provenance sub-check, band re-pin substitution chain).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

| Artifact | Path | Verified |
|:---------|:-----|:---------|
| script | `computations/session-114/s114_leggett_interband_25p5.py` | EXISTS; `grep` confirms `from canonical_constants import` + `print_verdict_payload` |
| data | `computations/session-114/s114_leggett_interband_25p5.npz` | EXISTS; carries `gap_Z2`, `omega_Leggett_over_Delta_BCS`, `omega_H3_over_Delta_BCS`, `clause_alpha_is_ns_transplant`, robustness table, 3-tuple |
| plot | `computations/session-114/s114_leggett_interband_25p5.png` | EXISTS; 4-panel (band+Higgs marker / Z₂ pre-flight bars / substitution chain / verdict) |
| verdict_line | `computations/session-114/s114_gate_verdicts.txt` | canonical line `^CF-S114-LEGGETT-INTERBAND-25P5: INFO .* audit_sha256=b6a7727b…` present; dual-SHA companion + **schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple row** present (`[SIGN]` trigger) |
| wp_section | this `### §W3-2.` section | Status COMPLETED / Verdict INFO / Output Artifacts / MCP Pre-Compute Audit all present |

**MCP Pre-Compute Audit** (queries run BEFORE writing the script; gate is NOT pre-closed — it is the open DM dimensionless corridor from the S113 DMMASS SYNTHESIS verdict):

- `search_knowledge("Leggett inter-band coherence mode dark matter mass omega Delta_BCS")` → LEGGETT-MOMENT-70 (PROVEN); `Mass_LeggettDM/Δ_BCS = 11.97` (S70); `Ω_DM h²=0.1200` from the Leggett mode; C11 CONDITIONAL on Γ_grav<H_0. Gate is the OPEN dimensionless sub-question, not pre-closed.
- `get_constant("Delta_BCS")` → `0.4642547394830737` (R-PROTECTED, S70 BCS-GAP-CANONICAL-70).
- `get_constant("omega_H3")` → `11.465` (no PROVENANCE entry; input-only Higgs-amplitude-branch member).
- `get_constant("Mass_LeggettDM_over_Delta_BCS")` → `11.97` (S70 LEGGETT-MOMENT, CONDITIONAL on Γ_grav<H_0).
- `search_knowledge("Z2 gauge invariance wall Josephson J_12 …")` → Wall #11 (S82 W2-11) EXACT on the projected 2-sector/1-bond Josephson subspace; `J_12_over_J_23=19.52` (CASIMIR-JOSEPHSON-52, τ-independent).
- `search_knowledge("n_s Wall-W9 170 transplant m_required 11.85 …")` → `m_required/m_Leggett=170` (n_s structure-formation target, investigation-5 / atlas-spectral-geometer-collab); Wall W9 Convex Combination Theorem (S51).
- `search_knowledge("omega_H3 Higgs amplitude branch 11.465 …")` → `c_Br5_Higgs3 = 11.465307` = "BCS-Higgs amplitude-mode Γ-point" (GL-JOSEPHSON-52); ladder `ω_H1=0.380, ω_H2=1.410 hybrid, ω_H3=11.465 amplitude`. **omega_H3 IS the amplitude branch.**
- `search_knowledge("EFOLD-MAPPING-52 Window-1 …")` → `n_s=0.965 achievable at K<K*=0.087` (Window-1, S51 W2-A); `K_pivot=2.0` (C2) **BROKEN-WITH-LIVE-RESEARCH-PATHWAY**; `z_tr=6.75e29` (22 OOM margin). **Confirms clause-α: the 25.5× is the n_s Wall-W9 number, not a DM requirement.**

**Verdict**: **INFO** — value=`omega_L/Δ_BCS=1.1817_band[24,27]_Z2gap=0.000e+00_omegaH3/D=24.695_clause_alpha=ns-Wall-W9-transplant`; scheme=BLV, convention=FULL-B2B3-SECTOR-LEGGETT-INTERBAND, L_max=10; `audit_sha256=b6a7727b550c816e71aecae7cb0f5172bc93be20890686b6bf441972f75b6fb6`, `content_sha256=4f7ed71a0b288274aace99de54e91b236addcab487b36b9e24f24f3f8f45e821`. Schema-v2 3-tuple: `sign=PASS magnitude=FAIL regime=BREAKDOWN`.

INFO fires via **BOTH** pre-registered sub-outcomes, cascaded in the gating order:
- **(a) INFO-blocked (primary, the HARD gate)** — the Z₂ pre-flight is BLOCKED: on the FULL B2⊕B3 sector at the condensate filling (N_pair=2), `E_GS(s++) = E_GS(s+-) = −2.2382430919` to machine precision, `gap_Z2 = 0.000000e+00`. The inter-band Josephson Z₂ sign is gauge-degenerate on the full sector — wall #11 (S82 W2-11) extends from the projected subspace to the full sector. The [24,27] band is NOT evaluated.
- **(b) INFO-misattribution (corroborating, clause-α)** — the 25.5× target is solely the n_s Wall-W9 transplant; no independent DM free-streaming requirement exists.

The composite is **INFO** (not FAIL) by the plan-frozen-operator precedence (gate-verdicts.md §"Plan-frozen gate-block operator precedence"): plan §W3-2 pre-registers "Z₂-pre-flight: IF NO → INFO-blocked" — an **applicability guard**, where `regime=BREAKDOWN` encodes the gating-prerequisite failure, not a hypothesis-physics breakdown; the disclosure is carried in the `# composite-precedence:` companion row.

**Results**:

PHONONIC. Substrate-IS framing: the substrate IS the BdG fabric; the Leggett mode is an inter-band relative-phase coherence excitation of the B2⊕B3 sector (the substrate DM language — Leggett-channel GGE quasiparticle). Direction: `D_K eigenvalues → B2/B3 band gaps (Δ_2,Δ_3), inter-band pair-transfer J_12, band-edge DOS (n_2,n_3) → ω_Leggett → DM-mass prefactor (Δ_BCS units)`.

**1. Z₂-PRE-FLIGHT (HARD GATE — runs FIRST) — BLOCKED.** On the FULL B2⊕B3 sector (NOT the projected 2-sector/1-bond Josephson subspace), the Leggett inter-band relative-phase observable is Z₂-gauge-DEGENERATE. With the standard chemical-potential subtraction `ξ_k = ε_k − μ` (μ = median over the 7-mode B2⊕B3 sector, matching `s82_w2_11` lines 298–301 — without it the bare positive `ε_k` make the trivial empty vacuum the GS and the test is vacuous), the condensate GS is at N_pair=2 with `E_GS(s++) = E_GS(s+-) = −2.2382430919`, `gap_Z2 = |E_GS(s++)−E_GS(s+-)|/|E_GS(s++)| = 0.000000e+00`. The inter-band Josephson sign `b2b3_sign` (s++ vs s+-) enters H only through pair-hops crossing B2↔B3, and on the s-wave singlet pair-basis this sign is removed by the staggered relabeling `c_k → (−1)^{[k∈B3]}c_k` (a Z₂ rotation of the B3 condensate phase) — so the sign of `J_12` (the quantity that would pump ω_Leggett upward) is gauge-unphysical on the full sector. **Wall #11 (S82 W2-11) extends from the projected subspace to the full B2⊕B3 sector.** The [24,27] band is NOT evaluated → INFO-blocked.

**2. ω_Leggett closed form (computed for completeness; the band is NOT the gating step since Z₂ blocked).** `ω_Leggett² = (4 Δ_2 Δ_3 / J_12)·(n_2⁻¹+n_3⁻¹)⁻¹·γ_12` with substrate D_K inputs:
   - `Δ_2 = Δ_B2 = 0.732026`, `Δ_3 = Δ_B3_s53 = 0.084152` (canonical per-band GL gaps; B3 lies far from the Fermi surface);
   - `J_12 = Σ|V_B2B3| = 0.764146` (the B2↔B3 block of V_phys, inter-band pair-transfer on the FULL sector);
   - `n_2 = 14.0233` (rho_B2_per_mode, fold-enhanced), `n_3 = 1.0`, reduced DOS `(n_2⁻¹+n_3⁻¹)⁻¹ = 0.933437`; `γ_12 = 1.0` (full-coherence baseline).
   
   ⇒ `ω_Leggett² = 0.300995 M_KK²`, `ω_Leggett = 0.548630 M_KK`, **`ω_Leggett/Δ_BCS = 1.1817`**. ED cross-check (relative-number operator `Q_23 = N_B2/4 − N_B3/3` on the full sector, GS at N_pair=2, dim=21, selectivity 5.48): `ω_Leggett(ED)/Δ_BCS = 1.8288`. Robustness across all J_12 ∈ {sum|V|, mean|V|, ‖V‖_F} and Δ_3 ∈ {0.084, 0.176} choices: range `[1.18, 5.92]` — **ALL far below the corrected target 25.5×.** The Leggett relative-phase mode is structurally SOFT (`ω_Leggett ~ O(Δ_BCS)`): the restoring force `ω² ∝ Δ_2Δ_3/J_12` is set by the geometric mean of the gaps, and `Δ_3 ≪ Δ_2` (flat B3 band) keeps it small. The Leggett branch does NOT reach 25.5×.

**3. Band re-pin substitution chain ([SIGN], MANDATORY) — Sage-exact.** Claim: PASS band [24,27] (corrected 25.5×), NOT the R1 mis-targeted [12,16]; the only existing-ladder mode near 25.5× is the Higgs amplitude branch.
   - `m_required = 11.85 M_KK` (n_s SA-Goldstone Wall-W9 target for n_s=0.965 at K_pivot=2.0); `m_Leggett = 11.97·Δ_BCS = 5.557129 M_KK`.
   - `target_factor = m_required/m_Leggett = 11.85/5.557 = 2.132396`.
   - `target_in_ΔBCS = target_factor × 11.97 = 25.524780` ≡ `m_required/Δ_BCS = 25.524780` (the 11.97 cancels exactly; Sage QQ: `EXACT equal? True`) ⇒ corrected target ≈ **25.5× Δ_BCS**.
   - R1 unit-error `170/11.97 = 14.202172` (the [12,16] mis-target: divides an m_G-relative ratio 170 by a Δ_BCS-relative anchor 11.97 — mixing two reference scales; [12,16] EXCLUDES 25.5).
   - `omega_H3/Δ_BCS = 11.465/0.4642547 = 24.695494 ≈ 24.70` — the Higgs-amplitude-branch member, 3.2% below 25.5×, the **WRONG branch** (adopting it re-identifies the DM, forfeits abundance + Z₂-protection → would be a FAIL signature). Step-4 direction read-off: the Leggett branch sits BELOW the band (1.18×); the only near-band mode is the Higgs amplitude branch (24.70×). Direction prediction confirmed (`sign_verdict=PASS`).

**4. CLAUSE-α PROVENANCE SUB-CHECK — CONFIRMED (25.5× is the n_s Wall-W9 transplant, no DM requirement).** From the knowledge MCP ledger: `170 = m_required/m_G = 11.85/0.070 = 169.29` is the n_s SA-Goldstone Wall-W9 number (Convex Combination Theorem, S51 W2-A); `25.5× = m_required/Δ_BCS` is that same Wall-W9 number expressed in Δ_BCS units — NOT a DM scale. `K_pivot=2.0` (C2) is **BROKEN-WITH-LIVE-RESEARCH-PATHWAY**; `n_s=0.965` is achievable at `K < K* = 0.087` (Window-1 / EFOLD-MAPPING-52 escape door). The DM free-streaming horizon `z_tr = 6.75e29` (22 OOM margin above any structure-formation scale) confirms there is NO independent DM structure-formation shortfall. ⇒ `clause_alpha_is_ns_transplant = True`, `dm_freestreaming_requires_255 = False`.

**5. Verdict mapping (per DMMASS verdict §4.2 / §5).** INFO ⇒ **HK-170X-DM is re-scoped/closed as mis-attributed**: the DM mass has no independent shortfall; the n_s 170× lives in its own sector with the documented Window-1 door; the DM ledger loses a phantom gap. (This is landau-r2's leading hypothesis, now CONFIRMED by the compute — both the realizability check (Leggett branch soft at 1.18×, only the Higgs branch near 24.70×) AND the provenance check point the same way.) Settled-regardless facts unchanged: the DM mass MAGNITUDE rides M_KK (permanent-external, S112 CF-S112-MKK-SUBSTRATE-ANCHOR FAIL); the σ_SI=1.299e-63 cm² NULL (Row #79) is anchor-robust (≥26.5 OOM below LZ-2024) and SHARPENS regardless. **This gate does NOT write Row #79 or any atlas falsifier cell — σ_SI NULL is mack-cosmic-bridge's sole-writer domain (`feedback_mack-bridge-role.md`).**

**SIGN/MAGNITUDE/REGIME 3-tuple**: `sign_verdict=PASS` (Step-4 predicted the Leggett branch sits BELOW the band; ω_L/Δ_BCS=1.18 < 24 confirms the direction); `magnitude_verdict=FAIL` (`|1.18 − 25.5| = 24.3 ≫` band width); `regime_verdict=BREAKDOWN` (the Z₂-pre-flight gating prerequisite failed — an applicability guard, not a hypothesis-physics breakdown; INFO-blocked per the plan-frozen-operator precedence). Composite collapses to **INFO** by the plan-frozen operator (`# composite-precedence:` disclosure row present).

**Dual prior posterior**: INFO(clause-α-dissolves) ⇒ priors UNCHANGED on the Reading-A/Reading-B axis (the verdict re-scopes HK-170X-DM out of the DM ledger rather than adjudicating A vs B); landau reads this as "phantom gap removed," mack as "Reading-B vindicated" (per the DMMASS verdict §5 residual-dissent — the dissent is interpretive, not factual).

---

### §W3-3. CF-S114-YUK-SHAPE-WALL-VII-LANDING (gen-physicist)

**Status**: COMPLETED
**Gate ID**: `CF-S114-YUK-SHAPE-WALL-VII-LANDING`
**Trigger**: `[VERIFY-THEOREM]`
**Classification**: **GEOMETRIC** (a spectral-triple obstruction theorem on the fabric; registry-landing WITH the D1 Sage-QQ substrate-physics verification — COMPUTE-class, no allowlist append owed)
**Agent**: `gen-physicist`
**Hypothesis**: The SHAPE-Branch Homogeneity Obstruction theorem registers as a §VII STAGE-1-CANDIDATE permanent-wall entry — on (A_K,H_K,D_K,γ₉,J), NO G-invariant functional in the class {Casimir-graded f(C₂,C₃) / γ₉-graded odd-power trace / γ₉-graded even spectral moment / γ₉-graded A_K-orientation cyclic cocycle} supplies a non-monotone sign-changing per-GENERATION (multiplicity-leg t) scalar — with D1 (`Tr[γ₉D_K^odd] ≡ 0`) machine-exact reproduced (`Tr[γ₉D_K] = Tr[γ₉D_K³] = 0` to machine-ε), and a scope qualifier citing W3-1 for the open D4 right-regular door.
**Plan reference**: `sessions/session-plan/session-114-plan-w3.md` §W3-3 (single-shot AFTER-pattern bridge-landing, D1 substitution chain, companion/differentia tag spec, runtime slot-reroute discipline).

**Output Artifacts** (closure-verification checklist; this is a **registry-landing** gate — its closure is artifact-existence of the §VII entry + the D1 machine-exact reproduction, NOT a numeric value band; mirrors the gate-block `output_artifacts:` YAML). ALL verified on disk:

- `computations/session-114/s114_yuk_shape_wall_vii_landing.py` — EXISTS. `grep -E 'from canonical_constants import|print_verdict_payload|verify_section_matches|write_atomic_with_fsync'` → all four present (`from canonical_constants import *`; `def print_verdict_payload`; `def verify_section_matches`; `def write_atomic_with_fsync_append`). Single-shot AFTER-pattern: `build_body_section + build_master_index_row → write_atomic_with_fsync_append → re_read + verify_section_matches → emit ONE verdict line`.
- `computations/session-114/s114_yuk_shape_wall_vii_landing.npz` — EXISTS (12242 B). Holds `Tr_g9_D_abs=0.0`, `Tr_g9_D3_abs=0.0`, `max_block_anticomm=0.0`, `section_verify_pass=True`, `slot='§VII.CK'`, `L_max_operational=10`, `L_max_plan=10`, `n_sectors_constructed=62`, `n_sectors_total=66`, `skipped_sectors=[(0,9),(9,0),(0,10),(10,0)]`, `exact_identity_proved=True`, dual-SHA.
- `computations/session-114/s114_yuk_shape_wall_vii_landing.png` — EXISTS (48292 B); the four-door D1–D4 status diagram (D1–D3 CLOSED green, D4 OPEN red) + D1 supertrace magnitudes vs tolerance (machine-exact 0 bars).
- `sessions/permanent-results-registry.md` — §VII STAGE-1-CANDIDATE entry LANDED at the runtime-verified next-free slot **§VII.CK** (matched the plan-pinned candidate; master-index frontier was §VII.CJ; NO reroute). Two-surface: master-index table row at line 173 (`| §VII.CK | THM | ... | gen-physicist | 2026-06-23 |`, immediately after the §VII.CJ frontier row — sorted-frontier CA→CJ→CK preserved) AND body section at line 22341 (`### §VII.CK —`). `grep -c '§VII.CK'` → 2. Registry-entry marker checklist (all present in the landed block, `verify_section_matches=True`): `STAGE-1-CANDIDATE`; D1–D3 proof (D1 machine-exact `**D1**`, D2 `[J,D_K]=0` conjugation-evenness `**D2**`, D3 Skolem–Noether leg-membership `**D3**`); LOAD-BEARING scope qualifier `class = {A_K-built ∪ Casimir-graded ∪ γ₉-traced}` + `right-regular SU(3)_R connection (D4) is NOT covered and is OPEN` + `CF-S114-YUK-RIGHTREG-CONNECTION` + audit `e392b832483e`; `STRUCTURAL-ORTHOGONAL-COMPANION` to `§VII.BV` (SIGN) and `§VII.BL` (MAGNITUDE); `NON-PROMOTION-BY-HELD-NUMBER` + `sign-lock`; `5-anatomy` 3-level N/A-with-reason + NON-BINDING Level-2; the two permanent anchors `{γ₉,D_K}=0` (S34/S56) + multiplicity-leg generation id (`proven_384`). gen-physicist is §VII registry sole-writer.
- `computations/session-114/s114_gate_verdicts.txt` — canonical line present, matches `^CF-S114-YUK-SHAPE-WALL-VII-LANDING: PASS .* audit_sha256=[a-f0-9]{64}` (audit `51f411950ae58c74…`, content `7c80f70ba0c42708…`); dual-SHA companion row + section-provenance extra row appended via the race-safe `emit_verdict` MCP tool (3 rows, cross-process locked, sig_5 unique). Schema-v2 3-tuple NOT required (`[VERIFY-THEOREM]` artifact-existence gate; the D1 chain is a zero-identity, not a directional band).
- this WP section `### §W3-3. CF-S114-YUK-SHAPE-WALL-VII-LANDING` — `Status: COMPLETED`, `Verdict: PASS`, `Output Artifacts`, `MCP Pre-Compute Audit` all present.

**MCP Pre-Compute Audit** (queries run before authoring the script, per `.claude/rules/knowledge-index-usage.md`):
- `search_knowledge("SHAPE-Branch Homogeneity Obstruction Yukawa generation gamma9 D_K odd supertrace")` → confirmed the (W2) homogeneity-wall family (`left-invariance ⇒ multiplicity-scalar ⇒ Ω¹_{D_K}(A_K)` valued in the multiplicity commutant), §VII.BL Generation-Blindness (STAGE-3-PERMANENT), `Yukawa tree-level mass generation` PROVEN S62. The SHAPE-branch closed-class theorem (D1–D3) is NOT yet a §VII slot → registration warranted, NOT a rediscovery.
- `trace_entity("Skolem-Noether leg-membership multiplicity-scalar")`, `trace_entity("§VII.BV …")`, `trace_entity("multiplicity-leg generation … proven_384")` → no direct trace hits (these live in registry §VII body text, not the entity index); recovered them by direct `grep` on `permanent-results-registry.md` — §VII.BL at line 21117 (MAGNITUDE companion, NON-PROMOTION-BY-HELD-NUMBER overlay, NON-BINDING Level-2), §VII.BV at line 158 (SIGN companion). This gives the exact companion-citation + the anatomy-N/A-with-reason precedent to mirror.
- `get_constant("tau_fold")` → `0.19` (S12/S42, CONST-FREEZE-42); `list_constants("tau_fold")` confirms canonical. Used `from canonical_constants import *` → `tau_fold` (NOT hardcoded).
- NOT PRE-CLOSED: the §VII registry slot for the SHAPE-branch closed-class theorem does not exist; the D1 machine-exact reproduction is a fresh COMPUTE leg. The frozen Stage-0 §4a text (`ws-s113-7-yukshape-verdict.md`, SHA `5cd77110…` — matches plan pin) is the registration source, transcribed VERBATIM.

**Verdict**: **PASS** — `D1_machine_exact_AND_section_verify`. 4-tuple `(value='D1:Tr[g9D]=0.00e+00_Tr[g9D3]=0.00e+00_anticomm=0.00e+00_exact=True_Lop=10of10_nsec=62of66_slot=§VII.CK_section_verify=True', scheme=FW, convention=VII-STAGE1-CANDIDATE-SINGLE-SHOT-AFTER-PATTERN, L_max=10)`. audit_sha256 `51f411950ae58c74c635d40fa9fb711acdc9b0a172a5959da5cecc710738171f`, content_sha256 `7c80f70ba0c42708a768d7f723598710a95dae2d434a62013103bd5ea6493294`. [VERIFY-THEOREM] artifact-existence gate; NO 3-tuple (the D1 chain is a zero-identity, not a directional band).

**Results**:

**(A) D1 machine-exact verification (the COMPUTE leg).** On the Jensen-deformed triple at `τ_fold = 0.19`, with `γ₉` (Cl(8) chirality, `build_chirality`) lifted to `I_{dim(p,q)} ⊗ γ₉` on each Peter-Weyl sector block of the block-diagonal `D_K = ⊕_{(p,q)} D_pi`:
- `max_{(p,q)} ‖{γ₉, D_pi}‖ = 0.000e+00` — `{γ₉, D_K} = 0` confirmed block-by-block (`{γ₉,γ_a}=0` Cl(8) residual 0.0 ∧ `{γ₉,Ω}=0` residual 0.0; both anticommutators the D1 identity needs).
- `|Tr[γ₉ D_K]| = 0.000000e+00` < 1e-12 (k=0 supertrace, PW-multiplicity-weighted).
- `|Tr[γ₉ D_K³]| = 0.000000e+00` < 1e-12 (k=1 supertrace, PW-weighted).
- **Sage-QQ exact-ring confirmation**: on the minimal anticommuting pair `γ₉=diag(1,−1)`, `D=[[0,d],[d,0]]` over `QQ(sympy)`, `Tr[γ₉ D] = 0` and `Tr[γ₉ D³] = 0` EXACTLY (`identity_proved_exact=True`) — exact rationals rule out a float `1e-16` round-off masquerading as the structural identity. Both traces are EXACTLY 0, not numerically near-0.

**(B) D1 substitution chain** (per `math-scripts.md §"Double-Check Logic Before Compute"`). Claim: `Tr[γ₉ D_K^{2k+1}] ≡ 0` at every τ, every L_max. Step 1 — `{γ₉,D_K}=0` (PERMANENT, S34/S56, the McKean–Singer KO-dim-6 anticommutator). Step 2 — `γ₉ D_K = −D_K γ₉` ⇒ `Tr[γ₉ D_K^{2k+1}] = Tr[(γ₉ D_K) D_K^{2k}] = Tr[(−D_K γ₉) D_K^{2k}] = −Tr[D_K γ₉ D_K^{2k}]`. Step 3 — by cyclicity `= −Tr[γ₉ D_K^{2k} D_K] = −Tr[γ₉ D_K^{2k+1}]` ⇒ `2·Tr[γ₉ D_K^{2k+1}] = 0` ⇒ `Tr[γ₉ D_K^{2k+1}] = 0`. Step 4 — the γ₉-graded odd-power trace is its own additive inverse ⇒ EXACTLY 0, L_max-INVARIANT. **Consequence**: connes's R1 orientation-slope `κ^orient = d/dτ(Tr[γ₉ D_K]) = d/dτ(0) ≡ 0` is an analytic FAIL, NOT an open compute — D1 is CLOSED by the permanent anticommutator.

**(C) Operational-L disclosure** (honest, per `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility"`). 62/66 sectors constructed; `L_max_operational = 10`, `L_max_plan = 10`. The 4 skipped sectors are the pure-symmetric corners `(0,9),(9,0),(0,10),(10,0)` — `irrep_symmetric_power` at `p+q ≥ 9` hits the documented recursive-Casimir construction wall (`(0,8)`/`(8,0)` ≈ 29–35 s each; `(0,9)`/`(0,10)` infeasible within an agent timeslot; ALL mixed `p+q=9,10` sectors build in <1 s). This downgrade is **FAITHFUL and the verdict is UNAFFECTED** because the D1 identity is a **PER-BLOCK exact-zero**: `Tr[(I⊗γ₉) D_pi^{2k+1}] = 0` for EACH `(p,q)` INDEPENDENTLY (by `{γ₉,D_pi}=0`), so the full-spectrum supertrace is a sum of identical zeros — there is NO cross-sector cancellation to verify, and the 4 unconstructed corners contribute exactly 0 by the same argument. The wall is an implementation artifact of recursive Casimir projection, NOT physics; the identity is sector-INDEPENDENT. (The first run at L=10 stalled building (0,9)/(0,10) past the agent timeslot; the corner-skip guard + per-block disclosure is the in-session structural correction, NOT convention-shopping — the convention tag is unchanged, the deviation is disclosed in the verdict value/companion + here.)

**(D) Registry-landing outcome.** Slot **§VII.CK** landed (the plan-pinned candidate; master-index frontier was §VII.CJ; NO reroute — the FAIL-with-remediation branch did NOT fire). Single-shot AFTER-pattern, two-surface: master-index table row (line 173, immediately after the §VII.CJ frontier row — sorted-frontier CA→CJ→CK preserved) AND body section (line 22341). `verify_section_matches = True` — all required markers present and verified by re-read from disk: STAGE-1-CANDIDATE; D1–D3 proof + four-door D1–D4 table (D1–D3 CLOSED, D4 OPEN); scope qualifier `class = {A_K-built ∪ Casimir-graded ∪ γ₉-traced}` with D4 OPEN citing W3-1 (audit `e392b832483e`); STRUCTURAL-ORTHOGONAL-COMPANION to §VII.BV (crossing-slope SIGN) + §VII.BL (hierarchy MAGNITUDE) on the THIRD γ₉/orientation axis (cross-observable co-primary FORBIDDEN per algebra-axis orthogonality K=3); NON-PROMOTION-BY-HELD-NUMBER + sign-lock differentia; 5-anatomy + 3-level N/A-with-reason (intra-pillar obstruction, NON-BINDING Level-2 — clears the HARD-HALT auditor per the §VII.BL/§VII.BV precedent); the two permanent anchors `{γ₉,D_K}=0` (S34/S56) + multiplicity-leg generation id (`proven_384`).

**(E) D2 / D3 (transcribed VERBATIM from the frozen YUKSHAPE §4a Stage-0 text, analytic, no new compute).** D2 — `Tr[γ₉ f(D_K²)]` is γ₉-EVEN (the trace survives) but `f(D_K²)` is a function of conjugation-EVEN `|λ|²` ⇒ by `[J,D_K]=0` (BDI reality, S17a) carries C₂, NOT the conjugation-odd C₃. D3 — every `[D_K, a]`, `a ∈ A_K`, maps into `⊕ B(V_{(p,q)}) ⊗ 1` (Skolem–Noether leg-membership, registry lines 21120/21155, the S110 mechanism); a product of multiplicity-scalars is multiplicity-scalar ⇒ the orientation cyclic cocycle distinguishes SECTORS (LABELING-B, foreclosed) but NOT the `t`-generations (LABELING-A, the operative index).

**(F) D4 scope (open, cites W3-1).** The one door this wall does NOT close is D4, the right-regular SU(3)_R connection `Y_R = Σ_a c_a R_{X_a}`. W3-1 `CF-S114-YUK-RIGHTREG-CONNECTION` (audit `e392b832483e8f75c6cbd87086c3a10bfb19f3d242ba9f873de3a9434997d49b`) closed **INFO**: `Y_R` is OUTSIDE the left A_K-calculus (residual = 1.0 EXACT, escaping D3) but is generation-DIAGONAL — neither closed-external (`ε_LX` re-dress) nor PASS-internal (off-Casimir SHAPE route). D4 is OPEN; the genus is NOT yet complete; this STAGE-1-CANDIDATE wall stays scoped to the closed class. A future session may upgrade it to unconditional ONLY if a subsequent gate discharges D4 definitively.

**Routing notes.** NO §7 / falsifier-inventory edit is owed (the YUKSHAPE §4 routing names that no falsifier row changes while D4 is open; §VII NCG/geometric structural-theorem landing = gen-physicist sole-writer, the §7 falsifier surface is mack-cosmic-bridge's). The Stage-2 cross-axis verify is a FUTURE gate (after W3-1's D4 resolves; Stage-2 verifiers MUST exclude the YUKSHAPE Stage-0 authors connes/paasch + downstream-inheritance successors per `joint-theorem-promotion.md`). The plan-pinned `canonical_constants.py` SHA `9ee1a113…` DRIFTED at runtime to `a4b8b679…` (a sibling S114 gate promoted a constant mid-session); RUNTIME state captured in the dual-SHA per `substrate-first-canonical-sourcing.md §(ii.B)` (audit-correct).

---

## Wave 3 Synthesis (team-lead)

The SHAPE-branch homogeneity-obstruction genus is now 3-doors-closed / 1-door-open, and the DM Leggett corridor's phantom gap is removed. **W3-3 PASS** — §VII.CK "SHAPE-Branch Homogeneity Obstruction" landed STAGE-1-CANDIDATE (D1–D3 closed-class), with D1 machine-exact: `|Tr[γ₉ D_K]| = |Tr[γ₉ D_K³]| = 0` (Sage-QQ exact-ring, the supertrace of an odd operator vanishing by `{γ₉,D_K}=0`); slot matched the plan pin (no reroute); 62/66 sectors constructed (the 4 pure-symmetric corners hit the recursive-Casimir wall, but the D1 identity is a per-block exact-zero so the verdict is unaffected). **W3-1 INFO** — D4 (the right-regular SU(3)_R connection `Y_R`) stays OPEN: `Y_R` is provably outside the left A_K-calculus (membership residual = 1.0 EXACT, so NOT the external ε_LX "in new dress" → not FAIL) but generation-DIAGONAL (center-neutral Cartan, `t(O)=0` → not the clean off-diagonal handle → not PASS); whether the right-root generators (`t(O)=±1`) are admissible substrate fermion DOF without enlarging A_K or dropping Axiom 5 is a representation-pinning choice the 7 NCG axioms do not fix. **W3-2 INFO** — the Z₂ pre-flight BLOCKED on the full B2⊕B3 sector (`gap_Z2 = 0`, wall #11 extends from the projected subspace), `ω_Leggett/Δ_BCS = 1.18` is structurally soft (≪ the 25.5× target), and the clause-α provenance check CONFIRMED the 25.5× is the n_s Wall-W9 transplant (`m_required/Δ_BCS`), NOT an independent DM free-streaming requirement (`z_tr = 6.75e29`, 22-OOM margin) ⇒ HK-170X-DM re-scoped/CLOSED as mis-attributed; the σ_SI NULL (Row #79) sharpens regardless.

### (a) Numerical revisions
- D1 supertrace: `|Tr[γ₉ D_K]| = |Tr[γ₉ D_K³]| = 0.00e+00` (machine-exact + Sage-QQ exact-ring).
- W3-1 (iv) membership residual: `1.000000 EXACT` (all 3 triality classes; positive control ≤1.01e-14 — the test discriminates).
- W3-2: `ω_Leggett/Δ_BCS = 1.18` (robustness range [1.18, 5.92], all ≪ 25.5×); `gap_Z2 = 0.000e+00`; corrected target `25.5× = m_required/Δ_BCS` (Sage-exact).

### (b) Structural changes
- §VII.CK SHAPE-Branch Homogeneity Obstruction: `not-yet-a-§VII-slot → STAGE-1-CANDIDATE landed` (the genus has D1–D3 closed + D4 open; STRUCTURAL-ORTHOGONAL-COMPANION to §VII.BV SIGN + §VII.BL MAGNITUDE on the third γ₉/orientation axis).
- D4 (right-regular SU(3)_R): `the simplest open door → sharpened` — RULED OUT the Reading-B reduction (Y_R is not external-in-new-dress) AND the simplest Reading-A claim (Y_R is generation-diagonal, not the off-diagonal mixing handle); what survives is a representation-pinning question.
- HK-170X-DM: `phantom DM-ledger gap → CLOSED, mis-attributed` (the 25.5× is the n_s Wall-W9 number in Δ_BCS units, not a DM scale).

## Carry-Forward Computations

### CF-S115-VIICK-STAGE2-VERIFY — Stage-2 blind cross-axis verify of §VII.CK (STAGE-1-CANDIDATE → STAGE-3-PERMANENT)

> **Routing note**: Q2-hygiene-promotion per `Investigating-Workshops.md §"Q2"` (mechanical promotion via the `joint-theorem-promotion.md` 4-stage pathway). Mirrored to `session-114-housekeeping.md §B`. NOT a workshop (no adversarial tension — a procedural Stage-2 independent-verify).

> **Why not §A (fix-in-session)**: Stage-2 → 3 promotion REQUIRES two independent cross-reviewers dispatched in parallel on different axes, operating WITHOUT prior workshop context — an orchestrator-direct edit cannot manufacture the independent-agreement evidence (`joint-theorem-promotion.md §"Stage 2"`).

1. **What**: two-agent blind cross-axis independent-verify of the §VII.CK D1–D3 closed-class obstruction theorem; on PASS-AND, promote STAGE-1-CANDIDATE → STAGE-3-PERMANENT (the D4-open scope qualifier is RETAINED — the wall is verified as the closed-class, not upgraded to unconditional).
2. **Inputs**: the §VII.CK registry entry (`permanent-results-registry.md` body §VII.CK + master-index row); W3-3 verdict `audit_sha256=51f411950ae58c74c635d40fa9fb711acdc9b0a172a5959da5cecc710738171f`; the D1 machine-exact reproduction; the permanent anchors `{γ₉,D_K}=0` (S34/S56) + multiplicity-leg generation id (`proven_384`).
3. **Gate**: `S115-VIICK-STAGE2-VERIFY` — PASS = both cross-reviewers PASS-AND on D1/D2/D3 (Axis-A NCG/spectral + Axis-B a structurally-distinct axis), BOTH **excluding connes + paasch** (the YUKSHAPE Stage-0 authors) and their downstream-inheritance successors per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"`.
4. **Effort**: ~1 wave (2 parallel verify agents).

**Workshop seed (route to `/rclab-investigate`, NOT a compute CF)**: the **D4 representation-pinning workshop** (W3-1 INFO) — are the right-root SU(3)_R generators (`t(O)=±1`) admissible substrate fermion DOF *without enlarging A_K or dropping Axiom 5*? This is a genuine adversarial Q1 tension (one reading: admissible-and-substrate-internal ⇒ a 3×3 mixing texture from the substrate's own isometry; the other: requires enlarging A_K ⇒ external), not a compute gate. It is recorded here for the `/rclab-investigate` workshop schedule, NOT as a WP compute CF. **Scheduled** (2026-06-23) as Slot-2 workshop **W-2** in `sessions/session-114/session-114-workshop-schedule.md` (`van-den-dungen-bridge-theorist` × `baptista-spacetime-analyst`, 2 rounds; connes + paasch excluded as YUKSHAPE Stage-0 authors).

### CF-S115-HK-1 — EVOI frontier-row add: D4 right-root SU(3)_R admissibility as a decidable frontier item (sagan-owned, plan-time maintenance)

> **Routing note**: Q2-hygiene EVOI-table maintenance per `Investigating-Workshops.md §"Q2"` (a frontier-row add is plan-time maintenance, NOT a workshop output). Surfaced by `/rclab-investigate` (W3 seed cross-wave flag) as a NEW item not yet captured at this resolution. Owner: `sagan-empiricist` at `/rclab-plan` S115 (EVOI-table sole maintenance per `evoi-prioritization.md`). NOT a compute gate — no verdict line; this is an EVOI `§EVOI` frontier-row insert.

1. **What**: add an EVOI frontier row for **D4 — right-root SU(3)_R fermion-coupling admissibility under the 7 NCG axioms** (substrate-internal mixing texture vs A_K-enlargement / Axiom-5-drop). The current EVOI version-history (line 7) + lines 134/189 track the SHAPE branch only at the coarse level "SHAPE branch lives outside the Casimir-graded calculus" + the ε_LX between-generation HELD-number (`NON-PROMOTION-BY-HELD-NUMBER`); the S114 W3-1 INFO SHARPENS this to a specific, named, decidable open question NOT yet a frontier row at that resolution.
2. **Inputs**: the W3-1 INFO verdict (`CF-S114-YUK-RIGHTREG-CONNECTION`, audit `e392b832483e8f75c6cbd87086c3a10bfb19f3d242ba9f873de3a9434997d49b`); the dual prior 0.40 internal / 0.60 external (the elicited P(pass) seed for the row); the W-2 workshop verdict (the discriminating test) when it lands.
3. **Gate**: N/A — this is an EVOI-table frontier-row insert, not a PASS/FAIL compute. The "gate" is the W-2 workshop verdict, which the row keys on as its discriminating test.
4. **Effort**: minutes-scale (a single EVOI-table row insert at `/rclab-plan` Step 1c-REGISTERS); sagan-owned, NOT a compute wave.

### CF-S115-VIICK-D4-DISCHARGE-UNCONDITIONAL — Stage-2 cross-axis verify of the D4 external-coupling discharge (§VII.CK STAGE-1-CANDIDATE → STAGE-3-PERMANENT-UNCONDITIONAL)

> **Routing note**: Q2-hygiene mechanical promotion (`joint-theorem-promotion.md §"Stage 2"`). Mirrored from `sessions/session-114/workshops/w-2-d4-rightreg-su3r-admissibility.md §"Carry-Forward Computations" CF-1` (back-filled at S114-close per the no-technical-debt rule; the W-2 workshop finalized AFTER this WP's CF section). **Same-slot relationship**: shares the §VII.CK slot with `CF-S115-VIICK-STAGE2-VERIFY` (above) but verifies a DIFFERENT clause — STAGE2-VERIFY promotes the D1–D3 closed class (D4-open RETAINED); this gate discharges the FOURTH door (D4). Register both as distinct gates; do NOT conflate. Sequencing: STAGE2-VERIFY (closed-class, D4-open) → D4-DISCHARGE (re-scope to D4-CLOSED-UNCONDITIONAL).

1. **What**: blind two-agent cross-axis independent-verify (per `joint-theorem-promotion.md §"Stage 2"`) of the D4-external JOINT clause — "the right-regular `R_{E_α}` SHAPE handle is external-as-a-coupling (admissible only via the canonical crossed product `A_K ⋊ SU(3)_R` / Kasparov external product, outside `Ω¹_{D_K}(A_K)` by the `t(O)=±1≠0` center-character selection rule), discharging D4 CLOSED-EXTERNAL-AS-A-COUPLING and completing the homogeneity-obstruction genus as a statement about `A_K`-internal couplings." On Stage-2 PASS-AND: §VII.CK re-scoped to the COMPLETE genus; tag STAGE-1-CANDIDATE → STAGE-3-PERMANENT-UNCONDITIONAL.
2. **Inputs**: the registered §VII.CK entry (D1–D3 closed class + D4 row, `permanent-results-registry.md`) + W3-1 residual = 1.000000 EXACT (audit `e392b832483e8f75c6cbd87086c3a10bfb19f3d242ba9f873de3a9434997d49b`) + the `t(O)=±1≠0` center-character selection rule (W-2 Re:V1) + the commutant argument (W-2 Re:V2) + `proven_384` (`t=(p−q) mod 3`). Reviewers receive ONLY the registered entry + these inputs — NOT the W-2 transcript.
3. **Gate**: `S115-VIICK-D4-DISCHARGE-UNCONDITIONAL` — PASS-AND across BOTH axes (logical AND). Axis-A (NCG/spectral-functional NON-AUTHOR): `lizzi-spectral-functional-theorist` OR `spectral-geometer` (audits the `Ω¹_{D_K}(A_K)`-membership / selection-rule leg). Axis-B (substrate-geometry NON-AUTHOR, §VII.BL-NON-inheriting): `volovik-superfluid-universe-theorist` (audits the isometry-vs-coupling / commutant / crossed-product-image leg). EXCLUDED: {connes-ncg-theorist, paasch-mass-quantization-analyst (YUKSHAPE Stage-0)} ∪ {van-den-dungen-bridge-theorist, baptista-spacetime-analyst (W-2 authors)} ∪ {kaluza-klein-theorist (§VII.BL reviewer-of-record + co-author, downstream-inheritance reach)} ∪ any §VII.BL/§VII.CK/WS-C2COSET downstream-inheritance successor.
4. **Effort**: ~1 wave (2 parallel cross-reviewers + 1 PASS-AND closeout). **Depends on**: independent of CF-S115-LEPTON-PMNS-FORCED-TEXTURE; shares the §VII.CK slot with `CF-S115-VIICK-STAGE2-VERIFY` (see Routing note for sequencing).

### CF-S115-LEPTON-PMNS-FORCED-TEXTURE — lepton-resonance test of the named external crossed-product corridor

> **Routing note**: Compute carry-forward. Mirrored from `sessions/session-114/workshops/w-2-d4-rightreg-su3r-admissibility.md §"Carry-Forward Computations" CF-2` (back-filled at S114-close per the no-technical-debt rule). A REAL gate, not a note: the W-2 verdict made the lepton resonance STRUCTURAL-conditional (gated on the `ℂ⊕ℍ` charged-lepton-vs-neutrino sector-asymmetry), not numerological. CONTINGENT on the external crossed-product enlargement being realized — it tests the NAMED external corridor, NOT a substrate-internal prediction.

1. **What**: construct the `A_K ⋊ SU(3)_R` right-regular circulant on the LEPTON multiplicity sector, impose the `ℂ⊕ℍ` charged-lepton-vs-neutrino sector-asymmetry (right-regular circulant on the neutrino/seesaw structure, coset-diagonal charged-lepton mass basis), compute the physical misalignment `U_mix = U_L^† U_R`, and test the forced tri-maximal `|U_ij|² = 1/3`, `J = 1/(6√3)` against observed PMNS `J ≈ 0.033`, `δ_CP` AFTER the charged-lepton correction. Pre-register: forced-and-surviving ⇒ zero-(mixing)-parameter prediction of the named external corridor; forced-and-washed-out ⇒ down-tag the lepton resonance to a symmetric-limit coincidence.
2. **Inputs**: B2 Sage-exact forced circulant (`|U_ij|² = 1/3`, `J = 1/(6√3)`, `arg(w) = 2π/3`) + the W-2 sector-misalignment result (two circulants ⇒ `U_mix = identity`; one-circulant-one-coset-diagonal ⇒ tri-maximal, Sage-confirmed) + the `ℂ⊕ℍ` lepton-sector structure of `A_K` + observed PMNS `J`/`δ_CP` (PDG).
3. **Gate**: `S115-LEPTON-PMNS-FORCED-TEXTURE` — `|J_forced − J_PMNS,observed| / J_PMNS,observed` after charged-lepton correction, against a pre-registered band (PASS if the corrected forced texture lands within the PMNS 3σ tri-maximal-deviation window; FAIL/down-tag otherwise). Negative control: the same machinery on `M₃(ℂ)`-shared quark chiralities MUST give `U_mix → identity` ≠ CKM (already established structurally, B2/Q3).
4. **Effort**: ~1 wave; routes through `neutrino-detection-specialist` (PMNS owner) and/or `gen-physicist` for the circulant construction. **Depends on**: B2 + W-2 Q3 sector-misalignment Sage result; INDEPENDENT of `CF-S115-VIICK-D4-DISCHARGE-UNCONDITIONAL` (that gate closes the genus; this one tests the corridor's residue).

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:--|:--|:--|:--|:--|
| 2026-06-23 | W3-3 §VII.CK | not-yet-a-slot | **STAGE-1-CANDIDATE** (PASS, D1 machine-exact) | SHAPE-branch D1–D3 closed-class wall landed; D4-scoped |
| 2026-06-23 | W3-1 D4 right-regular door | open (simplest reductions live) | **INFO** — open, both simple reductions ruled out | Y_R outside left A_K-calculus (residual=1.0) but generation-diagonal |
| 2026-06-23 | W3-2 HK-170X-DM | phantom DM-ledger gap | **CLOSED** — mis-attributed (n_s Wall-W9 transplant) | Z₂ blocked + ω_Leggett soft + clause-α confirmed |

Process observations: §VII.CK landed gen-physicist-sole-writer (registry §VII NCG/geometric structural-theorem domain); NO §7 / falsifier-inventory edit owed from W3-3 (D4 open). W3-2 σ_SI Row #79 sharpen + HK-170X-DM re-scope routed to mack (sole-writer; see `session-114-housekeeping.md §A8`). The 62/66-sector operational-L downgrade is faithfully disclosed (per-block exact-zero, no cross-sector cancellation).

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Registry/verdict |
|:--|:--|:--|:--|:--|
| W3-1 | `s114_yuk_rightreg_connection.py` | ✓ | ✓ | INFO (`e392b832…`) |
| W3-2 | `s114_leggett_interband_25p5.py` | ✓ | ✓ | INFO (`b6a7727b…`) |
| W3-3 | `s114_yuk_shape_wall_vii_landing.py` | ✓ | ✓ | PASS (`51f41195…`) + §VII.CK registry entry |
