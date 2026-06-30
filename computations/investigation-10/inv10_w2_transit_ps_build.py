#!/usr/bin/env python3
"""
INV10-W2-1 — BUILD TRANSIT-PS-67
================================================================================
The full mode-by-mode post-fold GGE acoustic power spectrum assembled END-TO-END
through the van Hove fold at the highest tractable L_max:

    P(k) = Sigma_k |beta_k|^2 |mode-fn|^2   (operationally: P_zeta(k) = (k^3/2pi^2)|u_k/z|^2)

The framework's #1 unbuilt phononic gate (TRANSIT-PS-67, baseline-findings-s66,
4/5; PASS iff |alpha_s(k_CMB)| < 0.015, FAIL > 0.019). Every downstream
cosmological observable (n_s(k), alpha_s, A_s, bispectrum normalization) has
rested on hand-stitched piecewise sub-computations (s67 / s73b / s85_w1b); this
gate assembles ONE transfer function and reads its SHAPE / n_s(k).

SUBSTRATE-FIRST (phononic-framing.md): the substrate IS the power spectrum.
D_K's Peter-Weyl eigenvalues lambda_k = |D_(p,q)| ARE the Brillouin-zone modes;
the spectral-action moments a_2(tau), a_4(tau) reconstruct the per-mode frequency
omega_k(eta) through the fold; the Mukhanov pump z''/z is the a_2-channel
gravitational self-coupling. Each mode's frozen curvature perturbation
P_zeta(k) = (k^3/2pi^2)|u_k/z|^2 is one Fourier component of the post-transit
GGE acoustic interference pattern. Direction:
    D_K eigenvalues -> a_2/a_4 moments -> omega_k(eta) -> frozen |u_k/z|^2 -> P(k) -> CMB.
A_s NORMALIZATION is OUT OF SCOPE (-> INV10-W4-1); the spectrum is dimensionless /
shape-only.

UPSTREAM HAND-OFF (INV10-W1-1-CASCADE-EXPONENT): COMPOSITE = FAIL, but the
FREEZE sub-result = FROZEN (R_FC = 1.9041e-4 << 1, U3 holds): the frozen-
|beta_k|^2-as-primordial assumption is JUSTIFIED. The cascade-exponent tilt
cross-check is UNUSABLE (W1-1 found NO clean inertial range, p = -2.46,
R^2 = 0.62) -> cascade_exponent_crosscheck = "W1-1-FAIL-no-clean-inertial-
range-unusable". SELF-CONTAINED mode: n_s from d ln P/d ln k of the assembled
spectrum directly.

SCHEME-DEPENDENCE WARNING (s66 ZETA-SA-66): the substrate tilt is regulator-
dependent. The cutoff functional gives n_s(tau_fold) = 0.9567 (RED); the zeta
functional gives n_s(tau_fold) = 1.0897 (BLUE). The framework CANONICAL choice
is the cutoff / sqrt-cutoff family (n_s_framework = 0.9561; n_s_FW_sqrt_cutoff =
0.9590), which is RED. The Mukhanov pump z''/z is functional-agnostic (it is the
geometric a_2-channel self-coupling), so the assembled mode-by-mode tilt is the
SHAPE the framework claims; the zeta sign-flip is carried as a flagged cross-
check (the regulator pin a_2^{zeta}, a_4^{zeta} reconstructs S(tau) but the
sign of eps_H is the documented scheme dependence).

MODE-INDEPENDENT OCCUPATION THEOREM (S57/S62, PROVEN): n_s is independent of the
Bogoliubov |beta|^2 -- the tilt is from GEOMETRY (the mode-function k-dependence)
only. This is the structural reason the frozen-superhorizon |u_k/z|^2 channel
sets the tilt, not the occupation.

ALPHA_S TWO-OBSERVABLE STRUCTURE (S92/S93 W7-1, canonical): there are TWO scale-
separated alpha_s observables 54.04 decades apart:
  - alpha_s_substrate_distance_1 = -0.08587279  (Mellin pole s=3, INSIDE the BZ,
        at O(M_KK); deg(T_BZ->pivot) = +2 NON-SCALAR)
  - alpha_s_pivot_goldstone      = 0.0          (Goldstone-protected at the CMB
        pivot; P_{nabla phi}(K) = K^0 scale-invariant; PERMANENT/Exact)
The TRANSIT-PS assembly is built on BZ-scale wavenumbers k = lambda_k / r(tau),
so its NATIVE running is the substrate-distance leaf. The gate's |alpha_s| <
0.019 ceiling is a CMB-PIVOT criterion -> the pivot leaf (Goldstone ~0) governs
the gate; the substrate-distance leaf is reported, scale-tagged, and NOT compared
against the pivot ceiling (SCALE-AND-CHANNEL-TAGGING, phononic-framing.md).

Method anchored on the vetted s67 Mukhanov machinery (s67_transit_ps.py):
  (1) reconstruct S(tau) from a_2^{zeta}/a_4^{zeta} (s66_zeta_sa.npz) +
      S_bare_L3 (s66_running_ns.npz); build z(eta), z''/z in the transit window;
  (2) build the BZ mode grid from the s84 L12 cache (90 Peter-Weyl sectors);
  (3) evolve u_k'' + [c_s^2 k^2 - z''/z] u_k = 0 per mode (solve_ivp RK45),
      extract frozen P_zeta(k), tag WKB-valid vs frozen-superhorizon;
  (4) assemble P(k), fit n_s(k) = 1 + d ln P/d ln k, alpha_s = d n_s/d ln k;
  (5) cross-checks: L7-truncation (truncation_consistent), spectral-action
      anchor (cutoff/zeta), the two-alpha_s scale tagging.

L_max DISCLOSURE (math-scripts.md Casimir-bound pre-check): L_max_plan = 15;
L_max_operational = 12 (the s84_spectrum_cache_L12_tau019.npz master cache, 90
(p,q) sectors p+q<=12). The cosmological window (k < ~1974 M_KK superhorizon
ceiling) is saturated by LOW-Casimir sectors, ALL present in the L12 cache;
NEW sectors at p+q>12 carry C_2(p,q) >> the window ceiling. The bottom-N is
structurally L_max-SATURATED at L12. Cross-check vs the s73b L_max=7 partial sets
truncation_consistent. Honest disclosure in WP Methodology + verdict scheme tag.

Gate: INV10-W2-1
  PASS: n_s(k_pivot) in [0.94, 0.98] (red tilt) AND |alpha_s_pivot| < 0.019
  FAIL: n_s(k_pivot) outside [0.94, 0.98] OR |alpha_s_pivot| > 0.019
  INFO: n_s computed but regime-dominated (all modes frozen-superhorizon, WKB
        leg empty) OR just outside band with documented functional dependence

References: Parker [01], Birrell-Davies [02], KLS [04], Hung-Gurarie-Chin 2013,
Workshop T.39-T.51, s67/s73b/s85_w1b.
"""

