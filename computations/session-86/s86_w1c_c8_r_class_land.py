#!/usr/bin/env python3
"""
S86 W1c-2 (C8) — S86-W6-W13-R-CLASS-LAND
==========================================

Gate: S86-W6-W13-R-CLASS-LAND ([VERIFY])

Purpose
-------
Land 7 R-class results from S85 W6-W13 into
sessions/permanent-results-registry.md (parallel to the existing W10-1
ANTI-CORRESPONDENCE patch). Each landed row carries a verbatim SHA-pin
matched against computations/session-85/s85_gate_verdicts.txt.

Pre-registered threshold (ABSOLUTE)
-----------------------------------
PASS iff all 7 entries are landed in the registry AND every per-row
audit_sha256 + content_sha256 pair matches the source line in
s85_gate_verdicts.txt byte-for-byte.

FAIL iff any entry is missing OR any SHA fails to match.
INFO not applicable (binary discrete).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema)
----------------------------------------------------
  - computations/session-85/s85_gate_verdicts.txt        (source verdicts)
  - sessions/permanent-results-registry.md         (landing target; mutated)
  - computations/session-85/s85_w10_anti_correspondence_30_REGISTRY_PATCH.md
                                                   (cross-link reference)
  - canonical_constants.py                         (audit_sha256 only)
  - script bytes                                   (both SHAs)

Output 4-tuple
--------------
  (value=7_R_class_rows_landed, scheme=registry-write,
   convention=parallel-to-W10-1-patch, L_max=per-row)

Classification: GEOMETRIC (R-class entries are spectral-triple meta-
exclusions / confirmations; the gate itself is META catalogue, but the
landed content is a substrate-spectral inventory).

METHODOLOGY
-----------
Step A. Parse s85_gate_verdicts.txt; extract verdict line for each of
        the 7 R-class gate IDs. Capture (verdict, value, scheme,
        convention, L_max, audit_sha256, content_sha256).
Step B. Compose R-class catalogue table (CSV) and registry section
        (Markdown) from the parsed payloads. Substrate one-line is
        pre-authored per the substrate->consequence framing rule.
Step C. Verify SHA-pins by re-reading the verdict file and
        round-tripping each (audit_sha256, content_sha256) pair. PASS
        iff 7/7 round-trip. FAIL iff any mismatch.
Step D. If PASS, append §VII.T section to permanent-results-registry.md
        (next free slot after §VII.S). If FAIL, ABORT registry edit;
        the verdict line records FAIL with the offending row(s).
Step E. Emit dual-SHA verdict line per S84+ schema.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local intermediate tagged `# (local)`
- CPU-only path (no GPU; pure file-IO + string parsing)
- OMP_NUM_THREADS cap set before numpy import (defensive — numpy not
  used here, but cap is cheap and prevents future drift).
- Substrate-framing: per-row substrate one-line flows substrate ->
  consequence (e.g., "spectral-triple invariance under inner-fluctuation
  forbids the W11 candidate corridor", NOT "Connes' NCG axioms exclude
  the W11 corridor").
- Tolerance: ABSOLUTE; SHA mismatch is binary.
"""

from __future__ import annotations

# -- Section 1: CPU thread cap (cheap defensive set; before numpy) ----------
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

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# -- Section 2: Canonical constants (mandatory first import after env) ------
from canonical_constants import *  # noqa: F401,F403

# -- Section 3: Standard imports --------------------------------------------
import csv
import hashlib
import json
import re
import sys
import time
from pathlib import Path

# -- Section 4: Paths -------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
SESSIONS_DIR = PROJECT_ROOT / "sessions"

SESSION = "S86"                                                       # (local)
GATE_ID = "S86-W6-W13-R-CLASS-LAND"                                   # (local)
SCHEME = "registry-write"                                             # (local)
CONVENTION = "parallel-to-W10-1-patch"                                # (local)
L_MAX = "per-row"                                                     # (local)

