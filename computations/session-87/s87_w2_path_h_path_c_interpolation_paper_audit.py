"""S87 W2-6 — S87-PATH-H-PATH-C-INTERPOLATION paper-mode audit.

Paper-mode artifact-existence audit for the W2-6 mack-cosmic-bridge gate
`S87-PATH-H-PATH-C-INTERPOLATION` per plan
`sessions/session-plan/session-87-plan-w2.md` §W2-6.

This is METHODOLOGY-class artifact-existence; the audit:
  1. Verifies `papers/s87-path-h-path-c-interpolation.md` exists.
  2. Greps the paper for the four required sections.
  3. Counts substantive (non-blank, non-pure-heading) lines in the
     §"Framework substrate-IS interpolation construction" section.
  4. Verifies the section explicitly states (i)-(iv) per plan §5
     (interpolation route, substrate-IS observable, ε boundaries,
     falsifier-distinguishing prediction at intermediate ε).
  5. Verifies the cross-link to W9 CF-54 + the L1/L3 boundary
     identification + the intermediate-r falsifier section.
  6. Computes dual-SHA (audit_sha256 over script+canonical+pinmap;
     content_sha256 over script bytes alone) per W9a-99.
  7. Emits the canonical verdict line + dual-SHA companion + the
     S87 schema-v2 3-tuple companion to
     `computations/session-87/s87_gate_verdicts.txt`.

No numerical thresholds, no GPU work, no eigenvalues. The "value" emitted
in the verdict line is the artifact-existence-with-substantive-content
predicate string per plan §8 expected output 4-tuple.

Owner: mack-cosmic-bridge.
Run:  "phonon-exflation-sim/.venv312/Scripts/python.exe" \
      "computations/session-87/s87_w2_path_h_path_c_interpolation_paper_audit.py"
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
import time
from pathlib import Path
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


# Section 1 -- Project paths

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
sys.path.insert(0, str(SCRIPT_DIR))

# Per computations/_shared/CLAUDE.md: every computation script MUST
# `from canonical_constants import *`. This audit is paper-mode
# artifact-existence and does not consume any framework constants for
# numerical thresholds, but the import is mandatory by policy and the
# canonical_constants.py file IS pinned in the audit_sha256 input map
# for closure-hash provenance per `gate-verdicts.md` §"S87+ canonical form".
from canonical_constants import *  # noqa: F401,F403  -- policy import

# Section 2 -- Gate identity (frozen at plan-freeze; per §W2-6.13 YAML)

GATE_ID = "S87-PATH-H-PATH-C-INTERPOLATION"                              # (local)
SCHEME = "Path-H-Path-C-interpolation"                                   # (local)
CONVENTION = "L1-L3-boundary-identification-canonical"                   # (local)
L_MAX = 10                                                               # (local) cited reference truncation

# Section 3 -- Pre-registered required-section list (frozen at plan-freeze; per §W2-6.5 + §W2-6.12)

REQUIRED_SECTIONS = [                                                    # (local)
    "Framework substrate-IS interpolation construction",
    "L1 / L3 boundary identification",
    "Intermediate-r falsifier-distinguishing prediction",
    "Cross-link to W9 CF-54 Path-(c) successor anchor",
]

# Pre-registered sub-bullet patterns for §1 substantive-content audit (plan §5 (i)-(iv)).
# Disjunction of regex patterns per `epistemic-discipline.md` §"Verifier-Rubric Pre-Registration"
# clause (1) "Pattern set: enumerate the specific lexical/structural patterns the verifier accepts"
# (2) "Disjunction-vs-conjunction declaration: state whether the verifier requires ALL patterns
# (conjunction) or ANY (disjunction) per content unit". Conjunction-by-clause: each of the 4
# clauses (i)-(iv) requires AT LEAST ONE matching pattern across the §1 body. The 4 clauses
# are PASS-AND'd at the audit-level (clause-conjunction).

REQUIRED_SUBPATTERNS_SEC1 = {                                            # (local)
    # (i) interpolation route: third regulator OR continuous deformation
    "(i) interpolation route": [
        r"third\s+(?:NCG-compatible\s+)?regulator",
        r"continuous\s+deformation\s+parameter",
        r"\bε\s*∈\s*\[\s*0\s*,\s*1\s*\]",
        r"5-atlas",
        r"5\+1",
        r"L1\s*↔\s*L3",
    ],
    # (ii) substrate-IS observable: Path-H/Path-C multi-valued α_s + n_s pair
    "(ii) substrate-IS observable": [
        r"multi-valued\s+\(?\s*α_s\s*,?\s*n_s",
        r"multi-valued\s+\(α_s,\s*n_s\)\s+pair",
        r"\(α_s,\s*n_s\).+regulator-class",
    ],
    # (iii) boundary identifications: ε=0 → L1/Path-H AND ε=1 → L3/Path-C
    "(iii) boundary identifications": [
        r"ε\s*=\s*0.*Path-H",
        r"ε\s*=\s*1.*Path-C",
    ],
    # (iv) falsifier-distinguishing prediction at intermediate-r ε ∈ (0, 1)
    "(iv) intermediate-r falsifier": [
        r"intermediate-r",
        r"falsifier-distinguishing",
        r"ε\s*∈\s*\(\s*0\s*,\s*1\s*\)",
    ],
}

# Section 4 -- Output paths

PAPER_PATH = PROJECT_ROOT / "papers" / "s87-path-h-path-c-interpolation.md"
VERDICT_TXT = resolve_output(87, 's87_gate_verdicts.txt')

# Input pin map (pinned files whose SHA-256 enters the audit_sha256 closure)

INPUT_FILES = [                                                          # (local)
    PROJECT_ROOT / "computations" / "_shared" / "canonical_constants.py",
    PROJECT_ROOT / "sessions" / "session-86" / "compute-carryforward.md",
    PROJECT_ROOT / ".claude" / "rules" / "regulator-pin-discipline.md",
    PROJECT_ROOT / ".claude" / "rules" / "registry-landing.md",
    PROJECT_ROOT / ".claude" / "rules" / "joint-theorem-promotion.md",
    PROJECT_ROOT / "sessions" / "session-plan" / "session-87-plan-w2.md",
    PAPER_PATH,
]

# Section 5 -- SHA-256 helpers (canonical pattern; cf. s87_w1b_lmax_weyl_convergence_sweep.py L203-247)

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} - input SHA-256 pins ===")
    pins = {}                                                            # (local)
    for p in inputs:
        sha = sha256_of(p)                                               # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")        # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins):
    items = sorted(pins.items())                                         # (local)
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path, canonical_path, pins):
    """audit_sha256 = SHA(script || canonical_constants.py || pinmap-json).
    content_sha256 = SHA(script bytes alone).
    Mirrors s87_w1b_lmax_weyl_convergence_sweep.py L231-247.
    """
    script_bytes = script_path.read_bytes()                              # (local)
    canonical_bytes = canonical_path.read_bytes()                        # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")                                                    # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                          # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()                                      # (local)
    return audit, content


# Section 6 -- Paper artifact-existence audit

def count_substantive_lines(text: str) -> int:
    """Count non-blank, non-pure-heading, non-pure-divider lines."""
    n = 0                                                                # (local)
    for raw in text.splitlines():
        line = raw.strip()                                               # (local)
        if not line:
            continue
        # Skip pure section dividers
        if re.fullmatch(r"-{3,}", line):
            continue
        # Skip pure heading lines (start with # but no body content beyond heading text)
        if line.startswith("#"):
            continue
        n += 1
    return n


def extract_section(paper_text: str, heading_substring: str) -> str:
    """Extract the body of a section whose heading contains `heading_substring`.
    Body extends from the matched heading to the next heading at the same or higher level.
    """
    lines = paper_text.splitlines()                                      # (local)
    in_section = False                                                   # (local)
    matched_level = None                                                 # (local)
    body_lines = []                                                      # (local)
    for raw in lines:
        m = re.match(r"^(#{1,6})\s+(.+)$", raw.strip())                  # (local)
        if m:
            level = len(m.group(1))                                      # (local)
            heading_text = m.group(2)                                    # (local)
            if not in_section:
                if heading_substring.lower() in heading_text.lower():
                    in_section = True
                    matched_level = level
                    continue
            else:
                # New heading at same or higher level => section ends.
                if level <= matched_level:
                    break
                # Sub-headings inside the section: include them as body.
        if in_section:
            body_lines.append(raw)
    return "\n".join(body_lines)


def audit_paper(paper_path: Path):
    """Returns (verdict_str, value_str, audit_diagnostics_dict).
    verdict_str ∈ {PASS, INFO, FAIL}, mapped per plan §5 thresholds.
    """
    diag = {}                                                            # (local)

    # Step 1: file presence
    if not paper_path.exists():
        diag["paper_present"] = False
        diag["reason"] = f"paper artifact missing at {paper_path}"
        return "FAIL", "paper_artifact_missing", diag
    diag["paper_present"] = True

    paper_text = paper_path.read_text(encoding="utf-8")                  # (local)
    diag["paper_size_bytes"] = len(paper_text.encode("utf-8"))
    diag["paper_total_lines"] = len(paper_text.splitlines())

    # Step 2: required section presence (4 sections per plan §12)
    sections_present = {}                                                # (local)
    section_bodies = {}                                                  # (local)
    for sec in REQUIRED_SECTIONS:
        body = extract_section(paper_text, sec)
        sections_present[sec] = (len(body) > 0)
        section_bodies[sec] = body
    diag["sections_present"] = sections_present

    missing = [s for s, present in sections_present.items() if not present]
    if missing:
        diag["missing_sections"] = missing
        diag["reason"] = f"required sections absent: {missing}"
        return "FAIL", "paper_artifact_missing_required_sections", diag

    # Step 3: §"Framework substrate-IS interpolation construction" substantive line count >= 15
    sec1_body = section_bodies["Framework substrate-IS interpolation construction"]
    sec1_substantive_lines = count_substantive_lines(sec1_body)
    diag["sec1_substantive_lines"] = sec1_substantive_lines
    diag["sec1_threshold"] = 15

    # Step 4: §1 (i)-(iv) sub-bullet pattern presence (each of 4 clauses must match >=1 pattern)
    sec1_subclause_status = {}                                           # (local)
    for clause_name, patterns in REQUIRED_SUBPATTERNS_SEC1.items():
        matches = []                                                     # (local)
        for pat in patterns:
            if re.search(pat, sec1_body, flags=re.IGNORECASE | re.MULTILINE):
                matches.append(pat)
        sec1_subclause_status[clause_name] = {
            "patterns_matched": matches,
            "matched": len(matches) > 0,
        }
    diag["sec1_subclause_status"] = sec1_subclause_status

    all_4_subclauses_ok = all(
        s["matched"] for s in sec1_subclause_status.values()
    )                                                                    # (local)
    diag["sec1_all_4_subclauses_ok"] = all_4_subclauses_ok

    # Step 5: PASS / INFO / FAIL mapping per plan §W2-6.5
    if (
        sections_present["Framework substrate-IS interpolation construction"]
        and sec1_substantive_lines >= 15
        and all_4_subclauses_ok
        and sections_present["L1 / L3 boundary identification"]
        and sections_present["Intermediate-r falsifier-distinguishing prediction"]
        and sections_present["Cross-link to W9 CF-54 Path-(c) successor anchor"]
    ):
        return "PASS", "paper_artifact_present_with_interpolation_construction", diag

    # INFO: §"Framework substrate-IS interpolation construction" present but
    # at least one of (i)-(iv) absent OR sec1 < 15 substantive lines.
    if sections_present["Framework substrate-IS interpolation construction"]:
        diag["reason"] = (
            f"§1 sec1_substantive_lines={sec1_substantive_lines} (>=15? "
            f"{sec1_substantive_lines >= 15}); 4-subclause ok? {all_4_subclauses_ok}"
        )
        return "INFO", "paper_artifact_present_with_partial_interpolation_construction", diag

    diag["reason"] = "§1 'Framework substrate-IS interpolation construction' absent"
    return "FAIL", "paper_artifact_missing_required_sections", diag


# Section 7 -- Verdict-line emission (canonical S81+ + W9a-99 dual-SHA + S87 schema-v2 3-tuple)

def append_verdict(verdict, value, audit_sha, content_sha,
                   sign_v, mag_v, regime_v):
    """Atomic append: canonical line + dual-SHA companion + schema-v2 3-tuple.
    Pattern mirrors s87_w1b_lmax_weyl_convergence_sweep.py L700-721.
    """
    canonical = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    dual_sha_row = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    schema_v2_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
        f"regime_verdict={regime_v} # {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical)
        fp.write(dual_sha_row)
        fp.write(schema_v2_row)


def map_to_3tuple(verdict: str):
    """Paper-mode 3-tuple: sign_verdict=N/A (no directional pre-reg);
    magnitude_verdict mirrors composite (PASS/INFO/FAIL all valid sub-states);
    regime_verdict=VALID always (artifact-existence has no regime-of-validity
    breakdown analog).
    """
    sign_v = "N/A"                                                       # (local) artifact-existence has no signed delta
    if verdict == "PASS":
        mag_v = "PASS"                                                   # (local)
    elif verdict == "INFO":
        mag_v = "INFO"                                                   # (local)
    else:
        mag_v = "FAIL"                                                   # (local)
    regime_v = "VALID"                                                   # (local) no regime-breakdown for artifact-existence
    return sign_v, mag_v, regime_v


# Section 8 -- Main

def main():
    t_start = time.time()                                                # (local)
    print("=" * 78)
    print(f"{GATE_ID} -- paper-mode artifact-existence audit")
    print("=" * 78)
    print(f"Paper path: {PAPER_PATH}")
    print(f"Verdict file: {VERDICT_TXT}")
    print()

    # 1. Pin SHAs (input-pin map closure provenance)
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)                                         # (local)
    print(f"  legacy closure: {closure[:16]}...")

    # 2. Compute dual-SHA (audit + content)
    script_path = Path(__file__).resolve()                               # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')                # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    # 3. Audit paper artifact + section presence + sub-clause patterns
    print("=== Paper artifact audit ===")
    verdict, value, diag = audit_paper(PAPER_PATH)
    print(f"  verdict: {verdict}")
    print(f"  value:   {value}")
    print(f"  diagnostics:")
    for k, v in diag.items():
        print(f"    {k}: {v}")
    print()

    # 4. Map to S87 schema-v2 3-tuple
    sign_v, mag_v, regime_v = map_to_3tuple(verdict)
    print(f"  3-tuple: sign={sign_v} magnitude={mag_v} regime={regime_v}")
    print()

    # 5. Emit verdict line
    append_verdict(verdict, value, audit_sha, content_sha, sign_v, mag_v, regime_v)
    print(f"  Verdict line appended to {VERDICT_TXT}")
    print(f"  Wall time: {time.time() - t_start:.2f}s")
    print()

    # Exit code per `math-scripts.md` §"Exit Codes and Verdict Semantics":
    # exit 0 on script success regardless of PASS/FAIL/INFO; non-zero only on
    # script breakage (paper missing handled in audit_paper return path).
    return 0


if __name__ == "__main__":
    sys.exit(main())
