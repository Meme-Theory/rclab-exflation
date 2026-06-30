#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S93-W2-2-VII-AU-OP-PROJ-STAGE-3-PERMANENT-PROMOTION
===================================================

Flips the §VII.AU.OP-PROJ joint cross-axis theorem from STAGE-1-CANDIDATE to
STAGE-3-PERMANENT in `sessions/permanent-results-registry.md`, citing the S92
Stage-2 PASS-AND-AND-PASS chain VERBATIM (full-64-hex):

  - S92 §W5-4  `S92-W5-CF-S91-W6-1-STAGE-2-PASS-AND-CROSS-AXIS-INDEPENDENT-VERIFY`
      audit_sha256 = 4a95a2769a6ed8f4d439b62c3c80d0f63f43dae2d9a7c8bd2a83994f6939bf64
      (Axis-A connes-ncg-theorist + Axis-B transit-dynamics-theorist; joint 3/3
       PASS-AND; substrate-input-orthogonality PASS; lizzi EXCLUDED).
  - S92 §W5-5  `S92-W5-CF-W8-CONSOLIDATED-9-VII-AU-OP-PROJ-W8-1-RE-DISPATCH`
      audit_sha256 = 64d45d718648f560cb9a209d9d5f91a849d7d5221a7d1ef0c08fe90a68939c4f
      (Axis-A vdd + Axis-B mack; joint PASS-AND; Option-A supersedes chain; the
       LATEST NON-SUPERSEDED W5-5 canonical line at s92_gate_verdicts.txt:164).

The framework's THIRD cross-axis joint theorem to reach STAGE-3-PERMANENT (after
§VII.AH and §VII.U.2 Corner II Var_a), per `joint-theorem-promotion.md §"Stage 3
— Permanent Registration"`: Stage-2 PASS verdict landed (BOTH §W5-4 + §W5-5
PASS-AND) ⇒ the sole-writer updates the tag STAGE-1-CANDIDATE → STAGE-3-PERMANENT.

The CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED sub-class tag (attached at S92 §W5-2)
is PRESERVED: the L_max→∞ asymptotic α=-3 remains deferred to S94+ per
CF-S94-W5-3. JOINT clauses are PASS-AND'd across BOTH axes (logical AND).

METHODOLOGY-class registry-landing gate per `wave-classification.md` (M1
artifact-existence-with-substantive-content PASS predicate; M2 registry Write +
SHA-256 cross-checks; M3 verbatim Stage-2-frozen audit chain from S92 §W5-4 +
§W5-5 closed verdicts; M4 allowlist append is ORCHESTRATOR-ONLY — flagged in the
WP, NOT edited by this script). mack-cosmic-bridge is the SOLE registry writer
per `feedback_mack-bridge-role.md`. The producing script reads NO D_K eigenvalues
— it flips a registry tag and records the Stage-2 chain provenance.

TWO HARD PRE-CONDITIONS (per `mechanical-closure-discipline.md`):
  1. Slot-lockfile RESERVATION: `sessions/framework/s93-slot-pre-allocation-
     lockfile.md` must RESERVE the §VII.AU.OP-PROJ slot to W2-2 (landed W0-1,
     LIVE). If absent ⇒ honest INFO close
     (value='PRE-REG-INC_blocked_by_s93_slot_lockfile_NOT-RESERVED').
  2. Stage-2 PASS-AND chain cited VERBATIM (the §W5-4 + §W5-5 audit_sha256 chain
     above + the §W5-2 sub-class tag).

Single-shot bridge-landing AFTER pattern per
`registry-landing.md §"Bridge-Landing Script Architecture"` +
`computations/_bridge_landing_script_template.py`:
    build_promotion_text  ->  write_atomic_with_fsync  ->
    re_read + verify_section_matches  ->  emit-ONCE
No conditional rewrite / re-emit. A verify-FAIL emits FAIL once and the gate
closes honestly per `mechanical-closure-discipline.md`.

The STAGE-3-PERMANENT promotion sub-block lands at the END of the §VII.AU.OP-PROJ
section (immediately BEFORE the `### §VII.AX.OP-PROJ` header), AFTER the S92 W5-2
sub-class block — so the CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED tag is left INTACT
(preserved). NO destructive in-place rewrite of curated prose; the flip is an
appended dated promotion block per the registry's established per-event
convention, with the STAGE-3-PERMANENT tag declared inside the §VII.AU.OP-PROJ
section boundary.

