# Investigation 3 Wave 2 — Heat-Kernel Scale-Transport & Spectral Rigidity (Results Working Paper)

**Investigation**: 3 | **Wave**: 2 | **Plan**: investigation-3-plan-w2.md | **Theme**: Heat-kernel machinery on the framework's dimensionful/extensive weak axis — d_s-flow scale-transport, isospectral rigidity, A_s amplitude floor, Weyl-remainder geodesic stationarity.

**Track**: INVESTIGATION | **Verdict ledger**: `computations/investigation-3/inv3_gate_verdicts.txt` (emit via `emit_verdict(session=3, track="investigation", ...)` per `.claude/rules/gate-verdicts.md §"Investigation-Track Canonical Path"`). All four gates are `gate_type: compute` (executor `spectral-geometer`) → each emits a verdict line.

## Gate Sections

### §W2-1. INV3-W2-1-DS-FLOW-SCALE-TRANSPORT (spectral-geometer)

**Status**: COMPLETED
**Gate ID**: `INV3-W2-1-DS-FLOW-SCALE-TRANSPORT`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (the heat trace `P(σ)=Tr e^{−σ D_K²}` and its `d_s(σ)` flow are the fabric itself, not its excitations)
**Gate type**: `compute`
**Agent**: `spectral-geometer`
**Hypothesis**: the anomalous-scaling integral `I = −∫ θ(σ) dlnσ` (with `θ(σ)=d_s(σ)−d_s(σ→0)`, `d_s(σ→0)=8`) equals the K→K* scale-transport e-fold count `ln(K/K*) ≈ ln(23) ≈ 3.135` to within 10%, identifying the dimensionful K-pivot as an EMERGENT output of the intensive `d_s(σ)` flow.
**Plan reference**: `sessions/investigation/investigation-3/investigation-3-plan-w2.md` §W2-1 (machinery pin, thresholds, substitution chain source).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

| # | Artifact | Path | must_contain | Status |
|:--|:---------|:-----|:-------------|:-------|
| 1 | script | `computations/investigation-3/inv3_w2_ds_flow_scale_transport.py` | `from canonical_constants import`, `print_verdict_payload` | ✓ both present (grep-verified) |
| 2 | data | `computations/investigation-3/inv3_w2_ds_flow_scale_transport.npz` | exists, non-stub (40 keys) | ✓ |
| 3 | plot | `computations/investigation-3/inv3_w2_ds_flow_scale_transport.png` | exists (3-panel: P(σ), d_s(σ), θ+cumulative-I) | ✓ |
| 4 | verdict line | `computations/investigation-3/inv3_gate_verdicts.txt` | `^INV3-W2-1:.* audit_sha256=[a-f0-9]{64}` | ✓ (FAIL; dual-SHA + 3-tuple + 5 extra rows) |
| 5 | WP section | this section | `**Status**:.*COMPLETED`, `**Verdict**:.*(PASS\|FAIL\|INFO)`, `**Output Artifacts**`, `**MCP Pre-Compute Audit**` | ✓ |

**MCP Pre-Compute Audit**:

Queries executed BEFORE writing the script (knowledge-MCP query-first discipline):

- `get_constant('d_s_fold_window_sigma')` → **1.4005** (S92-ADHOC-SPECTRAL-DIMENSION-DS-FLOW-VS-CDT; σ_fold pin confirmed).
- `search_knowledge('spectral dimension flow d_s sigma heat trace return probability')` → canonical form `P(σ)=Σ_{(p,q)} dim(p,q) Σ_i e^{−σλ²}`, `d_s(σ)=−2 dlnP/dlnσ` confirmed across S19/S35/S44/S92/S93; **`d_s_min=6.3091 at σ=1`** is an OLD S19a normal-state run (different L_max), informative not canonical.
- `trace_entity('spectral dimension flow d_s')` → S94 van-Hove γ_E resolution: **eq_7048 "the fold sits at FINITE energy"** + eq_7049 `d_s(σ_*)=2σ_*⟨λ²⟩_{σ_*}` (energy-axis DOS form) — flags that the σ→0=8 reasoning must be EMPIRICALLY verified, not assumed.
- `search_knowledge('K pivot scale transport e-fold ln(K/K*) 0.087 M_KK')` → **K_pivot=2.0 M_KK = atlas-04 C2 "BROKEN-WITH-LIVE-RESEARCH-PATHWAY"** (never rigorously derived; SA-Goldstone mixing FAILS at K=2.0); **K*=0.087 M_KK = atlas-07 S51 DERIVED** (`m_G/√J`). Confirms the gate is LIVE (testing whether d_s-flow emergently produces this ratio).
- `trace_entity('scale transport e-fold K pivot')` → **NO TRACE** — the d_s-flow↔scale-transport identity is NOT in the knowledge base; genuine unprecedented compute (NOT pre-closed).
- `get_constant('M_KK')` → 7.428660036284456e16 GeV; `get_constant('K_star')` → **1.3130** (S84 lab-3He-B coth(1) anchor — a DIFFERENT object from the 0.087 seed anchor; documented in the script).

**Branch decision**: NOT pre-closed; the σ→0=8 premise is flagged by S94 as window-sensitive and MUST be verified empirically (it was — and it FAILED, see Results).

**Verdict**: **FAIL** — `value=I=−0.200440 (=−∫θ dlnσ)`, `scheme=DS-FLOW-SCALE-TRANSPORT-heat-trace-FW`, `convention=RATIO`, `L_max=12`. 3-tuple: `sign=FAIL magnitude=FAIL regime=VALID` → composite FAIL (the collapse rule fires on `sign_verdict==FAIL` AND independently on `magnitude_verdict==FAIL & regime==VALID`). `audit_sha256=c31277d5acbc2aadc0ea792a12805fd55c7f8f7642cf6f2eb1e55a605040130e`, `content_sha256=6b1b806da7f32df6a1000ed3f49595f40b36c642292e92e453d30b7ebdd2a99b`.

**Results**:

*Governing structure & numbers.* Reconstructed the bare-`D_K` heat trace `P(σ)=Σ_{(p,q)} dim(p,q)·Σ_i e^{−σ|λ|²_{(p,q),i}}` over the L12 fold spectrum (NORMAL STATE, Δ=0; 89/90 Peter-Weyl sectors; the (4,4) sector — dim=125, weight 16·125²=250000 — is MISSING from the `s84_spectrum_cache_L12_tau019.npz`, consistent with the P(σ→0)≈3.191×10⁷ vs Σ16·dim²=3.196×10⁷ deficit of 50361). Block convention verified bit-exactly: each `(p,q)` block stores 16·dim(p,q) eigenvalues; the PW multiplicity dim(p,q) is the heat-trace weight. `d_s(σ)=−2 dlnP/dlnσ` by centered FD on a 4000-pt log-σ probe grid; integration on a 400-pt log grid over `[σ_UV, σ_fold]`.

| Quantity | Value |
|:---------|:------|
| `I = −∫θ dlnσ` | **−0.200440** (NEGATIVE) |
| `ln(K/K*)` target | 3.134994 (K=2.0, K*=0.087 M_KK; analytic) |
| relative deviation | **0.936064 (93.6%)** ≫ 25% INFO ceiling |
| `d_s(σ→0)` empirical (σ=1e-4) | **0.0032** — NOT 8 |
| `σ_UV` READ-OFF (last σ within 1% of 8) | 0.6634 M_KK⁻² (d_s there = 8.079) |
| `d_s(σ_fold=1.4005)` | 8.4847 (= d_s max on window; still rising) |
| σ_UV robustness (±0.5 dex) | I ∈ [−0.20, +1.03], spread 1.23, **frac_in_band = 0.000** |

*Substitution chain — the SIGN read-off (the [SIGN] test).* The plan's Step-2/4 chain predicted `θ(σ)=d_s(σ)−8 ≤ 0` on the window (d_s drops from a UV plateau of 8), hence `I=−∫θdlnσ ≥ 0`, same sign as `ln(K/K*)>0`. **The finite L12 spectrum delivers the OPPOSITE.** Empirically (each step substituted with the computed number):
- Step 2 premise `d_s(σ→0)=8` is FALSE on the finite spectrum: as σ→0, `P(σ)→Σ16·dim²=const`, so `dlnP/dlnσ→0` ⇒ `d_s(σ→0)→0.0032`, NOT 8. This is the validity-tier **Level-3 truncation artifact** ("d_s in UV → 0 not 8", per the spectral-geometer memory): a finite eigenvalue multiset has no continuum Weyl UV regime.
- The d_s curve RISES from 0, crosses 8 ONCE (upward) at σ=0.596, and on `[σ_UV=0.663, σ_fold=1.4005]` runs `d_s ∈ [8.08, 8.48]` ⇒ `θ = d_s−8 ∈ [+0.079, +0.485] ≥ 0` (POSITIVE).
- Therefore `∫θ dlnσ > 0` ⇒ `I = −∫θ dlnσ = −0.2004 < 0`. **SIGN MISMATCH** (predicted I ≥ 0; observed I < 0) ⇒ `sign_verdict=FAIL`.
- Step 4's "gap-dominated IR drives d_s→0 as σ→∞" is also FALSE on this finite spectrum: d_s keeps RISING to 137 at σ=100 (no gap-dominated d_s→0 regime at accessible σ, because min|λ|²≈0.672 is not a small gap).

