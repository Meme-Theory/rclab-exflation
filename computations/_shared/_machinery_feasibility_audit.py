#!/usr/bin/env python3
"""
_machinery_feasibility_audit.py — plan-freeze machinery-feasibility audit module
================================================================================

INAUGURAL CREATION (S101 W8a-1, gate S101-HK-SELECTION-RULE-PREFLIGHT-AUDIT).

This is the entity that three `math-scripts.md` rule references tag "queued"
(PRU Class-8 fix-now). It hosts plan-freeze audit detectors that statically
screen a session plan file's gate-block / substitution-chain text for
machinery-feasibility defects BEFORE any compute dispatches.

Governing rule anchors (math-scripts.md):
  - §:86  "Double-Check Logic Before Compute" — the runtime substitution-chain
          discipline this module's plan-freeze detectors are the F-image of.
  - §:141 "Plan-author discipline at plan-freeze" — the OPERATOR-MISMATCH-DETECTED
          routing this selection-rule sub-check extends to matrix-element claims.
  - §:305 "Machinery-Feasibility Audit" — the audit this module implements;
          every machinery pin declares its feasibility envelope; the
          SOURCE-RECONCILIATION sub-audit runs the feasibility check at
          plan-freeze.

ARCHITECTURE
------------
The module is a DETECTOR REGISTRY: a dict mapping a detector name to a callable
``(plan_text: str) -> list[Finding]``. New detectors are added by:
  (1) writing a ``detect_<name>(plan_text) -> list[Finding]`` function, and
  (2) registering it in ``DETECTOR_REGISTRY`` (one line).
No restructuring is needed to add a second detector — W8a-2 extends this same
file by adding one registry entry. The CLI, severity enum, finding schema, and
self-test harness are detector-agnostic.

SEVERITY LADDER
---------------
``Severity`` enum {S1, S2}. The selection-rule detector emits at S2 (advisory)
under the W8b-1 rule status SUGGESTION K=1, escalating to S1 ONLY on that rule's
future K=3 MANDATORY promotion. The severity is keyed on the rule-status string
the module reads from its own docstring constant
(``SELECTION_RULE_PREFLIGHT_STATUS``) — NOT auto-promoted by any gate. To
escalate, an orchestrator edits that constant when the rule promotes.

EXIT CODES (per math-scripts.md §"Exit Codes and Verdict Semantics")
--------------------------------------------------------------------
A finding is DATA, not a script error. ``--self-test`` exits 0 iff the self-test
ASSERTIONS hold (the detectors behave as pinned); nonzero exit is reserved for
script breakage (a self-test assertion failing = the module is broken). A plain
audit run (a plan-file path argument) exits 0 regardless of how many findings it
emits — findings are the audit's output, not its health.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field, asdict
from enum import Enum
from pathlib import Path

# Canonical-constants discipline (import-only compliance; this audit module
# consumes NO framework constant numerically — it is a pure text/AST audit — but
# co-located `_shared` modules carry the import so the canonical-constants audit
# and the runtime input-pin SHA see a compliant module, matching the sibling
# pattern in `_pru_cardinality_audit.py` / `_source_reconciliation_audit.py`).
sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from canonical_constants import *  # noqa: F401,F403
except Exception:  # noqa: BLE001 — audit module is import-tolerant; constants unused
    pass

# ---------------------------------------------------------------------------
# Severity enum {S1, S2}
# ---------------------------------------------------------------------------


class Severity(str, Enum):
    """Plan-freeze audit severity ladder.

    S2 = advisory (does NOT HARD-HALT plan-freeze under SUGGESTION status).
    S1 = MANDATORY (HALTS plan-freeze; reached when a SUGGESTION rule promotes
         to K=3 MANDATORY).
    """

    S1 = "S1"
    S2 = "S2"


# ---------------------------------------------------------------------------
# Finding schema (detector-agnostic)
# ---------------------------------------------------------------------------


@dataclass
class Finding:
    """One audit finding emitted by a detector.

    Attributes
    ----------
    detector   : registry name of the emitting detector.
    flag       : the canonical flag string (e.g. SELECTION-RULE-PREFLIGHT-VIOLATION).
    severity   : Severity.S1 | Severity.S2.
    message    : human-readable one-line diagnosis.
    detail     : structured payload (matched sectors, trialities, predicate, etc.).
    """

    detector: str
    flag: str
    severity: Severity
    message: str
    detail: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        d = asdict(self)
        d["severity"] = self.severity.value
        return d


# ---------------------------------------------------------------------------
# Detector 1 — selection-rule CG-admissibility pre-flight
#   (S101 W8a-1; governing rule W8b-1 SELECTION-RULE-PREFLIGHT-RULE)
# ---------------------------------------------------------------------------

# Rule-status constant the severity ladder keys on. Edited by the orchestrator
# ONLY when the W8b-1 rule promotes SUGGESTION -> MANDATORY (K=3). NOT
# auto-promoted by any gate.
SELECTION_RULE_PREFLIGHT_STATUS = "SUGGESTION"  # K=1 at landing

# Canonical flag strings.
FLAG_SELECTION_RULE_VIOLATION = "SELECTION-RULE-PREFLIGHT-VIOLATION"
FLAG_SELECTION_RULE_UNDECLARED_OPERATOR = (
    "SELECTION-RULE-PREFLIGHT-UNDECLARED-OPERATOR-CHARACTER"
)

# Sentinel for an operator whose center character cannot be read from the
# matched text (the claim is unscreenable as written).
_T_O_UNDECLARED = "UNDECLARED"

# ---- Pinned regex pattern set (verbatim from plan §W8a-1 method (b)) ----

# (i) bra-ket nonzero claims between named SU(3) sectors — ASCII <...|...|...>.
_PAT_BRAKET_ASCII = re.compile(
    r"<\s*(?:psi_?)?\(?(\d+)\s*,\s*(\d+)\)?\s*\|(.+?)\|\s*(?:psi_?)?\(?(\d+)\s*,\s*(\d+)\)?\s*>\s*(?:!=|\\neq|≠)\s*0"
)

# (i') unicode bra-ket variant ⟨...|...|...⟩ of the same form.
_PAT_BRAKET_UNICODE = re.compile(
    r"⟨\s*(?:psi_?)?\(?(\d+)\s*,\s*(\d+)\)?\s*\|(.+?)\|\s*(?:psi_?)?\(?(\d+)\s*,\s*(\d+)\)?\s*⟩\s*(?:!=|\\neq|≠)\s*0"
)

# (ii) prose-form claims: a "generically nonzero" / "nonzero matrix element" /
# "connects ... sectors" assertion within 400 chars of two named (p,q) labels.
_PAT_PROSE = re.compile(
    r"(?i)\b(generically\s+non-?zero|non-?zero\s+matrix\s+element|connect(?:s|ing)\s+.{0,40}sectors)\b"
)

# Named (p,q) sector label, e.g. "(1,0)" or "psi_(1,1)" — used to find the two
# nearest sector labels around a prose match.
_PAT_SECTOR_LABEL = re.compile(r"\(?\s*(\d+)\s*,\s*(\d+)\s*\)")

# Operator center-character readers.
#   declared-irrep form "in (a,b)" -> t_O = (a - b) mod 3.
_PAT_OP_DECLARED_IRREP = re.compile(r"\bin\s+\(?\s*(\d+)\s*,\s*(\d+)\s*\)")
#   squared-modulus forms -> t_O = 0 ALWAYS (center-invariant by construction):
#     |f|^2, |f(h)|^2, |s|^2, f*conj(f), conj-product, "mod-squared",
#     "squared modulus", "|...|²".
_PAT_OP_MOD_SQUARED = re.compile(
    r"(?:\|[^|]+\|\s*(?:\^?\s*2|²))"          # |...|^2 or |...|²
    r"|(?:mod[-\s]*squared)"                   # mod-squared
    r"|(?:squared\s+modul(?:us|i))"            # squared modulus / moduli
    r"|(?:\bconj\s*\()"                        # conj( ...  -> f*conj(f)
    r"|(?:\*\s*conj)"                          # f * conj(f)
    r"|(?:s\(h\)\s*\*\s*conj)",                # s(h)*conj(s(h))
    re.IGNORECASE,
)


def _triality(p: int, q: int) -> int:
    """SU(3) center-Z3 character (triality) of irrep (p, q): t = (p - q) mod 3."""
    return (p - q) % 3


def _operator_center_character(op_text: str, context: str | None = None):
    """Read the operator's center character t_O from the matched operator text.

    Returns an int in {0, 1, 2} when readable, or _T_O_UNDECLARED otherwise.

    Precedence (per plan method (b)):
      1. squared-modulus forms (in the bra-ket interior OR its surrounding
         context) -> t_O = 0 ALWAYS (center-invariant).
      2. declared-irrep "in (a,b)" inside the bra-ket interior -> t_O = (a-b) mod 3.
      3. declared-irrep tied to the operator symbol in the SURROUNDING CONTEXT
         (the natural prose form "<...| s(h) |...> != 0 with s(h) in (2,0)" — the
         irrep declaration sits outside the bra-ket bars) -> t_O = (a-b) mod 3.
      4. undeclared -> _T_O_UNDECLARED (claim unscreenable as written).

    The ``context`` argument is the local clause around the bra-ket match; it lets
    the reader recover an operator-irrep declaration that the bra-ket interior
    alone does not carry. Interior wins over context (precedence 2 before 3).
    """
    # (1) squared-modulus, interior first then context (center-invariant always).
    if _PAT_OP_MOD_SQUARED.search(op_text):
        return 0
    if context is not None and _PAT_OP_MOD_SQUARED.search(context):
        return 0
    # (2) declared irrep inside the bra-ket interior.
    m = _PAT_OP_DECLARED_IRREP.search(op_text)
    if m:
        a, b = int(m.group(1)), int(m.group(2))
        return (a - b) % 3
    # (3) declared irrep tied to the operator symbol in the surrounding context.
    if context is not None:
        sym = op_text.strip()
        if sym:
            # Match "<sym> in (a,b)" anywhere in the context (sym may contain
            # regex-special chars like the parens of s(h) -> escape it).
            pat = re.compile(re.escape(sym) + r"\s+in\s+\(?\s*(\d+)\s*,\s*(\d+)\s*\)")
            cm = pat.search(context)
            if cm:
                a, b = int(cm.group(1)), int(cm.group(2))
                return (a - b) % 3
        # Fallback: any bare "in (a,b)" declaration in the immediate context.
        cm = _PAT_OP_DECLARED_IRREP.search(context)
        if cm:
            a, b = int(cm.group(1)), int(cm.group(2))
            return (a - b) % 3
    # (4) unreadable.
    return _T_O_UNDECLARED


def _emit_braket_finding(
    p1: int, q1: int, op_text: str, p2: int, q2: int, context: str | None = None
):
    """Build a Finding for a bra-ket nonzero claim, or None if CG-admissible.

    Admissibility predicate (NECESSARY condition only — a passed screen does NOT
    certify nonzero): t(p1,q1) == (t(p2,q2) + t_O) mod 3.
    """
    severity = _current_severity()
    t1 = _triality(p1, q1)
    t2 = _triality(p2, q2)
    t_o = _operator_center_character(op_text, context)

    if t_o == _T_O_UNDECLARED:
        return Finding(
            detector="selection_rule_preflight",
            flag=FLAG_SELECTION_RULE_UNDECLARED_OPERATOR,
            severity=severity,
            message=(
                f"nonzero claim <({p1},{q1})| O |({p2},{q2})> has an operator whose "
                f"center character is UNDECLARED — the claim is unscreenable as written; "
                f"declare the operator irrep or recognise it as center-invariant (|f|^2)."
            ),
            detail={
                "bra": [p1, q1],
                "ket": [p2, q2],
                "t_bra": t1,
                "t_ket": t2,
                "t_op": _T_O_UNDECLARED,
                "operator_text": op_text.strip(),
                "predicate": "t(bra) == (t(ket) + t_O) mod 3",
                "predicate_evaluable": False,
            },
        )

    rhs = (t2 + t_o) % 3
    admissible = (t1 == rhs)
    if admissible:
        return None
    return Finding(
        detector="selection_rule_preflight",
        flag=FLAG_SELECTION_RULE_VIOLATION,
        severity=severity,
        message=(
            f"nonzero claim <({p1},{q1})| O |({p2},{q2})> violates the SU(3) center-Z3 "
            f"selection rule: t(bra)={t1} != (t(ket)+t_O) mod 3 = ({t2}+{t_o}) mod 3 = {rhs} "
            f"-> the element is 0 EXACTLY by the center average; the 'nonzero' claim is "
            f"group-theoretically inadmissible."
        ),
        detail={
            "bra": [p1, q1],
            "ket": [p2, q2],
            "t_bra": t1,
            "t_ket": t2,
            "t_op": t_o,
            "operator_text": op_text.strip(),
            "predicate": "t(bra) == (t(ket) + t_O) mod 3",
            "lhs": t1,
            "rhs": rhs,
            "predicate_evaluable": True,
            "admissible": False,
        },
    )


def _current_severity() -> Severity:
    """Severity keyed on the rule-status docstring constant (NOT auto-promoted).

    SUGGESTION -> S2 advisory; MANDATORY -> S1 HARD-HALT.
    """
    return Severity.S1 if SELECTION_RULE_PREFLIGHT_STATUS == "MANDATORY" else Severity.S2


def detect_selection_rule_preflight(plan_text: str) -> list[Finding]:
    """Center-character / triality CG-admissibility pre-flight detector.

    Screens plan-block / substitution-chain text for bra-ket and prose-form
    "generically nonzero" matrix-element claims between named SU(3) (p,q)
    sectors, and flags those that violate the SU(3) center-Z3 selection rule

        t(p1,q1) == (t(p2,q2) + t_O) mod 3            [NECESSARY condition]

    where t(p,q) = (p - q) mod 3 is the triality (center-Z3 character) and t_O is
    the operator's center character (0 for any squared-modulus / center-invariant
    operator; (a-b) mod 3 for an operator declared "in (a,b)"; UNDECLARED
    otherwise).

    This is the audit-floor F-image of the substrate's own selection rule: matrix
    elements of center-invariant observables between triality-mismatched
    Peter-Weyl sectors of D_K vanish IDENTICALLY (the same Z3 grading that
    underlies the PROVEN block-diagonal structure of D_K). The detector enforces
    what the fabric's representation theory already IS.

    Returns a list of Findings (possibly empty). A passed screen does NOT certify
    the element is nonzero — the center check is a NECESSARY condition only; the
    full Clebsch-Gordan decomposition can still vanish.
    """
    findings: list[Finding] = []

    # (i) + (i') bra-ket claims (ASCII and unicode). The bra-ket form carries the
    # operator EXPLICITLY, so admissibility is decidable; record every adjudicated
    # (bra,ket) sector pair (unordered) so the prose fallback (ii) does NOT
    # double-flag a claim the bra-ket detector already decided.
    adjudicated_pairs: set[frozenset[tuple[int, int]]] = set()
    for pat in (_PAT_BRAKET_ASCII, _PAT_BRAKET_UNICODE):
        for m in pat.finditer(plan_text):
            p1, q1 = int(m.group(1)), int(m.group(2))
            op_text = m.group(3)
            p2, q2 = int(m.group(4)), int(m.group(5))
            adjudicated_pairs.add(frozenset({(p1, q1), (p2, q2)}))
            # Context = the local clause around the match, so an operator-irrep
            # declaration that sits OUTSIDE the bra-ket bars (the natural form
            # "<...| s(h) |...> != 0 with s(h) in (2,0)") is recoverable.
            c_lo = max(0, m.start() - 200)  # (local)
            c_hi = min(len(plan_text), m.end() + 200)  # (local)
            context = plan_text[c_lo:c_hi]  # (local)
            f = _emit_braket_finding(p1, q1, op_text, p2, q2, context)
            if f is not None:
                findings.append(f)

    # (ii) prose-form claims: within 400 chars of TWO named (p,q) labels. This is
    # a FALLBACK for claims stated WITHOUT an explicit bra-ket (no readable
    # operator). When the prose match's nearest two sectors coincide with a pair
    # an explicit bra-ket ALREADY adjudicated, the prose match is that same claim
    # — the bra-ket adjudication (which CAN read the operator) supersedes the
    # prose fallback, so the prose finding is suppressed (no double-count).
    for m in _PAT_PROSE.finditer(plan_text):
        lo = max(0, m.start() - 400)
        hi = min(len(plan_text), m.end() + 400)
        window = plan_text[lo:hi]
        sectors = _PAT_SECTOR_LABEL.findall(window)
        # Deduplicate while preserving order; need at least two distinct labels.
        seen: list[tuple[int, int]] = []
        for (sp, sq) in sectors:
            tup = (int(sp), int(sq))
            if tup not in seen:
                seen.append(tup)
        if len(seen) < 2:
            continue
        (p1, q1), (p2, q2) = seen[0], seen[1]
        # Suppress if an explicit bra-ket already adjudicated this sector pair.
        if frozenset({(p1, q1), (p2, q2)}) in adjudicated_pairs:
            continue
        # Operator character unreadable from prose form -> UNDECLARED-OPERATOR
        # flag (the prose claim is unscreenable for admissibility as written).
        findings.append(
            Finding(
                detector="selection_rule_preflight",
                flag=FLAG_SELECTION_RULE_UNDECLARED_OPERATOR,
                severity=_current_severity(),
                message=(
                    f"prose 'nonzero/connecting' claim near sectors ({p1},{q1}) and "
                    f"({p2},{q2}) carries no readable operator center character — "
                    f"unscreenable as written; restate as an explicit bra-ket with a "
                    f"declared or center-invariant operator so the triality predicate "
                    f"can run."
                ),
                detail={
                    "match": m.group(0).strip(),
                    "sectors": [list(seen[0]), list(seen[1])],
                    "t_sectors": [_triality(p1, q1), _triality(p2, q2)],
                    "t_op": _T_O_UNDECLARED,
                    "predicate_evaluable": False,
                },
            )
        )

    return findings


# ---------------------------------------------------------------------------
# Detector 2 — multiplicative-normalization cancellation, 3 signature classes
#   (S101 W8a-2; governing rule math-scripts.md §"Multiplicative-normalization
#    cancellation invariants", MANDATORY at K=3 — S94 W6-18 promotion,
#    audit 6284d0d3ac7a85c8174f26c8d1ae8561f4ff89945ae6d86cffb4a8b8ff8fb27e)
# ---------------------------------------------------------------------------
#
# The MANDATORY rule pins THREE structurally-distinct SPECTRAL-SUPPORT
# factorization mechanisms in its K-counter (L_max-truncation / tau-moduli /
# Casimir-ceiling). Until this gate the rule had NO plan-freeze detector — its
# two S100b W7 instances (G-cancellation in a ratio-of-pipelines; flat-S
# invariance in a fractional count variance) self-detected only AT EXECUTION.
# This detector is the plan-freeze SCREEN across THREE signature classes:
#
#   S1 LOG-DERIVATIVE  — the rule's queued baseline (math-scripts.md), implemented
#                        here for the first time. Flags gated quantities of the
#                        form d^n ln(.)/d(ln K)^n: a multiplicative pre-factor
#                        w(L_max)/w(tau-moduli)/w(C_2^max) is annihilated by the
#                        log-derivative, so the "plateau" is a structural identity.
#                        Severity S1 MANDATORY (the rule is MANDATORY at K=3). The
#                        detector is the SCREEN ONLY — it routes the plan author to
#                        the Sage-MCP sage_simplify factorization check (rule
#                        §Plan-freeze pre-flight items 1-4); it proves nothing by
#                        itself.
#   S2 RATIO-OF-PIPELINES (NEW) — |log10(X_em/X_ref)| / named two-pipeline ratio,
#                        CONJOINED with a shared LABORATORY-IN pipeline parameter
#                        (G, H_0, S, calibration constant) appearing in BOTH legs'
#                        scalings: the shared factor cancels in the ratio. Severity
#                        S2 advisory (NEW classes ship at S2; hardening to S1 is a
#                        FUTURE K-decision this gate does NOT make).
#   S3 VARIANCE-FUNCTIONAL (NEW) — coefficient-of-variation / Std(N)/Mean(N) /
#                        sigma_CV, CONJOINED with a FLAT multiplicative
#                        capture/completeness parameter: N -> S*N leaves the
#                        fractional variance invariant. Severity S2.
#
# The cancelling factors in the two NEW classes (G, S) live in the LABORATORY-IN
# reduction pipeline (emergent-Friedmann halo counting; survey capture), NOT in
# the fabric's spectral support of any D_K functional — a categorically DIFFERENT
# documentation axis (cancelling_axis = LAB-IN-PIPELINE) vs the rule's three
# spectral-support K-counter rows. The corpus this gate lands tags both instances
# NON-K-ADVANCING for that reason (no fourth spectral-support row; no K decision).

# Rule-status constant the LOG-DERIVATIVE severity keys on. The rule is MANDATORY
# at K=3 (math-scripts.md), so the LOG-DERIVATIVE class emits S1. The NEW S2/S3
# classes are pinned S2 here independently (their S1-hardening is a future
# K-decision; see MULT_CANCEL_NEWCLASS_SEVERITY).
MULT_CANCELLATION_LOGDERIV_STATUS = "MANDATORY"  # rule MANDATORY at K=3 (S94 W6-18)
MULT_CANCEL_NEWCLASS_SEVERITY = Severity.S2  # RATIO-OF-PIPELINES + VARIANCE-FUNCTIONAL

# Canonical flag string (shared across all three classes).
FLAG_MULT_CANCELLATION = "MULTIPLICATIVE-NORMALIZATION-CANCELLATION-DETECTED"

# Signature-class labels.
SIGCLASS_LOG_DERIVATIVE = "LOG-DERIVATIVE"
SIGCLASS_RATIO_OF_PIPELINES = "RATIO-OF-PIPELINES"
SIGCLASS_VARIANCE_FUNCTIONAL = "VARIANCE-FUNCTIONAL"

# Cancelling-axis values.
AXIS_SPECTRAL_SUPPORT = "SPECTRAL-SUPPORT"   # LOG-DERIVATIVE class (fabric-side)
AXIS_LAB_IN_PIPELINE = "LAB-IN-PIPELINE"     # RATIO/VARIANCE classes (lab-side)

# ---- Shared LAB-IN pipeline-parameter keyword list (machinery_pin_map) -------
# Pinned initial list; EXTENSIBLE by future plan-freeze additions ONLY (an
# extension is a rule-side change, NOT silent in-module drift). The conjunction
# test for the two NEW classes requires one of these to appear in the gated
# quantity's defining scalings.
SHARED_LAB_IN_PARAM_KEYWORDS = (
    "G", "G_N", "G_eff", "GN",          # Newton's constant + emergent variants
    "H_0", "H0",                         # Hubble constant
    "S",                                 # flat multiplicative capture / completeness
    "calibration constant", "calibration_constant",
)

# Word-boundary regexes for each shared lab-IN parameter (built once). Bare
# single-letter tokens (G, S) MUST match as standalone symbols, not as
# substrings of unrelated words (e.g. "Goldstone", "Spectral").
def _build_shared_param_patterns() -> dict:
    pats: dict = {}  # (local)
    for kw in SHARED_LAB_IN_PARAM_KEYWORDS:
        if " " in kw or "_" in kw and kw.endswith("constant"):
            # multi-word / phrase keyword: literal, case-insensitive.
            pats[kw] = re.compile(re.escape(kw), re.IGNORECASE)
        else:
            # symbol keyword: standalone, case-SENSITIVE (G != g; S != s — the
            # capture S is upper-case, the spectral index s is lower-case).
            pats[kw] = re.compile(r"(?<![A-Za-z0-9_])" + re.escape(kw) + r"(?![A-Za-z0-9])")
    return pats


_SHARED_PARAM_PATTERNS = _build_shared_param_patterns()

# ---- (S1) LOG-DERIVATIVE pinned regex set (verbatim from plan §W8a-2) --------
# ASCII form: d^n ln(.)/d(ln K)^n — n optional (d ln / d ln K) and d^2 forms.
_PAT_LOGDERIV_ASCII = re.compile(
    r"d\^?\d*\s*ln\s*\(.+?\)\s*/\s*d\s*\(\s*ln\s*\w+\s*\)"
)
# Unicode / superscript-² variant: d²ln(.)/d(ln K)² and the d ln(.)/dlnK compact
# form (no inner parens around lnK).
_PAT_LOGDERIV_UNICODE = re.compile(
    r"d[²2]?\s*ln\s*\(.+?\)\s*/\s*d\s*\(?\s*ln\s*\w+\s*\)?[²2]?"
)
# R_KW / second-log-derivative shorthand the rule uses (d² ln κ / d(ln K)²).
_PAT_LOGDERIV_SHORTHAND = re.compile(
    r"(?i)\b(?:second\s+)?log[-\s]*derivative\b|d\^?2\s*ln\b|d²\s*ln\b"
)

# ---- (S2) RATIO-OF-PIPELINES pinned regex set --------------------------------
# Primary: |log10(X_em/X_ref)| with the em/ref|A/B|1/2 pipeline-suffix pair.
_PAT_RATIO_LOG10 = re.compile(
    r"log_?10\s*\(\s*\w+_(?:em|A|1)\s*/\s*\w+_(?:ref|B|2)\s*\)"
)
# Generic named two-pipeline ratio X_<suffixA>/X_<suffixB> (same root symbol,
# em/ref|A/B|1/2 suffixes) — catches ratio forms NOT wrapped in log10.
_PAT_RATIO_NAMED_PIPELINES = re.compile(
    r"\b(\w+?)_(?:em|A|1)\s*/\s*\1_(?:ref|B|2)\b"
)
# Prose marker: "ratio of (two )?pipelines" / "pipeline ratio" / "ratio-of-pipelines".
_PAT_RATIO_PROSE = re.compile(
    r"(?i)\bratio[-\s]of[-\s]pipelines\b|\bpipeline\s+ratio\b|\bratio\s+of\s+(?:the\s+)?(?:two\s+)?pipelines\b"
)

# ---- (S3) VARIANCE-FUNCTIONAL pinned regex set -------------------------------
# coefficient of variation / sigma_CV / fractional (count )?variance.
_PAT_CV_PROSE = re.compile(
    r"(?i)\bcoefficient\s+of\s+variation\b|\bsigma_?CV\b|\bσ_?CV\b|\bfractional\s+(?:count\s+)?variance\b|\bCV\b"
)
# Std(N)/Mean(N) operator form (or std/mean, lower-case).
_PAT_STD_OVER_MEAN = re.compile(
    r"(?i)\b(?:std|stdev|standard\s+deviation)\s*\(\s*\w+\s*\)\s*/\s*\b(?:mean|avg|average)\s*\(\s*\w+\s*\)"
)

# Flat multiplicative capture / completeness parameter marker (the S3
# conjunction's companion): "flat ... capture/completeness", "N -> S*N",
# "S*N", "z-independent completeness/capture".
_PAT_FLAT_CAPTURE = re.compile(
    r"(?i)\bflat\b.{0,40}\b(?:multiplicative\s+)?(?:capture|completeness)\b"
    r"|N\s*->\s*S\s*\*\s*N"
    r"|\bS\s*\*\s*N\b"
    r"|\bz-?independent\b.{0,20}\b(?:capture|completeness)\b"
)


def _shared_lab_in_params_present(window: str) -> list[str]:
    """Return the list of shared LAB-IN pipeline parameters appearing in `window`.

    The conjunction test for the NEW classes (S2 RATIO-OF-PIPELINES, S3
    VARIANCE-FUNCTIONAL) requires >= 1 of these to appear in the gated
    quantity's defining scalings. Symbol tokens (G, S) match standalone only;
    phrase tokens ('calibration constant') match case-insensitively.
    """
    found: list[str] = []  # (local)
    for kw, pat in _SHARED_PARAM_PATTERNS.items():
        if pat.search(window):
            found.append(kw)
    return found


def _both_legs_share_param(window: str) -> tuple[bool, list[str]]:
    """For a two-pipeline ratio, test that a shared LAB-IN parameter scales BOTH
    legs.

    The structural identity (G cancels in the ratio) requires the SAME parameter
    in numerator AND denominator. Operationally: the parameter token must appear
    >= 2 times in the local block (once per leg) OR appear inside an explicit
    'both legs' / 'each leg' / 'numerator and denominator' scaling statement.
    A two-pipeline ratio whose legs scale by DIFFERENT parameters (the synthetic
    NEGATIVE) yields NO shared param -> no flag.
    """
    shared: list[str] = []  # (local)
    explicit_both = bool(
        re.search(
            r"(?i)\bboth\s+legs\b|\beach\s+leg\b|\bnumerator\s+and\s+denominator\b"
            r"|\bsame\b.{0,30}\bscaling",
            window,
        )
    )  # (local)
    for kw, pat in _SHARED_PARAM_PATTERNS.items():
        hits = len(pat.findall(window))  # (local)
        if hits >= 2 or (hits >= 1 and explicit_both):
            shared.append(kw)
    return (len(shared) > 0, shared)


def _mult_cancel_severity(signature_class: str) -> Severity:
    """Severity per signature class. LOG-DERIVATIVE keys on the rule-status
    constant (MANDATORY -> S1); the NEW classes are pinned at S2 (future
    S1-hardening is a separate K-decision, NOT made here)."""
    if signature_class == SIGCLASS_LOG_DERIVATIVE:
        return (
            Severity.S1
            if MULT_CANCELLATION_LOGDERIV_STATUS == "MANDATORY"
            else Severity.S2
        )
    return MULT_CANCEL_NEWCLASS_SEVERITY


# Context window half-width (chars) around each signature match. A single gate
# block's criterion + scaling prose fall within one window; two genuinely
# DISTINCT gate blocks in a real multi-gate plan file are separated by far more.
_MC_WINDOW = 240  # (local) context half-width for the NEW (S2/S3) classes
_MC_WINDOW_LOGDERIV = 160  # (local) tighter window for the S1 class


def _cluster_dedup(spans: list[tuple[int, int, str]], window: int) -> list[tuple[int, int, str]]:
    """Collapse signature matches whose ±`window` context windows OVERLAP into
    ONE representative per cluster (the earliest match in the cluster).

    Rationale: a single gate block mentions its signature more than once (the
    criterion line + the scaling-prose restatement), and multiple sub-patterns
    fire on the same form (e.g. log10(...) AND the bare named ratio inside it).
    Those all describe ONE gated quantity -> ONE finding. But two DISTINCT gate
    blocks (far apart in a multi-gate plan file) have non-overlapping windows ->
    two findings. Clustering on window-overlap gives "one cancellation = one
    finding" without merging genuinely-separate gates.

    `spans` is a list of (start, end, match_text); the returned list preserves
    one (start, end, match_text) per cluster, sorted by start.
    """
    if not spans:
        return []
    ordered = sorted(spans, key=lambda s: s[0])  # (local)
    clusters: list[tuple[int, int, str]] = []  # (local)
    cur_lo, cur_hi, cur_match = (
        ordered[0][0] - window,
        ordered[0][1] + window,
        ordered[0][2],
    )  # (local)
    cur_rep = ordered[0]  # (local) representative (earliest) of the open cluster
    for (s, e, mt) in ordered[1:]:
        w_lo, w_hi = s - window, e + window  # (local)
        if w_lo <= cur_hi:  # window overlaps the open cluster -> same gate block
            cur_hi = max(cur_hi, w_hi)
        else:
            clusters.append(cur_rep)
            cur_lo, cur_hi, cur_rep = w_lo, w_hi, (s, e, mt)
    clusters.append(cur_rep)
    return clusters


def detect_multiplicative_cancellation(plan_text: str) -> list[Finding]:
    """Three-signature-class multiplicative-normalization cancellation detector.

    Statically screens plan-block / substitution-chain text for gated quantities
    whose criterion is ANNIHILATION-INVARIANT under a multiplicative factor — so
    the gate's "plateau"/"zero"/"invariance" is a STRUCTURAL IDENTITY, not
    empirical evidence about the cancelled factor.

      S1 LOG-DERIVATIVE       — d^n ln(.)/d(ln K)^n signatures; the multiplicative
                                spectral-support pre-factor w(L_max)/w(tau)/w(C_2)
                                is annihilated (cancelling_axis = SPECTRAL-SUPPORT,
                                fabric-side). Severity S1 MANDATORY. Routes the
                                plan author to the Sage-MCP sage_simplify
                                factorization check (rule §Plan-freeze pre-flight);
                                the detector is the SCREEN, not the disambiguator.
      S2 RATIO-OF-PIPELINES   — |log10(X_em/X_ref)| / named two-pipeline ratio
                                CONJOINED with a shared LAB-IN parameter (G/H_0/S/
                                calibration) in BOTH legs (cancelling_axis =
                                LAB-IN-PIPELINE, lab-side). Severity S2.
      S3 VARIANCE-FUNCTIONAL  — coefficient-of-variation / Std(N)/Mean(N) /
                                sigma_CV CONJOINED with a flat multiplicative
                                capture/completeness parameter (cancelling_axis =
                                LAB-IN-PIPELINE). Severity S2.

    Returns a list of Findings (possibly empty). A flagged finding is the
    plan-freeze SCREEN that a cancellation is STRUCTURALLY POSSIBLE; for the
    LOG-DERIVATIVE class the Sage factorization check is the disambiguator. For
    the two NEW classes the cancellation is an EXACT algebraic identity (G cancels
    in the ratio; flat S cancels in the fractional variance), so a positive screen
    is structurally decisive that the criterion tests NOTHING about the cancelled
    factor.

    This is the audit-floor F-image (epistemic-discipline.md §Layer-Decomposition)
    of the substrate-IS multiplicative-normalization cancellation theorem proven
    on D_K spectral-support weights at K=3: when a factor enters a gated functional
    multiplicatively, the functional's log-derivative / ratio / normalized-variance
    image annihilates it. The detector now sees that cancellation on BOTH layers —
    the fabric's spectral support (S1) AND the laboratory-IN reduction pipeline
    (S2, S3) where G and S live.
    """
    findings: list[Finding] = []

    # ----- (S1) LOG-DERIVATIVE: log-derivative operator signatures -----------
    # Collect every sub-pattern match, then cluster by context-window overlap so a
    # single gated quantity (criterion + prose restatement; multiple sub-patterns
    # on the same form) yields ONE finding; distinct gate blocks stay distinct.
    logderiv_spans: list[tuple[int, int, str]] = []  # (local)
    for pat in (_PAT_LOGDERIV_ASCII, _PAT_LOGDERIV_UNICODE, _PAT_LOGDERIV_SHORTHAND):
        for m in pat.finditer(plan_text):
            logderiv_spans.append((m.start(), m.end(), m.group(0)))
    for (start, end, match_text) in _cluster_dedup(logderiv_spans, _MC_WINDOW_LOGDERIV):
        findings.append(
            Finding(
                detector="mult_cancellation_lab_in_axis",
                flag=FLAG_MULT_CANCELLATION,
                severity=_mult_cancel_severity(SIGCLASS_LOG_DERIVATIVE),
                message=(
                    f"log-derivative signature '{match_text.strip()[:80]}' admits a "
                    f"multiplicative w(L_max)/w(tau-moduli)/w(C_2^max) factorization "
                    f"candidate — the pre-factor is annihilated by d^n ln/d(ln K)^n, so "
                    f"the L_max/moduli/Casimir 'plateau' is a STRUCTURAL identity, NOT "
                    f"empirical regulator-class evidence. ROUTE: Sage-MCP sage_simplify "
                    f"factorization check (math-scripts.md §Plan-freeze pre-flight items "
                    f"1-4); the detector is the SCREEN, not the disambiguator."
                ),
                detail={
                    "signature_class": SIGCLASS_LOG_DERIVATIVE,
                    "cancelling_axis": AXIS_SPECTRAL_SUPPORT,
                    "match": match_text.strip(),
                    "routes_to": "sage_simplify factorization check (w(L_max)*g(K))",
                    "screen_only": True,
                },
            )
        )

    # ----- (S2) RATIO-OF-PIPELINES: |log10(X_em/X_ref)| + shared lab-IN param -
    ratio_spans: list[tuple[int, int, str]] = []  # (start, end, match) (local)
    for pat in (_PAT_RATIO_LOG10, _PAT_RATIO_NAMED_PIPELINES):
        for m in pat.finditer(plan_text):
            ratio_spans.append((m.start(), m.end(), m.group(0)))
    # Prose marker independently seeds a ratio context.
    for m in _PAT_RATIO_PROSE.finditer(plan_text):
        ratio_spans.append((m.start(), m.end(), m.group(0)))

    for (start, end, match_text) in _cluster_dedup(ratio_spans, _MC_WINDOW):
        lo = max(0, start - _MC_WINDOW)  # (local)
        hi = min(len(plan_text), end + _MC_WINDOW)  # (local)
        window = plan_text[lo:hi]  # (local)
        # CONJUNCTION: a shared LAB-IN parameter must scale BOTH legs (the cancel).
        shared_ok, shared_params = _both_legs_share_param(window)
        if not shared_ok:
            # Two-pipeline ratio with NO shared lab-IN parameter scaling both legs
            # (the synthetic NEGATIVE: legs scale by DIFFERENT params) — NOT a
            # multiplicative-cancellation signature; do NOT flag.
            continue
        findings.append(
            Finding(
                detector="mult_cancellation_lab_in_axis",
                flag=FLAG_MULT_CANCELLATION,
                severity=_mult_cancel_severity(SIGCLASS_RATIO_OF_PIPELINES),
                message=(
                    f"two-pipeline ratio '{match_text.strip()[:60]}' carries a shared "
                    f"LABORATORY-IN parameter {shared_params} in BOTH legs' scalings — the "
                    f"shared factor cancels EXACTLY in the ratio (max_z |log10(X_em/X_ref)| "
                    f"== 0 in the pure shared-factor channel). The criterion tests NOTHING "
                    f"about {shared_params}; a plan-freeze detector keying only on "
                    f"log-derivative signatures cannot see this (the quantity is a "
                    f"log-RATIO-of-pipelines, not a log-derivative)."
                ),
                detail={
                    "signature_class": SIGCLASS_RATIO_OF_PIPELINES,
                    "cancelling_axis": AXIS_LAB_IN_PIPELINE,
                    "match": match_text.strip(),
                    "shared_lab_in_params": shared_params,
                    "identity": "max_z |log10(X_em/X_ref)| == 0 in the pure shared-factor channel",
                },
            )
        )

    # ----- (S3) VARIANCE-FUNCTIONAL: sigma_CV/Std/Mean + flat capture param ----
    variance_spans: list[tuple[int, int, str]] = []  # (local)
    for pat in (_PAT_CV_PROSE, _PAT_STD_OVER_MEAN):
        for m in pat.finditer(plan_text):
            variance_spans.append((m.start(), m.end(), m.group(0)))

    for (start, end, match_text) in _cluster_dedup(variance_spans, _MC_WINDOW):
        lo = max(0, start - _MC_WINDOW)  # (local)
        hi = min(len(plan_text), end + _MC_WINDOW)  # (local)
        window = plan_text[lo:hi]  # (local)
        # CONJUNCTION companion: a FLAT multiplicative capture/completeness param
        # in the same block (the S cancellation companion).
        flat_capture = bool(_PAT_FLAT_CAPTURE.search(window))  # (local)
        if not flat_capture:
            # A coefficient-of-variation form with NO flat multiplicative capture
            # parameter in scope is not a cancellation signature here — do not flag.
            continue
        findings.append(
            Finding(
                detector="mult_cancellation_lab_in_axis",
                flag=FLAG_MULT_CANCELLATION,
                severity=_mult_cancel_severity(SIGCLASS_VARIANCE_FUNCTIONAL),
                message=(
                    f"fractional-variance functional '{match_text.strip()[:60]}' is "
                    f"conjoined with a FLAT multiplicative capture/completeness parameter S "
                    f"in the same block — S cancels EXACTLY in the coefficient of variation "
                    f"(sigma_CV(S*N) = Std(S*N)/Mean(S*N) = Std(N)/Mean(N) = sigma_CV(N)). "
                    f"The variance criterion carries ZERO sensitivity to the capture "
                    f"normalization S (cancelling_axis = LAB-IN-PIPELINE)."
                ),
                detail={
                    "signature_class": SIGCLASS_VARIANCE_FUNCTIONAL,
                    "cancelling_axis": AXIS_LAB_IN_PIPELINE,
                    "match": match_text.strip(),
                    "flat_capture_param": "S",
                    "identity": "sigma_CV(S*N) == sigma_CV(N) (flat S annihilated)",
                },
            )
        )

    return findings


# ---------------------------------------------------------------------------
# Detector registry — add a detector here in ONE line (no restructuring)
# ---------------------------------------------------------------------------

DETECTOR_REGISTRY: dict = {
    "selection_rule_preflight": detect_selection_rule_preflight,
    # W8a-2 extension (S101) — 3-signature-class multiplicative-normalization
    # cancellation detector (LOG-DERIVATIVE / RATIO-OF-PIPELINES / VARIANCE-FUNCTIONAL):
    "mult_cancellation_lab_in_axis": detect_multiplicative_cancellation,
}


def run_all_detectors(plan_text: str) -> list[Finding]:
    """Run every registered detector over plan_text; return the merged findings."""
    out: list[Finding] = []
    for name, detector in DETECTOR_REGISTRY.items():
        out.extend(detector(plan_text))
    return out


# ---------------------------------------------------------------------------
# Self-test fixtures (pinned in plan §W8a-1 machinery_pin_map)
# ---------------------------------------------------------------------------

# Synthetic POSITIVE — the W2-2 form: <psi_(1,0)| |s(h)|^2 |psi_(1,1)> != 0
# asserted via a sector-connecting-weight argument. MUST be flagged
# SELECTION-RULE-PREFLIGHT-VIOLATION (t: 1 != 0+0 mod 3).
FIXTURE_POSITIVE = (
    "The pre-registered element <psi_(1,0)| |s(h)|^2 |psi_(1,1)> != 0 is "
    "generically nonzero, since the C^2 weight in su(3) connects triality-adjacent "
    "sectors, so the overlap does not vanish by symmetry."
)

# Synthetic NEGATIVE — <psi_(1,1)| s(h) |psi_(1,0)> != 0 with s(h) declared in
# irrep (2,0). MUST pass (t: 0 == (1+2) mod 3 = 0; CG-admissible at center level).
FIXTURE_NEGATIVE = (
    "The off-diagonal element <psi_(1,1)| s(h) |psi_(1,0)> != 0 with s(h) in (2,0) "
    "carries a non-vanishing center-allowed channel; the s-LINEAR coupling connects "
    "these sectors at the center-character level."
)

# ---------------------------------------------------------------------------
# Self-test fixtures — Detector 2 (multiplicative-normalization cancellation,
# 3 signature classes). FOUR fixtures: one synthetic POSITIVE per class
# (S1 LOG-DERIVATIVE, S2 RATIO-OF-PIPELINES, S3 VARIANCE-FUNCTIONAL) + ONE
# synthetic NEGATIVE (a two-pipeline ratio whose legs scale by DIFFERENT
# parameters — no shared factor; MUST NOT be flagged). Pinned in plan §W8a-2.
# ---------------------------------------------------------------------------

# (S1) POSITIVE — a gated quantity defined as a second log-derivative
# d² ln κ / d(ln K)²; the multiplicative spectral-support pre-factor w(L_max) is
# annihilated. MUST be flagged signature_class=LOG-DERIVATIVE, axis=SPECTRAL-SUPPORT.
FIXTURE_MC_POS_LOGDERIV = (
    "Gate criterion: the late-time running R_KW(tau_fold, L_max) = "
    "d^2 ln(kappa_FULL-PV(K)) / d(ln K) is evaluated at the horizon scale and its "
    "L_max-stability across L_max in {10,...,15} is the PASS predicate; the second "
    "log-derivative annihilates the multiplicative spectral-support weight w(L_max)."
)

# (S2) POSITIVE — |log10(n_ACH_em/n_ACH_ref)| with the SHARED lab-IN parameter G
# (Newton's constant) scaling BOTH legs (the W7-2 C2a G-cancellation form). MUST
# be flagged signature_class=RATIO-OF-PIPELINES, axis=LAB-IN-PIPELINE.
FIXTURE_MC_POS_RATIO = (
    "Gate criterion: max_z |log10(n_ACH_em/n_ACH_ref)| <= 0.5 dex. Pipeline scalings: "
    "M_ACH ~ 1/(G*H) and rho_m,0 ~ 1/G enter BOTH the emission and reference legs "
    "identically (the borrowed-(H_0, Omega, sigma_8) baseline carries G in numerator "
    "and denominator); the count above the fixed T_vir threshold is G-free, so the "
    "Newton-constant G cancels in the ratio of the two pipelines."
)

# (S3) POSITIVE — coefficient of variation sigma_CV = Std(N)/Mean(N) conjoined with
# a FLAT multiplicative capture S (z-independent completeness) — the W7-3 A2 flat-S
# form. MUST be flagged signature_class=VARIANCE-FUNCTIONAL, axis=LAB-IN-PIPELINE.
FIXTURE_MC_POS_VARIANCE = (
    "Gate criterion: the fractional count variance sigma_CV = Std(N)/Mean(N) over the "
    "redshift-binned count vector N is the PASS predicate. A flat multiplicative survey "
    "capture S (z-independent completeness) maps N -> S*N; the coefficient of variation "
    "is the normalized variance, so the flat capture S cancels exactly."
)

# (NEGATIVE) — a two-pipeline ratio X_em/X_ref whose legs scale by DIFFERENT
# parameters (numerator carries G, denominator carries H_0 ALONE — no shared
# factor). MUST NOT be flagged (no multiplicative cancellation across the ratio).
FIXTURE_MC_NEGATIVE = (
    "Gate criterion: the ratio X_em/X_ref discriminates the two models. The emission "
    "pipeline scales as X_em ~ 1/G (Newton-constant control only), while the reference "
    "pipeline scales as X_ref ~ H_0 (Hubble control only); the legs carry DIFFERENT "
    "parameters with no common factor, so nothing cancels across the ratio and the "
    "discrimination is genuine."
)


def _self_test_mult_cancellation() -> int:
    """Run the FOUR Detector-2 fixtures + assert flag/no-flag + class/axis behavior.

    NUMBERS/STRUCTURE FIRST — the two exact-cancellation identities the corpus
    documents are re-stated here as the calibration content (NOT re-derived):
      RATIO-OF-PIPELINES:  max_z |log10(n_ACH_em/n_ACH_ref)| == 0 by G-cancellation
                           (every G-factor appears identically in both legs).
      VARIANCE-FUNCTIONAL: sigma_CV(S*N) = (S*Std(N))/(S*Mean(N)) = Std(N)/Mean(N)
                           = sigma_CV(N) — flat S annihilated.
    Returns 0 iff ALL FOUR assertions hold; nonzero on a broken module.
    """
    ok = True

    def _classes(findings: list[Finding]) -> list[str]:
        return [f.detail.get("signature_class") for f in findings]  # (local)

    def _axes(findings: list[Finding]) -> list[str]:
        return [f.detail.get("cancelling_axis") for f in findings]  # (local)

    # --- (S1) POSITIVE: LOG-DERIVATIVE flagged, axis SPECTRAL-SUPPORT, S1 -----
    s1 = detect_multiplicative_cancellation(FIXTURE_MC_POS_LOGDERIV)  # (local)
    s1_logderiv = [
        f for f in s1
        if f.detail.get("signature_class") == SIGCLASS_LOG_DERIVATIVE
        and f.flag == FLAG_MULT_CANCELLATION
    ]  # (local)
    if not s1_logderiv:
        print(
            "[self-test:MC] FAIL: S1 LOG-DERIVATIVE positive NOT flagged "
            f"{FLAG_MULT_CANCELLATION}; classes={_classes(s1)}",
            file=sys.stderr,
        )
        ok = False
    elif not (
        s1_logderiv[0].detail.get("cancelling_axis") == AXIS_SPECTRAL_SUPPORT
        and s1_logderiv[0].severity == Severity.S1
    ):
        print(
            "[self-test:MC] FAIL: S1 axis/severity wrong; "
            f"axis={s1_logderiv[0].detail.get('cancelling_axis')} "
            f"severity={s1_logderiv[0].severity.value} (expect SPECTRAL-SUPPORT / S1)",
            file=sys.stderr,
        )
        ok = False
    else:
        print(
            "[self-test:MC] PASS: S1 LOG-DERIVATIVE flagged "
            "(axis=SPECTRAL-SUPPORT, severity=S1 MANDATORY; routes to sage_simplify)"
        )

    # --- (S2) POSITIVE: RATIO-OF-PIPELINES flagged, axis LAB-IN, shared G, S2 -
    s2 = detect_multiplicative_cancellation(FIXTURE_MC_POS_RATIO)  # (local)
    s2_ratio = [
        f for f in s2
        if f.detail.get("signature_class") == SIGCLASS_RATIO_OF_PIPELINES
        and f.flag == FLAG_MULT_CANCELLATION
    ]  # (local)
    if not s2_ratio:
        print(
            "[self-test:MC] FAIL: S2 RATIO-OF-PIPELINES positive NOT flagged; "
            f"classes={_classes(s2)}",
            file=sys.stderr,
        )
        ok = False
    else:
        d = s2_ratio[0].detail  # (local)
        shared = d.get("shared_lab_in_params", [])  # (local)
        if not (
            d.get("cancelling_axis") == AXIS_LAB_IN_PIPELINE
            and "G" in shared
            and s2_ratio[0].severity == Severity.S2
        ):
            print(
                "[self-test:MC] FAIL: S2 axis/shared-param/severity wrong; "
                f"axis={d.get('cancelling_axis')} shared={shared} "
                f"severity={s2_ratio[0].severity.value} (expect LAB-IN-PIPELINE / G in shared / S2)",
                file=sys.stderr,
            )
            ok = False
        else:
            print(
                "[self-test:MC] PASS: S2 RATIO-OF-PIPELINES flagged "
                "(axis=LAB-IN-PIPELINE, shared G, severity=S2; "
                "max_z|log10(n_em/n_ref)|==0 by G-cancellation)"
            )

    # --- (S3) POSITIVE: VARIANCE-FUNCTIONAL flagged, axis LAB-IN, flat S, S2 --
    s3 = detect_multiplicative_cancellation(FIXTURE_MC_POS_VARIANCE)  # (local)
    s3_var = [
        f for f in s3
        if f.detail.get("signature_class") == SIGCLASS_VARIANCE_FUNCTIONAL
        and f.flag == FLAG_MULT_CANCELLATION
    ]  # (local)
    if not s3_var:
        print(
            "[self-test:MC] FAIL: S3 VARIANCE-FUNCTIONAL positive NOT flagged; "
            f"classes={_classes(s3)}",
            file=sys.stderr,
        )
        ok = False
    elif not (
        s3_var[0].detail.get("cancelling_axis") == AXIS_LAB_IN_PIPELINE
        and s3_var[0].severity == Severity.S2
    ):
        print(
            "[self-test:MC] FAIL: S3 axis/severity wrong; "
            f"axis={s3_var[0].detail.get('cancelling_axis')} "
            f"severity={s3_var[0].severity.value} (expect LAB-IN-PIPELINE / S2)",
            file=sys.stderr,
        )
        ok = False
    else:
        # Numbers-first cross-check of the S-invariance identity (exact).
        # sigma_CV(S*N) = (S*Std(N))/(S*Mean(N)) = Std(N)/Mean(N) for any S != 0.
        s_test = 7.0  # (local) arbitrary flat capture scalar
        n_vec = [3.0, 5.0, 8.0, 6.0]  # (local) synthetic count vector
        mean_n = sum(n_vec) / len(n_vec)  # (local)
        var_n = sum((x - mean_n) ** 2 for x in n_vec) / len(n_vec)  # (local)
        std_n = var_n ** 0.5  # (local)
        cv_n = std_n / mean_n  # (local)
        sn_vec = [s_test * x for x in n_vec]  # (local)
        mean_sn = sum(sn_vec) / len(sn_vec)  # (local)
        var_sn = sum((x - mean_sn) ** 2 for x in sn_vec) / len(sn_vec)  # (local)
        std_sn = var_sn ** 0.5  # (local)
        cv_sn = std_sn / mean_sn  # (local)
        if abs(cv_sn - cv_n) > 1e-12:
            print(
                "[self-test:MC] FAIL: S-invariance identity broke numerically; "
                f"cv(N)={cv_n} cv(S*N)={cv_sn}",
                file=sys.stderr,
            )
            ok = False
        else:
            print(
                "[self-test:MC] PASS: S3 VARIANCE-FUNCTIONAL flagged "
                f"(axis=LAB-IN-PIPELINE, flat S, severity=S2; "
                f"sigma_CV(S*N)={cv_sn:.10f} == sigma_CV(N)={cv_n:.10f} exact)"
            )

    # --- (NEGATIVE): two-pipeline ratio, DIFFERENT params per leg, ZERO flags -
    neg = detect_multiplicative_cancellation(FIXTURE_MC_NEGATIVE)  # (local)
    if neg:
        print(
            "[self-test:MC] FAIL: NEGATIVE (legs scale by DIFFERENT params) produced "
            f"findings (expected zero); classes={_classes(neg)} axes={_axes(neg)}",
            file=sys.stderr,
        )
        ok = False
    else:
        print(
            "[self-test:MC] PASS: NEGATIVE produced zero findings "
            "(X_em~1/G, X_ref~H_0 — no shared factor; nothing cancels across the ratio)"
        )

    if ok:
        print("[self-test:MC] ALL 4 FIXTURES HOLD — Detector 2 behaves as pinned.")
        return 0
    print("[self-test:MC] BROKEN — at least one Detector-2 fixture failed.", file=sys.stderr)
    return 1


def _self_test() -> int:
    """Run the two pinned fixtures + assert the expected flag/no-flag behavior.

    Returns 0 iff ALL assertions hold (the detectors behave as pinned), nonzero
    on a broken module (a fixture misbehaving = script breakage per the exit-code
    semantics).
    """
    ok = True

    # --- Synthetic POSITIVE: MUST be flagged SELECTION-RULE-PREFLIGHT-VIOLATION ---
    pos = detect_selection_rule_preflight(FIXTURE_POSITIVE)
    pos_flags = [f.flag for f in pos]
    pos_violation = [f for f in pos if f.flag == FLAG_SELECTION_RULE_VIOLATION]
    if not pos_violation:
        print(
            "[self-test] FAIL: synthetic-POSITIVE was NOT flagged "
            f"{FLAG_SELECTION_RULE_VIOLATION}; flags={pos_flags}",
            file=sys.stderr,
        )
        ok = False
    else:
        d = pos_violation[0].detail
        # Numbers-first cross-check: t(bra)=1, rhs=(t(ket)+t_O)%3=(0+0)%3=0, 1!=0.
        if not (d.get("t_bra") == 1 and d.get("rhs") == 0 and d.get("lhs") == 1):
            print(
                "[self-test] FAIL: synthetic-POSITIVE triality arithmetic wrong; "
                f"expected t_bra=1 lhs=1 rhs=0, got t_bra={d.get('t_bra')} "
                f"lhs={d.get('lhs')} rhs={d.get('rhs')}",
                file=sys.stderr,
            )
            ok = False
        else:
            print(
                "[self-test] PASS: synthetic-POSITIVE flagged "
                f"{FLAG_SELECTION_RULE_VIOLATION} (t_bra=1 != (t_ket+t_O) mod 3 = 0)"
            )

    # --- Synthetic NEGATIVE: MUST produce zero findings ---
    neg = detect_selection_rule_preflight(FIXTURE_NEGATIVE)
    if neg:
        print(
            "[self-test] FAIL: synthetic-NEGATIVE produced findings (expected zero); "
            f"flags={[f.flag for f in neg]}",
            file=sys.stderr,
        )
        ok = False
    else:
        # Cross-check the admissibility arithmetic explicitly: t(1,1)=0 ==
        # (t(1,0)+t_O) mod 3 = (1+2) mod 3 = 0.
        t_bra = _triality(1, 1)
        t_ket = _triality(1, 0)
        t_op = _operator_center_character("s(h) in (2,0)")
        rhs = (t_ket + t_op) % 3
        if not (t_bra == rhs == 0 and t_op == 2):
            print(
                "[self-test] FAIL: synthetic-NEGATIVE admissibility arithmetic wrong; "
                f"t_bra={t_bra} t_ket={t_ket} t_op={t_op} rhs={rhs}",
                file=sys.stderr,
            )
            ok = False
        else:
            print(
                "[self-test] PASS: synthetic-NEGATIVE produced zero findings "
                "(t(1,1)=0 == (t(1,0)+t_O) mod 3 = (1+2) mod 3 = 0; CG-admissible)"
            )

    if ok:
        print("[self-test] ALL ASSERTIONS HOLD — module behaves as pinned.")
        return 0
    print("[self-test] BROKEN — at least one assertion failed.", file=sys.stderr)
    return 1


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def _audit_plan_file(plan_path: Path, as_json: bool) -> int:
    """Run all detectors over a plan file; print findings. Exit 0 regardless of
    finding count (findings are DATA, not script error)."""
    try:
        text = plan_path.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"ERROR: cannot read plan file {plan_path}: {exc}", file=sys.stderr)
        return 2  # script breakage (input missing) — NOT a finding verdict
    findings = run_all_detectors(text)
    if as_json:
        print(json.dumps([f.to_dict() for f in findings], indent=2, sort_keys=True))
    else:
        if not findings:
            print(f"{plan_path}: 0 findings (no machinery-feasibility defect detected).")
        else:
            print(f"{plan_path}: {len(findings)} finding(s).")
            for f in findings:
                print(f"  [{f.severity.value}] {f.flag} ({f.detector}): {f.message}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Plan-freeze machinery-feasibility audit "
            "(math-scripts.md §:86 / §:141 / §:305). "
            "Runs the registered detectors over a session plan file."
        )
    )
    parser.add_argument(
        "plan_file",
        nargs="?",
        default=None,
        help="path to a session plan file to audit",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="emit findings as JSON",
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="run the pinned fixtures and assert detector behavior; "
        "exit 0 iff all assertions hold",
    )
    args = parser.parse_args(argv)

    if args.self_test:
        # Run EVERY detector's self-test; the module is healthy iff all pass.
        rc_selrule = _self_test()  # (local) Detector 1 (W8a-1)
        rc_multcancel = _self_test_mult_cancellation()  # (local) Detector 2 (W8a-2)
        return 0 if (rc_selrule == 0 and rc_multcancel == 0) else 1

    if args.plan_file is None:
        parser.print_help(sys.stderr)
        return 2  # usage error (no plan file, no --self-test) — script-health, not a verdict
    return _audit_plan_file(Path(args.plan_file), args.json)


if __name__ == "__main__":
    sys.exit(main())
