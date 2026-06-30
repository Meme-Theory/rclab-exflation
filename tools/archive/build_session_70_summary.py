"""Build session-70-final.md by verbatim concatenation of source files."""
from pathlib import Path

ROOT = Path(r"C:\sandbox\Ainulindale Exflation")
SRC_DIR = ROOT / "sessions" / "session-70"
OUT = ROOT / "summary" / "session-70-final.md"

# Source ordering: master synthesis files (per-agent), workshops, results workingpaper
master_synthesis = [
    "session-70-connes-synthesis.md",
    "session-70-gen-physicist-synthesis.md",
]
workshops = [
    "session-70-hawking-phonon-first-workshop.md",
    "session-70-landau-lizzi-workshop.md",
    "session-70-van-den-dungen-mack-workshop.md",
]
outputs = [
    "session-70-results-workingpaper.md",
]

all_sources = master_synthesis + workshops + outputs

def read_full(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")

parts = []
parts.append("# Session 70 — Comprehensive Summary\n\n")
parts.append("_Built from: " + ", ".join(all_sources) + "_\n\n")
parts.append("---\n\n")

# Master synthesis
parts.append("## Master Post-Workshop Synthesis\n\n")
for fname in master_synthesis:
    parts.append(f"### {fname}\n\n")
    parts.append(read_full(SRC_DIR / fname))
    parts.append("\n\n")
parts.append("---\n\n")

# Workshops
parts.append("## Workshop Documents\n\n")
for fname in workshops:
    parts.append(f"### {fname}\n\n")
    parts.append(read_full(SRC_DIR / fname))
    parts.append("\n\n")
parts.append("---\n\n")

# Outputs
parts.append("## Outputs / Gate Verdicts / Computational Results\n\n")
for fname in outputs:
    parts.append(f"### {fname}\n\n")
    parts.append(read_full(SRC_DIR / fname))
    parts.append("\n\n")

content = "".join(parts)
OUT.write_text(content, encoding="utf-8")

# Report
print(f"Wrote {OUT}")
print(f"Total bytes: {len(content.encode('utf-8'))}")
print(f"Source count: {len(all_sources)}")
for f in all_sources:
    p = SRC_DIR / f
    print(f"  {f}: {p.stat().st_size} bytes")
