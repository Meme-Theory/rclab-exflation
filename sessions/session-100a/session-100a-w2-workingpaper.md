# Session 100a Wave 2 — Fermion-Mass Texture Cluster (Results Working Paper)

**Session**: 100 | **Wave**: 2 | **Plan**: session-100a-plan-w2.md | **Theme**: fermion-mass texture cluster — the literal Baptista Paper 14 §3 Dirac-mass overlap, computed two independent ways (overlap integral; Connes distance), plus the lepton-only Z₃ phase lever and the Casimir-widening discriminator.

## Gate Sections

### §W2-1. S100a-DUAL-Z3-PHI-POINTS (baptista-spacetime-analyst)

**Status**: COMPLETED
**Gate ID**: `S100a-DUAL-Z3-PHI-POINTS`
**Trigger**: `[SIGN]`
**Classification**: **PARTICLE**
**Agent**: `baptista-spacetime-analyst`
**Hypothesis**: At the three Z₃ phase-points φ ∈ {0, 2π/3, 4π/3} the diagonal weight c(φ)=1/(1+8cos²φ) collapses the three lepton generations to the 2-level multiset {1/9, 1/3, 1/3} (2-fold degeneracy at ±2π/3), while the quark matrices Ω^D, Ω^c carry no φ-dependence — the second Z₃ is a lepton-only lever.
**Plan reference**: `sessions/session-plan/session-100a-plan-w2.md` §W2-1 (machinery pin, thresholds, substitution chain source).

**MCP Pre-Compute Audit**:

| Query | Salient return |
|:--|:--|
| `search_knowledge("dual Z3 phase points lepton phi lever")` | No prior gate/closure covers the c(φ) Z₃-orbit collapse; nearest hits are the S63 generation-Z₃ work (`s63_generation_z3_output.txt` §16 — CPT-constrained Y on the FIRST Z₃/triality axis, a different construction) and unrelated phase/lever scripts (s50, s70). |
| `search_knowledge("Omega b mass matrix s_phi 8cos generation collapse")` | Surfaced `S97-YUKAWA-FAMILY-DERIVE` (FAIL, R_cross=1.0197) and the S62 theorem "Yukawa tree-level mass generation" (PROVEN — tree-level Yukawa vanishes by PW orthogonality). Both adjacent context, neither evaluates the Ω^b_g(φ) Z₃ phase-point structure. |
| `trace_entity("S97-YUKAWA-FAMILY-DERIVE")` | Confirmed predecessor: S97 FAIL, `R_cross_yukawa_t1_t2 = 1.019704` (multiplicity-scalar 1:1:1 vs PDG); S99 PROVEN-line: "a multiplicity-scalar operator cannot carry a generation index → democratic masses". This gate supplies the φ-weighting that observable ignored. |
| `search_knowledge("s_phi uniqueness family vertical transformation phase Baptista")` | No prior s_φ-family gate (hits are unrelated uniqueness gates: S84-DYNAMICS-UNIQUENESS etc.). |

**NOT PRE-CLOSED** — this is the first evaluation of the second-Z₃ (s_φ-phase) structure. Constants check: gate operator consumes NO numerical framework constant (closed-form rational identity); `tau_fold` and `Vol_SU3_Haar` confirmed present in `canonical_constants.py` and echoed in the `.npz` as context only (not load-bearing).

**Verdict**: **PASS** (composite; 3-tuple sign=PASS, magnitude=PASS, regime=VALID per the gate-verdicts.md collapse rule)

```
S100a-DUAL-Z3-PHI-POINTS: PASS -- value='c={1/9,1/3,1/3}exact;distinct=2;deg2@pm2pi/3;heavy/light=3;quark_dphi=0;haar(1/2)(1+8cos^2)ok' scheme=CLOSED-FORM-OMEGA-BG convention=EXACT-RATIONAL-QQ L_max=N/A audit_sha256=d23c7e99cba964035261235ef54b79876e89d2bd4b23d2e57f6f60151f94afe0 content_sha256=6a4e08ea7389d9a09213b567ccea0207337ae089744eef2fd9ff999b86daeb15 schema_version=S84+
# audit_sha256_short=d23c7e99cba96403 content_sha256_short=6a4e08ea7389d9a0 # S100a-DUAL-Z3-PHI-POINTS dual-SHA companion row; dual-Z3 lepton-only lever; eq 3.22 lineage; Sage-MCP cross-verified
# sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID # S100a-DUAL-Z3-PHI-POINTS 3-tuple annotation (schema-v2)
```

Emitted via the race-safe `emit_verdict` knowledge-MCP tool (4 rows incl. the eigenvalue-detail extra row; single lock-serialized writer; sig_5 unique).

**Results**:

4-tuple: `(value=c={1/9,1/3,1/3}exact;distinct=2;deg2@pm2pi/3;heavy/light=3;quark_dphi=0;haar(1/2)(1+8cos^2)ok, scheme=CLOSED-FORM-OMEGA-BG, convention=EXACT-RATIONAL-QQ, L_max=N/A)`

**Numbers (all exact rationals; float echoes 12 sig figs)**:

| Quantity | Exact (QQ) | Float | Test |
|:--|:--|:--|:--|
| c(0) | **1/9** | 0.111111111111 | — |
| c(2π/3) | **1/3** | 0.333333333333 | — |
| c(4π/3) | **1/3** | 0.333333333333 | — |
| multiset {c} vs {1/9, 1/3, 1/3} | equal | — | **exact MATCH** (tolerance 0.0) |
| distinct-value count | 2 | — | = target 2 (the 3 generations collapse to 2 levels) |
| 2-fold degeneracy at ±2π/3 | c(2π/3) = c(4π/3) | — | **exact** |
| heavy/light ratio | (1/3)/(1/9) = **3** | 3.0 | = target 3 exact, > 1 |
| quark ∂Ω^D/∂φ, ∂Ω^c/∂φ | Σ pairwise \|Δ entries\| = **0** | 0.0 | **exact zero** over Z₃ orbit + 2 generic probes (φ=0.7, 2.1) |
| Ω^b(0) spectrum | {94/27, 40/27, 40/27} | {3.48148148148, 1.48148148148 ×2} | numpy eigvalsh rel-dev 0.00e+00 < rtol 1e-12 |
| Ω^b(±2π/3) spectrum | {34/9, 16/9, 16/9} | {3.77777777778, 1.77777777778 ×2} | Z₃-pair spectra equal **exact**; rel-dev 0.00e+00 |
| M₀ = S1+S2+2·S3·I | diag(10/3, 4/3, 4/3) | — | off-diagonals exactly zero |
| Ω^D (eq 3.19) | (8/3)·I₃ | 2.667·I₃ | φ-flat exact |
| Ω^c (§3, ∝I₃) | (4/3)·I₃ | 1.333·I₃ | φ-flat exact |
| Haar moments | E\|s₁\|²=1/2, E\|s₂\|²=1/4, E[s̄₁s₂]=0 | — | exact Dirichlet; lineage c(φ)=α²(φ)/2 verified at all 3 points |

**Substitution chain (executed, plan §W2-1 verbatim with substituted numbers)**:

```
Definition 1: c(φ) = 1/(1 + 8·cos²φ)        [Baptista Paper 14 §3, eq (3.22) diagonal weight;
              lineage: eq (2.104) s_φ(h) = α[s₁(h) − 2(1+e^{2iφ})s₂(h)]]
Definition 2: Z₃ orbit = {0, 2π/3, 4π/3}    [cube-roots-of-unity arguments; the SECOND Z₃]

Step 1 (φ = 0):     cos(0) = 1   ⇒ cos² = 1   ⇒ c(0)     = 1/(1+8·1)   = 1/9
Step 2 (φ = 2π/3):  cos = −1/2   ⇒ cos² = 1/4 ⇒ c(2π/3)  = 1/(1+2)     = 1/3
Step 3 (φ = 4π/3):  cos = −1/2   ⇒ cos² = 1/4 ⇒ c(4π/3)  = 1/(1+2)     = 1/3

Collect:   {c} = {1/9, 1/3, 1/3};  distinct-value count = |{1/9, 1/3}| = 2
Direction: heavy/light = (1/3)/(1/9) = 3 > 1  [the heavy doublet sits at 3× the
           light-singlet weight — a genuine 2-tier split, NOT 1:1:1]
Conclusion: the s_φ-phase IS a Z₃ lever producing a 2-level generation collapse;
           the S97 1:1:1 degeneracy is BROKEN by the φ-weighted observable.
```

**Construction (Paper 14 §3 lineage, exact over Q(i,√3))**: the script builds the full Gell-Mann basis e_j = λ_j/2 (j=1..8) in exact field arithmetic and forms the eq (3.22)/(3.19) sums over ALL 8 generators (K-1e pin): S1 = Σe_je_j = (4/3)I₃ exactly (fundamental-Casimir cross-check), S2 = Σ4(e_j)₁₁e_j = diag(4/3,−2/3,−2/3), S3 = Σ((e_j)₁₁)² = 1/3, S4 = (S1)₁₁ = 4/3. Then Ω^b(φ) = S1 + S2 + (2S3 + S4·c(φ))I₃ — the φ-lever enters as the rigid diagonal shift S4·c(φ); per-generation weight recovered from the spectrum shift (eig − M₀)/S4 = c(φ_g) exactly. Generation g ↔ phase-point φ_g = 2πg/3 per the dual-Z₃ reading (first Z₃ = SU(3) triality channels; second Z₃ = the s_φ phase orbit, Paper 18 App E lineage).

**Haar-moment lineage (first-principles fiber integration)**: with the first column of Haar-SU(3) uniform on S⁵ ⊂ C³, exact Dirichlet moments give E|s₁|² = 1/2, E|s₂|² = 1/4, E[s̄₁s₂] = 0 (independent-phase vanishing), hence ∫_K|s_φ|²/(α²Vol) = 1/2 + |2(1+e^{2iφ})|²·(1/4) = 1/2 + 4cos²φ = (1/2)(1+8cos²φ). The unit-norm vertical profile therefore has α²(φ) = 2c(φ): **c(φ) IS the s_φ-family normalization weight** — the phase enters through the off-diagonal first-column monomials s₂ = h₁₁h₂₁+h₁₁h₃₁+h₂₁h₃₁ (eq 2.104) and lands in Ω^b as the diagonal weight after fiber integration. Verified exactly at all three points ((1/2)/N(φ_g) = c_g as Fractions).

**Quark φ-independence (exact-zero set test)**: Ω^D = S1 + (1/3)Tr(S1)I₃ = (8/3)I₃ (eq 3.19) and Ω^c ∝ I₃ (§3 transcription; color-Schur) evaluated at the 3 Z₃ points + 2 generic off-orbit probes — all pairwise entry differences exactly zero (Fraction arithmetic). Structural root: the D-sector vertical profile h·D·h̄ (eq 2.17) contains NO s_φ factor at any order, so its mass matrix cannot carry φ; the c-sector closed form carries no φ-term. The φ-lever is lepton-only.

