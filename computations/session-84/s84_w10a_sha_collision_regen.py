#!/usr/bin/env python3
"""
S84 W10a-110 -- SHA-COLLISION-REGEN
==================================================================
Gate: S84-SHA-COLLISION-REGEN ([AUDIT], NON-PHONONIC)

HYPOTHESIS: Three S82 verdict lines (W1-1-TD, W2-13, W3-7) that produced
duplicate SHA-256 closures (5aef2c40... triple-collision; documented in
S83-SHA-COLLISION-AUDIT, FAIL, value=1/3) can be deterministically
regenerated under the dual-SHA discipline (canonical ordered input-pin
sequence, UTF-8, no normalization shortcuts), yielding three DISTINCT
full 64-char hexdigests -- one per verdict.

PASS: All 3 regenerated SHAs are 64-char hexdigests, pairwise distinct,
      and round-trip-identical (recompute byte-for-byte on second pass).
FAIL: Any two regenerated SHAs coincide, OR any SHA shorter than 64
      chars, OR round-trip mismatch.
INFO: One or more source `s82_w{N}_*_inputs.json` files absent --
      verdict cannot be reconstructed under canonical pin-map. Mark as
      PRE-REG-INCOMPLETE (PRU Class 8); defer to W10b with explicit
      reconstruction protocol.

INPUTS (per plan §W10a-110):
  - sessions/archive/session-82/s82_gate_verdicts.txt           (recorded SHAs)
  - sessions/archive/session-82/computation-artifacts/s82_w1_1_td_inputs.json
  - sessions/archive/session-82/computation-artifacts/s82_w2_13_inputs.json
  - sessions/archive/session-82/computation-artifacts/s82_w3_7_inputs.json
  - sessions/archive/session-83/computation-artifacts/s83_g55_sha_collision_audit.json
  - computations/_shared/canonical_constants.py

4-tuple output:
  (value=<bool_all_distinct>, scheme=canonical_pin_ordering,
   convention=S84_dual_sha, L_max=N/A)

Classification: NON-PHONONIC (audit-integrity)

METHODOLOGY
-----------
The S81+ closure-SHA contract is:

    closure_sha256(v) := sha256(canonical_pin_map(v).to_utf8_bytes())

where canonical_pin_map(v) is the SORTED list of (relpath, sha256_of(file))
for every input read by the producing script of verdict v.

The S83 audit established that the S82 collision is NOT cryptographic and
NOT copy-paste: all three S82 producing scripts declared
`INPUT_FILES = [canonical_constants.py]` only, so by the closure-SHA
algorithm `sha256("canonical_constants.py=<sha>\\n")` is forced equal across
all three -- a *legitimate input-map coincidence*, not a hash anomaly.

The S84 W10a-110 fix is a SCHEMA UPGRADE: the dual-SHA discipline
introduces TWO companion hashes per verdict --
  - content_sha256 : the producing-script content hash (uniquely identifies
                     WHICH gate produced the verdict)
  - audit_sha256   : the canonical input-pin-map closure hash (auditable
                     reproduction of WHAT the script read)
The PER-VERDICT distinct content_sha256 breaks the legitimate-collision
case by design. A regen that emits both hashes for each of the three S82
verdicts proves the schema's distinctness property.

PRE-REGISTERED INFO PATH:
  The pin-map source for each verdict, per the plan, is
    sessions/archive/session-82/computation-artifacts/s82_w{N}_{slug}_inputs.json
  These files were NOT written by S82's producing scripts (the S82 schema
  did not include the inputs.json artifact). Therefore the canonical
  regeneration cannot proceed from the pre-registered source. This is a
  PRU Class 8 plan-property failure: the plan presupposed an artifact the
  preceding session did not produce.
  Per plan threshold: INFO (PRE-REG-INCOMPLETE), with reconstruction
  protocol documented in §W10-110 of the working paper.

VALUE-ADD INFORMATIONAL COMPUTATION (does not change verdict):
  The script also runs the alternative regeneration from each S82 script's
  declared INPUT_FILES, demonstrating that:
    (a) the canonical pin-map regen machinery is functional;
    (b) the audit_sha256 (input-pin closure) collision is reproduced
        byte-for-byte from independent recomputation;
    (c) under the dual-SHA schema (content_sha256 = sha256 of the
        producing script itself), the three verdicts are trivially
        distinct because the three scripts have different bytes.
  This information is recorded in the artifact JSON for downstream use
  but does NOT satisfy the pre-registered PASS criterion (canonical
  regen FROM s82_w{N}_*_inputs.json), so the verdict remains INFO.

DISCIPLINE
----------
- `from canonical_constants import *` per CLAUDE.md
- Every local/intermediate tagged `# (local)`
- CPU-only (sub-second hash computation)
- SHA-256 of all input files logged in first 20 lines of stdout
- Distinctness + round-trip tests under both schemas
- Verdict line uses dual-SHA: BOTH content_sha256 AND audit_sha256
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY per CLAUDE.md)
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
from computation_root import resolve_script, resolve_output, resolve_glob, resolve_dynamic, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===

os.environ.setdefault('OMP_NUM_THREADS', '8')     # (local) CPU cap
os.environ.setdefault('MKL_NUM_THREADS', '8')     # (local)

import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 -- Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import re
import time

# ---------------------------------------------------------------------------
# Section 3 -- Paths, IDs, scheme/convention pins
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
S82_DIR = PROJECT_ROOT / "sessions" / "session-82"
S82_ARTIFACTS_DIR = S82_DIR / "computation-artifacts"
S83_DIR = PROJECT_ROOT / "sessions" / "session-83"
S83_ARTIFACTS_DIR = S83_DIR / "computation-artifacts"
S84_ARTIFACTS_DIR = PROJECT_ROOT / "sessions" / "session-84" / "computation-artifacts"

SESSION = "S84"                                      # (local)
GATE_ID = "S84-SHA-COLLISION-REGEN"                  # (local)
SCHEME = "canonical_pin_ordering"                    # (local)
CONVENTION = "S84_dual_sha"                          # (local)
L_MAX = "N/A"                                        # (local)

# Pre-registered (per plan §W10a-110, lines 83-86):
#   PASS  : all 3 distinct, 64-char, round-trip OK
#   FAIL  : any duplicate / short / round-trip-mismatch
#   INFO  : any source s82_w{N}_*_inputs.json absent (PRE-REG-INCOMPLETE,
#                                                     PRU Class 8)

# Output artifact (per orchestrator override)
OUT_JSON = S84_ARTIFACTS_DIR / "s84_w10a_110_sha_regen.json"

# Verdict file (canonical per .claude/rules/gate-verdicts.md)
VERDICT_TXT = resolve_output(84, 's84_gate_verdicts.txt')

# S82 verdict file (per plan: in sessions/archive/session-82/, falls back to computations/)
S82_VERDICTS_PRIMARY = S82_DIR / "s82_gate_verdicts.txt"
S82_VERDICTS_FALLBACK = resolve_output(82, 's82_gate_verdicts.txt')

# The three triplet gates + their producing scripts + plan-spec inputs.json
TRIPLET = [                                          # (local)
    {
        "label": "W1-1-TD",
        "gate_id_s82": "S82-H-TILDE-EPOCH-TD",
        "script": resolve_script(82, 's82_w1_1_h_tilde_td.py'),
        "inputs_json": S82_ARTIFACTS_DIR / "s82_w1_1_td_inputs.json",
    },
    {
        "label": "W2-13",
        "gate_id_s82": "S82-F0-CONVENTION-AUDIT",
        "script": resolve_script(82, 's82_w2_13_f0_convention_audit.py'),
        "inputs_json": S82_ARTIFACTS_DIR / "s82_w2_13_inputs.json",
    },
    {
        "label": "W3-7",
        "gate_id_s82": "S82-EJ-CONVENTION-AUDIT",
        "script": resolve_script(82, 's82_w3_7_ej_convention_audit.py'),
        "inputs_json": S82_ARTIFACTS_DIR / "s82_w3_7_inputs.json",
    },
]

# This script's own INPUT_FILES (for its own closure SHA)
S83_G55_AUDIT_JSON = S83_ARTIFACTS_DIR / "s83_g55_sha_collision_audit.json"
INPUT_FILES = [                                      # (local)
    S82_VERDICTS_FALLBACK,
    resolve_script(82, 's82_w1_1_h_tilde_td.py'),
    resolve_script(82, 's82_w2_13_f0_convention_audit.py'),
    resolve_script(82, 's82_w3_7_ej_convention_audit.py'),
    resolve_script(None, 'canonical_constants.py'),
]


# ---------------------------------------------------------------------------
# Section 4 -- Canonical hash primitives (S82-replica)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string if missing/unreadable."""
    h = hashlib.sha256()                             # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def closure_hash(pins: dict) -> str:
    """Stable canonical hash over ordered input-pin map.

    Algorithm (matches S82 producing scripts byte-for-byte):
        items = sorted(pins.items())
        h = sha256()
        for k, v in items:
            h.update(f"{k}={v}\n".encode("utf-8"))
        return h.hexdigest()
    """
    items = sorted(pins.items())                     # (local)
    h = hashlib.sha256()                             # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def log_input_pins(inputs):
    """Print SHA-256 of each input; return dict {relpath: sha} for closure."""
    print(f"=== {GATE_ID} -- input SHA-256 pins (S81-hardened, dual-SHA) ===")
    pins = {}                                        # (local)
    for p in inputs:
        sha = sha256_of(p)                           # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p).replace("\\", "/")          # (local)
        present = "OK" if sha else "MISSING"          # (local)
        print(f"  [{present}] {rel}: {(sha or '----')[:16]}...")
        if sha:
            pins[rel] = sha
    return pins


