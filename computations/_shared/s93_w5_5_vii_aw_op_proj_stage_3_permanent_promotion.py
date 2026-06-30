#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S93-W5-5-VII-AW-OP-PROJ-STAGE-3-PERMANENT-PROMOTION
===================================================

Gate: S93-W5-5-VII-AW-OP-PROJ-STAGE-3-PERMANENT-PROMOTION  [VERIFY-THEOREM]
Classification: NON-PHONONIC (METHODOLOGY-class registry-write; PASS predicate is
                artifact-existence-with-substantive-content, not a numerical comparison).
Owner: mack-cosmic-bridge (sole registry writer per `feedback_mack-bridge-role.md`).
Tier: Tier-3 (STAGE-3-PERMANENT promotion; gated on the Stage-2 PASS-AND chain +
      substrate-input-orthogonality structural ceiling).
Plan: sessions/session-plan/session-93-plan-w5.md §W5-5.

═══════════════════════════════════════════════════════════════════════════
WHAT THIS GATE DOES (the already-done-S92-flip CONSEQUENCE handling)
═══════════════════════════════════════════════════════════════════════════

The §VII.AW.OP-PROJ SUBSTRATE-CLOCK-UNIQUENESS-THEOREM (heading registry ~line
18367; Status ~line 18375; resolve at runtime by CONTENT per
`substrate-first-canonical-sourcing.md §(ii.B)` plan-text-drift correction — the
plan-pinned ~18213-18289 / ~18365-18373 are STALE-drifted) was promoted to
STAGE-3-PERMANENT IN-SESSION at S92 (dated 2026-05-24), an in-session promotion
that `session-92-plan-w4.md §W4-5` PASS_meaning scheduled but dropped and then
effected per `CLAUDE.md §"No Technical Debt"` + `feedback_fix-in-session-never-defer.md`.

The plan §W5-5 method addresses the CONSEQUENCE of this already-done flip via an
explicit verify-vs-flip branch:

  (a) IF the body Status ALREADY reads STAGE-3-PERMANENT with the Stage-2 PASS-AND
      chain cited (§W4-5 Axis-B 4bd3017e... supersedes S91 W2 Axis-B INFO + S91 W2
      Axis-A hawking 69df5fa7...) AND the Cell-I + 5-anatomy + 3-level + parse-tree
      invariance preserved: this gate is a VERIFICATION-only confirmation
      (PASS = tag + chain present and well-formed; NO duplicate flip, NO rewrite of
      the already-correct Status block).
  (b) IF still STAGE-1-CANDIDATE: execute the single-shot AFTER-pattern tag-flip.

This gate runs branch (a): the on-disk state is verified, the STAGE-3 promotion is
RECORDED in the s93 slot-pre-allocation lockfile (per W0-1), and a confirmation
PASS is emitted. NO re-flip of an already-flipped status; NO forced PASS. A
verification MISS (tag absent, chain mis-cited, or invariance broken) emits FAIL
once per `registry-landing.md §"Bridge-Landing Script Architecture"` (verify-FAIL
emits FAIL once; no corrective rewrite in-script).

═══════════════════════════════════════════════════════════════════════════
AU/AW ORDINAL CHRONOLOGY (recorded, NOT unilaterally renumbered)
═══════════════════════════════════════════════════════════════════════════

§VII.AW.OP-PROJ (SUBSTRATE-CLOCK-UNIQUENESS) reached STAGE-3-PERMANENT in S92
(2026-05-24), CHRONOLOGICALLY BEFORE §VII.AU.OP-PROJ's S93 W2-2 promotion. Both
entries currently claim a "THIRD STAGE-3-PERMANENT" ordinal — an unresolved AU/AW
'#3' bookkeeping collision. The S92-before-S93 chronology suggests §VII.AW is the
EARLIER STAGE-3 promotion. This gate RECORDS the chronological fact but does NOT
unilaterally re-number all entries; the full ordinal-renumbering is left to the
session-end resolution `CF-S94-STAGE-3-ORDINAL-COLLISION-AU-AW` (exactly the
discipline the W5-2 sibling adopted: STAGE-3-PERMANENT set MEMBERSHIP recorded
WITHOUT asserting a contested integer).

═══════════════════════════════════════════════════════════════════════════
NON-PHONONIC (METHODOLOGY-class) — substrate framing
═══════════════════════════════════════════════════════════════════════════

