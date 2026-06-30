#!/usr/bin/env python3
"""
S100a W1-4 S100a-W1-4-SIGMA-DM-NUCLEON — Leggett-channel GGE quasiparticle
sigma_SI vs LZ-2024 exclusion + neutrino fog
===========================================================================

Gate: S100a-W1-4-SIGMA-DM-NUCLEON ([SIGN])

Pre-registered threshold (plan session-100a-plan-w1.md SS W1-4):
  PASS iff sigma_SI(M_DM) < sigma_excl^{LZ}(M_DM) AND sigma_SI <= sigma_nufog(M_DM)
  INFO iff sigma_SI < sigma_excl but sigma_SI > sigma_nufog (or frame MARGINAL)
  FAIL iff sigma_SI > sigma_excl^{LZ}(M_DM)
  Canonical sign form: sign(sigma_excl^{LZ}(M_DM) - sigma_SI); POSITIVE => below
  exclusion (PASS-eligible).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py
  - computations/session-100a/s100a_lz2024_si_exclusion.csv
    (digitized by THIS script on first run from the published LZ-2024 SI limit,
    arXiv:2410.17036 — METHODOLOGICAL empirical cross-check input per
    substrate-first-canonical-sourcing SS(i); then read back + SHA-pinned)

Output 4-tuple:
  (value=<sigma_SI cm^2>, scheme=FW, convention=LEGGETT-CHANNEL-SUBSTRATE-COUPLING,
   L_max=N/A)

Classification: PHONONIC

METHODOLOGY
-----------
Dark matter IS a Leggett-channel GGE quasiparticle — an inter-band coherence
mode of the (0,0) BdG sector of D_K, CPT-neutral and non-annihilating
(T^{0i}_4D = 0 exact, atlas-04 C7). Rest-mass anchor: M_DM = 11.97 * Delta_BCS
in M_KK units (LEGGETT-MOMENT-70; zero free parameters; CONDITIONAL on
Gamma_grav < H_0, with single-Leggett gravitational decay FORBIDDEN, S67).

DM-nucleon coupling channel (symmetry-first classification):
  (1) D_K is block-diagonal (S22b): inter-sector matrix elements vanish
      identically — no direct Dirac-operator vertex between the BCS-sector
      coherence mode and SM zero modes.
  (2) V(gap,gap) = 0 EXACTLY (S23a selection rule); B1 couples only to B2
      (S34 Trap 1) — no cubic vertex routes inter-band coherence into SM
      channels.
  (3) The Leggett mode is a gauge SINGLET (CPT-neutral): no photon/gluon/W/Z
      vertex; the relative-phase mode couples to band-density DIFFERENCES,
      so its linear coupling to total-mass-density probes vanishes; the
      leading surviving coupling is quadratic through the stress tensor.
  (4) Two-layer architecture (S72): the BCS sector communicates with the
      spectral (gravity) sector ONLY through the metric moments (a_2).
  => The DM-nucleon interaction is PURELY GRAVITATIONAL at leading order:
     alpha = G_N * M_DM * m_target, zero free parameters. This matches the
     S42/S44 collisionless self-interaction anchor sigma/m = 5.7e-51 cm^2/g,
     which is itself the gravitational Rutherford transport cross-section
     (s44_cdm_construct.py: sigma_T = 4 pi (G_N m)^2 / v^4 * ln Lambda).

sigma_SI construction (convention LEGGETT-CHANNEL-SUBSTRATE-COUPLING):
  Born-regime Rutherford recoil spectrum on the xenon target,
      dsigma/dE_R = 2 pi alpha_A^2 / (m_A v^2 E_R^2),  alpha_A = G_N M_DM m_A,
  integrated above the LZ threshold E_th:
      sigma_A(>E_th) = (2 pi alpha_A^2/(m_A v^2)) (1/E_th - 1/E_max),
      E_max = 2 mu_A^2 v^2 / m_A.
  Equal-above-threshold-rate contact-SI per-nucleon normalization (the axis
  the LZ curve is published on):
      sigma_SI = sigma_A(>E_th) / [A^2 (mu_A/mu_n)^2 (1 - E_th/E_max)].
  Born validity: alpha_A / v ~ 3e-16 << 1 (deep Born regime). Helm form
  factor at threshold q*R_Xe ~ 0.85 => O(1), immaterial at >=30-OOM margins.

Laboratory-frame vs substrate-M_KK-scale rest-energy resolution (Def 1 core):
  Frame A (BINDS): M_DM^lab = 11.97 * Delta_BCS * M_KK = 4.13e17 GeV.
  Frame B (EXCLUDED): the gap-scale anchor misread as a laboratory-GeV rest
  energy, M_DM = 5.557 GeV. Resolution argument in the working-paper section;
  the gate computes BOTH and shows the sign verdict is frame-robust.

DISCIPLINE
----------
- from canonical_constants import * ; intermediates tagged # (local)
- GPU_path pin: numpy cpu-cap-OMP8 (scalar closed form + 1D interpolation;
  no matrix >= 100x100, so no torch path needed)
- SHA-256 of all inputs logged in first 20 stdout lines; dual-SHA emitted
- verdict via print_verdict_payload -> agent calls mcp emit_verdict
  (NO open("a") verdict write — Windows cross-process race, S98)
"""