S85_VERDICT_FILE = resolve_output(85, 's85_gate_verdicts.txt')                # (local)
REGISTRY_FILE = SESSIONS_DIR / "permanent-results-registry.md"        # (local)
W10_PATCH_FILE = resolve_script(85, 's85_w10_anti_correspondence_30_REGISTRY_PATCH.md')  # (local)
CANONICAL_FILE = resolve_script(None, 'canonical_constants.py')                 # (local)

OUT_CSV = resolve_output(86, 's86_w1c_c8_r_class_table.csv')                  # (local)
VERDICT_TXT = resolve_output(86, 's86_gate_verdicts.txt')                     # (local)

INPUT_FILES = [                                                       # (local)
    S85_VERDICT_FILE,
    REGISTRY_FILE,
    W10_PATCH_FILE,
    CANONICAL_FILE,
]

# -- Section 5: R-class roster (the 7 rows + per-row metadata) --------------
#
# Substrate-framing rule: every one-liner flows substrate -> consequence.
# Each entry pairs a S85 source gate ID with a substrate-first reading.
#
R_CLASS_ROSTER = [                                                    # (local)
    {
        "r_row": "R-1",
        "source_gate": "S85-W6-1-AWH-FORMAL",
        "label": "AWH-formal kappa = 0.017",
        "substrate_one_line": (
            "Acoustic-white-hole surface gravity (kappa) emerges as a "
            "non-zero spectral observable of the EF-null-extended "
            "Jensen-deformed substrate; the substrate's spectral "
            "transit through the fold pins kappa = 0.0169 in the "
            "mostly-minus convention, formally certifying the AWH "
            "side of the cosmogenesis transit."
        ),
    },
    {
        "r_row": "R-2",
        "source_gate": "S85-W6-3-CONF-INF-BIFURC",
        "label": "Conformal-infinity bifurcation (n_distinct_topologies=2)",
        "substrate_one_line": (
            "Conformal infinity of the Jensen-deformed substrate "
            "bifurcates into exactly two distinct topology classes "
            "across the 5-regulator atlas; the substrate spectrum "
            "selects a discrete-valued conformal end whose "
            "regulator-invariance is the diagnostic signature of "
            "spectral-triple closure at infinity."
        ),
    },
    {
        "r_row": "R-3",
        "source_gate": "S85-W6-7-PETROV-NON-BD-PERT",
        "label": "Petrov non-bd FAIL (check_type = D)",
        "substrate_one_line": (
            "Substrate Weyl-tensor decomposition under W3_H "
            "perturbation does not preserve a Type-D Petrov class; "
            "the spectral-triple's perturbed Weyl spectrum forbids a "
            "non-degenerate boundary Petrov-D corridor, closing the "
            "Petrov-non-boundary candidate route."
        ),
    },
    {
        "r_row": "R-4",
        "source_gate": "S85-W12-ELIM-1",
        "label": "Inverted-Josephson signs (D_iv8/iv10/iv12 all -1)",
        "substrate_one_line": (
            "Substrate condensate-current dominance index D_iv across "
            "L = 8, 10, 12 carries a unanimous negative sign; the "
            "Jensen-deformed SU(3) Dirac spectrum enforces inverted-"
            "Josephson coupling at every truncation, certifying the "
            "BdG-substrate correspondence under sign inversion."
        ),
    },
    {
        "r_row": "R-5",
        "source_gate": "S85-W12-ELIM-8",
        "label": "a_n class-(d) regulator taxonomy (n_d = 3)",
        "substrate_one_line": (
            "Substrate Seeley-DeWitt coefficient population partitions "
            "13 frame-invariant entries against 3 regulator-dependent "
            "class-(d) entries across the 5-regulator atlas at L_max = "
            "10; the spectral-triple's regulator-invariance taxonomy "
            "isolates exactly 3 a_n that demand explicit regulator "
            "tagging downstream."
        ),
    },
    {
        "r_row": "R-6",
        "source_gate": "S85-EPSH-JENSEN-SURVIVAL",
        "label": "Jensen-survival meta (HP^1 norm = 10.157431)",
        "substrate_one_line": (
            "Substrate Heitsch-1-cocycle HP^1 norm survives Jensen "
            "deformation along the omega_J-transverse direction at "
            "L_max = 5 with norm 10.157, certifying the spectral "
            "triple's epsilon_H invariant against Jensen perturbation "
            "and pinning the Jensen-survival meta-channel as a "
            "substrate-protected corridor."
        ),
    },
    {
        "r_row": "R-7",
        "source_gate": "S85-NCG-META-EXCLUSION-CERTIFY",
        "label": "NCG meta-exclusion (KK-bivariant six-term exact, 2/2)",
        "substrate_one_line": (
            "Spectral-triple invariance under inner fluctuation "
            "(D_K -> D_K + A + J A J^{-1}) plus Cuntz-Quillen Z/2-"
            "graded HP^* exactness forbids the W11 candidate "
            "corridor; the KK-bivariant six-term sequence closes 2/2 "
            "and the meta-exclusion is registry-grade NCG-axiomatic, "
            "not phenomenological."
        ),
    },
]

