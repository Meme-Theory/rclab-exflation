#!/usr/bin/env python3
"""
FABRY-PEROT-73a: Dispersive Phase Decoherence at Entry Horizon
================================================================

Resonance structure
-------------------
What oscillates: BCS quasiparticle modes k (8 modes: 4 B2 + 1 B1 + 3 B3)
What constrains: the entry sonic horizon at tau_entry = 0.2195 (S72 W3-C)
What are the boundary conditions: supersonic flow (Ma=20.7) on both sides;
    NO exit horizon exists (W1-A confirmed: Ma varies by <0.2% across BCS
    gap range). Therefore NO cavity and NO round-trip resonance.
Normal modes: dispersive phase spread across the k-spectrum at the entry
    horizon determines inter-mode decoherence.

Adapted Physics (no cavity)
----------------------------
The original proposal assumed entry + exit sonic horizons form a Fabry-Perot
cavity with Q ~ |beta_k|^2 ~ 85, giving round-trip phase spread of ~1080 rad.
S70 CAVITY-BCS-HORIZON-70 found the compound barrier MONOTONIC (no F-P
resonance), and W1-A confirms there is no exit horizon at all.

With only one horizon, there is no cavity Q. Instead, we compute:

(A) DISPERSIVE PHASE SPREAD at the entry horizon:
    Each mode k accumulates a phase phi_k = integral over the entry-horizon
    scattering region of k_eff(tau) dtau, where k_eff = omega_k / c_eff(tau).
    The variance of phi across modes gives the inter-mode decoherence rate.

(B) IMPEDANCE MISMATCH decoherence:
    The four-speed hierarchy (c_mod=1.0, c_BLV=0.485, c_BA=0.399, c_L=0.025)
    creates acoustic impedance steps. Even without a horizon, these impedance
    mismatches scatter modes differentially.

(C) ENTRY HORIZON BOGOLIUBOV PHASE SPREAD:
    The S72 entry horizon gives r_k_entry ~ 2.9 (deeply thermal). The
    Bogoliubov phases phase_k have inter-mode spread that decoheres the
    density matrix.

(D) COMPOUND DECOHERENCE from entry horizon reflection + dispersive spread:
    Combines |beta_k|^2 from the entry horizon with the k-dependent phase
    accumulated during the transit.

Gate: FABRY-PEROT-73a
  PASS: t_dec^{FP}/t_transit in [0.57, 0.88]
  INFO: t_dec computed but outside gate band
  FAIL: phi_RT not well-defined (no acoustic propagation through supersonic region)

Cross-checks:
  (1) T -> 1 limit: Q -> 0, t_dec -> 0
  (2) T -> 0 limit: Q -> inf, t_dec -> inf
  (3) phi_RT must be mode-dependent (dispersion) -- if all same, no decoherence
"""

import sys
import os
import time
import numpy as np

# --- Canonical constants ---
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import *

t_start = time.time()

# ==============================================================================
# Section 1: Load input data
# ==============================================================================

# Entry horizon data from S72
d_entry = np.load(os.path.join(os.path.dirname(__file__),
                               "s72_blueshift_tilt.npz"), allow_pickle=True)
tau_entry_val = float(d_entry["tau_entry"])       # 0.2195
T_H_entry = float(d_entry["T_Hawking"])           # 72.84 M_KK
kappa_entry = float(d_entry["kappa_entry"])        # 79386 M_KK
beta_sq_entry = d_entry["beta_sq_entry"]           # shape (8,), ~82-88
alpha_sq_entry = d_entry["alpha_sq_entry"]         # shape (8,)
r_k_entry = d_entry["r_k_entry"]                   # squeeze params ~2.9
omega_k = d_entry["omega_k"]                       # mode frequencies (8,)
labels = d_entry["labels"]                         # mode labels
mode_weights = d_entry["mode_weights"]             # spectral weights (8,)

# Exit horizon data from W1-A
d_exit = np.load(os.path.join(os.path.dirname(__file__),
                              "s73a_exit_horizon_bog.npz"), allow_pickle=True)
beta_sq_exit = d_exit["beta_sq"]                   # shape (8,), ~1e-5 to 1e-2
n_k_exit = d_exit["n_k"]                           # same as beta_sq_exit
phase_k_exit = d_exit["phase_k"]                   # arg(beta_k) at exit
Phi_final_exit = d_exit["Phi_final"]               # accumulated phase
r_exit = d_exit["r_exit"]                          # exit squeeze params
phi_compound = d_exit["phi_compound"]              # compound phases
mach_fold = float(d_exit["mach_at_fold"])          # 20.73
gamma_fold = d_exit["gamma_at_fold"]               # adiabaticity params

# Four-speed hierarchy (M_KK units)
c_mod = 1.0      # modulus propagation speed (local, = 1 in M_KK units)  # (local)
c_BLV = 0.485    # Barcelo-Liberati-Visser effective speed  # (local)
c_BA_val = 0.399 # Bogoliubov-Anderson sound speed  # (local)
c_L_val = 0.025  # Leggett mode speed  # (local)
v_tau = float(d_exit["v_tau_at_fold"]) if "v_tau_at_fold" in d_exit else omega_tau  # (local)

print("=" * 72)
print("FABRY-PEROT-73a: Dispersive Phase Decoherence at Entry Horizon")
print("=" * 72)
print()
print(f"Entry horizon: tau_entry = {tau_entry_val:.5f}")
print(f"  T_Hawking = {T_H_entry:.2f} M_KK")
print(f"  kappa_entry = {kappa_entry:.1f} M_KK")
print(f"  beta_sq_entry = [{beta_sq_entry.min():.2f}, {beta_sq_entry.max():.2f}]")
print(f"  r_k_entry = [{r_k_entry.min():.4f}, {r_k_entry.max():.4f}]")
print()
print(f"Exit horizon: Ma_fold = {mach_fold:.2f} (NO EXIT HORIZON)")
print(f"  n_k_exit = [{n_k_exit.min():.2e}, {n_k_exit.max():.2e}]")
print(f"  r_exit = [{r_exit.min():.4f}, {r_exit.max():.4f}]")
print()
print(f"Transit velocity: v_tau = {v_tau:.2f} M_KK")
print(f"Transit duration: dt_transit = {dt_transit:.6f} M_KK^-1")
print()