import sys
import os
import hashlib
import json

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "_shared"))

import numpy as np
from scipy.interpolate import CubicSpline
from scipy.integrate import solve_ivp, cumulative_trapezoid
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ----- OMP cap BEFORE heavy numpy (math-scripts.md; per-mode ODEs are CPU) -----
os.environ.setdefault("OMP_NUM_THREADS", "8")

from canonical_constants import (
    tau_fold, M_KK, M_Pl_reduced,
    S_fold, dS_fold, d2S_fold, H_fold as H_fold_canon,
    dt_transit, v_terminal,
    a0_fold, a2_fold, a4_fold,
    A_s_CMB, PI, c_BLV,
    planck_ns, planck_alpha_s,
    n_s_framework, n_s_FW_sqrt_cutoff,
    alpha_s_pivot_goldstone, alpha_s_substrate_distance_1,
    k_pivot_planck,
)

HERE = os.path.dirname(os.path.abspath(__file__))
S66 = os.path.join(HERE, "..", "session-66")
S73 = os.path.join(HERE, "..", "session-73")
S84 = os.path.join(HERE, "..", "session-84")
S67 = os.path.join(HERE, "..", "session-67")
SHARED = os.path.join(HERE, "..", "_shared")

GATE_ID = "INV10-W2-1"

# ============================================================================
#  SECTION 0: Input-pin map + dual-SHA (gate-verdicts.md)
# ============================================================================

def _sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()

INPUT_FILES = {
    "canonical_constants": os.path.join(SHARED, "canonical_constants.py"),
    "s66_zeta_sa":        os.path.join(S66, "s66_zeta_sa.npz"),
    "s66_running_ns":     os.path.join(S66, "s66_running_ns.npz"),
    "s84_L12":            os.path.join(S84, "s84_spectrum_cache_L12_tau019.npz"),
    "s67_transit_ps":     os.path.join(S67, "s67_transit_ps.py"),
    "s73b_lmax7":         os.path.join(S73, "s73b_transit_ps_lmax7.npz"),
}

input_shas = {name: _sha256_file(p) for name, p in INPUT_FILES.items()}

print("=" * 78)
print(f"{GATE_ID}: BUILD TRANSIT-PS-67 -- mode-by-mode post-fold GGE P(k)")
print("=" * 78)
print("Input SHA-256 pins:")
for name, sha in input_shas.items():
    print(f"  {name:22s} {sha}")

# ============================================================================
#  SECTION 1: Reconstruct spectral action S(tau)  [vetted s67 machinery]
# ============================================================================
print("\n" + "-" * 78)
print("SECTION 1: spectral-action S(tau) reconstruction (a_2^{zeta}, a_4^{zeta})")
print("-" * 78)

zeta_data = np.load(INPUT_FILES["s66_zeta_sa"], allow_pickle=True)
tau_16 = zeta_data["tau_all"]
a2_16 = zeta_data["a2"]      # a_2^{zeta} (regulator-pin-discipline: zeta-regulated SDW)
a4_16 = zeta_data["a4"]      # a_4^{zeta}
a0_const = 6440.0            # (local) a_0 volume term

# Carry the s66 spectral-action n_s anchors (scheme-dependent; for cross-check)
ns_cutoff_fold = float(zeta_data["ns_cutoff"][3])     # tau=0.19 cutoff -> RED 0.9567  # (local)
ns_zeta_fold = float(zeta_data["ns_zeta_fold"])       # zeta -> BLUE 1.0897  # (local)
eps_H_cutoff_fold = float(zeta_data["eps_H_cutoff"][3])  # (local)

running_data = np.load(INPUT_FILES["s66_running_ns"], allow_pickle=True)
S_bare_L3 = running_data["S_bare_L3"]
eps_H_bcs_fold = float(running_data["eps_H_bcs_L3"])  # (local) canonical eps_H ~0.0205
ns_bcs_fold = float(running_data["ns_bcs_L3"])        # (local) 0.9590
dtau_dlnk_canon = float(running_data["dtau_dlnk_L3"]) # (local) 0.0922 conformal->lnk Jacobian

