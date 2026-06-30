# Investigation 3 Wave 3 — Mass-Quantization & Paasch Bridges (Results Working Paper)

**Investigation**: 3 | **Wave**: 3 | **Plan**: investigation-3-plan-w3.md | **Theme**: Connect the framework's Casimir-graded exponential mass namespace (S100a/S101) to Paasch's ~70-year exponential-mass program; harvest the survey's five untraveled bridges (UB1–UB5) as one solo + four compute gates.

**Verdict track**: `computations/investigation-3/inv3_gate_verdicts.txt` (emit via `emit_verdict(session=3, track="investigation", ...)` per `gate-verdicts.md §"Investigation-Track Canonical Path"`). compute AND solo gates each emit a verdict line + close their WP section; review/workshop gates (none in this wave) would close by artifact-existence only.

## Gate Sections

### §W3-1. INV3-W3-1-S0-PHI-FN-IDENTITY

**Status**: COMPLETED
**Gate ID**: `INV3-W3-1-S0-PHI-FN-IDENTITY`
**gate_type**: `solo` (executed by the MAIN orchestrator INLINE at `/rclab-coordinate` time — no subagent spawn; SAME full compute field-set + SAME closure as a compute gate)
**Trigger**: `[CHAIN]`
**Classification**: **PARTICLE** (φ_paasch is the bare (3,0)/(0,0) ratio; S₀ is the charged-lepton SHAPE selector / Casimir-envelope exponent)
**Agent**: `gen-physicist` (NOMINAL owner; runs solo / orchestrator-inline — "more independent than the finder verifying its own coincidence")
**Hypothesis**: The framework's empirically-selected charged-lepton SHAPE selector S₀ equals Paasch's φ_paasch raised to his golden-ratio factor fN=√5−1 (S₀ = φ_paasch^{fN}) to machine precision, exposing a shared two-transcendental structure between the dressed lepton hierarchy and Paasch's spiral.
**Plan reference**: `sessions/investigation/investigation-3/investigation-3-plan-w3.md` §W3-1 (machinery pin, three-zone thresholds, substitution chain source).

**MCP Pre-Compute Audit** (queries run BEFORE writing the script, per `knowledge-index-usage.md`; NOT PRE-CLOSED):
- `get_constant("phi_paasch")` → **1.53158** (NO PROVENANCE entry — flagged per plan; value confirmed, imported via `from canonical_constants import`, never hardcoded).
- `search_knowledge("S0 charged-lepton shape selector phi_paasch fN golden ratio envelope exponent")` → confirms both S₀ candidates are real framework outputs: `S101-NU-DIRAC-ENVELOPE-MAP` carries `b=S0=1.694153@(sqrtC2,0+) shapeDev=+6.880%_KILL`; `S101-W3-S0-KNOB` carries `knob=iii … S0*T_ac=τ_fold, dev_iii=0.0013` (the 95/56 graded leg). **No gate has computed the S₀=φ_paasch^fN identity** — `PHI-GOLDEN-22` / `P-30golden` concern a DIFFERENT question (whether the (2,2)/(0,0) ratio reaches the golden ratio 1.618, which P-30golden FAILed at φ_30,max=1.550). NOT PRE-CLOSED — distinct observable.
- `trace_entity("S0 charged-lepton envelope selector")` → no trace node (the S₀ values live in the S101 verdict files surfaced above, not as a named entity).

**Verdict**: **INFO** (numerical-proximity-not-identity). Three-zone: δ_min = δ_a = **4.188743e-04** ∈ [1e-12, 1e-3] dead-band → INFO; the headline "S₀ = φ_paasch^fN identity" reading is killed cleanly (NOT a machine-ε algebraic identity). `[CHAIN]` trigger, no schema-v2 3-tuple.

**Results**:

4-tuple: `(value=δ_min=4.188743e-04, scheme=SAGE-QQ-HIGHPREC-S0-PHI-FN-IDENTITY, convention=ABSOLUTE, L_max=N/A)`.

| Quantity | Value (mpmath, 50 dps) | Zone |
|:---------|:-----------------------|:-----|
| φ_paasch (canonical) | 1.53158 | — |
| fN = √5 − 1 | 1.2360679775 | — |
| φ_paasch^fN | 1.6937341257 | — |
| S₀_100a = 1.694153 (S101-NU-DIRAC-ENVELOPE-MAP b=S0) | δ_a = **4.188743e-04** | dead-band [1e-12, 1e-3] → INFO |
| S₀_101_graded = 95/56 = 1.6964285714 (S101-W3-S0-KNOB knob=iii) | δ_b = **2.694446e-03** | > 1e-3 → FAIL-zone |
| inverse exponent ln(S₀_100a)/ln(φ) | 1.2366480330 | vs fN=1.2360679775 (matches ~5e-4) |
| inverse exponent ln(95/56)/ln(φ) | 1.2397967319 | vs fN (matches ~4e-3) |

Substitution chain (substituted numbers): φ_paasch^fN = 1.531580^1.23606798 = 1.6937341257. δ_a = |1.694153 − 1.6937341| = 4.188743e-04; δ_b = |1.6964286 − 1.6937341| = 2.694446e-03; δ_min = δ_a = 4.188743e-04. PASS bar = 1e-12 (machine-ε algebraic identity) — δ_min exceeds it by ~8 OOM. FAIL bar = 1e-3 — δ_a < 1e-3 (dead band) while δ_b > 1e-3. ⇒ closest candidate (S₀_100a) lands INFO; the 95/56 candidate is FAIL-zone. **Precision-floor caveat (load-bearing):** φ_paasch is published to ~7 sig figs, so an algebraic identity is testable to ~1e-6 at best; δ_min=4.19e-4 is ~2 OOM above even that floor — the identity is decisively false, robustly, independent of φ_paasch's precision. Reproduces the plan-freeze Sage pre-flight (δ_a=4.18782e-4) to the φ_paasch rounding.

Substrate-physics assessment (PARTICLE on a GEOMETRIC substrate): φ_paasch is the bare (3,0)/(0,0) D_K eigenvalue ratio at s=0.15 (GEOMETRIC); S₀ is the charged-lepton SHAPE selector fixing the exp(−S₀·C₂) Higgs-overlap envelope (PARTICLE / Yukawa-texture). Direction: D_K eigenvalues → bare (3,0)/(0,0) ratio φ_paasch AND the Casimir-envelope exponent S₀ → charged-lepton mass shape. A machine-ε identity would mean the dressed-acoustic shape inherits the bare geometric ratio composed with Paasch's golden factor; the computation shows a 4-sig-fig PROXIMITY, not an identity. The headline UB4 bridge ("S₀ = φ_paasch^fN") is closed as a coincidence; the dressed lepton-shape selector is NOT governed by Paasch's two transcendentals — consistent with PHI-BDG-47 (φ_paasch is a bare-spectrum geometric fact, not a dressed-observable structural source).

**Output Artifacts** (verified by content presence on disk):
- script `computations/investigation-3/inv3_w3_s0_phi_fn_identity.py` — `from canonical_constants import` + `print_verdict_payload` (def + call) ✓
- data `computations/investigation-3/inv3_w3_s0_phi_fn_identity.npz` (keys: phi_paasch, fN, phi_fN, S0_100a, S0_101_graded, delta_a, delta_b, delta_min, inv_exponent_a/b, x_grid, curve_a, curve_b, verdict, closest) ✓
- plot `computations/investigation-3/inv3_w3_s0_phi_fn_identity.png` (|S₀ − φ^x| vs x near x=fN, both candidates, PASS/FAIL bars) ✓
- verdict line `INV3-W3-1: INFO -- … audit_sha256=d7994562d38d7a28d0692ed37d280f894035f22dffe6eb8ad79f162b27c1c985 content_sha256=1e8947ff…` in `computations/investigation-3/inv3_gate_verdicts.txt` + dual-SHA companion row + 3 extra rows (race-safe `emit_verdict`, track=investigation; sig_5 unique) ✓
- this WP section: Status COMPLETED, Verdict INFO, Output Artifacts, MCP Pre-Compute Audit ✓

---

### §W3-2. INV3-W3-2-W3-MINIMAL-MODEL-KINK-PHI

