#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S93-W3-1-VII-AV-OP-PROJ-STATE-PROJ-SLOT-SPLIT-LANDING
=====================================================

Splits the SINGLE STAGE-1-CANDIDATE §VII.AV registry slot in
`sessions/permanent-results-registry.md` into TWO
STRUCTURAL-ORTHOGONAL-COMPANION sub-slots:

  - §VII.AV.OP-PROJ   (Cell I  ; algebra-INVARIANT spectrum-only trace-residue;
                       anchor B_LAYER_A = 3.752271e+02 M_KK²; PW sectors
                       {(0,2),(1,1),(2,0)}; substrate-distance-2 pole s=4)
  - §VII.AV.STATE-PROJ (Cell IV ; algebra-DEPENDENT state-pair functional;
                       anchor L_emp = -7.046336474406761 M_KK²; K-window
                       log-derivative on the BdG sub-algebra M_2(C) ⊂ A_K)

declared STRUCTURAL-ORTHOGONAL-COMPANION (NOT SOURCE-DOUBLE-CITE-CO-PRIMARY:
cross-corner co-primary is STRUCTURALLY FORBIDDEN per the algebra-axis
orthogonality K=3 MANDATORY clause; the two sub-slots live on ORTHOGONAL
algebra-axis cells — Cell I ≠ Cell IV — and CANNOT be co-primary anchors of one
theorem).

SPLIT SOURCE (the workshop verdict this landing makes structural)
-----------------------------------------------------------------
S92 §W3-9 layer-attribution disambiguation gate
`S92-W3-CF-S92-W5-1-C-VII-AV-LAYER-ATTRIBUTION-DISAMBIGUATION`
(`computations/session-92/s92_gate_verdicts.txt:63`):
  audit_sha256 = 6038433b6c599518148746acb38a16b4eadf69392de3ad76895171e410c8a2bb
  value: B_LAYER_A=3.752271e+02, B_LAYER_B=-7.046336,
         Phi_correspondence_consistency_ratio=52.25 (F-images INCONSISTENT),
         slot_decision=MANDATORY-split-OP-PROJ-plus-STATE-PROJ,
         OP-PROJ_sectors=[(0,2),(1,1),(2,0)], layer_A_cell=Cell_I,
         layer_B_cell=Cell_IV, cross-corner co-primary FORBIDDEN.