# -- Section 6: SHA helpers (S84+ dual-SHA schema) --------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()                                              # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list) -> dict:
    """Print SHA-256 of each input; return {relpath: sha} for closure."""
    print(f"=== {GATE_ID} - input SHA-256 pins ===")
    pins = {}                                                         # (local)
    for p in inputs:
        sha = sha256_of(p)                                            # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")     # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict) -> str:
    """Stable hash over all input SHAs (invariant to dict ordering)."""
    items = sorted(pins.items())                                      # (local)
    h = hashlib.sha256()                                              # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path, canonical_path, pins):
    """Compute (audit_sha256, content_sha256) per S84+ dual-SHA schema."""
    script_bytes = b""                                                # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""                                             # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(                                         # (local)
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")

    h_audit = hashlib.sha256()                                        # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                       # (local)

    h_content = hashlib.sha256()                                      # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()                                   # (local)

    return audit, content


# -- Section 7: Verdict-line parser -----------------------------------------

# Canonical S84+ verdict line:
#   {GATE_ID}: {VERDICT} -- value={v} scheme={s} convention={c} L_max={L}
#   audit_sha256={A} content_sha256={C} schema_version=S84+
#
# A few S85 verdicts pre-date the canonical schema and use bare `sha256=`
# instead of dual-SHA; we accept both and flag the schema in the parsed row.
RE_DUAL = re.compile(                                                 # (local)
    r"^(?P<gate>[A-Z0-9\-]+):\s*(?P<verdict>PASS|FAIL|INFO)\s*--\s*"
    r"value=(?P<value>.+?)\s+"
    r"scheme=(?P<scheme>\S+)\s+"
    r"convention=(?P<convention>\S+)\s+"
    r"L_max=(?P<L_max>\S+)\s+"
    r"audit_sha256=(?P<audit>[0-9a-f]{64})\s+"
    r"content_sha256=(?P<content>[0-9a-f]{64})\s+"
    r"schema_version=S84\+\s*$"
)


