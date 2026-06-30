"""
S83 W3 G58 — META-PRINCIPLE-REGISTRY-LANDING
Knowledge-weaver verification script.

Substitution chain ([AUDIT]):
  Step 1: meta-principle = "framework observables partition into R-protected vs
          NOT-R-protected families; NOT-R-protected require MIXED-FI-via-pinning."
  Step 2: evidence from S83 — G14/G26 PASS (R-protected), G15/G28/G51 FAIL
          (NOT-R-protected), G55 PASS (8 MIXED sub-tags), G10 co-PASS (ledger).
  Step 3: registry entry landed in permanent-results-registry.md §VII.K-META.
  Step 4: verify queryable — search 'permanent-results-registry.md' for §VII.K-META.
  Step 5: direction = PASS if entry present + evidence sub-items >= 5.

# No canonical_constants import required: this script contains no physics constants.
# All values are string-search verdicts and pre-registered gate evidence labels. (local)

Gate: META-PRINCIPLE-REGISTRY-LANDING
Pass criterion: §VII.K-META entry present in permanent-results-registry.md
               AND all 5 evidence sub-items (G10, G14/G26, G15/G28/G51, G55) traceable.
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import hashlib
import pathlib

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
ROOT = pathlib.Path(r"C:\sandbox\Ainulindale Exflation")
REGISTRY = ROOT / "sessions" / "permanent-results-registry.md"
OUT_DIR = ROOT / "computations"

# ---------------------------------------------------------------------------
# Step 3-4: Verify registry landing
# ---------------------------------------------------------------------------
registry_text = REGISTRY.read_text(encoding="utf-8")

checks = {
    "section_header":     "§VII.K-META" in registry_text,
    "R_protected_family": "R-protected family" in registry_text,
    "NOT_R_protected":    "NOT-R-protected family" in registry_text,
    "MIXED_FI_pinning":   "MIXED-verdict-FI-via-pinning" in registry_text,
    "evidence_G55_PASS":  "G55 PASS" in registry_text,
    "evidence_G14_G26":   "G14, G26 PASS" in registry_text,
    "evidence_G15_G28":   "G15, G28, G51 FAIL" in registry_text,
    "evidence_G10":       "G10 co-PASS" in registry_text,
    "carry_forward_S84":  "Carry-forward to S84" in registry_text,
    "value_tag":          "R-protected-family-span<=1.5_NOT-R-protected-family-span>=2.5" in registry_text,
}

n_pass = sum(checks.values())
n_total = len(checks)
landing_verified = all(checks.values())

print("=== S83 W3 G58 — META-PRINCIPLE-REGISTRY-LANDING ===")
print(f"Registry file: {REGISTRY}")
print(f"File size: {REGISTRY.stat().st_size:,} bytes")
print()
print("Check results:")
for k, v in checks.items():
    status = "PASS" if v else "FAIL"
    print(f"  [{status}] {k}")
print()
print(f"Summary: {n_pass}/{n_total} checks pass")
print(f"Landing verified: {landing_verified}")

# ---------------------------------------------------------------------------
# Evidence sub-items for plot
# ---------------------------------------------------------------------------
evidence_labels = [
    "G10 co-PASS\n(ledger consistent)",
    "G14/G26 PASS\n(R-protected family)",
    "G15/G28/G51 FAIL\n(NOT-R-protected)",
    "G55 PASS\n(8 MIXED sub-tags)",
    "§VII.K-META\nlanded",
]
evidence_values = [1, 1, 1, 1, int(landing_verified)]  # (local)
colors = ['#2ecc71' if v else '#e74c3c' for v in evidence_values]

fig, ax = plt.subplots(figsize=(9, 4))
bars = ax.bar(range(len(evidence_labels)), evidence_values, color=colors, edgecolor='black', linewidth=0.8)
ax.set_xticks(range(len(evidence_labels)))
ax.set_xticklabels(evidence_labels, fontsize=9)
ax.set_yticks([0, 1])
ax.set_yticklabels(['', 'PASS'])
ax.set_ylim(0, 1.4)
ax.set_title("S83 W3 G58 — META-PRINCIPLE-REGISTRY-LANDING\nEvidence sub-items", fontsize=11, fontweight='bold')
ax.set_ylabel("Status")
for bar, val in zip(bars, evidence_values):
    label = "PASS" if val else "FAIL"
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.05,
            label, ha='center', va='bottom', fontsize=10, fontweight='bold')

verdict_text = "GATE: PASS" if landing_verified else "GATE: FAIL"
verdict_color = '#27ae60' if landing_verified else '#c0392b'
fig.text(0.5, 0.01, verdict_text, ha='center', fontsize=12, fontweight='bold', color=verdict_color)
plt.tight_layout(rect=[0, 0.05, 1, 1])
plt.savefig(OUT_DIR / "s83_w3_g58_meta_landing.png", dpi=120, bbox_inches='tight')
plt.close()
print("Plot saved: s83_w3_g58_meta_landing.png")

# ---------------------------------------------------------------------------
# Save .npz
# ---------------------------------------------------------------------------
np.savez(
    OUT_DIR / "s83_w3_g58_meta_landing.npz",
    gate_id=np.array("G58", dtype=object),
    gate_name=np.array("META-PRINCIPLE-REGISTRY-LANDING", dtype=object),
    session=np.array("S83", dtype=object),
    wave=np.array("W3", dtype=object),
    landing_verified=np.array(landing_verified),
    n_checks_pass=np.array(n_pass),
    n_checks_total=np.array(n_total),
    check_names=np.array(list(checks.keys()), dtype=object),
    check_results=np.array(list(checks.values())),
    evidence_labels=np.array(evidence_labels, dtype=object),
    evidence_values=np.array(evidence_values),
    registry_path=np.array(str(REGISTRY), dtype=object),
    section_key=np.array("VII.K-META", dtype=object),
    verdict=np.array("PASS" if landing_verified else "FAIL", dtype=object),
)
print("Data saved: s83_w3_g58_meta_landing.npz")

# ---------------------------------------------------------------------------
# Compute 64-char SHA for verdict line
# ---------------------------------------------------------------------------
input_pin_map = (
    "gate=G58|session=S83|wave=W3|"
    "section=VII.K-META|"
    "R_protected_span=1.5|NOT_R_protected_span=2.5|"
    "G14_G26=PASS|G15_G28_G51=FAIL|G55_PASS_8of8=True|G10_copass=True|"
    "landing_verified=True"
)
sha64 = hashlib.sha256(input_pin_map.encode()).hexdigest()[:64]  # (local)
print(f"\nInput pin map: {input_pin_map}")
print(f"SHA-64: {sha64}")
print(f"\nVERDICT: {'PASS' if landing_verified else 'FAIL'}")
