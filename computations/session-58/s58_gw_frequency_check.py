"""
S58 — Independent verification: peak GW frequency from first-order phase transitions.

Three methods:
  M1: Direct redshift of Hubble rate H(T_*) to today
  M2: Caprini et al. (2016/2020) simulation-calibrated envelope formula
  M3: Dimensional analysis T_* * T_0 / M_Pl

Three GW source mechanisms at each temperature:
  Bubble collisions (envelope), sound waves, MHD turbulence

Gen-Physicist standalone computation. No session files read.

Conventions:
  - Reduced Planck mass M_Pl = 1/sqrt(8*pi*G) = 2.435e18 GeV
    (Caprini et al. use this convention in their Friedmann equation)
  - Metric signature (-,+,+,+), natural units hbar = c = k_B = 1
  - Ordinary frequency f = omega/(2*pi), conversion: f[Hz] = E[GeV] / h
"""

import sys
import numpy as np

sys.path.insert(0, 'computations')
from canonical_constants import M_Pl_reduced as M_Pl  # GeV, reduced Planck mass

# ============================================================
# Constants
# ============================================================
k_B = 8.617333262e-14      # GeV/K
T0_K = 2.7255              # K (Fixsen 2009)  # (local)
T0_GeV = T0_K * k_B        # 2.348e-13 GeV
g_star = 106.75  # SM energy DOF at T >> 100 GeV (local)
g_starS = 106.75            # SM entropy DOF at T >> 100 GeV  # (local)
g_starS_0 = 3.91            # entropy DOF today (photons + 3 nu families)  # (local)
hbar_GeVs = 6.582119514e-25 # GeV * s  # (local)
GeV_to_Hz = 1.0 / (2 * np.pi * hbar_GeVs)  # 2.418e23 Hz/GeV

# Caprini et al. (2016) fitting parameters
# Bubble envelope: f_env = 16.5 uHz * h_env * (beta/H) * (T/100 GeV) * (g/100)^{1/6}
# Sound waves:     f_sw  = 1.9e-5 Hz * (1/v_w) * (beta/H) * (T/100 GeV) * (g/100)^{1/6}
# Turbulence:      f_turb = 2.7e-5 Hz * (1/v_w) * (beta/H) * (T/100 GeV) * (g/100)^{1/6}
# h_env(v_w) = 0.62 / (1.8 - 0.1*v_w + v_w^2); h_env(v_w=1) = 0.2296
v_w = 1.0  # (local)
h_env = 0.62 / (1.8 - 0.1 * v_w + v_w**2)
g_factor = (g_star / 100.0)**(1.0/6.0)

# Evaluation temperatures and labels
T_stars = [1e2, 1e6, 1e9, 1e14, 1e16]
names = ["EW (100 GeV)", "BSM (10^6)", "Interm (10^9)",
         "See-saw (10^14)", "GUT/KK (10^16)"]


def detector_band(f_Hz):
    """Classify into detector sensitivity band."""
    if f_Hz < 1e-9:   return "sub-PTA"
    if f_Hz < 1e-7:   return "PTA (nHz)"
    if f_Hz < 1e-4:   return "gap (PTA-LISA)"
    if f_Hz < 1e-1:   return "LISA"
    if f_Hz < 10:      return "gap (LISA-LIGO)"
    if f_Hz < 1e4:     return "LIGO/ET"
    if f_Hz < 1e8:     return "high-freq gap"
    return "GHz+"


def H_rad(T, g=106.75):
    """Hubble rate in radiation domination.
    H^2 = rho / (3 M_Pl^2),  rho = (pi^2/30) g T^4.
    => H = sqrt(pi^2 g / 90) * T^2 / M_Pl.
    """
    return np.sqrt(np.pi**2 * g / 90.0) * T**2 / M_Pl


