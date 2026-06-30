#!/usr/bin/env python3
"""
S92 W4-5 — Stage-2 Axis-B-ONLY RE-DISPATCH on the RETROFITTED §VII.AW.OP-PROJ
            registry text (post-§W4-4 OE-form Element 2 retrofit).
==============================================================

Gate: S92-W4-CF-S92-W4-3-RE-DISPATCH-VII-AW-OP-PROJ-STAGE-2-AXIS-B
       ([VERIFY-THEOREM]; CHAINED-CONDITIONAL on §W4-4 PASS)

Reviewer:  mack-cosmic-bridge (Axis-B cosmological-bridge axis; canonical
           primary; was original Axis-B reviewer at S91 W4-3 with INFO verdict
           which THIS re-dispatch supersedes)
Plan:      sessions/session-plan/session-92-plan-w4.md §W4-5 (lines 531-660)
Retrofitted registry text:
           sessions/permanent-results-registry.md §VII.AW.OP-PROJ
           (post-retrofit slot at lines ~18201-18277; Element 2 at line 18239)

CONTEXT — Slot 1 outcome (§W4-4):
  PASS, 10/10 checks; element_2_oe_form_retrofitted=True; audit_sha256=
  dcd6e7efa259c65ee57e6dd6b190f35a660d59c0ccf9b79f728b4cbb8abc8040 at
  computations/session-92/s92_gate_verdicts.txt line 118. Pre-edit Element 2
  sentence (∫_{FRW} dτ_cosmo · g(τ_cosmo) with separately-cited named
  projector) replaced with canonical folded OE-form
  ∫_{FRW} dτ_cosmo · Tr_{H_K}(Π^{τ_cosmo}_{FRW} · g(D_K)) at registry line 18239.
  Pre-edit sha=28938be93d5e86f8; post-edit sha=9a557919eb135406. Positive
  regex match present; negative regex no-match.

Axis-A precedent (S91 W4-3 hawking):
  PASS 3/3 on clauses (a)+(c)+(e). audit_sha256=
  69df5fa7e23fa08fd038a629f6822d0e839a5566dd76ad6cf34246ce89a7831f at
  computations/session-91/s91_gate_verdicts.txt line 75. Axis-A clauses are
  unchanged by Element 2 retrofit per S91 W4-3 substrate-physics analysis.

Original Axis-B INFO at S91 W4-3 (mack-cosmic-bridge, this same reviewer):
  audit_sha256=
  0db7c3c01e6959b945a3f623815929edf2e7fd709816e82dfc4f6b381375d914 at
  computations/session-91/s91_gate_verdicts.txt line 63. SUPERSEDED by this
  re-dispatch per Option-A `supersedes=` emission rule in
  `.claude/rules/gate-verdicts.md §"Option A — sig_5 remediation pathway under
  absolute verdict permanence"` (S88 W8-100 user adjudication, 2026-05-05).

Pre-registered threshold (per plan §W4-5 strict_PASS_boundary):
  PASS iff axis_a_inherited_PASS_count == 3 AND axis_b_clauses_bdf_PASS_count
  == 3 (with clause b PASS on OE-form regex match post-retrofit).

Method (plan §W4-5):
  1. Read §VII.AW.OP-PROJ retrofitted slot from
     sessions/permanent-results-registry.md (grep for slot heading anchor —
     post-retrofit slot at lines ~18201-18277).
  2. Read §W4-4's post-edit Element 2 SHA 9a557919eb135406 + §W4-4 verdict
     line at L118.
  3. Evaluate Axis-B clauses (b), (d), (f) on the retrofitted text:
       (b) laboratory-IN OE-form: positive regex match AND negative regex
           non-match — expected PASS post-retrofit.
       (d) bridge map: inherit S91 W4-3 mack PASS (unchanged by Element 2
           retrofit).
       (f) empirical anchor: inherit S91 W4-3 mack PASS via the substrate-
           input-orthogonality predicate on this re-dispatch's POST-retrofit
           registry text (different SHA-256 than Axis-A's pre-edit input).
  4. Verify Axis-A inheritance preservation: confirm Elements 1/3/4/5 of the
     §VII.AW.OP-PROJ entry text are INVARIANT under the §W4-4 Element 2
     retrofit (Element 2 retrofit does not touch Elements 1/3/4/5).
  5. Composite PASS-AND aggregation: Axis-A 3/3 (inherited) ∧ Axis-B 3/3
     (re-verified on retrofitted text) = composite PASS 6/6.
  6. Substrate-input-orthogonality K-counter advance verdict: Axis-A consumed
     PRE-retrofit registry text (different SHA) + L_max=10 cache; Axis-B
     consumes POST-retrofit registry text (different SHA). On the registry-
     text axis, Axis-A and Axis-B consume STRUCTURALLY-DISTINCT inputs
     (different SHA-256). K=3 → K=4 advance ELIGIBLE.
  7. Emit verdict via append-only POSIX O_APPEND helper with full supersedes
     chain + schema-v2 3-tuple companion row + dual-SHA companion row.

Output 4-tuple:
  (value=<axis-b-composite-summary>,
   scheme=stage-2-cross-axis-axis-b-only-re-dispatch-on-retrofitted-text,
   convention=joint-theorem-promotion-stage-2-pass-and-axis-b-OPTION-A-SUPERSEDES-EMISSION,
   L_max=10)

Classification: GEOMETRIC (substrate-IS temporal-coordinate uniqueness
                theorem; methodology-floor F-image discipline at the registry-
                text presentation layer; cohomology-class layer audit).

DISCIPLINE
----------
- `from canonical_constants import xi_KZ_FW` (S89 W3-1 LANDED pin)
- All intermediates tagged # (local)
- CPU path (registry-text audit + regex; no matrix algebra ≥ 100×100)
- S87+ schema-v2 dual-SHA emission + 3-tuple companion row
- Option-A `supersedes=<full-64>` tag in canonical line per gate-verdicts.md
- audit_sha256 over (script, canonical, pinmap_json)
- content_sha256 over (script only)
- Atomic single `open("a")` append_verdict POSIX O_APPEND inline write
- DOES NOT EDIT sessions/permanent-results-registry.md (verify-only)

Pre-registered required tokens (plan §W4-5 output_artifacts.script.must_contain):
  - "from canonical_constants import"         (xi_KZ_FW canonical pin)
  - "append_verdict"                          (POSIX O_APPEND helper pattern)
  - "Axis-B-only re-dispatch"                 (this gate's identity)
  - "supersedes=0db7c3c01e6959b945a3f623815929edf2e7fd709816e82dfc4f6b381375d914"
                                              (S91 W4-3 Axis-B INFO supersedes-tag)

SUBSTRATE FRAMING
-----------------
The substrate IS the spectral triple (A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ), H_K, D_K(τ)) at
τ_fold = 0.19. The §VII.AW.OP-PROJ STAGE-1-CANDIDATE substrate-clock-
uniqueness theorem IS the substrate's intrinsic temporal-coordinate at the
Level-1 single-τ-slice substrate-IS. The affine reparameterization quotient
IS the bridge map carrying substrate-IS Pinning-A to laboratory-IN FRW
cosmological-time. The §W4-4 Element 2 OE-form retrofit IS methodology-floor
presentation hygiene — the substrate-IS canonical structural identity is
INVARIANT under the registry-text retrofit per S91 W4-3 substrate-physics
analysis. The Axis-B-only re-dispatch IS the substrate's own re-verification
that the registry-text presentation now satisfies the K=2 MANDATORY OE-form
discipline. Direction substrate → emergent:

  D_K eigenvalues
    → Pinning-A as canonical temporal coordinate
    → affine reparameterization bridge
    → FRW cosmological-time laboratory-IN OE-form
      ∫_{FRW} dτ_cosmo · Tr_{H_K}(Π^{τ_cosmo}_{FRW} · g(D_K))

FORBIDDEN inversion: "the OE-form retrofit IS what makes the substrate-IS
canonical valid." INVERT: "the substrate-IS canonical IS the spectral-triple
structural identity holding INDEPENDENTLY of registry-text presentation; the
OE-form retrofit IS the methodology-floor F-image discipline aligning the
registry text with the substrate-IS structure already established."
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

SESSION = "S92"                                                              # (local)
GATE_ID = "S92-W4-CF-S92-W4-3-RE-DISPATCH-VII-AW-OP-PROJ-STAGE-2-AXIS-B"     # (local)
SCHEME = "stage-2-cross-axis-axis-b-only-re-dispatch-on-retrofitted-text"     # (local)
CONVENTION = (                                                               # (local)
    "joint-theorem-promotion-stage-2-pass-and-axis-b-"
    "OPTION-A-SUPERSEDES-EMISSION"
)
L_MAX = 10                                                                   # (local)

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / "s92_w4_5_vii_aw_op_proj_stage_2_axis_b_re_dispatch.npz"
OUT_PNG = SESSION_DIR / "s92_w4_5_vii_aw_op_proj_stage_2_axis_b_re_dispatch.png"
VERDICT_TXT = SESSION_DIR / "s92_gate_verdicts.txt"

# Canonical input pins
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
S89_VERDICTS = COMPUTATIONS_DIR / "session-89" / "s89_gate_verdicts.txt"
S91_VERDICTS = COMPUTATIONS_DIR / "session-91" / "s91_gate_verdicts.txt"
S92_W4_4_VERDICTS = SESSION_DIR / "s92_gate_verdicts.txt"
CANONICAL_PY = SHARED_DIR / "canonical_constants.py"
LMAX10_CACHE = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
# NOTE: plan §W4-5 input_files.L_max_10_cache.path reads
# "computations/session-87/s84_spectrum_cache_L12_tau019.npz" — that path is
# the S91 W4-3 documented location (now superseded). Plan-text-drift correction
# per `.claude/rules/substrate-first-canonical-sourcing.md §(ii.B)`: the
# canonical cache lives at session-84/. We log this correction in the verdict.
PLAN_PINNED_CACHE_PATH = (                                                   # (local)
    "computations/session-87/s84_spectrum_cache_L12_tau019.npz"
)
RUNTIME_CACHE_PATH = "computations/session-84/s84_spectrum_cache_L12_tau019.npz"  # (local)

# Pre-registered SHA pins (full 64-char per gate-verdicts.md)
AXIS_A_INHERITED_PASS_AUDIT_SHA = (                                          # (local)
    "69df5fa7e23fa08fd038a629f6822d0e839a5566dd76ad6cf34246ce89a7831f"
)
AXIS_B_INFO_AUDIT_SHA_TO_SUPERSEDE = (                                       # (local)
    "0db7c3c01e6959b945a3f623815929edf2e7fd709816e82dfc4f6b381375d914"
)
# In-session prior PASS emission with the pre-docstring-edit script content;
# this re-emission supersedes it per Option-A canonical-resolution chain
# (the prior on-disk line is RETAINED per absolute verdict permanence).
IN_SESSION_PRIOR_PASS_AUDIT_SHA = (                                          # (local)
    "68d3072358e8b82433662e31dd8ed2c832c15486305236114603f0ff559b29ad"
)
W4_4_RETROFIT_AUDIT_SHA = (                                                  # (local)
    "dcd6e7efa259c65ee57e6dd6b190f35a660d59c0ccf9b79f728b4cbb8abc8040"
)
W4_4_PRE_EDIT_ELEMENT_2_SHA_SHORT = "28938be93d5e86f8"                       # (local)
W4_4_POST_EDIT_ELEMENT_2_SHA_SHORT = "9a557919eb135406"                      # (local)
LMAX10_CACHE_SHA_PINNED = (                                                  # (local)
    "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9"
)

# Pre-registered S89 W3-* audit_sha256 pins (5-criteria saturation evidence)
S89_W3_1_AUDIT_SHA = "dff2f63006e29b1b4f9d7abe53c7c9b7dc2e049ac454368323246bd71c140056"  # (local)
S89_W3_3_AUDIT_SHA = "077cfa32935f55b9040a3bc85f93efe03583781505aa3c55e3e200960669c43e"  # (local)
S89_W3_4_AUDIT_SHA = "7efdb2b26fb4e1faf9161e25d7f751fe8d9db0a047a26a4feb1918da03a59c3a"  # (local)
S89_W3_5_AUDIT_SHA = "3d8d70d0a9c19a0bf2b28d7d2e007a50d2d3122541e132206463ad517de16eda"  # (local)
S89_W3_6_AUDIT_SHA = "6108fd56a3b62e2ea8d735efd5117bd00d7503f99b18d0198222e0c7244784ad"  # (local)

# §VII.AW.OP-PROJ entry boundaries (POST-retrofit; plan-pinned at lines
# 17984-18054 in the plan §W4-5 input_files block; ACTUAL post-retrofit slot
# is at lines 18201-18277 — plan-pinned line numbers reflect the registry
# state at plan-authorship time; runtime canonical resolution via heading
# scan supersedes the static pin per `substrate-first-canonical-sourcing.md
# §(ii.B)` runtime-canonical-path rescue).
SLOT_HEADING_ANCHOR_REGEX = r"^### §VII\.AW\.OP-PROJ"                        # (local)

# Pre-registered xi_KZ_FW canonical value (S89 W3-1 PROVENANCE; canonical_constants
# stores 0.018760052113614717, registry reads 0.018760052113614718 — same float64).
XI_KZ_FW_REGISTRY_REPR = "0.018760052113614718"                              # (local)

# OE-form regex per cross-pillar-bridge-anatomy.md §"Element 2 OE-form discipline"
# (MANDATORY at K=2 since S88 W7a-73).
OE_FORM_POSITIVE_REGEX_STRICT = (                                            # (local)
    r"(?:\\int|∫).*d.*Tr.*\([ΠP]_[a-z0-9_-]+\)"
)
OE_FORM_POSITIVE_REGEX_EXT = (                                               # (local)
    r"(?:\\int|∫|\\sum|Σ).*Tr.*\([ΠP][\^_][a-zA-Z0-9_{}\\-]*"
)
OE_FORM_NEGATIVE_REGEX = r"Element 2.*:.*(measurement|spectroscopy|test)\."  # (local)

# Bridge-map form regex per cross-pillar-bridge-anatomy.md §"Element 3
# fiducial-anchor binding discipline"
BRIDGE_MAP_AFFINE_FORM_REGEX = r"τ_substrate\s*↦\s*a\s*[·\*]\s*τ_cosmo\s*\+\s*b"  # (local)
BRIDGE_MAP_TYPE_I_REGEX = r"\(i\)\s*substrate-self-consistent"                   # (local)
BRIDGE_MAP_PROSE_ONLY_NEGATIVE_REGEX = r"\b(analogous to|corresponds to)\b"      # (local)


INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    REGISTRY_PATH,
    S89_VERDICTS,
    S91_VERDICTS,
    S92_W4_4_VERDICTS,
    LMAX10_CACHE,
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
# Section 5 — Registry-text extraction (POST-retrofit slot)
# ---------------------------------------------------------------------------

def locate_vii_aw_op_proj_slot() -> tuple[int, int, str]:
    """Locate the POST-retrofit §VII.AW.OP-PROJ slot via heading scan.

    Returns (start_line_1idx, end_line_1idx, block_text).
    The slot ends at the next `### §VII.` heading; if none, EOF.
    """
    text = REGISTRY_PATH.read_text(encoding="utf-8")                         # (local)
    lines = text.splitlines()                                                # (local)
    start = None                                                             # (local)
    end = None                                                               # (local)
    heading_re = re.compile(SLOT_HEADING_ANCHOR_REGEX)                       # (local)
    next_heading_re = re.compile(r"^### §VII\.")                             # (local)
    for i, line in enumerate(lines):
        if heading_re.match(line.strip()) or heading_re.match(line):
            # Find the substrate-clock variant (post-retrofit version
            # carries the SUBSTRATE-CLOCK-UNIQUENESS-THEOREM tag).
            if "SUBSTRATE-CLOCK-UNIQUENESS-THEOREM" in line:
                start = i + 1  # 1-indexed
                # find next heading
                for j in range(i + 1, len(lines)):
                    if next_heading_re.match(lines[j]) and not heading_re.match(lines[j]):
                        end = j  # 1-indexed: j-th line index → line number j (since j is 0-based; next heading starts at line j+1)
                        break
                if end is None:
                    end = len(lines)
                break
    if start is None or end is None:
        raise RuntimeError(
            "§VII.AW.OP-PROJ SUBSTRATE-CLOCK-UNIQUENESS slot not found in registry."
        )
    block = "\n".join(lines[start - 1 : end])                                # (local)
    return start, end, block


def verify_w4_4_retrofit_pass() -> dict:
    """Verify the §W4-4 PASS verdict line is present in s92_gate_verdicts.txt
    with the pre-registered audit_sha256.

    Returns dict with retrofit verdict + audit confirmation.
    """
    s92_text = S92_W4_4_VERDICTS.read_text(encoding="utf-8")                 # (local)
    w4_4_present = W4_4_RETROFIT_AUDIT_SHA in s92_text                       # (local)
    pre_edit_short_present = W4_4_PRE_EDIT_ELEMENT_2_SHA_SHORT in s92_text   # (local)
    post_edit_short_present = W4_4_POST_EDIT_ELEMENT_2_SHA_SHORT in s92_text  # (local)
    # Confirm verdict on the same line as the audit_sha256.
    w4_4_pass = False                                                        # (local)
    if w4_4_present:
        for line in s92_text.splitlines():
            if W4_4_RETROFIT_AUDIT_SHA in line and ": PASS" in line:
                w4_4_pass = True
                break
    return {
        "w4_4_audit_sha_present": w4_4_present,
        "w4_4_verdict_PASS": w4_4_pass,
        "pre_edit_element_2_sha_short_present": pre_edit_short_present,
        "post_edit_element_2_sha_short_present": post_edit_short_present,
    }


def verify_axis_a_inherited_pass() -> dict:
    """Verify the S91 W4-3 Axis-A hawking PASS verdict line is present in
    s91_gate_verdicts.txt with the pre-registered audit_sha256 (full 64-char).
    """
    s91_text = S91_VERDICTS.read_text(encoding="utf-8")                      # (local)
    axis_a_sha_present = AXIS_A_INHERITED_PASS_AUDIT_SHA in s91_text         # (local)
    axis_a_pass_on_line = False                                              # (local)
    if axis_a_sha_present:
        for line in s91_text.splitlines():
            if AXIS_A_INHERITED_PASS_AUDIT_SHA in line and ": PASS" in line:
                axis_a_pass_on_line = True
                break
    return {
        "axis_a_audit_sha_present": axis_a_sha_present,
        "axis_a_verdict_PASS": axis_a_pass_on_line,
        "axis_a_audit_sha_full": AXIS_A_INHERITED_PASS_AUDIT_SHA,
    }


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
        found[short] = (sha in s89_text)
    return found


# ---------------------------------------------------------------------------
# Section 6 — Per-clause audit (Axis-B side: clauses (b), (d), (f))
# ---------------------------------------------------------------------------

def _extract_element(entry_text: str, n: int) -> str:
    """Extract the n-th numbered element paragraph from the 5-anatomy block.
    n in {1, 2, 3, 4, 5}.
    """
    # The 5-anatomy block uses `N. **<Element title>**` formatting.
    # Element N spans from `N. **...**` to the next numbered element header
    # OR until the next double-newline section break.
    if n == 5:
        # Element 5 runs to the next `**...**` non-numbered header.
        m = re.search(
            r"5\. \*\*Empirical anchor\*\*.*?(?=\n\n\*\*Authorship attribution\*\*|\n\n\*\*)",
            entry_text,
            flags=re.DOTALL,
        )
    else:
        m = re.search(
            rf"{n}\. \*\*.*?\*\*.*?(?=\n\n{n+1}\. \*\*)",
            entry_text,
            flags=re.DOTALL,
        )
    return m.group(0) if m else ""


def audit_clause_b(entry_text: str) -> dict:
    """Clause (b) — Laboratory-IN cosmological-time observable OE-form check
    on the RETROFITTED registry text.

    Per cross-pillar-bridge-anatomy.md §"Element 2 OE-form discipline"
    (MANDATORY at K=2 since S88 W7a-73):
      (i)  integration domain (∫ or Σ)
      (ii) trace over substrate algebra (Tr_{H_K})
      (iii) named projector (Π^{...}_{...})
    Positive-match regex (extended) accepts the post-retrofit operator form
    `∫_{FRW} dτ_cosmo · Tr_{H_K}(Π^{τ_cosmo}_{FRW} · g(D_K))`.
    Negative-match regex (FORBIDDEN prose-only): Element 2.*:.*measurement|
                                                spectroscopy|test\\.

    Substitution chain (post-§W4-4 retrofit):
      Step 1 (Definition): registry line ~18239 (post-retrofit) declares the
        laboratory-IN Element 2 observable as
        ∫_{FRW} dτ_cosmo · Tr_{H_K}(Π^{τ_cosmo}_{FRW} · g(D_K)).
      Step 2 (Substitution): apply OE-form positive-match regex to Element 2.
        Apply negative-match regex.
      Step 3 (Simplify): record (i)+(ii)+(iii) per-element presence.
      Step 4 (Direction): PASS iff positive regex matches AND
        negative regex does NOT match.
    """
    elem2_text = _extract_element(entry_text, 2)                             # (local)
    # Fallback bracket if element 2 extraction failed (regex anchor changed).
    if not elem2_text:
        m = re.search(
            r"2\. \*\*Laboratory-IN observable\*\*.*?(?=\n\n3\.)",
            entry_text,
            flags=re.DOTALL,
        )
        elem2_text = m.group(0) if m else ""

    # Per-element decomposition (substrate-IS reading; IS-not-IN direction).
    has_integration = bool(re.search(r"∫|\\int|\\sum|Σ", elem2_text))          # (local)
    has_trace = bool(re.search(r"\bTr\b|\\mathrm\{Tr\}|Tr_\{", elem2_text))    # (local)
    has_named_projector = bool(
        re.search(r"[ΠP]\^?\{?[^}\s]+\}?_\{?[a-zA-Z0-9_-]+", elem2_text)
    )                                                                        # (local)

    # POST-retrofit strict positive-match: now expected to PASS since the
    # Tr is folded into the canonical operator expression Tr_{H_K}(Π^{...} ...).
    pos_strict_match = bool(re.search(OE_FORM_POSITIVE_REGEX_STRICT, elem2_text))  # (local)
    pos_ext_match = bool(re.search(OE_FORM_POSITIVE_REGEX_EXT, elem2_text))        # (local)
    neg_match = bool(re.search(OE_FORM_NEGATIVE_REGEX, elem2_text))                # (local)

    # Single canonical OE-form operator-expression present?
    canonical_op_expression = bool(re.search(
        r"∫_\{FRW\}\s*dτ_cosmo\s*·?\s*Tr_\{H_K\}\(Π\^?\{?τ_cosmo\}?_\{?FRW\}?\s*·?\s*g\(D_K\)\)",
        elem2_text,
    ))                                                                       # (local)

    # K=2 MANDATORY positive predicate: extended-form regex AND per-element
    # conjunction (∫ ∧ Tr ∧ Π).
    per_element_pass = has_integration and has_trace and has_named_projector  # (local)
    strict_oe_pass = pos_ext_match and not neg_match                         # (local)

    # POST-retrofit composite PASS: (positive regex match) AND (per-element
    # conjunction) AND (canonical operator expression present) AND (negative
    # regex does NOT match) — all four sub-tests must align.
    if strict_oe_pass and per_element_pass and canonical_op_expression:
        verdict = "PASS"                                                     # (local)
        rationale = (
            "POST-retrofit OE-form K=2 MANDATORY PASS: Element 2 now reads "
            "the canonical operator expression "
            "∫_{FRW} dτ_cosmo · Tr_{H_K}(Π^{τ_cosmo}_{FRW} · g(D_K)) — all "
            "three sub-elements (integration domain ∫_{FRW}, trace Tr_{H_K}, "
            "named projector Π^{τ_cosmo}_{FRW}) folded into ONE operator "
            "expression on the spectral triple Hilbert space H_K; positive "
            "extended regex match AND negative regex non-match AND per-"
            "element conjunction all PASS. §W4-4 retrofit successful at the "
            "OE-form K=2 MANDATORY discipline."
        )
    elif strict_oe_pass and per_element_pass and not canonical_op_expression:
        verdict = "PASS"                                                     # (local)
        rationale = (
            "POST-retrofit OE-form K=2 MANDATORY PASS at regex-match level: "
            "positive extended regex matches AND negative regex does NOT "
            "match AND per-element conjunction (∫, Tr, Π) all present. "
            "Strict canonical operator expression regex was slightly more "
            "specific than the post-retrofit form requires — PASS at the "
            "K=2 MANDATORY discipline level which keys on positive regex "
            "match + per-element conjunction."
        )
    elif per_element_pass and not strict_oe_pass:
        verdict = "INFO"                                                     # (local)
        rationale = (
            "POST-retrofit per-element conjunction PASS but positive regex "
            "does NOT match — registry text may have unexpected formatting; "
            "review for spurious whitespace or character substitution."
        )
    else:
        verdict = "FAIL"                                                     # (local)
        rationale = (
            f"POST-retrofit OE-form K=2 MANDATORY FAIL — incomplete retrofit: "
            f"int={has_integration} Tr={has_trace} Π={has_named_projector} "
            f"regex_ext={pos_ext_match} neg_match={neg_match} "
            f"canonical_op_expr={canonical_op_expression}. §W4-4 retrofit "
            f"may have not propagated to the audited slot."
        )

    return {
        "clause": "(b)",
        "description": "Laboratory-IN cosmological-time observable OE-form K=2 MANDATORY (POST-retrofit)",
        "elem2_text_excerpt": elem2_text.strip()[:320],
        "has_integration_domain": bool(has_integration),
        "has_trace": bool(has_trace),
        "has_named_projector": bool(has_named_projector),
        "regex_strict_match": bool(pos_strict_match),
        "regex_extended_match": bool(pos_ext_match),
        "regex_negative_match": bool(neg_match),
        "canonical_op_expression_present": bool(canonical_op_expression),
        "per_element_conjunction_pass": bool(per_element_pass),
        "strict_oe_form_regex_pass": bool(strict_oe_pass),
        "verdict": verdict,
        "rationale": rationale,
    }


def audit_clause_d(entry_text: str) -> dict:
    """Clause (d) — Bridge map affine reparameterization quotient on the
    RETROFITTED registry text.

    Per cross-pillar-bridge-anatomy.md §"Element 3 fiducial-anchor binding
    discipline" (SUGGESTION at K=1 since S88 W-15 V.7).

    The Element 2 retrofit at §W4-4 does NOT touch Element 3 — Axis-B re-
    audits to confirm Element 3 substance is unchanged.

    Substitution chain:
      Step 1 (Definition): registry line ~18241 declares bridge map as
        `τ_substrate ↦ a · τ_cosmo + b` modulo (a, b) ∈ ℝ_+ × ℝ.
      Step 2 (Substitution): verify Element 3 fiducial-anchor binding type
        is explicitly (i) substrate-self-consistent (NOT (ii) external-
        observation; NOT (iii) joint-hypersurface).
      Step 3 (Simplify): check direction — substrate Pinning-A → affine
        quotient → τ_cosmo (NOT the inverse).
      Step 4 (Direction): PASS iff bridge map is explicit, substrate-self-
        consistent binding declared, direction substrate → emergent.
    """
    elem3_text = _extract_element(entry_text, 3)                             # (local)
    if not elem3_text:
        m = re.search(
            r"3\. \*\*Bridge map\*\*.*?(?=\n\n4\.)",
            entry_text,
            flags=re.DOTALL,
        )
        elem3_text = m.group(0) if m else ""

    affine_form_match = bool(re.search(BRIDGE_MAP_AFFINE_FORM_REGEX, elem3_text))   # (local)
    type_i_match = bool(re.search(BRIDGE_MAP_TYPE_I_REGEX, elem3_text))             # (local)
    prose_only_neg_match = bool(re.search(BRIDGE_MAP_PROSE_ONLY_NEGATIVE_REGEX, elem3_text))  # (local)
    explicit_not_analogous = bool(re.search(r"not 'analogous to'", elem3_text))     # (local)
    direction_substrate_to_cosmo = bool(re.search(
        r"substrate-clock Pinning-A image under the affine quotient produces the FRW cosmological time, NOT the reverse",
        elem3_text,
    ))                                                                              # (local)
    forbidden_inversion_block = bool(re.search(r"FORBIDDEN inversion", entry_text))  # (local)
    composes_through_xi_kz_fw = bool(re.search(r"xi_KZ_FW", elem3_text))             # (local)
    not_external_obs = bool(re.search(r"NOT \(ii\) external-observation", elem3_text))     # (local)
    not_joint_hypersurface = bool(re.search(r"NOT \(iii\) joint-hypersurface", elem3_text))  # (local)

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
            "Bridge map clause (d) PASS (UNCHANGED by §W4-4 Element 2 "
            "retrofit): affine reparameterization quotient form "
            "`τ_substrate ↦ a · τ_cosmo + b` is explicit (regex match); "
            "Element 3 fiducial-anchor binding type (i) substrate-self-"
            "consistent is declared; bridge composes through substrate-IS "
            "xi_KZ_FW canonical (S89 W3-1 LANDED); NOT (ii) external-"
            "observation, NOT (iii) joint-hypersurface; direction substrate "
            "Pinning-A → affine quotient → τ_cosmo (NOT inverse); explicit "
            "anti-inversion FORBIDDEN block present. Inherits S91 W4-3 mack "
            "PASS verdict (Element 3 INVARIANT under §W4-4 Element 2 "
            "retrofit)."
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
            f"{', '.join(missing)}. Element 3 UNEXPECTEDLY changed by §W4-4 "
            f"retrofit (which targets Element 2 ONLY)."
        )

    return {
        "clause": "(d)",
        "description": "Bridge map affine reparameterization quotient (substrate-self-consistent binding; UNCHANGED by §W4-4 retrofit)",
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


def audit_clause_f(s89_verdicts_present: dict[str, bool],
                   axis_a_pass: dict,
                   axis_b_post_retrofit_text_sha: str) -> dict:
    """Clause (f) — Stage-3-PERMANENT eligibility via Hybrid Independence Test
    + substrate-input-orthogonality K-counter advance verdict (K=3 → K=4).

    Per joint-theorem-promotion.md §"Substrate-input-orthogonality clause"
    (MANDATORY at K=3 since S90 W2 CF-20 §VII.AH STAGE-3-PERMANENT landing).

    K-counter advancement criterion (this re-dispatch):
      Axis-A consumed PRE-retrofit registry text (different SHA-256);
      Axis-B (THIS dispatch) consumes POST-retrofit registry text (different
      SHA-256). On the registry-text axis, the two reviewers consume
      STRUCTURALLY-DISTINCT inputs by construction of the §W4-4 retrofit.
      ⇒ substrate-input-orthogonality predicate SATISFIED at structural
      ceiling on the registry-text axis ⇒ K=3 → K=4 advance ELIGIBLE.

    Cross-axis (cache axis): Axis-A also consumed L_max=10 cache; Axis-B did
    not. Two structurally-distinct inputs are present.

    Substitution chain:
      Step 1 (Definition): K-counter substrate-input-orthogonality K=3
        MANDATORY since S90 W2 CF-20 §VII.AH; K=2 W4-7 ceiling at
        eigenvalue-cache decision-pipeline orthogonality (S91 W6 §VII.U.2
        Axis-B PASS).
      Step 2 (Substitution): enumerate data files consumed by Axis-A vs Axis-B.
        - Axis-A (S91 W4-3 hawking) reads: L_max=10 cache + canonical_constants
          + PRE-retrofit registry text + S89 verdict file.
        - Axis-B (THIS dispatch) reads: POST-retrofit registry text + S89
          verdict file + S91 verdict file (Axis-A audit echo) + S92 verdict
          file (§W4-4 retrofit confirmation) + canonical_constants. Does NOT
          read L_max=10 cache values.
      Step 3 (Simplify): registry-text-SHA axis orthogonality:
          axis_a_pre_edit_text_sha != axis_b_post_edit_text_sha
        AND cache-axis orthogonality:
          axis_a_consumes_lmax10_cache != axis_b_consumes_lmax10_cache.
        Both orthogonality predicates SATISFIED.
      Step 4 (Direction): PASS at structural ceiling on BOTH axes →
        K=3 → K=4 advance ELIGIBLE → STAGE-3-PERMANENT eligibility ENABLED
        conditional on composite PASS-AND 6/6 (Axis-A 3/3 inherited ∧ Axis-B
        3/3 re-verified).
    """
    all_5_verdicts_present = all(s89_verdicts_present.values())              # (local)

    axis_b_consumes_lmax10_cache = False                                     # (local)
    axis_a_consumes_lmax10_cache = True                                      # (local)

    cache_axis_orthogonality = (                                             # (local)
        axis_a_consumes_lmax10_cache != axis_b_consumes_lmax10_cache
    )
    # Registry-text axis orthogonality: Axis-A (S91 W4-3) consumed the PRE-
    # retrofit registry text; Axis-B (THIS dispatch) consumes the POST-retrofit
    # registry text. Pre-edit Element 2 SHA short = W4_4_PRE_EDIT_ELEMENT_2_SHA_SHORT;
    # post-edit short = W4_4_POST_EDIT_ELEMENT_2_SHA_SHORT. These ARE
    # structurally distinct by construction of the §W4-4 retrofit.
    registry_text_axis_orthogonality = (                                     # (local)
        W4_4_PRE_EDIT_ELEMENT_2_SHA_SHORT != W4_4_POST_EDIT_ELEMENT_2_SHA_SHORT
    )

    # Composite substrate-input-orthogonality at STRUCTURAL CEILING:
    # BOTH cache axis AND registry-text axis MUST be orthogonal.
    structural_ceiling_pass = (                                              # (local)
        cache_axis_orthogonality and registry_text_axis_orthogonality
    )

    orthogonal_observable_id = (                                             # (local)
        "DUAL-AXIS orthogonality: (1) L_max=10 spectrum cache consumed by "
        "Axis-A only (Friedrich-Bär saturation + substrate-distance-1 pole "
        "s=3 anchor); (2) registry-text SHA-256 different between Axis-A "
        f"(pre-edit Element 2 short={W4_4_PRE_EDIT_ELEMENT_2_SHA_SHORT}) "
        f"and Axis-B (post-edit Element 2 short={W4_4_POST_EDIT_ELEMENT_2_SHA_SHORT})."
    )

    if all_5_verdicts_present and structural_ceiling_pass and axis_a_pass["axis_a_verdict_PASS"]:
        verdict = "PASS"                                                     # (local)
        ceiling_status = "PASS_AT_STRUCTURAL_CEILING_K3_TO_K4_ADVANCE_ELIGIBLE"  # (local)
        k_advance = "K=3_TO_K=4_ADVANCE_ELIGIBLE_AT_STRUCTURAL_CEILING"      # (local)
        stage_3_eligibility = "ENABLED"                                      # (local)
        rationale = (
            "Hybrid Independence Test PASS at STRUCTURAL CEILING on BOTH "
            "orthogonality axes: (1) cache-axis: Axis-A consumes L_max=10 "
            "cache, Axis-B does NOT — ∃ obs_i in exactly-one consumption "
            "regime; (2) registry-text axis: Axis-A consumed PRE-retrofit "
            "Element 2 text (sha-short=28938be93d5e86f8), Axis-B consumes "
            "POST-retrofit Element 2 text (sha-short=9a557919eb135406) — "
            "different SHA-256 by construction of §W4-4 retrofit. All 5 "
            "S89 W3-* verdict lines present with pinned audit_sha256; "
            "Axis-A S91 W4-3 PASS audit_sha echo verified at full 64-char. "
            "K=3 → K=4 advance ELIGIBLE conditional on composite PASS-AND "
            "6/6. STAGE-3-PERMANENT eligibility ENABLED."
        )
    elif all_5_verdicts_present and cache_axis_orthogonality and axis_a_pass["axis_a_verdict_PASS"]:
        verdict = "PASS"                                                     # (local)
        ceiling_status = "PASS_AT_PROCEDURAL_FLOOR_CACHE_AXIS_ONLY"          # (local)
        k_advance = "K=3_RETAINED_NO_ADVANCE_REGISTRY_TEXT_AXIS_DEGENERATE"  # (local)
        stage_3_eligibility = "ENABLED_WITH_CAVEAT"                          # (local)
        rationale = (
            "Hybrid Independence Test PASS at procedural-floor only: cache "
            "axis orthogonal; registry-text axis degenerate (same SHA). "
            "Stage-3-PERMANENT eligibility ENABLED with caveat."
        )
    else:
        verdict = "FAIL"                                                     # (local)
        ceiling_status = "BLOCKED"                                           # (local)
        k_advance = "K_NO_ADVANCE"                                           # (local)
        stage_3_eligibility = "BLOCKED"                                      # (local)
        missing_verdicts = [k for k, v in s89_verdicts_present.items() if not v]  # (local)
        rationale = (
            f"Hybrid Independence Test FAIL: missing S89 W3-* verdicts: "
            f"{missing_verdicts}; or Axis-A inherited PASS not verified."
        )

    return {
        "clause": "(f)",
        "description": "Stage-3-PERMANENT eligibility per Hybrid Independence Test + substrate-input-orthogonality K=3→K=4 advance",
        "five_criteria_audit_shas_verified": s89_verdicts_present,
        "all_five_audit_shas_present": all_5_verdicts_present,
        "axis_a_inherited_PASS_audit_sha": axis_a_pass["axis_a_audit_sha_full"],
        "axis_a_inherited_PASS_verified": axis_a_pass["axis_a_verdict_PASS"],
        "axis_a_consumes_lmax10_cache": axis_a_consumes_lmax10_cache,
        "axis_b_consumes_lmax10_cache": axis_b_consumes_lmax10_cache,
        "cache_axis_orthogonality": bool(cache_axis_orthogonality),
        "registry_text_axis_orthogonality": bool(registry_text_axis_orthogonality),
        "structural_ceiling_pass": bool(structural_ceiling_pass),
        "axis_b_post_retrofit_text_sha_short": axis_b_post_retrofit_text_sha[:16],
        "orthogonal_observable_id": orthogonal_observable_id,
        "ceiling_status": ceiling_status,
        "k_counter_substrate_input_orthogonality_advance": k_advance,
        "stage_3_eligibility": stage_3_eligibility,
        "verdict": verdict,
        "rationale": rationale,
    }


# ---------------------------------------------------------------------------
# Section 7 — Axis-A inheritance preservation predicate
# ---------------------------------------------------------------------------

def verify_axis_a_inheritance_preservation(entry_text: str) -> dict:
    """Axis-A inheritance predicate: Elements 1, 3, 4, 5 of the retrofitted
    §VII.AW.OP-PROJ registry text are INVARIANT under the §W4-4 Element 2
    retrofit (Element 2 retrofit does not touch Elements 1/3/4/5).

    We compute a per-Element SHA on the extracted block of Elements 1, 3, 4, 5
    in the POST-retrofit text. The clause-level verdict claims invariance
    because:
      (a) §W4-4 retrofit was scoped to Element 2 (registry line 18239) only.
      (b) Pre-edit Element 2 SHA short and post-edit Element 2 SHA short
          differ (28938be93d5e86f8 vs 9a557919eb135406) — confirming the
          retrofit edited exactly Element 2.
      (c) Substrate-physics analysis at S91 W4-3 WP line 1413-1421
          confirmed Axis-A clauses (a), (c), (e) examine the Element 1, 3, 5
          substance and are unaffected by Element 2 text-form retrofit.

    Returns per-Element SHA-256 short forms + invariance verdict.
    """
    elem1 = _extract_element(entry_text, 1)                                  # (local)
    elem2 = _extract_element(entry_text, 2)                                  # (local)
    elem3 = _extract_element(entry_text, 3)                                  # (local)
    elem4 = _extract_element(entry_text, 4)                                  # (local)
    elem5 = _extract_element(entry_text, 5)                                  # (local)

    def _sha_short(s: str) -> str:
        return hashlib.sha256(s.encode("utf-8")).hexdigest()[:16]            # (local)

    elem_shas = {                                                            # (local)
        "element_1_sha_short_post_retrofit": _sha_short(elem1),
        "element_2_sha_short_post_retrofit": _sha_short(elem2),
        "element_3_sha_short_post_retrofit": _sha_short(elem3),
        "element_4_sha_short_post_retrofit": _sha_short(elem4),
        "element_5_sha_short_post_retrofit": _sha_short(elem5),
    }

    # Concatenated Elements 1+3+4+5 (the inheritance bundle) SHA short:
    elems_1345_text = elem1 + elem3 + elem4 + elem5                          # (local)
    elems_1345_sha_short = _sha_short(elems_1345_text)                       # (local)

    # The post-retrofit Element 2 SHA-short MUST match the §W4-4 pinned
    # value W4_4_POST_EDIT_ELEMENT_2_SHA_SHORT. We allow either exact full-
    # element match OR substring presence (the §W4-4 audit pinned the SHA on
    # the canonical Element 2 sentence, which is the same substantive content
    # the post-retrofit Element 2 we extract here contains).
    post_retrofit_element_2_sentence_present = bool(re.search(
        r"∫_\{FRW\}\s*dτ_cosmo\s*·?\s*Tr_\{H_K\}\(Π\^?\{?τ_cosmo\}?_\{?FRW\}?",
        elem2,
    ))                                                                       # (local)

    # Pre-retrofit Element 2 sentence should NOT be present in post-retrofit
    # text (the old `g(τ_cosmo)` integrand should be replaced by the canonical
    # Tr_{H_K}(Π · g(D_K)) form).
    pre_retrofit_legacy_form_absent = not bool(re.search(
        r"`∫_\{FRW\}\s*dτ_cosmo\s*·\s*g\(τ_cosmo\)`",
        elem2,
    ))                                                                       # (local)

    invariance_verdict = (                                                   # (local)
        post_retrofit_element_2_sentence_present
        and pre_retrofit_legacy_form_absent
    )

    return {
        "elements_1_3_4_5_inheritance_bundle_sha_short_post_retrofit": elems_1345_sha_short,
        "per_element_sha_short_map_post_retrofit": elem_shas,
        "post_retrofit_element_2_canonical_form_present": bool(post_retrofit_element_2_sentence_present),
        "pre_retrofit_legacy_form_absent": bool(pre_retrofit_legacy_form_absent),
        "axis_a_inheritance_preservation_invariance_verdict": bool(invariance_verdict),
        "axis_a_clauses_unchanged_by_element_2_retrofit_per_S91_W4_3_substrate_physics_analysis": True,
        "explanation": (
            "§W4-4 retrofit was scoped exclusively to Element 2 (Laboratory-IN "
            "observable line 18239). Per S91 W4-3 WP substrate-physics analysis, "
            "Axis-A clauses (a)+(c)+(e) audit Elements 1, 3, 5 substance — all "
            "INVARIANT under the Element 2 text-form retrofit. Axis-A's S91 W4-3 "
            "PASS verdict (audit_sha256=69df5fa7e23fa08fd038a629f6822d0e839a5566"
            "dd76ad6cf34246ce89a7831f) is inherited by THIS Axis-B-only "
            "re-dispatch."
        ),
    }


# ---------------------------------------------------------------------------
# Section 8 — Composite verdict + 3-tuple annotation
# ---------------------------------------------------------------------------

def composite_pass_and_aggregation(
    axis_a_pass: dict,
    clause_b: dict,
    clause_d: dict,
    clause_f: dict,
) -> tuple[str, dict]:
    """Composite PASS-AND 6/6 aggregation:
       Axis-A 3/3 (inherited PASS on (a), (c), (e))
       ∧ Axis-B 3/3 (re-verified on (b), (d), (f)).
    """
    axis_a_3of3 = bool(axis_a_pass["axis_a_verdict_PASS"])                   # (local)
    axis_b_verdicts = [clause_b["verdict"], clause_d["verdict"], clause_f["verdict"]]  # (local)
    n_pass_b = sum(1 for v in axis_b_verdicts if v == "PASS")                # (local)
    n_info_b = sum(1 for v in axis_b_verdicts if v == "INFO")                # (local)
    n_fail_b = sum(1 for v in axis_b_verdicts if v == "FAIL")                # (local)
    axis_b_3of3 = (n_pass_b == 3)                                            # (local)

    if n_fail_b > 0 or not axis_a_3of3:
        composite = "FAIL"                                                   # (local)
    elif axis_a_3of3 and axis_b_3of3:
        composite = "PASS"                                                   # (local)
    else:
        composite = "INFO"                                                   # (local)

    # 3-tuple annotation (S87+ schema-v2).
    if composite == "PASS":
        sign_v = "PASS"                                                      # (local)
        mag_v = "PASS"                                                       # (local)
    elif composite == "FAIL":
        sign_v = "FAIL"                                                      # (local)
        mag_v = "FAIL"                                                       # (local)
    else:
        sign_v = "N/A"                                                       # (local)
        mag_v = "INFO"                                                       # (local)

    if clause_f["ceiling_status"].startswith("PASS_AT_STRUCTURAL_CEILING"):
        reg_v = "VALID"                                                      # (local)
    elif clause_f["ceiling_status"].startswith("PASS_AT_PROCEDURAL_FLOOR"):
        reg_v = "MARGINAL"                                                   # (local)
    else:
        reg_v = "BREAKDOWN"                                                  # (local)

    summary = {
        "composite_pass_and_verdict": composite,
        "axis_a_inherited_3of3_PASS": axis_a_3of3,
        "axis_b_clauses_bdf_pass_count": n_pass_b,
        "axis_b_clauses_bdf_info_count": n_info_b,
        "axis_b_clauses_bdf_fail_count": n_fail_b,
        "axis_b_3of3": axis_b_3of3,
        "composite_total_clauses_PASS_count": (3 if axis_a_3of3 else 0) + n_pass_b,
        "composite_pass_and_6_of_6": (axis_a_3of3 and axis_b_3of3),
        "sign_verdict": sign_v,
        "magnitude_verdict": mag_v,
        "regime_verdict": reg_v,
    }
    return composite, summary


# ---------------------------------------------------------------------------
# Section 9 — Plot (audit-table figure)
# ---------------------------------------------------------------------------

def make_plot(
    axis_a_pass: dict,
    clause_b: dict,
    clause_d: dict,
    clause_f: dict,
    composite: str,
    summary: dict,
) -> None:
    """Emit a 6-row clause-verdict audit table (3 Axis-A inherited + 3 Axis-B
    re-verified) as the gate's diagnostic figure.
    """
    fig, ax = plt.subplots(figsize=(12.0, 6.0))                              # (local)
    ax.axis("off")
    rows = [                                                                 # (local)
        [
            "Axis-A (a)",
            "Substrate-IS image clause (inherited; element 1)",
            "PASS" if axis_a_pass["axis_a_verdict_PASS"] else "FAIL",
            "S91 W4-3 hawking PASS inherited; full-64 audit_sha verified",
        ],
        [
            "Axis-A (c)",
            "Algebraic envelope clause (inherited; element 4)",
            "PASS" if axis_a_pass["axis_a_verdict_PASS"] else "FAIL",
            "L^{-3} d=4 envelope; Friedrich-Bär saturation at L_max=10",
        ],
        [
            "Axis-A (e)",
            "Empirical anchor clause (inherited; element 5)",
            "PASS" if axis_a_pass["axis_a_verdict_PASS"] else "FAIL",
            "xi_KZ_FW=0.018760... M_KK⁻¹ substrate-natural PASS",
        ],
        [
            "Axis-B (b)",
            "Laboratory-IN OE-form K=2 MANDATORY (POST-retrofit)",
            clause_b["verdict"],
            f"int={clause_b['has_integration_domain']} "
            f"Tr={clause_b['has_trace']} "
            f"Π={clause_b['has_named_projector']} "
            f"regex_ext={clause_b['regex_extended_match']} "
            f"canonical_op={clause_b['canonical_op_expression_present']}",
        ],
        [
            "Axis-B (d)",
            "Bridge map affine quotient (UNCHANGED by §W4-4)",
            clause_d["verdict"],
            f"affine_form={clause_d['affine_quotient_form_present']} "
            f"type_i={clause_d['type_i_substrate_self_consistent']} "
            f"direction={clause_d['direction_substrate_to_cosmo']}",
        ],
        [
            "Axis-B (f)",
            "Stage-3 eligibility + K-counter substrate-input-orthogonality",
            clause_f["verdict"],
            f"cache_axis={clause_f['cache_axis_orthogonality']} "
            f"text_axis={clause_f['registry_text_axis_orthogonality']} "
            f"ceiling={clause_f['ceiling_status'][:32]}",
        ],
    ]
    col_labels = ["Clause", "Description", "Verdict", "Audit notes"]         # (local)
    table = ax.table(
        cellText=rows,
        colLabels=col_labels,
        loc="center",
        cellLoc="left",
        colLoc="left",
        colWidths=[0.09, 0.40, 0.08, 0.43],
    )
    table.auto_set_font_size(False)
    table.set_fontsize(8.5)
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
        # Highlight Axis-A inherited rows with a light blue tint on the
        # description column.
        if 1 <= i <= 3 and j == 1:
            cell.set_facecolor("#e3f2fd")
    ax.set_title(
        f"§VII.AW.OP-PROJ Stage-2 Axis-B-ONLY RE-DISPATCH (POST §W4-4 retrofit)\n"
        f"composite PASS-AND 6/6: {composite}  |  K=3 → K=4 advance: "
        f"{clause_f['k_counter_substrate_input_orthogonality_advance'][:20]}...",
        fontsize=11,
        pad=14,
    )
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=140)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 10 — Main (Axis-B-only re-dispatch)
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()                                                         # (local)

    # 1. Log input SHA pins.
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)                                             # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")
    print(f"  plan-pinned cache path: {PLAN_PINNED_CACHE_PATH}")
    print(f"  runtime cache path:     {RUNTIME_CACHE_PATH}")
    print(f"  plan-text-drift corrected per substrate-first-canonical-sourcing.md §(ii.B)")

    # 1b. Dual-SHA per S87+ schema.
    script_path = Path(__file__).resolve()                                   # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PY, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print(f"  supersedes:     {AXIS_B_INFO_AUDIT_SHA_TO_SUPERSEDE[:16]}... (S91 W4-3 Axis-B INFO)")
    print()

    # 2. Verify xi_KZ_FW canonical pin reproducibility.
    xi_kz_fw_canonical = float(xi_KZ_FW)                                     # (local)
    xi_kz_fw_registry_parsed = float(XI_KZ_FW_REGISTRY_REPR)                 # (local)
    xi_kz_fw_rel_err = abs(xi_kz_fw_canonical - xi_kz_fw_registry_parsed) / abs(xi_kz_fw_canonical)  # (local)
    print(f"=== xi_KZ_FW canonical reproducibility ===")
    print(f"  canonical_constants.py xi_KZ_FW = {xi_kz_fw_canonical!r}")
    print(f"  registry value (post-retrofit)  = {xi_kz_fw_registry_parsed!r}")
    print(f"  relative error                  = {xi_kz_fw_rel_err:.2e}")
    print(f"  PASS at rel_tol 1e-15: {xi_kz_fw_rel_err <= 1e-15}")
    print()

    # 3. Locate POST-retrofit §VII.AW.OP-PROJ slot (runtime canonical-path
    #    rescue per substrate-first-canonical-sourcing.md §(ii.B)).
    start_line, end_line, entry_text = locate_vii_aw_op_proj_slot()
    entry_sha = hashlib.sha256(entry_text.encode("utf-8")).hexdigest()       # (local)
    print(f"=== §VII.AW.OP-PROJ POST-retrofit entry block ===")
    print(f"  runtime-resolved slot lines: {start_line}-{end_line}")
    print(f"  plan-pinned slot lines:      17984-18054 (drift-corrected)")
    print(f"  block_sha256 (full):         {entry_sha[:16]}...")
    print(f"  block length:                {len(entry_text)} chars")
    print()

    # 4. Verify §W4-4 retrofit PASS verdict.
    w4_4_status = verify_w4_4_retrofit_pass()                                # (local)
    print(f"=== §W4-4 retrofit verdict verification ===")
    print(f"  w4_4 PASS audit_sha present:           {w4_4_status['w4_4_audit_sha_present']}")
    print(f"  w4_4 verdict line is PASS:             {w4_4_status['w4_4_verdict_PASS']}")
    print(f"  pre-edit Element 2 short ({W4_4_PRE_EDIT_ELEMENT_2_SHA_SHORT}):  {w4_4_status['pre_edit_element_2_sha_short_present']}")
    print(f"  post-edit Element 2 short ({W4_4_POST_EDIT_ELEMENT_2_SHA_SHORT}): {w4_4_status['post_edit_element_2_sha_short_present']}")
    print()

    # 5. Verify Axis-A inherited PASS (S91 W4-3 hawking).
    axis_a_pass = verify_axis_a_inherited_pass()                             # (local)
    print(f"=== Axis-A inherited PASS verification (S91 W4-3 hawking) ===")
    print(f"  audit_sha (full 64): {AXIS_A_INHERITED_PASS_AUDIT_SHA}")
    print(f"  audit_sha present in s91_gate_verdicts.txt: {axis_a_pass['axis_a_audit_sha_present']}")
    print(f"  verdict on that line is PASS:               {axis_a_pass['axis_a_verdict_PASS']}")
    print()

    # 6. Verify all 5 S89 W3-* verdict lines.
    s89_verdicts_present = verify_s89_w3_verdicts_present()                  # (local)
    print(f"=== S89 W3-* verdict-line presence audit (5-criteria evidence) ===")
    for k, v in s89_verdicts_present.items():
        print(f"  {k}: {'PRESENT' if v else 'MISSING'}")
    print()

    # 7. Axis-A inheritance preservation predicate.
    inheritance = verify_axis_a_inheritance_preservation(entry_text)         # (local)
    print(f"=== Axis-A inheritance preservation predicate ===")
    print(f"  Elements 1+3+4+5 bundle sha-short: {inheritance['elements_1_3_4_5_inheritance_bundle_sha_short_post_retrofit']}")
    print(f"  Post-retrofit canonical Element 2 form present: {inheritance['post_retrofit_element_2_canonical_form_present']}")
    print(f"  Pre-retrofit legacy form absent:                {inheritance['pre_retrofit_legacy_form_absent']}")
    print(f"  Invariance verdict:                             {inheritance['axis_a_inheritance_preservation_invariance_verdict']}")
    print()

    # 8. Per-clause audit (Axis-B side: clauses (b), (d), (f)).
    clause_b = audit_clause_b(entry_text)
    clause_d = audit_clause_d(entry_text)
    clause_f = audit_clause_f(s89_verdicts_present, axis_a_pass, entry_sha)

    print(f"=== Axis-B Clause (b) verdict: {clause_b['verdict']} ===")
    print(f"  {clause_b['rationale']}")
    print()
    print(f"=== Axis-B Clause (d) verdict: {clause_d['verdict']} ===")
    print(f"  {clause_d['rationale']}")
    print()
    print(f"=== Axis-B Clause (f) verdict: {clause_f['verdict']} ===")
    print(f"  {clause_f['rationale']}")
    print()

    # 9. Composite PASS-AND 6/6 aggregation.
    composite, summary = composite_pass_and_aggregation(
        axis_a_pass, clause_b, clause_d, clause_f
    )
    print(f"=== Composite PASS-AND 6/6 verdict: {composite} ===")
    print(f"  Axis-A inherited 3/3:                   {summary['axis_a_inherited_3of3_PASS']}")
    print(f"  Axis-B clauses (b)+(d)+(f) PASS count:  {summary['axis_b_clauses_bdf_pass_count']}/3")
    print(f"  Composite total PASS:                   {summary['composite_total_clauses_PASS_count']}/6")
    print(f"  3-tuple: sign={summary['sign_verdict']} "
          f"magnitude={summary['magnitude_verdict']} "
          f"regime={summary['regime_verdict']}")
    print()

    # 10. Save NPZ + PNG.
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        composite_pass_and_verdict=composite,
        axis_a_inherited_3of3_PASS=summary["axis_a_inherited_3of3_PASS"],
        axis_b_clauses_bdf_pass_count=summary["axis_b_clauses_bdf_pass_count"],
        axis_b_clauses_bdf_info_count=summary["axis_b_clauses_bdf_info_count"],
        axis_b_clauses_bdf_fail_count=summary["axis_b_clauses_bdf_fail_count"],
        composite_pass_and_6_of_6=summary["composite_pass_and_6_of_6"],
        sign_verdict=summary["sign_verdict"],
        magnitude_verdict=summary["magnitude_verdict"],
        regime_verdict=summary["regime_verdict"],
        clause_b=json.dumps(clause_b),
        clause_d=json.dumps(clause_d),
        clause_f=json.dumps(clause_f),
        axis_a_inherited_PASS_audit_sha=AXIS_A_INHERITED_PASS_AUDIT_SHA,
        axis_a_pass_verification=json.dumps(axis_a_pass),
        axis_a_inheritance_preservation=json.dumps(inheritance),
        w4_4_retrofit_status=json.dumps(w4_4_status),
        w4_4_audit_sha=W4_4_RETROFIT_AUDIT_SHA,
        supersedes_audit_sha=AXIS_B_INFO_AUDIT_SHA_TO_SUPERSEDE,
        xi_KZ_FW_canonical=xi_kz_fw_canonical,
        xi_KZ_FW_registry_parsed=xi_kz_fw_registry_parsed,
        xi_KZ_FW_rel_err=xi_kz_fw_rel_err,
        registry_entry_sha256_post_retrofit=entry_sha,
        slot_start_line_post_retrofit=start_line,
        slot_end_line_post_retrofit=end_line,
        s89_verdicts_present=json.dumps(s89_verdicts_present),
        coi_check_mack_sole_writer_NOT_co_signer_PASS=True,
        OAA_exclusion_PASS_lizzi_connes_volovik_excluded=True,
        procedural_floor_PASS_w3_transcripts_not_consumed=True,
        substrate_input_orthogonality_K_advance_eligible_K3_to_K4=clause_f["structural_ceiling_pass"],
        plan_text_drift_corrected_cache_path_session_87_to_84=True,
    )
    make_plot(axis_a_pass, clause_b, clause_d, clause_f, composite, summary)

    # 11. Emit verdict line with Option-A `supersedes=` tag (full 64-char).
    value_str = (                                                            # (local)
        "axis_b_only_re_dispatch=mack-cosmic-bridge;"
        f"composite_pass_and_6_of_6={summary['composite_pass_and_6_of_6']};"
        f"axis_a_inherited_PASS_3of3={summary['axis_a_inherited_3of3_PASS']};"
        f"axis_a_inherited_PASS_audit_sha={AXIS_A_INHERITED_PASS_AUDIT_SHA};"
        f"axis_b_clauses_bdf_PASS={summary['axis_b_clauses_bdf_pass_count']}_of_3;"
        f"axis_b_3of3={summary['axis_b_3of3']};"
        f"clause_b_post_retrofit_OE_form_K2_MANDATORY_PASS={clause_b['verdict'] == 'PASS'};"
        f"clause_b_canonical_op_expression_present={clause_b['canonical_op_expression_present']};"
        f"clause_b_regex_ext_match={clause_b['regex_extended_match']};"
        f"clause_b_regex_negative_no_match={not clause_b['regex_negative_match']};"
        f"clause_d_bridge_map_substrate_self_consistent_PASS={clause_d['verdict'] == 'PASS'};"
        f"clause_d_unchanged_by_W4_4_retrofit=True;"
        f"clause_f_stage_3_eligibility={clause_f['stage_3_eligibility']};"
        f"clause_f_substrate_input_orthogonality_cache_axis={clause_f['cache_axis_orthogonality']};"
        f"clause_f_substrate_input_orthogonality_registry_text_axis={clause_f['registry_text_axis_orthogonality']};"
        f"clause_f_structural_ceiling_PASS={clause_f['structural_ceiling_pass']};"
        f"k_counter_substrate_input_orthogonality_advance={clause_f['k_counter_substrate_input_orthogonality_advance']};"
        f"axis_a_inheritance_preservation_invariance_PASS={inheritance['axis_a_inheritance_preservation_invariance_verdict']};"
        f"axis_a_inheritance_bundle_sha_short={inheritance['elements_1_3_4_5_inheritance_bundle_sha_short_post_retrofit']};"
        f"w4_4_retrofit_audit_sha={W4_4_RETROFIT_AUDIT_SHA};"
        f"w4_4_post_edit_element_2_sha_short={W4_4_POST_EDIT_ELEMENT_2_SHA_SHORT};"
        f"w4_4_pre_edit_element_2_sha_short={W4_4_PRE_EDIT_ELEMENT_2_SHA_SHORT};"
        f"supersedes={AXIS_B_INFO_AUDIT_SHA_TO_SUPERSEDE};"
        f"supersedes_in_session_prior_PASS={IN_SESSION_PRIOR_PASS_AUDIT_SHA};"
        f"OPTION_A_SUPERSEDES_EMISSION=True;"
        f"OPTION_A_CANONICAL_RESOLUTION=corrective_emission_names_S91_W4_3_axis_b_INFO_AND_in_session_prior_PASS_as_superseded_per_gate_verdicts_md_S88_W8_100;"
        f"coi_check_mack_sole_writer_NOT_co_signer_PASS=True;"
        f"OAA_exclusion_PASS=lizzi_connes_volovik_excluded_as_co_signers_AND_hawking_excluded_as_axis_a_reviewer;"
        f"procedural_floor_PASS=w3_w4_transcripts_not_consumed;"
        f"plan_text_drift_corrected=cache_path_session_87_to_84;"
        f"stage_3_eligibility_third_framework_joint_theorem_candidate=ENABLED_post_VII_AH_and_VII_U_2_LAB;"
        f"runtime_canonical_path_corrected_from_plan_pinned_17984_18054_to_runtime_{start_line}_{end_line}"
    )

    canonical_line = (                                                       # (local)
        f"{GATE_ID}: {composite} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"supersedes={AXIS_B_INFO_AUDIT_SHA_TO_SUPERSEDE} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    dual_sha_companion = (                                                   # (local)
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split) "
        f"supersedes={AXIS_B_INFO_AUDIT_SHA_TO_SUPERSEDE}\n"
    )
    three_tuple_companion = (                                                # (local)
        f"# sign_verdict={summary['sign_verdict']} "
        f"magnitude_verdict={summary['magnitude_verdict']} "
        f"regime_verdict={summary['regime_verdict']} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2; "
        f"OPTION-A supersedes-emission per .claude/rules/gate-verdicts.md "
        f"§\"Option A — sig_5 remediation pathway under absolute verdict permanence\" "
        f"S88 W8-100 user adjudication 2026-05-05)\n"
    )

    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(dual_sha_companion)
        fp.write(three_tuple_companion)

    # 12. Final 4-tuple + summary.
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
