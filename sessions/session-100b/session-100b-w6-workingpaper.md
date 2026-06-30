# Session 100b Wave 6 — Flat-Band Quantum Geometry / §VII.AF.1 Bridge Hardening (Results Working Paper)

**Session**: 100b | **Wave**: 6 | **Plan**: session-100b-plan-w6.md | **Theme**: S99 flat-band quantum-geometry carry-forwards — BdG-projector confirmation + non-Abelian metric-trace hardening of the §VII.AF.1.OP-PROJ bridge, plus MgB₂ Leggett-damping χ-inheritance transport audit (survival outputs in canonical ratio/inequality form).

## Gate Sections

### §W6-1. S100b-VII-AF1-BDG-PROJECTOR-CONFIRM (landau-condensed-matter-theorist)

**Status**: COMPLETED
**Gate ID**: `S100b-VII-AF1-BDG-PROJECTOR-CONFIRM`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (Element-5 structural confirmation of the existing §VII.AF.1.OP-PROJ entry at the PRIMARY ζ-pairing layer; not a new registration)
**Agent**: `landau-condensed-matter-theorist`
**Hypothesis**: Direct Connes–Karoubi pairing on the BdG/quasihole projector P_0(τ_fold) reproduces the PRIMARY canonical eps_H_HP1_norm = 16.197719 within the Level-2 envelope (δ_BdG ≤ 1e-3) while the rank-matched τ=0 normal-state swap does not (Δ_disc > 1e-3) — the §VII.AF.1.OP-PROJ projector choice is load-bearing (Porlles–Chen).
**Plan reference**: `sessions/session-plan/session-100b-plan-w6.md` §W6-1 (slot law, anchor-conflation + Reading-A/B guards, Mode-A/Mode-B normalization pre-declaration, machinery pins, substitution chain).

**MCP Pre-Compute Audit**:

