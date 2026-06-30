"""S85 carry-forward context file builder.

Mines Carry-Forward sections from all 19 S84 synthesis files (§V for most,
§IX for s2-landau and s4-mack; §V renamed for s3-gen), deduplicates by
title + gate_id, writes sessions/session-plan/session-85-context.md per
/rclab-plan skill §2e template.

NO interpretation. Pure mechanical extraction + dedup. Replaces the
stalled Phase 2 gen-physicist agent (which stopped at table-build step
after successfully extracting 169 raw entries).
"""

from pathlib import Path
import re
import sys
from collections import defaultdict

# Compliance import per .claude/rules/math-scripts.md (no constants used — text-only script)
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import *  # noqa: F401,F403

ROOT = Path(r"C:\sandbox\Ainulindale Exflation")
S84 = ROOT / "sessions" / "session-84"
OUT = ROOT / "sessions" / "session-plan" / "session-85-context-raw.md"
PARTITION_OUT = ROOT / "sessions" / "session-plan" / "session-85-partition.md"

# Reviewer-origin → subagent_type (per /rclab-plan §2.7a step 3)
OWNER_MAP = {
    "mack":             "mack-cosmic-bridge",
    "connes":           "connes-ncg-theorist",
    "transit":          "transit-dynamics-theorist",
    "tesla":            "tesla-resonance",
    "landau":           "landau-condensed-matter-theorist",
    "sp":               "schwarzschild-penrose-geometer",
    "feynman":          "feynman-theorist",
    "kaku":             "kaku-speculative-theorist",
    "little-red-dots":  "little-red-dots-jwst-analyst",
    "lizzi":            "lizzi-spectral-functional-theorist",
    "van-den-dungen":   "van-den-dungen-bridge-theorist",
    "volovik":          "volovik-superfluid-universe-theorist",
    "gen-physicist":    "gen-physicist",
}

WAVE_SIZE_MAX = 13   # (local) target upper bound for any single wave
WAVE_SIZE_MIN = 6    # (local) below this, warn (but don't merge — preserve reviewer ownership)

# (filename, cf_section_start_line, next_section_start_line, reviewer_origin)
# Line numbers are 1-indexed; both from Grep. Body slice = [start+1, next_section-1].
SOURCES = [
    ("session-84-feynman-synthesis.md",             159, 223, "feynman"),
    ("session-84-sp-synthesis.md",                  178, 248, "sp"),
    ("session-84-tesla-synthesis.md",               171, 271, "tesla"),
    ("session-84-transit-synthesis.md",             215, 279, "transit"),
    ("session-84-mack-synthesis.md",                225, 349, "mack"),
    ("session-84-s1-connes-alpha_s-synthesis.md",   246, 301, "connes"),
    ("session-84-s1-landau-alpha_s-synthesis.md",   268, 321, "landau"),
    ("session-84-s1-mack-alpha_s-synthesis.md",     162, 214, "mack"),
    ("session-84-s2-volovik-kcorridor-synthesis.md",134, 180, "volovik"),
    ("session-84-s2-landau-kcorridor-synthesis.md", 233, 279, "landau"),  # §IX
    ("session-84-s3-kaku-elimination-synthesis.md", 203, 267, "kaku"),
    ("session-84-s3-gen-elimination-synthesis.md",  252, 269, "gen-physicist"),  # §V renamed
    ("session-84-s4-lrd-falsifier-synthesis.md",    373, 439, "little-red-dots"),
    ("session-84-s4-mack-falsifier-synthesis.md",   354, 373, "mack"),  # §IX
    ("session-84-s5-connes-cohomology-synthesis.md",207, 247, "connes"),
    ("session-84-s5-lizzi-cohomology-synthesis.md", 124, 176, "lizzi"),
    ("session-84-s5-vdd-cohomology-synthesis.md",   267, 313, "van-den-dungen"),
    ("session-84-transit-CCrevisit-synthesis.md",   149, 221, "transit"),
    ("session-84-connes-CCrevisit-synthesis.md",    156, 224, "connes"),
]

# Entry-boundary prefixes seen across the 19 files:
#   V.1  V.1.  V.10  V.5a
#   CF-1  CF-6  CF-W4.1  CF-W4.2  CF-M1  CF-M10
#   ELIM-1  ELIM-8
ENTRY_PREFIX_RE = re.compile(
    r"^(?:#{1,6}\s+|\*\*)?"                        # optional header marks or bold
    r"(V\.\d+[a-z]?\.?"                            # V.1 / V.1. / V.5a
    r"|CF-W?\d+(?:\.\d+)?"                         # CF-1 / CF-W4.1
    r"|CF-M\d+"                                    # CF-M1
    r"|ELIM-\d+[a-z]?"                             # ELIM-1 / ELIM-5a
    r")"
    r"[\s:.\*]",                                   # followed by whitespace/colon/period/bold-close
    re.MULTILINE,
)

FIELD_TEMPLATE = (
    r"\*\*{field}\*\*[\s:]+(.+?)"
    r"(?=\n\s*[-*]?\s*\*\*(?:What|Inputs?|Gate|Effort|Owner|Priority|Agent)\*\*"
    r"|\n\s*(?:---|\*\*Cascade|\*\*Cross-check|\*\*Note)"
    r"|\Z)"
)
FIELD_RE = {
    "what":   re.compile(FIELD_TEMPLATE.format(field="What"),    re.DOTALL | re.IGNORECASE),
    "inputs": re.compile(FIELD_TEMPLATE.format(field="Inputs?"), re.DOTALL | re.IGNORECASE),
    "gate":   re.compile(FIELD_TEMPLATE.format(field="Gate"),    re.DOTALL | re.IGNORECASE),
    "effort": re.compile(FIELD_TEMPLATE.format(field="Effort"),  re.DOTALL | re.IGNORECASE),
}

