# investigation-11 — Distillation Digest

**Reviewer:** landau-condensed-matter-theorist (neutral; not an inv-11 author — seed authors were nazarewicz, neutrino, paasch, quantum-foam, volovik).  **Date:** 2026-06-20.
**Topic:** the M_KK keystone (BCS dimensional-transmutation) + the spectrum-forced neutrino/vacuum sectors + the dynamical-Volovik dark sector + the geometric-sector Planck-scale probes + the compact-object interior.
**inv-1 convergences/bridges executed:** CV-2 (M_KK keystone, B-2); CV-4 (CC/dark sector traded-not-solved, B-7); CV-6/quantum-foam (d_s windowed-γ_E successor, LIV two-speed); CV-7 (dark-sector unreconciled, DM mass); CV-9 (compact-object sector, B-8); partial CV-1/CV-5 (the EFOLD-MAPPING-52 / A_s knot, touched via W3-3).

**Gate tally:** 17 compute/solo verdict lines (4 PASS / 2 FAIL / 11 INFO) over 5 waves + 1 workshop deliverable (W5-1, artifact-existence closure, AGREE two-layer, no verdict line). All 17 verified on disk by content: verdict line + dual-SHA companion, `[SIGN]`-gates carry the 3-tuple row, every `audit_sha256` sig_5-unique. **No missing artifacts.** Verdict-by-wave: W1 1P/0F/3I · W2 1P/0F/3I · W3 0P/1F/3I · W4 2P/1F/1I · W5 (workshop AGREE)/1I. The plan-index "18 gates" count includes the W5-1 workshop (artifact-existence, no verdict line); 17 verdict-emitting + 1 workshop = 18.

---

## 1. Per-gate ledger

