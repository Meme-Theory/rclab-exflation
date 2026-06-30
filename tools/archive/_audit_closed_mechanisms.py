"""Audit the closed_mechanisms table — look at actual rows, group by patterns,
let the shape decide what the extractor predicate should be.

Throwaway script; safe to delete after the extractor fix lands.
"""
import sqlite3
import re
import random
from collections import defaultdict, Counter
from pathlib import Path

DB = Path(__file__).resolve().parent / "knowledge.db"
con = sqlite3.connect(str(DB))
cur = con.cursor()


def banner(t: str) -> None:
    print()
    print("=" * 78)
    print(t)
    print("=" * 78)


# ---------------------------------------------------------------------------
# 1. Per source-file category — which docs emit real closures vs noise
# ---------------------------------------------------------------------------
banner("CLOSED_MECHANISMS: BREAKDOWN BY source_file CATEGORY")


def categorize(sf: str | None) -> str:
    if not sf:
        return "z. NULL"
    sf = sf.replace("\\", "/")
    if "permanent-results-registry" in sf:
        return "a. permanent-results-registry"
    if any(s in sf for s in ("framework-cc-oom", "evoi-framework", "spectral-post-mortem", "closed-gw-channels")):
        return "b. framework/registry doc"
    if "/atlas-" in sf or "/Atlas/" in sf or "atlas-uplift" in sf:
        return "c. atlas doc"
    if "workingpaper" in sf:
        return "d. session WP (suspect)"
    if "wrapup" in sf or "synthesis" in sf or "session-end" in sf:
        return "e. session synthesis"
    if "sagan-redux" in sf or "sagan-verdict" in sf:
        return "f. sagan-verdict"
    if "Investigation-" in sf:
        return "g. investigation doc"
    if "plan" in sf:
        return "h. plan doc"
    if "results" in sf:
        return "i. results doc"
    return "z. other: " + sf[:50]


buckets = defaultdict(list)
for cm_id, name, session, gate_id, source_file in cur.execute(
    "SELECT id, name, session, gate_id, source_file FROM closed_mechanisms"
):
    buckets[categorize(source_file)].append((cm_id, name, session, gate_id, source_file))

random.seed(42)
for cat in sorted(buckets):
    rows = buckets[cat]
    print(f"\n  {cat}: {len(rows)} rows")
    for r in random.sample(rows, min(4, len(rows))):
        cm_id, name, session, gate_id, source_file = r
        print(f"    [{cm_id:<12s}] gate={ (gate_id or '')[:18]!r:<22s} session={(session or '')[:24]!r}")
        print(f"      name={(name or '')[:85]!r}")
        print(f"      src={source_file}")


# ---------------------------------------------------------------------------
# 2. MEMORY.md says framework has 25 real closures — can we find them?
# ---------------------------------------------------------------------------
banner("DO FRAMEWORK-REAL CLOSURES EXIST IN THE TABLE?")
hints = [
    "FRIEDMANN-BCS",
    "DILUTION-CC",
    "I-CC",
    "RPA",
    "Turing",
    "instanton",
    "perturbative",
    "Trap",
    "POMERANCHUK",
    "DNP",
    "PT-66",
    "EFFACEMENT",
    "WALL",
    "BCS-1D",
]
for h in hints:
    rows = cur.execute(
        "SELECT id, name, gate_id, session, source_file FROM closed_mechanisms WHERE name LIKE ? OR gate_id LIKE ? LIMIT 4",
        (f"%{h}%", f"%{h}%"),
    ).fetchall()
    if rows:
        print(f"\n  hint={h!r}: {len(rows)} match(es)")
        for r in rows:
            cm_id, name, gate, session, src = r
            print(f"    {cm_id:<12s} gate={(gate or '')[:18]!r:<22s} name={(name or '')[:60]!r}")
    else:
        print(f"  hint={h!r}: 0 matches")


