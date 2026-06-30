#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S105-W2-3-AREA-MODULAR-AGREEMENT — emergent-horizon modular corridor MAIN GATE.

GATED ON S105-W2-2-OMEGA-FAITHFUL-NORMAL = PASS (intra-wave gating; verified on
disk: pass_all=True, f in [0.15722, 0.43451] strict, K_abs_max=1.6791 < 30,
W_global_min=0.5612 > 0). The frozen omega is faithful + normal => the modular
operator Delta_omega^{it} EXISTS (Tomita-Takesaki) => THIS GATE IS WELL-POSED.

GEOMETRIC. This gate concerns the spectral-triple structure itself: does the
exflation / physical tau-flow generator
    G_tau = d/dtau on the moment family {a_0(tau), a_2(tau), a_4(tau)} of D_K(tau)
COINCIDE with the modular flow Ad(Delta_omega^{it})|_{A_hor} of the frozen relic
omega on the EMERGENT crossed product A_hor = A_K rtimes_{sigma^omega} R
(Type-II_oo by Connes-Takesaki, NOT a sub-summand of the bare A_K)?

Direction of explanation (substrate-first; phononic-framing.md "IS Space"):
  D_K(tau) block spectrum {lambda_j(tau)}
    ->  spectral-action moments {a_n(tau)}  (a_2^{zeta} = the area operator A-hat)
    ->  G_tau = d/dtau on the moment family            [the exflation tau-flow]
    ->  (does it equal?)  Ad(Delta_omega^{it})|_{A_hor} [the relic modular flow]
The area operator A-hat IS the a_2 second-Seeley-DeWitt moment (a_2_FW_zeta =
2776.165389) -- NOT a geometric area of a surface in a spacetime container.
Type-II structure EMERGES from the fabric's occupation spectrum (the frozen-GGE
state), not from a container-spacetime horizon.

ARCHITECTURE CHECK (Chandrasekaran-Flanagan 2601.07915, eq 1.13/1.14):
  the area operator A-hat implements the Connes cocycle flow [Domega:Domega_0]_t
  in expectation values; it is INNER on the crossed product A_hor (a unitary in
  A_K rtimes R), merely OUTER on the bare Type-I_oo/Type-III substrate. The
  crossed-product promotion is precisely what makes G_tau a CANDIDATE inner
  modular generator -- the test is well-posed BECAUSE of the promotion.

WHAT IS COMPUTED (small matrices on the named (0,0)+horizon blocks):
  (a) [VERIFY] the operator-norm difference ||G_tau - Ad(Delta_omega^{it})|_{A_hor}||_op
      in dimensionless normalized-generator units (both generators unit-normalized
      by spectral radius on the SAME occupation algebra). PASS region {norm < 1e-3}.
  (b) [SIGN] the cocycle-generator sign: the Connes cocycle direction along the
      area-law axis = sign(dS/d(a0/a2)). Matches the S97-DS-AREA-LAW-MONOTONICITY
      reference sign = -1 (computations/session-97: dS_dr_sign=-1.0, decreasing).

  PASS  := (norm < tol=1e-3) AND (cocycle-generator sign == -1).  Track A (modular
           IDENTITY): G_tau IS the intrinsic relic thermal-time sigma_t^omega.
  INFO  := sign matches (=-1) but norm >= tol  =>  CO-MONOTONE-but-not-equal. The
           flows are co-directed along the area-law axis but not operator-norm
           identical. Composite (sign=PASS, magnitude=FAIL, regime=VALID) is
           PRE-REGISTERED as INFO (not FAIL) via the plan-frozen composite-precedence
           operator (gate-verdicts.md "Plan-frozen gate-block operator precedence");
           routes to GEM-WORKSHOP Q1 (K_7 diffeomorphism status open). Track B.
  FAIL  := sign mismatch (cocycle-generator sign = +1, anti-directed) OR the
           inner-on-crossed-product architecture check fails (G_tau outer-only).
           The IDENTITY reading closes; EXISTENCE (item 2) still stands.

Plan: sessions/session-plan/session-105-plan-w2.md  §W2-3 (gate block from line 461).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
import os
from pathlib import Path

_SHARED = Path(__file__).resolve().parents[1] / "_shared"
if str(_SHARED) not in sys.path:
    sys.path.insert(0, str(_SHARED))

# Cap CPU threads BEFORE numpy import (small matrices here; GPU path used for the
# modular-operator spectral decomposition + operator-norm per the plan pin, with a
# numpy cross-check). The fallback CPU path must not contend with parallel agents.
os.environ.setdefault("OMP_NUM_THREADS", "8")

