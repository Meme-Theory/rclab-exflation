"""Adversarial test: does the proposed Patch C regex actually do what the author claims?

Tests:
- Cited prose fragments from EQUATIONS_PROSE_POLLUTION_HANDOFF.md
- Multi-word LHS VALID structurals from the audit
- NOISE structurals from the audit
- Stratified sample from unaudited structural population
"""
import json
import re
import random
from pathlib import Path
from collections import Counter

ROOT = Path("C:/sandbox/Ainulindale Exflation")

# ---------------- proposed Patch C regex (from review prompt) ----------------
NEW_RE = re.compile(
    r'^[ ]{0,8}('
    r'(?:'
    r'  [A-Za-z_\\][\w]*'              # identifier or \latex command
    r'  (?:'
    r'    \([^()\n]{0,80}\)'           # (...) group, no nested
    r'    | \{[^{}\n]{0,80}\}'         # {...} group, no nested
    r'    | \^[\w{}()]+'               # ^... superscript
    r'    | _[\w{}()]+'                # _... subscript
    r"    | '+"                        # primes
    r'  )*'
    r')'
    r'\s*[=≡≈]\s*'
    r'[^\n|]{5,}'
    r')$',
    re.MULTILINE | re.VERBOSE,
)

# Existing regex (line 2540 of extract_entities.py)
OLD_RE = re.compile(
    r'^[ ]{0,8}('
    r'[A-Za-z_\(\[][\w_{}\(\)\[\]\\,\s\^\']*'
    r'\s*[=≡≈]\s*'
    r'[^\n|]{5,}'
    r')$',
    re.MULTILINE,
)


def matches_new(s: str) -> bool:
    """True iff Patch-C regex accepts this single-line string."""
    return bool(NEW_RE.match(s + "\n"))


def matches_old(s: str) -> bool:
    return bool(OLD_RE.match(s + "\n"))


# ---------------- Test 1: cited prose fragments from the handoff ---------
HANDOFF_PROSE = [
    "with envelope α_k = 2k - 1 (rank-cocycle order).",
    "pi_3(SU(3)) = Z (instantons/skyrmions). If the transition is mediated by instanton",
    "absolutely for k = 0, 2, 4. The polynomial cutoff f_B(u) = (1+u)^{−2} is",
    "In d = n+1 spacetime dimensions (n spatial), the acoustic metric",
    "with k_BCS the integrating-out scale for soft-gap fluctuations; T_K",
    "The N_eff statistic is defined as the number of independent  modes contributing to",
]

# ---------------- Test 2: legitimate multi-word/multi-token LHSs --------
LEGIT_MULTI = [
    "dim HP^1(A_K, H_K, D_K) = 3",
    "log g(L) = -alpha L + c",
    "T_{mu nu} = R_{mu nu} - 0.5 g_{mu nu} R",
    "\\nabla^2 \\phi = 4 \\pi G \\rho",
    "(d/dx) f(x) = f'(x)",
    "Tr(D_K^2) = sum lambda_i^2",
    "ratio λ_max(L=12)/λ_max(L=8) = 1.04",
    "Tr(P · A) = Sum_i P_ii A_ii",
    "Var_a(n_a^GGE) = (1/N) Sum_a m_a |v_a|^4",
    "Res_{s=0} s^2 * Tr(D_K^{-2s}) = a_4",
]

# ---------------- Test 3: known NOISE shapes from audit ------------------
NOISE_SHAPES_FROM_HANDOFF = [
    "audit_sha256=7271a682f5",
    "s_2 = -5.145024e-06",
    "OMP_NUM_THREADS=8",
    "tau=0.18: rho_s = 8.406207",
    "scheme=spectral_moment_analytic",
    "tau = 0.140 (7/15)",
    "value='promotion_status=FAIL_retain_30pct' \\",
    "convention=substrate-distance-1-pole-s3-OP-PROJ-FIRST-EXTRACTION \\",
    "K = \\text{SU}(3)",
    "lockout γ=1 at K_FIRAS reflects a fixed-point of the spectral action",
    "Fold = van Hove A_2 catastrophe (atlas B1, S35; PROVEN):",
    "coefficient κ = f_L (Leggett fraction, S82 permanent ≥ 0.6027).",
    "at τ_fold = 0.190; the affine reparameterization quotient IS the bridge map",
]

print("===== Test 1: handoff-cited prose fragments =====")
for p in HANDOFF_PROSE:
    old = matches_old(p)
    new = matches_new(p)
    print(f"  OLD={old}  NEW={new}  | {p[:80]}")

print()
print("===== Test 2: legitimate multi-word LHS structurals =====")
for p in LEGIT_MULTI:
    old = matches_old(p)
    new = matches_new(p)
    flag = "[BROKEN]" if (old and not new) else "[ok]"
    print(f"  {flag} OLD={old}  NEW={new}  | {p[:80]}")

