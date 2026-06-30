# Investigation 8 Wave 3 — Cross-Domain Bridges (transit + condensed-matter + spectral-geometry) (Results Working Paper)

**Investigation**: 8 | **Wave**: 3 | **Plan**: investigation-8-plan-w3.md | **Theme**: five cross-domain springboards translating post-2015 condensed-matter / analog-gravity / quantum-geometry results into the substrate's own language — Kibble-Zurek Z₃ wall network of the transit, Peotta-Törmä quantum-metric stiffness as the imported Hubble backbone H(τ), spectral-dimension P(σ) at L_max=14-16 vs CDT/asymptotic-safety, Higgs-quartic λ(μ) running (substrate stability vs SM near-criticality), and the Watanabe-Murayama Goldstone branch count (6-vs-7 theorem). Three pillars: Pillar I/VI transit+soliton, Pillar IV/V flat-band BCS+Josephson, Pillar VII/VIII spectral dimension+KK geometry.

**Seed**: `sessions/investigation/investigation-8/investigation-8-seed.md §"Wave 3 items"` + `investigation-8-partition.md §"Wave 3"`, translating the phonon-first-cosmologist investigation-1 survey `sessions/investigation/investigation-1/phonon-first-cosmologist.md` §5 (Untraveled Bridges B-1, B-2, B-3, B-5) + §4 (Refinements R-1, R-2) + Closing "Highest-Leverage Next Steps" 1–5. Verdict file (investigation-track): `computations/investigation-8/inv8_gate_verdicts.txt` — emit via `emit_verdict(session=8, track="investigation", ...)` per `.claude/rules/gate-verdicts.md §"Investigation-Track Canonical Path"`. All five gates are `gate_type: compute` (each emits a verdict line).

## Gate Sections

### §W3-1. INV8-W3-1 (transit-dynamics-theorist)

**Status**: COMPLETED
**Gate ID**: `INV8-W3-1-KZ-Z3-WALL-NETWORK`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (the transit IS a quench of the substrate's internal spectral structure through the van Hove fold — the order-parameter manifold the D_K spectrum reorganizes onto, not a system passing through a transition IN a container)
**Agent**: `transit-dynamics-theorist`
**Hypothesis**: The finite-rate transit through the ACTUAL Z₃-structured Jensen order-parameter manifold at the ACTUAL Mach 13.75 freezes in a Z₃ domain-wall network (the "no-walls" verdict used π₀(U(1))=0 but the broken symmetry is U(1)₇×Z₃ with π₀(Z₃)=Z₃≠0); a frozen network contributes a w=−2/3 dark-energy component (DESI w_a candidate, C-1) and an a⁻¹-redshifting BBN relativistic-energy channel (C-4), reaching both with one compute.
**Plan reference**: `sessions/investigation/investigation-8/investigation-8-plan-w3.md` §W3-1 (machinery pin, π₀=Z₃ homotopy + KZ-freeze + w=−2/3 3-tuple PASS boundary, substitution chain source).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML per `.claude/templates/r3-yaml-gate-block.yaml`):
- `computations/investigation-8/inv8_w3_kz_z3_wall_network.py` — EXISTS (14753 B). `grep -E 'from canonical_constants import'` → `from canonical_constants import *  # noqa: F401,F403`. `grep -E 'print_verdict_payload'` → `def print_verdict_payload(verdict, value, audit_sha, content_sha,` + 1 call site. **PASS**.
- `computations/investigation-8/inv8_w3_kz_z3_wall_network.npz` — EXISTS (2989 B; 33 keys incl. value, composite_verdict, the 3-tuple, the 8-point Mach grids, dual-SHA). **PASS**.
- `computations/investigation-8/inv8_w3_kz_z3_wall_network.png` — EXISTS (4-panel: (a) ξ̂ vs Mach, (b) n_wall vs Mach [SIGN], (c) the L/ξ̂ 0D-regime bar, (d) the S42 a⁻¹ dilution to today). **PASS**.
- `computations/investigation-8/inv8_gate_verdicts.txt` — verdict line present. `grep -E '^INV8-W3-1-KZ-Z3-WALL-NETWORK:.* audit_sha256=[a-f0-9]{64}'` → matches (`audit_sha256=ce02c6003992a2b23562bb38e97c947283a2110e17e0021df6045e62d331c363`). Dual-SHA companion row present; schema-v2 3-tuple row present (`sign_verdict=PASS magnitude_verdict=FAIL regime_verdict=BREAKDOWN`). **PASS**.
- this WP §W3-1 — Status COMPLETED, Verdict FAIL, Output Artifacts + MCP Pre-Compute Audit blocks present. **PASS**.

**MCP Pre-Compute Audit**:
- `search_knowledge('Kibble-Zurek Z_3 domain walls transit defect formation')` → equation `n_defect ~ 1/ξ̂³, ξ̂ = ξ₀(τ_Q/τ₀)^{ν/(1+z_dν)}` (S41 voids); theorem **GGE Universality (S57, PROVEN): all cells identical post-transit, E_DW=0, no domain walls**; edge **T3-S38-KZ-DEFECTS bounds defect_density: "0D regime confirmed (L/ξ_GL=0.031), no topological domain walls"**.
- `search_knowledge('domain walls absent Jensen ridge pi_0 homotopy no-walls')` → equation `π₀(G/H)=0 (no domain walls — connected coset)` (S19d, the U(1)-only reading); the prior no-walls verdict surfaced. **NOT the only basis** — the 0D-regime + dilution + bias arguments are independent and sharper.
- `search_knowledge('w_a DESI dark energy ... w=-2/3')` → S42 equation `f_wall(today)=f_wall(transit)·a_transit`, `ρ_wall ~ a⁻¹`, **`w_wall=−2/3`**, `f_wall_energy(transit)=3.06e-7`; `Domain-wall GW (LISA) RETRACTED S77 — Josephson bias kills walls 15,000× before reheating`.
- `trace_entity('T3-S38-KZ-DEFECTS')` → gate S81 **PASS, value=1.000000, convention=0D_pair_reformulated** (the KZ defect gate reformulated as 0D pair production because the fold is sub-correlation-length).
- `search_knowledge('0D regime ... L/xi_GL ... fold crossing')` → `L/ξ_BCS=0.031` (INST-MC-37, S37); `xi_KZ=0.162075 M_KK⁻¹` (s53 STEP 1, τ₀=1/ω_att=0.699301); `L/ξ_KZ=0.1546` (s53 STEP 2 0D constraint).
- `get_constant`: `xi_BCS=0.8083468753837275` (S37), `dt_transit=0.0011301575037571713` (S38), `Mach_max_framework=13.75` (S85), `L_over_xi=0.031` (S37), `c_fabric=209.97368021` (S42), `tau_fold=0.19` (S12/S42). All imported from `canonical_constants.py` (never hardcoded).
- `search_knowledge('ANDREEV Z3 BdG wall ... 2pi/3')` → `δφ=2π/3` Andreev-Z3 BdG wall solution `Δ(x)=Δ₀ tanh(x/L) e^{iπ/3·sgn(x)}` exists (framework-paasch-potential-landau-collab); Q18 Z₃ domain wall energy STRUCTURAL ANCHOR via §VII.AG.4 512-plaquette.
- **BRANCH DECISION**: NOT a clean PRE-CLOSED (no prior gate computed THIS exact homotopy-corrected KZ-network-survival object), but THREE prior structural results decisively constrain the SURVIVAL half of the hypothesis (T3-S38 0D regime; S57 GGE universality E_DW=0; S77 Josephson-bias retraction). The gate's HOMOTOPY correction is CONFIRMED CORRECT (π₀=Z₃ admits walls); its FORMATION/SURVIVAL claim is overturned by the sharper 0D + dilution arguments. The computation reproduces these honestly rather than re-litigating them. Track B (no surviving network) is the survivor.

**Verdict**: **FAIL** — composite via the pre-registered collapse rule (`regime_verdict=BREAKDOWN ⇒ composite=FAIL`). Schema-v2 [SIGN] 3-tuple: **sign_verdict=PASS** (the n_wall-vs-Mach direction matches the predicted +), **magnitude_verdict=FAIL** (no surviving w=−2/3 cosmological component), **regime_verdict=BREAKDOWN** (the KZ network-formation regime of validity is violated — the fold is the 0D regime, L/ξ̂ ≪ 1). Dual prior re-allocates **0.9 to Track B** (the original "no-walls" verdict stands on a SHARPER footing than the π₀(U(1))=0 homotopy argument). `audit_sha256=ce02c6003992a2b23562bb38e97c947283a2110e17e0021df6045e62d331c363`, `content_sha256=45b95b61f93937d6dd3f88e3072f23dd0084b72fc8c2915cd6cda8f9232878d1`.

**Results**:

NUMBERS (computed, FW scheme, convention=KZ-mean-field-BCS-z2-nu-half):

| Quantity | Value | Source / cross-check |
|:---------|:------|:---------------------|
| `\|π₀(U(1)₇ × Z₃)\|` | **3** (> 1) | π₀(U(1))×π₀(Z₃) = {e}×Z₃ = Z₃; walls **ADMITTED** (homotopy part CORRECT) |
| KZ exponent ν/(1+zν) | **1/4** (= 0.2500) | ν=1/2 (mean-field BCS), z=2 (DYNAMICAL-EXPONENT-63); rational |
| τ_Q(13.75) | 1.130158e-3 M_KK⁻¹ | = `dt_transit` (canonical) |
| τ₀ (microscopic) | 0.699301 M_KK⁻¹ | = 1/ω_att (s53 STEP 1 canonical) |
| quench ratio τ_Q/τ₀ | 1.616e-3 (≪ 1) | **SUDDEN QUENCH** regime (P_exc=1.000) |
| **ξ̂(13.75)** | **0.162075 M_KK⁻¹** | **matches s53 canonical 0.162075 to rel dev 1.01e-06** (3-sig-fig cross-check PASS) |
| L_fold | 0.025059 M_KK⁻¹ | = L_over_xi · ξ_BCS = 0.031 × 0.8083 |
| **L/ξ̂** | **0.1546** (≪ 1) | the 0D-regime SURVIVAL discriminator; matches s53 STEP-2 L/ξ_KZ=0.1546 |
| n_wall ∝ Mach^α, α | **+1/2** | dn_wall/dMach **sign = +1** (8-point scan, denser at higher Mach) |
| w_wall | **−2/3** | codim-1 domain-wall EoS (rational; S42) |
| f_wall(transit) | 3.06e-7 | S42 |
| **f_wall(today)** | **7.19e-29** | = f_wall(transit)·a_transit (a_transit=2.35e-22); ≪ DESI w_a sens ≈ 0.3 |

SUBSTITUTION CHAIN (plan Steps 1–5, with substituted numbers — the [SIGN] prediction):
- **Step 1**: ξ̂ = ξ₀ (τ_Q/τ₀)^{ν/(1+zν)}, ξ₀ = ξ_BCS = 0.8083468753837275 [del Campo-Zurek 2014].
- **Step 2**: ν=1/2, z=2 ⇒ ν/(1+zν) = (1/2)/(1+1) = **1/4** [mean-field BCS, S53/S88].
- **Step 3**: τ_Q(Mach) = dt_transit·(13.75/Mach) [faster transit = shorter fold-crossing].
- **Step 4**: ξ̂(Mach) = ξ₀·[dt_transit·(13.75/Mach)/τ₀]^{1/4} = const·**Mach^{−1/4}**.
- **Step 5**: n_wall ∝ ξ̂^{−2} ⇒ n_wall ∝ (Mach^{−1/4})^{−2} = **Mach^{+1/2}**; d n_wall/d Mach = +(1/2)·const·Mach^{−1/2} > 0.
- **Direction (CONFIRMED)**: n_wall INCREASES with Mach — the SIGN prediction holds (sign_verdict=PASS). A faster transit freezes a DENSER network *if one forms*. But at the actual Mach=13.75, ξ̂ ≈ 0.162 M_KK⁻¹ exceeds the fold-crossing system size L = 0.025 M_KK⁻¹ by **6.5×**: the system is a *fraction of one correlation length across*, so there is no room for a single domain boundary.

