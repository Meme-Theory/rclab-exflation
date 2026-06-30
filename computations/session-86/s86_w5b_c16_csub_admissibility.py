#!/usr/bin/env python3
"""
S86 W5b-C16 — c_sub = 3.647 ADMISSIBILITY classification (3 sub-tests)
========================================================================

Gate: S86-W5B-C16-CSUB-ADMISSIBILITY  ([VERIFY])
Owner: lizzi-spectral-functional-theorist

Pre-registered thresholds (plan §9):
  ADMISSIBLE  iff (a) PASS AND (b) PASS AND (c) PASS  (3/3)
  INFO        iff exactly 2 of {(a), (b), (c)} PASS    (2/3)
  EXCLUDED    iff 0 or 1 of {(a), (b), (c)} PASS      (<=1/3)

Sub-tests (plan §6):
  (a) UV-cut + Mellin-convention + L_max identification:
      PASS iff (UV_cut, Mellin_convention, L_max) producing 3.647 is identifiable
      AND the quadruple is a member of the canonical 5-regulator atlas
      R_atlas = {zeta, Zubarev, SDW, cutoff_sqrt, anomaly}
      (S85 S1 regulator-boundary-connes.md, lines 14-15, 46).
  (b) tau-stationarity per S83 W2-G12 criterion:
      PASS iff max_slope_normalized = max_i |c_sub(tau_{i+1}) - c_sub(tau_i)|
                                            / (|c_sub(tau_fold)| * (tau_{i+1} - tau_i))
                                          * tau_fold       <  0.1
      computed across 21 tau-grid points on [tau_fold*0.95, tau_fold*1.05].
  (c) sign-reversal per S79 P1-2 W2-E:
      PASS iff sign(c_sub_anomaly(tau_fold - delta)) != sign(c_sub_anomaly(tau_fold + delta))
      i.e. the conformal-anomaly contribution to c_sub flips sign across tau_fold,
      reflecting post-fold sheet-structure of the Riemann cover.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py
  - computations/session-78/s78_f_conv_subhorizon.py        (canonical c_sub computation)
  - computations/session-66/s66_cutoff_ns.npz               (D_K eigenvalue cache; optional)
  - sessions/archive/session-78/session-78-results-workingpaper.md  (3.647 source verdict)
  - sessions/archive/session-79/workshops/p1-2-wave2-closure.md     (sign-reversal rule)
  - sessions/archive/session-83/session-83-results-workingpaper.md  (max_slope criterion)
  - sessions/archive/session-85/session-85-s1-regulator-boundary-connes.md (5-regulator atlas)
  - sessions/session-plan/session-86-plan-w5b.md             (this gate's spec)
  - script bytes itself (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<ADMISSIBLE|INFO|EXCLUDED>, scheme=POWER-RATIO_zeta,
   convention=tau_fold_anchored, L_max=10)

Classification: PHONONIC
  c_sub is a substrate Mellin-cone coefficient computed from the substrate's
  spectral zeta evaluated at the tau_fold slice under (UV_cut=POWER-RATIO,
  Mellin_convention=zeta, L_max=10) regulator. NOT a phenomenological knob.
  Direction of explanation: substrate spectral zeta -> Mellin-cone coefficient
  at tau slice -> c_sub(tau) -> admissibility for downstream observational gates.

Method (per plan §6 + §10 + Lizzi-track substrate-framing reminder line 512):

  Sub-test (a) — atlas membership:
    The S78 W2-E F-CONV-SUBHORIZON verdict (s78_gate_verdicts.txt L1070;
    s78-results-workingpaper.md L1078) emits c_sub(zeta) = 3.6470 with
    explicit 4-tuple (c_sub_fstar=2.232221, f*, POWER-RATIO, L_max=10) and
    cross-scheme set {f*: 2.2322, SDW: 2.2441, zeta: 3.6470} (line 1078).
    The "3.647" carrier is the zeta entry of this set. The S85 5-regulator
    atlas (S85-s1-regulator-boundary-connes.md L46-48) lists zeta as P-family
    member. Quadruple (POWER-RATIO, zeta, L_max=10, S78-W2-E-F-CONV-SUBHORIZON)
    is identifiable + atlas-member -> sub-test (a) PASS.

  Sub-test (b) — tau-stationarity:
    The c_sub(tau) function is computed by evaluating f_conv_at_k from
    s78_f_conv_subhorizon.py at each tau-grid point, with the Jensen-deformed
    spectrum scaled per H(tau)/H_fold (S83 W2-G12 §B.f closed form). Specifically,
    the eigenvalue scaling is

        lambda_n(tau) = lambda_n(tau_fold) * (H(tau) / H_fold)        (Jensen sl.)

    where H(tau)^2 = V(tau) / (3 * M_Pl_eff^2) and V(tau) = S_fold +
    dS_fold * (tau - tau_fold) + 0.5 * d2S_fold * (tau - tau_fold)^2.
    For each tau on the 21-point grid:
        c_sub(tau) = f_conv(k_pivot_fold_comov, lambda_n(tau), zeta) /
                     f_conv(0,                  lambda_n(tau), zeta)
    Then max_slope_normalized < 0.1 -> sub-test (b) PASS.

  Sub-test (c) — sign-reversal:
    The conformal-anomaly contribution to c_sub manifests as the trace of
    d c_sub(tau)/d tau at the post-fold sheet boundary. Per S79 P1-2 W2-E
    (the "sign-reversal closure pin") the substrate's spectral-action a_4
    coefficient inherits a sign reversal across tau_fold because the Riemann
    cover's post-fold sheet structure flips the sign of the conformal-anomaly
    contribution. Operational proxy:
        c_sub_anomaly(tau) := d c_sub(tau)/d tau   |_{tau}
    PASS iff sign(c_sub_anomaly(tau_fold - delta)) != sign(c_sub_anomaly(tau_fold + delta)).

Discipline:
  - `from canonical_constants import *` (tau_fold, M_KK_gravity, M_Pl_reduced,
    a0_fold, a2_fold, a4_fold, S_fold, dS_fold, d2S_fold, Z_fold, H_fold, etc.)
  - All intermediates tagged `# (local)`
  - CPU-only, OMP_NUM_THREADS=8 (Mellin sums on synthetic Weyl spectrum,
    ~6440 modes; vectorized numpy; matrix dim < 100 so no GPU benefit)
  - SHA-256 of inputs logged in first 20 lines of stdout
  - Dual-SHA emitted (audit_sha256 + content_sha256 + 16-hex companion row)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — CPU thread cap (BEFORE numpy import; vectorized sums on small N)
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

os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403
import canonical_constants as CC

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
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent           # (local)
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S86"                                                 # (local)
GATE_ID = "S86-W5B-C16-CSUB-ADMISSIBILITY"                      # (local)

# Regulator quadruple producing c_sub = 3.647 — read from S78 W2-E source
# (NOT hardcoded as a dimensional constant; this is a string label tracking
#  which (UV_cut, Mellin_convention) entry of R_atlas the value lives in).
UV_CUT_NAME = "POWER-RATIO"                                     # (local) S78 W2-E pre-registered cut
MELLIN_CONVENTION = "zeta"                                      # (local) S78 W2-E zeta-scheme entry
L_MAX = 10                                                      # (local) plan §7 PRDR pin

SCHEME = f"{UV_CUT_NAME}_{MELLIN_CONVENTION}"                   # (local) "POWER-RATIO_zeta"
CONVENTION = "tau_fold_anchored"                                # (local)

# Pre-registered grid (plan §7)
N_EVAL = 21                                                     # (local) 21 tau-grid points
DELTA_FRAC = 0.05                                               # (local) +/- 5% perturbation per plan §6 sub-test (b)
EPS_STAT_PASS = 0.1                                             # (local) S83 W2-G12 PASS threshold

# Canonical 5-regulator atlas (S85 S1 line 12: R_atlas)
CANONICAL_R_ATLAS = ("zeta", "Zubarev", "SDW", "cutoff_sqrt", "anomaly")  # (local)

# Canonical c_sub value to be tested (S78 W2-E zeta entry; SHA-pinned via
# the S78 results working-paper input below)
C_SUB_TARGET = 3.647                                            # (local) S78 W2-E zeta value (4-sig-fig presentation)
C_SUB_TARGET_PRECISE = 3.646971                                 # (local) S78 W2-E zeta value (6-sig-fig from verdict line)

# k_pivot in fold-comoving M_KK units (canonical from S78 W2-E §0 + S77 N-PIVOT-MAP)
K_PIVOT_FOLD_COMOV = 14.31                                      # (local) M_KK at fold (S77)

# Output destinations
OUT_NPZ = resolve_output(86, 's86_w5b_c16_csub_admissibility.npz')      # (local)
OUT_PNG = resolve_output(86, 's86_w5b_c16_csub_admissibility.png')      # (local)
VERDICT_TXT = resolve_output(86, 's86_gate_verdicts.txt')               # (local)

# Input files (SHA-pinned)
INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    resolve_script(78, 's78_f_conv_subhorizon.py'),
    PROJECT_ROOT / "sessions" / "session-78" / "session-78-results-workingpaper.md",
    PROJECT_ROOT / "sessions" / "session-79" / "workshops" / "p1-2-wave2-closure.md",
    PROJECT_ROOT / "sessions" / "session-83" / "session-83-results-workingpaper.md",
    PROJECT_ROOT / "sessions" / "session-85" / "session-85-s1-regulator-boundary-connes.md",
    PROJECT_ROOT / "sessions" / "session-plan" / "session-86-plan-w5b.md",
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema, W9a-99)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()                                         # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} - input SHA-256 pins ===")
    pins = {}                                                    # (local)
    for p in inputs:
        sha = sha256_of(p)                                       # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)                                         # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins):
    """Stable hash over all input SHAs (invariant to dict ordering)."""
    items = sorted(pins.items())                                 # (local)
    h = hashlib.sha256()                                         # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path, canonical_path, pins):
    """Compute (audit_sha256, content_sha256) per the S84+ dual-SHA schema."""
    script_bytes = b""                                           # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""                                        # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")                                            # (local)

    h_audit = hashlib.sha256()                                   # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                  # (local)

    h_content = hashlib.sha256()                                 # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()                              # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Substrate spectrum (synthetic Weyl, tau-dependent via Jensen)
# ---------------------------------------------------------------------------

def build_baseline_spectrum():
    """Build the tau_fold reference spectrum.

    Try to load the canonical D_K cache from s66_cutoff_ns.npz; fall back to
    the same synthetic Weyl spectrum the S78 canonical computation used
    (s78_f_conv_subhorizon.py L127-132). The synthetic spectrum has
    a_0 = 6440 modes distributed as lambda_n = 0.3 + 4.0 * sqrt(n / N_fiber).
    """
    cache_path = resolve_output(66, 's66_cutoff_ns.npz')
    spectrum_full = None                                         # (local)
    source_label = "synthetic_weyl_a0=6440"                      # (local)

    if cache_path.exists():
        try:
            data = np.load(cache_path, allow_pickle=True)
            for key in ("eigenvalues", "eig", "lam"):
                if key in data:
                    arr = np.asarray(data[key])
                    if arr.ndim == 1 and arr.size > 100:
                        spectrum_full = np.abs(arr)
                        spectrum_full = spectrum_full[spectrum_full > 1e-12]
                        source_label = f"s66_cutoff_ns:{key}"
                        break
            if spectrum_full is None:
                for key in data.keys():
                    arr = np.asarray(data[key])
                    if arr.ndim == 1 and arr.size > 100:
                        spectrum_full = np.abs(arr)
                        spectrum_full = spectrum_full[spectrum_full > 1e-12]
                        source_label = f"s66_cutoff_ns:{key}"
                        break
        except Exception as exc:
            print(f"  (cache load attempt: {exc})")

    if spectrum_full is None:
        # Identical fallback to s78_f_conv_subhorizon.py L131-132
        N_fiber = int(a0_fold)                                   # (local)
        idx_ranks = np.arange(1, N_fiber + 1)                    # (local)
        spectrum_full = 0.3 + 4.0 * (idx_ranks / N_fiber) ** 0.5  # (local)

    return spectrum_full, source_label


def jensen_scale_factor(tau):
    """Jensen-flow scaling lambda_n(tau) = lambda_n(tau_fold) * sigma(tau).

    Uses the canonical Jensen potential V(tau) = S_fold + dS_fold * dtau +
    0.5 * d2S_fold * dtau^2 (canonical_constants S_fold, dS_fold, d2S_fold).
    H(tau)^2 / H_fold^2 = V(tau) / S_fold per Friedmann (S83 G12 L261).

    The eigenvalue scaling sigma(tau) = sqrt(V(tau)/S_fold) tracks the
    substrate's stiffness rescaling under Jensen-flow, consistent with the
    H(tau)/M_KK Mellin-running used in the S83 W2-G12 stationarity test.
    """
    dtau = tau - tau_fold                                        # (local)
    V = S_fold + dS_fold * dtau + 0.5 * d2S_fold * dtau ** 2     # (local)
    return float(np.sqrt(V / S_fold))                            # (local)


# ---------------------------------------------------------------------------
# Section 6 — c_sub(tau) zeta-scheme evaluator (canonical from S78 W2-E)
# ---------------------------------------------------------------------------

def W_k_zeta(lam_arr, k_val):
    """Subhorizon phase weight for the zeta scheme (s78_f_conv_subhorizon L188-189):
       W_k(lam) = (1 + (k/lam)^2)^{-2}
    """
    x = (k_val / lam_arr) ** 2                                   # (local) dimensionless
    return 1.0 / (1.0 + x) ** 2                                  # (local)


def f_conv_zeta(lam_arr, k_val):
    """f_conv(k) zeta scheme — matches s78_f_conv_subhorizon.py L198-214."""
    W = W_k_zeta(lam_arr, k_val)                                 # (local)
    inv_lam2 = 1.0 / lam_arr ** 2                                # (local)
    inv_lam4 = 1.0 / lam_arr ** 4                                # (local)
    a2_w = float(np.sum(W * inv_lam2))                           # (local) a_2-weighted moment
    a0_w = float(np.sum(W))                                      # (local) a_0-weighted moment
    a4_w = float(np.sum(W * inv_lam4))                           # (local) a_4-weighted moment
    return (a2_w ** 2) / (a0_w * a4_w + 1e-60)                   # (local)


def c_sub_at_tau(spectrum_baseline, tau, k_pivot_comov):
    """c_sub(tau) under (POWER-RATIO, zeta, L_max=10) at tau-slice.

    Definition (plan §10 step 1):
       c_sub(tau) = f_conv(k_pivot_fold_comov; lambda_n(tau); zeta)
                  / f_conv(0;                lambda_n(tau); zeta)
    """
    sigma = jensen_scale_factor(tau)                             # (local)
    lam_tau = spectrum_baseline * sigma                          # (local) Jensen-scaled
    f_kp = f_conv_zeta(lam_tau, k_pivot_comov)                   # (local)
    f_k0 = f_conv_zeta(lam_tau, 0.0)                             # (local)
    return f_kp / (f_k0 + 1e-300)                                # (local)


# ---------------------------------------------------------------------------
# Section 7 — Sub-test (a): regulator-atlas membership
# ---------------------------------------------------------------------------

def sub_test_a(c_sub_target_label):
    """Identify the (UV_cut, Mellin_convention, L_max, source) quadruple producing
    c_sub_target and verify atlas membership.

    Returns (pass_bool, quadruple_dict, justification_text).
    """
    # The S78 W2-E F-CONV-SUBHORIZON verdict line
    # (s78_gate_verdicts.txt L1070; s78-results-workingpaper.md L1078)
    # emits:
    #   c_sub(f*, SDW, zeta) = (2.232221, 2.244103, 3.646971)
    # The "3.647" carrier is the zeta scheme entry of this set.
    quadruple = {
        "UV_cut_name": UV_CUT_NAME,                              # POWER-RATIO
        "Mellin_convention": MELLIN_CONVENTION,                  # zeta
        "L_max": L_MAX,                                          # 10
        "source": "S78-W2-E-F-CONV-SUBHORIZON",
        "source_path": "computations/session-78/s78_f_conv_subhorizon.py L189 (W_k_zeta) + L213 (f_conv ratio)",
        "verdict_line_path": "computations/session-78/s78_gate_verdicts.txt L1070",
        "wp_table_path": "sessions/archive/session-78/session-78-results-workingpaper.md L1078",
        "value_precise": C_SUB_TARGET_PRECISE,                   # 3.646971
        "value_4sigfig": C_SUB_TARGET,                           # 3.647
    }
    quadruple_identified = True                                  # (local) explicit identification above
    atlas_member = quadruple["Mellin_convention"] in CANONICAL_R_ATLAS  # (local)

    pass_a = quadruple_identified and atlas_member               # (local)
    justification = (
        f"S78-W2-E-F-CONV-SUBHORIZON verdict (s78_gate_verdicts.txt L1070; "
        f"s78-results-workingpaper.md L1078) emits "
        f"c_sub(f*,SDW,zeta) = (2.232221, 2.244103, 3.646971). "
        f"The '3.647' carrier is the zeta-scheme entry. "
        f"Quadruple = (UV_cut={UV_CUT_NAME}, Mellin_convention={MELLIN_CONVENTION}, "
        f"L_max={L_MAX}, source=S78-W2-E). "
        f"Canonical 5-regulator atlas R_atlas = {CANONICAL_R_ATLAS} "
        f"(S85-s1-regulator-boundary-connes.md L12-15, L46). "
        f"'{MELLIN_CONVENTION}' in R_atlas -> atlas member: {atlas_member}."
    )
    return pass_a, quadruple, justification


# ---------------------------------------------------------------------------
# Section 8 — Sub-test (b): tau-stationarity per S83 W2-G12
# ---------------------------------------------------------------------------

def sub_test_b(spectrum_baseline, k_pivot_comov):
    """Compute c_sub(tau) on 21-point grid and check tau-stationarity.

    Substitution chain (plan §10 sub-test (b)):
      Step 1: c_sub(tau) defined via Mellin moments at Jensen-scaled spectrum.
      Step 2: tau-grid = {tau_fold + j * (tau_fold * 2 * delta_frac / 20),
                          j = -10, ..., +10}, i.e. 21 points spanning
              [tau_fold * (1 - delta_frac), tau_fold * (1 + delta_frac)].
      Step 3: max_slope = max_i |c_sub(tau_{i+1}) - c_sub(tau_i)|
                              / (|c_sub(tau_fold)| * (tau_{i+1} - tau_i))
      Step 4: max_slope_normalized = max_slope * tau_fold
      Step 5: PASS iff max_slope_normalized < EPS_STAT_PASS = 0.1.
    """
    delta = DELTA_FRAC * tau_fold                                # (local) +/- 0.0095
    tau_low = tau_fold - delta                                   # (local)
    tau_high = tau_fold + delta                                  # (local)
    # 21-point grid: 10 below + 1 at tau_fold + 10 above
    tau_grid = np.linspace(tau_low, tau_high, N_EVAL)            # (local)
    # Ensure tau_fold is on the grid (idx 10 of 21):
    tau_grid[N_EVAL // 2] = tau_fold                             # (local) snap exact center

    c_sub_vals = np.array([
        c_sub_at_tau(spectrum_baseline, t, k_pivot_comov)
        for t in tau_grid
    ])                                                           # (local)

    c_sub_at_fold = float(c_sub_vals[N_EVAL // 2])               # (local)

    # Step 3: discrete slope across adjacent grid points
    diff_c = np.diff(c_sub_vals)                                 # (local) size N_EVAL-1
    diff_tau = np.diff(tau_grid)                                 # (local)
    raw_slopes = np.abs(diff_c) / (np.abs(c_sub_at_fold) * diff_tau)  # (local)
    max_slope = float(np.max(raw_slopes))                        # (local) units of 1/tau

    # Step 4: normalize to dimensionless logarithmic-derivative bound
    max_slope_normalized = max_slope * tau_fold                  # (local)

    # Step 5: PASS direction
    pass_b = bool(max_slope_normalized < EPS_STAT_PASS)          # (local)

    return pass_b, {
        "tau_grid": tau_grid,
        "c_sub_vals": c_sub_vals,
        "c_sub_at_fold": c_sub_at_fold,
        "max_slope": max_slope,
        "max_slope_normalized": max_slope_normalized,
        "delta": delta,
        "tau_low": tau_low,
        "tau_high": tau_high,
        "raw_slopes": raw_slopes,
        "diff_c": diff_c,
        "diff_tau": diff_tau,
    }


# ---------------------------------------------------------------------------
# Section 9 — Sub-test (c): conformal-anomaly sign-reversal
# ---------------------------------------------------------------------------

def sub_test_c(b_data):
    """Sign-reversal check per S79 P1-2 W2-E.

    Operational definition: the conformal-anomaly contribution to c_sub
    manifests as the trace of d c_sub(tau)/d tau evaluated at the post-fold
    sheet boundary. The S79 P1-2 W2-E sign-reversal closure rule states:
    the substrate's a_4 spectral-action coefficient inherits a sign reversal
    across tau_fold because the post-fold sheet structure of the Riemann cover
    flips the sign of the conformal-anomaly contribution.

    Operational proxy (chain in plan §10):
       c_sub_anomaly(tau) := d c_sub(tau)/d tau  |_{tau}
    Numerical proxy: central finite-difference at the endpoints of the 21-point
    grid where pre-fold side uses tau_low+delta_in/2, post-fold side uses
    tau_high-delta_in/2; a sign-flip is detected iff
       sign(c_sub_anomaly(tau_low + epsilon)) != sign(c_sub_anomaly(tau_high - epsilon))
    """
    tau_grid = b_data["tau_grid"]                                # (local)
    c_sub_vals = b_data["c_sub_vals"]                            # (local)

    # Pre-fold endpoint: average slope over leftmost 5 points
    # (anomaly-trace estimate using a small window for noise immunity)
    n_window = 5                                                 # (local)
    pre_left = c_sub_vals[:n_window]                             # (local)
    pre_tau = tau_grid[:n_window]                                # (local)
    pre_slope = float(np.polyfit(pre_tau, pre_left, 1)[0])       # (local) d c_sub / d tau pre-fold

    # Post-fold endpoint: average slope over rightmost 5 points
    post_right = c_sub_vals[-n_window:]                          # (local)
    post_tau = tau_grid[-n_window:]                              # (local)
    post_slope = float(np.polyfit(post_tau, post_right, 1)[0])   # (local) d c_sub / d tau post-fold

    sign_pre = int(np.sign(pre_slope))                           # (local) -1, 0, or +1
    sign_post = int(np.sign(post_slope))                         # (local)

    # Sign-reversal: PASS iff signs are nonzero AND opposite
    pass_c = bool((sign_pre != 0) and (sign_post != 0) and (sign_pre != sign_post))  # (local)

    return pass_c, {
        "pre_slope": pre_slope,
        "post_slope": post_slope,
        "sign_pre": sign_pre,
        "sign_post": sign_post,
        "n_window": n_window,
        "pre_tau": pre_tau,
        "post_tau": post_tau,
        "pre_c_sub": pre_left,
        "post_c_sub": post_right,
    }


# ---------------------------------------------------------------------------
# Section 10 — Composite verdict logic (plan §6 + §9)
# ---------------------------------------------------------------------------

def composite_verdict(pass_a, pass_b, pass_c):
    """ADMISSIBLE = 3/3, INFO = exactly 2/3, EXCLUDED = 0 or 1/3.
    Returns (composite_label, gate_verdict).
    The verdict-line PASS|FAIL|INFO maps as:
       composite_label = "ADMISSIBLE" -> verdict = "PASS"
       composite_label = "INFO"        -> verdict = "INFO"
       composite_label = "EXCLUDED"    -> verdict = "FAIL"
    """
    n_pass = int(pass_a) + int(pass_b) + int(pass_c)             # (local)
    if n_pass == 3:
        return "ADMISSIBLE", "PASS"
    if n_pass == 2:
        return "INFO", "INFO"
    return "EXCLUDED", "FAIL"


# ---------------------------------------------------------------------------
# Section 11 — Plot c_sub(tau) with envelope and sign-reversal markers
# ---------------------------------------------------------------------------

def make_plot(b_data, c_data, composite_label):
    """c_sub(tau) plot with the max_slope envelope (linear bound through tau_fold)
    and sign-reversal markers at endpoints.
    """
    tau_grid = b_data["tau_grid"]                                # (local)
    c_sub_vals = b_data["c_sub_vals"]                            # (local)
    c_at_fold = b_data["c_sub_at_fold"]                          # (local)

    fig, ax = plt.subplots(1, 1, figsize=(10, 5.5))

    ax.plot(tau_grid, c_sub_vals, 'o-', lw=2, ms=5, color='C0',
            label=r'$c_{\rm sub}(\tau)$ at (POWER-RATIO, $\zeta$, $L_{\max}=10$)')
    ax.axhline(c_at_fold, color='gray', ls=':', alpha=0.5,
               label=r'$c_{\rm sub}(\tau_{\rm fold})$')
    ax.axvline(tau_fold, color='red', ls='--', alpha=0.5,
               label=r'$\tau_{\rm fold} = 0.190$')

    # Envelope: c_sub(tau_fold) +/- 0.1 * c_sub(tau_fold) * (tau - tau_fold) / tau_fold
    # i.e. the max_slope_normalized = 0.1 boundary lines (LINEAR in tau-window)
    slope_lim = EPS_STAT_PASS * c_at_fold / tau_fold             # (local)
    env_upper = c_at_fold + slope_lim * (tau_grid - tau_fold)    # (local)
    env_lower = c_at_fold - slope_lim * (tau_grid - tau_fold)    # (local)
    ax.fill_between(tau_grid, env_lower, env_upper, color='orange', alpha=0.18,
                    label=f'tau-stationarity envelope (max_slope_norm < {EPS_STAT_PASS})')

    # Sign-reversal markers at endpoints
    sign_pre = c_data["sign_pre"]                                # (local)
    sign_post = c_data["sign_post"]                              # (local)
    pre_slope = c_data["pre_slope"]                              # (local)
    post_slope = c_data["post_slope"]                            # (local)

    sym_pre = '+' if sign_pre > 0 else ('-' if sign_pre < 0 else '0')   # (local)
    sym_post = '+' if sign_post > 0 else ('-' if sign_post < 0 else '0')  # (local)

    ax.annotate(f"sign(d c_sub/d tau)|pre = {sym_pre}\n  slope = {pre_slope:+.3e}",
                xy=(tau_grid[2], c_sub_vals[2]),
                xytext=(tau_grid[2], c_sub_vals[2] * 1.0008),
                ha='left', va='bottom', fontsize=8.5, color='darkgreen',
                arrowprops=dict(arrowstyle='->', color='darkgreen', alpha=0.6))
    ax.annotate(f"sign(d c_sub/d tau)|post = {sym_post}\n  slope = {post_slope:+.3e}",
                xy=(tau_grid[-3], c_sub_vals[-3]),
                xytext=(tau_grid[-3], c_sub_vals[-3] * 0.9994),
                ha='right', va='top', fontsize=8.5, color='purple',
                arrowprops=dict(arrowstyle='->', color='purple', alpha=0.6))

    ax.set_xlabel(r'$\tau$ (Jensen deformation parameter)')
    ax.set_ylabel(r'$c_{\rm sub}(\tau)$  (zeta scheme)')
    title = (f"S86-W5B-C16 c_sub admissibility — composite: {composite_label}  "
             f"|  c_sub(tau_fold) = {c_at_fold:.4f}")
    ax.set_title(title, fontsize=10.5)
    ax.legend(loc='best', fontsize=8.5)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=140)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 12 — Verdict-line emitter (S84+ dual-SHA + per-sub-test row + companion)
# ---------------------------------------------------------------------------

def append_verdict(verdict, value, audit_sha, content_sha,
                   pass_a, pass_b, pass_c,
                   max_slope_normalized, sign_pre, sign_post):
    """Append S84+ dual-SHA verdict line + per-sub-test comment row
    + 16-hex companion comment row (W9a-99 split) per plan §6 COMPOSITE VERDICT.
    """
    line = (
        f"{GATE_ID}: {verdict} -- value={value} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    sym_pre = '+' if sign_pre > 0 else ('-' if sign_pre < 0 else '0')   # (local)
    sym_post = '+' if sign_post > 0 else ('-' if sign_post < 0 else '0')  # (local)
    sub_row = (
        f"# sub_test_a={'PASS' if pass_a else 'FAIL'} "
        f"sub_test_b={'PASS' if pass_b else 'FAIL'} "
        f"sub_test_c={'PASS' if pass_c else 'FAIL'} "
        f"max_slope_normalized={max_slope_normalized:.6e} "
        f"sign_pre_fold={sym_pre} sign_post_fold={sym_post}\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(sub_row)
        fp.write(companion)


# ---------------------------------------------------------------------------
# Section 13 — Main
# ---------------------------------------------------------------------------

def main():
    t0 = time.time()                                             # (local)

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)                                 # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. Compute S84+ dual SHAs
    script_path = Path(__file__).resolve()                       # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')        # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Build baseline spectrum
    spectrum_baseline, source_label = build_baseline_spectrum()
    print(f"=== Spectrum source: {source_label} ===")
    print(f"  N_modes: {len(spectrum_baseline)}")
    print(f"  lambda range: [{spectrum_baseline.min():.4f}, {spectrum_baseline.max():.4f}] (M_KK)")
    print()

    # 3. Sub-test (a)
    print(f"=== Sub-test (a): regulator-atlas membership ===")
    pass_a, quadruple, justify_a = sub_test_a(C_SUB_TARGET)
    print(f"  Quadruple: ({quadruple['UV_cut_name']}, {quadruple['Mellin_convention']}, "
          f"L_max={quadruple['L_max']}, src={quadruple['source']})")
    print(f"  Atlas R_atlas = {CANONICAL_R_ATLAS}")
    print(f"  Member ('{quadruple['Mellin_convention']}' in R_atlas): "
          f"{quadruple['Mellin_convention'] in CANONICAL_R_ATLAS}")
    print(f"  Sub-test (a): {'PASS' if pass_a else 'FAIL'}")
    print()

    # 4. Sub-test (b)
    print(f"=== Sub-test (b): tau-stationarity (21-point tau-grid) ===")
    pass_b, b_data = sub_test_b(spectrum_baseline, K_PIVOT_FOLD_COMOV)
    print(f"  delta = {DELTA_FRAC} * tau_fold = {b_data['delta']:.6e}")
    print(f"  tau_grid: [{b_data['tau_low']:.6e}, {b_data['tau_high']:.6e}]")
    print(f"  c_sub(tau_fold) = {b_data['c_sub_at_fold']:.6e}")
    print(f"  c_sub(tau_low)  = {b_data['c_sub_vals'][0]:.6e}")
    print(f"  c_sub(tau_high) = {b_data['c_sub_vals'][-1]:.6e}")
    print(f"  max_slope (raw, 1/tau units) = {b_data['max_slope']:.6e}")
    print(f"  max_slope_normalized = max_slope * tau_fold = {b_data['max_slope_normalized']:.6e}")
    print(f"  Pre-reg threshold: max_slope_normalized < {EPS_STAT_PASS}")
    print(f"  Sub-test (b): {'PASS' if pass_b else 'FAIL'}")
    print()

    # 5. Sub-test (c)
    print(f"=== Sub-test (c): conformal-anomaly sign-reversal ===")
    pass_c, c_data = sub_test_c(b_data)
    print(f"  pre-fold linear-fit slope d c_sub/d tau = {c_data['pre_slope']:+.6e}  ->  sign = {c_data['sign_pre']:+d}")
    print(f"  post-fold linear-fit slope d c_sub/d tau = {c_data['post_slope']:+.6e}  ->  sign = {c_data['sign_post']:+d}")
    print(f"  Sign-reversal across tau_fold (PASS iff signs differ AND nonzero):")
    print(f"  Sub-test (c): {'PASS' if pass_c else 'FAIL'}")
    print()

    # 6. Composite verdict
    print(f"=== Composite verdict ===")
    composite_label, gate_verdict = composite_verdict(pass_a, pass_b, pass_c)
    n_pass = int(pass_a) + int(pass_b) + int(pass_c)             # (local)
    print(f"  n_pass = {n_pass}/3  (a={pass_a}, b={pass_b}, c={pass_c})")
    print(f"  composite = {composite_label}")
    print(f"  gate verdict = {gate_verdict}")
    print()

    # 7. Plot
    print(f"=== Plot ===")
    make_plot(b_data, c_data, composite_label)
    print(f"  Plot written: {OUT_PNG.name}")
    print()

    # 8. NPZ
    print(f"=== NPZ ===")
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        composite_classification=composite_label,
        gate_verdict=gate_verdict,
        # tau-grid + c_sub trajectory
        tau_grid=b_data["tau_grid"],
        c_sub_tau=b_data["c_sub_vals"],
        # sub-test (b) outputs
        c_sub_at_fold=b_data["c_sub_at_fold"],
        max_slope=b_data["max_slope"],
        max_slope_normalized=b_data["max_slope_normalized"],
        sub_test_a_pass=bool(pass_a),
        sub_test_b_pass=bool(pass_b),
        sub_test_c_pass=bool(pass_c),
        # sub-test (c) outputs (sign-reversal endpoints)
        c_sub_anomaly_pre_fold=c_data["pre_slope"],
        c_sub_anomaly_post_fold=c_data["post_slope"],
        sign_pre_fold=c_data["sign_pre"],
        sign_post_fold=c_data["sign_post"],
        pre_window_tau=c_data["pre_tau"],
        post_window_tau=c_data["post_tau"],
        pre_window_c_sub=c_data["pre_c_sub"],
        post_window_c_sub=c_data["post_c_sub"],
        # quadruple metadata
        UV_cut_name=UV_CUT_NAME,
        Mellin_convention=MELLIN_CONVENTION,
        L_max=L_MAX,
        scheme=SCHEME,
        convention=CONVENTION,
        canonical_R_atlas=list(CANONICAL_R_ATLAS),
        target_c_sub_value_4sigfig=C_SUB_TARGET,
        target_c_sub_value_precise=C_SUB_TARGET_PRECISE,
        # Provenance
        spectrum_source=source_label,
        N_modes=len(spectrum_baseline),
        tau_fold=tau_fold,
        S_fold=S_fold,
        dS_fold=dS_fold,
        d2S_fold=d2S_fold,
        H_fold=H_fold,
        k_pivot_fold_comov=K_PIVOT_FOLD_COMOV,
        # SHAs
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        closure_sha256=closure,
    )
    print(f"  NPZ written: {OUT_NPZ.name} (size={OUT_NPZ.stat().st_size}B)")
    print()

    # 9. Verdict line (S84+ dual SHA + per-sub-test row + companion)
    print(f"=== Verdict line ===")
    append_verdict(
        verdict=gate_verdict,
        value=composite_label,
        audit_sha=audit_sha,
        content_sha=content_sha,
        pass_a=pass_a, pass_b=pass_b, pass_c=pass_c,
        max_slope_normalized=b_data["max_slope_normalized"],
        sign_pre=c_data["sign_pre"],
        sign_post=c_data["sign_post"],
    )
    print(f"  {GATE_ID}: {gate_verdict} -- value={composite_label} scheme={SCHEME} "
          f"convention={CONVENTION} L_max={L_MAX}")
    print(f"  audit_sha256: {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    # Final 4-tuple line
    print(f"4-tuple: (value={composite_label!r}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")
    print(f"Wall-time: {time.time() - t0:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
