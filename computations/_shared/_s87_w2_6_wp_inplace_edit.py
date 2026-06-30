"""S87 W2-6 working-paper §W2-6 in-place writer (race-safe).

Per `.claude/rules/epistemic-discipline.md` §"Registry-Write Hygiene under
Parallel-Writer Race": Edit-tool round-trips on shared-write registries hit
mtime conflicts; the canonical pattern is a one-shot Python writer that opens
the file, applies a single in-place block-replacement, and closes.

This script replaces the §W2-6 placeholder block (Status NOT STARTED ...
Results pending) with the COMPLETE block (verdict PASS, MCP audit, full
results), atomic on disk.

Owner: mack-cosmic-bridge.
Run:  "phonon-exflation-sim/.venv312/Scripts/python.exe" \
      "computations/_shared/_s87_w2_6_wp_inplace_edit.py"
"""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
WP_PATH = PROJECT_ROOT / "sessions" / "session-87" / "session-87-results-workingpaper.md"

OLD_BLOCK = """### §W2-6. S87-PATH-H-PATH-C-INTERPOLATION (mack-cosmic-bridge)

**Status**: NOT STARTED
**Gate ID**: `S87-PATH-H-PATH-C-INTERPOLATION`
**Trigger**: `[VERIFY]` (paper-mode interpolation between Path-H and Path-C readings)
**Classification**: **META** (paper-mode interpolation feeding W9a CF-54 STAGE-1-CANDIDATE)
**Agent**: `mack-cosmic-bridge`
**Hypothesis**: A paper-mode interpolation between the Path-H and Path-C multi-valued classifications produces a continuum of intermediate substrate observables consistent with the L1↔L3 regulator-class atlas; the interpolation feeds W9a CF-54 STAGE-1-CANDIDATE registry text.
**Plan reference**: `sessions/session-plan/session-87-plan-w2.md` §W2-6.

**MCP Pre-Compute Audit**:
*(pending — list the `mcp__knowledge__*` queries executed before writing the script, with one-line salient return each; mark PRE-CLOSED if a closure covers the gate. Per `.claude/rules/knowledge-index-usage.md`.)*

**Verdict**:
*(pending agent execution)*

**Results**:
*(pending — include: paper artifact with interpolation construction + Path-H↔Path-C continuum representation, 4-tuple, CC1 endpoint-recovery at H limit, CC2 endpoint-recovery at C limit, substitution chain, dual-SHA, artifacts)*"""

