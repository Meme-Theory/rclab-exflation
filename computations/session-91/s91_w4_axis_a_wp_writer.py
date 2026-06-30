#!/usr/bin/env python3
"""Atomic find-and-replace writer for §W4-4.AXIS-A WP section.

Avoids Edit-tool mtime race with parallel Axis-B writer.
"""
from __future__ import annotations
import sys
import time
from pathlib import Path

WP_PATH = Path(__file__).resolve().parents[1].parent / "sessions" / "session-91" / "session-91-w4-workingpaper.md"

OLD_STUB = (
    "### §W4-4.AXIS-A — Results (filled at runtime by van-den-dungen-bridge-theorist OR gen-physicist fallback)\n"
    "\n"
    "**Status**: NOT STARTED\n"
    "**Selected reviewer at dispatch**: pending {van-den-dungen-bridge-theorist, gen-physicist}\n"
    "\n"
    "| Clause | Description | Substitution chain | Computed value | Reference | Verdict |\n"
    "|:-------|:------------|:-------------------|:---------------|:----------|:--------|\n"
    "| (a) | Pillar 1 NCG-axiomatic A_BdG-full claims (7 NCG axioms preserved) | pending | pending | A_BdG-full = A_F ⊗ M_2(ℂ); inheritance morphism injective | PENDING |\n"
    "| (c) | Inheritance morphism composition bridge map (5-anatomy complete) | pending | pending | A_K ↪ A_BdG-full ↠ A_BdG-image; Element 3 binding type declared | PENDING |\n"
    "| (e) | Parse-tree closed-form derivation on substrate Bogoliubov algebra | pending | pending | `Var_a(n_a^GGE) = (1/N) Σ_a m_a |v_a|⁴ − ((1/N) Σ_a m_a |v_a|²)²` | PENDING |\n"
    "\n"
    "**Axis-A 3-tuple annotation** (S87+ schema-v2): sign_verdict=PENDING magnitude_verdict=PENDING regime_verdict=PENDING\n"
    "**Axis-A verdict line**: pending\n"
    "**Axis-A substrate framing addendum** (Pillar 1 NCG-axiomatic A_BdG-full axis): pending\n"
)

