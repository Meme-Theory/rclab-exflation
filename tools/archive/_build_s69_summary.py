"""Build verbatim concatenated summary for session 69."""
import os
from pathlib import Path

SRC_DIR = Path(r"C:\sandbox\Ainulindale Exflation\sessions\session-69")
DST = Path(r"C:\sandbox\Ainulindale Exflation\summary\session-69-final.md")

# Categorize files
master_files = [
    "session-69-master-collab.md",
    "sagan-dismissal-ack.md",
]

workshop_files = [
    # No *-workshop.md or *-workshop-synthesis.md files in s69
    # but include the bucher singularity review as workshop-style document
    "s69-bucher-singularity-review.md",
]

collab_files = [
    "session-69-baptista-collab.md",
    "session-69-cosmic-web-collab.md",
    "session-69-dungen-collab.md",
    "session-69-lizzi-collab.md",
    "session-69-mack-collab.md",
    "session-69-phonon-first-collab.md",
    "session-69-sp-collab.md",
    "session-69-tesla-collab.md",
    "session-69-volovik-collab.md",
]

results_files = [
    "session-69-results-workingpaper.md",
]

all_files = master_files + workshop_files + collab_files + results_files

# Verify all exist
missing = [f for f in all_files if not (SRC_DIR / f).exists()]
if missing:
    raise SystemExit(f"Missing files: {missing}")

# Verify no orphan files
on_disk = sorted([p.name for p in SRC_DIR.iterdir() if p.is_file()])
known = sorted(all_files)
orphan = [f for f in on_disk if f not in known]
if orphan:
    raise SystemExit(f"Orphan files not categorized: {orphan}")

def read_file(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="replace")

# Build the output
parts = []
parts.append("# Session 69 — Comprehensive Summary\n\n")
parts.append("_Built from: " + ", ".join(all_files) + "_\n\n")
parts.append("---\n\n")

# Master Post-Workshop Synthesis
parts.append("## Master Post-Workshop Synthesis\n\n")
for fname in master_files:
    parts.append(f"### {fname}\n\n")
    parts.append(read_file(SRC_DIR / fname))
    parts.append("\n\n")
parts.append("---\n\n")

# Workshop Documents
parts.append("## Workshop Documents\n\n")
for fname in workshop_files:
    parts.append(f"### {fname}\n\n")
    parts.append(read_file(SRC_DIR / fname))
    parts.append("\n\n")
parts.append("---\n\n")

# Per-Agent Reviewer Collabs
parts.append("## Per-Agent Reviewer Collabs\n\n")
for fname in collab_files:
    parts.append(f"### {fname}\n\n")
    parts.append(read_file(SRC_DIR / fname))
    parts.append("\n\n")
parts.append("---\n\n")

# Outputs / Gate Verdicts / Computational Results
parts.append("## Outputs / Gate Verdicts / Computational Results\n\n")
for fname in results_files:
    parts.append(f"### {fname}\n\n")
    parts.append(read_file(SRC_DIR / fname))
    parts.append("\n\n")

content = "".join(parts)
DST.write_text(content, encoding="utf-8")

# Report
print(f"Wrote {DST}")
print(f"Final size: {DST.stat().st_size} bytes ({DST.stat().st_size/1024:.1f} KB)")
print(f"Number of sources: {len(all_files)}")
print()
print("Sources with sizes:")
for fname in all_files:
    sz = (SRC_DIR / fname).stat().st_size
    print(f"  {sz:>9} bytes  {fname}")

total_src = sum((SRC_DIR / f).stat().st_size for f in all_files)
print(f"\nTotal source size: {total_src} bytes ({total_src/1024:.1f} KB)")
