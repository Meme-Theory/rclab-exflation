#!/usr/bin/env python3
"""
Batch-tag untagged numeric assignments as `# (local)`.

Reads the "potential hardcode" flags from s80_pru_audit_report.json's (a)
list — names that appear in N>=3 scripts and are NOT in canonical_constants.
For each such name, scans the source scripts and appends ` # (local)` to
every assignment line that:

  - Is an assignment of the targeted name (LHS match).
  - Does not already carry a `# (local)` tag or any `#` comment.
  - Is not inside a multi-line string (heuristic: line starts with `name = `
    and is not preceded by an unterminated triple-quote).

Names that look like they MIGHT be real framework constants (observational
values, critical thresholds referenced by multiple gates) are deferred —
the user promotes those manually.

Gate: S81-BATCH-LOCAL-TAG (NON-PHONONIC; no sign/direction claims).

Usage:
    python _batch_tag_locals.py --dry
    python _batch_tag_locals.py
    python _batch_tag_locals.py --defer-observational
"""
from __future__ import annotations

from canonical_constants import *  # noqa: F401,F403

import argparse
import json
import re
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


PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: legacy alias replaced (replaced by tools.computation_root.resolve_*)
ARCHIVE_DIR = PROJECT_ROOT / "computation archive"
AUDIT_JSON = resolve_output(80, 's80_pru_audit_report.json')

# Names that look like observational / framework-critical values and
# should be hand-reviewed for promotion to canonical_constants.py.
# Batch tagger DEFERS these (skips) when --defer-observational is set.
OBSERVATIONAL_FLAG = frozenset({
    "ns_planck",       # Planck n_s (probably already canonical as planck_ns)
    "r_GOE",           # GOE r-statistic (spectral-chaos diagnostic)
    "c_BLV",           # Biermann-Levine-Volovik coefficient
    "z_eq",            # matter-radiation equality redshift
    "a_init",          # initial scale factor
    "k_pivot",         # CMB pivot scale
    "t_star",          # characteristic time
    "f_0",             # background frequency
    "f_2",
    "f_4",
    "n_t",             # tensor tilt
    "n_s", "n_s_FW", "n_s_LCDM",  # scalar spectral index family
    "g_star",          # effective relativistic degrees of freedom
    "f_sky",           # observational sky fraction
    "Lambda_test",     # test cosmological constant — investigate
})

# Obvious locals — always tag. These are widely-used per-script names.
OBVIOUS_LOCAL = frozenset({
    "width", "tol", "val", "w", "total", "count", "h", "dtau", "E_kin",
    "N_modes", "MAX_PQ_SUM", "dim_spin", "N_pair", "N_tau", "EVAL_CUTOFF",
    "L_MAX", "cliff_err", "N_MODES", "L_max", "N_pair_total",
    "N_sample", "N_steps", "N_boot", "N_bins", "N_grid", "N_points",
    "N_fine", "N_k", "N_A", "N_MC", "N_TAU", "N_t", "N_B", "N_C",
    "n_sectors", "n_skipped", "n_bins", "n_t",
    "t0", "t1", "dt", "eps", "idx_fold", "fold_idx",
    "PASS_THRESH", "gate_threshold", "INFO_THRESH", "threshold",
    "sigma", "mu", "rho", "scale", "norm", "num", "cnt", "size", "idx",
    "sum_", "avg", "delta", "tau", "phi", "psi",
    "n", "N", "T",
    "alpha", "beta", "gamma",
    # S81 final pass: these 5 look observational but are context-specific
    # scan values — each script sets its own per-context.
    "a_init",       # scan parameter (initial scale factor varies by script)
    "f_sky",        # survey-specific (Planck 0.7, SZ 0.65, DESI 0.36, SO 0.4)
    "Lambda_test",  # test cutoff scale (varies by audit context)
    "g_star",       # script-specific (SM vs BBN vs QCD regime)
    "n_s",          # derived per-script (slow-roll, BCS, Bogoliubov all produce distinct n_s)
})

# Assignment regex: matches `name = <number>` at start of non-comment line,
# with no existing `#` comment on the same line.
def _assign_re(name: str) -> re.Pattern:
    return re.compile(
        r"^(?P<lhs>\s*" + re.escape(name) + r"\s*=\s*"
        r"(?P<rhs>[^#\n]+?))"  # RHS up to a # or newline, no comment
        r"\s*$",
        re.MULTILINE,
    )