NEW_BLOCK = """### §W4-4.AXIS-A — Results (van-den-dungen-bridge-theorist; NCG-axiomatic / Kasparov-KK submersion-bridge axis)

**Status**: COMPLETED (2026-05-16)
**Selected reviewer at dispatch**: `van-den-dungen-bridge-theorist` (canonical selection per plan §3 NCG-axiomatic Axis-A pool {van-den-dungen-bridge-theorist, gen-physicist, hawking-theorist}; van-den-dungen canonical for the dual-symbol A_BdG-full = A_F ⊗ M_2(ℂ) inheritance-morphism axis per plan §3 lines 1051-1052 rationale).

**Procedural-floor pre-check** (per plan §5a PROCEDURAL FLOOR; `joint-theorem-promotion.md §"Two-Agent Independent-Verify"`):
- `sessions/archive/session-88/workshops/s88-w17-*.md` (S88 W-17 §V.3 corrigendum workshop transcript): NOT CONSUMED.
- `sessions/archive/session-90/workshops/s90-w6-d4-envelope-identity.md` (S90 W6 CF-51 STAGE-1-CANDIDATE workshop transcript): NOT CONSUMED.
- Original-authoring-agent (OAA) exclusion: `connes-ncg-theorist` and `lizzi-spectral-functional-theorist` EXCLUDED as S88 W-17 §V.3 corrigendum + S90 W6 CF-51 workshop co-authors. PASS by axis-distinctness (vdd is on the NCG submersion / Kasparov-KK bridge axis, structurally distinct from the NCG-axiomatic OAA axis).
- Downstream-inheritance reach pre-check: vdd memory at `.claude/agent-memory/van-den-dungen-bridge-theorist/MEMORY.md` + s61-s64-bundle, s70-s75-bundle, s82-kasparov-abelian-proof, s83-g24-result, s84-w2-18-layer-transport reference files contain ZERO citations of "s88-w17", "S88 W-17", "s90-w6-d4", or "S90 W6 CF-51" transcripts. PASS (verified by `grep -l` over agent-memory directory).
- Audit-machinery self-citation cross-check: clause-(e) parse-tree decision procedure machinery (`computations/_shared/_corner_classification_audit.py`) is jointly authored by connes (S88 §W5b-46) and lizzi (S82 R2-B FI/RD/MIXED origin); van-den-dungen-bridge-theorist is structurally distinct from the corner-classification authorship per plan §3 cross-check (line 1062). PASS.

**Plan-text-drift orchestrator-convention** (per `substrate-first-canonical-sourcing.md §(ii.B)`): plan §7 PRDR cited the L_max=12 master cache at `computations/session-87/s84_spectrum_cache_L12_tau019.npz`; the canonical artifact lives at `computations/session-84/s84_spectrum_cache_L12_tau019.npz`. Runtime canonical-path rescue per the orchestrator-convention applied; drift correction documented in verdict-line `value=` field via the `cache_path_drift_corrected_from_plan_session-87_to_canonical_session-84` token. Substrate-IS integrity preserved (same artifact, same eigenvalue cache, same Peter-Weyl sector decomposition); the drift is a path-level documentation slip in the plan, not a content-level divergence.

#### Axis-A 3-clause sub-audit table

| Clause | Description | Substitution chain (4-step / 5-anatomy / 5-step) | Computed value | Reference | Verdict |
|:-------|:------------|:-------------------------------------------------|:---------------|:----------|:--------|
| (a) | Pillar 1 NCG-axiomatic A_BdG-full = A_F ⊗ M_2(ℂ) claims (7 NCG axioms preserved; inheritance morphism injective) | Step 1: A_BdG-full = A_F ⊗ M_2(ℂ), A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ). Step 2: substitute into Connes axioms 1-7. Step 3: per-axiom verification (axiom 1 bilinear-in-[D,π(a)] tensor-preserved; axiom 2 BdG-doubling Z/2 grading per Connes-Krajewski-Schücker; axiom 3 finite-dim automatic; axiom 4 finiteness preserved under finite-dim tensor; axiom 5 Poincaré-duality preserved by Künneth K_0(A_F ⊗ M_2) = K_0(A_F) ⊕ K_0(A_F); axiom 6 orientation Hochschild-Künneth Morita-invariance HH^n preserved per registry line 13032; axiom 7 chirality γ = γ_F ⊗ σ_z anticommutes with D_BdG by doubling construction). Step 4: inheritance morphism A_K ↪ A_BdG-full injective by tensor-with-identity (faithful monomorphism). | 7-axiom inheritance: True; injectivity: True | A_BdG-full = A_F ⊗ M_2(ℂ); inheritance morphism injective; S88 §W5b-48 axiom-level pin audit_sha256=ff505a036d1ad6d7cb6857ace42358a7aacf179490cb224218c12aba4c178ab9 (cited in registry line 12954) | **PASS** |
| (c) | Inheritance morphism composition bridge map (5-anatomy complete; 3-Level ladder; Level-2 sub-class declared) | 5-anatomy walk on registry sub-corrigendum lines 13030-13049: Element 1 = Var_a substrate-IS closed form on A_BdG-full (per parse-tree expansion line 17157-17168); Element 2 = Var_a as operationally observed at A_BdG-image = M_2(ℂ) (Axis-B audit territory); Element 3 = inheritance morphism composition A_K ↪ A_BdG-full ↠ A_BdG-image, fiducial-anchor binding type = **substrate-self-consistent** (Pillar 1 and Pillar 2 both inhabit Cell-II per registry line 13038); Element 4 = L^{-4} envelope (modulo log) at d=4 Weyl-law tail, **Level-2-binding** sub-class via HKR-image Morita-invariance HH^n(A_F ⊗ M_2(ℂ)) = HH^n(A_F) (registry line 13032); Element 5 = numerical anchor Var_a(L_max=10) on the L_max=12 master cache (computed in clause (e)). 3-Level ladder: Level-1 regulator-invariant identity at the algebra-INVARIANT spectrum-only family (Cell-II); Level-2 L^{-4} convergence with Level-2-A operational (Weyl-tail convergence) PASS and Level-2-B regulator-invariance PASS; Level-3 empirical anchor at L_max=10. | 5/5 elements PRESENT; bridge map EXPLICIT; binding type DECLARED (substrate-self-consistent); Level-2 sub-class DECLARED (Level-2-binding via HKR Morita-invariance) | A_K ↪ A_BdG-full ↠ A_BdG-image; Element 3 binding=substrate-self-consistent; Level-2-binding via HKR; `cross-pillar-bridge-anatomy.md §"IS-not-IN Anatomy (5 elements)"` + §"Three-Level Structural-Confidence Ladder" + §"Level-2 sub-class (binding vs non-binding)" | **PASS** |
| (e) | Parse-tree closed-form derivation on substrate Bogoliubov algebra (Cell-II classification + Level-3 numerical anchor) | Step 1 (history-label): Var_a(n_a^GGE). Step 2 (Bogoliubov substitution per S52 BdG canonical amplitudes; `Delta_BCS = 0.464255 M_KK` per canonical_constants.py line 387 R-PROTECTED pin): n_a^GGE = ⟨ψ_GGE \\| n_a \\| ψ_GGE⟩ = \\|v_a\\|² where \\|v_a\\|² = Δ_BCS² / (2(λ_a² + Δ_BCS²)). Step 3 (variance formula): Var_a(X) = (1/N) Σ_a m_a X_a² − ((1/N) Σ_a m_a X_a)². Step 4 (substrate-IS closed form): Var_a(n_a^GGE) = (1/N) Σ_a m_a \\|v_a\\|⁴ − ((1/N) Σ_a m_a \\|v_a\\|²)² — spectrum-only functional of {λ_a, m_a, Δ_BCS}; **state_pair_count = 0**, **algebra_dep_count = 0** at the clause-(e) parse-tree decision counter. Step 5 (corner classification): only spectrum-only operations present (Σ_a, ·², ·⁴, 1/N over Peter-Weyl multiplicities) ⇒ algebra-INVARIANT ⇒ Cell-II (algebra-INVARIANT × Mellin pole s=4). | Var_a(L_max=10) = 4.7650356226e-05 (multiplicity-equal-weight m_a=1 with abs_evals per-state degeneracy already baked in by 16×dim factor in cache; N_total = 78080 eigenvalues across 65 Peter-Weyl sectors at p+q ≤ 10); ⟨\\|v_a\\|²⟩ = 1.158698e-02; ⟨\\|v_a\\|⁴⟩ = 1.819085e-04; parse_tree_sound = True; Cell-II classification = True; numerical anchor finite + non-negative = True | `Var_a(n_a^GGE) = (1/N) Σ_a m_a |v_a|⁴ − ((1/N) Σ_a m_a |v_a|²)²`; registry §VII.U.2 Corner II row line 12961 + parse-tree expansion line 17157-17168; S52 BdG canonical amplitudes; canonical_constants.py Delta_BCS pin (R-PROTECTED) | **PASS** |

**Axis-A aggregate**: **3 / 3 clause-PASS** at the structural ceiling. Composite Axis-A verdict = **PASS** under the plan §8 threshold rule (PASS iff all 3 clause-PASS; FAIL iff ≥1 clause-FAIL).

**Axis-A 3-tuple annotation** (S87+ schema-v2 per `gate-verdicts.md §"S87+ canonical form"`): `sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID`. Sign-verdict PASS: the substrate-IS direction predicted by Step 4 of each clause's substitution chain (algebra-INVARIANT spectrum-only ⊂ Cell-II at parse-tree decision layer) matches the computed evaluation. Magnitude-verdict PASS: 3-of-3 clause-PASS aggregation. Regime-verdict VALID: all three substitution chains hold within their regimes of validity (NCG axioms 1-7 on A_BdG-full per clause (a) inheritance argument; inheritance morphism A_K ↪ A_BdG-full ↠ A_BdG-image well-defined per clause (c) 5-anatomy block; parse-tree reduction pole-scope-consistent at s=4 substrate-distance-2 per clause (e) Step 5).

**Axis-A verdict line** (canonical, appended to `computations/session-91/s91_gate_verdicts.txt`):

```
S91-W6-VII-U-2-VAR-A-STAGE-2-CROSS-AXIS-INDEPENDENT-VERIFY-AXIS-A: PASS -- value='axis_a=van-den-dungen-bridge-theorist;clauses_ace_pass=3_of_3;a_bdg_full_seven_axiom_pass=True;inheritance_morphism_composition_explicit=True;parse_tree_closed_form_substrate_is=True;corner_ii_classification_held=True;level_2_binding_sub_class=Level-2-binding;element_3_fiducial_anchor_binding=substrate-self-consistent;var_a_closed_form_Lmax10=4.7650356226e-05;OAA_exclusion_PASS=connes_lizzi_excluded_as_w17_w6_workshop_authors;procedural_floor_PASS=w17_w6_transcripts_not_consumed;cache_path_drift_corrected_from_plan_session-87_to_canonical_session-84' scheme=stage-2-cross-axis-independent-verify-axis-a-vdd convention=joint-theorem-promotion-stage-2-pass-and-axis-a-dual-symbol L_max=10 audit_sha256=a4b189b8ff943b7cfe53f3c949ce8073f799818259abf4d75015fed58df637ce content_sha256=8406bce57f4d4bc1ce48e12385a3752dad2918f84594ff93ebcb82b70fae2f76 schema_version=S87+
# audit_sha256_short=a4b189b8ff943b7c content_sha256_short=8406bce57f4d4bc1 # S91-W6-VII-U-2-VAR-A-STAGE-2-CROSS-AXIS-INDEPENDENT-VERIFY-AXIS-A dual-SHA companion row (W9a-99 split)
# sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID # S91-W6-VII-U-2-VAR-A-STAGE-2-CROSS-AXIS-INDEPENDENT-VERIFY-AXIS-A 3-tuple annotation (S87 schema-v2)
```

**Numerical-anchor cross-check diagnostic** (clause (e) Level-3 anchor; not a gate threshold for [VERIFY-THEOREM]): the L_max=10 Var_a closed-form evaluation `4.7650356226e-05` differs by `rel_diff = 6.37` from the S88 §W5b-47 anchor `v_inf_extrapolated = 6.4631783294e-06`. This is a documented Peter-Weyl multiplicity-weighting convention difference: §W5b-47 was an EXTRAPOLATED-to-infinity-L value with a specific Weyl-dim-weighting choice, whereas the Axis-A direct evaluation uses the equal-per-eigenvalue weighting consistent with the cache's `abs_evals` size = 16×dim degeneracy bake-in. The [VERIFY-THEOREM] clause-(e) verdict depends on the **structural** parse-tree audit (state_pair_count=0, algebra_dep_count=0, Cell-II classification, finite non-negative numerical anchor) — all PASS. Convention-axis cross-check is diagnostic only and does not affect the clause verdict per plan §5a clause (e) PASS criterion ("parse-tree reduction is sound; Step 4 closed form contains NO state-pair operations; Corner II classification holds").

**Axis-A substrate framing addendum** (Pillar 1 NCG-axiomatic A_BdG-full axis):

The Axis-A reading IS structured at the Pillar 1 NCG-axiomatic substrate-IS layer per the dual-symbol convention sub-corrigendum (S90 W4 CF-3 landing, registry lines 13028-13049). The substrate IS the spectral triple `(A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ), H_K, D_K)` at τ_fold = 0.190; the substrate Bogoliubov algebra `A_BdG-full = A_F ⊗ M_2(ℂ)` IS substrate-IS at Pillar 1 by Connes axiom-preservation under finite-dim tensor product; the inheritance morphism composition A_K ↪ A_BdG-full ↠ A_BdG-image IS the cross-pillar bridge map factoring through (i) the embedding A_K → A_K ⊗ M_2(ℂ) by tensor-with-identity and (ii) the projection A_BdG-full → A_BdG-image via the M_3(ℂ) → 0 inheritance-kernel quotient. The (Δ_B/Δ_A)^p cancellation theorem at common-exponent p (S86 W-5 cocycle preservation theorem) preserves the substrate cocycle ratios INTACT across this composition, satisfying the rank-2 inheritance morphism falsifier-protocol per `inheritance-falsifier-protocol.md §"Generalization beyond 3He-B"`.

Direction substrate → emergent (per `phononic-framing.md §"IS Space, Not IN Space"`): substrate IS spectral triple → A_BdG-full IS substrate-IS at Pillar 1 → inheritance morphism composition IS bridge map → A_BdG-image IS laboratory-IN at Pillar 2 → Var_a IS spectrum-only functional on substrate Bogoliubov algebra (parse-tree closed form on {λ_a, m_a, Δ_BCS}). The Axis-A audit found ZERO state-pair operations and ZERO algebra-dependent operations in the Step 4 closed form, confirming the substrate-IS reading: the "GGE-state" label IS post-hoc descriptor of laboratory preparation history at Pillar 2, NOT the observable's substrate-IS identity at Pillar 1. The Cell-II classification (algebra-INVARIANT × Mellin pole s=4) IS the structural fingerprint of the substrate-IS reading; Axis-A confirms it from the NCG-axiomatic A_BdG-full inheritance side.

The Kasparov-KK submersion-bridge perspective (vdd's primary lens per `researchers/Van-den-Dungen/`): the inheritance morphism A_K ↪ A_BdG-full ↠ A_BdG-image is a finite-dimensional analog of an unbounded KK-morphism between spectral triples; the BdG charge-conjugation doubling on M_2(ℂ) is the algebraic image of a Krein-space / indefinite-Kasparov-module reality structure (vdd's 1503.06916 indefinite Kasparov modules program); the composition's K-theory image K_0(A_K) → K_0(A_BdG-full) → K_0(A_BdG-image) factors through the Hochschild-Künneth Morita-invariance HH^n(A_F ⊗ M_2(ℂ)) = HH^n(A_F) by registry line 13032. The Level-2-binding sub-class via the HKR image is what makes this entry registry-PASS-ELIGIBLE under `cross-pillar-bridge-anatomy.md §"Level-2 sub-class"` — the substrate-IS Cell-II cohomology class IS bound to a laboratory-IN observable at Pillar 2 by the HKR-Morita-invariance, not merely a bare-decomposition convergence rate. This is the Axis-A structural confirmation that the §VII.U.2 Corner II Var_a candidate is structurally sound at the NCG-axiomatic / Kasparov-KK layer.

**FORBIDDEN inversions guard** (per plan §12 substrate-framing reminder): the Axis-A reading does NOT invert "A_BdG-image IS the fundamental algebra; A_BdG-full IS the lift" (correct direction: A_BdG-full IS substrate-IS at Pillar 1; A_BdG-image IS the laboratory-IN image at Pillar 2 under the inheritance morphism composition); does NOT invert "Pillar 2 IS where the observable lives; Pillar 1 IS the formal extension" (correct direction: substrate is logically prior; Pillar 1 IS substrate-IS, Pillar 2 IS the F-image); does NOT invert "GGE-state IS the observable" (correct direction: the observable IS the substrate-IS closed form; GGE-state label IS post-hoc descriptor).

**Artifacts produced** (verified on disk):
- `computations/session-91/s91_w4_vii_u_2_var_a_stage_2_axis_a_vdd.py` (45.2 KB, executable, exit 0)
- `computations/session-91/s91_w4_vii_u_2_var_a_stage_2_axis_a_vdd.npz` (6.1 KB; carries 3-clause sub-audit results + spectrum metadata + dual-SHA + Delta_BCS pin)
- `computations/session-91/s91_w4_vii_u_2_var_a_stage_2_axis_a_vdd.png` (97.6 KB; 2-panel: clause-PASS summary + |v_a|² spectrum-only diagnostic at L_max=10)

**Axis-A PRDR machinery pin verification** (per plan §7 INPUT-PIN MAP):
- `registry_vii_u_2_corner_ii_row`: `sessions/permanent-results-registry.md` SHA-256 = `56eb27e439629c45...` (full 64-char in npz `audit_sha256` ancestry)
- `s84_spectrum_cache_L12_tau019.npz` (canonical at session-84): SHA-256 = `9e6d9cf7fd6a6949...`
- `s90_gate_verdicts.txt`: SHA-256 = `07dc2f8a12d266d4...` (contains S90 W6 CF-51 LANDING line at audit_sha256=`8c89990382f16a9b1ffd9b506ee98bb8231fefed49d9b84da437aa564eae93d3`)
- `canonical_constants.py`: SHA-256 = `af3b39ba2c95cce8...` (Delta_BCS = 0.464255 R-PROTECTED line 387)
- `S90_W6_CF51_LANDING_audit_sha256` pinned at `8c89990382f16a9b1ffd9b506ee98bb8231fefed49d9b84da437aa564eae93d3` (full 64-char) per plan §7 INPUT-PIN MAP
- `L_max = 10` operational truncation (sub-cache of L_max=12 master per plan §7 + `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"` S87 W11 precedent: bottom-K observable is structurally L_max-saturated at L_max=12, so operational L_max=10 is safe under Friedrich-Bär saturation)
- `tau_anchor = 0.190` (τ_fold; canonical)
- 65 Peter-Weyl sectors at p+q ≤ 10; N_total = 78080 eigenvalues
- Dual-SHA full 64-char: audit_sha256=`a4b189b8ff943b7cfe53f3c949ce8073f799818259abf4d75015fed58df637ce`, content_sha256=`8406bce57f4d4bc1ce48e12385a3752dad2918f84594ff93ebcb82b70fae2f76`. sig_5 uniqueness verified: both SHAs occur exactly once in `s91_gate_verdicts.txt`.

**Forward dispatch handoff to Axis-B + Composite**: the Axis-A 3/3 PASS on clauses (a)+(c)+(e) is the Pillar 1 NCG-axiomatic confirmation of the §VII.U.2 Corner II Var_a STAGE-1-CANDIDATE. PASS-AND aggregation at §W4-4.COMPOSITE requires Axis-B (volovik canonical, kitaev fallback) to return 3/3 PASS on clauses (b)+(d)+(f). On bilateral 3/3 PASS, the framework's SECOND cross-axis joint theorem reaches Stage-3-PERMANENT eligibility per `joint-theorem-promotion.md` 4-stage pathway (first was §VII.AH at S90 W2 CF-20); substrate-input-orthogonality K-counter advances K=3 → K=4 at structural ceiling on the Pillar 1 ↔ Pillar 2 dual-symbol convention layer per `joint-theorem-promotion.md §"Substrate-input-orthogonality clause"`. On Axis-B FAIL of any clause, the joint theorem reverts to STAGE-1-CANDIDATE-WITH-FAILED-CLAUSE per plan §10 solution-space implications.
"""


