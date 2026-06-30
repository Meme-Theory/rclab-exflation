# Session 99 Consolidation: S99 Research-Sweep Review Campaign — Planning-Consumable Synthesis

**Date**: 2026-06-04
**Agent**: gen-physicist (Workhorse-Gen-Physicist)
**Source Documents** (19 review reports + 1 register):
- R1 per-folder (8 folders × 2 agents): G1 emergent-spacetime (`…-emergent-spacetime-volovik.md`, `…-emergent-spacetime-phonon-first.md`); G2 dark-energy (`…-dark-energy-mack.md`, `…-dark-energy-sagan.md`); G3 neutrino-seesaw (`…-neutrino-seesaw-dirac.md`, `…-neutrino-seesaw-neutrino.md`); G4 NCG-spectral-action (`…-ncg-spectral-action-connes.md`, `…-ncg-spectral-action-lizzi.md`); G5 spectral-geometry (`…-spectral-geometry-spectral-geometer.md`, `…-spectral-geometry-baptista.md`); G6 nonequilibrium-transit (`…-nonequilibrium-transit-transit.md`, `…-nonequilibrium-transit-kitaev.md`); G7 flatband-geometry (`…-flatband-geometry-landau.md`, `…-flatband-geometry-berry.md`); G8 jwst-lrd (`…-jwst-lrd-little-red-dots.md`, `…-jwst-lrd-mack.md`).
- R3 cross-cutting (1 X-cut × 3 agents): `…-x-c10-vacuum-profile-mack.md`, `…-x-c10-vacuum-profile-volovik.md`, `…-x-c10-vacuum-profile-einstein.md`.
- Register: `sessions/evoi-framework.md` (S100-stamped guiding star).
- Canonical anchoring: knowledge MCP (`get_constant`, `search_knowledge`, `query_entity`) on 2026-06-04.

---

## I. Consolidation Outcome

This is a consolidation, NOT a compute session — **no gate verdict is re-adjudicated, no framework probability moves**. The 19 reports converge on a single highest-leverage compute and a handful of genuine forward gates; the rest is consistency-mapping or hygiene. The four numbered Focus deliverables follow as §II–§V.

**The one load-bearing convergence** (all three R3 agents + both G1 + both G2 = 7 independent reports): the C10/CC-residual BBN arm collapses to ONE compute, `CF-S100-W2-1-QEQ-DRIVE`, re-scoped to dual-output. The magnitude corridor is canonically CLOSED (`S99-W2-BBN-RELIEF` FAIL, three mechanisms non-substrate-justified); the time-profile corridor (post-BBN production / EDE-like dilution) is genuinely OPEN and is strictly DOWNSTREAM of `CF-S100-W2-1-QEQ-DRIVE` — a BBN-arm gate is a read-out CLAUSE on that drive, not an independent calculation. The canonical early-vacuum is a Volovik tracking vacuum `ρ_vac = α_V M_Pl² H^{n_eff}` with `n_eff = 1.978` ≈ 2 (substrate-IS: the a₀ Seeley-DeWitt zeroth spectral moment tracking H), which is radiation-like by construction — EDE-like relief is a *departure* from the tracking law, not a tuning of it.

**Three paired-report DISAGREEMENTS surfaced** (flagged, not averaged — §III.E): (1) the **n_eff-direction conflict** between canonical S66 (n_eff=2.3 PASS via 2% G_eff bound) and S98/S99 (n_eff<2 FAIL via the ΔN_eff lever) — surfaced only by volovik+einstein (R3), NOT by mack (R3); (2) the **G3 sector-conflation** — dirac (G3) flags the substrate δ_CP ∈ {0,π} (PMNS) vs π/2 (K_7 transit), correcting the index's claimed B-class match, while neutrino (G3) leans into the π/2 resonance with only a milder tension flag; (3) the **Ordered-Veil status** — both G6 reports (transit + kitaev) flag "GGE never thermalizes" as canonically BROKEN/RETRACTED-S39, inverting how G4/G5 narrate the Ordered Veil as a live falsifier.

**Honest count**: across 19 reports the genuine forward-compute candidates deduplicate to **~14 distinct gates**; the remainder are hygiene (registry-slot relabels, constant re-pins, sector-disambiguation) routed to §A-style in-session fixes, and consistency ceilings (the entire G8 group below the z<10²⁸ discrimination wall) that produce joint constraints, not discriminators. I do not pad: every G5/G7 paper produced a real validation angle but most are LOW-EVOI math-rigor cross-checks of ALREADY-PROVEN machinery.

Canonical anchors verified (knowledge MCP, 2026-06-04, none superseded): `delta_N_eff_vacuum_BBN_below = 2.0873` (S98); `Sigma_mnu_FW = 0.0582053272` (S99 PASS); GGE-permanence **RETRACTED-S39** (atlas-04 T3 BROKEN + atlas-07; t_therm ≈ 6 M_KK⁻¹, Brody β=0.633); `LRD_demographics_not_discriminating` STAGING (z<10²⁸); §VII.AF.1 = the R_geom HP¹ quantum-metric bridge (s86-hp1 session), §VII.W = HP parity-grading orthogonality (the G7 slot-correction is sound).

---

## II. Per-Group Top-3 Candidate Validation Angles (4-field carry-forward specs)

Deduplicated across each group's paired independent reports. Where the pair disagrees, the conflict is flagged inline (full adjudication in §III.E). Gate-IDs follow each pair's naming where they agree; I assign a consolidated ID where they diverge. EVOI tier mapping is in §IV; routing is in §V.

### G1 — Emergent-Spacetime / Superfluid-Vacuum (volovik + phonon-first)