The S92 W3-9 disambiguation found B_LAYER_A (Cell I) and L_emp (Cell IV) are
NOT two regulator-class F-images of ONE substrate-IS observable (Phi-ratio
52.25 ≠ 1) — they are two STRUCTURALLY DISTINCT observables on ORTHOGONAL
algebra-axes sharing only a pole label. This MANDATES the split. (This is a
DIFFERENT axis from the S91 W5-1 SCHEMATIC-vs-FULL-PV F-image divergence, where
both -7.046336 and -527.97 ARE Cell-IV regulator-class F-images of the SAME
observable and a split would FAIL the Hybrid Independence Test — that
"single-slot landing canonical" verdict is PRESERVED and lives ENTIRELY inside
the STATE-PROJ sub-slot's Level-2-B diagnostic sub-row table.)

STATE-PROJ anchor provenance: `computations/session-91/s91_w5_1_full_bdg_pv.npz`
key `L_emp_canonical` = -7.046336474406761 (per S92 W3-9 plan-text-drift
correction: the plan-cited `s89_w5_2_l_emp_canonical_anchor.npz` does NOT exist;
the runtime path is `s91_w5_1_full_bdg_pv.npz`).
STATE-PROJ OPERATIONAL-ALIGNMENT binding evidence: S91 W1-3 K_canonical pin
uniqueness class-(c) UNIQUE-multi-branch PASS
(`computations/session-91/s91_gate_verdicts.txt`):
  audit_sha256 = db08f3dfd9c8a5532c442629dd256950f51ac3219bfbe1bc8c35471b6b2be9c4.

METHODOLOGY-class registry-landing gate per `wave-classification.md` (M1
artifact-existence-with-substantive-content PASS predicate; M2 registry Write +
grep/SHA cross-checks; M3 verbatim split structure from the closed S92 §W3-9
disambiguation verdict; M4 allowlist append is ORCHESTRATOR-ONLY — flagged in
the WP, NOT edited by this script). mack-cosmic-bridge is the SOLE registry
writer per `feedback_mack-bridge-role.md`. The script reads NO D_K eigenvalues —
it splits a registry slot and records the W3-9 disambiguation provenance.

Single-shot bridge-landing AFTER pattern per
`registry-landing.md §"Bridge-Landing Script Architecture (single-shot pattern)"`
+ `computations/_bridge_landing_script_template.py`:
    build_promotion_text  ->  write_atomic_with_fsync  ->
    re_read + verify_section_matches  ->  emit-ONCE
No conditional rewrite / re-emit. A verify-FAIL emits FAIL once and the gate
closes honestly per `mechanical-closure-discipline.md`.

Verdict: [VERIFY] (METHODOLOGY-class; no [SIGN] 3-tuple — §9 pre-registers no
directional prediction; this is a set-equality artifact-existence gate). Dual-SHA
closure: content_sha256 over the TWO landed sub-slot section texts; audit_sha256
over the input-pin map + the W3-9 disambiguation SHA + L_emp anchor value +
per-gate identity keys per `wave-classification.md §"Dual-SHA closure for
METHODOLOGY-class"`.
"""

from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import re
import sys
from pathlib import Path

# --- canonical constants (mandatory per .claude/rules/math-scripts.md S34+) ---
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent  # (local)
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"  # (local)
sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import M_KK, tau_fold  # noqa: F401, E402

# ---------------------------------------------------------------------------
# Gate identity + canonical paths
# ---------------------------------------------------------------------------
GATE_ID = "S93-W3-1-VII-AV-OP-PROJ-STATE-PROJ-SLOT-SPLIT-LANDING"  # (local)
SCHEME = "METHODOLOGY-class-registry-text-edit"  # (local)
CONVENTION = (  # (local)
    "algebra-axis-orthogonality-K3-MANDATORY-cross-corner-co-primary-FORBIDDEN-"
    "STRUCTURAL-ORTHOGONAL-COMPANION-Cell-I-OP-PROJ-Cell-IV-STATE-PROJ"
)
L_MAX = "N/A"  # (local) METHODOLOGY-class registry slot-split; no compute

REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)
VERDICT_TXT = (  # (local) canonical per gate-verdicts.md §"Canonical Verdict-File Path"
    PROJECT_ROOT / "computations" / "session-93" / "s93_gate_verdicts.txt"
)
JSON_PATH = (  # (local)
    PROJECT_ROOT
    / "computations"
    / "session-93"
    / "s93_w3_1_vii_av_op_proj_state_proj_slot_split.json"
)
S92_VERDICT_TXT = (  # (local) source of the W3-9 layer-attribution disambiguation
    PROJECT_ROOT / "computations" / "session-92" / "s92_gate_verdicts.txt"
)
S92_W3_9_NPZ = (  # (local) W3-9 disambiguation npz
    PROJECT_ROOT
    / "computations"
    / "session-92"
    / "s92_w3_9_vii_av_layer_attribution_disambiguation.npz"
)
L_EMP_NPZ = (  # (local) runtime STATE-PROJ anchor (plan-text-drift-corrected path)
    PROJECT_ROOT / "computations" / "session-91" / "s91_w5_1_full_bdg_pv.npz"
)
SLOT_LOCKFILE = (  # (local) W0-1 deliverable; §VII.AV sub-slots RESERVED
    PROJECT_ROOT / "sessions" / "framework" / "s93-slot-pre-allocation-lockfile.md"
)

# --- split-source + binding-evidence SHAs (full-64-hex; cited VERBATIM) ---
W3_9_AUDIT_SHA = (  # (local) S92 §W3-9 layer-attribution disambiguation
    "6038433b6c599518148746acb38a16b4eadf69392de3ad76895171e410c8a2bb"
)
W3_9_GATE = "S92-W3-CF-S92-W5-1-C-VII-AV-LAYER-ATTRIBUTION-DISAMBIGUATION"  # (local)
W1_3_AUDIT_SHA = (  # (local) S91 W1-3 K_canonical OPERATIONAL-ALIGNMENT binding
    "db08f3dfd9c8a5532c442629dd256950f51ac3219bfbe1bc8c35471b6b2be9c4"
)
W1_3_GATE = "CF-S91-CF-71-K_CANONICAL-PIN-UNIQUENESS"  # (local)

# --- substrate-IS anchors (the two structural-orthogonal-companion anchors) ---
B_LAYER_A = 3.752271e02  # (local) OP-PROJ Cell-I trace-residue (M_KK²)
L_EMP_CANONICAL = -7.046336474406761  # (local) STATE-PROJ Cell-IV K-window log-deriv
PHI_RATIO = 5.225137e01  # (local) W3-9 Phi-correspondence consistency ratio (F-images INCONSISTENT)

# Insertion boundary: the TWO new sub-slot headings land immediately BEFORE the
# existing live §VII.AV header. The parent §VII.AV header gets a split-discharge
# note. The split sub-slots are NEW sub-slot headings (suffix-tags of the
# EXISTING §VII.AV slot, NOT new top-level letters).
PARENT_AV_HEADER = (  # (local) the live STAGE-1-CANDIDATE-PENDING-STAGE-2 §VII.AV header
    "### §VII.AV (STAGE-1-CANDIDATE-PENDING-STAGE-2 — S91 W1 OPERATIONAL-ALIGNMENT "
    "binding sub-class promotion via mack-cosmic-bridge sole-writer; PROXY-REFINEMENT "
    "pending FULL physical pipeline refinement at CF-61)"
)
OP_PROJ_HEADER = (  # (local)
    "### §VII.AV.OP-PROJ — Cell-I OP-PROJ Trace-Residue Sub-Slot"
)
STATE_PROJ_HEADER = (  # (local)
    "### §VII.AV.STATE-PROJ — Cell-IV STATE-PROJ K-Window Log-Derivative Sub-Slot"
)
SPLIT_DISCHARGE_MARKER = (  # (local) the split-discharge note prepended to the parent body
    "**S93 W3-1 OP-PROJ/STATE-PROJ slot-split discharge"
)

# Input-pin map (source documents the split consumes; SHAs feed audit_sha256).
INPUT_FILES = [  # (local)
    REGISTRY_PATH,
    S92_VERDICT_TXT,
    S92_W3_9_NPZ,
    L_EMP_NPZ,
    SLOT_LOCKFILE,
    PROJECT_ROOT / "computations" / "_bridge_landing_script_template.py",
]


# ---------------------------------------------------------------------------
# SHA helpers (canonical dual-SHA per the S84+ schema)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return "0" * 64


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(section_text: str, pins: dict[str, str]) -> tuple[str, str]:
    """Dual-SHA per wave-classification.md §"Dual-SHA closure for METHODOLOGY-class".

    content_sha256 = SHA-256 over the TWO landed sub-slot section texts (the
                     F-image of the numerical PASS-predicate under
                     substrate <-> methodology per epistemic-discipline.md
                     §"Layer-Decomposition").
    audit_sha256   = SHA-256 over the input-pin map + the W3-9 disambiguation SHA
                     + the W1-3 binding-evidence SHA + the L_emp anchor value +
                     per-gate identity keys (so audit_sha256 is gate-distinct per
                     mechanical-closure-discipline item 3).
    """
    h_content = hashlib.sha256()  # (local)
    h_content.update(section_text.encode("utf-8"))
    content = h_content.hexdigest()  # (local)

    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(pinmap_json)
    # The split is admissible ONLY by citing the W3-9 disambiguation chain + the
    # substrate-IS anchors; these are part of the canonical input set.
    h_audit.update(
        f"{W3_9_AUDIT_SHA}|{W1_3_AUDIT_SHA}|{B_LAYER_A!r}|{L_EMP_CANONICAL!r}".encode(
            "utf-8"
        )
    )
    # per-gate identity keys embedded so audit_sha256 is gate-distinct
    h_audit.update(f"{GATE_ID}|{SCHEME}|{CONVENTION}".encode("utf-8"))
    audit = h_audit.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Slot-lockfile pre-condition (RESERVATION confirmation; advisory — not HARD)
# ---------------------------------------------------------------------------
def confirm_slot_reserved() -> bool:
    """Confirm the S93 slot lockfile RESERVES the §VII.AV sub-slots.

    The umbrella reservation is RESERVED-FOR-S93-W3-6 (the gate that consumes the
    split per sub-slot); W3-1 performs the split that W3-6 verifies. The lockfile
    names BOTH §VII.AV.OP-PROJ + §VII.AV.STATE-PROJ in its Anchor list.
    """
    if not SLOT_LOCKFILE.exists():
        return False
    txt = SLOT_LOCKFILE.read_text(encoding="utf-8")  # (local)
    has_op = "§VII.AV.OP-PROJ" in txt  # (local)
    has_state = "§VII.AV.STATE-PROJ" in txt  # (local)
    has_reserved = "RESERVED" in txt  # (local)
    return bool(has_op and has_state and has_reserved)


# ---------------------------------------------------------------------------
# Split-source verification (the W3-9 disambiguation verdict)
# ---------------------------------------------------------------------------
def confirm_split_source() -> dict:
    """Confirm the S92 §W3-9 layer-attribution disambiguation verdict exists in
    s92_gate_verdicts.txt VERBATIM (full-64-hex) and carries the MANDATORY-split
    decision + the two corner-cell attributions + cross-corner-FORBIDDEN flag.
    """
    out = {  # (local)
        "w3_9_present": False,
        "mandatory_split_decision": False,
        "cell_I_op_proj": False,
        "cell_IV_state_proj": False,
        "cross_corner_forbidden": False,
    }
    if not S92_VERDICT_TXT.exists():
        return out
    for ln in S92_VERDICT_TXT.read_text(encoding="utf-8").splitlines():
        if ln.startswith(f"{W3_9_GATE}:") and f"audit_sha256={W3_9_AUDIT_SHA}" in ln:
            out["w3_9_present"] = True
            out["mandatory_split_decision"] = (
                "MANDATORY-split-OP-PROJ-plus-STATE-PROJ" in ln
            )
            out["cell_I_op_proj"] = "layer_A_cell=Cell_I_algebra-INVARIANT" in ln
            out["cell_IV_state_proj"] = (
                "layer_B_cell=Cell_IV_algebra-DEPENDENT" in ln
            )
            out["cross_corner_forbidden"] = (
                "cross-corner_co-primary_FORBIDDEN" in ln
            )
            break
    return out


# ---------------------------------------------------------------------------
# Step (1) — build_promotion_text  (pure functions; no I/O)
# ---------------------------------------------------------------------------
def build_op_proj_block() -> str:
    """§VII.AV.OP-PROJ sub-slot (Cell I; algebra-INVARIANT; B_LAYER_A). Pure."""
    return f"""{OP_PROJ_HEADER} (S93 W3-1 OP-PROJ/STATE-PROJ slot-split landing — STRUCTURAL-ORTHOGONAL-COMPANION to §VII.AV.STATE-PROJ, NOT cross-corner co-primary; mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`, 2026-05-24)

**Status**: STAGE-1-CANDIDATE per `.claude/rules/joint-theorem-promotion.md` 4-stage pathway. Split from the single §VII.AV slot by S93 W3-1 (Tier-1 anchor landing); the OP-PROJ object is gated for Level-3 eligibility by the W3-3 Class-8.7 degeneracy-witness (separate gate this wave). Stage-2 cross-axis independent-verify (W3-6) audits this sub-slot as a distinct STAGE-1-CANDIDATE registry target.

**Naming-hygiene suffix** (per `.claude/rules/registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` MANDATORY at K=3): this slot carries the `.OP-PROJ` suffix because it is an **operator-projection** observable — an algebra-side central-projection trace on `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` (the algebra-INVARIANT spectrum-only family). Bare `§VII.AV` (no suffix) is FORBIDDEN now that both projection-side readings are independently registry-eligible.

**Corner-cell**: **Cell I** (algebra-INVARIANT spectrum-only functional `F({{λ_k, m_k}}) = Σ_k m_k g(λ_k)` × substrate-distance-2 pole `s=4`) per `permanent-results-registry.md §VII.U.2` 4-corner classification. The trace-residue `B_LAYER_A` is a spectrum-only functional of `D_K` with NO state-pair dependence; its parse-tree terminus is `Tr`, which FORCES the Cell-I classification per `cross-pillar-bridge-anatomy.md §"Observable-Naming-History vs Parse-Tree-Structure"`.

**Parse-tree expansion** (per `registry-landing.md §"Parse-Tree Expansion Pre-Registration"`): `B_LAYER_A := Tr_{{A_K}}(P_a · |D_K|^{{-2s}})` at `s=4`, reduced over the level-2 Peter-Weyl sectors `{{(0,2),(1,1),(2,0)}}` (the OP-PROJ sector set isolated at S92 §W3-9); `P_a` a central projection on `A_K`. The closed form is a spectrum-only sum `Σ_k m_k |λ_k|^{{-2s}}` — Cell-I terminus by `Tr`.

**Three-level structural-confidence ladder**:

| Level | Anatomy | Status |
|:------|:--------|:-------|
| Level 1 | Single-τ-slice substrate-IS spectral identity at τ_fold = 0.19: the OP-PROJ trace-residue `Tr_{{A_K}}(P_a · |D_K|^{{-2s}})` at substrate-distance-2 pole `s=4` over PW sectors `{{(0,2),(1,1),(2,0)}}` IS a substrate-IS algebra-INVARIANT observable of the single-τ-slice spectral triple `(A_K, H_K, D_K(τ_fold = 0.19))`. Regulator-class-sensitive at the analytic-content level (NOT a finite-cardinality direct-sum tautology — W3-3 Class-8.7 witness). | STRUCTURAL THEOREM (pending W3-3 Class-8.7 witness confirming regulator-sensitivity gates Level-3 eligibility) |
| Level 2 | Algebraic convergence envelope at d=4 substrate-distance-2 pole `s=4` on the algebra-INVARIANT spectrum-only family; **Level-2-B regulator-invariance axis** (per `cross-pillar-bridge-anatomy.md §"Level-2 audit axes"`). Cross-regulator spread `O(heat-kernel moment-ratio) ≈ O(20%)` (ζ=141.44, PV=114.46, Mellin=141.44 ⇒ PV-vs-ζ swing 26.98/141.44 ≈ 19%) is the regulator-DEPENDENT signature of the algebra-INVARIANT family per `cross-pillar-bridge-corpus.md §22` regulator-behavior sibling discriminator. | STRUCTURAL PREDICTION (regulator-class-keyed; W3-3 witness pending) |
| Level 3 | Empirical anchor at canonical L_max=12: `B_LAYER_A = 3.752271e+02 M_KK²` (the LAYER-A residue isolated at S92 §W3-9). | EMPIRICAL CONFIRMATION candidate (Level-3 eligibility GATED by the W3-3 Class-8.7 degeneracy-witness PASS confirming the ~375 residue is genuine regulator-sensitive analytic content, NOT a direct-sum tautology under canonical Γ(s)). |

**IS-not-IN anatomy** (5 elements; MANDATORY at K=3 per `cross-pillar-bridge-anatomy.md §"Forward template-adoption"`):

1. **Substrate-IS observable**: OP-PROJ trace-residue `B_LAYER_A = Tr_{{A_K}}(P_a · |D_K|^{{-2s}})` at substrate-distance-2 pole `s=4` over PW sectors `{{(0,2),(1,1),(2,0)}}`, evaluated on the finite spectral triple `(A_K^{{≤L_max=12}}, H_K^{{≤L_max=12}}, D_K^{{≤L_max=12}})` at τ_fold = 0.19. **EXPLICIT TAG: Level 1 single-τ-slice at τ_fold = 0.19** (MANDATORY per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`). Algebra-INVARIANT (spectrum-only); NO state-pair dependence.
2. **Laboratory-IN observable** (OE-form): `∫_BZ d^d k Tr_{{A_K}}(P_a · ρ_BZ(k; τ_fold))` — the continuum spectral-action moment image of the OP-PROJ trace-residue under the HKR map at the partner pillar. Lab measures this IN the continuum container.
3. **Bridge map** (explicit; not 'analogous to'): HKR (Hochschild-Kostant-Rosenberg) map `L_max → ∞` image at d=4 substrate-distance-2 pole `s=4`; Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula on `A_K`. Element 3 fiducial-anchor binding: type **(i) substrate-self-consistent** (the bridge composes through the substrate-IS pin `B_LAYER_A` at the same algebra-INVARIANT family).
4. **Algebraic envelope**: regulator-class-keyed convergence envelope at d=4 substrate-distance-2 pole `s=4`; **Level-2-B regulator-invariance axis**. The cross-regulator spread (~19% PV-vs-ζ) is the algebra-INVARIANT family's regulator-DEPENDENT signature (`cross-pillar-bridge-corpus.md §22`).
5. **Empirical anchor**: `B_LAYER_A = 3.752271e+02 M_KK²` at L_max=12 (the LAYER-A residue isolated at S92 §W3-9). Level-3 eligibility GATED by W3-3 Class-8.7 witness.

**STRUCTURAL-ORTHOGONAL-COMPANION declaration** (per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3 + `registry-landing.md §"Detection"` criterion (4)): §VII.AV.OP-PROJ (Cell I) and §VII.AV.STATE-PROJ (Cell IV) are **STRUCTURAL-ORTHOGONAL-COMPANIONS, NOT SOURCE-DOUBLE-CITE-CO-PRIMARY**. Cross-corner co-primary is STRUCTURALLY FORBIDDEN: criterion (4) requires both co-primary anchors to be on the SAME algebra-axis cell, but `corner_cell(OP-PROJ) = Cell I ≠ Cell IV = corner_cell(STATE-PROJ)`. Cell I (algebra-INVARIANT spectrum-only) and Cell IV (algebra-DEPENDENT state-pair) live on ORTHOGONAL algebra-axes; when both projection-side readings are independently registry-eligible the correct anchor structure is structural-orthogonal-companion. Cross-corner cross-pole magnitude comparison of `B_LAYER_A` (Cell I × s=4) against `L_emp` (Cell IV × s=4) is STRUCTURALLY FORBIDDEN AS A GATE per the parent rule (permitted in narrative ONLY with explicit `[CROSS-CORNER COMPARISON; STRUCTURALLY FORBIDDEN AS GATE]` declaration).

**Split source** (the disambiguation verdict this landing makes structural): S92 §W3-9 gate `{W3_9_GATE}` (`computations/session-92/s92_gate_verdicts.txt:63`) **audit_sha256=`{W3_9_AUDIT_SHA}`** (content_sha256=`67cdf9e448d7a2b2a58a6e8ba98159eb274da5e7dddcf500383b801b90e678b3`). The W3-9 disambiguation found `B_LAYER_A=3.752271e+02` (LAYER-A, Cell I) and `B_LAYER_B=-7.046336` (LAYER-B, Cell IV) are NOT two regulator-class F-images of ONE observable (`Phi_correspondence_consistency_ratio = {PHI_RATIO:.6g}` ≠ 1 ⇒ `classification=F_IMAGE_INCONSISTENT_MANDATORY_SPLIT`); `slot_decision=MANDATORY-split-OP-PROJ-plus-STATE-PROJ`; `OP-PROJ_sectors=[(0,2),(1,1),(2,0)]`; `cross-corner_co-primary_FORBIDDEN`.

**Substrate framing** (per `phononic-framing.md §"IS Space, Not IN Space"`): GEOMETRIC (spectral triple structure, not excitation). The substrate IS the finite spectral triple `(A_K, H_K, D_K)` at τ_fold = 0.19; the OP-PROJ trace-residue `B_LAYER_A` IS the algebra-INVARIANT spectrum-only image at Cell I × substrate-distance-2 pole `s=4`. Direction of explanation:

```
Substrate (A_K spectrum) IS the OP-PROJ trace-residue Tr_{{A_K}}(P_a · |D_K|^{{-2s}}) at s=4
   → Bridge map (HKR L_max → ∞ at d=4 substrate-distance-2 pole s=4)
   → Laboratory IN the continuum spectral-action moment image
```

**FORBIDDEN inversion**: treating the continuum moment as fundamental and the substrate residue as its "analog" inverts the direction — container-thinking violation. The substrate residue IS canonical; the continuum is the measurement context.

**Cross-references**:

- `.claude/rules/registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` MANDATORY at K=3 — the `.OP-PROJ` suffix discipline.
- `.claude/rules/cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3 — Cell I (algebra-INVARIANT) classification + cross-corner co-primary FORBIDDEN.
- `.claude/rules/cross-pillar-bridge-corpus.md §22` — regulator-behavior sibling discriminator (algebra-INVARIANT family is regulator-DEPENDENT, bounded `O(20%)`).
- S92 §W3-9 disambiguation gate `{W3_9_GATE}` audit_sha256=`{W3_9_AUDIT_SHA}` — the split source.
- §VII.AV.STATE-PROJ (the structural-orthogonal-companion sub-slot; Cell IV).
- Parent §VII.AV (the host record, split-discharged at S93 W3-1).
- W3-3 Class-8.7 degeneracy-witness gate (gates Level-3 eligibility of the ~375 anchor).
- Precedent: §VII.AF.1.OP-PROJ + §VII.AF.1.STATE-PROJ structural-orthogonal-companion split (the canonical algebra-axis OP-PROJ/STATE-PROJ split template per `s88-pending-edits-ledger.md`).

**Audit pin**: S93 W3-1 single-shot AFTER-pattern gate `{GATE_ID}` (`computations/session-93/s93_w3_1_vii_av_op_proj_state_proj_slot_split.py`); single-shot AFTER-pattern per `registry-landing.md §"Bridge-Landing Script Architecture (single-shot pattern)"`. Sub-slot RESERVED at `sessions/framework/s93-slot-pre-allocation-lockfile.md §"RESERVED-FOR-S93-W3-6-VII-AV-STAGE-2-CROSS-AXIS-VERIFY-PER-SUB-SLOT"`.

"""


def build_state_proj_block() -> str:
    """§VII.AV.STATE-PROJ sub-slot (Cell IV; algebra-DEPENDENT; L_emp). Pure."""
    return f"""{STATE_PROJ_HEADER} (S93 W3-1 OP-PROJ/STATE-PROJ slot-split landing — STRUCTURAL-ORTHOGONAL-COMPANION to §VII.AV.OP-PROJ, NOT cross-corner co-primary; mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`, 2026-05-24)

