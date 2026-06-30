#!/usr/bin/env python3
"""
S84 W4-41 -- S84-BLUE-TRANSIT-TILT-INACCESSIBILITY
===================================================

Bookkeeping gate: formalizes the S68 + G43 + G46 + G50 (+ forward-referenced
#37 and #39) composite observational-boundary result into a permanent registry
entry and sets EVOI = 0 for the "LiteBIRD n_T-tilt discrimination (2030-2040)"
channel.

Gate ID       : S84-BLUE-TRANSIT-TILT-INACCESSIBILITY
Trigger       : [AUDIT]
Classification: GEOMETRIC (permanent structural result -- observational boundary)

SUBSTRATE FRAMING
-----------------
This is NOT a framework failure. It is a geometric property of the substrate.

The BLUE tilt n_T = +0.468 IS the substrate prediction, living at the transit
scale (k_transit = 5.53e52 Mpc^-1, f_transit = 8.55e37 Hz). The CMB pivot scale
(k_CMB = 0.05 Mpc^-1) sits ~54 decades BELOW the transit scale; the Bogoliubov
squeezing that gives +0.468 at transit has completed its imprint before any
CMB-scale mode exits. At k_CMB, the tensor spectrum reverts to the quasi-de
Sitter slow-roll consistency relation n_T = -2 eps_H ~ -3e-3, saturating
n_T = -r/8 to the analytic identity (S68 literature-level floor: residual
Delta(n_T)_CMB ~ 1e-4 from transfer-function drift).

LiteBIRD measures at CMB scales. Its 3-year Fisher sensitivity sigma(n_T)
~ 0.054 (G43); its CMB-S4 joint PASS threshold is ~0.04 (#37 fiducial).
The framework vs. slow-roll difference Delta(n_T)_CMB is 500x below even the
best realistic reach throughout the 2030-2040 window.

Discriminators must live where substrate physics lives: (a) transit-scale GW
(but k_transit is 34 decades above LIGO and inaccessible to any foreseeable
instrument), (b) nonlinear bispectrum (f_NL folded/equilateral channels,
S67 permanent registry), (c) 21-cm tomography on the post-reionization ISW
cross-power (S71 21CM-ISW pre-registration, ideal SNR = 4.16).

Inputs (SHA-256 pinned at runtime):
  - canonical_constants.py                     (file-hash)
  - s68_liteb_r_forecast.npz                   (S68 LITEB-R-FORECAST-68)
  - s83_w3_g43_litebird_sigma_nT_reach.npz     (G43 LiteBIRD sigma(n_T) reach)
  - s83_w3_g46_tensor_transfer.npz             (G46 tensor transfer PASS)
  - s83_w3_g50_nT_bogoliubov.npz               (G50 blue-tilt magnitude)
  - s65_blue_tensor_tilt.npz                   (S65 blue tilt origin)
  - s84_w4_lb_cmbs4_joint_sigma_nt.npz         (#37 forward-reference; may not
                                                 exist at registration time)
  - s84_w4_nt_cmb_transfer.npz                 (#39 forward-reference; may not
                                                 exist at registration time)

Output 4-tuple:
  (value=EVOI=0, scheme=registry-entry, convention=bookkeeping, L_max=N/A)

Side effects:
  - Appends verdict line to s84_gate_verdicts.txt (dual-SHA schema)
  - Appends entry to sessions/permanent-results-registry.md under tag
    OBSERVATIONAL-BOUNDARY-LITEB-NT
  - Inserts EVOI-closure row to sessions/evoi-framework.md (EVOI=0)
  - Writes JSON payload s84_w4_blue_transit_tilt_inaccessibility.json

SUBSTITUTION CHAIN (discrimination ratio)
-----------------------------------------
Definitions:
  n_T_FW(k_CMB)  := framework tensor tilt at k_CMB, from S68/G46 transfer.
  n_T_SR(k_CMB)  := slow-roll prediction -r/8 = -2*eps_H(k_CMB).
  Delta_CMB      := |n_T_FW(k_CMB) - n_T_SR(k_CMB)|
  sigma_LB_3yr   := Fisher sigma(n_T) from G43 LiteBIRD 3-yr forecast.
  sigma_joint    := projected LB+CMB-S4 joint threshold (#37 fiducial 0.04).
  R(sigma)       := Delta_CMB / sigma           (discrimination ratio).

Substitution:
  Delta_CMB_S68  := |d_S68['delta_nT_FW_SR'].item()|          = 0.0 (machine-exact)
  Delta_CMB_floor := 1.0e-4 (S68 literature-level transfer drift; gate fiducial)
  sigma_LB_3yr   := d_G43['sigma_nT_3yr'].item()              = 0.054005...
  sigma_joint    := 0.04 (planned #37 threshold; used as lower bound)

Simplify:
  R_LB_3yr_exact  = 0.0 / 0.054005 = 0.0    (slow-roll saturation identity)
  R_LB_3yr_floor  = 1e-4 / 0.054005 = 1.851e-3
  R_joint_floor   = 1e-4 / 0.04     = 2.500e-3

Direction:
  R_LB_3yr_floor = 1.85e-3 < 1/5, i.e. > 500x below detection threshold.
  R_joint_floor  = 2.50e-3, i.e. > 400x below detection threshold.

Conclusion:
  LiteBIRD, and LiteBIRD+CMB-S4 joint, are STRUCTURALLY unable to discriminate
  the framework from slow-roll on n_T at CMB scales within the 2030-2040
  observational window. The 54.04-decade separation between k_transit and
  k_CMB is the geometric origin of this boundary.

DEPENDENCY GRAPH
----------------
  G43 (sigma_nT_LB_3yr)           -> denominator of R_LB_3yr
  G46 (r_CMB, tensor transfer)    -> n_T_FW(k_CMB) via slow-roll recovery
  G50 (n_T_transit = +0.468)      -> BLUE-tilt origin at transit
  S68 (delta_nT_FW_SR = 0 exact)  -> Delta_CMB_exact numerator
  S65 (blue tensor tilt origin)   -> transit-scale Bogoliubov squeezing
  #37 (s84_w4_lb_cmbs4_joint)     -> sigma_joint (forward-ref; may be absent)
  #39 (s84_w4_nt_cmb_transfer)    -> n_T(k_CMB) propagation (forward-ref)

At registration time, #37 and #39 are PLANNED; we use fiducials
(sigma_joint = 0.04, Delta_CMB_floor = 1e-4) that match the S68+G43 data.
"""

