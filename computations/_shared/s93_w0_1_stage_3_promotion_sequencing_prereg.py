#!/usr/bin/env python3
"""
S93 W0-1 — STAGE-3 promotion sequencing pre-registration + anti-inflation
K-counter check + slot-pre-allocation lockfile
==========================================================================

Gate: S93-W0-1-STAGE-3-PROMOTION-SEQUENCING-PREREG  ([AUDIT])

Pre-registered threshold (METHODOLOGY/planning-class; artifact-existence):
  PASS iff ALL THREE deliverables present with required structure:
    (a) 3-tier dependency-ordered sequencing record (Tier-1 anchor-supplying
        -> Tier-2 value-pinning -> Tier-3 Stage-2/STAGE-3 flips), each of the
        7 Tier-3 gates citing its upstream CF IDs + substrate-input-
        orthogonality predicate (the obs_i loaded by exactly ONE cross-reviewer);
    (b) anti-inflation K-counter check pinning the orthogonality basis for the
        5 corpus DIRECTIVEs (corpus sections 18-23) + W9-3 + W9-4, each on its
        OWN axis (no double-count); the section-19 base-CLASS topological-
        stopping-rule cited as the no-fiber-count guard;
    (c) sessions/framework/s93-slot-pre-allocation-lockfile.md created with 7
        RESERVED-FOR blocks, each carrying {Reserved-for, Slot, Workshop,
        Next-free-letter basis, Provenance, Sponsors, Anchor list}.
  No numerical mesh; no substitution chain (the 3-tier order is a partial-order
  DAG FORCED by the S92 verdicts, not a signed numerical delta).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - sessions/archive/session-92/session-92-mack-synthesis.md       (V.1 sequencing + V.2 anti-inflation)
  - sessions/session-plan/session-93-context.md            (7 colliding STAGE-3 slots; per-wave gate IDs)
  - sessions/framework/registry/cross-pillar-bridge-corpus.md  (corpus sections 18-23 DIRECTIVEs)
  - sessions/framework/s90-slot-pre-allocation-lockfile.md (7-field RESERVED-FOR template)
  - canonical_constants.py                                 (feeds audit_sha256 only)
  - script bytes                                           (feeds BOTH SHAs)

Output 4-tuple:
  (value=<deliverables present-state>,
   scheme=STAGE-3-PROMOTION-SEQUENCING-PREREG-PLUS-ANTI-INFLATION-K-COUNTER-PLUS-SLOT-LOCKFILE,
   convention=3-tier-dependency-order-7-Tier-3-gates-cite-CF-IDs-AND-substrate-input-orthogonality-PLUS-5-DIRECTIVE-orthogonality-basis-PLUS-7-RESERVED-FOR-blocks,
   L_max=N/A)

Classification: NON-PHONONIC (methodology / planning pre-registration)

METHODOLOGY
-----------
This is the session's FIRST wave (W0); it runs before any compute wave and is
the upstream prereq for all 7 Tier-3 STAGE-3-flip gates (W2-2, W3-6, W4-2, W5-2,
W5-5, W6-3, W6-4). Per `epistemic-discipline.md` Layer-Decomposition, the 3-tier
sequencing record is the methodology-floor F-image of the substrate-IS dependency
chain: a Tier-1 anchor-supplying gate supplies a substrate-IS value a Tier-2
value-pinning gate consumes, which supplies a substrate-IS verdict a Tier-3
STAGE-3 flip cites. The lockfile is the audit-floor hygiene preventing parallel-
writer registry-write races (the F-image of the substrate's single-canonical-per-
observable discipline). Source-of-truth: mack-synthesis V.1 (sequencing) + V.2
(anti-inflation) + session-93-context.md (the 7 colliding slots + per-gate audit-
SHA upstream pins) + the s90 lockfile template; verbatim from closed-S92 synthesis,
no new derivation.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- No linear algebra; CPU-only, OMP threads capped to 8
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema), atomic append
- Verdict appended to canonical path computations/session-93/s93_gate_verdicts.txt
  (NOT computations/_shared/, per `gate-verdicts.md` Canonical Verdict-File Path)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

from canonical_constants import *  # noqa: F401,F403  (framework discipline; no constants hardcoded)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from pathlib import Path

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
# This script lives at computations/_shared/ (cross-cutting planning gate).
SHARED_DIR = Path(__file__).resolve().parent  # computations/_shared
COMPUTATIONS_DIR = SHARED_DIR.parent  # computations
PROJECT_ROOT = COMPUTATIONS_DIR.parent  # project root
SESSION_DIR = COMPUTATIONS_DIR / "session-93"  # canonical per-session dir
FRAMEWORK_DIR = PROJECT_ROOT / "sessions" / "framework"

SESSION = "S93"  # (local)
GATE_ID = "S93-W0-1-STAGE-3-PROMOTION-SEQUENCING-PREREG"  # (local)
SCHEME = (
    "STAGE-3-PROMOTION-SEQUENCING-PREREG-PLUS-ANTI-INFLATION-K-COUNTER-PLUS-SLOT-LOCKFILE"
)  # (local)
CONVENTION = (
    "3-tier-dependency-order-7-Tier-3-gates-cite-CF-IDs-AND-substrate-input-"
    "orthogonality-PLUS-5-DIRECTIVE-orthogonality-basis-PLUS-7-RESERVED-FOR-blocks"
)  # (local)
L_MAX = "N/A"  # (local) planning pre-registration; no spectral truncation

# Output destinations
OUT_JSON = SESSION_DIR / "s93_w0_1_stage_3_promotion_sequencing_prereg.json"  # (local)
OUT_PNG = SESSION_DIR / "s93_w0_1_stage_3_promotion_sequencing_prereg.png"  # (local)
LOCKFILE = FRAMEWORK_DIR / "s93-slot-pre-allocation-lockfile.md"  # (local)
# Canonical verdict-file path (gate-verdicts.md): computations/session-{N}/
VERDICT_TXT = SESSION_DIR / "s93_gate_verdicts.txt"  # (local)

INPUT_FILES = [
    PROJECT_ROOT / "sessions" / "session-92" / "session-92-mack-synthesis.md",
    PROJECT_ROOT / "sessions" / "session-plan" / "session-93-context.md",
    FRAMEWORK_DIR / "registry" / "cross-pillar-bridge-corpus.md",
    FRAMEWORK_DIR / "s90-slot-pre-allocation-lockfile.md",
    SHARED_DIR / "canonical_constants.py",
]  # (local)


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
#
# S84+ DUAL-SHA SCHEMA (W9a-99):
#   audit_sha256   = sha256( bytes(script) || bytes(canonical) || bytes(pinmap_json) )
#   content_sha256 = sha256( bytes(script) )
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
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


def closure_hash(pins: dict[str, str]) -> str:
    """Stable hash over all input SHAs (invariant to dict ordering)."""
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
    """Compute (audit_sha256, content_sha256) per the S84+ dual-SHA schema."""
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Deliverable (a): the 3-tier dependency-ordered sequencing record
#
# The ordering is a partial-order DAG FORCED by the S92 verdicts (mack-synthesis
# V.1: "the ordering is forced by the verdicts"). Tier-1 anchor-supplying gates
# supply substrate-IS values Tier-2 value-pinning gates consume, which supply
# substrate-IS verdicts the 7 Tier-3 Stage-2/STAGE-3 flips cite. Each Tier-3 gate
# carries its upstream-CF audit-SHA pins (from session-93-context.md per-gate
# 4-field specs) + its substrate-input-orthogonality predicate (the obs_i loaded
# by EXACTLY ONE cross-reviewer per joint-theorem-promotion.md Stage-2 clause).
# ---------------------------------------------------------------------------

def build_tier_1() -> list[dict]:
    """Tier-1 anchor-supplying / decision-closing gates (run FIRST)."""
    return [
        {
            "gate_id": "S93-W3-1-VII-AV-OP-PROJ-STATE-PROJ-SLOT-SPLIT-LANDING",
            "wave": "W3",
            "role": "anchor-supplying (the §VII.AV slot-split + Cell I/Cell IV anchors)",
            "supplies": "§VII.AV.OP-PROJ (Cell I; B_LAYER_A=3.752271e+02 M_KK^2) + "
                        "§VII.AV.STATE-PROJ (Cell IV; L_emp=-7.046336474406761 M_KK^2) anchors",
            "consumed_by": ["S93-W3-6"],
        },
        {
            "gate_id": "S93-W5-1-SUBSTRATE-COCYCLE-RATIO-67-88-R-MACHINE-RECOMPUTE",
            "wave": "W5",
            "alias": "CF-A (MANDATORY substrate arbiter)",
            "role": "decision-closing (the R_machine substrate arbiter for §VII.AY)",
            "supplies": "R_machine = (dE_6 . dE_7)/(dE_8)^2 full-float64 + Sage-QQ; "
                        "re-pin substrate_cocycle_ratio_67_88 + branch label",
            "consumed_by": ["S93-W5-2"],
        },
        {
            "gate_id": "S93-W1-2-VII-BA-STAGE-1-CANDIDATE-REGISTRATION",
            "wave": "W1",
            "role": "anchor-supplying (the §VII.BA joint two-axis theorem Stage-1 registration)",
            "supplies": "§VII.BA STAGE-1-CANDIDATE registry row (clauses (a)/(e) connes + "
                        "binding mack + (c) JOINT); the admissibility certificate downstream CFs cite",
            "consumed_by": ["S93-W1-3 (F-functor)", "(future) §VII.BA Stage-2"],
        },
    ]


def build_tier_2() -> list[dict]:
    """Tier-2 value-pinning compute gates (run NEXT)."""
    return [
        {
            "gate_id": "S93-W2-1-VII-AU-CF37-FREDHOLM-INDEX-INTEGER-TRIPLE",
            "wave": "W2",
            "role": "value-pinning (converts §VII.AU type-pinned canonical to value-pinned)",
            "pins": "Index(P_a.D_K^off-diag.P_a) integer triple in Z^3 for a in "
                    "{(0,0),(0,1),(1,0)} + measured C-gamma sign eps_Cgamma",
            "consumed_by": ["S93-W2-2"],
        },
        {
            "gate_id": "S93-W3-2-VII-AV-PV-BOTTOM-K-RESTRICTION-AT-FIXED-MASS",
            "wave": "W3",
            "role": "value-pinning (the §VII.AV PV-bottom-K discriminator; -527.97 -> -7.046336 recovery)",
            "pins": "d^2 ln kappa_FULL-PV^(bot-K)(K)/d(ln K)^2 at K_horizon, PV mass-tower "
                    "restricted to bottom-K (Casimir ceiling scan)",
            "consumed_by": ["S93-W3-6"],
        },
        {
            "gate_id": "S93-W3-3-VII-AV-OP-PROJ-CLASS-8-7-DEGENERACY-WITNESS",
            "wave": "W3",
            "role": "value-pinning (gates the OP-PROJ ~375 trace-residue soundness as Level-3 anchor)",
            "pins": "Class-8.7 degeneracy-witness: coincident-root declaration at s=4 + "
                    "per-pole multiplicity at level-2 PW sectors {(0,2),(1,1),(2,0)}",
            "consumed_by": ["S93-W3-6"],
        },
        {
            "gate_id": "S93-W4-3-N-PBH-CANONICAL-TRUNCATION-FACTORIZATION",
            "wave": "W4",
            "role": "value-pinning (resolves whether N_eigs(L_max) saturates -> §VII.AX canonical truncation)",
            "pins": "Sage-MCP factorization n_PBH(L_max)=w(L_max).kappa(g) discriminates "
                    "saturation (alpha) vs converging (beta); NOT curve-fit extrapolation",
            "consumed_by": ["S93-W4-2"],
        },
        {
            "gate_id": "S93-W4-1-VII-AX-OP-PROJ-AXIS-A-E2-VERDICT-ARTIFACT-RE-EMISSION",
            "wave": "W4",
            "role": "value-pinning (re-emits §W6-3 Axis-A composite verdict; E2 emit-bug -> PASS)",
            "pins": "axis_a_composite=PASS via Option-A supersedes=19662dc1... "
                    "(E2 emit-bug: all 5 sub-findings + interpretation PASS, only verdict-field FAIL)",
            "consumed_by": ["S93-W4-2"],
        },
    ]


def build_tier_3() -> list[dict]:
    """Tier-3 Stage-2 cross-axis PASS-AND + STAGE-3-PERMANENT flips (run LAST).

    The 7 colliding registry-writes. Each cites its upstream Tier-1+Tier-2 CF IDs
    (with the audit-SHA pins from session-93-context.md per-gate 4-field specs)
    AND its substrate-input-orthogonality predicate: the observable obs_i whose
    data file is loaded by EXACTLY ONE Stage-2 cross-reviewer (the structural
    ceiling per joint-theorem-promotion.md "Substrate-input-orthogonality clause",
    MANDATORY at K=3). For the non-Stage-2 mechanical tag-flips (W2-2, W5-5) the
    predicate names the inherited Stage-2 PASS-AND chain whose orthogonality was
    already established upstream.
    """
    return [
        {
            "gate_id": "S93-W2-2-VII-AU-OP-PROJ-STAGE-3-PERMANENT-PROMOTION",
            "wave": "W2",
            "slot": "§VII.AU.OP-PROJ",
            "flip": "STAGE-1-CANDIDATE -> STAGE-3-PERMANENT (mack tag-flip)",
            "upstream_cf_ids": [
                "S93-W2-1-VII-AU-CF37-FREDHOLM-INDEX-INTEGER-TRIPLE (Tier-2 value-pin)",
                "§W5-4 Stage-2 PASS (audit_sha256=4a95a276...)",
                "§W5-5 Stage-2 PASS (audit_sha256=64d45d71...)",
                "§W5-2 sub-class tag (CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED preserved)",
            ],
            "substrate_input_orthogonality": (
                "Inherited from the §W5-4 + §W5-5 Stage-2 PASS-AND-AND-PASS chain (a "
                "mechanical tag-flip, not a new Stage-2). The upstream Stage-2 chain "
                "established the orthogonality ceiling; W2-2 cites it and preserves the "
                "CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED tag. obs_i = the §W5-4/§W5-5 "
                "structural-ceiling observable loaded by exactly one of the two upstream "
                "cross-reviewers (mechanical inheritance, no new data-file load)."
            ),
            "verdict_class": "mechanical STAGE-3 tag-flip (METHODOLOGY-class; allowlist append)",
        },
        {
            "gate_id": "S93-W3-6-VII-AV-STAGE-2-CROSS-AXIS-VERIFY-PER-SUB-SLOT",
            "wave": "W3",
            "slot": "§VII.AV (per sub-slot: §VII.AV.OP-PROJ + §VII.AV.STATE-PROJ separately)",
            "flip": "Stage-2 cross-axis PASS-AND per sub-slot (CHAINED on W3-1 split)",
            "upstream_cf_ids": [
                "S93-W3-1 slot-split (Tier-1 anchor)",
                "S93-W3-2 PV-bottom-K (Tier-2 value-pin; STATE-PROJ anchor recovery)",
                "S93-W3-3 Class-8.7 degeneracy-witness (Tier-2 value-pin; OP-PROJ ~375 soundness)",
            ],
            "substrate_input_orthogonality": (
                "vdd Axis-A + mack Axis-B IN PARALLEL; OAA exclusion {connes, phonon-first, "
                "volovik}. obs_i = the STATE-PROJ anchor data file (s91_w5_1_full_bdg_pv.npz, "
                "L_emp=-7.046336474406761) loaded by EXACTLY ONE reviewer (mack Axis-B) vs "
                "the OP-PROJ ~375 trace-residue (W3-3 witness npz) loaded by the OTHER "
                "(vdd Axis-A) -> substrate-input orthogonality at >=1 observable. MANDATORY "
                "at K=3 (joint-theorem-promotion.md). Option-A supersedes on re-emission."
            ),
            "verdict_class": "Stage-2 cross-axis PASS-AND (substrate-input-orthogonality K=3)",
        },
        {
            "gate_id": "S93-W4-2-VII-AX-MULTI-PIN-ATLAS-STAGE-2-CROSS-AXIS-VERIFY",
            "wave": "W4",
            "slot": "§VII.AX.OP-PROJ (MULTI-PIN-ATLAS)",
            "flip": "Stage-2 cross-axis PASS-AND on §VII.AX.MULTI-PIN-ATLAS STAGE-1-CANDIDATE",
            "upstream_cf_ids": [
                "S93-W4-1 E2 verdict-artifact re-emission (Tier-2; axis_a_composite=PASS)",
                "S93-W4-3 n_PBH canonical-truncation factorization (Tier-2 value-pin)",
                "§W6-1 PASS (audit_sha256=a006b809...)",
                "§W6-2 K=2 corpus rows (corpus §3/§10/§17)",
            ],
            "substrate_input_orthogonality": (
                "Axis-A in {connes, lizzi}; Axis-B in {volovik, gen-physicist}; mack EXCLUDED. "
                "obs_i = obs_2 (the n_PBH grid s91_w5_3_cf41_upper_22_6.npz, L=14/15/16) "
                "loaded by EXACTLY ONE reviewer; the MULTI-PIN-ATLAS registry-text observable "
                "loaded by the other -> substrate-input orthogonality at obs_2 + machinery "
                "not self-authored. MANDATORY at K=3."
            ),
            "verdict_class": "Stage-2 cross-axis PASS-AND (substrate-input-orthogonality at obs_2)",
        },
        {
            "gate_id": "S93-W5-2-VII-AY-ELEMENT-5-TOLERANCE-STAGE-2-STAGE-3",
            "wave": "W5",
            "slot": "§VII.AY.OP-PROJ",
            "flip": "STAGE-1-CANDIDATE -> STAGE-3-PERMANENT (on 3-axis PASS-AND) + Element-3(iii) K=1->K=2",
            "upstream_cf_ids": [
                "S93-W5-1 R_machine recompute (Tier-1 CF-A; MANDATORY substrate arbiter; ORDERED FIRST)",
                "corpus §21.0 R1/R2/R3 (publication-precision tolerance + DEFERRED tag + two-layer Stage-3)",
            ],
            "substrate_input_orthogonality": (
                "3-axis Stage-2: vdd + cross-pillar spectral-geometer already PASS (substrate-IS "
                "structural ceiling); re-test mack Axis-B-primary at rel_tol>=1e-5 RELATIVE vs the "
                "CF-A substrate-sourced R_machine pin. obs_i = the R_machine full-float64 substrate "
                "recompute (CF-A npz) loaded by EXACTLY ONE reviewer (mack) vs the vdd/spectral-"
                "geometer structural-ceiling observable -> orthogonality. DEFERRED->resolved tag on "
                "the CF-A re-pin; chain holds for any faithful F-image of the 6-sf-sourced anchor."
            ),
            "verdict_class": "Stage-2 3-axis PASS-AND -> STAGE-3-PERMANENT (DEPENDS ON CF-A upstream)",
        },
        {
            "gate_id": "S93-W5-5-VII-AW-OP-PROJ-STAGE-3-PERMANENT-PROMOTION",
            "wave": "W5",
            "slot": "§VII.AW.OP-PROJ",
            "flip": "STAGE-1-CANDIDATE -> STAGE-3-PERMANENT (framework's THIRD; mack tag-flip)",
            "upstream_cf_ids": [
                "§W4-5 Stage-2 composite PASS-AND 6/6 (audit_sha256=4bd3017e...)",
                "S91 W4-3 Axis-A inherited PASS (hawking; audit_sha256=69df5fa7...)",
            ],
            "substrate_input_orthogonality": (
                "Inherited from the §W4-5 Stage-2 composite PASS-AND 6/6 + the S91 W4-3 Axis-A "
                "inherited PASS (a mechanical tag-flip, not a new Stage-2). obs_i = the §W4-5/"
                "S91-W4-3 structural-ceiling observable whose data file was loaded by exactly one "
                "of the two upstream cross-reviewers; parse-tree-expansion invariance preserved. "
                "Orthogonality established upstream; W5-5 cites it."
            ),
            "verdict_class": "mechanical STAGE-3 tag-flip (METHODOLOGY-class; allowlist append)",
        },
        {
            "gate_id": "S93-W6-3-VII-BB-STAGE-2-CROSS-AXIS-VERIFY-REGIME-IDENTITY",
            "wave": "W6",
            "slot": "§VII.BB",
            "flip": "Stage-2 cross-axis PASS-AND + DEGENERATE-pole regime-IDENTITY adjudication; "
                    "STAGE-1->STAGE-3 eligible iff PASS-AND",
            "upstream_cf_ids": [
                "S92 W9-8 §VII.BB FIRST-EXTRACTION DISCHARGED (alpha(s=5,d=4)=0 saturating; subsumes CF-S93-W7-4)",
                "vii_bb_element_5_empirical_anchor_FW=11.763253530952039 + FB-saturation (min eta_FB=0.4465)",
            ],
            "substrate_input_orthogonality": (
                "Axis-A connes + Axis-B landau; volovik EXCLUDED. obs_i = the §W9-8 closed-form "
                "shell-sum npz (composite R^2=0.992 vs FB R^2=0.865 candidate-regime fits) loaded "
                "by EXACTLY ONE reviewer vs the Level-3 empirical anchor "
                "(11.763253530952039) loaded by the other -> substrate-input orthogonality. "
                "JOINT PASS-AND on BOTH axes on the regime identity + Level-3 consistency."
            ),
            "verdict_class": "Stage-2 cross-axis PASS-AND (regime-IDENTITY; STAGE-1->STAGE-3 eligible iff PASS-AND)",
        },
        {
            "gate_id": "S93-W6-4-FWD-C4-PATI-SALAM-STAGE-2-CROSS-AXIS-VERIFY-LEVEL-3",
            "wave": "W6",
            "slot": "§VII.BE",
            "flip": "Stage-2 cross-axis PASS-AND on JOINT clauses + Level-3 empirical anchor at canonical L_max",
            "upstream_cf_ids": [
                "§VII.BE STAGE-1-CANDIDATE text (FWD-C4 Pati-Salam; S92 W7-9 registry landing)",
                "S91 W9-12 derivation (chi_PS:A_K->A_PS; SU(4)_C decomposition; audit_sha256=e16af0ba...)",
            ],
            "substrate_input_orthogonality": (
                "Axis-A connes + Axis-B (volovik OR landau). obs_i = the SU(4)_C decomposition / "
                "chi_PS morphism data (S91 W9-12, M_4(C)->C+M_2(C)+M_2(C)) loaded by EXACTLY ONE "
                "reviewer vs the §VII.BE Level-3 empirical anchor at canonical L_max loaded by the "
                "other -> substrate-input orthogonality at >=1 observable. JOINT PASS-AND + "
                "Level-3 < Level-2 at canonical L_max."
            ),
            "verdict_class": "Stage-2 cross-axis PASS-AND (JOINT clauses + Level-3 < Level-2)",
        },
    ]


def build_sequencing_record() -> dict:
    """Deliverable (a): the 3-tier dependency-ordered sequencing DAG."""
    tier_1 = build_tier_1()  # (local)
    tier_2 = build_tier_2()  # (local)
    tier_3 = build_tier_3()  # (local)
    return {
        "ordering_basis": (
            "Partial-order DAG FORCED by the S92 verdicts (mack-synthesis V.1): "
            "Tier-1 anchor-supplying/decision-closing CFs supply substrate-IS inputs "
            "Tier-2 value-pinning gates consume, which supply substrate-IS verdicts the "
            "7 Tier-3 Stage-2/STAGE-3 flips cite. No Stage-3 flip may be front-loaded "
            "before its anchor-supplying CF."
        ),
        "tier_1_anchor_supplying": tier_1,
        "tier_2_value_pinning": tier_2,
        "tier_3_stage2_stage3_flips": tier_3,
        "tier_3_gate_ids": [g["gate_id"] for g in tier_3],
        "all_seven_tier_3_cite_cf_ids": all(len(g["upstream_cf_ids"]) >= 1 for g in tier_3),
        "all_seven_tier_3_cite_substrate_input_orthogonality": all(
            bool(g["substrate_input_orthogonality"]) for g in tier_3
        ),
    }


# ---------------------------------------------------------------------------
# Section 6 — Deliverable (b): the anti-inflation K-counter orthogonality basis
#
# mack-synthesis V.2: the 5 corpus DIRECTIVEs advance toward K=3 MANDATORY ONLY on
# structurally-DISTINCT Hybrid-Independence-Test instances ((i v ii v iii) ^ iv);
# no two double-count. Each DIRECTIVE advances its OWN axis. corpus §19's
# weighting-functional K-counter is a base-CLASS count (topological stopping rule):
# every weighting factors through the same finite K_0 class, so counting FIBERS is
# illegitimate -- this is the no-fiber-count guard. W9-3 + W9-4 each advance their
# OWN axis distinct from the §18-§23 set.
# ---------------------------------------------------------------------------

def build_anti_inflation_basis() -> dict:
    """Deliverable (b): orthogonality basis for the corpus DIRECTIVE K-counters."""
    directives = [
        {
            "directive": "corpus §18",
            "name": "Composite Bridge-Map Dimensional-Class Admissibility",
            "axis": "composite-bridge-map homogeneity-degree axis (deg(B)=d_A; SUM-factor)",
            "k_counter_status": "K=1 SUGGESTION",
            "advancement_criterion": (
                "Hybrid Independence Test (iii): distinct bridge-map SUM-factor (Wodzicki vs "
                "MS vs ...) on a structurally-distinct (algebra, SUM-factor, pole) triple. "
                "N=2 corpus already (Wodzicki∘HKR + MS∘HKR), magnitude-ordered by SUM-growth."
            ),
        },
        {
            "directive": "corpus §19",
            "name": "Weighting-Functional-Family Canonical (§VII.AU CF-37 (c)∘(d) corridor)",
            "axis": "base-CLASS topological count (K_0(A_K)=Z^3 finite base; Fredholm-module shadow)",
            "k_counter_status": "K=1 SUGGESTION",
            "advancement_criterion": (
                "BASE-CLASS count, NOT a fiber count. TOPOLOGICAL STOPPING RULE: every "
                "weighting Phi_w factors through the SAME finite K_0 class [phi_cd] in Z^3, so "
                "counting weightings (fibers) is ILLEGITIMATE -- the K-counter is a base-count. "
                "THIS IS THE NO-FIBER-COUNT GUARD (mack V.2)."
            ),
            "no_fiber_count_guard": True,
        },
        {
            "directive": "corpus §20",
            "name": "Level-3 Annotation Discipline (§VII.AX.OP-PROJ JE5)",
            "axis": "Level-3 annotation / registry-PASS-criterion axis (central-value-vs-band; "
                    "Class-(i) detector)",
            "k_counter_status": "K=1 SUGGESTION",
            "advancement_criterion": (
                "Hybrid Independence Test: a distinct Level-3 row carrying a band-containment "
                "claim alongside the central-value criterion, on a structurally-distinct "
                "(algebra, anchor, pole) triple. Truncation-envelope-as-gate never credentialed."
            ),
        },
        {
            "directive": "corpus §21",
            "name": "Element-5 Publication-Precision Tolerance + DEFERRED tag (§VII.AY)",
            "axis": "publication-precision Level axis (Class-8.3 rel_tol >= 10^(-sig_figs_of_agreement))",
            "k_counter_status": "K=1 SUGGESTION",
            "advancement_criterion": (
                "Hybrid Independence Test (iv): a distinct STAGE-1-CANDIDATE whose Element-5 "
                "anchor is a published-precision substrate-IS quantity blocked solely by an "
                "over-tight Stage-2 tolerance, on a structurally-distinct (algebra, anchor, pole) "
                "triple with its own independent algebraic envelope (e.g. FWD-C1 n_s Row #55)."
            ),
        },
        {
            "directive": "corpus §22",
            "name": "Regulator-Behavior Sibling Discriminator + 2-bit Fingerprint (§VII.AV)",
            "axis": "regulator-behavior axis (UV-regulator RESPONSE: gapped state-pair regulator-"
                    "INVARIANT vs spectrum-only trace regulator-DEPENDENT ~20%)",
            "k_counter_status": "K=1 SUGGESTION",
            "advancement_criterion": (
                "Hybrid Independence Test (iv): a SIBLING discriminator of algebra-axis "
                "orthogonality on an axis ORTHOGONAL to parse-tree-membership (regulator-RESPONSE "
                "vs parse-tree); NOT folded into the parse-tree K-counter. 2-bit L_max-FLAT-vs-"
                "m_PV-FLOWING fingerprint requires BOTH axes separately scannable."
            ),
        },
        {
            "directive": "corpus §23",
            "name": "Per-Observable Transport-Degree K-counter + SCALE-AND-CHANNEL-TAGGING (AH-TR-1)",
            "axis": "per-observable transport-factor degree axis (deg(T_BZ->pivot): scalar T2-vacuous "
                    "vs substrate-natural non-scalar)",
            "k_counter_status": "K=2 SUGGESTION (n_T instance 1 + alpha_s instance 2)",
            "advancement_criterion": (
                "Hybrid Independence Test (i)/(iv): distinct observable + independent transport-"
                "factor-degree extraction (n_T proven non-scalar; alpha_s degree-OPEN at "
                "S92-W3-CF-S92-W5-1-D). K=3 candidate: deg(T) for r or alpha_t."
            ),
        },
    ]

    methodology_axes = [
        {
            "gate_id": "S93-W9-3-BRIDGE-MAP-SCHEME-SUFFIX-K3-MANDATORY-THIRD-INSTANCE",
            "axis": "bridge-map secondary-class scheme-suffix axis (corpus §10; APS-1975 / "
                    "Cheeger-Simons / Bismut-Cheeger). Axis-beta.",
            "k_counter_status": "K=2 -> K=3 MANDATORY (third structurally-independent instance)",
            "distinct_from_18_23": (
                "DISTINCT axis: the secondary-class-suffix discipline (which eta-scheme labels "
                "Element-3) is ORTHOGONAL to the §18 homogeneity-degree axis (corpus §18.0 scopes "
                "scheme-spread to the secondary-class axis ONLY, NOT the UV-regulator RD axis nor "
                "the homogeneity degree). Candidate: rho-invariant on Pillar-V BdG under 3 eta-schemes."
            ),
        },
        {
            "gate_id": "S93-W9-4-PER-BULLETIN-PER-POLE-K3-ADVANCEMENT",
            "axis": "per-Bulletin-per-pole axis (cross-pillar-bridge-anatomy.md Per-Bulletin-per-pole; "
                    "closed-form beta_i=B[S_i] at NEW (projector, bridge, pole) triplet)",
            "k_counter_status": "K=2 -> K=3 MANDATORY (OPTIONAL/EVOI-gated)",
            "distinct_from_18_23": (
                "DISTINCT axis: per-pole shell-sum exponent beta at a NEW (projector, bridge, pole) "
                "triplet (s=5 or distinct projector) is on the intra-Pillar-VII per-pole ladder, "
                "ORTHOGONAL to the cross-pillar composite-degree (§18), weighting-base-class (§19), "
                "Level-3-annotation (§20), publication-precision (§21), regulator-behavior (§22), "
                "transport-degree (§23) axes. Hybrid Independence Test distinctness required."
            ),
        },
    ]

    return {
        "principle": (
            "mack-synthesis V.2: the 5 corpus DIRECTIVEs (§18-§23) advance toward K=3 "
            "MANDATORY ONLY on structurally-DISTINCT Hybrid-Independence-Test instances "
            "((i v ii v iii) ^ iv per cross-pillar-bridge-anatomy.md); NO two double-count. "
            "Each DIRECTIVE advances its OWN orthogonal axis. W9-3 + W9-4 each advance their "
            "OWN methodology axis distinct from the §18-§23 set."
        ),
        "corpus_directive_axes": directives,
        "methodology_axes_W9_3_W9_4": methodology_axes,
        "no_fiber_count_guard": (
            "corpus §19 weighting-functional K-counter is a BASE-CLASS count (topological "
            "stopping rule): every weighting Phi_w factors through the same finite K_0(A_K)=Z^3 "
            "class, so counting fibers (weightings) is illegitimate. A fiber-count advancement on "
            "the §19 base-count K-counter is the explicit topological-stopping-rule violation "
            "(mack V.2 FAIL condition)."
        ),
        "axes_are_pairwise_orthogonal": True,
        "no_cross_advancement": (
            "§VII.AU+CF-37 (§19, W-2 base-CLASS), §VII.AV (§22, W-3 regulator-behavior), and "
            "§VII.AY (§21, W-5 publication-precision) all TOUCH the substrate-distance pole "
            "structure (s=4 for AU/AV; M_3(C) block for AY) but advance THREE ORTHOGONAL axes -- "
            "no second instance of one credits another's K-counter."
        ),
    }


# ---------------------------------------------------------------------------
# Section 7 — Deliverable (c): the slot-pre-allocation lockfile
#
# 7 RESERVED-FOR blocks, one per colliding STAGE-3 flip, each carrying the 7
# s90-template fields: Reserved-for / Slot / Workshop / Next-free-letter basis /
# Provenance / Sponsors / Anchor list. The mack-cosmic-bridge is sole writer for
# sessions/framework/ registry files (feedback_mack-bridge-role.md); the
# gen-physicist authors the DRAFT lockfile here and the orchestrator/mack confirms
# the landing. Producing scripts consult the lockfile to confirm their slot is
# RESERVED; on runtime occupancy they reroute to next-free-letter and emit FAIL-
# with-remediation per epistemic-discipline.md "Registry-Write Hygiene" item 3.
# ---------------------------------------------------------------------------

def build_lockfile_records() -> list[dict]:
    """Deliverable (c): the 7 RESERVED-FOR block records."""
    return [
        {
            "reserved_for": "S93-W2-2-VII-AU-OP-PROJ-STAGE-3-PERMANENT-PROMOTION gate (S93 W2)",
            "slot": "§VII.AU.OP-PROJ",
            "workshop": "W-2 §VII.AU CF-37 Fredholm-module + STAGE-3 cascade (connes-ncg-theorist)",
            "next_free_letter_basis": (
                "§VII.AU.OP-PROJ is an EXISTING occupied slot (STAGE-1-CANDIDATE, S91 W5/W6 "
                "landing); W2-2 is an in-place STAGE-3-PERMANENT tag-flip, NOT a new-letter "
                "allocation -- the RESERVED-FOR block protects the slot identity against a "
                "concurrent next-free-letter writer claiming §VII.AU during the W2-2 write-window."
            ),
            "provenance": (
                "session-93-plan-w2.md §W2-2; mack-synthesis V.1 Tier-3; cites §W5-4 audit "
                "4a95a276... + §W5-5 audit 64d45d71... Stage-2 PASS-AND-AND-PASS chain"
            ),
            "sponsors": (
                "mack-cosmic-bridge (sole writer); connes-ncg-theorist (Fredholm-index value-pin "
                "co-sign, W2-1); gen-physicist (5-anatomy + sequencing audit co-sign, W0-1)"
            ),
            "anchor_list": (
                "§VII.AU.OP-PROJ parent (STAGE-1-CANDIDATE); §VII.AU CF-37 Fredholm-module-as-"
                "canonical corpus §19; CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED sub-class tag preserved"
            ),
        },
        {
            "reserved_for": "S93-W5-5-VII-AW-OP-PROJ-STAGE-3-PERMANENT-PROMOTION gate (S93 W5)",
            "slot": "§VII.AW.OP-PROJ",
            "workshop": "W-5 §VII.AW STAGE-3 + canonical_constants promotion (mack-cosmic-bridge)",
            "next_free_letter_basis": (
                "§VII.AW.OP-PROJ is an EXISTING occupied slot (S90 W7 CF-45 reservation, "
                "STAGE-1-CANDIDATE since S91 W4); W5-5 is an in-place STAGE-3-PERMANENT tag-flip "
                "(framework's THIRD). NOTE: a SEPARATE S93 W5-6 slot-rename moves the rejected "
                "SU(3)-Coloured-Chirality entry to a free slot (>= §VII.BF); §VII.AW.OP-PROJ "
                "retains the SUBSTRATE-CLOCK-UNIQUENESS-THEOREM and is reserved here for W5-5."
            ),
            "provenance": (
                "session-93-plan-w5.md §W5-5; mack-synthesis V.1 Tier-3; cites §W4-5 Stage-2 "
                "composite PASS-AND 6/6 (audit 4bd3017e...) + S91 W4-3 Axis-A hawking (69df5fa7...)"
            ),
            "sponsors": (
                "mack-cosmic-bridge (sole writer); hawking (S91 W4-3 Axis-A inherited PASS); "
                "gen-physicist (sequencing audit co-sign, W0-1)"
            ),
            "anchor_list": (
                "§VII.AW.OP-PROJ SUBSTRATE-CLOCK-UNIQUENESS-THEOREM (STAGE-1-CANDIDATE); §VII.AQ.OP-PROJ "
                "parent; §VII.AT.OP-PROJ sibling; S90 W7 CF-45 RESERVED-FOR-WORKSHOP-W7-CF-45-VII-AW origin"
            ),
        },
        {
            "reserved_for": "S93-W5-2-VII-AY-ELEMENT-5-TOLERANCE-STAGE-2-STAGE-3 gate (S93 W5)",
            "slot": "§VII.AY.OP-PROJ",
            "workshop": "W-5 §VII.AY R_machine Element-5 tolerance Stage-2/Stage-3 (mack-cosmic-bridge)",
            "next_free_letter_basis": (
                "§VII.AY.OP-PROJ is an EXISTING occupied slot (STAGE-1-CANDIDATE); W5-2 flips it "
                "to STAGE-3-PERMANENT on the 3-axis PASS-AND vs the CF-A substrate-sourced R_machine "
                "pin. ORDERED AFTER CF-A (W5-1, MANDATORY upstream arbiter). RESERVED-FOR protects "
                "the slot against concurrent claim during the tolerance-driven re-emission."
            ),
            "provenance": (
                "session-93-plan-w5.md §W5-2; mack-synthesis V.1 Tier-3 + corpus §21.0 R1/R2/R3; "
                "DEPENDS ON CF-A R_machine recompute (W5-1); DEFERRED-to-R_machine tag (corpus §21)"
            ),
            "sponsors": (
                "mack-cosmic-bridge (sole writer); van-den-dungen-bridge-theorist (Axis-A PASS); "
                "cross-pillar spectral-geometer (Axis-B PASS); gen-physicist (sequencing audit, W0-1)"
            ),
            "anchor_list": (
                "§VII.AY.OP-PROJ Element-5 cocycle-ratio R=(dE_6.dE_7)/(dE_8)^2 (STAGE-1-CANDIDATE); "
                "Element-3(iii) K=1->K=2; corpus §21 K=1 calibration instance; canonical pin "
                "substrate_cocycle_ratio_67_88 re-pinned at CF-A"
            ),
        },
        {
            "reserved_for": "S93-W3-6-VII-AV-STAGE-2-CROSS-AXIS-VERIFY-PER-SUB-SLOT gate (S93 W3)",
            "slot": "§VII.AV (per sub-slot: §VII.AV.OP-PROJ + §VII.AV.STATE-PROJ)",
            "workshop": "W-3 §VII.AV anchor reconciliation + slot-split + Stage-2 (volovik-superfluid-universe-theorist)",
            "next_free_letter_basis": (
                "§VII.AV is split by W3-1 (Tier-1) into §VII.AV.OP-PROJ (Cell I) + §VII.AV.STATE-PROJ "
                "(Cell IV) STRUCTURAL-ORTHOGONAL-COMPANION; cross-corner co-primary FORBIDDEN. W3-6 "
                "Stage-2 verifies per sub-slot. RESERVED-FOR protects BOTH sub-slot identities "
                "against concurrent next-free-letter claim during the per-sub-slot write-window."
            ),
            "provenance": (
                "session-93-plan-w3.md §W3-6 (CHAINED on W3-1 split); mack-synthesis V.1 Tier-3; "
                "corpus §22 three-object reconciliation; substrate-input-orthogonality MANDATORY K=3"
            ),
            "sponsors": (
                "mack-cosmic-bridge (sole writer for registry-text); van-den-dungen-bridge-theorist "
                "(Axis-A); volovik via OAA-exclusion {connes, phonon-first, volovik}; "
                "gen-physicist (sequencing audit, W0-1)"
            ),
            "anchor_list": (
                "§VII.AV.OP-PROJ (Cell I; B_LAYER_A=3.752271e+02 M_KK^2; gated by W3-3 Class-8.7 "
                "witness); §VII.AV.STATE-PROJ (Cell IV; L_emp=-7.046336474406761 M_KK^2 single "
                "Level-3 anchor); FULL-PV -527.97 regulator-class diagnostic sub-row"
            ),
        },
        {
            "reserved_for": "S93-W4-2-VII-AX-MULTI-PIN-ATLAS-STAGE-2-CROSS-AXIS-VERIFY gate (S93 W4)",
            "slot": "§VII.AX.OP-PROJ (MULTI-PIN-ATLAS)",
            "workshop": "W-4 §VII.AX PBH cluster (mack-cosmic-bridge)",
            "next_free_letter_basis": (
                "§VII.AX.OP-PROJ.MULTI-PIN-ATLAS is an EXISTING occupied STAGE-1-CANDIDATE slot; "
                "W4-2 Stage-2 cross-axis verifies it. A SEPARATE W4-4 lands a NEW §VII.AX.STATE-PROJ "
                "companion (Cell IV) and W4-5 promotes n_PBH_FW_central -- those are distinct slots. "
                "RESERVED-FOR protects the MULTI-PIN-ATLAS identity during the Stage-2 write-window."
            ),
            "provenance": (
                "session-93-plan-w4.md §W4-2; mack-synthesis V.1 Tier-3; cites §W6-1 PASS "
                "(a006b809...) + §W6-2 K=2 corpus rows §3/§10/§17; CHAINED on W4-1 E2 re-emission + W4-3"
            ),
            "sponsors": (
                "mack-cosmic-bridge EXCLUDED as reviewer (slot owner); Axis-A in {connes, lizzi}; "
                "Axis-B in {volovik, gen-physicist}; gen-physicist (sequencing audit, W0-1)"
            ),
            "anchor_list": (
                "§VII.AX.OP-PROJ MULTI-PIN-ATLAS (STAGE-1-CANDIDATE); n_PBH grid obs_2 "
                "(s91_w5_3_cf41_upper_22_6.npz, L=14/15/16); §W6-1 PASS a006b809...; E2 re-emission W4-1"
            ),
        },
        {
            "reserved_for": "S93-W6-3-VII-BB-STAGE-2-CROSS-AXIS-VERIFY-REGIME-IDENTITY gate (S93 W6)",
            "slot": "§VII.BB",
            "workshop": "W-6 chirality / HH^1 / Pati-Salam Stage-2 (connes-ncg-theorist)",
            "next_free_letter_basis": (
                "§VII.BB is an EXISTING occupied STAGE-1-CANDIDATE slot (HH^1 s=5; FIRST-EXTRACTION "
                "DISCHARGED at S92 W9-8, alpha(s=5,d=4)=0 saturating). W6-3 Stage-2 verifies + "
                "adjudicates the composite-vs-licensed-FB DEGENERATE-pole regime-IDENTITY; "
                "STAGE-1->STAGE-3 eligible iff PASS-AND. Subsumes CF-S93-W7-4."
            ),
            "provenance": (
                "session-93-plan-w6.md §W6-3; mack-synthesis V.1 Tier-3; cites §W9-8 npz + "
                "vii_bb_element_5_empirical_anchor_FW=11.763253530952039 + FB min eta_FB=0.4465"
            ),
            "sponsors": (
                "connes-ncg-theorist (Axis-A); landau-condensed-matter-theorist (Axis-B); "
                "volovik EXCLUDED; mack-cosmic-bridge (sole writer for registry-text); "
                "gen-physicist (sequencing audit, W0-1)"
            ),
            "anchor_list": (
                "§VII.BB (STAGE-1-CANDIDATE; HH^1 s=5); Level-3 anchor 11.763253530952039; 3 "
                "candidate-regime R^2 fits (composite 0.992 / log 0.953 / FB 0.865); FB-saturation predicate"
            ),
        },
        {
            "reserved_for": "S93-W6-4-FWD-C4-PATI-SALAM-STAGE-2-CROSS-AXIS-VERIFY-LEVEL-3 gate (S93 W6)",
            "slot": "§VII.BE",
            "workshop": "W-6 FWD-C4 Pati-Salam Stage-2 cross-axis verify + Level-3 (connes-ncg-theorist)",
            "next_free_letter_basis": (
                "§VII.BE is an EXISTING occupied STAGE-1-CANDIDATE slot (FWD-C4 Pati-Salam, S91 "
                "W9-12 derivation + S92 W7-9 registry landing; occupied §VII.B letters A-B-C-D-E). "
                "W6-4 Stage-2 cross-axis verifies the JOINT clauses + Level-3 anchor. RESERVED-FOR "
                "protects the §VII.BE identity during the Stage-2 write-window."
            ),
            "provenance": (
                "session-93-plan-w6.md §W6-4; mack-synthesis V.1 Tier-3; cites §VII.BE STAGE-1-"
                "CANDIDATE text + S91 W9-12 derivation (chi_PS:A_K->A_PS; audit e16af0ba...)"
            ),
            "sponsors": (
                "connes-ncg-theorist (Axis-A); volovik-superfluid-universe-theorist OR "
                "landau-condensed-matter-theorist (Axis-B); mack-cosmic-bridge (sole writer); "
                "gen-physicist (sequencing audit, W0-1)"
            ),
            "anchor_list": (
                "§VII.BE FWD-C4 Pati-Salam (STAGE-1-CANDIDATE); A_K_PS=C+M_2(C)_L+M_2(C)_R+M_4(C)_PS "
                "rank-4; SU(4)_C decomposition M_4(C)->C+M_2(C)+M_2(C); Level-3 empirical anchor at canonical L_max"
            ),
        },
    ]


def render_lockfile(records: list[dict]) -> str:
    """Render the s93 lockfile markdown from the 7 RESERVED-FOR records.

    Pattern: sessions/framework/s90-slot-pre-allocation-lockfile.md.
    """
    today = "2026-05-24"  # (local)
    lines: list[str] = []  # (local)
    lines.append("# S93 Slot Pre-Allocation Lockfile")
    lines.append("")
    lines.append(
        "> **Provenance**: S93 W0-1 `S93-W0-1-STAGE-3-PROMOTION-SEQUENCING-PREREG` "
        "(gen-physicist DRAFT author; mack-cosmic-bridge sole-writer confirms landing per "
        "`feedback_mack-bridge-role.md`, " + today + "). Slot pre-allocation lockfile per "
        "`.claude/rules/epistemic-discipline.md §\"Registry-Write Hygiene under Parallel-Writer "
        "Race\"` (multi-slot pre-allocation; canonical pattern: "
        "`sessions/framework/s90-slot-pre-allocation-lockfile.md`). This lockfile pre-allocates "
        "the 7 colliding STAGE-3-PERMANENT registry slots in `sessions/permanent-results-registry.md` "
        "for the S93 §VII Stage-3 program (mack-synthesis §V.1 sequencing) to prevent parallel-"
        "writer race collisions across the 7 Tier-3 STAGE-3-flip gates (W2-2, W3-6, W4-2, W5-2, "
        "W5-5, W6-3, W6-4)."
    )
    lines.append("")
    lines.append("## Purpose")
    lines.append("")
    lines.append(
        "The S93 §VII STAGE-3-PERMANENT-promotion program lands MULTIPLE registry-writes whose "
        "slot-identity must remain non-colliding across waves. The orchestrator pre-allocates the "
        "slot assignments at plan-freeze time (Wave 0, before any compute wave) and records them "
        "here. Each Tier-3 producing script consults this lockfile to confirm its planned slot is "
        "RESERVED to it; on runtime occupancy by an intervening landing, it reroutes to the "
        "next-free-letter and emits FAIL-with-remediation per `epistemic-discipline.md "
        "§\"Registry-Write Hygiene\"` item 3. W0-1 runs FIRST so every colliding STAGE-3 "
        "registry-write has its RESERVED-FOR block before any Tier-3 gate fires; a Tier-3 gate that "
        "fires before this lockfile lands honestly closes PRE-REG-INC "
        "(`value='PRE-REG-INC_blocked_by_s93_slot_lockfile_NOT-LANDED'`) and re-runs after W0-1 per "
        "`mechanical-closure-discipline.md`."
    )
    lines.append("")
    lines.append("## Allocations (7 RESERVED-FOR blocks — one per colliding STAGE-3 flip)")
    lines.append("")
    for rec in records:
        # block tag derived from the gate-ID embedded in reserved_for
        gate = rec["reserved_for"].split(" gate")[0]  # (local)
        slot_tag = (
            rec["slot"].split(" ")[0].replace("§", "VII-").replace(".", "-")
        )  # (local)
        lines.append(f"### RESERVED-FOR-{gate}")
        lines.append("")
        lines.append(f"- **Reserved for**: `{rec['reserved_for']}`")
        lines.append(f"- **Slot**: `{rec['slot']}`")
        lines.append(f"- **Workshop**: {rec['workshop']}")
        lines.append(f"- **Next-free-letter basis**: {rec['next_free_letter_basis']}")
        lines.append(f"- **Provenance**: {rec['provenance']}")
        lines.append(f"- **Sponsors**: {rec['sponsors']}")
        lines.append(f"- **Anchor list**: {rec['anchor_list']}")
        lines.append("")
    lines.append("## Cross-link to canonical slot-allocation lockfile precedent")
    lines.append("")
    lines.append(
        "- `sessions/framework/s90-slot-pre-allocation-lockfile.md` (S90 precedent; this lockfile's "
        "7-field RESERVED-FOR block template)"
    )
    lines.append(
        "- `sessions/framework/s87-slot-pre-allocation-lockfile.md` (S87 origin of the lockfile pattern)"
    )
    lines.append(
        "- `.claude/rules/epistemic-discipline.md §\"Registry-Write Hygiene under Parallel-Writer "
        "Race\"` item 3 (FAIL-with-remediation discipline on runtime occupancy)"
    )
    lines.append(
        "- `.claude/rules/registry-landing.md §\"Bridge-Landing Script Architecture (single-shot "
        "pattern)\"` (single-shot AFTER-pattern emission, no in-place edits)"
    )
    lines.append(
        "- `sessions/archive/session-92/session-92-mack-synthesis.md §V.1` (the dependency-ordered Stage-3 "
        "sequencing record this lockfile backs)"
    )
    lines.append("")
    lines.append("## Lockfile updates")
    lines.append("")
    lines.append("| Date | Operation | Slot | Status |")
    lines.append("|:-----|:----------|:-----|:-------|")
    for rec in records:
        lines.append(
            f"| {today} | Initial allocation per S93 W0-1 (mack-synthesis §V.1 Tier-3) | "
            f"{rec['slot']} | RESERVED |"
        )
    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Section 8 — Optional plot: the Tier-dependency DAG
# ---------------------------------------------------------------------------

def try_render_dag(sequencing: dict) -> bool:
    """Best-effort Tier-dependency DAG diagram. Returns True on success."""
    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        from matplotlib.patches import FancyArrowPatch
    except Exception as exc:  # noqa: BLE001
        print(f"  [plot] matplotlib unavailable ({exc}); skipping optional DAG.")
        return False

    try:
        fig, ax = plt.subplots(figsize=(13, 8))  # (local)
        tiers = [
            ("Tier-1\nanchor-supplying", sequencing["tier_1_anchor_supplying"], "#2c7fb8"),
            ("Tier-2\nvalue-pinning", sequencing["tier_2_value_pinning"], "#41ae76"),
            ("Tier-3\nStage-2/STAGE-3 flips", sequencing["tier_3_stage2_stage3_flips"], "#d95f0e"),
        ]  # (local)
        x_positions = [0.5, 4.0, 8.5]  # (local)
        node_xy: dict[str, tuple[float, float]] = {}  # (local)
        for (label, gates, color), x in zip(tiers, x_positions):
            n = len(gates)  # (local)
            ax.text(x + 0.9, 7.6, label, ha="center", va="center",
                    fontsize=11, fontweight="bold", color=color)
            for i, g in enumerate(gates):
                y = 7.0 - i * (6.6 / max(n, 1))  # (local)
                short = g["gate_id"].replace("S93-", "")  # (local)
                short = short[:34]
                ax.add_patch(plt.Rectangle((x, y - 0.28), 1.8, 0.56,
                                           facecolor=color, alpha=0.25,
                                           edgecolor=color, linewidth=1.2))
                ax.text(x + 0.9, y, short, ha="center", va="center", fontsize=6.0)
                node_xy[g["gate_id"]] = (x + 1.8, y)
                node_xy[g["gate_id"] + "_in"] = (x, y)

        # Tier-3 -> upstream-CF arrows are implicit in the per-gate citations; draw
        # the structural Tier-1 -> Tier-2 -> Tier-3 forward edges by wave.
        for g in sequencing["tier_3_stage2_stage3_flips"]:
            if g["gate_id"] in node_xy:
                x2, y2 = node_xy[g["gate_id"] + "_in"]  # (local)
                # connect from the Tier-2 column center to this Tier-3 node
                arr = FancyArrowPatch((4.0 + 1.8, 3.5), (x2, y2),
                                      arrowstyle="-|>", mutation_scale=8,
                                      color="#999999", alpha=0.35, linewidth=0.7)
                ax.add_patch(arr)

        ax.set_xlim(0, 11)
        ax.set_ylim(0, 8)
        ax.axis("off")
        ax.set_title(
            "S93 STAGE-3 promotion dependency DAG (3 tiers; 7 Tier-3 colliding flips)\n"
            "partial-order FORCED by S92 verdicts (mack-synthesis §V.1)",
            fontsize=11,
        )
        fig.tight_layout()
        fig.savefig(OUT_PNG, dpi=130)
        plt.close(fig)
        print(f"  [plot] DAG written: {OUT_PNG.name}")
        return True
    except Exception as exc:  # noqa: BLE001
        print(f"  [plot] DAG render failed ({exc}); optional artifact skipped.")
        return False


# ---------------------------------------------------------------------------
# Section 9 — Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    """Append a single-line dual-SHA verdict to the canonical verdict file.

    Atomic append (single `open("a")` write — no read-modify-write, no truncate).
    The canonical path is computations/session-93/s93_gate_verdicts.txt per
    `gate-verdicts.md §"Canonical Verdict-File Path"` (NOT computations/_shared/).
    """
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
        f"METHODOLOGY/planning artifact-existence; [AUDIT] no [SIGN] 3-tuple\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


def evaluate_gate(checks: dict[str, bool]) -> str:
    """Artifact-existence-with-content conjunction over the 3 deliverables.

    PASS iff ALL structural requirements hold; FAIL if any deliverable is
    structurally incomplete. No INFO branch fires here unless a Tier-3 gate's
    substrate-input-orthogonality predicate is CONTESTED at author-time (it is
    not — all 7 are declared with an obs_i loaded by exactly one reviewer).
    """
    if all(checks.values()):
        return "PASS"
    return "FAIL"


# ---------------------------------------------------------------------------
# Section 10 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Input pins (first lines of stdout)
    pins = log_input_pins(INPUT_FILES)  # (local)
    closure = closure_hash(pins)  # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. Dual SHAs
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Build the three deliverables
    sequencing = build_sequencing_record()  # (local)  deliverable (a)
    anti_inflation = build_anti_inflation_basis()  # (local)  deliverable (b)
    lockfile_records = build_lockfile_records()  # (local)  deliverable (c)

    # 3. Write the lockfile (deliverable (c) artifact)
    LOCKFILE.parent.mkdir(parents=True, exist_ok=True)
    lockfile_text = render_lockfile(lockfile_records)  # (local)
    LOCKFILE.write_text(lockfile_text, encoding="utf-8")
    print(f"  lockfile written: {LOCKFILE}  ({len(lockfile_records)} RESERVED-FOR blocks)")

    # 4. Write the JSON sidecar (deliverable (a)+(b)+(c) machine-readable)
    SESSION_DIR.mkdir(parents=True, exist_ok=True)
    sidecar = {
        "gate_id": GATE_ID,
        "session": SESSION,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "classification": "NON-PHONONIC",
        "trigger": "[AUDIT]",
        "deliverable_a_sequencing_record": sequencing,
        "deliverable_b_anti_inflation_k_counter": anti_inflation,
        "deliverable_c_lockfile_records": lockfile_records,
        "input_pins": pins,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
    }  # (local)
    OUT_JSON.write_text(json.dumps(sidecar, indent=2), encoding="utf-8")
    print(f"  JSON sidecar written: {OUT_JSON}")

    # 5. Optional DAG plot
    try_render_dag(sequencing)

    # 6. Structural-completeness checks (the artifact-existence-with-content predicate)
    checks: dict[str, bool] = {
        "a_three_tiers_present": (
            len(sequencing["tier_1_anchor_supplying"]) >= 1
            and len(sequencing["tier_2_value_pinning"]) >= 1
            and len(sequencing["tier_3_stage2_stage3_flips"]) == 7
        ),
        "a_seven_tier3_cite_cf_ids": sequencing["all_seven_tier_3_cite_cf_ids"],
        "a_seven_tier3_cite_substrate_input_orthogonality": (
            sequencing["all_seven_tier_3_cite_substrate_input_orthogonality"]
        ),
        "b_five_directives_each_own_axis": (
            len(anti_inflation["corpus_directive_axes"]) >= 5
            and all(d.get("axis") for d in anti_inflation["corpus_directive_axes"])
        ),
        "b_no_fiber_count_guard_cited": any(
            d.get("no_fiber_count_guard") for d in anti_inflation["corpus_directive_axes"]
        ),
        "b_w9_3_w9_4_own_axis": (
            len(anti_inflation["methodology_axes_W9_3_W9_4"]) == 2
            and all(m.get("distinct_from_18_23")
                    for m in anti_inflation["methodology_axes_W9_3_W9_4"])
        ),
        "c_seven_reserved_for_blocks": len(lockfile_records) == 7,
        "c_seven_template_fields_each": all(
            all(k in rec for k in (
                "reserved_for", "slot", "workshop", "next_free_letter_basis",
                "provenance", "sponsors", "anchor_list"))
            for rec in lockfile_records
        ),
        "c_lockfile_on_disk_with_reserved_for": (
            LOCKFILE.exists() and "RESERVED-FOR" in LOCKFILE.read_text(encoding="utf-8")
        ),
        "c_json_on_disk": OUT_JSON.exists(),
    }  # (local)
    print("\n=== structural-completeness checks ===")
    for k, v in checks.items():
        print(f"  [{'PASS' if v else 'FAIL'}] {k}")

    # 7. Verdict
    verdict = evaluate_gate(checks)  # (local)
    value = (
        f"3-deliverables-present:"
        f"sequencing-3-tier-7-Tier-3-cite-CF-IDs-AND-substrate-input-orthogonality="
        f"{checks['a_seven_tier3_cite_substrate_input_orthogonality']};"
        f"anti-inflation-5-DIRECTIVE-orthogonality-basis-PLUS-W9-3-W9-4-no-fiber-count-guard="
        f"{checks['b_no_fiber_count_guard_cited']};"
        f"lockfile-7-RESERVED-FOR-blocks-7-fields-each="
        f"{checks['c_seven_reserved_for_blocks'] and checks['c_seven_template_fields_each']}"
    )  # (local)

    # 8. 4-tuple + append verdict (dual-SHA, S84+ schema)
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)  # (local)
    print()
    print(tag)
    append_verdict(verdict, value, audit_sha, content_sha)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    # Exit 0 on a valid verdict (PASS or FAIL); script-health only.
    return 0


if __name__ == "__main__":
    sys.exit(main())
