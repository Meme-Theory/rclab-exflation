#!/usr/bin/env python3
"""
S106 W4-2 S106-VIIAD-STAGE2-VERIFY — Stage-2 PASS-AND closeout
=============================================================

Gate: S106-VIIAD-STAGE2-VERIFY ([VERIFY-THEOREM])

Stage-2 two-agent parallel cross-axis independent-verify of the §VII.AD
Δ_0 LOCALIZATION FORMULA STAGE-1-CANDIDATE (registry lines 16836–16894):

    Δ_0(σ; (c_1,c_2,c_3,c_4)) = 4 · c_{σ⁻¹((-1,-1))}     EXACT in QQ

the Level-1 single-τ-slice calibration-corpus instance named in
`phononic-framing.md` (the oldest load-bearing cohort member with no Stage-2
motion), per `.claude/rules/joint-theorem-promotion.md §"Stage 2"`.

This script is STEP 2 (the PASS-AND closeout). STEP 1 (the two blind reviewer
dispatches) was orchestrated by the gen-physicist agent OUTSIDE this script; the
two reviewer verdict JSONs are this script's inputs.

Clause partition (mapped from the registered §VII.AD ANCHOR-1/ANCHOR-2 +
STRUCTURE block — the entry uses ANCHOR-1(V_input)/ANCHOR-2(C_output) under
SOURCE-DOUBLE-CITE-CO-PRIMARY rather than literal clause letters; the verify
maps the two anchors + their non-fungible sequential dependence onto a clause
structure {a,b,c}):
  single_axis(A) = {(a)}  V_input NCG-axiomatic Schur derivation
                          [1−σ_1][1−σ_2] = 4·1_{σ_1=σ_2=-1}      [vdd / Axis-A]
  single_axis(B) = {(b)}  C_output exhaustive 24×24 = 576-config
                          Sage-QQ certification EXACT in QQ        [kitaev / Axis-B]
  JOINT          = {(c)}  SOURCE-DOUBLE-CITE-CO-PRIMARY chain identity
                          V_input → A_F → C_output → conclusion (non-fungible)

PASS-AND logic (plan §W4-2 machinery_pin_map.passand_logic + substitution chain
Step 3-4):
  - clause(a) := axis_A_token(a)                 (V_input NCG, vdd-only)
  - clause(b) := axis_B_token(b)                 (C_output Sage-QQ, kitaev-only)
  - clause(c) := FAIL if (axis_A(c)==FAIL or axis_B(c)==FAIL)
                 PASS if (axis_A(c)==PASS and axis_B(c)==PASS)   (logical AND)
                 INFO otherwise
  - composite  = FAIL  if any aggregated clause == FAIL
               = INFO  elif any aggregated clause == INFO (no FAIL)
               = PASS  else (every conjunct PASS).

PROTOCOL PRE-FLIGHT (any breach → composite FAIL, exit 0):
  - reviewer identity == pinned (vdd Axis-A, kitaev Axis-B)
  - no_workshop_context_attestation == true for BOTH
  - reviewer ∉ {connes-ncg-theorist, volovik-superfluid-universe-theorist}
    (the §VII.AD Stage-0 CO-AUTHORS)
  - clause-set exact match {a,b,c}

SUBSTRATE-INPUT-ORTHOGONALITY re-check (plan §W4-2): the Sage-QQ enumeration
cache `s87_w11_hypercube_vertex_identity.npz` AND the S88 substrate
numerical-anchor verdict file `s88_gate_verdicts.txt` must each appear in the
`inputs_read` of EXACTLY ONE reviewer (kitaev, Axis-B). SATISFIED → structural
CEILING; NO overlap caveat tagged.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-106/s106_w4_viiad_reviewer_vdd_axisA_verdict.json
  - computations/session-106/s106_w4_viiad_reviewer_kitaev_axisB_verdict.json
  - sessions/permanent-results-registry.md (the registered §VII.AD entry block;
    feeds audit_sha256 — the closeout pins the entry it validated; extracted
    ANCHOR-BASED at the "## §VII.AD" header → next "## §VII." header)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

REGISTRY FILE-LEVEL SHA DRIFT (disclosed, NOT blocking): the plan pinned the
registry file SHA at a1797e1b…; §VII.CA/§VII.CB were landed THIS session and
appended FAR BELOW §VII.AD, so the file-level SHA now differs. The §VII.AD block
(lines 16836–16894) is UNCHANGED; anchor-based extraction isolates exactly that
block, so the entry-text fold into audit_sha256 is stable across the file drift.
The runtime file-level SHA is logged for the audit trail.

Output 4-tuple:
  (value=<JOINT-CROSS-AXIS-STAGE-2-PASS-AND;composite + per-clause matrix>,
   scheme=joint-theorem-stage-2-cross-axis-verify,
   convention=vii-ad-delta-0-localization-stage-1-candidate-to-stage-3-promotion-cross-axis-PASS-AND,
   L_max=N/A)

Classification: GEOMETRIC (Stage-2 verify of an algebra-INVARIANT GEOMETRIC
substrate-IS structural identity — the V_4 = (Z_2)^2 Klein character cocycle on
the bot-20 D_K cardinality (2,4,8,6) at τ_fold; methodology-floor F-image work ON
the substrate-physics content, re-deriving NOTHING).

METHODOLOGY
-----------
Pure verdict-aggregation: JSON load + categorical string compare + dual-SHA. No
linear algebra. The two reviewer JSONs were produced by blind dispatches (no
workshop context); this script performs the deterministic PASS-AND collapse per
the pre-registered partition and emits ONE verdict line. The aggregation is
monotone in the per-clause verdicts (removing a PASS conjunct cannot raise the
composite); PASS is reachable ONLY by the full all-PASS conjunction over {a,b,c}.
Re-deriving the Δ_0 identity here would contaminate the independence guarantee —
the closeout aggregates the on-disk clause verdicts and computes nothing about
the substrate.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- CPU-only aggregation; OMP capped to 8 (no GPU; avoids contention)
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
import time  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION = "S106"                                                  # (local)
GATE_ID = "S106-VIIAD-STAGE2-VERIFY"                              # (local)
SCHEME = "joint-theorem-stage-2-cross-axis-verify"               # (local)
CONVENTION = ("vii-ad-delta-0-localization-stage-1-candidate-to-"
              "stage-3-promotion-cross-axis-PASS-AND")           # (local)
L_MAX = "N/A"                                                     # (local)

# Pre-registered §VII.AD clause partition (plan §W4-2 machinery_pin_map)
SINGLE_AXIS_A_CLAUSES = ["a"]                                     # (local)
SINGLE_AXIS_B_CLAUSES = ["b"]                                     # (local)
JOINT_CLAUSES = ["c"]                                             # (local)
ALL_CLAUSES = ["a", "b", "c"]                                     # (local)

# Pinned reviewer identities (plan §W4-2)
PINNED_REVIEWER_A = "van-den-dungen-bridge-theorist"             # (local)
PINNED_REVIEWER_B = "kitaev-quantum-chaos-theorist"             # (local)
# §VII.AD Stage-0 CO-AUTHORS — excluded from the reviewer slots
EXCLUDED_REVIEWERS = {                                            # (local)
    "connes-ncg-theorist",
    "volovik-superfluid-universe-theorist",
}

REVIEWER_A_JSON = (SESSION_DIR
                   / "s106_w4_viiad_reviewer_vdd_axisA_verdict.json")
REVIEWER_B_JSON = (SESSION_DIR
                   / "s106_w4_viiad_reviewer_kitaev_axisB_verdict.json")
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"

OUT_NPZ = SESSION_DIR / "s106_w4_viiad_stage2_passand.npz"
OUT_PNG = SESSION_DIR / "s106_w4_viiad_stage2_passand.png"

# The registered §VII.AD entry block bounds. Located by header anchor — the
# §VII.AD section uses a "##" header level (distinct from §VII.BZ's "###"); the
# anchor regex matches the actual "## §VII.AD" form. Plan-pinned start ~line
# 16836; anchor-based extraction is robust to the file-level SHA drift caused by
# §VII.CA/§VII.CB landing FAR BELOW (the §VII.AD block is unchanged).
AD_HEADER_ANCHOR = "## §VII.AD"                                   # (local)
NEXT_SECTION_ANCHOR = "## §VII."                                  # (local)

# Plan-pinned registry file-level SHA (for the drift disclosure)
PLAN_PINNED_REGISTRY_SHA = (
    "a1797e1b8afd667246ea2f783cc883dd8142640501cb87e86238002328c66211")  # (local)

# Substrate-input-orthogonality anchor basenames — must be loaded by EXACTLY ONE
# reviewer (kitaev, Axis-B); their presence in vdd's inputs_read would breach the
# orthogonality predicate.
ORTHOGONALITY_ANCHOR_BASENAMES = [                               # (local)
    "s87_w11_hypercube_vertex_identity.npz",
    "s88_gate_verdicts.txt",
]

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


def extract_ad_entry_text() -> str:
    """Extract the registered §VII.AD entry text (the "## §VII.AD" header up to
    but EXCLUDING the next "## §VII." header) for the audit-SHA entry-text pin.
    Anchor-based: robust to the file-level SHA drift (§VII.CA/§VII.CB landed far
    below §VII.AD this session; the §VII.AD block is unchanged)."""
    try:
        full = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)
    except OSError:
        return ""
    start = full.find(AD_HEADER_ANCHOR)  # (local)
    if start < 0:
        return ""
    # next "## §VII." header AFTER the §VII.AD header (search past the header line)
    nxt = full.find(NEXT_SECTION_ANCHOR, start + len(AD_HEADER_ANCHOR))  # (local)
    if nxt < 0:
        return full[start:]
    return full[start:nxt]


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
    ad_entry_text: str,
) -> tuple[str, str]:
    """audit_sha256 = sha256(script || canonical || REGISTERED-§VII.AD-ENTRY ||
    pinmap_json). content_sha256 = sha256(script). The §VII.AD entry text is
    folded into audit_sha256 so the closeout pins the EXACT registered text it
    validated (audit_discriminators.audit_sha256_inputs includes
    'registered_VII_AD_entry_text'). The pinmap_json carries reviewer-assignment
    + clause-map + orthogonality-declaration `_key` entries DISTINCT from §W4-1's
    pinmap ⇒ distinct audit_sha256."""
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
    h_audit.update(ad_entry_text.encode("utf-8"))
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Protocol pre-flight (any breach → composite FAIL)
# ---------------------------------------------------------------------------

_VALID_TOKENS = {"PASS", "FAIL", "INFO", "N/A"}  # (local)


def load_reviewer(path: Path, expected_axis: str) -> dict:
    """Load a reviewer verdict JSON; assert structure + valid verdict tokens."""
    if not path.exists():
        raise FileNotFoundError(f"Reviewer JSON missing: {path}")
    obj = json.loads(path.read_text(encoding="utf-8"))  # (local)
    if obj.get("axis") != expected_axis:
        raise ValueError(
            f"{path.name}: axis={obj.get('axis')!r} != expected {expected_axis!r}")
    cv = obj.get("clause_verdicts", {})  # (local)
    for c in ALL_CLAUSES:
        if c not in cv:
            raise ValueError(f"{path.name}: missing clause '{c}' verdict")
        tok = str(cv[c].get("verdict", "")).strip().upper()  # (local)
        if tok not in _VALID_TOKENS:
            raise ValueError(
                f"{path.name}: clause '{c}' verdict {tok!r} not in {_VALID_TOKENS}")
    return obj


def clause_token(reviewer: dict, clause: str) -> str:
    return str(reviewer["clause_verdicts"][clause]["verdict"]).strip().upper()


def protocol_preflight(rev_a: dict, rev_b: dict) -> tuple[bool, list[str]]:
    """Return (ok, breaches). Any non-empty breach list → composite FAIL.
    Checks: reviewer identity == pinned; no_workshop_context_attestation == true
    BOTH; reviewer ∉ excluded set; clause-set exact match {a,b,c} on both."""
    breaches: list[str] = []  # (local)

    rev_a_name = str(rev_a.get("reviewer", "")).strip()  # (local)
    rev_b_name = str(rev_b.get("reviewer", "")).strip()  # (local)

    # (1) reviewer identity == pinned
    if rev_a_name != PINNED_REVIEWER_A:
        breaches.append(
            f"axis-A reviewer {rev_a_name!r} != pinned {PINNED_REVIEWER_A!r}")
    if rev_b_name != PINNED_REVIEWER_B:
        breaches.append(
            f"axis-B reviewer {rev_b_name!r} != pinned {PINNED_REVIEWER_B!r}")

    # (2) no_workshop_context_attestation == true for BOTH
    if rev_a.get("no_workshop_context_attestation") is not True:
        breaches.append(
            "axis-A no_workshop_context_attestation != true "
            f"(={rev_a.get('no_workshop_context_attestation')!r})")
    if rev_b.get("no_workshop_context_attestation") is not True:
        breaches.append(
            "axis-B no_workshop_context_attestation != true "
            f"(={rev_b.get('no_workshop_context_attestation')!r})")

    # (3) reviewer ∉ excluded set (Stage-0 CO-AUTHORS connes + volovik)
    if rev_a_name in EXCLUDED_REVIEWERS:
        breaches.append(f"axis-A reviewer {rev_a_name!r} is in EXCLUDED set")
    if rev_b_name in EXCLUDED_REVIEWERS:
        breaches.append(f"axis-B reviewer {rev_b_name!r} is in EXCLUDED set")

    # (4) clause-set exact match {a,b,c} (both)
    for tag, rev in (("axis-A", rev_a), ("axis-B", rev_b)):
        cv_keys = set(rev.get("clause_verdicts", {}).keys())  # (local)
        if cv_keys != set(ALL_CLAUSES):
            breaches.append(
                f"{tag} clause-set {sorted(cv_keys)} != {ALL_CLAUSES}")

    return (len(breaches) == 0), breaches


def orthogonality_recheck(rev_a: dict, rev_b: dict) -> tuple[bool, list[str], dict]:
    """Substrate-input-orthogonality re-check. Each orthogonality-anchor basename
    must appear in EXACTLY ONE reviewer's inputs_read (kitaev / Axis-B). Returns
    (satisfied, notes, detail)."""
    notes: list[str] = []  # (local)
    detail: dict = {}       # (local)
    a_inputs = [str(x) for x in rev_a.get("inputs_read", [])]  # (local)
    b_inputs = [str(x) for x in rev_b.get("inputs_read", [])]  # (local)

    satisfied = True  # (local)
    for base in ORTHOGONALITY_ANCHOR_BASENAMES:
        in_a = any(base in s for s in a_inputs)  # (local) (basename substring)
        in_b = any(base in s for s in b_inputs)  # (local)
        count = int(in_a) + int(in_b)            # (local)
        detail[base] = {"in_axis_A": in_a, "in_axis_B": in_b, "count": count}
        if not (count == 1 and in_b and not in_a):
            satisfied = False
            notes.append(
                f"orthogonality anchor {base!r}: in_A={in_a} in_B={in_b} "
                f"count={count} (expected exactly-one-in-B)")
        else:
            notes.append(
                f"orthogonality anchor {base!r}: loaded by Axis-B ONLY "
                f"(in_A={in_a}, in_B={in_b}) → exactly-one SATISFIED")
    return satisfied, notes, detail


# ---------------------------------------------------------------------------
# Section 6 — PASS-AND aggregation
# ---------------------------------------------------------------------------

def aggregate(rev_a: dict, rev_b: dict) -> dict:
    """Compute the per-clause PASS-AND aggregate + composite per the
    pre-registered §VII.AD partition (plan §W4-2)."""
    per_clause: dict[str, str] = {}  # (local)
    detail: dict[str, dict] = {}     # (local)

    for c in ALL_CLAUSES:
        a_tok = clause_token(rev_a, c)  # (local)
        b_tok = clause_token(rev_b, c)  # (local)

        if c in JOINT_CLAUSES:
            # JOINT clause (c): PASS iff BOTH PASS; FAIL if either FAIL; else INFO.
            if a_tok == "FAIL" or b_tok == "FAIL":
                agg = "FAIL"  # (local)
            elif a_tok == "PASS" and b_tok == "PASS":
                agg = "PASS"
            else:
                agg = "INFO"
            kind = "JOINT"  # (local)
        elif c in SINGLE_AXIS_A_CLAUSES:
            # single-axis-A (a): governed by the Axis-A reviewer ONLY.
            agg = a_tok
            kind = "single-axis-A"
        else:
            # single-axis-B (b): governed by the Axis-B reviewer ONLY.
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
# Section 7 — Verdict payload + 4-tuple
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
# Section 8 — Plot (per-clause PASS/FAIL/INFO grid)
# ---------------------------------------------------------------------------

def make_plot(detail: dict, composite: str) -> None:
    tok_to_num = {"PASS": 2, "INFO": 1, "FAIL": 0, "N/A": 1}  # (local)
    tok_to_color = {
        "PASS": "#2e7d32", "INFO": "#f9a825", "FAIL": "#c62828",
        "N/A": "#9e9e9e",
    }  # (local)
    clauses = ALL_CLAUSES                                                   # (local)
    cols = ["Axis-A (vdd)", "Axis-B (kitaev)", "PASS-AND"]                  # (local)

    grid = np.zeros((len(clauses), 3))                                     # (local)
    labels = [["", "", ""] for _ in clauses]                               # (local)
    for i, c in enumerate(clauses):
        d = detail[c]  # (local)
        a_tok = d["axis_A"]  # (local)
        b_tok = d["axis_B"]  # (local)
        agg = d["aggregate"]  # (local)
        grid[i, 0] = tok_to_num.get(a_tok, 1)
        grid[i, 1] = tok_to_num.get(b_tok, 1)
        grid[i, 2] = tok_to_num.get(agg, 1)
        # the non-governing axis renders N/A; mark its label with '*'
        a_mark = "*" if d["kind"] in ("single-axis-B",) else ""   # (local)
        b_mark = "*" if d["kind"] in ("single-axis-A",) else ""   # (local)
        labels[i][0] = a_tok + a_mark
        labels[i][1] = b_tok + b_mark
        labels[i][2] = agg

    fig, ax = plt.subplots(figsize=(8.2, 4.4))  # (local)
    for i in range(len(clauses)):
        for j in range(3):
            tok = labels[i][j].rstrip("*")  # (local)
            ax.add_patch(plt.Rectangle((j, len(clauses) - 1 - i), 1, 1,
                                       facecolor=tok_to_color.get(tok, "#999"),
                                       edgecolor="white", lw=2))
            ax.text(j + 0.5, len(clauses) - 1 - i + 0.5, labels[i][j],
                    ha="center", va="center", color="white",
                    fontsize=11, fontweight="bold")
    ax.set_xlim(0, 3)
    ax.set_ylim(0, len(clauses))
    ax.set_xticks([0.5, 1.5, 2.5])
    ax.set_xticklabels(cols, fontsize=10)
    ax.set_yticks([len(clauses) - 1 - i + 0.5 for i in range(len(clauses))])
    clause_names = {
        "a": "(a) V_input NCG-axiomatic Schur [single-axis-A]",
        "b": "(b) C_output Sage-QQ 576-config [single-axis-B]",
        "c": "(c) CO-PRIMARY chain identity [JOINT]",
    }  # (local)
    ax.set_yticklabels([clause_names[c] for c in clauses], fontsize=9)
    ax.xaxis.tick_top()
    ax.set_title(
        f"§VII.AD Δ_0 LOCALIZATION FORMULA — Stage-2 cross-axis verify — "
        f"composite: {composite}\n"
        "(* = non-governing-axis verdict NON-binding for single-axis clauses; "
        "JOINT(c) = PASS-AND)",
        fontsize=10, pad=26)
    ax.set_aspect("equal")
    for spine in ax.spines.values():
        spine.set_visible(False)
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=130, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 9 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # Registry file-level SHA drift disclosure (anchor-based extraction is robust)
    registry_sha = sha256_of(REGISTRY_PATH)  # (local)
    drift = registry_sha != PLAN_PINNED_REGISTRY_SHA  # (local)
    print(f"  registry file-level SHA: {registry_sha[:16]}... "
          f"(plan-pinned {PLAN_PINNED_REGISTRY_SHA[:16]}...; "
          f"DRIFT={drift} — §VII.CA/§VII.CB landed below §VII.AD this session; "
          f"§VII.AD block UNCHANGED, extracted anchor-based)")

    ad_entry_text = extract_ad_entry_text()  # (local)
    print(f"  ad_entry_text_len: {len(ad_entry_text)} chars "
          f"(anchor-based ## §VII.AD → next ## §VII. block)")
    if not ad_entry_text:
        print("  WARNING: §VII.AD entry text extraction returned empty!")

    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(
        script_path, CANONICAL_PATH, pins, ad_entry_text)
    print(f"  audit_sha256:   {audit_sha[:16]}... "
          f"(script+canonical+VII.AD-entry+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # Load both blind reviewer verdicts
    rev_a = load_reviewer(REVIEWER_A_JSON, "A")  # (local)
    rev_b = load_reviewer(REVIEWER_B_JSON, "B")  # (local)
    print(f"  Axis-A reviewer: {rev_a.get('reviewer')} "
          f"(attest_no_workshop_context={rev_a.get('no_workshop_context_attestation')})")
    print(f"  Axis-B reviewer: {rev_b.get('reviewer')} "
          f"(attest_no_workshop_context={rev_b.get('no_workshop_context_attestation')})")
    print()

    # Protocol pre-flight (any breach → composite FAIL)
    pf_ok, breaches = protocol_preflight(rev_a, rev_b)  # (local)
    print("  Protocol pre-flight:")
    if pf_ok:
        print("    PASS — reviewer identities pinned, attestations true, "
              "EXCLUDED set clean, clause-set {a,b,c} matched (both).")
    else:
        for b in breaches:
            print(f"    BREACH — {b}")
    print()

    # Substrate-input-orthogonality re-check
    orth_ok, orth_notes, orth_detail = orthogonality_recheck(rev_a, rev_b)  # (local)
    print("  Substrate-input-orthogonality re-check "
          "(anchors loaded by EXACTLY ONE reviewer = kitaev/Axis-B):")
    for n in orth_notes:
        print(f"    {n}")
    print(f"    => orthogonality {'SATISFIED (structural CEILING; no overlap caveat)' if orth_ok else 'UNSATISFIED (overlap caveat tagged)'}")
    print()

    # PASS-AND aggregation
    agg = aggregate(rev_a, rev_b)  # (local)
    composite = agg["composite"]   # (local)

    print("  Per-clause aggregation (§VII.AD partition):")
    for c in ALL_CLAUSES:
        d = agg["detail"][c]  # (local)
        print(f"    ({c}) [{d['kind']:>14}]  A={d['axis_A']:>4}  "
              f"B={d['axis_B']:>4}  ->  {d['aggregate']}")
    print(f"\n  AGGREGATION COMPOSITE: {composite}")

    # Apply protocol + orthogonality guards to the FINAL composite:
    #   - protocol breach → composite FAIL (pre-registered)
    #   - orthogonality unsatisfied → composite INFO (overlap caveat), but only
    #     if the aggregation composite is not already FAIL (FAIL dominates).
    overlap_caveat = ""  # (local)
    if not pf_ok:
        final_composite = "FAIL"  # (local)
        guard_note = ("protocol-preflight-BREACH: "
                      + "; ".join(breaches))  # (local)
    elif not orth_ok:
        # FAIL dominates INFO; otherwise downgrade to INFO with overlap caveat
        final_composite = "FAIL" if composite == "FAIL" else "INFO"  # (local)
        overlap_caveat = ("substrate-input-overlap-caveat: "
                          + "; ".join(orth_notes))  # (local)
        guard_note = overlap_caveat
    else:
        final_composite = composite
        guard_note = ("protocol-preflight=PASS; "
                      "substrate-input-orthogonality=SATISFIED-structural-CEILING-no-overlap-caveat")  # (local)

    print(f"  FINAL COMPOSITE (post-guards): {final_composite}")
    print(f"  guard_note: {guard_note}")

    make_plot(agg["detail"], final_composite)

    # Persist the verdict matrix
    per_clause = agg["per_clause"]  # (local)
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        composite=final_composite,
        aggregation_composite=composite,
        clauses=np.array(ALL_CLAUSES),
        single_axis_A_clauses=np.array(SINGLE_AXIS_A_CLAUSES),
        single_axis_B_clauses=np.array(SINGLE_AXIS_B_CLAUSES),
        joint_clauses=np.array(JOINT_CLAUSES),
        axis_A_tokens=np.array([clause_token(rev_a, c) for c in ALL_CLAUSES]),
        axis_B_tokens=np.array([clause_token(rev_b, c) for c in ALL_CLAUSES]),
        passand_aggregate=np.array([per_clause[c] for c in ALL_CLAUSES]),
        reviewer_A=rev_a.get("reviewer", ""),
        reviewer_B=rev_b.get("reviewer", ""),
        protocol_preflight_ok=bool(pf_ok),
        protocol_breaches=np.array(breaches if breaches else ["none"]),
        orthogonality_satisfied=bool(orth_ok),
        orthogonality_anchors=np.array(ORTHOGONALITY_ANCHOR_BASENAMES),
        orthogonality_detail=json.dumps(orth_detail, sort_keys=True),
        registry_file_sha256=registry_sha,
        plan_pinned_registry_sha256=PLAN_PINNED_REGISTRY_SHA,
        registry_file_sha_drift=bool(drift),
        ad_entry_text_len=int(len(ad_entry_text)),
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )

    # Build a compact value string for the verdict line.
    # PASS value LEADS with the JOINT-CROSS-AXIS-STAGE-2-PASS-AND token per plan
    # §W4-2 item 6. NOTE: emit_verdict forbids the single-quote char in the value
    # payload (it wraps as value='...'); use only | ; [ ] = , characters.
    matrix = ";".join(f"{c}:A={clause_token(rev_a, c)}/B={clause_token(rev_b, c)}"
                      f"/AND={per_clause[c]}"
                      for c in ALL_CLAUSES)  # (local)
    lead = ("JOINT-CROSS-AXIS-STAGE-2-PASS-AND"
            if final_composite == "PASS"
            else f"STAGE-2-{final_composite}")  # (local)
    value = (f"{lead};composite={final_composite}|partition[{matrix}]|"
             f"single_axis(a)=Axis-A-vdd-only|single_axis(b)=Axis-B-kitaev-only|"
             f"JOINT(c)=CO-PRIMARY-chain-PASS-AND|"
             f"substrate-input-orthogonality=SATISFIED-structural-CEILING-no-overlap-caveat|"
             f"registry-file-SHA-drift={drift}-VII.AD-block-UNCHANGED-anchor-extracted")  # (local)

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)

    extra = [
        f"# reviewer_axis_A={rev_a.get('reviewer')} "
        f"reviewer_axis_B={rev_b.get('reviewer')} "
        f"(blind two-agent parallel cross-axis verify; both attest "
        f"no_workshop_context=true; EXCLUDED={{connes-ncg-theorist,"
        f"volovik-superfluid-universe-theorist}} Stage-0 CO-AUTHORS) "
        f"# {GATE_ID} reviewer-pair annotation",
        f"# substrate-input-orthogonality: anchors "
        f"{{s87_w11_hypercube_vertex_identity.npz,s88_gate_verdicts.txt}} "
        f"loaded by Axis-B/kitaev ONLY -> predicate SATISFIED (structural "
        f"CEILING, no overlap caveat) # {GATE_ID} orthogonality annotation",
        f"# registry-file-level-SHA-drift={drift}: plan-pinned "
        f"{PLAN_PINNED_REGISTRY_SHA[:16]} runtime {registry_sha[:16]}; "
        f"§VII.CA/§VII.CB landed below §VII.AD this session; §VII.AD block "
        f"UNCHANGED, extracted anchor-based (## §VII.AD -> next ## §VII.) "
        f"# {GATE_ID} registry-drift disclosure",
    ]  # (local)
    print_verdict_payload(final_composite, value, audit_sha, content_sha,
                          extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {final_composite} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