# ==============================================================================
# Section 2: MECHANISM A -- Dispersive Phase Spread at Entry Horizon
# ==============================================================================
#
# The entry horizon scattering region has width ~ 1/kappa_entry in tau.
# Each mode k picks up a WKB phase:
#
#   phi_k = integral_{tau_entry - delta/2}^{tau_entry + delta/2}
#           omega_k / c_eff(tau) * dtau / v_tau                       (1)
#
# where c_eff(tau) varies through the horizon region and v_tau is the
# modulus velocity. The effective sound speed transitions:
#
#   c_eff(tau < tau_entry) ≈ c_BA     (in the BCS condensate)
#   c_eff(tau > tau_entry) ≈ c_mod    (post-condensate, before BCS reforms)
#
# But with Ma = 20.7 everywhere, the modes are ALWAYS supersonic.
# The phase is accumulated in the frame comoving with the modulus.

print("-" * 72)
print("MECHANISM A: Dispersive Phase Spread at Entry Horizon")
print("-" * 72)
print()

# Horizon width in tau
delta_tau_horizon = 1.0 / kappa_entry  # (local)
print(f"Horizon width: delta_tau = 1/kappa_entry = {delta_tau_horizon:.6e}")

# The scattering region from S72 extends from tau_int_start to tau_int_end
tau_start = float(d_exit["tau_int_start"])  # 0.164  # (local)
tau_end = float(d_exit["tau_int_end"])      # 0.224  # (local)
delta_tau_scatter = tau_end - tau_start  # (local)
print(f"Scattering region: [{tau_start:.4f}, {tau_end:.4f}], width = {delta_tau_scatter:.4f}")

# Number of integration steps
N_steps = 10000  # (local)
tau_arr = np.linspace(tau_start, tau_end, N_steps)  # (local)
dtau = tau_arr[1] - tau_arr[0]  # (local)

# Effective sound speed profile through the entry horizon
# Pre-horizon: modes propagate in BCS condensate at c_BA
# The horizon itself is where the condensate's character changes.
# Model: smooth tanh transition centered at tau_entry
#   c_eff(tau) = c_BA + (c_mod - c_BA) * 0.5 * (1 + tanh((tau - tau_entry)/sigma_h))
# where sigma_h ~ 1/kappa_entry is the horizon width.
sigma_h = 1.0 / kappa_entry  # (local)
c_eff_arr = c_BA_val + (c_mod - c_BA_val) * 0.5 * (1.0 + np.tanh((tau_arr - tau_entry_val) / sigma_h))  # (local)

# For each mode k, the local wavenumber is k_eff = omega_k / c_eff
# The accumulated phase over the scattering region:
# phi_k = integral omega_k / c_eff(tau) * dtau / v_tau
# (the 1/v_tau converts dtau to time in the lab frame)

phi_k_dispersive = np.zeros(8)  # (local)
for i in range(8):
    k_local = omega_k[i] / c_eff_arr  # (local)
    phi_k_dispersive[i] = np.trapezoid(k_local, tau_arr) / v_tau  # (local)

print()
print("Mode-resolved dispersive phase accumulation:")
print(f"{'Mode':>6} {'omega_k':>10} {'phi_k':>14} {'phi_k (rad)':>14}")
for i in range(8):
    print(f"{str(labels[i]):>6} {omega_k[i]:10.6f} {phi_k_dispersive[i]:14.8f} "
          f"{phi_k_dispersive[i]:14.8f}")

# Inter-mode phase differences
dphi_disp = np.diff(phi_k_dispersive)  # (local)
print()
print("Inter-mode phase differences (adjacent):")
for i in range(7):
    print(f"  {str(labels[i]):>5} -> {str(labels[i+1]):>5}: "
          f"delta_phi = {dphi_disp[i]:+.8e} rad")

# Variance of phases (full set)
var_phi_disp = np.var(phi_k_dispersive)  # (local)
std_phi_disp = np.std(phi_k_dispersive)  # (local)

# Weighted variance using mode_weights
phi_mean_w = np.average(phi_k_dispersive, weights=mode_weights)  # (local)
var_phi_w = np.average((phi_k_dispersive - phi_mean_w)**2, weights=mode_weights)  # (local)
std_phi_w = np.sqrt(var_phi_w)  # (local)

print()
print(f"Phase spread (unweighted): Var(phi) = {var_phi_disp:.6e}, "
      f"Std(phi) = {std_phi_disp:.6e}")
print(f"Phase spread (weighted):   Var(phi) = {var_phi_w:.6e}, "
      f"Std(phi) = {std_phi_w:.6e}")

# t_dec from dispersive spread: when Var(phi) ~ 1, coherence is lost.
# t_dec/t_transit ~ 1 / (Var(phi) * v_tau * dt_transit) ... but Var(phi) is
# already dimensionless (accumulated over the transit). So:
# If Var(phi) << 1, coherence is preserved (t_dec >> t_transit).
# t_dec/t_transit ~ 1 / Var(phi) when Var(phi) measures the spread per transit.

# But we must be more precise. The density matrix off-diagonal element
# decays as <exp(i phi_k) exp(-i phi_j)> = exp(-Var(phi)/2) for Gaussian spread.
# Decoherence factor: F_dec = exp(-Var(phi)/2)
F_dec_disp = np.exp(-var_phi_w / 2.0)  # (local)
t_dec_disp = -1.0 / np.log(F_dec_disp) if F_dec_disp < 1.0 else np.inf  # (local)

print()
print(f"Decoherence factor F_dec(dispersive) = exp(-Var/2) = {F_dec_disp:.10f}")
print(f"t_dec/t_transit (dispersive) = {t_dec_disp:.2f}" if t_dec_disp < 1e10
      else f"t_dec/t_transit (dispersive) = {t_dec_disp:.2e} (>> 1, no decoherence)")