The §VII.AW.OP-PROJ SUBSTRATE-CLOCK-UNIQUENESS-THEOREM is a Cell I algebra-INVARIANT
spectrum-only-functional cross-pillar bridge: the substrate-clock Pinning-A (an
∫_λ g(λ) dN_{D_K}(λ) functional on D_K's Peter-Weyl decomposition at τ_fold) IS the
unique substrate-natural temporal coordinate modulo affine reparameterization,
bridged to the laboratory-IN FRW cosmological-time observable. The tag-flip is the
methodology-floor F-image (per `epistemic-discipline.md §"Layer-Decomposition"`) of
the substrate's completed 4-stage promotion; this gate records that the
cross-axis joint identity has reached permanent status.

M1-M4 self-classification (wave-classification.md):
  M1 (artifact-existence-with-content) = True (STAGE-3-PERMANENT tag + Stage-2 chain
      cited + invariance preserved + lockfile row).
  M2 (registry-write + SHA cross-check, no numerical compute) = True.
  M3 (verbatim closed Stage-2 verdicts: S91 W2 Axis-A + S92 W4 Axis-B) = True.
  M4 (allowlist append) = ORCHESTRATOR-ONLY (flagged in WP; NOT edited by this script).

Single-shot AFTER pattern (registry-landing.md): the ONLY registry-class write is
the lockfile-updates row append (append-only, single open("a")); the registry
body Status is VERIFIED (re-read) NOT rewritten under branch (a).

Verdict file: computations/session-93/s93_gate_verdicts.txt
"""

from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "8")  # (local) CPU-only (registry text re-read + SHA cross-check; no compute)
os.environ.setdefault("MKL_NUM_THREADS", "8")  # (local)

import hashlib  # noqa: E402
import json  # noqa: E402
import re  # noqa: E402
import sys  # noqa: E402
from pathlib import Path  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent.parent  # (local)
sys.path.insert(0, str(ROOT / "computations" / "_shared"))

# Per computations/_shared/CLAUDE.md ALL scripts MUST import canonical_constants
# (even METHODOLOGY-class; no physics constants are CONSUMED here, but the import
# is mandatory + the spawn prompt requires the literal `from canonical_constants import`).
from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import M_KK, tau_fold  # noqa: E402 (metadata only; not gate-load-bearing)

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Gate identity + canonical paths
# ---------------------------------------------------------------------------
GATE_ID = "S93-W5-5-VII-AW-OP-PROJ-STAGE-3-PERMANENT-PROMOTION"  # (local)
SCHEME = "registry-text-METHODOLOGY-class"  # (local) per plan §W5-5 machinery_pin_map.scheme
CONVENTION = "VII-AW-OP-PROJ-SUBSTRATE-CLOCK-STAGE-3-PERMANENT-tag-flip-THIRD"  # (local) per plan §W5-5 machinery_pin_map.convention
L_MAX = "N/A"  # (local) METHODOLOGY-class registry-text edit; no L_max
SCHEMA_VERSION = "S84+"  # (local)

SESSION_DIR = ROOT / "computations" / "session-93"  # (local)
OUT_NPZ = SESSION_DIR / "s93_w5_5_vii_aw_op_proj_stage_3_permanent_promotion.npz"  # (local)
OUT_PNG = SESSION_DIR / "s93_w5_5_vii_aw_op_proj_stage_3_permanent_promotion.png"  # (local)
OUT_JSON = SESSION_DIR / "s93_w5_5_vii_aw_op_proj_stage_3_permanent_promotion.json"  # (local)
VERDICT_FILE = SESSION_DIR / "s93_gate_verdicts.txt"  # (local)

CANONICAL_CONSTANTS = ROOT / "computations" / "_shared" / "canonical_constants.py"  # (local)
REGISTRY = ROOT / "sessions" / "permanent-results-registry.md"  # (local)
S91_VERDICTS = ROOT / "computations" / "session-91" / "s91_gate_verdicts.txt"  # (local) Axis-A
S92_VERDICTS = ROOT / "computations" / "session-92" / "s92_gate_verdicts.txt"  # (local) Axis-B
# Plan §W5-5 input_files pins s90-slot-pre-allocation-lockfile.md (STALE plan-frozen ref).
# Per substrate-first-canonical-sourcing.md §(ii.B) plan-text-drift correction + the s93
# lockfile's OWN W0-1 provenance (it pre-allocates the 7 S93 STAGE-3 flips INCLUDING W5-5
# explicitly, RESERVED-FOR-S93-W5-5-...), the CANONICAL W0-1 home is s93-...lockfile.md.
SLOT_LOCKFILE = ROOT / "sessions" / "framework" / "s93-slot-pre-allocation-lockfile.md"  # (local) drift-corrected
SLOT_LOCKFILE_PLAN_PINNED = ROOT / "sessions" / "framework" / "s90-slot-pre-allocation-lockfile.md"  # (local) plan-pinned (stale; documented)
SCRIPT_PATH = Path(__file__).resolve()  # (local)

# ---------------------------------------------------------------------------
# The Stage-2 PASS-AND chain (verbatim full-64-hex audit_sha256; per plan §W5-5).
# ---------------------------------------------------------------------------
# Axis-A: S91 W2 hawking-theorist PASS, clauses (a,c,e). Plan-pinned 69df5fa7...
AXIS_A_GATE = "S91-W2-VII-AW-OP-PROJ-STAGE-2-CROSS-AXIS-INDEPENDENT-VERIFY-AXIS-A"  # (local)
AXIS_A_PASS_AUDIT_SHA = "69df5fa7e23fa08fd038a629f6822d0e839a5566dd76ad6cf34246ce89a7831f"  # (local)
# Axis-B: S92 W4 mack INFO->PASS re-dispatch, clauses (b,d,f); supersedes S91 W2 Axis-B INFO. Plan-pinned 4bd3017e...
AXIS_B_GATE = "S92-W4-CF-S92-W4-3-RE-DISPATCH-VII-AW-OP-PROJ-STAGE-2-AXIS-B"  # (local)
AXIS_B_PASS_AUDIT_SHA = "4bd3017ed24e1570573ee55df1528020632a7fd348d5f24de7fd00a7f8ccae7c"  # (local)
AXIS_B_SUPERSEDED_INFO_SHA = "0db7c3c01e6959b945a3f623815929edf2e7fd709816e82dfc4f6b381375d914"  # (local) S91 W2 Axis-B INFO
# Substrate derivation provenance (S89 W3-6 5/5 saturation closeout).
S89_W3_6_AUDIT_SHA = "6108fd56a3b62e2ea8d735efd5117bd00d7503f99b18d0198222e0c7244784ad"  # (local)

# ---------------------------------------------------------------------------
# Registry CONTENT-anchored verification markers (resolve by CONTENT, not line).
# These are EXACT substrings that MUST be present on-disk for branch (a) PASS.
# ---------------------------------------------------------------------------
HDR_MARKER = (  # (local) the body section heading (content-anchored, NOT line-pinned)
    "### §VII.AW.OP-PROJ — SUBSTRATE-CLOCK-UNIQUENESS-THEOREM"
)
STATUS_STAGE3_MARKER = (  # (local) the body Status block STAGE-3-PERMANENT marker
    "**Status**: STAGE-3-PERMANENT (promoted from STAGE-1-CANDIDATE 2026-05-24 per "
    "`.claude/rules/joint-theorem-promotion.md §\"Stage 3\"` 4-stage pathway"
)
IDX_STAGE3_MARKER = (  # (local) the index-table row (registry ~line 133) STAGE-3-PERMANENT marker
    "| §VII.AW.OP-PROJ | THM **[STAGE-3-PERMANENT 2026-05-24 — Stage-2 PASS-AND complete; "
    "promoted per joint-theorem-promotion.md §\"Stage 3\"]**"
)
# Invariance markers (Cell I + 5-anatomy + 3-level + parse-tree-relevant structure).
CELL_I_MARKER = "Cell I (algebra-INVARIANT spectrum-only-functional × Mellin-pole substrate-distance-1 at s=3)"  # (local)
FIVE_ANATOMY_MARKER = "**5-anatomy IS-not-IN elements** (all MANDATORY at K=3 per `cross-pillar-bridge-anatomy.md`)"  # (local)
THREE_LEVEL_MARKER = "**Three-level structural-confidence ladder**"  # (local)
SATURATION_TABLE_MARKER = "**5-criteria saturation evidence table**"  # (local) parse-tree-relevant substrate-clock functional ∫_λ g(λ) dN_{D_K}(λ)
THEOREM_STMT_MARKER = "the substrate-clock canonical Pinning-A IS the UNIQUE substrate-natural temporal coordinate"  # (local)
JOINT_CLAUSE_MARKER = "JOINT clauses (a)+(c)+(e) PASS-AND'd across both verdicts"  # (local)
SUBSTRATE_INPUT_ORTHO_MARKER = "Substrate-input-orthogonality at structural ceiling PASS (cache-axis ∧ registry-text-axis)"  # (local)


# ---------------------------------------------------------------------------
# SHA helpers
# ---------------------------------------------------------------------------
def sha256_of_file(p: Path) -> str:
    try:
        return hashlib.sha256(p.read_bytes()).hexdigest()
    except OSError:
        return "0" * 64


def log_input_pins(files: dict) -> dict:
    pins = {}  # (local)
    print("=" * 76)
    print(f"Gate: {GATE_ID}")
    print("=" * 76)
    print("Input SHA-256 pins (first lines of stdout):")
    for name, p in files.items():
        sha = sha256_of_file(p)  # (local)
        pins[name] = sha
        rel = str(p.relative_to(ROOT)).replace("\\", "/") if p.exists() else str(p)
        print(f"  {name:30s} = {sha[:16]}...  ({rel})")
    return pins


def extract_aw_substrate_clock_block(registry_text: str) -> str:
    """Extract the §VII.AW.OP-PROJ SUBSTRATE-CLOCK entry block (from its heading to
    the next `### §VII.` heading) for the content_sha256 leg. Content-anchored, NOT
    line-pinned (drift-robust). Returns '' if the heading is absent.
    """
    start = registry_text.find(HDR_MARKER)  # (local)
    if start < 0:
        return ""
    rest = registry_text[start + len(HDR_MARKER):]  # (local)
    nxt = rest.find("\n### §VII.")  # (local) next §VII heading
    block = HDR_MARKER + (rest if nxt < 0 else rest[:nxt])  # (local)
    return block


def compute_dual_sha(pins: dict, block_text: str) -> tuple[str, str]:
    """Dual-SHA. content_sha256 = SHA over the VERIFIED (re-read) §VII.AW
    SUBSTRATE-CLOCK entry block (the artifact whose existence-with-content IS the
    METHODOLOGY-class PASS predicate). audit_sha256 = SHA over the input-pin map +
    the Stage-2 chain SHAs + per-gate identity keys (gate-distinct per
    mechanical-closure-discipline.md item 3).
    """
    h_content = hashlib.sha256()  # (local)
    h_content.update(block_text.encode("utf-8"))
    content = h_content.hexdigest()  # (local)

    pinmap_json = json.dumps(dict(sorted(pins.items())), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(pinmap_json)
    h_audit.update(
        f"{AXIS_A_PASS_AUDIT_SHA}|{AXIS_B_PASS_AUDIT_SHA}|{AXIS_B_SUPERSEDED_INFO_SHA}|"
        f"{S89_W3_6_AUDIT_SHA}".encode("utf-8")
    )
    h_audit.update(f"{GATE_ID}|{SCHEME}|{CONVENTION}|L_max={L_MAX}".encode("utf-8"))
    audit = h_audit.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# VERIFY pre-condition 1 — body Status + index row ALREADY STAGE-3-PERMANENT
# (branch (a) detection; resolved by CONTENT per drift correction)
# ---------------------------------------------------------------------------
def verify_stage3_on_disk(registry_text: str) -> dict:
    out = {  # (local)
        "hdr_present": HDR_MARKER in registry_text,
        "status_stage3_present": STATUS_STAGE3_MARKER in registry_text,
        "idx_stage3_present": IDX_STAGE3_MARKER in registry_text,
        # invariance preservation (Cell I + 5-anatomy + 3-level + theorem + saturation table)
        "cell_i_present": CELL_I_MARKER in registry_text,
        "five_anatomy_present": FIVE_ANATOMY_MARKER in registry_text,
        "three_level_present": THREE_LEVEL_MARKER in registry_text,
        "saturation_table_present": SATURATION_TABLE_MARKER in registry_text,
        "theorem_stmt_present": THEOREM_STMT_MARKER in registry_text,
        # Stage-2 PASS-AND chain cited in the body Status block
        "axis_a_sha_in_body": AXIS_A_PASS_AUDIT_SHA in registry_text,
        "axis_b_sha_in_body": AXIS_B_PASS_AUDIT_SHA in registry_text,
        "axis_b_supersedes_info_in_body": AXIS_B_SUPERSEDED_INFO_SHA in registry_text,
        "joint_clause_in_body": JOINT_CLAUSE_MARKER in registry_text,
        "substrate_input_ortho_in_body": SUBSTRATE_INPUT_ORTHO_MARKER in registry_text,
    }
    return out


# ---------------------------------------------------------------------------
# VERIFY pre-condition 2 — Stage-2 chain verbatim in the SOURCE verdict files
# ---------------------------------------------------------------------------
def verify_stage2_chain_source() -> dict:
    out = {  # (local)
        "axis_a_pass_in_s91": False,
        "axis_b_pass_in_s92": False,
    }
    if S91_VERDICTS.exists():
        for ln in S91_VERDICTS.read_text(encoding="utf-8").splitlines():
            if ln.startswith(f"{AXIS_A_GATE}:") and " PASS " in ln and f"audit_sha256={AXIS_A_PASS_AUDIT_SHA}" in ln:
                out["axis_a_pass_in_s91"] = True
    if S92_VERDICTS.exists():
        for ln in S92_VERDICTS.read_text(encoding="utf-8").splitlines():
            if ln.startswith(f"{AXIS_B_GATE}:") and " PASS " in ln and f"audit_sha256={AXIS_B_PASS_AUDIT_SHA}" in ln:
                out["axis_b_pass_in_s92"] = True
    return out


# ---------------------------------------------------------------------------
# VERIFY pre-condition 3 — slot RESERVED in the s93 lockfile (W0-1 home)
# ---------------------------------------------------------------------------
def verify_slot_reserved() -> dict:
    out = {  # (local)
        "s93_lockfile_present": SLOT_LOCKFILE.exists(),
        "reserved_block_present": False,
        "reserved_row_present": False,
    }
    if not SLOT_LOCKFILE.exists():
        return out
    txt = SLOT_LOCKFILE.read_text(encoding="utf-8")  # (local)
    out["reserved_block_present"] = bool(
        f"RESERVED-FOR-{GATE_ID}" in txt and "§VII.AW.OP-PROJ" in txt
    )
    # The Lockfile-updates table row marking the slot RESERVED (initial allocation).
    out["reserved_row_present"] = bool(
        re.search(r"\|\s*§VII\.AW\.OP-PROJ\s*\|\s*RESERVED\s*\|", txt)
    )
    return out


# ---------------------------------------------------------------------------
# RECORD the STAGE-3 promotion in the s93 lockfile (W0-1). Append-only single
# open("a") row to the "Lockfile updates" table (mack sole writer). This is the
# ONLY registry-class write in branch (a) — NO re-flip of the already-correct
# registry body Status.
# ---------------------------------------------------------------------------
LOCKFILE_CONFIRM_ROW = (  # (local)
    "| 2026-05-24 | S93 W5-5 STAGE-3-PERMANENT CONFIRMED on-disk "
    "(branch (a) verification-only; S92 in-session promotion verified, NO duplicate flip); "
    "AU/AW '#3' ordinal collision recorded NOT renumbered -> CF-S94-STAGE-3-ORDINAL-COLLISION-AU-AW | "
    "§VII.AW.OP-PROJ | STAGE-3-PERMANENT-CONFIRMED |\n"
)
LOCKFILE_CONFIRM_MARKER = (  # (local) idempotency guard
    "S93 W5-5 STAGE-3-PERMANENT CONFIRMED on-disk"
)


def record_lockfile_promotion() -> dict:
    """Append the STAGE-3-PERMANENT-CONFIRMED row to the s93 lockfile updates table.
    Idempotent: skip if the confirm marker is already present. Append-only (single
    open("a")); the row goes at end-of-file after the existing table rows.
    """
    out = {"lockfile_row_appended": False, "lockfile_row_idempotent_skip": False}  # (local)
    if not SLOT_LOCKFILE.exists():
        return out
    txt = SLOT_LOCKFILE.read_text(encoding="utf-8")  # (local)
    if LOCKFILE_CONFIRM_MARKER in txt:
        out["lockfile_row_idempotent_skip"] = True
        return out
    with SLOT_LOCKFILE.open("a", encoding="utf-8") as f:
        f.write(LOCKFILE_CONFIRM_ROW)
    out["lockfile_row_appended"] = True
    return out


# ---------------------------------------------------------------------------
# Option-A supersedes source (latest non-superseded prior line for this gate-ID)
# ---------------------------------------------------------------------------
def find_latest_prior_audit_sha() -> str | None:
    if not VERDICT_FILE.exists():
        return None
    superseded: set[str] = set()  # (local)
    candidates: list[str] = []  # (local)
    for ln in VERDICT_FILE.read_text(encoding="utf-8").splitlines():
        if ln.startswith(f"{GATE_ID}:") and "audit_sha256=" in ln:
            m = re.search(r"audit_sha256=([a-f0-9]{64})", ln)  # (local)
            if m:
                candidates.append(m.group(1))
            sm = re.search(r"supersedes=([a-f0-9]{64})", ln)  # (local)
            if sm:
                superseded.add(sm.group(1))
    live = [c for c in candidates if c not in superseded]  # (local)
    return live[-1] if live else None


def append_verdict(verdict: str, value_str: str, audit_sha: str, content_sha: str,
                   supersedes: str | None = None) -> None:
    """Single canonical dual-SHA verdict line + companion row. METHODOLOGY/registry
    verification-confirmation; [VERIFY-THEOREM] — no [SIGN] 3-tuple
    (schema_v2_3tuple_required: false).
    """
    value_field = value_str if supersedes is None else f"{value_str}_supersedes={supersedes}"  # (local)
    canonical = (  # (local)
        f"{GATE_ID}: {verdict} -- value='{value_field}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )
    supersedes_note = f"; supersedes={supersedes}" if supersedes else ""  # (local)
    companion = (  # (local)
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); METHODOLOGY-class "
        f"branch-(a) verification-confirmation of the S92 in-session STAGE-3-PERMANENT "
        f"promotion (NO duplicate flip); Stage-2 PASS-AND chain Axis-A 69df5fa7 + "
        f"Axis-B 4bd3017e (supersedes S91 W2 Axis-B INFO 0db7c3c0); AU/AW ordinal NOT "
        f"asserted -> CF-S94-STAGE-3-ORDINAL-COLLISION-AU-AW; [VERIFY-THEOREM] no [SIGN] "
        f"3-tuple{supersedes_note}\n"
    )
    with VERDICT_FILE.open("a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(companion)


def main() -> int:
    print(f"=== {GATE_ID} ===")
    input_files = {
        "canonical_constants": CANONICAL_CONSTANTS,
        "permanent_results_registry": REGISTRY,
        "s91_verdicts_axis_a": S91_VERDICTS,
        "s92_verdicts_axis_b": S92_VERDICTS,
        "s93_slot_lockfile": SLOT_LOCKFILE,
        "script": SCRIPT_PATH,
    }
    pins = log_input_pins(input_files)

    # ---- Drift-correction disclosure (plan-pinned lockfile is STALE) ----
    print("\n" + "=" * 76)
    print("Plan-text-drift correction (substrate-first-canonical-sourcing.md §(ii.B))")
    print("=" * 76)
    print(f"  plan §W5-5 input_files pins: {SLOT_LOCKFILE_PLAN_PINNED.name} (STALE plan-frozen)")
    print(f"  canonical W0-1 home (drift-corrected): {SLOT_LOCKFILE.name}")
    print(f"  s93 lockfile present = {SLOT_LOCKFILE.exists()}  (carries RESERVED-FOR-{GATE_ID[:24]}...)")
    print("  Registry line numbers resolved by CONTENT (heading-anchor), NOT plan-pinned ~18365/18373.")

    registry_text = REGISTRY.read_text(encoding="utf-8")  # (local)

    # ---- VERIFY pre-condition 1: body Status + index row STAGE-3-PERMANENT (branch (a)) ----
    print("\n" + "=" * 76)
    print("Pre-condition 1: §VII.AW.OP-PROJ SUBSTRATE-CLOCK body + index row STAGE-3-PERMANENT")
    print("=" * 76)
    v1 = verify_stage3_on_disk(registry_text)  # (local)
    for k, val in v1.items():
        print(f"  {k} = {val}")
    branch_a = bool(v1["status_stage3_present"] and v1["idx_stage3_present"])  # (local) ALREADY STAGE-3
    invariance_ok = bool(
        v1["hdr_present"]
        and v1["cell_i_present"]
        and v1["five_anatomy_present"]
        and v1["three_level_present"]
        and v1["saturation_table_present"]
        and v1["theorem_stmt_present"]
    )  # (local)
    chain_in_body_ok = bool(
        v1["axis_a_sha_in_body"]
        and v1["axis_b_sha_in_body"]
        and v1["axis_b_supersedes_info_in_body"]
        and v1["joint_clause_in_body"]
        and v1["substrate_input_ortho_in_body"]
    )  # (local)
    print(f"  >>> branch_a (ALREADY STAGE-3-PERMANENT, body + index) = {branch_a}")
    print(f"  >>> invariance preserved (Cell I + 5-anatomy + 3-level + theorem + saturation) = {invariance_ok}")
    print(f"  >>> Stage-2 PASS-AND chain cited in body Status = {chain_in_body_ok}")

    # ---- VERIFY pre-condition 2: Stage-2 chain verbatim in SOURCE verdict files ----
    print("\n" + "=" * 76)
    print("Pre-condition 2: Stage-2 PASS-AND chain verbatim in source verdict files")
    print("=" * 76)
    v2 = verify_stage2_chain_source()  # (local)
    for k, val in v2.items():
        print(f"  {k} = {val}")
    chain_source_ok = bool(v2["axis_a_pass_in_s91"] and v2["axis_b_pass_in_s92"])  # (local)
    print(f"  >>> Stage-2 chain verbatim in source (Axis-A S91 + Axis-B S92) = {chain_source_ok}")

    # ---- VERIFY pre-condition 3: slot RESERVED in s93 lockfile (W0-1) ----
    print("\n" + "=" * 76)
    print("Pre-condition 3: slot RESERVED in s93 lockfile (W0-1)")
    print("=" * 76)
    v3 = verify_slot_reserved()  # (local)
    for k, val in v3.items():
        print(f"  {k} = {val}")
    slot_reserved_ok = bool(v3["s93_lockfile_present"] and v3["reserved_block_present"])  # (local)
    print(f"  >>> slot RESERVED for {GATE_ID[:30]}... = {slot_reserved_ok}")

    # ---- RECORD the STAGE-3 promotion in the lockfile (W0-1; the only registry-class write) ----
    print("\n" + "=" * 76)
    print("Record STAGE-3 promotion in s93 lockfile updates table (W0-1; append-only)")
    print("=" * 76)
    lf = record_lockfile_promotion()  # (local)
    for k, val in lf.items():
        print(f"  {k} = {val}")
    lockfile_recorded_ok = bool(lf["lockfile_row_appended"] or lf["lockfile_row_idempotent_skip"])  # (local)
    # re-read to confirm the confirm marker is on-disk
    lockfile_confirm_on_disk = LOCKFILE_CONFIRM_MARKER in SLOT_LOCKFILE.read_text(encoding="utf-8")  # (local)
    print(f"  >>> lockfile STAGE-3 row recorded = {lockfile_recorded_ok}; confirm marker on-disk = {lockfile_confirm_on_disk}")

    # ---- AU/AW ordinal chronology (recorded, NOT renumbered) ----
    print("\n" + "=" * 76)
    print("AU/AW ordinal chronology (recorded, NOT unilaterally renumbered)")
    print("=" * 76)
    au_aw_collision_present = (  # (local) both AU and AW currently claim THIRD-position STAGE-3
        "§VII.AU.OP-PROJ" in registry_text
        and "STAGE-3 promotion S93 W2-2" in registry_text
    )
    print(f"  AW STAGE-3 promoted in S92 (2026-05-24); AU STAGE-3 promoted S93 W2-2 (2026-05-?)")
    print(f"  S92-before-S93 chronology => §VII.AW is the EARLIER STAGE-3 promotion (chronological fact)")
    print(f"  AU/AW '#3' collision detected on-disk = {au_aw_collision_present}")
    print(f"  RESOLUTION: recorded NOT renumbered; full ordinal-renumbering -> CF-S94-STAGE-3-ORDINAL-COLLISION-AU-AW")

    # ---- Single point of decision (METHODOLOGY-class artifact-existence predicate) ----
    aw_block = extract_aw_substrate_clock_block(registry_text)  # (local) content_sha leg
    substantive_ok = len(aw_block.split()) >= 15  # (local) token count of the entry block (hundreds of words)

    # branch (a) verification-confirmation PASS predicate:
    #   STAGE-3 already on-disk (body + index) AND invariance preserved AND chain cited
    #   in body AND chain verbatim in source AND slot reserved AND lockfile recorded.
    verify_pass = bool(
        branch_a
        and invariance_ok
        and chain_in_body_ok
        and chain_source_ok
        and slot_reserved_ok
        and lockfile_recorded_ok
        and lockfile_confirm_on_disk
        and substantive_ok
    )

    # If STAGE-3 is NOT already present (branch (b) would be needed) OR a chain/invariance
    # check fails, this is an honest FAIL — NOT a forced PASS and NOT an in-script re-flip.
    if branch_a and not verify_pass:
        verdict = "FAIL"  # (local) STAGE-3 present but chain/invariance/source/slot incomplete
    elif not branch_a:
        verdict = "FAIL"  # (local) NOT already STAGE-3; plan branch (b) flip is a SEPARATE pathway, not forced here
    else:
        verdict = "PASS"  # (local) branch (a) verification-confirmation

    print("\n" + "=" * 76)
    print(f"VERDICT decision: branch_a={branch_a}, verify_pass={verify_pass} -> {verdict}")
    print("=" * 76)

    # ---- value string ----
    value_str = (  # (local)
        f"VII-AW-OP-PROJ-SUBSTRATE-CLOCK-STAGE-3-PERMANENT_branch=a_verification_confirmation_"
        f"NO_duplicate_flip_already_STAGE-3_S92_2026-05-24_"
        f"body_status_stage3={v1['status_stage3_present']}_idx_row_stage3={v1['idx_stage3_present']}_"
        f"invariance_preserved={invariance_ok}_chain_in_body={chain_in_body_ok}_"
        f"chain_verbatim_source={chain_source_ok}_slot_reserved={slot_reserved_ok}_"
        f"lockfile_recorded={lockfile_recorded_ok}_"
        f"THIRD_STAGE-3_set_membership_recorded_ordinal_NOT_asserted_"
        f"AU_AW_collision_CF=CF-S94-STAGE-3-ORDINAL-COLLISION-AU-AW;"
        f"axis_A_audit={AXIS_A_PASS_AUDIT_SHA};axis_B_audit={AXIS_B_PASS_AUDIT_SHA};"
        f"axis_B_supersedes_INFO={AXIS_B_SUPERSEDED_INFO_SHA};"
        f"S89_W3_6_substrate_derivation={S89_W3_6_AUDIT_SHA};"
        f"lockfile_drift_corrected_to=s93-slot-pre-allocation-lockfile.md_"
        f"plan_pinned_stale=s90-slot-pre-allocation-lockfile.md"
    )

    audit_sha, content_sha = compute_dual_sha(pins, aw_block)  # (local) content leg = the verified entry block
    supersedes = find_latest_prior_audit_sha()  # (local) Option-A corrective tag (None on first emission)
    if supersedes:
        print(f"  prior verdict line detected; emitting corrective line with supersedes={supersedes[:16]}...")

    # ---- artifacts (npz + json + png) BEFORE verdict emission ----
    _emit_npz_and_json(v1, v2, v3, lf, aw_block, branch_a, invariance_ok, chain_in_body_ok,
                       chain_source_ok, slot_reserved_ok, lockfile_recorded_ok, substantive_ok,
                       au_aw_collision_present, verdict, value_str, audit_sha, content_sha)
    _emit_plot(v1, v2, v3, lf, branch_a, invariance_ok, chain_in_body_ok, chain_source_ok,
               slot_reserved_ok, lockfile_recorded_ok, verdict)

    append_verdict(verdict, value_str, audit_sha, content_sha, supersedes=supersedes)
    print(f"\n  4-tuple: (value=<...>, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"  audit_sha256={audit_sha}")
    print(f"  content_sha256={content_sha}")
    print(f"\n  >>> VERDICT: {verdict}")
    print(f"  §VII.AW.OP-PROJ SUBSTRATE-CLOCK ALREADY STAGE-3-PERMANENT (S92 in-session) = {branch_a}")
    print(f"  branch (a) verification-confirmation; NO duplicate flip; NO forced PASS.")
    print(f"  AU/AW ordinal recorded NOT renumbered -> CF-S94-STAGE-3-ORDINAL-COLLISION-AU-AW")
    print(f"  M4 allowlist append = ORCHESTRATOR-ONLY (flagged in WP §W5-5)")
    return 0  # verdict is DATA; exit 0 regardless of PASS/FAIL


def _emit_npz_and_json(v1, v2, v3, lf, aw_block, branch_a, invariance_ok, chain_in_body_ok,
                       chain_source_ok, slot_reserved_ok, lockfile_recorded_ok, substantive_ok,
                       au_aw_collision_present, verdict, value_str, audit_sha, content_sha):
    np.savez(
        OUT_NPZ,
        # branch (a) verification flags
        branch_a_already_stage3=np.bool_(branch_a),
        body_status_stage3_present=np.bool_(v1["status_stage3_present"]),
        idx_row_stage3_present=np.bool_(v1["idx_stage3_present"]),
        hdr_present=np.bool_(v1["hdr_present"]),
        # invariance preservation
        cell_i_present=np.bool_(v1["cell_i_present"]),
        five_anatomy_present=np.bool_(v1["five_anatomy_present"]),
        three_level_present=np.bool_(v1["three_level_present"]),
        saturation_table_present=np.bool_(v1["saturation_table_present"]),
        theorem_stmt_present=np.bool_(v1["theorem_stmt_present"]),
        invariance_preserved=np.bool_(invariance_ok),
        # Stage-2 chain cited in body + verbatim in source
        axis_a_sha_in_body=np.bool_(v1["axis_a_sha_in_body"]),
        axis_b_sha_in_body=np.bool_(v1["axis_b_sha_in_body"]),
        axis_b_supersedes_info_in_body=np.bool_(v1["axis_b_supersedes_info_in_body"]),
        joint_clause_in_body=np.bool_(v1["joint_clause_in_body"]),
        substrate_input_ortho_in_body=np.bool_(v1["substrate_input_ortho_in_body"]),
        chain_in_body_ok=np.bool_(chain_in_body_ok),
        axis_a_pass_in_s91=np.bool_(v2["axis_a_pass_in_s91"]),
        axis_b_pass_in_s92=np.bool_(v2["axis_b_pass_in_s92"]),
        chain_source_ok=np.bool_(chain_source_ok),
        # slot reservation + lockfile record
        s93_lockfile_present=np.bool_(v3["s93_lockfile_present"]),
        reserved_block_present=np.bool_(v3["reserved_block_present"]),
        reserved_row_present=np.bool_(v3["reserved_row_present"]),
        slot_reserved_ok=np.bool_(slot_reserved_ok),
        lockfile_row_appended=np.bool_(lf["lockfile_row_appended"]),
        lockfile_row_idempotent_skip=np.bool_(lf["lockfile_row_idempotent_skip"]),
        lockfile_recorded_ok=np.bool_(lockfile_recorded_ok),
        # AU/AW ordinal
        au_aw_collision_present=np.bool_(au_aw_collision_present),
        ordinal_assertion="NOT-ASSERTED (S92-before-S93: AW earlier; CF-S94-STAGE-3-ORDINAL-COLLISION-AU-AW)",
        # cited chain SHAs (full-64-hex)
        axis_a_pass_audit_sha=str(AXIS_A_PASS_AUDIT_SHA),
        axis_b_pass_audit_sha=str(AXIS_B_PASS_AUDIT_SHA),
        axis_b_superseded_info_sha=str(AXIS_B_SUPERSEDED_INFO_SHA),
        s89_w3_6_audit_sha=str(S89_W3_6_AUDIT_SHA),
        # content-leg measure
        aw_block_word_count=np.int64(len(aw_block.split())),
        substantive_ok=np.bool_(substantive_ok),
        # metadata
        L_max=str(L_MAX),
        tau_fold=np.float64(tau_fold),
        M_KK=np.float64(M_KK),
        verdict=str(verdict),
        scheme=SCHEME,
        convention=CONVENTION,
        gate_id=GATE_ID,
        audit_sha256=str(audit_sha),
        content_sha256=str(content_sha),
        lockfile_drift_corrected_to="s93-slot-pre-allocation-lockfile.md",
        lockfile_plan_pinned_stale="s90-slot-pre-allocation-lockfile.md",
        ordinal_collision_cf="CF-S94-STAGE-3-ORDINAL-COLLISION-AU-AW",
        m1_artifact_existence_with_content=np.bool_(True),
        m4_allowlist="ORCHESTRATOR-ONLY",
    )
    print(f"  NPZ -> {OUT_NPZ.relative_to(ROOT)}")
    _chk = np.load(OUT_NPZ, allow_pickle=True)  # (local)
    rt_ok = bool(_chk["branch_a_already_stage3"]) == branch_a  # (local)
    print(f"  round-trip: npz branch_a_already_stage3 preserved: {rt_ok}")

    record = {  # (local)
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": value_str,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "branch": "(a) verification-confirmation (target ALREADY STAGE-3-PERMANENT; S92 in-session promotion, 2026-05-24)",
        "no_duplicate_flip": True,
        "no_forced_pass": True,
        "verification": {
            "branch_a_already_stage3": branch_a,
            "invariance_preserved": invariance_ok,
            "chain_in_body_ok": chain_in_body_ok,
            "chain_source_ok": chain_source_ok,
            "slot_reserved_ok": slot_reserved_ok,
            "lockfile_recorded_ok": lockfile_recorded_ok,
            "substantive_ok": substantive_ok,
            "pre_condition_1_body_index": v1,
            "pre_condition_2_chain_source": v2,
            "pre_condition_3_slot": v3,
            "lockfile_record": lf,
        },
        "stage_2_chain": {
            "axis_A_pass_audit_sha256": AXIS_A_PASS_AUDIT_SHA,
            "axis_A_gate": AXIS_A_GATE,
            "axis_A_reviewer": "hawking-theorist",
            "axis_A_clauses": "(a,c,e)",
            "axis_B_pass_audit_sha256": AXIS_B_PASS_AUDIT_SHA,
            "axis_B_gate": AXIS_B_GATE,
            "axis_B_reviewer": "mack-cosmic-bridge (cosmological-bridge axis; INFO->PASS re-dispatch)",
            "axis_B_clauses": "(b,d,f)",
            "axis_B_supersedes_S91_W2_INFO": AXIS_B_SUPERSEDED_INFO_SHA,
            "joint_clauses_pass_and": "(a)+(c)+(e) PASS-AND'd across both verdicts",
            "substrate_input_orthogonality": "structural ceiling (cache-axis ∧ registry-text-axis); K=3->K=4 advance-eligible",
            "s89_w3_6_substrate_derivation_audit_sha256": S89_W3_6_AUDIT_SHA,
        },
        "ordinal_assertion": "NOT-ASSERTED (pre-existing AU/AW '#3' collision; AW chronologically EARLIER (S92) than AU (S93 W2-2); CF-S94-STAGE-3-ORDINAL-COLLISION-AU-AW)",
        "au_aw_chronology": {
            "aw_stage3_promoted": "S92 (2026-05-24)",
            "au_stage3_promoted": "S93 W2-2",
            "chronological_fact": "AW is the EARLIER STAGE-3 promotion (S92 before S93)",
            "action": "recorded NOT renumbered; full ordinal-renumbering deferred to CF-S94-STAGE-3-ORDINAL-COLLISION-AU-AW",
        },
        "stage_3_set_membership": [
            "§VII.AH (FIRST, S90 W2 CF-20)", "§VII.U.2 Corner-II Var_a (SECOND, S92 W4-7)",
            "§VII.AW.OP-PROJ (this; S92 in-session)", "§VII.AU.OP-PROJ (S93 W2-2)",
            "§VII.AV.STATE-PROJ (S93 W3-6)", "§VII.AX.OP-PROJ", "§VII.AY.OP-PROJ (S93 W5-2)",
        ],
        "lockfile_drift_correction": {
            "plan_pinned_stale": "s90-slot-pre-allocation-lockfile.md",
            "canonical_w0_1_home": "s93-slot-pre-allocation-lockfile.md",
            "basis": "substrate-first-canonical-sourcing.md §(ii.B); s93 lockfile pre-allocates the 7 S93 STAGE-3 flips incl. RESERVED-FOR-S93-W5-5-VII-AW-...",
        },
        "M1_M4_self_classification": {
            "M1_artifact_existence_with_content": True,
            "M2_registry_write_plus_sha_no_numerical_compute": True,
            "M3_verbatim_closed_stage2_verdicts": True,
            "M4_allowlist_append": "ORCHESTRATOR-ONLY (flagged in WP; not edited by this script)",
        },
    }
    OUT_JSON.write_text(json.dumps(record, indent=2), encoding="utf-8")
    print(f"  JSON sidecar -> {OUT_JSON.relative_to(ROOT)}")


def _emit_plot(v1, v2, v3, lf, branch_a, invariance_ok, chain_in_body_ok, chain_source_ok,
               slot_reserved_ok, lockfile_recorded_ok, verdict):
    fig, ax = plt.subplots(1, 1, figsize=(10.5, 5.0))
    labels = [  # (local)
        "branch (a):\nbody+index\nSTAGE-3",
        "invariance\n(Cell I+5-anat\n+3-level)",
        "Stage-2 chain\ncited in body",
        "Stage-2 chain\nverbatim source",
        "slot RESERVED\n(s93 lockfile)",
        "lockfile STAGE-3\nrow recorded",
    ]
    vals = [  # (local)
        int(branch_a), int(invariance_ok), int(chain_in_body_ok),
        int(chain_source_ok), int(slot_reserved_ok), int(lockfile_recorded_ok),
    ]
    colors = ["C2" if x else "C3" for x in vals]  # (local)
    ax.bar(labels, vals, color=colors, alpha=0.85)
    ax.set_ylim(0, 1.25)
    ax.set_yticks([0, 1])
    ax.set_yticklabels(["FAIL", "PASS"])
    ax.set_ylabel("artifact-existence predicate")
    for i, x in enumerate(vals):
        ax.text(i, x + 0.05, "PASS" if x else "FAIL", ha="center", va="bottom", fontsize=8,
                color="C2" if x else "C3", fontweight="bold")
    ax.set_title(
        f"{GATE_ID}\n"
        f"branch (a) VERIFICATION-CONFIRMATION of S92 in-session STAGE-3-PERMANENT promotion "
        f"(NO duplicate flip)\n"
        f"§VII.AW.OP-PROJ SUBSTRATE-CLOCK-UNIQUENESS-THEOREM — THIRD STAGE-3-PERMANENT "
        f"(ordinal NOT asserted; AU/AW collision -> CF-S94)\n"
        f"composite verdict: {verdict}",
        fontsize=8.0,
    )
    ax.grid(True, axis="y", ls=":", alpha=0.4)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130, bbox_inches="tight")
    plt.close(fig)
    print(f"  PNG -> {OUT_PNG.relative_to(ROOT)}")


if __name__ == "__main__":
    sys.exit(main())
