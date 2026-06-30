"""
S92 §W7-4 — S92-W7-CF-W8-CONSOLIDATED-4-CROSS-WORKSHOP-K6-K7-PROMOTION-EVENT-LANDING

METHODOLOGY-class corpus row append at
`sessions/framework/registry/cross-pillar-bridge-corpus.md` documenting the
cross-workshop CROSS-AXIS JOINT-WIN K-counter advancement K=6 -> K=7.

mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md` AMRI-PROMOTED
2026-04-28 + per `cross-pillar-bridge-anatomy.md §"Calibration corpus +
K-counter status (pointers)"` corpus-table-maintenance discipline.

K-counter physical meaning (per S91 W8 WP §W8-4 line 885 + §"Wave 8 outcome
summary" line 1963 + CF-W8-CONSOLIDATED-4 spec at S91 W8 WP line 2087):

    K=6 baseline = §VII.AH at S90 W2 CF-20 STAGE-3-PERMANENT promotion
                   (framework's FIRST cross-axis joint theorem to reach
                   STAGE-3-PERMANENT eligibility via Stage-2 PASS at
                   substrate-input-orthogonality structural ceiling).
    K=7 advance  = §VII.AZ.OP-PROJ at S91 §W8-3 STAGE-1-CANDIDATE landing +
                   S91 §W8-4 Stage-2 PASS-AND structural ceiling + S92 §W7-3
                   STAGE-3-PERMANENT-eligible tag-flip. SECOND cross-axis joint
                   theorem at STAGE-3-PERMANENT eligibility AND framework's
                   FIRST cross-MORPHISM family member (structurally distinct
                   from instances #1-#6 cross-PILLAR family members; extends
                   the corpus from cross-PILLAR to cross-MORPHISM at the
                   Pillar-3 internal level via M_3(C)-kernel universality
                   theorem on inheritance morphisms chi_n : A_K -> T_n at
                   max-Wedderburn-rank(T_n) < 3 scope).

VERIFY-INTACT-OR-LAND pattern (Branch A / B / C analogous to W7-3 protocol):

  Branch A — VERIFY-INTACT (PASS, no append): a K=7 calibration instance row
            with §VII.AZ.OP-PROJ identifier already present in the corpus
            file's K-counter section. emit
            value='VERIFY-INTACT-K=7-row-already-landed-no-append-required'
  Branch B — APPEND-APPLIED (PASS, single-shot append): no K=7 row present;
            append the pre-composed 5-column K=7 calibration corpus row
            immediately AFTER the existing §5 K=3 corpus table (preserving
            all prior K=1/K=2/K=3 rows at their current positions on disk).
            The append takes the AFTER-pattern (single-shot write + re-read +
            verify) per `registry-landing.md §"Bridge-Landing Script
            Architecture (single-shot pattern)"`. emit
            value='K=7-row-appended-VII-AZ-OP-PROJ-FIRST-cross-MORPHISM-family-member-mack-sole-writer'
  Branch C — PATTERN-MISMATCH (FAIL, §-anchor ambiguous or §5 table absent):
            corpus file structure has drifted. Mechanical-closure FAIL per
            `mechanical-closure-discipline.md`; emit
            value='PRE-REG-INC_blocked_by_corpus_section_anchor_ambiguity_or_drift'

Plan-text resolution (§W7-4 Step 1): plan body did not name the exact §-anchor;
runtime grep on `cross-pillar-bridge-corpus.md` resolves to §5 "K=3 MANDATORY
corpus — 5-anatomy + 3-level discipline" (the canonical home of the cross-
workshop CROSS-AXIS JOINT-WIN K-counter calibration ladder; §VII.AF.1 / §VII.AJ
/ §VII.W-3.LAB rows 1/2/3 = K=1/K=2/K=3 inline baseline; K=4/K=5/K=6
advancements live in §11 / §12 inline narrative across S88-S91; K=7 row
formalizes the next promotion event for §VII.AZ.OP-PROJ).

Audit_sha cross-link inputs (all three full 64-char SHAs verified at runtime
against source verdict files):

  - S91 §W8-3 STAGE-1-CANDIDATE  (from s91_gate_verdicts.txt:132)
    = 27968f9843fe7e36935b49f0bf259245b26ba740b06c066e659e93b5eb12d806
  - S91 §W8-4 Stage-2 PASS-AND   (from s91_gate_verdicts.txt:178)
    = c0734928cf745645bd6ab6eb67cc49e558120da46ff33d0a41a820e8d0f02da3
  - S92 §W7-3 STAGE-3-eligible   (from s92_gate_verdicts.txt:188)
    = a8f5a3ef291be112363535e2ccd1c2f396193c1bd215fa14d4e6e5b9533cb652

Substrate framing: NON-PHONONIC by classification (corpus row append;
methodology-class artifact-existence predicate; no phononic substrate dynamics
evaluated at execution time). The substrate IS A_K = C (+) H (+) M_3(C) at
tau_fold = 0.19; the M_3(C)-kernel universality theorem IS substrate-IS at
every L_max via Wedderburn-Artin simple-block forcing; the cross-MORPHISM
family class IS STRUCTURALLY DISTINCT from cross-PILLAR family classes at the
substrate-axis layer (cross-MORPHISM covers inheritance morphisms chi_n with
max-Wedderburn-rank(T_n) < 3 at the SAME substrate-IS pillar A_K; cross-PILLAR
covers bridges between structurally distinct substrate-IS pillars). The K=7
row append is the methodology-floor F-image of the substrate-IS cross-MORPHISM
family class's first STAGE-3-PERMANENT-eligibility instance per
`epistemic-discipline.md §"Layer-Decomposition"` F : substrate -> methodology.

Container-thinking violation FORBIDDEN: "the K=7 row CREATES the cross-MORPHISM
family class" — INVERT: "the substrate constitutes the cross-MORPHISM family
class via the M_3(C)-kernel universality theorem's structural distinctness
from cross-PILLAR families; the K=7 row CONFIRMS this at the corpus-table
layer post-STAGE-3-PERMANENT-eligibility promotion".

Cross-references:
  - .claude/rules/cross-pillar-bridge-anatomy.md §"Calibration corpus + K-counter status (pointers)"
  - .claude/rules/joint-theorem-promotion.md §"Stage 3 — Permanent Registration" + §"Substrate-input-orthogonality clause"
  - .claude/rules/mechanical-closure-discipline.md §"When mechanical closure IS acceptable"
  - .claude/rules/phononic-framing.md §"IS Space, Not IN Space"
  - .claude/rules/registry-landing.md §"Bridge-Landing Script Architecture (single-shot pattern)"
  - .claude/rules/epistemic-discipline.md §"Registry-Write Hygiene under Parallel-Writer Race"
  - .claude/rules/gate-verdicts.md (S87+ canonical schema + dual-SHA + 3-tuple + Option A protocol)

VII.AZ.OP-PROJ identifier appears throughout this script; K=6 baseline and
K=7 advancement instance numbers (instance #6 -> instance #7) are documented
in the corpus row text below.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# Anchor sys.path to computations/_shared/ so the canonical_constants import
# resolves regardless of cwd (plan-freeze cwd was repo root; runtime cwd may
# differ when invoked via venv python from any subdirectory).
REPO_ROOT = Path(__file__).resolve().parents[2]
SHARED = REPO_ROOT / "computations" / "_shared"
sys.path.insert(0, str(SHARED))

from canonical_constants import (  # noqa: E402  # MANDATORY per math-scripts.md
    tau_fold,
    substrate_cocycle_ratio_67_88,
)

# ---------------------------------------------------------------------------
# Identity pins (plan-frozen)
# ---------------------------------------------------------------------------

GATE_ID = "S92-W7-CF-W8-CONSOLIDATED-4-CROSS-WORKSHOP-K6-K7-PROMOTION-EVENT-LANDING"  # (local) plan §W7-4
SCHEME = "cross-workshop-CROSS-AXIS-JOINT-WIN-K-counter-corpus-row-append-K6-K7"  # (local) plan §W7-4
CONVENTION = "calibration-corpus-instance-7-FIRST-cross-MORPHISM-family-member-mack-sole-writer-METHODOLOGY-class"  # (local) plan §W7-4
L_MAX = "NA"  # (local) METHODOLOGY-class corpus row append; no spectral truncation
SCHEMA_VERSION = "S87+"  # (local)

# Three audit_sha256 cross-link inputs (full 64-char, retrieved at runtime
# from source verdict files; embedded in the K=7 corpus row for audit trail).
S91_W8_3_AUDIT_SHA_FULL = "27968f9843fe7e36935b49f0bf259245b26ba740b06c066e659e93b5eb12d806"  # (local)
S91_W8_4_AUDIT_SHA_FULL = "c0734928cf745645bd6ab6eb67cc49e558120da46ff33d0a41a820e8d0f02da3"  # (local)
S92_W7_3_AUDIT_SHA_FULL = "a8f5a3ef291be112363535e2ccd1c2f396193c1bd215fa14d4e6e5b9533cb652"  # (local)

# Upstream gate IDs (for cross-reference grep verification)
UPSTREAM_W8_3_GATE_ID = "S91-M3C-KERNEL-UNIVERSALITY-STAGE-1-CANDIDATE-REGISTRY-LANDING"  # (local)
UPSTREAM_W8_4_GATE_ID = "S91-M3C-KERNEL-UNIVERSALITY-STAGE-2-CROSS-AXIS-INDEPENDENT-VERIFY"  # (local)
UPSTREAM_W7_3_GATE_ID = "S92-W7-CF-W8-CONSOLIDATED-3-VII-AZ-OP-PROJ-STAGE-3-PERMANENT-ELIGIBLE"  # (local)

# Pattern markers for VERIFY-INTACT-OR-APPEND classification
K7_ROW_IDENTITY_MARKER = "K=7 cross-MORPHISM"  # (local) Branch A marker (would already be on disk if landed prior)
VII_AZ_OP_PROJ_MARKER = "§VII.AZ.OP-PROJ"  # (local) row identifier
INSTANCE_7_MARKER = "instance #7"  # (local)
CROSS_MORPHISM_MARKER = "cross-MORPHISM"  # (local)

# K=6 baseline marker (the prior K=6 row at instance #6; §VII.AH at S90 W2 CF-20)
K6_BASELINE_INSTANCE_MARKER = "§VII.AH"  # (local)

# Section 5 header anchor in cross-pillar-bridge-corpus.md
SECTION_5_HEADER_PATTERN = r"^## §5\. K=3 MANDATORY corpus.*5-anatomy.*3-level discipline"  # (local) plan §W7-4 Step 1
SECTION_6_HEADER_PATTERN = r"^## §6\. Algebra-axis orthogonality K-counter"  # (local) Step 1: end-of-§5 boundary


# ---------------------------------------------------------------------------
# Hash helpers (canonical pattern; reuse the dual-SHA discipline used by every
# _shared/ closure helper)
# ---------------------------------------------------------------------------

def sha256_of_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def sha256_of_file(path: Path) -> str:
    return sha256_of_text(path.read_text(encoding="utf-8", errors="ignore"))


def closure_hash(pin_map: dict) -> str:
    """Deterministic SHA-256 over the ordered input-pin map (canonical pattern)."""
    canonical = json.dumps(pin_map, sort_keys=True, default=str, ensure_ascii=False)
    return sha256_of_text(canonical)


# ---------------------------------------------------------------------------
# File paths
# ---------------------------------------------------------------------------

CORPUS_PATH = REPO_ROOT / "sessions" / "framework" / "registry" / "cross-pillar-bridge-corpus.md"
REGISTRY_PATH = REPO_ROOT / "sessions" / "permanent-results-registry.md"
S91_VERDICTS_PATH = REPO_ROOT / "computations" / "session-91" / "s91_gate_verdicts.txt"
S92_VERDICTS_PATH = REPO_ROOT / "computations" / "session-92" / "s92_gate_verdicts.txt"
RULE_ANATOMY_PATH = REPO_ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md"


# ---------------------------------------------------------------------------
# Pre-flight cross-reference verification
# ---------------------------------------------------------------------------

def verify_s91_w8_3_anchor() -> bool:
    """Confirm S91 §W8-3 STAGE-1-CANDIDATE landing verdict carries the named SHA."""
    text = S91_VERDICTS_PATH.read_text(encoding="utf-8", errors="ignore")
    return S91_W8_3_AUDIT_SHA_FULL in text and UPSTREAM_W8_3_GATE_ID in text


def verify_s91_w8_4_anchor() -> bool:
    """Confirm S91 §W8-4 Stage-2 PASS-AND verdict carries the named SHA."""
    text = S91_VERDICTS_PATH.read_text(encoding="utf-8", errors="ignore")
    return S91_W8_4_AUDIT_SHA_FULL in text and UPSTREAM_W8_4_GATE_ID in text


def verify_s92_w7_3_anchor() -> bool:
    """Confirm §W7-3 PASS verdict carries the named SHA (CHAINED prereq)."""
    text = S92_VERDICTS_PATH.read_text(encoding="utf-8", errors="ignore")
    return S92_W7_3_AUDIT_SHA_FULL in text and UPSTREAM_W7_3_GATE_ID in text


def verify_vii_az_op_proj_stage3_eligible_in_registry() -> bool:
    """Verify §VII.AZ.OP-PROJ Status line reads STAGE-3-PERMANENT-eligible
    in the permanent-results-registry (per §W7-3 PASS retrofit)."""
    text = REGISTRY_PATH.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    header_re = re.compile(r"^###\s+§VII\.AZ\.OP-PROJ\b")  # (local)
    next_header_re = re.compile(r"^###\s+§VII\.")  # (local)
    status_re = re.compile(r"^\*\*Status\*\*:")  # (local)
    header_idx = None  # (local)
    for i, ln in enumerate(lines):
        if header_re.match(ln):
            header_idx = i
            break
    if header_idx is None:
        return False
    for j in range(header_idx + 1, len(lines)):
        if j > header_idx + 1 and next_header_re.match(lines[j]):
            break
        if status_re.match(lines[j]):
            return "STAGE-3-PERMANENT-eligible" in lines[j]
    return False


# ---------------------------------------------------------------------------
# Corpus §-anchor locator (plan §W7-4 Step 1)
# ---------------------------------------------------------------------------

def locate_section_5_boundaries() -> tuple[int, int, str]:
    """Locate §5 header line and end-of-§5 boundary (next ## §6 header).

    Returns (section_5_header_line_1_indexed, end_of_section_5_line_1_indexed,
             full_section_5_text).
    """
    text = CORPUS_PATH.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    sec5_re = re.compile(SECTION_5_HEADER_PATTERN)  # (local)
    sec6_re = re.compile(SECTION_6_HEADER_PATTERN)  # (local)
    sec5_idx = None  # (local)
    sec6_idx = None  # (local)
    for i, ln in enumerate(lines):
        if sec5_idx is None and sec5_re.match(ln):
            sec5_idx = i
            continue
        if sec5_idx is not None and sec6_re.match(ln):
            sec6_idx = i
            break
    if sec5_idx is None:
        raise RuntimeError("§5 header not found in cross-pillar-bridge-corpus.md")
    if sec6_idx is None:
        raise RuntimeError("§6 boundary header not found after §5 in cross-pillar-bridge-corpus.md")
    block = "\n".join(lines[sec5_idx: sec6_idx])  # (local)
    return sec5_idx + 1, sec6_idx + 1, block


def k7_row_already_landed(section_5_text: str) -> bool:
    """Branch A test: K=7 row + §VII.AZ.OP-PROJ + instance #7 + cross-MORPHISM
    all present in §5 text => already landed (idempotent re-run)."""
    needles = [  # (local)
        VII_AZ_OP_PROJ_MARKER,
        CROSS_MORPHISM_MARKER,
        "K=7",
    ]
    return all(n in section_5_text for n in needles)


# ---------------------------------------------------------------------------
# K=7 corpus row composer (Branch B path)
# ---------------------------------------------------------------------------

def compose_k7_row_text() -> str:
    """Compose the K=7 calibration corpus row as a NEW sub-section appended
    AFTER the existing §5 K=3 corpus table (preserving K=1/K=2/K=3 rows at
    instance #1/#2/#3 unchanged).

    Direction of explanation: substrate -> emergent. The substrate constitutes
    the cross-MORPHISM family class via the M_3(C)-kernel universality
    theorem's structural distinctness from cross-PILLAR families; the K=7
    row CONFIRMS this at the corpus-table layer post-STAGE-3-PERMANENT-
    eligibility promotion.

    The plan called for a 5-column row schema (# | Theorem-Slot | Stage-2-PASS
    audit_sha | substrate-input-pin-assignment | family-class). Because §5's
    on-disk table uses a 4-column schema (# | Workshop | Bridge | Status), the
    K=7 calibration is written as a NEW sub-block immediately after the §5
    table — including (i) the full 5-column row in its own table, (ii) the
    three audit_sha cross-link block, (iii) the substrate-physics direction
    paragraph, (iv) cross-references — so the existing table layout is
    preserved and the K=7 landing is fully self-describing.
    """
    return (
        "\n### Instance #7 — §VII.AZ.OP-PROJ Cross-MORPHISM M_3(C)-Kernel Universality "
        "(S92 W7-CF-W8-CONSOLIDATED-4; K=6 -> K=7 promotion event; 2026-05-23)\n\n"
        "**Provenance**: S92 §W7-CF-W8-CONSOLIDATED-4 cross-workshop CROSS-AXIS JOINT-WIN "
        "K-counter advancement landing (mack-cosmic-bridge sole-writer per "
        "`feedback_mack-bridge-role.md` AMRI-PROMOTED 2026-04-28; corpus-table-maintenance "
        "discipline per `cross-pillar-bridge-anatomy.md §\"Calibration corpus + K-counter "
        "status (pointers)\"`). Landed at S92 W7-4 close, 2026-05-23. Chained on S92 §W7-3 PASS "
        "(`STAGE-3-PERMANENT-eligible` tag-flip retrofit applied at "
        "`sessions/permanent-results-registry.md` §VII.AZ.OP-PROJ Status field).\n\n"
        "**K-counter advancement** (per `feedback_rules-compensate-missing-structure.md` "
        "K=3 promotion threshold; this K-counter already MANDATORY since S88 W4a-17; "
        "K-counter ADVANCES BY ONE STRUCTURAL INSTANCE per cross-workshop CROSS-AXIS "
        "JOINT-WIN landing): `K_post = K_pre + 1 = 6 + 1 = 7`. K=6 baseline at S90 W2 "
        "CF-20 (§VII.AH STAGE-3-PERMANENT promotion via Stage-2 PASS-AND at substrate-"
        "input-orthogonality structural ceiling; framework's FIRST cross-axis joint "
        "theorem at STAGE-3-PERMANENT eligibility, cross-PILLAR family class). K=7 "
        "advancement: §VII.AZ.OP-PROJ at S92 W7-3 STAGE-3-PERMANENT-eligible tag-flip "
        "(post-S91 §W8-3 STAGE-1-CANDIDATE + S91 §W8-4 Stage-2 PASS-AND structural "
        "ceiling); framework's SECOND cross-axis joint theorem at STAGE-3-PERMANENT-"
        "eligibility AND FIRST cross-MORPHISM family member (structurally distinct "
        "from instances #1-#6 cross-PILLAR family members).\n\n"
        "**5-column calibration corpus row** (instance #7; cross-workshop CROSS-AXIS "
        "JOINT-WIN K-counter):\n\n"
        "| # | Theorem / Slot | Stage-2 PASS audit_sha256 | Substrate-input pin assignment | Family class |\n"
        "|:--|:--------------|:--------------------------|:-------------------------------|:-------------|\n"
        "| 7 | §VII.AZ.OP-PROJ — Cross-MORPHISM M_3(C)-Kernel Universality "
        f"(S91 §W8-3 STAGE-1-CANDIDATE landing audit_sha256=`{S91_W8_3_AUDIT_SHA_FULL}`; "
        f"S91 §W8-4 Stage-2 cross-axis PASS-AND at structural ceiling audit_sha256=`{S91_W8_4_AUDIT_SHA_FULL}`; "
        f"S92 §W7-3 STAGE-3-PERMANENT-eligible tag-flip audit_sha256=`{S92_W7_3_AUDIT_SHA_FULL}`) "
        f"| S91 §W8-4 audit_sha256=`{S91_W8_4_AUDIT_SHA_FULL}` (full 64-char). "
        "Axis-A `van-den-dungen-bridge-theorist` (Kasparov KK-projection / K-theory boundary axis); "
        "Axis-B `mack-cosmic-bridge` (laboratory-side / cosmological-bridge axis) per "
        "`joint-theorem-promotion.md §\"Stage-2 Axis-B Selection Protocol\"` MANDATORY-K=1. "
        "Substrate-input-orthogonality at structural ceiling SATISFIED per "
        "`joint-theorem-promotion.md §\"Substrate-input-orthogonality clause\"` MANDATORY-K=3 "
        "(S90 W2 CF-20 promotion event): the two cross-reviewers consumed distinct S91 §W8-3 + "
        "§W8-5 + §W8-6 cross-link substrate-evidence files (Axis-A loaded Connes-Karoubi 1993 "
        "§IV.7 long exact sequence + CM-1995 §III.4 finite-spectral-triple residue formula on "
        "M_3(l) Peter-Weyl block; Axis-B loaded W-5 calibration corpus 3He-B vortex-core "
        "lab-conversion factor + L_max=10 cache filtered sub-block of L_max=12 master cache). "
        "| **cross-MORPHISM** (FIRST corpus member of this family class; structurally distinct "
        "from instances #1-#6 cross-PILLAR family members). Covers inheritance morphisms "
        "chi_n : A_K -> T_n at `max-Wedderburn-rank(T_n) < 3` scope; Pati-Salam-class IN scope, "
        "SU(5) GUT-class OUT of scope per S90 W-3 workshop §V2 line 509. |\n\n"
        "**Hybrid Independence Test predicate evaluation** (per parent rule "
        "`cross-pillar-bridge-anatomy.md §\"Hybrid Independence Test\"`): `(i ∨ ii ∨ iii) ∧ iv` "
        "where (i) distinct substrate-IS pillar, (ii) distinct laboratory-IN pillar, (iii) "
        "distinct bridge map class, (iv) independent algebraic envelope. For §VII.AZ.OP-PROJ "
        "K=7 vs prior K=1-K=6 cross-PILLAR baseline:\n\n"
        "- **(i) distinct substrate-IS pillar**: NO — §VII.AZ.OP-PROJ inhabits the SAME "
        "substrate-IS pillar (A_K = C (+) H (+) M_3(C)) as the K=1-K=6 cross-PILLAR instances; "
        "this is the defining feature of the cross-MORPHISM family (intra-pillar inheritance "
        "morphism rather than cross-pillar bridge).\n"
        "- **(ii) distinct laboratory-IN pillar**: PARTIAL — Pati-Salam-class superfluid host "
        "candidates are queued at S91 §W9 T2.44 CF-S91-PATI-SALAM-IN-SCOPE-LABORATORY-PILLAR-"
        "CANDIDATE-IDENTIFICATION (HIT K=2 -> K=3 MANDATORY promotion target).\n"
        "- **(iii) distinct bridge map class**: YES — the M_3(C)-kernel universality theorem "
        "operates at the C-algebra-MORPHISM layer (Wedderburn-Artin + Schur orthogonality), "
        "structurally distinct from the HKR / K-theory boundary / Connes-Karoubi pairing "
        "bridge map classes of FWD-C1/C2/C3 cross-PILLAR families.\n"
        "- **(iv) independent algebraic envelope**: YES — the kernel-summand NULL identity "
        "`ker(chi|_{M_3(C)}) = M_3(C)` is a regulator-invariant cohomology-class identity "
        "(holds at every L_max), structurally distinct from the L^{-3} convergence envelopes "
        "of FWD-C1/C2/C3 d=4 cross-PILLAR bridges.\n\n"
        "**Disjunction (i ∨ ii ∨ iii)** = (NO ∨ PARTIAL ∨ YES) = TRUE; **conjunction with (iv)** "
        "= TRUE ∧ YES = TRUE; §VII.AZ.OP-PROJ PASSES the Hybrid Independence Test ⇒ K_post=7 "
        "advancement LICENSED.\n\n"
        "**Substrate-physics direction** (per `phononic-framing.md §\"IS Space, Not IN Space\"`): "
        "the substrate IS A_K = C (+) H (+) M_3(C) at tau_fold = 0.19; the M_3(C) Peter-Weyl "
        "block IS substrate-IS at the Wedderburn-Artin + Schur orthogonality axiom layer of the "
        "finite spectral triple; the cross-MORPHISM family class IS STRUCTURALLY DISTINCT from "
        "cross-PILLAR family classes via the parse-tree distinction (intra-pillar inheritance "
        "morphism chi : A_K -> T at max-Wedderburn-rank(T) < 3 vs cross-pillar bridge between "
        "structurally distinct substrate-IS pillars); the K=7 row CONFIRMS the substrate-IS "
        "theorem's structural distinctness at the corpus-table layer post-STAGE-3-PERMANENT-"
        "eligibility promotion. Container-thinking violation FORBIDDEN: \"the K=7 row CREATES "
        "the cross-MORPHISM family class\" ⇒ INVERT: \"the substrate constitutes the "
        "cross-MORPHISM family class via the M_3(C)-kernel universality theorem; the K=7 row "
        "CONFIRMS the framework's FIRST member at STAGE-3-PERMANENT-eligibility at the "
        "corpus-table layer post-§W7-3 PASS\".\n\n"
        "**Cross-references**:\n"
        f"- Parent rule: `.claude/rules/cross-pillar-bridge-anatomy.md §\"Calibration corpus + "
        "K-counter status (pointers)\"` (cross-workshop CROSS-AXIS JOINT-WIN K-counter MANDATORY "
        "since S88 W4a-17; K=7 advancement at S92 W7-CF-W8-CONSOLIDATED-4).\n"
        f"- Joint-theorem 4-stage pathway: `.claude/rules/joint-theorem-promotion.md §\"Stage 3 "
        "— Permanent Registration\"` (STAGE-3-PERMANENT-eligibility PASS criterion) + "
        "`§\"Substrate-input-orthogonality clause\"` MANDATORY-K=3 (S90 W2 CF-20 promotion event).\n"
        f"- K=6 baseline instance: §VII.AH at S90 W2 CF-20 (FIRST cross-axis joint theorem at "
        "STAGE-3-PERMANENT eligibility; cross-PILLAR family class; substrate-input-orthogonality "
        "at structural ceiling SATISFIED at S89 W4-7 obs2+obs3 Stage-2 PASS 8/8 audit_sha256=`4fcd7d29af51c56d8c6620bc2c323970b96edc053e432232e680903d8926536a`).\n"
        f"- K=7 instance (this row): §VII.AZ.OP-PROJ at S92 W7-CF-W8-CONSOLIDATED-4 (S91 §W8-3 "
        f"STAGE-1-CANDIDATE audit_sha256=`{S91_W8_3_AUDIT_SHA_FULL}`; S91 §W8-4 Stage-2 PASS-AND "
        f"audit_sha256=`{S91_W8_4_AUDIT_SHA_FULL}`; S92 §W7-3 STAGE-3-PERMANENT-eligible "
        f"tag-flip audit_sha256=`{S92_W7_3_AUDIT_SHA_FULL}`).\n"
        f"- Forward K=8 / K=9 candidates: queued at S91 §W9 T2.44 "
        "CF-S91-PATI-SALAM-IN-SCOPE-LABORATORY-PILLAR-CANDIDATE-IDENTIFICATION (FWD-C4 "
        "Pati-Salam STAGE-1-CANDIDATE landing per S92 §W7-9) + rank >= 3 extensions per "
        "`.claude/rules/inheritance-falsifier-protocol.md §\"Generalization beyond 3He-B\"`.\n"
        f"- Layer-functor: `.claude/rules/epistemic-discipline.md §\"Layer-Decomposition\"` "
        "F : substrate -> methodology -> audit; this K=7 row is the methodology-floor F-image "
        "of the substrate-IS cross-MORPHISM family class's first STAGE-3-PERMANENT-eligibility "
        "instance at the corpus-table layer.\n"
        f"- `.claude/rules/feedback_rules-compensate-missing-structure.md` K-counter advancement "
        "criterion (this cross-workshop K-counter is already MANDATORY since S88 W4a-17; K=7 "
        "advancement adds the FIRST cross-MORPHISM family member, extending the corpus from "
        "cross-PILLAR-only saturation to cross-MORPHISM family inclusion).\n\n"
        "---\n"
    )


# ---------------------------------------------------------------------------
# AFTER-pattern single-shot append (registry-write hygiene per
# epistemic-discipline.md §"Registry-Write Hygiene under Parallel-Writer Race")
# ---------------------------------------------------------------------------

def append_k7_row_atomic(insertion_text: str, sec6_header_line_1_indexed: int) -> None:
    """Insert the K=7 row text immediately BEFORE the ## §6 header line
    (end of §5 boundary). Uses a single read + compose-in-memory + write
    pattern. Parallel-writer-safe because this script is the sole writer of
    corpus row appends per mack-sole-writer discipline."""
    text = CORPUS_PATH.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines(keepends=True)
    # Insert at index = sec6_header_line_1_indexed - 1 (0-indexed); insertion
    # places the K=7 block right before the next ## §6 header.
    insert_idx = sec6_header_line_1_indexed - 1  # (local)
    # Ensure the insertion ends with a trailing newline so the §6 header
    # remains at column 0 of its own line.
    if not insertion_text.endswith("\n"):
        insertion_text = insertion_text + "\n"
    new_lines = lines[:insert_idx] + [insertion_text] + lines[insert_idx:]  # (local)
    payload = "".join(new_lines)  # (local)
    CORPUS_PATH.write_text(payload, encoding="utf-8", newline="\n")


# ---------------------------------------------------------------------------
# Verdict-line emission (canonical S87+ schema + dual-SHA + 3-tuple)
# ---------------------------------------------------------------------------

def append_verdict(
    composite_verdict: str,
    value: str,
    audit_sha256: str,
    content_sha256: str,
    sign_verdict: str,
    magnitude_verdict: str,
    regime_verdict: str,
) -> None:
    """Append the canonical S87+ verdict triplet atomically (single open('a') write).

    Three lines per the registry-write hygiene rule for parallel-writer-safe
    append:
      (1) canonical line
      (2) dual-SHA companion comment row (W9a-99 split)
      (3) schema-v2 3-tuple annotation (S87+; trigger is [AUDIT])
    """
    canonical = (
        f"{GATE_ID}: {composite_verdict} -- value='{value}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha256} content_sha256={content_sha256} "
        f"schema_version={SCHEMA_VERSION}"
    )
    audit_short = audit_sha256[:16]  # (local)
    content_short = content_sha256[:16]  # (local)
    dual_sha_row = (
        f"# audit_sha256_short={audit_short} content_sha256_short={content_short} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); composite over "
        f"corpus-row-append pin map + S91 §W8-3 + S91 §W8-4 + S92 §W7-3 audit_sha cross-links"
    )
    tuple_row = (
        f"# sign_verdict={sign_verdict} magnitude_verdict={magnitude_verdict} "
        f"regime_verdict={regime_verdict} # {GATE_ID} 3-tuple annotation (S87 schema-v2); "
        f"composite={composite_verdict}; [AUDIT] trigger; K=7 cross-MORPHISM FIRST instance"
    )
    payload = canonical + "\n" + dual_sha_row + "\n" + tuple_row + "\n"
    with open(S92_VERDICTS_PATH, "a", encoding="utf-8", newline="\n") as f:
        f.write(payload)


# ---------------------------------------------------------------------------
# Main verify-intact-or-append driver (single-shot AFTER-pattern)
# ---------------------------------------------------------------------------

def main() -> int:
    # ---- Step 0: pre-flight cross-reference verification -----------------
    s91_w8_3_ok = verify_s91_w8_3_anchor()  # (local)
    s91_w8_4_ok = verify_s91_w8_4_anchor()  # (local)
    s92_w7_3_ok = verify_s92_w7_3_anchor()  # (local)
    vii_az_stage3_in_registry = verify_vii_az_op_proj_stage3_eligible_in_registry()  # (local)

    cross_refs_ok = s91_w8_3_ok and s91_w8_4_ok and s92_w7_3_ok  # (local)

    # ---- Step 1: resolve corpus §-anchor (single match expected) ---------
    sec5_header_line, sec6_header_line, section_5_text = locate_section_5_boundaries()

    # ---- Step 2: branch classifier ---------------------------------------
    branch = None  # (local) "A" intact | "B" append-applied | "C" pattern-mismatch
    composite_verdict = None  # (local)
    value = None  # (local)
    sign_verdict = "N/A"  # (local) AUDIT gate; no direction predicted
    magnitude_verdict = None  # (local)
    regime_verdict = None  # (local)
    insertion_text_applied = None  # (local)

    pre_append_corpus_sha = sha256_of_file(CORPUS_PATH)  # (local)

    if not cross_refs_ok:
        branch = "C"
        composite_verdict = "FAIL"
        value = (
            f"PRE-REG-INC_blocked_by_cross_ref_verification_FAIL"
            f"_s91_w8_3_ok={s91_w8_3_ok}"
            f"_s91_w8_4_ok={s91_w8_4_ok}"
            f"_s92_w7_3_ok={s92_w7_3_ok}"
        )
        magnitude_verdict = "FAIL"
        regime_verdict = "VALID"
    elif k7_row_already_landed(section_5_text):
        branch = "A"
        composite_verdict = "PASS"
        value = (
            "VERIFY-INTACT-K=7-row-already-landed-no-append-required"
            f"_pre_append_corpus_sha={pre_append_corpus_sha[:16]}"
            f"_sec5_line={sec5_header_line}"
            f"_sec6_line={sec6_header_line}"
        )
        magnitude_verdict = "PASS"
        regime_verdict = "VALID"
    else:
        # Branch B: append the K=7 row using single-shot AFTER-pattern.
        insertion_text_applied = compose_k7_row_text()
        append_k7_row_atomic(insertion_text_applied, sec6_header_line)
        # Re-read after fsync (Python write_text closes the file; OS commits)
        sec5_header_line_post, sec6_header_line_post, section_5_text_post = locate_section_5_boundaries()
        # Verify the insertion landed (k7 markers now present in §5)
        landed_ok = k7_row_already_landed(section_5_text_post)  # (local)
        cross_morphism_present = CROSS_MORPHISM_MARKER in section_5_text_post  # (local)
        vii_az_present = VII_AZ_OP_PROJ_MARKER in section_5_text_post  # (local)
        # Verify K=6 baseline (§VII.AH) NOT disturbed elsewhere in §5
        # (§VII.AH lives at §11/§12 inline, not in §5 table; we just verify the
        # 3-row table at instance #1/#2/#3 is intact via the §VII.AF.1 marker)
        prior_K3_intact = "§VII.AF.1" in section_5_text_post and "§VII.W-3.LAB" in section_5_text_post  # (local)
        if landed_ok and cross_morphism_present and vii_az_present and prior_K3_intact:
            branch = "B"
            composite_verdict = "PASS"
            value = (
                "K=7-row-appended-VII-AZ-OP-PROJ-FIRST-cross-MORPHISM-family-member-mack-sole-writer"
                f"_K_pre=6_K_post=7"
                f"_sec5_line={sec5_header_line_post}"
                f"_sec6_line={sec6_header_line_post}"
                f"_prior_K3_intact={prior_K3_intact}"
                f"_cross_morphism_marker_present={cross_morphism_present}"
            )
            magnitude_verdict = "PASS"
            regime_verdict = "VALID"
        else:
            branch = "C"
            composite_verdict = "FAIL"
            value = (
                f"PRE-REG-INC_blocked_by_post_append_verification_FAIL"
                f"_landed_ok={landed_ok}"
                f"_cross_morphism_present={cross_morphism_present}"
                f"_vii_az_present={vii_az_present}"
                f"_prior_K3_intact={prior_K3_intact}"
            )
            magnitude_verdict = "FAIL"
            regime_verdict = "VALID"

    # ---- Step 5: content_sha256 over post-append corpus K-counter ----
    # Re-read §5 block after any modification for the content_sha256 input
    _, _, final_section_5_text = locate_section_5_boundaries()
    post_append_section_5_sha = sha256_of_text(final_section_5_text)  # (local)
    post_append_corpus_file_sha = sha256_of_file(CORPUS_PATH)  # (local)

    # ---- Step 6: closure SHA over input-pin map ---------------------------
    pin_map = {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "schema_version": SCHEMA_VERSION,
        "S91_W8_3_AUDIT_SHA_FULL": S91_W8_3_AUDIT_SHA_FULL,
        "S91_W8_4_AUDIT_SHA_FULL": S91_W8_4_AUDIT_SHA_FULL,
        "S92_W7_3_AUDIT_SHA_FULL": S92_W7_3_AUDIT_SHA_FULL,
        "K_pre": 6,
        "K_post": 7,
        "instance_number": 7,
        "family_class": "cross-MORPHISM",
        "K6_baseline_instance_marker": K6_BASELINE_INSTANCE_MARKER,
        "VII_AZ_OP_PROJ_marker": VII_AZ_OP_PROJ_MARKER,
        "branch": branch,
        "value": value,
        "pre_append_corpus_file_sha256": pre_append_corpus_sha,
        "post_append_corpus_file_sha256": post_append_corpus_file_sha,
        "post_append_section_5_sha256": post_append_section_5_sha,
        "sec5_header_line_1_indexed_at_landing": sec5_header_line,
        "sec6_header_line_1_indexed_at_landing": sec6_header_line,
        "s91_w8_3_anchor_verified": s91_w8_3_ok,
        "s91_w8_4_anchor_verified": s91_w8_4_ok,
        "s92_w7_3_anchor_verified": s92_w7_3_ok,
        "vii_az_op_proj_stage3_eligible_in_registry": vii_az_stage3_in_registry,
        "script_sha256": sha256_of_file(Path(__file__)),
        "rule_anatomy_sha256": sha256_of_file(RULE_ANATOMY_PATH),
        "registry_sha256_at_dispatch": sha256_of_file(REGISTRY_PATH),
        "s91_verdicts_sha256_at_dispatch": sha256_of_file(S91_VERDICTS_PATH),
        "s92_verdicts_sha256_at_dispatch": sha256_of_file(S92_VERDICTS_PATH),
    }
    audit_sha256 = closure_hash(pin_map)  # (local)
    content_sha256 = post_append_section_5_sha  # (local) content over the §5 K-counter table sub-section

    # ---- Step 7: emit verdict triplet ------------------------------------
    append_verdict(
        composite_verdict=composite_verdict,
        value=value,
        audit_sha256=audit_sha256,
        content_sha256=content_sha256,
        sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
    )

    # ---- Step 8: stdout summary (for orchestrator + agent visibility) ----
    print(f"GATE_ID={GATE_ID}")
    print(f"branch={branch}")
    print(f"composite={composite_verdict}")
    print(f"sign={sign_verdict} magnitude={magnitude_verdict} regime={regime_verdict}")
    print(f"value={value}")
    print(f"audit_sha256={audit_sha256}")
    print(f"content_sha256={content_sha256}")
    print(f"pre_append_corpus_file_sha={pre_append_corpus_sha[:16]}")
    print(f"post_append_corpus_file_sha={post_append_corpus_file_sha[:16]}")
    print(f"sec5_header_line={sec5_header_line} sec6_header_line={sec6_header_line}")
    print(f"K_pre=6 K_post=7 instance_number=7 family_class=cross-MORPHISM")
    print(f"cross_refs: s91_w8_3={s91_w8_3_ok} s91_w8_4={s91_w8_4_ok} s92_w7_3={s92_w7_3_ok}")
    print(f"vii_az_op_proj STAGE-3-eligible in registry: {vii_az_stage3_in_registry}")
    print(f"tau_fold imported from canonical_constants: {tau_fold}")
    print(f"substrate_cocycle_ratio_67_88 imported: {substrate_cocycle_ratio_67_88}")
    print(f"timestamp={datetime.now(timezone.utc).isoformat()}")
    return 0  # script health, NOT verdict (per gate-verdicts.md exit-code discipline)


if __name__ == "__main__":
    raise SystemExit(main())
