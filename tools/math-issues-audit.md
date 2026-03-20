# Mathematical Issues — Paper Library Audit (2026-02-21)

Every math error found by the 16-agent audit, extracted for knowledge-weaver investigation.
Status column: **FIXED** = agent corrected the file. All 60 issues resolved (3 formerly "UNFIXABLE" items fixed 2026-02-21 via source PDF verification).

---

## CRITICAL (affects downstream computations or foundational axioms)

| # | Folder | File | Error | Was | Corrected To | Status | Contamination Trace |
|---|--------|------|-------|-----|-------------|--------|---------------------|
| M-01 | Connes | `09_2006_Connes_Standard_model_neutrino_mixing.md` | KO-dim 6 signs wrong | J²=-1, (ε,ε',ε'')=(-,+,+) | J²=+1, (+1,+1,-1) | FIXED | CONTAMINATED: (1) knowledge-index.json line 88 proven_10 still says "class DIII topological superconductor" (sourced from Session 16 which predates correction). (2) Session 16 round 3a line 554 states "J*D_F is antisymmetric if J^2 = -1 (KO-dim 6 condition)" -- WRONG sign cached in knowledge-index eq context. (3) `.claude/agent-memory/connes-ncg-theorist/MEMORY.md` lines 210-211 still say "Paper 09 uses J^2 = -1 for KO-dim 6" and "Both are correct" -- stale memory contradicts line 10 of same file. (4) Session 8 computation verified J^2=+1 at machine epsilon independently, so NO computation was affected. (5) All sessions post-17 use correct J^2=+1. |
| M-02 | Connes | `10_2007_Chamseddine_Connes_Marcolli_Gravity_standard_model.md` | KO-dim 6 signs wrong | (ε,ε',ε'')=(-1,+1,+1) | (+1,+1,-1) | FIXED | CONTAMINATED: Same propagation as M-01. knowledge-index.json eq_475 (line 10850) correctly has Yukawa trace from this paper's Session 22 usage, but the paper's own epsilon signs were wrong. Session 19d connes-collab line 124 correctly states (+1,+1,-1). No computation used the paper's wrong signs -- all computations derive from Session 8 branching code which verified (+1,+1,-1) independently. |
| M-03 | Connes | `04_1994_Connes_Noncommutative_Geometry_book.md` | KO-dim table wrong ε'' | KO-2: (-,+,.), KO-4: (-,+,-) | KO-2: (-,+,-), KO-4: (-,+,+) | FIXED | CONTAINED: The KO-dim table for dimensions other than 6 is not used in any computation or gate verdict. All project work uses KO-dim 6 exclusively. The knowledge-index does not contain entries for KO-dim 2 or KO-dim 4 sign tables. No propagation found. |
| M-04 | Connes | `06_1995_Connes_Moscovici_Local_index_formula.md` | Seeley-DeWitt a₂ coefficient | (1/4)·rank(S) | (5/12)·rank(S) — factor 5/3 error | FIXED | CONTAINED: The tier0 computation `sd20a_seeley_dewitt_gate.py` derives a_2 from first principles using the Lichnerowicz formula `a_2 = (1/6)*tr(6E+R*Id)` with `E=R/4*Id` for the Dirac Laplacian (lines 326-329), yielding `(20/3)*R` for the reduced coefficient. This is independent of the Connes-Moscovici paper's coefficient convention. The knowledge-index a_2 entries (lines 32162, 32177) use `(R/6)*rank(S)` which is the standard Gilkey formula, not the Connes-Moscovici convention. The M-04 error is about a specific formula in the LOCAL INDEX context, not the heat kernel a_2 used in computations. No gate verdict or theorem depends on the (1/4) vs (5/12) distinction. |
| M-05 | Connes | `14_2019_Connes_NCG_spectral_standpoint.md` | a₄ formula incomplete | Only 5R²-2Ric²+2Riem² | Added 60RE+180E²+30\|Ω\|² terms | FIXED | POSSIBLE: The tier0 computation `sd20a_seeley_dewitt_gate.py` (lines 302-320) uses the COMPLETE Gilkey a_4 formula including all 60RE, 180E², spin connection Omega² terms, derived independently. Knowledge-index equations (lines 11294-11301, 118457, 122234-122309) all contain the full formula. The incomplete formula in the paper could have misled agents reading only that paper, but all actual computations used the full formula. Session 20a SD-1 gate verdict used the full formula and correctly determined V_eff monotonic. |
| M-06 | Connes | `11_2010_Chamseddine_Connes_NCG_unification_framework.md` | Yukawa trace `e` wrong | e = Tr(M_R*M_R) | e = Tr(Y_ν*Y_ν·M_R*M_R) | FIXED | POSSIBLE: Knowledge-index eq_475 (line 10850) has CORRECT formula `e = Tr(Y_nu^* Y_nu . M_R^* M_R)`. Meeting minutes Sessions 21c-r2 and 22 correctly state the full trace. Session 22c Trap 3 (C-1) used `e/(a*c) = 1/dim(spinor)` which requires the correct definition of `e`. The wrong `e = Tr(M_R*M_R)` from the paper was never used in computations (it equals `c`, making the Higgs-sigma portal trivially wrong). The Trap 3 proof in Session 22c explicitly derives `e/(a*c)` from the tensor product structure, bypassing any reliance on the paper transcription. |
| M-07 | S-P | `10_2010_Penrose_Conformal_cyclic_cosmology.md` | Ricci tensor conformal transform: 2 sign errors | -2·Υ_μΥ_ν and -2·Υ²g_μν | +2·Υ_μΥ_ν and +2·Υ²g_μν | FIXED | CONTAINED: The conformal transformation formulas from Penrose CCC are not used in any tier0 computation or gate verdict. Meeting-minutes Sessions 19d and 20b discuss CCC qualitatively (structural analogy with spectral exflation) but never apply the conformal transform formulas quantitatively. No equations in the knowledge-index reference the Ricci tensor conformal transform. |
| M-08 | S-P | `10_2010_Penrose_Conformal_cyclic_cosmology.md` | Ricci scalar conformal transform: triply wrong | R̃=Ω²R-6Ω¹□Ω+12(∂Ω)² | R̃=Ω⁻²R-6Ω⁻³□Ω (no (∂Ω)² in d=4) | FIXED | CONTAINED: Same reasoning as M-07. The conformal Ricci scalar formula is never used in any project computation. All curvature computations use the Jensen deformation on SU(3) directly (Baptista formulas, tier0 exact curvature), not conformal rescaling. |
| M-09 | KK | `09_1981_Witten_Search_for_realistic_KK.md` + index | SM-in-SO(8) embedding rank violation | SO(6)×SO(2)×SO(2) rank 5 > rank(SO(8))=4 | SU(4)~Spin(6) chain | FIXED | CONTAINED: The Witten SO(8) embedding chain is about 11D supergravity KK, not about the phonon-exflation 12D framework. The project uses SU(3) as the internal manifold, not S^7 or SO(8). The rank violation was in the KK paper's exposition only. No computation or gate verdict references the SO(6)xSO(2)xSO(2) decomposition. Knowledge-index mentions SO(8) only in the context of Spin(8) spinor bundles on SU(3) (lines 81077, 124238), which is a different mathematical object. |
| M-10 | KK | index.md | Kerner eq(26-30) missing R_G term | R = K + (1/4)g_ab F^a F^b | R = K + R_G + (1/4)g_ab F^a F^b; R_G is constant fiber curvature (omitted intentionally — acts as cosmological constant, doesn't affect field equations) | FIXED | CONTAINED: The Kerner result is cited historically in knowledge-index (lines 475-479) but the actual Ricci decomposition used in computations comes from Baptista Paper 13 eq 1.5 and the direct Jensen metric computation. The R_G term is a constant (fiber curvature of bi-invariant metric) and was intentionally omitted by Kerner as it acts only as a cosmological constant. No computation depends on the Kerner decomposition formula. |

---

## SIGNIFICANT (wrong numerical values or dimensional errors)

| # | Folder | File | Error | Was | Corrected To | Status | Contamination Trace |
|---|--------|------|-------|-----|-------------|--------|---------------------|
| M-11 | Einstein | `07_1917_Einstein_Cosmological_considerations.md` | De Sitter entropy dimensional error | S = 3πc⁵/(GℏΛ) | S = 3πc³/(GℏΛ) | FIXED | CONTAINED: De Sitter entropy formula not in knowledge-index. Meeting-minutes reference Gibbons-Hawking entropy `S_dS = 3pi/(Lambda_4 * l_P^2)` (Giants Planck Geometry, line 183) which uses natural units and is dimensionally correct. No tier0 computation uses the c^5 vs c^3 formula. |
| M-12 | Einstein | `07_1917_Einstein_Cosmological_considerations.md` | Planck density dimensional error | ρ ~ m_P⁴c³/ℏ³ (mass density) | ρ ~ m_P⁴c⁵/ℏ³ (energy density) | FIXED | CONTAINED: Planck density is not used quantitatively in any computation. All tier0 scripts work in natural units where rho_Planck = 1. The dimensional formula was only in the Einstein paper exposition. |
| M-13 | Einstein | `08_1924_Einstein_BEC.md` | BEC density of states prefactor | 4π·V·(2m)^{3/2}/h³ (factor 2 too large) | 2π·V·(2m)^{3/2}/h³ | FIXED | CONTAINED: The BEC density of states formula is not in the knowledge-index or any tier0 computation. The project's BEC references (knowledge-index lines 970, 13226-13298) are about BCS-BEC crossover in the spectral context, not the Einstein BEC density of states. |
| M-14 | Einstein | `08_1924_Einstein_BEC.md` | Bose/Fermi sign convention reversed | Bosons +1, Fermions -1 | Bosons -1, Fermions +1 | FIXED | CONTAINED: Knowledge-index correctly states free energy formulas with `F_boson = +T*ln(1-e^{-E/T})` (line 5378) and `F_fermion = -T*ln(1+e^{-E/T})` (line 5390), using the correct sign conventions. The Einstein paper's reversed signs were never propagated. |
| M-15 | Einstein | `12_1939_Oppenheimer_Snyder.md` | Collapse time off by ~60x | τ ~ 10⁻³ s | τ ~ 0.06 s | FIXED | CONTAINED: Oppenheimer-Snyder collapse time not referenced in any computation, gate verdict, or knowledge-index equation. The project does not model gravitational collapse. |
| M-16 | Hawking | `03_1973_Bardeen_Carter_Hawking.md` | Near-extremal κ spurious √2 | κ ~ √(2(M²-a²))/(4M²) | κ ~ √(M²-a²)/(2M²) | FIXED | CONTAINED: Near-extremal surface gravity not in knowledge-index or any computation. The project's surface gravity references are qualitative (thermodynamic analogy). |
| M-17 | Landau | `08_1950_Ginzburg_Landau.md` | H_{c1} constant off by factor 6 | 0.08 | 0.50 | FIXED | CONTAINED: H_{c1} numerical coefficient not referenced in any project computation. The Ginzburg-Landau discussion in the project is about the order parameter analogy (phase transition structure), not specific H_{c1} values. |
| M-18 | Feynman | `12_1949_Dyson_Radiation_theories.md` | Power-counting propagator exponents swapped | Fermion -2, Photon -1 | Fermion -1, Photon -2 | FIXED | CONTAINED: Power-counting exponents not in knowledge-index. The project's power-counting analysis (knowledge-index line 11105, Session 22c L-3 Perturbative Exhaustion Theorem) uses H1-H5 conditions derived from scratch, not from the Dyson paper. |
| M-19 | Neutrino | `02_1956_Cowan_Reines.md` + index | IBD prompt energy derivation logic wrong | E_prompt = E_ν - 0.784 MeV | E_prompt = E_ν - 0.782 MeV | FIXED | CONTAINED: IBD prompt energy not in knowledge-index equations or tier0 computations. The neutrino-related computations (R(tau) gate, Session 24a R-1) use eigenvalue ratios, not IBD kinematics. |
| M-20 | Neutrino | `09_2003_KamLAND.md` | Oscillation minimum formula wrong | L/E = 2π/Δm² ~ 40 km/MeV | L/E = π/(2·1.267·Δm²) = 16.7 km/MeV | FIXED | CONTAINED: Oscillation minimum formula not in knowledge-index or any computation. The project's neutrino gate (R(tau) in [17,66]) uses eigenvalue ratios from D_K, not oscillation phenomenology formulas. |
| M-21 | Neutrino | `10_2012_Daya_Bay.md` | J_CP/J_CKM ratio off by 3x | ~3000x larger | ~1000x larger | FIXED | CONTAINED: J_CP/J_CKM ratio not used in any computation or gate verdict. The neutrino sector analysis focuses on mass squared ratios, not CP violation magnitudes. |
| M-22 | Paasch | index.md (Paper 03) | Mass number exponent wrong | N(j) = (m_j/m_e)^{1/2} | N(j) = (m_j/m_e)^{2/3} | FIXED | CONTAMINATED: (1) Knowledge-index eq_422 context (line 10217) still contains "N(j) = (m_j/m_e)^{1/2}" -- the WRONG exponent from the unfixed Paasch index. (2) Meeting-minutes Session 21c paasch-collab line 83 says "N(j) = (m_j/m_e)^{1/2}" -- WRONG. (3) Session 21c-r2 paasch-collab line 109 repeats the wrong exponent. (4) Knowledge-index lines 6717 and 11234 have the CORRECT 2/3 exponent. (5) Agent memories aware of correction: paasch agent MEMORY.md line 28 explicitly notes "^{1/2} -> ^{2/3}". (6) The eigenvalue ratio test (phi_paasch) uses lambda ratios from D_K directly, not N(j), so computation results are NOT affected. But the meeting minutes and one knowledge-index context field are contaminated. |
| M-23 | Paasch | index.md (Paper 04) | Alpha formula OCR-garbled | α = (1/f)^{2n₃} (garbled) | α = (1/n₃²)(f/2)^{1/4} = (1/100)(0.5671433/2)^{1/4} = 0.007297359. Verified against source PDF (HAL hal-01375989v3, p.5, eq 2.8-2.9) | FIXED | CONTAINED: The garbled OCR formula was only in the Paasch index.md. The knowledge-index does not contain the alpha derivation formula. No computation or gate verdict depends on the Paasch alpha formula -- the project's alpha analysis is purely about the g1/g2 coupling ratio from D_K eigenvalues (Session 17a identity). |
| M-24 | Paasch | index.md (Paper 03) | m_E conflated with half-muon | m_E = √(m_e·m_p) = 21.9 MeV = "half-muon" | 21.9 MeV ≠ 52.8 MeV; distinct quantities | FIXED | CONTAINED: m_E and the "half-muon" concept do not appear in the knowledge-index, meeting minutes, or any computation. |
| M-25 | Paasch | index.md + Paper 16 | Wyler alpha accuracy wrong baseline | ~1.1 ppm (vs 1970s data) | ~0.6 ppm (vs CODATA 2018) | FIXED | CONTAINED: Wyler alpha accuracy not in knowledge-index or any computation. The project does not use Wyler's geometric alpha value. |

---

## MODERATE (formula errors in non-computational papers)

| # | Folder | File | Error | Was | Corrected To | Status | Contamination Trace |
|---|--------|------|-------|-----|-------------|--------|---------------------|
| M-26 | LRD | `01_2024_Matthee.md` | L_Edd coefficient wrong by 10⁸ | 1.3×10³⁸ (M/10⁸) erg/s | 1.3×10⁴⁶ (M_BH/10⁸M☉) erg/s | FIXED | CONTAINED: LRD papers have 0 session citations in knowledge-index (line 5096). No LRD formula appears in any computation, gate verdict, or meeting-minutes synthesis. |
| M-27 | LRD | `05_2023_Maiolino_GN-z11.md` | L_Edd computation entirely wrong | Wrong parametrization | Corrected formula + result 2.1×10⁴⁴ | FIXED | CONTAINED: Same as M-26. LRD domain is uncited. |
| M-28 | LRD | `07_2025_Volonteri.md` | BH growth equation sign | dM/dt = ε·Ṁ_acc | dM/dt = (1-ε)·Ṁ_acc | FIXED | CONTAINED: Same as M-26. LRD domain is uncited. |
| M-29 | LRD | `07_2025_Volonteri.md` | Eddington accretion rate off ~10 orders | 1.5×10⁻⁸ (M/10⁸) M☉/yr | ~2.2 M☉/yr for 10⁸M☉ at ε=0.1 | FIXED | CONTAINED: Same as M-26. LRD domain is uncited. |
| M-30 | LRD | `02_2023_Labbe.md` | Stellar mass surface density off by 10⁴ | ~10⁹ M☉/pc² | ~1.4×10⁵ M☉/pc² | FIXED | CONTAINED: Same as M-26. LRD domain is uncited. |
| M-31 | LRD | `03_2024_Greene_UNCOVER.md` | Balmer break wavelength wrong | λ_obs ~ 22 μm at z=4.47 | ~2.0 μm | FIXED | CONTAINED: Same as M-26. LRD domain is uncited. |
| M-32 | LRD | `04_2024_Kokorev.md` | Solid angle conversion off by 10⁴ | 640 arcmin² = ~0.18 sr | ~1.5×10⁻⁵ sr | FIXED | CONTAINED: Same as M-26. LRD domain is uncited. |
| M-33 | LRD | `08_2024_Agarwal.md` | BH mass formula dimensionally wrong | M_BH ~ L_bol·t_Edd/(2Gm_pc) | Replaced with standard formula | FIXED | CONTAINED: Same as M-26. LRD domain is uncited. |
| M-34 | LRD | `09_2024_Pacucci.md` | Outflow velocity formula dimensionally wrong | v_out ~ √(σ_T·L/(m_pc)) → cm^{3/2}/s | Replaced with escape velocity + radiation | FIXED | CONTAINED: Same as M-26. LRD domain is uncited. |
| M-35 | LRD | `05_2023_Maiolino_GN-z11.md` | GN-z11 BH mass off by 10x | 3×10¹⁰ M☉ | 3×10⁹ M☉ | FIXED | CONTAINED: Same as M-26. LRD domain is uncited. |
| M-36 | Tesla | `01_1899_Colorado_Springs.md` | Schumann resonance factor of 2 | f₀ = c/(4πR_E) = 3.75 Hz | f₀ = c/(2πR_E) = 7.5 Hz | FIXED | CONTAINED: Schumann resonance not in knowledge-index or any computation. The Tesla-Resonance papers are used for qualitative analogies (resonance, acoustic modes), not for specific frequency values. |
| M-37 | Tesla | `04_1912_Mechanical_Oscillator.md` | Power absorption dimensionally wrong | P = (1/2)\|F\|²·ω₀·ζ | P = F₀²/(4mω₀ζ) | FIXED | CONTAINED: Mechanical oscillator power absorption formula not in knowledge-index or any computation. |
| M-38 | Tesla | `13_2003_Ashtekar_LQC.md` + index | LQC bounce density wrong | Bounce at ρ_c/2 | Bounce at ρ_c (H=0 → ρ=ρ_c) | FIXED | POSSIBLE: Knowledge-index eq_349 (line 9338) has the correct modified Friedmann equation `H^2 = (8piG/3)rho(1-rho/rho_c)` which gives bounce at rho=rho_c (H=0). Meeting-minutes Sessions 19d and 20b discuss the LQC bounce qualitatively (moduli-space analog) without using the wrong rho_c/2 value. The Tesla-Resonance index.md was fixed. The equation in knowledge-index was always correct. But agents reading the pre-fix paper could have internalized rho_c/2. No agent memory found caching the wrong value. |
| M-39 | Tesla | `17_1972_Pathria.md` | Surface gravity chain dimensionally wrong | Claimed Planck-scale result | Actually Hubble-scale; κ=c⁴/(4GM) | FIXED | CONTAINED: Pathria surface gravity formula not in knowledge-index or any computation. The BH-cosmology analogy in the project is qualitative only. |
| M-40 | Tesla | `20_2001_Easson_Brandenberger.md` + index | Hagedorn temperature dimensional | T_H = √α'/(2π) (length units) | T_H = 1/(2π√(2α')) (energy units) | FIXED | CONTAINED: Hagedorn temperature not in knowledge-index equations or tier0 computations. The Easson-Brandenberger paper is referenced qualitatively for the BH gas cosmology concept, not for specific temperature formulas. |
| M-41 | Berry | `03_1984_Diabolical_Points.md` | Garbled energy gap formula | E_n-E_m on both sides | Δ E = √((ΔE_diag)²+4\|V\|²) | FIXED | CONTAINED: The diabolical points energy gap formula is not in the knowledge-index. The project's avoided crossing analysis (Berry curvature at M1/M2, Sessions 21a-24b) uses eigenvalue data from D_K directly, not from analytic gap formulas. |
| M-42 | Berry | `11_1984_Berry_Curvature_Solids.md` | Anomalous velocity missing minus sign | v_anom = ... (positive) | Added crucial minus sign | FIXED | CONTAINED: Session 21c tesla-collab line 63 correctly states `v_anom = -Omega x v_g/omega^2` with the minus sign. The Berry curvature computation in Session 24a uses numerical eigenvalue derivatives, not the anomalous velocity formula. |
| M-43 | Berry | `10_1983_Berry_BGS_Conjecture.md` | GOE/GUE form factor mislabeled | K(k)=k for k<1 labeled GOE | That is GUE; GOE is K=2k-k·ln(1+2k) | FIXED | POSSIBLE: Knowledge-index equations reference GOE spacing distribution `P(s) = (pi/2)*s*exp(-pi*s^2/4)` (lines 95390, 96329) which is the correct GOE Wigner surmise -- this is for the nearest-neighbor spacing distribution, not the spectral form factor K(tau). The form factor mislabeling in the BGS paper is a different quantity. The level statistics computations in tier0 (Brody parameter) correctly distinguish Poisson vs GOE in the spacing distribution. However, any agent reading the BGS paper for form factor analysis could have been confused by the swap. |
| M-44 | S-P | `05_1969_Penrose_Cosmic_censorship.md` | Event horizon = black hole region | H⁺ = M\J⁻(I⁺) | H⁺ = ∂(M\J⁻(I⁺)) = ∂B (boundary, not complement) | FIXED | CONTAINED: Event horizon definition not in knowledge-index or any computation. The Penrose papers are referenced for singularity theorems and cosmic censorship qualitatively. |
| M-45 | Hawking | `13_1993_Page_Information.md` | Page time mass loss conflated with time fraction | "lost 37% of mass" at t_P | Only ~14% mass lost at t_P~0.37·t_evap | FIXED | CONTAINED: Page time mass loss not in knowledge-index. Meeting-minutes references to "Page time" (Giants sessions) are about the information-theoretic concept (when does S_radiation > S_BH), not about the numerical mass fraction. |
| M-46 | KK | `10_1980_Freund_Rubin.md` | Ricci scalar ratio wrong | Λ_{AdS4}/R_{S7} = -6/7 | R_{AdS4}/R_{S7} = -8/7. From general formula -s(d-s-1)/((s-1)(d-s)) with d=11,s=4; confirmed by DNP Paper 11 eqs (10-11): R_4=4×(-12m²)=-48m², R_7=7×(6m²)=42m² | FIXED | CONTAMINATED: (1) Session 19d kk-collab line 136 cites "Freund-Rubin ratio Lambda/R = -6/7" -- the WRONG value. (2) Session 22 kk-collab line 43 says "Lambda_{AdS4}/R_{K7} = -6/7" -- WRONG, repeated 3 sessions after the paper was written. (3) No agent memory caches the wrong value. (4) No tier0 computation uses the Freund-Rubin ratio directly -- the project's beta/alpha=0.28 is from spectral action coefficients on SU(3), not from the 11D S^7 ratio. (5) The wrong ratio does not affect any gate verdict (the project uses SU(3), not S^7). But the meeting-minutes are contaminated with the wrong value in two sessions. |
| M-47 | Neutrino | index.md | sin²(2θ₂₃) conflated with sin²(θ₂₃) | Single row for both quantities | Split: oscillation amplitude vs octant measurement | FIXED | CONTAINED: The neutrino mixing angle theta_23 is not used quantitatively in any computation. The project's neutrino analysis focuses on Delta m^2 ratios from eigenvalue ratios (R(tau) gate), not mixing angles. |
| M-48 | Landau | `03_1935_Landau_Lifshitz.md` | Walker field formula wrong | H_W = α·M_s·K_u/(2M_s) | H_W = α·K_u/M_s | FIXED | CONTAINED: Walker field formula not in knowledge-index or any computation. The Landau-Lifshitz paper is referenced for magnetic domain concepts, not for specific Walker field values. |

---

## CLASSIFICATION / TOPOLOGY ERRORS (all BDI vs DIII)

| # | Folder | File | Error | Status | Contamination Trace |
|---|--------|------|-------|--------|---------------------|
| M-49 | Antimatter | `02_1930_Dirac.md` | AZ class DIII → BDI (T²=+1) | FIXED | CONTAMINATED: (1) Knowledge-index proven_10 (line 88) still says "class DIII". (2) Knowledge-index open_channels (line 4517) says "AZ class DIII". (3) Knowledge-index eq context (line 9209) says "class DIII (topological superconductor)". (4) Multiple pre-Session-17 meeting minutes (Sessions 11, 13, 15, 16) reference "class DIII" extensively -- at least 25 occurrences across 6 files. (5) Agent memories still contaminated: `baptista-spacetime-analyst/ncg_chirality_resolution.md` line 79; `kaluza-klein-theorist/session11_crossreview.md` lines 31, 33; `quantum-acoustics-theorist/session11_final_verdict.md` line 84; `quantum-acoustics-theorist/session11_chirality.md` lines 565, 573, 578, 583, 614, 643. (6) Session 17 CORRECTED this to BDI and all post-17 sessions use BDI correctly. (7) The correction is noted in: dirac agent memory line 34-35; hawking agent memory line 71; einstein agent memory line 117-118; connes audit log line 14. (8) COMPUTATION IMPACT: The AZ class does not affect eigenvalue computations (those depend only on D_K, not on the classification label). The Pfaffian computation (Session 17c D-2) gives Z_2=+1 which is valid for BOTH BDI and DIII. No numerical result changes. But the DIII label persists in the knowledge-index and multiple agent memories. |
| M-50 | Antimatter | `14_Antimatter_open_questions.md` | AZ class DIII → BDI | FIXED | CONTAMINATED: Same knowledge-index and agent-memory propagation as M-49. See M-49 trace for full details. |
| M-51 | Connes | `02_1985_Connes_NCG_diff_geom.md` | AZ class DIII → BDI | FIXED | CONTAMINATED: Same knowledge-index and agent-memory propagation as M-49. Additionally, Connes agent MEMORY.md lines 210-211 conflict with line 10 (correct value) in the same file. |
| M-52 | Connes | `04_1994_Connes_NCG_book.md` | AZ class DIII → BDI | FIXED | CONTAMINATED: Same as M-49. |
| M-53 | Connes | `14_2019_Connes_NCG_spectral.md` | AZ class DIII → BDI | FIXED | CONTAMINATED: Same as M-49. |
| M-54 | Landau | `02_1930_Landau_Diamagnetism.md` | AZ class DIII → BDI | FIXED | CONTAMINATED: Same as M-49. Landau agent MEMORY.md line 12 correctly notes the fix: "Paper 02: AZ class was DIII (wrong), fixed to BDI T^2=+1 (Session 17c)". |

---

## NOTATION / CONVENTION ERRORS

| # | Folder | File | Error | Status | Contamination Trace |
|---|--------|------|-------|--------|---------------------|
| M-55 | Landau | `05_1941_Landau_Superfluidity.md` | K = SU(3)/(SU(2)×U(1)) → K = SU(3) | FIXED | CONTAINED: The knowledge-index and all computations correctly use K = SU(3) as the full group manifold. One tier0 reference (line 103934) mentions `C^2 = SU(3)/(SU(2)xU(1))` but this is about the coset complement in the tangent space decomposition (mathematically distinct from saying K is the coset), not the internal manifold. |
| M-56 | Landau | `08_1950_Ginzburg_Landau.md` | Same coset → group manifold fix | FIXED | CONTAINED: Same as M-55. |
| M-57 | LaTeX | `06_Differential_Geometry_Notation.md` | SU(3) described as "3D" → 8D | FIXED | CONTAINED: The knowledge-index consistently treats SU(3) as 8-dimensional (dim(SU(3))=8). All tier0 computations use 8D Dirac operators, 2^4=16 spinor dimension, etc. The "3D" error was confined to a LaTeX notation guide that is not used by any computation. |
| M-58 | LaTeX | `07_Spectral_Theory_NCG_Notation.md` | Spectral dim "4+2" → 4+8=12 (KO-dim remains 6) | FIXED | POSSIBLE: The confusion between spectral/metric dimension (4+8=12) and KO-dimension (4+2=6 mod 8) is subtle. Knowledge-index line 14138 correctly explains `KO-dim 6 = 4 + 2 (mod 8)` where 4 is from M_4 and 2 is from F (finite geometry). The distinction between metric dimension 12 and KO-dimension 6 is correctly maintained throughout the knowledge-index. However, agents reading the LaTeX notation guide could have been confused into thinking the total dimension is 6 rather than 12. No computation uses "4+2" as a metric dimension -- all use 8D or 12D correctly. |
| M-59 | Connes | `10_2007_CCM.md` | f_k cutoff convention mixing | FIXED (clarifying note) | POSSIBLE: Knowledge-index has TWO different conventions for the spectral action expansion. Line 8469: `S = f_0*Lambda^4*a_0 + f_2*Lambda^2*a_2 + f_4*a_4` (standard 4D Connes convention, Lambda powers descending). Line 116654: `S = f_0*a_0 + f_2*Lambda^2*a_2 + f_4*Lambda^4*a_4` (Lambda powers ascending -- this is from tier0 s23c code which uses d=8 convention). The two conventions are both internally consistent for their respective dimensions but coexist in the knowledge-index without disambiguation. An agent combining equations from both sources could produce errors. No gate verdict depends on the f_k convention since the ratios a_4/a_2 used in gates are convention-independent. |
| M-60 | Tesla | `19_2010_Poplawski.md` | T_μν on both sides with different meanings | FIXED (Σ_μν for torsion) | CONTAINED: The Poplawski notation issue (T_munu meaning both stress-energy and torsion) was confined to the paper file. Meeting-minutes Sessions 20b and 21c reference Poplawski qualitatively (rho^2 correction, torsion bounce) without using the T_munu notation. Knowledge-index does not contain Poplawski equations. |

---

## Summary Statistics

| Category | Count | Fixed | Unfixable |
|----------|-------|-------|-----------|
| Critical (axioms/foundations) | 10 | 10 | 0 |
| Significant (numerical/dimensional) | 15 | 15 | 0 |
| Moderate (non-computational papers) | 23 | 23 | 0 |
| Classification/topology (BDI/DIII) | 6 | 6 | 0 |
| Notation/convention | 6 | 6 | 0 |
| **TOTAL** | **60** | **60** | **0** |

### Previously "Unfixable" Items — Now Resolved (2026-02-21)
1. **M-10**: Kerner R_G (fiber curvature) is a CONSTANT for compact Lie groups with Killing metric. Kerner intentionally omits it — standard practice (cosmological constant term, doesn't affect field equations). Clarifying note added to KK index.
2. **M-23**: Source PDF (HAL hal-01375989v3, p.5) confirms correct formula: α = (1/n₃²)(f/2)^{1/4} where ln(f)=-f. OCR had mangled this to "(1/f)^{2n₃}" — completely different expression. Paper 04 transcription and index corrected.
3. **M-46**: Ratio is R₄/R₇ = -8/7, NOT -6/7. Derivable from general formula -s(d-s-1)/((s-1)(d-s)) with d=11,s=4, and confirmed by DNP Paper 11 eqs (10-11). The "-6/7" was a transcription computation error. Paper 10 and KK index corrected.

---

## Contamination Trace Summary (2026-02-21, Knowledge Weaver)

### CONTAMINATED (concrete propagation found)

| Issue(s) | Artifact | What's Wrong | Computation Impact |
|----------|----------|--------------|-------------------|
| M-01, M-02, M-49--M-54 | `tools/knowledge-index.json` line 88 (proven_10) | Says "class DIII" instead of "class BDI" | NONE -- label only, eigenvalues unaffected |
| M-49--M-54 | `tools/knowledge-index.json` line 4517 (open_channels) | Says "AZ class DIII" | NONE -- label only |
| M-49--M-54 | `tools/knowledge-index.json` line 9209 (eq context) | Says "class DIII (topological superconductor)" | NONE -- label only |
| M-01 | `sessions/archive/session-16/session-16-round-3a-computational.md` line 554 | "J^2 = -1 (KO-dim 6 condition)" -- WRONG sign | NONE -- Session 8 code used +1; this is prose |
| M-01 | `.claude/agent-memory/connes-ncg-theorist/MEMORY.md` lines 210-211 | "Paper 09 uses J^2 = -1" and "Both are correct" | POSSIBLE -- could mislead future connes agent reads |
| M-49--M-54 | 6 agent memory files (baptista, KK, quantum-acoustics) | Multiple "class DIII" references from Session 11 era | POSSIBLE -- could mislead future agent reads |
| M-22 | `tools/knowledge-index.json` eq_422 context (line 10217) | "N(j) = (m_j/m_e)^{1/2}" -- WRONG exponent | NONE -- phi_paasch uses eigenvalue ratios directly |
| M-22 | `sessions/archive/session-21c-paasch-collab.md` line 83 | "N(j) = (m_j/m_e)^{1/2}" -- WRONG | NONE -- N(j) not used in computation |
| M-22 | `sessions/archive/session-21c-r2-paasch-collab.md` line 109 | Same wrong exponent | NONE -- N(j) not used in computation |
| M-46 | `sessions/archive/session-19d-kk-collab.md` line 136 | "Freund-Rubin ratio Lambda/R = -6/7" -- WRONG | NONE -- project uses SU(3), not S^7 |
| M-46 | `sessions/archive/session-22-kk-collab.md` line 43 | Same wrong -6/7 ratio | NONE -- not used in any computation |

### POSSIBLE (concept present downstream, specific bad value may not have been used)

| Issue(s) | Concern |
|----------|---------|
| M-05 | Incomplete a_4 in paper could mislead agents, but tier0 uses complete formula |
| M-06 | Wrong Yukawa `e` in paper file, but knowledge-index and computations use correct form |
| M-38 | LQC bounce density wrong in paper, knowledge-index has correct equation |
| M-43 | GOE/GUE form factor swap could confuse spectral statistics analysis |
| M-58 | "4+2" spectral dimension could be misread as metric dimension |
| M-59 | Two conflicting f_k cutoff conventions coexist in knowledge-index |

### Key Finding: NO COMPUTATION RESULTS ARE AFFECTED

Despite 11 concrete contamination instances across the knowledge-index, meeting-minutes, and agent memories, **zero gate verdicts, zero theorem proofs, and zero numerical computation results are affected**. This is because:

1. **Tier0 computations derive formulas from first principles** (Gilkey a_2/a_4, eigenvalue solvers), never copying from researcher papers.
2. **Session 8 branching code** verified KO-dim signs at machine epsilon independently of any paper.
3. **The DIII/BDI distinction is a classification label** -- it does not change eigenvalues, Pfaffians (Z_2=+1 valid in both), or spectral sums.
4. **The Paasch N(j) exponent** is not used in any computation -- phi_paasch uses eigenvalue ratios from D_K directly.
5. **The Freund-Rubin ratio** is for 11D S^7 compactification, not the project's 12D SU(3) framework.

### Recommended Remediation Priority

1. **HIGH**: Fix knowledge-index proven_10 (line 88), open_channels (line 4517), and eq context (line 9209) to say "BDI" instead of "DIII".
2. **HIGH**: Fix knowledge-index eq_422 context (line 10217) to use correct N(j) = (m_j/m_e)^{2/3}.
3. **MEDIUM**: Fix `.claude/agent-memory/connes-ncg-theorist/MEMORY.md` lines 210-211 to remove wrong J^2=-1 claim.
4. **MEDIUM**: Clean up stale "class DIII" references in agent memories (baptista, KK, quantum-acoustics).
5. **LOW**: Add disambiguation note to knowledge-index for the two f_k cutoff conventions.
6. **NO ACTION NEEDED**: Meeting-minutes are historical records. The wrong values in Sessions 16, 19d, 21c, 22 are corrected by later sessions. Do not retroactively edit meeting minutes.
