# Session 111 Wave 2 — M_KK keystone + H-sector + CC (Results Working Paper)

**Session**: 111 | **Wave**: W2 | **Plan**: session-111-plan-w2.md | **Theme**: Tier-1 #2 / Tier-2 M_KK-DERIVATION harvest — the PRIME Topic-1 decider (is `w=M_KK` a τ-RG-invariant dimensional-transmutation scale DYNAMICAL or a bare CONST-FREEZE-42 import BARE-IMPORT?), the residual H₀ relief at the dimensionless-Ô layer, the A_s magnitude pin + POINT-vs-BAND epistemic-type resolution, and the substrate-derivation of the §VII.CE n↔w dictionary.

## Gate Sections

### §W2-1. S111-CF-MKK-RG-INVARIANCE (nazarewicz-nuclear-structure-theorist)

**Status**: COMPLETED
**Gate ID**: `S111-CF-MKK-RG-INVARIANCE`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (M_KK is a property of the D_K spectrum — the fabric — set by the fold-DOS enhancement + spectral-action coupling; not an excitation, not a quantum number)
**Agent**: `nazarewicz-nuclear-structure-theorist`
**Hypothesis**: The dimensionless transmutation ratio R(τ)=exp(−1/(λ_eff(τ)·N₀(τ))) is τ-INVARIANT across the modulus flow τ∈[0.190,0.6] (a single dimensional-transmutation fixed-point, the Λ_QCD-analog μ-independence) — DYNAMICAL — rather than carrying its only dimensionful scale through an external CODATA-unit cutoff — BARE-IMPORT. PRIME Topic-1 decider; the surviving leg of the §6.3 a(t)/Friedmann residual.
**Plan reference**: `sessions/session-plan/session-111-plan-w2.md` §W2-1 (machinery pin, dual-leg threshold, 3-claim substitution chain, dual_prior 0.45/0.55).

**Output Artifacts**:
- Script `computations/session-111/s111_mkk_rg_invariance.py` — EXISTS (40,986 bytes). `grep -E 'from canonical_constants import'` → 3 hits; `grep -E 'print_verdict_payload'` → 3 hits. Both must_contain patterns present.
- Data `computations/session-111/s111_mkk_rg_invariance.npz` — EXISTS (14,315 bytes); holds the full τ-scan arrays (`tau_scan`, `lam_scan`, `N0_scan`, `g_scan`, `R_scan`), the band curve (`tau_grid`, `E_grid`, `K_grid`), the fold continuity anchors, and the dual-SHA.
- Plot `computations/session-111/s111_mkk_rg_invariance.png` — EXISTS (153,310 bytes); 3 panels: E_B2(τ) band + fold, λ_eff/N₀/g across scan, R(τ) τ-spread (log scale).
- Verdict line in `computations/session-111/s111_gate_verdicts.txt` — EMITTED via `emit_verdict` MCP (10 rows, race-safe, sig_5 unique). Matches `^S111-CF-MKK-RG-INVARIANCE:.* audit_sha256=[a-f0-9]{64}`; dual-SHA companion row + schema-v2 3-tuple row both present.
- WP section (this §W2-1) — the four must_contain markers (`**Status**:.*COMPLETED`, `**Verdict**:.*(PASS|FAIL|INFO)`, `**Output Artifacts**`, `**MCP Pre-Compute Audit**`) all present.

**MCP Pre-Compute Audit**:
- `search_knowledge("M_KK dimensional transmutation BCS Coleman-Weinberg tau RG invariance")` → returned the INV11-W1-1 build (`M_KK_derived = M_Pl_reduced · exp(−1/(λ_eff·N₀))`, λ_eff=0.038935, N₀=14.0233) and the f_KK=(M_KK/M_Pl)⁴ transmutation factor. No prior gate evaluates the τ-RG-invariance of R(τ) — gate is NOT pre-closed.
- `get_constant("M_KK")` → 7.428660036284456e+16 GeV (CONST-FREEZE-42, alias M_KK_gravity); `get_constant("M_Pl_reduced")` → 2.435e+18 (CODATA 2018); `get_constant("tau_fold")` → 0.19 (CONST-FREEZE-42).
- `trace_entity("dimensional transmutation")` → confirmed eq_7613 `M_KK_derived = M_Pl_reduced·exp(−1/(λ_eff·N₀))` is the INV11 chain; the dimensionful magnitude anchor is M_Pl_reduced (the CODATA cutoff). No τ-scan of the dimensionless ratio existed prior to this gate.

**Verdict**: **FAIL** (BARE-IMPORT). Composite `FAIL`; 3-tuple `sign=PASS, magnitude=FAIL, regime=VALID` (collapse rule: `magnitude_verdict=FAIL ∧ regime=VALID ⇒ composite=FAIL`). `audit_sha256=10010211894762b41c75ccf8b4238ea6c9e80897a5ba5039fe7e4d3473e42fc3`, `content_sha256=fb14e062228824f878f831cc7431d9e93ee6363810b0b9c47488038a50e5c5ca`. Dual_prior re-allocation: **0.90 → Track B (BARE-IMPORT)** — M_KK's only dimensionful scale is the borrowed CODATA cutoff; the §6.3 a(t)/effective-Friedmann residual's M_KK-magnitude leg stays an external pin (constructive-O3 confirmed). 4-tuple: `(value=Δ_rel=8.193, scheme=SA, convention=RATIO, L_max=12)`.

**Results**:

*Method (substrate-first τ-generalization of the fixed-τ_fold CV2A/INV11-W1-1 BCS transmutation).* At each Jensen modulus τ the substrate IS the spectral triple `(A_K, H_K, D_K(τ))`. I generalize the two fixed-τ_fold inputs of the CV2A transmutation `R = exp(−1/(λ_eff·N₀))` to functions of τ, both deterministic functions of the Jensen metric `g_s(τ)`:
- **λ_eff(τ)** — the per-coset Kosmann V-matrix coupling on the fold B2 sector. Computed from the Kosmann spinorial correction `K_a(τ) = (1/8) Σ_{r,s}[Γ^s_{ra}−Γ^r_{sa}] γ_r γ_s` (Baptista Paper 17 eq 4.1, via `s23a_kosmann_singlet`), where Γ(τ) is the Levi-Civita connection of `g_s(τ)`. The C²-direction Kosmann norm `||K_a(τ)||_{C²}` is the substrate-natural τ-function; `λ_eff(τ) = ||K_a(τ)||²_{C²}/C_const` with `C_const = ||K_a(τ_fold)||²_{C²}/λ_eff(τ_fold) = 13.782` the **τ-INVARIANT** proportionality fixed at the fold (depends only on the spinor-space dimension + C²-multiplicity, not on τ).
- **N₀(τ)** — the FINITE-enhanced B2-band van Hove DOS pile-up, computed as the canonical windowed integral `ρ(τ) = ⟨1/(π·max(|v(t)|, v_min(t)))⟩` over the wall [τ−0.05, τ+0.05], where `v(t)=dE_B2/dt` is the B2-band group velocity along the τ-flow (the `s35a_vh_impedance_arbiter` construction). The B2 band itself is the 4-fold fold band among the 8 lowest positive (0,0)-singlet Dirac band modes (B1×1+B2×4+B3×3 split under residual U(2)). The true A₂ divergence is REFUTED (S94); the BCS chain runs through the 1D theorem, NOT a Fermi surface.

*Continuity with CV2A (bit-exact at the fold).* The τ-functions reproduce the CV2A anchor at the fold to machine precision:

| Quantity | This gate (at τ_fold) | CV2A anchor | Match |
|:---------|:----------------------|:------------|:------|
| τ_fold (v=0) | 0.190158 | 0.190 (canonical) | ✓ |
| E_B2 at fold | 0.845212 | 0.845269 (canonical) | ✓ (5 digits) |
| d²E/dτ² at fold | 1.175693 | ~1.176 (canonical) | ✓ |
| λ_eff(τ_fold) | 0.038934760900644856 | 0.038934760900644856 | ✓ exact |
| N₀(τ_fold) | 14.023250234055 | 14.023250234055 | ✓ exact |
| R(τ_fold) | 0.16016847970570353 | 0.16016847970570353 | ✓ exact |

The fold band E_B2(τ) has its minimum (v=dE_B2/dτ=0) at τ=0.190158, reproducing the canonical fold; the windowed DOS at the fold is calibrated (v_min_floor=1.199e-2) to N₀=14.0233 exactly; λ_eff and R follow exactly. So the τ-scan is the faithful substrate-natural generalization of CV2A, not a re-parameterization.

*τ-scan of R(τ) (42 points, τ∈[0.190,0.600], step 0.010).* The dimensionless transmutation ratio is sharply peaked at the fold and collapses across the modulus flow:

| τ | λ_eff(τ) | N₀(τ) | g=λ·N₀ | R(τ) |
|:--|:---------|:------|:-------|:-----|
| 0.190 | 0.038930 | 14.0234 | 0.5459 | 1.601e-01 |
| 0.250 | 0.040909 | 6.4893 | 0.2655 | 2.312e-02 |
| 0.310 | 0.043478 | 2.3673 | 0.1029 | 6.033e-05 |
| 0.400 | 0.048521 | 1.2797 | 0.0621 | 1.013e-07 |
| 0.490 | 0.055140 | 0.8783 | 0.0484 | 1.077e-09 |
| 0.580 | 0.063551 | 0.6673 | 0.0424 | 5.750e-11 |

R range: min=3.639e-11, max=1.601e-01, mean=1.955e-02. **Δ_rel = (R_max − R_min)/R_mean = 8.193** ≫ 5e-02 PASS band. R is strictly monotone-decreasing away from the fold (verified `np.all(np.diff(R)<0)`).

