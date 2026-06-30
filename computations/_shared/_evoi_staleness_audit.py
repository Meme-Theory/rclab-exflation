#!/usr/bin/env python3
"""
_evoi_staleness_audit.py — EVOI guiding-star content-staleness detector.

WHY THIS EXISTS
---------------
`sessions/evoi-framework.md` is the framework's computation-priority "guiding star".
It went CONTENT-frozen at the S83 stamp from S84 through S95 (~13 sessions) while broad
multi-file commits kept git-touching its bytes — so `git log -- <file>` showed recent
activity and it LOOKED maintained. git-touched != content-refreshed. This audit closes
that gap structurally: it compares the file's self-declared content-currency session tag
against the current session and flags a lag, regardless of git mtime.

VERDICT SEMANTICS (per .claude/rules/math-scripts.md "Exit Codes and Verdict Semantics")
----------------------------------------------------------------------------------------
Verdict is DATA, not an exit code.
  exit 0  -> script ran fine and produced a verdict (PASS / S2 / S1), whatever it is.
  exit !=0 -> script breakage only (file missing, parse failure, env error).

  PASS : lag == 0  (content currency == current session)
  S2   : 1 <= lag <= 2  (advisory; non-blocking nudge to re-stamp at plan-freeze)
  S1   : lag >= 3        (MANDATORY; the guiding star is rotting — REBUILD per the
                          §7 maintenance contract, do not re-note-and-defer)

USAGE
-----
  python computations/_shared/_evoi_staleness_audit.py
  python computations/_shared/_evoi_staleness_audit.py --json
  python computations/_shared/_evoi_staleness_audit.py --current-session 97
  python computations/_shared/_evoi_staleness_audit.py --self-test

Plan-freeze hook: run alongside the PRU / source-reconciliation audits. S1 halts
plan-freeze with a REBUILD remediation request; S2 emits an advisory.
"""
# canonical_constants: intentionally NOT used here. This is audit infrastructure
# (it parses a markdown currency tag); it consumes zero framework physics constants,
# so there is no `from canonical_constants import` line by design — the import
# convention in _shared/CLAUDE.md targets physics computation scripts, not infra tooling.
from __future__ import annotations
import argparse
import glob
import json
import os
import re
import sys

# Repo root = two levels up from computations/_shared/
_THIS = os.path.abspath(__file__)
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(_THIS), "..", ".."))
EVOI_PATH = os.path.join(REPO_ROOT, "sessions", "evoi-framework.md")

# The currency tag is read from the FIRST "S<NN>" appearing on the **Date** line
# OR the **Content currency** line of the EVOI file header. We scan both and take
# the max (most recent) so an annotation can only ever make the file look NEWER,
# never staler than its true content date.
# Letter-suffixed sub-sessions (e.g. session-100a / S100a) parse as their numeric era:
# the suffix is matched OUTSIDE the capture group so lag arithmetic stays integer.
_CURRENCY_LINE_RE = re.compile(r"^\*\*(?:Date|Content currency)\*\*.*", re.IGNORECASE)
_SNN_RE = re.compile(r"\bS(\d{1,3})[a-z]?\b")
_SESSION_DIR_RE = re.compile(r"^session-(\d{1,3})[a-z]?$")


_CURRENCY_MARKER_RE = re.compile(r"<!--\s*evoi-content-currency:\s*S?(\d{1,3})[a-z]?\s*-->", re.IGNORECASE)


def read_currency_session(evoi_text: str) -> int | None:
    """Authoritative machine marker first; fall back to header scan only if the marker is absent.

    The marker is authoritative because the prose header legitimately mentions OTHER sessions
    (e.g. "S96 close / S97-prep", "atlas (S94)"). A bare max-over-header scan over-reads such
    mentions and would inflate a stale file to look newer — the exact wrong direction. The
    marker pins the single true content-currency session unambiguously.
    """
    marker = _CURRENCY_MARKER_RE.search(evoi_text)
    if marker:
        return int(marker.group(1))
    found: list[int] = []
    for line in evoi_text.splitlines()[:12]:  # header only (fallback)
        if _CURRENCY_LINE_RE.match(line.strip()):
            found += [int(m) for m in _SNN_RE.findall(line)]
    return max(found) if found else None


