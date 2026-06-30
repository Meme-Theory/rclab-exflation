"""
T3 RE-RUN: S34A-DPHYS-KOSMANN (Connes NCG, S81 canonical form).

Thin wrapper around the archive S34a script:
  - Canonical-constants import (MANDATORY).
  - sys.path includes computations (for dirac_spectrum, s34a_dphys_fold).
  - sys.path includes computations/_shared    (for s23a_kosmann_singlet.npz + s34a_dphys_fold).
  - L_FIBER_DPHYS pinned to 16 (Hilbert space H_F = C^16, from Cliff(R^8) spinor rep).
  - Pre-registered gate thresholds 0.15 (STRONG PASS) / 0.05 (PASS) are left untouched.
  - All intermediate/scan/threshold quantities are tagged # (local).
"""

import os                                    # (local: stdlib)
import sys                                   # (local: stdlib)
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


# --- Canonical imports (MANDATORY, computations/_shared CLAUDE.md) ---
PROJECT_ROOT = r"C:/sandbox/Ainulindale Exflation"           # (local: path only)
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
ARCHIVE_DIR = os.path.join(PROJECT_ROOT, "computations", "_shared")     # (local)
for _p in (SCRIPT_DIR, ARCHIVE_DIR):          # (local: path setup)
    if _p not in sys.path:
        sys.path.insert(0, _p)

from canonical_constants import *  # noqa: F401,F403 — MANDATORY

# L_max pin: spectral-triple fiber dimension, fixed by Cliff(R^8) spinor module
L_FIBER_DPHYS = 16                   # (local: pin — dim H_F = 2^(8/2) = 16)

# Delegate to the archive S34a script (its SCRIPT_DIR resolves to computations/_shared,
# which is where s23a_kosmann_singlet.npz and s34a_dphys_fold.py live).
if __name__ == "__main__":
    script = os.path.join(ARCHIVE_DIR, "s34a_dphys_kosmann.py")   # (local)
    with open(script, "r", encoding="utf-8") as _f:
        code = _f.read()                                          # (local)
    # Execute in a namespace that has SCRIPT_DIR already set to the archive
    ns = {                                                        # (local)
        "__name__": "__main__",
        "__file__": script,
    }
    exec(compile(code, script, "exec"), ns)