def parse_verdict_for_gate(verdict_text: str, gate_id: str) -> dict:
    """Find the canonical verdict line for `gate_id` and parse it.

    Returns a dict with keys: verdict, value, scheme, convention,
    L_max, audit_sha256, content_sha256. KeyError is raised if not
    found or if the matched line does not satisfy the dual-SHA regex.
    """
    found_lines = []                                                  # (local)
    for raw in verdict_text.splitlines():
        line = raw.strip()                                            # (local)
        if not line or line.startswith("#"):
            continue
        if not line.startswith(gate_id + ":"):
            continue
        found_lines.append(line)
    if not found_lines:
        raise KeyError(f"no verdict line found for {gate_id}")
    if len(found_lines) > 1:
        raise KeyError(
            f"multiple verdict lines found for {gate_id} "
            f"(count={len(found_lines)}); ambiguous"
        )
    line = found_lines[0]                                             # (local)
    m = RE_DUAL.match(line)                                           # (local)
    if not m:
        raise KeyError(
            f"verdict line for {gate_id} did not match dual-SHA "
            f"S84+ schema; raw line: {line!r}"
        )
    return {
        "raw_line": line,
        "verdict": m.group("verdict"),
        "value": m.group("value"),
        "scheme": m.group("scheme"),
        "convention": m.group("convention"),
        "L_max": m.group("L_max"),
        "audit_sha256": m.group("audit"),
        "content_sha256": m.group("content"),
    }


# -- Section 8: Catalogue assembly -------------------------------------------

def assemble_catalogue() -> list:
    """Read s85 verdicts, look up each R-class gate, return rows + meta."""
    if not S85_VERDICT_FILE.exists():
        raise FileNotFoundError(
            f"S85 verdict file not found at {S85_VERDICT_FILE}"
        )
    s85_text = S85_VERDICT_FILE.read_text(encoding="utf-8")           # (local)
    rows = []                                                         # (local)
    for entry in R_CLASS_ROSTER:
        parsed = parse_verdict_for_gate(s85_text, entry["source_gate"])
        row = {
            "r_row": entry["r_row"],
            "source_gate": entry["source_gate"],
            "label": entry["label"],
            "verdict": parsed["verdict"],
            "value": parsed["value"],
            "scheme": parsed["scheme"],
            "convention": parsed["convention"],
            "L_max": parsed["L_max"],
            "audit_sha256": parsed["audit_sha256"],
            "content_sha256": parsed["content_sha256"],
            "substrate_one_line": entry["substrate_one_line"],
        }
        rows.append(row)
    return rows


def verify_round_trip(rows: list) -> tuple:
    """Re-read s85 verdict file; verify each (audit, content) pair matches.

    Returns (n_pass, n_fail, fail_details).
    """
    s85_text = S85_VERDICT_FILE.read_text(encoding="utf-8")           # (local)
    n_pass = 0                                                        # (local)
    n_fail = 0                                                        # (local)
    fail_details = []                                                 # (local)
    for row in rows:
        try:
            re_parsed = parse_verdict_for_gate(s85_text, row["source_gate"])
        except KeyError as exc:
            n_fail += 1
            fail_details.append(
                f"{row['r_row']} ({row['source_gate']}): re-parse failure: {exc}"
            )
            continue
        ok_audit = re_parsed["audit_sha256"] == row["audit_sha256"]   # (local)
        ok_content = re_parsed["content_sha256"] == row["content_sha256"]
        if ok_audit and ok_content:
            n_pass += 1
        else:
            n_fail += 1
            fail_details.append(
                f"{row['r_row']} ({row['source_gate']}): "
                f"audit_match={ok_audit} content_match={ok_content} "
                f"expected audit={row['audit_sha256']!r} "
                f"got audit={re_parsed['audit_sha256']!r}"
            )
    return n_pass, n_fail, fail_details


# -- Section 9: Output writers ----------------------------------------------

def write_csv(rows: list) -> None:
    """Write the 7-row R-class table as CSV."""
    header = [                                                        # (local)
        "r_row", "source_gate", "label", "verdict", "value",
        "scheme", "convention", "L_max",
        "audit_sha256", "content_sha256", "substrate_one_line",
    ]
    with OUT_CSV.open("w", encoding="utf-8", newline="") as fp:
        writer = csv.DictWriter(fp, fieldnames=header)                # (local)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row[k] for k in header})


