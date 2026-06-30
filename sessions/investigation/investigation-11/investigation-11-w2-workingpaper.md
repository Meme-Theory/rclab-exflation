# Investigation 11 Wave 2 — Harvesting the Spectrum-Forced Neutrino Predictions (Results Working Paper)

**Investigation**: 11 | **Wave**: W2 | **Plan**: investigation-11-plan-w2.md | **Track**: investigation (parallel exploratory) | **Theme**: spectrum-forced, zero-free-parameter neutrino-sector predictions (sterile-null + ΔN_eff, three-channel absolute-mass triangle, Majorana transition magnetic moment, M_R provenance audit).

**Verdict-file (investigation-track canonical)**: `computations/investigation-11/inv11_gate_verdicts.txt` — every verdict line emitted via `emit_verdict(session=11, track="investigation", ...)` per `.claude/rules/gate-verdicts.md §"Investigation-Track Canonical Path"`. NEVER a `computations/session-N/` path.

## Gate Sections

### §W2-1. INV11-W2-1-STERILE-NULL-DELTA-NEFF (neutrino-detection-specialist)
**Status**: COMPLETED
**Gate ID**: `INV11-W2-1-STERILE-NULL-DELTA-NEFF`
**Trigger**: `[VERIFY]` (set-membership count + a [SIGN]-flavored ΔN_eff direction; 3-tuple companion row required)
**Classification**: **PARTICLE** (representation-theoretic content of D_K — singlet-tower cardinality + B-branch freeze-out)
**Agent**: `neutrino-detection-specialist`
**Hypothesis**: The D_K singlet tower at τ_fold has EXACTLY three light bottoms (no eV-scale fourth active-mixing state hosting a sterile) AND the right-handed Majorana partners (M_R ~ 10¹⁷ GeV) freeze out far above ν decoupling so ΔN_eff(ν-sector) ~ 0 — two zero-free-parameter spectrum-forced predictions.
**Plan reference**: `sessions/investigation/investigation-11/investigation-11-plan-w2.md` §W2-1 (operator, strict_PASS_boundary, machinery pin, substitution chain, input-SHA pins).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- **script** `computations/investigation-11/inv11_w2_sterile_null_delta_neff.py` — EXISTS (27,377 B). `grep -cE 'from canonical_constants import'` → **3**; `grep -cE 'print_verdict_payload'` → **2**. Both must_contain patterns present.
- **data** `computations/investigation-11/inv11_w2_sterile_null_delta_neff.npz` — EXISTS (9,410 B; non-stub).
- **plot** `computations/investigation-11/inv11_w2_sterile_null_delta_neff.png` — EXISTS (88,163 B; two-panel: sterile-null scale-separation + ΔN_eff residual-vs-physical).
- **verdict_line** in `computations/investigation-11/inv11_gate_verdicts.txt` — present, matches `^INV11-W2-1-STERILE-NULL-DELTA-NEFF:.* audit_sha256=[a-f0-9]{64}`; dual-SHA companion row + schema-v2 [SIGN] 3-tuple row + 2 extra rows all emitted via `emit_verdict(session=11, track="investigation")` (5 rows; cross-process locked; sig_5 unique).
- **wp_section** — this section.

**MCP Pre-Compute Audit** (query-first per `.claude/rules/knowledge-index-usage.md`; queries run BEFORE the script was written):
- `get_constant('M_KK')` → **7.428660036284456e16 GeV** (S42 CONST-FREEZE-42; alias of M_KK_gravity). Imported, not hardcoded.
- `get_constant('N_eff_SM')` → **3.044** (SM N_eff: 3 ν + non-instantaneous decoupling). Imported.
- `search_knowledge('three generations Z3 triality singlet tower neutrino sterile')` → **theorem "Three generations from Z_3 triality" | PROVEN | S03** (src session-28-neutrino-collab.md); the (0,0) sector hosts the BCS/Leggett singlet ladder. → CC1 sterile-null count==3 is PRE-PROVEN structure, not re-derived here.
- `search_knowledge('N_eff freeze-out entropy dilution S56 W0-2 right-handed Majorana')` → `constraint-mega-matrix.md` lists **ΔN_eff among Gates PASSED**; the S56 §W0-2 freeze-out reproduces M_KK / Δ_BCS / H_fold. The S56 channel is the *fabric phonon* sector; THIS gate is the *neutrino B-branch / RH-partner* sector (distinct) re-using only the freeze-out arithmetic template, not re-running S56.
- `search_knowledge('M_R B-branch fold energy leptogenesis seesaw scale')` → **"Leptogenesis (real M_R)" | PROVEN | S60**; `Sigma_mnu_FW` provenance edges confirm `M_R = D_K B-branch fold energies × M_KK`. The s60 log gives M_1 = 1.004396 M_KK = 7.4613e16 GeV.
- Found canonical g_* pins in `canonical_constants.py`: `g_star_SM=106.75`, `g_star_BBN=10.75` — imported for the entropy-dilution ratio (no plan-text-approximation hardcode).
- **Not PRE-CLOSED as a single gate**: the two NULLs are *latent* in PROVEN structure (Z_3 triality + S60 M_R + S56 freeze-out) but had not been packaged as the two named spectrum-forced neutrino-sector predictions — this gate harvests them.

**Verdict**: **INFO**
- 4-tuple: `(value=<count=3; gap_ratio=0.8605; scale_sep_to_eV=25.86dec; M_R_lightest=7.4613e+16GeV; DeltaN_eff_physical=0.000e+00; N_eff_nu_FW=3.0440>, scheme=spectrum-forced-NULL, convention=ABSOLUTE, L_max=12)`
- [SIGN] 3-tuple: `sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID`.
- dual-SHA: `audit_sha256=1651ce1d6b8a8f5c01d9e680f47f20fb118ce14fcf2cc4511bbafdf64186563c`, `content_sha256=7b852869f4ce85decaa6f5eb7f2c6e4575da9b4af61793c9ba5ca47b9b033919`.

The composite is **INFO** (not PASS) because exactly ONE literal sub-criterion fired its INFO clause — the within-singlet **gap-ratio** test `E_first_above/E_third_bottom ≥ 1.05`. This is the plan's pre-registered `INFO_meaning` ("gap structure ambiguous"). It is NOT a FAIL: the count==3 test PASSES, both ΔN_eff conditions PASS, and the *dispositive* sterile-null criterion (the M_KK→eV scale separation) PASSES overwhelmingly. The INFO is reported faithfully (no threshold was moved to chase PASS — `v3-closure-recovery.md` Class-6 avoided).

**Results**:

**(a) STERILE-NULL — singlet (0,0) active-mixing tower** (L12 cache `s84_spectrum_cache_L12_tau019.npz`, sector_evals[(0,0)]):
- Distinct singlet bottoms = **3** (== expected 3): |λ| levels **[0.819741, 0.845212, 0.971408] M_KK** (degenerate multiplicities 2/8/6 = the 16-dim singlet sector). **CC1**: the count==3 is "Three generations from Z_3 triality", PROVEN S03/S28 — a set-cardinality, analytically exact, not a numerical fit.
- Third bottom = 0.971408 M_KK = **7.2163e16 GeV**. Singlet bottom in eV = **7.2163e25 eV**.
- **Scale separation to 1 eV = 25.86 decades** → there is categorically NO eigenstate within ~26 OOM of the eV scale a 3+1 sterile fit demands. This is the dispositive sterile-null: a light active-mixing sterile has no spectral home. The first genuinely-distinct higher state is the next Peter-Weyl tower (sector (0,1), |λ|_min = 0.835894 M_KK ~ 6.2e16 GeV) — at the KK gap, 16+ OOM above eV.
- **Gap-ratio sub-test = 0.8605** (< R_gap_min = 1.05) → the literal within-singlet gap-ratio FAILS its threshold, driving the composite to INFO. **Why**: the criterion assumed the three "bottoms" are the three lowest eigenvalues with a clean gap *above* the third. In fact the singlet sector's third distinct level (0.9714) is the *largest* of its three, and the adjacent (0,1)/(1,0) tower interleaves *below* it (0.8359 < 0.9714) in |λ|. So `E_first_above/E_third_bottom = 0.8359/0.9714 = 0.86 < 1.05`. The pre-registration mis-modeled the interleaved-tower geometry; the *physical* "no eV-scale room" claim is carried by the 25.86-decade scale separation, not by a within-singlet gap. (Recorded as a carry-forward correction below — the gap-ratio operationalization should be replaced by the scale-separation test.)

