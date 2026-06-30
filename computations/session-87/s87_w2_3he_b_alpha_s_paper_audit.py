#!/usr/bin/env python3
"""
S87 W2-1 — paper-mode artifact-existence audit for the
3He-B inheritance image of the framework's substrate-IS alpha_s prediction.

Gate: S87-LAB-3HE-B-ALPHA-S-EQUIVALENT  ([VERIFY], paper-mode)

Pre-registered threshold (per session-87-plan-w2.md §W2-1.5):
  PASS  iff  papers/s87-3he-b-alpha-s-equivalent.md exists AND
             contains the five required sub-sections, each with at
             least N_LINES_PASS = 15 substantive lines:
              (i)   "Framework substrate-IS prediction"
              (ii)  "Inheritance morphism to 3He-B BdG"
              (iii) "Class A + Class B falsifier protocol"
              (iv)  "Predicted Aalto LTL spin-tilt running magnitude"
              (v)   "Falsifier-master-inventory landing rows"
  INFO  iff  paper exists with all five sub-sections present, but at
             least one is below the 15-line substantive-content threshold
             (stub-form). INFO carries a next-session paper-finish carry-forward.
  FAIL  iff  paper missing OR one of the five required sub-sections is absent.

  Tolerance rule: ARTIFACT-EXISTENCE-WITH-SUBSTANTIVE-CONTENT (per
                  .claude/rules/agent-standards.md §"Completion Verification"
                  + .claude/rules/wave-classification.md §M1).

Inputs (SHA-256 dual-pinned at runtime):
  - papers/s87-3he-b-alpha-s-equivalent.md   (paper artifact under audit)
  - computations/_shared/canonical_constants.py
  - sessions/session-plan/session-87-plan-w2.md  (plan source)
  - .claude/rules/inheritance-falsifier-protocol.md
  - .claude/rules/cross-pillar-bridge-anatomy.md
  - sessions/framework/registry/falsifier-master-inventory.md
  - script bytes (this file)

Output 4-tuple:
  (value='paper_artifact_present_with_substrate_IS_prediction',
   scheme=single-pole-Mellin-substrate-distance-1,
   convention=inheritance-morphism-3He-B-BdG-canonical,
   L_max=10)

Classification: PHONONIC (per W2-1 §3 plan classification — 3He-B
                          dipolar excitation spectrum is the laboratory
                          analog of the substrate's GGE-relic running)

DISCIPLINE
----------
- `from canonical_constants import *`  (mandatory MGM CLAUDE.md)
- All intermediates tagged `# (local)`
- Pure I/O + grep; no GPU, no eigenvalue compute
- SHA-256 dual-pinned per S84+ schema; verdict appended atomically.
- 3-tuple companion row per S87+ schema-v2 (sign_verdict=N/A for
  artifact-existence gate; no directional pre-reg).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import os
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===

os.environ.setdefault("OMP_NUM_THREADS", "8")  # (local) CPU thread cap
import hashlib
import json
import sys
import time
from pathlib import Path

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
PAPERS_DIR = PROJECT_ROOT / "papers"
RULES_DIR = PROJECT_ROOT / ".claude" / "rules"
REGISTRY_DIR = PROJECT_ROOT / "sessions" / "framework" / "registry"
PLAN_DIR = PROJECT_ROOT / "sessions" / "session-plan"

SESSION = "S87"                                                   # (local)
GATE_ID = "S87-LAB-3HE-B-ALPHA-S-EQUIVALENT"                      # (local)
SCHEME = "single-pole-Mellin-substrate-distance-1"                # (local)
CONVENTION = "inheritance-morphism-3He-B-BdG-canonical"           # (local)
L_MAX = 10                                                        # (local)

# Pre-registered threshold values
N_LINES_PASS = 15                # (local) min substantive lines per required sub-section
MIN_LINE_LEN = 30                # (local) chars to count a line as "substantive"

PAPER_PATH = PAPERS_DIR / "s87-3he-b-alpha-s-equivalent.md"
CANONICAL_PY = resolve_script(None, 'canonical_constants.py')
PLAN_PATH = PLAN_DIR / "session-87-plan-w2.md"
INHERITANCE_RULE = RULES_DIR / "inheritance-falsifier-protocol.md"
CROSS_PILLAR_RULE = RULES_DIR / "cross-pillar-bridge-anatomy.md"
FALSIFIER_INVENTORY = REGISTRY_DIR / "falsifier-master-inventory.md"

VERDICT_TXT = resolve_output(87, 's87_gate_verdicts.txt')

INPUT_FILES = [
    PAPER_PATH,
    CANONICAL_PY,
    PLAN_PATH,
    INHERITANCE_RULE,
    CROSS_PILLAR_RULE,
    FALSIFIER_INVENTORY,
]

# Five required paper sub-sections — heading-substring patterns
# (matched case-sensitive against any line containing the substring).
REQUIRED_SECTIONS = [
    ("Framework substrate-IS prediction",
     "Substrate-IS observable + alpha_s = n_s^2 - 1 substitution chain"),
    ("Inheritance morphism to 3He-B BdG",
     "iota : C+H+M_3(C) -> M_2(C); rank-2 ker(iota_*) generators phi_67, phi_88"),
    ("Class A + Class B falsifier protocol",
     "Gates 1+2+3+4 inheritance-falsifier template (W-5 W11-C5/C6)"),
    ("Predicted Aalto LTL spin-tilt running magnitude",
     "alpha_s^lab inherits magnitude of alpha_s_FW under (Delta_B/Delta_A)^p"),
    ("Falsifier-master-inventory landing rows",
     "Row #45 (Class A NULL) + Row #46 (Class B ratio 7.3250)"),
]

# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} - input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        except ValueError:
            rel = str(p)
        marker = "" if sha else " (MISSING)"  # (local)
        print(f"  {rel}: {sha[:16]}...{marker}")
        pins[rel] = sha
    return pins


def closure_hash(pins):
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path, canonical_path, pins):
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        pass
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        pass
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
# Section 5 — Section-extraction + substantive-line counter
# ---------------------------------------------------------------------------

def extract_section_content(paper_text, heading_substring):
    """Find lines beginning a section that contains heading_substring; return
    the body text from immediately after that heading line to either the next
    top-level/equally-leveled markdown header or end-of-file.

    Markdown heading detection: any line starting with '#' or '##' or '###' or '####'
    that contains the substring is treated as the section opener. The section ends
    at the next line beginning with '#' at the SAME depth or LESS (i.e., '#'-count
    less-than-or-equal-to the opener's), or end-of-file.
    """
    lines = paper_text.splitlines()  # (local)
    opener_idx = -1                   # (local)
    opener_depth = -1                 # (local)
    for idx, ln in enumerate(lines):
        stripped = ln.lstrip()        # (local)
        if not stripped.startswith("#"):
            continue
        if heading_substring not in ln:
            continue
        depth = 0  # (local)
        for ch in stripped:
            if ch == "#":
                depth += 1
            else:
                break
        opener_idx = idx
        opener_depth = depth
        break
    if opener_idx < 0:
        return None  # heading not found
    # Walk forward until next heading at same or shallower depth
    end_idx = len(lines)  # (local)
    for j in range(opener_idx + 1, len(lines)):
        s = lines[j].lstrip()
        if not s.startswith("#"):
            continue
        d = 0  # (local)
        for ch in s:
            if ch == "#":
                d += 1
            else:
                break
        if d <= opener_depth:
            end_idx = j
            break
    body = "\n".join(lines[opener_idx + 1:end_idx])  # (local)
    return body


def count_substantive_lines(body_text):
    """Count lines with at least MIN_LINE_LEN non-whitespace chars and that
    are not pure code-fence delimiters / horizontal rules / list-bullet-only."""
    if body_text is None:
        return 0
    n = 0  # (local)
    for ln in body_text.splitlines():
        stripped = ln.strip()
        if not stripped:
            continue
        # Skip pure code-fence delimiters and horizontal rules
        if stripped.startswith("```") and len(stripped.replace("`", "").strip()) <= 20:
            # Permit fenced code blocks themselves contribute via their inner lines
            continue
        if stripped in {"---", "***", "___"}:
            continue
        # Substantive = at least MIN_LINE_LEN non-whitespace chars after
        # stripping markdown decoration prefixes.
        cleaned = stripped.lstrip("#-*>` ").rstrip()  # (local)
        if len(cleaned) >= MIN_LINE_LEN:
            n += 1
    return n


# ---------------------------------------------------------------------------
# Section 6 — Verdict logic
# ---------------------------------------------------------------------------

def classify_verdict(section_results):
    """Apply pre-registered verdict rule to per-section line counts.

    PASS: all 5 required sections found AND each has >= N_LINES_PASS substantive lines
    INFO: all 5 found but >= 1 below threshold
    FAIL: paper missing OR >= 1 section absent
    """
    n_present = sum(1 for r in section_results if r["present"])  # (local)
    if n_present < len(REQUIRED_SECTIONS):
        composite = "FAIL"
        verdict_label = (
            f"FAIL_section_missing_{len(REQUIRED_SECTIONS) - n_present}_of_{len(REQUIRED_SECTIONS)}"
        )
    else:
        below_thresh = sum(
            1 for r in section_results if r["substantive_lines"] < N_LINES_PASS
        )  # (local)
        if below_thresh > 0:
            composite = "INFO"
            verdict_label = (
                f"INFO_stub_form_{below_thresh}_of_{len(REQUIRED_SECTIONS)}_below_{N_LINES_PASS}_lines"
            )
        else:
            composite = "PASS"
            verdict_label = "paper_artifact_present_with_substrate_IS_prediction"
    return {
        "composite": composite,
        "verdict_label": verdict_label,
        "n_present": n_present,
        "section_results": section_results,
    }


# ---------------------------------------------------------------------------
# Section 7 — Verdict-line emission (atomic append)
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme, convention, L_max):
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict, value, audit_sha, content_sha,
                   sign_v, mag_v, regime_v):
    """Atomic append: canonical line + dual-SHA companion + 3-tuple companion."""
    canonical = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    dual_sha_companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    triple_companion = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical)
        fp.write(dual_sha_companion)
        fp.write(triple_companion)


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------

def main():
    t0 = time.time()  # (local)

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure(legacy): {closure[:16]}...")

    # 1b. Dual SHAs
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PY, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    # 2. Verify paper exists
    if not PAPER_PATH.exists():
        print(f"  PAPER MISSING: {PAPER_PATH.relative_to(PROJECT_ROOT)}")
        section_results = [{"name": s[0], "present": False, "substantive_lines": 0,
                            "expectation": s[1]} for s in REQUIRED_SECTIONS]
    else:
        paper_text = PAPER_PATH.read_text(encoding="utf-8", errors="replace")
        print(f"  Paper found: {PAPER_PATH.relative_to(PROJECT_ROOT)} "
              f"({len(paper_text):,} bytes)")

        # 3. Extract + count each required section
        section_results = []  # (local)
        for heading_sub, expectation in REQUIRED_SECTIONS:
            body = extract_section_content(paper_text, heading_sub)
            n_lines = count_substantive_lines(body) if body is not None else 0  # (local)
            section_results.append({
                "name": heading_sub,
                "present": body is not None,
                "substantive_lines": n_lines,
                "expectation": expectation,
            })

    # 4. Print per-section table
    print()
    print("=== Per-section substantive-line audit ===")
    print(f"  threshold N_LINES_PASS = {N_LINES_PASS}; MIN_LINE_LEN = {MIN_LINE_LEN}")
    for r in section_results:
        flag = "PASS" if (r["present"] and r["substantive_lines"] >= N_LINES_PASS) else \
               ("INFO_stub" if r["present"] else "FAIL_missing")
        print(f"  [{flag:13s}] {r['name']:50s}  lines={r['substantive_lines']:3d}")
    print()

    # 5. Classify verdict
    verdict_dict = classify_verdict(section_results)
    print("=== Verdict logic ===")
    print(f"  Sections present: {verdict_dict['n_present']}/{len(REQUIRED_SECTIONS)}")
    print(f"  Composite: {verdict_dict['composite']}")
    print(f"  Verdict label: {verdict_dict['verdict_label']}")
    print()

    composite = verdict_dict["composite"]            # (local)
    value = verdict_dict["verdict_label"]            # (local)

    # 6. 3-tuple annotation (artifact-existence gate)
    sign_v = "N/A"                                    # (local) no directional pre-reg
    mag_v = "PASS" if composite == "PASS" else (
        "INFO" if composite == "INFO" else "FAIL")    # (local)
    regime_v = "VALID"                                # (local) deterministic file I/O

    # 7. 4-tuple emission + verdict line
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)
    append_verdict(composite, value, audit_sha, content_sha,
                   sign_v, mag_v, regime_v)
    print(f"  Verdict appended to {VERDICT_TXT.relative_to(PROJECT_ROOT)}")

    # 8. Final summary
    wall = time.time() - t0  # (local)
    print()
    print(f"=== {GATE_ID}: {composite} ({value}) wall={wall:.2f}s ===")
    print(f"=== audit_sha256 = {audit_sha} ===")
    print(f"=== content_sha256 = {content_sha} ===")

    return 0


if __name__ == "__main__":
    sys.exit(main())
