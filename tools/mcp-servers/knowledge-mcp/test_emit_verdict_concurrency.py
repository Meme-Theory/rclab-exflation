"""Concurrency integration test for emit_verdict (the CF-S99-HK-2 PASS gate).

Spawns N SEPARATE processes that each call emit_verdict on the SAME session
verdict file simultaneously, and asserts ALL N lines land (zero lost lines) +
sig_5 clean. This validates that the cross-process O_EXCL lockfile actually
serializes writes — the failure the open-coded open("a") append could not
survive on Windows under concurrent agent processes.

Also runs a DIAGNOSTIC pass with the OLD open("a") path to report whether the
race reproduces on this machine (NOT asserted — the lost-update race is
probabilistic; absence of loss in one run does not disprove it).

    python tools/mcp-servers/knowledge-mcp/test_emit_verdict_concurrency.py
"""
import asyncio
import logging
import multiprocessing as mp
import re
import shutil
import sys
import time
from pathlib import Path

BASE = Path(__file__).resolve().parent          # tools/mcp-servers/knowledge-mcp
N = 16                                           # concurrent writers (2x the 8 that broke S98)
TS_TOOL = 990002                                 # throwaway session — emit_verdict path
TS_RAW = 990003                                  # throwaway session — open("a") diagnostic


def _verdict_path(ts: int) -> Path:
    root = BASE.parents[2]                       # knowledge-mcp -> mcp-servers -> tools -> root
    return root / "computations" / f"session-{ts}" / f"s{ts}_gate_verdicts.txt"


def _emit_worker(idx: int) -> None:
    """Child process: emit ONE verdict via the MCP tool's _emit_verdict."""
    logging.basicConfig = lambda *a, **k: None   # avoid log-file clobber on import
    sys.path.insert(0, str(BASE))
    import server  # noqa: E402
    payload = {
        "session": TS_TOOL,
        "gate_id": f"S{TS_TOOL}-CONC-{idx:03d}",
        "verdict": "PASS",
        "value": f"idx={idx}",
        "scheme": "FW", "convention": "ABSOLUTE", "l_max": "12",
        "audit_sha256": f"{idx:064x}",
        "content_sha256": f"{idx + 500000:064x}",
        "sign_verdict": "PASS", "magnitude_verdict": "PASS", "regime_verdict": "VALID",
    }
    asyncio.run(server._emit_verdict(payload))


def _raw_worker(args) -> None:
    """Child process: OLD open('a') append (the racy path), diagnostic only."""
    idx, vfile_str = args
    line = (f"S{TS_RAW}-RAW-{idx:03d}: PASS -- value='idx={idx}' scheme=FW "
            f"convention=ABSOLUTE L_max=12 audit_sha256={idx:064x} "
            f"content_sha256={idx + 500000:064x} schema_version=S84+\n")
    time.sleep(0.001 * (idx % 4))                # slight stagger to provoke collisions
    with open(vfile_str, "a", encoding="utf-8") as f:
        f.write(line)


def main() -> int:
    ok = True

    # ---- (b) emit_verdict path — HARD assertion: zero lost lines ----
    vfile = _verdict_path(TS_TOOL)
    if vfile.parent.exists():
        shutil.rmtree(vfile.parent)
    with mp.Pool(N) as pool:
        pool.map(_emit_worker, list(range(N)))
    text = vfile.read_text(encoding="utf-8") if vfile.exists() else ""
    canon = re.findall(rf"^S{TS_TOOL}-CONC-\d+: ", text, re.M)
    shas = re.findall(r"audit_sha256=([a-f0-9]{64})", text)
    dupes = sorted({s for s in shas if shas.count(s) > 1})
    print(f"[emit_verdict] {len(canon)}/{N} canonical lines present; "
          f"sig_5 dupes: {dupes or 'none'}")
    if len(canon) != N:
        print(f"  FAIL: lost {N - len(canon)} lines under {N} concurrent writers")
        ok = False
    if dupes:
        print("  FAIL: sig_5 duplicate audit SHAs")
        ok = False
    if len(canon) == N and not dupes:
        print("  PASS: zero lost lines, sig_5 clean")
    shutil.rmtree(vfile.parent, ignore_errors=True)

    # ---- (a) raw open('a') path — DIAGNOSTIC (race is probabilistic) ----
    rfile = _verdict_path(TS_RAW)
    if rfile.parent.exists():
        shutil.rmtree(rfile.parent)
    rfile.parent.mkdir(parents=True, exist_ok=True)
    rfile.touch()
    with mp.Pool(N) as pool:
        pool.map(_raw_worker, [(i, str(rfile)) for i in range(N)])
    rtext = rfile.read_text(encoding="utf-8") if rfile.exists() else ""
    rcanon = re.findall(rf"^S{TS_RAW}-RAW-\d+: ", rtext, re.M)
    verdict_raw = ("race reproduced — lines LOST" if len(rcanon) < N
                   else "no loss this run (race is probabilistic; not a disproof)")
    print(f"[raw open('a') DIAGNOSTIC] {len(rcanon)}/{N} lines present "
          f"({verdict_raw})")
    shutil.rmtree(rfile.parent, ignore_errors=True)

    print(f"\nemit_verdict concurrency test: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
