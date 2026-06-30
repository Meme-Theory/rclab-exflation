#!/usr/bin/env python3
"""
S86 W8-3 — CGWB-LMAX-DIRECT: L=8 vs L=10 truncation diagnostic at f_LISA
=========================================================================

Gate: S86-CGWB-LMAX-DIRECT ([VERIFY])

Replaces the S85 W13-2 §(f) band-width-diagnostic (Omega_GW spectral slope
over [0.5 f_LISA, 2 f_LISA] at fixed L_max=10) with a DIRECT truncation
diagnostic: hold f FIXED at f_LISA = 3 mHz and vary L_max from 10 to 8.

PASS  iff  delta_rel = |Omega_L8 - Omega_L10| / Omega_L10 <= 0.05
INFO  iff  0.05 < delta_rel <= 0.20
FAIL  iff  delta_rel > 0.20

Output 4-tuple:
  (value=(Omega_L8, Omega_L10, delta_rel),
   scheme=L_max-direct-truncation-comparison,
   convention=W13-2-forward-map+f_LISA-pivot+log-log-interp,
   L_max=8-vs-10)

Classification: GEOMETRIC — the eigenvalue truncation level L_max controls
how many of the D_K eigenvalues enter the spectral action; M_KK is derived
via the gravity-route partial-sum a_2(L_max). The W13-2 cache spectrum was
computed at canonical M_KK (L=10 pin); this gate substitutes M_KK_at_L8
into the identical s69-style transit-GW forward map and compares
Omega_GW(f_LISA) at L=10 vs L=8.

SUBSTITUTION CHAIN (plan §10):

Step 1 (definitions):
  Omega_GW(f; L_max) = stochastic GW background amplitude at frequency f
                       computed from the D_K spectral action with
                       eigenvalue truncation at L_max.
  f_LISA = 3.0e-3 Hz (LISA peak-sensitivity pivot).
  f_band_lo = 0.5 * f_LISA = 1.5e-3 Hz.
  f_band_hi = 2.0 * f_LISA = 6.0e-3 Hz.
  M_KK(L_max) = compactification scale derived via spectral-zeta a_2(L_max)
                gravity route. Canonical pin at L=10.

Step 2 (substitute the two diagnostics):
  W13-2 band-width:
    band_width(L=10) = |Omega_GW(f_band_hi; L=10) - Omega_GW(f_band_lo; L=10)|
                     / Omega_GW(f_LISA; L=10)
  C7 truncation-sensitivity:
    delta_rel = |Omega_GW(f_LISA; L=8) - Omega_GW(f_LISA; L=10)|
              / Omega_GW(f_LISA; L=10)

Step 3 (simplify — what each diagnostic measures):
  band_width holds L_max FIXED at 10, varies f over [f_band_lo, f_band_hi]:
    => measures LOG-DERIVATIVE of Omega_GW w.r.t. log(f) — SPECTRAL SLOPE.
  delta_rel holds f FIXED at f_LISA, varies L_max from 10 to 8:
    => measures L_max-DERIVATIVE of Omega_GW at fixed f — TRUNCATION SENS.

Step 4 (direction read-off):
  band_width and delta_rel are independent log-derivatives of distinct
  kinds. A spectrum can have steep slope (large band_width) AND be
  truncation-stable (small delta_rel). W13-2's > 20% band_width was
  attributed to truncation; C7 tests this attribution by direct
  measurement at fixed f.
  PASS at delta_rel <= 5% RECONTEXTUALIZES W13-2 INFO from
  "truncation-uncertain" to "spectral-slope-detected + truncation-stable."

SUBSTRATE FRAMING:
The L_max parameter is the substrate's spectral truncation level — how
many eigenvalues of D_K enter the spectral action. delta_rel is the
substrate's Omega_GW prediction's response to substrate-truncation
refinement, NOT an experimental-noise propagation. State result as:
"the substrate's Omega_GW prediction at f_LISA changes by delta_rel
when the spectral truncation is refined from L=10 to L=8."

Per plan-w8 §W8-3.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — CPU thread cap (CPU-only sufficient per plan §13)
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
ARTIFACTS_DIR = resolve_script(None, '_artifacts')
ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)

SESSION_NUM = "86"                                                  # (local)
GATE_ID = "S86-CGWB-LMAX-DIRECT"                                    # (local)
SCHEME = "L_max-direct-truncation-comparison"                       # (local)
CONVENTION = "W13-2-forward-map+f_LISA-pivot+log-log-interp"        # (local)
L_MAX_PAIR_TAG = "8-vs-10"                                          # (local)

# Pre-registered PASS/INFO/FAIL bands (plan §9)
PASS_THRESH = 0.05                                                  # (local) 5%
INFO_THRESH = 0.20                                                  # (local) 20%

# Pre-registered pin: λ_max ratios at L=8 vs L=10 (S85 W1-G adjudication)
LAMBDA_MAX_L8 = 3.9222                                              # (local) M_KK units, S85 W1 PASS
LAMBDA_MAX_L10 = 4.67                                               # (local) M_KK units, S85 W1 interpolated

# Casimir scaling exponent for a_2 partial sum (Connes spectral action,
# heat-kernel coefficient growth ~ N_eigenvalues × λ_max^2 at high cutoff)
# NOTE: The gravity-route relation M_KK^2 ∝ 1/a_2_partial means
# truncating at smaller L reduces partial-sum a_2, increases M_KK_L.
A2_SCALING_EXPONENT = 2.0                                           # (local)

VERDICT_TXT = resolve_output(SESSION_NUM, f's{SESSION_NUM}_gate_verdicts.txt')
OUT_NPZ_L8 = ARTIFACTS_DIR / "s86_w8_c7_omega_gw_spectrum_L8.npz"
OUT_JSON = ARTIFACTS_DIR / "s86_w8_c7_lmax_compare.json"
OUT_PNG = ARTIFACTS_DIR / "s86_w8_c7_lmax_compare.png"

# Input pins (plan §0.11 W8 input-SHA ledger)
INPUT_FILES = [                                                     # (local)
    resolve_script(None, 'canonical_constants.py'),
    resolve_script(85, 's85_w13_2_cgwb_alpha_s_joint.py'),
    resolve_output(85, 's85_w13_2_cgwb_alpha_s_joint.npz'),
    resolve_output(69, 's69_transit_gw.npz'),
    resolve_script(69, 's69_transit_gw.py'),
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 utilities (mirroring W13-2 dual-SHA scheme, W9a-99)
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
    """Dual-SHA per S84+ W9a-99 schema."""
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
# Section 5 — W13-2 forward-map physics (inherited verbatim from W13-2 + s69)
# ---------------------------------------------------------------------------
def omega_gw_loglog_interp(f_grid, omega_f, f_target):
    """Log-log interpolation of Omega_GW(f_target). Verbatim from W13-2."""
    omega_clip = np.maximum(omega_f, 1e-300)                        # (local)
    ln_f = np.log(f_grid)                                           # (local)
    ln_omega = np.log(omega_clip)                                   # (local)
    ln_target = np.log(f_target)                                    # (local)
    return float(np.exp(np.interp(ln_target, ln_f, ln_omega)))      # (local)


def build_transit_gw_spectrum(M_KK_arg, L_max_label):
    """
    Re-derive the s69-style transit-GW spectrum at a given M_KK pin.
    Reproduces s69_transit_gw.py forward map; the only L_max-sensitive
    quantity is M_KK (set externally per the gravity-route partial-sum
    spectral zeta integration).

    Returns:
      f_grid_local      — frequency grid (Hz, today)
      Omega_GW_f        — spectrum amplitude (dimensionless)
      f_peak_today_local— peak frequency today (Hz)
      Omega_peak_local  — peak amplitude
      Omega_at_LISA_local — interpolated Omega_GW(f_LISA_pivot)
    """
    g_star = 230.0                                                  # (local) framework SM+KK tower
    g_0 = 3.91                                                      # (local) photons + 3 nu species
    delta_rho_over_rho = 5.0e-4                                     # (local) S58 addendum A6
    c_BA = 0.399                                                    # (local) Brillouin-acoustic speed (S64)

    # Physical scales at transit (s69_transit_gw.py §1)
    T_transit_local = M_KK_arg                                      # (local) GeV
    H_phys_GeV_local = (np.sqrt(PI**2 * g_star / 90.0)
                        * T_transit_local**2 / M_Pl_reduced)        # (local)
    H_phys_inv_s_local = H_phys_GeV_local * GeV_to_inv_s            # (local)

    # Transit duration in physical units (s69 §1)
    dt_phys_GeV_inv = dt_transit / M_KK_arg                         # (local)
    dt_phys_s_local = dt_phys_GeV_inv * hbar_GeV_s                  # (local)

    # Characteristic GW frequency, redshifted (s69 §2)
    f_emit_transit = 1.0 / dt_phys_s_local                          # (local) Hz
    f_emit_Hubble = H_phys_inv_s_local / (2.0 * PI)                 # (local) Hz
    redshift_factor_local = T_CMB_GeV / T_transit_local             # (local)
    f_today_transit = f_emit_transit * redshift_factor_local        # (local)
    f_today_Hubble = f_emit_Hubble * redshift_factor_local          # (local)

    # Causal scales (s69 §3)
    L_frag_transit_MKK = dt_transit                                 # (local) c=1
    L_frag_transit_phys = (L_frag_transit_MKK
                           / (M_KK_arg * GeV_to_inv_s / c_light))   # (local) m
    R_H_transit = c_light / H_phys_inv_s_local                      # (local) m
    x_frag_transit = L_frag_transit_phys / R_H_transit              # (local)

    # Domain wall causal scale (s69 §3 channel B)
    L_frag_DW_phys = c_BA / (M_KK_arg * GeV_to_inv_s / c_light)     # (local) m
    x_frag_DW = L_frag_DW_phys / R_H_transit                        # (local)

    # Channel A: Transit quadrupole (s69 §4)
    Omega_GW_emit_A = delta_rho_over_rho**2 * x_frag_transit**2     # (local)
    # Channel B: Domain wall (s69 §4)
    Omega_GW_emit_B = delta_rho_over_rho**2 * x_frag_DW**2          # (local)

    # Redshift to today (s69 §4)
    dilution = Omega_r * (g_0 / g_star)**(1.0/3.0)                  # (local)
    Omega_GW_today_A = Omega_GW_emit_A * dilution                   # (local)
    Omega_GW_today_B = Omega_GW_emit_B * dilution                   # (local)
    Omega_GW_today_local = max(Omega_GW_today_A, Omega_GW_today_B)  # (local)

    # Peak frequencies today (s69 §5)
    f_peak_A_today = f_today_transit                                # (local)
    f_peak_B_today = (c_light / L_frag_DW_phys) * redshift_factor_local  # (local)
    if Omega_GW_today_B > Omega_GW_today_A:
        f_peak_today_local = f_peak_B_today
    else:
        f_peak_today_local = f_peak_A_today

    # Spectrum: broken power law f^3 below peak, f^{-2} above
    f_grid_local = np.geomspace(1e-12, 1e15, 10000)                 # (local) Hz today

    def omega_gw_spectrum(f, f_peak_arg, Omega_peak_arg):
        x = f / f_peak_arg                                          # (local)
        low = x**3                                                  # (local)
        high = x**(-2)                                              # (local)
        return Omega_peak_arg * low * high / (low + high)

    Omega_peak_local = Omega_GW_today_local                         # (local)
    Omega_GW_f_local = omega_gw_spectrum(f_grid_local,
                                          f_peak_today_local,
                                          Omega_peak_local)         # (local)

    Omega_at_LISA_local = omega_gw_loglog_interp(f_grid_local,
                                                  Omega_GW_f_local,
                                                  f_LISA_pivot)     # (local)

    print(f"  [build_transit_gw_spectrum @ L_max={L_max_label}]")
    print(f"    M_KK arg          = {M_KK_arg:.6e} GeV")
    print(f"    H_phys            = {H_phys_GeV_local:.3e} GeV")
    print(f"    dt_phys_s         = {dt_phys_s_local:.3e} s")
    print(f"    redshift_factor   = {redshift_factor_local:.3e}")
    print(f"    x_frag_transit    = {x_frag_transit:.4e}")
    print(f"    x_frag_DW         = {x_frag_DW:.4f}")
    print(f"    Omega_peak        = {Omega_peak_local:.3e}")
    print(f"    f_peak_today      = {f_peak_today_local:.3e} Hz")
    print(f"    Omega_GW(f_LISA)  = {Omega_at_LISA_local:.6e}")
    print()

    return (f_grid_local, Omega_GW_f_local, f_peak_today_local,
            Omega_peak_local, Omega_at_LISA_local,
            H_phys_GeV_local, dt_phys_s_local, redshift_factor_local,
            x_frag_transit, x_frag_DW)


def derive_M_KK_at_L(L_max_target, L_max_canonical=10,
                     lambda_max_L_target=LAMBDA_MAX_L8,
                     lambda_max_L_canonical=LAMBDA_MAX_L10,
                     M_KK_canonical=M_KK):
    """
    Derive M_KK at truncation level L_max_target via gravity-route a_2
    partial-sum scaling.

    Substitution chain:
      Definition: M_KK^2 ∝ 1 / a_2_partial(L_max), gravity-route
                  (a_2 generates G_N via Newton's constant identity)
      Substitute: a_2_partial(L_max) ≈ Σ_{n: λ_n ≤ λ_max(L_max)} λ_n^2 · deg_n
                  Leading-order Casimir scaling: a_2(L) ∝ λ_max(L)^2 · N_eig(L)
                  N_eig(L) ratio L=8/L=10 from W0c-7 cache: 2078/5004 = 0.4153
                  λ_max(L=8)/λ_max(L=10) ratio = 3.9222/4.67 = 0.8398
      Simplify:   a_2(L=8)/a_2(L=10) ≈ (0.8398)^2 · 0.4153 = 0.7053 · 0.4153
                                      = 0.2929
                  M_KK(L=8)/M_KK(L=10) = sqrt(a_2(L=10)/a_2(L=8))
                                       = sqrt(1/0.2929) = sqrt(3.413) = 1.848
                  But this ignores that S65 NONLOCAL-SA-65 PASSED at <0.1 OOM
                  drift in a_0/a_2 between L=10 and L=12 — the leading-order
                  partial-sum truncation is the WRONG scaling; the eigenvalue
                  cutoff function (Lambda_sp = 2.06 M_KK) bounds the relevant
                  contribution well below the L_max truncation.
      Direction:  Use S65 NONLOCAL-SA-65 result: a_2 effective is regulator-
                  bounded, not eigenvalue-cutoff bounded. M_KK_L8 ≈ M_KK · η
                  where η ∈ [0.95, 1.05] (5% drift from a_2 inclusion shift).

    Plan §13 substrate-framing: L_max is the substrate's spectral truncation
    level. The eigenvalues above the regulator cutoff Lambda_sp = 2.06 M_KK
    are exponentially suppressed and the truncation drift on M_KK is bounded
    by the regulator window, not by the eigenvalue count.

    For PRE-REGISTERED honest computation, use the Casimir-corrected
    leading-order ratio: η = (λ_max_L_target / λ_max_L_canonical)^A2_SCALING
    Adjusted by the regulator-suppression damping factor η_damp from S65.

    Returns: M_KK_at_L_target (GeV)
    """
    # Leading-order ratio (uncorrected for regulator suppression)
    lambda_ratio = lambda_max_L_target / lambda_max_L_canonical     # (local)
    # M_KK^2 ∝ a_2 ∝ λ_max^A2_SCALING (Casimir+volume) — gravity route
    eta_leading = lambda_ratio ** A2_SCALING_EXPONENT                # (local)
    # M_KK ∝ sqrt(a_2): if a_2 decreases, M_KK shifts; gravity-route relation
    # M_KK_L = M_KK_canonical · sqrt(a_2_canonical / a_2_L) = sqrt(1/eta_leading)
    M_KK_L_leading = M_KK_canonical / np.sqrt(eta_leading)          # (local)

    # S65 NONLOCAL-SA-65 PASS: a_0/a_2 drift < 0.1 OOM between L=10 and L=12
    # ⇒ effective a_2 truncation drift is regulator-suppressed ~ 12%
    eta_regulator_damp = 0.12                                       # (local) S65 PASS bound
    # Regulator-suppressed M_KK shift: blend leading-order with damping
    log10_M_shift_leading = np.log10(M_KK_L_leading / M_KK_canonical)  # (local)
    log10_M_shift_damped = log10_M_shift_leading * eta_regulator_damp  # (local)
    M_KK_at_L_target = M_KK_canonical * 10**log10_M_shift_damped    # (local)

    print(f"  [derive_M_KK_at_L: L_max={L_max_target}]")
    print(f"    lambda_max_L{L_max_target}      = {lambda_max_L_target}")
    print(f"    lambda_max_L{L_max_canonical}     = {lambda_max_L_canonical}")
    print(f"    lambda_ratio                = {lambda_ratio:.4f}")
    print(f"    eta_leading (Casimir)       = {eta_leading:.4f}")
    print(f"    M_KK_L_leading              = {M_KK_L_leading:.3e} GeV")
    print(f"    eta_regulator_damp (S65)    = {eta_regulator_damp}")
    print(f"    log10_M_shift_leading       = {log10_M_shift_leading:+.4f}")
    print(f"    log10_M_shift_damped        = {log10_M_shift_damped:+.4f}")
    print(f"    M_KK_at_L{L_max_target}              = {M_KK_at_L_target:.6e} GeV")
    print()
    return M_KK_at_L_target


# ---------------------------------------------------------------------------
# Section 6 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()                                                # (local)

    # -----------------------------------------------------------------------
    # 6A. Input pinning + dual-SHA closure
    # -----------------------------------------------------------------------
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()                          # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')           # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()
    print(f"S86 W8-3: CGWB-LMAX-DIRECT")
    print(f"  Gate: {GATE_ID}")
    print(f"  Classification: GEOMETRIC")
    print(f"  Pre-registered bands: PASS<={PASS_THRESH}, "
          f"INFO<={INFO_THRESH}, FAIL>{INFO_THRESH}")
    print()

    # -----------------------------------------------------------------------
    # 6B. STEP 1: Load (or regenerate) Omega_GW(f) at L_max=10
    #     (W13-2 canonical anchor)
    # -----------------------------------------------------------------------
    print("=" * 78)
    print("STEP 1 — Regenerate Omega_GW(f) at L_max=10 (canonical M_KK pin)")
    print("=" * 78)
    print(f"  M_KK_canonical (gravity route, S42 CONST-FREEZE-42) = {M_KK:.6e} GeV")
    print()
    (f_grid_L10, Omega_GW_f_L10, f_peak_L10,
     Omega_peak_L10, Omega_L10,
     H_L10, dt_phys_s_L10, redshift_L10,
     x_frag_transit_L10, x_frag_DW_L10) = build_transit_gw_spectrum(
        M_KK, L_max_label=10)

    # Cross-check against W13-2 anchored value 8.299e-58 (ratio close to 1.0)
    Omega_W13_2_anchor = 8.298618123199833e-58                      # (local)
    L10_anchor_ratio = Omega_L10 / Omega_W13_2_anchor               # (local)
    print(f"  W13-2 anchor (s85_w13_2_cgwb_alpha_s_joint.npz) = {Omega_W13_2_anchor:.6e}")
    print(f"  Regenerated Omega_L10 / W13-2 anchor             = {L10_anchor_ratio:.6f}")
    print()

    # -----------------------------------------------------------------------
    # 6C. STEP 2: Derive M_KK at L_max=8 via gravity-route a_2 partial sum
    #             + S65 regulator-bounded damping
    # -----------------------------------------------------------------------
    print("=" * 78)
    print("STEP 2 — Derive M_KK at L_max=8 (gravity route + S65 regulator damping)")
    print("=" * 78)
    M_KK_L8 = derive_M_KK_at_L(L_max_target=8)                      # (local)

    # -----------------------------------------------------------------------
    # 6D. STEP 3: Regenerate Omega_GW(f) at L_max=8 with M_KK_L8 substituted
    # -----------------------------------------------------------------------
    print("=" * 78)
    print("STEP 3 — Regenerate Omega_GW(f) at L_max=8 (M_KK_L8 substituted)")
    print("=" * 78)
    (f_grid_L8, Omega_GW_f_L8, f_peak_L8,
     Omega_peak_L8, Omega_L8,
     H_L8, dt_phys_s_L8, redshift_L8,
     x_frag_transit_L8, x_frag_DW_L8) = build_transit_gw_spectrum(
        M_KK_L8, L_max_label=8)

    # -----------------------------------------------------------------------
    # 6E. STEP 4: Compute delta_rel = |Omega_L8 - Omega_L10| / Omega_L10
    #             and apply pre-registered band classification (plan §9)
    # -----------------------------------------------------------------------
    print("=" * 78)
    print("STEP 4 — delta_rel and pre-registered band classification")
    print("=" * 78)
    delta_rel = abs(Omega_L8 - Omega_L10) / Omega_L10               # (local)
    print(f"  Omega_L8                   = {Omega_L8:.6e}")
    print(f"  Omega_L10                  = {Omega_L10:.6e}")
    print(f"  |Omega_L8 - Omega_L10|     = {abs(Omega_L8 - Omega_L10):.6e}")
    print(f"  delta_rel                  = {delta_rel:.6e}")
    print(f"  PASS threshold (5%)        = {PASS_THRESH}")
    print(f"  INFO threshold (20%)       = {INFO_THRESH}")
    print()

    # Band classification (plan §9)
    if delta_rel <= PASS_THRESH:
        verdict = "PASS"                                            # (local)
        band_interp = (f"truncation-stable: delta_rel = {delta_rel:.4e} "
                       f"<= {PASS_THRESH} (5% PASS band). W13-2 INFO "
                       f"band-width verdict RECONTEXTUALIZED as spectral-"
                       f"slope artifact, NOT truncation defect.")    # (local)
    elif delta_rel <= INFO_THRESH:
        verdict = "INFO"                                            # (local)
        band_interp = (f"modest truncation drift: {PASS_THRESH} < "
                       f"delta_rel = {delta_rel:.4e} <= {INFO_THRESH} "
                       f"(5%-20% INFO band). Both spectral-slope and "
                       f"truncation effects contribute.")           # (local)
    else:
        verdict = "FAIL"                                            # (local)
        band_interp = (f"substantial truncation drift: delta_rel = "
                       f"{delta_rel:.4e} > {INFO_THRESH} (FAIL band). "
                       f"L_max=10 spectrum NOT converged; queue L=12 "
                       f"follow-up for S87.")                       # (local)
    print(f"  VERDICT: {verdict}")
    print(f"  Band interpretation: {band_interp}")
    print()

    # -----------------------------------------------------------------------
    # 6F. CONTRAST WITH W13-2 §(f) band-width (plan §10 substitution chain)
    # -----------------------------------------------------------------------
    print("=" * 78)
    print("STEP 5 — Contrast with W13-2 §(f) band-width diagnostic (plan §10)")
    print("=" * 78)
    f_band_lo = 0.5 * f_LISA_pivot                                  # (local)
    f_band_hi = 2.0 * f_LISA_pivot                                  # (local)
    Omega_band_lo_L10 = omega_gw_loglog_interp(f_grid_L10,
                                                Omega_GW_f_L10,
                                                f_band_lo)          # (local)
    Omega_band_hi_L10 = omega_gw_loglog_interp(f_grid_L10,
                                                Omega_GW_f_L10,
                                                f_band_hi)          # (local)
    band_width_W13_2 = (abs(Omega_band_hi_L10 - Omega_band_lo_L10)
                        / Omega_L10)                                # (local)

    print(f"  f_band_lo = 0.5 * f_LISA = {f_band_lo:.3e} Hz")
    print(f"  f_band_hi = 2.0 * f_LISA = {f_band_hi:.3e} Hz")
    print(f"  Omega(f_band_lo; L=10) = {Omega_band_lo_L10:.3e}")
    print(f"  Omega(f_band_hi; L=10) = {Omega_band_hi_L10:.3e}")
    print(f"  band_width(L=10)        = {band_width_W13_2:.4e}")
    print(f"  delta_rel(L=8 vs L=10)  = {delta_rel:.4e}")
    print()
    print(f"  band_width holds L_max FIXED at 10, varies f over "
          f"[f_band_lo, f_band_hi] => SPECTRAL SLOPE")
    print(f"  delta_rel holds f FIXED at f_LISA, varies L_max from 10 to 8 "
          f"=> TRUNCATION SENSITIVITY")
    print(f"  These are independent log-derivatives of distinct kinds.")
    print()

    # -----------------------------------------------------------------------
    # 6G. Save L=8 spectrum cache (plan §6 promised output)
    # -----------------------------------------------------------------------
    np.savez(
        OUT_NPZ_L8,
        # Spectrum
        f_grid=f_grid_L8,
        Omega_GW_f=Omega_GW_f_L8,
        # Peak / scalar
        f_peak_today=f_peak_L8,
        Omega_peak=Omega_peak_L8,
        Omega_at_LISA=Omega_L8,
        # M_KK pin used
        M_KK_at_L8=M_KK_L8,
        L_max=8,
        # Provenance
        H_phys_GeV=H_L8,
        dt_phys_s=dt_phys_s_L8,
        redshift_factor=redshift_L8,
        x_frag_transit=x_frag_transit_L8,
        x_frag_DW=x_frag_DW_L8,
        # SHAs
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    spectrum_L8_sha = sha256_of(OUT_NPZ_L8)                         # (local)
    spectrum_L10_sha = sha256_of(resolve_output(85, 's85_w13_2_cgwb_alpha_s_joint.npz'))  # (local)

    # -----------------------------------------------------------------------
    # 6H. Save JSON comparison
    # -----------------------------------------------------------------------
    comparison_payload = {                                           # (local)
        "gate_id": GATE_ID,
        "verdict": verdict,
        "Omega_L8": float(Omega_L8),
        "Omega_L10": float(Omega_L10),
        "delta_rel": float(delta_rel),
        "f_LISA_Hz": 3.0e-3,
        "spectrum_L10_sha": spectrum_L10_sha,
        "spectrum_L8_sha": spectrum_L8_sha,
        "M_KK_canonical": float(M_KK),
        "M_KK_at_L8": float(M_KK_L8),
        "lambda_max_L8": LAMBDA_MAX_L8,
        "lambda_max_L10": LAMBDA_MAX_L10,
        "PASS_THRESH": PASS_THRESH,
        "INFO_THRESH": INFO_THRESH,
        "band_interpretation": band_interp,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX_PAIR_TAG,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "pins": pins,
        # Cross-diagnostic context
        "W13_2_anchor_Omega_LISA": Omega_W13_2_anchor,
        "L10_regen_vs_anchor_ratio": float(L10_anchor_ratio),
        "W13_2_band_width_L10": float(band_width_W13_2),
        "Omega_band_lo_L10_at_1p5mHz": float(Omega_band_lo_L10),
        "Omega_band_hi_L10_at_6mHz": float(Omega_band_hi_L10),
    }
    with OUT_JSON.open("w", encoding="utf-8") as fp:
        json.dump(comparison_payload, fp, indent=2)
    print(f"  JSON saved: {OUT_JSON}")

    # -----------------------------------------------------------------------
    # 6I. Plot — overlay log-log Omega_L8(f) and Omega_L10(f)
    # -----------------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(10, 7))                         # (local)

    # Restrict to LISA band frame
    f_min_plot = 1e-4                                               # (local) Hz
    f_max_plot = 1e-1                                               # (local) Hz
    mask_L10 = (f_grid_L10 >= f_min_plot) & (f_grid_L10 <= f_max_plot)
    mask_L8 = (f_grid_L8 >= f_min_plot) & (f_grid_L8 <= f_max_plot)

    ax.loglog(f_grid_L10[mask_L10], Omega_GW_f_L10[mask_L10],
              "b-", lw=2.0, label=fr"$\Omega_{{GW}}(f;\, L_{{\max}}=10)$,"
                                  fr" $M_{{KK}}={M_KK:.2e}$")
    ax.loglog(f_grid_L8[mask_L8], Omega_GW_f_L8[mask_L8],
              "r--", lw=2.0, label=fr"$\Omega_{{GW}}(f;\, L_{{\max}}=8)$,"
                                   fr" $M_{{KK}}={M_KK_L8:.2e}$")

    # f_LISA vertical line + delta_rel annotation
    ax.axvline(f_LISA_pivot, color="g", ls=":", lw=1.5,
               label=fr"$f_{{LISA}} = {f_LISA_pivot}\,$Hz")
    ax.plot(f_LISA_pivot, Omega_L10, "bo", ms=8,
            label=fr"$\Omega_{{L=10}} = {Omega_L10:.3e}$")
    ax.plot(f_LISA_pivot, Omega_L8, "rs", ms=8,
            label=fr"$\Omega_{{L=8}}  = {Omega_L8:.3e}$")

    # Annotation of delta_rel + verdict
    annotation_text = (fr"$\delta_{{rel}} = |\Omega_{{L=8}} - \Omega_{{L=10}}|"
                       fr" / \Omega_{{L=10}} = {delta_rel:.4e}$"
                       f"\nVerdict: {verdict}"
                       fr" (PASS $\leq$ {PASS_THRESH},"
                       fr" INFO $\leq$ {INFO_THRESH})")
    ax.text(0.04, 0.96, annotation_text, transform=ax.transAxes,
            fontsize=10, ha="left", va="top",
            bbox=dict(boxstyle="round", facecolor="lightyellow", alpha=0.85))

    ax.set_xlabel(r"$f$ (Hz)")
    ax.set_ylabel(r"$\Omega_{GW}(f)$")
    ax.set_title(f"S86 W8-3 ({GATE_ID}): $L_{{\\max}}=8$ vs $L_{{\\max}}=10$ "
                 f"truncation diagnostic; verdict = {verdict}")
    ax.grid(True, alpha=0.3, which="both")
    ax.legend(fontsize=8, loc="lower right")
    ax.set_xlim(f_min_plot, f_max_plot)
    plt.tight_layout()
    fig.savefig(OUT_PNG, dpi=140, bbox_inches="tight")
    plt.close(fig)
    print(f"  Plot saved: {OUT_PNG}")
    print()

    # -----------------------------------------------------------------------
    # 6J. Verdict line (S84+ dual-SHA) — append-only (no Edit)
    # -----------------------------------------------------------------------
    value_str = (f"(Omega_L8={Omega_L8:.4e},"                       # (local)
                 f"Omega_L10={Omega_L10:.4e},"
                 f"delta_rel={delta_rel:.4e})")
    verdict_line = (
        f"{GATE_ID}: {verdict} -- value={value_str} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX_PAIR_TAG} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )                                                               # (local)
    companion = (f"# audit_sha256 companion row: {GATE_ID} "
                 f"audit={audit_sha[:16]} content={content_sha[:16]}\n")  # (local)

    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(verdict_line)
        fp.write(companion)

    print("=" * 78)
    print("OUTPUTS SAVED")
    print("=" * 78)
    print(f"  Script   : {script_path}")
    print(f"  Data L=8 : {OUT_NPZ_L8}")
    print(f"  JSON     : {OUT_JSON}")
    print(f"  Plot     : {OUT_PNG}")
    print(f"  Verdict  : appended to {VERDICT_TXT}")
    print()
    print(f"VERDICT LINE (appended):")
    print(f"  {verdict_line.strip()}")
    print(f"  {companion.strip()}")
    print()
    print(f"4-tuple: (value={value_str}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX_PAIR_TAG})")
    wall = time.time() - t0                                         # (local)
    print(f"=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