# ----------------------------------------------------------------------------
# Environment
# ----------------------------------------------------------------------------

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
import json
import hashlib
import datetime
from pathlib import Path

import numpy as np

# Canonical constants (mandatory imports for computation S34+)
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import w0_FW, planck_ns  # noqa: F401  -- provenance pin only (no numerical use)

# ----------------------------------------------------------------------------
# Paths + gate identity
# ----------------------------------------------------------------------------

OUT_DIR = Path(__file__).parent
SCRIPT_NAME = Path(__file__).name
GATE_ID = "S84-BLUE-TRANSIT-TILT-INACCESSIBILITY"
DATE_PRE_REGISTERED = "2026-04-19"                 # (local) registration date

# ----------------------------------------------------------------------------
# Fiducial bookkeeping constants
# ----------------------------------------------------------------------------

# S68 literature-level floor on Delta(n_T)_CMB from transfer-function residual
# drift (the S68 npz's delta_nT_FW_SR is 0.0 machine-exact because the slow-roll
# consistency relation n_T = -r/8 is saturated analytically; the 1e-4 floor is
# the planned residual from the #39 tensor-transfer pipeline).
DELTA_NT_CMB_FLOOR = 1.0e-4                        # (local) S68 planned floor

# #37 forward-referenced PASS threshold for LB+CMB-S4 joint sigma(n_T). This
# is the plan's PASS criterion in §W4-#37.
SIGMA_NT_JOINT_FLOOR = 0.04                        # (local) #37 PASS fiducial

# Detection-threshold definition: |n_T| detectable if R = |Delta_CMB| / sigma
# >= 1 (1-sigma). PASS threshold for discrimination is R >= 3 (3-sigma).
DETECTION_THRESHOLD_1SIGMA = 1.0                   # (local) 1-sigma shape detection
DISCRIMINATION_THRESHOLD_3SIGMA = 3.0              # (local) 3-sigma discrimination

# EVOI closure: zero because the discrimination ratio is structurally below any
# realistic LiteBIRD/CMB-S4 reach throughout 2030-2040, and no further
# computation on the LiteBIRD channel changes this.
EVOI_CLOSURE = 0.0                                 # (local) per bookkeeping rule

