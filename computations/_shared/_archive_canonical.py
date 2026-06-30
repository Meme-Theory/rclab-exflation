#!/usr/bin/env python3
"""
_archive_canonical.py — Canonical constants byte-freeze archival (S84 W9a-101)
================================================================================

Purpose: At session close, freeze the byte-content of canonical_constants.py as
canonical_constants_s{N}_frozen.py so that S{N+1}+ can reconstruct any S{N}
verdict's audit_sha256 by re-running the producing script against the frozen
canonical and frozen pin-map.

Substitution chain (why the freeze is mandatory):
  Def 1: audit_sha256(g) = sha256( script_bytes || canonical_bytes_at_freeze
                                   || pinmap_bytes )
  Def 2: In S{N+1}+, canonical_bytes(current) may != canonical_bytes_at_S{N}_freeze
         (canonical evolves in place).
  Def 3: reconstructibility(g, t) = 1 iff every byte-string needed to recompute
         audit_sha256(g) is accessible at time t.
  => reconstructibility(S{N} g, S{N+1}+ t) = 1 iff canonical_bytes_at_S{N}_freeze
     is accessible at t, which requires a byte-copy persisted BEFORE S{N+1}
     edits canonical in place.
  Direction: without freeze, audit_sha256 becomes a one-way function in time.
  Conclusion: byte-freeze at session close is NECESSARY for long-horizon audit.

Machinery pins (PRDR):
  FROZEN_FILENAME_FORMAT : "canonical_constants_s{N}_frozen.py"
  FREEZE_TIMESTAMP_FORMAT: ISO-8601 UTC
  SENTINEL_MARKER        : "# FROZEN EOF"
  ROUND_TRIP_TOLERANCE   : exact byte-match (zero tolerance on source body)

Usage:
  python _archive_canonical.py --session 84 [--source PATH] [--out-dir DIR]
                               [--smoke-test] [--dry-run]
"""

from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
import os
import shutil
import sys
import tempfile
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


# --- PRDR pins (plan §W9a-101) ------------------------------------------------
FROZEN_FILENAME_FORMAT = "canonical_constants_s{N}_frozen.py"  # (local)
SENTINEL_MARKER = "# FROZEN EOF"                               # (local)
# FREEZE_TIMESTAMP_FORMAT is ISO-8601 UTC (Zulu); enforced below.

# --- Paths --------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent           # (local)
# X2-removed: legacy alias replaced (replaced by tools.computation_root.resolve_*)
DEFAULT_SOURCE = resolve_script(None, 'canonical_constants.py')           # (local)


# --- Byte utilities -----------------------------------------------------------
def sha256_bytes(b: bytes) -> str:
    """SHA-256 hex digest of a byte-string."""
    h = hashlib.sha256()  # (local)
    h.update(b)
    return h.hexdigest()


def sha256_of_path(p: Path) -> str:
    """SHA-256 of a file's bytes."""
    return sha256_bytes(p.read_bytes())


# --- Header construction ------------------------------------------------------
def build_frozen_header(session: int, source_sha: str, iso_timestamp: str) -> str:
    """Docstring block prepended to the frozen file."""
    return (
        f'"""\n'
        f"canonical_constants snapshot: Session {session}\n"
        f"Frozen: {iso_timestamp}\n"
        f"Source SHA-256: {source_sha}\n"
        f"Purpose: enables S{session + 1}+ audit_sha256 reconstruction of "
        f"S{session} verdicts.\n"
        f"DO NOT EDIT. For S{session + 1}+ constants, edit canonical_constants.py "
        f"in place\n"
        f"and create canonical_constants_s{session + 1}_frozen.py at S{session + 1} "
        f"close.\n"
        f'"""\n'
    )


