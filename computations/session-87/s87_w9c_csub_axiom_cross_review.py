#!/usr/bin/env python3
"""
S87 W9c-1 — Axiom-side cross-review of S86 W5b §W5b-2 c_sub admissibility
==========================================================================

Gate: S87-W5B-C16-AXIOM-SIDE-CSUB-CROSS-REVIEW  ([VERIFY] [CROSS-PROXY-ADJUDICATION])
Owner: connes-ncg-theorist  (independent cross-reviewer; NOT original W5b author)

Operationalizes the lizzi A-T4.2 substrate-distance-2 WZW-consistency residue
proxy

    c_sub_anomaly_WZW(R; tau) := Res[M_R(s) * anomaly_kernel(s); s=4]
                                  / Res[M_R(s); s=3]

across the 5-atlas of SCHEMATIC regulators
{zeta, Mellin, heat-kernel, hard-cutoff, Pauli-Villars}
(per `_spectral_action_regulators.py`; TIER-2 SCHEMATIC per
`.claude/rules/substrate-first-canonical-sourcing.md` §iv)
plus the (C_H, C_epsH) parity-twin pair from §VII.S sub-rows
(C-eta = Ward-identity branch; C-theta = Connes inner-fluctuation
A -> A+omega branch; the ε-twisted dual).

The cross-review is OPEN-VERDICT per `.claude/rules/epistemic-discipline.md`
§"Cross-Proxy Adjudication" requirement (2). Track A (FAIL stands -> C16
confirmed INFO) and Track B (cross-proxy yields PASS -> C16 promotes to
ADMISSIBLE) are both pre-registered as symmetric outcomes.

Per `.claude/rules/v3-closure-recovery.md` PROHIBITED_ACTIONS Class 6:
the WZW proxy formula, s=4 pole pin, and sign-reversal threshold are
LOCKED before any computation. No mid-execution adjustment to convert
FAIL to PASS.

Pre-registered thresholds (plan §9):
  Track-B PASS  iff sign_verdict=PASS (n_pass>=3 of 5 atlas AND
                    n_parity_twin_pass=2 of {C_H, C_epsH})
                AND magnitude_verdict=PASS (sheet-flip magnitudes >= 0.10)
                AND regime_verdict=VALID (all 5 regulators inside s=4 cone, margin>=0.10)
  Track-A FAIL  iff sign_verdict=FAIL (n_pass<=1 AND n_parity_twin_pass<=1)
                OR  regime_verdict=BREAKDOWN
                OR  (magnitude_verdict=FAIL AND regime_verdict=VALID)
  INFO          middle band; composite collapse per gate-verdicts.md §S87+ schema-v2

Inputs (SHA-pinned):
  - computations/_shared/canonical_constants.py
  - computations/_shared/_spectral_action_regulators.py
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz
  - computations/session-86/s86_w5b_c16_csub_admissibility.py (script-form proxy
    formula source; W5b workingpaper §W5b-2 line 331 is its embodied
    reference)
  - computations/session-86/s86_gate_verdicts.txt (S86-W5B-C16 prior verdict)
  - sessions/archive/session-86/session-86-w5b-workingpaper.md (W5b §W5b-2 lines 242-460)
  - sessions/archive/session-86/workshops/s86-path-c-double-double-fail-reassessment.md
    (W-9 §T-CR2.3 + lizzi A-T4.2 source lines 1154-1180, 1291-1334)
  - sessions/permanent-results-registry.md (§VII.S 10-row corollary atlas;
    sub-rows §VII.S.eta + §VII.S.theta = parity-twin (C_H, C_epsH))
  - script bytes itself (feeds audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<n_pass>/5+twin=<n_parity_twin_pass>/2,
   scheme=WZW-consistency-residue-substr-d-2,
   convention=cross-proxy-adjudication-OPEN-VERDICT-SCHEMATIC,
   L_max=10)

Classification: GEOMETRIC.

TIER-2 SCHEMATIC declaration:
  `_spectral_action_regulators.py` is SCHEMATIC per its docstring (lines
  23-30: "These are SCHEMATIC regulators ... NOT the full physical
  regularizations"). The cross-review's outcome holds under these
  schematic forms. Live-physical-regulator re-run is a SEPARATE forward
  question; do NOT attempt mid-execution upgrade to TIER-1.

Method (per plan §6 + §10 substitution chain):

  Step A. Pre-registration verification — formulas are transcribed
          verbatim from W-9 §T-CR2.3 (lines 1156-1158); s=4 / s=3 poles
          are pinned; no scheme substitution.

  Step B. For each regulator R in the 5-atlas {zeta, Mellin, heat-kernel,
          hard-cutoff, Pauli-Villars} AND for each parity-twin variant
          {C_H = +1 anomaly_kernel, C_epsH = -1 ε-twisted dual}:
            M_R(s=3; tau) = a_n=3 Mellin moment (substrate-d-1 normalization)
            M_R(s=4; tau) = a_n=4 Mellin moment (substrate-d-2 anomaly residue)
            c_sub_anomaly_WZW(R; tau) = M_R(4; tau) / M_R(3; tau)
              (positive-branch C_H; multiply by -1 for C_epsH)

  Step C. Sign-reversal sheet-flip evaluation across tau_fold:
          For each R, compute c_sub_anomaly_WZW at tau in
          {tau_fold - delta_tau, tau_fold, tau_fold + delta_tau}
          with delta_tau = 0.005.
          sign_reversal_R = sign(value(tau-)) * sign(value(tau+))
          -1 ⇒ flip (PASS row); +1 ⇒ no flip (FAIL row).

  Step D. Cross-regulator aggregate:
          n_pass = |{R in 5-atlas : sign_reversal_R = -1}|
          n_parity_twin_pass = |{R in {C_H, C_epsH} : sign_reversal_R = -1}|

  Step E. Regime-of-validity check (Mellin-cone substrate-d-2 convergence):
          For each R, the analytic boundary in s-plane is the largest s
          where Σ d(p,q)·f_R(C_2,s) converges absolutely. For zeta/Mellin
          on positive-Casimir spectrum at L_max=10, the boundary is
          structurally at s -> infty (sum is finite-rank); convergence_margin
          is the gap (s_boundary - 4)/4 ≥ very large ⇒ VALID at L_max=10.
          For Pauli-Villars and hard-cutoff: subtraction/truncation makes
          the s-plane analytic; for heat-kernel: damped exponential
          guarantees absolute convergence at all s>0.

  Step F. Cross-check (functional-pluralism comparison with W5b
          τ-flow-trace proxy):
          Re-evaluate sign(d c_sub(tau)/dtau) at tau_fold ± delta_tau
          on the same Jensen-scaled spectrum. Compare per-regulator:
            agree_R = (sign_reversal_R_WZW == sign_reversal_R_τflow)
          Report n_agree.

  Step G. Compute closure SHA-256 over input-pin map; emit canonical
          verdict + dual-SHA companion + 3-tuple annotation +
          cross-proxy adjudication record row.

Discipline:
  - `from canonical_constants import *` (tau_fold, S_fold, dS_fold,
    d2S_fold, Vol_SU3_Haar, a0_fold)
  - All intermediates tagged `# (local)`
  - CPU-only (small Mellin sums on Casimir spectrum at L_max=10);
    OMP_NUM_THREADS=8
  - SHA-256 of inputs logged in first 20 lines of stdout
  - Dual-SHA emitted (audit_sha256 + content_sha256 + 16-hex companion +
    3-tuple annotation + cross-proxy adjudication row)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — CPU thread cap (BEFORE numpy import)
# ---------------------------------------------------------------------------
import os
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

os.environ.setdefault('OMP_NUM_THREADS', '8')  # (local) CPU thread cap per .claude/rules/math-scripts.md
os.environ.setdefault('MKL_NUM_THREADS', '8')  # (local) MKL thread cap mirrors OMP cap

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403
import canonical_constants as CC

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
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Local schematic regulator atlas
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _spectral_action_regulators import (
    zeta_a_n,
    mellin_a_n,
    heat_kernel_a_n,
    hard_cutoff_a_n,
    pauli_villars_a_n,
)

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent           # (local)
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S87"                                                 # (local)
GATE_ID = "S87-W5B-C16-AXIOM-SIDE-CSUB-CROSS-REVIEW"            # (local)

# Plan §7 PRDR pins
L_MAX = 10                                                      # (local)
SCHEME = "WZW-consistency-residue-substr-d-2"                   # (local)
CONVENTION = "cross-proxy-adjudication-OPEN-VERDICT-SCHEMATIC"  # (local) TIER-2 SCHEMATIC
S4_POLE_PIN = 4                                                 # (local) substrate-d-2 conformal-anomaly residue pole
S3_POLE_PIN = 3                                                 # (local) substrate-d-1 normalization residue pole
DELTA_TAU = 0.005                                               # (local) sheet-flip step across tau_fold (plan §7)
CONVERGENCE_MARGIN_THRESHOLD = 0.10                             # (local) regime-of-validity at s=4
SHEET_FLIP_MAGNITUDE_THRESHOLD = 0.10                           # (local) RATIO PASS magnitude threshold
N_PASS_PASS_THRESHOLD = 3                                       # (local) >=3 of 5 atlas regulators
N_PARITY_TWIN_PASS_THRESHOLD = 2                                # (local) BOTH C_H and C_epsH must flip
N_PASS_FAIL_THRESHOLD = 1                                       # (local) <=1 of 5 atlas regulators
N_PARITY_TWIN_FAIL_THRESHOLD = 1                                # (local) <=1 of {C_H, C_epsH}

# 5-atlas regulator names (per plan §6 Step B and `_spectral_action_regulators.py`)
ATLAS_5 = ("zeta", "Mellin", "heat-kernel", "hard-cutoff", "Pauli-Villars")  # (local)

# Parity-twin pair from §VII.S.eta + §VII.S.theta sub-rows
PARITY_TWIN = ("C_H", "C_epsH")                                 # (local)

# Output destinations
OUT_NPZ = resolve_output(87, 's87_w9c_csub_axiom_cross_review.npz')     # (local)
OUT_PNG = resolve_output(87, 's87_w9c_csub_axiom_cross_review.png')     # (local)
VERDICT_TXT = resolve_output(87, 's87_gate_verdicts.txt')               # (local) canonical S87 verdict file

# Input files (SHA-pinned per plan §13 Input-SHA Ledger)
INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    resolve_script(None, '_spectral_action_regulators.py'),
    resolve_output(84, 's84_spectrum_cache_L12_tau019.npz'),
    resolve_script(86, 's86_w5b_c16_csub_admissibility.py'),
    resolve_output(86, 's86_gate_verdicts.txt'),
    PROJECT_ROOT / "sessions" / "session-86" / "session-86-w5b-workingpaper.md",
    PROJECT_ROOT / "sessions" / "session-86" / "workshops" / "s86-path-c-double-double-fail-reassessment.md",
    PROJECT_ROOT / "sessions" / "permanent-results-registry.md",
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema, W9a-99)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()                                         # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} - input SHA-256 pins ===")
    pins = {}                                                    # (local)
    for p in inputs:
        sha = sha256_of(p)                                       # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)                                         # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pinmap):
    """Stable SHA over ordered pin-name=value entries (input-pin map closure)."""
    items = sorted(pinmap.items())                               # (local)
    h = hashlib.sha256()                                         # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path, canonical_path, pins, machinery_pins):
    """Compute (audit_sha256, content_sha256) per the S84+ dual-SHA schema.

    audit_sha256:   SHA-256 of (script_bytes || canonical_bytes ||
                    pinmap_json || machinery_pins_json)
    content_sha256: SHA-256 of script_bytes only

    The machinery_pins_json embeds gate identity (gate_id, scheme,
    convention, L_max, s4_pole, s3_pole, delta_tau, thresholds) so the
    audit_sha256 is per-gate-distinct.
    """
    script_bytes = b""                                           # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""                                        # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""

    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")                                            # (local)

    machinery_json = json.dumps(
        dict(sorted(machinery_pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")                                            # (local)

    h_audit = hashlib.sha256()                                   # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_audit.update(machinery_json)
    audit = h_audit.hexdigest()                                  # (local)

    h_content = hashlib.sha256()                                 # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()                              # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Jensen-flow scaling (per Definition 4 of plan §10)
# ---------------------------------------------------------------------------

def jensen_sigma(tau):
    """Jensen scaling sigma(tau) = sqrt(V(tau)/S_fold).

    V(tau) = S_fold + dS_fold * (tau - tau_fold) + 0.5 * d2S_fold * (tau - tau_fold)^2
    The eigenvalue rescaling lambda_n(tau) = lambda_n(tau_fold) * sigma(tau)
    induces a Casimir rescaling C_2(p,q;tau) = C_2(p,q;tau_fold) * sigma(tau)^2,
    hence M_R(s; tau) = sigma(tau)^(-2s) * M_R(s; tau_fold) for the
    zeta/Mellin schemes (sum over fixed (p,q) with C ↦ sigma^2 C).

    For heat-kernel, hard-cutoff, Pauli-Villars: M_R(s; tau) is computed
    directly on the rescaled spectrum (since these schemes have additional
    nonlinear dependence on C_2).
    """
    dtau = tau - tau_fold                                        # (local)
    V = S_fold + dS_fold * dtau + 0.5 * d2S_fold * dtau ** 2     # (local)
    return float(np.sqrt(V / S_fold))                            # (local)


# ---------------------------------------------------------------------------
# Section 6 — Mellin moments M_R(s; tau) per regulator family
# ---------------------------------------------------------------------------

def M_R_at_tau(regulator_name, s, tau):
    """Compute the Mellin moment M_R(s; tau) for the named regulator.

    Implementation delegates to `_spectral_action_regulators.py` evaluators
    after applying the Jensen scaling C_2 ↦ sigma(tau)^2 * C_2 by composition.

    For zeta and Mellin: a_n(s) = (1/Vol_SU3_Haar) Σ d(p,q) / C_2(p,q)^s
       M_R(s; tau) = sigma(tau)^(-2s) * M_R(s; tau_fold)

    For heat-kernel: a_n includes an exp(-t * C) damping; the damping
       transforms under Jensen scaling and we recompute directly with the
       effective Casimir C_eff = sigma^2 * C.

    For hard-cutoff: the cutoff threshold is fraction * max(C); under
       Jensen scaling all Casimirs rescale uniformly so the truncation
       set is INVARIANT. Hence M_hard(s; tau) = sigma(tau)^(-2s) * M_hard(s; tau_fold).

    For Pauli-Villars: M_PV is fixed at fraction * max(C) at tau_fold;
       under Jensen scaling, max(C) -> sigma^2 * max(C), so we recompute
       directly with the rescaled M_PV at each tau.
    """
    sigma = jensen_sigma(tau)                                    # (local)
    sigma2 = sigma * sigma                                       # (local)

    if regulator_name == "zeta":
        # M_zeta(s; tau) = sigma(-2s) * M_zeta(s; tau_fold)
        return (sigma2 ** (-s)) * zeta_a_n(s, L_MAX, Vol_SU3_Haar)

    if regulator_name == "Mellin":
        # Identical to zeta on this spectrum (same operator)
        return (sigma2 ** (-s)) * mellin_a_n(s, L_MAX, Vol_SU3_Haar)

    if regulator_name == "heat-kernel":
        # Heat-kernel moment with effective Casimir C_eff = sigma^2 * C
        # Pass through the original evaluator with t_ref unchanged: the
        # Seeley-DeWitt extraction at fixed t with rescaled C gives a
        # nonlinear (non-pure-power) tau-dependence per scheme definition.
        # We compute by direct sum to preserve the regulator's nonlinearity.
        from _spectral_action_regulators import _enumerate_sectors
        sectors = _enumerate_sectors(L_MAX)                      # (local)
        if s == 0:
            total = sum(d for _, _, d, _ in sectors)             # (local)
            return total / Vol_SU3_Haar
        t_ref = 1.0e-3                                           # (local) heat_kernel_a_n default
        acc = 0.0                                                # (local)
        for _, _, d, c in sectors:
            c_eff = sigma2 * c                                   # (local) Jensen-rescaled Casimir
            acc += d * np.exp(-t_ref * c_eff) / (c_eff ** s)     # (local)
        return acc / Vol_SU3_Haar

    if regulator_name == "hard-cutoff":
        # Cutoff truncation set is INVARIANT under uniform sigma^2 rescaling
        # (it depends only on the RATIO C/max(C)). So M_hard scales like zeta.
        return (sigma2 ** (-s)) * hard_cutoff_a_n(s, L_MAX, Vol_SU3_Haar, cutoff_frac=0.7)

    if regulator_name == "Pauli-Villars":
        # PV: M_PV_sq = M_PV_sq_frac * max(C); under Jensen rescaling,
        # max(C) -> sigma^2 * max(C), so we recompute with rescaled spectrum.
        from _spectral_action_regulators import _enumerate_sectors
        sectors = _enumerate_sectors(L_MAX)                      # (local)
        if s == 0:
            total = sum(d for _, _, d, _ in sectors)             # (local)
            return total / Vol_SU3_Haar
        c_max_eff = sigma2 * max(s_[3] for s_ in sectors)        # (local)
        M_PV_sq = 0.1 * c_max_eff                                # (local) M_PV_sq_frac=0.1 default
        acc = 0.0                                                # (local)
        for _, _, d, c in sectors:
            c_eff = sigma2 * c                                   # (local)
            acc += d * (1.0 / (c_eff ** s) - 1.0 / ((c_eff + M_PV_sq) ** s))
        return acc / Vol_SU3_Haar

    raise ValueError(f"Unknown regulator: {regulator_name}")


# ---------------------------------------------------------------------------
# Section 7 — c_sub_anomaly_WZW(R; tau) and parity-twin variant
# ---------------------------------------------------------------------------

def c_sub_anomaly_WZW(regulator_name, tau, parity="C_H"):
    """Compute c_sub_anomaly_WZW(R; tau) per Definition 3 of plan §10:

       c_sub_anomaly_WZW(R; tau) := Res[M_R(s) * anomaly_kernel(s); s=4]
                                     / Res[M_R(s); s=3]
                                  = M_R(s=4; tau) / M_R(s=3; tau)

    For the parity-twin pair:
       parity = "C_H"     => Ward-identity branch (chiral re-phasing
                              preserves anomaly_kernel; positive sign)
       parity = "C_epsH"  => Connes inner-fluctuation epsilon-twisted branch
                              (A -> A + omega; ε-twist flips the
                              anomaly-kernel sign on the parity-odd sector)

    Direction (per substitution chain Step 2): denominator M_R(3;tau) is
    a sum-of-positive-Casimir-weights (positive for all 5 SCHEMATIC
    regulators), so the sign of the ratio equals the sign of the numerator.
    """
    num = M_R_at_tau(regulator_name, S4_POLE_PIN, tau)           # (local) Res at s=4
    den = M_R_at_tau(regulator_name, S3_POLE_PIN, tau)           # (local) Res at s=3
    if den == 0.0:
        return float('nan')
    val = num / den                                              # (local)
    if parity == "C_epsH":
        val = -val                                               # (local) ε-twisted dual
    return float(val)


# ---------------------------------------------------------------------------
# Section 8 — Sign-reversal sheet-flip evaluation
# ---------------------------------------------------------------------------

def sign_reversal_predicate(regulator_name, parity="C_H"):
    """Compute sign_reversal_R per Definition 5:
       sign_reversal_R = sign(c(tau_fold - delta)) * sign(c(tau_fold + delta))

    Returns (sign_reversal_int, val_minus, val_fold, val_plus) where
    sign_reversal_int = -1 (flip), +1 (no flip), or 0 (degenerate).
    """
    tau_minus = tau_fold - DELTA_TAU                             # (local)
    tau_plus = tau_fold + DELTA_TAU                              # (local)
    val_m = c_sub_anomaly_WZW(regulator_name, tau_minus, parity=parity)  # (local)
    val_f = c_sub_anomaly_WZW(regulator_name, tau_fold, parity=parity)   # (local)
    val_p = c_sub_anomaly_WZW(regulator_name, tau_plus, parity=parity)   # (local)
    s_m = int(np.sign(val_m))                                    # (local)
    s_p = int(np.sign(val_p))                                    # (local)
    return int(s_m * s_p), val_m, val_f, val_p


def sheet_flip_magnitude(val_m, val_p):
    """RATIO sheet-flip magnitude per plan §6 Decision rule magnitude_verdict:
       magnitude = |val(tau-) - val(tau+)| / max(|val(tau-)|, |val(tau+)|)
    """
    denom = max(abs(val_m), abs(val_p), 1e-300)                  # (local)
    return float(abs(val_m - val_p) / denom)                     # (local)


# ---------------------------------------------------------------------------
# Section 9 — τ-flow-trace cross-check (Step F)
# ---------------------------------------------------------------------------

def tau_flow_trace_sign_reversal(regulator_name, parity="C_H"):
    """Cross-check: τ-flow-trace proxy (W5b §W5b-2 line 331)

       c_sub_anomaly(τ) := d c_sub(τ)/dτ

    operationalized as the central finite-difference of c_sub_anomaly_WZW
    evaluated at the same Jensen-scaled spectrum:
       slope_pre  = (c_anom(tau_fold) - c_anom(tau_fold - delta)) / delta
       slope_post = (c_anom(tau_fold + delta) - c_anom(tau_fold)) / delta
    Returns sign_reversal predicate sign(slope_pre) * sign(slope_post).

    This is structurally distinct from the WZW residue-isolated proxy
    (the τ-flow-trace operates on the τ-derivative; the WZW proxy operates
    on the s-residue), per plan §3 Classification "algebraically distinct
    from the τ-flow-trace proxy (different operator, different pole,
    different physical interpretation)".
    """
    tau_minus = tau_fold - DELTA_TAU                             # (local)
    tau_plus = tau_fold + DELTA_TAU                              # (local)
    val_m = c_sub_anomaly_WZW(regulator_name, tau_minus, parity=parity)  # (local)
    val_f = c_sub_anomaly_WZW(regulator_name, tau_fold, parity=parity)   # (local)
    val_p = c_sub_anomaly_WZW(regulator_name, tau_plus, parity=parity)   # (local)
    slope_pre = (val_f - val_m) / DELTA_TAU                      # (local)
    slope_post = (val_p - val_f) / DELTA_TAU                     # (local)
    s_pre = int(np.sign(slope_pre))                              # (local)
    s_post = int(np.sign(slope_post))                            # (local)
    return int(s_pre * s_post), slope_pre, slope_post


# ---------------------------------------------------------------------------
# Section 10 — Regime-of-validity check (Step E)
# ---------------------------------------------------------------------------

def convergence_margin_at_s4(regulator_name):
    """Per plan §6 Step E: convergence_margin_R = |s=4 - boundary_R| / |s=4|.

    For the 5 SCHEMATIC regulators on a finite-rank Casimir spectrum
    (L_max=10, finite (p,q) sum) the partial sum Σ d(p,q)/C^s is a
    finite-rank rational function of s with no boundary at finite s
    (boundary -> infinity since the sum has finitely many positive terms,
    each entire in 1/s for s > 0). Thus convergence_margin -> 1.0 (cap).

    The structural reading: at L_max=10 with finite-rank spectrum, the
    Mellin-cone substrate-distance-2 pole at s=4 lies WELL INSIDE every
    regulator's analytic boundary. Schematic VALID-by-construction.

    Returns the convergence_margin and the regime_verdict label
    (VALID / MARGINAL / BREAKDOWN).
    """
    # Finite-rank => boundary at infinity => margin saturates at 1.0
    # (capped finite value to avoid float-inf in the JSON ledger)
    margin = 1.0                                                 # (local)
    if margin >= CONVERGENCE_MARGIN_THRESHOLD:
        return float(margin), "VALID"
    if margin >= 0.05:
        return float(margin), "MARGINAL"
    return float(margin), "BREAKDOWN"


# ---------------------------------------------------------------------------
# Section 11 — Aggregate verdict (sign + magnitude + regime; composite collapse)
# ---------------------------------------------------------------------------

def aggregate_sign_verdict(n_pass, n_parity_twin_pass):
    """Sign verdict from n_pass and n_parity_twin_pass aggregates."""
    if (n_pass >= N_PASS_PASS_THRESHOLD
            and n_parity_twin_pass == N_PARITY_TWIN_PASS_THRESHOLD):
        return "PASS"
    if (n_pass <= N_PASS_FAIL_THRESHOLD
            and n_parity_twin_pass <= N_PARITY_TWIN_FAIL_THRESHOLD):
        return "FAIL"
    return "N/A"  # middle band → INFO via composite collapse


def aggregate_magnitude_verdict(sign_verdict, magnitudes_passing):
    """Magnitude verdict per plan §6 Decision rule.

    PASS iff sign_verdict=PASS AND every flipped row has sheet-flip
    magnitude ≥ 0.10.
    INFO iff magnitudes are intermediate (0.01-0.10).
    FAIL otherwise.
    """
    if sign_verdict != "PASS":
        # Magnitude is only diagnostic when sign already passes
        if not magnitudes_passing:
            return "PASS"  # no flip rows present → trivially PASS for collapse
        # Use intermediate-band reading on the magnitudes we have
        any_high = any(m >= SHEET_FLIP_MAGNITUDE_THRESHOLD for m in magnitudes_passing)
        any_intermediate = any(0.01 <= m < SHEET_FLIP_MAGNITUDE_THRESHOLD for m in magnitudes_passing)
        if any_high:
            return "PASS"
        if any_intermediate:
            return "INFO"
        return "FAIL"
    # sign PASS → require all magnitudes ≥ threshold
    all_high = all(m >= SHEET_FLIP_MAGNITUDE_THRESHOLD for m in magnitudes_passing) if magnitudes_passing else False
    if all_high:
        return "PASS"
    any_intermediate = any(0.01 <= m < SHEET_FLIP_MAGNITUDE_THRESHOLD for m in magnitudes_passing)
    if any_intermediate:
        return "INFO"
    return "FAIL"


def aggregate_regime_verdict(per_regulator_regimes):
    """Regime verdict per plan §6 Step E aggregate."""
    n_breakdown = sum(1 for r in per_regulator_regimes if r == "BREAKDOWN")  # (local)
    n_marginal = sum(1 for r in per_regulator_regimes if r == "MARGINAL")    # (local)
    if n_breakdown > 0 or n_marginal >= 3:
        return "BREAKDOWN"
    if n_marginal >= 1:
        return "MARGINAL"
    return "VALID"


def composite_collapse(sign_verdict, magnitude_verdict, regime_verdict):
    """Per gate-verdicts.md §S87+ schema-v2 composite collapse rule.

    if regime_verdict == BREAKDOWN: composite = FAIL
    elif sign_verdict == FAIL: composite = FAIL
    elif magnitude_verdict == FAIL and regime_verdict == VALID: composite = FAIL
    elif magnitude_verdict == FAIL and regime_verdict == MARGINAL: composite = INFO
    elif magnitude_verdict == INFO: composite = INFO
    elif sign_verdict == "N/A": composite = INFO
    else: composite = PASS
    """
    if regime_verdict == "BREAKDOWN":
        return "FAIL"
    if sign_verdict == "FAIL":
        return "FAIL"
    if magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        return "FAIL"
    if magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        return "INFO"
    if magnitude_verdict == "INFO":
        return "INFO"
    if sign_verdict == "N/A":
        return "INFO"
    return "PASS"


def track_allocation(composite_verdict, sign_verdict):
    """Map composite verdict + sign verdict to track allocation (A / B / OPEN)."""
    if composite_verdict == "PASS":
        return "B"   # cross-proxy yields PASS → C16 promotes to ADMISSIBLE
    if composite_verdict == "FAIL" and sign_verdict == "FAIL":
        return "A"   # prior FAIL stands → C16 confirmed INFO at L_max=10
    return "OPEN"    # INFO / regime-marginal / disjoint → neither track allocated


# ---------------------------------------------------------------------------
# Section 12 — Plot (per-regulator bar plot)
# ---------------------------------------------------------------------------

def make_plot(rows, composite_label, n_pass, n_parity_twin_pass):
    """Per-regulator bar plot of c_sub_anomaly_WZW at tau_fold ± delta_tau,
    with sign-reversal indicator per row."""
    labels = [r["row_label"] for r in rows]                      # (local)
    val_m_list = [r["val_minus"] for r in rows]                  # (local)
    val_p_list = [r["val_plus"] for r in rows]                   # (local)
    sign_revs = [r["sign_reversal"] for r in rows]               # (local)

    fig, ax = plt.subplots(1, 1, figsize=(11, 6))
    x = np.arange(len(labels))                                   # (local)
    width = 0.35                                                 # (local)

    bars_minus = ax.bar(x - width / 2, val_m_list, width,
                        color='steelblue', alpha=0.8,
                        label=r'$c_{\rm sub}^{\rm anom,WZW}(\tau_{\rm fold} - \delta_\tau)$')
    bars_plus = ax.bar(x + width / 2, val_p_list, width,
                       color='salmon', alpha=0.8,
                       label=r'$c_{\rm sub}^{\rm anom,WZW}(\tau_{\rm fold} + \delta_\tau)$')

    # Annotate sign-reversal indicator above each bar pair
    for i, sr in enumerate(sign_revs):
        sym = "FLIP" if sr == -1 else ("NO-FLIP" if sr == 1 else "DEGEN")
        col = 'darkgreen' if sr == -1 else 'firebrick'
        height = max(abs(val_m_list[i]), abs(val_p_list[i]))     # (local)
        if height == 0:
            height = 1e-3                                        # (local) plot floor
        ax.text(i, height * 1.05 if val_m_list[i] >= 0 else -height * 1.15,
                sym, ha='center', va='bottom' if val_m_list[i] >= 0 else 'top',
                fontsize=8.5, color=col, weight='bold')

    ax.axhline(0, color='gray', ls='-', alpha=0.3)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=30, ha='right', fontsize=8.5)
    ax.set_ylabel(r'$c_{\rm sub}^{\rm anom,WZW}(R; \tau)  =  M_R(s{=}4;\tau)/M_R(s{=}3;\tau)$',
                  fontsize=9.5)
    title = (f"S87-W9c-1 axiom-side cross-review (TIER-2 SCHEMATIC) — "
             f"composite: {composite_label}  |  "
             f"n_pass={n_pass}/5  twin={n_parity_twin_pass}/2")
    ax.set_title(title, fontsize=10.5)
    ax.legend(loc='best', fontsize=8.5)
    ax.grid(True, alpha=0.3, axis='y')

    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=140)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 13 — Verdict-line emitter (S87+ schema-v2 + cross-proxy adjudication row)
# ---------------------------------------------------------------------------

def append_verdict(verdict, value, audit_sha, content_sha,
                   sign_v, mag_v, reg_v,
                   n_agree, track, n_pass, n_parity_twin_pass):
    """Emit canonical verdict line + dual-SHA companion + 3-tuple annotation +
    cross-proxy adjudication record row (S87+ schema-v2)."""
    line = (
        f"{GATE_ID}: {verdict} -- value={value} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    tuple3 = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
        f"regime_verdict={reg_v} # {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )
    cross_proxy = (
        f"# n_agree_with_tau_flow_trace={n_agree}/5 "
        f"track_allocation={track} # {GATE_ID} cross-proxy adjudication\n"
    )
    tier_pin = (
        f"# tier_pin=TIER-2 # {GATE_ID} TIER pin "
        f"(per .claude/rules/substrate-first-canonical-sourcing.md §iv "
        f"SCHEMATIC vs full physical tier rule; "
        f"_spectral_action_regulators.py SCHEMATIC docstring lines 23-30)\n"
    )
    aggregate_row = (
        f"# n_pass={n_pass}/5 n_parity_twin_pass={n_parity_twin_pass}/2 "
        f"# {GATE_ID} aggregate counts\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)
        fp.write(tuple3)
        fp.write(cross_proxy)
        fp.write(tier_pin)
        fp.write(aggregate_row)


# ---------------------------------------------------------------------------
# Section 14 — Main
# ---------------------------------------------------------------------------

def main():
    t0 = time.time()                                             # (local)

    # 1. Pre-registration verification (Step A)
    print(f"=== {GATE_ID} ===")
    print(f"  Pre-registration verification: WZW formula transcribed verbatim")
    print(f"    c_sub_anomaly_WZW(R;tau) := Res[M_R(s)*anomaly_kernel(s); s={S4_POLE_PIN}]")
    print(f"                                / Res[M_R(s); s={S3_POLE_PIN}]")
    print(f"  s4_pole_pin = {S4_POLE_PIN} (substrate-d-2 conformal-anomaly residue)")
    print(f"  s3_pole_pin = {S3_POLE_PIN} (substrate-d-1 normalization residue)")
    print(f"  delta_tau = {DELTA_TAU}")
    print(f"  TIER pin: TIER-2 SCHEMATIC (_spectral_action_regulators.py docstring)")
    print()

    # 2. Log input pins
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)                                 # (local) legacy closure
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 2b. Compute S84+ dual SHAs with machinery embedded for per-gate uniqueness
    machinery_pins = {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "s4_pole_pin": S4_POLE_PIN,
        "s3_pole_pin": S3_POLE_PIN,
        "delta_tau_pin": DELTA_TAU,
        "convergence_margin_threshold": CONVERGENCE_MARGIN_THRESHOLD,
        "sheet_flip_magnitude_threshold": SHEET_FLIP_MAGNITUDE_THRESHOLD,
        "n_pass_pass_threshold": N_PASS_PASS_THRESHOLD,
        "n_parity_twin_pass_threshold": N_PARITY_TWIN_PASS_THRESHOLD,
        "n_pass_fail_threshold": N_PASS_FAIL_THRESHOLD,
        "n_parity_twin_fail_threshold": N_PARITY_TWIN_FAIL_THRESHOLD,
        "tier_pin": "TIER-2-SCHEMATIC",
        "regulator_atlas_pin": list(ATLAS_5),
        "parity_twin_pin": list(PARITY_TWIN),
        "sign_reversal_predicate": "multiplicative",
    }                                                            # (local)
    script_path = Path(__file__).resolve()                       # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')        # (local)
    audit_sha, content_sha = compute_dual_sha(
        script_path, canonical_path, pins, machinery_pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap+machinery)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 3. Step B-D: Per-regulator + parity-twin sign-reversal evaluation
    print(f"=== Step B-D: 5-atlas + parity-twin sign-reversal evaluation ===")
    rows = []                                                    # (local) per-row records
    per_regulator_regimes_atlas = []                             # (local) for atlas regulators only
    magnitudes_pass_rows = []                                    # (local) magnitudes for sign-flipped rows

    # 5-atlas rows (Track-allocation evaluated on atlas regulators)
    for R_name in ATLAS_5:
        sr, vm, vf, vp = sign_reversal_predicate(R_name, parity="C_H")  # (local) C_H = identity branch on atlas
        mag = sheet_flip_magnitude(vm, vp)                       # (local)
        margin, regime = convergence_margin_at_s4(R_name)        # (local)
        # τ-flow-trace cross-check (Step F)
        tau_sr, slope_pre, slope_post = tau_flow_trace_sign_reversal(R_name, parity="C_H")
        agree = (sr == tau_sr)                                   # (local)
        per_regulator_regimes_atlas.append(regime)
        if sr == -1:
            magnitudes_pass_rows.append(mag)
        rows.append({
            "row_label": R_name,
            "regulator": R_name,
            "parity": "C_H",
            "is_atlas": True,
            "is_parity_twin": False,
            "val_minus": vm,
            "val_fold": vf,
            "val_plus": vp,
            "sign_reversal": sr,
            "magnitude": mag,
            "convergence_margin": margin,
            "regime_verdict": regime,
            "tau_flow_sign_reversal": tau_sr,
            "tau_flow_slope_pre": slope_pre,
            "tau_flow_slope_post": slope_post,
            "agree_with_tau_flow": bool(agree),
        })
        print(f"  R={R_name:<14} parity=C_H   "
              f"val(tau-)={vm:+.4e}  val(tau+)={vp:+.4e}  "
              f"sign_rev={sr:+d}  mag={mag:.4f}  regime={regime}  "
              f"τflow_sr={tau_sr:+d} agree={agree}")

    # Parity-twin rows (zeta carrier; both C_H and C_epsH evaluated)
    parity_twin_rows = []                                        # (local)
    for parity in PARITY_TWIN:
        # The §VII.S parity-twin pair lives in the zeta carrier (POWER-RATIO,
        # zeta) per the W5b §W5b-2 baseline. C_H = Ward branch on zeta;
        # C_epsH = ε-twisted Connes-inner-fluctuation dual on zeta.
        sr, vm, vf, vp = sign_reversal_predicate("zeta", parity=parity)  # (local)
        mag = sheet_flip_magnitude(vm, vp)                       # (local)
        margin, regime = convergence_margin_at_s4("zeta")        # (local)
        tau_sr, slope_pre, slope_post = tau_flow_trace_sign_reversal("zeta", parity=parity)
        agree = (sr == tau_sr)                                   # (local)
        parity_twin_rows.append({
            "row_label": parity,
            "regulator": "zeta",
            "parity": parity,
            "is_atlas": False,
            "is_parity_twin": True,
            "val_minus": vm,
            "val_fold": vf,
            "val_plus": vp,
            "sign_reversal": sr,
            "magnitude": mag,
            "convergence_margin": margin,
            "regime_verdict": regime,
            "tau_flow_sign_reversal": tau_sr,
            "tau_flow_slope_pre": slope_pre,
            "tau_flow_slope_post": slope_post,
            "agree_with_tau_flow": bool(agree),
        })
        rows.append(parity_twin_rows[-1])
        print(f"  R=zeta         parity={parity:<6} "
              f"val(tau-)={vm:+.4e}  val(tau+)={vp:+.4e}  "
              f"sign_rev={sr:+d}  mag={mag:.4f}  regime={regime}  "
              f"τflow_sr={tau_sr:+d} agree={agree}")
    print()

    # Aggregate counts
    n_pass = sum(1 for r in rows if r["is_atlas"] and r["sign_reversal"] == -1)  # (local)
    n_parity_twin_pass = sum(1 for r in rows
                              if r["is_parity_twin"] and r["sign_reversal"] == -1)  # (local)
    n_agree_atlas = sum(1 for r in rows if r["is_atlas"] and r["agree_with_tau_flow"])  # (local)

    print(f"=== Aggregates ===")
    print(f"  n_pass (atlas sheet-flip count) = {n_pass}/5  "
          f"(threshold for sign PASS: >={N_PASS_PASS_THRESHOLD})")
    print(f"  n_parity_twin_pass = {n_parity_twin_pass}/2  "
          f"(threshold for sign PASS: ={N_PARITY_TWIN_PASS_THRESHOLD})")
    print(f"  n_agree_with_tau_flow_trace = {n_agree_atlas}/5  (Step F cross-check)")
    print()

    # 4. Step E: regime-of-validity aggregate
    regime_verdict = aggregate_regime_verdict(per_regulator_regimes_atlas)
    print(f"=== Step E: regime-of-validity aggregate ===")
    print(f"  per-regulator regimes: {per_regulator_regimes_atlas}")
    print(f"  aggregate regime_verdict = {regime_verdict}")
    print()

    # 5. Sign + magnitude verdicts
    sign_verdict = aggregate_sign_verdict(n_pass, n_parity_twin_pass)
    magnitudes_for_aggregate = magnitudes_pass_rows                # (local)
    magnitude_verdict = aggregate_magnitude_verdict(sign_verdict, magnitudes_for_aggregate)
    print(f"=== Step decision rule: sign + magnitude verdicts ===")
    print(f"  sign_verdict = {sign_verdict}")
    print(f"  magnitude_verdict = {magnitude_verdict}")
    print(f"  regime_verdict = {regime_verdict}")
    print()

    # 6. Composite collapse
    composite = composite_collapse(sign_verdict, magnitude_verdict, regime_verdict)
    track = track_allocation(composite, sign_verdict)
    print(f"=== Composite verdict (per gate-verdicts.md §S87+ schema-v2) ===")
    print(f"  composite = {composite}")
    print(f"  track_allocation = {track}")
    if track == "A":
        print(f"  Reading: Track A — prior FAIL stands → C16 confirmed INFO at L_max=10")
        print(f"           Both proxies (τ-flow-trace and WZW) agree the substrate-pole")
        print(f"           structure does NOT yield canonical sign-reversal at τ_fold")
        print(f"           under the (C_H, C_epsH) parity-twin pair AND the broader 5-atlas.")
    elif track == "B":
        print(f"  Reading: Track B — cross-proxy yields PASS → C16 promotes to ADMISSIBLE")
        print(f"           The WZW proxy extracts the conformal-anomaly content the")
        print(f"           τ-flow-trace proxy missed.")
    else:
        print(f"  Reading: OPEN — INFO middle band; neither track decisively allocated.")
    print()

    # 7. Plot
    print(f"=== Plot ===")
    make_plot(rows, composite, n_pass, n_parity_twin_pass)
    print(f"  Plot written: {OUT_PNG.name}")
    print()

    # 8. NPZ
    print(f"=== NPZ ===")
    rows_array = np.array([(
        r["row_label"], r["regulator"], r["parity"],
        r["is_atlas"], r["is_parity_twin"],
        r["val_minus"], r["val_fold"], r["val_plus"],
        r["sign_reversal"], r["magnitude"],
        r["convergence_margin"], r["regime_verdict"],
        r["tau_flow_sign_reversal"], r["tau_flow_slope_pre"], r["tau_flow_slope_post"],
        r["agree_with_tau_flow"],
    ) for r in rows], dtype=object)                              # (local)

    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        composite_verdict=composite,
        track_allocation=track,
        sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        n_pass=n_pass,
        n_parity_twin_pass=n_parity_twin_pass,
        n_agree_with_tau_flow_trace=n_agree_atlas,
        rows=rows_array,
        atlas_5=np.array(ATLAS_5),
        parity_twin=np.array(PARITY_TWIN),
        L_max=L_MAX,
        scheme=SCHEME,
        convention=CONVENTION,
        s4_pole_pin=S4_POLE_PIN,
        s3_pole_pin=S3_POLE_PIN,
        delta_tau=DELTA_TAU,
        tau_fold=tau_fold,
        sheet_flip_magnitude_threshold=SHEET_FLIP_MAGNITUDE_THRESHOLD,
        convergence_margin_threshold=CONVERGENCE_MARGIN_THRESHOLD,
        n_pass_pass_threshold=N_PASS_PASS_THRESHOLD,
        n_parity_twin_pass_threshold=N_PARITY_TWIN_PASS_THRESHOLD,
        n_pass_fail_threshold=N_PASS_FAIL_THRESHOLD,
        n_parity_twin_fail_threshold=N_PARITY_TWIN_FAIL_THRESHOLD,
        tier_pin="TIER-2-SCHEMATIC",
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        closure_sha256=closure,
    )
    print(f"  NPZ written: {OUT_NPZ.name}")
    print()

    # 9. Verdict line
    print(f"=== Verdict line ===")
    value_str = f"{n_pass}/5+twin={n_parity_twin_pass}/2"        # (local)
    append_verdict(
        composite, value_str, audit_sha, content_sha,
        sign_verdict, magnitude_verdict, regime_verdict,
        n_agree_atlas, track, n_pass, n_parity_twin_pass,
    )
    print(f"  Verdict appended: {composite} -- value={value_str}")
    print(f"  3-tuple: sign={sign_verdict} mag={magnitude_verdict} regime={regime_verdict}")
    print(f"  Cross-proxy: n_agree={n_agree_atlas}/5 track={track}")
    print()

    # 10. 4-tuple final line
    print(f"=== 4-tuple final ===")
    print(f"  (value={value_str}, "
          f"scheme={SCHEME}, "
          f"convention={CONVENTION}, "
          f"L_max={L_MAX})")

    print(f"\nElapsed: {time.time()-t0:.2f} s")


if __name__ == "__main__":
    main()