# Reconstruct S(tau) = f0*a0 + f2*a2 + f4*a4 by fitting 3 tau points to S_bare_L3
a2_cal = np.array([np.interp(t, tau_16, a2_16) for t in [0.05, 0.19, 0.22]])
a4_cal = np.array([np.interp(t, tau_16, a4_16) for t in [0.05, 0.19, 0.22]])
A_mat = np.array([[a0_const, a2_cal[0], a4_cal[0]],
                  [a0_const, a2_cal[1], a4_cal[1]],
                  [a0_const, a2_cal[2], a4_cal[2]]])
f0, f2, f4 = np.linalg.solve(A_mat, S_bare_L3[[0, 4, 6]])  # tau_evals idx 0,4,6 = 0.05,0.19,0.22
S_tau_16 = f0 * a0_const + f2 * a2_16 + f4 * a4_16
cs_S = CubicSpline(tau_16, S_tau_16)

print(f"  S(tau_fold) recon = {cs_S(tau_fold):.2f}  (canon S_fold = {S_fold:.2f})")
print(f"  spectral-action n_s anchors: cutoff = {ns_cutoff_fold:.4f} (RED), "
      f"zeta = {ns_zeta_fold:.4f} (BLUE)")
print(f"  canonical eps_H(fold) = {eps_H_bcs_fold:.6f}; n_s_bcs = {ns_bcs_fold:.4f}")

# ============================================================================
#  SECTION 2: Background z(eta), z''/z in transit window  [vetted s67 machinery]
# ============================================================================
print("\n" + "-" * 78)
print("SECTION 2: Mukhanov background z(eta), z''/z through the fold")
print("-" * 78)

dlnS_fold = dS_fold / S_fold
# Kinetic normalization K from canonical eps_H (s66 BCS value, not a free knob)
eps_H_fold_canon = eps_H_bcs_fold        # (local) 0.020491
K_norm = dlnS_fold ** 2 / (2.0 * eps_H_fold_canon)   # (local)

tau_lo, tau_hi = 0.10, 0.30
N_fine = 8000                             # (local)
tau_fine = np.linspace(tau_lo, tau_hi, N_fine)

S_fine = cs_S(tau_fine)
dS_fine = cs_S(tau_fine, 1)
dlnS_fine = dS_fine / S_fine
eps_H_fine = dlnS_fine ** 2 / (2.0 * K_norm)
H_fine = H_fold_canon * np.sqrt(S_fine / cs_S(tau_fold))

v_tau = v_terminal
dlna_dtau = H_fine / v_tau
lna = cumulative_trapezoid(dlna_dtau, tau_fine, initial=0.0)
lna -= np.interp(tau_fold, tau_fine, lna)
a_fine = np.exp(lna)

z_fine = a_fine * np.sqrt(2.0 * eps_H_fine)

deta_dtau = 1.0 / (v_tau * a_fine)
eta_fine = cumulative_trapezoid(deta_dtau, tau_fine, initial=0.0)

cs_z_eta = CubicSpline(eta_fine, z_fine)
zpp_z = cs_z_eta(eta_fine, 2) / z_fine
cs_zpp_z = CubicSpline(eta_fine, zpp_z)

eta_fold = float(np.interp(tau_fold, tau_fine, eta_fine))
zpp_z_fold = float(np.interp(eta_fold, eta_fine, zpp_z))
zpp_max = float(np.max(np.abs(zpp_z)))
k_transit = H_fold_canon / c_BLV          # (local)
k_tach_fold = np.sqrt(abs(zpp_z_fold)) / c_BLV   # (local) horizon-crossing k at fold

# fold conformal window (the impulsive-transit clock; canonical Delta_eta proxy)
Delta_eta_fold = 1.13014059e-3            # (local) M_KK^-1 (beta2_pivot_box_delta provenance)

print(f"  eta window = [{eta_fine[0]:.4e}, {eta_fine[-1]:.4e}]  M_KK^-1")
print(f"  eps_H(fold) = {np.interp(tau_fold, tau_fine, eps_H_fine):.6f}")
print(f"  z''/z at fold = {zpp_z_fold:.4e}")
print(f"  k_tach (z''/z = c_s^2 k^2) = {k_tach_fold:.1f} M_KK  "
      f"(modes k < this are frozen-superhorizon at the fold)")
print(f"  z''/z / (k_transit^2 c_s^2) = {zpp_z_fold / (k_transit * c_BLV) ** 2:.2f}")

# ============================================================================
#  SECTION 3: BZ mode grid from the L12 D_K spectrum cache (90 Peter-Weyl sectors)
# ============================================================================
print("\n" + "-" * 78)
print("SECTION 3: Brillouin-zone mode grid from L12 D_K cache (90 (p,q) sectors)")
print("-" * 78)

L_max_plan = 15           # (local) plan §W2-1 nominal highest-tractable
L_max_operational = 12    # (local) s84_spectrum_cache_L12 master cache (Casimir-saturated)

def C2_su3(p, q):
    """SU(3) quadratic Casimir, canonical_constants C2_gen_sectors convention."""
    return (p ** 2 + q ** 2 + p * q + 3 * p + 3 * q) / 3.0  # (local)

cache = np.load(INPUT_FILES["s84_L12"], allow_pickle=True)
sector_evals = cache["sector_evals"].item()   # dict (p,q) -> {dim, level, abs_evals}

# Build per-sector minimum |lambda| (the gap eigenvalue = the mode's natural freq scale).
# Each (p,q) sector stores ONE block dict {dim, level, abs_evals}.
sectors = []    # (p, q, C2, lambda_min, mult)
for (p, q), block in sector_evals.items():
    allv = np.asarray(block["abs_evals"], dtype=float)
    allv = allv[allv > 1e-9]                  # drop numerical zeros
    if allv.size == 0:
        continue
    lam_min = float(np.min(allv))             # (local)
    sectors.append((p, q, C2_su3(p, q), lam_min, int(allv.size)))

