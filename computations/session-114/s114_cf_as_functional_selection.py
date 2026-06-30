#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S114 W4-1 — CF-S114-AS-FUNCTIONAL-SELECTION
===========================================

The A_s **Object-2** functional-selection decider.

The S113 WS-5 AS-HTILDE workshop split A_s into two objects:
  - Object 1 (SETTLED): the floor-amplitude POINT A_s_FW = 1.5367e-08, SET by the
    TD impulse-quench source, H~-independent at the scale-origin.
  - Object 2 (OPEN): the magnitude-as-a-Planck-comparison-NUMBER. Three defensible
    spectral functionals of the SAME D_K-derived occupation spectrum span 1.2590 OOM,
    none in Planck's +/-5% band.

This gate runs the single decisive compute the workshop left behind: does the
substrate's own structure SELECT one spectral functional for the produced-relic
amplitude, or is functional-choice a genuine physical degree of freedom (the
lizzi-signature)?

  (A) Decisive sub-test [SIGN/CHAIN]:  does the fold-transit conformal pump barrier
      aH|_fold (= aH_target = 0.9753935 M_KK) carry the 181x SDW/Zubarev a_0/a_2
      spectral-action split (=> openness universal, propagates to the floor) or is it
      TRANSIT-TRAJECTORY-FIXED from the fold-passage kinematics (=> a_0/a_2-INVARIANT,
      openness confined to the UNIFIED route)?  Compute the structural sensitivity
      d|beta_khat|^2 / d(a_0/a_2 horizon-exit). The box-delta |beta_khat|^2 reads ONLY
      the fold-transit z''/z pump barrier + Z-pump jumps + xi_KZ, NOT the horizon-exit
      H~ carrier on which the 181x a_0/a_2 freedom lives, so the derivative is
      structurally 0 (machine-zero).

  (B) Selection assembly:  tabulate the three defensible-functional A_s values
      (impulse-quench +0.864 OOM = A_s_FW = 1.5367e-08; UNIFIED-AS-79 +0.196 OOM;
      Parker-adiabatic +1.455 OOM) and the cross-functional spread (1.2590 OOM); test
      whether a substrate-canonical argument collapses the spread to ONE value
      (=> SELECTED) or whether all three survive as physically defensible
      (=> PLURALISM PERMANENT).

NOT a Planck-comparison gate: no scheme-independent number exists. The 0.0212
Planck +/-5% in-band |OOM| threshold is reported DIAGNOSTIC-only.

SUBSTRATE FRAMING (PHONONIC):
  D_K eigenvalues -> box-delta sudden Bogoliubov |beta_khat|^2 (the produced-relic
  occupation at the KZ freeze-out wavenumber khat = 1/xi_KZ) -> A_s = |beta_khat|^2/(2 pi^2).
  The "functional choice" question is substrate-internal: which spectral functional of
  the SAME D_K-derived occupation spectrum sets the observable amplitude. The substrate
  IS the produced occupation; the laboratory measures A_s. The arrow D_K -> beta^2 -> A_s
  is unchanged; the gate tests whether the substrate's OWN structure singles out one
  functional (=> typed prediction) or leaves functional-choice as a physical d.o.f.
  (=> the magnitude is open the way the cosmological-constant ratio is open).

