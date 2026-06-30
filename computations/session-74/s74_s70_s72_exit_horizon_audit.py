#!/usr/bin/env python3
"""
S70-S72-EXIT-HORIZON-AUDIT-74: Audit Exit-Horizon Vocabulary
=============================================================

S73A phonon-first-hawking workshop carry-forward #15.

"Exit horizon" is inflation/container-thinking vocabulary. In the substrate
picture, there is no horizon the fabric "exits through" -- there is a
post-fold region where the pair-production squeeze ceases to amplify and
the spectral weights relax. S73A EXIT-HORIZON-BOG-73a (W1-A) already
established that no sonic horizon exists at tau~0.16: the modulus flow is
deeply supersonic (Ma_BA = 20.7) everywhere across the BCS gap profile
range, varying by < 0.2%. There is no Ma = 1 crossing. The Bogoliubov
production is IMPULSIVE (parametric amplification during fast frequency
change), NOT from a sonic horizon crossing.

This audit identifies every occurrence of "exit horizon" (and variants)
in S70/S72/S73A computation scripts and proposes substrate-consistent replacements:
  - "post-fold spectral relaxation" (for the post-fold region where
    squeezing ceases and spectra relax)
  - "parametric amplification tail" (for the tail of pair production
    after the fold impulse)
  - keep "impulsive fold transit" (for the frequency-change event itself)

DO NOT EDIT the audited scripts. Audit only.

Gate: S70-S72-EXIT-HORIZON-AUDIT-74
  PASS: audit table produced AND >= 3 vocabulary updates proposed
  INFO: 1-2 updates proposed
  FAIL: 0 updates

Session: S74 | Wave: W4-AA | Classification: GEOMETRIC (vocabulary)
"""

import sys
import os
import re

sys.path.insert(0, os.path.dirname(__file__))

import numpy as np
from canonical_constants import *  # noqa: F401,F403

print("=" * 72)
print("S70-S72-EXIT-HORIZON-AUDIT-74: Exit-Horizon Vocabulary Audit")
print("=" * 72)
print()

# ==============================================================================
#  SECTION 1: Files to audit
# ==============================================================================
# Scripts flagged by grep as containing "exit horizon" variants.
# S70: none (checked s70_cavity_bcs_horizon.py uses "exits the" in context
#   unrelated to sonic-horizon vocabulary; keep it)
# S72: s72_dual_decoherence.py (heavy usage in dual-timescale decoherence)
# S73A: s73a_exit_horizon_bog.py (the file that REFUTES the exit horizon)
#       s73a_compound_ns.py (reads 's73a_exit_horizon_bog.npz')
#       s73a_fabry_perot_cavity.py (reads the npz; prints "NO EXIT HORIZON")
#       s73a_re_decoherence_multi.py (heavy usage; marks channel as DEAD)
#       s73b_transit_power_spectrum.py (reads the npz for validation)
#       s73b_transit_ps_lmax7.py (reads the npz for validation)

repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # (local)
script_dir = os.path.join(repo_root, "computations")  # (local)

audit_targets = [  # (local)
    "s72_dual_decoherence.py",
    "s73a_exit_horizon_bog.py",
    "s73a_compound_ns.py",
    "s73a_fabry_perot_cavity.py",
    "s73a_re_decoherence_multi.py",
    "s73b_transit_power_spectrum.py",
    "s73b_transit_ps_lmax7.py",
]

# ==============================================================================
#  SECTION 2: Pattern definitions
# ==============================================================================
# Case-insensitive phrase matches. The mapped replacement is chosen per context:
#   "exit horizon" / "exit sonic horizon"      -> post-fold spectral relaxation
#     (when referring to the region; there is no horizon -- the fabric does
#      not "exit" anywhere, it undergoes spectral relaxation post-fold)
#   "horizon crossing" / "horizon crossing width" -> parametric amplification tail
#     (when referring to the width over which phases scramble; the scrambling
#      is from parametric chirp, not causal disconnection)
#   "exits the" (only in s70_cavity_bcs_horizon.py describing the gap
#      turning off as the fiber leaves the paired region)
#      -> keep if context is NOT a sonic-horizon claim
#   "EXIT-HORIZON-BOG" gate name -> CANONICAL, do not rename (historical ID)
#   "no_exit_horizon" npz key -> keep (historical ID; meaning is documented)

