#!/usr/bin/env python3
"""
S{{SESSION}} {{WAVE}}-{{GATE_ID}} — {{SHORT_DESCRIPTION}}
========================================================

Gate: {{GATE_ID}} ({{TRIGGER}})
  Trigger options: [SIGN] | [VERIFY] | [AUDIT] | [VERIFY-THEOREM] | [CHAIN]

Pre-registered threshold:
  {{PASS_CRITERION}}
  PASS iff {{CONDITION}}, FAIL iff {{CONDITION_NEG}}, INFO otherwise.

Inputs (SHA-256 dual-pinned at runtime — see §4 below; S84+ schema):
  - {{INPUT_FILE_1}}
  - {{INPUT_FILE_2}}
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<computed>, scheme={{SCHEME}}, convention={{CONVENTION}}, L_max={{L_MAX}})

Classification: {{PHONONIC | GEOMETRIC | PARTICLE | NON-PHONONIC}}

METHODOLOGY
-----------
{{ONE-PARAGRAPH DESCRIPTION OF METHOD; cite prior sessions/gates/theorems.}}

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- GPU path via `torch.linalg` for matrices >= 100x100 (see computation-environment.md)
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- Gate verdict emitted via the `emit_verdict` knowledge-MCP tool (race-safe,
  syntax-forced; per `.claude/rules/gate-verdicts.md` §"Race-Safe Emission"):
  the script PRINTS the payload (`print_verdict_payload`) carrying BOTH
  `audit_sha256=<64>` and `content_sha256=<64>` plus `schema_version=S84+`;
  the dispatching AGENT reads it and calls `mcp__knowledge__emit_verdict(**payload)`.
  The script does NOT write `s{{SESSION}}_gate_verdicts.txt` directly — a raw
  `open("a")` append is NOT atomic across processes on Windows (it lost 5/8
  lines under 8 concurrent writers in S98).
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
import sys
import time
from pathlib import Path

# Numerical — uncomment as needed. torch.linalg PREFERRED for N >= 100.
# import numpy as np
# import torch

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
# Scripts live at computations/session-N/. SESSION_DIR is this script's parent;
# COMPUTATIONS_DIR is the parent of SESSION_DIR; SHARED_DIR holds
# canonical_constants.py and shared helpers.
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S{{SESSION}}"                                           # (local)
GATE_ID = "{{GATE_ID}}"                                            # (local)
SCHEME = "{{SCHEME}}"                                              # (local)
CONVENTION = "{{CONVENTION}}"                                      # (local)
L_MAX = {{L_MAX}}                                                  # (local)

# Pre-registered pass/fail threshold (define BEFORE running)
PASS_THRESHOLD = {{THRESHOLD_VALUE}}                               # (local)
N_EVAL = {{N_EVAL}}                                                # (local)
SCAN_MIN = {{SCAN_MIN}}                                            # (local)
SCAN_MAX = {{SCAN_MAX}}                                            # (local)

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / f"s{{SESSION}}_{{GATE_ID_LOWER}}_results.npz"
OUT_PNG = SESSION_DIR / f"s{{SESSION}}_{{GATE_ID_LOWER}}.png"
# The verdict file (s{SESSION}_gate_verdicts.txt) is written by the emit_verdict
# MCP tool — NOT by this script. See print_verdict_payload below + the
# "Race-Safe Emission" section of .claude/rules/gate-verdicts.md.

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    # SESSION_DIR / "{{OTHER_INPUT_NPZ}}",
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
#
# S84+ DUAL-SHA SCHEMA (W9a-99):
#   audit_sha256   = sha256( bytes(script) || bytes(canonical) || bytes(pinmap_json) )
#   content_sha256 = sha256( bytes(script) )
#
# Rationale: the legacy single-SHA closure collapsed (script, canonical,
# pinmap) into one digest, producing H(gate | single_SHA) = log2(3) = 1.585
# bits of pre-image entropy in the S82 G59 case. Splitting into two SHAs
# (one script-only, one script+canonical+pinmap) brings H(gate | (audit,
# content)) to 0 bits (joint pre-image size = 1 modulo 2^{-128} SHA-256
# collision probability).
#
# Canonical verdict line (S84+):
#   {GATE}: PASS|FAIL|INFO -- value=<v> scheme=<s> convention=<c> L_max=<L>
#     audit_sha256=<64> content_sha256=<64> schema_version=S84+
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
    """Stable hash over all input SHAs (invariant to dict ordering).

    Retained for backward compatibility; in the S84+ dual-SHA schema this
    function is an intermediate used by `audit_sha256`.
    """
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
    """Compute (audit_sha256, content_sha256) per the S84+ dual-SHA schema.

    audit_sha256:
        sha256( bytes(script) || bytes(canonical_constants.py) || pinmap_json )
        where pinmap_json is the canonical (sorted, separators=(",", ":"))
        JSON serialization of `pins` (the {relpath: sha256} map).

    content_sha256:
        sha256( bytes(script) )
        — responds to script edits only; INVARIANT under canonical /
        pinmap change. This separation resolves the S82 G59 ambiguity.
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
# Section 5 — Compute
# ---------------------------------------------------------------------------

