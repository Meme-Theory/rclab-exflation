"""tools/_install_computation_roots_table.py — additive schema migration for Phase 1.

Adds the `computation_roots` table to tools/knowledge.db. Idempotent: re-running
is safe (CREATE TABLE IF NOT EXISTS, INSERT OR IGNORE). Fully additive: no
existing tables modified, no rows changed in any other table.

Default state after install:
  +------------------+-----------+
  | root_name        | is_active |
  +------------------+-----------+
  | computations/_shared| 1         |
  | computations     | 0         |
  +------------------+-----------+

Rollback impact: 'DROP TABLE computation_roots;' restores the pre-install
schema with zero impact on extracted entities, FTS5 indices, or any consumer
that doesn't explicitly query this new table.

Usage:
    python tools/_install_computation_roots_table.py            # install (default)
    python tools/_install_computation_roots_table.py --check    # show table state
    python tools/_install_computation_roots_table.py --rollback # DROP TABLE (requires --yes)

Safety properties (load-bearing for the user's "minimum knowledgebase touch"
constraint):
  1. Pure additive: no ALTER TABLE on existing tables; only CREATE TABLE.
  2. Idempotent: re-running the install is a no-op.
  3. Reversible: --rollback drops the table; the rest of the database is
     untouched.
  4. The table is NOT YET QUERIED by any consumer; tools/computation_root.py
     reads its active_root from JSON, not from this table. The table exists
     for forward use by the eventual MCP wrapper / extract_entities.py
     root-awareness changes (Phase 1.3 / 1.4 deferred).
"""

from __future__ import annotations

import argparse
import pathlib
import sqlite3
import sys


PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
DB_PATH = PROJECT_ROOT / "tools" / "knowledge.db"

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS computation_roots (
    id            INTEGER PRIMARY KEY,
    root_name     TEXT    NOT NULL UNIQUE,
    is_active     INTEGER NOT NULL DEFAULT 0,
    registered_at TEXT    NOT NULL DEFAULT (datetime('now')),
    notes         TEXT
);
"""

# Use INSERT OR IGNORE so re-running install is a no-op; an existing row
# (e.g., one whose is_active was flipped manually for testing) is preserved.
SEED_INSERTS = [
    (
        "computations/_shared",
        1,
        "Live canonical root; default at install time. Flat layout under "
        "project_root/computations/. All S34+ scripts import "
        "canonical_constants from here.",
    ),
    (
        "computations",
        0,
        "Parallel mirror; pending validation per S88+ rigging plan. Layout: "
        "project_root/computations/session-N/ + project_root/computations/"
        "_shared/. Activated by setting is_active=1 here AND/OR setting "
        "active_root='computations' in tools/computation_root.json AND/OR "
        "setting env var COMPUTATION_ROOT=computations.",
    ),
]


def _connect() -> sqlite3.Connection:
    if not DB_PATH.exists():
        sys.stderr.write(
            f"ERROR: knowledge.db not found at {DB_PATH}.\n"
            f"Phase 1 schema migration requires the database to exist.\n"
        )
        sys.exit(1)
    return sqlite3.connect(str(DB_PATH))


def install() -> None:
    """Idempotent install: create table if not exists, seed default rows."""
    conn = _connect()
    try:
        cur = conn.cursor()
        cur.execute(CREATE_TABLE_SQL)
        for name, is_active, notes in SEED_INSERTS:
            cur.execute(
                "INSERT OR IGNORE INTO computation_roots "
                "(root_name, is_active, notes) VALUES (?, ?, ?)",
                (name, is_active, notes),
            )
        conn.commit()
        print(f"[install] computation_roots table installed at {DB_PATH}")
        _print_state(conn)
    finally:
        conn.close()


def check() -> None:
    """Report current state without modifying anything."""
    conn = _connect()
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT name FROM sqlite_master "
            "WHERE type='table' AND name='computation_roots'"
        )
        if cur.fetchone() is None:
            print("[check] computation_roots table does NOT exist; "
                  "run without --check to install.")
            return
        _print_state(conn)
    finally:
        conn.close()


def rollback(confirmed: bool) -> None:
    """Drop the computation_roots table. Requires explicit --yes."""
    if not confirmed:
        sys.stderr.write(
            "ERROR: --rollback requires --yes for confirmation. This DROPs "
            "the computation_roots table from knowledge.db. The rest of "
            "the database is unaffected, but any consumer that reads this "
            "table will fail until re-install.\n"
            "To proceed: python tools/_install_computation_roots_table.py "
            "--rollback --yes\n"
        )
        sys.exit(2)
    conn = _connect()
    try:
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS computation_roots")
        conn.commit()
        print(f"[rollback] computation_roots table dropped from {DB_PATH}")
    finally:
        conn.close()


def _print_state(conn: sqlite3.Connection) -> None:
    cur = conn.cursor()
    cur.execute(
        "SELECT id, root_name, is_active, registered_at, notes "
        "FROM computation_roots ORDER BY id"
    )
    rows = cur.fetchall()
    if not rows:
        print("[state] table empty.")
        return
    print("[state] computation_roots:")
    for row_id, name, is_active, registered, notes in rows:
        flag = "ACTIVE" if is_active else "      "
        notes_short = (notes[:60] + "...") if notes and len(notes) > 60 else notes
        print(f"  {flag} | id={row_id} | {name:24s} | "
              f"registered={registered} | {notes_short}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Phase 1 computation_roots table install/check/rollback."
    )
    parser.add_argument("--check", action="store_true",
                        help="Show table state without modifying anything")
    parser.add_argument("--rollback", action="store_true",
                        help="Drop the computation_roots table (requires --yes)")
    parser.add_argument("--yes", action="store_true",
                        help="Confirmation flag for --rollback")
    args = parser.parse_args()

    if args.rollback:
        rollback(confirmed=args.yes)
    elif args.check:
        check()
    else:
        install()


if __name__ == "__main__":
    main()