**Status**: COMPLETED
**Gate ID**: `INV3-W3-2-W3-MINIMAL-MODEL-KINK-PHI` (verdict emitted under short form `INV3-W3-2`)
**gate_type**: `compute`
**Trigger**: `[CHAIN]`
**Classification**: **PARTICLE** on a **GEOMETRIC** substrate (kink/soliton mass ratios of the Z3-Potts / W3 CFT -- the wall-intersection reading of phi_paasch; the W3 CFT IS the effective description of the substrate's Z3 wall criticality)
**Agent**: `paasch-mass-quantization-analyst`
**Hypothesis**: A kink (soliton) MASS ratio of the W3 minimal model M(6,5) (c=4/5, the Z3-Potts critical point), as given by the Reshetikhin-Smirnov / Bethe-ansatz S-matrix, equals phi_paasch=1.531580 or fN=sqrt(5)-1=1.236068 within 2% -- establishing phi_paasch as a universality-class number forced by the c=4/5 CFT rather than a D_K eigenvalue coincidence.
**Plan reference**: `sessions/investigation/investigation-3/investigation-3-plan-w3.md` SS W3-2.

**Verdict**: **FAIL** -- the target M(6,5) (c=4/5) integrable kink-MASS spectrum is a **degenerate doublet (single mass)**, so its only universality-class mass ratio is **1.000**; this is 34.7% from phi_paasch and 19.1% from fN. No M(6,5) kink mass ratio lands within 2% (or even 5%) of either target. phi_paasch is **NOT** a universality-class **mass** number forced by the c=4/5 CFT. A clean negative; the bare-(3,0)/(0,0)-spectrum-only reading of phi_paasch (consistent with the PHI-BDG-47 FAIL) survives, and the A3 six-sequence <-> Z3-wall map loses its hoped-for universality-class anchor.

**MCP Pre-Compute Audit** (queries run BEFORE computing; per `.claude/rules/knowledge-index-usage.md`):
- `get_constant('phi_paasch')` -> **1.53158** (canonical; line 289 of `canonical_constants.py`, "PROVEN (S12, machine epsilon). Paasch spectral ratio at s=0.15"). Used as comparison target (full-precision pin 1.531580).
- `get_constant('fN')` -> **not found** as a canonical entry -> derived Sage-exact in-script as sqrt(5)-1 = 1.2360679... (= 2/phi_golden; Paasch M-value successive ratio).
- `search_knowledge('phi_paasch golden ratio Z3 Potts W3 minimal model kink soliton universality class')` -> surfaced **prior art**: `s33a_w3_kink_masses.py` (S33a) already surveyed A_n/D4/E6/E7/E8 affine Toda + W3 M(6,5) Kac dims + Z3-Potts trig scans vs phi_paasch **only** (2%/5%, no fN target). Also `framework-paasch-potential.md` (wall-intersection treatment, fN=2 phi_golden) and `PHI-GOLDEN-22` (S47 open-channel: tau-sweep of (2,2)/(0,0) toward golden; distinct gate).
- `trace_entity('PHI-BDG-47')` -> empty (no indexed entity); the bare-spectrum-destruction result is carried in agent memory (D_K bare phi_paasch property destroyed by BCS dressing -> PHI-BDG-47 FAIL). This gate tests the **complementary** collective-excitation reading.
- `search_knowledge('Coldea E8 Ising golden ratio criticality Paasch wall Z3')` -> `f_N = 2 phi_golden = 1.236068` in `framework-paasch-potential.md`; Coldea/E8 golden-ratio-in-criticality is the adjacent precedent (Paasch Paper 11).
- `trace_entity('W3 minimal model kink masses Reshetikhin Smirnov')` -> no trace (no prior Reshetikhin-Smirnov kink-mass landing). NOT pre-closed -> compute proceeds. External literature is a **methodological** cross-check supplying the known CFT spectrum, not a canonical replacement for the substrate result.

**Literature retrieved** (paper-search + WebSearch THIS dispatch -- NOT training knowledge; per `feedback_research-corpus.md`):
- **[P1] L. Lepori, G. Z. Toth, G. Delfino, "Particle spectrum of the 3-state Potts field theory: a numerical study," arXiv:0909.2192v2 (SISSA 55/2009/EP).** DECISIVE for the target. Their Sec. 2: the S3-invariant 3-state Potts critical point is the **D4 (c=4/5) minimal model = M(6,5)**. Their Sec. 3.1: the massive integrable (h=0 thermal) deformation has a spectrum of kinks K_{ab} (a != b) **all of equal mass m** (citing Chim-Zamolodchikov, Int.J.Mod.Phys.A7(1992)5317 and Koberle-Swieca, Phys.Lett.B86(1979)209); Eq. (7): m = b * tau^{5/6}, b=4.504. The integrable spectrum is a **degenerate doublet -> only mass ratio = 1.000**. Nontrivial meson/baryon ratios arise **only for h != 0** and are **continuous** functions of eta_pm (their Fig. 5) -- tunable, **non-universal**.
- **[P2] G. Mussardo, M. Panero, A. Stampiggi, "Form Factors of the Tricritical Three-state Potts Model in its Scaling Limit," arXiv:2311.00654v2.** ADJACENT universality class: the **tricritical** 3-state Potts = M(6,7) (c=6/7), the **E6** theory. Their Eq. (14): m_l (lightest), m_L = 2cos(pi/4) m_l = sqrt(2) m_l ~ 1.41421, m_h = 2cos(pi/12) m_l ~ 1.93185, plus a heavier self-conjugate [2cos(pi/4)]^2 m_l = 2 m_l. **None** of these E6 universality-class numbers is phi_paasch or fN (closest is sqrt(2)=1.4142, 7.7% from phi_paasch).
- **[P3] Coldea et al., Science 327 (2010) 177** -- the **E8** Ising (c=1/2, M(4,3)) chain: golden ratio m2/m1 = 2cos(pi/5) = 1.618034 (the precedent Paasch Paper 11 cites). A **different** universality class (c=1/2), and golden != phi_paasch.

**Results**:
- **4-tuple**: `(value=FAIL, scheme=W3-MINIMAL-MODEL-KINK-PHI, convention=RATIO, L_max=N/A)`.
- **Target M(6,5) c=4/5 KINK-MASS spectrum** (PASS-eligible class): **1 ratio** = **1.000** (degenerate kink doublet). Matches within 2% of phi_paasch: **0**; within 2% of fN: **0**. Closest target kink-mass ratio -> phi_paasch: 1.000 (dev **34.71%**); -> fN: 1.000 (dev **19.10%**).
- **Look-elsewhere denominator (honest counts)**: TOTAL ratios scanned across all surveyed models = **1307**; genuine MASS ratios (target + adjacent E6/E8/A2/D4) = **17**; target KINK-MASS ratios = **1**; target DIMENSION-ratio diagnostics = **87**. Of the 1307 total, **236 fall within 5%** of phi_paasch or fN -- the algebraic-number family {sin(k pi/h), 2cos(k pi/n)} is **dense** near these values, so a bare 2% match anywhere is weak evidence by construction.
- **DIAGNOSTIC (reported, NOT PASS-eligible)**: the M(6,5) Kac **scaling-DIMENSION** ratio Delta_{(4,5)}/Delta_{(3,1)} = 0.825/0.6667 = **1.2375** is **0.116%** from fN. This is a conformal-WEIGHT ratio, **not a mass ratio**: the plan operator and hypothesis are mass-ratio claims, so a dimension ratio near fN does **not** satisfy the gate and does **not** make fN a universality-class mass number. (Flagging this explicitly is the look-elsewhere honesty the plan demands -- among ~1300 algebraic numbers, near-coincidences with fN at the 0.1% level are expected; the closest systematic-scan hit sin(5pi/10)/sin(3pi/10) = 1.236068 lands on fN to **0.0000%**, purely from density.)
- **Adjacent E6 tricritical-Potts M(6,7)** mass ratios {sqrt(2) ~ 1.4142, 2cos(pi/12) ~ 1.9319}: genuine universality-class numbers, **neither** phi_paasch nor fN. **E8 Ising (Coldea)** golden = 1.618034: different class (c=1/2). So even the neighbouring integrable-Potts class does not produce phi_paasch.

**Substitution chain** (plan SS W3-2; numerics now filled from retrieved spectrum):
1. phi_paasch = 1.531580 [`canonical_constants.py:289`].
2. fN = sqrt(5) - 1 = 1.2360680 [Sage-exact; Paasch M-ratio].
3. M(6,5) is the W3/D4 minimal model, c = 4/5 (three-state Potts critical point). Its integrable (h=0 thermal) perturbation has the kink spectrum {m_{ab}}; by Chim-Zamolodchikov / Koberle-Swieca [P1 Sec 3.1] **all kinks are degenerate**: a single mass m, so the spectrum yields the single mass ratio m/m = 1.000.
4. For r = 1.000: rel_phi = |1.000 - 1.531580|/1.531580 = 0.34708; rel_fN = |1.000 - 1.236068|/1.236068 = 0.19098.
5. PASS iff min over the spectrum of min(rel_phi, rel_fN) <= 0.02. min = 0.19098 > 0.02 => **FAIL**.
- **Direction/conclusion**: the c=4/5 universality class forces a degenerate kink doublet, NOT a phi_paasch/fN mass ratio. phi_paasch is not a Z3-Potts collective-excitation mass number. (Had the target been the tricritical M(6,7), the E6 spectrum {sqrt(2), 2cos(pi/12)} would still miss both targets -- so the negative is robust to the adjacent-class reading too.)

**Substrate-physics assessment** (direction D_K -> spectral/Casimir moments -> mass observable):
- The framework's domain walls carry a Z3 cubic Ginzburg-Landau term (S33 SS 1.2); the Z3-Potts critical point IS the W3 minimal model M(6,5), c=4/5, and the kink masses ARE the collective-excitation spectrum of the substrate's wall sector. The W3 CFT is the effective description of the substrate's Z3 wall criticality -- external literature (Reshetikhin-Smirnov / Lepori-Toth-Delfino) is a methodological cross-check supplying the known spectrum, never a canonical replacement for a substrate computation.
- The decisive substrate fact is that this wall-excitation spectrum is **single-mass at criticality** -- so the wall-intersection reading **cannot** be the origin of phi_paasch. phi_paasch therefore remains a **bare-(3,0)/(0,0)-eigenvalue-ratio** GEOMETRIC fact only (consistent with the bare-spectrum-only reading that the BdG-dressing PHI-BDG-47 FAIL leaves standing), with no universality-class promotion available from the c=4/5 kink sector.
- **Bridge-map consequence (A3)**: the six-sequence <-> Z3-wall map loses its candidate universality-class anchor. The corridor "phi_paasch is forced by the c=4/5 CFT" is **closed**; any residual case for phi_paasch as a physical (rather than purely geometric) number must come from a different observable (the bare D_K ratio, or a non-CFT wall structure), not the integrable kink spectrum.

**Output Artifacts** (closure-verification; mirrors gate-block `output_artifacts:`):
- **script** `computations/investigation-3/inv3_w3_w3_minimal_model_kink_phi.py` -- present; contains `from canonical_constants import` and `print_verdict_payload` (both must_contain patterns verified by grep).
- **data** `computations/investigation-3/inv3_w3_w3_minimal_model_kink_phi.npz` -- present (full ratio tables, counts, best-matches per role, lit refs).
- **plot** `computations/investigation-3/inv3_w3_w3_minimal_model_kink_phi.png` -- present (ratio scatter by role vs phi_paasch / fN 2% bands; target kink-mass single point at 1.000).
- **verdict_line** in `computations/investigation-3/inv3_gate_verdicts.txt` -- `INV3-W3-2: FAIL ...` matching `^INV3-W3-2:.* audit_sha256=[a-f0-9]{64}`; dual-SHA companion row present (schema-v2 3-tuple NOT required -- `[CHAIN]`, no `[SIGN]`).
  - `audit_sha256=e99cf44ae8042c2dee6e219fa80fbdcff1a86b4907269e285cffad5e02cfdc6c`
  - `content_sha256=b6bf1f58ff4327e7b2d8d10b3d1eeb9f736071274f5fa5a8bae6f95ba0f6e8ce`
- **regulator_pin**: N/A -- CFT kink mass ratios are sin(k pi/h)-type algebraic numbers from the Bethe-ansatz S-matrix, not Seeley-DeWitt a_n moments.

---

### §W3-3. INV3-W3-3-ALPHA-DIM-N3-TWO-ALPHA

**Status**: COMPLETED
**Gate ID**: `INV3-W3-3-ALPHA-DIM-N3-TWO-ALPHA` (verdict-line short form `INV3-W3-3`)
**gate_type**: `compute`
**Trigger**: `[CHAIN]`
**Classification**: **PARTICLE** (fine-structure constant + SU(3) representation dimension n3=dim(3,0)) on a **GEOMETRIC** substrate (the D_K SU(3) representation content).
**Agent**: `paasch-mass-quantization-analyst`
**Hypothesis**: (i) Paasch's α=(1/n3²)(f/2)^{1/4} (f=Ω, root of ln f=−f) and his proton-mass cubic reconstruct sub-ppm with n3 substituted by dim(3,0)=10 at every step (promoting the n3=10 coincidence to a derived SU(3) identity); and (ii) the framework's UV unified coupling α_GUT=1/10.8 runs down through KK thresholds to the IR electromagnetic α=1/137, with the n3=10 / ln(x)=−x structure governing the running.
**Plan reference**: `sessions/investigation/investigation-3/investigation-3-plan-w3.md` §W3-3.

**Verdict**: **INFO** (composite over two sub-tests; schema-v2 3-tuple sign=**PASS** / magnitude=**FAIL** / regime=**VALID** for sub-test (ii)).
- **Sub-test (i) PASS** — α(n3=dim(3,0)=10) = 0.007297358806, **0.855 ppm** vs CODATA (boundary ≤ 1 ppm). The SU(3)-dimension substitution reconstructs the fine-structure constant to sub-ppm at chain level; n3=10 is **uniquely** load-bearing.
- **Sub-test (ii) sign-PASS / magnitude-FAIL** — 1/α runs UP (UV→IR; charge screening) for every anchor (SIGN PASS), but the pinned survey anchor 1/α_GUT=1/10.8 does **not** run to 1/137 within the 10% band: it lands 1/α_IR≈34.5 (74.8% off). The closest reading (Model-C 1/39.47 / s42-snapshot 1/40) lands ≈111–112 (18–19% off), still ~2× the band. Per plan §W3-3 INFO_meaning the composite is **INFO**: (i) PASS + (ii) directionally-supported but quantitatively-open. (Composite-precedence disclosure: the gate is a two-sub-test composite; the plan-frozen INFO_meaning overrides the generic 3-tuple collapse, declared in the verdict-file extra-rows per `gate-verdicts.md §"Plan-frozen gate-block operator precedence"`.)

This is the EXPECTED outcome per the plan pre-flight. Sub-test (i) **promotes A1 (n3=dim(3,0)) to a chain-level SU(3) identity** (the sole-surviving Paasch–NCG bridge strengthens). Sub-test (ii) keeps the framework's two α-objects **disjoint** — a latent, not contradicted, tension (C3 directionally-supported but unclosed).

**Output Artifacts** (closure-verification checklist):
- script `computations/investigation-3/inv3_w3_alpha_dim_n3_two_alpha.py` — present; `from canonical_constants import *` ✓, `print_verdict_payload` ✓.
- data `computations/investigation-3/inv3_w3_alpha_dim_n3_two_alpha.npz` — present.
- plot `computations/investigation-3/inv3_w3_alpha_dim_n3_two_alpha.png` — present (3 panels: (i) n3-sensitivity bar, (ii) SM 1-loop EM running, (ii) two-α residual-vs-137 bar).
- verdict_line `computations/investigation-3/inv3_gate_verdicts.txt` — `INV3-W3-3: INFO -- … audit_sha256=2ee49a82b33e065187d6f44d00178b856dc0f563bd446ea26690ed69cbb7ef4a content_sha256=2afe319c3e041dc605c3a73f34534618b3035e02570dbcf75dcb6f59615d2216 schema_version=S84+` + dual-SHA companion row + schema-v2 3-tuple row + 6 extra companion rows (composite-precedence, sub-test(i), sub-test(ii), flagged α_GUT discrepancy, dual_prior).

**MCP Pre-Compute Audit** (queries executed BEFORE computing, per `knowledge-index-usage.md`):
- `search_knowledge("Paasch alpha fine structure constant formula n3 dim(3,0)")` → α=(1/n3²)(f/2)^{1/4}=0.007297359 (Paper 04 Eq 2.9); `dim(3,0)=binom(5,2)=10`; `n3=dim(3,0)=#sectors(p+q≤3)=T_4=10` (session-56-paasch-collab). The `alpha-dim (n3=10)` bridge is STRUCTURAL since S48 — this gate EXTENDS it to chain level (incl. proton-cubic) + the two-α reconciliation (new content).
- `search_knowledge("alpha_GUT unified coupling 1/10.8 spectral action f0")` → s42-snapshot has `alpha_GUT = 1/40 [approximate GUT unified coupling, Step 2b only]`; no canonical `alpha_GUT` constant.
- `search_knowledge("KK threshold M_U unification scale Model-C 7.68e14 GeV running coupling")` → `M_U=7.68e14 GeV` (S101 W3-7 RGE-solved Model-C); `alpha_U^{-1}=39.47`; open-channel **Q18a (α_GUT 1/10.8 vs 1/25)** — Model-C survives proton decay.
- `get_constant("alpha_GUT")` → NOT FOUND (no canonical pin); `get_constant("M_KK")` → 7.4287e16 GeV; `get_constant("phi_paasch")` → 1.53158; `get_constant("alpha_em_MZ_inv")` → 127.955 (PDG 2024); `get_constant("M_U")` → not found (lives in session-102 plan text).
- `trace_entity("Q18a alpha_GUT 1/10.8")` → no trace (open-channel only).
- **Anchor decision** (per plan): α_GUT=**1/10.8 PINNED** as survey/Q18a anchor; **1/40 s42-snapshot flagged** as Step-2b approximation; **Model-C 1/39.47** (RGE-solved) carried as the third reading. NOT PRE-CLOSED — the chain-level proton-cubic substitution + two-α RG running are new.

**Results**:

4-tuple: `(value='i_alpha=0.007297359_ppm=0.855_PASS;ii_sign=PASS_mag=FAIL_regime=VALID_survey1over10.8_to_IR=34.5_resid=75pct_bestModelC_resid=18pct;composite=INFO', scheme=ALPHA-DIM-N3-TWO-ALPHA, convention=RATIO, L_max=N/A)`.

**Sub-test (i) — chain-level α-dim (Sage-verified closed forms):**

Substitution chain (i):
- Step 1: f = Ω = W(1) = 0.567143290409783840, root of ln f = −f (residual ln f + f = −1.1e-16; Sage-exact 0.567143290409783873).
- Step 2: n3 = dim(3,0) = (3+1)(0+1)(3+0+2)/2 = binom(5,2) = **10** = #sectors(p+q≤3) = T_4. [C2(3,0)=6 in Gell-Mann norm; the (3,0) sector is the phi_paasch sector — its τ=0 round-metric |λ| ratio is sqrt(7/3)=1.527525.]
- Step 3–4: α = (1/n3²)(f/2)^{1/4} = (1/100)(0.5671433/2)^{1/4} = **0.007297358806**.
- Step 5: α_CODATA = 0.0072973525643 → **rel_dev = 8.553e-7 = 0.855 ppm** ≤ 1 ppm → **PASS** (vs Paasch-cited measured 0.007297353: 0.796 ppm).

n3-sensitivity scan (only n3=10 lands sub-ppm — confirms 10 is uniquely load-bearing):

| n3 | α | rel_dev | SU(3) dim? |
|----|-----|---------|------------|
| 8  | 0.011402123 | 56.25% | yes (=dim(1,1)) |
| 9  | 0.009009085 | 23.46% | no |
| **10** | **0.007297359** | **0.0001% (0.855 ppm)** | **yes (=dim(3,0)=dim(0,3))** |
| 11 | 0.006030875 | 17.36% | no |
| 12 | 0.005067610 | 30.56% | no |

Proton-cubic (Paper 03 Ch.6 Eq 6.3/6.4): βu² = 101.02 with best-fit integer u = n3 = dim(3,0) = **10** → β = 1.0102. The proton mass depends on two integers N(b)=112 and n3=10 (Paper 03 lines 430–431); the **u² = n3² = 100** in the proton cubic is the **SAME** 100 that appears in α=(1/n3²)…. The SU(3) (3,0) dimension is therefore the shared load-bearing integer across BOTH Paasch's α formula AND his proton-mass cubic — the chain-level substitution holds at every appearance.

**Sub-test (ii) — two-α reconciliation (one-loop SM RG, Sage cross-checked):**

Substitution chain (ii), running DIRECTION:
- Defs: 1/α_GUT(survey Q18a)=10.8 [PINNED]; 1/α_U(Model-C)=39.47; 1/α_GUT(s42-snap)=40 [flagged]; 1/α_em(M_Z)=127.955 [PDG]; 1/α_Thomson=137.035999 [CODATA]; M_U=7.68e14 GeV.
- One-loop: 1/α_i(μ)=1/α_i(μ₀)−(b_i/2π)ln(μ/μ₀); b₂=−19/6, b_Y=(3/5)(41/10). Decompose 1/α_em(M_Z)=1/α₂+1/α_Y via sin²θ_W=0.23122.
- Direction: U(1)_em is screened ⇒ 1/α LARGER in IR than UV ⇒ runs **UP** UV→IR. ✓ (SIGN PASS for all anchors; Δ>0).

RG-flow endpoints:
- SM 1-loop run M_Z→M_U: 1/α_em(M_Z)=127.955 → **1/α_em(M_U)=131.302**. The EM coupling is **near-flat** over ~13 decades (the SM excursion M_Z→Thomson is only +9.08 = 7.1%; M_U→Thomson screening is +5.73).
- **137.036 IS the SM-running IR endpoint of the measured 1/α_em(M_Z)=127.955** — NOT what 1/α_GUT=10.8 runs to.

Two-α magnitude test (EM embedding at sin²θ_W=3/8 GUT boundary, factor 8/3, then run to Thomson):

| UV anchor | 1/α_em(M_U) embed | → 1/α_IR | resid vs 137.036 | PASS(≤10%)? |
|-----------|-------------------|----------|------------------|-------------|
| survey 1/10.8 (**PINNED**) | 28.8 | 34.5 | **74.8%** | no |
| Model-C 1/39.47 | 105.3 | 111.0 | 19.0% | no |
| s42-snap 1/40 | 106.7 | 112.4 | 18.0% | no |

None lands 137 within 10%. The unified spectral-action coupling 1/10.8 and the IR 1/137 are **not** connected by simple KK+SM EM running within the band; the closest reading (Model-C) is still ~2× outside.

3-tuple (sub-test ii): **sign=PASS** (1/α runs UP UV→IR), **magnitude=FAIL** (pinned survey 74.8% off; best 18%), **regime=VALID** (one-loop perturbative throughout; min 1/α on flow = 128 ≫ 1).

dual_prior posterior: Track A (structural: n3=dim(3,0) is THE SU(3) origin) **0.6 → 0.85**; Track B (numerical-only) **0.4 → 0.15** — discriminator: sub-test (i) PASS at chain level with α AND the proton-cubic both reconstructing with dim(3,0).

**FLAGGED α_GUT discrepancy** (per plan): survey/Q18a **1/10.8** (PINNED anchor) vs s42-snapshot **1/40** (Step-2b approximation, `s42_constants_snapshot_verdict.txt`) vs Model-C **1/39.47** (S101 W3-7 RGE-solved). The 1/10.8 and 1/40 differ by ~3.7×; the two-α reconciliation is sensitive to which is the genuine UV unified coupling.

**Substrate-physics assessment**: PARTICLE on a GEOMETRIC substrate. The arrow is D_K SU(3) representation content → dim(3,0)=10 → Paasch's α formula → the IR electromagnetic constant. Sub-test (i) is a clean substrate-first win: the same (3,0) irrep dimension that (via the round-metric ratio sqrt(7/3)) underlies phi_paasch reconstructs the fine-structure constant to 0.855 ppm AND appears identically in the proton-mass cubic — n3 is a derived SU(3) dimension, not a fitted integer (A1 promoted to chain-level identity; the transcendental ln(x)=−x governing Ω is the n=0 version of Paasch's mass-quantization ln(x)=−x², same confined-relativistic-constituent geometry the logarithmic potential expresses). Sub-test (ii) shows the framework's UV unified coupling (the a₄ Yang-Mills spectral moment of D_K) and the IR Thomson α are NOT the same flow's endpoints within 10%: the running IS the scale-dependence of the a₄ moment as KK modes decouple, and that running barely moves the EM coupling (7.1% over 13 decades), so the IR 1/137 is the endpoint of 1/α_em(M_Z), not of 1/10.8. The two α-objects remain disjoint (latent tension, C3 unclosed). Paasch's external-paper closed forms (α formula Eq 2.8/2.9, proton cubic Eq 6.3/6.4) are methodological sources; the sub-ppm verification and the SU(3)-dimension substitution are the substrate-first content.