# Explicit gate-ID-looking tokens, e.g. CC-1, DR3-L9, DILUTION-CC-66, S85-W1-G3
GATE_ID_RE = re.compile(
    r"\b(CC-[A-Z0-9\-Γγ]+"   # CC-1, CC-Γ, CC-gamma
    r"|DR\d+-[A-Z0-9\-]+"
    r"|DILUTION-[A-Z0-9\-]+"
    r"|S\d+-W\d+[a-zA-Z]?-[A-Z0-9\-]+"
    r"|[A-Z]{3,}-[A-Z][A-Z0-9\-]{2,})"
)

def read_section(filename, start_hdr, next_hdr):
    fp = S84 / filename
    text = fp.read_text(encoding="utf-8")
    lines = text.splitlines()
    # start_hdr is 1-indexed line of the "## V." or "## IX." header.
    # Body = lines [start_hdr+1 .. next_hdr-1] inclusive (1-indexed).
    # In 0-indexed Python: lines[start_hdr : next_hdr-1]
    body = lines[start_hdr:next_hdr - 1]
    return "\n".join(body)


TABLE_HEADER_RE = re.compile(
    r"^\|\s*#\s*\|\s*What\s*\|\s*Inputs?\s*\|\s*Gate\s*\|\s*Effort\s*\|",
    re.MULTILINE | re.IGNORECASE,
)
TABLE_ID_RE = re.compile(
    r"^(V\.\d+[a-z]?|CF-W?\d+(?:\.\d+)?|CF-M\d+|ELIM-\d+[a-z]?)\b",
    re.IGNORECASE,
)


def parse_table_entries(section_text):
    """If §body is a markdown table with columns '# | What | Inputs | Gate | Effort',
    parse each data row as one entry. Returns list of (raw_id, synthetic_block) or []."""
    hdr = TABLE_HEADER_RE.search(section_text)
    if not hdr:
        return []
    lines = section_text[hdr.start():].splitlines()
    # Skip header + alignment row
    rows = lines[2:]
    out = []
    for line in rows:
        if not line.startswith("|"):
            break
        parts = [p.strip() for p in line.strip("|").split("|")]
        if len(parts) < 5:
            continue
        id_col = re.sub(r"\*", "", parts[0]).strip()
        id_m = TABLE_ID_RE.match(id_col)
        if not id_m:
            continue
        raw_id = id_m.group(1).rstrip(".")
        what, inputs, gate, effort = parts[1], parts[2], parts[3], parts[4]
        synth = (
            f"{raw_id}. {what[:80]}\n"
            f"- **What**: {what}\n"
            f"- **Inputs**: {inputs}\n"
            f"- **Gate**: {gate}\n"
            f"- **Effort**: {effort}\n"
        )
        out.append((raw_id, synth))
    return out


FIELD_PRESENCE_RE = re.compile(
    r"\*\*(?:What|Inputs?|Gate|Effort)\*\*",
    re.IGNORECASE,
)


def split_entries(section_text):
    # Prefer table-form if the section is a markdown table.
    table_entries = parse_table_entries(section_text)
    if table_entries:
        return table_entries
    matches = list(ENTRY_PREFIX_RE.finditer(section_text))
    blocks = []
    for i, m in enumerate(matches):
        raw_id = m.group(1).rstrip(".")
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(section_text)
        block = section_text[start:end]
        # Reject candidates that lack any of the 4 required fields within the block.
        # This filters out inline-reference hits like "V.7 precheck is required..."
        # that happen to start at line beginning but are prose, not real entries.
        if not FIELD_PRESENCE_RE.search(block):
            continue
        blocks.append((raw_id, block))
    return blocks


def extract_title(block, raw_id):
    first_line = block.split("\n", 1)[0]
    cleaned = re.sub(r"^#+\s*", "", first_line)
    cleaned = re.sub(r"^\*+", "", cleaned)
    cleaned = re.sub(rf"^{re.escape(raw_id)}[.:]?", "", cleaned, flags=re.IGNORECASE)
    cleaned = cleaned.strip(" *:—-\t")
    return cleaned if cleaned else "(untitled)"


def extract_fields(block):
    out = {}
    for key, rx in FIELD_RE.items():
        m = rx.search(block)
        if m:
            val = " ".join(m.group(1).strip().split())
            # Strip trailing markdown-bullets / closing stars
            val = val.rstrip(" *-")
            out[key] = val[:400]
        else:
            out[key] = ""
    return out


def extract_gate_id(block, raw_id, title):
    if raw_id and not raw_id.startswith("V."):
        return raw_id
    search_area = title + " " + block[:600]
    matches = GATE_ID_RE.findall(search_area)
    blacklist = {"CF-", "ELIM-", "PASS", "FAIL", "INFO", "PRU", "SHA"}
    candidates = [m for m in matches if not any(m.startswith(b) for b in blacklist)]
    return candidates[0] if candidates else ""


def canonicalize(title):
    return re.sub(r"[^a-z0-9]+", "", title.lower())


# ---------- Stage A: aggressive normalization ----------

_GREEK_MAP = {
    "η": "eta", "Η": "eta",
    "γ": "gamma", "Γ": "gamma",
    "ρ": "rho", "Ρ": "rho",
    "α": "alpha", "Α": "alpha",
    "β": "beta", "Β": "beta",
    "ζ": "zeta", "Ζ": "zeta",
    "τ": "tau", "Τ": "tau",
    "π": "pi", "Π": "pi",
    "μ": "mu", "Μ": "mu",
    "σ": "sigma", "Σ": "sigma",
    "δ": "delta", "Δ": "delta",
    "ε": "epsilon", "Ε": "epsilon",
    "χ": "chi", "Χ": "chi",
    "λ": "lambda", "Λ": "lambda",
    "ω": "omega", "Ω": "omega",
}

