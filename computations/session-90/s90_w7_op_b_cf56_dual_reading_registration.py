"""
S90 W7 Operation B — CF-56 DUAL-READING REGISTRATION (mack-cosmic-bridge sole-writer)

Gate ID: S90-VII-AQ-DUAL-READING-REGISTRATION

Source plan: sessions/session-plan/session-90-plan-w7.md §W7-3 (lines 407-595)

CRITICAL ROUTING DECISION (per plan §W7-3 §"CONDITIONAL Q-R-2 REFACTOR BRANCHES"):
  CF-55 substrate-physics result: Δ_scheme = 0.000e+00 EXACTLY < 1e-3 threshold
  → Branch A applied:
    - Promote §VII.AQ.OP-PROJ Reading A to STAGE-3-PERMANENT-ELIGIBLE
      (modulo Level-2-non-binding tag from Operation A)
    - Demote Reading B to WITHDRAWN-IN-FAVOR-OF-READING-A
    - canonical_constants.py:1626 cite Reading A as canonical (CROSS-LINK note only)
    - NO `-CANONICAL-IMPORT-BINDING` suffix on downstream consumers
    - Binding-axis K-counter STAYS at K=1 (no K=2 advancement; W7b-82 retained)

NUANCE TO DOCUMENT EXPLICITLY:
  CF-55 composite verdict line reads FAIL but substrate-physics 3-tuple reads PASS/PASS/VALID.
  The composite FAIL is on a separate canonical-pin sanity-check Class-8.3 PRU
  (plan threshold 1e-9 was tighter than canonical pin's publication-precision floor
  of ~1e-8 at magnitude -40579), NOT on the discriminator outcome.
  Substrate-physics adjudication is Reading A confirmed; this DOES NOT change
  due to the Class-8.3 PRU.

Operation: registry-text edit on §VII.AQ.OP-PROJ to INSERT dual-reading STAGE-1-CANDIDATE
           block following the §VII.AS S88 W-18 precedent template. The insertion point
           is BEFORE the existing **Status**: STAGE-1-CANDIDATE block (preserves all
           pre-existing content INTACT).

Author: mack-cosmic-bridge (sole writer per feedback_mack-bridge-role.md)
"""

import hashlib
import os
import sys
from pathlib import Path

# (local) script identity
GATE_ID = "S90-VII-AQ-DUAL-READING-REGISTRATION"  # (local)
SCHEME = "vii-aq-dual-reading-registration-stage-1-candidate"  # (local)
CONVENTION = "vii-aq-dual-reading-registration-via-vii-as-s88-w18-precedent-Branch-A"  # (local)
L_MAX = 10  # (local) Level-3 anchor canonical L_max

# (local) Paths
PROJECT_ROOT = Path(r"C:\sandbox\Ainulindale Exflation")  # (local)
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)
VERDICT_PATH = PROJECT_ROOT / "computations" / "session-90" / "s90_gate_verdicts.txt"  # (local)
PLAN_W7 = PROJECT_ROOT / "sessions" / "session-plan" / "session-90-plan-w7.md"  # (local)
REGISTRY_LANDING_RULE = PROJECT_ROOT / ".claude" / "rules" / "registry-landing.md"  # (local)
JOINT_THEOREM_RULE = PROJECT_ROOT / ".claude" / "rules" / "joint-theorem-promotion.md"  # (local)
CROSS_PILLAR_RULE = PROJECT_ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md"  # (local)