---

### §W3-4. INV3-W3-4-CASIMIR-GRADED-NJ-7N

**Status**: COMPLETED
**Gate ID**: `INV3-W3-4-CASIMIR-GRADED-NJ-7N` (emitted short-form `INV3-W3-4`)
**gate_type**: `compute`
**Trigger**: `[CHAIN]`
**Classification**: **PARTICLE** (Paasch's mass-number integers N(j) as a representation-theoretic mode count of D_K) on a **GEOMETRIC** substrate (the SU(3) Casimir ladder / Peter-Weyl mode geometry)
**Agent**: `paasch-mass-quantization-analyst`
**Hypothesis**: Paasch's mass-number integers N(j)=(m_j/m_e)^{2/3}={7, 35, 42, 98, 150} (electron, muon, pion, kaon, proton) emerge as multiples of 7 from an SU(3) Casimir / dimension mode-counting function N(p,q) built from {dim(p,q), C₂(p,q), p+q} evaluated on the L_max=12 fold spectrum at τ_fold=0.19 — giving Paasch's INTEGER scheme (the half the framework realizes, per G2) a substrate origin and tying his absolute-m_p prefactor to the framework's M_KK scale (G1).
**Plan reference**: `sessions/investigation/investigation-3/investigation-3-plan-w3.md` §W3-4.

**Output Artifacts** (closure-verification checklist):
- **Script**: `computations/investigation-3/inv3_w3_casimir_graded_nj_7n.py` — present; `grep` confirms `from canonical_constants import` (Section 1) and `print_verdict_payload` (Section 8). Runs CPU-only (OMP cap 8); wall 0.3 s.
- **Data**: `computations/investigation-3/inv3_w3_casimir_graded_nj_7n.npz` — present; carries the full 90-sector table (`table_pq/dim/C2/C2int/level/lammin`), the candidate-function report, the M/N-ratio diagnostics, dual-SHA.
- **Plot**: `computations/investigation-3/inv3_w3_casimir_graded_nj_7n.png` — present; 4 panels (Casimir ladder + N(j) overlay; candidate-count bars; √N ratios vs fN; N-ratios vs φ_paasch).
- **Verdict line**: `computations/investigation-3/inv3_gate_verdicts.txt` — `INV3-W3-4: INFO ...` matching `^INV3-W3-4:.* audit_sha256=[a-f0-9]{64}`; dual-SHA companion row present (schema-v2 3-tuple NOT required, no `[SIGN]`).
- **Input prereq**: L12 fold cache `computations/session-84/s84_spectrum_cache_L12_tau019.npz` present (`sha256` head `9e6d9cf7fd6a6949`); 90 sectors; `dim(cache)` vs `dim(p,q)` formula = 0 mismatches (cache integrity confirmed).

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script):
- `search_knowledge("Paasch N(j) 7n mass-number integers Casimir grading")` → hit: **eq_8060 (session-22-paasch-collab)** `N(j)^2=(m_j/m_e)^{2/3} and λ²=C₂(p,q)+3/4` — a prior N(j)↔Casimir connection already on record; **eq_7977 (session-21c)** the same `λ²=C₂(p,q)+3/4` bridge (bi-invariant τ=0 form). NOT a closure — open bridge.
- `search_knowledge("W_Casimir block-trace widening 9/5 exponential mass function")` → hit: **eq `W_Casimir = 3/(5/3) = 9/5 = 1.800`** from `session-100a-plan-w2` (`g_lo ∝ C₂(1,1)−C₂(1,0)=5/3`, `g_hi ∝ C₂(3,0)−C₂(1,1)=3`); gate **`S101-W2-BLOCKTRACE-WIDENING` PASS** (`W_flat=1.800000` at the 9/5 lower edge). The framework's Casimir-graded exponential mass function is canonical.
- `get_constant("W_Casimir")` → **not found** as a standalone constant (lives as the S100a/S101 gate value 9/5, not a `canonical_constants.py` pin).
- `get_constant("phi_paasch")` → **1.53158** (no PROVENANCE entry; PROVEN S12 machine-ε per `canonical_constants.py:289` = 1.531580).
- `get_constant("M_KK")` → **7.428660036284456e16 GeV** (S42 `CONST-FREEZE-42`, alias of `M_KK_gravity`).
- `get_constant("tau_fold")` → **0.19** (S12/S42 `CONST-FREEZE-42`).
- `trace_entity("lambda^2 = C_2(p,q) + 3/4")` → the S21c/S22 bridge equation (2 hits); used as a diagnostic (it holds at τ=0, NOT at τ_fold=0.19 — see Results).
- `search_knowledge("Paasch which grading resolved 7n mode multiplicity wall modes")` → open_channel **[Paasch]Q-1 "Which grading?" Resolved (session 25)**; framework-paasch-potential note: Nambu (1952) `m_n=(n/2)(1/α)m_e`; Paasch `N(j)=7n` give `m*(j)=N(j)^{3/2} m_e`; the S33 reframe guessed `1+4+2=7` wall modes. NOT a closure of THIS gate (the Casimir-graded 7n test was not previously computed on the L12 cache).
- **PRE-CLOSED?** NO. The N(j)↔Casimir connection was noted qualitatively (S21c/S22) but the explicit Casimir-graded mode-count 7n test on the L12 fold cache had not been run.