*Why this is robust, not a knob.* The σ_UV-robustness scan sweeps the read-off ±0.5 dex: `frac_in_band=0.000` (NO σ_UV brings |I| within 10%), so even an INFO (window-sensitive) reading is excluded. The FAIL holds on TWO independent pre-registered criteria (sign-flip AND 93.6% magnitude). The (4,4) missing sector cannot rescue it: d_s is a log-derivative, so one interior bulk sector is a near-multiplicative shift in P that largely cancels in dlnP/dlnσ — and no plausible single-sector correction flips a 93.6% miss or a sign.

*4-tuple*: `(value=−0.2004398017185191, scheme=DS-FLOW-SCALE-TRANSPORT-heat-trace-FW, convention=RATIO, L_max=12)`. *Regulator pin*: N/A — d_s is a log-derivative of `P=Tr e^{−σD_K²}`; no Seeley-DeWitt `a_n` moment is cited (scheme `heat-trace-FW`, Level-1 exact-on-truncation). *Dual-SHA*: `audit_sha256=c31277d5acbc2aad…` over [script, canonical, pinmap]; `content_sha256=6b1b806da7f32df6…` over [script]. *Schema-v2 3-tuple*: `sign_verdict=FAIL magnitude_verdict=FAIL regime_verdict=VALID`.

*dual_prior re-allocation.* FAIL (>25% AND sign-flip) → **0.85 to Track_B** (Reading_2 NUMERICAL-COINCIDENCE / non-structural): the d_s(σ)-flow integral does NOT encode the K→K* scale-transport map. Per the pre-registered `FAIL_meaning`: **the UB-1 (d_s-as-scale-map) corridor is CLOSED in its pre-registered form** — the dimensionful K-pivot is NOT recovered as an emergent output of the intensive d_s flow; the K/K* ratio remains an independent free parameter on the dimensionful axis. This route does not rescue the framework's weak (dimensionful/extensive) axis.

*Substrate-physics assessment (GEOMETRIC).* The substrate IS the return probability `P(σ)=Tr e^{−σD_K²}` — the finding is about the fabric's own diffusion kernel, not a probe in a container. The honest substrate-first reading: at the accessible diffusion-window the finite-truncation spectral-complexity flow `d_s(σ)` has the WRONG topology for the hypothesized e-fold map — it rises through 8 toward the fold (spectral weight CONCENTRATING as σ probes the fold band) rather than dropping from a continuum manifold-dimension plateau. The "8" that canonical_constants.py cites as the UV `d_s→8` Weyl limit is a *continuum* statement the finite L12 spectrum does not realize at σ ∈ [1e-4, 1.4]; the σ→0 behavior is the truncation-saturation `d_s→0`. This is the same epistemic class as the sibling INV3-W1-3 finding (a literal pre-registered operator geometrically mis-specified for the actual surface): the gate's pre-registration assumed continuum-manifold d_s topology; the substrate-IS finite-truncation flow refutes it. The result is a genuine boundary on the constraint surface — it tells us the intensive d_s(σ) flow, as computed on the bare D_K finite spectrum, does not carry the dimensionful scale-transport content the survey's UB-1 step hoped for. Follow-up (not this gate): whether a *continuum-extrapolated* `d_s` (L_max→∞, or the energy-axis `d_s(σ_*)=2σ_*⟨λ²⟩` windowed form of S94) recovers the predicted drop-from-8 topology — but that is a different observable than the one pre-registered here.

---

### §W2-2. INV3-W2-2-ISOSPECTRAL-RIGIDITY-L3 (spectral-geometer)

**Status**: COMPLETED
**Gate ID**: `INV3-W2-2-ISOSPECTRAL-RIGIDITY-L3` (verdict-line gate-id `INV3-W2-2`; `ISOSPECTRAL-RIGIDITY-L3` carried in `scheme=`)
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (tests whether the `D_K²` spectrum reconstructs the Jensen geometry — spectral-triple reconstruction)
**Gate type**: `compute`
**Agent**: `spectral-geometer`
**Hypothesis**: on the volume-preserving Jensen TT family at L_max=3, NO two distinct `τ≠τ'` produce bit-identical `{a_0,a_2,a_4}` Seeley-DeWitt multisets while differing in the non-spectral Kosmann pairing `V_nm` — i.e. the spectrum reconstructs the Jensen geometry (rigidity holds; Connes-reconstructible). Rigidity-FAIL = a named isospectral-non-isometric degeneracy.
**Plan reference**: `sessions/investigation/investigation-3/investigation-3-plan-w2.md` §W2-2 (set-membership predicate, tols, regulator pin).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

| # | Artifact | Path | must_contain → status |
|:--|:---------|:-----|:----------------------|
| 1 | script | `computations/investigation-3/inv3_w2_isospectral_rigidity_l3.py` | `from canonical_constants import` ✓ · `print_verdict_payload` ✓ |
| 2 | data | `computations/investigation-3/inv3_w2_isospectral_rigidity_l3.npz` | exists ✓ (24 keys) |
| 3 | plot | `computations/investigation-3/inv3_w2_isospectral_rigidity_l3.png` | exists ✓ (4-panel) |
| 4 | verdict | `computations/investigation-3/inv3_gate_verdicts.txt` | `^INV3-W2-2:.* audit_sha256=[a-f0-9]{64}` ✓ |
| 5 | wp_section | this section | `Status:.*COMPLETED` ✓ · `Verdict:.*(PASS\|FAIL\|INFO)` ✓ · `Output Artifacts` ✓ · `MCP Pre-Compute Audit` ✓ |

Verified by content presence (regex), not line/byte count. Verdict line (full): `INV3-W2-2: PASS -- value='RIGID_empty_degeneracy_set_closest_pair_tau=(0.05000,0.05015)_combined_d=2.461e+01_dmom=1.20e-06_dspec=2.46e+01_dV=1.46e-04' scheme=ISOSPECTRAL-RIGIDITY-L3 convention=ABSOLUTE L_max=3 audit_sha256=ba8d46af9aa3a3846db01df986fd651b2083c9bb6847f04c11fa7488824fd809 content_sha256=f395ad089b574002dc296407b1ced03ac8936e70f28a21d5f2bf5c9b8abe71eb schema_version=S84+`

**MCP Pre-Compute Audit** (run BEFORE writing the script; `.claude/rules/knowledge-index-usage.md`):

| Query | Salient return | Branch decision |
|:------|:---------------|:----------------|
| `search_knowledge('isospectral non-isometric spectral rigidity Jensen Connes reconstruction')` | `SU3-SPECTRAL-RIGIDITY` gate **seed** (session-99-litrev-spectral-geometry-baptista): "PASS = no two distinct-τ metrics isospectral; spectrum reconstructs Jensen geometry". Connes reconstruction theorem (Paper 11: the spectral triple `(A,H,D)`, not the cutoff, reconstructs the manifold). | NOT pre-closed — this gate IS the COMPUTE of that seed. Proceed. |
| `search_knowledge('Seeley-DeWitt a_2 fold 0.728235 Gilkey curvature polynomial')` | `a_2^{SD}(fold)=0.728235` (Gilkey, exact, S46/S61, 10-digit match); `a_2^{SD}=(4π)^{-4}·(20R/3)·Vol`. | Confirms the `a_n^{lattice}` regulator anchor. |
| `search_knowledge('Kosmann pairing V_nm spinor basis Lie derivative')` | `V_{nm}=Σ_a \|⟨ψ_n\|K_a\|ψ_m⟩\|²` (session-34-baptista-collab, canonical form); K_a = Kosmann generators (8 spinor-basis matrices). | Confirms V_nm convention + spinor basis. |
| `search_knowledge('a_2 zeta 2776 factor 3812 spectral zeta moment versus Seeley-DeWitt')` | "NOT the same number: `a_2^{ζ}=2776.17` is the spectral moment ζ_D(1); `a_2^{SD}=0.728` is the Gilkey coefficient. Ratio ≈ 3812." (`lizzi C-L4` PROVEN theorem). | **Load-bearing**: the rigidity test MUST use `a_n^{lattice}` (geometric SD), NOT `a_n^{ζ}`. |
| `trace_entity('Schur-rigidity')` | `§VII.BR Schur-rigidity (STAGE-3-PERMANENT, audit 6c53304a)` — band-selective Schur rigidity on G-invariant deformation families; S101 Stage-2 PASS-AND (Axis-A kaluza-klein, Axis-B landau). | **Structural prior**: Schur's lemma forbids the deformation from mixing inequivalent irreps ⟹ predicts rigidity-PASS (Track_A). This gate provides the L_max=3 operational evidence; NOT a pre-closure of the existence predicate. |
| `trace_entity('SU3-SPECTRAL-RIGIDITY')` / `trace_entity('isospectral rigidity SU(3)')` | seed equation only / no trace. | No prior compute exists — this is the inaugural computation. |
| `get_constant('tau_fold')` = 0.19 · `get_constant('a_2_FW_zeta')` = 2776.165389 | confirmed canonical. | τ-scan brackets τ_fold; a_2^{ζ} is the DISTINCT object NOT used as the regulator. |