| Gate | Verdict | Substrate reading | Framework claim touched (cite) | Verb | Magnitude |
|:-----|:--------|:------------------|:-------------------------------|:-----|:----------|
| INV11-W1-1 (M_KK dimensional transmutation) [FLAGSHIP] | **PASS** | GEOMETRIC — M_KK = Λ·exp(−1/(λ_eff·N₀)), a BCS gap of the fold DOS below M_Pl | M_KK-DERIVATION (S109 keystone, OPEN; CV-2/B-2); NOT a registered closed gate (MCP: only `f_KK=(M_KK/M_Pl)⁴` *factor* exists, S76) | **BOLSTERED** | OOM-dist 0.720 ≤ 1.0 (reduced-Planck), gap-term dominates 0.83; investigation-track |
| INV11-W1-2 (Richardson pairing engine) | INFO | PHONONIC — Δ_rich(B2)=0.4600; mean-field overestimates ×1.591 | atlas-04 B4 (+60% mean-field); R-protected Δ_BCS=0.4642 (S70) | CLARIFIED | clause-1 PASS (ratio 1.59∈[1.4,1.8]); clause-2 FAIL (⟨r⟩=0.4636 vs 0.4118, |Δ|=0.052>0.03) |
| INV11-W1-3 (ATDHFB collective τ_fold) | INFO | GEOMETRIC (Level-2) — collective H localizes transit to fold *region* | A-2 τ_fold dynamical-selection; re-derives FRIED-39 / T6-BROKEN in collective frame | CHALLENGED | τ_sel=0.1734, |Δτ|=0.0166 (INFO band); no interior extremum; SA/BCS gradient 17,827× |
| INV11-W1-4 (Bayesian-UQ posteriors) | INFO | NON-PHONONIC — marginalized posteriors over M_KK/gap/V priors | m_H/CC/H₀/Σm_ν predictions; BF ceiling 31.62 (S101) | CLARIFIED | 5 bands finite; BF_marg=0.040≤ceiling; ≥1 band wider than σ_obs (m_H,CC,Σm_ν) |
| INV11-W2-1 (sterile-null + ΔN_eff) | INFO | PARTICLE — singlet tower 3 bottoms; RH partner non-rel | Z₃ "three generations" PROVEN (MCP-confirmed S03/S28); N_eff_SM=3.044 | CLARIFIED | count=3 PASS; ΔN_eff=0 PASS; dispositive 25.86-dec M_KK→eV gap; within-singlet gap-ratio mis-op (0.86<1.05) → INFO |
| INV11-W2-2 (absolute-mass triangle) | INFO | PARTICLE — one S99-W3 triple → 3 detector channels | Σm_ν<DESI 0.072 (Row #77); m_ββ Row #80; m_β KATRIN/P8 | CLARIFIED | Σ=0.0582 (19% below DESI); m_β=8.75 meV non-detect; m_ββ central ON Row #80 edge (marginal) |
| INV11-W2-3 (Majorana transition-μ) | **PASS** | PARTICLE — diagonal μ_ii=0 EXACT; μ_23/μ_13 texture-fixed | [J,D_K]=0 KO-dim-6 (PROVEN S7-8/S43); S60 V_B3 texture | BOLSTERED | diag μ=0 (machine-exact); μ_23/μ_13=0.9979 scale-free; 2nd Majorana-test channel |
| INV11-W2-4 (M_R provenance audit) | INFO | PARTICLE — M_R IS B-branch D_K fold × M_KK | S99-W3 seesaw Σm_ν "cross-check" framing | CLARIFIED | 1.16e-5 round-trip = BY-CONSTRUCTION; 1.77% = distinct-pipeline (lattice-ED vs Peter-Weyl); independent-vs-circular = definitional residue |
| INV11-W3-1 (emergent dispersion bend) | INFO | GEOMETRIC — substrate band-bottom LINEAR (R²=0.994) | C-1 (W-FOAM-4 exact-LI vs S75 229× two-speed); T3-S43 α_LIV=0 | CLARIFIED | within-band climb 0.656× (NOT 229×); 229× is between-SECTOR; LI-null; residual α_LIV=−5.3e-4→0 |
| INV11-W3-2 (windowed d_s vs CDT, γ_E) | INFO | GEOMETRIC — windowed heat-trace d_s(σ_*)=8.49, NOT 2D | CV-6 d_s-flow; γ_E successor (RED-FLAG: NOT min-d_s<3, NOT dim-spectrum-flow) | CLARIFIED | d_s(σ_*)=8.49∉[1.9,2.1]; γ_E envelope [0.58,0.96] straddles bands → INDETERMINATE (reproduces S93W7-3) |
| INV11-W3-3 (Wheeler-DeWitt Ψ(τ) e-fold) | **FAIL** | GEOMETRIC (Level-2) — WDW WKB defines time direction; not e-fold count | C1 τ↔cosmic-time postulate; EFOLD-MAPPING-52 FAIL (MCP-confirmed N_e=0.1734 IC-indep) | CHALLENGED | clause-i PASS (τ_peak=0); clause-ii FAIL (N_e=0.1734<3.1, gap 2.93); direction half-derived |
| INV11-W3-4 (holographic foam K_pivot) | INFO | GEOMETRIC — holographic δ(lnK)=0.035 dec ≪ 55.31 needed | atlas-07 n_s=0.965 CONDITIONAL on K_pivot; A-4 noiseless-transport | BOLSTERED | INFO-NULL: 0.063% of required shift → A-4 SUPPORTED (sign=PASS/mag=FAIL/regime=VALID) |
| INV11-W4-1 (two-fluid coupled-decay ODE) | **FAIL** | PHONONIC — exchange (1−Γ_eff)=3e-4 sign-correct sink, 53.8× short | BBN-arm G-V1 (ρ_vac/ρ_rad<0.227); rho_vac_over_rho_rad_BBN_below=0.474049 (S98, MCP) | CHALLENGED | sign=PASS/mag=FAIL; BBN stays 0.468 (2.06× bound); **Ω_vac=0.685 ✓ Ω_DM=0.266 ✓ both land** |
| INV11-W4-2 (ρ_vac(q,T) surface) | **PASS** | PHONONIC — surface EXACTLY flat in T to BBN (gap≫T) | atlas-04 C10 tracking ANSATZ→DERIVATION; S97/S101 k_curv=3586.53 | BOLSTERED | anchor rel.err 0.000e+00; n_BBN=1.9755 (|n−2|=0.025); BBN excess REAL (Track A; Track B falsified) |
| INV11-W4-3 (de Sitter decay → w_a) | INFO | PHONONIC — bleed sign-correct (w_a<0), Γ_dS underflow → 0 | wa_FW=0.0 (MCP-confirmed); atlas-04 C5 (3.43σ); DESI DR2 | CHALLENGED | sign=PASS/mag=FAIL; m_min/T~10⁵⁹ → Γ_dS=exp(−2.66e59)=0; w_a=0; σ=3.476 unchanged |
| INV11-W4-4 (Gibbons-Hawking T audit) | **PASS** | NON-PHONONIC — T_local=H/π for Γ_dS; T_GH=H/2π for entropy | de Sitter T-convention (Volovik #11/#15/#35) | CLARIFIED | T_local/T_GH=2 exact; B(T_GH)=[B(T_local)]² residual 0; n_off_by_square=0; unblocks W4-3 |
| INV11-W5-1 (M_KK gap vs integer scheme) [workshop] | **AGREE (two-layer)** | GEOMETRIC — gap sets dimensionful w; integers grade dimensionless Ô | §VII.BS rank-1 (S103-NNU-BUNDLE-EXHAUSTIVENESS PASS, MCP-confirmed σ₂/σ_max=1.07e-17) | CLARIFIED | artifact-existence; rank-1 CONFIRMED (m_e=w·ô_e ⇒ w cancels from N(j), sympy-exact); M_KK 16.9 OOM off ladder |
| INV11-W5-2 (compact-object interior) | INFO | PHONONIC — horizonless Lobo-DE gravastar; v(r)+Mach=1 land | CV-9 compact-object sector (CORPUS-EXCEEDS, B-8); S105-TYPEIV-EMT | BOLSTERED | 2/4: v(r) discharges CF-S105-RELAY-VR; r_h=1.0000; QNM TRAPPED (echo, not ringdown); C_max=2.4e-4 unpinned |

---

## 2. Convergence read-back

**CV-2 — M_KK keystone (the spine, 4-of-5 inv-1 vantages named it): RELOCATED from "frozen-fit" to "dimensional-transmutation-corridor PASS," and its rank-1 status SURVIVED the discrete-scheme adversary.** W1-1 (PASS) derived M_KK/M_Pl = exp(−1/(λ_eff·N₀)) = 3.90×10¹⁷ GeV, 0.720 OOM from CONST-FREEZE-42, with the *gap-magnitude* term (the factor-1.59 mean-field-vs-Richardson ambiguity from W1-2) carrying 83% of the uncertainty budget — the signature of a derived scale rather than a back-fit. The MCP confirms M_KK-DERIVATION was never a closed gate; this is the first substrate-first attempt. W5-1 (workshop, AGREE two-layer) then tested it against Paasch's discrete N(j)=7n scheme and converged: the gap fixes the dimensionful weight w=M_KK (continuous), the integer scheme grades the dimensionless ratios Ô that ride on it — **zero overlap** (M_KK sits N(M_KK)=2.76×10¹³, 16.9 OOM above the heaviest particle rung). The rank-≥2 wedge (does the m_e-anchor import a 2nd scale?) is closed by S103-NNU-BUNDLE-EXHAUSTIVENESS (PASS, σ₂/σ_max=1.07e-17, MCP-confirmed): m_e=w·ô_e ⇒ w cancels from N(j) (sympy-exact). **Verdict: keystone relocated + confirmed, NOT closed** — the convergence is sharpened, with one decisive forward gate (the Ô-interface test) reserving the AGREE-coupled vs AGREE-independent question.

**CV-4 — CC / dark sector "traded not solved": CONFIRMED as a structural feature, with the BBN-arm wound shown REAL and one thermal-relief corridor CLOSED.** W4-2 (PASS) converts the C10 tracking ANSATZ into a DERIVATION (anchor rel.err 0; n_BBN=1.9755) and proves the surface is *exactly flat in T* to BBN — so the BBN excess ρ_vac/ρ_rad=0.474 (canonical S98, MCP-confirmed) is a genuine substrate consequence, not an epoch artifact (Track B falsified). W4-1 (FAIL) then shows the Volovik #35 two-fluid exchange at the substrate-fixed (1−Γ_eff)=3e-4 is sign-correct but 53.8× too weak — the thermal-relief corridor is CLOSED. The dark-sector *reconciliation* nonetheless WORKS (Ω_vac=0.685, Ω_DM=0.266 both land), vindicating the inv-1 CV-4/CV-7 claim that the w=−0.918 vacuum and the w=+1 stiff-DM are the two-fluid decomposition of one substrate, not rival accounts. **Verdict: the CV-4 incoherence is RESOLVED into a sharp boundary** — the wound is real, the thermal cure is dead, and the rescue (if any) is non-thermal (routes to inv-8).

**CV-6 — d_s flow / CDT bridge "misfiled as resolved": CONFIRMED non-analogous at the live (windowed-γ_E) observable, RED-FLAG guard held.** W3-2 (INFO) computed the LIVE successor — windowed heat-trace d_s(σ_*) discriminated by γ_E — explicitly NOT re-proposing the refuted dimension-spectrum-flow or the retired min-d_s<3. Result: d_s(σ_*)=8.49 (NOT 2D at the feature window); γ_E envelope [0.58,0.96] straddles three bands → INDETERMINATE (reproducing S93W7-3 on the investigation track). **Verdict: the inv-1 "misfiled as resolved" diagnosis is half-confirmed** — the windowed observable does NOT inherit CDT's reduction (a clean GEOMETRIC-sector negative), and the γ_E discriminator is structurally inapplicable at the fixed-τ fold; the live route forward is the τ-flow of γ_E (a Level-2 moduli observable), not the fixed-τ fit.

**CV-7 — dark sector unreconciled / DM mass unbuilt: PARTIALLY dissolved (reconciliation done) + DM-mass untouched this investigation.** W4-1's Ω-landing (both components) dissolves the "two parallel unreconciled accounts" half of CV-7. The DM-mass-factor half (the ~14× shortfall, the NSR/pseudogap two-scale route Landau proposed in inv-1) was NOT attacked in inv-11. **Verdict: reconciliation dissolved, mass-magnitude still open.**

**CV-9 — no compact-object sector: BOLSTERED — the sector now has its first interior solution.** W5-2 (INFO, 2/4) built the substrate compact-object interior: a horizonless ultracompact Lobo-DE gravastar (w_core=−0.92), v(r) acoustic flow + Mach=1 horizon at r_h=1.0000 (discharging CF-S105-RELAY-VR-CONSTRUCTION). The two unpinned legs (QNM TRAPPED echo-modes not ringdown; C_max=2.4e-4 underdetermined) are honest underdeterminations, not failures. **Verdict: the CV-9 "best escape from M_KK (dimensionless/anchor-free)" gap is now occupied** — with a falsifiable signature (echoes, not clean ringdown) for LISA-EMRI, though the absolute compactness needs the pinned EOS (CF below).

**CV-1/CV-5 (touched, not central) — the EFOLD-MAPPING-52 / A_s knot: CONFIRMED still the binding wall.** W3-3 (FAIL) shows the bare WDW constraint reproduces *exactly* the EFOLD-MAPPING-52 ceiling N_e=0.1734 (MCP-confirmed structural FAIL, IC-independent), far short of ≥3.1. This is the same N_e=0.1734 that reframes to TRANSIT-PS-67 (FAILed 125σ, S73B) — the CV-1/CV-5 A_s/e-fold knot. **Verdict: inv-11 did not attack TRANSIT-PS-67 (B-1, the survey's single highest-EVOI item); it confirmed, from a new (WDW) direction, that the e-fold history is not supplied by any *bare* substrate mechanism.** The direction-half of C1 (emergent time arrow) IS newly derived; the magnitude-half is not.

---

## 3. Four-verb classification

### BOLSTERED

1. **M_KK is a dimensional-transmutation gap** — *before:* M_KK-DERIVATION is the S109 keystone OPEN gap, frozen-to-Newton since S42, never derived (MCP: no closed gate exists). *after:* dimensional-transmutation-corridor PASS (INV11-W1-1), M_KK/M_Pl=exp(−1/(λ_eff·N₀))=3.90×10¹⁷ GeV. *magnitude:* OOM-dist 0.720 ≤ 1.0 under reduced-Planck cutoff, gap-term dominates the uncertainty (0.83) — a derivation, not a fit. *citation:* INV11-W1-1 (audit 2c51def3…), CV-2/B-2, atlas-05 W3 (1D-theorem). **Investigation-track only — session-promotion required (CF-INV11-W1-A).**

2. **§VII.BS rank-1 single-imported-scale survives the discrete-scheme adversary** — *before:* §VII.BS STAGE-3-PERMANENT (rank-1 proven), but the m_e-anchored Paasch ladder posed an untested rank-≥2 wedge. *after:* rank-1 CONFIRMED as a *measured* count (INV11-W5-1 workshop AGREE; S103-NNU-BUNDLE-EXHAUSTIVENESS PASS, MCP-confirmed). *magnitude:* σ₂/σ_max=1.07e-17; m_e=w·ô_e ⇒ w cancels from N(j) (sympy-exact identity). *citation:* INV11-W5-1, S103-NNU-BUNDLE-EXHAUSTIVENESS, §VII.BS.

3. **The ρ_vac(q,T) C10 tracking-form is a DERIVATION** — *before:* atlas-04 C10 ρ_vac∝H² tracking is an ANSATZ (CV-4: "ρ_vac~H² is overloaded"). *after:* substrate DERIVATION (INV11-W4-2 PASS) — anchor reproduced bit-faithfully, exponent T-stable to BBN. *magnitude:* k_curv rel.err 0.000e+00; n_BBN=1.9755 (|n−2|=0.025 ≤ 0.10). *citation:* INV11-W4-2 (audit 1f721395…), S97/S101 k_curv=3586.531181.

4. **Majorana diagonal-μ=0 is an exact second self-conjugacy channel** — *before:* the Majorana sector carried one lab-test channel (0νββ, Row #80). *after:* +2 channels (diagonal-μ=0 EXACT + the J-forced δ_CP∈{0,π}); μ_23/μ_13=0.9979 texture-fixed zero-free-parameter (INV11-W2-3 PASS). *magnitude:* diagonal vanishes to machine zero; scale-cancellation residual 0. *citation:* INV11-W2-3 (audit bcb17a74…), [J,D_K]=0 KO-dim-6 PROVEN.

5. **The compact-object sector has its first interior solution** — *before:* CORPUS-EXCEEDS, no mass-radius/QNM/formation channel (CV-9). *after:* horizonless Lobo-DE gravastar with v(r)+Mach=1 acoustic horizon (INV11-W5-2 INFO, 2/4); CF-S105-RELAY-VR-CONSTRUCTION discharged. *magnitude:* r_h=1.0000 exact; v₀=0.800; ω₀=0.485 M_KK (trapped). *citation:* INV11-W5-2 (audit 04effc46…), S105-TYPEIV-EMT.

6. **The A-4 noiseless-transport assumption is supported** — *before:* the BZ→pivot transport's noise-freedom was an assumption (A-4). *after:* holographic foam accumulates only 0.063% of the required pivot shift → A-4 SUPPORTED (INV11-W3-4 INFO-NULL). *magnitude:* δ(lnK)=0.035 dec vs 55.31 dec required (factor ~1580× short even coherent). *citation:* INV11-W3-4 (audit 32f8991e…), atlas-07 K_pivot.

### CHALLENGED

1. **The thermal two-fluid relief of the BBN arm is closed (sign-right, 53.8× short)** — *constraint:* the corridor "Volovik two-fluid exchange relieves BBN at (1−Γ_eff)" is CLOSED; BBN-arm G-V1 stays FAIL (ρ_vac/ρ_rad=0.468 > 0.227 bound, 2.06×). *magnitude:* substrate exchange 3e-4 vs needed 0.0162 (53.8×). The FAIL quantifies the exact rescue target a *non-thermal* mechanism must supply. *citation:* INV11-W4-1 (audit d8df09a5…), atlas-04 C10 / BBN-VOLOVIK-67.

2. **The de Sitter decay does NOT source the DESI w_a (sign-right, magnitude underflow)** — *constraint:* atlas-04 C5 (w_a, BROKEN 3.43σ) is NOT relieved by the de Sitter-instability bleed; the corridor is closed at the substrate scale. *magnitude:* m_min/T_local~10⁵⁹ ⇒ Γ_dS=exp(−2.66e59)=0; σ stays 3.476 (frozen baseline). wa_FW=0.0 confirmed unchanged (MCP). *citation:* INV11-W4-3 (audit 3028ae0e…), atlas-04 C5, DESI DR2.

3. **The bare WDW constraint does not supply the inflationary e-fold history** — *constraint:* the corridor "WDW constraint ALONE gives the e-fold history" is closed; N_e=0.1734 (= the EFOLD-MAPPING-52 ceiling, MCP-confirmed structural FAIL) ≪ 3.1. The C1 τ↔time postulate is now half-derived (direction yes, magnitude no). *magnitude:* gap 2.93, below even the acoustic 2.89. *citation:* INV11-W3-3 (audit 966b2dfe…), EFOLD-MAPPING-52.

4. **τ_fold is not dynamically derived by the collective Hamiltonian (FRIED-39 holds in the collective frame)** — *constraint:* the variational sub-route stays closed (E_eff=S_SA+E_cond has no interior extremum); the kinematic first-passage sub-route localizes only to the fold *region*. *magnitude:* |Δτ|=0.0166 (INFO band, not PASS ≤0.010); SA/BCS gradient 17,827× (re-derives FRIED-39/T6-BROKEN 6,596× in the collective frame). *citation:* INV11-W1-3 (audit 3796d72c…), atlas-04 T5/T6 BROKEN.

### CLARIFIED

1. **Richardson-Gaudin is the standard fold-pairing engine; Δ_rich(B2)=0.4600** — truth-value of atlas-04 B4 (+60% mean-field) unchanged; precision up — the R-protected Δ_BCS=0.4642 (S70) IS already the exact/projected-class gap, not mean-field 0.732. The ⟨r⟩ clause-2 FAIL clarifies that the pairing many-body spectrum (⟨r⟩=0.46, GOE-leaning) is a *different* level-statistics object from the single-particle length spectrum (Poisson 0.4118). *citation:* INV11-W1-2 (audit 365600e4…), atlas-04 B4.

2. **Predictions stratify by M_KK-robustness** — Bayesian-UQ confirms H₀=67.4 is δ-sharp (G_N-ratio channel cancels M_KK exactly), while m_H/CC/Σm_ν bands exceed σ_obs once the scale freedom is propagated. Truth-value unchanged; the stratification quantifies *why* W1-1 is the keystone (m_H's point-sharpness was inherited from frozen M_KK). *citation:* INV11-W1-4 (audit 0a1d03f9…).

3. **The sterile-null is carried by a 25.86-decade scale separation, not the within-singlet gap-ratio** — count=3 (Z₃ PROVEN, MCP-confirmed) + ΔN_eff=0 (RH non-rel by 19.9 OOM) both hold; the INFO is a *mis-operationalized literal sub-test* (the within-singlet gap-ratio mis-modeled the interleaved-tower geometry). The dispositive physics is the 25.86-dec M_KK→eV gap. Forward fix: replace the gap-ratio criterion with the scale-separation test (≥15 dec). *citation:* INV11-W2-1 (audit 1651ce1d…).

4. **The absolute-mass triangle is internally coherent across three detector classes** — one S99-W3 triple → Σm_ν (19% below DESI), m_β=8.75 meV (non-detection), m_ββ (central ON the Row #80 edge). Truth-value unchanged; the cross-channel coherence + the kinematic non-detection horizon are clarified. The m_ββ-edge marginality is structural (m₁=0 forbids the deep cancellation null). *citation:* INV11-W2-2 (audit 5f4aa7b1…).

5. **The seesaw Σm_ν "cross-check" is by-construction; the 1.77% is distinct-pipeline** — provenance audit clarifies the epistemic status: the 1.16e-5 round-trip carries ZERO independent information (forward map ∘ its own inverse, floor 2.8e-16); the 1.77% M_R-vs-L12 agreement IS distinct-pipeline (lattice-ED vs Peter-Weyl, exact-membership fails) but both diagonalize the same D_K ⇒ "independent corroboration vs circular" is a definitional, not factual, residue. *citation:* INV11-W2-4 (audit 88f25524…).

6. **C-1 (exact-LI vs 229× two-speed) resolves to the analogue-gravity LI-null** — the substrate band-bottom dispersion is LINEAR (R²=0.994); the 229× is a between-SECTOR ratio (c_Gold Goldstone vs c_fabric bulk-stiffness), each internally Lorentz-invariant; within-band climb 0.656×, NOT 229×. Residual α_LIV=−5.3e-4→0 (S43 structural cancellation). The substrate cannot produce an excluded LIV signal (LHAASO margin 12 OOM). *citation:* INV11-W3-1 (audit 96b6404a…), T3-S43-SPECTRAL-DISSOLUTION.

7. **The de Sitter T-convention is locked (nothing was off-by-square)** — T_local=H/π for Γ_dS, T_GH=H/2π for entropy/first-law; B(T_GH)=[B(T_local)]² residual 0; n_off_by_square=0. Pre-emptive (unblocks W4-3). Truth-value of the framework's existing de Sitter usages unchanged — confirmed correct. *citation:* INV11-W4-4 (audit 76dcd047…).

### MUDDLED

*(none)*. inv-11 is INFO-heavy (11 INFO) but every INFO fired a *pre-registered* clause with a clean structural reading — they are CLARIFIED (precision/scope up) or CHALLENGED (corridor closed), not incoherence-increasing. No "wall disagreeing with itself," no register-tag-outrunning-derivation surfaced *within* inv-11's own results. (The one genuine standing dissonance the investigation *touches but does not resolve* — the A_s wall's internal incoherence, CV-1, where the miss is quoted at 3.02/3.15/4.56/9.5 OOM with a sign-flip across the corpus — is an inv-1/inv-12 object, not an inv-11 product; W3-3 only confirms the e-fold-ceiling half. See §5.)

---

## 4. Routing

### →WORKSHOP (Q1 math/physics adjudication)

**None originate in inv-11.** Per `Investigating-Workshops.md` four-condition test + the Q1/Q2/Q3 discriminator: inv-11's substance contains no genuine two-competing-readings tension that an adversarial R1/R2/R3 panel would resolve into a new pinned structural verdict. The one workshop the investigation *ran* (W5-1, M_KK gap vs integer scheme) already CLOSED to AGREE (two-layer) by artifact-existence — it is a delivered result, not a candidate. Its single forward gate (the Ô-interface test) is a **compute carry-forward** (one agent, pre-registered PASS/INFO/FAIL criterion, reuses the L12 cache) — Q1 NO (no competing readings; the two participants already converged), Q2 NO (a substrate-physics compute, not a status-tag/hygiene move), so it routes to compute-CF, NOT a workshop. This is the honest "no workshops" output for this investigation.

(One *latent* cross-investigation tension exists — the A_s-wall self-incoherence, CV-1 — but it is an inv-1/inv-12 workshop seed, not an inv-11 finding; inv-11 only confirms one half of it. Recorded in §5 as a cross-investigation hook, not lifted here.)

### →COMPUTE-CF (4-field + EVOI)

These are the genuine new-compute carry-forwards inv-11 produced. EVOI tiers are ordinal leverage proxies (`evoi-prioritization.md`), not calibrated probabilities.

**CF-1 (HIGH EVOI) — Session-promote the W1-1 M_KK-derivation PASS** (= the WP's CF-INV11-W1-A).
- *What:* lift INV11-W1-1 into a `session-{N}` compute gate so the dimensional-transmutation PASS can land a `canonical_constants.py` provenance note + an atlas-04/§VII status update (M_KK-DERIVATION: keystone OPEN → transmutation-corridor PASS). Investigation verdicts are track-local and never enter the knowledge index until re-computed under a session gate (`gate-verdicts.md §"Investigation-Track"`).
- *Inputs:* `inv11_w1_mkk_dimensional_transmutation.npz`; `inv11_w1_richardson_pairing_engine.npz` (gap magnitude); CONST-FREEZE-42; M_Pl_reduced convention pin.
- *Gate:* reproduce M_KK_derived to publication precision under a session gate; OOM-dist ≤ 1.0 AND frac_gap ≥ 0.5 re-verified bit-for-bit → designated-writer landing.
- *Effort:* ~1 session (mostly the session re-wrap; physics done). **EVOI: highest — converts the spine's keystone from OPEN to a landed corridor-PASS; the single most consequential promotion inv-11 offers.**

**CF-2 (HIGH EVOI) — The Ô-interface test** (= W5-1's INV11-W5-1-FWD).
- *What:* compute the B2-sector dimensionless ratios feeding λ_eff=V(B2,B2)−mean(Kosmann) and N₀=ρ_B2, and test whether they carry the φ_paasch (1.5315844) / 7n grading the output ladder exhibits (N(p)/N(K)=75/49=1.5306, 0.06% from φ_paasch) — the decisive AGREE-coupled vs AGREE-independent discriminator from W5-1.
- *Inputs:* D_K L12 cache at τ_fold; B2-sector eigenvalue ratios; φ_paasch=1.5315844 (proven_1292); N(j)=7n grid (INV3-W3-4); CONST-FREEZE-42; Δ_BCS=0.46425.
- *Gate:* PASS if B2 ratios reproduce φ_paasch (or a 7n node) ≤1% (layers COUPLED); INFO if a different quantization (independent layers, still AGREE); FAIL-to-CONFLICT only if B2 input ratios provably continuous under a provably discrete output ladder.
- *Effort:* ~1 agent, reuses L12 cache (Friedrich-Bär-saturated, no new diagonalization). **EVOI: high — sharpens the W5-1 AGREE verdict and bears on whether one quantization condition governs the whole Ô-layer.**

**CF-3 (MED EVOI) — The W5-2 natural-split: QNM echo-boundary + EOS pressure-scale** (= CF-INV11-W5-2-QNM-EOS; a Q3 parallel-compute-wave, 3 orthogonal axes + AND closeout).
- *What:* (i) characterize the TRAPPED echo-mode spectrum (Cardoso-Pani w-mode trapping) of the horizonless Lobo-DE core as a LISA-EMRI echo discriminator; (ii) pin the EOS pressure-scale to give a physical M(R)/compactness (C_max=2.4e-4 is ~3 OOM below NS — underdetermined).
- *Inputs:* `inv11_w5_2_compact_object_interior.npz` (65 keys); Lobo-DE EOS w_core=−0.92; the landed v(r); nuclear-EOS-TOV machinery (nazarewicz co-option).
- *Gate:* (i) characterized echo-mode spectrum + LISA-EMRI echo horizon; (ii) M(R) with C≳1e-3, self-bound surface R<0.95·R_grid under a pinned pressure scale.
- *Effort:* ~2–3 agents (wave-together: 3 axes + AND). **EVOI: medium — first anchor-free compact-object falsifier (CV-9), but the dimensionless-but-pressure-scale-underdetermined compactness needs the EOS pin first.**

**CF-4 (MED EVOI) — First-principles M(τ) ATDHFB cranking scan to fix σ_M** (= CF-INV11-W1-C).
- *What:* replace the anchored-with-Gaussian-bump inertia (M_ATDHFB=1.695) with a full ATDHFB cranking M(τ) scan to pin the inertia-bump width σ_M — the single parameter setting W1-3's first-passage localization.
- *Inputs:* L12 cache; ATDHFB cranking linear-response; `inv11_w1_atdhfb_collective_tau_fold.npz`.
- *Gate:* τ_selected within 0.010 of 0.190 (W1-3 PASS band) under the first-principles σ_M.
- *Effort:* ~1–2 sessions. **EVOI: medium — would sharpen W1-3 INFO→PASS, but FRIED-39 monotonicity caps the variational sub-route regardless (only the kinematic dwell can move).**

**CF-5 (MED EVOI) — Resolve dispersion LINEAR-vs-BEND under the discreteness floor** (= CF-INV11-W3-A).
- *What:* re-evaluate band-bottom curvature |2a₂/c_eff²| at a resolution where the discreteness floor < tol_linear=1e-3 (higher L_max if feasible, OR a Friedrich-Bär / continuum argument), pushing W3-1 out of the [1e-3,1e-2] ambiguous band.
- *Inputs:* `inv11_w3_1_emergent_dispersion_bend.npz`; c_Gold, c_fabric; higher-L spectrum OR Friedrich-Bär saturation.
- *Gate:* |2a₂/c_eff²| resolved with floor < 1e-3: LINEAR if <tol (C-1 LI-null confirmed), BEND (+α_LIV) if >tol.
- *Effort:* ~1–2 sessions (L_max≥13 may be infeasible; analytic continuum is the fallback). **EVOI: medium — the substrate residual is *predicted* →0 by S43, so the expected outcome is LINEAR-confirm; leverage is on closing C-1 definitively.**

**CF-6 (MED EVOI) — τ-flow of γ_E vs v_g^B2** (the W3-2 forward discriminator).
- *What:* compute γ_E(τ) and v_g^B2(τ) on a τ-grid [0.15,0.23] (≥7 pts, NORMAL state, L12 cache) + the τ-correlation discriminator, sidestepping the one-sided starvation that defeats the fixed-τ γ_E fit.
- *Inputs:* s84/s92 L12 caches; the γ_E=1−1/n order map.
- *Gate:* KK iff γ_E(τ) τ-stable near 1/2 ∧ v_g^B2(τ) finite at τ_fold; Landau iff γ_E(τ)→1 ⟷ v_g^B2(τ)→0.
- *Effort:* ~0.5 wave (spectra exist; the work is the τ-scan + v_g band-ladder fit). **EVOI: medium — the only route that can make the windowed-d_s/CDT comparison decisive; a Level-2 observable immune to the fixed-τ starvation.**

**CF-7 (LOW EVOI) — Acoustic-source WKB e-fold history (non-bare WDW)** (= CF-INV11-W3-B).
- *What:* recompute the WDW Ψ(τ) WKB e-fold integral with the acoustic/GGE source included (not bare minisuperspace), testing N_e ≥ 3.1 (the acoustic 2.8913 anchor).
- *Inputs:* `inv11_w3_3_wheeler_dewitt_psi_tau.npz`; acoustic N_e=2.8913; the GGE/acoustic source term.
- *Gate:* WKB N_e ≥ 3.1.
- *Effort:* ~1–2 sessions. **EVOI: low — the acoustic ceiling itself is 2.89 < 3.1, and TRANSIT-PS-67 already FAILed 125σ (S73B); the e-fold corridor is heavily constrained from the start. Subordinate to the B-1 Parker-Bogoliubov route the survey actually prioritizes.**

**CF-8 (LOW EVOI) — Substrate-internal cutoff Λ to remove the M_Pl anchor** (= CF-INV11-W1-B).
- *What:* re-derive M_KK with the UV cutoff Λ pinned from a substrate-internal quantity (off-Jensen free-modulus / HY8 top-of-spectrum) instead of M_Pl, closing the W1-1 reduced/unreduced (0.72-vs-1.42 OOM) cutoff-normalization freedom.
- *Inputs:* `inv11_w1_mkk_dimensional_transmutation.npz`; off-Jensen modulus / HY8 spectrum; L12 top-of-spectrum max|λ|.
- *Gate:* OOM-dist ≤ 1.0 with a substrate-internal Λ (no M_Pl anchor) AND frac_gap ≥ 0.5.
- *Effort:* ~1–2 sessions. **EVOI: low — feeds CF-2/W5-1; the reduced-Planck reading is already PRIMARY and in-band, so removing the anchor is a robustness refinement, not a gap-closer.**

**CF-9 (LOW EVOI) — Finer-L blocked-⟨r⟩ cross-check** (= CF-INV11-W1-D).
- *What:* recompute the W1-2 blocked-(odd-N) Richardson ⟨r⟩ at L_max≥16 to test whether the 0.052 miss to the length-spectrum 0.4118 closes with truncation.
- *Inputs:* finer-L (≥16) cache; `inv11_w1_richardson_pairing_engine.npz` blocked routine.
- *Gate:* |⟨r⟩_blocking − 0.4118| ≤ 0.03.
- *Effort:* ~1 session. **EVOI: low — the W1-2 ratio (the load-bearing result) PASSed; the ⟨r⟩ tie is a secondary integrability question (the two are different objects regardless of L).**

**Cross-investigation hand-off (NOT a new inv-11 compute):** the BBN-arm (G-V1) and w_a (C5) wounds route to **inv-8 RG-running-vacuum / Kibble-Zurek-wall** — a non-thermal, non-Boltzmann mechanism that escapes the gap-suppression that closed W4-1/W4-3. Precise targets inv-11 hands it: g_eff=0.0162 (54× the 3e-4 leak) for BBN; the Γ_dS-underflow result (thermal route dead) for w_a.

### →HOUSEKEEPING (register cell + fix)

inv-11 has **no housekeeping file** (confirmed); its routed-out hygiene is the seed §"DEDUP (C)" list (HY1-HY8, rescued in §6). The CLARIFIED items above that are designated-writer register touches (NOT new computes) route to session-promotion at investigation-close:

- atlas-04 C10 re-tag (W4-2: scaling-form DERIVED + T-stable-to-BBN; W4-1: BBN-arm magnitude FAIL-at-2× stands) = HY5.
- atlas-04 C5 cross-ref (W4-3: de Sitter-decay mechanism evaluated-and-NULL at substrate scale; C5 stays BROKEN) — `mack-cosmic-bridge` sole-writer.
- §VII.BS annotation (W5-1: rank-1 CONFIRMED as a measured count, σ₂/σ_max=1.07e-17; no rank-≥2 re-scope) — designated writer.
- W2-1 sterile-null operationalization fix (gap-ratio → ≥15-dec scale-separation) for any HY-class promotion.
- W2-4 seesaw-corroboration wording (capstone "cross-check" → "by-construction round-trip" + 1.77% distinct-pipeline) — capstone-hygiene Q3, designated writer.

### →CLOSED (corridor + note)

- **Thermal two-fluid BBN-relief at (1−Γ_eff)** — CLOSED (W4-1, 53.8× short). Note: sign-correct; the rescue is non-thermal.
- **De Sitter-instability bleed as the DESI w_a source** — CLOSED at the substrate scale (W4-3, Γ_dS underflow). Note: direction vindicated, magnitude null; C5 stays BROKEN with a *reason* (gap≫T).
- **Bare WDW constraint as the e-fold-history source** — CLOSED (W3-3, N_e=0.1734=EFOLD-MAPPING-52 ceiling). Note: the time *direction* IS newly derived; the e-fold count needs an external (acoustic/Parker) pump.
- **Holographic foam as the K_pivot mechanism** — CLOSED via INFO-NULL (W3-4); framework-strengthening (A-4 supported). Note: the pivot is set by the existing transport map, not foam.
- **Pure-SA / collective-variational τ_fold selection** — CONFIRMED-CLOSED in the collective frame (W1-3; FRIED-39/T6-BROKEN re-derived 17,827×). Note: only the kinematic first-passage dwell localizes, and only to the fold region.

---

## 5. Cross-investigation hooks (for Stage-2 rollup)

- **M_KK cluster (inv-3, inv-6, inv-11):** all three attack CV-2/B-2. inv-11 W1-1 owns the BCS dimensional-transmutation *PASS*; inv-3 W4-1 ran the spectral-geometer↔paasch M_KK *derivability* workshop (DISTINCT pair/machinery from W5-1's nazarewicz↔paasch); inv-6 W2-4 owns the low-k O(k⁴) LIV coefficient (complementary to W3-1's full c_Gold→c_fabric band). The W5-1 Ô-interface forward gate (CF-2) explicitly consumes the INV3-W3-4 N(j)=7n grid — a hard inv-3↔inv-11 dependency. **Stage-2 should net these into one M_KK verdict** (the keystone is relocated-to-corridor-PASS + rank-1-confirmed; the open residual is the Ô-interface coupling and the cutoff-normalization freedom).

- **Dark-sector / BBN / w_a (inv-7, inv-8, inv-11):** inv-11 W4 owns the *thermal* relief corridors (both CLOSED) + the C10 derivation (PASS) + the Ω-reconciliation (vindicated). inv-7 owns the effective-Friedmann functional form (CV-3, B-4) and the n_PBH physical-vs-tautology workshop; inv-8 owns the running-vacuum-RG / KZ-wall route inv-11 explicitly hands the BBN/w_a wounds to. **Stage-2: the BBN-arm and w_a verdicts must combine inv-11's "thermal route dead, here are the exact targets" with inv-8's non-thermal attempt** — neither is complete alone.

- **Compact-object (inv-4, inv-9, inv-11):** inv-11 W5-2 owns the *interior* (gravastar v(r)+Mach=1, CV-9/B-8); inv-4 owns the CV-9 compact-object/greybody/Page cluster from the GR side; inv-9 owns the cross-framework QG / sum-over-geometries angle. **Stage-2: the compact-object falsifier (echoes-not-ringdown) is the cross-cut**; the CF-3 QNM-echo + EOS-pin wave-together is its compute home.

- **A_s / e-fold knot (inv-1 CV-1/CV-5, inv-5, inv-12, inv-11-partial):** inv-11 W3-3 confirms the e-fold-ceiling half (N_e=0.1734) from the WDW direction but does NOT touch TRANSIT-PS-67 (B-1, the survey's #1-EVOI item) or the A_s-functional incoherence (the 3.02/3.15/4.56/9.5-OOM + sign-flip wall). inv-5 owns the A_s impulse-quench (CV-1) + the two-effective-actions tension; inv-12 owns the A_s-wall 6-route hub + "is Tr f(D²) the right functional" (CV-4 SA≠free-energy). **Stage-2: inv-11 contributes only the WDW-direction confirmation to this knot** — the live workshop seed (the self-incoherent A_s wall) belongs to inv-5/inv-12, not inv-11.

- **Spectral-dimension / CDT (inv-3, inv-9, inv-11):** inv-11 W3-2 owns the windowed-heat-trace-γ_E successor (the LIVE object after min-d_s<3 was retired); inv-9 kaku R-2 owns the RED-FLAG (the refuted dimension-spectrum-flow). **Stage-2: the d_s/CDT verdict is "non-analogous at the windowed observable, INDETERMINATE discriminator"** — the τ-flow-of-γ_E (CF-6) is the only route that can make it decisive.

---

## 6. Stranded hygiene (rescue list)

inv-11 has no housekeeping file; the following HY1-HY8 live ONLY in the seed §"DEDUP (C)" (a PLAN/SEED file) and target session-track registers an investigation cannot mutate (track-local boundary). They are rescued here for Stage-3 routing to session-promotion / designated-writer (NOT workshops; NOT inv-11 edits). Several are routed by BOTH inv-3 and inv-11 — `/rclab-investigate` dedups at close.

| HY | Item | Session-track target | Routing note |
|:---|:-----|:---------------------|:-------------|
| HY1 | Register δ_CP∈{0,π} (J=0 from [J,D_K]=0) as a named falsifier-inventory row + DUNE/Hyper-K horizon + the ~1.5–2σ NuFIT-6.0 (≈230°) tension. | `falsifier-master-inventory.md` (mack sole-writer) | σ-tension + horizon near-trivial; J=0→{0,π} already proven. Registry-write, not a compute. |
| HY2 | Down-tag stale `atlas-neutrino-collab.md` R=27.2 prose → live seesaw Σm_ν; mark R=27.2 superseded by `S96-MATTER-R-HIERARCHY`=9.86 FAIL. | `Collabs/atlas-neutrino-collab.md` | Capstone-hygiene Q3 (prose tag == register tag). **Also flagged in inv-1 §4 item 5.** |
| HY3 | Promote the geometry/topology dichotomy ([H_foam, topological-index]=0 vs spectral-geometry-not-foam-stable) to a numbered wall / §VII slot. | `atlas-05` / `permanent-results-registry.md` | Organizing wall explaining the robust(topological)-vs-fragile(geometric) split inv-11 W3 confirmed throughout. |
| HY4 | Unify Ω_GW retirement + GQuEST/LISA foam-strain nulls into one fabric-gap sterility theorem (f_gap=3.96e40 Hz). | `falsifier-master-inventory.md` (mack sole-writer) | Sharpens falsifiability. (BBN-epoch density-scaled foam-fluctuation portion is a COMPUTE; the unification is a registry edit.) |
| HY5 | Re-tag atlas-04 C10 "CONFIRMED-TRACKING-FORM" → "CONFIRMED-PRESENT-EPOCH / BBN-FALSIFIED-AT-2×" (Layer-1 done / Layer-2 BBN FAIL). | `atlas-04-assumptions.md` | Capstone-hygiene Q3. **Directly supported by inv-11 W4-2 (form DERIVED) + W4-1 (BBN 2.06× FAIL stands).** |
| HY6 | Promote/make-load-bearing q=det(g_K)^{1/2} elasticity-tetrad (currently MIGRATED/INFO) + its connection to *why* topological baryogenesis fails (p₁[SU(3)]=0). | registry (Jensen↔q-theory mapping) | Structural keystone the W4-1/W4-2 CC↔Jensen bridge leans on. Re-run-as-live-gate portion could be a session compute; promotion is registry. |
| HY7 | Tag φ_paasch in the constant store (PROVEN-bare-ratio (3,0)/(0,0) at τ=0.15; BdG destroys it PHI-BDG-47 FAIL; recursion-invariant S42) + record Paasch LNH (Dirac G~1/t) exclusion. | `canonical_constants.py` PROVENANCE + capstone-hygiene Q3 | **Also routed by inv-3.** φ_paasch is W5-1's load-bearing input (proven_1292) — tag it canonically. |
| HY8 | Reconcile stale `constraint-mega-matrix.md` "off-Jensen 5D moduli" surviving-channel (closed S76 W2-J, ridge-confined) — remove as landscape-channel while preserving the distinct off-Jensen-free-modulus question for dynamical M_KK/τ relaxation. | `constraint-mega-matrix.md` | Bookkeeping-vs-physics split: landscape closed; the free-modulus question is the natural home for W1-1/W1-3 (CF-8) if the Jensen-line route degenerates. |

**Process observation (one upstream miss, recorded not propagated):** inv-11 produced no `session-{N}-housekeeping.md`; its Q2 hygiene lives only in the SEED. Per `Investigating-Workshops.md §"Enforcement"`, the canonical Q2 ledger should exist before `/rclab-investigate`; for inv-11 the seed §"DEDUP (C)" served as the de-facto ledger. This is a wave-synthesis-completeness note for Stage-3, not a finding.