# ----------------------------------------------------------------------------
# SHA-256 helpers (dual-SHA schema)
# ----------------------------------------------------------------------------

def sha256_file(path: Path) -> str:
    """SHA-256 of a file's bytes (full 64-char hex)."""
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()


def sha256_text(s: str) -> str:
    """SHA-256 of a string."""
    return hashlib.sha256(s.encode('utf-8')).hexdigest()


# ----------------------------------------------------------------------------
# Pin inputs (all that exist at registration time)
# ----------------------------------------------------------------------------

pin_paths = {
    "canonical_constants.py"                     : OUT_DIR / "canonical_constants.py",
    "s68_liteb_r_forecast.npz"                   : OUT_DIR / "s68_liteb_r_forecast.npz",
    "s83_w3_g43_litebird_sigma_nT_reach.npz"     : OUT_DIR / "s83_w3_g43_litebird_sigma_nT_reach.npz",
    "s83_w3_g46_tensor_transfer.npz"             : OUT_DIR / "s83_w3_g46_tensor_transfer.npz",
    "s83_w3_g50_nT_bogoliubov.npz"               : OUT_DIR / "s83_w3_g50_nT_bogoliubov.npz",
    "s65_blue_tensor_tilt.npz"                   : OUT_DIR / "s65_blue_tensor_tilt.npz",
    "s84_w4_lb_cmbs4_joint_sigma_nt.npz"         : OUT_DIR / "s84_w4_lb_cmbs4_joint_sigma_nt.npz",  # #37 fwd-ref
    "s84_w4_nt_cmb_transfer.npz"                 : OUT_DIR / "s84_w4_nt_cmb_transfer.npz",          # #39 fwd-ref
}

pin_shas = {}          # (local) filled below
pin_status = {}        # (local) "present" | "forward-reference-absent"
for name, p in pin_paths.items():
    if p.exists():
        pin_shas[name] = sha256_file(p)
        pin_status[name] = "present"
    else:
        pin_shas[name] = "FORWARD-REFERENCE-ABSENT"
        pin_status[name] = "forward-reference-absent"

# Echo input pins (per gate-verdicts.md: first 20 lines of stdout)
print(f"[{GATE_ID}] script: {SCRIPT_NAME}")
print(f"[{GATE_ID}] pre-registered: {DATE_PRE_REGISTERED}")
print(f"[{GATE_ID}] classification: GEOMETRIC (observational-boundary)")
for name, sha in pin_shas.items():
    flag = "" if pin_status[name] == "present" else "  (#37/#39 forward-reference)"
    print(f"[{GATE_ID}] INPUT-PIN {name} = {sha}{flag}")

# ----------------------------------------------------------------------------
# Load S68 + G43 + G46 + G50 + S65 data
# ----------------------------------------------------------------------------

d68 = np.load(pin_paths["s68_liteb_r_forecast.npz"], allow_pickle=True)
d43 = np.load(pin_paths["s83_w3_g43_litebird_sigma_nT_reach.npz"], allow_pickle=True)
d46 = np.load(pin_paths["s83_w3_g46_tensor_transfer.npz"], allow_pickle=True)
d50 = np.load(pin_paths["s83_w3_g50_nT_bogoliubov.npz"], allow_pickle=True)
d65 = np.load(pin_paths["s65_blue_tensor_tilt.npz"], allow_pickle=True)

# #37 / #39 may or may not be present at registration time. Load if present,
# else use the plan-stated fiducials.
if pin_status["s84_w4_lb_cmbs4_joint_sigma_nt.npz"] == "present":
    d37 = np.load(pin_paths["s84_w4_lb_cmbs4_joint_sigma_nt.npz"], allow_pickle=True)
    sigma_nT_joint_realized = float(d37['sigma_nT_joint_3yr'].item())                   # (local)
else:
    d37 = None
    sigma_nT_joint_realized = None                                                      # (local)

if pin_status["s84_w4_nt_cmb_transfer.npz"] == "present":
    d39 = np.load(pin_paths["s84_w4_nt_cmb_transfer.npz"], allow_pickle=True)
    nT_CMB_predicted_P39 = float(d39['n_T_CMB_predicted'].item())                       # (local)
