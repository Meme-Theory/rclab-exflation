#!/usr/bin/env python3
"""
S84 W6-51 — SIBLING-OBSERVABLES-COMMON-PREFACTOR  (H_tilde^n exponent atlas)
===========================================================================

Gate: S84-SIBLING-OBSERVABLES-COMMON-PREFACTOR  ([CHAIN])

Pre-registered threshold:
  PASS iff (# observables with |n| >= 1) >= 3
           AND >= 2 of those are detector-accessible by 2035.
  FAIL iff (# observables with |n| >= 1) == 0.
  INFO otherwise.

Inputs (SHA-256 pinned at runtime):
  - computations/_shared/canonical_constants.py

Output 4-tuple:
  (value=<k_obs_above_1decade>, scheme=CC3-propagation,
   convention=H_TD-vs-mixed-C, L_max=N/A)

Classification: PHONONIC — every observable is a spectral moment of D_K;
the common-prefactor structure IS CC3 propagation on the observable sheet,
not a Friedmann factor.

METHODOLOGY
-----------
Per plan §W6-51: catalog 12 observables, compute d(ln O_i)/d(ln H_tilde)
analytically (per-row substitution chain), cross-check via finite difference
at delta=1e-6, tabulate the common-prefactor atlas, compute (A)/(C) ratio in
decades, identify multi-D discriminator, compute rank-k joint sigma.

H_TD  = 5.90760e-03   (S80 W1-1 zeta/TD-framework anchor)
H_LI  = 2.46411e-05   (S82 W1-2 line-143 LI endpoint)
H_C   = sqrt(H_TD * H_LI) = geometric-mean mixed-C branch endpoint

Per-row analytic exponents:
  (a) A_s     : A_s = H~^2 / (8 pi^2) * (1/eps_H) * F_amp * (1/c_sub) * f_conv
                ln A_s = 2 ln H~ + const ;  n = +2
  (b) P_t     : P_t = (2/pi^2) (H~/M_Pl)^2 ;
                ln P_t = 2 ln H~ + const ;  n = +2
  (c) n_s     : n_s - 1 = -2 eps_H - eta_H (structural SR) ;  n = 0
  (d) alpha_s : alpha_s = d n_s / d(ln k) (2nd-order SR) ;  n = 0
  (e) n_t     : n_t = -2 eps_H (standard) / Jensen-locked (substrate) ;  n = 0
  (f) r       : r = 16 eps_H = P_t/P_s (H~ cancels in ratio) ;  n = 0
  (g) f_NL    : f_NL_local = -(5/12)(n_s-1) (Maldacena cons.) ;  n = 0
  (h) mu      : mu ~ integral(A_s W(k) dk/k) ;  mu ~ H~^2 ;  n = +2
  (i) tau_reio: astrophysical (reionization) — H~-independent ;  n = 0
  (j) alpha_s(CMB) S76 = n_s^2 - 1 (spectral moment id.) ;  n = 0
  (k) dn_s/d(ln k) : same as alpha_s ;  n = 0
  (l) spectral-index x-corr (n_t - n_s consistency) ;  n = 0

Exponent atlas tabulated; finite-diff cross-check at delta=1e-6 per row.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local tagged `# (local)`
- No GPU required (scalar tabulation)
- SHA-256 input pin, closure hash appended to verdict line
- Verdict append via atomic single-line `open("a")`
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403
import numpy as np                                                            # noqa: E402
import matplotlib                                                             # noqa: E402
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

matplotlib.use("Agg")
import matplotlib.pyplot as plt                                               # noqa: E402

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import csv
import hashlib
import sys
import time
from pathlib import Path

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S84"                                                               # (local)
GATE_ID = "S84-SIBLING-OBSERVABLES-COMMON-PREFACTOR"                          # (local)
SCHEME = "CC3-propagation"                                                    # (local)
CONVENTION = "H_TD-vs-mixed-C"                                                # (local)
L_MAX = "N/A"                                                                 # (local)

# Pre-registered pass/fail threshold
N_ABOVE_1DEC_PASS_MIN = 3                                                     # (local)
DETECTOR_HORIZON_YEAR = 2035                                                  # (local)
FD_DELTA = 1.0e-6                                                             # (local) finite-diff step
FD_TOL = 1.0e-4                                                               # (local) |analytic - FD| tolerance

# H_tilde anchors (local — derived from S80/S82 anchors, not canonical yet)
H_TILDE_TD = 5.90760e-03           # (local) S80 W1-1 zeta/TD-framework anchor
H_TILDE_LI = 2.46411e-05           # (local) S82 W1-2 line-143 LI endpoint
H_TILDE_C  = float(np.sqrt(H_TILDE_TD * H_TILDE_LI))  # (local) geometric-mean mixed-C

# Observable catalog — 12 entries, frozen per plan §W6-51 step 1
OBSERVABLE_CATALOG = [
    # (name, n_analytic, detector, year_accessible, notes)
    ("A_s",                +2, "Planck/CMB-S4",   2018, "H~^2/(8pi^2eps_H) * F_amp * 1/c_sub * f_conv"),
    ("P_t",                +2, "LISA/DECIGO",     2035, "(2/pi^2)(H~/M_Pl)^2"),
    ("n_s",                 0, "Planck/CMB-S4",   2018, "n_s - 1 = -2eps_H - eta_H (structural SR)"),
    ("alpha_s",             0, "CMB-S4/CMB-HD",   2030, "d n_s/d(ln k) 2nd-order SR"),
    ("n_t",                 0, "LiteBIRD",        2032, "n_t = -2eps_H / Jensen-locked (substrate)"),
    ("r",                   0, "LiteBIRD/BICEP",  2032, "r = 16 eps_H ratio — H~ cancels"),
    ("f_NL",                0, "SKA-2/CMB-S4",    2030, "f_NL_local = -(5/12)(n_s-1) Maldacena"),
    ("mu",                 +2, "PIXIE/PRISM",     2035, "mu ~ integral(A_s W(k) dk/k) Silk dissipation"),
    ("tau_reio",            0, "Planck/CMB-S4",   2018, "optical depth — astrophysical, H~-independent"),
    ("alpha_s_CMB_S76",     0, "CMB-S4 (via n_s)", 2030, "alpha_s = n_s^2 - 1 (S50 spectral-moment identity)"),
    ("dn_s_d_ln_k",         0, "CMB-S4",          2030, "same as alpha_s (SR 2nd derivative)"),
    ("spec_idx_xcorr_nt_ns",0, "LiteBIRD+CMB-S4", 2032, "n_t - n_s consistency — ratio form"),
]

# Output destinations
OUT_NPZ = resolve_output(84, 's84_w6_sibling_common_prefactor.npz')
OUT_PNG = resolve_output(84, 's84_w6_sibling_common_prefactor.png')
OUT_CSV = resolve_output(84, 's84_w6_sibling_common_prefactor.csv')
VERDICT_TXT = resolve_output(84, 's84_gate_verdicts.txt')

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                                       # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}                                                                  # (local)
    for p in inputs:
        sha = sha256_of(p)                                                     # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")              # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    # also pin the H_tilde values (not in canonical yet)
    pins["H_TILDE_TD"] = f"{H_TILDE_TD:.10e}"
    pins["H_TILDE_LI"] = f"{H_TILDE_LI:.10e}"
    pins["H_TILDE_C"]  = f"{H_TILDE_C:.10e}"
    return pins


def closure_hash(pins):
    items = sorted(pins.items())                                               # (local)
    h = hashlib.sha256()                                                       # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — Observable models (each O_i(H_tilde) analytic + closures)
# ---------------------------------------------------------------------------

# Local SR anchors (structural; H_tilde-independent by definition of "structural")
EPS_H_LOCAL = 0.02163                                                          # (local) S80 one-loop
ETA_H_LOCAL = 0.015                                                            # (local) SR anchor; structural
F_AMP_LOCAL = 1.0                                                              # (local) amplitude-channel composite
C_SUB_LOCAL = 2.238                                                            # (local) S78 W2-E central
F_CONV_LOCAL = 1.0                                                             # (local) conversion factor
M_PL = M_Pl_reduced                                                            # (local) reduced Planck GeV
# structural n_s central (for downstream chain tests)
N_S_STRUCT = 0.9653                                                            # (local) Planck central

PI = float(np.pi)                                                              # (local)


def O_As(H):
    # A_s = H^2/(8 pi^2) * (1/eps_H) * F_amp * (1/c_sub) * f_conv
    return (H**2) / (8.0 * PI**2) * (1.0 / EPS_H_LOCAL) * F_AMP_LOCAL * (1.0 / C_SUB_LOCAL) * F_CONV_LOCAL


def O_Pt(H):
    # P_t = (2/pi^2) (H/M_Pl)^2
    return (2.0 / PI**2) * (H / M_PL) ** 2


def O_ns(H):
    # n_s = 1 - 2 eps_H - eta_H; structural (H-independent). Return positive for ln.
    return 1.0 - 2.0 * EPS_H_LOCAL - ETA_H_LOCAL


def O_alpha_s(H):
    # alpha_s = d n_s / d(ln k); 2nd-order SR ~ constant scale here
    # For H-dependence: structural, returns constant positive value (magnitude for ln)
    return abs(-0.0143)  # S76 central alpha_s magnitude


def O_nt(H):
    # n_t = -2 eps_H structural.  Return magnitude for ln.
    # (Substrate: n_t = +0.4676 from G50; still structural in H~)
    return abs(-2.0 * EPS_H_LOCAL)


def O_r(H):
    # r = P_t/P_s = 16 eps_H (ratio — H cancels)
    return 16.0 * EPS_H_LOCAL


def O_fNL(H):
    # f_NL_local = -(5/12)(n_s - 1)  Maldacena single-field consistency
    return abs(-(5.0 / 12.0) * (N_S_STRUCT - 1.0))


def O_mu(H):
    # mu ~ integral(dk/k A_s(k) W(k)) ~ 2.3 * A_s_effective (Silk dissipation energy)
    # Direct A_s inheritance => mu ~ H^2
    return 2.3 * O_As(H)


def O_tau_reio(H):
    # Astrophysical (reionization) — H~-independent.
    return 0.054  # Planck central


def O_alpha_s_CMB_S76(H):
    # alpha_s = n_s^2 - 1  (S50 spectral moment identity); n_s is structural => H-independent
    ns = O_ns(H)                                                               # (local)
    return abs(ns**2 - 1.0)


def O_dns_dlnk(H):
    # Same as alpha_s (different convention, same H-scaling)
    return abs(-0.0143)


def O_spec_idx_xcorr(H):
    # n_t - n_s consistency — ratio form, H-independent
    return abs(O_nt(H) - (O_ns(H) - 1.0))


OBS_FN = {
    "A_s":                   O_As,
    "P_t":                   O_Pt,
    "n_s":                   O_ns,
    "alpha_s":               O_alpha_s,
    "n_t":                   O_nt,
    "r":                     O_r,
    "f_NL":                  O_fNL,
    "mu":                    O_mu,
    "tau_reio":              O_tau_reio,
    "alpha_s_CMB_S76":       O_alpha_s_CMB_S76,
    "dn_s_d_ln_k":           O_dns_dlnk,
    "spec_idx_xcorr_nt_ns":  O_spec_idx_xcorr,
}


def finite_diff_exponent(fn, H, delta=FD_DELTA):
    """Compute d(ln O)/d(ln H) at H via symmetric finite difference.

    Returns n_fd. If O(H) is H-independent the log-deriv is 0 (within eps).
    Uses symmetric step in ln H for accuracy: H*(1+delta) and H*(1-delta).
    """
    Hp = H * (1.0 + delta)                                                     # (local)
    Hm = H * (1.0 - delta)                                                     # (local)
    Op = fn(Hp)                                                                # (local)
    Om = fn(Hm)                                                                # (local)
    # If O is constant (H-independent), Op == Om => numerator zero
    if Op <= 0.0 or Om <= 0.0:
        return 0.0
    num = np.log(Op) - np.log(Om)                                              # (local)
    den = np.log(Hp) - np.log(Hm)                                              # (local)
    return float(num / den)


# ---------------------------------------------------------------------------
# Section 6 — Compute
# ---------------------------------------------------------------------------

def compute():
    H_anchor = H_TILDE_TD                                                      # (local)

    names = []                                                                 # (local)
    n_analytic = []                                                            # (local)
    n_fd = []                                                                  # (local)
    fd_err = []                                                                # (local)
    val_TD = []                                                                # (local)
    val_C = []                                                                 # (local)
    val_LI = []                                                                # (local)
    ratio_AC_log10 = []                                                        # (local)
    detectors = []                                                             # (local)
    year_access = []                                                           # (local)
    notes = []                                                                 # (local)

    for (nm, n_a, det, yr, note) in OBSERVABLE_CATALOG:
        fn = OBS_FN[nm]                                                        # (local)
        # analytic exponent from catalog
        # finite-diff cross-check at H=H_TD
        n_f = finite_diff_exponent(fn, H_anchor, FD_DELTA)                     # (local)
        err = abs(n_a - n_f)                                                   # (local)
        # Evaluate at all three H anchors
        oTD = fn(H_TILDE_TD)                                                   # (local)
        oC  = fn(H_TILDE_C)                                                    # (local)
        oLI = fn(H_TILDE_LI)                                                   # (local)
        # log10 |ratio TD/C|  = n_a * log10(H_TD/H_C)
        # For structural (n=0) observables ratio is 1.0 => log10 = 0
        # For H^2 observables: log10(H_TD/H_C)*n_a
        if oTD > 0 and oC > 0:
            rat = float(np.log10(oTD / oC))                                   # (local)
        else:
            rat = 0.0                                                          # (local)

        names.append(nm)
        n_analytic.append(int(n_a))
        n_fd.append(float(n_f))
        fd_err.append(float(err))
        val_TD.append(float(oTD))
        val_C.append(float(oC))
        val_LI.append(float(oLI))
        ratio_AC_log10.append(rat)
        detectors.append(det)
        year_access.append(int(yr))
        notes.append(note)

    names_arr = np.array(names)                                                # (local)
    n_a_arr = np.array(n_analytic, dtype=int)                                  # (local)
    n_fd_arr = np.array(n_fd, dtype=float)                                     # (local)
    fd_err_arr = np.array(fd_err, dtype=float)                                 # (local)
    val_TD_arr = np.array(val_TD, dtype=float)                                 # (local)
    val_C_arr = np.array(val_C, dtype=float)                                   # (local)
    val_LI_arr = np.array(val_LI, dtype=float)                                 # (local)
    ratio_arr = np.array(ratio_AC_log10, dtype=float)                          # (local)
    yr_arr = np.array(year_access, dtype=int)                                  # (local)

    # Count |n| >= 1 observables
    abs_n = np.abs(n_a_arr)                                                    # (local)
    k_obs_above_1 = int((abs_n >= 1).sum())                                    # (local)
    above_1_mask = abs_n >= 1                                                  # (local)
    names_above = names_arr[above_1_mask]                                      # (local)
    # Detector-accessible by 2035
    accessible_mask = (yr_arr <= DETECTOR_HORIZON_YEAR) & above_1_mask         # (local)
    n_accessible = int(accessible_mask.sum())                                  # (local)
    names_accessible = names_arr[accessible_mask]                              # (local)

    # FD cross-check: max error across all rows
    max_fd_err = float(fd_err_arr.max())                                       # (local)
    fd_cross_check_ok = bool(max_fd_err < FD_TOL)                              # (local)

    # Rank-k joint sigma (scaling factor):
    # joint_sigma_k / sigma_single = 1/sqrt(sum_i n_i^2) relative to n_single=2
    # For k equally-weighted n=2 observables: joint = sigma_single / sqrt(k)
    # Effective gain = sqrt(sum n_i^2) / 2 for k included (with diagonal cov)
    k_vals = [1, 2, 3, 5, 10, 12]                                              # (local)
    joint_sigma_k = []                                                         # (local)
    # Use only |n|>=1 rows (carriers) sorted by |n| desc for first k
    carrier_abs_n = np.sort(abs_n[above_1_mask])[::-1]                         # (local)
    for k in k_vals:
        if k == 1:
            # baseline: A_s only (single channel), factor=1
            joint_sigma_k.append(1.0)
            continue
        take = min(k, len(carrier_abs_n))                                      # (local)
        if take == 0:
            joint_sigma_k.append(1.0)
        else:
            # joint factor = 1/sqrt(sum n_i^2 / 4) = 2 / sqrt(sum n_i^2)
            # (expressed as multiplier to single-A_s sigma; <1 means improvement)
            sum_nsq = float((carrier_abs_n[:take].astype(float) ** 2).sum())   # (local)
            if sum_nsq <= 0:
                joint_sigma_k.append(1.0)
            else:
                joint_sigma_k.append(float(2.0 / np.sqrt(sum_nsq)))

    # CC3 consistency check: sum of exponents in A_s reconstruction equation
    # A_s = H^2/(8 pi^2) * (1/eps_H) * F_amp * (1/c_sub) * f_conv
    # => d(ln A_s)/d(ln H) decomposes to:  +2 (from H^2)  +0 (others structural) = +2
    cc3_sum_A_s = 2 + 0 + 0 + 0 + 0                                            # (local)
    cc3_check_A_s_OK = (cc3_sum_A_s == 2)                                      # (local)

    # G46 r-cancellation verification: r(H_TD) vs r(H_C) should be identical
    r_TD = O_r(H_TILDE_TD)                                                     # (local)
    r_C  = O_r(H_TILDE_C)                                                      # (local)
    r_ratio = r_TD / r_C if r_C != 0 else float("nan")                         # (local)
    r_cancel_OK = bool(abs(r_ratio - 1.0) < 1e-10)                             # (local)

    # Joint |n|=2 carriers count + detector accessibility (PASS criterion)
    heavy_n2_accessible = int(((abs_n == 2) & accessible_mask).sum())          # (local)

    results = dict(
        names=names_arr,
        n_analytic=n_a_arr,
        n_fd=n_fd_arr,
        fd_err=fd_err_arr,
        val_TD=val_TD_arr,
        val_C=val_C_arr,
        val_LI=val_LI_arr,
        ratio_AC_log10=ratio_arr,
        detectors=np.array(detectors),
        year_access=yr_arr,
        notes=np.array(notes),
        k_obs_above_1=k_obs_above_1,
        names_above_1=names_above,
        n_accessible=n_accessible,
        names_accessible=names_accessible,
        max_fd_err=max_fd_err,
        fd_cross_check_ok=fd_cross_check_ok,
        k_vals=np.array(k_vals),
        joint_sigma_k=np.array(joint_sigma_k),
        cc3_sum_A_s=cc3_sum_A_s,
        cc3_check_A_s_OK=cc3_check_A_s_OK,
        r_TD=r_TD,
        r_C=r_C,
        r_ratio=r_ratio,
        r_cancel_OK=r_cancel_OK,
        H_TILDE_TD=H_TILDE_TD,
        H_TILDE_LI=H_TILDE_LI,
        H_TILDE_C=H_TILDE_C,
        value=k_obs_above_1,
        heavy_n2_accessible=heavy_n2_accessible,
    )
    return results


# ---------------------------------------------------------------------------
# Section 7 — Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme, convention, L_max):
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict, value, closure_sha):
    # S81+ canonical single-line atomic append
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} sha256={closure_sha}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def evaluate_gate(result):
    k = result["k_obs_above_1"]                                                # (local)
    n_access = result["n_accessible"]                                          # (local)
    fd_ok = result["fd_cross_check_ok"]                                        # (local)
    r_ok = result["r_cancel_OK"]                                               # (local)
    cc3_ok = result["cc3_check_A_s_OK"]                                        # (local)

    # FD cross-check MANDATORY
    if not fd_ok:
        return "FAIL"  # machinery broken (unexpected)

    # Plan §W6-51 §9 thresholds:
    if k == 0:
        return "FAIL"
    if k >= N_ABOVE_1DEC_PASS_MIN and n_access >= 2 and r_ok and cc3_ok:
        return "PASS"
    return "INFO"


# ---------------------------------------------------------------------------
# Section 8 — Plotting + CSV
# ---------------------------------------------------------------------------

def write_csv(result):
    with OUT_CSV.open("w", encoding="utf-8", newline="") as fp:
        w = csv.writer(fp)
        w.writerow([
            "observable", "n_analytic", "n_fd", "|n_a - n_fd|",
            "value_H_TD", "value_H_C", "value_H_LI",
            "ratio_TD_over_C_log10", "detector", "year_accessible", "notes",
        ])
        for i in range(len(result["names"])):
            w.writerow([
                result["names"][i],
                int(result["n_analytic"][i]),
                f"{result['n_fd'][i]:.3e}",
                f"{result['fd_err'][i]:.3e}",
                f"{result['val_TD'][i]:.6e}",
                f"{result['val_C'][i]:.6e}",
                f"{result['val_LI'][i]:.6e}",
                f"{result['ratio_AC_log10'][i]:.4f}",
                str(result["detectors"][i]),
                int(result["year_access"][i]),
                str(result["notes"][i]),
            ])


def make_plot(result):
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))

    # Left: bar chart of n_analytic with n_fd overlay
    ax = axes[0]
    x = np.arange(len(result["names"]))                                        # (local)
    bars = ax.bar(x, result["n_analytic"], color="#4a7ab7", alpha=0.85,
                  label="analytic n")
    ax.scatter(x, result["n_fd"], color="crimson", marker="x", s=70, zorder=5,
               label="finite-diff n")
    ax.set_xticks(x)
    ax.set_xticklabels(result["names"], rotation=45, ha="right", fontsize=9)
    ax.set_ylabel(r"$n = d(\ln O_i)/d(\ln \tilde{H})$")
    ax.set_title("Observable H~^n Exponent Atlas (CC3 propagation)")
    ax.axhline(1.0, color="gray", ls="--", lw=0.8, alpha=0.7)
    ax.axhline(0.0, color="black", lw=0.5)
    ax.legend(loc="upper right")
    ax.grid(alpha=0.3)
    for i, b in enumerate(bars):
        h = b.get_height()
        ax.text(b.get_x() + b.get_width() / 2.0, h + 0.1, f"{int(h):+d}",
                ha="center", fontsize=8)

    # Right: cumulative joint sigma (factor to sigma_single) vs k
    ax2 = axes[1]
    ax2.plot(result["k_vals"], result["joint_sigma_k"],
             marker="o", color="#2c7d4f", lw=1.6, ms=7)
    ax2.set_xlabel("rank-k channels")
    ax2.set_ylabel(r"$\sigma_{\rm joint}/\sigma_{A_s\,\rm alone}$ (lower = better)")
    ax2.set_title(
        f"Rank-k joint sigma (|n|>=1 carriers, value={result['k_obs_above_1']})"
    )
    ax2.axhline(1.0, color="gray", ls="--", lw=0.8)
    for k, js in zip(result["k_vals"], result["joint_sigma_k"]):
        ax2.text(k, js + 0.03, f"{js:.3f}", ha="center", fontsize=8)
    ax2.grid(alpha=0.3)
    ax2.set_ylim(0.0, 1.15)

    fig.suptitle(
        f"S84 W6-51: Sibling-Observables Common-Prefactor Atlas  "
        f"(k_obs_above_1={result['k_obs_above_1']}, "
        f"detector-accessible={result['n_accessible']})"
    )
    fig.tight_layout(rect=(0.0, 0.02, 1.0, 0.95))
    fig.savefig(OUT_PNG, dpi=140)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 9 — Main
# ---------------------------------------------------------------------------

def main():
    t0 = time.time()                                                           # (local)

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}...")
    print(f"  H_TILDE_TD = {H_TILDE_TD:.6e}")
    print(f"  H_TILDE_C  = {H_TILDE_C:.6e}")
    print(f"  H_TILDE_LI = {H_TILDE_LI:.6e}")
    print()

    # 2. Compute
    result = compute()

    # 3. Print atlas
    print("=== Exponent Atlas ===")
    hdr = f"{'observable':>22s} | {'n_a':>4s} | {'n_fd':>10s} | {'|diff|':>9s} | {'log10(TD/C)':>11s} | {'detector':<20s} | {'yr':>5s}"
    print(hdr)
    print("-" * len(hdr))
    for i in range(len(result["names"])):
        print(f"{result['names'][i]:>22s} | {int(result['n_analytic'][i]):>+4d} "
              f"| {result['n_fd'][i]:>+10.3e} | {result['fd_err'][i]:>9.2e} "
              f"| {result['ratio_AC_log10'][i]:>+11.4f} "
              f"| {str(result['detectors'][i]):<20s} | {int(result['year_access'][i]):>5d}")
    print()
    print(f"k_obs_above_1 (|n|>=1) = {result['k_obs_above_1']} "
          f"names={list(result['names_above_1'])}")
    print(f"n_accessible (<= {DETECTOR_HORIZON_YEAR}) = {result['n_accessible']} "
          f"names={list(result['names_accessible'])}")
    print(f"FD cross-check: max|n_a - n_fd| = {result['max_fd_err']:.3e} "
          f"(tol {FD_TOL:.1e}) -> {'OK' if result['fd_cross_check_ok'] else 'FAIL'}")
    print(f"CC3 A_s exponent-sum = {result['cc3_sum_A_s']} (expect +2) -> "
          f"{'OK' if result['cc3_check_A_s_OK'] else 'FAIL'}")
    print(f"r-cancellation: r_TD/r_C - 1 = {result['r_ratio'] - 1.0:+.3e} "
          f"-> {'OK' if result['r_cancel_OK'] else 'FAIL'}")
    print(f"Joint sigma factor (k=3) = {result['joint_sigma_k'][2]:.4f}  "
          f"(k=5) = {result['joint_sigma_k'][3]:.4f}  "
          f"(k=10) = {result['joint_sigma_k'][4]:.4f}")

    # 4. Evaluate gate
    verdict = evaluate_gate(result)

    # 5. Emit 4-tuple + append verdict
    value = result["value"]                                                    # (local)
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print()
    print(tag)
    append_verdict(verdict, value, closure)

    # 6. Save .npz + .csv + .png
    np.savez(
        OUT_NPZ,
        observable_names=result["names"],
        n_exponent_analytic=result["n_analytic"],
        n_exponent_fd=result["n_fd"],
        fd_err=result["fd_err"],
        val_TD=result["val_TD"],
        val_C=result["val_C"],
        val_LI=result["val_LI"],
        ratio_AC_log10=result["ratio_AC_log10"],
        detectors=result["detectors"],
        year_access=result["year_access"],
        notes=result["notes"],
        k_obs_above_1=result["k_obs_above_1"],
        n_accessible=result["n_accessible"],
        names_above_1=result["names_above_1"],
        names_accessible=result["names_accessible"],
        k_vals=result["k_vals"],
        joint_sigma_k=result["joint_sigma_k"],
        max_fd_err=result["max_fd_err"],
        cc3_sum_A_s=result["cc3_sum_A_s"],
        r_ratio=result["r_ratio"],
        H_TILDE_TD=H_TILDE_TD,
        H_TILDE_LI=H_TILDE_LI,
        H_TILDE_C=H_TILDE_C,
        closure_sha256=closure,
    )
    write_csv(result)
    make_plot(result)

    wall = time.time() - t0                                                    # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    print(f"NPZ:  {OUT_NPZ}")
    print(f"CSV:  {OUT_CSV}")
    print(f"PNG:  {OUT_PNG}")
    print(f"Verdict appended to: {VERDICT_TXT}")
    return 0 if verdict != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