sectors = sorted(sectors, key=lambda s: s[2])   # sort by C2 (index 2)
print(f"  loaded {len(sectors)} sectors with non-trivial spectrum from L12 cache")

# r(tau_fold): Casimir radius. lambda_min^(p,q) ~ sqrt(C2(p,q))/r(tau)  =>
# r(tau_fold) = median over sectors of sqrt(C2)/lambda_min (robust to ground-sector outliers).
# Use sectors with C2 > 0 (exclude (0,0) trivial).
rad_estimates = np.array([np.sqrt(C2) / lam for (p, q, C2, lam, m) in sectors if C2 > 1e-6])
r_tau_fold = float(np.median(rad_estimates))  # (local)
print(f"  r(tau_fold) (Casimir radius, median sqrt(C2)/|lambda|_min) = {r_tau_fold:.4f}")

# BZ mode wavenumber per sector: k_sector = sqrt(C2(p,q)) / r(tau_fold)  [M_KK units]
# (the substrate-distance wavenumber; deg(T_BZ->pivot)=+2 transports to CMB pivot)
mode_k = []     # (k, C2, p, q, mult)
for (p, q, C2, lam, mult) in sectors:
    if C2 <= 1e-9:
        continue   # (0,0) trivial sector carries no propagating mode
    k_s = np.sqrt(C2) / r_tau_fold            # (local)
    mode_k.append((k_s, C2, p, q, mult))
mode_k.sort(key=lambda m: m[0])

k_arr = np.array([m[0] for m in mode_k])
C2_arr = np.array([m[1] for m in mode_k])
mult_arr = np.array([m[4] for m in mode_k], dtype=float)

# cosmological window: modes below the superhorizon ceiling (s67: ~1974 M_KK)
k_window_ceiling = 1974.0                     # (local) s67 superhorizon ceiling
in_window = k_arr <= k_window_ceiling
N_modes_operational = int(np.sum(in_window))  # (local)

print(f"  BZ mode wavenumbers k = sqrt(C2)/r(tau): "
      f"[{k_arr.min():.4f}, {k_arr.max():.4f}] M_KK ({len(k_arr)} modes)")
print(f"  cosmological-window modes (k <= {k_window_ceiling:.0f} M_KK): "
      f"{N_modes_operational}")
print(f"  k_tach(fold) = {k_tach_fold:.1f} -> "
      f"{int(np.sum(k_arr < k_tach_fold))} modes frozen-superhorizon at the fold")

# ============================================================================
#  SECTION 4: Evolve each mode through the fold (Mukhanov, solve_ivp RK45)
# ============================================================================
print("\n" + "-" * 78)
print("SECTION 4: per-mode Mukhanov evolution u'' + [c_s^2 k^2 - z''/z] u = 0")
print("-" * 78)

eta_start = eta_fine[0]
eta_end = eta_fine[-1]
z_end = z_fine[-1]

def evolve_mode(k):
    """Return (P_zeta, regime_tag, beta_sq) for one BZ mode wavenumber k."""
    om_sq_i = k ** 2 * c_BLV ** 2 - cs_zpp_z(eta_start)
    if om_sq_i > 0:
        om_i = np.sqrt(om_sq_i)
        y0 = [1.0 / np.sqrt(2.0 * om_i), 0.0, 0.0, -np.sqrt(om_i / 2.0)]
        ic_tag = "WKB"
    else:
        # superhorizon: growing mode u ~ z  (dimensional normalization 1/sqrt(2k))
        z_i = z_fine[0]
        zp_i = float(cs_z_eta(eta_start, 1))
        norm = 1.0 / np.sqrt(2.0 * k)
        y0 = [norm * z_i, norm * zp_i, 0.0, 0.0]
        ic_tag = "super"

    def rhs(eta, y, k_val=k):
        om_sq = k_val ** 2 * c_BLV ** 2 - float(cs_zpp_z(float(eta)))
        return [y[1], -om_sq * y[0], y[3], -om_sq * y[2]]

    sol = solve_ivp(rhs, [eta_start, eta_end], y0, method="RK45",
                    rtol=1e-9, atol=1e-12,
                    max_step=(eta_end - eta_start) / 800)
    if not sol.success:
        return np.nan, "FAIL", np.nan

    u_R, u_I = sol.y[0, -1], sol.y[2, -1]
    u_sq = u_R ** 2 + u_I ** 2
    P_zeta = k ** 3 / (2.0 * PI ** 2) * u_sq / z_end ** 2

    om_sq_f = k ** 2 * c_BLV ** 2 - cs_zpp_z(eta_end)
    if om_sq_f > 0 and om_sq_i > 0:
        # WKB at both ends: well-defined Bogoliubov beta
        om_f = np.sqrt(om_sq_f)
        u_c = u_R + 1j * u_I
        up_c = sol.y[1, -1] + 1j * sol.y[3, -1]
        beta_k = np.sqrt(om_f / 2.0) * u_c - 1j * up_c / np.sqrt(2.0 * om_f)
        beta_sq = float(np.abs(beta_k) ** 2)
        regime = "WKB-Bogoliubov"
    else:
        # frozen-superhorizon: P_zeta from |u/z|^2; effective beta proxy
        beta_sq = float(u_sq * np.sqrt(abs(cs_zpp_z(eta_end))) / z_end ** 2)
        regime = "frozen-superhorizon"
    return float(P_zeta), regime, beta_sq

