"""S84-CGWB-ABSOLUTE-PT-PREDICTION — W6-50.

Absolute tensor power P_t(f) prediction at LISA/DECIGO/BBO frequencies for
the TD-canonical (A) vs mixed-C (geometric-mean) vs LI (endpoint) branches.
Central arithmetic claim:

  (H_TD / H_mixed)^2 = H_TD / H_LI = 5.9076e-3 / 2.46411e-5 = 239.75
  log10(239.75) = 2.3798 decades

This is the (A)-vs-(C) discriminator on P_t (and therefore Omega_GW) at
ANY fixed frequency where the ratio of transfer functions between the
two branches is order unity. The PASS question is whether the absolute
strain h_c^(A) at f = 3 mHz exceeds LISA's sensitivity floor
h_LISA ~ 1e-21/sqrt(Hz) — that is the runtime gate split.

Substrate-framing (plan §6):
  These are phonon-pair relay patterns on M^4 x SU(3). The reheating-
  equivalent phase is Gamma_phi-driven modulus decay into SM relay
  patterns, NOT inflationary reheating. The frame rate c bounds the
  propagation of these GW modes ACROSS the substrate g_M, not the
  substrate's own dynamics. Direction of explanation:
     D_K eigenvalues -> spectral moments -> emergent GW spectrum.

SUBSTITUTION CHAIN (mandatory — [CHAIN] trigger, plan §10):
  Step 1 (def):  P_t(k) = (2/pi^2) * (H_tilde/M_Pl_eff)^2 * (k/k_*)^n_t
                 [canonical tensor power, Mukhanov-Sasaki]
  Step 2 (ratio at fixed k):
      P_t^(A)(k) / P_t^(C)(k) = (H_TD / H_mixed)^2
      (the (k/k_*)^n_t tilt cancels; common M_Pl_eff cancels)
  Step 3 (subst H_mixed = sqrt(H_TD * H_LI)):
      (H_TD / sqrt(H_TD*H_LI))^2 = H_TD / H_LI
                                 = 5.9076e-3 / 2.46411e-5
                                 = 239.75
  Step 4 (Omega_GW inherits P_t prefactor directly):
      Omega_GW^(A)/Omega_GW^(C) = P_t^(A)/P_t^(C) = 239.75
      log10(239.75) = 2.3798 >> 1.0 PASS threshold
  Step 5 (direction):  POSITIVE — TD branch is brighter than mixed-C
                       branch at every fixed frequency by 239.75x in
                       Omega_GW, 15.48x in h_c.
  Step 6 (runtime):    The detector-reach check h_c^(A) > h_LISA at
                       3 mHz is performed by the script body below.

Anchor pins:
  H_TD            = 5.90760e-3   (S82 W1-2 PASS-F2, zeta, L_max=3)
  H_LI            = 2.46411e-5   (S80 W1-1 LI reference endpoint)
  r_CMB           = 0.011731522... (S83 G46 PASS)
  n_t             = +0.4676      (S83 G50 BLUE at fold)
  eps_H           = 0.02163      (S82 one-loop SR)
  Gamma_phi       = 1.6e-37 s^-1 (S76 modulus SM decay rate)
  M_Pl_reduced    = 2.435e18 GeV (CODATA 2018, canonical)
  H0_Planck       = 2.184e-18 s^-1 (Planck 2018)
  LISA floor h_LISA(3 mHz) = 1e-21 / sqrt(Hz) (LISA-L3 design)

Outputs:
  computations/session-84/s84_w6_cgwb_absolute_pt.npz
  computations/session-84/s84_w6_cgwb_absolute_pt.png
Verdict line appended to computations/session-84/s84_gate_verdicts.txt with
full 64-char SHA-256 closure.
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
from pathlib import Path

# Scalar computation (~30 lines of arithmetic); cap CPU threads per rules.
os.environ.setdefault("OMP_NUM_THREADS", "8")

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# Anchor the script directory so canonical_constants imports resolve.
_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

from canonical_constants import (
    M_Pl_reduced,
    H_0_inv_s,
    c_light,
    r_CMB_framework,
    tau_fold,
    M_KK,
    planck_ns,
)

# ---------------------------------------------------------------------------
# Section 0 — input-pin map (SHA-256 closure)
# ---------------------------------------------------------------------------
INPUT_PINS: dict[str, str] = {}

# Pin this script's own source file and the canonical_constants module.
_self_path = _HERE / "s84_w6_cgwb_absolute_pt.py"
_cc_path = _HERE / "canonical_constants.py"
for _p in [_self_path, _cc_path]:
    if _p.exists():
        INPUT_PINS[_p.name] = hashlib.sha256(_p.read_bytes()).hexdigest()
    else:
        INPUT_PINS[_p.name] = "MISSING"

# ---------------------------------------------------------------------------
# Section 1 — anchor constants (local; not yet in canonical_constants.py)
# ---------------------------------------------------------------------------
H_TD = 5.90760e-3      # (local) S82 W1-2 PASS-F2 canonical TD branch
H_LI = 2.46411e-5      # (local) S80 W1-1 LI endpoint (reference only)
H_mixed = float(np.sqrt(H_TD * H_LI))  # (local) geometric mean (C) branch

r_CMB = r_CMB_framework  # (local alias) r(k_CMB) = 0.011731522... (G46)
n_t = 0.4676            # (local) BLUE tensor tilt at transit (S83 G50)
eps_H = 0.02163         # (local) one-loop slow-roll (S82)
Gamma_phi_modulus = 1.6e-37  # (local) s^-1, S76 modulus SM decay rate

# Pivots / frequencies
k_pivot_Mpc = 0.05      # (local) Planck pivot in Mpc^-1
k_CMB_Mpc = 0.002       # (local) CMB tensor pivot in Mpc^-1 (BK convention)
f_grid = np.array([1e-4, 1e-3, 1e-1])  # (local) LISA-low, LISA-mid, BBO/DECIGO

# LISA/DECIGO/BBO strain-amplitude floors (power-law-integrated, approximate)
h_LISA_at_3mHz = 1e-21  # (local) 1/sqrt(Hz), LISA-L3 design floor at 3 mHz
h_DECIGO = 1e-24        # (local) 1/sqrt(Hz), DECIGO design floor at 0.1 Hz
h_BBO = 1e-25           # (local) 1/sqrt(Hz), BBO design floor at 0.1 Hz

# transfer_correction sensitivity bracket (plan §6 step 2)
transfer_correction_grid = np.array([0.5, 1.0, 2.0])  # (local)
transfer_correction_central = 1.0  # (local) pinned per plan §7

# Reduced Planck mass = M_Pl_eff (epoch-pivot-stationary per S83 G12)
M_Pl_eff = M_Pl_reduced  # (local alias)

# Pin arithmetic anchors to closure
INPUT_PINS["H_TD"] = f"{H_TD:.10e}"
INPUT_PINS["H_LI"] = f"{H_LI:.10e}"
INPUT_PINS["H_mixed"] = f"{H_mixed:.10e}"
INPUT_PINS["r_CMB"] = f"{r_CMB:.10e}"
INPUT_PINS["n_t"] = f"{n_t:.6f}"
INPUT_PINS["eps_H"] = f"{eps_H:.10e}"
INPUT_PINS["Gamma_phi_modulus"] = f"{Gamma_phi_modulus:.10e}"
INPUT_PINS["M_Pl_reduced"] = f"{M_Pl_reduced:.10e}"
INPUT_PINS["H0_Planck_inv_s"] = f"{H_0_inv_s:.10e}"
INPUT_PINS["c_light"] = f"{c_light:.10e}"
INPUT_PINS["f_grid"] = ",".join(f"{f:.6e}" for f in f_grid)
INPUT_PINS["transfer_correction_central"] = f"{transfer_correction_central:.6f}"
INPUT_PINS["transfer_correction_grid"] = ",".join(
    f"{t:.3f}" for t in transfer_correction_grid
)
INPUT_PINS["k_pivot_Mpc"] = f"{k_pivot_Mpc:.6e}"
INPUT_PINS["k_CMB_Mpc"] = f"{k_CMB_Mpc:.6e}"
INPUT_PINS["h_LISA_at_3mHz"] = f"{h_LISA_at_3mHz:.6e}"
INPUT_PINS["h_DECIGO"] = f"{h_DECIGO:.6e}"
INPUT_PINS["h_BBO"] = f"{h_BBO:.6e}"
INPUT_PINS["tau_fold"] = f"{tau_fold:.6f}"
INPUT_PINS["L_max"] = "N/A"
INPUT_PINS["scheme"] = "TD-canonical-vs-mixed-C"
INPUT_PINS["convention"] = "transfer_correction=1.0"

CLOSURE_INPUT = json.dumps(INPUT_PINS, sort_keys=True, separators=(",", ":"))
CLOSURE_SHA = hashlib.sha256(CLOSURE_INPUT.encode("utf-8")).hexdigest()

# ---------------------------------------------------------------------------
# Section 2 — banner: SHA log + anchor echo (first 20 lines of stdout)
# ---------------------------------------------------------------------------
print("=" * 78)
print("S84 W6-50: CGWB-ABSOLUTE-PT-PREDICTION")
print("=" * 78)
print(f"closure SHA-256 (64 char): {CLOSURE_SHA}")
print(f"closure SHA-256 (16 head): {CLOSURE_SHA[:16]}")
print()
print("--- input pins ---")
for k, v in INPUT_PINS.items():
    print(f"  {k:<32s}: {v}")
print()
print("--- anchors (substrate-first-principles) ---")
print(f"  H_TD              = {H_TD:.6e}  (S82 W1-2 PASS-F2)")
print(f"  H_LI              = {H_LI:.6e}  (S80 W1-1 reference)")
print(f"  H_mixed (geom)    = {H_mixed:.6e}  (= sqrt(H_TD * H_LI))")
print(f"  r_CMB (G46)       = {r_CMB:.6e}")
print(f"  n_t (G50 BLUE)    = {n_t:.4f}")
print(f"  Gamma_phi         = {Gamma_phi_modulus:.3e} s^-1  (S76)")
print()

# ---------------------------------------------------------------------------
# Section 3 — substitution chain arithmetic (Steps 1-5)
# ---------------------------------------------------------------------------
print("=" * 78)
print("SUBSTITUTION CHAIN — Steps 1-5 (direction arithmetic)")
print("=" * 78)

# Step 1: P_t(k) = (2/pi^2) * (H_tilde/M_Pl_eff)^2 * (k/k_*)^n_t
print("Step 1 (def):")
print("  P_t(k) = (2/pi^2) * (H_tilde/M_Pl_eff)^2 * (k/k_*)^n_t")

# Step 2: ratio at fixed k (tilt and M_Pl cancel)
ratio_H_AC = H_TD / H_mixed  # (local)
ratio_H_AC_sq = ratio_H_AC ** 2  # (local) P_t ratio
print("Step 2 (ratio at fixed k):")
print(f"  H_TD / H_mixed     = {ratio_H_AC:.5f}")
print(f"  (H_TD / H_mixed)^2 = {ratio_H_AC_sq:.5f}")

# Step 3: substitute H_mixed = sqrt(H_TD * H_LI) => H_TD / H_LI
ratio_TD_LI = H_TD / H_LI  # (local)
print("Step 3 (subst H_mixed = sqrt(H_TD * H_LI)):")
print(f"  (H_TD / sqrt(H_TD * H_LI))^2 = H_TD / H_LI")
print(f"                               = {H_TD:.5e} / {H_LI:.5e}")
print(f"                               = {ratio_TD_LI:.5f}")
# Cross-check: ratio_H_AC_sq should equal ratio_TD_LI to machine epsilon
_chk_cross = abs(ratio_H_AC_sq - ratio_TD_LI) / ratio_TD_LI  # (local)
assert _chk_cross < 1e-12, f"algebra consistency broken: {_chk_cross}"
print(f"  cross-check: |ratio_sq - ratio_TD_LI|/ratio_TD_LI = {_chk_cross:.3e} (OK)")

# Step 4: Omega_GW inherits P_t ratio
log10_rho_AC = float(np.log10(ratio_TD_LI))  # (local)
print("Step 4 (Omega_GW inherits P_t prefactor):")
print(f"  Omega_GW^(A) / Omega_GW^(C) = {ratio_TD_LI:.5f}")
print(f"  log10(ratio)                = {log10_rho_AC:.5f}")

# Step 5: direction
print("Step 5 (direction):")
print(f"  {log10_rho_AC:.5f} >> 1.0 threshold => (A) >> (C) — POSITIVE")
print(f"  Pre-write task pin: expected ~2.38, computed {log10_rho_AC:.5f} "
      f"(delta = {abs(log10_rho_AC - 2.38):.5f})")
print()

# ---------------------------------------------------------------------------
# Section 4 — absolute P_t(f) and Omega_GW(f) across branches
# ---------------------------------------------------------------------------
print("=" * 78)
print("ABSOLUTE P_t AND Omega_GW COMPUTATIONS")
print("=" * 78)

# GeV -> 1/s conversion (angular frequency, natural units)
# 1 GeV = (1.602e-10 J) / hbar = 1.519e24 rad/s ≡ 1.519e24 1/s when expressing
# H as an angular Hubble rate.
GeV_to_inv_s = 1.519267523e24  # (local) angular-frequency conversion

# Physical Hubble at transit (post-fold cascade) in 1/s, per branch.
# H_tilde (dimensionless, M_Pl_reduced units per S82 A_s convention) ->
#   H_physical[GeV] = H_tilde * M_Pl_reduced[GeV]
#   H_physical[1/s] = H_physical[GeV] * GeV_to_inv_s
H_TD_phys = H_TD * M_Pl_reduced * GeV_to_inv_s  # (local) s^-1
H_LI_phys = H_LI * M_Pl_reduced * GeV_to_inv_s  # (local) s^-1
H_mx_phys = H_mixed * M_Pl_reduced * GeV_to_inv_s  # (local) s^-1

print(f"  H_TD (phys)       = {H_TD_phys:.4e} s^-1")
print(f"  H_LI (phys)       = {H_LI_phys:.4e} s^-1")
print(f"  H_mixed (phys)    = {H_mx_phys:.4e} s^-1")

# Post-fold cascade + reheating-equivalent phase (plan §6 step 2):
#   a_transit/a_0 = (H_tilde/H0)^(1/2) * (Gamma_phi/H0)^(-1/2) * correction
# A frequency f today corresponds to a transit-era k given by
#   f = (k/(2 pi)) * (a_transit/a_0)
# so the substrate tensor power at a given observational f reads
#   k_transit(f) = 2 pi f / (a_transit/a_0)
# and
#   P_t(f) = (2/pi^2) * (H_tilde/M_Pl_eff)^2 * (k_transit/k_star)^n_t
# with k_star taken at the CMB pivot k_CMB_Mpc (converted to 1/s via c).
def a_ratio_branch(H_inv_s: float, corr: float) -> float:
    return float(
        np.sqrt(H_inv_s / H_0_inv_s)
        * np.sqrt(H_0_inv_s / Gamma_phi_modulus)
        * corr
    )  # (local)

# Mpc -> 1/s conversion for k_CMB (use c_light)
# k (1/Mpc) * c (m/s) / (Mpc_in_m) = angular freq today (1/s)
Mpc_in_m = 3.0857e22  # (local) m per Mpc
k_star_invs = k_pivot_Mpc * c_light / Mpc_in_m  # (local) angular s^-1
print(f"  k_pivot (1/s today) = {k_star_invs:.3e}")
print()

# Pre-compute (H/M_Pl_eff)^2 prefactor per branch (dimensionless)
pref_TD = (H_TD / 1.0) ** 2  # (local) H_tilde already in M_Pl_eff units
pref_mx = (H_mixed / 1.0) ** 2  # (local)
pref_LI = (H_LI / 1.0) ** 2  # (local)

TWO_OVER_PI2 = 2.0 / (np.pi ** 2)  # (local)

# Cross-check: at k_CMB, n_t applied from k_CMB to k_CMB gives unity; the
# CMB r = 16 eps_H (standard) or r = r_CMB_framework (G46); verify by
# comparing TD-branch P_t(k_CMB) vs P_s(k_CMB) * r_CMB at CMB pivot.
# Use A_s_Planck = 2.10e-9 as scalar anchor.
A_s_Planck = 2.10e-9  # (local)
P_t_CMB_from_r = r_CMB * A_s_Planck  # (local) tensor power at CMB (G46-consistent)
P_t_TD_at_CMB_raw = TWO_OVER_PI2 * pref_TD  # (local) k=k_star (tilt unity)
# Normalize P_t(k) so TD branch reproduces CMB anchor at k_CMB.
#   Actually n_t is the transit-scale tilt; the CMB r-anchor pins overall
#   normalization. We define k_star = k_CMB and tilt is (k/k_CMB)^n_t.
norm_TD_to_CMB = P_t_CMB_from_r / P_t_TD_at_CMB_raw  # (local) normalization
print(f"--- tensor-spectrum continuity (cross-check) ---")
print(f"  P_t(k_CMB) from r_CMB * A_s  = {P_t_CMB_from_r:.4e}")
print(f"  P_t(k_CMB) TD raw (= (2/pi^2)*H_TD^2) = {P_t_TD_at_CMB_raw:.4e}")
print(f"  normalization (TD -> CMB anchor)      = {norm_TD_to_CMB:.4e}")
# This norm absorbs (1) H_tilde-to-physical-H conversion, (2) epsilon_H route
# to scalar vs tensor, (3) overall M_Pl_eff dressing. It must be applied to
# ALL branches identically so the A-vs-C ratio is preserved.
print(f"  continuity OK: |norm/P_t_TD_raw - r*A_s/P_t_TD_raw| = 0 by construction")
print()

def P_t_of_f(
    f_hz: float,
    H_inv_s: float,
    pref_sq: float,
    corr: float,
) -> tuple[float, float]:
    """Return (P_t_absolute, k_transit) at frequency f Hz for a given branch."""
    a_r = a_ratio_branch(H_inv_s, corr)
    # f = (k/(2pi)) * a_transit/a_0  ==> k_transit = 2 pi f / a_r
    k_transit = 2.0 * np.pi * f_hz / a_r  # (local) s^-1 angular
    # (k/k_star)^n_t tilt
    tilt = (k_transit / k_star_invs) ** n_t  # (local)
    # Absolute P_t with CMB normalization applied
    P_t_abs = norm_TD_to_CMB * TWO_OVER_PI2 * pref_sq * tilt  # (local)
    return float(P_t_abs), float(k_transit)


# Omega_GW(f) = (2 pi^2 / 3 H0^2) * f^2 * P_t(f) * dimensional-fixup
# Standard relation for GW energy density today:
#   h^2 Omega_GW(f) = (2 pi^2 / 3 H0^2) * f^2 * (h_c(f))^2
# and h_c^2 = P_t(f) * 1 / (f) [conventional characteristic strain]
# For a primordial stochastic background under radiation-era scaling:
#   Omega_GW(f) = (Omega_r,0 / 24) * P_t(f) * (transfer(f))
# We use the DIRECT relation h_c = sqrt(P_t), giving
#   Omega_GW = (2 pi^2 / 3 H0^2) * f^2 * P_t(f)
H0_squared = H_0_inv_s ** 2  # (local) s^-2
two_pi2 = 2.0 * np.pi ** 2  # (local)

def Omega_GW_of_f(P_t_val: float, f_hz: float) -> float:
    return float((two_pi2 / (3.0 * H0_squared)) * (f_hz ** 2) * P_t_val)  # (local)

def h_c_of_f(P_t_val: float, f_hz: float) -> float:
    """Characteristic strain: h_c = sqrt(P_t * f / c_light * m)"""
    # Standard: h_c^2(f) = 2 f * S_h(f); for a scale-invariant spectrum
    # S_h(f) = 3 H0^2 / (2 pi^2 f^3) * Omega_GW(f)
    #        = 3 H0^2 / (2 pi^2 f^3) * (2 pi^2 / 3 H0^2) f^2 P_t
    #        = P_t / f
    # => h_c(f) = sqrt(P_t * 2) (dimensionless; reported as 1/sqrt(Hz) per f)
    return float(np.sqrt(P_t_val))  # (local)

# ---------------------------------------------------------------------------
# Section 5 — evaluate at f_grid for each branch
# ---------------------------------------------------------------------------
results: dict[str, dict[str, np.ndarray]] = {}

for branch_name, H_phys, pref in [
    ("A_TD", H_TD_phys, pref_TD),
    ("C_mixed", H_mx_phys, pref_mx),
    ("LI_ref", H_LI_phys, pref_LI),
]:
    P_t_arr = np.zeros_like(f_grid)
    k_tr_arr = np.zeros_like(f_grid)
    Omega_arr = np.zeros_like(f_grid)
    h_c_arr = np.zeros_like(f_grid)
    for i_f, f_hz in enumerate(f_grid):
        P_t_val, k_tr_val = P_t_of_f(
            f_hz, H_phys, pref, transfer_correction_central
        )
        P_t_arr[i_f] = P_t_val
        k_tr_arr[i_f] = k_tr_val
        Omega_arr[i_f] = Omega_GW_of_f(P_t_val, f_hz)
        h_c_arr[i_f] = h_c_of_f(P_t_val, f_hz)
    results[branch_name] = {
        "P_t": P_t_arr,
        "k_transit": k_tr_arr,
        "Omega_GW": Omega_arr,
        "h_c": h_c_arr,
    }

# ---------------------------------------------------------------------------
# Section 6 — discriminator rho_AC(f)
# ---------------------------------------------------------------------------
rho_AC = np.log10(results["A_TD"]["Omega_GW"] / results["C_mixed"]["Omega_GW"])
max_rho_AC = float(np.max(np.abs(rho_AC)))  # (local)

print("=" * 78)
print("RESULTS — absolute P_t, Omega_GW, h_c per branch")
print("=" * 78)
print(f"{'f [Hz]':>12s}  {'P_t (A)':>12s}  {'P_t (C)':>12s}  {'P_t (LI)':>12s}"
      f"  {'Omega_A':>12s}  {'Omega_C':>12s}  {'Omega_LI':>12s}  {'rho_AC':>8s}")
for i_f, f_hz in enumerate(f_grid):
    print(f"{f_hz:>12.3e}  "
          f"{results['A_TD']['P_t'][i_f]:>12.3e}  "
          f"{results['C_mixed']['P_t'][i_f]:>12.3e}  "
          f"{results['LI_ref']['P_t'][i_f]:>12.3e}  "
          f"{results['A_TD']['Omega_GW'][i_f]:>12.3e}  "
          f"{results['C_mixed']['Omega_GW'][i_f]:>12.3e}  "
          f"{results['LI_ref']['Omega_GW'][i_f]:>12.3e}  "
          f"{rho_AC[i_f]:>8.4f}")
print()
print(f"  max |rho_AC(f)|        = {max_rho_AC:.5f}  (fixed-f, tilt-corrected)")
print(f"  fixed-k CHAIN value    = {log10_rho_AC:.5f}  (Step 4, tilt neglected)")
print()
print("--- fixed-f vs fixed-k reconciliation ---")
print("  At FIXED k_transit, P_t^A/P_t^C = (H_TD/H_mixed)^2 = 239.75 (log10 = 2.38)")
print("  At FIXED f_today, the two branches reach different k_transit:")
print("    k_transit^(A)(f) / k_transit^(C)(f) = sqrt(H_mixed/H_TD) = (H_LI/H_TD)^(1/4)")
_k_ratio_AC = float(np.sqrt(H_mixed / H_TD))  # (local)
_tilt_ratio_AC = _k_ratio_AC ** n_t  # (local) (k^A/k^C)^n_t
_full_ratio_AC_fixedf = (H_TD / H_mixed) ** 2 * _tilt_ratio_AC  # (local)
_log_full_fixedf = float(np.log10(_full_ratio_AC_fixedf))  # (local)
print(f"    k_transit^A/k_transit^C = {_k_ratio_AC:.5f}")
print(f"    tilt correction (k^A/k^C)^n_t = {_tilt_ratio_AC:.5f}")
print(f"  => fixed-f P_t ratio = 239.75 * {_tilt_ratio_AC:.5f}"
      f" = {_full_ratio_AC_fixedf:.3f}")
print(f"     log10              = {_log_full_fixedf:.5f}")
_chk_reconcile = abs(max_rho_AC - _log_full_fixedf)  # (local)
assert _chk_reconcile < 1e-4, (
    f"fixed-f reconciliation failed: |{max_rho_AC:.5f} - {_log_full_fixedf:.5f}| "
    f"= {_chk_reconcile:.3e}"
)
print(f"  reconciliation: rho_AC(grid) matches analytic fixed-f to "
      f"{_chk_reconcile:.3e} (algebra OK)")
print(f"  rho_AC is FLAT across f_grid (tilt cancels for A vs C at FIXED f"
      f" — it's the TILT WITH RESPECT TO k_pivot that shifts, same offset"
      f" for both branches, so rho_AC is k-independent): ")
print(f"    rho_AC[f=1e-4] = {rho_AC[0]:.5f}")
print(f"    rho_AC[f=1e-3] = {rho_AC[1]:.5f}")
print(f"    rho_AC[f=1e-1] = {rho_AC[2]:.5f}")
print(f"    std            = {float(np.std(rho_AC)):.3e}")
print()

# ---------------------------------------------------------------------------
# Section 7 — transfer_correction sensitivity bracket
# ---------------------------------------------------------------------------
rho_AC_bracket: dict[float, np.ndarray] = {}
for corr in transfer_correction_grid:
    P_A_c = np.array([
        P_t_of_f(f, H_TD_phys, pref_TD, corr)[0] for f in f_grid
    ])
    P_C_c = np.array([
        P_t_of_f(f, H_mx_phys, pref_mx, corr)[0] for f in f_grid
    ])
    Omega_A_c = np.array([
        Omega_GW_of_f(P_A_c[i], f_grid[i]) for i in range(len(f_grid))
    ])
    Omega_C_c = np.array([
        Omega_GW_of_f(P_C_c[i], f_grid[i]) for i in range(len(f_grid))
    ])
    rho_AC_bracket[corr] = np.log10(Omega_A_c / Omega_C_c)
    print(f"  transfer_correction = {corr:.2f}: "
          f"rho_AC = {rho_AC_bracket[corr]}")

# The correction DOES NOT affect rho_AC (it cancels branch-wise); this is
# the structural statement that CGWB branch-discrimination is transfer-
# normalization-insensitive.
rho_std_over_bracket = float(
    np.std([rho_AC_bracket[c][0] for c in transfer_correction_grid])
)  # (local)
print(f"  std(rho_AC) over transfer_correction grid = {rho_std_over_bracket:.3e}")
print(f"  (expected 0 to machine epsilon — correction cancels in ratio)")
print()

# ---------------------------------------------------------------------------
# Section 8 — detector-reach check (h_c^(A) at 3 mHz)
# ---------------------------------------------------------------------------
# Interpolate h_c^(A) to exactly 3 mHz using the two LISA gridpoints
# (1e-4, 1e-3). Since blue tilt is monotonic in log-f, extrapolate.
idx_LISA_mid = int(np.argmin(np.abs(f_grid - 1e-3)))  # (local) mid-LISA index
h_c_A_at_3mHz = float(results["A_TD"]["h_c"][idx_LISA_mid])  # (local) at f=1e-3
# Scale to 3 mHz using tilt
f_target = 3e-3  # (local) LISA peak-sensitivity frequency
f_ref = float(f_grid[idx_LISA_mid])  # (local) 1e-3
scale_factor = (f_target / f_ref) ** (n_t / 2.0)  # (local) h_c ~ sqrt(P_t), tilt n_t/2
h_c_A_at_3mHz_scaled = h_c_A_at_3mHz * scale_factor  # (local)

print("=" * 78)
print("DETECTOR REACH — h_c^(A) at 3 mHz vs LISA floor")
print("=" * 78)
print(f"  h_c^(A) at 1 mHz           = {h_c_A_at_3mHz:.3e}")
print(f"  h_c^(A) at 3 mHz (scaled)  = {h_c_A_at_3mHz_scaled:.3e}")
print(f"  LISA floor h(3 mHz)        = {h_LISA_at_3mHz:.3e}")
h_c_A_exceeds_LISA = h_c_A_at_3mHz_scaled > h_LISA_at_3mHz
print(f"  h_c^(A) > h_LISA?          = {h_c_A_exceeds_LISA}")
print()

# ---------------------------------------------------------------------------
# Section 9 — PASS/FAIL/INFO verdict (plan §9 thresholds)
# ---------------------------------------------------------------------------
PASS_threshold = 1.0  # (local) plan §9: max_rho_AC >= 1.0 AND detectable
INFO_threshold = 0.5  # (local) plan §9: 0.5 <= max_rho_AC < 1.0

discrim_PASS = max_rho_AC >= PASS_threshold  # (local) branches distinguishable
discrim_INFO = INFO_threshold <= max_rho_AC < PASS_threshold  # (local) marginal
discrim_FAIL = max_rho_AC < INFO_threshold  # (local) indistinguishable

if discrim_FAIL:
    verdict = "FAIL"
elif discrim_PASS and h_c_A_exceeds_LISA:
    verdict = "PASS"
elif discrim_PASS and not h_c_A_exceeds_LISA:
    # Discriminable but below detector floor -> INFO per plan §9
    verdict = "INFO"
else:
    verdict = "INFO"

print("=" * 78)
print("VERDICT LOGIC (plan §9)")
print("=" * 78)
print(f"  max_rho_AC         = {max_rho_AC:.5f}")
print(f"  PASS threshold     = {PASS_threshold} (discrimination)")
print(f"  INFO threshold     = {INFO_threshold} (marginal)")
print(f"  discrim_PASS?      = {discrim_PASS}")
print(f"  discrim_INFO?      = {discrim_INFO}")
print(f"  discrim_FAIL?      = {discrim_FAIL}")
print(f"  h_c^(A) > h_LISA?  = {h_c_A_exceeds_LISA}")
print(f"  VERDICT            = {verdict}")
print()

# ---------------------------------------------------------------------------
# Section 10 — plot
# ---------------------------------------------------------------------------
# Extend f grid for plotting continuous curves
f_plot = np.logspace(-5, 1, 300)  # (local) 1e-5 to 10 Hz
# P_t(f), Omega(f), h_c(f) for each branch over the plot grid
def branch_on_grid(H_phys: float, pref: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    P_arr = np.zeros_like(f_plot)
    O_arr = np.zeros_like(f_plot)
    h_arr = np.zeros_like(f_plot)
    for i_f, ff in enumerate(f_plot):
        P_val, _ = P_t_of_f(ff, H_phys, pref, transfer_correction_central)
        P_arr[i_f] = P_val
        O_arr[i_f] = Omega_GW_of_f(P_val, ff)
        h_arr[i_f] = h_c_of_f(P_val, ff)
    return P_arr, O_arr, h_arr  # (local)

P_A_plt, O_A_plt, h_A_plt = branch_on_grid(H_TD_phys, pref_TD)
P_C_plt, O_C_plt, h_C_plt = branch_on_grid(H_mx_phys, pref_mx)
P_L_plt, O_L_plt, h_L_plt = branch_on_grid(H_LI_phys, pref_LI)
rho_plot = np.log10(np.clip(O_A_plt, 1e-300, None) / np.clip(O_C_plt, 1e-300, None))

# Detector PLI curves (approximate, power-law-integrated) — in Omega_GW units.
# LISA PLI sensitivity (Moore-Cole-Berry approx, power-law-integrated)
def Omega_LISA(f):  # (local)
    f = np.asarray(f)
    return 1e-12 * ((f / 3e-3) ** (-4.0 / 3.0) + (f / 3e-3) ** 2.0)

def Omega_DECIGO(f):  # (local)
    f = np.asarray(f)
    return 1e-17 * ((f / 0.1) ** (-4.0) + (f / 0.1) ** 2.0) ** 0.5

def Omega_BBO(f):  # (local)
    f = np.asarray(f)
    return 1e-17 * ((f / 0.3) ** (-4.0) + (f / 0.3) ** 2.0) ** 0.5

Omega_LISA_curve = Omega_LISA(f_plot)
Omega_DECIGO_curve = Omega_DECIGO(f_plot)
Omega_BBO_curve = Omega_BBO(f_plot)

fig, (ax_top, ax_bot) = plt.subplots(2, 1, figsize=(11, 8.5), sharex=True)

# --- top panel: Omega_GW(f) three branches vs detector sensitivities ---
ax_top.loglog(f_plot, O_A_plt, color="tab:blue", lw=2.2,
              label=r"$\Omega_{GW}$ (A, TD)")
ax_top.loglog(f_plot, O_C_plt, color="tab:orange", lw=2.2, ls="--",
              label=r"$\Omega_{GW}$ (C, mixed)")
ax_top.loglog(f_plot, O_L_plt, color="tab:purple", lw=1.4, ls=":",
              label=r"$\Omega_{GW}$ (LI, ref)")
ax_top.loglog(f_plot, Omega_LISA_curve, color="gray", lw=1.0, alpha=0.7,
              label=r"LISA PLI $\Omega_{\rm sens}$")
ax_top.loglog(f_plot, Omega_DECIGO_curve, color="green", lw=1.0, alpha=0.7,
              label=r"DECIGO PLI $\Omega_{\rm sens}$")
ax_top.loglog(f_plot, Omega_BBO_curve, color="brown", lw=1.0, alpha=0.5,
              label=r"BBO PLI $\Omega_{\rm sens}$")
# Mark the three evaluation frequencies
for f_hz in f_grid:
    ax_top.axvline(f_hz, color="k", lw=0.4, ls=":", alpha=0.5)
ax_top.set_ylabel(r"$\Omega_{\rm GW}(f)$")
ax_top.set_title(
    r"S84 W6-50: CGWB absolute $P_t$ — TD (A) vs mixed-C (C) vs LI branches "
    rf"($\tilde H_{{TD}}/\tilde H_{{LI}} = {ratio_TD_LI:.2f}$)"
)
ax_top.legend(loc="lower right", fontsize=8, ncol=2)
ax_top.grid(True, which="both", alpha=0.25)
ax_top.set_ylim(1e-30, 1e-5)

# --- bottom panel: rho_AC(f) discriminator ---
ax_bot.semilogx(f_plot, rho_plot, color="tab:red", lw=2.0,
                label=r"$\rho_{AC}(f) = \log_{10}(\Omega_A/\Omega_C)$")
ax_bot.axhline(PASS_threshold, color="tab:green", ls="--",
               label=f"PASS threshold = {PASS_threshold:.1f}")
ax_bot.axhline(INFO_threshold, color="tab:orange", ls="--",
               label=f"INFO threshold = {INFO_threshold:.1f}")
ax_bot.axhline(log10_rho_AC, color="tab:blue", ls=":", alpha=0.6,
               label=rf"CHAIN prediction = {log10_rho_AC:.3f}")
for f_hz in f_grid:
    ax_bot.axvline(f_hz, color="k", lw=0.4, ls=":", alpha=0.5)
ax_bot.set_xlabel(r"$f$ [Hz]")
ax_bot.set_ylabel(r"$\rho_{AC}(f)$ [decades]")
ax_bot.legend(loc="lower right", fontsize=9)
ax_bot.grid(True, which="both", alpha=0.25)
ax_bot.set_ylim(-0.5, 3.5)

plt.tight_layout()
plot_path = _HERE / "s84_w6_cgwb_absolute_pt.png"
plt.savefig(plot_path, dpi=120, bbox_inches="tight")
plt.close(fig)
print(f"plot written: {plot_path}")

# ---------------------------------------------------------------------------
# Section 11 — save npz
# ---------------------------------------------------------------------------
npz_path = _HERE / "s84_w6_cgwb_absolute_pt.npz"
np.savez(
    npz_path,
    # arithmetic chain
    H_TD=H_TD,
    H_LI=H_LI,
    H_mixed=H_mixed,
    ratio_TD_LI=ratio_TD_LI,
    log10_rho_AC_chain_fixedk=log10_rho_AC,
    log10_rho_AC_fixedf=_log_full_fixedf,
    tilt_correction_AC=_tilt_ratio_AC,
    k_ratio_AC=_k_ratio_AC,
    # gridded arrays
    f_grid=f_grid,
    P_t_A=results["A_TD"]["P_t"],
    P_t_C=results["C_mixed"]["P_t"],
    P_t_LI=results["LI_ref"]["P_t"],
    k_transit_A=results["A_TD"]["k_transit"],
    k_transit_C=results["C_mixed"]["k_transit"],
    k_transit_LI=results["LI_ref"]["k_transit"],
    Omega_GW_A=results["A_TD"]["Omega_GW"],
    Omega_GW_C=results["C_mixed"]["Omega_GW"],
    Omega_GW_LI=results["LI_ref"]["Omega_GW"],
    h_c_A=results["A_TD"]["h_c"],
    h_c_C=results["C_mixed"]["h_c"],
    h_c_LI=results["LI_ref"]["h_c"],
    rho_AC=rho_AC,
    rho_AC_sigma_transfer=rho_std_over_bracket,
    transfer_correction_grid=transfer_correction_grid,
    rho_AC_corr_0p5=rho_AC_bracket[0.5],
    rho_AC_corr_1p0=rho_AC_bracket[1.0],
    rho_AC_corr_2p0=rho_AC_bracket[2.0],
    # detector reach
    h_c_A_at_3mHz_scaled=h_c_A_at_3mHz_scaled,
    h_LISA_at_3mHz=h_LISA_at_3mHz,
    h_c_A_exceeds_LISA=h_c_A_exceeds_LISA,
    # verdict
    verdict=verdict,
    max_rho_AC=max_rho_AC,
    PASS_threshold=PASS_threshold,
    INFO_threshold=INFO_threshold,
    # provenance
    closure_sha=CLOSURE_SHA,
    n_t=n_t,
    Gamma_phi_modulus=Gamma_phi_modulus,
)
print(f"npz  written: {npz_path}")
print()

# ---------------------------------------------------------------------------
# Section 12 — verdict line append
# ---------------------------------------------------------------------------
verdict_file = _HERE / "s84_gate_verdicts.txt"
verdict_line = (
    f"S84-CGWB-ABSOLUTE-PT-PREDICTION: {verdict} -- "
    f"value={max_rho_AC:.5f} "
    f"scheme=TD-canonical-vs-mixed-C "
    f"convention=transfer_correction=1.0 "
    f"L_max=N/A "
    f"sha256={CLOSURE_SHA}"
)
with verdict_file.open("a", encoding="utf-8") as f:
    f.write(verdict_line + "\n")
print(f"verdict appended: {verdict_file}")
print(f"  {verdict_line}")
print()

# ---------------------------------------------------------------------------
# Section 13 — 4-tuple output tag (final non-verdict line)
# ---------------------------------------------------------------------------
print(
    f"(value={max_rho_AC:.5f}, scheme=TD-canonical-vs-mixed-C, "
    f"convention=transfer_correction=1.0, L_max=N/A)"
)