print()
print("===== Test 3: handoff-cited NOISE shapes =====")
for p in NOISE_SHAPES_FROM_HANDOFF:
    old = matches_old(p)
    new = matches_new(p)
    flag = "[STILL_LEAKS]" if new else "[killed]"
    print(f"  {flag} OLD={old}  NEW={new}  | {p[:80]}")

# ---------------- Test 4: actual audit-NOISE structurals -----------------
print()
print("===== Test 4: actual 144 NOISE structurals from audit =====")

audit = json.loads((ROOT / "tools/_anchor_validation_results.json").read_text())
idx = json.loads((ROOT / "tools/knowledge-index.json").read_text(encoding="utf-8"))
eq_index = {e["id"]: e for e in idx["equations"]}

noise_structurals = []
valid_structurals = []
for aid, av in audit["equations"].items():
    e = eq_index.get(aid)
    if not e or e["type"] != "structural":
        continue
    if av["verdict"] == "NOISE":
        noise_structurals.append(e)
    elif av["verdict"] == "VALID":
        valid_structurals.append(e)

print(f"  NOISE structurals in audit: {len(noise_structurals)}")
print(f"  VALID structurals in audit: {len(valid_structurals)}")

# How many would the new regex still accept (i.e., still leak)?
# Take just the first non-empty line — the audit `raw` may include newlines.
def first_line(raw):
    return raw.split("\n", 1)[0].strip()

noise_still_match = 0
noise_killed = 0
for e in noise_structurals:
    line = first_line(e["raw"])
    if matches_new(line):
        noise_still_match += 1
    else:
        noise_killed += 1

print(f"  NOISE killed by new regex: {noise_killed} ({100.0*noise_killed/len(noise_structurals):.1f}%)")
print(f"  NOISE still matched (leaking): {noise_still_match} ({100.0*noise_still_match/len(noise_structurals):.1f}%)")

# False positives: VALID structurals rejected by the new regex
valid_dropped = []
valid_kept = 0
for e in valid_structurals:
    line = first_line(e["raw"])
    if matches_new(line):
        valid_kept += 1
    else:
        valid_dropped.append(e)

print(f"  VALID kept by new regex: {valid_kept} ({100.0*valid_kept/len(valid_structurals):.1f}%)")
print(f"  VALID DROPPED by new regex (false positives): {len(valid_dropped)} ({100.0*len(valid_dropped)/len(valid_structurals):.1f}%)")

print()
print("First 30 VALID structurals the new regex would drop:")
for e in valid_dropped[:30]:
    line = first_line(e["raw"])
    print(f"  [{e['id']}] {line[:110]}")

print()
print("First 20 NOISE structurals that LEAK through new regex (still match):")
n_shown = 0
for e in noise_structurals:
    line = first_line(e["raw"])
    if matches_new(line):
        print(f"  [{e['id']}] {line[:110]}")
        n_shown += 1
        if n_shown >= 20:
            break

# ---------------- Test 5: stratified sample of UNAUDITED structurals -----
print()
print("===== Test 5: stratified random sample of UNAUDITED structurals =====")

audited_ids = set(audit["equations"].keys())
unaudited_structurals = [e for e in idx["equations"] if e["type"] == "structural" and e["id"] not in audited_ids]
print(f"  Total UNAUDITED structurals: {len(unaudited_structurals)}")

# Stratified by source-file category
def category_of(path):
    p = path.lower().replace("\\", "/")
    if p.startswith("computations/") and (p.endswith(".txt") or p.endswith(".json")):
        return "computation_output"
    if p.startswith("computations/") and p.endswith(".py"):
        return "computation_script"
    if p.startswith("sessions/session-plan/"):
        return "plan_file"
    if "/workshops/" in p:
        return "workshop_md"
    if p.startswith("sessions/session-") and p.endswith(".md"):
        return "session_md"
    if p.startswith("sessions/framework/"):
        return "framework_md"
    return "other"

cat_buckets = {}
for e in unaudited_structurals:
    c = category_of(e["source_file"])
    cat_buckets.setdefault(c, []).append(e)

print("  Category distribution:")
for c, items in sorted(cat_buckets.items(), key=lambda x: -len(x[1])):
    print(f"    {c:25s} {len(items):>7d}")

# Stratified sample: 50 from each non-trivial bucket
random.seed(1337)
sample = []
for c, items in cat_buckets.items():
    n = min(50, len(items))
    sample.extend(random.sample(items, n))

print(f"  Stratified sample size: {len(sample)}")