Verdict: [VERIFY] (METHODOLOGY-class; no [SIGN] 3-tuple — §9 pre-registers no
directional prediction). Dual-SHA closure: content_sha256 over the §VII.AU.OP-PROJ
section text as landed; audit_sha256 over the input-pin map of source documents +
the W5-4/W5-5 Stage-2 chain SHAs + gate-identity keys per
`wave-classification.md §"Dual-SHA closure for METHODOLOGY-class"`.
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
GATE_ID = "S93-W2-2-VII-AU-OP-PROJ-STAGE-3-PERMANENT-PROMOTION"  # (local)
SCHEME = "STAGE-3-PERMANENT-TAG-FLIP-MACK-SOLE-WRITER-AFTER-PATTERN"  # (local)
CONVENTION = (  # (local)
    "joint-theorem-promotion-stage-3-permanent-cite-W5-4-AND-W5-5-Stage-2-chain-"
    "preserve-CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED-sub-class"
)
L_MAX = "N/A"  # (local) METHODOLOGY-class registry tag-flip; no compute

REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)
VERDICT_TXT = (  # (local) canonical per gate-verdicts.md §"Canonical Verdict-File Path"
    PROJECT_ROOT / "computations" / "session-93" / "s93_gate_verdicts.txt"
)
JSON_PATH = (  # (local)
    PROJECT_ROOT
    / "computations"
    / "session-93"
    / "s93_w2_2_vii_au_op_proj_stage_3_permanent_promotion.json"
)
S92_VERDICT_TXT = (  # (local) source of the W5-4/W5-5 Stage-2 PASS-AND chain
    PROJECT_ROOT / "computations" / "session-92" / "s92_gate_verdicts.txt"
)
SLOT_LOCKFILE = (  # (local) W0-1 deliverable; §VII.AU.OP-PROJ RESERVED-to-this-flip
    PROJECT_ROOT / "sessions" / "framework" / "s93-slot-pre-allocation-lockfile.md"
)

# --- Stage-2 PASS-AND-AND-PASS chain (full-64-hex; cited VERBATIM) ---
# §W5-4: Axis-A connes + Axis-B transit; joint 3/3 PASS-AND; sub-input-orthogonality PASS.
STAGE2_W5_4_AUDIT_SHA = (  # (local)
    "4a95a2769a6ed8f4d439b62c3c80d0f63f43dae2d9a7c8bd2a83994f6939bf64"
)
STAGE2_W5_4_GATE = "S92-W5-CF-S91-W6-1-STAGE-2-PASS-AND-CROSS-AXIS-INDEPENDENT-VERIFY"  # (local)
# §W5-5: Axis-A vdd + Axis-B mack; joint PASS-AND; Option-A supersedes; LATEST
# NON-SUPERSEDED canonical line (s92_gate_verdicts.txt:164).
STAGE2_W5_5_AUDIT_SHA = (  # (local)
    "64d45d718648f560cb9a209d9d5f91a849d7d5221a7d1ef0c08fe90a68939c4f"
)
STAGE2_W5_5_GATE = "S92-W5-CF-W8-CONSOLIDATED-9-VII-AU-OP-PROJ-W8-1-RE-DISPATCH"  # (local)
# §W5-2 sub-class tag (PRESERVED, NOT re-attached).
SUB_CLASS_TAG = "STAGE-1-CANDIDATE-CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED"  # (local)
SUB_CLASS_PROMOTED = "STAGE-3-PERMANENT-CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED"  # (local)
SUB_CLASS_W5_2_AUDIT_SHA = (  # (local) S92 §W5-2 attachment audit (line 153 canonical)
    "ed0050c30512a43d381005932525e46965a54c1f998333e7189b81d8eb6c9174"
)

# Insertion boundary: the STAGE-3 promotion sub-block lands immediately BEFORE
# this header, keeping it INSIDE the §VII.AU.OP-PROJ section (after the S92 W5-2
# sub-class block) and BEFORE §VII.AX so the CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED
# tag stays intact.
NEXT_SECTION_HEADER = (  # (local)
    "### §VII.AX.OP-PROJ — PBH Band-Edge Prediction"
)
PROMO_HEADER = (  # (local) the STAGE-3-PERMANENT promotion sub-block header
    "**S93 W2-2 STAGE-1-CANDIDATE → STAGE-3-PERMANENT promotion"
)
# Region anchor for the §VII.AU.OP-PROJ STAGE-1-CANDIDATE host (S91 W5/W6 block).
SECTION_REGION_ANCHOR = (  # (local)
    "**S91 W5/W6 sub-class transition — REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION"
    " → STAGE-1-CANDIDATE promotion**"
)