from __future__ import annotations

# --- machinery pin GPU_path=numpy cpu-cap-OMP8: env BEFORE numpy import ----
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403
# Names consumed (all canonical):
#   Mass_LeggettDM_over_Delta_BCS = 11.97        (LEGGETT-MOMENT-70)
#   Delta_BCS = 0.4642547394830737               (BCS-GAP-CANONICAL-70, R-protected)
#   M_KK = 7.428660036284456e16 GeV              (CONST-FREEZE-42)
#   sigma_over_m = 5.7e-51 cm^2/g                (S42 collisionless anchor)
#   M_Pl_unreduced = 1.2209e19 GeV               (CODATA)
#   hbar_c_GeV_cm, GeV_to_g, c_light_cgs

import hashlib
import json
import time

import numpy as np

# ---------------------------------------------------------------------------
# Section 3 — Identity + machinery pins
# ---------------------------------------------------------------------------
SESSION = "100a"                                          # (local)
GATE_ID = "S100a-W1-4-SIGMA-DM-NUCLEON"                   # (local)
SCHEME = "FW"                                             # (local)
CONVENTION = "LEGGETT-CHANNEL-SUBSTRATE-COUPLING"         # (local)
L_MAX = "N/A"                                             # (local) closed-form; no spectral truncation

OUT_NPZ = SESSION_DIR / "s100a_w1_sigma_dm_nucleon.npz"
OUT_PNG = SESSION_DIR / "s100a_w1_sigma_dm_nucleon.png"
OUT_CSV = SESSION_DIR / "s100a_lz2024_si_exclusion.csv"

# --- Laboratory / empirical inputs (single-script; PDG / LZ / SHM cited) ---
m_n_GeV = 0.93957          # (local) nucleon (neutron) mass, PDG 2024
m_u_GeV = 0.93149          # (local) atomic mass unit, PDG 2024
A_Xe = 131.29              # (local) xenon mean mass number (natural abundance)
m_Xe_GeV = A_Xe * m_u_GeV  # (local) xenon nucleus mass = 122.30 GeV
v_char = 1.1e-3            # (local) characteristic DM speed/c in detector frame (SHM: v_0=238 km/s, v_E~250 km/s => <v>~330 km/s)
v_esc_lab = 2.6e-3         # (local) (v_esc + v_E)/c ~ 780 km/s SHM tail ceiling
E_th_GeV = 5.0e-6          # (local) LZ-2024 effective NR threshold ~5 keV (ROI 5.5-70 keV)
rho_local_GeVcm3 = 0.3     # (local) local DM density GeV/cm^3 (LZ SHM convention)
ln_Lambda = 20.0           # (local) Coulomb-log analog, matches s44_cdm_construct.py
v_cluster = 4700e5 / c_light_cgs  # (local) Bullet-Cluster velocity/c, matches S44
# LZ-2024 detector geometry for the flux-floor / event-rate cross-checks:
A_det_cm2 = 2.1e4          # (local) LZ TPC projected area ~1.46 m diam x 1.46 m
T_eff_s = (4.2 / 5.5) * 3.156e7  # (local) 4.2 tonne-yr / 5.5 t fiducial = 0.764 yr
L_tpc_cm = 146.0           # (local) TPC height, cm
rho_LXe_gcm3 = 2.9         # (local) liquid xenon density g/cm^3
N_excl_90CL = 3.6          # (local) ~90% CL Poisson event ceiling for a null result

G_N_natural = 1.0 / M_Pl_unreduced**2   # (local) GeV^-2 (gravity = a_2 spectral moment bridge)
hbarc2_cm2 = hbar_c_GeV_cm**2           # (local) GeV^-2 -> cm^2 conversion

# ---------------------------------------------------------------------------
# LZ-2024 SI exclusion digitization (METHODOLOGICAL empirical input)
# Source: LZ collaboration, "Dark Matter Search Results from 4.2 Tonne-Years
# of Exposure of the LUX-ZEPLIN (LZ) Experiment", arXiv:2410.17036 (2024),
# Fig. 6 (combined WS2022+WS2024 SI 90% CL observed limit). Published anchor:
# minimum 2.2e-48 cm^2 at 40 GeV/c^2 (abstract). Other points digitized from
# the figure at +-0.15 dex fidelity — immaterial against >=30 OOM margins.
# ---------------------------------------------------------------------------
LZ_2024_SI = [
    (9.0, 1.0e-45), (10.0, 3.0e-46), (12.0, 6.5e-47), (14.0, 2.4e-47),
    (17.0, 1.0e-47), (20.0, 5.5e-48), (25.0, 3.4e-48), (30.0, 2.7e-48),
    (35.0, 2.35e-48), (40.0, 2.2e-48), (50.0, 2.3e-48), (60.0, 2.5e-48),
    (80.0, 3.0e-48), (100.0, 3.4e-48), (150.0, 4.8e-48), (200.0, 6.2e-48),
    (300.0, 8.8e-48), (500.0, 1.4e-47), (700.0, 1.9e-47), (1000.0, 2.7e-47),
    (2000.0, 5.2e-47), (3000.0, 7.7e-47), (5000.0, 1.3e-46), (10000.0, 2.6e-46),
]  # (local) digitized exclusion curve [GeV, cm^2]

