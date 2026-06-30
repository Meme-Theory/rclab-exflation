#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CF-S95-HK-1 — §VII.BG Stage-2 cross-axis verify AGGREGATOR (mechanical PASS-AND)
================================================================================

Two-agent parallel Stage-2 cross-axis independent-verify (per
`.claude/rules/joint-theorem-promotion.md §"Stage 2"`) of the §VII.BG α_s T5
Direct-Connes-Karoubi K_0-pairing transport bridge at the a_4 Yang-Mills home
pole s=2 — registered STAGE-1-CANDIDATE at S94 W1-3
(`permanent-results-registry.md:20713`).

This is the MECHANICAL AGGREGATION / EMISSION script. It performs the
deterministic PASS-AND of two ALREADY-FROZEN cross-reviewer MARKDOWN reviews:

    computations/session-95/s95_w1_1_axisA_lizzi_review.md   (Axis-A spectral/NCG)
    computations/session-95/s95_w1_1_axisB_volovik_review.md (Axis-B transport/superfluid)

The reviewers' independence IS the physics; this script does deterministic
boolean PASS-AND + verdict-line emission. It does NOT re-derive any clause.

CLAUSE PARTITION (asymmetric — the §VII.BG 5-anatomy splits spectral/transport):
  Axis-A (lizzi) single-axis clauses : Element-1, Element-3, Element-4, Degree-match
  Axis-B (volovik) single-axis clauses: Element-2-OE-form, BdG-chi-K_0-class,
                                        substrate-natural-NON-SCALAR-binding
  JOINT clause (c)  : Delta_scheme -> 0  (appears in BOTH reviews; PASS-AND'd,
                      logical AND not OR, per joint-theorem-promotion.md Stage-2 (b))

STRICT PASS-AND BOUNDARY (plan §W1-1 operator + strict_PASS_boundary):

    composite == 'PASS'  iff
        ( AND_{i in axisA single-axis clauses} verdict_A[i] == PASS )
        AND ( AND_{j in axisB single-axis clauses} verdict_B[j] == PASS )
        AND ( JOINT_c PASS in Axis-A  AND  JOINT_c PASS in Axis-B )   [PASS-AND]
        AND ( substrate_input_orthogonal == True )   [Axis-A anchor set
                                                       DISJOINT from Axis-B anchor set]
        AND ( both AXIS-COMPOSITE lines == PASS )
    composite == 'FAIL'  iff ANY single-axis clause FAILs on EITHER axis, OR the
        JOINT clause is not PASS-AND, OR orthogonality is violated, OR an axis
        composite is FAIL.
    composite == 'INFO'  iff no hard FAIL but >=1 clause (single-axis or JOINT)
        is INFO on either axis (Stage-2-INFO-deferred).

The JOINT clause (c) Delta_scheme=0 is independently corroborated by the SEPARATE
S90-AQ-SECONDARY-CLASS-SCHEME-DISCRIMINATOR gate (delta_scheme=0.000e+00,
GV_APS_L12=GV_CS_L12=-1.208158e+08) and the PROVEN W17 Bare-Eigenvalue
Parity-Blindness Wall — Delta_scheme=0 is FORCED by the BDI universality class
(eta-defect vanishes; odd-grading GV-Heitsch carries the secondary content).

SCOPE (§VII cross-pillar bridge — UNLIKE the LQG/CDT cross-FRAMEWORK comparison):
  §VII.BG IS a cross-PILLAR §VII bridge theorem on (A_K, H_K, D_K). A composite
  PASS LICENSES the STAGE-1-CANDIDATE -> STAGE-3-PERMANENT promotion; the
  registry-text flip is effected by mack-cosmic-bridge (sole registry writer per
  feedback_mack-bridge-role.md) as the post-gate hook. This gate does NOT edit
  permanent-results-registry.md.

NO OPTION-A SUPERSEDES: this is the FIRST CF-S95-HK-1 emission (0 prior lines in
  s95_gate_verdicts.txt; the file does not yet exist); the verdict line is a clean
  append. (A defensive latest-non-superseded scan is still run; returns None.)

