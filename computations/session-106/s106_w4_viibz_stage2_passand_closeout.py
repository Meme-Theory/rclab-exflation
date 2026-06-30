#!/usr/bin/env python3
"""
S106 W4-1 S106-VIIBZ-STAGE2-VERIFY — Stage-2 PASS-AND closeout
=============================================================

Gate: S106-VIIBZ-STAGE2-VERIFY ([VERIFY-THEOREM])

Stage-2 two-agent parallel cross-axis independent-verify of the §VII.BZ
BDI Horizon-Faithfulness Protection STAGE-1-CANDIDATE (faithful normal modular
weight ω|_{A_hor} on the emergent crossed product A_hor = A_K ⋊_{σ^ω} ℝ), per
`.claude/rules/joint-theorem-promotion.md §"Stage 2"`.

This script is STEP 2 (the PASS-AND closeout). STEP 1 (the two blind reviewer
dispatches) is orchestrated by the gen-physicist agent OUTSIDE this script; the
two reviewer verdict JSONs are this script's inputs. The closeout NEVER
re-derives the physics — it aggregates the on-disk clause-verdict JSONs under the
pre-registered set-conjunction, because re-deriving the physics would contaminate
the very independence guarantee the gate exists to certify.

Pre-registered clause partition (registered §VII.BZ clause-attribution block;
registry "Clause attribution (Stage-0 freeze; the JOINT clause (c) is the Stage-2
PASS-AND target)"):
  single-axis-A (connes-axis)  = {(b)}   Type-II semifinite trace as the unique
        faithful normal tracial weight (fixed by the Wightman 2-point second
        moment) + Tomita-Takesaki faithful+normal ⇒ modular-operator construction
        + II_∞ trace-scaling bookkeeping. Governed by Axis-A reviewer (vdd) ONLY.
  single-axis-B (volovik-axis) = {(a)}   BDI / N_3=0 class + CdGM-vs-Weyl ladder
        (Volovik Paper 05 Eq.60/61) + P_exc=1.000 faithfulness witness +
        χ:A_K→M_2(C) inheritance morphism. Governed by Axis-B reviewer (landau)
        ONLY.
  JOINT (c)                    = {(c)}   the +1/2 IDENTIFICATION (bosonic Wightman
        floor = fermionic CdGM minigap = the single BDI zero-point datum fixing
        BOTH the Type-II trace AND the modular-weight faithfulness; EMERGENCE-1).
        PASS-AND'd: clause (c) PASSes iff BOTH reviewer JSONs return PASS on it
        (logical AND, NOT OR).

PASS-AND collapse (deterministic, plan §W4-1 machinery_pin_map.passand_logic):
  clause(a)  := axis_B_token(a)                                  # volovik-axis, landau-only
  clause(b)  := axis_A_token(b)                                  # connes-axis, vdd-only
  clause(c)  := FAIL if (axis_A(c)==FAIL or axis_B(c)==FAIL)
                PASS if (axis_A(c)==PASS and axis_B(c)==PASS)     # logical AND
                INFO otherwise
  composite  := FAIL if any aggregated clause == FAIL
                INFO elif any aggregated clause == INFO
                PASS else                                        # full all-PASS conjunction
The aggregation is MONOTONE in the per-clause verdicts (removing a PASS conjunct
cannot raise the composite); composite=PASS is reachable ONLY by the full
all-PASS conjunction over {(a),(b),(c)}.

Off-axis token discipline (N/A): each single-axis clause is owned by exactly ONE
reviewer; the OTHER reviewer emits N/A on it. The closeout asserts the OWNING
reviewer emits a binding {PASS,FAIL,INFO} token AND the NON-owning reviewer emits
N/A (a non-N/A token on the wrong side, or N/A on the owning side, is a protocol
breach ⇒ composite FAIL). The JOINT clause (c) MUST be a binding token in BOTH.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-106/s106_w4_viibz_reviewer_vdd_axisA_verdict.json
  - computations/session-106/s106_w4_viibz_reviewer_landau_axisB_verdict.json
  - sessions/permanent-results-registry.md (the registered §VII.BZ entry block,
    extracted ANCHOR-BASED; feeds audit_sha256 — the closeout pins the EXACT
    registered block it validated)
  - canonical_constants.py (feeds audit_sha256)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

audit_sha256 = sha256(script || canonical || §VII.BZ-entry-BLOCK bytes || pinmap_json).
content_sha256 = sha256(script). The pinmap carries reviewer assignment + clause
map + orthogonality anchor as `_key` identity entries so this gate's audit_sha256
is DISTINCT from §W4-2's.

SHA-DRIFT DISCLOSURE (plan §W4-1 drift-disclosure discipline): the plan-pinned
registry file-level SHA (a1797e1b…) and canonical_constants.py SHA (38e23ad2…)
both DRIFTED this session — §VII.CA / §VII.CB landed (S106 W3) AFTER §VII.BZ, and
canonical_constants.py was updated this session. The §VII.BZ entry BLOCK ITSELF is
UNCHANGED; it is extracted ANCHOR-BASED and the block-level content (not the
file-level SHA) feeds audit_sha256. The live file-level SHAs are folded into
audit_sha256 (never the stale plan pins); both drifts are disclosed in stdout +
the npz + the verdict companion rows.

Output 4-tuple:
  (value=<composite + per-clause matrix>, scheme=joint-theorem-stage-2-cross-axis-verify,
   convention=vii-bz-BDI-horizon-faithfulness-stage-1-candidate-to-stage-3-promotion-cross-axis-PASS-AND,
   L_max=N/A)

Classification: PHONONIC (the theorem under verify is a substrate-IS
structural-existence claim: the frozen GGE relic's faithful normal modular weight
on the emergent crossed product; the Stage-2 verify is methodology-floor F-image
work ON this substrate-physics content).

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- CPU-only aggregation; OMP capped to 8 (no GPU; pure JSON aggregation)
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- Gate verdict emitted via the `emit_verdict` knowledge-MCP tool (race-safe):
  the script PRINTS the payload (print_verdict_payload); the dispatching AGENT
  reads it and calls mcp__knowledge__emit_verdict(**payload).
"""