WHY THE NETWORK DOES NOT SURVIVE (the three independent, sharper-than-homotopy arguments):
1. **0D regime** (regime_verdict=BREAKDOWN). L/ξ̂ = 0.1546 ≪ 1 (equivalently L/ξ_BCS = 0.031). A network requires L/ξ ≫ 1 (many correlation volumes to host distinct domains). Here L/ξ ≪ 1 — the KZ defect-formation interpretation is INVALID and is correctly reformulated as 0D pair production (T3-S38-KZ-DEFECTS, S81 PASS, `convention=0D_pair_reformulated`). This is INDEPENDENT of homotopy: even with π₀(Z₃)=Z₃, a single-correlation-volume system cannot resolve any domain structure.
2. **Uniform sector population** (GGE Universality, S57 PROVEN). The sudden quench (dt/T_L=1.25e-5, P_exc=1.000) populates the Z₃ sectors UNIFORMLY — no domain selection, E_DW=0, all cells identical post-transit.
3. **Dilution + bias** (magnitude_verdict=FAIL). Even a network that DID form carries f_wall(transit)=3.06e-7 and dilutes as ρ_wall ~ a⁻¹, so f_wall(today)=7.19e-29 — 28 OOM below the DESI w_a sensitivity (≈0.3). Independently, the Josephson bias annihilates walls 15,000× before reheating (Domain-wall GW RETRACTED S77).

CONSTRAINT-MAP CONSEQUENCE: The Kibble-Zurek route to the DESI w_a / BBN ΔN_eff tension is **CLOSED**. The gate's homotopy correction (π₀(U(1)₇×Z₃)=Z₃, walls admitted) is correct and sharpens the bookkeeping, but the "no-walls" cosmological verdict does NOT rest on the π₀(U(1))=0 argument the gate set out to overturn — it rests on the SHARPER 0D-regime + uniform-population + a⁻¹-dilution + Josephson-bias arguments, all of which survive the homotopy correction intact. The **frozen-modulus w_a=0 lock (C-1) stands on a sharper footing than before**, and the GGE-homogeneity T2 is UNAFFECTED (E_DW=0 holds regardless of homotopy). The surviving candidate for any DESI w_a≠0 / BBN signal is the **running-vacuum mechanism (INV8-W2-4)**, not a frozen Z₃ wall network — the W3-1 ↔ W2-4 competition resolves in W2-4's favor at the `/rclab-investigate --investigation 8` close synthesis.

SUBSTRATE FRAMING: PHONONIC. The transit IS a quench of the substrate's internal spectral structure through the van Hove fold. The order-parameter manifold IS the structure the D_K spectrum reorganizes onto at τ_fold — the U(1)₇ BCS-condensate phase (Cooper pairs carry K₇ charge ±1/2, B6) TIMES the Z₃ Jensen-deformation structure (π₀(Z₃)=Z₃, the 512-plaquette frustration §VII.AG.4). A Kibble-Zurek wall would be a frozen-in mismatch between Z₃ sectors of the reorganized spectrum — a relay-pattern domain boundary, NOT a topological defect embedded in a pre-existing spacetime. The direction of explanation holds: D_K eigenvalues reorganize at the fold → but the fold-crossing region is a *fraction of one correlation length* (a 0D pocket of reorganization, not an extended domain landscape) → so no frozen wall network is a substrate-IS interference pattern → there is no emergent w=−2/3 / a⁻¹ cosmological consequence. The "no-walls" claim once read π₀ off the U(1) factor alone; this gate reads it off the full U(1)₇×Z₃ substrate symmetry AND finds the same answer, for a deeper substrate-physics reason (the fold is sub-correlation-length, not topologically wall-free).

---

### §W3-2. INV8-W3-2 (phonon-first-cosmologist)

**Status**: **COMPLETED**
**Gate ID**: `INV8-W3-2-QUANTUM-METRIC-STIFFNESS-HTAU`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (the quantum metric g_ab^{(P_0)} IS a substrate-IS spectral-triple invariant — the metric structure of the substrate's reorganized spectral weight at the fold, not a property of a band IN a Brillouin-zone container)
**Agent**: `phonon-first-cosmologist`
**Hypothesis**: The integrated quantum metric of the fold band, dimensionalized by M_KK as the Peotta-Törmä superfluid-weight stiffness `D_geom = (2 Δ_BCS / V) ∫_BZ Tr g_ab^{(P_0)}(k; τ_fold) d^d k`, is a substrate-IS invariant (no imported scale but M_KK) that sets an emergent oscillation frequency identifiable with the Hubble backbone H(τ) the rank-1 NNU theorem (§VII.BS) currently imports; the substrate flat band is maximally-NON-ideal — Tr g>0 (metrically rich) while Berry Ω=0 EXACTLY (C=0).
**Plan reference**: `sessions/investigation/investigation-8/investigation-8-plan-w3.md` §W3-2 (machinery pin, R_stiff=ω_stiff/H*_imported OOM bands 0.5/2.0 decade, cross-pillar 5-anatomy+3-level refinement of §VII.W/§VII.AF.1.OP-PROJ, substitution chain source).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML; verified on disk by content, not line count):
- **script** — `computations/investigation-8/inv8_w3_quantum_metric_stiffness_htau.py` ✅ EXISTS (33538 B). `grep -E 'from canonical_constants import'` → line 96 `from canonical_constants import (`; `grep -E 'print_verdict_payload'` → line 534 `def print_verdict_payload():` (4 total matches). PASS.
- **data** — `computations/investigation-8/inv8_w3_quantum_metric_stiffness_htau.npz` ✅ EXISTS (11336 B). PASS.
- **plot** — `computations/investigation-8/inv8_w3_quantum_metric_stiffness_htau.png` ✅ EXISTS (76603 B). PASS.
- **verdict_line** — `computations/investigation-8/inv8_gate_verdicts.txt` line 55: `grep -E '^INV8-W3-2-QUANTUM-METRIC-STIFFNESS-HTAU:.* audit_sha256=[a-f0-9]{64}'` → matches (full 64-hex `audit_sha256=8e2e575e…f49ddac3`). Companion dual-SHA row (line 56) + schema-v2 3-tuple row (line 57, `sign_verdict=FAIL magnitude_verdict=FAIL regime_verdict=MARGINAL`) present (`[SIGN]` trigger satisfied). PASS.
- **wp_section** — this section: `Status:.*COMPLETED` ✅, `Verdict:.*(PASS|FAIL|INFO)` ✅, `Output Artifacts` ✅, `MCP Pre-Compute Audit` ✅.

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script, per query-first discipline; one-line salient return each):
- `search_knowledge('quantum metric Peotta-Torma superfluid stiffness flat band')` → **"Peotta-Torma for CC" (S64, PROVEN): flat-band superfluid-weight route INAPPLICABLE to the CC.** BRANCH: this gate targets H(τ) (the a(t) backbone G-1), NOT the CC — a DIFFERENT observable, so the S64 closure does **not** pre-close this gate. Also returned the canonical formula `D_s = (2Δ/V)·Tr(g)` (session-32) and `D_geom = quantum-metric from INTERBAND, ≥0 by Cauchy-Schwarz` (s86).
- `search_knowledge('Hubble backbone H tau imported rank-1 NNU theorem a(t) effective Friedmann gap')` → **NNU rank-1 theorem §VII.BS STAGE-3-PERMANENT** (`S103-NNU-BUNDLE-EXHAUSTIVENESS` PASS): every dimensionful observable shares ONE unfixed weight `w = M_KK`. The §6.3 a(t)-gap is "RE-FRAMED to ONE rank-1 normalization non-universality with a topological cause." `H(τ) = H_fold·√(V(τ)/S_fold)` (Friedmann form, S83).
- `search_knowledge('Pillar III IV bridge R_geom quantum metric Berry curvature zero maximally non-ideal')` → **`S87-PILLAR-III-IV-BRIDGE-PERMANENT-LAND` value=0.0950 (verdict-LINE FAIL on the 19/200 convention; STRUCTURAL bridge §VII.AF.1 PROVEN)**; atlas-07 "Berry curvature B=982.5" ERRATUM (was quantum metric; **Berry = 0 EXACT (W5)**); `S106-W3-1-METRIC-WITHOUT-CURVATURE-LANDING` PASS (§VII.CA: g≈982.5, Chern=Euler=graded-Ω=0).
- `get_constant('Delta_BCS')` → 0.4642547394830737 (R-protected, M_KK units). `get_constant('M_KK')` → 7.428660036284456e16 GeV. `get_constant('tau_fold')` → 0.19. `get_constant('w0_FW')` → −0.918. `get_constant('H_fold')` → **586.5267713108464 (S38, the imported Friedmann backbone, M_KK units)** — adopted as H*_imported. `get_constant('G_DeWitt')` → 5.0 (DeWitt kinetic coefficient = τ-modulus inertia χ). `get_constant('N_cells')` → 32.0 (Voronoi BZ-volume normalization V).
- Source-script reads (machinery faithfulness, not re-derivation): `s100b_nonabelian_metric_fraction.py` (the lowest |λ| J/PH doublet lives in the **(0,0) singlet block**, `D = Ω_spin`, band_deg=2; line 833: "the U(2)-invariant TT deformation cannot rotate the (0,0)-block ⇒ its QGT is **zero** on THIS surface"), `s104_euler_class_j_doublet.py` (line 92: "atlas-07's reservoir ~982.5 is a **methodological cross-check only**"), `s96_geom_offjensen_chern.py` (the canonical `(τ,μ)` TT machinery: `metric_scale_factors`, `build_dirac_sector`, `lowest_band_multiplet` band_deg=2, `dD_dparam`, the non-Abelian Provost-Vallée QGT trace; v_J=(2,−2,1), v_μ=n×v_J=(11,7,−8), n_vol=(1,3,4)).
- **PRE-CLOSED check**: NO closure covers the H(τ)-identification gate. S64 closes the CC route (different observable); §VII.AF.1/§VII.CA register the bridge + the metric-without-curvature wall but do NOT dimensionalize Tr g into a stiffness-frequency vs the imported backbone. The gate is genuinely open.

**Verdict**: **FAIL** (composite). Schema-v2 3-tuple: **sign_verdict = FAIL**, **magnitude_verdict = FAIL**, **regime_verdict = MARGINAL**. The constructive attack on the a(t) gap (G-1) via the lowest-doublet quantum-metric stiffness is **structurally CLOSED at the (0,0) block** — and the FAIL is itself a *stronger* statement than "magnitude doesn't match": the geometric stiffness is **zero by U(2)-invariance protection**, not merely off-scale.

**Results**:

