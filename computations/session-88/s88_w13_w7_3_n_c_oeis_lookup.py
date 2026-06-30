#!/usr/bin/env python3
"""
S88 W13-161 — S88-W7-3-N_C-OEIS-LOOKUP
======================================

Gate: S88-W7-3-N_C-OEIS-LOOKUP ([VERIFY])

Pre-registered threshold (per session-88-plan-w13.md §W13-161):
  PASS: ≥1 OEIS match with structural interpretation that aligns with
        substrate's C-γ-WEAK projection (e.g., "dimensions of irreps of
        SO(5)" or "partition counts at depth 5").
  FAIL: no OEIS hits, OR all hits are coincidental (no structural alignment).
  INFO: hits returned but interpretation ambiguous; document + route to S89.

Inputs (SHA-256 dual-pinned at runtime):
  - W7-3 SCHEMATIC verdict line at s87-axis-of-observation-anatomy-pin.md
    (knowledge MCP confirms n_c = (10, 10, 10, 11, 13) signature)
  - upstream W7-3 PRIMARY-LIFT verdict (#159) at
    computations/session-88/s88_gate_verdicts.txt:502 — FAIL with PRIMARY
    full-physical Pauli-Villars lift producing {1,1,1,1,1} (substrate-IS
    projection is {1,1,1,1,1}, NOT {10,10,10,11,13})
  - canonical_constants.py
  - this script's own bytes
  - OEIS query response timestamp (mcp__oeis__lookup_by_values)

Output 4-tuple:
  (value=<verdict-string>, scheme=mcp-oeis-lookup-by-values,
   convention=verbatim-w7-3-sequence-10-10-10-11-13, L_max=N/A)

Classification: NON-PHONONIC (external-database verification of an integer
signature; the verdict is interpretive, not a substrate-physics computation).

METHODOLOGY
-----------
1. The {n_c} = (10, 10, 10, 11, 13) integer-graded anomaly multiplier
   signature was emitted at the SCHEMATIC integer-graded layer in the W7-3
   workshop (s87-axis-of-observation-anatomy-pin.md).
2. Upstream gate #159 (S88-W7-3-C-GAMMA-WEAK-PRIMARY-LIFT) FAILed at full-
   physical Pauli-Villars lift; the substrate-IS C-γ-WEAK projection is
   {1, 1, 1, 1, 1}, NOT {10, 10, 10, 11, 13}. The {10,10,10,11,13}
   signature is therefore a SCHEMATIC-helper artifact, not a substrate-IS
   observable.
3. We perform the OEIS lookup as pre-registered to determine whether the
   SCHEMATIC signature corresponds to any known structural integer
   pattern — informative as a regulator-level interpretation, but the
   pre-registered PASS criterion ("alignment with substrate's C-γ-WEAK
   projection") is structurally moot post-#159.
4. mcp__oeis__lookup_by_values returned 8 hits; this script enumerates
   the top hits, classifies each by match-type and structural-
   interpretation, and emits the deterministic verdict per the literal
   pre-registered criterion.

DISCIPLINE
----------
- Imports canonical_constants (no values consumed; sentinel only).
- All locals tagged `# (local)`.
- Atomic single-write append for verdict line.
- Dual-SHA per S87+ schema.
- 4-tuple printed as final non-verdict line.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent  # (local)
COMPUTATIONS_DIR = SESSION_DIR.parent  # (local)
SHARED_DIR = COMPUTATIONS_DIR / "_shared"  # (local)
PROJECT_ROOT = COMPUTATIONS_DIR.parent  # (local)
sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import datetime as _dt
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Pre-registration constants
# ---------------------------------------------------------------------------
SESSION = "S88"  # (local)
GATE_ID = "S88-W7-3-N_C-OEIS-LOOKUP"  # (local)
SCHEME = "mcp-oeis-lookup-by-values"  # (local)
CONVENTION = "verbatim-w7-3-sequence-10-10-10-11-13"  # (local)
L_MAX = "N/A"  # (local)

# Verdict file (CANONICAL per gate-verdicts.md)
VERDICT_TXT = COMPUTATIONS_DIR / "session-88" / "s88_gate_verdicts.txt"  # (local)

# Output artifacts
OUT_JSON = SESSION_DIR / "s88_w13_w7_3_n_c_oeis_lookup.json"  # (local)
OUT_PNG = SESSION_DIR / "s88_w13_w7_3_n_c_oeis_lookup.png"  # (local)

# Pre-registered sequence
N_C_SEQUENCE = (10, 10, 10, 11, 13)  # (local) — W7-3 SCHEMATIC integer-graded multiplier

# ---------------------------------------------------------------------------
# Section 4 — SHA helpers (dual-SHA S87+ schema)
# ---------------------------------------------------------------------------

def sha256_file(p: Path) -> str:  # (local)
    h = hashlib.sha256()  # (local)
    h.update(p.read_bytes())
    return h.hexdigest()


def closure_hash(pins: dict) -> str:  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in sorted(pins.items()):
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — OEIS query response (recorded verbatim from mcp__oeis__lookup_by_values)
# ---------------------------------------------------------------------------
# Query: mcp__oeis__lookup_by_values([10, 10, 10, 11, 13], max_results=10)
# Response timestamp (UTC, ISO-8601):
OEIS_QUERY_TIMESTAMP = _dt.datetime(2026, 5, 6, 21, 0, 0, tzinfo=_dt.timezone.utc).isoformat()  # (local)

# Verbatim hits with first-terms enumeration (top-8 of 8 returned hits)
OEIS_HITS = [  # (local)
    {
        "id": "A067535",
        "name": "Smallest squarefree number >= n.",
        "first_terms": [1, 2, 3, 5, 5, 6, 7, 10, 10, 10, 11, 13, 13, 14, 15, 17, 17, 19, 19, 21],
        "keywords": ["nonn"],
        "author": "Reinhard Zumkeller",
        "date": "Jan 27 2002",
    },
    {
        "id": "A055748",
        "name": "A chaotic cousin of the Hofstadter-Conway sequence A004001.",
        "first_terms": [1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 7, 8, 8, 8, 8, 8, 8, 9],
        "keywords": ["nonn", "look"],
        "author": "N. J. A. Sloane",
        "date": "Jul 13 2000",
    },
    {
        "id": "A285735",
        "name": "a(1)=1, a(n) = least squarefree x such that x>n-x and n-x is also squarefree.",
        "first_terms": [1, 1, 2, 2, 3, 3, 5, 5, 6, 5, 6, 6, 7, 7, 10, 10, 10, 11, 13, 10],
        "keywords": ["nonn"],
        "author": "Antti Karttunen",
        "date": "May 02 2017",
    },
    {
        "id": "A132923",
        "name": "Triangle: T(n,k) = Fibonacci(k) + n - k.",
        "first_terms": [1, 2, 1, 3, 2, 2, 4, 3, 3, 3, 5, 4, 4, 4, 5, 6, 5, 5, 5, 6],
        "keywords": ["nonn", "tabl"],
        "author": "Gary W. Adamson",
        "date": "Sep 05 2007",
    },
    {
        "id": "A130766",
        "name": "3n+2 sandwiched by tripled 3n+1.",
        "first_terms": [1, 1, 1, 2, 4, 4, 4, 5, 7, 7, 7, 8, 10, 10, 10, 11, 13, 13, 13, 14],
        "keywords": ["nonn"],
        "author": "Paul Curtz",
        "date": "Aug 18 2007",
    },
    {
        "id": "A285509",
        "name": "a(1)=1; a(2)=a(3)=a(4)=2; a(n)=a(a(n-1)-1)+a(n-a(n-3)) for n>4.",
        "first_terms": [1, 2, 2, 2, 3, 4, 5, 5, 5, 5, 6, 8, 10, 10, 10, 9, 10, 10, 10, 10],
        "keywords": ["nonn", "look"],
        "author": "Altug Alkan",
        "date": "Apr 20 2017",
    },
    {
        "id": "A378771",
        "name": ("a(n) = least k such that the last k digits of m = A020666(n)^n "
                 "contain all 10 possible digits (0 through 9)."),
        "first_terms": [10, 10, 10, 11, 13, 11, 13, 17, 15, 16, 15, 15, 16, 18, 17, 15, 17, 15, 13, 16],
        "keywords": ["nonn", "easy", "base"],
        "author": "David A. Corneth",
        "date": "Dec 06 2024",
    },
    {
        "id": "A159624",
        "name": "a(n) = A159619(2n) - A159615(2n).",
        "first_terms": [3, 4, 5, 6, 6, 7, 9, 10, 10, 10, 10, 11, 13, 15, 17, 18, 18, 18, 18, 18],
        "keywords": ["nonn"],
        "author": "Vladimir Shevelev",
        "date": "Apr 17 2009",
    },
]


# ---------------------------------------------------------------------------
# Section 6 — Classification helpers
# ---------------------------------------------------------------------------

def classify_match_type(target: tuple, first_terms: list) -> dict:  # (local)
    """Determine match-type: exact-prefix / exact-substring / shifted / coincidental.

    Returns dict with keys: {match_type, position, span}.
    """
    n = len(target)  # (local)
    target_list = list(target)  # (local)
    # Exact prefix?
    if first_terms[:n] == target_list:
        return {"match_type": "exact-prefix", "position": 0, "span": n}
    # Exact substring (any offset > 0)?
    for offset in range(1, len(first_terms) - n + 1):
        if first_terms[offset:offset + n] == target_list:
            return {"match_type": "exact-substring", "position": offset, "span": n}
    # Should not happen given OEIS lookup fired, but classify as coincidental
    return {"match_type": "coincidental", "position": -1, "span": 0}


def classify_structural_interpretation(hit: dict) -> dict:  # (local)
    """Classify structural interpretation of an OEIS hit relative to the
    substrate's C-γ-WEAK projection.

    The substrate-IS C-γ-WEAK projection is {1, 1, 1, 1, 1} per upstream
    #159 PRIMARY-LIFT FAIL verdict at computations/session-88/s88_gate_verdicts.txt:502.
    The W7-3 SCHEMATIC signature {10, 10, 10, 11, 13} is therefore a
    SCHEMATIC-helper artifact, NOT a substrate-IS observable.

    Categories:
      - dimension-formula (Lie algebra irrep dimensions, partition function values)
      - partition-count (combinatorial counts at depth 5)
      - group-theoretic (orbit counts, character-table values)
      - number-theoretic-structural (squarefree, gcd-based)
      - hofstadter-class (recursive self-referential)
      - base-arithmetic (digit-property-based)
      - sandwich-pattern (constructed-by-formula triplet pattern)
      - coincidental (no structural alignment)
    """
    name = hit["name"].lower()  # (local)
    keywords = hit.get("keywords", [])  # (local)

    # Number-theoretic squarefree / divisibility families
    if "squarefree" in name:
        return {"category": "number-theoretic-structural",
                "substrate_alignment": "none",
                "rationale": ("Squarefree-floor / squarefree-decomposition number-theoretic "
                              "construction; no substrate-IS algebra-axis or partition-cardinality "
                              "interpretation.")}
    # Hofstadter-class chaotic recursive
    if "hofstadter" in name or "chaotic" in name:
        return {"category": "hofstadter-class",
                "substrate_alignment": "none",
                "rationale": ("Self-referential nested recursion (Hofstadter-Conway family); "
                              "no algebraic / Lie-theoretic interpretation.")}
    # Triangle Fibonacci
    if "fibonacci" in name:
        return {"category": "fibonacci-tabular",
                "substrate_alignment": "none",
                "rationale": ("Triangle of Fibonacci-shifted values; combinatorial but no "
                              "substrate-IS partition-class structural connection.")}
    # Sandwich-pattern / 3n+1 base arithmetic
    if "sandwich" in name or "3n+1" in name:
        return {"category": "sandwich-pattern",
                "substrate_alignment": "none",
                "rationale": ("Constructed by sandwiching tripled 3n+1 values around 3n+2; "
                              "purely arithmetic construction, no substrate connection.")}
    # Recursion with self-references (Hofstadter-class)
    if "look" in keywords:
        return {"category": "hofstadter-class",
                "substrate_alignment": "none",
                "rationale": ("OEIS 'look' keyword indicates visually-interesting irregular "
                              "sequence (typically Hofstadter-class); not algebra-axis-substrate-relevant.")}
    # Base/digit arithmetic
    if "base" in keywords or "digits" in name:
        return {"category": "base-arithmetic",
                "substrate_alignment": "none",
                "rationale": ("Base-10 digit-coverage construction; no algebraic / "
                              "partition-class interpretation.")}
    # A159619 - A159615 — derived quantities, no clear structural origin
    if "A15961" in hit["name"]:
        return {"category": "derived-difference",
                "substrate_alignment": "none",
                "rationale": ("Difference of two index-doubled OEIS sequences; derived "
                              "quantity with no direct substrate connection.")}
    # Default
    return {"category": "uncategorized",
            "substrate_alignment": "none",
            "rationale": "No matching structural category; treated as coincidental."}


# ---------------------------------------------------------------------------
# Section 7 — Run analysis
# ---------------------------------------------------------------------------

def analyze_hits(hits: list, target: tuple) -> dict:  # (local)
    table = []  # (local)
    for h in hits:
        mt = classify_match_type(target, h["first_terms"])  # (local)
        si = classify_structural_interpretation(h)  # (local)
        row = {
            "oeis_id": h["id"],
            "name": h["name"],
            "match_type": mt["match_type"],
            "position": mt["position"],
            "category": si["category"],
            "substrate_alignment": si["substrate_alignment"],
            "rationale": si["rationale"],
            "first_terms_snippet": h["first_terms"][:20],
        }  # (local)
        table.append(row)

    # Pre-registered PASS criterion: ≥1 hit with structural interpretation
    # aligning with substrate's C-γ-WEAK projection.
    aligned = [r for r in table if r["substrate_alignment"] == "aligned"]  # (local)
    coincidental_only = all(r["substrate_alignment"] == "none" for r in table)  # (local)

    # Enrich with substrate-IS context (post-#159 FAIL):
    # The C-γ-WEAK substrate-IS projection is {1,1,1,1,1}, not {10,10,10,11,13}.
    # The SCHEMATIC signature is a regulator-level artifact.
    return {
        "table": table,
        "aligned_hits": aligned,
        "coincidental_only": coincidental_only,
        "total_hits": len(table),
    }


def emit_plot(analysis: dict, target: tuple, out_png: Path) -> None:  # (local)
    fig, ax = plt.subplots(figsize=(10, 6))  # (local)
    target_x = list(range(len(target)))  # (local)
    ax.plot(target_x, list(target), marker="o", linewidth=2.5,
            color="black", label=f"W7-3 SCHEMATIC n_c = {target}", zorder=10)
    # Substrate-IS PRIMARY (post-#159 FAIL):
    primary = [1, 1, 1, 1, 1]  # (local)
    ax.plot(target_x, primary, marker="s", linewidth=2,
            color="red", linestyle="--",
            label="Substrate-IS PRIMARY (#159 FAIL): {1,1,1,1,1}", zorder=9)
    # Top hits (top 5 by relevance order in analysis)
    cmap = plt.get_cmap("tab10")  # (local)
    for i, row in enumerate(analysis["table"][:5]):
        # Find offset where the 5-tuple lives in the OEIS sequence
        ts = row["first_terms_snippet"]  # (local)
        pos = row["position"]  # (local)
        if pos >= 0:
            seg = ts[pos:pos + len(target)]  # (local)
        else:
            seg = ts[:len(target)]  # (local)
        ax.plot(target_x, seg, marker="x", linestyle=":",
                color=cmap(i), alpha=0.6,
                label=f"{row['oeis_id']}: {row['match_type']} @ pos {pos}")
    ax.set_xlabel("Class index c (5 partition classes)")
    ax.set_ylabel("n_c value")
    ax.set_title("S88-W7-3-N_C-OEIS-LOOKUP — SCHEMATIC signature vs OEIS hits + substrate PRIMARY")
    ax.legend(loc="best", fontsize=8)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(out_png, dpi=120)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 — Verdict assembly
# ---------------------------------------------------------------------------

def determine_verdict(analysis: dict) -> tuple:  # (local)
    """Apply pre-registered PASS criterion verbatim per plan §W13-161.

    PASS: ≥1 OEIS match with structural interpretation that aligns with
          substrate's C-γ-WEAK projection.
    FAIL: no hits, OR all hits coincidental (no structural alignment).
    INFO: hits returned but interpretation ambiguous.

    Substitution chain (verbatim per math-scripts.md §"Double-Check Logic"):
      Definition: substrate's C-γ-WEAK projection IS the integer signature
                  produced by the substrate-IS evaluation of the W7-3
                  observable at full-physical lift.
      Substitution: per upstream #159 PRIMARY-LIFT FAIL at
                    computations/session-88/s88_gate_verdicts.txt:502
                    (audit_sha256=f801167d...), substrate-IS PRIMARY = {1,1,1,1,1}.
                    The literal pre-registered PASS criterion asks for
                    alignment with {1,1,1,1,1} (the substrate-IS projection),
                    NOT alignment with {10,10,10,11,13} (the SCHEMATIC artifact
                    used as the OEIS query input).
      Simplify: zero of the 8 OEIS hits has first-terms {1,1,1,1,1};
                in fact, the OEIS lookup queried with {10,10,10,11,13}, NOT
                with {1,1,1,1,1}. Even if we re-read the criterion as
                "alignment with the queried sequence's structural meaning",
                all 8 hits fall in categories (squarefree, Hofstadter,
                Fibonacci-tabular, sandwich-pattern, base-arithmetic,
                derived-difference) with no algebra-axis / partition-class
                substrate connection.
      Direction: 0 aligned hits ⇒ FAIL per pre-registered criterion.
    """
    if len(analysis["aligned_hits"]) >= 1:
        return ("PASS",
                f"oeis_aligned_{len(analysis['aligned_hits'])}_of_{analysis['total_hits']}")
    if analysis["total_hits"] == 0:
        return ("FAIL", "no_oeis_hits")
    if analysis["coincidental_only"]:
        return ("FAIL",
                f"all_{analysis['total_hits']}_hits_coincidental_no_substrate_alignment")
    return ("INFO",
            f"oeis_hits_{analysis['total_hits']}_interpretation_ambiguous")


# ---------------------------------------------------------------------------
# Section 9 — Main
# ---------------------------------------------------------------------------

def main() -> int:  # (local)
    print("=" * 72)
    print(f"{GATE_ID} — W13-161 OEIS lookup on n_c = {N_C_SEQUENCE}")
    print("=" * 72)

    # Input SHA pinning (first 20 lines per template discipline)
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    verdict_path = VERDICT_TXT  # (local)

    sha_script = sha256_file(script_path)  # (local)
    sha_canonical = sha256_file(canonical_path)  # (local)
    # Pin upstream W7-3 PRIMARY-LIFT verdict line content (line 502-503)
    upstream_w7_3_primary_audit_sha = (
        "f801167d2b82c8011518c21359a5787732330e90b885fb02296a9cb205bce0ff"
    )  # (local) — from s88_gate_verdicts.txt:502
    # Pin OEIS sequence hash (verbatim sequence as input)
    n_c_str = ",".join(str(x) for x in N_C_SEQUENCE)  # (local)
    sha_n_c = hashlib.sha256(n_c_str.encode("utf-8")).hexdigest()  # (local)

    print(f"  script_sha256          = {sha_script}")
    print(f"  canonical_sha256       = {sha_canonical}")
    print(f"  upstream_W7-3_PRIMARY  = {upstream_w7_3_primary_audit_sha}")
    print(f"  n_c_sequence_sha256    = {sha_n_c}")
    print(f"  n_c_sequence           = {N_C_SEQUENCE}")
    print(f"  oeis_query_timestamp   = {OEIS_QUERY_TIMESTAMP}")
    print()

    # Run analysis
    analysis = analyze_hits(OEIS_HITS, N_C_SEQUENCE)  # (local)
    print(f"OEIS hits returned: {analysis['total_hits']}")
    print()
    print("Top-5 hit table (OEIS-ID × match-type × structural-interp × substrate-relevance):")
    print("-" * 72)
    for row in analysis["table"][:5]:
        print(f"  {row['oeis_id']:8s} | {row['match_type']:18s} @ pos {row['position']:3d} "
              f"| cat={row['category']:32s} | align={row['substrate_alignment']}")
    print()
    print(f"Coincidental-only?: {analysis['coincidental_only']}")
    print(f"Aligned hits     : {len(analysis['aligned_hits'])}")
    print()

    # Determine verdict per pre-registered criterion
    verdict, value_str = determine_verdict(analysis)  # (local)
    print(f"PRE-REGISTERED VERDICT: {verdict}")
    print(f"VALUE STRING          : {value_str}")
    print()

    # Substitution chain trace (printed in stdout)
    print("Substitution chain (per math-scripts.md):")
    print("  Step 1 (Definition)  : substrate's C-γ-WEAK projection = full-physical integer")
    print("                          signature at substrate-IS evaluation of W7-3 observable.")
    print(f"  Step 2 (Substitute)  : per #159 PRIMARY-LIFT FAIL (audit_sha={upstream_w7_3_primary_audit_sha[:16]}...),")
    print("                          substrate-IS PRIMARY = (1, 1, 1, 1, 1).")
    print(f"  Step 3 (Simplify)    : OEIS lookup queried with SCHEMATIC (10,10,10,11,13);")
    print(f"                          all 8 returned hits fall in non-substrate-aligned categories")
    print(f"                          (squarefree, Hofstadter, Fibonacci-tabular, sandwich-pattern,")
    print(f"                          base-arithmetic, derived-difference).")
    print(f"  Step 4 (Direction)   : 0 aligned hits ⇒ FAIL per pre-registered criterion.")
    print()

    # Emit plot
    emit_plot(analysis, N_C_SEQUENCE, OUT_PNG)
    print(f"Plot written: {OUT_PNG}")

    # Compose JSON output
    pinmap = {
        "script": sha_script,
        "canonical_constants": sha_canonical,
        "upstream_W7_3_primary_audit_sha": upstream_w7_3_primary_audit_sha,
        "n_c_sequence_sha256": sha_n_c,
        "oeis_query_timestamp": OEIS_QUERY_TIMESTAMP,
    }  # (local)
    audit_sha = closure_hash(pinmap)  # (local)
    content_sha = sha_script  # (local)

    out = {
        "gate_id": GATE_ID,
        "session": SESSION,
        "trigger": "[VERIFY]",
        "classification": "NON-PHONONIC",
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "n_c_sequence": list(N_C_SEQUENCE),
        "oeis_query_timestamp": OEIS_QUERY_TIMESTAMP,
        "oeis_hits_total": analysis["total_hits"],
        "oeis_hits": OEIS_HITS,
        "analysis_table": analysis["table"],
        "aligned_hits": analysis["aligned_hits"],
        "coincidental_only": analysis["coincidental_only"],
        "verdict": verdict,
        "value_string": value_str,
        "substitution_chain": {
            "step_1_definition": ("substrate's C-γ-WEAK projection = integer signature at "
                                  "substrate-IS full-physical lift"),
            "step_2_substitution": (f"per upstream #159 PRIMARY-LIFT FAIL "
                                    f"(audit_sha={upstream_w7_3_primary_audit_sha}), "
                                    f"substrate-IS PRIMARY projection = (1, 1, 1, 1, 1)"),
            "step_3_simplification": ("OEIS lookup queried with SCHEMATIC (10,10,10,11,13); "
                                      "all 8 returned hits in non-substrate-aligned categories "
                                      "(squarefree / Hofstadter / Fibonacci-tabular / "
                                      "sandwich-pattern / base-arithmetic / derived-difference)"),
            "step_4_direction": "0 aligned hits ⇒ FAIL per pre-registered criterion",
        },
        "input_pin_map": pinmap,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S87+",
        "substrate_framing": (
            "Container-thinking inversion preserved: the substrate IS the spectral "
            "triple at full-physical Pauli-Villars lift; the {10,10,10,11,13} "
            "SCHEMATIC signature is a regulator-helper artifact, not a substrate-IS "
            "observable. The OEIS lookup is a NON-PHONONIC external-database "
            "verification of whether the SCHEMATIC artifact corresponds to any "
            "known structural integer pattern. Outcome: no algebra-axis match; "
            "the SCHEMATIC signature is regulator-class-specific and does not "
            "correspond to any standard mathematical structure (Lie irrep "
            "dimensions, partition counts, group-theoretic counts)."
        ),
    }  # (local)
    OUT_JSON.write_text(json.dumps(out, indent=2))
    print(f"JSON  written: {OUT_JSON}")
    print()

    # Final 4-tuple line
    print(f"4-tuple: (value={value_str!r}, scheme={SCHEME}, convention={CONVENTION}, "
          f"L_max={L_MAX})")
    print(f"audit_sha256   = {audit_sha}")
    print(f"content_sha256 = {content_sha}")

    # Append verdict line (atomic single-write)
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value={value_str!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )  # (local)
    companion_line = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(companion_line)
    print()
    print(f"Verdict appended to: {VERDICT_TXT}")
    print(f"  {canonical_line.rstrip()}")
    print(f"  {companion_line.rstrip()}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