**Convention pins (each shifts only the constant offset M₀, never the gate operator)**: (i) Hermitian Gell-Mann basis e_j = λ_j/2 (positive-Laplacian convention); (ii) all-8 generator sum (K-1e); (iii) eq (3.22) "(e_j)²₁₁" read as [(e_j)₁₁]² (reading A — the same bracket uses the distinct notation (e_je_j)₁₁ for entry-of-the-square); (iv) round metric normalization (the transcribed eq 3.22 carries no λ_j weights; Jensen weights deform M₀ only). The c(φ)-multiset and quark-∂φ tests are invariant under all four.

**Cross-checks**: (1) independent Sage-MCP (sagecell QQ) verification pre-script — c-multiset [1/9,1/3,1/3], distinct=2, heavy/light=3, E|s₁|²=1/2, E|s₂|²=1/4, (1/2)(1+8cos²φ)−(4cos²φ+1/2)=0 symbolically, Ω^b eigs {94/27,40/27,40/27}/{34/9,16/9,16/9}, Z₃-pair degeneracy True — all agree with the in-script Fraction engine; (2) numpy.linalg.eigvalsh float cross-check max rel-dev 0.00e+00 < pinned rtol 1e-12; (3) cos² float/exact deviation < 1e-15 at all three points; (4) S1 = (4/3)I₃ Casimir identity exact.

**[SIGN] 3-tuple**: sign=PASS (pre-registered direction heavy/light > 1; computed 3 > 1 exact); magnitude=PASS (exact multiset match AND quark exact zero at tolerance 0.0); regime=VALID (closed-form exact arithmetic; no truncation/expansion window to breach). Composite → PASS.

**Assessment (substrate framing, PARTICLE-class)**: the substrate IS the SU(3) fiber; the three generations are its triality-distinct Peter-Weyl channels, and the s_φ-phase is the discrete Z₃ of the C² ⊂ su(3) deformation direction (the same C² carrying the Jensen Higgs |s(h)|² mode). The verified collapse {1/9, 1/3, 1/3} is the substrate's own statement that the three generations organize into a **1+2 level structure** under the second Z₃ — the heavy pair at exactly 3× the light singlet's diagonal weight — with the lever acting on the lepton (b) sector only. Within the b-sector matrix the (ν_L, e_L) doublet stays exactly degenerate (M₀ = 4/3 pair, SU(2)_L-protected) while e_R splits (M₀ = 10/3): the electroweak structure of the closed form is internally consistent. Flow: D_K fiber Peter-Weyl channels → Z₃ phase-weighting c(φ) → 2-level generation collapse → (downstream) charged-lepton mass envelope. **Feed to Item 6** (`S100a-YUKAWA-OVERLAP-OFFDIAG`): the dual-Z₃ {1/9, 1/3, 1/3} collapse structure is CONFIRMED and the φ-lever is lepton-only — Item 6's sector-assignment cross-check (overlap diagonal must respect the dual-Z₃ collapse, lepton sector) is licensed at full PASS-criterion strength.

**Output Artifacts**:

| Artifact | Path | Verification (content presence) |
|:--|:--|:--|
| script | `computations/session-100a/s100a_dual_z3_phi_points.py` | exists (39,373 B); `grep "from canonical_constants import"` → `from canonical_constants import *  # noqa: F401,F403  (tau_fold, Vol_SU3_Haar context echo)`; `grep -c "print_verdict_payload"` → 3 |
| data | `computations/session-100a/s100a_dual_z3_phi_points.npz` | exists (13,213 B); exact num/den arrays for c, M₀, Ω^b spectra + quark residuals + Haar moments + dual-SHA |
| plot | `computations/session-100a/s100a_dual_z3_phi_points.png` | exists (146,630 B); 2-panel — c(φ) Z₃-orbit collapse; Ω^b branches riding c(φ) vs exactly-flat quark lines |
| verdict line | `computations/session-100a/s100a_gate_verdicts.txt` | `grep -E "^S100a-DUAL-Z3-PHI-POINTS:.* audit_sha256=[a-f0-9]{64}"` → canonical PASS line (quoted under Verdict above); dual-SHA companion row + [SIGN] 3-tuple row + eigenvalue-detail extra row present |
| wp_section | this section | Status COMPLETED / Verdict / Output Artifacts / MCP Pre-Compute Audit blocks present |

---

### §W2-2. S100a-YUKAWA-OVERLAP-OFFDIAG (baptista-spacetime-analyst)

**Status**: COMPLETED
**Gate ID**: `S100a-YUKAWA-OVERLAP-OFFDIAG`
**Trigger**: `[SIGN]`
**Classification**: **PARTICLE**
**Agent**: `baptista-spacetime-analyst`
**Hypothesis**: The |s(h)|²-weighted overlap O_g = ∫_K Tr[ψ_g† |s(h)|² ψ_g] vol_{g_τ} on the triality tower (1,0)/(1,1)/(3,0) at L_max=12, τ_fold=0.19 yields a generation-DEPENDENT diagonal envelope (e lightest, ≥~2 OOM, heavy-end-compressed — not the S97 1:1:1) AND a nonzero off-diagonal w=|w|·e^{i·arg(w)} (t1↔t2) in one object — the unwritten Baptista Paper 14 §3 Dirac-mass overlap.
**Plan reference**: `sessions/session-plan/session-100a-plan-w2.md` §W2-2 (machinery pin, thresholds, substitution chain, fb_pair, dual_prior).

**Output Artifacts**:

| Artifact | Path | must_contain check |
|:--|:--|:--|
| script | `computations/session-100a/s100a_yukawa_overlap_offdiag.py` | `from canonical_constants import` ✓; `print_verdict_payload` ✓ (def + call) — grep-verified |
| data | `computations/session-100a/s100a_yukawa_overlap_offdiag.npz` | exists; keys incl. `O_g`, `d_i`, `widening_W`, `abs_w_phi`, `arg_w_M2_phi`, `eps_lx_block_phi0`, `evals_10/01/11/30/00`, `mu_H`, dual-SHAs (Item-7 HARD input; Items 8/9/14 soft) |
| plot | `computations/session-100a/s100a_yukawa_overlap_offdiag.png` | exists (4 panels: weighted spectra / envelope ladder / widening-vs-band / off-diagonal channel) |
| verdict line | `computations/session-100a/s100a_gate_verdicts.txt` | `^S100a-YUKAWA-OVERLAP-OFFDIAG:.* audit_sha256=[a-f0-9]{64}` ✓ + dual-SHA companion row ✓ + schema-v2 3-tuple row (`sign_verdict=PASS magnitude_verdict=INFO regime_verdict=VALID`) ✓ + 2 diagnostic companion rows — emitted via the race-safe `emit_verdict` knowledge-MCP tool (5 rows, lock-serialized, sig_5-unique) |
| wp_section | this section | Status/Verdict/Output Artifacts/MCP Pre-Compute Audit blocks present |

**MCP Pre-Compute Audit**:

| Query | Salient return |
|:--|:--|
| `search_knowledge("yukawa overlap Higgs mode s(h) fiber generation hierarchy")` | S62 PROVEN theorem "Tree-level Yukawa vanishes by PW orthogonality" (forces the leading diagonal into the \|s\|²-quadratic channel); `S97-YUKAWA-FAMILY-DERIVE` FAIL (`R_cross=1.0197`, wrong observable); S99 panel ansatz eq (A1) `O_g ≈ N(p,q)·exp[−Λ_def(p,q)/μ²]` (Gaussian-in-Laplacian). **NOT PRE-CLOSED** — no prior gate computes the \|s(h)\|²-weighted overlap; this is the first. |
| `get_constant("Vol_SU3_Haar")` | 8√3·π⁴ = 1349.74 (S44, Weyl-integration-corrected) — consumed as the normalized-Haar measure echo (volume-preserving Jensen ⇒ vol_{g_τ} = Haar exactly, Paper 13 eqs 2.37/3.35) |
| `get_constant("tau_fold")` | 0.19 (S12/S42, CONST-FREEZE-42) |
| `get_constant("R_cross_yukawa_t1_t2")` | 1.019704 (S97; §VII.BL generation-blindness obstruction; held number, NOT a framework prediction) — used as the cache-orientation cross-check anchor |
| `trace_entity("epsilon_LX left-invariance breaking multiplicity")` | no direct trace (ε_LX named only in S97+ registry prose) |
| `search_knowledge("deformed Laplacian Jensen directional weight Lambda_def sector")` | S16 machinery `scalar_laplacian_on_irrep`: deformed Casimir = scalar Laplacian (the Λ_def convention used for the scalar-channel anchor) |

**Verdict**: **INFO** — composite per the pre-registered gate-verdicts.md collapse rule (sign\_verdict=**PASS**, magnitude\_verdict=**INFO**, regime\_verdict=**VALID**). The envelope RESOLVES (strictly NOT the S97 1:1:1; e-channel strictly below heavy-channel) and the off-diagonal is nonzero with the exact second-Z₃ phase, but the widening lands outside [1.800, 1.8894] and the spread is sub-target — the plan's pre-registered INFO path: "routes the widening question to Item 7". Dual-prior posterior re-allocation: **unchanged at 0.6 (Track A) / 0.4 (Track B)** per the plan discriminator (INFO → unchanged).

**Results**:

Output 4-tuple: `(value='W=-4.663502_band[1.800,1.8894];spread=1.1031ef_min4;signlnEH=-1.1031;mono=False;d=[7.8935e-01,1.0000e+00,3.3183e-01];e_ch=(3, 0);|w|0=0.408248;argw_Z3={pi,+2pi/3,-2pi/3};w_t0chain=0_centerZ3;mu=0.819741_floor00;W_cas=9/5;W_scalar_spread=7.273;Rxrepro=1.019704', scheme=JENSEN-FIBER-OVERLAP-SU3-HAAR, convention=RATIO, L_max=12)`
Dual-SHA: `audit_sha256=871573da729c59722ee060b37c70741f8d917e2560fe11ef74910f6be3bd2925` (script ‖ canonical ‖ pinmap ‖ spectrum-cache-SHA, per the plan `audit_discriminators` 4-ingredient block), `content_sha256=e76d4952e6edd1e25c2b43ca83edadbffc833d909206016e42d405a86a5dd50d`. Spectrum-cache SHA verified against the plan-freeze pin `9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9` (HARD assert in-script).