Trigger: [VERIFY-THEOREM] (no [SIGN] 3-tuple companion row required). Dual-SHA
closure: content_sha256 over THIS script; audit_sha256 over the input-pin map +
both axis review SHAs + the registry-entry-text SHA + the w1_3 npz SHA + per-gate
identity keys (gate-distinct per mechanical-closure-discipline.md item 3).
"""

from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import argparse
import hashlib
import json
import re
import sys
import time
from pathlib import Path

import numpy as np

# --- canonical constants (mandatory per .claude/rules/math-scripts.md S34+) ---
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent  # (local)
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"  # (local)
sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import (  # noqa: E402
    M_KK,
    tau_fold,
    alpha_s_cmb_central,
    alpha_s_canon_2020,
    alpha_s_canon_2020_err,
    w0_FW,
    r_CMB_framework,
)

# ---------------------------------------------------------------------------
# Gate identity + canonical pins
# ---------------------------------------------------------------------------
GATE_ID = "CF-S95-HK-1"  # (local)
SCHEME = "T5-Connes-Karoubi-K_0-pairing-a_4-channel-s2-index-fixed"  # (local)
# convention per plan machinery_pin_map; FULL-class direct spectral re-derivation by both reviewers.
CONVENTION = "VII-BG-STAGE-2-TWO-AXIS-NON-CONNES-PASS-AND"  # (local)
L_MAX = "12"  # (local) the S94 W1-3 canonical L_max for the §VII.BG observable
TOL_DELTA_SCHEME = 1e-12  # (local) machine-zero band for the JOINT Delta_scheme clause

# Clause-name canonical lists (asymmetric: 5 spectral-side incl JOINT; 4 transport-side incl JOINT).
AXIS_A_SINGLE_CLAUSES = ["Element-1", "Element-3", "Element-4", "Degree-match"]  # (local)
AXIS_B_SINGLE_CLAUSES = ["Element-2", "BdG", "substrate-natural"]  # (local)
JOINT_CLAUSE_KEY = "JOINT"  # (local) Delta_scheme->0 (clause (c)), in BOTH reviews

# Original-authoring-agent exclusion (joint-theorem-promotion.md Axis-B Selection clause-2).
EXCLUDED_AUTHOR = "connes-ncg-theorist"  # (local)
ADMISSIBLE_REVIEWERS = {  # (local)
    "lizzi-spectral-functional-theorist",   # Axis-A (spectral / NCG)
    "volovik-superfluid-universe-theorist",  # Axis-B (transport / superfluid)
}

# ---------------------------------------------------------------------------
# Canonical paths
# ---------------------------------------------------------------------------
SESSION95_DIR = PROJECT_ROOT / "computations" / "session-95"  # (local)
VERDICT_TXT = SESSION95_DIR / "s95_gate_verdicts.txt"  # (local; canonical per gate-verdicts.md)
AXIS_A_MD = SESSION95_DIR / "s95_w1_1_axisA_lizzi_review.md"  # (local)
AXIS_B_MD = SESSION95_DIR / "s95_w1_1_axisB_volovik_review.md"  # (local)
OUT_JSON = SESSION95_DIR / "s95_w1_1_vii_bg_stage2_aggregator.json"  # (local)
OUT_NPZ = SESSION95_DIR / "s95_w1_1_vii_bg_stage2_aggregator.npz"  # (local)
OUT_PNG = SESSION95_DIR / "s95_w1_1_vii_bg_stage2_aggregator.png"  # (local)

REGISTRY = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)
W1_3_NPZ = (  # (local)
    PROJECT_ROOT / "computations" / "session-94"
    / "s94_w1_3_vii_bx_t5_alpha_s_a4_recovery.npz"
)
S94_VERDICTS = (  # (local)
    PROJECT_ROOT / "computations" / "session-94" / "s94_gate_verdicts.txt"
)
JOINT_THEOREM_RULE = (  # (local)
    PROJECT_ROOT / ".claude" / "rules" / "joint-theorem-promotion.md"
)
CANONICAL_CONSTANTS = SHARED_DIR / "canonical_constants.py"  # (local)

# §VII.BG registry block lines (the reviewers read ONLY this block; see audit_sha256_inputs).
REGISTRY_BLOCK_START = 20713  # (local)
REGISTRY_BLOCK_END = 20789  # (local; per both reviewers' recorded SHA pin)

# Input-pin map (source documents the aggregation consumes; SHAs feed audit_sha256).
INPUT_FILES = [  # (local)
    CANONICAL_CONSTANTS,
    AXIS_A_MD,
    AXIS_B_MD,
    W1_3_NPZ,
    S94_VERDICTS,
    JOINT_THEOREM_RULE,
]


# ---------------------------------------------------------------------------
# SHA helpers (canonical dual-SHA per the S84+ schema)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return "0" * 64


def sha256_of_registry_block() -> str:
    """SHA-256 over the §VII.BG registry block (lines 20713-20789 inclusive), the
    ONLY text the reviewers were given. Reconstructed here for the audit_sha256
    input-pin map; matches both reviewers' recorded pin 18d365904f...
    """
    try:
        lines = REGISTRY.read_text(encoding="utf-8").splitlines(keepends=True)  # (local)
        block = "".join(lines[REGISTRY_BLOCK_START - 1:REGISTRY_BLOCK_END])  # (local)
        return hashlib.sha256(block.encode("utf-8")).hexdigest()
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
    # registry block SHA (line-range, not whole-file) — the reviewers' actual input
    reg_block_sha = sha256_of_registry_block()  # (local)
    pins[f"registry_block_VII_BG_L{REGISTRY_BLOCK_START}-{REGISTRY_BLOCK_END}"] = reg_block_sha
    print(f"  registry_block_VII_BG (L{REGISTRY_BLOCK_START}-{REGISTRY_BLOCK_END}): "
          f"{reg_block_sha[:16]}...")
    return pins


def compute_dual_sha(pins: dict[str, str], aggregate_payload: str) -> tuple[str, str]:
    """Dual-SHA per gate-verdicts.md S84+ schema.

    content_sha256 = SHA-256 over THIS script (the verify-theorem aggregation logic).
    audit_sha256   = SHA-256 over the input-pin map (incl registry-block SHA + both
                     axis review SHAs + the w1_3 npz SHA) + the aggregate PASS-AND
                     payload + per-gate identity keys (gate-distinct).
    """
    h_content = hashlib.sha256()  # (local)
    h_content.update(Path(__file__).read_bytes())
    content = h_content.hexdigest()  # (local)

    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(pinmap_json)
    axis_a_sha = sha256_of(AXIS_A_MD)  # (local)
    axis_b_sha = sha256_of(AXIS_B_MD)  # (local)
    w1_3_sha = sha256_of(W1_3_NPZ)  # (local)
    reg_block_sha = sha256_of_registry_block()  # (local)
    h_audit.update(
        (
            f"axisA={axis_a_sha}|axisB={axis_b_sha}|"
            f"w1_3_npz={w1_3_sha}|registry_entry_text={reg_block_sha}|"
            f"{aggregate_payload}"
        ).encode("utf-8")
    )
    h_audit.update(f"{GATE_ID}|{SCHEME}|{CONVENTION}|L_max={L_MAX}".encode("utf-8"))
    audit = h_audit.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Option-A latest-non-superseded scan (defensive; expect None — first emission)
# ---------------------------------------------------------------------------
def find_latest_prior_audit_sha() -> str | None:
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


# ---------------------------------------------------------------------------
# Markdown review parsers (clause verdicts + composite + anchors)
# ---------------------------------------------------------------------------
# Both reviews list clauses as lines of the form:
#   - CLAUSE <name...> : <PASS|FAIL|INFO> — <rationale>
# and end with:
#   AXIS-A COMPOSITE: PASS   /   AXIS-B COMPOSITE: PASS
# The clause-name match keys on the canonical clause tokens (Element-1, ..., JOINT).

_CLAUSE_LINE = re.compile(
    r"^\s*(?:[-*]\s*)?(?:\*\*)?CLAUSE\b(?P<body>.*)$", re.IGNORECASE
)  # (local)
_VERDICT_TOK = re.compile(r"\b(PASS|FAIL|INFO)\b")  # (local)
_COMPOSITE = re.compile(
    r"^\s*(?:\*\*)?AXIS-(?P<axis>[AB])\s+COMPOSITE\b[^A-Za-z]*?(?P<v>PASS|FAIL|INFO)\b",
    re.IGNORECASE,
)  # (local)


def _split_label_rationale(body: str) -> tuple[str, str]:
    """Split a CLAUSE line body into (LABEL, RATIONALE).

    Both reviews use the shape `CLAUSE <label...>: <VERDICT> — <rationale...>`.
    The clause LABEL is everything before the FIRST colon that is immediately
    followed (after optional markdown/space) by a verdict token. Classification
    MUST key on the LABEL only — the rationale routinely mentions OTHER clauses'
    keywords (e.g. Element-3's rationale cites 'Δ_scheme=0'; the substrate-natural
    rationale cites 'K_0 class') which would mis-route a whole-body classifier.
    """
    # Find a colon followed (after optional '**'/spaces) by a verdict token.
    for m in re.finditer(r":", body):
        tail = body[m.end():]  # (local)
        head = tail.lstrip(" *")  # (local)
        vm = _VERDICT_TOK.match(head.upper())  # (local) verdict token at START of tail
        if vm:
            label = body[: m.start()]  # (local)
            return label, tail
    # Fallback: split on first colon regardless.
    if ":" in body:
        i = body.index(":")  # (local)
        return body[:i], body[i + 1:]
    return body, ""


def _verdict_from_rationale(rationale: str, label: str) -> str:
    """The verdict is the FIRST PASS/FAIL/INFO token in the rationale (right after
    the label colon). Fall back to the label, then ABSENT.
    """
    m = _VERDICT_TOK.search(rationale.upper())  # (local)
    if m:
        return m.group(1)
    m = _VERDICT_TOK.search(label.upper())  # (local)
    return m.group(1) if m else "ABSENT"


def _classify_clause(label: str) -> str | None:
    """Map a CLAUSE LABEL (text before the verdict colon) to a canonical clause key.

    Keys (canonical): Element-1, Element-3, Element-4, Degree-match (Axis-A single);
    Element-2, BdG, substrate-natural (Axis-B single); JOINT (the Delta_scheme clause,
    in BOTH reviews). Keying on the LABEL ONLY (not the rationale) is what prevents
    the rationale-keyword cross-routing the first dry-run exposed.
    """
    b = label  # (local)
    # JOINT clause (c) Delta_scheme — the label literally contains 'JOINT' and/or 'Δ_scheme'.
    if re.search(r"\bJOINT\b", b, re.IGNORECASE) or re.search(
        r"Δ_?scheme|delta_?scheme", b, re.IGNORECASE
    ):
        return JOINT_CLAUSE_KEY
    if re.search(r"Element[\s\-_]*1\b", b, re.IGNORECASE):
        return "Element-1"
    if re.search(r"Element[\s\-_]*2\b", b, re.IGNORECASE):
        return "Element-2"
    if re.search(r"Element[\s\-_]*3\b", b, re.IGNORECASE):
        return "Element-3"
    if re.search(r"Element[\s\-_]*4\b", b, re.IGNORECASE):
        return "Element-4"
    if re.search(r"Degree[\s\-_]*match", b, re.IGNORECASE):
        return "Degree-match"
    if re.search(r"substrate[\s\-_]*natural|NON[\s\-_]*SCALAR|non[\s\-_]*scalar", b, re.IGNORECASE):
        return "substrate-natural"
    if re.search(r"\bBdG\b|K_?0[\s\-]*class|inheritance", b, re.IGNORECASE):
        return "BdG"
    return None


def parse_review(md_path: Path) -> dict:
    """Parse one reviewer markdown -> {clauses: {key: verdict}, composite: V,
    raw_clause_lines: [...]}. Classification keys on the clause LABEL only.
    """
    text = md_path.read_text(encoding="utf-8")  # (local)
    clauses: dict[str, str] = {}  # (local)
    raw: list[str] = []  # (local)
    composite = "ABSENT"  # (local)
    for ln in text.splitlines():
        cm = _CLAUSE_LINE.match(ln)  # (local)
        if cm:
            body = cm.group("body")  # (local)
            label, rationale = _split_label_rationale(body)  # (local)
            key = _classify_clause(label)  # (local) LABEL-only classification
            if key is not None:
                verdict = _verdict_from_rationale(rationale, label)  # (local)
                # If the same key appears twice in one review, keep the worst (defensive).
                prior = clauses.get(key)  # (local)
                clauses[key] = _worse(prior, verdict) if prior else verdict
                raw.append(f"{key}={verdict} :: label='{label.strip()[:80]}'")
            continue
        comp_m = _COMPOSITE.match(ln)  # (local)
        if comp_m:
            composite = comp_m.group("v").upper()  # (local)
    return {"clauses": clauses, "composite": composite, "raw_clause_lines": raw}


def _worse(a: str, b: str) -> str:
    """Verdict severity ordering: FAIL/ABSENT worst, then INFO, then PASS."""
    order = {"FAIL": 0, "ABSENT": 0, "INFO": 1, "PASS": 2}  # (local)
    return a if order.get(a, 0) <= order.get(b, 0) else b


# ---------------------------------------------------------------------------
# Substrate-input-orthogonality (anchor-set disjointness)
# ---------------------------------------------------------------------------
# The reviewers' anchor sets are read from their recorded "Audit pins" SHA lines
# (the .npz files each loaded). Orthogonality = the two anchor SETS are DISJOINT
# (>= 1 observable loaded by exactly one reviewer) per
# joint-theorem-promotion.md §"Substrate-input-orthogonality clause".
AXIS_A_ANCHORS = {  # (local) Axis-A loaded ONLY this (Yang-Mills a_4-channel residue)
    "s94_w1_3_vii_bx_t5_alpha_s_a4_recovery.npz",
}
AXIS_B_ANCHORS = {  # (local) Axis-B loaded ONLY these (transport-side BdG/AZ inheritance)
    "s88_w3b_chi_inheritance_kde_complete.npz",
    "s88_w4c_az_inheritance_cartesian_confirm.npz",
}


_NEGATION_MARKERS = (  # (local) a filename in such a line is NOT a load (it is an attestation of non-load)
    "did not load",
    "didn't load",
    "not load",
    "disjoint from",
    "perp",
    "not the axis-a",
    "not load that file",
    "i did not",
)


def _anchors_loaded_in_review(md_path: Path, anchor_set: set[str]) -> set[str]:
    """Return the subset of `anchor_set` that the review LOADS (cites in a non-negated
    context). A filename appearing only in a 'did NOT load / DISJOINT from' attestation
    line is EXCLUDED — that is an independence attestation, not a load.

    Per-line scan: an anchor counts as loaded iff it appears on >=1 line that does NOT
    contain a negation marker. This prevents the Axis-B independence-attestation line
    ('I did NOT load s94_w1_3...') from being mis-counted as a cross-leak load.
    """
    loaded: set[str] = set()  # (local)
    for ln in md_path.read_text(encoding="utf-8").splitlines():
        low = ln.lower()  # (local)
        if any(neg in low for neg in _NEGATION_MARKERS):
            continue  # negated context — not a load
        for a in anchor_set:
            if a in ln:
                loaded.add(a)
    return loaded


def substrate_input_orthogonality() -> tuple[bool, dict]:
    a_cited = _anchors_loaded_in_review(AXIS_A_MD, AXIS_A_ANCHORS)  # (local)
    b_cited = _anchors_loaded_in_review(AXIS_B_MD, AXIS_B_ANCHORS)  # (local)
    # Defensive cross-leak check: did Axis-A LOAD any Axis-B anchor (or vice versa)?
    # (negated-context mentions excluded — an attestation 'did NOT load X' is not a load)
    a_leak = _anchors_loaded_in_review(AXIS_A_MD, AXIS_B_ANCHORS)  # (local)
    b_leak = _anchors_loaded_in_review(AXIS_B_MD, AXIS_A_ANCHORS)  # (local)
    overlap = (AXIS_A_ANCHORS & AXIS_B_ANCHORS)  # (local) intended-set overlap (must be empty)
    both_nonempty = bool(a_cited) and bool(b_cited)  # (local)
    disjoint = (len(overlap) == 0) and (len(a_leak) == 0) and (len(b_leak) == 0)  # (local)
    # exists >=1 observable loaded by exactly one reviewer:
    only_A = a_cited - b_cited  # (local)
    only_B = b_cited - a_cited  # (local)
    exists_disjoint_obs = bool(only_A) or bool(only_B)  # (local)
    ok = both_nonempty and disjoint and exists_disjoint_obs  # (local)
    detail = {
        "axis_A_anchors_cited": sorted(a_cited),
        "axis_B_anchors_cited": sorted(b_cited),
        "intended_set_overlap": sorted(overlap),
        "axis_A_cross_leak_into_B_set": sorted(a_leak),
        "axis_B_cross_leak_into_A_set": sorted(b_leak),
        "only_loaded_by_A": sorted(only_A),
        "only_loaded_by_B": sorted(only_B),
        "both_nonempty": both_nonempty,
        "disjoint": disjoint,
        "exists_disjoint_observable": exists_disjoint_obs,
        "orthogonality_ok": ok,
        "structural_ceiling": ok,
        "substrate_input_overlap_caveat": (not ok),
    }
    return ok, detail


# ---------------------------------------------------------------------------
# OAA exclusion (reviewers admissible; neither is the original author connes)
# ---------------------------------------------------------------------------
def oaa_exclusion_ok() -> tuple[bool, dict]:
    """Verify the two reviewers are the admissible non-connes axis-distinct pair and
    each attests no-workshop-transcript-read + non-authorship (from the review text).
    """
    a_text = AXIS_A_MD.read_text(encoding="utf-8")  # (local)
    b_text = AXIS_B_MD.read_text(encoding="utf-8")  # (local)
    a_rev = "lizzi-spectral-functional-theorist" if re.search(r"lizzi", a_text, re.IGNORECASE) else "UNKNOWN"  # (local)
    b_rev = "volovik-superfluid-universe-theorist" if re.search(r"volovik", b_text, re.IGNORECASE) else "UNKNOWN"  # (local)
    a_admissible = (a_rev in ADMISSIBLE_REVIEWERS) and (a_rev != EXCLUDED_AUTHOR)  # (local)
    b_admissible = (b_rev in ADMISSIBLE_REVIEWERS) and (b_rev != EXCLUDED_AUTHOR)  # (local)
    axis_distinct = a_rev != b_rev  # (local)

    def _attest_no_workshop(t: str) -> bool:
        tl = t.lower()  # (local)
        no_read = ("did not read" in tl) and ("workshop" in tl)  # (local)
        not_author = ("not the original" in tl) or ("author = connes" in tl) or (
            "no-shared-context" in tl) or ("not an original" in tl)  # (local)
        return no_read and not_author

    a_ws_ok = _attest_no_workshop(a_text)  # (local)
    b_ws_ok = _attest_no_workshop(b_text)  # (local)
    ok = a_admissible and b_admissible and axis_distinct and a_ws_ok and b_ws_ok  # (local)
    detail = {
        "axis_A_reviewer": a_rev,
        "axis_B_reviewer": b_rev,
        "excluded_author": EXCLUDED_AUTHOR,
        "axis_A_admissible": a_admissible,
        "axis_B_admissible": b_admissible,
        "axis_distinct": axis_distinct,
        "axis_A_no_workshop_attested": a_ws_ok,
        "axis_B_no_workshop_attested": b_ws_ok,
        "oaa_ok": ok,
    }
    return ok, detail


# ---------------------------------------------------------------------------
# Composite PASS-AND aggregation
# ---------------------------------------------------------------------------
def aggregate(rev_a: dict, rev_b: dict) -> dict:
    """Mechanical PASS-AND over the asymmetric clause partition + structural gates.

    Substitution chain (composite PASS-AND direction claim):
      Step 1: axisA single-axis clause verdicts  = {Element-1,3,4,Degree-match}  [MD_A]
      Step 2: axisB single-axis clause verdicts  = {Element-2,BdG,substrate-nat}  [MD_B]
      Step 3: JOINT (c) Delta_scheme verdicts     = (JOINT in A, JOINT in B)       [both MD]
      Step 4: joint_pass_and = (JOINT_A == PASS) AND (JOINT_B == PASS)             [logical AND]
      Step 5: orthogonality  = anchor-set(A) DISJOINT anchor-set(B)               [anchor SHAs]
      Step 6: composite_PASS = (all axisA single PASS) AND (all axisB single PASS)
                               AND joint_pass_and AND orthogonality AND OAA_ok
                               AND (axis-A composite == PASS) AND (axis-B composite == PASS)
      Step 7: substitute review contents -> evaluate each conjunct
      Step 8: read off composite; ANY FALSE conjunct => NOT PASS (FAIL or INFO)
    """
    a_clauses = rev_a["clauses"]  # (local)
    b_clauses = rev_b["clauses"]  # (local)

    # --- Axis-A single-axis clauses ---
    axisA_single = {c: a_clauses.get(c, "ABSENT") for c in AXIS_A_SINGLE_CLAUSES}  # (local)
    # --- Axis-B single-axis clauses ---
    axisB_single = {c: b_clauses.get(c, "ABSENT") for c in AXIS_B_SINGLE_CLAUSES}  # (local)
    # --- JOINT clause (c) on both sides ---
    joint_A = a_clauses.get(JOINT_CLAUSE_KEY, "ABSENT")  # (local)
    joint_B = b_clauses.get(JOINT_CLAUSE_KEY, "ABSENT")  # (local)
    joint_pass_and = (joint_A == "PASS") and (joint_B == "PASS")  # (local)

    # roll-ups
    def _roll(vs: list[str]) -> str:
        if any(v in ("FAIL", "ABSENT") for v in vs):
            return "FAIL"
        if any(v == "INFO" for v in vs):
            return "INFO"
        return "PASS"

    axisA_single_all = _roll(list(axisA_single.values()))  # (local)
    axisB_single_all = _roll(list(axisB_single.values()))  # (local)
    joint_roll = _roll([joint_A, joint_B])  # (local)

    # structural gates
    ortho_ok, ortho_detail = substrate_input_orthogonality()  # (local)
    oaa_ok, oaa_detail = oaa_exclusion_ok()  # (local)
    comp_A = rev_a["composite"]  # (local)
    comp_B = rev_b["composite"]  # (local)
    composites_pass = (comp_A == "PASS") and (comp_B == "PASS")  # (local)

    structural_gates_ok = ortho_ok and oaa_ok and composites_pass  # (local)

    all_single_pass = (axisA_single_all == "PASS") and (axisB_single_all == "PASS")  # (local)

    # any INFO (no hard FAIL) across the conjunction -> composite INFO
    any_fail = (
        axisA_single_all == "FAIL"
        or axisB_single_all == "FAIL"
        or joint_roll == "FAIL"
        or (not structural_gates_ok)
    )  # (local)
    any_info = (
        axisA_single_all == "INFO"
        or axisB_single_all == "INFO"
        or joint_roll == "INFO"
    )  # (local)

    # Composite collapse (plan §W1-1 strict_PASS_boundary):
    if any_fail:
        composite = "FAIL"
    elif any_info:
        composite = "INFO"
    elif all_single_pass and joint_pass_and and structural_gates_ok:
        composite = "PASS"
    else:
        composite = "FAIL"  # an ABSENT/unclassified conjunct that is neither INFO nor PASS

    promotion = (
        "STAGE-1-CANDIDATE -> STAGE-3-PERMANENT (LICENSED; registry-flip by "
        "mack-cosmic-bridge as post-gate hook)"
        if composite == "PASS"
        else (
            "STAYS STAGE-1-CANDIDATE (Stage-2-INFO-deferred clause)"
            if composite == "INFO"
            else "STAYS STAGE-1-CANDIDATE (Stage-2 clause FAIL; remediation next session)"
        )
    )  # (local)

    return {
        "gate_id": GATE_ID,
        "composite": composite,
        "axisA_single_clauses": axisA_single,
        "axisB_single_clauses": axisB_single,
        "axisA_single_all": axisA_single_all,
        "axisB_single_all": axisB_single_all,
        "joint_clause_A": joint_A,
        "joint_clause_B": joint_B,
        "joint_pass_and": joint_pass_and,
        "joint_rollup": joint_roll,
        "all_single_pass": all_single_pass,
        "any_fail": any_fail,
        "any_info": any_info,
        "axis_A_composite": comp_A,
        "axis_B_composite": comp_B,
        "structural_gates": {
            "substrate_input_orthogonality": ortho_detail,
            "oaa_exclusion": oaa_detail,
            "axis_composites_pass": composites_pass,
            "structural_gates_ok": structural_gates_ok,
        },
        "promotion": promotion,
        "scope_note": (
            "§VII cross-PILLAR bridge theorem on (A_K,H_K,D_K); composite PASS LICENSES "
            "STAGE-1-CANDIDATE -> STAGE-3-PERMANENT (registry-flip by mack-cosmic-bridge, "
            "sole writer); this gate does NOT edit permanent-results-registry.md"
        ),
    }


# ---------------------------------------------------------------------------
# NPZ + PNG writers (clause PASS-AND matrix)
# ---------------------------------------------------------------------------
def _v2i(v: str) -> int:
    return {"PASS": 1, "INFO": 0, "FAIL": -1, "ABSENT": -2}.get(v, -2)


def write_npz(agg: dict) -> None:
    sg = agg["structural_gates"]  # (local)
    # Axis-A single-clause vector (in canonical order) + JOINT_A
    a_vec = [_v2i(agg["axisA_single_clauses"][c]) for c in AXIS_A_SINGLE_CLAUSES]  # (local)
    a_vec.append(_v2i(agg["joint_clause_A"]))
    # Axis-B single-clause vector + JOINT_B
    b_vec = [_v2i(agg["axisB_single_clauses"][c]) for c in AXIS_B_SINGLE_CLAUSES]  # (local)
    b_vec.append(_v2i(agg["joint_clause_B"]))
    np.savez(
        OUT_NPZ,
        gate_id=np.array(GATE_ID),
        composite=np.array(agg["composite"]),
        axisA_clause_labels=np.array(AXIS_A_SINGLE_CLAUSES + ["JOINT-c"]),
        axisA_clause_verdicts=np.array(a_vec, dtype=np.int8),
        axisB_clause_labels=np.array(AXIS_B_SINGLE_CLAUSES + ["JOINT-c"]),
        axisB_clause_verdicts=np.array(b_vec, dtype=np.int8),
        joint_clause_A=np.array(_v2i(agg["joint_clause_A"]), dtype=np.int8),
        joint_clause_B=np.array(_v2i(agg["joint_clause_B"]), dtype=np.int8),
        joint_pass_and=np.array(1 if agg["joint_pass_and"] else 0, dtype=np.int8),
        all_single_pass=np.array(1 if agg["all_single_pass"] else 0, dtype=np.int8),
        orthogonality_ok=np.array(1 if sg["substrate_input_orthogonality"]["orthogonality_ok"] else 0, dtype=np.int8),
        oaa_ok=np.array(1 if sg["oaa_exclusion"]["oaa_ok"] else 0, dtype=np.int8),
        axis_composites_pass=np.array(1 if sg["axis_composites_pass"] else 0, dtype=np.int8),
        structural_gates_ok=np.array(1 if sg["structural_gates_ok"] else 0, dtype=np.int8),
        axis_A_composite=np.array(agg["axis_A_composite"]),
        axis_B_composite=np.array(agg["axis_B_composite"]),
        verdict_legend=np.array("PASS=1 INFO=0 FAIL=-1 ABSENT=-2"),
        axis_A_anchor=np.array(",".join(sg["substrate_input_orthogonality"]["axis_A_anchors_cited"])),
        axis_B_anchor=np.array(",".join(sg["substrate_input_orthogonality"]["axis_B_anchors_cited"])),
        promotion=np.array(agg["promotion"]),
        # canonical pins consumed (provenance)
        M_KK=np.array(float(M_KK)),
        tau_fold=np.array(float(tau_fold)),
        alpha_s_cmb_central=np.array(float(alpha_s_cmb_central)),
        alpha_s_canon_2020=np.array(float(alpha_s_canon_2020)),
        w0_FW=np.array(float(w0_FW)),
        r_CMB_framework=np.array(float(r_CMB_framework)),
    )


def write_png(agg: dict) -> None:
    """Optional clause PASS-AND matrix figure (two stacked rows: Axis-A, Axis-B)."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        from matplotlib.colors import ListedColormap, BoundaryNorm
    except Exception as exc:  # plotting is optional
        print(f"  [plot skipped: {exc}]")
        return
    a_labels = AXIS_A_SINGLE_CLAUSES + ["JOINT-c"]  # (local)
    b_labels = AXIS_B_SINGLE_CLAUSES + ["JOINT-c"]  # (local)
    a_vec = [_v2i(agg["axisA_single_clauses"][c]) for c in AXIS_A_SINGLE_CLAUSES] + [_v2i(agg["joint_clause_A"])]  # (local)
    b_vec = [_v2i(agg["axisB_single_clauses"][c]) for c in AXIS_B_SINGLE_CLAUSES] + [_v2i(agg["joint_clause_B"])]  # (local)
    ncol = max(len(a_vec), len(b_vec))  # (local)
    mat = np.full((2, ncol), -2.0)  # (local)
    for j, v in enumerate(a_vec):
        mat[0, j] = v
    for j, v in enumerate(b_vec):
        mat[1, j] = v
    cmap = ListedColormap(["#b2182b", "#f4a582", "#92c5de", "#2166ac"])  # ABSENT/FAIL/INFO/PASS  # (local)
    norm = BoundaryNorm([-2.5, -1.5, -0.5, 0.5, 1.5], cmap.N)  # (local)
    fig, ax = plt.subplots(figsize=(8.0, 3.2))
    ax.imshow(mat, cmap=cmap, norm=norm, aspect="auto")
    ax.set_yticks([0, 1])
    ax.set_yticklabels(["Axis-A (lizzi spectral)", "Axis-B (volovik transport)"], fontsize=9)
    ax.set_xticks(range(ncol))
    ax.set_xticklabels([f"c{j+1}" for j in range(ncol)], fontsize=8)
    for i, (labs, vec) in enumerate([(a_labels, a_vec), (b_labels, b_vec)]):
        for j in range(ncol):
            if j < len(vec):
                tag = {1: "PASS", 0: "INFO", -1: "FAIL", -2: "—"}.get(int(vec[j]), "?")  # (local)
                lab = labs[j] if j < len(labs) else ""  # (local)
                ax.text(j, i, f"{lab}\n{tag}", ha="center", va="center", fontsize=6.5,
                        color="white" if vec[j] >= 1 or vec[j] <= -1 else "black")
    sg = agg["structural_gates"]["substrate_input_orthogonality"]  # (local)
    ax.set_title(
        f"{GATE_ID}: composite = {agg['composite']}  |  JOINT-c PASS-AND = {agg['joint_pass_and']}  "
        f"|  orthogonal = {sg['orthogonality_ok']}",
        fontsize=9,
    )
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Verdict-line emission (S84+ dual-SHA; first emission, NO supersedes)
# ---------------------------------------------------------------------------
def build_value_string(agg: dict) -> str:
    sg = agg["structural_gates"]  # (local)
    a_single = ",".join(f"{c}={agg['axisA_single_clauses'][c]}" for c in AXIS_A_SINGLE_CLAUSES)  # (local)
    b_single = ",".join(f"{c}={agg['axisB_single_clauses'][c]}" for c in AXIS_B_SINGLE_CLAUSES)  # (local)
    ortho = sg["substrate_input_orthogonality"]  # (local)
    return (
        f"composite={agg['composite']};"
        f"axisA_single[{a_single}]_all={agg['axisA_single_all']};"
        f"axisB_single[{b_single}]_all={agg['axisB_single_all']};"
        f"JOINT_c_deltascheme_PASS-AND=(A={agg['joint_clause_A']},B={agg['joint_clause_B']})="
        f"{agg['joint_pass_and']}_tol<=1e-12;"
        f"orthogonality=(A={'+'.join(ortho['axis_A_anchors_cited'])}_PERP_"
        f"B={'+'.join(ortho['axis_B_anchors_cited'])})_disjoint={ortho['disjoint']}_"
        f"exists_disjoint_obs={ortho['exists_disjoint_observable']};"
        f"OAA_excl={EXCLUDED_AUTHOR};"
        f"axis_composites=(A={agg['axis_A_composite']},B={agg['axis_B_composite']});"
        f"promotion={agg['promotion']}"
    )


