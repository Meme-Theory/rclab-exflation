#!/usr/bin/env python3
"""
S85 W1c-3 — HISTORICAL-ALPHA-S-USAGE-AUDIT
==========================================

Gate: S85-W1c-HISTORICAL-ALPHA-S-USAGE-AUDIT ([AUDIT])

Pre-registered threshold (plan §W1c-3):
  PASS iff N_ambiguous_sites <= 5 (normal hygiene)
  INFO iff 5 < N_ambiguous_sites <= 20 (sub-campaign-scale)
  FAIL iff N_ambiguous_sites > 20 (systemic contamination)
  Tolerance rule: ABSOLUTE integer thresholds (no RATIO interpretation).

Scope (plan §W1c-3.7; actual file counts measured at runtime):
  - computations/_shared/*.py (~1361 files; ~232 mention alpha_s)
  - sessions/session-*/*.md (active + archive, S34+) (~1045 files)
  - sessions/framework/Atlas/atlas-*.md (11 files)  [plan said summary/atlas-*.md, path bug]
  - Session-floor filter: S34 (plan specifies S34-S85)

Output 4-tuple:
  (value=<N_ambiguous_sites>, scheme=symbol-usage-audit,
   convention=S34-S85, L_max=N/A)

Classification: META (cross-session symbol hygiene)

METHODOLOGY
-----------
For each file matching the globs above:
  1. Read the file.
  2. Find every line containing `alpha_s` (case-insensitive; whole-word-ish
     boundary so `alpha_star` and `alpha_scan` are NOT matched).
  3. Classify each line using the ±5-line context:

     QCD: any of (alpha_s_MZ_obs, alpha_s_MZ, M_Z, strong coupling, QCD,
                   PDG 2024, alpha_s(M_Z), perturbative QCD, beta-function,
                   alpha_s(M_Z)_obs, hadronic, gluon)
     INFLATIONARY: any of (planck_alpha_s, dn_s/dlnk, Mukhanov-Sasaki,
                           slow-roll, running of n_s, CMB pivot, spectral
                           index, Planck 2018, k_pivot, inflation running,
                           scalar spectral, n_s, sigma_8)
     FRAMEWORK-IDENTITY: any of (alpha_s_framework_central,
                                  alpha_s_inflation_framework,
                                  n_s_canon**2, n_s**2-1, n_s^2-1,
                                  S50-51 identity, -0.068968, alpha_s=n_s^2-1)
     AMBIGUOUS: none of the above present in context

Class precedence when multiple classes match (plan §W1c-3.6):
   FRAMEWORK-IDENTITY > QCD > INFLATIONARY > AMBIGUOUS
   (A single usage naming the identity is framework-specific; if both
   inflationary and QCD context appear, QCD wins — QCD physics is always
   flagged first so downstream reviewers notice the potential collision.)

Aggregate output:
  - Per-class count
  - Per-file table with classification breakdown
  - AMBIGUOUS remediation list (file:line:context-snippet for each site)

DISCIPLINE
----------
- `from canonical_constants import *` at top
- All local intermediates tagged `# (local)`
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- Exit 0 regardless of PASS/FAIL per .claude/rules/math-scripts.md
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
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


# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S85"                                              # (local)
GATE_ID = "S85-W1c-HISTORICAL-ALPHA-S-USAGE-AUDIT"           # (local)
SCHEME = "symbol-usage-audit"                                # (local)
CONVENTION = "S34-S85"                                       # (local)
L_MAX = "N/A"                                                # (local)

# Pre-registered thresholds (plan §W1c-3.9)
PASS_MAX_AMBIGUOUS = 5                                       # (local)
INFO_MAX_AMBIGUOUS = 20                                      # (local)

# Session floor (plan §W1c-3.7)
SESSION_FLOOR = 34                                           # (local)

CANONICAL_PATH = resolve_script(None, 'canonical_constants.py')
VERDICT_TXT = resolve_output(85, 's85_gate_verdicts.txt')
OUT_JSON = resolve_output(85, 's85_w1c_historical_alpha_s_audit.json')

# Match alpha_s as a symbol (not alpha_star, alpha_scan, etc.)
# Accept alpha_s, alpha_s_MZ, alpha_s(M_Z), alpha_s = ..., etc.
ALPHA_S_RE = re.compile(
    r"alpha_s(?![a-zA-Z0-9_])"     # alpha_s not followed by a word char
    r"|alpha_s_(?:MZ|mz|framework|inflation|central|QCD|qcd)"
    r"|α_s"                         # unicode variant
    r"|α\s*_\s*s",
    re.IGNORECASE,
)

# Classification keyword sets (case-insensitive)
QCD_KEYWORDS = [
    "alpha_s_mz_obs", "alpha_s_mz", "m_z", "strong coupling", "qcd",
    "pdg 2024", "alpha_s(m_z)", "perturbative qcd", "beta-function",
    "beta function", "hadronic", "gluon", "alphas(mz)", "running coupling",
    "strong sector",
]  # (local)

INFLATIONARY_KEYWORDS = [
    "planck_alpha_s", "dn_s/dlnk", "mukhanov-sasaki", "mukhanov",
    "slow-roll", "slow roll", "running of n_s", "cmb pivot",
    "spectral index", "planck 2018", "k_pivot", "inflation running",
    "scalar spectral", "sigma_8", "sigma8", "dn_s", "cmb",
    "acoustic power", "power spectrum tilt",
]  # (local)

FRAMEWORK_IDENTITY_KEYWORDS = [
    "alpha_s_framework_central", "alpha_s_inflation_framework",
    "n_s_canon**2", "n_s**2 - 1", "n_s^2 - 1", "n_s^2-1", "n_s**2-1",
    "s50-51 identity", "-0.068968", "alpha_s = n_s",
    "0.9649**2 - 1", "s50-51 framework identity", "identity prediction",
]  # (local)

# ---------------------------------------------------------------------------
# Section 4 — SHA helpers (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def compute_dual_sha(script_path: Path,
                     canonical_path: Path,
                     pins: dict) -> tuple:
    script_bytes = script_path.read_bytes()  # (local)
    canonical_bytes = canonical_path.read_bytes()  # (local)
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
# Section 5 — File discovery with S34+ filter
# ---------------------------------------------------------------------------

SESSION_NUM_RE = re.compile(r"session[-_/](\d+)", re.IGNORECASE)  # (local)


def session_num_of(path: Path) -> int:
    """Extract the session number from a path; return 0 if unparseable."""
    m = SESSION_NUM_RE.search(str(path))
    if not m:
        return 0
    try:
        return int(m.group(1))
    except ValueError:
        return 0


def discover_files() -> dict:
    """Return a dict {scope_name: [Path, ...]} filtered to S34+."""
    computation_files = sorted((PROJECT_ROOT / "computations").glob("*.py"))  # (local)
    # Sessions: both active and archive
    session_paths = []  # (local)
    for glob in ("sessions/session-*/*.md",
                 "sessions/archive/session-*/*.md"):
        session_paths.extend(sorted(PROJECT_ROOT.glob(glob)))
    # Filter sessions to S34+
    sessions_s34plus = [p for p in session_paths
                        if session_num_of(p) >= SESSION_FLOOR]  # (local)
    atlas = sorted((PROJECT_ROOT / "sessions" / "framework" / "Atlas")
                   .glob("atlas-*.md"))  # (local)
    return {"computations": computation_files,
            "sessions": sessions_s34plus,
            "atlas": atlas}


# ---------------------------------------------------------------------------
# Section 6 — Classification of a single usage site
# ---------------------------------------------------------------------------


def classify_context(context: str) -> str:
    """Return one of {FRAMEWORK-IDENTITY, QCD, INFLATIONARY, AMBIGUOUS}
    for a given ±5-line context blob (already lowercased)."""
    if any(kw in context for kw in FRAMEWORK_IDENTITY_KEYWORDS):
        return "FRAMEWORK-IDENTITY"
    if any(kw in context for kw in QCD_KEYWORDS):
        return "QCD"
    if any(kw in context for kw in INFLATIONARY_KEYWORDS):
        return "INFLATIONARY"
    return "AMBIGUOUS"


def scan_file(path: Path) -> dict:
    """Grep alpha_s, classify each hit by ±5-line context.
    Return per-class counts + snippets for AMBIGUOUS sites."""
    try:
        lines = path.read_text(encoding="utf-8",
                               errors="replace").splitlines()
    except OSError:
        return {"QCD": 0, "INFLATIONARY": 0, "FRAMEWORK-IDENTITY": 0,
                "AMBIGUOUS": 0, "ambiguous_sites": []}

    per_class = {"QCD": 0, "INFLATIONARY": 0,
                 "FRAMEWORK-IDENTITY": 0, "AMBIGUOUS": 0}  # (local)
    ambiguous_sites = []  # (local)

    for i, line in enumerate(lines):
        if ALPHA_S_RE.search(line):
            lo = max(0, i - 5)  # (local)
            hi = min(len(lines), i + 6)  # (local)
            context = "\n".join(lines[lo:hi]).lower()  # (local)
            cls = classify_context(context)  # (local)
            per_class[cls] += 1
            if cls == "AMBIGUOUS":
                ambiguous_sites.append({
                    "line": i + 1,
                    "snippet": line.strip()[:200],
                })
    return {**per_class, "ambiguous_sites": ambiguous_sites}


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------


def main() -> int:
    t0 = time.time()  # (local)

    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    canonical_sha = sha256_of(CANONICAL_PATH)  # (local)
    script_sha = sha256_of(Path(__file__).resolve())  # (local)
    print(f"  canonical_constants.py (post-W1c-1): {canonical_sha[:16]}...")
    print(f"  script (self):                       {script_sha[:16]}...")

    # 1. Discover files
    files = discover_files()  # (local)
    print(f"  computation scripts (all):            {len(files["computations"])}")
    print(f"  sessions markdown (S34+):       {len(files['sessions'])}")
    print(f"  atlas markdown:                 {len(files['atlas'])}")
    print()

    # 2. Scan everything. For computation scripts, DON'T SHA-pin every file
    # (1361 files -> enormous audit pinmap); instead, pin per-scope
    # aggregate SHA (concat of all file bytes, hashed once).
    def scope_aggregate_sha(paths: list) -> str:
        h = hashlib.sha256()
        for p in paths:
            try:
                h.update(p.name.encode("utf-8"))
                h.update(b"\x00")
                h.update(p.read_bytes())
                h.update(b"\x01")
            except OSError:
                continue
        return h.hexdigest()

    print("=== Scoping SHA (per-scope aggregate) ===")
    scope_shas = {}  # (local)
    for name, paths in files.items():
        sh = scope_aggregate_sha(paths)  # (local)
        scope_shas[name] = sh
        print(f"  {name:12s} ({len(paths):4d} files): {sh[:16]}...")
    print()

    # 3. Per-file scan
    totals = {"QCD": 0, "INFLATIONARY": 0,
              "FRAMEWORK-IDENTITY": 0, "AMBIGUOUS": 0}  # (local)
    per_file = {}  # (local)
    ambiguous_remediation = []  # (local)
    all_paths = files["computations"] + files["sessions"] + files["atlas"]  # (local)

    for p in all_paths:
        result = scan_file(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        # Only record files with at least one hit
        hits = (result["QCD"] + result["INFLATIONARY"]
                + result["FRAMEWORK-IDENTITY"] + result["AMBIGUOUS"])  # (local)
        if hits > 0:
            per_file[rel] = {k: result[k] for k in
                             ("QCD", "INFLATIONARY", "FRAMEWORK-IDENTITY",
                              "AMBIGUOUS")}
            for k in totals:
                totals[k] += result[k]
            for site in result["ambiguous_sites"]:
                ambiguous_remediation.append({
                    "file": rel,
                    "line": site["line"],
                    "snippet": site["snippet"],
                })

    n_ambig = totals["AMBIGUOUS"]  # (local)
    n_total_hits = sum(totals.values())  # (local)
    n_files_with_hits = len(per_file)  # (local)

    print(f"=== Aggregate classification ===")
    print(f"  Files scanned:                 {len(all_paths)}")
    print(f"  Files with >=1 alpha_s hit:    {n_files_with_hits}")
    print(f"  Total alpha_s usage sites:     {n_total_hits}")
    print(f"    QCD:                {totals['QCD']}")
    print(f"    INFLATIONARY:       {totals['INFLATIONARY']}")
    print(f"    FRAMEWORK-IDENTITY: {totals['FRAMEWORK-IDENTITY']}")
    print(f"    AMBIGUOUS:          {n_ambig}")
    print()

    # 4. Dispatch on N_ambiguous
    if n_ambig <= PASS_MAX_AMBIGUOUS:
        final_status = "PASS"  # (local)
        reason = f"N_ambiguous={n_ambig} <= PASS_MAX={PASS_MAX_AMBIGUOUS}"  # (local)
    elif n_ambig <= INFO_MAX_AMBIGUOUS:
        final_status = "INFO"  # (local)
        reason = (f"N_ambiguous={n_ambig} in ({PASS_MAX_AMBIGUOUS}, "
                  f"{INFO_MAX_AMBIGUOUS}] -> sub-campaign-scale remediation")  # (local)
    else:
        final_status = "FAIL"  # (local)
        reason = (f"N_ambiguous={n_ambig} > INFO_MAX={INFO_MAX_AMBIGUOUS} "
                  f"-> systemic contamination; requires W1d campaign")  # (local)

    # 5. Compute dual-SHA over scope-aggregate SHAs
    pins = {
        "computations/_shared/canonical_constants.py": canonical_sha,
        "computations-scope-aggregate": scope_shas["computations"],
        "sessions-scope-aggregate": scope_shas["sessions"],
        "atlas-scope-aggregate": scope_shas["atlas"],
    }  # (local)
    audit_sha, content_sha = compute_dual_sha(Path(__file__).resolve(),
                                              CANONICAL_PATH, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    # 6. Emit 4-tuple + verdict line
    value = n_ambig  # (local)
    four_tuple = (f"(value={value}, scheme={SCHEME}, "
                  f"convention={CONVENTION}, L_max={L_MAX})")  # (local)
    print("\n" + four_tuple)

    line = (
        f"{GATE_ID}: {final_status} -- value={value} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)

    # 7. Persist JSON summary (truncate per_file if huge)
    summary = {
        "gate_id": GATE_ID,
        "status": final_status,
        "value": value,
        "reason": reason,
        "totals": totals,
        "n_files_scanned": len(all_paths),
        "n_files_with_hits": n_files_with_hits,
        "n_total_hits": n_total_hits,
        "per_file": per_file,
        "ambiguous_remediation": ambiguous_remediation,
        "scope_shas": scope_shas,
        "canonical_sha": canonical_sha,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "path_discrepancies": {
            "plan_atlas_glob": "summary/atlas-*.md",
            "actual_atlas_glob": "sessions/framework/Atlas/atlas-*.md",
        },
        "thresholds": {
            "PASS_MAX_AMBIGUOUS": PASS_MAX_AMBIGUOUS,
            "INFO_MAX_AMBIGUOUS": INFO_MAX_AMBIGUOUS,
            "session_floor": SESSION_FLOOR,
        },
    }  # (local)
    OUT_JSON.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {final_status} (wall {wall:.2f}s) ===")
    print(f"    Reason: {reason}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
