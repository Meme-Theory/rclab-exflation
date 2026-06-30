"""
S83 W3-G61 — S83-N-PIVOT-CS-CANONICALIZATION
=============================================

Gate: S83-N-PIVOT-CS-CANONICALIZATION
Trigger: [AUDIT]
Classification: NON-PHONONIC (canonicalization/bookkeeping gate)

Question: Does the canonical-constants ledger contain N_pivot = 64.08
with provenance traceable to S82 W-1 Wrap-Up #10 (CMB pivot e-fold count)?

SUBSTITUTION CHAIN (pre-registered):

  Step 1 (definition). N_pivot is the number of e-folds from the end of
    (ex)inflation (substrate fold at tau=tau_fold, N=0) to the moment
    the CMB pivot mode k_pivot = 0.05 Mpc^-1 crosses the horizon.

    On the SUBSTRATE the horizon-crossing condition is set by the
    phononic sound speed c_s (not c):
      k_pivot = a(N_pivot) * c_s / tau_H(N_pivot)
    where tau_H = 1/H is the Hubble time and a = a_fold * exp(N_pivot).

    On the LCDM conversion (photon horizon), horizon crossing uses c:
      k_pivot = a(N_LCDM) * c / tau_H(N_LCDM).

    Dividing these two relations (same k_pivot, same tau_H branch):
      exp(N_pivot - N_LCDM) = c / c_s.

  Step 2 (substitution). With the canonical-constants values:
      N_LCDM = 55 (standard CMB pivot e-fold, matter-dominated convention)
      c_s    = 1.137e-4 (substrate phononic sound speed, S82 W-1 ledger)

    Then:
      N_pivot = N_LCDM + ln(c / c_s)
              = 55 + ln(1 / 1.137e-4)
              = 55 + ln(8795.07)
              = 55 + 9.0818
              = 64.082.

  Step 3 (simplification). Rounded to the published S82 W-1 #10 value:
      N_pivot = 64.08  (4 sig figs).

  Step 4 (direction). The c_s correction is a STRICT ADDITION:
      c/c_s = 1 / 1.137e-4 = 8795 > 1  => ln(c/c_s) = +9.08 > 0
      => N_pivot^substrate > N_pivot^LCDM (+9.08 e-folds).

    Physical: horizon crossing on the substrate is c_s-bounded, so the
    pivot mode is sub-horizon LONGER (by 9.08 e-folds) than on LCDM.
    This is the "substrate acoustic-horizon correction" noted in
    s82-w1-1-divergence-chase.md.

  Step 5 (verification). Gate PASSES iff:
      (a) from canonical_constants import N_pivot returns 64.08
      (b) get_constant("N_pivot") returns matching value with
          provenance string naming S82 W-1 #10 and session S83
      (c) numerical identity abs(N_pivot - 64.08) < 1e-6

PASS criteria:
  All three conditions (a, b, c) satisfied.

FAIL criteria:
  Any of (a, b, c) fails.

INFO:
  Not applicable (this is a bookkeeping gate — binary).

Source:
  - S82 W-1 Wrap-Up #10: sessions/archive/session-82/s82-w1-1-divergence-chase.md
  - s83_w2_g7_cc7_dynamical.py (N_PIVOT = 64.08 local pin)
  - s83_w2_g16_unified_as79_3pi_subst.py (F_amp_3PI_pivot at N_pivot=64.08)
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
import hashlib
import json
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).parent))

# Step 5a: verify import path
from canonical_constants import N_pivot

# Step 5b: cross-reference LCDM and c_s for substitution-chain verification
N_LCDM = 55.0                  # (local) standard CMB pivot e-fold, matter-dom
c_s_substrate = 1.137e-4       # (local) substrate phononic sound speed, S82 W-1
c_over_c_s = 1.0 / c_s_substrate  # (local) c=1 natural units; ratio c/c_s
ln_correction = np.log(c_over_c_s)  # (local) ln(c/c_s)
N_pivot_derived = N_LCDM + ln_correction  # (local) derived value, should match 64.08
N_pivot_expected = 64.08       # (local) pre-registered pin value

# -----------------------------------------------------------------------------
# SHA-256 input pin computation
# -----------------------------------------------------------------------------

def sha256_of(obj):
    """SHA-256 of a JSON-serializable object (sorted keys)."""
    s = json.dumps(obj, sort_keys=True, default=str).encode()
    return hashlib.sha256(s).hexdigest()

INPUT_PINS = {
    "N_pivot_canonical": float(N_pivot),
    "N_pivot_expected": N_pivot_expected,
    "N_LCDM": N_LCDM,
    "c_s_substrate": c_s_substrate,
    "gate": "S83-N-PIVOT-CS-CANONICALIZATION",
    "plan_section": "W3-G61",
    "source_note": "S82 W-1 Wrap-Up #10 (CMB pivot e-fold count)",
    "session": "S83",
}
input_sha = sha256_of(INPUT_PINS)

print("=" * 78)
print("S83 W3-G61 — S83-N-PIVOT-CS-CANONICALIZATION")
print("=" * 78)
print("Input pins (first 20-line SHA log):")
for k, v in INPUT_PINS.items():
    print(f"  {k} = {v}")
print(f"INPUT_SHA256 = {input_sha}")
print()

# -----------------------------------------------------------------------------
# STEP A — Verify import and value
# -----------------------------------------------------------------------------
print("STEP A — import-based check")
print(f"  from canonical_constants import N_pivot -> N_pivot = {N_pivot}")
print(f"  expected = {N_pivot_expected}")
check_import = abs(N_pivot - N_pivot_expected) < 1e-6  # (local)
print(f"  |N_pivot - 64.08| < 1e-6 ?  {check_import}")
print()

# -----------------------------------------------------------------------------
# STEP B — Verify substitution chain numerically
# -----------------------------------------------------------------------------
print("STEP B — substitution-chain verification")
print(f"  c / c_s = 1 / {c_s_substrate} = {c_over_c_s:.6e}")
print(f"  ln(c/c_s) = {ln_correction:.6f}")
print(f"  N_pivot_derived = N_LCDM + ln(c/c_s) = {N_LCDM} + {ln_correction:.6f} = {N_pivot_derived:.6f}")
print(f"  rounded to 2dp: {round(N_pivot_derived, 2)}")
check_derivation = abs(round(N_pivot_derived, 2) - N_pivot_expected) < 1e-6  # (local)
print(f"  round(derived, 2) == 64.08 ?  {check_derivation}")
print()

# -----------------------------------------------------------------------------
# STEP C — Verify knowledge MCP ledger provenance
# -----------------------------------------------------------------------------
# This script cannot call the MCP from inside Python, but the verification is
# that (a) the constant is retrievable via get_constant("N_pivot") [verified
# out-of-band by the orchestrator] and (b) the PROVENANCE dict in
# canonical_constants.py carries the S83 / S82 W-1 #10 lineage.

from canonical_constants import PROVENANCE  # (local) canonical PROVENANCE dict
prov_entry = PROVENANCE.get("N_pivot", None)
check_provenance = prov_entry is not None and prov_entry.get("session") == "S83"  # (local)
has_source = prov_entry is not None and "S82 W-1" in str(prov_entry.get("source", ""))  # (local)
has_gate = prov_entry is not None and prov_entry.get("gate") == "S83-N-PIVOT-CS-CANONICALIZATION"  # (local)

print("STEP C — PROVENANCE ledger verification")
if prov_entry is not None:
    print(f"  PROVENANCE['N_pivot'] = {prov_entry}")
else:
    print("  PROVENANCE['N_pivot'] = MISSING")
print(f"  session == 'S83'?                          {check_provenance}")
print(f"  source contains 'S82 W-1'?                 {has_source}")
print(f"  gate == 'S83-N-PIVOT-CS-CANONICALIZATION'? {has_gate}")
print()

# -----------------------------------------------------------------------------
# STEP D — Gate verdict
# -----------------------------------------------------------------------------

all_checks = check_import and check_derivation and check_provenance and has_source and has_gate
verdict = "PASS" if all_checks else "FAIL"

print("=" * 78)
print("VERDICT LOGIC")
print("=" * 78)
print(f"  check_import       = {check_import}")
print(f"  check_derivation   = {check_derivation}")
print(f"  check_provenance   = {check_provenance}")
print(f"  check_source_tag   = {has_source}")
print(f"  check_gate_tag     = {has_gate}")
print(f"  ALL PASS required: {all_checks}")
print(f"\n  VERDICT = {verdict}")
print()

# -----------------------------------------------------------------------------
# STEP E — Output 4-tuple and closure hash
# -----------------------------------------------------------------------------

OUTPUT_PINS = {
    **INPUT_PINS,
    "N_pivot_live": float(N_pivot),
    "N_pivot_derived": float(N_pivot_derived),
    "check_import": check_import,
    "check_derivation": check_derivation,
    "check_provenance": check_provenance,
    "check_source_tag": has_source,
    "check_gate_tag": has_gate,
    "verdict": verdict,
}
closure_sha = sha256_of(OUTPUT_PINS)

# 4-tuple: (N_pivot_pinned, scheme, convention, L_max)
value_tag = f"N_pivot={N_pivot}"  # (local) 4-tuple primary slot value
scheme_tag = "canonical-constants"
convention_tag = "S82-W-1-#10"
L_max_tag = "N/A"

verdict_line = (f"S83-N-PIVOT-CS-CANONICALIZATION: {verdict} -- value={value_tag} "
                f"scheme={scheme_tag} convention={convention_tag} "
                f"L_max={L_max_tag} sha256={closure_sha}")

print("=" * 78)
print(f"4-tuple output tag: (N_pivot_pinned={N_pivot}, scheme={scheme_tag}, "
      f"convention={convention_tag}, L_max={L_max_tag})")
print(f"CLOSURE_SHA256 = {closure_sha}")
print(f"\nVerdict line (S81+ format):")
print(verdict_line)
print("=" * 78)

# -----------------------------------------------------------------------------
# STEP F — Save data + plot
# -----------------------------------------------------------------------------

script_dir = Path(__file__).parent
out_npz = script_dir / "s83_w3_g61_n_pivot_canonicalization.npz"
out_png = script_dir / "s83_w3_g61_n_pivot_canonicalization.png"

np.savez_compressed(
    out_npz,
    N_pivot_live=float(N_pivot),
    N_pivot_expected=N_pivot_expected,
    N_pivot_derived=N_pivot_derived,
    N_LCDM=N_LCDM,
    c_s_substrate=c_s_substrate,
    ln_correction=ln_correction,
    check_import=check_import,
    check_derivation=check_derivation,
    check_provenance=check_provenance,
    check_source_tag=has_source,
    check_gate_tag=has_gate,
    verdict=verdict,
    closure_sha=closure_sha,
    input_sha=input_sha,
)

# Plot — diagnostic: derivation chain + verification checklist
fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))

# Left: bar chart of LCDM vs derived vs canonical
ax = axes[0]
labels = ['N_LCDM', 'ln(c/c_s)', 'derived\n(sum)', 'canonical\n(64.08)']
vals = [N_LCDM, ln_correction, N_pivot_derived, float(N_pivot)]
colors = ['C0', 'C1', 'C2', 'C3']
bars = ax.bar(labels, vals, color=colors)
ax.set_ylabel('e-folds')
ax.set_title('N_pivot substitution chain (LCDM + c_s correction)')
for bar, v in zip(bars, vals):
    ax.text(bar.get_x() + bar.get_width() / 2, v + 0.5, f"{v:.3f}",
            ha='center', fontsize=10)
ax.axhline(N_pivot_expected, color='k', linestyle=':', alpha=0.5,
           label=f'expected = {N_pivot_expected}')
ax.legend(loc='upper left')
ax.set_ylim(0, max(vals) * 1.15)

# Right: verdict summary
ax = axes[1]
ax.axis('off')
summary = (
    f"GATE: S83-N-PIVOT-CS-CANONICALIZATION\n\n"
    f"N_pivot (imported)       = {N_pivot}\n"
    f"N_pivot (derived chain)  = {N_pivot_derived:.4f}\n"
    f"N_pivot (expected pin)   = {N_pivot_expected}\n\n"
    f"Chain:\n"
    f"  N_LCDM       = {N_LCDM}\n"
    f"  c/c_s        = 1/{c_s_substrate} = {c_over_c_s:.3e}\n"
    f"  ln(c/c_s)    = {ln_correction:.4f}\n"
    f"  sum          = {N_pivot_derived:.4f}\n"
    f"  rounded(2dp) = {round(N_pivot_derived, 2)}\n\n"
    f"Checks:\n"
    f"  import            : {check_import}\n"
    f"  derivation        : {check_derivation}\n"
    f"  PROVENANCE session: {check_provenance}\n"
    f"  source tag S82W-1 : {has_source}\n"
    f"  gate tag          : {has_gate}\n\n"
    f"VERDICT: {verdict}\n\n"
    f"Provenance: S82 W-1 #10\n"
    f"SHA256: {closure_sha[:32]}...\n"
)
ax.text(0.02, 0.98, summary, transform=ax.transAxes, family='monospace',
        verticalalignment='top', fontsize=9)

plt.suptitle(f"S83 W3-G61: N_pivot canonicalization (64.08) — {verdict}", fontsize=13)
plt.tight_layout()
plt.savefig(out_png, dpi=120)
plt.close()

print(f"\nOutputs:")
print(f"  npz: {out_npz}")
print(f"  png: {out_png}")
print(f"\n[W3-G61 COMPLETE]")
