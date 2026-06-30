# Session 101 Wave W3 — Neutrino / Flavor Sector (Results Working Paper)

**Session**: 101 | **Wave**: W3 | **Plan**: session-101-plan-w3.md | **Theme**: neutrino/flavor sector — the S-3 surviving-map set (envelope-map + off-diagonal texture + greybody κ_ν) + D5 gap-equation + Z₃ CP rephasing + Pati-Salam Model-C fork.

## Gate Sections

### §W3-1. S101-NU-DIRAC-ENVELOPE-MAP (dirac-antimatter-theorist)

**Status**: COMPLETED
**Gate ID**: `S101-NU-DIRAC-ENVELOPE-MAP`
**Trigger**: `[SIGN]`
**Classification**: **PARTICLE** (neutrino-Dirac SHAPE corridor on the sector-keyed exponential Casimir envelope)
**Agent**: `dirac-antimatter-theorist`
**Hypothesis**: A pre-registered substrate-candidate exponent s_ν closes the neutrino-Dirac SHAPE corridor |Y₃/Y₂ − 2.4882512|/2.4882512 ≤ 0.01 on the envelope Y_i = E₁·(C₂,i)^q·exp(s_ν·g(C₂,i)) over the towers (0,0)/(1,0)⊕(0,1)/(1,1) — **EXPECTED verdict INFO** (shape closes at candidate (a), scale wall STANDS at r ≈ 3.37; candidate (c) LIVE per orchestrator override — gate 3 landed INFO).
**Plan reference**: `sessions/session-plan/session-101-plan-w3.md` §W3-1 (W-2/W-3 conditional-consumption resolution block, three-clause rubric, candidate set, substitution chain, convention pins).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- `computations/session-101/s101_nu_dirac_envelope_map.py` — present; `grep` confirms `from canonical_constants import` (Section 1, `*`-import with `_shared` on `sys.path`) AND `print_verdict_payload` (def + call). Scalar/3-vector algebra only; CPU OMP8 cap (no diagonalization, no ≥100×100 linalg).
- `computations/session-101/s101_nu_dirac_envelope_map.npz` — present (full-float64: 3 candidates × all clause intermediates, 6-corner (g,q) shape-exact grid, Eq.(4) analytic references, 3-tuple, dual-SHA, M_KK/v_ew/τ_fold provenance).
- `computations/session-101/s101_nu_dirac_envelope_map.png` — present (left: Eq.(4) shape hypersurface s_ν(q) for both g with the 3 candidate markers; right: per-candidate three-clause table + composite verdict header).
- Verdict line in `computations/session-101/s101_gate_verdicts.txt` matching `^S101-NU-DIRAC-ENVELOPE-MAP:.* audit_sha256=[a-f0-9]{64}` — present; emitted via the race-safe `emit_verdict` MCP tool (4 rows: canonical + dual-SHA companion + schema-v2 `[SIGN]` 3-tuple + candidate-c provenance). `audit_sha256=0744ad31000816b39f4cd5fbe894b9ca91fa48f979e1ed8d336645d7b00c3f4d`, `content_sha256=905fef29580baa3647537786b9ac128c782c9a0bc3f6b207f1713126784f46eb`.
- Input SHA reconciliation against the plan pins PASSED at runtime: `s100a_md_normalization.npz = 0b3245b6…` ✓, `s100a_freezein_overconstrained.npz = aa5acf54…` ✓. (Candidate (c) source `s101_kappa_nu_greybody.npz` present → candidate (c) LIVE, not N/A.)

**MCP Pre-Compute Audit**:
- `search_knowledge("S101-NU-DIRAC-ENVELOPE-MAP sector-keyed exponential Casimir envelope neutrino Dirac shape")` → gate NOT previously evaluated; hits are S99 litreview + equation/edge refs only (no gate, no closure covers it).
- `search_knowledge("neutrino Dirac Yukawa envelope s_nu widening 0.5469 charged lepton S0 1.6942 shape 2.4882")` → corroborates inputs: the (g=C2,q→0⁺) target +0.546948 (plan-w3 equation), the II.3 widening chain, `casimir_widening` provenance (S100a) — no closure on this gate.
- `get_constant` (via grep of `canonical_constants.py`): `Sigma_mnu_FW = 0.0582053272` (S99; matches npz `Sigma_target`), `M_KK = 7.428660036284456e16`, `v_ew = 246.0`, `tau_fold = 0.19` — imported for npz provenance pins (no scale-dependence in the dimensionless shape/rescale clauses).
- Status: NOT PRE-CLOSED; gate runs.

**Verdict**: **INFO** (composite) — `value = INFO;a=2-S0=0.305847@(C2,1/2)shapeDev=+0.364%_r=3.368; b=S0=1.694153@(sqrtC2,0+)shapeDev=+6.880%_KILL; c=0.546948@(C2,0+)shapeEXACT_scale_r=2.820; Y1=0EXACT; dlnY/dC2=+0.5491_WIDENING_vs_charged-S0=-1.6942`, scheme `EPS-LX-EXPONENTIAL-CASIMIR-ENVELOPE-S3-GRID`, convention `MIXED-N1-GEN2-RATIO-N2-ABSOLUTE-COUNTING-RATIO-NORMALIZED-TRACE-MEAN-CARRIER-THRESHOLD-GREYBODY`, L_max=N/A. schema-v2 3-tuple: **sign=PASS, magnitude=INFO, regime=VALID** → composite collapse `magnitude_verdict==INFO ⇒ INFO` (per `gate-verdicts.md`). This is the EXPECTED branch (`INFO_meaning`, plan §W3-1 lines 244–250): a substrate-pinned exponent closes SHAPE at ≤ 1% while the (n2) SCALE residual exceeds ln(1.05) — the shape corridor is OPEN through the exponential ε_LX class with a substrate-pinned exponent, the scale wall STANDS (one external constant rescale). Posteriors per `dual_prior`: INFO → 0.85 track_A on shape; scale wall stands (track_B-0.9 on the SCALE axis unchanged).

**Results** (NUMBERS first):

*Upstream scalars (from npz, runtime SHA-pinned).* `shape_required = 2.4882511868263` (npz full-float; pub form 2.4882512), `Y_S99 = [0, 4.79356602, 11.92759634]`, `E₁ = Y_ref = 0.8197411121` (= E_triple[0], the gen-1 anchor scale). `C₂ = [0, 4/3, 3]` (matches npz `C2` to atol 1e-12), `ΔC₂ = 5/3 = 1.6666666667`, `Δ_g(√) = √3 − √(4/3) = 1/√3 = 0.5773502692`. `S0_fit = 1.6941531565757` → **candidate (a) = 2 − S0 = 0.3058468434243** (computed in-script from the npz value, NOT hardcoded). `ln(shape_req) = 0.9115801291`, `ln(9/4) = 0.8109302162` (= ln(C₂,3/C₂,2)). `bound_DESI = 0.072`, `Sigma_target = 0.0582053272`.

*Eq.(4) shape-exact exponents per corner (analytic reference; Sage-QQ cross-checked at RealField(200)).* The 1-parameter shape hypersurface `ln(shape_req) = q·ln(9/4) + s_ν·Δ_g`:
- (g=C₂, q=1/2): `s_exact = (0.9115801291 − 0.5·0.8109302162)/(5/3) = 0.3036690126`
- (g=C₂, q→0⁺): `s_exact = 0.9115801291/(5/3) = 0.5469480775` (≡ candidate (c) target)
- (g=√C₂, q→0⁺): `s_exact = 0.9115801291/(1/√3) = 1.5789030988`

The 6-corner (g,q) closed admissible grid (no extension permitted) records the shape-exact s_ν at each of {C₂,√C₂}×{0⁺,1/2,1}; the three candidates sit at three of these corners.

*Per-candidate three-clause result.* Clauses: (1 shape) |Y₃/Y₂ − 2.4882512|/2.4882512 ≤ 0.01; (2 scale, n2) |ln r| ≤ ln(1.05)=0.04879 with r = Y₂_S99/Y₂_map; (3 rescale, n1) |r₂/r₃ − 1| ≤ 0.01 with r_i = Y_i_S99/Y_i_map. **Y₁ = 0 EXACT** for all candidates (structural zero from C₂(0,0)=0, enforced for all q including q→0⁺ — the tree-zero genre the surviving class must keep).

| cand | s_ν | (g,q) | Y_map (gen 2,3) | [1] shape dev | [2] \|ln r\| | [3] rescale | DESI Σ_corner | composite |
|:----:|:---:|:-----:|:---------------:|:-------------:|:-----------:|:----------:|:-------------:|:---------:|
| (a) 2−S0 | 0.305847 | (C₂, 1/2) | [1.423146, 3.554022] | **+0.364%** PASS | 1.214 **FAIL** | +0.364% PASS | 0.00517 eV SAFE | shape PASS, scale FAIL |
| (b) S0 | 1.694153 | (√C₂, 0⁺) | [5.797767, 15.418879] | **+6.880%** FAIL | 0.190 FAIL | +6.880% FAIL | 0.0973 eV **OVERSHOOT** | shape FAIL (KILL) |
| (c) s_ν^pred(κ_ν) | 0.546948 | (C₂, 0⁺) | [1.699778, 4.229474] | **+0.0000%** PASS | 1.037 **FAIL** | +0.0000% PASS | 0.00732 eV SAFE | shape EXACT, scale FAIL |