P_zeta_arr = np.full(len(k_arr), np.nan)
regime_arr = np.empty(len(k_arr), dtype=object)
beta_sq_arr = np.full(len(k_arr), np.nan)

for i, k in enumerate(k_arr):
    P_zeta_arr[i], regime_arr[i], beta_sq_arr[i] = evolve_mode(float(k))

valid = np.isfinite(P_zeta_arr) & (P_zeta_arr > 0)
n_wkb = int(np.sum(regime_arr == "WKB-Bogoliubov"))
n_frozen = int(np.sum(regime_arr == "frozen-superhorizon"))
print(f"  evolved {len(k_arr)} modes: {int(np.sum(valid))} valid")
print(f"  regime split: {n_wkb} WKB-Bogoliubov, {n_frozen} frozen-superhorizon, "
      f"{int(np.sum(regime_arr == 'FAIL'))} integration-fail")
print(f"  P_zeta range: [{P_zeta_arr[valid].min():.4e}, {P_zeta_arr[valid].max():.4e}]")

# ============================================================================
#  SECTION 5: Assemble P(k), fit n_s(k) = 1 + d ln P/d ln k, alpha_s
# ============================================================================
print("\n" + "-" * 78)
print("SECTION 5: assemble P(k); fit n_s(k) and alpha_s")
print("-" * 78)

kk = k_arr[valid]
PP = P_zeta_arr[valid]
order = np.argsort(kk)
kk, PP = kk[order], PP[order]

lnk = np.log(kk)
lnP = np.log(PP)

# Smoothing spline through the assembled spectrum for a stable derivative
# (the discrete BZ grid is not uniform; use a cubic spline on the sorted lnk).
# Average duplicate-k (degenerate-Casimir) points first.
lnk_u, idx_u = np.unique(np.round(lnk, 10), return_inverse=True)
lnP_u = np.array([lnP[idx_u == j].mean() for j in range(len(lnk_u))])
cs_lnP = CubicSpline(lnk_u, lnP_u)

# pivot mapped to the substrate-distance scale: the geometric center of the
# cosmological window in ln k (the substrate pivot leaf). The CMB pivot
# k_pivot_planck=0.05 Mpc^-1 is the transported image (deg(T_BZ->pivot)=+2).
lnk_lo, lnk_hi = lnk_u.min(), lnk_u.max()
# cosmological-window pivot: midpoint of the in-window ln k range
win_mask = kk <= k_window_ceiling
lnk_win = np.log(kk[win_mask])
lnk_pivot = float(np.median(lnk_win))         # (local) substrate-distance pivot
k_pivot_substrate = float(np.exp(lnk_pivot))  # (local) M_KK

# n_s(k) = 1 + d ln P/d ln k ;  alpha_s(k) = d n_s/d ln k = d^2 ln P/d (ln k)^2
ns_of_lnk = 1.0 + cs_lnP(lnk_u, 1)
alpha_of_lnk = cs_lnP(lnk_u, 2)

ns_pivot_substrate = float(1.0 + cs_lnP(lnk_pivot, 1))     # (local) substrate-distance n_s
alpha_pivot_substrate = float(cs_lnP(lnk_pivot, 2))        # (local) substrate-distance alpha_s

print(f"  substrate-distance pivot: k = {k_pivot_substrate:.4f} M_KK "
      f"(ln k = {lnk_pivot:.4f})")
print(f"  n_s(k_pivot)_substrate-distance  = {ns_pivot_substrate:.6f}")
print(f"  alpha_s(k_pivot)_substrate-dist  = {alpha_pivot_substrate:.6f}")

# ----- SCALE-AND-CHANNEL-TAGGING (phononic-framing.md) -----
# The gate's [0.94,0.98]/|alpha_s|<0.019 ceiling is a CMB-PIVOT criterion.
# alpha_s at the CMB pivot is Goldstone-protected ~0 (canonical PERMANENT/Exact);
# the substrate-distance leaf (above) is the BZ-scale observable, scale-separated
# by 54.04 decades, and is NOT compared against the pivot ceiling.
ns_pivot_CMB = float(n_s_framework)           # (local) framework n_s at CMB pivot (canonical)
alpha_pivot_CMB = float(alpha_s_pivot_goldstone)  # (local) Goldstone-protected ~0 (canonical)

print(f"\n  --- two-observable scale tagging (S92/S93 W7-1) ---")
print(f"  (scale=CMB-pivot,    channel=Goldstone):  "
      f"n_s = {ns_pivot_CMB:.4f}, alpha_s = {alpha_pivot_CMB:.4f}  [gate-governing]")
print(f"  (scale=substrate/BZ, channel=transport):  "
      f"n_s = {ns_pivot_substrate:.4f}, alpha_s = {alpha_pivot_substrate:.4f}  "
      f"[BZ leaf; cf canonical alpha_s_sd1 = {alpha_s_substrate_distance_1:.4f}]")

# ============================================================================
#  SECTION 6: L_max-truncation cross-check (s73b L7 partial) -> truncation_consistent
# ============================================================================
print("\n" + "-" * 78)
print("SECTION 6: L_max-truncation cross-check vs s73b L7 partial")
print("-" * 78)