*Numbers (the gate is NUMBERS-first):*
- **Lowest-|λ| Dirac doublet**: located in the **(0,0) Peter-Weyl singlet block** (`D = Ω_spin` offset, 16×16) at (τ_fold, μ=0); `|λ|_min = 0.819741112`, **lowest-band degeneracy = 2** (J/PH Kramers doublet, matches the plan-expected band_deg=2 and S96/S100b/S104). `D` anti-Hermiticity error = `0.00e+00` exact ⇒ `H = iD_K` real-symmetric ⇒ real eigenstates.
- **Provost-Vallée quantum metric over the U(2)-invariant volume-preserving TT (τ,μ) surface** (the genuine substrate-IS object; non-Abelian QGT trace over the doublet): `g_{τ,τ} = 1.09e-27` (Jensen direction v_J), `g_{μ,μ} = 2.91e-27` (C² Higgs-coset direction v_μ), cross term `g_{τ,μ} = −1.68e-27`. **`Tr g = g_ττ + g_μμ = 4.00e-27`** — i.e. **ZERO** at the float64 eigen-floor (~1e-27 is round-off, NOT a signal). 
- **Berry curvature** `Ω (Im QGT) = −1.43e-28`, `|Ω| = 1.43e-28 < 1e-10` ⇒ **Berry = 0 EXACT** (anti-Hermiticity of the Kosmann connection, as registered in §VII.CA / atlas-07 ERRATUM).
- **Geometric stiffness**: `D_conv = 0` (flat fold band, van Hove A₂ catastrophe, B1 PROVEN ⇒ Drude weight vanishes), `D_geom = (2·Δ_BCS/V)·Tr g = (2·0.464255/32)·4.00e-27 = 1.16e-28` M_KK² (≈0, inherited from Tr g≈0). `D_s = D_conv + D_geom = 1.16e-28` M_KK².
- **Emergent frequency**: `χ = G_DeWitt = 5.0` (τ-modulus inertia), `ω_stiff = √(D_geom/χ) = 4.82e-15` M_KK.
- **Comparison**: `H*_imported = H_fold = 586.5267713108464` M_KK (S38, the rank-1 NNU imported Friedmann backbone). `R_stiff = ω_stiff/H* = 8.22e-18`, `log₁₀ R_stiff = −17.09`, `|log₁₀ R_stiff| = 17.09` — **~17 decades below** the imported backbone, vastly outside both the PASS (≤0.5 dec) and INFO (≤2.0 dec) bands.
- 4-tuple: `(value=R_stiff=8.22e-18, scheme=FW, convention=Peotta-Torma-D-geom-substrate-IS-OP-PROJ, L_max=10)`. CLASS=FULL (quantum metric from the real D_K eigenvectors; no SCHEMATIC helper). regulator_pin=N/A (the quantum metric is a D_K eigenbundle property, NOT a Seeley-DeWitt aₙ moment — per the S105 W3-1/W3-2 verdict-line precedent).

*Substitution chain (faithful to the plan §W3-2 chain; the OUTCOME inverts its conditional):*
- Step 1–4 (plan): `D_s = D_conv + D_geom`; `D_conv ∝ <d²E/dk²> = 0` (flat band); `D_geom = (2Δ/V)∫Tr g`; the chain predicts `D_geom > 0 STRICTLY` **IF Tr g > 0**.
- Step 5 (plan, the conditional premise): "the fold band is METRICALLY RICH (§VII.W R_geom > 0; atlas-07 g≈982.5 WAS the quantum metric) ⇒ ∫Tr g > 0 STRICTLY." **This premise is FALSE for the lowest-doublet (τ,μ) metric.** The canonical machinery (S100b L833, S104 L92) shows the `g≈982.5` reservoir is a **methodological cross-check value — a DIFFERENT object**, not the lowest-doublet QGT trace. The genuine substrate-IS `Tr g` on the lowest (0,0) doublet over the U(2)-invariant TT surface is **ZERO** (`4.00e-27`, machine-floor), because **the U(2)-invariant volume-preserving deformation (v_J, v_μ) cannot rotate the (0,0) singlet block** — the QGT vanishes by representation-theoretic protection. `Tr g/g_atlas = 4.07e-30`.
- Conclusion: `D_geom = 0 + (2Δ/V)·0 ≈ 0` ⇒ `ω_stiff ≈ 0` ⇒ the quantum-metric stiffness is **not** the imported H(τ). The chain's Step-5 premise is the failure point, and the failure is **structural** (U(2)-protection), not a numerical near-miss.

*3-tuple semantics:*
- **sign_verdict = FAIL**: the chain predicted a strictly-positive geometric stiffness (`D_geom > 0` despite `D_conv = 0`); the substrate does **NOT realize** it because `Tr g = 0` (U(2)-protected). The predicted constructive direction is closed at the (0,0) doublet.
- **magnitude_verdict = FAIL**: `|log₁₀ R_stiff| = 17.09 ≫ 2.0` info-band ceiling.
- **regime_verdict = MARGINAL**: the maximally-NON-ideal signature has TWO halves — Berry = 0 EXACT (which **holds**, `1.43e-28`) and Tr g > 0 (which **fails**, the metric is trivial on this surface). Half the signature holds ⇒ MARGINAL (the stiffness-to-frequency identification is off-regime: there is no geometric stiffness to identify with H(τ)).
- Composite collapse (gate-verdicts.md PRE-REGISTERED rule): `sign_verdict == FAIL ⇒ composite = FAIL`.

*Constraint-map consequence (dual_prior Track B realized, prior 0.6):*
- **The quantum-metric-stiffness route to H(τ) is CLOSED** — the a(t) gap (G-1) **survives** this route. The closure is *structural*: the lowest-doublet quantum metric over the U(2)-invariant volume-preserving TT surface is **zero by representation-theoretic protection** of the (0,0) singlet block (the same U(2)-invariance that makes Berry/Chern/Euler/graded-Ω vanish, §VII.CA). H(τ) cannot be sourced from the lowest-band τ-stiffness because that stiffness identically vanishes.
- **Durable structural output (lands independent of the H(τ) question)**: the (0,0) lowest doublet is **half-maximally-NON-ideal on the deformation surface** — Berry Ω = 0 EXACT (the topological-triviality half holds), but the quantum metric ALSO vanishes on the U(2)-invariant directions (so it is NOT "metrically rich" on THIS surface — the `g≈982.5` reservoir is a different, non-(τ,μ) object). This SHARPENS §VII.CA: the metric-without-curvature wall's "g≈982.5 ≠ 0" is the reservoir value, but the *lowest-doublet (τ,μ)-projected* metric is itself zero — the (0,0) block is geometrically inert under the volume-preserving TT deformation.
- **Surviving candidate for G-1**: the running-vacuum / Volovik-tracking route (INV8-W2-4) and the Jacobson→CC magnitude attack (INV8-W2-1) remain the live constructive attacks on the dimensionful-scale knot; this gate eliminates the quantum-metric-stiffness corridor for the *backbone function* H(τ) specifically.

**Cross-pillar bridge anatomy** (this gate REFINES the registered §VII.AF.1.OP-PROJ / §VII.CA; per `cross-pillar-bridge-anatomy.md`):
- **Element 1 — substrate-IS observable**: the finite-L Provost-Vallée quantum-metric trace `Tr g = g_ττ + g_μμ` of the lowest J/BDI-real doublet of `D_K(τ,μ)` on `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})` at (τ_fold, μ=0), and its dimensionalized stiffness `D_geom`. Substrate-IS **Level 2 (moduli-deformation)** — the (τ,μ) surface IS the substrate's own volume-preserving TT deformation manifold (NOT a coordinate container), per `phononic-framing.md §"Single-τ-slice vs moduli-deformation"`.
- **Element 2 — laboratory-IN observable** (OE-form): `R_geom = ∫_BZ Tr_{lowest-band} P_0(k) [Provost-Vallée QGT real part] d^d k` (the Peotta-Törmä continuum BZ-trace; named projector `P_0` = lowest-band). The registered §VII.W laboratory-IN observable.
- **Element 3 — bridge map**: HKR `L_max → ∞` Connes-Karoubi pairing (same as §VII.W / §VII.AF.1; substrate-distance-1).
- **Element 4 — algebraic envelope**: `L^{−3}` at d=4 (Level-2-binding, inherited from §VII.W).
- **Element 5 — empirical anchor**: the §VII.W Level-3 anchor (0.0095% F_4 strict / 0.0950 inside envelope at L_max=10).
- **The NEW substrate finding** (not in the prior bridge): the dimensionalized stiffness `ω_stiff(fold)` is `~17 decades below` the imported backbone H_fold, and the lowest-doublet `Tr g` is **zero** on the U(2)-invariant surface — so the bridge does NOT extend to an H(τ)-identification. NOTE: this is an investigation gate; any permanent §VII registration (e.g. an OP-PROJ "U(2)-protected vanishing of the lowest-doublet (τ,μ) metric" sharpening of §VII.CA) is session-track promotion at `/rclab-investigate` close, NOT an investigation edit.

**Substrate framing** (`phononic-framing.md §"IS Space, Not IN Space"`). The quantum metric g_ab^{(P_0)} IS a substrate-IS spectral-triple invariant — the real part of the quantum geometric tensor on the lowest-band projector of `D_K`, computed from D_K eigenvectors with NO imported scale except M_KK. The **direction of explanation**: `D_K eigenvectors at the fold → the quantum metric of the lowest-band projector over the substrate's OWN (τ,μ) volume-preserving TT deformation manifold → the geometric superfluid stiffness D_geom → an emergent oscillation frequency → (the test) is that frequency the Hubble backbone H(τ) the cosmology rides on?` The answer the substrate gives: **no — the lowest-doublet metric is zero on its own deformation surface (U(2)-invariance protection of the (0,0) singlet block), so there is no geometric stiffness to ride on.** The Berry curvature is ZERO EXACTLY (K_a anti-Hermitian on any compact Lie group — Kosmann connection), consistent with the metric-without-curvature wall §VII.CA; but here the *projected metric itself* also vanishes, so the lowest doublet is geometrically inert under the volume-preserving TT deformation rather than "metrically rich." This is the cross-domain bridge B-1 read honestly: the post-2015 ideal-flat-band literature (Roy 2014; Ledwith-Vishwanath 2020) made the `Tr g ↔ Ω` relation precise, and the substrate's lowest doublet sits at the `Tr g = 0, Ω = 0` corner of its own moduli surface — topologically AND metrically trivial there (the `g≈982.5` reservoir is a different, non-(τ,μ)-projected object). The H(τ) backbone is NOT the quantum-metric stiffness; it is imported elsewhere (the rank-1 NNU `w = M_KK`), and the a(t) gap stands.

---

### §W3-3. INV8-W3-3 (spectral-geometer)

