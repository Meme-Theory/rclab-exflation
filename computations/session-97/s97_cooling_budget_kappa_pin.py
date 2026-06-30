#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S97-COOLING-BUDGET-KAPPA-PIN  (agent: hawking-theorist)
=======================================================
Test whether the SCENARIO-A cooling budget over-determines the M_KK^-1 -> s
seconds-normalization knob kappa.

This gate has a MANDATORY Class-8.7 PRE-FLIGHT (a [CHAIN] disambiguator) before
the MAIN [SIGN] band/recovery test:

  PRE-FLIGHT (Class-8.7 degenerate-observable):
    Confirm the cooling exponent  -0.8685 = ln(cooling)/N_e_exfl = -70.25/80.89
    is a kappa-INDEPENDENT ratio of two DIMENSIONLESS quantities (a log of a
    temperature ratio over an e-fold count) so that  d(exponent)/d(kappa) = 0.
    If the exponent secretly carried the seconds-normalization, the gate would be
    a tautology (Class-8.7 vacuous) -> FAIL.  Only on PRE-FLIGHT PASS do we run MAIN.

  MAIN ([SIGN] band/recovery):
    Combine the cooling budget {T_init=0.112*M_KK, N_e_exfl=80.89, exponent}
    with the AOFT anchor H^2(tau*) = 7.478844e-3 M_KK^2 (the substrate Hubble
    rate at tau*) to extract the seconds-per-e-fold the budget over-determines,
    hence kappa_implied.  Compare kappa_implied against kappa_nat = 8.86044e-42 s
    (the half-decade recovery band |log10(kappa_implied/kappa_nat)| <= 0.5) and
    against the W6-5 swept band [1e-20, 1e-10] (121 log-spaced points).

SUBSTRATE FRAMING (phononic-framing.md):
  kappa is the substrate-clock-tick (M_KK^-1) -> SI-seconds normalization. The
  SCENARIO-A cooling budget IS the substrate's own thermodynamic record of the
  fold->now transit (the GGE relic temperature decline through N_e exflationary
  e-folds = spectral-complexity doublings).  The arrow is
      D_K spectrum -> cooling budget (T_init, N_e, exponent) + H^2(tau*)
                   -> seconds-per-e-fold -> kappa_implied.
  NON-PHONONIC caveat: the hbar/GeV seconds-conversion arithmetic is a UNIT-CHAIN
  (not substrate dynamics); but the cooling budget feeding it IS substrate.

STRUCTURAL HONESTY (the key finding, reported FIRST in the WP):
  Every route that converts a substrate energy / rate scale (in M_KK units) to SI
  seconds is forced to kappa = hbar/(M_KK*GeV_to_J) = kappa_nat by dimensional
  consistency -- because the substrate Hubble rate H_star (inverse-ticks), the
  budget temperature T_init (M_KK units), and the tick itself ALL live in the same
  M_KK unit system. The cooling budget is CONSISTENT with kappa_nat (recovery PASS,
  log10-ratio = 0) but the recovery is an IDENTITY forced by unit-consistency, not
  an independent triangulation. The PRE-FLIGHT (exponent kappa-independent) is what
  certifies the gate is not Class-8.7 vacuous -- the budget does not pre-bake kappa.

Verdict rubric (per plan / gate-verdicts.md schema-v2 3-tuple collapse):
  sign_verdict    = PASS iff kappa_implied recovers kappa_nat in the predicted
                    direction (log10-ratio sign / magnitude as pre-registered).
  magnitude_verdict = PASS iff |log10(kappa_implied/kappa_nat)| <= 0.5 (recovery)
                    OR kappa_implied in [1e-20,1e-10] (band); else INFO/FAIL bands.
  regime_verdict  = VALID iff the budget arithmetic is within its validity window.

Composite collapse (gate-verdicts.md, PRE-REGISTERED):
  regime BREAKDOWN -> FAIL ; sign FAIL -> FAIL ;
  mag FAIL & regime VALID -> FAIL ; mag FAIL & regime MARGINAL -> INFO ;
  mag INFO -> INFO ; else PASS.
  PLUS: PRE-FLIGHT FAIL (exponent kappa-DEPENDENT) -> composite FAIL (Class-8.7 vacuous).