# ---------------------------------------------------------------------------
# Section 5 -- Pin-map regeneration: PRIMARY (canonical-from-inputs.json)
# ---------------------------------------------------------------------------
# The pre-registered regen path:
#   pin_map_v = json.load(s82_w{N}_*_inputs.json)
#   audit_sha256 = closure_hash(pin_map_v)
# The inputs.json schema (assumed) is { rel_path : sha256_hex }.
# If a key uses "size" or full record, accept either dict-of-strings OR
# dict-of-records and reduce to {relpath: sha256}.

def load_inputs_json(path: Path):
    """Load and normalize an inputs.json file to {relpath: sha256}.

    Accepts:
      (a) {rel: sha256_hex_string}                   -- minimal
      (b) {rel: {"sha256": ..., "size": ...}}        -- structured
      (c) {"pin_map": {...}}                         -- wrapped
    Returns (dict | None, str-status).
    """
    if not path.exists():
        return None, "ABSENT"
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))   # (local)
    except (OSError, json.JSONDecodeError) as e:
        return None, f"PARSE_ERROR:{e}"
    pin_dict = raw.get("pin_map", raw) if isinstance(raw, dict) else raw  # (local)
    if not isinstance(pin_dict, dict):
        return None, "SCHEMA_ERROR:not_a_dict"
    flat = {}                                        # (local)
    for k, v in pin_dict.items():
        if isinstance(v, str):
            flat[k] = v
        elif isinstance(v, dict) and "sha256" in v:
            flat[k] = v["sha256"]
        else:
            return None, f"SCHEMA_ERROR:unrecognized_value_for_{k}"
    return flat, "LOADED"