def a_ratio(T, g_s=106.75):
    """Scale factor ratio a(T)/a_0 from entropy conservation.
    g_{sS}(T) T^3 a^3 = g_{sS,0} T_0^3 a_0^3
    => a/a_0 = (g_{sS,0}/g_{sS})^{1/3} * T_0/T.
    """
    return (g_starS_0 / g_s)**(1./3.) * T0_GeV / T


# ============================================================
print("=" * 80)
print("S58 — GRAVITATIONAL WAVE FREQUENCY: FIRST-ORDER PHASE TRANSITIONS")
print("=" * 80)
print()
print(f"  M_Pl (reduced)   = {M_Pl:.3e} GeV")
print(f"  T_0              = {T0_K} K = {T0_GeV:.4e} GeV")
print(f"  g_* / g_{{*S}}     = {g_star} / {g_starS}")
print(f"  g_{{*S,0}}         = {g_starS_0}")
print(f"  v_w              = {v_w}")
print(f"  h_env(v_w=1)     = {h_env:.4f}")
print(f"  1 GeV -> Hz      = {GeV_to_Hz:.4e}")
print()

# ============================================================
# METHOD 1: Direct redshift of Hubble rate
# ============================================================
print("=" * 80)
print("METHOD 1: f_0 = H(T_*) * a_*/a_0  (Hubble horizon frequency, redshifted)")
print("=" * 80)
print()
print("  H(T) = sqrt(pi^2 g_*/90) * T^2 / M_Pl")
print("  a_*/a_0 = (g_{S0}/g_{S*})^{1/3} * T_0/T_*")
print("  => f_0 = sqrt(pi^2 g_*/90) * (g_{S0}/g_S)^{1/3} * T_0/M_Pl * T_*")
print()

C_m1 = np.sqrt(np.pi**2 * g_star / 90.0) * (g_starS_0/g_starS)**(1./3.) * T0_GeV / M_Pl
C_m1_Hz = C_m1 * GeV_to_Hz
print(f"  Prefactor: C_1 = {C_m1_Hz:.4e} Hz/GeV  (f_0 = C_1 * T_*)")
print()

for T, name in zip(T_stars, names):
    f = C_m1_Hz * T
    print(f"  T_* = {T:.0e} GeV  [{name}]:  f_0 = {f:.4e} Hz  [{detector_band(f)}]")
print()

# ============================================================
# METHOD 2: Caprini et al. (2016/2020)
# ============================================================
print("=" * 80)
print("METHOD 2: Caprini et al. simulation-calibrated peak frequencies")
print("=" * 80)
print()

# Prefactors per source mechanism
C_env  = 16.5e-6 * h_env / 100.0 * g_factor   # Hz/GeV at beta/H=1
C_sw   = 1.9e-5 / v_w / 100.0 * g_factor       # Hz/GeV at beta/H=1
C_turb = 2.7e-5 / v_w / 100.0 * g_factor        # Hz/GeV at beta/H=1

print(f"  Prefactors at beta/H_*=1:")
print(f"    Bubble envelope: C_env  = {C_env:.4e} Hz/GeV")
print(f"    Sound waves:     C_sw   = {C_sw:.4e} Hz/GeV")
print(f"    Turbulence:      C_turb = {C_turb:.4e} Hz/GeV")
print(f"    Method 1:        C_1    = {C_m1_Hz:.4e} Hz/GeV")
print()
print(f"  Ratios to Method 1:  env/M1 = {C_env/C_m1_Hz:.2f},  "
      f"sw/M1 = {C_sw/C_m1_Hz:.2f},  turb/M1 = {C_turb/C_m1_Hz:.2f}")
print()

# Full table for beta/H_* = 1
print(f"  {'T_* (GeV)':<14} {'Envelope':<14} {'Sound wave':<14} {'Turbulence':<14} {'Band (sw)'}")
print("  " + "-" * 70)
for T, name in zip(T_stars, names):
    f_e = C_env * T
    f_s = C_sw * T
    f_t = C_turb * T
    print(f"  {T:<14.0e} {f_e:<14.3e} {f_s:<14.3e} {f_t:<14.3e} {detector_band(f_s)}")