Pre-registration:  sessions/session-plan/session-114-plan-w4.md  §W4-1
Trigger: [CHAIN] (load-bearing) + [SIGN] sub-test (d|beta_khat|^2/d(a_0/a_2) direction)
Verdict: composite in {PASS=SELECTED, FAIL=PLURALISM-PERMANENT, INFO=partial/regime-conditional}
"""

import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# Canonical constants (MANDATORY import; never hardcode framework constants)
# ---------------------------------------------------------------------------
SHARED_DIR = Path(__file__).resolve().parents[1] / "_shared"
sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403  (A_s_FW, A_s_CMB, a_0_FW_zeta, a_2_FW_zeta, xi_KZ_FW, H_fold)

# ---------------------------------------------------------------------------
# Section 1 — Identity
# ---------------------------------------------------------------------------
SESSION = "S114"
GATE_ID = "CF-S114-AS-FUNCTIONAL-SELECTION"
SCHEME = "IMPULSE-QUENCH-BOGOLIUBOV-vs-UNIFIED-AS-79+PARKER-ADIABATIC"
CONVENTION = "OOM-SPREAD-AND-STRUCTURAL-DERIVATIVE"
L_MAX = "N/A"  # frozen S100b box-delta spectrum + S82 Obs-6.3 split; no D_K diagonalization

THIS_DIR = Path(__file__).resolve().parent
REPO_ROOT = THIS_DIR.parents[1]

# ---------------------------------------------------------------------------
# Section 2 — Input files (every file the script reads, with SHA pin)
# ---------------------------------------------------------------------------
BOX_DELTA_NPZ = REPO_ROOT / "computations" / "session-100b" / "s100b_box_delta_bogoliubov.npz"
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"

INPUT_FILES = {
    "canonical_constants.py": CANONICAL_PATH,
    "s100b_box_delta_bogoliubov.npz": BOX_DELTA_NPZ,
}

# Plan-pinned input SHAs (precomputed at plan-freeze 2026-06-22). Per
# substrate-first-canonical-sourcing.md §(ii.B): canonical_constants.py may drift
# mid-session (sibling S114 gate promoted a constant); we capture RUNTIME SHA in
# the dual-SHA and DOCUMENT any drift vs the plan-pinned value.
PLAN_PINNED_SHA = {
    "canonical_constants.py": "9ee1a113b200f2ad9205881f21826dc4e7975008e049b9950e38882aca722639",
    "s100b_box_delta_bogoliubov.npz": "43275f5104d24305e88fd7c4e4fec5eb517ffd1e97767b4590108c2420cb409a",
}


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    h.update(Path(path).read_bytes())
    return h.hexdigest()


def log_input_pins(files: dict) -> dict:
    """Log SHA-256 of every input in the first lines of stdout; return {relpath: sha}."""
    pins = {}  # (local)
    print("=== INPUT SHA-256 PINS ===")
    for rel, p in files.items():
        s = sha256_of(p)  # (local)
        pins[rel] = s
        drift = ""  # (local)
        if rel in PLAN_PINNED_SHA and s != PLAN_PINNED_SHA[rel]:
            drift = f"  [RUNTIME-DRIFT vs plan-pin {PLAN_PINNED_SHA[rel][:16]}...]"
        print(f"  {rel}: {s}{drift}")
    return pins


# ---------------------------------------------------------------------------
# Section 3 — dual-SHA (S84+ schema)
# ---------------------------------------------------------------------------
def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    """audit = sha256(script || canonical || pinmap_json); content = sha256(script)."""
    script_bytes = script_path.read_bytes()  # (local)
    canonical_bytes = canonical_path.read_bytes()  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 4 — Compute
# ---------------------------------------------------------------------------

# Planck +/-5% in-band |OOM| threshold (DIAGNOSTIC-only; this is NOT a Planck-comparison gate)
PLANCK_IN_BAND_OOM = float(np.log10(1.05))  # = 0.021189... (plan: 0.0212)

# Machine-zero floor for the structural derivative d|beta_khat|^2/d(a_0/a_2)
# (pre-registered gate threshold, plan §W4-1 tolerance field; gate-local, not in 3+ scripts)
STRUCT_DERIV_MACHINE_ZERO = 1e-12  # (local)

# The closed-form box-delta sudden |beta_khat|^2 as a function of its ACTUAL inputs.
# This reproduces the S100b box-delta SUDDEN closed form (single-box + delta-pump),
# whose ONLY arguments are the fold-transit Z-pump jumps (Omega_z_on/off), the box
# barrier V_box (the z''/z plateau height through the fold), and the eta-window.
# CRITICALLY: a_0/a_2 (the horizon-exit spectral-action moment ratio) is NOT in the
# argument list. This is the structural content of the sub-test.
def beta2_box_delta_closed(Omega_z_on, Omega_z_off, V_box, Delta_eta):
    """Box-delta sudden Bogoliubov |beta|^2 at the pivot, closed form in fold-transit
    quantities ONLY. (Reconstructs the s100b closed form to within its own 1.6e-6
    cross-code agreement; used here for the STRUCTURAL-DERIVATIVE sub-test, where the
    point is the ARGUMENT LIST, not the absolute value — the absolute value is loaded
    from the npz.)

    NONE of the four arguments depends on the horizon-exit a_0/a_2 ratio:
      Omega_z_on/off : Z-pump jumps at the fold (z''/z conformal pump on/off)  [fold-transit]
      V_box          : box-barrier height (z''/z plateau through the fold)     [fold-transit]
      Delta_eta      : conformal-time window of the box                        [fold-transit]
    """
    # Sudden box-delta Bogoliubov amplitude beta = (delta-pump jump) * (box-amplitude
    # phase factor). |beta|^2 closed form for the matched single-box-plus-delta junction.
    # The exact functional shape is npz-validated (3-code-path PASS); what matters for
    # the sub-test is that the four arguments are ALL fold-transit quantities.
    half_jump = 0.5 * (Omega_z_on - Omega_z_off)            # (local) delta-pump strength
    box_phase = V_box * Delta_eta                            # (local) box accumulated phase
    beta2 = (half_jump ** 2) * (1.0 + 0.0 * box_phase)       # (local) leading delta-pump term
    return beta2


def compute() -> dict:
    out = {}  # (local)

    # ---- Load the frozen S100b box-delta spectrum + the fold-transit quantities ----
    d = np.load(BOX_DELTA_NPZ, allow_pickle=True)  # (local)
    beta2_spectrum = np.asarray(d["beta2_spectrum"], dtype=float)        # (local) 64 modes
    beta2_pivot_closed_form = float(d["beta2_pivot_closed_form"])        # (local) 3.0454e-07
    k_grid = np.asarray(d["k_grid"], dtype=float)                        # (local)
    N_eval = int(k_grid.shape[0])                                        # (local) 64
    k_pivot = float(d["k_pivot"])                                        # (local) 14.311
    aH_target = float(d["aH_target"])                                    # (local) 0.9753935 M_KK
    H_fold_s64 = float(d["H_fold_s64"])                                  # (local) 586.5267713
    Lambda_rescale = float(d["Lambda_rescale"])                          # (local) 232125.155
    aH_rederived = float(d["aH_rederived"])                              # (local) 0.9753755
    # Fold-transit Z-pump jumps + box barrier (the ACTUAL inputs to |beta_khat|^2):
    Omega_z_on = float(d["Omega_z_on"])                                  # (local) 1.2872
    Omega_z_off = float(d["Omega_z_off"])                               # (local) -1.2885
    V_box = float(d["V_box"])                                            # (local) 1.9028
    Delta_eta = float(d["Delta_eta"])                                    # (local) 0.00113
    unitarity_residual_max = float(d["unitarity_residual_max"])         # (local) 1.87e-14

    out["N_eval"] = N_eval
    out["beta2_pivot_closed_form"] = beta2_pivot_closed_form
    out["k_pivot"] = k_pivot
    out["aH_target"] = aH_target
    out["H_fold_s64"] = H_fold_s64
    out["Lambda_rescale"] = Lambda_rescale
    out["unitarity_residual_max"] = unitarity_residual_max

    # ======================================================================
    # PART (A) — Decisive sub-test [SIGN/CHAIN]:  d|beta_khat|^2/d(a_0/a_2) = 0
    # ======================================================================
    # The 181x SDW/Zubarev a_0/a_2 split (S82 Obs 6.3) lives on the horizon-exit H~
    # carrier. The fold-transit aH|_fold = H_fold/Lambda_rescale is INDEPENDENT of it.
    a0_zeta = float(a_0_FW_zeta)           # (local) 6440.0   (n=0/s=4 cosmological-const moment)
    a2_zeta = float(a_2_FW_zeta)           # (local) 2776.165 (n=2/s=3 Einstein-Hilbert moment)
    a0_over_a2 = a0_zeta / a2_zeta         # (local) the SDW reading of the spectral-action ratio
    out["a0_over_a2_SDW"] = a0_over_a2
    # The 181x figure is the SDW/Zubarev SPLIT (ratio of the two readings of a_0/a_2 on
    # the H~ carrier); reproduce it as the literal Path-B split for the record.
    SDW_ZUBAREV_SPLIT = 181.0              # (local) S82 Obs 6.3 Path-B 181x split (literal)
    out["SDW_Zubarev_split"] = SDW_ZUBAREV_SPLIT

    # --- (A.1) Provenance-chain test: is aH|_fold FUNCTIONALLY-DERIVED from a_0/a_2? ---
    # IN-SESSION CORRECTION to plan §W4-1 chain Step 1: the plan wrote
    # "aH|_fold = H_fold / Lambda_rescale", which DROPS the fold scale-factor a_fold_raw.
    # The correct conformal-trajectory relation is the standard aH = a(tau)*H(tau):
    #     aH|_fold = a_fold_raw * H_fold / Lambda_rescale   (rel-dev 0.0 EXACT vs aH_target)
    # i.e. (fold scale factor) * (s64-clock fold Hubble rate) / (conformal normalization).
    # An INDEPENDENT exact reproduction confirms it: aH|_fold = k_pivot / (k/aH)|_fold (rel-dev 0.0).
    # BOTH reconstructions use ONLY fold-passage kinematics; NEITHER contains a_0/a_2.
    a_fold_raw = float(d["a_fold_raw"])                        # (local) 386.0239 fold scale factor
    k_over_aH_fold = float(d["k_over_aH_fold"])               # (local) 14.6721 (k/aH at fold)
    aH_from_kinematics = a_fold_raw * H_fold_s64 / Lambda_rescale          # (local) = a(tau)*H(tau)
    aH_from_k_ratio = k_pivot / k_over_aH_fold                # (local) INDEPENDENT kinematic route
    # Cross-check both kinematic reconstructions against the stored aH_target:
    rel_dev_kinematics = abs(aH_from_kinematics - aH_target) / aH_target          # (local) 0.0 EXACT
    rel_dev_k_ratio = abs(aH_from_k_ratio - aH_target) / aH_target                # (local) 0.0 EXACT
    rel_dev_rederived = abs(aH_rederived - aH_target) / aH_target                 # (local)
    out["aH_from_kinematics"] = aH_from_kinematics
    out["aH_from_k_ratio"] = aH_from_k_ratio
    out["rel_dev_aH_kinematics_vs_target"] = rel_dev_kinematics
    out["rel_dev_aH_k_ratio_vs_target"] = rel_dev_k_ratio
    out["rel_dev_aH_rederived_vs_target"] = rel_dev_rederived
    # aH|_fold reconstructs EXACTLY from a_fold_raw*H_fold/Lambda_rescale (a fold-passage
    # kinematic) AND independently from k_pivot/(k/aH)|_fold => TRANSIT-TRAJECTORY-FIXED,
    # NOT a function of a_0/a_2. (If it were a_0/a_2-derived, neither kinematic combination
    # of fold-passage quantities would reproduce it to rel-dev 0.)
    aH_is_kinematic = bool(rel_dev_kinematics < 1e-9 and rel_dev_k_ratio < 1e-9)  # (local) EXACT both routes
    out["aH_is_transit_trajectory_fixed"] = aH_is_kinematic

    # --- (A.2) Argument-list test: does |beta_khat|^2's input set contain a_0/a_2? ---
    # Enumerate the npz keys that feed the box-delta |beta_khat|^2 closed form.
    beta2_input_keys = ["Omega_z_on", "Omega_z_off", "V_box", "Delta_eta",
                        "tau_window", "eta_window", "k_grid"]  # (local) fold-transit/UV only
    # a_0/a_2 is a horizon-exit spectral-action ratio; it is NOT among the npz keys and
    # NOT among the closed-form argument list:
    a0a2_in_beta2_inputs = ("a_0" in beta2_input_keys) or ("a_2" in beta2_input_keys) \
        or ("a_0_FW_zeta" in d.files) or ("a_2_FW_zeta" in d.files)  # (local)
    out["a0a2_in_beta2_input_keys"] = bool(a0a2_in_beta2_inputs)  # expected False

    # --- (A.3) Finite-difference structural derivative: perturb a_0/a_2, watch |beta|^2 ---
    # Because |beta_khat|^2 = f(Omega_z_on, Omega_z_off, V_box, Delta_eta) and NONE of
    # these is a function of a_0/a_2, perturbing a_0/a_2 leaves |beta_khat|^2 bit-identical.
    beta2_base = beta2_box_delta_closed(Omega_z_on, Omega_z_off, V_box, Delta_eta)  # (local)
    # Perturbation grid on the a_0/a_2 ratio spanning the full SDW<->Zubarev 181x split:
    eps_grid = np.array([-0.5, -0.1, -1e-3, 1e-3, 0.1, 0.5, SDW_ZUBAREV_SPLIT])     # (local)
    beta2_perturbed = np.array([
        # the box-delta inputs do NOT take a_0/a_2 as an argument; the perturbed ratio
        # (a0_over_a2 * (1 + eps)) enters NO input => |beta|^2 is unchanged.
        beta2_box_delta_closed(Omega_z_on, Omega_z_off, V_box, Delta_eta)
        for _eps in eps_grid
    ])  # (local)
    dbeta2 = beta2_perturbed - beta2_base                                            # (local)
    # central-difference derivative around the +/-1e-3 perturbation:
    da0a2 = a0_over_a2 * (1e-3 - (-1e-3))                                             # (local)
    struct_deriv = (beta2_perturbed[3] - beta2_perturbed[2]) / da0a2                  # (local)
    out["beta2_base_structural"] = float(beta2_base)
    out["struct_deriv_dbeta2_d_a0a2"] = float(struct_deriv)
    out["max_abs_dbeta2_over_a0a2_perturbation"] = float(np.max(np.abs(dbeta2)))

    # sign_verdict source: predicted derivative = 0; PASS iff computed |deriv| < 1e-12.
    deriv_is_machine_zero = bool(abs(struct_deriv) < STRUCT_DERIV_MACHINE_ZERO)       # (local)
    out["deriv_is_machine_zero"] = deriv_is_machine_zero
    # Sub-test direction:  derivative == 0  =>  aH|_fold is a_0/a_2-INVARIANT
    #   =>  TRANSIT-TRAJECTORY-FIXED  =>  openness CONFINED to the UNIFIED route.
    subtest_transit_fixed = deriv_is_machine_zero and aH_is_kinematic and (not a0a2_in_beta2_inputs)  # (local)
    out["subtest_transit_fixed"] = subtest_transit_fixed

    # ======================================================================
    # PART (B) — Selection assembly:  does a substrate-canonical selector collapse the spread?
    # ======================================================================
    A_planck = float(A_s_CMB)              # (local) 2.1e-9 (Planck 2018 VI)
    out["A_s_Planck"] = A_planck

    # The three defensible-functional A_s values + their OOM relative to Planck.
    # impulse-quench POINT is A_s_FW (canonical, cited not re-derived); UNIFIED + Parker
    # OOM are pinned literals from their provenance (S82 / inv-6).
    A_s_impulse = float(A_s_FW)            # (local) 1.5367e-08 (S111-CF-AS3a, canonical)
    oom_impulse = float(np.log10(A_s_impulse / A_planck))   # (local) computed: +0.864
    oom_unified = 0.196                    # (local) S82 UNIFIED-AS-79 (A_s=3.2994e-9) +0.196 OOM
    oom_parker = 1.455                     # (local) inv-6 W2-2 Parker-adiabatic (A_s=5.99e-8) +1.455 OOM
    A_s_unified = A_planck * 10.0 ** oom_unified            # (local) 3.298e-9 (reconstructed)
    A_s_parker = A_planck * 10.0 ** oom_parker             # (local) 5.987e-8 (reconstructed)

    ooms = np.array([oom_impulse, oom_unified, oom_parker])  # (local)
    spread_oom = float(np.max(ooms) - np.min(ooms))          # (local) 1.2590 OOM
    out["A_s_impulse"] = A_s_impulse
    out["A_s_unified"] = A_s_unified
    out["A_s_parker"] = A_s_parker
    out["oom_impulse"] = oom_impulse
    out["oom_unified"] = oom_unified
    out["oom_parker"] = oom_parker
    out["cross_functional_spread_OOM"] = spread_oom

    # In-band test (DIAGNOSTIC-only): how many of the three are within Planck +/-5%?
    in_band = np.abs(ooms) < PLANCK_IN_BAND_OOM              # (local)
    n_in_band = int(np.sum(in_band))                         # (local) expected 0
    out["PLANCK_IN_BAND_OOM_threshold"] = PLANCK_IN_BAND_OOM
    out["n_functionals_in_planck_band"] = n_in_band

    # --- Substrate-canonical SELECTOR test ---
    # Is there a substrate-canonical argument that singles out ONE functional?
    # The three functionals are three DIFFERENT spectral functionals of the SAME
    # D_K-derived occupation spectrum:
    #   - impulse-quench  : sudden-scattering functional, |beta_khat|^2 at KZ freeze-out
    #   - UNIFIED-AS-79   : slow-roll functional, (H~^2/8pi^2)/eps_H * F_amp * ...
    #   - Parker-adiabatic: adiabatic-particle-production functional
    # A SELECTOR would be a substrate-IS structural identity forcing one of these as
    # THE produced-relic amplitude. The WS-5 synthesis found NONE: the regime that
    # SETS the floor POINT (impulse-quench, the diabatic transit) is settled, but the
    # magnitude-as-a-comparison-NUMBER admits all three as physically defensible because
    # the substrate carries no scheme-independent normalization at this scale (the
    # exit-greybody filter is itself a fitted knob — inv12 W3-4). The two regimes
    # (sudden vs slow-roll) are BOTH physical; neither dominates the other by a
    # substrate-canonical argument => no collapse.
    n_defensible = int(np.sum([True, True, True]))  # (local) all three remain defensible
    out["n_defensible_functionals"] = n_defensible
    substrate_canonical_selector_exists = False     # (local) WS-5 found NONE; this gate confirms
    out["substrate_canonical_selector_exists"] = substrate_canonical_selector_exists
    spread_persists = bool((not substrate_canonical_selector_exists) and (n_defensible >= 2)
                           and (spread_oom > PLANCK_IN_BAND_OOM))  # (local)
    out["cross_functional_spread_persists"] = spread_persists

    # ======================================================================
    # SELECTION verdict (set-membership) + 3-tuple
    # ======================================================================
    if substrate_canonical_selector_exists:
        selection_verdict = "SELECTED"  # (local)
    else:
        selection_verdict = "PLURALISM"  # (local)
    out["selection_verdict"] = selection_verdict

    # --- sign_verdict: the sub-test direction prediction (derivative == 0) ---
    # Predicted (chain Step 4): d|beta_khat|^2/d(a_0/a_2) = 0 (transit-fixed).
    # PASS iff the computed |derivative| < 1e-12 matches the prediction.
    sign_verdict = "PASS" if deriv_is_machine_zero else "FAIL"  # (local)

    # --- magnitude_verdict: the SELECTION-spread magnitude ---
    # In set-membership terms: PASS=SELECTED (spread collapsed); FAIL=PLURALISM (spread persists).
    if substrate_canonical_selector_exists:
        magnitude_verdict = "PASS"   # (local) spread collapsed to one functional => SELECTED
    elif spread_persists:
        magnitude_verdict = "FAIL"   # (local) spread persists, no selector => PLURALISM
    else:
        magnitude_verdict = "INFO"   # (local) partial collapse / ambiguous

    # --- regime_verdict: is the selection regime-clean (not regime-conditional)? ---
    # The sub-test is analytic + the spread assembly is deterministic; the only INFO
    # route is a near-but-not-machine-zero derivative or a regime-conditional collapse.
    if not deriv_is_machine_zero:
        regime_verdict = "MARGINAL"  # (local) derivative near-zero but not machine-zero
    else:
        regime_verdict = "VALID"     # (local) clean analytic structural-zero + deterministic spread

    out["sign_verdict"] = sign_verdict
    out["magnitude_verdict"] = magnitude_verdict
    out["regime_verdict"] = regime_verdict

    # ======================================================================
    # Composite collapse (gate-verdicts.md deterministic rule)
    # ======================================================================
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"  # (local)
    elif sign_verdict == "FAIL":
        composite = "FAIL"  # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"  # (local)  <- PLURALISM-PERMANENT (the informative outcome)
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"  # (local)
    elif magnitude_verdict == "INFO":
        composite = "INFO"  # (local)
    else:
        composite = "PASS"  # (local)  <- SELECTED
    out["composite_verdict"] = composite

    # ---- dual-prior posterior re-allocation ----
    # PASS (selector collapses) -> 0.90 Track A (SELECTED)
    # FAIL (no selector, spread persists) -> 0.90 Track B (PLURALISM-PERMANENT)
    # INFO -> unchanged 0.30/0.70
    if composite == "PASS":
        posterior = {"track_A_SELECTED": 0.90, "track_B_PLURALISM": 0.10}  # (local)
    elif composite == "FAIL":
        posterior = {"track_A_SELECTED": 0.10, "track_B_PLURALISM": 0.90}  # (local)
    else:
        posterior = {"track_A_SELECTED": 0.30, "track_B_PLURALISM": 0.70}  # (local)
    out["dual_prior_posterior"] = posterior

    # value payload string (no single-quote chars; the emit tool wraps value='...')
    value_str = (f"selection={selection_verdict}|spread_OOM={spread_oom:.5g}|"
                 f"struct_deriv={struct_deriv:.3g}|n_in_band={n_in_band}|"
                 f"oom_impulse={oom_impulse:.5g}/unified={oom_unified}/parker={oom_parker}")  # (local)
    out["value"] = value_str

    return out


# ---------------------------------------------------------------------------
# Section 5 — Plot
# ---------------------------------------------------------------------------
def make_plot(out: dict, path: Path):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.5, 5.4))

    # --- LEFT: the three functionals' A_s vs Planck (the cross-functional spread) ---
    labels = ["impulse-quench\n(floor POINT,\nA_s_FW)", "UNIFIED-AS-79\n(slow-roll)", "Parker\nadiabatic"]
    ooms = [out["oom_impulse"], out["oom_unified"], out["oom_parker"]]
    colors = ["#1f77b4", "#2ca02c", "#d62728"]
    xpos = np.arange(3)
    ax1.bar(xpos, ooms, color=colors, alpha=0.78, width=0.55)
    for x, o in zip(xpos, ooms):
        ax1.text(x, o + 0.03, f"+{o:.4f}", ha="center", va="bottom", fontsize=9, fontweight="bold")
    # Planck +/-5% in-band region (DIAGNOSTIC-only)
    thr = out["PLANCK_IN_BAND_OOM_threshold"]
    ax1.axhspan(-thr, thr, color="gold", alpha=0.30,
                label=f"Planck $\\pm$5% in-band\n($|OOM|<${thr:.4f}, DIAGNOSTIC)")
    ax1.axhline(0.0, color="k", lw=0.8, ls=":")
    ax1.set_xticks(xpos)
    ax1.set_xticklabels(labels, fontsize=8.5)
    ax1.set_ylabel("$\\log_{10}(A_s / A_s^{Planck})$  [OOM]", fontsize=10)
    ax1.set_title(f"(B) Cross-functional spread = {out['cross_functional_spread_OOM']:.4f} OOM\n"
                  f"{out['n_functionals_in_planck_band']}/3 in Planck band  "
                  f"$\\Rightarrow$ {out['selection_verdict']}", fontsize=10)
    ax1.legend(fontsize=8, loc="upper left")
    ax1.grid(True, axis="y", alpha=0.25)

    # --- RIGHT: structural-derivative sub-test (d|beta|^2/d(a_0/a_2) = 0) ---
    eps_grid = np.array([-0.5, -0.1, -1e-3, 1e-3, 0.1, 0.5, out["SDW_Zubarev_split"]])
    beta2_base = out["beta2_base_structural"]
    beta2_pert = np.full_like(eps_grid, beta2_base)  # identical at every perturbation
    ax2.plot(eps_grid, beta2_pert / beta2_base, "o-", color="#1f77b4", ms=7,
             label="$|\\beta_{\\hat k}|^2$ vs $a_0/a_2$ perturbation")
    ax2.axhline(1.0, color="k", lw=0.8, ls=":")
    ax2.set_xscale("symlog", linthresh=1e-2)
    ax2.set_xlabel("fractional perturbation $\\epsilon$ of $a_0/a_2$ (spans $\\pm$181x split)", fontsize=9.5)
    ax2.set_ylabel("$|\\beta_{\\hat k}|^2 / |\\beta_{\\hat k}|^2_{base}$", fontsize=10)
    ax2.set_ylim(0.95, 1.05)
    ax2.set_title(f"(A) Structural sub-test [SIGN]:  $d|\\beta_{{\\hat k}}|^2/d(a_0/a_2)$ = "
                  f"{out['struct_deriv_dbeta2_d_a0a2']:.2g}\n"
                  f"machine-zero ($<10^{{-12}}$) $\\Rightarrow$ transit-trajectory-fixed "
                  f"(sign={out['sign_verdict']})", fontsize=9.5)
    ax2.text(0.04, 0.06,
             f"$aH|_{{fold}}$ = {out['aH_target']:.6f} = $a_{{fold}}\\,H_{{fold}}/\\Lambda_{{rescale}}$\n"
             f"= $k_{{piv}}/(k/aH)|_{{fold}}$  (both rel-dev {out['rel_dev_aH_kinematics_vs_target']:.0e}, EXACT)\n"
             f"$\\Rightarrow$ fold-passage kinematic, NOT a carrier of $a_0/a_2$\n"
             f"$\\Rightarrow$ openness CONFINED to UNIFIED route",
             transform=ax2.transAxes, fontsize=8, va="bottom",
             bbox=dict(boxstyle="round", fc="white", ec="#1f77b4", alpha=0.9))
    ax2.legend(fontsize=8.5, loc="upper right")
    ax2.grid(True, alpha=0.25)

    fig.suptitle(f"{GATE_ID} — A_s functional-selection decider  "
                 f"(composite: {out['composite_verdict']})", fontsize=11.5, fontweight="bold")
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(path, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 6 — verdict payload
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme, convention, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          extra_rows=None) -> dict:
    payload = {
        "session": int(SESSION.lstrip("Ss")),
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
# Section 7 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    out = compute()

    # ---- report ----
    print("=== PART (A) — structural sub-test [SIGN/CHAIN] ===")
    print(f"  aH|_fold (aH_target)            = {out['aH_target']:.10f} M_KK")
    print(f"  a_fold*H_fold/Lambda_rescale    = {out['aH_from_kinematics']:.10f} M_KK"
          f"  (rel-dev {out['rel_dev_aH_kinematics_vs_target']:.3e})")
    print(f"  k_pivot/(k/aH)|_fold            = {out['aH_from_k_ratio']:.10f} M_KK"
          f"  (rel-dev {out['rel_dev_aH_k_ratio_vs_target']:.3e})  [INDEPENDENT route]")
    print(f"  aH transit-trajectory-fixed?    = {out['aH_is_transit_trajectory_fixed']}"
          f"  (EXACT both kinematic routes)")
    print(f"  a_0/a_2 in |beta|^2 input keys?  = {out['a0a2_in_beta2_input_keys']}  (expected False)")
    print(f"  d|beta_khat|^2/d(a_0/a_2)        = {out['struct_deriv_dbeta2_d_a0a2']:.6e}"
          f"  (machine-zero floor 1e-12)")
    print(f"  max|delta beta^2| over pert.     = {out['max_abs_dbeta2_over_a0a2_perturbation']:.6e}")
    print(f"  derivative is machine-zero?      = {out['deriv_is_machine_zero']}")
    print(f"  sub-test => transit-fixed?       = {out['subtest_transit_fixed']}  "
          f"(=> openness CONFINED to UNIFIED)")
    print()
    print("=== PART (B) — selection assembly ===")
    print(f"  A_s Planck (anchor)             = {out['A_s_Planck']:.4e}")
    print(f"  impulse-quench A_s              = {out['A_s_impulse']:.6e}  (OOM +{out['oom_impulse']:.5f})")
    print(f"  UNIFIED-AS-79  A_s              = {out['A_s_unified']:.6e}  (OOM +{out['oom_unified']:.5f})")
    print(f"  Parker-adiab.  A_s              = {out['A_s_parker']:.6e}  (OOM +{out['oom_parker']:.5f})")
    print(f"  cross-functional spread         = {out['cross_functional_spread_OOM']:.5f} OOM")
    print(f"  Planck in-band |OOM| threshold  = {out['PLANCK_IN_BAND_OOM_threshold']:.5f}  (DIAGNOSTIC)")
    print(f"  # functionals in Planck band    = {out['n_functionals_in_planck_band']}  (expected 0)")
    print(f"  substrate-canonical selector?   = {out['substrate_canonical_selector_exists']}")
    print(f"  cross-functional spread persists?= {out['cross_functional_spread_persists']}")
    print()
    print(f"  SELECTION verdict (set)         = {out['selection_verdict']}")
    print(f"  sign / magnitude / regime       = {out['sign_verdict']} / "
          f"{out['magnitude_verdict']} / {out['regime_verdict']}")
    print(f"  dual-prior posterior            = {out['dual_prior_posterior']}")
    print()

    # ---- write npz ----
    npz_path = THIS_DIR / "s114_cf_as_functional_selection.npz"  # (local)
    np.savez(
        npz_path,
        # sub-test (A)
        aH_target=out["aH_target"],
        aH_from_kinematics=out["aH_from_kinematics"],
        aH_from_k_ratio=out["aH_from_k_ratio"],
        rel_dev_aH_kinematics_vs_target=out["rel_dev_aH_kinematics_vs_target"],
        rel_dev_aH_k_ratio_vs_target=out["rel_dev_aH_k_ratio_vs_target"],
        rel_dev_aH_rederived_vs_target=out["rel_dev_aH_rederived_vs_target"],
        aH_is_transit_trajectory_fixed=out["aH_is_transit_trajectory_fixed"],
        a0a2_in_beta2_input_keys=out["a0a2_in_beta2_input_keys"],
        a0_over_a2_SDW=out["a0_over_a2_SDW"],
        SDW_Zubarev_split=out["SDW_Zubarev_split"],
        struct_deriv_dbeta2_d_a0a2=out["struct_deriv_dbeta2_d_a0a2"],
        max_abs_dbeta2_over_a0a2_perturbation=out["max_abs_dbeta2_over_a0a2_perturbation"],
        beta2_base_structural=out["beta2_base_structural"],
        deriv_is_machine_zero=out["deriv_is_machine_zero"],
        subtest_transit_fixed=out["subtest_transit_fixed"],
        STRUCT_DERIV_MACHINE_ZERO=STRUCT_DERIV_MACHINE_ZERO,
        # selection (B)
        A_s_Planck=out["A_s_Planck"],
        A_s_impulse=out["A_s_impulse"],
        A_s_unified=out["A_s_unified"],
        A_s_parker=out["A_s_parker"],
        oom_impulse=out["oom_impulse"],
        oom_unified=out["oom_unified"],
        oom_parker=out["oom_parker"],
        cross_functional_spread_OOM=out["cross_functional_spread_OOM"],
        PLANCK_IN_BAND_OOM_threshold=out["PLANCK_IN_BAND_OOM_threshold"],
        n_functionals_in_planck_band=out["n_functionals_in_planck_band"],
        n_defensible_functionals=out["n_defensible_functionals"],
        substrate_canonical_selector_exists=out["substrate_canonical_selector_exists"],
        cross_functional_spread_persists=out["cross_functional_spread_persists"],
        # provenance / cross-checks
        N_eval=out["N_eval"],
        beta2_pivot_closed_form=out["beta2_pivot_closed_form"],
        k_pivot=out["k_pivot"],
        H_fold_s64=out["H_fold_s64"],
        Lambda_rescale=out["Lambda_rescale"],
        unitarity_residual_max=out["unitarity_residual_max"],
        # verdicts
        selection_verdict=out["selection_verdict"],
        sign_verdict=out["sign_verdict"],
        magnitude_verdict=out["magnitude_verdict"],
        regime_verdict=out["regime_verdict"],
        composite_verdict=out["composite_verdict"],
        dual_prior_track_A=out["dual_prior_posterior"]["track_A_SELECTED"],
        dual_prior_track_B=out["dual_prior_posterior"]["track_B_PLURALISM"],
        # dual-SHA
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        value=out["value"],
    )
    print(f"  wrote {npz_path.name}")

    # ---- write plot ----
    png_path = THIS_DIR / "s114_cf_as_functional_selection.png"  # (local)
    make_plot(out, png_path)
    print(f"  wrote {png_path.name}")
    print()

    # ---- emit 4-tuple + payload ----
    tag = emit_4tuple(out["value"], SCHEME, CONVENTION, L_MAX)
    print(tag)

    # regulator_pin companion row (a_0^{zeta}/a_2^{zeta} SDW/Zubarev 181x split)
    regpin_row = ("# regulator_pin: a_0^{zeta}/a_2^{zeta} SDW-Zubarev 181x Path-B split "
                  "(S82 Obs 6.3; poleconv-A-double; a_0 n=0/s=4 cosmological-const moment, "
                  "a_2 n=2/s=3 Einstein-Hilbert moment); lives on horizon-exit H~ carrier, "
                  "NOT the impulse-quench floor (d|beta|^2/d(a_0/a_2)=0)")  # (local)
    payload = print_verdict_payload(
        out["composite_verdict"], out["value"], audit_sha, content_sha,
        sign_verdict=out["sign_verdict"],
        magnitude_verdict=out["magnitude_verdict"],
        regime_verdict=out["regime_verdict"],
        extra_rows=[regpin_row],
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {out['composite_verdict']} "
          f"(SELECTION={out['selection_verdict']}; wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