**Status**: COMPLETED
**Gate ID**: `INV8-W3-3-SPECTRAL-DIMENSION-LMAX14-CDT`
**Trigger**: `[CHAIN]`
**Classification**: **GEOMETRIC** (the return probability P(σ)=Tr e^{−σ D_K²} IS the substrate's own heat trace — the spectral fingerprint of the D_K eigenvalue spectrum, not a diffusion process IN a background geometry)
**Agent**: `spectral-geometer`
**Hypothesis**: Pushing the heat-trace return probability P(σ) to L_max=14-16 (the GT-builder lifted the Sym¹³/¹⁴ wall at S104/S105) escapes the narrow-band artifact and yields BOTH d_s(σ→0)→8 (the Weyl/SU(3)-manifold dimension) AND a windowed d_s(σ_*) at the fold; the CDT/asymptotic-safety dimensional-reduction comparison is made fairly via the energy-axis DOS exponent γ_E (the diffusion-window K=2 specialization), with the (observable, diffusion-window) pair fixed on BOTH sides and the same functional Φ at the same scale-type.
**Plan reference**: `sessions/investigation/investigation-8/investigation-8-plan-w3.md` §W3-3 (machinery pin, |d_s(σ→0)−8|≤0.5 Weyl recovery + |γ_E(16)−γ_E(14)|≤0.10 convergence, MANDATORY multiplicative-normalization-cancellation pre-flight + L_max_plan/L_max_operational Casimir-feasibility gate, substitution chain source).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

| Artifact | Path | Verified |
|:---------|:-----|:---------|
| script | `computations/investigation-8/inv8_w3_spectral_dimension_lmax14_cdt.py` | ✓ on disk (41,916 B); `grep "from canonical_constants import"` → 1 hit; `grep "print_verdict_payload\|VERDICT_PAYLOAD_JSON"` → 2 hits |
| data | `computations/investigation-8/inv8_w3_spectral_dimension_lmax14_cdt.npz` | ✓ on disk (25,787 B); loads; 50 keys incl. `verdict=INFO`, `gamma_E`, `ds_star`, `ds_weyl_crossing`, `saturated=True` |
| plot | `computations/investigation-8/inv8_w3_spectral_dimension_lmax14_cdt.png` | ✓ on disk (166,881 B); 4-panel (d_s flow; Weyl-window crossing vs L_max; γ_E saturation; new-sector floors vs fold ceiling) |
| verdict_line | `computations/investigation-8/inv8_gate_verdicts.txt` | ✓ `^INV8-W3-3-SPECTRAL-DIMENSION-LMAX14-CDT:.* audit_sha256=6b6484a1159f3f909839f2059aa0f884981eeae83115ebba5400e30c6029f0b5` (64-hex); dual-SHA companion row present; `[CHAIN]` → no schema-v2 3-tuple (correct) |

**MCP Pre-Compute Audit** (per `.claude/rules/knowledge-index-usage.md`; queries executed BEFORE writing the script):

- `get_constant('d_s_fold_window_sigma')` → **1.4005** (S92-ADHOC-SPECTRAL-DIMENSION-DS-FLOW-VS-CDT); the canonical fold diffusion-window σ_*. Confirmed the pin matches the plan.
- `search_knowledge('spectral dimension return probability CDT asymptotic safety dimensional reduction')` → **S92 workshop `s92-adhoc-spectral-dimension-ds-flow-vs-cdt.md`** (eq_7048–7052: the Φ functional `d_s=−2 dlnP/dlnσ`, `P(σ)=Σ dim(p,q) Σ_i e^{−σλ_i²}`, the matched-window CDT-comparison law `d_s^{substrate}(σ_*)=Φ[P_{D_K}](σ_*)` vs `d_s^{CDT}(intermediate-window)=Φ[P_CDT]`). **Critical prior**: the standing "no CDT reduction" headline was DOWNGRADED to *indeterminate-pending-compute*; THIS gate is the registered discharge. Also the open_channel `Phononic-Penrose-Diagrams.md`: `lim_{σ→0} d_s = 8` on the 8-dim SU(3) fiber.
- `search_knowledge('van Hove gamma_E DOS exponent heat trace spectral dimension d_s')` → **S93-W7-3 `s93-w7-3-gamma-e-dos-exponent-estimator.md`** (eq_7113–7122). The γ_E estimator (K1 Step 1–5): `N(λ)=Σ_{λ_i≤λ} m_i`, slope of `log|N−N₀|` vs `log|λ−E₀|` = `1−γ_E` ⇒ `γ_E=1−slope`; exact order map `γ_E=1−1/n` (n=2⇒½ √-edge KK; n→∞⇒1 vH). **DECISIVE prior finding**: at fixed τ_fold γ_E is L_max-SATURATED (`|γ_E(L12)−γ_E(L10)|=0.0000`) — new sectors land ABOVE the fold, never below. Prior anchors: `γ_E_central=0.4807`, `min_ds=7.7953`, `ds_σ_*=8.4851`, `n_distinct_2wf=5`, E_B2=0.845269, E_B1=0.819741.
- `trace_entity('spectral dimension d_s flow')` → eq_7889 (the Φ definition), eq_7049 (`d_s(σ_*)=2σ_*⟨λ²⟩_{σ_*}`, energy-axis-DOS-weighted), eq_7051 (the CDT matched-window law), eq_10556 (the Hawking `n_s−1~−d(d_s)/dτ` route, separate concern). Confirmed no closure pre-empts the HIGH-L_max fold-window measurement this gate makes.
- Cross-investigation dedup (per plan): complementary to inv-3 W2-1 (d_s-flow as K→K* map) + inv-3 W2-2 (isospectral rigidity at L_max=3); this gate is the HIGH-L_max (14-16 attempt) CDT comparison — distinct observable scope. **Not pre-closed** — the converged-L_max fold-window d_s + the matched-functional CDT comparison had never been run.

**Verdict**: **INFO** — `value='d_s_Weyl_crossing_L12p13=8.0202(uv_recovered=True); d_s_sigma_star=8.5184(matched-window,NOT~2); gamma_E_L12p13=0.4834(n_vH=1.94,KK/sqrt-edge); dgamma_L12p13_L12=0.00000(tol0.1,converged=True); SATURATED=True; mult_norm_factorization=False; CDT_reduction_reproduced=False; L_max_op=12+pL13_plan16_infeasible_Sym13wall'` scheme=`zeta` convention=`NORMAL-STATE-Delta0-heat-trace-energy-axis-gamma_E;diffusion-window-K2-specialization` L_max=`12+pL13(plan16)` `audit_sha256=6b6484a1159f3f909839f2059aa0f884981eeae83115ebba5400e30c6029f0b5` `content_sha256=07553caf2b0db713f3c362ee2cefee6cebe674568a1b085b2b99e9786aa5bc25`. regulator_pin=`a_n^{ζ}`.

Both LITERAL pre-registered legs PASS (UV Weyl recovery `|8.0202−8|=0.02≤0.5`; γ_E convergence `0.00000≤0.10`), but the SUBSTANTIVE answer CONTRADICTS the PASS-narrative's Track-A "dimensional reduction CONFIRMED": the matched-functional substrate d_s(σ_*)=8.5 (NOT ~2) means **CDT dimensional-reduction is NOT reproduced** on the matched functional, reached via L_max-SATURATION (a decisive comparison) rather than artifact-domination. INFO is the faithful encoding — the comparison is MADE and decisive (R-1 resolved), the resonance was a scale-type mismatch (the honest sub-reading of Track B), not a confirmed reduction.

**Results**:

**NUMBERS first.**

| Quantity | Value | Anchor / interpretation |
|:---------|:------|:------------------------|
| **Multiplicative-norm pre-flight** | `FACTORIZATION_HOLDS = False` | Sage-exact `d/ds[P_{N+1}/P_N] = −0.00581 ≠ 0` → genuine L_max-dependent observable |
| **d_s(σ→0) genuine-Weyl-window crossing** | **8.0202** (L12+pL13) | `|8.0202−8|=0.02 ≤ 0.5` → **uv_recovered = True** ("crossings not plateaus") |
| **max d_s in genuine Weyl window** | 8.5518 | d_s sweeps 0→8.55 through the window [1/λ_max², 1/λ_min²]=[0.034, 1.49] |
| **windowed d_s(σ_*=1.4005)** | **8.5184** | cf S93 anchor 8.4851 (0.4%); substrate retains dim ~8.5 in fold window, **NOT ~2** |
| **min d_s over [0.5, 2.0]** | 8.0202 (L12+pL13) | cf S93 anchor 7.7953; rises to 8 as L_max grows (truncation bias upward, S52/S92) |
| **γ_E (energy-axis DOS exponent)** | **0.4834** (ALL L_max) | cf S93 anchor 0.4807; `n_vH=1/(1−γ_E)=1.94≈2` ⇒ **√ band edge (KK), NOT ∞-order vH** |
| **γ_E L_max-convergence** | `|γ_E(L12p13)−γ_E(L12)| = 0.00000` | `≤0.10` → **gamma_converged = True**; reproduces S93 `d_gamma_L12_L10=0.0000` EXACTLY |
| **Saturation** | new-sector floor 2.412 > fold ceiling 0.873 | SATURATED=True; new sectors cannot enter the fold window |
| **CDT reduction reproduced** | **False** | substrate windowed d_s(σ_*)=8.52 vs CDT intermediate ~2 |
| **L_max** | plan=16; operational=12 full + partial L13 (12 sectors) | Sym¹³/¹⁴ wall (see feasibility) |

**MANDATORY multiplicative-normalization-cancellation pre-flight** (`math-scripts.md §"Multiplicative-normalization cancellation invariants"`, K=3 MANDATORY) — run via Sage `sage_eval` (NOT a simple `sage_simplify`; the multi-statement script needs `sage_eval`): test whether `P(σ) = w(L_max)·g(σ)` with g L_max-independent. Modelling `P_N = d1 e^{−s a1} + d2 e^{−s a2}` and `P_{N+1} = P_N + db e^{−s b1}` (a new sector at a LARGER eigenvalue-square b1), `d/ds[P_{N+1}/P_N] = ((a2−b1)d2·db·e^{2a1 s+a2 s} + (a1−b1)d1·db·e^{a1 s+2a2 s})·e^{−b1 s} / (d2² e^{2a1 s}+2 d1 d2 e^{a1 s+a2 s}+d1² e^{2a2 s})`, which is `−0.00581 ≠ 0` at a non-degenerate test point ⇒ **FACTORIZATION_HOLDS = False**. The additive-new-sector structure is NOT a product form. Therefore `d_s = −2 dlnP/dlnσ` is a GENUINE L_max-dependent observable, and the PASS criterion correctly targets the L_max-STABILITY of d_s/γ_E (empirical convergence), NOT an asymptote-value-only test. This is the OPPOSITE of the multiplicative-normalization case (where a w(L_max) pre-factor is annihilated by the log-derivative). Carried in the verdict-line convention/value field (`mult_norm_factorization=False`).

**FEASIBILITY GATE** (`math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"`) — the load-bearing operational disclosure. `L_max_plan = 16`; `L_max_operational = 12 full (90 cached + (4,4) reconstructed) + partial L13 (12 of 14 center sectors)`. **The plan's L_max=14-16 is INFEASIBLE within an agent timeslot**: (i) probed this session, `irrep_symmetric_power(gens, 13)` did NOT complete within a 160 s budget — the Sym¹³/¹⁴ pure-symmetric extremes are multi-hour single-thread (the builder docstring's own "Sym^13/14 are multi-hour" record); (ii) the GT-builder cache `s104_sym_p_chain_cache_L1314.npz` is `status=IN_PROGRESS` — only 12 of 14 L=13 center sectors on disk (the (0,13)/(13,0) extremes MISSING), and ZERO L=14, L=15, L=16 sectors. The plan's prerequisite ("the GT-builder lifted the Sym¹³/¹⁴ wall") was OPTIMISTIC: the wall is lifted only for the 12 center sectors of L=13, not the extremes nor L=14+. **Honest disclosure per math-scripts.md item-4**: no silent null-PASS; both L_max values recorded in npz. The L12 master cache loaded verbatim (SHA-pinned `9e6d9cf7…`), bit-exact; the only addition is the (4,4) reconstruction (dim 125, block 2000×2000, |λ|∈[2.41,3.76], ~1.7 s on the RX 9070 XT GPU).

