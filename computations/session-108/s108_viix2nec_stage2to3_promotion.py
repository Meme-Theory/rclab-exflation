#!/usr/bin/env python3
"""
S108 W2-4 S108-VIIX2NEC-STAGE2to3-PROMOTION — §VII.X.2-NECESSITY Stage-2→Stage-3 Promotion
=========================================================================================

Gate: S108-VIIX2NEC-STAGE2to3-PROMOTION ([VERIFY-THEOREM])

Pre-registered threshold (plan §W2-4 operator.form):
  PASS iff  (n_anchor_shas_full_64_char_on_disk == 6)
        AND (S107 Stage-2 structural-PASS-AND record present: S107-VIIX2NEC-STAGE2-VERIFY
             audit 4d98f916... in s107 verdict file)
        AND (entry-text anchor-availability diagnostic reconciled "2 of 6" -> "6 of 6 emitted")
        AND (Status tag flipped STAGE-1-CANDIDATE -> STAGE-3-PERMANENT on 4 surfaces)
        AND (re_read + verify_section_matches == True for all 4 surfaces)
  INFO (pre-registered intermediate): 6/6 SHAs present BUT the registered six-anchor TABLE and the
       S88-script enumeration name DIFFERENT 6-anchor sets (S88 counts the S87 aggregation gate
       fa225aac... as anchor 6; the registered table names S82 MP-Exclusion 98267d63... as anchor-5).
       The harvest succeeds under EITHER reading (all named SHAs are on disk); promotion fires; the
       INFO records the enumeration reconciliation + the canonical 6-anchor set adopted.
  FAIL iff <6/6 anchor SHAs verify full-64-char on disk (harvest IS the gate; promotion deferred).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-88/s88_gate_verdicts.txt   (anchors 1-5: S88-LAMBDA-SA-* family)
  - computations/session-87/s87_gate_verdicts.txt   (anchor 6: S87-M2-STRUCTURAL-SOURCE-...-LANDING)
  - computations/session-82/s82_gate_verdicts.txt   (registered-table anchor-5: S82 MP-Exclusion)
  - computations/session-84/s84_gate_verdicts.txt   (registered-table anchor-4: S77 successor 5baaa51c)
  - computations/session-107/s107_gate_verdicts.txt (Stage-2 record 4d98f916...)
  - sessions/permanent-results-registry.md          (§VII.X.2-NECESSITY block; surface 1)
  - sessions/framework/Atlas/atlas-04-assumptions.md (§X K9; surface 2)
  - sessions/framework/Atlas/atlas-07-permanent-results.md (§VII.X.2-NECESSITY row; surface 3)
  - sessions/framework/registry/open-channel-ledger.md (§C K9; surface 4)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<n_anchors>, scheme=joint-theorem-promotion-4-stage,
   convention=6-of-6-SHA-harvest + 4-surface-flip, L_max=10)

Classification: GEOMETRIC (substrate-IS NCG-axiomatic meta-theorem; orchestrator-direct registry landing)

METHODOLOGY
-----------
Registry-landing-class SHA-harvest + 4-surface tag-flip via the bridge-landing single-shot
AFTER-pattern (registry-landing.md §"Bridge-Landing Script Architecture"):
  build_promotion_text -> write_atomic_with_fsync -> re_read + verify_section_matches -> emit ONE verdict.
NO physics re-derivation: the M2 ==> Lambda_SA-finite-L-residual necessity direction is the entry's OWN
registered statement (registry line ~16536) and was blind-cross-axis PASS-AND'd at S107 (JOINT-1 + JOINT-2,
both axes; audit 4d98f916). This gate VERIFIES the registry-PASS criterion (6/6 full-64-char anchor-SHA
harvest) and flips the tag. The 6/6 count is a presence check, not a magnitude/direction claim, so no
substitution chain is required (plan §W2-4 substitution_chain.required=false).

The harvest reconciles two valid 6-anchor readings (the pre-registered INFO branch):
  S88-script-enumeration:  {S46, S64, S65, S77, C9}-SUCCESSOR/WITNESS (s88) + S87 aggregation (s87 fa225aac)
  registered-TABLE:        {S46, S64, S65}-via-S88-successors + S77 (s84 5baaa51c) + S82-MP-Exclusion
                           (s82 98267d63) + C9 (s88)
Both readings harvest 6 full-64-char SHAs on disk; the canonical set adopted = the S88-script enumeration
(the entry's registry-PASS criterion targets the S88-LAMBDA-SA-* successor family per the S107 verdict's
S108_fwd_gate field + the registry blockquote VERIFY-BEFORE-PROMOTION NOTE), with the registered-table
S77/S82 SHAs recorded as the alternate-reading anchors (both on disk).

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- No GPU (SHA-grep + text edits; matrices N/A)
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- Gate verdict emitted via the `emit_verdict` knowledge-MCP tool (race-safe): the script PRINTS the
  payload (`print_verdict_payload`); the dispatching AGENT calls mcp__knowledge__emit_verdict.
- Bridge-landing single-shot AFTER-pattern: ONE verify_section_matches boolean determines the verdict;
  NO conditional rewrite on intermediate FAIL (the BEFORE pattern is FORBIDDEN, registry-landing.md).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys as _sys
from pathlib import Path as _Path

# canonical_constants.py lives in computations/_shared/; add to path then import *
_SHARED = _Path(__file__).resolve().parent.parent / "_shared"  # (local)
if str(_SHARED) not in _sys.path:
    _sys.path.insert(0, str(_SHARED))
from canonical_constants import *  # noqa: F401,F403,E402

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402
import re  # noqa: E402
import sys  # noqa: E402
import time  # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np  # noqa: E402  (npz storage of harvested SHAs + flip booleans)

# Optional plot (gate verdict does not require it)
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt  # (local)
    _HAVE_MPL = True  # (local)
except Exception:  # pragma: no cover
    _HAVE_MPL = False  # (local)

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S108"                                                  # (local)
GATE_ID = "S108-VIIX2NEC-STAGE2to3-PROMOTION"                     # (local)
SCHEME = "joint-theorem-promotion-4-stage"                       # (local)
CONVENTION = ("stage-2-structural-PASS-AND-record-4d98f916 + "
              "6-of-6-anchor-SHA-harvest + 4-surface-tag-flip")  # (local)
L_MAX = 10                                                        # (local)

PASS_THRESHOLD = 6                                                # (local) n_anchor SHAs full-64-char
N_EVAL = 6                                                        # (local)

# --- anchor / record SHA targets (full-64-char) ----------------------------
# S107 Stage-2 structural-PASS-AND record (the blind cross-axis verify; necessity clauses PASS-AND).
S107_STAGE2_GATE = "S107-VIIX2NEC-STAGE2-VERIFY"                  # (local)

# CANONICAL 6-anchor set adopted = S88-script enumeration (anchors 1-5) + S87 aggregation (anchor 6).
# Each tuple: (anchor_label, gate_id_regex_prefix, verdict_file_relpath)
CANONICAL_ANCHORS = [                                            # (local)
    ("anchor_1_S46_a2_split",
     r"^S88-LAMBDA-SA-S46-A2-SPLIT-SUCCESSOR-EMISSION:",
     "computations/session-88/s88_gate_verdicts.txt"),
    ("anchor_2_S64_finite_L",
     r"^S88-LAMBDA-SA-S64-FINITE-L-COMPONENT-SUCCESSOR-EMISSION:",
     "computations/session-88/s88_gate_verdicts.txt"),
    ("anchor_3_S65_continuum_converse_witness",
     r"^S88-LAMBDA-SA-S65-CONTINUUM-CONVERSE-WITNESS-EMISSION:",
     "computations/session-88/s88_gate_verdicts.txt"),
    ("anchor_4_S77_a0_R_protection",
     r"^S88-LAMBDA-SA-S77-A0-R-PROTECTION-SUCCESSOR-EMISSION:",
     "computations/session-88/s88_gate_verdicts.txt"),
    ("anchor_5_C9_S86_W1_ratio",
     r"^S88-LAMBDA-SA-C9-S86-W1-RATIO-EMISSION:",
     "computations/session-88/s88_gate_verdicts.txt"),
    ("anchor_6_S87_M2_aggregation",
     r"^S87-M2-STRUCTURAL-SOURCE-FOR-LAMBDA-SA-FINITE-L-RESIDUAL-LANDING:",
     "computations/session-87/s87_gate_verdicts.txt"),
]

# ALTERNATE-reading anchors (registered six-anchor TABLE): anchor-4 = S77 successor 5baaa51c (s84),
# anchor-5 = S82 MP-Exclusion 98267d63 (s82). Harvested as cross-check that BOTH readings reach 6/6.
ALT_TABLE_ANCHORS = [                                            # (local)
    ("alt_anchor4_S77_5baaa51c",
     "5baaa51ca58174cb009757641c42e297efd07096a6f942836205d3e591e4622f",
     "computations/session-84/s84_gate_verdicts.txt"),
    ("alt_anchor5_S82_MP_Exclusion_98267d63",
     "98267d631c9f7a2c57f68e5feb767284a211f1987bc1e7fd412f2cfdfbf693c0",
     "computations/session-82/s82_gate_verdicts.txt"),
]

# --- editable-surface paths -------------------------------------------------
REGISTRY = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"          # (local)
ATLAS04 = PROJECT_ROOT / "sessions" / "framework" / "Atlas" / "atlas-04-assumptions.md"  # (local)
ATLAS07 = PROJECT_ROOT / "sessions" / "framework" / "Atlas" / "atlas-07-permanent-results.md"  # (local)
OCL = PROJECT_ROOT / "sessions" / "framework" / "registry" / "open-channel-ledger.md"  # (local)

OUT_NPZ = SESSION_DIR / "s108_viix2nec_stage2to3_promotion.npz"
OUT_PNG = SESSION_DIR / "s108_viix2nec_stage2to3_promotion.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    COMPUTATIONS_DIR / "session-88" / "s88_gate_verdicts.txt",
    COMPUTATIONS_DIR / "session-87" / "s87_gate_verdicts.txt",
    COMPUTATIONS_DIR / "session-82" / "s82_gate_verdicts.txt",
    COMPUTATIONS_DIR / "session-84" / "s84_gate_verdicts.txt",
    COMPUTATIONS_DIR / "session-107" / "s107_gate_verdicts.txt",
    REGISTRY,
    ATLAS04,
    ATLAS07,
    OCL,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
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
    """Stable hash over all input SHAs (invariant to dict ordering)."""
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    """(audit_sha256, content_sha256) per the S84+ dual-SHA schema.

    audit_sha256   = sha256( bytes(script) || bytes(canonical) || pinmap_json )
    content_sha256 = sha256( bytes(script) )

    The pinmap embeds per-gate identity (gate_id) + the §VII.X.2-NECESSITY block + the
    S88/S87/S107 anchor lines, so audit_sha256 is per-gate-distinct by construction
    (mechanical-closure-discipline.md item 3; sig_5 uniqueness).
    """
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
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
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
# Section 4b — SHA harvest helpers
# ---------------------------------------------------------------------------

_AUDIT_RE = re.compile(r"audit_sha256=([0-9a-f]{64})")  # (local)


def grep_canonical_audit_sha(verdict_file: Path, gate_prefix_regex: str) -> str | None:
    """Find the canonical line matching gate_prefix_regex and extract its full-64-char audit_sha256.

    Returns the 64-hex SHA, or None if the gate line or a full-64-char SHA is absent.
    """
    pat = re.compile(gate_prefix_regex)  # (local)
    try:
        text = verdict_file.read_text(encoding="utf-8", errors="replace")  # (local)
    except OSError:
        return None
    for line in text.splitlines():
        if line.startswith("#"):
            continue  # skip companion/comment rows
        if pat.search(line):
            m = _AUDIT_RE.search(line)  # (local)
            if m:
                return m.group(1)
    return None


def grep_sha_present(verdict_file: Path, sha_full64: str) -> bool:
    """True iff the literal full-64-char SHA appears anywhere in the verdict file."""
    try:
        text = verdict_file.read_text(encoding="utf-8", errors="replace")  # (local)
    except OSError:
        return False
    return sha_full64 in text


# ---------------------------------------------------------------------------
# Section 4c — Bridge-landing single-shot AFTER-pattern helpers
# ---------------------------------------------------------------------------

def write_atomic_with_fsync(path: Path, new_text: str) -> None:
    """Atomic write with fsync: write to a temp sibling, fsync, os.replace.

    os.replace is atomic on Windows + POSIX; fsync forces the bytes to disk before the
    rename so a crash mid-write cannot leave a partial file at the canonical path.
    """
    tmp = path.with_suffix(path.suffix + ".tmp")  # (local)
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        f.write(new_text)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)


def verify_section_matches(path: Path, expected_substring: str,
                           forbidden_substring: str | None = None) -> bool:
    """Re-read `path` from disk; True iff expected_substring is present AND
    (forbidden_substring is None OR absent). This is the FINAL verification step
    whose boolean determines the verdict (single-shot AFTER-pattern)."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")  # (local)
    except OSError:
        return False
    ok = expected_substring in text  # (local)
    if forbidden_substring is not None:
        ok = ok and (forbidden_substring not in text)
    return ok