**Verdict**: **INFO** — `value=best_candidate=D_single_dim_pq; 7n_match=2of5; struct_match=2of5; Nj_are_SU3_dims=2of5(35,42_yes;7,98,150_no); 150/98=1.530612_vs_phi_paasch_dev0.063pct; only_kaon-proton_M-ratio~fN`. Scheme `CASIMIR-GRADED-NJ-7N`, convention `ABSOLUTE`, L_max=12. `audit_sha256=0b5f371f5ae1ffabebae8d82ef2b9aa94c975db1b1c62f03c9f8bb8bd2dcd32b`, `content_sha256=153d20b2536f80db53a7dba5b3913444f3cc40d370b3cd3e3379647ef34e0902`.

This is **exactly the pre-registered expected outcome** (plan §W3-4: "INFO-partial; 35,42 ARE SU(3) dims; 7,98,150 are not"). 2-of-5 of Paasch's N(j) coincide with SU(3) irrep dimensions; this clears the INFO floor (≥2) but no single graded mode-count reproduces ≥4-of-5 as 7n, so the PASS boundary is not reached. Per the FAIL rubric (`<2-of-5`), FAIL is excluded.

**Results**:

**4-tuple**: `(value=2, scheme=CASIMIR-GRADED-NJ-7N, convention=ABSOLUTE, L_max=12)` — `value` = the 7n-match count of the best candidate.