*Construction pins (PRDR; fixed in the script header BEFORE compute).* The plan pins the integral form, the cache, the Haar normalization, and the observables; four construction freedoms were pinned structurally pre-compute: **P1** diagonal = per-sector block sum `S_g = Σ_{λ∈abs_evals(p,q)} exp(−λ²/μ_H²)` over the cached 16·dim Dirac eigenvalues (the S99-panel eq-A1 form; multiplicity included), times the exact-Haar kernel mean ⟨|ŝ|²⟩ = 1 (unit normalization α²(φ)=2c(φ), Item-5 lineage, verified exact: α²·E|s₀|² = (2/9)·(9/2) = 1); **P2** μ_H = global cached Dirac floor = λ_min(0,0) = 0.819741 (the fiber-singlet channel floor — the |S|² Higgs/modulus mode is fiber-constant under the left-invariant deformation, hence (0,0)-channel; the 4D modulus mass m_tau=2.062 M_KK is a potential-curvature mass, rejected as the smearing pin); **P3** off-diagonal = the s-LINEAR Dirac-mass element on the BDI pair (1,0)↔(0,1), Weingarten-exact (degree-2 < N=3 ⇒ SU(3)=U(3) moments; Wg(id)=1/8, Wg(swap)=−1/24, engine self-tested against ∫|h₁₁|⁴=1/6 and ∫|h₁₁|²|h₁₂|²=1/12 exact); **P4** 1:1:1-degeneracy FAIL floor = 0.05 e-folds (S97 signature sits at ~0.0195). No scan, no re-runs; the verdict reads the pinned primary only.

*Diagonal envelope (PRIMARY, μ_H = 0.819741, μ² = 0.671975):*

| sector | dim | n_evals | λ_min | O_g | d_i = O/O_max |
|:--|--:|--:|--:|--:|--:|
| (1,0) | 3 | 48 | 0.835894 | 8.206524 | 0.789352 |
| (1,1) | 8 | 128 | 0.872975 | 10.396533 | 1.000000 |
| (3,0) | 10 | 160 | 1.248264 | 3.449930 | 0.331835 |

g_lo = ln(O₁₁/O₁₀) = **+0.236543**; g_hi = ln(O₃₀/O₁₁) = **−1.103118**; monotone ladder: **False** (opposite signs); widening **W = g_hi/g_lo = −4.663502** ∉ [1.800, 1.8894]; spread = |ln(O_max/O_min)| = **1.103118 e-folds** (< 4 floor; PDG context target ~8.15); e-channel (argmin O) = **(3,0)**, heavy-channel (argmax O) = **(1,1)**; sign(ln d_e − ln d_heavy) = **−1.103118 < 0** strictly.