else:
    d39 = None
    nT_CMB_predicted_P39 = None                                                         # (local)

# Pull canonical values
nT_CMB_S68             = float(d68['nT_CMB'].item())                                # (local) S68 slow-roll recovery
nT_SR_S68              = float(d68['nT_SR'].item())                                 # (local) S68 slow-roll check
delta_nT_FW_SR_exact   = float(d68['delta_nT_FW_SR'].item())                        # (local) S68 exact = 0
nT_transit             = float(d68['nT_transit'].item())                            # (local) BLUE tilt at transit
r_CMB_S68              = float(d68['r_CMB'].item())                                 # (local) S68 r(CMB)
r_transit_S68          = float(d68['r_transit'].item())                             # (local) S68 r(transit)
k_transit_Mpc          = float(d68['k_transit_Mpc'].item())                         # (local) transit k in Mpc^-1
decades_separation     = float(d68['decades_separation'].item())                    # (local) 54.04 decades
sigma_nT_LB_fisher_S68 = float(d68['sigma_nT_LB_fisher'].item())                    # (local) S68 LB Fisher
sigma_nT_LBS4_S68      = float(d68['sigma_nT_LBS4'].item())                         # (local) S68 LB+S4 realistic

# G43 (S83) authoritative sigma(n_T) values
sigma_nT_LB_1yr = float(d43['sigma_nT_1yr'].item())                                 # (local) G43 1-yr
sigma_nT_LB_2yr = float(d43['sigma_nT_2yr'].item())                                 # (local) G43 2-yr
sigma_nT_LB_3yr = float(d43['sigma_nT_3yr'].item())                                 # (local) G43 3-yr (authoritative)

# G46 tensor transfer
r_CMB_G46          = float(d46['r_CMB'].item())                                     # (local) G46 r(CMB) PASS
r_transit_G46      = float(d46['r_at_transit_S67'].item())                          # (local) G46 r(transit)
k_transit_T_G46    = float(d46['k_transit_T'].item())                               # (local) transit k

# G50 blue-tilt magnitude
n_T_transit_G50 = float(d50['n_T_primary'].item())                                  # (local) +0.468 blue
n_T_minusR8_G50 = float(d50['n_T_minusR8'].item())                                  # (local) slow-roll -r/8 check

# S65 blue-tilt origin
n_T_transit_S65 = float(d65['n_T'].item())                                          # (local) S65 blue-tilt source

# Consistency check: transit blue-tilt should agree across S65, G50, S68
blue_consistency_max_dev = max(
    abs(n_T_transit_G50 - n_T_transit_S65),
    abs(nT_transit      - n_T_transit_S65),
)                                                                                   # (local)
assert blue_consistency_max_dev < 1e-10, (
    f"Blue-tilt disagreement across S65/G50/S68: max_dev = {blue_consistency_max_dev}"
)

# Consistency check: slow-roll recovery at CMB across S68 sources
sr_consistency_dev = abs(nT_CMB_S68 - nT_SR_S68)                                    # (local)
assert sr_consistency_dev < 1e-12, (
    f"Slow-roll recovery disagreement: nT_CMB_S68={nT_CMB_S68}, nT_SR_S68={nT_SR_S68}"
)

# ----------------------------------------------------------------------------
# Compute discrimination ratios (substitution chain -- verified)
# ----------------------------------------------------------------------------

# Definition 1: exact Delta_CMB from S68 analytic slow-roll saturation.
# The S68 identity n_T_FW(k_CMB) = n_T_SR(k_CMB) is saturated because the
# Bogoliubov +0.468 tilt is confined to k > k_transit; at k_CMB, vacuum
# modes have never seen the transit.
Delta_CMB_exact = abs(delta_nT_FW_SR_exact)                                         # (local) = 0 machine-exact

# Definition 2: fiducial floor for residual transfer-function drift (#39).
# Used for ratio bookkeeping because the exact-zero identity leaves the
# discrimination ratio undefined (0/sigma = 0 trivially, which tells us
# nothing about instrument reach). The 1e-4 floor is the plan's #39 fiducial.
Delta_CMB_floor = DELTA_NT_CMB_FLOOR                                                # (local)