**Substitution chain (executed numbers vs plan-freeze Sage pre-flight)** — all confirmed:
- Step 1: Paasch N(j) = {electron 7, muon 35, pion 42, kaon 98, proton 150}; N(j)/7 = {1, 5, 6, 14, 150/7=21.4286}. The proton (21.43) is itself NOT an integer multiple of 7 — Paasch's own scheme has N(p)=150, which is 7·21.43, so the "7n" labelling is approximate for the proton even in Paasch.
- Step 2: SU(3) dim(p,q)=(p+1)(q+1)(p+q+2)/2; C₂(p,q)=(p²+q²+pq+3p+3q)/3.
- Step 3 (partial-coincidence): **7 NOT a dim; 35 = dim(1,4)=dim(4,1) YES; 42 = dim(2,3)=dim(3,2) YES; 98 NOT a dim; 150 NOT a dim** → **2-of-5**. Exactly the pre-flight.
- Step 4 (M-ratios): M(j)=√N(j) = {2.6458, 5.9161, 6.4807, 9.8995, 12.2474}; successive ratios {2.2361, 1.0954, 1.5275, 1.2372}; fN=√5−1=1.2360680. **Only kaon→proton (1.2372, rel-dev 0.09%) matches fN within 2%**; the other three (0.81, 0.11, 0.24 rel-dev) do NOT. NOT a uniform geometric M-series — confirms √N is not a clean fN-graded ladder.
- Step 5: **N(p)/N(K) = 150/98 = 1.5306122 vs φ_paasch=1.531580 → rel-dev 0.063%**. The one striking near-coincidence (a ratio of two non-dim integers).

**Candidate mode-counting functions** (each: how many of {7,35,42,98,150} reproduced exactly as 7n / as raw integer, of 5):

| Candidate N(p,q) | exact 7n | which | raw | which | set size |
|:-----------------|:---------|:------|:----|:------|:---------|
| A — cumulative dim-weighted count below C₂ ceiling | 1 | {7} | 1 | {7} | 45 |
| B — cumulative sector count below C₂ ceiling | 1 | {42} | 1 | {42} | 45 |
| C — rank-graded p+q | 1 | {7} | 1 | {7} | 13 |
| **D — single dim(p,q)** | **2** | **{35,42}** | **2** | **{35,42}** | 46 |
| E — Casimir-level integer 3·C₂ | 0 | — | 0 | — | 45 |
| F — band-level index | 1 | {7} | 1 | {7} | 13 |

**Best candidate = D (single dim), 2-of-5 as 7n {35,42}.** Critically, **no single function reproduces ≥4-of-5**, and the functions that hit 7 (A, C, F) are DIFFERENT from the one that hits 35,42 (D). The 7n pattern does NOT emerge from one SU(3) grading; different N(j) trace to different (and mutually inconsistent) counting mechanisms.

**Arithmetic structure of the integers (decomposition diagnostic, Sage-grade exact)**:
- **7 = 1 ⊕ 3 ⊕ 3̄** = dim(0,0)+dim(1,0)+dim(0,1) — singlet + fundamental + antifundamental, i.e. the **cumulative count of the three lowest Peter-Weyl sectors**. This is the "**7 is a mode-MULTIPLICITY unit, not an irrep dimension**" reading the plan pre-registered (and the S33 `1+4+2=7` wall-mode guess). 7 is reproducible as a low-lying count (candidates A/C/F), just not by the dim-map that gives 35,42.
- **35 = 8 ⊕ 27** = dim(1,1)+dim(2,2) (adjoint+27), AND = dim(1,4) directly. **42 = 1 ⊕ 6 ⊕ 35** = dim(0,0)+dim(0,2)+dim(1,4), AND = dim(2,3) directly. Both have clean SU(3) homes.
- **98 = 2·7² and 150 = 6·25 are NOT dims, NOT 3·C₂, NOT triangular numbers.** Kaon and proton resist any single-SU(3)-structure interpretation. This is the honest negative: the two heaviest particles' N(j) have no clean Casimir/dimension origin.

**S21c/S22 bridge λ²=C₂(p,q)+3/4 diagnostic**: max|resid| = 47.2, mean|resid| = 23.0 at τ_fold=0.19. The bridge holds at the **τ=0 bi-invariant** metric (where λ²=n/36 maps to the Casimir tower); at τ_fold the **Jensen deformation has moved the spectrum off the bi-invariant form** (|λ|_min for (0,0) is 0.82, not 0; for (3,0) is 1.25, not √6.75=2.60). The N(j)=7n verdict does NOT depend on this bridge — it is decided on the EXACT dims/Casimirs (representation-theoretic, regulator/τ-independent), so the absolute eigenvalue values are immaterial. **Content lives in the rep content, not the eigenvalue magnitudes** (substrate-first: D_K rep content → Casimir ladder → integers).

**Full 90-sector table** (p, q, dim(p,q), C₂(p,q), band-level, |λ|_min at τ_fold=0.19), ordered by Casimir; the four N(j)-relevant rows bolded:

| (p,q) | dim | C₂ | level | \|λ\|_min |
|:------|:----|:---|:------|:---------|
| (0,0) | 1 | 0.0000 | 0 | 0.8197 |
| (0,1) | 3 | 1.3333 | 1 | 0.8359 |
| (1,0) | 3 | 1.3333 | 1 | 0.8359 |
| (1,1) | 8 | 3.0000 | 2 | 0.8730 |
| (0,2) | 6 | 3.3333 | 2 | 0.9722 |
| (2,0) | 6 | 3.3333 | 2 | 0.9722 |
| (1,2) | 15 | 5.3333 | 3 | 1.1238 |
| (2,1) | 15 | 5.3333 | 3 | 1.1238 |
| (0,3) | 10 | 6.0000 | 3 | 1.2483 |
| (3,0) | 10 | 6.0000 | 3 | 1.2483 |
| (2,2) | 27 | 8.0000 | 4 | 1.3770 |
| (1,3) | 24 | 8.3333 | 4 | 1.3821 |
| (3,1) | 24 | 8.3333 | 4 | 1.3821 |
| (0,4) | 15 | 9.3333 | 4 | 1.5242 |
| (4,0) | 15 | 9.3333 | 4 | 1.5242 |
| **(2,3)** | **42** | **11.3333** | **5** | **1.6352** |
| **(3,2)** | **42** | **11.3333** | **5** | **1.6352** |
| **(1,4)** | **35** | **12.0000** | **5** | **1.6454** |
| **(4,1)** | **35** | **12.0000** | **5** | **1.6454** |
| (0,5) | 21 | 13.3333 | 5 | 1.7875 |
| (5,0) | 21 | 13.3333 | 5 | 1.7875 |
| (3,3) | 64 | 15.0000 | 6 | 1.8925 |
| (2,4) | 60 | 15.3333 | 6 | 1.8972 |
| (4,2) | 60 | 15.3333 | 6 | 1.8972 |
| (1,5) | 48 | 16.3333 | 6 | 1.9118 |
| (5,1) | 48 | 16.3333 | 6 | 1.9118 |
| (0,6) | 28 | 18.0000 | 6 | 2.0526 |
| (6,0) | 28 | 18.0000 | 6 | 2.0526 |
| (3,4) | 90 | 19.3333 | 7 | 2.1530 |
| (4,3) | 90 | 19.3333 | 7 | 2.1530 |
| (2,5) | 81 | 20.0000 | 7 | 2.1594 |
| (5,2) | 81 | 20.0000 | 7 | 2.1594 |
| (1,6) | 63 | 21.3333 | 7 | 2.1804 |
| (6,1) | 63 | 21.3333 | 7 | 2.1804 |
| (0,7) | 36 | 23.3333 | 7 | 2.3204 |
| (7,0) | 36 | 23.3333 | 7 | 2.3204 |
| (3,5) | 120 | 24.3333 | 8 | 2.4162 |
| (5,3) | 120 | 24.3333 | 8 | 2.4162 |
| (2,6) | 105 | 25.3333 | 8 | 2.4164 |
| (6,2) | 105 | 25.3333 | 8 | 2.4164 |
| (1,7) | 80 | 27.0000 | 8 | 2.4505 |
| (7,1) | 80 | 27.0000 | 8 | 2.4505 |
| (0,8) | 45 | 29.3333 | 8 | 2.5900 |
| (4,5) | 165 | 29.3333 | 9 | 2.6735 |
| (5,4) | 165 | 29.3333 | 9 | 2.6735 |
| (8,0) | 45 | 29.3333 | 8 | 2.5900 |
| (3,6) | 154 | 30.0000 | 9 | 2.6791 |
| (6,3) | 154 | 30.0000 | 9 | 2.6791 |
| (2,7) | 132 | 31.3333 | 9 | 2.6771 |
| (7,2) | 132 | 31.3333 | 9 | 2.6771 |
| (1,8) | 99 | 33.3333 | 9 | 2.7216 |
| (8,1) | 99 | 33.3333 | 9 | 2.7216 |
| (5,5) | 216 | 35.0000 | 10 | 2.9335 |
| (4,6) | 210 | 35.3333 | 10 | 2.9372 |
| (6,4) | 210 | 35.3333 | 10 | 2.9372 |
| (0,9) | 55 | 36.0000 | 9 | 2.8608 |
| (9,0) | 55 | 36.0000 | 9 | 2.8608 |
| (3,7) | 192 | 36.3333 | 10 | 2.9344 |
| (7,3) | 192 | 36.3333 | 10 | 2.9344 |
| (2,8) | 162 | 38.0000 | 10 | 2.9403 |
| (8,2) | 162 | 38.0000 | 10 | 2.9403 |
| (1,9) | 120 | 40.3333 | 10 | 2.9935 |
| (9,1) | 120 | 40.3333 | 10 | 2.9935 |
| (5,6) | 273 | 41.3333 | 11 | 3.1955 |
| (6,5) | 273 | 41.3333 | 11 | 3.1955 |
| (4,7) | 260 | 42.0000 | 11 | 3.2003 |
| (7,4) | 260 | 42.0000 | 11 | 3.2003 |
| (0,10) | 66 | 43.3333 | 10 | 3.1324 |
| (3,8) | 234 | 43.3333 | 11 | 3.1885 |
| (8,3) | 234 | 43.3333 | 11 | 3.1885 |
| (10,0) | 66 | 43.3333 | 10 | 3.1324 |
| (2,9) | 195 | 45.3333 | 11 | 3.2057 |
| (9,2) | 195 | 45.3333 | 11 | 3.2057 |
| (1,10) | 143 | 48.0000 | 11 | 3.2660 |
| (6,6) | 343 | 48.0000 | 12 | 3.4560 |
| (10,1) | 143 | 48.0000 | 11 | 3.2660 |
| (5,7) | 336 | 48.3333 | 12 | 3.4593 |
| (7,5) | 336 | 48.3333 | 12 | 3.4593 |
| (4,8) | 315 | 49.3333 | 12 | 3.4570 |
| (8,4) | 315 | 49.3333 | 12 | 3.4570 |
| (3,9) | 280 | 51.0000 | 12 | 3.4458 |
| (9,3) | 280 | 51.0000 | 12 | 3.4458 |
| (0,11) | 78 | 51.3333 | 11 | 3.4048 |
| (11,0) | 78 | 51.3333 | 11 | 3.4048 |
| (2,10) | 231 | 53.3333 | 12 | 3.4725 |
| (10,2) | 231 | 53.3333 | 12 | 3.4725 |
| (1,11) | 168 | 56.3333 | 12 | 3.5390 |
| (11,1) | 168 | 56.3333 | 12 | 3.5390 |
| (0,12) | 91 | 60.0000 | 12 | 3.6776 |
| (12,0) | 91 | 60.0000 | 12 | 3.6776 |

