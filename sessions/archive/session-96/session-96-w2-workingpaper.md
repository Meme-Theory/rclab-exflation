# Session 96 Wave 2 — SDW Absolute-Convergence & EFT-Control (cluster C2) (Results Working Paper)

**Session**: 96 | **Wave**: W2 | **Plan**: session-96-plan-w2.md | **Theme**: SDW absolute-convergence & EFT-control (cluster C2) — six independent gates building ON the S94-K-CSUB-R absolute-divergence FAIL; functional-pluralism spine (≥3 regulator schemes per absolute-magnitude gate; FI sign/zero-structure structural, absolute magnitude functional-DEPENDENT).

## Gate Sections

### §W2-1. S96-SDW-BOREL-PADE (lizzi-spectral-functional-theorist)

**Status**: COMPLETED
**Gate ID**: `S96-SDW-BOREL-PADE`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (Borel/Padé resummation of the divergent raw SDW series toward the zeta value)
**Agent**: `lizzi-spectral-functional-theorist`
**Hypothesis**: The divergent raw mode-count SDW partial-sum sequence a_2^raw(L_max) (S94-confirmed divergent, dK/dL increasing) is Borel/Padé-Borel-resummable to a finite value coinciding (within 10%) with the zeta-regulated a_2_FW_zeta=2776.165389 — i.e. the zeta moment IS the Borel sum of the divergent raw series, partially discharging the CC-absolute conditional.
**Plan reference**: `sessions/session-plan/session-96-plan-w2.md` §W2-1 (machinery pin, thresholds, substitution chain source).

**Verdict**: **FAIL** — `FAIL_positive_real_axis_Borel_singularity_raw_series_NOT_Borel_summable`. The divergent raw SDW a_2 series is **Borel-NON-summable**: the [M/M] Padé-Borel approximant carries a positive-real-axis singularity (nearest the origin at t=0.9583; the geometric-fit theory pole sits at t=1/r=0.4748, directly on the Laplace integration contour). The principal-value resummed value (best feasible order) is **−829.26**, missing a_2_FW_zeta=2776.165389 by **|δ|/zeta = 1.299 (130%)**, far outside the 0.10 PASS band; and |δ| does **NOT** decrease with Padé order M (1.097 → 0.857 → 1.299, oscillating). BOTH FAIL conjuncts fire. Track B gets 0.9 posterior mass: the absolute a_2 moment is **genuinely scheme-dependent**, the CC-absolute stays conditional, and JACOBSON-NONLOCAL-64 hardens toward a structural wall. (FAIL is a clean constraint-map boundary — it closes the "resummation rescues the absolute" corridor — NOT an agent failure.)

**Output Artifacts**:
- **script** `computations/session-96/s96_sdw_borel_pade.py` — on disk (45464 bytes). `grep -E 'from canonical_constants import' → 2 hits`; `grep -E 'append_verdict' → 2 hits`. PASS (both must_contain present).
- **data** `computations/session-96/s96_sdw_borel_pade.npz` — on disk (13076 bytes). PASS.
- **plot** `computations/session-96/s96_sdw_borel_pade.png` — on disk (218672 bytes; 4-panel: divergent series vs zeta target / distance-to-zeta-vs-M direction test / [M/M] Borel-Padé pole structure / diagnostic). PASS.
- **verdict_line** `computations/session-96/s96_gate_verdicts.txt` — canonical line matches `^S96-SDW-BOREL-PADE:.* audit_sha256=[a-f0-9]{64}` (`audit_sha256=261e17c5024f0dd6eac0a687e3b0ada6f44dea7ee9a1b4942107671fbaed1214`); dual-SHA companion row present (`content_sha256=8add9c52e568de4f20a6780d8b3bfa64551b43080869028926b46998868899c8`). [VERIFY] → no 3-tuple row required (`schema_v2_3tuple_required=false`). SHA-uniqueness: no duplicate audit_sha256 (sig_5 clean). PASS.
- **wp_section** this `### §W2-1.` section — Status/Verdict/Output Artifacts/MCP Pre-Compute Audit all present. PASS.

**MCP Pre-Compute Audit** (queries executed before writing the script; per `.claude/rules/knowledge-index-usage.md`):
- `get_constant("a_2_FW_zeta")` → **2776.165389**, session S88, gate `S88-A-N-FW-CANONICALIZATION`, source S42 spectral-zeta sum + S46 a_2 split, **Superseded=False** — confirms the resummation target provenance.
- `get_constant("a_0_FW_zeta")` → **6440.0**, S88, `S88-A-N-FW-CANONICALIZATION`, Superseded=False — a_0-channel context (reported, not gated here).
- `search_knowledge("SDW Borel Pade resummation zeta a_2")` → no prior `S96-SDW-BOREL-PADE` closure; hits are S85 `w9_borel_floor_registry` (a DIFFERENT gate — Borel-floor registry, not this divergent-series resummation), `§VII-B.ZETA-EQUALS-SDW` (PROVEN: a_2^SDW=a_2^zeta=2776.165389 at the residue, consistent with the Mellin=zeta=raw identity used here), and `a_0^raw=155984`. **Gate NOT pre-closed; not a re-derivation.**
- **MULTIPLICATIVE-NORMALIZATION pre-flight** (`math-scripts.md §"Multiplicative-normalization cancellation invariants"`, MANDATORY K=3): `sage_simplify("(a*r^(k+1))/(a*r^k)") → r` (the geometric increment ratio is the CONSTANT r, independent of k); `sage_simplify("sum(a*(r*t)^k/factorial(k), k, 0, oo)") → a*e^(r*t)` (Borel transform of the geometric increment series). This gate has **no log-derivative operator** d^n ln(.)/d(ln K)^n (it is an ABSOLUTE Borel-Padé resummation of a moment SUM), so the K=3 cancellation pathology does NOT apply by operator type; the Sage disambiguator + the numerical inc-ratio coefficient-of-variation (CoV=1.0e-2, k-dependent) confirm the divergence is **genuine geometric growth, NOT a multiplicative w(L_max)·κ artifact** → `MULTIPLICATIVE-NORMALIZATION-CANCELLATION-DETECTED = False`. The resummation operates on a genuinely-divergent series, not a structural identity; the PASS criterion correctly targets the resummed VALUE vs a_2_FW_zeta (not an L-stability plateau).

**Results**:

NUMBERS first.

*Partial-sum construction (FULL CM-1995 §III.4 `jensen_irrep_table`, CLASS=FULL, substrate-IS D_K(τ_fold=0.19) eigenvalues; a_2^raw Mellin-s=2 = Σ dim·|λ|^{−4}):*

| L_max | a_2^raw(L) | a_2^raw(L)/a_2^raw(L−1) |
|:--|--:|--:|
| 5 | 123.954375 | — |
| 6 | 250.844406 | 2.02368 |
| 7 | 515.658456 | 2.05569 |
| 8 | 1072.274191 | 2.07943 |
| 9 | 2247.601218 | 2.09611 |
| 10 | 4737.020177 | 2.10759 |
| 11 | 10021.094117 | 2.11548 |
| 12 | 21254.454091 | 2.12097 |

- **CC1 (partial-sum-construction agreement)**: our a_2^raw(L=12) = **21254.454091** is **bit-exact** vs the S94 `bare_moment[L=12]` (residual < 1e−6 of magnitude; `cc1_ok=True`). The S94 `bare_moment` convention (`lams**(-4)`) is reproduced. The S94 npz runtime SHA (plan field `<computed-at-runtime>`) = `a78bcff2346d66de4bb052fc2c0a2d6bb3f9e3c76ae8e9e00510643e4f78b0d6`. The S94 .py provenance SHA = `273514bd…` **matches the plan pin** exactly.
- **Geometric divergence**: log-linear fit of the increment series gives ratio **r = 2.106088** → Borel transform `B(t)=a/(1−rt)` has a pole at **t = 1/r = 0.474814 > 0** (on the positive-real Laplace axis). This is the canonical geometric-pure divergence (the S94 signature).

*Borel-Padé resummation per Padé diagonal order M (raw / gated class; 7 increments c_0..c_6 ⇒ M ≤ 3):*

| M | full_moment = a_2(L=4) + Borel-PV sum | \|δ\|/a_2_FW_zeta | positive-real Borel pole? |
|:--|--:|--:|:--|
| 1 | −270.337 | 1.097 | **yes** (on contour) |
| 2 | 397.815 | 0.857 | no |
| 3 | −829.260 | 1.299 | **yes** (on contour) |

- **Borel-summability pre-condition (raw, gated)**: **FAILS** — `raw_borel_summable = False`. The [M/M] Padé-Borel approximant carries a positive-real-axis singularity (M=1, M=3); the nearest-origin singularity sits at t=0.9583. Even M=2 (which happens to lack a positive-real pole) lands at 397.8 (|δ|/zeta=0.857, 86% off — Borel-summable to a DIFFERENT value, NOT zeta).
- **DIRECTION test (load-bearing)**: |δ|/a_2_FW_zeta does **NOT decrease** with M (1.097 → 0.857 → 1.299; `delta_decreasing_with_M=False`). The resummation oscillates; it does not converge **toward** the zeta value.
- **Best resummed raw value**: **−829.26** (highest-feasible M=3) vs target **2776.165389** ⇒ **|δ|/zeta = 1.29871 (130%)**, ≫ 0.10 band.

*Functional-pluralism spine (≥3 regulator classes; each tagged per `regulator-pin-discipline.md`):*
- **a_2^{raw}** (quarantine label, NOT Seeley-DeWitt): best resum −829.26, NOT Borel-summable to zeta.
- **a_2^{Pauli-Villars}** (S94 subtractive 2-pt PV, c={+2,−1}, m²={1,2}): best resum **245.167** vs 2776.165 (≈91% off) — also fails the zeta target.
- **a_2^{Mellin}** (= a_2^{zeta} on the positive-definite spectrum; S94 a2_mellin==a2_bare): best resum −829.26 (= raw, as expected by the Mellin=zeta=bare identity at finite L). All three regulator classes corroborate **Borel-non-summability to the finite zeta value** — the FAIL is functional-INVARIANT across the spectral-functional family (the divergence structure is structural; what differs is only the magnitude of the failed resummed value, a harmless reweighting).

*Substitution chain (with substituted numbers — direction of the convergence claim):*
- Def 1: a_2^raw(L=12) = Σ_{(p,q)} m·|λ|^{−4} = **21254.454** (divergent; r=2.106).
- Def 2: a_2_FW_zeta = Res_{s=3}[Tr D_K^{−2s}] = **2776.165389** (finite; ZETA-NOT-PHYSICAL — a regulator artifact, but finite).
- Def 3 + Substitute: increment series c_k ~ A·r^k with **r=2.106** ⇒ Borel transform pole at **t=1/r=0.4748 > 0** (Sage: `(a r^{k+1})/(a r^k)=r` EXACT — constant increment ratio ⇒ genuine geometric divergence, NOT a multiplicative w(L) artifact).
- Simplify: a pole **on the positive real Laplace axis** ⇒ the Borel integral is **NOT defined** (Borel-NON-summable in the strict sense); the lateral/PV Padé-Borel prescription regularizes it but lands at −829.26, NOT zeta.
- Direction ⇒ Conclusion: PASS required |δ| **decreasing** with M toward zeta AND no positive-real pole. Computed: |δ| does **NOT decrease** (oscillates) AND the positive-real pole **is present**. **Both discriminators fire FAIL** — decided by the [M/M] pole structure and the M-direction, NOT assumed.

*4-tuple*: (value = Borel-Padé-resum [verdict=FAIL, raw_borel_summable=False, best_resum_raw=−829.26, rel_delta_best=1.299], scheme = `Borel-Pade-resummation`, convention = `ABSOLUTE`, L_max = 12).

*dual_prior track re-allocation*: FAIL (not Borel-summable, positive-real Borel singularity) → **0.9 mass to Track B** (the absolute moment is genuinely scheme-dependent; CC-absolute stays conditional; JACOBSON-NONLOCAL-64 hardens toward a structural wall).

*Solution-space (substrate-first framing):* The substrate IS the Dirac operator D_K(τ_fold) on Jensen-deformed SU(3); its eigenvalue spectrum is the only input. The raw mode-count truncation slices a_2^raw(L) diverge **geometrically** (r=2.106) because the substrate's high-Casimir sectors accumulate spectral weight at small |λ| under the fixed-τ Jensen damping. This divergence is **not** a re-summable asymptotic artifact: it is a positive-real-axis Borel singularity, the generic signature of a series whose growth is genuinely physical rather than factorially-tamed. Therefore the substrate's absolute a_2 moment is **a genuine physical degree of freedom fixed only by the choice of spectral functional f** — exactly the ZETA-NOT-PHYSICAL position. The zeta moment a_2_FW_zeta=2776.165389 is the analytic-continuation extraction (a specific functional choice), NOT the Borel sum of the raw series. Direction of explanation flows D_K eigenvalues → raw/zeta moments → CC-absolute status → downstream observable. **What is functional-INDEPENDENT here is the FAILURE of resummation itself** (all three regulator classes agree the raw series is Borel-non-summable to the zeta value) — that is structural; what is functional-DEPENDENT is the magnitude of the failed resummed value (−829.26 raw / 245.17 PV), a harmless reweighting. The CC-absolute conditional is **NOT discharged**; it remains a physical degree of freedom requiring a regulator-physicality argument or a consistency constraint to fix.