_GATE_SUFFIX_RE = re.compile(
    r"-(?:DERIVATION|CANONICAL|REFIT|LANDING|PRE-?REGISTRATION|PREREG|PRE-?REG|"
    r"AUDIT|CLOSURE|THEOREM|CHECK|PRECHECK|COMPUTATION|VERIFICATION|"
    r"TEST|TREE|SUCCESSOR|TIMELINE|JOINT|REGULATOR|INVARIANT)$",
    re.IGNORECASE,
)

_TITLE_WAVE_TAG_RE = re.compile(
    r"^(?:S\d+[-\s]+|W\d+[a-z]?[-\s]+\d+\s*[—:-]?\s*|\*\*.*?\*\*\s+—\s+)",
)


def _greek_to_latin(s):
    for g, lat in _GREEK_MAP.items():
        s = s.replace(g, lat)
    return s


def normalize_gate_id(gid):
    if not gid:
        return ""
    s = gid.strip()
    s = _greek_to_latin(s)
    # Strip session prefix (S84-, S85-, etc.) — may appear multiple times
    s = re.sub(r"^S\d+-", "", s, flags=re.IGNORECASE)
    # Strip wave prefix (W1a-, W4-, etc.)
    s = re.sub(r"^W\d+[a-zA-Z]?-", "", s, flags=re.IGNORECASE)
    # Drop suffix qualifier (iterative — may chain)
    prev = None
    while prev != s:
        prev = s
        s = _GATE_SUFFIX_RE.sub("", s)
    # Collapse multiple dashes
    s = re.sub(r"-+", "-", s).strip("-")
    return s.upper()


def normalize_title(title):
    t = _greek_to_latin(title)
    # Strip leading session markers and wave tags
    t = re.sub(r"^S\d+-\s*", "", t)
    t = re.sub(r"^W\d+[a-zA-Z]?-\d+\s*[—:.\-]?\s*", "", t, flags=re.IGNORECASE)
    # Drop parenthetical modifiers: (NEW, xyz-native), (PRIORITY N), (cf. W...), (W3-31 ...), (from ...)
    t = re.sub(
        r"\s*\([^)]*(?:NEW|UPDATED|REVISED|PRIORITY|cf\.?|W\d+|from|carry-?forward|"
        r"per\s|W\d+[a-z]?-\d+|formerly|was)[^)]*\)",
        "",
        t,
        flags=re.IGNORECASE,
    )
    # Drop trailing bold markers ** and asterisks
    t = re.sub(r"\*+", "", t)
    # Drop SHA-ish tokens
    t = re.sub(r"\bSHA[-:]?\s*[a-f0-9]{6,}", "", t, flags=re.IGNORECASE)
    t = re.sub(r"\b[a-f0-9]{8,}\b", "", t)  # long hex strings
    # Drop trailing dash-clauses with priority/pass/fail
    t = re.sub(r"\s*[—-]\s*(?:PRIORITY|PASS|FAIL|INFO|CRITICAL|HIGH|MEDIUM|LOW)\b.*$", "", t, flags=re.IGNORECASE)
    # Lowercase, strip, collapse
    return re.sub(r"[^a-z0-9]+", "", t.lower())


# ---------- Stage B: theme-bucket assignment ----------

# (bucket_name, regex patterns). First match wins.
THEME_BUCKETS = [
    # CC mechanism family
    ("cc-1-eta",               [r"\b(eta|η)\b.*\binvariant", r"\bCC-?1\b", r"\bCC-?(η|ETA)\b", r"APS\s+(η|eta)", r"aps-style"]),
    ("cc-2-triality",          [r"\bCC-?2\b", r"(Spin\(8\)|SO\(8\))\s+triality", r"\btriality\b"]),
    ("cc-3-connes-moscovici",  [r"\bCC-?3\b", r"Connes-?Moscovici", r"dimension\s+spectrum", r"signed\s+residue", r"\bHopf\b.*cocycle"]),
    ("cc-4-dai-freed",         [r"\bCC-?4\b", r"Dai-?Freed", r"pi_?4\(S\^?3\)", r"torsion\s+pairing"]),
    ("cc-5-multiplicative",    [r"\bCC-?5\b", r"multiplicative\s+identity", r"cluster\s+spans", r"asymptotic\s+refit"]),
    ("cc-6-parker",            [r"\bCC-?6\b", r"Parker\s+transit", r"parker.?residue", r"αβ\*|α_k\s*β_k"]),
    ("cc-gamma-impedance",     [r"\bCC-?(gamma|Γ)\b", r"impedance.?mismatch", r"effacement\s+residual", r"Gamma[-=\s]*0\.9997"]),

    # Structural theorems
    ("van-hove-cusp",          [r"[Vv]an\s*[Hh]ove", r"\bcusp\b", r"tau.?fold.*reform", r"first-?order\s+transit"]),
    ("jensen-triality",        [r"Jensen.+triality", r"Jensen.+precheck", r"triality.+preserv"]),
    ("ko-dim-pairing",         [r"\bKO-?dim\b", r"KO[-\s]?6", r"\[J,\s*D", r"j\s*operator.+kodim"]),
    ("poincare-dual-dmde",     [r"Poincar(é|e)", r"K_?0\(A_F\)", r"DM/DE.+summand", r"summand.+ratio", r"4/9"]),
    ("friedmann-bcs",          [r"Friedmann-?BCS", r"FRIEDMANN", r"wrong-?question"]),
    ("leggett-channel",        [r"Leggett", r"inter-?band", r"two-?fluid"]),

    # K-corridor family
    ("k-corridor-scan",        [r"K-?corridor", r"K-?scan", r"K_?substrate", r"mode-?partition", r"K-?floor", r"floor-?wall"]),

    # Regulator / scheme
    ("regulator-invariance",   [r"regulator(?!\s+shift).*invariance", r"\bZ_?R\b", r"\bZubarev\b", r"scheme-?dep", r"2-?loop", r"regulator.taxonomy"]),

    # Observational pre-registrations
    ("alpha-s-preregistration",[r"α_?s|alpha_?s", r"CMB-?S4", r"S50.+identity"]),
    ("beta-s-preregistration", [r"β_?s|beta_?s", r"β_?s.+pre-?reg"]),
    ("dr3-tree",               [r"\bDR3\b", r"R_?842", r"w_?0.*w_?a", r"DESI"]),
    ("litebird",               [r"LiteBIRD", r"n_?T.+CMB", r"r.+tensor-?to-?scalar", r"BB\s+polarization"]),
    ("bk-array",               [r"BK[-\s]?Array", r"BICEP.+Keck", r"BK2026"]),
    ("pixie",                  [r"PIXIE", r"μ-?distortion", r"mu-?distortion", r"FIRAS"]),
    ("lisa-cgwb",              [r"\bLISA\b", r"\bCGWB\b", r"Omega_?GW|Ω_?GW", r"stochastic.+GW"]),
    ("21cm",                   [r"21-?cm", r"folded-?shape", r"bispectrum"]),
    ("cmb-hd",                 [r"CMB-?HD", r"CMB.+high.+def"]),
    ("lrd-jwst",               [r"\bLRD\b", r"little red dot", r"JWST", r"overmassive"]),
    ("simons-obs",             [r"Simons\s+Obs", r"\bSO\b.+CMB"]),

    # Methodology / infrastructure
    ("permanent-results-reg",  [r"permanent-?results", r"registry.+land", r"§VII.+registry", r"registry\s+entry"]),
    ("w9a-methodology",        [r"\bW9a?\b", r"PRDR", r"PRU", r"plan-?layer", r"v3.?ladder", r"recovery.+controller"]),
    ("sha-audit",              [r"\bSHA\b.+audit", r"dual-?SHA", r"audit_?sha"]),
    ("knowledge-mcp",          [r"knowledge.?MCP", r"knowledge.?index", r"canonical_?constants"]),

    # NCG structural
    ("van-den-dungen-bridge",  [r"van\s+den\s+Dungen", r"Kasparov", r"submersion", r"factorization"]),
    ("spectral-triple",        [r"spectral\s+triple", r"Dirac\s+operator", r"spectral\s+action"]),
    ("hawking-area",           [r"Hawking", r"area\s+theorem", r"black\s+hole.+entropy"]),

    # Fallback
    ("misc",                   []),
]


