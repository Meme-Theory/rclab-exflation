#!/usr/bin/env python3
"""
s90_w1_emit_verdict.py — Atomic dual-SHA verdict-line emitter for S90 W1 gates.

Usage:
  python s90_w1_emit_verdict.py <gate_id> <verdict> <value_str> <scheme> <convention> \
                                <L_max> <input_pin_map_json> [supersedes_sha]

Computes:
  content_sha256 = SHA-256 over the producing artifact (rule-file diff or audit-script)
  audit_sha256   = SHA-256 over the ordered input-pin map (JSON-serialized)

Appends single canonical line + dual-SHA companion comment row to
`computations/session-90/s90_gate_verdicts.txt` using atomic single `open("a")`.

Per `.claude/rules/gate-verdicts.md` S87+ schema-v2 + `.claude/rules/v3-closure-recovery.md`.
"""
import hashlib
import json
import sys
from pathlib import Path

VERDICT_FILE = Path(__file__).resolve().parents[2] / 'computations' / 'session-90' / 's90_gate_verdicts.txt'


def sha256_of_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()


def sha256_of_text(text: str) -> str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def compute_audit_sha(input_pin_map: dict) -> str:
    """SHA-256 over ordered JSON-serialized input-pin map (sorted keys)."""
    canonical_json = json.dumps(input_pin_map, sort_keys=True, ensure_ascii=False)
    return sha256_of_text(canonical_json)


def emit_verdict(
    gate_id: str,
    verdict: str,
    value_str: str,
    scheme: str,
    convention: str,
    L_max: str,
    input_pin_map: dict,
    content_target: Path,
    supersedes: str = '',
) -> dict:
    """Emit a canonical verdict line + dual-SHA companion row atomically."""
    content_sha = sha256_of_file(content_target)
    audit_sha = compute_audit_sha(input_pin_map)

    if supersedes:
        value_field = f"value='{value_str};supersedes={supersedes}'"
    else:
        value_field = f"value='{value_str}'"

    canonical_line = (
        f'{gate_id}: {verdict} -- {value_field} '
        f'scheme={scheme} convention={convention} L_max={L_max} '
        f'audit_sha256={audit_sha} content_sha256={content_sha} schema_version=S87+'
    )
    companion_line = (
        f'# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} '
        f'# {gate_id} dual-SHA companion row (W9a-99 split)'
    )

    # Atomic single-call append (POSIX O_APPEND semantics on Windows is atomic for short writes)
    VERDICT_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not VERDICT_FILE.exists():
        VERDICT_FILE.touch()
    with VERDICT_FILE.open('a', encoding='utf-8') as f:
        f.write(canonical_line + '\n')
        f.write(companion_line + '\n')

    return {
        'gate_id': gate_id,
        'verdict': verdict,
        'content_sha256': content_sha,
        'audit_sha256': audit_sha,
        'canonical_line': canonical_line,
        'companion_line': companion_line,
    }


def main():
    """CLI entry-point — used for ad-hoc emission; for in-orchestrator use, import directly."""
    if len(sys.argv) < 8:
        print(json.dumps({'error': 'usage: s90_w1_emit_verdict.py <gate_id> <verdict> <value> <scheme> <convention> <L_max> <input_pin_json> [<supersedes_sha>] <content_target>'}, indent=2))
        sys.exit(1)
    gate_id = sys.argv[1]
    verdict = sys.argv[2]
    value_str = sys.argv[3]
    scheme = sys.argv[4]
    convention = sys.argv[5]
    L_max = sys.argv[6]
    input_pin_json = sys.argv[7]
    supersedes = ''
    content_target_idx = 8  # (local) — argv index, not a framework constant
    if len(sys.argv) >= 10:  # noqa: PLR2004 — argv length check
        supersedes = sys.argv[8]
        content_target_idx = 9  # (local) — argv index, not a framework constant
    content_target = Path(sys.argv[content_target_idx])
    input_pin_map = json.loads(input_pin_json)
    result = emit_verdict(gate_id, verdict, value_str, scheme, convention, L_max,
                          input_pin_map, content_target, supersedes)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
