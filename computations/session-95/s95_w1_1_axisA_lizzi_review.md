# S95 W1-1 — Axis-A (spectral/NCG) Independent Cross-Review of §VII.BG

**Gate**: CF-S95-HK-1 (§W1-1) — joint-theorem Stage-2 cross-axis verify of §VII.BG → STAGE-3-PERMANENT.
**Reviewer**: lizzi-spectral-functional-theorist (Axis-A spectral/NCG), independent cross-reviewer.
**Independence**: derived from the registered §VII.BG entry + the Axis-A orthogonal anchor npz ONLY. Did NOT read the S94 W1-3 workshop transcript, the S94 WP §-section narrative, or the S95 W1 plan file. No-shared-context requirement honored (`joint-theorem-promotion.md §"Two-Agent Independent-Verify"`).
**This is a REVIEW, not the gate verdict.** No line emitted to `s95_gate_verdicts.txt`; no working-paper edit. The mechanical aggregator consumes this downstream.

## Audit pins (SHA-256)

- Registry entry block read: `sessions/permanent-results-registry.md` lines 20713–20789 (77 lines).
  SHA-256 = `18d365904f251b7f6da50650a3eecfb80a56a0deb795bd616d4093396ebafc8e`
- Axis-A orthogonal anchor npz loaded: `computations/session-94/s94_w1_3_vii_bx_t5_alpha_s_a4_recovery.npz` (20264 bytes).
  SHA-256 = `e922b3b47fb49b9886800c86a7c7fab805d627c546af9d32b146eb508ec13ef6`
  (npz-internal audit_sha256 = `d40965ec70e8c203d09c324b19e03c36d2427d6e298dc69abbf740a25cdea778`, matches the registered canonical line.)
