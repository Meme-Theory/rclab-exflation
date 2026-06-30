"""Rebuild summary/session-68-final.md as a verbatim concatenation of
all session-68 post-workshop content. Helper script — pure file I/O,
no transformation of source content."""
import os

ROOT = r"C:\sandbox\Ainulindale Exflation"
SRC = os.path.join(ROOT, "sessions", "session-68")
OUT = os.path.join(ROOT, "summary", "session-68-final.md")

# Categorize files
master_files = [
    "session-68-master-collab.md",
    "session-68-phonon-vs-data-plan.md",
]

workshop_files = [
    "session-68-landau-transit-workshop.md",
    "session-68-lizzi-transit-workshop.md",
    "session-68-volovik-mack-workshop.md",
]

agent_collab_files = [
    "session-68-workshops-baptista-collab.md",
    "session-68-workshops-einstein-collab.md",
    "session-68-workshops-mack-collab.md",
    "session-68-workshops-phonon-first-collab.md",
    "session-68-workshops-qa-collab.md",
    "session-68-workshops-sp-collab.md",
]

results_files = [
    "session-68-results-workingpaper.md",
]

all_files = master_files + workshop_files + agent_collab_files + results_files


def read_verbatim(fname):
    path = os.path.join(SRC, fname)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def section(files, header):
    parts = [f"\n---\n\n## {header}\n"]
    for fname in files:
        parts.append(f"\n### {fname}\n\n")
        parts.append(read_verbatim(fname))
        parts.append("\n")
    return "".join(parts)


sources_csv = ", ".join(all_files)

out_parts = [
    "# Session 68 — Comprehensive Summary\n",
    f"\n_Built from: {sources_csv}_\n",
    section(master_files, "Master Post-Workshop Synthesis"),
    section(workshop_files, "Workshop Documents"),
    section(agent_collab_files, "Per-Agent Reviewer Collabs"),
    section(results_files, "Outputs / Gate Verdicts / Computational Results"),
]

content = "".join(out_parts)

with open(OUT, "w", encoding="utf-8") as f:
    f.write(content)

size = os.path.getsize(OUT)
print(f"WROTE: {OUT}")
print(f"SIZE: {size} bytes")
print(f"SOURCES ({len(all_files)}):")
for fname in all_files:
    p = os.path.join(SRC, fname)
    print(f"  {os.path.getsize(p):>8}  {fname}")
