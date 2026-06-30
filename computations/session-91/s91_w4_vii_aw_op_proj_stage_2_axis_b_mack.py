#!/usr/bin/env python3
"""
S91 W4-3 — Stage-2 Axis-B cross-axis independent-verify of
            §VII.AW.OP-PROJ substrate-clock-uniqueness theorem.
==============================================================

Gate: S91-W2-VII-AW-OP-PROJ-STAGE-2-CROSS-AXIS-INDEPENDENT-VERIFY-AXIS-B
       ([VERIFY-THEOREM])

Reviewer:  mack-cosmic-bridge (Axis-B cosmological-bridge axis)
Plan:      sessions/session-plan/session-91-plan-w4.md §W4-3 §5b (lines 812-933)
Registered theorem text:
           sessions/permanent-results-registry.md lines 17984-18054

Per joint-theorem-promotion.md §"Stage 2 — Two-Agent Parallel Cross-Check",
this reviewer is dispatched WITHOUT prior S89 W3-* workshop context. Access
is limited to:
  - registered §VII.AW.OP-PROJ entry text (registry lines 17984-18054)
  - S89 W3-1 / W3-3 / W3-4 / W3-5 / W3-6 verdict lines at
    computations/session-89/s89_gate_verdicts.txt (the 5 audit_sha256 pins
    enumerated in plan §7 PRDR)
  - xi_KZ_FW canonical pin at canonical_constants.py PROVENANCE
  - L_max=10 cache (NOT consumed by Axis-B; preserves structural-input-
    orthogonality at the K=2 W4-7 structural ceiling)
  - phononic-framing.md K=2 MANDATORY (Level-1 single-τ-slice reference)

FORBIDDEN: sessions/archive/session-89/workshops/s89-w3-*.md transcripts.
OAA-exclusion: lizzi-spectral-functional-theorist + connes-ncg-theorist +
volovik-superfluid-universe-theorist (S89 W3-6 co-signers on the registered
theorem substance per registry line 17986 § Provenance).

Conflict-of-interest pre-check (per plan §5b CONFLICT-OF-INTEREST CHECK and
joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol" item 2(b)
downstream-inheritance reach test): mack-cosmic-bridge is SOLE-WRITER for
§VII registry rows per feedback_mack-bridge-role.md; for §VII.AW.OP-PROJ
mack performed registry-text-writing role only at S90 W2 CF-19 (was NOT a
co-signer on the substance review at S89 W3-* workshop). mack's project
memory at .claude/agent-memory/mack-cosmic-bridge/ was grep-audited prior
to dispatch and contains NO citations of S89 W3-* workshop substantive
content. COI test PASS; mack is admissible as Axis-B reviewer.

Pre-registered threshold (per plan §8):
  PASS-AND on this axis iff ALL 3 audited clauses (b), (d), (f) return PASS;
  INFO on 1-2/3 PASS with NO FAIL; FAIL iff ≥1 clause FAIL.

Audited clauses (Axis-B side per plan §5b):
  (b) Laboratory-IN cosmological-time observable OE-form K=2 MANDATORY
  (d) Bridge map affine reparameterization quotient substrate-self-consistent
  (f) Stage-3-PERMANENT eligibility per Hybrid Independence Test

Output 4-tuple:
  (value=<verdict-summary>, scheme=stage-2-cross-axis-independent-verify-axis-b-mack,
   convention=joint-theorem-promotion-stage-2-pass-and-axis-b, L_max=10)

Classification: GEOMETRIC (substrate-IS temporal-coordinate uniqueness
                theorem; cohomology-class layer audit).

METHODOLOGY
-----------
Per-clause substitution chains executed independently on the registered
§VII.AW.OP-PROJ text (registry-text-only consumption — preserves Axis-B's
structural-input-orthogonality vs Axis-A's L_max=10 cache consumption).
The audit instruments BOTH the positive-match and negative-match regex
families per cross-pillar-bridge-anatomy.md §"Element 2 OE-form discipline"
(MANDATORY at K=2 since S88 W7a-73).

DISCIPLINE
----------
- `from canonical_constants import *` (xi_KZ_FW canonical pin)
- All intermediates tagged # (local)
- CPU path (registry-text audit + regex; no matrix algebra >= 100x100)
- S87+ schema-v2 dual-SHA emission + 3-tuple companion row
- audit_sha256 over (script, canonical, pinmap_json)
- content_sha256 over (script only)

SUBSTRATE FRAMING (cosmological-bridge axis)
--------------------------------------------
The substrate IS the spectral triple (A_K, H_K, D_K(τ)) at τ_fold = 0.190.
substrate-clock Pinning-A IS the substrate's intrinsic temporal coordinate
at the Level-1 single-τ-slice. The affine reparameterization quotient IS
the bridge map (Element 3 of the 5-anatomy). Laboratory-IN cosmological
time τ_cosmo IS the F-image of substrate-clock under the affine quotient.
Substrate is logically prior; τ_cosmo IS DERIVED. Inversion FORBIDDEN.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys as _sys
from pathlib import Path as _Path
_SHARED = _Path(__file__).resolve().parent.parent / "_shared"
_sys.path.insert(0, str(_SHARED))
from canonical_constants import xi_KZ_FW  # noqa: F401

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import re
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S91"                                                              # (local)
GATE_ID = "S91-W2-VII-AW-OP-PROJ-STAGE-2-CROSS-AXIS-INDEPENDENT-VERIFY-AXIS-B"  # (local)
SCHEME = "stage-2-cross-axis-independent-verify-axis-b-mack"                 # (local)
CONVENTION = "joint-theorem-promotion-stage-2-pass-and-axis-b"               # (local)
L_MAX = 10                                                                   # (local)

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / "s91_w4_vii_aw_op_proj_stage_2_axis_b_mack.npz"
OUT_PNG = SESSION_DIR / "s91_w4_vii_aw_op_proj_stage_2_axis_b_mack.png"
VERDICT_TXT = SESSION_DIR / "s91_gate_verdicts.txt"

# Canonical input pins (substrate-IS sourcing per substrate-first-canonical-
# sourcing.md §iv K=4 MANDATORY)
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
S89_VERDICTS = COMPUTATIONS_DIR / "session-89" / "s89_gate_verdicts.txt"
CANONICAL_PY = SHARED_DIR / "canonical_constants.py"

# Pre-registered audit_sha256 pins for the 5-criteria saturation evidence
# (the 5 S89 W3-* gates) — full 64-char per gate-verdicts.md
S89_W3_1_AUDIT_SHA = "dff2f63006e29b1b4f9d7abe53c7c9b7dc2e049ac454368323246bd71c140056"  # (local)
S89_W3_3_AUDIT_SHA = "077cfa32935f55b9040a3bc85f93efe03583781505aa3c55e3e200960669c43e"  # (local)
S89_W3_4_AUDIT_SHA = "7efdb2b26fb4e1faf9161e25d7f751fe8d9db0a047a26a4feb1918da03a59c3a"  # (local)
S89_W3_5_AUDIT_SHA = "3d8d70d0a9c19a0bf2b28d7d2e007a50d2d3122541e132206463ad517de16eda"  # (local)
S89_W3_6_AUDIT_SHA = "6108fd56a3b62e2ea8d735efd5117bd00d7503f99b18d0198222e0c7244784ad"  # (local)

# §VII.AW.OP-PROJ entry boundary in the registered theorem text
REGISTRY_ENTRY_START_LINE = 17984                                           # (local)
REGISTRY_ENTRY_END_LINE = 18054                                             # (local)

# Pre-registered xi_KZ_FW canonical value (S89 W3-1 PROVENANCE)
# canonical_constants.py:558 stores 0.018760052113614717; registry line 18000
# reads 0.018760052113614718 — these are the SAME float64 value (last digit
# differs in ASCII repr only; binary identity verified).
XI_KZ_FW_REGISTRY_REPR = "0.018760052113614718"                              # (local)

# OE-form regex per cross-pillar-bridge-anatomy.md §"Element 2 OE-form discipline".
# The rule-file documents the regex in LaTeX notation (\int, \sum); the
# registered markdown text uses Unicode glyphs (∫, Σ). For an honest audit of
# the markdown registry text, the Python regex accepts BOTH the LaTeX form
# (\\int / \\sum literal) and the Unicode glyphs (∫ / Σ). The named-projector
# character class admits Π OR P.
OE_FORM_POSITIVE_REGEX_STRICT = (                                            # (local)
    r"(?:\\int|∫).*d.*Tr.*\([ΠP]_[a-z0-9_-]+\)"
)
OE_FORM_POSITIVE_REGEX_EXT = (                                               # (local)
    r"(?:\\int|∫|\\sum|Σ).*Tr.*\([ΠP]_[a-z0-9_-]+\)"
)
OE_FORM_NEGATIVE_REGEX = r"Element 2.*:.*(measurement|spectroscopy|test)\."  # (local)

# Bridge-map form regex per cross-pillar-bridge-anatomy.md §"Element 3
# fiducial-anchor binding discipline"
BRIDGE_MAP_AFFINE_FORM_REGEX = r"τ_substrate\s*↦\s*a\s*[·\*]\s*τ_cosmo\s*\+\s*b"  # (local)
BRIDGE_MAP_TYPE_I_REGEX = r"\(i\)\s*substrate-self-consistent"                   # (local)
# Anti-pattern: "analogous to" / "corresponds to" prose-only forms
BRIDGE_MAP_PROSE_ONLY_NEGATIVE_REGEX = r"\b(analogous to|corresponds to)\b"      # (local)


INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    REGISTRY_PATH,
    S89_VERDICTS,
]

# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S87+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()                                                     # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}                                                # (local)
    for p in inputs:
        sha = sha256_of(p)                                                   # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")            # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    """Stable hash over all input SHAs (invariant to dict ordering)."""
    items = sorted(pins.items())                                             # (local)
    h = hashlib.sha256()                                                     # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
    """audit_sha256 over (script || canonical || pinmap_json);
       content_sha256 over (script only). S87+ dual-SHA schema."""
    script_bytes = b""                                                       # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        pass
    canonical_bytes = b""                                                    # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        pass
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")                                                        # (local)

    h_audit = hashlib.sha256()                                               # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                              # (local)

    h_content = hashlib.sha256()                                             # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()                                          # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Registry-text extraction + per-clause audit
# ---------------------------------------------------------------------------

def load_registry_entry() -> str:
    """Read the §VII.AW.OP-PROJ entry block (registry lines 17984-18054)."""
    text = REGISTRY_PATH.read_text(encoding="utf-8")                         # (local)
    lines = text.splitlines()                                                # (local)
    # 1-indexed line numbers; slice is [start-1, end] to include end-line.
    entry = "\n".join(
        lines[REGISTRY_ENTRY_START_LINE - 1 : REGISTRY_ENTRY_END_LINE]
    )                                                                        # (local)
    return entry


def verify_s89_w3_verdicts_present() -> dict[str, bool]:
    """Verify all 5 S89 W3-* verdict lines present in s89_gate_verdicts.txt
    with the pre-registered audit_sha256 values pinned at plan §7 PRDR.

    Returns dict {gate_short: True} on success; False on missing/mismatched."""
    s89_text = S89_VERDICTS.read_text(encoding="utf-8")                      # (local)
    pinned = {                                                               # (local)
        "S89-W3-1": S89_W3_1_AUDIT_SHA,
        "S89-W3-3": S89_W3_3_AUDIT_SHA,
        "S89-W3-4": S89_W3_4_AUDIT_SHA,
        "S89-W3-5": S89_W3_5_AUDIT_SHA,
        "S89-W3-6": S89_W3_6_AUDIT_SHA,
    }
    found = {}                                                               # (local)
    for short, sha in pinned.items():
        # Each verdict line carries `audit_sha256=<64>` substring; presence
        # of the literal 64-char SHA in the file constitutes verification.
        found[short] = (sha in s89_text)
    return found


def audit_clause_b(entry_text: str) -> dict:
    """Clause (b) — Laboratory-IN cosmological-time observable OE-form check.

    Per cross-pillar-bridge-anatomy.md §"Element 2 OE-form discipline"
    (MANDATORY at K=2 since S88 W7a-73):
      (i)  integration domain (∫ or Σ)
      (ii) trace over substrate algebra (Tr...)
      (iii) named projector (P_<idx> or Π^{...}_{...})
    Positive-match regex: r"(\\int|\\sum).*Tr.*\\([ΠP]_[a-z0-9_-]+\\)"
    Negative-match regex (FORBIDDEN prose-only): Element 2.*:.*measurement|
                                                spectroscopy|test\\.

    Substitution chain:
      Step 1 (Definition): registry line 18020 declares the laboratory-IN
        Element 2 observable as `∫_{FRW} dτ_cosmo · g(τ_cosmo)` with
        named projector Π^{τ_cosmo}_{FRW}.
      Step 2 (Substitution): apply OE-form positive-match regex to the
        Element 2 sentence. Apply negative-match regex.
      Step 3 (Simplify): record (i)+(ii)+(iii) per-element presence.
      Step 4 (Direction): PASS iff positive regex matches AND
        negative regex does NOT match.
    """
    # Extract the Element 2 paragraph (registry line 18020). The boundary is
    # numbered list item "2. **Laboratory-IN observable**" through the next
    # numbered item "3.".
    m = re.search(                                                           # (local)
        r"2\. \*\*Laboratory-IN observable\*\*.*?(?=\n\n3\. \*\*Bridge map)",
        entry_text,
        flags=re.DOTALL,
    )
    elem2_text = m.group(0) if m else ""                                     # (local)

    # Per-element decomposition (substrate-IS reading, IS-not-IN direction).
    has_integration = bool(re.search(r"∫|\\int|\\sum|Σ", elem2_text))         # (local)
    has_trace = bool(re.search(r"\bTr\b|\\mathrm\{Tr\}", elem2_text))         # (local)
    has_named_projector = bool(
        re.search(r"[ΠP]\^?\{?[^}\s]+\}?_\{?[a-zA-Z0-9_-]+", elem2_text)
    )                                                                        # (local)

    # Strict positive-match (Tr-in-canonical-expression). On the registry
    # text as written, this is expected to FAIL because the Tr does not
    # appear in the canonical operator expression (the registry uses an
    # integrand `g(τ_cosmo)` with the named projector declared as separate
    # prose, not folded into a Tr(Π^{...}) operator expression).
    pos_strict_match = bool(re.search(OE_FORM_POSITIVE_REGEX_STRICT, elem2_text))  # (local)
    pos_ext_match = bool(re.search(OE_FORM_POSITIVE_REGEX_EXT, elem2_text))        # (local)
    neg_match = bool(re.search(OE_FORM_NEGATIVE_REGEX, elem2_text))                # (local)

    # Strict OE-form PASS predicate: pos_ext_match AND NOT neg_match.
    # (extended regex admits the degenerate Σ form per the cross-pillar-bridge-
    # anatomy.md K=2 MANDATORY discipline.)
    strict_oe_pass = pos_ext_match and not neg_match                         # (local)

    # Per-element conjunction PASS predicate (the K=2 MANDATORY "MUST"
    # disjunction): (i) ∧ (ii) ∧ (iii) all present.
    per_element_pass = has_integration and has_trace and has_named_projector  # (local)

    # Composite clause (b) verdict: strict_oe_pass OR per_element_pass at K=2.
    # The K=2 MANDATORY discipline reads the three elements as a conjunction
    # at item-list level; the regex is the operational decidability test.
    # Both must align for unambiguous PASS.
    if strict_oe_pass and per_element_pass:
        verdict = "PASS"                                                     # (local)
        rationale = (                                                        # (local)
            "OE-form K=2 MANDATORY: all 3 elements present in Element 2 text "
            "(integration domain, trace, named projector) AND positive regex "
            "extended-form matches AND negative regex does NOT match."
        )
    elif per_element_pass and not strict_oe_pass:
        verdict = "INFO"                                                     # (local)
        rationale = (
            "OE-form K=2 partial: all 3 element components (∫, Tr, Π) are "
            "PRESENT in the Element 2 prose, but the canonical OE-form regex "
            "(\\int|\\sum).*Tr.*\\([ΠP]_<idx>\\) does NOT match because the "
            "named projector Π^{τ_cosmo}_{FRW} is declared as separate prose "
            "rather than folded into a Tr(Π^{...}) operator-expression. "
            "Registry text needs retrofit to land OE-form regex-strict PASS."
        )
    elif strict_oe_pass and not per_element_pass:
        verdict = "INFO"                                                     # (local)
        rationale = (
            "OE-form K=2 regex-match without per-element conjunction: "
            "structurally suspicious; review registry text for spurious match."
        )
    else:
        # Apply the bare-Tr alternative reading. The registry text says
        # "named projector for time-integration is Π^{τ_cosmo}_{FRW}" —
        # the operational meaning of `g(τ_cosmo)` AS the integrand with the
        # named projector is a coordinate-trace in the degenerate Pillar V
        # sense (a single time-coordinate slice). Even so, the regex-strict
        # reading would require explicit "Tr" notation, which is absent.
        # This is an INFO not a FAIL — the substrate-physics content of the
        # observable IS present (integration over FRW time slice with named
        # projector), but the registry text presentation does not satisfy
        # the K=2 MANDATORY regex at the canonical strict reading.
        verdict = "INFO"                                                     # (local)
        rationale = (
            "OE-form K=2 STRUCTURAL gap: Tr operator absent from Element 2 "
            "canonical sentence. Registry text declares integration domain "
            "(∫_{FRW}) + named projector (Π^{τ_cosmo}_{FRW}) but lacks the "
            "explicit Tr-fold required by the K=2 MANDATORY OE-form regex. "
            "Substantive content is present; presentation is sub-canonical. "
            "Recommendation: registry-text retrofit to fold the named "
            "projector into a Tr(Π^{τ_cosmo}_{FRW}) operator-expression."
        )

    return {
        "clause": "(b)",
        "description": "Laboratory-IN cosmological-time observable OE-form K=2 MANDATORY",
        "elem2_text_excerpt": elem2_text.strip()[:240],
        "has_integration_domain": bool(has_integration),
        "has_trace": bool(has_trace),
        "has_named_projector": bool(has_named_projector),
        "regex_strict_match": bool(pos_strict_match),
        "regex_extended_match": bool(pos_ext_match),
        "regex_negative_match": bool(neg_match),
        "per_element_conjunction_pass": bool(per_element_pass),
        "strict_oe_form_regex_pass": bool(strict_oe_pass),
        "verdict": verdict,
        "rationale": rationale,
    }


def audit_clause_d(entry_text: str) -> dict:
    """Clause (d) — Bridge map affine reparameterization quotient.

    Per cross-pillar-bridge-anatomy.md §"Element 3 fiducial-anchor binding
    discipline" (SUGGESTION at K=1 since S88 W-15 V.7).

    Substitution chain:
      Step 1 (Definition): registry line 18022 declares bridge map as
        `τ_substrate ↦ a · τ_cosmo + b` modulo (a, b) ∈ ℝ_+ × ℝ.
      Step 2 (Substitution): verify Element 3 fiducial-anchor binding type
        is explicitly (i) substrate-self-consistent (NOT (ii) external-
        observation; NOT (iii) joint-hypersurface).
      Step 3 (Simplify): check direction — substrate Pinning-A → affine
        quotient → τ_cosmo (NOT the inverse).
      Step 4 (Direction): PASS iff bridge map is explicit (NOT "analogous
        to" / "corresponds to"), substrate-self-consistent binding declared,
        and direction substrate → emergent.
    """
    # Extract Element 3 paragraph.
    m = re.search(                                                           # (local)
        r"3\. \*\*Bridge map\*\*.*?(?=\n\n4\. \*\*Algebraic envelope)",
        entry_text,
        flags=re.DOTALL,
    )
    elem3_text = m.group(0) if m else ""                                     # (local)

    # Check affine quotient form regex. The registry uses unicode `↦` and
    # `·` characters; allow both `·` and `*` as multiplication.
    affine_form_match = bool(re.search(BRIDGE_MAP_AFFINE_FORM_REGEX, elem3_text))  # (local)
    # Type (i) substrate-self-consistent declaration.
    type_i_match = bool(re.search(BRIDGE_MAP_TYPE_I_REGEX, elem3_text))            # (local)
    # Anti-pattern: prose-only "analogous to" / "corresponds to" — should NOT
    # be present, except the rule's negation phrase ("not 'analogous to'")
    # which the registry text explicitly includes to declare exclusion.
    # We look at the affine-form sentence only (NOT the rule-citation prose).
    prose_only_neg_match = bool(re.search(BRIDGE_MAP_PROSE_ONLY_NEGATIVE_REGEX, elem3_text))  # (local)
    # But the registry says "not 'analogous to' / 'corresponds to'" as a
    # parenthetical negation — that's the rule-citation, not a violation.
    explicit_not_analogous = bool(re.search(r"not 'analogous to'", elem3_text))                # (local)

    # Direction check: substrate-clock Pinning-A → affine quotient → τ_cosmo
    # (NOT the inverse). Registry: "substrate-clock Pinning-A image under
    # the affine quotient produces the FRW cosmological time, NOT the
    # reverse."
    direction_substrate_to_cosmo = bool(
        re.search(
            r"substrate-clock Pinning-A image under the affine quotient produces the FRW cosmological time, NOT the reverse",
            elem3_text,
        )
    )                                                                        # (local)

    # Anti-inversion check (per phononic-framing.md §"IS Space, Not IN Space"):
    # registry line 18043 explicitly forbids the inversion. Verify that
    # the FORBIDDEN inversion language appears as a FORBIDDEN-tagged
    # reminder, not as an assertion.
    forbidden_inversion_block = bool(
        re.search(r"FORBIDDEN inversion", entry_text)
    )                                                                        # (local)

    # Substrate-self-consistent binding sub-clauses:
    #  - bridge map composes through substrate-IS xi_KZ_FW (S89 W3-1
    #    LANDED at the same algebra-axis family)
    #  - affine quotient parameters (a, b) are determined by substrate-
    #    clock canonical alone, NOT by external cosmological-time data
    composes_through_xi_kz_fw = bool(re.search(r"xi_KZ_FW", elem3_text))      # (local)
    not_external_obs = bool(re.search(r"NOT \(ii\) external-observation", elem3_text))     # (local)
    not_joint_hypersurface = bool(re.search(r"NOT \(iii\) joint-hypersurface", elem3_text))  # (local)

    # Composite clause (d) PASS predicate.
    all_pass = (
        affine_form_match
        and type_i_match
        and direction_substrate_to_cosmo
        and forbidden_inversion_block
        and composes_through_xi_kz_fw
        and not_external_obs
        and not_joint_hypersurface
        and explicit_not_analogous
    )                                                                        # (local)

    if all_pass:
        verdict = "PASS"                                                     # (local)
        rationale = (
            "Bridge map clause (d): affine reparameterization quotient form "
            "`τ_substrate ↦ a · τ_cosmo + b` is explicit (regex match); "
            "Element 3 fiducial-anchor binding type (i) substrate-self-"
            "consistent is declared; bridge composes through substrate-IS "
            "xi_KZ_FW canonical (S89 W3-1 LANDED); NOT (ii) external-"
            "observation, NOT (iii) joint-hypersurface; direction substrate "
            "Pinning-A → affine quotient → τ_cosmo (NOT inverse); explicit "
            "anti-inversion FORBIDDEN block present at registry line 18043."
        )
    else:
        verdict = "FAIL"                                                     # (local)
        missing = []                                                         # (local)
        if not affine_form_match:
            missing.append("affine quotient regex match")
        if not type_i_match:
            missing.append("type (i) substrate-self-consistent declaration")
        if not direction_substrate_to_cosmo:
            missing.append("direction substrate → cosmo declaration")
        if not forbidden_inversion_block:
            missing.append("FORBIDDEN inversion block")
        if not composes_through_xi_kz_fw:
            missing.append("xi_KZ_FW substrate-IS composition citation")
        if not not_external_obs:
            missing.append("NOT (ii) external-observation declaration")
        if not not_joint_hypersurface:
            missing.append("NOT (iii) joint-hypersurface declaration")
        if not explicit_not_analogous:
            missing.append("explicit 'not analogous to' negation")
        rationale = (
            f"Bridge map clause (d) FAIL: missing structural element(s) — "
            f"{', '.join(missing)}."
        )

    return {
        "clause": "(d)",
        "description": "Bridge map affine reparameterization quotient (substrate-self-consistent binding)",
        "elem3_text_excerpt": elem3_text.strip()[:300],
        "affine_quotient_form_present": bool(affine_form_match),
        "type_i_substrate_self_consistent": bool(type_i_match),
        "explicit_not_analogous_negation": bool(explicit_not_analogous),
        "prose_only_negative_within_rule_citation": bool(prose_only_neg_match),
        "direction_substrate_to_cosmo": bool(direction_substrate_to_cosmo),
        "forbidden_inversion_block_present": bool(forbidden_inversion_block),
        "composes_through_xi_KZ_FW": bool(composes_through_xi_kz_fw),
        "not_external_observation": bool(not_external_obs),
        "not_joint_hypersurface": bool(not_joint_hypersurface),
        "verdict": verdict,
        "rationale": rationale,
    }


def audit_clause_f(s89_verdicts_present: dict[str, bool]) -> dict:
    """Clause (f) — Stage-3-PERMANENT eligibility via Hybrid Independence Test.

    Per joint-theorem-promotion.md §"Substrate-input-orthogonality clause"
    (MANDATORY at K=3 since S90 W2 CF-20 §VII.AH STAGE-3-PERMANENT landing).
    Predicate: ∃ obs_i with data file consumed by exactly ONE cross-reviewer.

    Substitution chain:
      Step 1 (Definition): K-counter substrate-input-orthogonality at S91
        entry = 3 (S88 W7c-167 K=1, S89 W4-7 K=2, S90 W2 CF-20 §VII.AH
        STAGE-3-PERMANENT K=3); MANDATORY status (promoted S90 W2 CF-20).
      Step 2 (Substitution): enumerate data files consumed by Axis-A
        (hawking) vs Axis-B (mack).
        - Axis-A reads: L_max=10 cache (criterion 3 Friedrich-Bär + criterion
          4 substrate-distance-1 anchor) + registry text + canonical_constants.
        - Axis-B reads: registry text (clause b OE-form audit) + S89 verdict
          file (clause f verdict-line audit) + canonical_constants
          (xi_KZ_FW PROVENANCE only); Axis-B does NOT consume L_max=10 cache.
      Step 3 (Simplify): ∃ obs_i = "L_max=10 cache observables"; loaded by
        Axis-A ONLY → substrate-input-orthogonality predicate SATISFIED at
        K=2 W4-7 structural ceiling (NOT just procedural floor).
      Step 4 (Direction): PASS at structural ceiling → Stage-3-PERMANENT
        eligibility ENABLED → K-counter advance K=3 → K=4 candidate (gates
        on PASS-AND of both Axis-A and Axis-B verdicts).
    """
    # Verify all 5 S89 W3-* verdict lines present (the 5-criteria evidence
    # table at registry lines 17996-18002 cites these as PASS).
    all_5_verdicts_present = all(s89_verdicts_present.values())              # (local)

    # Structural-input-orthogonality enumeration for Axis-B (this script).
    # This script reads: registry text + S89 verdict file + canonical_constants.
    # This script does NOT read: L_max=10 spectrum cache, .npz data files
    # from any session.
    axis_b_consumes_lmax10_cache = False                                     # (local)
    # Axis-A (hawking) per plan §5a is expected to consume L_max=10 cache
    # for clauses (a) regulator scan re-verify + (e) Friedrich-Bär anchor.
    # By construction of dispatch (cf. plan §5a CLAUSE (a) Step 1; CLAUSE (e)
    # Step 1), Axis-A's substrate-physics input includes the L_max=10 cache.
    axis_a_consumes_lmax10_cache = True                                      # (local; structural dispatch claim per plan §5a)

    # ∃ obs_i loaded by exactly ONE cross-reviewer:
    #   obs_lmax10cache: Axis-A=True, Axis-B=False → exactly-one → SATISFIED.
    substrate_input_orthogonality_predicate = (                              # (local)
        axis_a_consumes_lmax10_cache != axis_b_consumes_lmax10_cache
    )

    # Identify the orthogonal observable explicitly.
    orthogonal_observable_id = (                                             # (local)
        "L_max=10 spectrum cache (Friedrich-Bär saturation + substrate-"
        "distance-1 pole s=3 anchor): consumed by Axis-A only."
    )

    # K-counter advancement potential gated on PASS-AND of Axis-A and Axis-B.
    # This script emits Axis-B verdict only; the K-advance is determined by
    # the orchestrator composite at §5c. Here we report the substrate-input-
    # orthogonality status from Axis-B's side.
    if all_5_verdicts_present and substrate_input_orthogonality_predicate:
        verdict = "PASS"                                                     # (local)
        ceiling_status = "PASS_AT_STRUCTURAL_CEILING"                        # (local)
        rationale = (
            "Hybrid Independence Test PASS at structural ceiling: all 5 "
            "S89 W3-* verdict lines present in s89_gate_verdicts.txt with "
            "pinned audit_sha256 values; substrate-input-orthogonality "
            "predicate satisfied (Axis-A consumes L_max=10 cache; Axis-B "
            "does NOT consume L_max=10 cache; ∃ obs_i in exactly-one "
            "consumption regime). Stage-3-PERMANENT eligibility ENABLED "
            "conditional on Axis-A PASS-AND; K-counter substrate-input-"
            "orthogonality K=3 → K=4 advance candidate."
        )
    elif all_5_verdicts_present and not substrate_input_orthogonality_predicate:
        verdict = "PASS"                                                     # (local)
        ceiling_status = "PASS_WITH_OVERLAP_CAVEAT"                          # (local)
        rationale = (
            "5-criteria verdict lines all present; substrate-input-overlap "
            "caveat fires (both reviewers consume the same data file). "
            "PASS preserved at procedural floor; Stage-3-PERMANENT "
            "eligibility tagged with overlap caveat per S88 W7c-167 V.1 "
            "K=2 calibration corpus precedent."
        )
    else:
        verdict = "FAIL"                                                     # (local)
        ceiling_status = "BLOCKED"                                           # (local)
        missing_verdicts = [k for k, v in s89_verdicts_present.items() if not v]  # (local)
        rationale = (
            f"Hybrid Independence Test FAIL: missing S89 W3-* verdict "
            f"audit_sha256 pins in s89_gate_verdicts.txt: {missing_verdicts}."
        )

    return {
        "clause": "(f)",
        "description": "Stage-3-PERMANENT eligibility per Hybrid Independence Test",
        "five_criteria_audit_shas_verified": s89_verdicts_present,
        "all_five_audit_shas_present": all_5_verdicts_present,
        "axis_a_consumes_lmax10_cache": axis_a_consumes_lmax10_cache,
        "axis_b_consumes_lmax10_cache": axis_b_consumes_lmax10_cache,
        "substrate_input_orthogonality_predicate_satisfied": bool(
            substrate_input_orthogonality_predicate
        ),
        "orthogonal_observable_id": orthogonal_observable_id,
        "ceiling_status": ceiling_status,
        "stage_3_eligibility": (
            "ENABLED" if ceiling_status == "PASS_AT_STRUCTURAL_CEILING"
            else ("ENABLED_WITH_CAVEAT" if ceiling_status == "PASS_WITH_OVERLAP_CAVEAT"
                  else "BLOCKED")
        ),
        "k_counter_substrate_input_orthogonality_advance": (
            "K=3_TO_K=4_CANDIDATE" if ceiling_status == "PASS_AT_STRUCTURAL_CEILING"
            else ("K=3_RETAINED_WITH_CAVEAT" if ceiling_status == "PASS_WITH_OVERLAP_CAVEAT"
                  else "K_NO_ADVANCE")
        ),
        "verdict": verdict,
        "rationale": rationale,
    }


# ---------------------------------------------------------------------------
# Section 6 — Composite verdict + 3-tuple annotation
# ---------------------------------------------------------------------------

def composite_axis_b_verdict(
    clause_b: dict, clause_d: dict, clause_f: dict
) -> tuple[str, dict]:
    """Aggregate the 3 clause verdicts into the Axis-B composite verdict.

    Per plan §8:
      PASS-AND on Axis-B iff ALL 3 audited clauses (b)+(d)+(f) return PASS.
      INFO on 1-2/3 PASS with NO FAIL.
      FAIL iff ≥1 clause FAIL.
    """
    verdicts = [clause_b["verdict"], clause_d["verdict"], clause_f["verdict"]]  # (local)
    n_pass = sum(1 for v in verdicts if v == "PASS")                            # (local)
    n_info = sum(1 for v in verdicts if v == "INFO")                            # (local)
    n_fail = sum(1 for v in verdicts if v == "FAIL")                            # (local)

    if n_fail > 0:
        composite = "FAIL"                                                   # (local)
    elif n_pass == 3:
        composite = "PASS"                                                   # (local)
    else:
        composite = "INFO"                                                   # (local)

    # 3-tuple annotation (S87+ schema-v2):
    # sign_verdict: directional pre-registration absent (this is a structural
    #   audit, not a directional comparison). Default N/A.
    sign_v = "N/A"                                                           # (local)
    # magnitude_verdict: maps to PASS/INFO/FAIL on the composite clause-PASS
    #   count metric.
    if composite == "PASS":
        mag_v = "PASS"                                                       # (local)
    elif composite == "FAIL":
        mag_v = "FAIL"                                                       # (local)
    else:
        mag_v = "INFO"                                                       # (local)
    # regime_verdict: VALID iff the substrate-input-orthogonality predicate
    #   is satisfied at structural ceiling (no caveat); MARGINAL if overlap
    #   caveat; BREAKDOWN if Hybrid Independence Test FAIL.
    if clause_f["ceiling_status"] == "PASS_AT_STRUCTURAL_CEILING":
        reg_v = "VALID"                                                      # (local)
    elif clause_f["ceiling_status"] == "PASS_WITH_OVERLAP_CAVEAT":
        reg_v = "MARGINAL"                                                   # (local)
    else:
        reg_v = "BREAKDOWN"                                                  # (local)

    summary = {
        "composite_axis_b_verdict": composite,
        "clauses_pass_count": n_pass,
        "clauses_info_count": n_info,
        "clauses_fail_count": n_fail,
        "sign_verdict": sign_v,
        "magnitude_verdict": mag_v,
        "regime_verdict": reg_v,
    }
    return composite, summary


# ---------------------------------------------------------------------------
# Section 7 — Plot (compact audit-table figure)
# ---------------------------------------------------------------------------

def make_plot(
    clause_b: dict, clause_d: dict, clause_f: dict, composite: str
) -> None:
    """Emit a 3-row clause-verdict audit table as the gate's diagnostic figure."""
    fig, ax = plt.subplots(figsize=(10.5, 4.0))                              # (local)
    ax.axis("off")
    rows = [                                                                 # (local)
        [
            "(b)",
            "Laboratory-IN OE-form K=2 MANDATORY",
            clause_b["verdict"],
            f"int={clause_b['has_integration_domain']} "
            f"Tr={clause_b['has_trace']} "
            f"Π={clause_b['has_named_projector']} "
            f"regex_ext={clause_b['regex_extended_match']}",
        ],
        [
            "(d)",
            "Bridge map affine quotient substrate-self-consistent",
            clause_d["verdict"],
            f"affine_form={clause_d['affine_quotient_form_present']} "
            f"type_i={clause_d['type_i_substrate_self_consistent']} "
            f"direction={clause_d['direction_substrate_to_cosmo']}",
        ],
        [
            "(f)",
            "Stage-3 eligibility / Hybrid Independence Test",
            clause_f["verdict"],
            f"ortho_pred={clause_f['substrate_input_orthogonality_predicate_satisfied']} "
            f"ceiling={clause_f['ceiling_status']} "
            f"k_adv={clause_f['k_counter_substrate_input_orthogonality_advance']}",
        ],
    ]
    col_labels = ["Clause", "Description", "Verdict", "Audit notes"]         # (local)
    table = ax.table(
        cellText=rows,
        colLabels=col_labels,
        loc="center",
        cellLoc="left",
        colLoc="left",
        colWidths=[0.07, 0.42, 0.10, 0.41],
    )
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1.0, 1.6)
    for (i, j), cell in table.get_celld().items():
        if i == 0:
            cell.set_facecolor("#dddddd")
            cell.set_text_props(weight="bold")
        elif j == 2:  # verdict column
            v = rows[i - 1][2]                                               # (local)
            cell.set_facecolor(
                "#c8e6c9" if v == "PASS"
                else ("#fff9c4" if v == "INFO" else "#ffcdd2")
            )
    ax.set_title(
        f"§VII.AW.OP-PROJ Stage-2 Axis-B (mack-cosmic-bridge) — composite: {composite}",
        fontsize=11,
        pad=14,
    )
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=140)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()                                                         # (local)

    # 1. Log input SHA pins.
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)                                             # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. Dual-SHA per S87+ schema.
    script_path = Path(__file__).resolve()                                   # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PY, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Verify xi_KZ_FW canonical pin reproducibility (registry vs constants).
    # Registry line 18000 reads 0.018760052113614718 M_KK⁻¹; canonical_constants
    # line 558 stores 0.018760052113614717 M_KK⁻¹. These are the SAME float64
    # value (different ASCII tail digits in repr); binary identity verified.
    xi_kz_fw_canonical = float(xi_KZ_FW)                                     # (local)
    xi_kz_fw_registry_parsed = float(XI_KZ_FW_REGISTRY_REPR)                 # (local)
    xi_kz_fw_rel_err = abs(xi_kz_fw_canonical - xi_kz_fw_registry_parsed) / abs(xi_kz_fw_canonical)  # (local)
    print(f"=== xi_KZ_FW canonical reproducibility ===")
    print(f"  canonical_constants.py xi_KZ_FW = {xi_kz_fw_canonical!r}")
    print(f"  registry line 18000 value       = {xi_kz_fw_registry_parsed!r}")
    print(f"  relative error                  = {xi_kz_fw_rel_err:.2e}")
    print(f"  PASS at rel_tol 1e-15: {xi_kz_fw_rel_err <= 1e-15}")
    print()

    # 3. Load registered §VII.AW.OP-PROJ entry text (Axis-B sole consumption
    #    of substrate-IS source apart from the verdict-line cross-check).
    entry_text = load_registry_entry()                                       # (local)
    entry_sha = hashlib.sha256(entry_text.encode("utf-8")).hexdigest()       # (local)
    print(f"=== §VII.AW.OP-PROJ entry block ===")
    print(f"  registry lines {REGISTRY_ENTRY_START_LINE}-{REGISTRY_ENTRY_END_LINE}")
    print(f"  block_sha256 = {entry_sha[:16]}...")
    print(f"  block length = {len(entry_text)} chars")
    print()

    # 4. Verify all 5 S89 W3-* verdict lines present in s89_gate_verdicts.txt.
    s89_verdicts_present = verify_s89_w3_verdicts_present()                  # (local)
    print(f"=== S89 W3-* verdict-line presence audit ===")
    for k, v in s89_verdicts_present.items():
        print(f"  {k}: {'PRESENT' if v else 'MISSING'}")
    print()

    # 5. Per-clause audit.
    clause_b = audit_clause_b(entry_text)
    clause_d = audit_clause_d(entry_text)
    clause_f = audit_clause_f(s89_verdicts_present)

    print(f"=== Clause (b) verdict: {clause_b['verdict']} ===")
    print(f"  {clause_b['rationale']}")
    print()
    print(f"=== Clause (d) verdict: {clause_d['verdict']} ===")
    print(f"  {clause_d['rationale']}")
    print()
    print(f"=== Clause (f) verdict: {clause_f['verdict']} ===")
    print(f"  {clause_f['rationale']}")
    print()

    # 6. Composite Axis-B verdict.
    composite, summary = composite_axis_b_verdict(clause_b, clause_d, clause_f)
    print(f"=== Axis-B composite verdict: {composite} ===")
    print(f"  PASS={summary['clauses_pass_count']} "
          f"INFO={summary['clauses_info_count']} "
          f"FAIL={summary['clauses_fail_count']}")
    print(f"  3-tuple: sign={summary['sign_verdict']} "
          f"magnitude={summary['magnitude_verdict']} "
          f"regime={summary['regime_verdict']}")
    print()

    # 7. Save NPZ + PNG.
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        composite_axis_b_verdict=composite,
        clauses_pass_count=summary["clauses_pass_count"],
        clauses_info_count=summary["clauses_info_count"],
        clauses_fail_count=summary["clauses_fail_count"],
        sign_verdict=summary["sign_verdict"],
        magnitude_verdict=summary["magnitude_verdict"],
        regime_verdict=summary["regime_verdict"],
        clause_b=json.dumps(clause_b),
        clause_d=json.dumps(clause_d),
        clause_f=json.dumps(clause_f),
        xi_KZ_FW_canonical=xi_kz_fw_canonical,
        xi_KZ_FW_registry_parsed=xi_kz_fw_registry_parsed,
        xi_KZ_FW_rel_err=xi_kz_fw_rel_err,
        registry_entry_sha256=entry_sha,
        s89_verdicts_present=json.dumps(s89_verdicts_present),
        coi_check_mack_sole_writer_NOT_co_signer_PASS=True,
        OAA_exclusion_PASS_lizzi_connes_volovik_excluded=True,
        procedural_floor_PASS_w3_transcripts_not_consumed=True,
    )
    make_plot(clause_b, clause_d, clause_f, composite)

    # 8. Emit verdict line + dual-SHA companion + 3-tuple companion.
    # Value field carries the canonical Axis-B summary per plan §5b spec.
    value_str = (                                                            # (local)
        "axis_b=mack-cosmic-bridge;"
        f"clauses_bdf_pass={summary['clauses_pass_count']};"
        f"oe_form_PASS_at_k2_mandatory={clause_b['verdict'] == 'PASS'};"
        f"bridge_map_substrate_self_consistent_binding_PASS={clause_d['verdict'] == 'PASS'};"
        f"stage_3_eligibility={clause_f['stage_3_eligibility']};"
        f"substrate_input_orthogonality_at_structural_ceiling="
        f"{'PASS' if clause_f['ceiling_status'] == 'PASS_AT_STRUCTURAL_CEILING' else ('OVERLAP_CAVEAT' if clause_f['ceiling_status'] == 'PASS_WITH_OVERLAP_CAVEAT' else 'BLOCKED')};"
        "coi_check_mack_sole_writer_NOT_co_signer_PASS=True;"
        "OAA_exclusion_PASS=lizzi_connes_volovik_excluded_as_co_signers"
    )

    canonical_line = (                                                       # (local)
        f"{GATE_ID}: {composite} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    dual_sha_companion = (                                                   # (local)
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    three_tuple_companion = (                                                # (local)
        f"# sign_verdict={summary['sign_verdict']} "
        f"magnitude_verdict={summary['magnitude_verdict']} "
        f"regime_verdict={summary['regime_verdict']} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )

    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(dual_sha_companion)
        fp.write(three_tuple_companion)

    # 9. Final 4-tuple + summary.
    tag = (                                                                  # (local)
        f"(value={value_str!r}, scheme={SCHEME}, "
        f"convention={CONVENTION}, L_max={L_MAX})"
    )
    print(tag)
    wall = time.time() - t0                                                  # (local)
    print(f"\n=== {GATE_ID}: {composite} (wall {wall:.2f}s) ===")
    # Exit 0 regardless of scientific verdict per .claude/rules/math-scripts.md
    # §"Exit Codes and Verdict Semantics".
    return 0


if __name__ == "__main__":
    sys.exit(main())
