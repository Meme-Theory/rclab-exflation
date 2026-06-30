#!/usr/bin/env python3
"""
S85 W1c-1 — CANONICAL-CONSTANTS-ALPHA-S-DISAMBIGUATION-PATCH
============================================================

Gate: S85-W1c-CANONICAL-CONSTANTS-ALPHA-S-DISAMBIGUATION-PATCH ([AUDIT])

Pre-registered threshold (plan §W1c-1):
  PASS iff (a) three patches present and syntactically valid;
           (b) `from canonical_constants import *` succeeds (subprocess);
           (c) `alpha_s_inflation_framework` evaluates to n_s_canon**2 - 1
               within 1e-10 of the reference;
           (d) `alpha_s_framework_central` alias present and equal;
           (e) subprocess re-import does not raise ImportError.
  FAIL iff any of (a)-(e) fail.
  INFO iff patches applied but downstream breakage detected in >=1 script.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py (AUDIT+CONTENT target; patched in place)
  - this script's own bytes
Output 4-tuple:
  (value=3_patches_landed, scheme=canonical-constants-hygiene,
   convention=option-2-commit, L_max=N/A)

Classification: META (canonical_constants.py hygiene)

METHODOLOGY
-----------
Three patches are applied to canonical_constants.py (idempotently — if already
present, patch is a no-op). The patches are:

  (a) Inline disambiguation comment on the `alpha_s_MZ_obs = 0.1180` row:
      "# QCD strong coupling at M_Z. NOT to be conflated with inflationary
       alpha_s (see alpha_s_inflation_framework)."

  (b) Inline disambiguation comment on the `planck_alpha_s = -0.0045` row:
      "# Planck 2018 inflationary dn_s/dlnk. NOT to be conflated with QCD
       alpha_s (see alpha_s_MZ_obs)."

  (c) New block near the alpha_s section declaring:
        n_s_canon = planck_ns  # alias so plan notation resolves
        alpha_s_inflation_framework = n_s_canon**2 - 1
        alpha_s_framework_central   = alpha_s_inflation_framework

Verification: a subprocess invokes the venv Python with
  `from canonical_constants import *; print(alpha_s_inflation_framework)`
and asserts the value equals n_s_canon**2 - 1 to 1e-10.

DISCIPLINE
----------
- `from canonical_constants import *` at top
- All local intermediates tagged `# (local)`
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- Exit 0 regardless of PASS/FAIL per .claude/rules/math-scripts.md §Exit Codes
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
import subprocess
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
GATE_ID = "S85-W1c-CANONICAL-CONSTANTS-ALPHA-S-DISAMBIGUATION-PATCH"  # (local)
SCHEME = "canonical-constants-hygiene"                       # (local)
CONVENTION = "option-2-commit"                               # (local)
L_MAX = "N/A"                                                # (local)

# Pre-registered threshold: 3 patches, all must land
EXPECTED_PATCHES = 3                                         # (local)
REFERENCE_ALPHA_TOLERANCE = 1e-10                            # (local) plan §W1c-1 machinery pin
VENV_PYTHON = PROJECT_ROOT / "phonon-exflation-sim" / ".venv312" / "Scripts" / "python.exe"  # (local)

CANONICAL_PATH = resolve_script(None, 'canonical_constants.py')
VERDICT_TXT = resolve_output(85, 's85_gate_verdicts.txt')
OUT_JSON = resolve_output(85, 's85_w1c_canonical_constants_disambiguation.json')

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
    """(audit_sha256, content_sha256) per S84+ W9a-99 schema."""
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
# Section 5 — Patch specifications
# ---------------------------------------------------------------------------

# Patch (a): extend comment on alpha_s_MZ_obs
PATCH_A_OLD = "alpha_s_MZ_obs = 0.1180        # alpha_s(M_Z) observed (PDG 2024)"
PATCH_A_NEW = (
    "alpha_s_MZ_obs = 0.1180        # alpha_s(M_Z) observed (PDG 2024). "
    "QCD strong coupling at M_Z. "
    "NOT to be conflated with inflationary alpha_s "
    "(see alpha_s_inflation_framework). "
    "Disambiguation: S85-W1c-CANONICAL-CONSTANTS-ALPHA-S-DISAMBIGUATION-PATCH."
)

# Patch (b): extend comment on planck_alpha_s
PATCH_B_OLD = "planck_alpha_s = -0.0045       # Planck 2018 dn_s/dlnk (TT,TE,EE+lowE+lensing)"
PATCH_B_NEW = (
    "planck_alpha_s = -0.0045       # Planck 2018 dn_s/dlnk (TT,TE,EE+lowE+lensing). "
    "Inflationary running of the scalar spectral index. "
    "NOT to be conflated with QCD alpha_s(M_Z) (see alpha_s_MZ_obs). "
    "Disambiguation: S85-W1c-CANONICAL-CONSTANTS-ALPHA-S-DISAMBIGUATION-PATCH."
)

# Patch (c): new block, inserted AFTER planck_alpha_s_err line
# (it depends on planck_ns which is defined just above).
PATCH_C_ANCHOR = "planck_alpha_s_err = 0.0067    # Planck 2018 1-sigma on alpha_s"
PATCH_C_NEW = (
    "planck_alpha_s_err = 0.0067    # Planck 2018 1-sigma on alpha_s\n"
    "\n"
    "# ── S85 W1c-1: alpha_s disambiguation block ──\n"
    "# Framework S50-51 identity prediction for INFLATIONARY alpha_s = dn_s/dlnk.\n"
    "# Provenance: S50-51 derivation; interpretation-commit W1c-2 (2026-04-23).\n"
    "# Current: n_s_canon=0.9649, yields -0.068968.\n"
    "# Planck 2018 observed: -0.0045 +/- 0.0067.\n"
    "# Magnitude gap 15.3x; separation 9.62 sigma. See W1c-5 registry landing.\n"
    "# Aliases below let plan-notation `n_s_canon` resolve and let gate scripts\n"
    "# import `alpha_s_framework_central` as the canonical framework handle.\n"
    "n_s_canon = planck_ns          # alias: plan-notation n_s_canon = 0.9649 (S85 W1c-1)\n"
    "alpha_s_inflation_framework = n_s_canon**2 - 1  "
    "# Framework prediction; inflationary alpha_s (S50-51 identity, W1c-2 commit)\n"
    "alpha_s_framework_central = alpha_s_inflation_framework  "
    "# canonical handle for gate scripts (S85 W1c-1)"
)

# Idempotency sentinels (presence of these strings indicates patch is already applied)
SENTINEL_A = "NOT to be conflated with inflationary alpha_s"   # in patched alpha_s_MZ_obs
SENTINEL_B = "NOT to be conflated with QCD alpha_s(M_Z)"        # in patched planck_alpha_s
SENTINEL_C = "alpha_s_inflation_framework = n_s_canon**2 - 1"   # the new block


# ---------------------------------------------------------------------------
# Section 6 — Patch application (idempotent)
# ---------------------------------------------------------------------------


def already_has(text: str, sentinel: str) -> bool:
    return sentinel in text


def apply_patches(text: str) -> tuple:
    """Apply the three patches idempotently. Return (new_text, applied_list)."""
    applied = []  # (local)
    new_text = text  # (local)

    # Patch A: alpha_s_MZ_obs comment
    if already_has(new_text, SENTINEL_A):
        applied.append(("A", "already-present"))
    elif PATCH_A_OLD in new_text:
        new_text = new_text.replace(PATCH_A_OLD, PATCH_A_NEW, 1)
        applied.append(("A", "applied"))
    else:
        applied.append(("A", "anchor-not-found"))

    # Patch B: planck_alpha_s comment
    if already_has(new_text, SENTINEL_B):
        applied.append(("B", "already-present"))
    elif PATCH_B_OLD in new_text:
        new_text = new_text.replace(PATCH_B_OLD, PATCH_B_NEW, 1)
        applied.append(("B", "applied"))
    else:
        applied.append(("B", "anchor-not-found"))

    # Patch C: new disambiguation block (inserted AFTER planck_alpha_s_err line)
    if already_has(new_text, SENTINEL_C):
        applied.append(("C", "already-present"))
    elif PATCH_C_ANCHOR in new_text:
        new_text = new_text.replace(PATCH_C_ANCHOR, PATCH_C_NEW, 1)
        applied.append(("C", "applied"))
    else:
        applied.append(("C", "anchor-not-found"))

    return new_text, applied


# ---------------------------------------------------------------------------
# Section 7 — Subprocess re-import verification
# ---------------------------------------------------------------------------


def subprocess_reimport_check() -> dict:
    """Invoke venv Python in a subprocess; verify the three new symbols exist
    and alpha_s_inflation_framework equals n_s_canon**2 - 1 to 1e-10."""
    check_script = (
        "import sys\n"
        "sys.path.insert(0, r'" + str(SCRIPT_DIR).replace("\\", "\\\\") + "')\n"
        "from canonical_constants import (n_s_canon, planck_ns,\n"
        "    alpha_s_inflation_framework, alpha_s_framework_central)\n"
        "ref = n_s_canon**2 - 1\n"
        "d1 = abs(alpha_s_inflation_framework - ref)\n"
        "d2 = abs(alpha_s_framework_central - alpha_s_inflation_framework)\n"
        "d3 = abs(n_s_canon - planck_ns)\n"
        "import json\n"
        "print('SUBPROC_RESULT_JSON:' + json.dumps({\n"
        "    'n_s_canon': n_s_canon,\n"
        "    'planck_ns': planck_ns,\n"
        "    'alpha_s_inflation_framework': alpha_s_inflation_framework,\n"
        "    'alpha_s_framework_central': alpha_s_framework_central,\n"
        "    'reference': ref,\n"
        "    'delta_alpha_vs_reference': d1,\n"
        "    'delta_alias': d2,\n"
        "    'delta_nscanon_vs_planckns': d3,\n"
        "}))\n"
    )  # (local)

    proc = subprocess.run(  # (local)
        [str(VENV_PYTHON), "-c", check_script],
        capture_output=True,
        text=True,
        cwd=str(SCRIPT_DIR),
        timeout=30,
    )
    out = {"returncode": proc.returncode,
           "stdout": proc.stdout,
           "stderr": proc.stderr,
           "parsed": None,
           "import_ok": False}  # (local)

    if proc.returncode == 0:
        out["import_ok"] = True
        for line in proc.stdout.splitlines():
            if line.startswith("SUBPROC_RESULT_JSON:"):
                out["parsed"] = json.loads(line[len("SUBPROC_RESULT_JSON:"):])
                break
    return out


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------


def main() -> int:
    t0 = time.time()  # (local)

    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pre_canonical_sha = sha256_of(CANONICAL_PATH)  # (local)
    print(f"  canonical_constants.py (PRE-PATCH): {pre_canonical_sha[:16]}...")
    script_path = Path(__file__).resolve()  # (local)
    print(f"  script (self):                      {sha256_of(script_path)[:16]}...")
    print()

    # 1. Read canonical_constants.py
    original_text = CANONICAL_PATH.read_text(encoding="utf-8")  # (local)
    original_len = len(original_text)  # (local)

    # 2. Apply patches (idempotent)
    new_text, applied = apply_patches(original_text)  # (local)
    any_anchor_missing = any(status == "anchor-not-found"  # (local)
                             for _, status in applied)

    if any_anchor_missing:
        print("ERROR: one or more patch anchors not found in canonical_constants.py")
        for pid, status in applied:
            print(f"  Patch {pid}: {status}")
        # Proceed to verdict emission with FAIL status (do NOT mutate the file).
        post_canonical_sha = pre_canonical_sha
        subproc = {"import_ok": False, "parsed": None, "stderr": "patch-anchor-missing"}  # (local)
        final_status = "FAIL"  # (local)
    else:
        # Write patched content only if different
        if new_text != original_text:
            CANONICAL_PATH.write_text(new_text, encoding="utf-8")
            print(f"Patched canonical_constants.py: {original_len} -> {len(new_text)} bytes")
        else:
            print("canonical_constants.py already fully patched (no-op)")

        post_canonical_sha = sha256_of(CANONICAL_PATH)  # (local)

        # 3. Subprocess re-import verification
        subproc = subprocess_reimport_check()
        print(f"\n=== subprocess re-import check (returncode={subproc['returncode']}) ===")
        if subproc["parsed"]:
            p = subproc["parsed"]
            print(f"  n_s_canon                   = {p['n_s_canon']}")
            print(f"  planck_ns                   = {p['planck_ns']}")
            print(f"  alpha_s_inflation_framework = {p['alpha_s_inflation_framework']}")
            print(f"  alpha_s_framework_central   = {p['alpha_s_framework_central']}")
            print(f"  reference (n_s_canon**2-1)  = {p['reference']}")
            print(f"  |alpha - ref|               = {p['delta_alpha_vs_reference']}")
            print(f"  |alias - main|              = {p['delta_alias']}")
            print(f"  |n_s_canon - planck_ns|     = {p['delta_nscanon_vs_planckns']}")
        else:
            print(f"  stderr: {subproc['stderr']}")

        # 4. Evaluate PASS/FAIL
        if (subproc["import_ok"]
                and subproc["parsed"] is not None
                and subproc["parsed"]["delta_alpha_vs_reference"] < REFERENCE_ALPHA_TOLERANCE
                and subproc["parsed"]["delta_alias"] < REFERENCE_ALPHA_TOLERANCE
                and subproc["parsed"]["delta_nscanon_vs_planckns"] < REFERENCE_ALPHA_TOLERANCE):
            final_status = "PASS"
        else:
            final_status = "FAIL"

    # 5. Compute dual-SHA on the POST-PATCH state
    pins = {
        "computations/_shared/canonical_constants.py": sha256_of(CANONICAL_PATH),
        # pre-patch hash kept as a distinct pin so auditors can reconstruct
        # the patch delta exactly.
        "computations/_shared/canonical_constants.py.pre_patch": pre_canonical_sha,
    }  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH, pins)
    print(f"\n  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    # 6. Emit value (number of patches successfully applied or already present)
    patches_ok = sum(1 for _, s in applied if s in ("applied", "already-present"))  # (local)
    value = patches_ok  # (local) expected 3

    # 7. Emit 4-tuple (final non-verdict line)
    four_tuple = (f"(value={value}_patches_landed, scheme={SCHEME}, "
                  f"convention={CONVENTION}, L_max={L_MAX})")  # (local)
    print("\n" + four_tuple)

    # 8. Append verdict (dual-SHA, S84+ schema)
    line = (
        f"{GATE_ID}: {final_status} -- value={value}_patches_landed "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)

    # 9. Persist JSON summary (for downstream W1c-2/4/5/6/7)
    summary = {
        "gate_id": GATE_ID,
        "status": final_status,
        "value": value,
        "applied": applied,
        "pre_canonical_sha256": pre_canonical_sha,
        "post_canonical_sha256": sha256_of(CANONICAL_PATH),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "subprocess_result": subproc,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "substitution_chain": {
            "step_1_definition": "alpha_s_inflation_framework := n_s_canon**2 - 1",
            "step_2_substitute": "0.9649**2 - 1",
            "step_3_simplify_ns_squared": 0.9649**2,
            "step_3_simplify_minus_one": 0.9649**2 - 1,
            "step_4_direction": "NEGATIVE (n_s < 1 => n_s^2 < 1 => value < 0)",
        },
    }  # (local)
    OUT_JSON.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {final_status} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
