#!/usr/bin/env python3
"""
S86 W0c-2 — S86-K_CRIT_BDG-CANONICAL-CONSTANTS-REGISTRATION
============================================================

Gate: S86-K_CRIT_BDG-CANONICAL-CONSTANTS-REGISTRATION ([VERIFY])
Classification: META

Pre-registered threshold (plan §W0c-2.9):
  PASS iff K_crit_BdG = 2.035 exists in canonical_constants.py with a
  provenance block AND K_crit = 91.5 coexists unaltered.
  FAIL iff variable absent, value mismatch, K_crit overwritten, or
  provenance block missing.

Inputs (S84+ dual-SHA):
  - computations/_shared/canonical_constants.py (pre-edit)
  - computations/session-62/s62_w2_bdg_critical.py (provenance trace; may be absent)
  - script bytes (this file)

Output 4-tuple:
  (value=2.035, scheme=canonical_constants_register,
   convention=BdG_channel, L_max=N/A)
"""
from __future__ import annotations

import hashlib
import json
import sys
import time
import os
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


os.environ.setdefault("OMP_NUM_THREADS", "8")

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S86"
GATE_ID = "S86-K_CRIT_BDG-CANONICAL-CONSTANTS-REGISTRATION"
SCHEME = "canonical_constants_register"
CONVENTION = "BdG_channel"
L_MAX = "N/A"

CANONICAL_PATH = resolve_script(None, 'canonical_constants.py')
S62_SOURCE_PATH = resolve_script(62, 's62_w2_bdg_critical.py')  # may be absent
VERDICT_TXT = resolve_output(86, 's86_gate_verdicts.txt')

# Pre-registered values (plan §W0c-2.7)
K_CRIT_BDG_TARGET = 2.035   # (local) — plan-pinned BdG critical coupling
K_CRIT_EXPECTED = 91.5      # (local) — plan-pinned unchanged-assertion

# The new entry block to insert into canonical_constants.py
K_CRIT_BDG_BLOCK = """
# ─────────────────────────────────────────────────────────────
# K_crit_BdG: BdG-channel critical coupling
# ─────────────────────────────────────────────────────────────
# PROVENANCE: S62 W2 (Volovik BdG-channel derivation),
#             confirmed S82 W2-4 (R3 anchor numerical coincidence; K_base=2.035),
#             S85 W2-12 BdG band -> CMB l_crit projection (PROVEN, S7 combined landscape).
# CITATION:   sessions/permanent-results-registry.md (W2-12 theorem row)
# SOURCE:     active code reference: computations/session-85/s85_w2_band_detector_map.py
#             (S62 W2 producing script not in current repo tree; provenance via S85 W2-12 PROVEN).
# DISTINCT FROM:
#   K_crit = 91.5  (inflationary corridor critical coupling, S84 W5-55)
#   K_base = 2.035 (R3 band-weighted squeezing anchor, S82 W2-4 — numerical coincidence)
#   K_floor / K_wall (S85 W5-D.4 substrate-corridor brackets; pinned in W0c-4)
# UNITS:      dimensionless (coupling in M_KK units)
# ─────────────────────────────────────────────────────────────
K_crit_BdG = 2.035  # BdG-channel critical coupling (Volovik S62; S86 W0c-2)
"""


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        if sha:
            print(f"  {rel}: {sha[:16]}...")
        else:
            print(f"  {rel}: ABSENT")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
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


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def insert_block_after_kcrit(text: str) -> tuple[str, bool]:
    """Insert K_CRIT_BDG_BLOCK right after the existing K_crit assignment line.

    Returns (new_text, inserted) where `inserted` is False if K_crit_BdG was
    already present (idempotent re-runs).
    """
    if "K_crit_BdG" in text:
        return text, False  # already present; idempotent

    lines = text.split("\n")  # (local)
    out: list[str] = []  # (local)
    inserted = False  # (local)
    for line in lines:
        out.append(line)
        if (not inserted) and line.startswith("K_crit ") and "= 91.5" in line:
            # Append our K_crit_BdG block immediately after this line
            for bline in K_CRIT_BDG_BLOCK.strip("\n").split("\n"):
                out.append(bline)
            inserted = True
    return "\n".join(out), inserted


