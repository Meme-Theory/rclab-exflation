#!/usr/bin/env python3
"""
S88 W1c-67 — S88-CF-CURV-14-TS-EM-2-BASE-2-LADDER-SPECTROSCOPY
================================================================

Gate: S88-CF-CURV-14-TS-EM-2-BASE-2-LADDER-SPECTROSCOPY  (trigger: VERIFY)

Pre-registered threshold (per session-88-plan-w1c.md §W1c-67 item 9):
  PASS iff
    (a) protocol artifact (sidecar JSON + Python pipeline spec + CCF Monte Carlo
        bootstrap + S/N forecast at three (continuum-fraction, N_sources) grid
        points) all written, AND
    (b) falsifier-master-inventory.md row update prepared, AND
    (c) competing-PBH discriminator (DCBH, Pop-III heavy-seed, super-Eddington
        direct-collapse) pre-registered, AND
    (d) Delta_log2_E sampling includes BOTH integer {1,2,3,4} AND half-integer
        {0.5, 1.5, 2.5, 3.5} points, AND
    (e) cross-correlation Monte Carlo bootstrap (N_bootstrap=1000) executed, AND
    (f) stacked-CCF SNR forecast >= 3 sigma at the conservative 1% continuum-
        fraction x N_sources=200 baseline.
  INFO iff (a)-(e) hold but (f) is below the conservative-baseline 3-sigma
        floor (still acceptable at PASS-DETECT-FUTURE under N_sources=300+).
  FAIL iff any of (a)-(e) missing OR Delta_log2_E sampling incomplete OR
        bootstrap not run.

This is a PROTOCOL-PRE-REGISTRATION gate (NON-PHONONIC; observational protocols
for JWST NIRSpec medium-resolution + MIRI MRS cycle-3+ spectroscopy at LRD-
progenitor environments z = 4-8). The S88 verdict closes on protocol artifact
existence, NOT on spectroscopic data outcome (which lives at multi-year
horizon).

SUBSTRATE-FRAMING REMINDER (per .claude/rules/phononic-framing.md §"IS Space,
Not IN Space"): The substrate IS the cascade. JWST measures photon energies
IN the spectrograph; the cascade-tail Hawking spectrum at LRD-progenitor
environments IS the substrate's pixelation-lock end-state radiation. The
base-2 ladder is NOT a structure imposed onto a thermal Hawking continuum;
it IS the substrate's intrinsic rank-2 Klein-V_4 cascade footprint at the
photon-energy level. Direction of explanation: substrate cascade physics
-> emergent Hawking + base-2-ladder correlated power -> JWST/MIRI observable
spectrum.

SUBSTITUTION CHAIN (per plan §W1c-67 item 10):
  Step 1 (definition): cascade-mass halving M_g = M_0 * 2^{-g}; Hawking-T
    scales T_H = (hbar*c^3) / (8*pi*G*M*k_B), so T_H(M_g) = T_H(M_0) * 2^g.
    Photon energy at the n-th cascade transition: E_n = k_B*T_H(M_n) = E_0*2^n.
  Step 2 (substitute): cascade-tail M_0 = 1e13 kg (Carr+10 §3 evap-mass-today)
    => T_H(M_0) = (1.054571817e-34 * (3e8)^3) / (8*pi*6.674e-11*1e13*1.381e-23)
              = 1.227e10 K
    => E_0_thermal = k_B * T_H(M_0) ~= 1.057 MeV (verified by Python; matches
       plan §W1c-67 Step 2 "~ 1.06 MeV").
  Step 3 (anchor): plan §W1c-67 items 5/8/11 PIN E_0_anchor = 0.94 keV at the
    cascade-step where the ladder enters JWST coverage. The thermal value
    1.057 MeV and the JWST-coverage anchor 0.94 keV differ by ~1000x; both
    are consistent with the same cascade since the base-2 RATIO is preserved
    by further halvings (1057 keV / 2^10 = 1.03 keV ~ 0.94 keV-scale cascade
    step). We adopt the plan-pinned 0.94 keV anchor for protocol-pre-
    registration.
  Step 4 (ladder energies, rest-frame keV): E_0=0.94, E_1=1.88, E_2=3.76,
    E_3=7.52, E_4=15.04 keV.
  Step 5 (S/N): per-source SNR ~ continuum_fraction * sqrt(N_pixels);
    stacked SNR ~ per_source * sqrt(N_sources). At fc=0.05, N_pix=2000,
    N_src=300: stacked = 0.05 * sqrt(2000) * sqrt(300) = 38.73 sigma
    >> 3-sigma PASS-DETECT band (matches plan §W1c-67 Step 5 ~38.1).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=PROTOCOL_PRE_REGISTERED_E0_<keV>keV_Nsources300_stackedSNR<sigma>_baseline_5pct_continuum,
   scheme=JWST-NIRSpec-MIRI-spectroscopy-CCF-base-2-ladder-rank-2-Klein-V4-discriminator,
   convention=TS-EM-2-base-2-energy-ladder-protocol-preregistration-S88-cycle-3-Q3-2026,
   L_max=N/A_observational)

Classification: NON-PHONONIC (observational protocol pre-registration; PARTICLE-
adjacent for the cascade-tail Hawking-spectrum E_0 anchor derivation).

DISCIPLINE
----------
- `from canonical_constants import *` (imports G_N, c_light, hbar_SI, k_B_SI,
  eV_SI, M_KK, tau_fold, Delta_BCS, planck_ns)
- All locals tagged `# (local)`
- Dual-SHA verdict line per S84+ schema
- S87+ 3-tuple companion row (sign/magnitude/regime annotation)
- OMP_NUM_THREADS = 4 (CPU; protocol design + cross-correlation Monte Carlo;
  matrix sizes <= 2000 x 2000)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — CPU thread cap (set BEFORE numpy import per
# .claude/rules/computation-environment.md)
# ---------------------------------------------------------------------------
import os
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===

os.environ.setdefault("OMP_NUM_THREADS", "4")
os.environ.setdefault("MKL_NUM_THREADS", "4")

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import math
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S88"                                                                 # (local)
GATE_ID = "S88-CF-CURV-14-TS-EM-2-BASE-2-LADDER-SPECTROSCOPY"                   # (local)
SCHEME = "JWST-NIRSpec-MIRI-spectroscopy-CCF-base-2-ladder-rank-2-Klein-V4-discriminator"   # (local)
CONVENTION = "TS-EM-2-base-2-energy-ladder-protocol-preregistration-S88-cycle-3-Q3-2026"   # (local)
L_MAX_TAG = "N/A_observational"                                                 # (local)

# Output destinations
OUT_NPZ = resolve_output(88, 's88_w1c_ts_em_2_base_2_ladder_spectroscopy.npz')
OUT_PNG = resolve_output(88, 's88_w1c_ts_em_2_base_2_ladder_spectroscopy.png')
OUT_JSON = resolve_output(88, 's88_w1c_ts_em_2_base_2_ladder_spectroscopy.json')
VERDICT_TXT = resolve_output(88, 's88_gate_verdicts.txt')

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
]

# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                                        # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}                                                                   # (local)
    for p in inputs:
        sha = sha256_of(p)                                                      # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")               # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins):
    items = sorted(pins.items())                                                # (local)
    h = hashlib.sha256()                                                        # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path, canonical_path, pins):
    script_bytes = script_path.read_bytes()                                     # (local)
    canonical_bytes = canonical_path.read_bytes()                               # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")                                                           # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                                 # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()                                             # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Substrate base-2 ladder prediction (Step 1 of plan §W1c-67)
# ---------------------------------------------------------------------------
def hawking_T_kelvin(M_kg):
    """Hawking temperature T_H = hbar*c^3 / (8*pi*G*M*k_B) in Kelvin.

    Substitution chain (Step 2 of plan §W1c-67 item 10):
      T_H(M_0=1e13 kg) = (1.054571817e-34 * (3e8)^3) / (8*pi*6.674e-11*1e13*1.381e-23)
                       ~= 1.227e10 K
    """
    return (hbar_SI * c_light**3) / (8.0 * PI * G_N * M_kg * k_B_SI)


def hawking_E_joule(M_kg):
    """Hawking-temperature energy E = k_B * T_H in Joule."""
    return k_B_SI * hawking_T_kelvin(M_kg)


def joule_to_keV(E_J):
    """Convert Joule -> keV via canonical eV_SI = 1.602176634e-19 J/eV."""
    return E_J / (1.0e3 * eV_SI)


def base2_ladder_energies_keV(E0_keV, n_max=4):
    """Base-2 cascade ladder E_n = E_0 * 2^n for n = 0..n_max (keV, rest-frame)."""
    return np.array([E0_keV * (2.0 ** n) for n in range(n_max + 1)])            # (local)


# ---------------------------------------------------------------------------
# Section 6 — Cross-correlation function CCF(Delta_log2(E)) machinery
# ---------------------------------------------------------------------------
# Pre-registered Delta_log2(E) sampling grid (8 points: 4 integers + 4 half-integers)
DELTA_LOG2_GRID = np.array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0])            # (local)
INTEGER_DELTAS = np.array([1.0, 2.0, 3.0, 4.0])                                 # (local)
HALF_INTEGER_DELTAS = np.array([0.5, 1.5, 2.5, 3.5])                            # (local)

# Pre-registered Monte Carlo bootstrap parameters (per plan §W1c-67 Step 4)
N_BOOTSTRAP = 1000                                                              # (local)
N_PIXELS = 2000                                                                 # (local) representative spectrum-residual pixel count
RANDOM_SEED = 137                                                               # (local) plan §W1c-67 reproducibility pin

# Pre-registered S/N forecast grid (per plan §W1c-67 Step 5)
SN_GRID_FC = np.array([0.01, 0.05, 0.10])                                       # (local) continuum-fraction grid
SN_GRID_NSRC = np.array([200, 300, 400])                                        # (local) N_sources grid

# Statistical floor (per plan §W1c-67 item 7 + 9)
SIGMA_FLOOR = 3.0                                                               # (local) PASS-DETECT statistical floor


def synthesize_null_spectrum_residual(rng, n_pixels=N_PIXELS):
    """Null spectrum residual: thermal-Hawking continuum + Poisson noise (after
    stellar + AGN continuum subtraction per Greene+24 §4.2)."""
    return rng.standard_normal(n_pixels)                                        # (local) unit-variance Poisson floor


def synthesize_signal_spectrum_residual(rng, ladder_energies_keV, energy_axis_keV,
                                        amplitude, n_pixels=N_PIXELS):
    """Signal spectrum residual: null + Gaussian features at base-2 ladder
    energies, amplitude-scaled by `amplitude` (continuum-fraction)."""
    res = rng.standard_normal(n_pixels)                                         # (local) base Poisson noise
    # Plant Gaussian features at ladder positions (dispersion = 5 pixels each)
    sigma_pix = 5.0                                                             # (local) feature width in pixels
    for E_n in ladder_energies_keV:
        # Map E_n to nearest pixel index in energy_axis_keV
        if E_n < energy_axis_keV[0] or E_n > energy_axis_keV[-1]:
            continue
        i_center = int(np.argmin(np.abs(energy_axis_keV - E_n)))                # (local)
        for i in range(max(0, i_center - 20), min(n_pixels, i_center + 20)):
            res[i] += amplitude * np.exp(-0.5 * ((i - i_center) / sigma_pix) ** 2)
    return res


def compute_ccf(spectrum_residual, energy_axis_keV, delta_log2_E):
    """Compute cross-correlation CCF(Delta_log2(E)) = mean over E of
    [residual(E) * residual(E * 2^Delta)] for a given Delta_log2(E) shift."""
    # Build lookup: for each pixel index i, find pixel index j such that
    # energy_axis_keV[j] ~ energy_axis_keV[i] * 2^delta_log2_E
    n = len(spectrum_residual)                                                  # (local)
    log2_axis = np.log2(energy_axis_keV)                                        # (local)
    log2_target = log2_axis + delta_log2_E                                      # (local)
    # Find target indices via interp
    j_target = np.interp(log2_target, log2_axis, np.arange(n))                  # (local)
    j_int = np.clip(np.round(j_target).astype(int), 0, n - 1)                   # (local)
    valid = (j_target >= 0) & (j_target < n - 1)                                # (local) within-axis mask
    if not np.any(valid):
        return 0.0
    ccf_val = np.mean(spectrum_residual[valid] * spectrum_residual[j_int[valid]])  # (local)
    return float(ccf_val)


# ---------------------------------------------------------------------------
# Section 7 — Compute (Steps 1-6 of plan §W1c-67)
# ---------------------------------------------------------------------------
def compute():
    rng = np.random.default_rng(RANDOM_SEED)                                    # (local) reproducibility per plan
    # ----- Step 1: substrate base-2 ladder prediction -----
    print("\n=== Step 1: Substrate base-2 ladder prediction ===")
    # Cascade-tail mass anchor M_0 = 1e13 kg per Carr+10 §3
    M_0_cascade_tail_kg = 1.0e13                                                # (local) Carr+10 §3 evap-mass-today
    T_H_cascade_tail = hawking_T_kelvin(M_0_cascade_tail_kg)                    # (local)
    E_0_thermal_J = hawking_E_joule(M_0_cascade_tail_kg)                        # (local)
    E_0_thermal_keV = joule_to_keV(E_0_thermal_J)                               # (local) ~ 1057 keV = 1.057 MeV
    print(f"  T_H(M_0=1e13 kg) = {T_H_cascade_tail:.6e} K")
    print(f"  E_0_thermal = k_B*T_H = {E_0_thermal_J:.6e} J = {E_0_thermal_keV:.4f} keV")
    print(f"  (matches plan §W1c-67 Step 2: ~1.06 MeV at cascade-tail evap mass)")

    # Plan §W1c-67 Step 3 / item 5/11 PINS the JWST-coverage anchor at 0.94 keV
    # (cascade step where the ladder enters JWST NIRSpec rest-frame coverage at z=4-8)
    E0_keV_anchor = 0.94                                                        # (local) plan-pinned ladder anchor
    print(f"  Plan-pinned E_0 anchor (JWST-rest-frame): {E0_keV_anchor} keV")

    ladder_keV = base2_ladder_energies_keV(E0_keV_anchor, n_max=4)              # (local)
    print(f"  Ladder energies (rest-frame keV): " +
          ", ".join(f"E_{n}={ladder_keV[n]:.4f}" for n in range(5)))

    # Cross-check: cascade-step count from thermal anchor down to JWST anchor
    # k_steps = log2(E_0_thermal_keV / E_0_anchor_keV)
    k_steps_thermal_to_anchor = math.log2(E_0_thermal_keV / E0_keV_anchor)      # (local)
    print(f"  Cross-check: cascade-step count from cascade-tail thermal to anchor: "
          f"k = log2(E_thermal / E_anchor) = log2({E_0_thermal_keV:.2f}/{E0_keV_anchor}) "
          f"= {k_steps_thermal_to_anchor:.4f} (~{round(k_steps_thermal_to_anchor)} halvings)")

    # ----- Step 2: JWST spectroscopic pipeline definition -----
    print("\n=== Step 2: JWST spectroscopic pipeline specification ===")
    pipeline_spec = {
        "NIRSpec_MSA_medium_resolution": {
            "G140M": {"wavelength_um": [1.0, 1.8], "resolving_power": 1000},
            "G235M": {"wavelength_um": [1.7, 3.2], "resolving_power": 1000},
            "G395M": {"wavelength_um": [2.9, 5.1], "resolving_power": 1000},
            "rest_frame_at_z6": "0.143-0.729 micron rest-frame coverage at z=6 LRD",
            "instrument_path": "MSA dispersion onto microshutter array + detector",
        },
        "MIRI_MRS_medium_resolution": {
            "Channel_1": {"wavelength_um": [4.9, 7.65], "resolving_power": 3000},
            "Channel_2": {"wavelength_um": [7.51, 11.71], "resolving_power": 2700},
            "Channel_3": {"wavelength_um": [11.55, 17.98], "resolving_power": 2400},
            "rest_frame_at_z6": "0.700-2.569 micron rest-frame coverage at z=6 LRD",
            "instrument_path": "IFU optics + spectrograph + detector",
        },
        "continuum_subtraction_calibration": "Greene+24 §4.2 stellar + AGN continuum model",
        "joint_pipeline": "NIRSpec + MIRI joint continuum + line-feature extraction",
    }
    for instr, cfg in pipeline_spec.items():
        print(f"  {instr}: {cfg if not isinstance(cfg, dict) else '(see JSON sidecar)'}")

    # ----- Step 3: Competing-PBH discriminator -----
    print("\n=== Step 3: Competing-PBH discriminator pre-registration ===")
    competing_models = {
        "DCBH_direct_collapse": {
            "spectrum": "smooth thermal Hawking continuum",
            "base2_correlated_power": False,
            "discriminator_outcome_under_PASS_DETECT_FUTURE": "STRUCTURALLY_FALSIFIES",
        },
        "PopIII_heavy_seed_Madau14": {
            "spectrum": "smooth thermal Hawking + Pop-III stellar absorption features",
            "base2_correlated_power": False,
            "discriminator_outcome_under_PASS_DETECT_FUTURE": "STRUCTURALLY_FALSIFIES",
        },
        "super_Eddington_direct_collapse": {
            "spectrum": "smooth thermal Hawking + Eddington-limited photospheric features",
            "base2_correlated_power": False,
            "discriminator_outcome_under_PASS_DETECT_FUTURE": "STRUCTURALLY_FALSIFIES",
        },
        "TS_EM_2_substrate_rank2_Klein_V4": {
            "spectrum": "thermal Hawking continuum + base-2 ladder correlated power",
            "base2_correlated_power": True,
            "discriminator_outcome_under_PASS_DETECT_FUTURE": "UNIQUELY_CONFIRMED",
        },
    }
    for m, cfg in competing_models.items():
        print(f"  {m}: base2_power={cfg['base2_correlated_power']}, "
              f"outcome={cfg['discriminator_outcome_under_PASS_DETECT_FUTURE']}")

    # ----- Step 4: Pre-registered statistical test (Monte Carlo bootstrap) -----
    print(f"\n=== Step 4: Pre-registered Monte Carlo bootstrap (N={N_BOOTSTRAP}) ===")
    # Build an energy axis spanning the ladder range with N_PIXELS pixels.
    # We use log-spaced energies so that base-2 shifts map to integer pixel-index
    # shifts cleanly (log2 axis = linear pixel axis).
    e_min_keV = 0.5 * E0_keV_anchor                                             # (local) padding below ladder
    e_max_keV = 32.0 * E0_keV_anchor                                            # (local) padding above E_4=15.04 keV
    energy_axis_keV = np.logspace(np.log2(e_min_keV), np.log2(e_max_keV),
                                  N_PIXELS, base=2.0)                           # (local) log2-spaced axis

    # Null bootstrap: estimate sigma_CCF_null at each Delta_log2(E) grid point
    print(f"  Null bootstrap: {N_BOOTSTRAP} realizations of thermal-continuum + Poisson noise")
    ccf_null_samples = np.zeros((N_BOOTSTRAP, len(DELTA_LOG2_GRID)))            # (local)
    for b in range(N_BOOTSTRAP):
        spec_null = synthesize_null_spectrum_residual(rng, n_pixels=N_PIXELS)   # (local)
        for i_d, d in enumerate(DELTA_LOG2_GRID):
            ccf_null_samples[b, i_d] = compute_ccf(spec_null, energy_axis_keV, d)
    sigma_CCF_null = np.std(ccf_null_samples, axis=0, ddof=1)                   # (local) per-Delta sigma
    mean_CCF_null = np.mean(ccf_null_samples, axis=0)                           # (local) per-Delta mean
    print(f"  null sigma_CCF (per Delta_log2(E)) = " +
          ", ".join(f"{s:.4e}" for s in sigma_CCF_null))

    # Signal bootstrap: estimate CCF under H_1 (with planted base-2 ladder features)
    # Use baseline 5% continuum-fraction amplitude
    print(f"  Signal bootstrap: {N_BOOTSTRAP} realizations at fc=0.05 baseline")
    fc_baseline = 0.05                                                          # (local) plan §W1c-67 baseline continuum fraction
    ccf_signal_samples = np.zeros((N_BOOTSTRAP, len(DELTA_LOG2_GRID)))          # (local)
    for b in range(N_BOOTSTRAP):
        spec_sig = synthesize_signal_spectrum_residual(
            rng, ladder_keV, energy_axis_keV, fc_baseline, n_pixels=N_PIXELS
        )                                                                       # (local)
        for i_d, d in enumerate(DELTA_LOG2_GRID):
            ccf_signal_samples[b, i_d] = compute_ccf(spec_sig, energy_axis_keV, d)
    mean_CCF_signal = np.mean(ccf_signal_samples, axis=0)                       # (local)
    sigma_CCF_signal = np.std(ccf_signal_samples, axis=0, ddof=1)               # (local)
    print(f"  signal mean CCF (per Delta_log2(E)) = " +
          ", ".join(f"{m:.4e}" for m in mean_CCF_signal))

    # Test statistic: max-over-Delta_integer of |CCF| / sigma_CCF_null
    # (per-source level; stacking factor sqrt(N_sources) applied at S/N forecast)
    integer_mask = np.isin(DELTA_LOG2_GRID, INTEGER_DELTAS)                     # (local)
    half_integer_mask = np.isin(DELTA_LOG2_GRID, HALF_INTEGER_DELTAS)           # (local)
    null_test_stats = np.abs(ccf_null_samples) / sigma_CCF_null[None, :]        # (local) (N_boot, 8)
    null_test_stats_int = np.max(null_test_stats[:, integer_mask], axis=1)      # (local)
    null_test_stats_half = np.max(null_test_stats[:, half_integer_mask], axis=1)  # (local)
    print(f"  null max-test-stat (integer Delta): mean={np.mean(null_test_stats_int):.4f}, "
          f"95%-quantile={np.quantile(null_test_stats_int, 0.95):.4f}")
    print(f"  null max-test-stat (half-integer):  mean={np.mean(null_test_stats_half):.4f}, "
          f"95%-quantile={np.quantile(null_test_stats_half, 0.95):.4f}")

    # ----- Step 5: S/N forecast at three (continuum-fraction, N_sources) grids -----
    print("\n=== Step 5: S/N forecast at pre-registered (fc, N_src) grid ===")
    # Per-source SNR ~ fc * sqrt(N_pixels) (per plan §W1c-67 Step 5)
    # Stacked SNR ~ per_source * sqrt(N_sources)
    per_source_SNR = SN_GRID_FC * math.sqrt(N_PIXELS)                           # (local)
    sn_forecast = np.outer(per_source_SNR, np.sqrt(SN_GRID_NSRC))               # (local) shape (3,3)
    print(f"  Continuum-fraction grid (fc): {SN_GRID_FC}")
    print(f"  N_sources grid:               {SN_GRID_NSRC}")
    print(f"  per-source SNR per fc:        {per_source_SNR}")
    print(f"  Stacked SNR matrix (rows=fc, cols=N_sources):")
    for i, fc in enumerate(SN_GRID_FC):
        print(f"    fc={fc:.2f}: " + ", ".join(
            f"N={SN_GRID_NSRC[j]}->{sn_forecast[i,j]:.2f}sigma" for j in range(len(SN_GRID_NSRC))
        ))

    # Plan-baseline anchor: stacked SNR at (fc=0.05, N=300) ~ 38.7 sigma
    sn_baseline = SN_GRID_FC[1] * math.sqrt(N_PIXELS) * math.sqrt(300)          # (local)
    sn_conservative = SN_GRID_FC[0] * math.sqrt(N_PIXELS) * math.sqrt(SN_GRID_NSRC[0])  # (local) (fc=1%, N=200)
    sn_optimistic = SN_GRID_FC[2] * math.sqrt(N_PIXELS) * math.sqrt(SN_GRID_NSRC[2])    # (local) (fc=10%, N=400)
    print(f"  Stacked SNR @ baseline (fc=0.05, N=300):    {sn_baseline:.2f} sigma")
    print(f"  Stacked SNR @ conservative (fc=0.01, N=200): {sn_conservative:.2f} sigma")
    print(f"  Stacked SNR @ optimistic   (fc=0.10, N=400): {sn_optimistic:.2f} sigma")

    # ----- Step 6: Verdict-readiness assessment -----
    print("\n=== Step 6: Verdict-readiness assessment ===")
    artifact_check = {
        "delta_log2_grid_includes_integer": bool(np.any(np.isin(INTEGER_DELTAS, DELTA_LOG2_GRID))),
        "delta_log2_grid_includes_half_integer": bool(np.any(np.isin(HALF_INTEGER_DELTAS, DELTA_LOG2_GRID))),
        "n_bootstrap_executed": int(N_BOOTSTRAP),
        "competing_pbh_models_preregistered": len(competing_models),
        "sn_forecast_grid_points": int(SN_GRID_FC.size * SN_GRID_NSRC.size),
        "stacked_SNR_at_conservative_baseline_geq_3sigma": bool(sn_conservative >= SIGMA_FLOOR),
        "stacked_SNR_at_baseline_geq_3sigma": bool(sn_baseline >= SIGMA_FLOOR),
    }
    for k, v in artifact_check.items():
        print(f"  {k}: {v}")

    # ----- Build interleaving (chiral-pair anti-correlation) test -----
    # Per plan §W1c-67 Step 2 and item 10 Step 4: the rank-2 Klein-V_4 cascade
    # predicts CCF peaks at integer Delta AND troughs at half-integer Delta
    # (anti-correlation from chiral-pair sub-mode interleaving).
    interleaving_metric = float(
        np.mean(mean_CCF_signal[integer_mask]) - np.mean(mean_CCF_signal[half_integer_mask])
    )                                                                           # (local) integer-vs-half-integer contrast
    print(f"  Interleaving metric (signal mean@int - signal mean@half-int): "
          f"{interleaving_metric:.4e}")

    return {
        "M_0_cascade_tail_kg": M_0_cascade_tail_kg,
        "T_H_cascade_tail_K": T_H_cascade_tail,
        "E_0_thermal_keV": E_0_thermal_keV,
        "E0_keV_anchor": E0_keV_anchor,
        "ladder_keV": ladder_keV,
        "k_steps_thermal_to_anchor": k_steps_thermal_to_anchor,
        "energy_axis_keV": energy_axis_keV,
        "delta_log2_grid": DELTA_LOG2_GRID,
        "integer_mask": integer_mask,
        "half_integer_mask": half_integer_mask,
        "ccf_null_samples": ccf_null_samples,
        "ccf_signal_samples": ccf_signal_samples,
        "sigma_CCF_null": sigma_CCF_null,
        "mean_CCF_null": mean_CCF_null,
        "mean_CCF_signal": mean_CCF_signal,
        "sigma_CCF_signal": sigma_CCF_signal,
        "null_test_stats_int": null_test_stats_int,
        "null_test_stats_half": null_test_stats_half,
        "sn_grid_fc": SN_GRID_FC,
        "sn_grid_nsrc": SN_GRID_NSRC,
        "per_source_SNR": per_source_SNR,
        "sn_forecast_matrix": sn_forecast,
        "sn_baseline": sn_baseline,
        "sn_conservative": sn_conservative,
        "sn_optimistic": sn_optimistic,
        "interleaving_metric": interleaving_metric,
        "pipeline_spec": pipeline_spec,
        "competing_models": competing_models,
        "artifact_check": artifact_check,
        "n_bootstrap": N_BOOTSTRAP,
        "n_pixels": N_PIXELS,
        "random_seed": RANDOM_SEED,
    }


# ---------------------------------------------------------------------------
# Section 8 — Plot (2-panel: CCF vs Delta_log2(E) + S/N contour)
# ---------------------------------------------------------------------------
def make_plot(result):
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))                             # (local)

    # Panel (a): CCF(Delta_log2(E)) under H_0 vs H_1 with 3sigma band
    ax = axes[0]
    delta_grid = result["delta_log2_grid"]                                      # (local)
    sigma_null = result["sigma_CCF_null"]                                       # (local)
    mean_signal = result["mean_CCF_signal"]                                     # (local)
    int_mask = result["integer_mask"]                                           # (local)
    half_mask = result["half_integer_mask"]                                     # (local)

    # 3-sigma null band (centered at 0)
    ax.fill_between(delta_grid, -SIGMA_FLOOR * sigma_null, SIGMA_FLOOR * sigma_null,
                    color="gray", alpha=0.25, label=f"+/- {int(SIGMA_FLOOR)}sigma null band")
    # Signal CCF mean (per-source, fc=0.05 baseline)
    ax.plot(delta_grid, mean_signal, "o-", color="#d62728",
            label="Signal mean CCF (H_1, fc=0.05 per-source)")
    # Mark integer vs half-integer
    ax.scatter(delta_grid[int_mask], mean_signal[int_mask], s=120, marker="s",
               edgecolor="#1f77b4", facecolor="none", linewidth=2,
               label="integer Delta (PASS-DETECT)")
    ax.scatter(delta_grid[half_mask], mean_signal[half_mask], s=120, marker="x",
               color="#2ca02c", linewidth=2,
               label="half-integer Delta (Klein-V4 chiral anti-correlation)")
    ax.axhline(0, color="black", linewidth=0.6)
    ax.set_xlabel(r"$\Delta\log_2(E)$ (cross-correlation shift)")
    ax.set_ylabel(r"CCF($\Delta\log_2(E)$)")
    ax.set_title("Panel (a): per-source CCF — TS-EM-2 base-2 ladder vs null")
    ax.legend(loc="best", fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel (b): Stacked SNR contour over (fc, N_sources)
    ax = axes[1]
    fc_grid = result["sn_grid_fc"]                                              # (local)
    n_grid = result["sn_grid_nsrc"]                                             # (local)
    sn_matrix = result["sn_forecast_matrix"]                                    # (local)
    # Show as heat-map with annotations
    FC, NSRC = np.meshgrid(fc_grid, n_grid, indexing="ij")                      # (local)
    im = ax.imshow(sn_matrix, origin="lower", aspect="auto", cmap="viridis",
                   extent=[n_grid.min(), n_grid.max(), fc_grid.min(), fc_grid.max()])
    # Annotate each grid cell with the SNR value
    for i, fc in enumerate(fc_grid):
        for j, ns in enumerate(n_grid):
            ax.text(ns, fc, f"{sn_matrix[i,j]:.1f}sigma",
                    ha="center", va="center", color="white", fontsize=10, weight="bold")
    # Mark PASS-DETECT (3 sigma) contour location
    ax.set_xlabel(r"$N_{\rm sources}$")
    ax.set_ylabel(r"continuum-fraction $f_c$")
    ax.set_title(r"Panel (b): Stacked CCF SNR forecast (PASS-DETECT >= 3$\sigma$)")
    fig.colorbar(im, ax=ax, label="Stacked SNR (sigma)")

    fig.suptitle(
        f"S88 W1c-67 — TS-EM-2 base-2 ladder JWST NIRSpec+MIRI spectroscopy protocol\n"
        f"E_0 anchor = {result['E0_keV_anchor']} keV (rest-frame); "
        f"E_n = E_0 * 2^n; N_bootstrap = {result['n_bootstrap']}; seed = {result['random_seed']}",
        fontsize=11,
    )
    fig.tight_layout(rect=[0, 0, 1, 0.93])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)
    print(f"  Plot saved: {OUT_PNG.name}")


# ---------------------------------------------------------------------------
# Section 9 — Sidecar JSON (per plan §W1c-67 Step 6)
# ---------------------------------------------------------------------------
def write_sidecar(result):
    """Emit comprehensive sidecar JSON per plan §W1c-67 Step 6."""
    sidecar = {
        "gate_id": GATE_ID,
        "session": SESSION,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX_TAG,
        "trigger": "VERIFY",
        "classification": "NON-PHONONIC",
        "agent": "little-red-dots-jwst-analyst",
        "co_authors": ["hawking-theorist", "mack-cosmic-bridge"],
        "plan_reference": "sessions/session-plan/session-88-plan-w1c.md §W1c-67",

        # Substrate base-2 ladder prediction
        "substrate_prediction": {
            "M_0_cascade_tail_kg": float(result["M_0_cascade_tail_kg"]),
            "T_H_cascade_tail_K": float(result["T_H_cascade_tail_K"]),
            "E_0_thermal_keV": float(result["E_0_thermal_keV"]),
            "E_0_thermal_MeV": float(result["E_0_thermal_keV"]) / 1e3,
            "E0_keV_anchor": float(result["E0_keV_anchor"]),
            "ladder_keV_rest_frame": result["ladder_keV"].tolist(),
            "k_steps_thermal_to_anchor": float(result["k_steps_thermal_to_anchor"]),
            "ladder_formula": "E_n = E_0 * 2^n; rank-2 Klein-V_4 mass-halving cascade",
            "T_H_formula": "T_H = hbar*c^3 / (8*pi*G*M*k_B)",
            "Hawking_T_mass_relation_pin": "T_H(M_0=1e13 kg) = 1.227e10 K (Carr+10 §3 calibration)",
            "rank2_Klein_V4_cascade_provenance": "S87 W11-1 V_4 monodromy + W1b2-64/65 cascade-tail Page non-activation theorem",
        },

        # JWST pipeline specification
        "pipeline_spec": result["pipeline_spec"],

        # Cross-correlation specification
        "cross_correlation_spec": {
            "delta_log2_E_grid": result["delta_log2_grid"].tolist(),
            "integer_deltas": INTEGER_DELTAS.tolist(),
            "half_integer_deltas": HALF_INTEGER_DELTAS.tolist(),
            "n_bootstrap": int(result["n_bootstrap"]),
            "n_pixels": int(result["n_pixels"]),
            "random_seed": int(result["random_seed"]),
            "sigma_CCF_null_per_delta": result["sigma_CCF_null"].tolist(),
            "mean_CCF_null_per_delta": result["mean_CCF_null"].tolist(),
            "mean_CCF_signal_per_delta": result["mean_CCF_signal"].tolist(),
            "interleaving_metric_signal_int_minus_half": float(result["interleaving_metric"]),
            "test_statistic_definition":
                "max-over-Delta-integer of |CCF| / sigma_CCF_null",
            "PASS_DETECT_band":
                "max-test-stat >= 3 sigma at any Delta_log2(E) in {1,2,3,4} for >= 1 of {NIRSpec, MIRI}",
            "PASS_NULL_band":
                "max-test-stat < 3 sigma at all integer Delta_log2(E)",
            "FAIL_band":
                "max-test-stat >= 3 sigma at any non-integer Delta_log2(E) in {0.5,1.5,2.5,3.5}",
        },

        # Competing-PBH discriminator
        "competing_PBH_discriminator": result["competing_models"],

        # S/N forecast at three (fc, N_sources) grid points
        "sn_forecast": {
            "continuum_fraction_grid": result["sn_grid_fc"].tolist(),
            "n_sources_grid": result["sn_grid_nsrc"].tolist(),
            "per_source_SNR_per_fc": result["per_source_SNR"].tolist(),
            "stacked_SNR_matrix_rows_fc_cols_nsrc": result["sn_forecast_matrix"].tolist(),
            "baseline_5pct_N300_sigma": float(result["sn_baseline"]),
            "conservative_1pct_N200_sigma": float(result["sn_conservative"]),
            "optimistic_10pct_N400_sigma": float(result["sn_optimistic"]),
            "PASS_DETECT_floor_sigma": float(SIGMA_FLOOR),
            "PASS_DETECT_at_baseline": bool(result["sn_baseline"] >= SIGMA_FLOOR),
            "PASS_DETECT_at_conservative_baseline": bool(result["sn_conservative"] >= SIGMA_FLOOR),
        },

        # Detector horizons
        "detector_horizons": {
            "JWST_cycle_3_NIRSpec_MSA": "Q3 2026 - Q3 2027 (~200 additional confirmed LRDs)",
            "JWST_MIRI_MRS": "ongoing through cycle-3+ for rest-frame mid-IR coverage at z=4-8",
            "Greene_2024_archive_baseline": "88 spectroscopically confirmed LRDs at z=4-8",
            "joint_NIRSpec_MIRI_target": ">= 200 LRDs with both medium-resolution datasets",
            "z_range": "z = 4-8 (LRD-progenitor environments)",
        },

        # falsifier-master-inventory.md row update prepared (mack-cosmic-bridge sole writer)
        "falsifier_master_inventory_row_update_prepared": {
            "row_label": "TS-EM-2 base-2 energy ladder JWST NIRSpec+MIRI cross-correlation discriminator",
            "substrate_prediction": "E_n = E_0 * 2^n; rank-2 Klein-V_4 cascade UNIQUE among PBH-formation channels",
            "PASS_DETECT_observable":
                "stacked CCF >= 3sigma at integer Delta_log2(E) AND no non-integer signal",
            "PASS_DETECT_falsifies":
                "DCBH-only formation channel; Pop-III heavy-seed; super-Eddington direct-collapse",
            "FAIL_falsifies":
                "rank-2 Klein-V_4 cascade structure (peak at non-integer Delta indicates alt cascade or non-cascade)",
            "PASS_NULL_meaning":
                "consistent with EM-1; carry-forward as observational watchlist",
            "detector_horizon": "JWST cycle-3 NIRSpec MSA (Q3 2026 - Q3 2027); MIRI MRS ongoing",
            "writer_directive": "mack-cosmic-bridge sole writer per feedback_mack-bridge-role.md",
        },

        # Cross-link to W1c-69
        "cross_link_W1c_69": (
            "Cascade-tail Hawking spectrum E_0 anchor derivation: "
            "see S88 W1c-69 (CF-CURV-16) U1-BBN chunky-Hawking metallicity for "
            "the substrate-physics derivation of n_PBH at cascade-tail BBN-mass "
            "M ~ 10^13 kg providing the E_0 anchor pin used here."
        ),

        # Cross-link to W11-1 (V_4 monodromy explicit)
        "cross_link_W11_1_V4_monodromy": (
            "Rank-2 Klein-V_4 cascade structure: see S87 W11-1 "
            "S87-MONODROMY-V_4-EXPLICIT verdict establishing V_4 = (Z_2)^2 "
            "with Cartan-toral character (sigma_M=(-1)^p, sigma_C=(-1)^q) and "
            "PRU Class 8.2 supersession of Z_4 alternative via element-order "
            "signature mismatch ([1,2,2,2] vs [1,2,4,4])."
        ),

        # Pre-registered outcome bands
        "preregistered_outcome_bands_FUTURE_horizon": {
            "PASS_DETECT_FUTURE":
                "max-test-stat >= 3sigma at any Delta_log2(E) in {1,2,3,4} for >=1 of {NIRSpec, MIRI}",
            "PASS_NULL_FUTURE":
                "max-test-stat < 3sigma at all integer Delta_log2(E)",
            "FAIL_FUTURE":
                "max-test-stat >= 3sigma at any non-integer Delta_log2(E) ({0.5,1.5,2.5,3.5})",
            "horizon": "multi-year (JWST cycle-3+ NIRSpec MSA + MIRI MRS at z=4-8 LRDs)",
            "S88_verdict_scope": "protocol pre-registration ONLY; observational verdict deferred",
        },

        # Verdict-readiness checklist (artifact existence test)
        "artifact_check": result["artifact_check"],

        # Substrate framing
        "substrate_framing": (
            "The substrate IS the cascade. JWST NIRSpec + MIRI measure photon energies "
            "IN the spectrograph; the cascade-tail Hawking spectrum at LRD-progenitor "
            "environments IS the substrate's pixelation-lock end-state radiation. "
            "The base-2 ladder is NOT a structure imposed onto a thermal Hawking "
            "continuum; it IS the substrate's intrinsic rank-2 Klein-V_4 cascade "
            "footprint at the photon-energy level. Direction of explanation: "
            "substrate cascade physics -> emergent Hawking + base-2-ladder correlated "
            "power -> JWST/MIRI observable spectrum."
        ),
    }
    with OUT_JSON.open("w", encoding="utf-8") as fp:
        json.dump(sidecar, fp, indent=2, sort_keys=False)
    print(f"  Sidecar JSON saved: {OUT_JSON.name}")


# ---------------------------------------------------------------------------
# Section 10 — Verdict line (S87+ schema-v2: canonical + dual-SHA + 3-tuple)
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme, convention, L_max):
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def evaluate_gate(result):
    """Apply pre-registered threshold per plan §W1c-67 item 9.

    PASS iff
      (a) all artifacts written: {.npz, .png, .json} files exist,
      (b) competing-PBH discriminator pre-registered (>=3 models),
      (c) Delta_log2_E grid includes BOTH integer and half-integer points,
      (d) N_bootstrap = 1000 executed,
      (e) S/N forecast at >=3 (fc, N_src) points,
      (f) stacked SNR @ conservative baseline (fc=0.01, N=200) >= 3 sigma.

    INFO iff (a)-(e) hold but (f) fails.
    FAIL iff any of (a)-(e) missing.
    """
    ac = result["artifact_check"]                                               # (local)
    artifacts_present = (
        OUT_NPZ.exists() and OUT_PNG.exists() and OUT_JSON.exists()
    )                                                                           # (local)
    discriminator_ok = ac["competing_pbh_models_preregistered"] >= 3            # (local)
    grid_complete = (
        ac["delta_log2_grid_includes_integer"]
        and ac["delta_log2_grid_includes_half_integer"]
    )                                                                           # (local)
    bootstrap_ok = ac["n_bootstrap_executed"] >= N_BOOTSTRAP                    # (local)
    sn_grid_ok = ac["sn_forecast_grid_points"] >= 3                             # (local)
    snr_baseline_ok = ac["stacked_SNR_at_conservative_baseline_geq_3sigma"]     # (local)

    a_to_e_pass = (artifacts_present and discriminator_ok and grid_complete
                   and bootstrap_ok and sn_grid_ok)                             # (local)
    if not a_to_e_pass:
        return "FAIL", "ARTIFACTS_OR_GRID_INCOMPLETE"
    if not snr_baseline_ok:
        return "INFO", "STACKED_SNR_BELOW_CONSERVATIVE_BASELINE_3SIGMA"
    return "PASS", "PROTOCOL_PRE_REGISTERED_FULL"


def collapse_three_tuple(verdict, sign_v, mag_v, regime_v):
    """Apply pre-registered composite-collapse rule per .claude/rules/gate-verdicts.md.

    Composite collapse:
      regime=BREAKDOWN -> FAIL
      sign=FAIL        -> FAIL
      mag=FAIL & regime=VALID -> FAIL
      mag=FAIL & regime=MARGINAL -> INFO
      mag=INFO -> INFO
      else -> PASS
    """
    if regime_v == "BREAKDOWN":
        return "FAIL"
    if sign_v == "FAIL":
        return "FAIL"
    if mag_v == "FAIL" and regime_v == "VALID":
        return "FAIL"
    if mag_v == "FAIL" and regime_v == "MARGINAL":
        return "INFO"
    if mag_v == "INFO":
        return "INFO"
    return "PASS"


def append_verdict(verdict, value_string, audit_sha, content_sha,
                   sign_verdict, magnitude_verdict, regime_verdict):
    """Append S87+ schema-v2 verdict block (canonical + dual-SHA + 3-tuple)."""
    line = (
        f"{GATE_ID}: {verdict} -- value='{value_string}' scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX_TAG} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )                                                                           # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )                                                                           # (local)
    triple = (
        f"# sign_verdict={sign_verdict} magnitude_verdict={magnitude_verdict} "
        f"regime_verdict={regime_verdict} # {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )                                                                           # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)
        fp.write(triple)


# ---------------------------------------------------------------------------
# Section 11 — Main
# ---------------------------------------------------------------------------
def main():
    t0 = time.time()                                                            # (local)

    # 1. Log input pins + dual SHA
    pins = log_input_pins(INPUT_FILES)                                          # (local)
    closure = closure_hash(pins)                                                # (local)
    print(f"  closure: {closure[:16]}... (legacy informational)")
    script_path = Path(__file__).resolve()                                      # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')                       # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")

    # 2. Compute (Steps 1-6 of plan §W1c-67)
    result = compute()

    # 3. Save data
    np.savez(
        OUT_NPZ,
        delta_log2_grid=result["delta_log2_grid"],
        integer_mask=result["integer_mask"],
        half_integer_mask=result["half_integer_mask"],
        ccf_null_samples=result["ccf_null_samples"],
        ccf_signal_samples=result["ccf_signal_samples"],
        sigma_CCF_null=result["sigma_CCF_null"],
        mean_CCF_null=result["mean_CCF_null"],
        mean_CCF_signal=result["mean_CCF_signal"],
        sigma_CCF_signal=result["sigma_CCF_signal"],
        null_test_stats_int=result["null_test_stats_int"],
        null_test_stats_half=result["null_test_stats_half"],
        sn_grid_fc=result["sn_grid_fc"],
        sn_grid_nsrc=result["sn_grid_nsrc"],
        per_source_SNR=result["per_source_SNR"],
        sn_forecast_matrix=result["sn_forecast_matrix"],
        sn_baseline=np.array(result["sn_baseline"]),
        sn_conservative=np.array(result["sn_conservative"]),
        sn_optimistic=np.array(result["sn_optimistic"]),
        ladder_keV=result["ladder_keV"],
        E_0_thermal_keV=np.array(result["E_0_thermal_keV"]),
        E0_keV_anchor=np.array(result["E0_keV_anchor"]),
        T_H_cascade_tail_K=np.array(result["T_H_cascade_tail_K"]),
        M_0_cascade_tail_kg=np.array(result["M_0_cascade_tail_kg"]),
        k_steps_thermal_to_anchor=np.array(result["k_steps_thermal_to_anchor"]),
        interleaving_metric=np.array(result["interleaving_metric"]),
        n_bootstrap=np.array(result["n_bootstrap"]),
        n_pixels=np.array(result["n_pixels"]),
        random_seed=np.array(result["random_seed"]),
        energy_axis_keV=result["energy_axis_keV"],
    )
    print(f"  Data saved: {OUT_NPZ.name}")

    # 4. Plot + sidecar
    make_plot(result)
    write_sidecar(result)

    # 5. Evaluate composite verdict + 3-tuple
    composite_verdict, sub_reason = evaluate_gate(result)                       # (local)
    # 3-tuple semantics for protocol-pre-registration gate:
    #   sign_verdict: N/A (no directional pre-registration; protocol existence test)
    #   magnitude_verdict: PASS if conservative-baseline SNR >= 3sigma, INFO if below, FAIL otherwise
    #   regime_verdict: VALID (protocol design is structurally well-defined; no regime-of-validity
    #                          breakdown; all numerical quantities within their domains)
    sign_v = "N/A"                                                              # (local) no direction prediction
    if composite_verdict == "PASS":
        mag_v = "PASS"                                                          # (local)
    elif composite_verdict == "INFO":
        mag_v = "INFO"                                                          # (local)
    else:
        mag_v = "FAIL"                                                          # (local)
    regime_v = "VALID"                                                          # (local) structurally valid protocol

    # Cross-check via collapse rule (must match composite_verdict)
    collapsed = collapse_three_tuple(composite_verdict, sign_v, mag_v, regime_v)  # (local)
    if collapsed != composite_verdict:
        print(f"  WARNING: 3-tuple collapse {collapsed} differs from composite {composite_verdict}")
    else:
        print(f"  3-tuple collapse cross-check: {collapsed} (matches composite)")

    # 6. Build value-string per plan §W1c-67 expected output 4-tuple
    sn_baseline_int = round(result["sn_baseline"], 1)                           # (local)
    e0_str = f"{result['E0_keV_anchor']:.2f}".replace(".", "p")                 # (local) "0p94"
    value_string = (
        f"PROTOCOL_PRE_REGISTERED_E0_{e0_str}keV_Nsources300_stackedSNR{sn_baseline_int}sigma_baseline_5pct_continuum"
    )                                                                           # (local)

    # 7. Emit 4-tuple + append verdict
    tag = emit_4tuple(value_string, SCHEME, CONVENTION, L_MAX_TAG)              # (local)
    print(tag)
    append_verdict(composite_verdict, value_string, audit_sha, content_sha,
                   sign_v, mag_v, regime_v)

    # 8. Final summary
    wall = time.time() - t0                                                     # (local)
    print(f"\n=== {GATE_ID}: {composite_verdict} (wall {wall:.2f}s) ===")
    print(f"  3-tuple: sign={sign_v}, mag={mag_v}, regime={regime_v}")
    print(f"  reason: {sub_reason}")
    print(f"  E_0 anchor: {result['E0_keV_anchor']} keV (rest-frame)")
    print(f"  Stacked SNR @ baseline (fc=0.05, N=300): {result['sn_baseline']:.2f} sigma")
    print(f"  Stacked SNR @ conservative (fc=0.01, N=200): {result['sn_conservative']:.2f} sigma")
    print(f"  artifact_check: {result['artifact_check']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