def build_promotion_text(original: str, edits: list[tuple[str, str]]) -> str:
    """Apply an ordered list of (old, new) exact-substring replacements to `original`,
    fully in memory (no I/O). Each `old` MUST be present and unique; raises if not.

    Idempotent: if `old` is absent BUT `new` is already present (a prior run landed it),
    the edit is treated as already-applied (NO-OP for that pair). The function returns the
    fully-edited text; the caller writes it once and re-reads to verify."""
    text = original  # (local)
    for old, new in edits:
        if old in text:
            if text.count(old) != 1:
                raise ValueError(f"non-unique old_string (count={text.count(old)}): {old[:80]!r}")
            text = text.replace(old, new, 1)
        elif new in text:
            # already applied (idempotent re-run); skip
            continue
        else:
            raise ValueError(f"old_string ABSENT and new_string ABSENT (drift?): {old[:80]!r}")
    return text


# ---------------------------------------------------------------------------
# Section 5 — Surface edit definitions (exact old -> new substring pairs)
# ---------------------------------------------------------------------------

def surface_edits(canonical_shas: dict[str, str],
                  alt_shas: dict[str, str]) -> dict[str, dict]:
    """Return {surface_name: {path, edits:[(old,new)], expect:str, forbid:str|None}}.

    All 4 surfaces flip STAGE-1-CANDIDATE -> STAGE-3-PERMANENT for §VII.X.2-NECESSITY (K9),
    and the registry additionally reconciles the six-anchor table + the "2 of 6" diagnostic.
    """
    a1 = canonical_shas["anchor_1_S46_a2_split"]               # (local)
    a2 = canonical_shas["anchor_2_S64_finite_L"]               # (local)
    a3 = canonical_shas["anchor_3_S65_continuum_converse_witness"]  # (local)
    a4 = canonical_shas["anchor_4_S77_a0_R_protection"]        # (local)
    a5 = canonical_shas["anchor_5_C9_S86_W1_ratio"]            # (local)
    a6 = canonical_shas["anchor_6_S87_M2_aggregation"]         # (local)
    alt4 = alt_shas["alt_anchor4_S77_5baaa51c"]                # (local)
    alt5 = alt_shas["alt_anchor5_S82_MP_Exclusion_98267d63"]   # (local)

    edits: dict[str, dict] = {}

    # ---- Surface 1: registry §VII.X.2-NECESSITY (Status + anchor table + diagnostic) ----
    reg_edits: list[tuple[str, str]] = []  # (local)

    # 1a. Status line -> STAGE-3-PERMANENT
    reg_edits.append((
        "**Status**: STAGE-1-CANDIDATE (necessity-only meta-theorem; STRUCTURAL-DIAGNOSTIC at S87 due to upstream anchor-availability defect)",
        "**Status**: STAGE-3-PERMANENT (necessity-only meta-theorem; promoted S108 W2-4 via the joint-theorem-promotion 4-stage pathway — the S107 W2-3 blind two-agent cross-axis Stage-2 PASS-AND on EVERY clause [`S107-VIIX2NEC-STAGE2-VERIFY` INFO PASS-ON-STRUCTURE, audit 4d98f9161352e567ffc6cb211519d366f769f2d155fa9cd0e3977a7d269b5e9e] + the S108 W2-4 6-of-6 full-64-char anchor-SHA harvest VERIFIED on disk [`S108-VIIX2NEC-STAGE2to3-PROMOTION`]. The S87-era STRUCTURAL-DIAGNOSTIC anchor-availability defect is RESOLVED: the S88-LAMBDA-SA-* successor-emission family landed all 5 previously-absent anchors + the S87 aggregation gate = 6/6 on disk.)",
    ))

    # 1b. Anchor table rows 1,2,3,6 (absent -> SHA); row 4 (S77 5baaa51c alt) -> S88-successor SHA
    #     (canonical set adopted = S88 enumeration); row 5 (S82 98267d63) kept + cross-linked.
    reg_edits.append((
        "| 1 | S46 a_2 split | a_2 (s=1) | TRUE | TRUE | VALID-pre-S52-archive | TRUE | (absent — SOURCE-RECON Class-(c)) |",
        f"| 1 | S46 a_2 split | a_2 (s=1) | TRUE | TRUE | VALID-pre-S52-archive | TRUE | {a1} (S88-LAMBDA-SA-S46-A2-SPLIT-SUCCESSOR-EMISSION, s88) |",
    ))
    reg_edits.append((
        "| 2 | S64 finite-L Λ_SA + a_0 paired split | a_0 (s=0) | TRUE | TRUE | VALID-pre-S52-archive | TRUE | (absent — SOURCE-RECON Class-(c)) |",
        f"| 2 | S64 finite-L Λ_SA + a_0 paired split | a_0 (s=0) | TRUE | TRUE | VALID-pre-S52-archive | TRUE | {a2} (S88-LAMBDA-SA-S64-FINITE-L-COMPONENT-SUCCESSOR-EMISSION, s88) |",
    ))
    reg_edits.append((
        "| 3 | S65 a_0/a_2 = C/R universal | a_0 + a_2 (continuum) | TRUE | FALSE | VALID-continuum-limit | TRUE (CONVERSE-FAILURE WITNESS) | (absent — SOURCE-RECON Class-(c)) |",
        f"| 3 | S65 a_0/a_2 = C/R universal | a_0 + a_2 (continuum) | TRUE | FALSE | VALID-continuum-limit | TRUE (CONVERSE-FAILURE WITNESS) | {a3} (S88-LAMBDA-SA-S65-CONTINUUM-CONVERSE-WITNESS-EMISSION, s88) |",
    ))
    reg_edits.append((
        "| 4 | S77 a_0 R-protection-universal failure | a_0 (s=0) | TRUE | TRUE | VALID-S77-S86-confirmed | TRUE | 5baaa51ca58174cb009757641c42e297efd07096a6f942836205d3e591e4622f |",
        f"| 4 | S77 a_0 R-protection-universal failure | a_0 (s=0) | TRUE | TRUE | VALID-S77-S86-confirmed | TRUE | {a4} (S88-LAMBDA-SA-S77-A0-R-PROTECTION-SUCCESSOR-EMISSION, s88; alternate-reading registered-table SHA {alt4} = S84-R-PROTECTED-ATLAS-COMPLETENESS partial-match, s84 — BOTH on disk) |",
    ))
    reg_edits.append((
        "| 5 | S82 W2-5 MP-Exclusion | All slots (regulator-class) | TRUE | TRUE | VALID-S82-canonical | TRUE | 98267d631c9f7a2c57f68e5feb767284a211f1987bc1e7fd412f2cfdfbf693c0 |",
        f"| 5 | S82 W2-5 MP-Exclusion | All slots (regulator-class) | TRUE | TRUE | VALID-S82-canonical | TRUE | {alt5} (S82-HEAT-KERNEL-MP-EXCLUSION, s82 — registered-table anchor-5; the S88-script canonical enumeration substitutes C9 here and counts S87 aggregation {a6} as anchor 6) |",
    ))
    reg_edits.append((
        "| 6 | C9 (S86 W-1) 9.46x a_0/Λ_CC ratio | a_0 (s=0) | TRUE | TRUE | VALID-S86-workshop-only | TRUE | (absent — SOURCE-RECON Class-(c)) |",
        f"| 6 | C9 (S86 W-1) 9.46x a_0/Λ_CC ratio | a_0 (s=0) | TRUE | TRUE | VALID-S86-workshop-only | TRUE | {a5} (S88-LAMBDA-SA-C9-S86-W1-RATIO-EMISSION, s88; S87 aggregation gate {a6} is the S88-script anchor-6) |",
    ))

    # 1c. Anchor-availability diagnostic header "2 of 6" -> "6 of 6 emitted"
    reg_edits.append((
        "**Anchor-availability diagnostic**: Of the 6 anchors, **2** have full-64-char audit_sha256 in computations/s{52..85}_gate_verdicts.txt:",
        "**Anchor-availability diagnostic** (RECONCILED S108 W2-4 — `S108-VIIX2NEC-STAGE2to3-PROMOTION`): **6 of 6 emitted** — all 6 anchors now have a full-64-char audit_sha256 on disk. The S87-era \"2 of 6\" state was a pre-S88 diagnostic; the S88-LAMBDA-SA-* successor-emission family (S88 plan §W11-128..132) re-emitted the 5 previously-absent anchors (S46/S64/S65/S77/C9) as computation verdict lines, and the S87 aggregation gate supplies the 6th. (Original S87-era diagnostic, retained for audit trail:) Of the 6 anchors, **2** had full-64-char audit_sha256 in computations/s{52..85}_gate_verdicts.txt at S87:",
    ))

    edits["registry_VII_X_2_NECESSITY"] = {
        "path": REGISTRY,
        "edits": reg_edits,
        "expect": "**Status**: STAGE-3-PERMANENT (necessity-only meta-theorem; promoted S108 W2-4",
        "forbid": None,  # the S107 blockquote legitimately retains "STAYS STAGE-1-CANDIDATE" prose
    }

    # ---- Surface 2: atlas-04 §X K9 row ----
    edits["atlas_04_K9"] = {
        "path": ATLAS04,
        "edits": [(
            "| **K9** | §VII.X.2-NECESSITY M2 axiom structural source | M2 axiom structural source for Λ_SA finite-L residual | Stage-2 pending |",
            "| **K9** | §VII.X.2-NECESSITY M2 axiom structural source | M2 axiom structural source for Λ_SA finite-L residual | **STAGE-3-PERMANENT since S108 W2-4** (`S108-VIIX2NEC-STAGE2to3-PROMOTION`; the S107 W2-3 blind cross-axis Stage-2 PASS-AND on every necessity clause [`4d98f916…`] + the 6-of-6 full-64-char anchor-SHA harvest VERIFIED on disk; the S88-LAMBDA-SA-* successor family resolved the S87 anchor-availability diagnostic) |",
        )],
        "expect": "| **K9** | §VII.X.2-NECESSITY M2 axiom structural source | M2 axiom structural source for Λ_SA finite-L residual | **STAGE-3-PERMANENT since S108 W2-4**",
        "forbid": None,
    }

    # ---- Surface 3: atlas-07 §VII.X.2-NECESSITY row ----
    edits["atlas_07"] = {
        "path": ATLAS07,
        "edits": [(
            "| §VII.X.2-NECESSITY | M2 axiom structural source for Λ_SA finite-L residual | S87 W1a-6 | connes | STAGE-1-CANDIDATE (registry §VII.X.2-NECESSITY Status: \"STAGE-1-CANDIDATE (necessity-only meta-theorem; STRUCTURAL-DIAGNOSTIC at S87...)\"; atlas-04 K9 \"Stage-2 pending\"; down-corrected from unsupported \"PERMANENT\" 2026-06-12) |",
            "| §VII.X.2-NECESSITY | M2 axiom structural source for Λ_SA finite-L residual | S87 W1a-6 | connes | STAGE-3-PERMANENT (promoted S108 W2-4 `S108-VIIX2NEC-STAGE2to3-PROMOTION`: S107 W2-3 blind cross-axis Stage-2 PASS-AND on every necessity clause [`4d98f916…`] + 6-of-6 full-64-char anchor-SHA harvest VERIFIED on disk via the S88-LAMBDA-SA-* successor family; atlas-04 K9 + open-channel-ledger §C K9 flipped to STAGE-3-PERMANENT in lockstep; supersedes the 2026-06-12 down-correction) |",
        )],
        "expect": "| §VII.X.2-NECESSITY | M2 axiom structural source for Λ_SA finite-L residual | S87 W1a-6 | connes | STAGE-3-PERMANENT (promoted S108 W2-4",
        "forbid": None,
    }

    # ---- Surface 4: open-channel-ledger §C K9 row ----
    edits["open_channel_ledger_K9"] = {
        "path": OCL,
        "edits": [(
            "| K9 §VII.X.2-NECESSITY | M2 axiom structural source for Λ_SA finite-L residual | Stage-2 pending — **S107 W2-3 blind verify INFO (PASS-ON-STRUCTURE)** (`4d98f916…`; necessity-only structure PASS-AND every clause [JOINT-1 necessity + JOINT-2 converse-asymmetry]; INFO from 6/6 anchor-SHA harvest unmet as entry-text presents it → CF-S108-VIIX2NEC-STAGE2to3-PROMOTION; the S88-LAMBDA-SA-* successors may ALREADY have landed 6/6 — VERIFY before promotion) |",
            "| K9 §VII.X.2-NECESSITY | M2 axiom structural source for Λ_SA finite-L residual | **STAGE-3-PERMANENT since S108 W2-4** (`S108-VIIX2NEC-STAGE2to3-PROMOTION`; S107 W2-3 blind cross-axis Stage-2 PASS-AND every clause [`4d98f916…`, JOINT-1 necessity + JOINT-2 converse-asymmetry] + the 6-of-6 full-64-char anchor-SHA harvest VERIFIED on disk — the S88-LAMBDA-SA-* successor family landed all 5 previously-absent anchors + the S87 aggregation gate; the S87 anchor-availability diagnostic RECONCILED 2-of-6 → 6-of-6) |",
        )],
        "expect": "| K9 §VII.X.2-NECESSITY | M2 axiom structural source for Λ_SA finite-L residual | **STAGE-3-PERMANENT since S108 W2-4**",
        "forbid": None,
    }

    return edits


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
                          companion_note: str = "",
                          extra_rows: list[str] | None = None) -> dict:
    """PRINT the verdict payload for the dispatching AGENT to pass to emit_verdict."""
    payload: dict = {
        "session": int(SESSION.lstrip("Ss")),
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins (first 20 lines of stdout)
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. Dual SHAs
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. HARVEST the 6 canonical anchor SHAs + the S107 Stage-2 record + alt-table anchors
    print("=== SHA harvest (canonical 6-anchor set = S88-script enumeration) ===")
    canonical_shas: dict[str, str] = {}   # (local)
    present: list[str] = []               # (local)
    absent: list[str] = []                # (local)
    for label, gate_re, relpath in CANONICAL_ANCHORS:
        vf = PROJECT_ROOT / relpath  # (local)
        sha = grep_canonical_audit_sha(vf, gate_re)  # (local)
        if sha is not None and len(sha) == 64:
            canonical_shas[label] = sha
            present.append(label)
            print(f"  [PRESENT] {label}: {sha}  ({relpath})")
        else:
            canonical_shas[label] = ""
            absent.append(label)
            print(f"  [ABSENT ] {label}: (no full-64-char audit_sha256)  ({relpath})")

    n_present = len(present)  # (local)
    print(f"  n_anchor_shas_full_64_char_on_disk = {n_present} of 6")
    print()

    # alt-table cross-check (registered six-anchor TABLE reading)
    print("=== alt-reading cross-check (registered six-anchor TABLE: S77 5baaa51c + S82 98267d63) ===")
    alt_shas: dict[str, str] = {}  # (local)
    alt_present_all = True         # (local)
    for label, sha_lit, relpath in ALT_TABLE_ANCHORS:
        vf = PROJECT_ROOT / relpath  # (local)
        ok = grep_sha_present(vf, sha_lit)  # (local)
        alt_shas[label] = sha_lit if ok else ""
        alt_present_all = alt_present_all and ok
        print(f"  [{'PRESENT' if ok else 'ABSENT '}] {label}: {sha_lit}  ({relpath})")
    print(f"  alt-table anchors all on disk = {alt_present_all}")
    print()

    # S107 Stage-2 structural-PASS-AND record presence
    s107_vf = PROJECT_ROOT / "computations" / "session-107" / "s107_gate_verdicts.txt"  # (local)
    s107_sha = grep_canonical_audit_sha(s107_vf, r"^S107-VIIX2NEC-STAGE2-VERIFY:")       # (local)
    s107_present = (s107_sha is not None and s107_sha.startswith("4d98f916"))            # (local)
    print(f"=== S107 Stage-2 record: {S107_STAGE2_GATE} audit={s107_sha} present={s107_present} ===")
    print()

    # 3. Determine verdict precursors. PASS-eligibility: 6/6 present AND S107 record present.
    harvest_ok = (n_present == PASS_THRESHOLD) and s107_present  # (local)

    # enumeration reconciliation: do the S88-script set and the registered table name
    # DIFFERENT anchor-4/5 sets (both on disk)? -> the pre-registered INFO branch.
    enumeration_divergent = alt_present_all  # (local) registered table's S77/S82 SHAs also on disk

    # 4. BUILD all 4 surface promotion texts IN MEMORY (no I/O yet) — AFTER-pattern step 1.
    flip_booleans: dict[str, bool] = {}  # (local)
    surfaces_written: list[str] = []     # (local)
    build_error = ""                     # (local)
    if harvest_ok:
        edits = surface_edits(canonical_shas, alt_shas)  # (local)
        built: dict[str, tuple[Path, str, str, str | None]] = {}  # (local) name->(path,newtext,expect,forbid)
        try:
            for name, spec in edits.items():
                original = spec["path"].read_text(encoding="utf-8", errors="replace")  # (local)
                new_text = build_promotion_text(original, spec["edits"])               # (local)
                built[name] = (spec["path"], new_text, spec["expect"], spec["forbid"])
        except Exception as exc:  # build failed -> no writes; honest FAIL
            build_error = f"build_promotion_text error: {exc}"
            print(f"  [BUILD-FAIL] {build_error}")

        if not build_error:
            # AFTER-pattern step 2: write_atomic_with_fsync for each surface
            for name, (path, new_text, _expect, _forbid) in built.items():
                write_atomic_with_fsync(path, new_text)
                surfaces_written.append(name)
            # AFTER-pattern step 3: re_read + verify_section_matches for each surface
            for name, (path, _new_text, expect, forbid) in built.items():
                ok = verify_section_matches(path, expect, forbid)  # (local)
                flip_booleans[name] = bool(ok)
                print(f"  [VERIFY] surface {name}: verify_section_matches = {ok}")
    else:
        print("  [NO-WRITE] harvest_ok is False — promotion deferred; emitting FAIL/INFO, no surface edits.")

    all_surfaces_ok = (len(flip_booleans) == 4) and all(flip_booleans.values())  # (local)

    # 5. Verdict (single-shot AFTER-pattern: the verify booleans determine the verdict).
    #    PASS requires 6/6 + S107 record + all-4-surface verify. INFO if enumeration divergent
    #    (the pre-registered INFO branch: both 6-anchor readings on disk, promotion still fires).
    #    FAIL if <6/6 on disk OR a surface verify failed (harvest/landing IS the gate).
    if not harvest_ok:
        verdict = "FAIL"  # (local)
    elif build_error or not all_surfaces_ok:
        verdict = "FAIL"  # (local) landing-verify failure -> honest mechanical closure
    elif enumeration_divergent:
        verdict = "INFO"  # (local) pre-registered enumeration-reconciliation branch; promotion fired
    else:
        verdict = "PASS"  # (local)

    # 6. value payload (no single-quote chars).
    value = (f"n_anchor_shas_full_64_char_on_disk={n_present}_of_6;"
             f"s107_stage2_record_4d98f916_present={s107_present};"
             f"enumeration=S88-script-canonical-set_ADOPTED_alt-registered-table-S77-5baaa51c+S82-98267d63_ALSO-on-disk_divergent={enumeration_divergent};"
             f"4surface_flip_registry+atlas04K9+atlas07+ocl-C-K9_all_verified={all_surfaces_ok};"
             f"promotion=STAGE-1-CANDIDATE->STAGE-3-PERMANENT")  # (local)

    # 7. Emit 4-tuple + verdict payload
    tag = emit_4tuple(n_present, SCHEME, CONVENTION, L_MAX)
    print(tag)
    extra = [
        (f"# n_present={n_present}/6 s107_record={s107_present} "
         f"surfaces={'/'.join(surfaces_written) if surfaces_written else 'NONE'} "
         f"flips={json.dumps(flip_booleans, separators=(',',':'))}"),
        ("# enumeration: canonical=S88-script-set "
         "{S46,S64,S65,S77,C9}-successors(s88)+S87-aggregation(s87 fa225aac); "
         "alt=registered-table S77(s84 5baaa51c)+S82-MP-Exclusion(s82 98267d63); BOTH 6/6 on disk; "
         "INFO=pre-registered enumeration-reconciliation branch (promotion fires)"),
    ]  # (local)
    payload = print_verdict_payload(
        verdict, value, audit_sha, content_sha,
        companion_note=("§VII.X.2-NECESSITY K9 STAGE-1-CANDIDATE->STAGE-3-PERMANENT; "
                        "6/6 SHA harvest + S107 4d98f916 + 4-surface flip"),
        extra_rows=extra,
    )

    # 8. Persist npz (6 harvested SHAs + present/absent partition + 4-surface flip booleans)
    surface_names = ["registry_VII_X_2_NECESSITY", "atlas_04_K9", "atlas_07", "open_channel_ledger_K9"]  # (local)
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        verdict=verdict,
        n_anchor_shas_full_64_char_on_disk=n_present,
        pass_threshold=PASS_THRESHOLD,
        canonical_anchor_labels=np.array([a[0] for a in CANONICAL_ANCHORS]),
        canonical_anchor_shas=np.array([canonical_shas[a[0]] for a in CANONICAL_ANCHORS]),
        present_labels=np.array(present),
        absent_labels=np.array(absent if absent else [""]),
        alt_table_labels=np.array([a[0] for a in ALT_TABLE_ANCHORS]),
        alt_table_shas=np.array([alt_shas[a[0]] for a in ALT_TABLE_ANCHORS]),
        alt_present_all=alt_present_all,
        enumeration_divergent=enumeration_divergent,
        s107_stage2_gate=S107_STAGE2_GATE,
        s107_stage2_sha=(s107_sha or ""),
        s107_present=s107_present,
        surface_names=np.array(surface_names),
        surface_flip_booleans=np.array([flip_booleans.get(n, False) for n in surface_names]),
        all_surfaces_ok=all_surfaces_ok,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"  npz -> {OUT_NPZ}")

    # 9. Optional plot: 6/6 anchor-presence + 4-surface-flip diagnostic
    if _HAVE_MPL:
        try:
            fig, axes = plt.subplots(1, 2, figsize=(11, 4))  # (local)
            ax0 = axes[0]  # (local)
            labels0 = [a[0].replace("anchor_", "a").split("_")[0] + "_" + a[0].split("_")[2]
                       if len(a[0].split("_")) > 2 else a[0] for a in CANONICAL_ANCHORS]  # (local)
            vals0 = [1 if canonical_shas[a[0]] else 0 for a in CANONICAL_ANCHORS]  # (local)
            ax0.bar(range(6), vals0, color=["#2a7" if v else "#c33" for v in vals0])
            ax0.set_xticks(range(6))
            ax0.set_xticklabels([f"a{i+1}" for i in range(6)])
            ax0.set_ylim(0, 1.2)
            ax0.set_ylabel("full-64-char SHA on disk")
            ax0.set_title(f"6-anchor harvest: {n_present}/6  (verdict {verdict})")
            ax1 = axes[1]  # (local)
            svals = [1 if flip_booleans.get(n, False) else 0 for n in surface_names]  # (local)
            ax1.bar(range(4), svals, color=["#2a7" if v else "#c33" for v in svals])
            ax1.set_xticks(range(4))
            ax1.set_xticklabels(["registry", "atlas-04\nK9", "atlas-07", "OCL\n§C K9"], fontsize=8)
            ax1.set_ylim(0, 1.2)
            ax1.set_ylabel("verify_section_matches")
            ax1.set_title("4-surface STAGE-3 flip")
            fig.suptitle("S108-VIIX2NEC-STAGE2to3-PROMOTION — §VII.X.2-NECESSITY K9")
            fig.tight_layout()
            fig.savefig(OUT_PNG, dpi=110)
            print(f"  png -> {OUT_PNG}")
        except Exception as exc:  # pragma: no cover
            print(f"  [plot skipped] {exc}")

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    _ = payload  # payload printed above for the agent
    return 0  # script health: 0 regardless of scientific verdict (gate-verdicts.md exit-code semantics)


if __name__ == "__main__":
    sys.exit(main())
