"""Inspect data.js for closed_454 in the CLOSED_MECHANISMS section."""
import re
from pathlib import Path

js = (Path(__file__).resolve().parent / "viz" / "console" / "data.js").read_text(encoding="utf-8")

start = js.index('const CLOSED_MECHANISMS = [')
# Naive: read until next 'const ' or end of file
next_const = js.find('const ', start + 30)
section = js[start:next_const if next_const > 0 else len(js)]

print(f"CLOSED_MECHANISMS section length: {len(section):,} chars")

# Search for closed_454
for m in re.finditer(r"closed_454", section):
    a = max(0, m.start() - 300)
    b = min(len(section), m.end() + 300)
    print("--- match @", m.start(), "---")
    print(section[a:b])
    print()

# Also search for "Inventory row" in the same section
for m in re.finditer(r'"Inventory row"', section):
    a = max(0, m.start() - 300)
    b = min(len(section), m.end() + 300)
    print("--- 'Inventory row' in CLOSED_MECHANISMS @", m.start(), "---")
    print(section[a:b])
    print()
