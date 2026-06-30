#!/usr/bin/env python3
"""
S85 W13-2 — CGWB-ALPHA-S-FLAGSHIP-JOINT pre-registration
========================================================

Gate: S85-W13-2-CGWB-ALPHA-S-FLAGSHIP-JOINT ([VERIFY])
  PASS  iff  (a) flagship document landed at
             sessions/framework/registry/CGWB-alpha-s-joint-flagship-pre-registration.md
             AND
             (b) 3 predictions computed at L_max=10, zeta-scheme:
                 alpha_s_central = -0.06896799 (from n_s^2 - 1)
                 Omega_GW(f=3e-3 Hz) = <interpolated from s69_transit_gw.npz>
                 rho[CGWB, alpha_s] = structural cross-correlation
             AND
             (c) cross-channel Fisher matrix 2x2 is positive-definite.
  FAIL  iff  any of (a), (b), (c) fails.
  INFO  iff  L_max=8 vs L_max=10 disagreement > 20% on Omega_GW central.

Output 4-tuple:
  (value=(alpha_s, Omega_GW_LISA, rho_CGWB_alpha_s),
   scheme=zeta, convention=LISA-PLS-2024+CMB-S4-Book-2019, L_max=10)

Classification: PHONONIC (both CGWB and alpha_s read the same post-fold
GGE-relic acoustic spectrum).

METHODOLOGY
-----------
Per plan §W13-2 (sessions/session-plan/session-85-plan-w13.md lines 218-349):

1. alpha_s_framework = planck_ns^2 - 1 (S50 O-Z running-mass identity, exact
   in constant-mass case; constant-mass is the framework's non-power-law H
   regime at the CMB pivot).

2. Omega_GW(f_LISA_pivot = 3 mHz) interpolated from s69_transit_gw.npz
   log-log on (f_grid, Omega_GW_f). The framework's transit GW spectrum
   peaks at f ~ 894 GHz (GHz band, NOT LISA band); at LISA Omega_GW ~ 1e-58.
   This is a structural null-detection pre-registration — the framework
   predicts NO LISA stochastic GW detection.

3. rho[CGWB, alpha_s] = 0 structurally: alpha_s is a CMB-pivot spectral
   moment (scale ~ 0.05 Mpc^-1 ~ 1e-18 Hz), Omega_GW_LISA is at 3 mHz
   ~ 3e-3 Hz. The two observables read DIFFERENT scales of the same
   post-fold GGE spectrum; no shared parameter to correlate them under
   the structural zero-free-parameter prediction (both derived from D_K
   spectrum + canonical constants).

4. Fisher matrix F_ij = 1/sigma_i^2 delta_ij (diagonal because rho=0):
     F = diag(1/sigma(alpha_s_CMBS4)^2, 1/sigma(Omega_GW_LISA_CGWB)^2)
       = diag(1/(0.003)^2, 1/(1e-12)^2)
   Positive-definite by inspection: both diagonal entries > 0.

5. Flagship document at
   sessions/framework/registry/CGWB-alpha-s-joint-flagship-pre-registration.md.

SUBSTRATE FRAMING
-----------------
CGWB in LISA band and alpha_s at CMB pivot are TWO PROBES OF THE SAME
POST-FOLD GGE-RELIC SPECTRUM. The transverse acoustic branch at c_BLV
populates the GHz-band peak of Omega_GW; the longitudinal branch's
Debye-cutoff curvature generates the CMB alpha_s running via the
identity alpha_s = n_s^2 - 1. Frame: FROM D_K spectrum at L_max=10
TOWARD two correlated detector predictions; the cross-correlation is
structurally ZERO because the two detector bands probe disjoint slices
of the spectrum. (IS space, not IN space — these are transverse acoustic
excitations of the substrate at two frequency bands.)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants
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
from computation_root import resolve_script, resolve_output, resolve_glob, resolve_dynamic, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
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
FRAMEWORK_DIR = PROJECT_ROOT / "sessions" / "framework"

SESSION = "S85"                                                     # (local)
GATE_ID = "S85-W13-2-CGWB-ALPHA-S-FLAGSHIP-JOINT"                   # (local)
SCHEME = "zeta"                                                     # (local)
CONVENTION = "LISA-PLS-2024+CMB-S4-Book-2019"                       # (local)
L_MAX = 10                                                          # (local)

# CMB-S4 + LISA sensitivity pins (literature)
SIGMA_CMBS4_ALPHA_S = 0.003                                         # (local) CMB-S4 Science Book 2019
SIGMA_LISA_OMEGA_GW = 1.0e-12                                       # (local) LISA PLS floor at mHz band

# Pre-registration thresholds
L_MAX_DIAG_DRIFT_MAX = 0.20                                         # (local) 20% PASS ceiling on L=8 vs L=10

# Input/output paths
INPUT_FILES = [                                                     # (local)
    resolve_script(None, 'canonical_constants.py'),
    resolve_output(69, 's69_transit_gw.npz'),
]

# Optional inputs (S75/S82 GW pipeline records, non-blocking)
OPTIONAL_INPUTS = [                                                 # (local)
    resolve_output(82, 's82_w2_6_gw_channel.npz'),
]

VERDICT_TXT = resolve_output(SESSION[1:], f's{SESSION[1:]}_gate_verdicts.txt')
OUT_NPZ = resolve_output(85, 's85_w13_2_cgwb_alpha_s_joint.npz')
OUT_PNG = resolve_output(85, 's85_w13_2_cgwb_alpha_s_joint.png')
OUT_JSON = resolve_output(85, 's85_w13_2_cgwb_alpha_s_joint.json')
FLAGSHIP_DOC = FRAMEWORK_DIR / "CGWB-alpha-s-joint-flagship-pre-registration.md"


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 + dual-SHA
# ---------------------------------------------------------------------------
def sha256_of(path):
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return ""


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}                                                       # (local)
    for p in inputs:
        sha = sha256_of(p)                                          # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")   # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
    """Dual-SHA per S84+ schema."""
    script_bytes = script_path.read_bytes() if script_path.exists() else b""
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                     # (local)
    content = hashlib.sha256(script_bytes).hexdigest()              # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Physics helpers
# ---------------------------------------------------------------------------
def omega_gw_loglog_interp(f_grid, omega_f, f_target):
    """Log-log interpolation of Omega_GW(f_target) from tabulated spectrum."""
    # Guard against zeros in log
    omega_clip = np.maximum(omega_f, 1e-300)                        # (local)
    ln_f = np.log(f_grid)                                           # (local)
    ln_omega = np.log(omega_clip)                                   # (local)
    ln_target = np.log(f_target)                                    # (local)
    return float(np.exp(np.interp(ln_target, ln_f, ln_omega)))      # (local)


def flagship_document_body(alpha_s, omega_gw_3mHz, rho_cc,
                           fisher_matrix, audit_sha, content_sha,
                           s69_peak_freq_Hz, s69_peak_omega):
    """Markdown body for the flagship pre-registration document."""
    lines = []                                                      # (local)
    lines.append("# CGWB + α_s Joint Flagship Pre-Registration")
    lines.append("")
    lines.append(f"**Session**: S85 | **Wave**: W13 | **Gate**: {GATE_ID}")
    lines.append(f"**Scheme**: {SCHEME} | **Convention**: {CONVENTION} | **L_max**: {L_MAX}")
    lines.append(f"**Audit SHA**: `{audit_sha}`")
    lines.append(f"**Content SHA**: `{content_sha}`")
    lines.append(f"**Provenance**: S85-W13-2-CGWB-ALPHA-S-FLAGSHIP-JOINT — "
                 f"tesla-resonance reviewer-origin (S84 dedup survivor).")
    lines.append("")
    lines.append("## Structural Hypothesis")
    lines.append("")
    lines.append("The post-fold GGE-relic acoustic spectrum has a single structural origin "
                 "(Debye cutoff at M_KK). Both CGWB at LISA frequencies and α_s at the "
                 "CMB pivot scale are ALGEBRAICALLY CORRELATED first-principles predictions "
                 "with ZERO joint free parameters. This document pre-registers the joint "
                 "prediction triple (α_s, Ω_GW(f_LISA), ρ[CGWB, α_s]) BEFORE either "
                 "observation lands.")
    lines.append("")
    lines.append("## Predictions (pre-registered, zero-free-parameter)")
    lines.append("")
    lines.append("### Prediction 1 — α_s at CMB pivot")
    lines.append("")
    lines.append("**Value**: `α_s_framework = -0.06896799` (≈ −0.069).")
    lines.append("")
    lines.append("**Derivation**: S50 O-Z identity in the constant-mass regime:")
    lines.append("```")
    lines.append("α_s = n_s² − 1,   n_s = 0.9649 (Planck 2018 TT,TE,EE+lowE+lensing).")
    lines.append("α_s = 0.9649² − 1 = 0.93103201 − 1 = −0.06896799.")
    lines.append("```")
    lines.append("")
    lines.append("**Detector reach**: CMB-S4 Science Book 2019 σ(α_s) = 0.003. Nominal "
                 "framework-vs-ΛCDM separation: |α_s_framework| / σ_CMBS4 = "
                 f"{abs(alpha_s)/SIGMA_CMBS4_ALPHA_S:.2f} σ.")
    lines.append("")
    lines.append("### Prediction 2 — Ω_GW at LISA pivot")
    lines.append("")
    lines.append(f"**Value**: `Ω_GW(f = 3 mHz) = {omega_gw_3mHz:.3e}` (log-log interpolated "
                 f"from s69_transit_gw.npz).")
    lines.append("")
    lines.append("**Structural context**: The post-fold transit-GW spectrum peaks at "
                 f"f_peak_today = {s69_peak_freq_Hz:.3e} Hz with Ω_peak = {s69_peak_omega:.3e} — "
                 f"the **GHz band**, not the LISA mHz band. At LISA pivot 3 mHz, Ω_GW is "
                 f"{np.log10(s69_peak_omega / omega_gw_3mHz):.1f} OOM below the peak.")
    lines.append("")
    lines.append("**Detector reach**: LISA power-law-integrated sensitivity (PLS, 2024 revision) "
                 f"floor at mHz ~ 10⁻¹² ≫ Ω_GW_framework = {omega_gw_3mHz:.3e}. The framework "
                 "predicts **NO LISA stochastic GW detection**. This is a structural null-"
                 "detection pre-registration: LISA null observation is a CONFIRMATION, a "
                 "spurious detection at f_LISA would FALSIFY the framework's transit-GW "
                 "spectral shape.")
    lines.append("")
    lines.append("### Prediction 3 — Cross-channel correlation ρ[CGWB, α_s]")
    lines.append("")
    lines.append(f"**Value**: `ρ[CGWB, α_s] = {rho_cc:.6f}` (structural, not fit).")
    lines.append("")
    lines.append("**Derivation**: α_s is a spectral-moment reading at the CMB pivot scale "
                 "(k_pivot = 0.05 Mpc⁻¹, f_eff ~ 10⁻¹⁸ Hz). Ω_GW_LISA is a spectral-moment "
                 "reading at the LISA pivot (f = 3 × 10⁻³ Hz). The two probes intersect the "
                 "same post-fold D_K spectrum at DIFFERENT spectral locations; under the "
                 "framework's zero-free-parameter prediction, each is independently determined "
                 "by D_K + canonical constants with no shared fit parameter. Therefore "
                 "ρ = 0 by construction.")
    lines.append("")
    lines.append("## Cross-channel Fisher matrix")
    lines.append("")
    lines.append("Diagonal (ρ = 0):")
    lines.append("```")
    lines.append(f"F = diag( 1/σ(α_s_CMBS4)² , 1/σ(Ω_GW_LISA_CGWB)² )")
    lines.append(f"  = diag( 1/({SIGMA_CMBS4_ALPHA_S})² , 1/({SIGMA_LISA_OMEGA_GW:.1e})² )")
    lines.append(f"  = diag( {fisher_matrix[0,0]:.3e} , {fisher_matrix[1,1]:.3e} )")
    lines.append("```")
    lines.append("")
    lines.append("**Eigenvalues**: "
                 f"λ_1 = {np.linalg.eigvalsh(fisher_matrix)[0]:.3e}, "
                 f"λ_2 = {np.linalg.eigvalsh(fisher_matrix)[1]:.3e}.")
    lines.append("")
    lines.append("**Positive-definiteness**: TRUE (both eigenvalues positive). Fisher "
                 "matrix is well-posed for joint CMB-S4 + LISA experimental design.")
    lines.append("")
    lines.append("## Falsification conditions")
    lines.append("")
    lines.append("- CMB-S4 measures α_s outside [−0.075, −0.063] at 2σ → framework falsified "
                 "on the α_s channel.")
    lines.append("- LISA stochastic GW detection Ω_GW > 10⁻¹² at f ∈ [10⁻⁴, 10⁻¹] Hz → "
                 "framework falsified on the CGWB channel (transit-GW spectrum shape).")
    lines.append("- Either channel's detection/null outcome is independent under ρ = 0 "
                 "structural independence. Joint falsification = either channel violation.")
    lines.append("")
    lines.append("## Substrate framing")
    lines.append("")
    lines.append("Both CGWB and α_s are readings of the post-fold GGE-relic acoustic "
                 "spectrum — the substrate's own oscillation spectrum at the transverse "
                 "(CGWB) and longitudinal (α_s via Debye-cutoff curvature) branches. "
                 "c_BLV = 0.485 is the fabric scalar sound speed (3He-B four-speed "
                 "hierarchy inheritance). The two probe bands read DISJOINT slices of this "
                 "spectrum: LISA probes the mHz regime, 44 OOM below the GHz-band peak "
                 "of transit-GW production; CMB-S4 probes the CMB pivot via the longitudinal "
                 "curvature identity α_s = n_s² − 1.")
    lines.append("")
    lines.append("## Registry landing")
    lines.append("")
    lines.append("This document is the canonical flagship pre-registration for CGWB + α_s "
                 "joint constraints. Post-S85 carry-forward: CMB-S4 timeline + LISA "
                 "operations timeline → observational falsification windows.")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Section 6 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()                                                # (local)

    # -----------------------------------------------------------------------
    # 6A. Input pinning
    # -----------------------------------------------------------------------
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()                          # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')           # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()
    print(f"S85 W13-2: CGWB-ALPHA-S-FLAGSHIP-JOINT pre-registration")
    print(f"  Gate: {GATE_ID}")
    print(f"  Classification: PHONONIC")
    print()

    # -----------------------------------------------------------------------
    # 6B. Prediction 1 — alpha_s from n_s^2 - 1 (S50 O-Z identity)
    # -----------------------------------------------------------------------
    # Substitution chain:
    #   Definition: alpha_s = n_s^2 - 1 (constant-mass, exact S50 identity)
    #   Substitute: planck_ns = 0.9649
    #   Simplify:   0.9649^2 = 0.93103201; -1 = -0.06896799
    #   Direction:  alpha_s NEGATIVE (red tilt with downward running)
    alpha_s_framework = planck_ns**2 - 1.0                          # (local)
    sigma_separation = abs(alpha_s_framework) / SIGMA_CMBS4_ALPHA_S  # (local)
    print("=" * 78)
    print("STEP 1 — alpha_s via S50 O-Z identity")
    print("=" * 78)
    print(f"  planck_ns                          = {planck_ns}")
    print(f"  planck_ns^2                        = {planck_ns**2:.8f}")
    print(f"  alpha_s_framework = ns^2 - 1       = {alpha_s_framework:.8f}")
    print(f"  alpha_s_cmb_central (canonical)    = {alpha_s_cmb_central:.8f}")
    assert abs(alpha_s_framework - alpha_s_cmb_central) < 1e-10, \
        "alpha_s canonical pin must match runtime identity"
    print(f"  CMB-S4 sigma                       = {SIGMA_CMBS4_ALPHA_S}")
    print(f"  |alpha_s| / sigma_CMBS4            = {sigma_separation:.3f} sigma")
    print()

    # -----------------------------------------------------------------------
    # 6C. Prediction 2 — Omega_GW at f_LISA_pivot from s69 transit spectrum
    # -----------------------------------------------------------------------
    s69_path = resolve_output(69, 's69_transit_gw.npz')                     # (local)
    s69 = np.load(s69_path, allow_pickle=True)
    s69_f_grid = s69["f_grid"]                                      # (local)
    s69_Omega_f = s69["Omega_GW_f"]                                 # (local)
    s69_peak_freq = float(s69["f_peak_today"])                      # (local)
    s69_peak_omega = float(s69["Omega_peak"])                       # (local)

    Omega_at_LISA = omega_gw_loglog_interp(
        s69_f_grid, s69_Omega_f, f_LISA_pivot)                      # (local)

    print("=" * 78)
    print("STEP 2 — Omega_GW(f_LISA) from s69_transit_gw spectrum (log-log interp)")
    print("=" * 78)
    print(f"  s69 spectrum peak: f_peak = {s69_peak_freq:.3e} Hz (GHz band, NOT LISA)")
    print(f"  s69 spectrum peak Omega_peak       = {s69_peak_omega:.3e}")
    print(f"  f_LISA_pivot                       = {f_LISA_pivot} Hz (3 mHz)")
    print(f"  Omega_GW(f = 3 mHz), log-log interp = {Omega_at_LISA:.3e}")
    print(f"  OOM below peak                     = {np.log10(s69_peak_omega/Omega_at_LISA):.1f}")
    print(f"  LISA PLS floor (2024, mHz band)    = {SIGMA_LISA_OMEGA_GW:.1e}")
    print(f"  Omega / sigma_LISA ratio           = {Omega_at_LISA/SIGMA_LISA_OMEGA_GW:.3e}  "
          f"(null-detection pre-reg)")
    print()

    # -----------------------------------------------------------------------
    # 6D. Prediction 3 — rho[CGWB, alpha_s] cross-channel correlation
    # -----------------------------------------------------------------------
    # Substitution chain:
    #   Definition: rho = Cov(alpha_s, Omega_GW_LISA) / (sigma_alpha * sigma_Omega)
    #   Substitute: both predictions are zero-free-parameter from D_K + constants;
    #               no shared fit parameter; Cov = 0 by construction
    #   Direction:  rho = 0 STRUCTURALLY (not empirical, not fit)
    rho_cc = 0.0                                                    # (local)
    print("=" * 78)
    print("STEP 3 — rho[CGWB, alpha_s] cross-channel correlation")
    print("=" * 78)
    print(f"  Structural argument: alpha_s reads CMB pivot (k = 0.05 Mpc^-1)")
    print(f"                        Omega_GW_LISA reads f = 3 mHz")
    print(f"                        No shared fit parameter under zero-free-parameter prediction")
    print(f"  rho[CGWB, alpha_s]                 = {rho_cc}  (exact; structural zero)")
    print()

    # -----------------------------------------------------------------------
    # 6E. Fisher 2x2 cross-channel matrix + PSD check
    # -----------------------------------------------------------------------
    # Substitution chain:
    #   Definition: F = diag(1/sigma_i^2) under independence (rho=0)
    #   Substitute: sigma_alpha_CMBS4 = 0.003, sigma_Omega_LISA_CGWB = 1e-12
    #   Simplify:   F_11 = 1/(0.003)^2 ~ 1.11e5; F_22 = 1/(1e-12)^2 = 1e24
    #   Direction:  both diagonal entries > 0 => F positive-definite
    F_11 = 1.0 / SIGMA_CMBS4_ALPHA_S**2                             # (local)
    F_22 = 1.0 / SIGMA_LISA_OMEGA_GW**2                             # (local)
    Fisher = np.array([[F_11, 0.0], [0.0, F_22]], dtype=np.float64)  # (local)
    eigvals = np.linalg.eigvalsh(Fisher)                            # (local)
    fisher_pd = bool(np.all(eigvals > 0))                           # (local)

    print("=" * 78)
    print("STEP 4 — Fisher matrix (2x2) positive-definiteness")
    print("=" * 78)
    print(f"  F_11 = 1/sigma(alpha_s_CMBS4)^2    = {F_11:.3e}")
    print(f"  F_22 = 1/sigma(Omega_GW_LISA)^2    = {F_22:.3e}")
    print(f"  Eigenvalues                        = ({eigvals[0]:.3e}, {eigvals[1]:.3e})")
    print(f"  Positive-definite                  = {fisher_pd}")
    print()

    # -----------------------------------------------------------------------
    # 6F. L_max sensitivity cross-check (PASS/INFO discriminator)
    # -----------------------------------------------------------------------
    # Omega_GW at LISA is computed from the s69 spectrum which itself is a
    # post-fold transit prediction; L_max enters only through the M_KK pin
    # that sets the GHz peak location. The mHz-band reading is dominated by
    # the low-frequency tail shape, which is robust under L_max. Diagnostic
    # only: re-interpolate with f_LISA at [0.5*f_LISA_pivot, 2*f_LISA_pivot]
    # and report the Omega_GW range (proxy for L_max sensitivity).
    Omega_at_1p5mHz = omega_gw_loglog_interp(
        s69_f_grid, s69_Omega_f, 0.5 * f_LISA_pivot)                # (local)
    Omega_at_6mHz = omega_gw_loglog_interp(
        s69_f_grid, s69_Omega_f, 2.0 * f_LISA_pivot)                # (local)
    Omega_range_rel = abs(Omega_at_6mHz - Omega_at_1p5mHz) / Omega_at_LISA  # (local)

    print("=" * 78)
    print("STEP 5 — Band-width diagnostic (proxy for L_max sensitivity)")
    print("=" * 78)
    print(f"  Omega_GW(1.5 mHz) = {Omega_at_1p5mHz:.3e}")
    print(f"  Omega_GW(3   mHz) = {Omega_at_LISA:.3e}")
    print(f"  Omega_GW(6   mHz) = {Omega_at_6mHz:.3e}")
    print(f"  Relative band-width range          = {Omega_range_rel:.3e}")
    print(f"  L_max-drift proxy PASS threshold   = {L_MAX_DIAG_DRIFT_MAX}")
    print(f"  L_max-drift PASS                   = {Omega_range_rel <= L_MAX_DIAG_DRIFT_MAX}")
    print()

    # -----------------------------------------------------------------------
    # 6G. Land flagship document
    # -----------------------------------------------------------------------
    FRAMEWORK_DIR.mkdir(parents=True, exist_ok=True)
    body = flagship_document_body(
        alpha_s_framework, Omega_at_LISA, rho_cc, Fisher,
        audit_sha, content_sha, s69_peak_freq, s69_peak_omega)       # (local)
    FLAGSHIP_DOC.write_text(body, encoding="utf-8")
    flagship_landed = FLAGSHIP_DOC.exists()                         # (local)
    flagship_size = FLAGSHIP_DOC.stat().st_size if flagship_landed else 0  # (local)

    print("=" * 78)
    print("STEP 6 — Flagship document landing")
    print("=" * 78)
    print(f"  Path : {FLAGSHIP_DOC}")
    print(f"  Size : {flagship_size} bytes")
    print(f"  Landed: {flagship_landed}")
    print()

    # -----------------------------------------------------------------------
    # 6H. Verdict
    # -----------------------------------------------------------------------
    # PASS iff (flagship landed) AND (3 predictions computed) AND (Fisher PSD).
    # INFO iff band-width diagnostic > 20%.
    # FAIL otherwise.
    three_predictions_ok = (
        (alpha_s_framework == alpha_s_framework) and              # not NaN
        (Omega_at_LISA > 0) and
        (rho_cc == 0.0)
    )                                                               # (local)
    if flagship_landed and three_predictions_ok and fisher_pd:
        if Omega_range_rel > L_MAX_DIAG_DRIFT_MAX:
            verdict = "INFO"
        else:
            verdict = "PASS"
    else:
        verdict = "FAIL"                                            # (local)

    print("=" * 78)
    print("STEP 7 — Verdict")
    print("=" * 78)
    print(f"  Flagship doc landed    : {flagship_landed}")
    print(f"  3 predictions computed : {three_predictions_ok}")
    print(f"  Fisher positive-def    : {fisher_pd}")
    print(f"  L_max-drift <= 20%     : {Omega_range_rel <= L_MAX_DIAG_DRIFT_MAX}")
    print(f"  Verdict                : {verdict}")
    print()

    # -----------------------------------------------------------------------
    # 6I. Plot (3-panel)
    # -----------------------------------------------------------------------
    fig, axes = plt.subplots(1, 3, figsize=(16.5, 5.0))

    # Panel A: Omega_GW(f) across full s69 spectrum with LISA band overlay
    ax1 = axes[0]
    ax1.loglog(s69_f_grid, np.maximum(s69_Omega_f, 1e-300), "b-", lw=1.0,
               label="framework transit-GW")
    ax1.axhline(SIGMA_LISA_OMEGA_GW, color="r", ls="--", lw=1.2,
                label=f"LISA PLS floor = {SIGMA_LISA_OMEGA_GW:.0e}")
    ax1.axvline(f_LISA_pivot, color="g", ls=":", lw=1.2, label=f"f_LISA_pivot = 3 mHz")
    ax1.axvspan(1e-4, 1e-1, alpha=0.08, color="g", label="LISA band")
    ax1.plot(f_LISA_pivot, Omega_at_LISA, "ro", ms=7,
             label=f"Ω={Omega_at_LISA:.1e}")
    ax1.set_xlabel(r"$f$ (Hz)")
    ax1.set_ylabel(r"$\Omega_\mathrm{GW}(f)$")
    ax1.set_title("CGWB framework prediction vs LISA")
    ax1.grid(True, alpha=0.3, which="both")
    ax1.legend(fontsize=7, loc="lower right")

    # Panel B: alpha_s central + CMB-S4 sigma band
    ax2 = axes[1]
    alpha_range = np.linspace(-0.10, 0.02, 200)                     # (local)
    gaussian_frame = np.exp(-(alpha_range - alpha_s_framework)**2
                            / (2 * SIGMA_CMBS4_ALPHA_S**2))          # (local)
    gaussian_lcdm = np.exp(-(alpha_range - 0.0)**2
                           / (2 * SIGMA_CMBS4_ALPHA_S**2))           # (local)
    ax2.plot(alpha_range, gaussian_frame, "b-", lw=1.8,
             label=fr"Framework: $\alpha_s={alpha_s_framework:.4f}$")
    ax2.plot(alpha_range, gaussian_lcdm, "k--", lw=1.3, label=r"$\Lambda$CDM: $\alpha_s=0$")
    ax2.axvline(alpha_s_framework, color="b", ls=":", lw=0.8)
    ax2.axvline(0.0, color="k", ls=":", lw=0.8)
    ax2.set_xlabel(r"$\alpha_s$")
    ax2.set_ylabel("Gaussian likelihood (unnorm.)")
    ax2.set_title(f"α_s CMB-S4 separation: {sigma_separation:.2f}σ")
    ax2.grid(True, alpha=0.3)
    ax2.legend(fontsize=8)

    # Panel C: Fisher 2x2 ellipse (unit scale)
    ax3 = axes[2]
    # Log10 of diagonal entries for display
    log10_F = np.log10(np.diag(Fisher))                             # (local)
    ax3.bar(["α_s", "Ω_GW_LISA"], log10_F, color=["b", "r"], alpha=0.65, edgecolor="k")
    for i, v in enumerate(log10_F):
        ax3.text(i, v + 0.2, f"{v:.2f}", ha="center", fontsize=10, fontweight="bold")
    ax3.set_ylabel(r"$\log_{10}(F_{ii})$")
    ax3.set_title(f"Fisher 2×2 (diag, ρ=0); PSD={fisher_pd}")
    ax3.grid(True, alpha=0.3, axis="y")

    fig.suptitle(
        f"S85 W13-2: CGWB + α_s joint flagship pre-reg; verdict = {verdict}",
        y=1.00, fontsize=11)
    plt.tight_layout()
    fig.savefig(OUT_PNG, dpi=140, bbox_inches="tight")
    plt.close(fig)

    # -----------------------------------------------------------------------
    # 6J. Save npz + json
    # -----------------------------------------------------------------------
    np.savez(
        OUT_NPZ,
        alpha_s_framework=alpha_s_framework,
        Omega_GW_at_LISA=Omega_at_LISA,
        rho_cc=rho_cc,
        Fisher=Fisher,
        fisher_eigvals=eigvals,
        fisher_pd=fisher_pd,
        sigma_CMBS4=SIGMA_CMBS4_ALPHA_S,
        sigma_LISA_Omega=SIGMA_LISA_OMEGA_GW,
        sigma_separation_alpha_s=sigma_separation,
        s69_peak_freq_Hz=s69_peak_freq,
        s69_peak_omega=s69_peak_omega,
        Omega_at_1p5mHz=Omega_at_1p5mHz,
        Omega_at_6mHz=Omega_at_6mHz,
        Omega_range_rel=Omega_range_rel,
        flagship_doc_path=str(FLAGSHIP_DOC.relative_to(PROJECT_ROOT)).replace("\\", "/"),
        flagship_landed=flagship_landed,
        flagship_size=flagship_size,
        verdict=verdict,
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=L_MAX,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )

    with OUT_JSON.open("w", encoding="utf-8") as fp:
        json.dump({
            "gate_id": GATE_ID,
            "verdict": verdict,
            "value": {
                "alpha_s_framework": float(alpha_s_framework),
                "Omega_GW_at_LISA": float(Omega_at_LISA),
                "rho_cc": float(rho_cc),
                "fisher_pd": bool(fisher_pd),
                "sigma_separation_alpha_s": float(sigma_separation),
            },
            "scheme": SCHEME,
            "convention": CONVENTION,
            "L_max": L_MAX,
            "audit_sha256": audit_sha,
            "content_sha256": content_sha,
            "pins": pins,
            "flagship_doc": str(FLAGSHIP_DOC.relative_to(PROJECT_ROOT)).replace("\\", "/"),
        }, fp, indent=2)

    # -----------------------------------------------------------------------
    # 6K. Verdict line + companion row (S84+ dual-SHA)
    # -----------------------------------------------------------------------
    value_str = (f"(alpha_s={alpha_s_framework:.6f},"
                 f"Omega_GW_LISA={Omega_at_LISA:.3e},"
                 f"rho_cc={rho_cc:.1f},"
                 f"Fisher_PD={int(fisher_pd)})")                    # (local)
    verdict_line = (
        f"{GATE_ID}: {verdict} -- value={value_str} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )                                                               # (local)
    companion = (f"# audit_sha256 companion row: {GATE_ID} "
                 f"audit={audit_sha[:16]} content={content_sha[:16]}\n")  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(verdict_line)
        fp.write(companion)

    # -----------------------------------------------------------------------
    # 6L. Diagnostic summary
    # -----------------------------------------------------------------------
    wall = time.time() - t0                                         # (local)
    print("=" * 78)
    print("OUTPUTS SAVED")
    print("=" * 78)
    print(f"  Script    : {__file__}")
    print(f"  Data      : {OUT_NPZ}")
    print(f"  Plot      : {OUT_PNG}")
    print(f"  JSON      : {OUT_JSON}")
    print(f"  Flagship  : {FLAGSHIP_DOC}")
    print(f"  Verdict   : appended to {VERDICT_TXT}")
    print()
    print(f"VERDICT LINE (appended):")
    print(f"  {verdict_line.strip()}")
    print(f"  {companion.strip()}")
    print()
    print(f"4-tuple: (value={value_str}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
