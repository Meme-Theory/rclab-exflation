#!/usr/bin/env python3
"""
Batch migrator for scripts that don't need per-script adjudication.

Applies the migrate pattern mechanically to every matching script:
  1. Add `from canonical_constants import *` if missing.
  2. Compute SHA-256 of script + every .npz / .npy / .h5 input it loads.
  3. Append a one-line "migrate-only" verdict line to
     `computations/session-81/s81_batch_migrations.txt`:
     `MIGRATE-<SCRIPT-TAG>: INFO -- value=MIGRATED scheme=batch-canonical-hygiene convention=no-run-no-gate L_max=NA sha256=<closure>`

This is explicitly NOT a re-run — the script is not executed. The closure
SHA is over the input-pin map, NOT a reproduced result. The INFO verdict
records the pin surface only; a later pass can convert to PASS/FAIL with
a real run if the script turns out to inform a gate after all.

Gate: S81-BATCH-MIGRATE (NON-PHONONIC, infrastructure).

Usage:
    python _batch_migrate.py --scan computations --sessions 7-18 --dry
    python _batch_migrate.py --scan computations --sessions 7-18
    python _batch_migrate.py --scan computations --sessions 7-18 --write-imports
"""
from __future__ import annotations

from canonical_constants import *  # noqa: F401,F403

import argparse
import hashlib
import json
import re
import sys
from collections import OrderedDict
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
from computation_root import resolve_script, resolve_output, resolve_glob, resolve_dynamic, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===


PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'COMPUTATIONS_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
COMPUTATIONS_DIR = PROJECT_ROOT / "computations" / "_shared"
OUT_FILE = resolve_output(81, 's81_batch_gate_verdicts.txt')

# Regex: script filename pattern sN_something.py or sNa_something.py
RE_SESSION_SCRIPT = re.compile(r"^s(\d+)([a-z]?)_([A-Za-z0-9_]+)\.py$")

# Regex: canonical import already present
RE_HAS_CANON_IMPORT = re.compile(
    r"^\s*from\s+canonical_constants\s+import\s+",
    re.MULTILINE,
)

# Regex: load-input patterns (np.load, h5py.File, etc.) — capture the
# filename argument when it's a single string literal.
RE_NP_LOAD = re.compile(
    r"np\.load\(\s*['\"]([^'\"]+)['\"]",
)
RE_H5_OPEN = re.compile(
    r"h5py\.File\(\s*['\"]([^'\"]+)['\"]",
)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def find_input_files(script_path: Path, script_dir: Path) -> list[Path]:
    """Return the set of SHA-pinnable input files the script loads."""
    try:
        text = script_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []
    candidates: list[str] = []
    candidates.extend(RE_NP_LOAD.findall(text))
    candidates.extend(RE_H5_OPEN.findall(text))
    files: list[Path] = []
    seen: set[str] = set()
    for c in candidates:
        # Allow only simple .npz/.npy/.h5 basenames or relative paths;
        # skip anything with f-strings or formatted paths.
        if "{" in c or "%" in c:
            continue
        candidate_paths = [
            script_dir / c,
            ARCHIVE_DIR / Path(c).name,
            resolve_dynamic(Path(c).name),
        ]
        for p in candidate_paths:
            if p.exists() and p.suffix in (".npz", ".npy", ".h5", ".hdf5"):
                if str(p) not in seen:
                    files.append(p)
                    seen.add(str(p))
                break
    return files