# --- Freeze core --------------------------------------------------------------
def freeze(source: Path, frozen_path: Path, session: int,
           iso_timestamp: str | None = None) -> dict:
    """Freeze `source` to `frozen_path`; return the archival JSON record.

    Layout of the frozen file:
      [FROZEN_HEADER]            <- prepended docstring (timestamp + source SHA)
      [SOURCE_BYTES verbatim]    <- byte-exact copy of source
      [SENTINEL_MARKER]          <- "# FROZEN EOF" on its own line

    Round-trip verification: SHA-256 of the SOURCE_BYTES region (extracted from
    the frozen file by stripping header + sentinel) must equal source SHA.
    """
    if not source.is_file():
        raise FileNotFoundError(f"source not found: {source}")

    source_bytes = source.read_bytes()                              # (local)
    source_sha = sha256_bytes(source_bytes)                         # (local)

    if iso_timestamp is None:
        iso_timestamp = _dt.datetime.now(_dt.timezone.utc).strftime(
            "%Y-%m-%dT%H:%M:%SZ")                                   # (local)

    header = build_frozen_header(session, source_sha, iso_timestamp).encode("utf-8")  # (local)
    sentinel = f"\n{SENTINEL_MARKER}\n".encode("utf-8")             # (local)

    frozen_path.parent.mkdir(parents=True, exist_ok=True)
    # Atomic-ish: write to temp in same dir then rename.
    tmp = frozen_path.with_suffix(frozen_path.suffix + ".tmp")       # (local)
    with tmp.open("wb") as fp:
        fp.write(header)
        fp.write(source_bytes)
        fp.write(sentinel)
    os.replace(tmp, frozen_path)

    # Round-trip: re-extract source body by stripping header + sentinel,
    # then recompute SHA and compare.
    round_trip_sha = _extract_body_sha(frozen_path, header, sentinel)  # (local)
    if round_trip_sha != source_sha:
        frozen_path.unlink(missing_ok=True)
        raise RuntimeError(
            f"round-trip SHA mismatch: source={source_sha} "
            f"extracted={round_trip_sha}"
        )

    try:
        frozen_rel = str(frozen_path.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
    except ValueError:
        # smoke-test / off-project paths: emit absolute form
        frozen_rel = str(frozen_path).replace("\\", "/")                            # (local)
    record = {
        "session": session,
        "source_sha256": source_sha,
        "frozen_path": frozen_rel,
        "frozen_at": iso_timestamp,
        "round_trip_sha256": round_trip_sha,
        "sentinel": SENTINEL_MARKER,
    }
    return record


def _extract_body_sha(frozen_path: Path, header: bytes, sentinel: bytes) -> str:
    """SHA-256 of the frozen-file body with header + sentinel stripped."""
    buf = frozen_path.read_bytes()                                  # (local)
    if not buf.startswith(header):
        raise RuntimeError("frozen file does not begin with expected header")
    if not buf.endswith(sentinel):
        raise RuntimeError("frozen file does not end with expected sentinel")
    body = buf[len(header):-len(sentinel)]                          # (local)
    return sha256_bytes(body)


# --- Smoke test ---------------------------------------------------------------
def smoke_test() -> tuple[bool, dict]:
    """Run the archival script against a stub canonical file in tmp.

    Returns (pass_bool, smoke_record). PASS iff the stub round-trips, the JSON
    record is well-formed, and the recorded SHA equals the stub's SHA.
    """
    with tempfile.TemporaryDirectory() as td:
        td_path = Path(td)                                          # (local)
        stub = td_path / "canonical_constants.py"                   # (local)
        # Non-trivial stub: header, constants, footer — exercises byte copy.
        stub_text = (
            "#!/usr/bin/env python3\n"
            '"""Stub canonical for smoke test."""\n'
            "from math import pi\n"
            "M_KK = 1.234e4  # GeV (stub)\n"
            "tau_fold = 0.190  # dimensionless (stub)\n"
            "Delta_BCS = 3.14e-3  # GeV (stub)\n"
            "_SENTINEL_NOT_FROZEN = True\n"
            "print('stub-canonical-loaded')\n"
        )
        stub.write_bytes(stub_text.encode("utf-8"))
        stub_sha = sha256_of_path(stub)                             # (local)

        frozen = td_path / "canonical_constants_s99_frozen.py"      # (local)
        record = freeze(stub, frozen, session=99,
                        iso_timestamp="2026-04-19T00:00:00Z")

        # Checks
        checks = {
            "frozen_exists": frozen.is_file(),
            "frozen_size_gt_stub": frozen.stat().st_size > len(stub_text.encode("utf-8")),
            "record_source_sha_matches_stub": record["source_sha256"] == stub_sha,
            "record_round_trip_matches_source": (
                record["round_trip_sha256"] == record["source_sha256"]
            ),
            "record_has_session": record["session"] == 99,
            "record_has_frozen_path": "canonical_constants_s99_frozen.py" in record["frozen_path"],
            "record_has_iso_timestamp": record["frozen_at"].endswith("Z"),
            "record_has_sentinel": record["sentinel"] == SENTINEL_MARKER,
            "frozen_ends_with_sentinel": frozen.read_bytes().endswith(
                f"\n{SENTINEL_MARKER}\n".encode("utf-8")),
            "header_contains_source_sha": stub_sha in frozen.read_text(encoding="utf-8"),
        }
        smoke_rec = {
            "stub_sha256": stub_sha,
            "record": record,
            "checks": checks,
        }
        return all(checks.values()), smoke_rec


# --- CLI ---------------------------------------------------------------------
def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Byte-freeze canonical_constants.py.")
    ap.add_argument("--session", type=int, help="session number N")
    ap.add_argument("--source", type=Path, default=DEFAULT_SOURCE,
                    help="path to canonical_constants.py (default: computations/_shared/)")
    ap.add_argument("--out-dir", type=Path, default=COMPUTATIONS_DIR,
                    help="directory to write frozen file (default: computations/_shared/)")
    ap.add_argument("--smoke-test", action="store_true",
                    help="run smoke test (tmp stub); do NOT touch canonical")
    ap.add_argument("--dry-run", action="store_true",
                    help="compute SHA + record only; do not write frozen file")
    args = ap.parse_args(argv)

    if args.smoke_test:
        ok, smoke_rec = smoke_test()
        print(json.dumps(smoke_rec, indent=2, sort_keys=True))
        print(f"\nSMOKE_TEST: {'PASS' if ok else 'FAIL'}")
        return 0 if ok else 1

    if args.session is None:
        print("error: --session is required for real freeze (use --smoke-test to test)",
              file=sys.stderr)
        return 2

    frozen_name = FROZEN_FILENAME_FORMAT.format(N=args.session)     # (local)
    frozen_path = args.out_dir / frozen_name                        # (local)

    if args.dry_run:
        src_sha = sha256_of_path(args.source)                       # (local)
        iso = _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")  # (local)
        print(json.dumps({
            "dry_run": True,
            "session": args.session,
            "source": str(args.source),
            "source_sha256": src_sha,
            "would_write": str(frozen_path),
            "would_stamp": iso,
        }, indent=2, sort_keys=True))
        return 0

    record = freeze(args.source, frozen_path, session=args.session)
    print(json.dumps(record, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
