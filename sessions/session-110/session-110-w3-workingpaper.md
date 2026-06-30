# Session 110 Wave 3 — M_KK-value + compact-object + Yukawa + d_s (Results Working Paper)

**Session**: 110 | **Wave**: W3 | **Plan**: session-110-plan-w3.md | **Theme**: the framework's one dimensionful axis — the §VII.BS rank-1 NNU keystone weight w=M_KK seen from five sides (gauge-a₄ self-consistency, compact-object EoS + anchor-free falsifier, Yukawa internal-coset vs external-ε_LX, M⁴-base spectral dimension). Substrate-first throughout: the substrate IS the spectral triple `(A_K, H_K, D_K(τ))`; M_KK is the multiplicative weight on every dimensionful observable.

## Gate Sections

### §W3-1. S110-CF-CV2B-GAUGE-A4 (spectral-geometer)

**Status**: COMPLETED
**Gate ID**: `S110-CF-CV2B-GAUGE-A4`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (gauge a₄ inner-fluctuation self-consistency root; 3-way M_KK fork)
**Agent**: `spectral-geometer`
**Hypothesis**: `1/g²(M_KK)` from `Γ_1loop = −½ζ'_{D_K}(0,τ)` projected onto Tr F² THROUGH the SU(A_F)=ℂ⊕ℍ⊕M₃(ℂ) inner-fluctuation algebra (NOT the fiber Peter-Weyl tower — the W1-3 error S96 corrected), matched to (α_em, sin²θ_W, α_s) at m_Z, has a self-consistency root μ* that 3-way-forks the canonical M_KK: Fork-A μ*≈M_KK_gravity ⇒ OVER-DETERMINED; Fork-B μ*≈M_KK_kerner ⇒ §VII.BS fixed-internal; Fork-C no root / scheme-runaway ⇒ ONE-ROUTE-DOMINATES (gravity-a₂ sole canonical).
**Plan reference**: `sessions/session-plan/session-110-plan-w3.md` §W3-1 (machinery pin, fork bands, substitution chain source).

**Output Artifacts**:
- `computations/session-110/s110_cf_cv2b_gauge_a4.py` — present; `grep` confirms `from canonical_constants import` AND `print_verdict_payload` (def + call). PASS
- `computations/session-110/s110_cf_cv2b_gauge_a4.npz` — present (15670 bytes); verdict key `fork=Fork-C verdict=FAIL`, `mu_star_primary=4.4216e+13`, `scheme_spread_oom=167.107`, `root_in_window_primary=False`. PASS
- `computations/session-110/s110_cf_cv2b_gauge_a4.png` — present (121161 bytes); left panel = `1/g²` substrate-horizontal vs SM-RG-rising with the three convention crossings + the two fork targets + scan window; right panel = fork-verdict text card. PASS
- Verdict line in `computations/session-110/s110_gate_verdicts.txt` matching `^S110-CF-CV2B-GAUGE-A4:.* audit_sha256=[a-f0-9]{64}` + dual-SHA companion row + 2 extra companion rows (regulator_pin + fork summary). PASS
- This WP section satisfies the four `wp_section.must_contain` regexes (Status COMPLETED / Verdict FAIL / Output Artifacts / MCP Pre-Compute Audit). PASS

**MCP Pre-Compute Audit**:
- `get_constant(M_KK_gravity)` → 7.428660036284456e16 GeV (S42, CONST-FREEZE-42) — Fork-A target.
- `get_constant(M_KK_kerner)` → 5.041679838376001e17 GeV (S42, CONST-FREEZE-42) — Fork-B target.
- `get_constant(a_4_FW_zeta)` → 1350.7216 (S75/S88, Yang-Mills Tr F² moment; regulator a_4^{ζ}).
- `get_constant(a_2_FW_zeta)` → 2776.165389 (S88, gravity channel).
- `get_constant(alpha_s_MZ_obs)` → 0.118 (PDG); `M_Z`=91.1876; `sin2_thetaW_MSbar`=0.23122; `alpha_em_MZ_inv`=127.955; `f_0_sharp`=1.0 (S78).
- `search_knowledge("CV2B gauge a_4 inner fluctuation … fork")` → surfaced **(W3) Inner-fluctuation impotence** (PROVEN, permanent-results-registry): every `A_K`-built form (inner `A=Σaᵢ[D_K,bᵢ]`, twisted-inner, opposite `JAJ⁻¹`) is **multiplicity-scalar** — the algebra this gate projects onto. NOT pre-closed for the fork (the gauge-coupling self-consistency root is a new computation), but the impotence theorem is the structural prior consistent with the Fork-C outcome.
- `search_knowledge("f0 normalization … 1/g2 = f0 a4 …")` → **S76 W2-B** `a_4` normalization output (`1/g_YM² = f₄·a_4/(2π²)`, unification `f₄·g₀²/(12π²)=1`) + **S70** `s70_f0_alpha_s.py` (`α₃(tree)=2π²·f₀/a_4`, framework SU(3)_c form `1/g₃²=a_4/(8π³·f₀)`; S70 verdict FAIL: α_s tops at 0.0261 tree / 0.0134 with KK threshold, factor ~5.4× below 0.118). These are the source of the substrate-side normalization.
- `trace_entity("ONE-ROUTE-DOMINATES")` → no direct entity; the inv-6 W4-1 verdict is the Track-B prior cited in `dual_prior`.

**Verdict**: **FAIL** (Fork-C, ONE-ROUTE-DOMINATES). `value='fork=Fork-C_mu_star=4.4216e+13GeV_mu_over_Mgrav=0.0005952_scheme_spread=167.1OOM_root_in_window=False'`.
Dual-SHA: `audit_sha256=07aa755a7e4648c578dd2c8dbe1ef0a435a34da9ed8ae95a99970b1edcd19126`, `content_sha256=a8653e3225bf78b5d8d2f22a938fbff4936522345bdeaabdcf3835abb9aebe51`.

**Results**:

**The 3-way fork outcome — Fork-C (FAIL): the gauge-a₄ channel does NOT independently fix M_KK.** Two independent pre-registered Fork-C triggers both fire:

1. **No real root in the scan window [1e15, 1e18] GeV.** Under the framework-canonical normalization (S70 SU(3)_c summand form, f₀=1) the self-consistency root is **μ* = 4.422 × 10¹³ GeV** (4 sig figs), a factor **1680× below M_KK_gravity** (`μ*/M_grav = 5.952×10⁻⁴`, `|μ*/M_grav − 1| = 0.9994 ≫ 0.02`; `|μ*/M_kern − 1| = 0.9999`). The root sits two orders of magnitude *below* the window floor — neither fork target, and not even in the bracketing window.
2. **Cross-scheme spread = 167.1 OOM** ≫ the 1-OOM Fork-C ceiling. The three Chamseddine-Connes normalizations of the substrate `1/g²_sub` produce μ* spanning **6.4 GeV → 8.2×10¹⁶⁷ GeV**: `a_4/(8π³f₀)`→4.42e13, `a_4/(2π²)`→8.15e167, `2f₀/π²`→6.38 GeV. The substrate's a₄ channel carries **no scheme-invariant prediction** for the gauge coupling.

**4-tuple**: `(value='fork=Fork-C_mu_star=4.4216e+13GeV_mu_over_Mgrav=0.0005952_scheme_spread=167.1OOM_root_in_window=False', scheme=zeta-regulated-one-loop-spectral-action Λ_UV=μ=M_KK, convention=ABSOLUTE-1/g²-inner-fluctuation-AF-projector; poleconv-A-double (a_4 n=4, s=2); SU(3)_c on M₃(ℂ), L_max=12)`.
**regulator_pin companion row**: `a_4^{ζ}` poleconv-A-double, (pole_in_s=2, curvature_grade_n=4).

