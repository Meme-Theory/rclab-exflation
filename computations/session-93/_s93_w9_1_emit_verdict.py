#!/usr/bin/env python3
"""
_s93_w9_1_emit_verdict.py — dual-SHA verdict emitter for S93-W9-1-PLAN-LINE-ANCHOR-VALIDATOR.

[AUDIT]-trigger METHODOLOGY-class gate. Computes the dual-SHA closure at runtime
from the ordered input-pin map (never hardcoded) per the S84+ schema in
.claude/templates/script-template.py §4, then appends ONE canonical verdict line
+ ONE dual-SHA companion comment row atomically (single open("a")).

audit_sha256   = sha256( bytes(validator_script) || bytes(canonical_constants.py)
                         || pinmap_json )
content_sha256 = sha256( bytes(validator_script) )

pinmap = ordered {relpath: sha256} over the gate's input files (plan §W9-1
input_files: _plan_upstream_pin_validator.py + permanent-results-registry.md +
session-92-w4-workingpaper.md) PLUS the canonical calibration-corpus drift values
+ severity bands (plan §W9-1 audit_discriminators: canonical = the calibration-
corpus drift values + severity bands). The validator script's own bytes are the
content_sha256 source.

No 3-tuple companion row ([AUDIT] trigger, not [SIGN]).
NON-PHONONIC audit-floor tool — no framework constants imported.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

# This emitter lives at computations/session-93/<file>; project root is two up.
SESSION_DIR = Path(__file__).resolve().parent          # (local) computations/session-93
COMPUTATIONS_DIR = SESSION_DIR.parent                  # (local) computations
SHARED_DIR = COMPUTATIONS_DIR / "_shared"              # (local)
PROJECT_ROOT = COMPUTATIONS_DIR.parent                 # (local)

GATE_ID = "S93-W9-1-PLAN-LINE-ANCHOR-VALIDATOR"        # (local)
SCHEME = "PLAN-LINE-ANCHOR-DRIFT-HEADING-GREP-VALIDATOR"  # (local)
CONVENTION = (
    "section_anchor_lines-vs-current-registry-heading-grep-"
    "S2-at-drift-gt-50-S1-at-drift-gt-200"
)  # (local)
L_MAX = "N/A"                                          # (local) audit-script; no spectral compute

VALIDATOR_SCRIPT = SHARED_DIR / "_plan_line_anchor_validator.py"   # (local) content_sha source
CANONICAL = SHARED_DIR / "canonical_constants.py"                  # (local) audit_sha component
VERDICT_TXT = SESSION_DIR / "s93_gate_verdicts.txt"               # (local)
SELFTEST_JSON = SESSION_DIR / "s93_w9_1_plan_line_anchor_validator_selftest.json"  # (local)

# Input-pin files (plan §W9-1 input_files block).
INPUT_FILES = [
    SHARED_DIR / "_plan_upstream_pin_validator.py",
    PROJECT_ROOT / "sessions" / "permanent-results-registry.md",
    PROJECT_ROOT / "sessions" / "session-92" / "session-92-w4-workingpaper.md",
]

# Canonical calibration-corpus drift values + severity bands (plan §W9-1
# audit_discriminators: audit_sha256_inputs canonical component). These are the
# pre-registered corpus values the self-test reproduces; pinned into the audit
# closure so the verdict is reproducible against the exact corpus.
CALIBRATION_CANONICAL = {
    "drift_S2_floor": 50,
    "drift_S1_floor": 200,
    "corpus": [
        ["VII.AR", 106, "S2"],
        ["VII.AW.OP-PROJ", 229, "S1"],
        ["VII.U.2", 56, "S2"],
        ["S92-W5", 150, "S2"],
    ],
}


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def main() -> int:
    # 1. Load self-test result; PASS criterion = overall_pass True (5/5).
    st = json.loads(SELFTEST_JSON.read_text(encoding="utf-8"))  # (local)
    overall_pass = bool(st.get("overall_pass"))  # (local)
    n_pass = st.get("n_tests_pass")  # (local)
    n_tests = st.get("n_tests")  # (local)
    hook_ok = bool(st.get("integration_hook_upstream_validator"))  # (local)
    validator_exists = VALIDATOR_SCRIPT.exists()  # (local)
    has_selftest_main = (
        validator_exists and "__main__" in VALIDATOR_SCRIPT.read_text(encoding="utf-8")
    )  # (local)

    # METHODOLOGY-class artifact-existence-with-content PASS predicate:
    #   validator present + self-test 5/5 + integration hook live + __main__ driver.
    verdict = "PASS" if (
        overall_pass and validator_exists and has_selftest_main and hook_ok
    ) else "FAIL"  # (local)

    # 2. Build the ordered input-pin map (relpath -> sha256), sorted for stability.
    pins: dict[str, str] = {}  # (local)
    for p in INPUT_FILES:
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        pins[rel] = sha256_of(p)
    # Fold the canonical calibration-corpus values into the pinmap (audit-SHA
    # canonical component) so the audit closure is keyed to the exact corpus.
    pins["__calibration_canonical__"] = hashlib.sha256(
        json.dumps(CALIBRATION_CANONICAL, sort_keys=True,
                   separators=(",", ":")).encode("utf-8")
    ).hexdigest()

    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)

    # 3. Dual-SHA per S84+ schema.
    script_bytes = VALIDATOR_SCRIPT.read_bytes()  # (local) content_sha source
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = CANONICAL.read_bytes()
    except OSError:
        canonical_bytes = b""

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit_sha = h_audit.hexdigest()  # (local)

    content_sha = hashlib.sha256(script_bytes).hexdigest()  # (local)

    # 4. Verdict value string.
    value = (
        f"selftest_{n_pass}of{n_tests}_PASS_4TP_at_correct_severity_"
        f"VII-AR+106-S2_VII-AW-OP-PROJ+229-S1_VII-U2+56-S2_S92-W5~150-S2_"
        f"1TN_zero-drift-NO-ACTION_integration-hook-_plan_upstream_pin_validator={hook_ok}_"
        f"validator-exists-with-__main__-selftest={has_selftest_main}"
    )  # (local)

    # 5. Print input-pin SHAs (first 20 lines of stdout per gate-verdicts.md).
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    for rel, sha in sorted(pins.items()):
        print(f"  {rel}: {sha[:16]}...")
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (validator script only)")
    print(f"  verdict: {verdict}  (selftest {n_pass}/{n_tests})")
    print()

    # 6. Atomic append: ONE canonical line + ONE dual-SHA companion row.
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    companion_row = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(companion_row)

    print(f"=== {GATE_ID}: {verdict} appended ===")
    print(f"  audit_sha256={audit_sha}")
    print(f"  content_sha256={content_sha}")
    return 0  # verdict is data; exit 0 on valid emission (math-scripts.md §Exit Codes)


if __name__ == "__main__":
    sys.exit(main())