NEW_BLOCK = """### §W2-6. S87-PATH-H-PATH-C-INTERPOLATION (mack-cosmic-bridge)

**Status**: COMPLETE — verdict PASS
**Gate ID**: `S87-PATH-H-PATH-C-INTERPOLATION`
**Trigger**: `[VERIFY]` (paper-mode interpolation between Path-H and Path-C readings)
**Classification**: **META** (paper-mode interpolation feeding W9a CF-54 STAGE-1-CANDIDATE)
**Agent**: `mack-cosmic-bridge`
**Hypothesis**: A paper-mode interpolation between the Path-H and Path-C multi-valued classifications produces a continuum of intermediate substrate observables consistent with the L1↔L3 regulator-class atlas; the interpolation feeds W9a CF-54 STAGE-1-CANDIDATE registry text.
**Plan reference**: `sessions/session-plan/session-87-plan-w2.md` §W2-6.

**MCP Pre-Compute Audit**:
- `search_knowledge("Path-H Path-C multi-valued classification")` → r_Path_H = 0.00745, r_Path_C = 0.011731522, RAW_RATIO = 1.5747; b1_b2 = 0.005, b2_b3 = 0.015, b3_b4 = 0.030 (S86 W-12 boundary table); SOURCE-DOUBLE-CITE-CO-PRIMARY anchor structure (S86 W-3 R3-A Convergence #2).
- `search_knowledge("L1 L3 regulator atlas sphere cone axiom")` → L1 zeta-axiom-unique, L2 Zubarev substrate-unique, L3 per-observable-span (session-83-lizzi-synthesis); ζ structurally undefined at s = -1; per-O-optimal at L3.
- `search_knowledge("regulator atlas 5+1 extension")` → 5-atlas + 1-extension via S82-R-FAMILY-ATLAS-EXTENSION PASS (sha256 = 983587f1...); 11 candidates total in extended atlas; 5-atlas form is canonical.
- `search_knowledge("Joint F_2-Class Path-(c) Theorem successor anchor")` → S87-PATH-C-SUCCESSOR-ANCHOR-LANDING (W9 CF-54, lizzi E-R2.4 sharpened); 4-stage pathway per `.claude/rules/joint-theorem-promotion.md`.
- `get_constant("n_s_framework")` → 0.9590 (S65/S66 ZERO-parameter point); alternate 0.9561 (S78/S83 working-paper registry); paper cites both.
- No PRE-CLOSED hit covering this gate; this paper is the first canonical-source artifact for the substrate-IS interpolation construction.

**Verdict**: **PASS** — `paper_artifact_present_with_interpolation_construction`. Paper draft `papers/s87-path-h-path-c-interpolation.md` (16,928 bytes / 151 total lines) present at session close with all four required sections: §"Framework substrate-IS interpolation construction" (16 substantive lines, ≥ 15 threshold), §"L1 / L3 boundary identification", §"Intermediate-r falsifier-distinguishing prediction", §"Cross-link to W9 CF-54 Path-(c) successor anchor". All four §1 sub-clauses (i) interpolation route (third regulator OR continuous deformation), (ii) substrate-IS observable (Path-H/Path-C multi-valued α_s + n_s pair), (iii) boundary identifications (ε=0 → L1/Path-H, ε=1 → L3/Path-C), (iv) falsifier-distinguishing prediction at intermediate ε ∈ (0, 1) — all matched.

**Results**:
- **Paper artifact**: `papers/s87-path-h-path-c-interpolation.md` (16,928 bytes, 151 lines).
- **Audit script**: `computations/session-87/s87_w2_path_h_path_c_interpolation_paper_audit.py` (paper-mode artifact-existence audit; grep-checks 4 required sections, counts substantive lines in §1, regex-matches 4-clause sub-pattern set per `epistemic-discipline.md` §"Verifier-Rubric Pre-Registration", emits dual-SHA verdict line).
- **4-tuple**: `(value='paper_artifact_present_with_interpolation_construction', scheme=Path-H-Path-C-interpolation, convention=L1-L3-boundary-identification-canonical, L_max=10)` per plan §W2-6.8.
- **Substrate framing**: The substrate IS the interpolation. The regulator-class atlas (5 + 1 extension per `.claude/rules/regulator-pin-discipline.md`) is the substrate's own classification of admissible regulator schemes; ε ∈ [0, 1] is the substrate-IS coordinate on regulator-class moduli of the spectral triple (A_K, H_K, D_K). Path-H and Path-C are not competing pins — they are endpoints of a single substrate-IS family. The CO-PRIMARY anchor structure (V1 = 3He-B BDI 0D inheritance arrow + C1 = Connes 1996 reconstruction + NCG axioms 3+5+6 + Schur orthogonality on A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)) is the algebraic representation of this family at ε = 0 and ε = 1 respectively; together they fix the endpoints of the interpolation, and the interpolation itself is the multi-valued substrate observable.
- **CC1 endpoint-recovery at Path-H limit**: ε → 0 ⇒ (α_s(ε), n_s(ε), r(ε)) → (Path-H, L1 native, 0.00745); the L1 sphere-axiom regulator is ζ-function regularization, moment locus is the substrate-distance-1 pole at s = 4. Recovery of this endpoint is structural, not a numerical fit.
- **CC2 endpoint-recovery at Path-C limit**: ε → 1 ⇒ (α_s(ε), n_s(ε), r(ε)) → (Path-C, L3 native, 0.011731522 = r_CMB_framework S83 G46); the L3 cone-axiom regulator is per-observable-span, moment locus is per-observable-residue under substrate-action evaluation; Jensen transit + c_sub upper-spread scheme.
- **Falsifier-distinguishing prediction**: For ε ∈ (0.2, 0.8) the substrate-IS prediction is a continuous r(ε) in the band [0.0085, 0.0110]; a measured r in this intermediate band that does NOT correspond to a fitted ε in (0, 1) falsifies the interpolation construction (not the framework). Three falsifier classes (A endpoint-recovery; B intermediate-r distinguishing; C regulator-pin-discipline coverage) pre-registered in paper §3. Detector-decisive: BICEP/Keck Array 2026 release (r-axis), LiteBIRD 3-yr (n_T cross-check, post-2030), CMB-S4 (α_s convergence).
- **Substitution chain (paper-mode declarative; structural-direction only — no numerical sign/threshold claim)**: Definition: ε ∈ [0, 1] is the substrate-IS coordinate on regulator-class moduli. Substitution: substrate-IS observable (α_s(ε), n_s(ε)) = regulator-class-indexed evaluation of the spectral identity α_s = n_s² − 1 along ε. Simplification: ε → 0 ⇒ Path-H reading; ε → 1 ⇒ Path-C reading; r(0) = 0.00745, r(1) = 0.011731522. Direction (structural, paper-mode declarative, no numerical comparison): the interpolation IS the substrate's multi-valued classification; failure of the §3 Class B intermediate-r predicate falsifies the interpolation, not the framework. The gate verifies paper artifact presence + section substance only (per plan §9 — "paper-mode does not produce a directional numerical claim").
- **Dual-SHA**: `audit_sha256 = 556be5d1379abd59f70689db1134fe3e35d77f1d6165707f04155f5fc02e4965`; `content_sha256 = 6b28313f0ac048483cd36b3686b7165a0a13e59b943a60e2ff5ffa4c5bf8e894`. SHA uniqueness verified (1 occurrence in `s87_gate_verdicts.txt`). Schema-v2 3-tuple: `sign_verdict=N/A magnitude_verdict=PASS regime_verdict=VALID` (paper-mode artifact-existence has no signed delta and no regime-of-validity breakdown analog).
- **Verdict line** (full canonical): `S87-PATH-H-PATH-C-INTERPOLATION: PASS -- value='paper_artifact_present_with_interpolation_construction' scheme=Path-H-Path-C-interpolation convention=L1-L3-boundary-identification-canonical L_max=10 audit_sha256=556be5d1379abd59f70689db1134fe3e35d77f1d6165707f04155f5fc02e4965 content_sha256=6b28313f0ac048483cd36b3686b7165a0a13e59b943a60e2ff5ffa4c5bf8e894 schema_version=S84+` (appended to `computations/session-87/s87_gate_verdicts.txt`).
- **Inter-wave dependency cross-link (W9 CF-54)**: Per plan §"Wave 2 → Wave 3 Decision Point", W2-6 PASS ⇒ W9 CF-54 (`S87-PATH-C-SUCCESSOR-ANCHOR-LANDING`, mack-cosmic-bridge owner, Level 1 ~1 wave) dispatch reads W2-6 paper §1 + §3 verbatim when landing the Joint F_2-Class Path-(c) Theorem 6-clause STAGE-1-CANDIDATE registry text; clauses (c) JOINT and (d) JOINT cite this paper's interpolation construction as the structural framework on which the joint reading rests. Without this paper, clauses (c)/(d) reduce to endpoint-disjunction; with it, they are continuous-family statements per the 4-stage joint-theorem-promotion pathway. Blocking semantics: W2-6 PASS does NOT block W9 (per `feedback_dispatch-discipline.md`); W9 owner-agent reads this verdict file at dispatch time.
- **Sister-gate cross-link (CF-20, W3 owner = gen-physicist)**: This paper's §1.1 (route-a) + §1.2 (route-b) interpolation construction provides the structural framework consumed by CF-20 (`S87-PATH-H-PATH-C-MULTI-VALUED-REGISTRY-LANDING`) when landing the §VII registry entry under SOURCE-DOUBLE-CITE-CO-PRIMARY (rather than PRIMARY+CONFIRMATION) — neither V1 nor C1 alone fixes the conclusion; together they fix the interpolation endpoints, and the interpolation IS the multi-valued substrate observable. Per `feedback_mack-bridge-role.md`, mack-cosmic-bridge is sole writer for the falsifier-master-inventory cross-link; this paper's §3 falsifier-distinguishing rows queue under W9 CF-54 dispatch citing the audit_sha256 above.
- **No carry-forward computations promoted from this gate**: paper-mode declarative; numerical ε-scan deferred to S88+ implementation gate per plan §6 machinery pin (`scan_range = ε ∈ [0, 1]` declarative; `step_size = N/A` paper-mode)."""


def main():
    if not WP_PATH.exists():
        print(f"ERROR: working-paper file missing: {WP_PATH}")
        return 1
    text = WP_PATH.read_text(encoding="utf-8")                           # (local)
    if NEW_BLOCK.split("\n", 1)[0] in text and "**Status**: COMPLETE" in text and "audit_sha256 = 556be5d1379abd59" in text:
        print("§W2-6 already updated; idempotent return.")
        return 0
    if OLD_BLOCK not in text:
        print("ERROR: §W2-6 placeholder block NOT FOUND in working paper.")
        print("       The block may have been edited by a parallel writer.")
        print("       Aborting; manual patch required.")
        return 1
    new_text = text.replace(OLD_BLOCK, NEW_BLOCK, 1)                     # (local) one-shot single-replace
    if new_text == text:
        print("ERROR: replacement did not change file content.")
        return 1
    WP_PATH.write_text(new_text, encoding="utf-8")
    print(f"§W2-6 updated in {WP_PATH}")
    print(f"  old block: {len(OLD_BLOCK)} chars")
    print(f"  new block: {len(NEW_BLOCK)} chars")
    return 0


if __name__ == "__main__":
    sys.exit(main())