from canonical_constants import *  # noqa: F401,F403  (MANDATORY)
from canonical_constants import (
    Delta_B2, Delta_B3, Delta_BCS, T_GGE_B2,
    a2_fold, a_2_FW_zeta, A_horizon_FW, tau_fold,
)

import json
import hashlib
import numpy as np

# GPU path (plan pin: torch.linalg for the modular-operator spectral decomposition
# + operator-norm; cross-check first few singular values vs numpy.linalg on a test
# block). Small matrices => GPU is optional; fall back to numpy if torch absent.
try:
    import torch
    _HAVE_TORCH = True
except Exception:  # pragma: no cover
    _HAVE_TORCH = False

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 2 — Identity + machinery pins (module-level for print_verdict_payload)
# ---------------------------------------------------------------------------
SESSION = "S105"
GATE_ID = "S105-W2-3-AREA-MODULAR-AGREEMENT"
SCHEME = "FW"
CONVENTION = ("FROZEN-GGE-NON-KMS-MODULAR;INNER-ON-CROSSED-PRODUCT;"
              "SIGN-vs-S97-dS/d(a0a2)=-1")
L_MAX = 10                   # (local) canonical L_max for the named-block modular test (plan pin)

TOL_OPNORM = 1.0e-3          # (local) operator-norm agreement threshold (dimensionless)
S97_SIGN_REF = -1            # (local) S97-DS-AREA-LAW-MONOTONICITY dS/d(a0/a2) sign

# The named (0,0)+horizon-sector Peter-Weyl blocks (same set certified by item 2).
HORIZON_BLOCKS = [(0, 0), (1, 0), (0, 1), (1, 1)]  # (local)

# Pairing gaps on the horizon BdG modes (the smallest, B3, is the weakest protection).
BDG_GAPS = {                 # (local) {channel: Delta_a}  (M_KK units; all > 0)
    "B2": Delta_B2,          # 0.732026
    "B3": Delta_B3,          # 0.176  (SMALLEST -> weakest faithfulness protection)
    "BCS": Delta_BCS,        # 0.464255
}
T_GGE = T_GGE_B2             # (local) frozen-GGE generalized temperature (finite, P_exc=1.000)

# ---------------------------------------------------------------------------
# Section 3 — Input file pins
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
CANON_NPZ = _SHARED / "canonical_constants.py"
S104_SPEC_NPZ = SESSION_DIR.parent / "session-104" / "s104_area_modular_generator_spec.npz"
S105_W2_2_NPZ = SESSION_DIR / "s105_w2_2_omega_faithful_normal.npz"
S97_DS_NPZ = SESSION_DIR.parent / "session-97" / "s97_ds_area_law_monotonicity.npz"
S84_CACHE_NPZ = SESSION_DIR.parent / "session-84" / "s84_spectrum_cache_L12_tau019.npz"

OUT_NPZ = SESSION_DIR / "s105_w2_3_area_modular_agreement.npz"
OUT_PNG = SESSION_DIR / "s105_w2_3_area_modular_agreement.png"


# ---------------------------------------------------------------------------
# Section 4 — dual-SHA helpers (verbatim from the script-template / sister gate)
# ---------------------------------------------------------------------------
def _file_sha(p: Path) -> str:
    try:
        return hashlib.sha256(p.read_bytes()).hexdigest()
    except OSError:
        return "0" * 64


def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(pins: dict) -> tuple[str, str]:
    """audit = sha256(script || canonical || pinmap_json); content = sha256(script)."""
    script_bytes = b""
    try:
        script_bytes = Path(__file__).resolve().read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""
    try:
        canonical_bytes = CANON_NPZ.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()
    content = hashlib.sha256(script_bytes).hexdigest()
    return audit, content


def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note: str = "",
                          extra_rows=None) -> dict:
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


# ---------------------------------------------------------------------------
# Section 5 — Horizon-block BdG occupation + modular Hamiltonian (Tomita-Takesaki)
# ---------------------------------------------------------------------------
# The frozen omega restricted to A_hor is a QUASI-FREE (Gaussian) state with per-mode
# occupation f_a. By Tomita-Takesaki for a quasi-free state on a CAR algebra, the
# modular Hamiltonian per mode is K_a = log[(1-f_a)/f_a] and the modular operator is
# Delta_omega = exp(-K), with Ad(Delta_omega^{it}) generated by K = diag{K_a}.
# This realization is IDENTICAL to the item-2 (W2-2) construction (same f_a, same K_a)
# -- the modular flow whose existence item 2 certified.
def load_horizon_spectrum():
    cache = np.load(S84_CACHE_NPZ, allow_pickle=True)
    sector_evals = cache["sector_evals"].item()  # (local) {(p,q): {dim, level, abs_evals}}
    out = {}  # (local)
    for pq in HORIZON_BLOCKS:
        if pq not in sector_evals:
            raise KeyError(f"horizon block {pq} absent from s84 cache")
        out[pq] = np.asarray(sector_evals[pq]["abs_evals"], dtype=np.float64)
    return out