patterns = {  # (local)
    # Phrase: (replacement, category)
    "exit sonic horizon": ("post-fold spectral relaxation region", "region"),
    "exit horizon": ("post-fold spectral relaxation", "region"),
    "horizon crossing": ("parametric amplification tail", "process"),
    "no exit horizon": ("no post-fold horizon (flow stays supersonic)", "negation"),
    "sonic horizon crossing": ("parametric amplification tail", "process"),
    "entry sonic horizon": ("fold-entry impulsive region", "region"),  # for parallel
}

# Historical identifiers that must NOT be changed (they are canonical IDs):
preserve_ids = {  # (local)
    "EXIT-HORIZON-BOG-73a",
    "EXIT-HORIZON-BOG",
    "CAVITY-BCS-HORIZON-70",
    "s73a_exit_horizon_bog.npz",
    "s73a_exit_horizon_bog.py",
    "s73a_exit_horizon_bog.png",
    "no_exit_horizon",  # npz key
}

# ==============================================================================
#  SECTION 3: Scan files
# ==============================================================================

audit_rows = []  # (local) list of dicts: file, line, old_text, proposed_new, category

total_scanned = 0  # (local)
total_hits = 0  # (local)

for fname in audit_targets:
    fpath = os.path.join(script_dir, fname)
    if not os.path.exists(fpath):
        print(f"  [SKIP] {fname} not found")
        continue

    with open(fpath, "r", encoding="utf-8") as fh:
        lines = fh.readlines()

    total_scanned += 1
    for lineno, raw_line in enumerate(lines, start=1):
        line_lc = raw_line.lower()

        # Skip lines that are purely historical identifier usage (file
        # paths, npz keys, canonical gate IDs)
        # We test whether the phrase appears in a non-preserved context.
        for phrase, (replacement, category) in patterns.items():
            if phrase not in line_lc:
                continue

            # Verify the occurrence is NOT inside a preserved identifier.
            # Build a stripped view that removes preserved IDs first.
            stripped = raw_line
            for pid in preserve_ids:
                stripped = stripped.replace(pid, "")
            stripped_lc = stripped.lower()

            if phrase not in stripped_lc:
                continue  # all occurrences were inside preserved IDs

            # Record one audit row per (file, line, phrase)
            match = re.search(phrase, raw_line, flags=re.IGNORECASE)
            matched_text = match.group(0) if match else phrase  # (local)

            audit_rows.append({
                "file": fname,
                "line": lineno,
                "old": matched_text,
                "new": replacement,
                "category": category,
                "context": raw_line.rstrip("\n").strip()[:140],
            })
            total_hits += 1

# ==============================================================================
#  SECTION 4: Report
# ==============================================================================

print(f"Scanned: {total_scanned} files")
print(f"Vocabulary hits (non-preserved): {total_hits}")
print(f"Preserved identifiers (unchanged): "
      f"{len(preserve_ids)} canonical IDs")
print()

# Group by file
from collections import defaultdict  # (local)
by_file = defaultdict(list)  # (local)
for row in audit_rows:
    by_file[row["file"]].append(row)

print("AUDIT TABLE")
print("=" * 72)
for fname in sorted(by_file.keys()):
    rows = by_file[fname]
    print(f"\n{fname} -- {len(rows)} updates")
    print("-" * 72)
    for r in rows:
        print(f"  L{r['line']:4d} [{r['category']:8s}] "
              f"'{r['old']}' -> '{r['new']}'")
        print(f"         context: {r['context']}")

# ==============================================================================
#  SECTION 5: Category summary
# ==============================================================================

cat_counts = defaultdict(int)  # (local)
for r in audit_rows:
    cat_counts[r["category"]] += 1

print()
print("CATEGORY SUMMARY")
print("-" * 72)
for cat, n in sorted(cat_counts.items()):
    print(f"  {cat:12s}: {n} updates")

# ==============================================================================
#  SECTION 6: Physical justification
# ==============================================================================

