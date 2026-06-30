"""Build summary/session-73b-final.md verbatim from session-73b sources."""
import os

ROOT = r"C:\sandbox\Ainulindale Exflation"
SRC = os.path.join(ROOT, "sessions", "session-73b")
OUT = os.path.join(ROOT, "summary", "session-73b-final.md")

# Categorization of source files
master_post = []  # no master rollups exist for 73b separately
workshops = [
    "session-73b-landau-baptista-workshop.md",
    "session-73b-mack-vdd-workshop.md",
    "session-73b-phonon-first-hawking-workshop.md",
]
agent_collabs = [
    "session-73b-dirac-synthesis.md",
    "session-73b-sp-synthesis.md",
    "session-73b-tesla-synthesis.md",
]
outputs = [
    "session-73b-results-workingpaper.md",
]

all_sources = master_post + workshops + agent_collabs + outputs

# Build header
src_list = ", ".join(master_post + workshops + agent_collabs + outputs)
header = f"""# Session 73b - Comprehensive Summary

_Built from: {src_list}_

---

## Master Post-Workshop Synthesis

(No standalone master synthesis / way-forward / cross-workshop rollup file exists in `sessions/session-73b/`. The session's master-level synthesis is encoded in §I.A of `session-73b-results-workingpaper.md` (Master Gate AUDIT-GAUNTLET-73B) and in the per-workshop verdict tables below.)

---

## Workshop Documents

"""

with open(OUT, "w", encoding="utf-8", newline="\n") as out:
    out.write(header)

    for fname in workshops:
        path = os.path.join(SRC, fname)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        out.write(f"### {fname}\n\n")
        out.write(content)
        out.write("\n\n---\n\n")

    out.write("## Per-Agent Reviewer Collabs\n\n")
    for fname in agent_collabs:
        path = os.path.join(SRC, fname)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        out.write(f"### {fname}\n\n")
        out.write(content)
        out.write("\n\n---\n\n")

    out.write("## Outputs / Gate Verdicts / Computational Results\n\n")
    for fname in outputs:
        path = os.path.join(SRC, fname)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        out.write(f"### {fname}\n\n")
        out.write(content)
        out.write("\n\n---\n\n")

print("WROTE:", OUT)
print("SIZE:", os.path.getsize(OUT), "bytes")
for fname in all_sources:
    p = os.path.join(SRC, fname)
    print(f"  {fname}: {os.path.getsize(p)} bytes")