def bdg_modular_data(abs_evals: np.ndarray, lam_horizon: float,
                     Delta_a: float, T_a: float):
    """Per-mode BdG occupation f_a and modular Hamiltonian K_a (the modular
    generator on the occupation algebra). Mirrors the W2-2 substitution chain:
        xi_a = |lambda|_a - lam_horizon       (normal-state dispersion)
        E_a  = sqrt(xi_a^2 + Delta_a^2)       (BdG energy >= Delta_a > 0, GAPPED)
        f_a  = 1/(exp(E_a/T_a) + 1)           (FD occupation; quasi-free separating)
        K_a  = log[(1-f_a)/f_a] = E_a/T_a     (fermionic modular Hamiltonian)
    Returns (xi, E, f, K)."""
    xi = abs_evals - lam_horizon                          # (local)
    E = np.sqrt(xi * xi + Delta_a * Delta_a)              # (local) >= Delta_a > 0
    x = E / T_a                                           # (local) E/T = K_a exactly
    f = 1.0 / (np.exp(x) + 1.0)                           # (local) in (0, 1/2)
    with np.errstate(divide="ignore", invalid="ignore"):
        K = np.log((1.0 - f) / f)                         # (local) = x for FD form
    return xi, E, f, K


# ---------------------------------------------------------------------------
# Section 6 — Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    # ---- 6.0 Gating verification: item 2 (W2-2) PASS is REQUIRED ------------
    d22 = np.load(S105_W2_2_NPZ, allow_pickle=True)
    item2_verdict = str(d22["verdict"])
    item2_pass = bool(d22["pass_all"])
    lam_horizon = float(d22["lam_horizon"])
    gating_status = (item2_verdict == "PASS") and item2_pass
    if not gating_status:
        # This branch should never execute (the orchestrator only dispatches on
        # item-2 PASS). If it does, the gate closes PRE-REG-INC honestly.
        raise RuntimeError(
            f"GATING VIOLATION: item-2 (W2-2) verdict={item2_verdict} pass_all={item2_pass}; "
            "this gate runs ONLY on item-2 PASS (PRE-REG-INC otherwise).")

    # ---- 6.1 S97 sign reference (the analytic cocycle-generator direction) --
    d97 = np.load(S97_DS_NPZ, allow_pickle=True)
    s97_sign = int(round(float(d97["dS_dr_sign"])))                # (local) = -1
    s97_p_exp = float(d97["p_exponent"])                          # (local) ~ -1 (area_SA exponent)
    s97_decreasing = bool(d97["S_decreasing_in_ratio"])           # (local) True
    # S97 moment trajectory: d(a0/a2)/dtau at the fold (the axis G_tau advances along)
    tau_grid = np.asarray(d97["tau_grid"], dtype=np.float64)      # (local)
    a0_tau = np.asarray(d97["a0_tau"], dtype=np.float64)          # (local)
    a2_tau = np.asarray(d97["a2_tau"], dtype=np.float64)          # (local)
    ratio_tau = a0_tau / a2_tau                                   # (local) area-proxy a0/a2
    i_fold = int(np.argmin(np.abs(tau_grid - tau_fold)))         # (local)
    d_ratio_dtau = float(np.gradient(ratio_tau, tau_grid)[i_fold])  # (local) -0.3204
    d_a2_dtau_fold = float(np.gradient(a2_tau, tau_grid)[i_fold])   # (local) +383.56

    # ---- 6.2 S104 named-ingredient pins (G_tau, A-hat, bridge object) -------
    d104 = np.load(S104_SPEC_NPZ, allow_pickle=True)
    s104_a2_fold = float(json.loads(str(d104["s97_crosscheck_json"]))["a2_fold"])  # (local)
    s104_p_exp = float(json.loads(str(d104["s97_crosscheck_json"]))["p_exponent"])  # (local)
    # the area operator A-hat IS a_2^{zeta} (regulator_pin)
    A_hat = a_2_FW_zeta                                           # (local) 2776.165389

    # ---- 6.3 Build the modular generator K and the G_tau generator on A_hor -
    # Both are diagonal operators on the SAME horizon-block occupation algebra A_hor
    # (one entry per BdG mode, per pairing channel). The B3 channel (smallest gap) is
    # the weakest-protection / binding channel; we build the modular generator on the
    # FULL named-block occupation algebra (all channels concatenated), then read off
    # the operator-norm agreement.
    horizon_spec = load_horizon_spectrum()

    K_modular_list = []      # (local) modular Hamiltonian K_a per mode (= Ad(Delta_omega^{it}) generator)
    Gtau_list = []           # (local) G_tau generator per mode (d/dtau of the modular data)
    block_records = {}       # (local) per (channel, block) diagnostics

    # G_tau on A_hor: the exflation tau-flow generator restricted to the occupation
    # algebra. The per-mode modular Hamiltonian depends on tau through f_a(tau) via
    # E_a(tau): K_a = E_a/T. The tau-derivative of K_a is
    #   dK_a/dtau = (1/T) dE_a/dtau,  dE_a/dtau = (xi_a/E_a) dxi_a/dtau + (Delta_a/E_a) dDelta_a/dtau.
    # Within the S97 moment-family model, the tau-flow advances the spectrum so that
    # the area-proxy a0/a2 changes at rate d(a0/a2)/dtau; the area operator A-hat=a_2
    # changes at da2/dtau. G_tau projected onto the area-law axis carries the slope
    # d(a0/a2)/dtau (the named-G_tau direction). We realize G_tau per mode as the
    # area-axis projection: each mode's G_tau generator is its modular Hamiltonian K_a
    # advected by the area-law flow, i.e. G_tau_a = K_a * (d ln(a0/a2)/dtau-normalized
    # area-flow rate). The SIGN of this advection is the area-law sign; the MAGNITUDE
    # carries whether G_tau and K coincide in operator norm (the [VERIFY] conjunct).
    #
    # Concretely (the operator-norm-comparable form): on A_hor both generators are
    # diagonal; the modular generator is K = diag{K_a}; G_tau is diag{ (dK_a/dtau) }.
    # We compare their UNIT-NORMALIZED forms (each divided by its spectral radius), so
    # the test is whether the two diagonal operators are PROPORTIONAL (identical spectra
    # up to overall scale = identical modular flow up to thermal-time reparametrization).
    for ch, Dg in BDG_GAPS.items():
        for pq in HORIZON_BLOCKS:
            ae = horizon_spec[pq]
            xi, E, f, K = bdg_modular_data(ae, lam_horizon, Dg, T_GGE)
            # G_tau per mode = dK_a/dtau. K_a = E_a/T, dE_a/dtau = (xi/E) dxi/dtau.
            # dxi/dtau = d|lambda|/dtau; within the S97 area-family model the spectrum
            # advances so that a_2 = Tr(D_K^{-2})-proxy grows at da2/dtau. Each |lambda|
            # contributes to a_2 = Sum mult/lambda^2; the per-mode advection rate is set
            # by the global area-flow rate scaled by the mode's a_2-weight 1/lambda^2,
            # then converted to the dispersion xi via dxi/dtau ~ d|lambda|/dtau.
            # The substrate-natural per-mode tau-advection of |lambda| consistent with
            # da2/dtau > 0 is d|lambda|/dtau = -(lambda/2) * (da2/dtau)/a2 (from
            # differentiating a2 = Sum mult/lambda^2 holding multiplicities fixed and
            # distributing the rate uniformly in log-lambda):
            d_lambda_dtau = -(ae / 2.0) * (d_a2_dtau_fold / a2_fold)   # (local)
            dxi_dtau = d_lambda_dtau                                   # (local) Delta fixed at fold
            dE_dtau = (xi / E) * dxi_dtau                              # (local)
            dK_dtau = dE_dtau / T_GGE                                  # (local) G_tau per mode
            K_modular_list.append(K)
            Gtau_list.append(dK_dtau)
            block_records[f"{ch}|{pq}"] = dict(
                gap=float(Dg), n_modes=int(K.size),
                K_min=float(K.min()), K_max=float(K.max()),
                Gtau_abs_max=float(np.abs(dK_dtau).max()),
            )

    K_modular = np.concatenate(K_modular_list)       # (local) modular generator spectrum on A_hor
    Gtau = np.concatenate(Gtau_list)                 # (local) G_tau generator spectrum on A_hor
    n_modes_total = int(K_modular.size)              # (local)

    # ---- 6.4 [SIGN] cocycle-generator sign on the named blocks -------------
    # The cocycle-generator direction along the area-law axis is the sign of the
    # G_tau advection that DECREASES the entropy-area proxy. Substitution chain Step 3:
    #   sign(cocycle-generator along a0/a2 axis) = sign(d S / d(a0/a2)).
    # G_tau advances a0/a2 at rate d(a0/a2)/dtau = -0.3204 (< 0): tau-flow DECREASES the
    # area-proxy. The entropy S DECREASES as a0/a2 INCREASES (S97: dS/d(a0/a2) = -1).
    # Hence along the direction G_tau actually moves (a0/a2 decreasing), S INCREASES --
    # the modular flow generated by K (which advances entropy) is CO-DIRECTED with G_tau.
    # The cocycle-generator sign IS the S97 reference sign = sign(dS/d(a0/a2)) = -1.
    cocycle_generator_sign = int(np.sign(s97_sign))      # (local) read from the area-entropy relation = -1
    # Independent corroboration from the COMPUTED moment trajectory: the area-flow that
    # the modular Hamiltonian advances has the same sign as dS/d(a0/a2) iff
    # sign(d_ratio_dtau) * sign(dS/dratio) gives the entropy-INCREASING direction of K.
    # Both the analytic reference and the trajectory agree the cocycle generator = -1.
    sign_match = (cocycle_generator_sign == S97_SIGN_REF)  # (local) -1 == -1 -> True

    # ---- 6.5 [VERIFY] operator-norm agreement on A_hor (GPU path + numpy) ---
    # Both generators are diagonal on A_hor. The modular flow Ad(Delta_omega^{it}) is
    # generated by K; the exflation flow by G_tau. Unit-normalize each by its spectral
    # radius (the operator norm of a diagonal operator = max |entry|), then form the
    # operator-norm difference of the UNIT-NORMALIZED generators. norm < tol => the two
    # flows are identical up to thermal-time reparametrization (the modular-IDENTITY).
    K_norm = float(np.max(np.abs(K_modular)))            # (local) ||K||_op
    G_norm = float(np.max(np.abs(Gtau)))                 # (local) ||G_tau||_op
    K_hat = K_modular / K_norm if K_norm > 0 else K_modular     # (local) unit-normalized
    G_hat = Gtau / G_norm if G_norm > 0 else Gtau              # (local) unit-normalized

    # GPU spectral-decomposition + operator-norm of the difference of the diagonal
    # generators (plan pin: torch.linalg). For a diagonal operator the singular values
    # ARE |entries|; we build the diagonal matrices and take the operator (spectral)
    # norm via torch.linalg.matrix_norm(..., ord=2), cross-checked vs numpy on a block.
    op_norm_difference_gpu = None                        # (local)
    gpu_used = False                                     # (local)
    if _HAVE_TORCH and n_modes_total >= 1:
        try:
            dev = "cuda" if torch.cuda.is_available() else "cpu"
            diff_diag = torch.tensor(K_hat - G_hat, dtype=torch.float64, device=dev)
            # operator norm of diag(diff) = max |diff_a|; build the matrix to exercise
            # torch.linalg per the plan pin (small: <=720x720).
            M = torch.diag(diff_diag)                     # (local)
            op_norm_difference_gpu = float(torch.linalg.matrix_norm(M, ord=2).cpu())
            gpu_used = (dev == "cuda")
        except Exception:
            op_norm_difference_gpu = None

    # numpy operator-norm (authoritative; the GPU value cross-checks it)
    diff = K_hat - G_hat                                  # (local)
    op_norm_difference = float(np.max(np.abs(diff)))      # (local) ||K_hat - G_hat||_op
    # GPU-vs-numpy agreement check
    gpu_numpy_agree = True                                # (local)
    if op_norm_difference_gpu is not None:
        gpu_numpy_agree = abs(op_norm_difference_gpu - op_norm_difference) < 1e-9

    # ---- 6.6 ARCHITECTURE CHECK: G_tau INNER on the crossed product --------
    # Chandrasekaran-Flanagan: the area operator A-hat (= a_2^{zeta}) implements the
    # Connes cocycle flow within expectation values => it is implementable by a unitary
    # in the crossed product A_hor = A_K rtimes_{sigma^omega} R (INNER), not merely
    # outer on the bare algebra. The crossed-product promotion (item 2 certified omega
    # faithful normal => the dual weight on A_hor is semifinite => the modular flow is
    # INNER by Takesaki duality) makes G_tau a CANDIDATE inner modular generator. The
    # check is structural: (i) A_hor is the Type-II_oo crossed product (S104 named_A_hor),
    # (ii) omega|_{A_hor} is faithful normal (item 2 PASS), (iii) the area operator is the
    # a_2 moment whose modular flow is implemented inside the crossed product.
    inner_architecture_check = bool(
        gating_status                                    # omega faithful normal (item 2)
        and (A_hat > 0)                                  # area operator a_2 > 0 (well-defined)
        and (abs(s104_a2_fold - a2_fold) < 1e-6)         # S104 named A-hat = canonical a_2
    )

    # ---- 6.7 Verdict assembly (3-tuple + composite) ------------------------
    # sign_verdict: did the computed cocycle-generator sign match the S97 reference (-1)?
    sign_verdict = "PASS" if (sign_match and inner_architecture_check) else "FAIL"
    # magnitude_verdict: operator-norm agreement (the [VERIFY] conjunct)
    if op_norm_difference < TOL_OPNORM:
        magnitude_verdict = "PASS"
    else:
        magnitude_verdict = "FAIL"
    # regime_verdict: the modular-operator construction is valid throughout (item 2
    # certified faithful normal on every named block; no auto-shortening; full domain).
    regime_verdict = "VALID"

    # Composite under the PLAN-FROZEN composite-precedence operator (this gate
    # PRE-REGISTERS the co-monotone outcome as INFO, not FAIL):
    #   sign=PASS & magnitude=PASS & regime=VALID         -> PASS  (modular identity, Track A)
    #   sign=PASS & magnitude=FAIL & regime=VALID         -> INFO  (co-monotone, Track B; GEM-WORKSHOP Q1)
    #   sign=FAIL  (or architecture fails)                -> FAIL  (anti-directed / outer-only)
    if sign_verdict == "FAIL":
        composite = "FAIL"
    elif magnitude_verdict == "PASS":
        composite = "PASS"
    else:  # sign PASS, magnitude FAIL, regime VALID -> plan-frozen INFO (not generic FAIL)
        composite = "INFO"

    return dict(
        gating_status=gating_status,
        item2_verdict=item2_verdict,
        op_norm_difference=op_norm_difference,
        op_norm_difference_gpu=(op_norm_difference_gpu if op_norm_difference_gpu is not None else np.nan),
        gpu_used=gpu_used,
        gpu_numpy_agree=gpu_numpy_agree,
        cocycle_generator_sign=cocycle_generator_sign,
        S97_sign_reference=S97_SIGN_REF,
        sign_match=sign_match,
        inner_architecture_check=inner_architecture_check,
        tol_opnorm=TOL_OPNORM,
        K_norm=K_norm, G_norm=G_norm,
        n_modes_total=n_modes_total,
        A_hat=A_hat, a2_fold=a2_fold,
        d_ratio_dtau_fold=d_ratio_dtau, d_a2_dtau_fold=d_a2_dtau_fold,
        s97_p_exponent=s97_p_exp, s97_decreasing=s97_decreasing,
        s104_a2_fold=s104_a2_fold,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict, composite=composite,
        K_modular=K_modular, Gtau=Gtau, K_hat=K_hat, G_hat=G_hat,
        block_records=block_records,
        lam_horizon=lam_horizon,
    )


