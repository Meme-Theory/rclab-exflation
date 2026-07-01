#!/usr/bin/env python3
"""
Batch-suppression helper for hook scripts.

When N parallel tool calls fire the same hook with identical brief content
within a short window, only the first emission lands; subsequent invocations
exit with status 1 (caller suppresses emission).

Mechanism: atomic O_EXCL lockfile keyed by sha256(brief)[:16]. First invocation
to create the lockfile wins; concurrent invocations see the file and suppress.
Lockfiles older than `window_seconds` are treated as stale and replaced (this
prevents a wedged lockfile from suppressing future batches indefinitely).

Usage:
    python _batch_suppress.py <hook-id> <brief-content> [window-seconds=15.0]

Exit codes:
    0 = lead acquired OR error (caller should emit; default is non-suppress)
    1 = batch member (caller should suppress)

Note on the default-to-emit convention: on any unexpected error, we exit 0
(emit) rather than 1 (suppress). It is better to occasionally over-emit than
to silently suppress a brief the caller wanted delivered.
"""
import hashlib
import os
import sys
import tempfile
import time


def main():
    if len(sys.argv) < 3:
        sys.exit(0)

    hook_id = sys.argv[1]
    content = sys.argv[2]
    try:
        window = float(sys.argv[3]) if len(sys.argv) > 3 else 15.0
    except ValueError:
        window = 15.0

    content_hash = hashlib.sha256(content.encode("utf-8")).hexdigest()[:16]
    safe_hook_id = "".join(c for c in hook_id if c.isalnum() or c in "-_")[:32]
    lockfile = os.path.join(
        tempfile.gettempdir(),
        "hook-batch-{}-{}.lock".format(safe_hook_id, content_hash),
    )

    now = time.time()

    # Check for an existing lockfile. If fresh (within window), suppress.
    # If stale, attempt to remove so we can re-acquire below.
    if os.path.isfile(lockfile):
        try:
            mtime = os.path.getmtime(lockfile)
            if now - mtime < window:
                sys.exit(1)
            try:
                os.remove(lockfile)
            except OSError:
                pass
        except OSError:
            pass

    # Atomically attempt to acquire the lead. If a concurrent invocation
    # got here first, FileExistsError fires and we suppress.
    try:
        fd = os.open(lockfile, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o644)
        os.write(fd, str(now).encode("utf-8"))
        os.close(fd)
    except FileExistsError:
        sys.exit(1)
    except Exception:
        # Any other error: default to emit
        sys.exit(0)

    sys.exit(0)


if __name__ == "__main__":
    main()