def closure_sha(pin_map: dict[str, str]) -> str:
    """SHA-256 of the JSON-serialized sorted pin map."""
    blob = json.dumps(pin_map, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(blob).hexdigest()


def script_tag(script_path: Path) -> str | None:
    """Return the verdict-line tag (upper-case, hyphens) or None."""
    m = RE_SESSION_SCRIPT.match(script_path.name)
    if not m:
        return None
    ses = f"S{m.group(1)}{m.group(2).upper()}"
    rest = m.group(3).upper().replace("_", "-")
    return f"{ses}-{rest}"


def migrate_one(script_path: Path, write_imports: bool) -> dict | None:
    """Compute pin map + verdict line for one script. Returns dict or None."""
    tag = script_tag(script_path)
    if tag is None:
        return None
    script_dir = script_path.parent
    try:
        text = script_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    has_import = bool(RE_HAS_CANON_IMPORT.search(text))

    # Optionally add the canonical import line (only if write_imports and
    # the file is in computations)
    import_added = False
    if write_imports and not has_import:
        # Insert after the module docstring / existing imports. Simple
        # heuristic: find the first blank line after the first import; if
        # none, insert at the top after any shebang / docstring.
        lines = text.splitlines(keepends=True)
        insert_at = 0  # (local) position before insertion scan
        if lines and lines[0].startswith("#!"):
            insert_at = 1  # (local) skip shebang
        # Skip module docstring
        if insert_at < len(lines) and lines[insert_at].lstrip().startswith(
                ('"""', "'''")):
            # Advance until the docstring closes
            quote = lines[insert_at].lstrip()[:3]
            insert_at += 1
            while insert_at < len(lines):
                if quote in lines[insert_at]:
                    insert_at += 1
                    break
                insert_at += 1
        new_line = ("from canonical_constants import *  # noqa: F401,F403 "
                    "(batch migration)\n")
        new_lines = lines[:insert_at] + [new_line] + lines[insert_at:]
        try:
            script_path.write_text("".join(new_lines), encoding="utf-8")
            import_added = True
            text = "".join(new_lines)
        except OSError as e:
            print(f"WARN: could not write import to {script_path.name}: {e}")

    # SHA pins
    script_sha = sha256_file(script_path)
    canon_py = resolve_script(None, 'canonical_constants.py')
    canon_sha = sha256_file(canon_py) if canon_py.exists() else ""
    input_files = find_input_files(script_path, script_dir)
    pin_map = OrderedDict()
    pin_map["script"] = script_sha
    if canon_sha:
        pin_map["canonical_constants.py"] = canon_sha
    for p in input_files:
        pin_map[p.name] = sha256_file(p)
    closure = closure_sha(pin_map)

    return {
        "tag": tag,
        "gate_id": f"MIGRATE-BATCH-{tag}",
        "script_path": str(script_path.relative_to(PROJECT_ROOT)),
        "script_sha": script_sha,
        "canon_sha": canon_sha,
        "inputs": [(p.name, pin_map[p.name]) for p in input_files],
        "closure": closure,
        "has_canon_import": has_import or import_added,
        "import_added": import_added,
    }


def _scan_dir(root: Path, sess_lo: int, sess_hi: int) -> list[Path]:
    out: list[Path] = []
    if not root.is_dir():
        return out
    for f in sorted(root.glob("s*.py")):
        m = RE_SESSION_SCRIPT.match(f.name)
        if m:
            sess = int(m.group(1))
            if sess_lo <= sess <= sess_hi:
                out.append(f)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--scan", required=True,
                    choices=["computations"])
    ap.add_argument("--sessions", required=True,
                    help="Session range like '7-18' or '34-51'")
    ap.add_argument("--write-imports", action="store_true",
                    help="Add 'from canonical_constants import *' if missing")
    ap.add_argument("--dry", action="store_true",
                    help="Preview migration without writing outputs")
    ap.add_argument("--only-cited", action="store_true",
                    help="Only migrate scripts cited in gates.data_files")
    args = ap.parse_args()

    m = re.match(r"(\d+)-(\d+)$", args.sessions)
    if not m:
        print("ERROR: --sessions must be like '7-18'", file=sys.stderr)
        return 2
    lo, hi = int(m.group(1)), int(m.group(2))

    roots = []
    if args.scan == "computations":
        roots.append(COMPUTATIONS_DIR)

    scripts: list[Path] = []
    for r in roots:
        scripts.extend(_scan_dir(r, lo, hi))

    if args.only_cited:
        # Load knowledge.db and filter
        import sqlite3
        dbp = PROJECT_ROOT / "tools" / "knowledge.db"
        cited: set[str] = set()
        if dbp.exists():
            conn = sqlite3.connect(str(dbp))
            cur = conn.cursor()
            cur.execute("SELECT data_files FROM gates WHERE data_files!=''")
            for (df,) in cur.fetchall():
                for tok in re.split(r"[,\s]+", df or ""):
                    if tok.endswith(".py"):
                        cited.add(tok)
            conn.close()
        scripts = [p for p in scripts if p.name in cited]
        print(f"--only-cited filter: {len(scripts)} scripts remain.")

    print(f"Scanning {len(scripts)} script(s) in S{lo}-S{hi}...")
    results: list[dict] = []
    for p in scripts:
        r = migrate_one(p, args.write_imports and not args.dry)
        if r is None:
            continue
        results.append(r)

    with_import = sum(1 for r in results if r["has_canon_import"])
    imports_added = sum(1 for r in results if r["import_added"])
    print(f"  with canonical import: {with_import}/{len(results)}")
    if args.write_imports:
        print(f"  imports added this run: {imports_added}")

    if args.dry:
        print("\n--- dry-run: first 15 verdict lines ---")
        for r in results[:15]:
            print(
                f"{r['gate_id']}: INFO -- value=MIGRATED "
                f"scheme=batch-canonical-hygiene convention=no-run-no-gate "
                f"L_max=NA sha256={r['closure']}"
            )
        return 0

    if not results:
        print("Nothing to write.")
        return 0

    # Append to the batch migrations log (not s81_gate_verdicts.txt)
    lines = [
        f"## S81 Batch Migrations (S{lo}-S{hi}, scan={args.scan})\n",
        "## Each line pins the script + its npz/npy/h5 inputs + canonical_constants.\n",
        "## INFO verdict = migration recorded, script NOT re-run. Gate-informing\n",
        "## scripts should be promoted to a full re-run separately.\n\n",
    ]
    for r in results:
        lines.append(
            f"{r['gate_id']}: INFO -- value=MIGRATED "
            f"scheme=batch-canonical-hygiene convention=no-run-no-gate "
            f"L_max=NA sha256={r['closure']}\n"
        )
        # Comment lines with input detail
        lines.append(f"  # script: {r['script_path']}\n")
        lines.append(f"  # script_sha: {r['script_sha']}\n")
        lines.append(f"  # canon_sha:  {r['canon_sha']}\n")
        for name, sha in r["inputs"]:
            lines.append(f"  # input: {name} {sha}\n")

    mode = "a" if OUT_FILE.exists() else "w"
    with OUT_FILE.open(mode, encoding="utf-8") as f:
        f.write("".join(lines))
    print(f"\nAppended {len(results)} migration line(s) to {OUT_FILE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