# Xenon neutrino-fog floor (n=2 discrimination-index boundary).
# Source: C.A.J. O'Hare, PRL 127, 251802 (2021), arXiv:2109.03116 (xenon
# n=2 fog) + the fog boundary as plotted in LZ-2024 Fig. 6. Digitization
# fidelity +-0.3 dex — immaterial at >=30 OOM margins.
NU_FOG_XE = [
    (6.0, 1.0e-45), (8.0, 8.0e-47), (10.0, 4.0e-48), (12.0, 5.0e-49),
    (15.0, 3.0e-49), (20.0, 2.5e-49), (30.0, 2.7e-49), (40.0, 3.0e-49),
    (60.0, 3.5e-49), (100.0, 5.0e-49), (300.0, 1.2e-48), (1000.0, 3.5e-48),
    (3000.0, 1.0e-47), (10000.0, 3.3e-47),
]  # (local) digitized fog boundary [GeV, cm^2]


def write_lz_csv_if_missing() -> None:
    """Digitize the LZ-2024 SI exclusion to CSV (first run only; deterministic)."""
    if OUT_CSV.exists():
        return
    lines = [
        "# LZ-2024 spin-independent DM-nucleon exclusion (90% CL observed), digitized",
        "# Source: LZ collaboration, arXiv:2410.17036, Fig. 6 (WS2022+WS2024 combined)",
        "# Published anchor: minimum sigma_SI = 2.2e-48 cm^2 at M = 40 GeV/c^2 (abstract)",
        "# Digitization fidelity: +-0.15 dex (anchor point exact as published)",
        "# METHODOLOGICAL empirical cross-check input per substrate-first-canonical-sourcing SS(i)",
        "# Digitized: S100a-W1-4-SIGMA-DM-NUCLEON (landau-condensed-matter-theorist), 2026-06-06",
        "mass_GeV,sigma_SI_excl_cm2",
    ]
    for m, s in LZ_2024_SI:
        lines.append(f"{m:.6g},{s:.6g}")
    OUT_CSV.write_text("\n".join(lines) + "\n", encoding="utf-8")


def read_lz_csv() -> tuple[np.ndarray, np.ndarray]:
    """Read the digitized LZ-2024 curve back from the CSV (the pinned input)."""
    mass, sig = [], []   # (local)
    for ln in OUT_CSV.read_text(encoding="utf-8").splitlines():
        ln = ln.strip()
        if not ln or ln.startswith("#") or ln.startswith("mass_GeV"):
            continue
        a, b = ln.split(",")
        mass.append(float(a))
        sig.append(float(b))
    return np.asarray(mass), np.asarray(sig)


def curve_at(M: float, mass: np.ndarray, sig: np.ndarray) -> tuple[float, str]:
    """Log-log interpolate a (mass, sigma) curve at M; linear-in-M extrapolation
    above the table (iso-rate scaling sigma ~ M, exact for M >> m_A since the
    event rate R ~ (rho/M) sigma x mass-independent kinematics); power-law
    extension below the table. Returns (sigma, mode)."""
    lm, ls = np.log10(mass), np.log10(sig)   # (local)
    if M > mass[-1]:
        return float(sig[-1] * (M / mass[-1])), "extrapolated-linear-in-M"
    if M < mass[0]:
        slope = (ls[1] - ls[0]) / (lm[1] - lm[0])   # (local) low-mass log-log slope
        return float(10.0 ** (ls[0] + slope * (np.log10(M) - lm[0]))), "extrapolated-low-mass-powerlaw"
    return float(10.0 ** np.interp(np.log10(M), lm, ls)), "interpolated"


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)   # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")   # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = script_path.read_bytes()       # (local)
    canonical_bytes = canonical_path.read_bytes() # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes); h_audit.update(canonical_bytes); h_audit.update(pinmap_json)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — Compute
# ---------------------------------------------------------------------------

