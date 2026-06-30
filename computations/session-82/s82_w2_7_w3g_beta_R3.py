#!/usr/bin/env python3
"""
s82_w2_7_w3g_beta_R3.py -- S82-W3G-BETA-R3: DR3 Dual-Axis Falsifier Registration
================================================================================
Classification: PHONONIC (substrate compaction timescape; DR3 test is the
sharp falsifier for the Volovik partition's DE sector prediction).

Gate: S82-W3G-BETA-R3
  Pre-registration task (NOT a measurement).
  PASS: registration artifact successfully recorded with explicit bands,
        SHA pinned, frozen against post-hoc adjustment.
  FAIL: INCOMPUTABLE -- registration cannot be serialized.

The falsifier itself activates at DR3-release; this script produces the
binding document.

DUAL-AXIS FALSIFIER (P2-C C1 / Q4 §552):
  Framework SURVIVES iff BOTH:
    w_0^{DR3} in [-0.94, -0.88]  (framework band: canonical w0_FW = -0.918 +/- 0.06/2 asymmetric)
    AND
    w_a^{DR3} in [-0.10, +0.10]   (framework band: canonical w_a = 0 exactly +/- 0.10 scheme band)
  Framework FAILS if EITHER band is violated.

No scenario-conditioning (absolute coordinates per P2-C E3', §509-513).

BAND PROVENANCE (P2-C C2 / MC2 §584-591):
  - w_0 band [-0.94, -0.88]: sigma_w0_scheme = 0.06 (Zubarev-vs-Keldysh
    two-sector ambiguity, S73B W2-D). Asymmetric around canonical w_0 = -0.918:
    lower +0.022, upper +0.038 (landau Noether-chain few-percent rationale).
  - w_a band [-0.10, +0.10]: S59 CC-relaxation scheme band (S66 four-fold
    lock gives w_a = 0 exactly; +/-0.10 is scheme uncertainty).

ASYMMETRY FLAG (MC2, §586-589):
  Lower edge 0.022 is TIGHTER than upper 0.038. This is framework-friendly
  toward DR3-toward-LCDM outcomes. Documented as honest-practice flag.

SUBSTITUTION CHAIN (binding logic -- binary precedence ME4 §511, MC1 §580):
  Step 1: Define event E_survive = (w_0^DR3 in [-0.94,-0.88]) AND (w_a^DR3 in [-0.10,+0.10])
  Step 2: Define event E_fail    = NOT E_survive
  Step 3: By DeMorgan: E_fail = (w_0^DR3 outside) OR (w_a^DR3 outside)
  Step 4: DR3 release returns a 2D point (w_0^DR3, w_a^DR3) with covariance.
  Step 5: Binary falsifier test: check membership of point in 2D rectangle.
  Step 6: If in: SURVIVE. If out: FAIL. No scenario conditioning. No continuous-tension override.

Author: mack-cosmic-bridge (S82 W2-7 R3)
"""

import sys, os, hashlib, json
from datetime import datetime, timezone
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))  # (local)
sys.path.insert(0, SCRIPT_DIR)

import numpy as np
from canonical_constants import w0_FW  # canonical value being falsified

