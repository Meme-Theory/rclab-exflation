"""S86-PRR-THREE-LAYER-ADJUDICATION — W0b-3 producing script.

Verifies the §VII.S methodology entry was landed with keyword + 3 layers +
generalization-clause substring + R7 cross-reference, then emits the verdict
line per .claude/rules/gate-verdicts.md.

PASS iff:
  K = "three-layer adjudication for joint-channel ρ verdicts"  (keyword present)
  G = "joint-channel gate quoting ρ between two observables sharing a substrate parameter"  (generalization clause)
  L = {"LAYER-1", "LAYER-2", "LAYER-3"}  (all three layer names present)
  X = "§VII.R" cross-reference present

  PASS_predicate = K AND G AND (L == L_required) AND X
"""

from canonical_constants import c_fabric  # noqa: F401
import hashlib
import pathlib
import re
import sys


REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
REGISTRY = REPO_ROOT / "sessions" / "permanent-results-registry.md"
VERDICT_FILE = REPO_ROOT / "computations" / "session-86" / "s86_gate_verdicts.txt"

GATE_ID = "S86-PRR-THREE-LAYER-ADJUDICATION"

SECTION_ANCHOR = "§VII.S"
KEYWORD = "three-layer adjudication for joint-channel ρ verdicts"
GENERALIZATION_CLAUSE = (
    "joint-channel gate quoting ρ between two observables that share a substrate parameter"
)
LAYER_REQUIRED = {"LAYER-1", "LAYER-2", "LAYER-3"}
CROSSREF_TARGET = "§VII.R"


def sha256_path(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def extract_section(text: str, anchor: str) -> str:
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

    K = KEYWORD in block  # (local)
    G = GENERALIZATION_CLAUSE in block  # (local)
    L_set = {ln for ln in LAYER_REQUIRED if ln in block}  # (local)
    X = CROSSREF_TARGET in block  # (local)

    print(f"Keyword present: {K}")
    print(f"Generalization clause present: {G}")
    print(f"Layers present: {L_set}")
    print(f"Cross-reference {CROSSREF_TARGET}: {X}")

    pass_predicate = K and G and (L_set == LAYER_REQUIRED) and X  # (local)
    verdict = "PASS" if pass_predicate else "FAIL"  # (local)

    audit_payload = "|".join(f"{k}:{v}" for k, v in sorted(pins.items()))  # (local)
    audit_sha = hashlib.sha256(audit_payload.encode()).hexdigest()  # (local)

    content_payload = (  # (local)
        f"{GATE_ID}|section={SECTION_ANCHOR}|lines={block_lines}"
        f"|K={K}|G={G}|L={sorted(L_set)}|X={X}"
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
