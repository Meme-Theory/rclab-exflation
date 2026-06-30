#!/usr/bin/env python3
"""
S88 W1b1-63 — S88-CF-CURV-10-SUBSTRATE-BITS-PER-PIXEL
=======================================================

Gate: S88-CF-CURV-10-SUBSTRATE-BITS-PER-PIXEL ([VERIFY])

Pre-registered threshold:
  PASS:  bits_per_pixel_substrate_internal >= bits_per_pixel_required
  FAIL:  bits_per_pixel_substrate_internal <  bits_per_pixel_required / 10
  INFO:  bits_per_pixel_required / 10 <= substrate < bits_per_pixel_required

Inputs (SHA-256 dual-pinned at runtime, S84+ schema):
  - canonical_constants.py
  - script bytes (content_sha256)

Output 4-tuple:
  (value=<bits_per_pixel_substrate_internal>,
   scheme=direct-Bekenstein-Hawking-vs-PW-block-internal-dim-comparison,
   convention=substrate-bits-per-pixel-LRD-horizon-J3-lock-Lmax10,
   L_max=10)

Classification: GEOMETRIC

METHODOLOGY
-----------
The gate compares the substrate's per-pixel internal Hilbert dimension at
L_max=10 against the Bekenstein-Hawking entropy budget per pixel for a
LRD-scale BH (M_BH = 1e7 M_sun) on the J3 pixelation lock convention
(L_pix = M_KK^{-1}).

Bekenstein-Hawking entropy is computed via Method A (canonical area-form):

  S_BH (nats) = A_BH / (4 l_p^2)
             = pi * r_s^2 / l_p^2
             = 4 pi (M_BH / m_p)^2  (Standard Planck mass m_p^2 = hbar c / G_N)

  S_BH (bits) = S_BH (nats) * log_2(e)
             = (4 pi / ln 2) * (M_BH / m_p)^2

Note on plan §W1b1-63 Step 1: the plan's interim simplification
"S_BH (nats) = pi * (M/m_p)^2" is 4x too small with Standard Planck mass
convention; the canonical Bekenstein-Hawking formula gives the factor-4
correction restored by Method A. Sage cross-check at plan-time confirms:

  Method A (canonical area): S_BH = 1.514e91 bits = 10^{91.18}
  Method B (corrected 4pi):  S_BH = 1.514e91 bits  (matches A by construction)
  Method B' (plan interim, factor pi only): 3.785e90 bits  (factor 4 short)

This script uses Method A (canonical) as the authoritative form.

Substrate per-pixel internal Hilbert dimension is computed as the FULL
Peter-Weyl block-sum at L_max=10, since the substrate IS the spectral
triple at every pixel (substrate-first principle):

  internal_dim_per_pixel = N_DK_eigenvalues * 16_chiral
                        = 155984 * 16 = 2,495,744
  bits_per_pixel_substrate = log_2(2,495,744) = 21.251

Comparison against required bits_per_pixel = S_BH / N_pix gives the verdict.

References:
  Plan:         sessions/session-plan/session-88-plan-w1b1.md §W1b1-63
  Canonical:    M_KK_gravity = 7.428660036284456e+16 GeV  (S42)
                tau_fold     = 0.19  (S42)
                G_N          = 6.67430e-11  (CODATA 2018; canonical_constants.py:39)
  Anchor:       M_BH = 1e7 M_sun = 1.989e37 kg  (LRD curvature-tension review)

DISCIPLINE
----------
- `from canonical_constants import *`
- All locals tagged `# (local)`
- Scalar arithmetic; CPU; OMP cap 8.
- SHA-256 input pins; dual-SHA emission (S84+)
- 4-tuple printed as final non-verdict line
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 - Canonical constants + thread cap
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

import sys as _sys_bootstrap
from pathlib import Path as _Path_bootstrap
_THIS_DIR = _Path_bootstrap(__file__).resolve().parent
if str(_THIS_DIR) not in _sys_bootstrap.path:
    _sys_bootstrap.path.insert(0, str(_THIS_DIR))

from canonical_constants import *  # noqa: F401, F403, E402

# ---------------------------------------------------------------------------
# Section 2 - Imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json     # noqa: E402
import sys      # noqa: E402
import time     # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 - Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S88"                                                       # (local)
GATE_ID = "S88-CF-CURV-10-SUBSTRATE-BITS-PER-PIXEL"                   # (local)
SCHEME = "direct-Bekenstein-Hawking-vs-PW-block-internal-dim-comparison"  # (local)
CONVENTION = "substrate-bits-per-pixel-LRD-horizon-J3-lock-Lmax10"    # (local)
L_MAX = 10                                                            # (local)

# Pre-registered LRD anchor + canonical constants (per plan PRDR table)
M_BH_LRD_kg = 1.0e7 * 1.98892e30   # (local)  M_BH = 1e7 M_sun  (LRD curvature-tension review)
                                    # IAU 2015 M_sun = 1.98892e30 kg
c_speed_m_s = 299792458.0           # (local)  exact (defined SI value)
hbar_J_s = 1.054571817e-34          # (local)  CODATA 2018
GeV_to_J = 1.602176634e-10          # (local)  exact (defined SI value, eV)
M_PL_KG_PIN = 2.176434e-8           # (local)  Planck mass (Standard convention) m_p = sqrt(hbar c / G_N), CODATA 2018
L_P_M_PIN = 1.616255e-35            # (local)  Planck length l_p = sqrt(hbar G_N / c^3), CODATA 2018

# Pre-registered substrate cardinality (S86 W-5 calibration; canonical)
N_DK_EIGENVALUES_AT_LMAX10 = 155984         # (local)  total D_K eigenvalues at L_max=10
N_CHIRAL_COMPONENTS = 16                    # (local)  16 chiral spinor components per eigenvalue

# Naive per-pixel ceiling (W6 preliminary; INFO reference)
NAIVE_BITS_PER_PIXEL = 140                  # (local)  W6 preliminary

# Cascade-depth-at-lock pin (per CC_OOM × log_2(10))
CASCADE_DEPTH_AT_LOCK = 384                 # (local)

# Pre-registered FAIL/PASS boundaries (per plan §W1b1-63 thresholds)
PASS_RATIO_MIN = 1.0                        # (local)  substrate >= required
FAIL_RATIO_MAX = 0.1                        # (local)  substrate < required/10

# Output destinations
OUT_NPZ = resolve_output(88, 's88_w1b1_substrate_bits_per_pixel.npz')
OUT_PNG = resolve_output(88, 's88_w1b1_substrate_bits_per_pixel.png')
VERDICT_TXT = resolve_output(88, 's88_gate_verdicts.txt')

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
]


# ---------------------------------------------------------------------------
# Section 4 - SHA-256 dual-SHA + helpers
# ---------------------------------------------------------------------------

def sha256_of(path):
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} - input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins):
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path, canonical_path, pins):
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(  # (local)
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")

    identity_keys = json.dumps({  # (local)
        "_gate_id": GATE_ID,
        "_wp_id": "W1b1-63",
        "_scheme": SCHEME,
        "_convention": CONVENTION,
        "_L_max": L_MAX,
    }, sort_keys=True, separators=(",", ":")).encode("utf-8")

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_audit.update(identity_keys)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 - Bekenstein-Hawking + pixel-count + substrate Hilbert dim
# ---------------------------------------------------------------------------

def compute_BH_entropy_bits_method_A(M_BH_kg):
    """S_BH (bits) via canonical area-form: A / (4 l_p^2) in nats * log_2(e).

    Returns S_BH in bits, plus intermediate (r_s, A_BH).
    """
    G_canon = G_N  # noqa: F405  imported from canonical_constants.py
    r_s_m = 2.0 * G_canon * M_BH_kg / c_speed_m_s**2                  # (local)
    A_BH_m2 = 4.0 * np.pi * r_s_m**2                                  # (local)
    S_BH_nats = A_BH_m2 / (4.0 * L_P_M_PIN**2)                        # (local)
    S_BH_bits = S_BH_nats * np.log2(np.e)                             # (local)
    return S_BH_bits, S_BH_nats, r_s_m, A_BH_m2


def compute_BH_entropy_bits_method_B_corrected(M_BH_kg):
    """S_BH (bits) via 4*pi*(M/m_p)^2 in nats * log_2(e), Standard Planck mass.

    Cross-check of Method A. With m_p^2 = hbar c / G_N (Standard convention),
    S_BH (nats) = 4 pi (M/m_p)^2.
    """
    M_over_mp = M_BH_kg / M_PL_KG_PIN                                  # (local)
    S_BH_nats_method_B = 4.0 * np.pi * M_over_mp**2                    # (local)
    S_BH_bits_method_B = S_BH_nats_method_B * np.log2(np.e)            # (local)
    return S_BH_bits_method_B, S_BH_nats_method_B, M_over_mp


def compute_BH_entropy_bits_method_B_plan_interim(M_BH_kg):
    """S_BH (bits) via plan's interim Step 1 form pi*(M/m_p)^2 (4x too small).

    Returns the plan's stated value for cross-check; NOT used for verdict.
    """
    M_over_mp = M_BH_kg / M_PL_KG_PIN                                  # (local)
    S_BH_nats_plan = np.pi * M_over_mp**2                              # (local)
    S_BH_bits_plan = S_BH_nats_plan * np.log2(np.e)                    # (local)
    return S_BH_bits_plan, S_BH_nats_plan


def compute_pixel_size_and_count(A_BH_m2):
    """Pixel size L_pix = hbar c / M_KK_J; pixel count N_pix = A_BH / L_pix^2."""
    M_KK_GeV = M_KK_gravity  # noqa: F405
    M_KK_J = M_KK_GeV * GeV_to_J                                      # (local)
    L_pix_m = hbar_J_s * c_speed_m_s / M_KK_J                         # (local)
    N_pix = A_BH_m2 / L_pix_m**2                                      # (local)
    return L_pix_m, N_pix, M_KK_J


def compute_substrate_per_pixel_internal_Hilbert_dim():
    """Per-pixel internal Hilbert dim at L_max=10.

    Substrate-first principle: the substrate IS the spectral triple at every
    pixel; therefore each pixel hosts a copy of the full L_max=10 substrate
    Hilbert space H_K. The internal dim is N_eigenvalues * 16 chiral.
    """
    internal_dim = N_DK_EIGENVALUES_AT_LMAX10 * N_CHIRAL_COMPONENTS    # (local)
    bits_per_pixel_substrate = np.log2(internal_dim)                   # (local)
    return internal_dim, bits_per_pixel_substrate


# ---------------------------------------------------------------------------
# Section 6 - Compute (full chain)
# ---------------------------------------------------------------------------

def compute():
    """Execute the full LRD-scale Bekenstein-Hawking vs substrate comparison."""
    # 1. Bekenstein-Hawking entropy
    S_BH_bits, S_BH_nats, r_s_m, A_BH_m2 = compute_BH_entropy_bits_method_A(M_BH_LRD_kg)
    log10_S_BH_bits = float(np.log10(S_BH_bits))                       # (local)
    print(f"  M_BH (kg)              = {M_BH_LRD_kg}")
    print(f"  r_s (m)                = {r_s_m:.6e}")
    print(f"  A_BH (m^2)             = {A_BH_m2:.6e}")
    print(f"  S_BH (nats, Method A)  = {S_BH_nats:.6e}")
    print(f"  S_BH (bits, Method A)  = {S_BH_bits:.6e}  (= 10^{log10_S_BH_bits:.4f})")

    # Cross-check Method B (corrected 4*pi)
    S_BH_bits_B, S_BH_nats_B, M_over_mp = compute_BH_entropy_bits_method_B_corrected(M_BH_LRD_kg)
    print(f"  S_BH (bits, Method B corrected 4pi) = {S_BH_bits_B:.6e}")
    rel_dev_AB = abs(S_BH_bits - S_BH_bits_B) / S_BH_bits              # (local)
    print(f"  rel_dev Method A vs Method B (corrected) = {rel_dev_AB:.6e}")

    # Plan-interim Method B' (factor pi only; 4x too small)
    S_BH_bits_plan_interim, _ = compute_BH_entropy_bits_method_B_plan_interim(M_BH_LRD_kg)
    plan_interim_factor_low = S_BH_bits_plan_interim / S_BH_bits        # (local)
    print(f"  S_BH (bits, plan interim Step 2 form) = {S_BH_bits_plan_interim:.6e}")
    print(f"  plan-interim / canonical ratio = {plan_interim_factor_low:.6f}  (expect 0.25 from m_p convention factor-4)")

    # 2. Pixel count
    L_pix_m, N_pix, M_KK_J = compute_pixel_size_and_count(A_BH_m2)
    log10_N_pix = float(np.log10(N_pix))                               # (local)
    print(f"  M_KK (J)               = {M_KK_J:.6e}")
    print(f"  L_pix (m)              = {L_pix_m:.6e}")
    print(f"  N_pix                  = {N_pix:.6e}  (= 10^{log10_N_pix:.4f})")

    # 3. Required bits per pixel
    bits_per_pixel_required = S_BH_bits / N_pix                        # (local)
    log10_bpp_req = float(np.log10(bits_per_pixel_required))           # (local)
    print(f"  bits_per_pixel_required = {bits_per_pixel_required:.4f}  (= 10^{log10_bpp_req:.4f})")

    # 4. Substrate per-pixel internal Hilbert dim
    substrate_internal_dim, bits_per_pixel_substrate = compute_substrate_per_pixel_internal_Hilbert_dim()
    print(f"  substrate_internal_dim  = {substrate_internal_dim} (= 155984 * 16)")
    print(f"  bits_per_pixel_substrate = {bits_per_pixel_substrate:.6f}  (= log_2 dim)")

    # 5. Excess factor and ratio
    substrate_to_required_ratio = bits_per_pixel_substrate / bits_per_pixel_required  # (local)
    excess_factor_required_over_substrate = bits_per_pixel_required / bits_per_pixel_substrate
    log10_excess = float(np.log10(excess_factor_required_over_substrate))
    print(f"  substrate / required ratio = {substrate_to_required_ratio:.6e}")
    print(f"  excess_factor (required / substrate) = {excess_factor_required_over_substrate:.4f}  (= 10^{log10_excess:.4f})")

    # 6. Naive 140-bit ceiling check (INFO reference)
    naive_to_required_ratio = NAIVE_BITS_PER_PIXEL / bits_per_pixel_required  # (local)
    excess_naive = bits_per_pixel_required / NAIVE_BITS_PER_PIXEL
    log10_excess_naive = float(np.log10(excess_naive))
    print(f"  required / naive_140    = {excess_naive:.4f}  (= 10^{log10_excess_naive:.4f})")

    # 7. FAIL boundary
    fail_boundary = bits_per_pixel_required * FAIL_RATIO_MAX           # (local)
    print(f"  FAIL boundary (required * 0.10) = {fail_boundary:.4f}")

    # 8. Classify per plan thresholds
    if substrate_to_required_ratio >= PASS_RATIO_MIN:
        track_classification = "substrate_accommodates"
        verdict = "PASS"
    elif substrate_to_required_ratio < FAIL_RATIO_MAX:
        track_classification = "substrate_falls_short_by_more_than_1_OOM"
        verdict = "FAIL"
    else:
        track_classification = "INFO_intermediate"
        verdict = "INFO"

    # 9. Cross-checks
    # CC-i: M_BH/m_p value matches the LRD-anchor (~9.14e44)
    cc_M_over_mp_consistency = abs(M_over_mp - 9.14e44) / 9.14e44 < 1e-2
    # CC-ii: S_BH ~ 10^91 bits (canonical area form, Method A)
    cc_S_BH_oom = abs(log10_S_BH_bits - 91.18) < 0.5
    # CC-iii: N_pix ~ 10^87
    cc_N_pix_oom = abs(log10_N_pix - 87.19) < 0.5
    # CC-iv: bits_per_pixel_required ~ 10^4
    cc_bpp_req_oom = abs(log10_bpp_req - 3.99) < 0.5
    # CC-v: bits_per_pixel_substrate = log_2(2.49e6) ~ 21.25
    cc_bpp_substrate_value = abs(bits_per_pixel_substrate - 21.25) < 0.05
    # CC-vi: Method A = Method B (corrected 4*pi) at machine epsilon
    cc_method_A_eq_B_corrected = rel_dev_AB < 1e-9
    # CC-vii: Method B-plan-interim is exactly 1/4 of Method A (m_p convention factor)
    cc_plan_interim_factor_4 = abs(plan_interim_factor_low - 0.25) < 1e-9
    # CC-viii: J3 lock convention check r_s(M_BH) = L_pix(t_formation) at LRD scale gives a different d_lock?
    # The naive r_s/L_pix ratio at LRD: r_s/L_pix = 2.95e10 / 2.66e-33 = 1.11e43
    # log_2(1.11e43) = 142.7 (so r_s/L_pix corresponds to cascade depth ~143, NOT 384)
    # The 384 is from CC_OOM × log_2(10) cosmological convention; r_s/L_pix is direct mass-ratio
    r_s_over_L_pix_log2 = float(np.log2(r_s_m / L_pix_m))
    cc_d_lock_convention_alt = (r_s_over_L_pix_log2 < CASCADE_DEPTH_AT_LOCK)
    # log_2(r_s/L_pix) = log_2(N_pix^{1/2}) = (1/2) * log_2(A_BH/L_pix^2) since A_BH = pi r_s^2 ~ 4*r_s^2
    # So log_2(N_pix) = log_2(4*pi*r_s^2/L_pix^2) ~ 2 * log_2(r_s/L_pix) + log_2(4*pi)
    # Confirms d_lock_via_pixel_count = log_2(N_pix) ~ 290; CC_OOM convention = 384.

    print(f"\n  CC-i   M_BH/m_p match         : {cc_M_over_mp_consistency}")
    print(f"  CC-ii  S_BH OOM ~ 10^91.18    : {cc_S_BH_oom}")
    print(f"  CC-iii N_pix OOM ~ 10^87.19   : {cc_N_pix_oom}")
    print(f"  CC-iv  bpp_req OOM ~ 10^3.99  : {cc_bpp_req_oom}")
    print(f"  CC-v   bpp_substrate ~ 21.25  : {cc_bpp_substrate_value}")
    print(f"  CC-vi  Method A == B-corrected: {cc_method_A_eq_B_corrected}")
    print(f"  CC-vii plan-interim/A = 0.25  : {cc_plan_interim_factor_4}")
    print(f"  CC-viii d_lock alt ~ {r_s_over_L_pix_log2:.1f} < 384 (CC_OOM): {cc_d_lock_convention_alt}")

    return {
        "value": float(bits_per_pixel_substrate),
        "verdict": verdict,
        # Bekenstein-Hawking (Method A canonical)
        "M_BH_LRD_kg": float(M_BH_LRD_kg),
        "r_s_m": float(r_s_m),
        "A_BH_m2": float(A_BH_m2),
        "S_BH_nats": float(S_BH_nats),
        "S_BH_bits": float(S_BH_bits),
        "log10_S_BH_bits": float(log10_S_BH_bits),
        # Method B cross-checks
        "S_BH_bits_method_B_corrected": float(S_BH_bits_B),
        "S_BH_bits_plan_interim": float(S_BH_bits_plan_interim),
        "plan_interim_factor_low": float(plan_interim_factor_low),
        "rel_dev_method_A_vs_B_corrected": float(rel_dev_AB),
        "M_over_mp_LRD": float(M_over_mp),
        # Pixel count
        "M_KK_J": float(M_KK_J),
        "L_pix_m": float(L_pix_m),
        "N_pixels_at_horizon": float(N_pix),
        "log10_N_pix": float(log10_N_pix),
        # Bits per pixel
        "bits_per_pixel_required": float(bits_per_pixel_required),
        "log10_bits_per_pixel_required": float(log10_bpp_req),
        "bits_per_pixel_naive": float(NAIVE_BITS_PER_PIXEL),
        "bits_per_pixel_substrate_internal": float(bits_per_pixel_substrate),
        "substrate_internal_dim": int(substrate_internal_dim),
        # Ratios
        "substrate_to_required_ratio": float(substrate_to_required_ratio),
        "excess_factor_required_over_substrate": float(excess_factor_required_over_substrate),
        "log10_excess_factor": float(log10_excess),
        "excess_naive_required_over_140": float(excess_naive),
        "fail_boundary_bpp": float(fail_boundary),
        # Classification
        "track_classification": track_classification,
        # Cross-checks
        "cc_M_over_mp_consistency": bool(cc_M_over_mp_consistency),
        "cc_S_BH_oom": bool(cc_S_BH_oom),
        "cc_N_pix_oom": bool(cc_N_pix_oom),
        "cc_bpp_req_oom": bool(cc_bpp_req_oom),
        "cc_bpp_substrate_value": bool(cc_bpp_substrate_value),
        "cc_method_A_eq_B_corrected": bool(cc_method_A_eq_B_corrected),
        "cc_plan_interim_factor_4": bool(cc_plan_interim_factor_4),
        "cc_d_lock_convention_alt": bool(cc_d_lock_convention_alt),
        "r_s_over_L_pix_log2": float(r_s_over_L_pix_log2),
        # Pinned canonicals
        "L_max": L_MAX,
        "tau_fold_pin": float(tau_fold),  # noqa: F405
        "M_KK_gravity_pin": float(M_KK_gravity),  # noqa: F405
        "G_N_pin": float(G_N),  # noqa: F405
        "M_PL_KG_PIN": float(M_PL_KG_PIN),
        "L_P_M_PIN": float(L_P_M_PIN),
        "cascade_depth_at_lock_pin": int(CASCADE_DEPTH_AT_LOCK),
        "PASS_RATIO_MIN": float(PASS_RATIO_MIN),
        "FAIL_RATIO_MAX": float(FAIL_RATIO_MAX),
    }


def evaluate_gate(result):
    return result["verdict"]


# ---------------------------------------------------------------------------
# Section 7 - Plot
# ---------------------------------------------------------------------------

def make_plot(result):
    """Bar chart on log scale: required vs naive vs substrate-internal bits/pixel."""
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))

    labels = ["substrate\n(L_max=10)", "naive ceiling\n(W6 prelim)",
              "FAIL boundary\n(required/10)", "required\n(LRD-scale BH)"]
    values = [
        result["bits_per_pixel_substrate_internal"],
        result["bits_per_pixel_naive"],
        result["fail_boundary_bpp"],
        result["bits_per_pixel_required"],
    ]
    log_values = np.log10(values)  # (local)
    colors = ["C2" if values[0] >= values[3] else "C3", "C0", "orange", "C1"]
    bars = ax.bar(labels, log_values, color=colors, edgecolor="black", lw=1.5)

    # Horizontal annotation lines for PASS / FAIL boundaries
    ax.axhline(np.log10(result["bits_per_pixel_required"]), color="C1", lw=1,
               ls="--", label=f"PASS threshold: substrate >= required = {result['bits_per_pixel_required']:.0f} bits")
    ax.axhline(np.log10(result["fail_boundary_bpp"]), color="orange", lw=1,
               ls=":", label=f"FAIL threshold: substrate < {result['fail_boundary_bpp']:.0f} bits (= required/10)")

    # Annotate each bar with its value
    for bar, val in zip(bars, values):
        height = bar.get_height()  # (local)
        ax.text(bar.get_x() + bar.get_width() / 2, height + 0.1,
                f"{val:.2f}", ha='center', va='bottom', fontsize=10, fontweight="bold")

    ax.set_ylabel(r"$\log_{10}$(bits per pixel)")
    ax.set_title(f"S88 W1b1-63: substrate-bits-per-pixel vs Bekenstein-Hawking budget at LRD scale\n"
                 f"M_BH = {result['M_BH_LRD_kg']:.3e} kg ; verdict = {result['verdict']} "
                 f"(track = {result['track_classification']})")
    ax.legend(loc="upper left", fontsize=9)
    ax.grid(True, alpha=0.3, axis="y")

    # Annotate excess factor in subtitle
    ax.text(0.5, -0.18,
            f"excess_factor (required / substrate) = {result['excess_factor_required_over_substrate']:.2f}× "
            f"≈ 10^{result['log10_excess_factor']:.2f} OOM short",
            transform=ax.transAxes, ha='center', fontsize=10, style='italic')

    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=120)
    plt.close(fig)
    print(f"  plot saved: {OUT_PNG.relative_to(PROJECT_ROOT)}")


# ---------------------------------------------------------------------------
# Section 8 - Verdict emission
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme, convention, L_max):
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict, value, audit_sha, content_sha):
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


# ---------------------------------------------------------------------------
# Section 9 - Main
# ---------------------------------------------------------------------------

def main():
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure (legacy): {closure[:16]}...")

    script_path = Path(__file__).resolve()              # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script + canonical + pinmap + identity-keys)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    print("=== compute (Bekenstein-Hawking + N_pix + substrate per-pixel dim) ===")
    result = compute()
    value = result["value"]

    make_plot(result)

    np.savez(
        OUT_NPZ,
        M_BH_LRD_kg=np.float64(result["M_BH_LRD_kg"]),
        r_s_m=np.float64(result["r_s_m"]),
        A_BH_m2=np.float64(result["A_BH_m2"]),
        S_BH_nats=np.float64(result["S_BH_nats"]),
        S_BH_bits=np.float64(result["S_BH_bits"]),
        log10_S_BH_bits=np.float64(result["log10_S_BH_bits"]),
        S_BH_bits_method_B_corrected=np.float64(result["S_BH_bits_method_B_corrected"]),
        S_BH_bits_plan_interim=np.float64(result["S_BH_bits_plan_interim"]),
        plan_interim_factor_low=np.float64(result["plan_interim_factor_low"]),
        rel_dev_method_A_vs_B_corrected=np.float64(result["rel_dev_method_A_vs_B_corrected"]),
        M_over_mp_LRD=np.float64(result["M_over_mp_LRD"]),
        M_KK_J=np.float64(result["M_KK_J"]),
        L_pix_m=np.float64(result["L_pix_m"]),
        N_pixels_at_horizon=np.float64(result["N_pixels_at_horizon"]),
        log10_N_pix=np.float64(result["log10_N_pix"]),
        bits_per_pixel_required=np.float64(result["bits_per_pixel_required"]),
        log10_bits_per_pixel_required=np.float64(result["log10_bits_per_pixel_required"]),
        bits_per_pixel_naive=np.float64(result["bits_per_pixel_naive"]),
        bits_per_pixel_substrate_internal=np.float64(result["bits_per_pixel_substrate_internal"]),
        substrate_internal_dim=np.int64(result["substrate_internal_dim"]),
        substrate_to_required_ratio=np.float64(result["substrate_to_required_ratio"]),
        excess_factor_required_over_substrate=np.float64(result["excess_factor_required_over_substrate"]),
        log10_excess_factor=np.float64(result["log10_excess_factor"]),
        excess_naive_required_over_140=np.float64(result["excess_naive_required_over_140"]),
        fail_boundary_bpp=np.float64(result["fail_boundary_bpp"]),
        track_classification=np.array(result["track_classification"]),
        cc_M_over_mp_consistency=np.bool_(result["cc_M_over_mp_consistency"]),
        cc_S_BH_oom=np.bool_(result["cc_S_BH_oom"]),
        cc_N_pix_oom=np.bool_(result["cc_N_pix_oom"]),
        cc_bpp_req_oom=np.bool_(result["cc_bpp_req_oom"]),
        cc_bpp_substrate_value=np.bool_(result["cc_bpp_substrate_value"]),
        cc_method_A_eq_B_corrected=np.bool_(result["cc_method_A_eq_B_corrected"]),
        cc_plan_interim_factor_4=np.bool_(result["cc_plan_interim_factor_4"]),
        cc_d_lock_convention_alt=np.bool_(result["cc_d_lock_convention_alt"]),
        r_s_over_L_pix_log2=np.float64(result["r_s_over_L_pix_log2"]),
        L_max=np.int64(result["L_max"]),
        tau_fold_pin=np.float64(result["tau_fold_pin"]),
        M_KK_gravity_pin=np.float64(result["M_KK_gravity_pin"]),
        G_N_pin=np.float64(result["G_N_pin"]),
        M_PL_KG_PIN=np.float64(result["M_PL_KG_PIN"]),
        L_P_M_PIN=np.float64(result["L_P_M_PIN"]),
        cascade_depth_at_lock_pin=np.int64(result["cascade_depth_at_lock_pin"]),
        PASS_RATIO_MIN=np.float64(result["PASS_RATIO_MIN"]),
        FAIL_RATIO_MAX=np.float64(result["FAIL_RATIO_MAX"]),
    )
    print(f"  data saved: {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    verdict = evaluate_gate(result)
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)
    append_verdict(verdict, value, audit_sha, content_sha)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    print(f"  track_classification = {result['track_classification']}")
    print(f"  bits_per_pixel_substrate_internal = {result['bits_per_pixel_substrate_internal']:.6f}")
    print(f"  bits_per_pixel_required           = {result['bits_per_pixel_required']:.4f}")
    print(f"  excess_factor (req/substrate)     = {result['excess_factor_required_over_substrate']:.2f}x")
    return 0


if __name__ == "__main__":
    sys.exit(main())