**(b) ΔN_eff — RH Majorana freeze-out entropy-dilution** (M_R from s60_lepto_cp_log.txt; g_* from canonical_constants):
- B-branch fold energies = [1.004396, 1.078573, 1.170003] M_KK; **M_R(lightest) = 1.004396 M_KK = 7.4613e16 GeV** (the lightest sets the most generous, i.e. lowest, T_fo). **CC2**: S56 §W0-2 entropy-dilution g_* ratio.
- **Residual ceiling** (the value *if* the RH species were still relativistic at decoupling) = (4/11)^{4/3}·(g_BBN/g_SM)^{4/3} = (4/11)^{4/3}·(10.75/106.75)^{4/3} = **0.012160** (Sage-exact: (4/11)^{4/3}=0.259551, (43/427)^{4/3}=0.046851). Note this ceiling is marginally *above* 0.01 — but it is NOT the physical value.
- **Boltzmann suppression**: M_R/T_dec = 7.4613e16/1e-3 = **7.461e19** (the RH partner is non-relativistic at T_dec ~ 1 MeV by **19.87 OOM**). exp(−7.46e19) underflows to **0.0** to any float precision.
- **ΔN_eff(physical) = residual × Boltzmann = 0.012160 × 0 = 0.000e+00** ⇒ **N_eff_nu_FW = N_eff_SM + ΔN_eff = 3.044 + 0 = 3.0440** = N_eff_SM to the dilution floor. |ΔN_eff| = 0 ≤ 0.01 PASS. The RH sector is dark-radiation-inert.

**Substitution chain (with substituted numbers) — the [SIGN] direction claim**:
> Claim: ΔN_eff(ν-sector) is DECREASING in M_R and → 0 because M_R ≫ T_dec.
> - Def 1: ΔN_eff_residual = (4/11)^{4/3}·[g_*(T_dec)/g_*(T_fo)]^{4/3} (standard entropy-dilution, session-56-neutrino-collab.md ρ_rad form).
> - Def 2: T_fo = M_R = (B-branch fold)·M_KK = 1.004396 × 7.428660e16 = **7.4613e16 GeV**.
> - Def 3: T_dec ~ 1 MeV = 1e-3 GeV; g_*(T_dec)=10.75, g_*(T_fo≫T_EW)=106.75; RH partner non-relativistic at T_dec.
> - Substitute: ΔN_eff = 0.259551 × 0.046851 × exp(−M_R/T_dec) = 0.012160 × exp(−7.461e19).
> - Simplify: exp(−7.461e19) = 0 (float underflow; log10 ≈ −3.24e19) ⇒ ΔN_eff = 0.012160 × 0 = **0**.
> - Direction: d/dM_R[exp(−M_R/T_dec)] = −(1/T_dec)·exp(−M_R/T_dec) < 0 ⇒ **decreasing in M_R**. The computed physical value (0) sits far below the residual ceiling (0.01216) — the suppression is confirmed (sign_verdict=PASS).
> - Conclusion: a 10^17-GeV species is not a relativistic dof at 1 MeV; ΔN_eff → 0 EXACTLY, a zero-free-parameter NULL set by the spectrum's own M_R scale.

**Substrate framing** (PARTICLE; direction substrate → emergent): the substrate IS the Peter-Weyl decomposition D_K = ⊕_{(p,q)} D_{(p,q)}. The SINGLET (0,0) tower bottoms ARE the three light active states (S52); their cardinality is fixed by Z_3 triality (PROVEN), so a light sterile that MIXES with the active triplet has no spectral home — every eigenstate lives at O(1) M_KK ~ 10^16 GeV, 25.86 decades above the eV scale a 3+1 fit requires. The right-handed partners ARE the B-branch fold eigenvalues × M_KK (~10^17 GeV); their dark-radiation budget is read off the *same* spectrum via the S56 freeze-out arithmetic and entropy-diluted to ~0. Direction: D_K eigenvalues (singlet tower count + B-branch fold scale) → freeze-out entropy ratio → ΔN_eff → the measured N_eff. Both predictions are the SPECTRUM speaking; neither touches the oscillation-anchored m_D normalization (A-N1) — they are STRUCTURAL and offset the mass-magnitude weakness in the falsifiability ledger. NOT a re-run of the S56 fabric-phonon N_eff (distinct sector: ν B-branch vs fabric phonon); only the freeze-out arithmetic template is shared.

**Assessment / solution-space**: both zero-free-parameter NULLs hold on their *physical* content — exactly three light active states (no eV 3+1 room, 25.86-decade scale separation) and a dark-radiation-inert RH sector (ΔN_eff = 0, N_eff_nu = 3.044 = SM). The INFO (not PASS) is attributable solely to a mis-operationalized literal sub-test (the within-singlet gap-ratio assumed non-interleaved towers); it does NOT close the "spectrum forbids a sterile" corridor — that corridor is OPEN and the spectrum supports it via the scale separation. Forward fix: replace the gap-ratio sub-criterion with the M_KK→eV scale-separation test (≥ 15 decades) in any HY-class promotion.

---

### §W2-2. INV11-W2-2-ABS-MASS-TRIANGLE (neutrino-detection-specialist)

