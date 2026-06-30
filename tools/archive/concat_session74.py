"""Concatenate all session-74 files into the comprehensive summary."""
import os

SRC = r"C:\sandbox\Ainulindale Exflation\sessions\session-74"
OUT = r"C:\sandbox\Ainulindale Exflation\summary\session-74-final.md"

# Order: master/post-workshop, workshops, syntheses (per-agent), outputs/results.
master_files = [
    # No master synthesis-collation/way-forward exists in the dir; closest is rf-analysis.
    "session-74-rf-analysis.md",
    "session-74-luxe-pre-registration.md",
    "session-74-tgf-pre-registration.md",
]
workshop_files = [
    "session-74-mack-landau-workshop.md",
    "session-74-qa-vdd-workshop.md",
    "session-74-tesla-mack-bells-workshop.md",
    "session-74-transit-einstein-workshop.md",
]
synth_files = [
    "session-74-einstein-synthesis.md",
    "session-74-hawking-synthesis.md",
    "session-74-lizzi-synthesis.md",
    "session-74-nazarewicz-synthesis.md",
    "session-74-sp-synthesis.md",
    "session-74-tesla-synthesis.md",
    "session-74-transit-synthesis.md",
    "session-74-volovik-synthesis.md",
]
results_files = [
    "session-74-results-workingpaper.md",
]

all_files = master_files + workshop_files + synth_files + results_files

with open(OUT, "w", encoding="utf-8") as out:
    out.write("# Session 74 -- Comprehensive Summary\n\n")
    out.write("_Built from: " + ", ".join(all_files) + "_\n\n")
    out.write("---\n\n")

    out.write("## Master Post-Workshop Synthesis\n\n")
    for f in master_files:
        path = os.path.join(SRC, f)
        out.write(f"### {f}\n\n")
        with open(path, "r", encoding="utf-8") as fp:
            out.write(fp.read())
        out.write("\n\n---\n\n")

    out.write("## Workshop Documents\n\n")
    for f in workshop_files:
        path = os.path.join(SRC, f)
        out.write(f"### {f}\n\n")
        with open(path, "r", encoding="utf-8") as fp:
            out.write(fp.read())
        out.write("\n\n---\n\n")

    out.write("## Per-Agent Reviewer Collabs\n\n")
    for f in synth_files:
        path = os.path.join(SRC, f)
        out.write(f"### {f}\n\n")
        with open(path, "r", encoding="utf-8") as fp:
            out.write(fp.read())
        out.write("\n\n---\n\n")

    out.write("## Outputs / Gate Verdicts / Computational Results\n\n")
    for f in results_files:
        path = os.path.join(SRC, f)
        out.write(f"### {f}\n\n")
        with open(path, "r", encoding="utf-8") as fp:
            out.write(fp.read())
        out.write("\n\n---\n\n")

# Report sizes
final_size = os.path.getsize(OUT)
print(f"FINAL SIZE: {final_size} bytes ({final_size/1024:.1f} KB)")
print(f"SOURCES: {len(all_files)}")
print()
print("Source file sizes:")
total_src = 0
for f in all_files:
    p = os.path.join(SRC, f)
    s = os.path.getsize(p)
    total_src += s
    print(f"  {f}: {s} bytes ({s/1024:.1f} KB)")
print(f"TOTAL SOURCE: {total_src} bytes ({total_src/1024:.1f} KB)")
