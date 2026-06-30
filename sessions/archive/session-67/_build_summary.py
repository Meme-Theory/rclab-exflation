"""Build comprehensive session-67-final.md by verbatim concatenation of all session sources."""
import os

ROOT = r"C:\sandbox\Ainulindale Exflation"
SRC_DIR = os.path.join(ROOT, "sessions", "session-67")
OUT_PATH = os.path.join(ROOT, "summary", "session-67-final.md")

# Files in this session, classified
MASTER_SYNTHESIS = ["session-67-synthesis.md"]
WORKSHOP_DOCS = ["session-67-transit-phonon-first-workshop.md"]
PER_AGENT_COLLABS = []  # none in this session
RESULTS_OUTPUTS = ["session-67-results-workingpaper.md"]

ALL_SOURCES = MASTER_SYNTHESIS + WORKSHOP_DOCS + PER_AGENT_COLLABS + RESULTS_OUTPUTS


def read_file(name):
    path = os.path.join(SRC_DIR, name)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def section(title, files):
    out = [f"## {title}\n"]
    if not files:
        out.append("_(none)_\n")
        return "\n".join(out)
    for fn in files:
        content = read_file(fn)
        out.append(f"### {fn}\n")
        out.append(content)
        out.append("\n")
    return "\n".join(out)


def main():
    parts = []
    parts.append("# Session 67 — Comprehensive Summary\n")
    parts.append(f"_Built from: {', '.join(ALL_SOURCES)}_\n")
    parts.append("---\n")
    parts.append(section("Master Post-Workshop Synthesis", MASTER_SYNTHESIS))
    parts.append("---\n")
    parts.append(section("Workshop Documents", WORKSHOP_DOCS))
    parts.append("---\n")
    parts.append(section("Per-Agent Reviewer Collabs", PER_AGENT_COLLABS))
    parts.append("---\n")
    parts.append(section("Outputs / Gate Verdicts / Computational Results", RESULTS_OUTPUTS))

    output = "\n".join(parts)

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(output)

    size = os.path.getsize(OUT_PATH)
    print(f"Wrote {OUT_PATH}")
    print(f"Final size: {size} bytes ({size / 1024:.1f} KB)")
    print(f"Sources concatenated: {len(ALL_SOURCES)}")
    for fn in ALL_SOURCES:
        path = os.path.join(SRC_DIR, fn)
        sz = os.path.getsize(path)
        print(f"  - {fn}: {sz} bytes ({sz / 1024:.1f} KB)")


if __name__ == "__main__":
    main()