# ---------------------------------------------------------------------------
# 3. Session-field pattern distribution — what does the extractor put there?
# ---------------------------------------------------------------------------
banner("SESSION FIELD: PATTERN DISTRIBUTION")
real_session_re = re.compile(r"^(S?\d+[a-z]?)$|^Session\s+\d+")
counter = Counter()
for (s,) in cur.execute("SELECT session FROM closed_mechanisms"):
    s = (s or "").strip()
    if not s:
        key = "<empty>"
    elif real_session_re.match(s):
        key = "<looks like real session id>"
    elif len(s) < 25 and s[0].isupper() and not any(c.isdigit() for c in s):
        key = f"<markdown-header word>: {s}"
    elif len(s) > 60:
        key = "<long prose >60 chars>"
    elif len(s) > 30:
        key = "<medium prose 30-60 chars>"
    else:
        key = f"<other short>: {s}"
    counter[key] += 1

for k, n in counter.most_common(30):
    print(f"  {n:>4}  {k[:80]}")


# ---------------------------------------------------------------------------
# 4. Name field — markdown-marker rate (bullet-pass victims)
# ---------------------------------------------------------------------------
banner("NAMES CONTAINING MARKDOWN MARKERS (probable bullet-pass victims)")
patterns = [
    ("starts-with-backtick", r"^`"),
    ("contains-double-asterisk", r"\*\*"),
    ("starts-with-What\\*\\*:", r"^What"),
    ("starts-with-Inputs\\*\\*:", r"^Inputs"),
    ("starts-with-Gate\\*\\*:", r"^Gate"),
    ("starts-with-Output\\*\\*:", r"^Output"),
    ("looks-like-equation", r"^[^A-Z]*[a-zA-Z_]+\s*="),
    ("name > 80 chars", None),  # by length
    ("starts-with-bullet-text", r"^-\s"),
    ("ends-with-period", r"\.$"),
]
for label, pat in patterns:
    cnt = 0
    cre = re.compile(pat) if pat else None
    for (n,) in cur.execute("SELECT name FROM closed_mechanisms"):
        if not n:
            continue
        if cre and cre.search(n):
            cnt += 1
        elif cre is None and len(n) > 80:
            cnt += 1
    print(f"  {label:<35s}: {cnt}")


# ---------------------------------------------------------------------------
# 5. gate_id field — shape classification
# ---------------------------------------------------------------------------
banner("GATE_ID FIELD: SHAPE CLASSIFICATION")
gid_short_re = re.compile(r"^[A-Z]{2,8}-\d+$")
gid_long_re = re.compile(r"^[A-Z][A-Z0-9]*(-[A-Z0-9]+){1,12}$")
buckets_g = {"empty": 0, "STAGE-1 / MOMENT-70 style": 0, "S88-LONG-NAME style": 0, "junk": 0}
junk_samples = []
for (g,) in cur.execute("SELECT gate_id FROM closed_mechanisms"):
    g = (g or "").strip()
    if not g:
        buckets_g["empty"] += 1
    elif gid_short_re.match(g):
        buckets_g["STAGE-1 / MOMENT-70 style"] += 1
    elif gid_long_re.match(g):
        buckets_g["S88-LONG-NAME style"] += 1
    else:
        buckets_g["junk"] += 1
        if len(junk_samples) < 10:
            junk_samples.append(g)
for k, n in buckets_g.items():
    print(f"  {k:<32s}: {n}")
if junk_samples:
    print("  junk samples (first 10):")
    for j in junk_samples:
        print(f"    {j!r}")


# ---------------------------------------------------------------------------
# 6. The 15 rows that emit `bounds` edges — what are they?
# ---------------------------------------------------------------------------
banner("THE 15 ROWS THAT EMIT bounds EDGES (downstream contamination source)")
rows = cur.execute("""
  SELECT cm.id, cm.name, cm.gate_id, cm.session, cm.source_file
  FROM closed_mechanisms cm
  WHERE cm.id IN (SELECT source_id FROM edges
                  WHERE source_type='closed_mechanisms' AND type='bounds')
""").fetchall()
print(f"  Total: {len(rows)}")
for cm_id, name, gate, session, src in rows:
    print(f"  {cm_id:<12s} gate={(gate or '')[:14]!r:<18s} session={(session or '')[:20]!r}")
    print(f"    name={(name or '')[:90]!r}")
    print(f"    src={src}")