- Substrate-input-orthogonality: loaded ONLY the Yang-Mills a_4-channel residue/GV anchor (spectral side). Did NOT load any transport-side / BdG occupation data file (Axis-B volovik's disjoint anchor). Disjoint-input requirement satisfied → PASS-AND with Axis-B is structurally independent.

## NUMBERS (independent re-derivation from raw npz arrays — not from precomputed boolean flags)

**Element 1 (substrate-IS observable).** a_4 home pole s=2, a_2 pole s=1, τ_fold=0.19 (npz: `s_a4=2`, `s_a2=1`, `tau_fold=0.19`). Per-L spectral moments `a4_sum_per_L = [1072.27, 4737.02, 21254.45]`, `a2_sum_per_L = [1474.02, 4727.28, 14226.61]` — all finite and positive on the finite triple `(A_K^{≤L}, H_K^{≤L}, D_K^{≤L})`. The pairing `⟨[φ], Ch(P_0(τ_fold))⟩` is a spectrum-only (algebra-INVARIANT, Corner II) closed-form functional → well-formed substrate-IS spectral functional.

**Element 3 (bridge map).** Direct Connes-Karoubi K_0-pairing `K_0(A_K) × K^0(A_K) → ℤ`, `[φ] ⊗ [P_0] ↦ ⟨[φ], Ch(P_0)⟩` (T5, index-fixed). Explicitly named as a K-theory pairing — NOT "analogous"/"corresponds to". Binding axis SUBSTRATE-NATURAL (χ-image BdG inheritance class; the surviving a_4/a_2 moment-ratio flow carries the L-dependence). Scheme-suffix carve-out admissible because Δ_scheme=0 (see clause c).

**Degree-match (composite bridge dimensional-class admissibility).** Re-derived from Wodzicki/residue homogeneity (Res_W at pole s carries degree −2s):
- deg(Res_W a_4) = −2·2 = −4 (npz `deg_ResW_a4=-4` ✓)
- deg(Res_W a_2) = −2·1 = −2 (npz `deg_ResW_a2=-2` ✓)
- deg(a_4/a_2) = −4 − (−2) = **−2** (npz `deg_a4_over_a2=-2` ✓); exact-integer in Sage QQ.
- |deg(a_4/a_2)| = 2 = |d_A| (d_A=+2). Match: **True**. The index-fixed K_0 degree is a discrete integer topological invariant and CAN equal d_A (discrete equality, no operator-mismatch).
- Non-scalar: f_χ = 1/4 (=4/16, L_max-INDEPENDENT rep-theory const) CANCELS in the ratio; ratio_spread over L∈{8,10,12} = 0.766544 ≠ 0 → surviving L-flow → NON-SCALAR. A canonical-import reference would be a degree-matched SCALAR (VACUOUS, T2). **non_scalar=True** re-derived.

**JOINT clause (c) — Δ_scheme → 0.** Substitution chain at canonical L_max=12:
- GV_APS(L12) = −1.2081580929e+08 [APS-1975 secondary class]
- GV_CS(L12)  = −1.2081580929e+08 [Cheeger-Simons, CM-1995 §III.4 residue z=0]
- GV_BC(L12)  = −1.2081580929e+08 [Bismut-Cheeger η-form, adiabatic t→0⁺]
- |GV_APS−GV_CS| = 0.000e+00; |GV_APS−GV_BC| = 0.000e+00; |GV_CS−GV_BC| = 0.000e+00
- Δ_scheme = max pairwise = **0.000e+00** ≤ 1e-12 → PASS.
- **Sage-QQ exact-rational cross-check**: promoting each float64 to exact QQ, pairwise differences are `[0, 0, 0]` at L∈{8,10,12}; Δ_scheme(L12) = `0` in Rational Field, `== 0 EXACTLY`. This is bit-exact zero, not float-approximate — all three secondary-class schemes reduce identically to the cubic-ρ Dixmier-trace sum `−4·Σ dim·ρ³·|λ|^{−4}`. `eta_defect_L12 = 0.0` (BDI parity-blindness; odd-grading [φ] carries the secondary content).

**Element 4 (algebraic envelope L^{−α}) + Level-2 sub-class.** GV-Heitsch successive ratios `[1, 9.094976, 8.033812]`. Aitken-Δ² extrapolant Φ_∞ independently recomputed in Sage QQ = `2416198018347007853746342/296218956300025353422657` = 8.156797419472918 (matches npz bit-for-bit). Residual sequence |Φ(L)−Φ_∞| = `[7.156797, 0.938178, 0.122985]` is **strictly monotone-decreasing** → genuine convergence toward Φ_∞ → the convergence object is a real binding envelope (HKR/Connes-Karoubi image to a continuum laboratory observable), NOT a non-binding bare-decomposition rate. Empirical α from the L=10→12 residual ratio = 11.14 > 0 (in family with reported α_env=9.9887; difference is Aitken-Δ² vs single-step-ratio definitional, both fast-positive). Level-2 = 0.132537, Level-3 = 0.122985; **Level-3 < Level-2** with margin (L2−L3)/L2 = 0.072073 > 1e-3 → registry-PASS criterion satisfied. Level-2 sub-class = **Level-2-binding** (confirmed).

## CLAUSE VERDICTS (spectral side)

- CLAUSE Element-1 (Substrate-IS observable): PASS — a_4 K_0-pairing at s=2 on (A_K,H_K,D_K) at τ_fold=0.19 is a finite, positive, spectrum-only (Corner II algebra-INVARIANT) functional; per-L moments finite/positive; well-formed substrate-IS spectral functional re-derived from raw arrays.
- CLAUSE Element-3 (Bridge map): PASS — explicit direct Connes-Karoubi K_0-pairing `K_0×K^0→ℤ`, `[φ]⊗[P_0]↦⟨[φ],Ch(P_0)⟩`, index-fixed; named K-theory pairing (not "analogous"); SUBSTRATE-NATURAL-BINDING via χ-image class; bare Element-3 admissible under the Δ_scheme=0 scheme-INDEPENDENCE carve-out.
- CLAUSE Element-4 (Algebraic envelope L^{−α}, sub-class): PASS — residual sequence |Φ(L)−Φ_∞| strictly monotone-decreasing toward Sage-exact Φ_∞=8.156797; α>0 (empirical 11.14, npz α_env=9.9887); Level-2-binding confirmed; Level-3 (0.122985) < Level-2 (0.132537), margin 7.21% > 1e-3. INFO-NOTE (non-blocking): envelope rests on 3 L-points (Aitken-Δ² extrapolant), so α_env is a 3-point object not a many-point regression; the registry-PASS criterion (binding + monotone + L3<L2 at canonical L_max) re-derives cleanly regardless, so the verdict is PASS.
- CLAUSE Degree-match (d_A=+2 vs deg(a_4/a_2)=−2, non-scalar): PASS — |deg(a_4/a_2)|=2 re-derived exactly from Wodzicki homogeneity (−2s_a4 − (−2s_a2) = −2), equals |d_A|=2; index-fixed K_0 degree admits discrete-integer equality with d_A; non-scalar confirmed (f_χ=1/4 cancels, ratio_spread=0.766544≠0 → surviving L-flow). SPECTRAL-SIDE NOTE: the *value* d_A=+2 originates from the W7-1 transport `deg(T_BZ→pivot)`, which is Axis-B's (transport/superfluid) anchor; from the spectral side I independently verify (a) deg(a_4/a_2)=−2 exactly, (b) the |·| match given d_A=+2, and (c) non-scalarity — these are the spectral-content clauses. Axis-B confirms the d_A=+2 transport value on its disjoint anchor (this is by design the PASS-AND structure).
- CLAUSE JOINT (c) Δ_scheme→0: PASS — Δ_scheme = max{|GV_APS−GV_CS|,|GV_APS−GV_BC|,|GV_CS−GV_BC|} = 0.000e+00 at L_max=12 (and bit-identical at L=8,10); Sage-QQ exact-rational difference = 0 EXACTLY in Rational Field; |Δ_scheme| ≤ 1e-12 satisfied with strict bit-exact zero. All three schemes (APS-1975 / Cheeger-Simons / Bismut-Cheeger) collapse to the same cubic-ρ Dixmier-trace closed form.

AXIS-A COMPOSITE: PASS

## Interpretation (third, after numbers + clause verdicts)

All five spectral-side clauses re-derive cleanly from the registered entry + the Axis-A orthogonal anchor alone, with no inference-from-assertion: Δ_scheme is bit-exact zero (Sage-QQ confirmed, not float-marginal), the degree-match is exact-integer from Wodzicki homogeneity, and the L^{−α} envelope is a genuine *binding* convergence object (monotone residual decay to a Sage-exact Aitken limit), so the Level-2-binding sub-class and the Level-3<Level-2 registry-PASS criterion both hold structurally rather than numerically-fragile. The only honest caveat is the 3-point envelope (an Aitken-Δ² extrapolant), recorded as a non-blocking INFO-NOTE on Element-4; it does not change any verdict because the registry-PASS predicate is about binding+monotone+ordering at canonical L_max, all of which hold. The d_A=+2 *value* is Axis-B's transport anchor; the spectral side independently verifies the degree-match given d_A and the non-scalarity, which is exactly the clause partition the PASS-AND is designed for. JOINT clause (c) PASS-AND-eligible from this side. Functional-independence note: Δ_scheme=0 means the bridge-map *value* is invariant across the three secondary-class schemes — a FUNCTIONAL-INDEPENDENT (structural) result on the secondary-class axis, distinct from (and orthogonal to) the UV-regulator RD axis. Recommend STAGE-3-PERMANENT promotion on the spectral side, contingent on Axis-B's parallel PASS-AND on clause (c) and the d_A=+2 transport value.