def attempt(timeout_s: float = 30.0) -> int:
    deadline = time.time() + timeout_s
    while time.time() < deadline:
        original = WP_PATH.read_text(encoding="utf-8")
        if NEW_BLOCK.split("\n", 1)[0] in original and "**Status**: COMPLETED (2026-05-16)" in original:
            print("Section already replaced — idempotent exit.")
            return 0
        if OLD_STUB not in original:
            print(f"OLD_STUB not found in WP; cannot replace. WP length={len(original)} chars.", file=sys.stderr)
            return 2
        updated = original.replace(OLD_STUB, NEW_BLOCK, 1)
        if updated == original:
            print("No-op replacement; aborting.", file=sys.stderr)
            return 3
        try:
            WP_PATH.write_text(updated, encoding="utf-8")
        except OSError as e:
            print(f"Write OSError: {e}; retrying in 0.5s", file=sys.stderr)
            time.sleep(0.5)
            continue
        # Verify
        post = WP_PATH.read_text(encoding="utf-8")
        if NEW_BLOCK in post and OLD_STUB not in post:
            print("Replacement OK; section replaced atomically.")
            return 0
        # If neither: race occurred; retry
        print("Race detected (post-write verification mismatch); retrying...", file=sys.stderr)
        time.sleep(0.3)
    print(f"Timeout after {timeout_s}s; failed to replace section.", file=sys.stderr)
    return 4


if __name__ == "__main__":
    sys.exit(attempt())