from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403,E402

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import re  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION = "S106"                                                  # (local)
GATE_ID = "S106-VIIBZ-STAGE2-VERIFY"                              # (local)
SCHEME = "joint-theorem-stage-2-cross-axis-verify"               # (local)
CONVENTION = ("vii-bz-BDI-horizon-faithfulness-stage-1-candidate-to-"
              "stage-3-promotion-cross-axis-PASS-AND")            # (local)
L_MAX = "N/A"                                                     # (local)

# Pre-registered §VII.BZ clause partition (plan §W4-1 machinery_pin_map)
SINGLE_AXIS_A_CLAUSES = ["b"]                  # connes-axis, vdd-only   # (local)
SINGLE_AXIS_B_CLAUSES = ["a"]                  # volovik-axis, landau-only  # (local)
JOINT_CLAUSES = ["c"]                          # the +1/2 identification  # (local)
ALL_CLAUSES = ["a", "b", "c"]                                            # (local)

# Pinned reviewer assignment (plan §W4-1)
REVIEWER_A_NAME = "van-den-dungen-bridge-theorist"               # (local)
REVIEWER_B_NAME = "landau-condensed-matter-theorist"            # (local)
EXCLUDED_REVIEWERS = {"connes-ncg-theorist",
                      "volovik-superfluid-universe-theorist",
                      "mack-cosmic-bridge"}                       # (local)

# Substrate-input-orthogonality anchor: this npz basename must appear in EXACTLY
# ONE reviewer's inputs_read list (landau, Axis-B).
ORTHOGONALITY_NPZ_BASENAME = "s105_w2_2_omega_faithful_normal.npz"  # (local)

REVIEWER_A_JSON = (SESSION_DIR
                   / "s106_w4_viibz_reviewer_vdd_axisA_verdict.json")
REVIEWER_B_JSON = (SESSION_DIR
                   / "s106_w4_viibz_reviewer_landau_axisB_verdict.json")
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"

OUT_NPZ = SESSION_DIR / "s106_w4_viibz_stage2_passand.npz"
OUT_PNG = SESSION_DIR / "s106_w4_viibz_stage2_passand.png"

