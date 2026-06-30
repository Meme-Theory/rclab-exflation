"""
S74 W4-E: N15-MODULUS-DECAY-74 — Modulus Decay Rate into Radiation.

Substrate framing:
After the fold, the Jensen deformation parameter tau relaxes by reorganizing
the D_K eigenvalue spectrum, which releases spectral-weight energy into gauge
field excitations on the fiber. The vertex comes from the tau-derivative of
the instanton action S_inst(tau), loaded from s73a_instanton_landscape.npz.

The canonical modulus field is phi_mod = M_KK * tau (dimension: mass).
The instanton-mediated vertex is L_int ~ (1/f_mod) * phi_mod * Tr(F F),
with decay constant f_mod = M_KK / |dS_inst/dtau|.

Decay rate (standard modulus-to-gauge-boson formula, one loop instanton-weighted):
    Gamma_mod = N_G * (alpha_gauge / (8 pi)) * (|dS/dtau|^2 / M_KK^2)
                * exp(-2 S_inst) * m_mod^3 / (8 pi)

For the substrate, we use Fermi's golden rule with the vertex-squared from
the instanton-weighted coupling:
    Gamma_mod = (g_mod^2 / (M_KK^2)) * rho_gauge(m_mod) / (2 m_mod)
with rho_gauge(E) = E^2 * N_gauge / (2 pi^2)  (massless gauge boson density of states).

Modulus mass from instanton-generated potential curvature:
    V_eff(tau) = M_KK^4 * exp(-S_inst(tau))
    d^2 V/d phi_mod^2 = (1/M_KK^2) * d^2 V/d tau^2
    m_mod^2 = M_KK^2 * [(dS/dtau)^2 - d2S/dtau^2] * exp(-S_inst)

Reheating temperature from Fermi's golden rule result:
    T_rh = (90 / (pi^2 g_*))^{1/4} * sqrt(Gamma_mod * M_Pl_reduced)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from canonical_constants import (
    M_KK,
    tau_fold,
    M_Pl_reduced,
    g_star_SM,
)

# ---------- Load instanton landscape ----------
landscape_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                              's73a_instanton_landscape.npz')
d = np.load(landscape_path, allow_pickle=True)

tau_scan = d['tau_scan']                 # (local)
S_inst_A = d['S_inst_A']                 # (local)
n_inst_unnorm = d['n_inst_unnorm']       # (local)

# ---------- Post-fold index ----------
# tau_fold = 0.19 — the first grid point >= tau_fold is the post-fold reference.
# Use tau = 0.20 (idx=4), the first grid point strictly after the fold.
idx_post = int(np.searchsorted(tau_scan, tau_fold, side='right'))  # (local)
tau_post = float(tau_scan[idx_post])                               # (local)

# ---------- Spectral derivatives ----------
dS_dtau_array = np.gradient(S_inst_A, tau_scan)         # (local)
d2S_dtau2_array = np.gradient(dS_dtau_array, tau_scan)  # (local)

dS_dtau_post = float(dS_dtau_array[idx_post])           # (local)
d2S_dtau2_post = float(d2S_dtau2_array[idx_post])       # (local)
S_inst_post = float(S_inst_A[idx_post])                 # (local)

# ---------- Modulus-to-gauge-field coupling ----------
# g_mod is the dimensionless substrate vertex |dS_inst/dtau|.
# In physical units, the canonical modulus phi_mod = M_KK * tau has coupling
# strength g_mod / M_KK (since d phi = M_KK d tau).
g_mod_dimless = abs(dS_dtau_post)                        # (local)
g_mod_physical = g_mod_dimless / M_KK                    # (local) [GeV^{-1}]

# ---------- Modulus mass from instanton potential curvature ----------
# V_eff(tau) = M_KK^4 * exp(-S_inst(tau))  (one-instanton contribution)
# dV/d tau = -M_KK^4 * (dS/dtau) * exp(-S_inst)
# d^2V/d tau^2 = M_KK^4 * [(dS/dtau)^2 - (d2S/dtau2)] * exp(-S_inst)
# m_mod^2 = d^2V / d phi_mod^2 = (1/M_KK^2) * d^2V/d tau^2
curvature_factor = (dS_dtau_post**2 - d2S_dtau2_post) * np.exp(-S_inst_post)  # (local)
m_mod_sq = M_KK**2 * curvature_factor                    # (local) [GeV^2]

if m_mod_sq <= 0:
    raise RuntimeError(f"Modulus mass squared non-positive: {m_mod_sq}. "
                       "Instanton potential not convex at tau_post.")

m_mod = float(np.sqrt(m_mod_sq))                         # (local) [GeV]

# ---------- Decay rate via Fermi's golden rule ----------
# Gamma_mod = (vertex^2) * rho_final(m_mod) / (2 m_mod)
# Vertex: L_int = (g_mod/M_KK) * phi_mod * (F mu nu F^mu nu) / (4 * M_KK)
# After integrating out instanton background, the squared matrix element
# for phi_mod -> 2 gauge bosons is |M|^2 = (g_mod^2 / M_KK^2) * m_mod^4 / 4
# The 2-body phase space gives a factor 1/(8 pi) (massless final state).
# Gauge bosons have N_gauge = 12 (SU(3) has 8, SU(2) has 3, U(1) has 1 — pre-fold SM).
# For substrate, we use N_G = 8 (SU(3) gluon octet of the fiber).
N_gauge = 8                                              # (local) SU(3) fiber
# Instanton weight: decay is suppressed by exp(-S_inst) at the amplitude level,
# i.e. exp(-2 S_inst) at the rate level.
instanton_weight = np.exp(-2.0 * S_inst_post)            # (local)

# Standard modulus decay width:
# Gamma(phi -> g g) = N_G * (m_mod^3) / (64 pi * f_mod^2)
# with f_mod = M_KK / g_mod_dimless (decay constant).
f_mod = M_KK / g_mod_dimless                             # (local) [GeV]
Gamma_mod_bare = N_gauge * (m_mod**3) / (64.0 * np.pi * f_mod**2)  # (local) [GeV]

# Instanton-mediated processes are suppressed by the instanton action at the rate.
# The decay phi -> 2 gauge quanta through an instanton background picks up
# exp(-2 S_inst) from the tunneling amplitude squared.
Gamma_mod = Gamma_mod_bare * instanton_weight            # (local) [GeV]

# ---------- Reheating temperature ----------
# T_rh = (90 / (pi^2 g_*))^{1/4} * sqrt(Gamma_mod * M_Pl_reduced)
T_rh = ((90.0 / (np.pi**2 * g_star_SM))**0.25) \
       * np.sqrt(Gamma_mod * M_Pl_reduced)               # (local) [GeV]
T_rh_MeV = T_rh * 1e3                                    # (local) [MeV]
T_rh_GeV = T_rh                                          # (local) [GeV]

# ---------- Cross-checks ----------
# Check 1: dimensional analysis
# [Gamma_mod] = [m_mod^3 / f_mod^2] = GeV^3 / GeV^2 = GeV  OK
# [T_rh] = [(Gamma_mod * M_Pl)^{1/2}] = GeV  OK

# Check 2: f_mod should satisfy f_mod < M_Pl (super-Planckian decay constants forbidden)
f_mod_sub_planckian = f_mod < M_Pl_reduced               # (local)

# Check 3: m_mod should be less than M_KK (since it's instanton-suppressed curvature)
m_mod_sub_MKK = m_mod < M_KK                             # (local)

# Check 4: kinematic threshold — decay only open if m_mod > 0 (massless gauge bosons)
kinematic_ok = m_mod > 0                                 # (local)

# Check 5: Bare width sanity — if exp(-S_inst) were 1, what would T_rh be?
Gamma_bare_only = Gamma_mod_bare                                                   # (local)
T_rh_bare = ((90.0 / (np.pi**2 * g_star_SM))**0.25) * np.sqrt(Gamma_bare_only * M_Pl_reduced)  # (local)

# ---------- Gate verdict ----------
# N15-MODULUS-DECAY-74: PASS if T_rh > 1 MeV, INFO if [10 keV, 1 MeV], FAIL if < 10 keV
T_rh_1MeV_threshold_GeV = 1e-3                           # (local)
T_rh_10keV_threshold_GeV = 1e-5                          # (local)

if T_rh > T_rh_1MeV_threshold_GeV:
    verdict = "PASS"
    verdict_detail = f"T_rh = {T_rh_MeV:.3e} MeV > 1 MeV (BBN-compatible)"
elif T_rh > T_rh_10keV_threshold_GeV:
    verdict = "INFO"
    verdict_detail = f"T_rh = {T_rh_MeV:.3e} MeV in [10 keV, 1 MeV] (BBN-borderline)"
else:
    verdict = "FAIL"
    verdict_detail = f"T_rh = {T_rh_MeV:.3e} MeV < 10 keV (too cold for BBN)"

# ---------- Print results ----------
print("=" * 72)
print("S74 W4-E: N15-MODULUS-DECAY-74 — Modulus Decay Rate into Radiation")
print("=" * 72)
print(f"tau_fold (canonical)       = {tau_fold}")
print(f"tau_post (grid)            = {tau_post}")
print(f"idx_post                   = {idx_post}")
print()
print(f"S_inst(tau_post)           = {S_inst_post:.6f}")
print(f"dS_inst/dtau(tau_post)     = {dS_dtau_post:+.6f}")
print(f"d2S_inst/dtau2(tau_post)   = {d2S_dtau2_post:+.6f}")
print()
print(f"g_mod (dimensionless)      = {g_mod_dimless:.6f}")
print(f"f_mod = M_KK / g_mod       = {f_mod:.6e} GeV")
print(f"f_mod / M_Pl_reduced       = {f_mod / M_Pl_reduced:.6e}  (sub-Planckian: {f_mod_sub_planckian})")
print()
print(f"curvature factor           = {curvature_factor:.6e}")
print(f"m_mod                      = {m_mod:.6e} GeV = {m_mod/1e16:.4f} * 10^16 GeV")
print(f"m_mod / M_KK               = {m_mod / M_KK:.6e}  (sub-M_KK: {m_mod_sub_MKK})")
print()
print(f"exp(-2 S_inst) suppression = {instanton_weight:.6e}")
print(f"Gamma_bare (no inst supp)  = {Gamma_mod_bare:.6e} GeV")
print(f"Gamma_mod (full)           = {Gamma_mod:.6e} GeV")
print()
print(f"g_*                        = {g_star_SM}")
print(f"M_Pl_reduced               = {M_Pl_reduced:.6e} GeV")
print(f"T_rh (bare, diagnostic)    = {T_rh_bare:.6e} GeV")
print(f"T_rh (full)                = {T_rh:.6e} GeV = {T_rh_MeV:.6e} MeV")
print()
print(f"Kinematic open              : {kinematic_ok}")
print(f"Sub-Planckian f_mod         : {f_mod_sub_planckian}")
print(f"Sub-M_KK m_mod              : {m_mod_sub_MKK}")
print()
print("Gate verdict: N15-MODULUS-DECAY-74 =", verdict)
print(f"  {verdict_detail}")

# ---------- Save data ----------
out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        's74_modulus_decay.npz')
np.savez(
    out_path,
    # Inputs
    tau_scan=tau_scan,
    S_inst_A=S_inst_A,
    tau_fold=float(tau_fold),
    tau_post=tau_post,
    idx_post=idx_post,
    M_KK=float(M_KK),
    M_Pl_reduced=float(M_Pl_reduced),
    g_star_SM=float(g_star_SM),
    N_gauge=N_gauge,
    # Intermediate
    dS_dtau_array=dS_dtau_array,
    d2S_dtau2_array=d2S_dtau2_array,
    dS_dtau_post=dS_dtau_post,
    d2S_dtau2_post=d2S_dtau2_post,
    S_inst_post=S_inst_post,
    curvature_factor=curvature_factor,
    instanton_weight=instanton_weight,
    Gamma_mod_bare=Gamma_mod_bare,
    f_mod=f_mod,
    # Outputs (the three required quantities)
    g_mod=g_mod_dimless,
    g_mod_physical=g_mod_physical,
    m_mod=m_mod,
    Gamma_mod=Gamma_mod,
    T_rh=T_rh,
    T_rh_MeV=T_rh_MeV,
    # Gate
    gate_name="N15-MODULUS-DECAY-74",
    gate_verdict=verdict,
    gate_detail=verdict_detail,
)
print(f"\nSaved data to: {out_path}")