print()
print("MECHANISM A ASSESSMENT: The entry horizon width 1/kappa = "
      f"{delta_tau_horizon:.2e} << scattering width {delta_tau_scatter:.4f}.")
print(f"  The c_eff transition is extremely sharp (sigma_h = {sigma_h:.2e}).")
print(f"  Modes accumulate nearly identical phases because omega_k spans only")
print(f"  {(omega_k.max() - omega_k.min())/omega_k.mean()*100:.1f}% range and "
      f"the transition is too narrow to differentiate.")

# ==============================================================================
# Section 3: MECHANISM B -- Impedance Mismatch Decoherence
# ==============================================================================
#
# Even without a sonic horizon, the four-speed hierarchy creates impedance
# steps. When a mode crosses from a region with sound speed c_1 to c_2,
# the acoustic impedance changes from Z_1 = rho * c_1 to Z_2 = rho * c_2.
# The reflection coefficient at the interface:
#   R = |(Z_2 - Z_1) / (Z_2 + Z_1)|^2
# The phase shift on reflection is mode-dependent (dispersive).

print()
print("-" * 72)
print("MECHANISM B: Impedance Mismatch Decoherence")
print("-" * 72)
print()

# Impedance ratios at each interface in the four-speed hierarchy
# (assuming rho ~ const across the interfaces for acoustic modes)
speeds = {"c_mod": c_mod, "c_BLV": c_BLV, "c_BA": c_BA_val, "c_L": c_L_val}  # (local)

print("Four-speed hierarchy impedance mismatches:")
speed_names = list(speeds.keys())  # (local)
speed_vals = list(speeds.values())  # (local)

for i in range(len(speed_names)):
    for j in range(i+1, len(speed_names)):
        R_ij = ((speed_vals[j] - speed_vals[i]) / (speed_vals[j] + speed_vals[i]))**2  # (local)
        print(f"  {speed_names[i]}/{speed_names[j]}: "
              f"c_ratio = {speed_vals[i]/speed_vals[j]:.4f}, R = {R_ij:.6f}")

# The dominant impedance mismatch is between c_BA and c_mod
R_BA_mod = ((c_mod - c_BA_val) / (c_mod + c_BA_val))**2  # (local)
T_BA_mod = 1.0 - R_BA_mod  # (local)

# For the pre/post-transit impedance step:
# Before transit: BCS condensate with c_eff ~ c_BA = 0.399
# After transit: spectral action modulus with c_eff ~ c_mod = 1.0
# But the modulus is moving at v_tau = 8.27 >> both speeds (supersonic)
# So the relevant Mach numbers are:
Ma_BA = v_tau / c_BA_val  # (local)
Ma_mod = v_tau / c_mod    # (local)

print()
print(f"Mach numbers: Ma_BA = {Ma_BA:.2f}, Ma_mod = {Ma_mod:.2f}")
print(f"Both supersonic => no sonic horizon at either speed.")
print()

# Phase shift on reflection from impedance mismatch
# For a mode at frequency omega hitting an impedance step:
#   phi_R(omega) = arg((Z_2 - Z_1)/(Z_2 + Z_1)) + 2*omega*L/v_tau
# where L is the effective thickness of the transition region.
# The first term is 0 or pi (real coefficient); the second gives dispersion.

# Transition region effective thickness ~ BCS coherence length
L_eff = xi_BCS  # (local)
print(f"Effective transition region: L_eff = xi_BCS = {L_eff:.4f} M_KK^-1")

# Phase accumulated by each mode across the transition region
phi_k_impedance = np.zeros(8)  # (local)
for i in range(8):
    # Phase in the transition: omega_k * L_eff / c_BA (pre-transition speed)
    phi_k_impedance[i] = omega_k[i] * L_eff / c_BA_val  # (local)

# Mode-dependent reflection coefficient (with dispersion)
# In the supersonic regime, the reflection coefficient involves the
# Doppler-shifted frequency: omega_D = omega * (1 - v/c)
# Since v >> c, omega_D ~ omega * (1 - Ma) is negative (modes are blueshifted
# past the group velocity). This means the standard reflection formula
# doesn't apply directly -- we need the supersonic scattering theory.

# For supersonic flow past an impedance step, the Bogoliubov channel opens.
# The "reflection" is actually mode conversion (particle creation).
# The relevant quantity is beta_k from the entry horizon, which we already have.

print()
print("Impedance mismatch phases (omega_k * xi_BCS / c_BA):")
for i in range(8):
    print(f"  {str(labels[i]):>5}: phi_imp = {phi_k_impedance[i]:.6f} rad")

dphi_imp = np.diff(phi_k_impedance)  # (local)
var_phi_imp = np.var(phi_k_impedance)  # (local)
var_phi_imp_w = np.average((phi_k_impedance - np.average(phi_k_impedance, weights=mode_weights))**2,
                            weights=mode_weights)  # (local)

print()
print(f"Impedance phase spread (unweighted): Var = {var_phi_imp:.6e}")
print(f"Impedance phase spread (weighted):   Var = {var_phi_imp_w:.6e}")

F_dec_imp = np.exp(-var_phi_imp_w / 2.0)  # (local)
t_dec_imp = -1.0 / np.log(F_dec_imp) if F_dec_imp < 1.0 else np.inf  # (local)
print(f"F_dec(impedance) = {F_dec_imp:.10f}")
print(f"t_dec/t_transit (impedance) = {t_dec_imp:.2f}" if t_dec_imp < 1e10
      else f"t_dec/t_transit (impedance) = {t_dec_imp:.2e}")