def detect_current_session(repo_root: str) -> int | None:
    """Max numeric N among sessions/session-<N> directories."""
    sessions_dir = os.path.join(repo_root, "sessions")
    nums: list[int] = []
    for entry in glob.glob(os.path.join(sessions_dir, "session-*")):
        if not os.path.isdir(entry):
            continue
        m = _SESSION_DIR_RE.match(os.path.basename(entry))
        if m:
            nums.append(int(m.group(1)))
    return max(nums) if nums else None


def classify(currency: int | None, current: int | None) -> dict:
    if currency is None:
        return {"verdict": "S1", "lag": None,
                "detail": "EVOI file carries no parseable S<NN> content-currency tag in its header."}
    if current is None:
        return {"verdict": "PASS", "lag": None,
                "detail": "No sessions/session-<N> dirs found; cannot compute lag (treated as non-blocking)."}
    lag = current - currency
    if lag <= 0:
        v, d = "PASS", f"EVOI content currency S{currency} is at/ahead of current session S{current} (lag={lag})."
    elif lag <= 2:
        v, d = "S2", f"EVOI content currency S{currency} lags current session S{current} by {lag} — advisory: re-stamp at plan-freeze."
    else:
        v, d = "S1", (f"EVOI content currency S{currency} lags current session S{current} by {lag} (>=3) — "
                      f"MANDATORY: the guiding star is rotting. REBUILD per evoi-framework.md §7, do not re-note-and-defer.")
    return {"verdict": v, "lag": lag, "detail": d}


def run(current_override: int | None = None) -> dict:
    if not os.path.exists(EVOI_PATH):
        raise FileNotFoundError(f"EVOI file not found: {EVOI_PATH}")
    with open(EVOI_PATH, "r", encoding="utf-8") as fh:
        text = fh.read()
    currency = read_currency_session(text)
    current = current_override if current_override is not None else detect_current_session(REPO_ROOT)
    result = classify(currency, current)
    result.update({"currency_session": currency, "current_session": current,
                   "evoi_path": os.path.relpath(EVOI_PATH, REPO_ROOT)})
    return result


def self_test() -> int:
    """Synthetic POSITIVE (fresh) + NEGATIVE (stale) cases. Returns 0 on success."""
    cases = [
        # (currency, current) -> expected verdict
        ((96, 96), "PASS"),
        ((96, 95), "PASS"),   # currency ahead (annotation) -> still PASS
        ((96, 97), "S2"),     # lag 1
        ((96, 98), "S2"),     # lag 2
        ((83, 96), "S1"),     # the real lapse: lag 13
        ((None, 96), "S1"),   # unparseable currency
    ]
    ok = True
    for (cur, now), expected in cases:
        got = classify(cur, now)["verdict"]
        flag = "ok" if got == expected else "FAIL"
        if got != expected:
            ok = False
        print(f"  self-test currency={cur} current={now}: expected {expected}, got {got} [{flag}]")
    # currency-PARSER tests (the S97-prep header-inflation bug this marker fixes)
    parse_cases = [
        ("<!-- evoi-content-currency: S96 -->\n**Date**: 2026 (S96 close / S97-prep)", 96),  # marker wins
        ("**Date**: 2026 (S96 close / S97-prep grounded REBUILD)", 97),  # NO marker -> fallback over-reads to 97 (documents the bug)
        ("**Content currency**: atlas-08 (S94 cluster)", 94),
        ("<!-- evoi-content-currency: S100a -->\n**Date**: 2026 (S99 close)", 100),  # letter-suffixed sub-session parses as its numeric era
        ("**Date**: 2026 (S100a-prep re-stamp)", 100),  # suffixed label on the fallback line
    ]
    for text, expected in parse_cases:
        got = read_currency_session(text)
        flag = "ok" if got == expected else "FAIL"
        if got != expected:
            ok = False
        print(f"  parse-test currency={got} expected={expected} [{flag}]")
    print("self-test:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser(description="EVOI guiding-star content-staleness audit.")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--current-session", type=int, default=None,
                    help="override detected current session number")
    ap.add_argument("--self-test", action="store_true", help="run synthetic test fixtures")
    args = ap.parse_args()

    if args.self_test:
        return self_test()

    try:
        result = run(args.current_session)
    except Exception as exc:  # script breakage -> exit !=0
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"EVOI staleness audit: {result['verdict']}")
        print(f"  content currency : S{result['currency_session']}")
        print(f"  current session  : S{result['current_session']}")
        print(f"  lag              : {result['lag']}")
        print(f"  {result['detail']}")
    return 0  # verdict is data; script ran fine


if __name__ == "__main__":
    sys.exit(main())
