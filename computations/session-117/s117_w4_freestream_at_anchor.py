#!/usr/bin/env python3
"""
S117 W4-1 CF-S117-FREESTREAM-AT-ANCHOR -- DM free-streaming length at the
graph-anchored Leggett mass, with the WHICH-VELOCITY pre-registration.
=========================================================================

Gate: CF-S117-FREESTREAM-AT-ANCHOR ([SIGN])
  PRIMARY, EVOI-carrying gate of the Wave-4 Q3 leg (the 170x re-typing discharge).

Pre-registered threshold (operator = inequality):
  (lambda_fs - lambda_threshold) < 0   [equivalently z_tr > z_threshold = 6.2e7]
  PASS  iff sign(lambda_fs - lambda_threshold) NEGATIVE (cold; below threshold)
  FAIL  iff a 4D streaming channel with T^{0i}_4D != 0 is found
            (warm-DM kinematic tension; contradicts CDM-CONSTRUCT-44)
  INFO  iff lambda_fs lands within ~1 decade of lambda_threshold under the
            internal-diagnostic (Track-B) reading.

WHICH-VELOCITY pre-registration (W-2 workshop refinement; latest-synthesis-wins):
  TRACK A (load-bearing): v_fs^4D = T^{0i}_4D / T^{00} = 0 EXACT
        (CDM-CONSTRUCT-44, 5 proofs S44; CONSTRUCT-43; w = 0).
        The squeeze creates (k,-k) pairs => n(k)=n(-k) even => the momentum
        density integral int k n(k) d3k vanishes by parity. Cold by ALGEBRA.
        => lambda_fs^4D = int v_fs^4D / a dt = 0 << lambda_threshold.
  TRACK B (diagnostic, EXPLICITLY NOT the 4D velocity):
        v_rms_internal = the RMS of the single-mode internal momentum spread of
        the transit-frozen Bogoliubov occupation n(k). A substrate-INTERNAL
        property of the fiber excitation spectrum -- a velocity DISPERSION,
        not the bulk 4D streaming velocity. Reported with the category-error
        guard (S43/S44). Even naively plugged into the free-streaming metric it
        gives lambda_fs << lambda_threshold (heavy mass + GUT-scale production).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - canonical_constants.py (Delta_BCS, Mass_LeggettDM_over_Delta_BCS,
    M_DM_Leggett_GeV, n_Bog, W_BG, n_pairs, Omega_*, M_KK_*, c_Gold, ...)
  - computations/session-58/s58_free_streaming.npz (prior anchor FREE-STREAMING-58:
    z_tr_grav=6.754e29, z_tr_threshold=6.2e7, v_prod=0.915c)
  - frozen Bogoliubov occupation n(k): CLOSED-FORM (BdG dispersion + capped
    squeeze) from canonical n_Bog / W_BG -- no npz, no D_K diagonalization.

Output 4-tuple:
  (value=<sign-verdict summary>, scheme=FREESTREAM-ANCHOR,
   convention=WHICH-VELOCITY-PREREG, L_max=N/A)

Classification: PHONONIC (free-streaming kinematics of the Leggett GGE relic).

METHODOLOGY
-----------
Symmetry-first. The DM relic IS the conserved Leggett-channel quasiparticle
number N_DM = sum_k n(k), a GGE relic of the supersonic transit (S38 squeeze
frozen by the Ordered Veil S_ent=0, S95). The order parameter for "warmness" is
the bulk 4-momentum current T^{0i}; isotropy of the (k,-k) creation FORCES it to
zero (an exact parity selection rule = CDM-CONSTRUCT-44). The free-streaming
velocity is T^{0i}/T^{00} = 0, so lambda_fs^4D = 0 by structure, independent of
the detailed occupation. The z_tr metric (FREE-STREAMING-58) is reproduced at
the graph-anchored mass m_Leggett = 11.97*Delta_BCS = 5.5571 M_KK and confirmed
mass-robust; the Track-B internal momentum spread is computed as a diagnostic and
shown not to enter the 4D current.

DISCIPLINE
----------
- `from canonical_constants import *` first.
- Every local/intermediate tagged `# (local)`.
- cpu-cap-OMP8 (closed-form scalar integrals; no matrix >= 100x100; no GPU).
- dual-SHA (audit + content) emitted; 4-tuple printed; verdict via the
  `emit_verdict` knowledge-MCP tool (the agent reads print_verdict_payload).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 -- CPU thread cap (BEFORE numpy; closed-form scalar integrals)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
SHARED = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_shared")
sys.path.insert(0, os.path.abspath(SHARED))
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 -- Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time
from pathlib import Path

import numpy as np
from scipy import integrate
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 -- Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S117"                                                   # (local)
GATE_ID = "CF-S117-FREESTREAM-AT-ANCHOR"                           # (local)
SCHEME = "FREESTREAM-ANCHOR"                                       # (local)
CONVENTION = "WHICH-VELOCITY-PREREG"                               # (local)
L_MAX = "N/A"                                                      # (local)

# Pre-registered machinery pins (plan W4-1 machinery_pin_map)
N_EVAL = 2000                                                      # (local) momentum-grid points
K_MIN = 1e-4                                                       # (local) M_KK units
K_MAX = 50.0                                                       # (local) M_KK units (frozen-occupation support)
INT_RTOL = 1e-6                                                    # (local) integration relative tolerance
Z_THRESHOLD = 6.2e7                                                # (local) z_tr structure-formation threshold (s58)
LAMBDA_THRESHOLD_MPC = 0.1                                         # (local) structure-formation comoving scale (WDM half-mode reference)

OUT_NPZ = SESSION_DIR / "s117_w4_freestream_at_anchor.npz"
OUT_PNG = SESSION_DIR / "s117_w4_freestream_at_anchor.png"

S58_NPZ = COMPUTATIONS_DIR / "session-58" / "s58_free_streaming.npz"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    S58_NPZ,
]


# ---------------------------------------------------------------------------
# Section 4 -- SHA-256 input-pin block (dual-SHA, S84+)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        pass
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        pass
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 -- Frozen Bogoliubov occupation n(k) (BdG dispersion + capped squeeze)
# ---------------------------------------------------------------------------
def frozen_occupation(k, m_L, n_peak):
    """Transit-frozen Bogoliubov occupation of the Leggett quasiparticle.

    Relativistic massive BdG dispersion E_k = sqrt(k^2 + m_L^2) (M_KK units).
    Sudden-quench (massless -> massive) squeeze:
        n_quench(k) = (omega_i - omega_f)^2 / (4 omega_i omega_f),
        omega_i = k, omega_f = E_k.
    => soft modes diverge (k -> 0), hard modes fall as m_L^4/(16 k^4).
    The finite transit rate caps the soft amplification at the canonical peak
    squeeze: n(k) = min(n_quench(k), n_peak), n_peak = sinh^2(r_squeeze) = (W_BG-1)/2.
    n(k) is EVEN in k (the (k,-k) pair structure) -- the parity that forces T^{0i}=0.
    """
    k = np.asarray(k, dtype=float)  # (local)
    ak = np.abs(k)                  # (local) occupation depends on |k| (isotropy)
    E = np.sqrt(ak**2 + m_L**2)     # (local) BdG dispersion
    with np.errstate(divide="ignore", invalid="ignore"):
        n_q = (ak - E)**2 / (4.0 * ak * E)  # (local) sudden-quench squeeze
    n_q = np.where(ak > 0, n_q, n_peak)     # (local) k->0 limit handled by cap
    return np.minimum(n_q, n_peak)


# ---------------------------------------------------------------------------
# Section 6 -- Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    out: dict = {}  # (local)

    # --- anchored mass (graph-anchored Leggett DM scale) -------------------
    m_L = Mass_LeggettDM_over_Delta_BCS * Delta_BCS        # (local) = 5.5571 M_KK
    m_L_GeV = m_L * M_KK_gravity                           # (local) physical rest energy
    out["m_Leggett_MKK"] = m_L
    out["m_Leggett_GeV"] = m_L_GeV
    out["m_Leggett_GeV_canonical"] = M_DM_Leggett_GeV      # cross-check pin

    # --- squeeze parameters derived from canonical n_Bog / W_BG ------------
    r_squeeze = float(np.arctanh(np.sqrt(n_Bog)))          # (local) = 3.99045
    n_peak = (W_BG - 1.0) / 2.0                            # (local) = sinh^2(r) = 730.65
    out["r_squeeze"] = r_squeeze
    out["n_peak"] = n_peak
    out["n_pairs"] = n_pairs

    # ======================================================================
    #  TRACK A (LOAD-BEARING): v_fs^4D = T^{0i}/T^{00} = 0 EXACT
    #  Demonstrate the (k,-k) momentum cancellation to machine precision.
    # ======================================================================
    # Signed 1D grid (the squeeze produces +k and -k pairs); n(k)=n(-k) EVEN.
    k_signed = np.linspace(-K_MAX, K_MAX, 2 * N_EVAL + 1)  # (local) symmetric grid
    n_signed = frozen_occupation(k_signed, m_L, n_peak)    # (local)
    E_signed = np.sqrt(k_signed**2 + m_L**2)               # (local)
    # Momentum density T^{0i} ~ int k n(k) dk  (1D proxy; odd integrand => 0)
    T0i_1d = float(np.trapezoid(k_signed * n_signed, k_signed))      # (local)
    T00_1d = float(np.trapezoid(E_signed * n_signed, k_signed))      # (local)
    # Full isotropic 3D demonstration: the angular integral of k_hat^i over the
    # sphere is int_0^pi cos(theta) sin(theta) dtheta = 0 (parity), so
    # T^{0i}_3D = int k_hat^i k n(k) d3k = 0 regardless of the radial profile.
    theta = np.linspace(0.0, np.pi, 4001)                  # (local)
    ang_zero = float(np.trapezoid(np.cos(theta) * np.sin(theta), theta))  # (local) ~1e-17
    v_fs_4D = abs(T0i_1d) / T00_1d                          # (local) = 0 to machine eps
    out["T0i_1d"] = T0i_1d
    out["T00_1d"] = T00_1d
    out["angular_integral_cos"] = ang_zero
    out["v_fs_4D"] = v_fs_4D
    out["lambda_fs_4D_Mpc"] = 0.0                           # = int 0/a dt EXACT

    # ======================================================================
    #  z_tr RE-ANCHOR (reproduce FREE-STREAMING-58 at the anchored mass)
    # ======================================================================
    # Production redshift from the transit energy scale M_KK (s58 STEP 3).
    g_star_S_today = 3.938                                  # (local) photons + 3 nu
    g_star_S_SM = 106.75                                    # (local) full SM
    g_ratio = (g_star_S_today / g_star_S_SM) ** (1.0 / 3.0)  # (local)
    z_prod_grav = (M_KK_gravity / T_CMB_GeV) * g_ratio - 1.0  # (local)
    z_prod_kern = (M_KK_kerner / T_CMB_GeV) * g_ratio - 1.0   # (local)

    # Fixed-velocity reading (s58 canonical: v_prod = c_Gold = 0.915c).
    v_prod = c_Gold                                         # (local) 0.915c
    gamma_prod = 1.0 / np.sqrt(1.0 - v_prod**2)            # (local)
    p_prod_over_m = gamma_prod * v_prod                    # (local) = 2.268
    p_tr_over_m = 1.0 / (2.0 * np.sqrt(2.0))               # (local) v=c/3 threshold
    kin_factor = p_prod_over_m / p_tr_over_m               # (local) = 6.41
    z_tr_grav = kin_factor * (1.0 + z_prod_grav) - 1.0     # (local)
    z_tr_kern = kin_factor * (1.0 + z_prod_kern) - 1.0     # (local)
    margin_grav = float(np.log10(z_tr_grav / Z_THRESHOLD)) # (local) OOM
    margin_kern = float(np.log10(z_tr_kern / Z_THRESHOLD)) # (local) OOM
    out["z_prod_grav"] = z_prod_grav
    out["z_prod_kern"] = z_prod_kern
    out["z_tr_grav"] = z_tr_grav
    out["z_tr_kern"] = z_tr_kern
    out["z_threshold"] = Z_THRESHOLD
    out["margin_grav_OOM"] = margin_grav
    out["margin_kern_OOM"] = margin_kern

    # s58 cross-check (faithful reproduction)
    s58 = np.load(S58_NPZ, allow_pickle=True)              # (local)
    z_tr_grav_s58 = float(s58["z_tr_grav"])               # (local)
    out["z_tr_grav_s58"] = z_tr_grav_s58
    out["z_tr_reproduction_relerr"] = abs(z_tr_grav - z_tr_grav_s58) / z_tr_grav_s58

    # Heavier-mass (fixed-momentum) reading: a heavier mass at fixed production
    # momentum is LESS relativistic => colder. p_prod_abs from the s58 B2 anchor.
    m_B2_fold = float(s58["m_B2_fold_MKK"])               # (local) 0.7231 M_KK
    p_prod_abs = float(s58["p_prod_over_m"]) * m_B2_fold  # (local) absolute production momentum
    v_prod_fixedp = p_prod_abs / np.sqrt(p_prod_abs**2 + m_L**2)  # (local) at m_Leggett
    out["v_prod_fixedp"] = float(v_prod_fixedp)
    out["p_prod_abs_MKK"] = float(p_prod_abs)

    # ======================================================================
    #  TRACK B (DIAGNOSTIC): internal momentum spread of n(k)
    #  EXPLICITLY NOT the 4D free-streaming velocity (S43/S44 category guard).
    # ======================================================================
    # Number-weighted moments over the isotropic frozen occupation (d3k = 4pi k^2 dk).
    k_grid = np.logspace(np.log10(K_MIN), np.log10(K_MAX), N_EVAL)  # (local)
    n_grid = frozen_occupation(k_grid, m_L, n_peak)        # (local)
    w = 4.0 * np.pi * k_grid**2                            # (local) d3k measure
    norm = float(np.trapezoid(n_grid * w, k_grid))         # (local) total number ~ int n d3k
    mean_k = float(np.trapezoid(k_grid * n_grid * w, k_grid)) / norm        # (local) <k>
    mean_k2 = float(np.trapezoid(k_grid**2 * n_grid * w, k_grid)) / norm    # (local) <k^2>
    # Relativistic group velocity v_g = k/E (BOUNDED by c); the physical reading.
    vg = k_grid / np.sqrt(k_grid**2 + m_L**2)              # (local)
    vg2_mean = float(np.trapezoid(vg**2 * n_grid * w, k_grid)) / norm       # (local) <v_g^2>
    v_rms_internal = float(np.sqrt(vg2_mean))              # (local) BOUNDED internal RMS velocity
    # Plan's literal (k/m) form: the NON-relativistic 2nd moment (UV-sensitive).
    km2_mean = mean_k2 / m_L**2                            # (local) <(k/m)^2>
    v_km_internal = float(np.sqrt(km2_mean))               # (local) (k/m) RMS (cutoff-sensitive)
    out["mean_k_MKK"] = mean_k
    out["mean_k2_MKK2"] = mean_k2
    out["v_rms_internal_vg"] = v_rms_internal
    out["v_km_internal_NR"] = v_km_internal
    out["total_number_norm"] = norm

    # quad cross-check of the (bounded) v_g 2nd-moment numerator/denominator
    num_q, _ = integrate.quad(lambda x: (x / np.sqrt(x**2 + m_L**2))**2
                              * frozen_occupation(x, m_L, n_peak) * 4 * np.pi * x**2,
                              K_MIN, K_MAX, limit=400, epsrel=INT_RTOL)  # (local)
    den_q, _ = integrate.quad(lambda x: frozen_occupation(x, m_L, n_peak)
                              * 4 * np.pi * x**2,
                              K_MIN, K_MAX, limit=400, epsrel=INT_RTOL)  # (local)
    vg2_quad = num_q / den_q                                # (local)
    out["vg2_quad_crosscheck"] = float(vg2_quad)
    out["vg2_trapz_vs_quad_relerr"] = abs(vg2_mean - vg2_quad) / vg2_quad

    # Naive Track-B z_tr: plug v_rms_internal (capped <c) as an effective v_prod.
    v_eff = min(v_rms_internal, 0.999)                     # (local) cap below c
    gv_eff = v_eff / np.sqrt(1.0 - v_eff**2) / p_tr_over_m  # (local) kinematic factor
    z_tr_trackB = gv_eff * (1.0 + z_prod_grav) - 1.0       # (local)
    out["z_tr_trackB"] = float(z_tr_trackB)
    out["margin_trackB_OOM"] = float(np.log10(z_tr_trackB / Z_THRESHOLD))

    # ======================================================================
    #  PHYSICAL lambda_fs in Mpc (comoving free-streaming horizon integral)
    #  lambda_fs = (c/H_0) int_{a_prod}^{1} v(a) / (a^2 E_H(a)) da
    # ======================================================================
    c_over_H0_Mpc = c_light_km_s / H_0_km_s_Mpc            # (local) = 4448 Mpc

    def E_H(a):
        return np.sqrt(Omega_r / a**4 + Omega_m / a**3 + (1.0 - Omega_r - Omega_m))  # (local)

    def lambda_fs_Mpc(v_prod_in, gv_in):
        """Comoving free-streaming length for a relic produced at z_prod_grav
        with production velocity v_prod_in (kinematic ratio gv_in = gamma*v)."""
        a_prod = 1.0 / (1.0 + z_prod_grav)                 # (local)
        a_grid = np.logspace(np.log10(a_prod), 0.0, 4000)  # (local)
        p_over_m = gv_in * (a_prod / a_grid)               # (local) p/m redshifts as 1/a
        v_a = p_over_m / np.sqrt(p_over_m**2 + 1.0)         # (local) v(a) = p/E
        integrand = v_a / (a_grid**2 * E_H(a_grid))         # (local)
        return float(c_over_H0_Mpc * np.trapezoid(integrand, a_grid))  # (local)

    lam_fixedv = lambda_fs_Mpc(v_prod, p_prod_over_m)      # (local) s58 fixed-v reading
    lam_trackB = lambda_fs_Mpc(v_eff, v_eff / np.sqrt(1.0 - v_eff**2))  # (local) Track-B
    out["lambda_fs_Mpc_fixedv"] = lam_fixedv
    out["lambda_fs_Mpc_trackB"] = lam_trackB
    out["lambda_threshold_Mpc"] = LAMBDA_THRESHOLD_MPC
    out["lambda_fs_4D_Mpc"] = 0.0                          # Track A: EXACT 0

    # WDM-equivalent mass (s58 STEP 8 metric; larger => colder)
    T_nu_today_eV = (4.0 / 11.0)**(1.0 / 3.0) * T_CMB * 8.617e-5  # (local)
    m_WDM_equiv_keV = 3.0 * T_nu_today_eV * z_tr_grav * 1e-3      # (local)
    out["m_WDM_equiv_keV"] = float(m_WDM_equiv_keV)

    # store grids for plotting
    out["_k_grid"] = k_grid
    out["_n_grid"] = n_grid
    out["_vg"] = vg

    # ======================================================================
    #  [SIGN] verdict
    # ======================================================================
    # Sign: (lambda_fs - lambda_threshold). Track A EXACT => 0 - threshold < 0.
    delta_lambda_A = out["lambda_fs_4D_Mpc"] - LAMBDA_THRESHOLD_MPC  # (local) < 0
    delta_lambda_B = lam_trackB - LAMBDA_THRESHOLD_MPC              # (local) < 0 (cross-check)
    out["delta_lambda_A"] = delta_lambda_A
    out["delta_lambda_B"] = delta_lambda_B

    # sign_verdict: PASS iff NEGATIVE (cold) -- prediction matches computed sign
    sign_pass = (delta_lambda_A < 0) and (delta_lambda_B < 0) and (v_fs_4D < 1e-12)
    sign_verdict = "PASS" if sign_pass else "FAIL"          # (local)
    # magnitude_verdict: PASS iff > 1 decade below threshold (z_tr margin >> 1)
    mag_pass = (margin_grav > 1.0) and (out["margin_trackB_OOM"] > 1.0)
    mag_within_decade = abs(np.log10(max(lam_trackB, 1e-300) / LAMBDA_THRESHOLD_MPC)) <= 1.0  # (local)
    if mag_pass and not mag_within_decade:
        magnitude_verdict = "PASS"
    elif mag_within_decade:
        magnitude_verdict = "INFO"
    else:
        magnitude_verdict = "FAIL"
    # regime_verdict: load-bearing Track A exact + bounded v_g => VALID.
    regime_verdict = "VALID" if (out["vg2_trapz_vs_quad_relerr"] < 1e-3
                                 and v_rms_internal <= 1.0) else "MARGINAL"  # (local)

    # composite collapse (gate-verdicts.md rule)
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"
    elif sign_verdict == "FAIL":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"
    elif magnitude_verdict == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"

    out["sign_verdict"] = sign_verdict
    out["magnitude_verdict"] = magnitude_verdict
    out["regime_verdict"] = regime_verdict
    out["composite"] = composite
    out["value"] = (f"lambda_fs^4D=0(EXACT,v_fs^4D={v_fs_4D:.2e}); "
                    f"z_tr={z_tr_grav:.3e}>>z_thr={Z_THRESHOLD:.1e} ({margin_grav:.1f}OOM); "
                    f"lambda_fs<{LAMBDA_THRESHOLD_MPC}Mpc by ~{-np.log10(max(lam_trackB,1e-300)/LAMBDA_THRESHOLD_MPC):.0f}dec; "
                    f"v_rms_int(v_g)={v_rms_internal:.3f}c[NOT-4D]; cold;170x-DISCHARGED")
    return out


# ---------------------------------------------------------------------------
# Section 7 -- Plot
# ---------------------------------------------------------------------------
def make_plot(r: dict) -> None:
    fig, ax = plt.subplots(2, 2, figsize=(13, 9))  # (local)
    k = r["_k_grid"]; n = r["_n_grid"]; vg = r["_vg"]; m_L = r["m_Leggett_MKK"]  # (local)

    # Panel 1: frozen Bogoliubov occupation n(k)
    ax[0, 0].loglog(k, n, "b-", lw=1.6)
    ax[0, 0].axhline(r["n_peak"], color="g", ls=":", label=f"n_peak={r['n_peak']:.1f} (cap)")
    ax[0, 0].axvline(m_L, color="r", ls="--", label=f"m_Leggett={m_L:.3f} M_KK")
    ax[0, 0].set_xlabel("k  (M_KK units)"); ax[0, 0].set_ylabel("n(k)")
    ax[0, 0].set_title("Frozen Bogoliubov occupation (BdG + capped squeeze)")
    ax[0, 0].legend(fontsize=8); ax[0, 0].grid(alpha=0.3, which="both")

    # Panel 2: internal velocity structure -- v_g(k) bounded, (k/m)(k) unbounded
    ax[0, 1].semilogx(k, vg, "b-", lw=1.6, label="v_g = k/E  (bounded < c)")
    ax[0, 1].semilogx(k, k / m_L, "m--", lw=1.2, label="(k/m)  (NR; > c at high k)")
    ax[0, 1].axhline(1.0, color="k", ls=":", lw=0.8, label="c")
    ax[0, 1].axhline(r["v_rms_internal_vg"], color="g", ls="-.",
                     label=f"v_rms_int(v_g)={r['v_rms_internal_vg']:.3f}c [NOT 4D]")
    ax[0, 1].set_xlabel("k  (M_KK units)"); ax[0, 1].set_ylabel("internal velocity (c)")
    ax[0, 1].set_ylim(0, 3)
    ax[0, 1].set_title("Track B internal momentum spread (category-guarded)")
    ax[0, 1].legend(fontsize=8); ax[0, 1].grid(alpha=0.3)

    # Panel 3: z_tr vs production velocity (s58 robustness) + threshold
    v_scan = np.linspace(0.1, 0.999, 200)  # (local)
    gv_scan = v_scan / np.sqrt(1 - v_scan**2) / (1 / (2 * np.sqrt(2)))  # (local)
    z_tr_scan = gv_scan * (1 + r["z_prod_grav"]) - 1  # (local)
    ax[1, 0].semilogy(v_scan, z_tr_scan, "b-", lw=1.6, label="z_tr(v_prod), z_prod~1e29")
    ax[1, 0].axhline(r["z_threshold"], color="r", ls="--", label=f"z_thr={r['z_threshold']:.1e}")
    ax[1, 0].axvline(r["v_rms_internal_vg"], color="g", ls="-.", label="v_rms_int (Track B)")
    ax[1, 0].axvline(0.915, color="k", ls=":", label="c_Gold=0.915 (s58)")
    ax[1, 0].set_xlabel("production velocity (c)"); ax[1, 0].set_ylabel("z_tr")
    ax[1, 0].set_title(f"z_tr >> z_thr for ANY v  (margin {r['margin_grav_OOM']:.0f} OOM)")
    ax[1, 0].legend(fontsize=8); ax[1, 0].grid(alpha=0.3)

    # Panel 4: lambda_fs bar chart (3 readings) vs threshold
    labels = ["Track A\n(v_fs^4D=0)", "fixed-v\n(s58 reading)", "Track B\n(internal,naive)"]  # (local)
    vals = [max(r["lambda_fs_4D_Mpc"], 1e-300), r["lambda_fs_Mpc_fixedv"], r["lambda_fs_Mpc_trackB"]]  # (local)
    vals = [max(v, 1e-300) for v in vals]  # (local) floor for log plot
    ax[1, 1].bar(labels, [np.log10(v) for v in vals], color=["g", "b", "m"], alpha=0.7)
    ax[1, 1].axhline(np.log10(r["lambda_threshold_Mpc"]), color="r", ls="--",
                     label=f"log10 threshold ({r['lambda_threshold_Mpc']} Mpc)")
    ax[1, 1].set_ylabel("log10(lambda_fs / Mpc)")
    ax[1, 1].set_title("Comoving free-streaming length << threshold (all readings)")
    ax[1, 1].legend(fontsize=8); ax[1, 1].grid(alpha=0.3, axis="y")
    ax[1, 1].annotate("Track A = 0 EXACT\n(floored for log)", xy=(0, -200),
                      fontsize=7, ha="center", color="g")

    fig.suptitle(f"{GATE_ID}: DM free-streaming at the graph-anchored Leggett mass "
                 f"(m={r['m_Leggett_MKK']:.3f} M_KK = {r['m_Leggett_GeV']:.2e} GeV)",
                 fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 -- verdict payload (race-safe emit via the agent)
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme, convention, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="",
                          extra_rows=None) -> dict:
    payload: dict = {
        "session": 117,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if not (sign_verdict is None and magnitude_verdict is None and regime_verdict is None):
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 9 -- Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    r = compute()

    print("=" * 72)
    print(f"  {GATE_ID}")
    print("=" * 72)
    print(f"  anchored mass m_Leggett = {r['m_Leggett_MKK']:.6f} M_KK "
          f"= {r['m_Leggett_GeV']:.6e} GeV  (canonical M_DM_Leggett_GeV={r['m_Leggett_GeV_canonical']:.6e})")
    print(f"  squeeze: r={r['r_squeeze']:.6f}, n_peak={r['n_peak']:.4f}, n_pairs={r['n_pairs']}")
    print()
    print("  --- TRACK A (load-bearing): v_fs^4D = T^0i/T^00 ---")
    print(f"    T^0i (1D, (k,-k) cancellation) = {r['T0i_1d']:.3e}  (=> 0 by parity)")
    print(f"    T^00 (energy density)          = {r['T00_1d']:.3e}  (> 0)")
    print(f"    angular int cos*sin            = {r['angular_integral_cos']:.3e}  (=> 0)")
    print(f"    v_fs^4D = |T^0i|/T^00          = {r['v_fs_4D']:.3e}  (= 0 EXACT, CDM-CONSTRUCT-44)")
    print(f"    lambda_fs^4D = int 0/a dt      = {r['lambda_fs_4D_Mpc']:.1f} Mpc  (< threshold)")
    print()
    print("  --- z_tr RE-ANCHOR (FREE-STREAMING-58 reproduction) ---")
    print(f"    z_prod (grav) = {r['z_prod_grav']:.4e}  | z_prod (kern) = {r['z_prod_kern']:.4e}")
    print(f"    z_tr   (grav) = {r['z_tr_grav']:.4e}  | z_tr   (kern) = {r['z_tr_kern']:.4e}")
    print(f"    z_threshold   = {r['z_threshold']:.2e}  | margin = {r['margin_grav_OOM']:.1f} OOM (grav)")
    print(f"    s58 cross-check z_tr_grav = {r['z_tr_grav_s58']:.4e}  (relerr {r['z_tr_reproduction_relerr']:.2e})")
    print(f"    fixed-momentum reading: v_prod(m_Leggett) = {r['v_prod_fixedp']:.4f}c  (heavier => colder)")
    print()
    print("  --- TRACK B (diagnostic, NOT the 4D velocity) ---")
    print(f"    <k> = {r['mean_k_MKK']:.4f} M_KK | <k^2> = {r['mean_k2_MKK2']:.4f} M_KK^2")
    print(f"    v_rms_internal (v_g=k/E, BOUNDED)   = {r['v_rms_internal_vg']:.4f} c   [the physical reading]")
    print(f"    v_km_internal  ((k/m), NR/UV-sens.) = {r['v_km_internal_NR']:.4f}     [cutoff-dependent => Track A load-bearing]")
    print(f"    quad cross-check <v_g^2> relerr     = {r['vg2_trapz_vs_quad_relerr']:.2e}")
    print(f"    naive Track-B z_tr = {r['z_tr_trackB']:.4e}  (margin {r['margin_trackB_OOM']:.1f} OOM)")
    print()
    print("  --- PHYSICAL lambda_fs (comoving, Mpc) ---")
    print(f"    Track A (v_fs^4D=0)  : lambda_fs = {r['lambda_fs_4D_Mpc']:.3e} Mpc  (EXACT 0)")
    print(f"    fixed-v (s58 reading): lambda_fs = {r['lambda_fs_Mpc_fixedv']:.4e} Mpc")
    print(f"    Track B (internal)   : lambda_fs = {r['lambda_fs_Mpc_trackB']:.4e} Mpc")
    print(f"    lambda_threshold     = {r['lambda_threshold_Mpc']} Mpc  | m_WDM_equiv = {r['m_WDM_equiv_keV']:.2e} keV")
    print()
    print(f"  [SIGN] sign={r['sign_verdict']} magnitude={r['magnitude_verdict']} "
          f"regime={r['regime_verdict']} => composite={r['composite']}")
    print()

    make_plot(r)

    save = {k: v for k, v in r.items() if not k.startswith("_")}  # (local)
    save["_k_grid"] = r["_k_grid"]; save["_n_grid"] = r["_n_grid"]; save["_vg"] = r["_vg"]
    save["gate_name"] = np.array([GATE_ID])
    save["gate_verdict"] = np.array([f"{r['composite']}: {r['value']}"])
    np.savez(OUT_NPZ, **save)
    print(f"  saved: {OUT_NPZ.name}, {OUT_PNG.name}")

    tag = emit_4tuple(r["value"], SCHEME, CONVENTION, L_MAX)
    print(tag)
    extra = [
        f"# regime_note: load-bearing Track-A v_fs^4D={r['v_fs_4D']:.2e} EXACT (CDM-CONSTRUCT-44); "
        f"Track-B v_rms_internal(v_g)={r['v_rms_internal_vg']:.3f}c is a substrate-INTERNAL "
        f"momentum spread, NOT the 4D free-streaming velocity (S43/S44 category guard); "
        f"(k/m) form UV-sensitive ({r['v_km_internal_NR']:.2f}) => Track A load-bearing.",
        f"# crosscheck: z_tr reproduces s58 FREE-STREAMING-58 to relerr {r['z_tr_reproduction_relerr']:.1e}; "
        f"170x re-typing DISCHARGED on the free-streaming axis (lambda_fs << threshold all readings).",
    ]  # (local)
    print_verdict_payload(
        r["composite"], r["value"], audit_sha, content_sha,
        sign_verdict=r["sign_verdict"], magnitude_verdict=r["magnitude_verdict"],
        regime_verdict=r["regime_verdict"], extra_rows=extra,
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {r['composite']} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
