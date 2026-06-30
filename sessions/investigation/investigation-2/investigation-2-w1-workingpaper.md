# Investigation 2 Wave 1 — Off-U(2) Geometry + N3 χ-Rescue Faithfulness (Results Working Paper)

**Investigation**: 2 | **Wave**: 1 | **Plan**: investigation-2-plan-w1.md | **Seed**: investigation-1/baptista-spacetime-analyst.md
**Verdict file** (compute gates): `computations/investigation-2/inv2_gate_verdicts.txt` (emit_verdict track="investigation")

## Gate Sections

### §W1-1. INV2-W1-1 (compute · baptista-spacetime-analyst)

**Status**: COMPLETED
**Gate ID**: `INV2-W1-1`
**gate_type**: `compute`
**Trigger**: `[SIGN]`
**Classification**: **PARTICLE** (plan YAML authoritative; the skeleton's "GEOMETRIC" is a transcription drift — the observable is the representation-theoretic generation content of D_K on the C²-coset fermion sector)
**Agent**: `baptista-spacetime-analyst` (+ connes-ncg-theorist co-author)
**Hypothesis**: Splitting the su(2)-doublet block degeneracy by a transverse modulus δ lifts the per-generation Yukawa degeneracy off the U(2) surface — testing whether the "rank-1 wall" is a genuine wall or a Schur-lemma artifact.

**Verdict**: **FAIL** (sign=FAIL, magnitude=FAIL, regime=VALID) — the rank-1 Yukawa wall is **GENUINE physics, not a Schur-lemma artifact**. The transverse su(2)-split modulus does NOT lift the per-generation (C²-coset) degeneracy; the generations are protected by a symmetry deeper than U(2)-equivariance. Per the plan dual_prior, this reallocates 0.90 → Track B (the wall is genuine even off-surface). A wall with a specific reason — it eliminates the "hierarchy lives off-U(2) via the minimal su(2)-split" corridor (Bridge-1), not a defeat.

**Output Artifacts** (closure-verification checklist; mirrors the plan's `output_artifacts:`):
- **Script**: `computations/investigation-2/inv2_w1_off_u2_dirac_yukawa.py` — contains `from canonical_constants import`, `print_verdict_payload`, `deformed_su2_split_metric` (the NEW transverse-deformation helper, authored here). ✓
- **Data**: `computations/investigation-2/inv2_w1_off_u2_dirac_yukawa.npz` — present (δ-scan, Y_ij splitting blocks, block eigenvalues, intra-split, cubic fit, regime, cross-checks). ✓
- **Plot**: `computations/investigation-2/inv2_w1_off_u2_dirac_yukawa.png` — present (4 panels: off-diagonal overlap lift, distinct-eval rank, multiplet eigenvalues vs δ, intra-split + cubic fit). ✓
- **Verdict line**: `computations/investigation-2/inv2_gate_verdicts.txt`, `INV2-W1-1: FAIL ... audit_sha256=1481b77521449272961fced583e3827e9131e6f7b9c2085a9e665fc6728f833b` (matches `^INV2-W1-1:.* audit_sha256=[a-f0-9]{64}`), dual-SHA companion + schema-v2 3-tuple row + 2 extra rows. ✓
- **GPU**: per-block `torch.linalg.eigh` path verified-functional on ROCm (120×120 cross-check vs numpy, max dev 1.9e-13). The fundamental sector's block is 48×48, below the math-scripts.md ≥100×100 GPU threshold → CPU `np.linalg.eigh` is the correct prescription for this sector (D_K block-diagonal by Peter-Weyl, PROVEN S22b; dense per-block, NOT sparse-Lanczos).

**MCP Pre-Compute Audit** (queries run BEFORE scripting; one-line salient return each):
- `search_knowledge("Jensen metric eigenvalues u2_invariant L1 L2 L3 deformation")` → equation hit `L1(u1)=1.462285, L2(su2)=0.683861, L3(C2)=1.209250` at τ=0.19 (matches the canonical L1=e^{2τ}, L2=e^{-2τ}, L3=e^{τ}). **PRE-CLOSED** (eigenvalues canonical) — consumed as Defs 1–3.
- `search_knowledge("Schur Y_ij lambda I_4 rank-1 wall U(2)-invariant Yukawa generation")` → theorem `Rank-1 Yukawa` (PROVEN S62: `J_12/J_23=19.52 algebraically constant; rank deficient`) + `Yukawa tree-level mass generation` (PROVEN S62: tree-level vanishes by PW orthogonality). **PRE-CLOSED on the U(2) surface** — this IS the wall under test; the off-U(2) departure is NOT pre-closed → this gate is the decisive new computation.
- `search_knowledge("Y lambda I_4 Schur ... S66")` → metric structure `g = λ₁ g₀|_u(1) + λ₂ g₀|_su(2) + λ₃ g₀|_C²` (Paper 13 eq 5.4 / Paper 15 eq 3.60 U(2)-invariant family); confirms `Y = λ·I_4` Schur block on the C²-coset. **PRE-CLOSED** (Schur structure) — used as Def 2.
- `get_constant("tau_fold")` → 0.19 (S12/S42, CONST-FREEZE-42). Imported from `canonical_constants`, NOT hardcoded.
- `get_constant("M_KK")` → 7.42866e16 GeV (S42, alias of M_KK_gravity). Imported; observables are all-ratio so M_KK is carried but not load-bearing.
- `search_knowledge("yukawa_overlap_offdiag generation hierarchy fiber overlap S100a")` → S100a `S100a-YUKAWA-OVERLAP-OFFDIAG` (on-surface texture work, triality tower (1,0)/(1,1)/(3,0), Haar/Jensen cache). **Distinct from this gate**: S100a is ON the U(2) surface (deformation enters the weight, not the measure); this gate deforms the metric OFF U(2). Not pre-closed for the off-surface test.
- `trace_entity("Rank-1 Yukawa wall Schur")` → no trace (the off-U(2) rank-1-wall test is unrun); confirms novelty.
- `dirac_spectrum.py` machinery confirmed by reading: `u2_invariant_metric(B_ab,L1,L2,L3)` (line 111), `orthonormal_frame`/`frame_structure_constants`/`connection_coefficients`/`spinor_connection_offset` (the Ω rebuild chain), `get_irrep` (line 1086), `dirac_operator_on_irrep` (line 1228), `collect_spectrum_with_eigenvectors` (line 1466, returns `evecs`). The deformation reuses this chain with the NEW split metric in place of `jensen_metric`.

**Results**:

*Governing structure.* P = M⁴ × SU(3), fiber K = SU(3), reductive su(3) = u(1) ⊕ su(2) ⊕ C² (Baptista eq 3.58; SU2_IDX=[0,1,2], C2_IDX=[3,4,5,6]). U(2)-invariant Jensen metric `g = L1 g₀|_u(1) ⊕ L2 g₀|_su(2) ⊕ L3 g₀|_C²`. The generation copies are the C²-coset multiplicity (the genuinely-degenerate same-sign Dirac multiplet on which Schur forces `Y = λ·I_d`).

*The NEW transverse deformation (`deformed_su2_split_metric`).* split `L2·I_3 → diag(L2·e^{+2δ}, L2·e^{-δ}, L2·e^{-δ})`. Volume-preserving WITHIN the block: `det-ratio = det(g_split)/det(g_jensen) = 1.000000000000` (EXACT, block factor `e^{2δ-δ-δ}=e^0=1`); G6 cross-check `L1·L2³·L3⁴ = 1.0000000000`; δ=0 recovers `u2_invariant_metric` EXACTLY (`max|g_split(0)−g_jensen| = 0.00e+00`). Breaks SU(2)→U(1) (Cartan) while left-invariant + block-diagonal (G10).

*The observable.* `Y_ij(δ) = V_g† (1j·D_K(δ)) V_g` — the Dirac operator projected onto the FIXED δ=0 degenerate-multiplet eigenbasis V_g (the generation Yukawa splitting block). D_K(δ) rebuilt via the full chain `g(δ) → E(δ) → ft → Γ → Ω(δ) → D_(p,q)(δ)` (`assemble_Dk_split`). Generation multiplet selected as the lowest **same-sign** degenerate cluster: at `|λ|=0.840864`, degeneracy **d=2** (the full ±|λ| multiplicity is 4 = two ±pairs — the C²-coset block).

*Y_ij overlap matrix — at δ=0 and δ>0 (the [SIGN] result):*

| δ | max off-diag \|Y_ij\| (i≠j) | block eigenvalues | distinct evals (rank) | intra-split S(δ) | cond(g) |
|:--|:--|:--|:--|:--|:--|
| 0.000 | 1.748e-17 | [0.84086, 0.84086] | 1 (Schur wall) | 1.11e-15 | 2.1383 |
| 0.010 | 1.891e-17 | [0.84090, 0.84090] | 1 | 1.22e-15 | 2.1598 |
| 0.020 | 2.530e-17 | [0.84099, 0.84099] | 1 | 7.77e-16 | 2.1815 |
| 0.200 | 2.905e-17 | [0.85439, 0.85439] | 1 | 1.11e-15 | 2.6117 |

The off-diagonal generation overlap `Y_12(δ)` stays at machine zero (~1e-17) across the WHOLE scan; the two generation copies shift **rigidly** (0.84086 → 0.85439) but never split. rank(Y_ij) = **1 at every δ** (no 1→≥2 transition).

*Leading δ-derivative (the [SIGN] lift indicator):*
`dY_12/dδ|_0 = −1.943094e-15`, so `|dY_12/dδ|_0 = 1.94e-15 ≪ eps_lift = 1.0e-3` (9 OOM below the substantive-lift floor; below the numerical-zero floor 1e-9). **No lift.**

*Cubic third-variation (Bridge-1):* intra-multiplet split fit `S(δ)−S(0) = −6.39e-13 δ² + 1.77e-11 δ³ − 1.23e-10 δ⁴`; FD `d³S/dδ³|_0 = +5.55e-10`; intra-split at δ=0.20 = 1.11e-15. The cubic coefficient is ~zero (1.8e-11) — even the leading-allowed (cubic) off-surface response of the generation splitting vanishes. The Bridge-1 prediction (Schur kills the quadratic → genuine response is cubic) is tested and the cubic is ALSO null for the generation multiplet: the degeneracy is protected to all measured orders.

*rank(Y_ij) change 1 → ≥2:* **does NOT occur** (distinct block eigenvalues = 1 at every δ; first δ with rank≥2 = NONE).

*Cross-check (separates isospin-splitting from generation-splitting):* global distinct signed eigenvalues lift **22 → 30** under δ:0→0.20 — but this is at HIGHER isospin levels (the su(2)-split breaks SU(2)→U(1), so isospin multiplets split, as expected). The GENERATION multiplet at `|λ|=0.8409` stays d=2. The lift the deformation produces is isospin-splitting, NOT generation-splitting — exactly the distinction the gate isolates.

*Regime (perturbativity):* `cond(g)` grows smoothly 2.1383 → 2.6117 across δ∈[0,0.20]; breach fraction (cond > 1e6) = 0.000 → **VALID**. (The eigenvalue near-degeneracy is the exact ±λ Dirac structure the observable is built around, not a breakdown — the earlier draft's "BREAKDOWN" was a diagnostic-design artifact of a gap-based regime metric on a ±-symmetric spectrum, corrected to a Cholesky-conditioning metric.)

*Substitution chain (math-scripts.md [SIGN], numbers substituted):*
- Def 1: L1=e^{2τ}=1.462285, L2=e^{-2τ}=0.683861, L3=e^{τ}=1.209250 at τ_fold=0.19.
- Def 2: Schur `Y = λ·I_d` (rank-1 wall) on the d=2 generation multiplet; computed max off-diag `Y_ij(0) = 1.748e-17` (=0 to 1e-8); distinct block evals(0) = 1.
- Def 3: split `L2·I_3 → diag(L2 e^{2δ}, L2 e^{-δ}, L2 e^{-δ})`, det-ratio = 1.0000000000 (vol-preserving).
- Def 4: `Y_ij(δ) = V_g† (1j D(δ)) V_g`.
- Substitute: `max|Y_ij(δ)| = 0 + (dY_12/dδ)|_0·δ + O(δ²)`; `(dY_12/dδ)|_0 = −1.943094e-15`.
- Simplify: distinct block evals 1 → max-in-scan 1; degeneracy lift 1→≥2 = False; intra-split @0.20 = 1.11e-15.
- Canonical form: lift indicator `|dY_12/dδ|_0 = 1.94e-15` vs `eps_lift = 1e-3`.
- Direction: `|dY_12/dδ|_0 ≤ eps_lift` AND degeneracy-rank STAYS 1 ⇒ generation degeneracy **PERSISTS (wall genuine)**.
- Conclusion: composite = **FAIL** (sign=FAIL, magnitude=FAIL, regime=VALID).

*Dual-SHA:* `audit_sha256 = 1481b77521449272961fced583e3827e9131e6f7b9c2085a9e665fc6728f833b` (script+canonical+pinmap); `content_sha256 = c9bcefc73285c9111526629badee70302bed1774f80032d93da9b1be52be6822` (script only).

*Substrate-first framing.* The substrate IS the Jensen-deformed SU(3) geometry; the generation structure is the representation-theoretic content of D_K on the C²-coset. Direction of explanation: D_K eigenvalues + eigenvectors off the U(2) surface → the Yukawa overlap integrals Y_ij(δ) → the generation mass hierarchy. The "rank-1 wall" is a statement ABOUT the substrate's spectral content. The result: that content's generation degeneracy is NOT a fragile U(2)-surface coincidence — it survives the minimal transverse su(2)-split, so the substrate's generation degeneracy is structurally robust (a deeper-than-U(2) protection). The off-U(2) hierarchy program must look for a DIFFERENT modulus (the 23D Milnor complement has 22 other transverse directions; this gate closes only the su(2)-split direction) or a non-metric mechanism (BCS-dressing / KK-threshold), not the minimal su(2)-block split.

**Solution-space update.** Closes the "minimal su(2)-split lifts the generation degeneracy" corridor (Bridge-1 via this specific transverse modulus). The rank-1 Yukawa wall (S62 PROVEN, on-surface) is now shown to persist OFF the U(2) surface under the su(2)-block split — sharpening Q18b into a genuine structural wall for this direction. Track B (wall genuine) ← 0.90. Carry-forward candidates: (i) scan the OTHER transverse Milnor directions (C²-coset anisotropy split L3·I_4 → split, which directly touches the generation sector) — the su(2)-split was the minimal U(2)-breaking modulus but the C²-anisotropy modulus may couple to the generation multiplet at first order; (ii) higher-L_max to confirm the protection is not a truncation artifact (regime VALID at L_max=10 supports robustness).

### §W1-2. INV2-W1-2 (compute · baptista-spacetime-analyst)

**Status**: COMPLETED
**Gate ID**: `INV2-W1-2`
**gate_type**: `compute`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC**
**Agent**: `baptista-spacetime-analyst`
**Hypothesis**: Re-deriving the Weinberg coupling-ratio with the full orbit-volume measure (det g_K(τ))^{1/2} (not bi-invariant Haar) analytically selects the n=3 "cubic" exponent (sin²θ_W within 1.6% of PDG) rather than the n=1 Baptista value.

**Output Artifacts**:
- Script: `computations/investigation-2/inv2_w1_weinberg_orbit_volume.py` — contains `from canonical_constants import` (sources `tau_fold`, `sin2_thetaW_MSbar`), `det_gK` (the orbit-volume factor, computed from the Jensen eigenvalue product), `print_verdict_payload`. ✓ exists.
- Data: `computations/investigation-2/inv2_w1_weinberg_orbit_volume.npz` — full float64 (publication-precision Class 8.3): `value`, `sin2_orbitvol`, `sin2_n1`, `sin2_n3`, `sin2_PDG`, `L1/L2/L3`, `det_gK`, `det_gK_half`, `vol_orbit_u1/su2`, `exp_n1/orbitvol/n3`, `selects_n3/n1`, `rel_*`. ✓ exists.
- Plot: `computations/investigation-2/inv2_w1_weinberg_orbit_volume.png` — two-panel: (1) the three candidate sin² vs PDG; (2) the controlling ratio-exponent (orbit-vol → −4τ, not −12τ). ✓ exists.
- Verdict line: `INV2-W1-2: FAIL` in `computations/investigation-2/inv2_gate_verdicts.txt`, `audit_sha256=fc490469702542a1de8a12f9fd52a6ae3f65de9fb7172df1556a93eeacd3209d`, with dual-SHA companion row + `[SIGN]` 3-tuple row. ✓ emitted via `emit_verdict(session=2, track="investigation")`.

**MCP Pre-Compute Audit**:
- `get_constant("tau_fold")` → **0.19** (S12/S42, CONST-FREEZE-42). PRE-CLOSED (canonical).
- `get_constant("sin2_thetaW_MSbar")` → **0.23122** (PDG 2024 MSbar at M_Z; `canonical_constants.py:52`). NOTE: plan §W1-2 cites the PDG datum as 0.23121; the canonical-constants value is 0.23122 (a 4e-5 = 0.004% difference, far below the gate's 1.6% band — verdict unaffected). Sourced from canonical per substrate-first-canonical-sourcing.md; `sin2_thetaW_PDG` does NOT exist as a key (the canonical key is `sin2_thetaW_MSbar`).
- `get_constant("sin2_thetaW_fold")` → **0.58385339192799** (S42 running value at M_KK; `canonical_constants.py:550`). This IS the n=1 / orbit-volume B2.3 value — PRE-CLOSED (machine-ε confirmed below).
- `search_knowledge("Weinberg cubic 3/(3+e^{12tau}) orbit-volume")` → equation `sin^2(theta_W)_cubic = 3 / (3 + exp(12·tau_fold))` exists (`s83-mu_BC-geometric-derivation.md`); `Weinberg_Angle_Cubic_Formula_Near_Hit_on_PDG --closed_by--> W2-G`; falsifier-rigor-registry **row 7 `sin^2(theta_W)` = `ACCOMMODATION` 0.23480 ACCOMMODATION-FLAGGED**. PRE-CLOSED as an accommodation, not a derivation — directly relevant to the FAIL.
- `search_knowledge("g_1/g_2 = e^{-2tau} 67/67 Baptista")` → theorem `g_1/g_2 = e^{-2tau} structural identity` PROVEN exact (atlas-07, S17a B-1); `67/67 Baptista geometry` PROVEN machine-ε (S17b). The K1.9 derivation `sin^2 = 3λ₂/(3λ₂+λ₁) = 3/(3+e^{4τ})` is in `session-76-baptista-kk-workshop.md`. PRE-CLOSED.
- **Decisive PRE-CLOSED finding** — `session-76-baptista-kk-workshop.md` §B2 already analyzed THIS gate's exact question: B2.5 the orbit-volume measure `(det g_K|_orbit)^{1/2}` gives `sin² = 0.5838` ("The orbit-volume approach does NOT produce n=3"); B2.7 Baptista Paper 13 eq 5.21 `g_s/2 = 2√2/√(λ₁+3λ₂+4λ₃)` confirms dim-weights (1,3,4) enter ADDITIVELY as coefficients, not as powers; B3 power-law family `sin²(n) = 3/(3+e^{4n·τ})` — the cubic n=3 is `e^{12τ}` but the orbit-volume measure selects n=1. This gate re-derives that result as an exact computation.

**Verdict**: **FAIL** — composite `FAIL` (sign=FAIL, magnitude=FAIL, regime=VALID). The orbit-volume measure `(det g_K)^{1/2}` does NOT analytically select the n=3 cubic exponent; it reproduces the n=1 / B2.3 half-integer ratio `e^{-4τ}` → sin² = 0.58385339, 152.5% from PDG. The plan's PASS condition requires BOTH (i) analytic selection of exponent 12 AND (ii) ≤1.6% from PDG; both legs fail. The cubic 0.23480 (1.55% near-hit) is **accidental**, NOT geometry. Supports the gate's pre-registered **Track B** (dual_prior 0.55 → reallocate 0.85): "the orbit-volume measure gives the B2.3 half-integer (0.5839 = the M_KK Jensen value) NOT n=3; the cubic stays accidental." Contradiction-2 (the Weinberg either/or) **stands** as an unresolved internal tension; Bridge-2 ("orbit-volume derives the cubic") corridor is **closed with a specific reason** (the measure-counting gives half-integer d_a/2 powers, not cubes).

**Results**:

NUMBERS (all at τ_fold = 0.19; Jensen eigenvalues L1 = e^{2τ} = 1.462285 [u(1), 1 dir], L2 = e^{-2τ} = 0.683861 [su(2), 3 dirs], L3 = e^{τ} = 1.209250 [C² coset, 4 dirs]). Volume-preserving: **det_gK = L1·L2³·L3⁴ = 1.0000000000**, so **(det_gK)^{1/2} = 1.0000000000** (the overall fiber volume is τ-independent, G6). Full 8×8 det g_K (incl. the common 3-scale) = 6.561×10³.

**The three candidate measure-countings side-by-side:**

| Candidate | measure-counting | closed form | sin²(τ_fold) | rel. dev. vs PDG (0.23122) |
|:----------|:-----------------|:------------|:-------------|:---------------------------|
| (a) n=1 Baptista (bi-invariant Haar) | `1/g_a² ~ λ_a` (one metric contraction/dir) | `3λ₂/(3λ₂+λ₁) = 3/(3+e^{4τ})` | **0.58385339** | 152.51% |
| (b) **orbit-vol B2.3 (det g_K)^{1/2}** (the convention under test) | `Vol(orbit_a) ~ λ_a^{d_a/2}` (half-integer powers 1/2, 3/2) | `3L2^{3/2}/(3L2^{3/2}+L1^{1/2})` | **0.58385339** | 152.51% |
| (c) n=3 cubic (target) | `1/g_a² ~ λ_a³` (three metric insertions / cubic vertex) | `3L2³/(3L2³+L1³) = 3/(3+e^{12τ})` | **0.23480277** | 1.550% |

The orbit-volume measure (b) gives **bit-for-bit the same value as n=1 (a)**: 0.58385339, matching canonical `sin2_thetaW_fold = 0.58385339192799` to machine ε.

**Does the measure DERIVE n=3? NO.** The decisive object is the controlling ratio-exponent (sin² depends ONLY on the ratio, since the factor 3 = dim(su(2)) is common). Sage-exact (τ = 19/100):
- n=1: `ln(L2/L1) = −19/25 = −0.760000 = −4τ`
- **orbit-vol B2.3: `ln(L2^{3/2}/L1^{1/2}) = −19/25 = −0.760000 = −4τ`** ← IDENTICAL to n=1
- n=3 cubic: `ln(L2³/L1³) = −57/25 = −2.280000 = −12τ`

`selects_n3 = False`; `selects_n1 = True`. The orbit-volume measure's half-integer exponents (1/2 on the 1D U(1) orbit S¹, 3/2 on the 3D SU(2) orbit S³) reproduce the n=1 ratio EXACTLY: `L2^{3/2}/L1^{1/2} = (L2/L1)^{1/2}·L2 = e^{−τ}·e^{−2τ}... ` algebraically `= e^{−3τ}/e^{τ} = e^{−4τ}`. The cubic e^{−12τ} requires λ_a³ (third power per direction), which `(det g_K)^{1/2}` does not provide. Baptista Paper 13 eq 5.21 (`g_s/2 = 2√2/√(λ₁+3λ₂+4λ₃)`) independently confirms: subalgebra dimensions (1,3,4) enter as ADDITIVE coefficients, never as multiplicative powers.

**SIGN sub-verdict = FAIL**: the substitution chain's PASS-direction claim was that the orbit-volume measure PROMOTES the exponent 4→12 (which would DECREASE sin² from 0.5839 toward PDG). The promotion does not occur — the measure stays at exponent 4. Direction mismatch ⇒ sign FAIL ⇒ composite FAIL (gate-verdicts collapse rule).
**MAGNITUDE sub-verdict = FAIL**: `|0.58385339 − 0.23122|/0.23122 = 1.5251 ≫ 0.016` info-band.
**REGIME sub-verdict = VALID**: closed-form algebra at a single τ_fold evaluation, in-regime by construction.

**Full substitution chain (substituted numbers):**
1. `L1 = e^{2·0.19} = e^{0.38} = 1.462285`; `L2 = e^{−2·0.19} = e^{−0.38} = 0.683861`.
2. Baptista n=1 (Def 2): `sin² = 3·0.683861/(3·0.683861 + 1.462285) = 2.051583/3.513868 = 0.58385339`.
3. Orbit-volume measure (Def 3): `(det g_K)^{1/2} = (L1·L2³·L3⁴)^{1/2} = 1^{1/2} = 1` (volume-preserving). Per-orbit Weyl/Riemannian volumes: `Vol(S¹) = L1^{1/2} = e^{0.19} = 1.209250`; `Vol(S³) = L2^{3/2} = e^{−0.57} = 0.565525`.
4. Orbit-volume sin² (B2.3): `sin² = 3·0.565525/(3·0.565525 + 1.209250) = 1.696575/2.905825 = 0.58385339`.
5. Cubic target (Def 4): `sin² = 3/(3+e^{12·0.19}) = 3/(3+e^{2.28}) = 3/(3+9.776692) = 3/12.776692 = 0.23480277`.
6. Exponent read-off: orbit-volume → `e^{−4τ}` (n=1 family), NOT `e^{−12τ}` (cubic). Exponent NOT promoted 4→12.
7. Conclusion: the orbit-volume measure does NOT derive the cubic ⇒ FAIL (i); sin² = 0.5839 is 152.5% from PDG ⇒ FAIL (ii). The cubic's 1.55% near-hit is accidental (consistent with falsifier-rigor-registry row 7 `ACCOMMODATION-FLAGGED`).

**Dual-SHA**: `audit_sha256=fc490469702542a1de8a12f9fd52a6ae3f65de9fb7172df1556a93eeacd3209d`, `content_sha256=a826ed4f77f9e286147ba91c41fe90e29235fa5bab7c69a56626851217b300c3` (schema S84+).

**Substrate framing (GEOMETRIC)**: the substrate IS the Jensen-deformed SU(3) fiber; the Weinberg angle is the ratio of the orbit-volume-weighted fiber integrals of the U(1)_Y and SU(2)_L gauge-kinetic densities. Direction of explanation: Jensen eigenvalues (L1 on hypercharge, L2 on isospin) + orbit-volume measure (det g_K)^{1/2} → coupling normalisations g_1, g_2 → sin²θ_W. The intrinsic fiber-volume measure of the substrate's internal geometry sets the relative normalisation of the two emergent gauge fields — and that measure inserts half-integer (d_a/2) powers, fixing sin² at the n=1 value 0.5839, NOT the cubic 0.2348. Because this same orbit-volume measure object is what changes off the U(2) surface (INV2-W1-1 / Bridge-1), the FAIL here means the Weinberg angle and the Yukawa hierarchy do NOT share the cubic-promotion mechanism through this particular measure-counting (Bridge-2 ≠ Bridge-1 via the orbit-volume route).

### §W1-3. INV2-W1-3 (compute · baptista-spacetime-analyst)

**Status**: COMPLETED
**Gate ID**: `INV2-W1-3`
**gate_type**: `compute`
**Trigger**: `[VERIFY]` (existence / set-membership; `schema_v2_3tuple_required: false`)
**Classification**: **GEOMETRIC**
**Agent**: `baptista-spacetime-analyst` (sole writer; + schwarzschild-penrose-geometer causal-structure + volovik-superfluid-universe-theorist superfluid-lump cross-checks folded into Results)
**Hypothesis**: The reduced 12D Einstein equation on M⁴×SU(3) (DeWitt supermetric G_DeWitt=5.0, monotone V_SA(τ)) admits a static spherically-symmetric τ(r) modulus-soliton with a finite mass-radius relation + Buchdahl-like compactness ceiling — opening the compact-object sector.

**Verdict**: **FAIL** — the existence set is EMPTY. 0/25 τ_c values yield a regular localized self-gravitating profile; all 25 are `non_localizing` (the mass function m(r) diverges, never plateaus). A wall with a specific reason, not a defeat: it eliminates the static-modulus-soliton region of the compact-object solution space.

**Output Artifacts**:
- Script: `computations/investigation-2/inv2_w1_tau_modulus_soliton.py` (29,647 B; `from canonical_constants import *`, `solve_ivp` RK45 adaptive shooting from a regular center, `print_verdict_payload`; R_K(τ) recomputed in-script from the E3 closed form — NO 2.018144 literal).
- Data: `computations/investigation-2/inv2_w1_tau_modulus_soliton.npz` (93,612 B; 25-pt τ_c-scan classifications, M/R/compactness arrays, representative profiles, all cross-check scalars).
- Plot: `computations/investigation-2/inv2_w1_tau_modulus_soliton.png` (159,159 B; 4 panels — (a) τ(r) profiles, (b) divergent m(r), (c) monotone V=−R_K with no well, (d) class-vs-τ_c + verdict banner).
- Verdict line: `computations/investigation-2/inv2_gate_verdicts.txt` —
  `INV2-W1-3: FAIL -- value='NO_localized_profile_set_empty_0/25_dominant_channel=non_localizing_monotoneV_no_well' scheme=reduced-12D-einstein-scalar-soliton-shooting-G-DeWitt-5-V-SA-monotone convention=static-spherically-symmetric-TOV-radion-analog L_max=N/A audit_sha256=7273dbac8672f8a65eeb7eee82b401a40172f1c889aa1eb049b8429bbd8b8c54 content_sha256=1a42afc65d305a8365c16301d6426947ef731d811802a0d1c33fc1a022d2898c schema_version=S84+`
- **dual-SHA**: audit_sha256 `7273dbac8672f8a65eeb7eee82b401a40172f1c889aa1eb049b8429bbd8b8c54`; content_sha256 `1a42afc65d305a8365c16301d6426947ef731d811802a0d1c33fc1a022d2898c`. (canonical_constants.py pin `e6829db013a713a4…`.)

**MCP Pre-Compute Audit** (query-first discipline; each query + one-line salient return):
- `get_constant(G_DeWitt)` → **5.0** (S42 s42_gradient_stiffness). (1/2)·G_DeWitt = **2.5 = 5/2** — the S32 first-integral prefactor. **PRE-CLOSED** (canonical).
- `get_constant(tau_fold)` → **0.19** (S42 CONST-FREEZE-42). **PRE-CLOSED**.
- `search_knowledge(V_SA monotone / dS/dτ)` → **S_SA(τ)=a_0−a_2+a_4, monotone, dS/dτ=+58672.8>0** at fold (PROVEN S17a–S45, 9600/9600; `Spectral Action Monotonicity` theorem). Also surfaced: **τ_NEC=1.383** (NEC-violation onset, S95 W4-5 12D censorship) — physical domain boundary inside the τ_c-scan, recorded. **PRE-CLOSED** (PROVEN).
- `search_knowledge(R_K E3 closed form)` → **R_K(τ)=−¼e^{−4τ}+2e^{−τ}−¼+½e^{2τ}** (E3, baptista-operator-dk-tau.md); R_K(0)=2, R_K(0.19)=2.01814396, dR_K/dτ(fold)=0.27603275 (s95_w3_5). **PRE-CLOSED**; recomputed in-script and reproduced to machine precision.
- `search_knowledge(S32 domain-wall balance)` → **(5/2)(dτ/dx)²=V(τ)−V₀ with V(τ)=−R_K(τ)** (session-32-baptista-collab). Fixes BOTH the kinetic prefactor (5/2=G_DeWitt/2) AND the geometric reduced potential V=−R_K. **PRE-CLOSED**.
- `trace_entity(spectral action monotonicity)` → 6 PROVEN theorem hits (Structural Monotonicity: ⟨λ²⟩(τ) increases under volume-preserving Jensen deformation, all monotone f). Confirms V_SA well-less.
- `search_knowledge(τ-soliton / compact object / boson star)` → **no prior soliton/compact-object/mass-radius gate** exists in the corpus → this region is genuinely unexplored (the seed's Gap-C). Adjacent: Λ_eff=−½R_K (session-54), Λ_eff=⅛R_K (session-64) — the fiber curvature as the 4D potential, consistent with V=−R_K.

**Results**

*Substrate-first framing.* Reduced 12D Einstein-Hilbert action `S_{12D}=∫_{M⁴×SU(3)} R_P√g_P d¹²x` → (Kerner reduction, fiber Einstein-Hilbert R_K descending as the 4D modulus potential) the DeWitt-supermetric scalar-soliton functional `E[τ(r)]=∫d³x[(1/2)G_DeWitt(∂_rτ)²+V(τ)]`, V(τ)=−R_K(τ) → the static self-gravitating profile → M(R)+compactness. A compact object IS a region where the fiber modulus τ(r) climbs to deep compactification (spectral weight concentrating in **space**), the spatial analog of the τ(t) cosmogenesis history. Direction of explanation flows substrate → emergent, never the inverse.

*Substitution chain (the 5/2 prefactor + monotone-potential reasoning, Sage-verified).*
1. **12D action / Kerner**: `R_P(τ)=R_K(τ)+(1/4)|F(τ)|²`; in the static spherically-symmetric homogeneous-fiber reduction the fiber curvature R_K descends as the 4D scalar potential (the Λ_eff=−½R_K lineage, session-54). Geometric reduced potential **V(τ)=−R_K(τ)**.
2. **DeWitt kinetic stiffness**: modulus kinetic term `(1/2)·G_DeWitt·(∇τ)²` with G_DeWitt=5.0 (canonical). The S32 flat-space domain-wall first integral `(5/2)(dτ/dx)²=V(τ)−V₀` ⇒ **(1/2)·G_DeWitt = (1/2)·5 = 5/2**. **CHECK** — reproduced in-script (`half_G_DeWitt=2.5`).
3. **Monotone potential (PROVEN)**: V_SA=a_0−a_2+a_4 is monotone (dS/dτ=+58672.8>0). Independently, **V=−R_K is monotone DECREASING on [0.19,2.0]** — Sage `solve(dV/dτ=0)` returns the **empty set** (no critical point); in-script `V_monotone=True`. MONOTONE ⇒ **no interior well**. The soliton, if any, is gradient-vs-gravity balance (radion-boson-star analog), **NOT a double-well kink** — made explicit per the gate rubric.
4. **Reduced static Einstein-scalar (radion-TOV) system** (8πG=1, geometrized; compactness 2GM/R reported dimensionlessly so the unit choice does not bias the existence verdict). State `y=[τ,ψ=τ',m,Φ]`, `e^{−2Λ}=1−2m/r`:
   - `dm/dr=4πr²ρ`, `ρ=(1/2)G_DeWitt e^{−2Λ}ψ²+V(τ)`
   - `p_r=(1/2)G_DeWitt e^{−2Λ}ψ²−V(τ)`
   - `dΦ/dr=(m+4πr³p_r)/(r(r−2m))`
   - `τ''+(2/r+Φ'−Λ')τ'=(1/G_DeWitt)e^{2Λ}dV/dτ`
   - regular center `τ(0)=τ_c, τ'(0)=0, m(0)=0`.
5. **Derrick/Pohozaev (D=3, gravity-off limit)**: a static finite-energy lump requires `E_pot=−(1/2)E_grad`, i.e. a balance with a potential possessing an asymptotic stationary point τ_∞. A monotone, well-less, unbounded-below potential admits no such τ_∞ — the field rolls. **Structural prediction: no static modulus-soliton.**
6. **Set-membership read-off**: does the τ_c-shooting scan contain a regular localized profile with finite M and sup(2GM/R)<8/9?

*Numerical outcome (NUMBERS first).* 25-point τ_c-scan on [0.19, 2.0], RK45 adaptive (rtol 1e-8, atol 1e-10), outward to r=5×10³ M_KK⁻¹ with horizon (collapse) and |τ|→50 (runaway) termination events:

| Channel | count / 25 |
|:--|:--|
| **localized** (finite-M, density-decayed, field-settled) | **0** |
| non_localizing (m(r) diverges, no plateau) | **25** |
| rolling_runaway (|τ|→50) | 0 |
| collapse_horizon (1−2m/r→0) | 0 |

- `sup(2GM/R)` over localized profiles: **undefined** (set empty); C_max=8/9=0.8889 never reached because no profile localizes.
- The mass function diverges monotonically in magnitude with τ_c: m_end ranges from −1.06×10¹² (τ_c=0.19) to −1.01×10¹³ (τ_c=2.0). The sign is negative and the magnitude grows because, with V=−R_K<0 in the bulk, the energy density ρ is dominated by the negative potential term, so `∫4πr²ρ dr` diverges negative rather than settling to a finite ADM-like plateau. No mass-radius relation M(R) exists.

**Existence: FAIL (set empty).** No static spherically-symmetric self-gravitating τ(r) modulus-soliton exists within this ansatz. This is the structurally-predicted result (item 5), now confirmed by direct integration — the right epistemic order: structure first, computation confirms.

*Cross-check — schwarzschild-penrose causal-structure / trapped-surface reading (co-author framing).* The natural place a localized self-gravitating profile would announce itself causally is the formation of a marginally-trapped surface (an apparent horizon, `1−2m/r→0`) bounding a compact interior — the Buchdahl/Penrose compactness ceiling 2GM/R<8/9 is precisely the no-trapped-surface margin for a regular static sphere. The scan finds **zero horizon hits**: the `collapse_horizon` channel is empty (0/25). The geometry never builds a trapped surface because the mass function never concentrates — m(r) grows secularly without bound rather than saturating to a finite M inside a finite R. There is no causal boundary to enclose a compact object: the would-be interior is not causally severable from the exterior because the profile is delocalized. The Buchdahl ceiling is therefore vacuously respected (never approached) — consistent with FAIL: no trapped surface, no compact object, no causal-structure analog of a black-hole/neutron-star interior in this static modulus sector.

*Cross-check — volovik superfluid-lump / emergent-horizon analog (co-author framing).* In the superfluid-universe picture the modulus τ is the order-parameter-like deformation of the fabric; a gravity-bound "lump" would be an emergent acoustic-metric structure where the fiber order parameter concentrates and an emergent (acoustic/ergo-) horizon forms. The well-less spectral-action potential is the substrate statement that the fabric has **no static stable lump configuration**: monotone V_SA (dS/dτ=+58672.8) means there is no order-parameter value the fabric prefers to sit at — it always flows toward deeper compactification. A static superfluid lump requires a restoring potential with a minimum; the substrate's own monotonicity theorem forbids it at the single-crystal level. (This is the same structural fact that, in the **time** sector, makes cosmogenesis a one-way supersonic transit through the fold rather than oscillation in a well — the τ↔time correspondence, Bridge-3.) The volovik reading thus predicts the static lump fails and routes the compact-object sector to a **dynamical** / relic-concentration mechanism: the GGE-relic spectral-weight concentration (a non-equilibrium, time-dependent build-up), not a static modulus soliton. This is the alternative Bridge-3 reading the FAIL_meaning anticipates.

*Solution-space interpretation (what the wall closes, what survives).*
- **Closes**: the "static modulus-soliton compact object" region. The DeWitt kinetic term (prefactor fixed at 5/2, no free knob) + the monotone reduced potential V=−R_K (and equally the monotone V_SA) do **not** support a static gravity-bound modulus lump in the static spherically-symmetric ansatz. Eliminated with a specific reason (Derrick + well-lessness), not merely "not found."
- **Survives / routes forward (Bridge-3 alternative)**: the compact-object sector must be sought in a **dynamical / non-static** mechanism — GGE-relic spectral-weight concentration (volovik reading), or an oscillaton/time-dependent τ(t,r) configuration, where the monotone potential is not a static-equilibrium obstruction. The τ↔time correspondence (Gap-B) is engaged from the FAIL side: because the static spatial profile cannot settle for the same reason the cosmic transit cannot oscillate (well-lessness), the compact-object interior is more plausibly the **acoustic-white-hole interior run in time** (S105 Pillar I↔VI↔IV identity) than a static spatial soliton.
- **Regime note**: VALID throughout. The reduced-action truncation is not the limiting factor — the FAIL is structural (no τ_∞ stationary point), independent of the perturbative-fiber window; the integration completed cleanly to r=5×10³ for all 25 τ_c. The well-lessness holds in BOTH the geometric (V=−R_K) and spectral-action (V_SA) conventions, so the result is convention-robust.

*Carry-forward (genuine future computation, 4-field).* **What**: test the compact-object sector under a **dynamical** ansatz — either a τ(t,r) oscillaton (time-periodic self-gravitating modulus) or the GGE-relic spectral-weight concentration profile — to see whether a non-static localized energy concentration with a finite effective M(R) forms where the static soliton fails. **Inputs**: this gate's reduced Einstein-scalar system + G_DeWitt + V_SA/R_K closed forms; the GGE-relic density (n_pairs=59.8) machinery; the S105 acoustic-white-hole-interior identity. **Gate**: existence of a time-averaged finite-mass localized configuration with sup⟨2GM/R⟩ vs 8/9. **Effort**: 1 session (the radial ODE infrastructure is in hand; add the time dimension or the relic source term).

### §W1-4. INV2-W1-4 (workshop · van-den-dungen-bridge-theorist ↔ connes-ncg-theorist)

**Status**: COMPLETED (closed by artifact-existence on the workshop md; NO verdict line — workshop gate)
**Gate ID**: `INV2-W1-4`
**gate_type**: `workshop`
**Trigger**: `[VERIFY-THEOREM]`
**Classification**: **GEOMETRIC**
**Agents (EXACTLY 2)**: `van-den-dungen-bridge-theorist` ↔ `connes-ncg-theorist` | **Rounds**: 2 (4 turns, sequential)
**Adjudication**: Is the N3 Wedderburn χ-rescue (χ-killing M₃(ℂ) to pass orientability) the genuine fiber-over-base Kasparov product, or a convenient amputation?

**Output Artifacts** (artifact-existence closure — verified on disk):
- Workshop md: `sessions/investigation/investigation-2/workshops/n3-chi-rescue-kasparov-faithfulness.md` — present with `## Wrap-Up` + `Effected In-Session` (5 items, all `- [x]`, all routed to session-promotion) + `## Carry-Forward Computations` (CF-INV2-W1-4-M1, CF-INV2-W1-4-TYPEBRIDGE). Zero `*[NOT STARTED]*`/`*pending*` remaining; Workshop Verdict table filled. **This is the authoritative deliverable** — full R1/R2 content, substitution, and citations live there.
- NO verdict line (correct: workshop gates close by artifact-existence, not a verdict-file entry; `gate-verdicts.md §"Investigation-Track Canonical Path"`).

**Verdict** (structural, from the workshop Wrap-Up): **EXTRINSIC RESTRICTION WITH AXIOM-FORCED KERNEL** (converged; all three sub-questions **Converged**). Two-step composite: **Step A** (restrict A_F to the triality-0/BdG sub-sector) is geometry-UNFORCED (the M⁴×SU(3) vertical symbol does not select it; the Connes-Karoubi boundary sends the M₃-gap-class to (0,0,0)∈ℤ³ — no faithful fiber-image); **Step B** (given A, kernel = M₃) is axiom-FORCED (registry line 287 "by THEOREM", line 13208 "by NCG axiom 5"; the §VII.O d-singleton makes M₃ the only killable matrix block). Not faithful-rescue, not crude amputation.

**Results** (summary; authoritative detail in the workshop md):
- **(a)** Converged — χ is NOT the M⁴×SU(3) shriek, established as a THEOREM on two independent axes (category-mismatch: π_!∈KK^{dim F}(C(E),C(M⁴)) vs χ a finite-matrix *-homomorphism on A_F; + the Connes-Karoubi zero-map, registry line 288).
- **(b)** Converged — CLAIM-FULL false (D_total fails axiom 5 bare; N3 BROKEN); only CLAIM-χ holds. The M₃ double-use is dissolved by two functors on one algebra (G5 reads M₃'s representation — UNCONDITIONAL; axiom-5 reads M₃'s Hochschild cycle — fails).
- **(c)** Converged (Emerged) — the compound verdict above.
- **Register-status implication (ROUTED to session-promotion, NOT applied here — investigation track-local boundary):** N3 bare = BROKEN (stays); **N7-(i)** algebraic-singleton = STAGE-3-PERMANENT UNCONDITIONAL; **N7-(ii)** spectral-triple-for-D_total = CONDITIONAL-on-χ-admissibility; **LBA-5** = PROMOTED to a named, undischarged assumption (single discharge route = CF-INV2-W1-4-M1, expected FAIL per the Q10 zero-map); **G5** = UNCONDITIONAL.
- **EM-1 (primary pinned output):** the Step-A(chosen)/Step-B(forced) decomposition DISSOLVES the framework's own register contradiction — line 287/13208 "forced by theorem" vs line 17004 "up to χ-kernel choice" are both correct at different generality levels (singleton-specific forced vs generic-Wedderburn chosen).

## Wave 1 Synthesis (team-lead)

**Investigation 2 — single-wave guinea-pig run (terminal): 4 gates — 3 compute FAIL + 1 workshop LANDED.** The wave attacked the 23D Milnor-moduli complement transverse to the U(2)-invariant slice (the survey's root of the framework's two oldest tensions + two newest gaps). As a *set* the results are a high-information constraint-map update — four sharp boundaries, each with a specific mathematical reason and a forward route — not a defeat (per `epistemic-discipline.md`: negative results are boundaries).

**Per-gate results.**
- **INV2-W1-1 (FAIL; Track B ← 0.90):** off the U(2) surface, the minimal su(2)-split transverse modulus does NOT lift the per-generation Yukawa degeneracy — Schur-zero holds (`|dY_12/dδ|_0 = 1.9e-15 ≪ eps_lift = 1e-3`; the cubic Bridge-1 response is also null; the d=2 generation multiplet shifts rigidly 0.84086→0.85439 without splitting; det-ratio = 1.0 exact). The rank-1 wall is GENUINE physics for this direction — generations protected by a symmetry deeper than U(2)-equivariance. Cross-check separates isospin-splitting (22→30 distinct evals, expected SU(2)→U(1)) from generation-splitting (none). Closes the "hierarchy via the minimal su(2)-split" corridor; the C²-coset anisotropy direction is the natural next test.
- **INV2-W1-2 (FAIL; Track B ← 0.85):** the orbit-volume measure `(det g_K)^{1/2}` inserts half-integer powers (d_a/2 = 1/2, 3/2) whose controlling ratio-exponent is Sage-exact `ln(L2^{3/2}/L1^{1/2}) = −4τ` — IDENTICAL to Baptista n=1 (`sin² = 0.58385339`, machine-ε match to canonical `sin2_thetaW_fold`), NOT the cubic's −12τ. The measure does NOT derive the n=3 cubic; the cubic's 1.55%-of-PDG near-hit is confirmed accidental (falsifier-rigor-registry row 7 ACCOMMODATION-FLAGGED). Bridge-2 closed; Contradiction-2 (the Weinberg either/or) stands.
- **INV2-W1-3 (FAIL; existence set empty):** no static spherically-symmetric τ(r) modulus-soliton exists (0/25 τ_c values localize; all non-localizing, m(r) diverges). Structurally over-determined: the kinetic prefactor checks out (`(1/2)G_DeWitt = 5/2`), but `V = −R_K` is monotone (Sage `solve(dV/dτ=0) = ∅`, no interior well) and Derrick/Pohozaev (D=3) forbids a static finite-energy lump with a well-less potential — the numerics confirm the structure. Convention-robust (V=−R_K and V_SA both monotone). Zero trapped-surface formation (schwarzschild-penrose cross-check); the same well-lessness that makes cosmogenesis a one-way τ(t) transit forbids a static τ(r) lump (volovik cross-check). Closes the static-modulus-soliton compact-object region; routes Gap-C to a dynamical τ(t,r) oscillaton / GGE-relic mechanism.
- **INV2-W1-4 (workshop LANDED): "EXTRINSIC RESTRICTION WITH AXIOM-FORCED KERNEL".** vdd (Kasparov-submersion lens) + connes (Wedderburn-NCG-uniqueness lens) converged on all three sub-questions: (a) χ ≠ the M⁴×SU(3) shriek (theorem, two independent axes); (b) CLAIM-FULL false, CLAIM-χ holds, M₃ double-use dissolved by a two-functor reading (G5 UNCONDITIONAL); (c) the two-step composite (Step A extrinsic / Step B axiom-forced). N7 split into an UNCONDITIONAL algebraic-singleton leg and a CONDITIONAL spectral-triple-for-D_total leg (LBA-5 promoted, undischarged). EM-1 dissolves the register's own forced-vs-chosen contradiction.

**Cross-gate reading (the wave's headline).** The survey's central **"Bridge-1 = Bridge-2"** bet — that one off-U(2) geometric root (the orbit-volume measure) underlies BOTH the Yukawa generation hierarchy AND the Weinberg angle — is FALSIFIED on both arms: INV2-W1-1 shows the minimal transverse split does not lift the hierarchy; INV2-W1-2 shows the orbit-volume measure gives n=1, not the cubic. The two oldest tensions do not share this particular geometric mechanism. With the compact-object FAIL and the N3/N7 down-scoping, the wave returns four boundaries that sharpen the constraint surface and route four concrete forward computes. As the guinea-pig run, it also exercised `/rclab-coordinate`'s full mixed-gate-type juggling (3 compute background + 1 sequential 2-agent workshop) in a single pass.

### Carry-Forward Computations (MATH ONLY — propagate to `/rclab-investigate --investigation 2` → next investigation or session-promotion)

Full 4-field specs in the dedicated **## Carry-Forward Computations** section below: **CF-INV2-W1-1-C2COSET** (C²-coset anisotropy off-U(2) test), **CF-INV2-W1-3-DYNSOLITON** (dynamical τ(t,r) / GGE-relic compact-object), **CF-INV2-W1-4-M1** (M1 internal-shriek intertwiner — EVOI-highest on the N3/N7 axis), **CF-INV2-W1-4-TYPEBRIDGE** (categorical obstruction lemma).

### Effected In-Session (NON-MATH — completed by the orchestrator before STOP)

- [x] python-validate hook investigation-naming false-positive — extended `FILENAME_RE` to accept `inv{n}_*.py` (was `s{N}_*.py`-only) — `.claude/hooks/python-validate.py:40` (+ docstring L12, WARN message L157-159) and `.claude/hooks/python-validate.sh:16`; regex verified on disk (all 3 inv2 filenames + s84/s100a MATCH; helpers/random excluded).
- [x] Workshop document duplicate-header cleanup — removed 4 orphan blank skeleton sections (Re:V-b / Re:V-c / C-b / C-Q duplicates introduced during R1 editing) — orchestrator-direct presentation patch (`/rclab-coordinate` Hard Rule 2) — `sessions/investigation/investigation-2/workshops/n3-chi-rescue-kasparov-faithfulness.md` (post-clean: single header each, 0 placeholders).
- [x] WP §W1-4 stub → COMPLETED + structural verdict + workshop-md pointer (workshop gate closes by artifact-existence; no verdict line) — this file, §W1-4.
- [x] WP §W1-1 classification GEOMETRIC→PARTICLE — self-corrected by the INV2-W1-1 agent (plan YAML authoritative; the skeleton's GEOMETRIC was a transcription drift); verified on disk at §W1-1 line 14. No further action.

**Routed to session-promotion (NOT effected here — investigation track-local boundary per `gate-verdicts.md §"Investigation-Track Canonical Path"`; an investigation result enters the permanent record only when promoted into a session; full list with file:anchor pins in `investigation-2-housekeeping.md §B`):** the workshop's 5 register implications (atlas-04 N7 two-leg annotation; atlas-08 Q10 scope-fix; permanent-results-registry §VII.W-3 verdict-name + LBA-5; LBA-5 named-assumption registration; CF propagation) **+** the plan-index "routed-out" **Q9 CLOSED→PARTIAL down-correction (NS-3)** on `atlas-08-open-questions.md`. NOTE: the plan-index tagged Q9 "orchestrator effects in-session"; it is reclassified here to session-promotion for consistency with the track-local boundary (an investigation must not mutate curated, capstone-governing session-track registers — the same reason connes routed the workshop's analogous atlas edits to promotion rather than applying them).

## Carry-Forward Computations

**CF-INV2-W1-1-C2COSET — C²-coset anisotropy off-U(2) Yukawa test** (from INV2-W1-1):
1. **What**: build the C²-coset anisotropy transverse modulus (split L3·I_4, the C²-coset block, transverse to U(2) — the direction that DIRECTLY touches the generation/fermion sector) and re-run the off-U(2) Dirac + Yukawa-overlap test on the d=2 generation multiplet; does this direction lift the per-generation degeneracy at first order, where the su(2)-split (INV2-W1-1) could not?
2. **Inputs**: `computations/investigation-2/inv2_w1_off_u2_dirac_yukawa.py` (the `deformed_*_split_metric` + `Y_ij(δ)` + fixed-δ=0-multiplet machinery), `dirac_spectrum.py`, `canonical_constants` (`tau_fold`, L3=e^τ); INV2-W1-1's su(2)-split-null result as baseline.
3. **Gate**: `|dY_12/dδ_C2|_0 > eps_lift = 1e-3` AND `rank(Y_ij): 1 → ≥2` ⇒ PASS (hierarchy lives off-U(2) via the C²-anisotropy direction); both sub-thresholds null across the scan ⇒ FAIL (generation degeneracy protected on this direction too); sub-threshold lift ⇒ INFO.
4. **Effort**: 1 wave (machinery in hand; swap the split target su(2)→C²-coset, keep the L_max=10 GPU-block path).

**CF-INV2-W1-3-DYNSOLITON — dynamical τ(t,r) / GGE-relic compact-object test** (from INV2-W1-3):
1. **What**: test the compact-object sector under a DYNAMICAL ansatz — a τ(t,r) oscillaton (time-periodic self-gravitating modulus) OR a GGE-relic spectral-weight-concentration profile — to see whether a non-static localized energy concentration with finite effective M(R) forms where the static soliton FAILed (the monotone potential is not a static-equilibrium obstruction once time-dependence is allowed).
2. **Inputs**: `computations/investigation-2/inv2_w1_tau_modulus_soliton.py` (the reduced Einstein-scalar system + G_DeWitt + V_SA/R_K closed forms); the GGE-relic density machinery (n_pairs=59.8); the S105 acoustic-white-hole-interior identity (Pillar I↔VI↔IV).
3. **Gate**: existence of a time-averaged finite-mass localized configuration with `sup⟨2GM/R⟩` vs the Buchdahl C_max=8/9 ⇒ PASS (compact-object sector opens dynamically); empty existence set ⇒ FAIL (sector closed in this ansatz too); regime-marginal ⇒ INFO.
4. **Effort**: 1 session (the radial-ODE infrastructure is in hand; add the time dimension or the relic source term).

**CF-INV2-W1-4-M1 — M1 internal-shriek intertwiner construction** (from the INV2-W1-4 workshop; mirrors workshop CF; EVOI-highest on the N3/N7 axis — the single (c)-moving computation):
1. **What**: construct (or prove obstructed) the intertwiner identifying χ-killing M₃(ℂ) with the shriek `π_!^{CP²}` of `π_internal: SU(3)→SU(3)/U(2)=CP²` restricted to triality-0 content — exhibit `χ = (type-bridge) ∘ π_!^{CP²}` with a vertically-elliptic symbol on the U(2)-fiber whose index data selects exactly `ker(ι_*) = M₃(ℂ)`, to a machine-checkable commuting square; OR prove the type-bridge (fiber-function-algebra Peter-Weyl selection ↔ finite-summand deletion) categorically obstructed.
2. **Inputs**: Van-den-Dungen Paper 02 (1405.5368, almost-commutative manifolds, M⁴×F); `dirac_spectrum.py` reductive split (su(3)=u(1)⊕su(2)⊕C², U2_IDX=[0,1,2,7], M_IDX=[3,4,5,6]); registry line 287 (triality-0 ⇔ color-singlet ⇔ BdG-restricted); the Q10 W4 zero-map (registry line 288, gate S93-W2-1) as the hard constraint any candidate must reproduce.
3. **Gate**: PASS = commuting square verified + vertically-elliptic symbol exhibited ⇒ LBA-5 DISCHARGED, (c) flips to faithful-internal-shriek, N7-(ii) → UNCONDITIONAL. FAIL = type-bridge proven obstructed ⇒ LBA-5 permanently undischargeable on this route, (c) "extrinsic restriction" becomes PERMANENT. INFO = partial (irrep-selection matches, type-bridge open). Expected FAIL (Q10 zero-map is current evidence against a faithful image).
4. **Effort**: multi-wave; joint connes (NCG-axiomatic / K-theory zero-map cross-check) + vdd (Paper 02 almost-commutative machinery / Kasparov shriek).

**CF-INV2-W1-4-TYPEBRIDGE — categorical obstruction of summand-deletion-as-fiber-integration** (from the INV2-W1-4 workshop; isolable sub-lemma of CF-M1):
1. **What**: prove or refute, INDEPENDENT of CP² specifics, whether Paper 02 almost-commutative machinery admits ANY expression of "delete a Wedderburn summand of the fiber algebra F" as a fiber-integration on M⁴×F. A general NO closes M1 for ALL internal submersions at once (stronger than the CP²-specific CF-M1 FAIL).
2. **Inputs**: Paper 02 (1405.5368); the general almost-commutative spectral-triple axioms; the §VII.W-3.ALGEBRAIC Wedderburn rescue characterization (registry lines 16987-17004).
3. **Gate**: PASS (NO — categorically obstructed) ⇒ "extrinsic restriction" permanent on a categorical basis. FAIL (a fiber-integration realization exists) ⇒ M1 is open and CF-M1 must run case-by-case.
4. **Effort**: 1 wave NCG-axiomatic lemma (connes primary; vdd cross-check on the Kasparov-shriek side).

## Constraint-Map Updates

*(Investigation-track note: these updates are track-local until promoted into a session per `gate-verdicts.md §"Investigation-Track Canonical Path"`.)*

- **NEW WALL (Yukawa / Pillar-II):** the rank-1 Yukawa generation degeneracy is GENUINE off the U(2) surface under the minimal su(2)-split (INV2-W1-1; |dY_12/dδ|_0 = 1.9e-15, cubic also null) — protected deeper than U(2)-equivariance. Q18b sharpened for this transverse direction; Track B ← 0.90. The "minimal su(2)-split" corridor of Bridge-1 is closed.
- **NEW WALL (Weinberg / Pillar-II):** the orbit-volume measure selects n=1 (e^{−4τ}, sin² = 0.5839 = the M_KK Jensen value), NOT the n=3 cubic — Bridge-2 ("orbit-volume derives the cubic") closed with a specific reason (half-integer d_a/2 powers, not cubes); the cubic 0.23480 is accidental (ACCOMMODATION). Contradiction-2 (the Weinberg either/or) stands.
- **NEW WALL (compact-object / Gap-C):** no static τ(r) modulus-soliton (monotone V, Derrick/Pohozaev) — the static-modulus-soliton compact-object region is eliminated; routes to a dynamical / GGE-relic mechanism.
- **STRUCTURAL VERDICT (N3/N7):** χ-rescue = "extrinsic restriction with axiom-forced kernel"; N7 two-leg split (algebraic-singleton UNCONDITIONAL / spectral-triple-for-D_total CONDITIONAL-on-LBA-5); G5 UNCONDITIONAL; "χ ≠ M⁴×SU(3) shriek" = THEOREM on two axes; the register's forced-vs-chosen contradiction dissolved (EM-1). [All register annotations ROUTED to session-promotion.]
- **Bridge-1 = Bridge-2 convergence hypothesis FALSIFIED (both arms):** the Yukawa hierarchy and the Weinberg angle do not share the off-U(2) orbit-volume geometric root.

## Files Produced

Compute (`computations/investigation-2/`):
- `inv2_w1_off_u2_dirac_yukawa.{py,npz,png}` — INV2-W1-1
- `inv2_w1_weinberg_orbit_volume.{py,npz,png}` — INV2-W1-2
- `inv2_w1_tau_modulus_soliton.{py,npz,png}` — INV2-W1-3
- `inv2_gate_verdicts.txt` — 3 compute verdict lines (INV2-W1-1/2/3, all FAIL, pairwise-distinct audit_sha256: 1481b775…, fc490469…, 7273dbac…) + dual-SHA companions + [SIGN] 3-tuples (W1-1, W1-2)

Workshop deliverable:
- `sessions/investigation/investigation-2/workshops/n3-chi-rescue-kasparov-faithfulness.md` — INV2-W1-4 (artifact-existence closure; no verdict line)

Working paper + housekeeping:
- `sessions/investigation/investigation-2/investigation-2-w1-workingpaper.md` (this file)
- `sessions/investigation/investigation-2/investigation-2-housekeeping.md`

Infrastructure (Effected-In-Session):
- `.claude/hooks/python-validate.py` + `.claude/hooks/python-validate.sh` — investigation-track filename pattern (`inv{n}_*.py`)
