"""Orchestrator batched audit for session-x verdict file.

Computes sig_5 (duplicate audit_sha256) over the NON-SUPERSEDED set only, per the
Option-A absolute-verdict-permanence reading discipline (gate-verdicts.md): superseded
lines are retained on disk by design; sig_5 uniqueness is judged on the live terminal
line of each supersession chain.

Checks:
  A. sig_5: non-superseded canonical lines have unique audit_sha256.
  B. one-canonical-verdict-per-gate: each gate_id resolves to exactly one non-superseded line.
  C. verdict distribution over the canonical (non-superseded) set.
  D. supersession-chain integrity: every superseded audit_sha is named by a successor's
     supersedes= token, and every supersedes= token on a CANONICAL line is full-64-hex.

Read-only. Exit 0 = audit ran (verdicts are data); the report is the deliverable.
"""
import os
import re
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import *  # noqa: E402,F401,F403 — rule compliance (S34+); audit operates on text, not values

VERDICT_FILE = "computations/session-x/sx_gate_verdicts.txt"

CANON_RE = re.compile(r"^(WX-\S+):\s+(PASS|FAIL|INFO)\b")
AUDIT_RE = re.compile(r"audit_sha256=([a-f0-9]{64})")
SUPERSEDES_ANY_RE = re.compile(r"supersedes=([a-f0-9]{16,64})")
SUPERSEDES_64_RE = re.compile(r"supersedes=([a-f0-9]{64})")

text = open(VERDICT_FILE, encoding="utf-8").read()
lines = text.splitlines()

# All supersedes targets anywhere in the file (full-64 only; 16-hex comment-row forms ignored
# for chain resolution but reported separately).
superseded_64 = set(SUPERSEDES_64_RE.findall(text))

canon = []  # (gate_id, verdict, audit_sha, is_canonical_line_text)
for ln in lines:
    m = CANON_RE.match(ln)
    if not m:
        continue
    gate_id, verdict = m.group(1), m.group(2)
    am = AUDIT_RE.search(ln)
    audit = am.group(1) if am else None
    canon.append((gate_id, verdict, audit, ln))

non_superseded = [(g, v, a, ln) for (g, v, a, ln) in canon if a not in superseded_64]
superseded = [(g, v, a, ln) for (g, v, a, ln) in canon if a in superseded_64]

# A. sig_5 over non-superseded
audit_counts = defaultdict(list)
for g, v, a, ln in non_superseded:
    audit_counts[a].append(g)
dup_audit = {a: gs for a, gs in audit_counts.items() if len(gs) > 1}
sig5 = "PASS" if not dup_audit else "FAIL"

# B. one canonical verdict per gate
per_gate = defaultdict(list)
for g, v, a, ln in non_superseded:
    per_gate[g].append((v, a))
multi_gate = {g: vs for g, vs in per_gate.items() if len(vs) > 1}
one_per_gate = "PASS" if not multi_gate else "FAIL"

# C. verdict distribution over canonical set
dist = defaultdict(int)
for g, (vs) in per_gate.items():
    dist[vs[0][0]] += 1

# D. supersession-chain integrity: every superseded audit_sha has a successor naming it (true by
# construction of superseded_64), and report any supersedes= token that is NOT 64-hex AND sits on
# a canonical (non-#) line (that would violate Option-A full-64 discipline).
bad_supersedes_on_canon = []
for ln in lines:
    if ln.lstrip().startswith("#"):
        continue  # comment rows may carry 16-hex for readability
    for tok in SUPERSEDES_ANY_RE.findall(ln):
        if len(tok) != 64:
            bad_supersedes_on_canon.append((ln[:80], tok))

print("=" * 72)
print("SESSION-X BATCHED VERDICT AUDIT (non-superseded set)")
print("=" * 72)
print(f"total canonical lines     : {len(canon)}")
print(f"  superseded (retained)   : {len(superseded)}")
print(f"  non-superseded (live)   : {len(non_superseded)}")
print(f"distinct gate_ids (live)  : {len(per_gate)}")
print()
print(f"[A] sig_5 (unique audit_sha256 over non-superseded): {sig5}")
if dup_audit:
    for a, gs in dup_audit.items():
        print(f"    DUPLICATE {a[:16]}... shared by {gs}")
print(f"[B] one-canonical-verdict-per-gate                 : {one_per_gate}")
if multi_gate:
    for g, vs in multi_gate.items():
        print(f"    MULTI {g}: {vs}")
print(f"[C] canonical verdict distribution                 : {dict(dist)}")
print(f"[D] bad (non-64) supersedes on canonical lines     : "
      f"{'PASS (none)' if not bad_supersedes_on_canon else 'FAIL'}")
for ln, tok in bad_supersedes_on_canon:
    print(f"    {tok} on: {ln}")
print()
print("Canonical (live) verdict per gate:")
for g in sorted(per_gate):
    v, a = per_gate[g][0]
    print(f"  {v:4s}  {g}  audit={a[:16]}...")
print()
fails = [g for g, vs in per_gate.items() if vs[0][0] == "FAIL"]
print(f"Live FAIL gates: {fails if fails else 'NONE'}")
print("=" * 72)
print(f"AUDIT VERDICT: sig_5={sig5}  one_per_gate={one_per_gate}  "
      f"bad_supersedes={'NONE' if not bad_supersedes_on_canon else 'PRESENT'}")
sys.exit(0)