**Substitution chain (at-most-one-root monotonicity, with substituted numbers)** — per `math-scripts.md §"Double-Check Logic Before Compute"`:
- **Step 1 (substrate side, μ-INDEPENDENT):** `1/g²_sub = a_4/(8π³·f₀)` [S70 line 28; SU(3)_c = M₃(ℂ)-summand projection of the a₄ inner-fluctuation 1-form] = `1350.7216/(8π³·1) = 5.4454`. Yang-Mills Tr F² is classically scale-invariant ⇒ `d(1/g²_sub)/d(ln μ) = 0` (a horizontal line). Cross-anchor: the inv-6 W2-1 one-loop machinery's `lambda_induced_fold = 1350.7216 == a_4_FW_zeta` bit-for-bit (the a₄ moment of `Γ_1loop = −½ζ'_D(0,τ)` equals the zeta-Seeley-DeWitt a₄).
- **Step 2 (SM-RG side, log-linear in μ):** `1/g₃²(μ) = 1/g₃²(m_Z) − (b₃/4π²)·ln(μ/m_Z)`, GUT-normalized `g²=4π·α`, `1/g₃²(m_Z) = 1/(4π·0.118) = 0.6744`, `b₃ = −7`. Evaluated: `1/g₃²(M_grav) = 6.7622`, `1/g₃²(M_kern) = 7.1017` — the SM coupling is logarithmically FLAT across 15 decades (rises only 0.674 → 7.10).
- **Step 3 (self-consistency):** `Δ(μ) = 1/g²_sub − 1/g²_RG(μ)`. `1/g²_sub` const in ln μ; `1/g²_RG` monotone-increasing in ln μ (b₃<0). ⇒ `Δ(μ)` strictly monotone-decreasing in ln μ ⇒ **AT MOST ONE root** (numerical witness: `monotone_decreasing=True`, `sign_changes_in_window=0` — the unique root falls *below* the window). The fork classification is therefore well-posed.
- **Step 4 (read off):** μ* = `m_Z·exp((1/g²_mZ − 1/g²_sub)·4π²/b₃)` = `91.19·exp((0.6744−5.4454)·4π²/(−7))` = **4.422×10¹³ GeV**. No direction was pre-asserted as PASS; the computed fork-band is the verdict.
- **Step 5 (conclusion):** ≤1 root by Step-3 monotonicity ⇒ well-posed; the unique root populates *neither* fork target *and* the scheme-spread is 167 OOM ⇒ **Fork-C**.

**Physics reading (substrate-first).** GEOMETRIC. The arrow `D_K eigenvalues → a₄ Seeley-DeWitt coefficient of Tr f(D_K/Λ) → Yang-Mills 1/g² → unification matching → the M_KK weight`. The gauge a₄ channel is **dimensionless** (Tr F² is scale-invariant) — it has no power-law lever on M_KK. Contrast the gravity a₂ channel, which fixes M_KK through the **dimensionful** `M_Pl² = f₂·M_KK²·a₂` (a power law in M_KK, hence a unique root tautologically at M_KK_gravity — confirmed by the inv-6 W2-1 cross-anchor: a₂-channel `root_count=1`, `M_root=7.4287×10¹⁶ = M_KK_gravity` by construction). The a₄ crossing scale is exponentially sensitive to the unfixed f₀/f₄ Mellin-moment normalization, which is precisely why it cannot independently fix the keystone. This is the substrate signature of **ONE-ROUTE-DOMINATES**: the rank-1 §VII.BS NNU wall says only dimensionless ratios Ô are derivable; the single dimensionful weight w = M_KK is one irreducible external import, fixed once by the gravity a₂ moment, not over-determined by the a₄ moment. Consistent with the PROVEN **inner-fluctuation impotence** theorem (every A_K-built form is multiplicity-scalar) and the inv-6 W4-1 ONE-ROUTE-DOMINATES verdict.

**dual_prior posterior reallocation.** Fork-C realized (no root in window AND scheme-runaway) ⇒ per the pre-registered discriminator, **0.9 mass to Track B** (ONE-ROUTE-DOMINATES; gravity-a₂ stays sole canonical). Track A (gauge channel over-determines M_KK) is closed by this gate. The pre-registered priors were Track A 0.45 / Track B 0.55; posterior ≈ Track A 0.10 / Track B 0.90.

**fb_pair backward-consumer note.** Per `fb_pair.backward`: the atlas-04 M_KK cell + §VII.BS support-row (W0 HK-MKK / HK-SCOPED-VIIBS) MUST NOT up-tag M_KK to "derived" — this gate CONFIRMS the gauge channel does not derive it. The canonical M_KK cell stays gravity-a₂, frozen-since-S42. The CV2A (W2) BCS-transmutation PASS (Question A, derivation-*in-principle*) is read against this Fork-C: CV2A's OOM-distance is a *transmutation-corridor* result, NOT a second independent fix of the value. Downstream consumers of the canonical M_KK value (A_s prefactor (M_KK)², CC magnitude) continue to inherit the single gravity-a₂ import; the recurring sign-PASS/magnitude-FAIL pattern is the one keystone weight seen from many sides, NOT a multiply-determined quantity.

**Cross-checks logged**: inv-6 W2-1 `lambda_induced_fold == a_4_FW_zeta` (a₄ one-loop = zeta-SDW, bit-for-bit); L12 cache loaded (90 sectors, max_pq_level=12), a₄ Friedrich-Bär saturated at L_max=12 (new (p,q) sectors above L=12 land at `|λ| ~ √C₂(p,q)` far above the a₄ bulk weight ⇒ zero added resolution — the L_max pin rationale).

**Plan-text-drift corrections** (per `substrate-first-canonical-sourcing.md §(ii.B)`, documented in script stdout): (a) plan path `inv6_w2_1.npz` → actual `inv6_w2_1_gamma_tau_oneloop_trajectory.npz` (the inv-6 W2-1 one-loop gauge-coefficient machinery; plan-prose head `b8cc01fc`, runtime full head `e929b54a`); (b) plan path `computations/_shared/s84_spectrum_cache_L12_tau019.npz` → actual `computations/session-84/s84_spectrum_cache_L12_tau019.npz` (known doc bug; runtime head `9e6d9cf7`).

**Artifacts**: `s110_cf_cv2b_gauge_a4.py` / `.npz` / `.png`.

---

### §W3-2. S110-CF-CO1-EOS (nazarewicz-nuclear-structure-theorist)

**Status**: COMPLETED
**Gate ID**: `S110-CF-CO1-EOS`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (self-consistent finite-μ CFL EoS → TOV M_max + compactness)
**Agent**: `nazarewicz-nuclear-structure-theorist`
**Hypothesis**: a self-consistent finite-μ CFL EoS — μ_eff adjusted WITH density (not the fixed-floor scan that ran Δ/μ→4.82 and closed inv-13 W2-1) with a physical pairing-window narrowing forcing Δ/μ→O(0.1) — stiffens M_max into [2.0, 2.6] M_⊙ WITHOUT tuning and, fed into the inv-11 Lobo-DE interior, fixes C_max ≳ 1e-3 and a physical M(R). Single binding magnitude gap for the whole compact-object assembly. **Sign pre-registered PASS** (stiffens + dΔ_CFL/dμ>0 retained); the magnitude band is the open question.
**Plan reference**: `sessions/session-plan/session-110-plan-w3.md` §W3-2.

**Output Artifacts** (closure-verification, content presence by regex per `feedback_max-effort-full-fidelity.md` — never line/byte counts):
- `computations/session-110/s110_cf_co1_eos.py` — PRESENT (55288 B); `grep` confirms `from canonical_constants import` (line 84) AND `print_verdict_payload` (def + call) PRESENT.
- `computations/session-110/s110_cf_co1_eos.npz` — PRESENT (21453 B); keys incl. `mu_traj`, `Delta_traj`, `ratio_traj`, `M_max_Msun`, `C_max_pinned`, `P_c_at_Mmax_MeV_fm3`, dual-SHA.
- `computations/session-110/s110_cf_co1_eos.png` — PRESENT (180514 B); 4-panel (gap vs μ_eff / Δ/μ runaway-fix / TOV M-R / interior C_max feed-through).
- Verdict line in `computations/session-110/s110_gate_verdicts.txt` — PRESENT, matches `^S110-CF-CO1-EOS:.* audit_sha256=[a-f0-9]{64}` (`audit_sha256=66045cb872c43defdc7f87150aeb31b4d3b3a6cf397f9ba98873da25eb10900e`) + dual-SHA companion row + **schema-v2 sign/magnitude/regime 3-tuple row** (`[SIGN]`; `# sign_verdict=PASS magnitude_verdict=INFO regime_verdict=MARGINAL`) + 3 extra annotation rows.
- This WP section — satisfies the four `wp_section.must_contain` regexes (Status COMPLETED / Verdict / Output Artifacts / MCP Pre-Compute Audit).

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script, per `.claude/rules/knowledge-index-usage.md`):
- `search_knowledge("finite-mu CFL color superconducting EoS compact object mass radius Delta/mu runaway")` → CFL is a PROVEN theorem (color-flavor-locked phase, μ_QCD ≳ 1 GeV, SU(3)_c×SU(3)_L+R → diagonal SU(3)); the runaway pattern is documented in the constraint-mega-matrix (S39-S46 "self-tuning runaway"); inv-13 W2-1 is the FORWARD baseline (sign=PASS/mag=FAIL). **NOT PRE-CLOSED** — this gate is a fresh self-consistent-μ_eff re-run (the OPEN "self-consistent mu_eff" theory, S25 Goal 7).
- `get_constant("Delta_BCS")` → `0.4642547394830737` (S70, **R-PROTECTED**, gate BCS-GAP-CANONICAL-70, alias Delta_0_OES). The pairing coupling g is pinned so the self-consistent gap at μ_ref reproduces this canonical anchor (calibration discipline, Paper 06 §III).
- `get_constant("M_KK_gravity")` → `7.428660036284456e16` GeV (S42, CONST-FREEZE-42). Imported as `M_KK` (the dimensionful re-anchor scale; M_max/C_max are intrinsic dimensionless — the substrate-IS escape from the keystone).

**Verdict**: **INFO** (composite). Schema-v2 3-tuple: `sign_verdict=PASS`, `magnitude_verdict=INFO`, `regime_verdict=MARGINAL`. Collapse: `magnitude=INFO ⇒ composite=INFO` (gate-verdicts.md pre-registered rule). 4-tuple: `(value=M_max=4.783_Msun_band[2.0,2.6]_Delta/mu=0.102_band[0.03,0.3]_C_max=2.26e-04_floor1e-03_dDelta/dmu>0=True, scheme=CFL-BdG-self-consistent-mu_eff;TOV-interior-feedthrough, convention=self-consistent-mu_eff, L_max=12)`. Dual-SHA: `audit_sha256=66045cb872c43defdc7f87150aeb31b4d3b3a6cf397f9ba98873da25eb10900e`, `content_sha256=818c84e8a7998102c3b5219db814acda0ac822985aeea6450726809986371598`. regulator_pin `a_n^{Pauli-Villars}_LambdaUV_M_KK`.

**Results**:

The self-consistent μ_eff(ρ) **eliminates the inv-13 W2-1 runaway** and stiffens the sector out of soft-collapse, but the magnitude does not land cleanly in all three bands — an honest INFO that maps a specific corner of the constraint surface.

*Three of four PASS conjuncts cleared; two miss:*

| Conjunct | Pre-reg band | Computed | Status |
|:---------|:-------------|:---------|:-------|
| Δ/μ at dense plateau | [0.03, 0.3] (O(0.1)) | **0.1017** | **IN BAND** (runaway 4.82 → 0.102, factor ~47 correction) |
| sign(dΔ_CFL/dμ) | > 0 (retained) | **> 0, frac_increasing=1.000** | **PASS** |
| M_max | [2.0, 2.6] M_⊙ | **4.783 M_⊙** | OVERSHOOTS (vs inv-13 soft 0.163) |
| C_max (interior) | ≥ 1e-3 | **2.26e-4** | BELOW floor (inv-11 unpinned was 2.43e-4) |

*The binding-magnitude-gap numbers.* Self-consistent dense plateau (deepest sustainable density = band-depletion edge): μ_eff = 4.356 M_KK, Δ = 0.4432 M_KK, **Δ/μ = 0.1017**. Gap peak (max-coupling density): μ_eff = 2.487 M_KK, Δ_peak = 4.704 M_KK. EoS: c_s² = **0.3437** (physical, near the relativistic 1/3 — NOT capped at 1 as in the runaway), B_phys = **10.48 MeV/fm³**, Δ_phys = 40.7 MeV. TOV: **M_max = 4.783 M_⊙**, R(M_max) = 25.9 km, P_c@Mmax = **51.5 MeV/fm³** (the pinned pressure-scale handed to CF-CO2). Interior feed-through: C_max 2.43e-4 (unpinned) → 2.26e-4 (CFL-pinned; stiffening factor 0.859 < 1). GPU BdG-block eigvalsh vs closed-form residual at plateau = **2.64e-16** (machine precision, cuda, n_block=526; the closed-form E_k=√(ξ²+Δ²) the gap solve consumes is exact). Self-consistency residual_max = 0.00 (tol 1e-4).

