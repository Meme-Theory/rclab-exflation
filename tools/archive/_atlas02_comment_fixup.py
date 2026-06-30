"""Follow-up to _atlas02_cleanup.py: fix the 4 comments that ACTIVELY
contradict the new state (atlas-02 no longer a canonical extraction source).

Skips comments that are still factually correct about document content
(e.g., "§V is a SUBSET of atlas-02's coverage" — atlas-02 document still
contains those Eras even though we don't extract from it).
"""
import ast
import pathlib
import sys


def main():
    p = pathlib.Path("tools/extract_entities.py")
    orig = p.read_text(encoding="utf-8")
    text = orig

    fixes = []

    # (A) The "Canonical sources covered here" comment block (was L673-687
    # of original; now shifted to L673 of post-cleanup file).
    old_a = (
        "# Canonical sources covered here:\n"
        "#   - sessions/framework/Atlas/atlas-02-mechanism-lifecycle.md (this commit)\n"
        "#\n"
        "# Pending future commits:\n"
        "#   - sessions/permanent-results-registry.md §V\n"
        "#   - sessions/framework/registry/closed-gw-channels.md\n"
        "#   - strict narrative-source parser (replaces legacy table+bullet+narrative\n"
        "#     strategies)"
    )
    new_a = (
        "# Canonical sources covered here:\n"
        "#   - sessions/permanent-results-registry.md §V\n"
        "#   - sessions/framework/registry/closed-gw-channels.md\n"
        "#\n"
        "# atlas-02-mechanism-lifecycle.md was previously special-cased as a\n"
        "# canonical source (S89 cleanup); reverted 2026-05-19 because Atlas\n"
        "# docs are downstream summaries — the S91 cmap retrofit lifted\n"
        "# closures back to per-session WPs / synthesis docs as the\n"
        "# authoritative sources.\n"
        "#\n"
        "# Pending future commits:\n"
        "#   - strict narrative-source parser (replaces legacy table+bullet+narrative\n"
        "#     strategies)"
    )
    fixes.append(("(A) canonical-sources-comment-block", old_a, new_a))

    # (B) "atlas-02 is the canonical source for S63-S65" comment
    old_b = (
        "# The parser scopes to Era-keyed subsections only. V-H/I/J are\n"
        "# intentionally skipped: atlas-02 is the canonical source for S63-S65.\n"
        "# V-K/L/M are skipped because they're metadata."
    )
    new_b = (
        "# The parser scopes to Era-keyed subsections only. V-H/I/J are\n"
        "# intentionally skipped (different schema — would require\n"
        "# schema-specific handling; S63-S65 closures from those subsections\n"
        "# fall through to the per-session WP / synthesis parsers).\n"
        "# V-K/L/M are skipped because they're metadata."
    )
    fixes.append(("(B) V-H/I/J skip-reason", old_b, new_b))

    # (C) "extracted via the atlas-02 canonical-source parser" comment
    old_c = (
        "            # are extracted via the atlas-02 canonical-source parser and\n"
        "            # do NOT touch this legacy path."
    )
    new_c = (
        "            # are extracted via the per-session WP cmap parser and the\n"
        "            # §V canonical-source parser, and do NOT touch this legacy path."
    )
    fixes.append(("(C) legacy-path-bypass-comment", old_c, new_c))

    # (D) "closed_atlas02_*" listed in canonical-namespace IDs comment
    old_d = (
        "    # synthesis below. Canonical-namespace IDs (closed_atlas02_*,\n"
        "    # closed_regv_*, closed_gwch_*, proven_atlas07_*, proven_regvii_*)"
    )
    new_d = (
        "    # synthesis below. Canonical-namespace IDs (closed_regv_*,\n"
        "    # closed_gwch_*, proven_atlas07_*, proven_regvii_*)"
    )
    fixes.append(("(D) canonical-namespace-comment", old_d, new_d))

    for desc, old, new in fixes:
        n = text.count(old)
        if n != 1:
            print(f"FAIL: {desc} anchor count = {n} (expected 1)")
            sys.exit(1)
        text = text.replace(old, new, 1)
        print(f"OK: {desc}")

    try:
        ast.parse(text)
    except SyntaxError as e:
        print(f"FAIL: syntax error after edits: {e}")
        sys.exit(1)
    print("OK: ast.parse passed")

    # Final remaining-atlas-02 audit
    remaining = []
    for i, line in enumerate(text.split("\n"), 1):
        low = line.lower()
        if "atlas-02" in low or "atlas02" in low:
            remaining.append((i, line))
    print(f"remaining atlas-02 / atlas02 mentions: {len(remaining)}")
    for i, line in remaining:
        print(f"  L{i}: {line[:120]}")

    print(f"size:  {len(orig):>8d} -> {len(text):>8d} bytes (delta {len(text)-len(orig):+d})")
    p.write_text(text, encoding="utf-8")
    print("WROTE tools/extract_entities.py")


if __name__ == "__main__":
    main()
