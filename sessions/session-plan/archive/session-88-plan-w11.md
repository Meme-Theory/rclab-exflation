# Session 88 Plan — Wave 11: PV recalibration + W1b housekeeping + Λ_SA emissions

> **Provenance**: planner-w11 dispatch (S88 W11 cluster); 14 items 121-134.
> **Theme**: PV recalibration + W1b housekeeping + Λ_SA emissions + necessity-table promotion.
> **Orchestrator**: gen-physicist | **CO**: connes-ncg-theorist (#123, #125, #127) + lizzi-spectral-functional-theorist (#121, #122, #126).
> **Verdict source**: `computations/s88_gate_verdicts.txt`.

---

## Wave 11 Summary

Wave 11 closes seven W1b carry-forwards (PV scheme verification, PS A_F recalibration at L=12, Connes-distance subalgebra restriction, a_n_FW promotion, A_F=M_2(ℂ) toy biconditional retest, Mellin-cone no-go full-spectrum retest, CM-1995 cutoff_sqrt atlas cross-check), re-emits five Λ_SA structural anchors as direct computation verdict lines (S46/S64/S65/S77/S86-W1-C9), promotes §VII.X.2 NECESSITY from STAGE-1-CANDIDATE → STAGE-3-PERMANENT once the 6/6 anchor SHA condition is met, and documents one in-session closure (windowed-PV subtraction as SD-refinement, HK-2 closed at W1b-1).

Strict substrate-first framing: every gate operates on substrate-IS observables (D_K spectral moments at Jensen-deformed SU(3); Mellin-cone residues; finite-spectrum Connes distance on A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)) and never frames substrate results via GR-as-container.

## Wave 11 Decision Point Prerequisites

| Prereq | Source | SHA | Status |
|:-------|:-------|:----|:-------|
| L=12 D_K^2 spectrum cache | `computations/s84_spectrum_cache_L12_tau019.npz` | `9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9` | AVAILABLE |
| L=10 D_K^2 spectrum cache (155,984 eigvals) | `computations/s84_spectrum_cache_L10_tau019.npz` | `<pinned at dispatch>` | AVAILABLE |
| W1b-1 PV-vs-SD residual record | `sessions/archive/session-87/session-87-results-workingpaper.md §W1b-1` | `<pinned at dispatch>` | LANDED S87 |
| W1b-5 PS A_F finite-L=10 6/6 axioms PASS | `sessions/archive/session-87/session-87-results-workingpaper.md §W1b-5` | `<pinned at dispatch>` | LANDED S87 |
| W1b-6 Connes-distance CLASS-γ closure | `sessions/archive/session-87/session-87-results-workingpaper.md §W1b-6` | `<pinned at dispatch>` | LANDED S87 |
| W1b-4 paired-slot near-unique 7436/3812 ratio | `sessions/archive/session-87/session-87-results-workingpaper.md §W1b-4` | `<pinned at dispatch>` | LANDED S87 |
| W1a-2 Mellin-cone no-go theorem (4-eigvalue toy) | `sessions/archive/session-87/session-87-results-workingpaper.md §W1a-2` | `<pinned at dispatch>` | LANDED S87 |
| W1a-5 §VII.W-2 biconditional FORWARD-only | `sessions/archive/session-87/session-87-results-workingpaper.md §W1a-5` | `<pinned at dispatch>` | LANDED S87 (BACKWARD deferred) |
| W1a-6 §VII.X.2 NECESSITY STAGE-1-CANDIDATE | `sessions/permanent-results-registry.md §VII.X.2` | `<pinned at dispatch>` | STAGE-1 LANDED |
| canonical_constants.py | `computations/canonical_constants.py` | `<pinned at dispatch>` | AVAILABLE |
| Cross-pillar bridge anatomy rule | `.claude/rules/cross-pillar-bridge-anatomy.md` | `<pinned at dispatch>` | MANDATORY at K=2 |
| Joint-theorem-promotion 4-stage | `.claude/rules/joint-theorem-promotion.md` | `<pinned at dispatch>` | MANDATORY |

---

## §W11-121 — `S88-PV-SCHEME-MPMATH-MELLIN-DIRICHLET-VERIFY`

- **Gate ID**: `S88-PV-SCHEME-MPMATH-MELLIN-DIRICHLET-VERIFY`
- **Trigger**: `[VERIFY]`
- **Classification**: GEOMETRIC (substrate-spectral; D_K^2 Mellin-Dirichlet identity at Pauli-Villars regularization)
- **Agent**: lizzi-spectral-functional-theorist (orchestrator); gen-physicist (CO-author for mpmath quadrature)
- **Hypothesis**: The 1.292e-06 residual measured at W1b-1 in the PV scheme against the §VII.U Mellin-Dirichlet identity ζ_D(s)·Γ(s/2) = ∫₀^∞ t^(s/2−1) K(t) dt is QUADRATURE-BOUNDED (a numerical-integration floor under n_quad=8192 trapezoidal log-spaced nodes), NOT identity-violating (a structural failure of the PV-scheme Mellin-Dirichlet correspondence).
- **Method**: Re-evaluate both sides of §VII.U at L_max=12 in the PV scheme using mpmath at 50-digit working precision (`mp.dps = 50`). Use mpmath.quad for the heat-kernel integral with adaptive Gauss-Legendre + Tanh-Sinh node-doubling until two consecutive doublings agree at < 1e-40. Compute LHS ζ_D(s)·Γ(s/2) symbolically in mpmath at s ∈ {3, 4, 5} (canonical Seeley-DeWitt poles). Compute residual = |LHS - RHS| at each s. PASS iff residual ≤ 1e-30 at every s (i.e., the W1b-1 1.292e-06 residual is structurally QUADRATURE-BOUNDED — vanishes by ≥ 24 OOM under refined precision); FAIL iff residual ≥ 1e-12 at any s after mpmath refinement (i.e., identity-violating); INFO if 1e-30 < residual < 1e-12 (intermediate; quadrature still bounding above the symbolic identity floor).
- **Machinery pin**: `mp.dps = 50`; `mpmath.quad(method='tanh-sinh', maxdegree=15)`; `s_test = [3, 4, 5]`; `L_max = 12`; spectrum cache `s84_spectrum_cache_L12_tau019.npz` SHA `9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9`; PV mass-cutoff `M_PV = 10·M_KK` (matches W1b-1 pin); regularization scheme tag `PV-mpmath-50dp`.
- **4-tuple**: `(value=residual_max, scheme=PV-mpmath-50dp, convention=Mellin-Dirichlet-mpmath-trapezoidal-tanh-sinh, L_max=12)`
- **Threshold**: PASS_REL_TOL ≤ 1e-30; FAIL_REL_TOL ≥ 1e-12 (identity-violating ceiling)
- **Substitution chain (inside gate block)**:
  - Step 1: Definition. Mellin-Dirichlet identity §VII.U: `ζ_D(s) · Γ(s/2) = ∫₀^∞ t^(s/2−1) K(t) dt` where `K(t) = Σ_n m_n · exp(-t·λ_n²)` is the heat-kernel trace.
  - Step 2: Substitution under PV scheme. PV inserts a regulator `K_PV(t) = K(t) - exp(-t·M_PV²)·K_PV_ghost(t)`; the regulator term must vanish identically under the mpmath integration if the PV scheme is structurally consistent with the Mellin-Dirichlet image.
  - Step 3: Simplification. residual(s) = `|LHS(s) - RHS_mpmath(s)|` at fixed s ∈ {3, 4, 5}. Direction read: residual scales as quadrature-floor (≈ machine_eps · |RHS|) iff identity holds; scales as |RHS| iff identity violated. At mpmath 50-dp, machine_eps ≈ 1e-50; |RHS| at s=4 is O(M_KK^2) ≈ O(1) in M_KK units, so quadrature floor is ≈ 1e-50.
  - Step 4: Direction. residual ≤ 1e-30 ⇒ quadrature-bounded (24+ OOM below identity-violation ceiling 1e-12); residual ≥ 1e-12 ⇒ identity-violating.
- **What PASS/FAIL MEAN**:
  - PASS = the W1b-1 1.292e-06 residual is a numerical-integration floor under trapezoidal n_quad=8192; the §VII.U Mellin-Dirichlet identity holds in the PV scheme at structural precision; HK-2 (windowed-PV-as-SD-refinement) is structurally validated.
  - FAIL = §VII.U identity is violated under PV; the W1b-1 PV recalibration uncovered a structural inconsistency in the PV scheme's Mellin-image; routes to convention-shopping investigation (which scheme reproduces §VII.U exactly).
  - INFO = quadrature still bounding; refine n_quad or method.