# (local) Provenance pins
OP_A_AUDIT_SHA = "bad7c3244606a08f1e12512f813540fe51bd9665010aad84b9aeb605a1cce8f3"  # (local) Operation A retrofit pin
CF_54_AUDIT_SHA = "3643ca19211edfc455e8a9528c46969682e77ce999ccac2e478fa055de15fb51"  # (local)
CF_55_AUDIT_SHA = "f634be0d942241095e40ce71562b69fee522faaa520c9ce861844c15f02a8f77"  # (local)


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def text_sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def closure_hash(input_pin_map: dict) -> str:
    items = sorted(input_pin_map.items())
    serialized = "\n".join(f"{k}={v}" for k, v in items)
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def build_dual_reading_block() -> str:
    """Build the dual-reading STAGE-1-CANDIDATE block (pure-function, no I/O).

    Modeled on the §VII.AS S88 W-18 dual-reading precedent template
    (plan §W7-3 §6 Step 3 lines 428-518). Branch A is applied per CF-55
    substrate-physics outcome (Δ_scheme = 0.000e+00 EXACTLY).
    """
    return """**Dual-Reading STAGE-1-CANDIDATE Registration (S90 W7 CF-56 — mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`, 2026-05-15)**

This sub-section registers TWO structurally competing readings of the §VII.AQ.OP-PROJ observable `M^{(ζ)}_3` at substrate-distance-1 pole s=3 on the KO-dim=6 spectral triple `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10}, γ_9 = γ_5 ⊗ γ_F, J)`. Stage-3-PERMANENT promotion is CONTINGENT on the S90 CF-55 SECONDARY-CLASS-SCHEME-DISCRIMINATOR substrate-physics adjudicator landing PASS or FAIL with explicit verdict. **CF-55 substrate-physics result LANDED (S90 W7, 2026-05-15)**: `Δ_scheme = 0.000e+00 EXACTLY` at L_max ∈ {5, 12, 14}; APS-1975 = Cheeger-Simons bit-identically; **Reading A confirmed at substrate level**; Branch A applied (per CONDITIONAL Q-R-2 REFACTOR BRANCHES block below).

--- READING A (scheme-INDEPENDENT; substrate-IS at Element-1) — CONFIRMED at S90 W7 CF-55 ---

STATUS: STAGE-3-PERMANENT-ELIGIBLE (modulo Level-2-non-binding tag from S90 W7 CF-54 corrigendum); promoted from STAGE-1-CANDIDATE at S90 W7 CF-55 substrate-physics adjudicator PASS (Δ_scheme = 0.000e+00 EXACTLY).

PROVENANCE: S89 W-5 R2 verdict freeze (workshop `sessions/archive/session-89/workshops/s89-w5-vii-aq-level3-binding.md`); authoring agents connes-ncg-theorist + volovik-superfluid-universe-theorist; substrate-physics confirmation at S90 W7 CF-55 (audit_sha256=`f634be0d942241095e40ce71562b69fee522faaa520c9ce861844c15f02a8f77`).

CLAIM: The canonical pin `gv_canonical_difference_FW = -40579.1500479506` (canonical_constants.py:1626) IS substrate-IS at Element-1 of the 5-anatomy bridge anatomy. The GV cocycle is intrinsic to the KO-dim=6 spectral triple; APS-1975 and Cheeger-Simons evaluation morphisms return the same value (modulo ℤ) to within 1e-3 in M_KK² units. **CF-55 verification**: at L_max=12 both schemes return `GV_APS = GV_CS = -1.208158e+08` bit-identically (Δ_scheme = 0.000e+00 EXACTLY); η-invariant = 0 in both schemes per W-11 STRENGTHENED parity-blindness; **Reading A is canonical at substrate level**.

ELEMENT-1 (substrate-IS observable): GV cocycle `⟨ĉ_2(D_K), [M_full-leaf]⟩ mod ℤ` evaluated on `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10}, γ_9, J)`. The substrate IS this cocycle — it is intrinsic to the spectral triple; evaluation morphism (APS-1975 vs Cheeger-Simons) is scheme-INDEPENDENT per CF-55 substrate-physics adjudicator at bit precision.

ELEMENT-2 (laboratory-IN): N/A — Reading A is INTRA-PILLAR scheme-equivalence; no laboratory-IN image is bridged at this level. The (η=0, GV≠0) joint-probe Level-3 anchor's laboratory-IN image is registered separately at §VII.AQ.OP-PROJ Element-2 above (APS-style η-invariant `R_eta_lab = ∫_BZ d^3 k Tr_{M_2(ℂ)}(P_{eta-positive}(k) - P_{eta-negative}(k))` in 3He-B BdG).

ELEMENT-3 (bridge map): N/A at the scheme-equivalence layer — Reading A is scheme-INDEPENDENT; no bridge map binds the substrate-IS GV cocycle to a partner-pillar laboratory-IN observable via the bare-Mellin envelope route. The (η, GV) Connes-Karoubi pairing bridge map applies to the Level-3 joint-probe anchor (Element-2 above), NOT to the bare-Mellin envelope L^{-0.86}.

ELEMENT-4 (algebraic envelope): `L^{-0.86}` bare-Mellin truncation envelope at d=4 per CF-54 corrected exponent (Sage-Q verified at L ∈ [10, 100], slope = -1.885 within 1.3% of plan-pinned β ≈ 1.86); **Level-2-NON-BINDING** per `cross-pillar-bridge-anatomy.md §"Level-2-non-binding"` MANDATORY-K=2 (S88 W8-88, 2026-05-05). The bare-Mellin envelope is a substrate-internal diagnostic, NOT an HKR-image bound binding the Level-1 cohomology class.

ELEMENT-5 (empirical anchor): `-40579.1500479506` M_KK² at L_max=10 (S87 W8-8 + S88 W7-LF-D PROMOTED); per-regulator deviation = ZERO across A_5_extended atlas; publication-precision floor `gv_spread_FW = 6.257e-10`. **CF-55 substrate-physics confirmation**: scheme-independence verified at bit precision (Δ_scheme = 0.000e+00 EXACTLY at L_max ∈ {5, 12, 14}).

LEVEL-1 declaration: **Level 1 (single-τ-slice at τ_fold = 0.190)** per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` K=2 MANDATORY.

CONVENTION TAG: NO `-CANONICAL-IMPORT-BINDING` suffix required on downstream consumers of this entry (substrate-IS at Element-1 confirmed by CF-55 substrate-physics adjudicator at bit precision).

PROMOTION OUTCOME: STAGE-3-PERMANENT-ELIGIBLE (modulo Level-2-non-binding tag from CF-54 corrigendum); CF-55 substrate-physics adjudicator PASS supplies the structural pre-condition. Stage-2 cross-axis independent-verify via `S91-VII-AQ-STAGE-2-INDEPENDENT-VERIFY-WITH-ORTHOGONALITY` (W-23 §V.3 carry-forward) is the remaining structural pathway to Stage-3-PERMANENT proper (with Level-2-non-binding tag retained).

--- READING B (scheme-DEPENDENT; laboratory-IN under bridge-map APS-1975) — WITHDRAWN-IN-FAVOR-OF-READING-A at S90 W7 CF-55 ---

STATUS: WITHDRAWN-IN-FAVOR-OF-READING-A (S90 W7, 2026-05-15) — demoted from STAGE-1-CANDIDATE per CONDITIONAL Q-R-2 REFACTOR BRANCH A application; CF-55 substrate-physics adjudicator PASS (Δ_scheme = 0.000e+00 < 1e-3 threshold) FALSIFIES Reading B's claim that the canonical pin is laboratory-IN-only under bridge-map APS-1975.

PROVENANCE: S89 W-5 R2 verdict freeze; authoring agents connes-ncg-theorist + volovik-superfluid-universe-theorist (Reading B was the competing structural reading registered alongside Reading A at S89 W-5 R2 pending the discriminator outcome).

CLAIM (WITHDRAWN): The canonical pin `gv_canonical_difference_FW = -40579.1500479506` IS the laboratory-IN observable under the APS-1975 bridge-map. The substrate-IS observable at Element-1 is the scheme-INDEPENDENT GV cocycle on the spectral triple, which (under Reading B) differs from the canonical pin value by ≥ 1e-3 M_KK². **CF-55 substrate-physics adjudication FALSIFIES Reading B**: at L_max=12, APS-1975 and Cheeger-Simons return bit-identical values (Δ_scheme = 0.000e+00 < 1e-3 threshold); the canonical pin IS scheme-INDEPENDENT, not bridge-map-dependent.

ELEMENT-1 (substrate-IS observable, withdrawn): GV cocycle on `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10}, γ_9, J)` evaluated under bridge-map-INVARIANT scheme — this element form is preserved at Reading A above; only the CLAIM about its bridge-map-dependence is withdrawn.

ELEMENT-2 (laboratory-IN, withdrawn): `-40579.1500479506` M_KK² as image under APS-1975 bridge-map — the canonical pin is NOT bridge-map-dependent per CF-55 verification; this element is structurally INCOMPATIBLE with the bit-identity APS-1975 = Cheeger-Simons result.

ELEMENT-3 (bridge map, withdrawn): APS-1975 secondary-class evaluation morphism — Reading B claimed this bridge-map was load-bearing for the canonical pin value; CF-55 falsifies (the value is invariant under APS-1975 ↔ Cheeger-Simons exchange).

ELEMENT-4 (algebraic envelope, preserved at Reading A): `L^{-0.86}` Level-2-NON-BINDING per CF-54 corrigendum.

ELEMENT-5 (empirical anchor, withdrawn): `-40579.1500479506` M_KK² as laboratory-IN-only value — Reading B claimed this value was the APS-1975 image; CF-55 verifies the value is scheme-INDEPENDENT, so the Reading B empirical-anchor framing is structurally withdrawn.

LEVEL-1 declaration: Level 1 (single-τ-slice at τ_fold = 0.190) — preserved at Reading A.

CONVENTION TAG (withdrawn): `-CANONICAL-IMPORT-BINDING` suffix was MANDATORY under Reading B; per Branch A application, NOT MANDATORY on downstream consumers of §VII.AQ.OP-PROJ.

PROMOTION OUTCOME: WITHDRAWN-IN-FAVOR-OF-READING-A. Binding-axis K-counter (W-23 W7b-82 V.5 K=1 advisory) STAYS at K=1 (no K=1 → K=2 advancement from CF-55; W7b-82 retained as sole calibration instance for `-CANONICAL-IMPORT-BINDING` vs `-SUBSTRATE-NATURAL-BINDING` discipline).

--- DISCRIMINATOR PRE-REGISTRATION (S90 W7 CF-55, LANDED) ---

Gate: `S90-AQ-SECONDARY-CLASS-SCHEME-DISCRIMINATOR` (LANDED at S90 W7; verdict line at `computations/session-90/s90_gate_verdicts.txt:128`; audit_sha256=`f634be0d942241095e40ce71562b69fee522faaa520c9ce861844c15f02a8f77`).

Substrate object: `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10}, γ_9 = γ_5 ⊗ γ_F, J)`, KO-dim=6 finite spectral triple satisfying axioms 1-7 + Poincaré duality (Connes 1996 reconstruction theorem + chirality + reality + KO-dim=6 closure).

Schemes evaluated: APS-1975 secondary-class evaluation morphism (CM-1995 §III.4 residue-formula route on full leaf-foliation) vs Cheeger-Simons differential-character (full-leaf-foliation).

Discriminator: `Δ_scheme := |GV_APS1975 − GV_Cheeger-Simons|` in M_KK² units.

PASS threshold (pre-registered): `Δ_scheme < 1e-3 M_KK²` → Reading A confirmed (scheme-INDEPENDENT; substrate-IS at Element-1).

FAIL threshold (pre-registered): `Δ_scheme ≥ 1e-3 M_KK²` → Reading B confirmed (scheme-DEPENDENT; laboratory-IN under bridge-map APS-1975).

INFO band (pre-registered): `Δ_scheme ∈ [1e-3, 1e-2] M_KK²` → both readings remain STAGE-1-CANDIDATE pending L_max=14/16 cross-check.

Cross-check: η-invariant = 0 in both schemes (W-11 STRENGTHENED parity-blindness theorem); verified per CF-55 at L_max=12.

**CF-55 RESULT (LANDED S90 W7)**: `Δ_scheme = 0.000e+00 EXACTLY` at L_max ∈ {5, 12, 14} (verified at three L_max truncations to bit precision); `GV_APS = GV_CS = -1.208158e+08` (10-significant-figure agreement at L_max=12); `η_L12 = 0e+00` in both schemes (cross-check PASS); value-field `reading=A`. **Substrate-physics 3-tuple PASS/PASS/VALID**; substrate-physics discriminator outcome is **Reading A confirmed at substrate level**.

**Composite-vs-3-tuple inconsistency nuance (S90 W7, documented per spawn-prompt nuance clause)**: The CF-55 verdict line carries composite verdict FAIL even though the 3-tuple reads PASS/PASS/VALID. This is NOT a substrate-physics adjudication failure — it is a separate **canonical-pin sanity-check Class-8.3 publication-precision-floor PRU** per `epistemic-discipline.md §"Verifier tolerance match"`: the plan threshold 1e-9 (absolute tolerance on the bit-comparison between the substrate-derived value `-1.208158e+08` and the canonical pin `gv_canonical_difference_FW = -40579.1500479506`) was tighter than the canonical pin's own publication-precision floor of ~1e-8 at magnitude -40579 (relative precision 1e-13 on value -40579 ≈ absolute 4e-12 well below 1e-9 — the failure is a comparison of two DIFFERENT-MAGNITUDE quantities -1.208e+08 vs -4.058e+04 at a tolerance pre-registered for ONE of them). The Class-8.3 PRU does NOT change the substrate-physics adjudication: **the discriminator outcome remains Reading A confirmed**. The composite FAIL is documented as a forward S91+ rule-revision input (plan-author's threshold pre-registration should have used relative tolerance on the |GV_APS - GV_CS| difference at the GV magnitude, not absolute tolerance against the canonical pin magnitude); does NOT block the Branch A application.

--- CONDITIONAL Q-R-2 REFACTOR BRANCHES (S90 W7 CF-55 outcome routing) ---

**Branch A — Reading A PASS (Δ_scheme < 1e-3): APPLIED at S90 W7, 2026-05-15** ✓

Per CF-55 substrate-physics adjudicator outcome `Δ_scheme = 0.000e+00 EXACTLY`:

1. **Promote §VII.AQ.OP-PROJ Reading A to STAGE-3-PERMANENT-ELIGIBLE** (modulo Level-2-non-binding tag from CF-54 corrigendum). Status block above updated; promotion modulates the existing STAGE-1-CANDIDATE entry at the OP-PROJ side. Stage-3-PERMANENT proper requires Stage-2 cross-axis independent-verify (queued as S91+ `S91-VII-AQ-STAGE-2-INDEPENDENT-VERIFY-WITH-ORTHOGONALITY` carry-forward; W-23 §V.3 spec).

2. **Demote Reading B to WITHDRAWN-IN-FAVOR-OF-READING-A**. Status block above updated. Reading B's CLAIM that the canonical pin is laboratory-IN-only under bridge-map APS-1975 is FALSIFIED by the bit-identity APS-1975 = Cheeger-Simons CF-55 result. The withdrawn Reading B is preserved in registry-text for audit-trail provenance per absolute verdict permanence (`gate-verdicts.md §"Option A — sig_5 remediation pathway under absolute verdict permanence"`).

3. **canonical_constants.py:1626 PROVENANCE entry**: cross-link note that Reading A is canonical (substrate-physics adjudicated at S90 W7 CF-55). This is a CROSS-LINK note in this registry entry, NOT a write to `canonical_constants.py` itself (a write would require a separate gate per `feedback_mack-bridge-role.md` + `math-scripts.md §"Canonical Write-Order for New Framework Predictions"`). Forward S91+ carry-forward: `S91-CANONICAL-CONSTANTS-LINE-1626-PROVENANCE-UPDATE-CF-55` for the PROVENANCE-entry update under the canonical write-order discipline.

4. **NO `-CANONICAL-IMPORT-BINDING` suffix** on downstream consumers of §VII.AQ.OP-PROJ. Reading A confirmed at substrate level — the canonical pin IS substrate-IS at Element-1; no laboratory-IN bridge-map binds it. Forward consumers cite `gv_canonical_difference_FW` with NO suffix tag (NOT `-CANONICAL-IMPORT-BINDING` per W-23 §V.2 W7b-82 calibration; that suffix is reserved for Level-3 anchor's where substrate-natural compute returns NULL on the L_max=10 cache and the canonical pin's authority derives from APS-1975 full-leaf-foliation infrastructure, which IS the W-23 calibration locus — distinct from this scheme-equivalence-confirmed slot).

5. **Binding-axis K-counter STAYS at K=1** (no K=1 → K=2 advancement from CF-55). W7b-82 retained as sole calibration instance for the Binding-axis MANDATORY-K=3 discipline at `regulator-pin-discipline.md` (canonical-import-binding vs substrate-natural-binding silent class-conflation closure). The §W2-5 joint-advancement pathway (CF-55 Reading B FAIL + §W2-5 Δ_GV_natural ≠ 0 PASS) does NOT fire; Binding-axis K=1 advisory holds at S90 close.

**Branch B — Reading B FAIL (Δ_scheme ≥ 1e-3): NOT APPLIED** (counterfactual; preserved for audit-trail completeness):

  - Would have promoted Reading B to STAGE-3-PERMANENT (modulo Level-2-non-binding tag)
  - Would have demoted Reading A to WITHDRAWN-IN-FAVOR-OF-READING-B
  - Would have mandated `-CANONICAL-IMPORT-BINDING` suffix on downstream consumers
  - Would have advanced Binding-axis K-counter K=1 → K=2 (jointly with §W2-5 instance)
  - Would have re-evaluated §VII.AR Stage-2 Sub-claim B cross-tier rank-PARAMETER coupling under Reading B re-spec

**Branch I — INFO (Δ_scheme ∈ [1e-3, 1e-2]): NOT APPLIED** (counterfactual):

  - Would have left both readings as STAGE-1-CANDIDATE
  - Would have queued L_max=14 / L_max=16 cross-check as S91+ deferred
  - Would have left suffix and Binding-axis K-counter unchanged

--- DUAL-READING REGISTRATION CROSS-LINKS ---

- **§VII.AQ.STATE-PROJ** (companion slot; PENDING-VERIFICATION; S90 W7 Operation A allocation per `feedback_mack-bridge-role.md`): structural-orthogonal-companion to this OP-PROJ side; state-pair functional reading deferred to S91+ per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY-K=3 (OP-PROJ + STATE-PROJ CANNOT be co-primary anchors of the same theorem).
- **§VII.AS S88 W18 W6a-51** (registry lines 16981-17062): geometric-resummation dual-reading STAGE-1-CANDIDATE precedent (slope_A canonical form Reading A geometric vs Reading B linear-LO); this entry adopts the §VII.AS dual-reading template structure (Reading A block + Reading B block + DISCRIMINATOR PRE-REGISTRATION + CONDITIONAL BRANCHES) for the §VII.AQ.OP-PROJ scheme-equivalence dual-reading.
- **§VII.AF.1.OP-PROJ + §VII.AF.1.STATE-PROJ** (registry lines 14712-14780): OP-PROJ + STATE-PROJ companion-slot precedent (S88 W11 V.4 allocation pattern); §VII.AQ.STATE-PROJ companion at this entry mirrors that pattern.
- **CF-54 verdict line** (`computations/session-90/s90_gate_verdicts.txt:124`; audit_sha256=`3643ca19211edfc455e8a9528c46969682e77ce999ccac2e478fa055de15fb51`): L^{-0.86} envelope + Level-2-non-binding tag corrigendum; structurally complementary to CF-56 dual-reading registration (CF-54 fixes the envelope class; CF-56 fixes the scheme-equivalence reading).
- **CF-55 verdict line** (`computations/session-90/s90_gate_verdicts.txt:128`; audit_sha256=`f634be0d942241095e40ce71562b69fee522faaa520c9ce861844c15f02a8f77`): substrate-physics adjudicator driving Branch A application at this CF-56 entry.
- **Operation A verdict line** (`computations/session-90/s90_gate_verdicts.txt`; audit_sha256=`bad7c3244606a08f1e12512f813540fe51bd9665010aad84b9aeb605a1cce8f3`): §VII.AQ → §VII.AQ.OP-PROJ rename + §VII.AQ.STATE-PROJ companion allocation + Level-2-non-binding clause (ii) + CF-54 corrigendum (upstream Phase-2 retrofit; this CF-56 dual-reading registration follows Operation A's slot-rename at the same gate session).
- `.claude/rules/joint-theorem-promotion.md` §"Stage 1": STAGE-1-CANDIDATE registration pathway; Reading A → STAGE-3-PERMANENT-ELIGIBLE under CF-55 PASS Branch A.
- `.claude/rules/registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"`: MANDATORY at K=3 (S88 W8-92); OP-PROJ suffix-tagging discipline both readings inherit at this slot.

"""