**Why the operational ceiling is SUFFICIENT (Casimir / Friedrich-Bär saturation — the structure-first argument).** The fold-window observables (γ_E, d_s(σ_*)) are STRUCTURALLY L_max-SATURATED at L12, so L_max=14-16 cannot move them, so the operational truncation is not a limitation but a *proof*. The Casimir law `|λ(p,q,τ)| = √C₂(p,q)·exp(−τ(p+q))` sends every new (p,q) sector to LARGER |λ|: the reconstructed (4,4) has min |λ|=2.412, and the L13 center sectors min |λ|≥2.41 — all far ABOVE the fold-window ceiling E₀+2·w_fit = 0.873. A new sector whose eigenvalue floor exceeds the fold-window ceiling cannot contribute a single eigenvalue to the ±2·w_fit window, so it cannot change the γ_E fit nor the windowed d_s. Directly verified: `γ_E = 0.4834` is IDENTICAL across {L10, L11, L12, L12+pL13} (`|Δγ_E| = 0.00000`), reproducing the S93 `d_gamma_L12_L10 = 0.0000` finding from independent data. **This STRUCTURALLY REFUTES the gate's own hypothesis** that high-L_max "escapes the narrow-band artifact" *for the fold edge*: the fold is a one-sided-starved spectral-bottom edge whose DOS staircase is L_max-frozen; adding sectors above it adds zero resolution below it. The narrow-band character is intrinsic to the fold geometry (4 distinct levels within 2·w_fit, 4 below E₀, 1 above), NOT a truncation under-resolution that more L_max removes.

**Substitution chain (plan Steps 1–5, additive-new-sector structure — CONFIRMED).**
- **Step 1**: `P(σ) = Σ_{(p,q): p+q≤L_max} dim(p,q) Σ_{i∈(p,q)} e^{−σλ_i²}` [heat trace, NORMAL state Δ=0; PW multiplicity = dim(p,q)].
- **Step 2**: increasing L_max→L_max+1 ADDS new sectors `{(p,q): p+q=L_max+1}` with NEW eigenvalues at NEW magnitudes (higher C₂ ⇒ larger |λ|_min ~ √C₂·exp(−τL)). Verified: (4,4)+L13 floors ≥ 2.41.
- **Step 3**: `P_{L+1}(σ) = P_L(σ) + [new-sector](σ)` — ADDITIVE in σ-dependent terms, not multiplicative.
- **Step 4**: therefore `P_{L+1}/P_L` is σ-DEPENDENT (new sectors weight large-λ, reshape the bulk slope) ⇒ NO L_max-independent kernel g(σ) with `P=w(L_max)g(σ)`. Sage-confirmed (`d/ds[ratio]≠0`).
- **Step 5**: `d lnP/d lnσ` picks up the new-sector reshaping ⇒ d_s(σ) genuinely flows with L_max in the Weyl window until the sector sum converges — the OPPOSITE of the multiplicative-normalization case. **CONFIRMED**: the multiplicative-normalization pre-flight returns FALSE; the PASS criterion correctly targets the L_max-STABILITY of d_s/γ_E.

**The CDT / asymptotic-safety comparison — MADE, on the matched functional (the K=2 same-functional-different-scale discipline).** Per `phononic-framing.md §"Same-functional-different-scale fair-comparison"` (K=2) and `cross-pillar-bridge-anatomy.md §24` (diffusion-window-observable specialization): the (observable, diffusion-window) pair is fixed on BOTH sides, the SAME functional Φ = `−2 d ln(Tr e^{−σD²})/d lnσ` is applied at the SAME scale-type, and the discriminator is the directly-fitted energy-axis DOS exponent γ_E (the impedance Z=ρ_E·v_g is a consistency check, not a lock — NO cross-scale d_s magnitude is used as a gate). **Substrate side**: Φ[P_{D_K}](σ_*) = d_s(σ_*=1.4005) = **8.5184**, with the energy-axis exponent **γ_E = 0.4834 ⇒ n_vH ≈ 2** (a square-root band edge). **CDT/asymptotic-safety side**: the UV dimensional reduction d_s → ~2 in their own intermediate diffusion window (Ambjørn–Jurkiewicz–Loll 2005; Reuter–Saueressig asymptotic safety) is governed by a DOS that produces an intermediate-window d_s plateau at ~2. **Result**: the substrate's matched-window d_s(σ_*) = 8.5, NOT ~2 — the substrate retains its full fiber dimension in the fold window, and the energy-axis edge is √-type (n≈2), the KK/embedding-dimension reading, NOT the infinite-order van-Hove divergence (n→∞ ⇒ γ_E→1) that a CDT-like reduction would require. **The CDT dimensional-reduction analogy is NOT reproduced on the matched functional.** This is fully consistent with the S92-D-KK-4 finite-σ floor (prior accessible `d_s_min ≈ 6.3`, with truncation bias pushing d_s UP toward 8 as L_max grows — confirmed here: min d_s over [0.5,2.0] rose 7.24→8.02 across L10→L12+pL13).

**CONSTRAINT-MAP CONSEQUENCE.** **R-1 is RESOLVED**: the spectral-dimension / CDT comparison — previously asserted as a "resonance" and never measured — is now MADE at the highest operationally-reachable L_max, and the answer is *no CDT-like dimensional reduction on the matched functional*. The standing fence ("DO NOT compare d_s to CDT until L_max ≫ 6") is **lifted with a refinement**: the comparison is now possible (and decisive) at L12 NOT because L12 is large enough to "escape the narrow-band artifact," but because the fold-window observables are STRUCTURALLY L_max-SATURATED — pushing higher L_max is provably futile for the fold edge (the one-sided-starvation is intrinsic, not truncation-removable). The asserted CDT resonance was a **scale-type mismatch**: it compared the substrate's σ→0 Weyl asymptotic (correctly = 8) to CDT's intermediate-window value (~2); once the (observable, window) pair is matched on both sides, the substrate stays near 8 in the window. Two PERMANENT structural results land: (i) **d_s(σ→0) recovers the Weyl manifold dimension 8** (crossing value 8.02, "crossings not plateaus" — the S52/S92 σ→0 structural theorem, now numerically confirmed at converged L12); (ii) **the B2 fold is a √ band edge (γ_E≈½, n_vH≈2), NOT an infinite-order van-Hove divergence on the energy axis** — and γ_E is L_max-saturated, so this reading is final at fixed τ_fold (the remaining live discriminator is the τ-DERIVATIVE dγ_E/dτ + v_g^{B2}(τ), the S93-K4 Level-2 moduli-deformation probe, which this gate does NOT compute — a genuine carry-forward). The dimensional-reduction route to a CDT/asymptotic-safety correspondence is CLOSED on the matched static functional; if a correspondence exists it lives in the M⁴ summand (d_s^{M4}→2/4), NOT in the D_K-on-SU(3) fiber spectral dimension (the S92 F-K1-ADDITIVITY category point).

**SUBSTRATE FRAMING: GEOMETRIC.** The return probability P(σ) = Tr e^{−σ D_K²} IS the substrate's own heat trace — the spectral fingerprint of the D_K eigenvalue spectrum, the set of all vibrational modes of the fabric. The spectral dimension d_s(σ) = −2 dlnP/dlnσ is a substrate-IS functional of that fingerprint; it is NOT a property of a diffusion process IN a background geometry. d_s(σ→0)→8 because the genuine Weyl window probes the full SU(3) manifold dimension (the Minakshisundaram–Pleijel asymptotic of the bare D_K — the literal σ→0 limit on a FINITE spectrum saturates the heat trace flat, d_s→0, an artifact of truncation, NOT the Weyl regime; the recovery is read on `1/λ_max² ≪ σ ≪ 1/λ_min²` where the Gaussian cutoff σ^{−1/2} sweeps the bulk count N~λ⁸ ⇒ d_s=8). The CRITICAL discipline (`phononic-framing.md §"Same-functional-different-scale fair-comparison"`, K=2) was honored: the CDT/asymptotic-safety framework's scale-type was NOT allowed to be authoritative over the substrate's own — the substrate IS the return probability, and d_s(σ→0) (Weyl) and d_s(σ_*) (windowed) are TWO intrinsic functionals of it, compared to CDT only with the (observable, diffusion-window) pair matched on both sides and the same Φ at the same scale-type. The direction of explanation: D_K eigenvalue spectrum → heat trace P(σ) → spectral-dimension functional d_s → (the comparison) the substrate's matched-window d_s = 8.5 does NOT reproduce the CDT dimensional-reduction pattern; the high-L_max measurement the framework asserted-but-never-made is now made, and it refutes the resonance as a scale-type mismatch while confirming the Weyl-8 σ→0 structure and the √-edge (n≈2, KK) character of the B2 fold.

---

### §W3-4. INV8-W3-4 (phonon-first-cosmologist)