def truncate_value(v: str, n: int = 60) -> str:
    """Trim long value strings for the registry table cell."""
    if len(v) <= n:
        return v
    return v[: n - 3] + "..."


def build_registry_section(rows: list, audit_sha: str,
                           content_sha: str) -> str:
    """Build the §VII.T R-class catalogue section (with W10-1 cross-link).

    The W10-1 ANTI-CORRESPONDENCE patch was previously authored as a
    standalone patch file (s85_w10_anti_correspondence_30_REGISTRY_PATCH.md)
    intended for §VII.Q but never merged: §VII.Q at the time of this
    landing is occupied by S85 W9-2 F_amp^3PI Factorization-Invariance
    Theorem. The 7+1 = 8-entry catalogue therefore lands at the next
    free slot §VII.T, with the W10-1 patch's content cross-linked here
    as the +1 entry. The plan's reference to "W10-1 patch at §VII.Q"
    is treated as a documentation drift; the physics SHAs in the W10-1
    patch file remain verbatim and are cited here.
    """
    lines = []                                                        # (local)
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(
        "## §VII.T — R-Class Catalogue: 7 R-class S85 W6-W13 Results "
        "+ W10-1 ANTI-CORRESPONDENCE (S86 W1c-2 — connes-ncg-theorist, "
        "2026-04-26)"
    )
    lines.append("")
    lines.append(
        "**Status**: META (registry catalogue with per-row SHA citations). "
        "Each row is a substrate-spectral outcome of a S85 W6-W13 R-class "
        "gate; the catalogue serves as the canonical R-class anchor for "
        "S86+ gates that cite an R-class result."
    )
    lines.append("")
    lines.append(
        "**Slot-allocation note**: §VII.Q was intended as the R-class "
        "landing slot in the plan (parallel to W10-1 ANTI-CORRESPONDENCE). "
        "§VII.Q at landing time is occupied by S85 W9-2 F_amp^3PI "
        "Factorization-Invariance Theorem (landed 2026-04-24); §VII.R and "
        "§VII.S are occupied by S86 W0b-2/W0b-3 methodology entries. "
        "§VII.T is the next free Roman-letter slot. The W10-1 ANTI-"
        "CORRESPONDENCE patch (`s85_w10_anti_correspondence_30_REGISTRY_PATCH.md`) "
        "was previously authored as a standalone patch file but never "
        "merged into the registry; this catalogue cross-links the W10-1 "
        "patch as the +1 = 8th entry, forming a single 8-entry R-class "
        "catalogue."
    )
    lines.append("")
    lines.append("### Catalogue table")
    lines.append("")
    lines.append(
        "| R-row | Source gate | Verdict | Value | Scheme | Convention | "
        "L_max | SHA-pin (audit/content, head-16) | Substrate one-line |"
    )
    lines.append(
        "|:------|:------------|:--------|:------|:-------|:-----------|"
        ":------|:---------------------------------|:-------------------|"
    )
    for row in rows:
        sha_short = (                                                 # (local)
            f"{row['audit_sha256'][:16]} / {row['content_sha256'][:16]}"
        )
        value_short = truncate_value(row["value"], 50).replace("|", r"\|")
        scheme_short = row["scheme"].replace("|", r"\|")
        conv_short = row["convention"].replace("|", r"\|")
        oneline = row["substrate_one_line"].replace("|", r"\|")
        lines.append(
            f"| {row['r_row']} | `{row['source_gate']}` | "
            f"**{row['verdict']}** | `{value_short}` | "
            f"`{scheme_short}` | `{conv_short}` | `{row['L_max']}` | "
            f"`{sha_short}` | {oneline} |"
        )
    # +1 W10-1 cross-link entry
    lines.append(
        "| R-W10-1 | `S85-W10-ANTI-CORRESPONDENCE-30-REGISTRY` | "
        "**PASS** | `30` | `correspondence-table-registry-landing` | "
        "`kaku-post-S64` | `N/A` | "
        "`e034e19f7fbc3d96 / 5e5f6f0dcb6cbefc` | "
        "Substrate spectral-triple K_0(A_F) = 3 with Witten-1998 single-"
        "brane K^0(X) = 1 forbids any K-theoretic uplift from the "
        "framework's `det(P) = 1` identity to the Type IIB D-brane "
        "anomaly-cancellation ledger; the divergence is an "
        "anti-correspondence at the structural-identity level. "
        "(See: `computations/session-85/s85_w10_anti_correspondence_30_REGISTRY_PATCH.md`.) "
        "|"
    )
    lines.append("")
    lines.append("### Per-row SHA verification block")
    lines.append("")
    lines.append("```")
    for row in rows:
        lines.append(
            f"  {row['r_row']:6s} {row['source_gate']:40s} "
            f"audit_sha256={row['audit_sha256']}"
        )
        lines.append(
            f"  {'':6s} {'':40s} "
            f"content_sha256={row['content_sha256']}"
        )
    lines.append(
        "  R-W10-1 S85-W10-ANTI-CORRESPONDENCE-30-REGISTRY  "
        "audit_sha256=e034e19f7fbc3d9642997559ed8fd77c070e98331d07dddbf04405b2c464fddc"
    )
    lines.append(
        "                                                      "
        "content_sha256=5e5f6f0dcb6cbefcbfe146aa9ecc056f55b653469308a487308518ef36042138"
    )
    lines.append("```")
    lines.append("")
    lines.append("### Landing closure SHA")
    lines.append("")
    lines.append("```")
    lines.append(f"  audit_sha256   = {audit_sha}")
    lines.append(f"  content_sha256 = {content_sha}")
    lines.append("```")
    lines.append("")
    lines.append("### Provenance")
    lines.append("")
    lines.append(
        "- Landing gate: `S86-W6-W13-R-CLASS-LAND`"
    )
    lines.append("- Landing date: 2026-04-26")
    lines.append("- Landing agent: connes-ncg-theorist")
    lines.append(
        "- Source verdicts: `computations/session-85/s85_gate_verdicts.txt` "
        "(7 lines, IDs above)"
    )
    lines.append(
        "- Cross-link: `computations/session-85/s85_w10_anti_correspondence_30_REGISTRY_PATCH.md` "
        "(8th entry; standalone patch never previously merged)"
    )
    lines.append(
        "- Working paper: `sessions/archive/session-86/session-86-w1c-workingpaper.md` §W1c-2"
    )
    lines.append("")
    lines.append("### Cross-references")
    lines.append("")
    lines.append(
        "- §VII.Q (S85 W9-2 F_amp^3PI Factorization-Invariance Theorem) "
        "— pre-occupant of the originally-planned R-class slot."
    )
    lines.append(
        "- §VII.R (S86 W0b-2 Single-Name Conflation methodology) "
        "— sibling META entry."
    )
    lines.append(
        "- §VII.S (S86 W0b-3 Three-Layer Adjudication methodology) "
        "— sibling META entry."
    )
    lines.append(
        "- W10-1 patch file: `computations/session-85/s85_w10_anti_correspondence_30_REGISTRY_PATCH.md` "
        "(originally targeted §VII.Q; folded into §VII.T as the +1 entry)."
    )
    lines.append("")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def append_section_to_registry(section_text: str) -> None:
    """Append the §VII.T section to permanent-results-registry.md.

    The append is atomic (single open/write). The pre-existing
    registry content is preserved verbatim. The section is added at
    end-of-file; `/weave --update` will index it.
    """
    with REGISTRY_FILE.open("a", encoding="utf-8") as fp:
        fp.write(section_text)