| # | Query | Salient return |
|:--|:------|:---------------|
| 1 | `search_knowledge("BdG projector quantum metric bridge VII.AF.1 Connes-Karoubi pairing")` | 10 hits. Closest prior compute: `S89-CONNES-KAROUBI-PAIRING-BDG-RESTRICTED-INFRASTRUCTURE` (FAIL, `R_canonical = 7.32497`) — that is the **χ-restricted M₂(ℂ) child pairing** (3He-B inheritance observable), structurally DISTINCT from this gate's full-A_K band-0 projector discrimination against `eps_H_HP1_norm`. NOT PRE-CLOSED. |
| 2 | `get_constant("eps_H_HP1_norm")` | 16.197719 (matches `canonical_constants.py:172`, "S84 W10a-114; 6 sig figs"; MCP row carries no PROVENANCE entry — provenance lives in the canonical_constants CF-28 comment block, lines 150–172/255–270). |
| 3 | `get_constant("tau_fold")` | 0.19; S12/S42; CONST-FREEZE-42; not superseded. |
| 4 | `trace_entity("eps_H_HP1_norm projector-side pairing")` | No trace — the s86-hp1 V4-queued projector-side numerical evaluation has never been run. |
| 5 | `trace_entity("VII.AF.1 quantum metric bridge")` | No trace under that label (the registered entry is covered by query 1's theorem hit: §VII.AF.1 LANDED block carries HKR + Connes-Karoubi naming, S87 W5). |

Conclusion: gate NOT pre-closed. Pin scoping: of the wave-level pin set, §W6-1 imports `eps_H_HP1_norm` and `tau_fold` only (the Δ_BCS/ω_L1/DM pins belong to §W6-3).

**Verdict**: **PASS** — `delta_BdG = 0` (Mode-B, VACUOUS by construction) ≤ 1e-3 AND `Delta_disc = 0.341975501613` > 1e-3 (342× the discrimination floor). Schema-v2 3-tuple: `sign_verdict=PASS` (R^N < R^BdG, pre-registered content-loss direction), `magnitude_verdict=PASS`, `regime_verdict=VALID`. Emitted via race-safe `emit_verdict`: `audit_sha256=06206dbbd1f6ec3858e8fc1469d87d24e52164e72bd1f70ad05cbbd02b172783`, `content_sha256=03029fc80a0b02dc7f8fb001f06d95945a9dc61f4168f798d98722d38da4cd39`.

**UNTRUSTED-UPSTREAM caveat (MANDATORY, carried per orchestrator dispatch)**: this gate consumes the s84 spectrum-cache lineage flagged by the S100b-TAU0-LAITEH-REDUCTION ESCALATION (FAIL, SUBCASE=STRUCTURED): the framework τ=0 operator sits at the Levi-Civita torsion point t = 1/2 of the Lai-Teh family, NOT the Kostant cubic t = 1/3; the eigensolver itself is verified CORRECT by a cubic-modified control at machine epsilon; the λ² = n/36 PROVEN record remains VALID (this gate independently re-confirms it: 36λ² = 27.000000000 at τ=0); the cache numerics are self-consistent with the LC lineage the framework has always computed. The open question is operator CANONICITY (Q1-workshop carry-forward, WP §W3-2), NOT numerical validity. **All results in this section are conditional on the LC-operator lineage being canonical**: both arms (τ_fold and τ=0) and the CC1 cache anchor are built from the same LC t = 1/2 connection, so a future canonicity re-adjudication would shift both arms coherently — the gate's discrimination CONCLUSION (projector choice load-bearing at 342× the envelope) is robust in structure but its numerical values inherit the LC lineage. Dispatched per the plan's pre-registered orchestrator-triage option "dispatch under explicit UNTRUSTED-UPSTREAM caveat"; the caveat is mirrored as a verdict-file extra row.

**Results** (NUMBERS first; full float64 in npz, 6 sig figs here per the publication-precision pin):

| Quantity | Value | Threshold / anchor |
|:---------|:------|:-------------------|
| Normalization mode | **Mode-B** (normalization-anchored; pre-declared fallback) | Mode-A sufficiency set {cocycle_representative, generator_basis, N_pair} ABSENT from s84 npz (keys recorded: ch_matrix, eps_H_cocycle, image_basis, residual_value, hp1_representative, cm_hopf_lift, relative_match, heitsch_ratio_used, leg/verdict/sha scalars) |
| φ_g^sym signed pairing, BdG arm | −0.0417715 (metric trace 0.0417715) | τ_fold = 0.19, (0,0) block 16×16 |
| φ_g^sym signed pairing, N arm | −0.0274866 (metric trace 0.0274866) | τ = 0, rank-matched, stable-tie-break pin |
| N_pair (Mode-B anchor) | −387.770 | := heitsch_full / φ_signed(BdG) |
| R^BdG | 16.1977188529899 (≡ anchor, exact by construction) | CC2 target 16.197718852989908 |
| R^N | 10.6585 | — |
| δ_BdG | 0.0 — **VACUOUS** (Mode-B, pre-declared) | ≤ 1e-3 ✓ (clause carried by construction; only Δ_disc evidential) |
| **Δ_disc** | **0.341976** | > 1e-3 ✓ (342× floor; = \|1 − met_N/met_BdG\|, N_pair cancels) |
| R^N/R^BdG | 0.658024 | direction R^N < R^BdG matches pre-registered content loss |
| r0 (BdG multiplet rank, deg_tol 1e-9) | 2 (the B1 particle-hole pair; \|λ\|_min = 0.819741112, gap to B2 = 0.025471) | expected 2 ✓ |
| τ=0 lowest-\|λ\| degeneracy | 16 (uniform \|λ\| = 0.866025404 = √3/2; 36λ² = 27.000000000 — PROVEN λ²=n/36, n=27) | tie-break pin load-bearing; d2 orbit diagnostic below |
| CC1 cache cross-check | builder \|λ\|_min = 0.819741112067 == cache 0.819741112067; full-16-multiset max rel dev = 1.219e-15 | guard 1e-9 ✓ (no builder drift) |
| CC2 target | s84 npz heitsch_ratio_used = 16.197718852989908 == pinned target; canonical 6-sig-fig form drift 9.08e-9 | Class-8.3 compliant |
| Eigh residuals | 7.3e-16 (BdG), 6.3e-16 (N) | tol 1e-12 ✓ |
| Structural identity Tr(P[P,J][P,J]) = −Tr(PJ(1−P)JP) | max dev 3.5e-18 (BdG), 8.7e-19 (N) | asserted at machine precision ✓ |

4-tuple: `(value=0.341976, scheme=CONNES-KAROUBI-PAIRING-W10A114-NORM, convention=RATIO, L_max=10)`. Verdict-file rows: canonical line + dual-SHA companion + schema-v2 3-tuple + 3 extra rows (UNTRUSTED-UPSTREAM caveat, regulator_pin a_4^{ζ} inherited verbatim, Mode-B/fallback/CLASS=FULL disclosure).

**Substitution chain (with substituted numbers; plan §W6-1 item 7 executed)**:

```
Step 1 (definitions, computed):
  phi_g^sym(P; a_0=P, legs J_a) = sum_a Re (1/16) Tr( P [P, J_a][P, J_a] ),
      J_a = i K_a, K_a = (1/8) sum_{r,s}(Gamma[s,r,a] - Gamma[r,s,a]) gamma_r gamma_s
      (Kosmann spin-lift of Gell-Mann lambda_a on the 16-dim singlet fiber; S23a lineage)
  phi_signed(BdG) = -0.041771468172      [P_0^BdG: r0=2 B1 pair at tau_fold = 0.19]
  phi_signed(N)   = -0.027486649391      [P_0^N: rank-2 stable-tie-break at tau = 0]
  heitsch_full    = 16.197718852989908   [s84 script, S83 W1-G2; CC2 pin]
Step 2 (substitute, no simplification):
  N_pair = 16.197718852989908 / (-0.041771468172) = -387.769919557
  R^BdG  = N_pair x phi_signed(BdG) = 16.197718852990   (anchor, exact)
  R^N    = N_pair x phi_signed(N)   = (-387.769919557) x (-0.027486649391)
         = 10.658495823259
Step 3 (simplify):
  delta_BdG  = |16.197718852990 - 16.197718852989908| / 16.197718852989908 = 0.0  (VACUOUS)
  Delta_disc = |16.197718852990 - 10.658495823259| / 16.197718852990
             = 5.539223029731 / 16.197718852990
             = 0.341975501613
  cross-check (N_pair cancellation): |1 - 0.027486649391/0.041771468172|
             = |1 - 0.658024498387| = 0.341975501613  ✓ identical
Step 4 (direction read-off):
  met_N (0.0274866) < met_BdG (0.0417715)  =>  R^N < R^BdG   [pre-registered: content loss]
  0.341975501613 > 1.0e-3                  =>  discrimination clause PASS
  delta_BdG = 0 <= 1.0e-3                  =>  reproduction clause PASS (vacuous, declared)
Conclusion: PASS — the BdG/quasihole projector choice is load-bearing; the
normal-state swap moves the pairing 342x outside the Level-2 envelope.
```

**Methodology subsection — OPERATIONAL DEVIATIONS and structural notes (honest disclosure)**:

1. **Generator-basis fallback fired (plan-pinned)**: the s84 W10a-114 npz carries no explicit cocycle-leg basis (Mode-A key inspection above), so the pinned fallback — Gell-Mann λ_1..λ_8 on the M_3(ℂ) summand of A_K — was used. On the (0,0) singlet spinor fiber the represented action of the generator direction a is the canonical Kosmann spin-lift K_a (S23a `kosmann_operator_antisymmetric`, Baptista Paper 17 eq 4.1; the same lineage as the S25 Ω=0 theorem and the S96 scaffold), implemented verbatim in the producing script. Each arm is evaluated self-consistently at its own metric point (P_0^X, Γ(τ_X), J_a(τ_X) all at τ_X) per the plan's "projector swap propagates to BOTH legs".
2. **Class-8.7-adjacent degeneracy note (pre-flight)**: the literal all-three-slots substitution φ_g^sym(P, P, P) vanishes IDENTICALLY for ANY projector ([P,P] = 0) — a structural zero with no discriminating power. The pairing is therefore evaluated in the idempotent-evaluation form with the K_0-class representative P_0^X in the a_0 (Chern) slot and the generator-basis differentials in the two cocycle legs — exactly the s86-hp1 eq. R-V1.3 form (φ_g^sym(a_0, a_k, a_l) = Re τ_S(a_0 g_kl a_k a_l): the quantum metric lifted to a Hochschild cochain), which is what the plan's `generator_basis` machinery pin exists to supply. The structural identity Tr(P[P,J][P,J]) = −Tr(PJ(1−P)JP) (asserted at ≤3.5e-18) confirms the evaluated object IS the Provost–Vallée metric trace Σ_a (1/16)‖(1−P)J_aP‖²_F — the substrate's Re⟨dP ∧ dP⟩ Riemannian component.
3. **Mode-B vacuity (pre-declared)**: δ_BdG = 0 by construction; the FAIL branch (Element-5 regression) is unreachable in Mode-B; PASS/INFO is carried by Δ_disc alone, per the plan's normalization_mode pin and INFO_meaning. The Mode-A absolute reproduction of the anchor from the projector side alone remains an open (un-run) computation — it would require the W10a-114 normalization constants that the npz does not carry.
4. **τ_S normalization**: normalized trace Tr/16 on the spinor fiber; the Vol(SU(3)) factor and all overall constants are absorbed by N_pair (Mode-B); Δ_disc is a ratio and is normalization-free.
5. **CLASS=FULL**: direct finite-spectral-triple pairing via the full `dirac_spectrum` builder; no SCHEMATIC helper imported. Regulator pin a_4^{ζ} inherited verbatim from the registered entry; no new Mellin-pole evaluation, hence no new poleconv-{A|B} tag obligation.

**Diagnostics (pre-declared in the producing script; NOT PASS inputs)**:

- **d1 (fixed-generator arm)**: metric_trace(P_0^N, J_a(τ_fold)) = 0.0288341 → Δ_disc(fixed-gen) = 0.309717. The discrimination is carried overwhelmingly by the **projector swap** itself; the generator τ-dependence contributes only ~0.03 of the 0.34.
- **d2 (τ=0 representative-orbit robustness)**: 8 random orthonormal rank-2 frames in the 16-dim |λ|-tied τ=0 subspace (seed 100616): metric_trace(N) ∈ [0.0269971, 0.0292027], implied Δ_disc ∈ [0.300894, 0.353695]. **Every** representative of the tie-break class discriminates at >300× the floor — the PASS does not hinge on the stable-eigh tie-break pin.
- **d3 (channel anatomy, u(2) vs C²)**: BdG arm: u(2) = 0.0021565, C² = 0.0396150 (94.8% of the metric content in the coset directions λ_4..λ_7); N arm: u(2) = 0.0147231, C² = 0.0127635 (roughly even). Per-generator BdG content: λ_1 = λ_2 = λ_3 = 7.18835e-4 (su(2) isotropy, bit-exact equal), λ_4..λ_7 = 9.90374e-3 (C² isotropy), **λ_8 = 4.93e-31 — machine-zero**. The λ_8 zero is the proven wall [iK_7, D_K] = 0 (U(1)_7 exactness) manifest in the metric trace: on the non-degenerate B1 band the λ_8 Kosmann generator commutes with D_K and hence with its spectral projector, so (1−P)J_8P = 0 exactly. A free, independent machine-precision confirmation of permanent wall #5.

**Substrate framing (GEOMETRIC; direction of explanation preserved)**: the substrate IS the spectral triple (A_K, H_K, D_K); the quantum metric on the Jensen-deformed band-0 projector IS the substrate observable. D_K eigenvalues → band-0 projector P_0(τ_fold) → Hochschild pairing (substrate-IS) → HKR bridge map → Peotta–Törmä superfluid-stiffness trace (laboratory-IN). Porlles–Chen's quasihole metric is the laboratory-IN shadow of the substrate's BdG-state projection — the lab paper confirms the substrate's structural choice, not the reverse. **Landau reading**: the Jensen deformation τ IS the substrate's order parameter ((SU(3)_L×SU(3)_R)/Z_3 breaks at τ > 0); P_0(τ_fold) is the condensed-phase projector, P_0(0) the symmetric-phase one. The gate's verdict confirms Element 5 of the registered anatomy is anchored to the **ordered state**, as a Landau free-energy reading requires — and the d3 channel anatomy shows it concretely: at the fold, 94.8% of the band-0 metric content lives in the symmetry-broken C² (coset) directions, the Cartan/hypercharge direction carries exactly zero (U(1)_7 survives), and the normal-state arm loses precisely the order-parameter-gated coset content (C²: 0.0396 → 0.0128, a 3.1× loss). The condensed-phase pairing anchor is structurally a property of the broken phase.

**Assessment**: PASS at 342× the pre-registered floor closes the latent projector ambiguity in the §VII.AF.1 → §VII.AF anchor chain at the PRIMARY pairing layer: the bridge targets the superconducting-state (quasihole) metric, structurally, with independent laboratory convergence (Porlles–Chen arXiv:2505.17349) now matched by a direct substrate-side computation — the numerical projector-side evaluation the s86-hp1 workshop's V4 question queued. Per the plan's pre-registered discriminator the outcome routes to Track A (projector choice load-bearing). The Element-5 confirmation annotation on the §VII.AF.1.OP-PROJ registry surface routes to `mack-cosmic-bridge` (sole writer per `feedback_mack-bridge-role.md`); this gate wrote only its script/npz/png/verdict/WP-section. The registered entry's Level-3 verdict is untouched (this gate cannot retro-modify it; anchor-conflation guard respected: the three derived scalars r = 19/200, STRICT_F4 = 1.030902, err = 0.0095% were not consumed — the gate operated at the PRIMARY `eps_H_HP1_norm` layer where the projector swap is visible, not at the F₄ atlas-ratio layer where it cancels).

**Output Artifacts**:

| Artifact | Path | Size |
|:---------|:-----|:-----|
| Script | `computations/session-100b/s100b_vii_af1_bdg_projector_confirm.py` | 38.7 KB |
| Data | `computations/session-100b/s100b_vii_af1_bdg_projector_confirm.npz` | 16.9 KB |
| Plot | `computations/session-100b/s100b_vii_af1_bdg_projector_confirm.png` | 111 KB |
| Verdict | `computations/session-100b/s100b_gate_verdicts.txt` (canonical line + companion + 3-tuple + 3 extra rows) | — |

---

### §W6-2. S100b-NONABELIAN-METRIC-FRACTION (berry-geometric-phase-theorist)

**Status**: COMPLETED
**Gate ID**: `S100b-NONABELIAN-METRIC-FRACTION`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (algebra-correctness confirmation of the §VII.AF.1.OP-PROJ metric-trace object on the degenerate D_K multiplet; metric-not-curvature re-check)
**Agent**: `berry-geometric-phase-theorist`
**Hypothesis**: On the (τ,μ) U(2)-invariant TT surface the degenerate lowest D_K multiplet carries within-multiplet Wilczek–Zee content — f_nonAb > 1e-10, i.e. Tr R ≠ Σ(per-band Abelian QM), the algebra-correct object for A_K = ℂ ⊕ ℍ ⊕ M₃(ℂ) — while the imaginary part integrates to Chern = 0 (|Im_int| < 1e-12).
**Plan reference**: `sessions/session-plan/session-100b-plan-w6.md` §W6-2 (S96 scaffold + surface pins, multiplet arms, gauge-orbit + negative-control diagnostics, substitution chain).

**MCP Pre-Compute Audit**:

- `search_knowledge("non-Abelian quantum metric Wilczek-Zee degenerate multiplet trace")` → only hits are this gate's own plan equations + the s86-hp1 workshop definitions (R_universal BZ-trace, τ_S trace). NO prior f_nonAb computation exists; NOT PRE-CLOSED.
- `get_constant("tau_fold")` → 0.19 (S12/S42, CONST-FREEZE-42, not superseded) — matches the plan pin.
- `trace_entity("OFFJENSEN-CHERN")` → S96-GEOM-OFFJENSEN-CHERN PASS-TRIVIAL (C_FHS=9.777563e-15, maxΩ=2.272e-23, C_cont=−5.368e-29, allsectorsTrivial=True) — the scaffold baseline consumed as CC-3.
- `get_constant("F_squeeze_bare")` → not a canonical-constants entry; `search_knowledge("F_squeeze flat band squeeze 54.06")` → equation hit `F_squeeze_bare = 5.4060e+01` (s74 output). Cited here as narrative context only per the Wave-6 "37×" law (37× is NOT a pin; no block in this section cites it).
- `trace_entity("Berry curvature off-Jensen Chern")` → no direct trace under that phrase (the OFFJENSEN-CHERN trace above covers it).

Pin scoping: of the wave-level pin set, §W6-2 imports `tau_fold` only (the eps_H/Δ_BCS/ω_L1/DM pins belong to §W6-1/§W6-3).

**Verdict**: **FAIL** — `[FAIL-a-JPH-protected-B2-carries-CKH]` per the pre-registered FAIL-arm discrimination. Schema-v2 3-tuple: `sign_verdict=PASS` (numerator ≥ 0 at the canonical float-cancellation floor), `magnitude_verdict=FAIL` (f_nonAb = 2.96e-15 ≤ 1e-10), `regime_verdict=VALID` (breach fraction 1.38% ≤ 5%). Composite per the gate-verdicts.md collapse rule: FAIL. Emitted via the race-safe `emit_verdict` MCP tool: `audit_sha256=4a03497c43a97335144bad80f60e16d00097829ca4310f25315dfe4c9c926818`, `content_sha256=03c7532340767a9932e6cbb487ddb65f7f56a596e466a6d7f1b1db505340192a`.

**UNTRUSTED-UPSTREAM caveat (mandatory)**: this gate consumes the s84 spectrum-cache lineage flagged by the S100b-TAU0-LAITEH-REDUCTION ESCALATION (FAIL, SUBCASE=STRUCTURED: the framework τ=0 operator sits at the Levi-Civita torsion point t=1/2 of the Lai–Teh family, NOT the Kostant cubic t=1/3; the eigensolver itself is verified CORRECT by a cubic-modified control at machine epsilon; the λ²=n/36 PROVEN record remains VALID; the cache numerics are self-consistent with the LC lineage the framework has always computed). The open question is operator CANONICITY (Q1-workshop carry-forward, WP §W3-2), NOT numerical validity. Dispatched per the plan's pre-registered orchestrator-triage option "dispatch under explicit UNTRUSTED-UPSTREAM caveat"; **every result in this section is conditional on the LC-operator lineage being canonical**. If the canonicity adjudication lands on a different torsion point, the (0,0)-block spectrum and eigenbundle would need recomputation under the adjudicated operator; the gauge-free projector machinery, the trace-identity LEMMA, and the Schur/isotropy arguments below are operator-independent and transfer as-is. The caveat is mirrored as a verdict-file extra row.

**Results — geometry first**

The fiber over the 2-parameter Ad-U(2)-invariant volume-preserving TT surface (S96 pins: l(τ,μ) = τ·v_J + (μ/|v_μ|)·v_μ, v_J = (2,−2,1), v_μ = n×v_J = (11,7,−8), |v_μ|² = 234; 51×51 nodes on [0.10,0.30]×[−0.10,0.10], Δ = 0.004; μ=0 IS the Jensen line, fold τ_fold = 0.19 enclosed) is the 16-dim (0,0) Peter-Weyl singlet block of D_K (S22b block-diagonality). Its signed spectrum at every node is PH/chiral-symmetric with the layout

```
[ −B3 ×3 | −B2 ×4 | −B1 | +B1 | +B2 ×4 | +B3 ×3 ]      (max|λ₇+λ₈| = 2.4e-15)
```

The PRIMARY lowest-|λ| multiplet detected at deg_tol = 1e-7 at the anchor (τ_fold, 0) has **deg = 2 as plan-expected** — and it is the **J/PH pair** {u₋, u₊} at (−|λ|min, +|λ|min) = two individually 1-dim eigenspaces paired by the chirality γ₉ (= normalized product of the Cl(8) gammas): max|{H,γ₉}| = 0.0e+00 exactly, and |⟨u₊|γ₉|u₋⟩| = 1.000000000 — the pair is **chirality-locked**. The B2 group detects at deg = 8 in |λ| — **deviation declared**: this is the J/PH double (4+4) of a 4-fold eigenspace; the plan-expected deg = 4 corresponds to the signed +λ quadruplet (signed cols 9..12), which is the B2 arm used.

**Gauge pin + evaluator (operational note, honest-disclosure per math-scripts.md plan-deviation discipline)**: the declared gauge pin is signed-eigh-ascending member order + largest-|component| real-positive phase. Probe measurement found π-jumps in the phase pin where the argmax component switches (max per-step phase defect = π), so the PASS quantities are evaluated through the **exact gauge-free projector identity** (proven in the script header):

```
Tr_band Q_ab = Tr[(d_a P_M)(1 − P_M)(d_b P_M)],   g⁽ⁿ⁾_ab = Tr[(d_a P_n)(1 − P_n)(d_b P_n)]  (rank-1)
```

mathematically IDENTICAL to the plan's Step-1 state-form definitions and needing no phase convention at all (P_M and the rank-1 P_n are basis-free; the pair members are canonically defined 1-dim signed eigenspaces). The plan-literal state-FD arm was computed in full and reported as CC-2. FD scheme = central differences on the pinned mesh, one-sided at boundary (declared).

**Numbers (operator clauses + companions)**

| Quantity | Value | Pre-registered criterion | Clause |
|:---------|:------|:------------------------|:-------|
| f_nonAb (primary pair) | **2.960595e-15** | > 1e-10 | **FAIL** |
| Im_int | **6.124613e-18** | < 1e-12 | PASS |
| I_NA = ∫ Σ_a Tr_band R_aa | 1.500000000e+00 (100.00% corner-defect; see e1) | — | — |
| I_Ab (rank-1 projector form) | 1.500000000e+00 | — | — |
| I_Ab − I_NA (WZ numerator) | −4.440892e-15 = 20·ε (float-cancellation floor; ≥ 0 at the canonical 1e-14 floor) | ≥ 0 (chain Step 4) | sign PASS |
| C_FHS (det-U(2) pair) | −0.500000 = single corner π-plaquette (2499/2500 plaquettes \|F\| < 1e-6) | \|C\| < 1e-3 companion | reported (defect-attributed) |
| Im_int (state-FD CC) | −2.18e-14 | — | consistent ~0 |
| breach fraction (gap12 < 0.005) | 1.38% | ≤ 5% → VALID | VALID |
| deg detected (anchor) | 2 (plan-expected 2) | recorded | ✓ |

**Substitution chain with substituted numbers** (plan §W6-2 item 7): Steps 2–3 give I_Ab − I_NA = ∫ Σ_{n≠m∈M} |⟨u_m|d_a u_n⟩|² ≥ 0 (Cauchy–Schwarz). Substituting the measured first-order couplings: |A^WZ_{+−,a}| = |⟨u₊|dH_a|u₋⟩|/(λ₋−λ₊) has **median 1.297e-17 over the surface, < 1e-12 at 99.96% of nodes** (both axes; the intra-pair denominator λ₊−λ₋ ≈ 1.64 is large and well-conditioned) → the numerator integrand is machine-zero pointwise → I_Ab − I_NA = −4.44e-15 (the float-cancellation floor of a 2601-node trapezoid of O(1)-scale integrands) → f_nonAb = |−4.44e-15|/1.5 = 2.96e-15 ≤ 1e-10 → the f_nonAb clause FAILs with the **direction consistent** with Step 4 (numerator = 0⁻ at floor, not structurally negative). The Im part: Im Tr_band Q_{[τ,μ]} integrates to 6.12e-18 < 1e-12 ✓ (pointwise max 1.53e-12, localized at the corner defect) — metric-not-curvature holds.

**e1 — corner-defect anatomy (why I_NA = 1.5 EXACTLY)**: the B1/B2 crossing is symmetry-ALLOWED (different U(2)-isotropy characters; von Neumann–Wigner permits exact crossing) and clips the scan window at the (0.10,+0.10) corner. The signed-col tracking jumps to an orthogonal subspace there, injecting exact-rational FD spikes: node (0,50) na = 2.500000e+05 = 4/Δ² (weight×value = 1.000000), nodes (0,49) and (1,50) na = 3.125000e+04 (weight×value = 0.250000 each) — totalling **1.0 + 0.5 = 1.5 = 100.0000% of the pinned-mesh I_NA**. Defect-excluded companions (diagnostic, NOT the clause values): I_NA_excl = 2.602e-24, I_Ab_excl = 2.603e-24, num_excl = 2.96e-28 — the interior integrand ceiling is 1.64e-21, i.e. the projector-FD round-off floor. The f_nonAb clause is artifact-ROBUST: the WZ numerator is machine-zero at every node including the defect (both arms see the same jump; their difference stays at floor).

**e2 — band-selective Schur rigidity (the central structural finding)**: gauge-free frozen-bundle witness, max pairwise ‖P_X(nᵢ) − P_X(nⱼ)‖_F across well-separated non-defect nodes:

| Band group | max ‖ΔP‖_F | Reading |
|:-----------|:-----------|:--------|
| pair (B1±) | 7.94e-14 | **FROZEN** |
| B3− / B3+ | 1.44e-14 / 1.57e-14 | **FROZEN** |
| B2− / B2+ | **2.279e-01 / 2.279e-01** | **MOVING** |

The B1 pair and the B3 triplets are **constant eigenbundles over the entire U(2)-invariant surface** (multiplicity/direction-locked isotypic slots: dH|u₋⟩ = (dλ)|u₋⟩ pointwise — the U(2)-invariant deformation family cannot rotate these slots, so their QGT is identically zero on THIS base and their CKH non-additivity is 0/0-vacuous). The **B2 quadruplets genuinely move** (subspace rotation 0.228 across the window) and carry real metric content: defect-excluded I_NA(B2) = **2.591e-02** — twenty-two orders of magnitude above the frozen pair's 2.6e-24 floor. The flat optical multiplet is the geometric carrier on this base, exactly as the plan's d2 arm anticipated ("the most Chen-Karki-Hosur-apt sector"); B2 is also the flatter band in dispersion (std(λ_B1)/std(λ_B2) = 3.2; canonical flat-vs-dispersive context: F_squeeze_bare = 54.06, S74 — narrative context, not a pin).

**e3 — frame-free B2 CKH witness**: the band operator M_ab = P(d_aP)(1−P)(d_bP)P restricted to the B2 quadruplet is **Schur-scalar**: ‖M_ab − (Tr M_ab/4)P‖/‖M_ab‖ ≈ 1e-13 at interior sample nodes (both ττ and μμ) — the same U(2) isotropy that freezes B1/B3 forces the moving B2 quadruplet's complement-QGT band-matrix to be ∝ 1₄ (Schur's lemma on the 4-dim irrep slot). Consequence: on a U(2)-invariant base the invariant complement-metric CANNOT distinguish Abelian from non-Abelian band structure (it is symmetry-forced isotropic); the non-Abelian content survives only in (i) the transport/holonomy — gauge-invariant witness 1 − |Tr W_plaq|/deg: B2 mean 4.27e-7, max 1.07e-3 (corner), pair mean 3.13e-7 — and (ii) the frame-dependence of the Abelian decomposition (d1).