# =============================================================================
# 0. Input SHA pins
# =============================================================================
def sha256_file(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for blk in iter(lambda: f.read(65536), b''):
            h.update(blk)
    return h.hexdigest()

R1_path = os.path.join(SCRIPT_DIR, 's82_w2_7_w3g_beta_R1.npz')    # (local)
R2_path = os.path.join(SCRIPT_DIR, 's82_w2_7_w3g_beta_R2.npz')    # (local)
cc_path = os.path.join(SCRIPT_DIR, 'canonical_constants.py')      # (local)

sha_R1 = sha256_file(R1_path)
sha_R2 = sha256_file(R2_path)
sha_cc = sha256_file(cc_path)

print("=" * 72)
print("S82-W3G-BETA-R3: DR3 Dual-Axis Falsifier Registration")
print("=" * 72)
print(f"INPUT PIN: s82_w2_7_w3g_beta_R1.npz  sha256={sha_R1[:16]}...")
print(f"INPUT PIN: s82_w2_7_w3g_beta_R2.npz  sha256={sha_R2[:16]}...")
print(f"INPUT PIN: canonical_constants.py    sha256={sha_cc[:16]}...")

# =============================================================================
# 1. Falsifier band definition (ABSOLUTE COORDINATES, no scenario-conditioning)
# =============================================================================
w0_band_lower  = -0.94  # (local) canonical w0_FW (-0.918) + (-0.022) tight side
w0_band_upper  = -0.88  # (local) canonical w0_FW (-0.918) + (+0.038) loose side
wa_band_lower  = -0.10  # (local) four-fold lock w_a = 0 - scheme band 0.10
wa_band_upper  = +0.10  # (local) four-fold lock w_a = 0 + scheme band 0.10

# Framework-predicted canonical values (NOT inputs to registration; reported only)
w0_canonical = w0_FW            # -0.918 (loaded from canonical_constants)
wa_canonical = 0.0              # (local) S66 four-fold lock: w_a = 0 exactly

# Asymmetry offsets (P2-C MC2 §589)
offset_lower_w0 = abs(w0_band_lower - w0_canonical)   # (local) 0.022
offset_upper_w0 = abs(w0_band_upper - w0_canonical)   # (local) 0.038

print(f"\n=== DUAL-AXIS DR3 FALSIFIER BANDS ===")
print(f"  Canonical w_0 (framework prediction) = {w0_canonical}")
print(f"  Canonical w_a (four-fold lock)       = {wa_canonical} (exact)")
print(f"")
print(f"  w_0 FALSIFIER BAND:  [{w0_band_lower}, {w0_band_upper}]")
print(f"    Width             = {w0_band_upper - w0_band_lower}")
print(f"    Lower offset      = {offset_lower_w0:.3f}  (tight side)")
print(f"    Upper offset      = {offset_upper_w0:.3f}  (loose side)")
print(f"    Asymmetry flag    = framework-friendly toward LCDM direction")
print(f"")
print(f"  w_a FALSIFIER BAND:  [{wa_band_lower}, {wa_band_upper}]")
print(f"    Width             = {wa_band_upper - wa_band_lower}")
print(f"    Symmetric around 0 = True")

# =============================================================================
# 2. DR3 scenario reference points (published forecasts -- reporting only)
# =============================================================================
# DR2 central (arXiv 2503.14738):
dr2_w0 = -0.752   # (local)
dr2_wa = -0.73    # (local)
# Forecast DR3 scenarios (S60 DR3-PREREGISTER-60):
scA_w0, scA_wa = -0.752, -0.73  # (local) preserves DR2
scB_w0, scB_wa = -0.918, 0.0    # (local) returns toward LCDM / framework canonical
scC_w0, scC_wa = -0.85, -0.30   # (local) intermediate
# DR3 central is UNKNOWN until release.

def in_dual_band(w0, wa):
    return ((w0_band_lower <= w0 <= w0_band_upper) and
            (wa_band_lower <= wa <= wa_band_upper))

print(f"\n=== PRE-REGISTERED BAND EVALUATION AT REFERENCE POINTS ===")
print(f"  (Reporting only -- DR3 FINAL central is not yet public)")
print(f"  {'Reference':<30s}  {'w_0':>8s}  {'w_a':>8s}  {'Survive?':>10s}")
print(f"  {'-'*66}")
for (lbl, w0, wa) in [
    ('DR2 central (arXiv 2503.14738)', dr2_w0, dr2_wa),
    ('Forecast DR3 Sc.A (DR2-like)', scA_w0, scA_wa),
    ('Forecast DR3 Sc.B (LCDM-like)', scB_w0, scB_wa),
    ('Forecast DR3 Sc.C (intermediate)', scC_w0, scC_wa),
    ('LCDM (w_0=-1, w_a=0)',             -1.0,  0.0),
    ('Framework canonical',              w0_canonical, wa_canonical),
]:
    surv = in_dual_band(w0, wa)
    print(f"  {lbl:<30s}  {w0:>+8.3f}  {wa:>+8.3f}  {str(surv):>10s}")

# =============================================================================
# 3. Registration artifact -- the binding document
# =============================================================================
registration = {
    "gate_id": "S82-W3G-BETA-R3",
    "registration_date_utc": datetime.now(timezone.utc).isoformat(),
    "registration_session": "S82",
    "binding_activation": "DR3 FINAL release (date TBD)",
    "type": "DUAL-AXIS ABSOLUTE-COORDINATE FALSIFIER",
    "falsifier_structure": "(w_0^DR3 in band) AND (w_a^DR3 in band) -- else FAIL",
    "scenario_conditioning": False,
    "continuous_tension_override": False,
    "binary_precedence_over_sigma_tension": True,
    "axes": {
        "w_0": {
            "band_lower": w0_band_lower,
            "band_upper": w0_band_upper,
            "framework_canonical": float(w0_canonical),
            "offset_lower": offset_lower_w0,
            "offset_upper": offset_upper_w0,
            "asymmetry_flag": "framework-friendly toward LCDM; honest-practice note",
            "band_source": "sigma_w0_scheme = 0.06 (Zubarev-vs-Keldysh, S73B W2-D)",
        },
        "w_a": {
            "band_lower": wa_band_lower,
            "band_upper": wa_band_upper,
            "framework_canonical": wa_canonical,
            "band_source": "S59 CC-relaxation scheme; S66 four-fold lock gives w_a = 0 exactly",
        },
    },
    "route": "Route A (Volovik partition, S58 canonical)",
    "route_B_status": "CLOSED (Weyl-scaling theorem, P2-C MC4 §606)",
    "parameterization_protocol": {
        "preferred": "CPL",
        "convert_to_CPL_if_DR3_reports_in": ["JBP", "Sc.B-scalable"],
        "refs": ["Linder 2003 §III", "DESI DR2 §VI.D Table 3"],
    },
    "freeze_policy": "No post-hoc band adjustment. Gate verdicts permanent on output; interpretation labels only via REFORMULATE.",
    "decision_rule_at_release": [
        "1. Extract CPL-equivalent (w_0^DR3, w_a^DR3) with covariance.",
        "2. If BOTH in bands -> SURVIVE.",
        "3. If EITHER outside band -> FAIL (binary precedence).",
        "4. Record continuous 2D sigma-tension as reportable but NOT override.",
    ],
}

# =============================================================================
# 4. Serialization check (R3 decisiveness condition)
# =============================================================================
# Gate PASS: registration is successfully serialized.
# Gate FAIL: INCOMPUTABLE (registration cannot be serialized).
try:
    registration_json = json.dumps(registration, indent=2, sort_keys=True)
    verdict_R3 = "PASS"
    detail = ("DR3 dual-axis falsifier REGISTERED and FROZEN at S82-W3G-BETA-R3. "
              f"w_0 band [{w0_band_lower}, {w0_band_upper}]; "
              f"w_a band [{wa_band_lower}, {wa_band_upper}]. "
              f"Binds at DR3 release. Asymmetry flag: {offset_lower_w0:.3f} tight / "
              f"{offset_upper_w0:.3f} loose (framework-friendly toward LCDM).")
    falsifier_status = "REGISTERED-AND-FROZEN"
except Exception as e:
    registration_json = None
    verdict_R3 = "FAIL"
    detail = f"INCOMPUTABLE: registration could not be serialized ({e})"
    falsifier_status = "INCOMPUTABLE"

print(f"\n=== R3 GATE VERDICT ===")
print(f"  Registration: {falsifier_status}")
print(f"  VERDICT: {verdict_R3} -- {detail}")

# =============================================================================
# 5. Save the registration JSON (binding artifact)
# =============================================================================
reg_path = os.path.join(SCRIPT_DIR, 's82_w2_7_w3g_beta_R3_registration.json')
with open(reg_path, 'w') as f:
    f.write(registration_json)

# =============================================================================
# 6. Closure SHA
# =============================================================================
input_pins = {
    's82_w2_7_w3g_beta_R1.npz': sha_R1,
    's82_w2_7_w3g_beta_R2.npz': sha_R2,
    'canonical_constants.py':    sha_cc,
    'w0_band_lower': str(w0_band_lower),
    'w0_band_upper': str(w0_band_upper),
    'wa_band_lower': str(wa_band_lower),
    'wa_band_upper': str(wa_band_upper),
    'w0_canonical':  str(float(w0_canonical)),
    'wa_canonical':  str(wa_canonical),
    'registration_type': 'DUAL-AXIS ABSOLUTE-COORDINATE',
    'scenario_conditioning': 'False',
    'binary_precedence':     'True',
    'route': 'Route A (Volovik partition)',
}
closure_sha = hashlib.sha256(
    json.dumps(input_pins, sort_keys=True).encode()
).hexdigest()

# =============================================================================
# 7. Save npz output
# =============================================================================
out_path = os.path.join(SCRIPT_DIR, 's82_w2_7_w3g_beta_R3.npz')
np.savez(
    out_path,
    # Bands
    w0_band=np.array([w0_band_lower, w0_band_upper]),
    wa_band=np.array([wa_band_lower, wa_band_upper]),
    w0_canonical=np.array(float(w0_canonical)),
    wa_canonical=np.array(wa_canonical),
    offset_lower_w0=np.array(offset_lower_w0),
    offset_upper_w0=np.array(offset_upper_w0),
    # Reference points
    dr2_w0=np.array(dr2_w0), dr2_wa=np.array(dr2_wa),
    scA_w0=np.array(scA_w0), scA_wa=np.array(scA_wa),
    scB_w0=np.array(scB_w0), scB_wa=np.array(scB_wa),
    scC_w0=np.array(scC_w0), scC_wa=np.array(scC_wa),
    # Registration
    falsifier_status=np.array([falsifier_status]),
    registration_type=np.array(['DUAL-AXIS ABSOLUTE-COORDINATE']),
    route=np.array(['Route A (Volovik partition)']),
    # Gate
    gate_name=np.array(['S82-W3G-BETA-R3']),
    gate_verdict=np.array([verdict_R3]),
    gate_detail=np.array([detail]),
    closure_sha=np.array([closure_sha]),
    registration_path=np.array([reg_path]),
)

# =============================================================================
# 8. Plot: DR3 falsifier band overlay with w(z) trajectory and reference points
# =============================================================================
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(16, 7))