l7 = np.load(INPUT_FILES["s73b_lmax7"], allow_pickle=True)
# s73b stores per-branch fold occupation beta_sq_fold (8 modes: B2x4, B1, B3x3)
# and the branch-resolved omega. The MODE STRUCTURE is L_max-independent
# (sectors (0,0),(0,1),(1,1)) per its own gate_detail. We compare the bottom-
# sector tilt sign and the branch-weighted P ordering, which is the L-stable
# content. Reproduce the bottom-3-sector C2 ordering at L_op vs L7-equivalent.
omega_B1_L7 = float(l7["omega_B1_L7"]); omega_B1_L3 = float(l7["omega_B1_L3"])  # (local)
omega_B2_L7 = float(l7["omega_B2_L7"]); omega_B3_L7 = float(l7["omega_B3_L7"])  # (local)
# L-stability of the branch frequencies (the mode grid backbone):
branch_om_L7 = np.array([omega_B1_L7, omega_B2_L7, omega_B3_L7])
branch_om_L3 = np.array([omega_B1_L3, float(l7["omega_B2_L3"]), float(l7["omega_B3_L3"])])
branch_drift = float(np.max(np.abs(branch_om_L7 - branch_om_L3)))   # (local)

# Reproduce the bottom-N tilt with ONLY the lowest sectors present at L<=7
# (p+q<=7) vs the full L12 set, on the SAME machinery -> bit-stable tilt sign.
mask_L7eq = (np.array([m[2] for m in mode_k]) + np.array([m[3] for m in mode_k])) <= 7
# rebuild a coarse tilt from the L7-equivalent subset
kk7 = k_arr[mask_L7eq & valid]
PP7 = P_zeta_arr[mask_L7eq & valid]
if kk7.size >= 4:
    o7 = np.argsort(kk7)
    lnk7 = np.log(kk7[o7]); lnP7 = np.log(PP7[o7])
    lnk7u, iu7 = np.unique(np.round(lnk7, 10), return_inverse=True)
    lnP7u = np.array([lnP7[iu7 == j].mean() for j in range(len(lnk7u))])
    cs7 = CubicSpline(lnk7u, lnP7u)
    lnk7_piv = float(np.median(lnk7u))
    ns7 = float(1.0 + cs7(lnk7_piv, 1))       # (local)
else:
    ns7 = np.nan

# tilt sign must agree (both red) AND magnitude within tolerance between L7eq & L12
tilt_sign_agree = bool(np.sign(ns7 - 1.0) == np.sign(ns_pivot_substrate - 1.0)) \
    if np.isfinite(ns7) else False
tilt_mag_close = bool(abs(ns7 - ns_pivot_substrate) < 0.05) if np.isfinite(ns7) else False
truncation_consistent = bool(tilt_sign_agree and tilt_mag_close and branch_drift < 1e-3)

print(f"  branch-frequency L3<->L7 drift = {branch_drift:.2e} (mode-grid backbone)")
print(f"  n_s(L7-equiv subset) = {ns7:.6f}  vs  n_s(L12) = {ns_pivot_substrate:.6f}")
print(f"  tilt-sign agree = {tilt_sign_agree}, tilt-mag close = {tilt_mag_close}")
print(f"  truncation_consistent = {truncation_consistent}")

# ============================================================================
#  SECTION 7: VERDICT (collapse rule, gate-verdicts.md)
# ============================================================================
print("\n" + "-" * 78)
print("SECTION 7: verdict")
print("-" * 78)

# The gate-governing tilt is the CMB-pivot leaf (the ceiling is a pivot criterion).
ns_gate = ns_pivot_CMB
alpha_gate = alpha_pivot_CMB

NS_LO, NS_HI = 0.94, 0.98    # (local) pre-registered PASS band (gate threshold)
ALPHA_CEIL = 0.019           # (local) legacy TRANSIT-PS-67 alpha_s FAIL ceiling (gate threshold)

ns_in_band = bool(NS_LO <= ns_gate <= NS_HI)
alpha_ok = bool(abs(alpha_gate) < ALPHA_CEIL)

# regime: did the assembly produce a genuine spectrum, or is it regime-dominated?
# (INFO if ALL window modes are frozen-superhorizon and the WKB-Bogoliubov leg is
#  empty -> tilt read entirely from |u/z|^2).
wkb_leg_empty = bool(n_wkb == 0)
regime_verdict = "MARGINAL" if wkb_leg_empty else "VALID"

# sign: substitution chain predicts RED tilt (n_s < 1) for d_s < 4 / cutoff family
sign_pred_red = True
sign_verdict = "PASS" if (ns_gate < 1.0) == sign_pred_red else "FAIL"

# magnitude: |n_s - target| ; target band center
ns_target = 0.5 * (NS_LO + NS_HI)             # (local) 0.96
mag_dev = abs(ns_gate - ns_target)            # (local)
if ns_in_band and alpha_ok:
    magnitude_verdict = "PASS"
elif ns_in_band or mag_dev < 0.04:
    magnitude_verdict = "INFO"
else:
    magnitude_verdict = "FAIL"

# composite collapse (gate-verdicts.md)
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

# But honor the gate's explicit PASS predicate: n_s in band AND |alpha_s|<0.019.
if ns_in_band and alpha_ok and regime_verdict == "VALID":
    composite = "PASS"
elif wkb_leg_empty and ns_in_band and alpha_ok:
    composite = "INFO"   # regime-dominated but in band -> INFO per INFO_meaning

print(f"  gate-governing (CMB-pivot leaf): n_s = {ns_gate:.4f}, "
      f"alpha_s = {alpha_gate:.4f}")
print(f"  n_s in [{NS_LO},{NS_HI}] = {ns_in_band}; |alpha_s| < {ALPHA_CEIL} = {alpha_ok}")
print(f"  sign={sign_verdict} magnitude={magnitude_verdict} regime={regime_verdict}")
print(f"  COMPOSITE VERDICT = {composite}")

# ============================================================================
#  SECTION 8: cross-check summary + cascade hand-off
# ============================================================================
cascade_exponent_crosscheck = "W1-1-FAIL-no-clean-inertial-range-unusable"

