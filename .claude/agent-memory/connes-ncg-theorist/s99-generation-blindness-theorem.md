---
name: Generation-Blindness Obstruction + fermion-mass reframing (§VII.BL)
description: STAGE-3-PERMANENT theorem — homogeneous D_K is multiplicity-scalar so the Yukawa hierarchy CANNOT be an A_K-built form; it requires an external non-LI eps_LX. The permanent reframe of the fermion-mass problem.
type: reference
---

## §VII.BL — Generation-Blindness Obstruction (STAGE-3-PERMANENT)

Co-authored by connes (Stage-0, with kaluza-klein-theorist), S97 W-2 workshop. Promoted STAGE-1→STAGE-3-PERMANENT at S99 W3-1 (Stage-2 cross-axis PASS-AND, audit `0f0c4f65`, axis-A vdd + axis-B dirac, BOTH non-authors; the connes axis-A leg was re-dispatched because I was a Stage-0 co-author — Stage-2 item-3 violation).

**The theorem.** `D_K` left-invariant on SU(3) ⇒ Peter-Weyl rep is multiplicity-scalar `π(a)=⊕π_{(p,q)}(a)⊗1_{m(p,q)}`. Generations = the multiplicity index (Z₃-triality `t=(p−q) mod 3`). Therefore EVERY A_K-built form — inner fluctuation `A=Σaᵢ[D_K,bᵢ]`, real image `ε'JAJ⁻¹`, twisted-inner `Ω¹_σ` — is scalar on each `ℂ^{m(p,q)}`, hence CANNOT lift the generation degeneracy. `R_cross=1.019704`, `n_distinct=2` EXACT at all L_max. This is WHY S97-YUKAWA-FAMILY-DERIVE gave democratic 1:1:1 (FAIL vs PDG 1:0.0595:0.000288).

**Two walls.** (W1) Reality `[J,D_K]=0` forces t=1 ≡ t=2 spectra (BDI conj (p,q)↔(q,p)) — SATISFIABLE, INNOCENT, never the obstruction. (W2) Homogeneity (left-invariance) ⇒ multiplicity-scalar — this IS the obstruction. (W3) inner-fluct impotence is the consequence.

**Twisted escape DEAD by Skolem–Noether.** A_K=ℂ⊕ℍ⊕M₃(ℂ): three simple summands ℝ-dims {1,4,18}, pairwise non-iso, distinct centers ⇒ every σ∈Aut(A_K) block-inner ⇒ multiplicity-scalar. `Aut(A_K)` is multiplicity-blind. (I re-derived via Sage at S99 W3-1.)

## The permanent reframe (use this for ALL future fermion-mass work)

The hierarchy is NOT in the bare D_K spectrum — by THEOREM. It must be an external non-left-invariant deformation `ε_LX` on the multiplicity bundle `⊕ 1_{V_{(p,q)}}⊗M_{m(p,q)}(ℂ)` (the complement of the Hochschild 1-cochain `[D_K,−]` image), reality-compatible (`[J,D_K+ε_LX]=0` block-by-block), order-one-constrained, but OUTSIDE every A_K-module. So the hierarchy is necessarily a threshold/transit/localization effect — NOT a tree number (consistent with S62 tree-Yukawa-vanishes PROVEN). See [[s96-dk-df-recovery]] (D_K≡D_F), [[s62-results]] (tree vanishes).

## Standard NCG vs framework (the scoping that matters)

Connes 2006 (paper 09 §4.1): in STANDARD NCG the Yukawas Y_ν,Y_e,Y_u,Y_d and M_R are FREE finite-geometry parameters — axioms fix algebra/H_F/gauge group/hypercharges/ν_R-existence but NOT the magnitudes. The framework's departure (D_K≡D_F, capstone §1.1) PROMOTES them to SU(3)-spectral data → makes the hierarchy a falsifiable prediction → and that prediction FAILED democratically. So the framework is STRICTLY stronger than Connes-SM here, and §VII.BL is the price.

## S99 panel — my candidate mechanisms for ε_LX (5, ranked)

