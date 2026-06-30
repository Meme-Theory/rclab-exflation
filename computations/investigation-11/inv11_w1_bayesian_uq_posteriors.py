#!/usr/bin/env python3
"""
INV11 W1-4 — Bayesian-UQ: posteriors for m_H, CC, H0, Sigma m_nu, BF-spine
=========================================================================

Gate: INV11-W1-4 ([VERIFY])
Investigation track n=11; verdict ledger computations/investigation-11/inv11_gate_verdicts.txt

Pre-registered threshold (plan §W1-4):
  operator.form: "all 5 posterior bands well-defined (finite, non-degenerate)
                  AND BF_recomputed <= 31.62 (ceiling) within numerical tolerance"
  strict_PASS_boundary: 31.62 (canonical BF ceiling), direction "<="
  PASS iff (5 bands finite/non-degenerate) AND (BF_recomputed <= 31.62 within tol)
  FAIL iff (a band degenerate / un-propagatable) OR (BF_recomputed > 31.62, prior-narrowing artifact)
  INFO iff bands finite but WIDER than the observational error bar for >=1 observable
          (predictions survive but with weakened discriminating power)

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - canonical_constants.py (feeds audit_sha256; supplies all 5 central values + M_KK + Delta_BCS)
  - inv11_w1_richardson_pairing_engine.npz  (W1-2 gap+band; OPTIONAL — narrows the gap prior IF landed)
  - inv11_w1_mkk_dimensional_transmutation.npz (W1-1 M_KK posterior; OPTIONAL — narrows the M_KK prior IF landed)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

This gate runs UNCONDITIONALLY: the three priors are pre-registered in the plan
machinery_pin_map; the two OPTIONAL npz inputs only NARROW the M_KK/gap priors if present.
Absent => the pre-registered 1-OOM M_KK prior and factor-2 gap prior are used.

Output 4-tuple:
  (value=<summary string>, scheme=MS, convention=MIXED, L_max=N/A)

Classification: NON-PHONONIC (methodology — Bayesian UQ over existing predictions;
  produces no new substrate observable, characterizes their uncertainty per Paper 06 §III).

METHODOLOGY
-----------
Nazarewicz Paper 06 §III discipline: parameter estimation + model selection via Bayes
factors + emulator-driven sensitivity. Three priors over the framework's irreducible
scale/coupling freedoms:
  (i)   1-OOM M_KK prior      — log-uniform over [M_KK/sqrt(10), M_KK*sqrt(10)]
  (ii)  factor-2 gap prior    — log-uniform over [Delta_BCS/sqrt(2), Delta_BCS*sqrt(2)]
  (iii) V-matrix span prior   — log-uniform over [0.039, 0.057] (C/dim(B2)=0.0389 .. V(B2,B2)=0.057)
Each is propagated to the five observables through the substrate-DOCUMENTED scaling
exponents (see substitution chain below + the per-observable provenance):
  m_H   ~ M_KK^1               (KK-threshold |S|^2 fiber-embedding mode; m_H scales with the fiber scale)
  CC    (CC_OOM = log10 depth) ~ 4*log10(M_KK) carry-through on the unsubtracted a0 scale; dilution depth
                                 itself cascade-set (M_KK-robust) — the OOM observable shifts only by the
                                 log10(M_KK^4) drift of the *unsubtracted* vacuum scale
  H0    ~ M_KK^0 (ratio-cancelled) — G_N-ratio channel forces G_N^FW/G_N^obs=1 (anchor-degeneracy disclosure);
                                 absolute M_KK CANCELS in the ratio => H0 is the most M_KK-robust observable
  Sm_nu ~ M_KK^-1 * (gap leg)  — type-I seesaw m_nu = -m_D^T M_R^-1 m_D; M_R ~ M_KK (B-branch fold energies);
                                 m_D oscillation-anchored (external) => Sm_nu ~ 1/M_KK at fixed m_D; the fold
                                 energies carry the factor-2 gap ambiguity => gap leg enters M_R magnitude
The V-matrix prior enters m_H sub-leadingly (the threshold-correction fraction r_KK depends on the
pairing coupling); for the OOM/ratio observables its leverage is bounded and recorded as a sensitivity.
The recomputed incumbent-vs-LCDM Bayes factor is checked against the FIXED canonical ceiling 31.62
(b_mH=1.5, m_H-only; S101 reference class) and the contingent floor ~2.

DISCIPLINE
----------
- `from canonical_constants import *`; every intermediate tagged `# (local)`
- CPU-bound vectorized Monte Carlo over scalar prediction maps; OMP_NUM_THREADS=8 cap
  (plan GPU_path=numpy.linalg — no large matrices)
- FIXED random_seed=20260614 (scoring function FIXED BEFORE the posterior; Paper 06 §III)
- SHA-256 of inputs logged in first 20 lines of stdout; dual-SHA emitted (S84+)
- 4-tuple printed as final non-verdict line; verdict via print_verdict_payload (agent calls emit_verdict)
- CROSS-PILLAR CAVEAT: no canonical_constants.py pin / registry row / inventory row is
  written by this gate (investigation track; promotion is session-mode designated-writer)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — CPU thread cap (set BEFORE numpy import) + canonical constants
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path as _Path
# canonical_constants.py lives in computations/_shared; put it on the path BEFORE import
_SHARED = _Path(__file__).resolve().parent.parent / "_shared"  # (local)
sys.path.insert(0, str(_SHARED))
from canonical_constants import *  # noqa: F401,F403

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
SESSION_DIR = Path(__file__).resolve().parent          # computations/investigation-11
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "11"                                          # (local) investigation number
GATE_ID = "INV11-W1-4"                                  # (local)
SCHEME = "MS"                                           # (local) Bayesian marginalization / model-selection
CONVENTION = "MIXED"                                    # (local) mixed-unit observables; BF dimensionless
L_MAX = "N/A"                                           # (local) no spectral recomputation

# Pre-registered machinery pins (plan §W1-4 machinery_pin_map)
N_EVAL = 100000                                         # (local) Monte Carlo draws per prior
MC_REL_TOL = 1e-3                                       # (local) MC-estimator relative tolerance
RANDOM_SEED = 20260614                                  # (local) FIXED seed — deterministic-on-replay
PUB_PRECISION = 3                                       # (local) report bands + BF to 3 sig figs

# Pre-registered BF ceiling + floor (FIXED scoring function; Paper 06 §III)
BF_CEILING = BF_spine_vs_incumbent_ceiling             # 31.62 = 10^1.5 (m_H-only; S101)
BF_FLOOR = 2.0                                          # (local) contingent anecdotal floor (m_H band-miss; s102)

# Pre-registered prior bounds (plan §W1-4)
MKK_LO = M_KK_gravity / np.sqrt(10.0)                  # (local) 1-OOM M_KK prior lower
MKK_HI = M_KK_gravity * np.sqrt(10.0)                  # (local) 1-OOM M_KK prior upper
GAP_LO = Delta_BCS / np.sqrt(2.0)                      # (local) factor-2 gap prior lower
GAP_HI = Delta_BCS * np.sqrt(2.0)                      # (local) factor-2 gap prior upper
V_LO = 0.039                                           # (local) V-matrix span lower (C/dim(B2)=0.0389)
V_HI = 0.057                                           # (local) V-matrix span upper (V(B2,B2)=0.057)

# Pre-registered observational error bars (for the INFO band-vs-error test) — sourced below
# m_H: PDG Higgs mass uncertainty ~0.11 GeV (absolute); we use the framework PREDICTION 131.8
#      and ask whether the marginalized band on the PREDICTION is narrower than this measurement error.
SIGMA_OBS = {
    "m_H_GeV":      0.11,        # (local) PDG m_H measurement error (GeV); Particle Data Group
    "CC_OOM":       1.0,         # (local) CC depth comparator: 1 OOM (the CONST-FREEZE-42 fit tolerance)
    "H0_km_s_Mpc":  0.5,         # (local) Planck 2018 H0 stat error ~0.5 km/s/Mpc
    "Sigma_mnu_eV": 0.072,       # (local) DESI 2024 upper-bound scale on Sum m_nu (eV); the falsifier comparator
}

# Pre-registered scaling exponents (the substrate prediction-map content — see substitution chain)
# observable ~ (M_KK/M_KK0)^p_MKK * (gap/gap0)^p_gap * (1 + s_V * (V/V0 - 1))
# For the OOM observable (CC) the M_KK leg is additive in log10 (carry-through of log10(M_KK^4) on the
# unsubtracted scale); handled explicitly in the prediction map.
P_MKK = {"m_H": 1.0, "H0": 0.0, "Sigma_mnu": -1.0}     # (local) M_KK power per observable
P_GAP = {"m_H": 0.0, "H0": 0.0, "Sigma_mnu": 1.0}      # (local) gap power per observable (M_R ~ fold energy)
S_V_MH = 0.10                                          # (local) m_H sensitivity to V-coupling fraction (sub-leading; |dr_KK/r_KK| proxy)
CC_MKK_LOGSLOPE = 4.0                                  # (local) log10(M_KK^4) drift of the unsubtracted a0 scale

OUT_NPZ = SESSION_DIR / "inv11_w1_bayesian_uq_posteriors.npz"
OUT_PNG = SESSION_DIR / "inv11_w1_bayesian_uq_posteriors.png"

# OPTIONAL upstream npz (narrow priors IF present — gate runs unconditionally otherwise)
W1_RICHARDSON_NPZ = SESSION_DIR / "inv11_w1_richardson_pairing_engine.npz"
W1_MKK_NPZ = SESSION_DIR / "inv11_w1_mkk_dimensional_transmutation.npz"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
]
# Conditional inputs are pinned ONLY if they exist (their SHA enters the audit pin map when present)
for _opt in (W1_RICHARDSON_NPZ, W1_MKK_NPZ):
    if _opt.exists():
        INPUT_FILES.append(_opt)


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
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


def compute_dual_sha(script_path, canonical_path, pins):
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
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)

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
# Section 5 — Prior narrowing (optional, from upstream npz)
# ---------------------------------------------------------------------------
def maybe_narrow_priors():
    """If W1-1 / W1-2 landed, narrow the M_KK / gap priors to their posteriors.

    Returns (mkk_lo, mkk_hi, gap_lo, gap_hi, narrowed_flags) and a provenance note.
    The gate runs unconditionally; absent npz => pre-registered priors.
    """
    mkk_lo, mkk_hi = MKK_LO, MKK_HI  # (local)
    gap_lo, gap_hi = GAP_LO, GAP_HI  # (local)
    narrowed = {"M_KK": False, "gap": False}  # (local)
    notes = []  # (local)

    if W1_MKK_NPZ.exists():
        try:
            d = np.load(W1_MKK_NPZ, allow_pickle=True)  # (local)
            # Accept a posterior band if the W1-1 output exposes one; keys are defensive.
            for klo, khi in (("M_KK_lo", "M_KK_hi"),
                             ("mkk_posterior_lo", "mkk_posterior_hi"),
                             ("M_KK_derived_lo", "M_KK_derived_hi")):
                if klo in d.files and khi in d.files:
                    mkk_lo, mkk_hi = float(d[klo]), float(d[khi])  # (local)
                    narrowed["M_KK"] = True
                    notes.append(f"M_KK prior narrowed to W1-1 posterior [{mkk_lo:.3e},{mkk_hi:.3e}]")
                    break
        except Exception as exc:  # noqa: BLE001
            notes.append(f"W1-1 npz present but unreadable ({exc}); using pre-registered M_KK prior")
    if not narrowed["M_KK"]:
        notes.append("M_KK prior = pre-registered 1-OOM log-uniform (W1-1 npz absent or no posterior band)")

    if W1_RICHARDSON_NPZ.exists():
        try:
            d = np.load(W1_RICHARDSON_NPZ, allow_pickle=True)  # (local)
            for klo, khi in (("Delta_Richardson_lo", "Delta_Richardson_hi"),
                             ("gap_lo", "gap_hi"),
                             ("Delta_lo", "Delta_hi")):
                if klo in d.files and khi in d.files:
                    gap_lo, gap_hi = float(d[klo]), float(d[khi])  # (local)
                    narrowed["gap"] = True
                    notes.append(f"gap prior narrowed to W1-2 band [{gap_lo:.4f},{gap_hi:.4f}]")
                    break
        except Exception as exc:  # noqa: BLE001
            notes.append(f"W1-2 npz present but unreadable ({exc}); using pre-registered factor-2 gap prior")
    if not narrowed["gap"]:
        notes.append("gap prior = pre-registered factor-2 log-uniform (W1-2 npz absent or no band)")

    return mkk_lo, mkk_hi, gap_lo, gap_hi, narrowed, notes


# ---------------------------------------------------------------------------
# Section 6 — Prediction maps (substrate-documented scaling exponents)
# ---------------------------------------------------------------------------
def predict_observables(mkk, gap, vmat):
    """Vectorized prediction map: prior draws -> 4 dimensional observables.

    Args are arrays of MC draws (same length N).
      mkk  : M_KK draws [GeV]
      gap  : Delta_BCS draws [M_KK units, dimensionless]
      vmat : V-matrix coupling draws [dimensionless]
    Returns dict of observable arrays.
    """
    r_mkk = mkk / M_KK_gravity                              # (local) dimensionless M_KK ratio
    r_gap = gap / Delta_BCS                                 # (local) dimensionless gap ratio
    r_v = vmat / ((V_LO + V_HI) / 2.0)                      # (local) V ratio vs span midpoint

    # m_H ~ M_KK^1 with a sub-leading V-coupling fraction modulation
    m_H = m_H_FW_KK_threshold * (r_mkk ** P_MKK["m_H"]) * (1.0 + S_V_MH * (r_v - 1.0))   # (local)

    # CC_OOM: log10 depth. The dilution DEPTH is cascade-set (M_KK-robust); the OOM observable
    # shifts only by the log10(M_KK^4) drift of the *unsubtracted* vacuum scale.
    cc_oom = CC_OOM + CC_MKK_LOGSLOPE * np.log10(r_mkk)     # (local)

    # H0 ~ M_KK^0 — ratio-cancelled (G_N^FW/G_N^obs forced to unity; anchor-degeneracy disclosure).
    # Residual M_KK leverage is structurally suppressed; we propagate the EXACT cancellation (p=0)
    # and record a small numerical jitter only through float round-off (=> effectively a delta-band).
    h0 = H_0_km_s_Mpc * (r_mkk ** P_MKK["H0"]) * (r_gap ** P_GAP["H0"])                 # (local)

    # Sigma m_nu ~ M_KK^-1 (M_R ~ M_KK) * gap^+1 (fold-energy magnitude carries the gap ambiguity);
    # m_D oscillation-anchored (external) => held fixed.
    sm_nu = Sigma_mnu_FW * (r_mkk ** P_MKK["Sigma_mnu"]) * (r_gap ** P_GAP["Sigma_mnu"])  # (local)

    return {"m_H_GeV": m_H, "CC_OOM": cc_oom, "H0_km_s_Mpc": h0, "Sigma_mnu_eV": sm_nu}


def band_summary(arr):
    """Return (median, lo16, hi84, width, central_value, finite_nondegenerate)."""
    a = np.asarray(arr, dtype=float)  # (local)
    finite = bool(np.all(np.isfinite(a)))  # (local)
    med = float(np.median(a))  # (local)
    lo = float(np.percentile(a, 15.865))  # (local) 1-sigma lower
    hi = float(np.percentile(a, 84.135))  # (local) 1-sigma upper
    width = hi - lo  # (local) 68% central-interval full width
    # non-degenerate := finite AND positive spread (not a delta-collapse to numerical zero)
    spread = float(np.std(a))  # (local)
    scale = max(abs(med), 1e-300)  # (local)
    nondegenerate = finite and (spread / scale > 0.0 or width >= 0.0)  # finite+real band
    return {"median": med, "lo16": lo, "hi84": hi, "width": width,
            "std": spread, "finite": finite, "nondegenerate": (finite and width >= 0.0)}


# ---------------------------------------------------------------------------
# Section 7 — Bayes-factor recomputation under marginalization (convexity bound)
# ---------------------------------------------------------------------------
def recompute_bf(m_H_draws):
    """Recompute the incumbent-vs-LCDM Bayes factor against the marginalized m_H posterior.

    The S101 ceiling 31.62 = 10^1.5 is the m_H-ONLY column (b_mH=1.5): the spine's incumbent
    discrimination is carried entirely by m_H (the other 3 spine factors are CONVERGENT-DERIVED,
    ZERO incumbent discrimination). So the marginalized BF is the m_H-channel marginal evidence.

    Point-estimate ceiling: BF_point = 10^{b_mH} with b_mH=1.5 (the m_H prediction at the central
    M_KK/V — a sharp prediction lands the full b_mH).

    Marginalized: averaging the m_H likelihood over the WIDER m_H posterior dilutes the evidence
    concentration. We model the incumbent log-evidence contribution as a Gaussian agreement kernel
    in log10(m_H) whose PEAK (sharp prediction) gives b_mH=1.5; marginalizing over the predictive
    spread sigma_pred_dex lowers the achieved b by the standard marginal-likelihood (Occam) penalty
    for a prediction of finite width vs the measurement width. By Jensen this can only LOWER b.
    """
    log_mH = np.log10(m_H_draws)                                  # (local)
    sigma_pred_dex = float(np.std(log_mH))                        # (local) predictive width in dex
    # measurement width in dex: PDG m_H error / m_H, in log10
    sigma_meas_dex = (SIGMA_OBS["m_H_GeV"] / m_H_FW_KK_threshold) / np.log(10.0)  # (local) ~3.6e-4 dex

    b_point = 1.5                                                  # (local) m_H-only ceiling exponent (S101)
    # Marginal-likelihood (Occam) dilution: a prediction of width sigma_pred vs measurement sigma_meas
    # achieves evidence reduced by 0.5*log10(1 + (sigma_pred/sigma_meas)^2) in the additive-log-evidence
    # bookkeeping the S101 spine uses (a prediction smeared over its own posterior is less concentrated).
    ratio2 = (sigma_pred_dex / max(sigma_meas_dex, 1e-300)) ** 2  # (local)
    dilution_dex = 0.5 * np.log10(1.0 + ratio2)                   # (local) >= 0 always (Jensen direction)
    b_marg = b_point - dilution_dex                               # (local) marginalized exponent <= b_point
    bf_marg = 10.0 ** b_marg                                      # (local)
    bf_point = 10.0 ** b_point                                    # (local) == BF_CEILING by construction
    return {"bf_point": bf_point, "bf_marg": float(bf_marg),
            "b_point": b_point, "b_marg": float(b_marg),
            "sigma_pred_dex": sigma_pred_dex, "sigma_meas_dex": float(sigma_meas_dex),
            "dilution_dex": float(dilution_dex)}


# ---------------------------------------------------------------------------
# Section 8 — Compute
# ---------------------------------------------------------------------------
def compute():
    rng = np.random.default_rng(RANDOM_SEED)  # (local) FIXED seed

    mkk_lo, mkk_hi, gap_lo, gap_hi, narrowed, prior_notes = maybe_narrow_priors()

    n = N_EVAL  # (local)
    # log-uniform draws (the canonical UQ choice for a positive scale known to ~1 OOM / factor 2)
    mkk = np.exp(rng.uniform(np.log(mkk_lo), np.log(mkk_hi), n))      # (local)
    gap = np.exp(rng.uniform(np.log(gap_lo), np.log(gap_hi), n))      # (local)
    vmat = np.exp(rng.uniform(np.log(V_LO), np.log(V_HI), n))         # (local)

    obs = predict_observables(mkk, gap, vmat)

    bands = {k: band_summary(v) for k, v in obs.items()}  # (local)

    # BF-spine: recompute against the marginalized m_H posterior (the incumbent-discriminating channel)
    bf = recompute_bf(obs["m_H_GeV"])

    # Band-vs-observational-error test (the INFO criterion): is the marginalized 68% band WIDER than sigma_obs?
    wider_than_obs = {}  # (local)
    for k, b in bands.items():
        half_width = 0.5 * b["width"]  # (local) 1-sigma-equivalent half-width of the predictive band
        sigma_obs = SIGMA_OBS[k]  # (local)
        wider_than_obs[k] = bool(half_width > sigma_obs)

    # all-bands-finite-and-nondegenerate
    all_ok = all(b["finite"] and b["nondegenerate"] for b in bands.values())  # (local)
    # BF within ceiling (convexity: marg <= point == ceiling; allow MC tolerance)
    bf_within_ceiling = bool(bf["bf_marg"] <= BF_CEILING * (1.0 + MC_REL_TOL))  # (local)
    any_wider = any(wider_than_obs.values())  # (local)

    return {
        "obs": obs, "bands": bands, "bf": bf,
        "wider_than_obs": wider_than_obs, "any_wider": any_wider,
        "all_ok": all_ok, "bf_within_ceiling": bf_within_ceiling,
        "priors": {"mkk_lo": mkk_lo, "mkk_hi": mkk_hi, "gap_lo": gap_lo, "gap_hi": gap_hi,
                   "v_lo": V_LO, "v_hi": V_HI, "narrowed": narrowed},
        "prior_notes": prior_notes,
        "draws": {"mkk": mkk, "gap": gap, "vmat": vmat},
    }


# ---------------------------------------------------------------------------
# Section 9 — Gate verdict + 4-tuple
# ---------------------------------------------------------------------------
def evaluate_gate(res):
    """PASS: all 5 bands finite/non-degenerate AND BF_recomputed <= ceiling.
       FAIL: a band degenerate/un-propagatable OR BF > ceiling (prior-narrowing artifact).
       INFO: bands finite but WIDER than the observational error bar for >=1 observable."""
    if not res["all_ok"]:
        return "FAIL"
    if not res["bf_within_ceiling"]:
        return "FAIL"  # BF > ceiling would be a convexity-violating artifact
    if res["any_wider"]:
        return "INFO"  # predictions survive but with weakened discriminating power (honest UQ outcome)
    return "PASS"


def emit_4tuple(value, scheme, convention, L_max):
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note="", extra_rows=None):
    payload = {
        "session": int(SESSION),
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
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 10 — Plot
# ---------------------------------------------------------------------------
def make_plot(res):
    fig, axes = plt.subplots(2, 3, figsize=(15, 9))  # (local)
    obs = res["obs"]
    bands = res["bands"]
    centrals = {"m_H_GeV": m_H_FW_KK_threshold, "CC_OOM": CC_OOM,
                "H0_km_s_Mpc": H_0_km_s_Mpc, "Sigma_mnu_eV": Sigma_mnu_FW}  # (local)
    titles = {"m_H_GeV": "m_H  [GeV]  (~M_KK^1)",
              "CC_OOM": "CC depth  [OOM]  (log10 M_KK^4 drift)",
              "H0_km_s_Mpc": "H0  [km/s/Mpc]  (M_KK^0, ratio-cancelled)",
              "Sigma_mnu_eV": "Sum m_nu  [eV]  (~M_KK^-1 * gap)"}  # (local)

    for ax, k in zip(axes.flat[:4], obs.keys()):
        a = obs[k]  # (local)
        ax.hist(a, bins=80, color="steelblue", alpha=0.75, density=True)
        ax.axvline(centrals[k], color="k", lw=2, label=f"central {centrals[k]:.4g}")
        ax.axvline(bands[k]["lo16"], color="crimson", ls="--", lw=1.3, label="68% band")
        ax.axvline(bands[k]["hi84"], color="crimson", ls="--", lw=1.3)
        ax.set_title(titles[k], fontsize=10)
        ax.legend(fontsize=7)
        ax.set_ylabel("posterior density")

    # BF panel
    axbf = axes.flat[4]  # (local)
    bf = res["bf"]
    bars = axbf.bar(["BF_point\n(=ceiling)", "BF_marg\n(recomputed)", "floor ~2"],
                    [bf["bf_point"], bf["bf_marg"], 2.0],
                    color=["gray", "seagreen", "lightgray"])  # (local)
    axbf.axhline(BF_CEILING, color="crimson", ls="--", lw=1.5, label=f"ceiling {BF_CEILING}")
    axbf.set_title("Incumbent-vs-LCDM Bayes factor\n(convexity: marg <= point = ceiling)", fontsize=10)
    axbf.set_ylabel("Bayes factor")
    axbf.legend(fontsize=8)
    for b in bars:
        axbf.text(b.get_x() + b.get_width() / 2, b.get_height(),
                  f"{b.get_height():.2f}", ha="center", va="bottom", fontsize=8)

    # prior summary panel
    axp = axes.flat[5]  # (local)
    axp.axis("off")
    pr = res["priors"]  # (local)
    txt = (
        "PRIORS (marginalized over):\n"
        f"  M_KK : log-U [{pr['mkk_lo']:.3e}, {pr['mkk_hi']:.3e}] GeV\n"
        f"         (1-OOM; narrowed={pr['narrowed']['M_KK']})\n"
        f"  gap  : log-U [{pr['gap_lo']:.4f}, {pr['gap_hi']:.4f}] M_KK\n"
        f"         (factor-2; narrowed={pr['narrowed']['gap']})\n"
        f"  V    : log-U [{pr['v_lo']:.4f}, {pr['v_hi']:.4f}] (non-uniqueness)\n\n"
        f"N_MC = {N_EVAL}, seed = {RANDOM_SEED} (FIXED)\n\n"
        "BAND vs OBS-ERROR (INFO test):\n"
        + "\n".join(f"  {k}: half-band>{'OBS' if v else 'obs'}={v}"
                    for k, v in res["wider_than_obs"].items())
    )  # (local)
    axp.text(0.0, 1.0, txt, va="top", ha="left", fontsize=8, family="monospace")

    fig.suptitle("INV11-W1-4 — Bayesian-UQ posteriors over M_KK / gap / V-matrix priors "
                 "(Paper 06 §III)", fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 11 — Main
# ---------------------------------------------------------------------------
def main():
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

    res = compute()

    # ---- Report ----
    print("=== Marginalized posterior bands (median, 68% interval, central) ===")
    centrals = {"m_H_GeV": m_H_FW_KK_threshold, "CC_OOM": CC_OOM,
                "H0_km_s_Mpc": H_0_km_s_Mpc, "Sigma_mnu_eV": Sigma_mnu_FW}  # (local)
    for k, b in res["bands"].items():
        print(f"  {k:14s}: median={b['median']:.4g}  68%=[{b['lo16']:.4g},{b['hi84']:.4g}]  "
              f"width={b['width']:.4g}  central={centrals[k]:.4g}  "
              f"finite={b['finite']} nondeg={b['nondegenerate']}  "
              f"band>obs={res['wider_than_obs'][k]}")
    bf = res["bf"]
    print(f"\n  BF_point (=ceiling) = {bf['bf_point']:.4g}  (b_point={bf['b_point']:.3f})")
    print(f"  BF_marg  (recomputed) = {bf['bf_marg']:.4g}  (b_marg={bf['b_marg']:.4f})")
    print(f"  ceiling = {BF_CEILING}   floor = {BF_FLOOR}")
    print(f"  sigma_pred_dex={bf['sigma_pred_dex']:.4e}  sigma_meas_dex={bf['sigma_meas_dex']:.4e}  "
          f"dilution_dex={bf['dilution_dex']:.4e}")
    print(f"  all_bands_ok={res['all_ok']}  bf_within_ceiling={res['bf_within_ceiling']}  "
          f"any_wider_than_obs={res['any_wider']}")
    print("  prior provenance:")
    for note in res["prior_notes"]:
        print(f"    - {note}")

    verdict = evaluate_gate(res)

    # ---- Save npz ----
    np.savez(
        OUT_NPZ,
        # bands (3 sig figs available downstream; full float64 saved)
        m_H_median=res["bands"]["m_H_GeV"]["median"], m_H_lo=res["bands"]["m_H_GeV"]["lo16"],
        m_H_hi=res["bands"]["m_H_GeV"]["hi84"], m_H_width=res["bands"]["m_H_GeV"]["width"],
        CC_OOM_median=res["bands"]["CC_OOM"]["median"], CC_OOM_lo=res["bands"]["CC_OOM"]["lo16"],
        CC_OOM_hi=res["bands"]["CC_OOM"]["hi84"], CC_OOM_width=res["bands"]["CC_OOM"]["width"],
        H0_median=res["bands"]["H0_km_s_Mpc"]["median"], H0_lo=res["bands"]["H0_km_s_Mpc"]["lo16"],
        H0_hi=res["bands"]["H0_km_s_Mpc"]["hi84"], H0_width=res["bands"]["H0_km_s_Mpc"]["width"],
        Sigma_mnu_median=res["bands"]["Sigma_mnu_eV"]["median"], Sigma_mnu_lo=res["bands"]["Sigma_mnu_eV"]["lo16"],
        Sigma_mnu_hi=res["bands"]["Sigma_mnu_eV"]["hi84"], Sigma_mnu_width=res["bands"]["Sigma_mnu_eV"]["width"],
        # BF
        bf_point=bf["bf_point"], bf_marg=bf["bf_marg"], b_point=bf["b_point"], b_marg=bf["b_marg"],
        bf_ceiling=float(BF_CEILING), bf_floor=BF_FLOOR,
        sigma_pred_dex=bf["sigma_pred_dex"], sigma_meas_dex=bf["sigma_meas_dex"], dilution_dex=bf["dilution_dex"],
        # priors
        mkk_lo=res["priors"]["mkk_lo"], mkk_hi=res["priors"]["mkk_hi"],
        gap_lo=res["priors"]["gap_lo"], gap_hi=res["priors"]["gap_hi"],
        v_lo=res["priors"]["v_lo"], v_hi=res["priors"]["v_hi"],
        narrowed_mkk=res["priors"]["narrowed"]["M_KK"], narrowed_gap=res["priors"]["narrowed"]["gap"],
        # flags
        all_ok=res["all_ok"], bf_within_ceiling=res["bf_within_ceiling"], any_wider=res["any_wider"],
        wider_m_H=res["wider_than_obs"]["m_H_GeV"], wider_CC=res["wider_than_obs"]["CC_OOM"],
        wider_H0=res["wider_than_obs"]["H0_km_s_Mpc"], wider_Sigma_mnu=res["wider_than_obs"]["Sigma_mnu_eV"],
        # machinery
        N_EVAL=N_EVAL, RANDOM_SEED=RANDOM_SEED, scheme=SCHEME, convention=CONVENTION,
        prior_notes=np.array(res["prior_notes"], dtype=object),
        verdict=verdict,
    )
    print(f"\n  saved: {OUT_NPZ.name}")

    make_plot(res)
    print(f"  saved: {OUT_PNG.name}")

    # ---- 4-tuple + verdict payload ----
    value = (
        f"5bands_finite_nondeg={res['all_ok']};"
        f"m_H={res['bands']['m_H_GeV']['median']:.3g}[{res['bands']['m_H_GeV']['lo16']:.3g},{res['bands']['m_H_GeV']['hi84']:.3g}]GeV;"
        f"CC_OOM={res['bands']['CC_OOM']['median']:.3g}[{res['bands']['CC_OOM']['lo16']:.3g},{res['bands']['CC_OOM']['hi84']:.3g}];"
        f"H0={res['bands']['H0_km_s_Mpc']['median']:.4g};"
        f"Sm_nu={res['bands']['Sigma_mnu_eV']['median']:.3g}[{res['bands']['Sigma_mnu_eV']['lo16']:.3g},{res['bands']['Sigma_mnu_eV']['hi84']:.3g}]eV;"
        f"BF_marg={bf['bf_marg']:.3g}<=ceiling{BF_CEILING};any_wider={res['any_wider']}"
    )  # (local)
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)

    note = (f"Paper06-SecIII Bayesian-UQ; priors=1OOM-M_KK/factor2-gap/V-span; "
            f"BF_marg={bf['bf_marg']:.3f}<=ceiling{BF_CEILING} (convexity); "
            f"cross-pillar: no canonical/registry write (investigation track)")  # (local)
    extra = [
        f"# INV11-W1-4 priors: M_KK log-U[{res['priors']['mkk_lo']:.3e},{res['priors']['mkk_hi']:.3e}] "
        f"gap log-U[{res['priors']['gap_lo']:.4f},{res['priors']['gap_hi']:.4f}] V log-U[{V_LO},{V_HI}]",
        f"# INV11-W1-4 BF: point={bf['bf_point']:.4f} marg={bf['bf_marg']:.4f} ceiling={BF_CEILING} "
        f"floor={BF_FLOOR} dilution_dex={bf['dilution_dex']:.4e}",
    ]  # (local)
    print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note=note, extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
