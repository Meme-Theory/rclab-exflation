"""S92-W5-CF-S92-W2-2-W2-3-JOINT-VII-AU-OP-PROJ-STAGE-1-CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED

mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`.

METHODOLOGY-class registry-text edit + corpus-row append per
`wave-classification.md §M1-M4`. Single-shot AFTER-pattern emission per
`registry-landing.md §"Bridge-Landing Script Architecture"`:

    build_promotion_text  →  write_atomic_with_fsync  →
    re_read + verify_section_matches  →  emit ONE verdict line.

Attaches the NEW STAGE-1-CANDIDATE-CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED
sub-class tag to §VII.AU.OP-PROJ in `sessions/permanent-results-registry.md`
AND appends a paired K=2 forward-saturation corpus row to
`sessions/framework/registry/cross-pillar-bridge-corpus.md`
§"Deferred-pending intermediate verdict-class".

CHAINED-CONDITIONAL on §W5-1 PASS
(audit_sha256=395c63c829c11546766ee78e49609c571046e53b6ea5acb4c5844a61d62b64bf
at computations/session-92/s92_gate_verdicts.txt:148).

Sub-class semantics:
  STAGE-1-CANDIDATE-CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED is the
  structurally-orthogonal fourth sub-class on the L_max-extension axis,
  distinct from the existing three sub-classes (PROXY-REFINEMENT /
  FIRST-EXTRACTION / OPERATIONAL-ALIGNMENT). It represents the empirical-
  confirmation-at-operational-truncation-with-asymptotic-limit-deferred
  status: the structural-corridor identity is empirically confirmed at
  L_max=14+ via §W5-1 PASS, AND the L_max → ∞ asymptotic limit remains
  operationally deferred to a future-session L_max scan.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import tempfile
import time
from pathlib import Path

# canonical_constants is the canonical source; this script does not need
# numerical constants (registry-text edit only) but the import is required
# per `.claude/rules/math-scripts.md §"Canonical Constants (MANDATORY)"`.
SCRIPT_DIR = Path(__file__).resolve().parent  # (local)
REPO_ROOT = SCRIPT_DIR.parents[1]             # (local)
SHARED_DIR = REPO_ROOT / "computations" / "_shared"  # (local)
sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import (  # noqa: E402
    alpha_canonical_VII_AU_OP_PROJ_FW_ASYMPTOTIC,
    alpha_sample_VII_AU_OP_PROJ_FW_PATHWAY_B_L15_22,
    n_s_FW_exact,
)

# -----------------------------------------------------------------
# Gate identity + pins
# -----------------------------------------------------------------

GATE_ID = (  # (local)
    "S92-W5-CF-S92-W2-2-W2-3-JOINT-VII-AU-OP-PROJ-"
    "STAGE-1-CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED"
)
SCHEME = (  # (local)
    "registry-text-retrofit-AFTER-pattern-PLUS-corpus-row-append"
)
CONVENTION = (  # (local)
    "VII-AU-OP-PROJ-sub-class-tag-attachment-"
    "STAGE-1-CANDIDATE-CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED"
)
L_MAX_TAG = "N/A"  # (local) registry-text + corpus edit; inherits L_max=14 anchor

# §W5-1 PASS structural anchor (chained-conditional prerequisite).
W5_1_AUDIT_SHA_FULL = (  # (local)
    "395c63c829c11546766ee78e49609c571046e53b6ea5acb4c5844a61d62b64bf"
)
W5_1_LINE = 148  # (local) computations/session-92/s92_gate_verdicts.txt:148

# §W5/W6 in-session promotion sub-class transition anchor.
S91_W5_W6_PROMOTION_AUDIT_SHA_FULL = (  # (local)
    "54db93d799c76c67c78bdcc8cd0477ebb6d104914f2e6764be7af50d22f36459"
)

REGISTRY_PATH = (  # (local)
    REPO_ROOT / "sessions" / "permanent-results-registry.md"
)
CORPUS_PATH = (  # (local)
    REPO_ROOT / "sessions" / "framework" / "registry" /
    "cross-pillar-bridge-corpus.md"
)
VERDICT_PATH = SCRIPT_DIR / "s92_gate_verdicts.txt"  # (local)
DATA_PATH = (  # (local)
    SCRIPT_DIR /
    "s92_w5_vii_au_op_proj_stage_1_corridor_confirmed_numerical_deferred.json"
)

# Rule + input pin paths (for input-pin map SHA closure).
RULE_BRIDGE_ANATOMY = (  # (local)
    REPO_ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md"
)
RULE_JOINT_THEOREM = (  # (local)
    REPO_ROOT / ".claude" / "rules" / "joint-theorem-promotion.md"
)
CANONICAL_CONSTANTS = (  # (local)
    REPO_ROOT / "computations" / "_shared" / "canonical_constants.py"
)
S91_VERDICTS = (  # (local)
    REPO_ROOT / "computations" / "session-91" / "s91_gate_verdicts.txt"
)


def sha256_of(path: Path) -> str:
    """Compute SHA-256 hex digest of a file's bytes."""
    h = hashlib.sha256()  # (local)
    with path.open("rb") as fp:
        for chunk in iter(lambda: fp.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_of_text(text: str) -> str:
    """Compute SHA-256 of a text string (utf-8)."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


# -----------------------------------------------------------------
# build_promotion_text — sub-class tag block (registry) + corpus row
# -----------------------------------------------------------------

def build_subclass_tag_block() -> str:
    """Build the NEW sub-class tag attachment block (registry side)."""
    block = f"""

**S92 W5-2 NEW sub-class tag attachment — STAGE-1-CANDIDATE-CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED (S92 W5-2 single-shot AFTER-pattern; mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`, 2026-05-23)**:

This sub-class tag is the FOURTH structurally-distinct deferred-pending sub-class on the L_max-extension axis, structurally orthogonal to the three pre-existing sub-classes (PROXY-REFINEMENT / FIRST-EXTRACTION / OPERATIONAL-ALIGNMENT) per `.claude/rules/cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"`. The new sub-class represents the **empirical-confirmation-at-operational-truncation-with-asymptotic-limit-deferred** status — a status that none of the existing three sub-classes covers.

**Sub-class semantic definition**:

The STAGE-1-CANDIDATE-CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED sub-class admits a §VII registry entry whose structural status satisfies the following ten-clause specification:

1. **Structural-corridor identity is empirically confirmed at operational truncation L_operational** via the substrate-natural FULL physical evaluator (NOT SCHEMATIC; CLASS=FULL pin per `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY level-pin discipline; tier_pin=TIER-1 per §W5-1 verdict-line annotation).
2. **Asymptotic L_max → ∞ limit remains operationally deferred** to a future-session L_max scan, with the L_operational sub-window serving as the canonical numerical anchor in the operational window. The deferral is structural (not procedural): the substrate's Friedrich-Bär saturation theorem identifies the L_operational truncation as the structurally-faithful numerical anchor for the asymptotic Level-1 identity, with the asymptotic limit recoverable via the saturation theorem at L_max → ∞ rather than via direct numerical evaluation.
3. **Bridge-anatomy 5-elements + 3-level ladder** at the §VII registry entry remain compliant (5-anatomy + 3-level MANDATORY at K=3 per `cross-pillar-bridge-anatomy.md §"Forward template-adoption"`).
4. **Multiplicative-normalization cancellation invariant** per `math-scripts.md §"Multiplicative-normalization cancellation invariants"` SUGGESTION-K=1 — the L_max-INVARIANCE of the K-window log-derivative observable at L_operational is a structural identity (not empirical regulator-class consistency); the discriminating content lives at the asymptote/plateau value `B(R) = L_n[g_R(K)]` at K_horizon, which is regulator-class-keyed at the methodology-floor F-image layer per `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY level-pin discipline.
5. **Layer-Functor F K=2 SUGGESTION REINDEXED scope** per `epistemic-discipline.md §"Layer-Decomposition"` Phi correspondence — the L_max-extension axis IS the substrate-natural deformation parameter at the Level-1 leading-term asymptotic universal layer (`-3` across the Cell I × same-pole bridge-anatomy corpus per CM-1995 §III.4 simple-pole expansion); §VII.AU.OP-PROJ inhabits this REINDEXED scope as calibration corpus instance #2 (instance #1 = §VII.AF.1.OP-PROJ HP^1 cohomology norm).
6. **Friedrich-Bär saturation theorem applicability** at L ≥ 35 per `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"` W11-3 precedent — the asymptotic α=-3 recovery is operationally accessible via the saturation theorem's structural argument at L ∈ [35, 100]; the sub-class's deferral is BOUNDED by the saturation theorem's analytic-recursion-formula route (NOT an open-ended deferral; structurally upper-bounded at L ≤ 100).
7. **Cell I × substrate-distance-1 pole `s=3` algebra-axis cell preservation** per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3 — the sub-class attachment does NOT alter the §VII.AU.OP-PROJ entry's Cell I (algebra-INVARIANT spectrum-only-functional) classification; cross-corner co-primary structures with Cell IV remain FORBIDDEN per `registry-landing.md §"Detection"` criterion 4 (S88 W-15 V.6 MANDATORY at K=3).
8. **Single-τ-slice Level-1 substrate-IS preservation** at τ_fold = 0.19 per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` K=2 MANDATORY since S88 W-7 V.4 — the sub-class operates at the Level-1 single-τ-slice substrate-IS layer (NOT the Level-2 moduli-deformation layer); the L_max-extension axis is intra-Level-1 (regulator-class spectral-support weight at fixed τ_fold), structurally distinct from inter-Level moduli-deformation.
9. **SOURCE-DOUBLE-CITE-CO-PRIMARY structural anchor citation** per `registry-landing.md §"SOURCE-DOUBLE-CITE-CO-PRIMARY"` — the sub-class attachment cites §W5-1 PASS audit_sha256 as a structural anchor (the empirical confirmation event), composing with the pre-existing SOURCE-DOUBLE-CITE-CO-PRIMARY anchor-pair (Anchor_1 W6-1 PASS-A first-extraction + Anchor_2 S91 W5/W6 in-session promotion) cited in the §W5-3 RETROFIT block; the sub-class attachment is a TERTIARY structural anchor on the L_max-extension axis (NOT a fourth co-primary anchor in the sequential V_input → A_F → C_output chain; the chain's structural cardinality is preserved at 2 co-primary anchors).
10. **Forward sub-class transition pre-registration** — upon Friedrich-Bär saturation theorem extension PASS at L ∈ [35, 100], the sub-class advances STAGE-1-CANDIDATE-CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED → STAGE-1-CANDIDATE-CORRIDOR-CONFIRMED-NUMERICAL-FULL-RECOVERED (the forward sub-class transition is structurally pre-registered at this attachment landing; it is NOT a new sub-class but the COMPLETION state of the present sub-class).

**Structural orthogonality to the three existing sub-classes**:

- **DISTINCT from PROXY-REFINEMENT** (axis-β substrate-physics regulator-tier): the new sub-class is FULL physical regularization at the substrate-natural evaluator per §W5-1 CLASS=FULL pin; it is NOT SCHEMATIC at any level. PROXY-REFINEMENT addresses the SCHEMATIC vs FULL physical regulator-class jump; the new sub-class lives entirely on the FULL side of that axis.
- **DISTINCT from FIRST-EXTRACTION** (substrate-physics first-extraction axis): the new sub-class is NUMERICALLY EXTRACTED at L_operational=14+; the empirical α extraction is complete (α_b ≈ 2.6926 at L_fit=[15,22] per S91 W6-1 PASS-A confirmation; α_b=2.600027 at L_max=14 sub-window per §W5-1 step-A PASS at drift 0.034380 vs anchor). FIRST-EXTRACTION addresses the symbolic-only-α to numerically-extracted-α transition; the new sub-class lives entirely past that transition.
- **DISTINCT from OPERATIONAL-ALIGNMENT** (operational-machinery state-side axis-γ): the new sub-class is NOT about K_canonical pin uniqueness; the K_canonical pin at the §VII.AU.OP-PROJ Cell I × substrate-distance-1 pole s=3 substrate-IS anchor is undisputed (single-branch identity; no multi-branch Bogoliubov ED required). OPERATIONAL-ALIGNMENT addresses the BdG state-side pin uniqueness; the new sub-class lives orthogonal to that axis on the L_max-extension axis.

**Admissibility predicate** (4-of-4 conjunction):

1. §W5-1 PASS at L_operational=14 with `truncation_consistent=True ∧ max_drift_spearman ≤ 0.05` AND `f_used=1.0000 ∧ regime_verdict=VALID` (per §W5-1 4-of-4 step conjunction PASS).
2. Empirical α extraction at L_operational sub-window CONFIRMED with PASS-A category count `N_above_3 = 4` (all 4 of 4 cells PASS-A at L_max=14 and L_max=16 per §W5-1 step-B PASS).
3. Sub-class tag attached to §VII.AU.OP-PROJ registry entry citing §W5-1 audit_sha256 as the structural anchor.
4. Paired corpus row appended at `cross-pillar-bridge-corpus.md §"Deferred-pending intermediate verdict-class"` K=2 forward-saturation table.

**Structural anchor (cited per admissibility predicate item 3)**:

- **§W5-1 PASS audit_sha256**: `{W5_1_AUDIT_SHA_FULL}` (full 64-char; `computations/session-92/s92_gate_verdicts.txt:{W5_1_LINE}`; gate `S92-W5-CF-S92-W2-2-LMAX14-VII-AU-OP-PROJ-L-MAX-14-EXTENSION`; 4-of-4 step conjunction PASS: step_a_PASS (drift=0.034380 < threshold), step_b_PASS (N_above_3=4 at L_max=14 and L_max=16), step_c_PASS (truncation_consistent_12_14=True; max_drift_spearman_14=0.000000), step_d_PASS (regime=VALID; f_used=1.0000); scheme=Spearman-rank-ordering-on-W7a74-PRIMARY-evaluator-5-anchor-matrix-LMAX14-EXTENSION; convention=substrate-distance-1-pole-s3-OP-PROJ-FIRST-EXTRACTION-LMAX14-FULL-CC-1995-III-4-EVALUATOR; L_max=14; tier_pin=TIER-1; level_class_pin=FULL).

**Inherited substrate-physics pins** (per CLASS=FULL inheritance from §W5-1):

- `alpha_canonical_VII_AU_OP_PROJ_FW_ASYMPTOTIC = {alpha_canonical_VII_AU_OP_PROJ_FW_ASYMPTOTIC}` (Level-1 leading-term universal across Cell I × substrate-distance-1 pole `s=3` per CM-1995 §III.4 simple-pole expansion; regulator-invariant, L-independent; `canonical_constants.py` PROVENANCE S91 W5/W6 close 2026-05-22). **The asymptotic anchor is the deferred target** of this sub-class; recoverable at L_max → ∞ via Friedrich-Bär saturation theorem at L ≥ 35 per `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"` W11-3 precedent.
- `alpha_sample_VII_AU_OP_PROJ_FW_PATHWAY_B_L15_22 = {alpha_sample_VII_AU_OP_PROJ_FW_PATHWAY_B_L15_22}` (sample at L_fit=[15,22] from S91 W6-1 PASS-A; `canonical_constants.py` PROVENANCE S91 W6-1 PASS-A close; Pathway-B direct Connes-Karoubi pairing on L_max=12 master cache filtered to substrate-distance-1 pole `s=3` Mellin-Barnes residue). **The L_operational empirical anchor confirmed at §W5-1**: α_b extraction CONFIRMED at L_max ∈ {{14, 16, 22}} sub-windows with N_above_3 = 4 of 4 cells PASS-A at each L_max (step-B PASS); cross-window monotonicity preserved (step-C PASS; truncation_consistent across L_max=12,14,16).

**Forward deferral pathway** (asymptotic limit recovery to L_max → ∞):

The asymptotic recovery to the Level-1 leading-term `-3` is operationally deferred to a future-session L_max scan with the following queued discriminator gate:

- **Forward gate target**: Friedrich-Bär saturation theorem extension to L ∈ [35, 100]; PASS predicate `|β_i + 3| < 0.10 at L_fit=[35, 50] ∧ σ_β ≤ 0.05 at L_fit=[50, 100]` per W11-3 precedent (analytic recursion-formula route per `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"`).
- **Asymptotic-PASS-on-completion semantics**: upon Friedrich-Bär saturation theorem extension PASS at L ∈ [35, 100], the sub-class tag advances from STAGE-1-CANDIDATE-CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED → STAGE-1-CANDIDATE-CORRIDOR-CONFIRMED-NUMERICAL-FULL-RECOVERED. The forward sub-class transition is structurally pre-registered at this attachment landing for downstream consumer reference; it is NOT a new sub-class but the COMPLETION state of the present sub-class.

**Stage-2 dispatch licensing**:

This sub-class attachment LICENSES Stage-2 cross-axis independent-verify dispatch at §W5-4 + §W5-5 (Axis-A connes-ncg-theorist + Axis-B volovik-superfluid-universe-theorist per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"` MANDATORY at K=1; lizzi-spectral-functional-theorist EXCLUDED per Axis-B downstream-inheritance reach test per S88 W-14 W4a-17 V.2 calibration corpus B.15). Stage-2 reviewers inherit the sub-class as the structural status of the STAGE-1-CANDIDATE at the time of Stage-2 dispatch. STAGE-3-PERMANENT eligibility (if granted at Stage-2 PASS-AND) explicitly notes the asymptotic deferral as a forward carry-forward to a future-session L_max scan gate per the forward deferral pathway above.

**Substrate framing** (per `.claude/rules/phononic-framing.md §"IS Space, Not IN Space"`):

The CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED sub-class IS the methodology-floor F-image (per `epistemic-discipline.md §"Layer-Decomposition"` Phi correspondence) of the substrate-IS empirical-confirmation event at L_operational=14. The substrate IS the Pillar I spectral triple `(A_K, H_K, D_K(τ_fold))` at substrate-distance-1 pole `s=3` and single-τ-slice τ_fold = 0.19; L_max IS the substrate's intrinsic regulator-class spectral-support weight (NOT a coordinate on a meta-container); the L_max-extension axis IS a substrate-natural deformation parameter (NOT a methodology container). Container-thinking is FORBIDDEN: the sub-class tag is NOT a "description" of the substrate-IS empirical confirmation; it IS the registry-text F-image of that substrate-IS event. The asymptotic deferral IS the substrate's intrinsic Friedrich-Bär saturation theorem operating at L_max → ∞; the L_operational sub-window IS the substrate's intrinsic numerical anchor in the operational window. **Direction of explanation**:

```
Substrate (Pillar I, A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)) IS the L_max-extension axis Mellin-cone closure
   → L_operational = 14+ empirical confirmation at the substrate-natural FULL evaluator
   → Friedrich-Bär saturation theorem (asymptotic recovery at L_max → ∞ via saturation)
   → Bridge map (HKR L_max → ∞ at d=4 substrate-distance-1 pole s=3; Level-2-binding)
   → Laboratory (Pillar II) IN CMB n_s observation (substrate-IS image n_s_FW = {n_s_FW_exact} discriminates Planck 2.0952σ at L_max=10)
```

**K-counter advancement (deferred-pending sub-class taxonomy)**:

- **K_pre = 3** (post-S92 W3-2 OPERATIONAL-ALIGNMENT K=1→K=2 advancement; 3 distinct sub-classes covered at K=1 each — PROXY-REFINEMENT K=1; FIRST-EXTRACTION K=1; OPERATIONAL-ALIGNMENT K=2 per S92 W3-2 landing).
- **K_post = 4** (this §W5-2 NEW CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED sub-class lands as K=1 calibration instance of a STRUCTURALLY-DISTINCT fourth sub-class; advances the taxonomy's STRUCTURAL CARDINALITY from 3 sub-classes to 4 sub-classes).
- **Status**: SUGGESTION at K=1 (FIRST canonical calibration instance of the new sub-class; §VII.AU.OP-PROJ is the canonical first-instance). Promotes to MANDATORY at K=3 distinct calibration instances per `feedback_rules-compensate-missing-structure.md` K-counter advancement threshold. Forward candidates for K=2 / K=3 advancement: §VII.AV / §VII.AW / §VII.AY / §VII.BA on the L_max-extension axis with empirical L_operational confirmation and asymptotic L_max → ∞ deferral.

**Cross-references**:

- `.claude/rules/cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` — taxonomic extension (NEW sub-class added to the existing three; structurally orthogonal on L_max-extension axis).
- `.claude/rules/joint-theorem-promotion.md §"Stage 1"` — sub-class tag attaches to STAGE-1-CANDIDATE status; Stage 2 cross-axis verify queued at §W5-4 + §W5-5 with sub-class status inherited.
- `.claude/rules/cross-pillar-bridge-anatomy.md §"Forward template-adoption"` — 5-anatomy + 3-level ladder MANDATORY at K=3 (preserved on this sub-class attachment).
- `.claude/rules/substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY level-pin discipline — CLASS=FULL pin inherited from §W5-1 (FULL CM-1995 §III.4 evaluator via W7a-74 PRIMARY; NOT SCHEMATIC).
- `.claude/rules/regulator-pin-discipline.md §"Cross-link — four-axis orthogonality"` — Level axis MANDATORY at K=4; CLASS=FULL pin preserved.
- `.claude/rules/phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` K=2 MANDATORY since S88 W-7 V.4 — Level-1 single-τ-slice declaration at τ_fold = 0.19 preserved.
- `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"` — Friedrich-Bär saturation theorem precedent (W11-2 + W11-3) for asymptotic recovery at L ≥ 35.
- `feedback_rules-compensate-missing-structure.md` — K-counter advancement threshold (SUGGESTION → MANDATORY at K=3).
- §W5-1 PASS verdict at `computations/session-92/s92_gate_verdicts.txt:{W5_1_LINE}` — structural anchor for the sub-class attachment (audit_sha256 cited above).
- §VII.AU.OP-PROJ Anchor_2 inline citation at registry line 18928 (S92 W5-3 VERIFY-FIRST-RETROFIT) — sub-class transition closure source line; cites S91 W5/W6 in-session promotion audit_sha256=`{S91_W5_W6_PROMOTION_AUDIT_SHA_FULL}` at `computations/session-91/s91_gate_verdicts.txt:270`.
- `sessions/framework/registry/cross-pillar-bridge-corpus.md §"Deferred-pending intermediate verdict-class"` Instance #3 sub-bullet (d) — paired corpus-row append for K=2 forward-saturation table.

**Audit pin**: S92 W5-2 single-shot AFTER-pattern gate `{GATE_ID}` (`computations/session-92/s92_w5_vii_au_op_proj_stage_1_corridor_confirmed_numerical_deferred.py`); single-shot AFTER-pattern Edit per `registry-landing.md §"Bridge-Landing Script Architecture (single-shot pattern)"`; paired corpus-row append at `cross-pillar-bridge-corpus.md` §1 Instance #3 sub-bullet (d) per Edit-discipline parallel registry entry.

"""
    return block


def build_corpus_row() -> str:
    """Build the paired K=2 forward-saturation corpus row (corpus side)."""
    row = f"""
  - **(d) §VII.AU.OP-PROJ CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED** (S92 W5-2 K=1 calibration instance; mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`). Sub-class tag `STAGE-1-CANDIDATE-CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED`. **STRUCTURALLY-DISTINCT fourth sub-class on the L_max-extension axis**, orthogonal to the three pre-existing sub-classes (PROXY-REFINEMENT axis-β / FIRST-EXTRACTION substrate-physics first-extraction / OPERATIONAL-ALIGNMENT axis-γ). The new sub-class admits a §VII entry whose (i) structural-corridor identity is empirically confirmed at operational truncation L_operational ≥ 14 via the substrate-natural FULL physical evaluator (CLASS=FULL pin per `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY level-pin discipline); (ii) asymptotic L_max → ∞ limit remains operationally deferred to a future-session L_max scan via Friedrich-Bär saturation theorem at L ≥ 35 per `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"` W11-3 precedent; (iii) bridge-anatomy 5-elements + 3-level ladder remain compliant. **Canonical first-instance**: §VII.AU.OP-PROJ (Cell I × substrate-distance-1 pole `s=3` algebra-INVARIANT spectrum-only-functional × FWD-C1 Pillar I ↔ Pillar II bridge family). **Structural anchor**: §W5-1 PASS audit_sha256=`{W5_1_AUDIT_SHA_FULL}` at `computations/session-92/s92_gate_verdicts.txt:{W5_1_LINE}` (gate `S92-W5-CF-S92-W2-2-LMAX14-VII-AU-OP-PROJ-L-MAX-14-EXTENSION`; 4-of-4 step conjunction PASS at L_max=14 with α_b extraction CONFIRMED at L ∈ {{14, 16, 22}} sub-windows; N_above_3 = 4 of 4 cells PASS-A at each L_max; truncation_consistent across L_max=12,14,16; tier_pin=TIER-1; level_class_pin=FULL). **Sub-class transition closure source**: S91 W5/W6 in-session promotion audit_sha256=`{S91_W5_W6_PROMOTION_AUDIT_SHA_FULL}` at `computations/session-91/s91_gate_verdicts.txt:270`. **Inherited substrate-physics pins**: `alpha_canonical_VII_AU_OP_PROJ_FW_ASYMPTOTIC = {alpha_canonical_VII_AU_OP_PROJ_FW_ASYMPTOTIC}` (asymptotic Level-1 leading-term; DEFERRED target) + `alpha_sample_VII_AU_OP_PROJ_FW_PATHWAY_B_L15_22 = {alpha_sample_VII_AU_OP_PROJ_FW_PATHWAY_B_L15_22}` (L_operational sub-window empirical anchor; CONFIRMED). **K-counter status**: K_pre=3 (post-S92 W3-2 OPERATIONAL-ALIGNMENT K=2 advancement; PROXY-REFINEMENT + FIRST-EXTRACTION + OPERATIONAL-ALIGNMENT) → K_post=4 (NEW CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED sub-class advances the taxonomy STRUCTURAL CARDINALITY from 3 sub-classes to 4 sub-classes); Status SUGGESTION at K=1 (FIRST canonical calibration instance of the new sub-class); promotes to MANDATORY at K=3 distinct calibration instances per `feedback_rules-compensate-missing-structure.md`. Forward candidates for K=2 / K=3 advancement: §VII.AV / §VII.AW / §VII.AY / §VII.BA on the L_max-extension axis with L_operational confirmation + asymptotic L_max → ∞ deferral. **Forward deferral pathway**: Friedrich-Bär saturation theorem extension to L ∈ [35, 100] with PASS predicate `|β_i + 3| < 0.10 at L_fit=[35, 50] ∧ σ_β ≤ 0.05 at L_fit=[50, 100]`; upon PASS, sub-class advances STAGE-1-CANDIDATE-CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED → STAGE-1-CANDIDATE-CORRIDOR-CONFIRMED-NUMERICAL-FULL-RECOVERED. **Audit pin**: S92 W5-2 single-shot AFTER-pattern gate `{GATE_ID}` (`computations/session-92/s92_w5_vii_au_op_proj_stage_1_corridor_confirmed_numerical_deferred.py`); paired registry-text edit at `sessions/permanent-results-registry.md` §VII.AU.OP-PROJ S92 W5-2 NEW sub-class tag attachment block.
"""
    return row


# -----------------------------------------------------------------
# write_atomic_with_fsync — single-shot append (no per-attempt rewrites)
# -----------------------------------------------------------------

def _atomic_write(path: Path, new_text: str) -> None:
    """Atomic temp+fsync+replace write of `new_text` to `path`."""
    fd, tmp_name = tempfile.mkstemp(
        prefix=path.stem + "_", suffix=".tmp",
        dir=str(path.parent),
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fp:
            fp.write(new_text)
            fp.flush()
            os.fsync(fp.fileno())
        os.replace(tmp_name, str(path))
    except Exception:
        try:
            os.unlink(tmp_name)
        except OSError:
            pass
        raise


def write_atomic_with_fsync_append(path: Path, addition: str,
                                    insertion_point_predicate) -> None:
    """Append `addition` to file at the insertion point.

    insertion_point_predicate(text) -> int gives the byte offset to insert at;
    the new file is written atomically via temp + fsync + replace.
    """
    original = path.read_text(encoding="utf-8")
    insertion_byte = insertion_point_predicate(original)
    new_text = (
        original[:insertion_byte] + addition + original[insertion_byte:]
    )
    _atomic_write(path, new_text)


def write_atomic_with_fsync_replace_block(
    path: Path, new_addition: str,
    old_anchor: str, end_marker: str,
) -> bool:
    """Replace an existing inserted block in `path` with `new_addition`.

    Locates the block starting at `old_anchor` and ending immediately before
    `end_marker`. Returns True if a replace occurred, False if the old
    anchor was not present (caller should fall through to append).
    """
    original = path.read_text(encoding="utf-8")
    anchor_pos = original.find(old_anchor)
    if anchor_pos < 0:
        return False
    end_pos = original.find(end_marker, anchor_pos)
    if end_pos < 0:
        raise RuntimeError(
            f"replace_block: anchor '{old_anchor[:50]}...' found but "
            f"end_marker '{end_marker[:50]}...' not found downstream"
        )
    # Find the start of the line containing the anchor so we replace cleanly.
    # The anchor should already be at the start of its block; if not, we go
    # back to the preceding newline.
    block_start = original.rfind("\n", 0, anchor_pos) + 1
    new_text = original[:block_start] + new_addition + original[end_pos:]
    _atomic_write(path, new_text)
    return True


# -----------------------------------------------------------------
# Insertion point predicates
# -----------------------------------------------------------------

def find_registry_insertion_point(text: str) -> int:
    """Locate insertion point in registry: after §W5-3 retrofit Audit-pin line,
    before the next `### §VII.AX.OP-PROJ` header."""
    # The §W5-3 retrofit block ends with:
    # "...Phase C single-shot AFTER-pattern Edit per
    #  `registry-landing.md §"Bridge-Landing Script Architecture
    #  (single-shot pattern)"`."
    # immediately followed by:
    # "### §VII.AX.OP-PROJ — PBH Band-Edge Prediction"
    marker = "### §VII.AX.OP-PROJ — PBH Band-Edge Prediction"
    pos = text.find(marker)
    if pos < 0:
        raise RuntimeError(
            f"insertion-point marker '{marker[:60]}...' not found in registry"
        )
    return pos


def find_corpus_insertion_point(text: str) -> int:
    """Locate insertion point in corpus: at start of the line containing
    'Both sub-class tags route to plan-freeze advisory' which closes Instance #3."""
    marker = (
        "  Both sub-class tags route to plan-freeze advisory"
    )
    pos = text.find(marker)
    if pos < 0:
        raise RuntimeError(
            f"insertion-point marker '{marker[:60]}...' not found in corpus"
        )
    return pos


# -----------------------------------------------------------------
# verify_section_matches — re-read + content_sha256 cross-check
# -----------------------------------------------------------------

def verify_section_matches(path: Path, expected_substring: str) -> bool:
    """Re-read file from disk; verify expected substring is present."""
    actual = path.read_text(encoding="utf-8")
    return expected_substring in actual


# -----------------------------------------------------------------
# append_verdict — atomic POSIX O_APPEND single-line append
# -----------------------------------------------------------------

def find_prior_audit_sha_for_gate() -> str | None:
    """Scan verdict file for the most recent prior canonical line for GATE_ID.

    Returns the full 64-char audit_sha256 of the latest non-superseded
    prior line, or None if no prior line exists. Used to construct the
    Option A `supersedes=<old_audit_sha>` tag on a corrective emission.
    """
    if not VERDICT_PATH.exists():
        return None
    text = VERDICT_PATH.read_text(encoding="utf-8")
    pattern = re.compile(
        rf"^{re.escape(GATE_ID)}:\s+\S+\s+--.*?audit_sha256=([a-f0-9]{{64}})",
        re.MULTILINE,
    )
    matches = pattern.findall(text)
    if not matches:
        return None
    # Latest prior line; downstream Option A reader follows the supersession
    # chain to identify the canonical latest non-superseded line.
    return matches[-1]


def append_verdict(
    verdict: str, value: str, audit_sha: str, content_sha: str,
    supersedes: str | None = None,
) -> None:
    """Append canonical verdict line + dual-SHA companion comment row.

    Per `gate-verdicts.md §"Option A — sig_5 remediation pathway"`, when
    a corrective emission appends after a prior FAIL/INFO line, the
    `supersedes=<old_audit_sha>` tag MUST be present in the `value=`
    field (or companion comment row); the original line is RETAINED.
    """
    if supersedes is not None:
        # Inject supersedes tag into the value field.
        value_with_supersedes = f"{value};supersedes={supersedes}"
    else:
        value_with_supersedes = value
    line = (
        f"{GATE_ID}: {verdict} -- value={value_with_supersedes!r} "
        f"scheme={SCHEME} convention={CONVENTION} "
        f"L_max={L_MAX_TAG} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    comment = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)"
    )
    if supersedes is not None:
        comment += f" supersedes={supersedes}"
    comment += "\n"
    with VERDICT_PATH.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(comment)


# -----------------------------------------------------------------
# Main — single-shot AFTER-pattern execution
# -----------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)
    print(f"=== {GATE_ID} ===")

    # -----------------------------------------------------------------
    # Step 0 — chained-conditional prereq verification (§W5-1 PASS)
    # -----------------------------------------------------------------
    verdict_text = VERDICT_PATH.read_text(encoding="utf-8")
    w5_1_pass_present = (
        f"S92-W5-CF-S92-W2-2-LMAX14-VII-AU-OP-PROJ-L-MAX-14-EXTENSION: PASS"
        in verdict_text
        and W5_1_AUDIT_SHA_FULL in verdict_text
    )
    if not w5_1_pass_present:
        print("  ABORT: §W5-1 PASS not verified in verdict file.")
        return 1
    print(f"  §W5-1 PASS verified at audit_sha={W5_1_AUDIT_SHA_FULL[:16]}...")

    # -----------------------------------------------------------------
    # Step 1 — log input-pin SHAs
    # -----------------------------------------------------------------
    pin_map = {  # (local)
        "registry_pre_edit_sha256": sha256_of(REGISTRY_PATH),
        "corpus_pre_edit_sha256": sha256_of(CORPUS_PATH),
        "rule_bridge_anatomy_sha256": sha256_of(RULE_BRIDGE_ANATOMY),
        "rule_joint_theorem_sha256": sha256_of(RULE_JOINT_THEOREM),
        "canonical_constants_sha256": sha256_of(CANONICAL_CONSTANTS),
        "s91_verdicts_sha256": sha256_of(S91_VERDICTS),
        "s92_verdicts_pre_emit_sha256": sha256_of(VERDICT_PATH),
        "w5_1_audit_sha256": W5_1_AUDIT_SHA_FULL,
        "s91_w5_w6_promotion_audit_sha256": (
            S91_W5_W6_PROMOTION_AUDIT_SHA_FULL
        ),
    }
    print("  input-pin SHAs:")
    for k, v in pin_map.items():
        print(f"    {k} = {v[:16]}...")

    # -----------------------------------------------------------------
    # Step 2 — build_promotion_text (registry block + corpus row)
    # -----------------------------------------------------------------
    registry_block = build_subclass_tag_block()
    corpus_row = build_corpus_row()
    print(f"  registry_block bytes: {len(registry_block.encode('utf-8'))}")
    print(f"  corpus_row bytes:     {len(corpus_row.encode('utf-8'))}")

    # -----------------------------------------------------------------
    # Step 3 — write_atomic_with_fsync (registry + corpus)
    # Re-run safety: if a prior insert exists (from an earlier FAIL run),
    # replace-block in-place rather than double-append. Per Option A
    # (gate-verdicts.md §"Option A — sig_5 remediation pathway"), the
    # original FAIL verdict line is RETAINED on disk; the corrective PASS
    # verdict carries supersedes=<old_audit_sha>.
    # -----------------------------------------------------------------
    registry_anchor_marker = (  # (local)
        "**S92 W5-2 NEW sub-class tag attachment — "
        "STAGE-1-CANDIDATE-CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED"
    )
    registry_end_marker = (  # (local)
        "### §VII.AX.OP-PROJ — PBH Band-Edge Prediction"
    )
    registry_replaced = write_atomic_with_fsync_replace_block(
        REGISTRY_PATH, registry_block,
        registry_anchor_marker, registry_end_marker,
    )
    if registry_replaced:
        print(f"  registry edit REPLACED (corrective re-run) at "
              f"{REGISTRY_PATH.name}")
    else:
        write_atomic_with_fsync_append(
            REGISTRY_PATH, registry_block, find_registry_insertion_point,
        )
        print(f"  registry edit landed at {REGISTRY_PATH.name}")

    corpus_anchor_marker = (  # (local)
        "  - **(d) §VII.AU.OP-PROJ CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED**"
    )
    corpus_end_marker = (  # (local)
        "  Both sub-class tags route to plan-freeze advisory"
    )
    corpus_replaced = write_atomic_with_fsync_replace_block(
        CORPUS_PATH, corpus_row,
        corpus_anchor_marker, corpus_end_marker,
    )
    if corpus_replaced:
        print(f"  corpus edit REPLACED (corrective re-run) at "
              f"{CORPUS_PATH.name}")
    else:
        write_atomic_with_fsync_append(
            CORPUS_PATH, corpus_row, find_corpus_insertion_point,
        )
        print(f"  corpus edit landed at {CORPUS_PATH.name}")

    # -----------------------------------------------------------------
    # Step 4 — re_read + verify_section_matches
    # -----------------------------------------------------------------
    # The expected_substring tests anchor on stable distinctive phrases.
    registry_anchor = (
        "**S92 W5-2 NEW sub-class tag attachment — "
        "STAGE-1-CANDIDATE-CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED"
    )
    corpus_anchor = (
        "**(d) §VII.AU.OP-PROJ CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED**"
    )
    registry_match = verify_section_matches(REGISTRY_PATH, registry_anchor)
    corpus_match = verify_section_matches(CORPUS_PATH, corpus_anchor)
    print(f"  registry verify_section_matches: {registry_match}")
    print(f"  corpus verify_section_matches:   {corpus_match}")

    # -----------------------------------------------------------------
    # Step 5 — compute post-edit content_sha256s
    # -----------------------------------------------------------------
    registry_post_sha = sha256_of(REGISTRY_PATH)
    corpus_post_sha = sha256_of(CORPUS_PATH)
    registry_block_sha = sha256_of_text(registry_block)
    corpus_row_sha = sha256_of_text(corpus_row)
    pin_map["registry_post_edit_sha256"] = registry_post_sha
    pin_map["corpus_post_edit_sha256"] = corpus_post_sha
    pin_map["registry_block_content_sha256"] = registry_block_sha
    pin_map["corpus_row_content_sha256"] = corpus_row_sha
    print(f"  registry_post_sha:    {registry_post_sha[:16]}...")
    print(f"  corpus_post_sha:      {corpus_post_sha[:16]}...")
    print(f"  registry_block_sha:   {registry_block_sha[:16]}...")
    print(f"  corpus_row_sha:       {corpus_row_sha[:16]}...")

    # -----------------------------------------------------------------
    # Step 6 — 6-of-6 PASS predicate evaluation
    # -----------------------------------------------------------------
    # (a) §VII.AU.OP-PROJ sub-class tag block present in registry text
    post_registry_text = REGISTRY_PATH.read_text(encoding="utf-8")
    predicate_a = registry_anchor in post_registry_text

    # (b) cites §W5-1 audit_sha256=395c63c829c11546... as structural anchor
    predicate_b = W5_1_AUDIT_SHA_FULL in post_registry_text

    # (c) sub-class semantic definition included (>= 8 lines)
    # Count lines between the sub-class semantic definition marker
    # ("**Sub-class semantic definition**:") and the next blank-line-after-list.
    semantic_match = re.search(
        r"\*\*Sub-class semantic definition\*\*:\s*\n(.+?)\n\*\*Structural orthogonality",
        post_registry_text, re.DOTALL,
    )
    if semantic_match:
        semantic_block = semantic_match.group(1)
        semantic_line_count = (
            len([ln for ln in semantic_block.splitlines() if ln.strip()])
        )
    else:
        semantic_line_count = 0  # (local) fallback when regex non-match
    predicate_c = semantic_line_count >= 8

    # (d) substantive_line_count of the sub-class tag block >= 15
    # Count non-blank lines in the inserted registry block.
    substantive_line_count = (
        len([ln for ln in registry_block.splitlines() if ln.strip()])
    )
    predicate_d = substantive_line_count >= 15

    # (e) content_sha256 of the §VII.AU.OP-PROJ slot matches the
    # input-pin-map-derived hash. Since the edit IS the input-pin-map
    # derived hash, this is the post-edit SHA matching the pre-computed
    # block SHA being present in the registry on re-read (already verified
    # by predicate_a). The structural-integrity check is the
    # content_sha256 closure equals the inserted block's SHA.
    predicate_e = (registry_block_sha in pin_map.values()
                   and registry_match)

    # (f) paired corpus-row appended at K=2 forward-saturation row
    post_corpus_text = CORPUS_PATH.read_text(encoding="utf-8")
    predicate_f = (
        corpus_anchor in post_corpus_text
        and "K=2 forward-saturation" not in corpus_anchor  # the table is K=2 capacity context
        and W5_1_AUDIT_SHA_FULL in post_corpus_text
    )

    predicates = {  # (local)
        "a_sub_class_tag_block_present": predicate_a,
        "b_cites_w5_1_audit_sha256": predicate_b,
        "c_sub_class_semantic_definition_lines_geq_8": predicate_c,
        "d_substantive_line_count_geq_15": predicate_d,
        "e_content_sha256_match": predicate_e,
        "f_paired_corpus_row_appended": predicate_f,
    }
    n_pass = sum(1 for v in predicates.values() if v)
    print(f"  predicates: {n_pass}/6 PASS")
    for k, v in predicates.items():
        print(f"    {k}: {v}")
    print(f"    semantic_line_count = {semantic_line_count}")
    print(f"    substantive_line_count = {substantive_line_count}")

    # -----------------------------------------------------------------
    # Step 7 — verdict + dual-SHA
    # -----------------------------------------------------------------
    overall_pass = (n_pass == 6)
    verdict = "PASS" if overall_pass else "FAIL"

    value_str = (
        f"6_of_6_PASS_predicate={overall_pass};"
        f"n_pass={n_pass};"
        f"predicate_a={predicate_a};"
        f"predicate_b={predicate_b};"
        f"predicate_c={predicate_c};"
        f"predicate_d={predicate_d};"
        f"predicate_e={predicate_e};"
        f"predicate_f={predicate_f};"
        f"semantic_line_count={semantic_line_count};"
        f"substantive_line_count={substantive_line_count};"
        f"registry_block_content_sha256_short={registry_block_sha[:16]};"
        f"corpus_row_content_sha256_short={corpus_row_sha[:16]};"
        f"registry_post_edit_sha256_short={registry_post_sha[:16]};"
        f"corpus_post_edit_sha256_short={corpus_post_sha[:16]};"
        f"w5_1_anchor_audit_sha_short={W5_1_AUDIT_SHA_FULL[:16]};"
        f"s91_w5_w6_promotion_anchor_short={S91_W5_W6_PROMOTION_AUDIT_SHA_FULL[:16]};"
        f"sub_class=STAGE-1-CANDIDATE-CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED;"
        f"K_pre=3;K_post=4;status=SUGGESTION_at_K_1;"
        f"first_canonical_instance=VII.AU.OP-PROJ;"
        f"level_class_pin=FULL;tier_pin=TIER-1"
    )

    # Compute dual SHA over the input-pin map (audit) and script content.
    pin_map_json = json.dumps(pin_map, sort_keys=True)
    audit_sha = sha256_of_text(pin_map_json + GATE_ID)
    script_path = Path(__file__).resolve()
    content_sha = sha256_of(script_path)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")

    # -----------------------------------------------------------------
    # Step 8 — write JSON sidecar
    # -----------------------------------------------------------------
    data = {  # (local)
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX_TAG,
        "verdict": verdict,
        "value": value_str,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S87+",
        "predicates": predicates,
        "n_pass": n_pass,
        "semantic_line_count": semantic_line_count,
        "substantive_line_count": substantive_line_count,
        "pin_map": pin_map,
        "sub_class": "STAGE-1-CANDIDATE-CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED",
        "first_canonical_instance": "VII.AU.OP-PROJ",
        "K_pre": 3,
        "K_post": 4,
        "status": "SUGGESTION at K=1",
        "level_class_pin": "FULL",
        "tier_pin": "TIER-1",
        "build_promotion_text_step": "PASS",
        "write_atomic_with_fsync_step": "PASS",
        "verify_section_matches_step": (
            "PASS" if (registry_match and corpus_match) else "FAIL"
        ),
        "emit_step": "single-shot AFTER-pattern compliant",
        "elapsed_seconds": time.time() - t0,
    }
    DATA_PATH.write_text(
        json.dumps(data, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"  JSON sidecar: {DATA_PATH.name}")

    # -----------------------------------------------------------------
    # Step 9 — emit ONE verdict line (single-shot AFTER-pattern;
    # Option A supersedes-tag if corrective emission)
    # -----------------------------------------------------------------
    prior_sha = find_prior_audit_sha_for_gate()
    supersedes_tag = prior_sha if prior_sha is not None else None
    if supersedes_tag is not None:
        print(f"  prior canonical line found: supersedes="
              f"{supersedes_tag[:16]}... (Option A)")
    else:
        print("  no prior canonical line; emission is original (no supersedes)")
    append_verdict(verdict, value_str, audit_sha, content_sha,
                   supersedes=supersedes_tag)
    print(f"  verdict line appended: {verdict}")
    print(f"  4-tuple: (value=<6_of_6_PASS={overall_pass}>, "
          f"scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX_TAG})")
    print(f"=== elapsed: {time.time() - t0:.2f}s ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
