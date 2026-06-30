"""Scan every session NPZ file for embedded pre-migration path strings.

The text-search audit pipeline cannot see strings serialized inside numpy
arrays (npz is a binary ZIP of .npy arrays). This scanner loads each file
via numpy and walks every key whose dtype is string-bearing, testing
values against the stale-path pattern set.

Default: scan-only, JSON report, no mutation.
With --patch: rewrites affected NPZ files in place after creating a
`.pre_scrub.bak` backup. WARNING: patching changes content_sha256 of the
file, which invalidates any verdict-line or canonical_sha_ledger.json
audit pin referencing the old SHA. Only patch when SHA-invalidation is
acceptable; for audit-pinned files, regenerate from the producing
script instead.
"""
import sys
import json
import re
import argparse
import shutil
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import *  # noqa: F401, F403 — rule compliance (S34+)

PROJECT_ROOT = Path(__file__).resolve().parents[2]
NPZ_GLOB_ROOTS = [
    PROJECT_ROOT / "computations",
]

# Match the stale prefix; suffix is then read as a path-component to decide
# session-vs-shared routing (verified against actual filesystem 2026-05-04).
STALE_PREFIX_RE = re.compile(r"tier[01][-_]?(?:computation|archive)/")
PATH_SUFFIX_RE = re.compile(r"[A-Za-z0-9_.\-]+")
SESSION_FILE_RE = re.compile(r"^s(\d+)_")

# Pattern label for the report (single canonical pattern; no longer multiple)
STALE_PATTERNS = [(STALE_PREFIX_RE, "computations/session-{N}/ or _shared/")]


def remap_suffix(suffix):
    """Map a path suffix to its canonical destination subdirectory.

    Rule (verified 2026-05-04 against filesystem):
      - 'sNN_<rest>' (session-prefixed file) -> 'computations/session-{int(NN)}/<suffix>'
      - everything else (canonical_constants.py, _shared infrastructure)
        -> 'computations/_shared/<suffix>'
    """
    sess_match = SESSION_FILE_RE.match(suffix)
    if sess_match:
        return f"computations/session-{int(sess_match.group(1))}/{suffix}"
    return f"computations/_shared/{suffix}"


def substitute_stale_paths(s):
    """Walk a string, replacing every stale-prefix occurrence with the canonical form."""
    out = []
    pos = 0                 # (local)
    for m in STALE_PREFIX_RE.finditer(s):
        out.append(s[pos:m.start()])
        end = m.end()
        suffix_match = PATH_SUFFIX_RE.match(s[end:])
        if not suffix_match:
            # No path-suffix -- leave the matched prefix alone (defensive)
            out.append(s[m.start():m.end()])
            pos = m.end()
            continue
        suffix = suffix_match.group(0)
        out.append(remap_suffix(suffix))
        pos = end + len(suffix)
    out.append(s[pos:])
    return "".join(out)


def find_npz_files(roots):
    for root in roots:
        if not root.exists():
            continue
        yield from sorted(root.rglob("*.npz"))


def extract_strings(arr):
    """Yield (flat_index, string_value) for every string-bearing element."""
    if arr.dtype.kind in ("U", "S"):
        flat = arr.ravel()
        for i, v in enumerate(flat):
            yield i, v.decode("utf-8", "replace") if isinstance(v, bytes) else str(v)
    elif arr.dtype == object:
        flat = arr.ravel()
        for i, v in enumerate(flat):
            if isinstance(v, (str, bytes)):
                yield i, v.decode("utf-8", "replace") if isinstance(v, bytes) else v


def detect_hits(npz_path):
    """Return (hits, errors) for one NPZ file. Read-only."""
    hits = []
    errors = []
    try:
        data = np.load(npz_path, allow_pickle=True)
    except Exception as e:
        return [], [{"file": str(npz_path.relative_to(PROJECT_ROOT)), "error": f"load_failed: {e}"}]
    try:
        for key in data.files:
            try:
                arr = data[key]
            except Exception as e:
                errors.append({"file": str(npz_path.relative_to(PROJECT_ROOT)), "key": key, "error": str(e)})
                continue
            if not hasattr(arr, "dtype"):
                continue
            for idx, s in extract_strings(arr):
                for pat, _ in STALE_PATTERNS:
                    m = pat.search(s)
                    if m:
                        excerpt = s if len(s) <= 240 else s[:240] + "…"
                        hits.append({
                            "file": str(npz_path.relative_to(PROJECT_ROOT)).replace("\\", "/"),
                            "key": key,
                            "index": idx,
                            "pattern": pat.pattern,
                            "match_pos": m.start(),
                            "excerpt": excerpt,
                        })
                        break
    finally:
        data.close()
    return hits, errors