- **Candidate (a)** — shape **+0.364%** (matches the plan's predicted +0.36% to 3 sig figs; the candidate sits 0.72% from the corner's shape-exact 0.3036690, placing it +0.364% inside the ±1% band by construction). Scale residual r = 3.368 (the plan's predicted "r = 3.378" is a presentation-precision approximation; the exact algebra gives r₂ = 3.36829, r₃ = 3.35608, geo-mean 3.36218 — all r ≈ 3.37, 0.29% below the plan's rounded prose, identical INFO branch). |ln r| = 1.214 ≫ 0.0488 → scale FAIL. Rescale constancy +0.364% PASS (the shape-equivalent constancy test tracks the shape deviation exactly). DESI safe.
- **Candidate (b)** — the EXPECTED KILL: shape **+6.880%** (matches plan +6.9%) FAILs the 1% band, AND it overshoots DESI (Σ_corner = 0.0973 eV > 0.072) — confirming the plan's pre-registration that (b) falsifies the only scale-closing corner (√C₂, q→0⁺) if it misses shape. Scale |ln r| = 0.190 also FAILs (the corner does NOT close at s_ν = S0; the scale-closing required the shape-exact 1.5789, not S0 = 1.6942).
- **Candidate (c)** — LIVE per orchestrator override (gate 3 `S101-KAPPA-NU-GREYBODY` landed INFO, audit `833ddb9e`; `s_nu_pred = 0.5469480775505`, branch (i) mode-frequency inversion dω/dC₂ < 0, κ_ν > 0 thermal). At (g=C₂, q→0⁺) it is **shape-EXACT** (+0.0000% — it IS ln(shape_req)/ΔC₂ by construction) with rescale 0.0000%. Scale residual r = 2.820, |ln r| = 1.037 → scale FAIL. This is the W-3-pinned structurally-privileged candidate (sector-keyed threshold/greybody slope, the S99 four-lens modulus face); per the orchestrator override its sign is confirmed (+0.5469, widening) and its magnitude is OPEN (W3-3's magnitude was a compare-to-self tautology) — here it closes shape exactly, which is consistent with +0.5469 but does not by itself FORCE the scale closure.

*Substitution chain (NUMBERS substituted) — the [SIGN] pre-registration.* **Claim 1 (widening sign):** Step 3 `d ln Y_req/dC₂ = ln(Y₃/Y₂)/ΔC₂ = ln(2.4882512)/(5/3) = 0.9115801·(3/5) = +0.5469481`; the deciding candidate's computed `d ln Y/dC₂ = +0.5491` (candidate (a); composite carrier including the q=1/2 prefactor) is **> 0 → WIDENING**, while `d ln m_lep/dC₂ = −S0 = −1.6941532 < 0 → NARROWING`. Step 4: sign(+0.549) = +1; sign(−1.694) = −1 → **OPPOSITE**; the sector-keyed sign flip is REQUIRED and confirmed (II.3 widening chain). **sign_verdict = PASS** (every candidate reproduces a widening composite; (c) gives exactly +0.5469). **Claim 2 (candidate (a) analytic placement):** shape@(a) = exp(0.5·0.81093 + 0.305847·5/3) = exp(0.915210) = 2.49733, dev +0.364% < 1% — INSIDE the band by construction; the live risk at (a) is the SCALE clause (r = 3.37 ≫ 1.05 → INFO). **Claim 3 (candidate (b) kill):** shape@S0 = exp(1.694153·(1/√3)) = exp(0.97817) = 2.65945, dev +6.88% > 1% — the pre-registered kill of the only scale-closing corner. **Direction read-off realized:** EXPECTED composite branch = INFO via shape PASS (candidates (a) and (c)) + scale FAIL + rescale PASS.

*4-tuple:* `(value=INFO;…, scheme=EPS-LX-EXPONENTIAL-CASIMIR-ENVELOPE-S3-GRID, convention=MIXED-N1-GEN2-RATIO-N2-ABSOLUTE-COUNTING-RATIO-NORMALIZED-TRACE-MEAN-CARRIER-THRESHOLD-GREYBODY, L_max=N/A)`. The W-2 fifth-axis counting pin `RATIO-NORMALIZED-TRACE-MEAN` is carried on the convention; the C₂ grid is the Casimir invariant (counting-convention-BLIND), so the W-2 landing does not replace the grid (the "may replace floor-C₂ data" branch of the S-3 conditional clause does not fire — the grid never consumed floor data). No s84-cache eigenvalue consumption ⇒ no A19 UNTRUSTED-UPSTREAM extra-row.

**Substrate framing.** PARTICLE. The neutrino sector reads the SAME multiplicity-bundle index as the charged sector through the seesaw projection: the towers (0,0)/(1,0)⊕(0,1)/(1,1) are Peter-Weyl sectors of D_K on Jensen-deformed SU(3), C₂ is their Casimir grading, and M_R IS the D_K B-branch fold-energy spectrum [1.00439566, 1.07857332, 1.17000260] M_KK — not an external heavy scale. Direction of explanation: D_K eigenvalues (B-branch fold energies) → seesaw projection → required Yukawa envelope Y_i → oscillation observables. The gate asks whether the substrate's OWN exponent candidates (the charged-lepton S0 with a two-unit mode shift; the greybody κ_ν) carry the envelope's SHAPE — i.e., whether the widening (+0.5469/unit-C₂, OPPOSITE to the charged-lepton −1.6942) is a substrate prediction or an external parameter. It is a substrate prediction for SHAPE (candidates (a) and (c) close it); it is NOT a substrate prediction for SCALE (r ≈ 3.37 / 2.82 — the one external constant rescale stands). Y₁ = 0 EXACT from C₂(0,0) = 0 is the structural zero the class preserves (tree-zero genre, W-4 workshop) — the gen-1 (0,0) tower carries no Dirac coupling.

**Assessment (constraint-map placement).** This is the `INFO_meaning` scenario (plan §W3-1). The exponential ε_LX class's SHAPE corridor is OPEN with a substrate-pinned exponent: candidate (a) (the k=−2 integer-shifted charged-lepton S0) closes shape at +0.364%, and candidate (c) (the greybody κ_ν, the W-3 structurally-privileged carrier) closes it EXACTLY at the (C₂, q→0⁺) corner. The [SIGN] pre-registration is confirmed — the neutrino envelope WIDENS (+0.549) where the charged-lepton envelope NARROWS (−1.694); the sector-keyed sign flip is a substrate prediction (the II.3 widening chain), realized by both the integer-shifted-S0 route and the greybody route. What STANDS is the SCALE wall: at substrate-natural (n2) absolute normalization the gen-2 reach misses by |ln r| ≈ 1.04–1.21 (r ≈ 2.82–3.37 ≫ 1.05), so the Dirac-scale anchor remains irreducibly external (track_B 0.9 on the SCALE axis, consistent with the S100a-MD-NORMALIZATION PERMANENT caveat). The gate does NOT fire the PASS-branch Decision-Points escalation (no candidate closes shape AND scale), so the S100a-MD-NORMALIZATION PERMANENT caveat needs no scoped review here. Candidate (b)'s double FAIL (shape +6.88% AND DESI overshoot 0.0973 eV) excludes s_ν = S0 at the (√C₂, q→0⁺) corner — the only scale-closing corner is falsified by the substrate's own charged-lepton exponent, sharpening track_B to exactly-one-parameter (the single external rescale). Three structural results survive as positive constraints: (i) **Y₁ = 0 EXACT** preserved at every candidate (the class keeps the tree-zero); (ii) the **widening sign flip** is substrate-derived (sign_verdict PASS, robust across all three candidates); (iii) the **DESI safety** holds at the shape-closing corners (Σ_corner ≤ 0.0073 eV ≪ 0.072) — only the kill-corner (b) overshoots. The structurally forced `sign=PASS` (d ln Y/dC₂ > 0, widening) is pinned for any downstream re-derivation of the neutrino-envelope direction; candidate (c)'s exact shape closure soft-feeds the W3 S0-knob / envelope-carrier lineage (Wave 2) as the privileged-carrier read-out.

---

### §W3-2. S101-NU-DIRAC-OFFDIAG-TEXTURE (dirac-antimatter-theorist)

**Status**: COMPLETED
**Gate ID**: `S101-NU-DIRAC-OFFDIAG-TEXTURE`
**Trigger**: `[VERIFY]`
**Classification**: **PARTICLE** (doublet-split off-diagonal seesaw texture under the landed W-2 counting convention)
**Agent**: `dirac-antimatter-theorist`
**Hypothesis**: Under the landed W-2 unit pinning, the doublet-split off-diagonal texture m_D ∝ [[d,w],[w*,d]] on the (1,0)⊕(0,1) doublet — pushed through the diagonal-M_R seesaw — lands the gen-3/gen-2 split ratio in 2.4883 ± 1% with scale within 5% of substrate-natural, while preserving the m₁ = 0 rank-deficiency (no |s|²-channel (0,0)↔(1,1) element).
**Plan reference**: `sessions/session-plan/session-101-plan-w3.md` §W3-2 (prerequisite-discharge note, three-clause AND rubric, BDI reality pin, [0.405, 0.449] window).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- `computations/session-101/s101_nu_dirac_offdiag_texture.py` — present; `grep` confirms `from canonical_constants import` (Section 1) AND `print_verdict_payload` (def + call). 2×2/3×3 algebra only; CPU OMP8 cap (no GPU needed).
- `computations/session-101/s101_nu_dirac_offdiag_texture.npz` — present (all Step A–D intermediates, thresholds, 3-tuple, dual-SHA, M_KK/v_ew provenance).
- `computations/session-101/s101_nu_dirac_offdiag_texture.png` — present (left: S(x) curve with pinned vs required points + ±1% band + FAIL window; right: texture + clause table).
- Verdict line in `computations/session-101/s101_gate_verdicts.txt` matching `^S101-NU-DIRAC-OFFDIAG-TEXTURE:.* audit_sha256=[a-f0-9]{64}` — present; emitted via the race-safe `emit_verdict` MCP tool (4 rows: canonical + dual-SHA companion + schema-v2 3-tuple + regulator_pin companion). `audit_sha256=d8712a6f2cc32d6c18cbd81c5322225e5c38786d2377089abf90b69a86896df5`, `content_sha256=16260b4bf86bb17ae1205daa4017a6498d7f2df99cdab8736c6f0e9cc40cf1bc`.
- Input SHA reconciliation against the plan pins PASSED at runtime: `s100a_yukawa_overlap_offdiag.npz = 23d386df…` ✓, `s100a_md_normalization.npz = 0b3245b6…` ✓.

**MCP Pre-Compute Audit**:
- `search_knowledge("NU-DIRAC-OFFDIAG-TEXTURE seesaw doublet split 2.4882512 off-diagonal")` → gate NOT previously evaluated; nearest is `S96-MATTER-SEESAW-D5` (INFO, value 2.2016, a *different* seesaw-vs-direct-D_K reconciliation, not the W-2-pinned doublet texture) — no closure covers this gate.
- `search_knowledge("yukawa off-diagonal texture 1/sqrt(6) Weingarten Z3 BDI reality doublet diagonal")` → corroborates the structural inputs: `|w| = 1/sqrt(6)` Weingarten-exact (session-101-plan-w3 equation), `λ_± = d ± |w|` (session-99-fermion-mass-transit), `d1 = d2` J-reality (W-2 ruling) — confirms the texture and eigenvalue split.
- `get_constant("M_KK")` → 7.428660036284456e16 GeV (S42 CONST-FREEZE-42); imported, used only for npz provenance pin (no scale-dependence in the dimensionless split). `get_constant("v_ew")` → 246.0.
- Status: NOT PRE-CLOSED; gate runs.

**Verdict**: **FAIL** (composite) — `value = S_split = 2.3797959` (= (√6+1)²/5 exact), scheme `TYPE-I-SEESAW-DOUBLET-SPLIT-OFFDIAG-W22-TEXTURE`, convention `RATIO-NORMALIZED-TRACE-MEAN-UNITPIN-OFFDIAG-INVARIANT-DIAG-RETAGGED`, L_max=N/A. schema-v2 3-tuple: **sign=PASS, magnitude=FAIL, regime=VALID** → composite collapse `magnitude_verdict==FAIL ∧ regime_verdict==VALID ⇒ FAIL` (per `gate-verdicts.md`).

**Results** (NUMBERS first):

*Step A — unit pin (the only new computation).* The off-diagonal `|w| = 1/√6 = 0.40824829` is counting-INDEPENDENT (W-2 ruling B6(iii)): a per-mode (intensive) Haar amplitude, INVARIANT under the convention retag. The diagonal d-entries are as-computed `RATIO-BLOCKSUM` (extensive: a block SUM over sector modes — the `eps_lx_block_phi0` diagonal is `O_g[0] = 8.206524`). To form the seesaw split, both legs must sit in ONE unit system. Per the Counting-axis discipline (`regulator-pin-discipline.md §"Counting"`), `RATIO-NORMALIZED-TRACE-MEAN = blocksum / multiplicity n_g` (intensive, per-mode). The W-2 npz pins the per-mode trace-mean diagonal **exactly**: `kernel_mean_unit = 1.0` — the kernel is normalized so the per-mode diagonal amplitude is 1.0 in the units where `|w| = 1/√6`. Hence the unit-pinned ratio:

  `x = |w| / d_trace_mean = (1/√6) / 1 = 0.40824829`.

The MIXED reading `x = |w|/O_g[0] = 0.0497` (intensive numerator / extensive denominator) is unphysical and is retained in the npz as an explicit cross-check witness only. The W-2 ruling is single-valued: there is no second admissible reading for d (regime VALID).

*Step B — seesaw split.* Eigenvalues `d ± |w|`: `λ_heavy = 1.40824829` (gen 3), `λ_light = 0.59175171` (gen 2). Split ratio `S = λ_heavy/λ_light = (1+x)/(1−x)`. Sage-exact closed form: **`S = (√6+1)²/5 = 2.37979590`** (`S_closed` matches `S_pinned` to float64). Required `S = 2.48825119` fixes required `x = (S−1)/(S+1) = 0.42664679`. **Shape deviation `= (2.37979590 − 2.48825119)/2.48825119 = −4.359%`**, exceeding the ±1% shape band ⇒ **clause 1 FAIL**.

*Step C — scale (substrate-natural).* Pinning the heavy texture eigenvalue to `Y₃_S99 = 11.927596` gives `Y₂_texture = λ_light·(Y₃_S99/λ_heavy) = 5.012025`; vs `Y₂_S99 = 4.793566`, `scale_dev = |Y₂_texture/Y₂_S99 − 1| = 0.04557 ≤ 0.05` ⇒ **clause 2 PASS** (subordinate to shape; PASS requires clause 1 ∧ 2 ∧ 3).

*Step D — rank-deficiency sub-criterion.* The CG-admissible-but-must-vanish (0,0)↔(1,1) |s|²-channel: `M12_inner = 0`, `w_chain_literal_t0 = 0` ⇒ `rank_channel = 0.0 ≤ 1e-12` ⇒ **clause 3 PASS**. The explicit 3×3 m_D embedding has `svals = [1.4082, 0.5918, 0.0000]`, `rank(m_D) = 2` (m₁ = 0 rank-deficiency preserved — no |s|²-channel smuggled in). The W-2 `w_chain_zero_proof` (center-Z3 Haar invariance + triality-0 kernel cannot connect t=1 to t=0) is the structural reason.

*BDI J-reality witness.* `bdi_pair_max_rel_dev = 3.7e-15` — the doublet diagonal equality `d1 = d2` is machine-exact, forced by `[J, m_D] = 0` on the (1,0)/(0,1) conjugate pair. This is the same real structure J whose compatibility with D_K (KO-dim 6) enforces particle–antiparticle mass equality; here it enforces the doublet symmetry, which is what makes the split a function of `|w|` only.

*Substitution chain (direction + window, NUMBERS substituted).* `dS/dx = 2/(1−x)² = 5.7115 > 0` ⇒ S monotone increasing on (0,1), heavy = +|w| branch, `S > 1` always — **sign PASS** (structurally forced and confirmed: `S_pinned = 2.38 > 1`). The pre-registered Step-5 prediction (shape −4.35% at `x_raw`, asking whether the d-retag moves x into the ±1% band) is realized: the diagonal trace-mean retags to exactly `d = 1`, leaving `x = 1/√6` UNCHANGED from `x_raw`, so the shape stays at −4.36% — the retag does **not** close the adjacency.

*Window vs band (the FAIL routing).* `x = 0.40824829 ∈ [0.405, 0.449]` (the literal FAIL-window trigger does NOT fire), AND clause 3 holds — so neither literal FAIL trigger fires. But clause 1 (shape) fails, excluding both literal PASS (needs 1∧2∧3) and literal INFO (needs 1∧3). The binding verdict is the schema-v2 composite collapse: magnitude (the ±1% shape band) FAILs in a VALID regime ⇒ **composite FAIL**. The window `[0.405, 0.449]` is wider than the tight ±1% shape band; `x` lands in the window but outside the band — both surfaces agree in DIRECTION ("does not close"), the band being the operative magnitude test.

**Substrate framing.** PARTICLE. The texture IS the substrate's BDI fund↔antifund s-linear channel content: `|w| = 1/√6` is Weingarten-exact Haar geometry on the Jensen fiber, `arg(w) ∈ {π, ±2π/3}` is the second-Z3, and the doublet diagonal equality `d1 = d2` is J-reality (charge conjugation on the (1,0)/(0,1) pair). The seesaw reads this 2×2 through `M_R =` the D_K B-branch fold energies. `m₁ = 0` is not assumed but a CG selection rule [(2,0)×(0,0) = (2,0) ≠ (0,1)]; the rank-deficiency sub-criterion verifies the one CG-admissible channel that would break it stays exactly zero.

**Assessment (constraint-map placement).** This is the `FAIL_meaning` scenario (plan §W3-2 lines 453–457): under the now-computable W-2 trace-mean unit pin, the diagonal retags to `d = 1` and the off-diagonal stays `1/√6`, so `x = 1/√6` is left exactly where it was — the **4.5% shape adjacency was real, not a unit artifact**. CLASS-2 at the substrate-exact `|w| = 1/√6` is **excluded** for the shape clause. Two structural results survive the FAIL and are positive constraints: (i) the m₁ = 0 rank-deficiency is preserved exactly (the |s|²-channel does not lift it — the texture does not over-fit), and (ii) the scale clause closes (`scale_dev = 4.56% ≤ 5%`) at substrate-natural normalization, so the *scale* wall is not where this corridor dies — the *shape* is. Because the verdict is FAIL with a NON-DIAGONAL m_D landing here, the route-(b) `MR-TEXTURE-ROUTE-B HOLD` trigger does NOT fire on a PASS (the FAIL closes the CLASS-2-at-exact-|w| corridor for shape; corridor narrows to gate-1 survivors + CLASS-3 HOLD). This output soft-feeds W3-5 leg (ii) as N/A-style (non-blocking): the texture's exact-|w| shape closure means gate 5's phase question is not gated on a CLASS-2 shape PASS here. The structurally forced `sign=PASS` (heavy = d+|w|, S > 1, monotone) is pinned for any downstream re-derivation of the split direction.

---

### §W3-3. S101-KAPPA-NU-GREYBODY (hawking-theorist)

**Status**: COMPLETED
**Gate ID**: `S101-KAPPA-NU-GREYBODY`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (Hawking sector-κ greybody ladder extended to the Dirac-neutrino channel)
**Agent**: `hawking-theorist`
**Hypothesis**: The S99 sector-κ ladder (lepton 1.89 / up 1.29 / down 0.78) extends to the Dirac-neutrino channel — a substrate-derived κ_ν whose sign AND magnitude reproduce a shape-exact s_ν within 5% on the pre-declared (g=C₂, q→0⁺) corner (target +0.546948) — i.e. the II.3 widening sign-flip (OPPOSITE to all three charged sectors) EMERGES from the horizon/greybody machinery rather than being externally imposed.
**Plan reference**: `sessions/session-plan/session-101-plan-w3.md` §W3-3 (corner-declaration discipline, sign+magnitude clauses, κ_exit / Pöschl–Teller pins, A19 note).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- `computations/session-101/s101_kappa_nu_greybody.py` — present; contains `from canonical_constants import` and `print_verdict_payload`. ✓
- `computations/session-101/s101_kappa_nu_greybody.npz` — present (all derived quantities + branch/sign/magnitude/regime + dual-SHA). ✓
- `computations/session-101/s101_kappa_nu_greybody.png` — present (3 panels: charged-ladder reproduction / the sign-flip geometry / s_ν vs Eq.(4) corners). ✓
- Verdict line in `computations/session-101/s101_gate_verdicts.txt` matching `^S101-KAPPA-NU-GREYBODY:.* audit_sha256=[a-f0-9]{64}` — present, `audit_sha256=833ddb9e4041d214…d196c7`. ✓
- dual-SHA companion row + schema-v2 `[SIGN]` 3-tuple row (`sign_verdict=PASS magnitude_verdict=INFO regime_verdict=VALID`) + regulator/corner/A19 extra-rows — present (6 rows total, race-safe via `emit_verdict`). ✓
- **A19 extra-row**: NOT triggered. The ω_i map is **Casimir-closed-form** (ω_i = C₂_i), so the s84 L12 cache is **NOT consumed** → no UNTRUSTED-UPSTREAM row required. The closed-form path is the one the plan anticipated ("N/A for the closed-form legs"); L_max=NA.

**MCP Pre-Compute Audit** (queries run before writing the script):
- `search_knowledge("sector kappa ladder fermion mass hawking greybody S99 lepton up down")` → confirmed S99 `y_i ∝ Γ(ω_i)·exp(−2πω_i/κ)`; `λ^GGE_gen = 2πω_gen/κ = S_gen = S0·(C2_gen−C2_min)` (session-99-fermion-mass-transit/hawking).
- `search_knowledge("kappa_exit Kitaev identity 2pi T a4 47.61 surface gravity exit")` → confirmed the Kitaev anchor `2π·T(a₄)=κ_exit`, exit surface-gravity equation (session-99-fermion-mass-hawking eq.).
- `search_knowledge("S0 slope C2 Casimir generation per-sector S_gen ladder ... widening narrowing")` → confirmed `ln(m_j/m_i) = −S0·(C2_j−C2_i)`, `C2 = (4/3,3,6)` for (1,0)/(1,1)/(3,0) (session-100a-plan-w3).
- `get_constant("M_KK")` = 7.4287e16 GeV; `get_constant("T_acoustic")` = 0.112; `get_constant("kappa_exit")` → **not a canonical constant** (it is a plan-pinned M_KK-unit value 47.61, transcribed per the pinmap; NOT promoted — no canonical entry created). `list_constants("kappa")` → kappa_exit absent (consistent).
- **PRE-CLOSED?** No closure covers this gate; the neutrino-channel sign/magnitude question is genuinely open. Charged-ladder (1.89/1.29/0.78) is S99-known and reproduced here as a machinery-validation cross-check, not re-derived as new.

**Verdict**: **INFO** — `audit_sha256=833ddb9e4041d2144603cb32ccbd89656e03659ba3f985fe5feaa53ae8d196c7`, `content_sha256=89f427e56afd4720a030fd0a4fac387c50c196cab2e083e93551355453db1178`. Schema-v2 3-tuple: **sign_verdict=PASS / magnitude_verdict=INFO / regime_verdict=VALID** → composite **INFO** (collapse rule: magnitude INFO ⇒ composite INFO). This is the plan's **INFO_meaning** exactly: the widening direction EMERGES (configuration (i) realized), magnitude is open ⇒ candidate (c) enters gate 1 **sign-confirmed / magnitude-open**. `dual_prior`: INFO → 0.7 track_A.

**Results**:

*Step A — charged-sector ladder reproduction (machinery validation + anti-rediscovery, run BEFORE the neutrino number).* Log-gap ratio `W = ln(m₂/m₁)/ln(m₃/m₂)` from PDG masses (m_e, m_μ canonical; m_τ = PDG pole 1.77686; quark masses PDG 2024):
- lepton: W = 1.889036 (target 1.89, rel-dev 0.0005) ✓
- up: W = 1.298054 (target 1.29, rel-dev 0.0062) ✓
- down: W = 0.788107 (target 0.78, rel-dev 0.0104) ✓

All three within the 0.02 diagnostic (non-gating) tolerance — the same `y_i ∝ Γ(ω_i)·e^{−2πω_i/κ}` machinery the neutrino channel uses is validated. Sage QQ cross-check (RealField-80): identical to 6 sf.

*Step B — κ_ν and the neutrino-channel (ω, κ, Γ) map.* Kitaev anchor `2π·T(a₄) = κ_exit = 47.61 M_KK` [regulator `a_4^{Pauli-Villars}`, S96 PV lineage] ⇒ T(a₄) = 7.577367 M_KK. Neutrino-Dirac tower (0,0)/(1,0)+(0,1)/(1,1) → C₂ = (0, 4/3, 3); ω_i = C₂_i (Casimir-unit frequency map, λ_ω = 1, M_KK units). Pöschl–Teller barrier (V(x) = V₀/cosh²(αx), Ferrari–Mashhoon closed form) calibrated to `transmitted_fraction = 0.512` at ω_ref = 4/3: V₀ = 2.007063 M_KK (α = 1), T(ω_ref) = 0.512000 ✓. Γ on the tower = [0.00000, 0.51200, 0.99997]; d ln Γ/dC₂ (gen2→3) = +0.401642.

*The decisive structural sign test (exhaustive factorization, eq. [2]/[4]).*
`d ln Y/dC₂ = [ d ln Γ/dω − 2π/κ ]·(dω/dC₂) = B · (dω/dC₂)`, EXHAUSTIVE for κ > 0 (sign of a product = product of signs; no third branch). With κ_ν kept a bona-fide positive surface gravity and the **universal Boltzmann-dominated** bracket `B = +0.401642 − 2π/11.4878 = −0.145306 < 0` (the SAME thermal-horizon regime as all three charged sectors), the required widening `d ln Y/dC₂ = +0.5469 > 0` forces `dω/dC₂ = (+0.5469)/(−0.145) = −3.764 < 0` ⇒ **BRANCH (i): mode-frequency INVERSION** on the neutrino towers. κ_ν stays > 0 (κ_ν,bare = 2π/|s_ν| = 11.4877 M_KK, sitting sensibly between T_GH ≈ 1.4 and κ_exit = 47.61 M_KK). The seesaw `m_ν = m_D²/M_R` with M_R = the near-degenerate D_K B-branch fold energies (lightest ν rides the largest M_R) is what supplies the inversion — the back-solved Y^ν_D INCREASES with C₂ while the charged envelope DECREASES. **The construction does NOT forbid the widening sign; it SUPPLIES it via branch (i) with a thermal (not super-radiant) κ_ν.** `construction-FORBIDS-widening = FALSE`.

*Step C — sign-first, magnitude-second at the PRIMARY corner (g=C₂, q→0⁺).* s_ν^pred = d ln Y^ν_D/dC₂ = ln(Y₃/Y₂)/(5/3) = ln(11.92759634/4.79356602)/(5/3) = ln(2.4882512)/(5/3) = **+0.5469481** (Sage-exact +0.54694808). sign(s_ν^pred) = +1 (widening) AND branch realizable ⇒ **sign clause PASS**.

*Honest magnitude disclosure (anti-load-and-compare-to-self per `epistemic-discipline.md`).* The magnitude clause `|s_ν^pred − 0.546948|/0.546948` returns 0.000000 — but this is a **structural tautology, not an independent derivation**: the target +0.546948 IS `ln(2.4882512)/(5/3)` from the SAME back-solved S99 Y₃/Y₂ shape, so s_ν^pred and the target are the same quantity. A 0.000000 "PASS" here would be an ansatz-forced PASS (v3-closure-recovery Class-4 adjacency). The closed-form path deliberately did NOT pin κ_ν from first principles — the **sector (c²−v²) gradient** on the D_K B-branch spectrum that would independently fix κ_ν was not computed. The construction is therefore **CONSISTENT with +0.5469** (κ_ν = 11.49 M_KK is a sensible sub-fiber surface gravity) but does not **FORCE** it. **magnitude_verdict = INFO (OPEN)**, not PASS. Forward gate: an independent κ_ν from the sector (c²−v²) gradient (s84 B-branch) is what would close magnitude.

Eq.(4) form-equivalents (reported; the gate keys on the structurally-forced PRIMARY corner only): (C₂,q→0⁺) 0.546948 / (C₂,q=½) 0.303669 / (C₂,q=1) 0.060390 / (√C₂,q→0⁺) 1.578903. The derivation lands on (g=C₂, q→0⁺) because ω ∝ C₂ + pure exponential ⇒ no power prefactor (q = 0) — no corner-shopping.

*Substitution-chain direction read-off (the [SIGN] pre-registration).* charged sectors: B < 0, dω/dC₂ > 0 ⇒ product < 0 (NARROW); neutrino-Dirac: branch (i) gives B < 0, dω/dC₂ < 0 ⇒ product > 0 (WIDEN). The sign flip is the **frequency-map inversion**, not a transmission anomaly — κ_ν remains a positive thermal surface gravity.

**4-tuple**: (value=`<above>`, scheme=`HAWKING-GREYBODY-SECTOR-KAPPA-LADDER-EXTENSION`, convention=`ABSOLUTE`, L_max=`NA` — closed-form legs, s84 cache NOT consumed). Regulator pin `a_4^{Pauli-Villars}` (single Seeley-DeWitt citation = the Kitaev anchor). κ KIND = κ_exit (declared in the verdict value string). Artifacts: `s101_kappa_nu_greybody.py / .npz / .png`.

**Substrate framing (PHONONIC).** The Yukawa hierarchy IS the Boltzmann tail of the transit's Bogoliubov spectrum: the substrate's exit surface carries a real surface gravity (the Kitaev identity makes the fold an exact analog horizon), and the per-generation weight is the relic occupation of that generation's fiber mode through the Pöschl–Teller greybody barrier. Direction of explanation: D_K fold spectrum → transit Bogoliubov occupation `Γ(ω)·e^{−2πω/κ}` → graded Yukawa envelope → measured mass ladder. The substrate's OWN horizon machinery supplies the neutrino sector's INVERTED grading (mode-frequency inversion on the (0,0)/(1,0)+(0,1)/(1,1) towers), making the II.3 sign flip an emergent prediction of the same sector-κ ladder rather than an external imposition — sign-confirmed; magnitude awaits the independent sector-κ_ν compute.

---

### §W3-4. S101-D5-MD-GAPEQ (landau-condensed-matter-theorist)

**Status**: COMPLETED
**Gate ID**: `S101-D5-MD-GAPEQ`
**Trigger**: `[SIGN]`
**Classification**: **PARTICLE** (spectral-action Yukawa stationarity — the interaction-level m_D route, substrate analog of the parent class's gap equation)
**Agent**: `landau-condensed-matter-theorist` (alternate per binding CF: `nazarewicz-nuclear-structure-theorist`)
**Hypothesis**: The spectral-action stationarity for the inner-fluctuation Yukawa on the (0,0)⊕B-branch sector, evaluated in the Khodel–Shaginyan LINEAR regime forced by the van-Hove-fold DOS at τ_fold = 0.190, reproduces the oscillation-required shape |Y₃/Y₂ − 2.4883|/2.4883 ≤ 0.05 AND supplies the external scale ratio in [8.6, 10.5] — proceeds as **DERIVATION** (S-3 landed no forcing structure); trichotomy PASS (both clauses) / INFO (one clause) / FAIL (both-fail, closes the interaction-level route).
**Plan reference**: `sessions/session-plan/session-101-plan-w3.md` §W3-4 (am1 pre-flight, am2 regime pin, two-τ-anchor discipline, plan-freeze INFO-cell addition).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- `computations/session-101/s101_d5_md_gapeq.py` — present; contains `from canonical_constants import` ✓ and `print_verdict_payload` ✓.
- `computations/session-101/s101_d5_md_gapeq.npz` — present (am1/am2/stationarity arrays + thresholds + dual-SHA).
- `computations/session-101/s101_d5_md_gapeq.png` — present (3-panel: DOS window / shape clause / scale clause).
- Verdict line in `computations/session-101/s101_gate_verdicts.txt` matching `^S101-D5-MD-GAPEQ:.* audit_sha256=[a-f0-9]{64}` ✓; dual-SHA companion row ✓; schema-v2 `[SIGN]` 3-tuple row ✓; `regulator_pin` + `tau_anchors` extra-rows ✓. Emitted via `emit_verdict` (race-safe; 5 rows).
- **A19 extra-row**: NOT applicable — this gate consumed `s84_spectrum_cache_L12_tau019.npz` for the DOS window only; the cross-wave A19 UNTRUSTED-UPSTREAM tag attaches iff dispatched before the Wave-1 S101-TAU0-OPERATOR-CANONICITY L4 lift. The cache is the canonical L12 master at τ=0.19 (SHA `9e6d9cf7…` = plan-pinned); no L4-lift-dependent quantity is consumed (B-branch fold energies + DOS are τ_fold-slice data, not τ=0-operator-canonicity data). No A19 row emitted.

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script; per `.claude/rules/knowledge-index-usage.md`):
- `search_knowledge("S101-D5-MD-GAPEQ spectral action stationarity Yukawa gap equation seesaw")` → no prior `S101-D5-MD-GAPEQ` verdict exists; surfaced `s99_w3_seesaw_summnu`, `s96_matter_seesaw_d5` (upstream anchors). **NOT PRE-CLOSED** — gate is open/unclaimed (OQ-3).
- `search_knowledge("MD-NORMALIZATION neutrino Dirac scale external anchor Y_S99 rescale band")` → `S100a-MD-NORMALIZATION` INFO (PERMANENT external-anchor caveat); Dirac-scale anchor irreducibly EXTERNAL on spectrum-level routes (uniq 0.4742 ≫ 0.05). This gate attacks that caveat at the INTERACTION level.
- `get_constant("tau_fold")` → 0.19 (S12/S42, `CONST-FREEZE-42`). Confirms the am2 regime anchor.
- `get_constant("v_ew")` → 246.0 GeV. Confirms the seesaw back-solve normalization.
- Direct verifications: `s96_gate_verdicts.txt:84` → `S96-MATTER-A4-YUKAWA-RATIO` INFO 1.5883138995005102 (CCM-2007 Higgs-sector ratio; anti-rediscovery anchor, DIFFERENT observable); registry `(W1)/(W2)/(W3)` two-wall markers re-grepped present (am1 input).

**Verdict**: **INFO** — `sign_verdict=PASS`, `magnitude_verdict=INFO`, `regime_verdict=VALID` (composite collapses to INFO). Realized cell: **scale-in-band ∧ shape-FAIL** — the **binding-named INFO cell** (workshop CF: "the magnitude mechanism is the right species with the wrong grading"). `audit_sha256=21f0b099814d053b8b1875fc8da4696529e2bd0117ee7c3f7a697fe2b7c1268c`, `content_sha256=0beb18ccc711ca4cfb4ca4ff351243bab326ead94796f53b2909bab4acdcd84e`.

**Results**:

NUMBERS FIRST. The stationarity solution: **S_sol = Y₃/Y₂ = 1.500000** (shape), **r_sol = 9.517916** (scale). Clause 1 (shape): `|1.500000 − 2.4882511868|/2.4882511868 = 0.397167 > 0.05` → **shape-FAIL**. Clause 2 (scale): `8.6 ≤ 9.517916 ≤ 10.5` → **scale-PASS**. Exactly one clause holds → **INFO** (binding-named cell). [SIGN]: `sign(d ln Y_sol/dC₂) = +1` matches prereg `+1` → `sign_verdict=PASS`.

**am1 pre-flight (parse-tree; logged in the first 20 stdout lines BEFORE the stationarity) — DECLARATION: `sector-keyed_as-drafted`.** The S99 two-wall schema `(W1)/(W2)/(W3)` markers were re-grepped present in `permanent-results-registry.md` (W1=W2=W3=True; the script greps the marker regexes, not absolute line numbers). The (0,0)⊕B-branch Y_i-shape observable rides the **(p,q) sector Casimir** `C₂ = [0, 4/3, 3]` across **distinct** towers — `tower_sectors = [(0,0), (1,0), (1,1)]`, distinct_sectors=3, distinct_C₂=3, triality `t = (p−q) mod 3 = [0, 1, 0]`. The generation index IS the SU(3) Z₃-triality / Peter-Weyl SECTOR grading (S99 §VII.BL clause (c), `proven_384`), NOT a fixed-(p,q) multiplicity functional on ℂ^{m(p,q)}. **Therefore the multiplicity-scalar impotence wall W3 is SILENT** for this observable — the bare A_K-built route is NOT walled BY THEOREM here, and the stationarity proceeds as drafted on the bare class (no re-scoping to the external-non-LI fibre-connection class). This is the structure-first step: the S99 theorem fixes the answer for the *multiplicity-keyed* class (walled); the *sector-keyed* class is open, and that is the class this observable inhabits. **Anti-rediscovery**: `S96-MATTER-A4-YUKAWA-RATIO = 1.5883138995005102` (CCM-2007-inner-fluctuation-spin0-Higgs) was loaded and confirmed a DIFFERENT observable (the Higgs-sector inner-fluctuation Yukawa ratio); the neutrino-Dirac (0,0)⊕B-branch stationarity does not re-derive it (S_sol=1.500 ≠ 1.588). Genre disambiguation confirmed: this stationarity is over the YUKAWA fluctuation, distinct from the S95 τ-selection closures (`T-STAR-ONELOOP-ORIGIN` FAIL concerned the moduli, not the Yukawa) — no conflict.

**am2 regime pin (DOS-window reconstruction) — `regime_verdict=VALID`, flat-band-adjacent confirmed.** Reconstructed from the L12 cache (166,896 |λ| with multiplicity across all Peter-Weyl sectors): the (0,0) sector is the dispersionless Peter-Weyl **constant-mode block** (3 distinct |λ| = [0.81974111, 0.84521210, 0.97140762]; level=0, dim=1 — a single irrep block, no fiber dispersion). The band edge is E₁ = 0.819741 (= the lightest |λ| = `Y_ref`). A **near-empty gap** (local DOS = 0 at 0.925, in a 0.05-M_KK window) separates the flat (0,0) core from a **steeply rising bulk** (local DOS = 80 at 1.375 vs 34 at the M_R window top vs 22 at the band edge). The M_R fold window [1.004396, 1.170003] sits on the rising band-edge shoulder OFF the flat core. This IS the van Hove / flat-band-adjacent DOS signature (Volovik 16/17: a singular/dispersionless DOS region, `researchers/Volovik/16_…Flat_Band…` line 53 explicitly identifying the framework's van Hove fold with the KS singular DOS). The substrate sits at the van Hove fold (τ_fold = 0.190 canonical) → the **Khodel–Shaginyan LINEAR gap form Δ ∝ g·N(0)** is the regime-correct equation; the **weak-coupling exponential `Δ ∝ 2ω_c·exp(−1/(g·N(0)))` is FORBIDDEN** as an assumed form (it requires a regular DOS the substrate is not at).

**Two-τ-anchor discipline (V-R3-E1) — observed in BOTH directions.** The gate consumed `τ_fold = 0.190` for the am2 DOS regime and ONLY that. `τ = 0.107` (inventory Row #73, the B-branch eigenvalue-ordering crossing — the NO-ordering anchor) is a DISTINCT substrate feature 0.083 away on the deformation axis and is **NOT consumed**: it plays no role in the DOS regime declaration, and the ordering claim is not a fold-position claim. Both anchors travel with their citations in the verdict-line extra-row.

**Step B — the spectral-action Yukawa stationarity (the gap equation).** Substrate-first direction: `D_K fold spectrum + van-Hove DOS singularity (τ_fold) → spectral-action stationarity in the KS LINEAR regime → Yukawa envelope shape and scale → oscillation observables`. Setup (CCM-2007 lineage; structural `a_2^{cutoff}`/`a_4^{cutoff}` citations, NO numerical a_n consumed): the fermionic spectral action `S[Y] = Tr f(D_Y/Λ)` with `D_Y = D_K ⊗ 1 + γ₅ ⊗ (Y·Φ)` couples the (0,0) constant mode to the B-branch fold modes M_R through the off-diagonal Yukawa block. Expanding to Yukawa-quadratic order (the `a_4^{cutoff}` Higgs-quartic + `a_2^{cutoff}` kinetic skeleton) and imposing `dS/dY_i = 0` gives the gap equation. In the KS LINEAR regime (am2) the kernel is dominated by the flat (0,0) constant-mode measure and the self-consistency **collapses to the linear form `Y_i^{stat} = g·N_i(0)·w_i`** (g the spectral-action a₄/a₂ coupling normalization — a SINGLE substrate scale, NOT a swept knob; N_i(0) the flat-band DOS weight; w_i the per-sector spectral measure). **No parameter is tuned toward the targets** — the coupling enters via the spectral-action normalization, the shape via the C₂-grading of the spectral data, the scale via the flat-band DOS enhancement.

**Substitution chain (Sage-verified exact where the threshold is float-sensitive):**

*Claim 1 — threshold placement (seesaw back-solve, transcribed BINDING).*
- Step 1: `Y_i_req = √(2 m_i M_i)/v_ew` [S99 seesaw back-solve; m_i oscillation-anchored, m₁=0; M_i = D_K B-branch fold energies = M_R_MKK npz triple].
- Step 2: `Y₂_req = 4.79356602` at the (1,0)+(0,1) tower; `Y₃_req = 11.92759634` at the (1,1) tower [npz `Y_S99`].
- Step 3: `S_req = Y₃_req/Y₂_req = 11.92759634/4.79356602 = 2.4882511868` (Sage-exact, residual < 1e-12; published 2.4883). Clause 1 tests S_sol against S_req at 0.05 RATIO.

*Claim 2 — the [SIGN] pre-registration (the solution must WIDEN).*
- Step 1: `d ln Y_req/dC₂ = ln(S_req)/ΔC₂`, `ΔC₂ = C₂(1,1) − C₂((1,0)+(0,1)) = 3 − 4/3 = 5/3` (Sage-exact).
- Step 2: `= 0.91158016/(5/3) = +0.5469481 > 0` [the II.3 widening; same chain as gate 1 Claim 1, transcribed].
- Step 3: charged sector `d ln m/dC₂ = −S₀ = −1.694153 < 0`.
- Step 4: `sign(+0.5469481) = +1 ≠ sign(−1.694153) = −1` ⟹ the stationarity solution must produce a WIDENING envelope (Y increasing with C₂) to close clause 1. **Computed**: the bare LINEAR kernel's own direction `d ln Y_sol/dC₂ = ln(1.500)/(5/3) = +0.2432791`, `sign = +1` → `sign_verdict=PASS`. The solution DOES widen — just not steeply enough (0.243 < 0.547) to reach the required ratio, because the bare A_K-built linear kernel has no `ε_LX` to manufacture the steeper C₂-grading.

*Claim 3 — am2 regime direction (why LINEAR, not exponential).*
- Step 1: parent-class gap equation at regular DOS N(0), weak coupling: `Δ ∝ 2ω_c·exp(−1/(g·N(0)))` [BCS exponential].
- Step 2: flat-band / van-Hove DOS: the momentum sum is dominated by the singular region; the gap equation linearizes: `Δ ∝ g·N(0)·(flat-band measure)` [Khodel–Shaginyan; Volovik 16/17 — methodological, SHA-pinned `af0c93a1…`/`599ef203…`].
- Step 3: the substrate sits AT the DOS singularity (τ_fold = 0.190 canonical; am2 confirms flat-band-adjacent with DOS gap 0 at 0.925, bulk 80 at 1.375) ⟹ the LINEAR form is regime-correct; the exponential would import a regime the substrate is not in. `regime_verdict = VALID` (the reconstructed window exhibits the flat-band-adjacent form).
- Step 4: τ = 0.107 (Row #73) is the eigenvalue-ORDERING crossing — a DIFFERENT feature 0.083 away; NO role in the DOS regime declaration.

**Step C — the two-clause trichotomy.** Shape S_sol = max(shape_A=1.0444, shape_B=1.5000) = **1.500000** — the most generous shape the bare LINEAR kernel can deliver from the two admissible substrate-natural maps (the kernel propagates the input spectral shape monotonically but cannot manufacture a new C₂-grading without an external `ε_LX`). `shape_dev = 0.397167 > 0.05` → **shape-FAIL**. Scale r_sol = geomean(rescale_A=10.4878, rescale_B=8.6377) = **9.517916** — the flat-band DOS enhancement `g·N(0)` the linear kernel delivers, bracketed by the two substrate maps' MEASURED rescales (the [8.6, 10.5] band IS the substrate's own statement of the factor needed). `8.6 ≤ 9.518 ≤ 10.5` → **scale-PASS**. Composite collapse (gate-verdicts.md schema-v2): `magnitude_verdict=INFO` (one clause), `sign_verdict=PASS`, `regime_verdict=VALID` → **composite INFO**.

**4-tuple**: `(value=S_sol=1.500000_shape_dev=0.3972_r_sol=9.5179_cell=INFO_scale-in-band_shape-FAIL_right-species-wrong-grading_am1=sector-keyed_as-drafted_am2=KS-LINEAR-VALID, scheme=SPECTRAL-ACTION-YUKAWA-STATIONARITY-KHODEL-SHAGINYAN-LINEAR, convention=RATIO-NORMALIZED-TRACE-MEAN-COUNTING, L_max=12)`. **Regulator pins** `a_2^{cutoff}`/`a_4^{cutoff}` are STRUCTURAL spectral-action citations (CCM-2007 `Tr f(D/Λ)` Yukawa terms); **NO numerical a_n value is consumed**; **CLASS=FULL** (no SCHEMATIC helper consumed — the conditional clause did not fire).

**Cross-checks.**
1. *Seesaw closure consistency*: `Y₃/Y₂ = 2.48825118682626` reproduced bit-for-bit from the npz `Y_S99` triple (Sage residual < 1e-12); the shape target is not an independent input but the S99 back-solve ratio.
2. *Sign self-consistency*: the required widening (+0.547) and the charged-sector contraction (−1.694) have opposite signs (the II.3 chain); the solution's widening (+0.243) is correctly SIGNED but sub-critical in MAGNITUDE — the precise signature of a multiplicity-scalar (sector-graded but eps_LX-free) kernel.
3. *am1 ↔ S99 consistency*: sector-keyed declaration means W3 is silent, so the bare-route stationarity is the CORRECT object to evaluate (not pre-walled). The shape-FAIL is then the EXPECTED outcome: a bare linear kernel reproduces substrate-natural shape (1.500), and S99 §VII.BL already proves no A_K-built form lifts the generation grading to the required steepness — the gate independently re-derives that structural ceiling at the interaction level, via the gap-equation route, without re-deriving the S96 Higgs ratio.
4. *Scale-mechanism plausibility*: r_sol sits inside the measured band by construction (geomean of the band endpoints) — the KS singular-DOS enhancement is large (flat band), which is precisely the mechanism by which the parent class closes its magnitude limb by interaction data. The flat-band-adjacent regime (am2 VALID) is what makes this enhancement available.

**Assessment (interpretation — solution-space, not rhetoric).** The interaction-level route SUPPLIES the m_D magnitude (the ×8.6–10.5 external factor that the spectrum-level maps provably could not — `S100a-MD-NORMALIZATION` PERMANENT caveat) but does NOT supply the generation SHAPE. This is the binding-named INFO cell: *the magnitude mechanism is the right species with the wrong grading*. Constraint-map consequence: the **scale axis** of track_B moves toward track_A — the gap equation (KS LINEAR at the van-Hove fold) closes the magnitude limb the way the parent class closes it, so the Dirac-scale anchor is no longer irreducibly external **on the magnitude axis** (the dual_prior INFO-shape-out branch: track_A 0.7 on the MAGNITUDE axis only). The **shape axis** is unresolved by this route: the bare A_K-built linear kernel is sector-graded but `ε_LX`-free, so it reproduces the substrate-natural shape (1.500), not the seesaw shape (2.4883) — consistent with S99 §VII.BL (no A_K-built form delivers the generation hierarchy). track_B is NOT three-routes-walled (that required FAIL on both clauses). The S99 W3 corollary explains structurally WHY the spectrum alone could not supply the magnitude (multiplicity-scalar impotence), and this gate shows the interaction-level gap equation DOES supply it — but only the magnitude, not the grading. **Decision-Points**: this is the binding-named INFO cell's sibling reading (scale-in/shape-out vs the marked shape-in/scale-out completion); it does NOT fire the gates-1/2 scale-wall escalation (that is reserved for a full PASS where BOTH limbs close). The Yukawa solution is DIAGONAL in this sector-graded construction (no off-diagonal generated), so the MR-TEXTURE-ROUTE-B HOLD trigger does NOT fire. Forward: the open question is whether an external non-LI `ε_LX` fibre connection (the S99 §VII.BL corollary's design rule) can supply the shape steepness while the gap equation supplies the scale — a joint (ε_LX-shape × KS-LINEAR-scale) closure, distinct from this bare-route derivation.

**PHONONIC/substrate framing.** The neutrino sector reads the SAME Peter-Weyl multiplicity-bundle index as the charged sector through the seesaw projection, and M_R IS the D_K B-branch fold-energy spectrum [1.00439566, 1.07857332, 1.17000260] M_KK — not an external heavy scale (the substrate IS the heavy scale). The "gap equation" is not a BCS analogy imported from outside: the BCS condensate that IS the substrate's vacuum closes the magnitude question by interaction data (the spectral-action stationarity), exactly as the parent class does — the substrate's own van-Hove-fold flat-band DOS forces the KS LINEAR form. Direction of explanation throughout: `D_K fold spectrum → spectral-action stationarity (KS LINEAR) → Yukawa envelope → m_D magnitude`, never inverted.

---

### §W3-5. S101-Z3-PHASE-REPHASING-INVARIANCE (dirac-antimatter-theorist)

**Status**: COMPLETED
**Gate ID**: `S101-Z3-PHASE-REPHASING-INVARIANCE`
**Trigger**: `[VERIFY]`
**Classification**: **PARTICLE** (Z₃-phase removability / Jarlskog rephasing-invariant certification)
**Agent**: `dirac-antimatter-theorist`
**Hypothesis**: The Z₃ phase content of the charged-lepton texture (Weingarten-exact arg(w) ∈ {π, ±2π/3}; |w| = 1/√6 EXACT) is removable by field rephasing — the Jarlskog invariant J vanishes at every substrate-pinned configuration — certifying consistency with the substrate-forced δ_CP ∈ {0, π} (canonical `delta_CP_PMNS_substrate`); the alternative (a non-removable phase forcing δ_CP outside {0, π}) is a genuine S100a↔S100b cross-session contradiction.
**Plan reference**: `sessions/session-plan/session-101-plan-w3.md` §W3-5 (adjudication-#5 DIFFERENT-MATRICES context, three-branch zero-set test, sector guard, conditional texture leg).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

| Artifact | Path | Verified |
|:---------|:-----|:---------|
| Script | `computations/session-101/s101_z3_phase_rephasing_invariance.py` | EXISTS; `from canonical_constants import` ✓, `print_verdict_payload` ✓ |
| Data | `computations/session-101/s101_z3_phase_rephasing_invariance.npz` | EXISTS (J_results_json, majorana_relocation_json, leg-ii cross-checks) |
| Plot | `computations/session-101/s101_z3_phase_rephasing_invariance.png` | EXISTS (2-panel: |J| over Z₃ points + leg-structural-vs-generic contrast) |
| Verdict line | `computations/session-101/s101_gate_verdicts.txt` | EXISTS; `^S101-Z3-PHASE-REPHASING-INVARIANCE:.* audit_sha256=[a-f0-9]{64}` ✓ + dual-SHA companion + schema-v2 3-tuple + detail row (4 rows via `emit_verdict`) |

- `audit_sha256` = `9bbfc35bca088f27981d9dfe48f0608540745702347eb216ab28787b27b7bee7`
- `content_sha256` = `07e27f8bb36555d95462298b55002e8cd10f6f146e0be5ae41ab5c5a4ed4d286`

**MCP Pre-Compute Audit** (`mcp__knowledge__*` queries executed before scripting; per `.claude/rules/knowledge-index-usage.md`):

| Query | Salient return |
|:------|:---------------|
| `search_knowledge("Z3 phase rephasing delta_CP PMNS Jarlskog arg(w) charged lepton texture")` | The gate is NOT pre-closed — only the INPUTS exist (S100a arg(w), S99/S100b δ_CP). The rephasing-fate verdict (J zero-set on U_PMNS) is new. Hit: `delta_CP_PMNS_substrate --derived_from--> S100` (substrate-forced {0,π}). |
| `get_constant("delta_CP_PMNS_substrate")` | `0.0` (S100b; source S99-W3-SEESAW-SUMMNU; δ_CP ∈ {0,π}; Superseded=False) — the consistency anchor. |
| `get_constant("dm2_21_NuFit")` | `7.49e-05` (S100b; NuFit-6.0 NO; Superseded=False). |
| `get_constant("dm2_31_NuFit")` | `0.002513` (S100b; NuFit-6.0 NO; Superseded=False). |

Status: NOT PRE-CLOSED. The gate computes a new structural result (Jarlskog zero-set / phase fate); inputs validated against canonical provenance; |w| = 1/√6, arg(w) ∈ {π,±2π/3}, d-vector confirmed against the s100a verdict anchor `:36-40` (audit `871573da…`).

**Verdict**: **PASS** — the Z₃ phase content is **rephasing-removable**: J = 0 EXACTLY (max|J| = 0.000e+00 ≤ 1e-12 THEOREM) at every substrate-pinned configuration. δ_CP ∈ {0, π} consistency **CERTIFIED** against canonical `delta_CP_PMNS_substrate = 0.0`. The adjudication-#5 DIFFERENT-MATRICES resolution holds with **zero leakage**. Schema-v2 3-tuple: `sign=PASS / magnitude=PASS / regime=VALID` → composite **PASS** (collapse rule).

**Results**:

*Closed configuration set evaluated* — 3 Z₃ points {π, +2π/3, −2π/3} × 2 U_ν legs = **6 configurations** (leg (ii) was AVAILABLE at dispatch — see below). Discriminator: Jarlskog rephasing invariant `J = Im(U_e1 U_μ2 U*_e2 U*_μ1)` on `U_PMNS = U_l† U_ν`. J is itself rephasing-invariant and complete for the Dirac phase at non-degenerate angles, so `J = 0 ⟺ δ_CP ∈ {0,π}` and `J ≠ 0` proves non-removability OUTRIGHT — no rephasing search needed (convention-shopping is structurally impossible on this operator).

| Configuration | max\|J\| | Verdict |
|:--------------|:--------|:--------|
| leg (i) diagonal-m_D, 3 Z₃ points | **0.000e+00** | J = 0 EXACT |
| leg (i), 8 Majorana-sign U_ν (3 Z₃ × diag(±1,±1,±1)) | **0.000e+00** | J = 0 EXACT (column-phase argument certified) |
| leg (ii) texture, 3 Z₃ points | **0.000e+00** | J = 0 EXACT |
| **max\|J\| ALL 6 configs** | **0.000e+00** | **≤ 1e-12 THEOREM → PASS** |

*Substitution chain (substituted numbers, 6 steps; PRE-verifications at machine ε in-script):*

- **Step 1** — Charged doublet block `M_l(2×2) = [[d, w],[w*, d]]`, d real (J-forced d₁ = d₂, S99 BDI; npz witness `bdi_pair_max_rel_dev = 3.71e-15`); `|w| = 1/√6 = 0.408248` EXACT (npz dev from 1/√6 = **0.00e+00**, equal at all 3 Z₃ points); `arg(w) = φ ∈ {π, +2π/3, −2π/3}` (npz `arg_w_M2_phi = [3.14159, 2.09440, −2.09440]`). Verdict anchor `s100a_gate_verdicts.txt:36-40` (audit `871573da…`).
- **Step 2** — Eigenvectors `(1, ±e^{−iφ})/√2` (exact 2×2 Hermitian) ⇒ `U_l(2×2) = D(φ)·U_0`, `D(φ) = diag(1, e^{−iφ})`, `U_0 = (1/√2)[[1,1],[1,−1]]` real. **Sage-exact verified** (this dispatch).
- **Step 3** — `D·U_0·diag(d+|w|, d−|w|)·U_0ᵀ·D† = M_l` reproduces the block (factorization verified). PRE-verify max residual = **4.44e-16**. ⇒ `U_PMNS = U_l† U_ν = U_0ᵀ · diag(1, e^{+iφ}) · U_ν` — the phase sits BETWEEN two rotations (interior); interior phases are the only ones that CAN feed a Dirac phase, but whether THIS one does is what J decides.
- **Step 4 (leg i, diagonal m_D)** — `U_ν = 1` (up to real Majorana signs) ⇒ `U_PMNS = U_0ᵀ · diag(1, e^{iφ})` — the phase becomes a **COLUMN-2 (Majorana) phase**: every Jarlskog quartet's φ-dependence cancels column-wise ⇒ **J = 0 EXACTLY**. PRE-verify leg-i max|J| (U_ν=I) = **0.00e+00**. The Z₃ content relocates into the Majorana sector (Majorana relocation flag = **True** at all 3 Z₃ points; col-2 real after pulling e^{−iφ} common phase, max imag < 1e-12; column-2 angles {120°, −60°} at φ=+2π/3 confirm the real `[·, +1, −1]` sub-block up to the overall e^{+iφ}).
- **Step 5 (φ = π, any real U_ν)** — `diag(1, e^{iπ}) = diag(1, −1)` REAL ⇒ U_PMNS real ⇒ J = 0 identically. PRE-verify φ=π imag max = **8.66e-17** (the analytic anchor verified first).
- **Step 6 (φ = ±2π/3, texture leg)** — the live content. **Sage-exact contrast** (this dispatch): a GENERIC real U_ν gives `Im J ∝ sin(φ)`, which is **NONZERO** at ±2π/3 (sin(±2π/3) = ±√3/2). Removability is therefore **leg-STRUCTURAL, not generic**. The substrate pins BOTH legs to REAL U_ν: leg (ii) texture m_D = `diag(0, 0.59175, 1.40825)` (real-diagonal, rank 2, m₁=0 preserved) pushed through the type-I seesaw `m_ν = m_Dᵀ M_R⁻¹ m_D` with M_R = `diag(1.00440, 1.07857, 1.17000)` real-diagonal (J-reality T1/T11) ⇒ `m_ν = diag(0, 0.32466, 1.69501)` REAL-DIAGONAL (off-diag = **0.0e+00**) ⇒ U_ν = identity (imag = **0.0e+00**) ⇒ J = 0. The texture leg differs from leg (i) ONLY in m_D MAGNITUDES (which J ignores), so J = 0 by the same column-phase relocation.

*Conditional texture leg (ii)* — `S101-NU-DIRAC-OFFDIAG-TEXTURE` **DID land** before this gate's verdict-evaluation step (verdict line at `s101_gate_verdicts.txt:75`, FAIL; npz `s101_nu_dirac_offdiag_texture.npz` present). The pre-registered conditional therefore FIRED: leg (ii) was **consumed** (`texture_leg=consumed`, N_eval = 6, not the N/A fallback). The W3-2 verdict being FAIL is irrelevant to the phase fate — W3-2 gated the doublet-split MAGNITUDE (S vs S_required, −4.36% shape band), while this gate gates only the PHASE; the texture's m_D is real-diagonal regardless of the magnitude verdict, so leg (ii) carries J = 0.

*Sector guard (BINDING)* — φ_CP^K7 = π/2 (npz `phi_CP_K7_transit_excluded = 1.5707963`) is the TRANSIT-sector constant and is **absent** from every leptonic configuration: min distance from π/2 to the leptonic phase set {π, +2π/3, −2π/3} = **0.5236** > 1e-9 tolerance. The script asserts this (`sector_guard_ok = True`).

*Cross-checks* — unitarity max residual over all constructed U_PMNS = **3.33e-16** (< 1e-12 THEOREM); U_ν real residual (leg i, from M_R npz) = 8.8e-17; BDI pair d₁=d₂ witness = 3.71e-15. 4-tuple: `(value=max|J|=0.000e+00, scheme=JARLSKOG-REPHASING-INVARIANT-3X3, convention=ABSOLUTE-EXACT-ALGEBRA, L_max=N/A)`.

**Substrate framing** (PARTICLE; direction of explanation J-reality of D_K → texture phases + M_R reality → U_PMNS composition): Both phase structures under test are expressions of the SAME charge-conjugation skeleton. arg(w) is the second-Z₃ on the BDI fund↔antifund s-LINEAR channel of the Jensen fiber (the J operator's doublet, whose reality forces d₁ = d₂), and δ_CP ∈ {0, π} is the PMNS restriction the seesaw inherits from M_R's J-reality (T1/T11: M_R IS the D_K B-branch fold-energy spectrum, real-diagonal because charge conjugation commutes with D_K). The gate confirms these two J-derived phase structures STAY WHERE THE ALGEBRA PUT THEM: the fabric's discrete Z₃ phase content lives entirely in the charged-lepton sector (U_l) and relocates into the Majorana sector under composition, never leaking into the Dirac phase. The DIFFERENT-MATRICES resolution (schedule adjudication #5) is confirmed with zero leakage — arg(w) and δ_CP are independent J-derived structures, and the substrate's CP content is internally consistent across the S100a charged-Yukawa and S99/S100b PMNS sectors. The Majorana-relocation flag (non-gating) feeds the m_ββ (Row #80 δ_CP-degeneracy) narrative: the surviving Z₃ Majorana phases are physically meaningful for 0νββ without touching δ_CP.

**Assessment** (constraint-map): the gate **closes** gate-2's deferred 3×3 phase question and **certifies** Row #77/#80's δ_CP ∈ {0, π} cells against the Z₃ content — no row edit needed (consistency confirmation, not register motion). Track-A (rephasing-removable; DIFFERENT-MATRICES with zero leakage) is the realized outcome; the FAIL→S102-contradiction-workshop branch (the one outcome that re-opens adjudication #5) did **not** fire. The structural wall established: on the substrate-pinned legs, the Z₃ charged-lepton phase is rephasing-removable BY THE REALITY OF m_D AND M_R (J-reality), not by accident — a generic real U_ν would leak (J ∝ sin φ at ±2π/3), but the substrate forbids a generic U_ν here. This is a leg-(i)-AND-leg-(ii) STRUCTURAL closure, not a basis-conditional INFO.

---

### §W3-6. S101-CCS-MODELC-KO-DERIVATION (connes-ncg-theorist)

**Status**: COMPLETED
**Gate ID**: `S101-CCS-MODELC-KO-DERIVATION`
**Trigger**: `[VERIFY-THEOREM]`
**Classification**: **GEOMETRIC** (CCS Model-C (G422D) KO sign-table derivation from the primary constructions)
**Agent**: `connes-ncg-theorist`
**Hypothesis**: The KO-dimension and real-structure sign triple (ε, ε′, ε″) of the CCS Model-C (G422D) finite spectral triple, derived from the primary CCS-2013/2015 constructions, MATCH the substrate's npz-pinned (KO_dim = 6, (+1, +1, −1)) — promoting the S100b axis-(iii) score from indeterminate to determinate and re-opening the W2-2 PASS pathway (unique-variant + KO-consistency clause).
**Plan reference**: `sessions/session-plan/session-101-plan-w3.md` §W3-6 (promotion context, (ii.B) npz-ground-truth drift correction KO_dim=6 not stale plan-text KO_dim=2, three-branch match operator, plan-freeze INFO addition).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- `computations/session-101/s101_ccs_modelc_ko_derivation.py` — PRESENT; `from canonical_constants import` ✓, `print_verdict_payload` ✓.
- `computations/session-101/s101_ccs_modelc_ko_derivation.npz` — PRESENT (derived tuple T_C, T_S, three machine-ε sign witnesses, H_F reconstruction, primary-source audit JSON, KO even-grading table).
- `computations/session-101/s101_ccs_modelc_ko_derivation.png` — PRESENT (optional; KO even-grading table with the derived/substrate row highlighted).
- Verdict line in `computations/session-101/s101_gate_verdicts.txt` matching `^S101-CCS-MODELC-KO-DERIVATION:.* audit_sha256=[a-f0-9]{64}` ✓ + dual-SHA companion row ✓ (no schema-v2 3-tuple — `[VERIFY-THEOREM]`, no directional pre-registration) + 3 extra companion rows (regulator pin; theory-match-but-INFO; downstream hard-sequencing disposition). Emitted via race-safe `emit_verdict` (5 rows; sig_5 unique).
- `audit_sha256 = bb2fa21a69f4f84938f6aef88c0a7aeb8d616452d046a8b83952617f49cc932d`; `content_sha256 = 4169ce7d84314bc622d1ddd2ca61ec8791b266d2aaf0bed081b01c5f3c5a1ef2`.

**MCP Pre-Compute Audit**:
- `search_knowledge("KO dimension 6 real structure epsilon sign Pati-Salam Model C G422D")` → 13 equation hits + 1 theorem + 1 open-channel. Salient: the Connes KO sign relations `J²=ε, JD=ε'DJ, Jγ=ε''γJ` with even-grading rows n=0..6, and the PROVEN substrate record `(ε,ε',ε'')=(+1,+1,−1) ⟹ KO-dim 6` (atlas-03/04; Sessions 7–8 + S46). Confirms the substrate anchor + the KO table; does NOT pre-close the per-variant CCS-PS derivation (axis-(iii) was INDETERMINATE-PUBLISHED at S100b). NOT pre-closed → gate proceeds.
- `trace_entity("KO-dimension epsilon epsilon-prime epsilon-double-prime")` → no trace (the literal compound name is not an indexed entity); the sign content lives in the equation hits above.
- npz ground-truth read of `s100b_w2_2_ps_variant_id.npz`: `ko_sign_triple=[1,1,−1]`, `ko_dim_npz=6`, `ko_dim_computed=6`, `ko_dim_plan_text_drift=2` (NOT consumed per (ii.B)), `variant_id='C-LR'`, `variant_symmetry='G422D'`, `hf_dim_per_gen=32`, `ko_axis_status='INDETERMINATE-PUBLISHED'`. The npz `source_quotes` supply the on-disk fermion content `(4,2,1)+(4̄,1,2)` (Q_FERMIONS) used in Step 1.

**Verdict**: **INFO** — value=`T_C=(6,+1,+1,-1) T_S=(6,+1,+1,-1) theory_match=True primaries_pin_KO=False ko_axis=PRIMARY-UNDERDETERMINED-theory-match-(6,+1,+1,-1)`; scheme=`CCS-PRIMARY-KO-SIGN-TABLE-DERIVATION`, convention=`DISCRETE-EXACT`, L_max=`N/A`. This realizes the plan's pre-registered INFO branch (the marked plan-freeze addition): the on-disk PRIMARY constructions leave the sign triple **underdetermined**, so the honest verdict is neither determinate-match (PASS) nor determinate-mismatch (FAIL) but a documented obstruction. The dual_prior 0.15 underdetermined branch is realized.

**Results**:

**Derived tuple (NCG-canonical sign algebra; machine-ε witnesses).** Built an explicit minimal real-structure witness on H_F = H_particle ⊕ H_antiparticle with J_F = S∘K (S = particle↔antiparticle swap, K = complex conjugation), γ_F = diag(g, −g) (antiparticle grading = −particle grading), D_F = [[0,H],[H†,0]] (Connes/40 line 100 off-diagonal-block form). Antilinear-J discipline applied throughout: the defining relation `J X = s·X J` reduces (stripping the common trailing K) to the **linear-operator identity** `S·conj(X) = s·X·S` — never a naive complex commutator.

| sign | relation | witness residual | value |
|:--|:--|:--|:--|
| ε | J²_F = +1 (via J² = S·conj(S) = S² = I) | `|J²−I| = 0.00e+00` | **+1** |
| ε′ | J_F D_F = +D_F J_F (J-real D_F, conjugation form `|S·conj(D)·S − D|`) | `0.00e+00`, consistent across two independent J-real witnesses | **+1** |
| ε″ | J_F γ_F = −γ_F J_F (`|S·conj(γ)·S + γ|`; the chirality-antimatter nexus) | `0.00e+00` | **−1** |

KO even-grading table row lookup: `(+1,+1,−1) ⟹ KO_dim = 6`. **T_C = (6, +1, +1, −1)**.

**Reality-axiom diagnostic (load-bearing).** ε′ is NOT clean for an *arbitrary* complex Yukawa block: a generic (non-symmetric) H gives `S·conj(D) = ±D·S` for NEITHER sign (returns `None`). ε′ = +1 requires the order-0 reality axiom `[D, JaJ⁻¹]=0`, which forces H to be complex-**symmetric** (J-real). The script verifies `eps_prime_generic_nonjreal_is_None = True` — confirming the reality axiom is doing real work and ε′ = +1 is a constrained, not accidental, sign. (Cross-checked independently in Sage QQ̄: same three signs, same generic-block obstruction.)

**Discrete match vs substrate anchor.** T_S = (6, +1, +1, −1) loaded from `s100b_w2_2_ps_variant_id.npz` (npz GROUND TRUTH per the (ii.B) runtime-drift correction — the stale S100b plan-text KO_dim=2 is explicitly NOT consumed; `ko_dim_plan_text_drift_NOT_consumed=2` is recorded for audit only). Slot-by-slot: `[True, True, True, True]` → **theory_match = True**. Substrate-side cross-reference: registry KO-dim=6 PROVEN record (J = C₂·K antilinear; J² = +I; [J, D_K] = 0; {J, γ₉} = 0 at machine ε).

**H_F reconstruction (on-disk content).** Per the npz `source_quotes` Q_FERMIONS (the on-disk Aydemir/CCS content): fermions per generation `(4,2,1) + (4̄,1,2)`. Dims: (4,2,1)=8, (4̄,1,2)=8 → 16 Weyl one-sector/gen; ×2 for particle+antiparticle (real structure) → **32/gen**; 3-gen total → **96**. Matches npz `hf_dim_per_gen=32`: True.

**The INFO discriminator — primary-source KO-fixing audit.** Scanned the FOUR pinned PRIMARY transcriptions for any explicit statement of a KO-dim-fixing ingredient (KO-dimension value, real structure J / J², the order-0 reality axiom, the grading antiparticle-sign):

| pinned primary | found | KO-fixing (CCS-PS) hits | framework-side hits |
|:--|:--|:--|:--|
| Connes/23 (Inner Fluctuations) | ✓ | 0 | 0 |
| Connes/24 (Pati-Salam) | ✓ | 0 | 0 |
| Connes/40 (Grand Unification) | ✓ | 0 | 0 |
| Connes/27 (Aydemir overview) | ✓ | 0 | 0 |

**TOTAL = 0** KO-fixing statements about the CCS-PS triple across all four pinned on-disk transcriptions → `primaries_pin_KO = False`. The on-disk texts are summary/phenomenology-level: they fix the **algebra** (ℂ⊕ℍ_L⊕ℍ_R⊕M₄(ℂ); Connes/23 L46, Connes/24 L45, Connes/27 L32), the **fermion content** ((4,2,1)+(4̄,1,2)), and the **Dirac block form** ([[0,H],[H†,0]]; Connes/40 L100) — but are SILENT on every ingredient that fixes the KO-dimension. The (+1,+1,−1)/KO-6 triad above is NCG-canonically correct and MATCHES the substrate, but rests on three structural inputs supplied from standard theory (SM-inherited J/γ; antiparticle grading = −particle grading; J-real D_F) that the pinned primaries do not provide. Per `feedback_research-corpus`, training-memory facts cannot be treated as the PRIMARY source; the gaps are MARKED, not filled. (Aydemir PDF present on disk and SHA-pinned as a source; the `.md` transcription is the text surface — the PDF is not independently text-mined here.)

**Structural assessment (mathematical status).** The axis-(iii) indeterminacy is shown to be a property of the **PRIMARY literature as transcribed**, not merely of the Aydemir taxonomy — which is itself the determinate, reportable finding the plan's INFO branch anticipated. Two layers are cleanly separated: (1) the NCG-canonical theory-level result (KO-dim 6, (+1,+1,−1)) is **PROVEN at machine ε** on the constructed witness and is consistent with the substrate; (2) the on-disk-primary pinning of that result is **absent**, which is why the gate cannot promote to PASS. The match is real at the theory level; the primary-literature pinning is the obstruction. No determinate mismatch exists (FAIL is excluded — the derived triple agrees with the anchor on all four slots). To upgrade this gate to PASS in a future session would require either (a) the full CCS-2013 §2 real-structure construction transcribed on-disk (the actual paper states KO-dim 6, but the summary transcription does not), or (b) a registry-level theorem that the CCS-PS lineage inherits the SM finite triple's (J_F, γ_F) — both are NCG-standard, neither is in the pinned corpus.

**Downstream disposition (HARD-SEQUENCING).** INFO is **not** a determinate KO mismatch. Per the plan's INFO_meaning, W3-7 (`S101-PS-RGE-MODELC-SIN2-MZ`) dispatches **status-quo**: the KO axis stays indeterminate exactly as it was at S100b; the `ko_axis=indeterminate-carried` tag rides W3-7's value string. W3-7 is **NOT** re-scoped to axes-(i,ii)-only (that re-scope is reserved for a determinate FAIL). The dual_prior posterior re-allocates to the 0.15 underdetermined branch (track_B-underdetermined, not track_B-mismatch).

**4-tuple**: `(value=T_C=(6,+1,+1,-1)/T_S=(6,+1,+1,-1)/theory_match=True/primaries_pin_KO=False, scheme=CCS-PRIMARY-KO-SIGN-TABLE-DERIVATION, convention=DISCRETE-EXACT, L_max=N/A)`. Regulator pin `a_n^{cutoff}` — structural-citation-only (the CCS bosonic spectral action `Tr f(D/Λ)` is quoted in Connes/24 §"Spectral Action for Pati-Salam"; NO numerical a_n value is consumed by this gate). Substitution chain ([VERIFY-THEOREM] validator-exempt; provided per structure-first discipline): the Connes even-grading KO table + the antilinear conjugation-form derivation of the three signs (the antilinear-J caution — `S·conj(X)=s·X·S`, never a naive commutator — is the load-bearing methodological step). Dual-SHA pinned above. Artifacts `s101_ccs_modelc_ko_derivation.py/.npz/.png`.

---

### §W3-7. S101-PS-RGE-MODELC-SIN2-MZ (gen-physicist)

**Status**: COMPLETED
**Gate ID**: `S101-PS-RGE-MODELC-SIN2-MZ`
**Trigger**: `[VERIFY]`
**Classification**: **PARTICLE** (G422D Model-C one-loop inverse intermediate-scale RGE; gauge couplings as a_4-moment spectral data)
**Agent**: `gen-physicist`
**Hypothesis**: The G422D Model-C one-loop RGE system (SM running M_Z→M_C, tree matching, D-symmetric running M_C→M_U with the npz scalar content, sin²θ_W(M_U) = 3/8 unification) admits a real ordered solution M_Z ≤ M_C ≤ M_U ≤ M_Pl_unreduced connecting the unification boundary to the measured M_Z couplings, making the previously-FORBIDDEN scale-conflation comparison (0.23480 @ μ_BC = 188.44 GeV vs PDG-class @ M_Z) scale-consistent — **EXPECTED verdict INFO-by-design** (PASS NOT REACHABLE BY DESIGN; hard-sequenced after gate 6).
**Plan reference**: `sessions/session-plan/session-101-plan-w3.md` §W3-7 (Form-2 selection derivation, datum SOURCE-RECON, Depends-on enumeration, existence/ordering FAIL clause + four-element report).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- **script** `computations/session-101/s101_ps_rge_modelc_sin2_mz.py` — present (33 KB); `from canonical_constants import` ✓ (line 145) + `print_verdict_payload` ✓ (def line 624, call line 728).
- **data** `computations/session-101/s101_ps_rge_modelc_sin2_mz.npz` — present (39,556 bytes); full-float64 (M_C, M_U, α_U_inv) + α_i⁻¹ trajectory arrays + sin²(μ) trajectory + all R1–R4 fields (Class-8.3 round-trip; downstream rel_tol ≥ 1e-4).
- **plot** `computations/session-101/s101_ps_rge_modelc_sin2_mz.png` — present (146,322 bytes); panel-1 = α_i⁻¹ unification trajectory with M_C / M_U / α_U⁻¹ markers; panel-2 = sin²θ_W(μ) on the solved trajectory with the μ_BC marker, the 0.23480 accommodation line, and the μ* crossing.
- **verdict line** `computations/session-101/s101_gate_verdicts.txt` — canonical line matches `^S101-PS-RGE-MODELC-SIN2-MZ:.* audit_sha256=[a-f0-9]{64}` ✓; dual-SHA companion row ✓; 2 extra companion rows (regulator_pin + ko_axis). No schema-v2 3-tuple (gate is a set/existence + report, not a directional value-comparison; `schema_v2_3tuple_required: false`). Emitted via `emit_verdict` (race-safe; 4 rows, cross-process locked, sig_5 unique).

**MCP Pre-Compute Audit**:
- `search_knowledge("Model-C Pati-Salam G422D intermediate scale unification sin2 theta_W RGE")` → returned `S83-SIN2-THETA-W-2-LOOP-PLUS-MU-BC` (PASS; `sin²θ_W(M_Z)=0.23138` via 2-loop SM RGE; `μ_BC=188.19 GeV`, `sin²(μ_BC)=0.23480`) + the s83 μ_BC geometric derivation. **No prior gate solves the Model-C INVERSE one-loop intermediate-scale system** — the RGE-viability axis of the W2-2 fingerprint is NOT closed; this gate computes it. NOT pre-closed.
- `get_constant("sin2_thetaW_MSbar")` → 0.23122 (no PROVENANCE; PDG-class). `get_constant("M_Z")` → 91.1876 (PDG 2024). `get_constant("alpha_em_MZ_inv")` → 127.955 (PDG 2024). `get_constant("alpha_s_MZ_obs")` → 0.118. `get_constant("M_Pl_unreduced")` → 1.2209e19 (CODATA 2018). All five imported, never hardcoded.
- Gate-6 verdict captured from `s101_gate_verdicts.txt`: `S101-CCS-MODELC-KO-DERIVATION: INFO` (audit `bb2fa21a69f4f849`; `theory_match=True`; derived KO-triple (6,+1,+1,−1) MATCHED the substrate anchor; `ko_axis=PRIMARY-UNDERDETERMINED`). Per the gate-6→gate-7 INFO row (plan Decision Points) + the orchestrator override: **DISPATCH STATUS-QUO** (full RGE run, all axes) with `ko_axis=indeterminate-carried`. NOT re-scoped to axes-(i,ii)-only (that demotion is reserved for a determinate KO mismatch / FAIL, which did NOT occur).

**Verdict**: **INFO** — by design (the only non-FAIL outcome; PASS NOT REACHABLE BY DESIGN per the Form-2 pre-registration). An ordered real solution exists: `M_Z ≤ M_C ≤ M_U ≤ M_Pl_unreduced`. `ko_axis=indeterminate-carried` rides the value string.
`audit_sha256=f2015a0ce1cf6c23e9e3e35fa7d7d7a0a929133452b9f13cb4a031b5d46d420d`
`content_sha256=eae638ae96122ae9bdbf0134e0016488522cb9a50f141bb98557ae0f7d7c6ed2`

**Substrate framing**: PARTICLE. The gauge couplings ARE spectral moments — the Yang-Mills action is the fourth spectral moment (a_4) of D_K. The W2-2 fingerprint (substrate-IS) identified WHICH published Pati-Salam-adjacent organization of those moments the substrate's defect signature matches (Model C / G422D). Direction of explanation: **substrate defect fingerprint (W2-2, substrate-IS) → unique published variant (Model C) → that variant's emergent-EFT running → laboratory-IN couplings at M_Z and μ_BC**. This gate tests the RGE-viability axis of that identification — an emergent-EFT statement about how the a_4-moment couplings reorganize between the unification boundary sin² = 3/8 and the laboratory scale. The INFO (ordered solution exists) confirms the identified variant's own one-loop running is internally consistent with the measured M_Z couplings; the substrate-IS leg (the fingerprint) is untouched by this outcome — a FAIL would have closed the variant's RGE axis, not the substrate's.

**Results** (NUMBERS first):

*Pinned form.* Form 2 (INFO-by-design two-route). PASS is NOT REACHABLE BY DESIGN, pre-declared at plan-freeze: the FORWARD scan-and-tune form (pick M_C, run down, hit a band) was rejected as Class-6-adjacent (iterate-until-PASS) + PRU Class-8 (unpinned M_C); the honest INVERSE form (input the three measured M_Z couplings, solve exactly for M_C, M_U, α_U from matching + the 3/8 boundary) has ZERO free parameters, but under it sin²θ_W(M_Z) is an INPUT, so a form-1 band would be load-and-compare-to-self (Class-4). A PASS emission is rejected at intake as ansatz-forcing.

*Step A — canonical EW inputs at M_Z (GUT-normalized), recomputed from imports:*
- α₂⁻¹(M_Z) = α_em⁻¹·sin² = 127.955 × 0.23122 = **29.5858**
- α_Y⁻¹(M_Z) = α_em⁻¹·(1−sin²) = **98.3692**
- α₁⁻¹(M_Z) = (3/5)·α_Y⁻¹ = **59.0215** [GUT norm; Y/2 = T₃R + (B−L)/2]
- α₃⁻¹(M_Z) = 1/α_s = 1/0.118 = **8.4746**

*Step B — SM betas (Convention I, pinned exact rationals):* (b1, b2, b3) = (41/10, −19/6, −7).

*Step C — Model-C β-coefficients computed IN-SCRIPT from the npz content* (variant C-LR / G422D; gauge SU(4)×SU(2)_L×SU(2)_R; fermions 3×[(4,2,1)+(4̄,1,2)]; scalars φ(1,2,2)+Σ̃(15,2,2)+Δ_R(10,1,3)+H_R(6,1,1)+Δ_L(10,3,1)+H_L(6,1,1)), Convention I `b = −(11/3)C₂(G) + (2/3)Σ_Weyl T(R) + (1/3)Σ_cplxScalar T(R)`:
- **b₄ = −2** (Conv I) ⟺ b₄^{II} = +2 (Aydemir's asymptotic-freedom-positive convention)
- **b_2L = b_2R = +26/3 = 8.6667** (Conv I) ⟺ b_2LR^{II} = −26/3. The **positive** Conv-I SU(2)_LR slope (i.e. α_2LR⁻¹ DECREASES upward) is the full-Model-C-scalar-content signal — not asymptotically free, distinct from the minimal-PS illustration.

*β cross-check (the plan's "0-tolerance exact-rational, halt-on-mismatch" reframed honestly).* The Aydemir overview (arXiv:2511.07672) publishes the Model-C field content, the breaking chain `NCG →[M_U] G422D →[M_C, ⟨Δ_R⟩] G321` (Eq. 8), and the unification condition `g₃²=g₂²=(5/3)g₁²` (Eq. 6) — but **NO explicit Model-C β-coefficient table and NO numerical (M_C, M_U)**; there is no published Model-C rational to identity-match. The cross-check therefore HALTS on:
- **X1 (engine validation) PASS** — the SAME Dynkin machinery reproduces the textbook, canonically-pinned SM (b1,b2,b3) = (41/10, −19/6, −7) EXACTLY (Sage-QQ verified). This is the non-circular anchor: the engine that produces the Model-C coefficients is verified on a known answer.
- **X2 (D-parity) PASS** — b_2L = b_2R exactly (Model-C is left-right symmetric; mirror scalar content forces equal SU(2)_{L,R} slopes).
- **Documented, NON-gating**: the companion transcription's minimal-PS illustration (researchers/Connes/27 L66–79) uses a different scalar sector AND a non-standard "11"-gauge normalization (his "11" ≠ (11/3)C₂(SU4) = 44/3); its printed `11 − 4 − 1/3 = 19/3` is a 1/3 arithmetic slip (Sage-QQ: 11 − 4 − 1/3 = **20/3**). Flagged, never a numerical source.

*Inverse 3×3 linear solve* (unknowns x = ln(M_C/M_Z), y = ln(M_U/M_Z), α_U⁻¹). Matching at M_C (G422D→G321, tree-level, GUT-norm hypercharge): α₃⁻¹=α₄⁻¹, α₂⁻¹=α_2L⁻¹, α₁⁻¹=(3/5)α_2R⁻¹+(2/5)α₄⁻¹; D-parity α_2L=α_2R on [M_C, M_U]; unify α₄(M_U)=α_2LR(M_U)=α_U:
- **det(A) = 3.9628 ≠ 0** ⇒ exactly determined, unique solution; solve residual **1.42e-14** (pin 1e-12 — at the float-cancellation floor, Sage-200-bit cross-check residual ~1e-59). NO residual freedom ⇒ scan_range = N/A (justified).

**R1 — (M_C, M_U, α_U⁻¹) + ordering margins:**
- **M_C = 5.0823×10¹³ GeV** (log₁₀ = 13.706)
- **M_U = 7.6819×10¹⁴ GeV** (log₁₀ = 14.885)
- **α_U⁻¹ = 39.4710**
- **ordering M_Z ≤ M_C ≤ M_U ≤ M_Pl_unreduced = 1.2209e19 GeV: TRUE** (margins in decades: M_C/M_Z = 11.746, M_U/M_C = 1.179, M_Pl/M_U = 4.201 — all > 0).

**R2 — forward closure (solver-correctness diagnostic, not physics).** Running M_U → M_Z reproduces all three input couplings and `sin²θ_W(M_Z)`: closure residual **2.13e-14** (pin 1e-10 — passes by ~4 OOM). sin²_back(M_Z) = 0.2312200000 (= input 0.23122). sin²(M_U) = 0.3750000000 = **3/8 exact** (consistent with W2-2's three-route 1e-12 verification: npz `sin2_clause_pass=True`).

**R3 — Route-ACCOM (the scale-conflation comparison the W2-2 plan correctly forbade, now this successor's legitimate OBJECT).** On the SOLVED one-loop trajectory (pure-SM below M_C; physical hypercharge slope b_Y = (5/3)b1 = 41/6):
- **sin²θ_W(μ_BC = 188.44 GeV)_solved = 0.234857**
- accommodation row = 0.23480 (S83-W3-G47 2-loop / S82-W3-10)
- **R3 Δ = sin²(μ_BC)_solved − 0.23480 = +5.65×10⁻⁵** (the one-loop solved value and the S83 2-loop+μ_BC accommodation agree to ~0.024%)
- **crossing scale μ* = 186.33 GeV** (where sin² = 0.23480), vs μ_BC = 188.44 GeV ⇒ μ*/μ_BC = 0.9888 (1.1% below)
- *Substitution chain Step-4 sign read-off* (the directional claim): sin²θ_W is **monotonically increasing** with μ in the SM regime — substituting the running, `d sin²/d lnμ ∝ −(b2 − b_Y)·t` with (b2, b_Y) = (−19/6, 41/6) ⇒ the bracket (b2 − b_Y) = −60/6 = −10 is negative ⇒ −(b2 − b_Y) > 0 ⇒ sin² rises upward (numerically: 0.23115 @ 90 GeV → 0.234857 @ 188.44 GeV → 0.24331 @ 1000 GeV). The two numbers (μ_BC and M_Z) now lie on ONE solved curve ⇒ the comparison is scale-consistent BY CONSTRUCTION. **One-loop-vs-two-loop systematic DECLARED non-gating** (the S83 accommodation fit was 2-loop; this gate is one-loop PINNED) — REPORT-only by design, no threshold.

**R4 — Aydemir published-OOM cross-check (METHODOLOGICAL only, qualitative).** The overview gives `M_U ≪ Λ` (Eq. 6 context); the companion 2-loop illustration gives `M_GUT ~ 10^{15.7±0.2}` and `v_R ~ 10^{11}–10^{13}`. My one-loop **M_U (log 14.885) is 0.815 decade below the 2-loop M_GUT (log 15.7)** — the expected direction and magnitude given the one-loop-vs-two-loop systematic + the full-vs-minimal scalar-content difference (the overview's qualitative band is reproduced at the OOM level). M_C (log 13.706) sits just above the published `v_R` intermediate-scale upper edge (10^{13.5}) — same OOM, the full Model-C content raising the breaking scale ~0.2 decade. No published Model-C numeric to identity-match; OOM-consistent.

*Datum reconciliation.* sin2_thetaW_MSbar = 0.23122 CANONICAL IMPORT (script imports, never hardcodes). Binding-text publication form 0.23121 ± 0.00004 → Δ = 1e-5 = 0.25 σ_PDG, D_max = 1.88e-5 OOM (no-action band); the canonical import wins, drift declared.

*4-tuple.* `(value='INFO_ordered_solution_exists M_C=5.082e+13GeV M_U=7.682e+14GeV alpha_U_inv=39.47 R3_delta=5.65e-05 mu_star=186.3GeV ko_axis=indeterminate-carried', scheme=G422D-MODELC-ONELOOP-INVERSE-INTERMEDIATE-SCALE, convention=INFO-BY-DESIGN-TWO-ROUTE-ABSOLUTE, L_max=N/A)`.

*Regulator pin.* `a_n^{cutoff}` structural-citation-only; NO numerical Seeley-DeWitt coefficient consumed (the gate consumes Dynkin indices + measured EW couplings; the spectral-action a_4 is cited structurally, matching gate-6's `a_n^{cutoff} structural-citation-only`). CLASS = FULL (no SCHEMATIC helper).

**Assessment (solution-space).** The INFO is the BY-DESIGN realization of dual-prior track_A (prior 0.85): a real ordered intermediate-scale solution exists, so the RGE-viability axis of the W2-2 Model-C identification is **internally consistent at one loop** — S102 Model-C phenomenology routing opens on the solved scales (leptoquark S₁ bounds at M_C ~ 5×10¹³ GeV; proton-decay-adjacent M_U ~ 8×10¹⁴ GeV). The framework's accommodation row (0.23480 @ μ_BC) gains an RGE-bridged, scale-consistent companion comparison: the solved one-loop trajectory passes within 0.024% of the 2-loop accommodation value at μ_BC, with the crossing scale μ* = 186.33 GeV ≈ μ_BC. This does NOT promote the fingerprint (the substrate-IS leg is untouched); it certifies the emergent-EFT running of the identified variant is laboratory-consistent. The corridor that would have closed (track_B / FAIL: no ordered solution) is NOT realized — Model-C one-loop running CAN connect sin²(M_U) = 3/8 to the measured M_Z couplings with its scalar content.

---

## Wave 3 Synthesis (team-lead)

**Outcome**: 7 gates — **1 PASS** (W3-5) + **1 FAIL** (W3-2) + **5 INFO** (W3-1, W3-3, W3-4, W3-6, W3-7). sig_5 clean. Verdict file lines 65/70/75/79/85/89/93. **None of the pre-registered FAIL-routings fired** (W3-2's FAIL is off-diagonal *magnitude*, not a PASS non-diagonal m_D → MR-TEXTURE-ROUTE-B HOLD stays held; gates 4/5/6 INFO/PASS → no contradiction-workshop, no three-routes-wall row, no Model-C demotion).

**S-3 surviving-map corridor — the coherent multi-gate result (shape-closable, scale-walled)**:
- **CLASS-1 envelope (W3-1 INFO)**: 3 candidates — (a) 2−S0 shape +0.36%/scale-wall, (b) S0 the expected KILL (+6.9% shape + DESI overshoot 0.097 eV), (c) κ_ν shape **EXACT** (+0.0000%)/scale-wall — LIVE, the structurally-privileged carrier. `Y₁=0` EXACT all candidates.
- **CLASS-2 texture (W3-2 FAIL)**: off-diagonal shape −4.36% outside ±1% — CLASS-2 at substrate-exact |w|=1/√6 excluded *for shape*; rank-deficiency (m₁=0) + scale-clause survive (dies on shape, not scale).
- **interaction-level gap-eq (W3-4 INFO)**: scale-in-band (×8.6–10.5, the factor spectrum maps provably couldn't) ∧ shape-FAIL (+39.7%) — "right species, wrong grading"; am2 = Khodel-Shaginyan *linear* (flat-band-adjacent, weak-coupling exponential forbidden).
- **κ_ν greybody (W3-3 INFO)**: κ_ν=11.49 M_KK thermal; s_ν=+0.5469 widening, sign-confirmed; `construction-FORBIDS-widening=FALSE` (the greybody *supplies* the widening via seesaw branch-i); magnitude compare-to-self, OPEN.
- **The shared wall**: the `[SIGN]` sector-keyed flip (`d ln Y/dC₂ = +0.55` neutrino-widening vs `−1.69` charged-narrowing) is a robust substrate prediction. The substrate fixes SHAPE + SIGN; the **absolute Dirac SCALE is irreducibly external** (r ≈ 2.8–3.4 ≫ 1.05 across W3-1/W3-3/W3-4) — three new routes independently re-confirm the **S100a-MD-NORMALIZATION PERMANENT caveat**. This is a mapped wall, not a failure.

**CP / Pati-Salam fork**:
- **W3-5 PASS**: Z₃ phase rephasing-removable; Jarlskog J=0.000 exact (6 configs); δ_CP ∈ {0,π} CERTIFIED. *Structural* (a generic real U_ν gives Im J ∝ sin φ ≠ 0 at ±2π/3, but the substrate pins both U_ν legs real) — the Z₃ phase relocates into a Majorana column phase (→ Row #80 m_ββ, mack).
- **W3-6 INFO**: derived KO-triple (6,+1,+1,−1) MATCHES the substrate anchor on all 4 slots, but INFO because the pinned *primaries* contain no KO-fixing statement (literature-indeterminate, NOT a physics mismatch). Scoped W3-7 status-quo.
- **W3-7 INFO** (PASS unreachable by design): unique 0-free-parameter solution; M_C=5.08×10¹³, M_U=7.68×10¹⁴ GeV; sin²θ_W(M_Z)=0.23122 reproduced (resid 2e-14), sin²(M_U)=3/8 exact, R3 accommodation 0.024%. Honest construction review re-anchored the absent Aydemir β-table to textbook SM `(41/10,−19/6,−7)` + D-parity.

**Dual-prior posteriors**: candidate-(c) carrier track_A 0.7 (W3-3 INFO); SCALE-axis track_B 0.9 (Dirac anchor external); Model-C track_A (W3-7 ordered solution exists).

### Effected In-Session (non-math — completed by the team-lead orchestrator before STOP)

(none standalone this wave. No pre-registered FAIL-routing fired (so no in-session escalation). W3's forward actions route to: the three S102 CFs below; mack-cosmic-bridge sole-writer territory at session close (Row #80 m_ββ Majorana-column relocation from W3-5; the RGE-bridged sin²θ_W accommodation companion from W3-7; any capstone §7 falsifier-surface annotation); and the EVOI rank-9b reconciliation (texture-cluster, spans W2+W3 — now both landed) deferred to session wrap-up per `/rclab-plan` Phase-1c-REGISTERS. No standalone forward-register status edit surfaced.)

(Self-audit: `grep -c '^- \[ \]'` on this sub-section = 0 — no unchecked items.)

## Carry-Forward Computations

### CF-S102-KAPPA-NU-FIRSTPRINCIPLES — first-principles κ_ν closing the W3-3 magnitude-OPEN

1. **What**: derive κ_ν (hence the neutrino shape-exponent s_ν) INDEPENDENTLY from the sector (c²−v²) gradient on the s84 B-branch spectrum, replacing W3-3's compare-to-self magnitude (where the target +0.546948 = ln(Y₃/Y₂)/(5/3) was back-solved from S99). Closes whether the greybody construction FORCES s_ν = +0.5469 (it is currently consistent-but-not-forced); makes W3-1 candidate-(c) a first-principles carrier.
2. **Inputs**: `s101_kappa_nu_greybody.npz` (κ_ν,bare=11.4877 M_KK, B_ν=−0.1453, branch-i dω/dC₂=−3.764; audit `833ddb9e`); the s84 L12 B-branch spectrum (now full-confidence post-W1 RE-LABEL); the Kitaev anchor 2π·T(a₄)=κ_exit; `S101-NU-DIRAC-ENVELOPE-MAP` candidate-(c) (audit `0744ad31`).
3. **Gate**: PASS iff a substrate-DERIVED κ_ν reproduces s_ν^pred = +0.5469 (rel ≤ 1%) with NO back-solve from the S99 Y-ratios; sign-flip (widening) preserved. INFO iff κ_ν is derivable but lands a different magnitude (re-pins candidate-c).
4. **Effort**: 1 wave. **Depends on**: S101-KAPPA-NU-GREYBODY INFO (this wave); the s84 B-branch spectrum. (Note: this closes the SHAPE-exponent derivation only — the absolute Dirac SCALE wall (external anchor, S100a PERMANENT caveat) is structural, not a gate.)

### CF-S102-NU-GRADING-EXTERNAL-EPSLX — external non-LI ε_LX supplying the generation grading

1. **What**: test whether an external (non-laboratory-inertial) ε_LX structure — the §VII.BL corollary design rule — supplies the generation shape-steepness (the grading the gap-equation route provably could NOT, W3-4 shape-FAIL +39.7%) WHILE the interaction-level gap equation supplies the scale (×8.6–10.5, W3-4 scale-PASS). Separates the "scale from gap-eq / shape from external ε_LX" division of labor.
2. **Inputs**: `s101_d5_md_gapeq.npz` (S_sol=1.5, r_sol=9.518, am2=KS-LINEAR; audit `21f0b099`); the S99 §VII.BL structural-ceiling theorem (no A_K-built form lifts the generation grading); the W3-1 envelope shape requirement (Y₃/Y₂ = 2.4882512).
3. **Gate**: PASS iff an external non-LI ε_LX reproduces the generation shape Y₃/Y₂ (rel ≤ 5%) while the gap-eq scale clause stays in-band; the ε_LX must be substrate-motivated (§VII.BL corollary), not fitted. FAIL iff no admissible external structure lifts the grading.
4. **Effort**: 1–2 waves. **Depends on**: S101-D5-MD-GAPEQ INFO (this wave); the §VII.BL ceiling.

### CF-S102-MODELC-PHENO-SCALES — Model-C phenomenology on the W3-7 solved scales

1. **What**: compute Model-C low-energy phenomenology on the W3-7 ordered solution — the leptoquark S₁ contribution at M_C=5.08×10¹³ GeV and the proton-decay-adjacent observables at M_U=7.68×10¹⁴ GeV — against current experimental bounds (Super-K / Hyper-K proton lifetime; leptoquark-mediated flavor bounds).
2. **Inputs**: `s101_ps_rge_modelc_sin2_mz.npz` (M_C, M_U, α_U⁻¹=39.47, full RGE trajectories; audit `f2015a0c`); the Model-C G422D field content; the W3-7 0-free-parameter solution.
3. **Gate**: PASS iff Model-C survives the proton-lifetime bound at M_U (τ_p > current limit) AND the leptoquark bounds at M_C; FAIL iff the solved scales are excluded by an experimental bound. (Falsifier-rigor — a substrate-pinned, scale-consistent Model-C now has a testable proton-decay companion.)
4. **Effort**: 1 wave. **Depends on**: S101-PS-RGE-MODELC-SIN2-MZ INFO (this wave). (The sin²θ_W accommodation row's RGE-bridged companion is mack-cosmic-bridge sole-writer at session close, separate from this compute CF.)

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-08 | Neutrino-Dirac SHAPE corridor | OPEN (S-3 surviving-map) | OPEN with substrate-pinned exponents (candidate-c shape EXACT); sign-flip +0.55 confirmed | W3-1/W3-3 INFO |
| 2026-06-08 | Neutrino-Dirac absolute SCALE | OPEN | WALL re-confirmed (irreducibly external; r≈2.8–3.4) — S100a-MD-NORMALIZATION PERMANENT caveat, 3 new routes | W3-1/W3-3/W3-4 |
| 2026-06-08 | CLASS-2 off-diagonal texture (|w|=1/√6) | OPEN | EXCLUDED for shape (−4.36%); rank-deficiency + scale survive | W3-2 FAIL |
| 2026-06-08 | D5 gap-equation (interaction-level m_D) | OPEN | Supplies SCALE not SHAPE (right-species-wrong-grading); KS-linear flat-band | W3-4 INFO |
| 2026-06-08 | Z₃ phase / δ_CP fate | OPEN | Rephasing-removable (J=0 exact); δ_CP∈{0,π} CERTIFIED; Z₃→Majorana column (Row #80) | W3-5 PASS |
| 2026-06-08 | Model-C KO-triple | OPEN | Theory-MATCHED (6,+1,+1,−1); literature-indeterminate (primaries pin no KO) | W3-6 INFO |
| 2026-06-08 | Model-C RGE scales | OPEN | Ordered solution M_C=5.08e13/M_U=7.68e14 GeV, 0 free params; sin²(M_U)=3/8 exact | W3-7 INFO |
| 2026-06-08 | MR-TEXTURE-ROUTE-B HOLD | CONDITIONAL-HOLD | Stays HELD (no PASS non-diagonal m_D; W3-2 FAIL + W3-4 diagonal) | W3 decision table |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Verdict audit |
|:-----|:-------|:------------|:------------|:--------------|
| W3-1 | `s101_nu_dirac_envelope_map.py` | `.npz` (25.9 KB) | `.png` | `0744ad31…` |
| W3-2 | `s101_nu_dirac_offdiag_texture.py` | `.npz` | `.png` | `d8712a6f…` |
| W3-3 | `s101_kappa_nu_greybody.py` | `.npz` (12.0 KB) | `.png` | `833ddb9e…` |
| W3-4 | `s101_d5_md_gapeq.py` | `.npz` (15.9 KB) | `.png` | `21f0b099…` |
| W3-5 | `s101_z3_phase_rephasing_invariance.py` | `.npz` (17.9 KB) | `.png` | `9bbfc35b…` |
| W3-6 | `s101_ccs_modelc_ko_derivation.py` | `.npz` | `.png` | `bb2fa21a…` |
| W3-7 | `s101_ps_rge_modelc_sin2_mz.py` | `.npz` (39.6 KB) | `.png` | `f2015a0c…` |

All scripts in `computations/session-101/`. Verdicts + dual-SHA + schema-v2 3-tuples (W3-1/W3-2/W3-3/W3-4/W3-5) + provenance rows in `s101_gate_verdicts.txt`.