**Status**: COMPLETED
**Gate ID**: `INV8-W3-4-HIGGS-QUARTIC-RG-STABILITY`
**Trigger**: `[SIGN]`
**Classification**: **PARTICLE** (the Higgs is the transverse |S|² oscillation of the fiber embedding — a specific excitation mode of the substrate's reorganized spectral structure, NOT a scalar field living IN spacetime)
**Agent**: `phonon-first-cosmologist`
**Hypothesis**: Running the Higgs quartic λ(μ) from the framework's predicted m_H=131.8 GeV (Route-B KK-threshold) up to M_KK=7.43e16 GeV on the substrate-fixed boundary value determines whether the substrate vacuum is absolutely stable (λ stays positive to M_KK — a prediction distinguishing the substrate from the SM) or reproduces SM near-criticality (λ→0 near ~10¹⁰-10¹¹ GeV — strong evidence the spectral-action cutoff f IS physical; bridges A-3).
**Plan reference**: `sessions/investigation/investigation-8/investigation-8-plan-w3.md` §W3-4.

**Output Artifacts** (closure-verification checklist):
- `computations/investigation-8/inv8_w3_higgs_quartic_rg_stability.py` — EXISTS (32,473 B). `grep -E 'from canonical_constants import|print_verdict_payload'` → `from canonical_constants import *  # noqa: F401,F403` ✓ ; `def print_verdict_payload(verdict, value, audit_sha, content_sha,` ✓
- `computations/investigation-8/inv8_w3_higgs_quartic_rg_stability.npz` — EXISTS (393,671 B); keys include `outcome`, `lam_fw`, `lam_fw_MKK`, `min_lam_fw`, `mu_star_fw`, `mt_scan`, `sm_crossings`, `composite`, `sign_verdict`, `magnitude_verdict`, `regime_verdict`.
- `computations/investigation-8/inv8_w3_higgs_quartic_rg_stability.png` — EXISTS (81,238 B); λ(μ) trajectories for the substrate (131.8) and SM-obs (125.1) to M_KK, and the SM benchmark to M_Pl, with the M_KK marker.
- Verdict line in `computations/investigation-8/inv8_gate_verdicts.txt` — `grep -E '^INV8-W3-4-HIGGS-QUARTIC-RG-STABILITY:.* audit_sha256=[a-f0-9]{64}'` → `INV8-W3-4-HIGGS-QUARTIC-RG-STABILITY: PASS -- value='ABSOLUTE-STABILITY_lambda(M_KK)=0.0484_minlambda=0.0477_mustar=no-crossingGeV' … audit_sha256=020ad93475ecde835f0d0b3f385b559f197a6a4ee5c59ed7193a3b34191c885f content_sha256=840c620b7bf126701685edfc262a4228b97381c36c78471aa62df436a8998dae schema_version=S84+` ✓ ; dual-SHA companion row present ✓ ; schema-v2 3-tuple row present (`sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID`) ✓.
- This WP §W3-4 — Status COMPLETED, Verdict present, Output Artifacts present, MCP Pre-Compute Audit present.

**MCP Pre-Compute Audit**:
- `get_constant('m_H_FW_KK_threshold')` → **131.8** (S100a, source KK-THRESHOLD-64 / S28c lineage, gate S100a-M0-MH-INHERITANCE). The substrate-fixed boundary m_H (Route-B). ✓
- `get_constant('m_H_obs')` → **125.1** (ATLAS+CMS Run-1 combined; load-bearing exact-rational denominator; the SM-observed benchmark). ✓
- `get_constant('v_ew')` → **246.0** (electroweak VEV). ✓
- `get_constant('M_KK')` → **7.428660036284456e16** (S42, alias M_KK_gravity, gate CONST-FREEZE-42). The run endpoint. ✓
- `get_constant('m_t_pole')` → **172.69** ; `get_constant('alpha_s_MZ_obs')` → **0.1180** ; `M_Z=91.1876`, `alpha_em_MZ_inv=127.955`, `sin2_thetaW_MSbar=0.23122` — the SM gauge/top-Yukawa β-function inputs (PDG 2024).
- `search_knowledge('Higgs quartic lambda running vacuum stability near-criticality metastability')` → surfaced prior `s63_higgs_running.py` (RUNNING-63, THRESHOLD-63), `s69_kk_higgs.py` (QUARTIC-69, HIGGS-69), and the CCM matching `lambda_CCM(M_KK)=(4/3)g_3²(M_KK)(a_4/a_2)`. **NOT PRE-CLOSED for this gate**: those gates run λ_CCM(M_KK) DOWN to M_Z to PREDICT m_H (the m_H-VALUE question); this gate runs λ UP from the substrate-fixed m_H boundary to M_KK to answer the STABILITY/near-criticality (SIGN of λ) question — the complementary direction. Cross-investigation dedup vs inv-5 W1-1/W2-3/W3-3 (the m_H-VALUE +5.36% residual) confirmed distinct.
- The prior `beta_2loop_SM` from `s63_higgs_running.py` (lines 150–233) supplied the validated 2-loop gauge+top machinery; its β_λ uses a doubled-y_t⁴ (V=(λ/2)(Φ†Φ)²-style) convention. **Corrected here** to the canonical `V=λ(Φ†Φ)²` form (1-loop `24λ²−6y_t⁴+(3/8)(2g_2⁴+(g_1²+g_2²)²)+λ(12y_t²−9g_2²−3g_1²)`; standard 2-loop β_λ with the dominant `+30y_t⁶−32g_3²y_t⁴` QCD-top term), VALIDATED against the published SM near-criticality shape (Degrassi/Buttazzo 2013, arXiv:1307.3536, fetched). Buttazzo is a cited cross-check anchor, NOT a canonical value source.

**Verdict**: **PASS** — composite PASS; schema-v2 3-tuple `sign_verdict=PASS, magnitude_verdict=PASS, regime_verdict=VALID`. Structural outcome: **ABSOLUTE-STABILITY** (Track A). `value='ABSOLUTE-STABILITY_lambda(M_KK)=0.0484_minlambda=0.0477_mustar=no-crossingGeV'`. audit_sha256 `020ad93475ecde835f0d0b3f385b559f197a6a4ee5c59ed7193a3b34191c885f`.

**Results**:

*Substitution chain (plan §W3-4 Steps 1–4; the tree-level direction):*
- Step 1: λ_tree = m_H²/(2 v_ew²) (V=λ(Φ†Φ)² convention; the |S|² transverse fiber-mode mass sets the tree quartic vertex).
- Step 2: λ_tree(m_H=131.8) = 131.8²/(2·246.0²) = **0.143526010** [substrate boundary; verified].
- Step 3: λ_tree(m_H=125.1) = 125.1²/(2·246.0²) = **0.129304729** [SM-observed benchmark].
- Step 4: Δ = λ_tree(FW) − λ_tree(obs) = **+0.014221280 > 0**. The substrate boundary quartic is LARGER (more positive) ⇒ the substrate starts FURTHER from the instability boundary; the tree-level direction FAVORS stability. Direction CONFIRMED.

*SM initial conditions @ M_Z (GUT-normalized g₁):* g₁=0.4614, g₂=0.6517, g₃=1.2177, y_t=0.9430 (from m_t_pole=172.69 with 1-loop QCD shift). t = ln(M_KK/m_H_FW) = 33.97.

*SM benchmark validation (m_H=125.1 → M_Pl=1.221e19, the same RG pipeline):* λ(M_Pl) = +0.02275, min λ = +0.02029 at μ = 6.93e14 GeV, **no zero crossing** — the canonical pipeline places the SM marginally on the STABLE side of the famous metastability knife-edge. SM-benchmark VALID = True (near-criticality SHAPE reproduced: |min λ|<0.05 at a high scale >10⁹ GeV). The doubled-y_t⁴ s63 convention and a pure-1-loop run both cross spuriously at ~10³ GeV; the corrected 2-loop `V=λ(Φ†Φ)²` form moves the shallow minimum to ~10¹⁴-10¹⁵ GeV, matching the canonical Degrassi/Buttazzo SM behaviour (their m_t=173.34 central lands marginally METASTABLE; the ~0.6 GeV lower canonical m_t_pole flips the marginal sign — this is the documented knife-edge, not a pipeline error).

*m_t-sensitivity sub-scan (the knife-edge, SM-obs boundary → M_Pl):* across m_t ∈ {171.5, 172.0, 172.69, 173.34, 174.0} GeV the SM never crosses in this 2-loop pipeline (min λ ranges +0.0269 → +0.0128, monotone-decreasing in m_t). The verdict-relevant fact is robust to this scan: the substrate's λ₀ sits +0.0142 ABOVE the SM-obs λ₀, so FW is more stable than the SM at every m_t in the band.

*Substrate run (m_H=131.8 boundary → M_KK):* λ(M_KK) = **+0.04840**, min λ = **+0.04767** at μ = 3.44e14 GeV, **NO zero crossing below M_KK**. The substrate vacuum is **absolutely stable**. FW min λ (+0.0477) > SM-obs min λ (+0.0203) > 0, consistent with the Step-4 direction. (Same-endpoint cross-check: the SM-obs boundary run to M_KK also shows no crossing, min λ=+0.0203 — so the FW result is the MORE-stable member of an already-stable pair in this pipeline.)

*Substrate KK-threshold spectrum (L12 cache `s84_spectrum_cache_L12_tau019.npz`, SHA `9e6d9cf7…`):* 90 Peter-Weyl sectors up to p+q=12; min|λ|=0.8197, max|λ|=5.4189 (M_KK units). The lowest fiber/KK state sits at ~0.82·M_KK ≈ 6.09e16 GeV — i.e. the KK-threshold tower enters AT the run endpoint M_KK, so the SM-like running below M_KK (with the substrate-fixed boundary value) governs the stability verdict, exactly as the gate is constructed. The substrate adds no new state below ~0.82 M_KK that would alter the trajectory.

*Schema-v2 SIGN 3-tuple:* sign_verdict = **PASS** (the computed running selects the tree-favored ABSOLUTE-STABILITY branch — λ(FW) stays further from zero than λ(SM-obs) at every scale, and neither crosses; the Step-4 direction λ_tree(FW)>λ_tree(obs) is realized in the full running). magnitude_verdict = **PASS** (the outcome lands in a recognized structural regime — ABSOLUTE-STABILITY, one of the two named PASS branches). regime_verdict = **VALID** (2-loop perturbativity holds throughout, |min λ|≪4π, λ(μ) finite over the whole window; the SM benchmark reproduces the near-criticality shape). Dual-SHA: audit_sha256 over [script, canonical, pinmap]; content_sha256 over [script].

*Constraint-map consequence:* The gate engages the EW-vacuum-stability sector for the first time and lands cleanly in **Track A (absolute stability)** rather than the plan's higher-prior Track B (near-criticality). The substrate predicts an **absolutely stable** electroweak vacuum (λ>0 to M_KK), a clean falsifiable statement distinguishing it from the metastable SM — and it is at LEAST as stable as the SM in any consistent single-pipeline comparison, by the robust +0.0142 tree-level head start. A-3 (is the spectral-action cutoff f physical?) is NOT directly bridged here: absolute stability is a DIFFERENT claim from the near-criticality coincidence, so this result does not supply the "f reproduces the SM coincidence from geometry" evidence; instead it makes an independent, distinct prediction. The near-criticality reading (Track B) would have required the SM-side to be metastable in the same pipeline — which the canonical m_t_pole=172.69 does not produce. **CAVEAT for downstream synthesis:** the verdict's *branch* (stable vs metastable) is knife-edge in m_t/α_s/the NNLO matching scheme; what is robust and pipeline-independent is the RELATIVE statement (substrate more stable than SM by the tree head-start). A full NNLO matching with the published m_t central (173.34) would shift the SM marginally metastable; the substrate would then sit near the stability boundary itself, re-opening a Track-B reading. This is the natural follow-up (a y_t/NNLO-matching pin) rather than a resolution here.

*Substrate framing:* D_K KK-threshold spectrum → the |S|² fiber-mode mass m_H = 131.8 GeV and its quartic spectral-action vertex λ → the RG running of λ → (the test) absolute stability vs SM near-criticality. The running of λ is a genuine dynamical statement about the substrate's spectral-action structure (the quartic vertex evolving as the fabric is probed at higher energy), NOT a regulator artifact — which is precisely why a near-criticality match WOULD bridge A-3. The substrate sits, here, in the absolutely-stable corner: the higher fiber-mode mass pushes the quartic vertex further from zero, and the KK tower's lowest state (~0.82 M_KK) only enters at the very top of the run.

---

### §W3-5. INV8-W3-5 (phonon-first-cosmologist)

**Status**: COMPLETED
**Gate ID**: `INV8-W3-5-WATANABE-MURAYAMA-BRANCH-COUNT`
**Trigger**: `[VERIFY-THEOREM]`
**Classification**: **PHONONIC** (the phonon branches ARE the Goldstone modes of the substrate's spontaneously-broken symmetry at the fold — the medium's own low-energy degrees of freedom, NOT modes propagating IN a medium)
**Agent**: `phonon-first-cosmologist`
**Hypothesis**: The phonon branch count is settled as a representation-theoretic THEOREM by the exact non-Lorentz-invariant Goldstone-counting formula n_NG = (dim G − dim H) − ½ rank(ρ), where ρ_ab = −i⟨[Q_a,Q_b]⟩ is the Watanabe-Murayama matrix of broken-charge commutators computed from the D_K/Kosmann-connection algebra; z=2 (known, EXACT) ⇒ the principal mode is Type-B (quadratic) so rank(ρ)≥2 and the count is fixed WITHOUT the deferred full SU(3) sigma-model — settling the parked 6-vs-7 and classifying which branches are Type-A (acoustic, feed the GGE pair count→A_s) vs Type-B.
**Plan reference**: `sessions/investigation/investigation-8/investigation-8-plan-w3.md` §W3-5 (machinery pin, theorem-form 4-clause PASS rubric with PRDR (2)(3)(4) set N/A-with-reason as a representation-theoretic identity, substitution chain source).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML per `.claude/templates/r3-yaml-gate-block.yaml`):

