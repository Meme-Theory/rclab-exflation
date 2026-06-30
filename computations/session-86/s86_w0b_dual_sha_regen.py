"""S86-W7-SIG2-DUAL-SHA-REGEN + S86-S85-VERDICT-FILE-COMPANION-ROW-CANONICALIZATION.

W0b-4 producing script. Sweeps computations/session-85/s85_gate_verdicts.txt for
canonical verdict lines that lack a matching W9a-99 companion comment row,
extracts content_sha256 and audit_sha256 from the canonical line itself, and
appends NEW canonicalized companion rows at the end of the file.

W9a-99 form (per .claude/rules/gate-verdicts.md S81+ + W9a-99 template):
  # GATE_ID: audit_sha256_short=<16hex> content_sha256=<64hex> audit_sha256=<64hex>

Existing schema-1.5 companion form (kept for back-compat, re-emitted in W9a-99):
  # audit_sha256 companion row: <GATE_ID> audit=<16hex> content=<16hex>

Per .claude/rules/gate-verdicts.md "verdicts are permanent — no retroactive
changes": this script APPENDS new companion rows; it never edits or deletes
historical lines.

Plan §W0b-4 §6 names target=24 (7 W7 + 17 schema-1.5) but lizzi 9A §4.4 line
295-297 reports 17 missing companions in current state. The script honors
the actual filesystem count, not the plan's wished-for 24.
"""

from canonical_constants import c_fabric  # noqa: F401
import hashlib
import pathlib
import re
import sys


REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
S85_VERDICT = REPO_ROOT / "computations" / "session-85" / "s85_gate_verdicts.txt"
S86_VERDICT = REPO_ROOT / "computations" / "session-86" / "s86_gate_verdicts.txt"

GATE_ID = "S86-W7-SIG2-DUAL-SHA-REGEN"

# Canonical-line regex — captures GATE_ID + audit_sha256 (64hex) + content_sha256 (64hex)
# Field order varies: some lines have audit_sha256 before content_sha256, some reverse.
CANONICAL_RE = re.compile(
    r"^(?P<gate_id>S\d+-[A-Z0-9_-]+):\s+(?:PASS|FAIL|INFO|PENDING-EVENT)\s+--\s+"
)
AUDIT_SHA_RE = re.compile(r"audit_sha256=(?P<sha>[0-9a-f]{64})")
CONTENT_SHA_RE = re.compile(r"content_sha256=(?P<sha>[0-9a-f]{64})")
LEGACY_SHA_RE = re.compile(r"\bsha256=(?P<sha>[0-9a-f]{64})\b")
COMPANION_RE = re.compile(
    r"^#\s+(?:audit_sha256\s+companion\s+row:\s+(?P<gate_legacy>\S+)\s+audit="
    r"(?P<audit_short_legacy>[0-9a-f]{16})\s+content=(?P<content_short_legacy>[0-9a-f]{16})|"
    r"(?P<gate_w9a99>\S+):\s+audit_sha256_short=(?P<audit_short_w9a99>[0-9a-f]{16})\s+"
    r"content_sha256=(?P<content_w9a99>[0-9a-f]{64})\s+audit_sha256=(?P<audit_w9a99>[0-9a-f]{64})|"
    r"audit_sha256_short=(?P<audit_short_orchestrator>[0-9a-f]{16})\s+"
    r"content_sha256=(?P<content_orchestrator>[0-9a-f]{64})\s+"
    r"audit_sha256=(?P<audit_orchestrator>[0-9a-f]{64}))"
)