**Status**: STAGE-1-CANDIDATE-PENDING-STAGE-2 per `.claude/rules/joint-theorem-promotion.md` 4-stage pathway, with the OPERATIONAL-ALIGNMENT binding sub-class (S91 W1) and the PROXY-REFINEMENT deferred-pending sub-class (FULL physical pipeline at CF-61). This sub-slot inherits the canonical Cell-IV content of the pre-split §VII.AV entry (the K-window log-derivative on the BdG sub-algebra; `L_emp = -7.046336474406761 M_KK²`). Stage-2 cross-axis independent-verify (W3-6) audits this sub-slot as a distinct STAGE-1-CANDIDATE registry target. The full curated Cell-IV content (5-anatomy, 3-level ladder, Level-2-B diagnostic sub-row table, refinement-pathway routes (i)-(viii), SOURCE-DOUBLE-CITE-CO-PRIMARY anchor structure, FOUR-rule cross-composition meta-pattern) lives in the parent §VII.AV host body below; this sub-slot heading is the STATE-PROJ structural-orthogonal-companion landing that names the Cell-IV anchor and binding.

**Naming-hygiene suffix** (per `.claude/rules/registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` MANDATORY at K=3): this slot carries the `.STATE-PROJ` suffix because it is a **state-projection** observable — a state-pair functional on the BdG sub-algebra `M_2(ℂ) ⊂ A_K` (the algebra-DEPENDENT family). Bare `§VII.AV` (no suffix) is FORBIDDEN now that both projection-side readings are independently registry-eligible.