(Note: dim(3,0)=10 = **n3**, the sole-surviving Paasch-NCG bridge — appears at C₂=6, band-level 3. dim(1,1)=8 is the adjoint at C₂=3, the W_Casimir=9/5 lower-edge anchor C₂(1,1)−C₂(1,0)=5/3.)

**Prefactor m0 (electron N=7) tie to M_KK** (G1 candidate): Paasch's `m*(j)=N(j)^{3/2} m_e` anchors the absolute scale on the electron. m_e=0.51099895 MeV; M_KK=7.4287×10¹⁹ MeV; m_e/M_KK = 6.88×10⁻²¹ — the ~14-OOM (here ~20.2-OOM in MeV) scale separation the framework documents. A Casimir origin for N=7 would tie m0 to M_KK, but since 7 is a **cumulative low-lying count (1+3+3̄)** rather than a clean irrep dim, the tie is structurally weak: the prefactor is set by the electron Higgs-overlap, not by the count itself.

**fb_pair**:
- `forward` = the L12 fold spectrum (`s84_spectrum_cache_L12_tau019.npz`) feeding (p,q) sector content + Casimir grading.
- `backward` = the INV3-W4-1 M_KK-derivability workshop consumes this verdict as **adjudication candidate (c)** ("does N(j)=7n fix m_p hence M_KK?"). This INFO verdict supplies that workshop with: candidate (c) is NOT a clean PASS — the 7n pattern does not have a single-graded-count origin, so N(j)=7n does NOT mechanically fix m_p/M_KK. The framework's M_KK-DERIVATION standing gap (atlas-04 single imported scale) is NOT closed via this route.

**Substrate-physics assessment** (substrate-first, per `phononic-framing.md`):
The framework's canonical mass ladder `m_g ∝ exp(−k·C₂(p,q))` with super-linear Casimir (the W_Casimir=9/5=1.800 block-trace widening, `S101-W2-BLOCKTRACE-WIDENING` PASS) is the **STRUCTURAL TYPE** of Paasch's N(j) integer scheme — an integer-graded, exponential-in-a-super-linearly-growing-quantity ladder — and decisively NOT the type of his geometric φ^n series (uniform widening, provably absent from D_K per PAASCH-CC CLOSED). So the framework and Paasch agree at the level of *type* (integer/Casimir-graded, not geometric). But at the level of the *specific integers*, the SU(3) Casimir/dimension content of D_K reproduces only **2-of-5** of Paasch's N(j) as 7n (the two that happen to be irrep dimensions, muon 35 and pion 42), with no single grading reaching the rest. The electron's 7 is a cumulative low-lying multiplicity (1⊕3⊕3̄), not a dimension; the kaon's 98 and proton's 150 have no SU(3) home at all. Direction of explanation held throughout: D_K eigenvalues → Peter-Weyl (p,q) content → Casimir grading → mode-count integers → Paasch's mass numbers (never inverted). The **G2 answer** ("which Paasch object does the framework realize?") sharpens to: the framework realizes Paasch's *integer-graded exponential mass-ladder TYPE* (via W_Casimir=9/5), but NOT his *specific N(j)=7n integer values* through any single SU(3) Casimir-graded mode count. The lone arithmetic residue worth flagging is **150/98=1.5306 ≈ φ_paasch (0.063%)** — but it is a ratio of two SU(3)-homeless integers and is not promoted (a mass-phenomenology near-coincidence, consistent with the honest-count discipline). G1 (the m0↔M_KK tie via electron N=7) is not supported, because 7 is a count, not a scale-setting dimension.

---

### §W3-5. INV3-W3-5-KOIDE-CASIMIR-Z3-FOOT

**Status**: COMPLETED
**Gate ID**: `INV3-W3-5` (short form; `scheme=KOIDE-CASIMIR-Z3-FOOT`)
**gate_type**: `compute`
**Trigger**: `[CHAIN]` (Q=2/3 ratio + 45° angle claim — substitution chain mandatory; `schema_v2_3tuple_required: false`)
**Classification**: **PARTICLE** on a **GEOMETRIC** substrate (Koide Q=2/3 is a charged-lepton mass relation; the √m vector IS Paasch's M-value vector M(j)=(m_j/m_e)^{1/3})
**Agent**: `paasch-mass-quantization-analyst`
**Hypothesis**: Koide's Q=(Σm_l)/(Σ√m_l)²=2/3 falls out of the framework's Casimir-envelope √m vector √(m_g)~exp(−k·C₂(p,q)/2) over the three triality-distinct sectors (1,0)/(1,1)/(3,0), with the 45° Foot angle (cos²θ=1/2 between the √m vector and (1,1,1)) emerging from the Z₃ junction symmetry of the three wall types.
**Plan reference**: `sessions/investigation/investigation-3/investigation-3-plan-w3.md` §W3-5.

**Verdict**: **INFO** — Q=2/3 is **reachable** within the Casimir-envelope family but **only by fitting** the decay constant k; it is **NOT forced by the Z₃ symmetry**. The Z₃-symmetry-distinguished point (k=0, where all three √(m_g) become equal) gives **Q=1/3**, not 2/3. The 45° Foot angle at the Q=2/3 crossing is **Foot's 1994 algebraic identity** (Q=2/3 ⟺ cos²θ=1/2), NOT an independent confirmation of a Z₃ origin. Per the pre-registered KILL discipline (derived-from-Z₃ vs fitted-k): reachable, not derived ⇒ INFO.

**Output Artifacts** (closure-verification checklist):
- **script** `computations/investigation-3/inv3_w3_koide_casimir_z3_foot.py` — EXISTS. `grep -E 'from canonical_constants import'` → `from canonical_constants import *` + `from canonical_constants import phi_paasch` (2 hits); `grep -E 'print_verdict_payload'` → def + call (2 hits). PASS.
- **data** `computations/investigation-3/inv3_w3_koide_casimir_z3_foot.npz` — EXISTS (written by run; keys incl. `k_grid`, `Q_grid`, `theta_grid`, `k_star`, `Q_at_kstar`, `theta_at_kstar`, `z3_forced`, `cache_lam_min`, `verdict`).
- **plot** `computations/investigation-3/inv3_w3_koide_casimir_z3_foot.png` — EXISTS (Q(k) + θ_Foot(k) panels; k*=1.7053 marked FITTED, Q=1/3 democratic line at k=0).
- **verdict_line** `computations/investigation-3/inv3_gate_verdicts.txt` — `^INV3-W3-5:.* audit_sha256=[a-f0-9]{64}` matched; dual-SHA companion row present (`audit_sha256_short=c2b1d0441d345049`); schema-v2 3-tuple NOT emitted (not required).
- **input prereq** L12 fold cache `computations/session-84/s84_spectrum_cache_L12_tau019.npz` — PRESENT (SHA `9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9`); sub-test 3 ran (NOT PRE-REG-INC).

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script, per `.claude/rules/knowledge-index-usage.md`):
- `search_knowledge("Koide Q=2/3 charged lepton mass relation Foot angle 45 degrees")` → HIT: `sessions/framework/Collabs/framework-paasch-potential.md` §3.3 "The 45-Degree Angle and Z_3 Geometry" + line 461 Koide-from-Z₃ (flagged "speculative but structurally motivated") + `n_3=dim(3,0)=10`. **This gate makes that flagged hypothesis decidable.** PDG charged-lepton masses surfaced.
- `search_knowledge("Casimir-envelope sqrt mass exp(-k C2) triality sectors (1,0) (1,1) (3,0)")` → HIT: `session-100a-plan-w2.md` `C2=(4/3,3,6) for (1,0)/(1,1)/(3,0)` (Sage-confirmed, C₂(1,1)/C₂(1,0)=9/4, S61 W8); `s100a-w2-mass-functional-counting-workshop.md` heavy pair (μ,τ)=((1,1),(1,0)), heaviest=(1,0).
- `search_knowledge("Z3 wall geometry domain wall junction triality 120 degrees lepton")` → HIT: `framework-paasch-potential.md` `E_junction=3σL−T_core`, 120° Z₃ junction by discrete rotational symmetry; JUNCTION-angle gate (effective spiral angle <50°, "compatible with Paasch's 45°") = **UNCOMPUTED**. The 45-vs-120° incommensurability is a KNOWN structural objection (§3.3 line 168).
- `search_knowledge("S99 sector assignment charged lepton Casimir-graded exponential mass function")` → HIT: `session-101-plan-w2.md` Casimir-graded charged-lepton envelope; N(π)=42 Paasch exponential (session-56-paasch-collab).
- `trace_entity("Foot angle Koide 45 degrees Z3 junction")` → no trace (no prior dedicated entity); `trace_entity("Casimir-envelope mass exp(-S0 C2) charged lepton")` → no trace.
- `get_constant("phi_paasch")` → **1.53158** (no PROVENANCE entry; PROVEN bare (3,0)/(0,0) ratio at s=0.15). `get_constant("S0")` → not found (sourced substrate-first from S101 verdict files per plan; not needed for this gate — Koide is scale-invariant).
- **NOT PRE-CLOSED**: no closure or canonical result evaluates Q=2/3 from the Casimir-envelope over (1,0)/(1,1)/(3,0). The prior framework treatment (`framework-paasch-potential.md` §3.3 + line 461) is a *flag*, not a computed gate; this gate is the first decidable evaluation.