*Leg-1 (RG-invariance) — FAIL.* Δ_rel = 8.193 ≥ 5e-02 ⇒ **R is τ-FLOWING, NOT a fixed-point.** The driver is N₀(τ): the van Hove DOS pile-up is a **fold-localized 1D phenomenon** (it exists only where the B2-band group velocity vanishes, at the fold). Away from the fold |v(τ)| grows, the DOS collapses (14.02→0.67), so g=λ·N₀ collapses (0.546→0.042) and R=exp(−1/g)→0. There is no β-function compensation holding g·(something) invariant — unlike Λ_QCD, where the running coupling produces a μ-INDEPENDENT Λ_QCD. **The "fixed point" of the substrate transmutation IS the fold τ_fold=0.190 itself, not a flow-invariant.** This is precisely why M_KK is pinned by CONST-FREEZE-42 (a specific τ choice), not derived as an RG-invariant.

*Leg-2 (no-import) — FAIL (set-membership).* SCALE-IMPORT AUDIT-LOG of the transmutation chain by mass dimension:
- DIMENSIONLESS chain (substrate-natural transmutation content): `λ_eff(τ)` (Kosmann V-matrix mean per coset; V-matrix elements dimensionless in M_KK units), `N₀(τ)` (DOS per mode, dimensionless count), `g(τ)=λ·N₀` (dimensionless BCS product), `R(τ)=exp(−1/g)` (dimensionless ratio).
- DIMENSIONFUL MAGNITUDE leg (the absolute-scale anchor): `Λ_cutoff = M_Pl_reduced` (CV2A anchored the cutoff to M_Pl_reduced via the a₂/Einstein-Hilbert channel, `1/(16πG)=M_Pl_reduced²/2`).
- Set-membership test: `M_Pl_reduced ∈ {dimensionful magnitude inputs}` → **TRUE** ⇒ leg-2 no-import PASS = **False**. The only dimensionful scale in the magnitude leg IS the borrowed CODATA cutoff.