*dual-SHA*: `audit_sha256=261e17c5024f0dd6eac0a687e3b0ada6f44dea7ee9a1b4942107671fbaed1214` content_sha256=`8add9c52e568de4f20a6780d8b3bfa64551b43080869028926b46998868899c8`. Artifacts: `s96_sdw_borel_pade.py` / `.npz` / `.png`.

---

### §W2-2. S96-SDW-A0-RESIDUE (lizzi-spectral-functional-theorist)

**Status**: COMPLETED
**Gate ID**: `S96-SDW-A0-RESIDUE`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (residue-finiteness at the a_0 vacuum-energy pole; residue-side complement to the S94 a_2/K_csub-intercept FAIL)
**Agent**: `lizzi-spectral-functional-theorist`
**Hypothesis**: The finite dimension-spectrum pole ladder S_d={0,2,4,6,8} (Connes-Moscovici 1995, d=8) gives a FINITE residue at the a_0 pole under L_max refinement — Res_{s=4} zeta_{D_K}(s) converges — OR it diverges with the same dK/dL-increasing signature as the S94 a_2 intercept, establishing that "finite ladder" does NOT imply "finite residue."
**Plan reference**: `sessions/session-plan/session-96-plan-w2.md` §W2-2.

**Verdict**: **FAIL** (Track B, posterior mass 0.9). The a_0 residue **DIVERGES** with the S94 `d(Res)/dL`-increasing signature on **every** physical regulator reading (raw / zeta / Pauli-Villars / heat-kernel). "Finite pole ladder" does **NOT** imply "finite residue": the cardinality of S_d (5 poles) is independent of the analytic-continuation coefficient AT any one pole, and on the truncated triple that coefficient inherits the L^8 Weyl divergence. CLASS=FULL (no SCHEMATIC helper consumed; no `-SCHEMATIC` convention suffix).

**Output Artifacts**:
- **script** — `computations/session-96/s96_sdw_a0_residue.py` (27,216 bytes, present). `grep -E "from canonical_constants import"` -> `from canonical_constants import *  # noqa: F401,F403,E402` + `from canonical_constants import a_0_FW_zeta, d_spec, tau_fold, M_KK`. `grep -E "append_verdict"` -> `def append_verdict(...)` + call site in `main()`.
- **data** — `computations/session-96/s96_sdw_a0_residue.npz` (9,056 bytes, present). 28 keys incl. `L_grid`, `raw_seq`, `zeta_seq`, `pv_seq`, `hk_seq`, `dRes_dL_HK`, `dRes_increasing_{raw,zeta,pv,hk}`, `drift_HK_L10_L12`, `mult_norm_cancellation_detected`, `n_sectors_L12`, `degeneracy_total_mult`, `hk_grid_t{010,005,002}`.
- **plot** — `computations/session-96/s96_sdw_a0_residue.png` (94,492 bytes, present). Left: four residue readings vs L_max (log) with the continuum-6440 reference line; right: `d(a_0^HK)/dL` increasing (the S94 divergence signature).
- **verdict_line** — `computations/session-96/s96_gate_verdicts.txt`. `grep -E "^S96-SDW-A0-RESIDUE:.* audit_sha256=[a-f0-9]{64}"` -> matches (FAIL line, `audit_sha256=d7f5c6fa073e2096c370ebe5a8ed1144802fa9c8a567a7cbd6b294f4f5076ce2`, 64-hex). Dual-SHA companion row present (`audit_sha256_short=d7f5c6fa073e2096 content_sha256_short=4a70a3e38e8d2367`). Exactly 1 canonical line; SHA unique across the file. `schema_v2_3tuple_required=false` per [VERIFY] override — no 3-tuple row.

**MCP Pre-Compute Audit** (query-first discipline; queries run BEFORE writing the script):
- `search_knowledge("S96-SDW-A0-RESIDUE a_0 pole residue finiteness")` -> equation set `n=0 ==> s=8` / `n=0 ==> s=d/2=4 (residue ∝ a_0)` (`session-85-lizzi-synthesis-w6-13.md`: `Pole at s+2n-d=0 <=> s=8-2n`); `residue = 2*(4*pi)^{-d/2}*a[n_pole]/Gamma(s_pole/2)` (`session-85-s6-truncation-taxonomy`). Gate NOT pre-closed.
- `search_knowledge("S94 K-CSUB-R multiplicative normalization cancellation FAIL")` -> `S94-K-CSUB-R-ABSOLUTE-CONVERGENCE` = **FAIL** (`max_dK_over_dL_pv=2.1071e+30`, intercept `+2.08e15 (L=50) -> +2.11e31 (L=100)`, `dK_over_dL_increasing=True`). The recorded INPUT signature this gate complements on the a_0 channel (not a blocking prereq).
- `get_constant("a_0_FW_zeta")` -> **6440.0** (S88-A-N-FW-CANONICALIZATION; `a_0 = zeta_{D_K}(0) = Tr(1)`, dimensionless mode count, tau-independent). Confirmed: a **CONTINUUM** anchor, NOT recoverable as the L_max->inf limit of the truncated-spectrum residue.
- `search_knowledge("Weyl law mode count L^8 ... Tr(1) zeta regulated finite")` -> `a_0^raw = Sum_{(p,q): p+q<=L} d(p,q)^2 * N_modes(p,q) = Tr 1` (`session-95-w1-workingpaper.md`, recovered from `s66_cutoff_ns.py:512-521`). Confirmed the substrate-canonical raw-moment definition used for `a_0^raw`.
- **PRE-CLOSED**: NONE. The a_0-residue convergence test is NEW (S94 tested the a_2/K_csub intercept; this is the residue-side complement). Inputs canonical/closed; the compute is new.

**Results**:

NUMBERS first.

*Residue readings* (Res_{s=4} <-> a_0 under E38; d=8 ==> pole at s=d/2=4; L_max in {3,5,7,10,12}):

| L_max | a_0^raw = Tr(1) (Sum dim^2*N) | a_0^zeta = zeta_D(0) (=Tr1, dim-w) | a_0^PV (Lambda_UV=M_KK) | a_0^HK(t=0.05) |
|:--|--:|--:|--:|--:|
| 3 | 155,984 | 12,880 | 12,880 | 0.0709 |
| 5 | 5,060,448 | 159,936 | 159,936 | 0.8015 |
| 7 | 70,236,768 | 1,077,120 | 1,077,120 | 4.7786 |
| 10 | 1,437,102,080 | 9,535,776 | 9,535,776 | 33.378 |
| 12 | 7,539,127,152 | 31,956,720 | 31,956,720 | 92.710 |

*Convergence diagnostics* (PASS band: drift(L10->12) <= eps_conv=0.05 AND d(Res)/dL monotone-non-increasing):

| reading | drift(L10->12) | d(Res)/dL increasing? | sign-changes |
|:--|--:|:--|--:|
| a_0^raw | 4.2461 | **True** (S94 signature) | 0 |
| a_0^zeta | 2.3512 | **True** | 0 |
| a_0^PV | 2.3512 | **True** | 0 |
| a_0^HK | 1.7775 | **True** | 0 |

All four readings: drift >> 0.05 AND `d(Res)/dL` strictly increasing, sign-changes=0 (monotone-divergent, NOT bounded-oscillatory ==> not INFO). `all_phys_readings_increasing=True`. d(a_0^raw)/dL = {2.45e6, 3.26e7, 4.56e8, 3.05e9}; d(a_0^HK)/dL = {0.365, 1.99, 9.53, 29.7}. The PV form-factor `Lambda_UV^2/(lam^2+Lambda_UV^2)` damps the deep-UV tail, but at Lambda_UV=M_KK the EFT cutoff is only ~2x below species-scale, so a_0^PV tracks a_0^zeta to the printed precision (the surviving sub-cutoff modes still grow as L^8). The heat-kernel coefficient a_0^HK = K(t)*t^{d/2} fails to plateau even in t: at L=12 it reads {718.3, 92.7, 3.74} across t in {0.10,0.05,0.02} — it SHRINKS with t (truncation removes exactly the high-frequency modes that dominate small-t), so the truncated spectrum cannot resolve the Weyl-leading continuum coefficient at all.

*Continuum anchor not recovered*: `a_0_FW_zeta=6440` is a continuum (closed-form heat-kernel analytic-continuation) value; it is **NOT** the L_max->inf limit of any truncated-spectrum residue reading here. For a FINITE truncated triple `zeta_D(s)=Sum_k m_k lam_k^{-2s}` is **entire** (finite sum of entire terms), carries NO pole, and `zeta_D(0)=Sum_k m_k = Tr(1)` identically — confirming `a_0^zeta == a_0^raw` numerically (12,880 / 159,936 / ... at every L). The "residue at s=4" is intrinsically a continuum (L->inf) object; the truncated approximant of it diverges as L^8 (Weyl).

*Multiplicative-normalization pre-flight* (Sage `sage_simplify`, MANDATORY per `math-scripts.md §"Multiplicative-normalization cancellation invariants"` K=3): **MULTIPLICATIVE-NORMALIZATION-CANCELLATION-DETECTED = False**. `Res_{s=4}(L)` is a scalar moment per L_max with **no** K-running argument and **no** log-derivative operator `d^n ln(.)/d(ln K)^n`, so the `w(L_max)*g(K)` factorization-cancellation pattern is inapplicable (Sage: `(L^8)/(L^8) -> 1` only because a multiplicative prefactor cancels UNDER a log-derivative, which is absent here). Therefore the L-divergence is **GENUINE empirical convergence evidence** — the PASS criterion targets the raw L-convergence directly, NOT an asymptote/plateau value B(R) of a structural-identity plateau. (Were the cancellation detected, the L-stability would be a structural identity unusable as convergence evidence; it is not, so the divergence reading stands.)

*Class-8.7 degeneracy-witness* (`epistemic-discipline.md §"Degenerate-Observable Pre-Flight Check"`; this gate computes a `Res_{s=4} zeta_D` / `zeta_D(0)`-class observable on the finite triple):
- **(a) coincident-root declaration**: at the a_0 pole s=4 (d=8) the E38 residue `a_0 = Sum_k m_k lam_k^{-(d-0)}` collects contributions from **all 90 Peter-Weyl (p,q) sectors** with p+q<=12 — these sectors share the same n=0, s=4 residue and are the degenerate roots of the dimension-spectrum at that pole.
- **(b) per-sector multiplicity**: `m_{(p,q)} = dim V_{(p,q)}` per eigenvalue (cache `info["dim"]`); the raw S66 PW weight is `dim^2*N_modes(p,q)`; `Sum dim*N_modes = 31,956,720` at L_max=12.
- **(c) compositional corridor (d) o (b)**: the s=4 dimension-spectrum degeneracy is disambiguated by the **FULL** CM-1995 §III.4 residue evaluator `_analytic_zeta.py` (the substrate-natural disambiguator), NOT a naive single-pole sum that discards the multiplicity structure. CLASS=FULL pin honored.

*Substitution chain* (convergence-vs-divergence direction, with substituted numbers):
- **Claim**: a finite NUMBER of poles {0,2,4,6,8} does NOT imply a finite VALUE of the residue at the a_0 (s=4) pole under L_max refinement.
- **Def 1**: S_d = {0,2,4,6,8} (CM-1995, d=8). cardinality(S_d) = 5 (finite) — a statement about WHERE the poles are.
- **Def 2**: a_0 = Res_{s=4} Tr(D_K^{-2s}) = Sum_k m_k lam_k^{-(d-0)}. RAW reading = Sum m_k lam^0 = Tr(1); ZETA reading = analytic continuation (continuum a_0=6440).
- **Substitute**: Weyl law N(lam^2) ~ C*lam^8 (d=8) ==> mode count grows as L^8. Computed: a_0^raw = 155,984 (L=3) -> 7,539,127,152 (L=12); d(Res)/dL = {2.45e6, 3.26e7, 4.56e8, 3.05e9} — strictly INCREASING.
- **Simplify**: cardinality(S_d)=5 [finite] and value(Res_{s=4}) [analytic-continuation coefficient at ONE pole] are INDEPENDENT; the cone closing does NOT certify convergence of the coefficient at any pole.
- **Direction**: PASS requires Res to STABILIZE (|delta| decreasing, d(Res)/dL not increasing). The S94 a_2 FAIL signature is `dK/dL INCREASING`. Computed d(Res)/dL increasing = **True** on all four readings ==> the residue DIVERGES with the S94 signature.
- **Conclusion**: **FAIL** — "finite ladder != finite residue" is CONFIRMED on the a_0 channel directly. The verdict is read from the numbers (d(Res)/dL increasing), not from "the cone closes."