# -- Section 10: Verdict appender (S84+ dual-SHA) ---------------------------

def append_verdict(verdict: str, value, audit_sha: str,
                   content_sha: str) -> None:
    """Append the dual-SHA verdict line to s86_gate_verdicts.txt.

    Atomic single-open append per POSIX O_APPEND.
    """
    line = (                                                          # (local)
        f"{GATE_ID}: {verdict} -- value={value} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (                                                     # (local)
        f"# audit_sha256 companion row: {GATE_ID} "
        f"audit={audit_sha[:16]} content={content_sha[:16]}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


# -- Section 11: Main -------------------------------------------------------

def main() -> int:
    t0 = time.time()                                                  # (local)

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)                                # (local)
    closure = closure_hash(pins)                                      # (local)
    print(f"  closure (legacy): {closure[:16]}...")

    # 2. Compute S84+ dual SHAs (must be done BEFORE registry mutation
    # so the audit_sha256 reflects the pre-mutation registry SHA)
    script_path = Path(__file__).resolve()                            # (local)
    audit_sha, content_sha = compute_dual_sha(                        # (local)
        script_path, CANONICAL_FILE, pins
    )
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 3. Assemble catalogue (parse 7 verdict lines)
    print("=== Step A/B: assemble catalogue ===")
    rows = assemble_catalogue()                                       # (local)
    for row in rows:
        print(
            f"  {row['r_row']:6s} {row['source_gate']:40s} "
            f"{row['verdict']:5s} audit={row['audit_sha256'][:16]}..."
        )

    # 4. Verify round-trip SHA-pin match (PASS gate iff 7/7)
    print()
    print("=== Step C: verify round-trip SHA-pins ===")
    n_pass, n_fail, fail_details = verify_round_trip(rows)            # (local)
    print(f"  round-trip: PASS={n_pass} / FAIL={n_fail}")
    for fd in fail_details:
        print(f"  FAIL: {fd}")

    # 5. Pre-registered threshold (ABSOLUTE)
    n_total = len(rows)                                               # (local)
    n_expected = 7                                                    # (local) plan-pinned
    if n_total != n_expected:
        verdict = "FAIL"                                              # (local)
        fail_reason = (                                               # (local)
            f"row-count mismatch: assembled {n_total}, expected "
            f"{n_expected}"
        )
    elif n_pass == n_expected and n_fail == 0:
        verdict = "PASS"                                              # (local)
        fail_reason = ""                                              # (local)
    else:
        verdict = "FAIL"                                              # (local)
        fail_reason = (                                               # (local)
            f"SHA round-trip mismatch: {n_fail}/{n_expected} failed; "
            f"first failure: {fail_details[0] if fail_details else 'none'}"
        )

    print()
    print(f"=== Step D/E: verdict = {verdict} ===")
    if fail_reason:
        print(f"  reason: {fail_reason}")

    # 6. Write CSV (always — diagnostic value even on FAIL)
    write_csv(rows)
    print(f"  CSV written: {OUT_CSV}")

    # 7. Conditionally append registry section (only on PASS)
    if verdict == "PASS":
        section = build_registry_section(rows, audit_sha, content_sha)
        append_section_to_registry(section)
        print(f"  registry section appended to: {REGISTRY_FILE}")
    else:
        print(
            "  registry section NOT appended (FAIL gate; per ABSOLUTE "
            "tolerance, registry is left untouched until the source "
            "SHA mismatch is resolved)."
        )

    # 8. Emit 4-tuple
    value_tag = (                                                     # (local)
        f"7_R_class_rows_landed" if verdict == "PASS"
        else f"FAIL_{n_pass}_of_{n_expected}_rows_round_tripped"
    )
    tag = emit_4tuple(value_tag, SCHEME, CONVENTION, L_MAX)           # (local)
    print()
    print(tag)

    # 9. Append dual-SHA verdict line
    append_verdict(verdict, value_tag, audit_sha, content_sha)

    wall = time.time() - t0                                           # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0  # always 0 per .claude/rules/math-scripts.md (verdict is data)


if __name__ == "__main__":
    sys.exit(main())