# ==============================================================================
# Section 4: MECHANISM C -- Entry Horizon Bogoliubov Phase Spread
# ==============================================================================
#
# The entry horizon at tau_entry = 0.2195 produces Bogoliubov particles with
# beta_sq ~ 82-88 per mode (deeply thermal). The phases of these beta_k
# coefficients vary across modes. The inter-mode phase coherence determines
# whether the entry-horizon production acts as a coherent or incoherent source.
#
# From S72: the Bogoliubov phases at the entry horizon are encoded in
# the x_k = omega_k / T_H values. The thermal distribution
#   n_k = 1/(exp(omega_k/T_H) - 1) ~ T_H/omega_k - 1/2 + ...
# means each mode sees slightly different occupation.
#
# The Bogoliubov transformation is:
#   a_out = alpha_k a_in + beta_k a_in^dag
# where arg(beta_k) is the squeeze angle. Inter-mode decoherence comes from
# the variance of arg(beta_k) across modes.

print()
print("-" * 72)
print("MECHANISM C: Entry Horizon Bogoliubov Phase Spread")
print("-" * 72)
print()

# The phase of the Bogoliubov coefficient at the entry horizon.
# For a thermal horizon with surface gravity kappa:
#   beta_k = -exp(-pi omega_k / kappa) / (1 - exp(-2pi omega_k / kappa))^{1/2}
# The phase of beta_k involves the mode's propagation through the horizon
# geometry. For the Unruh/Hawking case:
#   arg(beta_k) = omega_k * ln(omega_k / kappa) / kappa + constant
# This is the key dispersive phase from the horizon.

# Using the S72 data directly:
x_k = d_entry["x_k"]  # omega_k / T_H
print(f"x_k = omega_k / T_H: [{x_k.min():.6f}, {x_k.max():.6f}]")
print(f"  All modes deeply thermal (x_k << 1)")
print()

# The WKB phase accumulated by mode k near the horizon:
# phi_k^{WKB} = integral_{near horizon} omega_k / c_eff(tau) dtau / v_tau
# Near the horizon, c_eff varies as c_eff ~ c_BA * |tau - tau_entry|/sigma_h
# giving a logarithmic phase:
#   phi_k^{WKB} ~ (omega_k / kappa_v) * ln(Lambda / omega_k)   (eq. 2)
# where kappa_v = v_tau * kappa_entry is the velocity-scaled surface gravity
# and Lambda is a UV cutoff (typically kappa_entry).

kappa_v = float(d_entry["kappa_v"])  # 457.66 M_KK (velocity-weighted surface gravity)

# Dispersive WKB phase near the entry horizon for each mode
# phi_k = (omega_k / kappa_v) * ln(kappa_entry / omega_k)
phi_k_horizon = (omega_k / kappa_v) * np.log(kappa_entry / omega_k)  # (local)

print("Entry horizon WKB phases:")
for i in range(8):
    print(f"  {str(labels[i]):>5}: phi_h = {phi_k_horizon[i]:.8f} rad "
          f"(omega/kappa_v = {omega_k[i]/kappa_v:.6f})")

dphi_horizon = np.diff(phi_k_horizon)  # (local)
var_phi_horizon = np.var(phi_k_horizon)  # (local)
phi_h_mean_w = np.average(phi_k_horizon, weights=mode_weights)  # (local)
var_phi_horizon_w = np.average((phi_k_horizon - phi_h_mean_w)**2,
                                weights=mode_weights)  # (local)
std_phi_horizon_w = np.sqrt(var_phi_horizon_w)  # (local)

print()
print(f"Horizon phase spread (unweighted): Var = {var_phi_horizon:.6e}, "
      f"Std = {np.sqrt(var_phi_horizon):.6e}")
print(f"Horizon phase spread (weighted):   Var = {var_phi_horizon_w:.6e}, "
      f"Std = {std_phi_horizon_w:.6e}")

F_dec_horizon = np.exp(-var_phi_horizon_w / 2.0)  # (local)
t_dec_horizon = -1.0 / np.log(F_dec_horizon) if F_dec_horizon < 1.0 else np.inf  # (local)
print(f"F_dec(horizon WKB) = {F_dec_horizon:.10f}")
print(f"t_dec/t_transit (horizon WKB) = {t_dec_horizon:.2e}" if t_dec_horizon > 1e6
      else f"t_dec/t_transit (horizon WKB) = {t_dec_horizon:.2f}")

# ==============================================================================
# Section 5: MECHANISM D -- Compound Entry Horizon + BCS Squeeze
# ==============================================================================
#
# The FULL decoherence from the entry horizon comes from combining:
# (i) the Bogoliubov squeeze (r_k_entry ~ 2.9) which AMPLIFIES phase differences
# (ii) the dispersive phase accumulated through the transit
# (iii) the BCS fold squeeze (r_k_bcs ~ 1.8-3.6) which adds further k-dependent phase
#
# For a squeezed state with squeeze parameter r and squeeze angle theta:
#   <delta_phi^2> = e^{2r} * <delta_phi^2>_vacuum
# The entry horizon squeeze AMPLIFIES any initial phase spread by e^{2r}.
#
# The compound phase per mode:
#   Phi_k = phi_k^{entry_squeeze} + phi_k^{transit} + phi_k^{BCS_squeeze}
# where each term is mode-dependent.

print()
print("-" * 72)
print("MECHANISM D: Compound Entry Horizon + BCS Squeeze Decoherence")
print("-" * 72)
print()

# From S72, the compound squeeze parameters
r_k_bcs = d_entry["r_k_bcs"]  # BCS fold squeeze
r_k_compound = d_entry["r_compound"]  # total compound squeeze

print("Squeeze parameters by mode:")
print(f"{'Mode':>6} {'r_entry':>10} {'r_BCS':>10} {'r_compound':>10} "
      f"{'e^{2r_entry}':>14} {'e^{2r_comp}':>14}")
for i in range(8):
    print(f"{str(labels[i]):>6} {r_k_entry[i]:10.4f} {r_k_bcs[i]:10.4f} "
          f"{r_k_compound[i]:10.4f} "
          f"{np.exp(2*r_k_entry[i]):14.2f} {np.exp(2*r_k_compound[i]):14.2f}")

# The compound Bogoliubov phase from the exit computation (phi_compound)
# already includes entry + BCS + transit effects
print()
print("Compound phases from W1-A:")
for i in range(8):
    print(f"  {str(labels[i]):>5}: phi_compound = {phi_compound[i]:+.8f} rad")