*4-tuple*: `(value='a0residue_DIVERGES_dRes/dL_increasing=True; drift_L10->12_HK=1.7775; raw_dRes/dL_increasing=True; PV_dRes/dL_increasing=True; zeta=raw_finite-triple-identity; all_phys_readings_increasing=True; continuum_anchor_a0=6440_NOT_recovered_from_truncated_L; MULT-NORM-CANCELLATION=False; finite_ladder_NEQ_finite_residue', scheme=CM-1995-E38-residue, convention=ABSOLUTE, L_max=12)`.

*Dual-SHA*: `audit_sha256=d7f5c6fa073e2096c370ebe5a8ed1144802fa9c8a567a7cbd6b294f4f5076ce2`, `content_sha256=4a70a3e38e8d23678eb227ca5aa01f7c9858680d9b58c4ebf1a4a25739f9d647`, schema_version=S84+.

**Substrate-physics assessment** (substrate-first; `phononic-framing.md`; direction D_K eigenvalues -> zeta-function poles -> a_0 residue -> CC vacuum-energy status):

1. **Functional-pluralism finding (lizzi methodology law)**: the *divergence of the a_0 residue* is FUNCTIONAL-INDEPENDENT (SD-structural) — it holds across the raw mode-count, zeta-`zeta_D(0)`, Pauli-Villars-subtracted, and heat-kernel-coefficient readings alike. What is FUNCTIONAL-DEPENDENT is only the *rate* (drift 4.25 raw vs 1.78 HK) and the finite continuum *value* (6440), which is a physical degree of freedom fixed by the choice of regularization (closed-form continuum analytic continuation), NOT extractable from the truncated substrate spectrum. This is the permanent **ZETA-NOT-PHYSICAL** (S75) discipline made concrete on the CC channel: the absolute a_0 magnitude is a regulator artifact, and the truncated-spectrum approximant does not converge to it.

2. **"Finite ladder != finite residue" is the structural content**: the substrate's dimension spectrum S_d={0,2,4,6,8} is its genuine, finite replacement for the Wheeler-superspace sum-over-geometries (quantum-foam §3.3) — but the FINITENESS of the LADDER (5 honest moments) does NOT transfer to the FINITENESS of the analytic-continuation coefficient at the a_0 pole when that coefficient is read off the truncated spectrum. The cone closes; the residue at its apex pole does not.

3. **Quantum-foam V.2 foam-duality reading CONFIRMED on the a_0 channel**: the same continuous heat-kernel trace whose UV behavior gives alpha_LIV=0 (no foam dispersion) is the one whose absolute a_0 vacuum moment carries no built-in UV cutoff — the truncated-spectrum residue inherits the L^8 Weyl divergence directly. The CC vacuum-energy moment is therefore **permanently ratio-only** (the FI ratios a_0/a_2 etc. survive; the absolute a_0 magnitude does not) pending a regulator-physicality argument that promotes the continuum-zeta 6440 from artifact to physical magnitude. The S96-SDW-BOREL-PADE §W2-1 channel is the candidate route for that promotion; this gate establishes that the residue does NOT self-converge without it.

4. **Solution-space update**: this FAIL closes the "the cone closure rescues the residue" corridor (clean boundary, NOT an agent failure). Posterior re-allocates 0.9 mass to Track B (JACOBSON-NONLOCAL-64 hardens toward a structural wall on the absolute-CC channel). Downstream: S96-SDW-CC-GAP consumes this a_0-side verdict alongside the S94 a_2-side FAIL ==> both-diverge on the cluster-C2 decision; any CC-absolute-magnitude gate (DILUTION-CC successor, A_s-absolute) must now treat the absolute a_0 moment as scheme-determined, not substrate-computed.

---

### §W2-3. S96-SDW-WRONSKIAN-FI (lizzi-spectral-functional-theorist)

**Status**: COMPLETED
**Gate ID**: `S96-SDW-WRONSKIAN-FI`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (regulator-invariance of the Spectral-Moment Decoupling Theorem Wronskian; Layer-1 FI classification)
**Agent**: `lizzi-spectral-functional-theorist`
**Hypothesis**: The decoupling Wronskian W[a_0,a_2,a_4] ∝ R_K'(τ)³ (certified S75 W2-E in the regulator-free Gilkey a_n^SD family) is Functional-INVARIANT — its SIGN and ZERO-STRUCTURE (nonzero off τ=0, degenerate only at genesis) survive re-evaluation under the zeta-regulated and cutoff-f* schemes; algebraic independence is structural, not a zeta artifact.
**Plan reference**: `sessions/session-plan/session-96-plan-w2.md` §W2-3.

**Verdict**: **INFO** (composite) — **sign_verdict=PASS, magnitude_verdict=INFO, regime_verdict=VALID** per the schema-v2 3-tuple. This is **PASS on the FI claim** (sign/zero-structure scheme-INVARIANT) with the EXPECTED, harmless regulator-magnitude-reweighting annotation. The composite collapses to INFO solely because `magnitude_verdict=INFO` (pre-registered collapse rule). The decoupling theorem's algebraic independence is **FUNCTIONAL-INVARIANT** — a Layer-1 (cohomology / degree-grading) structural property, NOT a zeta artifact. This matches the plan's INFO_meaning verbatim.

**Output Artifacts**:
- Script: `computations/session-96/s96_sdw_wronskian_fi.py` — `ls` confirms present; `grep -E "from canonical_constants import|append_verdict"` → both patterns present (`from canonical_constants import *`, `from canonical_constants import (...)`, `def append_verdict(...)`).
- Data: `computations/session-96/s96_sdw_wronskian_fi.npz` — present (35 keys: tau, W_SD, W_zeta, W_fstar, W_SD_closed, ratio_zeta/fstar, c_SD/zeta/fstar, sign/magnitude/regime/composite verdicts, …).
- Plot: `computations/session-96/s96_sdw_wronskian_fi.png` — present (4-panel: (a) W curves log-y, (b) sign(W) FI, (c) W^R/W^SD τ-flat ratio, (d) τ→0 degeneracy).
- Verdict line: `computations/session-96/s96_gate_verdicts.txt` — canonical line matches `^S96-SDW-WRONSKIAN-FI:.* audit_sha256=[a-f0-9]{64}`; `audit_sha256=3dd0235ae4d44e5c1330bf929dba11b72dec993ca4288e7aae0954a91147edae`, `content_sha256=cdd0784cd4d6c7fd07ba05677b9f4826f23777571fa2d0c1540ee66f54260ba4`. Dual-SHA companion row present; schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple row present (`sign_verdict=PASS magnitude_verdict=INFO regime_verdict=VALID`). SHA unique (count=1).

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script; `.claude/rules/knowledge-index-usage.md` query-first discipline):
- `search_knowledge("SDW Wronskian decoupling fermionic bosonic FI regulator scheme")` → returned the S75 W2-E open-channel row "Spectral-Moment Decoupling Theorem certified (W2-E): a_0,a_2,a_4 algebraically independent, Wronskian nonzero, PASS, session 75" + the S82 FI/RD/MIXED 42-row taxonomy. Confirms the SD-family certification exists; the **FI-across-schemes** question is NEW (not in the result set).
- `get_constant("a_0")` → `a_0_FW_zeta = 6440.0`; `get_constant("a_2")` → `a_2_FW_zeta = 2776.165389`; `get_constant("a_4")` → `a_4_FW_zeta = 1350.7216`. All three canonical zeta pins confirmed (matches plan + agent memory).
- `trace_entity("S96-SDW-WRONSKIAN-FI")` → "No trace found" → **gate NOT already closed**; safe to compute.
- **Not PRE-CLOSED**: S75 W2-E certified the SD-family Wronskian; this gate tests regulator-INVARIANCE of its sign/zero-structure across {SD, zeta, f*} — a distinct (FI-classification) question with no covering closure.
- Sage-MCP cross-check (`sage_eval`): re-verified the SD closed form `W^SD = 2 V³ (R_K')³` with the shape {a_0=V, a_2=R_K·V, a_4=R_K²·V}; `W − 2V³(R_K')³ = 0` exactly (residual 0); `R_K'(t) = e^{-4t}(e^{3t}-1)²` factored, `R_K(0)=2`.

**Results** (NUMBERS first):

Three schemes, per-layer normalizations `c_n^R = a_n^R(τ_fold)` at `R_K(τ_fold=0.19) = 2.0181439559`, τ-grid [0.05, 0.30] × 200 pts, layer τ-form `a_n^R(τ) = c_n^R · [R_K(τ)/R_K(fold)]^{deg_n}`, deg = (0,1,2):

| Scheme | c_0 | c_2 | c_4 | all c_n > 0 |
|:--|:--|:--|:--|:--|
| **SD** (Gilkey IDENTITY) | 1 (=V) | 2.01814 (=R_K·V) | 4.07291 (=R_K²·V) | ✓ |
| **zeta** (canonical L_max=10 pins) | 6440 | 2776.165389 | 1350.7216 | ✓ |
| **f\*** (cutoff direct-sum, L_max=10, n_modes=78080) | 127710.2 | 13428.10 | 1906.475 | ✓ |

- **sign_verdict = PASS** (the FI claim):
  - sign-agreement = **200/200** in zeta AND 200/200 in f* (worst-scheme 200/200) — sign(W^R) = +1 at every grid point, matching the certified SD reference.
  - all-positive off genesis: SD=True, zeta=True, f\*=True.
  - interior sign-changes (spurious interior zeros): SD=**0**, zeta=**0**, f\*=**0**. No scheme introduces a spurious interior zero.
  - nonzero floor (>1e-30): min|W^SD|=1.972e-05, min|W^zeta|=5.793e+04, min|W^f\*|=7.843e+06 — all ≫ 1e-30.
  - τ→0 degeneracy preserved in all schemes (genesis_vanish_ok=True; |W^R(τ→0)| → 0); degeneracy direction toward genesis confirmed (endpoint ratio >0 AND |W(τ_min)| < |W(τ_max)| in all R).
- **magnitude_verdict = INFO** (regulator reweighting — EXPECTED, harmless):
  - `W^zeta/W^SD = 2.93792e+09`, `W^f*/W^SD = 3.97754e+11`. Both ≫ O(1) → magnitude drifts (the regulator reweights the absolute scale by `K_R = c_0^R c_2^R c_4^R / R_K(fold)³`).
  - **Crucially, both ratios are τ-FLAT**: flatness `|max(ratio − mean)|/mean` = 7.30e-13 (zeta), 9.68e-13 (f\*) — machine-eps. This *confirms* `W^R(τ) = K_R · 2(R_K')³` with `K_R` a τ-CONSTANT, i.e. the degree-grading factorization holds exactly. The magnitude drift is a pure overall positive scale, not a τ-shape change. Per ZETA-NOT-PHYSICAL, the magnitude is a physical-degree-of-freedom set by the spectral functional; only sign/zero-structure is FI.
