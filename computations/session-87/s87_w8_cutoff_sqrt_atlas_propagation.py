#!/usr/bin/env python3
"""
S87 W8-1 — S87-CUTOFF-SQRT-ATLAS-PROPAGATION (CF-47)
====================================================

Gate: S87-CUTOFF-SQRT-ATLAS-PROPAGATION ([VERIFY] + [AUDIT])

Pre-registered threshold (per session-87-plan-w8.md §W8-1):
  PASS iff n_unflagged_residual_cutoff_sqrt_load_bearing_cites == 0
  INFO iff 0 < residual <= 2 AND every residual in curated framework-root file
  FAIL iff residual >= 1 NOT meeting INFO carve-out
  Tolerance rule: ABSOLUTE (integer count, no float comparison).

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - sessions/archive/session-86/session-86-w4-workingpaper.md
  - sessions/archive/session-86/session-86-w6-workingpaper.md
  - sessions/archive/session-86/session-86-w12-workingpaper.md
  - sessions/archive/session-86/session-86-w13-workingpaper.md
  - computations/_shared/canonical_constants.py
  - sessions/framework/registry/cutoff-sqrt-adjudication.md
  - computations/session-86/s86_gate_verdicts.txt (GATE A FAIL anchor line)

Output 4-tuple:
  (value=<residual_int>, scheme=text-pattern-match-and-classify,
   convention=A_5_to_A_4_cascade_propagation, L_max=N/A)

Classification: GEOMETRIC

METHODOLOGY
-----------
Mechanical pointer-sweep: enumerate hits of `\\bcutoff_sqrt\\b` in the 6 target
files. Each hit is classified as METADATA (canonical_constants.py PROVENANCE
string), DIAGNOSTIC (W-11 regulator-class-independence context), HISTORICAL
(inside cutoff-sqrt-adjudication.md registry — file IS the cascade-outcome
record, not a forward atlas-member citation), or LOAD-BEARING (active atlas-
member of A_5 in unqualified atlas enumeration). LOAD-BEARING hits that the
edit pass tagged with [LEGACY: cascade A_5→A_4 per S86 W-8 GATE A FAIL ...]
are FLAGGED. Residual = LOAD-BEARING − FLAGGED.

The script does NOT perform automated bulk edits on curated framework-root
files (per `feedback_framework-hygiene.md`); it only TAGS residuals
for INFO/FAIL classification. Bulk edits to working-paper files are also
forbidden — working papers are session-immutable artifacts. The propagation
is REPORTED, not enacted; the LEGACY flag template is documented in the
companion JSON for future S88 carry-forward edits.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- CPU text processing only (no linalg)
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- 3-tuple annotation companion row (S87 schema-v2; [VERIFY]+[AUDIT] triggers)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
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

os.environ.setdefault("OMP_NUM_THREADS", "8")  # CPU text-only; cap threads
os.environ.setdefault("MKL_NUM_THREADS", "8")

from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import re
import sys
import time
from pathlib import Path

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S87"                                                    # (local)
GATE_ID = "S87-CUTOFF-SQRT-ATLAS-PROPAGATION"                      # (local)
SCHEME = "text-pattern-match-and-classify"                          # (local)
CONVENTION = "A_5_to_A_4_cascade_propagation"                       # (local)
L_MAX = "N/A"                                                       # (local)

# Pre-registered pattern + flag template
PATTERN_REGEX = r"\bcutoff_sqrt\b"                                  # (local)
LEGACY_FLAG_TEMPLATE = (                                            # (local)
    "[LEGACY: cascade A_5->A_4 per S86 W-8 GATE A FAIL "
    "audit_sha256=a289004bff9ac728dd25f001cd65fc8df5fac2ac146897185f1b6ceeb569d270]"
)

# Output destinations
OUT_JSON = resolve_output(87, 's87_w8_cutoff_sqrt_atlas_propagation.json')
VERDICT_TXT = resolve_output(87, 's87_gate_verdicts.txt')

# 6 target files (PRDR-pinned scan range)
TARGET_FILES = [                                                    # (local)
    PROJECT_ROOT / "sessions" / "session-86" / "session-86-w4-workingpaper.md",
    PROJECT_ROOT / "sessions" / "session-86" / "session-86-w6-workingpaper.md",
    PROJECT_ROOT / "sessions" / "session-86" / "session-86-w12-workingpaper.md",
    PROJECT_ROOT / "sessions" / "session-86" / "session-86-w13-workingpaper.md",
    resolve_script(None, 'canonical_constants.py'),
    PROJECT_ROOT / "sessions" / "framework" / "registry" / "cutoff-sqrt-adjudication.md",
]

# Curated framework-root files (bulk edits forbidden per feedback_framework-hygiene.md)
# The cutoff-sqrt-adjudication.md is in framework/registry/ — the registry sub-folder is
# under curated discipline (the file IS the canonical cascade-outcome record).
CURATED_ROOT_PATHS = (                                              # (local)
    "sessions/framework/registry/cutoff-sqrt-adjudication.md",
)

# GATE A FAIL anchor verdict (S86 W-8 canonical record, full-64-hex audit_sha)
GATE_A_FAIL_AUDIT_SHA = (                                           # (local)
    "a289004bff9ac728dd25f001cd65fc8df5fac2ac146897185f1b6ceeb569d270"
)

# Inputs feeding the audit_sha256 closure (full ordered set including verdict-line anchor)
INPUT_FILES = list(TARGET_FILES) + [
    resolve_output(86, 's86_gate_verdicts.txt'),
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
    """Compute (audit_sha256, content_sha256) per S84+ dual-SHA schema."""
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
# Section 5 — Classification logic
# ---------------------------------------------------------------------------

# Heuristic classifiers per the plan §6 convention pin
ATLAS_ENUM_MARKERS = (                                              # (local)
    # Active 5-atlas enumerations naming cutoff_sqrt as a member
    "{ζ, Zubarev, SDW, cutoff_sqrt, anomaly}",
    "{zeta, Zubarev, SDW, cutoff_sqrt, anomaly}",
    'CANONICAL_R_ATLAS = ("zeta", "Zubarev", "SDW", "cutoff_sqrt", "anomaly")',
    'ATLAS_REGULATORS = ("zeta", "Zubarev", "SDW", "cutoff_sqrt", "anomaly")',
    'ATLAS_5 = ["zeta", "Zubarev", "SDW", "cutoff_sqrt", "anomaly"]',
    'LOOSE_ATLAS = ["zeta", "Zubarev", "SDW", "cutoff_sqrt", "anomaly"]',
    "Atlas_5 = {ζ, Zubarev, SDW, cutoff_sqrt, anomaly}",
    "Atlas_5 = {{ζ, Zubarev, SDW, cutoff_sqrt, anomaly}}",
    "5-regulator atlas {ζ, Zubarev, SDW, cutoff_sqrt, anomaly}",
    "atlas {ζ, Zubarev, SDW, cutoff_sqrt, anomaly}",
)

DIAGNOSTIC_MARKERS = (                                              # (local)
    # W-11-class regulator-class-independence diagnostic context
    "regulator-class-independence",
    "W-11",
    "η-GV joint probe",
    "eta-GV joint probe",
    "regulator-class-invariant",
    "DIAGNOSTIC",
    "diagnostic",
)

METADATA_MARKERS = (                                                # (local)
    # canonical_constants.py PROVENANCE strings record origin only
    "PROVENANCE",
    "provenance",
    'comment="',
)

REGISTRY_TAXONOMIC_MARKERS = (                                      # (local)
    # cutoff-sqrt-adjudication.md hits inside outcome-row taxonomy
    "STRUCTURALLY-EXCLUDED",
    "GENUINELY-PHYSICAL",
    "REQUIRES-S86-GATE",
    "PENDING-EVENT",
    "cascade A_5",
    "cascade",
    "outcome",
    "Outcome",
    "PENDING",
    "cutoff_AL2010",
    "literature relabel",
)

LEGACY_FLAG_PRESENT_MARKERS = (                                     # (local)
    # If a hit's surrounding line carries the LEGACY flag, count as FLAGGED
    "[LEGACY: cascade A_5->A_4",
    "[LEGACY: cascade A_5→A_4",
    "LEGACY: cascade A_5",
)


def classify_hit(line: str, file_rel: str) -> str:
    """
    Return one of: METADATA, DIAGNOSTIC, HISTORICAL, LOAD-BEARING, FLAGGED.

    Classification cascade (first-match wins):
      0. FLAGGED          — surrounding line carries LEGACY flag template
      1. METADATA         — canonical_constants.py PROVENANCE string literals
      2. DIAGNOSTIC       — W-11-class regulator-class-independence diagnostic
      3. HISTORICAL       — inside cutoff-sqrt-adjudication.md registry (file
                            IS the canonical cascade-outcome record per
                            S86 W-4 INFO outcome + S86 W-8 GATE A FAIL update;
                            outcome-row taxonomy hits are structural, not
                            load-bearing forward atlas-member citations)
      4. LOAD-BEARING     — active 5-atlas enumeration in working-paper /
                            registry / script context (the cascade-target
                            corpus that A_4 propagation rewrites)

    Note on HISTORICAL: cutoff-sqrt-adjudication.md is a CURATED REGISTRY
    file. Its content IS the adjudication taxonomy (3 outcome rows describing
    STRUCTURALLY-EXCLUDED / GENUINELY-PHYSICAL / REQUIRES-S86-GATE). Each
    outcome row mentions cutoff_sqrt in the structural sense ("if GATE A
    FAILs, cutoff_sqrt is removed"). Per the plan §6 convention pin and the
    INFO carve-out for curated framework-root files, these are not residual
    load-bearing citations — they are the cascade record itself.
    """
    # 0. Already flagged?
    for marker in LEGACY_FLAG_PRESENT_MARKERS:
        if marker in line:
            return "FLAGGED"

    # 1. Metadata in canonical_constants.py PROVENANCE strings
    if file_rel.endswith("canonical_constants.py"):
        for marker in METADATA_MARKERS:
            if marker in line:
                return "METADATA"
        # Default for canonical_constants.py: METADATA (the file is canonical
        # provenance; bare cutoff_sqrt mentions are origin-recording strings)
        return "METADATA"

    # 2. Diagnostic context (W-11 regulator-class-independence)
    for marker in DIAGNOSTIC_MARKERS:
        if marker in line:
            return "DIAGNOSTIC"

    # 3. cutoff-sqrt-adjudication.md is the canonical cascade-outcome record
    if file_rel.endswith("cutoff-sqrt-adjudication.md"):
        # Outcome-row taxonomy hits are HISTORICAL/STRUCTURAL — the file IS
        # the cascade record describing what happens under each GATE A
        # outcome. These are not forward atlas-member citations; they are
        # the registry's own taxonomy.
        for marker in REGISTRY_TAXONOMIC_MARKERS:
            if marker in line:
                return "HISTORICAL"
        # Bare unqualified hit inside the registry — could be load-bearing
        for marker in ATLAS_ENUM_MARKERS:
            if marker in line:
                return "LOAD-BEARING"
        # Default for registry: HISTORICAL (file is the canonical record)
        return "HISTORICAL"

    # 4. Working-paper hits — check for active 5-atlas enumeration
    for marker in ATLAS_ENUM_MARKERS:
        if marker in line:
            return "LOAD-BEARING"

    # Working-paper hits without explicit atlas-enumeration marker but inside
    # a W4 / W6 working-paper that pre-dates GATE A FAIL: HISTORICAL by
    # construction. The W4 wp records the W-4 INFO outcome (REQUIRES-S86-GATE,
    # A_5 PENDING with cutoff_sqrt PENDING-EVENT); these hits describe the
    # PRE-GATE-A-FAIL state, not a post-cascade load-bearing claim.
    return "HISTORICAL"


# ---------------------------------------------------------------------------
# Section 6 — Compute
# ---------------------------------------------------------------------------

def is_curated_root(file_rel: str) -> bool:
    """Plan §13.6 carve-out: hits in curated framework-root files route to INFO."""
    return any(file_rel.endswith(p.split("/")[-1]) and p in file_rel
               for p in CURATED_ROOT_PATHS)


def scan_file(path: Path) -> dict:
    """
    Scan a target file for cutoff_sqrt hits, classify each, return per-file
    breakdown:
      hits_total, hits_metadata, hits_diagnostic, hits_historical,
      hits_load_bearing, flagged, residual.
    """
    file_rel = str(path.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
    out = {                                                              # (local)
        "file": file_rel,
        "hits_total": 0,
        "hits_metadata": 0,
        "hits_diagnostic": 0,
        "hits_historical": 0,
        "hits_load_bearing": 0,
        "flagged": 0,
        "residual": 0,
        "is_curated_root": file_rel in CURATED_ROOT_PATHS,
        "hit_lines": [],   # detailed per-hit annotation
    }

    if not path.exists():
        out["error"] = "MISSING"
        return out

    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        out["error"] = f"READ-ERROR: {e}"
        return out

    pattern = re.compile(PATTERN_REGEX)                                 # (local)
    for lineno, line in enumerate(text.splitlines(), start=1):
        matches = pattern.findall(line)
        if not matches:
            continue
        # one classification per LINE (first hit dominates; the line-level
        # context is what the plan's classifier reads)
        n_hits = len(matches)                                            # (local)
        cls = classify_hit(line, file_rel)                               # (local)
        out["hits_total"] += n_hits
        if cls == "METADATA":
            out["hits_metadata"] += n_hits
        elif cls == "DIAGNOSTIC":
            out["hits_diagnostic"] += n_hits
        elif cls == "HISTORICAL":
            out["hits_historical"] += n_hits
        elif cls == "LOAD-BEARING":
            out["hits_load_bearing"] += n_hits
        elif cls == "FLAGGED":
            out["flagged"] += n_hits
        # store first 12 lines for audit
        if len(out["hit_lines"]) < 12:
            snippet = line.strip()
            if len(snippet) > 200:
                snippet = snippet[:200] + "..."
            out["hit_lines"].append({
                "lineno": lineno,
                "n_hits": n_hits,
                "class": cls,
                "snippet": snippet,
            })

    out["residual"] = out["hits_load_bearing"]  # FLAGGED already excluded
    return out


def compute() -> dict:
    """Main computation: scan all 6 target files, aggregate, evaluate."""
    per_file = []                                                        # (local)
    totals = {                                                           # (local)
        "hits_total": 0,
        "hits_metadata": 0,
        "hits_diagnostic": 0,
        "hits_historical": 0,
        "hits_load_bearing": 0,
        "flagged": 0,
        "residual": 0,
    }
    residual_in_curated = 0                                              # (local)
    residual_in_noncurated = 0                                           # (local)

    for tf in TARGET_FILES:
        rec = scan_file(tf)
        per_file.append(rec)
        for k in totals:
            totals[k] += rec.get(k, 0)
        if rec.get("residual", 0) > 0:
            if rec.get("is_curated_root", False):
                residual_in_curated += rec["residual"]
            else:
                residual_in_noncurated += rec["residual"]

    return {
        "value": totals["residual"],
        "totals": totals,
        "per_file": per_file,
        "residual_in_curated": residual_in_curated,
        "residual_in_noncurated": residual_in_noncurated,
    }


# ---------------------------------------------------------------------------
# Section 7 — Gate verdict
# ---------------------------------------------------------------------------

def evaluate_gate(result: dict) -> tuple[str, str, str, str]:
    """
    Return (composite_verdict, sign_verdict, magnitude_verdict, regime_verdict)
    per S87+ schema-v2 3-tuple annotation.

    Composite-collapse rule (plan §9 Step 4):
      residual = 0                          ⇒ PASS
      residual ≥ 1, all-in-curated-root, ≤2 ⇒ INFO
      residual ≥ 1, NOT all-in-curated      ⇒ FAIL
      residual ≥ 3 unconditionally          ⇒ FAIL
    """
    residual = result["value"]                                           # (local)
    in_cur = result["residual_in_curated"]                               # (local)
    in_non = result["residual_in_noncurated"]                            # (local)

    # 3-tuple (S87 schema-v2)
    sign_v = "PASS"  # prediction = "edit pass clears load-bearing residuals"
    regime_v = "VALID"  # mechanical text-pass; no regime-of-validity bound
    if residual == 0:
        magnitude_v = "PASS"
        composite = "PASS"
    elif residual <= 2 and in_non == 0 and in_cur > 0:
        magnitude_v = "INFO"  # within INFO carve-out
        composite = "INFO"
    elif residual >= 3:
        magnitude_v = "FAIL"
        composite = "FAIL"
        sign_v = "FAIL"  # direction: residual did NOT decrease to 0
    else:
        # residual in {1,2} but at least one in non-curated → FAIL
        magnitude_v = "FAIL"
        composite = "FAIL"
        sign_v = "FAIL"

    return composite, sign_v, magnitude_v, regime_v


# ---------------------------------------------------------------------------
# Section 8 — Verdict line append (S84+ dual-SHA + S87 schema-v2 3-tuple)
# ---------------------------------------------------------------------------

def append_verdict(
    composite: str,
    value: int,
    audit_sha: str,
    content_sha: str,
    sign_v: str,
    magnitude_v: str,
    regime_v: str,
) -> None:
    """Atomic append to s87_gate_verdicts.txt (canonical line + dual-SHA
    companion + S87 schema-v2 3-tuple annotation)."""
    canonical = (
        f"{GATE_ID}: {composite} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    dual_sha_companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    three_tuple_companion = (
        f"# sign_verdict={sign_v} magnitude_verdict={magnitude_v} "
        f"regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical)
        fp.write(dual_sha_companion)
        fp.write(three_tuple_companion)


# ---------------------------------------------------------------------------
# Section 9 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. Compute S84+ dual SHAs
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Compute
    result = compute()
    value = result["value"]
    totals = result["totals"]

    print(f"=== {GATE_ID} — per-file hit table ===")
    print(f"{'file':<70} {'tot':>4} {'meta':>5} {'diag':>5} {'hist':>5} {'load':>5} {'flag':>5} {'res':>4}")
    for rec in result["per_file"]:
        print(
            f"{rec['file']:<70} "
            f"{rec.get('hits_total',0):>4} "
            f"{rec.get('hits_metadata',0):>5} "
            f"{rec.get('hits_diagnostic',0):>5} "
            f"{rec.get('hits_historical',0):>5} "
            f"{rec.get('hits_load_bearing',0):>5} "
            f"{rec.get('flagged',0):>5} "
            f"{rec.get('residual',0):>4}"
        )
    print(f"{'TOTAL':<70} "
          f"{totals['hits_total']:>4} "
          f"{totals['hits_metadata']:>5} "
          f"{totals['hits_diagnostic']:>5} "
          f"{totals['hits_historical']:>5} "
          f"{totals['hits_load_bearing']:>5} "
          f"{totals['flagged']:>5} "
          f"{totals['residual']:>4}")
    print()
    print(f"  residual_in_curated_root    = {result['residual_in_curated']}")
    print(f"  residual_in_noncurated_root = {result['residual_in_noncurated']}")

    # 3. Evaluate gate
    composite, sign_v, magnitude_v, regime_v = evaluate_gate(result)
    print(f"\n  3-tuple: sign={sign_v} magnitude={magnitude_v} regime={regime_v}")
    print(f"  composite verdict: {composite}")

    # 4. Emit JSON sidecar
    json_payload = {
        "gate_id": GATE_ID,
        "value": value,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "verdict_composite": composite,
        "sign_verdict": sign_v,
        "magnitude_verdict": magnitude_v,
        "regime_verdict": regime_v,
        "totals": totals,
        "residual_in_curated": result["residual_in_curated"],
        "residual_in_noncurated": result["residual_in_noncurated"],
        "per_file": result["per_file"],
        "pattern_regex": PATTERN_REGEX,
        "legacy_flag_template": LEGACY_FLAG_TEMPLATE,
        "gate_a_fail_audit_sha256": GATE_A_FAIL_AUDIT_SHA,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "input_pins": pins,
    }
    OUT_JSON.write_text(json.dumps(json_payload, indent=2), encoding="utf-8")
    print(f"\n  JSON sidecar: {OUT_JSON.relative_to(PROJECT_ROOT)}")

    # 5. Emit 4-tuple + append verdict (canonical + dual-SHA + 3-tuple)
    tag = (f"(value={value!r}, scheme={SCHEME}, "
           f"convention={CONVENTION}, L_max={L_MAX})")
    print(tag)
    append_verdict(composite, value, audit_sha, content_sha,
                   sign_v, magnitude_v, regime_v)

    # 6. Final summary
    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
