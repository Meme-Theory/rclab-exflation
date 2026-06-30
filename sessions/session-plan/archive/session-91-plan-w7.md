# Session 91 Plan — Wave 7: §VII.AQ + §VII.AT + §VII.AW substrate-physics chirality

**Wave Theme**: Substrate-physics evaluation of three chirality candidates landed at S90 W7 CF-45 (the CF-A40 FAIL alternative-chirality-rescope landing per `methodology-wave-instances.md ### W7-6 (S90)` audit_sha256=`84ecf7a76ce2244efec2da6f96c4eca72c4416242b37ac862918905337564c88`). The three candidates partition the chirality-grading axis of the substrate spectral triple `(A_K, H_K, D_K, γ, J)`:

- **Candidate (c) — Inner-fluctuation 1-form A at fixed γ_9** (§VII.AQ.OP-PROJ Stage-2-style upgrade per the existing tensor-product chirality `γ_9 = γ_5 ⊗ γ_F`)
- **Candidate (a) — Bi-chirality direct-sum** `γ_9' = γ_5 ⊕ γ_F` (§VII.AT.OP-PROJ; STAGE-0-CANDIDATE-PENDING-S91-SUBSTRATE-PHYSICS at S90 close)
- **Candidate (b) — SU(3)-coloured chirality** `γ_9'' = γ_F^c` per Connes-Marcolli 2008 §11 (§VII.AW.OP-PROJ; STAGE-0-CANDIDATE-PENDING-S91-SUBSTRATE-PHYSICS at S90 close)

W7 evaluates substrate-physics for all three plus refines the CF-54 Route C in-cache regression at L_max=16 via cache extension under Friedrich-Bär saturation feasibility pre-check per `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"`.