# --- (a) 2D (w_0, w_a) dual-axis falsifier with reference points ---
ax = axes[0]
# Draw survival rectangle
rect = plt.Rectangle((w0_band_lower, wa_band_lower),
                     w0_band_upper - w0_band_lower,
                     wa_band_upper - wa_band_lower,
                     linewidth=2, edgecolor='green', facecolor='green', alpha=0.15,
                     label=f'SURVIVAL band\nw_0 in [{w0_band_lower},{w0_band_upper}]\nw_a in [{wa_band_lower},{wa_band_upper}]')
ax.add_patch(rect)
# Reference points
refs = [
    ('DR2 central', dr2_w0, dr2_wa, 'red', 's'),
    ('DR3 Sc.A forecast', scA_w0, scA_wa, 'orange', '^'),
    ('DR3 Sc.B forecast', scB_w0, scB_wa, 'limegreen', 'D'),
    ('DR3 Sc.C forecast', scC_w0, scC_wa, 'purple', 'v'),
    ('LCDM', -1.0, 0.0, 'black', 'o'),
    ('Framework canonical', float(w0_canonical), wa_canonical, 'darkblue', '*'),
]
for lbl, w0, wa, c, m in refs:
    ax.scatter([w0], [wa], c=c, marker=m, s=180, zorder=5, label=f'{lbl} ({w0:+.3f}, {wa:+.3f})',
               edgecolors='black', linewidths=0.8)