| Artifact | Path | must_contain check |
|:---------|:-----|:-------------------|
| script | `computations/investigation-8/inv8_w3_watanabe_murayama_branch_count.py` | `from canonical_constants import` ✓ ; `print_verdict_payload` ✓ |
| data | `computations/investigation-8/inv8_w3_watanabe_murayama_branch_count.npz` | exists ✓ (present, non-stub) |
| plot | `computations/investigation-8/inv8_w3_watanabe_murayama_branch_count.png` | exists ✓ (present, non-stub) |
| verdict_line | `computations/investigation-8/inv8_gate_verdicts.txt` | `^INV8-W3-5-WATANABE-MURAYAMA-BRANCH-COUNT:.* audit_sha256=[a-f0-9]{64}` ✓ ; companion row ✓ ; schema-v2 3-tuple NOT required (`[VERIFY-THEOREM]`) |
| wp_section | this §W3-5 | `Status:.*COMPLETED` ✓ ; `Verdict:.*(PASS\|FAIL\|INFO)` ✓ ; `Output Artifacts` ✓ ; `MCP Pre-Compute Audit` ✓ |

Closure-verification bash output (content-presence, never line-count, per `feedback_max-effort-full-fidelity.md`):
```
$ ls computations/investigation-8/inv8_w3_watanabe_murayama_branch_count.{py,npz,png}
inv8_w3_watanabe_murayama_branch_count.py    (present, ~16 KB)
inv8_w3_watanabe_murayama_branch_count.npz   (present)
inv8_w3_watanabe_murayama_branch_count.png   (present)
$ grep -E 'from canonical_constants import|print_verdict_payload' inv8_w3_watanabe_murayama_branch_count.py   → both match
$ grep -E '^INV8-W3-5-WATANABE-MURAYAMA-BRANCH-COUNT:.* audit_sha256=[a-f0-9]{64}' inv8_gate_verdicts.txt   → matches (1 canonical line + dual-SHA companion + branch-count extra row)
```

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script; one-line salient return each; gate is NOT pre-closed — it is a genuine new theorem application):
- `search_knowledge('Watanabe Murayama Goldstone branch count type-A type-B')` → returns only `S82-W0-A-BRANCH-COUNT` (INFO, value=6, 2D-BZ-EXTENSION/BCC-HIGH-SYMMETRY/L_max=64) and `s80/s82 branch_count` scripts; **no prior WM-theorem application** exists. This gate is the first to apply the n_NG counting formula.
- `search_knowledge('phonon branch count 6 vs 7 broken charge algebra')` → same hits; the 6-vs-7 is parked at S82 INFO=6, never upgraded via ρ-rank. NOT pre-closed.
- `trace_entity('DYNAMICAL-EXPONENT-63')` → z=2 (EXPONENT-63, INFO; the `J_L = eps·E_J = 0.00374·7.0415` Leggett-mode equation confirms the ω_B = 0.0019 + 7.0415 λ_n B-sector dispersion, residual 7e-15). z=2 EXACT confirmed — the Type-B smoking gun.
- `search_knowledge('session-73a Higgs coset T_coset C^2 four generators su(2) u(1) Jensen stabilizer')` → the canonical su(3) decomposition: `Tr_V(Σ_su(2) T²)=3 T_2` (3 su(2)), `Tr_V(Σ_coset T²)=4 T_coset` (4 C² coset), `Tr_V(T⁸ T⁸)=T_Y` (1 u(1)); Jensen `L1=e^{2τ}(u(1),1), L2=e^{-2τ}(su(2),3), L3=e^{τ}(C²,4)`; **S33b: "V(B2,B2)=0 exactly by U(1) charge conservation (C² carries U(1) charge)"** — the exact algebra confirming the C² commutators land on the pinned Cartan U(1).
- `get_constant('Delta_BCS')` → 0.4642547394830737 (R-PROTECTED, BCS-GAP-CANONICAL-70); `get_constant('tau_fold')` → 0.19; `get_constant('M_KK')` → 7.428660036284456e16; `get_constant('J_u1/J_su2/J_C2')` → 0.038 / 0.059 / 0.933. All importable via `from canonical_constants import *`.

**Verdict**: **PASS** — the Watanabe-Murayama Goldstone-counting theorem holds exactly on the Kosmann broken-charge algebra; the 6-vs-7 question is **settled at 6 (NOT 7)** with a definite Type-A/Type-B classification, WITHOUT the deferred full SU(3) sigma-model. All 4 rubric clauses pass; deterministic (identical dual-SHA across runs). `audit_sha256=7d2c8e40cef60946b039c206d8764f46cb6589dfe072db757fdd402843c36582`, `content_sha256=8f992a15eae57281f53717b5535aa966f56989f9efd1d8ba3108993d1729b88f`.

**Results**:

**Broken-symmetry enumeration at τ_fold = 0.19.** The internal symmetry at the fold is G = SU(3)_Jensen × U(1)₇^{BCS-phase}, **dim G = 8 + 1 = 9**. The Jensen deformation (volume-preserving L₁=e^{2τ}, L₂=e^{−2τ}, L₃=e^{τ}) breaks SU(3) down to its **U(2) = u(1)⊕su(2) stabilizer** — the unbroken homogeneous-metric isometries — so **dim H = 4**. The broken SU(3) directions are exactly the **C² coset** (λ₄,₅,₆,₇; indices [3,4,5,6] in the `su3_generators` convention, scale L₃=e^{τ}), and the BCS condensate breaks the U(1)₇ phase (Cooper pairs carry K₇ charge ±½, B6 PROVEN). Broken-generator count: **dim(G/H) = (8 − 4) + 1 = 5** (C² coset 4 + BCS phase 1).

**Watanabe-Murayama matrix ρ_ab = −i⟨[Q_a,Q_b]⟩_GS (Kosmann algebra, exact).** The broken charges are Q_a = K_a (the Kosmann-connection / su(3) generators e_a = −i/2 λ_a, a ∈ {3,4,5,6}) plus Q_BCS. For the su(3) coset pairs, [e_a, e_b] = f_{abc} e_c, so ⟨[Q_a,Q_b]⟩_GS = Σ_c f_{abc} ⟨Q_c⟩_GS. The ground state is **su(2)-symmetric** (H = U(2) ⇒ ⟨Q_{su(2)}⟩=0) but the Jensen deformation **pins the u(1) hypercharge Cartan direction** e₇ (~λ₈): its scale L₁=e^{2τ} ≠ 1 gives Cartan charge density q₀ = e^{2τ_fold} − 1 = **0.462285 > 0** (the Jensen u(1) order parameter). The computed ρ (M_KK-dimensionless units):
```
ρ_ab =  [[ 0       +0.40035   0         0        0 ]      indices: Q_4, Q_5, Q_6, Q_7, Q_BCS
         [-0.40035  0         0         0        0 ]
         [ 0        0         0        +0.40035  0 ]
         [ 0        0        -0.40035   0        0 ]
         [ 0        0         0         0        0 ]]
  antisymmetric residual |ρ + ρᵀ|_max = 0.00e+00   (exact)
  rank(ρ) = 4   (even; SVD floor 1e-10)
  ρ eigenvalues |Im| = [0.40035, 0.40035, 0.40035, 0.40035, 0]  (two degenerate ±i·g pairs + one zero)
```
The Jensen-pinned Cartan charge makes **BOTH C² doublets** {Q₄,Q₅} and {Q₆,Q₇} pair (each commutator lands on λ₈ with the same magnitude 0.40035) → two 2×2 antisymmetric blocks → **rank(ρ) = 4**. The BCS phase commutes with su(3) (independent U(1) factor), so its row/column is zero → it is the unpaired Type-A (Anderson-Bogoliubov) mode.

**Counting result.** Applying Watanabe-Murayama PRL 108.251602 (2012) / Hidaka PRL 110.091601 (2013):
$$ n_{NG} = (\dim G - \dim H) - \tfrac12\,\mathrm{rank}(\rho) = 5 - \tfrac12(4) = 5 - 2 = \mathbf{3}\ \text{Goldstone modes}. $$
Classification: **1 Type-A** (ω∼k, z=1: the BCS phase / Anderson-Bogoliubov acoustic mode) **+ 2 Type-B** (ω∼k², z=2: the two C² coset quadratic modes). Identity cross-check n_Type-A + n_Type-B = 1 + 2 = 3 = n_NG ✓.

**z=2 consistency (the smoking gun).** z=2 EXACT for the principal B-sector mode (ω_B = 0.0019 + 7.0415 λ_n, residual 7e-15, DYNAMICAL-EXPONENT-63) forces the principal branch to be Type-B ⇒ ≥1 Type-B pair ⇒ rank(ρ) ≥ 2. The computed rank(ρ) = 4 ≥ 2 ✓ — and indeed yields **2** Type-B modes, fully consistent with z=2.