def assign_theme(u):
    """Return (bucket_name, matched_pattern) for the given entry."""
    haystack = (
        (u["title"] or "") + " "
        + (u["gate_id"] or "") + " "
        + (u["what"] or "")[:400] + " "
        + (u["inputs"] or "")[:200]
    )
    for bucket, patterns in THEME_BUCKETS:
        for p in patterns:
            if re.search(p, haystack, re.IGNORECASE):
                return bucket, p
    return "misc", ""


def main():
    all_entries = []
    missing = []
    source_meta = []

    for filename, start, end, origin in SOURCES:
        fp = S84 / filename
        if not fp.exists():
            missing.append(filename)
            continue
        section = read_section(filename, start, end)
        blocks = split_entries(section)
        body_lines = end - start - 1
        source_meta.append((filename, body_lines, origin, len(blocks)))
        for raw_id, block in blocks:
            title = extract_title(block, raw_id)
            fields = extract_fields(block)
            gate_id = extract_gate_id(block, raw_id, title)
            all_entries.append({
                "raw_id":  raw_id,
                "title":   title,
                "gate_id": gate_id,
                "what":    fields["what"],
                "inputs":  fields["inputs"],
                "gate":    fields["gate"],
                "effort":  fields["effort"],
                "origin":  origin,
                "source":  filename,
                "canon":   canonicalize(title),
            })

    # Stage A: aggressive normalization → upgraded dedup keys
    for e in all_entries:
        e["norm_gate_id"] = normalize_gate_id(e["gate_id"])
        e["norm_title"]   = normalize_title(e["title"])

    # Dedup: normalized gate_id takes precedence over normalized title
    groups = defaultdict(list)
    for e in all_entries:
        key = ("GID:" + e["norm_gate_id"]) if e["norm_gate_id"] else ("T:" + e["norm_title"])
        groups[key].append(e)

    uniq = []
    for key, entries in groups.items():
        best = max(entries, key=lambda x: len(x["title"]))
        origins = sorted({e["origin"] for e in entries})
        sources = sorted({e["source"] for e in entries})
        def longest(field):
            vals = [e[field] for e in entries if e[field]]
            return max(vals, key=len) if vals else ""
        uniq_entry = {
            "gate_id":        best["gate_id"],
            "norm_gate_id":   best["norm_gate_id"],
            "title":          best["title"],
            "norm_title":     best["norm_title"],
            "what":           longest("what"),
            "inputs":         longest("inputs"),
            "gate":           longest("gate"),
            "effort":         longest("effort"),
            "convergence":    len(sources),
            "origins":        origins,
            "sources":        sources,
            "n_raw":          len(entries),
        }
        bucket, matched_pat = assign_theme(uniq_entry)
        uniq_entry["theme"] = bucket
        uniq_entry["theme_match"] = matched_pat
        uniq.append(uniq_entry)

    uniq.sort(key=lambda x: (-x["convergence"], x["title"].lower()))

    # Write context file
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("# Session 85 — Context File\n\n")
        f.write("**Generated**: 2026-04-21\n")
        f.write("**Topic label**: CC (cosmetic — scope is full S84 carry-forward per /rclab-plan §0b)\n")
        f.write("**Planner default**: gen-physicist (cross-reviewer waves); reviewer-origin overrides apply per §2.7a step 3\n")
        f.write("**Source session**: S84 — 19 solo syntheses\n")
        f.write("**Extraction**: mechanical Python script `computations/session-85/s85_context_build.py` ")
        f.write("(replaces stalled Phase 2 gen-physicist agent which extracted 169 raw entries but stalled on table-build).\n\n")

        f.write("## Source Wrap-Ups\n\n")
        f.write("| File | CF body lines | Origin (agent) | Entries extracted |\n")
        f.write("|:-----|--------------:|:---------------|------------------:|\n")
        for fname, lines, origin, n in source_meta:
            f.write(f"| {fname} | {lines} | {origin} | {n} |\n")

        total_pre = sum(x[3] for x in source_meta)

        f.write(f"\n**Total extracted pre-dedup**: {total_pre}\n\n")

        f.write("## Missing Carry-Forward Section\n\n")
        if missing:
            for m in missing:
                f.write(f"- {m}\n")
        else:
            f.write("None — all 19 files parsed.\n")

        conv_dist = defaultdict(int)
        for u in uniq:
            conv_dist[u["convergence"]] += 1

        f.write("\n## Deduplicated Carry-Forward Computations\n\n")
        f.write(f"**Total pre-dedup**: {total_pre}\n")
        f.write(f"**Unique after dedup**: {len(uniq)}\n")
        f.write("**Convergence distribution**: ")
        f.write(", ".join(f"conv={k}: {v}" for k, v in sorted(conv_dist.items(), reverse=True)) + "\n\n")

        f.write("| # | Gate ID | Computation | What | Inputs | Gate criteria | Effort | Conv | Origin(s) |\n")
        f.write("|--:|:--------|:------------|:-----|:-------|:--------------|:-------|-----:|:----------|\n")
        for i, u in enumerate(uniq, 1):
            def esc(s):
                if not s:
                    return "—"
                s2 = s.replace("|", "\\|").replace("\n", " ")
                return s2 if len(s2) <= 300 else s2[:297] + "..."
            f.write(
                f"| {i} | {esc(u['gate_id'])} | {esc(u['title'])} "
                f"| {esc(u['what'])} | {esc(u['inputs'])} | {esc(u['gate'])} | {esc(u['effort'])} "
                f"| {u['convergence']} | {', '.join(u['origins'])} |\n"
            )

        f.write("\n## Summary\n\n")
        f.write(f"- Total source files scanned: {len(SOURCES)}\n")
        f.write(f"- Total CF entries extracted (pre-dedup): {total_pre}\n")
        f.write(f"- Unique entries after dedup: {len(uniq)}\n")
        f.write(f"- Files missing CF section: {len(missing)}\n")
        f.write(f"- Reduction ratio: {(1 - len(uniq)/total_pre):.1%} deduplicated\n")

    print(f"[OK] wrote {OUT}")
    print(f"     pre-dedup entries: {total_pre}")
    print(f"     unique: {len(uniq)}")
    print(f"     convergence distribution: {dict(conv_dist)}")
    print(f"     by origin (unique count):")
    origin_count = defaultdict(int)
    for u in uniq:
        for o in u["origins"]:
            origin_count[o] += 1
    for o, n in sorted(origin_count.items(), key=lambda x: -x[1]):
        print(f"       {o:20s} {n}")

    # Stage B: theme-bucket report + dump per-bucket JSON for Stage C agents
    write_themes_report(uniq)
    dump_buckets_json(uniq)

    # Stage D: apply per-bucket cluster JSONs (written by Stage C agents) → collapsed context
    collapsed_uniq, stats = apply_cluster_merges(uniq)
    write_collapsed_context(collapsed_uniq, stats)

    # Phase 2.7 partition — now operates on the COLLAPSED list
    write_partition(collapsed_uniq)


