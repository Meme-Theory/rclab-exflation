"""S86-SINGLE-NAME-CONFLATION-METHODOLOGY-ENTRY — W0b-2 producing script.

Verifies the §VII.R methodology entry was landed with all 4 required witness
citations + keyword + R8 cross-reference, then emits the verdict line per
.claude/rules/gate-verdicts.md.

PASS iff:
  W = {"2A", "2B", "6A", "W12-2"}     (4 witness IDs present in §VII.R block)
  K = "single-name conflation"          (keyword present)
  X = cross-reference to R8 (§VII.S)    (cross-reference present)

  PASS_predicate = (W == W_required) AND K AND X
"""

from canonical_constants import c_fabric  # noqa: F401
import hashlib
import pathlib
import re
import sys


REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
REGISTRY = REPO_ROOT / "sessions" / "permanent-results-registry.md"
VERDICT_FILE = REPO_ROOT / "computations" / "session-86" / "s86_gate_verdicts.txt"

GATE_ID = "S86-SINGLE-NAME-CONFLATION-METHODOLOGY-ENTRY"

SECTION_ANCHOR = "§VII.R"
KEYWORD = "single-name conflation"
WITNESS_REQUIRED = {"2A", "2B", "6A", "W12-2"}
CROSSREF_TARGET = "§VII.S"


def sha256_path(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def extract_section(text: str, anchor: str) -> str:
    """Extract from a `## §VII.X` header up to the next `## §` header."""
    pattern = re.compile(  # (local)
        rf"^## {re.escape(anchor)}.*?(?=^## §|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    m = pattern.search(text)  # (local)
    return m.group(0) if m else ""


def main() -> int:
    pins: dict[str, str] = {  # (local)
        "permanent-results-registry.md": sha256_path(REGISTRY),
    }
    print("=" * 76)
    print(f"{GATE_ID} — input-pin SHAs:")
    for k, v in pins.items():
        print(f"  {k}: {v}")
    print("=" * 76)

    text = REGISTRY.read_text(encoding="utf-8")  # (local)
    block = extract_section(text, SECTION_ANCHOR)  # (local)
    block_lines = len(block.splitlines())  # (local)
    print(f"Section {SECTION_ANCHOR} found: {bool(block)}; lines: {block_lines}")

    # Witnesses: present iff the witness ID appears as a numbered list
    # ("1. **2A SECTOR-1...", "2. **2B R_JK...", "3. **6A ρ...", "4. **W12-2 bare K...").
    witness_present: dict[str, bool] = {}  # (local)
    for w in WITNESS_REQUIRED:
        # Match witness ID at the start of a witness-line (after a digit-period
        # or after **bold** opener within the same line) — keep it loose
        # but require the witness token verbatim.
        witness_present[w] = bool(re.search(rf"\*\*{re.escape(w)}\b", block))
    W_set = {w for w, ok in witness_present.items() if ok}  # (local)

    K = KEYWORD in block  # (local)
    X = CROSSREF_TARGET in block  # (local)

    print(f"Witnesses present: {witness_present}")
    print(f"Keyword '{KEYWORD}': {K}")
    print(f"Cross-reference to {CROSSREF_TARGET}: {X}")

    pass_predicate = (W_set == WITNESS_REQUIRED) and K and X  # (local)
    verdict = "PASS" if pass_predicate else "FAIL"  # (local)

    audit_payload = "|".join(f"{k}:{v}" for k, v in sorted(pins.items()))  # (local)
    audit_sha = hashlib.sha256(audit_payload.encode()).hexdigest()  # (local)

    content_payload = (  # (local)
        f"{GATE_ID}|section={SECTION_ANCHOR}|lines={block_lines}"
        f"|W={sorted(W_set)}|K={K}|X={X}"
    )
    content_sha = hashlib.sha256(content_payload.encode()).hexdigest()  # (local)

    canonical_line = (  # (local)
        f"{GATE_ID}: {verdict} -- value={block_lines} "
        f"scheme=permanent_results_registry convention=methodology_entry "
        f"L_max=N/A sha256={audit_sha}"
    )
    companion_line = (  # (local)
        f"# audit_sha256_short={audit_sha[:16]} content_sha256={content_sha} "
        f"audit_sha256={audit_sha}"
    )

    with VERDICT_FILE.open("a", encoding="utf-8") as f:
        f.write(canonical_line + "\n")
        f.write(companion_line + "\n")

    print()
    print(canonical_line)
    print(companion_line)
    print(f"\n4-tuple: (value={block_lines}, scheme=permanent_results_registry, "
          f"convention=methodology_entry, L_max=N/A)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