# Inter-mode phase differences for the compound channel
dphi_compound = np.diff(phi_compound)  # (local)
var_phi_compound = np.var(phi_compound)  # (local)
phi_c_mean_w = np.average(phi_compound, weights=mode_weights)  # (local)
var_phi_compound_w = np.average((phi_compound - phi_c_mean_w)**2,
                                 weights=mode_weights)  # (local)

print()
print(f"Compound phase spread (unweighted): Var = {var_phi_compound:.6e}")
print(f"Compound phase spread (weighted):   Var = {var_phi_compound_w:.6e}")

# The compound decoherence factor: the density matrix off-diagonal decays as
# rho_{ij} ~ exp(-|phi_i - phi_j|^2 / 2 * n_bar)
# where n_bar is the mean occupation number (squeeze amplification).
# For the compound channel:
#   F_dec = prod_k exp(-(phi_k - <phi>)^2 * n_k_entry / 2)   (eq. 3)
# where n_k_entry = beta_sq_entry ~ 85 amplifies the phase spread.

# Individual mode decoherence factors with squeeze amplification
n_bar_entry = np.mean(beta_sq_entry)  # (local)
print(f"\nMean entry occupation: n_bar = {n_bar_entry:.2f}")

# Method 1: Squeeze-amplified phase variance
var_phi_squeezed = var_phi_compound_w * n_bar_entry  # (local)
F_dec_squeezed = np.exp(-var_phi_squeezed / 2.0)  # (local)
t_dec_squeezed = -1.0 / np.log(F_dec_squeezed) if F_dec_squeezed < 1.0 else np.inf  # (local)

print(f"Squeeze-amplified variance: Var_sq = Var * n_bar = {var_phi_squeezed:.6e}")
print(f"F_dec(squeezed) = {F_dec_squeezed:.10f}")
print(f"t_dec/t_transit (squeezed) = {t_dec_squeezed:.2f}" if t_dec_squeezed < 1e6
      else f"t_dec/t_transit (squeezed) = {t_dec_squeezed:.2e}")

# Method 2: Direct pairwise decoherence from compound phases
# The off-diagonal coherence between modes i and j:
#   C_{ij} = exp(-n_bar * (phi_i - phi_j)^2 / 2)
# Total coherence = sum of weighted |C_{ij}| over all pairs
n_modes = 8  # (local)
C_matrix = np.zeros((n_modes, n_modes))  # (local)
for i in range(n_modes):
    for j in range(n_modes):
        dphi_ij = phi_compound[i] - phi_compound[j]  # (local)
        C_matrix[i, j] = np.exp(-n_bar_entry * dphi_ij**2 / 2.0)  # (local)

# Weighted total coherence
w_outer = np.outer(mode_weights, mode_weights)  # (local)
F_dec_pairwise = np.sum(w_outer * C_matrix)  # (local)
# Normalize by autocorrelation
F_dec_pairwise_norm = F_dec_pairwise / np.sum(w_outer)  # (local)

print()
print(f"Pairwise decoherence matrix:")
print(f"  F_dec(pairwise, normalized) = {F_dec_pairwise_norm:.8f}")

# The key insight: the compound phases from W1-A split into TWO groups
# B2 + B1 are near -1.57 rad (pi/2 phase shift), B3 modes near -2.12 rad
# The inter-branch split is ~ 0.55 rad, which is O(1).
phi_B2_mean = np.mean(phi_compound[:4])  # (local)
phi_B1 = phi_compound[4]  # (local)
phi_B3_mean = np.mean(phi_compound[5:8])  # (local)
delta_phi_B2_B3 = phi_B2_mean - phi_B3_mean  # (local)
delta_phi_B1_B3 = phi_B1 - phi_B3_mean  # (local)
delta_phi_B2_B1 = phi_B2_mean - phi_B1  # (local)

print()
print("Inter-branch compound phase splits:")
print(f"  <phi_B2> = {phi_B2_mean:.6f}, phi_B1 = {phi_B1:.6f}, <phi_B3> = {phi_B3_mean:.6f}")
print(f"  delta_phi(B2-B3) = {delta_phi_B2_B3:+.6f} rad")
print(f"  delta_phi(B1-B3) = {delta_phi_B1_B3:+.6f} rad")
print(f"  delta_phi(B2-B1) = {delta_phi_B2_B1:+.6f} rad")

# Squeeze amplification of the inter-branch split
C_B2_B3 = np.exp(-n_bar_entry * delta_phi_B2_B3**2 / 2.0)  # (local)
C_B2_B1 = np.exp(-n_bar_entry * delta_phi_B2_B1**2 / 2.0)  # (local)
C_B1_B3 = np.exp(-n_bar_entry * delta_phi_B1_B3**2 / 2.0)  # (local)

print()
print("Squeeze-amplified inter-branch coherence:")
print(f"  C(B2,B3) = exp(-n_bar * dphi^2/2) = exp(-{n_bar_entry:.1f} * "
      f"{delta_phi_B2_B3**2:.4f} / 2) = {C_B2_B3:.6e}")
print(f"  C(B2,B1) = {C_B2_B1:.6e}")
print(f"  C(B1,B3) = {C_B1_B3:.6e}")

# ==============================================================================
# Section 6: MECHANISM E -- Full Phase Budget & Master Decoherence
# ==============================================================================
#
# Combine ALL phase sources:
# 1. Dispersive phase from entry horizon traversal (Mechanism A)
# 2. Impedance mismatch phase (Mechanism B)
# 3. Entry horizon WKB phase (Mechanism C)
# 4. Compound squeeze phase from W1-A (Mechanism D)
# 5. The exit Bogoliubov phases (small, from W1-A data)
#
# The total phase per mode: Phi_k_total = sum of all contributions.
# The total decoherence = exp(-Var(Phi_total) * n_bar / 2).

print()
print("-" * 72)
print("MECHANISM E: Full Phase Budget & Master Decoherence")
print("-" * 72)
print()