ax.set_xlabel('w_0')
ax.set_ylabel('w_a')
ax.set_title('S82-W3G-BETA-R3: DUAL-AXIS DR3 Falsifier\n(SURVIVE iff both axes in band)')
ax.axhline(0, color='gray', alpha=0.3, ls=':')
ax.axvline(-1, color='gray', alpha=0.3, ls=':')
ax.grid(True, alpha=0.3)
ax.legend(loc='lower left', fontsize=8)
ax.set_xlim(-1.05, -0.65)
ax.set_ylim(-0.85, +0.2)

# --- (b) w(z) trajectory under Volovik partition with DR3 band ---
# CPL: w(z) = w_0 + w_a * z/(1+z)
ax = axes[1]
z_grid = np.linspace(0, 2.0, 200)  # (local)
a_grid = 1.0/(1.0+z_grid)           # (local)

def cpl(w0, wa):
    return w0 + wa*(1.0-a_grid)

# Framework central
ax.plot(z_grid, cpl(float(w0_canonical), wa_canonical), 'darkblue', linewidth=3,
        label=f'Framework canonical (w_0={float(w0_canonical)}, w_a={wa_canonical})')
# DR3 band edges swept
for w0 in [w0_band_lower, w0_band_upper]:
    for wa in [wa_band_lower, wa_band_upper]:
        ax.plot(z_grid, cpl(w0, wa), color='green', alpha=0.35, linewidth=1)