**Results**:

4-tuple: `(value=INFO_Q2/3-reachable-by-fit-NOT-Z3-forced, scheme=KOIDE-CASIMIR-Z3-FOOT, convention=RATIO, L_max=12)`.

**Substitution chain (executed, Sage + numpy; numbers substituted):**
- Step 1 — Koide Q = (Σm_l)/(Σ√m_l)² [Koide 1983]. PDG (in-script): Q=**0.66666051**, θ_Foot=**44.999735°** — the real-world Foot fact.
- Step 2 — Foot (1994): Q=2/3 ⟺ cos²θ=1/2 ⟺ θ=45°, θ = angle between v=(√m_e,√m_μ,√m_τ) and (1,1,1). **This is an algebraic identity, reported as such — not an independent prediction.**
- Step 3 — Casimir-envelope √(m_g)=exp(−k·C₂/2); **C₂=(4/3, 3, 6)** for (1,0)/(1,1)/(3,0) (Sage-confirmed). v(k)=(exp(−2k/3), exp(−3k/2), exp(−3k)).
- Step 4 — Q(k)=[exp(−4k/3)+exp(−3k)+exp(−6k)] / [exp(−2k/3)+exp(−3k/2)+exp(−3k)]². Q is **monotone** from Q(0)=**1/3** (the N=3 democratic value) to Q(k→∞)=**1**. The Q=2/3 root: **k\*=1.7053418260** (Q(k\*)=0.66666667, bisection on the closed form).
- Step 5 — θ_Foot(k\*)=**45.00000000°**, cos²θ(k\*)=**0.500000000000** — exact, BY Foot's identity (Step 2), since Q(k\*)=2/3.