def write_themes_report(uniq):
    """Group unique entries by theme, write a review-friendly markdown report."""
    THEMES_OUT = ROOT / "sessions" / "session-plan" / "session-85-themes-report.md"
    buckets = defaultdict(list)
    for u in uniq:
        buckets[u["theme"]].append(u)

    # Sort buckets: by size descending, misc last
    ordered = sorted(
        buckets.items(),
        key=lambda kv: (kv[0] == "misc", -len(kv[1]), kv[0]),
    )

    with open(THEMES_OUT, "w", encoding="utf-8") as f:
        f.write("# Session 85 — Theme-Bucket Report (Stage B pre-dedup)\n\n")
        f.write("**Generated**: 2026-04-21\n")
        f.write(f"**Total unique entries (Stage A)**: {len(uniq)}\n")
        f.write(f"**Total buckets**: {len(buckets)}\n")
        f.write("**Purpose**: user review before Stage C per-bucket semantic dedup agents.\n\n")
        f.write("**Merge-candidate threshold**: buckets with >= 4 items dispatch a semantic-dedup "
                "agent (Stage C); buckets with <= 3 items skip the agent pass.\n\n")

        f.write("## Bucket summary\n\n")
        f.write("| Bucket | Items | Stage-C dispatch | Candidate-merge flag |\n")
        f.write("|:-------|------:|:-----------------|:---------------------|\n")
        for bucket, items in ordered:
            dispatch = "YES" if len(items) >= 4 else "skip"
            flag = "review candidate" if len(items) >= 4 else "—"
            f.write(f"| {bucket} | {len(items)} | {dispatch} | {flag} |\n")

        f.write("\n## Bucket contents (compact)\n\n")
        for bucket, items in ordered:
            f.write(f"### {bucket} ({len(items)} item{'s' if len(items) != 1 else ''})\n\n")
            for i, u in enumerate(items, 1):
                gid = u["gate_id"] if u["gate_id"] else "—"
                title_short = u["title"][:110] + ("..." if len(u["title"]) > 110 else "")
                origins = ", ".join(u["origins"])
                conv = u["convergence"]
                f.write(
                    f"  {i:>3}. **{gid}** — {title_short}\n"
                    f"       _conv={conv}; origins: {origins}_\n"
                )
            f.write("\n")

    print(f"[OK] wrote {THEMES_OUT}")
    bucket_sizes = [(b, len(items)) for b, items in ordered]
    print(f"     buckets ({len(buckets)}): " + ", ".join(f"{b}={n}" for b, n in bucket_sizes))
    dispatch_buckets = [b for b, n in bucket_sizes if n >= 4]
    print(f"     Stage-C dispatch buckets ({len(dispatch_buckets)}): {dispatch_buckets}")


