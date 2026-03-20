#!/usr/bin/env python3
"""Analyze LaTeX mismatches more carefully."""
import json
import re

def main():
    with open("tools/knowledge-index.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    eqs = data.get("equations", [])

    has_latex = [eq for eq in eqs if eq.get("latex")]

    true_mismatches = []
    acceptable = []
    borderline = []

    backslash = chr(92)

    for eq in has_latex:
        raw = eq.get("raw", "")
        latex = eq.get("latex", "")
        eid = eq["id"]
        etype = eq.get("type", "unknown")

        # Normalize for comparison
        def clean(s):
            s = s.lower()
            s = re.sub(r"\\[a-z]+", " ", s)  # remove latex commands
            s = s.replace("{", "").replace("}", "")
            s = s.replace("_", "").replace("^", "")
            s = re.sub(r"[^a-z0-9. ]", " ", s)
            return set(s.split())

        raw_tokens = clean(raw)
        latex_tokens = clean(latex)

        # Remove trivial tokens
        trivial = {"", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c",
                    "d", "e", "f", "i", "j", "k", "n", "s", "t", "x", "y", "z",
                    "the", "is", "at", "of", "in", "for", "and", "to", "with", "from",
                    "text", "quad", "rm"}
        raw_tokens -= trivial
        latex_tokens -= trivial

        if not raw_tokens:
            acceptable.append(eid)
            continue

        overlap = len(raw_tokens & latex_tokens)
        ratio = overlap / len(raw_tokens)

        # Extract LHS variable from raw
        lhs_match = re.match(r"([A-Za-z_][A-Za-z_0-9'^{}()]*)\s*=", raw)
        if lhs_match:
            lhs = lhs_match.group(1).lower().replace("_", "").replace("^", "").replace("'", "")
            latex_clean = latex.lower().replace("_", "").replace("{", "").replace("}", "").replace("^", "")
            latex_clean = re.sub(r"\\[a-z]+", "", latex_clean)
            if len(lhs) >= 2 and lhs[:3] in latex_clean:
                acceptable.append(eid)
                continue

        if ratio >= 0.4:
            acceptable.append(eid)
        elif ratio >= 0.15:
            borderline.append((eid, etype, raw[:100], latex[:100], f"{overlap}/{len(raw_tokens)}", ratio))
        else:
            true_mismatches.append((eid, etype, raw[:120], latex[:120], f"{overlap}/{len(raw_tokens)}", ratio))

    print(f"Acceptable (correct LaTeX): {len(acceptable)}")
    print(f"Borderline: {len(borderline)}")
    print(f"TRUE mismatches (wrong equation in LaTeX): {len(true_mismatches)}")

    print("\n=== TRUE MISMATCHES (SEVERE) ===")
    for eid, etype, raw, latex, ratio_str, ratio in true_mismatches:
        print(f"\n  {eid} [{etype}] overlap={ratio:.0%} ({ratio_str}):")
        print(f"    RAW:   {raw}")
        print(f"    LATEX: {latex}")

    print("\n=== BORDERLINE ===")
    for eid, etype, raw, latex, ratio_str, ratio in borderline:
        print(f"\n  {eid} [{etype}] overlap={ratio:.0%} ({ratio_str}):")
        print(f"    RAW:   {raw}")
        print(f"    LATEX: {latex}")

if __name__ == "__main__":
    main()