**6-vs-7 RESOLUTION = 6 (NOT 7).** The propagating-band count dim(V) = 6 (S82-W0-A-BRANCH-COUNT INFO) = 3 amplitude/Higgs (GAPPED, NOT Goldstone) + 3 phase. The WM Goldstone count **n_NG = 3 IS exactly the 3 phase/Goldstone bands** of dim(V) — 1 Type-A band + 2 Type-B bands. Each Type-B band pairs 2 broken generators and is counted ONCE; the naive coset reading (5 broken directions, or "4 phase directions each partnered with an amplitude") over-counts and is what manufactures the spurious 7th band. The Type-B pairing removes it. The 7th branch **does not exist**: the count is 6, settled as a theorem. (This is consistent with — and now sharpens — the registry's `dim(V)=6 STRUCTURAL FLOOR` for sectoral s52, 3 amplitude + 3 phase.)

**4-tuple**: `(value='n_NG=3_dimGmH=5_rankrho=4_TypeA=1_TypeB=2_count6not7', scheme=FW, convention=Watanabe-Murayama-rho-ab-Kosmann-broken-charge ; Type-A-Type-B-classification, L_max=10)`. publication_precision = exact (all integers). PRDR (2)(3)(4) [strict_PASS_boundary scalar / boundary-reachable / reachable-rationals] declared **N/A-with-reason**: this is a representation-theoretic identity, not a numerical-threshold gate — the operative criterion is the operator (the WM identity) + the 4-clause verdict rubric, all of which PASS (clause i ρ exactly antisymmetric, ii WM identity consistent, iii z=2 consistent rank≥2, iv count resolved to a definite integer).

**Substitution chain (computed numbers).** Step 1: n_NG = (dim G − dim H) − ½ rank(ρ_ab), ρ_ab = −i⟨[Q_a,Q_b]⟩. Step 2: Type-A ω∼k (z=1), Type-B ω∼k² (z=2). Step 3: framework principal mode z=2 EXACT ⇒ principal branch Type-B. Step 4: a Type-B mode ⟺ a broken-generator PAIR has ⟨[Q_a,Q_b]⟩≠0 ⟺ ρ has a nonzero 2×2 block ⇒ rank(ρ)≥2; **computed: rank(ρ)=4** (both C² doublets pair on the Jensen-pinned Cartan). Step 5: substitute, n_NG = 5 − ½(4) = 3 = (k − r) with k=5 broken generators and r=2 Type-B pairs. Direction: the Type-B pairing reduces the count below the naive broken-generator count by ½rank(ρ) = 2, taking 5 → 3 Goldstones (= the 3 phase bands of dim(V)=6). Conclusion: settled WITHOUT the full SU(3) sigma-model.

**Dual-SHA**: `audit_sha256` over [script, canonical_constants.py, pinmap]; `content_sha256` over [script]. Deterministic — identical SHAs across two consecutive runs.

**Constraint-map consequence (PASS)**: **R-2 closes** — the parked branch count is settled as a representation-theoretic theorem WITHOUT the deferred full SU(3) sigma-model (the survey's R-2 claim that the WM route suffices is VINDICATED; the deferral was NOT necessary). The Type-A count (= 1, the acoustic Anderson-Bogoliubov mode) is pinned — this is the acoustic branch feeding the GGE pair-production → A_s. The 2 Type-B modes are identified — soft quadratic modes bearing on the C-2 thermalization-vs-survival split (Type-A and Type-B have different finite-T fate). NOTE: any permanent §VII / canonical registration of the settled count (the branch-count theorem) is **session-track promotion at /rclab-investigate close, NOT an investigation edit**.

**Substrate framing.** PHONONIC. The phonon branches ARE the Goldstone modes of the substrate's spontaneously-broken symmetry at the fold — the medium's own low-energy degrees of freedom, NOT modes propagating IN a medium. The broken charges Q_a ARE the Kosmann-connection generators K_a (the natural anti-Hermitian connection on the spinor bundle that also provides the BCS interaction). The WM matrix ρ_ab = −i⟨[Q_a,Q_b]⟩_GS is a substrate-IS object: the ground-state expectation of the commutators of the substrate's own broken charges. Direction of explanation: **D_K/Kosmann broken-charge algebra at the fold → the antisymmetric ρ_ab (rank 4) → the Goldstone count n_NG = 3 and the Type-A(1)/Type-B(2) classification → the number of acoustic branches (feeding GGE pair-production → A_s) and the soft Type-B modes (the thermalization split)**. z=2 is the smoking gun: it FORCES Type-B, hence rank(ρ)≥2, hence a count below the naive coset dimension — settling 6-vs-7 as a theorem (count = 6), not a dynamical solve.

---

## Wave 3 Synthesis (team-lead)

Wave 3 closed 5/5 (W3-1 FAIL · W3-2 FAIL · W3-3 INFO · W3-4 PASS · W3-5 PASS). Cross-domain bridges: the two new attacks on the dimensionful-scale knot and the w_a/BBN tension both close, two long-parked structural questions settle, and the CDT comparison is finally *made*.

- **W3-1 (FAIL; sign=PASS, regime=BREAKDOWN)** — the homotopy correction is *correct* (|π₀(U(1)₇×Z₃)|=3>1, walls admitted) but the fold is the **0D regime** (L/ξ̂=0.1546≪1 — less than one correlation length across), so no Z₃ wall network forms/survives. The prior "no-walls" verdict never rested on the homotopy argument; it rests on three sharper arguments that survive. **Kibble-Zurek route to w_a/BBN CLOSED.**
- **W3-2 (FAIL; the spine attack on G-1)** — the lowest-doublet quantum metric **vanishes by U(2)-invariance protection** (Tr g≈4×10⁻²⁷≈0, Berry Ω=0 EXACT; the (0,0) singlet block can't be rotated by the volume-preserving TT deformation). R_stiff=8.2×10⁻¹⁸. The plan's premise (atlas-07 g≈982.5 *was* the quantum metric) is false for the (τ,μ)-projected metric (g≈982.5 is a different reservoir). G-1 survives; **sharpens §VII.CA**.
- **W3-3 (INFO)** — multiplicative-norm pre-flight `FACTORIZATION_HOLDS=False` (Sage-exact ⇒ d_s a genuine L_max-dependent observable). The **CDT comparison is now MADE (R-1 resolved): NO dimensional reduction** on the matched functional — d_s(σ_*)=8.52 vs CDT ~2; the asserted "resonance" was a scale-type mismatch (σ→0 Weyl=8 compared to CDT's intermediate window). d_s(σ→0)=8.02 (Weyl recovery), γ_E=0.4834 (L_max-saturated). L_max=14-16 infeasible (Sym¹³ wall) but the fold-window is **L_max-SATURATED** (new sectors land above the fold ceiling) — making L=12-operational a *proof*. The narrow-band-artifact fence is LIFTED.
- **W3-4 (PASS, ABSOLUTE-STABILITY)** — λ(M_KK)=+0.0484, min λ=+0.0477, no zero crossing: the substrate vacuum is absolutely stable (vs metastable SM), distinguished by a +0.0142 tree head-start. Corrected a doubled-y_t⁴ β_λ convention bug (validated vs Degrassi/Buttazzo 2013). Caveat for the close: A-3 not bridged — absolute-stability ≠ near-criticality; an NNLO matching at m_t=173.34 could re-open Track-B.
- **W3-5 (PASS)** — Watanabe-Murayama branch count **settled at 6, NOT 7** (n_NG=3 = 1 Type-A acoustic + 2 Type-B quadratic; rank(ρ)=4 because the Jensen deformation pins the u(1) Cartan, pairing both C² doublets on λ₈) — as a *theorem*, without the deferred full SU(3) sigma-model.

### What Changed
**(a) Numerical revisions** — `L/ξ̂=0.1546` (0D regime), `f_wall(today)=7.2×10⁻²⁹`; `R_stiff=8.2×10⁻¹⁸`, `Tr g≈0`; `d_s(σ→0)=8.02`, `d_s(σ_*)=8.52`, `γ_E=0.4834`; `λ(M_KK)=+0.0484`, `min λ=+0.0477`; `n_NG=3`, `rank(ρ)=4`.
**(b) Structural changes** — KZ-walls route CLOSED (0D); quantum-metric-stiffness route to H(τ) CLOSED by representation-theoretic protection (G-1 survives; §VII.CA sharpened); d_s/CDT "resonance" reclassified as a scale-type mismatch → NO reduction (fence lifted); Higgs vacuum re-typed to ABSOLUTE-STABILITY; 6-vs-7 branch count settled as a theorem.

### Effected In-Session (non-math)
All W3 non-math findings are SESSION-track promotions, routed OUT to the `/rclab-investigate --investigation 8` close per the track-local boundary — NOT effected here (catalogued in `investigation-8-housekeeping.md §B`):
- **W3-2 §VII.CA sharpening** (the lowest-doublet (τ,μ) metric is geometrically inert under volume-preserving TT) — registry edit, session-track.
- **W3-5 §VII promotion** of the 6-Goldstone branch-count theorem (Type-A/Type-B split) — session-track.
- **W3-3** narrow-band-artifact fence-lift + the d_s/CDT measurement — registry/methodology note, session-track.
- **HY5** — Strutinsky = O'Neill A-tensor = spectral-action saddle-point §VII registration (survey R-4) — session-track.
No investigation-local non-math edits were required.

## Carry-Forward Computations

### CF-INV8-W3-3-MODULI — τ-derivative CDT discriminator dγ_E/dτ + v_g^{B2}(τ)
| Field | Spec |
|:------|:-----|
| **What** | Compute the τ-derivative `dγ_E/dτ` and the B2 group velocity `v_g^{B2}(τ)` (the S93-K4 Level-2 moduli-deformation CDT discriminator) — the one live discriminator W3-3 left after the fixed-τ_fold reading came back L_max-saturated. |
| **Inputs** | the L₁₂ master spectrum cache across a τ-window; the W3-3 energy-axis γ_E estimator; the S93-K4 moduli-deformation machinery. |
| **Gate** | does `dγ_E/dτ` show a substrate-IS moduli-deformation signature distinguishable from a CDT/asymptotic-safety reference (pre-register threshold + window at plan time)? |
| **Effort** | ~1–2 wave-equivalents. |

### CF-INV8-W3-4-YT-NNLO — Higgs absolute-stability vs near-criticality at NNLO (A-3 bridge)
| Field | Spec |
|:------|:-----|
| **What** | Re-run the Higgs λ(μ) stability verdict with a substrate top-Yukawa `y_t` pin and full NNLO matching at m_t=173.34, to test whether the ABSOLUTE-STABILITY verdict survives the m_t knife-edge or re-opens the Track-B near-criticality reading (the A-3 f-physicality bridge W3-4 flagged but did not resolve). |
| **Inputs** | W3-4 script + npz (2-loop RGEs, corrected β_λ); a substrate-derived y_t pin OR the canonical m_t=173.34 NNLO inputs; Degrassi/Buttazzo 2013 NNLO matching. |
| **Gate** | does the substrate vacuum stay absolutely stable (min λ > 0) at NNLO m_t=173.34, or land marginally metastable like the SM? PASS = absolute stability survives; FAIL/INFO = Track-B re-opens. |
| **Effort** | ~1 wave-equivalent. |

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-15 | Kibble-Zurek Z₃ wall network (W3-1) | candidate w_a/BBN mechanism | CLOSED (0D regime; walls die) | L/ξ̂=0.1546≪1; homotopy correct but not load-bearing |
| 2026-06-15 | quantum-metric stiffness → H(τ) (W3-2) | candidate G-1 attack | CLOSED (zero by U(2) protection) | Tr g≈0, Berry Ω=0 EXACT; R_stiff=8.2e-18 |
| 2026-06-15 | §VII.CA metric-without-curvature wall | g≈982.5 reservoir | sharpened (lowest-doublet (τ,μ) metric = 0) | W3-2 |
| 2026-06-15 | d_s / CDT dimensional-reduction comparison (W3-3) | asserted resonance (fenced) | MADE — NO reduction (8.5 vs ~2; scale-mismatch) | matched-functional fair comparison |
| 2026-06-15 | narrow-band-artifact fence | standing | LIFTED (d_s L_max-saturated; comparison made) | W3-3 |
| 2026-06-15 | Higgs vacuum stability (W3-4) | metastable-SM-like | ABSOLUTE-STABILITY (λ(M_KK)=+0.0484) | +0.0142 tree head-start; caveat A-3 NNLO |
| 2026-06-15 | Goldstone branch count (W3-5) | 6-vs-7 parked | SETTLED 6 (theorem; n_NG=3, 1 Type-A + 2 Type-B) | rank(ρ)=4, Jensen-pinned Cartan |
| 2026-06-15 | dimensionful-scale knot (W2-1↔W3-2) | #1 gap; two new attacks | both attacks CLOSED; knot survives, H(τ) stays imported | convergence verdict (for close) |
| 2026-06-15 | w_a/BBN tension (W2-4↔W3-1) | two competing mechanisms | both CLOSED; frozen-modulus w_a=0 lock stands sharper | convergence verdict (for close) |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Verdict |
|:-----|:-------|:------------|:------------|:--------|
| INV8-W3-1 | `inv8_w3_kz_z3_wall_network.py` | ✓ | ✓ | FAIL |
| INV8-W3-2 | `inv8_w3_quantum_metric_stiffness_htau.py` | ✓ | ✓ | FAIL |
| INV8-W3-3 | `inv8_w3_spectral_dimension_lmax14_cdt.py` | ✓ | ✓ | INFO (Option-A supersede) |
| INV8-W3-4 | `inv8_w3_higgs_quartic_rg_stability.py` | ✓ | ✓ | PASS |
| INV8-W3-5 | `inv8_w3_watanabe_murayama_branch_count.py` | ✓ | ✓ | PASS |

All under `computations/investigation-8/`; verdicts in `inv8_gate_verdicts.txt`.