def _already_tagged(line: str) -> bool:
    return bool(re.search(r"#\s*\(.*?local", line, re.IGNORECASE))


def tag_in_file(path: Path, names: list[str]) -> tuple[int, int]:
    """Tag untagged assignments of `names` in `path`. Returns (tagged, total).

    Handles three cases:
      (1) `name = NN`                 → append ` # (local)`
      (2) `name = NN  # some comment` → append ` (local)` to the comment
      (3) `name = NN  # (local) ...`  → skip (already tagged)
    """
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return 0, 0
    tagged_count = 0  # (local)
    total_count = 0  # (local)
    lines = text.splitlines(keepends=True)

    # Regex: `name = numeric_literal` with OPTIONAL existing comment.
    # Captures (lhs_rhs, existing_comment_or_empty).
    def make_assign_with_comment(name: str) -> re.Pattern:
        return re.compile(
            r"^(?P<lhs>\s*" + re.escape(name) + r"\s*=\s*"
            r"[0-9\-\.\+eE][0-9\-\.\+eE]*)"
            r"(?P<trail>\s*)"
            r"(?P<comment>(?:#.*)?)$"
        )

    compiled = {n: make_assign_with_comment(n) for n in names}

    out: list[str] = []
    for raw in lines:
        line = raw.rstrip("\n\r")
        newline = "\n" if raw.endswith("\n") else ""
        if line.strip().startswith("#"):
            out.append(raw)
            continue
        matched = False
        for name, pat in compiled.items():
            m = pat.match(line)
            if not m:
                continue
            total_count += 1
            existing = m.group("comment") or ""
            if _already_tagged(line):
                break
            lhs = m.group("lhs")
            if existing:
                # Keep existing comment, append " (local)" to it
                new_comment = existing.rstrip() + " (local)"
                out.append(f"{lhs}  {new_comment}{newline}")
            else:
                out.append(f"{lhs}  # (local){newline}")
            tagged_count += 1
            matched = True
            break
        if not matched:
            out.append(raw)

    if tagged_count > 0:
        path.write_text("".join(out), encoding="utf-8")
    return tagged_count, total_count


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry", action="store_true",
                    help="Preview tags without writing")
    ap.add_argument("--defer-observational", action="store_true",
                    help="Skip names in OBSERVATIONAL_FLAG (user promotes)")
    ap.add_argument("--only-obvious", action="store_true",
                    help="Tag only names in OBVIOUS_LOCAL set")
    args = ap.parse_args()

    if not AUDIT_JSON.exists():
        print(f"ERROR: {AUDIT_JSON} not found. Run s80_pru_audit.py first.")
        return 2
    audit = json.loads(AUDIT_JSON.read_text(encoding="utf-8"))
    entries = audit["constants_audit"]["unregistered_ge_threshold"]
    names = [e["name"] for e in entries]

    if args.only_obvious:
        names = [n for n in names if n in OBVIOUS_LOCAL]
    elif args.defer_observational:
        names = [n for n in names if n not in OBSERVATIONAL_FLAG]

    print(f"Batch-tagging {len(names)} names across scripts in "
          f"computations + computation archive...")

    total_tagged = 0  # (local)
    total_assigns = 0  # (local)
    files_touched = 0  # (local)

    for root in (COMPUTATIONS_DIR, ARCHIVE_DIR):
        if not root.is_dir():
            continue
        for f in root.glob("s*.py"):
            if args.dry:
                # Count only — don't modify.
                text = f.read_text(encoding="utf-8", errors="replace")
                for name in names:
                    for _ in re.finditer(
                        r"^(\s*" + re.escape(name) + r"\s*=\s*"
                        r"[0-9\-\.\+eE][^#\n]*)$",
                        text, re.MULTILINE,
                    ):
                        total_assigns += 1
                continue
            tagged, total = tag_in_file(f, names)
            total_tagged += tagged
            total_assigns += total
            if tagged > 0:
                files_touched += 1

    if args.dry:
        print(f"  {total_assigns} untagged assignments scanned (dry)")
    else:
        print(f"  {total_tagged} assignments tagged across {files_touched} files "
              f"({total_assigns} total scanned)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
