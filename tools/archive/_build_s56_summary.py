"""Build comprehensive session-56-final.md by concatenating verbatim S56 source files."""
import os

ROOT = r"C:\sandbox\Ainulindale Exflation"
SRC = os.path.join(ROOT, "sessions", "session-56")
OUT = os.path.join(ROOT, "summary", "session-56-final.md")

def read(name):
    with open(os.path.join(SRC, name), "r", encoding="utf-8") as f:
        return f.read()

# Source file listing
master_files = [
    "session-56-final-synthesis.md",
]
topic_files = [
    "session-56-dm-synthesis.md",
]
workshop_files = [
    "session-56-workshop-teams.md",
    "session-56-workshop-1-firewall.md",
    "session-56-workshop-2-cc-formula.md",
    "session-56-workshop-3-transit.md",
    "session-56-workshop-4-predictions.md",
]
followup_collab_files = [
    "session-56-final-synthesis-cw-collab.md",
    "session-56-final-synthesis-naz-collab.md",
]
collab_files = [
    "session-56-bap-collab.md",
    "session-56-berry-collab.md",
    "session-56-connes-collab.md",
    "session-56-cw-collab.md",
    "session-56-dirac-collab.md",
    "session-56-einstein-collab.md",
    "session-56-feynman-collab.md",
    "session-56-foam-collab.md",
    "session-56-gen-collab.md",
    "session-56-hawking-collab.md",
    "session-56-kaku-collab.md",
    "session-56-kitaev-collab.md",
    "session-56-kk-collab.md",
    "session-56-landau-collab.md",
    "session-56-lrd-collab.md",
    "session-56-naz-collab.md",
    "session-56-neutrino-collab.md",
    "session-56-paasch-collab.md",
    "session-56-phonon-collab.md",
    "session-56-qa-collab.md",
    "session-56-sagan-collab.md",
    "session-56-sp-collab.md",
    "session-56-spectral-collab.md",
    "session-56-string-collab.md",
    "session-56-tesla-collab.md",
    "session-56-vol-collab.md",
]
output_files = [
    "session-56-results-workingpaper.md",
]

all_sources = (
    master_files + topic_files + workshop_files
    + followup_collab_files + collab_files + output_files
)

parts = []
parts.append("# Session 56 -- Comprehensive Summary\n")
parts.append("\n_Built from S56 post-workshop documents._\n")
parts.append("\n_Source files:_\n")
for f in all_sources:
    parts.append(f"- `{f}`\n")
parts.append("\n---\n\n")

# Master Post-Workshop Synthesis
parts.append("## Master Post-Workshop Synthesis (Final Synthesis)\n\n")
parts.append(read("session-56-final-synthesis.md"))
parts.append("\n\n---\n\n")

# DM Topic Synthesis
parts.append("## DM Topic Synthesis\n\n")
parts.append(read("session-56-dm-synthesis.md"))
parts.append("\n\n---\n\n")

# Workshop Documents
parts.append("## Workshop Documents\n\n")
for wf in workshop_files:
    label = wf.replace("session-56-", "").replace(".md", "")
    parts.append(f"### {label}\n\n")
    parts.append(read(wf))
    parts.append("\n\n")
parts.append("---\n\n")

# Post-Synthesis Follow-up Collabs (CW, Naz on final synthesis)
parts.append("## Post-Synthesis Follow-up Collabs\n\n")
for cf in followup_collab_files:
    label = cf.replace("session-56-", "").replace(".md", "")
    parts.append(f"### {label}\n\n")
    parts.append(read(cf))
    parts.append("\n\n")
parts.append("---\n\n")

# Per-Agent Reviewer Collabs
parts.append("## Per-Agent Reviewer Collabs\n\n")
for cf in collab_files:
    label = cf.replace("session-56-", "").replace("-collab.md", "")
    parts.append(f"### {label}\n\n")
    parts.append(read(cf))
    parts.append("\n\n")
parts.append("---\n\n")

# Outputs / Working Paper
parts.append("## Outputs / Results Working Paper\n\n")
for of in output_files:
    parts.append(read(of))
    parts.append("\n\n")

content = "".join(parts)

with open(OUT, "w", encoding="utf-8") as f:
    f.write(content)

size = os.path.getsize(OUT)
print(f"Wrote: {OUT}")
print(f"Size: {size} bytes ({size/1024:.1f} KB)")
print(f"Sources concatenated: {len(all_sources)}")
print(f"Sections: 6 (Master + DM Topic + Workshops + Followup-collabs + Per-Agent + Outputs)")