Deliverable: `sessions/archive/session-99/session-99-fermion-mass-connes.md`. Best bet = **Connes-distance hierarchy**: mass_i ~ exp(−d_i/ℓ), the 3 generation-states at different Connes distances on the multiplicity bundle. Cheapest (machinery built: S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY=0.980). Sharp signature I derived: charged-lepton log-mass spacings WIDEN, ratio (d_e−d_μ)/(d_μ−d_τ)=1.89 (NOT equal).

**Honest Sage negatives (S99, reusable):**
- Generic rank-1 (democratic J₃, eigvals 0,0,3) + GENERIC perturbation ε gives light/heavy ≈ mid/heavy ≈ O(ε) — i.e. (ε,ε). Data needs (ε²,ε): factor ~200 between the two light steps. ⇒ the perturbation must be STRUCTURED, not generic.
- Single-param FN with λ_C=0.225, charges (e,μ,τ)=(2,1,0): μ/τ matches within 15%, but e/τ is 9× off. Approximately power-law; needs O(1) coefficients. ε from μ/τ=0.244, from e/τ=0.130 — no single ε fits both.

Other candidates: seesaw-textured charged sector (m_D²/M squaring turns ~14 spread into ~200 — route to hawking/KK heavy partners); Pati-Salam quadratic fluctuations (order-one fails 4.000) as the ALGEBRAIC origin of ε_LX — but PRODUCT of multiplicity-scalars is STILL multiplicity-scalar, so PS quadratic fluctuations from A_K alone are ALSO blind; only the ENLARGED A_K^PS=ℂ⊕ℍ_L⊕ℍ_R⊕M₄(ℂ) re-runs Skolem–Noether and could make ε_LX inner.

## S99 transit↔connes adjudication (Sage-exact, REUSABLE structural fact)

transit asked: does reality [J,ε_LX]=0 permit a complex triality-odd PHASE (needed to split 2↔3 since C₂(1,0)=C₂(0,1)=4/3 EXACTLY — fund/antifund share Casimir)? My verdict (Sage):
- Model ε_LX Hermitian on t=1↔t=2 doublet; J = swap∘conj (BDI, J²=+1). Reality `J ε_LX J⁻¹ = σ_x conj(ε_LX) σ_x = ε_LX` forces **d₁=d₂ on diagonal** (W2 reasserts) but leaves **off-diagonal w UNCONSTRAINED, phase included**.
- Eigenvalues of [[d,w],[w*,d]] = d±|w|: depend on |w| ONLY, not arg(w). ⇒ MASS split needs |w|≠0 (REAL w_r suffices); **arg(w) = triality-odd phase lives in the diagonalizing unitary = PMNS/CKM + CP**, NOT in masses.
- **KO-class-specific**: checked J²=−1 (DIII) → reality forces w REAL (phase KILLED) + d₁=d₂. So **CP phase survives BECAUSE framework is BDI (J²=+1); would die in DIII.** Permanent KO-class fact.
- Joint result: transit's DIAGONAL a_gen=exp(−S_gen) can't split 2↔3 (reality forces d₁=d₂ — confirms his Casimir wall from reality side, 2 routes 1 wall); the OFF-DIAGONAL |w| splits masses; the same off-diagonal's PHASE gives PMNS+CP (the S34 "inter-sector Bogoliubov" conjecture). Recorded in deliverable §4.0.

## S99 order-one SILENCE on generation texture (Sage, REUSABLE)

baptista Q1: does an off-diagonal-in-generation D_F satisfy order-one? VERDICT (Sage, exact): with an order-one-ADMISSIBLE INTERNAL block, [[D_F,a],Jb*J⁻¹]=0 IDENTICALLY for ARBITRARY generation texture (all y_ij free — diag/off-diag/complex). Reason: **index-disjointness** — order-one constrains the INTERNAL (color/isospin) index (Connes 2006 §5.2: Yukawas color-diagonal, M_R lepton-only); A_K acts as IDENTITY on the generation/multiplicity index ⇒ order-one is SILENT on the generation texture. CAUTION: conditional on the internal block being SM-admissible — a bad internal block (e.g. σ_x not commuting with diagonal a) gives a SPURIOUS nonzero residual (I made this error first, corrected it). So: the generation texture freedom is real but rides on an order-one-admissible internal structure.