def import_test() -> dict:
    """Subprocess import-test confirming both K_crit and K_crit_BdG."""
    import subprocess  # (local)
    cmd = [
        sys.executable,
        "-c",
        (
            "import sys; sys.path.insert(0, 'computations'); "
            "from canonical_constants import K_crit, K_crit_BdG; "
            "assert K_crit == 91.5, f'K_crit={K_crit}'; "
            "assert K_crit_BdG == 2.035, f'K_crit_BdG={K_crit_BdG}'; "
            "print('OK')"
        ),
    ]  # (local)
    proc = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        cwd=str(PROJECT_ROOT),
    )  # (local)
    return {
        "returncode": proc.returncode,
        "stdout": proc.stdout.strip(),
        "stderr": proc.stderr.strip(),
    }


def main() -> int:
    t0 = time.time()  # (local)

    # Compute pre-edit SHAs
    canonical_pre_text = CANONICAL_PATH.read_text(encoding="utf-8")  # (local)
    pre_edit_sha = hashlib.sha256(
        canonical_pre_text.encode("utf-8")
    ).hexdigest()  # (local)
    print(f"=== {GATE_ID} — pre-edit canonical_constants.py SHA ===")
    print(f"  {pre_edit_sha}")

    pins = log_input_pins([CANONICAL_PATH, S62_SOURCE_PATH])

    # Verify K_crit value unchanged BEFORE edit
    k_crit_pre_check = "K_crit = 91.5" in canonical_pre_text  # (local)
    if not k_crit_pre_check:
        print("PRE-EDIT FAIL: K_crit = 91.5 not found at expected location")
        # We still proceed but this likely means the assertion will fail.

    # Insert the block
    new_text, inserted = insert_block_after_kcrit(canonical_pre_text)  # (local)
    if inserted:
        CANONICAL_PATH.write_text(new_text, encoding="utf-8")
        print(f"  K_crit_BdG block inserted after K_crit line.")
    else:
        print(f"  K_crit_BdG already present; idempotent no-op.")

    # Verify K_crit STILL = 91.5 post-edit (no overwrite)
    post_text = CANONICAL_PATH.read_text(encoding="utf-8")  # (local)
    k_crit_post_check = "K_crit = 91.5" in post_text  # (local)
    k_crit_bdg_post_check = "K_crit_BdG = 2.035" in post_text  # (local)

    # Compute dual SHA AFTER edit (so audit_sha includes the edited canonical)
    script_path = Path(__file__).resolve()  # (local)
    pins_for_audit = dict(pins)  # (local)
    pins_for_audit[
        "computations/_shared/canonical_constants.py"
    ] = hashlib.sha256(post_text.encode("utf-8")).hexdigest()
    audit_sha, content_sha = compute_dual_sha(
        script_path, CANONICAL_PATH, pins_for_audit
    )
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical_post+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # Run subprocess import test
    test = import_test()
    print(f"=== Import test ===")
    print(f"  returncode: {test['returncode']}")
    print(f"  stdout:     {test['stdout']}")
    if test["stderr"]:
        print(f"  stderr:     {test['stderr']}")

    # Verdict logic
    pass_conditions = (
        k_crit_post_check
        and k_crit_bdg_post_check
        and test["returncode"] == 0
        and test["stdout"] == "OK"
    )  # (local)

    verdict = "PASS" if pass_conditions else "FAIL"  # (local)
    value = K_CRIT_BDG_TARGET  # (local) — pre-registered value

    # 4-tuple output
    print()
    print(
        f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, "
        f"L_max={L_MAX})"
    )

    append_verdict(verdict, value, audit_sha, content_sha)

    # Diagnostic JSON for traceability
    diag = {
        "gate_id": GATE_ID,
        "verdict": verdict,
        "session": SESSION,
        "wave": "W0c",
        "k_crit_pre_check": k_crit_pre_check,
        "k_crit_post_check": k_crit_post_check,
        "k_crit_bdg_post_check": k_crit_bdg_post_check,
        "import_test": test,
        "canonical_pre_edit_sha": pre_edit_sha,
        "canonical_post_edit_sha": pins_for_audit[
            "computations/_shared/canonical_constants.py"
        ],
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "inserted_this_run": inserted,
    }  # (local)
    diag_path = resolve_output(86, 's86_w0c_2_kcrit_bdg_register.json')  # (local)
    diag_path.write_text(json.dumps(diag, indent=2), encoding="utf-8")
    print(f"\nDiagnostic JSON: {diag_path.name}")

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