def patch_file(npz_path):
    """Rewrite npz with stale strings substituted. Returns (n_strings_patched, keys_touched)."""
    with np.load(npz_path, allow_pickle=True) as data:
        store = {k: np.array(data[k], copy=True) for k in data.files}

    n_patched = 0           # (local)
    keys_touched = set()
    for key, arr in store.items():
        if not hasattr(arr, "dtype"):
            continue
        if arr.dtype.kind in ("U", "S"):
            flat = arr.ravel()
            is_bytes = arr.dtype.kind == "S"
            for i, v in enumerate(flat):
                v_str = v.decode("utf-8", "replace") if isinstance(v, bytes) else str(v)
                v_new = substitute_stale_paths(v_str)
                if v_new != v_str:
                    flat[i] = v_new.encode("utf-8") if is_bytes else v_new
                    n_patched += 1
                    keys_touched.add(key)
        elif arr.dtype == object:
            flat = arr.ravel()
            for i, v in enumerate(flat):
                if isinstance(v, (str, bytes)):
                    v_str = v.decode("utf-8", "replace") if isinstance(v, bytes) else v
                    v_new = substitute_stale_paths(v_str)
                    if v_new != v_str:
                        flat[i] = v_new
                        n_patched += 1
                        keys_touched.add(key)

    if n_patched > 0:
        backup = npz_path.with_suffix(npz_path.suffix + ".pre_scrub.bak")
        if not backup.exists():
            shutil.copy2(npz_path, backup)
        np.savez_compressed(npz_path, **store)

    return n_patched, sorted(keys_touched)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--patch", action="store_true",
                        help="Rewrite NPZ files in place (creates .pre_scrub.bak); "
                             "WARNING: invalidates content_sha256 pins.")
    parser.add_argument("--json", default=None, help="Write structured report to this path")
    parser.add_argument("--max-files", type=int, default=None, help="Stop after N files (testing)")
    parser.add_argument("--quiet", action="store_true", help="Suppress per-file lines")
    args = parser.parse_args()

    n_scanned = 0           # (local)
    n_hit_files = 0         # (local)
    n_total_hits = 0        # (local)
    n_patched_files = 0     # (local)
    n_patched_strings = 0   # (local)
    n_load_errors = 0       # (local)
    all_hits = []
    all_errors = []
    patch_log = []

    for npz_path in find_npz_files(NPZ_GLOB_ROOTS):
        if args.max_files and n_scanned >= args.max_files:
            break
        n_scanned += 1
        hits, errors = detect_hits(npz_path)
        all_errors.extend(errors)
        if errors:
            n_load_errors += len([e for e in errors if "load_failed" in e.get("error", "")])
        if hits:
            n_hit_files += 1
            n_total_hits += len(hits)
            all_hits.extend(hits)
            if not args.quiet:
                rel = npz_path.relative_to(PROJECT_ROOT)
                print(f"  HIT: {str(rel).replace(chr(92), '/')} -- {len(hits)} string(s) match")
            if args.patch:
                n_p, keys = patch_file(npz_path)
                if n_p > 0:
                    n_patched_files += 1
                    n_patched_strings += n_p
                    patch_log.append({
                        "file": str(npz_path.relative_to(PROJECT_ROOT)).replace("\\", "/"),
                        "strings_patched": n_p,
                        "keys": keys,
                    })
                    if not args.quiet:
                        print(f"    PATCHED: {n_p} string(s) in keys {keys}")

    print()
    print("=" * 60)
    print(f"NPZ files scanned: {n_scanned}")
    print(f"Files with stale-path hits: {n_hit_files}")
    print(f"Total stale-path string hits: {n_total_hits}")
    print(f"Load errors: {n_load_errors}")
    if args.patch:
        print(f"Files patched: {n_patched_files}")
        print(f"Strings patched: {n_patched_strings}")
    else:
        print("[scan-only mode -- run with --patch to mutate]")

    if args.json:
        report = {
            "mode": "patch" if args.patch else "scan",
            "n_files_scanned": n_scanned,
            "n_hit_files": n_hit_files,
            "n_total_hits": n_total_hits,
            "n_patched_files": n_patched_files,
            "n_patched_strings": n_patched_strings,
            "patterns": [{"regex": p.pattern, "replacement": r} for p, r in STALE_PATTERNS],
            "hits": all_hits,
            "errors": all_errors,
            "patch_log": patch_log,
        }
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)
        print(f"Report written to: {args.json}")


if __name__ == "__main__":
    main()