## S99 PANEL FOUR-LENS SYNTHESIS (the completed picture — use for any future fermion-mass work)

All 4 lenses triangulated on ONE complex amplitude:
  a_gen = |O_g| = exp(−d_i/ℓ) = Γ(ω_i)·exp(−2πω_i/κ)  ×  exp(iΘ_i)
          └──── MODULUS (one exponent, 3 languages) ────┘   └ PHASE ┘
- MODULUS (gen-2/3 MASS split + e-vs-heavy envelope): baptista fiber-overlap O_g = my Connes-distance ladder exp(−d_i/ℓ) = hawking greybody Γ(ω)exp(−2πω/κ). One exponent, three languages (d_i/ℓ ↔ 2πω_i/κ ↔ k·C₂). My piece: algebraic HOME (multiplicity-acting complement, §VII.BL) + METRIC (Connes distance) + reality/order-one admissibility proof.
- PHASE (μ↔τ split + PMNS/CKM + CP): transit triality-odd Θ = baptista s_φ-phase (2nd Z₃ of Z₃×Z₃). My piece: proof it SURVIVES reality (BDI-specific, §4.0), lives in mixing not mass.
- hawking answered MY §3.4 cross-q (KK threshold generation-dependent?): KK tower sum is BLIND (same §VII.BL obstruction, sets only sector scale M₀); the greybody exp(−2πω/κ) supplies the grading on the ε_LX-split ω_i; sector-dependent κ (lepton 1.89/up 1.29/down 0.78) gives the non-universal slopes.
- I RETIRED my own §3.4 seesaw-squaring speculation: KK threshold blind ⇒ factor-200 from greybody exponentiation, not a charged seesaw. Right instinct (exponentiation), wrong vehicle.
- Durable claim: §VII.BL locks the DIAGONAL reality-degenerate (generation-blind, d₁=d₂); ALL hierarchy+mixing+CP lives OFF-DIAGONAL in ε_LX; the 4 lenses each construct that one off-diagonal ε_LX from a different start (geometric overlap / dynamical freeze-in / horizon greybody / multiplicity-bundle metric). My §3.1 Connes-distance is the best first compute (widening ratio 1.89 falsifiable).

## S114 W3-1 — the D4 right-regular SU(3)_R decider (SHAPE-branch genus, INFO)

CF-S114-YUK-RIGHTREG-CONNECTION (audit `e392b832483e8f75…`). The SHAPE-branch homogeneity-obstruction genus has four doors; D1–D3 (A_K-built / Casimir-graded / γ₉-traced) are CLOSED by permanent theorems. D4 = the open right-regular door: can a fermion-mass SHAPE handle be built from the substrate's OWN SU(3)_R right-isometry on the multiplicity leg (internal) rather than the external ε_LX?

**Construction (REUSABLE Peter-Weyl fact).** L²(SU(3),S) = ⊕ V_{(p,q)} ⊗ ℂ^{m(p,q)} ⊗ ℂ¹⁶, m(p,q)=dim(p,q). LEFT-regular SU(3)_L acts on the carrier V_{(p,q)}; RIGHT-regular SU(3)_R acts on the multiplicity leg ℂ^{m(p,q)}, which carries the CONJUGATE irrep (q,p). So the right-regular Cartan on the leg of sector (p,q) = `i·ρ_{(q,p)}(e_a)` — the SAME `get_irrep` machinery at the conjugate sector. No new rep theory. (Verified Sage A2 WeylCharacterRing + numerically.)