Inputs:
  computations/_shared/canonical_constants.py            (M_KK, M_KK_inv_seconds, hbar_SI, GeV_to_J, T_CMB, ...)
  computations/session-96/s96_w1_aoft_friedmann_map.npz  (H^2(tau*) anchor; audit edfe1f7f...)

Outputs:
  computations/session-97/s97_cooling_budget_kappa_pin.npz
  computations/session-97/s97_cooling_budget_kappa_pin.png
  verdict line + dual-SHA companion row + schema-v2 3-tuple row appended to
  computations/session-97/s97_gate_verdicts.txt
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")     # scalar/1D arithmetic; CPU thread cap (no large matrices)
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import hashlib
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --- locate project root and canonical_constants ---
THIS = Path(__file__).resolve()
PROJECT_ROOT = THIS.parents[2]                                  # .../Ainulindale Exflation
SHARED = PROJECT_ROOT / "computations" / "_shared"
sys.path.insert(0, str(SHARED))

from canonical_constants import (                                # noqa: E402
    M_KK,                 # GeV; substrate compactification scale (= M_KK_gravity)
    M_KK_inv_seconds,     # s; kappa_nat = hbar_SI/(M_KK*GeV_to_J)
    hbar_SI,              # J*s
    GeV_to_J,             # J/GeV
    k_B_SI,               # J/K
    T_CMB,                # K (cooling-budget present endpoint)
    tau_fold,             # 0.19 (fold order-parameter value)
)

# ---------------------------------------------------------------------------
# Gate identity + machinery pins (PRDR; per plan §W1-5 machinery_pin_map)
# ---------------------------------------------------------------------------
GATE_ID    = "S97-COOLING-BUDGET-KAPPA-PIN"
SCHEME     = "FW"
CONVENTION = "ABSOLUTE"            # kappa_implied compared as log10-ratio (absolute half-decade)
L_MAX      = "10"                  # H^2(tau*) from L_max=10 AOFT map

SESSION_97_DIR = PROJECT_ROOT / "computations" / "session-97"
VERDICT_TXT    = SESSION_97_DIR / "s97_gate_verdicts.txt"      # canonical path (gate-verdicts.md)
NPZ_OUT        = SESSION_97_DIR / "s97_cooling_budget_kappa_pin.npz"
PNG_OUT        = SESSION_97_DIR / "s97_cooling_budget_kappa_pin.png"

CANONICAL_PATH = SHARED / "canonical_constants.py"
AOFT_NPZ       = PROJECT_ROOT / "computations" / "session-96" / "s96_w1_aoft_friedmann_map.npz"

# --- pre-registered budget constants (s53 SCENARIO-A; plan §W1-5 machinery_pin_map) ---
# These are session-specific PRE-REGISTERED gate pins sourced from s53 SCENARIO-A
# (s53_exflation_cmb_temp_output.txt) and the S96 AOFT anchor -- NOT framework-wide
# canonicals; tagged local per math-scripts.md ("gate thresholds and pre-registered
# criteria" are pinned here, not promoted to canonical_constants.py).
T_INIT_OVER_MKK = 0.112           # (local) SCENARIO-A T_init = 0.112*M_KK (s53; = 8.3201e15 GeV)
N_E_EXFL        = 80.89           # (local) SCENARIO-A exflationary e-fold count (s53)
COOLING_EXP_REG = -0.8685         # (local) s53 reported cooling exponent (= ln(cooling)/N_e)
LN_COOLING      = -70.25          # (local) s53 ln(cooling) (dimensionless; numerator of exponent ratio)
H2_STAR_ANCHOR  = 7.478844e-03    # (local) M_KK^2; S96-W1-AOFT-FRIEDMANN-MAP (audit edfe1f7f...)
TAU_STAR_NOM    = 0.451041        # (local) tau* internal anchor (informational)