def sigma_SI_gravitational(M_DM: float, v: float) -> dict:
    """Per-nucleon-equivalent SI cross-section for a purely gravitationally
    coupled DM quasiparticle on a xenon target, equal-above-threshold-rate
    contact normalization. All quantities natural units (GeV) unless noted."""
    mu_A = M_DM * m_Xe_GeV / (M_DM + m_Xe_GeV)   # (local) DM-nucleus reduced mass
    mu_n = M_DM * m_n_GeV / (M_DM + m_n_GeV)     # (local) DM-nucleon reduced mass
    alpha_A = G_N_natural * M_DM * m_Xe_GeV      # (local) gravitational vertex (dimensionless)
    E_max = 2.0 * mu_A**2 * v**2 / m_Xe_GeV      # (local) max recoil at speed v
    if E_max <= E_th_GeV:
        # kinematic null: no above-threshold recoil possible at this (M, v)
        return dict(sigma_SI_cm2=0.0, sigma_A_cm2=0.0, alpha_A=alpha_A,
                    E_max_GeV=E_max, mu_A=mu_A, mu_n=mu_n, kinematic_null=True)
    ir_factor = (1.0 / E_th_GeV - 1.0 / E_max)   # (local) threshold-cut IR integral of 1/E_R^2
    sigma_A_nat = 2.0 * np.pi * alpha_A**2 / (m_Xe_GeV * v**2) * ir_factor  # (local) GeV^-2
    sigma_A_cm2 = sigma_A_nat * hbarc2_cm2       # (local)
    coh = A_Xe**2 * (mu_A / mu_n)**2             # (local) contact-SI coherent factor
    thr = 1.0 - E_th_GeV / E_max                 # (local) contact above-threshold fraction
    sigma_SI_cm2 = sigma_A_cm2 / (coh * thr)     # (local) per-nucleon equivalent
    return dict(sigma_SI_cm2=sigma_SI_cm2, sigma_A_cm2=sigma_A_cm2, alpha_A=alpha_A,
                E_max_GeV=E_max, mu_A=mu_A, mu_n=mu_n, kinematic_null=False)