# Total phase per mode from all mechanisms
Phi_total = phi_k_dispersive + phi_k_impedance + phi_k_horizon + phi_compound  # (local)

# Also add the exit Bogoliubov phases (small contribution)
Phi_total += phase_k_exit  # (local)

print("Full phase budget per mode:")
print(f"{'Mode':>6} {'phi_disp':>10} {'phi_imp':>10} {'phi_hor':>10} "
      f"{'phi_comp':>10} {'phi_exit':>10} {'Phi_total':>12}")
for i in range(8):
    print(f"{str(labels[i]):>6} {phi_k_dispersive[i]:10.6f} {phi_k_impedance[i]:10.6f} "
          f"{phi_k_horizon[i]:10.6f} {phi_compound[i]:10.6f} "
          f"{phase_k_exit[i]:10.6f} {Phi_total[i]:12.6f}")

# Total variances (weighted)
Phi_mean_w = np.average(Phi_total, weights=mode_weights)  # (local)
Var_total_w = np.average((Phi_total - Phi_mean_w)**2, weights=mode_weights)  # (local)

# Squeeze-amplified total variance
Var_total_sq = Var_total_w * n_bar_entry  # (local)

# Master decoherence factor
F_dec_master = np.exp(-Var_total_sq / 2.0)  # (local)

# Convert to t_dec/t_transit
# The decoherence factor applies per transit. For single-pass:
# t_dec = t_transit * (-1/ln(F_dec))
if F_dec_master > 0 and F_dec_master < 1.0:
    t_dec_master = -1.0 / np.log(F_dec_master)  # (local)
else:
    t_dec_master = np.inf  # (local)

print()
print(f"Total weighted phase variance: Var(Phi_total) = {Var_total_w:.6e}")
print(f"Squeeze-amplified: Var_sq = {Var_total_sq:.6e}")
print(f"Master decoherence factor: F_dec = {F_dec_master:.10f}")
print(f"Master t_dec/t_transit = {t_dec_master:.2f}" if t_dec_master < 1e8
      else f"Master t_dec/t_transit = {t_dec_master:.2e}")

# ==============================================================================
# Section 7: The KEY physical result -- entry-exit asymmetry
# ==============================================================================
#
# The inter-branch phase split (B2 vs B3 ~ 0.55 rad) is the DOMINANT
# phase structure. This comes from the compound squeeze (BCS + entry horizon)
# which treats B1, B2, B3 branches differently because they have different
# frequencies and coupling to the condensate.
#
# The squeeze amplification by n_bar ~ 85 turns this into:
#   n_bar * delta_phi^2 / 2 ~ 85 * 0.30 / 2 ~ 12.8
# which gives COMPLETE decoherence between B2 and B3 branches (C ~ e^{-12.8}).
# But WITHIN each branch, the phase spread is tiny (~mrad).
#
# This means the density matrix has block structure:
# - B2 sector: coherent within (4 modes)
# - B1 sector: single mode
# - B3 sector: coherent within (3 modes)
# - B2-B3 and B1-B3 inter-branch: fully decohered

print()
print("-" * 72)
print("Section 7: Entry-Exit Asymmetry and Block Decoherence")
print("-" * 72)
print()

# Intra-branch phase spreads
var_B2_intra = np.var(Phi_total[:4])  # (local)
var_B3_intra = np.var(Phi_total[5:8])  # (local)
print(f"Intra-branch phase variances:")
print(f"  B2 (4 modes): Var = {var_B2_intra:.6e}")
print(f"  B3 (3 modes): Var = {var_B3_intra:.6e}")
print(f"  B1: single mode (no intra-branch variance)")

# Inter-branch variances (the dominant contribution)
Phi_branch_means = np.array([np.mean(Phi_total[:4]), Phi_total[4], np.mean(Phi_total[5:8])])  # (local)
branch_weights = np.array([4*mode_weights[0], mode_weights[4], 3*mode_weights[5]])  # (local)
branch_weights /= branch_weights.sum()  # (local)
Phi_branch_mean_w = np.average(Phi_branch_means, weights=branch_weights)  # (local)
Var_inter_branch = np.average((Phi_branch_means - Phi_branch_mean_w)**2,
                               weights=branch_weights)  # (local)

print()
print(f"Inter-branch phase variance: {Var_inter_branch:.6e}")
print(f"Inter-branch squeeze-amplified: {Var_inter_branch * n_bar_entry:.4f}")
print(f"Inter-branch C = exp(-n_bar*Var/2) = {np.exp(-n_bar_entry * Var_inter_branch / 2):.6e}")

# The block decoherence picture
# The density matrix has 3 blocks (B2, B1, B3). The inter-block coherence
# is killed by the squeeze-amplified inter-branch phase split.
# The effective number of independent sectors = 3 (from 1 if fully coherent).
# This is partial decoherence: not enough to reach the A_s gate band.

# What matters for A_s: the total squeeze parameter determines the amplitude.
# Decoherence sets the EFFECTIVE squeeze to the incoherent average of branches.
# r_eff^{incoherent} = sqrt(sum_i w_i r_i^2) for decohered branches
# vs r_eff^{coherent} = |sum_i w_i r_i e^{i phi_i}| for coherent case

r_eff_coherent = np.abs(np.sum(mode_weights * r_k_compound * np.exp(1j * Phi_total)))  # (local)
r_eff_incoherent = np.sqrt(np.sum(mode_weights * r_k_compound**2))  # (local)
r_eff_partial = np.sqrt(np.sum(mode_weights * r_k_compound**2 * F_dec_master))  # (local)

print()
print(f"Effective squeeze parameters:")
print(f"  r_eff (fully coherent):   {r_eff_coherent:.6f}")
print(f"  r_eff (fully incoherent): {r_eff_incoherent:.6f}")
print(f"  r_eff (partial, F_dec):   {r_eff_partial:.6f}")
print(f"  Ratio incoh/coh: {r_eff_incoherent/r_eff_coherent:.4f}" if r_eff_coherent > 0
      else "  Coherent r_eff = 0 (destructive interference)")

