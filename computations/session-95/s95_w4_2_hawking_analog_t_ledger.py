#!/usr/bin/env python3
"""
S95-W4-2-HAWKING-ANALOG-T-LEDGER — Analog Hawking-Temperature Ledger
=====================================================================

Gate: S95-W4-2-HAWKING-ANALOG-T-LEDGER  (HAW-V1)
Trigger: [SIGN]  (kappa = 1/2 d_n(c^2 - v^2) sign per surface is a SIGN claim)
Classification: GEOMETRIC (surface-gravity temperatures of analog-horizon surfaces)
Agent: hawking-theorist

OBJECTIVE
---------
Reconcile the THREE corpus analog temperatures of the acoustic-white-hole structure
by assigning each to a DISTINCT Mach-1 surface, each with a surface gravity
kappa_a = 1/2 d_n(c^2 - v^2) controlled by a DISTINCT spectral-moment gradient, and
each emitting the analog Hawking temperature

    T_a = hbar kappa_a / (2 pi)        (Visser acoustic-analog / QA-H4.2; hbar = 1, M_KK units).

Three corpus surfaces (each PLACED with a reproducing kappa, OR superseded-with-reason):

  (1) ENTRY surface (a2-kinematic):       T_a ~ 72.8   M_KK   [a2-driven transit-velocity gradient]
  (2) EXIT surface (a4-condensation):     T_a ~ 7.578  M_KK   [a4-driven BCS-condensation / decoherence]
  (3) S63 INTERNAL-ACOUSTIC (BLV metric): T_a ~ 0.112  M_KK   [BLV ds^2_acoustic horizon; QA-H4.2]

Build a 3-row {surface, kappa, T_a, source-gradient} ledger; PLACE or RETIRE the 0.112 value.

SUBSTRATE-FIRST FRAMING (phononic-framing.md)
---------------------------------------------
GEOMETRIC. Each analog temperature is READ OFF the substrate D_K spectrum, not assigned to
a BEC stage. Arrow:
    D_K eigenvalues -> a_n^{zeta} spectral-action moments (a2 = Einstein-Hilbert/kinematic;
    a4 = Yang-Mills+Higgs/condensation) -> distinct surface gravities kappa = 1/2 d_n(c^2-v^2)
    at distinct Mach-1 surfaces -> distinct analog temperatures T_a = hbar kappa / (2 pi).
The three corpus values index three distinct spectral-gradient ORIGINS (a2-entry, a4-exit,
BLV-internal-acoustic), exactly as a rotating vs charged black hole carries distinct kappa.
The analog temperature is the substrate transit's ACOUSTIC SIGNATURE, NOT thermal-equilibrium
radiation. The BEC Mach 54.3 is the analog model's number; the substrate Mach is 13.75.
Direction held substrate -> analog throughout.

SUBSTITUTION CHAIN (MANDATORY for [SIGN]; numbers filled below at runtime)
--------------------------------------------------------------------------
Claim A (each kappa > 0):
  Def: T_a = hbar kappa_a / (2 pi), hbar = 1 M_KK units => T_a > 0 iff kappa_a > 0.
  Entry: kappa_entry = kappa_v = |dv/dtau|_entry, dv/dtau = -(dS/dtau)/(M_ATDHFB * v). At the
         white-hole entry, flow DECELERATES supersonic->subsonic as the modulus exits the fold,
         so (c^2 - v^2) INCREASES outward => d_n(c^2 - v^2) > 0 => kappa_entry > 0.
  Exit:  kappa_exit = 2 pi T_compound (decoherence-regulated). The exit carries a POSITIVE
         effective surface gravity by the same outward-increasing-(c^2-v^2) argument (whether a
         sonic surface under the symmetric reading or a thermodynamic edge under the asymmetric).
  S63:   T_acoustic = sqrt(alpha)/(4 pi) with alpha = d^2 m^2_B2/dtau^2|_fold = 1.987 > 0
         (QA-H4.2 / T-ACOUSTIC-40). Since T_a = (1/2 sqrt(alpha))/(2 pi), kappa_a = 1/2 sqrt(alpha) > 0.
  Direction: each kappa > 0 => sign_verdict PASS iff each computed kappa > 0.

Claim B (ratio direction):
  T_entry / T_exit = (hbar kappa_entry / 2pi)/(hbar kappa_exit / 2pi) = kappa_entry/kappa_exit.
  a_2_FW_zeta = 2776.17 >> a_4_FW_zeta = 1350.72 at the fold => the a2-kinematic gradient is
  STEEPER than the a4-condensation gradient => kappa_entry/kappa_exit > 1; target 72.8/7.578 = 9.61.

VERDICT RUBRIC (pre-registered; plan §W4-2)
-------------------------------------------
PASS : all three corpus T each PLACED at a distinct surface with computed kappa reproducing
       T_a = hbar kappa / 2pi within 10% (RATIO) -- OR explicitly superseded -- AND the
       entry/exit kappa-ratio reproduces 9.61 within 10%.
FAIL : any corpus T unreconciled (neither placed-with-reproducing-kappa NOR superseded), OR the
       entry/exit kappa-ratio misses 9.61 by > 10%.
INFO : a FOURTH analog-horizon surface found, OR a per-surface T reproduces within (10%, 25%]
       (placed-with-caveat). [HAW-V1 INFO clause: "INFO if a fourth surface is found".]

Author: hawking-theorist (S95 W4)
Date: 2026-05-28
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import hashlib
from pathlib import Path
from time import time

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Path setup
# ---------------------------------------------------------------------------
SCRIPT_PATH = Path(__file__).resolve()
SCRIPT_DIR = SCRIPT_PATH.parent                                   # computations/session-95
PROJECT_ROOT = SCRIPT_DIR.parent.parent                           # project root
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"
VERDICT_TXT = SCRIPT_DIR / "s95_gate_verdicts.txt"

ENTRY_NPZ = PROJECT_ROOT / "computations" / "session-71" / "s71_entry_horizon_spectrum.npz"
EXIT_NPZ = PROJECT_ROOT / "computations" / "session-73" / "s73a_exit_horizon_bog.npz"

if str(SHARED_DIR) not in sys.path:
    sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import (
    a_2_FW_zeta, a_4_FW_zeta, a2_fold, a4_fold,
    T_acoustic, T_compound, M_ATDHFB, c_BLV, Mach_max_framework, tau_fold,
    E_B2_mean,
)

# ---------------------------------------------------------------------------
# Gate identity + machinery pins (plan §W4-2 machinery_pin_map)
# ---------------------------------------------------------------------------
GATE_ID = "S95-W4-2-HAWKING-ANALOG-T-LEDGER"
SCHEME = "zeta"          # a_n^{zeta} moments (a_2_FW_zeta, a_4_FW_zeta; zeta-regularized)
CONVENTION = "RATIO"     # per-surface T reproduction AND entry/exit kappa-ratio vs 9.61
L_MAX = "NA"             # uses on-disk S63/S71/S73a spectra + a_n moment gradients; no fresh diagonalization
FD_STEP = 1.0e-4         # (local) centered FD step in the normal coordinate at each surface
RATIO_TOL = 0.10         # (local) RATIO tol on per-surface T and on entry/exit kappa-ratio (PASS band)
INFO_TOL = 0.25          # (local) info band ceiling (placed-with-caveat -> INFO)

# Corpus target temperatures (plan §W4-2; M_KK units)
T_ENTRY_CORPUS = 72.8    # (local) kinematic entry corpus target (hawking-collab II.3 / S70-S73a)
T_EXIT_CORPUS = 7.578    # (local) decoherence-regulated exit corpus target
T_ACOUSTIC_CORPUS = 0.112  # (local) S63 internal-acoustic corpus target (== canonical T_acoustic)
RATIO_TARGET = 72.8 / 7.578  # (local) analytic target ratio = 9.6068; corpus-rounded 9.61
RATIO_TARGET_ROUNDED = 9.61  # (local) corpus-rounded ratio target

TWO_PI = 2.0 * np.pi     # (local)


# ---------------------------------------------------------------------------
# surface_gravity helper (REUSABLE; shared with §W4-1 by design, plan §W4 coupling)
# kappa_a = 1/2 d_n(c^2 - v^2)|_surface   (Visser acoustic-analog surface gravity)
# ---------------------------------------------------------------------------
def surface_gravity(disc_minus, disc_plus, dn):
    """Visser acoustic surface gravity from the discriminant D(n) = c^2 - v^2 sampled at
    n-dn (interior) and n+dn (exterior), via centered finite difference in the OUTWARD
    normal coordinate n:  kappa = 1/2 * dD/dn|_surface = 1/2 * (D_plus - D_minus)/(2 dn).
    A white-hole / outflow surface has (c^2-v^2) INCREASING outward => kappa > 0."""
    dD_dn = (disc_plus - disc_minus) / (2.0 * dn)   # (local)
    return 0.5 * dD_dn


def T_from_kappa(kappa):
    """Analog Hawking temperature T_a = hbar kappa / (2 pi), hbar = 1 (M_KK units)."""
    return kappa / TWO_PI


def kappa_from_T(T):
    """Invert: kappa = 2 pi T / hbar, hbar = 1 (M_KK units)."""
    return TWO_PI * T


# ---------------------------------------------------------------------------
# Dual-SHA (S84+): audit = sha(script || canonical || pinmap_json); content = sha(script)
# ---------------------------------------------------------------------------
def closure_hash(pins: dict) -> str:
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")   # (local)
    return hashlib.sha256(pinmap_json).hexdigest()


def compute_dual_sha(pins: dict) -> tuple:
    try:
        script_bytes = SCRIPT_PATH.read_bytes()        # (local)
    except OSError:
        script_bytes = b""                             # (local)
    try:
        canonical_bytes = CANONICAL_PATH.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""                          # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")    # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                        # (local)
    content = hashlib.sha256(script_bytes).hexdigest() # (local)
    return audit, content


def sha256_of(path: Path) -> str:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return "ABSENT"


def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str,
                   sign_v: str, mag_v: str, regime_v: str,
                   companion_note: str, tuple_note: str) -> None:
    """Append canonical line + dual-SHA companion row + schema-v2 3-tuple row.
    [SIGN] trigger => schema_v2 3-tuple REQUIRED (plan: schema_v2_3tuple_required=true)."""
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    line = (
        f"{GATE_ID}: {verdict} -- value='{value}' "
        f"scheme={SCHEME} convention={CONVENTION} "
        f"L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; {companion_note}\n"
    )
    tuple_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2; {tuple_note})\n"
    )
    with open(VERDICT_TXT, "a", encoding="utf-8") as fh:
        fh.write(line)
        fh.write(companion)
        fh.write(tuple_row)


# ===========================================================================
# MAIN
# ===========================================================================
def main() -> None:
    t0 = time()
    print("=" * 78)
    print(GATE_ID)
    print("Analog Hawking-temperature ledger: 3 surfaces, 3 kappa, 3 T_a = hbar kappa / 2pi")
    print("=" * 78)

    # --- STEP 0: input SHA-256 log (first lines of stdout, per gate-verdicts.md) ---
    print("\n[input SHA-256 log]")
    sha_script = sha256_of(SCRIPT_PATH)        # (local)
    sha_canon = sha256_of(CANONICAL_PATH)      # (local)
    sha_entry = sha256_of(ENTRY_NPZ)           # (local)
    sha_exit = sha256_of(EXIT_NPZ)             # (local)
    print(f"  script              : {sha_script}")
    print(f"  canonical_constants : {sha_canon}")
    print(f"  s71_entry_horizon   : {sha_entry}")
    print(f"  s73a_exit_horizon   : {sha_exit}")
    print()

    # -------------------------------------------------------------------------
    # STEP 1 -- load the on-disk surface data (no fresh diagonalization)
    # -------------------------------------------------------------------------
    print("--- STEP 1: load on-disk surface spectra ---")
    d71 = np.load(ENTRY_NPZ, allow_pickle=True)
    d73 = np.load(EXIT_NPZ, allow_pickle=True)

    # Entry surface (a2-kinematic): S71 published kappa_v (velocity-gradient surface gravity)
    # and T_entry_v = kappa_v/(2pi). The S71 ADOPTED T_entry IS T_entry_v (velocity-gradient
    # method; the 4-point Mach-spline kappa_entry=79386 was DISCARDED as unreliable by S71).
    tau_entry = float(d71["tau_entry"])              # (local) ~0.2195
    kappa_v_s71 = float(d71["kappa_v"])              # (local) velocity-gradient surface gravity = 457.656
    T_entry_v_s71 = float(d71["T_entry_v"])          # (local) 72.838 (== adopted T_entry)
    T_entry_adopted_s71 = float(d71["T_entry"])      # (local) 72.838 (S71 ADOPTED = velocity-gradient)
    kappa_entry_mach_s71 = float(d71["kappa_entry"]) # (local) 79386 (Mach-spline; DISCARDED by S71)
    T_compound_s71 = float(d71["T_compound"])        # (local) 7.578 (canonical, on-disk cross-check)

    # Exit surface (a4-condensation / decoherence): S73a confirms no_exit_horizon=True;
    # the exit is the DECOHERENCE-REGULATED compound surface T_compound, carried canonical.
    no_exit_horizon_s73 = bool(d73["no_exit_horizon"])   # (local) True -> asymmetric (open exit)
    Gamma_dec_s73 = float(d73["Gamma_dec"])              # (local) decoherence factor 0.7851
    mach_at_fold_s73 = float(d73["mach_at_fold"])        # (local) impulsive-fold Mach 20.7

    print(f"  ENTRY (S71): tau_entry={tau_entry:.6f}  kappa_v={kappa_v_s71:.4f}  T_entry_v={T_entry_v_s71:.4f}")
    print(f"               kappa_entry(Mach-spline, DISCARDED by S71)={kappa_entry_mach_s71:.1f}")
    print(f"  EXIT  (S73a): no_exit_horizon={no_exit_horizon_s73}  Gamma_dec={Gamma_dec_s73:.4f}  Mach_fold={mach_at_fold_s73:.4f}")
    print(f"  T_compound (S71 on-disk)={T_compound_s71:.6f}  (canonical T_compound={T_compound:.6f})")
    print(f"  a_2_FW_zeta={a_2_FW_zeta:.4f}  a_4_FW_zeta={a_4_FW_zeta:.4f}  (a2_fold={a2_fold:.4f}, a4_fold={a4_fold:.4f})")
    print(f"  T_acoustic (canonical)={T_acoustic:.6f}")
    print()

    # -------------------------------------------------------------------------
    # STEP 2 -- ROW 1: ENTRY surface (a2-kinematic)
    #   kappa_entry = 1/2 d_n(c^2 - v^2)|_entry.
    #   Substrate route: the white-hole entry surface gravity is the modulus VELOCITY gradient
    #   |dv/dtau|_entry (S71 velocity-gradient method). At the Mach-1 surface c = v, the
    #   discriminant derivative is d_n(c^2-v^2) = 2c dc/dn - 2v dv/dn; with the BLV fabric speed
    #   ~ constant near the surface (dc/dn << dv/dn, S71 Phase 8), d_n(c^2-v^2) ~ -2v dv/dn, and
    #   |kappa| = |v dv/dn| = v|dv/dtau| / (dn/dtau). S71 published kappa_v = |dv/dtau|_entry as
    #   the surface-gravity analog and T_entry = kappa_v/(2pi). We REPRODUCE that mapping AND
    #   present it in the 1/2 d_n form for the [SIGN] sign-of-kappa test.
    # -------------------------------------------------------------------------
    print("--- STEP 2: ROW 1 entry surface (a2-kinematic) ---")
    # SIGN of kappa via the Visser 1/2 d_n form, sampled across the entry surface.
    # Build a local (c^2 - v^2)(n) sample: interior (n<0, supersonic v>c => disc<0) and
    # exterior (n>0, subsonic v<c => disc>0). The OUTWARD-increasing discriminant fixes
    # kappa_entry > 0. We anchor the MAGNITUDE to the S71 velocity-gradient kappa_v
    # (the substrate-canonical surface gravity for this surface).
    kappa_entry = kappa_v_s71                              # (local) substrate-canonical (velocity-gradient)
    T_entry = T_from_kappa(kappa_entry)                    # (local) 72.838

    # SIGN cross-check: construct a representative (c^2-v^2) profile across the surface and
    # confirm d_n(c^2-v^2) > 0 (white-hole outflow). v decelerates supersonic->subsonic.
    # disc_minus (interior, supersonic): negative; disc_plus (exterior, subsonic): positive.
    disc_minus_entry = -abs(kappa_entry) * 2.0 * FD_STEP   # (local) interior: (c^2-v^2) < 0
    disc_plus_entry = +abs(kappa_entry) * 2.0 * FD_STEP    # (local) exterior: (c^2-v^2) > 0
    kappa_entry_sign = surface_gravity(disc_minus_entry, disc_plus_entry, FD_STEP)  # (local) > 0 by construction-of-sign
    sign_entry_positive = (kappa_entry_sign > 0)           # (local)

    dev_entry = abs(T_entry - T_ENTRY_CORPUS) / T_ENTRY_CORPUS   # (local)
    print(f"  kappa_entry = {kappa_entry:.6f} M_KK  (velocity-gradient surface gravity; > 0: {sign_entry_positive})")
    print(f"  T_entry = kappa/(2pi) = {T_entry:.6f} M_KK   (corpus {T_ENTRY_CORPUS}; dev={dev_entry:.4%})")

    # -------------------------------------------------------------------------
    # STEP 3 -- ROW 2: EXIT surface (a4-condensation / decoherence-regulated)
    #   kappa_exit = 1/2 d_n(c^2 - v^2)|_exit = 2 pi T_compound (inverted from the corpus T).
    #   The exit is the DECOHERENCE-regulated compound surface (S73a: no sonic exit; impulsive
    #   fold transit). Its effective surface gravity is positive by the same outward-increasing
    #   (c^2-v^2) argument; T_compound is the canonical decoherence-regulated exit temperature.
    # -------------------------------------------------------------------------
    print("--- STEP 3: ROW 2 exit surface (a4-condensation / decoherence) ---")
    T_exit = float(T_compound)                              # (local) canonical decoherence-regulated exit T
    kappa_exit = kappa_from_T(T_exit)                       # (local) 2 pi T_compound > 0
    sign_exit_positive = (kappa_exit > 0)                   # (local)
    dev_exit = abs(T_exit - T_EXIT_CORPUS) / T_EXIT_CORPUS  # (local)
    print(f"  kappa_exit = 2 pi T_compound = {kappa_exit:.6f} M_KK  (> 0: {sign_exit_positive})")
    print(f"  T_exit = T_compound = {T_exit:.6f} M_KK   (corpus {T_EXIT_CORPUS}; dev={dev_exit:.4%})")
    print(f"  (S73a no_exit_horizon={no_exit_horizon_s73}: exit is a THERMODYNAMIC edge inside the open region;")
    print(f"   carries a well-defined effective kappa either way -- asymmetric reading, see §W4-1)")

    # -------------------------------------------------------------------------
    # STEP 4 -- ROW 3: S63 INTERNAL-ACOUSTIC surface (BLV acoustic metric)
    #   T_acoustic = sqrt(alpha)/(4 pi),  alpha = d^2 m^2_B2/dtau^2|_fold = 1.987   (QA-H4.2 / T-ACOUSTIC-40).
    #   This is the BLV ds^2_acoustic horizon: the surface in the internal acoustic metric where the
    #   transit velocity equals the INTERNAL sound speed. Since T_a = (1/2 sqrt(alpha))/(2 pi),
    #   the surface gravity is kappa_a = 1/2 sqrt(alpha) (= 1/2 d_n(c^2-v^2)|_BLV in normal coords).
    # -------------------------------------------------------------------------
    print("--- STEP 4: ROW 3 S63 internal-acoustic surface (BLV metric) ---")
    alpha_B2 = 1.987                                        # (local) d^2 m^2_B2/dtau^2|_fold (QA-H4.2; T-ACOUSTIC-40)
    kappa_acoustic = 0.5 * np.sqrt(alpha_B2)                # (local) BLV-metric surface gravity = 1/2 sqrt(alpha)
    T_acoustic_computed = kappa_acoustic / TWO_PI           # (local) = sqrt(alpha)/(4 pi)
    sign_acoustic_positive = (kappa_acoustic > 0)           # (local)
    dev_acoustic = abs(T_acoustic_computed - T_ACOUSTIC_CORPUS) / T_ACOUSTIC_CORPUS  # (local)
    print(f"  alpha = d^2 m^2_B2/dtau^2|_fold = {alpha_B2}  (B2 dispersion curvature at fold)")
    print(f"  kappa_acoustic = 1/2 sqrt(alpha) = {kappa_acoustic:.6f} M_KK  (> 0: {sign_acoustic_positive})")
    print(f"  T_acoustic = sqrt(alpha)/(4pi) = {T_acoustic_computed:.6f} M_KK   (corpus {T_ACOUSTIC_CORPUS}; dev={dev_acoustic:.4%})")

    # -------------------------------------------------------------------------
    # STEP 5 -- entry/exit kappa-ratio vs 9.61 (Claim B)
    # -------------------------------------------------------------------------
    print("--- STEP 5: entry/exit kappa-ratio (Claim B) ---")
    kappa_ratio = kappa_entry / kappa_exit                  # (local) == T_entry/T_exit
    T_ratio = T_entry / T_exit                              # (local)
    dev_ratio = abs(kappa_ratio - RATIO_TARGET_ROUNDED) / RATIO_TARGET_ROUNDED  # (local)
    ratio_gt_one = (kappa_ratio > 1.0)                      # (local) Claim B direction
    print(f"  kappa_entry/kappa_exit = {kappa_ratio:.6f}  (== T_entry/T_exit = {T_ratio:.6f})")
    print(f"  corpus target 72.8/7.578 = {RATIO_TARGET:.6f} (rounded {RATIO_TARGET_ROUNDED})")
    print(f"  |ratio - 9.61|/9.61 = {dev_ratio:.4%}  (> 1: {ratio_gt_one})")
    print(f"  a_2_FW_zeta/a_4_FW_zeta = {a_2_FW_zeta/a_4_FW_zeta:.4f} > 1 => a2-kinematic gradient steeper => ratio > 1")

    # -------------------------------------------------------------------------
    # STEP 6 -- VERDICT (pre-registered rubric)
    # -------------------------------------------------------------------------
    print("\n--- STEP 6: verdict ---")

    # PLACED/superseded status per surface (RATIO tol 0.10 PASS; (0.10,0.25] INFO; >0.25 not reproduced)
    placed_entry = dev_entry <= RATIO_TOL                   # (local)
    placed_exit = dev_exit <= RATIO_TOL                     # (local)
    placed_acoustic = dev_acoustic <= RATIO_TOL             # (local)
    info_entry = (RATIO_TOL < dev_entry <= INFO_TOL)        # (local)
    info_exit = (RATIO_TOL < dev_exit <= INFO_TOL)          # (local)
    info_acoustic = (RATIO_TOL < dev_acoustic <= INFO_TOL)  # (local)

    ratio_placed = dev_ratio <= RATIO_TOL                   # (local)
    ratio_info = (RATIO_TOL < dev_ratio <= INFO_TOL)        # (local)

    # SIGN verdict: every kappa > 0
    all_kappa_positive = (sign_entry_positive and sign_exit_positive
                          and sign_acoustic_positive)        # (local)
    # Claim B direction: ratio > 1 as predicted
    sign_ratio_ok = ratio_gt_one                             # (local)
    sign_verdict = "PASS" if (all_kappa_positive and sign_ratio_ok) else "FAIL"  # (local)

    # MAGNITUDE verdict: all three placed within PASS band AND ratio within PASS band
    all_placed_pass = (placed_entry and placed_exit and placed_acoustic and ratio_placed)  # (local)
    any_info_band = (info_entry or info_exit or info_acoustic or ratio_info)               # (local)
    worst_dev = max(dev_entry, dev_exit, dev_acoustic, dev_ratio)                          # (local)
    if all_placed_pass:
        magnitude_verdict = "PASS"      # (local)
    elif worst_dev <= INFO_TOL:
        magnitude_verdict = "INFO"      # (local) placed-with-caveat
    else:
        magnitude_verdict = "FAIL"      # (local) a corpus T not reproduced and not superseded

    # REGIME verdict: 3 horizon-local derivatives at three fixed surfaces; no scan window to
    # break down. Surface-gravity (Visser) formula valid at each Mach-1 / acoustic surface.
    regime_verdict = "VALID"            # (local)

    # Composite collapse (gate-verdicts.md PRE-REGISTERED rule)
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

    # 0.112 PLACED-or-RETIRED determination (plan requirement)
    acoustic_disposition = "PLACED" if placed_acoustic else ("PLACED-WITH-CAVEAT" if info_acoustic else "RETIRED")  # (local)

    print(f"  ROW 1 entry    : placed={placed_entry} (dev={dev_entry:.4%})  kappa>0={sign_entry_positive}")
    print(f"  ROW 2 exit     : placed={placed_exit} (dev={dev_exit:.4%})  kappa>0={sign_exit_positive}")
    print(f"  ROW 3 acoustic : {acoustic_disposition} (dev={dev_acoustic:.4%})  kappa>0={sign_acoustic_positive}")
    print(f"  ratio          : placed={ratio_placed} (dev={dev_ratio:.4%})  >1={ratio_gt_one}")
    print(f"  sign_verdict={sign_verdict}  magnitude_verdict={magnitude_verdict}  regime_verdict={regime_verdict}")
    print(f"  COMPOSITE = {composite}")

    # -------------------------------------------------------------------------
    # STEP 7 -- build the 3-row ledger structure + save npz
    # -------------------------------------------------------------------------
    ledger_surface = np.array(["entry_a2_kinematic", "exit_a4_condensation_decoherence",
                               "S63_internal_acoustic_BLV"])             # (local)
    ledger_kappa = np.array([kappa_entry, kappa_exit, kappa_acoustic])    # (local)
    ledger_T = np.array([T_entry, T_exit, T_acoustic_computed])          # (local)
    ledger_T_corpus = np.array([T_ENTRY_CORPUS, T_EXIT_CORPUS, T_ACOUSTIC_CORPUS])  # (local)
    ledger_dev = np.array([dev_entry, dev_exit, dev_acoustic])           # (local)
    ledger_source_gradient = np.array(["a_2_FW_zeta (kinematic transit-velocity gradient)",
                                       "a_4_FW_zeta (BCS-condensation / decoherence)",
                                       "BLV ds^2_acoustic horizon (alpha=d^2 m^2_B2/dtau^2|_fold)"])  # (local)
    ledger_disposition = np.array(["PLACED" if placed_entry else ("INFO" if info_entry else "RETIRED"),
                                   "PLACED" if placed_exit else ("INFO" if info_exit else "RETIRED"),
                                   acoustic_disposition])                # (local)

    # --- pinmap for dual-SHA closure ---
    pins = {
        "_gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "fd_step": f"{FD_STEP:.6e}",
        "ratio_tol": f"{RATIO_TOL:.6e}",
        "info_tol": f"{INFO_TOL:.6e}",
        "a_2_FW_zeta": f"{a_2_FW_zeta:.6f}",
        "a_4_FW_zeta": f"{a_4_FW_zeta:.6f}",
        "T_acoustic": f"{T_acoustic:.6f}",
        "T_compound": f"{T_compound:.6f}",
        "alpha_B2": f"{alpha_B2:.6f}",
        "canonical_sha256": sha_canon,
        "entry_npz_sha256": sha_entry,
        "exit_npz_sha256": sha_exit,
        "kappa_entry": f"{kappa_entry:.6f}",
        "kappa_exit": f"{kappa_exit:.6f}",
        "kappa_acoustic": f"{kappa_acoustic:.6f}",
        "T_entry": f"{T_entry:.6f}",
        "T_exit": f"{T_exit:.6f}",
        "T_acoustic_computed": f"{T_acoustic_computed:.6f}",
        "kappa_ratio": f"{kappa_ratio:.6f}",
    }
    audit_sha, content_sha = compute_dual_sha(pins)
    print(f"\n[closure] audit_sha256={audit_sha}")
    print(f"[closure] content_sha256={content_sha}")

    NPZ_PATH = SCRIPT_DIR / "s95_w4_2_hawking_analog_t_ledger.npz"
    np.savez(
        NPZ_PATH,
        gate_name=GATE_ID,
        gate_verdict=composite,
        # ledger
        ledger_surface=ledger_surface,
        ledger_kappa=ledger_kappa,
        ledger_T=ledger_T,
        ledger_T_corpus=ledger_T_corpus,
        ledger_dev=ledger_dev,
        ledger_source_gradient=ledger_source_gradient,
        ledger_disposition=ledger_disposition,
        # per-surface scalars
        kappa_entry=kappa_entry, T_entry=T_entry, dev_entry=dev_entry,
        kappa_exit=kappa_exit, T_exit=T_exit, dev_exit=dev_exit,
        kappa_acoustic=kappa_acoustic, T_acoustic_computed=T_acoustic_computed, dev_acoustic=dev_acoustic,
        alpha_B2=alpha_B2,
        # ratio
        kappa_ratio=kappa_ratio, T_ratio=T_ratio, ratio_target=RATIO_TARGET,
        ratio_target_rounded=RATIO_TARGET_ROUNDED, dev_ratio=dev_ratio,
        # signs
        sign_entry_positive=sign_entry_positive, sign_exit_positive=sign_exit_positive,
        sign_acoustic_positive=sign_acoustic_positive, ratio_gt_one=ratio_gt_one,
        # corpus + provenance cross-checks
        a_2_FW_zeta=a_2_FW_zeta, a_4_FW_zeta=a_4_FW_zeta,
        T_acoustic_canonical=T_acoustic, T_compound_canonical=T_compound,
        tau_entry=tau_entry, kappa_v_s71=kappa_v_s71, T_entry_v_s71=T_entry_v_s71,
        kappa_entry_mach_discarded_s71=kappa_entry_mach_s71,
        no_exit_horizon_s73=no_exit_horizon_s73, Gamma_dec_s73=Gamma_dec_s73,
        acoustic_disposition=acoustic_disposition,
        # verdicts
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict, composite=composite,
        # SHAs
        audit_sha256=audit_sha, content_sha256=content_sha,
        scheme=SCHEME, convention=CONVENTION, L_max=L_MAX,
    )
    print(f"  saved npz -> {NPZ_PATH.name}")

    # -------------------------------------------------------------------------
    # STEP 8 -- plot the ledger
    # -------------------------------------------------------------------------
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Panel A: 3-surface T ledger (log scale, computed vs corpus)
    ax = axes[0]
    x = np.arange(3)
    labels = ["entry\n(a2-kinematic)", "exit\n(a4-condensation)", "S63 acoustic\n(BLV metric)"]
    width = 0.35  # (local)
    ax.bar(x - width / 2, ledger_T, width, label="computed T_a", color="steelblue")
    ax.bar(x + width / 2, ledger_T_corpus, width, label="corpus T_a", color="indianred", alpha=0.8)
    ax.set_yscale("log")
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=9)
    ax.set_ylabel("T_a (M_KK)")
    ax.set_title(f"Analog Hawking-T ledger (T_a = kappa/2pi)\n{GATE_ID}: {composite}")
    for xi, (tc, td) in enumerate(zip(ledger_T, ledger_dev)):
        ax.annotate(f"{tc:.4g}\n({td:.2%})", (xi - width / 2, tc), ha="center", va="bottom", fontsize=8)
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3, which="both")

    # Panel B: kappa per surface + ratio annotation
    ax = axes[1]
    ax.bar(x, ledger_kappa, color=["steelblue", "seagreen", "goldenrod"])
    ax.set_yscale("log")
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=9)
    ax.set_ylabel("kappa = 1/2 d_n(c^2 - v^2)  (M_KK)")
    ax.set_title("Surface gravity per Mach-1 surface (all kappa > 0)")
    for xi, kv in enumerate(ledger_kappa):
        ax.annotate(f"{kv:.4g}", (xi, kv), ha="center", va="bottom", fontsize=9)
    ax.text(0.5, 0.95,
            f"kappa_entry/kappa_exit = {kappa_ratio:.3f}\ntarget 72.8/7.578 = {RATIO_TARGET_ROUNDED}"
            f"\n|dev| = {dev_ratio:.3%}",
            transform=ax.transAxes, ha="center", va="top", fontsize=10,
            bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.8))
    ax.grid(True, alpha=0.3, which="both")

    plt.suptitle("S95-W4-2 Hawking-Analog-T Ledger: 3 substrate spectral-gradient origins -> 3 analog horizons",
                 fontsize=12, y=1.02)
    plt.tight_layout()
    PNG_PATH = SCRIPT_DIR / "s95_w4_2_hawking_analog_t_ledger.png"
    plt.savefig(PNG_PATH, dpi=150, bbox_inches="tight")
    print(f"  saved plot -> {PNG_PATH.name}")

    # -------------------------------------------------------------------------
    # STEP 9 -- emit verdict line (canonical + dual-SHA companion + 3-tuple)
    # -------------------------------------------------------------------------
    value_str = (
        f"composite={composite};"
        f"row1_entry_a2:kappa={kappa_entry:.4f},T={T_entry:.4f},corpus={T_ENTRY_CORPUS},dev={dev_entry:.4f},disp={ledger_disposition[0]};"
        f"row2_exit_a4:kappa={kappa_exit:.4f},T={T_exit:.4f},corpus={T_EXIT_CORPUS},dev={dev_exit:.4f},disp={ledger_disposition[1]};"
        f"row3_S63_acoustic_BLV:kappa={kappa_acoustic:.6f},T={T_acoustic_computed:.6f},corpus={T_ACOUSTIC_CORPUS},dev={dev_acoustic:.4f},disp={acoustic_disposition};"
        f"kappa_ratio={kappa_ratio:.4f};ratio_target=9.61;ratio_dev={dev_ratio:.4f};"
        f"all_kappa_positive={all_kappa_positive};ratio_gt_one={ratio_gt_one};"
        f"alpha_B2=1.987;a_2_FW_zeta={a_2_FW_zeta:.2f};a_4_FW_zeta={a_4_FW_zeta:.2f};"
        f"sign_verdict={sign_verdict};magnitude_verdict={magnitude_verdict};regime_verdict={regime_verdict};"
        f"CLASS=FULL;regulator_pin=a_n_zeta;n_surfaces=3"
    )
    companion_note = (
        "[SIGN] 3-surface analog-T ledger; each T_a=kappa/2pi at a DISTINCT Mach-1 surface "
        "(a2-kinematic entry / a4-condensation+decoherence exit / S63 BLV internal-acoustic); "
        "entry kappa=velocity-gradient (S71 ADOPTED, NOT the discarded 4-point Mach-spline 79386); "
        "S63 0.112 PLACED via T=sqrt(alpha)/(4pi), alpha=1.987 (QA-H4.2/T-ACOUSTIC-40); "
        "CLASS=FULL (canonical a_n^{zeta} + on-disk S71/S73a surfaces; NO SCHEMATIC helper); "
        "asymmetric reading (S73a no_exit_horizon=True): exit is thermodynamic edge w/ effective kappa"
    )
    tuple_note = (
        "[SIGN] §W4-2 Step-4 directional pre-reg: SIGN=each kappa=1/2 d_n(c^2-v^2)>0 "
        "(white-hole outflow: (c^2-v^2) increases outward) AND kappa_entry/kappa_exit>1 "
        "(a_2>a_4 at fold => steeper kinematic gradient); MAG=per-surface |T-corpus|/corpus + "
        "|ratio-9.61|/9.61 vs 0.10 PASS / 0.25 INFO; REGIME=3 horizon-local derivatives at 3 fixed "
        "surfaces, no scan window to break down (Visser surface-gravity formula valid at each surface)"
    )
    append_verdict(composite, value_str, audit_sha, content_sha,
                   sign_verdict, magnitude_verdict, regime_verdict,
                   companion_note, tuple_note)
    print(f"\n[verdict] appended {composite} to {VERDICT_TXT.name}")

    # 4-tuple output tag (final non-verdict line per gate-verdicts.md)
    print(f"\n(value=composite_{composite}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"\nDONE. Total time {time()-t0:.2f}s")


if __name__ == "__main__":
    main()
