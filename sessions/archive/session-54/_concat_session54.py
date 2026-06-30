"""Concatenate all session-54 source files into summary/session-54-final.md (verbatim).

Categorization (from the rebuild prompt):
- Master rollups: master-collab, way-forward, synthesis-collation, cross-workshop, post-workshop, framework-update
- Workshop docs: *-workshop.md AND *-workshop-synthesis.md
- Per-agent collabs: *-{agent}-collab.md and *-{agent}-synthesis.md (agent-specific, not workshop)
- Outputs: results-workingpaper, outputs, extraction, verdicts
"""

from pathlib import Path

SRC = Path(r"C:\sandbox\Ainulindale Exflation\sessions\archive\session-54")
OUT = Path(r"C:\sandbox\Ainulindale Exflation\summary\session-54-final.md")

# Enumerate all .md files
all_md = sorted(p.name for p in SRC.glob("session-54-*.md"))

# Bucket assignments (explicit per file from the ls listing)
master_files = [
    "session-54-master-collab.md",
    "session-54-master-workshop-synthesis.md",
]

workshop_files = [
    # Full transcripts + their syntheses, paired
    "session-54-nazarewicz-connes-workshop.md",
    "session-54-nazarewicz-connes-workshop-synthesis.md",
    "session-54-phonon-landau-workshop.md",
    "session-54-phonon-landau-workshop-synthesis.md",
    "session-54-qa-hawking-workshop.md",
    "session-54-qa-hawking-workshop-synthesis.md",
]

# Per-agent reviewer collabs (NOT workshop transcripts; pre-workshop reviewer reads)
agent_collab_files = [
    "session-54-baptista-collab.md",
    "session-54-feynman-collab.md",
    "session-54-phonon-collab.md",
    "session-54-qa-collab.md",
    "session-54-sp-collab.md",
    "session-54-tesla-collab.md",
    "session-54-volovik-collab.md",
]

outputs_files = [
    "session-54-results-workingpaper.md",
    "session-54-extraction-collabs.md",
    "session-54-extraction-workshops.md",
]

bucketed = set(master_files + workshop_files + agent_collab_files + outputs_files)
missing = [f for f in all_md if f not in bucketed]
if missing:
    raise SystemExit(f"Unbucketed files exist: {missing}")
extra = [f for f in bucketed if f not in all_md]
if extra:
    raise SystemExit(f"Listed files not on disk: {extra}")

def read_file(name: str) -> str:
    return (SRC / name).read_text(encoding="utf-8", errors="replace")

source_list = ", ".join(master_files + workshop_files + agent_collab_files + outputs_files)

doc = []
doc.append("# Session 54 - Comprehensive Summary\n\n")
doc.append(f"_Built from: {source_list}_\n\n")
doc.append("---\n\n")
doc.append("## Master Post-Workshop Synthesis\n\n")
for f in master_files:
    body = read_file(f)
    doc.append(f"### {f}\n")
    doc.append(body)
    if not body.endswith("\n"):
        doc.append("\n")
    doc.append("\n")
doc.append("---\n\n")
doc.append("## Workshop Documents\n\n")
for f in workshop_files:
    body = read_file(f)
    doc.append(f"### {f}\n")
    doc.append(body)
    if not body.endswith("\n"):
        doc.append("\n")
    doc.append("\n")
doc.append("---\n\n")
doc.append("## Per-Agent Reviewer Collabs\n\n")
for f in agent_collab_files:
    body = read_file(f)
    doc.append(f"### {f}\n")
    doc.append(body)
    if not body.endswith("\n"):
        doc.append("\n")
    doc.append("\n")
doc.append("---\n\n")
doc.append("## Outputs / Gate Verdicts / Computational Results\n\n")
for f in outputs_files:
    body = read_file(f)
    doc.append(f"### {f}\n")
    doc.append(body)
    if not body.endswith("\n"):
        doc.append("\n")
    doc.append("\n")

OUT.write_text("".join(doc), encoding="utf-8")
print(f"WROTE: {OUT}")
print(f"BYTES: {OUT.stat().st_size}")
print(f"SOURCE FILE COUNT: {len(bucketed)}")
for f in master_files + workshop_files + agent_collab_files + outputs_files:
    print(f"  {f}: {(SRC / f).stat().st_size} bytes")
