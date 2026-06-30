"""Helper: build summary/session-72-final.md by verbatim concatenation."""
import os
from pathlib import Path

ROOT = Path(r"C:\sandbox\Ainulindale Exflation")
SRC = ROOT / "sessions" / "session-72"
OUT = ROOT / "summary" / "session-72-final.md"

# Categorized source files (order matters within section)
master_rollups = [
    "session-72-audit-master-synthesis.md",
    "session-72-sp-synthesis.md",
    "session-72-tesla-synthesis.md",
]

workshops = [
    "session-72-laminar-flow-workshop.md",
    "session-72-landau-baptista-workshop.md",
    "session-72-mack-vdd-workshop.md",
]

per_agent_collabs = [
    "session-72-laminar-flow-workshop-tesla-collab.md",
    "session-72-landau-baptista-workshop-connes-collab.md",
    "session-72-mack-vdd-workshop-phonon-first-collab.md",
    "session-72-audit-connes.md",
    "session-72-audit-gen-physicist.md",
    "session-72-audit-landau.md",
    "session-72-audit-mack.md",
    "session-72-audit-phonon-first.md",
    "session-72-audit-volovik.md",
]

results = [
    "session-72-results-workingpaper.md",
]

all_sources = master_rollups + workshops + per_agent_collabs + results

# Verify all exist
missing = [f for f in all_sources if not (SRC / f).exists()]
if missing:
    raise FileNotFoundError(f"Missing source files: {missing}")

def read_verbatim(name):
    p = SRC / name
    with open(p, "rb") as f:
        raw = f.read()
    # decode as utf-8, replace errors so we never lose bytes silently
    return raw.decode("utf-8", errors="replace")

def emit_section(parts, files):
    for fn in files:
        parts.append(f"### {fn}\n\n")
        parts.append(read_verbatim(fn))
        if not parts[-1].endswith("\n"):
            parts.append("\n")
        parts.append("\n")

parts = []
parts.append("# Session 72 — Comprehensive Summary\n\n")
parts.append("_Built from: " + ", ".join(all_sources) + "_\n\n")
parts.append("---\n\n")
parts.append("## Master Post-Workshop Synthesis\n\n")
emit_section(parts, master_rollups)
parts.append("---\n\n")
parts.append("## Workshop Documents\n\n")
emit_section(parts, workshops)
parts.append("---\n\n")
parts.append("## Per-Agent Reviewer Collabs\n\n")
emit_section(parts, per_agent_collabs)
parts.append("---\n\n")
parts.append("## Outputs / Gate Verdicts / Computational Results\n\n")
emit_section(parts, results)

content = "".join(parts)

OUT.parent.mkdir(parents=True, exist_ok=True)
with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    f.write(content)

# Report
final_size = OUT.stat().st_size
print(f"WROTE: {OUT}")
print(f"FINAL_SIZE_BYTES: {final_size}")
print(f"NUM_SOURCES: {len(all_sources)}")
print("SOURCES:")
for fn in all_sources:
    sz = (SRC / fn).stat().st_size
    print(f"  {sz:>8d}  {fn}")
total_src = sum((SRC / fn).stat().st_size for fn in all_sources)
print(f"TOTAL_SOURCE_BYTES: {total_src}")
print(f"OVERHEAD_BYTES: {final_size - total_src}")