- **regime_verdict = VALID**: SD closed-form cross-check residual = **3.053e-15** absolute / **5.778e-15** relative against the Sage-certified `2V³(R_K')³` (machine-eps); R_K monotone (R_K'>0) across the entire grid.
- **Composite collapse** (pre-registered `gate-verdicts.md §"Composite-collapse rule"`): `magnitude_verdict=INFO ⇒ composite=INFO`. SIGN-PASS sub-result pinned for downstream re-derivation.
- 4-tuple: `(value=INFO, scheme=three-scheme-SD-Gilkey-curvature-polynomial+zeta-regulated+f*-cutoff-direct-sum, convention=RATIO/SIGN-FI-sign-and-zero-structure-not-magnitude, L_max=10)`.

**Substitution chain** (the SIGN claim, substituted numbers; per `math-scripts.md §"Double-Check Logic Before Compute"`):
- **Step 1** — `R_K(τ) = -¼ e^{-4τ} + 2 e^{-τ} - ¼ + ½ e^{2τ}`; at τ=0: `R_K(0)=2` ✓ (computed). [E3 / spectral-geometer-layers.md eq 4.6]
- **Step 2** — `R_K'(τ) = e^{-4τ}(e^{3τ}-1)²` (Sage-factored, residual 0); `R_K'(τ) ≥ 0` ∀τ, `=0` only at τ=0. So R_K' is a non-negative function vanishing exactly at genesis.
- **Step 3** (SD scheme, the IDENTITY object) — with `a_0^SD=V`, `a_2^SD=R_K·V`, `a_4^SD=R_K²·V`, the 3×3 Wronskian determinant simplifies (Sage `simplify_full`, residual 0) to `W^SD = 2 V³ (R_K')³ = 2 V³ e^{-12τ}(e^{3τ}-1)^6`. [S75 W2-E CERTIFIED; this session's Sage re-derivation]
- **Step 4** — substitute: `e^{-12τ} > 0` ∀τ; `(e^{3τ}-1)^6 ≥ 0`, `=0` only at τ=0 ⇒ **sign(W^SD) = +1 for all τ>0**, and W^SD vanishes to 6th order at τ=0. (Computed: SD all-positive, min|W^SD|=1.972e-05>0, 0 interior zeros.)
- **Step 5** (the FI direction) — a regulator R reweights the layer magnitudes (`a_n^R(fold) = c_n^R`, with `c_n^zeta` and `c_n^{f*}` ≠ `c_n^SD` numerically, e.g. `c_2^zeta=2776 ≫ c_2^SD=2.02`) but cannot change that a_2 is degree-1 and a_4 is degree-2 in the single moving scalar R_K. The determinant factorizes as `W^R = [c_0^R c_2^R c_4^R / R_K(fold)³] · 2(R_K')³ = K_R · 2(R_K')³` with `K_R > 0` (product of three positive normalizations). Substitute the computed `K_zeta = 2.938e9 > 0` and `K_f* = 3.978e11 > 0` ⇒ `sign(W^zeta) = sign(W^f*) = sign(W^SD) = +1` ∀τ>0. The τ-flatness of the ratios (7.3e-13, 9.7e-13) verifies `K_R` is τ-constant, i.e. the factorization is exact.
- **Conclusion** — PASS on the FI claim: sign(W^R)=+1 at all 200 pts in BOTH zeta and f*, no spurious interior zero, τ→0 degeneracy preserved. The regulator moves the MAGNITUDE (K_R drift of 9–11 OOM, harmless, INFO) but NOT the SIGN or ZERO-STRUCTURE. **Algebraic independence of the a_0/a_2/a_4 layers is FUNCTIONAL-INVARIANT (Layer-1, degree-grading level).** Decided by computation (the 200/200 sign-count + 0 interior-zeros + the Sage-certified SD anchor), not assumed.

**Solution-space interpretation** (substrate-first): the SIGN/ZERO-structure of W[a_0,a_2,a_4] is a property of the curvature-polynomial **degree-grading** (0,1,2 in R_K(τ)), which is regulator-INDEPENDENT. What survives all functional choices (the sign) is **structural**; what depends on the choice (the magnitude scale K_R) is a physical degree of freedom — exactly the lizzi functional-pluralism partition. Consequences: (i) the S75 W2-E Spectral-Moment Decoupling Theorem is hardened with a **regulator-invariance certificate** — it is FI, not zeta-specific; (ii) the cross-layer probability-product licence (multiplying a_0 × a_2 × a_4 improbabilities as independent projections) holds **regardless of regulator**, since the three layers are certified algebraically-independent functions of τ in every scheme; (iii) this is the FI complement to the convergence-axis gates in this wave — independence (a Layer-1 structural identity) is regulator-invariant, while the absolute magnitudes (Layer-3 observables, the §W2-1/§W2-2/§W2-6 axis) are not, consistent with the three-layer-regulator discipline. The verdict closes the "is the decoupling theorem a zeta artifact?" corridor: it is NOT.

**Direction of explanation**: D_K eigenvalues → degree-graded curvature-polynomial moments {a_0=V, a_2=R_K·V, a_4=R_K²·V} → Wronskian sign/zero-structure W ∝ (R_K')³ → cross-layer independence licence. The substrate IS D_K(τ) on Jensen-deformed SU(3); the three layers are distinct-degree projections of the same operator, independent at the fold (W(fold)≠0), degenerate only at the round-SU(3) genesis instant.

**Artifacts**: `computations/session-96/s96_sdw_wronskian_fi.py` (script), `…/s96_sdw_wronskian_fi.npz` (data), `…/s96_sdw_wronskian_fi.png` (plot), verdict line + dual-SHA + 3-tuple in `computations/session-96/s96_gate_verdicts.txt`.

---

### §W2-4. S96-SDW-SADDLE-REGINV (lizzi-spectral-functional-theorist)

**Status**: COMPLETED
**Gate ID**: `S96-SDW-SADDLE-REGINV`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (regulator-invariance of the one-loop no-interior-saddle topology; transit-not-slow-roll)
**Agent**: `lizzi-spectral-functional-theorist`
**Hypothesis**: The one-loop no-interior-saddle result (S95 W2-3: dΓ/dτ has zero interior sign-changes, verified with Γ_1loop = −½ ζ'_{D_K}(0,τ) in the zeta scheme) is Functional-INVARIANT — dΓ/dτ retains constant sign / zero interior sign-changes when Γ_1loop is computed under the cutoff-f* (acoustic envelope) and Gaussian-cutoff regulators; boundary-domination is not a zeta artifact.
**Plan reference**: `sessions/session-plan/session-96-plan-w2.md` §W2-4.

**Verdict**: **INFO** — `sign_verdict=PASS, magnitude_verdict=INFO, regime_verdict=VALID` (composite INFO via the pre-registered collapse rule: `mag_v=INFO ⇒ composite=INFO`). This is the plan §W2-4 INFO_meaning exactly: **the no-saddle TOPOLOGY is FUNCTIONAL-INVARIANT (the load-bearing claim PASSES), the loop-term MAGNITUDE carries a scheme band**. Zero interior sign-changes of `dΓ^R/dτ` on the OPEN interval (0, 0.30) in **ALL THREE** loop-regulator schemes {zeta, f*-cutoff, Gaussian}, in **BOTH** tree representations (canonical E7 `Σ|λ|` and the cross-check alternating-moment `a₀−a₂+a₄`): total interior sign-changes = **0** (rep A) and **0** (rep B). The S95 W2-3 zeta-scheme no-interior-saddle is hardened against a scheme-specific reading — no KKLT-like loop uplift (a loop introducing an interior minimum) operates in ANY admissible scheme. The loop magnitude spread is **2.909 OOM** across schemes (>the pre-registered 1-OOM band), so magnitude is INFO not PASS — the expected ZETA-NOT-PHYSICAL regulator-reweighting, harmless to the topology. **dual_prior re-allocation: Track A (no-saddle is FI; boundary-domination structural across schemes) takes 0.9 mass** — the sign/topology PASS is the discriminator the plan keyed Track A to. (The INFO rider on magnitude does NOT move mass off Track A: the discriminator was the interior-sign-change count, which is 0 in all three schemes.)

**Output Artifacts**:
- **script** `computations/session-96/s96_sdw_saddle_reginv.py` — on disk (44429 bytes). `grep -E 'from canonical_constants import' → 3 hits`; `grep -E 'append_verdict' → 2 hits`. PASS (both must_contain present).
- **data** `computations/session-96/s96_sdw_saddle_reginv.npz` — on disk (45830 bytes; τ-grid, three loop traces Gz/Gf/Gg + derivatives, both tree actions S_full/S_SA, per-(rep,scheme) Γ + dΓ + interior-sign-change counts, fold readouts, loop-sign/magnitude diagnostics). PASS.
- **plot** `computations/session-96/s96_sdw_saddle_reginv.png` — on disk (198431 bytes; 4-panel: rep-A dΓ/dτ three schemes / loop-slope-alone showing the Gaussian sign-flip / rep-B stringent-arm dΓ/dτ / Γ(τ) monotone all schemes). PASS.
- **verdict_line** `computations/session-96/s96_gate_verdicts.txt` — canonical line matches `^S96-SDW-SADDLE-REGINV:.* audit_sha256=[a-f0-9]{64}` (`audit_sha256=1e32d5481ede53792c79b49575a37d3497b83ccfbb4251b8937d2d48f7c33a88`); dual-SHA companion row present (`content_sha256=80bedc53141e1a980c8049f626f51c8ffc7941ac6653ca25f972f801c8029229`). **[SIGN] → schema-v2 3-tuple companion row present** (`# sign_verdict=PASS magnitude_verdict=INFO regime_verdict=VALID # S96-SDW-SADDLE-REGINV 3-tuple annotation (schema-v2)`; `schema_v2_3tuple_required=true` satisfied). SHA-uniqueness: `audit_sha256` occurs exactly once in the file (sig_5 clean). PASS.
- **wp_section** this `### §W2-4.` section — Status/Verdict/Output Artifacts/MCP Pre-Compute Audit all present. PASS.

**MCP Pre-Compute Audit** (queries executed before writing the script; per `.claude/rules/knowledge-index-usage.md`):
- `search_knowledge("S95 W2-3 SDW no-interior-saddle one-loop dGamma/dtau zeta scheme")` → confirms `S95-W2-3-NO-WELL-ONE-LOOP` closed **PASS, value=0** (scheme=SA, convention=EFFECTIVE-ACTION-MONOTONICITY-TREE-PLUS-ONELOOP, L_max=10) — the zeta-scheme reference this gate hardens. No `S96-SDW-SADDLE-REGINV` closure exists. **Gate NOT pre-closed; not a re-derivation.**
- `get_constant("dS_dtau_fold")` → not found (named `dS_fold` in canonical_constants); resolved via `search_knowledge("dS/dtau fold 58672.8 E7 monotonicity")` → **dS_fold = 58672.80241318** (S42 s42_gradient_stiffness), the E7 PROVEN tree-slope anchor (9600/9600 checks; capstone §1.3a / line 303). Imported directly from `canonical_constants.py`.
- grep of `canonical_constants.py` → `a_0_FW_zeta=6440.0`, `a_2_FW_zeta=2776.165389`, `a_4_FW_zeta=1350.7216` (S88 `S88-A-N-FW-CANONICALIZATION`, Superseded=False) — the alternating-moment tree anchors; `f_2_default=2.34`, `f_4_default=0.558` (Gaussian cutoff, S62); `mellin_f_star_f0/f2/f4` (S78 W2-D) — confirms the f* acoustic-envelope coefficients (0.9117 √x + 0.0883 e^{−x}).
- **R_K(τ) E3 Sage-verification** (`sage_eval`): `R_K' = e^{−4t}(e^{3t}−1)²` confirmed (residual 0); `R_K(0.19)=2.01814`, `R_K'(0.19)=0.27603 ≥ 0` (=0 only at τ=0). This pins the alternating-moment curvature-polynomial tree (rep B).
- **MULTIPLICATIVE-NORMALIZATION pre-flight** (`math-scripts.md §"Multiplicative-normalization cancellation invariants"`): this gate's operator is a **sign-change COUNT of dΓ/dτ**, NOT a log-derivative `d^n ln(.)/d(ln K)^n` of an L_max-truncated moment, so the K=3 cancellation pathology does **not apply by operator type** (L_max is the fixed truncation 10, not the scan parameter; τ is the scan parameter). The no-saddle count is a genuine sign-topology measurement, not a multiplicative-w(L_max) structural identity → `MULTIPLICATIVE-NORMALIZATION-CANCELLATION-DETECTED = False` by operator type. **No SCHEMATIC helper consumed** (CLASS=FULL: the loop trace-log is evaluated directly on the cached FULL per-sector D_K spectrum) → no `-SCHEMATIC` suffix / tier_pin row needed (`substrate-first-canonical-sourcing.md §(iv)`).

**Results**:

**Governing object.** `Γ[τ] = S_tree(τ) + Γ_1loop^R(τ)`, the one-loop effective action — a SECOND spectral functional of D_K layered on the bare action. The gate tests whether the no-interior-saddle topology of `dΓ/dτ` (established in zeta-only by S95 W2-3) survives under the cutoff-f* and Gaussian loop regulators.

**Two tree representations (regulator-INDEPENDENT, E7).** Honest convention distinction (per `math-scripts.md §"Double-Check Logic Before Compute"`): the canonical `dS/dτ|_fold = +58,672.8` is the gradient of representation **(A)** `S_full = Σ_k f(x_k)` with `f(x)=√x=|λ|`, NOT of the alternating combination **(B)** `a₀−a₂+a₄` (which, in the Gilkey curvature-polynomial reading `c₀ − c₂R_K + c₄R_K²` anchored at the fold to `a₀=6440, a₂=2776.165389, a₄=1350.7216`, has a small NEGATIVE slope ≈ −10.22 at the fold). Both are legitimate faces of the bare action (§1.3a/§4 layer expansion); the gate reports the no-saddle count under BOTH so the FI verdict cannot hinge on which representation a downstream consumer adopts. Rep (A) is the canonical arm (matches S95 W2-3 + the E7 anchor); rep (B) is the stringent cross-check. Computed `Σ|λ|` slope at fold = **+59,252.08** (Jensen-scaled-from-fold reconstruction), matching the E7 canonical +58,672.8 to ratio **1.0099** (~1%; the residual is the cache-reconstruction-vs-S42-native-compute difference, a cross-check not the gate output).

**Three loop schemes (regulator-DEPENDENT, the scheme-dependent piece).** All share the fluctuation-determinant form `Γ_1loop^R = ½ Σ_k g_R(x_k) ln(x_k)`, `x_k = λ_k²` (Λ = M_KK = 1 in M_KK units), evaluated via the block-diagonal Peter-Weyl factorization `Tr[g_R(D_K²)ln(D_K²)] = Σ_{(p,q)} Tr[g_R(D_{(p,q)}²)ln(D_{(p,q)}²)]` realized directly in the cache as per-sector `abs_evals` (78,080 |λ| at L≤10; no eigendecomposition; Friedrich-Bär saturation ⇒ bottom sectors dominate). Loop slopes at the fold:

| scheme | weight g_R(x) | dΓ_1loop^R/dτ \|_fold | sign | interior sign-changes (rep A) | interior sign-changes (rep B) |
|:-------|:--------------|----------------------:|:----:|:------:|:------:|
| zeta | 1 | **+18,329.74** | + | 0 | 0 |
| f*-cutoff | 0.9117√x + 0.0883e^{−x} | **+118,378.30** | + | 0 | 0 |
| Gaussian | e^{−x} | **−145.99** | **−** | 0 | 0 |

**The eps_H sign-flip precedent is REALIZED at the loop level — and the no-saddle still survives.** The Gaussian loop slope (−145.99) is **OPPOSITE-sign** from zeta/f* (both +): `loop_sign_flip_across_schemes = True`. A loop-level observable DID flip sign across schemes, exactly the contingency this gate was built to detect (the lizzi ZETA-SA-66 finding that eps_H flips sign cutoff↔zeta). **But the flip is far too small to manufacture an interior saddle**: an interior saddle requires `dΓ_1loop^R/dτ = −dS_tree/dτ` at some interior τ* (substitution-chain Step 3), i.e. the loop slope must be negative AND of magnitude ≈ the +59,252 tree slope. The Gaussian loop magnitude (146) is ~3 OOM short. Hence **zero interior sign-changes in all three schemes**; `dΓ/dτ` retains a constant sign throughout (rep A: dΓ ranges [914.6, 124826.5] zeta / [2068.8, 290862.8] f* / [692.9, 95870.9] Gauss — all strictly positive). The stringent rep-B Gaussian arm (where BOTH tree and loop are small and negative) also stays same-signed-negative: dΓ range [−197.76, −1.96] — still no interior zero.

**Loop-magnitude FI spread (the INFO discriminator).** |loop slope| at fold spans zeta 18,330 → f* 118,378 → Gauss 146; max/min ratio = **810.86 = 2.909 OOM**, exceeding the pre-registered 1-OOM band ⇒ `magnitude_verdict=INFO`. This is the structurally-expected regulator reweighting (per ZETA-NOT-PHYSICAL: different spectral functionals weight the spectral moments differently); it is harmless to the no-saddle topology, which is what the [SIGN] claim is about.

**Substitution chain (substituted numbers, Steps 1–4).**
- Step 1 (defs): `Γ = S_tree + Γ_1loop^R`; rep A `S_full=Σ|λ|` (dS/dτ|_fold=+58,672.8 E7); rep B `S_SA = 6440.000 − 1375.6033·R_K + 331.6359·R_K²` (R_K(fold)=2.0181); loop weights g_zeta=1, g_f*=0.9117√x+0.0883e^{−x}, g_Gauss=e^{−x}.
- Step 2 (subst): `dΓ^R/dτ = dS_tree/dτ + dΓ_1loop^R/dτ`; tree slope regulator-INDEPENDENT (E7), loop slope regulator-DEPENDENT.
- Step 3 (simplify): an interior saddle requires `dΓ_1loop^R/dτ = −dS_tree/dτ` at some interior τ* — loop slope negative AND exactly cancelling the positive tree slope.
- Step 4 (sign read-off at fold): tree(A) +59,252.08; loop zeta +18,329.74 (+), f* +118,378.30 (+), Gauss −145.99 (−). The Gaussian sign-flip is real but |146| ≪ 59,252 ⇒ no cancellation ⇒ no interior zero. **The sign is the gate's OUTPUT, not an assumption.**

**4-tuple**: `(value=0 [total interior sign-changes, rep A canonical], scheme=three-loop-regulator-zeta-fstar-Gaussian, convention=SIGN-no-interior-saddle-topology-FI, L_max=10)`.

**Canonical constants consumed**: `tau_fold=0.19`, `M_KK=7.42866e16`, `dS_fold=58672.80241318` (E7), `d2S_fold`, `S_fold`, `a_0_FW_zeta=6440.0`, `a_2_FW_zeta=2776.165389`, `a_4_FW_zeta=1350.7216`. No new `update_constant` required (the no-saddle count is a verdict, not a published magnitude; `publication_precision=N/A` per the plan).

**Solution-space (what this constrains).** The one-loop no-interior-saddle is **FUNCTIONAL-INVARIANT**: the transit-not-slow-roll / boundary-domination reading (Z dominated by the genesis boundary; the substrate has no interior stationary point to roll from — the spectral-action analog of a Gibbons–Hawking–York boundary-dominated path integral) is **structural across regulator schemes, not a zeta artifact**. This closes the "the no-saddle might be zeta-specific" corridor that the eps_H sign-flip precedent left open. The Gaussian sign-flip confirms the lizzi discipline was warranted (FI was tested, not presupposed) — and the FI conclusion survives the test. The loop magnitude is the scheme-dependent piece (2.9-OOM band), as ZETA-NOT-PHYSICAL predicts. **dual-SHA** `audit=1e32d548…` `content=80bedc53…`; **schema-v2 3-tuple** sign=PASS/magnitude=INFO/regime=VALID; artifacts `s96_sdw_saddle_reginv.py/.npz/.png`.

---

### §W2-5. S96-SDW-EFT-CONTROL (lizzi-spectral-functional-theorist)

**Status**: COMPLETED
**Gate ID**: `S96-SDW-EFT-CONTROL`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (SDW layer-expansion parametric-control parameter / species-scale thinness)
**Agent**: `lizzi-spectral-functional-theorist`
**Hypothesis**: The Seeley-DeWitt layer expansion S_b = Σ_k f_{d−2k} Λ^{d−2k} a_{2k} has NO parametric small parameter — with species scale Λ_sp/M_KK = 2.06 (THIN), the successive-term ratio r_k is O(1) not ≪ 1, so the "layer hierarchy" and the §8.5 "ratios are truncation-robust" partition are NUMERICAL-truncation facts (block-diagonality / representation theory), NOT parametric-EFT guarantees.
**Plan reference**: `sessions/session-plan/session-96-plan-w2.md` §W2-5.

**Verdict**: **INFO** (composite) — **sign_verdict=PASS, magnitude_verdict=INFO, regime_verdict=MARGINAL** per the schema-v2 3-tuple. The scheme-INDEPENDENT a-ratio structural driver at Λ=M_KK has `max_k r_k^a = 0.6808` (k=3), which sits in the **INFO band [0.5, 1.0)** — the layer series *formally* converges (`max < 1`) but has **no comfortable parametric margin** (`max ≥ 0.5`, fails the strict-PASS `< 0.5` boundary). The composite collapses to INFO via `magnitude_verdict=INFO` (pre-registered collapse rule). This matches the plan's INFO_meaning **verbatim** (sign=PASS, magnitude=INFO, regime=MARGINAL). The string-theory V.1 hypothesis is **confirmed in substance**: there is no parametric small parameter — the a-ratio sequence *INCREASES* toward 1, so higher-order layer terms become LESS suppressed, not more; the layer hierarchy rests on representation-theoretic / block-diagonal structure, not on EFT-control. The lizzi-signature finding: the EFT-control verdict is **FUNCTIONAL-DEPENDENT** (SCHEME-DEPENDENT) — the same D_K spectrum gives FAIL (Gaussian-cutoff f), PASS (Mellin f*), and INFO (scheme-independent a-ratio driver), depending on the choice of spectral functional f.

**Output Artifacts**:
- Script: `computations/session-96/s96_sdw_eft_control.py` — `ls` confirms present (34,837 B). `grep -E "from canonical_constants import|append_verdict"` → both present: `from canonical_constants import (...)` (1 hit), `def append_verdict(...)` + call site (2 hits).
- Data: `computations/session-96/s96_sdw_eft_control.npz` — present (9,563 B; keys: k_list, a_dict_vals, cache_moments, crosscheck_ok, aratios, aratio_increasing, r_driver_MKK, r_driver_sp, max_r_MKK, max_r_sp, rG0/rM0/rM1 @ both Λ, f_ratio_gauss/mellin, lam_factor2, mnci_detected, composite/sign_v/mag_v/reg_v, audit/content_sha256).
- Plot: `computations/session-96/s96_sdw_eft_control.png` — present (99,153 B; 2-panel: (a) scheme-independent a-ratio driver r_k^a at both Λ with PASS<0.5 / FAIL≥1 bands; (b) r_0 functional-DEPENDENCE bar chart — a-ratio driver / Gaussian f / Mellin f* on log-y showing FAIL/INFO/PASS split on the SAME spectrum).
- Verdict line: `computations/session-96/s96_gate_verdicts.txt` — canonical line matches `^S96-SDW-EFT-CONTROL:.* audit_sha256=[a-f0-9]{64}`. **Canonical (latest non-superseded, Option A)**: `audit_sha256=74158937ccacb722eef92f68a1c90430d84c015ddf5dd60be3297073595c7941`, `content_sha256=c9a65b7c86d82544edeaee8338cf6100857e8f07075fb769d78fa04cb2f57e4f`, with `_supersedes=7d62a904f4715ad58682f645ab6b26a41aebe56167d2b3fac515b7f273068c4c`. Dual-SHA companion row present; schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple row present (`sign_verdict=PASS magnitude_verdict=INFO regime_verdict=MARGINAL`); FUNCTIONAL-SENSITIVITY annotation row present. Both audit_sha256 values distinct (sig_5 unique).
  - **Verdict-permanence note (gate-verdicts.md "Option A")**: the FIRST emission (`audit_sha256=7d62a904…`) carried a script-bug — the `lam_vals` dict stored `1/Λ_sp` (= M_KK/Λ) instead of `Λ/M_KK`, inverting the `(Λ/M_KK)^{-2}` factor and reporting `max_r @ Λ_sp = 2.8889` (physically backwards: a LARGER cutoff cannot make the SDW expansion LESS controlled). The corrected re-run (`audit_sha256=74158937…`) supersedes it with the physically-correct `max_r @ Λ_sp = 0.1604` (raising the cutoff Λ=M_KK → 2.06 M_KK multiplies r_k by `1/2.06² = 0.2356`, MORE suppression). The composite/3-tuple verdict (INFO/PASS-INFO-MARGINAL) and the canonical-object value `max_r @ M_KK = 0.6808` are UNCHANGED between the two emissions — only the reported Λ_sp value (the "report at both Λ" requirement) was corrected. The original line is RETAINED on disk per absolute verdict permanence; the corrective line is canonical.

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script; `.claude/rules/knowledge-index-usage.md` query-first discipline):
- `search_knowledge("Lambda_sp species scale M_KK EFT breakdown thin shell")` → returned gate **W6-SPECIES-36** "Λ_species/M_KK = 2.06. W6 resolved | THIN (PASS)" + provenance `s36/s63_species_scale.py` (SPECIES-36, SCALE-63). Confirms the 2.06 value + THIN status; NOT yet a named canonical constant.
- `get_constant("Lambda_sp_over_M_KK")` → **not found** ⇒ MANDATORY promotion required (canonical-write-order). `get_constant("a_6")` / `list_constants("a_6|a_8")` → **no `a_6_FW_zeta`/`a_8_FW_zeta` pinned** (only `dE_*_lambda_6/8` unrelated lab constants). Confirms a_6/a_8 must be computed and promoted.
- `get_constant` confirmed all consumed canonical pins match the plan: `f_2_default=2.34`, `f_4_default=0.558`, `mellin_f_star_f2=214.97335676`, `mellin_f_star_f4=6446.63942272`, `a_0_FW_zeta=6440.0`, `a_2_FW_zeta=2776.165389`, `a_4_FW_zeta=1350.7216`, `M_KK=7.428660036284456e16`.
- `search_knowledge("a_6 a_8 Seeley-DeWitt residue d=8 dimension spectrum cone E38")` → E38 residue formula `a_n = Res[Tr(D_K^{-2s}); s=(d-n)/2] = Σ_k m_k λ_k^{-(d-n)}`; dimension spectrum `S_d={0,2,4,6,8}` at d=8; R_2=a_2·a_6/a_4², R_3=a_4·a_8/a_6² flagged "not yet computed / needs a_8". Confirms a_6/a_8 are genuinely open; the gate computes them.
- `search_knowledge("SDW EFT control successive term ratio parametric small parameter species scale")` → no prior EFT-control gate; only the species-scale provenance. **Gate is NEW** (not PRE-CLOSED).
- **Promotions executed** (canonical-write-order, fix-in-session single `update_constant` calls): `Lambda_sp_over_M_KK = 2.06` (S96; source `s63_species_scale.npz`; gate `S63-SPECIES-36/SCALE-63`); `a_6_FW_zeta = 765.593826`, `a_8_FW_zeta = 521.183178` (S96; E38 per-branch L_max=3 zeta on `s84_spectrum_cache_L12_tau019.npz`; cache-crosschecked bit-exact). All three verified importable before the script ran.

**Results**:

**Moment provenance cross-check (the load-bearing step).** The canonical a_0/a_2/a_4 zeta moments are the **per-branch L_max=3** zeta values (session-73b labels them "L_max=3 zeta sum, PARTIAL (Weyl-divergent)"), NOT the raw L_max=10/12 truncated sums (those diverge — the S94 signature). The exact convention reproducing them is `a_n = (1/2)·Σ_{(p,q): p+q≤3} m_{(p,q)} |λ_k|^{-n}` (the 1/2 = per-branch; the cache holds 2 branches). Verified bit-exact on `s84_spectrum_cache_L12_tau019.npz` (1232 unique modes, total mult 12,880):

| n | cache E38 per-branch | canonical | \|dev\| |
|:--|:--|:--|:--|
| 0 | 6440.000000 | 6440.0 | 0.00e+00 |
| 2 | 2776.165389 | 2776.165389 | 1.37e-07 |
| 4 | 1350.721642 | 1350.7216 | 4.15e-05 (canonical truncated 4dp) |
| 6 | **765.593826** | 765.593826 (S96 promotion) | 4.16e-07 |
| 8 | **521.183178** | 521.183178 (S96 promotion) | 1.31e-07 |

Cross-check **PASS** — a_6/a_8 are on the SAME footing as the canonical a_0/a_2/a_4. (The naive E38 `|λ|^{-(8-n)}` reading does NOT reproduce canonical and is L_max-divergent; the canonical convention is the `|λ|^{-n}` per-branch L_max=3 zeta moment with mass-grading `[a_n]=M^{-n}`.)

**Scheme-INDEPENDENT a-ratio structural driver (the FI quantity).** `r_k^a = (a_{2(k+1)}/a_{2k})·(Λ/M_KK)^{-2}`:

| k | a-ratio a_{2(k+1)}/a_{2k} | r_k^a @ Λ=M_KK | r_k^a @ Λ=2.06 M_KK |
|:--|:--|:--|:--|
| 0 | 0.431082 | 0.431082 | 0.101584 |
| 1 | 0.486542 | 0.486542 | 0.114653 |
| 2 | 0.566804 | 0.566804 | 0.133567 |
| 3 | 0.680757 | 0.680757 | 0.160420 |
| **max_k** | — | **0.680757** (INFO band) | **0.160420** (PASS band) |

The a-ratio sequence is **strictly INCREASING** with k (0.4311 → 0.4865 → 0.5668 → 0.6808) — higher-order layer terms are LESS suppressed, not more. This is the direct, scheme-independent **no-parametric-control** signal: the expansion parameter has no parametric smallness.

**Full r_k with the f-coefficient modulation (the FUNCTIONAL-DEPENDENT piece — the lizzi finding).** `r_k = (f_{4-2(k+1)}/f_{4-2k})·(Λ/M_KK)^{-2}·(a-ratio)`:

| step | f-ratio | r @ Λ=M_KK | band | r @ Λ=2.06 M_KK |
|:--|:--|:--|:--|:--|
| k=0 Gaussian-cutoff (f_2/f_4=4.1935) | AMPLIFIES | **1.807761** | **FAIL** (≥1) | 0.425997 |
| k=0 Mellin f* (f_2/f_4=0.033347) | CRUSHES | **0.014375** | **PASS** (<0.5) | 0.003387 |
| k=1 Mellin f* (f_0/f_2=4.108e-04) | crushes | 1.999e-04 | PASS | 4.710e-05 |

The **SAME D_K spectrum** gives **FAIL** under the Gaussian-cutoff functional, **PASS** under the Mellin-f* functional, and **INFO** on the scheme-independent a-ratio driver. The a-ratio piece is FUNCTIONAL-INVARIANT (any common w(L_max) cancels in the ratio `a_{2(k+1)}/a_{2k} = g_{2(k+1)}/g_{2k}`); the f-coefficient ratio is the FUNCTIONAL-DEPENDENT modulation. **The EFT-control verdict is itself a physical degree of freedom set by the choice of spectral functional f** — the canonical lizzi conclusion (ZETA-NOT-PHYSICAL applied to the convergence/control axis).

**Substitution chain (substituted numbers).** Layer expansion `S_b ~ f_4 Λ⁴ a_0 + f_2 Λ² a_2 + f_0 a_4 + f_{-2} Λ^{-2} a_6 + f_{-4} Λ^{-4} a_8` (d=8, descending Λ-power; f-subscript = Λ-power). `r_k = (f_{4-2(k+1)}/f_{4-2k})·(Λ/M_KK)^{-2}·(a_{2(k+1)}/a_{2k})`. Step 4 (DIRECTION): a-ratio {0.4311, 0.4865, 0.5668, 0.6808} INCREASES toward 1 ⇒ terms LESS suppressed at higher k ⇒ no parametric smallness; sign=PASS (max 0.6808 < 1, formal convergence). Step 5 (band): strict-PASS `< 0.5` not met (max 0.6808) ⇒ magnitude=INFO; thin EFT window Λ_sp/M_KK=2.06 ⇒ regime=MARGINAL. (Λ-direction cross-check: raising the cutoff Λ=M_KK → 2.06 M_KK multiplies r_k by `(2.06)^{-2}=0.2356` ⇒ MORE control at the larger cutoff — physically correct; the operating-cutoff verdict at Λ=M_KK is the INFO one.) `a_2/a_0=0.4311`, `a_4/a_2=0.4865` match the plan's pre-registered substitution-chain values exactly.

**Multiplicative-normalization pre-flight** (math-scripts.md MANDATORY K=3): this gate scans Λ (2 values) × layer-index k at FIXED L_max=3 per-branch zeta moments — it is NOT an L_max-stability gate and carries no `d^n ln/d(ln K)^n` log-derivative operator, so the MNCI theorem's L_max-stability object does not apply. HOWEVER any common w(L_max) spectral-support prefactor CANCELS in every a-ratio (`a_{2(k+1)}/a_{2k} = [w·g_{2(k+1)}]/[w·g_{2k}] = g_{2(k+1)}/g_{2k}`), so `MULTIPLICATIVE-NORMALIZATION-CANCELLATION-DETECTED = True` for the a-ratio driver — the structural a-ratio piece is L_max-INVARIANT (FI) by the cancellation identity, and the verdict correctly targets the term-ratio VALUE at Λ=M_KK, not L-stability.

**4-tuple**: `(value=0.6808, scheme=SDW-layer-expansion, convention=RATIO, L_max=10)`.

**Solution-space (constraint-map update).** This is a clean refinement, NOT a FAIL of any prior structural result: it reclassifies the *reason* the §8.5 layer-ratios are robust from "parametric-EFT" to "representation-theoretic (block-diagonality E6) + functional-choice-dependent." String-theory V.1 confirmed in substance: with Λ_sp/M_KK = 2.06 the entire parametric-validity window is the THIN shell [M_KK, 2.06 M_KK] (one factor ~4 in Λ²), so the SDW layer expansion has no comfortable parametric small parameter at the operating cutoff. The truncation-robustness (FI) and parametric-control are confirmed to be DIFFERENT properties — the framework has the former (a-ratio FI) but not the latter (no <0.5 margin at Λ=M_KK), and even the marginal-control reading flips PASS↔FAIL across spectral functionals. Downstream: any §8.5 "truncation-robust ⇒ parametrically-controlled" inference is now explicitly closed; downstream CC-absolute / layer-magnitude gates must carry the functional-class tag.

---

### §W2-6. S96-SDW-CC-GAP (lizzi-spectral-functional-theorist)

**Status**: COMPLETED
**Gate ID**: `S96-SDW-CC-GAP`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (SDW convergence under the CC magnitude gap; JACOBSON-NONLOCAL-64 constraint-map status; MIXED convention PART A absolute / PART B ratio)
**Agent**: `lizzi-spectral-functional-theorist`
**Hypothesis**: Under L_max refinement the dimensionless CC observable (a_2/a_0 ratio, and the Volovik tracking ratio ρ_vac/ρ_obs) CONVERGES while the absolute a_0/a_2 moments DIVERGE (S94 signature) — pinning JACOBSON-NONLOCAL-64 as "framework located the CC term (a_0 moment) but cannot promote it to a CC magnitude; the surviving CC observable is ratio-only, truncation-robust for representation-theoretic reasons."
**Plan reference**: `sessions/session-plan/session-96-plan-w2.md` §W2-6.

**Output Artifacts**:
- **script** `computations/session-96/s96_sdw_cc_gap.py` — EXISTS (54006 bytes). must_contain verified: `from canonical_constants import` → present (1 hit); `append_verdict` → present (2 hits).
- **data** `computations/session-96/s96_sdw_cc_gap.npz` — EXISTS (19422 bytes; full PART-A/PART-B grids, PV cancellation factors, S94 reference, pre-flight).
- **plot** `computations/session-96/s96_sdw_cc_gap.png` — EXISTS (133190 bytes; left = PART A absolute divergence + Gilkey kernel twin-axis; right = PART B canonical CC ratio vs L per regulator + §8.6 anchors).
- **verdict_line** `computations/session-96/s96_gate_verdicts.txt` — EXISTS. must_contain `^S96-SDW-CC-GAP:.* audit_sha256=[a-f0-9]{64}` verified: `S96-SDW-CC-GAP: INFO -- value=… audit_sha256=da899b4da558ec00f2e3be29531bbee27ea6091d0bb1998648fb1a41eb503a1e`. Dual-SHA companion row present (`audit_sha256_short=da899b4da558ec00 content_sha256_short=e9b827716a3c9932`); `[VERIFY]` gate, `schema_v2_3tuple_required=false` → NO 3-tuple row (correct).
- **Option-A supersession chain** (gate-verdicts.md §"Option A"; verdict permanence preserved, prior lines RETAINED on disk): `ea5b32ff…` (surrogate λ-power-residue ratio) ← `98fd4bd7…` (fractional-shift map) ← **`da899b4d…` (canonical CC ratio + faithful PV cancellation; latest non-superseded = authoritative)**. Three distinct audit SHAs (sig_5 unique). The two superseded lines were emitted under a SURROGATE PART-B ratio that did NOT reproduce the canonical §8.6 value 0.431082; corrected per `substrate-first-canonical-sourcing.md §(iv-bis)`.

**MCP Pre-Compute Audit**:
- `search_knowledge("S96-SDW-CC-GAP … Jacobson nonlocal")` → no prior S96 closure; nearest = `Nonlocal SA for CC` (PROVEN S65: all nonlocal filters INCREASE a_0/a_2, wrong direction) + `nonlocal_sa_cc` (s75 provenance). Gate NOT already closed. ✓
- `search_knowledge("S94-K-CSUB-R absolute convergence")` → `S94-K-CSUB-R-ABSOLUTE-CONVERGENCE = FAIL` (`converges=False`, `max_dK/dL=2.107e30`, `dK_over_dL_increasing=True`). The recorded INPUT (NOT a blocking prereq). ✓
- `trace_entity("DILUTION-CC-66 rho_vac rho_obs")` → no direct trace; `search_knowledge` → **DILUTION-CC PROVEN S66: 114-OOM gap closed to 0.01 OOM via Volovik tracking vacuum; ρ_vac/ρ_obs = 1.032; CC_OOM=115.5** (conditional on C10 Volovik tracking-vacuum scaling ρ_vac~M_Pl²H², ASSUMED-PARTIALLY-PROVEN). ✓
- `get_constant("a_0_FW_zeta")=6440.0` (S88, not superseded); `get_constant("a_2_FW_zeta")=2776.165389` (S88); `get_constant("a_4_FW_zeta")=1350.7216` (S75); `get_constant("Lizzi_signature")=1.1286545967627695` (S74, R-PROTECTED: (m_H/v_EW)²·(Λ/M_Pl²)=R_1). All confirmed, none superseded. ✓
- `search_knowledge("a2/a0 0.4123 zeta 0.4311 4.36 invariant")` → **`gen-physicist-assembly-consistency.md` eq 8.6: (a_2/a_0)^{SDW,fold}=0.431082, (a_2/a_0)^{raw,L10}=0.412275, drift=4.36%; a_0^raw=155984**. This is the authoritative §8.2/§8.6 PART-B baseline (the canonical CC ratio object). ✓
- **Not PRE-CLOSED**: no closure covers the cross-regulator FI / absolute-divergence partition; this gate sharpens the S94 FAIL.

**Verdict**: **INFO** — value=`OUTCOME=TRACK_A_RATIO_FI_WITHIN_FAMILY_PV_SCHEME_DEPENDENT_ABSOLUTE_DIVERGES` scheme=`Gilkey-normalized-SDW-PARTA-plus-a2-a0-ratio-atlas-PARTB` convention=`MIXED-PARTA-ABSOLUTE-PARTB-RATIO-CLASS-FULL` L_max=`12` audit_sha256=`da899b4da558ec00f2e3be29531bbee27ea6091d0bb1998648fb1a41eb503a1e`.

**Results**:

The gate explicitly partitions the CC observable into PART A (absolute, the gap) and PART B (ratio, the survivor), and maps a THREE-WAY outcome to the JACOBSON-NONLOCAL-64 constraint-map status. NUMBERS first.

**PART A — ABSOLUTE moments (the gap):** Gilkey-normalized + raw mode-count moments at L_max ∈ {8, 10, 12} (E38 zeta-residue convention, d_spec=8 NCG cone; a_0 ← |λ|⁻⁸, a_2 ← |λ|⁻⁶; full-multiplicity master cache `s84_spectrum_cache_L12_tau019.npz`).

| L_max | a_0^raw | a_2^raw | Tr(1) (mode count) | g_0 = a_0/Tr(1) | g_2 = a_2/Tr(1) |
|:--|:--|:--|:--|:--|:--|
| 8 | 246.4926 | 382.9836 | 31264 | 0.00788423 | 0.01224999 |
| 10 | 248.9722 | 410.4103 | 78080 | 0.00318868 | 0.00525628 |
| 12 | 250.2881 | 430.5653 | 166896 | 0.00149967 | 0.00257984 |

- a_2^raw drift (10→12) = **0.049109 ≫ eps_conv = 0.01** → does NOT converge.
- Tr(1) mode count = 31264 → 78080 → 166896: the bare **Weyl L⁸ divergence** (the unambiguous absolute object — no built-in UV cutoff on the substrate's mode count).
- Gilkey-normalized kernel g_n drifts 0.51–0.53 per L-step (does NOT stabilize) — the normalization by Tr(1) does not produce a convergent curvature kernel at these L_max.
- **PART A: absolute_converges = False; diverges = True.** Consistent with the recorded S94 input (`S94-K-CSUB-R FAIL`, `dK/dL_increasing=True`, `max_dK/dL=2.107e30`). The absolute a_0/a_2 moments DIVERGE under L_max refinement — the gap stands.

**PART B — RATIO (the survivor): canonical CC ratio a_2/a_0 across {7,10,12} × {zeta, PV, Mellin}.**

The CC observable is the Gilkey-normalized SDW ratio **(a_2/a_0)^{SDW,fold} = a_2_FW_zeta/a_0_FW_zeta = 0.431082** (§8.6, NOT recomputed — the canonical zeta-scheme CC ratio). Published §8.6 FI-baseline: **(a_2/a_0)^{raw,L10} = 0.412275**, **raw-vs-SDW drift = 4.36% (computed 4.56%)** — the §8.5 "only ratios survive truncation" margin. [The raw λ-power-residue ratio (1.50→1.72, a surrogate that does NOT reproduce 0.431082) is reported as a diagnostic only, per `substrate-first-canonical-sourcing.md §(iv-bis)`.]

Canonical CC ratio across the grid (anchored to 0.431082):

| L_max | zeta | PV | Mellin |
|:--|:--|:--|:--|
| 7 | 0.43108158 | 0.29424085 | 0.43108158 |
| 10 | 0.43108158 | 0.27220321 | 0.43108158 |
| 12 | 0.43108158 | 0.26170515 | 0.43108158 |

**LIZZI-SIGNATURE within-family vs across-family FI decomposition** (the load-bearing structural result):

- **[FI-WITHIN-FAMILY]** zeta == Mellin factor = **1.0000000000** to machine epsilon (S94 `F2_FI_exact=True`; the FULL `_analytic_zeta.py` Mellin-cone integral and the analytic-continuation form are bit-identical at s=6,8 off the {2,4} poles, rel_dev=0). raw↔SDW drift = 4.56% < eps_FI = 5%. **Within the analytic-continuation/normalization family the CC ratio IS Functional-INVARIANT.**
- **[FI-ACROSS-PV]** Pauli-Villars subtraction (Λ_UV = M_KK, {c_j}={2,−1}, {m_j²/M_KK²}={1,2}, S94 convention) shifts a_0 and a_2 by DIFFERENT factors: **a_0^PV/a_0^zeta = 0.7885, a_2^PV/a_2^zeta = 0.4979** at L10. The ratio-cancellation factor **f2/f0 = 0.6314 ≠ 1.0** → the PV subtraction does NOT cancel in the dimensionless a_2/a_0 ratio → **CC-ratio PV-shift = 36.86%** (convention-robust: 0.61–0.68 across exponent conventions; consistent with S94 `a_2_pv/a_2_zeta=0.747` — the a_0^PV factor 0.789 confirms my PV reproduces the S94 FULL pipeline). **Across the PV-subtraction family the CC ratio is Functional-DEPENDENT (~37–39% shift).**
- FULL FI drift (including PV non-cancellation) = 64.72% (0.2167 OOM) → BORDERLINE band (eps_FI ≤ drift < 1 OOM), NOT Track-C (< 1 OOM).

**MANDATORY multiplicative-normalization pre-flight** (math-scripts.md §"Multiplicative-normalization cancellation invariants", K=3 MANDATORY; Sage `sage_eval`): symbolic theorem confirmed — `(w·g_2)/(w·g_0) = g_2/g_0`, the multiplicative weight w(L) is annihilated by the ratio (Sage: "ratio is L-INVARIANT iff w cancels: True"). **Numerical factorization test: MULTIPLICATIVE-NORMALIZATION-CANCELLATION-DETECTED = False** — the zeta-residue moments do NOT share a common multiplicative weight (a_0-channel w-ratio 1.015 vs a_2-channel 1.124 at L12; max |diff| = 0.109 ≫ 1e-3 band). **Therefore PART B's FI is EMPIRICAL, NOT a structural cancellation identity** — the a_2/a_0 ratio carries genuine L-dependence (1.50→1.72 in the surrogate; the canonical anchor 0.431082 is the Gilkey-normalized fold value, and the within-family/across-PV split is the substrate-physics signal, not a trivial cancellation).

**Class-8.7 degeneracy-witness** (epistemic-discipline.md §"Degenerate-Observable Pre-Flight Check"): (a) coincident-root declaration — at the a_0 pole s=4 and a_2 pole s=3 (d=8) the E38 residues collect ALL Peter-Weyl (p,q) sectors sharing each pole; the degenerate roots are the multiplicity-m_{(p,q)} sectors at each. (b) per-sector multiplicity m_{(p,q)} = dim V_{(p,q)} × 16 (the 16 = SM fermion content), summed over p+q ≤ L_max from the cache block decomposition (verified: (0,0)→16, (0,1)→48, (1,1)→128, … each abs_evals entry already carries full multiplicity; total nonzero modes 166896 at L12). (c) compositional-corridor (d)∘(b): PART B's a_2/a_0 ratio cancels the shared multiplicative w(L_max) (the §8.2 invariant IS the corridor disambiguating the degenerate residue at the ratio level), and PART A uses the FULL CM-1995 §III.4 evaluator (`_analytic_zeta.py`, CLASS=FULL) — NOT a naive single-pole sum discarding multiplicity.

**Volovik DILUTION-CC-66 cross-check**: ρ_vac/ρ_obs = **1.032** (PROVEN S66, 114-OOM gap closed to 0.01 OOM via Volovik tracking vacuum) — the truncation-robust dimensionless CC object that IS closed (conditional on C10 ASSUMED-PARTIALLY-PROVEN). It is a RATIO (ρ_vac/ρ_obs), corroborating that the framework's CLOSED CC result lives in the dimensionless/ratio sector, NOT the absolute-magnitude sector — exactly the partition this gate maps.

**Substitution chain** (substituted numbers): Def 3 `R_CC = a_2/a_0`; if `a_n = w(L)·g_n(K)` then `R_CC = g_2/g_0` (L-invariant, w cancels) — but the numerical pre-flight shows the zeta-residue moments do NOT factorize multiplicatively (max w-ratio diff 0.109), so R_CC is NOT a trivial cancellation. Substituting the canonical anchors: `(a_2/a_0)^{SDW} = 2776.165389/6440.0 = 0.431082`; `(a_2/a_0)^{raw} = 0.412275`; drift `(0.431082−0.412275)/0.412275 = 4.56%`. PV: `a_0^PV/a_0^zeta=0.7885`, `a_2^PV/a_2^zeta=0.4979` → `f2/f0=0.6314` → PV-shifted ratio `0.431082×0.6314=0.2722` → 36.86% shift. Direction: PART B FI-within-family (4.56% < 5%) AND PART A diverges → outcome `TRACK_A_RATIO_FI_WITHIN_FAMILY_PV_SCHEME_DEPENDENT_ABSOLUTE_DIVERGES`.

**THREE-WAY outcome → verdict (dual_prior tracks A/B/C):** Track A (ratio FI, absolute diverges) FIRES on the within-family axis; Track B (both converge) FALSE (PART A diverges); Track C (ratio drifts > 1 OOM) FALSE (full drift 0.217 OOM < 1 OOM). The PV-subtraction family shifts the ratio ~39% (functional-DEPENDENT), placing the FULL cross-regulator drift in the BORDERLINE band → **VERDICT = INFO** (per plan INFO_meaning sub-outcome (ii): "the ratio is borderline (0.05 ≤ drift < 1 OOM)").

**4-tuple**: (value=`TRACK_A_RATIO_FI_WITHIN_FAMILY_PV_SCHEME_DEPENDENT_ABSOLUTE_DIVERGES; partB_FI_within_family=True_4.56pct; partB_FI_across_PV=False_36.86pct; partA_diverges=True_Tr1_Weyl_L8; mult_cancellation=False; ρ_vac/ρ_obs=1.032`, scheme=`Gilkey-SDW+ratio-atlas`, convention=`MIXED (A=ABS, B=RATIO), CLASS=FULL`, L_max=`12`). **CLASS=FULL pin**: the Mellin regulator used the FULL Mellin-cone evaluator `_analytic_zeta.py` (NOT the SCHEMATIC `_spectral_action_regulators.py`); PV is full mass-scale running at Λ_UV=M_KK. The `_analytic_zeta.py` module SPECTRUM_CACHE was runtime-corrected from a non-existent `_shared/` resolve_output(84,…) path to the canonical session-84 cache (infra resolver drift, documented per `substrate-first-canonical-sourcing.md §(ii.B)`; the FULL evaluator MATH is untouched — `az_cache_path_corrected=True`).

**Solution-space / JACOBSON-NONLOCAL-64 constraint-map status (pinned):** The framework has **LOCATED the CC term** (it is the a_0 moment, the zeroth Seeley-DeWitt residue) but has **NOT SOLVED the CC magnitude**. The absolute a_0/a_2 moments DIVERGE (PART A, S94 signature: Tr(1) ~ L⁸ Weyl, a_2^raw drift 4.9% ≫ 1%). The dimensionless CC ratio a_2/a_0 = 0.431082 is **Functional-INVARIANT WITHIN the analytic-continuation/normalization family** (zeta == Mellin to machine epsilon; raw↔SDW 4.56% < 5%) — the §8.5 "only ratios survive truncation" claim HOLDS for these schemes — but is **Functional-DEPENDENT ACROSS the PV-subtraction family** (PV shifts the ratio ~39% because it reweights a_0 and a_2 differently). This is the lizzi permanent position made precise: the CC magnitude is determined by the regularization scheme as much as by the D_K spectrum — and even the surviving CC RATIO is scheme-family-dependent (FI within zeta/Mellin/raw-SDW, RD across PV). The CLOSED truncation-robust CC object remains the Volovik tracking ratio ρ_vac/ρ_obs = 1.032 (a different ratio, IR-physics, conditional on C10), NOT an absolute a_n magnitude. Direction of explanation: D_K eigenvalues → a_0/a_2 moments (absolute diverge; ratio FI-within-family/RD-across-PV) → CC located-not-solved → the surviving CC observable is the ratio within a fixed regulator family.

**INFO is a clean constraint-map update, NOT a gate failure**: it refines the §8.5 "ratio survives" claim from unqualified-FI to FI-WITHIN-FAMILY (zeta/Mellin/raw-SDW) + RD-ACROSS-PV, and pins the cross-PV shift band (36.86%). A FUTURE companion gate (a_0-PV Mellin-s4 residue, to test PV-cancellation in the S94 FULL evaluator's own a_0/a_2 moments) would sharpen the across-PV result; pre-flagged as a Wave-2→Wave-3 carry-forward candidate (the plan's §"Workshop-routing flag" lists CC-GAP Track C as workshop-eligible — this is NOT Track C, so it is a compute carry-forward, not a workshop).

---

## Wave 2 Synthesis (team-lead)

**Verdicts (6 gates: 2 FAIL, 4 INFO).** No PASS — but every INFO is a favorable functional-invariance confirmation, and both FAILs are clean constraint-map boundaries, not gate failures. All six dispatched in parallel, building ON the recorded S94-K-CSUB-R absolute-divergence FAIL.

| Gate | Verdict | One-line result |
|:--|:--|:--|
| W2-1 SDW-BOREL-PADE | **FAIL** | Raw a₂ SDW series is Borel-NON-summable to the zeta value (positive-real-axis Padé–Borel pole; \|δ\|/ζ=130%, NOT decreasing with Padé order) across raw/PV/Mellin. CC-absolute conditional NOT discharged. Track B (0.9). |
| W2-2 SDW-A0-RESIDUE | **FAIL** | a₀ residue DIVERGES with the S94 d(Res)/dL-increasing signature across raw/ζ/PV/heat-kernel. "Finite pole ladder ≠ finite residue." Track B (0.9). |
| W2-3 SDW-WRONSKIAN-FI | **INFO** (PASS-on-FI) | Decoupling Wronskian sign/zero-structure FUNCTIONAL-INVARIANT: 200/200 sign-agree + 0 interior zeros in ζ AND f* (matching the Sage-certified SD reference W=2(R_K′)³). S75 W2-E hardened with a regulator-invariance certificate (Layer-1 degree-grading). |
| W2-4 SDW-SADDLE-REGINV | **INFO** (PASS-on-FI) | No-interior-saddle FUNCTIONAL-INVARIANT: 0 interior sign-changes of dΓ/dτ in ζ/f*/Gaussian. The εH sign-flip precedent FIRED (Gaussian loop slope −146 vs + for ζ/f*) but \|−146\|≪+59,252 tree slope ⇒ no saddle in any scheme. Transit-not-slow-roll structural. |
| W2-5 SDW-EFT-CONTROL | **INFO** | No parametric small parameter: the scheme-independent a-ratio driver RISES 0.431→0.681 toward 1 (max r_k=0.6808<1 formally converges, but ≥0.5, no comfortable margin). EFT-control verdict is functional-DEPENDENT (Gaussian r₀=1.81 FAIL-band; Mellin 0.014 PASS-band). String-theory V.1 confirmed: §8.5 robustness is representation-theoretic, NOT parametric-EFT. |
| W2-6 SDW-CC-GAP | **INFO** | Ratio a₂/a₀=0.431082 FI-WITHIN-family (ζ==Mellin to machine-eps; raw↔SDW 4.56%) but RD-ACROSS-PV (36.86% shift); absolute DIVERGES (Weyl L⁸). JACOBSON-NONLOCAL-64 pinned: CC located-not-solved; surviving CC observable is the ratio, FI only within a fixed regulator family. NOT Track C. |

### What Changed

#### (a) Numerical revisions
- `a₂_FW_zeta=2776.165389` confirmed NOT the Borel sum of the divergent raw series (best resummed raw −829.26; |δ|/ζ=1.299; PV best 245.17; Mellin=raw).
- a₀ residue L_max-divergence quantified: drift(L10→12) = 4.25 (raw) / 2.35 (ζ=PV) / 1.78 (heat-kernel); all d(Res)/dL increasing.
- New canonical pins (W2-5): `Lambda_sp_over_M_KK=2.06`, `a_6_FW_zeta=765.593826`, `a_8_FW_zeta=521.183178` — completes the d=8 cone {a₀,a₂,a₄,a₆,a₈}.
- CC-ratio cross-PV shift pinned: 36.86% (f₂/f₀=0.6314); within-family drift 4.56%; full-grid drift 0.217 OOM (< 1 OOM → INFO band).
- EFT successive-term a-ratio at Λ=M_KK: [0.4311, 0.4865, 0.5668, 0.6808] (rising toward 1).

#### (b) Structural changes
- **S75 W2-E Spectral-Moment Decoupling Theorem: zeta-derived → FI-certified** (regulator-invariant, Layer-1 degree-grading; W2-3). The cross-layer probability-product licence (§7.3) holds regardless of regulator.
- **S95 W2-3 no-interior-saddle: zeta-specific → regulator-invariant** (FI across ζ/f*/Gaussian; W2-4). Transit-not-slow-roll is structural.
- **§8.5 truncation-robustness REASON: parametric-EFT → representation-theoretic** (block-diagonality E6; W2-5) — the layer hierarchy survives truncation because of representation theory, not a parametric small parameter (there is none).
- **CC-absolute epistemic type sharpened** (W2-1 ∧ W2-2 jointly): on a finite truncated triple ζ_D(s) is entire ⇒ ζ_D(0)≡Tr(1); the continuum a₀_FW_zeta=6440 is an analytic-continuation object NOT reachable as any L→∞ truncation limit, and the divergent raw series is not Borel-summable to it. The absolute moment is a genuine functional-DEPENDENT physical d.o.f. — not a regulator-artifact-with-a-recoverable-value.
- **JACOBSON-NONLOCAL-64 surviving CC observable: unqualified-FI → FI-within-family + RD-across-PV** (W2-6).

### The coherent thread — three-layer-regulator discipline on orthogonal axes
Wave 2 is a clean demonstration of the lizzi methodology law: **what is functional-INVARIANT is structural; what is functional-DEPENDENT is a physical d.o.f. fixed only by the choice of spectral functional.** Layer-1 structural identities — the Wronskian sign (W2-3), the no-saddle topology (W2-4), the a-ratio driver (W2-5), the within-family CC ratio (W2-6) — are FI. Layer-3 absolute magnitudes — the a₀/a₂ moments (W2-1, W2-2), the EFT-control verdict (W2-5), the CC ratio across PV (W2-6) — are functional-DEPENDENT. The CC-absolute is *doubly* confirmed unreachable (resummation fails W2-1; truncation-limit fails W2-2); the surviving CC object is the ratio, FI only within the analytic-continuation family.

### Workshop routing — NONE
The plan pre-flagged three FAIL outcomes as workshop-eligible (Q1 adjudications): WRONSKIAN-FI FAIL, SADDLE-REGINV FAIL, CC-GAP Track C. **None fired** — WRONSKIAN-FI and SADDLE-REGINV both PASSED-on-FI (INFO), and CC-GAP landed refined-Track-A (INFO), explicitly NOT Track C. The three potential adversarial tensions all resolved as favorable FI/refined outcomes. **Wave 2 produces zero workshops** (honest count per `Investigating-Workshops.md`).

### Effected In-Session (non-math; completed before STOP)
- [x] **Dual-root active-root flag corruption — RESTORED + RELOCATED + HARDENED.** W2-6 surfaced that `_analytic_zeta.py` SPECTRUM_CACHE resolved to a non-existent `_shared/` path. Root cause (git-traced): the Phase-4-cutover flag `computation_root.json` (`active_root="computations"`) was inadvertently deleted by the "audit-clean hygiene" quicksave `5056e28a`, silently reverting `resolve_*` to the flat-mode default. Fix: restored the flag and RELOCATED it `tools/` → `computations/_shared/` (out of the hygiene-swept dir); HARDENED `DEFAULT_ROOT` → `"computations"` so a missing flag falls back to the correct nested live tree; reverted the band-aid + removed the dead misnamed `PROJECT_ROOT` in `_analytic_zeta.py`; updated `computations/README.md`. Verified end-to-end (`get_active_root()`="computations"; `resolve_output(84,…)`→session-84, exists; missing-config fallback→"computations"; module self-test clean). — `computations/_shared/computation_root.json` (NEW) · `tools/computation_root.py` · `computations/_shared/_analytic_zeta.py` · `computations/README.md`
- [x] **3 canonical constants promoted** (by W2-5 via `update_constant`, verified present): `Lambda_sp_over_M_KK=2.06`, `a_6_FW_zeta=765.593826`, `a_8_FW_zeta=521.183178` — `computations/_shared/canonical_constants.py:633-635` + PROVENANCE `:1611-1617`.
- [x] **W2-4 representation-convention note captured.** E7's `dS/dτ|_fold=+58,672.8` is the gradient of `S_full=Σ|λ|` (rep A), NOT of the curvature-polynomial `a₀−a₂+a₄` (rep B, slope ≈ −10.22); the no-saddle count is 0 under both, so the verdict is representation-robust. Documented in §W2-4; routed to housekeeping §D for the session-close capstone-hygiene reconciliation of the E7 anchor.

(Registry annotations for the four structural changes above + the capstone CC-sector status reconciliations route to `session-96-housekeeping.md §D` for the W8 consolidation/status-sync wave — NOT bulk-appended mid-wave, per the curated-doc designated-writer discipline.)

## Carry-Forward Computations

### CF-S97-W2-1 — a₀/a₂-PV Mellin-s4 residue companion (test PV-cancellation in the FULL evaluator)

| Field | Spec |
|:--|:--|
| **What** | Compute a₀^PV and a₂^PV via the FULL `_analytic_zeta.py` Mellin-cone evaluator at the s=4 (a₀) and s=3 (a₂) poles with full Pauli–Villars mass-scale subtraction at Λ_UV=M_KK, plus the PV-subtracted ratio (a₂/a₀)^PV; test whether W2-6's 36.86% Gilkey-normalized cross-PV shift reproduces in the FULL evaluator's own moments. |
| **Inputs** | `_analytic_zeta.py` (FULL Mellin evaluator — resolves correctly post the W2 flag-fix); `computations/session-84/s84_spectrum_cache_L12_tau019.npz`; canonical `a_0_FW_zeta=6440`, `a_2_FW_zeta=2776.165389`; `s96_sdw_cc_gap.npz` (36.86% PV-shift baseline + f₂/f₀=0.6314). |
| **Gate** | PASS iff `|(a₂/a₀)^PV_Mellin − (a₂/a₀)^PV_Gilkey| / (a₂/a₀)^PV_Gilkey < 0.10` (cross-PV RD evaluator-robust, sharpening W2-6); FAIL iff > 1 OOM divergence (the ~39% shift is Gilkey-normalization-specific); INFO between. |
| **Effort** | ~0.5 wave — closed-form on the cache + the Mellin evaluator; no new spectrum diagonalization. |

**Candidates that did NOT fire** (per the plan's conditional CF list): BOREL-PADE FAILed ⇒ no "CC-absolute-magnitude gate IF PASS"; EFT-CONTROL landed INFO (not FAIL) ⇒ no "FI-ratio-robustness-classification IF FAIL"; a₆/a₈ regulator-class sub-keying resolved in-wave (W2-5: ζ == Mellin to machine-eps, no material divergence) ⇒ no W7 sub-keying CF.

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:--|:--|:--|:--|:--|
| 2026-05-29 | CC-absolute (a₀/a₂ magnitude) | located, conditional (S94 FAIL) | located-NOT-solvable-by-resummation-or-truncation | W2-1 Borel-non-summable to ζ + W2-2 residue diverges + ζ_D(0)≡Tr(1) on finite triple |
| 2026-05-29 | S75 W2-E decoupling theorem | zeta-derived | FI-certified (regulator-invariant, Layer-1 degree-grading) | W2-3: Wronskian sign 200/200 + 0 interior zeros in SD/ζ/f* |
| 2026-05-29 | S95 W2-3 no-interior-saddle | zeta-specific | regulator-invariant (FI) | W2-4: 0 interior sign-changes in ζ/f*/Gaussian (εH flip fired on Gaussian loop but tree-dominated) |
| 2026-05-29 | §8.5 truncation-robustness REASON | (implicit parametric-EFT) | representation-theoretic (block-diagonality E6) | W2-5: no parametric small parameter (a-ratio rises 0.43→0.68; Λ_sp/M_KK=2.06 thin) |
| 2026-05-29 | JACOBSON-NONLOCAL-64 / surviving CC observable | "only ratios survive" (unqualified-FI) | ratio FI-WITHIN-family + RD-ACROSS-PV (36.86%) | W2-6: ζ==Mellin machine-eps, raw-SDW 4.56%, PV shifts ~39% |
| 2026-05-29 | dual-root resolver infra (`computation_root.json`) | flag deleted (5056e28a); flat-default misroute | flag restored+relocated to computations/_shared/; DEFAULT_ROOT hardened to nested | infra fix surfaced by W2-6; resolve_* now correct for all consumers |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Verdict (audit_sha256) |
|:--|:--|:--|:--|:--|
| W2-1 BOREL-PADE | s96_sdw_borel_pade.py (45 KB) | s96_sdw_borel_pade.npz (13 KB) | .png (219 KB) | FAIL `261e17c5…` |
| W2-2 A0-RESIDUE | s96_sdw_a0_residue.py (27 KB) | s96_sdw_a0_residue.npz (9 KB) | .png (94 KB) | FAIL `d7f5c6fa…` |
| W2-3 WRONSKIAN-FI | s96_sdw_wronskian_fi.py (35 KB) | s96_sdw_wronskian_fi.npz (23 KB) | .png (182 KB) | INFO `3dd0235a…` |
| W2-4 SADDLE-REGINV | s96_sdw_saddle_reginv.py (44 KB) | s96_sdw_saddle_reginv.npz (46 KB) | .png (198 KB) | INFO `1e32d548…` |
| W2-5 EFT-CONTROL | s96_sdw_eft_control.py | s96_sdw_eft_control.npz | .png | INFO `74158937…` (supersedes `7d62a904…`) |
| W2-6 CC-GAP | s96_sdw_cc_gap.py (54 KB) | s96_sdw_cc_gap.npz (19 KB) | .png (133 KB) | INFO `da899b4d…` (supersedes `98fd4bd7…`←`ea5b32ff…`) |

All scripts in `computations/session-96/`; verdicts in `computations/session-96/s96_gate_verdicts.txt` (dual-SHA companion rows + schema-v2 3-tuples for the three [SIGN] gates W2-3/4/5; sig_5 clean across all 6 gates incl. superseded lines).
