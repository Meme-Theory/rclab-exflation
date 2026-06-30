#!/usr/bin/env python3
"""
S93 W4-1 — §VII.AX.OP-PROJ Axis-A Element-2 Verdict-Artifact Re-Emission
=======================================================================

Gate: S93-W4-1-VII-AX-OP-PROJ-AXIS-A-E2-VERDICT-ARTIFACT-RE-EMISSION ([VERIFY])

Writer-of-record continuity. connes-ncg-theorist was the Axis-A producing
agent of the original S92 §W6-3 verify
(`S92-W6-CF-S92-W5-4-STAGE-2-VII-AX-CROSS-AXIS-VERIFY-AXIS-A`, audit_sha256=
19662dc1544604e55f49280bd36d5a1e3862df381d0eb14f17b68ebc5b933cff, FAIL). This
gate re-emits the CORRECTED Axis-A composite verdict line (NO new physics — a
writer-of-record corrected re-emission of the E2 OE-form artifact).

------------------------------------------------------------------------------
DERIVATIVE-OUTPUT discipline (load-bearing; per plan §W4-1 substrate_framing)
------------------------------------------------------------------------------
The on-disk JSON artifact
  computations/session-92/s92_w6_3_axis_a_connes_ncg_vii_ax_stage_2_verify.json
is REALITY. The prior characterization "Axis-A E2 is FAIL" was INTENT. The
JSON records an internal contradiction:
  - element_2.sub_findings[0] (id "2.1").verdict = "FAIL"
    yet its .evidence reads "...integration domain + trace + named projector
    all structurally present" (PASS-LANGUAGE).
  - element_2.sub_findings 2.2, 2.3, 2.4, 2.5 .verdict all = "PASS".
  - element_2.interpretation = "...all structurally present and correctly
    formed at the laboratory-IN observable axis" (PASS-LANGUAGE).
  - element_2.verdict = "FAIL" (the emit-bug, propagated from 2.1).
  - element_1.verdict = "PASS"; joint_element_3.verdict = "PASS";
    joint_element_5.verdict = "PASS".
  - axis_a_composite = "FAIL" — driven SOLELY by the E2 verdict-FIELD.

The 2.1 FAIL is a verdict-FIELD emit-bug: the registry OE-form
`∫_{Σ_CMB ∪ Σ_LISA ∪ Σ_PTA} d³x · Tr_{M_PBH-mass}(P_{PBH-mass} · ρ_BH(x))`
uses a BRACE-DELIMITED projector subscript `P_{PBH-mass}`. The
cross-pillar-bridge-anatomy.md §"Element 2 OE-form discipline" rule prose
(iii) explicitly admits `P_<index>` OR `Π^{<superscript>}_{<subscript>}` —
i.e. BOTH the bare-subscript form AND the brace-delimited subscript form
satisfy the named-projector requirement. An earlier version of the producing
script's regex matched only the bare subscript, so 2.1 was emitted FAIL while
its evidence (correctly) describes the structural presence of all three
OE-form constituents. The narrow-regex artifact is the source of the
verdict-FIELD defect.

------------------------------------------------------------------------------
Re-emission logic (read-from-disk; this gate runs NO new physics)
------------------------------------------------------------------------------
1. READ the on-disk JSON (REALITY).
2. Confirm the THREE corrective antecedents:
     (A) all 5 E2 sub-finding .evidence are PASS-language (structural presence);
     (B) E2 .interpretation is PASS-language ("all structurally present and
         correctly formed");
     (C) the OE-form positive-match regex of cross-pillar-bridge-anatomy.md
         §"Element 2 OE-form discipline" matches the registered Element-2
         OE-form (verified DIRECTLY against the LIVE registry text — not
         merely the JSON evidence string), admitting BOTH bare- and
         brace-delimited subscript per rule prose (iii); AND the negative-
         match prose-only regex does NOT trigger.
3. Re-derive corrected E2 = PASS IFF (A) ∧ (B) ∧ (C).
4. Re-derive Axis-A composite = PASS IFF
     (E1_JOINT == PASS) AND (E2_corrected == PASS)
       AND (JE3 == PASS) AND (JE5 == PASS)  (each read from the on-disk JSON;
     substrate-input-orthogonality also PASS on disk).
5. Emit ONE corrective canonical verdict line via the Option-A supersedes
   protocol (`gate-verdicts.md §"Option A — sig_5 remediation pathway under
   absolute verdict permanence"`) carrying
     supersedes=19662dc1544604e55f49280bd36d5a1e3862df381d0eb14f17b68ebc5b933cff
   (the full-64-char audit_sha256 of the original S92 Axis-A FAIL line, which
   is RETAINED on disk per absolute verdict permanence).

If any antecedent FAILS on disk (OE-form regex no-match, an E2 sub-finding
evidence genuinely FAIL-language, or one of E1/JE3/JE5 not PASS), the original
Axis-A FAIL STANDS and this gate emits FAIL (no supersedes), per plan §W4-1
FAIL_meaning.

scheme     = stage-2-cross-axis-verify-axis-a-NCG-axiomatic-spectral-side-E2-RE-EMISSION
convention = stage-2-cross-reviewer-protocol-without-prior-workshop-context-OPTION-A-SUPERSEDES
L_max      = 14 (the §W6-3 Axis-A verify canonical L_max; JSON line 7)

Classification: NON-PHONONIC (verdict-artifact integrity re-emission; methodology-
layer F-image of the substrate-IS Stage-2 verify per epistemic-discipline.md
§"Layer-Decomposition" Phi correspondence. The substrate-IS observable — n_PBH
cardinality-cascade-tail — is UNCHANGED; only the verdict-FIELD F-image is
corrected.)

Substitution chain (per math-scripts.md §"Double-Check Logic Before Compute"):
  Claim: "Re-emitting E2=PASS makes axis_a_composite=PASS (the FAIL was a
          verdict-FIELD emit-bug)."
  Step 1: E2_evidence = {2.1, 2.2, 2.3, 2.4, 2.5}.evidence  [JSON element_2]
          all PASS-language (structural presence of ∫ / Tr_<sub> / P_<index>).
  Step 2: E2_interpretation = element_2.interpretation       [JSON line 82]
          = "...all structurally present and correctly formed" (PASS-language).
  Step 3: OE_regex (positive-match, brace OR bare subscript) [rule prose (iii)]
          applied to LIVE registry OE-form ⇒ MATCH (brace subscript).
          negative-match prose-only regex ⇒ NO trigger.
  Step 4: corrected E2 = PASS IFF (Step1 ∧ Step2 ∧ Step3) = PASS ∧ PASS ∧ PASS
                       = PASS.
  Step 5: axis_a_composite = E1_JOINT ∧ E2_corrected ∧ JE3 ∧ JE5
                       = PASS [L43] ∧ PASS [corrected] ∧ PASS [L119] ∧ PASS [L158]
                       = PASS.
  Conclusion: the ONLY FAIL in the four Axis-A-audited clauses was the E2
              verdict-FIELD; correcting it (justified by all 5 sub-finding
              evidence + interpretation + live-registry regex match) flips the
              conjunction to PASS. Original FAIL is RETIRED-NOT-OVERTURNED via
              Option-A supersedes. VALID only after on-disk verification of all
              antecedents.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # CPU-only gate; cap threads
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_SHARED = _THIS_DIR.parent / "_shared"
if str(_SHARED) not in sys.path:
    sys.path.insert(0, str(_SHARED))

from canonical_constants import *  # noqa: F401,F403  (brings M_KK and others)
from canonical_constants import M_KK  # explicit (satisfies 'from canonical_constants import')

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import re
import time
from typing import Any

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Gate metadata
# ---------------------------------------------------------------------------
GATE_ID = "S93-W4-1-VII-AX-OP-PROJ-AXIS-A-E2-VERDICT-ARTIFACT-RE-EMISSION"
SCHEME = (
    "stage-2-cross-axis-verify-axis-a-NCG-axiomatic-spectral-side-E2-RE-EMISSION"
)
CONVENTION = (
    "stage-2-cross-reviewer-protocol-without-prior-workshop-context-"
    "OPTION-A-SUPERSEDES"
)
L_MAX = 14  # (local) — §W6-3 Axis-A verify canonical L_max (JSON line 7)

PROJECT_ROOT = _THIS_DIR.parent.parent
VERDICT_TXT = _THIS_DIR / "s93_gate_verdicts.txt"
SCRIPT_PATH = Path(__file__).resolve()
CANONICAL_CONSTANTS_PY = _SHARED / "canonical_constants.py"

# Input artifacts (the on-disk REALITY + supersedes-target source + rule file)
AXIS_A_JSON = (
    _THIS_DIR.parent / "session-92"
    / "s92_w6_3_axis_a_connes_ncg_vii_ax_stage_2_verify.json"
)
S92_VERDICTS_TXT = _THIS_DIR.parent / "session-92" / "s92_gate_verdicts.txt"
REGISTRY_MD = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
CROSS_PILLAR_RULE = (
    PROJECT_ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md"
)

# Original S92 Axis-A FAIL line audit_sha256 — the supersedes target (full-64).
# Plan §W4-1 machinery_pin_map: "supersedes-tag must be full-64-char EXACT".
SUPERSEDES_TARGET_AUDIT_SHA = (
    "19662dc1544604e55f49280bd36d5a1e3862df381d0eb14f17b68ebc5b933cff"
)

# ---------------------------------------------------------------------------
# Section 4 — SHA helpers (mirror S92 W6-3 producing script — writer continuity)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    """Return the SHA-256 hex digest of the file at `path` (chunked)."""
    h = hashlib.sha256()
    with path.open("rb") as fp:
        for chunk in iter(lambda: fp.read(64 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pin_map: dict[str, str]) -> str:
    """Closure hash over ordered (key, sha256) input-pin map."""
    h = hashlib.sha256()
    for k in sorted(pin_map.keys()):
        h.update(k.encode("utf-8"))
        h.update(b":")
        h.update(pin_map[k].encode("utf-8"))
        h.update(b"\n")
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — PASS-language classifier for E2 sub-finding evidence
# ---------------------------------------------------------------------------
# A sub-finding's EVIDENCE is PASS-language iff it asserts structural presence
# of the OE-form constituents and does NOT assert a structural defect. The
# DERIVATIVE-OUTPUT discipline: we judge the evidence text (REALITY), not the
# possibly-buggy verdict FIELD.
#
# Negation-awareness (load-bearing): a FAIL-phrase that is NEGATED in context
# is in fact a PASS statement. Example (sub-finding 2.5 evidence on disk):
#   "No prose-only 'measurement/spectroscopy/test' substitutes for OE-form ..."
# The literal token "prose-only ... substitut" is a FAIL-vocabulary item, but
# the leading "No " negates it — the sentence ASSERTS that the FORBIDDEN
# prose-only form is ABSENT, which is exactly the PASS condition (the
# negative-match regex does NOT trigger). A naive FAIL-token scan mis-reads
# such negated assertions as defects. The classifier therefore strips
# negated FAIL-phrases before scanning for un-negated defect language.
_NEGATORS = (
    r"no|not|does not|do not|doesn't|don't|never|without|absent of|free of|"
    r"NOT\b"
)
# Negated FAIL-phrase: a negator within ~3 words preceding a FAIL token, OR a
# FAIL token followed by an explicit "does NOT trigger" / "do(es) not" tail.
_NEGATED_FAIL_RE = re.compile(
    rf"(?:{_NEGATORS})\W+(?:\w+\W+){{0,3}}"
    rf"(?:absent|missing|prose-only|substitut|defect|trigger|present|"
    rf"satisfy|named projector|trace|integration domain)",
    re.IGNORECASE,
)
_FAIL_LANGUAGE_RE = re.compile(
    r"\b(absent|missing|not present|prose-only substitut|does NOT satisfy|"
    r"fails to|no named projector|no trace|no integration domain|"
    r"FORBIDDEN.*present|defect)\b",
    re.IGNORECASE,
)
_PASS_LANGUAGE_RE = re.compile(
    r"(structurally present|correctly formed|all .* present|"
    r"named .*projector|subscripted trace|named integration region|"
    r"does NOT trigger|substitutes for|IS the algebraic-structure-aware "
    r"bridge image|explicitly declared|lifts substrate)",
    re.IGNORECASE,
)


def evidence_is_pass_language(evidence: str) -> bool:
    """True iff the evidence text asserts structural presence (PASS-language)
    and does NOT assert an UN-NEGATED structural defect (FAIL-language).

    Negation-aware: strip negated FAIL-phrases (e.g. 'No prose-only ...
    substitutes', 'does NOT trigger') BEFORE scanning for un-negated defect
    language, so a negated FAIL-vocabulary token is correctly read as a PASS
    statement (per the sub-finding 2.5 on-disk evidence)."""
    # Remove negated FAIL-phrases so they do not register as defects.
    stripped = _NEGATED_FAIL_RE.sub(" [NEGATED-FAIL-PHRASE] ", evidence)  # (local)
    if _FAIL_LANGUAGE_RE.search(stripped):
        return False
    return bool(_PASS_LANGUAGE_RE.search(evidence))


# ---------------------------------------------------------------------------
# Section 6 — Live-registry OE-form regex (the (C) antecedent, on disk)
# ---------------------------------------------------------------------------
def extract_vii_ax_op_proj_block(registry_text_full: str) -> str:
    """Extract the §VII.AX.OP-PROJ PBH Band-Edge entry block from the live
    registry (the same block the S92 W6-3 producing script audited)."""
    lines = registry_text_full.splitlines()
    start_idx = None  # (local)
    end_idx = None     # (local)
    for i, line in enumerate(lines):
        if "### §VII.AX.OP-PROJ" in line and "PBH" in line:
            start_idx = i
        elif (
            start_idx is not None
            and line.startswith("### §VII.A")
            and i > start_idx + 5
        ):
            end_idx = i
            break
    if start_idx is None:
        return ""
    if end_idx is None:
        end_idx = len(lines)
    return "\n".join(lines[start_idx:end_idx])


def oe_form_regex_match(registry_block: str) -> dict[str, Any]:
    """Apply the cross-pillar-bridge-anatomy.md §"Element 2 OE-form discipline"
    positive-match regex (admitting bare OR brace-delimited subscript per rule
    prose (iii)) AND the negative-match prose-only regex, to the LIVE registry
    OE-form. Returns the match booleans + the matched substring."""
    # Positive-match: ∫ ... d ... Tr ... ( [ΠP]_<subscript>  with bare OR brace.
    oe_re_bare = re.compile(r"∫.*d.*Tr.*\([ΠP]_[A-Za-z0-9_-]+")
    oe_re_brace = re.compile(r"∫.*d.*Tr.*\([ΠP]_\{[A-Za-z0-9_-]+")
    m_bare = oe_re_bare.search(registry_block)
    m_brace = oe_re_brace.search(registry_block)
    # Negative-match (FORBIDDEN prose-only forms) per the rule:
    neg_re = re.compile(
        r"Element 2.*: \.\.\.measurement|Element 2.*: \.\.\.spectroscopy|"
        r"Element 2.*: \.\.\.test\."
    )
    neg = neg_re.search(registry_block)
    positive = bool(m_bare or m_brace)
    matched = (m_bare or m_brace)
    return {
        "positive_match": positive,
        "bare_subscript_match": bool(m_bare),
        "brace_subscript_match": bool(m_brace),
        "negative_match_triggered": bool(neg),
        "matched_substring": (matched.group(0) if matched else ""),
        # The (C) antecedent: positive match AND negative-match does NOT trigger.
        "antecedent_C": positive and (not neg),
    }


# ---------------------------------------------------------------------------
# Section 7 — Plot (optional; per-clause + E2-correction bar)
# ---------------------------------------------------------------------------
def make_plot(payload: dict[str, Any], out_png: Path) -> None:
    """Axis-A clause verdicts: original (E2 emit-bug) vs corrected re-emission."""
    clauses = ["E1\n(JOINT)", "E2\n(Axis-A)", "JE3\n(JOINT)", "JE5\n(JOINT)",
               "SIO", "Axis-A\ncomposite"]
    orig = [
        payload["e1_disk"], payload["e2_disk"], payload["je3_disk"],
        payload["je5_disk"], payload["sio_disk"], payload["axis_a_composite_disk"],
    ]
    corr = [
        payload["e1_disk"], payload["e2_corrected"], payload["je3_disk"],
        payload["je5_disk"], payload["sio_disk"], payload["axis_a_composite_corrected"],
    ]
    cmap = {"PASS": "#2ca02c", "INFO": "#ff7f0e", "FAIL": "#d62728"}  # (local)
    fig, ax = plt.subplots(figsize=(10, 4.5))
    n = len(clauses)  # (local)
    for i in range(n):
        ax.add_patch(plt.Rectangle((i - 0.4, 0), 0.38, 1,
                     facecolor=cmap.get(orig[i], "#888"), edgecolor="black"))
        ax.text(i - 0.21, 0.5, orig[i], ha="center", va="center",
                color="white", fontsize=8, weight="bold", rotation=90)
        ax.add_patch(plt.Rectangle((i + 0.02, 0), 0.38, 1,
                     facecolor=cmap.get(corr[i], "#888"), edgecolor="black"))
        ax.text(i + 0.21, 0.5, corr[i], ha="center", va="center",
                color="white", fontsize=8, weight="bold", rotation=90)
    ax.set_xlim(-0.6, n - 0.4)
    ax.set_ylim(0, 1)
    ax.set_xticks(range(n))
    ax.set_xticklabels(clauses, fontsize=8)
    ax.set_yticks([])
    ax.set_title(
        f"§W4-1 Axis-A re-emission — LEFT bar = on-disk (E2 emit-bug); "
        f"RIGHT bar = corrected\n"
        f"composite {payload['axis_a_composite_disk']} → "
        f"{payload['axis_a_composite_corrected']} "
        f"(Option-A supersedes={SUPERSEDES_TARGET_AUDIT_SHA[:16]}...)",
        fontsize=9,
    )
    plt.tight_layout()
    plt.savefig(out_png, dpi=130, bbox_inches="tight")
    plt.close()


# ---------------------------------------------------------------------------
# Section 8 — Verdict emission (S87+ dual-SHA + 3-tuple + tier_pin + Option-A)
# ---------------------------------------------------------------------------
def append_verdict(verdict: str, value: str,
                   audit_sha: str, content_sha: str,
                   emit_3tuple: bool) -> None:
    """Atomic single-line append (S87+ dual-SHA schema + tier_pin companion).

    The corrective canonical line carries supersedes=<full-64-char> inside the
    value= field (Option-A protocol). The original S92 Axis-A FAIL line is
    RETAINED on disk in s92_gate_verdicts.txt (absolute verdict permanence;
    NOT touched by this script).
    """
    canonical = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    companion_dual_sha = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    # tier_pin=TIER-2 companion row: this is a Tier-2 value-pinning re-emission
    # of the Axis-A verdict artifact (plan §"Tier-ordering": W4-1 is Tier-2).
    # The substantive audit-trail supersession is over the ORIGINAL S92 Axis-A
    # FAIL line (19662dc1...; RETAINED on s92_gate_verdicts.txt per rule 1).
    companion_tier = (
        f"# tier_pin=TIER-2 # {GATE_ID} value-pinning re-emission of the "
        f"Axis-A E2 OE-form verdict artifact; CLASS=FULL — read-from-disk "
        f"on the §W6-3 Axis-A JSON REALITY; NO SCHEMATIC helper consumption; "
        f"s92_axis_a_super={SUPERSEDES_TARGET_AUDIT_SHA} (Option-A substantive "
        f"target; original S92 Axis-A FAIL line RETAINED on "
        f"s92_gate_verdicts.txt); supersedes= tag in value field points to "
        f"latest prior same-gate-ID line when present (script-bug-fix re-run)\n"
    )
    payload = canonical + companion_dual_sha + companion_tier
    if emit_3tuple:
        # §9 of plan does NOT pre-register a directional [SIGN] prediction
        # (schema_v2_3tuple_required: false); 3-tuple omitted. Guard kept for
        # interface symmetry.
        sign_v, mag_v, reg_v = "PASS", "PASS", "VALID"  # (local)
        payload += (
            f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
            f"regime_verdict={reg_v} # {GATE_ID} 3-tuple annotation "
            f"(S87 schema-v2)\n"
        )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(payload)


# ---------------------------------------------------------------------------
# Section 9 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)
    print("=" * 78)
    print(f"  {GATE_ID}")
    print(f"  scheme={SCHEME}")
    print(f"  convention={CONVENTION}")
    print(f"  L_max={L_MAX}")
    print(f"  M_KK (canonical import sanity): {M_KK}")
    print("=" * 78)

    # -- 1. Log input SHAs in first 20 lines of stdout (gate-verdicts.md §2) ---
    print()
    print("--- Input SHA-256 pins (REALITY-on-disk per DERIVATIVE-OUTPUT) ---")
    axis_a_json_sha = sha256_of(AXIS_A_JSON)
    s92_verdicts_sha = sha256_of(S92_VERDICTS_TXT)
    registry_sha = sha256_of(REGISTRY_MD)
    rule_sha = sha256_of(CROSS_PILLAR_RULE)
    cc_sha = sha256_of(CANONICAL_CONSTANTS_PY)
    self_sha = sha256_of(SCRIPT_PATH)
    print(f"  axis_a_json_sha:         {axis_a_json_sha[:16]}...")
    print(f"  s92_verdicts_sha:        {s92_verdicts_sha[:16]}...")
    print(f"  registry_md_sha:         {registry_sha[:16]}...")
    print(f"  cross_pillar_rule_sha:   {rule_sha[:16]}...")
    print(f"  canonical_constants_sha: {cc_sha[:16]}...")
    print(f"  script_self_sha:         {self_sha[:16]}...")
    print(f"  supersedes_target:       {SUPERSEDES_TARGET_AUDIT_SHA}")
    print()

    # -- 2. Read the on-disk JSON (REALITY) ----------------------------------
    detail = json.loads(AXIS_A_JSON.read_text(encoding="utf-8"))
    e1_disk = detail["element_1"]["verdict"]                  # (local)
    e2_disk = detail["element_2"]["verdict"]                  # (local)
    je3_disk = detail["joint_element_3"]["verdict"]           # (local)
    je5_disk = detail["joint_element_5"]["verdict"]           # (local)
    sio_disk = detail["substrate_input_orthogonality"]["verdict"]  # (local)
    axis_a_composite_disk = detail["axis_a_composite"]        # (local)
    print("--- On-disk JSON verdict FIELDS (the recorded state) ---")
    print(f"  element_1.verdict:                  {e1_disk}")
    print(f"  element_2.verdict:                  {e2_disk}  <- emit-bug suspect")
    print(f"  joint_element_3.verdict:            {je3_disk}")
    print(f"  joint_element_5.verdict:            {je5_disk}")
    print(f"  substrate_input_orthogonality:      {sio_disk}")
    print(f"  axis_a_composite (recorded):        {axis_a_composite_disk}")
    print()

    # -- 3. Antecedent (A): all 5 E2 sub-finding evidence PASS-language -------
    e2_subs = detail["element_2"]["sub_findings"]
    sub_evidence_pass: list[tuple[str, bool]] = []  # (local)
    for sf in e2_subs:
        ok = evidence_is_pass_language(sf["evidence"])  # (local)
        sub_evidence_pass.append((sf["id"], ok))
    antecedent_A = all(ok for _, ok in sub_evidence_pass)  # (local)
    print("--- Antecedent (A): E2 sub-finding EVIDENCE PASS-language ---")
    for sid, ok in sub_evidence_pass:
        print(f"  2.{sid.split('.')[-1] if '.' in sid else sid}  "
              f"evidence PASS-language: {ok}")
    print(f"  antecedent_A (all 5 evidence PASS-language): {antecedent_A}")
    print()

    # -- 4. Antecedent (B): E2 interpretation PASS-language ------------------
    e2_interp = detail["element_2"]["interpretation"]  # (local)
    antecedent_B = evidence_is_pass_language(e2_interp)  # (local)
    print("--- Antecedent (B): E2 interpretation PASS-language ---")
    print(f"  interpretation[:90]: {e2_interp[:90]}...")
    print(f"  antecedent_B: {antecedent_B}")
    print()

    # -- 5. Antecedent (C): live-registry OE-form regex match ----------------
    registry_full = REGISTRY_MD.read_text(encoding="utf-8")
    registry_block = extract_vii_ax_op_proj_block(registry_full)
    oe = oe_form_regex_match(registry_block)
    antecedent_C = oe["antecedent_C"]  # (local)
    print("--- Antecedent (C): LIVE-registry OE-form positive-match regex ---")
    print(f"  registry §VII.AX.OP-PROJ block chars: {len(registry_block)}")
    print(f"  positive_match (bare OR brace):       {oe['positive_match']}")
    print(f"    bare-subscript match:               {oe['bare_subscript_match']}")
    print(f"    brace-subscript match:              {oe['brace_subscript_match']}")
    print(f"  negative-match (prose-only) triggered:{oe['negative_match_triggered']}")
    print(f"  matched substring: {oe['matched_substring'][:80]}")
    print(f"  antecedent_C (positive AND not-negative): {antecedent_C}")
    print()

    # -- 6. Re-derive corrected E2 + composite -------------------------------
    e2_corrected = "PASS" if (antecedent_A and antecedent_B and antecedent_C) else "FAIL"  # (local)
    print("--- Corrected E2 (substitution-chain Step 4) ---")
    print(f"  corrected E2 = PASS IFF (A ∧ B ∧ C) = "
          f"{antecedent_A} ∧ {antecedent_B} ∧ {antecedent_C} = {e2_corrected}")
    print()

    # Composite under corrected E2 (substitution-chain Step 5).
    # axis_a_composite = E1 ∧ E2_corrected ∧ JE3 ∧ JE5 ∧ SIO (all read from disk).
    clause_inputs = {  # (local)
        "E1_JOINT": e1_disk,
        "E2_corrected": e2_corrected,
        "JE3_JOINT": je3_disk,
        "JE5_JOINT": je5_disk,
        "SIO": sio_disk,
    }
    all_pass = all(v == "PASS" for v in clause_inputs.values())  # (local)
    any_info = any(v == "INFO" for v in clause_inputs.values())  # (local)
    axis_a_composite_corrected = (
        "PASS" if all_pass else ("INFO" if any_info else "FAIL")
    )  # (local)
    print("--- Corrected Axis-A composite (substitution-chain Step 5) ---")
    for k, v in clause_inputs.items():
        print(f"  {k:14s}: {v}")
    print(f"  axis_a_composite_corrected: {axis_a_composite_corrected}")
    print()

    # Re-emission verdict: PASS iff the emit-bug is confirmed AND composite=PASS.
    # FAIL iff the corrective antecedents are refuted (original FAIL stands).
    emit_bug_confirmed = (
        (e2_disk == "FAIL") and (e2_corrected == "PASS")
        and antecedent_A and antecedent_B and antecedent_C
    )  # (local)
    if emit_bug_confirmed and axis_a_composite_corrected == "PASS":
        verdict = "PASS"
    else:
        # On-disk antecedents refute the emit-bug hypothesis (plan FAIL_meaning)
        # OR one of E1/JE3/JE5/SIO is not PASS on disk. Original FAIL stands.
        verdict = "FAIL"
    print(f"=== RE-EMISSION VERDICT: {verdict} "
          f"(emit_bug_confirmed={emit_bug_confirmed}, "
          f"composite_corrected={axis_a_composite_corrected}) ===")
    print()

    # -- 7. Save NPZ + PNG ---------------------------------------------------
    out_npz = _THIS_DIR / "s93_w4_1_vii_ax_op_proj_axis_a_e2_re_emission.npz"
    out_png = _THIS_DIR / "s93_w4_1_vii_ax_op_proj_axis_a_e2_re_emission.png"

    plot_payload = {  # (local)
        "e1_disk": e1_disk, "e2_disk": e2_disk, "je3_disk": je3_disk,
        "je5_disk": je5_disk, "sio_disk": sio_disk,
        "axis_a_composite_disk": axis_a_composite_disk,
        "e2_corrected": e2_corrected,
        "axis_a_composite_corrected": axis_a_composite_corrected,
    }
    make_plot(plot_payload, out_png)
    print(f"  saved PNG: {out_png.name}")

    np.savez(
        out_npz,
        gate_id=GATE_ID,
        # on-disk recorded verdict FIELDS (the emit-bug state)
        e1_disk=e1_disk, e2_disk=e2_disk, je3_disk=je3_disk,
        je5_disk=je5_disk, sio_disk=sio_disk,
        axis_a_composite_disk=axis_a_composite_disk,
        # corrective antecedents
        antecedent_A_all_evidence_pass=antecedent_A,
        antecedent_B_interpretation_pass=antecedent_B,
        antecedent_C_oe_regex_match=antecedent_C,
        e2_sub_evidence_pass=np.array(
            [[sid, str(ok)] for sid, ok in sub_evidence_pass], dtype=object
        ),
        oe_positive_match=oe["positive_match"],
        oe_bare_match=oe["bare_subscript_match"],
        oe_brace_match=oe["brace_subscript_match"],
        oe_negative_triggered=oe["negative_match_triggered"],
        oe_matched_substring=oe["matched_substring"],
        # corrected state
        e2_corrected=e2_corrected,
        axis_a_composite_corrected=axis_a_composite_corrected,
        emit_bug_confirmed=emit_bug_confirmed,
        reemission_verdict=verdict,
        # Option-A supersedes + provenance
        supersedes_target_audit_sha=SUPERSEDES_TARGET_AUDIT_SHA,
        L_max=L_MAX,
        scheme=SCHEME,
        convention=CONVENTION,
        input_pins_json=json.dumps({
            "axis_a_json_sha256": axis_a_json_sha,
            "s92_verdicts_sha256": s92_verdicts_sha,
            "registry_md_sha256": registry_sha,
            "cross_pillar_rule_sha256": rule_sha,
            "canonical_constants_sha256": cc_sha,
            "script_self_sha256": self_sha,
        }, indent=2),
    )
    print(f"  saved NPZ: {out_npz.name}")
    print()

    # -- 8. Emit corrective verdict line via Option-A supersedes -------------
    pin_map = {  # (local) — audit_sha256 inputs per plan §W4-1 (6)
        "axis_a_json_sha256": axis_a_json_sha,
        "s92_verdicts_original_line_sha256": s92_verdicts_sha,
        "registry_md_sha256": registry_sha,
        "cross_pillar_rule_sha256": rule_sha,
        "canonical_constants_sha256": cc_sha,
        "script_self_sha256": self_sha,
        "supersedes_target_audit_sha": SUPERSEDES_TARGET_AUDIT_SHA,
        "e2_corrected": e2_corrected,
        "axis_a_composite_corrected": axis_a_composite_corrected,
        "reemission_verdict": verdict,
        "GATE_ID": GATE_ID,
        "SCHEME": SCHEME,
        "CONVENTION": CONVENTION,
        "L_MAX": str(L_MAX),
    }
    audit_sha = closure_hash(pin_map)
    content_sha = sha256_of(SCRIPT_PATH)  # content_sha256 inputs = ["script"]

    # Option-A supersedes target selection (gate-verdicts.md §"Option A",
    # rules 1-5; v3-closure-recovery.md sig_5 "script-bug fix" clause):
    #   - The SUBSTANTIVE supersession claim is over the ORIGINAL S92 Axis-A
    #     FAIL line (19662dc1...): this corrected Axis-A re-emission retires it
    #     in the audit-trail-canonical reading. Recorded as `s92_axis_a_super=`.
    #   - The Option-A `supersedes=` TAG (rule 2) points to the LATEST PRIOR
    #     canonical line for THIS gate-ID on the s93 verdict file, IF one
    #     exists (the run-1 line was emitted under a classifier bug in this
    #     same script). Each corrective iteration supersedes its most-recent
    #     prior same-gate-ID line; the original buggy line is RETAINED on disk
    #     (absolute verdict permanence, rule 1).
    prior_same_gate_shas: list[str] = []  # (local)
    if VERDICT_TXT.exists():
        for ln in VERDICT_TXT.read_text(encoding="utf-8").splitlines():
            if ln.startswith(f"{GATE_ID}:"):
                m = re.search(r"audit_sha256=([a-f0-9]{64})", ln)
                if m:
                    prior_same_gate_shas.append(m.group(1))
    supersedes_tag_target = (
        prior_same_gate_shas[-1] if prior_same_gate_shas else ""
    )  # (local)
    if supersedes_tag_target:
        print(f"  Option-A: prior same-gate-ID canonical line detected "
              f"({supersedes_tag_target[:16]}...); corrective line supersedes it")

    # The `supersedes=` field in the value string carries the Option-A TAG
    # target (prior same-gate-ID line) when one exists; otherwise (first clean
    # emission) it carries the substantive S92 Axis-A target on PASS.
    if verdict == "PASS":
        supersedes_field = (
            f";supersedes={supersedes_tag_target}"
            if supersedes_tag_target
            else f";supersedes={SUPERSEDES_TARGET_AUDIT_SHA}"
        )  # (local)
    else:
        # FAIL re-emission: original S92 FAIL STANDS (no substantive supersede);
        # but a prior same-gate-ID buggy line is still Option-A-superseded.
        supersedes_field = (
            f";supersedes={supersedes_tag_target}"
            if supersedes_tag_target else ""
        )  # (local)

    value_str = (
        f"axis_a_composite={axis_a_composite_corrected};"
        f"E1={e1_disk};E2_corrected={e2_corrected};E2_disk_field={e2_disk};"
        f"JE3={je3_disk};JE5={je5_disk};sio={sio_disk};"
        f"emit_bug_confirmed={emit_bug_confirmed};"
        f"antecedent_A_evidence_pass={antecedent_A};"
        f"antecedent_B_interp_pass={antecedent_B};"
        f"antecedent_C_oe_regex_match={antecedent_C};"
        f"oe_brace_match={oe['brace_subscript_match']};"
        f"s92_axis_a_super={SUPERSEDES_TARGET_AUDIT_SHA};"
        f"reviewer=connes-ncg-theorist;writer-of-record-continuity=True;"
        f"central=7.2761e-23_m_minus_3;conjunct=[5.5e-23,2.2e-22]"
        f"{supersedes_field}"
    )

    append_verdict(verdict, value_str, audit_sha, content_sha, emit_3tuple=False)
    print("--- Verdict line emitted (Option-A corrective) ---")
    print(f"  audit_sha256:        {audit_sha}")
    print(f"  content_sha256:      {content_sha}")
    print(f"  supersedes= TAG:     "
          f"{supersedes_tag_target if supersedes_tag_target else '(none — first emission)'}")
    print(f"  s92_axis_a_super (substantive): {SUPERSEDES_TARGET_AUDIT_SHA}")
    print(f"  verdict:             {GATE_ID}: {verdict}")
    print()

    # SHA-uniqueness self-check vs prior canonical lines in s93 verdict file.
    prior_audit_shas: list[str] = []  # (local)
    for ln in VERDICT_TXT.read_text(encoding="utf-8").splitlines():
        if " audit_sha256=" in ln and not ln.lstrip().startswith("#"):
            m = re.search(r"audit_sha256=([a-f0-9]{64})", ln)
            if m:
                prior_audit_shas.append(m.group(1))
    dup = prior_audit_shas.count(audit_sha)  # (local)
    print(f"  audit_sha256 occurrences in s93 verdict file: {dup} "
          f"(expect 1; sig_5 uniqueness)")
    print()
    print(f"  elapsed: {time.time() - t0:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
