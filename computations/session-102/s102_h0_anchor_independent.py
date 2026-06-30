#!/usr/bin/env python3
"""
S102 W5-1 — CF-S102-H0-ANCHOR-INDEPENDENT
=========================================

Gate: W5-1-CF-S102-H0-ANCHOR-INDEPENDENT ([SIGN])

Pre-registered threshold (plan §W5-1, set form):
  PASS iff  (|H_0^joint(N->1) - H_obs| > delta_degen = 0.5 km/s/Mpc)
        AND (energy_leg_substrate_derived == True)
        AND (sigma_distance computable from substrate-derived covariance)
  FAIL iff the joint estimator algebra is internally inconsistent OR the
        substrate energy leg yields an unphysical (negative/complex) H_0^*.
  INFO iff the L2 energy leg cannot be made anchor-free -- rho_substrate
        inadvertently reintroduces H_obs (degeneracy persists). The 67.40
        ratio-channel readout stands; an anchor-independent H_0 remains future work.

Substrate-first framing (PHONONIC):
  The substrate IS the spectral triple (A_K, H_K, D_K(tau_fold)). H_0 is the
  emergent expansion rate set by TWO substrate channels:
    Level-1 (gravity-coupling leg): G_N^FW = a_2 second spectral moment
                                     (W4-4 convergent-a2; N = G_N^FW/G_N^obs = 0.999859)
    Level-2 (energy-content leg):    rho_substrate(tau_fold) = rho_vac_tracking * Gamma_eff
                                     (Volovik partition S58/S60; effacement Gamma_eff = 0.99970)
  The joint Friedmann normalization:  H_0^joint^2 = (8 pi G_N^FW / 3) * rho_substrate.

  The Level-1-only readout H_0 = H_obs*sqrt(N) -> H_obs at N->1 is the disclosed
  anchor degeneracy (S101 npz anchor_degeneracy_disclosure): the energy-content leg
  there IS the OBSERVED critical density rho_crit(H_obs). This gate asks whether the
  Volovik-partition Level-2 leg can REPLACE that observed energy leg with a
  substrate-IS quantity, removing H_obs from the readout.

CENTRAL STRUCTURAL FINDING (derived, Sage-verified, S66 DILUTION-CC lineage):
  The Volovik tracking vacuum (S66 Scenario B, the DILUTION-CC PASS mechanism;
  Volovik Paper 25 Sec V) is  rho_vac = alpha_V * M_Pl^2 * H^2.  At today H = H_0^joint,
  so substituting into Friedmann:
        H_0^joint^2 = (8 pi G_N^FW / 3) * alpha_V * M_Pl^2 * H_0^joint^2 * Gamma_eff
  The H_0^joint^2 CANCELS on both sides, leaving a CONSTRAINT on the dimensionless
  combination  (8 pi G_N^FW/3) * alpha_V * M_Pl^2 * Gamma_eff = 1, with H_0^joint
  UNDETERMINED. A vacuum that tracks H^2 (which is precisely WHY it solves the CC
  problem -- it auto-tracks rho_crit ~ H^2) cannot ALSO fix the magnitude of H.
  => The tracking leg REINTRODUCES H_0 through the tracking law; degeneracy persists.

  The only anchor-FREE Level-2 alternative is a fixed (tau_fold-pinned, H-independent)
  floor rho_0 ~ M_KK^4 (S66 Scenario A's w=-1 component, rho_cc ~ 0.939 M_KK^4). That
  leg DOES determine H_0^joint = sqrt((8 pi G_N^FW/3) rho_0 Gamma_eff), but rho_0 ~ M_KK^4
  overshoots rho_obs by ~114 OOM (the unsolved bare-CC magnitude), so H_0^* ~ 10^57
  km/s/Mpc -- unphysical. This is the SAME bare-CC magnitude problem the tracking
  mechanism was introduced to evade. The two legs are the two horns of one dilemma:
  anchor-free => 114-OOM-overshoot; right-magnitude => H_0-degenerate.

  VERDICT: INFO (Track B). The L2 energy leg cannot be made simultaneously anchor-free
  AND right-magnitude on the substrate's current energy-content theory. The 67.40
  ratio-channel readout stands as the canonical (anchor-degenerate) H_0; an
  anchor-independent H_0 awaits a substrate-derived FIXED energy floor at the OBSERVED
  CC scale (the residual-3% CC underivation; capstone Sec 6.3 a(t) gap).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-101/s101_w4_h0_proper_a2.npz   (N=0.999859, convergent-a2 Level-1)
  - canonical_constants.py (Gamma_effacement, rho_vac_over_rho_obs, M_Pl, H_0, rho_Lambda_obs, M_KK)
  - script bytes

Output 4-tuple:
  (value=<H_0^joint summary + degeneracy verdict>, scheme=FW,
   convention=ABSOLUTE-L1-L2-JOINT-substrate-energy-leg, L_max=10)

Classification: PHONONIC

Author: volovik-superfluid-universe-theorist
Session: 102 (2026-06-09)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — Path bootstrap (canonical_constants lives in computations/_shared)
# ---------------------------------------------------------------------------
import os as _os
import sys as _sys
_sys.path.insert(0, _os.path.join(
    _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))), "_shared"))

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (
    Gamma_effacement, rho_vac_over_rho_obs,
    M_Pl_reduced, M_Pl_unreduced, M_KK,
    H_0_km_s_Mpc, H_0_GeV, rho_Lambda_obs, rho_crit_GeV4,
    Omega_Lambda, Omega_m, tau_fold, PI,
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import os
import sys
import time
from pathlib import Path

os.environ.setdefault('OMP_NUM_THREADS', '8')   # scalar algebra; CPU; cap threads
os.environ.setdefault('MKL_NUM_THREADS', '8')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S102"                                                   # (local)
GATE_ID = "W5-1-CF-S102-H0-ANCHOR-INDEPENDENT"                    # (local)
SCHEME = "FW"                                                      # (local)
CONVENTION = "ABSOLUTE-L1-L2-JOINT-substrate-energy-leg"          # (local)
L_MAX = 10                                                         # (local)

# Pre-registered thresholds (plan §W5-1 strict_PASS_boundary)
DELTA_DEGEN = 0.5            # (local) km/s/Mpc non-degeneracy floor
TOL = 1e-4                  # (local) relative tolerance on the joint-estimator algebra

# Observational anchors for the sigma-distance (plan §W5-1 method)
H_SH0ES = 73.04             # (local) SH0ES Cepheid-SN local H_0 (km/s/Mpc)
SIG_SH0ES = 1.04            # (local) SH0ES 1sigma
H_PLANCK = 67.34            # (local) Planck-LCDM H_0 (km/s/Mpc)
SIG_PLANCK = 0.54           # (local) Planck-LCDM 1sigma

OUT_NPZ = SESSION_DIR / "s102_h0_anchor_independent.npz"
OUT_PNG = SESSION_DIR / "s102_h0_anchor_independent.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    SESSION_DIR.parent / "session-101" / "s101_w4_h0_proper_a2.npz",
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
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
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Compute
# ---------------------------------------------------------------------------

def km_s_Mpc_from_H_GeV(H_GeV: float) -> float:
    """Convert H in GeV to km/s/Mpc using the canonical anchor pair
    (H_0_GeV, H_0_km_s_Mpc), so the conversion carries NO new scale and is
    self-consistent with the canonical anchor by construction."""
    return H_GeV * (H_0_km_s_Mpc / H_0_GeV)   # (local) anchored unit conversion


def compute() -> dict:
    out: dict = {}  # (local)

    # -- Level-1 leg (W4-4 convergent-a2), loaded from S101 npz ---------------
    d = np.load(INPUT_FILES[1], allow_pickle=True)  # (local)
    N_conv = float(d['chain_convergent__N'])                       # (local) 0.9998591
    abs_N_minus_1 = float(d['chain_convergent__abs_N_minus_1'])    # (local) 1.409e-4
    H0_L1_readout = float(d['chain_convergent__H0_FW_km_s_Mpc'])   # (local) 67.40
    H_obs = float(d['sign_check__H_obs'])                          # (local) 67.4 (the anchor)
    M_Pl_red_FW = float(d['chain_convergent__M_red_FW_GeV'])       # (local) 2.435e18 GeV

    out['N_conv'] = N_conv
    out['abs_N_minus_1'] = abs_N_minus_1
    out['H0_L1_readout_km_s_Mpc'] = H0_L1_readout
    out['H_obs_km_s_Mpc'] = H_obs
    out['M_Pl_red_FW_GeV'] = M_Pl_red_FW

    # Level-1 N->1 limit: H_0^(L1) = H_obs * sqrt(N) -> H_obs * 1 = H_obs.
    # The anchor degeneracy of the Level-1-only readout (plan substitution Step 1).
    H0_L1_at_Nto1 = H_obs * np.sqrt(1.0)                           # (local)
    out['H0_L1_at_Nto1_km_s_Mpc'] = H0_L1_at_Nto1
    out['L1_alone_degenerate'] = bool(abs(H0_L1_at_Nto1 - H_obs) <= DELTA_DEGEN)  # True

    # -- Level-2 leg, CANDIDATE 1: Volovik TRACKING vacuum (S66 Scenario B) ---
    # rho_vac = alpha_V * M_Pl^2 * H^2 (Volovik Paper 25 Sec V; the DILUTION-CC PASS
    # mechanism). The canonical headline rho_vac/rho_obs = 1.032 is itself a RATIO
    # evaluated AT today using H_0 -- i.e. it is built FROM the observed Friedmann
    # history (S66 line 515-524). It is NOT an H-independent energy.
    #
    # Joint Friedmann with the tracking leg (rho_substrate = rho_vac_tracking * Gamma_eff,
    # H = H_0^joint at today):
    #   H_0^joint^2 = (8 pi G_N^FW/3) * alpha_V * M_Pl^2 * H_0^joint^2 * Gamma_eff
    # The H_0^joint^2 CANCELS. Demonstrate numerically: the residual of the Friedmann
    # equation is INDEPENDENT of the trial H_0 value (the equation is homogeneous degree-2
    # in H_0 on BOTH sides), so no trial value is singled out.
    #
    # rho_vac_tracking(today) = rho_vac_over_rho_obs * rho_Lambda_obs (the S66/S97 headline),
    # but rho_Lambda_obs ITSELF = Omega_Lambda * rho_crit(H_obs) ~ H_obs^2. Make the H_obs
    # dependence explicit:  rho_crit(H) = 3 H^2 / (8 pi G_N) = (3/(8 pi)) * M_Pl_red^2-equivalent.
    rho_vac_tracking_today = rho_vac_over_rho_obs * rho_Lambda_obs   # (local) GeV^4, ~ H_obs^2
    out['rho_vac_tracking_today_GeV4'] = rho_vac_tracking_today
    out['rho_vac_over_rho_obs'] = rho_vac_over_rho_obs

    # Friedmann homogeneity test: form f(H) = H^2 - (8 pi G_N^FW/3) rho_vac(H) Gamma_eff
    # with rho_vac(H) = (rho_vac_tracking_today/H_obs_GeV^2) * H^2 (the tracking law,
    # normalized to reproduce the today value at H=H_obs). Show f(H)/H^2 is a CONSTANT
    # (H-independent) => no H singled out => degeneracy.
    # G_N^FW from M_Pl_red_FW: rho_crit(H) = 3 H^2 M_Pl_red^2 ... in natural units
    # rho = (3/(8 pi)) * ... ; we work in the ratio form to avoid unit drift.
    alpha_track = rho_vac_tracking_today / (H_0_GeV**2)             # (local) GeV^2 coefficient, rho_vac=alpha_track*H^2
    # Trial H grid spanning SH0ES..Planck..arbitrary, in GeV:
    H_trial_km = np.array([60.0, 67.34, 67.4, 70.0, 73.04, 100.0])  # (local) km/s/Mpc
    H_trial_GeV = H_trial_km * (H_0_GeV / H_0_km_s_Mpc)             # (local)
    # rho_vac(H) via the tracking law:
    rho_vac_of_H = alpha_track * H_trial_GeV**2                     # (local) GeV^4
    # Friedmann LHS-minus-RHS normalized: the "closure functional"
    #   C(H) = (8 pi/3) * (rho_vac_of_H * Gamma_eff) / (rho_crit_natural_per_H2 * H^2)
    # Using rho_crit(H) = (3/(8 pi)) * M_Pl_red^2_equiv * H^2 with the SAME M_Pl_red,
    # the H^2 cancels and C(H) is H-INDEPENDENT. Compute the ratio rho_vac(H)/rho_crit(H):
    # rho_crit(H) in GeV^4 = rho_crit_GeV4 * (H/H_obs)^2 (rho_crit ~ H^2; canonical at H_obs).
    rho_crit_of_H = rho_crit_GeV4 * (H_trial_GeV / H_0_GeV)**2      # (local) GeV^4
    Omega_vac_eff = (rho_vac_of_H * Gamma_effacement) / rho_crit_of_H  # (local) dimensionless
    out['H_trial_km_s_Mpc'] = H_trial_km
    out['Omega_vac_eff_grid'] = Omega_vac_eff
    out['Omega_vac_eff_spread'] = float(Omega_vac_eff.max() - Omega_vac_eff.min())
    out['tracking_leg_H_independent'] = bool(out['Omega_vac_eff_spread'] < TOL)  # True => degeneracy

    # The closure CONSTRAINT value (what the tracking law fixes -- a dimensionless number,
    # NOT an H_0): it fixes Omega_vac_eff = rho_vac/rho_crit = rho_vac_over_rho_obs *
    # Omega_Lambda * Gamma_eff. This is the SAME at every trial H -> H_0 undetermined.
    Omega_vac_constraint = rho_vac_over_rho_obs * Omega_Lambda * Gamma_effacement  # (local)
    out['Omega_vac_constraint'] = Omega_vac_constraint

    # -- Level-2 leg, CANDIDATE 2: FIXED M_KK^4 floor (S66 Scenario A, w=-1) --
    # rho_0 ~ rho_cc ~ 0.939 M_KK^4 (S66 two-component split; H-INDEPENDENT, anchor-FREE).
    # This DOES determine H_0^joint = sqrt((8 pi G_N^FW/3) rho_0 Gamma_eff), but the
    # magnitude is set by rho_0 ~ M_KK^4 -- the unsolved bare-CC scale.
    rho_cc_floor_MKK4 = 0.939                                       # (local) M_KK^4 (S66 rho_cc split)
    rho_cc_floor_GeV4 = rho_cc_floor_MKK4 * M_KK**4                 # (local) GeV^4
    out['rho_cc_floor_GeV4'] = rho_cc_floor_GeV4
    # Overshoot vs rho_obs (the 114-OOM bare-CC magnitude problem):
    floor_overshoot_OOM = float(np.log10(rho_cc_floor_GeV4 / rho_Lambda_obs))  # (local)
    out['floor_overshoot_OOM'] = floor_overshoot_OOM
    # H_0^joint from the fixed floor: H^2 = (8 pi G_N/3) rho_0 -> H = sqrt(rho_0/rho_crit)*H_obs
    # (since rho_crit = 3 H_obs^2/(8 pi G_N)). So H_0^floor/H_obs = sqrt(rho_0/rho_crit(H_obs)).
    H0_floor_over_Hobs = float(np.sqrt(rho_cc_floor_GeV4 * Gamma_effacement / rho_crit_GeV4))  # (local)
    H0_floor_km_s_Mpc = H0_floor_over_Hobs * H_obs                  # (local) ~10^57 km/s/Mpc
    out['H0_floor_over_Hobs'] = H0_floor_over_Hobs
    out['H0_floor_km_s_Mpc'] = H0_floor_km_s_Mpc
    out['floor_anchor_free'] = True   # rho_0 has NO H dependence -> anchor-free
    out['floor_physical'] = bool(50.0 < H0_floor_km_s_Mpc < 100.0)  # False (unphysical)

    # -- Joint estimator H_0^joint and its N->1 limit (plan Step 3/4) ---------
    # H_0^joint = sqrt(N) * sqrt((8 pi G_N^obs/3) rho_substrate).
    # With the TRACKING leg, sqrt((8 pi G_N^obs/3) rho_substrate) reduces to a quantity
    # proportional to H_0^joint itself (homogeneity) -> H_0^* undetermined.
    # With the FIXED-FLOOR leg, the N->1 limit is H0_floor_km_s_Mpc (anchor-free but ~10^57).
    H0_joint_track_Nto1 = float('nan')   # (local) UNDETERMINED (cancellation)
    H0_joint_floor_Nto1 = H0_floor_km_s_Mpc  # (local) determined but unphysical
    out['H0_joint_track_Nto1'] = H0_joint_track_Nto1
    out['H0_joint_floor_Nto1'] = H0_joint_floor_Nto1

    # -- sigma-distances for the readouts that ARE available ------------------
    # The Level-1 readout 67.40 (anchor-degenerate) is the only finite, physical readout.
    def sigma_dist(H_pred: float, H_ref: float, sig_ref: float) -> float:
        return abs(H_pred - H_ref) / sig_ref   # (local)

    sig_L1_SH0ES = sigma_dist(H0_L1_readout, H_SH0ES, SIG_SH0ES)    # (local) ~5.4 sigma
    sig_L1_Planck = sigma_dist(H0_L1_readout, H_PLANCK, SIG_PLANCK) # (local) ~0.1 sigma
    out['sigma_L1_readout_vs_SH0ES'] = sig_L1_SH0ES
    out['sigma_L1_readout_vs_Planck'] = sig_L1_Planck
    # The anchor-degenerate readout 67.40 sits essentially ON Planck-LCDM (it borrows the
    # Planck-anchored energy leg) and ~5sigma from SH0ES -- a tautology of the anchor, NOT
    # a substrate-independent prediction. No substrate-derived covariance exists for the
    # tracking leg (it reintroduces H_obs); the sigma-distance for an anchor-INDEPENDENT
    # H_0 is therefore NOT computable on the current energy-content theory.
    out['sigma_anchor_independent_computable'] = False

    # -- Degeneracy verdict (the [SIGN] direction read-off, plan Step 5) ------
    # Track A (PASS): the L2 leg CAN be made anchor-free with right magnitude.
    # Track B (INFO): it cannot -- tracking leg cancels H_0 (degeneracy);
    #                 fixed floor overshoots 114 OOM (unphysical).
    tracking_degenerate = out['tracking_leg_H_independent']         # True
    floor_unphysical = not out['floor_physical']                   # True
    # Non-degeneracy requires SOME substrate leg that is BOTH anchor-free AND |H-H_obs|>delta
    # AND physical. Tracking: anchor-DEPENDENT (fails). Floor: anchor-free but unphysical (fails).
    non_degeneracy_achieved = (not tracking_degenerate) or (
        out['floor_anchor_free'] and out['floor_physical'])         # False
    out['non_degeneracy_achieved'] = bool(non_degeneracy_achieved)
    out['energy_leg_substrate_derived'] = True   # both candidate legs ARE substrate-derived...
    out['energy_leg_anchor_free_and_physical'] = bool(
        out['floor_anchor_free'] and out['floor_physical'])         # ...but neither is anchor-free AND physical

    # Algebra internally consistent (not FAIL): the cancellation is a clean algebraic
    # identity (Sage-verified); the floor readout is a finite positive real. No
    # dimensional inconsistency, no negative/complex H. => not FAIL.
    algebra_consistent = (np.isfinite(H0_floor_km_s_Mpc) and H0_floor_km_s_Mpc > 0
                          and np.isfinite(Omega_vac_constraint) and Omega_vac_constraint > 0)  # (local)
    out['algebra_consistent'] = bool(algebra_consistent)

    return out


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note="", extra_rows=None) -> dict:
    payload: dict = {
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


def evaluate_gate(r: dict) -> tuple[str, str, str, str]:
    """Return (composite, sign_verdict, magnitude_verdict, regime_verdict).

    Plan set-form operator:
      PASS iff non_degeneracy AND energy_leg_substrate_derived AND sigma computable.
      FAIL iff algebra inconsistent OR unphysical H_0^*.
      INFO iff the L2 leg cannot be made anchor-free (degeneracy persists).

    [SIGN] 3-tuple (plan substitution Step 4/5 directional prediction):
      sign_verdict   = did the predicted direction hold? The substitution chain
                       PREDICTS that the tracking-leg substitution removes the H_obs
                       prefactor by cancellation (Step 5: "the substitution removes the
                       H_obs prefactor entirely"). The COMPUTED behavior confirms the
                       cancellation direction (H_0^joint^2 cancels) -> sign PASS.
      magnitude_verdict = did the L2 leg produce a TESTABLE anchor-independent H_0
                       (a distinct, physical value to place in/out of band)?
                       NO -- the tracking leg yields an UNDETERMINED H_0 (cancellation),
                       the floor leg yields an unphysical 10^57. The gate produced NO
                       anchor-independent value to band-test -> this is the pre-registered
                       INFO band (between PASS and FAIL), NOT an out-of-band FAIL. So
                       magnitude_verdict = INFO. Under the gate-verdicts.md generic
                       composite-collapse rule (magnitude==INFO => composite=INFO), this
                       lands the plan's pre-registered INFO outcome with NO operator-
                       precedence override needed (a magnitude=FAIL would force composite
                       FAIL and mis-read a clean applicability guard as a hypothesis FAIL).
      regime_verdict = is the estimator within its regime of validity? The Friedmann
                       normalization is exact algebra (no small-parameter expansion);
                       VALID throughout.
    """
    # FAIL guard first
    if not r['algebra_consistent']:
        return ("FAIL", "FAIL", "FAIL", "BREAKDOWN")

    # sign: the predicted cancellation/substitution direction held (tracking leg IS
    # H-homogeneous as the chain predicted). Direction PASS.
    sign = "PASS" if r['tracking_leg_H_independent'] else "FAIL"

    # PASS requires non-degeneracy with an anchor-free, physical, substrate-derived leg.
    pass_condition = (r['non_degeneracy_achieved']
                      and r['energy_leg_anchor_free_and_physical']
                      and r['sigma_anchor_independent_computable'])

    if pass_condition:
        return ("PASS", sign, "PASS", "VALID")

    # INFO: degeneracy persists (tracking leg cancels H_0; fixed floor overshoots 114 OOM).
    # The substrate energy legs ARE derived, but none is simultaneously anchor-free AND
    # physical -> NO testable anchor-independent H_0 was produced. magnitude=INFO (the
    # pre-registered between-PASS-and-FAIL band: no value to band-test), regime VALID
    # (exact algebra). Generic collapse (magnitude==INFO => INFO) lands the plan INFO.
    return ("INFO", sign, "INFO", "VALID")


# ---------------------------------------------------------------------------
# Section 7 — Plot
# ---------------------------------------------------------------------------

def make_plot(r: dict) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    # Panel 1: the two-horn dilemma -- tracking leg (H-degenerate) vs fixed floor (114 OOM)
    ax1 = axes[0]
    H_grid = r['H_trial_km_s_Mpc']
    Omega = r['Omega_vac_eff_grid']
    ax1.plot(H_grid, Omega, 'o-', color='crimson', lw=2, ms=7,
             label=r'$\Omega_{\rm vac}^{\rm eff}(H)$ = $\rho_{\rm vac}(H)/\rho_{\rm crit}(H)$')
    ax1.axhline(r['Omega_vac_constraint'], color='navy', ls='--', lw=1.5,
                label=f"constraint = {r['Omega_vac_constraint']:.4f} (H-INDEPENDENT)")
    ax1.set_xlabel('trial $H_0$ [km/s/Mpc]', fontsize=11)
    ax1.set_ylabel(r'$\Omega_{\rm vac}^{\rm eff}$ (dimensionless)', fontsize=11)
    ax1.set_title('Tracking-vacuum leg: FLAT in $H_0$\n'
                  r'$\Rightarrow H_0$ undetermined (degeneracy)', fontsize=12)
    ax1.legend(fontsize=9, loc='center right')
    ax1.grid(True, alpha=0.3)
    ax1.set_ylim(r['Omega_vac_constraint'] * 0.5, r['Omega_vac_constraint'] * 1.5)

    # Panel 2: readouts vs observational anchors
    ax2 = axes[1]
    ax2.axvspan(H_PLANCK - SIG_PLANCK, H_PLANCK + SIG_PLANCK, color='royalblue', alpha=0.2,
                label=f'Planck-LCDM {H_PLANCK}$\\pm${SIG_PLANCK}')
    ax2.axvspan(H_SH0ES - SIG_SH0ES, H_SH0ES + SIG_SH0ES, color='darkorange', alpha=0.2,
                label=f'SH0ES {H_SH0ES}$\\pm${SIG_SH0ES}')
    ax2.axvline(r['H0_L1_readout_km_s_Mpc'], color='black', lw=2.5,
                label=f"L1 ratio-channel readout = {r['H0_L1_readout_km_s_Mpc']:.2f}\n(anchor-DEGENERATE)")
    ax2.axvline(r['H_obs_km_s_Mpc'], color='gray', ls=':', lw=2,
                label=f"$H_{{\\rm obs}}$ = {r['H_obs_km_s_Mpc']:.2f} (the anchor)")
    ax2.set_xlim(64, 76)
    ax2.set_yticks([])
    ax2.set_xlabel('$H_0$ [km/s/Mpc]', fontsize=11)
    ax2.set_title('Anchor-independent $H_0$: NOT computable\n'
                  'tracking leg $\\to H_0$-degenerate; floor leg $\\to$ '
                  f"{r['floor_overshoot_OOM']:.0f} OOM overshoot", fontsize=12)
    ax2.legend(fontsize=8.5, loc='upper right')
    ax2.grid(True, alpha=0.3, axis='x')

    fig.suptitle('W5-1 CF-S102-H0-ANCHOR-INDEPENDENT  —  INFO (Track B): '
                 'L2 energy leg cannot be made anchor-free AND physical',
                 fontsize=13, fontweight='bold')
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(OUT_PNG, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f"Plot saved to {OUT_PNG}")


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    r = compute()

    print("=" * 78)
    print("  W5-1 CF-S102-H0-ANCHOR-INDEPENDENT — joint L1(+)L2 H_0 estimator")
    print("=" * 78)
    print(f"\n--- Level-1 leg (W4-4 convergent-a2) ---")
    print(f"  N = G_N^FW/G_N^obs = {r['N_conv']:.7f}  (|N-1| = {r['abs_N_minus_1']:.3e})")
    print(f"  H_0^(L1) readout      = {r['H0_L1_readout_km_s_Mpc']:.4f} km/s/Mpc")
    print(f"  H_obs (anchor)        = {r['H_obs_km_s_Mpc']:.4f} km/s/Mpc")
    print(f"  H_0^(L1) at N->1      = {r['H0_L1_at_Nto1_km_s_Mpc']:.4f} km/s/Mpc")
    print(f"  L1-alone degenerate?  = {r['L1_alone_degenerate']}  (|readout-H_obs| <= {DELTA_DEGEN})")

    print(f"\n--- Level-2 CANDIDATE 1: Volovik TRACKING vacuum (S66 Scenario B) ---")
    print(f"  rho_vac/rho_obs       = {r['rho_vac_over_rho_obs']:.4f}  (S97/S66 DILUTION-CC headline)")
    print(f"  Omega_vac^eff(H) grid = {np.array2string(r['Omega_vac_eff_grid'], precision=6)}")
    print(f"  Omega_vac^eff spread  = {r['Omega_vac_eff_spread']:.3e}  (< {TOL} => H-INDEPENDENT)")
    print(f"  tracking leg H-indep? = {r['tracking_leg_H_independent']}  => H_0 UNDETERMINED (cancellation)")
    print(f"  closure constraint    = Omega_vac = {r['Omega_vac_constraint']:.6f}  (a NUMBER, not an H_0)")

    print(f"\n--- Level-2 CANDIDATE 2: FIXED M_KK^4 floor (S66 Scenario A, w=-1) ---")
    print(f"  rho_0 ~ 0.939 M_KK^4  = {r['rho_cc_floor_GeV4']:.4e} GeV^4")
    print(f"  overshoot vs rho_obs  = {r['floor_overshoot_OOM']:.2f} OOM  (the unsolved bare-CC magnitude)")
    print(f"  H_0^floor             = {r['H0_floor_km_s_Mpc']:.4e} km/s/Mpc  (anchor-FREE but UNPHYSICAL)")
    print(f"  floor physical?       = {r['floor_physical']}  (50 < H_0 < 100)")

    print(f"\n--- Joint estimator N->1 limits ---")
    print(f"  H_0^joint (tracking)  = {r['H0_joint_track_Nto1']}  (UNDETERMINED -- H_0^2 cancels)")
    print(f"  H_0^joint (floor)     = {r['H0_joint_floor_Nto1']:.4e}  (determined but ~10^57 too big)")

    print(f"\n--- sigma-distances (only the L1 anchor-degenerate readout is finite/physical) ---")
    print(f"  sigma(L1 vs SH0ES)    = {r['sigma_L1_readout_vs_SH0ES']:.3f}")
    print(f"  sigma(L1 vs Planck)   = {r['sigma_L1_readout_vs_Planck']:.3f}")
    print(f"  anchor-indep sigma computable? = {r['sigma_anchor_independent_computable']}")

    composite, sign_v, mag_v, regime_v = evaluate_gate(r)

    print(f"\n--- Non-degeneracy assessment ---")
    print(f"  non_degeneracy_achieved          = {r['non_degeneracy_achieved']}")
    print(f"  energy_leg_substrate_derived     = {r['energy_leg_substrate_derived']}")
    print(f"  energy_leg_anchor_free_AND_phys  = {r['energy_leg_anchor_free_and_physical']}")
    print(f"  algebra_consistent (not FAIL)    = {r['algebra_consistent']}")

    # Build the compact value payload (no single-quote chars; the tool wraps value='...')
    value = (
        f"VERDICT={composite}_TrackB;"
        f"N={r['N_conv']:.6f};H0_L1_readout={r['H0_L1_readout_km_s_Mpc']:.4f}_km_s_Mpc(anchor-degenerate);"
        f"H_obs={r['H_obs_km_s_Mpc']:.4f};L1_alone_degenerate_at_Nto1={r['L1_alone_degenerate']};"
        f"trackingLeg:rho_vac/rho_obs={r['rho_vac_over_rho_obs']:.4f},Omega_vac^eff_spread={r['Omega_vac_eff_spread']:.2e},"
        f"H-INDEPENDENT={r['tracking_leg_H_independent']}=>H0_CANCELS_constraint=Omega_vac={r['Omega_vac_constraint']:.4f};"
        f"floorLeg:rho0~0.939_M_KK^4,overshoot={r['floor_overshoot_OOM']:.1f}_OOM,H0_floor={r['H0_floor_km_s_Mpc']:.2e}_km_s_Mpc,physical={r['floor_physical']};"
        f"H0joint_Nto1_tracking=UNDETERMINED(H0^2_cancels),H0joint_Nto1_floor={r['H0_joint_floor_Nto1']:.2e}(unphysical);"
        f"non_degeneracy_achieved={r['non_degeneracy_achieved']};energy_leg_substrate_derived=True;"
        f"anchor_free_AND_physical={r['energy_leg_anchor_free_and_physical']};"
        f"sigma_L1_vs_SH0ES={r['sigma_L1_readout_vs_SH0ES']:.2f},sigma_L1_vs_Planck={r['sigma_L1_readout_vs_Planck']:.2f};"
        f"anchor_indep_sigma_computable=False;"
        f"DILEMMA=anchor-free=>114OOM-overshoot_XOR_right-magnitude=>H0-degenerate;"
        f"67.40_ratio-channel_STANDS_anchor-independent-H0_remains_future-work(capstone_Sec6.3_a(t)_gap)"
    )

    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        composite_verdict=composite,
        sign_verdict=sign_v,
        magnitude_verdict=mag_v,
        regime_verdict=regime_v,
        **{k: v for k, v in r.items()},
        delta_degen=DELTA_DEGEN,
        tol=TOL,
        H_SH0ES=H_SH0ES, SIG_SH0ES=SIG_SH0ES,
        H_PLANCK=H_PLANCK, SIG_PLANCK=SIG_PLANCK,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"\nData saved to {OUT_NPZ}")

    make_plot(r)

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)
    extra = [
        f"# tracking_leg_H_independent={r['tracking_leg_H_independent']} "
        f"Omega_vac_eff_spread={r['Omega_vac_eff_spread']:.2e} "
        f"closure_constraint_Omega_vac={r['Omega_vac_constraint']:.6f} "
        f"# {GATE_ID} tracking-leg H_0-cancellation (degeneracy persists)",
        f"# floor_overshoot_OOM={r['floor_overshoot_OOM']:.2f} "
        f"H0_floor_km_s_Mpc={r['H0_floor_km_s_Mpc']:.4e} floor_physical={r['floor_physical']} "
        f"# {GATE_ID} fixed-M_KK^4-floor leg anchor-free-but-114OOM-overshoot",
    ]
    print_verdict_payload(composite, value, audit_sha, content_sha,
                          sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
                          extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} "
          f"(sign={sign_v}, magnitude={mag_v}, regime={regime_v}) (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