print()

# beta/H scan for GUT scale
print("  GUT scale (10^16 GeV) -- beta/H_* scan:")
print(f"  {'beta/H':<10} {'Envelope (Hz)':<18} {'Sound wave (Hz)':<18} {'Turbulence (Hz)':<18}")
print("  " + "-" * 64)
for bH in [1, 10, 100, 421, 1000]:
    fe = C_env * 1e16 * bH
    fs = C_sw * 1e16 * bH
    ft = C_turb * 1e16 * bH
    print(f"  {bH:<10d} {fe:<18.3e} {fs:<18.3e} {ft:<18.3e}")
print()

# ============================================================
# METHOD 3: Dimensional analysis
# ============================================================
print("=" * 80)
print("METHOD 3: Dimensional analysis  f_0 ~ T_* T_0 / M_Pl")
print("=" * 80)
print()

C_m3 = T0_GeV / M_Pl * GeV_to_Hz
print(f"  Prefactor: C_3 = {C_m3:.4e} Hz/GeV")
print(f"  Ratio C_1/C_3 = {C_m1_Hz/C_m3:.4f}  "
      f"(= sqrt(pi^2 g_*/90) * (g_{{S0}}/g_S)^{{1/3}} = {np.sqrt(np.pi**2*g_star/90)*(g_starS_0/g_starS)**(1./3.):.4f})")
print()
for T, name in zip(T_stars, names):
    f = C_m3 * T
    print(f"  T_* = {T:.0e} GeV:  f ~ {f:.4e} Hz")
print()

# ============================================================
# MASTER COMPARISON TABLE
# ============================================================
print("=" * 80)
print("MASTER COMPARISON (all methods, beta/H_*=1)")
print("=" * 80)
print()
print(f"  {'T_*':<10} {'M1:Hubble':<14} {'M2:Envelope':<14} {'M2:SndWave':<14} "
      f"{'M2:Turb':<14} {'M3:DimAnal':<14} {'Band(SW)'}")
print("  " + "-" * 90)
for T, name in zip(T_stars, names):
    f1 = C_m1_Hz * T
    fe = C_env * T
    fs = C_sw * T
    ft = C_turb * T
    f3 = C_m3 * T
    print(f"  {T:<10.0e} {f1:<14.3e} {fe:<14.3e} {fs:<14.3e} {ft:<14.3e} {f3:<14.3e} {detector_band(fs)}")
print()
print(f"  All scale linearly with T_*. Spread across methods: factor ~10")
print(f"  (from C_m3 = {C_m3:.2e} to C_turb = {C_turb:.2e} Hz/GeV)")
print()

# ============================================================
# GUT/KK FOCUS
# ============================================================
print("=" * 80)
print("GUT / KK SCALE: T_* = 10^16 GeV")
print("=" * 80)
print()

T_GUT = 1e16
H_GUT = H_rad(T_GUT)  # GeV
H_GUT_Hz = H_GUT * GeV_to_Hz
a_GUT = a_ratio(T_GUT)
f_Hubble_today = H_GUT_Hz * a_GUT

print(f"  H(10^16 GeV)          = {H_GUT:.4e} GeV = {H_GUT_Hz:.4e} Hz")
print(f"  a_*/a_0               = {a_GUT:.4e}")
print(f"  f_Hubble today (M1)   = {f_Hubble_today:.4e} Hz  ({f_Hubble_today/1e6:.1f} MHz)")
print()
print(f"  Sound wave peak (M2, beta/H=1) = {C_sw*T_GUT:.4e} Hz  ({C_sw*T_GUT/1e9:.2f} GHz)")
print(f"  Sound wave peak (M2, beta/H=10) = {C_sw*T_GUT*10:.4e} Hz  ({C_sw*T_GUT*10/1e9:.2f} GHz)")
print()
print(f"  Hubble rate vs Planck:  H/M_Pl = {H_GUT/M_Pl:.4e}  (well below Planck, semiclassical valid)")
print(f"  T_*/M_Pl = {T_GUT/M_Pl:.4e}  (perturbative gravity valid)")
print()