def compute() -> dict:
    """Main computation. Return a dict with 'value' and any cross-check fields.

    All internal intermediates MUST be tagged `# (local)`.
    """
    # Example:
    #     result = some_canonical * some_other_canonical   # framework-valid
    #     z_ratio = result / M_KK                          # (local)
    raise NotImplementedError("Replace this body with the computation.")


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(
    verdict: str,
    value,
    audit_sha: str,
    content_sha: str,
    sign_verdict: str | None = None,
    magnitude_verdict: str | None = None,
    regime_verdict: str | None = None,
    companion_note: str = "",
    extra_rows: list[str] | None = None,
) -> dict:
    """Emit the verdict PAYLOAD for the dispatching AGENT to pass to the
    knowledge-MCP `emit_verdict` tool.

    The script does NOT write the verdict file — that single, lock-serialized
    write is owned by `emit_verdict` (per `.claude/rules/gate-verdicts.md`
    §"Race-Safe Emission"). This closes the Windows cross-process O_APPEND
    lost-update race: `open("a")` is NOT atomic across processes on Windows;
    concurrent appenders lose lines (S98 lost 5/8 under 8 writers). The script
    still computes the dual-SHA (it alone holds the input-pin map + content
    target); the agent reads the delimited JSON block below from this script's
    stdout and calls `mcp__knowledge__emit_verdict(**payload)`.

    For [SIGN]-trigger gates, pass ALL THREE of sign/magnitude/regime_verdict
    (the tool enforces all-three-or-none). `value` is the RAW payload string
    (no surrounding quotes, no single-quote chars — the tool wraps value='...').
    `extra_rows` are optional `#`-prefixed companion rows (EMERGENCE-1 detail,
    regulator_pin, etc.).
    """
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
    if not (sign_verdict is None and magnitude_verdict is None and regime_verdict is None):
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    # Delimited so the agent can extract it deterministically from stdout.
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


def evaluate_gate(value) -> str:
    """Compare computed value to pre-registered threshold; return PASS/FAIL/INFO."""
    # Replace this logic with the actual gate rule.
    # Example for |value| <= PASS_THRESHOLD:
    #     if value <= PASS_THRESHOLD:
    #         return "PASS"
    #     if value > PASS_THRESHOLD * 10:
    #         return "FAIL"
    #     return "INFO"
    raise NotImplementedError("Define the gate rule before running.")


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins (first 20 lines of stdout)
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

    # 2. Compute
    result = compute()
    value = result["value"]

    # 3. Evaluate gate
    verdict = evaluate_gate(value)

    # 4. Emit 4-tuple + PRINT the emit_verdict payload. The dispatching agent
    #    reads the delimited JSON block and calls mcp__knowledge__emit_verdict.
    #    For [SIGN] gates, also pass sign_verdict/magnitude_verdict/regime_verdict.
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)
    print_verdict_payload(verdict, value, audit_sha, content_sha)

    # 5. Final summary
    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0 if verdict != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