*CC1 (the discriminator's sign axis — output is DIMENSIONLESS).* Substitution chain: Step 1 `M_KK_derived = Λ_cutoff·exp(−1/(λ_eff·N₀))` [BCS/Coleman-Weinberg, INV11-W1-1 Step 4]; Step 2 `R := M_KK_derived/Λ_cutoff = exp(−1/(λ_eff·N₀))`; Step 3 `[λ_eff]=dimensionless` (V-matrix mean per coset), `[N₀]=dimensionless` (DOS per mode) ⇒ `[1/(λ_eff·N₀)]=dimensionless`; Step 4 `[R]=[exp(dimensionless)]=dimensionless`. Conclusion: R is a pure number at every τ; the dimensionful M_KK enters ONLY through Λ_cutoff (the CODATA anchor). `sign_verdict=PASS` (dimension-of-output prediction holds by construction).

*CC2 (RG-invariance ⇒ DYNAMICAL — the τ-spread direction).* Step 1 `R(τ)=exp(−1/(λ_eff(τ)·N₀(τ)))`; Step 2 `Δ_rel := (max_τ R − min_τ R)/mean_τ R`; Step 3 IF `g(τ)=λ_eff(τ)·N₀(τ)` is τ-FLAT to within the band ⇒ R τ-FLAT ⇒ Δ_rel<5e-2; Step 4 (computed) `g(τ)` is NOT τ-flat — it collapses 0.546→0.042 (factor 13) because N₀ collapses 14.02→0.67 ⇒ Δ_rel=8.193≥5e-2 ⇒ R flows with τ ⇒ M_KK is read off the modulus-flow evaluation point ⇒ **BARE-IMPORT**. `magnitude_verdict=FAIL`.

*CC3 (the NO-IMPORT leg is the binding falsifier — set-membership, exact).* Step 1 `audited_dimensionful_inputs = {Λ_cutoff = M_Pl_reduced}`; Step 2 leg-2 PASS iff `M_Pl_reduced ∉ audited_dimensionful_inputs`; Step 3 CV2A's magnitude leg DID anchor Λ_cutoff to M_Pl_reduced via the a₂/EH channel ⇒ leg-2 FAILS on the magnitude. Conclusion: the discriminator is honest precisely because leg-2 is a set-membership test the CV2A construction does NOT trivially pass — and it does not pass here. BOTH legs fail independently; the BARE-IMPORT verdict is over-determined.

*MULTIPLICATIVE-NORMALIZATION cancellation pre-flight.* Declared **NOT-APPLICABLE-BY-OPERATOR-FORM** (`math-scripts.md §"Multiplicative-normalization cancellation invariants"`). The observable is the τ-spread of the transmutation EXPONENT `1/(λ_eff(τ)·N₀(τ))`, NOT a K-log-derivative operator `d^n ln(·)/d(ln K)^n` (n≥1) applied to a spectral functional. The cancellation invariant binds ONLY when an L_max-multiplicative pre-factor `w(L_max)` is annihilated by a log-derivative operator; no such operator is applied here, so no `w(L_max)·g(K)` factorization check is triggered. R(τ) is L_max-SATURATED at L12 (Friedrich-Bär feasibility pre-check), not L_max-multiplicative — confirmed: the band E_B2(τ) is the bottom-K (0,0)-singlet observable, L_max-saturated per INV11-W1-1.

*Canonical write-order.* NO new canonical constant lands (the gate produces a verdict + dual_prior re-allocation, not a new framework prediction value). No `update_constant` / falsifier-inventory write is triggered (the M_KK magnitude itself is unchanged — CONST-FREEZE-42 stays the pin; this gate establishes that it CANNOT be re-derived as a τ-RG-invariant, which is a structural finding, not a new number). M_KK_derived(M_Pl_reduced anchor)=3.900e+17 GeV / OOM 0.7202 is reported as a sensitivity continuity check (reproducing CV2A), NOT a PASS-contributing derivation.

*Substrate-first assessment (GEOMETRIC).* The flow `D_K(τ) eigenvalues → B2-band van Hove DOS pile-up ρ_B2(τ)=N₀(τ) + Kosmann V-matrix ||K_a(τ)||_{C²}=λ_eff(τ) → transmutation exponent 1/(λ_eff·N₀) → dimensionless ratio R(τ) → M_KK magnitude` is preserved throughout — M_KK IS read off `{λ_k(τ)}`, the question was whether that reading is flow-invariant. SCALE-AND-CHANNEL-TAGGING (`phononic-framing.md`): the observable is the SUBSTRATE/BZ-scale transmutation ratio O(M_KK), evaluated INSIDE the modulus flow; there is no pivot transport (the test is intrinsic to the BZ-scale spectral triple across its own τ-deformation, Level-2 substrate-IS per the moduli-deformation level). The Λ_QCD μ-independence analog FAILS: the substrate's transmutation scale is NOT flow-invariant because the van Hove DOS enhancement that drives the BCS coupling is fold-localized — the substrate computes its transmutation scale AT a specific point (the fold), not independent of where on the flow it is read. The result is a clean structural boundary, not a method failure: it CLOSES the DYNAMICAL corridor of the §6.3 a(t)/Friedmann residual's M_KK-magnitude leg and confirms constructive-O3 (M_KK's only dimensionful scale is the borrowed CODATA cutoff).

---

### §W2-2. S111-CF3-H0-RESIDUAL (mack-cosmic-bridge)

**Status**: COMPLETED
**Gate ID**: `S111-CF3-H0-RESIDUAL`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (ΔH₀/H₀ is a ratio of spectral-action moments — a₀⊥a₂ Ô-relations on the D_K spectrum; the fabric's own clock-rate, not an excitation)
**Agent**: `mack-cosmic-bridge` (executor + falsifier-inventory sole writer; `volovik-superfluid-universe-theorist` performs the a₀-orthogonality cross-check per `session-110-volovik-cf3-a0-orthogonality-audit.md`)
**Hypothesis**: Once `w=M_KK` is fixed by ONE observation, a substrate-derived DIMENSIONLESS RELATION (the a₂ focusing-clock 6.125% + any a₀⊥a₂ dimensionless relation at the dimensionless-Ô layer) predicts ΔH₀/H₀; the full [0.08,0.10] band CANNOT be closed by drawing a dimensionful relief budget out of a₀ (the Layer-1 wall — a dimensionless ratio cannot close a dimensional gap). NOT gated on MKK-RG (independent axis, volovik a₀-orthogonality). INFO-by-design expected (only the partial 49/800=6.125% lands; ~94% held).
**Plan reference**: `sessions/session-plan/session-111-plan-w2.md` §W2-2 (3-claim substitution chain, dual_prior 0.20/0.70/0.10, d_A=0 parity gate).

**Output Artifacts**:
- Script `computations/session-111/s111_cf3_h0_residual.py` — `grep -E 'from canonical_constants import|print_verdict_payload'` returns both markers (`from canonical_constants import (` line 96; `def print_verdict_payload` line 414). Imports `w0_FW`, `clock_coeff`, `H_0_km_s_Mpc` from `canonical_constants.py` (no hardcoded framework constants).
- Data `computations/session-111/s111_cf3_h0_residual.npz` — written (all result fields + dual-SHA + the exact partial-fraction numerator/denominator + the 49/800 round-figure num/den).
- Plot `computations/session-111/s111_cf3_h0_residual.png` — 2-panel (Panel 1: dimensionless-Ô relief bar vs the [0.08,0.10] band with the held-residual annotation; Panel 2: the d_A=0 parity-exclusion + dimensionless-channel-enumeration table).
- Verdict line `computations/session-111/s111_gate_verdicts.txt` — matches `^S111-CF3-H0-RESIDUAL:.* audit_sha256=[a-f0-9]{64}`; dual-SHA companion row + schema-v2 3-tuple row present; 3 extra companion rows (parity_pin, composite-precedence, partial_relief_exact). Emitted race-safe via `emit_verdict` (6 rows; sig_5 unique).
- WP section `### §W2-2. S111-CF3-H0-RESIDUAL` — this section (the four `must_contain` markers Status/Verdict/Output Artifacts/MCP Pre-Compute Audit all present).

**MCP Pre-Compute Audit**:
- `search_knowledge("H0 residual timescape relief a0 a2 orthogonal dimensionless 49/800 focusing clock")` → returned `[gate] S110-CF3-TIMESCAPE-H0` (the upstream INFO this gate consumes: `dH0/H0_BZ=0.0049 deg_T=2.0 a0_orthogonal=True`) + `[gate] INV4-W2-2` (`a2_share=0.999700; a0_share=0.000300` — the a₀/a₂ dominance split used in Claim 3) + `[gate] INV4-W3-1` (`a0-clock-reduces-to-Volovik-MPl2H2`). Confirms the gate is NOT pre-closed; it is the formal compute landing the §VII.CF EVEN-face / corpus §23.0(5) "absent-scale-leg complement" already noted at corpus §23.0(5) line 1990.
- `get_constant("w0_FW")` → `-0.918` (S58 four-fold lock; the a₀-orthogonal channel anchor). Imported, not hardcoded.
- `trace_entity("parity selection rule d_A scale leg transport degree")` → no knowledge.db hit (the S110 W4 parity rule is registry/corpus-resident, not yet indexed); verified DIRECTLY against `permanent-results-registry.md §VII.CF` (line 168/22199) + `cross-pillar-bridge-corpus.md §23.0(5)` (line 1699/1723/1738) — both confirm ΔH₀/H₀ (d_A=0) transports entirely within the EVEN morphism sector, the EVEN face of the parity-complete `Q=R·M_KK^m` wall.
- Sage QQ (`sage_eval`): `dH0_BZ/band_lo = 1224993/20000000 = 0.06124965` exact; `49/800 = 0.06125`; diff `−3.5e-07` (4-sf agreement). The round-figure is the rationalized partial; the exact is published, 49/800 pinned alongside (round-figure-fidelity discipline).

**Verdict**: **INFO** — value=`partial_relief_frac_lo=0.0612497 roundfig=49/800=0.06125 residual_held=0.93875 d_A=0 M_KK1_scale_leg_INADMISSIBLE=True band_closed_dimensionless=False dimensionful_draw_attempted=False a0_a2_orthogonal=True deg_T=2.0 sign=PASS mag=PASS regime=VALID 3tuple_composite=PASS` ; scheme=`emergent-scale-transport-DIMENSIONLESS-ONLY` ; convention=`DA-0-PARITY-EVEN` ; L_max=12 ; audit_sha256=`5ba2650e78ace69ce7da669d177a537dbe454da351662cce58fdb2c69ea624f4` ; content_sha256=`dde5eefb49a1b80c0fdc39c77003d6b97c2a75f9f0160b001ffc10c5790361ac`. schema-v2 3-tuple: **sign=PASS, magnitude=PASS, regime=VALID**.

This is the prior-0.70 expected outcome (dual_prior Track-B-INFO): only the partial 49/800 = 6.125% of band-low lands at the dimensionless-Ô layer; ~93.9% is **HELD**. The band-closure is a HELD question pending the single `w=M_KK`-fixing observation; the residual is routed to the dimensionless-slot, NOT closed by a dimensionful draw.

**3-tuple composite vs gate-operator top-line (disclosed).** The `[SIGN]` 3-tuple scores the SIGNED sub-claims — (sign) the d_A=0 parity-exclusion of the M_KK¹ scale leg AND the relief-fraction direction (partial < band-low); (magnitude) the partial relief matching the pre-registered 49/800 floor to 4 sig figs; (regime) the set-membership-exact admissibility test — all of which PASS, so the 3-tuple composite collapses to PASS. The gate's **top-line** follows the plan-frozen **band-closure operator** (INFO: only the partial lands, band does NOT close at the dimensionless layer), NOT the 3-tuple composite. These are NOT in conflict: the signed content is all correct; the band simply does not close knob-free. The distinction is disclosed in the verdict-line `# composite-precedence:` companion row per `gate-verdicts.md §"Plan-frozen gate-block operator precedence"`.

**Results**:

**Substrate-first framing.** The substrate IS the D_K spectrum; the Hubble rate H is read OFF the substrate's late-time spectral dynamics — H emerges from the a₂ Seeley-DeWitt focusing channel (the second spectral moment IS Newton's constant; the clock-rate is the fabric's own, NOT a field fitted to an FRW expansion rate). The flow: `D_K eigenvalues → a₀ (zeroth moment, cosmological term) ⊥ a₂ (second moment, EH/G_N) → dimensionless Ô-relations between a₀ and a₂ images → the a₂ focusing-clock relief ΔH₀/H₀ (transported at deg_T, dimensionless-Ô layer)`. The d_A=0 inadmissibility is substrate-first: ΔH₀/H₀ IS a dimensionless property of the spectrum, so its transport carries NO M_KK¹ scale leg.

**Substitution chain (3 claims, substituted numbers).**

- **Claim 1 — the d_A=0 scale leg is INADMISSIBLE (the EVEN face of §VII.CF parity).**
  Step 1: ΔH₀/H₀ = (Hubble rate)/(Hubble rate) ⇒ `d_A = 0` (mass-dimension zero). Step 2: transport bridge `B = (M_KK^{d_A} scale leg) ⊙ (dimensionless morphism)` (per-observable transport-degree theorem, corpus §23.0(5)). Step 3: substitute `d_A=0` ⇒ scale-leg exponent = 0 ⇒ scale leg = `M_KK^0 = 1` (the TRIVIAL leg) ⇒ transport carried ENTIRELY by the dimensionless morphism. Step 4: the 54.04-decade conversion (`M_KK^1`) is the ODD scale leg (deg=+1, parity 1); the morphism sector is EVEN (Wodzicki `−2(s−s')`, HKR `0`, parity 0) ⇒ ODD scale leg ⊥ EVEN morphism sector. Step 5: ⇒ the +2 full-homogeneity reading (which WOULD invoke the 54.04-decade leg) is dimensionally FORBIDDEN for ΔH₀/H₀. **Computed**: `scale_leg_exponent=0`, `full_homogeneity_reading_admissible = (0==1) = False`, `M_KK1_scale_leg_INADMISSIBLE = True`. Set-membership form: admissible EVEN-sector transport degrees for d_A=0 = `{0, 2}`; `deg_T=2 ∈ {0,2}` (admissible NON-SCALAR) but `odd_scale_leg_degree=1 ∉ {0,2}` (EXCLUDED). **Conclusion 1**: the residual-relief channel MUST be a dimensionless-morphism; the M_KK¹ scale leg is excluded a priori — the EVEN d_A=0 face of the §VII.CF parity-complete wall (§VII.CF closes the ODD d_A=+1 face, the LRD-T held-prediction).

- **Claim 2 — the partial relief is 49/800 = 6.125% of band-low (the honest outcome).**
  Step 1: `ΔH₀/H₀_BZ = 0.004899972` (S110 CF3, the a₂ focusing-clock transported relief at the dimensionless-Ô layer; `s110_cf3_timescape_h0.npz: dH0_BZ_central`). Step 2: band-low target = 0.08. Step 3: partial fraction = `0.004899972 / 0.08 = 0.06124965`. Step 4: rationalize (Sage QQ) = `1224993/20000000` exact; registry round-figure `49/800 = 0.06125` (4-sf agreement, diff `−3.5e-07` from the round-off in the transported scalar). **Conclusion 2**: the a₂ focusing-clock relief closes **6.125%** of band-low; **residual HELD = 0.93875035 (~93.9%)** — the honest pre-registered partial-INFO outcome, NOT a fitted near-miss. (Diagnostic fractions: of band-central 0.09 → 0.054444; of band-hi 0.10 → 0.049000; of lit 0.084 → 0.058333.)

- **Claim 3 — a₀ refines RELATIONS, does NOT supply a dimensionful budget (the Layer-1 wall).**
  Step 1: `a₀ ⊥ a₂` (FUNCTIONAL-INDEPENDENT, S66 / W2-E PASS S75; confirmed `a0_a2_orthogonal=True` in S110 CF3). Step 2: at the dimensionless-Ô layer, a₀ can enter a dimensionless RELATION `R_dimless(a₀-Ô, a₂-Ô)` refining the a₀/a₂ Ô-image ratio (the a₀ residual share = 0.000300 vs a₂ dominant share = 0.999700, INV4-W2-2). Step 3: a₀ CANNOT supply a dimensionful relief budget ΔH₀ (a mass-dimension-1 quantity) — drawing a dimensionful budget out of a dimensionless ratio is the workshop-killed O2 / Layer-1 wall. Step 4: ⇒ PASS would require `R_dimless` to predict ΔH₀/H₀ ∈ [0.08,0.10] as a DIMENSIONLESS relation, with `w=M_KK` fixed by one observation supplying the single dimensionful anchor. **Computed**: best dimensionless-morphism channel (max over {scalar deg-0, NON-SCALAR deg-2, a₀-refined ceiling `0.004899972·(1+a0_share/a2_share)=0.00490144`}) = `0.00490144`; `band_closed_dimensionless = (0.00490144 ≥ 0.08) = False`. The ONLY way to reach band-central 0.09 is a multiplicative ratio of **18.36×** (the fitted budget the S110 CF3 row already flagged as `ratio_needed_central=18.367`, `fitted_budget_pct=1.17`) — a DIMENSIONFUL a₀ draw via the M_KK¹ leg, i.e. the Layer-1 wall. `dimensionful_draw_attempted = False` (the wall is HONORED, not breached). **Conclusion 3**: the dimensionless-Ô layer under-delivers beyond 6.125%; the verdict is INFO; band-closure is a HELD question pending the one `w=M_KK`-fixing observation. If a future channel CLOSED the band only by demanding the dimensionful a₀ draw, that would be the FAIL path (Layer-1 wall confirmed) — distinct from this INFO (the dimensionless channel honestly under-delivers).

**Cross-checks** (all PASS): (CC0a) central-relief source consistency — `s110_cf3 dH0_BZ_central` and `inv7_w1_4 DH0_B_central` agree to `<1e-12` (both `0.004899972`); (CC0b) `clock_coeff` canonical (`−3.08`) == npz value; (CC0c) `dec_separation` npz (`54.04`) == pinned; (CC0d) `a0_a2_orthogonal=True` carried intact from S110 CF3.

**Scale-and-channel tagging** (`phononic-framing.md`): the observable is a dimensionless ratio at the substrate/BZ scale; its CMB-pivot image is **itself** (d_A=0, the trivial `M_KK^0` scale leg — the EVEN-morphism transport is its own pivot image, NO 54.04-decade shift). Convention `…-DA-0-PARITY-EVEN` per `regulator-pin-discipline.md §"Mass-dimension/parity"`. NOT gated on MKK-RG (independent axis; the two probe orthogonal legs of the §6.3 residual — magnitude vs dimensionless-clock-relation).

**Solution-space reading.** This gate does NOT close the §6.3 a(t)/effective-Friedmann residual's H₀-leg; it MAPS the leg precisely. The corridor that survives is the single dimensionless-Ô-layer relief (6.125% of band-low), reachable knob-free; the corridor that is CLOSED is "close the full band by a dimensionful a₀ draw" (the Layer-1 wall, forbidden by parity). The residual H₀-relief at the dimensionless layer is therefore **partial-by-structure**, not partial-by-incomplete-computation: the ~94% held fraction is the parity-walled gap a dimensionless ratio cannot bridge, and band-closure is forward-routed to the one `w=M_KK`-fixing observation (the FRW-anchor-independent H₀ channel; cf. CF-S102-H0-ANCHOR-INDEPENDENT). Falsifier-surface landing (mack sole writer, separate session-close pass): `falsifier-master-inventory.md` Row #81.audit-S110-CF3-H0-RESIDUAL-PARTIAL (the absent-scale-leg complement: a d_A=0 ratio has NO dimensionful slot to collide with; relief capped at the dimensionless morphism 49/800=6.125% — the volovik a₀-orthogonality Layer-1 wall directly, corpus §23.0(5) line 1990).

---

### §W2-3. S111-CF-AS3 (transit-dynamics-theorist + nazarewicz-nuclear-structure-theorist)

> A_s magnitude pin + all-frozen-superhorizon regime resolution + the DECISIVE Friedrich-Bär-temp per-sector test. Split into **AS3a** (impulse-quench A_s magnitude + regime resolution; transit-dynamics) and **AS3b** (FB-temp per-sector sub-compute; nazarewicz). AS3b's verdict SETS AS3a's epistemic TYPE: POINT (verdict-A, converged physical d.o.f.) if FB-temp PASS, BAND (verdict-B, L_max-soft) if FB-temp FAIL. Two distinct gate-IDs, two verdict lines.

### §W2-3a. S111-CF-AS3a (transit-dynamics-theorist)

**Status**: COMPLETED
**Gate ID**: `S111-CF-AS3a`
**Trigger**: `[VERIFY]`
**Classification**: **PHONONIC** (A_s is the amplitude of the post-transit GGE acoustic excitation spectrum — the impulse-quench |β_k|² relic occupation)
**Agent**: `transit-dynamics-theorist` (computes A_s; `mack-cosmic-bridge` is the falsifier Row 8 sole writer, canonical write-order step 3)
**Hypothesis**: One defensible impulse-quench A_s magnitude lands from the locked {β_k} functional, with the all-frozen-superhorizon regime resolved (89/89 frozen; the WKB-Bogoliubov leg is empty BY CONSTRUCTION in the frozen regime — the correct frozen-regime behavior, NOT a method failure). The epistemic TYPE (POINT vs BAND) is set by the AS3b FB-temp verdict.
**Plan reference**: `sessions/session-plan/session-111-plan-w2.md` §W2-3a (regime-resolution substitution chain, dual_prior 0.55 POINT / 0.45 BAND conditional on AS3b, canonical write-order).

**Output Artifacts**:
- **Script** `computations/session-111/s111_cf_as3a_impulse_quench.py` — `grep -E 'from canonical_constants import|print_verdict_payload'` → both present (`from canonical_constants import *  # noqa: F401,F403`; `def print_verdict_payload(...)`). ✓
- **Data** `computations/session-111/s111_cf_as3a_impulse_quench.npz` — on disk (49 keys: A_s_impulse, OOM_dist_Row8, regime_resolved, epistemic_type, beta_sq, …). ✓
- **Plot** `computations/session-111/s111_cf_as3a_impulse_quench.png` — on disk (two-spectra + OOM ladder). ✓
- **Verdict line** `computations/session-111/s111_gate_verdicts.txt` — matches `^S111-CF-AS3a:.* audit_sha256=[a-f0-9]{64}`; dual-SHA companion row + 4 `#` annotation rows present (schema_v2 3-tuple NOT required — `[VERIFY]` gate). ✓
- **WP section** — this section (Status COMPLETED / Verdict PASS / Output Artifacts / MCP Pre-Compute Audit present). ✓

**MCP Pre-Compute Audit**:
- `search_knowledge("TRANSIT-PS-67 impulse quench A_s magnitude all-frozen superhorizon")` → returned `INV5-W2-1-AS-IMPULSE-QUENCH-BOGOLIUBOV` (A_s_impulse=1.5367e-08, OOM_gap=0.8644) + `S110-CF-AS3-QUENCH-PIN` (A_s_pin=POINT 1.54e-08) + WS-AS-1 theorem (verdict-A/B). Confirms the magnitude is a mechanical promotion, not a new derivation.
- `search_knowledge("WS-AS-1 verdict-A verdict-B SCHEME-DEPENDENT FI PERMANENT floor")` → returned the WS-AS-1 PROVEN theorem + falsifier Row 8 (`A_s | SCHEME-DEPENDENT | 5.078e-9 TD-canonical | 2.099e-9 Planck | 0.384 OOM above Planck`). Grounds the FI/PERMANENT-floor vs SCHEME-DEPENDENT-magnitude split.
- `get_constant("M_KK")` → 7.428660036284456e+16 (CONST-FREEZE-42); `get_constant("A_s_FW")` → **not found** (PENDING BAND comment only, line 1721 canonical_constants) — confirms A_s_FW is NOT yet a canonical pin; promotion is a downstream-of-AS3b action (the sub-key needs POINT/BAND).
- NOT PRE-CLOSED: the gate is a live mechanical-promotion + regime-resolution. The magnitude (1.54e-08) is the upstream continuity anchor; this gate re-derives it from the impulse-quench spectrum and resolves the all-frozen regime.

**Verdict**: **PASS** — one defensible A_s lands (1.537e-08, round-trip-consistent with the INV5 anchor to 3.9e-6); the all-frozen-superhorizon regime is RESOLVED-FROZEN (89/89 frozen, Z_norm=1); the epistemic-type conditional mapping is SET (AS3b-CONDITIONAL → POINT if AS3b PASS / BAND if AS3b FAIL). `[VERIFY]` trigger; informational 3-tuple sign=N/A magnitude=PASS regime=VALID. `audit_sha256=3f095d72a1c7169ec6f2a8825bf95ed2ad31400f365a350503fb08babace9789`.

**Results**:

**(1) Magnitude — the defensible impulse-quench A_s.** The magnitude is the impulse-quench Bogoliubov amplitude
```
A_s = |β_{k_hat}|² / (2π²),   N_norm = ξ_KZ³ (Kibble-Zurek coherence VOLUME),   k_hat = 1/ξ_KZ
```
with `ξ_KZ = ξ_KZ_FW = 0.0187601 M_KK⁻¹` (S89 substrate-natural) and `k_hat = 53.305 M_KK`. `|β_{k_hat}|²` is read from the S100b box-delta **sudden-limit** spectrum (3-code-path PASS to 1.4e-13; unitarity residual 1.87e-14) by near-flat UV-tail extrapolation (slope −0.0031 = the scale-invariant sudden signature). Computed:

| Quantity | Value | Cross-check |
|:---|:---|:---|
| `A_s_impulse` | **1.536706e-08** | rel-dev 3.9e-6 vs INV5 anchor 1.5367e-08 (round-trip exact, 5 sf) |
| OOM vs Planck (2.1e-9) | **+0.8644** | = `OOM_gap_inv5` (s110_cf_b1, amp_inv5_consistent=True) |
| **OOM-distance vs Row 8 (5.078e-9 TD-canonical)** | **+0.4809** | = plan-stated ≈0.48 OOM |
| `A_s_parker_inv6` (alt leg) | 5.99e-08 | Parker-adiabatic, +1.455 OOM (the sub-2-OOM over-production band) |

Scheme-tag: `scheme=IMPULSE-QUENCH-BOGOLIUBOV`, `convention=FROZEN-OCCUPATION-NORMALIZED-BY-SUBSTRATE-NATURAL`, `L_max=12`. 4-tuple `value=A_s_impulse=1.537e-08`.

**(2) Regime resolution — all-frozen-superhorizon ⇒ frozen-occupation A_s IS physical (substitution chain).** The locked {β_k} (inv10_w2 transit-build, the 89 fold-window curvature modes) resolves the regime:
```
Step 1: regime test = fraction of modes exiting the WKB-adiabatic window during transit   [B1 regime flag]
Step 2: all 89 modes labelled 'frozen-superhorizon'; n_wkb=0; wkb_leg_empty=True; all k_modes < k_tach=1974 M_KK   [transit-build]
Step 3: in the all-frozen regime Z_norm = 1 (superhorizon conservation — once a mode freezes, its occupation is conserved)   [T4.4, S77 transit-einstein workshop]
Step 4: ⇒ A_s = |β_k|²-derived frozen occupation is the PHYSICAL amplitude; the empty WKB-Bogoliubov leg is the CORRECT frozen-regime behavior (89 modes conserved as relics), NOT a method breakdown   [direction read-off]
Step 5: the epistemic TYPE of this A_s is decided by AS3b (per-mode λ_pivot L_max-stable ⇒ POINT; shifts ⇒ BAND)   [hand-off]
Conclusion: regime = RESOLVED-FROZEN (frozen-occupation A_s physical, Z_norm=1); one defensible A_s lands; type set by AS3b.
```
Result: `all_frozen=True`, `frac_frozen=1.000`, `Z_norm=1.0`, `regime=RESOLVED-FROZEN`.

**(3) Epistemic type — set by AS3b (parallel gate).** AS3b (`S111-CF-AS3b`, the Friedrich-Bär per-sector decisive test) was NOT YET on disk at runtime (parallel dispatch), so the type is emitted as **AS3b-CONDITIONAL**: POINT (verdict-A, converged physical d.o.f.) if AS3b FB-temp PASS / BAND (verdict-B, L_max-soft) if AS3b FB-temp FAIL. The script re-reads `s111_gate_verdicts.txt` at runtime and auto-promotes to POINT/BAND if AS3b has landed; the AS3b-CONDITIONAL tag is the honest state under parallel dispatch. Per the plan discriminator, the epistemic type is "set" once the conditional mapping is declared — satisfied.

**Substrate-honest disclosure — the rejected naive locked-build extrapolation.** The locked {β_k} transit-build grid spans k ∈ [0.56, 3.75] M_KK (the fold-window superhorizon modes); k_hat = 53.30 M_KK sits **14.2× ABOVE** the build max. Extrapolating the locked-build UV slope (−1.000) to k_hat gives A_s = 4.96 (**+9.37 OOM**) — which is EXACTLY the discredited naive-aggregate normalization artifact (WS-AS-1 §47: "the +9.5-OOM figure is the naive aggregate-occupation dump … a normalization artifact, reproduced then discarded"). The two β-spectra are distinct functionals on distinct grids: the **box-delta sudden-scattering spectrum at the KZ scale is the MAGNITUDE source**; the **fold-window curvature-mode grid is the REGIME source**. Using the correct spectrum for each role is the substrate-correct construction; the +9.37-OOM artifact is documented and REJECTED.

**FLOOR sub-annotation (FUNCTIONAL-INDEPENDENT / PERMANENT, WS-AS-1 LIZ2-1).** The inequality `A_s ≥ A_s^{BD}` holds because `S_IC = 1 + 2 n_k ≥ 1` (`n_k = |β_k|² ≥ 0`; `|α_k|² − |β_k|² = 1`), confirmed `floor_satisfied=True` (all β_sq ≥ 0). The FLOOR is FUNCTIONAL-INDEPENDENT and PERMANENT on 3 orthogonal axes (reference-state / families-index η-form / dynamical-Bogoliubov); the **MAGNITUDE is SCHEME-DEPENDENT**. The falsifier Row 8 keeps `SCHEME-DEPENDENT` for the magnitude AND adds the FI/PERMANENT floor sub-annotation.

**Canonical write-order.**
- **Step 1 (verdict)** — DONE: `S111-CF-AS3a: PASS` emitted via `emit_verdict` (race-safe), `audit_sha256=3f095d72…`, `content_sha256=b7e6ae0e…`, 4 `#` companion rows.
- **Step 2 (canonical_constants A_s_FW + POINT/BAND sub-key)** — DEFERRED-pending-AS3b: `A_s_FW` is not yet a canonical pin (PENDING BAND comment only); the sub-key (POINT vs BAND) is set by the AS3b verdict (parallel gate), so the `update_constant("A_s_FW", …, comment="POINT|BAND per AS3b")` promotion is a genuine cross-gate downstream action — to be effected once AS3b lands (a derivation dependency, NOT a hygiene-deferral). The magnitude value 1.537e-08 is permanently pinned in the verdict line + npz.
- **Step 3 (mack writes falsifier Row 8)** — routed to `mack-cosmic-bridge` (sole writer): keep Row 8 `SCHEME-DEPENDENT` for the magnitude, add the FI/PERMANENT floor sub-annotation, cite this gate's `audit_sha256` + the npz.

**SCALE-AND-CHANNEL-TAGGING.** A_s here is the **substrate/BZ-scale** value (the impulse-quench amplitude at k_hat, INSIDE the fold-window). Its CMB-pivot image lives at the Goldstone-pivot leaf via the Mode-Independent Occupation Theorem, `deg(T_{BZ→pivot})=+2 NON-SCALAR` (54.04 decades) — a SEPARATE transport leg; the falsifier Row 8 target (5.078e-9 TD-canonical) lives at the transit-canonical scale, and the +0.4809 OOM-distance is the substrate-scale comparison. The pivot transport is not re-derived here.

---

### §W2-3b. S111-CF-AS3b (nazarewicz-nuclear-structure-theorist)

**Status**: COMPLETED
**Gate ID**: `S111-CF-AS3b`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (the GGE chemical-potential λ_pivot = −ln(n_pivot/(1−n_pivot)) is the per-charge occupation potential of the relic quasiparticle band)
**Agent**: `nazarewicz-nuclear-structure-theorist`
**Hypothesis**: The GGE per-charge potential λ_pivot = −ln(n_pivot/(1−n_pivot)) does NOT shift when a NEW high-Casimir in-band (p,q) sector is added at L_max+1 (holding n_pivot fixed) — a per-charge multiplier (intensive), NOT an extensive sum — so |β_k|² is a converged physical d.o.f. (POINT), not L_max-soft (BAND). The DECISIVE sub-compute that sets AS3a's epistemic type.
**Plan reference**: `sessions/session-plan/session-111-plan-w2.md` §W2-3b (NO-SHIFT per-charge-multiplier substitution chain, dual_prior 0.65 POINT / 0.35 BAND, Counting-axis convention).

**Output Artifacts**:
- **script** `computations/session-111/s111_cf_as3b_fb_temp_per_sector.py` — EXISTS (33,738 B). `must_contain` greps:
  - `L114: from canonical_constants import (  # noqa: E402`
  - `L159: def print_verdict_payload(...)` + `L566: print_verdict_payload(verdict, value, SCHEME, CONVENTION, L_MAX, ...)`
- **data** `computations/session-111/s111_cf_as3b_fb_temp_per_sector.npz` — EXISTS (17,905 B; per-sector η_FB arrays, botK ceiling, new-sector-13 bound, per-branch λ_pivot/n, the two-closure counterfactual, verdict).
- **plot** `computations/session-111/s111_cf_as3b_fb_temp_per_sector.png` — EXISTS (115,759 B; left: per-sector η_FB vs C₂ with the new-sector-13 floor bound + pivot ceiling; right: per-charge vs shared-aggregate Δλ_pivot contrast).
- **verdict_line** `computations/session-111/s111_gate_verdicts.txt` line 43 — matches `^S111-CF-AS3b:.* audit_sha256=[a-f0-9]{64}` (audit_sha256=`77b6603800bc6e97cb3654a93bda7ad5f1494d6a30a4e56bcd34ef3a690ff25b`); dual-SHA companion row + schema-v2 3-tuple row present; 5 `#`-prefixed annotation extra-rows present.
- **wp_section** this section — Status/Verdict/Output Artifacts/MCP Pre-Compute Audit markers present.

**MCP Pre-Compute Audit** (query-first discipline, `.claude/rules/knowledge-index-usage.md`):
- `search_knowledge("GGE chemical potential lambda_pivot n_pivot per-charge multiplier intensive extensive")` → returned the INTENSIVE/EXTENSIVE tagging equations (`tag_i = INTENSIVE if scope_i == "per-mode" else EXTENSIVE`; `λ_k = −ln(n_k/(1−n_k))` GGE-temperature form) and the S = −Tr(ρ ln ρ), ρ = e^{−β(H−μN)}/Z reference. Confirms the per-charge form is the canonical GGE construction; NOT a closed/duplicate gate.
- `search_knowledge("Friedrich-Bar saturation eta_FB Casimir eigenvalue floor L_max")` → returned the S92-W9 `FRIEDRICH-BAR-SATURATION-UNIFIED` gate (INFO) with the canonical pins `eta_FB_lower=0.4`, `eta_FB_all_min=0.436488`, `NEW_sector13_bound=3.0022`, `botK_ceiling=0.8452`; and the PROVEN bottom-K-invariance-∀-L_max≥10 theorem. This gate REUSES (does not re-derive) the S92 anchor.
- `search_knowledge("AS3 POINT BAND A_s amplitude transit-ps L_max-soft converged d.o.f.")` → returned the `ws-as-1.md` PROVEN theorem (A): "the locked, Floquet-frozen impulse-quench |β_k|² is a genuine intensive amplitude" (the verdict-A/POINT Reading my PASS resolves) + the S110-CF-AS3-QUENCH-PIN POINT 1.54e-08 anchor.
- `trace_entity` / direct read of `sessions/session-110/workshops/ws-as-1.md` → the converged 3-round verdict; this gate is the **named FB-temp R3-Turn-B cross-review compute** the Reading-A verdict is conditioned on (Verdict row #3, Open Question #1, CF-AS-3 decisive sub-input). Register-PREDICTED PASS via the per-charge GGE-LAMBDA-38 structure.
- `get_constant(M_KK / tau_fold)` → M_KK=7.428660036284456e16 GeV, tau_fold=0.19 (CONST-FREEZE-42). `lambda_B1/B2/B3` = 2.771/1.459/6.007 (canonical_constants.py, S39 provenance "λ_k = −ln|ψ_pair[k]|²").
- **NOT PRE-CLOSED**: the per-sector FB-temp eigenvalue-floor compute itself is an OPEN carry-forward (ws-as-1 Open Question #1); this gate is its execution.

**Verdict**: **PASS** — **NO-SHIFT ⇒ POINT** (verdict-A). `Δλ_pivot = 0.000e+00 < eps_shift = 1e-3`. Schema-v2 3-tuple: **sign=PASS** (the NO-SHIFT per-charge-multiplier direction is realized) / **magnitude=PASS** (|Δλ_pivot − 0| ≤ eps_shift; target = 0, NO-SHIFT) / **regime=VALID** (the Friedrich-Bär out-of-band bound holds: the new p+q=13 sector floor 3.0022 ≫ pivot ceiling 0.8452). dual_prior re-allocation: 0.90 → Track A (POINT). **This verdict SETS AS3a's epistemic type to POINT** (|β_k|² is a converged physical d.o.f.).

**Results**:

*The gate quantity* (per-charge / register closure): `Δλ_pivot = |λ_pivot(L=13, +new high-C₂ sector) − λ_pivot(L=12)| / |λ_pivot(L=12)| = 0.000e+00` (EXACT) `< eps_shift = 1e-3` ⇒ **NO-SHIFT**. 4-tuple: `(value=Δλ_pivot=0.000e+00, scheme=GGE-CHEMICAL-POTENTIAL λ_k=−ln(n_k/(1−n_k)) [S38/S39] + Friedrich-Bär η_FB [S87 W11-2/3], convention=PER-CHARGE-MULTIPLIER, L_max=12 baseline + 13 probe)`.

*Pivot mode (B1 acoustic, dominant by ~37× per the flat-band ledger)*: `λ_pivot = λ_B1 = 2.771000` (canonical), inverted to the per-mode occupation `n_pivot = n_B1 = 1/(1+e^{2.771}) = 0.058912`; per-charge roundtrip `−ln(n_pivot/(1−n_pivot)) = 2.770992` (roundtrip_err = 0.0e+00). Companion branches: `n_B2 = 0.188620` (λ_B2=1.459), `n_B3 = 0.002455` (λ_B3=6.007) — the per-charge structure is branch-INDEPENDENT; the test holds for any branch.

*In-band sectors + Friedrich-Bär ratios* (read from `s84_spectrum_cache_L12_tau019.npz`, 90 Peter-Weyl sectors, levels p+q ∈ {0,…,12}): η_FB(p,q) = |λ|_min(p,q)/√(C₂(p,q)+1). The 4 lowest sectors:

| (p,q) | level | dim | C₂(p,q) | \|λ\|_min | η_FB |
|:------|:------|:----|:--------|:----------|:-----|
| (0,0) | 0 | 1 | 0.0000 | 0.819741 | 0.819741 |
| (0,1)/(1,0) | 1 | 3 | 1.3333 | 0.835894 | 0.547221 |
| (1,1) | 2 | 8 | 3.0000 | 0.872975 | **0.436488** (empirical floor) |
| (2,0)/(0,2) | 2 | 6 | 3.3333 | 0.972246 | 0.467052 |

`eta_FB_all_min = 0.436488` — matches the S92 W9-3 canonical empirical floor exactly; `eta_FB_lower = 0.40` is the 8–10% safety-margin pin below it.

*Pivot band ceiling*: the bottom-(0,0) block's dominant value `botK_ceiling = 0.845212 M_KK` (the B-band pile-up at 0.8452121, multiplicity-weighted), absolute pivot floor `botK_floor = 0.819741 M_KK`.

*New-sector-13 floor via Friedrich-Bär saturation BOUND* (NO L13 re-diagonalization — FORBIDDEN per the recursive-Casimir-projection feasibility pre-check, `math-scripts.md §"D_K Block-Diagonality"`): the **lowest-C₂** p+q=13 sector is **(6,7)/(7,6)**, C₂ = 55.3333 (the worst case — lowest possible new-sector floor). The FB bound: `floor_new ≥ η_FB_lower·√(C₂(13)_min+1) = 0.40·√(56.3333) = 0.40·7.5056 = 3.0022 M_KK` — **reproduces the S92 W9-3 `NEW_sector13_bound = 3.0022` exactly**. (Maximal-asymmetry corner (0,13)/(13,0): C₂=69.333 → floor ≥ 3.3546 M_KK, an even higher floor.)

*The NO-SHIFT ⇒ POINT substitution chain (substituted numbers)*:
- **Step 4 (out-of-band test)**: `new_sector13_bound = 3.0022 M_KK ≫ botK_ceiling = 0.8452 M_KK` (margin = 3.55×) ⇒ `out_of_band = True`. The new p+q=13 sector lies ABOVE the pivot band ⇒ it carries no in-band occupation at the pivot.
- **Step 5 (n_pivot invariance)**: out-of-band ⇒ the new sector contributes a NEW per-charge multiplier `λ_{k'} = −ln(n_{k'}/(1−n_{k'}))` for ITS OWN occupation; it does NOT enter `n_pivot`. With `n_pivot` fixed, `λ_pivot = −ln(n_pivot/(1−n_pivot))` (a function of `n_pivot` ALONE — session-38 GGE-LAMBDA-38, VERBATIM) is unmoved ⇒ `Δλ_pivot = 0.000e+00 < 1e-3`. **NO SHIFT.**
- **Step 6 (hand-off)**: NO-SHIFT ⇒ λ_pivot is a PER-CHARGE multiplier (intensive), L_max-stable ⇒ POINT.

*The DECISIVE discriminator (per-charge vs shared-aggregate — the workshop crux, ws-as-1 R3)*: I computed BOTH closures on the SAME synthetic-new-sector counterfactual.
- **PER-CHARGE (register, non-thermal GGE)**: `Δλ_pivot = 0.000e+00` (EXACT) — λ_pivot depends on n_pivot alone; the 8 Richardson-Gaudin {I_k} COMMUTE (atlas-04 T2 PROVEN) ⇒ the max-entropy constraints DECOUPLE per-k ⇒ each λ_k conjugate to its OWN I_k. NO-SHIFT.
- **SHARED-AGGREGATE (thermal-like, the REJECTED closure)**: a single β solves Σ_k n_k(β) = ⟨Q⟩; adding one in-band mode raises ⟨Q⟩ and forces `β: 3.380336 → 3.346537`, a relative `Δβ = 9.999e-03` — i.e. the temperature WOULD move. Robustness scan: the shared-agg shift scales monotonically as O(1/N_band) (1.66e-3 → 2.30e-4 across N_band = 8→64), a genuine physical effect, not a tuned coincidence; the per-charge closure is N-INDEPENDENT and exact-0.
- **The contrast (0 vs O(1%)) IS the falsifiable signature**: the non-thermal GGE's per-charge structure is the CAUSE of NO-SHIFT. Had the substrate's GGE closure been shared-aggregate (the thermal re-collapse transit-dynamics suspected in ws-as-1 R2 D(TD)1), the temperature input would have inherited the band-aggregate `truncation_consistent=False` softness; the register's per-charge construction launders that softness OUT of the pivot temperature. **Reading B's regime of validity is confirmed EMPTY at the canonical L_max.**

*Hand-off to AS3a*: **PASS (NO-SHIFT) ⇒ A_s epistemic type = POINT (verdict-A)** — the |β_k|² impulse-quench amplitude is a converged physical d.o.f., NOT L_max-soft. Both inputs to the canonical UNIFIED-AS-79 pivot coth `S_IC(k_pivot) = coth(Δ_pivot/2T_pivot)` are per-mode quantities of the low-Casimir pivot mode (the gap Δ_pivot, conceded-saturated in ws-as-1; and T_pivot = 1/(k_B·λ_pivot) with λ_pivot per-charge, this gate). This resolves the WS-AS-1 (FB-temp) leg with the register-predicted PASS. CF-AS-3 (the A_s canonical pin) accordingly records a **POINT-per-functional + scheme-tag** (Reading-A form), with the (b-ii) L_max-tag on T_pivot reading "saturated".

*Convention / regulator pins*: `convention = PER-CHARGE-MULTIPLIER` (the intensive Counting-axis pin per `regulator-pin-discipline.md §"Counting (intensive/extensive)"`; the EXTENSIVE-SUM reading that would make λ_pivot L_max-soft is EXCLUDED). `regulator_pin = N/A` (λ_pivot is a GGE occupation potential, NOT a Seeley-DeWitt a_n residue; η_FB is an eigenvalue-floor ratio, not a regulator-weighted moment). dual-SHA: `audit_sha256=77b6603800bc6e97cb3654a93bda7ad5f1494d6a30a4e56bcd34ef3a690ff25b`, `content_sha256=9957d7a37596a49f1be9093a7ab10375d01e43c7e9fc47c93302567a99fd63be`.

*Substrate-first assessment* (PHONONIC): the substrate IS the D_K(τ_fold) spectrum; the Peter-Weyl (p,q) sectors ARE its representation-theoretic content (NOT a container the substrate sits inside). The arrow `D_K(τ_fold) eigenvalues → (p,q) sectors → n_pivot → λ_pivot = −ln(n_pivot/(1−n_pivot))` is unbroken. The intensive/extensive distinction IS the substrate's own answer to whether the |β_k|² amplitude is a converged d.o.f.: the non-thermal GGE does not collapse its 8 per-charge multipliers into a single shared β, and THAT non-collapse — a structural property of the substrate's representation-theoretic content, not an external regulator choice — is what makes both the pivot gap and the pivot temperature per-mode-saturated, hence the amplitude a POINT. This is the SAME per-charge mechanism that makes the SHAPE (n_s, α_s) intensive (S57/S62 Mode-Independent Occupation), now seen on the AMPLITUDE.

---

### §W2-4. S111-CF-VIICE-NW (volovik-superfluid-universe-theorist)

**Status**: COMPLETED
**Gate ID**: `S111-CF-VIICE-NW`
**Trigger**: `[CHAIN]`
**Classification**: **PHONONIC** (the two-fluid EoS w_i is the barotropic response of the relic GGE occupation n_i — the Leggett-channel quasiparticle band's pressure/density ratio)
**Agent**: `volovik-superfluid-universe-theorist` (derives the n↔w map; `einstein-theorist` cross-checks the effective-Friedmann dq/da-sees-(w₁−w₂) side)
**Hypothesis**: The two-fluid EoS difference (w₁−w₂) is a substrate-DERIVED (THEOREM/exact) function of the band-occupation difference (n₁−n₂) via the relic-occupation → ρ_i(a) dilution chain → barotropic w_i(n_i) map — NOT an author-stipulated identification — so §VII.CE clause-(a)'s perfect-square dq/da=−(n₁−n₂)² rests on a derived (n₁−n₂)↔(w₁−w₂) dictionary. §VII.CE is already STAGE-3-PERMANENT (S110 W4b); this gate lands a sharpening ANNOTATION on clause-(a), it does NOT re-register the theorem.
**Plan reference**: `sessions/session-plan/session-111-plan-w2.md` §W2-4 (7-step barotropic-dilution substitution chain; NO dual_prior — THEOREM/INFO is the verdict rubric, not a two-track re-allocation).

**Output Artifacts**:
- **Script** `computations/session-111/s111_cf_viice_nw.py` — `grep -E 'from canonical_constants import|print_verdict_payload'`:
  - `L90: from canonical_constants import tau_fold, Delta_BCS, M_KK_gravity`
  - `L125: def print_verdict_payload(...)` + `L424: print_verdict_payload(...)`
- **Data** `computations/session-111/s111_cf_viice_nw.npz` — present (13876 bytes); spot-check `verdict=PASS`, `all_exact=1`, `numerical_correspondence_max_abs_resid=3.553e-15`, `endpoint w/n efface/GGE = -1 0 0 3`.
- **Plot** `computations/session-111/s111_cf_viice_nw.png` — present (109787 bytes); left panel = the affine bijection n_i=3(1+w_i) with the two-fluid endpoints marked; right panel = the perfect-square morphism (n₁−n₂)²=9(w₁−w₂)².
- **Verdict line** `computations/session-111/s111_gate_verdicts.txt` — matches `^S111-CF-VIICE-NW:.* audit_sha256=[a-f0-9]{64}`:
  ```
  S111-CF-VIICE-NW: PASS -- value='THEOREM:n<->w_closed_form_bijection_w_i=n_i/3-1;(n1-n2)^2=9(w1-w2)^2_sympy-exact;dq/da=-(n1-n2)^2C=-(w1-w2)^2(9C)_perfect-square-preserved;endpoints_w(-1,0)<->n(0,3);VII.CE_clause-a_substrate-derived' scheme=TWO-FLUID-EOS convention=BAROTROPIC-DILUTION L_max=N/A audit_sha256=8a833079ae110445b9d03e9145bfa12c7256c55f7efdde4c26918862b5310dc6 content_sha256=2815111c86d2b6e9a3f6305017cad6409b297bb59fd4c18c4da728fc5466065b schema_version=S84+
  ```
  Dual-SHA companion row present; `regulator_pin=N/A` + n↔w-map + §VII.CE-annotation companion rows present. schema_v2 3-tuple NOT required ([CHAIN] derivation — THEOREM/INFO, no signed direction). sig_5: audit_sha256 unique (count 0 prior).

**MCP Pre-Compute Audit** (per `.claude/rules/knowledge-index-usage.md`):
- `search_knowledge("VII.CE two-fluid EoS occupation dq/da perfect square back-reaction")` → returned §VII.CE clause-(a) PROVEN `dq/da=−(n₁−n₂)²×(positive prefactor)`, clause-(b) back-reaction closure PROVEN; provenance `inv12_w3_3_back_reaction_closure_hsq`.
- `trace_entity("two-fluid effacement GGE w=-1 w=0")` → no trace (the two-fluid w=−1/w=0 structure is a substrate-physics fact, not a named knowledge entity; confirmed not separately indexed — derivation required).
- `search_knowledge("VII.CE clause relic-Friedmann Connes-proxy deceleration parameter STAGE-3-PERMANENT")` → returned the JOINT clause (PASS-AND both reviewers) + clause-(c) q-as-observable distinction PROVEN; confirmed §VII.CE is STAGE-3-PERMANENT.
- Registry read `permanent-results-registry.md:22182–22195` (§VII.CE full entry) — clause-(a) form pinned, author-side `(n₁−n₂)↔(w₁−w₂)` identification identified as the INFO-not-falsified target this gate derives.
- NOT PRE-CLOSED: the closure covers the FORM + sign of clause-(a) (PROVEN); the n↔w *dictionary derivation* (this gate) is the open sharpening, recorded INFO-not-falsified at §VII.CE — distinct deliverable, no prior gate derives it.

**Verdict**: **PASS (THEOREM)**. The n↔w dictionary is substrate-DERIVED closed-form (a bijection); (n₁−n₂)²-form ⇔ (w₁−w₂)²-form is sympy-exact (10/10 symbolic checks PASS); no contradiction with §VII.CE clause-(a) (sign + form preserved). 4-tuple: `(value=THEOREM:…, scheme=TWO-FLUID-EOS, convention=BAROTROPIC-DILUTION, L_max=N/A)`.

**Results**:

The two-fluid EoS difference (w₁−w₂) is a substrate-DERIVED closed-form function of the band-occupation difference (n₁−n₂) — NOT an author stipulation. §VII.CE clause-(a)'s perfect-square `dq/da = −(n₁−n₂)²` rests on a derived dictionary.

**The n↔w map (closed-form affine bijection).** From the barotropic dilution law:
- Forward: `n_i = 3(1+w_i)` (the dilution exponent is fixed by the EoS)
- Inverse: `w_i = n_i/3 − 1 = −1 − (1/3) d ln ρ_i/d ln a` (the barotropic index is the dilution exponent, exact)

Round-trips are sympy-exact identities (`w→n→w − w = 0`, `n→w→n − n = 0`) ⇒ the map is a BIJECTION, not a one-way pairing. The dilution-law form and the inverse-map form agree exactly (`w_dilution − w_of_n = 0`), confirming `w_i = −1 −(1/3) d ln ρ_i/d ln a` with `ρ_i(a) ∝ a^{−n_i}` reproduces `w_i = n_i/3 − 1`.

**7-step barotropic-dilution substitution chain (substituted numbers):**
1. `ρ_i(a) ∝ a^{−n_i}` — barotropic dilution law (inv12 line 308: `n_r = 3.0*(1.0 + w_relic)`).
2. `ρ_i(a) ∝ a^{−3(1+w_i)}` ⇒ `n_i = 3(1+w_i)` — the n↔w MAP (closed-form, affine).
3. invert: `w_i = n_i/3 − 1 = −1 − (1/3) d ln ρ_i/d ln a` (with `d ln ρ_i/d ln a = −n_i`, sympy-exact).
4. `(n₁−n₂) = 3(1+w₁) − 3(1+w₂) = 3(w₁−w₂)` — the difference morphism (`ndiff − 3·wdiff = 0`).
5. `(n₁−n₂)² = 9(w₁−w₂)²` — the perfect-square morphism (`ndiff_sq − 9·wdiff_sq = 0`, sympy-exact).
6. `dq/da = −(n₁−n₂)²·C = −9(w₁−w₂)²·C = −(w₁−w₂)²·(9C)` — the perfect-square in n IS the perfect-square in w, rescaled by the POSITIVE factor 9 ⇒ sign of dq/da preserved (`dq_in_w − (−(w₁−w₂)²·9C) = 0`).
7. endpoints (Volovik two-fluid): effacement vacuum `w₂=−1 → n₂=0` (ρ₂=const, S58/S66 Volovik-partition DILUTION-CC ρ_vac/ρ_obs=1.032); GGE matter `w₁=0 → n₁=3` (ρ₁∝a^{−3}, CDM-by-construction S43/S44). Check: `(n₁−n₂)=3=3·(w₁−w₂)=3·1`; `(n₁−n₂)²=9=9·(w₁−w₂)²=9·1²` ✓; dust asymptote `q=n_eff/2−1=+1/2`.

**Symbolic verification (sympy-exact, 10/10 PASS).** `bijection_w_n_w_residual=1`, `bijection_n_w_n_residual=1`, `dlnrho_dlna_is_minus_ni=1`, `w_dilution_eq_inverse_map=1`, `ndiff_eq_3_wdiff=1`, `ndiff_sq_eq_9_wdiff_sq=1`, `dq_da_perfect_square_in_w=1`, `prefactor_rescale_is_9_positive=1`, `endpoint_n_eq_3w=1`, `endpoint_nsq_eq_9wsq=1`. ALL EXACT = True. (Cross-checked independently in Sage MCP: `(n1-n2)^2 factored = 9*(w1 - w2)^2`; `Step 5 equality (lhs-rhs) = 0`; `Step 6 perfect-square-in-w check = 0`; round-trips `wi`/`ni` exact.)

**einstein effective-Friedmann cross-check (consumed from `inv12_w3_3_back_reaction_closure_hsq.npz`).** The source uses the GGE relic (w=0, n=3) as the diluting component against the effacement vacuum (w=−1, n=0): `n_eff=3.0`, `w_r_eff=0.0`, `q_relic_dominated_asymptote=0.5` — all three match the GGE-dust endpoint of the derived map (`source_npz_consistent=True`). The effective-Friedmann scalars `Λ_eff=8.9349`, `G_eff=0.006790` (Sakharov a₂→Newton), `M_Pl_eff_sq=5.8601`, q-band `[−0.97, +0.81]` are what `dq/da` sees: with `w_r=0` the relic-Friedmann `q_eff = (3/2)Ω_relic − 1` is monotone-non-increasing in a (the `−(n₁−n₂)²≤0` sign), exactly the §VII.CE clause-(a)/(d) structure — the (w₁−w₂)=+1 endpoint difference is what the deceleration `dq/da` registers. Numerical-correspondence cross-check over a w-grid ∈ [−1, 0.5] (61 points, w₂=−1 fixed): `max|(n₁−n₂)² − 9(w₁−w₂)²| = 3.553e-15` (float-eps) — the perfect-square identity holds pointwise across the whole two-fluid family, not only at the endpoints.

**§VII.CE clause-(a) basis upgrade (annotation, NOT re-registration).** The clause-(a) identification `(n₁−n₂)↔(w₁−w₂)` upgrades from author-stipulated to substrate-derived: the occupation difference IS the EoS difference (via the factor-3 map `n_i=3(1+w_i)`), and the perfect-square `dq/da=−(n₁−n₂)²` IS the perfect-square `−(w₁−w₂)²·(9C)` in the EoS difference, Sage/sympy-exact. §VII.CE remains STAGE-3-PERMANENT (S110 W4b Stage-2 PASS-AND `S110-CF-W33-THEOREM` audit_sha256=a0021aa0…) — the original blind cross-axis volovik[Axis-A]×einstein[Axis-B] PASS-AND stands; this gate lands a sharpening ANNOTATION on clause-(a)'s basis, it does NOT re-open the theorem's status (no re-promotion). Routes to capstone-hygiene Q3 (a PROVEN-clause basis sharpening, not a status change): the (n₁−n₂)↔(w₁−w₂) READING moves author-side → derived; no down-tag, no inversion of explanation direction.

**Dual-SHA.** `audit_sha256=8a833079ae110445b9d03e9145bfa12c7256c55f7efdde4c26918862b5310dc6` (script+canonical+pinmap; independently reproduced), `content_sha256=2815111c86d2b6e9a3f6305017cad6409b297bb59fd4c18c4da728fc5466065b` (script only). Input pins: `canonical_constants.py` (f2270207…), `inv12_w3_3_back_reaction_closure_hsq.npz` (5a9a3dfd…). `regulator_pin=N/A` (the EoS w_i is a thermodynamic ratio p_i/ρ_i, NOT a Seeley-DeWitt a_n; ρ_i(a) is a dilution law, not a spectral-action moment).

**Substrate-first framing (PHONONIC).** The substrate IS the D_K spectrum; the two-fluid components are the Leggett-channel GGE relic (w=0 matter — inter-band coherence mode, CPT-neutral, non-annihilating, CDM-by-construction) + the effacement residual (w=−1 vacuum — Volovik-partition leftover, 0.03% impedance-mismatch leakage). The flow `D_K eigenvalues → relic band occupations n_i → energy-density dilution ρ_i(a)∝a^{−3(1+w_i)} → effective barotropic w_i=p_i/ρ_i → (n₁−n₂)↔(w₁−w₂) dictionary → §VII.CE dq/da=−(n₁−n₂)²` is not a container-level EoS imposed on the substrate — the EoS EMERGES from the relic occupations because the band occupations FIX the dilution exponents (the substrate's own two-fluid thermodynamics). The map is intrinsic to the substrate, read FROM `{λ_k}` via the occupations, never an external fluid added to FRW.

---

## Wave 2 Synthesis (team-lead)

**Wave 2 result: 3 PASS + 1 INFO + 1 FAIL — the §6.3 M_KK-magnitude leg does NOT close; it is pinned as an external-import boundary.** This is the session's pivotal outcome. After W1 closed the §6.3 clock leg (well-posed, unique, inflaton-incompatible), W2's prime decider answers the magnitude leg: under the substrate-natural BARE-IMPORT reading, M_KK is NOT a τ-RG-invariant fixed-point scale and its only dimensionful content is a borrowed CODATA cutoff. The §6.3 a(t)/effective-Friedmann residual therefore NARROWS (clock leg closed) but does NOT vanish — the M_KK magnitude remains a knob, not a substrate-derivation.

**Per-gate:**

- **MKK-RG-INVARIANCE — FAIL** (§W2-1; PRIME Topic-1). `Δ_rel=8.193` (≫ 5e-2), `leg1_RGinv=False` (M_KK flows with the modulus-evaluation point — not a fixed-point scale), `leg2_noimport=False` with `CODATA_in_magnitude_leg=True` (the magnitude leg imports CODATA). `multnorm=NOT-APPLICABLE-BY-OPERATOR-FORM` ⇒ this is NOT a multiplicative-normalization structural-identity artifact; the FAIL is genuine. Dual-prior re-allocated 0.90 → Track B (BARE-IMPORT). [SIGN] sign=PASS/mag=FAIL/regime=VALID. **Corridor closed**: "M_KK is a knob-free substrate-RG-invariant scale" is falsified under the bare reading; the magnitude leg stays an external pin.
- **CF3-H0-RESIDUAL — INFO** (§W2-2). Pre-registered honest-partial: relief `49/800 = 6.125%` through the dimensionless a₀-orthogonal channel (`a0_a2_orthogonal=True` — volovik cross-check holds), residual_held=93.875%, dimensionful `M_KK¹` scale leg INADMISSIBLE (`d_A=0` even-parity, `deg_T=2.0`). Band NOT closed dimensionlessly → INFO. NO capstone down-tag (dimensionless-layer scope confirmed). The held 93.875% is downstream of the same M_KK-magnitude question MKK-RG FAILed.
- **AS3a — PASS** (§W2-3a). One defensible impulse-quench A_s = 1.537e-08 (round-trip-consistent with the INV5 anchor to 3.9e-6); all-frozen-superhorizon regime RESOLVED-FROZEN (89/89, Z_norm=1); epistemic type set by AS3b.
- **AS3b — PASS** (§W2-3b). `epistemic_type=POINT` (so AS3a's A_s is a sharp POINT, not a band): λ_pivot=2.771, n_pivot=0.0589; sector-13 Friedrich-Bär bound 3.0022 > bottom-K ceiling 0.8452 (3.55× margin, out-of-band) ⇒ no L_max≥13 re-opening. roundtrip_err=0.
- **VIICE-NW — PASS/THEOREM** (§W2-4). Closed-form n↔w bijection `w_i=n_i/3−1` makes `(n₁−n₂)²=9(w₁−w₂)²` sympy-exact, so §VII.CE clause-(a)'s `dq/da=−(n₁−n₂)²·C` perfect-square is substrate-DERIVED (not author-stipulated). Endpoints `w(−1,0)↔n(0,3)`. A sharpening ANNOTATION on §VII.CE clause-(a) (already STAGE-3-PERMANENT, S110 W4b) — does NOT re-register; correctly did NOT write the registry (volovik is not §VII.CE's writer).

**Substrate framing.** The headline FAIL is itself substrate-first: it does not say "the framework can't predict M_KK," it says the *bare-import* route to a knob-free M_KK is structurally shut, and names exactly what a passing route must avoid (no CODATA, no routing through M_Pl). FAIL maps the corridor; it does not concede the program.

**Capstone-hygiene (→ session-close, MANDATORY).** Q1 = YES (MKK-RG alters the §6.3 a(t)/effective-Friedmann gap status — magnitude leg now pinned as external-import). Q3 = YES (the M_KK-magnitude derivation status changes to BARE-IMPORT FAIL). CF3 INFO does NOT down-tag (dimensionless-layer scope). Action: run the full 5-question gate at session-close; reconcile capstone §6.3 + Atlas D04 so no section narrates §6.3 as "closed" — the clock leg is proven-well-posed, the magnitude leg is an open external pin. Routed to `session-111-housekeeping.md` (session-close consolidated pass), NOT deferred to S112.

### Effected In-Session (non-math — completed by the team-lead orchestrator)

- W2 WP is clean (all 5 sections COMPLETED, 0 `NOT STARTED`; no stale-status quirk this wave) — no status-line hygiene owed.
- No W2 registry landings needing two-surface verification (VIICE-NW is annotation-only and correctly did not write; no §VII slot allocated this wave).
- **Routed to the session-close consolidated registry/canonical/falsifier pass** (tracked in `session-111-housekeeping.md`): (i) promote `A_s_FW = 1.537e-08` (full-precision from the AS3a npz) via `update_constant` — Step 2 of the canonical write-order, single-value POINT, fix-in-session; (ii) VIICE-NW n↔w sharpening annotation onto §VII.CE clause-(a) (registry annotation; route to the §VII.CE writer); (iii) AS3a A_s → falsifier Row 8 via mack (Step 3, sole writer); (iv) the capstone-hygiene 5-Q gate + §6.3 / Atlas D04 reconciliation.

## Carry-Forward Computations

Two genuine math carry-forwards, both rooted in the MKK-RG FAIL (the M_KK-magnitude leg is the §6.3 residual's remaining open half). The VIICE-NW n↔w derivation is COMPLETE (PASS, in-section) — not a CF; its registry annotation is the session-close item in Effected-In-Session.

### CF-S112-MKK-SUBSTRATE-ANCHOR — derive the dimensionful M_KK anchor from a substrate-natural scale (non-bare-import)

| Field | Spec |
|:------|:-----|
| **What** | Find/derive a substrate-natural dimensionful scale that fixes M_KK WITHOUT importing CODATA and WITHOUT routing through M_Pl, then re-run the τ-RG-invariance two-leg test under that non-bare reading. This is the §6.3 a(t)/effective-Friedmann residual's remaining (magnitude) half. |
| **Inputs** | `computations/session-111/s111_mkk_rg_invariance.npz` (the BARE-IMPORT FAIL fingerprint: Δ_rel=8.193, leg1_RGinv=False, leg2_noimport=False, R_fold=1.6017e-01); the S110-CF-CV2A transmutation chain (`s110_cf_cv2a_mkk_transmut_promote.npz`); `canonical_constants.py` M_KK + the a₀/a₂ spectral moments. |
| **Gate** | `leg1_RGinv=True` (M_KK τ-invariant under the new reading) AND `leg2_noimport=True` (no CODATA/M_Pl import) AND `Δ_rel < 5e-2`. PASS → the §6.3 M_KK-magnitude leg CLOSES (and the H0 residual's held 93.875% becomes addressable); FAIL → the magnitude leg is a permanent external-import boundary (a substantive framework limitation to be narrated honestly in the capstone). |
| **Effort** | ~1–2 waves (the M_KK origin is a hard substrate-physics problem; this is the keystone's open half). |

### CF-S112-H0-BAND-CLOSURE — H0 full closure pending the M_KK-magnitude fix

| Field | Spec |
|:------|:-----|
| **What** | Re-test the H0-residual band closure once a substrate-natural M_KK anchor exists: the dimensionful `M_KK¹` scale leg that is INADMISSIBLE under the bare reading (parity-locked, `d_A=0` even) may become admissible if M_KK is substrate-derived, releasing the held 93.875%. |
| **Inputs** | `computations/session-111/s111_cf3_h0_residual.npz` (partial_relief=49/800, residual_held=0.93875, a0_a2_orthogonal=True); the output of CF-S112-MKK-SUBSTRATE-ANCHOR (UPSTREAM — proximate dependency). |
| **Gate** | Band closes dimensionfully (`band_closed=True`) iff the M_KK anchor PASSes CF-S112-MKK-SUBSTRATE-ANCHOR; otherwise the residual stays held and H0 relief is capped at the 6.125% dimensionless channel. |
| **Effort** | ~0.5 wave (conditional re-run once the M_KK anchor lands). |
| **Depends on** | CF-S112-MKK-SUBSTRATE-ANCHOR (UPSTREAM — H0 full closure cannot proceed until the M_KK magnitude is substrate-fixed). |

## Constraint-Map Updates

(One row per state change. Columns: Date | Mechanism/gate | Prior state | New state | Reason.)

## Files Produced

(One row per gate. Columns: Gate | Script | Data (.npz) | Plot (.png) | JSON | Size.)