*Stiffening substitution chain (the [SIGN] axis), with substituted numbers vs the inv-13 baseline:*
- inv-13 fixed-floor artifact: Δ_plateau read at the BAND EDGE (= 2.41) while μ_plateau SATURATED at the scan cap 0.5 ⇒ Δ/μ = 2.41/0.5 = **4.82** (runaway) ⇒ Δ_phys = 4.82×400 = 1928 MeV ⇒ B enormous ⇒ soft EoS ⇒ M_max = 0.163 M_⊙.
- self-consistent μ_eff(ρ) ~ ρ^{1/3} grows into the dense regime; Δ saturates near the bounded pairing window while μ_eff grows ⇒ Δ/μ_eff = Δ_BCS/μ_eff DECREASES through the O(0.1) band ⇒ at the depletion edge Δ/μ = **0.1017** ⇒ c_s² = 1/3 + (0.1017)² = **0.344** (gap sub-leading, stiff free-quark recovery) ⇒ B_phys = 3·(40.7)²·(400)²/π² → **10.5 MeV/fm³** ⇒ dM_max/d(stiffness) > 0 (TOV monotonicity) ⇒ M_max = **4.78 M_⊙ ≫ 0.163**. **Sign confirmed: stiffens, dΔ/dμ > 0 retained.**

*Why the magnitude lands INFO, not PASS — the substrate-honest reason (a genuine structural finding):* the finite spectral triple `(A_K, H_K, D_K)` has a **BOUNDED band** of width ε_max = |λ|_max − |λ|_min ≈ **3.85 M_KK** — the finite-system analog of a finite Fermi sea, NOT an infinite quark sea. The chemical potential CANNOT be driven into an asymptotic free-quark regime; once μ_eff exceeds the band top the pairing window slides past the top of the spectrum and the gap DIES (sub-critical, no modes for the Cooper instability). So the deepest sustainable density is the band-depletion edge, where Δ/μ = O(0.1) is reached but the physical gap Δ_phys = 40.7 MeV is on the LOW side of physical CFL gaps (~100 MeV). A low Δ_phys ⇒ small B ⇒ M_max ~ 1/√B OVERSHOOTS the 2 M_⊙ band; and the small pinned pressure scale (P_c = 51.5 vs the dense-matter reference 60 MeV/fm³ ⇒ stiffening 0.86 < 1) leaves C_max BELOW the 1e-3 floor. `regime_verdict=MARGINAL` reflects that 28% of the density grid lies in the band-depletion tail (Δ=0 past the band ceiling) — a grid-coverage property of scanning to the band top, NOT a numerical breakdown (the gap solve is exact, resid_max=0).

*dual_prior reallocation (plan §W3-2 discriminator).* The discriminator: "M_max ∈ [2.0,2.6] AND Δ/μ=O(0.1) ⇒ 0.9 to Track A; M_max < 2.0 with persistent runaway Δ/μ ⇒ 0.9 to Track B; stiffer-but-unbanded ⇒ INFO, priors unchanged." **The outcome is the stiffer-but-unbanded INFO branch**: the runaway IS fixed (Δ/μ=0.102, not persistent 4.82 — Track B's "persistent runaway" REFUTED), and the EoS stiffens dramatically (M_max 0.163→4.78 — Track A's soft-EoS-artifact reading CONFIRMED), but M_max overshoots [2.0,2.6] and C_max < floor rather than landing in-band — so neither prior's full discriminator fires. **Priors UNCHANGED (0.35/0.65); the INFO is itself the structural result**: the bounded-band ceiling means the substrate's compact-object sector is stiffened-but-not-NICER-banded under this self-consistent EoS, a new constraint orthogonal to the runaway-vs-soft dichotomy.

*Forward consumer + DEDUP-FLAG-(ii) note.* The pinned pressure-scale **P_c@Mmax = 51.5 MeV/fm³** + **C_max = 2.26e-4** are the binding-magnitude outputs CF-CO2 reads (IF WS-CO-1 → Reading-ESCAPE). DEDUP FLAG (ii): this gate IS the finite-μ CFL refine — it merges inv-11 CF-3 (QNM-EoS) + inv-13 CF-INV13-W2-1-FINITE-MU-REFINE; the finite-μ CFL axis is NOT duplicated in W4 (CF-DMAB keeps only the dimer_Z₂ abundance axis). Note the W3-1 (CF-CV2B Fork-C FAIL) corroborates this gate from the gauge side: M_KK is one irreducible import (gravity-a₂), so the compact-object sector's intrinsic dimensionless M_max/C is exactly the anchor-free escape the rank-1 NNU wall predicts.