def apply_cluster_merges(uniq):
    """Stage D: load all {bucket}_clusters.json, apply merges, return collapsed uniq list.

    Returns:
        new_uniq: list of merged+singleton entries (shorter than input)
        stats: dict with merge counts, bucket stats, theme_suggestions
    """
    import json
    BUCKETS_DIR = ROOT / "sessions" / "session-plan" / "session-85-buckets"
    cluster_files = sorted(BUCKETS_DIR.glob("*_clusters.json"))

    all_clusters = []
    theme_suggestions = []
    bucket_stats = {}
    for cf in cluster_files:
        with open(cf, encoding="utf-8") as f:
            data = json.load(f)
        bucket = data.get("bucket", cf.stem)
        summary = data.get("summary", {})
        bucket_stats[bucket] = {
            "input":    summary.get("input_count", 0),
            "clusters": summary.get("cluster_count", 0),
            "merged":   summary.get("merged_items", 0),
            "singleton":summary.get("singleton_items", 0),
        }
        for c in data.get("clusters", []):
            # Tolerant key lookup — agents used 3 schema variants
            indices = (
                c.get("raw_indices")
                or c.get("member_raw_indices")
                or [it.get("raw_index") for it in c.get("items", []) if isinstance(it, dict)]
                or []
            )
            title = (
                c.get("canonical_title")
                or c.get("representative_title")
                or c.get("label")
                or (c.get("member_titles", [""]) or [""])[0]
                or ""
            )
            gate_id = (
                c.get("canonical_gate_id")
                or c.get("representative_gate_id")
                or (c.get("member_gate_ids", [""]) or [""])[0]
                or ""
            )
            rationale = (
                c.get("rationale")
                or c.get("merge_rationale")
                or ""
            )
            if not indices:
                continue  # skip malformed clusters
            all_clusters.append({
                "indices":          indices,
                "canonical_title":  title,
                "canonical_gate_id":gate_id,
                "rationale":        rationale,
                "bucket":           bucket,
            })
        theme_suggestions.extend(data.get("theme_suggestions", []))

    indices_in_cluster = set()
    for c in all_clusters:
        indices_in_cluster.update(c["indices"])

    # Apply theme_suggestions (re-tag items without merging)
    ts_by_idx = {ts["raw_index"]: ts for ts in theme_suggestions}

    merged_entries = []
    for c in all_clusters:
        cluster_items = [uniq[i] for i in c["indices"]]
        origins = sorted({o for item in cluster_items for o in item["origins"]})
        sources = sorted({s for item in cluster_items for s in item["sources"]})
        def longest(field):
            vals = [item[field] for item in cluster_items if item[field]]
            return max(vals, key=len) if vals else ""
        merged = {
            "gate_id":           c["canonical_gate_id"] or cluster_items[0]["gate_id"],
            "norm_gate_id":      normalize_gate_id(c["canonical_gate_id"] or cluster_items[0]["gate_id"]),
            "title":             c["canonical_title"] or cluster_items[0]["title"],
            "norm_title":        normalize_title(c["canonical_title"] or cluster_items[0]["title"]),
            "what":              longest("what"),
            "inputs":            longest("inputs"),
            "gate":              longest("gate"),
            "effort":            longest("effort"),
            "convergence":       len(sources),
            "origins":           origins,
            "sources":           sources,
            "theme":             cluster_items[0]["theme"],
            "theme_match":       cluster_items[0].get("theme_match", ""),
            "merge_rationale":   c["rationale"],
            "merged_from_indices": c["indices"],
            "cluster_size":      len(c["indices"]),
        }
        merged_entries.append(merged)

    singleton_entries = []
    for i, u in enumerate(uniq):
        if i in indices_in_cluster:
            continue
        # Apply theme_suggestion if present
        new_u = dict(u)
        if i in ts_by_idx:
            sug = ts_by_idx[i]
            suggested = sug["suggested_theme"]
            if suggested.startswith("NEW:"):
                suggested = suggested.removeprefix("NEW:").strip()
            new_u["theme"] = suggested
            new_u["theme_resuggest_reason"] = sug.get("reason", "")
        new_u["cluster_size"] = 1
        new_u["merge_rationale"] = ""
        new_u["merged_from_indices"] = []
        singleton_entries.append(new_u)

    new_uniq = merged_entries + singleton_entries
    new_uniq.sort(key=lambda x: (-x["convergence"], x["title"].lower()))

    stats = {
        "pre_merge":          len(uniq),
        "post_merge":         len(new_uniq),
        "clusters_applied":   len(all_clusters),
        "items_merged":       sum(c["cluster_size"] if c["cluster_size"] else 0 for c in merged_entries),
        "singletons":         len(singleton_entries),
        "bucket_stats":       bucket_stats,
        "theme_suggestions":  len(theme_suggestions),
    }
    return new_uniq, stats