**d1 — gauge-orbit spread (seed 100615, 8 global Haar U(2) rotations)**: I_NA is **exactly frame-invariant** (max ‖P_M(rot) − P_M‖ = 1.67e-16, by construction of the basis-free projector). I_Ab over the orbit spans 141.9 → 1006.9 (spread 1.005e+03 ≈ 670× I_NA) — the per-band Abelian decomposition is violently frame-dependent. Attribution: the rotated-frame rank-1 projectors inherit the pinned frame's relative-phase π-jumps, so the orbit magnitudes are FD-artifact-amplified; the qualitative contrast (invariant trace vs frame-dependent decomposition) is the load-bearing point and is exact.

**d2/d3 — B2 pinned-frame numbers + negative control**: the pre-registered B2 discriminator evaluates literally to f_nonAb(B2) = 7.440e+03 > 1e-10 → FAIL-arm reading **(a)**. Attribution: I_Ab(B2, pinned frame) = 5.77e+03 is dominated by eigh's arbitrary intra-eigenspace basis rotations inside the exactly-degenerate quadruplet (per-member rank-1 projectors are frame-dependent BY CONSTRUCTION there — the sharpened CKH point: the Abelian decomposition is not even FD-stable in a degenerate fiber); the genuine B2 motion is the e2/e1-B2 content above (‖ΔP‖ = 0.228, I_NA_excl(B2) = 2.59e-2, with 96.66% of the pinned I_NA(B2) = 0.776 carried by the 3 corner-defect nodes). The d3 NEGATIVE CONTROL fires as expected: the naive argmin(|w|) single-band U(1) FHS gives C = −7.342 (non-quantized garbage; the S96 ~0.78-class finding reproduced in kind) — the det-normalized U(deg) link is REQUIRED.