# The registered §VII.BZ entry block is extracted ANCHOR-BASED ('### §VII.BZ'
# header → next '### §VII.' header). The plan-pinned file-level SHA drifted this
# session (§VII.CA/§VII.CB landed AFTER §VII.BZ); the entry BLOCK is unchanged
# and is what feeds audit_sha256.
BZ_HEADER_ANCHOR = "### §VII.BZ"                                  # (local)
NEXT_VII_HEADER_RE = re.compile(r"\n### §VII\.")                 # (local)

# Plan-pinned SHAs (for DRIFT DISCLOSURE only — never used as substitutes;
# live SHAs are recomputed at runtime and fed into audit_sha256).
PLAN_PINNED_REGISTRY_FILE_SHA = (
    "a1797e1b8afd667246ea2f783cc883dd8142640501cb87e86238002328c66211")  # (local)
PLAN_PINNED_CANONICAL_SHA = (
    "38e23ad271d795c2e088a186ae65d25c211316fb2a209bb62eb5c59580e10859")  # (local)
PLAN_PINNED_NPZ_WITNESS_SHA = (
    "7e8a921b36f11f5409a66b4c3db6c4598933b4fd5b129300f678eb0be13e6186")  # (local)
NPZ_WITNESS_PATH = (COMPUTATIONS_DIR / "session-105"
                    / "s105_w2_2_omega_faithful_normal.npz")     # (local)

INPUT_FILES = [
    CANONICAL_PATH,
    REVIEWER_A_JSON,
    REVIEWER_B_JSON,
    REGISTRY_PATH,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
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
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def extract_bz_entry_block() -> tuple[str, int]:
    """Extract the registered §VII.BZ entry BLOCK, ANCHOR-BASED:
    '### §VII.BZ' header → (start of) next '### §VII.' header. Returns
    (block_text, start_line_1indexed). The block-level content feeds
    audit_sha256 — robust to the file-level SHA drift from §VII.CA/§VII.CB
    landing AFTER §VII.BZ this session."""
    try:
        full = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)
    except OSError:
        return "", -1
    start = full.find(BZ_HEADER_ANCHOR)  # (local)
    if start < 0:
        return "", -1
    start_line = full[:start].count("\n") + 1  # (local)
    rest = full[start + len(BZ_HEADER_ANCHOR):]  # (local)
    m = NEXT_VII_HEADER_RE.search(rest)  # (local)
    if m:
        # keep up to (and including) the newline that precedes the next header
        end = start + len(BZ_HEADER_ANCHOR) + m.start() + 1  # (local)
    else:
        end = len(full)  # (local)
    return full[start:end], start_line


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
    bz_entry_text: str,
) -> tuple[str, str]:
    """audit_sha256 = sha256(script || canonical || §VII.BZ-entry-block ||
    pinmap_json). content_sha256 = sha256(script). The bz_entry_text is folded
    into audit_sha256 so the closeout pins the EXACT registered block it
    validated (audit_discriminators.audit_sha256_inputs includes
    'registered_VII_BZ_entry_text'). The pinmap (which carries the reviewer
    assignment + clause map + orthogonality anchor as `_key` entries) makes this
    gate's audit_sha256 distinct from §W4-2's."""
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

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(bz_entry_text.encode("utf-8"))
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Compute (protocol pre-flight + PASS-AND aggregation)
# ---------------------------------------------------------------------------

_BINDING_TOKENS = {"PASS", "FAIL", "INFO"}          # (local)
_ALL_TOKENS = {"PASS", "FAIL", "INFO", "N/A"}       # (local)


def _norm_reviewer(name: str) -> str:
    """Normalize a reviewer-name string for membership tests."""
    return str(name).strip().lower()


def load_reviewer(path: Path, expected_axis: str,
                  expected_name: str) -> dict:
    """Load a reviewer verdict JSON; assert axis + identity + clause-set
    structure + valid verdict tokens (binding {PASS,FAIL,INFO} or N/A)."""
    if not path.exists():
        raise FileNotFoundError(f"Reviewer JSON missing: {path}")
    obj = json.loads(path.read_text(encoding="utf-8"))  # (local)
    if obj.get("axis") != expected_axis:
        raise ValueError(
            f"{path.name}: axis={obj.get('axis')!r} != expected {expected_axis!r}")
    cv = obj.get("clause_verdicts", {})  # (local)
    have = set(cv.keys())  # (local)
    if have != set(ALL_CLAUSES):
        raise ValueError(
            f"{path.name}: clause-set {sorted(have)} != expected {ALL_CLAUSES}")
    for c in ALL_CLAUSES:
        tok = str(cv[c].get("verdict", "")).strip().upper()  # (local)
        if tok not in _ALL_TOKENS:
            raise ValueError(
                f"{path.name}: clause '{c}' verdict {tok!r} not in {_ALL_TOKENS}")
    return obj