*Pre-registered criteria:* (i) sign **PASS** (envelope strictly resolves; NOT 1:1:1) · (ii) spread ≥ 4 **FAIL** (1.103) · (iii) gap-asymmetry **FAIL** (non-monotone) · (iv) W-band **FAIL** (−4.66) · (v) |w| > 1e-12 **PASS** (0.408248). Composite: sign=PASS ∧ magnitude=INFO ∧ regime=VALID → **INFO** (the magnitude-INFO clause is the plan's INFO_meaning verbatim: envelope direction correct, widening needs the Item-7 closure).

*Substitution chain (numbers substituted; [SIGN] discipline):*
- Step 1 (defs): O_g = Σ_{λ∈g} e^{−λ²/μ²} (kernel mean 1); d_i = O_g/O_max; g_lo, g_hi, W, spread as above.
- Step 2 (μ pin): μ_H = λ_min over all 90 sectors = λ_min(0,0) = 0.819741 (verified equal, assert).
- Step 3 (floors): λ_min = 0.835894 / 0.872975 / 1.248264 ⇒ λ_min² = 0.6987 / 0.7621 / 1.5582. The plan Definition-3 premise λ_min ≈ √C₂/r is **falsified by the cache**: the floors crowd (floor(1,0)/floor(0,0) = 1.019704 = the S97 R_cross wall, reproduced to 2.7e-7 against the canonical constant) — the plan text had mislabeled the (1,0) sector MAX (1.327661) as its min.
- Step 4 (direction): e^{−λ²/μ²} monotone-decreasing ⇒ the e-channel (lightest, m ∝ O) = argmin O = (3,0) at the ladder top; computed ln d_e − ln d_heavy = −1.103 < 0 ⇒ sign **PASS**. At the SECTOR level the block sums are non-monotone in C₂: the (1,1) multiplicity (128 eigenvalues vs 48) overwhelms its 4.4% floor offset above (1,0) — the multiplicity-vs-floor competition breaks rung 1.
- Step 5 (band): W_Casimir = (6−3)/(3−4/3) = 9/5 = 1.800 exact (exact Fraction in-script); Jensen trace-mean slope J(τ_fold) = (3e^{2τ}+4e^{−τ}+e^{−2τ})/8 = 1.047319 is gap-ratio-NEUTRAL by the Dynkin identity Tr[π(T_a)π(T_b)] = (C₂·dim/8)δ_ab; computed primary W = −4.664 ∉ band ⇒ (iv) FAIL.
- Conclusion: envelope resolves with e at (3,0) and a strict sign; the Dirac-channel block-sum at the pinned Higgs-floor scale does NOT reproduce the 4-e-fold spread or the in-band widening ⇒ INFO, widening routed to Item 7.

*Off-diagonal w (one object, second channel; Weingarten-exact):* ‖M₁‖²_F = 3/4, ‖M₂‖²_F = 3/8 exact; ⟨M₁,M₂⟩_F = 0 exact (disjoint support). |w|(φ) = α(φ)·‖M₁+β(φ)M₂‖_F/3 with β(φ) = −2(1+e^{2iφ}): **|w| = 0.408248 at all three Z₃ points** (the |β|² = 16cos²φ growth exactly cancels the α² = 2c(φ) normalization — a closed-form identity: α²·(‖M₁‖²+16cos²φ·‖M₂‖²)/9 = (2c)·(3/4+6cos²φ)/9 = (3/4)·2c·(1+8cos²φ)/9 = (3/4)·(2/9) = **1/6 exactly**, |w| = 1/√6). Phase: **arg(w_{M₂-channel}) = arg β(φ) = {π, +2π/3, −2π/3}** at the Z₃ orbit — the second Z₃ imprinted EXACTLY on the off-diagonal (the panel's Θ; CP seed; survives reality because J²=+1, BDI). Criterion (v) PASS with margin ~4×10¹¹ over the 1e-12 tolerance. The ε_LX seed block `[[d,|w|],[|w|,d]]` at φ=0 is emitted in the npz (`eps_lx_block_phi0`) for Wave-4 Item 14; |w| and arg(w) feed Wave-3 Item 9.

*Selection-rule finding (plan-text correction, honestly disclosed):* the plan substitution-chain's literal off-diagonal object ⟨ψ_(1,0)| |s(h)|² |ψ_(1,1)⟩ is **ZERO EXACTLY** — center-Z₃ proof: under h → ωh (ω = e^{2πi/3}·I), conj(f_(1,0)) pulls ω^{−1} while |s|² (triality-0) and f_(1,1) (triality-0) are invariant; Haar invariance ⇒ integral = ω^{−1}·integral ⇒ 0. (Equivalently CG: a triality-0 kernel cannot connect t=1 to t=0; the chain's parenthetical "carries C² ⊂ su(3) weight connecting triality-adjacent sectors" is the property of s(h) ∈ (2,0), not of |s(h)|².) The structurally-correct nonzero off-diagonal is the **s-LINEAR** Dirac-mass element on the BDI pair t1=(1,0) ↔ t2=(0,1) — which is also what the plan's own "t1↔t2" naming (the S97 triality classes), the Wave-3 `[[d,w],[w*,d]]` consumer, and the S99-panel partition specify; CG-allowed since (2,0)⊗(0,1) = (2,1)⊕(1,0) ⊇ (1,0). Both objects were computed; the verdict's (v) reads the allowed channel.

*Cross-checks:* (a) cache SHA = plan pin ✓ (HARD assert); (b) S97 wall reproduced: floor(1,0)/floor(0,0) = 1.019704 vs canonical R_cross_yukawa_t1_t2 = 1.019704 (dev 2.7e-7) ✓; (c) BDI pair (1,0)/(0,1) machine-degenerate: spectra max rel dev 3.7e-15, O rel dev 1.1e-15 (< the 1e-12 wave float pin) ✓ — the Item-5-licensed sector-assignment cross-check: the diagonal realizes the 2+1 structure (degenerate t1=t2 doublet + distinct third channel) mirroring the dual-Z₃ {1/3,1/3}+{1/9} collapse ✓; (d) Casimir anchor 9/5 exact ✓; (e) kernel exact-Haar engine anchors E|s₁|²=1/2, E|s₂|²=1/4, E[s̄₁s₂]=0, E|s₁|⁴=1/3 all exact ✓; kernel unit norm exact, relative variance E|ŝ|⁴−1 = **1/3 exact** (the un-factorized CG remainder — the quantified seat of the Item-7 Jensen-tilt closure); (f) PDG band-edge provenance: 1.8894 = ln(m_μ/m_e)/ln(m_τ/m_μ) ⇒ implied m_τ = 1.776 GeV ≈ PDG 1.77686 (the plan's band-edge formula label was inverted; the VALUE 1.8894 is the binding pin; canonical m_e, m_mu consumed, ln(m_μ/m_e) = 5.331599); (g) blocks complete: n_evals = 16·dim for all five sectors ⇒ the sums are EXACT for their sectors (no within-block truncation; L_max=12 only bounds which sectors exist) ⇒ regime VALID.

*Diagnostics (non-verdict, pre-registered as such):* per-mode mean W = **1.781924** (1.0% below the band floor 1.800), spread 2.071; floor-only W = 12.563, spread 1.279; scalar-channel (Λ̄_def = J·C₂) anchor W = **9/5 exact**, spread = J·ΔC₂/μ² = **7.273 e-folds** (inside the ±2 window of the ~8 target); μ-ribbon W = {6.85, −4.66, −0.85} at μ²·{½,1,2} — the primary's W is strongly μ-sensitive in the non-monotone competition regime, while the scalar-channel widening is μ-independent and exactly Casimir.

*Assessment (solution-space interpretation).* The gate breaks the S97 1:1:1 (sign strictly resolves; spread 1.10 e-folds = 56× the S97 degeneracy scale) and lands the off-diagonal payload exactly (|w| = 1/√6 closed form; arg(w) = the second-Z₃ phase — the CP-seed structure the panel predicted, now Weingarten-exact). What the INFO localizes: the charged-lepton ENVELOPE does not live in the spin-dressed Dirac-block heat sums — the Dirac floors crowd (the S97 wall, faithfully reproduced) and the block multiplicities fight the floors, breaking rung-1 monotonicity. The Casimir ladder (W = 9/5, spread ~7.3) lives in the SCALAR-channel grading Λ̄_def = J(τ)·C₂ — exactly the S99-panel eq-(A1) Gaussian-in-LAPLACIAN form — and the per-mode diagnostic (W = 1.782, 1.0% under the band floor) shows the multiplicity-normalized Dirac data sits just below the Casimir value. Constraint mapped: the Higgs-overlap suppression exponent must be Laplacian-graded (scalar channel), not Dirac-floor-graded; Item 7's discriminator (which consumes this module and the C₂ ladder directly) adjudicates the widening; Item 8's regulator-invariant Connes route tests the same envelope independently. Dual-prior: **unchanged 0.6/0.4** (plan discriminator, INFO branch).

**Substrate framing** (PARTICLE with PHONONIC overlap content): the substrate IS the Jensen-deformed SU(3) fiber; the three charged-lepton generations ARE its triality-distinct Peter-Weyl channels, and a generation's mass weight IS the channel's spectral weight at the Higgs channel's own floor — not a Yukawa imposed from outside. Flow: D_K Peter-Weyl channels → Casimir/Laplacian grading (scalar channel carries the 9/5 ladder; Dirac floors carry the S97 crowding) → |s(h)|²-weighted channel weights → envelope + the s-linear BDI off-diagonal carrying the second-Z₃ phase → (downstream) charged-lepton hierarchy + mixing/CP seed. The measurement localizes WHERE in the fiber's spectral anatomy the hierarchy exponent lives; no metric expansion, no container.

---

### §W2-3. S100a-CASIMIR-WIDENING (kaluza-klein-theorist)

**Status**: COMPLETED
**Gate ID**: `S100a-CASIMIR-WIDENING`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC**
**Agent**: `kaluza-klein-theorist`
**Hypothesis**: The integral-derived envelope widening W from the Item-6 |s(h)|²-weighted overlaps equals the consecutive-Casimir-gap ratio 9/5=1.800 on the triality tower C₂=(4/3,3,6) — landing in [1.80,1.89] — discriminated against 1.333 (wrong fundamental (k,0) tower) and 3.0 (generic equal-spacing, Casimir ladder refuted).
**Plan reference**: `sessions/session-plan/session-100a-plan-w2.md` §W2-3 (Casimir machinery, discriminator bands, substitution chain, fb_pair).

**MCP Pre-Compute Audit**:
- `search_knowledge("Casimir widening 9/5 generation envelope triality tower")` → S99 mack-synthesis open-channel rows ("Casimir candidate" `3/(5/3) = 9/5 = 1.800`; "PDG widening ratio" 1.889) + this plan's own equation entries; **no prior evaluation of this gate** — NOT PRE-CLOSED.
- `search_knowledge("yukawa overlap diagonal generation hierarchy Casimir ladder")` → S62 `Yukawa tree-level mass generation` PROVEN (tree-level Yukawa vanishes by PW orthogonality); `S97-YUKAWA-FAMILY-DERIVE` FAIL (R_cross=1.0197); no closure covering the widening-shape question.
- `get_constant("tau_fold")` → 0.19 (S12/S42, CONST-FREEZE-42); matches `tau_fold_used` in the Item-6 npz exactly.
- `list_constants("widening|casimir|lepton|m_mu|m_tau|m_e")` → `m_e` (S98, PDG 2024), `m_mu` (PDG 2024) imported for the PDG ln-gap cross-check; **trap avoided**: canonical `m_tau = 2.062` is the MODULUS mass at fold in M_KK units (S42 W2-1), NOT the PDG τ-lepton mass — the PDG-widening context number 1.8894 enters only as the plan-pinned band-edge reference, never recomputed from `m_tau`.
- Sage MCP `sage_eval` (exact QQ, independent of the in-script Fraction engine): `C2 tower [4/3, 3, 6]; g_lo = 5/3; g_hi = 3; W_cas = 9/5; C2(2,0) = 10/3; W_fund = 4/3; dims [3,8,10]; trialities [1,0,0]` — all five identity checks `True`.

**Verdict**: **FAIL** — composite via the pinned gate-verdicts.md collapse rule; 3-tuple `sign_verdict=FAIL`, `magnitude_verdict=FAIL`, `regime_verdict=VALID`. The integral-derived widening **W = −4.663502** lies outside ALL three pre-registered discriminator bands {PASS [1.80, 1.89], INFO 1.333±0.05, FAIL ≥ 2.5 named onset}: the overlap-diagonal ladder is **sign-inverted**, not Casimir-graded — and not generic-equal-spacing either.

**Results** (numbers first):

4-tuple: `(value=W=-4.663502_OUTSIDE-ALL-BANDS{...}, scheme=CASIMIR-LADDER-WIDENING, convention=RATIO, L_max=12)`.

*(1) Tower confirmation (plan step 1; exact rationals, dual-engine).* In-script `fractions.Fraction` + agent-side Sage-QQ agree exactly: C₂(p,q) = (p²+q²+pq+3p+3q)/3 gives C₂ = (4/3, 3, 6) on (1,0)/(1,1)/(3,0); dims = (3, 8, 10) (fundamental/adjoint/decuplet); trialities t = (p−q) mod 3 = (1, 0, 0). All exact-int comparisons against the Item-6 npz (`tower_pq`, `tower_C2_num/den`, `dims`, `W_casimir_num/den` = 9/5) match. Casimir gaps: g_lo^cas = 3 − 4/3 = **5/3**, g_hi^cas = 6 − 3 = **3**.

*(2) Structural anchor (plan step 3).* W_cas = 3/(5/3) = **9/5 = 1.800000 exact**. Fundamental-tower alternative (1,0)/(2,0)/(3,0): C₂(2,0) = 10/3, gaps (2, 8/3), W_fund = **4/3 exact**. Generic equal-Δlog reference: 3.0.

*(3) Integral-derived widening (plan steps 2+4 — THE gate quantity).* From the Item-6 diagonal overlaps d_i = (0.789352, 1.000000, 0.331835) on (1,0)/(1,1)/(3,0), recomputed independently in this gate's script:

```
Substitution chain (realised):
  Step 1: C₂(p,q) = (p²+q²+pq+3p+3q)/3                  [SU(3) quadratic Casimir]
  Step 2: tower (1,0)/(1,1)/(3,0) ⇒ C₂ = (4/3, 3, 6)    [exact; Sage-QQ + Fraction]
  Step 3: g_lo = ln(d₍₁,₁₎/d₍₁,₀₎) = ln(1.000000/0.789352) = +0.236543
          g_hi = ln(d₍₃,₀₎/d₍₁,₁₎) = ln(0.331835/1.000000) = −1.103118
  Step 4: W = g_hi/g_lo = −1.103118/+0.236543           = −4.663502
  Step 5: predicted W_cas = +9/5 = +1.800000 (positive; PASS band)
          computed  W     = −4.663502  ⇒ sign mismatch  ⇒ sign_verdict = FAIL
  Band read-off: W ∉ [1.80, 1.89] (PASS); |W − 4/3| = 5.997 > 0.05 (INFO);
          W matches NONE of the three discriminators     ⇒ magnitude_verdict = FAIL
```

The monotone-ladder premise d₍₁,₀₎ > d₍₁,₁₎ > d₍₃,₀₎ is FALSE: d₍₁,₁₎ = 1.0 is the MAXIMUM (adjoint channel overlap-enhanced above the fundamental), so the first rung runs the wrong way and the second runs steeply down — opposite-sign log-gaps, negative ratio.

*(4) Cross-checks (all at machine zero unless noted).* d_i reconstruction from raw O_g (= O_g/max O_g): dev 0.0e+00. Recomputed (g_lo, g_hi, W) vs Item-6 npz: devs (1.1e−16, 0.0, 1.8e−15). Per-sector floors λ_min = (0.835894, 0.872975, 1.248264) == min of each `evals_*` array: dev 0.0; μ_H = 0.819741 == min(evals_00): dev 0.0; Peter-Weyl block counts = 16·dim = (48, 128, 160) + 16: True (D_K block-diagonality, S22b). PDG ln(m_μ/m_e) recomputed from canonical m_e, m_mu = 5.331599: dev vs Item-6 0.0. τ_fold consistency: True. R_cross canonical consistency (`R_cross_yukawa_t1_t2`): dev 0.0. Spectrum-cache SHA triple-match (disk == plan pin 9e6d9cf7… == Item-6 npz): **True**. Item-6 npz SHA (4th audit ingredient): 23d386dfa7e6d54d… (runtime-pinned; npz was finalized after its verdict emission, so the runtime SHA is the canonical pin).

*(5) Where the Casimir grading breaks (floor-route decomposition).* λ²_min floors = (0.698718, 0.762085, 1.558163). Chord slopes d(λ²)/d(C₂): lo = 0.038020, hi = 0.265359 — **slope ratio 6.979380** vs 1.0 for a Casimir-linear spectrum. Algebraic identity verified to 1.8e−15: W_floor_only = (9/5)·slope_ratio = 12.562884. On the bi-invariant fiber (τ=0) the Laplacian floors ARE C₂-exact (Peter-Weyl), and any floor-graded widening would be 9/5 exactly; the Jensen deformation at τ_fold = 0.19 deforms the three sector floors non-uniformly (factor ~7 between consecutive chord slopes), and the |s(h)|² channel weighting then inverts rung 1 outright.

*(6) Diagnostics (non-gating, pre-registered as such in Item 6).* W_permode = 1.781924 (**−1.00% vs 9/5**, just below the PASS-band floor) — the per-mode Gaussian trace over each full sector block V₍p,q₎⊗ℂ¹⁶ washes out the floor deformation and recovers near-Casimir grading; W_floor_only = 12.562884; scalar-channel anchor = 9/5 exact BY CONSTRUCTION (ln d ∝ C₂ trivially reproduces the Casimir gap ratio — an anchor, not evidence).

*Assessment (solution-space interpretation; gate adjudicates the W2→W3 INFO row).* Per the plan's decision table, Item 6's INFO handed the envelope-SHAPE question to this gate. The answer is decisive on the pinned route: **the corridor "generation-envelope shape = consecutive-Casimir log-gaps realised through the |s(h)|²-weighted overlap diagonal" is CLOSED at τ_fold** — the realised ladder is sign-inverted (W = −4.66), which is neither the Casimir 9/5, nor the fundamental-tower 4/3 (sector re-assignment would NOT rescue it), nor the generic 3.0. The FAIL is therefore sharper than the pre-registered FAIL_meaning: the overlap diagonal is not "un-graded"; it is *channel-weighted with an adjoint enhancement* that no monotone C₂ relabeling reproduces. What survives in the neighborhood, as diagnostics: (i) the per-mode sector-trace route sits 1.0% below 9/5 — the Casimir ladder IS present in the full Peter-Weyl block traces, where the C₂-graded bulk of each KK tower dominates over the deformed floors; (ii) Item 6's scalar-channel (Laplacian-graded) form carries 9/5 exactly with spread 7.27 e-folds. Constraint mapped for the fb_pair backward consumer (Wave 4 §IV layer-separation ledger): the widening-as-fermionic-sector-ratio inherits FAIL on the Dirac-channel overlap diagonal; any surviving Casimir-shape claim must route through Laplacian/scalar grading or whole-tower traces, not through Dirac-floor overlap diagonals. Item 8 (Connes-distance ladder, §W2-4) tests the same envelope on a regulator-invariant route and is unaffected by this closure.

**Substrate framing** (GEOMETRIC): the widening is a property of the fabric itself — the SU(3) Peter-Weyl spectral structure — not of its excitations. The substrate IS the Jensen-deformed SU(3) fiber; its quadratic Casimir C₂(p,q) grades the Peter-Weyl channels, and the measurement asked WHICH geometric structure (triality tower 9/5 / fundamental tower 4/3 / no structure 3.0) the fabric's Higgs-channel overlap diagonal realises at τ_fold. The fabric's answer: none of the three — the Jensen deformation breaks the bi-invariant λ² ∝ C₂ floor grading (chord-slope ratio 6.98 ≠ 1) and the |s(h)|² channel weight enhances the adjoint channel above the fundamental, inverting the ladder's first rung. Flow: D_K Peter-Weyl channels → Jensen-deformed floors (Casimir grading broken at the floor level) → |s(h)|²-weighted overlap diagonal (rung-1 inversion) → W = −4.66 ≠ 9/5. The e→μ→τ spacing is NOT set by the Casimir ladder of the overlap diagonal; where the 9/5 ladder does live (whole-block traces, scalar-channel grading) is now a mapped boundary, not a hypothesis.

**Output Artifacts**:
- Script: `computations/session-100a/s100a_casimir_widening.py` (contains `from canonical_constants import` + `print_verdict_payload`; OMP-capped 8 before numpy per machinery pin)
- Data: `computations/session-100a/s100a_casimir_widening.npz` (W, gaps, exact num/den anchors, bands, floors, slopes, all cross-check devs, 3-tuple, dual-SHA)
- Plot: `computations/session-100a/s100a_casimir_widening.png` (A: ln d_i vs C₂ sign-inverted ladder; B: λ²_min floors vs C₂ with Casimir-linear continuation; C: W candidates vs discriminator bands)
- Verdict line: `computations/session-100a/s100a_gate_verdicts.txt` — canonical line + dual-SHA companion + schema-v2 3-tuple row + 2 structural companion rows, emitted via the race-safe `emit_verdict` MCP tool; `audit_sha256=67a71781b45ea5d4cb9e43a976464b4eb489fb2cf402b8f466f79ef82dfb4a05` (script+canonical+pinmap+item6_npz_sha per the plan audit block), `content_sha256=ce9f15fa3e9bb16261a6cd57908ecf177a9d1b5fb18abc07e72292bb28ea330e`
- This WP section §W2-3

---

### §W2-4. S100a-CONNES-DISTANCE-LADDER (connes-ncg-theorist)

**Status**: COMPLETED
**Gate ID**: `S100a-CONNES-DISTANCE-LADDER`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC**
**Agent**: `connes-ncg-theorist`
**Hypothesis**: Connes geodesic distances d_i between generation-states on the finite-D_F multiplicity bundle reproduce the SAME charged-lepton e-vs-heavy envelope (~8 e-fold spread) as the Item-6 overlap via mass=e^{−d_i/ℓ}, with widening ∈ [1.80,1.89] — an independent, regulator-invariant route to the same envelope.
**Plan reference**: `sessions/session-plan/session-100a-plan-w2.md` §W2-4 (S88-Connes-distance machinery, ℓ-calibration, widening band, fb_pair).

**MCP Pre-Compute Audit**:
- `search_knowledge("Connes distance generation states multiplicity bundle")` → the machinery gate `S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY-CONJECTURE` (INFO, value 0.9800418463588636, scheme=Connes-distance-finite-spectrum-identity-conjecture, convention=substrate-state-pair-canonical, registered in `s87_gate_verdicts.txt`; producing script `s87_w1b_connes_distance_finite_spectrum_identity.py`) + the S99 fermion-mass deliverable rows (`session-99-fermion-mass-connes.md`: Connes-distance program = best-bet ε_LX candidate) + the §VII.BL Generation-Blindness anchor. **No prior evaluation of THIS gate** — NOT PRE-CLOSED. The S87/S88 machinery lesson loaded: the full-M_n(C) Connes distance is regulator-divergent (CLASS-γ; any f(D²) commutes with D) — the construction below restricts to the commutative multiplicity-bundle channel algebra where the IKM distance is finite and regulator-free.
- `get_constant("m_tau")` → **2.062, NO PROVENANCE entry** — confirmed the name-collision trap: this is the S42 modulus mass at fold in M_KK units (canonical_constants line 497 comment), NOT the PDG τ-lepton mass, despite the plan-w2 Input-SHA ledger grouping it among "PDG charged-lepton masses". Remediated in-session per `math-scripts.md` canonical-write-order: `update_constant("m_tau_PDG", 1.77686, S100a, gate=S100a-CONNES-DISTANCE-LADDER)` added the genuine PDG τ pole mass WITH provenance BEFORE compute; the ℓ-calibration uses m_e, m_mu, m_tau_PDG (all PDG-provenance).
- Input verification: spectrum-cache SHA on disk == plan static pin `9e6d9cf7…ca0f8d9` (hard-fail guard in-script, PASSED); Item-6 npz LANDED (verdict INFO) → the same-envelope-two-ways cross-check computable (NOT INFO-pending).
- **Plan-text-drift note** (`substrate-first-canonical-sourcing.md §(ii.B)`): the plan's prose pin "(1,0) dim=3 |λ|_min=1.32766" misquotes the cache MAX of that sector (1.327661); runtime ground truth min = 0.83589351 — the same floors Item-6 consumed (`floors_lambda_min` identity dev 0.0e+00).

**Verdict**: **INFO** — composite via the pinned gate-verdicts.md collapse rule; 3-tuple `sign_verdict=PASS`, `magnitude_verdict=INFO`, `regime_verdict=VALID`. This is the plan's pre-registered INFO branch verbatim: **envelope reproduced** (sign correct, non-degenerate strict ladder, spread 7.14 e-folds ∈ [6,10]) **but the widening lands OUTSIDE [1.80, 1.89]** (W_Connes = 12.562884; greybody-reweighting / multiplicity-metric closure needed). Dual-prior re-allocation per the pre-registered discriminator: unchanged (0.6/0.4). The gate's designed FAIL mode — generation-DEGENERATE d_i (multiplicity-blindness) — did NOT occur.

**Results** (numbers first):

4-tuple: `(value=W_Connes=12.562884_OUTSIDE[1.8,1.89];spread=7.1378efolds_IN[6,10];…, scheme=CONNES-DISTANCE-MULTIPLICITY-BUNDLE, convention=substrate-state-pair-canonical, L_max=12)`.

*(0) Construction (frozen BEFORE compute; full derivation in the script docstring).* Finite real spectral triple (A_mult, H_F, D_F; J, γ): A_mult = self-adjoint part of ℂ⁴ — the **channel algebra** of the multiplicity bundle on {v=(0,0) vacuum/Higgs reference; (1,0); (1,1); (3,0)}. Per §VII.BL (STAGE-3-PERMANENT) A_K acts as the identity on the multiplicity index, so the metric-bearing algebra ON the bundle is the channel function algebra — the canonical Iochum–Krajewski–Martinetti finite-point setting in which the Connes distance is finite WITHOUT a Frobenius regulator. H_F = ℂ²_chir ⊗ ℂ⁴_chan ⊗ ℂ²_{p/ap} = ℂ¹⁶. D_F = **greybody-reweighted chiral star**: couplings t_g = 1/ω_g with ω_g = λ_g(τ_fold)² the channel D²-floor from the L=12 cache (κ=1 cache units, absorbed into ℓ — not a parameter); antiparticle star on the BDI-conjugate sectors (0,1)/(1,1)/(0,3). The greybody form t_g ∝ 1/ω_g is the unique Connes-metric realization of the S99 four-lens modulus exponent d_i/ℓ ↔ 2πω_i/κ ↔ k·C₂ (the star closed form gives d(v,g) = 1/t_g = ω_g EXACTLY, linear in the D²-floor, hence linear in C₂ at undeformed scaling — reproducing the plan's Casimir floor W = 3/(5/3) = **9/5 exactly** in the undeformed limit; the foam reading: the reference couples to channel g propagator-suppressed ∝ 1/ω_g, so the high-C₂ channel is most distant ⇒ lightest). **Ladder disambiguation** (frozen): verdict-bearing d_i = vacuum-referenced d_C(ω_v, ω_g) (the mass map needs one common reference — the same reference object as Item-6's |s(h)|² overlap); the N_eval "2 adjacent Connes distances" = the ladder gaps Δ₁ = d_e−d_μ, Δ₂ = d_μ−d_τ; the pairwise adjacent distances (Pythagorean star forms, NOT gaps) are a reported secondary diagnostic.

*(1) Floors, reality, KO-dim-6 (machine-zero unless noted).* Tower floors λ_g(τ_fold=0.19) = (0.83589351, 0.87297503, 1.24826413); strict ordering TRUE; BDI conjugate-floor equality max rel dev **1.2e−15** (the reality input that forces [J,D_F]=0). ω_g = λ_g² = (0.698717957, 0.762085410, 1.558163346). KO-dim-6 sign checks on the J-doubled triple: |J²−1| = 0.0, ‖[J,D_F]‖ = 1.6e−15, ‖{J,γ}‖ = 0.0 (ε″=−1), ‖{γ,D_F}‖ = 0.0 — (ε,ε′,ε″) = (+1,+1,−1) verified numerically. First-order residual max‖[[D_F,a],b°]‖ = **2.0450, REPORTED not asserted zero**: a generation-RESOLVING D_F on the multiplicity bundle necessarily sits outside every A_K-bimodule (§VII.BL) — the same structural root as the framework's standing order-one obstruction; the Connes distance formula requires only (A,H,D), and the J-compatibility constraint that the plan pins ([J,D_F]=0) HOLDS.

*(2) Connes distances: SDP = closed form; doubling- and regulator-invariance.* IKM SDP (cvxpy CLARABEL, tol 1e−8, gauge-fixed constant direction; all 22 solves `optimal`): d_C(v,(1,0)) = 0.698717956, d_C(v,(1,1)) = 0.762085410, d_C(v,(3,0)) = 1.558163343 — **max rel dev vs the exact star closed form d(v,g)=ω_g: 2.5e−09** (the SDP verifies the theorem; the substrate numbers are the cache floors). Doubling-invariance (16-dim J-doubled vs 8-dim single chiral star): 1.8e−09. **Regulator-invariance demonstrated**: Frobenius-bound R-sweep over 3 decades (R = 10/100/1000 × ω_max) moves d_C by ≤ **1.8e−09** — contrast the S87 full-M_n(C) lineage (machinery value 0.9800418463588636, INFO CLASS-γ) where d_C diverged ~linearly in R. The commutative-channel restriction makes the route functional-independent by construction, as the plan's convention pin claims.

*(3) Assignment, ladder, widening (substitution chain realized).*

```
Step 3 (closed): d_g = ω_g  ⇒  d-ladder (0.698718, 0.762085, 1.558163), strict, non-degenerate
                 (rel spread 0.5516 ≫ 1e-6 floor)
Step 5 (mass map): m = e^{−d/ℓ}, ∂m/∂d < 0  ⇒  most distant = lightest
                 ⇒ e = (3,0) [most distant], μ = (1,1), τ = (1,0)    [sign(d_e − d_τ) > 0 ✓]
Widening:        Δ₁ = d_e − d_μ = 0.796078;  Δ₂ = d_μ − d_τ = 0.063367
                 W_Connes = Δ₁/Δ₂ = 12.562884
Step-4 read-off: undeformed-Casimir prediction 9/5 = 1.800; measured 12.562884
                 = 6.979× the Casimir value  ⇒  band test [1.80, 1.89] FAILS (crit_iii False)
```

sign_verdict = **PASS** (crit_i: non-degenerate strict ladder, ℓ>0, e-most-distant exists — the pre-registered FAIL mode, degeneracy, is excluded at rel spread 0.55). The widening inflation factor 6.979 is bit-identical to §W2-3's chord-slope ratio 6.979380 (their `W_floor_only = (9/5)·slope_ratio = 12.562884`): the two gates agree exactly on WHERE the shape breaks — the Jensen fold compresses the (1,0)/(1,1) floor gap ~4.8× below Casimir-linear scaling and stretches the (1,1)/(3,0) gap ~1.4×.

*(4) ℓ-calibration + spread (criterion ii).* Centered OLS of ln m_i^PDG on d_i (the unique pairing-independent one-parameter least squares; the centering constant is the non-physical overall scale): slope = −8.305078 ⇒ **ℓ = 0.120408** (cache-units²), R² = 0.9228. Predicted spread (d_max−d_min)/ℓ = **7.137761 e-folds ∈ [6,10]** ✓ (PDG target 8.153991). Sensitivity variants (diagnostics, not verdict-bearing): τ-anchored 8.3169; adjacent-gap 5.9608 — the ~6–8 e-fold envelope magnitude is calibration-variant-robust. PDG anchors: m_e, m_mu, **m_tau_PDG = 1.77686 GeV** (added this session with provenance; W_PDG = ln(m_μ/m_e)/ln(m_τ/m_μ) = 1.889036 recomputed from the canonical PDG values, consistent with the plan's 1.8894 band-edge anchor).

*(5) Same-envelope-two-ways cross-check vs Item-6 (npz LANDED, test computable).* Floors identity (same cache): dev 0.0e+00. **e-sector: Item-6 (3,0) vs Connes (3,0) — MATCH.** The two routes' lightest-channel identifications agree, and Item-6's e-assignment came from the FULL |s(h)|²-weighted spectral-sum overlaps O_g (kernel-weighted whole-sector sums), not from the floors alone — so the e-end agreement is a genuine two-functional consistency, while my W = 12.562884 vs their floor-only diagnostic 12.562884 (rel dev 3.8e−09) is a SAME-SOURCE identity check (both are the floor-quadratic ladder), not independent evidence. Full 3-sector mass-ordering Spearman ρ_S = **0.5** (one heavy-pair transposition: Item-6's overlap ladder puts (1,1) heaviest, the Connes floor ladder puts (1,0) heaviest). Item-6's own overlap widening −4.663502 (rung-1-inverted, non-monotone) vs my monotone 12.562884: both outside [1.80,1.89], failing in different directions.

*(6) Bare-metric contrast (pre-registered diagnostic, not verdict-bearing).* The UNreweighted two-point metric d = 1/λ gives W_bare = 0.1476 with the assignment FLIPPED (e=(1,0)): the band cleanly discriminates the greybody-reweighted metric (monotone-in-C₂ ladder, e=(3,0), matching Item-6's computed envelope) from the bare one — the reweighting is load-bearing, not cosmetic.

| criterion | pre-registered | measured | verdict |
|:--|:--|:--|:--|
| (i) sign: non-degenerate strict ladder, e most distant, ℓ>0 | degeneracy floor 1e−6 | rel spread 0.5516; e=(3,0); ℓ=0.1204>0 | **PASS** |
| (ii) spread ≈ 8 ± 2 e-folds | [6, 10] | 7.1378 | **PASS** |
| (iii) widening W_Connes | [1.80, 1.89] | 12.562884 | **FAIL** |
| magnitude (ii ∧ iii; INFO if ii ∧ ¬iii) | — | envelope yes, shape no | **INFO** |
| regime (SDP conv., closed-form ≤1e−6, R-sweep ≤1e−8, KO checks) | — | 2.5e−09 / 1.8e−09 / machine-zero | **VALID** |

*Assessment (solution-space interpretation).* The gate asked whether the spectral-triple metric route recovers the charged-lepton envelope, with three possible worlds: (a) degenerate d_i — multiplicity-blindness re-confirmed (Track B); (b) envelope + widening both reproduced (Track A, independent confirmation); (c) envelope yes, shape no. The substrate answered **(c)**, and sharply: (i) the multiplicity-bundle Connes metric is **generation-RESOLVING** (0.55 rel spread — the §VII.BL degeneracy obstruction does NOT propagate to the greybody-reweighted state-space metric; the metric lives exactly in the ε_LX complement the S99 reframe requires); (ii) the **e-end of the envelope is now two-route consistent** — overlap functional and Connes metric independently select (3,0) (highest Casimir, most greybody-suppressed) as the electron channel, inverting the wave's pre-registered e↔(1,0) convention in BOTH routes; (iii) the **~8-e-fold magnitude survives** (7.14 in-band, variant-robust 5.96–8.32); but (iv) the **widening shape fails on the floor-graded route, identically in both gates** — W = 12.5629 here = (9/5)×6.9794 = §W2-3's floor decomposition. Constraint mapped: *the corridor "charged-lepton widening from FLOOR-graded multiplicity-bundle observables at τ_fold" is now closed on two routes* (W2-3 overlap diagonal: sign-inverted −4.66; W2-4 Connes floor-metric: monotone but 6.98× too wide). The Casimir 9/5 shape survives only in whole-block spectral content (§W2-3's per-mode trace W_permode = 1.7819, −1.0% below 9/5). Forward route for the Connes side (CF-ready, 4-field): replace the floor couplings t_g = 1/λ_g,min² by whole-block heat-trace couplings t_g = 1/⟨ω⟩_g with ⟨ω⟩_g the per-sector Gaussian-trace mean energy (inputs: L=12 cache + this gate's star machinery; gate: W_Connes^block ∈ [1.80,1.89] with the SAME ℓ-calibration scheme, pre-registered before compute; effort: ~1 agent-hour — the star closed form makes it a floors→block-means substitution). Per the Wave-2→3 decision table this INFO leaves Item 6's |w| seed handling unchanged; for the fb_pair backward consumer (Wave 4 §IV layer-separation ledger): the Connes-route widening inherits the same floor-localization boundary as W2-3 — any surviving Casimir-shape claim routes through whole-block traces, not floors.

**Substrate framing** (GEOMETRIC): the Connes geodesic distance IS the intrinsic metric of the fabric's finite internal structure — the substrate IS the finite spectral triple, and the three generation channels sit at substrate-defined distances from the vacuum/Higgs channel. The measurement asked the fabric two questions. First: does your state-space metric distinguish the generation channels at all? Answer: yes — d = (0.6987, 0.7621, 1.5582), a strict ladder; the fabric's metric resolves generations even though its homogeneous Dirac spectrum cannot (§VII.BL). Second: is the ladder's shape the undeformed Casimir 9/5? Answer: no — at τ_fold the Jensen deformation has compressed the (1,0)/(1,1) floors into the van-Hove fold pile-up (gap 0.0634 vs Casimir-ideal ~0.31) while (3,0) escapes upward, so the floor-graded metric carries W = 12.56. Flow: D_K sector floors (Jensen-deformed) → greybody-reweighted star D_F → Connes distances d_i = ω_g exactly → mass = e^{−d/ℓ} envelope: e = (3,0) most distant and lightest, ~7 e-folds, shape fold-distorted. The electron is the channel the fabric's foam transmits LEAST — most distant in the substrate's own metric — and the distance ladder is a property of the fabric, not of any container.

**Output Artifacts**:
- Script: `computations/session-100a/s100a_connes_distance_ladder.py` (contains `from canonical_constants import` + `print_verdict_payload`; OMP-capped 8 before numpy per machinery pin; cache-SHA hard-fail guard)
- Data: `computations/session-100a/s100a_connes_distance_ladder.npz` (full-float64 round-trip per Class 8.3: floors, ω, d_vac SDP+closed+single-star, Δ₁/Δ₂/W, pairwise diagnostics, R-sweep, KO-check residuals, first-order residual, ℓ/R²/spreads + variants, Item-6 cross-check block, criteria, 3-tuple, dual-SHA)
- Plot: `computations/session-100a/s100a_connes_distance_ladder.png` (A: distance ladder, SDP vs closed form; B: ln m^PDG vs d_i with ℓ-calibration line; C: widening candidates vs [1.80,1.89] band)
- Verdict line: `computations/session-100a/s100a_gate_verdicts.txt` — canonical line + dual-SHA companion + schema-v2 3-tuple row + 3 structural companion rows (S88-machinery lineage; KO-dim-6/first-order; m_tau_PDG promotion), emitted via the race-safe `emit_verdict` MCP tool; `audit_sha256=5e24db72e3e5121b445477e2433a3c50084a4c5951111297c439a2da9b63491a` (script+canonical+pinmap incl. spectrum-cache SHA, Item-6 npz SHA, S88 literal machinery pin), `content_sha256=fe31ed40146a9aa148ecb72a4161b130d256cde8beeeb5c3d4a78df1a31bb97e`
- Canonical-constants promotion: `m_tau_PDG = 1.77686` (SECTION E + PROVENANCE entry, gate-tagged) — canonical-write-order Step 2 executed in-session
- This WP section §W2-4

---

## Wave 2 Synthesis (team-lead)

**Date**: 2026-06-06. **Gates**: 4 (1 PASS, 2 INFO, 1 FAIL), executed in the plan's within-wave order 5 → 6 → {7 ∥ 8}. All four `[SIGN]` gates carry canonical verdict lines with full 64-char dual-SHA closures + schema-v2 3-tuples; all artifacts content-verified; sig_5 uniqueness holds.

### 1. The lepton-only lever is exact (W2-1)

**W2-1 (PASS)**: at the three Z₃ phase-points, c(φ) = 1/(1+8cos²φ) collapses the lepton generations to the exact 2-level multiset **{1/9, 1/3, 1/3}** (Sage-QQ; 2-fold degeneracy at ±2π/3; heavy/light = 3 exact) while the quark matrices carry ZERO φ-dependence (exact, over the orbit + generic probes). New lineage result: the Haar moments give ∫|s_φ|² ∝ (1/2)(1+8cos²φ), identifying **c(φ) = α²(φ)/2 as the eq-2.104 s_φ-family normalization weight** — the second Z₃ IS the s_φ phase, a structurally lepton-only lever.

### 2. The envelope EXISTS and breaks the S97 wall — but is not floor-Casimir-graded (W2-2 ∧ W2-3 ∧ W2-4)

**W2-2 (INFO, dual-prior unchanged)**: the |s(h)|²-weighted overlap diagonal breaks the S97 1:1:1 (spread 1.103 e-folds — 56× the degeneracy scale; sign(ln d_e − ln d_heavy) < 0 strict, e-channel = (3,0)) — but the envelope is NON-MONOTONE (g_lo > 0, g_hi < 0 ⟹ W = −4.66), landing the pre-registered INFO path that routes shape adjudication to Item 7. The off-diagonal lands EXACTLY: **|w| = 1/√6 = 0.408248 at all three Z₃ points** (the c(φ) normalization cancels |β|² identically) with **arg(w) = {π, +2π/3, −2π/3}** — the second-Z₃ phase on the BDI (1,0)↔(0,1) s-linear channel, the framework's CP seed. The plan-chain's literal ⟨(1,0)| |s|² |(1,1)⟩ = 0 exactly (center-Z₃/triality selection rule); the computed w is the structurally-correct s-linear object the Wave-3 `[[d,w],[w*,d]]` block consumes.

**W2-3 (FAIL — corridor closure with mechanism)**: the integral-derived widening W = −4.663502 sits outside ALL THREE discriminator bands. The floor decomposition isolates the cause exactly: W_floor = (9/5) × slope_ratio with slope_ratio = 6.979 (bi-invariant metric would give 1.0) — **the Jensen fold compresses the (1,0)/(1,1) eigenvalue floors into the van-Hove pile-up while (3,0) escapes**, so per-mode floors carry a fold-distorted, sign-inverted ladder. The 9/5 Casimir grading survives ONLY in whole-block Peter-Weyl traces (diagnostic W_permode = 1.7819, 1.0% below 9/5) and the scalar-Λ channel.

**W2-4 (INFO — independent route, same verdict structure)**: the Connes-distance ladder on the multiplicity bundle is strict and generation-RESOLVING (d = 0.6987 / 0.7621 / 1.5582; SDP = closed form at 2.5e-9; **regulator-invariant at 1.8e-9 over a 3-decade sweep** via the commutative channel-algebra restriction that cures the S87 CLASS-γ divergence). Envelope magnitude 7.138 e-folds ∈ [6,10] PASS-leg; e = (3,0) MATCHES Item-6's assignment (genuine two-functional agreement); but **W_Connes = 12.5629 = (9/5)×6.979, bit-identical to W2-3's floor decomposition** — the two independent routes agree exactly on WHERE the Casimir shape breaks (the Jensen-fold floor compression), closing the floor-graded widening corridor on BOTH routes.

### 3. Composite picture

Wave 2 establishes, on two independent functionals (overlap kernel; Connes metric): (a) the generation envelope EXISTS at ~the right magnitude (PDG spread 8.15 e-folds; routes give 1.1 diagonal / 7.14 metric); (b) the e-sector assignment is stable ((3,0) both routes); (c) the off-diagonal CP seed is exact and Z₃-structured; (d) the envelope SHAPE is NOT consecutive-Casimir at the floor/diagonal level — the fold's van-Hove compression is the named mechanism, and the Casimir grading retreats to whole-block traces (W_permode within 1% of 9/5). The surviving shape corridor is block-trace-graded couplings — CF below.

### 4. W2 → W3 decision-table application

Item 6 INFO row fires: Item 7 adjudicated the shape (FAIL — not Casimir-floor-graded); W3-9 proceeds PDG-self-contained with |w| as fit-output-only, reporting `seed_vs_fit_agreement` vs the substrate 1/√6 as a DIAGNOSTIC (dispatched under exactly this regime). Item-8-PASS-independent row: the Connes route stands as the regulator-invariant envelope anchor; no overlap-vs-Connes tension exists (the routes AGREE bit-identically on the widening decomposition) — no workshop seed from divergence.

### Effected In-Session (NON-MATH — team-lead orchestrator)

- [x] `m_tau_PDG = 1.77686` PROVENANCE promotion + name-collision documentation (canonical `m_tau = 2.062` is the S42 MODULUS mass, not the lepton; plan-ledger mis-grouping documented in §W2-4) — effected in-gate by W2-4 via `update_constant`; orchestrator import-verified — `computations/_shared/canonical_constants.py` SECTION E — `5e24db72e3e5121b`
- [x] Plan-prose floor-pin misquote disclosed ((1,0) "min=1.32766" is the sector MAX; true min 0.83589351) — documented in §W2-2 + §W2-4 audit trails (frozen plan untouched; corrections live in WP + verdict companion rows)
- [x] Housekeeping ledger §A row A6 recorded — `sessions/session-100a/session-100a-housekeeping.md §A`
- [x] Orchestrator-direct presentation patches: none required (all four sections landed complete; zero must_contain misses)

## Carry-Forward Computations

### CF-S101-W2-BLOCKTRACE-WIDENING — whole-block heat-trace widening test (the surviving Casimir-shape corridor)

1. **What**: Compute the generation-envelope widening on whole-block Peter-Weyl heat-trace couplings (per-block traces, NOT per-mode floors): W_block = g_hi/g_lo on block-trace couplings for (1,0)/(1,1)/(3,0) at τ_fold, L_max=12 — testing whether the Casimir 9/5 grading is carried at the block-trace level (both W2-3's W_permode = 1.7819 and W2-4's fold-compression decomposition point here; the per-mode/floor level is CLOSED by this wave).
2. **Inputs**: `computations/session-84/s84_spectrum_cache_L12_tau019.npz` (SHA 9e6d9cf7…); `computations/session-100a/s100a_casimir_widening.npz` (W_permode machinery; audit `67a71781b45ea5d4`); `computations/session-100a/s100a_yukawa_overlap_offdiag.npz` (kernel + μ_H; audit `871573da729c5972`); `computations/session-100a/s100a_connes_distance_ladder.npz` (floor decomposition; audit `5e24db72e3e5121b`); canonical tau_fold, Vol_SU3_Haar.
3. **Gate**: `S101-W2-BLOCKTRACE-WIDENING` — PASS iff W_block ∈ [1.800, 1.8894]; INFO iff |W_block − 4/3| ≤ 0.05 (fundamental-tower re-key); FAIL otherwise (closes the last Casimir-shape corridor; envelope shape becomes fold-dynamical, feeding the W3 freeze-in reading).
4. **Effort**: ~0.5 wave-equivalents (cache reads + block traces; no new diagonalization).

> **Addendum (2026-06-07, `/rclab-investigate` consolidation)**: two Q2 items below surfaced FIRST at investigation (`workshops/_seed-w2.md` carry-forwards; upstream wave-synthesis miss — housekeeping §B carried only CF-S101-HK-1 and §D was empty at session close). Canonical Q2 routing (housekeeping §D / §B appends) is the orchestrator's; these blocks are the WP mirrors `/rclab-plan` consumes. The S2-1 counting-convention workshop (`session-100a-workshop-schedule.md` W-2) amends CF-S101-W2-BLOCKTRACE-WIDENING's pre-registration (counting-convention pin + heavy-pair-ordering sub-criterion) BEFORE S101 plan-freeze.

> **AMENDED by W-2 workshop (2026-06-07, `workshops/s100a-w2-mass-functional-counting-workshop.md` R2-B B-item 2 — counting-convention pin + heavy-pair-ordering sub-criterion + route-fork closure)**: the six-item text below SUPERSEDES fields 1–4 above for S101 plan-freeze consumption. The original pre-registration is PRESERVED above for the audit trail; this is the amendment the addendum pre-authorizes.
>
> 1. **What**: Compute the generation-envelope widening on **multiplicity-NORMALIZED** whole-block observables at τ_fold, L_max=12, tower (1,0)/(1,1)/(3,0), under the workshop-pinned counting convention — the normalized channel-STATE class: every mass-bearing channel functional is a state evaluation ρ_g(f(D_K)) of ρ_g = P_g/Tr(P_g) (NCG state axiom + Paper-14 §3 Rayleigh-quotient lineage + CCM-2007 intensive/extensive partition; workshop verdict item 1). Block-SUM counting is EXCLUDED for mass use — it is the unique unnormalized object on the table; its ln n_g staircase is a K₀-rank (topological) datum (workshop B2/C2). Two faces, both computed: **(F2-flat, PRIMARY)** ⟨λ²⟩_g = ρ_g(D²) = (1/n_g)Σ_{λ∈g} λ² (μ-free block trace-mean), W_flat = (⟨λ²⟩₃₀−⟨λ²⟩₁₁)/(⟨λ²⟩₁₁−⟨λ²⟩₁₀); **(F2-weighted, SECONDARY)** ⟨ω⟩_g = Σλ²e^{−λ²/μ_H²}/Σe^{−λ²/μ_H²} at μ_H = 0.819741 (P2 inheritance), star couplings t_g = 1/⟨ω⟩_g per the W2-4 CF form, W_block analogous. The already-measured per-mode Gaussian face (W_permode = 1.781924) is reported as cross-face consistency, NOT gated. Design note: the two faces are the class's two maximally-pinned members — F2-flat annihilates the μ-axis (μ-free), F2-weighted annihilates the counting-axis (cancellation identity) — one compute spans both machinery axes of the Wave-2 dispute.
> 2. **Inputs**: `computations/session-84/s84_spectrum_cache_L12_tau019.npz` (SHA 9e6d9cf7…); `computations/session-100a/s100a_casimir_widening.npz` (audit `67a71781b45ea5d4`); `computations/session-100a/s100a_yukawa_overlap_offdiag.npz` (μ_H pin; audit `871573da729c5972`); `computations/session-100a/s100a_connes_distance_ladder.npz` (star machinery; audit `5e24db72e3e5121b`); this workshop's verdict (counting pin + ordering direction); canonical tau_fold, Vol_SU3_Haar.
> 3. **Gate**: `S101-W2-BLOCKTRACE-WIDENING` — composite [SIGN]: **(ordering sub-criterion, sign_verdict)** strict C₂-monotone ladder ⟨λ²⟩₁₀ < ⟨λ²⟩₁₁ < ⟨λ²⟩₃₀ ⟺ heavy-pair direction τ = (1,0), μ = (1,1), e = (3,0) — pre-registered from the workshop's two substitution chains (B2 overlap; Re:B2 metric); violation ⇒ sign FAIL (closes the normalized-counting corridor too). On the SECONDARY face the same ordering check is counting-convention-INDEPENDENT (multiplicative-normalization cancellation identity, `math-scripts.md` MANDATORY K=3, instantiated on the counting axis — Re:B2(ii)): a weighted-face ordering violation falsifies the direction for BOTH counting positions simultaneously. **(magnitude)** PASS iff W_flat ∈ [1.800, 1.8894]; INFO iff |W_flat − 4/3| ≤ 0.05 (fundamental-tower re-key); FAIL otherwise (envelope shape becomes fold-dynamical, feeding the W3 freeze-in reading). **(analytic anchor, non-gating)** τ=0 control via the Lai-Teh Thm-2.3 closed form λ² = (3/2)[C₂(μ_w)+C₂(V)] + 9/4 (LC t=1/2; no diagonalization): pre-registered prediction W_flat(τ=0) = 9/5 EXACT (trace-mean Casimir-linearity, canonicity-branch-invariant in ratio); deviation > 1e-10 flags machinery error, not physics. RATIO-LEVEL control; the unit map cancels (closed form in (ρ,ρ)=3 units, cache in frame units = LT/9; W is a gap ratio — any global unit factor cancels). Absolute-level machinery validation is ALREADY LANDED (S100b W3-2 per-sector Thm-2.3 match 8.9e-15, audit `bea5401ae1ac3c4d`) — cited, not re-run. **(μ-robustness, non-gating)** ordering stability of ⟨ω⟩_g across μ_H²·{½, 1, 2}. **(cumulant diagnostic, non-gating)** report sector variances Var_g and check the second-order identity W^PM ≈ W_flat·[1 + (s/2)(ΔVar_lo/Δ_lo − ΔVar_hi/Δ_hi)], s = 1/μ_H² (workshop R2-A A-C3); the sign of W_flat − W^PM was adjudicated NOT structurally pre-registrable — no one-sided bound is inherited; the primary carries genuine two-sided risk.
> 4. **Effort**: ~0.5 wave-equivalents (cache reads + block means + closed-form τ=0 control; no new diagonalization).
> 5. **Convention pin**: verdict line carries `convention=RATIO-NORMALIZED-TRACE-MEAN` (counting axis pinned per s100a-w2 workshop; fifth pin axis, SUGGESTION K=1). Re-running the same observable under `RATIO-BLOCKSUM` post-hoc is PROHIBITED_ACTIONS Class 1; the block-sum class is closed for mass-functional use by the workshop adjudication (it remains legitimate for extensive observables — degeneracy/occupation/relic/action-moment statistics). **Route-fork closure**: the star-metric face is closed-form-identical to the trace-mean face — d(v,g) = 1/t_g with t_g = 1/⟨λ²⟩_g (resp. 1/⟨ω⟩_g) gives d_g = ⟨λ²⟩_g (resp. ⟨ω⟩_g) EXACTLY (star closed form; SDP dev 2.5e-09, audit `5e24db72e3e5121b`) — this gate's verdict binds BOTH the overlap-route and the metric-route successor claims; the W2-4 §-Assessment forward route (t_g = 1/⟨ω⟩_g) is SUBSUMED, and no separate S101 Connes-route gate is planned (one compute, both routes; the fork closes by theorem, not by choice).
> 6. **Reference-channel pin**: `reference_channel = (0,0)` (vacuum/Higgs channel — common to W2-2 P2, μ_H = λ_min(0,0), and W2-4 d(v,·), v = (0,0)). This pin is b-component-specific per the global-map disposition: the reference convention is degree-graded (Ω⁰/amplitude class references the unit's channel, where its coupling is extremal; the Ω¹/derivation class references its own structural zero, the m₁ = 0 slot — [D,1] = 0 annihilates (0,0), so (0,0) cannot reference the ν-sector). A successor silently re-referencing a different channel violates this pin.
>
> *Scope annotation (functional-independence)*: the S100a-M0-FUNCTIONAL-SENSITIVITY pin (audit `2993dbf63fcb25d9`) covers RATIOS and their discrete images along the REGULATOR-SCHEME axis at fixed counting convention; μ/τ ASSIGNMENTS are counting-convention-dependent — pinned here as the fifth axis `convention=RATIO-NORMALIZED-TRACE-MEAN`; the mass-map monotone direction is the assignment functional's THIRD pinned input (workshop B3/Re:B3 + R2-B B-item 7).
> *CF-S101-HK-1 cross-reference (ordering caveat)*: the foam-protection landing text carries the workshop's ordering caveat (B6(iii) disposition): the ε_LX diagonal d-entries are `RATIO-BLOCKSUM`-tagged (as-computed P1 class) with μ/τ orientation re-pinned τ = (1,0), μ = (1,1); the off-diagonal payloads (|w| = 1/√6, arg w ∈ {π, ±2π/3}) and the max_C = 0.0 topological claim are counting-INDEPENDENT and orientation-ROBUST; caveat dischargeable once this gate lands under the pinned convention.

> **Rider (2026-06-07, W-3 carrier workshop R2-B Effected item 5, routed via orchestrator)**: CF-S101-W2-BLOCKTRACE-WIDENING additionally publishes its ⟨λ²⟩_g triple npz under a pinned SHA and reports the OLS slope s̄(τ_fold) as a secondary output; S101-ENVELOPE-CARRIER-DISCRIMINATE Leg A consumes the SAME npz under the SAME audit SHA (one dataset, two gates — W-3 workshop Re:T1(5)/C-2).

### CF-W2-1 — selection-rule pre-flight for pre-registered nonzero matrix elements [Q2-methodology — registry-hygiene compute carry-forward; housekeeping §D mirror]

1. **What**: Extend the `math-scripts.md §"Double-Check Logic Before Compute"` substitution-chain discipline (directive-only diff per `feedback_rules-directive-only-no-session-info.md`; calibration instance → corpus) plus a `_machinery_feasibility_audit.py` sub-check: any plan substitution chain claiming a matrix element is "generically nonzero" MUST carry a center-character/triality CG-admissibility check at plan-freeze. Calibration instance: plan-w2 §W2-2's chain asserted ⟨ψ_(1,0)| |s(h)|² |ψ_(1,1)⟩ ≠ 0 via "C² ⊂ su(3) weight connecting triality-adjacent sectors" — group-theoretically FALSE (|s(h)|² is triality-0; the center-Z₃ proof gives 0 EXACTLY; the cited property belongs to s(h) ∈ (2,0), not |s(h)|²). Caught in-gate and honestly disclosed (§W2-2 selection-rule finding; verdict companion row line 40); a two-line center-Z₃ pre-flight would catch it at plan-freeze.
2. **Inputs**: WP §W2-2 selection-rule finding; `computations/session-100a/s100a_gate_verdicts.txt:40` companion row (audit `871573da729c5972`); `.claude/rules/math-scripts.md`; `computations/_shared/_machinery_feasibility_audit.py`.
3. **Gate**: `S101-HK-SELECTION-RULE-PREFLIGHT` — PASS iff the rule-file directive lands AND the audit sub-check ships with `--self-test` covering a synthetic positive (triality-violating nonzero claim → flagged) and a synthetic negative (CG-admissible claim → passes).
4. **Effort**: ~0.2 wave-equivalents.

### CF-W2-2 — W2-1 exact lepton-only Z₃ lever registry landing [Q2-hygiene — registry-hygiene compute carry-forward; housekeeping §B mirror]

1. **What**: Land the W2-1 closed-form exact result — c(φ) = 1/(1+8cos²φ) collapse to {1/9, 1/3, 1/3} (2-fold degenerate at ±2π/3, heavy/light = 3 exact); quark ∂φ ≡ 0 EXACT (Ω^D = (8/3)I₃, Ω^c = (4/3)I₃ φ-flat — the second Z₃ is a structurally lepton-only lever); c(φ) = α²(φ)/2 eq-2.104 s_φ-normalization lineage — as a registered exact-result entry in `sessions/permanent-results-registry.md`, batched alongside the CF-S101-HK-1 single-shot bridge-landing wave (same `registry-landing.md §"Bridge-Landing Script Architecture"` AFTER pattern). Currently PERMANENT-class exact material citable only from this WP.
2. **Inputs**: `computations/session-100a/s100a_dual_z3_phi_points.npz` (audit `d23c7e99cba96403`; Sage-QQ + Fraction dual-engine, tolerance 0.0); WP §W2-1; `computations/_bridge_landing_script_template.py`.
3. **Gate**: `S101-DUAL-Z3-REGISTRY-LANDING` — PASS iff the registry section matches the built promotion text post-fsync re-read (single-shot AFTER pattern) AND the verdict line lands with dual-SHA; FAIL emits once per `mechanical-closure-discipline.md`.
4. **Effort**: ~0.3 wave-equivalents.

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-06 | Second Z₃ as generation lever | hypothesis (S97 successor) | EXACT — c(φ) = {1/9, 1/3, 1/3}, lepton-only (quark ∂φ ≡ 0); c(φ) = α²(φ)/2 lineage identified | S100a-DUAL-Z3-PHI-POINTS PASS (`d23c7e99cba96403`) |
| 2026-06-06 | S97 1:1:1 generation-degeneracy wall (overlap diagonal) | 1:1:1 at L12/τ_fold (S97) | BROKEN — spread 1.103 e-folds, sign correct, e=(3,0); envelope non-monotone (W=−4.66); off-diagonal \|w\|=1/√6 exact, arg(w) Z₃-structured (CP seed) | S100a-YUKAWA-OVERLAP-OFFDIAG INFO (`871573da729c5972`) |
| 2026-06-06 | Casimir-gap envelope shape (floor/diagonal level) | OPEN (9/5 hypothesis) | CLOSED on BOTH routes — overlap W=−4.66, Connes W=12.56=(9/5)×6.979 bit-identical; mechanism = Jensen-fold van-Hove floor compression; 9/5 survives only at whole-block traces (W_permode 1.78) | S100a-CASIMIR-WIDENING FAIL (`67a71781b45ea5d4`) + S100a-CONNES-DISTANCE-LADDER INFO (`5e24db72e3e5121b`) |
| 2026-06-06 | Connes-metric generation resolution | §VII.BL obstruction (no generation-resolving D_F in A_K-bimodules) | metric RESOLVES generations (strict ladder, regulator-invariant 1.8e-9/3-decades) while the first-order residual 2.045 keeps the §VII.BL obstruction standing — resolution lives in the state-pair metric, not the operator | S100a-CONNES-DISTANCE-LADDER INFO (`5e24db72e3e5121b`) |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | JSON | Size |
|:-----|:-------|:------------|:------------|:-----|:-----|
| S100a-DUAL-Z3-PHI-POINTS | `s100a_dual_z3_phi_points.py` | `s100a_dual_z3_phi_points.npz` | `s100a_dual_z3_phi_points.png` | — | 39.4 KB / 13.2 KB / 146.6 KB |
| S100a-YUKAWA-OVERLAP-OFFDIAG | `s100a_yukawa_overlap_offdiag.py` | `s100a_yukawa_overlap_offdiag.npz` | `s100a_yukawa_overlap_offdiag.png` | — | 52.5 KB / 26.3 KB / 233.1 KB |
| S100a-CASIMIR-WIDENING | `s100a_casimir_widening.py` | `s100a_casimir_widening.npz` | `s100a_casimir_widening.png` | — | 34.4 KB / npz / 159.0 KB |
| S100a-CONNES-DISTANCE-LADDER | `s100a_connes_distance_ladder.py` | `s100a_connes_distance_ladder.npz` | `s100a_connes_distance_ladder.png` | — | 53.3 KB / 26.5 KB / 113.9 KB |

(All four gates emit to `computations/session-100a/s100a_gate_verdicts.txt` via the race-safe `emit_verdict` MCP tool.)