# ---------------------------------------------------------------------------
# Section 6 -- Pin-map regeneration: SECONDARY (canonical-from-script-decl)
# ---------------------------------------------------------------------------
# Value-add informational path: parse INPUT_FILES from the producing script
# itself and recompute the canonical closure. This proves the regen machinery
# functions and reproduces the documented S82 collision byte-for-byte; it
# does NOT satisfy the pre-registered PASS criterion (which requires the
# inputs.json source).

INPUT_FILES_PATTERN = re.compile(
    r"INPUT_FILES\s*=\s*\[(.*?)\]",
    re.DOTALL,
)
ENTRY_PATTERN = re.compile(
    r'SCRIPT_DIR\s*/\s*"([^"]+)"',
)


def parse_input_files_declaration(script_path: Path):
    """Extract INPUT_FILES entries declared in a script. Returns [Path,...]."""
    try:
        text = script_path.read_text(encoding="utf-8")  # (local)
    except OSError:
        return []
    m = INPUT_FILES_PATTERN.search(text)             # (local)
    if m is None:
        return []
    body = m.group(1)                                # (local)
    names = ENTRY_PATTERN.findall(body)              # (local)
    return [resolve_dynamic(n) for n in names]


def regen_audit_sha_from_script_decl(script_path: Path):
    """Recompute canonical input-pin-map closure from script's declared list."""
    declared = parse_input_files_declaration(script_path)  # (local)
    pins = {}                                        # (local)
    for p in declared:
        sha = sha256_of(p)                           # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        pins[rel] = sha
    return closure_hash(pins), pins, declared