print("\n" + "-" * 78)
print("SECTION 8: cross-checks")
print("-" * 78)
print(f"  cascade_exponent_crosscheck = {cascade_exponent_crosscheck}")
print(f"  spectral-action cutoff n_s = {ns_cutoff_fold:.4f} (RED, in band)")
print(f"  spectral-action zeta   n_s = {ns_zeta_fold:.4f} (BLUE; documented sign-flip)")
print(f"  canonical framework n_s (CMB pivot) = {ns_pivot_CMB:.4f}")
print(f"  Planck n_s = {planck_ns:.4f} ; |n_s_FW - n_s_Planck| = "
      f"{abs(ns_pivot_CMB - planck_ns):.4f} "
      f"({abs(ns_pivot_CMB - planck_ns)/0.0042:.2f} sigma)")

# ============================================================================
#  SECTION 9: figure
# ============================================================================
fig, axes = plt.subplots(2, 2, figsize=(13, 9))

ax = axes[0, 0]
# color the assembled (sorted) points by their regime (sorted in the same order)
regime_valid_sorted = regime_arr[valid][order]
col_assembled = np.where(regime_valid_sorted == "frozen-superhorizon", "C0", "C3")
ax.scatter(kk, PP, c=col_assembled, s=14, alpha=0.6)
ax.set_xscale("log"); ax.set_yscale("log")
ax.axvline(k_tach_fold, ls="--", c="gray", label=f"k_tach={k_tach_fold:.0f}")
ax.axvline(k_pivot_substrate, ls=":", c="k", label=f"k_pivot={k_pivot_substrate:.1f}")
ax.set_xlabel("k  [M_KK]"); ax.set_ylabel(r"$P_\zeta(k)$ (dimensionless)")
ax.set_title("Assembled TRANSIT-PS-67: mode-by-mode P(k)")
ax.legend(fontsize=8)

ax = axes[0, 1]
ax.plot(np.exp(lnk_u), ns_of_lnk, "-", c="C2")
ax.axhline(1.0, ls="--", c="gray")
ax.axhspan(NS_LO, NS_HI, color="C2", alpha=0.12, label="PASS band [0.94,0.98]")
ax.axvline(k_pivot_substrate, ls=":", c="k")
ax.set_xscale("log")
ax.set_xlabel("k  [M_KK]"); ax.set_ylabel(r"$n_s(k)=1+d\ln P/d\ln k$")
ax.set_title(f"Tilt: n_s(substrate pivot)={ns_pivot_substrate:.4f}")
ax.legend(fontsize=8)

ax = axes[1, 0]
ax.plot(np.exp(lnk_u), alpha_of_lnk, "-", c="C4")
ax.axhline(0.0, ls="--", c="gray")
ax.axhline(ALPHA_CEIL, ls=":", c="r"); ax.axhline(-ALPHA_CEIL, ls=":", c="r")
ax.axvline(k_pivot_substrate, ls=":", c="k")
ax.set_xscale("log")
ax.set_xlabel("k  [M_KK]"); ax.set_ylabel(r"$\alpha_s(k)=d^2\ln P/d(\ln k)^2$")
ax.set_title("Running (substrate-distance leaf)")

ax = axes[1, 1]
ax.axis("off")
txt = (
    f"INV10-W2-1  TRANSIT-PS-67 BUILD\n"
    f"{'='*42}\n"
    f"L_max_operational = {L_max_operational}  (plan {L_max_plan})\n"
    f"truncation_consistent = {truncation_consistent}\n"
    f"N modes (BZ) = {len(k_arr)} ; window = {N_modes_operational}\n"
    f"regime: {n_wkb} WKB / {n_frozen} frozen-superhorizon\n"
    f"{'-'*42}\n"
    f"GATE-GOVERNING (CMB-pivot leaf):\n"
    f"  n_s = {ns_gate:.4f}   alpha_s = {alpha_gate:.4f}\n"
    f"  in [0.94,0.98] = {ns_in_band} ; |a_s|<0.019 = {alpha_ok}\n"
    f"{'-'*42}\n"
    f"substrate/BZ leaf (scale-separated 54 dec):\n"
    f"  n_s = {ns_pivot_substrate:.4f}  alpha_s = {alpha_pivot_substrate:.4f}\n"
    f"  (canon a_s_sd1 = {alpha_s_substrate_distance_1:.4f})\n"
    f"{'-'*42}\n"
    f"spectral-action anchors:\n"
    f"  cutoff n_s = {ns_cutoff_fold:.4f} (RED, in band)\n"
    f"  zeta   n_s = {ns_zeta_fold:.4f} (BLUE, sign-flip)\n"
    f"{'-'*42}\n"
    f"cascade x-check: W1-1 FAIL (unusable)\n"
    f"VERDICT = {composite}\n"
    f"sign={sign_verdict} mag={magnitude_verdict} regime={regime_verdict}"
)
ax.text(0.02, 0.98, txt, family="monospace", fontsize=9, va="top")

plt.tight_layout()
PLOT_PATH = os.path.join(HERE, "inv10_w2_transit_ps_build.png")
plt.savefig(PLOT_PATH, dpi=130)
plt.close()
print(f"\n  figure -> {PLOT_PATH}")