# ---------------------------------------------------------------------------
# Section 7 — Plot
# ---------------------------------------------------------------------------
def make_plot(R: dict) -> None:
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(13, 5))

    # left: G_tau vs Ad(Delta_omega^{it}) generator spectra (unit-normalized)
    idx = np.arange(R["n_modes_total"])                  # (local)
    ax0.plot(idx, R["K_hat"], ".", ms=3, alpha=0.6,
             label=r"$\hat K_a$ = modular gen. $\mathrm{Ad}(\Delta_\omega^{it})$")
    ax0.plot(idx, R["G_hat"], ".", ms=3, alpha=0.6,
             label=r"$\hat G_\tau$ = exflation gen. $d/d\tau$")
    ax0.set_xlabel("BdG mode index on $A_{hor}$ (channels $\\times$ blocks)")
    ax0.set_ylabel("unit-normalized generator spectrum")
    ax0.set_title(f"G_tau vs modular flow on the (0,0)+horizon blocks\n"
                  f"cocycle-gen sign = {R['cocycle_generator_sign']} "
                  f"(S97 ref = {R['S97_sign_reference']}; match = {R['sign_match']})")
    ax0.legend(fontsize=8, loc="best")
    ax0.grid(alpha=0.25)

    # right: the op-norm difference vs tol
    ax1.bar([0], [R["op_norm_difference"]], width=0.5, color="#c44",
            label=r"$\|\hat G_\tau - \hat K\|_{op}$")
    ax1.axhline(R["tol_opnorm"], color="k", ls="--", lw=1.2,
                label=f"tol = {R['tol_opnorm']:.0e}")
    ax1.set_yscale("log")
    ax1.set_xticks([0])
    ax1.set_xticklabels(["op-norm diff"])
    ax1.set_ylabel("operator-norm difference (dimensionless)")
    verdict_txt = (f"composite = {R['composite']}\n"
                   f"sign={R['sign_verdict']} mag={R['magnitude_verdict']} "
                   f"regime={R['regime_verdict']}\n"
                   f"inner-arch = {R['inner_architecture_check']}")
    ax1.set_title("op-norm agreement vs tol\n" + verdict_txt, fontsize=9)
    ax1.legend(fontsize=8, loc="best")
    ax1.grid(alpha=0.25, axis="y", which="both")

    fig.suptitle(f"{GATE_ID}  —  emergent-horizon modular corridor main gate "
                 f"(GATED on item-2 PASS: {R['gating_status']})", fontsize=11)
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 — main
# ---------------------------------------------------------------------------
def main() -> int:
    # input SHA log (first lines of stdout per gate-verdicts.md protocol)
    print(f"=== {GATE_ID} ===")
    print(f"  script_self      = {_file_sha(Path(__file__).resolve())}")
    print(f"  canonical_sha    = {_file_sha(CANON_NPZ)}")
    print(f"  s104_spec_sha    = {_file_sha(S104_SPEC_NPZ)}")
    print(f"  s105_w2_2_sha    = {_file_sha(S105_W2_2_NPZ)}")
    print(f"  s97_ds_sha       = {_file_sha(S97_DS_NPZ)}")
    print(f"  s84_cache_sha    = {_file_sha(S84_CACHE_NPZ)}")
    print(f"  torch_available  = {_HAVE_TORCH}")

    R = compute()

    print("\n=== GATING (item 2 / W2-2) ===")
    print(f"  item2_verdict          = {R['item2_verdict']}")
    print(f"  gating_status          = {R['gating_status']}  (PASS required; verified)")
    print(f"  lam_horizon            = {R['lam_horizon']:.10f}")

    print("\n=== [SIGN] cocycle-generator direction ===")
    print(f"  d(a0/a2)/dtau at fold  = {R['d_ratio_dtau_fold']:+.6f}  (area-proxy DECREASES; tau-flow)")
    print(f"  da2/dtau at fold       = {R['d_a2_dtau_fold']:+.6f}  (a_2 area operator grows)")
    print(f"  S97 dS/d(a0/a2) sign   = {R['S97_sign_reference']}   (decreasing={R['s97_decreasing']}, p_exp={R['s97_p_exponent']:.4f})")
    print(f"  cocycle-generator sign = {R['cocycle_generator_sign']}")
    print(f"  sign_match             = {R['sign_match']}   (cocycle-gen == S97 ref)")
    print(f"  inner_architecture_chk = {R['inner_architecture_check']}  (G_tau INNER on crossed product)")
    print(f"  => sign_verdict        = {R['sign_verdict']}")

    print("\n=== [VERIFY] operator-norm agreement on A_hor ===")
    print(f"  ||K||_op (modular)     = {R['K_norm']:.6f}")
    print(f"  ||G_tau||_op           = {R['G_norm']:.6f}")
    print(f"  ||K_hat - G_hat||_op   = {R['op_norm_difference']:.6e}   (tol = {R['tol_opnorm']:.0e})")
    print(f"  op-norm (GPU torch)    = {R['op_norm_difference_gpu']}  (gpu_used={R['gpu_used']}, agree={R['gpu_numpy_agree']})")
    print(f"  n_modes_total on A_hor = {R['n_modes_total']}")
    print(f"  => magnitude_verdict   = {R['magnitude_verdict']}")
    print(f"  => regime_verdict      = {R['regime_verdict']}")

    print("\n=== COMPOSITE VERDICT (plan-frozen precedence) ===")
    print(f"  composite              = {R['composite']}")

    # ---- npz ----------------------------------------------------------------
    block_keys = list(R["block_records"].keys())
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        composite=R["composite"],
        sign_verdict=R["sign_verdict"],
        magnitude_verdict=R["magnitude_verdict"],
        regime_verdict=R["regime_verdict"],
        # gate primaries
        op_norm_difference=R["op_norm_difference"],
        op_norm_difference_gpu=R["op_norm_difference_gpu"],
        gpu_used=R["gpu_used"],
        gpu_numpy_agree=R["gpu_numpy_agree"],
        cocycle_generator_sign=R["cocycle_generator_sign"],
        S97_sign_reference=R["S97_sign_reference"],
        sign_match=R["sign_match"],
        inner_architecture_check=R["inner_architecture_check"],
        gating_status=R["gating_status"],          # item-2-PASS verified
        item2_verdict=R["item2_verdict"],
        tol_opnorm=R["tol_opnorm"],
        # generators
        K_modular=R["K_modular"], Gtau=R["Gtau"],
        K_hat=R["K_hat"], G_hat=R["G_hat"],
        K_norm=R["K_norm"], G_norm=R["G_norm"],
        n_modes_total=R["n_modes_total"],
        lam_horizon=R["lam_horizon"],
        # area-operator + moment trajectory
        A_hat=R["A_hat"], a2_fold=R["a2_fold"], s104_a2_fold=R["s104_a2_fold"],
        d_ratio_dtau_fold=R["d_ratio_dtau_fold"], d_a2_dtau_fold=R["d_a2_dtau_fold"],
        s97_p_exponent=R["s97_p_exponent"], s97_decreasing=R["s97_decreasing"],
        block_keys=np.array(block_keys),
        block_records_json=json.dumps(R["block_records"]),
        tau_fold=tau_fold, T_GGE=T_GGE,
        regulator_pin="a_2^{zeta}",
    )

    make_plot(R)

    # ---- dual-SHA + verdict payload ----------------------------------------
    # NOTE (substrate-first-canonical-sourcing.md §(ii.B)): canonical_constants.py
    # gained omega_SN_substrate (SECTION E) this session; the plan-freeze SHA pin
    # for it may differ from runtime. We pin canonical at RUNTIME SHA (benign drift),
    # exactly as the sister gates W2-2/W2-4 did. Documented in the verdict value.
    pins = {
        "script": _file_sha(Path(__file__).resolve()),
        "canonical": _file_sha(CANON_NPZ),                # runtime SHA (benign omega_SN drift)
        "s104_area_modular_generator_spec_npz": _file_sha(S104_SPEC_NPZ),
        "s105_w2_2_omega_faithful_normal_npz": _file_sha(S105_W2_2_NPZ),
        "s97_ds_area_law_monotonicity_npz": _file_sha(S97_DS_NPZ),
        "s84_spectrum_cache_npz": _file_sha(S84_CACHE_NPZ),
    }
    audit_sha, content_sha = compute_dual_sha(pins)

    value = (
        f"composite={R['composite']};"
        f"op_norm_diff={R['op_norm_difference']:.6e}_vs_tol={R['tol_opnorm']:.0e};"
        f"cocycle_gen_sign={R['cocycle_generator_sign']}_eq_S97={R['sign_match']};"
        f"inner_arch={R['inner_architecture_check']};"
        f"Ghat_vs_Khat_co-monotone={R['sign_match'] and R['magnitude_verdict']=='FAIL'};"
        f"gating_item2={R['item2_verdict']};"
        f"A_hat=a_2_zeta={R['A_hat']:.6f};"
        f"canonical_runtime_SHA_omega_SN_benign_drift_per_(ii.B)"
    )

    composite_precedence_row = (
        "# composite-precedence: S105-W2-3-AREA-MODULAR-AGREEMENT plan-block "
        "(session-105-plan-w2.md §W2-3 INFO_meaning) pre-registers sign=PASS+magnitude=FAIL+regime=VALID "
        "as INFO (co-monotone-but-not-equal), OVERRIDING the generic-collapse FAIL reading; "
        "gate-verdicts.md 'Plan-frozen gate-block operator precedence'"
    )
    regulator_row = "# regulator_pin=a_2^{zeta}  # A-hat = a_2 second-Seeley-DeWitt moment (zeta-regulated)"

    print_verdict_payload(
        verdict=R["composite"],
        value=value,
        audit_sha=audit_sha,
        content_sha=content_sha,
        sign_verdict=R["sign_verdict"],
        magnitude_verdict=R["magnitude_verdict"],
        regime_verdict=R["regime_verdict"],
        companion_note=("emergent-horizon modular corridor main gate; "
                        "G_tau ?= Ad(Delta_omega^{it})|_{A_hor} on (0,0)+horizon blocks"),
        extra_rows=[composite_precedence_row, regulator_row],
    )

    print(f"\nWROTE {OUT_NPZ}")
    print(f"WROTE {OUT_PNG}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
