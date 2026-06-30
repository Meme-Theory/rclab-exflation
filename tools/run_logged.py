#!/usr/bin/env python3
"""run_logged.py -- deterministic command runner with guaranteed-complete output capture.

WHY THIS EXISTS
---------------
The harness truncates/persists large Bash stdout to ephemeral files (showing only a
~2KB preview), interleaves parallel tool calls, and the Read tool has returned glitched
text (stray characters, wrong line numbers). The combined effect: command output has
been unreliable, and acting on it produced false-confidence claims.

This wrapper makes output trustworthy by construction:

  1. Runs exactly ONE command (subprocess, shell=False -> no space-in-path breakage).
  2. Captures stdout+stderr (merged) + exit code IN FULL to a stable, in-project log
     under tools/_runlog/  (never an ephemeral harness location).
  3. Prints a bounded summary that is GUARANTEED to fit inline (hard byte budget well
     under the harness persist threshold): the complete output when small, else
     head + tail with the EXACT elided-line count and the on-disk log path.

So every invocation yields: an unambiguous EXIT code, exact line/byte totals, and either
the full output inline or a precise pointer to the bytes not shown. Nothing is asserted
that a non-zero exit or an elision marker would contradict.

USAGE
-----
  python tools/run_logged.py -- <command> [args...]        # run a command (logged + printed)
  python tools/run_logged.py --show <path> [START END]     # print a bounded slice of any file
  python tools/run_logged.py --tail <path> [N]             # print last N lines (default 200)

The wrapper itself ALWAYS exits 0 (so it never masquerades as a script error); the
wrapped command's real exit code is in the banner and the log header.
"""
import sys, os, subprocess, time, glob

LOGDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_runlog")
PRINT_BUDGET = 16000   # max bytes printed inline; stays well under harness persist threshold
LINE_WIDTH   = 240     # per-line clip width for inline printing
KEEP_LOGS    = 100     # prune run_*.txt beyond this many


def _clip(line, w=LINE_WIDTH):
    return line if len(line) <= w else line[:w] + f" …(+{len(line) - w} chars)"


def _budget_ok(buf):
    return len(buf.encode("utf-8", "replace")) <= PRINT_BUDGET


def _emit(text, logpath, exit_code, elapsed):
    raw_lines = text.splitlines()
    nlines = len(raw_lines)
    nbytes = len(text.encode("utf-8", "replace"))
    lines = [_clip(l) for l in raw_lines]
    banner = [
        f"=== run_logged | EXIT={exit_code} | {nlines} lines | {nbytes} bytes | {elapsed:.1f}s ===",
        f"=== full log: {logpath} ===",
    ]
    body_full = "\n".join(banner + lines + [f"=== END (complete: all {nlines} lines shown) ==="])
    if _budget_ok(body_full):
        print(body_full)
        return
    # too large -> head + tail, shrink until within budget
    h = t = 70
    while h >= 5:
        head, tail = lines[:h], lines[-t:]
        elided = nlines - h - t
        mid = (f"--- [ELIDED {elided} lines -- read them with: "
               f"python tools/run_logged.py --show {logpath} {h + 1 + 5} {nlines - t + 5}  "
               f"(+5 offsets for the 5-line log header) ; or --tail {logpath} <N>] ---")
        buf = "\n".join(
            banner
            + [f"--- HEAD (first {h} of {nlines} lines) ---"] + head
            + [mid, f"--- TAIL (last {t} of {nlines} lines) ---"] + tail
            + [f"=== END (PARTIAL: {elided} middle lines NOT shown inline; on disk at log path) ==="]
        )
        if _budget_ok(buf):
            print(buf)
            return
        h -= 10
        t -= 10
    print("\n".join(banner + [f"--- output too large to inline even as head/tail; use "
                              f"python tools/run_logged.py --tail {logpath} 200 ---",
                              "=== END (PARTIAL) ==="]))


def _prune():
    runs = sorted(glob.glob(os.path.join(LOGDIR, "run_*.txt")))
    for old in runs[:-KEEP_LOGS]:
        try:
            os.remove(old)
        except OSError:
            pass