**4-part discriminator @ τ_fold (all machine-exact):**
- (i) `[L_g,Y_R]` = 7.25e-17 PASS (tensor-factor disjoint: L on carrier, R on leg).
- (ii) sign_flip = True for 4/6 BDI-real Cartan dirs (EVERY dir with an H₈/hypercharge component; pure-H₃/isospin gives uniform sign). The flip is INTER-sector (rep eigenvalue of t=0 leg (1,1), t=1 leg (1,0), t=2 leg (0,1) — three distinct-triality sectors). ADMISSIBLE not Schur-locked because R_H ∉ A_K-image (center-char pre-flight t(O)=0 PASSES; unlike A_K-built |f|² which is t(O)=0 BUT Schur-scalar).
- (iii) GENERATION-DIAGONAL. Within ONE leg = conj (q,p), EVERY weight shares triality (q−p) mod 3 ⇒ Y_R acts within one generation class, block-diagonal across triality. Cross-generation (off-diagonal) needs a ROOT generator t(O)=±1, NOT in the center-neutral Cartan. So Y_R is reality-compatible but caught by the SAME diagonal J-lock as the d₁=d₂ kernel — does NOT evade it.
- (iv) LOAD-BEARING membership: residual ‖Y_R − P_{Ω¹}(Y_R)‖/‖Y_R‖ = **1.000000 EXACT** (all 3 classes). REUSABLE structural proof: every Ω¹_{D_K}(A_K) form is (carrier⊗spinor op)⊗I_leg (A_K acts LEFT-only on the 16-spinor, identity on carrier AND right-leg); Y_R = I_car⊗R_H_leg⊗I_spin acts ONLY on the leg ⇒ Y_R ∈ span(Ω¹) iff R_H_leg ∝ I_leg, but R_H_leg is TRACELESS ⇒ never. POSITIVE CONTROL passes (genuine Ω¹ form → residual 1e-14), so the test discriminates.

**Verdict INFO (NOT FAIL, NOT PASS) — the precise boundary.** Y_R is provably OUTSIDE the left A_K-calculus (residual=1 ⇒ NOT the external ε_LX "in new dress", so NOT Reading-B/FAIL) but generation-DIAGONAL (NOT the clean off-diagonal SHAPE handle, so NOT Reading-A/PASS). Whether the right-regular SU(3)_R action is an admissible substrate fermion DOF without enlarging A_K / dropping Axiom 5 is a representation-pinning choice NOT fixed by the 7 axioms. Dual priors UNCHANGED (0.40 internal / 0.60 external). **D4 stays OPEN.** Forward: a 3×3 cross-generation operator needs the right-ROOT generators (t(O)=±1, off-diagonal across triality); their admissibility is the representation-pinning workshop owed. For W3-3 SHAPE-wall §VII landing: D4 NOT covered, scope qualifier stays "{A_K-built ∪ Casimir-graded ∪ γ₉-traced}; right-regular SU(3)_R (D4) OPEN". Script `computations/session-114/s114_yuk_rightreg_connection.py`.

**ROCm gotcha (REUSABLE):** `torch.linalg.qr`/`lstsq` return NaN (qr) / need MAGMA (lstsq) on RANK-DEFICIENT COMPLEX matrices on the RX 9070 XT ROCm build. Ω¹ basis is heavily rank-deficient (rank 103 of 196 raw forms on the (1,0) block — the bounded dim of the left calculus). Use numpy SVD (rank-truncated U_r U_rᴴ projector) for rank-deficient complex projections; reserve GPU for well-conditioned ops.

## S115/S116 — PMNS/CKM symmetric-attractor reframe (verdict-INDEPENDENT structural fact, REUSABLE)

The S115 forced internal `A_K⋊SU(3)_R` Z₃-circulant is the **symmetric attractor** of the multiplicity-scalar structure: `F₃` diagonalizes ANY circulant (coefficient-INDEPENDENT) ⇒ tri-maximal `|U_ij|²=1/3`, `J=1/(6√3)=0.0962250`. Two fibers, two symmetric fixed points: quark `M₃(ℂ)`-shared → two circulants → `U_mix=F₃†F₃=1`, `J=0` (identity attractor); lepton `ℂ⊕ℍ` → coset-diagonal `U_L` → tri-maximal, `J=0.0962` (DFT attractor). **THEOREM (rephasing-invariance, S115, machine-exact):** a coset-diagonal `U_L=diag(e^{iα})` leaves `J` INVARIANT (`J_scan_spread=8.3e-17`) — the ℂ⊕ℍ sector-asymmetry is **J-inert**; only a NON-coset-diagonal `U_eL` (= off-diagonal-in-generation charged-lepton ε_LX, the §VII.BL-external deformation) can break tri-maximality.