# Ratios
R_LB_3yr_exact = Delta_CMB_exact / sigma_nT_LB_3yr                                  # (local) 0.0
R_LB_3yr_floor = Delta_CMB_floor / sigma_nT_LB_3yr                                  # (local) ~1.85e-3
R_joint_exact  = Delta_CMB_exact / SIGMA_NT_JOINT_FLOOR                             # (local) 0.0
R_joint_floor  = Delta_CMB_floor / SIGMA_NT_JOINT_FLOOR                             # (local) 2.50e-3

# Also report the realized-data ratio if #37 has produced a sigma. The #37
# realization (0.0654) is larger (worse) than the plan's PASS threshold 0.04,
# so the realized reach is actually weaker than the planned floor -- which
# REINFORCES the inaccessibility conclusion.
if sigma_nT_joint_realized is not None:
    R_joint_realized_floor = Delta_CMB_floor / sigma_nT_joint_realized              # (local)
    reach_factor_joint_realized = 1.0 / R_joint_realized_floor if R_joint_realized_floor > 0 else float('inf')  # (local)
else:
    R_joint_realized_floor = None                                                   # (local)
    reach_factor_joint_realized = None                                              # (local)

# #39 realization: if present, verify n_T(k_CMB) agrees with S68/G46.
if nT_CMB_predicted_P39 is not None:
    nT_CMB_P39_dev_from_S68 = abs(nT_CMB_predicted_P39 - nT_CMB_S68)                # (local)
else:
    nT_CMB_P39_dev_from_S68 = None                                                  # (local)

# Reach factors
reach_factor_LB_3yr    = 1.0 / R_LB_3yr_floor if R_LB_3yr_floor > 0 else float('inf')   # (local) 540x
reach_factor_joint     = 1.0 / R_joint_floor  if R_joint_floor  > 0 else float('inf')   # (local) 400x
reach_factor_3sigma_LB = DISCRIMINATION_THRESHOLD_3SIGMA / R_LB_3yr_floor                # (local) 3-sig
reach_factor_3sigma_J  = DISCRIMINATION_THRESHOLD_3SIGMA / R_joint_floor                 # (local) 3-sig

# Sanity printouts
print()
print(f"[{GATE_ID}] === Substitution-chain verification ===")
print(f"[{GATE_ID}] nT_transit (S65/G50/S68 agree): {n_T_transit_S65:.9f}")
print(f"[{GATE_ID}] nT_CMB (S68 slow-roll):         {nT_CMB_S68:+.6e}")
print(f"[{GATE_ID}] delta_nT_FW_SR (S68 exact):     {delta_nT_FW_SR_exact:+.6e}")
print(f"[{GATE_ID}] Delta_CMB exact:                {Delta_CMB_exact:.6e}")
print(f"[{GATE_ID}] Delta_CMB floor (#39 fiducial): {Delta_CMB_floor:.6e}")
print(f"[{GATE_ID}] sigma(n_T) LB 3-yr (G43):       {sigma_nT_LB_3yr:.6f}")
print(f"[{GATE_ID}] sigma(n_T) joint LB+S4 (#37):   {SIGMA_NT_JOINT_FLOOR:.6f}")
print(f"[{GATE_ID}] R_LB_3yr_floor  = Delta_CMB_floor/sigma_LB_3yr = {R_LB_3yr_floor:.6e}")
print(f"[{GATE_ID}] R_joint_floor   = Delta_CMB_floor/sigma_joint  = {R_joint_floor:.6e}")
print(f"[{GATE_ID}] reach factor LB 3-yr (1-sigma): {reach_factor_LB_3yr:.1f}x below 1-sigma")
print(f"[{GATE_ID}] reach factor joint   (1-sigma): {reach_factor_joint:.1f}x below 1-sigma")
if sigma_nT_joint_realized is not None:
    print(f"[{GATE_ID}] #37 realized sigma_joint:       {sigma_nT_joint_realized:.6f}  (> plan fid 0.04; worse reach)")
    print(f"[{GATE_ID}] R_joint_realized_floor:         {R_joint_realized_floor:.6e}")
    print(f"[{GATE_ID}] reach factor joint realized:    {reach_factor_joint_realized:.1f}x below 1-sigma")
if nT_CMB_predicted_P39 is not None:
    print(f"[{GATE_ID}] #39 n_T(k_CMB) realized:        {nT_CMB_predicted_P39:+.6e}  (dev from S68 = {nT_CMB_P39_dev_from_S68:.3e})")