**Verdict**: **PASS** — empty degeneracy set; rigidity holds; the `D_K²` spectrum reconstructs the Jensen geometry at L_max=3. Dual-prior re-allocation: PASS empty-set → **0.9 to Track_A** (rigidity holds; Connes-reconstructible at this truncation). **No 3-tuple companion row** (set-membership `[VERIFY]` gate, no `[SIGN]` trigger). Composite collapse: trivially PASS (set-membership; the degeneracy set is empty).

**Results**:

*Regulator pin — load-bearing (`a_n^{lattice}`, NOT `a_n^{ζ}`).* The three Seeley-DeWitt moments are the **GEOMETRIC curvature-polynomial** coefficients on `(SU(3), g_τ)`, d=8, spinor rank 2⁴=16, prefactor `(4π)^{-4}`, with the Lichnerowicz endomorphism `E = −R/4·1` (`D_K² = ∇*∇ + R/4`):

```
a_0^{lattice}(τ) = (4π)^{-4} · tr_S(1) · Vol(g_τ) = (4π)^{-4} · 16 · Vol
a_2^{lattice}(τ) = (4π)^{-4} · tr_S(R/6 − E) · Vol = (4π)^{-4} · (20R(τ)/3) · Vol
a_4^{lattice}(τ) = (4π)^{-4} · (1/360) · Vol · [60·R·tr(E) + 180·tr(E²) + 30·tr_S(Σ Ω_ab Ω^ab) + tr(1)·(5R² − 2|Ric|² + 2|Riem|²)]
```
All `∇`-derivative terms (`E_{;kk}`, `R_{;kk}`) vanish on the homogeneous space (constant curvature scalars). The spin-bundle curvature `Ω_ab = (1/4)R_{abcd}γ^cγ^d` and its Clifford trace `tr_S(Σ Ω_ab Ω^ab)` are computed EXACTLY from the SP-2 Riemann tensor `R_abcd(τ)` (machine-ε validated, S20a 147/147) + the Cliff(8) γ's — no folklore coefficient. The curvature scalars are the SP-2 exact analytic forms: `R(τ) = −¼e^{−4τ} + 2e^{−τ} − ¼ + ½e^{2τ}`, `K(τ) = |Riem|²` (closed form), `|Ric|²(τ) = Σ Ric_ab²`.

- **Anchor cross-check**: `a_2^{lattice}(τ_fold=0.19) = 0.728234973`, matches canonical `a_2^{SD}=0.728235` to **|dev|=2.74e-8**. ✓
- **Factor-3812 discipline confirmed**: `a_2^{lattice}=0.728235` is NOT `a_2^{ζ}=2776.1654`; ratio = **3812.2**. The isospectral test used the geometric SD multiset throughout. ✓
- **`a_0^{lattice}` is τ-INDEPENDENT** = 0.8660254 at EVERY τ (unique value across the whole scan): the volume-preserving Jensen constraint `L1·L2³·L3⁴ = 1` ⟹ `Vol(g_τ) = Vol(g_0) = const`. This is a structural feature, not a numerical coincidence. ✓

*Spectral multiset.* `{λ_k²(τ)}` built per Peter-Weyl sector p+q≤3 (sectors (0,0),(1,0),(0,1),(1,1),(2,0),(0,2),(2,1),(1,2),(3,0),(0,3)) via `1j·D_π` Hermitian diagonalization; each block eigenvalue entered with PW multiplicity dim(p,q). **Count = 12880** (PW-weighted) eigenvalues per τ. **L_max=3 sub-block cross-validation vs the L12 master cache** (`s84_spectrum_cache_L12_tau019.npz` filtered to p+q≤3) at τ=0.19: max|dev| = **8.88e-15** (machine ε) across 10 sectors — the reconstruction IS the cache.

*Non-spectral discriminator (Kosmann pairing).* `V_total(τ) = Σ_{n,m,a} |⟨n|K_a(τ)|m⟩|² = Σ_a ‖K_a(τ)‖_F²` on the (0,0) singlet sector (canonical s23a construction; the eigenbasis projection is unitary so the n,m-sum is the Frobenius norm). `K_a(τ) = (1/8) Σ_{r,s} [Γ^s_{ra}(τ) − Γ^r_{sa}(τ)] γ_r γ_s` is the Kosmann–Lichnerowicz spinorial correction (Baptista Paper 17 eq 4.1, ANTISYMMETRIC covariant-derivative form). **Convention reconciliation**: the plan's `K_a = (1/8)Σ A^a_{rs}γ_rγ_s` pin is satisfied by `A^a_{rs}(τ) = Γ^s_{ra}(τ) − Γ^r_{sa}(τ)`; the MEMORY "adjoint" form `A^a_{rs}=−f_{a,r,s}` is the τ=0 bi-invariant special case (`Γ^c_{ab}=½f^c_{ab}`). The τ-VARYING `Γ(τ)` is precisely what makes V_total a genuine NON-spectral discriminator carrying geometric information beyond the eigenvalue list. `V_total(τ)` ranges [4.0245, 5.1474] over the scan, strictly monotone increasing.

*Rigidity scan (O(N²), 2,001,000 pairs over 2001 τ in [0.05, 0.35], step 1.5e-4).*

| Quantity | Value |
|:---------|:------|
| Exact degeneracies (FAIL evidence) | **0** |
| Near-degeneracies (INFO band [1e-9, 1e-6]) | **0** |
| Global closest pair (combined moment+spectral metric) | τ = (0.05000, 0.05015) — the ADJACENT grid neighbours |
| · d_moment (a0+a2+a4) | 1.199e-6 |
| · d_spec_scalar (s1+s2+s3+count) | 24.61 |
| · ΔV (Kosmann) | 1.462e-4 |
| min adjacent \|Δs1\| (= \|ΔΣλ²\|) | **0.6535** |
| min adjacent \|ΔV\| | 1.46e-4 (> tol_V=1e-6 everywhere) |

*Structural reason rigidity holds (NOT a tol/pre-screen artifact).* `s1 = Σλ²(τ)` is **strictly monotone increasing** in τ (sign-uniform finite difference), with **minimum adjacent gap 0.6535 — nine orders of magnitude above tol_spec=1e-9**. Because s1 is monotone, the smallest spectral separation over ALL 2,001,000 pairs IS the adjacent one (0.6535); any non-adjacent pair sums ≥2 positive gaps and is strictly larger. Therefore NO τ-pair — adjacent or not — can have a matching eigenvalue multiset. The empty degeneracy set is a **structural consequence of s1-monotonicity**, independent of the (loose 1e-7) pre-screen, which can never fire for any pair. Even the degenerate counterfactual is moot: `V_total` itself separates every pair by ≥1.46e-4. The first spectral power-sum `Σλ²` (essentially Tr D_K², the integrated heat-trace at leading order) alone reconstructs τ.

**4-tuple**: `(value=RIGID_empty_degeneracy_set..., scheme=ISOSPECTRAL-RIGIDITY-L3, convention=ABSOLUTE, L_max=3)`. **dual-SHA**: audit_sha256=`ba8d46af9aa3a384…` over [script, canonical, pinmap]; content_sha256=`f395ad089b574002…` over [script]. Companion `extra_rows` carry the regulator_pin (`a_n^{lattice}` factor-3812), the rigidity predicate, and the closest-pair distance.