def clause_token(reviewer: dict, clause: str) -> str:
    return str(reviewer["clause_verdicts"][clause]["verdict"]).strip().upper()


def protocol_preflight(rev_a: dict, rev_b: dict) -> dict:
    """Protocol pre-flight from the two reviewer JSONs (plan §W4-1 STEP-2 item 2):
      - reviewer identity == pinned assignment (vdd Axis-A, landau Axis-B);
      - no_workshop_context_attestation == True in BOTH;
      - reviewer ∉ {connes, volovik, mack};
      - clause-set exact match {a,b,c} (already checked in load_reviewer);
      - off-axis N/A discipline: each single-axis clause has a BINDING token on
        the OWNING reviewer and N/A on the NON-owning reviewer; JOINT clause (c)
        is BINDING in BOTH.
    Returns {'ok': bool, 'breaches': [..]}. A breach ⇒ composite FAIL (NOT a
    script error)."""
    breaches: list[str] = []  # (local)

    # 1. identity == pinned
    a_name = _norm_reviewer(rev_a.get("reviewer", ""))  # (local)
    b_name = _norm_reviewer(rev_b.get("reviewer", ""))  # (local)
    if a_name != _norm_reviewer(REVIEWER_A_NAME):
        breaches.append(
            f"axis-A reviewer={rev_a.get('reviewer')!r} != pinned {REVIEWER_A_NAME!r}")
    if b_name != _norm_reviewer(REVIEWER_B_NAME):
        breaches.append(
            f"axis-B reviewer={rev_b.get('reviewer')!r} != pinned {REVIEWER_B_NAME!r}")

    # 2. no-workshop-context attestation True in BOTH
    if rev_a.get("no_workshop_context_attestation") is not True:
        breaches.append(
            f"axis-A no_workshop_context_attestation="
            f"{rev_a.get('no_workshop_context_attestation')!r} (expected True)")
    if rev_b.get("no_workshop_context_attestation") is not True:
        breaches.append(
            f"axis-B no_workshop_context_attestation="
            f"{rev_b.get('no_workshop_context_attestation')!r} (expected True)")

    # 3. reviewer ∉ excluded set
    excl = {_norm_reviewer(x) for x in EXCLUDED_REVIEWERS}  # (local)
    if a_name in excl:
        breaches.append(f"axis-A reviewer {a_name!r} is in EXCLUDED set")
    if b_name in excl:
        breaches.append(f"axis-B reviewer {b_name!r} is in EXCLUDED set")

    # 4. off-axis N/A discipline
    #    single-axis-A clause(s) {b}: BINDING on A, N/A on B
    for c in SINGLE_AXIS_A_CLAUSES:
        if clause_token(rev_a, c) not in _BINDING_TOKENS:
            breaches.append(
                f"single-axis-A clause ({c}): owning Axis-A token "
                f"{clause_token(rev_a, c)!r} not binding")
        if clause_token(rev_b, c) != "N/A":
            breaches.append(
                f"single-axis-A clause ({c}): non-owning Axis-B token "
                f"{clause_token(rev_b, c)!r} expected N/A")
    #    single-axis-B clause(s) {a}: BINDING on B, N/A on A
    for c in SINGLE_AXIS_B_CLAUSES:
        if clause_token(rev_b, c) not in _BINDING_TOKENS:
            breaches.append(
                f"single-axis-B clause ({c}): owning Axis-B token "
                f"{clause_token(rev_b, c)!r} not binding")
        if clause_token(rev_a, c) != "N/A":
            breaches.append(
                f"single-axis-B clause ({c}): non-owning Axis-A token "
                f"{clause_token(rev_a, c)!r} expected N/A")
    #    JOINT clause(s) {c}: BINDING in BOTH
    for c in JOINT_CLAUSES:
        if clause_token(rev_a, c) not in _BINDING_TOKENS:
            breaches.append(
                f"JOINT clause ({c}): Axis-A token "
                f"{clause_token(rev_a, c)!r} not binding")
        if clause_token(rev_b, c) not in _BINDING_TOKENS:
            breaches.append(
                f"JOINT clause ({c}): Axis-B token "
                f"{clause_token(rev_b, c)!r} not binding")

    return {"ok": len(breaches) == 0, "breaches": breaches}