**Status**: COMPLETED
**Gate ID**: `INV11-W2-2-ABS-MASS-TRIANGLE`
**Trigger**: `[VERIFY]`
**Classification**: **PARTICLE** (seesaw-image light triple → three detector-class contractions)
**Agent**: `neutrino-detection-specialist`
**Hypothesis**: The oscillation-anchored light triple m_ν=[0, 0.008678, 0.049528] eV (S99-W3, normal ordering) is mutually consistent across all three absolute-mass detector classes — m_β (kinematic), Σm_ν (cosmological, DESI Row #77), m_ββ (0νββ, LEGEND Row #80) — and yields the publishable kinematic non-detection m_β ~ 0.009 eV.
**Plan reference**: `sessions/investigation/investigation-11/investigation-11-plan-w2.md` §W2-2 (operator, strict_PASS_boundary, machinery pin, substitution chain, input-SHA pins).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- **script** `computations/investigation-11/inv11_w2_abs_mass_triangle.py` — EXISTS (30,261 B). `grep -E 'from canonical_constants import'` → line 87 `from canonical_constants import *  # noqa: F401,F403,E402`; `grep -E 'print_verdict_payload'` → line 436 `def print_verdict_payload(...)`. Both must_contain patterns PRESENT.
- **data** `computations/investigation-11/inv11_w2_abs_mass_triangle.npz` — EXISTS (12,325 B).
- **plot** `computations/investigation-11/inv11_w2_abs_mass_triangle.png` — EXISTS (82,132 B).
- **verdict line** in `computations/investigation-11/inv11_gate_verdicts.txt` — matches `^INV11-W2-2-ABS-MASS-TRIANGLE:.* audit_sha256=[a-f0-9]{64}` (line 32); `audit_sha256=5f4aa7b143950b17d56c574a909c3e17cff86a672c95f9988aab8dd4ed713069` `content_sha256=6fdd21c719f8d2f8af8ce432697f1cc9947adde47977e0b12087c791440007c6`; dual-SHA companion row present (line 33). Emitted via `emit_verdict(session=11, track="investigation")`. (`schema_v2_3tuple_required: false` per plan §W2-2 — `[VERIFY]`, no `[SIGN]` 3-tuple.)
- **wp_section** — this section (Status COMPLETED, Verdict, Output Artifacts, MCP Pre-Compute Audit all present).

**MCP Pre-Compute Audit** (query-first, before any compute, per `knowledge-index-usage.md`):
- `search_knowledge('absolute neutrino mass m_beta ... m_betabeta ... seesaw')` → returned `S99-W3-SEESAW-SUMMNU` PASS (the canonical anchor), `Sigma_mnu_bound_DESI_2024=0.072`, and the falsifier-rigor-registry mass-ordering row. NOT pre-closed for the triangle itself (no prior gate ties the three channels together).
- `search_knowledge('S99 W3 seesaw ... m_nu eigenvalues normal ordering')` → confirmed m_nu=[0, 0.0086776, 0.0495278] eV, NO, `crosscheck_reldiff=1.16e-05`, `MR_coincidence_maxrel=0.0177`, `delta_CP=[0,π]`.
- `get_constant('Sigma_mnu_FW')` → **0.0582053272** eV (S99, s99_w3_seesaw_summnu.npz). The Σ consistency anchor.
- `get_constant('Sigma_mnu_bound_DESI_2024')` → **0.072** eV (DESI 2024 arXiv:2404.03002, 95% CL). The cosmological bound (Row #77).
- `get_constant('m_bb_FW')` → **0.0036950127968154492** eV = 3.695 meV (S100a, Row #80 central; δ_CP=0≡π degenerate, no-cancellation upper funnel edge). The m_ββ anchor.
- `list_constants('sin2_theta...')` → `sin2_theta12_PDG=0.307`, `sin2_theta13_PDG=0.0220` (the pair Row #80 / m_bb_FW CONSUMED) **vs** `sin2_theta12_NuFit60=0.303`, `sin2_theta13_NuFit60=0.02225` (TRUE NuFit-6.0). **Version-disambiguation finding** (canonical provenance lines 699–702, S101 PAIR-OF-PAIRS): the plan §W2-2 "NuFit-6.0" label is de-facto NuFit-5.x/PDG central. → PDG pair PRIMARY (reproduces the canonical Row #80 band bit-consistently); NuFit-6.0 pair DIAGNOSTIC.
- `Read` falsifier-master-inventory.md Row #80 → band `[1.516, 3.695] meV` = analytic `[|t₂−t₃|, t₂+t₃]`; central IS the no-cancellation upper edge; `publication_precision=4`.
- npz load `s99_w3_seesaw_summnu.npz` → exact triple `m_nu_eV=[0, 0.00867756, 0.04952777]`, `Sigma_mnu_eV=0.0582053272`, `delta_CP_allowed=[0, π]`.

**Verdict**: **INFO** — pre-registered marginal-edge outcome (plan §W2-2 INFO_meaning: "m_betabeta only marginally inside the Row #80 band — the Majorana-phase sign ambiguity straddles an edge"). All three channels are mutually consistent from ONE triple; the m_ββ **central** lands exactly ON the Row #80 upper funnel edge (it IS that edge by construction), so the band-membership is marginal, not interior. This is a STRUCTURED pre-registered result, not a failure: the triangle closes (all three detector observables reproduce from the single oscillation-anchored triple), and m_β ~ 0.009 eV is the clean kinematic non-detection forward prediction. (A first run produced a literal-`≤` FAIL on the rounded upper edge by +3.5e-6 relative — a Class-8.3 publication-precision-floor artifact corrected in-script per `epistemic-discipline.md §"Publication-Precision Pre-Registration (Class 8.3)"` item 2: the band edges are published at 4 sf, so the membership test carries `rel_tol ≥ 1e-4`. This is an operator-precision fix, NOT a threshold change to reach a verdict — the central equals the canonical edge to reldiff 0.0.)

**Results** (NUMBERS first):

*One input set (canonical S99-W3 light triple, normal ordering):* m_ν = [0, 0.00867756, 0.04952777] eV; m₁=0 EXACT (MAP-B Casimir grading C₂(0,0)=0, S100a); δ_CP ∈ {0, π} J-forced ([J,D_K]=0, T11). The three detector observables are three DISTINCT contractions of this triple with the laboratory-IN PMNS electron row.

| Channel | Observable | Value | Detector horizon | Status |
|:--------|:-----------|:------|:-----------------|:-------|
| (i) cosmological | Σm_ν = m₁+m₂+m₃ | **0.0582053272 eV** | DESI Row #77 bound 0.072 eV | reldiff vs Σ_mnu_FW = **8.3e-10** (≤1e-6 ✓); **19.2% below** DESI ✓ |
| (ii) kinematic | m_β = √(Σ\|U_ei\|²m_i²) | **8.751 meV = 0.00875 eV** | KATRIN final ~0.3 eV; Project-8 ~0.04 eV | **NON-DETECTION** at both (×34.3 below KATRIN; ×4.6 below Project-8) ✓ |
| (iii) 0νββ | m_ββ = \|Σ U_ei² m_i\| | band **[1.516, 3.695] meV**, central **3.695013 meV** | LEGEND Row #80; KamLAND-Zen 122 meV; LEGEND-200 75 meV | central reldiff vs m_bb_FW = **0.0e+00**; ×33.0 below KamLAND-Zen; ×20.3 below LEGEND-200; central ON upper funnel edge (marginal) |

*Substitution chain (m_β, PDG primary — reproduces the consumed Row #80 PMNS row), substituted numbers:*
- |U_e1|² = c₁₂²c₁₃² = 0.677754; |U_e2|² = s₁₂²c₁₃² = 0.300246; |U_e3|² = s₁₃² = 0.0220 (sin²θ₁₂=0.307, sin²θ₁₃=0.0220).
- m_β² = (0.677754)(0)² + (0.300246)(0.00867756)² + (0.0220)(0.04952777)² = 0 + 2.2606e-5 + 5.3963e-5 = 7.6568e-5 eV²
- m_β = √(7.6568e-5) = **8.751e-3 eV** (Sage-exact 8.75069 meV). Both endpoint terms comparable despite small s₁₃² (because m₃ ≫ m₂): the s₁₃²m₃² term (5.40e-5) slightly exceeds the s₁₂²c₁₃²m₂² term (2.26e-5).
- Direction: m_β ≈ 0.00875 eV ≪ 0.04 eV (Project-8) ≪ 0.3 eV (KATRIN) ⇒ m_β − reach < 0 for BOTH ⇒ NON-DETECTION at both.

*m_ββ band (the J-forced δ_CP∈{0,π} Majorana-phase sign sweep):* with t_i = |U_ei|²m_i and t₁=0 (m₁=0), the resultant magnitude |t₂ ± t₃| ranges over [|t₂−t₃|, t₂+t₃] = **[1.51579, 3.69501] meV** (PDG). Upper edge (constructive, δ_CP=0) = central = 3.695013 meV, matching canonical `m_bb_FW=3.6950128 meV` to **reldiff 0.0**; PDG band edges reproduce the Row #80 [1.516, 3.695] published edges to reldiff (lo 1.38e-4, hi 3.46e-6). The lower edge 1.516 meV is **finite and well above zero** — the m₁=0 (rank-deficient lightest) structure forbids the deep cancellation null a non-zero-lightest model would permit, so a non-vanishing 0νββ is itself a substrate prediction in this (NO, m₁=0, Majorana) configuration.

*Canonical anchors:* CC1 Σ_mnu_FW = 0.0582053272 eV (S99, the consistency anchor); CC2 m_bb_FW = 0.0036950127968 eV (S100a, the m_ββ anchor); CC3 the S99-W3 npz crosscheck_reldiff = 1.16e-5 (the seesaw round-trip, a by-construction self-consistency — see §W2-4 provenance audit).

*PMNS-convention diagnostic (the version-disambiguation cross-check):* TRUE NuFit-6.0 pair (0.303, 0.02225) → m_β = 8.769 meV; m_ββ band [1.46881, 3.67279] meV, central 3.67279 meV. PDG → NuFit-6.0 m_ββ central shift = **−0.601%**, DECISION-IRRELEVANT (sub-percent; both land inside the NO funnel [1.5, 4.5] meV). Matches Row #80's recorded diagnostic (−0.60%).

*4-tuple:* `(value='Sigma=0.0582053eV(<0.072_DESI,reldiff8.3e-10);m_beta=8.751meV(KATRIN/P8_NONDETECT);m_bb=[1.516,3.695]meV_central3.695(Row80_band,reldiff0.0e+00);PDG_primary;NuFit6.0_shift-0.60pct;delta_CP[0,pi]', scheme=seesaw-anchored-triple, convention=ABSOLUTE, L_max=N/A)`.

*Dual-SHA:* `audit_sha256=5f4aa7b143950b17d56c574a909c3e17cff86a672c95f9988aab8dd4ed713069`, `content_sha256=6fdd21c719f8d2f8af8ce432697f1cc9947adde47977e0b12087c791440007c6`.

**Substrate framing (PARTICLE).** The substrate IS the m-triple — the seesaw image of the singlet-tower bottoms (S52/S60/S99): D_K B-branch fold energies → M_R (M₃(ℂ) KO-dim-6 Pfaffian) → type-I seesaw m_ν = −m_Dᵀ M_R⁻¹ m_D → the light triple. The three absolute-mass observables are three DIFFERENT contractions of that ONE substrate object with the (measured) PMNS electron row: Σm_ν the bare L1 sum (cosmological free-streaming, measured IN the DESI BAO container), m_β the incoherent |U_ei|²-weighted RMS (the β-decay endpoint, measured IN the KATRIN/Project-8 spectrometer), m_ββ the coherent U_ei² sum with the J-forced δ_CP∈{0,π} Majorana sign (the 0νββ half-life, measured IN the ⁷⁶Ge/¹³⁶Xe isotope). Direction: D_K B-branch + singlet tower → seesaw m-triple → PMNS contractions → {Σm_ν, m_β, m_ββ} → measured at DESI / KATRIN / LEGEND. The gate tests whether ONE substrate triple lands inside all three detector windows simultaneously — it does, with m_ββ's central ON its own funnel edge. The triple is NOT a free fit: m₁=0 EXACT (Casimir C₂(0,0)=0), m₂/m₃ fixed by the oscillation-anchored Δm² spacing; the absolute-scale (Dirac normalization) is the irreducibly-external oscillation-anchor caveat (`S100a-MD-NORMALIZATION` INFO, track_B 0.9, PERMANENT) — so m_β ~ 0.009 eV is a forward prediction CONDITIONAL on the measured Δm² plus the substrate-structural inputs (NO ordering, m₁=0 exact, Majorana texture, δ_CP∈{0,π}), the same conditional status Row #80 carries for m_ββ. The substrate-FIRST content is the internal coherence — that the single anchoring choice reproduces every direct-mass observable — and the kinematic non-detection number.

**Assessment.** The absolute-mass triangle closes. The same oscillation-anchored light triple that S99-W3 fixed from the seesaw lands self-consistently in all three direct-mass detector windows: Σm_ν 19% below the DESI bound, m_ββ reproducing the canonical Row #80 central to machine-zero (its central sitting ON the no-cancellation upper funnel edge — the marginal-edge INFO), and m_β ~ 0.009 eV a clean kinematic non-detection ×4.6 below the most ambitious near-term reach (Project-8). This INFO is the *honest* verdict: the anchoring is internally coherent across detector classes (not a FAIL — nothing falls out of band), but the m_ββ central is not strictly *interior* to its band, it IS the band's upper edge by construction. The empirical read: this configuration is **invisible** to the current generation of absolute-mass experiments — m_β below KATRIN/Project-8, m_ββ below the LEGEND-200/next-gen 10 meV floor (Row #80's one-sided clause: only a beyond-next-gen ~meV-class 0νββ instrument can probe the band from below; a detection above 4.5 meV would FALSIFY the (NO, m₁=0, Majorana, δ_CP∈{0,π}) configuration). The framework's strength here is NOT a magnitude prediction (the absolute scale is oscillation-anchored, A-N1) but the *structural cross-channel coherence* + the falsifiable non-detection horizons. The PMNS version-disambiguation (PDG primary vs NuFit-6.0 diagnostic, −0.60% decision-irrelevant) was handled per substrate-first-canonical-sourcing.md §(iv) — the canonical Row #80 anchor (PDG-consumed) takes precedence over the plan's mislabeled "NuFit-6.0" prose.

---

### §W2-3. INV11-W2-3-MAJORANA-TRANSITION-MU (neutrino-detection-specialist)

**Status**: COMPLETED
**Gate ID**: `INV11-W2-3-MAJORANA-TRANSITION-MU`
**Trigger**: `[VERIFY]` (diagonal μ=0 EXACT structural identity; the μ_23/μ_13 ratio is the extracted prediction)
**Classification**: **PARTICLE** (electromagnetic-vertex texture of D_K's Majorana sector)
**Agent**: `neutrino-detection-specialist`
**Hypothesis**: For Majorana neutrinos the magnetic-moment matrix is antisymmetric (KO-dim-6 Pfaffian / J-self-conjugacy), so diagonal μ_ii = 0 EXACTLY and only transition μ_ij survive; the texture-fixed ratio μ_23/μ_13 is determined by the M₃(ℂ) off-diagonal structure, independent of the overall m_D scale.
**Plan reference**: `sessions/investigation/investigation-11/investigation-11-plan-w2.md` §W2-3 (operator, strict_PASS_boundary, machinery pin, substitution chain, input-SHA pins).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

All four artifacts verified on disk by content (regex match, not line/byte count):

- **script** `computations/investigation-11/inv11_w2_majorana_transition_mu.py` (22191 bytes) — `grep -E "from canonical_constants import|print_verdict_payload"` returns:
  - `from canonical_constants import *  # noqa: F401,F403,E402`
  - `from canonical_constants import M_KK_gravity  # noqa: E402  explicit: magneton scale`
  - `def print_verdict_payload(...)` + `print_verdict_payload(verdict, value_str, audit_sha, content_sha, ...)`
- **data** `computations/investigation-11/inv11_w2_majorana_transition_mu.npz` (3932 bytes) — present (carries `mu_unit`, `mu_23_over_13`, `mu_12_over_13`, `diag_max`, `antisym_residual`, `V_B3`, etc.).
- **plot** `computations/investigation-11/inv11_w2_majorana_transition_mu.png` (93566 bytes) — present (antisymmetric moment-matrix heatmap + texture-ratio bar chart).
- **verdict line** in `computations/investigation-11/inv11_gate_verdicts.txt` — matches `^INV11-W2-3-MAJORANA-TRANSITION-MU:.* audit_sha256=[a-f0-9]{64}`; `audit_sha256=bcb17a746cd2813f66449a391a25fefe4ecaca8cef24d3f4b419916ddd7d00da` `content_sha256=2654b7d602368836c2545f1b26b251fc9452e08093f24ab2882c80a30afabedc`; dual-SHA companion row + 3 texture/magneton/falsifier extra rows present. Emitted via `emit_verdict(session=11, track="investigation")`.

**MCP Pre-Compute Audit** (query-first; per `.claude/rules/knowledge-index-usage.md`):

| Query | Salient return |
|:------|:---------------|
| `search_knowledge('Majorana magnetic moment transition neutrino antisymmetric')` | **MOMENT-46** (`s46_phonon_magnetic_moment.py`) is the magneton template; no prior neutrino transition-μ gate → NOT pre-closed. |
| `search_knowledge('KO-dim 6 Majorana texture seesaw M_R fold energy B-branch')` | `A_K = ℂ ⊕ ℍ ⊕ M₃(ℂ)` KO-dim-6 Pfaffian on H_K+ (S96-MATTER-0NUBB); Majorana texture lives in the M₃(ℂ) summand; M_R = B-branch D_K fold energies × M_KK. |
| `search_knowledge('M3(C) off-diagonal texture Majorana mass matrix Pfaffian')` | S96-MATTER-0NUBB (`MAJORANA`, KO-dim-6-Pfaffian-on-H_K+); B-30a Pfaffian trivial on Jensen; the flavor texture is the S60 V_B3 block. |
| `trace_entity('Majorana antisymmetry [J,D_K]=0')` | No trace (compound key); resolved via the searches above + the S60 log (the antisymmetry is the textbook Majorana-vertex selection rule anchored to PROVEN [J,D_K]=0). |
| `get_constant('M_KK')` / `get_constant('M_KK_gravity')` | 7.428660036284456e16 GeV (S42, CONST-FREEZE-42, not superseded) — the magneton scale μ_natural = 1/(2 M_KK). |

PRE-CLOSED check: **NOT pre-closed** — no prior gate computes the neutrino transition-magnetic-moment matrix or its texture-fixed ratios. The diagonal-μ=0 identity is the textbook Majorana selection rule (Schechter-Valle 1981 / Nieves 1982), here anchored to the framework's PROVEN [J,D_K]=0 (KO-dim=6, S7-S8/S43); the ratio μ_23/μ_13 is a new texture extraction from the S60 V_B3 block.

**Verdict**: **PASS** — `value='mu_diag=0_EXACT(max|mu_ii|=0.0e+00); mu_23/mu_13=0.997922; mu_12/mu_13=0.099399 (texture-fixed, scale-free)'`. 4-tuple: `(value=0.9979224588495583, scheme=Majorana-antisymmetric-moment, convention=RATIO-mu23_mu13-magneton-1over2MKK, L_max=12)`. Diagonal vanishes to machine-exact zero AND the transition ratio is finite/determined — both PASS clauses met.

**Results**:

**Step 1 — diagonal μ_ii = 0 EXACT (structural identity).** The Majorana electromagnetic-moment matrix is antisymmetric (μ_ij = −μ_ji). The producing script imposes this from the Majorana-vertex selection rule and verifies the structural zero:
- antisymmetry residual `max|μ + μᵀ| = 0.000e+00` (machine-exact),
- diagonal magnitude `max_i |μ_ii| = 0.000e+00` ≤ threshold `1e-12`.

This is an EXACT structural zero, not a small number. **Substitution chain** (the diagonal-vanishing argument, per `math-scripts.md`):

```
Def 1: Majorana mass eigenstate is self-conjugate:  ν_i^c = ν_i   [J-self-conjugacy; [J,D_K]=0, KO-dim=6, T11 — PROVEN S7-S8/S43]
Def 2: moment operator ν̄_i σ_μν ν_j F^μν is ODD under i↔j for self-conjugate fields
       ⇒ μ_ij = −μ_ji  (antisymmetric)                          [Schechter-Valle 1981 / Nieves 1982 selection rule]
Substitute i = j into the antisymmetry relation:  μ_ii = −μ_ii
Simplify:  2 μ_ii = 0  ⇒  μ_ii = 0  for every i
Canonical form: μ(Majorana) is a real antisymmetric 3×3 matrix; diagonal ≡ 0 EXACT;
                the only independent entries are μ_12, μ_13, μ_23 (transition moments).
Direction: antisymmetry forces the diagonal to vanish IDENTICALLY — an exact zero, not a small residual.
```

**Step 2 — transition texture (M₃(ℂ) off-diagonal entries).** The off-diagonal magnitudes inherit the S60 Majorana mass texture V_B3 (the B3-B3 interaction matrix, the M₃(ℂ) summand of `A_K = ℂ ⊕ ℍ ⊕ M₃(ℂ)`), loaded directly from `s60_lepto_cp.npz` (NOT hardcoded; real-symmetric to `1.4e-17`, confirming the S60 Section-5 theorem that [J,D_K]=0 forces V_B3 real symmetric). The off-diagonal entries:
- V_12 = 0.00733458 (1-2 inter-generation coupling — the weak entry),
- V_13 = 0.07378902 (1-3 coupling),
- V_23 = 0.07363572 (2-3 coupling).

Magneton scale `μ_natural = 1/(2 M_KK) = 6.730689e-18 GeV⁻¹` (MOMENT-46, `s46_phonon_magnetic_moment.py` Eq. (3)/(5); M_KK = 7.42866e16 GeV gravity route, canonical). The neutrino per-element weight is the texture entry V_ij, replacing the charged-sector Zak phase γ_n/2π.

**Step 3 — texture-fixed transition RATIOS (zero-free-parameter).** The dimensionless ratios cancel BOTH the overall m_D normalization (oscillation-anchored, A-N1) AND the 1/(2 M_KK) magneton:
- **μ_23/μ_13 = V_23/V_13 = 0.9979** (the headline texture number; near-unity, reflecting the quasi-degenerate B3 texture V_23 ≈ V_13),
- μ_12/μ_13 = V_12/V_13 = 0.09940 (suppressed ~10× — the 1-2 coupling V_12 is the weak texture entry),
- μ_12/μ_23 = V_12/V_23 = 0.09961.

Scale-cancellation residual (physical magneton-applied, m_D-scaled ratio minus bare texture ratio) = `0.000e+00` — the cancellation is EXACT, confirming the ratio is zero-free-parameter. The signs are determined (all V off-diagonals are the same sign — real symmetric, positive), so no INFO-class sign/phase-branch ambiguity arises.

**Substrate framing** (PARTICLE; direction substrate → observable). The substrate IS the antisymmetric moment matrix. The J-self-conjugacy ([J,D_K]=0, KO-dim=6) that makes the neutrino Majorana is the SAME structure that forces the moment matrix antisymmetric — so the diagonal vanishes by IDENTITY, not by tuning. The transition entries inherit the M₃(ℂ) off-diagonal texture (the same V_B3 that fixes the Majorana mass-matrix flavor structure, S60). Direction: `D_K Majorana sector (KO-dim-6 antisymmetry + M₃(ℂ) V_B3 texture) → moment matrix → transition-ratio observable → laboratory electromagnetic-coupling measurement`. The ratio is the zero-free-parameter deliverable; it does NOT inherit the m_D magnitude weakness — it is spectrum/texture-forced. Note the two matrices have OPPOSITE symmetry and are distinct objects: the Majorana MASS texture V_B3 is symmetric (Fermi statistics, S60 line 43), while the magnetic-MOMENT matrix is antisymmetric (the self-conjugacy selection rule); the texture supplies the magnitudes |μ_ij| = V_ij, the selection rule supplies the antisymmetric sign structure.

**Falsification statement.** A DIAGONAL magnetic moment μ_ii ≠ 0 (a non-vanishing diagonal electromagnetic vertex) would FALSIFY the Majorana nature of the neutrino — a Dirac neutrino permits non-zero diagonal moments, a Majorana neutrino forbids them by antisymmetry. This is a SECOND independent Majorana-test channel beyond 0νββ (Row #80): 0νββ tests lepton-number violation; the diagonal-μ=0 selection rule tests self-conjugacy directly. The texture-fixed transition ratio μ_23/μ_13 ≈ 1.00 is the framework's structural prediction for the relative strengths of the surviving (transition) moments, should the overall scale ever become accessible. (Experimental context: the OVERALL transition-moment magnitude is hierarchically suppressed by the m_D/M_KK seesaw — the magneton unit here is 1/(2 M_KK) ≈ 6.7×10⁻¹⁸ GeV⁻¹, ~17 orders below the nuclear magneton — and lies far below any current laboratory or astrophysical neutrino-magnetic-moment bound [the standard limits are O(10⁻¹¹–10⁻¹²) μ_B from stellar-cooling and direct-detection experiments; specific numbers not fetched this session — flagged as domain-knowledge context, not a session-sourced citation per `feedback_research-corpus.md`]. The live falsifier is therefore the *diagonal-vanishing selection rule*, not the magnitude: a detection of any sizeable DIAGONAL moment is the Majorana discriminator, independent of the suppressed overall scale.)

**Assessment.** PASS. The substrate furnishes a clean, zero-free-parameter Majorana-discrimination structure: diagonal-μ=0 is an exact identity inherited from PROVEN [J,D_K]=0, and the transition ratio μ_23/μ_13 = 0.9979 is texture-forced (scale + magneton cancel to machine zero). This is a STRUCTURAL prediction that offsets the oscillation-anchored m_D weakness (A-N1) in the same way as the sterile-null and mass-ordering predictions — the *shape/selection-rule* content is rigid even where the *magnitude* content is anchored. Combined with the J-forced δ_CP ∈ {0,π} (S41 W1-2; [J,D_K]=0), the framework's Majorana sector carries two independent self-conjugacy-test channels (diagonal-μ=0, δ_CP discreteness) beyond the 0νββ lepton-number channel.

**Output artifacts**: `computations/investigation-11/inv11_w2_majorana_transition_mu.{py,npz,png}`; verdict line in `computations/investigation-11/inv11_gate_verdicts.txt`. **Dual-SHA**: audit `bcb17a746cd2813f66449a391a25fefe4ecaca8cef24d3f4b419916ddd7d00da`, content `2654b7d602368836c2545f1b26b251fc9452e08093f24ab2882c80a30afabedc`.

**Note on plan-pinned canonical SHA (plan-text drift)**: the plan §W2-3 input block pins `canonical_constants.py` at `e6829db0…`; the runtime SHA is `ef6243dba5…` (the file evolved between plan-freeze and execution). Per `substrate-first-canonical-sourcing.md §(ii.B)`, the dual-SHA captures runtime ground-truth, and the consumed values are unaffected (M_KK_gravity = 7.42866e16 unchanged; V_B3 loaded from the SHA-matched `s60_lepto_cp.npz`; `s60_lepto_cp_log.txt` SHA `49fdadc5…` matches the plan pin exactly). The audit_sha256 correctly reflects the runtime canonical.

---

### §W2-4. INV11-W2-4-MR-PROVENANCE-AUDIT (orchestrator inline — solo)

**Status**: COMPLETED
**Gate ID**: `INV11-W2-4-MR-PROVENANCE-AUDIT`
**Trigger**: `[AUDIT]`
**Classification**: **PARTICLE** (provenance audit of how the substrate observable M_R feeds the Σm_ν prediction)
**Agent**: `gen-physicist` (orchestrator-inline solo, neutral provenance auditor by design — non-neutrino-author so the audit is not run by the agent with a stake in the seesaw result). SAME closure as a compute gate: it emits a verdict line + this WP section.
**Hypothesis**: The S60 right-handed Majorana scale M_R is DERIVED FROM the SAME B-branch / B3-sector D_K fold eigenvalues the type-I seesaw then consumes — so the seesaw round-trip reldiff (1.16e-5) is by-construction self-consistency, NOT a cross-check; the only potentially-informative number is the SEPARATE 1.77% agreement between M_R and an independently-extracted L12-cache B-branch triple. Verdict: classify the 1.77% as genuine corroboration (independent) vs consistency-check (circular).
**Plan reference**: `sessions/investigation/investigation-11/investigation-11-plan-w2.md` §W2-4 (two-branch classification operator, provenance-trace machinery pin, substitution chain, input-SHA pins).

**Verdict**: **INFO** — `value='classification=definitional_residue(independent_corroboration|consistency_check_circular); roundtrip_1.16e-5=BY-CONSTRUCTION(shared-operand floor=2.8e-16<1e-09); 1.77pct_maxrel=0.017735(re-derived,matches_S99=True); exact_member_in_L12=False(=>distinct_pipelines=True); ...'` scheme=`provenance-trace` convention=`ABSOLUTE` L_max=`12-vs-s54-ED-8x8` (the L12 master cache vs the s54 32-cell ED). `audit_sha256=88f25524988eb97b96e2d320cc8893f706e3ab3b4233524ae697c23fa252fd06` `content_sha256=8b834fc350e407754f7f96356b5d7dfa71212d6df1c14ee058feb91d9d55e051`.

INFO is the pre-registered outcome (plan §W2-4 INFO_meaning): the 1.16e-5 round-trip is confirmed by-construction (clean), but the independent-vs-circular label on the 1.77% is a **definitional, not factual, residue** — both readings of "independent" are admissible on the SAME unambiguous facts. The gate classifies the EPISTEMIC STATUS; it does NOT PASS/FAIL on the 1.77% magnitude.

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- **script** `computations/investigation-11/inv11_w2_mr_provenance_audit.py` — EXISTS (size > 0); `grep -E 'from canonical_constants import'` → PRESENT; `grep -E 'print_verdict_payload'` → PRESENT (def + call). PASS.
- **data** `computations/investigation-11/inv11_w2_mr_provenance_audit.npz` — EXISTS (size > 0; 31 keys incl. `value`, `verdict`, `pipelines_distinct_numerics`, `roundtrip_is_byconstruction`, `min_abs_diff`, `reldiff_recomputed`). PASS.
- **plot** `computations/investigation-11/inv11_w2_mr_provenance_audit.png` — EXISTS (size > 0; provenance-chain diagram + M_R-vs-L12 overlay). [optional per plan]
- **verdict_line** `computations/investigation-11/inv11_gate_verdicts.txt` — `grep -E '^INV11-W2-4-MR-PROVENANCE-AUDIT:.* audit_sha256=[a-f0-9]{64}'` → PRESENT; dual-SHA companion row + 5 provenance extra-rows present. PASS.
- **wp_section** — this section; `**Status**: COMPLETED`, `**Verdict**: ... INFO`, `**Output Artifacts**`, `**MCP Pre-Compute Audit**` all present. PASS.

**MCP Pre-Compute Audit** (queries run before the trace, per knowledge-MCP query-first discipline):
- `search_knowledge('M_R right-handed Majorana scale seesaw Sigma_mnu provenance B-branch fold')` → edge `Sigma_mnu_FW --derived_from--> S96/S99/S100`: provenance text "M_R=D_K B-branch fold energies (M_3(C))" — confirms M_R IS the B-branch fold energies the seesaw consumes.
- `search_knowledge('s54_ed_sweep effective Hamiltonian Seeley-DeWitt moments fold 8x8')` → `s54_ed_sweep.py --depends_on--> a0_fold/a2_fold/a4_fold/S_fold/dS_fold/d2S_fold/tau_fold`: confirms s54 is parameterized by the fold moments; provenance dict `ed_sweep` (session-54).
- `search_knowledge('1.77% M_R coincidence seesaw round-trip crosscheck reldiff corroboration')` → gates `S99-W3-SEESAW-SUMMNU` (crosscheck_reldiff=1.16e-05; MR_coincidence_maxrel=0.0177) + `S96-MATTER-SEESAW-D5` (value=2.20, scheme=`seesaw-vs-direct-DK-reconciliation`, INFO).
- `get_constant('Sigma_mnu_FW')` → 0.0582053272 (S99, `S99-W3-SEESAW-SUMMNU`, not superseded). `get_constant('M_KK')` → 7.428660036284456e16 GeV (S42). `get_constant('a2_fold')` → 2776.165 (zeta-scheme; the moment family s54 consumes).
- `trace_entity('S99-W3-SEESAW-SUMMNU')` → the seesaw gate + npz provenance. `trace_entity('S96-MATTER-SEESAW-D5')` → eq_18003 verbatim: "confirmed by S96-MATTER-SEESAW-D5 **PART-1 spectral-coincidence at <2% against the L12** [cache]" — the 1.77% lineage is the S96 PART-1 nearest-|λ| comparison.
- **PRE-CLOSED status**: the seesaw + Σm_ν is CLOSED/canonical (S99-W3). The 1.77% comparison and the round-trip were ALREADY computed (S96 PART-1 / S99-W3). This gate does NOT recompute them — it READS the numbers and classifies their epistemic status (a NEW provenance verdict, not a re-derivation).

**Results**:

*Provenance chain (factual; traced first-hand from the on-disk source files, all four text-anchors confirmed `True`):*
1. **M_R diagonal** = `E_B3_fold × M_KK`, with `E_B3_fold = E_sp_sweep[fold_idx, 5:8]` (`s60_lepto_cp.py:93`) → `M_1_MKK=E_B3_fold[0]`, etc. (`s60_lepto_cp.py:212-214`) = **[1.00439566, 1.07857332, 1.17000260] M_KK** (bit-identical to the S99-W3 `M_R_MKK`, `max|diff|=0.0`).
2. **`E_sp_sweep[t] = eigenvalues[t, :8]`** (`s54_ed_sweep.py:274`) = the **lowest-8 eigenvalues of the 32-cell tight-binding lattice Hamiltonian** `s54_tb_hamiltonian.npz` (`eigenvalues (50,32)`; cells labelled by SU(3) Casimir; `adj_C2/adj_su2/adj_u1` CG adjacency — `s54_ed_sweep.py:70-78`). So the M_R source is a **lattice-ED pipeline**, parameterized at the fold by the Seeley-DeWitt moments `a0/a2/a4_fold`.
3. **The seesaw** `m_ν = -m_D^T M_R^-1 m_D` consumes the **SAME M_R** built in (1).

*The 1.16e-5 round-trip — BY-CONSTRUCTION (substitution chain, per `math-scripts.md`):*
- **Def 1**: `M_R = diag(E_B3_fold)·M_KK` (Branch 1 above; the array used to BUILD m_ν).
- **Def 2**: `m_ν = -m_D^T M_R^-1 m_D` consumes that same `M_R`.
- **Def 3**: `crosscheck_reldiff = |reconstruct(m_ν, M_R, m_D) − m_ν| / |m_ν|` (round-trip).
- **Substitute**: `reconstruct()` inverts and re-applies the SAME `M_R`, `m_D` used to build `m_ν`.
- **Simplify**: a forward map composed with its own numerical inverse on shared operands ⇒ reldiff is bounded by float64 inversion error. **Re-verified independently here** in the aligned/diagonal basis (`m_ν,i = m_D,i² / M_R,i`): the forward seesaw reproduces the published `m_ν=[0, 0.00867756, 0.04952777] eV` to **2.8e-16** (the float floor).
- **Direction**: same input in ⇒ same input out (up to float inversion) ⇒ the agreement is GUARANTEED by construction, **independent of whether the physics is right**.
- **Conclusion**: the S99-W3 `Sigma_mnu_crosscheck_reldiff = 1.16e-5` carries ZERO independent physical information. **ANNOTATION: by-construction round-trip, NOT a cross-check.**

*The 1.77% coincidence — RE-COMPUTED from the two pipelines (the only potentially-informative number):*
The 1.77% (`M_R_spectral_coincidence_maxrel = 0.017735`) is the `S96-MATTER-SEESAW-D5` PART-1 comparison: it takes the S60 M_R targets (Pipeline-1, lattice-ED) and finds the **nearest |λ| in the L12 master cache** `s84_spectrum_cache_L12_tau019.npz` (Pipeline-2, the **direct full Peter-Weyl block-diagonal diagonalization** D_K = ⊕_{(p,q)} D_{(p,q)}, 90 sectors, 166896 |λ|). Re-computed nearest-|λ| (reproduces the S99-W3 number to 8 sig figs, `matches_S99=True`):

| M_i | M_R (s54 lattice-ED) | nearest L12 \|λ\| | reldiff | min\|diff\| | exact-member (atol 1e-12)? |
|:----|:---------------------|:------------------|:--------|:------------|:---------------------------|
| M_1 | 1.00439566 | 1.02220880 | 1.7735e-2 | 1.781e-2 | **False** |
| M_2 | 1.07857332 | 1.07842811 | 1.3463e-4 | 1.452e-4 | **False** |
| M_3 | 1.17000260 | 1.17583354 | 4.9837e-3 | 5.831e-3 | **False** |

maxrel = **0.01773518** (driven by M_1).

*The DISCRIMINATOR (does the 1.77% compare structurally distinct extractions or the same eigenvalues re-read?):*
**EXACT-MEMBERSHIP FAILS for all three M_i** — none of the M_R values is a literal L12 eigenvalue re-read (`min|diff|` = [1.78e-2, 1.45e-4, 5.83e-3] ≫ float floor 1e-12; even the closely-matching M_2 misses by 1.45e-4 ≫ 1e-12). The two pipelines are **DIFFERENT numerical objects** — a 32-cell tight-binding lattice ED (`s54_tb_hamiltonian`) vs a full Peter-Weyl operator diagonalization (`s84 sector_evals`) — producing **different float eigenvalues** that agree to 0.01–1.77%. This is the cleanest possible discriminator: were the 1.77% a re-extraction of the same eigenvalues, at least the near-coincident M_2 would be an exact member. It is not.

*Classification (the EPISTEMIC verdict):*
- **Track A — distinct NUMERICAL PIPELINE** (the methods differ; not a re-read): TRUE ⇒ `independent_corroboration` (two diagonalization methods, lattice-ED and Peter-Weyl, converging).
- **Track B — same SPECTRAL INPUT** (both extract the SAME operator D_K at the SAME τ_fold near the fundamental): TRUE ⇒ `consistency_check_circular` (a re-extraction consistency of one substrate object).

Both readings are admissible on the SAME unambiguous facts. The FACTUAL core is settled (the round-trip is by-construction; the two pipelines are distinct numerical methods, not a re-read). The LABEL on the 1.77% turns on the DEFINITION of "independent" — distinct-numerical-pipeline (Track A) vs distinct-physical-input (Track B) — a **definitional, not factual, residue**. Per plan §W2-4 INFO_meaning, this is exactly **INFO**.

*Reporting consequence (the gate's purpose):* the verdict prevents over-claiming the 1.77% as strong corroboration. Honest framing: the 1.77% is a **same-operator cross-pipeline consistency** (lattice-ED vs Peter-Weyl convergence at the 1–2% level), which is genuine but **modest** support for the M_R-as-internal-D_K-spectral-object identification — NOT an independent-physical-input confirmation. The 1.16e-5 round-trip is **not** support at all (by-construction). This scopes how the Σm_ν seesaw prediction's corroboration should be reported; the actual capstone/atlas "cross-check"→"by-construction" language fix is a **session-promotion** item (capstone-hygiene Q3 + designated writer), NOT an investigation-track edit.

**Substrate framing**: PARTICLE — a provenance audit of how a substrate-IS observable (M_R) feeds a downstream prediction (Σm_ν). The substrate-IS content is methodological: the right-handed Majorana scale M_R **IS** the B-branch / B3-sector D_K fold eigenvalues × M_KK (S60). Direction preserved: **D_K B-branch eigenvalues → M_R → seesaw → Σm_ν**; the audit traces this chain and flags which agreements are informative (two independent diagonalization pipelines converging — Track A) vs tautological (a forward map and its own inverse — the round-trip). This protects the framework from over-claiming a by-construction self-consistency as evidence, exactly the measurement-first / multi-source discipline the audit enforces. NOT a re-derivation of the seesaw (closed, canonical S99-W3) — a one-thread trace classifying the epistemic status of its corroboration numbers.

**Output 4-tuple**: `(value=definitional_residue(independent_corroboration|consistency_check_circular), scheme=provenance-trace, convention=ABSOLUTE, L_max=12-vs-s54-ED-8x8)`.

---

## Wave 2 Synthesis (team-lead)

**Verdict tally**: 1 PASS (W2-3) + 3 INFO (W2-1, W2-2, W2-4). All four verified on disk (verdict line + dual-SHA, W2-1 [SIGN] 3-tuple, WP §-section `must_contain`; all `audit_sha256` sig_5-unique). **Process note**: W2-4 was NOT run orchestrator-inline (the plan's "solo" framing) — per a mid-session user directive (the orchestrator is not a compute executor; `feedback_orchestrator-not-a-compute-executor.md`) it was dispatched to `gen-physicist` as a neutral, non-author auditor, satisfying BOTH "task agents for computes" AND the plan's auditor-≠-author independence intent. The agent's trace was sharper than an inline pass would have been (it resolved the s54 source to a 32-cell tight-binding-lattice ED and ran the exact-membership test the plan only sketched).

**What the wave establishes.** The neutrino sector's ZERO-FREE-PARAMETER content (counts, NULLs, ratios, selection rules — fixed by spectrum topology + the J / KO-dim-6 selection rules alone) is rigid; the mass-MAGNITUDE content is oscillation-anchored-weak (A-N1; the S102 Yukawa-shape FAIL). Wave 2 harvested four items on the rigid side:

- **W2-1 — sterile-null + ΔN_eff (INFO).** The singlet (0,0) tower has EXACTLY 3 distinct bottoms [0.820, 0.845, 0.971] M_KK (Z₃ triality, PROVEN S03/S28); the dispositive result is a **25.86-decade scale separation** between the O(1) M_KK floor and 1 eV — no spectral home for an eV-scale 3+1 sterile. ΔN_eff_physical = 0 (RH partner non-relativistic at ν-decoupling by 19.87 OOM → Boltzmann exp(−7.5e19)=0; N_eff_nu_FW = 3.0440 = SM). INFO fired on ONE literal sub-criterion — within-singlet gap-ratio 0.8605 < 1.05 — which **mis-modeled the interleaved-tower geometry** (the singlet's 3rd distinct level is its largest; the (0,1) tower interleaves below it). count==3 and both ΔN_eff conditions PASS; [SIGN] 3-tuple sign=PASS/mag=PASS/regime=VALID.
- **W2-2 — absolute-mass triangle (INFO).** From ONE S99-W3 triple m_ν=[0, 0.00868, 0.04953] eV (NO, m₁=0 exact): Σm_ν = 0.05821 eV (19.2% below DESI 0.072), m_β = 8.751 meV (kinematic NON-DETECTION — ×34 below KATRIN, ×4.6 below Project-8: the headline forward number), m_ββ = [1.516, 3.695] meV. INFO because the m_ββ central (3.695) lands ON the Row #80 upper funnel edge by construction (marginal, not interior). The triangle's **internal coherence** (one triple → three independent detector channels) is the substrate-first result; the absolute scale is the soft A-N1 caveat.
- **W2-3 — Majorana transition-μ (PASS).** Diagonal μ_ii = 0 EXACT (self-conjugacy antisymmetry, anchored to PROVEN [J,D_K]=0 / KO-dim=6) — a diagonal-μ detection **falsifies Majorana**, a 2nd self-conjugacy channel beyond 0νββ. Transition ratio μ_23/μ_13 = 0.9979 texture-fixed zero-free-parameter (scale-cancel EXACT). The mass texture V_B3 is SYMMETRIC while the moment matrix is ANTISYMMETRIC — opposite-symmetry, distinct objects.
- **W2-4 — M_R provenance (INFO).** The seesaw round-trip reldiff 1.16e-5 is **BY-CONSTRUCTION** (shared-operand floor 2.8e-16). The 1.77% M_R-vs-L12 agreement: `exact_member_in_L12 = False` ⇒ **distinct pipelines** (s54 32-cell tight-binding-lattice ED vs s84 L12 Peter-Weyl direct diagonalization), but both diagonalize the same D_K-at-τ_fold ⇒ "independent corroboration vs circular" is a **definitional, not factual, residue**.

**Falsifiability ledger.** The wave's shape / selection-rule predictions (rigid) partially offset the mass-magnitude weakness (soft) — the recurring pattern: sterile-null, mass-ordering, and the Majorana selection rules are zero-free-parameter; the absolute scale carries the A-N1 caveat. Combined with the J-forced δ_CP ∈ {0,π}, the Majorana sector now carries **two self-conjugacy-test channels** (diagonal-μ=0, δ_CP discreteness) beyond the 0νββ lepton-number channel.

### What Changed

**(a) Numerical revisions** — Σm_ν = 0.05821 eV; m_β = 8.751 meV; m_ββ central = 3.695 meV; μ_23/μ_13 = 0.9979, μ_12/μ_13 = 0.0994; M_KK→eV scale-sep = 25.86 decades; ΔN_eff_residual_ceiling = 0.01216 → ΔN_eff_physical = 0.

**(b) Structural changes** — sterile-null gate OPERATIONALIZATION: within-singlet gap-ratio → M_KK→eV scale-separation (≥15 decades), a pre-registration fix (W2-1) for HY-class promotion; Majorana sector: 1 test channel (0νββ) → **3** (+ diagonal-μ=0 + δ_CP∈{0,π}); seesaw corroboration epistemics: "cross-check" → 1.16e-5 BY-CONSTRUCTION round-trip + 1.77% distinct-pipeline definitional-residue.

### Effected In-Session (NON-MATH)

- [x] Wave-2 gate WP sections — written by the dispatched agents (W2-1…W2-4 all Status COMPLETED, verified on disk); team-lead synthesis (this section) written.
- [x] No canonical / registry / inventory / capstone edits this wave — correct and mandatory per the investigation-track cross-track boundary (all are session-mode designated-writer, routed to investigation-close). Self-audit: zero unchecked items.

## Carry-Forward Computations

**No math carry-forwards: all Wave-2 outcomes closed in-session or routed to investigation-close session-promotion.** None of the four gates produced a genuine new-compute item satisfying the 4-field test (what/inputs/gate/effort) — the forward content is registry/inventory/capstone promotion handled by `/rclab-investigate --investigation 11` close (designated-writer; mack sole-writer for inventory rows), NOT new computation:

- **W2-1** → HY-class sterile-null + ΔN_eff inventory row, using the **corrected** M_KK→eV scale-separation criterion (≥15 decades), NOT the mis-modeled within-singlet gap-ratio.
- **W2-2** → m_β KATRIN/Project-8 non-detection horizon linking Rows #77/#80 (INFO-tagged: triangle coherent, absolute scale A-N1-soft).
- **W2-3** → second Majorana-test channel (diagonal-μ=0 EXACT + μ_23/μ_13=0.9979) beyond 0νββ inventory row.
- **W2-4** → annotation pass down-tagging the seesaw 1.16e-5 "cross-check" language to "by-construction round-trip" + scoping the 1.77% as distinct-pipeline (capstone/atlas wording, designated-writer).
- **Routed-OUT** (plan §"DEDUP (C)"): HY1 δ_CP∈{0,π} `falsifier-master-inventory.md` row (mack); HY2 stale `Collabs/atlas-neutrino-collab.md` R=27.2 → live-seesaw down-tag.

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-16 | eV-scale 3+1 sterile | under-advertised NULL | INFO — count=3 EXACT + 25.86-dec M_KK→eV gap (dispositive); no eV home | W2-1 |
| 2026-06-16 | ΔN_eff(ν-sector) | un-quantified | = 0 (RH partner non-rel by 19.87 OOM); N_eff_nu_FW=3.044=SM | W2-1 |
| 2026-06-16 | sterile-null gate operationalization | within-singlet gap-ratio (mis-modeled interleaved tower) | M_KK→eV scale-separation ≥15 dec (corrected) | W2-1 forward fix (process obs) |
| 2026-06-16 | absolute-mass triangle | three detector channels separate | one S99-W3 triple → three coherent channels; m_β=8.75 meV non-detection | W2-2 (INFO; m_ββ on band edge) |
| 2026-06-16 | Majorana self-conjugacy tests | 1 channel (0νββ) | +2 (diagonal-μ=0 EXACT, δ_CP∈{0,π}); μ_23/μ_13=0.9979 | W2-3 PASS |
| 2026-06-16 | seesaw 1.77% / 1.16e-5 epistemic status | "cross-check" framing | 1.16e-5 BY-CONSTRUCTION; 1.77% distinct-pipeline definitional-residue | W2-4 INFO |
| 2026-06-16 | canonical_constants.py pin (W2-1/2/3) | e6829db0 (plan-freeze) | ef6243db (runtime); consumed values unaffected | plan-text drift, substrate-first §(ii.B) |
| 2026-06-16 | PMNS pair (Row #80) | plan labeled "NuFit-6.0" | actually PDG (canonical_constants.py:699-702, S101 PAIR-OF-PAIRS); PDG pinned primary | W2-2 mislabel correction |

**Process observation (concurrent-write race)**: the W2-1 agent landed its WP §W2-1 via an atomic Python read-replace-write after the Edit tool lost the mtime race against the concurrent w2-2/w2-3 writers (matched on unique §W2-1 anchors; §W2-2 header count verified =1 after). No content lost — a recurring N>2-concurrent-writers-on-one-WP hazard (`feedback_session-process.md`).

## Files Produced

| Gate | Script (`inv11_w2_*.py`) | Data | Plot | Verdict | audit_sha256 (head) |
|:-----|:------------------------|:-----|:-----|:--------|:--------------------|
| INV11-W2-1-STERILE-NULL-DELTA-NEFF | `sterile_null_delta_neff` | ✓ | ✓ | INFO | `1651ce1d…` |
| INV11-W2-2-ABS-MASS-TRIANGLE | `abs_mass_triangle` | ✓ | ✓ | INFO | `5f4aa7b1…` |
| INV11-W2-3-MAJORANA-TRANSITION-MU | `majorana_transition_mu` | ✓ | ✓ | PASS | `bcb17a74…` |
| INV11-W2-4-MR-PROVENANCE-AUDIT | `mr_provenance_audit` | ✓ | ✓ | INFO | `88f25524…` |

All under `computations/investigation-11/`; verdict lines in `computations/investigation-11/inv11_gate_verdicts.txt` (`track=investigation, session=11`). W2-4 dispatched to `gen-physicist` (neutral auditor), NOT orchestrator-inline.