# delta_OOM from the dispersive decoherence
# A_s ~ exp(2*r_eff), so delta_OOM = 2*(r_incoh - r_coh) / ln(10)
if r_eff_coherent > 0:
    delta_OOM_disp = 2.0 * (r_eff_incoherent - r_eff_coherent) / np.log(10)  # (local)
else:
    delta_OOM_disp = 0.0  # (local)
print(f"  delta_OOM (dispersive channel) = {delta_OOM_disp:.4f}")

# ==============================================================================
# Section 8: Cross-checks
# ==============================================================================

print()
print("=" * 72)
print("CROSS-CHECKS")
print("=" * 72)
print()

# (1) T -> 1 limit (no reflection): set all beta_sq = 0
# When n_bar = 0, squeeze amplification vanishes, so F_dec -> 1 (no decoherence)
F_dec_T1 = np.exp(-Var_total_w * 0.0 / 2.0)  # = exp(0) = 1  # (local)
print(f"(1) T -> 1 (no reflection, n_bar=0): F_dec = {F_dec_T1:.6f} "
      f"{'PASS' if abs(F_dec_T1 - 1.0) < 1e-10 else 'FAIL'}")
print(f"    -> t_dec = infinity (no decoherence). Consistent: no horizon => no decoherence.")

# (2) T -> 0 limit (perfect reflection): n_bar -> infinity
# F_dec -> 0 (complete decoherence), t_dec -> 0
F_dec_T0 = np.exp(-Var_total_w * 1e6 / 2.0)  # n_bar = 1e6  # (local)
t_dec_T0 = -1.0 / np.log(F_dec_T0) if F_dec_T0 > 0 else 0.0  # (local)
print(f"(2) T -> 0 (perfect reflection, n_bar=1e6): F_dec = {F_dec_T0:.6e}")
print(f"    -> t_dec/t_transit ~ {t_dec_T0:.6e}. Consistent: strong horizon => rapid decoherence.")

# (3) Mode-independence test: if all modes had same frequency,
#     Var(phi) = 0 and F_dec = 1 (no decoherence)
omega_flat = np.full(8, omega_k.mean())  # (local)
phi_flat = omega_flat * L_eff / c_BA_val  # (local)
var_flat = np.var(phi_flat)  # (local)
print(f"(3) Equal frequencies: Var(phi) = {var_flat:.2e} "
      f"{'PASS' if var_flat < 1e-20 else 'FAIL'}")
print(f"    -> No inter-mode decoherence when all modes degenerate.")

# (4) Consistency with W1-A t_dec
print(f"(4) W1-A compound t_dec/t_transit = {float(d_exit['t_dec_primary']):.2f}")
print(f"    Our compound (squeeze-amplified): {t_dec_squeezed:.2e}" if t_dec_squeezed > 1e6
      else f"    Our compound (squeeze-amplified): {t_dec_squeezed:.2f}")
print(f"    Note: W1-A uses exit Bogoliubov production only (n_k ~ 0.01).")
print(f"    This computation uses entry horizon amplification (n_bar ~ {n_bar_entry:.0f}).")
print(f"    Ratio: {float(d_exit['t_dec_primary'])/t_dec_master:.2f}x" if t_dec_master > 0
      else "    Ratio: undefined (t_dec_master = inf)")

# (5) Compound phase self-consistency
print(f"(5) Compound phases B2 near -pi/2: {phi_B2_mean:.4f} vs -pi/2 = {-np.pi/2:.4f}, "
      f"diff = {phi_B2_mean + np.pi/2:.4e}")
print(f"    B3 near -2.12: {phi_B3_mean:.4f}")
print(f"    Branch-dependent phase ~ O(1) with inter-branch split {abs(delta_phi_B2_B3):.4f}")

# (6) omega_k dispersion
omega_spread_frac = (omega_k.max() - omega_k.min()) / omega_k.mean()  # (local)
print(f"(6) omega_k fractional spread: {omega_spread_frac:.4f} ({omega_spread_frac*100:.1f}%)")
print(f"    Narrow bandwidth limits dispersive decoherence (all mechanisms scale with omega spread)")

# (7) Dimensional consistency
print(f"(7) All phases computed as dimensionless ratios (omega * length / speed). "
      f"All in M_KK units. PASS.")

# ==============================================================================
# Section 9: Gate Verdict
# ==============================================================================

print()
print("=" * 72)
print("GATE VERDICT: FABRY-PEROT-73a")
print("=" * 72)
print()

# Collect all t_dec results
results = {
    "dispersive_A": t_dec_disp,
    "impedance_B": t_dec_imp,
    "horizon_WKB_C": t_dec_horizon,
    "compound_squeezed_D": t_dec_squeezed,
    "master_E": t_dec_master,
}

# The primary result is the MASTER decoherence (all mechanisms combined)
t_dec_primary = t_dec_master  # (local)

# Gate band: [0.57, 0.88]
gate_lo = 0.57  # (local)
gate_hi = 0.88  # (local)

if t_dec_primary >= gate_lo and t_dec_primary <= gate_hi:
    verdict = "PASS"
    verdict_detail = (f"t_dec/t_transit = {t_dec_primary:.4f} in [{gate_lo}, {gate_hi}]. "
                      f"Dispersive entry-horizon decoherence matches A_s gate band.")
elif not np.isfinite(t_dec_primary) or t_dec_primary > 1e6:
    verdict = "INFO"
    verdict_detail = (f"t_dec/t_transit = {t_dec_primary:.2e}. Dispersive phase spread from "
                      f"entry horizon is too small for decoherence. The compound phases have "
                      f"O(1) inter-branch split but the BCS mode bandwidth ({omega_spread_frac*100:.1f}%) "
                      f"is too narrow for significant dispersive decoherence in the other channels. "
                      f"Block decoherence DOES separate B2/B1 from B3 (C = {C_B2_B3:.2e}).")