**d4 — protection mechanism**: the J/PH pair's cross-QGT channel is doubly locked: γ₉ (anticommutes with H exactly, residual 0.0e+00; maps u₋ ↦ u₊ with overlap 1.000000000) forces ⟨u₊|dH_a|u₋⟩ = −⟨u₊|dH_a|u₋⟩* (imaginary-only), and the substrate J reality (S25/S61 mechanism class) kills the imaginary part — measured |A^WZ_{+−,a}| median 1.3e-17 across the surface, both axes; the max 0.155 localizes at the corner tracking defect only.

**Cross-checks**: **CC-1** — the (0,0)-block builder at exact (τ_fold, 0) matches the s84 L12 cache (0,0) sector to max|Δ| = 9.99e-16 over all 16 |λ| values (builder-drift guard PASS; tied nearest mesh nodes 0.188/0.192 bracket the cache value 0.819741112 as expected). Sector (4,4) — repaired by W3-1 elsewhere — is not consumed; this gate touches ONLY (0,0). **CC-2** — state-FD integrals reproduce the projector-form integrals to 1e-10 (both dominated by the same defect nodes); the 94.35% pointwise rel-dev statistic is uninformative here (relative deviation of two round-off-floor fields ~1e-22). **CC-3** — C_FHS = −0.5 vs the S96 baseline 9.78e-15: fully attributed to the SINGLE corner π-plaquette at (0,49) where the signed-col tracking crosses the B1/B2 defect with overlaps above the det-link guard (S96's |λ|-argsort blocks fell below the guard → identity links); 2499/2500 plaquettes carry |F| < 1e-6 — the punctured-surface topology is trivial, consistent with the 12 zero invariants (S25/S61/S96).

**Pre-emission corrections (disclosed; composite verdict unchanged by construction)**: (i) the sign-margin was corrected from a hand-pinned −1e-15 to the canonical float-cancellation floor −1e-14 per `epistemic-discipline.md` Class 8.3 item 4 ("expected achievable floor ~10×float_eps = 2.22e-15; safe threshold < 1e-14") AFTER the first un-emitted run measured the numerator at exactly 20·ε; the raw numerator is unchanged and reported; the composite FAIL holds under both margins. (ii) The e1/e2/e3 diagnostic arms were added after the first un-emitted run to explain the corner anatomy and rigidity; the pre-registered operator clauses and their values are bit-identical across runs. Nothing was emitted before the final script state; the emitted line carries the final dual-SHA.

**Assessment + routing**: the pre-registered FAIL-arm discrimination lands on **(a)** (B2-arm f_nonAb > 1e-10): a J/PH-pair-specific anti-unitary protection — structurally informative, the CKH content lives on the flat multiplet, route to interpretation, **no registry regression** (per the plan's dual_prior this is the Track-B variant: protection specific to the PH doublet, NOT Abelian reduction of the algebra). The e2/e3 arms sharpen the reading: the protection is the chirality-lock γ₉ + J reality; the pair (and B3) bundles are moreover FROZEN (Schur-locked slots — zero QGT of any kind on this base); the CKH content that exists on this base lives on the genuinely-moving B2 quadruplet (‖ΔP‖ = 0.228, I_NA_excl = 2.59e-2), whose invariant band-matrix is Schur-scalar — so on a U(2)-INVARIANT base the Abelian-vs-non-Abelian discrimination of the bridge integrand is structurally unresolvable by the complement-metric alone (symmetry-forced isotropic). The natural forward discrimination is the same construction on an isotropy-BREAKING deformation direction (outside the U(2)-invariant family), where the multiplicity locks release. The §VII.AF.1.OP-PROJ entry is NOT regressed: the bridge object (quantum METRIC, Re QGT) and the metric-not-curvature regime are RE-CONFIRMED (Im_int = 6.1e-18; punctured-surface F-field trivial); what FAILed is the conjecture that the within-multiplet WZ non-additivity is visible on the LOWEST multiplet over THIS base — it is doubly protected there.

**Substrate framing (GEOMETRIC)**: the substrate IS the D_K eigenbundle over its own modulus space; the (τ,μ) surface IS the substrate's intrinsic Level-2 moduli-deformation manifold (phononic-framing.md). Direction: D_K eigenbundle → non-Abelian QGT (substrate-IS) → trace form Tr R → laboratory degenerate-band superfluid weight (laboratory-IN; Chen–Karki–Hosur's MoS₂/TiSe₂ 20%/50% fractions are laboratory-IN shadows — and per this gate's finding, the substrate's analog of those fractions does NOT live on the protected ground pair but on the flat optical multiplet, the inter-band-coherence carrier, consistent with the substrate's permanent structural fact that inter-sector coherence (Leggett/GGE physics) is not reducible to single-sector content). The vanishing Im part is the substrate's signature regime — metrically structured where symmetry permits motion (B2), topologically trivial everywhere (12 zero invariants; the −0.5 lattice reading is a tracking artifact at a symmetry-allowed crossing, not substrate topology).

**Output Artifacts**:

| Artifact | Path | Content |
|:---------|:-----|:--------|
| Script | `computations/session-100b/s100b_nonabelian_metric_fraction.py` | full pipeline: eigh sweep, projector QGT (LEMMA evaluator), state-FD CC arm, FHS + negative control, d1 orbit, B2 arm + e3 witness, e2 rigidity, d4 mechanism, CC-1 cache check, verdict payload |
| Data | `computations/session-100b/s100b_nonabelian_metric_fraction.npz` | W_signed, integrand maps, gap12, defect anatomy, orbit, rigidity table, A_prot map, cache CC, dual-SHA |
| Plot | `computations/session-100b/s100b_nonabelian_metric_fraction.png` | 6 panels: metric-trace map, non-additivity integrand, gap12/regime map, Im map, gauge-orbit, protection map |
| Run log | `computations/session-100b/s100b_nonabelian_metric_fraction_run.log` | full stdout incl. INPUT-PIN plan-pin matches |
| Verdict | `computations/session-100b/s100b_gate_verdicts.txt` | canonical line + dual-SHA companion + schema-v2 3-tuple + 4 extra rows (UNTRUSTED-UPSTREAM, regulator_pin, gauge_pin, anatomy) |

**4-tuple**: (value=f_nonAb=2.960595e-15_…_ndefect=3, scheme=WILCZEK-ZEE-FHS-DETU2, convention=RATIO, L_max=10). **Dual-SHA**: audit=4a03497c43a97335…, content=03c7532340767a99… (full 64-hex on the verdict line). Input plan-pins verified at runtime: s96_scaffold, dirac_spectrum, s84_spectrum_cache all [PLAN-PIN MATCH].

---

### §W6-3. S100b-LEGGETT-DAMPING-INHERITANCE (landau-condensed-matter-theorist)

**Status**: COMPLETED
**Gate ID**: `S100b-LEGGETT-DAMPING-INHERITANCE`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (χ-inheritance transport audit: MgB₂ Leggett damping → substrate DM inter-band-coherence channel; CANONICAL-FORM LAW binds all survival outputs to ratio/inequality form)
**Agent**: `landau-condensed-matter-theorist`
**Hypothesis**: The Yuan MgB₂ Leggett-mode damping, transported through χ : ℂ ⊕ ℍ ⊕ M₃(ℂ) → M₂(ℂ) (M₃(ℂ) → 0), classifies entirely into χ-closed channel classes — pair-breaking continuum (kinematically/Z₂-blocked) and extrinsic bath (no substrate counterpart) — so Γ_grav < H_0 holds and the CONDITIONAL survival ratio τ_DM/t_univ = 1.13e65 stands.
**Plan reference**: `sessions/session-plan/session-100b-plan-w6.md` §W6-3 (PDF-extraction honesty pins, χ morphism pin, 3-class channel set, CANONICAL-FORM LAW, substitution chains A/B/C).

**MCP Pre-Compute Audit**:

| Query | Salient return |
|:------|:---------------|
| `search_knowledge("Leggett damping MgB2 inheritance")` | No prior gate covers the χ-transport audit — NOT PRE-CLOSED. Prior Leggett-damping artifacts are substrate-internal channels (S50/S53/S61); the LEGGETT-DAMPING-50 PASS row carries the historical ω_L = 0.070 / Q = 6.7e5 values. |
| `get_constant("Delta_BCS")` | 0.4642547394830737 (R-PROTECTED; S70 BCS-GAP-CANONICAL-70) — matches plan pin. |
| `get_constant("omega_L1")` | 0.138 (no PROVENANCE entry in knowledge DB; canonical_constants.py:733 is the authoritative import). |
| `get_constant("Mass_LeggettDM_over_Delta_BCS")` | 11.97 (S70 LEGGETT-MOMENT-70; CONDITIONAL on Γ_grav < H_0; pinned S96 W7-2). |
| `get_constant("H_0_inv_s")`, `get_constant("t_universe_s")` | 2.184e-18 s⁻¹; 4.35e17 s (PDG/Planck-class; no PROVENANCE rows). |
| `get_constant("M_KK_inv_seconds")` | 8.860439881925477e-42 s (S96-W1-MKK-SECONDS). |
| `get_constant("Q_Leggett")` | 670000.0 (knowledge DB; see tension (2) below). |
| `get_constant("tau_fold")` | 0.19 (CONST-FREEZE-42) — context only. |
| `trace_entity("LEGGETT-GRAV-DECAY")` | Theorem proven_2046 (CRITICAL conditional: Γ_grav > H_0 ⇒ DM sector collapses); gates -67 (PASS, Γ_grav < H_0), -73a (PASS, τ_DM/t_univ = 1.13e65, Z₂ parity P_L from J-evenness), S95 LEGGETT-GRAV-DECAY-CONDITIONAL (Row #68; Γ_grav/H₀ ≈ 8.85e-66; 65 OOM margin; Ω_DM h² = 0.120 = 0.7σ vs Planck). All plan survival anchors confirmed — this gate re-affirms, it does not re-derive. |

**Provenance tensions recorded** (per the wave's mandatory pre-compute-audit clause; record-only, NOT re-adjudicated): (1) ω_L1 — the atlas-07 LEGGETT-MODE-48 row carries the historical S48 values (ω_L1 = 0.070, Q = 670,000); canonical_constants.py:733 carries the authoritative ω_L1 = 0.138 (imported). (2) Q_Leggett — the plan text asserts "Q_Leggett = 18.6 provenanced S50 LEGGETT-DAMPING-50", but the on-disk canonical_constants.py:2222 carries `Q_Leggett = 6.7e5`, which matches the S50 producing artifact itself (s50_leggett_damping.npz: Q_total = 665595 ≈ 6.7e5, Γ_grav-limited at T = 0; S53/S61 npz also checked, no 18.6 anywhere). The 18.6 figure matches no on-disk artifact — plan-text drift recorded per `substrate-first-canonical-sourcing.md §(ii.B)`; the script imports the on-disk canonical. Q_Leggett is DIAGNOSTIC-only in this gate (formation-epoch comparator); no PASS impact on any clause.

**Verdict**: **PASS** (composite; schema-v2 3-tuple: `sign_verdict=PASS`, `magnitude_verdict=PASS`, `regime_verdict=VALID`; gate-verdicts.md collapse rule applied verbatim and asserted equal to the pre-registered operator conjunction in-script)

4-tuple: `(value=<channel-closure summary>, scheme=CHI-INHERITANCE-TRANSPORT-AUDIT, convention=RATIO, L_max=N/A)`
Dual-SHA (canonical, latest non-superseded line): `audit_sha256=bce1ed8010a6a023db44d8076485a5e3c68249f2b31397caf4b862d5fe2453dc` · `content_sha256=8a749fe6e7bf2c8f7f883005ee68fe601ef9c4943b0fb5e6a0e1b468705f37b0` (schema_version=S84+), carrying `supersedes=cd5b0bc3a037aa68d40cbb85199baa2c4a438c71fa8bae10ef89dfa6c320b573` per the gate-verdicts.md Option-A protocol — the superseded first emission differed ONLY in the producing script’s plot-layout block (constrained_layout + annotation de-collision); all physics values, verdict, and 3-tuple identical. Emitted race-safe via `emit_verdict` — canonical line + dual-SHA companion + 3-tuple row + 4 audit rows per emission.

**Results**:

*D1 — Extraction (as-printed; SHA-pinned PDF `f8f38970…` verified at runtime; all 33 pages read via the Skill(pdf) 4-chunk route)*:

| Element | As-printed value | Source location in arXiv 2412.13830 |
|:--------|:-----------------|:------------------------------------|
| ω_L (observed) | **1.8 THz ± 0.8 THz** — overdamped oscillation; center + error bar by Lorentz fitting of segmented-FFT spectra; "broad peak", softens with T | main text p.4 + p.12; Fig. 3B/3G; p.11 (fit method) |
| ω_L (calculated) | **1.81 ± 0.27 THz** (zero-T) — Eq. (11) ω_L² = (N_σ+N_π)/(N_σN_π) · 4V_σπΔ_σΔ_π/detV with N_σ = 2.04, N_π = 2.78 Ry⁻¹spin⁻¹cell⁻¹, 3 pairing-potential sets (Liu/Choi/Golubov) | SI §XII p.26-27 |
| Δ_π | **0.44 THz** (2Δ_π = 0.88 ± 0.05 THz onset absorption in σ₁ at 2 K) | p.10; SI §XII |
| Δ_σ | **1.32 THz** (empirical Δ_σ ≈ 3Δ_π; 2Δ_σ ≈ 2.64 THz) | p.10; SI §XII |
| Γ_L / linewidth | **No separately-named Γ_L or decay-time constant is printed.** Width-class published number: the ±0.8 THz Lorentz-fit spread of the explicitly "overdamped"/"broad" feature → width-proxy (Γ_L/ω_L)_lab = 0.8/1.8 = 0.444 (derived-from-printed; DIAGNOSTIC only — the PASS predicate never consumes the Γ_L magnitude). Extraction judged COMPLETE on the "Γ_L or linewidth" element with this qualification recorded. | p.11-12; Fig. 3E/3G |
| Mechanism attribution (paper's own) | Mode = Leggett (relative π/σ condensate phase): "over-damped oscillation corresponding to the Leggett mode" (abstract). Damping: "overdamped"/"strongly damped"/"heavily damped"; decay "much faster than that observed in NbN" (Fig. 3E: "Fast-decay Leggett-mode" vs "Persisting Higgs-mode"). Attribution sentence (p.12): "the presence of inter-band coupling between the two superconductivity order parameters changes the spectrum of collective modes and affects their nonlinear responses." Kinematic position fixed by the paper's own printed numbers: ω_L = 1.8 THz > 2Δ_π = 0.88 THz (mode INSIDE the π-band pair-breaking continuum) and < 2Δ_σ = 2.64 THz. Per the paper's own refs [20] (Leggett 1966) + [24] (Blumberg 2007 — the source of its SI Eq. 11), continuum (pair-breaking) decay is OPEN when ω_L > 2Δ_min ⇒ continuum-resonant. UNAMBIGUOUS at channel-class level — the INFO arm does not fire. | abstract; p.11-12; Fig. 3E |

*D2 — Kinematic + protection-layer map (substitution chains A/B executed with substituted numbers)*:

```
Chain A (substrate L1 collective mode):
  x_L1 = ω_L1/(2·Δ_BCS) = 0.138/(2 × 0.4642547394830737)
       = 0.138/0.9285094789661474 = 0.148625   (6 s.f.; plan pin reproduced exactly)
  0.148625 < 1 ⇒ L1 BELOW the pair-breaking edge — quasiparticle channel kinematically CLOSED.

Chain B (substrate DM relic quantum — protection NOT kinematic):
  x_DM = (m_DM/Δ_BCS)/2 = 11.97/2 = 5.985 > 1 ⇒ relic ABOVE the edge
  ⇒ protection = Z₂ parity P_L from J-evenness (LEGGETT-GRAV-DECAY-73a)
    + single-Leggett decay FORBIDDEN (S67, PROVEN) — symmetry selection rule, not kinematics.

Lab (as-printed Yuan values):
  x_lab,π = ω_L/(2Δ_π) = 1.8/0.88 = 2.045455 ≥ 1  (π continuum OPEN — overdamping is continuum-resonant)
  x_lab,σ = ω_L/(2Δ_σ) = 1.8/2.64 = 0.681818      (diagnostic; below the σ edge)
```

The two substrate Leggett-channel objects are NOT conflated (plan D2 law): the THz-driven lab mode is the analog of the L1 mode (kinematically protected, x = 0.148625); the survival claim concerns the relic quantum (symmetry-protected, x = 5.985).

*Chain C — transported-rate edge (class (iii) only)*:

```
m_DM  = 11.97 × 0.4642547394830737 = 5.5571292 M_KK
      = 5.5571292 / 8.860439881925477e-42 s = 6.271844e41 s⁻¹
transport_factor = m_DM/H_0 = 6.271844e41 / 2.184e-18 = 2.871723e59
survival edge (Γ_L/ω_L)_crit = 1/transport_factor = 3.482230e-60
```

Plan 6 s.f. pins (2.87172e59; 3.48222e-60) reproduced from canonical imports; the last-digit wobble on the edge is the plan's rounded-intermediate artifact (within Class-8.3 publication precision; full float64 in the npz).

*D3 — χ-transport audit (pre-registered 3-class classification of every extracted mechanism; χ : ℂ ⊕ ℍ ⊕ M₃(ℂ) → M₂(ℂ), M₃(ℂ) → 0, ker χ = M₃(ℂ) — `inheritance-falsifier-protocol.md` canonical realization + `3HeB-inheritance-canonical.md`)*:

| Channel class | Fired by extraction? | χ-closure for the substrate relic |
|:--------------|:---------------------|:----------------------------------|
| (i) PAIR-BREAKING CONTINUUM | **YES** — the single extracted mechanism (coded rule: x_lab,π = 2.045455 ≥ 1; continuum-resonant overdamping) | **χ-CLOSED on both substrate objects.** L1 mode: kinematic (x_L1 = 0.148625 < 1; the dimensionless continuum position is evaluated per system, and the substrate's is on the protected side of the edge — opposite the lab mode). DM relic quantum: pair-breaking of a single relic quantum requires a Z₂-ODD single-quantum vertex — FORBIDDEN (73a P_L from J-evenness + S67 PROVEN single-Leggett-decay prohibition). |
| (ii) EXTRINSIC BATH | NO — the paper makes no extrinsic (impurity/inhomogeneity/thermal/phonon-bath) attribution for the LEGGETT damping; the p.9 dirty-limit remark concerns the π-band Higgs/THG channel | Would be χ-closed regardless: no substrate counterpart (substrate-IS; no container bath per `phononic-framing.md`). Substrate-internal comparator Q_Leggett (S50, formation-epoch acoustic channel) cited DIAGNOSTIC-only, scoped to the transit/GGE-formation epoch; the relic state is protected by fabric-scale Ordered-Veil integrability (RECONCILED scope: fabric-scale Poisson ⟨r⟩ = 0.367; the retracted single-cell permanence is NOT invoked). |
| (iii) INTRINSIC PARITY-EVEN MULTI-QUANTUM | **EMPTY** — no below-threshold, bath-free, parity-even intrinsic mechanism is proposed anywhere in the paper; structurally, the observed damping operates AT/ABOVE the continuum edge (x ≥ 1) while class (iii) is defined by below-threshold operation | No member transports. The quantitative test is vacuous. Counterfactual diagnostic (NOT fired): IF the lab width-proxy were χ-open, Γ_inherit/H₀ = 0.444 × 2.871723e59 = 1.276e59 ≫ 1 — confirming the pre-registered structural consequence: ANY measurable χ-open lab damping (≳1e-6 of the mode frequency) exceeds the 3.48e-60 edge by ≳54 OOM, so the gate's evidential content IS the channel-closure audit, not the smallness of a transported number. |

*D4 — Survival statement (wave CANONICAL-FORM LAW: ratio/inequality form ONLY)*:

- **Γ_grav < H₀ holds**: Γ_grav/H₀ ≈ 8.85e-66 (S95 LEGGETT-GRAV-DECAY-CONDITIONAL, Row #68; 65 OOM margin).
- **Survival margin ratio**: τ_DM/t_univ = 1.13e65 (LEGGETT-GRAV-DECAY-73a PASS; Z₂ parity P_L from J-evenness).
- **Consistency identity**: H_0_inv_s × t_universe_s = 2.184e-18 × 4.35e17 = 0.950 ~ O(1), and 1/(Γ_grav/H₀) = 1.12994e65 vs τ_DM/t_univ = 1.13e65 — the same statement to O(1), identical at 3 s.f.
- Non-canonical caveat (single pre-authorized sentence): the index's τ_DM = 4.93e82 s is non-canonical — do not propagate.

*Operator conjunction (pre-registered)*: extraction_complete = True ∧ (every extracted mechanism in class (i)/(ii) AND χ-closed) = True ∧ (no transported channel ≥ 1) = True (class-(iii) members: 0) ⇒ operator PASS; collapse-rule composite = PASS (in-script assert: collapse == operator).

*[SIGN] 3-tuple*: sign_verdict = **PASS** (pre-registered direction Chain C Step 5 — the extracted MgB₂ damping attribution lands in class (i)/(ii), expected continuum-resonant or extrinsic: realized as class (i) continuum-resonant); magnitude_verdict = **PASS** (no transported channel ≥ 1; substrate anchor 8.85e-66 ≪ 1); regime_verdict = **VALID** (exact float64 scalar ratio arithmetic on canonical pins; no scan, no expansion regime; the extraction width-proxy qualification is an extraction-precision note, not a regime breach — the PASS predicate never consumes the Γ_L magnitude).

*Cross-checks*: (1) static input SHAs verified at runtime against plan pins (yuan_pdf `f8f38970…` ✓, chi_morphism_canonical `f5a4204a…` ✓; mismatch ⇒ hard abort); (2) plan 6 s.f. pins x_L1 = 0.148625, x_DM = 5.98500, transport 2.87172e59, edge 3.48222e-60 all reproduced from canonical imports; (3) paper-internal ω_L consistency: observed 1.8 ± 0.8 THz vs calculated 1.81 ± 0.27 THz (SI Eq. 11) — mutually consistent; (4) 73a ↔ S95 anchor consistency through H₀t_univ = 0.950 (above); (5) collapse-rule-vs-operator equality asserted.

*Dual-prior discriminator (plan)*: PASS → **0.95 to Track A** (lab Leggett damping is χ-closed for the relic; substrate protections — kinematic for L1, Z₂/J-evenness for the DM quantum — untouched).

**Output Artifacts**:

| Artifact | Path | Content |
|:---------|:-----|:--------|
| Script | `computations/session-100b/s100b_leggett_damping_inheritance.py` | D1-D4 pipeline; chains A/B/C; 3-class audit; dual-SHA; `print_verdict_payload` |
| Data | `computations/session-100b/s100b_leggett_damping_inheritance.npz` | extraction record (as-printed + quotes), kinematic ratios, transport edge, classification JSON, survival anchors, verdict block, full-float64 values |
| Plot | `computations/session-100b/s100b_leggett_damping_inheritance.png` | Panel A: per-system pair-breaking-edge map x = ω/(2Δ) (lab π/σ; substrate L1/DM; edge x = 1); Panel B: χ-transport edge on log axis (lab width-proxy NOT transported vs Γ_grav/H₀ = 8.85e-66 vs edge 3.48e-60) |
| Verdict | `computations/session-100b/s100b_gate_verdicts.txt` | canonical line + dual-SHA companion + schema-v2 3-tuple + 4 audit rows (D1/D3/D4/provenance), emitted via race-safe `emit_verdict` |

**Substrate framing (PHONONIC)**: The framework's dark matter IS a Leggett-channel GGE quasiparticle — an inter-band relative-phase coherence mode of the substrate condensate, CPT-neutral and non-annihilating, with mass anchor 11.97 × Δ_BCS on the BCS gap scale (substrate-IS). MgB₂'s THz-driven Leggett mode is a laboratory-IN shadow: a two-condensate child in which the same relative-phase degree of freedom is driven and its damping measured. Direction of explanation: substrate condensate sectors → inter-band coherence mode (substrate-IS) → χ inheritance morphism (M₃(ℂ) → 0) → two-band laboratory Leggett mode (laboratory-IN). The audit direction never inverts — the lab measurement CONSTRAINS the universality class of decay channels; it does not define the substrate mode. Landau reading: the Leggett mode is the relative-phase Goldstone-class oscillation between two condensate order parameters; its decay channels are classified by symmetry (Z₂ parity from J-evenness) and kinematics (position relative to the 2Δ pair-breaking edge) BEFORE any rate is computed — the three-class transport audit executed here IS that classification, run against the extracted lab attribution. Slot-law compliance: this section makes no quantum-metric claim; the wave's bridge object is §VII.AF.1.OP-PROJ (never §VII.W).

**Assessment**: The first laboratory anchor on the DM-mode lifetime question lands CONSISTENT. MgB₂'s overdamped Leggett mode — the most direct laboratory realization of the substrate's inter-band coherence channel — derives its entire measured damping from a channel class (pair-breaking continuum, continuum-resonant at x_lab = 2.045455) that the χ morphism cannot transport onto the substrate relic: the substrate L1 mode sits at x_L1 = 0.148625, kinematically below its own edge (the opposite side from the lab mode), and the DM relic quantum at x_DM = 5.985 is protected by the Z₂/J-evenness selection rule (single-quantum vertex Z₂-odd, FORBIDDEN per 73a + S67). The lab system exhibits NO universality-class (below-threshold, bath-free, parity-even) decay channel — exactly the class whose existence would have transported through χ and threatened the non-annihilation claim. Constraint-map content: the region "the best available two-band laboratory child exhibits a χ-open inter-band-coherence decay class" is EXCLUDED at the current extraction; the C11 conditional (Leggett-channel DM mass anchor, CONDITIONAL on Γ_grav < H₀) gains a lab-side consistency leg, while the CONDITIONAL tag itself is NOT discharged — this gate cannot discharge it (Element-annotation routed to mack-cosmic-bridge as sole falsifier-surface writer, per the Wave 6 → Wave 7 decision point).

---

## Wave 6 Synthesis (team-lead)

**Written**: 2026-06-07, session close. All 3 gates landed; verdicts verified on disk against each gate's `output_artifacts` must_contain set, including the W6-3 Option-A supersession chain and the W6-1/W6-2 UNTRUSTED-UPSTREAM caveat rows.

| Gate | Verdict | Headline value |
|:-----|:--------|:---------------|
| §W6-1 S100b-VII-AF1-BDG-PROJECTOR-CONFIRM | **PASS** | Δ_disc = 0.341976 = 342× the 1e-3 Level-2 floor; 94.8% of BdG metric content in C² coset directions (audit `06206dbbd1f6ec38…`) |
| §W6-2 S100b-NONABELIAN-METRIC-FRACTION | **FAIL** (reading a: J/PH-protected, B2-carries-CKH) | f_nonAb = 2.96e-15 on the pair (float floor); B2-arm 7.44e+03; no registry regression (audit `4a03497c43a97335…`) |
| §W6-3 S100b-LEGGETT-DAMPING-INHERITANCE | **PASS** (Option-A canonical; supersedes `cd5b0bc3…`) | class-(iii) decay channels EMPTY; x_L1 = 0.148625 < 1; DM Z₂-protected at x_DM = 5.985 (audit `bce1ed8010a6a023…`) |

**Wave reading.** The §VII.AF.1 bridge is HARDER after this wave, and on exactly the axes the litrev flagged. W6-1 confirms the Element-5 projector choice is load-bearing physics, not convention: swapping the ordered-state (quasihole) projector for the normal-state arm loses Δ_disc = 0.342 of pairing content — 342× the Level-2 floor — localized in the order-parameter-gated C² coset directions (0.0396 → 0.0128), exactly the Landau reading. Free structural bonus: λ₈ content = 4.9e-31 machine-zero — permanent wall #5 ([iK₇, D_K] = 0) manifest directly in the metric trace. W6-2's FAIL is the informative arm of its own pre-registered discriminator: the lowest multiplet's non-Abelian fraction is zero because it is DOUBLY protected (γ₉ forces the cross-WZ channel imaginary-only; J reality kills it) — while the flat B2 quadruplets carry genuine non-Abelian content (I_NA = 2.59e-2) under band-selective Schur rigidity (pair + B3 bundles FROZEN, QGT ≡ 0). The deepest finding is a no-go: the B2 band-matrix is Schur-scalar (∝ 1₄ to 1e-13), so Abelian-vs-non-Abelian is SYMMETRY-UNDECIDABLE on any U(2)-invariant base — discrimination requires isotropy-breaking deformations (CF below). The S96 suspicious values (I_NA = 1.5 exact, C_FHS = −0.5) are both reconciled as FD-defect corner artifacts. W6-3 lands the first laboratory anchor on the DM-mode lifetime: MgB₂'s overdamped Leggett mode derives its entire damping from the pair-breaking continuum class, which the χ morphism CANNOT transport onto the substrate relic (kinematically closed for L1; Z₂/J-evenness forbidden for the DM quantum); class-(iii) — the only dangerous class — is EMPTY at this extraction. C11 gains a lab-side consistency leg; the CONDITIONAL tag stands.

**Decision-point evaluation** (plan §"Wave 6 → Wave 7 Decision Point"): W6-1=PASS → Element-5 confirmation annotation landed by mack (sole-writer, in-session): `sessions/permanent-results-registry.md:15013`, caveat-tagged, "annotation only — registered status and three-level ladder unchanged". W6-2=FAIL(a) → J/PH-protection interpretation recorded (this synthesis + §W6-2); no registry regression (correct branch). W6-3=PASS → C11 lab-side consistency-leg annotation landed by mack in-cell on the C11 row: `sessions/framework/Atlas/atlas-04-assumptions.md:70`, CONDITIONAL status cell byte-identical (tag NOT discharged).

**Carry-Forward Computations (MATH ONLY — propagate to S101)**

### CF-S101-B2-ISOTROPY-BREAKING — discriminate Abelian-vs-non-Abelian on the B2 multiplet via isotropy-breaking deformations

Lifted from §W6-2 structural finding 2 (band-selective Schur rigidity / symmetry-undecidability): **What** — evaluate the B2 quadruplet's non-Abelian metric fraction on an isotropy-BROKEN base family (deformations breaking the U(2)-invariance that forces the Schur-scalar band-matrix), measuring whether f_nonAb(B2) survives off the symmetric point — the discrimination W6-2 proved impossible on any U(2)-invariant base. **Inputs** — `s100b_nonabelian_metric_fraction.npz` (B2 eigenbundle, I_NA = 2.59e-2 baseline, frame-invariance diagnostics d1), the gauge-free projector machinery from `s100b_nonabelian_metric_fraction.py` (operator-independent per §W6-2 caveat paragraph), a pre-registered deformation family (to be pinned at S101 plan-freeze). **Gate** — pre-registered at S101 plan-freeze: f_nonAb(B2, deformed) threshold + direction (the W6-2 FAIL-arm discriminator template applies; B2-arm baseline 7.44e+03 anchors the scale). **Effort** — 1 compute gate, ≤ half a session (small-matrix eigenbundle sweep; GPU optional).

### CF-W6-1 (AF1-MODE-A-ABSOLUTE) — Mode-A absolute reproduction of R^BdG from the projector side *(investigation append, 2026-06-07, /rclab-investigate consolidator; Q-other solo compute follow-up)*

W6-1's reproduction clause was VACUOUS by pre-declared Mode-B construction (delta_BdG ≡ 0; the s84 W10a-114 npz lacks the Mode-A sufficiency set {cocycle_representative, generator_basis, N_pair}) — the s86-hp1 V4 question ("verify the projector-side value reproduces the W5-6 value") is therefore only half-answered: discrimination confirmed at 342×, absolute reproduction un-run. **What** — reconstruct the W10a-114 Heitsch/GV-lift normalization chain (S83 W1-G2) from the producing script and evaluate R^BdG absolutely from the projector side. **Inputs** — `computations/session-84/s84_w10a_eps_h_k_class_location.py` (+ npz), `computations/session-100b/s100b_vii_af1_bdg_projector_confirm.{py,npz}` (phi_signed values, Kosmann generator basis), s86-hp1 eqs. R-V1.1–R-V1.3. **Gate** — delta_BdG(Mode-A) ≤ 1e-3 (same Level-2 L^-3 envelope; pre-register at S101 plan-freeze; carries the same UNTRUSTED-UPSTREAM caveat until the τ=0 canonicity adjudication lands). **Effort** — 1 gate, ≤ half a session.

**Effected In-Session (NON-MATH — completed before STOP)**

- [x] §VII.AF.1.OP-PROJ Element-5 projector-choice CONFIRMATION annotation (W6-1 PASS routing) — mack-cosmic-bridge sole-writer via `s100b_close_mack_registry_batch3.py` — `sessions/permanent-results-registry.md:15013` (§-body end; STATE-PROJ heading intact at 15015) — audit `06206dbbd1f6ec38`
- [x] C11 lab-side consistency-leg annotation, CONDITIONAL tag NOT discharged (W6-3 PASS routing) — mack-cosmic-bridge sole-writer, in-cell additive — `sessions/framework/Atlas/atlas-04-assumptions.md:70` (status cell byte-identical, grep-verified) — audit `bce1ed8010a6a023`
- [x] UNTRUSTED-UPSTREAM caveats carried on W6-1/W6-2 (verdict extra-rows + WP paragraphs; W6-3 not a cache consumer — correctly uncaveated) — landau + berry in-gate — `s100b_gate_verdicts.txt` — trigger audit `bea5401ae1ac3c4d`
- [x] `tools/pdf-extract-pages.py` → `tools/archive/pdf-extract-pages.py` path drift in the pdf skill (surfaced by W6-3's extraction run) — orchestrator-direct — `.claude/skills/pdf/SKILL.md:32` — verified archive copy exists, root copy absent

**Process observations (closed in-session; do NOT propagate)**: W6-3's plan-text `Q_Leggett = 18.6` matched no on-disk artifact; the agent correctly imported the canonical `Q_Leggett = 6.7e5` (canonical_constants.py:2222) per the plan's own authority rule — diagnostic-only, no PASS impact, recorded in §W6-3 process notes. W6-3's Option-A corrective emission (plot-layout fix; physics byte-identical) carries the full-64-hex supersedes token — chain verified.

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-07 | §VII.AF.1.OP-PROJ Element-5 projector choice | registered (choice unconfirmed as load-bearing) | CONFIRMED load-bearing at the PRIMARY ζ-pairing layer (342× floor; content loss localized to order-parameter-gated C² coset) | W6-1 PASS |
| 2026-06-07 | Non-Abelian quantum-metric content (flat-band sector) | presumed accessible on the lowest multiplet | LOCALIZED to B2 quadruplets (J/PH double protection kills the pair channel); Abelian-vs-non-Abelian SYMMETRY-UNDECIDABLE on U(2)-invariant bases | W6-2 FAIL(a) |
| 2026-06-07 | S96 I_NA = 1.5-exact + C_FHS = −0.5 anomalies | unexplained | RECONCILED as FD-defect corner artifacts (3 nodes; single π-plaquette) — not topology | W6-2 corner anatomy |
| 2026-06-07 | C11 (Leggett-channel DM, CONDITIONAL on Γ_grav < H₀) | CONDITIONAL, no lab-side evidence | CONDITIONAL + lab-side consistency leg (class-(iii) χ-transportable decay channels EMPTY in the best two-band child) | W6-3 PASS |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Other | Size |
|:-----|:-------|:------------|:------------|:------|:-----|
| W6-1 | s100b_vii_af1_bdg_projector_confirm.py | ✓ | ✓ | — | 39.6 KB / 16.9 KB / 111 KB |
| W6-2 | s100b_nonabelian_metric_fraction.py | ✓ (600 KB) | ✓ | run.log | 64.6 KB / 600 KB / 268 KB |
| W6-3 | s100b_leggett_damping_inheritance.py | ✓ | ✓ | — | 39.7 KB / 20.8 KB / 111 KB |
