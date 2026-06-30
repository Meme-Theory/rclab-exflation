"""sig_5 + companion-row audit on s85_gate_verdicts.txt for W6-W13 entries.

Run by lizzi 9A combined-landscape synthesis (S85 W6-W13). Output is a
deterministic forensic audit of dual-SHA uniqueness and 16-hex companion-row
prefix matching for the W6-W13 verdict slice.

No physics computation. Tagged (local) intermediates throughout.
"""
import re
from collections import Counter, defaultdict

VERDICT_PATH = r"C:\sandbox\Ainulindale Exflation\computations\s85_gate_verdicts.txt"  # (local)

with open(VERDICT_PATH, "r") as f:
    lines = f.readlines()  # (local)

# W6-W13 gate filter — explicit W-prefix
re_w_prefix = re.compile(r"S85-(W6|W7|W8|W9|W10|W11|W12|W13)")  # (local)
# also include gates that originated in W6-W13 but lack a "W#-" prefix
re_extra = re.compile(
    r"S85-(EPSH-JENSEN|S5-CONVERGENCE|NCG-META-EXCLUSION|FIBER-GROUP-PARITY|"
    r"BASE-PONTRYAGIN|FOLDED-TRIANGLE|F-AMP-3PI|BOREL-FLOOR|MELLIN-BALANCE|"
    r"YUKAWA-MW|ANTI-CORRESPONDENCE|R842-PHYSICAL|BRANCH-A-HTILDE|"
    r"CGWB-ALPHA-S|R1-RANK)"
)  # (local)

canon = []  # (local)
for ln in lines:
    if ln.startswith("#"):
        continue
    if re_w_prefix.search(ln) or re_extra.search(ln):
        canon.append(ln.rstrip("\n"))

print("TOTAL_W6_13_CANON_LINES =", len(canon))

audit_pat = re.compile(r"audit_sha256=([0-9a-f]{64})")  # (local)
content_pat = re.compile(r"content_sha256=([0-9a-f]{64})")  # (local)
gate_pat = re.compile(r"^(S85-[A-Z0-9_-]+):")  # (local)
verdict_pat = re.compile(r":\s*(PASS|FAIL|INFO|PARTIAL-PASS|PRE-REG|PRE-REG-INCOMPLETE)\s+--")  # (local)

audits = defaultdict(list)  # (local)
contents = defaultdict(list)  # (local)
verdict_tally = Counter()  # (local)
gates_seen = []  # (local)

for ln in canon:
    g = gate_pat.search(ln)
    a = audit_pat.search(ln)
    c = content_pat.search(ln)
    v = verdict_pat.search(ln)
    gid = g.group(1) if g else "UNKNOWN"
    gates_seen.append(gid)
    if a:
        audits[a.group(1)].append(gid)
    if c:
        contents[c.group(1)].append(gid)
    if v:
        verdict_tally[v.group(1)] += 1

print("UNIQUE_GATES =", len(set(gates_seen)))
print("UNIQUE_AUDIT_SHA =", len(audits))
print("UNIQUE_CONTENT_SHA =", len(contents))
print("VERDICT_TALLY =", dict(verdict_tally))

audit_dups = [(k, v) for k, v in audits.items() if len(v) > 1]  # (local)
content_dups = [(k, v) for k, v in contents.items() if len(v) > 1]  # (local)
print("AUDIT_SHA_DUPLICATES (sig_5 violations) =", len(audit_dups))
for k, v in audit_dups:
    print("  AUDIT_DUP", k[:16], "->", v)
print("CONTENT_SHA_SHARED (legitimate when one script writes multi-subgate) =", len(content_dups))
for k, v in content_dups:
    print("  CONTENT_DUP", k[:16], "->", v)

# Companion-row 16-hex prefix verification
companion_pat = re.compile(
    r"^# audit_sha256 companion row:\s*(S85-[A-Z0-9_-]+)\s+audit=([0-9a-f]{16})\s+content=([0-9a-f]{16})"
)  # (local)
companions = {}  # (local)
for ln in lines:
    m = companion_pat.search(ln)
    if m:
        companions[m.group(1)] = (m.group(2), m.group(3))

print("TOTAL_COMPANION_ROWS_W6_13 =",
      sum(1 for k in companions if re_w_prefix.search(k) or re_extra.search(k)))

matched = mismatch = missing = 0  # (local)
mismatches = []  # (local)
missing_list = []  # (local)
for ln in canon:
    g = gate_pat.search(ln)
    a = audit_pat.search(ln)
    c = content_pat.search(ln)
    if not g:
        continue
    gid = g.group(1)
    full_a = a.group(1) if a else None
    full_c = c.group(1) if c else None
    if gid not in companions:
        missing += 1
        missing_list.append(gid)
        continue
    short_a, short_c = companions[gid]
    if full_a and full_c and full_a.startswith(short_a) and full_c.startswith(short_c):
        matched += 1
    else:
        mismatch += 1
        mismatches.append((gid, short_a, short_c, full_a[:16] if full_a else None, full_c[:16] if full_c else None))

print("COMPANION_MATCHED =", matched)
print("COMPANION_MISMATCH =", mismatch)
print("COMPANION_MISSING_GATE_RECORDS =", missing)
if mismatches:
    print("MISMATCH_DETAIL:")
    for row in mismatches:
        print(" ", row)
if missing_list:
    print("MISSING_DETAIL (first 10):", missing_list[:10])

# sig_2 adjacency: any canonical line with audit/content but no comment row downstream
print("\nsig_2 STALE-CONTENT-SHA SCAN (gates whose audit_sha appears AFTER content_sha invariance promise):")
# For S85+ schema, content_sha256 should be invariant under canonical_constants/pinmap edits;
# audit_sha256 changes with any input pin. Flag any cases where two different audit_sha256
# appear with the same content_sha256 across W6-W13 entries — that's the legitimate signature
# (not a sig_2 violation), but distinguishes single-subgate from multi-subgate scripts.
content_to_gates = defaultdict(set)  # (local)
for k, v in contents.items():
    for gid in v:
        content_to_gates[k].add(gid)
multi_audit_per_content = 0  # (local)
for content_sha, gid_set in content_to_gates.items():
    if len(gid_set) > 1:
        multi_audit_per_content += 1
        # legit if it's the W9-5 family or similar multi-subgate orchestrator
        print(f"  content_sha {content_sha[:16]} -> {len(gid_set)} sibling gates: {sorted(gid_set)}")
print("MULTI_GATE_PER_CONTENT_SHA_COUNT =", multi_audit_per_content)
print("SCRIPT_OK")