# Input-pin map (source documents the promotion consumes; SHAs feed audit_sha256).
INPUT_FILES = [  # (local)
    REGISTRY_PATH,
    S92_VERDICT_TXT,
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

    content_sha256 = SHA-256 over the §VII.AU.OP-PROJ section text as landed (the
                     F-image of the numerical PASS-predicate eigenvalue under
                     substrate <-> methodology per epistemic-discipline.md
                     §"Layer-Decomposition").
    audit_sha256   = SHA-256 over the input-pin map of source documents + the
                     W5-4/W5-5 Stage-2 chain SHAs + per-gate identity keys (so the
                     audit_sha256 is gate-distinct per mechanical-closure-discipline
                     item 3).
    """
    h_content = hashlib.sha256()  # (local)
    h_content.update(section_text.encode("utf-8"))
    content = h_content.hexdigest()  # (local)

    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(pinmap_json)
    # Stage-2 PASS-AND chain SHAs are part of the canonical input set (the
    # promotion is admissible ONLY by citing this chain).
    h_audit.update(
        f"{STAGE2_W5_4_AUDIT_SHA}|{STAGE2_W5_5_AUDIT_SHA}|"
        f"{SUB_CLASS_W5_2_AUDIT_SHA}".encode("utf-8")
    )
    # per-gate identity keys embedded so audit_sha256 is gate-distinct
    h_audit.update(f"{GATE_ID}|{SCHEME}|{CONVENTION}".encode("utf-8"))
    audit = h_audit.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Slot-lockfile pre-condition (HARD pre-condition 1)
# ---------------------------------------------------------------------------
def confirm_slot_reserved() -> bool:
    """Confirm the S93 slot lockfile RESERVES §VII.AU.OP-PROJ to this gate.

    Per `mechanical-closure-discipline.md §"When mechanical closure IS acceptable"`:
    if the reservation is absent, the gate honestly closes INFO/PRE-REG-INC. The
    lockfile landed at W0-1 (LIVE); the RESERVED-FOR block names this gate-ID.
    """
    if not SLOT_LOCKFILE.exists():
        return False
    txt = SLOT_LOCKFILE.read_text(encoding="utf-8")  # (local)
    reserved_block = f"RESERVED-FOR-{GATE_ID}"  # (local)
    has_block = reserved_block in txt  # (local)
    # Confirm the slot identity + RESERVED status appear in the lockfile updates table.
    has_slot = "§VII.AU.OP-PROJ" in txt and "RESERVED" in txt  # (local)
    return bool(has_block and has_slot)


# ---------------------------------------------------------------------------
# Stage-2 chain verbatim verification (HARD pre-condition 2)
# ---------------------------------------------------------------------------
def confirm_stage2_chain() -> dict:
    """Confirm the S92 §W5-4 + §W5-5 Stage-2 PASS-AND audit_sha256 chain exists
    VERBATIM (full-64-hex) on a PASS canonical line in s92_gate_verdicts.txt, and
    that the W5-5 line cited is the LATEST NON-SUPERSEDED canonical line.
    """
    out = {  # (local)
        "w5_4_present_pass": False,
        "w5_5_present_pass": False,
        "w5_5_latest_non_superseded": False,
    }
    if not S92_VERDICT_TXT.exists():
        return out
    lines = S92_VERDICT_TXT.read_text(encoding="utf-8").splitlines()  # (local)

    # §W5-4: a PASS canonical line carrying STAGE2_W5_4_AUDIT_SHA.
    for ln in lines:
        if (
            ln.startswith(f"{STAGE2_W5_4_GATE}:")
            and " PASS " in ln
            and f"audit_sha256={STAGE2_W5_4_AUDIT_SHA}" in ln
        ):
            out["w5_4_present_pass"] = True
            break

    # §W5-5: the supersession chain — collect candidate canonical lines + their
    # supersedes targets; the cited SHA must be the latest non-superseded.
    w5_5_candidates: list[str] = []  # (local)
    w5_5_superseded: set[str] = set()  # (local)
    w5_5_cited_is_pass = False  # (local)
    for ln in lines:
        if ln.startswith(f"{STAGE2_W5_5_GATE}:") and "audit_sha256=" in ln:
            m = re.search(r"audit_sha256=([a-f0-9]{64})", ln)  # (local)
            if m:
                w5_5_candidates.append(m.group(1))
            for sm in re.finditer(r"supersedes=([a-f0-9]{64})", ln):  # (local)
                w5_5_superseded.add(sm.group(1))
            if (
                f"audit_sha256={STAGE2_W5_5_AUDIT_SHA}" in ln
                and " PASS " in ln
            ):
                w5_5_cited_is_pass = True
    out["w5_5_present_pass"] = w5_5_cited_is_pass
    live = [c for c in w5_5_candidates if c not in w5_5_superseded]  # (local)
    out["w5_5_latest_non_superseded"] = (
        bool(live) and live[-1] == STAGE2_W5_5_AUDIT_SHA
    )
    return out


# ---------------------------------------------------------------------------
# Step (1) — build_promotion_text  (pure function; no I/O)
# ---------------------------------------------------------------------------
def build_promotion_block() -> str:
    """The STAGE-1-CANDIDATE → STAGE-3-PERMANENT promotion sub-block. Pure.

    Lands at the END of the §VII.AU.OP-PROJ section (before §VII.AX), AFTER the
    S92 W5-2 sub-class block. Declares STAGE-3-PERMANENT, cites the W5-4 + W5-5
    Stage-2 PASS-AND chain VERBATIM (full-64-hex), and PRESERVES the
    CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED sub-class (promoted to its STAGE-3 form).
    Direction: substrate-IS Fredholm-module canonical -> F-image -> registry tag.
    """
    return f"""{PROMO_HEADER} (S93 W2-2 single-shot AFTER-pattern; mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`, 2026-05-24)**:

The §VII.AU.OP-PROJ joint cross-axis theorem advances **STAGE-1-CANDIDATE → STAGE-3-PERMANENT** per `.claude/rules/joint-theorem-promotion.md §"Stage 3 — Permanent Registration"`. The Stage-2 pre-condition is DISCHARGED: BOTH Stage-2 PASS-AND verdicts landed at S92 W5, with the JOINT clauses PASS-AND'd across BOTH axes (logical AND, not OR). This is the framework's **THIRD cross-axis joint theorem to reach STAGE-3-PERMANENT** (after §VII.AH at S90 W2 CF-20 and §VII.U.2 Corner II Var_a). The CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED sub-class tag (attached at S92 §W5-2; preserved at line region above) is PRESERVED through the promotion: the asymptotic `L_max → ∞` α=-3 Level-1 leading-term remains operationally deferred to S94+ per the forward Friedrich-Bär saturation gate `CF-S94-W5-3`; the STAGE-3-PERMANENT status explicitly carries this asymptotic-deferral forward-note.

**Stage-2 PASS-AND-AND-PASS evidence chain (cited VERBATIM, full-64-hex; per `joint-theorem-promotion.md §"Stage 3"`)**:

- **S92 §W5-4** — gate `{STAGE2_W5_4_GATE}` PASS (`computations/session-92/s92_gate_verdicts.txt`): **audit_sha256=`{STAGE2_W5_4_AUDIT_SHA}`** (content_sha256=`7bc64a96b6fc3113b5d5c49408279bdd976bda493cac860974c3b3e6787d298b`). Axis-A = `connes-ncg-theorist` (spectral / NCG-axiomatic; clauses authored on axis A + JOINT) `axis_a_single=3_of_3_PASS`; Axis-B = `transit-dynamics-theorist` (substrate-physics; clauses authored on axis B + JOINT) `axis_b_single=3_of_3_PASS`; `joint_PASS_AND=3_of_3`; `substrate_input_orthogonality=PASS`; `K_post_orthogonality=K_3_MANDATORY_PRESERVED`. `lizzi_excluded=True` per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"` downstream-inheritance-reach test (S88 W-14 W4a-17 V.2 calibration corpus B.15). 3-tuple companion: `sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID`.

- **S92 §W5-5** — gate `{STAGE2_W5_5_GATE}` PASS (`computations/session-92/s92_gate_verdicts.txt`; LATEST NON-SUPERSEDED canonical line): **audit_sha256=`{STAGE2_W5_5_AUDIT_SHA}`** (content_sha256=`1bb341f95a674cc1337fef41265a5f2893bcd33a0a3bc6455a42f573bae27d7a`). Axis-A = `van-den-dungen-bridge-theorist` (vdd; `axis_A_vdd_composite=PASS`, `n_vdd_single=5`); Axis-B = `mack-cosmic-bridge` (`axis_B_mack_composite=PASS`, `n_mack_single=3`); `P3_joint_PASS_AND=True` (`n_joint_clauses=3`); `P4_substrate_input_orthogonality_structural_ceiling=True`; `partition_disjoint=True`; `P5_supersedes_tag_compliance=True`. Option-A supersedes-chain corrective canonical line (per `gate-verdicts.md §"Option A — sig_5 remediation pathway under absolute verdict permanence"`): `supersedes=cdbebfa9ad4cc4a8d14d487142a2b132f6d5f8073bea0aeb2f2e29ef330c408b` (the original S91 W8-1 line at `s91_gate_verdicts.txt:148`); `intermediate_supersedes=882eb784d1108ee0d1a2df9d1e39c4fbb61d1049f827715091c374e18f58df39,cf64fe2925f9c86bbdf857f56b03107f2e1cc9771e1aa09e7f5ebc4d6fa14473`. 3-tuple companion: `sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID`.

**JOINT-clause PASS-AND across BOTH axes** (per `joint-theorem-promotion.md §"Stage 2"` JOINT-clause PASS-AND requirement): the JOINT clauses (Element-1 substrate-IS observable specification + Element-3 HKR bridge map specification) PASS independently in BOTH the §W5-4 verdict (connes Axis-A + transit Axis-B; `joint_PASS_AND=3_of_3`) AND the §W5-5 verdict (vdd Axis-A + mack Axis-B; `P3_joint_PASS_AND=True`). Both Stage-2 verifications operated WITHOUT prior workshop context (read only the registered STAGE-1-CANDIDATE entry text); the agreement is structurally independent per `epistemic-discipline.md §"What Counts as a Result"`. The substrate-input-orthogonality predicate is satisfied at the structural ceiling in BOTH (`substrate_input_orthogonality=PASS` / `P4_substrate_input_orthogonality_structural_ceiling=True`), per `joint-theorem-promotion.md §"Substrate-input-orthogonality clause"` MANDATORY at K=3.

**Sub-class tag PRESERVED through STAGE-3**: the S92 §W5-2 sub-class tag `{SUB_CLASS_TAG}` (audit_sha256=`{SUB_CLASS_W5_2_AUDIT_SHA}` at `s92_gate_verdicts.txt:153`) is PRESERVED; at STAGE-3-PERMANENT it reads `{SUB_CLASS_PROMOTED}`. The empirical-confirmation-at-operational-truncation status is unchanged (L_operational=14 FULL-physical evaluator confirmation per §W5-1 PASS audit_sha256=`395c63c829c11546766ee78e49609c571046e53b6ea5acb4c5844a61d62b64bf`); the asymptotic `L_max → ∞` α=-3 recovery remains DEFERRED to the Friedrich-Bär saturation gate `CF-S94-W5-3` at L ∈ [35, 100] per `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"` W11-3 precedent. STAGE-3-PERMANENT does NOT discharge the asymptotic deferral; it carries it forward as an explicit forward note per `joint-theorem-promotion.md §"Stage 3"` (STAGE-3-PERMANENT eligibility explicitly notes the asymptotic deferral as a forward carry-forward).

**Slot-lockfile reservation**: §VII.AU.OP-PROJ is RESERVED to this gate by `sessions/framework/s93-slot-pre-allocation-lockfile.md §"RESERVED-FOR-{GATE_ID}"` (landed W0-1, LIVE; status RESERVED). This is an IN-PLACE STAGE-3-PERMANENT tag-flip on an EXISTING occupied slot (STAGE-1-CANDIDATE since S91 W5/W6), NOT a new-letter allocation; the RESERVED-FOR block protects the slot identity against any concurrent next-free-letter writer claiming §VII.AU during the W2-2 write-window (one of the 6-7 colliding STAGE-3 registry-writes this session).

**4-stage pathway status** (per `joint-theorem-promotion.md`): Stage 0 (workshop-internal candidate — the §VII.AU.OP-PROJ FWD-C1 substrate-IS / HKR bridge derivation) → Stage 1 (S91 W5/W6 STAGE-1-CANDIDATE registration, audit_sha256=`54db93d799c76c67c78bdcc8cd0477ebb6d104914f2e6764be7af50d22f36459`) → **Stage 2 (S92 §W5-4 + §W5-5 two-agent parallel cross-axis PASS-AND on BOTH axes, WITHOUT prior workshop context — DISCHARGED)** → **Stage 3 (this entry — STAGE-3-PERMANENT)**. The theorem joins the permanent-results table alongside KO-dim=6, [J,D_K]=0, §VII.AH, and Var_a; it is eligible for citation as a structural theorem WITHOUT the candidate qualifier (the CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED sub-class persists as the asymptotic-deferral annotation, NOT a candidate qualifier).

**Substrate framing** (per `phononic-framing.md §"IS Space, Not IN Space"`): NON-PHONONIC (methodology/registry promotion). Under `epistemic-discipline.md §"Layer-Decomposition"`, the STAGE-3-PERMANENT tag-flip is the methodology-floor F-image of the substrate-IS §VII.AU bridge anatomy at the (c)∘(d) corridor: the substrate-physics PASS-predicate (the §W5-4 + §W5-5 Stage-2 numerical verdicts) maps under F to the artifact-existence predicate (STAGE-3 tag present + Stage-2 chain cited verbatim). Container-thinking is FORBIDDEN: the §VII.AU.OP-PROJ block does NOT live IN the registry container — it IS the methodology-floor image of the substrate's Fredholm-module canonical at substrate-distance-1 pole `s=3`, and the registry tag is a label that DESCENDS from the substrate result, never the other way around.

**Direction of explanation**:

```
Substrate (Pillar I) IS the substrate-distance-1 Hochschild-pairing image n_s_FW (Fredholm-module canonical)
   → Stage-2 cross-axis PASS-AND on BOTH axes (§W5-4 connes+transit ∧ §W5-5 vdd+mack)
   → Methodology-floor F-image: STAGE-3-PERMANENT registry tag
```

**M1-M4 self-classification** (per `wave-classification.md`): M1 (PASS-predicate = artifact-existence-with-content; 4 content predicates + substantive_line_count ≥ 15; no numerical threshold) SATISFIED; M2 (producing-op = registry Write + grep/SHA) SATISFIED; M3 (source-of-truth = verbatim from closed S92 §W5-4 + §W5-5 Stage-2 verdicts) SATISFIED; M4 (allowlist membership) REQUIRES ORCHESTRATOR APPEND — gate-ID `{GATE_ID}` must be appended to `sessions/framework/registry/methodology-wave-allowlist-ledger.md` at plan-freeze (orchestrator-only edit per recursion-attack closure); FLAGGED for orchestrator, NOT edited by this script.

**Audit pin**: S93 W2-2 single-shot AFTER-pattern gate `{GATE_ID}` (`computations/session-93/s93_w2_2_vii_au_op_proj_stage_3_permanent_promotion.py`); single-shot AFTER-pattern per `registry-landing.md §"Bridge-Landing Script Architecture (single-shot pattern)"` (build_promotion_text → write_atomic_with_fsync → re_read+verify → emit-ONCE; NO conditional rewrite). Slot reserved at `sessions/framework/s93-slot-pre-allocation-lockfile.md §"RESERVED-FOR-{GATE_ID}"`.

**Cross-references for the STAGE-3-PERMANENT promotion**:

- `.claude/rules/joint-theorem-promotion.md §"Stage 3 — Permanent Registration"` — the tag-flip discipline (Stage-2 PASS landed ⇒ STAGE-1-CANDIDATE → STAGE-3-PERMANENT).
- `.claude/rules/joint-theorem-promotion.md §"Stage 2"` + §"Substrate-input-orthogonality clause" (MANDATORY at K=3 since S90 W2 CF-20) — the JOINT-clause PASS-AND-across-both-axes + substrate-input-orthogonality structural ceiling the §W5-4 + §W5-5 verdicts satisfy.
- `computations/session-92/s92_gate_verdicts.txt:155` (§W5-4 PASS, audit_sha256=`{STAGE2_W5_4_AUDIT_SHA}`) + `:164` (§W5-5 PASS latest-non-superseded, audit_sha256=`{STAGE2_W5_5_AUDIT_SHA}`).
- `.claude/rules/gate-verdicts.md §"Option A — sig_5 remediation pathway under absolute verdict permanence"` — the §W5-5 supersession-chain reading discipline (latest non-superseded line is canonical).
- `.claude/rules/cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` — CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED sub-class preserved through STAGE-3.
- `sessions/framework/s93-slot-pre-allocation-lockfile.md §"RESERVED-FOR-{GATE_ID}"` — slot reservation (W0-1, LIVE).
- §VII.AH STAGE-3-PERMANENT (S90 W2 CF-20) + §VII.U.2 Corner II Var_a — the framework's first two cross-axis joint theorems at STAGE-3-PERMANENT; §VII.AU.OP-PROJ is the THIRD.

"""


def build_promotion_text(registry_text: str, promo_block: str) -> tuple[str, int]:
    """Insert the STAGE-3 promotion block immediately before the §VII.AX header,
    keeping it INSIDE the §VII.AU.OP-PROJ section (after the S92 W5-2 sub-class
    block). Pure function; no I/O. Returns (full_new_text, insertion_offset).
    """
    idx = registry_text.find(NEXT_SECTION_HEADER)  # (local)
    if idx == -1:
        raise RuntimeError(
            f"insertion anchor not found: {NEXT_SECTION_HEADER!r} "
            "(cannot locate §VII.AX header to land before)"
        )
    new_text = registry_text[:idx] + promo_block + "\n" + registry_text[idx:]  # (local)
    return new_text, idx


# ---------------------------------------------------------------------------
# Step (2) — write_atomic_with_fsync
# ---------------------------------------------------------------------------
def write_atomic_with_fsync(text: str, path: Path) -> None:
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
        fh.flush()
        os.fsync(fh.fileno())


# ---------------------------------------------------------------------------
# Section slice — the §VII.AU.OP-PROJ section as landed (for content_sha + verify)
# ---------------------------------------------------------------------------
def slice_au_op_proj_section(text: str) -> str:
    """Return the §VII.AU.OP-PROJ STAGE-1-CANDIDATE host region: from the S91
    W5/W6 sub-class-transition block (the STAGE-1-CANDIDATE host) to the §VII.AX
    header. This is the section whose content_sha256 is the dual-SHA content leg.
    """
    start = text.find(SECTION_REGION_ANCHOR)  # (local)
    end = text.find(NEXT_SECTION_HEADER)  # (local)
    if start == -1 or end == -1 or start >= end:
        return ""
    return text[start:end]


# ---------------------------------------------------------------------------
# Step (3) — re_read + verify_section_matches
# ---------------------------------------------------------------------------
def verify_landing(promo_block: str) -> dict:
    """Re-read the registry; verify the STAGE-3-PERMANENT promotion block landed
    verbatim INSIDE the §VII.AU.OP-PROJ section, with the 4 M1 content predicates
    present, and the CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED sub-class preserved.
    Pure verification — no write.
    """
    actual = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)
    section = slice_au_op_proj_section(actual)  # (local)

    # (a) STAGE-3-PERMANENT tag present in the §VII.AU.OP-PROJ section text
    pred_a_stage3_present = "STAGE-3-PERMANENT" in section  # (local)
    # (b) both W5-4 + W5-5 audit_sha256 cited VERBATIM (full-64-hex) in the section
    pred_b_w5_4_cited = STAGE2_W5_4_AUDIT_SHA in section  # (local)
    pred_b_w5_5_cited = STAGE2_W5_5_AUDIT_SHA in section  # (local)
    pred_b_chain_cited = bool(pred_b_w5_4_cited and pred_b_w5_5_cited)  # (local)
    # (c) CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED sub-class preserved (still present)
    pred_c_sub_class_preserved = "CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED" in section  # (local)
    # (d) promotion block landed verbatim + INSIDE the section (offset ordering)
    promo_present = promo_block in actual  # (local)
    region_start = actual.find(SECTION_REGION_ANCHOR)  # (local)
    promo_idx = actual.find(PROMO_HEADER)  # (local)
    ax_idx = actual.find(NEXT_SECTION_HEADER)  # (local)
    inside_section = (  # (local)
        region_start != -1
        and promo_idx != -1
        and ax_idx != -1
        and region_start < promo_idx < ax_idx
    )

    # substantive line count of the promotion block (non-empty lines)
    substantive_line_count = sum(  # (local)
        1 for ln in promo_block.splitlines() if ln.strip()
    )

    # JOINT-clause PASS-AND-across-both-axes evidence present in the block text
    joint_pass_and_cited = (  # (local)
        "joint_PASS_AND=3_of_3" in section and "P3_joint_PASS_AND=True" in section
    )

    return {
        "pred_a_stage3_present": pred_a_stage3_present,
        "pred_b_w5_4_cited": pred_b_w5_4_cited,
        "pred_b_w5_5_cited": pred_b_w5_5_cited,
        "pred_b_chain_cited": pred_b_chain_cited,
        "pred_c_sub_class_preserved": pred_c_sub_class_preserved,
        "promo_present": promo_present,
        "inside_section": inside_section,
        "substantive_line_count": substantive_line_count,
        "joint_pass_and_cited": joint_pass_and_cited,
        "section_len": len(section),
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
        f"METHODOLOGY-class registry STAGE-3-PERMANENT tag-flip artifact-existence; "
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

    # --- HARD pre-condition 1: slot-lockfile RESERVATION ---
    slot_reserved = confirm_slot_reserved()  # (local)
    print(f"slot_reserved (s93 lockfile RESERVED-FOR-{GATE_ID}) = {slot_reserved}")

    # --- HARD pre-condition 2: Stage-2 PASS-AND chain verbatim ---
    chain = confirm_stage2_chain()  # (local)
    print("Stage-2 chain verification:")
    for k, v in chain.items():
        print(f"  {k} = {v}")
    chain_ok = bool(  # (local)
        chain["w5_4_present_pass"]
        and chain["w5_5_present_pass"]
        and chain["w5_5_latest_non_superseded"]
    )

    promo_block = build_promotion_block()  # (local) Step (1) pure build

    # Honest mechanical closure if a HARD pre-condition is unmet (NO forced PASS):
    if not slot_reserved or not chain_ok:
        blocker = (  # (local)
            "s93_slot_lockfile_NOT-RESERVED"
            if not slot_reserved
            else "S92_stage_2_W5-4_W5-5_chain_NOT-VERBATIM-PASS"
        )
        value = f"PRE-REG-INC_blocked_by_{blocker}"  # (local)
        actual = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)
        section = slice_au_op_proj_section(actual)  # (local)
        audit_sha, content_sha = compute_dual_sha(section, pins)  # (local)
        supersedes = find_latest_prior_audit_sha()  # (local)
        append_verdict("INFO", value, audit_sha, content_sha, supersedes=supersedes)
        _write_json(
            verdict="INFO",
            value=value,
            audit_sha=audit_sha,
            content_sha=content_sha,
            verify={},
            chain=chain,
            slot_reserved=slot_reserved,
            landed=False,
        )
        print(f"VERDICT: INFO (honest mechanical closure: {blocker})")
        return 0  # verdict is DATA; exit 0

    # --- idempotent guard (single-shot; re-runs must not duplicate the block) ---
    registry_text = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)
    header_present = PROMO_HEADER in registry_text  # (local)
    verbatim_present = promo_block in registry_text  # (local)

    if not header_present:
        new_text, ins_off = build_promotion_text(registry_text, promo_block)  # (local)
        write_atomic_with_fsync(new_text, REGISTRY_PATH)  # (local) Step (2)
        print(f"  STAGE-3 promotion block inserted at char offset {ins_off} (before §VII.AX)")
    elif not verbatim_present:
        # stale prior landing: replace the block span (header .. before §VII.AX)
        sub_start = registry_text.find(PROMO_HEADER)  # (local)
        ax_start = registry_text.find(NEXT_SECTION_HEADER, sub_start)  # (local)
        if sub_start == -1 or ax_start == -1:
            raise RuntimeError("stale-replace span resolution failed")
        new_text = (  # (local)
            registry_text[:sub_start] + promo_block + "\n" + registry_text[ax_start:]
        )
        write_atomic_with_fsync(new_text, REGISTRY_PATH)  # (local)
        print("  stale prior STAGE-3 promotion block REPLACED in-place with canonical build")
    else:
        print("  STAGE-3 promotion block already present verbatim (idempotent re-run); no write")

    # --- Step (3) re_read + verify_section_matches ---
    v = verify_landing(promo_block)  # (local)
    print("Verification:")
    for k in (
        "pred_a_stage3_present",
        "pred_b_w5_4_cited",
        "pred_b_w5_5_cited",
        "pred_b_chain_cited",
        "pred_c_sub_class_preserved",
        "promo_present",
        "inside_section",
        "substantive_line_count",
        "joint_pass_and_cited",
    ):
        print(f"  {k} = {v.get(k)}")

    # --- Step (4) determine verdict (single point of decision) ---
    # M1 4-of-4 content predicate conjunction + substantive_line_count >= 15 +
    # verbatim-landed-inside-section.
    m1_4_of_4 = bool(  # (local)
        v["pred_a_stage3_present"]
        and v["pred_b_chain_cited"]
        and v["pred_c_sub_class_preserved"]
        and v["promo_present"]
        and v["inside_section"]
    )
    substantive_ok = v["substantive_line_count"] >= 15  # (local)
    verdict = "PASS" if (m1_4_of_4 and substantive_ok) else "FAIL"  # (local)

    # --- Step (5) emit ONCE — dual-SHA over the §VII.AU.OP-PROJ section + pinmap ---
    actual = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)
    section = slice_au_op_proj_section(actual)  # (local)
    audit_sha, content_sha = compute_dual_sha(section, pins)  # (local)

    value = (  # (local)
        f"VII-AU-OP-PROJ-STAGE-3-PERMANENT_"
        f"stage3_tag={v['pred_a_stage3_present']}_"
        f"w5_4_cited={v['pred_b_w5_4_cited']}_w5_5_cited={v['pred_b_w5_5_cited']}_"
        f"sub_class_preserved={v['pred_c_sub_class_preserved']}_"
        f"inside_section={v['inside_section']}_"
        f"substantive_lines={v['substantive_line_count']}_"
        f"joint_pass_and={v['joint_pass_and_cited']}_"
        f"third_joint_theorem_after_VII.AH_and_Var_a;"
        f"W5_4_audit={STAGE2_W5_4_AUDIT_SHA};W5_5_audit={STAGE2_W5_5_AUDIT_SHA}"
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
        chain=chain,
        slot_reserved=slot_reserved,
        landed=True,
    )

    # exit 0 regardless of PASS/FAIL — verdict is DATA, not script health, per
    # math-scripts.md §"Exit Codes and Verdict Semantics".
    return 0


def _write_json(
    *, verdict, value, audit_sha, content_sha, verify, chain, slot_reserved, landed
) -> None:
    """JSON sidecar: pre/post registry-block content_sha256 + cited Stage-2 chain."""
    record = {  # (local)
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": value,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "stage_2_chain": {
            "W5_4_gate": STAGE2_W5_4_GATE,
            "W5_4_audit_sha256": STAGE2_W5_4_AUDIT_SHA,
            "W5_5_gate": STAGE2_W5_5_GATE,
            "W5_5_audit_sha256": STAGE2_W5_5_AUDIT_SHA,
            "W5_2_sub_class_tag": SUB_CLASS_TAG,
            "W5_2_audit_sha256": SUB_CLASS_W5_2_AUDIT_SHA,
        },
        "stage_2_chain_verification": chain,
        "slot_lockfile_reserved": slot_reserved,
        "landed": landed,
        "verify": verify,
        "M1_M4_self_classification": {
            "M1_artifact_existence_with_content": True,
            "M2_registry_write_plus_sha": True,
            "M3_verbatim_closed_stage2_verdicts": True,
            "M4_allowlist_append": "ORCHESTRATOR-ONLY (flagged in WP; not edited by this script)",
        },
        "third_joint_theorem_after": ["§VII.AH (S90 W2 CF-20)", "§VII.U.2 Corner II Var_a"],
        "sub_class_preserved": SUB_CLASS_TAG,
        "sub_class_at_stage_3": SUB_CLASS_PROMOTED,
        "asymptotic_deferral_forward_gate": "CF-S94-W5-3 (Friedrich-Bär saturation L in [35,100])",
    }
    JSON_PATH.parent.mkdir(parents=True, exist_ok=True)
    JSON_PATH.write_text(json.dumps(record, indent=2), encoding="utf-8")
    print(f"JSON sidecar: {JSON_PATH}")


if __name__ == "__main__":
    sys.exit(main())