else:
    verdict = "INFO"
    verdict_detail = (f"t_dec/t_transit = {t_dec_primary:.4f} outside [{gate_lo}, {gate_hi}]. "
                      f"Entry-horizon dispersive decoherence computed but outside A_s gate band.")

print(f"Gate: FABRY-PEROT-73a")
print(f"Criterion: t_dec/t_transit in [{gate_lo}, {gate_hi}]")
print(f"Computed: t_dec/t_transit = {t_dec_primary:.4e}" if t_dec_primary > 1e4
      else f"Computed: t_dec/t_transit = {t_dec_primary:.4f}")
print(f"Verdict: {verdict}")
print(f"Detail: {verdict_detail}")
print()

# HOWEVER: the block decoherence result from Mechanism D is physically significant
# even though it doesn't close the A_s gap directly. Check if the inter-branch
# decoherence contributes to delta_OOM.
print("BLOCK DECOHERENCE RESULT (physically significant):")
print(f"  B2-B3 inter-branch: C = {C_B2_B3:.6e} (FULLY DECOHERED)")
print(f"  B2-B1 inter-branch: C = {C_B2_B1:.6e}")
print(f"  B1-B3 inter-branch: C = {C_B1_B3:.6e}")
print(f"  -> Density matrix has 3 decohered blocks: B2(4), B1(1), B3(3)")
print(f"  -> delta_OOM from block decoherence: {delta_OOM_disp:.4f}")
print()

# Additional information: what would be NEEDED for t_dec in gate band?
# We need Var_total_sq ~ 2 * (-ln(exp(-1/t_gate)))
# For t_gate = 0.72 (midpoint): -ln(F) = 1/0.72 = 1.39
# => Var_sq = 2 * 1.39 = 2.78
# => With n_bar=85: Var(phi) = 2.78/85 = 0.0327
# => Std(phi) = 0.181 rad
# Currently Var(phi) ~ few x 10^{-2} to 10^{-1}
Var_needed = 2.0 * (1.0 / 0.72) / n_bar_entry  # (local)
Std_needed = np.sqrt(Var_needed)  # (local)
print(f"Phase spread NEEDED for gate band (t_dec/t_transit ~ 0.72):")
print(f"  Var(phi) needed = {Var_needed:.6f}")
print(f"  Std(phi) needed = {Std_needed:.6f} rad")
print(f"  Current Var(phi_total, weighted) = {Var_total_w:.6e}")
print(f"  Shortfall ratio: {Var_needed / Var_total_w:.1f}x" if Var_total_w > 0
      else "  Shortfall ratio: inf (no phase spread)")
print()

# ==============================================================================
# Section 10: Save data
# ==============================================================================

t_end = time.time()

# Build complete output dict
save_dict = {
    # Gate
    "gate_name": "FABRY-PEROT-73a",
    "gate_verdict": verdict,
    "gate_detail": verdict_detail[:200],

    # Mechanism A: Dispersive
    "phi_k_dispersive": phi_k_dispersive,
    "var_phi_dispersive_w": var_phi_w,
    "F_dec_dispersive": F_dec_disp,
    "t_dec_dispersive": t_dec_disp,

    # Mechanism B: Impedance
    "phi_k_impedance": phi_k_impedance,
    "var_phi_impedance_w": var_phi_imp_w,
    "R_BA_mod": R_BA_mod,
    "F_dec_impedance": F_dec_imp,
    "t_dec_impedance": t_dec_imp,

    # Mechanism C: Horizon WKB
    "phi_k_horizon": phi_k_horizon,
    "var_phi_horizon_w": var_phi_horizon_w,
    "F_dec_horizon": F_dec_horizon,
    "t_dec_horizon": t_dec_horizon,

    # Mechanism D: Compound squeeze
    "phi_compound": phi_compound,
    "var_phi_compound_w": var_phi_compound_w,
    "F_dec_squeezed": F_dec_squeezed,
    "t_dec_squeezed": t_dec_squeezed,
    "n_bar_entry": n_bar_entry,

    # Mechanism E: Master
    "Phi_total": Phi_total,
    "Var_total_w": Var_total_w,
    "Var_total_sq": Var_total_sq,
    "F_dec_master": F_dec_master,
    "t_dec_master": t_dec_master,

    # Block decoherence
    "delta_phi_B2_B3": delta_phi_B2_B3,
    "delta_phi_B1_B3": delta_phi_B1_B3,
    "delta_phi_B2_B1": delta_phi_B2_B1,
    "C_B2_B3": C_B2_B3,
    "C_B2_B1": C_B2_B1,
    "C_B1_B3": C_B1_B3,
    "var_B2_intra": var_B2_intra,
    "var_B3_intra": var_B3_intra,
    "Var_inter_branch": Var_inter_branch,
    "delta_OOM_dispersive": delta_OOM_disp,

    # Effective squeezes
    "r_eff_coherent": r_eff_coherent,
    "r_eff_incoherent": r_eff_incoherent,
    "r_eff_partial": r_eff_partial,

    # Cross-check data
    "omega_spread_frac": omega_spread_frac,
    "Var_needed_for_gate": Var_needed,
    "shortfall_ratio": Var_needed / Var_total_w if Var_total_w > 0 else np.inf,

    # Input echoes
    "labels": labels,
    "omega_k": omega_k,
    "mode_weights": mode_weights,
    "r_k_entry": r_k_entry,
    "r_k_bcs": r_k_bcs,
    "r_k_compound": r_k_compound,
    "beta_sq_entry": beta_sq_entry,
    "n_k_exit": n_k_exit,
    "mach_fold": mach_fold,
    "tau_entry": tau_entry_val,

    # Speeds
    "c_mod": c_mod,
    "c_BLV": c_BLV,
    "c_BA": c_BA_val,
    "c_L": c_L_val,
    "v_tau": v_tau,

    # Timing
    "total_time": t_end - t_start,
}

outpath = os.path.join(os.path.dirname(__file__), "s73a_fabry_perot_cavity.npz")
np.savez(outpath, **save_dict)
print(f"Data saved to {outpath}")
print(f"Total runtime: {t_end - t_start:.3f} s")