**The discriminator (derivation vs fit) — the load-bearing result:**
- The Z₃-symmetry-distinguished point is **k=0**: this is the ONLY k at which the three √(m_g) are equal (C₂=(4/3,3,6) are distinct, so exp(−k·C₂/2) coincide only at k=0). At k=0, **Q=1/3** (the maximally democratic N=3 Koide value) — **NOT 2/3**. The symmetric point does not realize Koide.
- k\*=1.7053 is a **finite-hierarchy** point, far from the symmetric k=0. It matches **no** Casimir/φ/golden-distinguished constant within the pre-registered 2% Z₃-forcing tolerance: closest is **5/3 at 2.32%** (just outside), then golden=1.618 at 5.4%, φ_paasch=1.5316 at 11.3%, fN=√5−1 at 38%. ⇒ `z3_forced = False`.
- **Conclusion**: Q=2/3 is reached only by **tuning k** to 1.7053; the Z₃ symmetry does **not** single it out. Reachable-by-fit, not derived ⇒ **INFO** (exactly the rubric's INFO clause).

**Cache cross-check (sub-test 3; independent realization):** bottom-of-band |λ|_min for (1,0)/(1,1)/(3,0) at τ_fold=0.190 = (0.835894, 0.872975, 1.248264), dims (3,8,10). Treating √m∝|λ|_min directly: Q=**0.345236** (θ=10.70°); treating √m∝exp(−|λ|_min): Q=**0.343314** (θ=9.82°). Both sit near the democratic 1/3, **nowhere near 2/3** — the actual cache masses do not spontaneously realize Koide either. This independently corroborates that Q=2/3 over these three sectors is not a structural feature of the substrate spectrum but a tuned point of the analytic envelope.

**45-vs-120° resolution (the right way, per substrate framing):** the gate confirms the framework's `framework-paasch-potential.md` §3.3 incommensurability concern is correctly dissolved by SPACE-separation — the Z₃ walls meet at 120° in **real** space, while the Foot 45° lives in **mass-space** (the angle between the Casimir-envelope √m vector and (1,1,1), set by the triality-sector Casimirs C₂). The gate shows the 45° IS realizable in mass-space at k\*. **But realizability ≠ Z₃-forcing**: mass-space can host 45° at a tuned k; it does not make 45° a consequence of the 120° junction symmetry. The incommensurability is dissolved (different spaces), but the *derivation* of Koide from Z₃ is NOT established.

**Substrate-physics assessment:**
- **Direction of explanation honored**: D_K's three triality-distinct Peter-Weyl sectors → C₂=(4/3,3,6) (GEOMETRIC, exact) → Casimir-envelope masses exp(−k·C₂/2) → √m democratic vector → Koide Q + Foot angle. The substrate is not a container in which leptons "happen" to satisfy Q=2/3.
- **Mass-phenomenology honest count**: a monotone Q(k) with continuum range [1/3, 1] will cross 2/3 for a *wide* class of three-sector envelopes — reachability alone is cheap (the look-elsewhere problem of the Paasch tradition). The KILL criterion (Z₃-forced k\*) was pre-registered precisely to deny PASS to mere reachability. The gate correctly returns INFO.
- **What survives**: the geometric mass-space resolution of the 45-vs-120° objection (a structural clarification), and a concrete, decidable replacement for the previously-UNCOMPUTED JUNCTION-angle flag. **What does NOT survive**: the claim that Koide's Q=2/3 / the Foot 45° is *derived* from the Z₃ junction symmetry over (1,0)/(1,1)/(3,0). UB5 is not closed as a derivation; it is downgraded to "reachable-not-derived." The Z₃-forcing question (is there a circulant/democratic structure on the three triality-odd sectors that singles out k\*≈1.705?) is the carry-forward.
- **Bridge-map status**: this connects Paasch's M-values (=√m) to the Koide tradition (Foot/Sumino/Brannen) the framework had not engaged — but as a *family-membership* statement (Koide lies in the Casimir-envelope family), not a derivation. Cross-link: my memory's Koide note (Q=2/3 ⟺ cos²θ=1/2 ⟺ 45° EXACT; PDG Q=0.66666051) is reproduced in-script.

**Input-SHA verification**: `canonical_constants.py` = `fa2d94018ac1b098daaa85d8c00866dc0c11ab19c3f6fbcf3bb15c827867c8e7`; L12 cache = `9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9`. **Dual-SHA**: `audit_sha256=c2b1d0441d34504903d18a4769d9eccd1c0370e27633b5324faeaa37e83cf227`, `content_sha256=fdf432d4ad37e30701eccb93f56fdc5c311ae5490e678608a82422d4a63f9f0a`.

**Artifacts**: `inv3_w3_koide_casimir_z3_foot.py` / `.npz` / `.png`; verdict line in `computations/investigation-3/inv3_gate_verdicts.txt`.

---

## Wave 3 Synthesis (team-lead)

Wave 3 connected the framework's Casimir-graded exponential mass namespace (S100a/S101) to Paasch's ~70-year program and harvested the five untraveled bridges (UB1–UB5) as one solo + four compute gates: **1 FAIL (W3-2), 4 INFO (W3-1, W3-3, W3-4, W3-5)**. The coherent reading: the Paasch↔framework connection is real at the level of *type and proximity*, but only ONE strong claim promotes to a structural identity, and every scale-fixing / universality / forced-coincidence claim is killed cleanly by its pre-registered criterion.

**The bridge map after Wave 3:**

| Bridge | Gate | Verdict | Status |
|:-------|:-----|:--------|:-------|
| **UB1** N(j)=7n / G1 absolute scale | W3-4 | INFO | TYPE realized (W_Casimir=9/5 super-linear Casimir ladder), but specific integers only 2-of-5 (35,42 are SU(3) dims; 7,98,150 homeless) and G1 m0↔M_KK tie NOT supported (7 is a count 1⊕3⊕3̄, not a dim) |
| **UB2** φ_paasch a universality-class number | W3-2 | **FAIL** | CLOSED — M(6,5) c=4/5 kink doublet is mass-degenerate (ratio 1.000); φ_paasch stays a bare-(3,0)/(0,0) geometric fact (consistent with PHI-BDG-47) |
| **UB3(i)** α-dim n3=dim(3,0)=10 | W3-3(i) | **PASS** | **A1 PROMOTED to a chain-level SU(3) identity** — α=0.855 ppm, only n3=10 sub-ppm, proton-cubic shares the same 100=n3². The wave's one clean structural positive |
| **UB3(ii)** two-α (1/10.8 → 1/137) | W3-3(ii) | FAIL (mag) | SIGN right (1/α screens UV→IR) but magnitude off; 137 is the SM-running endpoint of the *measured* 1/α(M_Z), not what 1/10.8 runs to. C3 latent, not contradicted |
| **UB4** S₀ = φ_paasch^fN | W3-1 | INFO | CLOSED as coincidence — δ_min=4.19e-4, a 4-sig-fig proximity ~8 OOM above the identity bar |
| **UB5** Koide Q=2/3 from Z₃ | W3-5 | INFO | downgraded derived→**reachable-not-derived** (Z₃-democratic k=0 gives Q=1/3; Q=2/3 needs a fitted k*=1.705). 45-vs-120° objection dissolved by space-separation |

**Honest-count discipline worked.** Mass phenomenology is dense with coincidences — W3-2 found 236 of 1307 scanned algebraic ratios within 5% of φ_paasch/fN. The pre-registered kill criteria (machine-ε for an identity; Z₃-forcing for Koide; ≥4-of-5 for N(j)=7n; universality-class membership for φ_paasch) denied PASS to mere reachability/proximity, so 4 of 5 gates returned INFO/FAIL — each a corridor closed, not a failure. The one survivor (A1) is robust because it is *over-determined* (the same n3²=100 reconstructs both α and the proton-cubic; only n3=10 works). The G2 question ("which Paasch object does the framework realize?") sharpens to: the **integer-graded exponential mass-ladder TYPE** (via W_Casimir=9/5), NOT his specific N(j)=7n integers or his geometric φ^n series (PAASCH-CC closed).

### W3 → W4 hand-off (decisive for the M_KK workshop)
**W3-4 IS the decisive-forward-gate candidate (c)** named by INV3-W4-1, and it returned a clear negative: N(j)=7n does NOT mechanically fix m_p/M_KK (the 7n pattern has no single SU(3)-graded-count origin; the electron-N=7 scale anchor is unsupported). Combined with W2-1 (d_s-flow ≠ scale-transport) and W2-4 (geodesic-stationarity ≠ τ_fold-selection), **both advocates' candidate routes to a substrate-internal emergent M_KK have now come back negative** — the spectral-geometer's two emergent-scale routes AND the paasch integer-structure route. This materially constrains the W4-1 adjudication toward PROVEN-IMPOSSIBLE-WALL or a precisely-scoped INTERMEDIATE (e.g. "type-derivable, value/normalization-not"). W3-3(i)'s A1 identity is the live counterweight the paasch advocate brings: the SU(3) integer structure DOES fix a dimensionless coupling (α) exactly — the open question for (b) is whether that ever reaches a dimensionful m_p without importing a scale.

### What Changed

#### (a) Numerical revisions
- α(n3=dim(3,0)=10) = 0.007297358806 = **0.855 ppm** vs CODATA (only n3=10 sub-ppm; n3=9→23%, n3=11→17%).
- φ_paasch^fN = 1.6937341257; δ_a(S₀=1.694153)=4.188743e-04, δ_b(95/56)=2.694446e-03.
- N(p)/N(K) = 150/98 = 1.5306122 vs φ_paasch=1.531580 (0.063% — homeless-integer ratio, NOT promoted).
- Koide Q=2/3 crossing at fitted k*=1.7053418 (Z₃-democratic k=0 gives Q=1/3); M(6,5) c=4/5 kink-mass ratio = 1.000 (degenerate doublet).

#### (b) Structural changes
- **A1 (n3=dim(3,0)) PROMOTED**: "necessary coincidence" → chain-level SU(3) identity (over-determined across α + proton-cubic).
- **UB2 CLOSED (FAIL)**: φ_paasch is NOT a c=4/5 universality-class number — the A3 six-sequence↔Z₃-wall map loses its universality-class anchor.
- **UB5 downgraded**: Koide-from-Z₃ derived → reachable-not-derived; 45-vs-120° incommensurability dissolved by space-separation (45° in mass-space, 120° in real-space).
- **UB4 closed as coincidence**; **G2 sharpened** (type-match via W_Casimir=9/5, not specific integers).

### Effected In-Session (non-math)
- [x] Removed orphaned one-shot WP-writer helper `computations/investigation-3/_inv3_w3_3_wp_writer.py` (the W3-3 agent's atomic-substitution scratch script; siblings W3-2/4/5 removed theirs — in-session hygiene per `CLAUDE.md §"No Technical Debt"`). Verified 0 `_wp_writer` helpers remain.

All other non-math items are **session-track curated-register edits** an investigation cannot make — they route to `/rclab-investigate --investigation 3` close:
- [→investigate] **A1 session-promotion**: land the n3=dim(3,0)=10 chain-level SU(3) identity in the permanent register (see CF-INV3-W3-A) — the wave's strongest positive.
- [→investigate] HY8 (`phi_paasch` carries NO PROVENANCE entry in the knowledge MCP — register tag); HY9 (Paasch LNH Dirac-G~1/t scaffolding exclusion note); HY11 (OCR-garbled-formula re-pin) — all session-track register hygiene per the seed's §"Non-gate items".

## Carry-Forward Computations

Genuine future compute (4-field) → `/rclab-investigate --investigation 3`. W3-2 (UB2) and the UB4/N(j)-value claims are CLOSED (no re-run is a carry-forward). The three below are the wave's live forward items.

### CF-INV3-W3-A — Session-promote the n3=dim(3,0)=10 chain-level SU(3) identity (A1)
| Field | Spec |
|:------|:-----|
| **What** | Re-run the α-dim chain reconstruction (α=(1/n3²)(Ω/2)^¼ + proton-cubic βu²) as a session-track gate; land a permanent-results entry: "n3=dim(3,0)=10 is a chain-level SU(3) identity — the same n3²=100 reconstructs both the sub-ppm α and the proton-cubic; only n3=10 is sub-ppm." |
| **Inputs** | `computations/investigation-3/inv3_w3_alpha_dim_n3_two_alpha.py`; Ω=W(1)=0.5671432904; dim(3,0)=10; CODATA α; Paasch Paper-03 cubic. |
| **Gate** | \|α(n3=10) − α_CODATA\|/α_CODATA ≤ 1e-6 reproduced on the session track; n3-sensitivity confirms 10 uniquely sub-ppm. |
| **Effort** | ~0.5 wave-equiv (script exists; session-track re-run + registry landing). |

### CF-INV3-W3-B — Two-α reconciliation under correct KK+SM threshold structure (C3)
| Field | Spec |
|:------|:-----|
| **What** | Resolve whether the framework's UV unified coupling runs to the IR Thomson α=1/137 — first pinning the α_GUT anchor (the 1/10.8 Q18a vs 1/40 s42-snapshot vs 1/39.47 Model-C spread, ~3.7×), then running with the framework-computed KK + SM thresholds. Closes C3 (currently directionally-supported, magnitude-unclosed). |
| **Inputs** | `inv3_w3_alpha_dim_n3_two_alpha.py` (RG flow); the three α_GUT readings; M_U=7.68e14 GeV (Model-C); the framework's KK-threshold spectrum. |
| **Gate** | \|1/α_IR_run − 137.036\|/137.036 ≤ 0.10 under a single pinned α_GUT + threshold structure, OR a named structural reason the two α-objects stay disjoint. |
| **Effort** | ~1 wave-equiv. |

### CF-INV3-W3-C — Z₃-forcing closure for Koide (the k*≈1.705 question)
| Field | Spec |
|:------|:-----|
| **What** | Test whether a circulant / democratic structure on the three triality-odd sectors (1,0)/(1,1)/(3,0) singles out the Koide decay constant k*≈1.7053 — i.e. whether Q=2/3 is *forced* by a deeper Z₃ structure rather than reached by tuning. Resolves the UB5 reachable-vs-derived gap. |
| **Inputs** | `computations/investigation-3/inv3_w3_koide_casimir_z3_foot.py`; C₂=(4/3,3,6); the Z₃ wall-junction structure (`framework-paasch-potential.md §3.3`). |
| **Gate** | k* matches a Z₃/circulant-distinguished constant within 2% (→ derived) OR not (→ confirmed reachable-not-derived, UB5 permanently downgraded). |
| **Effort** | ~1 wave-equiv. |

## Constraint-Map Updates

| Date | Mechanism / gate | Prior state | New state | Reason |
|:-----|:-----------------|:------------|:---------|:-------|
| 2026-06-15 | UB3/A1 — n3=dim(3,0)=10 | necessary numerical coincidence | chain-level SU(3) identity (over-determined) | W3-3(i) α 0.855 ppm + proton-cubic share n3²=100; only n3=10 sub-ppm |
| 2026-06-15 | UB2 — φ_paasch as universality-class number | OPEN (candidate c=4/5 origin) | CLOSED — NOT a c=4/5 number | W3-2 M(6,5) kink doublet mass-degenerate (ratio 1.000); no ratio within 2% |
| 2026-06-15 | UB4 — S₀ = φ_paasch^fN | OPEN (candidate identity) | CLOSED as coincidence | W3-1 δ_min=4.19e-4, dead-band; ~8 OOM above identity bar |
| 2026-06-15 | UB5 — Koide Q=2/3 from Z₃ | candidate derivation | reachable-not-derived | W3-5 Z₃-democratic k=0→Q=1/3; Q=2/3 needs fitted k*=1.705 |
| 2026-06-15 | UB1/G2 — Paasch N(j)=7n vs framework | OPEN (candidate value-match) | TYPE-match only (W_Casimir=9/5); 2-of-5 integers; G1 scale-tie unsupported | W3-4 INFO; 7=1⊕3⊕3̄ count not dim |
| 2026-06-15 | C3 — two α-objects (UV unified vs IR Thomson) | disjoint, untested | directionally-supported (sign), magnitude-unclosed | W3-3(ii) 1/α screens UV→IR but 1/10.8 ↛ 137 within band |
| 2026-06-15 | M_KK-DERIVATION (W4-1 input) | #1 gap; Reading-P integer route open | Reading-P route (N(j)=7n scale-fixing) negative | W3-4 candidate (c) returns negative; both advocates' emergent-scale routes now closed |

## Files Produced

| Gate | Script (`computations/investigation-3/`) | Data (.npz) | Plot (.png) | Verdict | audit_sha256 (head) |
|:-----|:------------------------------------------|:------------|:------------|:--------|:--------------------|
| INV3-W3-1 (solo) | inv3_w3_s0_phi_fn_identity.py | ✓ | ✓ | INFO | d7994562… |
| INV3-W3-2 | inv3_w3_w3_minimal_model_kink_phi.py | ✓ | ✓ | FAIL | e99cf44a… |
| INV3-W3-3 | inv3_w3_alpha_dim_n3_two_alpha.py | ✓ | ✓ | INFO (i-PASS/ii-FAIL) | 2ee49a82… |
| INV3-W3-4 | inv3_w3_casimir_graded_nj_7n.py | ✓ | ✓ | INFO | 0b5f371f… |
| INV3-W3-5 | inv3_w3_koide_casimir_z3_foot.py | ✓ | ✓ | INFO | c2b1d044… |

(Verdict ledger: `computations/investigation-3/inv3_gate_verdicts.txt`.)