def sha256_path(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_verdict_lines(text: str) -> list[dict]:
    """Return [{gate_id, audit, content, line_no, has_companion_next}] per canonical line."""
    lines = text.splitlines()  # (local)
    out: list[dict] = []  # (local)
    for i, line in enumerate(lines):
        m = CANONICAL_RE.match(line)  # (local)
        if not m:
            continue
        gate_id = m.group("gate_id")  # (local)
        audit_m = AUDIT_SHA_RE.search(line)  # (local)
        content_m = CONTENT_SHA_RE.search(line)  # (local)
        legacy_m = LEGACY_SHA_RE.search(line)  # (local)
        # Both SHAs present in canonical line OR fallback to legacy single-SHA
        if audit_m and content_m:
            audit = audit_m.group("sha")  # (local)
            content = content_m.group("sha")  # (local)
            schema = "S84+"  # (local)
        elif legacy_m:
            audit = legacy_m.group("sha")  # (local)
            content = ""  # (local) — no content_sha256 on canonical
            schema = "schema-1.5"  # (local)
        else:
            continue  # malformed; skip
        # Look ahead for matching companion row
        has_match = False  # (local)
        if i + 1 < len(lines):
            next_line = lines[i + 1]  # (local)
            cm = COMPANION_RE.match(next_line)  # (local)
            if cm:
                # Match by audit-prefix bit-identity
                companion_audit_short = (
                    cm.group("audit_short_legacy")
                    or cm.group("audit_short_w9a99")
                    or cm.group("audit_short_orchestrator")
                )  # (local)
                if companion_audit_short and audit.startswith(companion_audit_short):
                    has_match = True
        out.append({
            "gate_id": gate_id,
            "audit": audit,
            "content": content,
            "line_no": i + 1,
            "has_companion": has_match,
            "schema": schema,
        })
    return out


def main() -> int:
    pins: dict[str, str] = {  # (local)
        "s85_gate_verdicts.txt_pre_canonicalization": sha256_path(S85_VERDICT),
    }
    print("=" * 76)
    print(f"{GATE_ID} — input-pin SHAs:")
    for k, v in pins.items():
        print(f"  {k}: {v}")
    print("=" * 76)

    text = S85_VERDICT.read_text(encoding="utf-8")  # (local)
    parsed = parse_verdict_lines(text)  # (local)

    n_canonical = len(parsed)  # (local)
    n_with_companion = sum(1 for p in parsed if p["has_companion"])  # (local)
    n_missing = n_canonical - n_with_companion  # (local)
    n_schema_1_5 = sum(1 for p in parsed if p["schema"] == "schema-1.5")  # (local)

    print(f"S85 canonical lines: {n_canonical}")
    print(f"S84+ schema canonical lines: {n_canonical - n_schema_1_5}")
    print(f"schema-1.5 canonical lines: {n_schema_1_5}")
    print(f"Canonical lines with matching companion: {n_with_companion}")
    print(f"Canonical lines missing companion: {n_missing}")

    missing = [p for p in parsed if not p["has_companion"]]  # (local)
    n_with_content_sha = sum(1 for p in missing if p["content"])  # (local)
    n_without_content_sha = sum(1 for p in missing if not p["content"])  # (local)
    print(f"  - of which with content_sha256 on canonical (W9a-99 reachable): {n_with_content_sha}")
    print(f"  - of which without content_sha256 (schema-1.5 INFO): {n_without_content_sha}")

    # Append NEW canonicalized companion rows for the missing ones that have
    # content_sha256 reachable from the canonical line itself.
    # Schema-1.5 entries with no content_sha256 on canonical → skipped here;
    # the canonicalization for those requires reading the producing script's
    # content (which may not exist post-edit). Per plan §9 INFO clause: those
    # are PRE-REG-INCOMPLETE and carry forward.
    appended_lines: list[str] = []  # (local)
    for p in missing:
        if not p["content"]:
            continue
        new_companion = (  # (local)
            f"# {p['gate_id']}: audit_sha256_short={p['audit'][:16]} "
            f"content_sha256={p['content']} audit_sha256={p['audit']}  "
            f"# canonicalized S86 W0b-4 (post-hoc append, not edit)"
        )
        appended_lines.append(new_companion)

    n_appended = len(appended_lines)  # (local)
    print(f"New W9a-99 companion rows appended: {n_appended}")

    if appended_lines:
        with S85_VERDICT.open("a", encoding="utf-8") as f:
            f.write("\n# ===== S86 W0b-4 canonicalization sweep =====\n")
            for L in appended_lines:
                f.write(L + "\n")
            f.write("# ===== end S86 W0b-4 sweep =====\n")

    # Verdict: PASS iff all reachable missing companions were appended successfully
    # AND the schema-1.5-without-content gap is documented as INFO.
    plan_target = 24  # (local) plan §0.10 target_total (acknowledged plan-author conflation)
    actual_appended = n_appended  # (local)
    pass_predicate = (n_appended > 0) and (n_appended == n_with_content_sha)  # (local)
    if n_without_content_sha > 0:
        verdict = "INFO"  # (local) per plan §9 INFO clause
    elif pass_predicate:
        verdict = "PASS"  # (local)
    else:
        verdict = "FAIL"  # (local)

    audit_payload = "|".join(f"{k}:{v}" for k, v in sorted(pins.items()))  # (local)
    audit_sha = hashlib.sha256(
        (audit_payload + f"|appended:{n_appended}|missing:{n_missing}").encode()
    ).hexdigest()  # (local)

    content_payload = (  # (local)
        f"{GATE_ID}|appended={n_appended}|missing_total={n_missing}"
        f"|missing_with_content_sha={n_with_content_sha}"
        f"|missing_without_content_sha={n_without_content_sha}"
        f"|plan_target={plan_target}|actual_canonical={n_canonical}"
    )
    content_sha = hashlib.sha256(content_payload.encode()).hexdigest()  # (local)

    canonical_line = (  # (local)
        f"{GATE_ID}: {verdict} -- value={n_appended} "
        f"scheme=verdict_file_dual_sha_regen convention=W9a99 "
        f"L_max=N/A sha256={audit_sha}"
    )
    companion_line = (  # (local)
        f"# audit_sha256_short={audit_sha[:16]} content_sha256={content_sha} "
        f"audit_sha256={audit_sha}"
    )

    with S86_VERDICT.open("a", encoding="utf-8") as f:
        f.write(canonical_line + "\n")
        f.write(companion_line + "\n")

    print()
    print(canonical_line)
    print(companion_line)
    print(f"\n4-tuple: (value={n_appended}, scheme=verdict_file_dual_sha_regen, "
          f"convention=W9a99, L_max=N/A)")
    print(f"\nNote: plan §0.10 target_total=24 conflates W7-single-SHA with "
          f"schema-1.5 (lizzi 9A §4.4 reports 17 total missing companions, not 7+17).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