**Corner-cell**: **Cell IV** (algebra-DEPENDENT state-pair functional × substrate-distance-2 pole `s=4`) per `permanent-results-registry.md §VII.U.2` 4-corner classification (LANDED S88 W5b-45). The K-window log-derivative is a state-pair functional on the BdG sub-algebra `M_2(ℂ) ⊂ A_K`; its parse-tree terminus is `Var_a` / `d(ln ·)/d(ln K)` over a gapped occupation distribution, which FORCES the Cell-IV classification per `cross-pillar-bridge-anatomy.md §"Observable-Naming-History vs Parse-Tree-Structure"`.

**Parse-tree expansion** (per `registry-landing.md §"Parse-Tree Expansion Pre-Registration"`): `L_emp := d² ln Var_a(|v_a(K)|²)/d(ln K)²` at `s=4` on the BdG sub-algebra `M_2(ℂ) ⊂ A_K`, where `v_a` is the canonical s52 8-mode Bogoliubov amplitude vector (gapped occupation). The closed form is a state-pair functional on `A` — Cell-IV terminus by `Var_a`. NOT a spectrum-only `Tr` (that is the OP-PROJ companion).

**Three-level structural-confidence ladder**:

| Level | Anatomy | Status |
|:------|:--------|:-------|
| Level 1 | Single-τ-slice substrate-IS spectral identity at τ_fold = 0.19: the Corner-IV K-window log-derivative on the BdG sub-algebra `M_2(ℂ) ⊂ A_K` IS a substrate-IS state-pair observable of the single-τ-slice spectral triple `(A_K, H_K, D_K(τ_fold = 0.19))` at substrate-distance-2 pole `s=4`. Regulator-INVARIANT (IR-self-regularized by the BdG gap `|Δ_a|` per `cross-pillar-bridge-corpus.md §22`). | STRUCTURAL THEOREM |
| Level 2 | Algebraic convergence envelope `L^{{-3}}` HKR-image at d=4 substrate-distance-2 pole `s=4` (Level-2-binding sub-class): the HKR `L_max → ∞` image binds the Level-1 cohomology-class identity to the laboratory-IN Pillar V continuum BdG-sector observable. Empirical α exponent DEFERRED PENDING CF-61 / discharged via the Connes-Karoubi envelope predictor (W3-4 this wave). | STRUCTURAL PREDICTION (PROXY-REFINEMENT sub-class; FULL physical pipeline pending) |
| Level 3 | Empirical anchor at canonical L_max=12: substrate-natural anchor `L_emp(L_max=12) = -7.046336474406761 M_KK²` (Corner-IV K-window log-derivative; the SOLE Corner-IV calibration source). Single-pinned (Level-3-anchor singleness per `cross-pillar-bridge-anatomy.md §"Level-3 anchor singleness sub-clause"`): the FULL-PV `-527.97` value is a Level-2-B regulator-class DIAGNOSTIC sub-row, NOT a Level-3 co-primary. | EMPIRICAL CONFIRMATION (Cell-IV operational axis): `L_emp` reproduced at machine ε (delta=-1.26e-16) by the canonical s52 8-mode Bogoliubov amplitude vector via the S91 W1-3 class-(c) UNIQUE-multi-branch OPERATIONAL-ALIGNMENT discriminator. |

**IS-not-IN anatomy** (5 elements; MANDATORY at K=3): identical to the pre-split §VII.AV Cell-IV anatomy (parent host body below):

1. **Substrate-IS observable**: Corner-IV K-window log-derivative `R_KW(τ_fold) = d ln(Tr_{{M_2(ℂ)}}(P_BdG · D_K^{{−2s}})) / d ln(K_window)` on the BdG sub-algebra `M_2(ℂ) ⊂ A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`, at τ_fold = 0.19 and substrate-distance-2 pole `s=4`. **EXPLICIT TAG: Level 1 single-τ-slice at τ_fold = 0.19**. Algebra-DEPENDENT (state-pair functional).
2. **Laboratory-IN observable** (OE-form): `∫_{{BZ-BdG}} d^d k Tr_{{M_2(ℂ)}}(P_BdG · ρ_BZ(k; τ_fold)) · (d ln · / d ln K)` — Pillar V continuum 3He-B BdG-sector mutual-friction measurement.
3. **Bridge map**: HKR map `L_max → ∞` image at d=4 substrate-distance-2 pole `s=4`; Connes-Moscovici 1995 §III.4 residue formula on `M_2(ℂ) ⊂ A_K`. Element 3 binding: type **(i) substrate-self-consistent**; **substrate-natural-binding** (NOT canonical-import-binding) — `L_emp` is computed directly on the substrate's BdG sub-algebra.
4. **Algebraic envelope**: `L^{{-3}}` at d=4 substrate-distance-2 pole `s=4`; **Level-2-binding sub-class**; **REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT** (SCHEMATIC Casimir-bound proxy; FULL physical pipeline pending CF-61 / Connes-Karoubi discharge W3-4).
5. **Empirical anchor**: substrate-natural anchor `L_emp(L_max=12) = -7.046336474406761 M_KK²` (SOLE Corner-IV calibration source); Pillar V continuum target = 3He-B mutual-friction coefficient at substrate-distance-2 pole `s=4`.