# Survival band envelope
w_upper = np.maximum.reduce([cpl(w0_band_upper, wa_band_upper), cpl(w0_band_upper, wa_band_lower),
                              cpl(w0_band_lower, wa_band_upper), cpl(w0_band_lower, wa_band_lower)])
w_lower = np.minimum.reduce([cpl(w0_band_upper, wa_band_upper), cpl(w0_band_upper, wa_band_lower),
                              cpl(w0_band_lower, wa_band_upper), cpl(w0_band_lower, wa_band_lower)])
ax.fill_between(z_grid, w_lower, w_upper, color='green', alpha=0.12,
                label='DR3 SURVIVAL envelope')

# LCDM
ax.axhline(-1.0, color='black', ls='--', alpha=0.6, label='LCDM w=-1')
# DR2 central trajectory
ax.plot(z_grid, cpl(dr2_w0, dr2_wa), 'r--', alpha=0.8, linewidth=1.5,
        label=f'DR2 central (w_0={dr2_w0}, w_a={dr2_wa})')
# Sc.B forecast
ax.plot(z_grid, cpl(scB_w0, scB_wa), 'limegreen', ls=':', linewidth=2,
        label=f'DR3 Sc.B forecast (w_0={scB_w0}, w_a={scB_wa})')
# Sc.A forecast
ax.plot(z_grid, cpl(scA_w0, scA_wa), 'orange', ls=':', linewidth=2,
        label=f'DR3 Sc.A forecast (w_0={scA_w0}, w_a={scA_wa})')

ax.set_xlabel('z (redshift)')
ax.set_ylabel('w(z) under CPL')
ax.set_title('w(z) trajectory with DR3 SURVIVAL envelope\n(dual-axis falsifier range)')
ax.legend(loc='lower right', fontsize=8)
ax.grid(True, alpha=0.3)
ax.set_ylim(-1.2, -0.5)

plt.tight_layout()
plot_path = os.path.join(SCRIPT_DIR, 's82_w2_7_w3g_beta_R3.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# 9. Canonical verdict line
# =============================================================================
print(f"\n{'='*72}")
print(f"VERDICT LINE:")
print(f"S82-W3G-BETA-R3: {verdict_R3} -- value={falsifier_status} scheme=DR3-DUAL-AXIS convention=DESI-DR3-2026 L_max=N/A sha256={closure_sha}")
print(f"{'='*72}")
print(f"Saved: {out_path}")
print(f"Saved: {reg_path}")
print(f"Saved: {plot_path}")
print("DONE.")
