"""Self-test for the knowledge-MCP emit_verdict tool (S98).

Exercises the syntax-force validation, sig_5 uniqueness, idempotency, the [SIGN]
3-tuple all-or-none rule, and the Option-A supersedes path — against a throwaway
session dir that is removed at the end. Run with the same interpreter the server
uses (system Python with `mcp` installed):

    python tools/mcp-servers/knowledge-mcp/test_emit_verdict.py
"""
import asyncio
import logging
import shutil
import sys
import re
from pathlib import Path

# Avoid clobbering the live server's log handle (Windows file-sharing) on import.
logging.basicConfig = lambda *a, **k: None  # noqa: E731

sys.path.insert(0, str(Path(__file__).resolve().parent))
import server  # noqa: E402

TS = 990001  # throwaway session number
VDIR = server.PROJECT_ROOT / "computations" / f"session-{TS}"
VFILE = VDIR / f"s{TS}_gate_verdicts.txt"

A, B, C, D = "a" * 64, "b" * 64, "c" * 64, "d" * 64

_passed = 0
_failed = 0


def check(name: str, cond: bool) -> None:
    global _passed, _failed
    print(("  PASS" if cond else "  FAIL"), name)
    if cond:
        _passed += 1
    else:
        _failed += 1


def txt(res) -> str:
    return res[0].text


async def emit(**kw) -> str:
    return txt(await server._emit_verdict(kw))


async def main() -> int:
    if VDIR.exists():
        shutil.rmtree(VDIR)

    base = dict(session=TS, scheme="FW", convention="ABSOLUTE", l_max="12")

    # 1 — valid [SIGN] emission
    r = await emit(gate_id="S990-T1-SIGN", verdict="PASS", value="x=1;y=2",
                   audit_sha256=A, content_sha256=B,
                   sign_verdict="PASS", magnitude_verdict="PASS", regime_verdict="VALID", **base)
    check("valid [SIGN] emit returns OK", "emit_verdict OK" in r)
    c = VFILE.read_text(encoding="utf-8")
    check("canonical line present", "S990-T1-SIGN: PASS -- value='x=1;y=2'" in c)
    check("audit/content SHA on canonical", f"audit_sha256={A} content_sha256={B}" in c)
    check("dual-SHA companion row present", f"audit_sha256_short={A[:16]}" in c)
    check("3-tuple row present", "sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID" in c)

    # 2 — idempotent re-call (same gate, same audit) -> NO-OP, file unchanged
    before = VFILE.read_text(encoding="utf-8")
    r = await emit(gate_id="S990-T1-SIGN", verdict="PASS", value="x=1;y=2",
                   audit_sha256=A, content_sha256=B,
                   sign_verdict="PASS", magnitude_verdict="PASS", regime_verdict="VALID", **base)
    check("idempotent re-call is NO-OP", "NO-OP" in r and VFILE.read_text(encoding="utf-8") == before)

    # 3 — sig_5 collision (different gate, reused audit SHA) -> reject
    r = await emit(gate_id="S990-T2-OTHER", verdict="FAIL", value="z=9",
                   audit_sha256=A, content_sha256=C, **base)
    check("sig_5 collision rejected", "sig_5 COLLISION" in r)

    # 4 — AUDIT gate (no 3-tuple) -> 2 rows, no 3-tuple line
    r = await emit(gate_id="S990-T3-AUDIT", verdict="INFO", value="hygiene=ok",
                   audit_sha256=C, content_sha256=D, **base)
    check("AUDIT gate OK", "emit_verdict OK" in r)
    check("AUDIT gate has NO 3-tuple row", "S990-T3-AUDIT 3-tuple" not in VFILE.read_text(encoding="utf-8"))

    # 5 — partial 3-tuple (sign only) -> reject
    r = await emit(gate_id="S990-T4-PARTIAL", verdict="PASS", value="q=1",
                   audit_sha256="e" * 64, content_sha256="f" * 64, sign_verdict="PASS", **base)
    check("partial 3-tuple rejected", "requires ALL of" in r)

    # 6 — malformed audit_sha256 -> reject
    r = await emit(gate_id="S990-T5-BADSHA", verdict="PASS", value="q=1",
                   audit_sha256="NOTHEX", content_sha256="f" * 64, **base)
    check("non-64-hex audit_sha rejected", "audit_sha256 must be 64" in r)

    # 7 — bad verdict enum -> reject
    r = await emit(gate_id="S990-T6-BADV", verdict="MAYBE", value="q=1",
                   audit_sha256="1" * 64, content_sha256="2" * 64, **base)
    check("non-enum verdict rejected", "verdict must be one of" in r)

    # 8 — single-quote in value -> reject (would break the value='...' delimiter)
    r = await emit(gate_id="S990-T7-QUOTE", verdict="PASS", value="it's bad",
                   audit_sha256="3" * 64, content_sha256="4" * 64, **base)
    check("single-quote in value rejected", "single quote" in r)

    # 9 — double-emission (same gate, NEW audit, no supersedes) -> reject
    r = await emit(gate_id="S990-T1-SIGN", verdict="FAIL", value="x=2",
                   audit_sha256="5" * 64, content_sha256="6" * 64,
                   sign_verdict="FAIL", magnitude_verdict="FAIL", regime_verdict="VALID", **base)
    check("double-emission without supersedes rejected", "already has a canonical verdict line" in r)

    # 10 — Option-A correction (same gate, NEW audit, WITH supersedes) -> allowed
    r = await emit(gate_id="S990-T1-SIGN", verdict="FAIL", value="x=2",
                   audit_sha256="5" * 64, content_sha256="6" * 64,
                   sign_verdict="FAIL", magnitude_verdict="FAIL", regime_verdict="VALID",
                   supersedes=A, **base)
    check("supersedes correction allowed", "emit_verdict OK" in r)
    check("corrective line carries supersedes tag", f"supersedes={A}" in VFILE.read_text(encoding="utf-8"))

    # final — sig_5 uniqueness across the whole file
    shas = re.findall(r"audit_sha256=([a-f0-9]{64})", VFILE.read_text(encoding="utf-8"))
    dupes = sorted({s for s in shas if shas.count(s) > 1})
    check("final file sig_5 clean (no duplicate audit SHAs)", not dupes)

    print(f"\nemit_verdict self-test: {_passed} passed, {_failed} failed")
    shutil.rmtree(VDIR)  # cleanup throwaway session
    return 0 if _failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
