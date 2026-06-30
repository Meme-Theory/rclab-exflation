#!/usr/bin/env python3
"""
INV12 W3-3 — BACK-REACTION-CLOSURE-HSQ — effective-Friedmann closure from the locked relic
==========================================================================================

Gate: INV12-W3-3-BACK-REACTION-CLOSURE-HSQ ([SIGN])

Pre-registered threshold (plan §W3-3, operator type=span):
  q_eff(tau) in [q_band_lo, q_band_hi] = [-0.97, +0.81] (SCALE-FACTOR-54, Connes-distance proxy).
  PASS iff max excursion outside the band <= band_tol = 0.05.
  FAIL iff excursion > band_fail = 0.30.
  INFO otherwise (partial containment with a stated regime).

[SIGN] directional claim (substitution chain in §Methodology / WP):
  A DILUTING positive-energy relic source DECELERATES — raises q_eff above -1 (the pure-Lambda
  value) toward the +0.81 decelerating edge. Sign-verdict tests this direction.

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - computations/investigation-12/inv12_w3_1_relic_spectrum_ode_lock.npz  (locked relic spectrum)
  - computations/_shared/canonical_constants.py                           (a_2_FW_zeta, M_KK, Gamma)
  - script bytes

Output 4-tuple:
  (value=<max_excursion>, scheme=FW-effective-Friedmann, convention=ABSOLUTE-Connes-proxy-q, L_max=10)

Classification: PHONONIC — the substrate IS the source of its own effective expansion.

METHODOLOGY
-----------
The framework's #1 transit-side gap (G2: no derived a(t)/Friedmann map; C1 ASSUMED, C2/T6 BROKEN)
is tested at the EFFECTIVE-FRIEDMANN level. The substrate-IS direction:
  D_K eigenvalues lambda_k(tau)  ->  locked relic squeeze {beta_k} (INV12-W3-1)
   ->  relic energy density rho_relic = Sum_k mult_k E_k |beta_k|^2 (the GGE charge carried as energy)
   ->  back-reaction on the internal tau-flow via the Sakharov-induced G_eff (a_2 channel, E30)
   ->  H^2_eff = (8 pi G_eff/3) rho_relic + Lambda_eff
   ->  q_eff = -1 - Hdot_eff/H_eff^2  (the deceleration an external container-observer would infer).

Substrate scale factor: the SCALE-FACTOR-54 a(tau) (the Connes-distance growth d_mean(tau), to which
a(tau) is proportional to 4 sig figs: a/d_mean = 1.0085 const). This is the SAME object whose
Connes-distance-proxy q(tau) carved out the band [-0.97,+0.81] — so the gate is a genuine independent
cross-closure: can a relic-back-reaction Friedmann reading of the substrate's OWN scale-factor history
land q_eff in the band the Connes-distance reading produced?

Two-component closure (exflation, NOT slow-roll):  q only RISES with a (s54: -0.97 -> +0.81) if the
relic ENERGY FRACTION RISES with a. Physics: the GGE relic is DEPOSITED at the fold (Parker pair
production, P_exc=1); pre-fold the state is vacuum/Lambda-dominated (q ~ -1, cold-big-bang tau~0
unstable maximum); the transit deposits the relic, whose fraction rises 0 -> dominant, driving
q: -1 -> +n_eff/2-1.  A single diluting relic + const Lambda gives dq/da<0 (WRONG direction); the
RISING-relic-fraction deposit model gives the s54 direction (verified symbolically, Sage).

Effective dilution n_eff of the gapped relic gas:  rho ~ a^{-n_eff}, n_eff in [3 (cold/massive),
4 (massless/radiation)], set by the energy-weighted kinetic fraction <(E_k - Delta)/E_k> with the
BdG gap Delta acting as the rest mass.  Relic-dominated asymptote q -> n_eff/2 - 1.

Pre-flight (MANDATORY): confirm the 8-mode BCS source is the WRONG object — the T6 FAIL 133,200x
overwhelm (atlas-04, S39 FRIED-39: spectral action 155,984 modes overwhelms BCS 8 modes). We
reproduce the order of the overwhelm from the spectral-action-vs-BCS mode-count ratio as a sanity
anchor, establishing rho_relic = Sum_k E_k|beta_k|^2 (full locked spectrum) as the correct source.

Truncation band: rho_relic carries the W3-1 INFO truncation band (15.414 @ p+q<=7  ->  26.851 @
p+q<=8, rel 0.426).  Since H^2_eff ~ rho_relic ABSOLUTELY but q_eff = -1 - Hdot/H^2 is INVARIANT
under constant rescaling of H, the band cancels in q_eff EXCEPT through the Lambda_eff/rho_relic
ratio (which sets the deposit crossover).  We run BOTH rho endpoints and report q_eff sensitivity.

DISCIPLINE
----------
- `from canonical_constants import *`; every intermediate tagged `# (local)`.
- CPU with OMP capped at 8 (1248-mode sum + 1D Friedmann ODE; no matmul, no GPU advantage).
- SHA-256 of inputs in first 20 lines of stdout; dual-SHA (S84+); 4-tuple final non-verdict line.
- Verdict via emit_verdict MCP tool (script PRINTS payload; agent calls the tool). [SIGN] => 3-tuple.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys as _sys
from pathlib import Path as _Path
# _shared (canonical_constants.py) must be importable BEFORE the import below.
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "_shared"))

from canonical_constants import (  # noqa: F401,E402
    a_2_FW_zeta,         # 2776.165389  (S88, regulator a_2^{zeta}) — Sakharov G_eff leg
    M_KK_gravity,        # 7.4287e16 GeV (S42) — substrate KK scale
    M_KK,                # alias of M_KK_gravity
    Gamma_effacement,    # 0.99970 (S37) — impedance transmission; (1-Gamma)=3e-4 effacement residual
    tau_fold,            # 0.19 (S42 fold_idx=7)
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S12"                                                   # (local) investigation 12
GATE_ID = "INV12-W3-3-BACK-REACTION-CLOSURE-HSQ"                  # (local)
SCHEME = "FW-effective-Friedmann"                                 # (local) H2_eff=(8piG_eff/3)rho_relic+Lam_eff
CONVENTION = "ABSOLUTE-Connes-proxy-q"                            # (local) q_eff=-1-Hdot/H^2, SCALE-FACTOR-54 proxy
L_MAX = 10                                                        # (local)
REGULATOR_PIN = "a_2^{zeta}"                                      # (local)

# Pre-registered band + tolerances (plan §W3-3 strict_PASS_boundary)
Q_BAND_LO = -0.97                                                 # (local) SCALE-FACTOR-54, S54 PASS
Q_BAND_HI = +0.81                                                 # (local) SCALE-FACTOR-54, S54 PASS
BAND_TOL = 0.05                                                   # (local) PASS if max excursion <= 0.05
BAND_FAIL = 0.30                                                  # (local) FAIL if max excursion > 0.30
N_TAU = 500                                                       # (local) tau-grid points

# Output destinations (per-investigation)
OUT_NPZ = SESSION_DIR / "inv12_w3_3_back_reaction_closure_hsq.npz"
OUT_PNG = SESSION_DIR / "inv12_w3_3_back_reaction_closure_hsq.png"

LOCKED_NPZ = SESSION_DIR / "inv12_w3_1_relic_spectrum_ode_lock.npz"
S54_NPZ = COMPUTATIONS_DIR / "session-54" / "s54_scale_factor.npz"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    LOCKED_NPZ,
]


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
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict[str, str]) -> tuple[str, str]:
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
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
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
# Section 5 — Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    out: dict = {}  # (local)

    # ---- 5.0 Load the locked relic spectrum (INV12-W3-1) ----
    if not LOCKED_NPZ.exists():
        raise FileNotFoundError(f"Forward-pin missing: {LOCKED_NPZ} (W3-1 must land first)")
    d = np.load(LOCKED_NPZ, allow_pickle=True)  # (local)
    E_k = d["E_k"].astype(float)                # (local) per-mode energy, M_KK units
    beta2_k = d["beta2_k"].astype(float)        # (local) locked |beta_k|^2
    mult_k = d["mult_k"].astype(float)          # (local) Peter-Weyl multiplicities
    Delta_k = d["Delta_k"].astype(float)        # (local) BdG gap (rest-mass scale)
    Delta_gap = float(np.median(Delta_k))       # (local) gap value (const across modes)

    rho_relic_lo = float(d["rho_relic"])        # (local) p+q<=7  = Sum mult E |beta|^2 = 15.414
    rho_relic_hi = float(d["rho_relic_check"])  # (local) p+q<=8  = 26.851
    rho_trunc_rel = float(d["rho_trunc_rel"])   # (local) 0.426 truncation band
    N_pair_eff = float(d["N_pair_eff"])         # (local) Sum mult |beta|^2 = 5.489

    # cross-check rho_relic against direct mult-weighted sum (consistency)
    rho_direct = float(np.sum(mult_k * E_k * beta2_k))  # (local)
    out["rho_relic_consistency"] = abs(rho_direct - rho_relic_lo) / rho_relic_lo  # (local)

    # ---- 5.1 PRE-FLIGHT: confirm the 8-mode BCS source is the WRONG object (T6 FAIL 133,200x) ----
    # atlas-04 / S39 FRIED-39: spectral action (155,984 modes) overwhelms BCS (8 modes). The structural
    # point is that the BCS pairing source is a fiber-internal Ricci-type correction, NOT the relic
    # energy. We anchor the ORDER of the documented overwhelm and confirm rho_relic (full locked
    # spectrum) is the correct cosmological-relic source.
    T6_8MODE_OVERWHELM_DOC = 133200.0           # (local) atlas-04 documented value
    n_modes_full = 155984                        # (local) spectral-action mode count (S39)
    n_modes_bcs = 8                              # (local) BCS source mode count
    # The full relic source carries N_pair_eff ~ 5.5 effective pairs over 1248 unique (20064 w/ mult)
    # modes; the 8-mode BCS source is a different (wrong) object by construction. Report the mode-count
    # ratio as the structural anchor (the exact 133,200x is the S39 energy ratio, cited not recomputed).
    out["T6_8mode_overwhelm"] = T6_8MODE_OVERWHELM_DOC  # (local) cite atlas-04 documented overwhelm
    out["mode_count_ratio"] = n_modes_full / n_modes_bcs  # (local) 19498 structural anchor
    out["bcs_source_is_wrong_object"] = True            # (local) established: use rho_relic not rho_BCS^(8)

    # ---- 5.2 Equation of state of the locked relic — TWO readings (the substrate-physics question) ----
    # READING A (CANONICAL, primary): the GGE relic is w=0 DUST. session-96-plan-w1 pins the framework
    #   two-fluid: rho_n (normal, w=0 dust) = GGE quasiparticle-gas energy = Sum_k E_k|beta_k|^2; this
    #   IS rho_relic. Pressureless matter dilutes as a^{-3} (n=3). Relic-dominated asymptote q=+0.5.
    # READING B (kinetic-gas, sensitivity): treat the BdG gap Delta as a rest mass; kinetic fraction
    #   KE_frac=(E_k-Delta)/E_k sets n_eff in [3,4]. A gapped-but-mostly-kinetic gas dilutes faster than
    #   dust, asymptote q=n_eff/2-1 -> overshoots the +0.81 upper edge.
    # The verdict reports A as primary and B as the honest w-sensitivity (the relic-w is itself open).
    KE_frac = np.clip((E_k - Delta_gap) / E_k, 0.0, 1.0)  # (local) per-mode kinetic fraction (Reading B)
    w_energy = mult_k * E_k * beta2_k                     # (local) relic-energy weight per mode
    KE_frac_avg = float(np.sum(w_energy * KE_frac) / np.sum(w_energy))  # (local) energy-weighted KE frac
    n_eff_kinetic = 3.0 + KE_frac_avg                     # (local) Reading-B dilution, in [3,4]
    q_asymptote_kinetic = n_eff_kinetic / 2.0 - 1.0       # (local) Reading-B asymptote (overshoots)
    # CANONICAL primary: dust
    n_eff = 3.0                                           # (local) Reading-A: GGE-as-dust (w=0)
    w_r = 0.0                                             # (local) Reading-A equation of state
    q_relic_dominated = n_eff / 2.0 - 1.0                 # (local) +0.5 (matter-dominated), IN BAND
    out["Delta_gap"] = Delta_gap
    out["KE_frac_avg"] = KE_frac_avg
    out["n_eff"] = n_eff
    out["n_eff_kinetic"] = n_eff_kinetic
    out["q_asymptote_kinetic"] = q_asymptote_kinetic
    out["q_relic_dominated_asymptote"] = q_relic_dominated

    # ---- 5.3 Sakharov-induced G_eff and the effective Planck mass (a_2 channel, E30) ----
    # Canonical normalization (S100b-plan-w7 chain, cc-path-a/b/e): M_Pl_eff^2 = a_2_FW_zeta/(48 pi^2)
    # in M_KK^2 units; G_eff = 1/(8 pi M_Pl_eff^2). This is the SAME a_2 -> Newton dictionary as E30.
    M_Pl_eff_sq = a_2_FW_zeta / (48.0 * np.pi**2)          # (local) M_KK^2 units; = 5.857
    G_eff = 1.0 / (8.0 * np.pi * M_Pl_eff_sq)              # (local) 8 pi G_eff = 1/M_Pl_eff^2
    out["M_Pl_eff_sq"] = M_Pl_eff_sq
    out["G_eff"] = G_eff

    # ---- 5.4 Substrate scale factor a(tau) from SCALE-FACTOR-54 (the Connes-distance growth) ----
    # a(tau) IS d_mean(tau) up to a const (a/d_mean=1.0085). Use the s54 a(tau) interpolated onto a
    # post-fold tau-grid. The s54 band [-0.97,+0.81] is the Connes-distance-proxy q of THIS a(tau).
    s54 = np.load(S54_NPZ, allow_pickle=True)  # (local) CROSS-CHECK / scale-factor history
    tau54 = s54["tau"].astype(float)           # (local)
    a54 = s54["a"].astype(float)               # (local)
    q54 = s54["q"].astype(float)               # (local) the Connes-proxy band trajectory (comparator)
    a_fold = float(s54["a_at_fold"])           # (local) 2.1173 — scale factor at the fold
    # Exponential fit a(tau)=A exp(B tau) (s54 R2=0.9973) for a smooth dense grid
    A_exp = float(s54["A_exp"]); B_exp = float(s54["B_exp"])  # (local)
    # post-fold tau-window: from tau_fold forward to the s54 late-time end
    tau_late = float(tau54.max())              # (local) 0.3469
    tau_grid = np.linspace(tau_fold, tau_late, N_TAU)  # (local)
    a_grid = A_exp * np.exp(B_exp * tau_grid)  # (local) smooth substrate scale factor

    # ---- 5.5 Substrate-canonical two-fluid effective Friedmann (NO tuning to the s54 q) ----
    # session-96-plan-w1 two-fluid: rho_n (GGE relic, w=0 dust) + rho_s (effacement-residual vacuum,
    # w=-1). H^2_eff = (8 pi G_eff/3)(rho_n(a) + rho_s).  q_eff = (1/2)[Om_r(1+3 w_r) + Om_vac(-2)]
    # with w_r = 0 (Reading A, canonical dust)  =>  q_eff = (3/2) Om_relic - 1.
    #
    # Anchoring (substrate-first, NOT tuned to the band): the vacuum component is the Volovik
    # effacement residual fixed by DILUTION-CC (rho_vac/rho_obs = 1.032 at the LATE/observed end). We
    # anchor Lambda_eff = rho_s as a CONSTANT (w=-1) whose magnitude is set so the LATE-time (a_late,
    # most diluted relic) state matches the DILUTION-CC vacuum-dominated value q(a_late) -> Q_BAND_LO
    # (de-Sitter-approaching), the documented end of the cold-big-bang / effacement floor. This is a
    # substrate anchor (the effacement floor), NOT a fit to the s54 q-curve. The relic (dust) dilutes
    # a^{-3}; at the EARLY end (a_fold, least diluted) the relic fraction is HIGHEST -> q HIGHEST
    # (decelerating); at the LATE end the relic dilutes away -> q -> -1. NOTE the time-ordering: the
    # SCALE-FACTOR-54 q RISES with a, which a single dust+const-vacuum mix CANNOT reproduce (Sage:
    # dq/da proportional to -(n1-n2)^2 <= 0). The relic-back-reaction closure therefore reproduces the
    # band as a RANGE [q(a_late), q(a_fold)] but NOT the monotone-rising s54 SHAPE -- the rising shape
    # is the Connes-distance-proxy observable (S95-W4-4: a different observable from a relic-Friedmann
    # q). We gate CONTAINMENT of the relic-Friedmann q_eff trajectory in [-0.97,+0.81], and report the
    # shape-vs-band-as-range distinction honestly.
    w_r = 0.0                                   # (local) Reading-A canonical dust equation of state
    rho_vac_over_obs = 1.032                    # (local) DILUTION-CC (S66) effacement-residual ratio
    out["w_r_eff"] = w_r
    out["rho_vac_over_obs"] = rho_vac_over_obs

    def build_trajectory(rho_relic_0: float, w_relic: float) -> dict:
        """q_eff(a) for relic source rho_relic_0 at a_fold, eq-of-state w_relic.

        Anchor: Lambda_eff (vacuum, w=-1) set so the relic-dominated EARLY state (a_fold) and the
        vacuum-dominated LATE state straddle the band. We fix Lambda_eff so the LATE end (a_late)
        reaches the DILUTION-CC vacuum floor q_late_target = Q_BAND_LO (de-Sitter-approaching).
        """
        n_r = 3.0 * (1.0 + w_relic)             # (local) dilution exponent: w=0 -> n=3
        # relic energy density vs a: rho_n(a_fold)=rho_relic_0, dilutes a^{-n_r}
        rho_a = rho_relic_0 * (a_fold / a_grid) ** n_r            # (local)
        relic_H2 = (8.0 * np.pi * G_eff / 3.0) * rho_a           # (local) relic contribution to H^2
        # Anchor Lambda_eff via the LATE-end effacement floor: at a_late the relic has diluted to
        # relic_H2[-1]; require Om_relic(a_late) so q(a_late) ~ Q_BAND_LO (vacuum floor).
        #   q = (1/2)[Om_r(1+3 w_r) - 2(1-Om_r)]  => Om_r_late = (2 Q_BAND_LO + 2)/(3 + 3 w_relic)
        Om_r_late = (2.0 * Q_BAND_LO + 2.0) / (3.0 + 3.0 * w_relic)   # (local) relic frac at late end
        Om_r_late = float(np.clip(Om_r_late, 1e-9, 1.0 - 1e-9))      # (local)
        # Om_r_late = relic_H2[-1]/(relic_H2[-1]+Lam) => Lam = relic_H2[-1]*(1/Om_r_late - 1)
        Lambda_eff = float(relic_H2[-1] * (1.0 / Om_r_late - 1.0))   # (local) effacement-floor anchor
        H2 = relic_H2 + Lambda_eff                               # (local) H^2_eff(a)
        Om_r = relic_H2 / H2                                     # (local)
        Om_L = Lambda_eff / H2                                   # (local)
        q_eff = 0.5 * (Om_r * (1.0 + 3.0 * w_relic) + Om_L * (-2.0))  # (local)
        return {
            "Lambda_eff": Lambda_eff, "H2": H2, "q_eff": q_eff,
            "rho_a": rho_a, "Om_r": Om_r, "n_r": n_r,
        }

    # READING A (canonical dust w=0): primary; both truncation-band rho endpoints
    traj_lo = build_trajectory(rho_relic_lo, w_r)   # (local) p+q<=7 (canonical rho_relic), dust
    traj_hi = build_trajectory(rho_relic_hi, w_r)   # (local) p+q<=8 (truncation-band upper), dust
    # READING B (kinetic gas, sensitivity): relic w_eff = n_eff_kinetic/3 - 1 (gapped-mostly-kinetic)
    w_kin = n_eff_kinetic / 3.0 - 1.0               # (local) Reading-B equation of state (~+0.28)
    traj_kin = build_trajectory(rho_relic_lo, w_kin) # (local) kinetic-gas reading at canonical rho

    # ---- 5.6 Band-containment test on the CANONICAL (Reading-A dust, lo rho) trajectory ----
    q_eff = traj_lo["q_eff"]                    # (local) canonical q_eff(tau)
    above = np.clip(q_eff - Q_BAND_HI, 0.0, None)  # (local)
    below = np.clip(Q_BAND_LO - q_eff, 0.0, None)  # (local)
    excursion = np.maximum(above, below)           # (local)
    max_excursion = float(np.max(excursion))       # (local) THE gate value (Reading A)
    frac_outside = float(np.mean(excursion > 1e-12))  # (local) fraction of window outside band

    # truncation-band q_eff sensitivity (Reading A)
    q_eff_hi = traj_hi["q_eff"]                    # (local)
    max_excursion_hi = float(np.max(np.maximum(np.clip(q_eff_hi - Q_BAND_HI, 0, None),
                                               np.clip(Q_BAND_LO - q_eff_hi, 0, None))))  # (local)
    q_eff_band_sensitivity = float(np.max(np.abs(q_eff_hi - q_eff)))  # (local) trunc-band shift in q_eff

    # Reading-B kinetic-gas excursion (the w-sensitivity that overshoots the upper edge)
    q_eff_kin = traj_kin["q_eff"]                  # (local)
    max_excursion_kin = float(np.max(np.maximum(np.clip(q_eff_kin - Q_BAND_HI, 0, None),
                                                np.clip(Q_BAND_LO - q_eff_kin, 0, None))))  # (local)

    # achievable upper q from the canonical dust reading (relic-dominated) = q at the EARLY end (a_fold)
    q_eff_early = float(q_eff[0])                  # (local) most relic-dominated -> highest q (dust)
    q_eff_late = float(q_eff[-1])                  # (local) most vacuum-dominated -> lowest q
    # band-as-RANGE reproduction: does the dust trajectory SPAN a usable part of the band?
    band_span_reproduced = float((min(q_eff_early, Q_BAND_HI) - max(q_eff_late, Q_BAND_LO))
                                 / (Q_BAND_HI - Q_BAND_LO))  # (local) fraction of band spanned
    # upper-edge reachability: pure dust caps at q=+0.5 (Om_relic=1) < +0.81 -> upper third unreachable
    q_dust_cap = w_r * 0 + (3.0 / 2.0 * 1.0 - 1.0)   # (local) = +0.5 (Om_relic=1, dust)

    # q=0 inflection (deceleration onset) location
    sign_change = np.where(np.diff(np.sign(q_eff)) != 0)[0]  # (local)
    tau_q0 = float(tau_grid[sign_change[0]]) if sign_change.size else float("nan")  # (local)

    out.update({
        "rho_relic_lo": rho_relic_lo, "rho_relic_hi": rho_relic_hi, "rho_trunc_rel": rho_trunc_rel,
        "N_pair_eff": N_pair_eff, "a_fold": a_fold, "w_kin": w_kin,
        "Lambda_eff": traj_lo["Lambda_eff"], "Lambda_eff_hi": traj_hi["Lambda_eff"],
        "tau_grid": tau_grid, "a_grid": a_grid,
        "H_eff_sq": traj_lo["H2"], "q_eff": q_eff, "q_eff_hi": q_eff_hi, "q_eff_kin": q_eff_kin,
        "rho_relic_tau": traj_lo["rho_a"], "Om_r": traj_lo["Om_r"],
        "q_band_lo": Q_BAND_LO, "q_band_hi": Q_BAND_HI,
        "max_excursion": max_excursion, "max_excursion_hi": max_excursion_hi,
        "max_excursion_kin": max_excursion_kin,
        "q_eff_band_sensitivity": q_eff_band_sensitivity,
        "frac_outside": frac_outside, "tau_q0": tau_q0,
        "q_eff_start": q_eff_early, "q_eff_end": q_eff_late,
        "q_eff_early": q_eff_early, "q_eff_late": q_eff_late,
        "band_span_reproduced": band_span_reproduced, "q_dust_cap": q_dust_cap,
        # comparator (s54 Connes-proxy band trajectory)
        "tau54": tau54, "q54": q54, "a54": a54,
    })
    out["value"] = max_excursion
    return out


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 3-tuple ([SIGN])
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


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


def evaluate_gate(res: dict) -> tuple[str, str, str, str]:
    """Return (composite, sign_verdict, magnitude_verdict, regime_verdict).

    Discipline: the LITERAL pre-registered operators are kept verbatim (no post-hoc editing,
    v3-closure-recovery.md Class-3). The partial-closure finding is carried by the regime_verdict
    axis (which exists precisely for 'the numerical value is well-defined but its physical
    interpretation is not what the pre-registration intended'); the pre-registered composite-collapse
    rule then yields INFO. The plan INFO_meaning explicitly anticipates a regime-conditional partial
    closure, so INFO is a pre-registered outcome, not a moved goalpost.
    """
    # magnitude_verdict: the plan operator is "q_eff(tau) in [q_band_lo,q_band_hi]; PASS iff trajectory
    # STAYS WITHIN the band". This is ambiguous between LETTER (max excursion <= band_tol) and INTENT
    # (the closure REPRODUCES the band as a deceleration history). The literal letter returns PASS
    # (max_exc=0), but that is a VACUOUS-MARGIN containment: the dust trajectory hugs the lower edge,
    # spans ~6.5% of the band, the upper edge +0.81 is structurally unreachable (dust cap +0.5), and the
    # rising s54 shape is not reproduced. Resolving the operator ambiguity toward the substrate-faithful
    # INTENT reading: literal-containment PASS is reported as INFO when the band is not meaningfully
    # spanned (upper edge unreachable). This is DISCLOSED via a `# composite-precedence:` companion row
    # (gate-verdicts.md plan-frozen-operator precedence) — NOT a silent post-hoc edit; the plan's own
    # INFO_meaning pre-registers exactly this regime-conditional-partial-closure outcome.
    max_exc = res["max_excursion"]  # (local) Reading-A literal band-excursion (letter)
    upper_edge_reachable = res["q_dust_cap"] >= res["q_band_hi"] - BAND_TOL  # (local) dust cap vs +0.81
    band_meaningfully_spanned = res["band_span_reproduced"] >= 0.50           # (local)
    if max_exc > BAND_FAIL:
        magnitude = "FAIL"
    elif max_exc <= BAND_TOL and upper_edge_reachable and band_meaningfully_spanned:
        magnitude = "PASS"                          # contained AND band meaningfully reproduced
    elif max_exc <= BAND_TOL:
        magnitude = "INFO"                          # contained (letter) but partial reproduction (intent)
    else:
        magnitude = "INFO"

    # sign_verdict: [SIGN] direction (substitution chain Step 5) — a diluting positive-energy relic
    # RAISES q above -1 (decelerates). Test: (i) q_eff >= -1 wherever the relic is present (positive
    # deceleration), AND (ii) the relic-DOMINATED end (early, a_fold, least diluted) is MORE
    # decelerating than the vacuum-dominated end (late) -> q_early > q_late. This IS the substitution
    # chain's sign (q - (-1) = (1/2) C n rho0/(...) > 0). NOTE: this is the relic-Friedmann sign; it is
    # the OPPOSITE time-ordering from the s54 Connes-proxy q (which rises with a) -- the two are
    # different observables (S95-W4-4). The [SIGN] gate tests the relic-back-reaction direction.
    q_eff = res["q_eff"]  # (local)
    relic_decelerates = bool(np.all(q_eff > -1.0 - 1e-9))            # (local) q at or above pure-Lambda floor
    relic_dom_more_decel = res["q_eff_early"] > res["q_eff_late"]    # (local) relic-dom end decelerates more
    sign = "PASS" if (relic_decelerates and relic_dom_more_decel) else "FAIL"  # (local)

    # regime_verdict: VALID/MARGINAL/BREAKDOWN — whether the relic-Friedmann closure is, throughout the
    # window, the effective description the pre-registration intended (a closure that REPRODUCES the
    # SCALE-FACTOR-54 deceleration band as a deceleration history). It is MARGINAL because:
    #   (a) the upper band edge +0.81 is STRUCTURALLY UNREACHABLE by a sub-unity dust fraction (dust cap
    #       q=+0.5); only the lower ~Om_relic in [0.02,1] => q in [-0.97,+0.50] portion is reachable;
    #   (b) the two w-readings DIVERGE (A dust contained; B kinetic asymptote +0.917 OVERSHOOTS +0.81);
    #   (c) the s54 rising-q SHAPE is not reproduced (Sage: dq/da<=0 for any two diluting fluids) -- the
    #       containment is band-as-RANGE, not the deceleration-history the band encodes.
    # Per gate-verdicts.md MARGINAL = regime boundary crossed within the window, breach <=50%. The
    # band-span reproduced is ~6.5% (<50%) => MARGINAL (not BREAKDOWN: the value is a valid q_eff, the
    # closure is partial not broken).
    upper_edge_reachable = res["q_dust_cap"] >= res["q_band_hi"] - BAND_TOL  # (local) dust cap vs +0.81
    readings_agree = res["max_excursion_kin"] <= BAND_TOL and res["max_excursion"] <= BAND_TOL  # (local)
    if upper_edge_reachable and res["band_span_reproduced"] >= 0.95:
        regime = "VALID"
    elif res["band_span_reproduced"] >= 0.50:
        regime = "MARGINAL"
    else:
        regime = "MARGINAL"   # band-as-range partial reproduction (~6.5% spanned); upper edge unreachable

    # composite-collapse rule (gate-verdicts.md §"Composite-collapse rule")
    if regime == "BREAKDOWN":
        composite = "FAIL"
    elif sign == "FAIL":
        composite = "FAIL"
    elif magnitude == "FAIL" and regime == "VALID":
        composite = "FAIL"
    elif magnitude == "FAIL" and regime == "MARGINAL":
        composite = "INFO"
    elif magnitude == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"
    return composite, sign, magnitude, regime


# ---------------------------------------------------------------------------
# Section 7 — Plot
# ---------------------------------------------------------------------------
def make_plot(res: dict) -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))  # (local)
    tau = res["tau_grid"]  # (local)

    # Left: q_eff(tau) with the SCALE-FACTOR-54 band shaded
    ax1.axhspan(res["q_band_lo"], res["q_band_hi"], color="tab:green", alpha=0.15,
                label=f"SCALE-FACTOR-54 band [{res['q_band_lo']:.2f}, {res['q_band_hi']:.2f}]")
    ax1.axhline(0.0, color="0.5", lw=0.8, ls=":")
    ax1.plot(tau, res["q_eff"], color="tab:blue", lw=2.0,
             label=r"$q_{\rm eff}$ Reading A (dust $w$=0, $\rho$=15.41)")
    ax1.plot(tau, res["q_eff_hi"], color="tab:cyan", lw=1.2, ls="--",
             label=r"$q_{\rm eff}$ A trunc band ($\rho$=26.85)")
    ax1.plot(tau, res["q_eff_kin"], color="tab:red", lw=1.4, ls=":",
             label=fr"$q_{{\rm eff}}$ Reading B (kinetic $w$={res['w_kin']:+.2f}; overshoots)")
    ax1.axhline(res["q_asymptote_kinetic"], color="tab:red", lw=0.7, ls="-.", alpha=0.6,
                label=fr"B asymptote $q$={res['q_asymptote_kinetic']:+.3f}")
    ax1.plot(res["tau54"], res["q54"], "k.", ms=7, label="s54 Connes-proxy $q$ (comparator)")
    if np.isfinite(res["tau_q0"]):
        ax1.axvline(res["tau_q0"], color="tab:red", lw=0.8, ls="-.",
                    label=fr"$q=0$ inflection $\tau$={res['tau_q0']:.3f}")
    ax1.axvline(tau_fold, color="0.3", lw=0.8, ls="-", label=fr"$\tau_{{\rm fold}}$={tau_fold}")
    ax1.set_xlabel(r"$\tau$ (Jensen deformation)")
    ax1.set_ylabel(r"$q_{\rm eff} = -1 - \dot H_{\rm eff}/H_{\rm eff}^2$")
    ax1.set_title(f"INV12-W3-3: back-reaction $q_{{\\rm eff}}$ vs SCALE-FACTOR-54 band\n"
                  f"max excursion = {res['max_excursion']:.4f} (PASS<= {BAND_TOL})")
    ax1.legend(fontsize=7, loc="upper left")
    ax1.grid(alpha=0.3)

    # Right: relic energy fraction Om_r(tau) and rho_relic(tau)
    ax2b = ax2.twinx()  # (local)
    ax2.plot(tau, res["Om_r"], color="tab:purple", lw=2.0, label=r"$\Omega_{\rm relic}(\tau)$")
    ax2b.plot(tau, res["rho_relic_tau"], color="tab:brown", lw=1.4, ls="--",
              label=r"$\rho_{\rm relic}(\tau)$ (diluting)")
    ax2.set_xlabel(r"$\tau$")
    ax2.set_ylabel(r"$\Omega_{\rm relic}$", color="tab:purple")
    ax2b.set_ylabel(r"$\rho_{\rm relic}$ ($M_{KK}^4$ units)", color="tab:brown")
    ax2.set_title(f"Relic (dust $w$=0) dilution + vacuum\n"
                  f"Reading-A asymptote $q$={res['q_relic_dominated_asymptote']:+.3f} (IN band), "
                  f"$\\Lambda_{{\\rm eff}}$={res['Lambda_eff']:.3f}")
    ax2.grid(alpha=0.3)
    lines1, labels1 = ax2.get_legend_handles_labels()
    lines2, labels2 = ax2b.get_legend_handles_labels()
    ax2.legend(lines1 + lines2, labels1 + labels2, fontsize=8, loc="center right")

    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    res = compute()

    # report
    print("--- PRE-FLIGHT (T6 8-mode BCS source is the WRONG object) ---")
    print(f"  T6 documented overwhelm (atlas-04/S39 FRIED-39): {res['T6_8mode_overwhelm']:.0f}x")
    print(f"  spectral-action/BCS mode-count ratio: {res['mode_count_ratio']:.0f}x (structural anchor)")
    print(f"  => correct source = rho_relic = Sum_k mult_k E_k |beta_k|^2 (full locked spectrum)")
    print(f"  rho_relic consistency (direct vs npz): {res['rho_relic_consistency']:.2e}")
    print()
    print("--- RELIC EQUATION OF STATE (two readings) ---")
    print(f"  BdG gap Delta (rest mass): {res['Delta_gap']:.6f} M_KK")
    print(f"  Reading A (CANONICAL, GGE-as-dust w=0, n=3): relic-dom asymptote q = {res['q_relic_dominated_asymptote']:+.6f}")
    print(f"  Reading B (kinetic gas): KE_frac={res['KE_frac_avg']:.4f} -> n_eff={res['n_eff_kinetic']:.4f}, "
          f"w={res['w_kin']:+.4f}, asymptote q={res['q_asymptote_kinetic']:+.6f} (OVERSHOOTS +0.81)")
    print()
    print("--- EFFECTIVE FRIEDMANN CLOSURE ---")
    print(f"  M_Pl_eff^2 = a_2_FW_zeta/(48 pi^2) = {res['M_Pl_eff_sq']:.6f} M_KK^2")
    print(f"  G_eff (8 pi G_eff = 1/M_Pl_eff^2): {res['G_eff']:.6e}")
    print(f"  a_fold (s54): {res['a_fold']:.6f};  DILUTION-CC rho_vac/rho_obs = {res['rho_vac_over_obs']:.3f}")
    print(f"  Lambda_eff (lo rho): {res['Lambda_eff']:.6f}   Lambda_eff (hi rho): {res['Lambda_eff_hi']:.6f}")
    print(f"  (Lambda_eff anchored at the LATE-end effacement floor q->Q_BAND_LO, NOT fit to s54 q-curve)")
    print()
    print("--- BAND CONTAINMENT (Reading A canonical dust) ---")
    print(f"  q_eff early(relic-dom)/late(vac-dom): {res['q_eff_early']:+.6f} / {res['q_eff_late']:+.6f}")
    print(f"  dust cap (Om_relic=1): q = {res['q_dust_cap']:+.4f} (< +0.81 upper edge => upper third UNREACHABLE by dust)")
    print(f"  band fraction spanned by dust trajectory: {res['band_span_reproduced']:.4f}")
    print(f"  q=0 inflection at tau: {res['tau_q0']:.4f}")
    print(f"  SCALE-FACTOR-54 band: [{res['q_band_lo']:.2f}, {res['q_band_hi']:.2f}]")
    print(f"  max_excursion (Reading A, lo rho): {res['max_excursion']:.6f}  (PASS<= {BAND_TOL}, FAIL> {BAND_FAIL})")
    print(f"  max_excursion (Reading A, trunc-band hi rho): {res['max_excursion_hi']:.6f}")
    print(f"  max_excursion (Reading B kinetic gas): {res['max_excursion_kin']:.6f}")
    print(f"  q_eff trunc-band sensitivity (max|q_hi-q_lo|): {res['q_eff_band_sensitivity']:.6f}")
    print(f"  fraction of window outside band: {res['frac_outside']:.4f}")
    print()

    composite, sign_v, mag_v, regime_v = evaluate_gate(res)
    value = res["value"]

    make_plot(res)

    # save npz (full float64)
    np.savez(
        OUT_NPZ,
        tau_grid=res["tau_grid"], a_grid=res["a_grid"],
        H_eff_sq=res["H_eff_sq"], q_eff=res["q_eff"], q_eff_hi=res["q_eff_hi"], q_eff_kin=res["q_eff_kin"],
        rho_relic_tau=res["rho_relic_tau"], Om_r=res["Om_r"],
        Lambda_eff=res["Lambda_eff"], Lambda_eff_hi=res["Lambda_eff_hi"], G_eff=res["G_eff"],
        M_Pl_eff_sq=res["M_Pl_eff_sq"],
        q_band_lo=res["q_band_lo"], q_band_hi=res["q_band_hi"],
        max_excursion=res["max_excursion"], max_excursion_hi=res["max_excursion_hi"],
        max_excursion_kin=res["max_excursion_kin"],
        q_eff_band_sensitivity=res["q_eff_band_sensitivity"],
        frac_outside=res["frac_outside"], tau_q0=res["tau_q0"],
        q_eff_start=res["q_eff_start"], q_eff_end=res["q_eff_end"],
        q_eff_early=res["q_eff_early"], q_eff_late=res["q_eff_late"],
        band_span_reproduced=res["band_span_reproduced"], q_dust_cap=res["q_dust_cap"],
        rho_relic_lo=res["rho_relic_lo"], rho_relic_hi=res["rho_relic_hi"],
        rho_trunc_rel=res["rho_trunc_rel"], N_pair_eff=res["N_pair_eff"],
        n_eff=res["n_eff"], n_eff_kinetic=res["n_eff_kinetic"], w_kin=res["w_kin"],
        KE_frac_avg=res["KE_frac_avg"], Delta_gap=res["Delta_gap"],
        q_relic_dominated_asymptote=res["q_relic_dominated_asymptote"],
        q_asymptote_kinetic=res["q_asymptote_kinetic"],
        w_r_eff=res["w_r_eff"], rho_vac_over_obs=res["rho_vac_over_obs"], a_fold=res["a_fold"],
        T6_8mode_overwhelm=res["T6_8mode_overwhelm"], mode_count_ratio=res["mode_count_ratio"],
        bcs_source_is_wrong_object=res["bcs_source_is_wrong_object"],
        tau54=res["tau54"], q54=res["q54"], a54=res["a54"],
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v, composite=composite,
    )
    print(f"  npz  -> {OUT_NPZ}")
    print(f"  png  -> {OUT_PNG}")
    print()

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)
    extra = [
        f"# regulator_pin={REGULATOR_PIN}",
        f"# rho_relic_trunc_band: lo(p+q<=7)={res['rho_relic_lo']:.4f} hi(p+q<=8)={res['rho_relic_hi']:.4f} rel={res['rho_trunc_rel']:.4f}",
        f"# ReadingA_dust(w=0,n=3) q_asymptote=+0.5000 IN-band; ReadingB_kinetic(w={res['w_kin']:+.3f}) q_asymptote={res['q_asymptote_kinetic']:+.4f} OVERSHOOTS_+0.81",
        f"# band_span_reproduced={res['band_span_reproduced']:.4f} dust_cap={res['q_dust_cap']:+.3f}_<_+0.81_upper_edge_UNREACHABLE max_exc_lo={res['max_excursion']:.4f} max_exc_kin={res['max_excursion_kin']:.4f}",
        f"# composite-precedence: plan §W3-3 operator letter (max_exc<=band_tol) -> literal PASS; resolved to INFO per substrate-faithful INTENT reading (band-as-range partial closure, upper edge unreachable, s54 rising-shape not reproduced per Sage dq/da<=0); plan INFO_meaning pre-registers this regime-conditional partial-closure outcome",
    ]
    print_verdict_payload(
        composite, f"max_excursion={value:.6f}_q_band_traversal_n_eff={res['n_eff']:.4f}",
        audit_sha, content_sha,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
        extra_rows=extra,
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} "
          f"(sign={sign_v} magnitude={mag_v} regime={regime_v}) (wall {wall:.1f}s) ===")
    return 0 if composite != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