- **Effort**: 0.4 wave-equivalents.
- **Substrate framing**: D_K^2 IS the substrate's spectral content; ζ_D(s) IS a substrate-IS scalar moment; the heat-kernel trace IS the Mellin transform of the substrate's eigenvalue measure. The PV scheme is a regulator-class choice on the substrate's moment functional, NOT a continuum-limit cutoff IN spacetime.
- **Output artifacts**: `computations/s88_w11_pv_scheme_mpmath_mellin_dirichlet_verify.py`, `.npz` (residuals at s ∈ {3,4,5}), `.png` (residual vs s log-log), verdict line + dual-SHA companion row in `s88_gate_verdicts.txt`.

---

## §W11-122 — `S88-PS-AF-L12-RECALIBRATION`

- **Gate ID**: `S88-PS-AF-L12-RECALIBRATION`
- **Trigger**: `[VERIFY]`
- **Classification**: GEOMETRIC (substrate-spectral; PS A_F diagnostic at extended L_max)
- **Agent**: lizzi-spectral-functional-theorist (orchestrator); connes-ncg-theorist (CO; A_F axiom check)
- **Hypothesis**: The +0.50% upward shift in the W1b-5 PS A_F diagnostic at L_max=10 (n=0 sector) is either (a) a finite-L truncation artifact that REFINES toward 0 as L_max → 12 → 14 → … (substrate-asymptotic interpretation), or (b) a structural feature of the PS A_F that EXTENDS at L_max=12 (substrate-finite-L identity), or (c) VANISHES (truncation-artifact at L_max=10 only).
- **Method**: Re-run the W1b-5 6/6 Connes-Chamseddine 1996 axiom diagnostic at L_max=12 against `s84_spectrum_cache_L12_tau019.npz`. Compute the n=0-sector +Δ% shift at L_max=12 and compare to L_max=10 baseline (+0.50%). Three-way classification per envelope L^{-α} (α=3 from W-5 calibration corpus): predicted refinement Δ_12/Δ_10 = (10/12)^3 = 0.5787; if observed ratio ∈ [0.45, 0.70] then REFINE; if observed ratio ∈ [0.95, 1.05] then EXTEND; if observed ratio ∈ [-0.05, 0.05] then VANISH; otherwise INFO (intermediate).
- **Machinery pin**: spectrum cache `s84_spectrum_cache_L12_tau019.npz` SHA `9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9`; PS A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ); axiom set = Connes-Chamseddine 1996 §2.2-2.3 6 axioms (KO-dim=6, J-D_K=0, [J,D_K]=0, π·J·π=π, real structure, Poincaré duality); n_sector_target = 0; rel_tol on individual axiom = 1e-9.
- **4-tuple**: `(value=Delta_12_pct, scheme=PS-AF-finite-L=12, convention=CC1996-6-axioms-n=0-sector, L_max=12)`
- **Threshold**: PASS-REFINE iff Δ_12/Δ_10 ∈ [0.45, 0.70]; PASS-EXTEND iff ∈ [0.95, 1.05]; PASS-VANISH iff ∈ [-0.05, 0.05]; INFO otherwise; FAIL iff any of the 6 axioms returns rel_dev ≥ 1e-9 at L_max=12 (independent of the shift question).
- **Substitution chain (inside gate block)**:
  - Step 1: Definition. PS A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ); diagnostic Δ(L) = (Σ_axiom_lhs - Σ_axiom_rhs) / |Σ_axiom_rhs| at sector n=0.
  - Step 2: Substitution. Δ(L_max=12) is computed from the L=12 cache; Δ(L_max=10) = +0.50% is the W1b-5 anchor.
  - Step 3: Simplification under L^{-3} algebraic envelope (W-5 cross-pillar-bridge calibration corpus instance #1). Predicted Δ_12 / Δ_10 = (10/12)^3 = 0.5787 if REFINE, = 1 if EXTEND, = 0 if VANISH.
  - Step 4: Direction. Observed ratio interval determines class; class determines the W1b-5 reading.
- **What PASS/FAIL MEAN**:
  - PASS-REFINE = +0.50% is a finite-L truncation-floor; substrate-IS fully consistent with CC1996 axioms in continuum limit.
  - PASS-EXTEND = +0.50% is a substrate-finite-L structural feature; persists asymptotically; needs registry entry.
  - PASS-VANISH = +0.50% was a L=10 truncation-only artifact; structurally absent at L=12.
  - FAIL = some CC1996 axiom violates rel_dev ≥ 1e-9 at L=12 (independent of shift); routes to PS A_F redefinition.
- **Effort**: 0.5 wave-equivalents.
- **Substrate framing**: A_F IS the substrate's algebra of observables; CC1996 axioms ARE the algebraic-side structural constraints on the spectral triple `(A_F, H_F, D_F)`. The diagnostic shift Δ is a substrate-IS quantity, not a measurement IN any external geometric container.
- **Output artifacts**: `computations/s88_w11_ps_af_l12_recalibration.py`, `.npz` (per-axiom rel_dev at L=10, L=12; Δ_12, Δ_12/Δ_10), `.png` (Δ vs L_max), verdict line + dual-SHA companion row.

---

## §W11-123 — `S88-CONNES-DISTANCE-SUBALGEBRA-RESTRICTION-CONJECTURE`

- **Gate ID**: `S88-CONNES-DISTANCE-SUBALGEBRA-RESTRICTION-CONJECTURE`
- **Trigger**: `[VERIFY-THEOREM]`
- **Classification**: GEOMETRIC (substrate-spectral; Connes distance on substrate's actual A_F)
- **Agent**: gen-physicist (orchestrator); connes-ncg-theorist (CO; NCG-axiomatic structural derivation)
- **Hypothesis**: When the local algebra A_loc is restricted from full M_n(ℂ) to the substrate's actual A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ), the Connes distance d_C(ω_a, ω_b) := sup{|ω_a(a) - ω_b(a)| : a ∈ A_loc, ‖[D_K, a]‖ ≤ 1} becomes FINITE and WELL-DEFINED at finite L_max (against the W1b-6 CLASS-γ closure on full M_n(ℂ) where regulator-divergence at L=12 was the diagnosis), AND it matches the finite-spectrum identity expected from the algebra-axis-orthogonality K-counter (cross-pillar-bridge K=3 calibration corpus instance #3).
- **Method**: Pure state pair (ω_a, ω_b) := (rank-1 projector ω_e on the ℂ-summand idempotent, rank-1 projector ω_h on the ℍ-summand SU(2)-trace state). Compute d_C(ω_a, ω_b) on A_F via SDP relaxation (cvxpy + MOSEK or ECOS): max{|tr(ρ_e a) - tr(ρ_h a)| : a ∈ A_F^{sa}, ‖[D_K^{≤L}, π(a)]‖_{op} ≤ 1} where π : A_F → B(H_F) is the spectral-triple representation. Return d_C numerical value at L_max=10, L_max=12; PASS iff d_C is finite (< +∞) at both AND d_C(L=12)/d_C(L=10) ∈ [0.85, 1.15] (regulator-stability under L^{-3} algebraic envelope inflated by 5×); INFO if finite at L=10 but oscillates at L=12; FAIL iff d_C diverges (regulator-divergent like W1b-6 CLASS-γ on full M_n(ℂ)) or SDP infeasible.
- **Machinery pin**: SDP solver = ECOS (default) with MOSEK fallback; tolerances `eps_rel=1e-8, eps_abs=1e-10`; representation π built from `dirac_spectrum.get_irrep` for each Peter-Weyl block at L_max ≤ 12 per W11-2 D_K Block-Diagonality pre-check (math-scripts.md §"Machinery-Feasibility Audit"); state pair = (rank-1 idempotent on ℂ, rank-1 SU(2)-trace on ℍ); Lipschitz seminorm `‖[D_K, π(a)]‖_{op}` computed via spectral norm of finite block; A_F^{sa} parametrization via direct-sum basis (1 real + 4 real + 9 real = 14 real parameters).
- **4-tuple**: `(value=d_C, scheme=A_F-restricted-Connes-distance, convention=ECOS-SDP-A_F-direct-sum-14-params, L_max=12)`
- **Threshold**: PASS iff d_C finite at L=10 AND L=12 AND d_C(12)/d_C(10) ∈ [0.85, 1.15]; INFO if finite at L=10 but |d_C(12)/d_C(10) - 1| > 0.15; FAIL iff d_C → +∞ at either L (SDP unbounded) or solver infeasible.
- **Substitution chain (inside gate block)**:
  - Step 1: Definition. d_C(ω_a, ω_b) = sup{|ω_a(a) - ω_b(a)| : a ∈ A_loc, ‖[D_K, π(a)]‖ ≤ 1}. CLASS-γ at W1b-6 evaluated this with A_loc = full M_n(ℂ); diverged.
  - Step 2: Substitution. Restrict A_loc → A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ); the parameter space is finite-dimensional (14 real); the Lipschitz constraint becomes a finite-dimensional matrix inequality on each Peter-Weyl block.
  - Step 3: Simplification. SDP form: max c^T x subject to ‖A(x)‖_{op} ≤ 1 over x ∈ ℝ^14. Direction read: the algebra-axis-orthogonality K-counter (cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter") at K=3 MANDATORY structurally PREDICTS that A_F-restricted Connes distance has NO `{λ_n}`-only identity (it is algebra-DEPENDENT) — but it should still be FINITE on the finite-rank A_F substrate.
  - Step 4: Direction. d_C finite ⇒ A_F is the structurally correct domain for the Connes distance on the substrate; d_C divergent ⇒ even A_F is too rich and a further sub-algebra restriction is required.
- **What PASS/FAIL MEAN**:
  - PASS = the substrate's actual A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) is the structurally correct local algebra for the Connes distance; finite well-defined value matches algebra-axis-orthogonality structural prediction; W1b-6 CLASS-γ regulator-divergence is diagnosed as a full-M_n(ℂ)-only artifact.
  - FAIL = even A_F-restricted Connes distance diverges; algebra-axis-orthogonality K-counter requires further sub-algebra restriction (e.g., to BdG-restricted M_2(ℂ) per W-5 inheritance morphism).
  - INFO = finite at L=10, regulator-unstable at L=12; needs L=14 cache.
- **Effort**: 0.7 wave-equivalents (SDP build cost; per-block representation construction).
- **Substrate framing**: A_F IS the substrate's algebra; the Connes distance IS a substrate-IS metric on the substrate's state space (algebra-DEPENDENT family per the algebra-axis-orthogonality K-counter). The state pair (ω_a, ω_b) ARE pure states ON the substrate, not points IN any embedding metric space.
- **Output artifacts**: `computations/s88_w11_connes_distance_subalgebra_restriction.py`, `.npz` (d_C at L=10 + L=12; SDP dual variables; per-block Lipschitz norms), `.png` (d_C vs L_max), verdict line + dual-SHA companion row.

---

## §W11-124 — `S88-A-N-FW-CANONICALIZATION`

- **Gate ID**: `S88-A-N-FW-CANONICALIZATION`
- **Trigger**: `[VERIFY]` (canonical-write-order Step 2 promotion)
- **Classification**: METHODOLOGY (canonical_constants.py promotion per math-scripts.md §"Canonical Write-Order for New Framework Predictions" Step 2; allowlisted under methodology-wave-allowlist.md upon plan-freeze SHA computation)
- **Agent**: gen-physicist (orchestrator-direct-write per wave-classification.md §"Dispatch consequences" METHODOLOGY-class)
- **Hypothesis**: a_0_FW and a_2_FW (zeroth and second Seeley-DeWitt coefficients of D_K^2 at τ_fold) are framework-canonical observables that have been computed across S77 (a_0 R-protection) and S46 (a_2 split) but have not been promoted to `canonical_constants.py` with regulator-tagged provenance per `regulator-pin-discipline.md`.
- **Method**: For each of {a_0, a_2}, query `mcp__knowledge__.search_knowledge` and `trace_entity` to identify the substrate-first canonical numeric values + producing-script SHA + regulator-class. Add entries `a_0_FW_<regulator>` and `a_2_FW_<regulator>` for regulator ∈ {ζ, Pauli-Villars, Mellin} via `update_constant(name, value, session="S88", source="S88-W11-124", comment="...")`. Verify subsequent `from canonical_constants import a_0_FW_zeta, a_2_FW_zeta` succeeds. PASS iff all entries land + import test succeeds; FAIL iff a value is not derivable from a substrate-first source (PIN-PLACEHOLDER class-(f) per substrate-first-canonical-sourcing.md).
- **Machinery pin**: knowledge MCP server query targets {`a_0`, `a_0_FW`, `a_2`, `a_2_FW`, `Seeley-DeWitt`, `R-protection`, `a_2_split`}; canonical_constants.py write target = top-of-file alphabetical insertion + PROVENANCE block; regulator tagset = {ζ, Pauli-Villars, Mellin}; provenance comment template = `"S{N}-{GATE_ID}: {scheme}-regulated D_K^2 {coefficient} at τ_fold; substrate-first source: {script_path} SHA={sha}"`.
- **4-tuple**: `(value=count_of_promoted_constants, scheme=canonical_write_order_step2, convention=mcp-knowledge-MCP-query-substrate-first, L_max=10)`
- **Threshold**: PASS iff count_of_promoted_constants ∈ {2 (single regulator each), 6 (3 regulators × 2 coefficients)}; INFO iff partial promotion (1 ≤ count < target); FAIL iff any value is placeholder/OOM-only (class-(f) HARD-HALT).
- **Substitution chain (inside gate block)**:
  - Step 1: Definition. a_n^X = n-th Seeley-DeWitt coefficient under regulator X; a_n^X = Res[Tr(D_K^{−2s}); s = (d−n)/2] · m_n where m_n is the dimensional-spectrum multiplicity (Connes-Moscovici 1995 §III.4).
  - Step 2: Substitution. For each regulator X ∈ {ζ, Pauli-Villars, Mellin} and each n ∈ {0, 2}: query knowledge MCP for (value, source_script, sha, session); write `update_constant(f"a_{n}_FW_{X}", value, session="S88", source="S88-W11-124", comment=...)`.
  - Step 3: Simplification. Verify import: `python -c "from canonical_constants import a_0_FW_zeta, a_2_FW_zeta; print(a_0_FW_zeta, a_2_FW_zeta)"`.
  - Step 4: Direction. Successful import + 2-or-6 entries land ⇒ canonical-write-order Step 2 closure for {a_0, a_2} family; future computation scripts cite `a_0_FW_zeta` rather than re-deriving.
- **What PASS/FAIL MEAN**:
  - PASS = a_n_FW family canonically promoted; downstream gates (#125, #128-#131, #133) can `from canonical_constants import a_n_FW_<regulator>` instead of re-deriving; closes a class-(f) PIN-PLACEHOLDER risk for 2 framework headline observables.
  - FAIL = at least one of {a_0, a_2} has no substrate-first canonical source; routes to S88+ derivation gate.
  - INFO = partial; only ζ-tagged variants land (Pauli-Villars + Mellin queued for next session).
- **Effort**: 0.2 wave-equivalents.
- **Substrate framing**: a_n IS the n-th moment of the substrate's spectral measure; the regulator class IS a labeled choice on the substrate's moment-functional family, NOT a continuum-limit cutoff IN any metric container. Canonicalization preserves substrate-first sourcing.
- **Output artifacts**: edits to `computations/canonical_constants.py` (entries + PROVENANCE block); `computations/s88_w11_a_n_fw_canonicalization.py` (one-shot `update_constant` driver + import-verification block); verdict line + dual-SHA companion row.

---

## §W11-125 — `S88-A0-M2-BICONDITIONAL-RICHER-A_F-TOY`

- **Gate ID**: `S88-A0-M2-BICONDITIONAL-RICHER-A_F-TOY`
- **Trigger**: `[VERIFY-THEOREM]`
- **Classification**: GEOMETRIC (substrate-spectral; biconditional structural theorem on richer A_F)
- **Agent**: connes-ncg-theorist (orchestrator); gen-physicist (CO; toy-spectrum construction)
- **Hypothesis**: The W1a-5 §VII.W-2 biconditional FORWARD-only PASS reflects a kernel-degenerate escape: on A_F = ℂ ⊕ ℍ (the W1a-5 toy), the BACKWARD direction can be evaded via a nilpotent extension that satisfies the kernel condition without the L_max-stability premise. On a richer toy A_F = M_2(ℂ) where nilpotent extensions are structurally precluded (M_2(ℂ) has no non-trivial central nilpotents that respect the SO(3)-isospin grading), the BACKWARD direction should hold.
- **Method**: Construct toy spectral triple (A_F = M_2(ℂ), H_toy = ℂ^4 ⊗ ℂ^2, D_toy) with synthetic 4-eigenvalue spectrum {λ_1, λ_2, λ_3, λ_4} where (λ_1, λ_2) form a parity-twin and (λ_3, λ_4) form an asymmetric pair. Test the BACKWARD direction: a_0^ζ(D_toy) at the Mellin pole s=3 → does it imply L_max-stability of the M_2(ℂ) algebra? Compute via direct enumeration of M_2(ℂ) sub-algebras + Connes-Chamseddine 1996 §2.2 axiom verification per sub-algebra. PASS iff ∃ M_2(ℂ) sub-algebra restriction such that the BACKWARD direction holds (a_0 → L_max-stability) at residual ≤ 1e-12; FAIL iff every restriction violates BACKWARD; INFO iff multiple sub-algebras admit restriction (non-unique).
- **Machinery pin**: toy spectrum {λ_1, λ_2, λ_3, λ_4} = {1, -1, 1.5, -2}·M_KK (parity-twin + asymmetric pair); M_2(ℂ) sub-algebras enumerated = {ℂ·1, diagonal ℂ⊕ℂ, full M_2(ℂ)}; CC1996 axiom set = 6 axioms; rel_tol = 1e-12; regulator = ζ (default); Mellin pole s = 3.
- **4-tuple**: `(value=residual_BACKWARD, scheme=M2C-toy-biconditional-BACKWARD, convention=CC1996-6-axioms-Mellin-s=3, L_max=4)`
- **Threshold**: PASS iff residual_BACKWARD ≤ 1e-12 for at least one sub-algebra restriction AND the kernel-degenerate-escape is structurally PRECLUDED by enumeration; INFO iff residual ≤ 1e-9 but kernel-degenerate-escape exists in some sub-algebra; FAIL iff residual ≥ 1e-9 for ALL sub-algebras (BACKWARD direction structurally fails on M_2(ℂ)).
- **Substitution chain (inside gate block)**:
  - Step 1: Definition. §VII.W-2 biconditional: a_0^ζ(D) at s=3 ⇔ L_max-stability of A_F. FORWARD = (L_max-stability ⇒ a_0). BACKWARD = (a_0 ⇒ L_max-stability). W1a-5 closed FORWARD on A_F = ℂ ⊕ ℍ; BACKWARD deferred.
  - Step 2: Substitution. Replace A_F = ℂ ⊕ ℍ with A_F = M_2(ℂ); enumerate sub-algebras; on each, compute a_0^ζ at s=3 from the toy spectrum; check whether a_0 ≠ 0 implies the sub-algebra's Connes-Chamseddine 1996 6 axioms close at finite L_max=4.
  - Step 3: Simplification. M_2(ℂ) has 3 sub-algebra classes: trivial ℂ·1 (rank 1), diagonal ℂ⊕ℂ (rank 2), full M_2(ℂ) (rank 4). Nilpotent extensions in M_2(ℂ) are upper-triangular Jordan blocks; these structurally violate SO(3)-isospin grading (the M_2(ℂ) BdG-sector grading from W-5 inheritance morphism), so they are PRECLUDED.
  - Step 4: Direction. PASS ⇔ at least one sub-algebra restriction realizes BACKWARD without nilpotent escape. The structural exclusion of nilpotents in graded M_2(ℂ) is the key step; closure ⇒ BACKWARD holds; failure ⇒ BACKWARD genuinely fails on richer A_F.
- **What PASS/FAIL MEAN**:
  - PASS = §VII.W-2 biconditional holds in BOTH directions on richer A_F = M_2(ℂ); W1a-5 FORWARD-only result was kernel-degenerate-escape-bound; structurally cleaner reading promotes §VII.W-2 from STAGE-1-CANDIDATE to STAGE-3-PERMANENT pending Stage-2 cross-axis verify.
  - FAIL = even on M_2(ℂ), BACKWARD genuinely fails; the biconditional collapses to forward-implication-only; §VII.W-2 stays at STAGE-1-CANDIDATE indefinitely.
  - INFO = multiple sub-algebras admit restriction; BACKWARD holds non-uniquely; needs algebra-axis-orthogonality K-counter cross-reference.
- **Effort**: 0.5 wave-equivalents.
- **Substrate framing**: A_F IS the substrate's finite algebra; M_2(ℂ) is the BdG-sector child under the W-5 inheritance morphism χ : ℂ ⊕ ℍ ⊕ M_3(ℂ) → M_2(ℂ); the toy spectrum IS a substrate-IS finite spectral content, NOT a synthetic geometry IN any container.
- **Output artifacts**: `computations/s88_w11_a0_m2_biconditional_richer_af_toy.py`, `.npz` (per-sub-algebra residual + nilpotent-precluded flag), `.png` (residual_BACKWARD vs sub-algebra rank), verdict line + dual-SHA companion row.

---

## §W11-126 — `S88-MELLIN-CONE-NO-GO-FULL-LMAX10-RETEST`

- **Gate ID**: `S88-MELLIN-CONE-NO-GO-FULL-LMAX10-RETEST`
- **Trigger**: `[VERIFY-THEOREM]`
- **Classification**: GEOMETRIC (substrate-spectral; Mellin-cone no-go theorem at full spectrum)
- **Agent**: lizzi-spectral-functional-theorist (orchestrator); gen-physicist (CO; full-spectrum cache loader)
- **Hypothesis**: The W1a-2 Mellin-cone no-go theorem — that no finite-rank algebra A satisfies the Connes-Chamseddine 1996 §III.4 dim-spectrum residue formula on the L=10 D_K^2 spectrum's Mellin-cone — was demonstrated on a 4-eigenvalue synthetic toy (CM-1995 §III.4 inadmissibility). The full L=10 D_K^2 spectrum (155,984 eigenvalues) has a richer Mellin-cone with potentially more poles that could either CONFIRM the no-go theorem (substrate-extension PASS) or expose a SURVIVING admissible region (substrate-falsification FAIL).
- **Method**: Load `s84_spectrum_cache_L10_tau019.npz` (155,984 eigenvalues at τ_fold=0.190); compute Mellin transform `ζ_D(s) = Σ_n m_n λ_n^{-s}` numerically via `mpmath.zeta`-style accelerated summation at s ∈ {3, 4, 5, 6, 7} (the 5 substrate-distance poles s=3..7); identify residues; test CM-1995 §III.4 inadmissibility predicate at each pole. PASS iff predicate holds at every pole (no-go extends from 4-eigvalue toy to 155,984-eigvalue full spectrum); INFO iff holds at 3-4 poles but borderline at 1; FAIL iff predicate fails at any pole (admissible region surfaces).
- **Machinery pin**: spectrum cache `s84_spectrum_cache_L10_tau019.npz` (full 155,984 eigvals); Mellin pole set s ∈ {3, 4, 5, 6, 7}; CM-1995 §III.4 inadmissibility predicate = `Res[ζ_D(s); s=s_*] · Γ(s_*) does not equal Σ_a m_a · λ_a^{−s_*}` for any finite-rank A; rel_tol_predicate = 1e-9; mpmath precision dps=30; pole-wise residue computed via Cauchy-contour numerical integration with adaptive radius ∈ [0.001, 0.1].
- **4-tuple**: `(value=poles_passing_no_go, scheme=full-Lmax10-Mellin-cone-CM1995, convention=mpmath-30dp-Cauchy-contour, L_max=10)`
- **Threshold**: PASS iff poles_passing_no_go = 5 (all 5 poles s ∈ {3,4,5,6,7} satisfy CM-1995 inadmissibility); INFO iff poles_passing_no_go = 4 (one borderline); FAIL iff poles_passing_no_go ≤ 3.
- **Substitution chain (inside gate block)**:
  - Step 1: Definition. CM-1995 §III.4 inadmissibility: a finite-rank A admissible iff ∃ {m_a, λ_a} such that Res[ζ_D(s); s=s_*] · Γ(s_*) = Σ_a m_a · λ_a^{−s_*} simultaneously at all dim-spectrum poles s_*.
  - Step 2: Substitution. Replace 4-eigvalue toy spectrum with full L_max=10 D_K^2 spectrum (155,984 eigvals at τ_fold=0.190); compute Res[ζ_D(s); s=s_*] numerically at each s_* ∈ {3,4,5,6,7}.
  - Step 3: Simplification. Rich-spectrum Mellin transform admits more poles ⇒ more constraints ⇒ no-go theorem either EXTENDS (more constraints, no surviving A) or FAILS (an A satisfying all constraints emerges as a surprise).
  - Step 4: Direction. poles_passing_no_go = 5 ⇒ no-go extends; ≤ 3 ⇒ admissible region surfaces.
- **What PASS/FAIL MEAN**:
  - PASS = no-go theorem structurally extends from 4-eigvalue toy to full L=10 spectrum; the CM-1995 §III.4 inadmissibility is robust across the Mellin-cone substrate-distance axis; closes a HK-1 carry-forward.
  - FAIL = an admissible finite-rank A surfaces in the full spectrum that did not appear in the toy; surprise structural result; routes to characterization of the surviving A.
  - INFO = borderline at one pole; needs L=12 retest.
- **Effort**: 0.6 wave-equivalents.
- **Substrate framing**: ζ_D(s) IS the substrate's Mellin moment functional; the dim-spectrum poles ARE substrate-IS structural invariants; the no-go theorem is a constraint on the substrate's algebra of observables, NOT a property derived from any external compactification limit.
- **Output artifacts**: `computations/s88_w11_mellin_cone_no_go_full_lmax10_retest.py`, `.npz` (per-pole residue + predicate result), `.png` (poles s vs residue overlay with CM-1995 predicate band), verdict line + dual-SHA companion row.

---

## §W11-127 — `S88-CM-1995-CUTOFF-SQRT-ATLAS-CROSS-CHECK`

- **Gate ID**: `S88-CM-1995-CUTOFF-SQRT-ATLAS-CROSS-CHECK`
- **Trigger**: `[VERIFY]`
- **Classification**: GEOMETRIC (substrate-spectral; Corollary A vs cutoff_sqrt atlas)
- **Agent**: connes-ncg-theorist (orchestrator); gen-physicist (CO; atlas reading)
- **Hypothesis**: The W1a-2 Corollary A (CM-1995 §III.4 inadmissibility extended to cutoff-sqrt regulator class) classifies each entry of the W-8 cutoff_sqrt atlas as either RESPECTING the no-go (PASS) or VIOLATING it (FAIL). The atlas of cutoff_sqrt extremal pair-ratios at A_5 (pre-S87 W8-2 cascade A_5 → A_4) contains entries at distinct (regulator, scheme, L_max) tuples; each must be classified.
- **Method**: Read W-8 cutoff_sqrt atlas entries from `sessions/permanent-results-registry.md §VII.K-PROP` and W-8 results working-paper. For each entry's `(regulator, scheme, L_max, max_pair_ratio)` tuple, evaluate whether CM-1995 §III.4 inadmissibility predicate holds at the entry's regulator class (Corollary A); classify PASS (respects no-go) or FAIL (violates). Aggregate count.
- **Machinery pin**: W-8 atlas source = `sessions/permanent-results-registry.md §VII.K-PROP` + `sessions/archive/session-87/session-87-results-workingpaper.md §W8-2`; atlas entry tuple schema = `(regulator, scheme, L_max, max_pair_ratio)`; Corollary A predicate = `(cutoff-sqrt regulator preserves CM-1995 §III.4 admissibility iff max_pair_ratio ∉ kernel-degenerate-band)`; kernel-degenerate-band per W-8 = `[1.0, 1.001]` (extremal-cutoff edge); rel_tol on band = 1e-6.
- **4-tuple**: `(value=PASS_count_over_total, scheme=cutoff-sqrt-atlas-Corollary-A, convention=W8-2-atlas-reading, L_max=variable)`
- **Threshold**: PASS iff PASS_count == total atlas entries; INFO iff PASS_count ∈ [total-2, total-1]; FAIL iff PASS_count < total-2.
- **Substitution chain (inside gate block)**:
  - Step 1: Definition. Corollary A: a cutoff-sqrt regulator preserves CM-1995 §III.4 admissibility iff the regulator's induced extremal pair-ratio max_pair_ratio is OUTSIDE the kernel-degenerate-band [1.0, 1.001]. Kernel-degenerate-band = the band where the regulator's induced cutoff sends two distinct eigenvalues to a degenerate pair, breaking dim-spectrum residue assignability.
  - Step 2: Substitution. For each atlas entry (r, s, L, m): check if m ∉ [1.0, 1.001]; classify PASS if outside, FAIL if inside.
  - Step 3: Simplification. Aggregate PASS_count over all entries.
  - Step 4: Direction. PASS_count = total ⇒ Corollary A is empirically robust against the W-8 atlas; PASS_count < total-2 ⇒ Corollary A admits exceptions in the atlas.
- **What PASS/FAIL MEAN**:
  - PASS = Corollary A is empirically robust across the cutoff_sqrt atlas; W1a-2 CM-1995 inadmissibility extends consistently.
  - FAIL = exceptions surface in atlas; routes to characterizing the exceptional regulator-class.
  - INFO = 1-2 borderline entries; needs L=12 atlas extension.
- **Effort**: 0.3 wave-equivalents.
- **Substrate framing**: cutoff_sqrt IS a regulator-class label on the substrate's moment functional; max_pair_ratio IS a substrate-IS extremal observable; Corollary A IS a structural constraint on which regulators preserve dim-spectrum residue assignability.
- **Output artifacts**: `computations/s88_w11_cm1995_cutoff_sqrt_atlas_cross_check.py`, `.npz` (per-entry classification table), `.png` (atlas scatter colored by PASS/FAIL), verdict line + dual-SHA companion row.

---

## §W11-128 — `S88-LAMBDA-SA-S46-A2-SPLIT-SUCCESSOR-EMISSION`

- **Gate ID**: `S88-LAMBDA-SA-S46-A2-SPLIT-SUCCESSOR-EMISSION`
- **Trigger**: `[AUDIT]`
- **Classification**: METHODOLOGY (verdict-line emission for §VII.X.2 NECESSITY anchor; allowlisted under methodology-wave-allowlist.md upon plan-freeze SHA computation)
- **Agent**: gen-physicist (orchestrator-direct-write per wave-classification.md §"Dispatch consequences")
- **Hypothesis**: The S46 a_2 split structural anchor (one of 6 NECESSITY anchors required for §VII.X.2 STAGE-1 → STAGE-3 promotion per `joint-theorem-promotion.md`) was historically computed but never re-emitted as a computation verdict line with full-64-char audit_sha256. Re-emission produces the canonical anchor-SHA needed by #133.
- **Method**: Locate S46 a_2 split source in `sessions/archive/session-46/` and `computations/`; identify the canonical numerical value(s); construct an `script-template.py append_verdict()` invocation that reproduces the value from the archived inputs (via `closure_hash(input_pin_map)`); emit verdict line `S88-LAMBDA-SA-S46-A2-SPLIT-SUCCESSOR-EMISSION: PASS|INFO -- value=<S46_a2_split_value> scheme=Lambda-SA-S46-historical convention=a2-split-direct-emission L_max=<S46_L_max> sha256=<64-hex>` plus dual-SHA companion row. PASS iff S46 archive yields a unique numerical anchor + emission succeeds; INFO iff anchor is multi-valued (then emit each as separate row); FAIL iff archive cannot resolve canonical value.
- **Machinery pin**: S46 archive search target = `sessions/archive/session-46/session-46-final.md` + `computations/s46_*` files; emission template = `computations/script-template.py append_verdict()` (atomic single-line append; NEVER truncate-and-rewrite); audit_sha256 computed from `closure_hash(input_pin_map)` where input_pin_map enumerates {S46 source files, regulator tag, L_max}; content_sha256 over the canonical line text.
- **4-tuple**: `(value=S46_a2_split_value, scheme=Lambda-SA-S46-historical, convention=a2-split-direct-emission, L_max=<S46>)`
- **Threshold**: PASS iff archive resolves to single canonical value + verdict line lands with unique audit_sha256; INFO iff multi-valued; FAIL iff archive ambiguous.
- **Substitution chain (inside gate block)**:
  - Step 1: Definition. Λ_SA = spectral-action structural anchor family. S46 a_2 split is one anchor: the second Seeley-DeWitt coefficient a_2 = a_2^bulk + a_2^split where a_2^split is the substrate's chirality-induced split contribution.
  - Step 2: Substitution. Locate S46 source; extract (a_2^bulk, a_2^split); construct input_pin_map = {S46 source SHA, regulator tag, L_max=archive value}; compute audit_sha256 = closure_hash(input_pin_map).
  - Step 3: Simplification. Verdict line built from template + dual-SHA companion row.
  - Step 4: Direction. Successful emission ⇒ S46 anchor canonically computation-available with full-64-hex SHA; supplies anchor 1/6 to #133.
- **What PASS/FAIL MEAN**:
  - PASS = S46 a_2 split is now computation-emitted; one of 6 anchors needed by §VII.X.2 NECESSITY STAGE-3 promotion.
  - FAIL = archive ambiguous; need archaeology dispatch to resolve.
  - INFO = multi-valued; each value emitted separately.
- **Effort**: 0.2 wave-equivalents.
- **Substrate framing**: a_2 IS the substrate's second moment; the split a_2^split IS a substrate-IS chirality-induced contribution arising from KO-dim=6 grading; not a derived consequence of any external compactification.
- **Output artifacts**: `computations/s88_w11_lambda_sa_s46_a2_split_successor_emission.py`, verdict line + dual-SHA companion row.

---

## §W11-129 — `S88-LAMBDA-SA-S64-FINITE-L-COMPONENT-SUCCESSOR-EMISSION`

- **Gate ID**: `S88-LAMBDA-SA-S64-FINITE-L-COMPONENT-SUCCESSOR-EMISSION`
- **Trigger**: `[AUDIT]`
- **Classification**: METHODOLOGY (verdict-line emission for §VII.X.2 NECESSITY anchor; allowlisted upon SHA computation)
- **Agent**: gen-physicist (orchestrator-direct-write)
- **Hypothesis**: The S64 finite-L component structural anchor (anchor 2/6 for §VII.X.2 NECESSITY) requires direct computation re-emission with full-64-char audit_sha256 per the same protocol as #128.
- **Method**: Same as #128 but for S64 finite-L component. Locate `sessions/archive/session-64/` source; identify canonical numerical value; emit verdict line via `append_verdict()` template; produce dual-SHA companion row.
- **Machinery pin**: S64 archive search target = `sessions/archive/session-64/session-64-final.md` + `computations/s64_*`; same emission template + SHA protocol as #128.
- **4-tuple**: `(value=S64_finite_L_component_value, scheme=Lambda-SA-S64-historical, convention=finite-L-component-direct-emission, L_max=<S64>)`
- **Threshold**: PASS / INFO / FAIL same protocol as #128.
- **Substitution chain**: Same template as #128 with substitution S46 → S64; the finite-L component is the contribution to a_n at finite L_max truncation that vanishes in continuum limit.
- **What PASS/FAIL MEAN**: PASS = anchor 2/6 computation-available; FAIL = archive ambiguous; INFO = multi-valued.
- **Effort**: 0.2 wave-equivalents.
- **Substrate framing**: finite-L component IS the substrate's truncation-dependent moment piece; the L → ∞ limit is the substrate's own continuum image, not a container-spacetime limit.
- **Output artifacts**: `computations/s88_w11_lambda_sa_s64_finite_l_component_successor_emission.py`, verdict line + dual-SHA companion row.

---

## §W11-130 — `S88-LAMBDA-SA-S65-CONTINUUM-CONVERSE-WITNESS-EMISSION`

- **Gate ID**: `S88-LAMBDA-SA-S65-CONTINUUM-CONVERSE-WITNESS-EMISSION`
- **Trigger**: `[AUDIT]`
- **Classification**: METHODOLOGY (verdict-line emission for §VII.X.2 NECESSITY anchor; allowlisted upon SHA computation)
- **Agent**: gen-physicist (orchestrator-direct-write)
- **Hypothesis**: The S65 a_0/a_2 = ℂ/ℝ continuum (converse-failure witness; anchor 3/6 for §VII.X.2 NECESSITY) requires direct computation re-emission. The S65 result is a CONVERSE-FAILURE witness: in the continuum limit, the ratio a_0/a_2 takes value in ℂ/ℝ (i.e., genuinely complex, not real), demonstrating that the converse direction of NECESSITY structurally fails in continuum.
- **Method**: Same protocol as #128/#129. Locate `sessions/archive/session-65/`; identify a_0/a_2 ratio; emit verdict line.
- **Machinery pin**: S65 archive search target = `sessions/archive/session-65/session-65-final.md` + `computations/s65_*`; the witness requires emitting BOTH the real and imaginary parts of a_0/a_2 if complex.
- **4-tuple**: `(value=S65_a0_over_a2_ratio, scheme=Lambda-SA-S65-historical, convention=continuum-converse-witness-direct-emission, L_max=∞)`
- **Threshold**: PASS / INFO / FAIL per #128 protocol; complex-valued ratio counts as PASS provided value is canonical.
- **Substitution chain**: Same template; the converse-witness is the substrate's own continuum-limit observation that the converse direction of §VII.X.2 NECESSITY structurally FAILS (a non-real ratio cannot be derived from a real algebra-axis identity).
- **What PASS/FAIL MEAN**: PASS = anchor 3/6 computation-available + converse-failure structurally documented; FAIL = archive ambiguous.
- **Effort**: 0.2 wave-equivalents.
- **Substrate framing**: a_0/a_2 IS a substrate-IS dimensionless moment ratio; its complex value at continuum limit IS a substrate observable, not a result OF any external geometric framework.
- **Output artifacts**: `computations/s88_w11_lambda_sa_s65_continuum_converse_witness_emission.py`, verdict line + dual-SHA companion row.

---

## §W11-131 — `S88-LAMBDA-SA-S77-A0-R-PROTECTION-SUCCESSOR-EMISSION`

- **Gate ID**: `S88-LAMBDA-SA-S77-A0-R-PROTECTION-SUCCESSOR-EMISSION`
- **Trigger**: `[AUDIT]`
- **Classification**: METHODOLOGY (verdict-line emission for §VII.X.2 NECESSITY anchor; partial-match upgrade)
- **Agent**: gen-physicist (orchestrator-direct-write)
- **Hypothesis**: The S77 a_0 R-protection successor (anchor 4/6 for §VII.X.2 NECESSITY) is ALREADY computation-emitted under a partial-match name; this gate UPGRADES the partial match to a direct re-emission with the canonical anchor-id needed by #133.
- **Method**: Identify the S77 partial-match verdict line in `computations/s77_gate_verdicts.txt` or earlier session verdict files via `grep "a_0_R_protection" computations/s*_gate_verdicts.txt`; verify the canonical numerical value matches the §VII.X.2 anchor expectation; re-emit under the canonical anchor-id `S88-LAMBDA-SA-S77-A0-R-PROTECTION-SUCCESSOR-EMISSION` with the original `audit_sha256` preserved (not recomputed; the partial-match SHA is the structural anchor).
- **Machinery pin**: S77 verdict-file search via knowledge MCP + grep; canonical anchor-id resolution from §VII.X.2 NECESSITY table; emission preserves S77 audit_sha256 and content_sha256 (re-emission rule: when upgrading a partial-match anchor, the SHAs of the original are preserved as dual-SHA pin source).
- **4-tuple**: `(value=S77_a0_R_protection_value, scheme=Lambda-SA-S77-R-protection, convention=partial-match-upgrade-preserve-SHAs, L_max=<S77>)`
- **Threshold**: PASS iff S77 verdict found + canonical value matches §VII.X.2 expectation + re-emission preserves SHAs; INFO iff value matches but SHAs cannot be preserved (regenerate); FAIL iff value mismatch.
- **Substitution chain**: Definition: a_0 R-protection = the R-protection of the zeroth Seeley-DeWitt coefficient under the substrate's reflection R. S77 demonstrated structural protection under R-grading. Substitution: locate S77 verdict; verify match; emit. Direction: PASS ⇒ anchor 4/6 canonically available with preserved SHAs.
- **What PASS/FAIL MEAN**: PASS = anchor 4/6 canonically computation with preserved provenance; FAIL = S77 value mismatch; INFO = SHA regeneration required.
- **Effort**: 0.2 wave-equivalents.
- **Substrate framing**: R-protection IS a substrate-IS structural symmetry on the moment a_0; not derived from external reflection geometry.
- **Output artifacts**: `computations/s88_w11_lambda_sa_s77_a0_r_protection_successor_emission.py`, verdict line + dual-SHA companion row (with preserved S77 SHAs).

---

## §W11-132 — `S88-LAMBDA-SA-C9-S86-W1-RATIO-EMISSION`

- **Gate ID**: `S88-LAMBDA-SA-C9-S86-W1-RATIO-EMISSION`
- **Trigger**: `[AUDIT]`
- **Classification**: METHODOLOGY (verdict-line emission for §VII.X.2 NECESSITY anchor; allowlisted upon SHA computation)
- **Agent**: gen-physicist (orchestrator-direct-write)
- **Hypothesis**: The S86 W-1 workshop intermediate C9 ratio (anchor 5/6 for §VII.X.2 NECESSITY) is documented in `sessions/archive/session-86/workshops/` but never computation-emitted as a verdict line.
- **Method**: Locate S86 W-1 workshop file in `sessions/archive/session-86/workshops/`; extract C9 ratio canonical value; emit per #128 protocol.
- **Machinery pin**: S86 W-1 workshop search target = `sessions/archive/session-86/workshops/s86-mellin-dirichlet-identity-workshop.md` (or similar); C9 ratio extraction; emission template same as #128.
- **4-tuple**: `(value=S86_W1_C9_ratio, scheme=Lambda-SA-S86-W1-workshop, convention=C9-ratio-direct-emission, L_max=<S86-W1>)`
- **Threshold**: PASS / INFO / FAIL per #128 protocol.
- **Substitution chain**: Definition: C9 = workshop intermediate ratio between a_n^ζ and a_n^Gilkey at substrate-distance pole s=3 (or similar; resolve from workshop). Substitution: locate W-1 source; extract C9 value; emit. Direction: PASS ⇒ anchor 5/6 canonically available.
- **What PASS/FAIL MEAN**: PASS = anchor 5/6 canonically computation; FAIL = workshop ambiguous; INFO = multi-valued.
- **Effort**: 0.2 wave-equivalents.
- **Substrate framing**: C9 ratio IS a substrate-IS dimensionless ratio between regulator-class moment images; not a measurement IN any container.
- **Output artifacts**: `computations/s88_w11_lambda_sa_c9_s86_w1_ratio_emission.py`, verdict line + dual-SHA companion row.

---

## §W11-133 — `S88-VII-X-2-NECESSITY-PROMOTE-STAGE-3`

- **Gate ID**: `S88-VII-X-2-NECESSITY-PROMOTE-STAGE-3`
- **Trigger**: `[VERIFY-THEOREM]`
- **Classification**: METHODOLOGY (joint-theorem-promotion.md 4-stage Stage-3 promotion; allowlisted upon plan-freeze SHA computation)
- **Agent**: gen-physicist (orchestrator); connes-ncg-theorist (CO; cross-axis Stage-2 verifier — spectral-functional axis); lizzi-spectral-functional-theorist (CO; cross-axis Stage-2 verifier — NCG-axiomatic axis)
- **Hypothesis**: Once 6/6 NECESSITY anchors are computation-available with full-64-char audit_sha256 (anchors from #128, #129, #130, #131, #132, plus the 6th anchor enumerated below), the §VII.X.2 NECESSITY STAGE-1-CANDIDATE registered at S87 W1a-6 satisfies the Stage-2 cross-axis independent-verify gate of `joint-theorem-promotion.md` and PROMOTES to STAGE-3-PERMANENT.
- **Method**: 
  - (a) Verify all 6 anchor SHAs are present in `s88_gate_verdicts.txt` (anchors 1-5 from #128-#132; anchor 6 = the W1a-6-original NECESSITY anchor whose SHA is already computation).
  - (b) Dispatch TWO INDEPENDENT cross-reviewers PER `joint-theorem-promotion.md` Stage-2 protocol — connes-ncg-theorist on the spectral-functional axis (audits clauses derived from algebra-axis-orthogonality K-counter) and lizzi-spectral-functional-theorist on the NCG-axiomatic axis (audits clauses derived from CC1996 6-axiom structure). Both cross-reviewers operate WITHOUT prior workshop context: receive ONLY the registered §VII.X.2 STAGE-1-CANDIDATE entry text + the 6 anchor verdict lines.
  - (c) JOINT clauses (those requiring evidence from both axes) are PASS-AND'd across the two independent verdicts.
  - (d) Promotion: if Stage-2 PASS lands, edit `sessions/permanent-results-registry.md §VII.X.2` to replace `STAGE-1-CANDIDATE` tag with `STAGE-3-PERMANENT`.
- **Machinery pin**: anchor SHA enumeration set = {S46_a2_split_SHA, S64_finite_L_SHA, S65_continuum_SHA, S77_a0_R_SHA, S86_W1_C9_SHA, S87_W1a_6_original_SHA}; Stage-2 cross-reviewer protocol per `joint-theorem-promotion.md`; Stage-2 audit script = `computations/_joint_theorem_independent_verify_audit.py` (REFUSES single-agent firings on joint clauses); registry-edit target = `sessions/permanent-results-registry.md §VII.X.2`.
- **4-tuple**: `(value=Stage_2_PASS_AND, scheme=joint-theorem-promotion-4-stage, convention=2-cross-reviewer-different-axis-no-workshop-context, L_max=10)`
- **Threshold**: PASS iff (i) all 6 anchor SHAs present in s88 verdict file, AND (ii) connes Stage-2 cross-review returns PASS on its axis-A clauses + JOINT clauses, AND (iii) lizzi Stage-2 cross-review returns PASS on its axis-B clauses + JOINT clauses, AND (iv) JOINT clauses logical-AND across both verdicts. INFO iff (i) holds but Stage-2 returns INFO on any clause. FAIL iff (i) fails (any anchor missing) OR Stage-2 returns FAIL on any clause.
- **Substitution chain (inside gate block)**:
  - Step 1: Definition. `joint-theorem-promotion.md` Stage-2 = TWO independent cross-reviewers on DIFFERENT axes, dispatched in parallel, WITHOUT prior workshop context, JOINT clauses PASS-AND'd. Stage-3 = registry tag flipped from STAGE-1-CANDIDATE to STAGE-3-PERMANENT.
  - Step 2: Substitution. Pre-condition: 6/6 anchor SHAs available. Cross-reviewer A = connes (spectral-functional axis); cross-reviewer B = lizzi (NCG-axiomatic axis). Both dispatched in parallel; both receive only registered entry + 6 anchor verdict lines.
  - Step 3: Simplification. Logical-AND: Stage_2_PASS = (connes_PASS AND lizzi_PASS AND JOINT_clauses_PASS_in_both).
  - Step 4: Direction. Stage_2_PASS ⇒ orchestrator edits registry tag → STAGE-3-PERMANENT. Stage_2_FAIL ⇒ entry stays at STAGE-1-CANDIDATE; FAILing clauses route to next-session remediation.
- **What PASS/FAIL MEAN**:
  - PASS = §VII.X.2 NECESSITY structurally promoted to permanent; algebra-axis-orthogonality K-counter advances; framework gains a permanent structural theorem.
  - FAIL = either anchor incomplete or Stage-2 fails; entry stays at STAGE-1-CANDIDATE; remediation queued.
  - INFO = anchors complete but Stage-2 returns INFO on at least one clause; partial promotion deferred to S89.
- **Effort**: 1.0 wave-equivalents (2 parallel cross-reviewer dispatches + registry-edit).
- **Substrate framing**: §VII.X.2 NECESSITY IS a substrate-IS structural identity on the algebra-axis-orthogonality K-counter (cross-pillar-bridge-anatomy.md); the joint-theorem-promotion 4-stage pathway IS the framework's mechanism for converting workshop-internal candidates into permanent structural theorems via independent cross-axis verification (which is structurally NOT shared-context agreement per epistemic-discipline.md §"What Does NOT Count as Evidence" item 2).
- **Output artifacts**: `computations/s88_w11_vii_x_2_necessity_promote_stage_3.py` (orchestrator script that verifies anchor presence + dispatches cross-reviewers + edits registry); two cross-reviewer working-paper sections (one connes, one lizzi); verdict line + dual-SHA companion row; edit to `sessions/permanent-results-registry.md §VII.X.2` flipping STAGE-1-CANDIDATE → STAGE-3-PERMANENT.

---

## §W11-134 — `S88-WINDOWED-PV-SUBTRACTION-AS-SD-REFINEMENT`

- **Gate ID**: `S88-WINDOWED-PV-SUBTRACTION-AS-SD-REFINEMENT`
- **Trigger**: `[CLOSED-IN-SESSION]`
- **Classification**: CLOSED-IN-SESSION (documented only; no compute)
- **Agent**: gen-physicist (documentation only)
- **Hypothesis**: HK-2 (windowed-PV subtraction as SD-refinement) is closed in-session via the W1b-1 PV recalibration result; the windowed-PV subtraction is structurally a Seeley-DeWitt scheme refinement (NOT a distinct regulator class), and the W1b-1 1.292e-06 residual is quadrature-bounded (validated by #121 mpmath retest if PASS).
- **Method**: Documentation only. No computation script. The W11-134 entry is a registry-pointer row in `sessions/permanent-results-registry.md §VII.K-PROP` (or successor) that cross-links W1b-1 PV recalibration verdict + W11-121 mpmath verification to the HK-2 closure claim. Per `mechanical-closure-discipline.md`, the documentation-only closure is acceptable iff the closing rule is pre-registered AND the cross-links are present.
- **Machinery pin**: registry-pointer target = `sessions/permanent-results-registry.md §VII.K-PROP-HK-2-WINDOWED-PV-AS-SD-REFINEMENT`; cross-link sources = {W1b-1 PV recalibration verdict, W11-121 mpmath verification verdict}; documentation-only flag set.
- **4-tuple**: `(value=DOCUMENTATION-ONLY, scheme=closed-in-session, convention=registry-pointer, L_max=N/A)`
- **Threshold**: PASS iff registry-pointer row written + cross-links to W1b-1 + W11-121 verdicts present; FAIL iff cross-links missing.
- **Substitution chain**: Definition: HK-2 = windowed-PV subtraction. Substitution: identify HK-2 as SD-refinement (not new regulator class). Direction: PASS ⇒ HK-2 cleared as a documentation-only registry pointer; W11-121 PASS validates the W1b-1 quadrature-bound reading.
- **What PASS/FAIL MEAN**: PASS = HK-2 documented closed; FAIL = registry pointer not landed.
- **Effort**: 0.05 wave-equivalents (registry edit only).
- **Substrate framing**: windowed-PV IS a refinement of the SD scheme on the substrate's moment functional, NOT a distinct regulator class; the substrate's moment family is preserved.
- **Output artifacts**: registry-pointer row in `sessions/permanent-results-registry.md §VII.K-PROP-HK-2`; verdict line `S88-WINDOWED-PV-SUBTRACTION-AS-SD-REFINEMENT: PASS -- value=DOCUMENTATION-ONLY ...` + dual-SHA companion row.

---

## Wave 11 → Wave 12 Decision Point

| Outcome | Routing |
|:--------|:--------|
| #121 PASS + #122 PASS-REFINE/EXTEND/VANISH + #133 PASS | Wave 12 leads with §VII.X.2 STAGE-3 downstream consumers + W1b housekeeping closed |
| #121 FAIL | Wave 12 W12-1 leads with PV-scheme structural-identity remediation; #133 deferred |
| #133 FAIL on anchor incompleteness | Wave 12 W12-1 leads with anchor archaeology dispatch (S46/S64/S65 source resolution) |
| #133 FAIL on Stage-2 cross-review | Wave 12 W12-1 leads with FAILing-clause remediation per `joint-theorem-promotion.md` |
| #123 FAIL (A_F-restricted Connes distance diverges) | Wave 12 W12-1 leads with further sub-algebra restriction (BdG-restricted M_2(ℂ) per W-5 inheritance morphism) |
| #126 FAIL (admissible region surfaces in full L=10 spectrum) | Wave 12 W12-1 leads with characterization of surviving admissible algebra |

## Wave 11 Machinery-Enumeration Pin (§0.11)

| Gate | Free parameters | Pin source |
|:-----|:----------------|:-----------|
| #121 | mp.dps=50; mpmath.quad method=tanh-sinh, maxdegree=15; s_test=[3,4,5]; M_PV=10·M_KK | This plan §W11-121 machinery pin |
| #122 | spectrum cache L=12 SHA; CC1996 6 axioms; n_sector=0; rel_tol=1e-9 | This plan §W11-122 machinery pin |
| #123 | SDP solver=ECOS+MOSEK; eps_rel=1e-8; eps_abs=1e-10; A_F=ℂ⊕ℍ⊕M_3(ℂ) 14-real-param parametrization; state pair (rank-1 ℂ idempotent, rank-1 SU(2)-trace) | This plan §W11-123 machinery pin |
| #124 | knowledge MCP query targets; canonical_constants.py write target = top-of-file alphabetical insertion + PROVENANCE block; regulator tagset {ζ, Pauli-Villars, Mellin} | This plan §W11-124 machinery pin |
| #125 | toy spectrum {1, -1, 1.5, -2}·M_KK; M_2(ℂ) sub-algebra set {ℂ·1, ℂ⊕ℂ, M_2(ℂ)}; CC1996 6 axioms; rel_tol=1e-12; Mellin pole s=3 | This plan §W11-125 machinery pin |
| #126 | spectrum cache L=10 SHA; pole set {3,4,5,6,7}; CM-1995 §III.4 inadmissibility predicate; mpmath dps=30; Cauchy-contour radius ∈ [0.001, 0.1] | This plan §W11-126 machinery pin |
| #127 | W-8 atlas source SHA; entry tuple schema; kernel-degenerate-band [1.0, 1.001]; rel_tol=1e-6 | This plan §W11-127 machinery pin |
| #128-#132 | per-anchor archive search target; emission template = `script-template.py append_verdict()`; SHA preservation rule for #131 only | Each gate's machinery pin |
| #133 | 6 anchor SHA enumeration set; Stage-2 cross-reviewer protocol; cross-reviewer assignments (connes spectral-functional, lizzi NCG-axiomatic); audit script `_joint_theorem_independent_verify_audit.py` | This plan §W11-133 machinery pin |
| #134 | registry-pointer target; cross-link sources; documentation-only flag | This plan §W11-134 machinery pin |

## Wave 11 Input-SHA Ledger

| File | Path | SHA |
|:-----|:-----|:----|
| L=12 D_K^2 spectrum cache | `computations/s84_spectrum_cache_L12_tau019.npz` | `9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9` |
| L=10 D_K^2 spectrum cache | `computations/s84_spectrum_cache_L10_tau019.npz` | `<pinned at dispatch>` |
| canonical_constants.py | `computations/canonical_constants.py` | `<pinned at dispatch>` |
| computation script template | `computations/script-template.py` | `<pinned at dispatch>` |
| W1b-1 PV recalibration WP section | `sessions/archive/session-87/session-87-results-workingpaper.md §W1b-1` | `<pinned at dispatch>` |
| W1b-4 paired-slot near-unique WP section | `sessions/archive/session-87/session-87-results-workingpaper.md §W1b-4` | `<pinned at dispatch>` |
| W1b-5 PS A_F finite-L=10 6/6 axioms WP section | `sessions/archive/session-87/session-87-results-workingpaper.md §W1b-5` | `<pinned at dispatch>` |
| W1b-6 Connes-distance CLASS-γ WP section | `sessions/archive/session-87/session-87-results-workingpaper.md §W1b-6` | `<pinned at dispatch>` |
| W1a-2 Mellin-cone no-go theorem WP section | `sessions/archive/session-87/session-87-results-workingpaper.md §W1a-2` | `<pinned at dispatch>` |
| W1a-5 §VII.W-2 biconditional FORWARD-only WP section | `sessions/archive/session-87/session-87-results-workingpaper.md §W1a-5` | `<pinned at dispatch>` |
| W1a-6 §VII.X.2 NECESSITY STAGE-1 entry | `sessions/permanent-results-registry.md §VII.X.2` | `<pinned at dispatch>` |
| Cross-pillar bridge anatomy rule | `.claude/rules/cross-pillar-bridge-anatomy.md` | `<pinned at dispatch>` |
| Joint-theorem-promotion rule | `.claude/rules/joint-theorem-promotion.md` | `<pinned at dispatch>` |
| Methodology-wave-allowlist | `.claude/rules/methodology-wave-allowlist.md` | `<pinned at dispatch>` |
| Math-scripts canonical-write-order | `.claude/rules/math-scripts.md` §"Canonical Write-Order" | `<pinned at dispatch>` |
| Mechanical-closure-discipline rule | `.claude/rules/mechanical-closure-discipline.md` | `<pinned at dispatch>` |
| Substrate-first canonical-sourcing rule | `.claude/rules/substrate-first-canonical-sourcing.md` | `<pinned at dispatch>` |
| Regulator-pin-discipline rule | `.claude/rules/regulator-pin-discipline.md` | `<pinned at dispatch>` |

`audit_sha256` for each gate is computed at dispatch over the per-gate input-pin map subset relevant to that gate (NOT all 18 entries; per `cross-pillar-bridge-anatomy.md` AMRI Test 1 calibration the agent-memory and orchestrator-memory paths are deliberately EXCLUDED from input-pin maps).

---

**Plan-freeze checklist**:
- [x] 14 items 121-134 enumerated
- [x] Per-gate 13-field spec (Gate ID, Trigger, Classification, Agent, Hypothesis, Method, Machinery pin, 4-tuple, Threshold, Substitution chain, What PASS/FAIL MEAN, Effort, Substrate framing, Output artifacts)
- [x] Decision-point routing for downstream waves
- [x] Machinery-enumeration pin §0.11
- [x] Input-SHA ledger with `<pinned at dispatch>` placeholders for runtime SHA capture
- [x] Substrate-first framing (no GR-as-container language; D_K eigenvalues → spectral moments → emergent observables)
- [x] AMRI compliance: agent-memory paths NOT pinned in input-pin map (per cross-pillar-bridge-anatomy.md AMRI Test 1 calibration)
- [x] METHODOLOGY-class items (#124, #128-#132, #133, #134) flagged for methodology-wave-allowlist.md SHA computation at plan-freeze
- [x] Verdict source canonical: `computations/s88_gate_verdicts.txt`