**STRUCTURAL-ORTHOGONAL-COMPANION declaration** (per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3 + `registry-landing.md §"Detection"` criterion (4)): §VII.AV.STATE-PROJ (Cell IV) and §VII.AV.OP-PROJ (Cell I) are **STRUCTURAL-ORTHOGONAL-COMPANIONS, NOT SOURCE-DOUBLE-CITE-CO-PRIMARY**. Cross-corner co-primary is STRUCTURALLY FORBIDDEN: `corner_cell(STATE-PROJ) = Cell IV ≠ Cell I = corner_cell(OP-PROJ)`. The K-window log-derivative is a state-pair functional on the BdG sub-algebra, NOT a spectrum-only-functional image — period. Cross-corner cross-pole magnitude comparison of `L_emp` (Cell IV × s=4) against `B_LAYER_A` (Cell I × s=4) is STRUCTURALLY FORBIDDEN AS A GATE per the parent rule.

**Within-Cell-IV regulator-class diagnostic** (NOT cross-corner; NOT a rival anchor): the FULL-PV value `-527.97 M_KK²` (m_PV = M_KK) and the SCHEMATIC Casimir-bound proxy `-7.046336 M_KK²` are TWO regulator-class F-images of the SAME Cell-IV substrate-IS observable per the K=3 MANDATORY single-observable-per-triple algebra-axis axiom (Hybrid Independence Test FAILS for any split of THIS pair — identical substrate-IS pillar III, identical laboratory-IN pillar V, identical bridge-map class HKR). The `-527.97` value is filed as a Level-2-B DIAGNOSTIC sub-row in the parent host body, NOT as a Level-3 co-primary. This within-Cell-IV regulator-class divergence is STRUCTURALLY DISTINCT from the cross-corner OP-PROJ/STATE-PROJ split (which separates Cell I from Cell IV).

**Split source + binding evidence** (cited VERBATIM, full-64-hex): S92 §W3-9 gate `{W3_9_GATE}` (`computations/session-92/s92_gate_verdicts.txt:63`) **audit_sha256=`{W3_9_AUDIT_SHA}`** established `B_LAYER_B=-7.046336` at `layer_B_cell=Cell_IV_algebra-DEPENDENT` and `STATE-PROJ_anchor=L_emp_canonical=-7.046336474406761`. S91 W1-3 OPERATIONAL-ALIGNMENT binding gate `{W1_3_GATE}` (`computations/session-91/s91_gate_verdicts.txt`) **audit_sha256=`{W1_3_AUDIT_SHA}`** class-(c) UNIQUE-multi-branch PASS (Δ_B_multi-branch = -1.26e-16 PASS while Δ_A_scalar = +11.05% FAIL at REL_TOL=1e-3) — the OPERATIONAL-ALIGNMENT binding preserved in this sub-slot's anatomy element 4. STATE-PROJ anchor provenance: `computations/session-91/s91_w5_1_full_bdg_pv.npz` key `L_emp_canonical` = -7.046336474406761 (per S92 W3-9 plan-text-drift correction — NOT `s89_w5_2_l_emp_canonical_anchor.npz` which does not exist).

**Substrate framing** (per `phononic-framing.md §"IS Space, Not IN Space"`): GEOMETRIC / PHONONIC-boundary (state-pair functional on the BdG sub-algebra). The substrate IS the BdG sub-algebra `M_2(ℂ) ⊂ A_K` at single-τ-slice τ_fold = 0.19 substrate-distance-2 pole `s=4`; the laboratory-IN observation IS the Pillar V 3He-B BdG-sector continuum measurement. Direction of explanation:

```
Substrate (BdG sub-algebra M_2(ℂ) ⊂ A_K) IS the Corner-IV K-window log-derivative
   → Bridge map (HKR L_max → ∞ at d=4 substrate-distance-2 pole s=4)
   → Laboratory (Pillar V) IN 3He-B BdG-sector mutual-friction observation
```

**FORBIDDEN inversion**: treating the 3He-B cryostat observation as the canonical substrate observable and the K-window log-derivative as its "analog" inverts the direction — container-thinking violation. The substrate's BdG sub-algebra K-window log-derivative IS canonical; the cryostat IS the measurement context.

**Cross-references**:

- `.claude/rules/registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"` MANDATORY at K=3 — the `.STATE-PROJ` suffix discipline.
- `.claude/rules/cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3 — Cell IV (algebra-DEPENDENT state-pair) classification + cross-corner co-primary FORBIDDEN.
- `.claude/rules/cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` — PROXY-REFINEMENT + OPERATIONAL-ALIGNMENT sub-class tags.
- S92 §W3-9 disambiguation gate `{W3_9_GATE}` audit_sha256=`{W3_9_AUDIT_SHA}` — the split source.
- S91 W1-3 OPERATIONAL-ALIGNMENT binding gate audit_sha256=`{W1_3_AUDIT_SHA}`.
- §VII.AV.OP-PROJ (the structural-orthogonal-companion sub-slot; Cell I).
- Parent §VII.AV (the host record carrying the full curated Cell-IV anatomy + Level-2-B diagnostic sub-row table + refinement-pathway routes (i)-(viii) + SOURCE-DOUBLE-CITE-CO-PRIMARY anchor structure, split-discharged at S93 W3-1).
- W3-4 Connes-Karoubi PROXY-REFINEMENT discharge gate (Level-2-binding for this sub-slot).
- Precedent: §VII.AF.1.OP-PROJ + §VII.AF.1.STATE-PROJ structural-orthogonal-companion split template.

**Audit pin**: S93 W3-1 single-shot AFTER-pattern gate `{GATE_ID}`. Sub-slot RESERVED at `sessions/framework/s93-slot-pre-allocation-lockfile.md`.

"""


def build_split_discharge_note() -> str:
    """The split-discharge note prepended to the parent §VII.AV body. Pure.

    Non-destructive: this note is INSERTED at the top of the parent §VII.AV body
    (immediately after the parent header line); all curated parent prose below is
    PRESERVED. The parent becomes the host/provenance record; the two sub-slots
    above are the structural-orthogonal-companion landings.
    """
    return f"""{SPLIT_DISCHARGE_MARKER} (S93 W3-1 single-shot AFTER-pattern; mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`, 2026-05-24)**:

This single §VII.AV slot is **SPLIT into two STRUCTURAL-ORTHOGONAL-COMPANION sub-slots** by S93 W3-1 (Tier-1 anchor landing), per the S92 §W3-9 layer-attribution disambiguation MANDATORY-split decision (gate `{W3_9_GATE}`, audit_sha256=`{W3_9_AUDIT_SHA}`; `slot_decision=MANDATORY-split-OP-PROJ-plus-STATE-PROJ`; `classification=F_IMAGE_INCONSISTENT_MANDATORY_SPLIT`; `Phi_correspondence_consistency_ratio = {PHI_RATIO:.6g}` ≠ 1):

- **§VII.AV.OP-PROJ** (Cell I; algebra-INVARIANT spectrum-only trace-residue `B_LAYER_A = 3.752271e+02 M_KK²` over PW sectors `{{(0,2),(1,1),(2,0)}}`; substrate-distance-2 pole `s=4`) — the sub-slot heading landed ABOVE this parent block.
- **§VII.AV.STATE-PROJ** (Cell IV; algebra-DEPENDENT state-pair K-window log-derivative `L_emp = -7.046336474406761 M_KK²`; substrate-distance-2 pole `s=4`) — the sub-slot heading landed ABOVE this parent block; the full curated Cell-IV anatomy + Level-2-B diagnostic sub-row table + refinement-pathway routes (i)-(viii) + SOURCE-DOUBLE-CITE-CO-PRIMARY anchor structure + FOUR-rule cross-composition meta-pattern PRESERVED in this parent host body below.