**Primary author**: `connes-ncg-theorist` (all four gates; the NCG-axiomatic axis is where the chirality grading discriminator lives). Stage-2-style cross-axis confirmation routes to `van-den-dungen-bridge-theorist` (NCG-submersion / Kasparov-bridge axis distinct from connes-ncg's axiomatic-NCG axis) and `volovik-superfluid-universe-theorist` (substrate-physics / 3He-B inheritance axis) where Stage-2 PASS-AND aggregation is required per `joint-theorem-promotion.md §"Stage 2"` + §"Axis-B Selection Protocol" (downstream-inheritance reach + axis-distinctness + audit-coverage adequacy).

## Wave 7 Summary

- **Item count**: 4 gates (T2.22 split into two PARALLEL sub-gates §W7-2a + §W7-2b for §VII.AT and §VII.AW)
- **Effort**: ~3.5 wave-equivalents (T2.21 ~1.0 + T2.22a ~0.85 + T2.22b ~0.85 + T2.23 ~0.8)
- **Primary author**: `connes-ncg-theorist` (all four)
- **Substrate framing**: three distinct chirality candidates ⇒ three distinct spectral triples ⇒ three distinct §VII slots. Direction of explanation: substrate IS spectral triple → chirality-grading modification IS new-spectral-triple → new substrate-IS observables. No container-thinking; the chirality is not a "convention" chosen on top of a pre-existing substrate but IS substrate-IS structural data.
- **Wave-class**: COMPUTE (all four gates are substrate-physics numerical / axiomatic-derivation gates with pre-registered PASS / FAIL / INFO thresholds per `wave-classification.md` M1 numerical-predicate-present test). No METHODOLOGY-class items in W7 (no rule-file edits or registry-landing-only items; the §VII.AT.OP-PROJ + §VII.AW.OP-PROJ 5-anatomy completion landings at T2.22 are substrate-physics derivations producing new numerical predicate satisfaction, NOT artifact-existence-only landings).

## Wave 7 Decision Point Prerequisites

| Gate | Prereqs | Routing |
|:-----|:--------|:--------|
| §W7-1 (T2.21) | §VII.AQ.OP-PROJ STAGE-1-CANDIDATE entry (S88 W7b-79 baseline + S90 W7 CF-54 Phase-2 retrofit) at registry line 17341; `_spectral_action_regulators.py` SCHEMATIC helper at L_max=12 cache | INDEPENDENT — dispatches FIRST in W7 (no prereqs on T2.22a/b/T2.23) |
| §W7-2a (T2.22 part 1; §VII.AT) | §VII.AT.OP-PROJ STAGE-0-CANDIDATE entry (S90 W7 CF-45 landing) at registry line 17237; L_max=12 spectrum cache `s84_spectrum_cache_L12_tau019.npz` | PARALLEL with §W7-2b — no inter-dependency between the bi-chirality and SU(3)-coloured axiom re-derivations (orthogonal chirality-grading modifications) |
| §W7-2b (T2.22 part 2; §VII.AW) | §VII.AW.OP-PROJ STAGE-0-CANDIDATE entry (S90 W7 CF-45 landing) at registry line 17293; Connes-Marcolli 2008 ch.1 + §11 SU(3)-coloured chirality framework | PARALLEL with §W7-2a — same orthogonality remark |
| §W7-3 (T2.23) | CF-54 Route C in-cache regression baseline at L_max=10 (S90 W7-1 / W7-3); L_max=12 spectrum cache; Friedrich-Bär saturation feasibility pre-check per `math-scripts.md §"D_K Block-Diagonality"` | INDEPENDENT — L_max=16 cache extension is a refinement of an existing in-cache regression; does NOT depend on T2.21/T2.22 verdicts |

**Dispatch order**: §W7-1, §W7-2a, §W7-2b, §W7-3 are launched together (no serial dependencies); the §W7-2a + §W7-2b parallel pair is the canonical instance of `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3 applied at the chirality-grading sub-axis (bi-chirality direct-sum vs SU(3)-coloured colour-axis decomposition are STRUCTURALLY ORTHOGONAL grading-modifications of the substrate's chirality element γ — neither sub-axis pre-determines the other's verdict).

## Wave 7 → Wave 8 Decision Point (forward routing)

| Gate verdict | Forward consequence |
|:-------------|:--------------------|
| T2.21 PASS | §VII.AQ.OP-PROJ promotes to STAGE-3-PERMANENT-ELIGIBLE under Reading A: Stage-2-style cross-axis re-evaluation under substrate-natural inner-fluctuation 1-form `A` confirms scheme-equivalence at machine precision (`|GV_canonical − GV_inner-fluctuation| < 1e-3` in M_KK² units), strengthening the §VII.AQ.OP-PROJ Reading A scheme-INDEPENDENCE evidence beyond the W7-2 CF-55 substrate-physics adjudicator (S90). The Stage-2 cross-axis independent-verify gate `S91-VII-AQ-STAGE-2-INDEPENDENT-VERIFY-WITH-ORTHOGONALITY` queued at S91+ per W-23 §V.3 spec is then dispatchable as a separate W8 gate. |
| T2.21 FAIL | §VII.AQ.OP-PROJ STAGE-1-CANDIDATE retains its existing tag; the substrate-natural inner-fluctuation deformation does NOT preserve the GV-canonical-difference; Reading B (Δ_scheme ≥ 1e-3 at the bridge-map-scheme axis) reopens at the inner-fluctuation deformation layer. Forward S92+ gate: re-evaluate §VII.AQ Element-3 fiducial-anchor binding under Branch B per `cross-pillar-bridge-anatomy.md §"Element 3 fiducial-anchor binding discipline"` axis β bridge-map-scheme suffix discipline. |
| T2.21 INFO | regime_verdict ∈ {MARGINAL, BREAKDOWN} per the auto-shortening clause discipline in `gate-verdicts.md`; the inner-fluctuation deformation is well-defined within a sub-window of the planned (p, q) sector enumeration but breaks down on the boundary; queue forward extension at S92+ once the regime-breakdown sub-block is characterized. |
| T2.22a PASS | §VII.AT.OP-PROJ promotes from STAGE-0-CANDIDATE → STAGE-1-CANDIDATE (5-anatomy completion): all 7 NCG axioms re-derived under direct-sum chirality `γ_9' = γ_5 ⊕ γ_F`; KO-dim computed under bi-chirality; bridge-map class (Element-3) identified; Level-2 envelope (Element-4) declared; Level-3 empirical anchor (Element-5) extracted at L_max=12. Forward: Stage-2 cross-axis independent-verify queued at W8 with axis-distinct cross-reviewers per `joint-theorem-promotion.md §"Stage 2"`. |
| T2.22a FAIL | §VII.AT.OP-PROJ retains STAGE-0-CANDIDATE; the bi-chirality grading violates one or more NCG axioms (most likely axiom 5' `J γ_9' = -γ_9' J` under direct-sum grading; alternative violations: orientability axiom 6 under non-tensor chirality, Poincaré duality under direct-sum grading). Diagnostic emitted: which axiom(s) FAILed and the algebraic obstruction. The candidate (a) substrate is structurally rejected; CF-A40 alternative-chirality-rescope evaluation closes the bi-chirality branch as eliminated. |
| T2.22a INFO | Axioms 1-7 + Poincaré duality consistent at L_max=12 but KO-dim ambiguous (e.g., direct-sum grading admits two distinct chirality conventions producing different KO-dim mod 8 assignments); further substrate-physics work needed at S92+ to pin KO-dim canonically. STAGE-0-CANDIDATE retained with KO-dim disambiguation queued. |
| T2.22b PASS | §VII.AW.OP-PROJ promotes from STAGE-0-CANDIDATE → STAGE-1-CANDIDATE (5-anatomy completion); analogous structure to T2.22a PASS under SU(3)-coloured chirality `γ_F^c`; Connes-Marcolli 2008 §11 framework verified at L_max=12. Forward: Stage-2 cross-axis independent-verify queued at W8. |
| T2.22b FAIL | §VII.AW.OP-PROJ retains STAGE-0-CANDIDATE; colour-dressed chirality grading violates one or more NCG axioms or produces KO-dim shift inconsistent with the Connes-Marcolli framework. SU(3)-coloured branch closes. |
| T2.22b INFO | Analogous KO-dim disambiguation or partial Element-3 bridge-map identification; STAGE-0-CANDIDATE retained with sub-questions queued. |
| T2.23 PASS | CF-54 Route C in-cache regression refined at L_max=16; the empirical-β estimate at substrate-distance pole s=4 (the Route C target observable per S90 W7-3 spec) converges to the asymptotic limit `α(s=4)` within ±10% per `cross-pillar-bridge-anatomy.md §"Level-2 empirical-β verification rule"`; cache-ceiling boundary effect characterized. |
| T2.23 FAIL | L_max=16 cache extension required but Friedrich-Bär saturation feasibility pre-check fails (the η_FB lower bound at the (p+q=L_max) NEW-sector intrusion exceeds the observable's structural ceiling); cache extension infeasible at L_max=16 within the saturation theorem's analytic certification; queued for S92+ at L_max ≥ 22 per W-6 CF-1 sub-window approach. |
| T2.23 INFO | Cache extension feasible at L_max=16 but the L^{-α} envelope's empirical exponent at the cache-ceiling boundary deviates from asymptotic limit by > 10%; cache-ceiling boundary effect is structurally significant per `cross-pillar-bridge-anatomy.md §"Level-2 empirical-β verification rule"`; diagnostic emitted + S92+ follow-up queued. |

---

## §W7-1. S91-VII-AQ-OP-PROJ-STAGE-2-UPGRADE-SUBSTRATE-PHYSICS (T2.21)

### 1. Gate ID

`S91-VII-AQ-OP-PROJ-STAGE-2-UPGRADE-SUBSTRATE-PHYSICS`

Provenance: S91 W7 carry-forward T2.21 = W7-CF-W7-2 from S90 W7 CF-55 substrate-physics adjudicator (`sessions/archive/session-90/session-90-w7-workingpaper.md §"W7-CF-W7-2"` carry-forward block).

### 2. Trigger

`[VERIFY]` + `[SIGN]` — substrate-physics Stage-2-style upgrade evaluation requires both the regime-of-validity verification (inner-fluctuation deformation preserves γ_9 + J + axioms 1-7 by Connes-Chamseddine construction at L_max=12) AND the sign-direction prediction (Reading A: |GV_canonical − GV_inner-fluctuation| < tolerance; Reading B: difference exceeds tolerance). Per `gate-verdicts.md §"S87+ canonical form Schema-v2"`, the sign-verdict / magnitude-verdict / regime-verdict 3-tuple companion row IS REQUIRED.

### 3. Classification

**GEOMETRIC** (substrate-IS structural property of the spectral triple at §VII.AQ.OP-PROJ; specifically, the scheme-equivalence of the SECONDARY-CLASS-SCHEME-DISCRIMINATOR theorem under the substrate-natural inner-fluctuation 1-form `A` deformation, which is a GEOMETRIC deformation of the Dirac operator at fixed chirality grading `γ_9 = γ_5 ⊗ γ_F` and fixed real structure `J`).

### 4. Agent type

**Primary author**: `connes-ncg-theorist`

Rationale: the inner-fluctuation 1-form `A` is the substrate-natural Connes-Chamseddine 1996 §2.2-2.3 deformation `D_K → D_K + A + J A J^{-1}` where `A = Σ_i a_i [D_K, b_i]` for `a_i, b_i ∈ A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`. This is the NCG-axiomatic axis — `connes-ncg-theorist` owns the inner-fluctuation calculus, the preservation of NCG axioms 1-7 under the deformation, and the cross-check that `γ_9` and `J` are invariant (no chirality-grading or real-structure modification).

**FORBIDDEN test-case agent type**: `gen-physicist` (per spawn-prompt). The gate-block dispatch prompt MUST name `connes-ncg-theorist` as primary author.

Stage-2-style cross-axis confirmation routing (forward; queued for W8 dispatch on PASS): `van-den-dungen-bridge-theorist` (Axis-A NCG-submersion / Kasparov-bridge axis distinct from connes-ncg's axiomatic-NCG axis per axis-distinctness clause) + `volovik-superfluid-universe-theorist` (Axis-B substrate-physics / 3He-B inheritance axis; Stage-2 cross-axis PASS-AND aggregation per `joint-theorem-promotion.md §"Stage 2"` strict-conjunction requirement).

### 5. Hypothesis

**Hypothesis statement (Reading A)**: The SECONDARY-CLASS-SCHEME-DISCRIMINATOR theorem of §VII.AQ.OP-PROJ — that the GV-Heitsch invariant on the `(C_H, C_εH)` parity-twin pair evaluates to the same Sage-QQ exact canonical pin `gv_canonical_difference_FW = -40579.1500479506` under the three secondary-class schemes (APS-1975-secondary-class, Cheeger-Simons, Bismut-Cheeger) per `cross-pillar-bridge-anatomy.md §"Element 3 fiducial-anchor binding discipline"` axis β — is INVARIANT under the substrate-natural Connes-Chamseddine 1996 §2.2-2.3 inner-fluctuation deformation `D_K → D_K + A + J A J^{-1}` where `A = Σ_i a_i [D_K, b_i]` for `a_i, b_i ∈ A_K`.

**Substrate-physics content**: the inner-fluctuation 1-form `A` is the substrate-NATURAL deformation WITHIN the registered spectral triple at §VII.AQ.OP-PROJ. By Connes-Chamseddine construction, the deformation preserves: (i) the chirality grading `γ_9 = γ_5 ⊗ γ_F`; (ii) the real structure `J`; (iii) NCG axioms 1-7 + Poincaré duality. Therefore the GV-Heitsch invariant computed on the deformed Dirac operator `D_K + A + JAJ^{-1}` lives on the SAME spectral triple class as `D_K`; scheme-equivalence is preserved by Connes-Chamseddine theorem (intrinsic to the spectral triple, not to a particular Dirac operator within its inner-automorphism orbit).

**Reading B (alternative)**: scheme-equivalence at the canonical pin is an accidental feature of the un-deformed `D_K` at L_max=10; inner-fluctuation breaks the equivalence by perturbing the spectrum of `D_K^2` at the substrate-distance pole driving the GV cocycle. Reading B is the structural-counterpart to Reading A and is the FAIL branch of the discriminator gate.

### 6. Method (complete dispatch prompt for connes-ncg-theorist)

```
Dispatch prompt for connes-ncg-theorist:

You are dispatched as primary author for gate
S91-VII-AQ-OP-PROJ-STAGE-2-UPGRADE-SUBSTRATE-PHYSICS (T2.21).

Substrate framing: §VII.AQ.OP-PROJ's substrate IS the spectral triple
(A_K, H_K, D_K, γ_9, J) at fixed chirality grading γ_9 = γ_5 ⊗ γ_F.
The inner-fluctuation 1-form A IS a substrate-natural deformation
WITHIN the registered spectral triple's inner-automorphism orbit;
preserves γ_9 + J + axioms 1-7 by Connes-Chamseddine 1996
§2.2-2.3 construction.

DELIVERABLES:

(D1) New helper module:
     computations/_shared/_connes_chamseddine_inner_fluctuation.py
     - Class InnerFluctuation1Form(A_K_generators, D_K_spectrum_cache, L_max)
     - Method build_A(a_coeffs, b_coeffs): A = Σ_i a_i [D_K, b_i]
       returns Hermitian 1-form operator on H_K (block-diagonal across
       Peter-Weyl (p,q) sectors per D_K block-diagonality theorem)
     - Method apply_deformation(A_form): D_K → D_K + A + J·A·J^{-1}
       returns deformed Dirac operator with preserved γ_9 anticommutation
       and J commutation (axiom 5 + axiom 3 verified at machine epsilon)
     - Method verify_axioms_1_7(D_K_def): returns dict of axiom-by-axiom
       PASS/FAIL status under the deformation. Each axiom verified
       independently:
         axiom 1 (dimension): spectrum growth rate preserved (Wodzicki/
           Weyl bound at d=4)
         axiom 2 (regularity): [D_K_def, a] bounded for all a in A_K
         axiom 3 (reality): J D_K_def = D_K_def J (real structure
           preservation by inner-fluctuation construction)
         axiom 4 (first-order): [[D_K_def, a], b^o] = 0
         axiom 5 (chirality): {D_K_def, γ_9} = 0
         axiom 6 (orientability): unchanged by inner-fluctuation
         axiom 7 (finiteness + Poincaré duality): K-theory pairing
           invariant
     - SCHEMATIC-vs-FULL pin: this is a FULL physical Connes-Chamseddine
       1996 §2.2-2.3 implementation (NOT SCHEMATIC); CLASS=FULL in
       gate-block PIN MAP; convention=...-FULL-CC1996-INNER-FLUCTUATION
       (no -SCHEMATIC suffix). Per `substrate-first-canonical-sourcing.md
       §(iv)` K=4 MANDATORY level-pin discipline, CLASS=FULL is the
       structural-canonical pin for this gate; SCHEMATIC fallback is
       NOT admissible because the inner-fluctuation calculus has a
       closed-form algebraic implementation on A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ).

(D2) Producing script:
     computations/session-91/s91_w7_1_vii_aq_op_proj_stage_2_upgrade.py
     - Loads s84_spectrum_cache_L12_tau019.npz at L_max=12 (per
       `math-scripts.md §"D_K Block-Diagonality"` Casimir-bound:
       worst-case (p,q) sector for the GV-Heitsch invariant truncates
       at p+q ≤ 8 at machine precision; L_max=12 is 2-level safety
       margin)
     - Computes baseline GV_canonical on un-deformed D_K from the
       cache → cross-validates against canonical pin
       gv_canonical_difference_FW = -40579.1500479506 (S87 W8-8 audit
       _sha256=ec8c92e51d3bff95df8b3b9b4dc60d27e10a4d96e234eb14d27c1d8c6f5cd47e)
     - Inner-fluctuation deformation scan: iterate (a_coeffs, b_coeffs)
       over a pre-registered 5-point grid of A_K generator pairs:
         (1) a = (1, 0, 0), b = (i, 0, 0)  [ℂ-summand only]
         (2) a = (0, 1_ℍ, 0), b = (0, j_ℍ, 0)  [ℍ-summand only]
         (3) a = (0, 0, e_11), b = (0, 0, e_22)  [M_3(ℂ)-summand only]
         (4) a = (1, 1_ℍ, 0), b = (i, j_ℍ, 0)  [ℂ ⊕ ℍ mixed]
         (5) a = (1, 1_ℍ, e_11), b = (i, j_ℍ, e_22)  [ℂ ⊕ ℍ ⊕ M_3(ℂ)
              full]
       (i, j_ℍ are standard imaginary units in ℂ, ℍ; e_ij are matrix
       units in M_3(ℂ))
     - For each of the 5 grid points, compute the deformed Dirac
       operator D_K_def = D_K + A + J·A·J^{-1}, verify axioms 1-7
       at machine epsilon, then compute GV_deformed on the deformed
       spectrum (same secondary-class scheme as the canonical pin)
     - Output: 5-element array Δ_GV_inner-fluctuation[i] = GV_deformed[i]
       − gv_canonical_difference_FW for i = 1..5
     - PASS criterion (Reading A): max_i |Δ_GV_inner-fluctuation[i]| <
       pass_tolerance per §9 below; AND axioms 1-7 PASS at machine
       epsilon at all 5 grid points
     - FAIL criterion (Reading B): max_i |Δ_GV_inner-fluctuation[i]| ≥
       info_tolerance per §9 below
     - INFO criterion: pass_tolerance ≤ max_i |Δ_GV_inner-fluctuation[i]|
       < info_tolerance; regime_verdict = MARGINAL or BREAKDOWN per
       auto-shortening clause (if the 5-grid window must be shortened
       at runtime due to axiom-violation at one or more grid points)

(D3) Working-paper section in
     sessions/archive/session-91/session-91-w7-workingpaper.md §W7-1
     >15 lines; substantive content per `agent-standards.md §"Completion
     Verification"`; substrate-framing reminder + 5-anatomy IS-not-IN
     declaration (substrate-IS = inner-fluctuation-deformed Dirac
     operator's GV-Heitsch invariant; laboratory-IN = 3He-B BdG sector
     (η=0, GV≠0) joint-probe under inner-fluctuation deformation; bridge
     map = APS-1975-secondary-class scheme per §VII.AQ.OP-PROJ Element-3
     binding declaration; algebraic envelope = Connes-Chamseddine 1996
     §2.2-2.3 finite-deformation theorem; empirical anchor = canonical
     pin gv_canonical_difference_FW invariance at 5 grid points).

(D4) Verdict line in
     computations/session-91/s91_gate_verdicts.txt
     Canonical line per `gate-verdicts.md §"S81+ canonical form"`:
     S91-VII-AQ-OP-PROJ-STAGE-2-UPGRADE-SUBSTRATE-PHYSICS: PASS|FAIL|INFO
       -- value=<max_i |Δ_GV_inner-fluctuation[i]|>
       scheme=APS-1975-secondary-class
       convention=substrate-distance-1-FULL-CC1996-INNER-FLUCTUATION
       L_max=12
       audit_sha256=<64-hex from closure_hash(input-pin-map)>
       content_sha256=<64-hex of producing-script bytes>
       schema_version=S87+

     Dual-SHA companion comment row (W9a-99 split):
     # audit_sha256_short=<16-hex> content_sha256_short=<16-hex> #
     S91-VII-AQ-OP-PROJ-STAGE-2-UPGRADE-SUBSTRATE-PHYSICS dual-SHA
     companion row (W9a-99 split)

     Schema-v2 3-tuple companion row (REQUIRED per [SIGN] trigger):
     # sign_verdict=PASS|FAIL|N/A magnitude_verdict=PASS|INFO|FAIL
       regime_verdict=VALID|MARGINAL|BREAKDOWN #
       S91-VII-AQ-OP-PROJ-STAGE-2-UPGRADE-SUBSTRATE-PHYSICS 3-tuple
       annotation (S87 schema-v2)

(D5) Substitution chain in §10 below (mandatory per `math-scripts.md
     §"Double-Check Logic Before Compute"` for [SIGN] gate); the
     chain shows the direction of the predicted Δ_GV under inner-
     fluctuation deformation derived from substrate-IS Connes-
     Chamseddine 1996 §2.2-2.3 theorem.

FORBIDDEN actions per `v3-closure-recovery.md §PROHIBITED_ACTIONS`:
- Convention-shopping: do NOT switch from APS-1975-secondary-class
  scheme to Cheeger-Simons or Bismut-Cheeger to reach PASS; the
  scheme is pre-registered at §VII.AQ.OP-PROJ Element-3 binding.
- Iterate-until-PASS: do NOT expand the 5-grid window to additional
  generator pairs if the 5-grid FAILs; the grid is pre-registered.
- Post-hoc threshold editing: pass_tolerance + info_tolerance are
  pinned per §9; do NOT loosen.
- Ansatz-forced PASS: do NOT hardcode the canonical pin into the
  comparison; load it from canonical_constants.gv_canonical_difference_FW.
```

### 7. Machinery pin (PRDR)

| Pin | Value | Source |
|:----|:------|:-------|
| `N_eval` | 5 generator pairs × ~9792 (largest single block dim at L_max=12) = ~48960 eigenvalue evaluations | derived; pin |
| `L_max` | 12 (operational); 10 (canonical_constants pin baseline) | `s84_spectrum_cache_L12_tau019.npz`; Casimir-bound truncation per `math-scripts.md §"D_K Block-Diagonality"` |
| `scan_range` | (a_coeffs, b_coeffs) 5-point grid enumerated in §6 D2 | pre-registered |
| `step_size` | N/A (discrete grid, not continuous scan) | — |
| `tolerance` | `pass_tolerance = 1e-3` M_KK² units; `info_tolerance = 1e-1` M_KK² units | per §VII.AQ.OP-PROJ scheme-equivalence threshold (`|GV_APS1975 − GV_Cheeger-Simons| < 1e-3` in M_KK² units, per `cross-pillar-bridge-anatomy.md §"Element 3 fiducial-anchor binding discipline"` axis β Reading A spec); the analogous threshold for inner-fluctuation deformation invariance |
| `scheme` | `APS-1975-secondary-class` | §VII.AQ.OP-PROJ Element-3 binding (registry line 17341) |
| `convention` | `substrate-distance-1-FULL-CC1996-INNER-FLUCTUATION` | NEW convention tag; FULL physical Connes-Chamseddine 1996 §2.2-2.3 implementation; no SCHEMATIC suffix per `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY (FULL is structurally-canonical) |
| `random_seed` | N/A (deterministic) | — |
| `GPU path` | NumPy CPU (block-diagonal sparse-Lanczos on per-(p,q) sector; largest block ~9792×9792 dense fits in 17.1 GB VRAM with margin >11× per `math-scripts.md §"D_K Block-Diagonality"`; GPU optional `torch.linalg` for large blocks) | per `math-scripts.md §"Environment"`; OMP_NUM_THREADS=8 cap CPU fallback |
| `CLASS pin` | `FULL` (NOT SCHEMATIC) | `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY level-pin |
| `tier_pin` | `TIER-1` (FULL physical regularization at structural-canonical layer) | — |
| `precision` | float64 throughout; complex128 for J operator (KO-dim=6 BDI class) | — |

**Input SHA-256 pins (Input-PIN MAP)**:

| File | Path | SHA | Source |
|:-----|:-----|:----|:-------|
| L_max=12 spectrum cache | `computations/session-84/s84_spectrum_cache_L12_tau019.npz` | `<pinned at dispatch>` (static; precompute at plan-freeze) | S84 W2 D_K-canonical compute |
| canonical_constants module | `computations/_shared/canonical_constants.py` | `<pinned at dispatch>` | post-S91 W0 housekeeping (lines 561-563 fresh pins) |
| Connes-Chamseddine inner-fluctuation helper (NEW) | `computations/_shared/_connes_chamseddine_inner_fluctuation.py` | `<computed-at-runtime>` (D1 deliverable; new module) | this gate (T2.21) |
| §VII.AQ.OP-PROJ canonical pin | `gv_canonical_difference_FW = -40579.1500479506` | S87 W8-8 audit_sha256=`ec8c92e51d3bff95df8b3b9b4dc60d27e10a4d96e234eb14d27c1d8c6f5cd47e` | from canonical_constants via `mcp__knowledge__.get_constant("gv_canonical_difference_FW")` |
| §VII.AQ.OP-PROJ registry entry | `sessions/permanent-results-registry.md` line 17341 | `<pinned at dispatch>` (file SHA-256 over rolling content; S90-frozen) | S88 W7b-79 + S90 W7 CF-54 Phase-2 retrofit |

**Audit-SHA closure**: `audit_sha256 = closure_hash(ordered-input-pin-map)` per `_script_template.py` `append_verdict()` canonical pattern. Per Class 8.3 publication precision: SHA computed at full 64-hex; no head-truncation.

### 8. Expected output 4-tuple

`(value=<max_i |Δ_GV_inner-fluctuation[i]|>, scheme=APS-1975-secondary-class, convention=substrate-distance-1-FULL-CC1996-INNER-FLUCTUATION, L_max=12)`

Output file contents (`s91_w7_1_vii_aq_op_proj_stage_2_upgrade.npz` + `.png` + `.json` sidecar):

- `Delta_GV_inner_fluctuation_array`: shape (5,); float64
- `GV_deformed_per_grid_point`: shape (5,); float64
- `axioms_pass_status_per_grid_point`: shape (5, 7); bool (per axiom 1-7 per grid point)
- `KO_dim_per_grid_point`: shape (5,); int (expected: all 6 by Connes-Chamseddine theorem)
- `pass_band_max`, `info_band_max`, `verdict_composite` strings
- `sign_verdict`, `magnitude_verdict`, `regime_verdict` strings per `gate-verdicts.md §"S87+ canonical form Schema-v2"`
- `audit_sha256`, `content_sha256` 64-hex
- `runtime_seconds` float
- `domain_used_frac` float (1.0 by default since no auto-shortening anticipated; <1.0 if axiom-violation forces 5-grid window shortening at runtime)

PNG plot: `Δ_GV_inner-fluctuation` value per grid point with horizontal lines at pass_tolerance and info_tolerance for visual band-comparison.

### 9. PASS / FAIL / INFO thresholds

**PASS**: `max_i |Δ_GV_inner-fluctuation[i]| < pass_tolerance = 1e-3` (M_KK² units) AND axioms 1-7 PASS at machine epsilon (`|J D_K_def - D_K_def J| < 1e-12` for axiom 3; `|{D_K_def, γ_9}| < 1e-12` for axiom 5; analogous machine-precision bounds for axioms 1, 2, 4, 6, 7) at all 5 grid points AND KO-dim = 6 invariant across all 5 grid points AND `regime_verdict = VALID`.

**INFO**: `pass_tolerance ≤ max_i |Δ_GV_inner-fluctuation[i]| < info_tolerance = 1e-1` (M_KK² units) AND axioms 1-7 PASS AND KO-dim = 6 invariant; OR axioms 1-7 PASS at all 5 grid points but with `regime_verdict = MARGINAL` (one or more grid points triggers a sub-window of regime-of-validity activation per the auto-shortening clause of `gate-verdicts.md`); composite collapse per rule: `magnitude_verdict=INFO` composite=INFO.

**FAIL**: `max_i |Δ_GV_inner-fluctuation[i]| ≥ info_tolerance = 1e-1` (M_KK² units) — Reading B confirmed (inner-fluctuation deformation perturbs the GV-canonical at a level structurally distinguishable from the canonical pin) OR axioms 1-7 FAIL at one or more grid points OR KO-dim shifts from 6 at one or more grid points OR `regime_verdict = BREAKDOWN`. Composite collapse per rule: `regime_verdict=BREAKDOWN` composite=FAIL regardless of magnitude.

**Tolerance rule**: ABSOLUTE (M_KK² units, not ratio); pass_tolerance and info_tolerance are 2 orders of magnitude apart at 1e-3 and 1e-1 respectively to allow a clean INFO band for marginal-deformation cases.

**Publication precision per Class 8.3 MANDATORY**: pass_tolerance and info_tolerance are pinned at 3-significant-figure publication precision (1.00e-3 and 1.00e-1 respectively); downstream verifier rel_tol ≥ 1e-3 per the publication-precision pre-registration discipline.

### 10. Substitution chain ([SIGN])

Pre-registered direction-prediction substitution chain per `math-scripts.md §"Double-Check Logic Before Compute"`:

**Step 1 (Definitions)**:
- `D_K`: un-deformed Dirac operator at τ_fold = 0.190, L_max=12 (from `s84_spectrum_cache_L12_tau019.npz`)
- `A = Σ_i a_i [D_K, b_i]`: substrate-natural 1-form built from generators `a_i, b_i ∈ A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`
- `D_K_def = D_K + A + J A J^{-1}`: inner-fluctuation deformed Dirac operator (Hermitian by construction since A^* = -A, J A^* J^{-1} = -J A J^{-1}, so D_K_def = D_K_def^*)
- `GV_canonical = gv_canonical_difference_FW = -40579.1500479506` (S87 W8-8 canonical pin on un-deformed D_K)
- `GV_deformed = GV-Heitsch invariant computed on D_K_def using the same APS-1975-secondary-class scheme`
- `Δ_GV_inner-fluctuation = GV_deformed - GV_canonical`

**Step 2 (Substitution — Connes-Chamseddine 1996 §2.2-2.3 theorem)**:

The Connes-Chamseddine 1996 §2.2-2.3 inner-fluctuation theorem states:

```
For any 1-form A built as A = Σ_i a_i [D_K, b_i] with a_i, b_i ∈ A_K and
J = real structure, the deformation D_K → D_K + A + J A J^{-1} preserves
the full spectral triple structure: chirality γ_9 anticommutation, J
commutation, NCG axioms 1-7. The deformed Dirac operator D_K_def lives
in the same NCG inner-automorphism orbit as D_K.
```

**Step 3 (Simplification — Algebraic invariance of secondary-class evaluation)**:

The GV-Heitsch invariant on the `(C_H, C_εH)` parity-twin pair is a SECONDARY-CLASS invariant of the spectral triple's K-theory class (per Connes-Karoubi pairing). Inner-automorphism deformations preserve K-theory class (homotopy-invariant). Therefore:

```
GV_deformed(D_K_def) = GV_canonical(D_K)  ⟺  K-theory class preserved
                                          ⟺  Connes-Chamseddine 1996 §2.2-2.3 inner-fluctuation invariance theorem
```

**Step 4 (Direction-prediction)**:

Predicted: `Δ_GV_inner-fluctuation = 0` to machine epsilon (`|Δ_GV| < 1e-12` M_KK² units) by the algebraic theorem of Step 3 — modulo numerical noise from L_max=12 truncation and float64 round-off in the inner-fluctuation calculus.

**Conservative substrate-physics direction**: the predicted Reading A PASS is `max_i |Δ_GV_inner-fluctuation[i]| < pass_tolerance = 1e-3` (M_KK² units; 9 orders of magnitude looser than the machine-epsilon theoretical bound of 1e-12 to absorb truncation noise). The sign-verdict is PASS by the algebraic argument of Step 3; the magnitude_verdict is PASS by the numerical tolerance band.

**Step 5 (Conclusion — Pre-registered direction)**:

Sign_verdict PASS prediction: `max_i |Δ_GV_inner-fluctuation[i]| > 0` (trivially; numerical noise is non-zero) but bounded above by pass_tolerance. The Connes-Chamseddine 1996 §2.2-2.3 theorem PINs the direction of the Δ_GV measurement to "approximately zero" (algebraic identity modulo numerical noise); a FAIL outcome (`Δ_GV` of order 1e-1 or larger) would falsify either: (i) the un-deformed canonical pin's accuracy at L_max=10 → 12 → ...; (ii) the Connes-Chamseddine 1996 §2.2-2.3 theorem's applicability at L_max=12 truncation; (iii) the assumption that the GV-Heitsch invariant is a SECONDARY-CLASS invariant rather than a representative-dependent observable.

### 11. Solution-space interpretation

**PASS solution-space corridor**: §VII.AQ.OP-PROJ Reading A is STRENGTHENED — the SECONDARY-CLASS-SCHEME-DISCRIMINATOR theorem's scheme-equivalence is not just numerically coincidental at L_max=10 on the un-deformed `D_K`, but is structurally invariant under the substrate-natural inner-fluctuation deformation. Reading B (Δ_scheme ≥ 1e-3 alternative) closes definitively at the inner-fluctuation deformation layer. Stage-3 PERMANENT eligibility advances; the remaining requirement is Stage-2 cross-axis independent-verify (queued for W8 dispatch per `joint-theorem-promotion.md §"Stage 2"`).

**FAIL solution-space corridor**: Reading B (Δ_scheme ≥ 1e-3 at the inner-fluctuation deformation layer) opens for §VII.AQ.OP-PROJ; the canonical pin `gv_canonical_difference_FW = -40579.1500479506` is representative-dependent rather than secondary-class-invariant. The §VII.AQ Element-3 fiducial-anchor binding declaration (axis β bridge-map-scheme suffix discipline per `cross-pillar-bridge-anatomy.md §"Element 3 fiducial-anchor binding discipline"`) requires MANDATORY suffix tagging across the three secondary-class schemes; the §VII.AQ.OP-PROJ Reading A claim of scheme-equivalence is structurally weakened to Reading B status. Forward S92+ work: characterize the `Δ_GV` perturbation direction as a function of generator-pair choice; identify whether the algebraic FAIL is structural (Connes-Chamseddine 1996 §2.2-2.3 inapplicable at L_max=12 truncation) or numerical (truncation noise dominating the algebraic invariance).

**INFO solution-space corridor**: scheme-equivalence is preserved under most grid points but fails at one or more; the failure pattern's substrate-physics correlation (which A_K summand is the trigger?) is informative for the Element-3 binding direction. Forward: characterize the failure pattern; reassess whether the 5-grid window is exhaustive or whether additional generator-pair classes must be tested at S92+.

### 12. Effort

**~1.0 wave-equivalent** (~6-8 hours of connes-ncg-theorist dispatch time):
- D1 helper module authoring: ~2-3 hours (Connes-Chamseddine 1996 §2.2-2.3 inner-fluctuation calculus implementation on block-diagonal D_K at L_max=12; 7-axiom verification subroutines)
- D2 producing script: ~2-3 hours (5-point grid scan; 5 deformations × axiom verification × GV-canonical recomputation)
- D3 working-paper section: ~1 hour (>15 lines substantive; 5-anatomy IS-not-IN declaration; substrate-framing reminder)
- D4 verdict line + dual-SHA + 3-tuple companion: ~30 minutes (via `_script_template.py` `append_verdict()` canonical helper)
- D5 substitution chain documentation in working-paper: included in D3

### 13. Substrate-framing reminder

§VII.AQ.OP-PROJ's substrate IS the spectral triple `(A_K, H_K, D_K, γ_9 = γ_5 ⊗ γ_F, J)` at the registered tensor-product chirality. The inner-fluctuation 1-form `A` IS a substrate-NATURAL deformation WITHIN the registered spectral triple's inner-automorphism orbit (per Connes-Chamseddine 1996 §2.2-2.3); preserves `γ_9` + `J` + axioms 1-7 by construction. Direction of explanation: substrate IS spectral triple → inner-fluctuation IS substrate-natural deformation within the registered triple's inner-automorphism orbit → deformed Dirac `D_K_def` lives on the SAME spectral triple class as `D_K` → GV-Heitsch invariant is K-theory-class-invariant → scheme-equivalence preserved under deformation. Container-thinking violation FORBIDDEN: "we deform the Dirac operator by adding a 1-form A" — INVERT: "the inner-fluctuation 1-form A IS substrate-IS structural data living within the spectral triple's inner-automorphism orbit; the deformation D_K → D_K_def is the orbit action of A on D_K, intrinsic to the registered spectral triple at §VII.AQ.OP-PROJ".

---

## §W7-2a. S91-VII-AT-OP-PROJ-7-AXIOM (T2.22 part 1) [PARALLEL with §W7-2b]

### 1. Gate ID

`S91-VII-AT-OP-PROJ-7-AXIOM`

Provenance: S91 W7 carry-forward T2.22 part 1 = §VII.AT.OP-PROJ STAGE-0-CANDIDATE-PENDING-S91-SUBSTRATE-PHYSICS substrate-physics derivation (registry entry at line 17237 explicitly defers the 7-axiom + KO-dim + 5-anatomy completion to S91+ per W-5 CF-W5-5 substrate-physics computation spec; the §VII.AT.OP-PROJ entry's S91+ DEFERRED COMPUTATION block at registry lines 17269-17276 enumerates the 6-item work).

### 2. Trigger

`[VERIFY-THEOREM]` + `[VERIFY]` — substrate-physics derivation requires axiomatic theorem verification (7 NCG axioms + Poincaré duality under direct-sum chirality grading `γ_9' = γ_5 ⊕ γ_F`) plus numerical empirical anchor verification (cocycle evaluation on L_max=12 spectrum cache under bi-chirality grading).

### 3. Classification

**GEOMETRIC** (substrate-IS structural property of a NEW spectral triple distinct from §VII.AQ.OP-PROJ; the bi-chirality direct-sum grading IS a structurally distinct spectral triple, NOT a deformation of the §VII.AQ.OP-PROJ spectral triple — direction of explanation: each chirality grading IS a structurally distinct substrate per §VII.AT.OP-PROJ registry entry substrate framing block at line 17287).

### 4. Agent type

**Primary author**: `connes-ncg-theorist`

Rationale: 7-axiom re-derivation under modified chirality grading is the NCG-axiomatic axis; `connes-ncg-theorist` owns the chirality grading axioms (5 + 5' under modification), the J commutation/anticommutation calculus (axiom 3 + KO-dim mod 8 classification), the Poincaré duality K-theory pairing, and the orientability axiom 6.

**FORBIDDEN test-case agent type**: `gen-physicist` (per spawn-prompt).

Stage-2-style cross-axis confirmation routing (forward; queued for W8 on PASS): `van-den-dungen-bridge-theorist` (Axis-A NCG-submersion / Kasparov-bridge axis; distinct from connes-ncg's axiomatic-NCG axis per axis-distinctness clause) + `volovik-superfluid-universe-theorist` (Axis-B substrate-physics; cross-checks the bi-chirality grading's superfluid-analog at 3He-A vs 3He-B chirality decomposition — superfluid 3He-A has a chirality structure that maps interestingly to bi-chirality direct-sum decomposition).

### 5. Hypothesis

**Hypothesis statement (PASS)**: The candidate (a) bi-chirality grading `γ_9' = γ_5 ⊕ γ_F` defines a STRUCTURALLY VALID spectral triple `(A_K, H_K, D_K, γ_9', J)` distinct from §VII.AQ.OP-PROJ's tensor-product chirality. Specifically: (i) all 7 NCG axioms + Poincaré duality satisfied under direct-sum grading (with axiom 5' verified at `J γ_9' = -γ_9' J` modified-sign relation); (ii) KO-dim well-defined under bi-chirality (computed value pinned via the modified `(ε, ε', ε'')` signs per Connes 1996 reconstruction); (iii) substrate-IS observables on the bi-chirality spectral triple have a Connes-Karoubi pairing (Element-3 bridge map identified) to laboratory-IN observables (joint-probe `(η_{γ_5}, η_{γ_F})` in 3He-B BdG under independent-chirality-axis decomposition); (iv) Level-3 empirical anchor extractable on L_max=12 spectrum cache; (v) the bi-chirality cocycle's chirality split DIFFERS from the §VII.AQ.OP-PROJ tensor-product chirality's 78080:78080 cancellation (predicted: NOT uniform 8d:8d per-sector — bi-chirality gives 4 sectors `(+,+), (+,-), (-,+), (-,-)` with non-uniform cardinality per (p,q)).

**Hypothesis statement (FAIL alternatives)**: one or more of axiom 5' (chirality anticommutation), axiom 3 (J commutation/anticommutation under modified chirality), axiom 6 (orientability under direct-sum), axiom 7 (Poincaré duality / finiteness) FAIL under direct-sum grading; OR KO-dim is ambiguous/multivalued under bi-chirality; OR no Connes-Karoubi pairing exists (Element-3 bridge map undefined); OR no Level-3 empirical anchor extractable at L_max=12. Any of these closes the candidate (a) bi-chirality branch as structurally rejected.

### 6. Method (complete dispatch prompt for connes-ncg-theorist; PARALLEL with §W7-2b)

```
Dispatch prompt for connes-ncg-theorist (parallel with §W7-2b):

You are dispatched as primary author for gate
S91-VII-AT-OP-PROJ-7-AXIOM (T2.22 part 1; PARALLEL with §W7-2b
S91-VII-AW-OP-PROJ-7-AXIOM-COLOURED).

Substrate framing: §VII.AT.OP-PROJ's substrate IS a NEW spectral
triple (A_K, H_K, D_K, γ_9' = γ_5 ⊕ γ_F, J) distinct from
§VII.AQ.OP-PROJ. The bi-chirality grading γ_9' modifies the
chirality axis (γ_9 → γ_9'). NEW substrate ⇒ new substrate-IS
observables ⇒ new §VII registry slot at §VII.AT.OP-PROJ. The
chirality grading IS substrate-IS structural data (NOT a convention
choice).

DELIVERABLES:

(D1) Producing script:
     computations/session-91/s91_w7_2a_vii_at_op_proj_7_axiom.py
     - Loads s84_spectrum_cache_L12_tau019.npz at L_max=12
     - Constructs bi-chirality operator γ_9' = γ_5 ⊕ γ_F on H_K via
       direct-sum decomposition of the 32-dim chirality fiber:
         γ_5 acts on the spacetime spinor 4-dim chirality sub-space
         γ_F acts on the finite-sector 8-dim chirality sub-space
       Direct-sum decomposition: H_K = H_K^{γ_5+,γ_F+} ⊕
         H_K^{γ_5+,γ_F-} ⊕ H_K^{γ_5-,γ_F+} ⊕ H_K^{γ_5-,γ_F-}
       (4 sectors via joint (γ_5, γ_F) eigenvalue assignment)
     - Per-axiom verification subroutines for each of axioms 1-7 +
       Poincaré duality under γ_9' direct-sum grading:
         axiom 1 (dimension): spectrum growth rate unchanged
           (chirality grading doesn't affect spectrum)
         axiom 2 (regularity): [D_K, a] bounded — unchanged
         axiom 3 (reality): test J D_K = D_K J — unchanged
         axiom 4 (first-order): [[D_K, a], b^o] = 0 — unchanged
         axiom 5' (chirality MODIFIED): verify {D_K, γ_9'} = 0 where
           γ_9' = γ_5 ⊕ γ_F (direct sum); compare against the
           tensor-product axiom 5: {D_K, γ_5 ⊗ γ_F} = 0
         axiom 5' J-anticommutation: verify J γ_9' = ε_J γ_9' J for
           sign ε_J = -1 per Connes 1996 KO-dim=6 BDI class (or
           recompute if KO-dim shifts under direct-sum grading)
         axiom 6 (orientability): verify orientability cocycle on
           bi-chirality grading
         axiom 7 (finiteness + Poincaré duality): verify K-theory
           pairing K_0(A_K) × K_0(A_K^o) → ℤ under γ_9' grading
       Each axiom returns PASS/FAIL/INFO + (if FAIL) algebraic
       obstruction characterization
     - Compute KO-dim under bi-chirality direct-sum grading:
         signs (ε, ε', ε'') per (J^2, J D_K, J γ_9' relations)
         classification mod 8 per Connes 1996 reconstruction
         compare against §VII.AQ.OP-PROJ KO-dim = 6 (BDI class)
     - Compute cocycle cardinality per 4-sector decomposition
       (+,+), (+,-), (-,+), (-,-) at L_max=12:
         predicted: NOT uniform 8d:8d per-sector
         predicted: breaks the 78080:78080 cancellation diagnosed
           at S89 §W2-5 (the CF-A40 FAIL)
       Output cardinality_per_sector array shape (4, num_pq_sectors)
     - Element-3 bridge map identification: test candidate maps
       (HKR, K-theory boundary, Connes-Karoubi pairing under
       bi-chirality grading); for each, return PASS/FAIL on
       "bridge map well-defined under axiom 5' modified-sign relation"
     - Element-4 algebraic envelope classification per
       `cross-pillar-bridge-anatomy.md §"Level-2 sub-class (binding
       vs non-binding)"`: Level-2-binding if HKR-image binds Level-1
       cohomology class; Level-2-non-binding if bare-decomposition
       convergence rate not bridging laboratory-IN
     - Element-5 empirical anchor extraction at L_max=12: numerical
       evaluation of the bi-chirality cocycle (η_{γ_9'}, GV_{γ_9'})
       on the spectrum cache; output Δ_GV_bi-chirality scalar pin
     - SCHEMATIC-vs-FULL pin: CLASS=FULL for the axiomatic
       derivation (closed-form on substrate algebra A_K, NOT a
       SCHEMATIC analog); convention=...-FULL-CONNES-1996-BICHIRALITY;
       no -SCHEMATIC suffix per `substrate-first-canonical-sourcing.md
       §(iv)` K=4 MANDATORY level-pin.

(D2) Working-paper section in
     sessions/archive/session-91/session-91-w7-workingpaper.md §W7-2a
     >15 lines; substantive content per `agent-standards.md §"Completion
     Verification"`; substrate-framing reminder + 5-anatomy IS-not-IN
     declaration (substrate-IS = bi-chirality cocycle on the new
     spectral triple at §VII.AT.OP-PROJ; laboratory-IN = (η_{γ_5},
     η_{γ_F}) joint-probe in 3He-B BdG sector under independent-chirality
     decomposition; bridge map = identified per (D1) Element-3
     subroutine; algebraic envelope = Level-2-binding or non-binding
     per (D1); empirical anchor = Δ_GV_bi-chirality scalar at L_max=12).

(D3) Verdict line in
     computations/session-91/s91_gate_verdicts.txt
     S91-VII-AT-OP-PROJ-7-AXIOM: PASS|FAIL|INFO
       -- value=<axioms_pass_count>/7+poincare_duality_status
       scheme=bi-chirality-direct-sum
       convention=substrate-distance-1-FULL-CONNES-1996-BICHIRALITY
       L_max=12
       audit_sha256=<64-hex>
       content_sha256=<64-hex>
       schema_version=S87+

     Dual-SHA companion comment row (W9a-99 split).

(D4) §VII.AT.OP-PROJ registry-entry update at
     sessions/permanent-results-registry.md line 17237
     [DELEGATED TO mack-cosmic-bridge sole-writer per
     `feedback_mack-bridge-role.md`]:
     - If PASS: STAGE-0-CANDIDATE → STAGE-1-CANDIDATE (5-anatomy
       completion); populate Element-1 through Element-5 from (D1)
       outputs; declare KO-dim value; declare Level-2 sub-class;
       cite this gate's audit_sha256 as the substrate-physics
       derivation anchor.
     - If FAIL: STAGE-0-CANDIDATE retained; populate "FAIL diagnostic"
       block citing the FAILing axiom(s) + algebraic obstruction; close
       candidate (a) bi-chirality branch.
     - If INFO: STAGE-0-CANDIDATE retained; populate partial 5-anatomy
       with FAILing element(s) flagged; queue S92+ follow-up for the
       missing/ambiguous element(s).
     [The mack-cosmic-bridge dispatch is a SEPARATE W8 gate per the
     mack-bridge-role rule; this T2.22a gate produces the substrate-
     physics derivation outputs that mack consumes.]

FORBIDDEN actions per `v3-closure-recovery.md §PROHIBITED_ACTIONS`:
- Convention-shopping: do NOT switch from bi-chirality to a different
  chirality convention to reach PASS; the chirality grading is
  pre-registered at §VII.AT.OP-PROJ Element-1 specification.
- Iterate-until-PASS: do NOT modify the direct-sum decomposition to
  reach PASS on a FAILing axiom; the decomposition is pre-registered.
- Post-hoc threshold editing: axioms 1-7 + Poincaré duality are
  pinned per §9; do NOT loosen any axiom check.
- Ansatz-forced PASS: do NOT hardcode the predicted cardinality
  pattern into the comparison; compute it from the bi-chirality
  decomposition of the L_max=12 spectrum.
```

### 7. Machinery pin (PRDR)

| Pin | Value | Source |
|:----|:------|:-------|
| `N_eval` | 4 sectors × ~78080 chirality-fiber-dim eigenvalues at L_max=12 = ~312320 per-sector cardinality assignments + 7 axiom checks × per-axiom subroutine | derived; pin |
| `L_max` | 12 (operational); 10 (canonical_constants pin baseline) | `s84_spectrum_cache_L12_tau019.npz`; Casimir-bound truncation per `math-scripts.md §"D_K Block-Diagonality"` |
| `scan_range` | Per-axiom verification across all 7 NCG axioms + Poincaré duality + KO-dim computation + Element-3 bridge map candidate set {HKR, K-theory boundary, Connes-Karoubi} | pre-registered |
| `step_size` | N/A (discrete axiom checks + discrete bridge-map candidate set) | — |
| `tolerance` | Machine epsilon (`1e-12`) for axiom anticommutation/commutation residuals; ABSOLUTE tolerance for cocycle cardinality (integer-valued; tolerance 0) | per `gate-verdicts.md §"S87+ canonical form"` precision pin |
| `scheme` | `bi-chirality-direct-sum` | NEW scheme tag (registry-pre-registered at §VII.AT.OP-PROJ Element-1) |
| `convention` | `substrate-distance-1-FULL-CONNES-1996-BICHIRALITY` | NEW convention tag; FULL physical Connes 1996 reconstruction theorem application under direct-sum chirality grading; no SCHEMATIC suffix per K=4 MANDATORY level-pin discipline |
| `random_seed` | N/A (deterministic) | — |
| `GPU path` | NumPy CPU (per-(p,q) sector block-diagonal; chirality fiber 32-dim direct-sum decomposition fits comfortably in 17.1 GB VRAM at the largest single block) | per `math-scripts.md §"Environment"`; OMP_NUM_THREADS=8 |
| `CLASS pin` | `FULL` (NOT SCHEMATIC) | `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY level-pin |
| `tier_pin` | `TIER-1` (FULL physical Connes 1996 reconstruction; closed-form algebraic axiom verification on substrate algebra) | — |
| `precision` | float64 throughout; complex128 for J operator | — |

**Input SHA-256 pins**:

| File | Path | SHA | Source |
|:-----|:-----|:----|:-------|
| L_max=12 spectrum cache | `computations/session-84/s84_spectrum_cache_L12_tau019.npz` | `<pinned at dispatch>` | S84 W2 D_K-canonical compute |
| canonical_constants module | `computations/_shared/canonical_constants.py` | `<pinned at dispatch>` | post-S91 W0 housekeeping |
| §VII.AT.OP-PROJ registry entry stub | `sessions/permanent-results-registry.md` line 17237 | `<pinned at dispatch>` | S90 W7 CF-45 mack-cosmic-bridge sole-writer landing |
| Slot-allocation lockfile | `sessions/framework/s90-slot-pre-allocation-lockfile.md` | `<pinned at dispatch>` | S90 W7 CF-45 RESERVED-FOR-WORKSHOP-W7-CF-45-VII-AT allocation |
| Connes 1996 reconstruction theorem reference | `researchers/Connes/connes-1996-noncommutative-geometry-reconstruction-theorem.md` (or equivalent transcribed source under `researchers/Connes/`) | `<pinned at dispatch>` | static; precompute at plan-freeze |

**Audit-SHA closure**: `audit_sha256 = closure_hash(ordered-input-pin-map)`; per `_script_template.py` `append_verdict()` canonical pattern.

### 8. Expected output 4-tuple

`(value=<axioms_pass_count>/7 + poincare_duality_status, scheme=bi-chirality-direct-sum, convention=substrate-distance-1-FULL-CONNES-1996-BICHIRALITY, L_max=12)`

Output file contents (`s91_w7_2a_vii_at_op_proj_7_axiom.npz` + `.png` + `.json` sidecar):

- `axioms_pass_status`: shape (7,); bool; PASS/FAIL per axiom 1-7
- `poincare_duality_status`: bool; PASS/FAIL
- `axiom_5_prime_residual`: float64; `||{D_K, γ_9'}||` norm (expect 0 to machine epsilon if PASS)
- `J_gamma9prime_commutation_sign`: int (-1 or +1); the sign ε_J in `J γ_9' = ε_J γ_9' J`
- `KO_dim_under_bichirality`: int (expected 6 if PASS, else shifted mod 8)
- `KO_dim_signs_eps_eps_prime_eps_doubleprime`: shape (3,); int triplet (ε, ε', ε'') per Connes 1996 reconstruction
- `cardinality_per_sector_per_pq`: shape (4, num_pq_sectors); int; 4 sectors `(+,+), (+,-), (-,+), (-,-)` × per-(p,q) cardinality
- `chirality_split_78080_78080_status`: string; "PRESERVED" or "BROKEN"; whether the §VII.AQ.OP-PROJ tensor-product 78080:78080 cancellation persists under bi-chirality
- `bridge_map_candidate_status`: dict; per-candidate {HKR, K-theory boundary, Connes-Karoubi} PASS/FAIL/INFO
- `level_2_sub_class`: string; "binding", "non-binding", or "undeclared" per `cross-pillar-bridge-anatomy.md §"Level-2 sub-class (binding vs non-binding)"`
- `delta_GV_bichirality`: float64; Level-3 empirical anchor scalar
- `verdict_composite`, `sign_verdict`, `magnitude_verdict`, `regime_verdict` strings
- `audit_sha256`, `content_sha256` 64-hex
- `runtime_seconds` float

### 9. PASS / FAIL / INFO thresholds

**PASS**: ALL of (i) all 7 NCG axioms PASS at machine epsilon (axiom 5' residual `||{D_K, γ_9'}|| < 1e-12`; axiom 3 residual `||J D_K - D_K J|| < 1e-12`); (ii) Poincaré duality PASS (K-theory pairing well-defined under γ_9'); (iii) KO-dim well-defined (single value, mod 8 classification unambiguous); (iv) at least ONE bridge-map candidate (HKR or K-theory boundary or Connes-Karoubi) PASS for Element-3; (v) Level-2 sub-class declared (binding or non-binding, not "undeclared"); (vi) Level-3 empirical anchor extractable at L_max=12 (scalar `delta_GV_bichirality` computed without numerical breakdown).

Composite PASS ⇒ §VII.AT.OP-PROJ STAGE-0-CANDIDATE → STAGE-1-CANDIDATE eligible for promotion.

**INFO**: 6/7 NCG axioms PASS AND Poincaré duality PASS AND KO-dim well-defined; the 1 FAILing axiom is either axiom 5' (chirality anticommutation FAIL by structural sign-discrepancy in the direct-sum) OR axiom 6 (orientability ambiguous under direct-sum) — interpretation: substrate-physics derivation incomplete; STAGE-0-CANDIDATE retained; the FAILing axiom's structural reason is informative for the candidate (a) bi-chirality structural status. OR all axioms 1-7 PASS but Element-3 bridge map identification ambiguous (multiple candidates compete; INFO band activated).

**FAIL**: ≥2 NCG axioms FAIL; OR Poincaré duality FAIL; OR KO-dim multivalued / undefined; OR ALL three Element-3 bridge map candidates FAIL; OR Level-3 empirical anchor extraction breaks down at L_max=12 (NaN or Inf in `delta_GV_bichirality`); OR `regime_verdict = BREAKDOWN`.

Composite FAIL ⇒ candidate (a) bi-chirality branch closed structurally; §VII.AT.OP-PROJ retains STAGE-0-CANDIDATE with FAIL diagnostic populated.

**Tolerance rule**: THEOREM (machine-epsilon axiom checks; structural PASS/FAIL on axiom-by-axiom basis); ABSOLUTE for Element-3 bridge-map candidate evaluation; integer-valued for cardinality split.

**Publication precision**: machine-epsilon publication for axiom residuals; 14-sig-fig float64 publication for `delta_GV_bichirality` scalar pin; integer publication for KO-dim and cardinality.

### 10. Substitution chain ([VERIFY-THEOREM])

Pre-registered substitution chain for axiom 5' modification under direct-sum chirality:

**Step 1 (Definitions)**:
- `γ_9 = γ_5 ⊗ γ_F`: §VII.AQ.OP-PROJ tensor-product chirality (registered KO-dim=6 BDI class with anticommutation sign `J γ_9 = -γ_9 J` per Connes 1996 ε_J = -1)
- `γ_9' = γ_5 ⊕ γ_F`: candidate (a) bi-chirality direct-sum grading
- `H_K = H_K^{γ_5+,γ_F+} ⊕ H_K^{γ_5+,γ_F-} ⊕ H_K^{γ_5-,γ_F+} ⊕ H_K^{γ_5-,γ_F-}`: 4-sector direct-sum Hilbert decomposition under (γ_5, γ_F) joint eigenvalue assignment

**Step 2 (Substitution into axiom 5)**:

Standard axiom 5 (tensor product): `{D_K, γ_9} = D_K · (γ_5 ⊗ γ_F) + (γ_5 ⊗ γ_F) · D_K = 0`

Modified axiom 5' (direct sum): `{D_K, γ_9'} = D_K · (γ_5 ⊕ γ_F) + (γ_5 ⊕ γ_F) · D_K`

The direct-sum action `γ_5 ⊕ γ_F` decomposes as block-diagonal:

```
γ_9' = | γ_5   0  |
       |  0   γ_F |
```

Applied to a state `ψ = ψ_5 + ψ_F` in the direct-sum decomposition: `γ_9' ψ = γ_5 ψ_5 + γ_F ψ_F`.

**Step 3 (Simplification — sector-level anticommutation)**:

`{D_K, γ_9'} ψ = D_K(γ_5 ψ_5 + γ_F ψ_F) + (γ_5 ⊕ γ_F)(D_K ψ_5 + D_K ψ_F) = (D_K γ_5 + γ_5 D_K) ψ_5 + (D_K γ_F + γ_F D_K) ψ_F`

For axiom 5' to PASS at machine epsilon, we need:
- `{D_K, γ_5}|_{ψ_5} = 0` (anticommutation on γ_5-decomposed sector)
- `{D_K, γ_F}|_{ψ_F} = 0` (anticommutation on γ_F-decomposed sector)

The first holds IFF `D_K` acts on `ψ_5` in a manner anticommuting with the spacetime chirality γ_5; the second holds IFF `D_K` acts on `ψ_F` anticommuting with the finite-sector chirality γ_F. These are SEPARATE anticommutation conditions; the tensor-product axiom 5 conflates them into a single anticommutation `{D_K, γ_5 ⊗ γ_F} = 0`.

**Step 4 (Direction-prediction)**:

The substrate's standard `D_K` is constructed to satisfy `{D_K, γ_5 ⊗ γ_F} = 0` (axiom 5 for tensor-product chirality). The bi-chirality axiom 5' requires the STRONGER joint condition `{D_K, γ_5}|_{ψ_5} = 0 AND {D_K, γ_F}|_{ψ_F} = 0`, which is a more restrictive constraint than the tensor-product condition. Predicted: axiom 5' is more likely to FAIL than PASS at the canonical `D_K` because the joint sector-anticommutation is generically over-determined.

**Conservative direction prediction**: axiom 5' is MORE LIKELY to FAIL than PASS; the workshop expected this outcome at S89 W-5 R2 verdict freeze (workshop transcript). The W7-2a gate is the substrate-physics test of whether the canonical `D_K` satisfies the over-determined joint anticommutation IN SPITE of the additional restrictiveness.

**Step 5 (Conclusion)**:

Sign_verdict prediction PASS = "axiom 5' residual is small but non-zero (machine epsilon noise)"; FAIL = "axiom 5' residual is structurally non-zero (above 1e-12 threshold)". The W7-2a gate decides the direction empirically at L_max=12.

### 11. Solution-space interpretation

**PASS corridor**: candidate (a) bi-chirality is structurally viable; §VII.AT.OP-PROJ promotes to STAGE-1-CANDIDATE with full 5-anatomy populated; the candidate-(a) alternative to §VII.AQ.OP-PROJ tensor-product chirality is a parallel valid spectral-triple registration. Forward: Stage-2 cross-axis verify queued at W8 (per `joint-theorem-promotion.md §"Stage 2"`); STAGE-3-PERMANENT eligible upon Stage-2 PASS-AND.

**FAIL corridor**: candidate (a) bi-chirality closes structurally; §VII.AT.OP-PROJ remains STAGE-0-CANDIDATE with FAIL diagnostic; the S89 §W2-5 CF-A40 FAIL's alternative-chirality re-scope is partially resolved (one of the three candidates eliminated). Forward: candidate (b) SU(3)-coloured chirality at §VII.AW.OP-PROJ (§W7-2b parallel gate) and candidate (c) inner-fluctuation at §VII.AQ.OP-PROJ (T2.21) remain as the surviving CF-A40 re-scope candidates.

**INFO corridor**: substrate-physics derivation partially complete; 6/7 axioms PASS or ambiguous KO-dim or Element-3 ambiguous; §VII.AT.OP-PROJ retains STAGE-0-CANDIDATE with specific element flagged for S92+ resolution.

### 12. Effort

**~0.85 wave-equivalent** (~5-7 hours of connes-ncg-theorist dispatch time):
- Bi-chirality operator construction + direct-sum decomposition: ~1 hour
- Per-axiom verification subroutines (7 axioms + Poincaré duality + KO-dim): ~3 hours
- Element-3 bridge map candidate evaluation (HKR, K-theory boundary, Connes-Karoubi): ~1 hour
- Element-4 + Element-5 derivation and anchor extraction: ~1 hour
- Working-paper section + verdict line: ~1 hour

Parallel with §W7-2b; combined ~1.7 wave-equivalents.

### 13. Substrate-framing reminder

§VII.AT.OP-PROJ's substrate IS a NEW spectral triple `(A_K, H_K, D_K, γ_9' = γ_5 ⊕ γ_F, J)` STRUCTURALLY DISTINCT from §VII.AQ.OP-PROJ's tensor-product chirality. The substrate IS spectral triple — modifying any of (A, H, D, γ, J) IS a new substrate registering at a NEW §VII slot (§VII.AT.OP-PROJ). Direction of explanation: substrate IS spectral triple → chirality-grading modification IS new-spectral-triple → new substrate-IS observables → new §VII slot. Container-thinking violation FORBIDDEN: "we choose between chirality conventions on a single underlying spectral triple" — INVERT: "each chirality grading IS a structurally distinct spectral triple at a separate §VII slot; the candidate (a) bi-chirality at §VII.AT.OP-PROJ IS a different substrate, NOT a convention choice on the §VII.AQ.OP-PROJ substrate" (per §VII.AT.OP-PROJ registry substrate framing block at registry line 17287).

---

## §W7-2b. S91-VII-AW-OP-PROJ-7-AXIOM-COLOURED (T2.22 part 2) [PARALLEL with §W7-2a]

### 1. Gate ID

`S91-VII-AW-OP-PROJ-7-AXIOM-COLOURED`

Provenance: S91 W7 carry-forward T2.22 part 2 = §VII.AW.OP-PROJ STAGE-0-CANDIDATE-PENDING-S91-SUBSTRATE-PHYSICS substrate-physics derivation (registry entry at line 17293; S91+ DEFERRED COMPUTATION block at registry lines 17317-17324 enumerates the 6-item work for SU(3)-coloured chirality per Connes-Marcolli 2008 §11 framework).

### 2. Trigger

`[VERIFY-THEOREM]` + `[VERIFY]` — substrate-physics derivation requires axiomatic theorem verification (7 NCG axioms + Poincaré duality under SU(3)-coloured chirality grading `γ_9'' = γ_F^c` per Connes-Marcolli 2008 §11) plus numerical empirical anchor verification (colour-axis-resolved cocycle evaluation on L_max=12 spectrum cache).

### 3. Classification

**GEOMETRIC** (substrate-IS structural property of a NEW spectral triple structurally distinct from §VII.AQ.OP-PROJ AND §VII.AT.OP-PROJ; the SU(3)-coloured chirality grading IS a structurally distinct spectral triple with colour-axis-resolved chirality decomposition of the `M_3(ℂ)` summand per Connes-Marcolli 2008 §11 framework — direction of explanation: each chirality grading IS a structurally distinct substrate per §VII.AW.OP-PROJ registry entry substrate framing block at line 17335).

### 4. Agent type

**Primary author**: `connes-ncg-theorist`

Rationale: SU(3)-coloured chirality grading `γ_F^c` per Connes-Marcolli 2008 §11 is canonically the NCG-axiomatic domain; `connes-ncg-theorist` owns the Connes-Marcolli 2008 framework (this is the canonical NCG Standard Model treatise), the colour-axis decomposition of the `M_3(ℂ)` summand into colour-tagged chirality sectors `(r, g, b) × (+, -)`, the J commutation/anticommutation calculus under colour-dressed grading (axiom 3 + KO-dim mod 8 classification with the modified sign relation `J γ_9'' = ε γ_9'' J`), and the Poincaré duality under colour-resolved K-theory pairing.

**FORBIDDEN test-case agent type**: `gen-physicist` (per spawn-prompt).

Stage-2-style cross-axis confirmation routing (forward; queued for W8 on PASS): `van-den-dungen-bridge-theorist` (Axis-A NCG-submersion / Kasparov-bridge axis; specifically the Connes-Marcolli 2008 §11 SU(3)-coloured chirality framework is cross-checked at the K-theory submersion axis via van-den-dungen-bridge's domain expertise) + `volovik-superfluid-universe-theorist` (Axis-B substrate-physics; SU(3)-coloured chirality has an analog at the 3He-A vs 3He-B colour-axis-decomposition that volovik-superfluid-universe specifically owns).

### 5. Hypothesis

**Hypothesis statement (PASS)**: The candidate (b) SU(3)-coloured chirality grading `γ_9'' = γ_F^c` per Connes-Marcolli 2008 §11 defines a STRUCTURALLY VALID spectral triple `(A_K, H_K, D_K, γ_9'', J)` distinct from §VII.AQ.OP-PROJ tensor-product chirality AND §VII.AT.OP-PROJ bi-chirality direct-sum. Specifically: (i) all 7 NCG axioms + Poincaré duality satisfied under SU(3)-coloured grading per Connes-Marcolli 2008 §11 framework; (ii) KO-dim computed under SU(3)-coloured chirality (predicted: KO-dim shift mod 8 dependent on the J anticommutation sign ε per Connes-Marcolli 2008 §11); (iii) Element-3 bridge map identified (Connes-Marcolli 2008 §11 framework cites HKR at colour-dressed grading and K-theory boundary with SU(3)-colour-axis decomposition); (iv) Level-3 empirical anchor extractable on L_max=12 with colour-tagged cocycle observables (`GV_{γ_F^c}` per colour-tagged sector); (v) the colour-axis decomposition produces 9 colour-tagged sectors per (p,q) rather than uniform 8d:8d cancellation of §VII.AQ.OP-PROJ — predicted: breaks the 78080:78080 cancellation in a colour-axis-resolved manner distinct from §VII.AT.OP-PROJ's 4-sector direct-sum.

**Hypothesis statement (FAIL alternatives)**: KO-dim shift mod 8 is structurally inconsistent (KO-dim ambiguous or multivalued under colour-dressing); OR axiom 5'' (modified chirality anticommutation `{D_K, γ_9''} = 0` under colour-dressing) FAILs; OR axiom 3 J commutation/anticommutation under colour-dressed γ_9'' FAILs with no sign ε satisfying the consistency conditions; OR Connes-Marcolli 2008 §11 bridge-map class is undefined at L_max=12 truncation; OR Level-3 empirical anchor breaks numerically. Any of these closes the candidate (b) SU(3)-coloured branch as structurally rejected.

### 6. Method (complete dispatch prompt for connes-ncg-theorist; PARALLEL with §W7-2a)

```
Dispatch prompt for connes-ncg-theorist (parallel with §W7-2a):

You are dispatched as primary author for gate
S91-VII-AW-OP-PROJ-7-AXIOM-COLOURED (T2.22 part 2; PARALLEL with
§W7-2a S91-VII-AT-OP-PROJ-7-AXIOM).

Substrate framing: §VII.AW.OP-PROJ's substrate IS a NEW spectral
triple (A_K, H_K, D_K, γ_9'' = γ_F^c, J) STRUCTURALLY DISTINCT from
§VII.AQ.OP-PROJ tensor-product chirality AND §VII.AT.OP-PROJ
bi-chirality. The SU(3)-coloured chirality γ_9'' = γ_F^c per
Connes-Marcolli 2008 §11 refines the finite-sector chirality γ_F by
attaching a colour-axis label to each chirality eigenstate, producing
a finer decomposition of the M_3(ℂ) summand than the colour-blind
tensor product γ_9 = γ_5 ⊗ γ_F. The colour-axis IS substrate-IS
(intrinsic to the M_3(ℂ) summand's representation theory), NOT a
label imposed FROM OUTSIDE the substrate.

DELIVERABLES:

(D1) Producing script:
     computations/session-91/s91_w7_2b_vii_aw_op_proj_7_axiom_coloured.py
     - Loads s84_spectrum_cache_L12_tau019.npz at L_max=12
     - Constructs SU(3)-coloured chirality operator γ_9'' = γ_F^c on
       H_K via colour-axis decomposition of the M_3(ℂ) summand:
         γ_F^c acts on the colour-tagged chirality eigenstates
           (r, +), (r, -), (g, +), (g, -), (b, +), (b, -)
         The colour-axis is the SU(3) ⊃ {r, g, b} fundamental
           representation acting on M_3(ℂ)
         The chirality assignment is per Connes-Marcolli 2008 §11
           framework (colour-dressed chirality grading on the finite
           sector)
       Per-(p,q) sector decomposition: each Peter-Weyl block
       decomposes into 9 colour-tagged sub-blocks `(c1, c2)` for
       c1, c2 ∈ {r, g, b} via the SU(3) ⊗ SU(3)^* decomposition of
       M_3(ℂ)
     - Per-axiom verification subroutines for each of axioms 1-7 +
       Poincaré duality under γ_9'' colour-dressed grading per
       Connes-Marcolli 2008 §11:
         axiom 1 (dimension): spectrum growth rate unchanged
         axiom 2 (regularity): [D_K, a] bounded under colour-axis
           decomposition of a ∈ A_K
         axiom 3 (reality): test J D_K = D_K J
         axiom 4 (first-order): [[D_K, a], b^o] = 0 — but under
           colour-axis decomposition; verify on coloured generators
         axiom 5'' (chirality MODIFIED): verify {D_K, γ_9''} = 0
           where γ_9'' = γ_F^c (colour-dressed); compare against
           axiom 5: {D_K, γ_5 ⊗ γ_F} = 0
         axiom 5'' J-commutation: verify J γ_9'' = ε γ_9'' J for
           sign ε per Connes-Marcolli 2008 §11 framework; ε is the
           KO-dim-shift-determining sign (predicted: ε may shift from
           -1 to +1 under colour-dressing, producing KO-dim shift
           from 6 to 2 mod 8)
         axiom 6 (orientability): verify orientability cocycle on
           colour-dressed chirality
         axiom 7 (finiteness + Poincaré duality): verify K-theory
           pairing K_0(A_K) × K_0(A_K^o) → ℤ under γ_9'' grading;
           per Connes-Marcolli 2008 §11 the colour-dressing may
           refine the K-theory pairing structure
       Each axiom returns PASS/FAIL/INFO + (if FAIL) algebraic
       obstruction characterization
     - Compute KO-dim under SU(3)-coloured chirality grading:
         signs (ε, ε', ε'') per (J^2, J D_K, J γ_9'' relations)
         classification mod 8 per Connes-Marcolli 2008 §11
         compare against §VII.AQ.OP-PROJ KO-dim = 6 (BDI class) AND
           §VII.AT.OP-PROJ KO-dim (from §W7-2a output)
     - Compute colour-tagged cocycle cardinality per 9-sector
       decomposition `(c1, c2) ∈ {r, g, b}^2` at L_max=12:
         predicted: NOT uniform per-sector
         predicted: breaks the 78080:78080 cancellation in a
           STRUCTURALLY DIFFERENT manner from §VII.AT.OP-PROJ
           bi-chirality 4-sector decomposition
       Output colour_tagged_cardinality_per_pq array shape
       (9, num_pq_sectors)
     - Element-3 bridge map identification per Connes-Marcolli 2008
       §11: test candidate maps (HKR at colour-dressed grading,
       K-theory boundary with SU(3)-colour-axis decomposition,
       Connes-Karoubi pairing under colour-dressed axioms); for each,
       return PASS/FAIL on "bridge map well-defined under axiom 5''
       modified-sign relation per Connes-Marcolli 2008 §11"
     - Element-4 algebraic envelope classification per
       `cross-pillar-bridge-anatomy.md §"Level-2 sub-class"`:
       Level-2-binding if HKR-image binds Level-1 cohomology class
       under colour-dressing; non-binding otherwise
     - Element-5 empirical anchor extraction at L_max=12: numerical
       evaluation of the colour-tagged cocycle (η_{γ_F^c},
       GV_{γ_F^c}) per colour-tagged sector on the spectrum cache;
       output Δ_GV_SU(3)-coloured per-sector array shape (9,)
     - SCHEMATIC-vs-FULL pin: CLASS=FULL for the axiomatic
       derivation (Connes-Marcolli 2008 §11 framework closed-form on
       substrate algebra A_K); convention=...-FULL-CM2008-§11-COLOURED;
       no -SCHEMATIC suffix per K=4 MANDATORY level-pin discipline.

(D2) Working-paper section in
     sessions/archive/session-91/session-91-w7-workingpaper.md §W7-2b
     >15 lines; substantive content per `agent-standards.md §"Completion
     Verification"`; substrate-framing reminder + 5-anatomy IS-not-IN
     declaration (substrate-IS = colour-tagged cocycle on the new
     spectral triple at §VII.AW.OP-PROJ; laboratory-IN = colour-axis-
     resolved (η_{γ_F^c}, GV_{γ_F^c}) joint-probe in 3He-A chirality
     decomposition; bridge map = identified per (D1) Element-3
     subroutine + Connes-Marcolli 2008 §11 framework citation;
     algebraic envelope = Level-2-binding or non-binding per (D1);
     empirical anchor = Δ_GV_SU(3)-coloured per-sector array at
     L_max=12).

(D3) Verdict line in
     computations/session-91/s91_gate_verdicts.txt
     S91-VII-AW-OP-PROJ-7-AXIOM-COLOURED: PASS|FAIL|INFO
       -- value=<axioms_pass_count>/7+poincare_duality_status+KO_dim_value
       scheme=SU(3)-coloured-chirality
       convention=substrate-distance-1-FULL-CM2008-§11-COLOURED
       L_max=12
       audit_sha256=<64-hex>
       content_sha256=<64-hex>
       schema_version=S87+

     Dual-SHA companion comment row (W9a-99 split).

(D4) §VII.AW.OP-PROJ registry-entry update at
     sessions/permanent-results-registry.md line 17293
     [DELEGATED TO mack-cosmic-bridge sole-writer]:
     - If PASS: STAGE-0-CANDIDATE → STAGE-1-CANDIDATE (5-anatomy
       completion); populate Element-1 through Element-5 from (D1)
       outputs; declare KO-dim value (with shift annotation if mod 8
       shifted from 6); declare Level-2 sub-class; cite this gate's
       audit_sha256 as the substrate-physics derivation anchor.
     - If FAIL: STAGE-0-CANDIDATE retained; populate "FAIL diagnostic"
       block citing the FAILing axiom(s) + algebraic obstruction;
       close candidate (b) SU(3)-coloured branch.
     - If INFO: STAGE-0-CANDIDATE retained; populate partial 5-anatomy
       with FAILing element(s) flagged; queue S92+ follow-up.

FORBIDDEN actions per `v3-closure-recovery.md §PROHIBITED_ACTIONS`:
- Convention-shopping: do NOT switch from SU(3)-coloured chirality
  to a different colour-axis decomposition convention to reach PASS.
- Iterate-until-PASS: do NOT modify the colour-axis decomposition to
  reach PASS on a FAILing axiom.
- Post-hoc threshold editing: axioms 1-7 + Poincaré duality + KO-dim
  computation are pinned per §9.
- Ansatz-forced PASS: do NOT hardcode the predicted KO-dim shift or
  the predicted 9-sector cardinality pattern.
```

### 7. Machinery pin (PRDR)

| Pin | Value | Source |
|:----|:------|:-------|
| `N_eval` | 9 colour-tagged sectors × ~78080 chirality-fiber-dim eigenvalues at L_max=12 = ~702720 colour-axis-resolved cardinality assignments + 7 axiom checks × per-axiom subroutine | derived; pin |
| `L_max` | 12 (operational); 10 (canonical_constants pin baseline) | `s84_spectrum_cache_L12_tau019.npz`; Casimir-bound truncation |
| `scan_range` | Per-axiom verification across 7 NCG axioms + Poincaré duality + KO-dim + Element-3 bridge map candidate set; colour-axis decomposition into 9 colour-tagged sectors `(c1, c2) ∈ {r, g, b}^2` | pre-registered |
| `step_size` | N/A (discrete axiom + colour-tag enumeration) | — |
| `tolerance` | Machine epsilon (`1e-12`) for axiom residuals; ABSOLUTE for cocycle cardinality (integer-valued); KO-dim integer-valued tolerance 0 | per `gate-verdicts.md §"S87+ canonical form"` |
| `scheme` | `SU(3)-coloured-chirality` | NEW scheme tag (registry-pre-registered at §VII.AW.OP-PROJ Element-1) |
| `convention` | `substrate-distance-1-FULL-CM2008-§11-COLOURED` | NEW convention tag; FULL physical Connes-Marcolli 2008 §11 framework; no SCHEMATIC suffix per K=4 MANDATORY level-pin |
| `random_seed` | N/A | — |
| `GPU path` | NumPy CPU (per-(p,q) sector with 9-fold colour-axis decomposition; chirality fiber 32-dim × colour 9-fold = effective 288-fold per-(p,q) sub-block; still fits in 17.1 GB VRAM at largest block) | per `math-scripts.md §"Environment"`; OMP_NUM_THREADS=8 |
| `CLASS pin` | `FULL` (NOT SCHEMATIC) | `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY |
| `tier_pin` | `TIER-1` (FULL physical Connes-Marcolli 2008 §11 framework) | — |
| `precision` | float64 throughout; complex128 for J operator + SU(3) generators | — |

**Input SHA-256 pins**:

| File | Path | SHA | Source |
|:-----|:-----|:----|:-------|
| L_max=12 spectrum cache | `computations/session-84/s84_spectrum_cache_L12_tau019.npz` | `<pinned at dispatch>` | S84 W2 D_K-canonical compute |
| canonical_constants module | `computations/_shared/canonical_constants.py` | `<pinned at dispatch>` | post-S91 W0 housekeeping |
| §VII.AW.OP-PROJ registry entry stub | `sessions/permanent-results-registry.md` line 17293 | `<pinned at dispatch>` | S90 W7 CF-45 mack-cosmic-bridge sole-writer landing |
| Slot-allocation lockfile | `sessions/framework/s90-slot-pre-allocation-lockfile.md` | `<pinned at dispatch>` | S90 W7 CF-45 RESERVED-FOR-WORKSHOP-W7-CF-45-VII-AW allocation |
| Connes-Marcolli 2008 §11 framework reference | `researchers/Connes/connes-marcolli-2008-noncommutative-geometry-physics-motives.md` (or equivalent transcribed source under `researchers/Connes/`) | `<pinned at dispatch>` | static; precompute at plan-freeze |

**Audit-SHA closure**: `audit_sha256 = closure_hash(ordered-input-pin-map)`.

### 8. Expected output 4-tuple

`(value=<axioms_pass_count>/7 + poincare_duality_status + KO_dim_value, scheme=SU(3)-coloured-chirality, convention=substrate-distance-1-FULL-CM2008-§11-COLOURED, L_max=12)`

Output file contents (`s91_w7_2b_vii_aw_op_proj_7_axiom_coloured.npz` + `.png` + `.json` sidecar):

- `axioms_pass_status`: shape (7,); bool
- `poincare_duality_status`: bool
- `axiom_5_doubleprime_residual`: float64; `||{D_K, γ_9''}||` norm
- `J_gamma9doubleprime_sign`: int (-1, +1); the sign ε in `J γ_9'' = ε γ_9'' J`
- `KO_dim_under_su3_colouring`: int; expected may shift from 6 (predicted: 2 or 6 mod 8 dependent on ε)
- `KO_dim_shift_from_§VII_AQ`: int; (KO_dim_under_su3_colouring - 6) mod 8
- `KO_dim_signs_eps_eps_prime_eps_doubleprime`: shape (3,); int triplet
- `colour_tagged_cardinality_per_pq`: shape (9, num_pq_sectors); int; 9 sectors `(c1, c2)` × per-(p,q) cardinality
- `chirality_split_78080_78080_status_coloured`: string; "PRESERVED", "BROKEN-COLOUR-RESOLVED", or "BROKEN-OTHER"
- `bridge_map_candidate_status_coloured`: dict; per-candidate {HKR-coloured, K-theory-boundary-coloured, Connes-Karoubi-coloured} PASS/FAIL/INFO per Connes-Marcolli 2008 §11
- `level_2_sub_class`: string; "binding", "non-binding", or "undeclared"
- `delta_GV_su3_coloured_per_sector`: shape (9,); float64; Level-3 empirical anchor per colour-tagged sector
- `verdict_composite`, `sign_verdict`, `magnitude_verdict`, `regime_verdict` strings
- `audit_sha256`, `content_sha256` 64-hex
- `runtime_seconds` float

### 9. PASS / FAIL / INFO thresholds

**PASS**: ALL of (i) all 7 NCG axioms PASS at machine epsilon (axiom 5'' residual `||{D_K, γ_9''}|| < 1e-12`); (ii) Poincaré duality PASS under colour-dressed K-theory pairing; (iii) KO-dim well-defined (single value mod 8; ANY value, with shift annotation if shifted from 6); (iv) at least ONE Element-3 bridge map candidate PASS (HKR-coloured / K-theory-boundary-coloured / Connes-Karoubi-coloured) per Connes-Marcolli 2008 §11; (v) Level-2 sub-class declared (binding or non-binding); (vi) Level-3 empirical anchor extractable (`delta_GV_su3_coloured_per_sector` shape (9,) without NaN/Inf).

Composite PASS ⇒ §VII.AW.OP-PROJ STAGE-0-CANDIDATE → STAGE-1-CANDIDATE eligible.

**INFO**: 6/7 axioms PASS + Poincaré duality PASS + KO-dim well-defined; 1 FAILing axiom (likely axiom 5'' or axiom 3 J-commutation under colour-dressing) is informative for the candidate-(b) substrate-physics status; STAGE-0-CANDIDATE retained. OR all axioms PASS but KO-dim ambiguous between two mod-8 classes (e.g., the J anticommutation sign ε admits two consistent values producing distinct KO-dim assignments); diagnostic emitted + S92+ KO-dim disambiguation queued.

**FAIL**: ≥2 axioms FAIL; OR Poincaré duality FAIL under colour-dressed K-theory; OR KO-dim multivalued/undefined; OR ALL Element-3 bridge map candidates FAIL; OR Level-3 anchor extraction breaks; OR `regime_verdict = BREAKDOWN`.

Composite FAIL ⇒ candidate (b) SU(3)-coloured branch closed; §VII.AW.OP-PROJ retains STAGE-0-CANDIDATE with FAIL diagnostic.

**Tolerance rule**: THEOREM (machine-epsilon axiom checks; structural PASS/FAIL on axiom-by-axiom basis); ABSOLUTE for bridge-map candidate evaluation; integer-valued for cardinality and KO-dim.

**Publication precision**: machine-epsilon for axiom residuals; 14-sig-fig float64 for per-sector `delta_GV_su3_coloured` scalars; integer publication for KO-dim and cardinality.

### 10. Substitution chain ([VERIFY-THEOREM])

Pre-registered substitution chain for axiom 5'' modification under colour-dressed chirality:

**Step 1 (Definitions)**:
- `γ_9 = γ_5 ⊗ γ_F`: §VII.AQ.OP-PROJ tensor-product chirality
- `γ_9'' = γ_F^c`: candidate (b) SU(3)-coloured chirality per Connes-Marcolli 2008 §11
- `M_3(ℂ)`-summand decomposition: `M_3(ℂ) = ⊕_{c1, c2 ∈ {r,g,b}} E_{c1, c2}` where `E_{c1, c2}` is the matrix unit eigenstate of the colour-axis
- `H_K = ⊕_{(c1, c2) ∈ {r,g,b}^2} H_K^{(c1, c2)}` (9-sector colour-tagged Hilbert decomposition)
- `γ_F^c` action: on `H_K^{(c1, c2)}`, `γ_F^c = ε_{c1, c2} γ_F` where `ε_{c1, c2} ∈ {-1, +1}` is the colour-tagged chirality assignment per Connes-Marcolli 2008 §11 framework (the specific assignment depends on the colour-singlet vs colour-octet decomposition of `M_3(ℂ)` under SU(3))

**Step 2 (Substitution into axiom 5'')**:

`{D_K, γ_9''} = D_K · γ_F^c + γ_F^c · D_K`

Decomposing per colour-tagged sector: `{D_K, γ_9''}|_{(c1, c2)} = ε_{c1, c2} {D_K, γ_F}|_{(c1, c2)}`

For axiom 5'' to PASS at machine epsilon, we need `{D_K, γ_F}|_{(c1, c2)} = 0` for all 9 colour-tagged sectors. This is a more restrictive condition than the tensor-product axiom 5 (`{D_K, γ_5 ⊗ γ_F} = 0`); the colour-resolved anticommutation must hold per-sector.

**Step 3 (Simplification — KO-dim shift per Connes-Marcolli 2008 §11)**:

The J anticommutation sign relation under colour-dressing:

`J γ_9'' = ε γ_9'' J` where `ε ∈ {-1, +1}` per Connes-Marcolli 2008 §11.

The KO-dim under colour-dressing:
- If `J^2 = +1` AND `JD_K = D_K J` (axiom 3) AND `J γ_9'' = -γ_9'' J` (ε = -1): KO-dim = 6 (BDI; unchanged from §VII.AQ.OP-PROJ)
- If `J^2 = +1` AND `J γ_9'' = +γ_9'' J` (ε = +1): KO-dim shifts to 2 mod 8 (CI class per Connes-Marcolli 2008 §11)
- Other combinations of (J^2, JD_K, Jγ_9'') signs produce different KO-dim mod 8 assignments per Connes 1996 reconstruction

**Step 4 (Direction-prediction)**:

The substrate's standard `D_K` is constructed to satisfy `{D_K, γ_F} = 0` (tensor-product axiom 5 on the γ_F factor alone). Predicted: axiom 5'' PASSes IFF the per-colour-tagged-sector restriction of axiom 5 holds at machine epsilon — which is TRUE iff `D_K` does NOT mix colour-tagged sectors of `M_3(ℂ)` (i.e., `D_K` is colour-axis-preserving). Per the K=4 algebra-axis orthogonality classification, the substrate's `D_K` acts colour-axis-preservingly on `M_3(ℂ)` BY CONSTRUCTION (Connes-Chamseddine 1996 construction of the SM finite-sector Dirac operator).

**Conservative direction prediction**: axiom 5'' is MORE LIKELY to PASS than FAIL because the colour-axis-preserving construction of `D_K` is consistent with the per-sector restriction; the KO-dim under colour-dressing may shift from 6 to 2 mod 8 (Connes-Marcolli 2008 §11 framework prediction).

**Step 5 (Conclusion)**:

Sign_verdict prediction: axiom 5'' residual is small (PASS direction); axiom 3 J-commutation under colour-dressing may admit two solutions for ε producing KO-dim = 6 or KO-dim = 2 mod 8 (INFO direction if both are admissible); ALL 7 axioms expected to PASS if the colour-axis-preserving structure of `D_K` is preserved at L_max=12.

### 11. Solution-space interpretation

**PASS corridor**: candidate (b) SU(3)-coloured chirality is structurally viable per Connes-Marcolli 2008 §11; §VII.AW.OP-PROJ promotes to STAGE-1-CANDIDATE with full 5-anatomy populated; the candidate-(b) alternative to §VII.AQ.OP-PROJ tensor-product chirality is a parallel valid spectral-triple registration with colour-axis-resolved cocycle observables. The colour-axis-resolved chirality decomposition of `M_3(ℂ)` opens a parallel substrate-physics axis to §VII.AQ.OP-PROJ + §VII.AT.OP-PROJ; if KO-dim shifts from 6 to 2 mod 8 under colour-dressing, this is a structurally significant Connes-Marcolli 2008 §11 framework confirmation. Forward: Stage-2 cross-axis verify at W8.

**FAIL corridor**: candidate (b) SU(3)-coloured chirality closes structurally; §VII.AW.OP-PROJ remains STAGE-0-CANDIDATE with FAIL diagnostic. Combined with §W7-2a FAIL (if both close): the CF-A40 FAIL alternative-chirality re-scope is partially resolved by closing candidates (a) AND (b), leaving candidate (c) inner-fluctuation at §VII.AQ.OP-PROJ (T2.21) as the surviving CF-A40 branch.

**INFO corridor**: 6/7 axioms or KO-dim ambiguity (two consistent ε values); §VII.AW.OP-PROJ retains STAGE-0-CANDIDATE with specific element flagged for S92+ resolution. The KO-dim ambiguity is informative for the Connes-Marcolli 2008 §11 framework's structural status at L_max=12.

### 12. Effort

**~0.85 wave-equivalent** (~5-7 hours of connes-ncg-theorist dispatch time):
- SU(3)-coloured chirality operator construction + 9-fold colour-axis decomposition: ~1.5 hours
- Per-axiom verification subroutines (7 axioms + Poincaré duality + KO-dim with mod-8 classification): ~3 hours
- Element-3 bridge map candidate evaluation under Connes-Marcolli 2008 §11 framework: ~1 hour
- Element-4 + Element-5 derivation and per-sector anchor extraction: ~1 hour
- Working-paper section + verdict line: ~1 hour

Parallel with §W7-2a; combined ~1.7 wave-equivalents.

### 13. Substrate-framing reminder

§VII.AW.OP-PROJ's substrate IS a NEW spectral triple `(A_K, H_K, D_K, γ_9'' = γ_F^c, J)` STRUCTURALLY DISTINCT from §VII.AQ.OP-PROJ tensor-product chirality AND §VII.AT.OP-PROJ bi-chirality direct-sum. The colour-axis IS substrate-IS (intrinsic to the `M_3(ℂ)` summand's representation theory under SU(3)), NOT a label imposed FROM OUTSIDE the substrate. Direction of explanation: substrate IS spectral triple → colour-axis-resolved chirality grading IS new-spectral-triple → new substrate-IS observables (colour-axis-tagged cocycles) → new §VII slot. Container-thinking violation FORBIDDEN: "colour is a label we attach to chirality eigenstates" — INVERT: "the SU(3)-coloured chirality grading IS the substrate's intrinsic refinement of the chirality decomposition at the `M_3(ℂ)` summand; the colour-axis IS substrate-IS structural data, NOT a label imposed FROM OUTSIDE" (per §VII.AW.OP-PROJ registry substrate framing block at registry line 17335).

---

## §W7-3. S91-W7-CF-W7-5-CF-54-ROUTE-C-IN-CACHE-REGRESSION-LMAX-16 (T2.23)

### 1. Gate ID

`S91-W7-CF-W7-5-CF-54-ROUTE-C-IN-CACHE-REGRESSION-LMAX-16`

Provenance: S91 W7 carry-forward T2.23 = W7-CF-W7-5 from S90 W7 CF-54 Route C in-cache regression baseline (`sessions/archive/session-90/session-90-w7-workingpaper.md §"W7-3"` carry-forward block; Route C target observable = empirical-β estimate at substrate-distance pole s=4 per `cross-pillar-bridge-anatomy.md §"Level-2 empirical-β verification rule"` advisory until K=3).

### 2. Trigger

`[VERIFY]` — substrate-physics in-cache regression refinement requires verification of the L_max=16 cache extension's structural feasibility (Friedrich-Bär saturation theorem applicability per `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"`) plus the empirical-β convergence between asymptotic limit (Sage-Q L ∈ [10, asymptotic-cutoff]) and in-cache fit at L_max=16.

### 3. Classification

**GEOMETRIC** (substrate-IS Level-2 envelope at the substrate-distance pole s=4 per the Level-2 empirical-β verification rule; the cache-ceiling boundary effect characterization IS a substrate-IS property of the L^{-α} convergence rate at the Mellin-cone pole, NOT a particle or phononic observable).

### 4. Agent type

**Primary author**: `connes-ncg-theorist`

Rationale: the substrate-distance pole s=4 evaluation under the Mellin-cone residue formula at L_max=16 cache extension is the NCG-axiomatic axis where `connes-ncg-theorist` owns the Mellin-Barnes residue calculus, the Casimir-bound L_max-truncation feasibility argument, and the Friedrich-Bär saturation theorem application. The L_max=16 cache extension is a structural extension of `s84_spectrum_cache_L12_tau019.npz`; the feasibility pre-check (Friedrich-Bär saturation per `math-scripts.md §"D_K Block-Diagonality"`) determines whether the cache extension is admissible at the substrate algebra layer.

**FORBIDDEN test-case agent type**: `gen-physicist` (per spawn-prompt).

Stage-2-style cross-axis confirmation routing (forward, queued for W8 if needed): `lizzi-spectral-functional-theorist` (Axis-A spectral-functional / regulator-class axis; cross-checks the L^{-α} envelope's regulator-invariance per the F_2 = {ζ, SDW} K-invariant identity sub-atlas + Wodzicki residue universality) — but Stage-2 may NOT be required for this gate at S91 (the L_max=16 cache extension is a structural-refinement gate at a single axis, not a cross-axis joint theorem).

### 5. Hypothesis

**Hypothesis statement (PASS)**: The CF-54 Route C in-cache regression's empirical-β estimate at substrate-distance pole s=4 (`α(s=4) ≈ 1.885` per W-6 CF β_shell FI tag at d=4) refines under L_max=16 cache extension to within ±10% of the asymptotic limit `α_asymptotic(s=4)` (Sage-Q at L ∈ [10, asymptotic-cutoff = L_max=100 default]); the cache-ceiling boundary effect is characterized; the L_max=16 cache extension is feasible per Friedrich-Bär saturation theorem per `math-scripts.md §"D_K Block-Diagonality"`.

**Hypothesis statement (FAIL alternatives)**: (i) Friedrich-Bär saturation pre-check FAILs at L_max=16 (the NEW-sector η_FB lower bound exceeds the observable's structural ceiling at one or more (p, q) sectors with p+q=L_max=16); cache extension infeasible at L_max=16; (ii) cache extension feasible but the empirical-β deviates from asymptotic limit by > 10% — i.e., the cache-ceiling boundary effect dominates at L_max=16 and structural-saturation has not been reached; (iii) regime breakdown: the Mellin-Barnes residue evaluation at s=4 pole breaks down at L_max=16 truncation (numerical NaN/Inf).

### 6. Method (complete dispatch prompt for connes-ncg-theorist)

```
Dispatch prompt for connes-ncg-theorist:

You are dispatched as primary author for gate
S91-W7-CF-W7-5-CF-54-ROUTE-C-IN-CACHE-REGRESSION-LMAX-16 (T2.23).

Substrate framing: The Route C in-cache regression target IS the
substrate-IS empirical-β exponent at the Mellin-cone substrate-
distance pole s=4. The L_max=16 cache extension IS a substrate-
internal feasibility question — whether the substrate's D_K
eigenvalue spectrum at L_max=16 is structurally accessible (per
Friedrich-Bär saturation) AND whether the empirical-β converges to
its asymptotic limit by L_max=16.

DELIVERABLES:

(D1) Friedrich-Bär saturation feasibility pre-check:
     - Compute per-(p,q) sector η_FB(p,q) = |λ|_min(p,q) /
       √(C_2(p,q) + 1) on existing L_max=12 master cache
       (s84_spectrum_cache_L12_tau019.npz)
     - Pin η_FB_lower = 0.40 (8% below empirical (1,1)-sector floor)
       per W11-3 saturation theorem precedent
     - For each (p, q) sector with p+q = 13, 14, 15, 16, compute the
       Casimir-bound: λ_min,NEW(p,q) ≥ η_FB_lower · √(C_2(p+q=L_max)+1)
     - Verify the NEW-sector lower bound exceeds the empirical-β
       target observable's structural ceiling (the substrate-distance
       pole s=4 effective cardinality bound per W-6 CF-1 sub-window
       analysis); IF YES → cache extension at L_max=16 feasible AND
       structural-saturation reached at L_max=16; IF NO → cache
       extension infeasible at L_max=16; queue forward at L_max ≥ 22
       per W-6 CF-1 sub-window approach
     - Output `friedrich_baer_saturation_at_lmax_16` bool

(D2) L_max=16 cache extension (CONDITIONAL on D1 PASS):
     - Construct (p,q) irreps for sectors p+q ∈ {13, 14, 15, 16} via
       recursive Casimir projection from the (4, 4) seed sector (per
       `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-
       Projection Feasibility Pre-Check"`)
     - Time budget: per W11-3 precedent, irrep (13, 0) construction
       did NOT complete within 10-minute wall time; THEREFORE the
       cache extension at L_max=16 MUST proceed sector-by-sector
       (not in a single batch); per-sector incremental construction
       allows the gate to honor the agent timeslot bound
     - IF the construction completes for all (p,q) sectors with
       p+q ≤ 16 within the per-gate wall-time budget → output
       extended cache `s91_spectrum_cache_L16_tau019.npz`
     - IF construction times out at one or more (p,q) sectors with
       p+q ≤ 16 → emit INFO with partial-cache output AND
       regime_verdict = MARGINAL or BREAKDOWN per the auto-
       shortening clause discipline of `gate-verdicts.md`

(D3) Empirical-β estimate at substrate-distance pole s=4 on
     extended cache (CONDITIONAL on D2 PASS):
     - Load extended cache (or partial cache from D2)
     - Compute Mellin-Barnes residue at pole s=4 per
       `cross-pillar-bridge-anatomy.md §"Level-2 empirical-β
       verification rule"` advisory until K=3:
         (i) asymptotic verification via Sage-Q at L ∈ [10, asymptotic-
             cutoff = L_max=100 default] (use `mcp__sage__sage_eval`
             with QQ exact-fraction arithmetic; output asymptotic
             α(s=4) limit value)
         (ii) in-cache verification at L_max=16 via log-log fit on
             the empirical L_max-truncated value range L ∈ {10, 12,
             14, 16}
     - Output: asymptotic_alpha_s4 (Sage-Q exact); in_cache_alpha_s4
       (in-cache fit at L_max=16); relative_deviation = |asymptotic -
       in_cache| / asymptotic
     - PASS criterion: relative_deviation < 0.10 (within ±10%);
       AND cite cache-ceiling boundary effect per
       `cross-pillar-bridge-anatomy.md §"Level-2 empirical-β
       verification rule"` IF relative_deviation > 0.05

(D4) Working-paper section in
     sessions/archive/session-91/session-91-w7-workingpaper.md §W7-3
     >15 lines; substantive content; cache-ceiling boundary effect
     declaration + Friedrich-Bär saturation feasibility status +
     asymptotic vs in-cache empirical-β comparison + β_shell FI tag
     per `regulator-pin-discipline.md §"Extension: β_shell FI
     Classification"` advisory until K=3.

(D5) Verdict line in
     computations/session-91/s91_gate_verdicts.txt
     S91-W7-CF-W7-5-CF-54-ROUTE-C-IN-CACHE-REGRESSION-LMAX-16:
       PASS|FAIL|INFO -- value=<relative_deviation>
       scheme=route-C-in-cache-regression
       convention=substrate-distance-pole-s4-Mellin-Barnes-residue
       L_max=16
       audit_sha256=<64-hex>
       content_sha256=<64-hex>
       schema_version=S87+

     Dual-SHA companion comment row.
     domain_used_frac companion (if auto-shortening at L_max=16 fires).

FORBIDDEN actions per `v3-closure-recovery.md §PROHIBITED_ACTIONS`:
- Convention-shopping: do NOT switch from the pre-registered Mellin-
  Barnes residue scheme to a different residue evaluation method.
- Iterate-until-PASS: do NOT extend the L_max sweep beyond 16 in the
  same gate run; if L_max=16 INFO/FAIL, queue forward at L_max ≥ 22
  as a separate S92+ gate (not in-session retry).
- Post-hoc threshold editing: ±10% relative_deviation tolerance is
  pinned; do NOT loosen.
- Ansatz-forced PASS: do NOT hardcode asymptotic_alpha_s4 from
  literature or canonical_constants; compute it via Sage-Q.
```

### 7. Machinery pin (PRDR)

| Pin | Value | Source |
|:----|:------|:-------|
| `N_eval` | Per-(p,q) sector irrep construction at p+q ∈ {13, 14, 15, 16}; ~30 sectors at the L_max=16 boundary; per-sector ~few-thousand eigenvalues | per `math-scripts.md §"D_K Block-Diagonality"` Casimir-bound estimate |
| `L_max` | 16 (operational target); 12 (existing baseline cache); 100 (asymptotic Sage-Q cutoff) | NEW extended cache target |
| `scan_range` | L ∈ {10, 12, 14, 16} for in-cache fit; L ∈ [10, 100] for asymptotic Sage-Q | pre-registered per `cross-pillar-bridge-anatomy.md §"Level-2 empirical-β verification rule"` |
| `step_size` | L-step = 2 for in-cache fit; Sage-Q continuous asymptotic limit | pre-registered |
| `tolerance` | `pass_tolerance = 0.10` (10% relative deviation between asymptotic α(s=4) and in-cache α(s=4) at L_max=16); ABSOLUTE on relative_deviation metric | per `cross-pillar-bridge-anatomy.md §"Level-2 empirical-β verification rule"` 10% threshold |
| `scheme` | `route-C-in-cache-regression` | NEW scheme tag (S90 W7 CF-54 baseline at L_max=10; S91 W7-3 extension at L_max=16) |
| `convention` | `substrate-distance-pole-s4-Mellin-Barnes-residue` | NEW convention tag; substrate-distance pole s=4 Mellin-Barnes residue evaluation |
| `random_seed` | N/A (deterministic) | — |
| `GPU path` | NumPy CPU; per-(p,q) sector incremental construction; per `math-scripts.md §"Environment"` `torch.linalg` on GPU for individual sector eigenvalue extraction if sector dim ≥ 1000 | OMP_NUM_THREADS=8 fallback |
| `CLASS pin` | `FULL` (Mellin-Barnes residue formula at substrate-distance pole s=4 is FULL physical evaluation; SCHEMATIC helpers may be consumed but the gate's primary output is the FULL evaluation per Sage-Q asymptotic limit + in-cache fit comparison) | — |
| `tier_pin` | `TIER-1` (FULL physical) | — |
| `precision` | float64 for in-cache fit; Sage-Q exact-fraction (QQ) for asymptotic | per `math-scripts.md §"Sage-Exact Rationals"` mandatory clause for Ω_GW-class observables; analogous discipline for empirical-β |
| `friedrich_baer_eta_lower` | 0.40 (8% below empirical (1,1)-sector floor 0.4365 per W11-3 saturation theorem precedent) | `math-scripts.md §"D_K Block-Diagonality"` |

**Input SHA-256 pins**:

| File | Path | SHA | Source |
|:-----|:-----|:----|:-------|
| L_max=12 spectrum cache | `computations/session-84/s84_spectrum_cache_L12_tau019.npz` | `<pinned at dispatch>` | S84 W2 |
| CF-54 Route C baseline at L_max=10 | `computations/session-90/s90_w7_3_cf_54_route_c_in_cache_regression.npz` (or equivalent) | `<pinned at dispatch>` | S90 W7-3 baseline |
| canonical_constants module | `computations/_shared/canonical_constants.py` | `<pinned at dispatch>` | post-S91 W0 housekeeping |
| Sage MCP availability check | runtime via `mcp__sage__sage_backend_info` | `<computed-at-runtime>` | runtime |

**Audit-SHA closure**: `audit_sha256 = closure_hash(ordered-input-pin-map)`.

### 8. Expected output 4-tuple

`(value=<relative_deviation_percent>, scheme=route-C-in-cache-regression, convention=substrate-distance-pole-s4-Mellin-Barnes-residue, L_max=16)`

Output file contents (`s91_w7_3_cf_54_route_c_in_cache_lmax_16.npz` + `.png` + `.json` sidecar; optional `s91_spectrum_cache_L16_tau019.npz` extended cache):

- `friedrich_baer_saturation_at_lmax_16`: bool; D1 pre-check PASS status
- `friedrich_baer_eta_FB_per_pq`: shape (num_pq_sectors,); float64 per-sector η_FB(p,q)
- `cache_extension_feasibility_status`: string; "FEASIBLE-FULL-LMAX-16", "FEASIBLE-PARTIAL", or "INFEASIBLE"
- `extended_cache_pq_sectors_completed`: shape (n,); list of (p,q) tuples successfully constructed at p+q ∈ {13, 14, 15, 16}
- `asymptotic_alpha_s4`: Sage-Q exact form (e.g., `Fraction(1885, 1000)` or analogous); float64 image
- `in_cache_alpha_s4_lmax_16`: float64; in-cache log-log fit value at L_max=16
- `relative_deviation`: float64; `|asymptotic - in_cache| / |asymptotic|`
- `relative_deviation_percent`: float64; `relative_deviation × 100`
- `cache_ceiling_boundary_effect_status`: string; "DOMINANT" (>10%), "NEAR-CEILING" (5-10%), or "SUBDOMINANT" (<5%)
- `beta_shell_FI_tag`: bool; True (per `regulator-pin-discipline.md §"Extension: β_shell FI Classification"` advisory until K=3)
- `verdict_composite`, `sign_verdict`, `magnitude_verdict`, `regime_verdict` strings
- `domain_used_frac`: float64; fraction of intended L-window actually computed (1.0 if no auto-shortening; < 1.0 if Friedrich-Bär saturation breakdown forces sub-window evaluation)
- `audit_sha256`, `content_sha256` 64-hex
- `runtime_seconds` float

PNG plot: log-log fit of empirical α(s=4) vs L_max for L ∈ {10, 12, 14, 16} with asymptotic limit line + ±10% tolerance band.

### 9. PASS / FAIL / INFO thresholds

**PASS**: (i) `friedrich_baer_saturation_at_lmax_16 = True`; AND (ii) `cache_extension_feasibility_status = "FEASIBLE-FULL-LMAX-16"`; AND (iii) `relative_deviation < 0.10` (within ±10%); AND (iv) `regime_verdict = VALID` (no auto-shortening triggered at the asymptotic Sage-Q step or the in-cache fit step); AND (v) `domain_used_frac ≥ 0.95` (per `gate-verdicts.md §"Auto-shortening clause discipline"`).

**INFO**: `cache_extension_feasibility_status = "FEASIBLE-PARTIAL"` (some sectors at p+q ∈ {13..16} timed out but a partial cache is usable for the in-cache fit) AND `relative_deviation < 0.10`; OR full cache feasible AND `0.05 ≤ relative_deviation < 0.10` (cache-ceiling boundary effect near-ceiling); OR `regime_verdict = MARGINAL` per auto-shortening clause (`0.50 ≤ domain_used_frac < 0.95`).

**FAIL**: `cache_extension_feasibility_status = "INFEASIBLE"` (Friedrich-Bär saturation pre-check FAILed at L_max=16; cache extension structurally inadmissible); OR `relative_deviation ≥ 0.10` (cache-ceiling boundary effect dominates at L_max=16; structural-saturation not reached); OR `regime_verdict = BREAKDOWN` per auto-shortening clause (`domain_used_frac < 0.50`); OR Mellin-Barnes residue evaluation at s=4 pole produces NaN/Inf.

**Tolerance rule**: RATIO (`relative_deviation` is a ratio metric); ABSOLUTE on `domain_used_frac` (band thresholds at 0.95, 0.50).

**Publication precision**: `relative_deviation` published at 4-significant-figure float64 (1e-4 absolute precision); `asymptotic_alpha_s4` published at Sage-Q exact form per `regulator-pin-discipline.md §"Sage-Exact Rationals"` discipline.

### 10. Substitution chain ([VERIFY])

Pre-registered substitution chain for empirical-β estimate at substrate-distance pole s=4:

**Step 1 (Definitions)**:
- `α(s=4)`: empirical Level-2 envelope exponent at the Mellin-cone substrate-distance pole s=4 on the substrate algebra `A_K`
- `α_asymptotic(s=4)`: asymptotic limit as L_max → ∞ via Sage-Q exact-fraction arithmetic at L ∈ [10, 100]
- `α_in-cache(s=4, L_max=16)`: in-cache log-log fit at L ∈ {10, 12, 14, 16}
- `relative_deviation = |α_asymptotic - α_in-cache| / |α_asymptotic|`

**Step 2 (Substitution — Level-2 empirical-β verification rule)**:

Per `cross-pillar-bridge-anatomy.md §"Level-2 empirical-β verification rule"` advisory until K=3 (S90 close):

```
Asymptotic verification (canonical): α_asymptotic(s=4) via Sage-Q
                                      at L ∈ [10, asymptotic-cutoff=100]
In-cache verification (diagnostic): α_in-cache(s=4, L_max=16) via
                                      log-log fit on L ∈ {10, 12, 14, 16}
PASS predicate: relative_deviation < 0.10 (10% tolerance band)
```

**Step 3 (Simplification — Friedrich-Bär saturation pre-check)**:

Per `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"`:

```
η_FB_lower = 0.40 (8% safety margin below empirical (1,1)-floor 0.4365)
For each NEW (p, q) sector at p+q ∈ {13, 14, 15, 16}:
  λ_min,NEW(p, q) ≥ η_FB_lower · √(C_2(p, q) + 1)
If λ_min,NEW(p, q) exceeds the substrate-distance pole s=4 observable's
  effective cardinality ceiling at the cache-ceiling boundary →
  structural-saturation reached → cache extension feasible AND
  the empirical-β at L_max=16 is invariant under further L_max
  increase (analytic certification by saturation theorem)
```

**Step 4 (Direction-prediction)**:

Per W-6 CF β_shell FI tag at d=4 substrate-distance s*=3 (forward analogous to s=4): predicted `α(s=4) ≈ 1.885` per W-6 calibration corpus. The Friedrich-Bär saturation theorem at L_max=16 IS PREDICTED to certify structural-saturation if the W-6 CF-1 sub-window approach holds; the in-cache empirical-β at L_max=16 should converge to within ±5% of asymptotic.

**Step 5 (Conclusion)**:

Sign_verdict prediction PASS = `relative_deviation < 0.10`; the substrate-physics direction is "asymptotic and in-cache agree at L_max=16 within structural-saturation tolerance". FAIL would indicate cache-ceiling boundary effect dominance; INFO would indicate near-ceiling deviation.

### 11. Solution-space interpretation

**PASS corridor**: Route C in-cache regression refined to within ±10% asymptotic at L_max=16; structural-saturation reached; the W-6 CF β_shell FI classification at d=4 substrate-distance s* = 3 extends analogously to s=4 with the L_max=16 cache extension; Level-2 envelope empirical-β verification rule advisory K=1 → K=2 (per `cross-pillar-bridge-anatomy.md §"Level-2 empirical-β verification rule"` calibration corpus saturation). Forward: K=3 promotion at S92+ on a third independent Level-2 empirical-β verification gate.

**FAIL corridor**: cache extension at L_max=16 either infeasible (Friedrich-Bär saturation pre-check FAILed) or feasible but cache-ceiling boundary effect dominates (relative_deviation ≥ 10%). Forward: queue at L_max ≥ 22 per W-6 CF-1 sub-window approach as separate S92+ gate (not in-session retry).

**INFO corridor**: partial cache feasibility OR near-ceiling deviation (5-10% relative_deviation) OR MARGINAL regime_verdict; cache-ceiling boundary effect characterization is informative; forward S92+ refinement queued with the partial-cache output as starting point.

### 12. Effort

**~0.8 wave-equivalent** (~5-6 hours of connes-ncg-theorist dispatch time):
- D1 Friedrich-Bär saturation feasibility pre-check: ~1 hour
- D2 L_max=16 cache extension (per-sector incremental construction; budget-constrained per W11-3 timeout precedent): ~2-3 hours
- D3 empirical-β estimate at s=4 pole on extended cache: ~1 hour
- Sage-Q asymptotic limit via MCP: ~30 minutes
- Working-paper section + verdict line: ~1 hour

### 13. Substrate-framing reminder

The CF-54 Route C in-cache regression target IS the substrate-IS empirical-β exponent at the Mellin-cone substrate-distance pole s=4. The L_max=16 cache extension IS a substrate-internal feasibility question — does the substrate's `D_K` eigenvalue spectrum at L_max=16 admit structural access via the Friedrich-Bär saturation theorem? Direction of explanation: substrate IS spectral triple with `D_K` eigenvalue spectrum → L_max=16 truncation IS substrate-internal observation window → Friedrich-Bär saturation IS substrate-internal structural property → empirical-β at s=4 pole IS substrate-IS Level-2 envelope exponent. Container-thinking violation FORBIDDEN: "we extend the cache to L_max=16 by running the computation longer" — INVERT: "the L_max=16 truncation IS substrate-internal observation window; the cache extension's feasibility IS the substrate's own Friedrich-Bär saturation property; the empirical-β at s=4 pole IS substrate-IS structural data evaluated at the L_max=16 truncation window".

---

## Wave 7 Machinery-Enumeration Pin (PRDR across all 4 gates)

Per `epistemic-discipline.md §"Pre-Registration Completeness"` PRDR Class 8 pre-flight requirement, the W7 wave's full free-parameter enumeration across §W7-1 + §W7-2a + §W7-2b + §W7-3:

| Free parameter | §W7-1 (T2.21) | §W7-2a (T2.22a) | §W7-2b (T2.22b) | §W7-3 (T2.23) |
|:---------------|:--------------|:----------------|:----------------|:--------------|
| `L_max` | 12 (operational); 10 (canonical baseline) | 12 | 12 | 16 (extended); 12 (baseline); 100 (asymptotic Sage-Q) |
| `scan_range` | 5-point generator-pair grid | 7 axioms + Poincaré duality + KO-dim + 3 bridge-map candidates | 7 axioms + Poincaré duality + KO-dim + 3 bridge-map candidates + 9 colour-tagged sectors | L ∈ {10, 12, 14, 16} in-cache; L ∈ [10, 100] asymptotic |
| `tolerance` | abs `1e-3` pass / `1e-1` info | machine eps `1e-12` axioms | machine eps `1e-12` axioms | rel `0.10` pass band; abs `0.95` / `0.50` domain_used_frac bands |
| `scheme` | APS-1975-secondary-class | bi-chirality-direct-sum | SU(3)-coloured-chirality | route-C-in-cache-regression |
| `convention` | `substrate-distance-1-FULL-CC1996-INNER-FLUCTUATION` | `substrate-distance-1-FULL-CONNES-1996-BICHIRALITY` | `substrate-distance-1-FULL-CM2008-§11-COLOURED` | `substrate-distance-pole-s4-Mellin-Barnes-residue` |
| `random_seed` | N/A (deterministic) | N/A | N/A | N/A |
| `GPU path` | NumPy CPU (largest block ~9792²); optional torch.linalg | NumPy CPU per-(p,q) sector | NumPy CPU per-(p,q) sector + colour-axis | NumPy CPU per-sector incremental |
| `CLASS pin` | FULL | FULL | FULL | FULL |
| `tier_pin` | TIER-1 | TIER-1 | TIER-1 | TIER-1 |
| `precision` | float64 + complex128 (J) | float64 + complex128 (J) | float64 + complex128 (J + SU(3) generators) | float64 (in-cache) + Sage-Q (asymptotic) |

**SCHEMATIC-vs-FULL pin discipline check**: ALL four W7 gates pin `CLASS = FULL` per `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY level-pin discipline. No SCHEMATIC consumption admitted at this wave; the Connes-Chamseddine 1996 §2.2-2.3 inner-fluctuation calculus (§W7-1), the Connes 1996 reconstruction theorem application under bi-chirality (§W7-2a), the Connes-Marcolli 2008 §11 SU(3)-coloured chirality framework (§W7-2b), and the Mellin-Barnes residue evaluation at substrate-distance pole s=4 (§W7-3) are all FULL physical implementations on the substrate algebra `A_K`. No `-SCHEMATIC` suffix on any convention tag; no `tier_pin = TIER-2` companion comment row.

**PRDR pre-flight**: all 4 W7 gates have pinned every free parameter at plan-freeze. PRU Class 8 cardinality test PASSes: no missing pin per `_pru_cardinality_audit.py` D_PRU_raw threshold.

**SOURCE-RECONCILIATION at plan-freeze**: all canonical pins consumed (`gv_canonical_difference_FW`, `slope_A_FW_Conv_A`, `slope_A_FW_Conv_B`, `M_KK`, `tau_fold`, `Delta_BCS`, `E_cond`, `c_sub`, `c_W12_deficit_FW_PRIMARY_ConvB`, `tau_max_HK5_regime_FW_asymptotic_limit_FW`) are queried via `mcp__knowledge__.get_constant(...)` at plan-freeze and verified against `canonical_constants.py` post-S91-W0-housekeeping baseline (PROVENANCE dict count 134 entries). D_max < 0.1 for all pin queries (no Class-(a), Class-(b), Class-(c), Class-(d), Class-(e), Class-(f) SOURCE-RECON activations expected).

**SUBSTRATE-FIRST-PROVENANCE at plan-freeze**: all gate output values cite substrate-first canonical sources (Connes-Chamseddine 1996 §2.2-2.3, Connes 1996 reconstruction, Connes-Marcolli 2008 §11, Mellin-Barnes residue formula on `A_K`). No external-paper placeholder pins; no SCHEMATIC-helper consumption without disclosure; no ambient knowledge fallback.

---

## Wave 7 Input-SHA Ledger (per-gate Input-PIN MAP digest)

Each gate's `audit_sha256` is computed at runtime as `closure_hash(input_pin_map)` where the input_pin_map is the ordered concatenation of file-SHAs + constant-values + pre-registered thresholds. The full Input-PIN MAP for each gate is enumerated in §6 (Method) and §7 (Machinery pin) blocks above. The plan-block SHA-256 over the §W7-N block from heading to next-section boundary is computed at plan-freeze for the `methodology-wave-allowlist.md` allowlist append (per `wave-classification.md` M4) — but W7 is COMPUTE-class (numerical-predicate-present per M1 fail-test), not METHODOLOGY-class; therefore W7 does NOT append to the allowlist.

| Gate | Plan-block SHA-256 over §W7-N | Output `audit_sha256` source |
|:-----|:-------------------------------|:------------------------------|
| §W7-1 (T2.21) | `<computed-at-plan-freeze>` over the `## §W7-1.` block | runtime: closure_hash over the 5 file-SHAs + 5 constant pins enumerated in §7 |
| §W7-2a (T2.22a) | `<computed-at-plan-freeze>` over the `## §W7-2a.` block | runtime: closure_hash over the 5 file-SHAs + 4 constant pins enumerated in §7 |
| §W7-2b (T2.22b) | `<computed-at-plan-freeze>` over the `## §W7-2b.` block | runtime: closure_hash over the 5 file-SHAs + 4 constant pins enumerated in §7 |
| §W7-3 (T2.23) | `<computed-at-plan-freeze>` over the `## §W7-3.` block | runtime: closure_hash over the 4 file-SHAs + 5 constant pins enumerated in §7 |

**Note on SHA computation discipline**: per `gate-verdicts.md` MANDATORY clause, all `audit_sha256` values are emitted at full 64-character hex; no head-truncation. The 16-character head form is permitted in the dual-SHA companion comment row's short-form fields (`audit_sha256_short`, `content_sha256_short`) per W9a-99 split, but NEVER in the canonical first line.

**Verdict-file path**: all W7 verdict lines are appended to the canonical `computations/session-91/s91_gate_verdicts.txt` per `gate-verdicts.md §"Canonical Verdict-File Path"` MANDATORY clause. No variant paths admitted.

---

**End of Session 91 Wave 7 plan**: 4 substrate-physics chirality gates (T2.21 + T2.22a + T2.22b + T2.23) at ~3.5 wave-equivalents combined; primary author `connes-ncg-theorist` (all four); Stage-2 cross-axis verifies for §VII.AQ.OP-PROJ + §VII.AT.OP-PROJ + §VII.AW.OP-PROJ promotions queued forward at W8 conditional on W7 PASS verdicts. The W7 wave evaluates the substrate-physics content of the three CF-A40 FAIL alternative-chirality re-scope candidates (a) bi-chirality + (b) SU(3)-coloured + (c) inner-fluctuation deposited at S90 W7 CF-45; the L_max=16 cache extension refines the CF-54 Route C in-cache regression at substrate-distance pole s=4 per Friedrich-Bär saturation theorem feasibility.