new_matches = 0
new_drops = 0
new_drop_examples = []
new_match_examples = []
for e in sample:
    line = first_line(e["raw"])
    if matches_new(line):
        new_matches += 1
        if len(new_match_examples) < 50:
            new_match_examples.append(e)
    else:
        new_drops += 1
        if len(new_drop_examples) < 50:
            new_drop_examples.append(e)

print(f"  Of {len(sample)} sample: NEW regex matches {new_matches}, drops {new_drops}")
print(f"  Rough projected reduction on unaudited structurals: {100.0*new_drops/len(sample):.1f}%")

# ---------------- Test 6: Patch B denylist coverage on cited NOISE -------
print()
print("===== Test 6: Patch B denylist on actual NOISE structurals =====")

VERDICT_PIN_PREFIXES = (
    'audit_sha256', 'content_sha256', 'closure_sha256', 'sha256',
    'convention', 'scheme', 'value=', 'value =',
    'tier_pin', 'schema_version', 'supersedes',
    'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'PYTHONPATH'
)


def patch_b_kills(line: str) -> str:
    first_tok = line.split('=', 1)[0].strip()
    for p in VERDICT_PIN_PREFIXES:
        if first_tok.startswith(p):
            return f"denylist:{p}"
    if line.rstrip().endswith(':'):
        return "ends-with-colon"
    return ""


killed_by_b = 0
killed_categories = Counter()
for e in noise_structurals:
    line = first_line(e["raw"])
    reason = patch_b_kills(line)
    if reason:
        killed_by_b += 1
        killed_categories[reason] += 1

print(f"  NOISE killed by Patch B: {killed_by_b} / {len(noise_structurals)} ({100.0*killed_by_b/len(noise_structurals):.1f}%)")
print("  Breakdown:")
for r, n in killed_categories.most_common():
    print(f"    {r:30s} {n}")

# ---------------- Test 7: A+B+C union (actual cleanup) -------------------
print()
print("===== Test 7: ACTUAL union of A+B+C (not the author's sum) =====")

# Patch A drops anything in computations/*.txt or .json
def patch_a_kills(source_file: str) -> bool:
    p = source_file.lower().replace("\\", "/")
    if (p.endswith('.txt') or p.endswith('.json')) and '/computations/' in p:
        return True
    return False


a_kills = set()
b_kills = set()
c_kills = set()
for e in noise_structurals:
    line = first_line(e["raw"])
    if patch_a_kills(e["source_file"]):
        a_kills.add(e["id"])
    if patch_b_kills(line):
        b_kills.add(e["id"])
    if not matches_new(line):
        c_kills.add(e["id"])

union = a_kills | b_kills | c_kills
print(f"  Patch A kills: {len(a_kills)} of {len(noise_structurals)}")
print(f"  Patch B kills: {len(b_kills)} of {len(noise_structurals)}")
print(f"  Patch C kills: {len(c_kills)} of {len(noise_structurals)}")
print(f"  Union A+B+C:   {len(union)} of {len(noise_structurals)} ({100.0*len(union)/len(noise_structurals):.1f}%)")
print(f"  Author's stated sum: ~100 (~75%)")
print(f"  Overlap counts (intersection):")
print(f"    A∩B: {len(a_kills & b_kills)}")
print(f"    A∩C: {len(a_kills & c_kills)}")
print(f"    B∩C: {len(b_kills & c_kills)}")
print(f"    A∩B∩C: {len(a_kills & b_kills & c_kills)}")

residual = set(e["id"] for e in noise_structurals) - union
print(f"  RESIDUAL NOISE (none of A/B/C kills): {len(residual)} of {len(noise_structurals)}")
print()
print("  First 25 residual NOISE samples (what patches don't catch):")
for e in noise_structurals:
    if e["id"] in residual:
        line = first_line(e["raw"])
        print(f"    [{e['id']}] {line[:110]}")
        if e["id"] in residual:
            pass
            # decrement-safe; just show 25
        if list(residual).index(e["id"]) >= 24:
            break

# ---------------- Test 8: VALID structurals — what does each patch drop? -
print()
print("===== Test 8: VALID structural false-positive rates per patch =====")
v_a = sum(1 for e in valid_structurals if patch_a_kills(e["source_file"]))
v_b = sum(1 for e in valid_structurals if patch_b_kills(first_line(e["raw"])))
v_c = sum(1 for e in valid_structurals if not matches_new(first_line(e["raw"])))
print(f"  VALID killed by A: {v_a}/{len(valid_structurals)} ({100.0*v_a/len(valid_structurals):.1f}%) — author claimed 101")
print(f"  VALID killed by B: {v_b}/{len(valid_structurals)} ({100.0*v_b/len(valid_structurals):.1f}%)")
print(f"  VALID killed by C: {v_c}/{len(valid_structurals)} ({100.0*v_c/len(valid_structurals):.1f}%)")