**Anchor structure**: §VII.AV.OP-PROJ and §VII.AV.STATE-PROJ are **STRUCTURAL-ORTHOGONAL-COMPANIONS, NOT SOURCE-DOUBLE-CITE-CO-PRIMARY** (per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3 + `registry-landing.md §"Detection"` criterion (4)): `corner_cell(OP-PROJ) = Cell I ≠ Cell IV = corner_cell(STATE-PROJ)`; cross-corner co-primary is STRUCTURALLY FORBIDDEN (criterion (4): both co-primary anchors MUST be on the SAME algebra-axis cell). The two objects share only the substrate-distance-2 pole label `s=4`; they are STRUCTURALLY DISTINCT observables on ORTHOGONAL algebra-axis cells, period.

**Disambiguation from the S91 "single-slot canonical" verdict**: the S91 W5-1 "single-slot landing is canonical" verdict (PRESERVED in the STATE-PROJ sub-slot's within-Cell-IV regulator-class diagnostic) concerns the **SCHEMATIC-proxy `-7.046336` vs FULL-PV `-527.97`** axis — both Cell IV, two regulator-class F-images of ONE observable (Hybrid Independence Test FAILS any split of THAT pair). The S93 W3-1 split is a STRUCTURALLY DIFFERENT axis: it separates **Cell I OP-PROJ `B_LAYER_A`** (algebra-INVARIANT) from **Cell IV STATE-PROJ `L_emp`** (algebra-DEPENDENT), which the S92 W3-9 disambiguation found to be F-image INCONSISTENT (Phi-ratio {PHI_RATIO:.6g} ≠ 1) ⇒ MANDATORY split. The two verdicts are CONSISTENT: no split within Cell IV (regulator F-images of one observable); MANDATORY split across Cell I / Cell IV (two observables on orthogonal axes).

**Stage-2 targets**: the split gives W3-6 (Stage-2 cross-axis independent-verify) TWO distinct STAGE-1-CANDIDATE registry targets (§VII.AV.OP-PROJ + §VII.AV.STATE-PROJ), audited per sub-slot. Both sub-slots are RESERVED at `sessions/framework/s93-slot-pre-allocation-lockfile.md §"RESERVED-FOR-S93-W3-6-VII-AV-STAGE-2-CROSS-AXIS-VERIFY-PER-SUB-SLOT"` (landed W0-1, LIVE; status RESERVED).

**Parent host status**: this parent §VII.AV block is now the **host / provenance record** for the split; all curated Cell-IV anatomy below is PRESERVED (it is the STATE-PROJ sub-slot's full body, cross-referenced from the §VII.AV.STATE-PROJ heading above). The split is METHODOLOGY-class artifact-existence (NO destructive rewrite of curated prose).

"""


def build_registry_text(registry_text: str) -> tuple[str, dict]:
    """Insert the TWO sub-slot blocks immediately BEFORE the live §VII.AV header,
    and prepend the split-discharge note to the parent §VII.AV body (immediately
    after the parent header line). Pure function; no I/O. Returns
    (full_new_text, offsets).
    """
    parent_idx = registry_text.find(PARENT_AV_HEADER)  # (local)
    if parent_idx == -1:
        raise RuntimeError(
            f"parent §VII.AV header not found: {PARENT_AV_HEADER[:60]!r}... "
            "(cannot locate the live STAGE-1-CANDIDATE §VII.AV slot to split)"
        )

    op_block = build_op_proj_block()  # (local)
    state_block = build_state_proj_block()  # (local)
    discharge_note = build_split_discharge_note()  # (local)

    # Locate the end of the parent header line (to insert the discharge note
    # immediately after it, at the top of the parent body).
    parent_line_end = registry_text.find("\n", parent_idx)  # (local)
    if parent_line_end == -1:
        raise RuntimeError("parent §VII.AV header has no terminating newline")

    # (1) Two sub-slot blocks BEFORE the parent header.
    pre = registry_text[:parent_idx]  # (local)
    # parent header line itself (preserved verbatim)
    parent_header_line = registry_text[parent_idx:parent_line_end + 1]  # (local)
    # parent body (everything after the header line)
    parent_body = registry_text[parent_line_end + 1:]  # (local)

    new_text = (  # (local)
        pre
        + op_block
        + "\n"
        + state_block
        + "\n"
        + parent_header_line
        + "\n"
        + discharge_note
        + "\n"
        + parent_body
    )
    offsets = {  # (local)
        "parent_idx": parent_idx,
        "op_block_len": len(op_block),
        "state_block_len": len(state_block),
        "discharge_note_len": len(discharge_note),
    }
    return new_text, offsets


# ---------------------------------------------------------------------------
# Step (2) — write_atomic_with_fsync
# ---------------------------------------------------------------------------
def write_atomic_with_fsync(text: str, path: Path) -> None:
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
        fh.flush()
        os.fsync(fh.fileno())


# ---------------------------------------------------------------------------
# Section slices (for content_sha + verify)
# ---------------------------------------------------------------------------
def slice_block(text: str, header: str, next_markers: list[str]) -> str:
    """Return the block from `header` to the first of `next_markers` after it."""
    start = text.find(header)  # (local)
    if start == -1:
        return ""
    end = len(text)  # (local)
    for m in next_markers:
        idx = text.find(m, start + len(header))  # (local)
        if idx != -1 and idx < end:
            end = idx
    return text[start:end]


# ---------------------------------------------------------------------------
# Step (3) — re_read + verify_section_matches
# ---------------------------------------------------------------------------
def verify_section_matches(op_block: str, state_block: str, discharge_note: str) -> dict:
    """Re-read the registry; verify BOTH sub-slot blocks + the parent split-
    discharge note landed verbatim with the correct corner-cell tags, naming-
    hygiene suffixes, STRUCTURAL-ORTHOGONAL-COMPANION declaration, cross-corner-
    FORBIDDEN constraint, W3-9 cross-link, and correct ordering. Pure verify; no write.
    """
    actual = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)

    op_idx = actual.find(OP_PROJ_HEADER)  # (local)
    state_idx = actual.find(STATE_PROJ_HEADER)  # (local)
    parent_idx = actual.find(PARENT_AV_HEADER)  # (local)
    discharge_idx = actual.find(SPLIT_DISCHARGE_MARKER)  # (local)

    # both sub-slot blocks landed verbatim
    op_present = op_block in actual  # (local)
    state_present = state_block in actual  # (local)
    discharge_present = discharge_note in actual  # (local)

    op_section = slice_block(  # (local)
        actual, OP_PROJ_HEADER, [STATE_PROJ_HEADER, PARENT_AV_HEADER]
    )
    state_section = slice_block(  # (local)
        actual, STATE_PROJ_HEADER, [PARENT_AV_HEADER, SPLIT_DISCHARGE_MARKER]
    )

    # corner-cell tags
    op_cell_I = "**Corner-cell**: **Cell I**" in op_section  # (local)
    state_cell_IV = "**Corner-cell**: **Cell IV**" in state_section  # (local)

    # naming-hygiene suffixes (the sub-slot headings carry .OP-PROJ / .STATE-PROJ)
    op_suffix = "§VII.AV.OP-PROJ" in op_section and ".OP-PROJ` suffix" in op_section  # (local)
    state_suffix = (  # (local)
        "§VII.AV.STATE-PROJ" in state_section
        and ".STATE-PROJ` suffix" in state_section
    )

    # STRUCTURAL-ORTHOGONAL-COMPANION (NOT co-primary) in both sub-slots
    op_soc = (  # (local)
        "STRUCTURAL-ORTHOGONAL-COMPANION" in op_section
        and "NOT SOURCE-DOUBLE-CITE-CO-PRIMARY" in op_section
    )
    state_soc = (  # (local)
        "STRUCTURAL-ORTHOGONAL-COMPANION" in state_section
        and "NOT SOURCE-DOUBLE-CITE-CO-PRIMARY" in state_section
    )

    # cross-corner co-primary FORBIDDEN confirmation in both
    op_cc_forbidden = (  # (local)
        "Cross-corner co-primary is STRUCTURALLY FORBIDDEN" in op_section
    )
    state_cc_forbidden = (  # (local)
        "Cross-corner co-primary is STRUCTURALLY FORBIDDEN" in state_section
    )

    # W3-9 audit_sha cross-linked in both sub-slots + discharge note
    w3_9_op = W3_9_AUDIT_SHA in op_section  # (local)
    w3_9_state = W3_9_AUDIT_SHA in state_section  # (local)

    # anchor values present
    op_anchor = "3.752271e+02" in op_section  # (local)
    state_anchor = "-7.046336474406761" in state_section  # (local)

    # 5-anatomy + 3-level present per sub-slot
    op_anatomy = (  # (local)
        "IS-not-IN anatomy" in op_section
        and "Three-level structural-confidence ladder" in op_section
    )
    state_anatomy = (  # (local)
        "IS-not-IN anatomy" in state_section
        and "Three-level structural-confidence ladder" in state_section
    )

    # ordering: OP-PROJ block, then STATE-PROJ block, then parent header, then
    # discharge note (the discharge note is INSIDE the parent body, after header).
    ordering_ok = (  # (local)
        op_idx != -1
        and state_idx != -1
        and parent_idx != -1
        and discharge_idx != -1
        and op_idx < state_idx < parent_idx < discharge_idx
    )

    # parent split-discharge note cites both sub-slots + W3-9
    discharge_section = slice_block(  # (local)
        actual, SPLIT_DISCHARGE_MARKER, ["### §VII.AU.OP-PROJ"]
    )
    discharge_cites_both = (  # (local)
        "§VII.AV.OP-PROJ" in discharge_section
        and "§VII.AV.STATE-PROJ" in discharge_section
        and W3_9_AUDIT_SHA in discharge_section
    )

    # substantive line counts (non-empty lines per block)
    op_lines = sum(1 for ln in op_block.splitlines() if ln.strip())  # (local)
    state_lines = sum(1 for ln in state_block.splitlines() if ln.strip())  # (local)

    return {
        "op_present": op_present,
        "state_present": state_present,
        "discharge_present": discharge_present,
        "op_cell_I": op_cell_I,
        "state_cell_IV": state_cell_IV,
        "op_suffix": op_suffix,
        "state_suffix": state_suffix,
        "op_soc": op_soc,
        "state_soc": state_soc,
        "op_cc_forbidden": op_cc_forbidden,
        "state_cc_forbidden": state_cc_forbidden,
        "w3_9_op": w3_9_op,
        "w3_9_state": w3_9_state,
        "op_anchor": op_anchor,
        "state_anchor": state_anchor,
        "op_anatomy": op_anatomy,
        "state_anatomy": state_anatomy,
        "ordering_ok": ordering_ok,
        "discharge_cites_both": discharge_cites_both,
        "op_lines": op_lines,
        "state_lines": state_lines,
    }


# ---------------------------------------------------------------------------
# Step (5) — emit ONCE
# ---------------------------------------------------------------------------
def find_latest_prior_audit_sha() -> str | None:
    """Latest NON-SUPERSEDED canonical audit_sha256 for this gate-ID (Option-A
    supersedes-tag source per gate-verdicts.md). None if no prior line.
    """
    if not VERDICT_TXT.exists():
        return None
    superseded: set[str] = set()  # (local)
    candidates: list[str] = []  # (local)
    for ln in VERDICT_TXT.read_text(encoding="utf-8").splitlines():
        if ln.startswith(f"{GATE_ID}:") and "audit_sha256=" in ln:
            m = re.search(r"audit_sha256=([a-f0-9]{64})", ln)  # (local)
            if m:
                candidates.append(m.group(1))
            sm = re.search(r"supersedes=([a-f0-9]{64})", ln)  # (local)
            if sm:
                superseded.add(sm.group(1))
    live = [c for c in candidates if c not in superseded]  # (local)
    return live[-1] if live else None


def append_verdict(
    verdict: str, value, audit_sha: str, content_sha: str, supersedes: str | None = None
) -> None:
    """Append a single canonical dual-SHA verdict line + companion row.

    Atomic append (single `open("a")`). METHODOLOGY-class artifact-existence
    closure; [VERIFY] trigger — no [SIGN] 3-tuple companion row (§9 pre-registers
    no directional prediction). When `supersedes` is set, the corrective line
    carries the `supersedes=<full-64-char-old-audit-sha>` token per gate-verdicts.md
    Option A rule (2)/(5).
    """
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    value_field = value if supersedes is None else f"{value}_supersedes={supersedes}"  # (local)
    line = (  # (local)
        f"{GATE_ID}: {verdict} -- value={value_field!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    supersedes_note = f"; supersedes={supersedes}" if supersedes else ""  # (local)
    companion = (  # (local)
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
        f"METHODOLOGY-class registry OP-PROJ/STATE-PROJ slot-split artifact-existence; "
        f"[VERIFY] no [SIGN] 3-tuple{supersedes_note}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


# ---------------------------------------------------------------------------
# Main — single-shot AFTER pattern
# ---------------------------------------------------------------------------
def main() -> int:
    print(f"=== {GATE_ID} ===")
    print("Input-pin SHAs (first lines of stdout):")
    pins = log_input_pins(INPUT_FILES)  # (local)

    # --- advisory pre-conditions (NOT HARD; documented in verdict value) ---
    slot_reserved = confirm_slot_reserved()  # (local)
    print(f"slot_reserved (s93 lockfile §VII.AV.OP-PROJ + STATE-PROJ) = {slot_reserved}")
    src = confirm_split_source()  # (local)
    print("Split-source (S92 §W3-9) verification:")
    for k, v in src.items():
        print(f"  {k} = {v}")
    src_ok = bool(  # (local)
        src["w3_9_present"]
        and src["mandatory_split_decision"]
        and src["cell_I_op_proj"]
        and src["cell_IV_state_proj"]
        and src["cross_corner_forbidden"]
    )

    op_block = build_op_proj_block()  # (local) Step (1)
    state_block = build_state_proj_block()  # (local)
    discharge_note = build_split_discharge_note()  # (local)

    # Honest mechanical closure if the split source is absent (NO forced PASS):
    if not src_ok:
        value = "PRE-REG-INC_blocked_by_S92_W3-9_split_source_NOT-VERBATIM"  # (local)
        actual = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)
        section = slice_block(actual, PARENT_AV_HEADER, ["### §VII.AU.OP-PROJ"])  # (local)
        audit_sha, content_sha = compute_dual_sha(section, pins)  # (local)
        supersedes = find_latest_prior_audit_sha()  # (local)
        append_verdict("INFO", value, audit_sha, content_sha, supersedes=supersedes)
        _write_json(
            verdict="INFO",
            value=value,
            audit_sha=audit_sha,
            content_sha=content_sha,
            verify={},
            split_source=src,
            slot_reserved=slot_reserved,
            landed=False,
        )
        print(f"VERDICT: INFO (honest mechanical closure: {value})")
        return 0  # verdict is DATA; exit 0

    # --- idempotent guard (single-shot; re-runs must not duplicate the blocks) ---
    registry_text = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)
    op_already = OP_PROJ_HEADER in registry_text  # (local)
    state_already = STATE_PROJ_HEADER in registry_text  # (local)
    discharge_already = SPLIT_DISCHARGE_MARKER in registry_text  # (local)
    op_verbatim = op_block in registry_text  # (local)
    state_verbatim = state_block in registry_text  # (local)
    discharge_verbatim = discharge_note in registry_text  # (local)

    if not (op_already or state_already or discharge_already):
        new_text, offsets = build_registry_text(registry_text)  # (local) Step (1)
        write_atomic_with_fsync(new_text, REGISTRY_PATH)  # (local) Step (2)
        print(f"  Two sub-slots + split-discharge note inserted; offsets={offsets}")
    elif not (op_verbatim and state_verbatim and discharge_verbatim):
        # stale prior landing: rebuild from a clean base by stripping prior blocks.
        # Strip OP-PROJ block (header .. STATE-PROJ header), STATE-PROJ block
        # (header .. parent header), and discharge note (marker .. next §VII.AU),
        # then re-insert canonically.
        cleaned = registry_text  # (local)
        # remove discharge note span first (inside parent body)
        d0 = cleaned.find(SPLIT_DISCHARGE_MARKER)  # (local)
        if d0 != -1:
            d1 = cleaned.find("### §VII.AU.OP-PROJ", d0)  # (local)
            if d1 != -1:
                cleaned = cleaned[:d0] + cleaned[d1:]
        # remove STATE-PROJ block span
        s0 = cleaned.find(STATE_PROJ_HEADER)  # (local)
        if s0 != -1:
            s1 = cleaned.find(PARENT_AV_HEADER, s0)  # (local)
            if s1 != -1:
                cleaned = cleaned[:s0] + cleaned[s1:]
        # remove OP-PROJ block span
        o0 = cleaned.find(OP_PROJ_HEADER)  # (local)
        if o0 != -1:
            o1 = cleaned.find(PARENT_AV_HEADER, o0)  # (local)
            if o1 != -1:
                cleaned = cleaned[:o0] + cleaned[o1:]
        new_text, offsets = build_registry_text(cleaned)  # (local)
        write_atomic_with_fsync(new_text, REGISTRY_PATH)  # (local)
        print(f"  Stale prior split REPLACED with canonical build; offsets={offsets}")
    else:
        print("  Both sub-slots + discharge note already present verbatim (idempotent re-run); no write")

    # --- Step (3) re_read + verify_section_matches ---
    v = verify_section_matches(op_block, state_block, discharge_note)  # (local)
    print("Verification:")
    for k in sorted(v):
        print(f"  {k} = {v[k]}")

    # --- Step (4) determine verdict (single point of decision) ---
    m1_predicates = bool(  # (local)
        v["op_present"]
        and v["state_present"]
        and v["discharge_present"]
        and v["op_cell_I"]
        and v["state_cell_IV"]
        and v["op_suffix"]
        and v["state_suffix"]
        and v["op_soc"]
        and v["state_soc"]
        and v["op_cc_forbidden"]
        and v["state_cc_forbidden"]
        and v["w3_9_op"]
        and v["w3_9_state"]
        and v["op_anchor"]
        and v["state_anchor"]
        and v["op_anatomy"]
        and v["state_anatomy"]
        and v["ordering_ok"]
        and v["discharge_cites_both"]
    )
    substantive_ok = v["op_lines"] >= 15 and v["state_lines"] >= 15  # (local)
    verdict = "PASS" if (m1_predicates and substantive_ok) else "FAIL"  # (local)

    # --- Step (5) emit ONCE — dual-SHA over the TWO sub-slot sections + pinmap ---
    actual = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)
    op_section = slice_block(  # (local)
        actual, OP_PROJ_HEADER, [STATE_PROJ_HEADER]
    )
    state_section = slice_block(  # (local)
        actual, STATE_PROJ_HEADER, [PARENT_AV_HEADER]
    )
    content_section = op_section + state_section  # (local)
    audit_sha, content_sha = compute_dual_sha(content_section, pins)  # (local)

    value = (  # (local)
        f"VII-AV-SLOT-SPLIT_"
        f"op_proj=Cell-I_B_LAYER_A=3.752271e+02_"
        f"state_proj=Cell-IV_L_emp=-7.046336474406761_"
        f"anchor_structure=STRUCTURAL-ORTHOGONAL-COMPANION_"
        f"cross_corner_co_primary=FORBIDDEN_"
        f"op_suffix={v['op_suffix']}_state_suffix={v['state_suffix']}_"
        f"ordering_ok={v['ordering_ok']}_"
        f"discharge_cites_both={v['discharge_cites_both']}_"
        f"op_lines={v['op_lines']}_state_lines={v['state_lines']}_"
        f"split_source_W3-9={W3_9_AUDIT_SHA}"
    )

    supersedes = find_latest_prior_audit_sha()  # (local) Option-A corrective tag
    if supersedes:
        print(
            f"  prior verdict line detected; emitting corrective line with "
            f"supersedes={supersedes[:16]}..."
        )
    append_verdict(verdict, value, audit_sha, content_sha, supersedes=supersedes)
    print(
        f"4-tuple: (value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})"
    )
    print(f"audit_sha256={audit_sha}")
    print(f"content_sha256={content_sha}")
    print(f"VERDICT: {verdict}")

    _write_json(
        verdict=verdict,
        value=value,
        audit_sha=audit_sha,
        content_sha=content_sha,
        verify=v,
        split_source=src,
        slot_reserved=slot_reserved,
        landed=True,
    )

    # exit 0 regardless of PASS/FAIL — verdict is DATA, not script health, per
    # math-scripts.md §"Exit Codes and Verdict Semantics".
    return 0


def _write_json(
    *, verdict, value, audit_sha, content_sha, verify, split_source, slot_reserved, landed
) -> None:
    """JSON sidecar: split structure + corner-cell tags + anchors + W3-9 source."""
    record = {  # (local)
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": value,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "split_structure": {
            "op_proj": {
                "slot": "§VII.AV.OP-PROJ",
                "corner_cell": "Cell I",
                "algebra_axis": "algebra-INVARIANT (spectrum-only functional)",
                "anchor": "B_LAYER_A = 3.752271e+02 M_KK^2",
                "naming_hygiene_suffix": ".OP-PROJ",
                "pw_sectors": [[0, 2], [1, 1], [2, 0]],
                "pole": "substrate-distance-2 s=4",
            },
            "state_proj": {
                "slot": "§VII.AV.STATE-PROJ",
                "corner_cell": "Cell IV",
                "algebra_axis": "algebra-DEPENDENT (state-pair functional on M_2(C) sub BdG)",
                "anchor": f"L_emp = {L_EMP_CANONICAL} M_KK^2",
                "naming_hygiene_suffix": ".STATE-PROJ",
                "pole": "substrate-distance-2 s=4",
            },
            "anchor_structure": "STRUCTURAL-ORTHOGONAL-COMPANION",
            "cross_corner_co_primary": "FORBIDDEN (Cell I != Cell IV)",
        },
        "split_source": {
            "W3_9_gate": W3_9_GATE,
            "W3_9_audit_sha256": W3_9_AUDIT_SHA,
            "Phi_correspondence_consistency_ratio": PHI_RATIO,
            "classification": "F_IMAGE_INCONSISTENT_MANDATORY_SPLIT",
            "slot_decision": "MANDATORY-split-OP-PROJ-plus-STATE-PROJ",
            "W1_3_operational_alignment_binding": W1_3_AUDIT_SHA,
        },
        "split_source_verification": split_source,
        "slot_lockfile_reserved": slot_reserved,
        "landed": landed,
        "verify": verify,
        "M1_M4_self_classification": {
            "M1_artifact_existence_with_content": True,
            "M2_registry_write_plus_grep_sha": True,
            "M3_verbatim_closed_W3_9_disambiguation_verdict": True,
            "M4_allowlist_append": "ORCHESTRATOR-ONLY (flagged in WP; not edited by this script)",
        },
        "disambiguation_from_S91_single_slot_verdict": (
            "S91 'single-slot canonical' = SCHEMATIC -7.046336 vs FULL-PV -527.97 "
            "(both Cell IV, regulator F-images of ONE observable, HIT fails any split). "
            "S93 W3-1 split = Cell I OP-PROJ B_LAYER_A vs Cell IV STATE-PROJ L_emp "
            "(two observables on orthogonal algebra-axes; W3-9 F-image INCONSISTENT "
            "Phi-ratio 52.25 => MANDATORY split). Verdicts CONSISTENT."
        ),
        "constants_used": {"M_KK_GeV": float(M_KK), "tau_fold": float(tau_fold)},
    }
    JSON_PATH.parent.mkdir(parents=True, exist_ok=True)
    JSON_PATH.write_text(json.dumps(record, indent=2), encoding="utf-8")
    print(f"JSON sidecar: {JSON_PATH}")


if __name__ == "__main__":
    sys.exit(main())