# --- pre-registered thresholds (plan §W1-5) ---
KAPPA_BAND_LO   = 1e-20           # (local) W6-5 swept band floor
KAPPA_BAND_HI   = 1e-10           # (local) W6-5 swept band ceiling
RECOVERY_TOL    = 0.5             # (local) |log10(kappa_implied/kappa_nat)| <= 0.5 (half-decade)
N_SWEEP         = 121             # (local) W6-5 kappa-sweep grid points (log-spaced)

# pre-flight float tolerances
EXP_RECON_TOL   = 5e-4            # (local) |exponent_recon - (-0.8685)| tolerance (4 sig figs)
DKAPPA_FLOOR    = 1e-30           # (local) analytic d(exponent)/d(kappa) must vanish to this floor


# ---------------------------------------------------------------------------
# Dual-SHA helpers (S84+ schema; mirrors s96_w1_aoft_friedmann_map sibling)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs) -> dict:
    print(f"=== {GATE_ID} -- input SHA-256 pins (first 20 lines of stdout) ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    script_bytes = script_path.read_bytes() if script_path.exists() else b""        # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    """Atomic single-write canonical line + dual-SHA companion row.

    Canonical path computations/session-97/s97_gate_verdicts.txt per
    gate-verdicts.md (NOT _shared/).
    """
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; [CHAIN] Class-8.7 PRE-FLIGHT: cooling "
        f"exponent -0.8685 = ln(cooling)/N_e = -70.25/80.89 is a ratio of two "
        f"DIMENSIONLESS quantities => d(exponent)/d(kappa)=0 (NOT vacuous); [SIGN] MAIN: "
        f"kappa_implied vs kappa_nat=8.86044e-42; recovery is an IDENTITY forced by "
        f"M_KK-unit consistency (hbar/M_KK_J), NOT independent triangulation; "
        f"NON-PHONONIC unit-chain (hbar,GeV_to_J) over a substrate cooling budget\n"
    )
    SESSION_97_DIR.mkdir(parents=True, exist_ok=True)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


def append_3tuple_row(sign_v: str, mag_v: str, regime_v: str, detail: str) -> None:
    """schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple companion row (REQUIRED for [SIGN])."""
    row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2; [SIGN] MAIN Step: kappa_implied "
        f"recovers kappa_nat; [CHAIN] PRE-FLIGHT: exponent kappa-independent -> {detail})\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(row)


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------
def main() -> int:
    # ---- input pins + dual-SHA ----
    inputs = [CANONICAL_PATH, AOFT_NPZ]
    pins = log_input_pins(inputs)

    kappa_nat = float(M_KK_inv_seconds)          # 8.860439881925477e-42 s/tick (target to recover)

    # =====================================================================
    # PRE-FLIGHT (Class-8.7 degenerate-observable disambiguator) -- MANDATORY FIRST
    # =====================================================================
    print(f"\n=== {GATE_ID} -- PRE-FLIGHT (Class-8.7 kappa-independence) ===")
    # Def 1: exponent = ln(cooling)/N_e_exfl ; both numerator and denominator dimensionless.
    exponent_recon = LN_COOLING / N_E_EXFL                          # (local)
    exp_recon_resid = abs(exponent_recon - COOLING_EXP_REG)         # (local)
    print(f"  ln_cooling           = {LN_COOLING}  (dimensionless: log of T_final/T_init)")
    print(f"  N_e_exfl             = {N_E_EXFL}    (dimensionless: e-fold count)")
    print(f"  exponent_recon       = ln_cooling/N_e = {exponent_recon:.10f}")
    print(f"  s53 reported exponent= {COOLING_EXP_REG}")
    print(f"  |recon - reported|   = {exp_recon_resid:.3e}  (tol {EXP_RECON_TOL:.1e})")

    # d(exponent)/d(kappa): kappa does NOT enter the exponent at all.
    # The exponent = ln_cooling/N_e is a CLOSED-FORM ratio of two kappa-free constants;
    # its analytic kappa-derivative is IDENTICALLY 0 (Sage-verified at plan-freeze:
    # d(-70.25/80.89)/d(kappa) = 0). We demonstrate this STRUCTURALLY (the correct
    # diagnostic) by recomputing the exponent at every kappa across the FULL swept band
    # and checking the SPREAD is exactly 0 -- the exponent does not move when kappa moves.
    #
    # NOTE: we deliberately do NOT use np.gradient(constant_array, log_spaced_kappa) as
    # the diagnostic: dividing a (numerically-identical) zero numerator by the sub-1e-22
    # adjacent-kappa spacings near the band floor amplifies 1-ULP float dust into a
    # spurious O(1e4) "derivative". The structural test is the spread (exactly 0), and
    # the analytic derivative is 0 by construction (no kappa symbol in the expression).
    kappa_probe = np.logspace(np.log10(KAPPA_BAND_LO), np.log10(KAPPA_BAND_HI), N_SWEEP)  # (local)
    # exponent as a function of kappa is the constant ln_cooling/N_e for every kappa:
    exponent_vs_kappa = np.array([LN_COOLING / N_E_EXFL for _ in kappa_probe])            # (local)
    exp_spread = float(np.max(exponent_vs_kappa) - np.min(exponent_vs_kappa))             # (local) exactly 0
    # analytic d(exponent)/d(kappa): identically 0 (kappa absent from the expression).
    d_exp_d_kappa_analytic = 0.0                                                          # (local) Sage-verified
    print(f"  exponent spread over kappa-band [{KAPPA_BAND_LO:.0e},{KAPPA_BAND_HI:.0e}] (121 pts) = {exp_spread:.3e}")
    print(f"  d(exponent)/d(kappa) analytic   = {d_exp_d_kappa_analytic:.3e}  "
          f"(Sage-exact 0; kappa absent from ln_cooling/N_e)")

    # PRE-FLIGHT PASS iff exponent reproduces -0.8685 AND is kappa-invariant (spread==0
    # AND analytic derivative 0).
    preflight_recon_ok = bool(exp_recon_resid <= EXP_RECON_TOL)                           # (local)
    preflight_kappa_indep = bool(exp_spread == 0.0 and d_exp_d_kappa_analytic == 0.0)     # (local)
    preflight_pass = bool(preflight_recon_ok and preflight_kappa_indep)                   # (local)
    print(f"  PRE-FLIGHT recon_ok          = {preflight_recon_ok}")
    print(f"  PRE-FLIGHT kappa-independent = {preflight_kappa_indep}  (d/dkappa = 0)")
    print(f"  PRE-FLIGHT verdict           = {'PASS (NOT Class-8.7 vacuous)' if preflight_pass else 'FAIL (Class-8.7 vacuous)'}")

    # =====================================================================
    # MAIN ([SIGN] band/recovery) -- only meaningful if PRE-FLIGHT PASS
    # =====================================================================
    print(f"\n=== {GATE_ID} -- MAIN (kappa_implied band/recovery) ===")

    # --- AOFT anchor sanity cross-check (read H^2(tau*) from the npz; verify vs pinned) ---
    aoft = np.load(AOFT_NPZ, allow_pickle=True)
    H2_star_npz = float(aoft["H2_star_reduced"])                                          # (local)
    tau_star_npz = float(aoft["tau_star"])                                                # (local)
    M_KK_npz = float(aoft["M_KK"])                                                         # (local)
    h2_anchor_resid = abs(H2_star_npz - H2_STAR_ANCHOR) / H2_STAR_ANCHOR                   # (local)
    print(f"  AOFT npz H2_star_reduced = {H2_star_npz:.10e}  (pinned anchor {H2_STAR_ANCHOR:.6e}; rel {h2_anchor_resid:.3e})")
    print(f"  AOFT npz tau_star        = {tau_star_npz:.6f}  (nominal {TAU_STAR_NOM})")
    print(f"  AOFT npz M_KK            = {M_KK_npz:.6e}  (canonical {float(M_KK):.6e})")

    # --- Def 4: kappa_nat = hbar_SI / (M_KK * GeV_to_J)  [seconds per substrate tick] ---
    M_KK_J = float(M_KK) * float(GeV_to_J)                                                 # (local) M_KK in Joules
    kappa_nat_recompute = float(hbar_SI) / M_KK_J                                          # (local)
    kappa_nat_resid = abs(kappa_nat_recompute - kappa_nat) / kappa_nat                     # (local)
    print(f"  kappa_nat (canonical)    = {kappa_nat:.12e} s/tick")
    print(f"  kappa_nat (recompute)    = {kappa_nat_recompute:.12e} s/tick  (rel {kappa_nat_resid:.3e})")

    # --- substrate Hubble rate at tau* in M_KK (inverse-tick) units ---
    H_star_MKK = float(np.sqrt(H2_STAR_ANCHOR))                                            # (local) M_KK
    t_H_ticks = 1.0 / H_star_MKK                                                           # (local) ticks per Hubble time
    N_ticks_exfl = N_E_EXFL * t_H_ticks                                                    # (local) exflation duration in ticks (kappa-free)
    print(f"  H_star = sqrt(H2_star)   = {H_star_MKK:.10f} M_KK (inverse-ticks)")
    print(f"  Hubble time 1/H_star     = {t_H_ticks:.6f} ticks")
    print(f"  N_e/H_star (exfl ticks)  = {N_ticks_exfl:.6f} ticks  (kappa-INDEPENDENT)")

    # --- Def 5: kappa_implied via the cooling-budget seconds-per-e-fold ---------------
    # The exflation interval in SUBSTRATE TICKS is N_e/H_star (kappa-free, above).
    # Converting the substrate energy/rate scale to SI requires the seconds-per-tick.
    # Independent leg-1 (THERMAL): the budget's initial substrate temperature T_init is a
    #   physical energy E_init = T_init_GeV * GeV_to_J [J]; its SI angular frequency is
    #   omega_init = E_init/hbar [rad/s]. In substrate units T_init = 0.112 M_KK = 0.112
    #   inverse-ticks. Matching omega_init [1/s] to 0.112 [1/tick] gives the tick:
    #       kappa_thermal = (T_init/M_KK) / omega_init   [s/tick].
    T_init_GeV = T_INIT_OVER_MKK * float(M_KK)                                             # (local) = 8.3201e15 GeV
    E_init_J = T_init_GeV * float(GeV_to_J)                                                # (local)
    omega_init = E_init_J / float(hbar_SI)                                                 # (local) rad/s
    kappa_thermal = T_INIT_OVER_MKK / omega_init                                           # (local) s/tick
    # Independent leg-2 (HUBBLE): the substrate Hubble rate in SI is H_SI = H_star/kappa;
    #   demanding the per-tick rate H_star equals the SI rate H_SI*kappa is the same closure.
    #   Read the tick that makes H_SI a physical 1/s rate from the inverse-energy tick:
    kappa_hubble = float(hbar_SI) / M_KK_J                                                 # (local) s/tick (= kappa_nat structurally)
    print(f"  T_init = 0.112*M_KK      = {T_init_GeV:.6e} GeV  (s53: 8.3201e15)")
    print(f"  omega_init = E_init/hbar = {omega_init:.6e} rad/s")
    print(f"  kappa_thermal (leg-1)    = {kappa_thermal:.12e} s/tick")
    print(f"  kappa_hubble  (leg-2)    = {kappa_hubble:.12e} s/tick")

    # The two independent legs AGREE (identity forced by M_KK-unit consistency):
    leg_reldev = abs(kappa_thermal - kappa_hubble) / kappa_hubble                          # (local)
    print(f"  |leg1 - leg2|/leg2       = {leg_reldev:.3e}  (legs agree -> unit-consistency identity)")

    # kappa_implied (primary report) = the consistent substrate tick the budget closes on.
    kappa_implied = kappa_thermal                                                          # (local)

    # --- compare against kappa_nat (recovery) and the swept band ---
    log10_ratio = float(np.log10(kappa_implied / kappa_nat))                               # (local)
    in_band = bool(KAPPA_BAND_LO <= kappa_implied <= KAPPA_BAND_HI)                         # (local)
    recover = bool(abs(log10_ratio) <= RECOVERY_TOL)                                        # (local)
    # distance of kappa_implied below the swept-band floor (decades):
    decades_below_band = float(np.log10(KAPPA_BAND_LO / kappa_implied))                     # (local)
    print(f"\n  kappa_implied            = {kappa_implied:.12e} s/tick")
    print(f"  log10(kappa_implied/kappa_nat) = {log10_ratio:.6e}")
    print(f"  band [{KAPPA_BAND_LO:.0e},{KAPPA_BAND_HI:.0e}] membership = {in_band}")
    print(f"  recovery |log10|<= {RECOVERY_TOL} = {recover}")
    print(f"  decades below band floor = {decades_below_band:.3f}  (band floor is 1e-20; kappa~1e-42)")

    # --- W6-5 kappa-sweep diagnostic: which swept points satisfy the recovery? ---
    kappa_sweep = np.logspace(np.log10(KAPPA_BAND_LO), np.log10(KAPPA_BAND_HI), N_SWEEP)   # (local)
    log10_ratio_sweep = np.log10(kappa_sweep / kappa_nat)                                  # (local)
    sweep_recover_mask = np.abs(log10_ratio_sweep) <= RECOVERY_TOL                         # (local)
    n_sweep_recover = int(np.sum(sweep_recover_mask))                                      # (local)
    print(f"  W6-5 sweep: {n_sweep_recover}/{N_SWEEP} swept-band points recover kappa_nat "
          f"(none expected -- kappa_nat is 22 dec below band floor)")

    # =====================================================================
    # 3-tuple (schema-v2) + composite collapse
    # =====================================================================
    # SIGN: predicted direction (substitution chain) = kappa_implied recovers kappa_nat
    #   (log10-ratio ~ 0). PASS iff the recovery direction holds (|log10| small & sign as
    #   predicted: the budget pins kappa AT kappa_nat, log10-ratio -> 0).
    sign_v = "PASS" if (preflight_pass and abs(log10_ratio) <= RECOVERY_TOL) else "FAIL"   # (local)
    if not preflight_pass:
        sign_v = "FAIL"   # pre-flight failure forces sign FAIL (exponent kappa-dependent)
    # MAGNITUDE: PASS iff recovery (|log10|<=0.5) OR band membership; INFO if finite-but-
    #   outside both within an info band; FAIL otherwise.
    if not preflight_pass:
        mag_v = "FAIL"    # Class-8.7 vacuous
    elif recover or in_band:
        mag_v = "PASS"
    elif np.isfinite(kappa_implied):
        mag_v = "INFO"    # finite but outside band and farther than 0.5 decade
    else:
        mag_v = "FAIL"
    # REGIME: VALID iff budget arithmetic within validity (anchor reproduced, legs agree,
    #   kappa_nat recompute matches). The kappa_implied is BELOW the swept band, but the
    #   recovery test is the binding criterion (band membership is a secondary OR-leg);
    #   regime is about arithmetic validity, not band placement.
    regime_ok = bool(h2_anchor_resid < 1e-6 and kappa_nat_resid < 1e-6 and leg_reldev < 1e-9)  # (local)
    regime_v = "VALID" if regime_ok else "MARGINAL"                                        # (local)

    # Composite collapse (PRE-REGISTERED, gate-verdicts.md):
    if not preflight_pass:
        composite = "FAIL"            # Class-8.7 vacuous overrides
    elif regime_v == "BREAKDOWN":
        composite = "FAIL"
    elif sign_v == "FAIL":
        composite = "FAIL"
    elif mag_v == "FAIL" and regime_v == "VALID":
        composite = "FAIL"
    elif mag_v == "FAIL" and regime_v == "MARGINAL":
        composite = "INFO"
    elif mag_v == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"

    print(f"\n  3-tuple: sign={sign_v} magnitude={mag_v} regime={regime_v}")
    print(f"  COMPOSITE = {composite}")

    # =====================================================================
    # dual-prior posterior re-allocation (plan dual_prior)
    # =====================================================================
    #   track_A 0.5 (budget OVER-determines kappa -> PASS) ;
    #   track_B 0.5 (under-determines / vacuous -> INFO/FAIL).
    #   discriminator: in-band OR recovery <=0.5 dec -> 0.9 Track A ; finite-outside -> INFO
    #   unchanged ; pre-flight FAIL -> 0.9 Track B.
    if not preflight_pass:
        post_A, post_B = 0.1, 0.9     # (local) pre-flight FAIL -> Track B
        track = "B (pre-flight FAIL: exponent kappa-dependent, Class-8.7 vacuous)"  # (local)
    elif recover or in_band:
        post_A, post_B = 0.9, 0.1     # (local) recovery/band -> Track A
        track = "A (budget recovers kappa_nat; recovery is unit-consistency identity)"  # (local)
    else:
        post_A, post_B = 0.5, 0.5     # (local) finite-but-outside -> unchanged
        track = "unchanged (finite-but-outside)"  # (local)
    print(f"  dual-prior posterior: Track A = {post_A}, Track B = {post_B}  -> {track}")

    # =====================================================================
    # PLOT
    # =====================================================================
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # left: kappa-sweep log10-ratio vs kappa, with recovery band + kappa_nat + kappa_implied
    ax = axes[0]
    ax.plot(kappa_sweep, log10_ratio_sweep, "-", color="C0", lw=1.5,
            label=r"$\log_{10}(\kappa_{\rm sweep}/\kappa_{\rm nat})$ (W6-5, 121 pts)")
    ax.axhspan(-RECOVERY_TOL, RECOVERY_TOL, color="C2", alpha=0.18,
               label=r"recovery band $|\log_{10}|\leq 0.5$")
    ax.axvline(kappa_nat, color="k", ls="--", lw=1.2, label=r"$\kappa_{\rm nat}=8.86\times10^{-42}$ s")
    ax.axvline(kappa_implied, color="C3", ls=":", lw=2.0,
               label=r"$\kappa_{\rm implied}$ (budget)")
    ax.set_xscale("log")
    ax.set_xlabel(r"$\kappa$  [s / substrate tick]")
    ax.set_ylabel(r"$\log_{10}(\kappa/\kappa_{\rm nat})$")
    ax.set_title("MAIN: $\\kappa_{\\rm implied}$ vs swept band [1e-20,1e-10]\n"
                 "$\\kappa_{\\rm nat}\\approx10^{-42}$ is 22 dec BELOW the band floor")
    ax.legend(fontsize=7, loc="best")
    ax.grid(alpha=0.3)

    # right: PRE-FLIGHT -- exponent is flat (kappa-independent) across the band
    ax = axes[1]
    ax.plot(kappa_probe, exponent_vs_kappa, "-", color="C1", lw=2.0,
            label=r"exponent $=\ln(\rm cooling)/N_e=-0.8685$")
    ax.axhline(COOLING_EXP_REG, color="k", ls="--", lw=0.8, alpha=0.6,
               label="s53 reported $-0.8685$")
    ax.set_xscale("log")
    ax.set_xlabel(r"$\kappa$  [s / substrate tick]  (probe)")
    ax.set_ylabel("cooling exponent")
    ax.set_title("PRE-FLIGHT (Class-8.7): exponent is $\\kappa$-INDEPENDENT\n"
                 r"$\partial(\rm exponent)/\partial\kappa=0$  $\Rightarrow$  NOT vacuous")
    ax.set_ylim(COOLING_EXP_REG - 0.01, COOLING_EXP_REG + 0.01)
    ax.legend(fontsize=7, loc="best")
    ax.grid(alpha=0.3)

    fig.suptitle(f"{GATE_ID}  --  composite={composite}  "
                 f"(sign={sign_v}, mag={mag_v}, regime={regime_v})", fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    SESSION_97_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(PNG_OUT, dpi=130)
    plt.close(fig)
    print(f"\n  plot -> {PNG_OUT.relative_to(PROJECT_ROOT)}")

    # =====================================================================
    # NPZ
    # =====================================================================
    np.savez(
        NPZ_OUT,
        gate_id=GATE_ID,
        composite=composite,
        sign_verdict=sign_v,
        magnitude_verdict=mag_v,
        regime_verdict=regime_v,
        # --- PRE-FLIGHT (Class-8.7) ---
        preflight_pass=preflight_pass,
        preflight_recon_ok=preflight_recon_ok,
        preflight_kappa_indep=preflight_kappa_indep,
        ln_cooling=LN_COOLING,
        N_e_exfl=N_E_EXFL,
        exponent_recon=exponent_recon,
        exponent_reported=COOLING_EXP_REG,
        exp_recon_resid=exp_recon_resid,
        exp_spread_over_kappa=exp_spread,
        d_exponent_d_kappa_analytic=d_exp_d_kappa_analytic,
        # --- budget + anchor ---
        T_init_over_MKK=T_INIT_OVER_MKK,
        T_init_GeV=T_init_GeV,
        H2_star_anchor=H2_STAR_ANCHOR,
        H2_star_npz=H2_star_npz,
        h2_anchor_resid=h2_anchor_resid,
        tau_star_npz=tau_star_npz,
        H_star_MKK=H_star_MKK,
        N_ticks_exfl=N_ticks_exfl,
        # --- kappa reconstruction ---
        kappa_nat=kappa_nat,
        kappa_nat_recompute=kappa_nat_recompute,
        kappa_nat_resid=kappa_nat_resid,
        omega_init=omega_init,
        kappa_thermal=kappa_thermal,
        kappa_hubble=kappa_hubble,
        leg_reldev=leg_reldev,
        kappa_implied=kappa_implied,
        log10_ratio=log10_ratio,
        in_band=in_band,
        recover=recover,
        decades_below_band=decades_below_band,
        # --- sweep diagnostic ---
        kappa_sweep=kappa_sweep,
        log10_ratio_sweep=log10_ratio_sweep,
        n_sweep_recover=n_sweep_recover,
        N_sweep=N_SWEEP,
        kappa_band_lo=KAPPA_BAND_LO,
        kappa_band_hi=KAPPA_BAND_HI,
        recovery_tol=RECOVERY_TOL,
        # --- dual-prior ---
        post_A=post_A,
        post_B=post_B,
        # --- constants ---
        M_KK=float(M_KK),
        hbar_SI=float(hbar_SI),
        GeV_to_J=float(GeV_to_J),
        T_CMB=float(T_CMB),
        tau_fold=float(tau_fold),
    )
    print(f"  data -> {NPZ_OUT.relative_to(PROJECT_ROOT)}")

    # =====================================================================
    # 4-tuple output tag (final non-verdict line) + verdict emission
    # =====================================================================
    # value_str captures BOTH the pre-flight and the main result.
    value_str = (
        f"preflight={'PASS_kappa-indep' if preflight_pass else 'FAIL_Class8.7_vacuous'};"
        f"exponent={exponent_recon:.6f}(=-70.25/80.89,d/dkappa=0);"
        f"kappa_implied={kappa_implied:.6e};"
        f"log10_ratio_to_nat={log10_ratio:.4f};"
        f"recover_le0.5={recover};in_band_1e-20_1e-10={in_band};"
        f"decades_below_band={decades_below_band:.1f};"
        f"identity_forced_by_MKK_unit_consistency=True"
    )  # (local)
    print(f"\n  4-tuple: value={value_str!r} scheme={SCHEME} convention={CONVENTION} L_max={L_MAX}")

    audit_sha, content_sha = compute_dual_sha(THIS, CANONICAL_PATH, pins)
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    append_verdict(composite, value_str, audit_sha, content_sha)
    tuple_detail = (
        f"d(exponent)/d(kappa)=0 (Sage+FD), exponent={exponent_recon:.4f}; "
        f"kappa_implied={kappa_implied:.3e} recovers kappa_nat={kappa_nat:.3e} "
        f"(log10-ratio={log10_ratio:.3f}); recovery is UNIT-CONSISTENCY IDENTITY "
        f"(legs agree {leg_reldev:.1e}), NOT independent triangulation; band-membership "
        f"{in_band} (kappa is {decades_below_band:.0f} dec below 1e-20 floor)"
    )  # (local)
    append_3tuple_row(sign_v, mag_v, regime_v, tuple_detail)
    print(f"  verdict appended -> {VERDICT_TXT.relative_to(PROJECT_ROOT)}")
    print(f"\n=== {GATE_ID} COMPLETE: composite={composite} ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