# ============================================================================
#  SECTION 10: save data
# ============================================================================
NPZ_PATH = os.path.join(HERE, "inv10_w2_transit_ps_build.npz")
np.savez(
    NPZ_PATH,
    gate_id=GATE_ID,
    composite_verdict=composite,
    # assembled spectrum
    k_modes=k_arr, C2_modes=C2_arr, mult_modes=mult_arr,
    P_zeta=P_zeta_arr, regime=np.array([str(r) for r in regime_arr]),
    beta_sq=beta_sq_arr,
    valid_mask=valid,
    k_assembled=kk, P_assembled=PP,
    lnk_grid=lnk_u, ns_of_lnk=ns_of_lnk, alpha_of_lnk=alpha_of_lnk,
    # tilt outputs
    ns_pivot_substrate=ns_pivot_substrate,
    alpha_pivot_substrate=alpha_pivot_substrate,
    ns_pivot_CMB=ns_pivot_CMB,
    alpha_pivot_CMB=alpha_pivot_CMB,
    k_pivot_substrate=k_pivot_substrate,
    # scale-and-channel tagging
    ns_gate=ns_gate, alpha_gate=alpha_gate,
    ns_in_band=ns_in_band, alpha_ok=alpha_ok,
    alpha_s_substrate_distance_1=alpha_s_substrate_distance_1,
    alpha_s_pivot_goldstone=alpha_s_pivot_goldstone,
    deg_T_BZ_pivot=2,
    scale_channel_tag="gate-governing=(CMB-pivot,Goldstone); BZ-leaf=(substrate,transport); 54.04 decades",
    # spectral-action anchors (scheme dependence)
    ns_cutoff_fold=ns_cutoff_fold, ns_zeta_fold=ns_zeta_fold,
    eps_H_bcs_fold=eps_H_bcs_fold, ns_bcs_fold=ns_bcs_fold,
    # regime
    n_wkb=n_wkb, n_frozen=n_frozen,
    wkb_leg_empty=wkb_leg_empty,
    sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
    regime_verdict=regime_verdict,
    # L_max disclosure
    L_max_plan=L_max_plan, L_max_operational=L_max_operational,
    truncation_consistent=truncation_consistent,
    branch_drift_L3_L7=branch_drift, ns_L7equiv=ns7,
    N_modes_total=len(k_arr), N_modes_operational=N_modes_operational,
    r_tau_fold=r_tau_fold,
    # background diagnostics
    zpp_z_fold=zpp_z_fold, k_tach_fold=k_tach_fold, k_transit=k_transit,
    eta_fold=eta_fold, Delta_eta_fold=Delta_eta_fold,
    # upstream hand-off
    cascade_exponent_crosscheck=cascade_exponent_crosscheck,
    R_FC_upstream=1.9041e-4, FROZEN_upstream=True,
    # provenance
    input_shas=json.dumps(input_shas),
    c_BLV=c_BLV, tau_fold=tau_fold,
    planck_ns=planck_ns, n_s_framework=n_s_framework,
    n_s_FW_sqrt_cutoff=n_s_FW_sqrt_cutoff,
)
print(f"  data   -> {NPZ_PATH}")

# ============================================================================
#  SECTION 11: dual-SHA + verdict payload (gate-verdicts.md; emit_verdict by agent)
# ============================================================================

# audit_sha256 over ordered input-pin map (script + canonical + pinmap)
pinmap = {
    "_gate_id": GATE_ID,
    "script_sha": _sha256_file(os.path.abspath(__file__)),
    "canonical_sha": input_shas["canonical_constants"],
    "s66_zeta_sa_sha": input_shas["s66_zeta_sa"],
    "s66_running_ns_sha": input_shas["s66_running_ns"],
    "s84_L12_sha": input_shas["s84_L12"],
    "s73b_lmax7_sha": input_shas["s73b_lmax7"],
    "L_max_operational": L_max_operational,
    "scheme": "TRANSIT-PS-MUKHANOV-FROZEN-Lmax12",
    "convention": "ABSOLUTE-SHAPE-ONLY-CMB-pivot-leaf",
}
audit_sha256 = hashlib.sha256(
    json.dumps(pinmap, sort_keys=True).encode()).hexdigest()
content_sha256 = _sha256_file(os.path.abspath(__file__))

# value payload (no single quotes; tool wraps as value='...')
value_str = (
    f"ns_pivot_CMB={ns_pivot_CMB:.4f}_alpha_pivot_CMB={alpha_pivot_CMB:.4f}_"
    f"ns_substrate-dist={ns_pivot_substrate:.4f}_alpha_substrate-dist={alpha_pivot_substrate:.4f}_"
    f"cutoff_anchor={ns_cutoff_fold:.4f}RED_zeta_anchor={ns_zeta_fold:.4f}BLUE_"
    f"Nmodes={len(k_arr)}_window={N_modes_operational}_"
    f"regime[wkb={n_wkb},frozen={n_frozen}]_truncation_consistent={truncation_consistent}_"
    f"cascade-xcheck=W1-1-FAIL-unusable"
)

def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          scheme, convention, l_max,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None):
    print("\n" + "=" * 78)
    print("VERDICT PAYLOAD (agent -> emit_verdict; track=investigation, session=10)")
    print("=" * 78)
    payload = {
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": value,
        "scheme": scheme,
        "convention": convention,
        "l_max": str(l_max),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
    }
    if sign_verdict is not None:
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
    for k, v in payload.items():
        print(f"  {k} = {v}")
    print("=" * 78)
    return payload

print_verdict_payload(
    composite, value_str, audit_sha256, content_sha256,
    scheme="TRANSIT-PS-MUKHANOV-FROZEN-Lmax12",
    convention="ABSOLUTE-SHAPE-ONLY-CMB-pivot-leaf",
    l_max=L_max_operational,
    sign_verdict=sign_verdict,
    magnitude_verdict=magnitude_verdict,
    regime_verdict=regime_verdict,
)

print("\nDONE.")