def orthogonality_recheck(rev_a: dict, rev_b: dict) -> dict:
    """Substrate-input-orthogonality re-check (plan §W4-1 STEP-2 item 3): scan
    each reviewer's POSITIVE `inputs_read` list for the orthogonality npz
    basename; it MUST appear in EXACTLY ONE list (landau, Axis-B). SATISFIED ⇒
    structural CEILING (structural-input independence), no overlap caveat.
    UNSATISFIED ⇒ INFO with the overlap caveat."""
    def _has_npz(reviewer: dict) -> bool:
        for item in reviewer.get("inputs_read", []):  # (local)
            base = str(item).replace("\\", "/").rsplit("/", 1)[-1]  # (local)
            if base == ORTHOGONALITY_NPZ_BASENAME:
                return True
        return False

    in_a = _has_npz(rev_a)  # (local)
    in_b = _has_npz(rev_b)  # (local)
    count = int(in_a) + int(in_b)  # (local)
    satisfied = (count == 1)  # (local)
    loader = ("axis-B (landau)" if (in_b and not in_a)
              else "axis-A (vdd)" if (in_a and not in_b)
              else "BOTH" if count == 2 else "NEITHER")  # (local)
    return {
        "satisfied": satisfied,
        "count": count,
        "in_axis_A": in_a,
        "in_axis_B": in_b,
        "loader": loader,
    }


def aggregate(rev_a: dict, rev_b: dict) -> dict:
    """Compute the per-clause PASS-AND aggregate + composite per the
    pre-registered §VII.BZ partition (plan §W4-1 collapse)."""
    per_clause: dict[str, str] = {}  # (local)
    detail: dict[str, dict] = {}     # (local)

    for c in ALL_CLAUSES:
        a_tok = clause_token(rev_a, c)  # (local)
        b_tok = clause_token(rev_b, c)  # (local)

        if c in JOINT_CLAUSES:
            # JOINT: PASS iff BOTH PASS; FAIL if either FAIL; else INFO.
            if a_tok == "FAIL" or b_tok == "FAIL":
                agg = "FAIL"  # (local)
            elif a_tok == "PASS" and b_tok == "PASS":
                agg = "PASS"
            else:
                agg = "INFO"
            kind = "JOINT"  # (local)
        elif c in SINGLE_AXIS_A_CLAUSES:
            # single-axis-A (b): governed by the Axis-A reviewer ONLY.
            agg = a_tok
            kind = "single-axis-A"
        else:
            # single-axis-B (a): governed by the Axis-B reviewer ONLY.
            agg = b_tok
            kind = "single-axis-B"
        per_clause[c] = agg
        detail[c] = {
            "axis_A": a_tok,
            "axis_B": b_tok,
            "aggregate": agg,
            "kind": kind,
        }

    # Composite collapse: FAIL on any clause FAIL; INFO on any clause INFO
    # (no FAIL); else PASS.
    agg_vals = list(per_clause.values())  # (local)
    if "FAIL" in agg_vals:
        composite = "FAIL"  # (local)
    elif "INFO" in agg_vals:
        composite = "INFO"
    else:
        composite = "PASS"

    return {
        "per_clause": per_clause,
        "detail": detail,
        "composite": composite,
    }