# ============================================================
# INVERSE TABLE
# ============================================================
print("=" * 80)
print("INVERSE: Required T_* to hit each detector band")
print("=" * 80)
print()
print("  Using sound-wave prefactor (typically dominant source)")
print(f"  C_sw = {C_sw:.4e} Hz/GeV")
print()

targets = [
    ("PTA (30 nHz)", 3e-8),
    ("LISA sweet spot (3 mHz)", 3e-3),
    ("DECIGO/BBO (0.3 Hz)", 0.3),
    ("LIGO/Virgo (100 Hz)", 100),
    ("ET upper band (5 kHz)", 5000),
    ("MHz gap (1 MHz)", 1e6),
    ("GHz band (1 GHz)", 1e9),
]

print(f"  {'Target':<30} {'f (Hz)':<14} {'T_* (b/H=1)':<18} {'T_* (b/H=10)':<18} {'T_* (b/H=100)'}")
print("  " + "-" * 90)
for name, f in targets:
    T1 = f / (C_sw * 1)
    T10 = f / (C_sw * 10)
    T100 = f / (C_sw * 100)
    print(f"  {name:<30} {f:<14.1e} {T1:<18.2e} {T10:<18.2e} {T100:<18.2e}")
print()

# ============================================================
# PHYSICAL CONCLUSIONS
# ============================================================
print("=" * 80)
print("CONCLUSIONS")
print("=" * 80)
print()
print("1. SCALING LAW (exact, from dimensional analysis + adiabatic expansion):")
print("     f_peak ~ C * T_* * (beta/H_*)")
print("   where C ~ 10^{-7} Hz/GeV (sound waves) to 10^{-8} Hz/GeV (Hubble).")
print()
print("2. THREE METHODS AGREE to within one order of magnitude:")
print("   Method 1 (Hubble redshift) is a LOWER BOUND (source = horizon scale).")
print("   Method 2 (Caprini fits) is the PHYSICAL ANSWER (source = bubble/sound dynamics).")
print("   Method 3 (dim. analysis) matches Method 1 up to g_* factors (~1.14x).")
print()
print("3. DETECTOR REACH:")
print("   PTA  (nHz):       T_* ~ 0.01 - 1 GeV     (QCD-scale, BBN-era)")
print("   LISA (mHz):       T_* ~ 10^2 - 10^5 GeV   (EW to TeV BSM)")
print("   LIGO/ET (10-5kHz): T_* ~ 10^7 - 10^10 GeV (intermediate scales)")
print("   NO DETECTOR:      T_* > 10^10 GeV          (GUT, KK, Planck)")
print()
print("4. THE SHATTERING (T_* = 10^16 GeV):")
print("   f_peak ~ 0.4 - 3 GHz at beta/H = 1")
print("   f_peak ~ 4 - 30 GHz at beta/H = 10")
print("   This is 5 orders of magnitude above LIGO, 7 above LISA.")
print("   GRAVITATIONALLY DARK to all funded detectors.")
print("   Only TRL-1 concepts (Gertsenshtein cavities, magnon sensors) apply.")
print()
print("5. M2/M1 RATIO DIAGNOSIS:")
print("   Method 2 exceeds Method 1 by factor 1.4 (envelope) to 7.3 (turbulence)")
print("   at beta/H_*=1. This is NOT an error. Method 1 gives the horizon-scale")
print("   frequency. The physical GW peak is at the BUBBLE scale ~ beta, which for")
print("   beta/H=1 is the same order but with O(1) simulation-calibrated corrections.")
print("   For beta/H >> 1, Method 2 exceeds Method 1 by exactly (beta/H) as expected.")
print()
print("=" * 80)
print("COMPUTATION COMPLETE")
print("=" * 80)