print()
print("PHYSICAL JUSTIFICATION")
print("=" * 72)
print("""
  1. S73A EXIT-HORIZON-BOG-73a (W1-A) proved that Ma_BA = 20.7 at the
     fold and varies by <0.2% across |delta_tau| = 0.1. There is NO
     Ma = 1 crossing in the physical range of the BCS gap profile.
     Therefore "exit sonic horizon" is literally false -- there is no
     surface at which the flow transitions from super- to sub-sonic.

  2. The substrate picture: pair production is IMPULSIVE (parametric
     amplification during the rapid frequency change at the van Hove
     fold). The post-fold region is a SPECTRAL RELAXATION region --
     the eigenvalue spectrum reorganizes back toward its post-fold
     equilibrium. There is no horizon crossing in the causal sense;
     there is a parametric amplification tail.

  3. "Exit horizon" comes from inflation vocabulary (modes exit the
     horizon during inflation). In exflation:
       - Space does not expand; spectral complexity grows
       - There is no "horizon" modes cross; there is a fold they
         traverse impulsively
       - Post-fold, the spectral weights relax; they do not emerge
         from behind a causal boundary

  4. Historical gate IDs (EXIT-HORIZON-BOG-73a, CAVITY-BCS-HORIZON-70)
     and npz/png file names are CANONICAL and MUST be preserved. The
     vocabulary update applies to physical prose only, not to IDs.

  5. Replacement rules:
       "exit horizon"              -> "post-fold spectral relaxation"
       "exit sonic horizon"        -> "post-fold spectral relaxation region"
       "horizon crossing"          -> "parametric amplification tail"
       "sonic horizon crossing"    -> "parametric amplification tail"
       "no exit horizon"           -> "no post-fold horizon (flow stays supersonic)"
       "entry sonic horizon"       -> "fold-entry impulsive region"
""")

# ==============================================================================
#  SECTION 7: Gate verdict
# ==============================================================================

gate_name = "S70-S72-EXIT-HORIZON-AUDIT-74"  # (local)
n_updates = len(audit_rows)  # (local)

if n_updates >= 3:
    gate_verdict = "PASS"
    gate_detail = (
        f"{n_updates} vocabulary updates proposed "
        f"across {len(by_file)} files")
elif n_updates >= 1:
    gate_verdict = "INFO"
    gate_detail = (
        f"Only {n_updates} vocabulary updates proposed "
        f"(threshold for PASS is >= 3)")
else:
    gate_verdict = "FAIL"
    gate_detail = "No vocabulary updates proposed"

print()
print("=" * 72)
print(f"Gate: {gate_name}")
print(f"  Verdict: {gate_verdict}")
print(f"  Detail:  {gate_detail}")
print("=" * 72)

# ==============================================================================
#  SECTION 8: Save audit data
# ==============================================================================

data_dir = os.path.dirname(os.path.abspath(__file__))  # (local)
outpath = os.path.join(data_dir, "s74_s70_s72_exit_horizon_audit.npz")  # (local)

# Pack audit table as parallel arrays for npz
files_arr = np.array([r["file"] for r in audit_rows])  # (local)
lines_arr = np.array([r["line"] for r in audit_rows], dtype=np.int32)  # (local)
old_arr = np.array([r["old"] for r in audit_rows])  # (local)
new_arr = np.array([r["new"] for r in audit_rows])  # (local)
cat_arr = np.array([r["category"] for r in audit_rows])  # (local)
ctx_arr = np.array([r["context"] for r in audit_rows])  # (local)

np.savez(
    outpath,
    gate_name=gate_name,
    gate_verdict=gate_verdict,
    gate_detail=gate_detail,
    n_updates=n_updates,
    n_files_touched=len(by_file),
    files=files_arr,
    lines=lines_arr,
    old=old_arr,
    new=new_arr,
    category=cat_arr,
    context=ctx_arr,
    # Category summary
    categories=np.array(list(cat_counts.keys())),
    category_counts=np.array(list(cat_counts.values()), dtype=np.int32),
    # Preserved identifiers
    preserved_ids=np.array(sorted(preserve_ids)),
    audit_targets=np.array(audit_targets),
)
print(f"\nAudit data saved: {outpath}")
print(f"Audit complete. {n_updates} updates recorded.")