def write_collapsed_context(uniq, stats):
    """Write the final collapsed context file post-Stage-D."""
    COLLAPSED_OUT = ROOT / "sessions" / "session-plan" / "session-85-context.md"

    conv_dist = defaultdict(int)
    for u in uniq:
        conv_dist[u["convergence"]] += 1
    theme_dist = defaultdict(int)
    for u in uniq:
        theme_dist[u["theme"]] += 1

    with open(COLLAPSED_OUT, "w", encoding="utf-8") as f:
        f.write("# Session 85 — Context File (collapsed, post-Stage-D)\n\n")
        f.write("**Generated**: 2026-04-21\n")
        f.write("**Topic label**: CC (cosmetic; scope is full S84 carry-forward per /rclab-plan §0b)\n")
        f.write("**Source session**: S84 — 19 solo syntheses\n")
        f.write("**Extraction pipeline**: Stage A (normalization) + Stage B (theme buckets) + "
                "Stage C (15 per-bucket semantic dedup agents) + Stage D (merge).\n\n")

        f.write("## Pipeline stats\n\n")
        f.write(f"- Pre-Stage-D unique: {stats['pre_merge']}\n")
        f.write(f"- Post-Stage-D unique: **{stats['post_merge']}**\n")
        f.write(f"- Clusters applied: {stats['clusters_applied']}\n")
        f.write(f"- Items merged into clusters: {stats['items_merged']}\n")
        f.write(f"- Singletons preserved: {stats['singletons']}\n")
        f.write(f"- Theme re-suggestions applied: {stats['theme_suggestions']}\n")
        f.write(f"- Net reduction: {stats['pre_merge'] - stats['post_merge']} items "
                f"({(1 - stats['post_merge']/stats['pre_merge']):.1%} collapse)\n\n")

        f.write("## Stage-C per-bucket results\n\n")
        f.write("| Bucket | Input | Clusters | Merged | Singletons |\n")
        f.write("|:-------|------:|---------:|-------:|-----------:|\n")
        for b, s in sorted(stats["bucket_stats"].items(), key=lambda kv: -kv[1]["input"]):
            f.write(f"| {b} | {s['input']} | {s['clusters']} | {s['merged']} | {s['singleton']} |\n")

        f.write(f"\n**Convergence distribution**: ")
        f.write(", ".join(f"conv={k}: {v}" for k, v in sorted(conv_dist.items(), reverse=True)))
        f.write("\n\n")

        f.write("## Theme distribution (post-collapse)\n\n")
        f.write("| Theme | Items |\n|:------|------:|\n")
        for theme, n in sorted(theme_dist.items(), key=lambda kv: -kv[1]):
            f.write(f"| {theme} | {n} |\n")

        f.write("\n## Collapsed Carry-Forward Table\n\n")
        f.write("| # | Gate ID | Computation | Conv | Origins | Theme | Cluster-size |\n")
        f.write("|--:|:--------|:------------|-----:|:--------|:------|-------------:|\n")
        for i, u in enumerate(uniq, 1):
            def esc(s):
                if not s:
                    return "—"
                s2 = str(s).replace("|", "\\|").replace("\n", " ")
                return s2 if len(s2) <= 180 else s2[:177] + "..."
            gid = esc(u["gate_id"])
            title = esc(u["title"])
            conv = u["convergence"]
            origins = ", ".join(u["origins"])
            theme = esc(u.get("theme", ""))
            csize = u.get("cluster_size", 1)
            f.write(f"| {i} | {gid} | {title} | {conv} | {origins} | {theme} | {csize} |\n")

    print(f"[OK] wrote collapsed context {COLLAPSED_OUT}")
    print(f"     {stats['pre_merge']} → {stats['post_merge']} ({stats['pre_merge'] - stats['post_merge']} collapsed)")


def dump_buckets_json(uniq):
    """Write a compact JSON file per theme bucket with items for Stage C agents."""
    import json
    BUCKETS_DIR = ROOT / "sessions" / "session-plan" / "session-85-buckets"
    BUCKETS_DIR.mkdir(parents=True, exist_ok=True)

    by_bucket = defaultdict(list)
    for i, u in enumerate(uniq):
        by_bucket[u["theme"]].append({
            "raw_index":    i,
            "gate_id":      u["gate_id"],
            "norm_gate_id": u["norm_gate_id"],
            "title":        u["title"],
            "norm_title":   u["norm_title"],
            "what":         u["what"][:300],
            "inputs":       u["inputs"][:200],
            "convergence":  u["convergence"],
            "origins":      u["origins"],
            "sources":      u["sources"],
        })

    manifest = []
    for bucket, items in by_bucket.items():
        fp = BUCKETS_DIR / f"{bucket}.json"
        with open(fp, "w", encoding="utf-8") as f:
            json.dump({"bucket": bucket, "item_count": len(items), "items": items}, f, indent=2, ensure_ascii=False)
        manifest.append({"bucket": bucket, "file": fp.name, "item_count": len(items)})

    with open(BUCKETS_DIR / "_manifest.json", "w", encoding="utf-8") as f:
        json.dump({"buckets": manifest, "total_items": len(uniq)}, f, indent=2)

    print(f"[OK] wrote {len(manifest)} per-bucket JSON files to {BUCKETS_DIR}")