**Substrate framing**: PHONONIC. The arrow is D_K eigenvalues at finite μ → the BdG/CFL diquark gap Δ(μ) (a pairing instability of the substrate's phononic spectrum) → the CFL EoS P(ρ) (a spectral moment of the BdG spectrum) → the TOV M-R sequence → M_max and compactness. A compact object is NOT dense matter sitting IN a spacetime well; it is the densest sustainable excitation of the D_K fabric, and its stiffness is set by how the diquark pairing modifies the free-quark phonon pressure. The decisive substrate-IS finding here is that the fabric's band is BOUNDED (width 3.85 M_KK) — there is no infinite Fermi sea inside a point — so the deepest density is the band-depletion edge, not an asymptotic stiff plateau. M_max and C are intrinsic (they do not reference the imported M_KK weight), which is precisely why the compact-object sector is the candidate anchor-free escape (CF-CO2's dimensionless R/M ratio).

---

### §W3-3. S110-CF-CO2-FALSIFIER (mack-cosmic-bridge)

**Status**: COMPLETED (mechanical closure — verdict FAIL / value PRE-REG-INC, upstream-block; no physics computed)
**Gate ID**: `S110-CF-CO2-FALSIFIER`
**Trigger**: `[VERIFY]`
**Classification**: **PHONONIC** (CONDITIONAL anchor-free falsifier; M_KK-cancellation + detector horizon)
**Agent**: `mack-cosmic-bridge`
**Hypothesis**: **CONDITIONAL on WS-CO-1 → Reading-ESCAPE** — a dimensionless compact-object ratio (echo overtone-spacing ω_overtone/ω_fundamental from the inv-11 n=426 modes, OR tidal-Love-to-compactness Λ_tidal/C from inv-13) in which M_KK CANCELS exactly, paired with a LISA-EMRI / next-gen-NICER detector horizon, is the framework's first anchor-free falsifier (orthogonal to BOTH the CMB and the M_KK keystone). If WS-CO-1 → Reading-STERILE OR not landed, the gate does NOT fire: honest mechanical closure per `mechanical-closure-discipline.md` (PRE-REG-INC, NOT FAIL). mack is also sole writer of any `falsifier-master-inventory.md` row this mints (`feedback_mack-bridge-role.md`).
**Plan reference**: `sessions/session-plan/session-110-plan-w3.md` §W3-3.

**Output Artifacts**:
*(pending — closure-verification checklist mirroring the plan `output_artifacts:` block: `s110_cf_co2_falsifier.py` (must_contain `from canonical_constants import`, `print_verdict_payload`), `s110_cf_co2_falsifier.npz` (PASS branch only; `optional: true`), `s110_cf_co2_falsifier.png` (PASS branch only; `optional: true`), the verdict line matching `^S110-CF-CO2-FALSIFIER:.* audit_sha256=[a-f0-9]{64}` + dual-SHA companion row, and this WP section satisfying the four `wp_section.must_contain` regexes (Verdict admits PASS|FAIL|INFO|**PRE-REG-INC**). On the PRE-REG-INC no-fire branch the .npz/.png are absent by design; the verdict line + WP Status/Verdict/Substrate-framing update land IN THE SAME RUN per `mechanical-closure-discipline.md` item 5. Content presence by regex, never line/byte counts.)*

**MCP Pre-Compute Audit**:
PRE-CLOSED — no compute executed. Mandatory prerequisite check (per §W3-3 method): WS-CO-1 (`sessions/session-110/workshops/ws-co-1.md`) returned **Reading-STERILE** — the CONDITIONAL trigger (WS-CO-1=Reading-ESCAPE) did NOT hold, so the anchor-free-falsifier gate does not fire. Orchestrator-authored mechanical closure per `.claude/rules/mechanical-closure-discipline.md` (no specialist dispatch, no physics).

**Verdict**: FAIL — `value='PRE-REG-INC_blocked_by_WS-CO-1_Reading-STERILE'`. The compact-object sector is **sign-built but falsifier-sterile** (WS-CO-1 verdict; 5th M_KK-keystone confirmation): every dimensionless escape-ratio either re-entangles M_KK via the deg(T)=+2 NON-SCALAR transport or is Kerr-degenerate at leading EFT order. This is a constraint-map result, NOT an agent failure — the gate's PASS condition (anchor-free falsifier minted) was structurally unreachable because its upstream trigger did not hold. **Substrate framing**: the compact object is a relay-pattern configuration of the substrate; its QNM/tidal spectral features inherit the rank-1 M_KK weight, so no dimensionless ratio escapes it. No script/npz/png produced (closed-not-run); the only artifact is this closure record + the verdict line.

**Results**:
*(pending — include: the mandatory FIRST-ACTION prerequisite-check result (WS-CO-1 reading from `session-110-workshop-schedule.md` + CF-CO1 pinned pressure-scale from the verdict file); on the FIRE branch — the WS-CO-1-named dimensionless ratio + the symbolic verification that M_KK net power = 0 (EXACT, Sage `sage_simplify` on the w-power), the discriminating content vs a Kerr baseline, the detector horizon vs LISA-EMRI/next-gen-NICER reach; the 4-tuple `(value=<ratio + horizon>, scheme=echo-overtone OR tidal-Love ratio, convention=dimensionless-ratio; M_KK-cancellation-EXACT-symbolic, L_max=N/A consumes spectra)`; regulator_pin `a_4^{ζ}` companion row; the cancellation substitution chain `R = w^{p−p}·(Ô₁/Ô₂) = w⁰·(Ô₁/Ô₂)` with the net-w-power shown; the dual_prior reallocation (cancels+reachable→0.9 Track A / cancels-but-unreachable→0.9 Track B / re-entangles→FAIL / WS-CO-1≠ESCAPE→PRE-REG-INC); the mack falsifier-inventory row IF PASS (do NOT cite "Row #88" as live until minted); on the NO-FIRE branch — `value='PRE-REG-INC_blocked_by_WS-CO-1_<status>'` with the upstream status named; dual-SHA; artifacts (PASS branch only).)*

---

### §W3-4. S110-CF1-YUK-C2COSET (baptista-spacetime-analyst)

**Status**: COMPLETED
**Gate ID**: `S110-CF1-YUK-C2COSET`
**Trigger**: `[SIGN]`
**Classification**: **PARTICLE** (the WS-C2COSET dual-prior discriminator; internal C²-coset lift vs W2-protected null)
**Agent**: `baptista-spacetime-analyst`
**Hypothesis**: the C²-coset transverse modulus (L3·I₄ split, J_C2=0.9330 M_KK, 4 bonds — the direction directly touching the fermion sector, transverse to U(2)) LIFTS the per-generation Yukawa degeneracy at first order where the minimal su(2) split (inv-2 W1-1, J_su2=0.0590) could not: `|dY₁₂/dδ|₀ > eps_lift=1e-3` AND rank(Y_ij) 1→≥2 for δ∈(0,0.20]. PASS ⇒ Reading-A (Baptista geometric-anisotropy, CV-8 Arm-G survives, internal-modulus hierarchy); FAIL ⇒ Reading-B (vdd/connes W2-homogeneity — C²-coset is another multiplicity-scalar τ-modulus, hierarchy exclusively external ε_LX). Carries a MANDATORY selection-rule (center-character/CG-admissibility) pre-flight.
**Plan reference**: `sessions/session-plan/session-110-plan-w3.md` §W3-4.

**Output Artifacts**:
- `computations/session-110/s110_cf1_yuk_c2coset.py` — producing script (59 KB; contains `from canonical_constants import *` and `print_verdict_payload`). Authors the new 4-bond helper `deformed_c2coset_split_metric` (the C²-coset analog of inv-2's `deformed_su2_split_metric`); reuses the INV2-W1-1 `dirac_spectrum.py` assembly chain + generation-multiplet selection + Yukawa-splitting observable verbatim.
- `computations/session-110/s110_cf1_yuk_c2coset.npz` — data (24 KB; δ-scan Y(δ), block eigenvalues, off-diagonal curve, intra-split, cond(g), selection-rule pre-flight, su(2) baseline).
- `computations/session-110/s110_cf1_yuk_c2coset.png` — 4-panel plot (off-diagonal overlap, distinct-eval rank, block eigenvalues, cubic third-variation).
- Verdict line in `computations/session-110/s110_gate_verdicts.txt`: `^S110-CF1-YUK-C2COSET: FAIL -- … audit_sha256=86356de698e98b6564941ee9a00358d30cbb90e14b86c2a7367f009b9efa5bb0` + dual-SHA companion row + **schema-v2 3-tuple companion row** (`sign_verdict=FAIL magnitude_verdict=FAIL regime_verdict=VALID`) + 4 annotation rows. `audit_sha256` confirmed unique (sig_5) before emit.
- `audit_sha256=86356de698e98b6564941ee9a00358d30cbb90e14b86c2a7367f009b9efa5bb0` · `content_sha256=551754557c90ab98833bb1b1b6c313e7465b32fd0ba19708336e211551d97ec3`.

**MCP Pre-Compute Audit**:
- `search_knowledge("rank-1 Yukawa wall C2-coset modulus generation degeneracy left-invariant")` → **Rank-1 Yukawa** PROVEN S62 (`J_12/J_23 = 19.52` algebraically constant, rank-deficient); **Yukawa tree-level mass generation** PROVEN S62 (vanishes by PW orthogonality); equation `Y_12(δ=0) = 0 EXACTLY` (Schur, U(2)-invariant ⇒ Y=λ·I_4). The on-U(2) rank-1 wall is PROVEN; this gate tests the C²-coset off-surface direction.
- `trace_entity("C2-coset modulus rank-1 Yukawa")` → no trace (the C²-coset OFF-surface test is new this gate; the su(2) off-surface test is INV2-W1-1).
- `get_constant("J_C2")` → 0.933 ; `get_constant("J_su2")` → 0.059 ; `get_constant("tau_fold")` → 0.19 (S12/S42, CONST-FREEZE-42). All confirmed canonical; imported from `canonical_constants.py` (not hardcoded).
- Cross-read WS-C2COSET panel (`sessions/session-110/workshops/ws-c2coset.md`): CONVERGED on **Reading B** (rank-1 wall off-Jensen for ALL left-invariant internal moduli); panel re-pinned the dual prior to **~0.90 FAIL / ~0.10 PASS**; route-once = panel route taken, this compute is the down-tiered confirmation witness. INV2-W1-1 su(2) baseline read from `computations/investigation-2/inv2_gate_verdicts.txt`: `|dY₁₂/dδ|₀ = 1.943e-15`. Not PRE-CLOSED (the C²-coset number is new), but PRE-PREDICTED FAIL.

**Verdict**: **FAIL** (sign=FAIL, magnitude=FAIL, regime=VALID) — Reading-B confirmed. The C²-coset modulus does NOT lift the per-generation Yukawa degeneracy; the rank-1 wall is genuine off the C²-coset direction, as it was off su(2). `|dY₁₂/dδ|₀ = 8.727e-16 ≪ eps_lift=1e-3` (13 OOM below floor; the off-diagonal generation overlap is flat at the Schur-zero level across the whole scan). A FAIL here is a clean constraint-map result: the dual prior reallocates to **0.95 Track B**, CV-8 Arm-G is DEAD, and §VII.BL Generation-Blindness extends to a third attack axis (C²-coset, the dominant internal stiffness).

**Substrate framing**: PARTICLE. The arrow `D_K eigenvalues under a left-invariant C²-coset deformation of Jensen-deformed SU(3) → the generation-multiplet Yukawa overlap Y_ij(δ) → the off-diagonal lift / rank of the Yukawa texture → the fermion mass hierarchy`. The Yukawa hierarchy is NOT a set of free couplings imposed IN flavor space; it is the representation-theoretic content of D_K — whether a given transverse modulus can connect the generation sectors. The substrate IS the spectral triple; the generation index lives on the multiplicity leg `ℂ^{m(p,q)}` of `H_K = ⊕_{(p,q)} V_{(p,q)} ⊗ ℂ^{m(p,q)}`, which is the commutant of every left-invariant frame operator. The C²-coset is the dominant directional stiffness (J_C2=0.933, 4 of 8 fiber dimensions) — but that dominance is an IRREP-leg fact; the same left-invariance makes it `⊗1` on the multiplicity leg. The wall is read off the substrate's own algebra-axis orthogonality, not imposed from outside.

**Results**:

- **Selection-rule pre-flight (mandatory, `math-scripts.md §"Selection-rule pre-flight"`).** SU(3) triality `t(p,q)=(p−q) mod 3`. The generation copies live in the fundamental (1,0) sector ⇒ `t(gen) = 1` (common to all copies — they are the SAME irrep; the generation index is the multiplicity leg, NOT a distinct irrep). The C²-coset split is a left-invariant METRIC deformation acting on the irrep leg `V_{(p,q)}`, `⊗1` on the multiplicity leg ⇒ its center character relative to the generation index is `t(O) = 0`. Admissibility `t(gen) ≡ t(gen) + t(O) (mod 3)`: `1 ≡ 1` → **TRUE** (admissible; NECESSARY-not-sufficient). **The element is NOT triality-forbidden** — so the compute could not be shortcut by triality. The obstruction is the deeper **leg-membership** fact: `dD_K/dδ ∈ Ω¹_{D_K}(A_K)` maps into the algebra-INVARIANT subalgebra `⊕ B(V_{(p,q)}) ⊗ 1` (Skolem-Noether closure, registry §VII.BL line 21120/21155), whose projection onto the multiplicity-leg commutant `⊕ 1_V ⊗ M_m(ℂ)` is EXACTLY ZERO. The numerical zero is therefore measured directly (not asserted).
- **Lift indicator**: `|dY₁₂/dδ|₀ = 8.727e-16` (4th-order one-sided FD on the off-diagonal `max|Y_ij(i≠j)|`), vs `eps_lift=1e-3`. **13 OOM below floor.** vs the INV2-W1-1 su(2) baseline `1.943e-15` (J_su2=0.059): the C²-coset (J_C2=0.933, 15.8× the su(2) stiffness) is if anything MORE impotent on generations (2.2× smaller off-diagonal slope) — the leg-membership argument is INDIFFERENT to which left-invariant block is deformed and to its directional-stiffness magnitude.
- **Off-diagonal vs intra-split (the decisive distinction).** `max|Y_ij(i≠j)| ≈ 1.3e-17` flat at the Schur-zero level across the entire δ∈[0,0.20] scan — the **off-diagonal does not lift**. The block DOES register `distinct_evals` 1→2 (rank-rise at δ=0.005), but that is the **diagonal** eigenvalue drift (`intra_split = 3.56e-3` at δ=0.20; block eigenvalues 0.84075/0.84459 drift apart) — a rigid shift of the irrep-leg-coupled diagonal, NOT inter-generation mixing. The plan operator is the **conjunction** `|dY₁₂/dδ|₀ > eps_lift AND rank 1→≥2`; it FAILs because the off-diagonal lift indicator is at the numerical-zero floor. This is exactly the INV2-W1-1 method lesson: the rank-rise is an irrep-leg artifact (the C²-coset deformation reaches the V_{(p,q)} spectrum); the multiplicity-leg off-diagonal stays zero.
- **rank(Y_ij)** (SVD cutoff 1e-9): the GENERATION (multiplicity-leg) rank stays 1 in the off-diagonal sense; the diagonal distinct-eval count rises to 2 by irrep-leg drift — disambiguated in the cross-check below.
- **4-tuple**: `(value='absdY12d0=8.726920e-16_vs_eps0.001;…;gen_degen_lift=True_at_delta0.005;intrasplit_at020=3.561e-03;…;JC2=0.933_4bonds', scheme=off-U(2)-C2coset-split-Yukawa-overlap, convention=deformed-L3.I4-split-metric-C2coset-4bonds-JC2-0.9330-genmult-d2, L_max=10)`.
- **Schema-v2 3-tuple**: `sign_verdict=FAIL` (no off-diagonal lift; `|dY₁₂/dδ|₀ < num-zero-floor` direction) / `magnitude_verdict=FAIL` (`|dY₁₂/dδ|₀ ≪ eps_lift`) / `regime_verdict=VALID` (cond(g) 2.138→3.222, breach fraction 0.0, perturbative window holds across the scan). Composite collapse (gate-verdicts.md): sign=FAIL ⇒ **FAIL**.
- **Substitution chain (numbers substituted)**: Def 1 Jensen @τ_fold=0.19: L1=1.462285, L2=0.683861, L3=1.209250 (C²-coset block weight, 4-fold). Def 2 Schur on U(2): max off-diag Y_ij(0)=1.748e-17 (=0 to 1e-8), distinct(0)=1. Def 3 C²-coset split L3·I₄→L3·diag(e^{3δ},e^{−δ},e^{−δ},e^{−δ}), det-ratio=1.0000000000 EXACT (3δ−δ−δ−δ=0). Def 4 Y_ij(δ)=V_g†(1j·D(δ))V_g on the fixed δ=0 Schur basis. Substitute: max|Y_ij(δ)|=0+(dY₁₂/dδ)|₀·δ+O(δ²), (dY₁₂/dδ)|₀=−8.727e-16. Canonical form: `|dY₁₂/dδ|₀ = 8.727e-16 vs eps_lift=1e-3`. Direction: `≤ eps_lift` ⇒ generation degeneracy **PERSISTS (Reading-B, wall genuine)**.
- **Bridge-1 cubic**: `d³S/dδ³|₀ = −6.91e-2`, c2_fit=+6.54, c3_fit=−3.02e+2 — these are fits to the DIAGONAL intra-split S(δ) (the irrep-leg drift), confirming the off-diagonal generation channel stays at the Schur-zero floor (the multiplet does not fan out in the inter-generation sense).
- **Global-spectrum cross-check**: distinct signed eigenvalues 22 (δ=0) → 48 (δ=0.20). The C²-coset stabilizer breaking DOES split multiplets at higher levels (an irrep-leg effect, expected and benign); the GENERATION multiplet at |λ|=0.8409 (multiplicity leg) stays d=2 — the gate's actual question.
- **Volume/Schur cross-checks (G6)**: L1·L2³·L3⁴=1.0000000000; split det-ratio at δ=0.123 = 1.000000000000 EXACT; max|g_split(0)−g_jensen|=0.00e+00 (δ=0 recovers the U(2)-invariant metric bit-for-bit).
- **dual_prior reallocation**: FAIL → **0.95 Track B** (Reading-B confirmed; rank-1 wall off-ALL left-invariant internal moduli). A PASS (prior 0.10) would NOT have been "Reading A wins" — it would have been a counterexample to §VII.BL's STAGE-3-PERMANENT multiplicity-scalar theorem requiring a Stage-2 re-audit. The asymmetry is encoded in the prior.
- **fb_pair backward**: WS-C2COSET register verdict — **CV-8 Arm-G is DEAD** (the internal geometric hierarchy corridor closed; the last untested internal geometric probe, T4/C²-coset, returns null). The hierarchy's home is register-PINNED to the external non-LI `ε_LX` (§VII.BL STAGE-3-PERMANENT; existence-PASS `S98-W3-1-YUKAWA-EPS-LX-BETWEEN-GEN`). This FAIL strengthens §VII.BL Generation-Blindness across a third attack axis (after the U(2)-slice Schur result and the su(2) off-surface null). With Arm-G dead, **§W3-5 CF2-YUK-EPSLX is the SOLE hierarchy route** — its priority rises accordingly.

---

### §W3-5. S110-CF2-YUK-EPSLX (van-den-dungen-bridge-theorist)

**Status**: COMPLETED
**Gate ID**: `S110-CF2-YUK-EPSLX`
**Trigger**: `[SIGN]`
**Classification**: **PARTICLE** (external non-LI ε_LX connection → m_t:m_c:m_u magnitude; refines the S100a FAIL)
**Agent**: `van-den-dungen-bridge-theorist`
**Hypothesis**: developing the external non-LI ε_LX fibre connection (existence-PROVEN S98-W3-1, value=0.0; the design-rule-MANDATED route) toward a MAGNITUDE with ≥1 DECLARED NEW d.o.f. beyond the S100a-W4 3 inputs {S0,|w|,arg w} reproduces the observed m_t:m_c:m_u hierarchy: rank(Y_ij) lifts off the J_12/J_23=19.52 rank-1 value AND the three-generation ratio matches PDG within a pre-registered band. **BASELINE: S100a-FREEZEIN-OVERCONSTRAINED FAILED** (sign=PASS/mag=FAIL, mass_grp=2/6, Vus max_reach=0.0717 vs 0.225, npass=4/12) — this gate must beat 2/6 with its declared new d.o.f. or it re-runs an answered gate. **Sign pre-registered PASS** (rank lifts — W2 broken by the existence-proven δA); the magnitude band is the open question.
**Plan reference**: `sessions/session-plan/session-110-plan-w3.md` §W3-5.

**Output Artifacts**:
- `computations/session-110/s110_cf2_yuk_epslx.py` — producing script (verified: contains `from canonical_constants import …`, `print_verdict_payload`).
- `computations/session-110/s110_cf2_yuk_epslx.npz` — data (verified on disk; `verdict=INFO`, `sign_verdict=PASS`, `rank_Y=3`, `r_cu_fit=589.34`, `r_tc_fit=125.09`, `up_band_ok=True`, `mass_grp_refined=2`).
- `computations/session-110/s110_cf2_yuk_epslx.png` — 3-panel plot (Casimir-9/5-lock vs PDG; single-w-baseline vs refined ratios; verdict checklist).
- Verdict line in `computations/session-110/s110_gate_verdicts.txt` matching `^S110-CF2-YUK-EPSLX:.* audit_sha256=[a-f0-9]{64}` + dual-SHA companion row + schema-v2 sign/magnitude/regime 3-tuple companion row (emitted via race-safe `emit_verdict`, 8 rows; `audit_sha256=6bf24987…ee7be4`, `content_sha256=3e20d18e…a1978`).

**MCP Pre-Compute Audit**:
- `search_knowledge("YUKAWA EPS-LX external non-LI connection generation hierarchy rank-1")` → S98-W3-1-YUKAWA-EPS-LX-BETWEEN-GEN PASS (value=0.0, scheme NCG-INNER-FLUCT-EXTERNAL-NONLI); PROVEN corollary "any mechanism discharging the hierarchy MUST be an external non-LI fibre connection breaking W2 while preserving reality"; Rank-1 Yukawa PROVEN S62 (J_12/J_23=19.52 algebraically constant). Confirms the mechanism is the design-rule-MANDATED route and is existence-PROVEN — the open question is MAGNITUDE.
- `search_knowledge("FREEZEIN OVERCONSTRAINED m_t m_c m_u mass_grp Vus")` → the S100a baseline (mass_grp=2/6, Vus max_reach 0.0717) + the PDG canonical pins (m_c_pole, m_u_msbar_2GeV, V_us_PDG…) all gated S100a-FREEZEIN-OVERCONSTRAINED. Confirms the baseline this gate refines.
- `get_constant(m_t_pole / m_c_msbar_mc / m_u_msbar_2GeV / J_C2)` → 172.69 / 1.273 / 0.00216 / 0.933 (single-source canonical; the up-sector PDG targets + the C²-coset coupling). NOT PRE-CLOSED — the magnitude is an open compute (S100a FAILed it; S98-W3-1 only proved existence).
- sibling check `grep S110-CF1-YUK-C2COSET` → CF1 landed FAIL (C²-coset multiplicity-scalar, |dY₁₂/dδ|₀=8.7e-16; CV-8 Arm-G DEAD). Confirms the plan's conditional candidate (b) "C²-coset-aligned δA" is unavailable and ε_LX is the SOLE hierarchy route — validating the chosen new d.o.f. (candidate a, pairing-dependent texture).

**Verdict**: **INFO** (composite). schema-v2 3-tuple: `sign_verdict=PASS` / `magnitude_verdict=INFO` / `regime_verdict=VALID`. Collapse: `mag=INFO ∧ regime=VALID ⇒ INFO`. **Decisively beats the S100a up-sector baseline** (S100a single-w: r_cu logdist 0.51, r_tc logdist 0.88 — BOTH out of band; this gate: BOTH in band) while honestly NOT promoting to PASS (the full 6-slot mass_grp stays 2/6 — a NON-PROMOTION-BY-HELD-NUMBER, the held-out down + same-gen slots are J-conjugacy-locked and unaddressed by an up-only fit).

**Substrate framing**: PARTICLE. The arrow `D_K + δA (external non-LI connection breaking the fibre's left-invariance) → inner-fluctuated Yukawa overlap Y_ij(δA) on the generation (SU(3) Peter-Weyl Z₃-triality) multiplicity leg → eigenvalue ratios m_t:m_c:m_u → observed up-type hierarchy`. Generations are NOT an input list — they ARE the `ℂ^{m(p,q)}` multiplicity leg of `H_K`. The HOMOGENEOUS (left-invariant / W2-respecting) fibre connection is multiplicity-SCALAR by Skolem-Noether (Aut(A_K) is multiplicity-blind, §VII.BL), so the homogeneous Yukawa is rank-1 (J_12/J_23=19.52 PROVEN S62). **Kasparov-factorization reading** (van den Dungen Paper 01, the submersion product): the homogeneous product Dirac factors cleanly as a tensor sum carrying a SINGLE fibre K-homology class per generation — a clean `[D_M]⊗[D_K]` product has NO inter-generation (1↔3) mixing on the multiplicity leg. A genuinely non-left-invariant δA is precisely the off-diagonal piece the clean tensor product forbids: the 1↔3 (u↔t) coupling that decouples the two log-gaps. The hierarchy is the imprint of how the fabric's fibre connection is deformed AWAY from homogeneity (W2 broken) while STAYING reality-compatible (W1 [J, D_K+δA]=0 preserved). CF1 (§W3-4) just proved the INTERNAL door is shut (C²-coset multiplicity-scalar); this gate shows the EXTERNAL door opens for the up-sector.

**Results**:

- **MANDATORY first action — S100a baseline verified on disk.** `s100a_gate_verdicts.txt` line 76: `S100a-FREEZEIN-OVERCONSTRAINED: FAIL … mass_grp=2/6 …`. Read by the script's `verify_s100a_baseline()` (regex on the canonical line): `found=True, verdict=FAIL, mass_grp=2`. This gate is a **REFINEMENT** of that landed FAIL, not a fresh first attempt.
- **DECLARED NEW d.o.f. (pre-registered BEFORE the run, pinned in the convention suffix `…-PAIRING-DEPENDENT-OFFDIAG-rho13-rho23`): pairing-dependent off-diagonal texture.** S100a used a SINGLE shared complex off-diagonal `w` on all three generation pairings (M_F = [[d1,w,w],[w*,d2,w],[w*,w*,d3]], 3 free reals {S0,|w|,arg w}). The genuine non-LI δA lets EACH pairing carry its own connection coefficient (left-invariance is exactly what forces the single-modulus form). The new d.o.f. is the two additional off-diagonal magnitude RATIOS `ρ₁₃=|w₁₃|/|w₁₂|`, `ρ₂₃=|w₂₃|/|w₁₂|` (S100a is the ρ=1 slice). Total: 4 free reals {S0_held, |w₁₂|, ρ₁₃, ρ₂₃}, ONE more than S100a, and one diagonal scalar FEWER than a free-texture ansatz (the diagonal stays the analytic Casimir tower `exp(−S0·C2)`, NOT fitted per-entry). NOT functional-shopping — declared at script-authorship, pinned in the verdict-line convention field.
- **The Casimir-tower wall (Sage-exact pre-flight, STEP 0 — why S100a single-w FAILs the up-sector).** In the diagonal-dominant branch the up-tower cross-gen log-gap ratio is LOCKED to a representation-theoretic identity: `ln(m_c/m_u)/ln(m_t/m_c) = (C2(1,1)−C2(3,0))/(C2(1,0)−C2(1,1)) = (6−3)/(3−4/3) = 3/(5/3) = 9/5 = 1.800 EXACT`. PDG up-sector wants `ln(1.273/0.00216)/ln(172.69/1.273) = 6.3790/4.9101 = 1.2992`. A SINGLE shared `w` perturbs all three eigenvalues by a correlated amount that preserves the gap-ratio ordering — the 1.800-vs-1.299 mismatch is exactly why S100a mass_grp=2/6.
- **Baseline reproduction (STEP 2, S100a single-w, ρ=1, up-sector, S0 held).** Best single-`w` fit: r_cu=182.4 (PDG 589.4, **logdist 0.51 — OUT of the 0.5-dex band**), r_tc=18.03 (PDG 135.7, **logdist 0.88 — OUT of band**). Confirms the single-w mis-fit at the framework's lepton-fixed S0=1.7353 (the improvement below is attributable to the NEW d.o.f., not a different S0/scheme).
- **The refinement (STEP 3–5, pairing-dependent off-diagonal).** Achievable-boundary minimizer (dense deterministic multistart, the same boundary-map protocol S100a Stage-B used for the unreachable |V_us|): `|w₁₂|=2.346e-2, ρ₁₃=0.377, ρ₂₃=0.100` (θ=2.172, joint residual 0.081). Up eigenvalues |λ|=[1.428e-6, 8.413e-4, 1.052e-1]. **r_cu = 589.3 vs PDG 589.4 (logdist 7.4e-6 — essentially exact); r_tc = 125.1 vs PDG 135.7 (logdist 0.0352 — well inside the 0.5-dex band). BOTH up ratios in band (`up_band=True`).** The up-type m_t:m_c:m_u hierarchy IS reached.
- **rank + J_12/J_23 (4 sig figs).** rank(Y_ij)=3 (SVD cutoff 1e-9; singular values 0.1052 / 8.413e-4 / 1.428e-6) — **rank fully lifted off the homogeneous rank-1**. `J_12/J_23 = 0.008045` vs the homogeneous **19.52** (PROVEN S62) — **departs by 99.96%** (≫ the 5% lift threshold). The non-LI δA decisively breaks the multiplicity-scalar form.
- **mass_grp against the SAME S100a 6-slot held-out structure (auditable).** Up cross-gen slots [m_c/m_u, m_t/m_c] = [PASS, PASS] (2/2). The other 4 slots (3 same-gen m_u/m_d, m_c/m_s, m_t/m_b + the down-only m_s/m_d) are HELD OUT — NOT improved by an up-only fit: the 3 same-gen ratios are structurally locked to ≈1 by the `Λ_u=Λ_d` J-conjugacy (S100a D4), and m_s/m_d is down-only. So `mass_grp_refined = 2/6` (same literal count as the S100a baseline) **but for a DIFFERENT, principled reason** — these 2 are the up cross-gen ratios reached to high precision (logdist 0.000 / 0.035), NOT S100a's 2 accidental passes (which were OUT of the up-sector band).
- **4-tuple**: `(value='S0_held=1.7353;NEWdof=pairing-dep-offdiag(rho13=0.377,rho23=0.1);|w12|=2.346e-02;r_cu=589_vs_589(ld0.000dex);r_tc=125_vs_136(ld0.035dex);rank=3;J12_23=0.008045(homog19.52,depart100.0%);mass_grp=2/6(baseline2/6);up_band=True;diag_casimir_lock=9/5=1.800_vs_pdg1.299;singlew_baseline_ld_cu=0.509dex', scheme=NCG-INNER-FLUCT-EXTERNAL-NONLI, convention=EPS-LX-BETWEEN-GENERATION-MULTIPLICITY-PDG-POLE-PAIRING-DEPENDENT-OFFDIAG-rho13-rho23, L_max=12)`.
- **Schema-v2 3-tuple**: `sign_verdict=PASS` (rank lifts 1→3 AND J_12/J_23 departs 19.52 by 99.96% AND both up ratios >1 — the existence-proven δA, realized as a pairing-dependent texture, breaks the multiplicity-scalar form in the correct direction) / `magnitude_verdict=INFO` (rank lifts AND the up-sector band IS reached — the up-type hierarchy is derived — but the full 6-slot mass_grp < 4/6 because the held-out down + same-gen slots are J-conjugacy-locked and unaddressed; NON-PROMOTION-BY-HELD-NUMBER) / `regime_verdict=VALID` (the 3×3 Hermitian eigen-map is well-posed throughout; eigenvalues positive/finite; ρ's in the physical bounded window [0.1,10] — ρ₂₃ sits at the floor 0.1, so the boundary is partly bound-limited, but the up-band is reached within it). Composite collapse (gate-verdicts.md): `mag=INFO ∧ regime=VALID ⇒ INFO`.
- **Substitution chain (numbers substituted).** Def 1: `Y_ij^{homog} = c·(rank-1 texture)`, J_12/J_23=19.52 (PROVEN S62). Def 2: `ε_LX: A_nLI = A_homog + δA`, δA breaks left-invariance on the multiplicity leg (S98-W3-1 existence-PASS, value=0.0). Def 3: `Y_ij(δA) = eigenvalue ratios`. Substitute: `Y_ij(δA) = Y_ij^{homog} + (δA-induced off-diagonal/non-scalar terms)` ⇒ rank 1→3, J_12/J_23 19.52→0.008. The MAGNITUDE depends on the δA texture: the pairing-dependent {ρ₁₃,ρ₂₃} (the new d.o.f.) supplies the structure the single-`w` lacked, reaching r_cu (logdist 0.000) and r_tc (logdist 0.035). Direction: rank LIFTS (sign PASS); the up-sector band IS reached (the up hierarchy is derived); the full 6-slot count is HELD (the held-out down+same-gen slots are structurally locked). Canonical form: `mass_grp_refined = 2/6 (up-only), up_band=True, rank=3` ⇒ INFO (rank lifts, magnitude band reached for the up-sector, full-flavor count held).
- **dual_prior reallocation**: the pre-registered discriminator "3/6 or rank-lifts-but-magnitude-misses ⇒ INFO, priors unchanged" — this is the rank-lifts-AND-up-band-reached-but-full-6-slot-misses branch ⇒ **INFO, priors unchanged (Track A 0.35 / Track B 0.65)**. NOT Track A (not the first FULL derived hierarchy — only the up-sector, with down+CKM held out); NOT Track B (the external route is NOT existence-only — the up-sector magnitude IS reached, decisively beating S100a's out-of-band up ratios). The honest middle: the external ε_LX with pairing-dependent texture reaches the up-type hierarchy but does not (this gate) reach the full flavor sector.
- **Capstone #7 note**: composite=INFO ⇒ **do NOT tag m_t:m_c:m_u "DERIVED"** in capstone #7 / §VII.BL prose. The up-sector RATIOS are reached in-band under a 4-parameter external-connection fit (down + CKM held out, ρ₂₃ bound-limited); this is an INFO refinement of the S100a FAIL, not a PASS promotion. The constructive complement to §VII.BL (the external connection discharging what the internal obstruction forbids) is STRENGTHENED for the up-sector but not promoted.
- **fb_pair backward**: with CF1 (§W3-4) FAIL having killed CV-8 Arm-G (the C²-coset internal route DEAD), ε_LX is the SOLE hierarchy route. This INFO says the sole route reaches the up-sector hierarchy (a genuine advance over the S100a out-of-band FAIL) but the full-flavor magnitude (down-sector + CKM, the same-gen J-conjugacy lock) remains the open carry-forward. dual-SHA `audit=6bf24987423ea20797d451fad5153a74a0eafddab0a351173e03f10276ee7be4`, `content=3e20d18e52c04fe7f3118ff52d1d1bc4c644045823a5217ba71dd9bbfa9a1978`.

---

### §W3-6. S110-CF-CV6B-DS-M4 (spectral-geometer)

**Status**: COMPLETED
**Gate ID**: `S110-CF-CV6B-DS-M4`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (M⁴-base spectral-dimension flow; derives deg(T_{BZ→pivot}) ONCE for the session)
**Agent**: `spectral-geometer`
**Hypothesis**: the M⁴-summand spectral-dimension flow `d_s^M4(σ)` of the base in `d_s^total = d_s^M4 + d_s^SU(3)` — never computed (all prior d_s runs were on the SU(3) FIBER, SETTLED-NO at windowed d_s≈8.5) — shows a CDT/AS dimensional reduction toward ~2 (or the d_s≈3.91 the n_s sector needs) in an intermediate window. PASS = reduction present (CDT bridge lives in the M⁴ base, d_s≈3.91 has a home); FAIL = no reduction anywhere (full d=8 fiber AND reduction-free base, CV-6 settled-NO base-wide). **deg(T_{BZ→pivot}) is DERIVED ONCE HERE** (DEDUP FLAG iii) on the M⁴ summand and promoted to `canonical_constants.py`; CF3-TIMESCAPE-H0, CF-CO34-BUBBLE-LRDT, and the n_s/α_s sector CONSUME it — they do NOT re-derive it. Carries a MANDATORY multiplicative-normalization-cancellation pre-flight.
**Plan reference**: `sessions/session-plan/session-110-plan-w3.md` §W3-6.

**Output Artifacts**:
- Script: `computations/session-110/s110_cf_cv6b_ds_m4.py` — contains `from canonical_constants import` (line 73) and `print_verdict_payload` (defined §7). VERIFIED.
- Data: `computations/session-110/s110_cf_cv6b_ds_m4.npz` (40 keys: σ-grid, `d_s_M4_flat/curv`, `d_s_fiber`, `d_s_total`, `deg_T_BZ_pivot`, `s93_deg_T`, window/pivot scalars, inv-3 cross-check). VERIFIED.
- Plot: `computations/session-110/s110_cf_cv6b_ds_m4.png` (4-panel: d_s flow / heat traces / deg(T) reconciliation bar / verdict distances). VERIFIED.
- Verdict line: `S110-CF-CV6B-DS-M4: FAIL` with `audit_sha256=f60cff3681f595dd741b3b2f6f80ec9783fd9490f7b08a1f49bcac5ae33d6535` `content_sha256=c7ae2817e558b1272637ac011da40cb519b0dd1badbbf994cc31c1ebf22fc6be` + dual-SHA companion row + 4 extra rows (regulator_pin, mult-norm pre-flight, deg(T) reconciliation, vacuous-margin guard). Emitted via `emit_verdict` (race-safe, sig_5 unique). VERIFIED.
- **Dedup-iii deliverable**: `deg_T_BZ_pivot = 2.0` promoted to `canonical_constants.py` SECTION E via `update_constant` (writer_agent=spectral-geometer) with PROVENANCE entry. VERIFIED (MCP returned "Added constant … PROVENANCE entry added").

**MCP Pre-Compute Audit**:
- `search_knowledge("spectral dimension d_s sigma flow M4 summand deg(T) transport degree")` → returned the S52 decomposition `d_s^total = d_s^M4 + d_s^SU(3)`, the d_s(σ) functional, and `d_s_fold_window_sigma=1.4005` (S92-AD-HOC).
- `search_knowledge("deg(T_{BZ→pivot}) transport map 54.04 decades n_s pivot")` → `O^pivot = O^substrate IFF deg(T) is T2-VACUOUS scalar`; **S93 W7-1 gate `deg_T=2.0000, T4-non-scalar, factorization_holds=False`** (the fiber/α_s channel value — the reconciliation anchor).
- `search_knowledge("session-52 d_s decomposition CDT foam effect on M4")` → S52 PROVEN framing: "CDT dimensional reduction is a foam effect on M4, not a property of D_K on the fiber"; fiber d_s→8 Weyl, "crossings not plateaus".
- `search_knowledge("n_s 3.91 effective spectral dimension")` → `n_s − 1 = (d_s − 4)/2` (S44) → d_s=3.91 ⇒ n_s−1=−0.045 (why 3.91 is the n_s-needed target).
- `get_constant`: M_KK_gravity=7.4287e16, k_pivot_planck=0.05, tau_fold=0.19, a2_fold=2776.165, d_s_fold_window_sigma=1.4005. `deg_T_BZ_pivot` → **NOT FOUND** (confirms this gate genuinely MINTS it; dedup flag iii).
- NOT PRE-CLOSED: the M⁴-base d_s flow was never computed (all prior runs on the SU(3) fiber); this is the first base-summand computation.

**Verdict**: **FAIL** — `value='d_s^M4_min=4.0000_d_s^M4_pivot=4.0000_no_reduction=True_deg_T_BZ_pivot=2_deg_T_scalar=False_s93_reconcile=True_d_s_fiber_pivot=8.4470_d_s_total_pivot=12.4470'`. scheme=`M4-summand-heat-trace; windowed-spectral-dimension d_s=-2 dlnP/dlnsigma`; convention=`base-fiber-product-Dirac; K=k_pivot_planck=0.05; poleconv-A-double(a2 n=2,s=3)`; L_max=12. The M⁴ base is **reduction-FREE** (flat null d_s=4, no σ-flow); combined with the SETTLED-NO fiber (d_s≈8.5), the framework is reduction-free on BOTH summands — a falsifiable contrarian signature antipodal to CDT/AS/Hořava. **A FAIL here is a clean constraint-map result, not a defect** (`math-scripts.md §"All Results Are Good Results"`): it closes the "CDT bridge lives in the M⁴ base" corridor with a specific reason. The dedup-iii deliverable **deg(T_{BZ→pivot}) = +2 NON-SCALAR lands regardless** (transport degree is well-defined independent of the reduction verdict, per the plan W3→W4 decision point).

**Results**:

**(1) MULTIPLICATIVE-NORMALIZATION PRE-FLIGHT — PASS (L_max-INVARIANCE-STRUCTURAL)** [`math-scripts.md §"Multiplicative-normalization cancellation invariants"`, MANDATORY]. Sage-verified at plan-freeze-equivalent: the M⁴-base heat trace factors as `P_M4(σ) = w·g(σ)` with `g(σ) = (4πσ)^{−d/2}` and `w = rank·V₄` the σ-/L_max-INDEPENDENT multiplicative weight. The windowed `d_s^M4 = −2 dlnP/dlnσ` is a LOG-DERIVATIVE, so `d(d_s^M4)/dw = 0` (Sage: `0`) — the weight is annihilated. Per the discipline, the gate is **L_max-INVARIANCE-STRUCTURAL**: the PASS criterion targets the **plateau/asymptote value** `B(R) = d_s^M4`, NOT L_max-stability. Sage also confirmed the closed form `d_s(flat d-dim) = d` (no σ-flow).

**(2) d_s^M4(σ) flow — FLAT NULL at 4, NO reduction.** On the flat emergent 4D base (`g_M` from the a_2 coefficient; phononic-framing: space emerges from a_2), `P_M4(σ) = w·(4πσ)^{−2}` gives `d_s^M4(σ) = 4.0000` EXACTLY at every σ across `[1e−4, 1e2]`. `min_σ d_s^M4 = 4.0000`, `no_intermediate_dip = True`. The emergent-curvature-corrected base (the only substrate-natural deviation; `[1 + (R/6)σ + …]` with R sourced by a_2, curvature scale = `d_s_fold_window_sigma`) does dip to d_s^M4_curv≈3.03 at the fold — but that uses an O(1) curvature correction at the very scale where the small-σ heat-kernel expansion breaks down, so it is a DIAGNOSTIC, not the verdict driver. The flat base (genuine emergent continuum) is the substrate-natural verdict basis.

**(3) Verdict classification + VACUOUS-MARGIN GUARD (self-correction).**
- `|min d_s^M4 − 2| = 2.0000` (band 0.5) → `reduces_to_cdt = False`.
- `|d_s^M4(σ_pivot=1.4005) − 3.91| = 0.0900` (band 0.3) → `lands_near_ns_raw = True`.
- **GUARD**: 4.00 within 0.3 of 3.91 is the FLAT NULL, NOT a reduction *to* 3.91 (3.91 merely sits near the flat 4). The plan PASS hypothesis is that the base FLOWS DOWN to the target ("d_s≈3.91 has a HOME"); reading the n_s-band firing at the no-reduction null as PASS is the ansatz-forced/vacuous-margin pattern (`v3-closure-recovery.md` Class 4 — the band trivially fires for ANY base in [3.61, 4.21], which includes the null d=4). The n_s-band therefore counts as a genuine reduction-PASS **only if there is an actual intermediate dip** (`not no_intermediate_dip`). Sage-verified precedence: `lands_near_ns_genuine = False`, `no_intermediate_dip = True` → honest verdict **FAIL** (plan FAIL_meaning verbatim: "d_s^M4 stays ≳4 with no intermediate dip → FAIL"). The guard contrast is printed in the script output AND the verdict extra-rows so the wrong reading cannot regenerate from the artifact.

**(4) Additive-decomposition cross-check — PASSES (machinery validated).** Heat kernels multiply on the M⁴×K product: `P_total(σ) = P_M4(σ)·P_fiber(σ)` ⇒ `d_s^total = d_s^M4 + d_s^SU(3)` (S52 PROVEN, EXACT). My fiber reconstruction from the L12 cache (166,896 modes, 31,956,720 weighted, 90 sectors) gives `d_s_fiber(σ_pivot) = 8.4470`, matching the inv-3 W2 fiber-transport baseline `ds_at_fold = 8.4847` to within 0.04 (`fiber_matches_inv3 = True`; the inv-3 fiber transport I=−0.2004 FAIL, SETTLED-NO). Reconstructed `d_s_total(σ_pivot) = 12.4470 = 4.0000 + 8.4470` (exact additive). This validates the product machinery against the independently-landed fiber result.

**(5) deg(T_{BZ→pivot}) DERIVATION (DEDUP FLAG iii — derived ONCE; substitution chain).**
- *Definition*: `T_{BZ→pivot}` carries a substrate observable `O = w·Ô` (rank-1 NNU, §VII.BS) from the BZ scale `M_KK` to the CMB pivot `k_pivot` (54.04-decade gap). `deg(T)` = homogeneity degree of `T` on the observable.
- *Step 1*: `d_s = −2 dlnP/dlnσ` is a LOG-DERIVATIVE ⇒ scale-free. Under `σ → λ²σ` (λ = scale ratio), Sage: `d_s` is INVARIANT (no λ, no amplitude A). So for d_s itself, `O^pivot = O^substrate` would hold (the T2-VACUOUS reading).
- *Step 2*: But the dimensionful return-probability AMPLITUDE `P_M4(σ) ∝ σ^{−d/2}` is NOT scale-free. Sage: `P(λ²σ)/P(σ) = λ^{−d}` ⇒ homogeneity degree `−d` in λ; per unit-λ the amplitude carries transport degree `d/2`.
- *Step 3*: For the d=4 base, `deg(T_{BZ→pivot}) = d/2 = 2`. Since `2 ≠ 0`, this is **NON-SCALAR** (NOT the §VII.BA T2-VACUOUS scalar case): `O^pivot ≠ O^substrate` for amplitude-carrying observables (n_s prefactor, A_s), which IS the 54.04-decade scale separation the n_s/α_s sector needs.
- *Cross-sector reconciliation*: S93 W7-1 (α_s/fiber channel) found `deg_T = 2.0000, T4-non-scalar, factorization_holds=False`. My independent M⁴-base derivation lands **exactly +2** (`deg_T_reconciles_s93 = True`) — corroboration from an orthogonal summand. Promoted to `canonical_constants.py` (`deg_T_BZ_pivot = 2.0`) for the W4 consumers CF3-TIMESCAPE-H0, CF-CO34-BUBBLE-LRDT, and the n_s/α_s sector (import, NOT re-derive).

**(6) K-anchor discipline.** `k_pivot_planck = 0.05` Mpc⁻¹ (Planck 2018) is the ONLY canonical pivot; the inv-3 `K_pivot_seed = 2.0` is a SEED, NOT canonical. The diffusion-variable pivot scale used here is the substrate's own fold-window `σ_* = d_s_fold_window_sigma = 1.4005` (S92-AD-HOC, treated as a cross-check anchor only, never the PASS anchor — the flat null d_s=4 is σ-independent so the verdict does not depend on this choice).

**(7) Dual-prior reallocation.** Pre-registered: reduces ~2 or ~3.91 → 0.9 Track A (CDT-in-base); no dip → 0.9 Track B (reduction-free both summands). Outcome: `no_intermediate_dip = True`, no genuine reduction ⇒ **0.9 to Track B** — the framework is reduction-free on both summands; the d_s≈3.91 the n_s sector needs has NO home in the spectral-dimension flow and must come from a different mechanism (the transport-degree scale-separation deg(T)=+2, NOT a dimensional reduction).

**(8) 4-tuple + SHAs.** `(value='d_s^M4_min=4.0000_…_deg_T_BZ_pivot=2_…', scheme=M4-summand-heat-trace; windowed-spectral-dimension, convention=base-fiber-product-Dirac; K=k_pivot_planck=0.05, L_max=12)`. regulator_pin `a_2^{ζ}` (Weyl-term leading heat-trace coefficient; poleconv-A-double, pole_in_s=3, curvature_grade_n=2). audit_sha256=`f60cff36…d6535`, content_sha256=`c7ae2817…fc6be`. Artifacts: `s110_cf_cv6b_ds_m4.py/.npz/.png`. Runtime path corrections (drift per `substrate-first-canonical-sourcing.md §(ii.B)`): fiber cache resolved to `session-84/s84_spectrum_cache_L12_tau019.npz` (plan `_shared/` path is a doc bug); inv-3 transport resolved to `inv3_w2_ds_flow_scale_transport.npz` (plan name `inv3_w2_1_ds_transport.npz` is a doc bug).

**Substrate framing**: GEOMETRIC. The arrow `D_M4 eigenvalues → P_M4(σ)=Tr e^{−σD_M4²} → windowed d_s^M4(σ) → CDT/AS reduction question + BZ→pivot transport degree`. The spectral dimension is NOT a property of a container the substrate sits IN; it is an intrinsic functional of the substrate's own heat trace, and d_s^total splits cleanly into base (M⁴) and fiber (SU(3)) summands. The S52 framing "CDT dimensional reduction is a foam effect on M4, not a property of D_K on the fiber" is PROVEN but was never computed on the M⁴ summand — this gate asks the base and finds it FLAT (d_s=4, no foam-reduction). The reduction-free-on-both-summands result is a substrate-IS structural statement: the framework keeps full Weyl dimension everywhere, contrarian to (and falsifiable against) every dimensional-reduction program. deg(T_{BZ→pivot})=+2 is the homogeneity degree of the substrate→pivot transport on the dimensionful heat-trace amplitude — the same machinery that scale-separates n_s/α_s by 54.04 decades — derived ONCE here so the downstream consumers share one substrate-derived value.

---

## Wave 3 Synthesis (team-lead)

**Tally**: 6 gates — 0 PASS, 2 INFO (CO1-EOS, CF2-YUK-EPSLX), 4 FAIL (CV2B, CO2-FALSIFIER [mechanical closure], CF1-YUK-C2COSET, CV6B). All disciplined pre-registered outcomes; sig_5 clean (12 distinct audit_sha256 across W2+W3); all 6 WP §-sections COMPLETED.

**Cross-gate keystone diagnosis (the M_KK register motion)**. W3 sits on the dimensionful axis; each gate is the rank-1 §VII.BS weight `w=M_KK` seen from a different side, and the wave's FAILs sharpen the constraint surface rather than weaken anything:

**(b) Structural changes**
- **M_KK keystone — Question-A vs Question-B resolved orthogonally**: CV2A (W2) transmutation-corridor **PASS** (derivation-IN-PRINCIPLE) + **CV2B FAIL = Fork-C** (the gauge-a₄ Tr F² channel does NOT independently fix the canonical VALUE — μ*=4.42e13 GeV, no root in [1e15,1e18], 167-OOM cross-scheme spread; the dimensionless channel has no power-law lever on the dimensionful keystone). **NET: M_KK stays gravity-a₂ frozen-since-S42, NOT up-tagged to "derived"** (HK-MKK). The rank-1 weight has exactly ONE canonical determination; a corridor-PASS does not multiply-determine the value.
- **Yukawa hierarchy — internal door SHUT, external up-sector door OPENS**: CF1-YUK-C2COSET **FAIL** (`|dY_12/dδ|=8.7e-16 ≪ eps_lift`; the selection-rule preflight shows the obstruction is **leg-membership** — the C²-coset T4 deformation acts ⊗1 on the multiplicity leg, commutant projection = 0 EXACTLY; rank-1 wall off-ALL left-invariant internal moduli, confirming WS-C2COSET Reading B, dual-prior → 0.95 Track B). CF2-YUK-EPSLX **INFO** (the external non-LI ε_LX with a DECLARED new d.o.f. — pairing-dependent off-diagonal texture {ρ13,ρ23} — beats the S100a baseline for the up-sector: m_c/m_u=589 vs PDG 589 [ld 0.000], m_t/m_c in-band, breaking the Sage-exact 9/5 diagonal-Casimir lock; but up-only ⇒ mass_grp 2/6 ⇒ NON-PROMOTION-BY-HELD-NUMBER). **Do NOT tag m_t:m_c:m_u "DERIVED"** (§VII.BL / capstone #7).
- **Spectral dimension — reduction-FREE on BOTH summands** (contrarian falsifiable signature): CV6B **FAIL** (d_s^M4 = 4.0000 flat, base has NO dimensional reduction; combined with the SETTLED-NO fiber d_s≈8.5). The d_s≈3.91 the n_s sector needs has NO home in the spectral-dimension flow — it comes from the transport degree, NOT a CDT/AS-style reduction. Antipodal to CDT/AS/Hořava.
- **Compact-object sector — sign-built but falsifier-STERILE**: CO2-FALSIFIER **FAIL** (mechanical closure, WS-CO-1=Reading-STERILE; the conditional anchor-free-falsifier trigger did not fire — 5th M_KK-keystone confirmation). CO1-EOS **INFO** (the self-consistent μ_eff CFL gate forces Δ/μ=0.102 in-band, but M_max=4.783 M_⊙ soft vs [2.0,2.6] and C_max below the 1e-3 floor — binding-magnitude gap partial).

**(a) Numerical revisions**
- `deg(T_{BZ→pivot}) = 2.0` NON-SCALAR (homogeneity d/2 for d=4 base) — **DERIVED ONCE** (dedup flag iii) on the M⁴ summand, promoted to `canonical_constants.py:716` (+ PROVENANCE :2018); reconciles S93 W7-1 deg_T=2.0000 EXACTLY (cross-sector).
- CV2B μ* = 4.4216e13 GeV (1680× below M_KK_gravity); scheme spread 167.1 OOM.
- CF2 up-ratios: m_c/m_u logdist 0.000 dex, m_t/m_c logdist 0.035 dex (vs S100a single-w 0.509 dex out-of-band).

**Effected In-Session (non-math)**:
- atlas-04 S110 W2/W3 results freshness line appended (`atlas-04-assumptions.md` — M_KK guard CV2A-PASS+CV2B-FAIL → no up-tag; C10 CCDARK1 BBN-wall-hardens; C2 CV6B reduction-free + deg(T)=2.0; S3 CCDARK-2 Reading-A Layer-A-scoped). Scoping/freshness notes, NOT status-cell flips (S110 reconciliation discipline).
- `deg_T_BZ_pivot=2.0` canonical promotion (by CV6B, on disk).
- Flagged for session-close: `/weave --update` to index the new `deg_T_BZ_pivot` constant + the W1 corpus (§25.5) / falsifier-inventory (Rows #88/#76/#12) edits.

## Carry-Forward Computations

The W3→W4 consumers are IN-SESSION (W4 imports `deg(T_{BZ→pivot})=2.0` → CF3-TIMESCAPE-H0 + CF-CO34-BUBBLE-LRDT + n_s/α_s; CO1 pressure-scale → CF-CO34). Genuine S111 math carry-forward:

### CF-S111-YUK-FULLFLAVOR — full-flavor Yukawa magnitude (down-sector + CKM + same-gen J-conjugacy lock)

1. **What**: extend the CF2-YUK-EPSLX up-sector INFO (mass_grp 2/6) to the full flavor sector — the 4 held-out slots (3 same-generation ratios J-conjugacy-locked to ≈1 by Λ_u=Λ_d, + the down-only m_s/m_d) structurally unaddressed by an up-sector texture; develop the down-sector ε_LX texture + the CKM angles.
2. **Inputs**: `s110_cf2_yuk_epslx.npz` (the up-sector pairing-dependent {ρ13,ρ23} texture); the J-conjugacy lock structure; PDG down-sector + CKM targets.
3. **Gate**: mass_grp ≥ 5/6 (down-sector ratios in-band + the same-gen lock resolved or its origin pinned); pre-register the band.
4. **Effort**: ~1–2 waves (the up-sector machinery exists; new work = the down-sector + CKM d.o.f., + resolving the J-conjugacy lock).

(M_KK canonical VALUE: settled gravity-a₂ frozen-since-S42; CV2B closed the gauge route — NOT a carry-forward. The M_KK absolute-convergence magnitude (CF-S94) is a pre-existing standing item.)

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-20 | M_KK canonical value (CV2B) | Question-B canonical value open (3-way fork) | Fork-C: gauge-a₄ channel does NOT fix value; gravity-a₂ SOLE canonical, frozen-S42 (no up-tag) | dimensionless Tr F² channel has no power-law lever; 167-OOM spread |
| 2026-06-20 | Rank-1 Yukawa wall (CF1-C2COSET) | off-su(2) only (W1 panel ~0.90 FAIL prior) | off-ALL left-invariant internal moduli (leg-membership obstruction; mult-leg commutant=0) | C²-coset T4 acts ⊗1 on multiplicity leg; dY_12=8.7e-16 |
| 2026-06-20 | Yukawa external route (CF2-EPSLX) | S100a single-w FAIL (mass_grp 2/6) | up-sector in-band (9/5 Casimir lock broken); mass_grp still 2/6 (up-only) → INFO, NON-PROMOTION; m_t:m_c:m_u NOT "derived" | pairing-dependent {ρ13,ρ23} texture; down+CKM held-out → CF-S111-YUK-FULLFLAVOR |
| 2026-06-20 | Spectral dimension (CV6B) | "drop-from-8" reading | reduction-FREE on BOTH summands (d_s^M4=4.0 flat, fiber 8.5); contrarian vs CDT/AS; deg(T)=2.0 minted | M⁴ heat-trace flat; d_s=3.91 has no base home |
| 2026-06-20 | Compact-object falsifier (CO2) | conditional on WS-CO-1=ESCAPE | sterile (WS-CO-1=STERILE); PRE-REG-INC mechanical closure; CF-CO-2 closed-not-run | upstream trigger did not fire |
| 2026-06-20 | Compact-object EoS (CO1) | binding-magnitude gap unpinned | Δ/μ=0.102 self-consistent in-band; M_max/C_max soft → INFO (partial) | self-consistent μ_eff CFL gate |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) |
|:-----|:-------|:------------|:------------|
| S110-CF-CV2B-GAUGE-A4 | s110_cf_cv2b_gauge_a4.py | ✓ | ✓ |
| S110-CF-CO1-EOS | s110_cf_co1_eos.py | ✓ | ✓ |
| S110-CF-CO2-FALSIFIER | s110_w3_co2_pre_reg_inc_closure.py (mechanical closure; no compute artifacts) | — | — |
| S110-CF1-YUK-C2COSET | s110_cf1_yuk_c2coset.py | ✓ | ✓ |
| S110-CF2-YUK-EPSLX | s110_cf2_yuk_epslx.py | ✓ | ✓ |
| S110-CF-CV6B-DS-M4 | s110_cf_cv6b_ds_m4.py | ✓ | ✓ |

All in `computations/session-110/` (closure script in `computations/_shared/`); verdict lines + dual-SHA companions in `s110_gate_verdicts.txt`.