def cmd_run(argv):
    if not argv:
        print("=== run_logged: no command given after -- ===")
        return 0
    os.makedirs(LOGDIR, exist_ok=True)
    cf = os.path.join(LOGDIR, "_counter")
    n = 0
    if os.path.exists(cf):
        try:
            n = int(open(cf).read().strip())
        except ValueError:
            n = 0
    n += 1
    open(cf, "w").write(str(n))

    ts = time.strftime("%Y%m%d-%H%M%S")
    logpath = os.path.join(LOGDIR, f"run_{n:04d}_{ts}.txt")
    lastpath = os.path.join(LOGDIR, "last.txt")

    # Windows CreateProcess (used by subprocess, shell=False) cannot resolve a relative,
    # forward-slash executable path the way Git Bash can -> FileNotFoundError(2). Absolutize
    # argv[0] when it names a real on-disk file so the subprocess can actually launch.
    if argv:
        _cand = os.path.abspath(argv[0])
        if os.path.exists(_cand):
            argv = [_cand] + list(argv[1:])
    t0 = time.time()
    try:
        proc = subprocess.run(argv, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                              text=True, errors="replace")
        rc = proc.returncode
        out = proc.stdout or ""
    except Exception as e:  # command itself unlaunchable
        rc = 127
        out = f"[run_logged] FAILED TO LAUNCH: {e!r}\n"
    elapsed = time.time() - t0

    header = (f"# CMD: {' '.join(argv)}\n# EXIT: {rc}\n# WHEN: {ts}\n"
              f"# ELAPSED: {elapsed:.2f}s\n# {'=' * 60}\n")
    full = header + out
    for path in (logpath, lastpath):
        with open(path, "w", encoding="utf-8", errors="replace") as f:
            f.write(full)
    _prune()
    _emit(out, logpath, rc, elapsed)
    return 0


def cmd_show(path, start=None, end=None):
    if not os.path.exists(path):
        print(f"=== run_logged --show: NO SUCH FILE: {path} ===")
        return 0
    raw = open(path, encoding="utf-8", errors="replace").read().splitlines()
    nlines = len(raw)
    s = int(start) if start else 1
    e = int(end) if end else nlines
    s = max(1, s)
    e = min(nlines, e)
    if e < s:
        s, e = e, s
    if e - s + 1 > 600:           # window cap
        e = s + 599
    out = [f"=== run_logged --show {path} | lines {s}-{e} of {nlines} ==="]
    for i in range(s, e + 1):
        out.append(f"{i}: {_clip(raw[i - 1])}")
    out.append(f"=== END show ({e - s + 1} of {nlines} lines) ===")
    buf = "\n".join(out)
    # enforce budget by shrinking the window if needed
    while not _budget_ok(buf) and e > s:
        e -= max(1, (e - s) // 4)
        out = [f"=== run_logged --show {path} | lines {s}-{e} of {nlines} (window shrunk to fit print budget) ==="]
        for i in range(s, e + 1):
            out.append(f"{i}: {_clip(raw[i - 1])}")
        out.append(f"=== END show ({e - s + 1} of {nlines} lines) ===")
        buf = "\n".join(out)
    print(buf)
    return 0


def main():
    a = sys.argv[1:]
    if not a:
        print("usage: run_logged.py -- <cmd...> | --show <path> [s e] | --tail <path> [n]")
        return 0
    if a[0] == "--":
        return cmd_run(a[1:])
    if a[0] == "--show":
        if len(a) < 2:
            print("=== --show needs a path ===")
            return 0
        return cmd_show(a[1], a[2] if len(a) > 2 else None, a[3] if len(a) > 3 else None)
    if a[0] == "--tail":
        if len(a) < 2:
            print("=== --tail needs a path ===")
            return 0
        path = a[1]
        n = int(a[2]) if len(a) > 2 else 200
        if not os.path.exists(path):
            print(f"=== --tail: NO SUCH FILE: {path} ===")
            return 0
        total = len(open(path, encoding="utf-8", errors="replace").read().splitlines())
        return cmd_show(path, max(1, total - n + 1), total)
    return cmd_run(a)   # convenience: bare argv treated as a command


if __name__ == "__main__":
    sys.exit(main())