def write_partition(uniq):
    """Bucket entries into waves by reviewer origin; split oversized buckets."""
    # Step 1: classify each entry
    cross_reviewer = [u for u in uniq if u["convergence"] >= 2]
    sole_origin = [u for u in uniq if u["convergence"] == 1]

    # Step 2: bucket sole-origin items by their (single) origin
    origin_buckets = defaultdict(list)
    for u in sole_origin:
        origin = u["origins"][0]
        origin_buckets[origin].append(u)

    # Step 3: assign wave IDs
    # Wave 0 is always cross-reviewer (gen-physicist breadth owner)
    # Waves 1+ are reviewer-origin, split a/b/c... when > WAVE_SIZE_MAX
    waves = []
    waves.append({
        "id": "W0",
        "theme": "Cross-reviewer high-convergence (conv >= 2)",
        "owner_origin": "cross",
        "owner_agent": "gen-physicist",
        "items": cross_reviewer,
        "split_rationale": "All items convergent across >= 2 S84 reviewers; no single "
                          "reviewer owns them. gen-physicist is the breadth owner.",
    })

    # Deterministic ordering of origins: descending by bucket size, then alphabetically
    ordered_origins = sorted(
        origin_buckets.keys(),
        key=lambda o: (-len(origin_buckets[o]), o),
    )

    wave_num = 1  # (local)
    for origin in ordered_origins:
        bucket = origin_buckets[origin]
        owner_agent = OWNER_MAP.get(origin, "gen-physicist")
        n = len(bucket)
        if n <= WAVE_SIZE_MAX:
            waves.append({
                "id": f"W{wave_num}",
                "theme": f"{origin}-origin single-reviewer wave",
                "owner_origin": origin,
                "owner_agent": owner_agent,
                "items": bucket,
                "split_rationale": "Single-reviewer bucket fits within WAVE_SIZE_MAX; no split.",
            })
            wave_num += 1
        else:
            # Split into sub-waves a, b, c, ... each <= WAVE_SIZE_MAX
            import math
            n_splits = math.ceil(n / WAVE_SIZE_MAX)
            split_size = math.ceil(n / n_splits)
            for i in range(n_splits):
                letter = chr(ord('a') + i)
                slice_ = bucket[i * split_size : (i + 1) * split_size]
                waves.append({
                    "id": f"W{wave_num}{letter}",
                    "theme": f"{origin}-origin reviewer wave ({letter}, split {i+1}/{n_splits})",
                    "owner_origin": origin,
                    "owner_agent": owner_agent,
                    "items": slice_,
                    "split_rationale": f"Bucket size {n} > WAVE_SIZE_MAX={WAVE_SIZE_MAX}; "
                                       f"split into {n_splits} sub-waves of ~{split_size} items.",
                })
            wave_num += 1

    # Dispatch batching (max ~8 concurrent per feedback_dispatch-discipline.md)
    CONCURRENCY_CAP = 8  # (local)
    batches = []
    current_batch = []
    for w in waves:
        if len(current_batch) >= CONCURRENCY_CAP:
            batches.append(current_batch)
            current_batch = []
        current_batch.append(w["id"])
    if current_batch:
        batches.append(current_batch)

    # Write partition manifest
    with open(PARTITION_OUT, "w", encoding="utf-8") as f:
        f.write("# Session 85 — Wave Partition Manifest\n\n")
        f.write("**Generated**: 2026-04-21\n")
        f.write(f"**Total carry-forward items**: {len(uniq)}\n")
        f.write(f"**Wave count**: {len(waves)}\n")
        f.write(f"**Cross-reviewer items** (conv >= 2): {len(cross_reviewer)}\n")
        f.write(f"**Sole-origin items** (conv = 1): {len(sole_origin)}\n")
        f.write("**Partition rules** (mechanical):\n")
        f.write("  - conv >= 2 → Wave 0 (gen-physicist breadth owner)\n")
        f.write(f"  - conv = 1 → reviewer-origin wave (per OWNER_MAP); "
                f"buckets > {WAVE_SIZE_MAX} items pre-split alphabetically (a, b, c, ...)\n")
        f.write(f"**Dispatch batching**: CONCURRENCY_CAP = {CONCURRENCY_CAP} concurrent agents.\n")
        f.write("Batches:\n")
        for i, batch in enumerate(batches, 1):
            f.write(f"  - Batch {i}: {', '.join(batch)}\n")

        f.write("\n## Wave Summary Table\n\n")
        f.write("| Wave | Theme | Owner (agent) | Items | Output plan file |\n")
        f.write("|:-----|:------|:--------------|------:|:-----------------|\n")
        for w in waves:
            f.write(
                f"| {w['id']} | {w['theme']} | {w['owner_agent']} | "
                f"{len(w['items'])} | session-85-plan-{w['id'].lower()}.md |\n"
            )

        f.write("\n## Wave Assignments (detailed)\n\n")
        for w in waves:
            f.write(f"### Wave {w['id']} — {w['theme']}\n")
            f.write(f"**Owner**: {w['owner_agent']}\n")
            f.write(f"**Output**: `sessions/session-plan/session-85-plan-{w['id'].lower()}.md`\n")
            f.write(f"**Split rationale**: {w['split_rationale']}\n")
            f.write(f"**Items** ({len(w['items'])}):\n\n")
            for i, u in enumerate(w["items"], 1):
                gid = u["gate_id"] if u["gate_id"] else "—"
                title_short = u["title"][:100] + ("..." if len(u["title"]) > 100 else "")
                origins = ", ".join(u["origins"])
                conv = u["convergence"]
                f.write(f"  {i}. **{gid}**: {title_short} _(conv={conv}, origins: {origins})_\n")
            f.write("\n")

        f.write("\n## Natural split candidates (for stall remediation)\n\n")
        f.write("Per `/rclab-plan` §3c, if a wave stalls, split it into sub-waves rather "
                "than degrade the spec. Candidate splits for single-reviewer waves that "
                "are already near WAVE_SIZE_MAX:\n\n")
        for w in waves:
            if w["owner_origin"] == "cross":
                continue
            n = len(w["items"])
            if WAVE_SIZE_MIN <= n <= WAVE_SIZE_MAX and "split" not in w["id"]:
                # If this wave could be pre-emptively split
                if n >= 8:
                    half = n // 2
                    f.write(
                        f"- **{w['id']}** ({w['owner_agent']}, {n} items): if stalls, "
                        f"split {w['id']}a (items 1-{half}) + {w['id']}b (items {half+1}-{n}).\n"
                    )

    print(f"[OK] wrote {PARTITION_OUT}")
    print(f"     wave count: {len(waves)}")
    print(f"     cross-reviewer (W0): {len(cross_reviewer)} items")
    print(f"     dispatch batches: {len(batches)}")
    for i, batch in enumerate(batches, 1):
        print(f"       Batch {i}: {batch}")


if __name__ == "__main__":
    main()