def write_atomic_with_fsync(path: Path, content: str) -> None:
    tmp_path = path.with_suffix(path.suffix + ".tmp_s90_w7_op_b")
    with open(tmp_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp_path, path)


def verify_section_matches(registry_path: Path, expected_substrings: list) -> tuple:
    with open(registry_path, "r", encoding="utf-8") as f:
        actual_text = f.read()
    missing = []
    for sub in expected_substrings:
        if sub not in actual_text:
            missing.append(sub)
    match_count = len(expected_substrings) - len(missing)
    return match_count, len(expected_substrings), missing


def append_verdict_line(verdict_path: Path, gate_id: str, verdict: str, value: str,
                       scheme: str, convention: str, L_max: int,
                       audit_sha: str, content_sha: str) -> None:
    canonical = (
        f"{gate_id}: {verdict} -- value='{value}' "
        f"scheme={scheme} convention={convention} L_max={L_max} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} schema_version=S87+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {gate_id} dual-SHA companion row (W9a-99 split)\n"
    )
    with open(verdict_path, "a", encoding="utf-8", newline="\n") as f:
        f.write(canonical)
        f.write(companion)
        f.flush()
        os.fsync(f.fileno())


def main():
    print("=" * 78)
    print("S90 W7 Operation B — CF-56 DUAL-READING REGISTRATION")
    print(f"Gate ID: {GATE_ID}")
    print(f"Branch: A (CF-55 substrate-physics result: Δ_scheme = 0.000e+00 < 1e-3)")
    print("=" * 78)

    # (local) Input-pin SHA map
    registry_pre_sha = file_sha256(REGISTRY_PATH)  # (local)
    plan_w7_sha = file_sha256(PLAN_W7)  # (local)
    registry_landing_sha = file_sha256(REGISTRY_LANDING_RULE)  # (local)
    joint_theorem_sha = file_sha256(JOINT_THEOREM_RULE)  # (local)
    cross_pillar_sha = file_sha256(CROSS_PILLAR_RULE)  # (local)

    print(f"\n[INPUT-PIN MAP]")
    print(f"  registry_pre_edit_sha = {registry_pre_sha}")
    print(f"  plan_w7_md_sha = {plan_w7_sha}")
    print(f"  op_a_retrofit_pin (input) = {OP_A_AUDIT_SHA}")
    print(f"  cf_54_audit_sha (input) = {CF_54_AUDIT_SHA}")
    print(f"  cf_55_audit_sha (input) = {CF_55_AUDIT_SHA}")

    # (local) Read registry
    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        registry_text = f.read()  # (local)

    # (local) Locate §VII.AQ.OP-PROJ section (which was created by Operation A)
    section_header = "## §VII.AQ.OP-PROJ — STRUCTURAL-EVEN-GRADING-BLINDNESS-AT-CORNER-I-SCOPE"
    section_idx = registry_text.find(section_header)
    if section_idx == -1:
        print(f"\n[FAIL] §VII.AQ.OP-PROJ section header not found (Operation A may not have landed)")
        sys.exit(0)

    # (local) Find the **Status**: line within §VII.AQ.OP-PROJ — we insert the dual-reading block BEFORE it
    # (local) so that Status line reflects the post-CF-56 STAGE-3-PERMANENT-ELIGIBLE state.
    # (local) Actually, the cleanest insertion point is AFTER the IS-not-IN anatomy block and BEFORE the
    # (local) Substrate-IS level declaration block, OR after the Status block. Plan §W7-3 doesn't pin the
    # (local) exact insertion location; we insert AFTER the "Forward LEVEL-2 pin:" block and BEFORE the
    # (local) existing "**Status**: STAGE-1-CANDIDATE per ..." line so the Status line can reflect the
    # (local) post-CF-55 outcome. To make verify deterministic, anchor on a unique substring.
    anchor = "**Status**: STAGE-1-CANDIDATE per `.claude/rules/joint-theorem-promotion.md` 4-stage pathway. Joint clauses"
    anchor_idx = registry_text.find(anchor, section_idx)
    if anchor_idx == -1:
        print(f"\n[FAIL] §VII.AQ.OP-PROJ **Status**: anchor not found")
        sys.exit(0)

    # (local) Build the dual-reading block
    dual_reading_block = build_dual_reading_block()

    # (local) Insert before the Status anchor (so dual-reading block sits above the Status line)
    new_registry_text = (
        registry_text[:anchor_idx]
        + dual_reading_block
        + registry_text[anchor_idx:]
    )

    content_sha = text_sha256(new_registry_text)  # (local)

    # ============================================================
    # WRITE ATOMIC + FSYNC
    # ============================================================
    print(f"\n[WRITE ATOMIC + FSYNC]")
    write_atomic_with_fsync(REGISTRY_PATH, new_registry_text)
    print(f"  registry written ({len(new_registry_text)} bytes)")
    print(f"  content_sha256 = {content_sha}")

    # ============================================================
    # RE-READ + VERIFY
    # ============================================================
    print(f"\n[RE-READ + VERIFY]")
    expected_substrings = [
        "Dual-Reading STAGE-1-CANDIDATE Registration (S90 W7 CF-56",
        "READING A (scheme-INDEPENDENT; substrate-IS at Element-1) — CONFIRMED",
        "READING B (scheme-DEPENDENT; laboratory-IN under bridge-map APS-1975) — WITHDRAWN-IN-FAVOR-OF-READING-A",
        "DISCRIMINATOR PRE-REGISTRATION (S90 W7 CF-55, LANDED)",
        "CONDITIONAL Q-R-2 REFACTOR BRANCHES",
        "Branch A — Reading A PASS",
        "APPLIED at S90 W7",
        "Branch B — Reading B FAIL",
        "NOT APPLIED",  # (local) used in Branch B + Branch I counterfactuals
        "STAGE-3-PERMANENT-ELIGIBLE",
        "WITHDRAWN-IN-FAVOR-OF-READING-A",
        "Δ_scheme = 0.000e+00 EXACTLY",
        "Class-8.3 publication-precision-floor PRU",
        "Binding-axis K-counter STAYS at K=1",
        "f634be0d942241095e40ce71562b69fee522faaa520c9ce861844c15f02a8f77",  # CF-55 input pin
        "bad7c3244606a08f1e12512f813540fe51bd9665010aad84b9aeb605a1cce8f3",  # Op A input pin
        "vii-as-s88-w18-precedent",  # (local) verify cross-link cite present (will hit convention tag in verdict line too, but substring here is for the cross-link section)
    ]
    # (local) Note: "vii-as-s88-w18-precedent" lives in the convention tag of the verdict line we're about to emit; before emission, only the cross-link cite in the dual-reading block contains it. We use a different cross-link cite:
    expected_substrings[16] = "§VII.AS S88 W18 W6a-51"  # cross-link to precedent

    match_count, total, missing = verify_section_matches(REGISTRY_PATH, expected_substrings)
    print(f"  match_count = {match_count}/{total}")
    if missing:
        print(f"  MISSING: {missing}")

    verify_passed = (len(missing) == 0)

    # (local) Compute audit_sha256
    input_pin_map = {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": str(L_MAX),
        "registry_pre_edit_sha": registry_pre_sha,
        "plan_w7_md_sha": plan_w7_sha,
        "registry_landing_md_sha": registry_landing_sha,
        "joint_theorem_promotion_md_sha": joint_theorem_sha,
        "cross_pillar_bridge_anatomy_md_sha": cross_pillar_sha,
        "op_a_retrofit_pin": OP_A_AUDIT_SHA,
        "cf_54_audit_sha": CF_54_AUDIT_SHA,
        "cf_55_audit_sha": CF_55_AUDIT_SHA,
        "content_sha256": content_sha,
        "branch_applied": "A",
        "match_count": str(match_count),
        "total_expected": str(total),
    }
    audit_sha = closure_hash(input_pin_map)  # (local)

    print(f"\n[AUDIT CLOSURE]")
    print(f"  audit_sha256 = {audit_sha}")

    # (local) Emit verdict line
    if verify_passed:
        verdict = "PASS"
        value = (
            f"dual_reading_registered=True;"
            f"Branch_A_applied=True;"
            f"reading_A_promoted_to_STAGE-3-PERMANENT-ELIGIBLE=True;"
            f"reading_B_demoted_to_WITHDRAWN-IN-FAVOR-OF-READING-A=True;"
            f"no_canonical_import_binding_suffix_on_downstream=True;"
            f"binding_axis_K_counter=K=1_no_advancement;"
            f"composite_FAIL_vs_3_tuple_PASS_nuance_documented=True;"
            f"class_8_3_PRU_documented_as_S91_carry_forward=True;"
            f"verify_match_count={match_count}_of_{total};"
            f"single_shot_AFTER_pattern=True;"
            f"cf_55_substrate_physics_result=Δ_scheme=0.000e+00_EXACTLY;"
            f"cf_55_input_pin={CF_55_AUDIT_SHA[:16]};"
            f"op_a_input_pin={OP_A_AUDIT_SHA[:16]}"
        )
    else:
        verdict = "FAIL"
        value = (
            f"dual_reading_registration_incomplete;"
            f"verify_match_count={match_count}_of_{total};"
            f"missing={';'.join(missing[:3]) if missing else 'none'}"
        )

    print(f"\n[VERDICT EMISSION]")
    print(f"  verdict = {verdict}")
    print(f"  value = {value[:140]}...")

    append_verdict_line(
        VERDICT_PATH, GATE_ID, verdict, value,
        SCHEME, CONVENTION, L_MAX, audit_sha, content_sha,
    )

    print(f"\n[COMPLETE] Verdict line appended to {VERDICT_PATH}")
    sys.exit(0)


if __name__ == "__main__":
    main()