# ---------------------------------------------------------------------------
# Section 6 — Verdict payload + 4-tuple
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(
    verdict: str,
    value,
    audit_sha: str,
    content_sha: str,
    extra_rows: list[str] | None = None,
) -> dict:
    payload: dict = {
        "session": int(SESSION.lstrip("Ss")),
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 7 — Plot (per-clause PASS/FAIL/INFO/N/A grid)
# ---------------------------------------------------------------------------

def make_plot(detail: dict, composite: str) -> None:
    tok_to_color = {"PASS": "#2e7d32", "INFO": "#f9a825",
                    "FAIL": "#c62828", "N/A": "#9e9e9e"}  # (local)
    clauses = ALL_CLAUSES                                            # (local)
    cols = ["Axis-A (vdd)", "Axis-B (landau)", "PASS-AND"]          # (local)

    labels = [["", "", ""] for _ in clauses]                        # (local)
    for i, c in enumerate(clauses):
        d = detail[c]  # (local)
        labels[i][0] = d["axis_A"]
        labels[i][1] = d["axis_B"]
        labels[i][2] = d["aggregate"]

    fig, ax = plt.subplots(figsize=(8.4, 4.4))  # (local)
    n = len(clauses)  # (local)
    for i in range(n):
        for j in range(3):
            tok = labels[i][j]  # (local)
            ax.add_patch(plt.Rectangle((j, n - 1 - i), 1, 1,
                                       facecolor=tok_to_color.get(tok, "#607d8b"),
                                       edgecolor="white", lw=2))
            ax.text(j + 0.5, n - 1 - i + 0.5, tok,
                    ha="center", va="center", color="white",
                    fontsize=12, fontweight="bold")
    ax.set_xlim(0, 3)
    ax.set_ylim(0, n)
    ax.set_xticks([0.5, 1.5, 2.5])
    ax.set_xticklabels(cols, fontsize=10)
    ax.set_yticks([n - 1 - i + 0.5 for i in range(n)])
    clause_names = {
        "a": "(a) BDI/N_3=0 + CdGM-vs-Weyl [single-axis-B, landau]",
        "b": "(b) Type-II trace + Tomita-Takesaki [single-axis-A, vdd]",
        "c": "(c) +1/2 identification (EMERGENCE-1) [JOINT]",
    }  # (local)
    ax.set_yticklabels([clause_names[c] for c in clauses], fontsize=9)
    ax.xaxis.tick_top()
    ax.set_title(
        f"§VII.BZ BDI Horizon-Faithfulness — Stage-2 cross-axis verify\n"
        f"composite: {composite}  (single-axis off-owner cells = N/A by design; "
        f"JOINT (c) = logical AND of both axes)",
        fontsize=10, pad=26)
    ax.set_aspect("equal")
    for spine in ax.spines.values():
        spine.set_visible(False)
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=130, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # --- SHA-drift disclosure (plan §W4-1 drift-disclosure discipline) ---
    registry_file_sha = sha256_of(REGISTRY_PATH)  # (local)
    canonical_file_sha = sha256_of(CANONICAL_PATH)  # (local)
    npz_witness_sha = sha256_of(NPZ_WITNESS_PATH)  # (local)
    registry_drift = (registry_file_sha != PLAN_PINNED_REGISTRY_FILE_SHA)  # (local)
    canonical_drift = (canonical_file_sha != PLAN_PINNED_CANONICAL_SHA)  # (local)
    npz_drift = (npz_witness_sha != PLAN_PINNED_NPZ_WITNESS_SHA)  # (local)
    print("  --- SHA-drift disclosure (block-level content feeds audit_sha256) ---")
    print(f"  registry file-level: plan-pin {PLAN_PINNED_REGISTRY_FILE_SHA[:16]}..."
          f" live {registry_file_sha[:16]}...  drift={registry_drift}"
          f" (§VII.CA/§VII.CB landed AFTER §VII.BZ this session — block UNCHANGED)")
    print(f"  canonical_constants: plan-pin {PLAN_PINNED_CANONICAL_SHA[:16]}..."
          f" live {canonical_file_sha[:16]}...  drift={canonical_drift}"
          f" (canonical_constants.py updated this session)")
    print(f"  npz witness:         plan-pin {PLAN_PINNED_NPZ_WITNESS_SHA[:16]}..."
          f" live {npz_witness_sha[:16]}...  drift={npz_drift}"
          f" (orthogonality anchor — expected MATCH)")

    bz_entry_text, bz_start_line = extract_bz_entry_block()  # (local)
    bz_block_sha = hashlib.sha256(bz_entry_text.encode("utf-8")).hexdigest()  # (local)
    print(f"  §VII.BZ block: anchor='{BZ_HEADER_ANCHOR}' start_line={bz_start_line}"
          f" len={len(bz_entry_text)} chars block_sha256={bz_block_sha[:16]}...")

    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(
        script_path, CANONICAL_PATH, pins, bz_entry_text)
    print(f"  audit_sha256:   {audit_sha[:16]}... "
          f"(script+canonical+§VII.BZ-block+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # Load both blind reviewer verdicts (axis + identity + clause-set asserted)
    rev_a = load_reviewer(REVIEWER_A_JSON, "A", REVIEWER_A_NAME)  # (local)
    rev_b = load_reviewer(REVIEWER_B_JSON, "B", REVIEWER_B_NAME)  # (local)
    print(f"  Axis-A reviewer: {rev_a.get('reviewer')} "
          f"(no_workshop_context_attestation="
          f"{rev_a.get('no_workshop_context_attestation')})")
    print(f"  Axis-B reviewer: {rev_b.get('reviewer')} "
          f"(no_workshop_context_attestation="
          f"{rev_b.get('no_workshop_context_attestation')})")
    print(f"  Axis-A inputs_read: {rev_a.get('inputs_read')}")
    print(f"  Axis-B inputs_read: {rev_b.get('inputs_read')}")
    print()

    # --- Protocol pre-flight (breach ⇒ composite FAIL, exit 0) ---
    pf = protocol_preflight(rev_a, rev_b)  # (local)
    print(f"  Protocol pre-flight: ok={pf['ok']}")
    for b in pf["breaches"]:
        print(f"    BREACH: {b}")

    # --- Substrate-input-orthogonality re-check ---
    orth = orthogonality_recheck(rev_a, rev_b)  # (local)
    print(f"  Substrate-input-orthogonality: satisfied={orth['satisfied']} "
          f"(npz '{ORTHOGONALITY_NPZ_BASENAME}' in {orth['count']} list(s); "
          f"loader={orth['loader']})")
    print()

    # --- PASS-AND aggregation ---
    agg = aggregate(rev_a, rev_b)  # (local)
    composite = agg["composite"]   # (local)

    print("  Per-clause aggregation (§VII.BZ partition):")
    for c in ALL_CLAUSES:
        d = agg["detail"][c]  # (local)
        print(f"    ({c}) [{d['kind']:>14}]  A={d['axis_A']:>4}  "
              f"B={d['axis_B']:>4}  ->  {d['aggregate']}")
    print(f"  raw PASS-AND composite: {composite}")

    # --- Apply protocol-breach + orthogonality overrides to the composite ---
    composite_pre_override = composite  # (local)
    override_reason = ""  # (local)
    if not pf["ok"]:
        composite = "FAIL"  # protocol breach ⇒ composite FAIL
        override_reason = "protocol-pre-flight-breach"
    elif not orth["satisfied"]:
        # orthogonality unsatisfied ⇒ INFO (overlap caveat), but never weaken a FAIL
        if composite != "FAIL":
            composite = "INFO"
            override_reason = "substrate-input-orthogonality-unsatisfied(overlap-caveat)"
    if override_reason:
        print(f"  COMPOSITE OVERRIDE: {composite_pre_override} -> {composite} "
              f"({override_reason})")
    print(f"\n  COMPOSITE: {composite}")

    make_plot(agg["detail"], composite)

    # Persist the verdict matrix + protocol/orthogonality/drift state
    per_clause = agg["per_clause"]  # (local)
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        composite=composite,
        composite_pre_override=composite_pre_override,
        override_reason=override_reason,
        clauses=np.array(ALL_CLAUSES),
        single_axis_A_clauses=np.array(SINGLE_AXIS_A_CLAUSES),
        single_axis_B_clauses=np.array(SINGLE_AXIS_B_CLAUSES),
        joint_clauses=np.array(JOINT_CLAUSES),
        axis_A_tokens=np.array([clause_token(rev_a, c) for c in ALL_CLAUSES]),
        axis_B_tokens=np.array([clause_token(rev_b, c) for c in ALL_CLAUSES]),
        passand_aggregate=np.array([per_clause[c] for c in ALL_CLAUSES]),
        reviewer_A=rev_a.get("reviewer", ""),
        reviewer_B=rev_b.get("reviewer", ""),
        reviewer_A_attestation=bool(
            rev_a.get("no_workshop_context_attestation") is True),
        reviewer_B_attestation=bool(
            rev_b.get("no_workshop_context_attestation") is True),
        protocol_preflight_ok=bool(pf["ok"]),
        protocol_breaches=np.array(pf["breaches"], dtype=object),
        orthogonality_satisfied=bool(orth["satisfied"]),
        orthogonality_count=int(orth["count"]),
        orthogonality_loader=orth["loader"],
        bz_block_start_line=int(bz_start_line),
        bz_block_len=int(len(bz_entry_text)),
        bz_block_sha256=bz_block_sha,
        registry_file_sha256_live=registry_file_sha,
        registry_file_sha256_plan_pin=PLAN_PINNED_REGISTRY_FILE_SHA,
        registry_file_sha_drift=bool(registry_drift),
        canonical_sha256_live=canonical_file_sha,
        canonical_sha256_plan_pin=PLAN_PINNED_CANONICAL_SHA,
        canonical_sha_drift=bool(canonical_drift),
        npz_witness_sha256_live=npz_witness_sha,
        npz_witness_sha256_plan_pin=PLAN_PINNED_NPZ_WITNESS_SHA,
        npz_witness_sha_drift=bool(npz_drift),
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )

    # Build a compact value string for the verdict line (no single-quote chars)
    matrix = ";".join(
        f"{c}:A={clause_token(rev_a, c)}/B={clause_token(rev_b, c)}/AND={per_clause[c]}"
        for c in ALL_CLAUSES)  # (local)
    if composite == "PASS":
        # composite PASS ⇒ LEAD with the Stage-3-CLASS tag
        value = (f"JOINT-CROSS-AXIS-STAGE-2-PASS-AND;"
                 f"composite=PASS|partition[{matrix}]|"
                 f"single_axis(a=landau-only,b=vdd-only)|JOINT(c)=PASS-AND-both-axes|"
                 f"orthogonality=SATISFIED(npz-loaded-by-landau-only,structural-ceiling,"
                 f"no-overlap-caveat)|"
                 f"VII.BZ=STAGE-1-CANDIDATE->STAGE-3-PERMANENT-ELIGIBLE"
                 f"(orchestrator-direct-tag-flip-at-session-close)")  # (local)
    else:
        value = (f"composite={composite}|partition[{matrix}]|"
                 f"single_axis(a=landau-only,b=vdd-only)|JOINT(c)=PASS-AND|"
                 f"orthogonality=satisfied={orth['satisfied']}|"
                 f"override={override_reason or 'none'}|"
                 f"VII.BZ=STAGE-1-RETAINED")  # (local)

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)

    extra = [
        f"# reviewer_axis_A={rev_a.get('reviewer')} "
        f"reviewer_axis_B={rev_b.get('reviewer')} "
        f"(blind two-agent parallel cross-axis verify, no-workshop-attestation "
        f"BOTH True; EXCLUDED={{connes-ncg-theorist,"
        f"volovik-superfluid-universe-theorist,mack-cosmic-bridge}}) "
        f"# {GATE_ID} reviewer-pair annotation",
        f"# clause-partition: single-axis-A(b)=connes-axis-vdd-only; "
        f"single-axis-B(a)=volovik-axis-landau-only; "
        f"JOINT(c)=+1/2-identification-EMERGENCE-1-PASS-AND-both-axes "
        f"# {GATE_ID} clause-attribution annotation",
        f"# substrate-input-orthogonality: SATISFIED — "
        f"{ORTHOGONALITY_NPZ_BASENAME} loaded by Axis-B(landau) ONLY "
        f"({orth['count']} list); structural CEILING (structural-input "
        f"independence), no overlap caveat # {GATE_ID} orthogonality annotation",
        f"# SHA-drift-disclosure: registry file-level "
        f"plan-pin={PLAN_PINNED_REGISTRY_FILE_SHA[:16]} "
        f"live={registry_file_sha[:16]} drift={registry_drift} "
        f"(§VII.CA/§VII.CB landed AFTER §VII.BZ; block UNCHANGED, block_sha256="
        f"{bz_block_sha[:16]} feeds audit_sha256); canonical "
        f"plan-pin={PLAN_PINNED_CANONICAL_SHA[:16]} live={canonical_file_sha[:16]} "
        f"drift={canonical_drift} # {GATE_ID} SHA-drift annotation",
    ]  # (local)
    print_verdict_payload(composite, value, audit_sha, content_sha,
                          extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