**The 2.9× vs 3124× is ATTRACTOR-DISTANCE, not a derivation handle.** Both residuals = distance from the SAME symmetric forced texture to the data: small-mixing CKM (`J=3.08e-5`) is FAR from any symmetric attractor (tri-max overshoots 3124×, identity undershoots to 0); near-maximal PMNS (`J=0.0329`) sits only 2.9× from tri-max. The lepton "RESONANT-CONDITIONAL ~2.9×" is the data landing near a symmetric attractor, NOT leptons carrying a handle quarks lack. **The 2.9× is a J-only artifact:** tri-maximal overshoots `sin²θ₁₃` by 15× (`1/3` vs NuFIT `0.02203`) — the single-number near-miss hides an order-of-magnitude detail miss. ε_LX epistemic status is MACHINERY-keyed (non-LI multiplicity-bundle deformation outside `Ω¹_{D_K}(A_K)`), sector-INDEPENDENT: cannot be a "fit" for quarks (CKM FALSIFIED, V_us FAIL) and a "derivation" for leptons. My WALLED R1 in `sessions/session-116/workshops/s116-w2-pmns-rescue.md`. The attractor-distance + J-inert-coset + 15×-θ₁₃ facts hold regardless of the verdict.

## S116 W2 PMNS-rescue R2 (my Turn A) — two REUSABLE corrections/reframes (verdict-INDEPENDENT)

1. **J-inertness CORRECTION (concede, reusable):** `J_scan_spread=8.3e-17` is a COSET-DIAGONAL-SUBSPACE identity (3-real-param slice of U(3)), NOT a wash-out theorem. An off-diagonal `U_eL` DOES move J — neutrino-specialist's 1-param `R₁₂(b)` Sage table sweeps J 0.0962→0.0520→−0.0219 (crosses band b∈[0.5,0.9]); S96-MATTER-PMNS-3X3 lifts sin²θ₁₂/θ₂₃ monotonically from 0 with `‖[iK₇,M_lep]‖=0` preserved. My R1 "2.9× IS the wall" was OVER-STATED. Do NOT cite J-inertness as a mixing wall going forward; scope it to the coset-diagonal slice.
2. **MASS-PINNING reframe (the surviving WALLED core, reusable for ALL PMNS/CKM work):** the off-diagonal in `U_eL` is NOT a free dial — it is PINNED by charged-lepton mass-fitting (`PMNS=U_eL†U_ν`, `U_eL` diagonalizes `M_e=diag(log-gap)+ε_LX^e_offdiag`; lepton diagonal log-spacing ratio `ln(m_μ/m_e)/ln(m_τ/m_μ)=1.89` ≈ down-quark `9/5`). The fork is ORBIT-vs-PINNED-POINT: the orbit passes through the band (conceded); whether the MASS-PINNED point lands there is the S111 quark precedent verbatim (`V_us=0.3107/0.225=1.38` overshoot, slot-6 FAIL — mass-fitting forces off-diagonals LARGER than mixing needs).
3. **Spectrum-pinned M_R DICHOTOMY (NEW, closes the seesaw-rescue claim):** a TRULY spectrum-supplied `M_R` (B-branch D_K fold energies) is multiplicity-SCALAR by §VII.BL ⇒ generation-DIAGONAL `diag(M_0,M_1,M_1)` ⇒ supplies ZERO PMNS mixing (seesaw `m_ν=M_D^T M_R⁻¹ M_D` with diagonal M_R: all mixing from off-diagonal M_D=external ε_LX). Either M_R diagonal (no mixing, rescue misattributed) OR M_R off-diagonal (NOT spectrum-pinned = MORE external input). Dirac/Majorana split is a MASS-channel DOF, §VII.BL-blind as a MIXING handle. sub-(b): W2-1 this session holds D4 crossed-product CLOSED-EXTERNAL-AS-A-COUPLING (g_R + forced Z₃-circulant, which WASHED OUT); the rescue's off-diagonal is DOUBLY external (beyond Ω¹ AND beyond the forced circulant). Discriminator = W2-3 `S116-W2-LEPTON-PMNS-TEXTURE`: mix_grp≥3 SIMULTANEOUS with m_e:m_μ:m_τ at spectrum-pinned M_R (Track A live-but-external) vs over-rotation/detachment (Track B wall). S96 R-shortfall (peak 6.87 ≪ [17,66], no simultaneous landing) is the standing prior toward Track B.