**G1-1. SF54 non-ratio expansion observable** *(both reports, CONVERGENT)*
- **What**: Define and compute the SF54 substrate expansion observable as an integrated spectral moment `M_exp = ∫ N(k) w(k) dk` over post-transit GGE occupation N(k) (the spectral-action image of the BEC phonon pair-production power spectrum), REPLACING the conformally-stationary ratio-form deceleration q = ä·a/ȧ² (which is 0/0 on the a₂-canonical acoustic frame). Verify frame-independence where q is 0/0.
- **Inputs**: s53 KZ pair-production (P_exc=1.000, N_pair=59.8); 8-mode BCS Bogoliubov fold spectrum (B1 acoustic, S74 W1-H); `S99-W1-Q-NONRATIO-OBSERVABLE` npz (`arr_H_bare_t` backbone, audit 8bcbca9c); τ_fold=0.19; papers 01/03/11 (BEC FLRW, spinor-Proca, spin-sonic Hawking) as methodological cross-check.
- **Gate**: `CF-S100-W1-SF54-MAPPING` (Tier-1 #1 successor). PASS: M_exp finite + frame-independent (≥2 frames agree <1%); FAIL: inherits 0/0 degeneracy; INFO: finite but transit-independent.
- **Effort**: 4–6 hours, 1 agent session.
- **Note (einstein R3 correction)**: the W1 non-ratio observable already landed INFO in S99 and EXPORTED the H_bare backbone; the dependency is W1(done)→W2-1(done,FAIL)→QEQ-DRIVE(open), SEQUENTIAL not parallel. SF54-MAPPING is the band-membership re-derivation (band_frac 0.490<0.90), distinct from the non-ratio observable per se.

**G1-2. Object-C q_eq(H) drive — substrate friction-ODE** *(both reports, CONVERGENT; THE keystone)*
- **What**: Derive the substrate-internal q_eq(H) relaxation map from `q″ + 3Hq′ + V′(q)=0` with V=δρ_vac from D_K (NOT the imposed linear closure q_eq=c·H), re-integrating WITHOUT the imposed fluid closure. Test whether the Jensen constraint (det g_τ=const, ONE constraint) fixes (ε(q),G(q)) without paper-04's measure-zero 1D Minkowski separatrix.
- **Inputs**: `S98-MK3-1-C10-SUBLEADING-SIGN` npz (sign_a3_meas=−1, a3_q0_analytic=−881.5351 — drive sign already derived); `s99_w2_relaxation_closure.npz` (bare-ODE oscillator, k_curv=+3586.5); `arr_H_bare_t` backbone; Volovik Gibbs-Duhem ρ_V=ε−q dε/dq=0 (S95 EQUILIBRIUM-CC-WARRANT); paper 04 friction-ODE (Klinkhamer-Savelainen-Volovik), paper 02 f(R) ε_vac(H)=f(R=12H²) as candidate drives.
- **Gate**: `CF-S100-W2-1-QEQ-DRIVE` (Tier-1 #2 successor), [SIGN], **re-scoped to DUAL output per all 3 R3 agents**: (slope clause) PASS iff |d ln q/d ln H − 1| ≤ 0.05 UNFORCED (§8.5 OPEN→CLOSED); (BBN read-out clause, NEW) emit the early-time radiation-era ρ_vac(a) trajectory feeding G1-3/X-cut regardless of slope verdict; FAIL iff no substrate q_eq(H) exists (n=2 structurally a fluid-closure input).
- **Effort**: 6–8 hours, 1–2 agent sessions.

**G1-3. f(R)-profile / q-theory BBN time-profile check** *(both reports, CONVERGENT in substance)*
- **What**: Compute the early-time radiation-era ρ_vac(a) implied by the QEQ-DRIVE output (or the paper-02 f(R) form), classify radiation-like (a-exponent ≥0) vs EDE-like (∝a^{−n}, n>4) vs post-BBN-produced, and evaluate ΔN_eff at BOTH BBN (T~1 MeV) AND recombination.
- **Inputs**: G1-2 output q_eq(H); `delta_N_eff_vacuum_BBN_below=2.0873`; `rho_vac_over_rho_rad_BBN_below=0.474049`; canonical S66 formula ΔN_eff=(ρ_vac/ρ_rad)/((7/8)(4/11)^{4/3}), bound 0.227113; X_BBN=40.2756; paper-11 external budget 0.107 (combined BBN+CMB+BAO, NON-canonical — flag tag).
- **Gate**: `S100-X-C10-RHOVAC-EPOCH-PROFILE` [SIGN], CONDITIONAL/trigger-first (fires iff G1-2 returns a non-tracking q_eq(H)). PASS: ΔN_eff ≤ 1 at BOTH epochs AND EDE-like-or-later; INFO: clears canonical 0.227 at BBN but not external 0.107 OR Ω_b h²→D/H unchecked; FAIL: radiation-like (19.51× exceedance stands); CONDITIONAL-SKIP-as-INFO iff G1-2 FAILs (tracking law stays imposed-closure ⇒ radiation-like reading stands).
- **Effort**: 3–4 hours, 1 agent session (downstream of G1-2; this IS the X-cut load-bearing gate — see §III.A).

*(G1 lower-EVOI angles routed but not top-3: N_3-horizon-consistency confirmation gate, lab-platform falsifier consolidation, metastring w₀-wₐ benchmark — §V.)*

### G2 — Dark-Energy / Expansion-History Observational (mack + sagan)

**G2-1. Substrate ρ_vac(a) time-profile — C10 relief discriminator** *(both reports, CONVERGENT)* — **MERGES with G1-3 / X-cut as ONE gate**
- **What**: Identical in substance to G1-3 and the X-cut V.1; the three groups (G1, G2, R3) name the same compute. Trace the a₀-zeroth-moment / GGE-relic occupation across fold→BBN→recombination; classify the profile; emit both epoch-resolved fractions.
- **Inputs**: as G1-3, plus T_RH=1.70e15 GeV (S76 — **non-canonical, flag**; volovik R3 hygiene), Ω_b/ω_H2 (verify canonical at run-time; sagan's pins Ω_b=0.0493 NOT independently confirmed).
- **Gate**: see G1-3 (`S100-X-C10-RHOVAC-EPOCH-PROFILE`). The G2/R3/G1 triple-naming is a dedup, not three gates.
- **Effort**: 4–6 hours, 1–2 agent sessions.

**G2-2. w_a=0 lock vs Planck-low-ℓ-independent CMB combination** *(both reports, CONVERGENT)*
- **What**: Score `wa_FW=0` (S58 four-fold lock) against the ACT/SPT+WMAP (Planck-low-ℓ-independent)+DESI DR2 BAO+Pantheon+ combination that papers 02/03/05 identify as systematics-robust. Use paper-05 compressed Planck+ACT datavector (R=1.7504, ℓ_a=301.77, Ω_b h²=0.022371) — no full Boltzmann run.
- **Inputs**: wa_FW=0; paper 03 (Giarè) ACT+WMAP+BAO+Pantheon+ (CC within 2σ, w_a→0); paper 05 compressed likelihood; canonical σ-distances 2.92σ (DR2-marginalized) / 3.74σ (DESY5-joint).
- **Gate**: `S100-WA-ROBUST` (new falsifier-watchlist sub-row). PASS: |w_a=0 − w_a,recovered|/σ < 2 in the robust combination; INFO: 2–3σ; FAIL: >3σ even Planck-independent.
- **Effort**: 4–6 hours, 1 agent session.
- **Caveat (sagan)**: w_a=0 is a null ΛCDM shares; the lock earns falsification-SURVIVAL, not Bayesian credit over ΛCDM. The discriminator is w_0 at fixed w_a=0.

**G2-3. w_0 branch-resolution: canonical −0.918 vs R_842 −0.842454** *(sagan emphasizes; mack notes anchor-currency)*
- **What**: Execute/re-confirm `w0-primary-decision-rule.md` to determine the canonical w_0 branch on INDEPENDENT geometric grounds (NOT by proximity to data). Until resolved, the 0.731σ R_842-vs-post-Dovekie proximity is branch-shopping-adjacent and cannot be scored as a PASS.
- **Inputs**: `w0-primary-decision-rule.md` (w_0_A=−0.918 Volovik partition; w_0_B=−0.842454 substrate-compaction branch-iv); `S84-W0-REGULATOR-RESOLUTION-SV1` (L_max convergence of R_JE); regulator convergence at L_max=12.
- **Gate**: feeds Falsifier-1 (w_0/R_842 rectangle) + DR3 readiness. PASS: branch-iv converges to a stable value by L_max=12 (genuine prediction, pin it); FAIL: R_JE keeps drifting (branch-iv not a stable prediction).
- **Effort**: 3–4 hours, 1 agent session.
- **Conflict flagged (anchor-currency, both reports agree)**: the 0.081σ Pantheon+ headline is vs a SUPERSEDED anchor; the live register anchor is post-Dovekie −0.803 → 0.731σ (R_842) / 2.130σ (canonical). Hygiene re-anchor routed to mack (§V).

*(G2 lower-EVOI: timescape ln B>5 Bayesian SN; σ8 re-positioning vs KiDS-Legacy (registry-hygiene, both reports flag tension-direction REVERSAL — both framework channels now below BOTH high anchors); ALPHA-ENV-43 status reconciliation (sagan flags register internally inconsistent: "CLOSED-S56" graph-edge vs "queued" memory); H_0=65.4 LIVE-PENDING correction (both reports flag index over-states it as firm; sagan corrects σ-distance to 1.88σ via lower-error-bar). §V.)*

### G3 — Neutrino Mass / Seesaw vs Cosmology (dirac + neutrino)

**G3-1. m_D normalization from D_K — close the oscillation-anchored caveat** *(both reports, CONVERGENT)*
- **What**: Derive the Dirac-mass m_D entries (Yukawa Y_i) from the off-diagonal gauge-connection relay structure of D_K on Jensen-deformed SU(3), replacing the oscillation-anchored Y_i; re-compute Σm_ν zero-free-parameter.
- **Inputs**: D_K B-branch fold-energy spectrum at L_max=12 (s99 seesaw npz); M_KK=7.42866e16; `S96-MATTER-SEESAW-D5` ratio=2.2016 (s96 npz); M_1/M_2/M_3=7.46e16/8.01e16/8.69e16 GeV (S60); `Sigma_mnu_FW=0.0582053272`.
- **Gate**: `CF-S100-MD-NORMALIZATION` (Tier-1 #3 successor). PASS: Σm_ν(zero-free m_D) reproduces 0.0582 eV within crosscheck tol (reldiff<1.16e-05) AND MR_coincidence residual ≤0.0177; INFO: within 2×; FAIL: >2× or wrong ordering.
- **Effort**: 4–6 hours, 1 agent session.

**G3-2. M_R two-zero texture classification against {A₁,A₂,B₃,B₄,B₆}** *(both reports, CONVERGENT; DISAGREE on phase reading)*
- **What**: Build the M₃(ℂ)-derived M_R, reduce to texture-zero form, classify against paper-08 (Ma/Xu/Zhao) Eq.8 five-class survivor set. Cross-constrains: near-floor Σm_ν=0.0582 ⇒ A-class-compatible; an eventual detection at 0.098 ⇒ B-class-compatible.
- **Inputs**: M₃(ℂ) factor of A_K; s99 seesaw M_R=D_K fold-energy matrix; paper-08 Eq.8; substrate δ_CP ∈ {0,π} (S99 gate); NuFIT mixing angles (PIN vintage — both flag dm2_21 drift, §III.E).
- **Gate**: `S100-MR-TEXTURE-CLASS`. PASS: matches exactly one survivor class AND δ_CP∈{0,π} consistent; INFO: matches a class but δ_CP conflicts (disfavoring B-class); FAIL: no match in {A₁,A₂,B₃,B₄,B₆}.
- **Effort**: 3–4 hours, 1 agent session.
- **PAIRED-REPORT DISAGREEMENT (flag, do not average)**: dirac (G3) — the index's "B-class Majorana phases ~π/2 match the framework's φ_CP=π/2" is a **SECTOR CONFLATION**: the framework's π/2 is the K_7 transit phase (baryogenesis), the S99 PMNS phases are {0,π}; this DISFAVORS the B-class and points to A-class. neutrino (G3) — flags the same tension more mildly ("a B-class match predicts lightest m≈0.1 eV → Σm_ν near upper NO edge, NOT both achievable with the 0.0582 floor") but still emphasizes the π/2 resonance as "striking corroboration." **Consolidated reading**: dirac's sector-conflation correction is the sharper structural claim; the classification gate MUST run with δ_CP∈{0,π}, which immediately disfavors B-class predictions (δ~1.5π). The π/2 resonance is a consistency check on the SEPARATE K_7 baryogenesis sector (already CLOSED-SOURCED-UNIQUE), not a leptonic-phase match.

**G3-3. m_ββ prediction for the queued S100-D5-0NUBB-MAJORANA gate** *(both reports, CONVERGENT)*
- **What**: Compute m_ββ = |U_e2² m_2 e^{iα_2} + U_e3² m_3 e^{iα_3}| with m_1=0 EXACT (Rank-1 Yukawa S62), substrate m_2=0.0086776, m_3=0.0495278 eV, PMNS from NuFit-6.0, Majorana phases constrained to {0,π} (from δ_CP∈{0,π}). Yields a DISCRETE finite set (near-zero-free in phases), in the NO-floor ~1–4 meV band — distinct from the index's B-class tens-of-meV expectation.
- **Inputs**: m_nu=[0,0.0086776,0.0495278] eV (S99 npz); sin²θ13, sin²θ12 (NuFit-6.0: 0.02225, ~0.303); δ_CP∈{0,π}; m_1=0 PROVEN; `S96-MATTER-0NUBB` INFO (Majorana KO-dim-6 Pfaffian, structural confirmation).
- **Gate**: `S100-D5-0NUBB-MAJORANA` (already queued, register-sourced). PASS: m_ββ_FW below LEGEND-200 AND within LEGEND-1000/nEXO reach; INFO: below all current+next-gen reach; FAIL: m_ββ already excluded by LEGEND-200.
- **Effort**: 2–3 hours, 1 agent session.

*(G3 superseded narrative — BOTH reports CONVERGENT and decisive: the leptogenesis "1.1 OOM gap" framing of index papers 07/08/11 is SUPERSEDED by `S98-W3-2-BARYOGEN-UNIQUENESS` PASS — baryogenesis is CLOSED-SOURCED-UNIQUE (η_B=4.517492e-11, φ_CP=π/2 FORCED, φ88 unique CP source). The enhancement-menu papers are central-value-refinement candidates DOWNSTREAM of a PASS, NOT gap-closers. Do NOT carry "close the gap" forward. Lower-EVOI G3 angles: N_eff cold-population reconciliation vs canonical BBN-N_eff; η_B magnitude audit (INFO-only, internal-to-unique-source); hygiene: phi_CP sector-disambiguation (0.0→split internal/K_7), NuFit-vintage re-pin. §V.)*

### G4 — NCG / Spectral-Action (connes + lizzi)

**G4-1. Sym³(3) cubic-ladder test on D_K bottom-3 generation eigenvalues** *(both reports, CONVERGENT; corroborates §VII.BL)*
- **What**: Feed the triality-distinct tower (1,0)/(1,1)/(3,0) [C₂=(4/3,3,6)] bottom-3 generation eigenvalues through a Sym³(3) cubic ladder (paper-02 exceptional-Jordan mechanism), fit the hierarchy exponent p, and map ε_LX onto the paper's fitted exponent + octonionic phase.
- **Inputs**: D_K L_max=12 cache (s84_spectrum_cache_L12_tau019.npz); M_KK, τ_fold; PDG charged-lepton masses; §VII.BL Generation-Blindness Obstruction (STAGE-3-PERMANENT, promoted S99 W3-1) + W2 Homogeneity wall (proven_231).
- **Gate**: `S100-SYM3-CUBIC-LADDER-P-EXPONENT`. PASS: p∈[0.8,1.2] (matching paper-02 p≃1) AND maps ε_LX onto the fitted exponent+phase, residual no worse than the panel 9/5=1.800 widening candidate; INFO: p out-of-band but ladder present; FAIL: no ladder structure.
- **Effort**: 3–4 hours, 1 agent session.
- **Convergent finding**: paper 02 is independent external corroboration of §VII.BL ε_LX-necessity (a DIFFERENT algebra, the same FITTED-exponent wall — NOT shared-context per epistemic-discipline). This is the G4 cross-link to the rank-9b fermion-mass texture cluster (§III.D).

**G4-2. Pati-Salam A/B/C variant identification for the rescued order-one** *(both reports, CONVERGENT; both CORRECT the index)*
- **What**: Map the framework's order-one defect (4.000 bare → 2.100 after inner fluctuations, order_one_closes=False, KO_dim=2 from S93-W6-1) onto the Aydemir/CCS PS variants A/B/C; extract sin²θ_W + S₁(3̄,1,1/3) leptoquark content.
- **Inputs**: S93-W6-1 gate (defect trajectory 4.000→2.100); paper 05 (Aydemir) variant taxonomy; CCS-2013 inner-fluctuations-without-first-order; A_F^PS=ℍ_R⊕ℍ_L⊕M_4(ℂ); PS-W3-I sin² channel; §VII.BE FWD-C4 SU(4)_PS s=6 Mellin anchor (Tier-1 PASS).
- **Gate**: `S100-PS-VARIANT-ID` (= lizzi `S100-NCG-PS-VARIANT-ID`). PASS: unique variant + sin²θ_W consistent with PS-W3-I; INFO: variant identified but sin² is a new prediction; FAIL: defect matches no A/B/C variant.
- **Effort**: 3–5 hours, 1 agent session.
- **Index correction (both reports)**: the index's "broken order-one at 4.000" is RESCUED STAGE-3-PERMANENT (Wedderburn-Frobenius, §VII.W-3, Q10) — the conversion is RESCUED-axiom → positive-PS-variant, NOT broken-axiom. A positive ID opportunity, not a flaw.

**G4-3. Geodesic-flow ergodicity / vacuum-uniqueness test of D_K (Ordered-Veil spectral-triple test)** *(both reports, CONVERGENT; HIGHEST-leverage truncation-channel item per both)*
- **What**: Apply paper-04 (Hekkelman-McDonald) ergodicity criterion (= uniqueness of the vacuum state for the C*-dynamical system) to D_K on Jensen-deformed SU(3). A NON-unique vacuum (failure of quantum ergodicity) is the spectral-triple-level statement of Ordered-Veil integrability.
- **Inputs**: D_K spectrum + Peter-Weyl decomposition at τ_fold; M_KK=7.4287e16; paper-04 NC-integral approximation + ergodicity criterion (arXiv 2412.00628); Ordered-Veil paradigm.
- **Gate**: `S100-DK-ERGODICITY` (= connes `S100-QUANTUM-ERGODICITY-VACUUM-UNIQUENESS`). PASS (Ordered-Veil corroborated at spectral-triple level): D_K geodesic flow NON-ergodic (n_vacuum>1); FAIL (tension): uniquely ergodic; INFO: local Weyl law inapplicable on the finite truncation.
- **Effort**: 6–8 hours, 1–2 agent sessions.
- **CROSS-GROUP TENSION (see §III.C)**: this gate tests the Ordered-Veil INTEGRABILITY claim, which is canonically distinct from the Ordered-Veil PERMANENCE claim (RETRACTED S39 per G6). The "transit IS the physics" / integrable-at-fabric-scale survives; "GGE never thermalizes" does not. The ergodicity test must be scoped to the fabric-scale integrability (CG(24) Poisson ⟨r⟩=0.367), NOT the retracted single-cell permanence.

*(G4 lower-EVOI math-rigor cluster (BOTH reports): Spectral-Fejér α derivation (first-principles α=3 for §VII.AF.1 Level-2 envelope, currently FB-certified); δ-gapped spectral-localizer index pairing on the BdG triple at δ=Δ_BCS=0.4642547; Yu-Ma tensor⊗quaternion homogeneity-wall compatibility (must RESPECT §VII.BL — admissible ONLY if the extension IS ε_LX); cyclic-cocycle convergence (paper 09); Carathéodory-Fejér zero-localization on §VII.AJ; f-decay-order admissibility class (paper 10, Q28 sharpening); zeta-Majorana CC route (paper 06, orthogonal to the failed zeta-tilt axis). §V.)*

### G5 — Spectral Geometry / Heat Kernels / Zeta-Mellin Poles (spectral-geometer + baptista)

**G5-1. CF28 simple-vs-log pole classification at s∈{5,6,7}** *(both reports, CONVERGENT; the decisive G5 angle)*
- **What**: For each candidate substrate-distance pole s∈{5,6,7}, test whether the heat trace Tr(e^{−σ D_K²}) acquires a `t^{n/2} log t` term at the matching order (Connes paper-10 mechanism = non-simple pole; Fucci-Stanfill paper-06 = boundary-data trigger). A log term ⇔ non-simple pole ⇔ residue is a log-coefficient, not a clean SDW moment (Class-8.7 degenerate-observable).
- **Inputs**: s84_spectrum_cache_L12_tau019.npz; C₂(p,q) Casimir; τ_fold=0.19; CM-1995 §III.4 residue formula; canonical S_d={0,2,4,6,8}; PRU Class-8.7 degeneracy-witness machinery; regulator tag MANDATORY (a_n^{Mellin}/a_n^{ζ}).
- **Gate**: `S100-CF28-SIMPLE-POLE-PREFLIGHT`. PASS: no log term at s∈{5,6,7} (poles simple, s=7 Pillar-VII registration eligible); FAIL: log term present (non-simple pole, registration BLOCKED with remediation); INFO: s=7 shell-sum non-convergent (off-pole-Hankel contour deferred).
- **Effort**: 3–4 hours, 1 agent session.
- **Scope correction (both reports)**: s=5/s=6 are ALREADY convergent (SU(4)_PS s>9/2; residue_s6_PS_Linf=0.0009393639575775 canonical S95) and carry F_2-class anti-correlation PASSes (S88 §W12-148, |ρ_S+1|=0.0 EXACT); §VII.BB already lands at s=5. The genuinely-open item is **s=7** + the pole-ORDER (simple-vs-log) question (distinct from convergence) at the higher poles.

**G5-2. Lai-Teh τ=0 bi-invariant reduction regression test** *(both reports, CONVERGENT; mandatory unit test)*
- **What**: Verify the Jensen-deformed D_K eigensolver reduces at τ=0 to the Lai-Teh cubic-point spectrum: λ(p,q)=p²+q²+pq, multiplicity 2p²q²(p+q)², AND the 4-term Λ⁸/Λ⁶/Λ⁴/Λ² polynomial with the (3t−1)(3t−2) torsion-twist vanishing at t=1/3. No registered reduction test currently exists — closes that gap.
- **Inputs**: `dirac_spectrum.get_irrep(p,q)`; Lai-Teh Thm 2.2 closed form (paper 01); Weyl dim ½(p+1)(q+1)(p+q+2); canonical τ=0 anchor R_{(30,0)}=12.05; D_F(τ=0)=0 exact.
- **Gate**: `S100-TAU0-LAITEH-REDUCTION`. PASS: (λ,mult) + 4-term polynomial match Lai-Teh to machine ε at τ=0; FAIL: mismatch (eigensolver/normalization bug — must fix before trusting any τ>0 output).
- **Effort**: 2 hours, 1 agent session.

**G5-3. Symmetry-resolved kNN spacing — Ordered-Veil integrability falsifier inside (p,q) sectors** *(both reports, CONVERGENT)*
- **What**: Compute symmetry-unfolded NN AND kNN (k=1,2,3) level-spacing distributions of the bottom-N D_K eigenvalues INSIDE fixed Peter-Weyl (p,q) sectors (removing the Weyl degeneracy that makes the current ⟨r⟩=0.321 sub-Poisson), test against Berry-Tabor Poisson vs the corrected Wigner-kNN surmise (paper 08).
- **Inputs**: s84_spectrum_cache_L12_tau019.npz; (p,q)-sector labels; corrected kNN surmise variance (extract from arXiv 2504.20134); CHAOS-1 baseline (⟨r⟩=0.321, r_pooled=0.422); AZ class BDI.
- **Gate**: `S100-KNN-ORDERED-VEIL` (extends CHAOS-1). PASS (confirms integrability): Poisson/super-Poisson at all k inside resolved sectors; FAIL (falsifies non-thermalization): level repulsion at any k; INFO: residual super-Poisson attributable to accidental degeneracy.
- **Effort**: 3–4 hours, 1 agent session.
- **CROSS-GROUP link (§III.C)**: this is the same Ordered-Veil falsifier-protocol object G4-3 (ergodicity) and G6 (GGE thermalization) bear on — the three-group Ordered-Veil stack. Scoped to fabric-scale integrability post-S39-retraction.

*(G5 lower-EVOI: Savale continuum-floor cross-check (rank-2 Weyl remainder 8/7 — **flag: index "rank-4=6/5" is WRONG, exact is 16/13**, both reports Sage-confirm); SU(3) spectral-rigidity vs isospectral-non-isometric (reconstruction boundary); non-minimal â₂ for TT/vector sectors (low-leverage, canonical δa_4/a_4=−3.4e−4); Berger-sphere second-order asymmetry benchmark for η=0. §V.)*

### G6 — Non-equilibrium Transit (transit + kitaev)

**G6-1. Ordered-Veil capstone/registry reconciliation to canonical transit-window status** *(both reports, CONVERGENT; LOAD-BEARING CONFLICT — see §III.C)*
- **What**: Reconcile the "GGE never thermalizes" narration (capstone §7 falsifier surface, index framing, agent memory) DOWN to the canonical S39 status: GGE valid DURING transit, thermalizes ~6 M_KK⁻¹ after via the 13% non-separable density-density channel; survives as Poisson integrability ONLY at the fabric scale (CG(24) ⟨r⟩=0.367). Corrected falsifier: discriminator is GGE-as-prethermal-plateau DURING transit (anti-diagonal Langen tomography), NOT eternal non-thermalization.
- **Inputs**: atlas-04 T3 (BROKEN); atlas-07 (RETRACTED-S39); INTEG-39 (DECISIVE FAIL, Brody β=0.633, t_therm≈6 M_KK⁻¹); session-62-hawking-qa (density-density mechanism); capstone-hygiene-gate Q3 routing.
- **Gate**: capstone-hygiene Q3 (PROSE tag == register tag); housekeeping §A (in-session designated-writer fix) — NOT a compute gate. PASS: capstone/inventory/memory narrate the Veil at BROKEN/transit-window status, no surface above register status.
- **Effort**: 1–2 hours, 1 agent session (orchestrator-direct prose patch + mack for §7 table cell).
- **Routing**: §7 falsifier surface = mack-cosmic-bridge sole-writer; §-prose = gen-physicist designated writer (capstone-hygiene-gate.md Q3/Q4).

**G6-2. Box+delta transfer-matrix re-attempt of |β_k|² at k_pivot (sudden-limit discretization)** *(both reports, CONVERGENT)*
- **What**: Re-run the Bogoliubov |β_k|² extraction discretizing the fold a(τ) as a BOX potential (height from V(η)=(1/4)ȧ²+(1/2)ä·a, Sparn Eq.4) with TWO delta-peaks at the switch-on/off boundaries — NOT a smooth interpolated cusp. Compare |β_2|²(k_pivot) against the sub-horizon `sin²[μ_k Δη]` formula (Schmidt Eq.75). Re-opens `S85-W7-CUSP-BOGOLIUBOV` (FAIL).
- **Inputs**: s77_mode_threshold.npz (k_pivot=14.310, k/aH=14.70, x_pivot=11.075); s64 fold a(τ) profile; dt_transit=1.1302e-3; Sparn/Schmidt closed forms; B2-ladder |β_2|²≈1.7e3 (S79).
- **Gate**: `S100-BOX-DELTA-BOGOLIUBOV`. PASS: |β_pivot|² N_seg-stable (var<2× across N_seg∈{50,100,200,400}) AND matches sin²[μ_k Δη] within 10%; FAIL: OOM-sensitive to N_seg (confirms smooth-cusp pathology); INFO: stable but off the closed form.
- **Effort**: 4–6 hours, 1 agent session.
- **Convergent correction (both reports)**: the standing `S85-W7-CUSP-BOGOLIUBOV` FAIL is NOT vindicated by Sparn — it FAILed because the fold was treated as a smooth cusp; transfer-matrix is EXACT for box+delta sharp boundaries (the fold's genuine geometry). A concrete re-attempt recipe, not a claim it already passes.

**G6-3. Fast-quench universality class of the fold: Rao range-scaling vs Li KZ-survival** *(both reports, CONVERGENT — both place the fold in Rao's class)*
- **What**: Test that the fold's P_exc=1.000 / 59.8-pair saturation is fold-RANGE-controlled (Rao v>v_c, ρ~δ_max, rate-independent), NOT rate-controlled (Li KZ-survival). Compute n_pairs/P_exc as functions of (i) transit rate and (ii) fold range; verify rate-independent saturation + range-scaling.
- **Inputs**: dS/dτ=+58,673 (fold gradient); n_pairs=59.8; P_exc_kz=1.0; τ_fold=0.19, Mach=13.75; Rao (08) ρ~δ_max; Li (13) z'<z+1/ν.
- **Gate**: `S100-FOLD-RANGE-SCALING` (= kitaev `S100-FOLD-RANGE-SCALING`). PASS: P_exc rate-independent (Δ<1% across Mach∈[5,30]) AND n_pairs scales with range (Rao class confirmed); FAIL: rate-dependent (would place fold in slow-quench KZ class, contradicting saturation).
- **Effort**: 3–5 hours, 1 agent session.

*(G6 lower-EVOI: ΔN_eff/BBN bound on substrate-scale blue tilt n_T=+0.468 (both flag index drift: canonical n_T=+0.468 transit / −1.5e-3 pivot, scale-and-channel-tagged; substrate blue tilt INACCESSIBLE at CMB per S84 PASS EVOI=0); ζ-tail Gaussianity cross-check vs Ahmadi; Langen GGE tomography (which-scale discriminator); Stahl small-scale matter-power + sign-keyed HMF (addresses K_pivot gap atlas-04 C2); F_amp energy-conserving validation; Xue non-log-periodicity discriminator; two-process thermalization reconciliation (kitaev: prethermalization ≠ interaction-thermalization, registry wins over agent memory). §V.)*

### G7 — Flat-Band Quantum Geometry / Multiband BdG (landau + berry)

**G7-1. §VII.AF.1 registry-slot label reconciliation (R_geom is §VII.AF.1, NOT §VII.W)** *(both reports, CONVERGENT; CANONICAL CORRECTION)*
- **What**: Registry-hygiene (NOT a computation). Confirm the Peotta-Törmä R_geom = ∫_BZ Tr g_ab^(P0) bridge is §VII.AF.1.OP-PROJ (substrate-IS Pillar III HP¹, laboratory-IN Pillar IV Peotta-Törmä, HKR bridge); §VII.W is the HP parity-grading orthogonality theorem. Flag the index-legend conflation so downstream sweeps inherit the correct slot.
- **Inputs**: atlas-07 (§VII.W, §VII.AF.1 rows); permanent-results-registry (W-5 §VII.AF.1 instance #1 anchor); s86-hp1-cohomology-quantum-metric-bridge.md (eps_H_HP1_norm=16.197719); registry-landing.md §"Operator-Projection naming hygiene".
- **Gate**: feeds the mack-cosmic-bridge registry-hygiene queue. INFO if registry already carries correct labels (likely); deliverable = index-legend caveat note. **Anchored**: knowledge MCP confirms §VII.AF.1 = the s86-hp1 R_geom bridge.
- **Effort**: 0.5–1 hour, 1 agent session (mack-cosmic-bridge or orchestrator-direct).

**G7-2. §VII.AF.1 BdG-projector + non-Abelian-trace structural confirmation** *(both reports, CONVERGENT)*
- **What**: Two paired sub-checks the literature now independently demands. (a) Confirm the R_geom integrand uses the BdG/quasihole-state projector P_0, not a normal-state band projector (Porlles-Chen paper 03). (b) Compute the non-Abelian Tr[R_μν] over the degenerate Peter-Weyl sectors and verify Tr R ≠ Σ(per-band Abelian QM) — the algebra-correct object for A_K=ℂ⊕ℍ⊕M₃(ℂ) (Chen-Karki-Hosur paper 06; 20%/50% measured fractions).
- **Inputs**: P_0(τ_fold) from s86-hp1; s84_spectrum_cache filtered to L_max=10; eps_H_HP1_norm=16.197719; non-Abelian Wilczek-Zee FHS link machinery (S96 off-Jensen Chern, single-band link gives gauge-noise C~0.78 as negative control); Level-3 anchor 0.0095% F₄, Level-2 envelope L^{-3}=0.10% (r=0.0950).
- **Gate**: `S100-VII-W-BDG-PROJECTOR-CONFIRM` + `S100-NONABELIAN-METRIC-FRACTION`. (a) PASS: BdG integrand reproduces the 0.0095% F₄ anchor AND normal-state does NOT (choice load-bearing); INFO: choice numerically immaterial at L_max=10. (b) PASS: f_nonAb>0 (inter-band term structurally present) AND imaginary part integrates to Chern=0 (<1e-12, re-confirms metric-not-curvature); FAIL: f_nonAb=0 (reduces to Abelian).
- **Effort**: 3–4 + 4–6 hours, 1–2 agent sessions.
- **Berry geometric correction (load-bearing)**: the bridge object is the quantum METRIC (Re QGT), NOT Berry curvature — the framework's Berry curvature vanishes identically on SU(3) (Im(QGT)=0, max|Ω|<4e-14, 12 zero invariants, g=982.5 reservoir). The framework lives in EXACTLY the Chen-Karki-Hosur regime: metrically rich, topologically trivial (Tr R≠0 while Chern=0).

**G7-3. MgB₂ Leggett-damping → χ-inherited DM lifetime bound (corrected form)** *(both reports, CONVERGENT; both flag the index τ_DM figure as UNCANONICAL)*
- **What**: Extract the MgB₂ Leggett-mode frequency-to-gap ratio and damping (paper 02, marked [INCOMPLETE]; pull from PDF arXiv 2412.13830), propagate the universality class through the χ inheritance morphism to bound the substrate DM inter-band-coherence decay channel. Express as the CONDITIONAL ratio τ_DM/t_univ (canonical 1.13e65, Γ_grav<H_0).
- **Inputs**: paper-02 PDF (extract Leggett ω/Δ and Γ_Leggett); `Mass_LeggettDM_over_Delta_BCS=11.97` (CONDITIONAL Γ_grav<H_0); LEGGETT-GRAV-DECAY-73a (τ_DM/t_univ=1.13e65); Δ_BCS=0.4642547; χ projection (M₃(ℂ)→0).
- **Gate**: `S100-LEGGETT-DAMPING-INHERITANCE`. PASS: χ-inherited bound consistent with Γ_grav<H_0 (DM relic survives); FAIL: lab Leggett damping implies inter-band-coherence decay faster than H_0 under inheritance.
- **Effort**: 4–5 hours, 1 agent session.
- **CANONICAL CORRECTION (both reports)**: the index's "τ_DM=4.93e82 s" absolute figure is UNCANONICAL; the canonical survival condition is the qualitative inequality Γ_grav<H_0, with the survival-margin RATIO 1.13e65. Do NOT propagate the absolute-seconds figure.

*(G7 lower-EVOI: Hou ±l CdGM → MCT-3 7.324992 cohomology-asymmetry read-out protocol (mack-bridge inventory annotation; Friedel-vs-cohomology guard); thermal node-resolved D^geom(T) vs Hirobe; MATBG-T²/MATTG-T-linear node-discriminant (Element-5 dual-platform note, mack); AV₃Sb₅ vHs-driven flat-band as τ_fold transit analog (mechanism not velocity); Penttilä flat-band-ratio vs flat-vs-dispersive hierarchy; hygiene: "37×" B1-dominance multiplier canonical-pin verification (both flag canonical squeeze=54.06×; 37× not pinned — landau cautious, berry asserts RECONCILED-69). §V.)*

### G8 — JWST Little Red Dots (little-red-dots + mack)

**Governing fact (BOTH reports, CONVERGENT — anchored canonical)**: `LRD_demographics_not_discriminating` STAGING — LRD/structure demographics cannot discriminate the framework from ΛCDM at z<10²⁸. Every paper observes at z≈3–16 (~28 OOM below the wall). Therefore papers 01–05,07–10 are **consistency CEILINGS, not discriminators**. The lone physics-level discriminator (escapes the wall) is the seeding fork (paper 06).

**G8-1. SMDS dark-star NON-channel forward falsifier row (seeding fork, the ONE physics-level discriminator)** *(both reports, CONVERGENT)*
- **What**: Register the annihilating-DM Supermassive-Dark-Star channel as CLOSED-to-framework in falsifier-master-inventory.md: substrate predicts NO SMDS-powered seeds (Leggett-channel DM cannot annihilate); falsifier = confirmed DM-annihilation SMDS LRD progenitor with the cool/extended spectral signature; corroborator = SMDS-null + gas-dynamical (DCBH) seeding.
- **Inputs**: `Mass_LeggettDM_over_Delta_BCS=11.97` (LEGGETT-MOMENT-70 PROVEN); baseline Annihilation=0 PASS; `LRD_demographics_not_discriminating` (to scope this as the ONE LRD channel that ESCAPES the z<10²⁸ wall); Ilie ⟨Γ₁⟩_P/Γ_crit≈4/3+C·GM/(Rc²); paper-06 SMDS signature (100 GeV WIMP, MESA).
- **Gate**: `S100-SMDS-DARK-STAR-FORK`. INFO on landing; PASS-criterion-for-future = SMDS spectral signature in a confirmed progenitor ⇒ non-annihilating-DM CHALLENGED; null ⇒ corroborated. Row MUST declare PHYSICS-level (NOT subject to the demographics wall).
- **Effort**: 2–3 hours, 1 agent session (mack-cosmic-bridge sole-writer; registry write, not numerical gate).

**G8-2. a₂-channel heavy-seed collapse vs DCBH atomic-cooling-halo benchmark** *(both reports, CONVERGENT — OPEN side of the fork)*
- **What**: Compute whether GGE acoustic interference self-organizing through the a₂ channel yields a compact relay-pattern attractor of M_seed~10⁵ M⊙ under gas-dynamical collapse with NO DM-annihilation power source, at the DCBH number density Pacucci requires (puzzle e).
- **Inputs**: a_2_FW_zeta=2776.165389; a₀ vacuum moment (2776/6440 ratio); kappa_2_substrate_FW=0.0210181; emergent Friedmann H²=(8πG/3)ρ_eff (a₂-channel); Pacucci DCBH (M_g~10⁷ M⊙ atomic-cooling halos, n>10⁷⁻⁸ cm⁻³); L_bol<3e43 erg/s ceiling (paper 01) as X-ray-self-screening check; PANORAMIC/Whitler abundance anchors.
- **Gate**: `S100-A2-HEAVY-SEED-ABUNDANCE` (= LRD-analyst `A2-DCBH-SEED-BENCHMARK`). PASS: a₂-collapse produces M_seed~10⁵ M⊙ at the DCBH host abundance within 0.5 dex, NO annihilation term; FAIL: requires an energy source beyond the a₂ moment; INFO: produces a seed at an abundance/redshift the substrate cannot independently source. Folds through the selection function (G8-3).
- **Effort**: 6–9 hours, 2 agent sessions.

**G8-3. Selection-function discipline wrapper + two-axis structure-timing joint constraint** *(both reports, CONVERGENT; methodology gate)*
- **What**: (a) Build the substrate-side S_i(z) folding wrapper so every abundance/clustering/UVLF prediction is compared to data ONLY after convolution through a stated selection function (Rinaldi ≲25% color-cut capture floor). (b) Pre-register the two-axis joint constraint: a substrate assembly prediction must hit BOTH axes simultaneously — (07) ≳1 dex quiescent abundance (decisive) AND σ_CV≈0.7±0.3 clustering (MILD, spot-verified "low significance"); (09) both-ends UV excess AND steep α=−2.36 to −2.60.
- **Inputs**: Rinaldi S_i(z) (arXiv 2604.07138, ≲25% capture); PDF-verified PANORAMIC σ_CV=0.7±0.3 (arXiv 2604.05022); PDF-verified Whitler α=−2.36..−2.60, ρ_UV=2.82e25 at z~10, φ* decline ~2.1–2.3 z~10→13 (arXiv 2501.00984); prior CLUST-43 (s43_lrd_clustering).
- **Gate**: `S100-SELECTION-FUNCTION-FLOOR` + `S100-STRUCTURE-TIMING-TWO-AXIS`. Methodology/INFO: produces the selection-folded comparison band; the two-axis gate's EXPECTED verdict is INFO (degenerate-with-ΛCDM-below-z=10²⁸) — a CONSISTENCY ceiling, NOT a discriminator. The gate block MUST say so to prevent over-claiming.
- **Effort**: 4–5 + 3–4 hours, 1–2 agent sessions.
- **Spot-verification correction (both reports)**: the clustering axis (paper 07) is "MILD tension / low significance" (σ_CV 0.7±0.3 error bar overlaps mock 0.43–0.51) — the index overstated it as a "decisive second fingerprint." The abundance axis carries the weight.

*(G8 lower-EVOI: QSO1 dynamical-mass joint constraint with the Chandra ceiling (emission-envelope-vs-point-mass internal constraint — papers 01+02 joint); TWINKLE non-variability substrate emission-mechanism gate; reionization budget ceiling (Γ_HI window, two-sided, LRDs-as-Type-I-subset η≈0.10); bright-end LF cutoff single-channel-scale check; high-z UVLF both-ends. ALL consistency ceilings under the wall. §V.)*

---

## III. Cross-Group Tension Table

The Focus's minimum set, plus the consolidation's own surfaced tensions. "Tension" here = a place where two groups (or two paired reports) pull on the same structural object, and the joint reading is signal.

| # | Tension | Groups | Substrate object | Consolidated reading |
|:--|:--------|:-------|:-----------------|:---------------------|
| **A** | ΔN_eff budget vs q-theory time-profiles | R3 (×3) + G1 + G2 | a₀ tracking-vacuum ρ_vac(a) across radiation era | The C10/BBN residual collapses to ONE compute (`CF-S100-W2-1-QEQ-DRIVE` dual-output) → `S100-X-C10-RHOVAC-EPOCH-PROFILE`. Magnitude corridor CLOSED; time-profile corridor OPEN, strictly DOWNSTREAM of the q_eq(H) drive. Canonical 2.0873 fails the canonical bound 0.227 by 2.09×, the external 0.107 by 19.51×. See §III.A. |
| **B** | n_eff-direction conflict (S66 vs S98/S99) | R3 (volovik+einstein ONLY) | tracking exponent n_eff sign in the lever vs G_eff routes | UNRESOLVED CANONICAL conflict, surfaced by 2 of 3 R3 agents, NOT by mack(R3). S66 G_eff-route: n_eff=2.3 PASS (2% G_eff bound); S98/S99 lever-route: n_eff<2 FAIL; the two point OPPOSITE in the lever form. Prerequisite for any relief gate → `S100-X-C10-BBN-CONSTRAINT-RECONCILE`. See §III.A. |
| **C** | Ordered-Veil falsifier protocol stack | G4 + G5 + G6 | GGE relic integrability / non-thermalization | THREE groups bear on ONE object via THREE tests: G4-3 (D_K ergodicity / vacuum-uniqueness), G5-3 (symmetry-resolved kNN spacing), G6 (GGE thermalization). **Decisive cross-group correction**: "GGE NEVER thermalizes" = BROKEN/RETRACTED-S39 (atlas-04 T3, anchored). What survives: "transit IS the physics" + fabric-scale integrability (CG(24) Poisson ⟨r⟩=0.367). G4/G5 narrate the Ordered Veil as a live PERMANENCE falsifier; G6 corrects to transit-window. All three gates MUST scope to fabric-scale integrability, NOT retracted single-cell permanence. See §III.C. |
| **D** | ε_LX cluster vs Jordan-ladder fitted-exponent | G4 (×2) ↔ rank-9b register | inter-generation Yukawa spread on the multiplicity index | CONVERGENT, not adversarial: paper-02 exceptional-Jordan FITTED p≃1 is independent external corroboration of §VII.BL ε_LX-necessity (STAGE-3-PERMANENT). The S99 fermion-mass panel rank-9b cluster (`S100-DUAL-Z3-PHI-POINTS`→`-YUKAWA-OVERLAP-OFFDIAG`→`-CASIMIR-WIDENING`) is the framework's own attack; G4-1 (`S100-SYM3-CUBIC-LADDER`) maps ε_LX onto the Jordan fitted exponent + octonionic phase. Both say the spread is NOT A_K-buildable. See §III.D. |
| **E** | §VII.W bridge sharpenings | G7 (×2) | R_geom HP¹ quantum-metric cross-pillar bridge | Index conflates the R_geom bridge with §VII.W; canonical is §VII.AF.1.OP-PROJ (anchored: s86-hp1 session). Three independent 2024–26 results (Porlles-Chen BdG-projector, Chen-Karki-Hosur non-Abelian trace, Tanaka+Banerjee dual-platform) confirm the EXACT algebraic spec of R_geom. Berry: object is the METRIC not curvature (Im QGT=0 on SU(3)). G7-1 (slot relabel) + G7-2 (projector/trace confirm). See §III.E. |
| **F** | Seeding-fork DM-annihilation discriminator vs framework DM properties | G8 (×2) | Leggett-channel GGE DM (non-annihilating) | The SMDS dark-star channel (paper 06) REQUIRES annihilating 100 GeV WIMP DM → structurally CLOSED to the framework's PROVEN non-annihilating Leggett DM (LEGGETT-MOMENT-70). The ONLY G8 channel that escapes the z<10²⁸ demographics wall (tests the DM INTERACTION property, not the assembly count). Gas-dynamical DCBH (paper 10) is framework-COMPATIBLE. → `S100-SMDS-DARK-STAR-FORK` (new physics-level falsifier row). See §III.F. |

### §III.A — Tension A in detail (the keystone)

All seven C10-touching reports agree on the structure; the precision differs. The substitution chain (einstein R3, Sage-verified to 0.000e+00 residual):

```
Step 1 (Definition): (ρ_vac/ρ_rad)_BBN = frac_base · exp((n_eff − 2)·X)   [radiation era H∝a^−2, tracking law H^{n_eff}]
Step 2: frac_base = 1.144730 ; X = ln(H_BBN/H_0) = 40.2756 ; n_eff = 1.978111 (HARD from-below, S98 V.9, divergence_type=A)
Step 3: relief_factor = exp((1.978111 − 2)·40.2756) = exp(−0.021889·40.2756) = 0.414123
Step 4: (ρ_vac/ρ_rad)_BBN = 1.144730 · 0.414123 = 0.474049 ;  ΔN_eff = 0.474049/0.227113 = 2.0873   [the S98 FAIL]
Step 5 (sign read-off): n_eff < 2 ⇒ (n_eff−2) < 0 ⇒ a-exponent on ρ_vac/ρ_rad is 2(2−n_eff) = +0.0438 > 0
        ⇒ fraction GROWS toward late times / SHRINKS toward early times ("from-below relief" direction)
Conclusion: the canonical tracking vacuum is RADIATION-LIKE (near-flat fraction, +0.0438 a-exponent).
            EDE-like relief REQUIRES the OPPOSITE sign (ρ_vac ∝ a^{−n}, n>4 ⇒ negative a-exponent).
            EDE-like is therefore a DEPARTURE from the tracking law, not a tuning of n_eff near 2.
```

The exponent-sensitivity (einstein): ∂ ln(ρ_vac/ρ_rad)_BBN/∂n_eff = X = 40.2756 — a 0.01 change in n_eff moves the BBN fraction by e^{0.40}≈1.5. Reaching ΔN_eff≤1 (canonical bound) needs n_eff=1.95984 (1.835× the substrate shift); reaching 0.107 (external) needs n_eff=1.904349 (4.37× the substrate shift). **The magnitude axis is exhausted** (S99-W2-BBN-RELIEF closed all three mechanisms); the only surviving relief is the time-profile axis, reachable only by abandoning n_eff≈2 — which is what `CF-S100-W2-1-QEQ-DRIVE` decides. A BBN-arm gate is NOT independent of it; it is a read-out clause that cannot run until q_eq(H) is known.

### §III.B — Tension B in detail (the n_eff-direction conflict, surfaced by 2/3)

volovik(R3) and einstein(R3) flag a conflict INTERNAL to the framework's canonical sessions (mack R3 does not): in the **lever form** `exp((n_eff−2)·X)` with X>0, the from-ABOVE direction (n_eff>2) makes the BBN fraction LARGER (worse); the from-BELOW (n_eff<2) makes it smaller (better). But the canonical S66 mack-transit-workshop passed n_eff=2.3 via a 2% G_eff(BBN)=1.03G bound (a DIFFERENT observable). These cannot both be the operative BBN falsifier with the same sign convention. **Consolidated routing**: this is a genuine math/physics adjudication (Q1-YES per Investigating-Workshops), NOT a hygiene re-tag — it is a prerequisite for any relief gate. Route as `S100-X-C10-BBN-CONSTRAINT-RECONCILE` [VERIFY] + registry: determine which BBN constraint (2% G_eff bound vs ΔN_eff lever) is the operative falsifier on the tracking vacuum, and which n_eff direction relieves it, with a Sage-exact substitution chain. The disagreement among R3 agents about WHETHER this is a conflict is itself signal — mack treated 0.107 as the headline and did not surface the upstream G_eff-vs-lever tension. I do not average: I carry the volovik/einstein flag as the live item because it is structurally concrete (two canonical sessions, opposite n_eff direction).

### §III.C — Tension C in detail (Ordered-Veil stack across G4/G5/G6)

This is the cross-group tension the Focus names, and it carries a load-bearing CANONICAL correction surfaced ONLY by G6:

- **G4 (connes+lizzi)**: paper-04 ergodicity = vacuum-uniqueness is "the highest-leverage truncation-channel angle" — a NON-ergodic D_K confirms Ordered-Veil INTEGRABILITY. Both narrate the Ordered Veil as a live PROVEN paradigm.
- **G5 (spectral-geometer+baptista)**: the corrected kNN surmise sharpens the integrability falsifier; the current ⟨r⟩=0.321 sub-Poisson is a symptom of UNRESOLVED degeneracy; symmetry-resolved kNN is the clean test.
- **G6 (transit+kitaev)**: BOTH flag — anchored to canonical (atlas-04 T3 BROKEN, atlas-07 RETRACTED-S39, INTEG-39 DECISIVE FAIL, t_therm≈6 M_KK⁻¹, Brody β=0.633) — that "GGE NEVER thermalizes" does NOT survive. The reconciliation (S62): single-cell with physical interactions thermalizes fast (63% GOE); the CG(24) fabric is Poisson-integrable (⟨r⟩=0.367) and the Ordered Veil survives THERE; "valid during transit" is the operative scope.

**Consolidated reading**: the three Ordered-Veil gates (G4-3 ergodicity, G5-3 kNN, G6-1 reconciliation) are coherent ONLY if all are scoped to the fabric-scale integrability, NOT the retracted single-cell permanence. G6-1 is a prerequisite hygiene fix (capstone §7 narration DOWN to BROKEN/transit-window, capstone-hygiene Q3) that MUST precede or accompany the G4-3/G5-3 compute gates — otherwise the ergodicity and kNN gates inherit the over-stated permanence framing. The "transit IS the physics" claim (atlas-10 #8 PROVEN) is untouched; only "never thermalizes" is retracted. This is a Q3 capstone-hygiene action (PROSE tag == register tag), not a physics re-adjudication.

### §III.D — Tension D in detail (ε_LX cluster vs Jordan-ladder)

Not adversarial — convergent. The S99 fermion-mass panel (5 review syntheses, consensus lead baptista per-sector Higgs overlap) re-posed the S98 standing ε_LX gap as the rank-9b texture cluster (EVOI §1 rank-9b, raised to ~0.12). G4-1 (Sym³(3) cubic-ladder) is the cross-link: paper-02's exceptional-Jordan construction reaches the SAME FITTED-p≃1 wall in a DIFFERENT algebra, independently corroborating §VII.BL Generation-Blindness (the hierarchy is NOT A_K-buildable; ε_LX must break left-invariance on the multiplicity index). The consolidated structural statement: the cluster's `S100-YUKAWA-OVERLAP-OFFDIAG` (diagonal envelope = one Casimir exponential exp(−(k+S₀)C₂); off-diagonal w in one object) and `S100-CASIMIR-WIDENING` (9/5=1.800 vs PDG 1.8894) are the framework's own derivation; G4-1 maps ε_LX onto the Jordan fitted exponent + octonionic phase as an external cross-check. Any Yu-Ma generation-tripling route (G4 lower-EVOI) MUST RESPECT, not overturn, §VII.BL — admissible only if the tensor⊗quaternion extension IS the ε_LX deformation. No tension to resolve; the cluster and the corroboration reinforce.

### §III.E — Tension E in detail (§VII.W bridge sharpenings across G7)

The substantive content is a CANONICAL slot correction the index propagates. Anchored (knowledge MCP): §VII.AF.1 = the s86-hp1 R_geom quantum-metric bridge; §VII.W = HP parity-grading orthogonality of HP_*(A_F). The G7 sharpenings (both reports CONVERGENT): (1) Porlles-Chen — the diamagnetic metric is the quasihole/BdG-state metric, confirming the P_0 BdG-projector choice; (2) Chen-Karki-Hosur — the non-Abelian Tr[R_μν] (20%/50% fractions) is the algebra-correct object for A_K=ℂ⊕ℍ⊕M₃(ℂ), with Tr R≠Σ(per-band); (3) Tanaka(T²)+Banerjee(T-linear) — dual-platform measured anchor. Berry's geometric correction is load-bearing: the bridge object is the METRIC (Re QGT), and the framework's Berry CURVATURE vanishes identically (Im QGT=0, max|Ω|<4e-14) — so any reading importing a Chern/curvature contribution lands on a structurally-zero quantity. The framework lives in exactly the Chen-Karki-Hosur regime (metrically rich, topologically trivial: Tr R≠0 while Chern=0). G7-1 (slot relabel, hygiene) + G7-2 (projector/non-Abelian-trace structural confirmation). landau and berry agree on substance; minor disagreement on whether "37×" B1-dominance is canonically pinned (landau: not pinned, canonical squeeze=54.06×; berry: RECONCILED-69) — routed to a hygiene canonical-pin verification.

### §III.F — Tension F in detail (G8 seeding fork vs DM properties)

Anchored: `LRD_demographics_not_discriminating` STAGING (z<10²⁸). Both G8 reports converge: the SMDS dark-star channel (paper 06) is the ONLY G8 item that escapes the demographics wall, because it tests the DM INTERACTION property (annihilating vs not), not the assembly count. The framework's Leggett-channel DM is PROVEN non-annihilating (LEGGETT-MOMENT-70, Annihilation=0 PASS) → SMDS power source does not exist → channel CLOSED. The gas-dynamical DCBH (paper 10) is framework-COMPATIBLE, with the framework's DM contributing only gravitational adiabatic-contraction/dynamical-friction. The fork is ASYMMETRIC and that asymmetry IS the framework's position: if LRD heavy seeds form, they form gas-dynamically (DCBH/a₂-channel), NOT via dark stars — falsifiable in both directions. → `S100-SMDS-DARK-STAR-FORK` (mack-cosmic-bridge sole-writer registry row; the framework's distinctive falsifiable prediction in the seeding literature).

---

## IV. EVOI-Tier Mapping

Every consolidated candidate mapped against `sessions/evoi-framework.md` §1/§2/§3 tables (S100-stamped). EVOI values are the table's ordinal leverage proxies (NOT calibrated probabilities — honesty caveat per evoi-prioritization.md); used for ordering only.

| Candidate | EVOI-table anchor | Tier (table) | Leverage class |
|:----------|:------------------|:-------------|:---------------|
| **G1-2 / G2-1 / G1-3 / X-cut** `CF-S100-W2-1-QEQ-DRIVE` (dual-output) + `S100-X-C10-RHOVAC-EPOCH-PROFILE` | §1 rank-2 `CC-RESIDUAL-3PCT / C10-CLOSURE` (~0.18) + §6 queue #2 | **Tier 1** | HIGH — CC crown result, 114 OOM closed; C10 conditionality is the live edge. The single highest-EVOI compute in S99 review. |
| **G1-1** `CF-S100-W1-SF54-MAPPING` | §1 rank-1 `A(t)-FRIEDMANN-RECONCILE` (~0.20) + §6 queue #1 | **Tier 1** | HIGH — substrate→FRW keystone; one compute, three pillars. EVOI-maximal. |
| **G3-1** `CF-S100-MD-NORMALIZATION` | §1 rank-3 `Σm_ν-SEESAW` successor (~0.17) + §6 queue #8 | **Tier 1** | HIGH — zero-free-parameter firming of a clean external falsifier vs DESI (PASS landed). |
| **G3-2** `S100-MR-TEXTURE-CLASS`, **G3-3** `S100-D5-0NUBB-MAJORANA` | §2 rank-9b fermion-mass cluster adjacency + §6 queue #8 (D5 register-sourced) | **Tier 2** | MEDIUM-HIGH — discrete falsifiable M_R classification; m_ββ detection-match-ready (LEGEND-1000/nEXO). |
| **G4-1** `S100-SYM3-CUBIC-LADDER`, **G4-2** `S100-PS-VARIANT-ID` | §2 rank-9b ε_LX texture cluster (~0.12) + §6 queue #5 | **Tier 2** | MEDIUM-HIGH — first zero-parameter charged-lepton hierarchy attack (G4-1); positive beyond-SM gauge content + sin²θ_W (G4-2). |
| **G8-1** `S100-SMDS-DARK-STAR-FORK` | §2 rank-7 `σ_DM-NUCLEON` adjacency (~0.10; DM-property channel) | **Tier 2** | MEDIUM — turns the DM non-annihilation property into a direct seed-epoch falsifier (the ONE G8 discriminator). |
| **G2-2** `S100-WA-ROBUST`, **G2-3** w_0 branch-resolution | §5 w_a=0 four-fold lock (settled) + §1 rank-1/Falsifier-1 | **Tier 2** | MEDIUM — w_a=0 falsification-survival (not BF credit); w_0 DR3-binding branch pin. |
| **G6-3** `S100-FOLD-RANGE-SCALING`, **G6-2** `S100-BOX-DELTA-BOGOLIUBOV` | §3 adjacency (transit dynamics); K_pivot gap atlas-04 C2 | **Tier 3** | LOW-MED — universality-class pin (Rao); re-opens the FAILed cusp-Bogoliubov via correct discretization. |
| **G4-3 / G5-3** Ordered-Veil ergodicity + kNN, **G5-1** CF28 pole pre-flight, **G5-2** Lai-Teh reduction | §4 (structural/conceptual) + §3 higher-moments/Mellin-poles (<0.04) | **Tier 3–4** | LOW-MED — Ordered-Veil spectral-triple test (structural); CF28 pole-order pre-flight (gates s=7 registration); Lai-Teh is a mandatory unit test. |
| **G7-2** BdG-projector/non-Abelian-trace, **G7-3** Leggett-damping inheritance | §3 adjacency (lab-channel); §VII.AF.1 Element-5 strengthening | **Tier 3** | LOW-MED — hardens the strongest-evidenced bridge's laboratory-IN element; first lab handle on DM-mode lifetime. |
| **Hygiene cluster** (G6-1 capstone-Veil reconcile, G7-1 slot relabel, G3 phi_CP sector-split + NuFit re-pin, G2 σ8/H_0/anchor-currency re-pins, B reconcile) | Not EVOI gates — housekeeping/§A | **N/A** | Fix-in-session OR mack-bridge registry-write; the n_eff-direction reconcile (B) is the one genuine math-adjudication in this cluster. |
| **G8-2/G8-3 + G8 ceilings, G5/G7 math-rigor cluster** | §3/§4 adjacency; consistency-ceiling (G8 under z<10²⁸ wall) | **Tier 3–4** | LOW — joint constraints / rigor cross-checks of ALREADY-PROVEN machinery; valuable but not state-changing. |

**EVOI-table maintenance note for `/rclab-plan`**: the S100 EVOI table §6 queue already names `CF-S100-W2-1-QEQ-DRIVE`, `CF-S100-W1-SF54-MAPPING`, `CF-S100-MD-NORMALIZATION`, the fermion-mass cluster, and `S100-D5-0NUBB-MAJORANA`. This consolidation ADDS to the forward register: (a) the X-cut `S100-X-C10-RHOVAC-EPOCH-PROFILE` as the BBN read-out clause of QEQ-DRIVE (re-scope, not a new wave gate); (b) the n_eff-direction reconcile (§III.B) as a NEW Tier-1-adjacent prerequisite the table does not yet carry; (c) `S100-SMDS-DARK-STAR-FORK` as a new falsifier-inventory row (register-side, not a compute wave). The capstone-Veil reconciliation (G6-1) is a Q3 hygiene item the EVOI table does not track (housekeeping).

---

## V. Routing Recommendations (per candidate)

Three destinations: **S100-amendment** (the gate refines/extends an already-planned S100 wave — fold into the existing plan); **S101-plan via /rclab-plan** (genuine new forward compute, queue for next planning pass); **registry/inventory row via designated writer** (mack-cosmic-bridge sole-writes falsifier-master-inventory + capstone §7 surface; gen-physicist designated-writes capstone §-prose).

| Candidate | Route | Rationale |
|:----------|:------|:----------|
| **G1-2** `CF-S100-W2-1-QEQ-DRIVE` (dual-output re-scope) | **S100-amendment** | Already in EVOI §6 queue #2 (S100 W1). The re-scope (add BBN read-out clause emitting early-time ρ_vac(a)) is a plan amendment to the existing gate, per all 3 R3 agents. |
| **G1-3 / G2-1 / X-cut** `S100-X-C10-RHOVAC-EPOCH-PROFILE` | **S100-amendment** (CONDITIONAL/trigger-first) | A read-out clause on QEQ-DRIVE, not an independent gate — fold into the same S100 W1 block as a trigger-first sub-gate (fires iff QEQ-DRIVE returns non-tracking q_eq(H)). |
| **G1-1** `CF-S100-W1-SF54-MAPPING` | **S100-amendment** | EVOI §6 queue #1 (S100 W1). Already planned; the SF54 band-membership re-derivation is the named successor. |
| **G3-1** `CF-S100-MD-NORMALIZATION` | **S100-amendment** | EVOI §6 queue #8 (S100 W5). Already planned (Tier-1 #3 successor). |
| **G3-2** `S100-MR-TEXTURE-CLASS` | **S100-amendment** | Feeds CF-S100-MD-NORMALIZATION; co-locate in W5. MUST carry δ_CP∈{0,π} (dirac sector-conflation correction, §III.E). |
| **G3-3** `S100-D5-0NUBB-MAJORANA` | **S100-amendment** | EVOI §6 queue #8 (register-sourced, capstone §7.3 item-4 route). Already queued. |
| **G4-1** `S100-SYM3-CUBIC-LADDER`, **G4-2** `S100-PS-VARIANT-ID` | **S100-amendment** | Within the rank-9b fermion-mass cluster (EVOI §6 queue #5, S100 W2) for G4-1; PS-variant-ID is a W2/W4 adjacency. |
| **G8-1** `S100-SMDS-DARK-STAR-FORK` | **registry/inventory row → mack-cosmic-bridge** | A falsifier-master-inventory row (substrate predicts NO SMDS-powered seeds), NOT a compute gate. Sole-writer = mack per feedback_mack-bridge-role. Write-order: verdict→canonical_constants→inventory (math-scripts.md). |
| **G2-2** `S100-WA-ROBUST`, **G2-3** w_0 branch-resolution | **S101-plan via /rclab-plan** | Not in the current S100 queue (S100 is C10/fermion-mass-heavy). Genuine forward compute (uses paper-05 compressed datavector); queue for S101 with the observational anchors. |
| **G6-2** `S100-BOX-DELTA-BOGOLIUBOV`, **G6-3** `S100-FOLD-RANGE-SCALING` | **S101-plan via /rclab-plan** | New forward computes (addresses K_pivot gap atlas-04 C2, fast-quench class). Not in S100 queue; G6-2 re-opens the FAILed S85-W7 gate (carry the re-attempt recipe). |
| **G4-3** `S100-DK-ERGODICITY`, **G5-3** `S100-KNN-ORDERED-VEIL` | **S101-plan via /rclab-plan**, AFTER G6-1 | Ordered-Veil spectral-triple tests; both MUST be scoped to fabric-scale integrability (§III.C), so G6-1 (capstone reconcile) is a prerequisite. Queue together as the Ordered-Veil-stack wave. |
| **G5-1** `S100-CF28-SIMPLE-POLE-PREFLIGHT`, **G5-2** `S100-TAU0-LAITEH-REDUCTION` | **S101-plan via /rclab-plan** | G5-1 gates s=7 Pillar-VII registration (pole-order pre-flight); G5-2 is a mandatory eigensolver unit test (no registered reduction test exists). Both forward computes. |
| **G7-2** `S100-VII-W-BDG-PROJECTOR-CONFIRM` + `S100-NONABELIAN-METRIC-FRACTION` | **S101-plan via /rclab-plan** | §VII.AF.1 Element-5 structural confirmation (hardens the strongest-evidenced bridge). Forward compute (reuses S96 non-Abelian FHS scaffold). |
| **G7-3** `S100-LEGGETT-DAMPING-INHERITANCE`, **G8-2** `S100-A2-HEAVY-SEED-ABUNDANCE`, **G8-3** wrappers | **S101-plan via /rclab-plan** | Lab-channel + a₂-seeding forward computes; G8-2/G8-3 are consistency ceilings (degenerate below z<10²⁸) but produce joint constraints worth pre-registering. |
| **G7-1** §VII.AF.1 slot relabel | **registry/inventory → mack-cosmic-bridge** (or orchestrator-direct) | Registry-hygiene (index-legend caveat). §VII.W/§VII.AF.1 are mack sole-writer territory; INFO if registry already correct (likely). |
| **G6-1** capstone Ordered-Veil reconciliation | **registry/inventory → SPLIT writer** (§A in-session) | Capstone §7 falsifier-TABLE cell = mack-cosmic-bridge; capstone §-PROSE = gen-physicist designated writer (capstone-hygiene Q3/Q4). Fix-in-session, NOT a compute gate. |
| **Tension B** `S100-X-C10-BBN-CONSTRAINT-RECONCILE` (n_eff-direction) | **S101-plan via /rclab-plan** (genuine math-adjudication) | NOT hygiene — a Q1-YES math/physics adjudication (which BBN falsifier is operative; which n_eff direction relieves). Prerequisite for any relief gate. Carries Sage-exact substitution chain + registers external 0.107 budget (NON-canonical tag) + T_RH (non-canonical, locate). |
| **Hygiene re-pins** (phi_CP sector-split, NuFit-vintage, σ8/S8 re-anchor, H_0 LIVE-PENDING correction, w_0 anchor-currency post-Dovekie, "37×" canonical-pin) | **registry/inventory → mack/orchestrator (§A in-session)** | Status-tag edits / constant re-pins / provenance hygiene on already-correct artifacts. Fix-in-session per feedback_fix-in-session-never-defer; NOT carry-forwards (fail the 4-field test). σ8/S8 + H_0 + anchor-currency + falsifier rows route to mack (§7 surface sole-writer). |

**Honest-count discipline applied**: the 19 reports produced ~14 distinct genuine forward-compute gates (above) + ~12 hygiene/registry actions + the entire G8 consistency-ceiling family. I do NOT pad the carry-forward queue with the hygiene items (they fail the 4-field test — they are status-tag edits or re-pins on already-correct artifacts, fixed in-session) nor with the G8 ceilings re-cast as discriminators (they are joint constraints under the z<10²⁸ wall, explicitly INFO-by-design). The forward-compute queue that propagates via /rclab-plan is signal-rich and tight.

---

## VI. Summary Table

| # | Consolidated finding | Classification | Status | Routing |
|:--|:---------------------|:---------------|:-------|:--------|
| 1 | C10/BBN residual collapses to ONE compute (`CF-S100-W2-1-QEQ-DRIVE` dual-output → `S100-X-C10-RHOVAC-EPOCH-PROFILE`); magnitude corridor CLOSED, time-profile OPEN downstream | PHONONIC | Tier-1 keystone (7 reports converge) | S100-amendment (re-scope + trigger-first read-out) |
| 2 | n_eff-direction conflict (S66 G_eff n_eff=2.3 PASS vs S98/S99 lever n_eff<2 FAIL) — surfaced by 2/3 R3 agents | PHONONIC | UNRESOLVED canonical (math-adjudication) | S101-plan (`S100-X-C10-BBN-CONSTRAINT-RECONCILE`) |
| 3 | Ordered-Veil "never thermalizes" = BROKEN/RETRACTED-S39; survives as fabric-scale integrability; G4/G5/G6 stack must scope to fabric | PHONONIC | CANONICAL correction (G6 anchored) | G6-1 capstone reconcile (§A) PRECEDES G4-3/G5-3 (S101) |
| 4 | SF54 non-ratio expansion observable (spectral moment over GGE N(k), not q=0/0) | GEOMETRIC | Tier-1 #1 successor | S100-amendment (`CF-S100-W1-SF54-MAPPING`) |
| 5 | Σm_ν zero-free-parameter firming (m_D from D_K); M_R texture class (δ_CP∈{0,π} disfavors B-class); m_ββ ~1–4 meV NO-floor | PHONONIC/PARTICLE | Tier-1/2 (G3, sector-conflation flagged) | S100-amendment (W5 cluster) |
| 6 | ε_LX texture cluster ↔ Jordan-ladder FITTED-p≃1 = convergent corroboration of §VII.BL (STAGE-3-PERMANENT) | GEOMETRIC | Tier-2 (rank-9b, convergent not adversarial) | S100-amendment (`S100-SYM3-CUBIC-LADDER`, W2) |
| 7 | §VII.W bridge sharpenings: R_geom is §VII.AF.1 (slot correction); BdG-projector + non-Abelian-trace confirmed; object is METRIC not curvature | GEOMETRIC | Canonical correction + Element-5 strengthening | G7-1 hygiene (mack); G7-2 S101 |
| 8 | SMDS dark-star seeding REQUIRES annihilating DM → CLOSED to non-annihilating Leggett DM (the ONE G8 channel escaping z<10²⁸ wall) | PHONONIC | Physics-level discriminator | registry row → mack (`S100-SMDS-DARK-STAR-FORK`) |
| 9 | Baryogenesis "1.1 OOM gap" SUPERSEDED — CLOSED-SOURCED-UNIQUE (η_B=4.52e-11, φ_CP=π/2, φ88 unique); enhancement-menu = refinement-downstream | PHONONIC | Index framing corrected (both G3 converge) | Do NOT carry "close the gap"; η_B audit INFO-only |
| 10 | CF28 pole-order pre-flight (simple-vs-log at s∈{5,6,7}) gates s=7 Pillar-VII registration; Lai-Teh τ=0 reduction is a mandatory unit test | GEOMETRIC | Tier-3 (G5, scope-corrected: s=5/6 already convergent) | S101-plan (`S100-CF28-SIMPLE-POLE-PREFLIGHT`, `S100-TAU0-LAITEH-REDUCTION`) |
| 11 | Fold fast-quench class = Rao range-saturation (P_exc=1.000 rate-independent); box+delta re-attempt of FAILed S85-W7 cusp-Bogoliubov | PHONONIC | Tier-3 (G6, both converge) | S101-plan (`S100-FOLD-RANGE-SCALING`, `S100-BOX-DELTA-BOGOLIUBOV`) |
| 12 | Hygiene cluster: capstone-Veil reconcile, §VII.AF.1 relabel, phi_CP sector-split, NuFit re-pin, σ8/H_0/anchor-currency re-pins, "37×" pin | — | Fix-in-session (fail 4-field test) | §A in-session / mack registry-writes — NOT carry-forwards |
| 13 | G8 demographics = consistency CEILINGS not discriminators (z<10²⁸ wall, anchored); two-axis joint constraints + selection-function floor | PHONONIC/NON-PHONONIC | INFO-by-design (degenerate-with-ΛCDM) | S101-plan (joint-constraint pre-registration, explicitly non-discriminating) |

---

**Consolidation closing note.** The S99 review campaign's signal is concentrated: one keystone compute (the C10 q_eq(H) drive with a BBN read-out clause) that 7 of 19 reports independently name, three genuine paired-report DISAGREEMENTS that are signal not noise (the n_eff-direction conflict surfaced by 2/3 R3 agents; the G3 PMNS-vs-K_7 sector conflation; the Ordered-Veil permanence retraction that G4/G5 narrate as live and G6 corrects to fabric-scale-only), and a tight forward queue of ~14 distinct gates. The rest is consistency-mapping (the entire G8 group below the z<10²⁸ discrimination wall) and hygiene (slot relabels, constant re-pins, sector-disambiguation) that is fixed in-session, not carried forward. Every framework-state claim is anchored to canonical via the knowledge MCP; no gate verdict is re-adjudicated; paired-report disagreements are flagged explicitly, never averaged. The substrate-first arrow holds throughout: D_K eigenvalues → spectral-action moments → emergent physics → measurement — the early-vacuum time-profile, the seesaw spectrum, the quantum-metric bridge, the GGE relic statistics, and the heavy-seed collapse are all substrate-IS objects whose laboratory-IN shadows the 87 swept papers measure.

*Anchoring note: framework-state claims verified against canonical via knowledge MCP (get_constant / search_knowledge / query_entity) on 2026-06-04 — `delta_N_eff_vacuum_BBN_below=2.0873` (S98, not superseded), `Sigma_mnu_FW=0.0582053272` (S99 PASS, not superseded), GGE-permanence RETRACTED-S39 (atlas-04 T3 BROKEN + atlas-07; t_therm≈6 M_KK⁻¹, Brody β=0.633), `LRD_demographics_not_discriminating` STAGING (z<10²⁸), §VII.AF.1 = s86-hp1 R_geom quantum-metric bridge. The 19 source reports' gate-verdict citations are authoritative and NOT re-adjudicated; their paired-report disagreements are carried as flagged conflicts per the Focus. EVOI values are the S100-table ordinal leverage proxies, not calibrated probabilities. Sage-exact figures (ΔN_eff 2.0873; relief_factor 0.414123; a-exponent +0.0438; ∂/∂n_eff = X = 40.2756; n_eff crossings 1.95984/1.904349; exceedances 2.087×/19.51×) reproduced from the R3 syntheses, not independently re-derived here.*