# ---------------------------------------------------------------------------
# Section 7 -- Recorded-SHA parser (from S82 verdict file)
# ---------------------------------------------------------------------------

def find_s82_verdicts_file() -> Path:
    """Resolve the S82 verdict file path (plan vs canonical location)."""
    if S82_VERDICTS_PRIMARY.exists():
        return S82_VERDICTS_PRIMARY
    return S82_VERDICTS_FALLBACK


def parse_recorded_sha(verdicts_path: Path, gate_id: str) -> str:
    """Extract sha256 value for a given gate ID; '' if absent."""
    try:
        text = verdicts_path.read_text(encoding="utf-8")  # (local)
    except OSError:
        return ""
    for line in text.splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        if s.startswith(gate_id + ":") or s.startswith(gate_id + " :"):
            m = re.search(r"sha256=([0-9a-f]{64})", s)    # (local)
            if m:
                return m.group(1)
    return ""


# ---------------------------------------------------------------------------
# Section 8 -- Round-trip + distinctness tests
# ---------------------------------------------------------------------------

def round_trip_test(pins_v: dict) -> tuple:
    """Recompute closure twice; return (sha1, sha2, equal_bool)."""
    sha1 = closure_hash(pins_v)                      # (local)
    sha2 = closure_hash(dict(pins_v))                # (local) fresh dict copy
    return sha1, sha2, (sha1 == sha2 and len(sha1) == 64)