**Substrate-physics assessment** (GEOMETRIC). The fabric's vibrational spectrum `{λ_k²(τ)}` determines its own internal Jensen-deformed SU(3) geometry — Kac's "can one hear the shape of the drum?" specialized to the substrate, answered **YES** at L_max=3. The arrow is substrate-first: `D_K(τ) eigenvalues → {a_0(const), a_2∝R(τ), a_4(curvature²(τ))}` (the LOCAL geometry the spectrum encodes) + the full multiset (the GLOBAL datum). The spectrum IS the geometry — the strongest IS-not-IN statement: the substrate is NOT a metric on an external manifold being reconstructed; its own spectral content fixes its own internal structure. The result is consistent with, and provides operational L_max=3 evidence for, the `§VII.BR Schur-rigidity` STAGE-3-PERMANENT structural prior (Schur's lemma forbids the G-invariant deformation from mixing inequivalent irreps, so no accidental isospectral-non-isometric pair can arise). The Kosmann pairing `V_total` (the non-spectral discriminator) is also injective in τ, so even if a spectral degeneracy existed the substrate's spinor structure would still fix τ. **Caveat on scope**: this is a finite-truncation (L_max=3) result; the bridge to the full continuum Connes-reconstruction is the `L_max → ∞` limit (the candidate Track_A reading at 0.9). The monotonicity of `Σλ²` is what underlies the rigidity and is expected to persist at higher L_max (each new sector adds strictly positive, τ-monotone curvature-weighted contributions); a finer-bracket or L_max=4 control is the natural follow-up only if a near-degeneracy ever surfaces (none did here). **Substrate-first framing of "rigidity"**: the eigenvalue spectrum does not merely *label* the Jensen geometry — it IS the geometry's complete local+global invariant content at this truncation; the dimensionful K-pivot / A_s weakness elsewhere on the extensive axis is orthogonal to this intensive, regulator-robust reconstruction statement.
---

### §W2-3. INV3-W2-3-AS-AMPLITUDE-FLOOR-NSFUNCTIONAL (spectral-geometer)

**Status**: COMPLETED
**Gate ID**: `INV3-W2-3-AS-AMPLITUDE-FLOOR-NSFUNCTIONAL`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (`A_s` is the amplitude of the post-transit GGE acoustic interference pattern — a phononic observable)
**Gate type**: `compute`
**Agent**: `spectral-geometer` (computes the value ONLY; the `falsifier-master-inventory.md` ROW is `mack-cosmic-bridge` sole-writer ON SESSION-PROMOTION, NOT this investigation gate — `feedback_mack-bridge-role.md`)
**Hypothesis**: under the S103 n_s-SELECTED generating functional (`sqrt(x)` Chamseddine-Connes / BCS+1-loop-sqrt-cutoff, `n_s_FW_sqrt_cutoff=0.959`), `A_s = (M_KK/M_Pl)² × (dimensionless near-floor functional via exp(−ζ'_{D_K}(0)) of the near-floor DOS at the FK-saturating sector λ_min=0.845269)` collapses to ONE regulator-tagged OOM value vs Planck `A_s=2.1e-9`, retiring the 3.02× / 3.15-OOM / 9.47-OOM ambiguity.
**Plan reference**: `sessions/investigation/investigation-3/investigation-3-plan-w2.md` §W2-3 (CLASS=FULL, M_Pl_choice=reduced, publication_precision=4 pins).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- (1) script `computations/investigation-3/inv3_w2_as_amplitude_floor.py` — EXISTS; `from canonical_constants import` ✓ (line 73), `print_verdict_payload` ✓ (docstring contract; the script prints the `<<<EMIT_VERDICT_PAYLOAD>>>` delimited block per the template, agent calls `emit_verdict`).
- (2) data `computations/investigation-3/inv3_w2_as_amplitude_floor.npz` — EXISTS (14649 bytes, 51 keys; `gap_OOM=6.0076`, `F_nearfloor=2.2961`, `verdict_composite=INFO`).
- (3) plot `computations/investigation-3/inv3_w2_as_amplitude_floor.png` — EXISTS (113292 bytes; OOM-ladder + near-floor-DOS panels).
- (4) verdict line `computations/investigation-3/inv3_gate_verdicts.txt` — `^INV3-W2-3:.* audit_sha256=[a-f0-9]{64}` ✓. CANONICAL (latest non-superseded, Option A) `audit_sha256=f85e981d1f74b3a3f1ec9e3e83a360a3c7386ce444476ceb666f1ccebb92f523`, `supersedes=73e0b9d8243f892382f97f389ec3426e88b90d8b3a3037b7ad03ef1069502b0a` (the prior line retained per absolute verdict permanence; superseded for a script-bug fix — added the `print_verdict_payload` helper the must_contain requires; physics IDENTICAL, gap_OOM=+6.008, INFO). 2 canonical lines × 9 rows.
- (5) this WP section — `**Status**: COMPLETED`, `**Verdict**: INFO`, `**Output Artifacts**`, `**MCP Pre-Compute Audit**` all present.

**MCP Pre-Compute Audit**:
- `get_constant('M_KK')` → `7.428660036284456e16` GeV (S42 CONST-FREEZE-42; default = M_KK_gravity).
- `get_constant('M_Pl_reduced')` → `2.435e18` GeV (S7, CODATA 2018); `get_constant('M_Pl_unreduced')` → `1.2209e19` (the 1.40-OOM lever, cross-reported).
- `get_constant('A_s_Planck')` → `2.1e-9` (Planck 2018; alias of A_s_CMB).
- `get_constant('n_s_FW_sqrt_cutoff')` → `0.9590` (S103-Q28-LAYER2-A6 PASS; the SELECTED sqrt(x)/BCS+1-loop-sqrt-cutoff functional — the SAME functional that fixes n_s now fixes A_s here).
- `get_constant('E_B2_mean')` → `0.845269087679269` (S38 s38_attempt_freq.npz; FK-saturating B2 sector floor).
- `get_constant('a_2_zeta')` → not a canonical-constants entry; confirmed from `lizzi-spectral-functional.md`: `a_2^ζ = 2776.165389` (the factor-3812-distinct spectral-zeta moment vs Gilkey a_2^SD=0.728235 — regulator-discipline anchor).
- `search_knowledge('A_s amplitude floor 3.02x Planck PERMANENT WALL')` → S83 CF23 HARDENED to PERMANENT WALL (3.02× Planck, near-floor + reduced M_Pl) ⇒ the 3.02× = +0.480 OOM Planck-MULTIPLE reading confirmed.
- `search_knowledge('A_s 3.15 OOM Route B Peter-Weyl 9.47 OOM Bogoliubov')` → S66 AMPLITUDE-NORM-66 (3.15 OOM Route-B-PW, FAIL marginal); S74 `s74_as_from_bogoliubov_output.txt` (`gap_OOM = 9.4716` Bogoliubov). Both legacy numbers confirmed exactly.
- `trace_entity('A_s amplitude floor')` → CF23 PERMANENT WALL + F_supp rate-limiter chain (S83/S84).
- **PRE-CLOSED check**: NO closure covers this gate. The S103 sqrt-cutoff functional that fixes n_s has NEVER been applied to A_s as a near-floor `exp(−ζ'(0))` functional; the three legacy numbers all used DIFFERENT functionals. **Gate genuinely open → proceeded to compute.** (Surfaced a FOURTH record number not in the plan triplet: S84 TD-canonical A_s=5.078e-9 = +0.384 OOM SCHEME-DEPENDENT, falsifier-rigor-registry Row 8 — cross-reported; the ambiguity is even wider than the plan's triplet, strengthening the case for ONE regulator-tagged number.)

**Verdict**: **INFO** (`sign_verdict=PASS · magnitude_verdict=INFO · regime_verdict=VALID` → composite INFO per the gate-verdicts.md collapse rule `magnitude==INFO ⇒ INFO`).

A SINGLE regulator-tagged number IS emitted under ONE named scheme — `gap_OOM = +6.008` (sqrt-cutoff, `a_n^{ζ}`, reduced M_Pl, near-floor) — so the *ambiguity over which functional is canonical* is retired. But the n_s-selected near-floor number lands **+6.008**, which is **5.53 OOM from the S83 +0.48 wall** (NOT the PASS criterion of ≤0.5 OOM) yet within **2.86 OOM of the nearest legacy reading (S66 Route-B)** (NOT a fourth >3-OOM-from-ALL FAIL value). The SIGN prediction (overproduction, `gap_OOM > 0`) is **confirmed** (substitution-chain Step 4). INFO is the pre-registered outcome for "single regulator-tagged number emitted but lands away from all legacy readings; the legacy-reconciliation is the deciding follow-up."

**Results**:

**Single regulator-tagged number (the deliverable):**
> **`gap_OOM = log10(A_s_computed / A_s_Planck) = +6.008`** (4 sig figs; publication_precision pin) · scheme **`sqrt-cutoff`** · regulator **`a_n^{ζ}`** · CLASS **FULL** · M_Pl **reduced** · convention **ABSOLUTE** · L_max **12**. `A_s_computed = 2.137e-3`.

**Decomposition `A_s = (M_KK/M_Pl_reduced)² × F_nearfloor`:**

| Piece | Value | log10 | Reading |
|:------|:------|:------|:--------|
| prefactor `(M_KK/M_Pl_reduced)²` | `9.3073e-4` | `−3.0312` | **DIMENSIONFUL** — ALL the weakness; the M_KK-normalization gap **G1** (the #1 standing gap, shared with Paasch). |
| `[lever] (M_KK/M_Pl_unreduced)²` | `3.7022e-5` | `−4.4315` | unreduced choice = a **1.40-OOM lever** (−3.031 vs −4.432); reduced is PINNED (cosmological A_s convention). |
| `F_nearfloor` (intensive) | `2.2961` | `+0.3610` | **DIMENSIONLESS** — n_s-selected sqrt-cutoff per-mode functional; INTENSIVE, same functional that fixes n_s; solid heat-kernel footing. |
| prefactor-only gap (F=1) | — | — | **+5.6466 OOM** (substitution-chain Step-4 anchor). |

**Near-floor block (PW-weighted spectral measure):** band `λ ≤ 2·E_B2_mean = 1.6905`, capturing **14,496 PW-weighted modes** across **19 Peter-Weyl sectors** (1124 block-level eigenvalues × outer multiplicity `dim(p,q)`); `λ_min = 0.8197`, FK floor `λ_floor = E_B2_mean = 0.8453`. The `abs_evals` per sector are the genuine Dirac block eigenvalues on `V_{(p,q)} ⊗ C^16` (16 = Spin(8) spinor rank, d=8); outer Peter-Weyl multiplicity = `dim(p,q)`. (Cache (4,4) sector MISSING, but `√C_2(4,4) ≫ 1.6905` band ceiling ⇒ cannot perturb the near-floor block — Friedrich-Bär floor argument.)

**FULL ζ'(0) functional determinant (a_n^{ζ}; regulator discipline load-bearing):**
- Direct EXACT finite-spectrum: `ζ(0)_nearfloor = Σ d_k = 14496`; `ζ'(0) = −Σ d_k ln(μ_k) = −11728.6717`; `log det' = −ζ'(0) = +11728.67` ⇒ raw `det' = exp(+11728.67) ≈ 10^5093.7` — **EXTENSIVE, overflow** (this is why the literal `exp(−ζ'(0))` is NOT the dimensionless functional: it carries the band cardinality).
- FULL live-zeta cross-check (Mellin-grid centered FD at s=0): `ζ'(0)_Mellin = −11728.6718`, residual `9.50e-5` vs direct ⇒ the two FULL evaluators agree (genuine Mellin-cone evaluator on the cached L12 eigenvalues, NOT the SCHEMATIC `_spectral_action_regulators.py` helper — **CLASS=FULL satisfied; no `-SCHEMATIC` suffix**).
- The **intensive** dimensionless functional under the sqrt-cutoff weight: `F_nearfloor = exp[ (Σ d_k w_k ln μ_k)/(Σ d_k w_k) ] = 2.2961`, `w_k = λ_k/λ_floor` (sqrt-cutoff weight `f(x)=√x ⇒ √(μ/Λ²)=λ/Λ`, floor-normalized). The per-mode geometric mean of μ under the SELECTED measure — the scale-free reduction appropriate to an intensive amplitude.

**Substitution-chain Step-4 SIGN read-off (overproduction):**
- `gap_OOM = log10(prefactor) + log10(F_nearfloor) − log10(A_s_Planck) = −3.0312 + 0.3610 − (−8.6778) = +6.008 > 0`. **SIGN = PASS** (overproduction confirmed; the substrate is LOUDER than Planck by ~6 OOM under this convention).
- Plan Step-4 caveat: to land at S83 wall (+0.48) needs `F ≈ 6.8e-6` (suppress 5.17 OOM); at S66 (+3.15) `F ≈ 3.2e-3`; at S74 (+9.47) `F ≈ 6.7e3`. **None is an intensive O(1) functional** — they are the extensive / full-spectral-weight / Bogoliubov normalizations. **Robustness cross-check:** four independent intensive definitions (unweighted geom-mean μ → 2.246; sqrt-cutoff-weighted geom-mean μ → 2.296; sqrt-cutoff geom-mean |λ| → 1.515; spectral-action `⟨|λ|⟩` → 1.507) ALL give `F = O(1)` ⇒ `gap_OOM ∈ [+5.82, +6.01]`, span 0.19 OOM. **Prefactor-dominated, NOT sensitive to the intensive-functional choice.**

**Three legacy numbers cross-reported (the ambiguity retired):**

| Reading | gap_OOM | dist from +6.008 | Provenance / why it differs |
|:--------|:--------|:-----------------|:----------------------------|
| **S83 3.02× PERMANENT WALL** | **+0.480** | 5.53 OOM | Planck-MULTIPLE; near-floor + reduced M_Pl; CF23 HARDENED. A Planck-MULTIPLE assertion (A_s/A_s_Planck=3.02), NOT the substrate-computed near-floor functional value. |
| **S66 Route-B PW** | **+3.150** | 2.86 OOM (nearest) | AMPLITUDE-NORM-66 FAIL(marginal); Route-B **FULL-spectral-weight** Peter-Weyl sum (not near-floor-restricted, not intensive). |
| **S74 Bogoliubov** | **+9.472** | 3.46 OOM | AS-BOGOLIUBOV-S74; 8-mode Bogoliubov amplitude, full fiber weight, different normalization chain (H_transit baked in per S76). |
| *[extra record]* S84 TD-canonical | +0.384 | — | AS-PIN-MAP-COMMIT TD-canonical; SCHEME-DEPENDENT (falsifier-rigor-registry Row 8); not in the plan triplet. |

**Which does the single number supersede, and why:** the n_s-selected near-floor INTENSIVE functional matches NONE of the three numerically — it is a FOURTH, distinct functional. What it *retires* is the **ambiguity over which functional is canonical**: the three legacy numbers are three DIFFERENT spectral functionals (Planck-multiple assertion / full-spectral-weight extensive sum / Bogoliubov chain), NOT three measurements of one quantity. The n_s-SELECTION criterion (the functional that fixes n_s must also fix A_s — functional-selection consistency) picks the **intensive near-floor sqrt-cutoff functional**, whose unambiguous value is **+6.008 OOM**, dominated by the M_KK-normalization prefactor (G1). The S83 +0.48 wall is a Planck-MULTIPLE statement at a different layer; it is not contradicted, it is a different object.

**Output 4-tuple:** `(value=gap_OOM=+6.008, scheme=AS-AMPLITUDE-FLOOR-NSFUNCTIONAL-sqrt-cutoff, convention=ABSOLUTE, L_max=12)` + `CLASS=FULL` + `M_Pl_choice=reduced` + `regulator_pin=a_n^{ζ}`.

**Dual-SHA (CANONICAL, latest non-superseded):** `audit_sha256=f85e981d1f74b3a3f1ec9e3e83a360a3c7386ce444476ceb666f1ccebb92f523` (over [script, canonical_constants.py, pinmap]); `content_sha256=bf2d0638813351d54a918489d37c574385b8a659bc78cc67fd4667f699e75d25` (over [script]). Supersedes the first emission `audit_sha256=73e0b9d8…` (Option A, gate-verdicts.md; prior line retained on disk; script-bug fix only — physics identical). **Schema-v2 3-tuple companion row:** `sign_verdict=PASS magnitude_verdict=INFO regime_verdict=VALID`.

**dual_prior re-allocation:** prior 0.55 Track_A (RESOLVED to S83 wall) / 0.45 Track_B (ambiguity functional-choice-deep). Outcome INFO (single number emitted, but >1.5 OOM from all legacy readings) → the value STANDS as the n_s-selected near-floor result, but the legacy-reconciliation is the deciding follow-up → **prior unchanged; flag the near-floor-vs-full-spectral-weight OOM gap (2.86 OOM to S66) as the next compute.** Net reading: the A_s amplitude is **prefactor-dominated (G1/M_KK gap)**; the dimensionless intensive functional is O(1) and robust; the weakness is entirely on the dimensionful axis, exactly as the substrate framing predicts.

**Substrate-physics assessment (PHONONIC):** `A_s` IS the loudness of the post-transit GGE acoustic interference pattern — not "density perturbations in expanding space." The arrow: `D_K near-floor eigenvalues {λ_k → λ_min=0.8453 at the FK-saturating B2 sector} → near-floor DOS ρ_E(λ) → n_s-SELECTED sqrt-cutoff weights it → intensive functional F_nearfloor=2.296 → A_s = (M_KK/M_Pl)² × F_nearfloor`. The decomposition is the whole point: the DIMENSIONLESS part (F_nearfloor, intensive, the same functional that fixes n_s) is on solid heat-kernel footing and robustly O(1); ALL the weakness is in the DIMENSIONFUL prefactor (M_KK/M_Pl)² = the M_KK-normalization gap **G1** (the #1 standing gap, shared with Paasch). The three legacy OOM numbers are NOT three measurements of one thing but three DIFFERENT spectral functionals applied to the same fabric; this gate picks the n_s-consistent intensive one and emits its single number (+6.008). Regulator discipline held: the functional determinant is an `a_n^{ζ}` object (ζ'(0)=−11728.67, zeta-scheme), NOT mixed with the Gilkey SD curvature polynomials (a_2^SD=0.728235; the a_2^ζ=2776.165389 factor-3812 warning honored). **CROSS-TRACK:** this investigation gate emits ONLY the value — NO `falsifier-master-inventory.md` row (that is `mack-cosmic-bridge` sole-writer on session-promotion).

**Artifacts:** `computations/investigation-3/inv3_w2_as_amplitude_floor.py` / `.npz` / `.png`; verdict in `computations/investigation-3/inv3_gate_verdicts.txt`.

---

### §W2-4. INV3-W2-4-WEYL-REMAINDER-GEODESIC-STATIONARITY (spectral-geometer)

**Status**: COMPLETED
**Gate ID**: `INV3-W2-4-WEYL-REMAINDER-GEODESIC-STATIONARITY` (verdict-line short form `INV3-W2-4`; descriptive suffix in `scheme=`)
**Trigger**: `[SIGN]` (schema-v2 3-tuple REQUIRED; carried)
**Classification**: **GEOMETRIC** (the Weyl-law remainder + closed-geodesic length spectrum are properties of the fabric's spectral geometry)
**Gate type**: `compute`
**Agent**: `spectral-geometer`
**Hypothesis**: the oscillatory remainder `N(λ)−N_Weyl(λ)` of the `D_K(τ)` counting function (oscillation periods set by closed-geodesic lengths via the Selberg/Gutzwiller/Berry-Tabor trace formula) has a shortest-closed-geodesic length `L_γ,min(τ)` STATIONARY (`dL_γ,min/dτ=0`) at a preferred `τ*` COMMENSURATE with `τ_fold=0.190` — a NON-VARIATIONAL geometric route to `τ_fold` the failed S95 one-loop/variational corridors never tried.
**Plan reference**: `sessions/investigation/investigation-3/investigation-3-plan-w2.md` §W2-4 (coroot-lattice/Casimir-metric closed form, τ_fold commensurability band).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

| # | Artifact | Path | must_contain → status |
|:--|:---------|:-----|:----------------------|
| 1 | script | `computations/investigation-3/inv3_w2_weyl_remainder_geodesic.py` | `from canonical_constants import` ✓ (`import *` + explicit `PI, tau_fold, Vol_SU3_Haar`) · `print_verdict_payload` ✓ (def + call) |
| 2 | data | `computations/investigation-3/inv3_w2_weyl_remainder_geodesic.npz` | exists ✓ (`taus`, `L_min_mean`, `L_min_c2`, `dL_dtau`, `m_track`, `stationary_taus`, anchor Hessians, FFT x-check arrays, verdict fields) |
| 3 | plot | `computations/investigation-3/inv3_w2_weyl_remainder_geodesic.png` | exists ✓ (4-panel: `L_γ,min(τ)` both conv · `dL/dτ` stationarity · winding `m(τ)` · method-(i) FFT @ τ=0.19) |
| 4 | verdict | `computations/investigation-3/inv3_gate_verdicts.txt` | `^INV3-W2-4:.* audit_sha256=[a-f0-9]{64}` ✓ + dual-SHA companion row + schema-v2 3-tuple row |
| 5 | wp_section | this section | `Status:.*COMPLETED` ✓ · `Verdict:.*(PASS\|FAIL\|INFO)` ✓ · `Output Artifacts` ✓ · `MCP Pre-Compute Audit` ✓ |

Verified by content presence (regex), not line/byte count. Verdict line (full): `INV3-W2-4: FAIL -- value='verdict_basis=NO_stationary_point;n_stationary=0;n_stationary_within_eps=0;monotone_dL=True;dL_dtau_at_fold=-5.20139;min|dL/dtau|=4.13919@tau=0.15000_vs_eps=1e-03;L_min_at_fold=21.26821;L_min(0.15)=21.45510;L_min(0.23)=21.03958;tau0_anchor_mean=4pi_sqrt3=21.76559_C2=4pi=12.56637;winding=(-1,-1)_switches=0;hess_saturated_mpq4eq5=True(1.7e-15);L12cache_validated=True(relmax=2.0e-14);FFT_xcheck_relmax=0.617_TRUNC-INFLUENCED-W7-2;commens_min|dL|_pt=0.2105' scheme=Weyl-leading-WEYL-REMAINDER-GEODESIC-STATIONARITY convention=ABSOLUTE L_max=4-operational-Casimir-saturated(plan-L12-redundant-for-quadratic-Hessian) audit_sha256=45d1cfa8a9a9d603709f1b1fb420c1182f96fdb47b3f923154c57deab4d4871c content_sha256=1d6041b52519e724e1afe2ab29194247b30166e9d38fb214d2206ecf122c9725 schema_version=S84+`

**MCP Pre-Compute Audit** (run BEFORE writing the script; `.claude/rules/knowledge-index-usage.md`):

| Query | Salient return | Branch decision |
|:------|:---------------|:----------------|
| `search_knowledge('Weyl law oscillatory remainder closed geodesic length spectrum trace formula')` | S105 W7-1 trace-formula anchor; eq `N(λ)=Seeley-DeWitt + Σ_orbits A_γ exp(i L_γ λ)` (Duistermaat-Guillemin); s61 weyl_law/trace_formula_geometric precedents. | Confirms the governing structure (trace formula links remainder oscillation periods to geodesic lengths). |
| `search_knowledge('closed-geodesic length coroot winding lattice Casimir metric S105 torus theta')` | `S105-W7-2-LENGTH-SPECTRUM-FT: PASS` (dominantL=124.26, **primitiveL=12.5664=4π**, deltaL=1.1595, tau_fold-peaks "truncation-influ[enced]"); `S105-W7-4-GEODESIC-COMMENSURABILITY: FAIL` (squared-length **ratios**). | Provides the exact coroot-lattice closed form + the W7-2 truncation caveat I reuse + report. |
| `search_knowledge('tau_fold geometric selection non-variational route S95 one-loop t* FAIL Berry-Tabor')` | `S95-W2-1-T-STAR-ONELOOP-ORIGIN: FAIL` (variational corridor CLOSED); `S105-W7-3-BERRY-TABOR-MATCH: FAIL` (match_frac=0.1579, **`primitive_L_pred_tau_fold=21.2682`**). | The variational/one-loop τ_fold corridors this gate routes AROUND are CLOSED; W7-3 gives the τ_fold primitive length I reproduce. |
| `search_knowledge('S106 W1 commensurability reconciliation length-rematch ...')` | `S106-W1-LENGTH-REMATCH-P2: FAIL` (match_frac_L14/L16=0.0). | Prior geodesic work tested **length-RATIO commensurability**, not **τ-stationarity** — distinct question. |
| `trace_entity('closed geodesic length spectrum')` | coroot/winding lattice = trace-formula conjugate variable setting closed-geodesic LENGTHS (S106 eq_7513). | Confirms the lattice = the geodesic-length-side object. |
| `get_constant('tau_fold')` = **0.19** (CONST-FREEZE-42, not superseded) · `get_constant('Vol_SU3_Haar')` = **1349.74** (S44 Weyl-corrected) · `get_constant('M_KK')` = 7.428660036284456e16 · `get_constant('d_s_fold_window_sigma')` = 1.4005 | canonical confirmed. | Commensurability target + Weyl-term volume pinned. |
| **BRANCH-CHECK (NOT pre-closed)** | The prior geodesic body (S105 W7-1/2/3/4, S106 W1) addresses commensurability of geodesic LENGTHS (length-ratio rationality; whether the τ_fold-predicted length matches the measured dominant length). | This gate is the **structurally distinct** question — **stationarity of `L_γ,min(τ)` in τ** (`dL/dτ=0`), a τ-derivative/extremality test. The S105/S106 FAILs do NOT close it. REUSE the W7-1/W7-3 exact coroot closed form (`L_m=2π√(mᵀ(Hess(E)/2)⁻¹m)`, 4π at τ=0) but apply it across a τ-scan for the first time. PROCEED. |

**Verdict**: **FAIL** — `sign=FAIL magnitude=FAIL regime=VALID` (composite-collapse: `regime=VALID ∧ sign=FAIL ⇒ FAIL`). `L_γ,min(τ)` is **monotone decreasing** with **no stationary point** anywhere in [0.15, 0.23]; the non-variational geometric route to `τ_fold` joins the closed S95 variational corridors. `audit_sha256=45d1cfa8a9a9d603709f1b1fb420c1182f96fdb47b3f923154c57deab4d4871c` `content_sha256=1d6041b52519e724e1afe2ab29194247b30166e9d38fb214d2206ecf122c9725`. 4-tuple `(scheme=Weyl-leading-WEYL-REMAINDER-GEODESIC-STATIONARITY, convention=ABSOLUTE, L_max=4-operational-Casimir-saturated)`.

**Results**:

*Governing structure (heat-trace / trace-formula first).* The closed-geodesic length spectrum is the geometric side of the substrate's own trace formula (S105 W7-1 PASS: spectral Peter-Weyl side = coroot-Poisson dual to <1e-9 at τ=0). On the Manakov-integrable Jensen geodesic flow (S54), the Berry-Tabor closed-orbit length for winding `m∈Z²\{0}` is the coroot-lattice closed form
> **L_m(τ) = 2π·√(mᵀ M(τ)⁻¹ m)**, with **M(τ) = Hess(E(τ))/2** the energy-Hessian quadratic form of the Dirac-square level surface `E(p,q;τ) = ⟨|λ(p,q;τ)|²⟩_(p,q)`. `L_γ,min(τ) = min_m L_m(τ)`.

*Casimir-bound feasibility (operational deviation from plan L_max=12 — disclosed per `v3-closure-recovery.md` Class-1 boundary).* The level surface is **EXACTLY quadratic at every τ** (R²=1.00000000), so its Hessian is L_max-SATURATED: `Hess(mpq=4) == Hess(mpq=5)` to **1.7e-15** at τ_fold. The plan's L_max=12 is structurally redundant for this Hessian-determined observable. The operational `mpq=4` Hessian was VALIDATED against the **full L12 caches** at the three bracket anchors (s92 τ=0.18, s84 τ=0.19, s92 τ=0.20): max relΔ = **1.95e-14** (≤ 2% pin), `L_op == L_cache` to 4 d.p. at each. This satisfies the math-scripts.md Friedrich-Bär/Casimir-bound pre-check: `L_max_operational=4` reproduces the geodesic observable bit-for-bit, making the 401-point τ-scan feasible (~0.5 s/τ; ~204 s total vs infeasible at L12).

*τ=0 anchor (exact, two conventions; Sage-QQ verified).* `L_γ,min(0)` with the action-variable Casimir surface `E=C2(p,q)` is **4π = 12.5664** at winding `m=(−1,−1)` — bit-exact match to the W7-2/W7-3 coroot primitive (`m=(−1,−1)`, `mᵀM⁻¹m=4`). The Dirac-square sector-mean surface (the actual D_K² spectrum the cache stores) gives `L_γ,min(0) = 4π√3 = 21.7656`, because `Hess(⟨|λ|²⟩) = Hess(C2)/3` EXACTLY (the Fegan `|λ|²=(1/6)(C2_μ+C2_pq)+1/4`, S105 W7-1). The two conventions differ only by the overall length scale √3; **the stationarity verdict is scale-invariant** (a √3 factor moves no zero of `dL/dτ`).

*Stationarity scan (PRIMARY = method (ii), Dirac-square mean; 401 τ-points in [0.15, 0.23]):*

| τ | L_γ,min(τ) [mean conv] | winding m | R² |
|:--|:--|:--|:--|
| 0.15000 | 21.45510 | (−1,−1) | 1.00000000 |
| 0.18200 | 21.30899 | (−1,−1) | 1.00000000 |
| **0.19000 (fold)** | **21.26821** | (−1,−1) | 1.00000000 |
| 0.20000 | 21.21490 | (−1,−1) | 1.00000000 |
| 0.23000 | 21.03958 | (−1,−1) | 1.00000000 |

- `dL_γ,min/dτ ∈ [−6.2194, −4.1392]` — **all-negative, sign constant** ⇒ monotone DECREASING.
- **Zero** sign-change zeros of `dL/dτ`; **0** stationary points with `|dL/dτ| ≤ eps_stationary=1e-3`.
- `min|dL/dτ| = 4.1392` at τ=0.150 — **~3.6 orders of magnitude above** the `eps_stationary=1e-3` bar; no near-stationary point in the bracket either.
- `dL/dτ|_{fold} = −5.2014` (the shortest closed geodesic is SHRINKING through τ_fold at rate ≈5.2 per unit τ).
- Winding vector **constant `m=(−1,−1)`, 0 switches** across the whole scan ⇒ `L_γ,min(τ)` is smooth, **no kink/cusp** that could fabricate a stationary point; `det Hess > 0` throughout.

*Substitution-chain Step-5 SIGN read-off (with substituted numbers).* Step 4: `L_γ,min(τ)=2π√(mᵀM(τ)⁻¹m)`, `M=Hess(E)/2`. At fold `Hess=[[0.232738,0.116369],[0.116369,0.232738]]`, `m=(−1,−1)` ⇒ `mᵀM⁻¹m = (2π·21.268/2π)² = 11.46`, `L=2π√11.46=21.268` ✓. Step 5: the diagonal Hessian entry `2a(τ)` INCREASES with τ across the bracket (0.231632→0.233909 over 0.18→0.20; the Jensen `e^{−2τ}` su(2) factor stiffens the level surface), so `M⁻¹` shrinks and `L_γ,min` DECREASES — `dL/dτ < 0` everywhere. **Predicted-structure check: a stationary point requires `dL/dτ` to change sign; it does not.** ⇒ `sign_verdict = FAIL` (predicted stationary structure absent), `magnitude_verdict = FAIL` (`min|dL/dτ|=4.14 ≫ 1e-3`), `regime_verdict = VALID` (closed form exact, R²=1, Hessian L_max-saturated + cache-validated throughout the window).

*Method (i) FFT cross-check (honest truncation caveat).* The Weyl-subtracted counting remainder `N(λ)−N_Weyl(λ)` FFT'd at the three anchors gives dominant length L≈8.13–8.27 (SNR 84–121), differing from the analytic `L_ii≈21.2–21.3` by relΔ≈0.61 — method (i) does NOT pass the 5% cross-check. This is the **known S105 W7-2 truncation-influence** (`n_lambda_range_robust=0` at L_max=12; the compressed lambda-support `delta_L≈1.16` cannot resolve clean closed-geodesic lengths from the FFT). Reported transparently but NOT the stationarity basis; the analytic coroot closed form (method (ii)) — exact, R²=1, Hessian-saturated and L12-cache-validated — is PRIMARY. Notably the FFT dominant length is ALSO monotone in τ (8.270→8.121), reinforcing no-stationary-point under both extractions.

*Solution-space (FAIL_meaning).* Closed-geodesic-length stationarity does NOT select `τ_fold=0.190`. `L_γ,min(τ)` is monotone-decreasing across the entire bracket with no extremum — the substrate's shortest closed geodesic is not extremal at the fold (it is shrinking, `dL/dτ|_{fold}=−5.20`). The **A4-moduli geometric-selection corridor is CLOSED**: the non-variational geometric route joins the failed S95 one-loop / variational corridors (`S95-W2-1-T-STAR-ONELOOP-ORIGIN: FAIL`). `τ_fold` remains **dynamically (transit-physics) or empirically pinned** — the mechanism-chain dynamical-relaxation route is the surviving live corridor for "why τ_fold=0.190". **dual_prior re-allocation**: outcome FAIL ⇒ **Track_A=0.15, Track_B=0.85** (Reading_NO-GEOMETRIC-ROUTE confirmed — the prior-favored reading).

*Substrate-first framing.* The closed geodesics ARE the periodic orbits of the fabric's own internal geometry (the SU(3) coroot lattice in the Casimir metric, S105 W7-1), not paths in an external container; τ IS the substrate's intrinsic Jensen TT-deformation parameter (Level-2 moduli-deformation substrate-IS). The result is a clean negative boundary on the moduli-space: the fold is not a geodesic-length extremum of the substrate's own length spectrum. This is a genuine constraint (it delimits what the geodesic geometry can/cannot select), not a weakness — a FAIL closes a corridor in the τ_fold-derivability constraint map.

---

## Wave 2 Synthesis (team-lead)

Wave 2 took heat-kernel machinery to the framework's one structurally-weak axis — the dimensionful/extensive observables (M_KK normalization, A_s amplitude, τ_fold selection). Four gates closed: **1 PASS (W2-2), 1 INFO (W2-3), 2 FAIL (W2-1, W2-4)**. The four outcomes are unusually coherent and point one way.

**The intensive axis is solid; every route to an emergent dimensionful scale closed.** W2-2 PASS establishes that the dimensionless structure is *rigid*: Tr D_K² is strictly monotone in τ (min adjacent gap 0.6535, nine OOM above tolerance), so the D_K² spectrum reconstructs the Jensen geometry — Connes-reconstructible at L_max=3, operational evidence for the §VII.BR Schur-rigidity STAGE-3-PERMANENT theorem. W2-3 confirms the A_s amplitude's dimensionless part is robust (F_nearfloor=2.30, span 0.19 OOM across four independent definitions). But the two attempts to make the *dimensionful scale itself* emergent both FAILed: W2-1 (the d_s-flow integral does not transport K→K* — the finite-spectrum UV topology is d_s(σ→0)=0.003, not the continuum 8, so the integral has the wrong sign and magnitude; no σ_UV window rescues it, frac_in_band=0) and W2-4 (the shortest closed geodesic length is monotone in τ, dL/dτ|_fold=−5.20, with zero stationary points — geodesic-length extremality does not select τ_fold). Both join the closed S95 one-loop/variational corridors. W2-3's decomposition pins *why*: A_s = (M_KK/M_Pl)² × F_nearfloor, with all the weakness in the (M_KK/M_Pl)²=9.3×10⁻⁴ prefactor — the G1 M_KK-normalization gap.

### What Changed

#### (a) Numerical revisions
- A_s OOM ambiguity `{3.02× (+0.48), 3.15 OOM, 9.47 OOM}` → **single n_s-selected number gap_OOM = +6.008** (regulator a_n^ζ, sqrt-cutoff, reduced M_Pl); a fourth legacy record (S84 TD-canonical +0.384, scheme-dependent) was surfaced, widening the prior spread and strengthening the one-number case.
- ζ'_{D_K}(0) = −11728.6717 (direct finite-spectrum) vs −11728.6718 (Mellin-grid), residual 9.5e-5 — FULL live-zeta evaluator agreement (CLASS=FULL confirmed, no SCHEMATIC helper).
- d_s-flow integral I = −0.200440 vs target ln(K/K*)=3.134994 (rel dev 93.6%, sign-flipped); L_γ,min(τ_fold)=21.268, dL/dτ|_fold=−5.20.

#### (b) Structural changes
- **UB-1 corridor (d_s-flow as scale-transport map): CLOSED.** The dimensionful K-pivot is NOT an emergent output of the intensive d_s flow on the finite truncation; the K/K* ratio stays a free parameter.
- **A4-moduli geometric-selection corridor (geodesic-length stationarity → τ_fold): CLOSED.** τ_fold remains dynamically (transit-physics) or empirically pinned; mechanism-chain dynamical relaxation is the surviving live route.
- **Isospectral rigidity at L_max=3: established** — "one can hear the Jensen geometry" at this truncation (Connes-reconstructible; §VII.BR operational support).
- **A_s ambiguity retired to one functional**: the three legacy OOM numbers are exposed as three *different spectral functionals* on one fabric, not three measurements of one quantity; the n_s-selection criterion picks the intensive near-floor functional.

### W2 → W4 hand-off (M_KK-derivability workshop inputs)
- **Sub-question (a)** [does NNU rank-1 *prove* M_KK underivability, or merely confirm one external pin?]: W2-1 and W2-4 supply two independent spectral-geometer-side data points — both candidate routes to a *substrate-internal emergent scale* came back **closed**. This materially strengthens Reading-S (scale-free; M_KK irreducibly external) without, by itself, proving in-principle underivability (the integer-structure route of Reading-P is untouched by these two negatives — that is W3-4's domain).
- **Sub-question (b)** [does Paasch fix m_p without a hidden scale?]: W2-3's A_s = (M_KK/M_Pl)² × intensive shows A_s, M_KK, M_Pl are **not independent** — a clean A_s adds no degree of freedom; any scale-free derivation of m_p must produce the single M_KK weight from dimensionless input alone. This is the spectral-geometer-side framing the workshop's falsifier-(i) test sharpens.
- W2-2 (rigidity) supports Reading-S's premise that the scale-free triple predicts *all* the dimensionless Ô's exactly — the dimensionless content is internally complete and rigid.

### Effected In-Session (non-math)
**None executed in-investigation** — every non-math item is session-track and routes to `/rclab-investigate --investigation 3` close (track-local boundary):
- [→investigate] Session-promotion of the single A_s number (gap_OOM=+6.008) to a `falsifier-master-inventory.md` row is **mack-cosmic-bridge sole-writer on session-promotion** (`feedback_mack-bridge-role.md`) — NOT written by this investigation (the W2-3 gate correctly emitted value-only, no inventory row).
- [→investigate] Anchor-provenance facts surfaced by W2-1 (K_pivot=2.0 M_KK is atlas-04 C2 **BROKEN-WITH-LIVE-RESEARCH-PATHWAY**, never derived; K*=0.087 is atlas-07 S51 DERIVED and DISTINCT from `canonical_constants.py K_star=1.3130`, the S84 3He-B anchor) are session-track register notes.

## Carry-Forward Computations

Genuine future compute (4-field) → consumed by `/rclab-investigate --investigation 3`. The two FAILs (W2-1, W2-4) CLOSE their corridors in-investigation (no re-run is a carry-forward — iterate-until-PASS is forbidden); the items below are a DIFFERENT observable (CF-A), a reconciliation the INFO explicitly defers (CF-B), and a session-promotion (CF-C).

### CF-INV3-W2-A — Scale-transport under the energy-axis-windowed / continuum-extrapolated d_s
| Field | Spec |
|:------|:-----|
| **What** | Re-pose the scale-transport test with a DIFFERENT observable than the closed UB-1 form: the S94 energy-axis windowed d_s(σ_*)=2σ_*⟨λ²⟩ and/or a continuum-extrapolated (L_max→∞ Richardson) d_s, testing whether the drop-from-8 topology and a positive e-fold integral I ≈ ln(K/K*) are recovered. NOT a re-run of the FAILed finite-truncation d_s-flow (that corridor is closed). |
| **Inputs** | `inv3_w2_ds_flow_scale_transport.py`; S94 γ_E / energy-axis-DOS machinery; L12 (+ higher-L caches if available for extrapolation); K=2.0, K*=0.087 M_KK. |
| **Gate** | \|I\| matches ln(K/K*)=3.135 within 10% **with correct sign I>0** under the windowed/extrapolated d_s. |
| **Effort** | ~1 wave-equiv (new observable assembly + L_max extrapolation). |

### CF-INV3-W2-B — A_s near-floor vs full-spectral-weight legacy reconciliation
| Field | Spec |
|:------|:-----|
| **What** | Derive why the n_s-selected intensive near-floor A_s (gap_OOM=+6.008) differs from the S66 Route-B full-spectral-weight reading (+3.15 OOM) by 2.86 OOM — band-cardinality / spectral-support structural accounting (the deciding follow-up the W2-3 INFO names). |
| **Inputs** | `inv3_w2_as_amplitude_floor.py` (near-floor); S66 Route-B Peter-Weyl full-spectral-weight machinery; L12 fold cache; `n_s_FW_sqrt_cutoff=0.959`. |
| **Gate** | the 2.86-OOM offset is structurally accounted to within 0.5 OOM (named spectral-support cardinality reason), OR a named structural obstruction. |
| **Effort** | ~1 wave-equiv. |

### CF-INV3-W2-C — Session-promote isospectral-rigidity (L=3) as §VII.BR operational evidence
| Field | Spec |
|:------|:-----|
| **What** | Re-run the L_max=3 isospectral-rigidity test as a session-track gate and land it as operational support for the §VII.BR Schur-rigidity STAGE-3-PERMANENT theorem ("the D_K² spectrum reconstructs the Jensen geometry; Connes-reconstructible at L=3"). |
| **Inputs** | `inv3_w2_isospectral_rigidity_l3.py`; geometric a_n^lattice machinery; canonical `a_2^SD=0.728235`. |
| **Gate** | empty degeneracy set (PASS) reproduced on the session track; Tr D_K² strict monotonicity confirmed. |
| **Effort** | ~0.5 wave-equiv (script exists; session-track re-run + §VII.BR registry note). |

## Constraint-Map Updates

| Date | Mechanism / gate | Prior state | New state | Reason |
|:-----|:-----------------|:------------|:---------|:-------|
| 2026-06-15 | UB-1 d_s-flow-as-scale-transport-map | OPEN (candidate emergent K-pivot) | CLOSED in pre-registered form | W2-1 I=−0.200 vs 3.135 (sign+magnitude FAIL); finite-spectrum d_s(σ→0)=0.003 not 8; frac_in_band=0 |
| 2026-06-15 | A4-moduli geodesic-stationarity τ_fold selection | OPEN (candidate non-variational route) | CLOSED | W2-4 L_γ,min monotone, dL/dτ\|_fold=−5.20, 0 stationary points (joins S95 variational corridors) |
| 2026-06-15 | A_s amplitude OOM ambiguity (3.02×/3.15/9.47) | OPEN (3-way scheme ambiguity) | retired to one n_s-selected number +6.008 (INFO) | W2-3 functional-selection consistency; weakness localized to the (M_KK/M_Pl)² prefactor (G1) |
| 2026-06-15 | Isospectral-non-isometric τ-pair (Jensen TT, L=3) | untested | NONE EXISTS — rigidity holds (Connes-reconstructible) | W2-2 Tr D_K² strictly monotone; empty degeneracy set across 2,001,000 pairs |
| 2026-06-15 | M_KK normalization gap (G1) | #1 standing gap | unchanged; two emergent-scale routes (W2-1, W2-4) closed → strengthens scale-free reading for W4-1 (a) | W2 dimensionful-axis sweep |

## Files Produced

| Gate | Script (`computations/investigation-3/`) | Data (.npz) | Plot (.png) | Verdict | audit_sha256 (head) |
|:-----|:------------------------------------------|:------------|:------------|:--------|:--------------------|
| INV3-W2-1 | inv3_w2_ds_flow_scale_transport.py | ✓ | ✓ | FAIL | c31277d5… |
| INV3-W2-2 | inv3_w2_isospectral_rigidity_l3.py | ✓ | ✓ | PASS | ba8d46af… |
| INV3-W2-3 | inv3_w2_as_amplitude_floor.py | ✓ | ✓ | INFO | f85e981d… (supersedes 73e0b9d8…, Option A) |
| INV3-W2-4 | inv3_w2_weyl_remainder_geodesic.py | ✓ | ✓ | FAIL | 45d1cfa8… |

(Verdict ledger: `computations/investigation-3/inv3_gate_verdicts.txt`.)