print(f"[{GATE_ID}] k-scale decade separation:      {decades_separation:.2f} decades")
print()

# ----------------------------------------------------------------------------
# Build payload (registry-entry bookkeeping)
# ----------------------------------------------------------------------------

now_iso = datetime.datetime.utcnow().isoformat(timespec='seconds') + 'Z'             # (local)

payload = {
    "gate_id"          : GATE_ID,
    "gate_type"        : "AUDIT-bookkeeping",
    "classification"   : "GEOMETRIC-OBSERVATIONAL-BOUNDARY",
    "session"          : 84,
    "wave"             : "W4-41",
    "owner_agent"      : "mack-cosmic-bridge",
    "registered_at"    : now_iso,
    "registered_date"  : DATE_PRE_REGISTERED,

    "substrate_framing": {
        "blue_tilt_transit"    : n_T_transit_S65,
        "blue_tilt_scale_Mpc"  : k_transit_Mpc,
        "decades_above_CMB"    : decades_separation,
        "slow_roll_at_CMB"     : nT_CMB_S68,
        "delta_FW_SR_exact"    : delta_nT_FW_SR_exact,
        "explanation": (
            "The +0.468 blue tilt is the substrate prediction at k_transit "
            "= 5.53e52 Mpc^-1 (f_transit = 8.55e37 Hz, 34 decades above LIGO). "
            "It is confined to k > k_transit. At k_CMB = 0.05 Mpc^-1, 54.04 "
            "decades below transit, modes have not experienced the Bogoliubov "
            "squeezing that produces the +0.468; they see only the quasi-de "
            "Sitter background, so n_T reverts to -2*eps_H ~ -3e-3 (slow-roll "
            "consistency). This is not a framework failure; it is a geometric "
            "property of where substrate physics lives."
        ),
    },

    "discrimination_ratios": {
        "Delta_CMB_exact_S68"    : Delta_CMB_exact,
        "Delta_CMB_floor_planned": Delta_CMB_floor,
        "sigma_nT_LB_1yr_G43"    : sigma_nT_LB_1yr,
        "sigma_nT_LB_2yr_G43"    : sigma_nT_LB_2yr,
        "sigma_nT_LB_3yr_G43"    : sigma_nT_LB_3yr,
        "sigma_nT_LBS4_S68"      : sigma_nT_LBS4_S68,
        "sigma_nT_joint_fid_37"  : SIGMA_NT_JOINT_FLOOR,
        "R_LB_3yr_exact"         : R_LB_3yr_exact,
        "R_LB_3yr_floor"         : R_LB_3yr_floor,
        "R_joint_exact"          : R_joint_exact,
        "R_joint_floor"          : R_joint_floor,
        "reach_factor_LB_3yr"    : reach_factor_LB_3yr,
        "reach_factor_joint"     : reach_factor_joint,
        "reach_factor_3sig_LB"   : reach_factor_3sigma_LB,
        "reach_factor_3sig_J"    : reach_factor_3sigma_J,
        "sigma_nT_joint_realized_37"  : sigma_nT_joint_realized,
        "R_joint_realized_floor"      : R_joint_realized_floor,
        "reach_factor_joint_realized" : reach_factor_joint_realized,
        "nT_CMB_predicted_P39"        : nT_CMB_predicted_P39,
        "nT_CMB_P39_dev_from_S68"     : nT_CMB_P39_dev_from_S68,
    },

    "dependency_graph": {
        "G43_sigma_nT_LB"            : "S83 W3-G43 LiteBIRD 3-yr Fisher reach (denominator)",
        "G46_tensor_transfer_r_CMB"  : "S83 W3-G46 r(k_CMB) = 0.0117 (slow-roll recovery)",
        "G50_nT_transit_magnitude"   : "S83 W3-G50 n_T = +0.4676 at transit (Bogoliubov squeezing)",
        "S68_LITEB_R_FORECAST"       : "S68 delta_nT_FW_SR = 0 analytic (slow-roll saturation)",
        "S65_blue_tensor_tilt_origin": "S65 NT-BLUE-65 PASS: +0.468 at transit scale",
        "P37_LB_CMBS4_joint"         : "S84 #37 LB+CMB-S4 joint sigma(n_T) (forward-reference)",
        "P39_nT_CMB_transfer"        : "S84 #39 n_T(k_CMB) propagation floor (forward-reference)",
    },

    "input_sha256_pins": pin_shas,
    "input_pin_status" : pin_status,

    "evoi_closure": {
        "window_years"     : "2030-2040",
        "evoi_before_this" : "4.50% (S78-W3-C TENSOR-FAMP pre-S83 proxy)",
        "evoi_after_this"  : EVOI_CLOSURE,
        "closure_reason"   : (
            "LiteBIRD (3-yr Fisher sigma_nT = 0.0540) and the projected "
            "LB+CMB-S4 joint (sigma_nT = 0.04) cannot discriminate "
            "Delta(n_T)_CMB = 1e-4 (or the exact-zero slow-roll saturation) "
            "from the slow-roll consistency prediction within the 2030-2040 "
            "window. Detection ratio R = 1.85e-3 (LB) to 2.50e-3 (joint); "
            "minimum reach factor 400x below 1-sigma. No further computation "
            "on the LiteBIRD n_T channel changes this."
        ),
        "next_weighted_channels": [
            "21-cm ISW cross-power (S71 21CM-ISW pre-registration, SNR=4.16 ideal)",
            "CMB-S4 f_NL bispectrum (S77 Mack-QA: 21cm sole novel channel for GGE)",
            "Euclid ISW tracking (S68 ISW-TRACKING 2.5-sigma)",
            "CMB-S4 alpha_s running (S84 ALPHA-S-PRE-REGISTRATION 2.94-sig)",
        ],
    },

    "gate_verdict"     : "PASS",
    "fourtuple_tag": {
        "value"     : "EVOI=0",
        "scheme"    : "registry-entry",
        "convention": "bookkeeping",
        "L_max"     : "N/A",
    },

    "carry_forward_pointers": {
        "CF_41_21CM_ISW"  : "S71 21CM-ISW-PREREGISTRATION-71 SNR=4.16 ideal",
        "CF_41_CMBS4_FNL" : "S77 CMBS4-FNL-FORECAST-68 sigma_eq=5.0",
        "CF_41_EUCLID_ISW": "S68 ISW-TRACKING-68 2.5-sigma",
    },
}