# ---------------------------------------------------------------------------
# Section 9 -- Main audit logic
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()                                 # (local)

    # -- 9A. THIS script's input SHA pinning + own closure SHA --------------
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)                     # (local) audit_sha256
    own_content_sha = sha256_of(Path(__file__))      # (local) content_sha256
    print(f"  audit_sha256  : {closure}")
    print(f"  content_sha256: {own_content_sha}")
    print()
    print(f"S84 W10a-110: SHA-COLLISION-REGEN (W1-1-TD / W2-13 / W3-7 triplet)")
    print(f"  Gate            : {GATE_ID}")
    print(f"  Classification  : NON-PHONONIC (audit-integrity)")
    print(f"  Schema          : S84_dual_sha (content + audit)")
    print()

    # -- 9B. Pre-registered substitution chain (identity, not direction) ----
    print("=" * 78)
    print("STEP 1 -- SUBSTITUTION CHAIN (identity, audit-class)")
    print("=" * 78)
    print("  Definition  : closure_sha256(v) := sha256( canonical_pin_map(v).utf8 )")
    print("  Pin map     : canonical_pin_map(v) = sorted{ (relpath, sha256_of(file)) }")
    print("  Regen rule  : load pin_map from sessions/archive/session-82/computation-artifacts/")
    print("                s82_w{N}_*_inputs.json; recompute closure_sha256.")
    print("  Distinctness: PASS iff |{closure_sha256(W1-1-TD), W2-13, W3-7}| == 3")
    print("  Round-trip  : PASS iff closure_sha256(v) == closure_sha256(v) on 2nd")
    print("                independent recomputation, byte-equal, len == 64.")
    print("  INFO clause : any inputs.json absent => PRE-REG-INCOMPLETE (PRU Class 8)")
    print()

    # -- 9C. Resolve recorded SHAs (from S82 verdict file) ------------------
    s82_verdicts_path = find_s82_verdicts_file()     # (local)
    print(f"  S82 verdicts source: {s82_verdicts_path}")
    print(f"    (primary spec    : {S82_VERDICTS_PRIMARY.exists()})")
    print(f"    (canonical t0    : {S82_VERDICTS_FALLBACK.exists()})")
    print()

    # -- 9D. Per-verdict regen attempt --------------------------------------
    print("=" * 78)
    print("STEP 2 -- Per-verdict canonical regen from inputs.json (PRE-REGISTERED)")
    print("=" * 78)

    records = []                                     # (local)
    inputs_json_status = {}                          # (local) label -> status
    primary_path_used = True                         # (local)

    for item in TRIPLET:
        label = item["label"]
        gate_s82 = item["gate_id_s82"]
        script = item["script"]
        inputs_json_path = item["inputs_json"]

        recorded_sha = parse_recorded_sha(s82_verdicts_path, gate_s82)  # (local)

        # --- PRIMARY REGEN: from s82_w{N}_*_inputs.json ---
        pin_map_primary, status_primary = load_inputs_json(inputs_json_path)
        inputs_json_status[label] = status_primary

        if pin_map_primary is not None:
            audit_sha_primary = closure_hash(pin_map_primary)  # (local)
            rt_a, rt_b, rt_ok = round_trip_test(pin_map_primary)
        else:
            audit_sha_primary = ""
            rt_a, rt_b, rt_ok = "", "", False
            primary_path_used = False

        # --- SECONDARY REGEN: from script's declared INPUT_FILES (info only) ---
        audit_sha_secondary, secondary_pins, declared_paths = (
            regen_audit_sha_from_script_decl(script)
        )
        rt2_a, rt2_b, rt2_ok = round_trip_test(secondary_pins)

        # --- Per-script content_sha256 (uniquely identifies producing gate) ---
        content_sha = sha256_of(script)              # (local)

        records.append({
            "label": label,
            "gate_s82": gate_s82,
            "script": str(script.relative_to(PROJECT_ROOT)).replace("\\", "/"),
            "inputs_json_path": str(
                inputs_json_path.relative_to(PROJECT_ROOT)
            ).replace("\\", "/"),
            "inputs_json_status": status_primary,
            "recorded_audit_sha256": recorded_sha,
            # Primary (canonical, pre-registered) regen:
            "primary_audit_sha256": audit_sha_primary,
            "primary_pin_map": pin_map_primary or {},
            "primary_round_trip_ok": rt_ok,
            "primary_round_trip_pair": [rt_a, rt_b],
            # Secondary (informational) regen:
            "secondary_audit_sha256": audit_sha_secondary,
            "secondary_pin_map": secondary_pins,
            "secondary_declared_input_files": [
                str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
                for p in declared_paths
            ],
            "secondary_round_trip_ok": rt2_ok,
            "secondary_round_trip_pair": [rt2_a, rt2_b],
            # Dual-SHA content hash:
            "content_sha256_of_producing_script": content_sha,
        })

        print(f"  [{label}] gate = {gate_s82}")
        print(f"    script              = {script.name}")
        print(f"    inputs.json path    = {inputs_json_path.name}")
        print(f"    inputs.json status  = {status_primary}")
        print(f"    recorded audit_sha  = {recorded_sha}")
        print(f"    PRIMARY regen sha   = {audit_sha_primary or '(SKIPPED -- absent)'}")
        print(f"    PRIMARY round-trip  = {rt_ok}")
        print(f"    SECONDARY regen sha = {audit_sha_secondary}")
        print(f"    SECONDARY rt        = {rt2_ok}")
        print(f"    content_sha256      = {content_sha}")
        print()

    # -- 9E. Distinctness tests ---------------------------------------------
    print("=" * 78)
    print("STEP 3 -- Distinctness analysis")
    print("=" * 78)

    primary_shas = [r["primary_audit_sha256"] for r in records]      # (local)
    secondary_shas = [r["secondary_audit_sha256"] for r in records]  # (local)
    content_shas = [r["content_sha256_of_producing_script"]
                    for r in records]                                 # (local)
    recorded_shas = [r["recorded_audit_sha256"] for r in records]    # (local)

    # Filter empty strings (from absent files) for distinctness:
    primary_nonempty = [s for s in primary_shas if s]                # (local)
    primary_all_64 = all(len(s) == 64 for s in primary_nonempty)     # (local)
    primary_distinct_ct = len(set(primary_nonempty))                 # (local)
    primary_all_distinct = (
        len(primary_nonempty) == 3 and primary_distinct_ct == 3
    )                                                                 # (local)
    primary_all_round_trip = all(r["primary_round_trip_ok"] for r in records)

    secondary_distinct_ct = len(set(secondary_shas))                 # (local)
    secondary_all_distinct = (secondary_distinct_ct == 3)            # (local)
    secondary_all_round_trip = all(r["secondary_round_trip_ok"]
                                    for r in records)
    secondary_all_64 = all(len(s) == 64 for s in secondary_shas)     # (local)

    content_distinct_ct = len(set(content_shas))                     # (local)
    content_all_distinct = (content_distinct_ct == 3)                # (local)
    content_all_64 = all(len(s) == 64 for s in content_shas)         # (local)

    recorded_distinct_ct = len(set(recorded_shas))                   # (local)

    print(f"  PRIMARY (from inputs.json):")
    print(f"    recovered SHAs : {len(primary_nonempty)}/3")
    print(f"    distinct       : {primary_distinct_ct}/3")
    print(f"    all 64-char    : {primary_all_64}")
    print(f"    all round-trip : {primary_all_round_trip}")
    print(f"    all_distinct   : {primary_all_distinct}")
    print(f"  SECONDARY (from script's INPUT_FILES decl):")
    print(f"    distinct       : {secondary_distinct_ct}/3")
    print(f"    all 64-char    : {secondary_all_64}")
    print(f"    all round-trip : {secondary_all_round_trip}")
    print(f"    all_distinct   : {secondary_all_distinct}")
    print(f"  CONTENT-SHA (per-script, dual-SHA component):")
    print(f"    distinct       : {content_distinct_ct}/3")
    print(f"    all 64-char    : {content_all_64}")
    print(f"    all_distinct   : {content_all_distinct}")
    print(f"  RECORDED (S82 verdict file):")
    print(f"    distinct       : {recorded_distinct_ct}/3 (1/3 expected per S83 audit)")
    print()

    # -- 9F. Verdict decision (PRE-REGISTERED THRESHOLDS, plan §W10a-110) --
    print("=" * 78)
    print("STEP 4 -- Verdict decision (pre-registered, identity-only)")
    print("=" * 78)

    # PRE-REG INFO check FIRST (precedes PASS/FAIL):
    any_inputs_absent = any(s != "LOADED" for s in inputs_json_status.values())
    if any_inputs_absent:
        verdict = "INFO"                             # (local)
        reason = (
            "PRE-REG-INCOMPLETE (PRU Class 8): one or more "
            "s82_w{N}_*_inputs.json source artifacts absent. The S82 producing "
            "scripts did not write the inputs.json schema this gate "
            "presupposes. Canonical regen FROM inputs.json cannot proceed; "
            "deferred to W10b with reconstruction protocol below."
        )
        # value bool is the all_distinct outcome that COULD have been computed;
        # we report False since primary regen did not complete for all 3.
        value_bool = False                           # (local)
    else:
        # Both regen sources present; apply PASS/FAIL on PRIMARY.
        if not primary_all_64:
            verdict = "FAIL"                         # (local)
            reason = "PRIMARY regen produced a sub-64-char hexdigest"
            value_bool = False
        elif not primary_all_round_trip:
            verdict = "FAIL"                         # (local)
            reason = "PRIMARY round-trip mismatch (non-deterministic hash)"
            value_bool = False
        elif not primary_all_distinct:
            verdict = "FAIL"                         # (local)
            reason = (
                "PRIMARY canonical regen yielded duplicate audit_sha256; "
                "schema does not break the S82 collision"
            )
            value_bool = False
        else:
            verdict = "PASS"                         # (local)
            reason = (
                "all 3 PRIMARY audit_sha256 are 64-char, distinct, "
                "and round-trip identical"
            )
            value_bool = True

    print(f"  inputs.json statuses    : {inputs_json_status}")
    print(f"  any_inputs_absent       : {any_inputs_absent}")
    print(f"  primary_all_distinct    : {primary_all_distinct}")
    print(f"  primary_all_64          : {primary_all_64}")
    print(f"  primary_all_round_trip  : {primary_all_round_trip}")
    print(f"  VERDICT                 : {verdict}")
    print(f"  REASON                  : {reason}")
    print()

    # -- 9G. Reconstruction protocol (only meaningful when verdict == INFO) --
    reconstruction_protocol = [
        "STEP A: For each S82 producing script (w1_1, w2_13, w3_7):",
        "        re-run with an instrumented wrapper that emits",
        "        sessions/archive/session-82/computation-artifacts/s82_w{N}_{slug}_inputs.json",
        "        with schema { rel_path : sha256_hex } for every file read",
        "        (including transitively-imported modules detected via importlib).",
        "STEP B: Re-dispatch S84-SHA-COLLISION-REGEN with the new artifacts.",
        "        Under dual-SHA schema, content_sha256 is per-script and is",
        "        already distinct (proven this run); the audit_sha256 should",
        "        also become distinct iff the inputs.json captures more than",
        "        canonical_constants.py (e.g., the producing script itself,",
        "        its transitively-imported modules, or a per-gate scheme tag).",
        "STEP C: If after STEP A the audit_sha256 are STILL identical, the",
        "        inputs.json schema must be extended to include the producing-",
        "        script's own SHA as a pinned input. This is the documented",
        "        S83 recommendation ('pin producing-script SHA into INPUT_FILES",
        "        so single-input audits differentiate by script').",
    ]

    # -- 9H. Save artifact JSON --------------------------------------------
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    artifact = {
        "session": SESSION,
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "verdict": verdict,
        "reason": reason,
        "value_bool_all_distinct": value_bool,
        "schema_version": "S84+",
        "dual_sha": {
            "content_sha256": own_content_sha,
            "audit_sha256": closure,
        },
        "inputs_json_status": inputs_json_status,
        "any_inputs_absent": any_inputs_absent,
        "primary_regen": {
            "source": "sessions/archive/session-82/computation-artifacts/s82_w{N}_*_inputs.json",
            "all_distinct": primary_all_distinct,
            "all_64_char": primary_all_64,
            "all_round_trip_ok": primary_all_round_trip,
            "shas": primary_shas,
            "distinct_count": primary_distinct_ct,
        },
        "secondary_regen_informational": {
            "source": "INPUT_FILES declaration parsed from each producing script",
            "all_distinct": secondary_all_distinct,
            "all_64_char": secondary_all_64,
            "all_round_trip_ok": secondary_all_round_trip,
            "shas": secondary_shas,
            "distinct_count": secondary_distinct_ct,
            "interpretation": (
                "Reproduces S82 collision byte-for-byte; confirms the "
                "collision is a legitimate input-map coincidence (all 3 "
                "scripts declare INPUT_FILES = [canonical_constants.py]) "
                "and not a copy-paste or cryptographic anomaly."
            ),
        },
        "content_sha_dual_component": {
            "source": "sha256 of each producing script's bytes",
            "all_distinct": content_all_distinct,
            "all_64_char": content_all_64,
            "shas": content_shas,
            "interpretation": (
                "The dual-SHA schema's content_sha256 component is "
                "trivially distinct because the three producing scripts "
                "have different bytes. This proves dual-SHA breaks the "
                "single-input-collision pathology by construction."
            ),
        },
        "recorded_s82_shas": {
            "source": str(s82_verdicts_path.relative_to(PROJECT_ROOT)).replace(
                "\\", "/"
            ),
            "shas": recorded_shas,
            "distinct_count": recorded_distinct_ct,
        },
        "per_verdict_records": [
            {
                "label": r["label"],
                "gate_s82": r["gate_s82"],
                "script": r["script"],
                "inputs_json_path": r["inputs_json_path"],
                "inputs_json_status": r["inputs_json_status"],
                "recorded_audit_sha256": r["recorded_audit_sha256"],
                "primary_audit_sha256": r["primary_audit_sha256"],
                "primary_pin_map": r["primary_pin_map"],
                "primary_round_trip_ok": r["primary_round_trip_ok"],
                "secondary_audit_sha256": r["secondary_audit_sha256"],
                "secondary_pin_map": r["secondary_pin_map"],
                "secondary_declared_input_files": r["secondary_declared_input_files"],
                "secondary_round_trip_ok": r["secondary_round_trip_ok"],
                "content_sha256_of_producing_script":
                    r["content_sha256_of_producing_script"],
            }
            for r in records
        ],
        "reconstruction_protocol_for_W10b": reconstruction_protocol,
        "input_files_for_this_audit": [
            str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
            for p in INPUT_FILES
        ],
        "wall_time_s": None,  # filled below
    }

    # -- 9I. 4-tuple + dual-SHA verdict line --------------------------------
    four_tuple = (
        f"(value={value_bool}, scheme={SCHEME}, "
        f"convention={CONVENTION}, L_max={L_MAX})"
    )
    print(f"4-tuple: {four_tuple}")

    verdict_line = (
        f"{GATE_ID}: {verdict} -- "
        f"value={value_bool} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={closure} content_sha256={own_content_sha}\n"
    )
    companion_line = (
        f"# {GATE_ID} dual-SHA: "
        f"content_sha256={own_content_sha} audit_sha256={closure}\n"
    )

    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(verdict_line)
        fp.write(companion_line)

    wall = time.time() - t0                          # (local)
    artifact["wall_time_s"] = wall

    OUT_JSON.write_text(json.dumps(artifact, indent=2), encoding="utf-8")

    # -- 9J. Diagnostic summary ---------------------------------------------
    print()
    print("=" * 78)
    print("OUTPUTS SAVED")
    print("=" * 78)
    print(f"  Script   : {__file__}")
    print(f"  Artifact : {OUT_JSON}")
    print(f"  Verdict  : appended to {VERDICT_TXT}")
    print()
    print("VERDICT LINE (appended):")
    print(f"  {verdict_line.strip()}")
    print(f"  {companion_line.strip()}")
    print()
    print(f"=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