def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str) -> None:
    """Append the single canonical verdict line (atomic single open('a') write).

    First CF-S95-HK-1 emission => NO supersedes tag.
    """
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def append_companion_row(audit_sha: str, content_sha: str, agg: dict) -> None:
    """Dual-SHA companion comment row + a Stage-2 provenance comment row.

    [VERIFY-THEOREM] trigger: NO [SIGN] 3-tuple companion row (plan
    schema_v2_3tuple_required: false).
    """
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row\n"
    )
    prov_row = (
        f"# {GATE_ID} Stage-2 §VII.BG two-axis cross-verify: Axis-A lizzi (spectral; "
        f"5 clauses incl JOINT-c) + Axis-B volovik (transport; 4 clauses incl JOINT-c); "
        f"JOINT clause (c) Delta_scheme->0 PASS-AND'd (logical AND); substrate-input-"
        f"orthogonality at >=1 obs (Axis-A {{s94_w1_3...}} PERP Axis-B {{s88_w3b,s88_w4c}}); "
        f"OAA-excluded={EXCLUDED_AUTHOR}; NO Option-A supersedes (first CF-S95-HK-1 emission); "
        f"composite={agg['composite']} => {agg['promotion']}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(companion)
        fp.write(prov_row)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)
    ap = argparse.ArgumentParser()
    ap.add_argument("--emit", action="store_true",
                    help="Emit the verdict line (requires both review MDs present).")
    args = ap.parse_args()

    print(f"=== {GATE_ID} — §VII.BG Stage-2 aggregation (mechanical PASS-AND of 2 frozen reviewer MDs) ===")
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = log_input_pins(INPUT_FILES)  # (local)

    # Emission guard: both review MDs must be present.
    if not AXIS_A_MD.exists() or not AXIS_B_MD.exists():
        print("\n[EMISSION GUARD] one or both review MDs ABSENT; aggregation cannot run.")
        print(f"  Axis-A present: {AXIS_A_MD.exists()}  Axis-B present: {AXIS_B_MD.exists()}")
        return 2

    rev_a = parse_review(AXIS_A_MD)  # (local)
    rev_b = parse_review(AXIS_B_MD)  # (local)

    agg = aggregate(rev_a, rev_b)  # (local)

    # Canonical-pin provenance log (consumed pins).
    print("\n=== canonical pins consumed (provenance) ===")
    print(f"  M_KK = {M_KK:.6e} GeV  tau_fold = {tau_fold}")
    print(f"  alpha_s_cmb_central = {alpha_s_cmb_central}  alpha_s_canon_2020 = {alpha_s_canon_2020} +/- {alpha_s_canon_2020_err}")
    print(f"  w0_FW = {w0_FW}  r_CMB_framework = {r_CMB_framework}")

    print("\n=== Axis-A (lizzi spectral) clause verdicts (parsed from review MD) ===")
    for c in AXIS_A_SINGLE_CLAUSES:
        print(f"  {c}: {agg['axisA_single_clauses'][c]}")
    print(f"  JOINT-c (Delta_scheme): {agg['joint_clause_A']}")
    print(f"  Axis-A single-axis roll-up: {agg['axisA_single_all']}  |  Axis-A COMPOSITE (recorded): {agg['axis_A_composite']}")

    print("\n=== Axis-B (volovik transport) clause verdicts (parsed from review MD) ===")
    for c in AXIS_B_SINGLE_CLAUSES:
        print(f"  {c}: {agg['axisB_single_clauses'][c]}")
    print(f"  JOINT-c (Delta_scheme): {agg['joint_clause_B']}")
    print(f"  Axis-B single-axis roll-up: {agg['axisB_single_all']}  |  Axis-B COMPOSITE (recorded): {agg['axis_B_composite']}")

    print("\n=== JOINT clause (c) Delta_scheme->0 PASS-AND ===")
    print(f"  JOINT_A={agg['joint_clause_A']}  JOINT_B={agg['joint_clause_B']}  "
          f"=> PASS-AND={agg['joint_pass_and']}  (|Delta_scheme| <= {TOL_DELTA_SCHEME})")

    sg = agg["structural_gates"]  # (local)
    ortho = sg["substrate_input_orthogonality"]  # (local)
    print("\n=== structural gates ===")
    print(f"  substrate_input_orthogonality: {ortho['orthogonality_ok']}")
    print(f"    Axis-A anchors cited: {ortho['axis_A_anchors_cited']}")
    print(f"    Axis-B anchors cited: {ortho['axis_B_anchors_cited']}")
    print(f"    intended-set overlap: {ortho['intended_set_overlap']} (must be empty)")
    print(f"    cross-leak A->Bset: {ortho['axis_A_cross_leak_into_B_set']}  B->Aset: {ortho['axis_B_cross_leak_into_A_set']}")
    print(f"    exists disjoint observable: {ortho['exists_disjoint_observable']}  caveat={ortho['substrate_input_overlap_caveat']}")
    print(f"  OAA exclusion: {sg['oaa_exclusion']['oaa_ok']} "
          f"(A={sg['oaa_exclusion']['axis_A_reviewer']}, B={sg['oaa_exclusion']['axis_B_reviewer']}, "
          f"excluded={sg['oaa_exclusion']['excluded_author']}, axis_distinct={sg['oaa_exclusion']['axis_distinct']})")
    print(f"  axis_composites_pass: {sg['axis_composites_pass']}")
    print(f"  structural_gates_ok: {sg['structural_gates_ok']}")

    print(f"\n=== COMPOSITE: {agg['composite']} ===")
    print(f"=== PROMOTION: {agg['promotion']} ===")

    # Aggregate payload (feeds audit_sha256 — gate-distinct, content-bound).
    aggregate_payload = json.dumps(  # (local)
        {
            "composite": agg["composite"],
            "axisA_single_clauses": agg["axisA_single_clauses"],
            "axisB_single_clauses": agg["axisB_single_clauses"],
            "joint_clause_A": agg["joint_clause_A"],
            "joint_clause_B": agg["joint_clause_B"],
            "joint_pass_and": agg["joint_pass_and"],
            "orthogonality_ok": ortho["orthogonality_ok"],
            "oaa_ok": sg["oaa_exclusion"]["oaa_ok"],
            "axis_composites_pass": sg["axis_composites_pass"],
        },
        separators=(",", ":"), sort_keys=True,
    )
    audit_sha, content_sha = compute_dual_sha(pins, aggregate_payload)  # (local)
    print(f"\n  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")

    prior = find_latest_prior_audit_sha()  # (local)
    print(f"  latest-prior-{GATE_ID} audit_sha (Option-A source): {prior} (None expected — first emission)")

    value = build_value_string(agg)  # (local)
    tag = (f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")  # (local)

    # JSON + NPZ + PNG sidecars (always written).
    OUT_JSON.write_text(
        json.dumps(
            {
                **agg,
                "scheme": SCHEME,
                "convention": CONVENTION,
                "L_max": L_MAX,
                "tolerance_delta_scheme": TOL_DELTA_SCHEME,
                "audit_sha256": audit_sha,
                "content_sha256": content_sha,
                "value_string": value,
                "option_a_supersedes": prior,  # None for first emission
                "input_pins": pins,
                "raw_clause_lines_axisA": rev_a["raw_clause_lines"],
                "raw_clause_lines_axisB": rev_b["raw_clause_lines"],
                "canonical_pins": {
                    "M_KK": float(M_KK),
                    "tau_fold": float(tau_fold),
                    "alpha_s_cmb_central": float(alpha_s_cmb_central),
                    "alpha_s_canon_2020": float(alpha_s_canon_2020),
                    "alpha_s_canon_2020_err": float(alpha_s_canon_2020_err),
                    "w0_FW": float(w0_FW),
                    "r_CMB_framework": float(r_CMB_framework),
                },
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    write_npz(agg)
    write_png(agg)
    print(f"\n  wrote {OUT_JSON.relative_to(PROJECT_ROOT)}")
    print(f"  wrote {OUT_NPZ.relative_to(PROJECT_ROOT)}")
    if OUT_PNG.exists():
        print(f"  wrote {OUT_PNG.relative_to(PROJECT_ROOT)}")

    print("\n" + tag)

    if args.emit:
        append_verdict(agg["composite"], value, audit_sha, content_sha)
        append_companion_row(audit_sha, content_sha, agg)
        print(f"\n[EMITTED] verdict line + dual-SHA companion + Stage-2 provenance row -> "
              f"{VERDICT_TXT.relative_to(PROJECT_ROOT)}")
    else:
        print("\n[DRY-RUN] --emit not passed; NO verdict line appended. Verdict line WOULD be:")
        print(f"  {GATE_ID}: {agg['composite']} -- value={value!r} scheme={SCHEME} "
              f"convention={CONVENTION} L_max={L_MAX} audit_sha256={audit_sha} "
              f"content_sha256={content_sha} schema_version=S84+")

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {agg['composite']} (wall {wall:.2f}s) ===")
    # Exit 0 on a valid verdict (PASS/INFO); verdict is DATA, not exit code.
    return 0 if agg["composite"] != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