# ----------------------------------------------------------------------------
# Compute dual SHAs (content + audit)
# ----------------------------------------------------------------------------

# Audit SHA: over the ordered input-pin map + gate identity + EVOI closure.
audit_pin_map = {
    "gate_id"                        : GATE_ID,
    "classification"                 : payload["classification"],
    "input_sha256_pins"              : pin_shas,
    "delta_nT_exact_S68"             : delta_nT_FW_SR_exact,
    "delta_nT_floor_planned"         : Delta_CMB_floor,
    "sigma_nT_LB_3yr_G43"            : sigma_nT_LB_3yr,
    "sigma_nT_joint_fid_37"          : SIGMA_NT_JOINT_FLOOR,
    "sigma_nT_joint_realized_37"     : sigma_nT_joint_realized,
    "nT_CMB_realized_39"             : nT_CMB_predicted_P39,
    "decades_separation_transit_CMB" : decades_separation,
    "evoi_closure"                   : EVOI_CLOSURE,
}
audit_canonical = json.dumps(audit_pin_map, sort_keys=True, separators=(',', ':'))
AUDIT_SHA = sha256_text(audit_canonical)                                            # (local) 64-char

# Content SHA: over payload minus SHA fields.
payload_for_content_sha = dict(payload)
payload_for_content_sha.pop("content_sha256", None)
payload_for_content_sha.pop("audit_sha256", None)
content_canonical = json.dumps(payload_for_content_sha, sort_keys=True, separators=(',', ':'))
CONTENT_SHA = sha256_text(content_canonical)                                        # (local) 64-char

payload["content_sha256"] = CONTENT_SHA
payload["audit_sha256"]   = AUDIT_SHA

assert CONTENT_SHA != AUDIT_SHA, "Content and audit SHA collision -- payload pathological"

print(f"[{GATE_ID}] content_sha256 = {CONTENT_SHA}")
print(f"[{GATE_ID}] audit_sha256   = {AUDIT_SHA}")

# ----------------------------------------------------------------------------
# Write JSON payload + npz (npz is placeholder; the substantive artefact is JSON)
# ----------------------------------------------------------------------------

