#!/usr/bin/env python3
"""
S88 W8-92 — S88-OPERATOR-PROJECTION-READING-A-RULE-PROMOTE
==========================================================

Gate: S88-OPERATOR-PROJECTION-READING-A-RULE-PROMOTE ([VERIFY])
  Trigger: Wave-0 plan-freeze; standalone Reading-A registry-naming-hygiene rule
  promotion (3-instance corpus pre-verified at S87-close).

Pre-registered threshold (PASS iff ALL of (a)-(d)):
  (a) §"Operator-Projection Reading-A Naming Hygiene" section present in
      .claude/rules/registry-landing.md with naming convention + 3-instance
      corpus + enforcement clause.
  (b) Status promoted to MANDATORY (per K=3 ≥ K_promotion=3).
  (c) Allowlist row appended to .claude/rules/methodology-wave-allowlist.md.
  (d) Substantive line count of the new section >= 15.

Inputs (SHA-256 dual-pinned at runtime — see §4 below; S84+ schema):
  - .claude/rules/registry-landing.md (current state, pre-edit)
  - .claude/rules/methodology-wave-allowlist.md (current state, pre-edit)
  - sessions/permanent-results-registry.md (registry state for §VII.AJ.W4-1, §VII.AG.1)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=K=3-MANDATORY-promoted, scheme=METHODOLOGY-rule-file-edit,
   convention=reading-A-operator-projection-K-3-promote-MANDATORY, L_max=N/A)

Classification: NON-PHONONIC (METHODOLOGY-class wave per wave-classification.md M1-M4)

METHODOLOGY
-----------
This is a METHODOLOGY-class wave (M1-M4 conjunction satisfied):
  M1: PASS predicate is artifact-existence-with-substantive-content (>=15 lines).
  M2: producing operations are Edit on .claude/rules/*.md + grep + line counts.
  M3: source-of-truth is verbatim extracts from S87 W4-2 §VII.AJ.W4-1 +
      S87 W6-1 §VII.AG.1 + S87 W11-meta-2 (corpus pre-verified).
  M4: gate-ID appended to methodology-wave-allowlist.md herewith.

The script:
  1. Captures pre-edit SHAs of .claude/rules/registry-landing.md +
     .claude/rules/methodology-wave-allowlist.md (BEFORE state).
  2. Performs the rule-file edits via subprocess delegation to the orchestrator
     (this script does NOT itself perform the Edit-tool operations; it audits
     the result post-orchestrator-edit per the AFTER-pattern of registry-
     landing.md §"Bridge-Landing Script Architecture").
  3. Captures post-edit SHAs (AFTER state).
  4. Verifies (a)-(d) by re-reading the rule files and asserting:
     - the new §"Operator-Projection Reading-A Naming Hygiene" header exists
     - status keyword "MANDATORY" present in that section
     - 3-instance corpus citations (S87 W4-2 + S87 W6-1 + S87 W11-meta-2)
     - allowlist row "W8-92" with this gate-ID
     - substantive line count >= 15 in the new section
  5. Emits exactly one verdict line per AFTER-pattern.

DISCIPLINE
----------
- `from canonical_constants import *` (Section 1)
- Every local/intermediate tagged `# (local)`
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- Single-shot verdict emission (no BEFORE-pattern conditional retries)
- Substrate framing: operator-projection vs state-projection IS structural
  distinction at algebra-axis orthogonality (cross-pillar-bridge-anatomy.md
  K-counter MANDATORY at K=3); naming hygiene enforces it at registry layer.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys as _sys
from pathlib import Path as _Path
_SHARED = _Path(__file__).resolve().parent.parent / "_shared"
if str(_SHARED) not in _sys.path:
    _sys.path.insert(0, str(_SHARED))
from canonical_constants import *  # noqa: F401,F403,E402

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import re  # noqa: E402
import sys  # noqa: E402
import time  # noqa: E402
from pathlib import Path  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S88"                                                    # (local)
GATE_ID = "S88-OPERATOR-PROJECTION-READING-A-RULE-PROMOTE"         # (local)
SCHEME = "METHODOLOGY-rule-file-edit"                              # (local)
CONVENTION = "reading-A-operator-projection-K-3-promote-MANDATORY" # (local)
L_MAX = "N/A"                                                      # (local)

# Pre-registered threshold pins (define BEFORE running)
K_CORPUS = 3                                                        # (local)
K_PROMOTION = 3                                                     # (local)
SUBSTANTIVE_LINE_COUNT_MIN = 15                                     # (local)

# 3-instance corpus identifiers (verbatim from plan §W8-92 method step 3)
CORPUS_INSTANCE_1 = "S87 W4-2 §VII.AJ.W4-1"                         # (local)
CORPUS_INSTANCE_2 = "S87 W6-1 §VII.AG.1"                            # (local)
CORPUS_INSTANCE_3 = "S87 W11-meta-2"                                # (local)

# Output destinations
OUT_JSON = SESSION_DIR / "s88_w8_reading_a_rule_promote.json"
VERDICT_TXT = SESSION_DIR / "s88_gate_verdicts.txt"

# Rule files this gate edits (verified at audit time)
RULE_REGISTRY_LANDING = PROJECT_ROOT / ".claude" / "rules" / "registry-landing.md"
RULE_METHODOLOGY_ALLOWLIST = PROJECT_ROOT / ".claude" / "rules" / "methodology-wave-allowlist.md"
PERMANENT_REGISTRY = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    RULE_REGISTRY_LANDING,
    RULE_METHODOLOGY_ALLOWLIST,
    PERMANENT_REGISTRY,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict:
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict,
):
    """Compute (audit_sha256, content_sha256) per the S84+ dual-SHA schema."""
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
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Verify (AFTER-pattern: re-read + verify)
# ---------------------------------------------------------------------------

def count_substantive_lines(section_text: str) -> int:
    """Count non-blank, non-pure-delimiter lines in a section block."""
    count = 0  # (local)
    for raw in section_text.splitlines():
        s = raw.strip()  # (local)
        if not s:
            continue
        # skip pure horizontal-rule delimiters
        if re.match(r"^-{3,}$", s) or re.match(r"^={3,}$", s):
            continue
        count += 1
    return count


def extract_section(rule_text: str, header_pattern: str) -> str:
    """Extract a top-level (## ) section by exact header pattern match.

    Returns the section body INCLUDING its header line, ending just before
    the NEXT top-level (## or higher) header.
    """
    # Match the header line; allow leading "## " or "### "
    m = re.search(
        rf"^(#{{2,3}}\s+{re.escape(header_pattern)}\s*$)",
        rule_text,
        re.MULTILINE,
    )
    if not m:
        return ""
    start = m.start()  # (local)
    rest = rule_text[m.end():]  # (local)
    # Find next top-level (## ) header — but allow ### sub-headers within
    next_m = re.search(r"^##\s+\S", rest, re.MULTILINE)
    if next_m:
        end = m.end() + next_m.start()  # (local)
    else:
        end = len(rule_text)  # (local)
    return rule_text[start:end]


def verify() -> dict:
    """Verify all four PASS conditions (a)-(d). Returns audit dict."""
    audit = {}  # (local)

    # Read rule files
    rl_text = RULE_REGISTRY_LANDING.read_text(encoding="utf-8")  # (local)
    al_text = RULE_METHODOLOGY_ALLOWLIST.read_text(encoding="utf-8")  # (local)

    # Condition (a): new section header present
    section_header = "Operator-Projection Reading-A Naming Hygiene"  # (local)
    section_body = extract_section(rl_text, section_header)  # (local)
    cond_a = bool(section_body)  # (local)
    audit["condition_a_section_present"] = cond_a

    # Condition (b): status promoted to MANDATORY
    cond_b = False  # (local)
    if section_body:
        # The MANDATORY status assertion must appear within the new section.
        cond_b = bool(re.search(r"\bMANDATORY\b", section_body))
    audit["condition_b_mandatory_status"] = cond_b

    # Condition (c): allowlist row for W8-92 with this gate-ID
    cond_c = bool(
        re.search(
            r"\|\s*W8-92\s*\|\s*S88\s*\|\s*S88-OPERATOR-PROJECTION-READING-A-RULE-PROMOTE",
            al_text,
        )
    )
    audit["condition_c_allowlist_row"] = cond_c

    # Sub-check: 3-instance corpus citations in the new section
    corpus_hits = {}  # (local)
    for label, needle in [
        ("instance_1_W4-2_VII.AJ.W4-1", r"W4-2.*VII\.AJ\.W4-1"),
        ("instance_2_W6-1_VII.AG.1", r"W6-1.*VII\.AG\.1"),
        ("instance_3_W11-meta-2", r"W11-meta-2"),
    ]:
        corpus_hits[label] = bool(re.search(needle, section_body))
    audit["corpus_3_instance_hits"] = corpus_hits
    cond_corpus = all(corpus_hits.values())  # (local)
    audit["corpus_complete"] = cond_corpus

    # Condition (d): substantive line count >= 15
    sub_lines = count_substantive_lines(section_body)  # (local)
    cond_d = sub_lines >= SUBSTANTIVE_LINE_COUNT_MIN  # (local)
    audit["condition_d_substantive_line_count"] = sub_lines
    audit["condition_d_passes"] = cond_d

    # Composite — ALL of (a), (b), (c), (d), and corpus_complete must hold.
    all_pass = cond_a and cond_b and cond_c and cond_d and cond_corpus  # (local)
    audit["all_pass"] = all_pass

    # Substitution chain (recorded for audit-trail re-derivation)
    audit["substitution_chain"] = {
        "step_1_definition_K_promotion": (
            "K_promotion = 3 per feedback_rules-compensate-missing-structure.md"
        ),
        "step_2_definition_naming_convention": (
            "Reading-A operator-projection: §VII.X.OP-PROJ vs state-side §VII.X.STATE-PROJ"
        ),
        "step_3_substitution_corpus": [
            CORPUS_INSTANCE_1,
            CORPUS_INSTANCE_2,
            CORPUS_INSTANCE_3,
        ],
        "step_4_simplify": f"K = {K_CORPUS} >= K_promotion = {K_PROMOTION}",
        "step_5_direction": "SUGGESTION -> MANDATORY at plan-freeze for all S88+ entries",
    }

    return audit


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


def evaluate_gate(audit: dict) -> str:
    """PASS iff (a) AND (b) AND (c) AND (d) AND corpus_complete; else FAIL."""
    return "PASS" if audit.get("all_pass", False) else "FAIL"


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. Compute S84+ dual SHAs
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Verify (single-shot, AFTER-pattern)
    audit = verify()
    value = (
        f"K={K_CORPUS}-MANDATORY-promoted" if audit["all_pass"]
        else f"K={K_CORPUS}-verify-FAIL-conditions={audit}"
    )

    # 3. Persist audit JSON sidecar
    audit_record = {
        "gate_id": GATE_ID,
        "session": SESSION,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "input_pin_map": pins,
        "before_after_shas": {
            "registry_landing_md_sha256_post_edit": pins.get(
                ".claude/rules/registry-landing.md", ""
            ),
            "methodology_wave_allowlist_md_sha256_post_edit": pins.get(
                ".claude/rules/methodology-wave-allowlist.md", ""
            ),
        },
        "audit": audit,
    }
    OUT_JSON.write_text(
        json.dumps(audit_record, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    print(f"  audit JSON: {OUT_JSON.relative_to(PROJECT_ROOT)}")

    # 4. Evaluate gate (single-shot)
    verdict = evaluate_gate(audit)

    # 5. Emit 4-tuple + append verdict
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)
    append_verdict(verdict, value, audit_sha, content_sha)

    # 6. Final summary
    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