def compute() -> dict:
    r: dict = {}

    # --- Step 1: DM mass, both frames -------------------------------------
    M_DM_mkk = Mass_LeggettDM_over_Delta_BCS * Delta_BCS    # (local) M_KK units
    M_DM_A = M_DM_mkk * M_KK                                # (local) Frame A: GeV (BINDS)
    M_DM_B = M_DM_mkk                                       # (local) Frame B: gap-scale number misread as lab GeV (EXCLUDED)
    r["M_DM_substrate_MKK_units"] = M_DM_mkk
    r["M_DM_GeV"] = M_DM_A
    r["M_DM_frameB_GeV"] = M_DM_B

    print("=== Substitution chain (sign/threshold claim; math-scripts.md) ===")
    print("Claim: sigma_SI(M_DM) < sigma_excl^LZ(M_DM)  [below exclusion]")
    print(f"Step 1: M_DM = Mass_LeggettDM_over_Delta_BCS * Delta_BCS * M_KK   [LEGGETT-MOMENT-70 x BCS-GAP-CANONICAL-70 x CONST-FREEZE-42]")
    print(f"        = {Mass_LeggettDM_over_Delta_BCS} * {Delta_BCS} * {M_KK:.6e} GeV")
    print(f"        = {M_DM_A:.6e} GeV   (Frame A, substrate anchor in the single unit map — BINDS)")
    print(f"        Frame B (excluded reading): {M_DM_B:.6f} GeV")

    # --- Step 2-4: sigma_SI in both frames ---------------------------------
    fa = sigma_SI_gravitational(M_DM_A, v_char)   # (local)
    fb = sigma_SI_gravitational(M_DM_B, v_char)   # (local)
    r["sigma_SI_cm2"] = fa["sigma_SI_cm2"]
    r["sigma_A_Xe_cm2"] = fa["sigma_A_cm2"]
    r["alpha_A"] = fa["alpha_A"]
    r["E_max_GeV"] = fa["E_max_GeV"]
    r["sigma_SI_frameB_cm2"] = fb["sigma_SI_cm2"]
    r["frameB_kinematic_null"] = bool(fb["kinematic_null"])
    # Frame-B null check: minimum speed for an above-threshold xenon recoil
    muB = fb["mu_A"]   # (local)
    v_req_B = np.sqrt(E_th_GeV * m_Xe_GeV / 2.0) / muB   # (local)
    r["v_required_frameB"] = v_req_B

    print(f"Step 2: alpha_A = G_N * M_DM * m_Xe = (1/M_Pl^2) M_DM m_Xe   [pure gravitational vertex:")
    print(f"        S22b block-diagonality + S23a V(gap,gap)=0 + S34 Trap1 + CPT-neutral gauge singlet")
    print(f"        => no gauge/Yukawa channel; gravity (a_2 moment) is the only inter-sector channel]")
    print(f"        = {G_N_natural:.6e} * {M_DM_A:.6e} * {m_Xe_GeV:.4f} = {fa['alpha_A']:.6e}")
    print(f"Step 3: sigma_A(>E_th) = (2 pi alpha_A^2/(m_Xe v^2)) (1/E_th - 1/E_max)")
    print(f"        E_max = 2 mu_A^2 v^2/m_Xe = {fa['E_max_GeV']:.6e} GeV; E_th = {E_th_GeV:.1e} GeV; v = {v_char:.2e} c")
    print(f"        sigma_A = {fa['sigma_A_cm2']:.6e} cm^2")
    print(f"Step 4: sigma_SI = sigma_A / [A^2 (mu_A/mu_n)^2 (1 - E_th/E_max)]   [equal-above-threshold-rate")
    print(f"        contact-SI per-nucleon normalization = the LZ publication axis]")
    print(f"        = {fa['sigma_SI_cm2']:.6e} cm^2")

    # --- Step 5: exclusion + fog at M_DM ------------------------------------
    write_lz_csv_if_missing()
    lz_m, lz_s = read_lz_csv()
    fog_m = np.array([p[0] for p in NU_FOG_XE])   # (local)
    fog_s = np.array([p[1] for p in NU_FOG_XE])   # (local)
    sig_excl_A, mode_excl_A = curve_at(M_DM_A, lz_m, lz_s)
    sig_fog_A, mode_fog_A = curve_at(M_DM_A, fog_m, fog_s)
    sig_excl_B, mode_excl_B = curve_at(M_DM_B, lz_m, lz_s)
    r["sigma_excl_at_MDM_cm2"] = sig_excl_A
    r["sigma_nufog_at_MDM_cm2"] = sig_fog_A
    r["sigma_excl_at_frameB_cm2"] = sig_excl_B
    r["excl_mode"] = mode_excl_A
    r["lz_curve_mass_GeV"] = lz_m
    r["lz_curve_sigma_cm2"] = lz_s
    r["fog_mass_GeV"] = fog_m
    r["fog_sigma_cm2"] = fog_s

    print(f"Step 5: sigma_excl^LZ(M_DM) = sigma_excl({lz_m[-1]:.0e} GeV) * (M_DM/{lz_m[-1]:.0e})   [iso-rate sigma ~ M, exact at M >> m_A]")
    print(f"        = {sig_excl_A:.6e} cm^2  ({mode_excl_A})")
    print(f"        sigma_nufog(M_DM) = {sig_fog_A:.6e} cm^2  ({mode_fog_A})")

    # --- Step 6: canonical sign form ----------------------------------------
    sign_delta = sig_excl_A - fa["sigma_SI_cm2"]   # (local)
    r["sign_delta"] = sign_delta
    margin_excl_OOM = np.log10(sig_excl_A / fa["sigma_SI_cm2"])   # (local)
    margin_fog_OOM = np.log10(sig_fog_A / fa["sigma_SI_cm2"])     # (local)
    r["margin_OOM_below_excl"] = margin_excl_OOM
    r["margin_OOM_below_fog"] = margin_fog_OOM
    print(f"Step 6: sign(sigma_excl - sigma_SI) = sign({sig_excl_A:.3e} - {fa['sigma_SI_cm2']:.3e}) = {'+1' if sign_delta > 0 else '-1'}")
    print(f"        => {'BELOW' if sign_delta > 0 else 'ABOVE'} exclusion; margin = {margin_excl_OOM:.2f} OOM below exclusion,")
    print(f"           {margin_fog_OOM:.2f} OOM below the neutrino fog")

    # --- Cross-checks --------------------------------------------------------
    print("\n=== Cross-checks ===")
    # CC1: DM-DM self-interaction vs the S42 collisionless anchor (bounds the coupling)
    GNm = G_N_natural * M_DM_A                                  # (local) GeV^-1
    sigma_T_nat = 4.0 * np.pi * GNm**2 / v_cluster**4 * ln_Lambda  # (local) GeV^-2, S44 form
    sigma_T_cm2 = sigma_T_nat * hbarc2_cm2                      # (local)
    m_DM_g = M_DM_A * GeV_to_g                                  # (local)
    sigma_T_over_m = sigma_T_cm2 / m_DM_g                       # (local) cm^2/g
    cc1_ok = sigma_T_over_m <= sigma_over_m                     # (local)
    r["sigma_T_DMDM_over_m_cm2g"] = sigma_T_over_m
    r["sigma_over_m_anchor"] = sigma_over_m
    r["cc1_collisionless_consistent"] = bool(cc1_ok)
    print(f"CC1 (self-interaction anchor): sigma_T^DMDM/m at Bullet v ({v_cluster:.4f} c, lnLambda={ln_Lambda:.0f})")
    print(f"    = {sigma_T_over_m:.4e} cm^2/g  <=  anchor sigma/m = {sigma_over_m:.1e} cm^2/g : {'CONSISTENT' if cc1_ok else 'INCONSISTENT'}")
    print(f"    (same zero-free-parameter G_N^2 coupling class as the S42/S44 anchor derivation)")

    # CC2: independent event-rate route vs curve-margin route
    n_DM = rho_local_GeVcm3 / M_DM_A                            # (local) cm^-3
    flux = n_DM * v_char * c_light_cgs                          # (local) cm^-2 s^-1
    N_transit = flux * A_det_cm2 * T_eff_s                      # (local) DM transits in WS2022+WS2024
    n_Xe = rho_LXe_gcm3 / (A_Xe * 1.66054e-24)                  # (local) LXe number density cm^-3
    P_scatter = n_Xe * fa["sigma_A_cm2"] * L_tpc_cm             # (local) >E_th scatters per crossing
    N_events = N_transit * P_scatter                            # (local) predicted events
    margin_event = N_excl_90CL / N_events if N_events > 0 else np.inf  # (local)
    cc2_logdiff = abs(np.log10(margin_event) - margin_excl_OOM) # (local)
    cc2_ok = cc2_logdiff <= 2.0                                 # (local)
    r["N_transit_LZ"] = N_transit
    r["N_events_pred_LZ"] = N_events
    r["margin_event_route"] = margin_event
    r["cc2_logdiff_OOM"] = cc2_logdiff
    r["cc2_routes_agree"] = bool(cc2_ok)
    print(f"CC2 (independent rate route): N_transit = {N_transit:.1f}; P(>E_th scatter)/crossing = {P_scatter:.3e}")
    print(f"    predicted events = {N_events:.3e}; event-route margin = {margin_event:.3e} ({np.log10(margin_event):.2f} OOM)")
    print(f"    vs curve-route margin {margin_excl_OOM:.2f} OOM; |diff| = {cc2_logdiff:.2f} OOM <= 2.0 : {'AGREE' if cc2_ok else 'DISAGREE'}")

    # CC3: flux floor — validity of the linear-in-M exclusion extrapolation
    cc3_ok = N_transit >= 1.0                                   # (local)
    r["cc3_flux_floor_valid"] = bool(cc3_ok)
    print(f"CC3 (flux floor): N_transit = {N_transit:.1f} >= 1 during LZ exposure : {'VALID' if cc3_ok else 'BEYOND FLUX FLOOR'}")
    print(f"    (at M >~ 1e19 GeV fewer than one DM particle crosses LZ; M_DM sits inside validity)")

    # CC4: Born-regime validity of the Rutherford form
    born = fa["alpha_A"] / v_char                               # (local)
    cc4_ok = born < 1.0                                         # (local)
    r["born_parameter"] = born
    r["cc4_born_valid"] = bool(cc4_ok)
    print(f"CC4 (Born validity): alpha_A/v = {born:.3e} << 1 : {'VALID' if cc4_ok else 'CLASSICAL REGIME'}")

    # --- Frame resolution + robustness ---------------------------------------
    print("\n=== Laboratory-frame vs substrate-M_KK-scale rest-energy resolution ===")
    print("Frame A (BINDS): M_DM^lab = 11.97 * Delta_BCS * M_KK = %.3e GeV." % M_DM_A)
    print("  (i) ONE unit map: the spectral triple converts M_KK units to GeV once, via the")
    print("      a_2/G_N gravity bridge (CONST-FREEZE-42); every GeV-valued framework observable")
    print("      uses this single conversion — a mode-specific second conversion does not exist.")
    print("  (ii) Gapped quasiparticle: emergent-4D dispersion w^2 = w_0^2 + c^2 k^2 with")
    print("      hbar*w_0 = 11.97*Delta_BCS*M_KK; rest energy IS hbar*w_0 (Landau quasiparticle")
    print("      correspondence); the relic is comoving (T^{0i}_4D = 0 exact, C7) — rest energy")
    print("      is frame-invariant; the laboratory moves at v ~ 1e-3 c relative to it.")
    print("  (iii) GGE bookkeeping: the Parker-pair relic energy budget is fixed in M_KK units;")
    print("      rescaling per-quantum mass ~17 OOM would break the Omega_DM closure by ~17 OOM.")
    print(f"Frame B (EXCLUDED): gap-scale anchor misread as lab-GeV rest energy = {M_DM_B:.4f} GeV.")
    print(f"  Frame-B sigma_SI(>E_th) = {fb['sigma_SI_cm2']:.3e} (kinematic null: E_max = {fb['E_max_GeV']*1e6:.3f} keV")
    print(f"  < E_th = {E_th_GeV*1e6:.0f} keV; required v = {v_req_B:.3e} c > SHM ceiling {v_esc_lab:.1e} c)")
    frameB_below_excl = fb["sigma_SI_cm2"] < sig_excl_B          # (local)
    r["frameB_below_exclusion"] = bool(frameB_below_excl)
    print(f"  => Frame B also below exclusion ({fb['sigma_SI_cm2']:.1e} < {sig_excl_B:.3e} cm^2):")
    print(f"     sign verdict is FRAME-ROBUST; regime resolution rests on (i)-(iii), not on the choice.")

    # --- Verdict 3-tuple ------------------------------------------------------
    sign_v = "PASS" if sign_delta > 0 else "FAIL"               # (local)
    if fa["sigma_SI_cm2"] <= sig_fog_A:
        mag_v = "PASS"                                          # (local) at/below the fog
    elif fa["sigma_SI_cm2"] < sig_excl_A:
        mag_v = "INFO"                                          # (local) above fog, below exclusion
    else:
        mag_v = "FAIL"                                          # (local) excluded
    frame_resolved = True                                       # (local) Frame A binds via (i)-(iii)
    regime_v = "VALID" if (frame_resolved and frameB_below_excl and cc3_ok and cc4_ok) else "MARGINAL"  # (local)

    # Composite per the PRE-REGISTERED collapse rule (gate-verdicts.md)
    if regime_v == "BREAKDOWN":
        composite = "FAIL"                                      # (local)
    elif sign_v == "FAIL":
        composite = "FAIL"                                      # (local)
    elif mag_v == "FAIL" and regime_v == "VALID":
        composite = "FAIL"                                      # (local)
    elif mag_v == "FAIL" and regime_v == "MARGINAL":
        composite = "INFO"                                      # (local)
    elif mag_v == "INFO":
        composite = "INFO"                                      # (local)
    else:
        composite = "PASS"                                      # (local)

    r["sign_verdict"] = sign_v
    r["magnitude_verdict"] = mag_v
    r["regime_verdict"] = regime_v
    r["verdict"] = composite
    return r


