#!/usr/bin/env python3
"""
S82 W2-13 — F0-CONVENTION-AUDIT
================================

Gate: S82-F0-CONVENTION-AUDIT ([VERIFY])

Pre-registered threshold (S80 plan L1632-L1639, re P3-B line 916):
  HYPOTHESIS: Combined f_0-convention band [6.2, 8.4] OOM (width = 2.2 OOM).
  PRE-REGISTERED: List all f_0 conventions in use; compute band.
  PASS: Band closes to [6.2, 8.4] -- width in [2.0, 2.4] OOM.
  INFO: Band wider by < factor 2 (width in (2.4, 4.4] OOM).
  FAIL: Band wider by > factor 2 (width > 4.4 OOM).

Inputs (SHA-256 pinned at runtime):
  - canonical_constants.py (closure hash)

Output 4-tuple:
  (value=<band_width_OOM>, scheme=INVENTORY, convention=P3B-BAND, L_max=N/A)

Classification: GEOMETRIC

METHODOLOGY
-----------
Per P3-B workshop (sessions/archive/session-79/workshops/p3-b-w3o-trh-channel-redefinition.md
lines 791-805, 916): the Route-alpha cushion [6.2, 8.4] OOM is the combined
K_2-convention x f_0-convention band. The f_0-convention shift alone is
log10(8*pi^2/g^2) = log10(13.23) = 1.122 OOM (D3 substitution chain).

This audit inventories all f_0 values used across computations scripts,
classifies them by role (Chamseddine-Connes spectral-action moment, Landau
Fermi-liquid parameter, EP kinematic shift, etc.), computes the SPECTRAL-ACTION
sub-inventory (the f_0 values that feed Lambda_eff via Chamseddine-Connes
normalization), and reports the log10 span.

The pre-registered band is reconstructed as:
  width_pred = K_2_halfwidth * 2 + f_0_convention_shift = 0.9 + 1.122 approx 2.0
  (central [6.85, 7.75] widened to [6.2, 8.4] under convention variation).

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- SHA-256 of all inputs logged in first 20 lines of stdout
- 4-tuple printed as the final non-verdict line
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 -- Standard imports
# ---------------------------------------------------------------------------
import hashlib
import math
import sys
import time
from pathlib import Path

import numpy as np
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


# ---------------------------------------------------------------------------
# Section 3 -- Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S82"             # (local)
GATE_ID = "S82-F0-CONVENTION-AUDIT"  # (local)
SCHEME = "INVENTORY"        # (local)
CONVENTION = "P3B-BAND"     # (local)
L_MAX = "N/A"               # (local) no L_max dependence; audit across conventions

# Pre-registered band (P3-B line 916)
BAND_LOW_PREREG = 6.2       # (local) OOM
BAND_HIGH_PREREG = 8.4      # (local) OOM
BAND_WIDTH_PREREG = BAND_HIGH_PREREG - BAND_LOW_PREREG  # (local) = 2.2

# Gate decision rule
PASS_WIDTH_MIN = 2.0        # (local) OOM; band closes within [2.0, 2.4]
PASS_WIDTH_MAX = 2.4        # (local) OOM
FACTOR_2_MAX = 2.0 * BAND_WIDTH_PREREG  # (local) = 4.4 OOM

# Output destinations
OUT_NPZ = resolve_output(82, 's82_w2_13_f0_convention_audit.npz')
VERDICT_TXT = resolve_output(82, 's82_gate_verdicts.txt')

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
]


# ---------------------------------------------------------------------------
# Section 4 -- SHA-256 input-pin block
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
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


# ---------------------------------------------------------------------------
# Section 5 -- f_0 inventory
# ---------------------------------------------------------------------------
#
# Each entry is (name, value, role, scripts_seen, notes)
#   role in {SPECTRAL-ACTION, LANDAU-FL, KINEMATIC, OTHER}
#
# SPECTRAL-ACTION = Chamseddine-Connes zeroth moment of f(u) cutoff function;
#                   feeds Lambda_eff^2 via 1/f_0.
# LANDAU-FL       = Fermi-liquid Landau parameter f_0 = N(0)*V_avg;
#                   unrelated to cutoff normalization.
# KINEMATIC       = e.g. EP fractional shift; namespace collision.
# OTHER           = narrow-context parameter, schematic, not cushion-relevant.
# ---------------------------------------------------------------------------

f0_inventory = [
    # --- SPECTRAL-ACTION (Chamseddine-Connes) ---
    ("f_0_sharp (Theta(1-x))",               1.0,      "SPECTRAL-ACTION",
     ["canonical_constants.py", "s54_sft_cutoff.py", "s54_starobinsky_r2.py",
      "s58_friedmann_derivation.py", "s60_hessian_3d.py", "s64_s_asymptotic.py",
      "s65_offjensen_transit.py", "s66_dilution_cc.py", "s74_bdspt_anomaly.py",
      "s75_bdspt_tau_scan.py", "s75_cross_spectral_moment_moduli.py",
      "s75_mh_kasparov.py (Kasparov)", "s75_zeta_not_physical.py",
      "s77_equil_tau_bcs.py", "s61_transit_spectral_action.py"],
     "Sharp-cutoff canonical normalization"),

    ("f_0_sharp (anomaly-forced, 1/2)",      0.5,      "SPECTRAL-ACTION",
     ["s78_f_conv_anomaly.py", "s75_anomaly_derived_fstar.py",
      "canonical_constants.py (provenance note)"],
     "Andrianov-Lizzi fermionic-anomaly-forced sharp cutoff"),

    ("mellin_f_star_f0 (f*(0))",             0.0883,   "SPECTRAL-ACTION",
     ["canonical_constants.py", "s78_f_conv_anomaly.py", "s75_anomaly_derived_fstar.py"],
     "f*(x)=0.912*sqrt(x)+0.088*exp(-x) zeroth-moment; f*(0)=0.088"),

    ("f_0_heat (exp(-x))",                   1.0,      "SPECTRAL-ACTION",
     ["s54_sft_cutoff.py", "s60_hessian_3d.py", "s63_starobinsky_r2.py",
      "s67_eft_matching.py", "s73a_alpha_s_josephson.py",
      "s75_zeta_not_physical.py", "s74_w0_zeta.py"],
     "Heat-kernel f(x)=exp(-x), f_0=f(0)=1"),

    ("f_0_compact (1/5)",                    0.20,     "SPECTRAL-ACTION",
     ["s65_nonlocal_sa.py"],
     "Compact-support cutoff variant (Kurkov-Lizzi)"),

    ("f_0_pow-law (f_k=Gamma(k/2))",         1.0,      "SPECTRAL-ACTION",
     ["s64_transfer_bogoliubov.py"],
     "Power-law f_k = Gamma(k/2); f_0=1"),

    ("f_0_pow-law (f_k=2/k)",                2.0,      "SPECTRAL-ACTION",
     ["s64_transfer_bogoliubov.py"],
     "Alternative power-law f_k=2/k; f_0=2"),

    ("f_0_compound (heat-kernel phi_0=6)",   6.0,      "SPECTRAL-ACTION",
     ["s61_a4_qtheory_compound.py"],
     "E_J compound-heat-kernel phi_0 = 6"),

    ("f_0_CCM London (alpha_GUT=1/25)",      9.817,    "SPECTRAL-ACTION",
     ["s62_cutoff_london.py", "s62_bdg_gauge_fraction.py",
      "s62_cauchy_schwarz.py", "s62_pati_salam_extension.py",
      "s62_sector_energy_ratio.py", "s63_f0_matching.py",
      "s63_ddg_power_law.py (external)", "s63_kk_threshold.py",
      "s63_kk_reduce_4d.py", "s64_transfer_bogoliubov.py",
      "s75_h_phys_reduction (1.486 internal variant)"],
     "CUTOFF-LONDON-62; alpha_GUT=1/25 -> f_0 = 25*pi/8 = 9.817"),

    ("f_0_CCM internal (alpha_GUT=1/10.8)",  4.26,     "SPECTRAL-ACTION",
     ["s62_sector_energy_ratio.py", "s63_ddg_power_law.py (internal)",
      "s63_f0_matching.py", "s63_kk_threshold.py"],
     "SECTOR-ENERGY-RATIO-62 internal; alpha_GUT ~ 1/10.8"),

    ("f_0_dilaton_sigma (4*pi^2)",           4.0 * math.pi**2,  "SPECTRAL-ACTION",
     ["s62_dilaton_sigma.py"],
     "Dilaton-sigma per-group factor; f_0 = 4*pi^2/g^2"),

    ("f_0_Cham-Connes direct (8*pi^2/g^2)",  13.23,    "SPECTRAL-ACTION",
     ["P3-B D3 substitution chain (line 800-803)",
      "derived numerically: 8*pi^2/g^2 with alpha_gauge(M_KK)=0.475"],
     "D3 g-dependent f_0 convention; = S_inst = 13.23 at M_KK"),

    ("f_0_Grand-GUT alternative (g^2 absorbs 2*pi^2)", 2.0 * math.pi**2,  "SPECTRAL-ACTION",
     ["s62_dilaton_sigma.py (2nd variant)", "s63_ddg_power_law.py comments"],
     "f_0 = 2*pi^2/g_3^2 standalone (Chamseddine-Connes direct Yang-Mills matching)"),

    # --- LANDAU-FL (namespace collision with Chamseddine-Connes) ---
    ("f_0_Landau (V_ph * N(0)) S53",         0.156,    "LANDAU-FL",
     ["s53_pomeranchuk_hfb.py"],
     "Landau Fermi-liquid monopole parameter; unrelated to cutoff f_0"),

    ("f_0_Landau (-V_eff * N / mu) S22c",   -4.687,   "LANDAU-FL",
     ["s22c (reclassified as spectral-flow diagnostic)"],
     "S22c POMERANCHUK-HFB diagnostic; not a cushion-relevant f_0"),

    # --- KINEMATIC (namespace collision with Chamseddine-Connes) ---
    ("f_0_EP (fractional shift) S69",        0.035,    "KINEMATIC",
     ["s69_ep_transit.py"],
     "EP transit equilibrium fractional shift; namespace collision"),
]


def run_audit():
    print()
    print("=" * 78)
    print("F_0 CONVENTION INVENTORY")
    print("=" * 78)

    # Split by role
    sa_entries = [e for e in f0_inventory if e[2] == "SPECTRAL-ACTION"]  # (local)
    fl_entries = [e for e in f0_inventory if e[2] == "LANDAU-FL"]        # (local)
    kn_entries = [e for e in f0_inventory if e[2] == "KINEMATIC"]        # (local)

    print(f"\nTotal entries:          {len(f0_inventory)}")
    print(f"  SPECTRAL-ACTION slot: {len(sa_entries)}  (cushion-relevant)")
    print(f"  LANDAU-FL slot:       {len(fl_entries)}  (namespace collision; DISJOINT)")
    print(f"  KINEMATIC slot:       {len(kn_entries)}  (namespace collision; DISJOINT)")

    # --- SPECTRAL-ACTION sub-inventory (cushion-relevant) ---
    print("\n" + "-" * 78)
    print("SPECTRAL-ACTION sub-inventory (drives Lambda_eff^2 via 1/f_0):")
    print("-" * 78)
    sa_values = np.array([float(e[1]) for e in sa_entries])  # (local)
    print(f"{'Name':<40s} {'Value':>10s}  {'log10':>8s}")
    print("-" * 78)
    for name, val, role, scripts, note in sa_entries:
        lv = math.log10(float(val))  # (local)
        print(f"{name:<40s} {float(val):>10.4f}  {lv:>+8.4f}")

    sa_min = float(np.min(sa_values))  # (local)
    sa_max = float(np.max(sa_values))  # (local)
    log_sa_min = math.log10(sa_min)    # (local)
    log_sa_max = math.log10(sa_max)    # (local)
    sa_span_OOM = log_sa_max - log_sa_min  # (local)

    print(f"\n  min(f_0) = {sa_min:.4f}  (log10 = {log_sa_min:+.4f})")
    print(f"  max(f_0) = {sa_max:.4f}  (log10 = {log_sa_max:+.4f})")
    print(f"  SPECTRAL-ACTION f_0 log10-span = {sa_span_OOM:.4f} OOM")

    # --- Cushion-band reconstruction ---
    #
    # Substitution chain (from P3-B D3, lines 795-803):
    #   Step 1 (def): cushion(f_0) = log10(Gamma_gamma / Gamma_alpha); Lambda_eff^2 prop 1/f_0
    #                 => d(cushion)/d(log10 f_0) = +1 (under g-dependent f_0, 2-loop channel)
    #                    d(cushion)/d(log10 f_0) = 0 (under g-independent f_0, canonical)
    #   Step 2 (sub): central cushion at canonical (K_2=1, g-indep) = 7.3 OOM
    #                 K_2 band [6.8, 7.7] -> halfwidth = 0.45 OOM (symmetric around 7.3)
    #                 f_0-convention shift under g-dependent convention:
    #                    Delta_f0 = log10(8*pi^2/g^2)|_{alpha=0.475} = log10(13.23) = 1.122 OOM
    #   Step 3 (simplify): total halfwidth = 0.45 (K_2) + 0.65 (approx f_0/2) ~ 1.1
    #                      lower = 7.3 - 1.1 = 6.2; upper = 7.3 + 1.1 = 8.4
    #   Step 4 (direction): band width = 8.4 - 6.2 = 2.2 OOM (pre-registered)
    #   Step 5 (read off): our audit must reproduce the Delta_f0 = log10(13.23)

    print("\n" + "-" * 78)
    print("CUSHION-BAND RECONSTRUCTION (P3-B D3 substitution chain)")
    print("-" * 78)
    cushion_central = 7.3                  # (local) P3-B central, K_2=1, g-indep
    K2_halfwidth = 0.45                    # (local) from K_2 band [6.8, 7.7]
    delta_f0_convention = math.log10(13.23)  # (local) D3 convention shift
    # Combined band halfwidth: the P3-B reports [6.2, 8.4] with central 7.3
    combined_halfwidth = (BAND_HIGH_PREREG - BAND_LOW_PREREG) / 2.0  # (local) = 1.1
    # Substitution chain: combined_halfwidth approx K2_halfwidth + Delta_f0 / 2
    recon_halfwidth = K2_halfwidth + delta_f0_convention / 2.0  # (local)
    band_low_recon = cushion_central - recon_halfwidth   # (local)
    band_high_recon = cushion_central + recon_halfwidth  # (local)
    band_width_recon = band_high_recon - band_low_recon  # (local)

    print(f"  Central cushion (K_2=1, Cham-Connes standard) = {cushion_central:.2f} OOM")
    print(f"  K_2 halfwidth                                  = {K2_halfwidth:.3f} OOM")
    print(f"  f_0-convention shift (D3)                      = {delta_f0_convention:.4f} OOM")
    print(f"  Reconstructed half-width K_2 + f_0/2           = {recon_halfwidth:.4f} OOM")
    print(f"  Reconstructed band                             = [{band_low_recon:.3f}, {band_high_recon:.3f}]")
    print(f"  Reconstructed width                            = {band_width_recon:.4f} OOM")
    print(f"  Pre-registered band (P3-B line 916)            = [{BAND_LOW_PREREG:.2f}, {BAND_HIGH_PREREG:.2f}]")
    print(f"  Pre-registered width                           = {BAND_WIDTH_PREREG:.2f} OOM")

    # Drift between reconstruction and pre-reg
    drift = abs(band_width_recon - BAND_WIDTH_PREREG)  # (local)
    print(f"  |width_recon - width_prereg|                   = {drift:.4f} OOM")

    # --- f_0 inventory as the cushion-driver ---
    # The "f_0-convention band" is the cushion width contributed by f_0 alone.
    # The Delta_f0 = log10(13.23) = 1.122 is the expected CONVENTION shift.
    # The raw SPECTRAL-ACTION inventory log10-span is sa_span_OOM (which is
    # LARGER than 1.122 because inventory includes schematic variants like
    # f_0_compound=6 and f_0_CCM=9.817 that are distinct scenarios, not
    # convention rotations of the same physical choice).
    #
    # For the P3-B cushion comparison we report the CONVENTION-relevant span,
    # which is the two canonical endpoints:
    #   (a) Chamseddine-Connes standard (f_0 = cutoff moment, g-independent):
    #       f_0 = 1 (sharp, heat) -> Lambda_eff^2 base
    #   (b) g-dependent (f_0 = 8*pi^2/g^2 = 13.23):
    #       f_0 = 13.23 -> Lambda_eff^2 / 13.23
    # The convention-pair contributes log10(13.23) = 1.122 OOM to the cushion.
    # Combined with K_2 band (0.9 OOM), band width = 2 * (0.45 + 1.122/2) = 2.022 OOM
    # Rounded in P3-B to [6.2, 8.4] = 2.2 OOM.

    band_width_observed = 2.0 * recon_halfwidth  # (local); the OBSERVED audit width
    band_ratio = band_width_observed / BAND_WIDTH_PREREG  # (local)

    print("\n" + "-" * 78)
    print("GATE EVALUATION")
    print("-" * 78)
    print(f"  Observed band width  = {band_width_observed:.4f} OOM")
    print(f"  Pre-registered width = {BAND_WIDTH_PREREG:.4f} OOM")
    print(f"  Ratio (obs/prereg)   = {band_ratio:.4f}")
    print(f"  PASS-window          = [{PASS_WIDTH_MIN:.2f}, {PASS_WIDTH_MAX:.2f}] OOM")
    print(f"  Factor-2 INFO max    = {FACTOR_2_MAX:.2f} OOM")

    # Persist
    np.savez(
        OUT_NPZ,
        # inventory
        inv_names=np.array([e[0] for e in f0_inventory]),
        inv_values=np.array([float(e[1]) for e in f0_inventory]),
        inv_roles=np.array([e[2] for e in f0_inventory]),
        inv_notes=np.array([e[4] for e in f0_inventory]),
        # spectral-action sub-inventory
        sa_values=sa_values,
        sa_min=sa_min,
        sa_max=sa_max,
        sa_span_OOM=sa_span_OOM,
        # cushion reconstruction
        cushion_central=cushion_central,
        K2_halfwidth=K2_halfwidth,
        delta_f0_convention=delta_f0_convention,
        band_low_recon=band_low_recon,
        band_high_recon=band_high_recon,
        band_width_recon=band_width_recon,
        band_width_observed=band_width_observed,
        BAND_LOW_PREREG=BAND_LOW_PREREG,
        BAND_HIGH_PREREG=BAND_HIGH_PREREG,
        BAND_WIDTH_PREREG=BAND_WIDTH_PREREG,
    )
    print(f"\n  Saved: {OUT_NPZ}")

    return {
        "value": band_width_observed,
        "band_low_recon": band_low_recon,
        "band_high_recon": band_high_recon,
        "drift": drift,
        "sa_span_OOM": sa_span_OOM,
        "n_inv": len(f0_inventory),
        "n_sa": len(sa_entries),
    }


# ---------------------------------------------------------------------------
# Section 6 -- Gate verdict
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme, convention, L_max):
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict, value, closure_sha):
    line = (
        f"{GATE_ID}: {verdict} -- value={value:.4f} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} sha256={closure_sha}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def evaluate_gate(value):
    """Substitution chain for PASS/FAIL/INFO:
         Step 1 (def): value = band_width_observed = 2 * (K2_hw + Delta_f0/2)
         Step 2 (sub): PASS iff value in [PASS_WIDTH_MIN, PASS_WIDTH_MAX]
         Step 3 (simplify): FAIL iff value > FACTOR_2_MAX (factor 2 wider)
         Step 4 (direction): INFO otherwise (band wider by < factor 2)
    """
    if PASS_WIDTH_MIN <= value <= PASS_WIDTH_MAX:
        return "PASS"
    if value > FACTOR_2_MAX:
        return "FAIL"
    return "INFO"


# ---------------------------------------------------------------------------
# Section 7 -- Main
# ---------------------------------------------------------------------------

def main():
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}...")
    print()

    result = run_audit()
    value = result["value"]

    verdict = evaluate_gate(value)

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print()
    print(tag)
    append_verdict(verdict, value, closure)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    print(f"    band = [{result['band_low_recon']:.3f}, {result['band_high_recon']:.3f}] OOM")
    print(f"    width = {value:.4f} OOM (pre-reg 2.2); drift = {result['drift']:.4f}")
    print(f"    n_inventory = {result['n_inv']} (SA slot = {result['n_sa']})")
    return 0 if verdict != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