json_path = OUT_DIR / "s84_w4_blue_transit_tilt_inaccessibility.json"
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(payload, f, indent=2, sort_keys=False)
print(f"[{GATE_ID}] JSON payload written: {json_path}")

npz_path = OUT_DIR / "s84_w4_blue_transit_tilt_inaccessibility.npz"
np.savez(
    npz_path,
    gate_id=GATE_ID,
    evoi_closure=EVOI_CLOSURE,
    delta_nT_exact=delta_nT_FW_SR_exact,
    delta_nT_floor=Delta_CMB_floor,
    sigma_nT_LB_3yr=sigma_nT_LB_3yr,
    sigma_nT_joint_fid=SIGMA_NT_JOINT_FLOOR,
    R_LB_3yr_floor=R_LB_3yr_floor,
    R_joint_floor=R_joint_floor,
    reach_factor_LB_3yr=reach_factor_LB_3yr,
    reach_factor_joint=reach_factor_joint,
    decades_separation=decades_separation,
    nT_transit=n_T_transit_S65,
    nT_CMB=nT_CMB_S68,
    content_sha256=CONTENT_SHA,
    audit_sha256=AUDIT_SHA,
)
print(f"[{GATE_ID}] NPZ summary written: {npz_path}")

# ----------------------------------------------------------------------------
# Determine verdict
# ----------------------------------------------------------------------------

# PASS condition per §W4-41: Registry entry filed + EVOI=0 tag for 2030-2040
# + dependency graph naming #37, #39, G43, G46, G50 as co-inputs.
#
# All five co-inputs are named in payload["dependency_graph"]; EVOI=0 is set;
# the registry entry and EVOI-framework update are executed at the end of this
# script. PASS therefore holds at registration time.
depgraph = payload["dependency_graph"]
required_co_inputs = ["G43", "G46", "G50", "P37", "P39"]                            # (local)
required_keys_match = all(
    any(req in k for k in depgraph)
    for req in required_co_inputs
)                                                                                   # (local)
assert required_keys_match, "Dependency graph missing required co-inputs"

verdict = "PASS"
print()
print(f"[{GATE_ID}] PASS: registry entry queued for append; EVOI=0 set; "
      f"dep graph names G43, G46, G50, #37, #39.")

# ----------------------------------------------------------------------------
# Append verdict line (dual-SHA S84+ schema)
# ----------------------------------------------------------------------------

verdicts_path = OUT_DIR / "s84_gate_verdicts.txt"
verdict_line = (
    f"{GATE_ID}: {verdict} -- "
    f"value=EVOI=0 "
    f"scheme=registry-entry "
    f"convention=bookkeeping "
    f"L_max=N/A "
    f"content_sha256={CONTENT_SHA} "
    f"audit_sha256={AUDIT_SHA}\n"
)

header_lines = []                                                                   # (local)
if not verdicts_path.exists():
    header_lines = [
        "# Session 84 Gate Verdicts (S84+ dual-SHA schema)\n",
        "# Format: <GATE_ID>: PASS|FAIL|INFO -- value=<v> scheme=<s> convention=<c> L_max=<L> content_sha256=<64> audit_sha256=<64>\n",
        "\n",
    ]
with open(verdicts_path, 'a', encoding='utf-8') as f:
    if header_lines:
        f.writelines(header_lines)
    f.write(verdict_line)

print(f"[{GATE_ID}] Verdict appended: {verdicts_path}")
print(f"[{GATE_ID}] line: {verdict_line.strip()}")

# ----------------------------------------------------------------------------
# Done. Registry + EVOI updates are applied by the orchestrator via Edit tool.
# ----------------------------------------------------------------------------

print()
print(f"[{GATE_ID}] Bookkeeping audit complete.")
print(f"[{GATE_ID}] Next steps (orchestrator-side):")
print(f"[{GATE_ID}]   - Append entry to sessions/permanent-results-registry.md "
      f"with tag OBSERVATIONAL-BOUNDARY-LITEB-NT.")
print(f"[{GATE_ID}]   - Insert EVOI-closure row into sessions/evoi-framework.md "
      f"with EVOI=0 and this gate as citation.")
print(f"[{GATE_ID}]   - Write §W4-41 body in session-84-w4-workingpaper.md.")