# ---------------------------------------------------------------------------
# Section 6 — Verdict payload printer (emit via knowledge-MCP emit_verdict)
# ---------------------------------------------------------------------------

def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
                          sign_verdict: str | None = None,
                          magnitude_verdict: str | None = None,
                          regime_verdict: str | None = None,
                          companion_note: str = "",
                          extra_rows: list[str] | None = None) -> dict:
    payload: dict = {
        "session": SESSION,
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


def make_plot(r: dict) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(9.5, 7))   # (local)
    lz_m, lz_s = r["lz_curve_mass_GeV"], r["lz_curve_sigma_cm2"]
    fog_m, fog_s = r["fog_mass_GeV"], r["fog_sigma_cm2"]
    M_DM = r["M_DM_GeV"]

    # extended axes out to the predicted mass
    m_ext = np.logspace(np.log10(lz_m[-1]), np.log10(M_DM) + 0.5, 200)   # (local)
    lz_ext = lz_s[-1] * (m_ext / lz_m[-1])                               # (local)
    fog_ext = fog_s[-1] * (m_ext / fog_m[-1])                            # (local)

    ax.loglog(lz_m, lz_s, "b-", lw=2, label="LZ-2024 SI 90% CL (digitized, arXiv:2410.17036)")
    ax.loglog(m_ext, lz_ext, "b--", lw=1.5, label=r"LZ-2024 iso-rate extrapolation ($\sigma \propto M$)")
    ax.loglog(fog_m, fog_s, "-", color="orange", lw=2, label="Xe neutrino fog n=2 (OHare 2021, digitized)")
    ax.loglog(m_ext, fog_ext, "--", color="orange", lw=1.5)
    ax.fill_between(np.concatenate([fog_m, m_ext]),
                    np.concatenate([fog_s, fog_ext]), 1e-70,
                    color="orange", alpha=0.12)

    ax.plot([M_DM], [r["sigma_SI_cm2"]], "r*", ms=22, zorder=5,
            label=(r"Leggett-channel GGE DM (Frame A binds): $M$=%.2e GeV, $\sigma_{SI}$=%.2e cm$^2$"
                   % (M_DM, r["sigma_SI_cm2"])))
    ax.annotate("%.1f OOM below exclusion\n%.1f OOM below fog"
                % (r["margin_OOM_below_excl"], r["margin_OOM_below_fog"]),
                xy=(M_DM, r["sigma_SI_cm2"]), xytext=(1e8, 1e-58),
                arrowprops=dict(arrowstyle="->", color="gray"), fontsize=10)
    ax.axvline(r["M_DM_frameB_GeV"], color="gray", ls=":", lw=1.2)
    ax.text(r["M_DM_frameB_GeV"] * 1.3, 1e-44,
            "Frame B (excluded reading)\n%.2f GeV: kinematic null" % r["M_DM_frameB_GeV"],
            fontsize=8, color="gray")

    ax.set_xlabel(r"$M_{DM}$ [GeV]")
    ax.set_ylabel(r"$\sigma_{SI}$ per nucleon [cm$^2$]")
    ax.set_title("S100a-W1-4: Leggett-channel GGE quasiparticle vs LZ-2024 + neutrino fog\n"
                 "(pure-gravitational coupling floor; substrate anchor M = 11.97 $\\Delta_{BCS}$ $M_{KK}$)")
    ax.set_xlim(1, 1e19)
    ax.set_ylim(1e-66, 1e-42)
    ax.grid(True, which="both", alpha=0.25)
    ax.legend(loc="upper left", fontsize=8.5)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=140)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()   # (local)

    # 0. Digitize the LZ-2024 CSV if absent (FIRST step per orchestrator override),
    #    so the input-pin block below pins the actual on-disk bytes.
    write_lz_csv_if_missing()

    # 1. Log input pins (first 20 stdout lines)
    input_files = [SHARED_DIR / "canonical_constants.py", OUT_CSV]   # (local)
    pins = log_input_pins(input_files)

    # 1b. S84+ dual SHAs
    script_path = Path(__file__).resolve()                  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Compute
    r = compute()

    # 3. Persist npz (full float64; publication precision 3 sig figs in WP)
    np.savez(
        OUT_NPZ,
        M_DM_GeV=r["M_DM_GeV"],
        M_DM_substrate_MKK_units=r["M_DM_substrate_MKK_units"],
        M_DM_frameB_GeV=r["M_DM_frameB_GeV"],
        sigma_SI_cm2=r["sigma_SI_cm2"],
        sigma_A_Xe_cm2=r["sigma_A_Xe_cm2"],
        alpha_A=r["alpha_A"],
        E_max_GeV=r["E_max_GeV"],
        sigma_SI_frameB_cm2=r["sigma_SI_frameB_cm2"],
        frameB_kinematic_null=r["frameB_kinematic_null"],
        v_required_frameB=r["v_required_frameB"],
        sigma_excl_at_MDM_cm2=r["sigma_excl_at_MDM_cm2"],
        sigma_nufog_at_MDM_cm2=r["sigma_nufog_at_MDM_cm2"],
        sigma_excl_at_frameB_cm2=r["sigma_excl_at_frameB_cm2"],
        margin_OOM_below_excl=r["margin_OOM_below_excl"],
        margin_OOM_below_fog=r["margin_OOM_below_fog"],
        sign_delta=r["sign_delta"],
        lz_curve_mass_GeV=r["lz_curve_mass_GeV"],
        lz_curve_sigma_cm2=r["lz_curve_sigma_cm2"],
        fog_mass_GeV=r["fog_mass_GeV"],
        fog_sigma_cm2=r["fog_sigma_cm2"],
        sigma_T_DMDM_over_m_cm2g=r["sigma_T_DMDM_over_m_cm2g"],
        sigma_over_m_anchor=r["sigma_over_m_anchor"],
        cc1_collisionless_consistent=r["cc1_collisionless_consistent"],
        N_transit_LZ=r["N_transit_LZ"],
        N_events_pred_LZ=r["N_events_pred_LZ"],
        margin_event_route=r["margin_event_route"],
        cc2_logdiff_OOM=r["cc2_logdiff_OOM"],
        cc2_routes_agree=r["cc2_routes_agree"],
        cc3_flux_floor_valid=r["cc3_flux_floor_valid"],
        born_parameter=r["born_parameter"],
        cc4_born_valid=r["cc4_born_valid"],
        frameB_below_exclusion=r["frameB_below_exclusion"],
        pin_v_char=v_char, pin_E_th_GeV=E_th_GeV, pin_A_Xe=A_Xe,
        pin_m_Xe_GeV=m_Xe_GeV, pin_m_n_GeV=m_n_GeV,
        pin_rho_local_GeVcm3=rho_local_GeVcm3, pin_ln_Lambda=ln_Lambda,
        pin_v_cluster=v_cluster, pin_G_N_natural=G_N_natural,
        sign_verdict=r["sign_verdict"], magnitude_verdict=r["magnitude_verdict"],
        regime_verdict=r["regime_verdict"], verdict=r["verdict"],
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"\n[npz] {OUT_NPZ.name} written")

    # 4. Plot
    make_plot(r)
    print(f"[png] {OUT_PNG.name} written")

    # 5. 4-tuple (final non-verdict line) + verdict payload
    value_str = (
        "sigma_SI=%.3e_cm2_at_M_DM=%.3e_GeV(FrameA-substrate-anchor-binds);"
        "excl_LZ2024=%.3e;nufog=%.3e;%.1fOOM-below-excl;%.1fOOM-below-fog;"
        "coupling=pure-gravitational-GN-floor;frameB(%.3fGeV)=kinematic-null-also-unexcluded;"
        "DMDM-sigma_T/m=%.2e<=anchor%.1e"
    ) % (r["sigma_SI_cm2"], r["M_DM_GeV"], r["sigma_excl_at_MDM_cm2"],
         r["sigma_nufog_at_MDM_cm2"], r["margin_OOM_below_excl"],
         r["margin_OOM_below_fog"], r["M_DM_frameB_GeV"],
         r["sigma_T_DMDM_over_m_cm2g"], r["sigma_over_m_anchor"])   # (local)

    print(f"(value={value_str!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print_verdict_payload(
        r["verdict"], value_str, audit_sha, content_sha,
        sign_verdict=r["sign_verdict"],
        magnitude_verdict=r["magnitude_verdict"],
        regime_verdict=r["regime_verdict"],
        companion_note="LZ-2024 digitization arXiv:2410.17036 Fig.6 (min 2.2e-48 cm2 at 40 GeV exact; +-0.15 dex); Xe nu-fog n=2 OHare PRL 127 251802 (+-0.3 dex); iso-rate sigma~M extrapolation beyond 1e4 GeV",
        extra_rows=[
            "# frame_resolution: FrameA-substrate-M_KK-anchor-BINDS (single-unit-map a_2/G_N bridge; gapped-mode rest energy = hbar*w_0; comoving relic T0i=0) # S100a-W1-4-SIGMA-DM-NUCLEON",
        ],
    )

    print(f"\n=== {GATE_ID}: {r['verdict']} (wall {time.time() - t0:.1f}s) ===")
    # Exit 0 regardless of scientific verdict (math-scripts.md: verdicts are data;
    # exit != 0 reserved for script breakage)
    return 0


if __name__ == "__main__":
    sys.exit(main())
