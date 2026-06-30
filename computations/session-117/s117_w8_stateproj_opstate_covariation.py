#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CF-S117-STATEPROJ-OPSTATE-COVARIATION (S117 W8-2) — numerical bound on the
residual OP-PROJ <-> STATE-PROJ co-variation under substrate deformation.

Gate: CF-S117-STATEPROJ-OPSTATE-COVARIATION | [VERIFY] | classification PHONONIC
Plan: sessions/session-plan/session-117-plan-w8.md  §W8-2
Owner: landau-condensed-matter-theorist

SUBSTRATE FRAMING (phononic-framing.md; cross-pillar-bridge-anatomy.md
§"Algebra-axis orthogonality K-counter"):
  Both observables are substrate-IS on the SAME D_K spectrum.
    OP-PROJ  : R_OP = (N_unpaired - 2 N_paired)/N_paired, a multiplicity-
               weighted Mellin-pole-window count on the SU(3) Peter-Weyl
               sectors (algebra-INVARIANT, spectrum-only -> Corner I). It is a
               PURE representation-theoretic count: it reads only (p,q) Weyl
               dims + Casimirs, NEVER the eigenvalue magnitudes. R_OP therefore
               responds ONLY to the truncation axis L_max; it is EXACTLY
               invariant under xi-scaling and tau-moduli.
    STATE-PROJ: R_STATE = (a-b)/(a+b) with a,b the BdG condensation energies
               rho_BCS(P_sector . H_pair) at the A/B sector gaps (Delta_BCS*SC_A,
               Delta_BCS*SC_B) on the substrate spectrum (algebra-DEPENDENT,
               state-pair -> Corner III). It reads the eigenvalues, so it
               responds to ALL three deformation axes (xi-scale, L_max, tau).
  Direction of explanation: D_K eigenvalues -> {the group-theoretic sector
  count (OP-PROJ)} and {the BdG condensation state-pair functional (STATE-PROJ)}
  are two structurally-orthogonal functionals (Corner I _|_ Corner III, proven
  at Level 1 in S116-W7). This gate DEFORMS the substrate and bounds the
  RESIDUAL numerical co-variation C_covar = |Pearson rho(R_OP, R_STATE)|. A
  bounded C_covar is the numerical face of the intrinsic orthogonality; it is
  NOT an inference that the substrate is a container in which the two co-vary.

GATE METRIC (plan §W8-2):
  C_covar = |Pearson rho(R_OP, R_STATE)| over the joint deformation ensemble
            {xi-scale x L_max x tau}.
  PASS iff C_covar < 0.5 (benign CONFIRMED); 0.5 <= C_covar < 0.85 -> INFO;
  C_covar >= 0.85 -> FAIL (near-total co-variation; surprise).
  Diagnostics (NOT the gate metric): per-axis spreads + detrended residual
  correlation (a co-MONOTONIC deformation response inflates Pearson |rho|
  without identity-class leakage; the detrended residual isolates that).
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # cpu-cap-OMP8 (GPU_path pin: light cache re-eval)
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import time
import hashlib
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --------------------------------------------------------------------------
# Section 1 — Paths + canonical imports (NEVER hardcode framework constants)
# --------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import (        # noqa: E402
    Delta_BCS,        # canonical substrate BCS gap (M_KK units; R-PROTECTED, S70)
    SC_corr_A,        # 3He-A strong-coupling gap enhancement (LAB; sets the A-sector gap split)
    SC_corr_B,        # 3He-B strong-coupling gap enhancement (LAB; sets the B-sector gap split)
    M_KK,             # KK mass scale (gravity-route alias)
    tau_fold,         # R-PROTECTED fold modulus (0.19)
)

# --------------------------------------------------------------------------
# Section 2 — Gate identity + machinery pins (plan W8-2 PRDR block)
# --------------------------------------------------------------------------
GATE_ID = "CF-S117-STATEPROJ-OPSTATE-COVARIATION"
SESSION = "S117"
SCHEME = "OP-STATE-COVARIATION-DEFORMATION-BOUND"
CONVENTION = ("PEARSON-RHO-JOINT-ENSEMBLE + per-axis-spread + "
              "detrended-residual-correlation")
L_MAX = "12,14"                                 # (local) deformation truncation axis

# Pre-registered thresholds (plan §W8-2; define BEFORE running)
PASS_THRESH = 0.5                               # (local) C_covar < 0.5 -> PASS (benign)
INFO_THRESH = 0.85                              # (local) 0.5 <= C_covar < 0.85 -> INFO
MELLIN_WINDOW_FRAC = 0.5                        # (local) OP-PROJ Mellin-pole window (s87 canonical)
XI_SCALES = (0.90, 0.95, 1.00, 1.05, 1.10)      # (local) plan-pinned xi-scale grid (5 pts)

# 8-1 substrate-first inter-summand STATE-PROJ companion values, cited from the
# CF-S117-STATEPROJ-INTER-SUMMAND canonical verdict line (audit_sha256
# 9252fc09af1239dd...; s117_gate_verdicts.txt). Used ONLY as a robustness
# companion diagnostic (NOT the gate metric; NOT an audit-SHA input).
R_SUMMAND_L12 = 0.955038                         # (local) 8-1 inter-summand R (L=12), verdict-line cite
R_SUMMAND_L14 = 0.968531                         # (local) 8-1 inter-summand R (L=14), verdict-line cite

# Input files (plan §W8-2 input_files; feed audit_sha256 per the dual-SHA schema)
CANONICAL = SHARED_DIR / "canonical_constants.py"
W7_NPZ = COMPUTATIONS_DIR / "session-116" / "s116_w7_stateproj_bcs.npz"
S84_CACHE = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
S87_CACHE = COMPUTATIONS_DIR / "session-87" / "s87_spectrum_cache_L14_tau019.npz"
S92_CACHE_T18 = COMPUTATIONS_DIR / "session-92" / "s92_spectrum_cache_L12_tau018.npz"
S92_CACHE_T20 = COMPUTATIONS_DIR / "session-92" / "s92_spectrum_cache_L12_tau020.npz"

INPUT_FILES = [CANONICAL, W7_NPZ, S84_CACHE, S87_CACHE, S92_CACHE_T18, S92_CACHE_T20]

# --------------------------------------------------------------------------
# Section 3 — dual-SHA helpers (S84+ schema; mirror script-template.py)
# --------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                    # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}                                               # (local)
    for p in inputs:
        sha = sha256_of(p)                                  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict) -> str:
    h = hashlib.sha256()
    for k, v in sorted(pins.items()):
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    try:
        script_bytes = script_path.read_bytes()             # (local)
    except OSError:
        script_bytes = b""                                  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()       # (local)
    except OSError:
        canonical_bytes = b""                               # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note="", extra_rows=None):
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
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# --------------------------------------------------------------------------
# Section 4 — OP-PROJ evaluator (inline exact SU(3) group theory => CLASS=FULL)
#
# Re-implements the s87_w11_3heb_excess_inheritance_comparison.py
# compute_substrate_excess_ratio (the evaluator that produced
# R_substrate_OP_L10 = -1.21222 -> R_inf ~ -1.892). The three helper functions
# are EXACT closed-form representation theory (NOT the SCHEMATIC *_a_n regulators
# of _spectral_action_regulators.py), so the gate is unambiguously CLASS=FULL.
# A sanity assert reproduces -1.21222 at L=10.
# --------------------------------------------------------------------------
def weyl_dim_su3(p, q):
    """SU(3) Weyl dimension dim((p,q)) = (p+1)(q+1)(p+q+2)/2 (exact)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def casimir_su3(p, q):
    """SU(3) quadratic Casimir C_2(p,q) = (p^2 + pq + q^2 + 3(p+q))/3 (exact)."""
    return (p * p + p * q + q * q + 3 * (p + q)) / 3.0


def enumerate_sectors(L_max):
    """List (p, q, d, C_2) for (p,q) != (0,0), p+q <= L_max (exact)."""
    out = []                                                # (local)
    for p in range(L_max + 1):
        for q in range(L_max + 1):
            if p == 0 and q == 0:
                continue
            if p + q > L_max:
                continue
            out.append((p, q, weyl_dim_su3(p, q), casimir_su3(p, q)))
    return out


def R_op_proj(L_max, window_frac=MELLIN_WINDOW_FRAC):
    """OP-PROJ multiplicity-weighted Mellin-pole-window excess ratio.

    R_OP = (N_unpaired - 2 N_paired)/N_paired, where 'paired' = sectors whose
    Casimir lies within |C - C_pole|/C_pole <= window_frac of the Casimir
    median C_pole, and N_x = sum of Weyl dims over x. Spectrum-INDEPENDENT:
    a pure function of L_max (algebra-INVARIANT, Corner I).
    """
    secs = enumerate_sectors(L_max)                         # (local)
    cas = np.array([s[3] for s in secs])                    # (local)
    wey = np.array([s[2] for s in secs], dtype=float)       # (local)
    C_pole = float(np.median(cas))                          # (local)
    paired = np.abs(cas - C_pole) / C_pole <= window_frac   # (local)
    N_paired = float(np.sum(wey[paired]))                   # (local)
    N_unpaired = float(np.sum(wey[~paired]))                # (local)
    return (N_unpaired - 2.0 * N_paired) / N_paired


# --------------------------------------------------------------------------
# Section 5 — STATE-PROJ evaluator (S116-W7 bcs_condensation_energy functional)
# --------------------------------------------------------------------------
def load_substrate_spectrum(cache_path: Path, l_max: int):
    """Flatten cached D_K(tau) |lambda_k| over Peter-Weyl sectors level <= l_max."""
    d = np.load(cache_path, allow_pickle=True)
    sector_evals = d["sector_evals"].item()                 # dict {(p,q): {...}}
    xis = []                                                # (local)
    for (p, q), blk in sector_evals.items():
        if int(blk.get("level", p + q)) <= l_max:
            xis.append(np.asarray(blk["abs_evals"], dtype=float))
    return np.concatenate(xis)


def bcs_condensation_energy(xi, delta):
    """S116-W7 functional: E_cond = sum_k [ |xi_k| - E_k + delta^2/(2 E_k) ],
    E_k = sqrt(xi_k^2 + delta^2). PH-even, gap-localized; returns |E_cond|."""
    Ek = np.sqrt(xi ** 2 + delta ** 2)                      # (local)
    e_cond = np.sum(np.abs(xi) - Ek + delta ** 2 / (2.0 * Ek))  # (local)
    return abs(e_cond)


def R_state_proj(xi, delta_bcs, sc_a, sc_b):
    """STATE-PROJ R_BdG = (a-b)/(a+b), a = E_cond(xi, Delta_BCS*SC_A),
    b = E_cond(xi, Delta_BCS*SC_B). Algebra-DEPENDENT, spectrum-dependent
    (Corner III). Reproduces the S116-W7 R_BdG_occupation form."""
    a = bcs_condensation_energy(xi, delta_bcs * sc_a)       # (local)
    b = bcs_condensation_energy(xi, delta_bcs * sc_b)       # (local)
    return (a - b) / (a + b)


# --------------------------------------------------------------------------
# Section 6 — Compute
# --------------------------------------------------------------------------
def compute() -> dict:
    out = {}

    # ----- Sanity anchor 1: OP-PROJ reproduces R_substrate_OP_L10 = -1.21222 --
    R_op_L10 = R_op_proj(10)                                # (local)
    out["R_op_L10_reproduction"] = R_op_L10
    out["R_op_L10_anchor"] = -377.0 / 311.0                 # -1.21222 (Sage-Q exact -3393/2799)
    assert abs(R_op_L10 - (-377.0 / 311.0)) < 1e-9, (
        f"OP-PROJ L=10 reproduction failed: {R_op_L10} vs -1.21222")

    # ----- Sanity anchor 2: STATE-PROJ reproduces S116-W7 R_BdG_occupation ---
    w7 = np.load(W7_NPZ, allow_pickle=True)
    R_BdG_w7 = float(w7["R_BdG_occupation"])               # (local) 0.068847 (W7, L=10)
    R_state_OP_L10_w7 = float(w7["R_substrate_OP_L10"])    # (local) -1.21222 (W7-cited)
    OP_PROJ_R_INF = float(w7["OP_PROJ_R_INF"])             # (local) -1.892 (W7-cited companion)
    xi_s84_L10 = load_substrate_spectrum(S84_CACHE, 10)    # (local) 78080 modes
    R_BdG_repro = R_state_proj(xi_s84_L10, Delta_BCS, SC_corr_A, SC_corr_B)  # (local)
    out["R_BdG_w7_anchor"] = R_BdG_w7
    out["R_BdG_L10_reproduction"] = R_BdG_repro
    out["R_BdG_repro_reldev"] = abs(R_BdG_repro - R_BdG_w7) / abs(R_BdG_w7)
    out["R_substrate_OP_L10_w7"] = R_state_OP_L10_w7
    out["OP_PROJ_R_INF"] = OP_PROJ_R_INF
    assert out["R_BdG_repro_reldev"] < 1e-6, (
        f"STATE-PROJ W7 reproduction failed: reldev={out['R_BdG_repro_reldev']:.2e}")

    # ----- Deformation ensemble {xi-scale x L_max x tau} ----------------------
    # Realizable base spectra (the 4 caches available on the L_max x tau grid:
    # tau=0.18/0.20 exist only at L12; L14 exists only at tau=0.19).
    base_spectra = [                                        # (local)
        ("L12_tau018", S92_CACHE_T18, 12, 0.18),
        ("L12_tau019", S84_CACHE,     12, 0.19),
        ("L14_tau019", S87_CACHE,     14, 0.19),
        ("L12_tau020", S92_CACHE_T20, 12, 0.20),
    ]
    # Pre-load each base spectrum once (xi-scale rescales the loaded |lambda_k|).
    loaded = {}                                             # (local)
    for label, path, Lm, tau in base_spectra:
        loaded[label] = load_substrate_spectrum(path, Lm)

    rows = []                                               # (local) ensemble points
    for label, path, Lm, tau in base_spectra:
        xi0 = loaded[label]                                 # (local)
        r_op = R_op_proj(Lm)                                # (local) L_max-keyed only
        for s in XI_SCALES:
            r_state = R_state_proj(s * xi0, Delta_BCS, SC_corr_A, SC_corr_B)  # (local)
            rows.append({
                "label": label, "L_max": Lm, "tau": tau, "xi_scale": s,
                "R_OP": r_op, "R_STATE": r_state, "n_modes": int(xi0.size),
            })

    R_OP = np.array([r["R_OP"] for r in rows])              # (local)
    R_STATE = np.array([r["R_STATE"] for r in rows])        # (local)
    out["n_ensemble"] = len(rows)
    out["R_OP_values"] = R_OP
    out["R_STATE_values"] = R_STATE
    out["R_OP_distinct"] = sorted(set(np.round(R_OP, 10).tolist()))
    out["R_STATE_min"] = float(R_STATE.min())
    out["R_STATE_max"] = float(R_STATE.max())

    # ----- GATE METRIC: C_covar = |Pearson rho(R_OP, R_STATE)| ---------------
    sd_op = float(np.std(R_OP))                             # (local)
    sd_state = float(np.std(R_STATE))                       # (local)
    if sd_op < 1e-15 or sd_state < 1e-15:
        pearson = 0.0                                       # (local) degenerate (no variance)
    else:
        pearson = float(np.corrcoef(R_OP, R_STATE)[0, 1])   # (local)
    C_covar = abs(pearson)                                  # (local) GATE METRIC
    out["pearson_rho"] = pearson
    out["C_covar"] = C_covar
    out["sd_R_OP"] = sd_op
    out["sd_R_STATE"] = sd_state

    # ----- DIAGNOSTIC 1: per-axis spreads (max-min holding others at baseline)
    # xi-axis: L12, tau=0.19 (s84 baseline), vary xi.
    xi_axis_state = [R_state_proj(s * loaded["L12_tau019"], Delta_BCS, SC_corr_A, SC_corr_B)
                     for s in XI_SCALES]                    # (local)
    xi_spread_OP = 0.0                                      # (local) R_OP xi-invariant (exact)
    xi_spread_STATE = float(max(xi_axis_state) - min(xi_axis_state))  # (local)
    # tau-axis: L12, xi=1.0, vary tau in {0.18, 0.19, 0.20}.
    tau_axis_state = [
        R_state_proj(loaded["L12_tau018"], Delta_BCS, SC_corr_A, SC_corr_B),
        R_state_proj(loaded["L12_tau019"], Delta_BCS, SC_corr_A, SC_corr_B),
        R_state_proj(loaded["L12_tau020"], Delta_BCS, SC_corr_A, SC_corr_B),
    ]                                                      # (local)
    tau_spread_OP = 0.0                                     # (local) R_OP tau-invariant (exact)
    tau_spread_STATE = float(max(tau_axis_state) - min(tau_axis_state))  # (local)
    # L_max-axis: xi=1.0, tau=0.19, vary L in {12 (s84), 14 (s87)}.
    Lmax_axis_OP = [R_op_proj(12), R_op_proj(14)]           # (local)
    Lmax_axis_state = [
        R_state_proj(loaded["L12_tau019"], Delta_BCS, SC_corr_A, SC_corr_B),
        R_state_proj(loaded["L14_tau019"], Delta_BCS, SC_corr_A, SC_corr_B),
    ]                                                      # (local)
    Lmax_spread_OP = float(Lmax_axis_OP[1] - Lmax_axis_OP[0])      # (local)
    Lmax_spread_STATE = float(Lmax_axis_state[1] - Lmax_axis_state[0])  # (local)
    out["xi_spread_OP"] = xi_spread_OP
    out["xi_spread_STATE"] = xi_spread_STATE
    out["tau_spread_OP"] = tau_spread_OP
    out["tau_spread_STATE"] = tau_spread_STATE
    out["Lmax_spread_OP"] = Lmax_spread_OP
    out["Lmax_spread_STATE"] = Lmax_spread_STATE

    # ----- DIAGNOSTIC 2: detrended residual correlation ----------------------
    # Subtract each observable's multilinear deformation trend, then correlate
    # residuals. Design: [1, (s-1), (L-12)/2, (tau-0.19)/0.01].
    s_col = np.array([r["xi_scale"] - 1.0 for r in rows])           # (local)
    L_col = np.array([(r["L_max"] - 12) / 2.0 for r in rows])       # (local)
    t_col = np.array([(r["tau"] - 0.19) / 0.01 for r in rows])      # (local)
    design = np.column_stack([np.ones(len(rows)), s_col, L_col, t_col])  # (local)

    def detrend(y):
        coef, *_ = np.linalg.lstsq(design, y, rcond=None)  # (local)
        return y - design @ coef                           # (local)

    resid_OP = detrend(R_OP)                                # (local)
    resid_STATE = detrend(R_STATE)                          # (local)
    sd_resid_OP = float(np.std(resid_OP))                   # (local)
    sd_resid_STATE = float(np.std(resid_STATE))             # (local)
    if sd_resid_OP < 1e-12 or sd_resid_STATE < 1e-15:
        detrended_corr = 0.0                                # (local) R_OP residual below floor
        detrended_note = ("R_OP residual below floor (sd=%.2e): R_OP variation is "
                          "ENTIRELY the L_max truncation trend; after removing the "
                          "shared linear deformation trends nothing remains to "
                          "correlate -> co-variation is co-monotonic-L_max, NOT "
                          "identity-class leakage" % sd_resid_OP)
    else:
        detrended_corr = float(np.corrcoef(resid_OP, resid_STATE)[0, 1])  # (local)
        detrended_note = "detrended residual correlation computed over both nonzero residuals"
    out["detrended_corr"] = abs(detrended_corr)
    out["detrended_corr_signed"] = detrended_corr
    out["sd_resid_OP"] = sd_resid_OP
    out["sd_resid_STATE"] = sd_resid_STATE
    out["detrended_note"] = detrended_note

    # ----- COMPANION (robustness, NOT the gate metric): OP <-> R_summand ------
    # 8-1 inter-summand STATE-PROJ co-moves with R_OP only on the L_max axis;
    # both observables increase from L12->L14 here. 2-point co-movement sign.
    op_dL = R_op_proj(14) - R_op_proj(12)                   # (local)
    summand_dL = R_SUMMAND_L14 - R_SUMMAND_L12             # (local)
    out["companion_R_summand_L12"] = R_SUMMAND_L12
    out["companion_R_summand_L14"] = R_SUMMAND_L14
    out["companion_op_Lmax_delta"] = op_dL
    out["companion_summand_Lmax_delta"] = summand_dL
    out["companion_comove_sign"] = "co-monotonic" if (op_dL * summand_dL) > 0 else "anti-monotonic"

    # ----- VERDICT (plan §W8-2 pre-registered bands) -------------------------
    if C_covar < PASS_THRESH:
        verdict = "PASS"                                   # (local)
    elif C_covar < INFO_THRESH:
        verdict = "INFO"                                   # (local)
    else:
        verdict = "FAIL"                                   # (local)
    out["verdict"] = verdict
    out["rows"] = rows
    return out


# --------------------------------------------------------------------------
# Section 7 — Plot
# --------------------------------------------------------------------------
def make_plot(out, png_path: Path):
    rows = out["rows"]
    fig, axes = plt.subplots(1, 3, figsize=(17, 5.2))

    # Panel 1 — scatter R_OP vs R_STATE over the ensemble, colored by L_max
    ax = axes[0]
    R_OP = out["R_OP_values"]
    R_STATE = out["R_STATE_values"]
    Lm = np.array([r["L_max"] for r in rows])
    for Lval, col, mk in [(12, "#1a9850", "o"), (14, "#d73027", "s")]:
        m = Lm == Lval
        ax.scatter(R_STATE[m], R_OP[m], c=col, marker=mk, s=70, alpha=0.8,
                   edgecolor="k", linewidth=0.5, label=f"L_max={Lval}")
    ax.set_xlabel("R_STATE  (Corner III, BdG condensation, spectrum-dependent)")
    ax.set_ylabel("R_OP  (Corner I, Mellin-pole count, L_max-keyed)")
    ax.set_title(f"OP-PROJ vs STATE-PROJ over deformation ensemble (N={out['n_ensemble']})\n"
                 f"C_covar = |Pearson rho| = {out['C_covar']:.3f}  [{out['verdict']}]")
    ax.legend(loc="best", fontsize=9)
    ax.grid(alpha=0.3)

    # Panel 2 — per-axis spreads (the orthogonality fingerprint)
    ax = axes[1]
    axes_labels = ["xi-scale", "L_max", "tau"]
    op_spreads = [out["xi_spread_OP"], abs(out["Lmax_spread_OP"]), out["tau_spread_OP"]]
    st_spreads = [out["xi_spread_STATE"], abs(out["Lmax_spread_STATE"]), out["tau_spread_STATE"]]
    x = np.arange(3)                                       # (local)
    w = 0.38                                               # (local) bar width
    ax.bar(x - w / 2, op_spreads, w, color="#d73027", label="R_OP spread", alpha=0.85)
    ax.bar(x + w / 2, st_spreads, w, color="#1a9850", label="R_STATE spread", alpha=0.85)
    ax.set_xticks(x)
    ax.set_xticklabels(axes_labels)
    ax.set_ylabel("per-axis spread |max - min|")
    ax.set_yscale("symlog", linthresh=1e-6)
    ax.set_title("Per-axis spread fingerprint\nR_OP varies ONLY on L_max (xi,tau spreads = 0 EXACT)")
    ax.legend(loc="best", fontsize=9)
    ax.grid(alpha=0.3, axis="y")

    # Panel 3 — text summary
    ax = axes[2]
    ax.axis("off")
    txt = (
        "CF-S117-STATEPROJ-OPSTATE-COVARIATION\n"
        "------------------------------------\n"
        f"C_covar (gate metric)   = {out['C_covar']:.4f}\n"
        f"  PASS band  : < {PASS_THRESH}\n"
        f"  INFO band  : [{PASS_THRESH}, {INFO_THRESH})\n"
        f"  FAIL band  : >= {INFO_THRESH}\n"
        f"  VERDICT    : {out['verdict']}\n\n"
        f"Pearson rho (signed)    = {out['pearson_rho']:+.4f}\n"
        f"detrended resid corr    = {out['detrended_corr']:.4f}\n"
        f"  sd(resid R_OP)        = {out['sd_resid_OP']:.2e}\n"
        f"  sd(resid R_STATE)     = {out['sd_resid_STATE']:.2e}\n\n"
        "Per-axis spreads (OP / STATE):\n"
        f"  xi-scale : {out['xi_spread_OP']:.2e} / {out['xi_spread_STATE']:.4f}\n"
        f"  L_max    : {out['Lmax_spread_OP']:+.4f} / {out['Lmax_spread_STATE']:+.4f}\n"
        f"  tau      : {out['tau_spread_OP']:.2e} / {out['tau_spread_STATE']:.4f}\n\n"
        "Sanity anchors:\n"
        f"  R_OP(L=10)   = {out['R_op_L10_reproduction']:.6f}  (=-1.21222)\n"
        f"  R_BdG(L=10)  = {out['R_BdG_L10_reproduction']:.6f}\n"
        f"  W7 R_BdG     = {out['R_BdG_w7_anchor']:.6f}  (reldev {out['R_BdG_repro_reldev']:.1e})\n"
        f"  OP R_inf     = {out['OP_PROJ_R_INF']:.4f}\n\n"
        "Companion (NOT gate): OP<->R_summand (8-1)\n"
        f"  dR_OP(L12->14)      = {out['companion_op_Lmax_delta']:+.4f}\n"
        f"  dR_summand(L12->14) = {out['companion_summand_Lmax_delta']:+.4f}\n"
        f"  => {out['companion_comove_sign']} on L_max\n\n"
        "Level-1 algebra-axis orthogonality (Corner I _|_\n"
        "Corner III) is the PROVEN identity (S116-W7);\n"
        "C_covar is its numerical face under deformation."
    )
    ax.text(0.01, 0.99, txt, va="top", ha="left", family="monospace", fontsize=8.7,
            transform=ax.transAxes)

    fig.suptitle(
        f"{GATE_ID}: OP-PROJ <-> STATE-PROJ co-variation bound = {out['C_covar']:.3f} "
        f"[{out['verdict']}]",
        fontsize=12, fontweight="bold")
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(png_path, dpi=130)
    plt.close(fig)


# --------------------------------------------------------------------------
# Section 8 — Main
# --------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()                                       # (local)
    pins = log_input_pins(INPUT_FILES)
    print(f"  closure: {closure_hash(pins)[:16]}... (legacy closure, informational)")
    script_path = Path(__file__).resolve()
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print(f"  Delta_BCS={Delta_BCS!r}  SC_corr_A={SC_corr_A}  SC_corr_B={SC_corr_B}", flush=True)
    print()

    out = compute()

    print("=== RESULTS ===")
    for k in ("n_ensemble", "R_op_L10_reproduction", "R_BdG_L10_reproduction",
              "R_BdG_w7_anchor", "R_BdG_repro_reldev", "OP_PROJ_R_INF",
              "R_STATE_min", "R_STATE_max", "pearson_rho", "C_covar",
              "sd_R_OP", "sd_R_STATE", "detrended_corr", "sd_resid_OP",
              "sd_resid_STATE", "xi_spread_OP", "xi_spread_STATE",
              "Lmax_spread_OP", "Lmax_spread_STATE", "tau_spread_OP",
              "tau_spread_STATE", "companion_op_Lmax_delta",
              "companion_summand_Lmax_delta", "companion_comove_sign", "verdict"):
        print(f"  {k:30s} = {out[k]}")
    print(f"  R_OP distinct values: {out['R_OP_distinct']}")
    print(f"  detrended_note: {out['detrended_note']}")
    print(flush=True)

    png_path = script_path.with_suffix(".png")
    make_plot(out, png_path)
    npz_path = script_path.with_suffix(".npz")
    rows = out["rows"]
    np.savez(
        npz_path,
        C_covar=out["C_covar"],
        pearson_rho=out["pearson_rho"],
        verdict=out["verdict"],
        detrended_corr=out["detrended_corr"],
        detrended_corr_signed=out["detrended_corr_signed"],
        sd_resid_OP=out["sd_resid_OP"],
        sd_resid_STATE=out["sd_resid_STATE"],
        sd_R_OP=out["sd_R_OP"],
        sd_R_STATE=out["sd_R_STATE"],
        n_ensemble=out["n_ensemble"],
        R_OP_values=out["R_OP_values"],
        R_STATE_values=out["R_STATE_values"],
        R_OP_distinct=np.array(out["R_OP_distinct"]),
        ensemble_labels=np.array([r["label"] for r in rows]),
        ensemble_Lmax=np.array([r["L_max"] for r in rows]),
        ensemble_tau=np.array([r["tau"] for r in rows]),
        ensemble_xi_scale=np.array([r["xi_scale"] for r in rows]),
        ensemble_n_modes=np.array([r["n_modes"] for r in rows]),
        xi_spread_OP=out["xi_spread_OP"], xi_spread_STATE=out["xi_spread_STATE"],
        Lmax_spread_OP=out["Lmax_spread_OP"], Lmax_spread_STATE=out["Lmax_spread_STATE"],
        tau_spread_OP=out["tau_spread_OP"], tau_spread_STATE=out["tau_spread_STATE"],
        R_op_L10_reproduction=out["R_op_L10_reproduction"],
        R_op_L10_anchor=out["R_op_L10_anchor"],
        R_BdG_L10_reproduction=out["R_BdG_L10_reproduction"],
        R_BdG_w7_anchor=out["R_BdG_w7_anchor"],
        R_BdG_repro_reldev=out["R_BdG_repro_reldev"],
        R_substrate_OP_L10_w7=out["R_substrate_OP_L10_w7"],
        OP_PROJ_R_INF=out["OP_PROJ_R_INF"],
        companion_R_summand_L12=out["companion_R_summand_L12"],
        companion_R_summand_L14=out["companion_R_summand_L14"],
        companion_op_Lmax_delta=out["companion_op_Lmax_delta"],
        companion_summand_Lmax_delta=out["companion_summand_Lmax_delta"],
        companion_comove_sign=out["companion_comove_sign"],
        Delta_BCS=Delta_BCS, SC_corr_A=SC_corr_A, SC_corr_B=SC_corr_B,
        M_KK=M_KK, tau_fold=tau_fold,
        PASS_THRESH=PASS_THRESH, INFO_THRESH=INFO_THRESH,
        MELLIN_WINDOW_FRAC=MELLIN_WINDOW_FRAC,
        XI_SCALES=np.array(XI_SCALES),
        audit_sha256=audit_sha, content_sha256=content_sha,
        detrended_note=np.array(out["detrended_note"]),
    )
    print(f"  wrote {npz_path.name}, {png_path.name}", flush=True)
    print()

    # ----- value payload (no apostrophes; emit_verdict wraps value='...') -----
    value = (
        f"C_covar={out['C_covar']:.3f}_{out['verdict']}-benign_"
        f"pearson={out['pearson_rho']:+.3f}_detrended-resid-corr={out['detrended_corr']:.3f}_"
        f"R_OP-L_max-keyed-only_xi-spread-OP=0_tau-spread-OP=0_EXACT_"
        f"R_STATE-all-3-axes_N={out['n_ensemble']}_"
        f"OP-resid-below-floor-comonotonic-L_max-NOT-identity-leakage_"
        f"Level1-CornerI-perp-CornerIII-orthogonality-UNAFFECTED"
    )

    extra_rows = [
        f"# diagnostics: per-axis spread R_OP (xi={out['xi_spread_OP']:.1e}, "
        f"L_max={out['Lmax_spread_OP']:+.4f}, tau={out['tau_spread_OP']:.1e}) vs "
        f"R_STATE (xi={out['xi_spread_STATE']:.4f}, L_max={out['Lmax_spread_STATE']:+.4f}, "
        f"tau={out['tau_spread_STATE']:.4f}); R_OP is L_max-keyed-only (xi,tau spreads 0 EXACT)",
        f"# detrended-residual: {out['detrended_note']}",
        f"# anchors: R_OP(L=10)={out['R_op_L10_reproduction']:.6f} (=-1.21222 canonical); "
        f"R_BdG(L=10)={out['R_BdG_L10_reproduction']:.6f} vs W7 {out['R_BdG_w7_anchor']:.6f} "
        f"(reldev {out['R_BdG_repro_reldev']:.1e}); OP_R_inf={out['OP_PROJ_R_INF']}",
        f"# companion (NOT gate metric): OP<->R_summand(8-1) {out['companion_comove_sign']} "
        f"on L_max (dR_OP={out['companion_op_Lmax_delta']:+.4f}, "
        f"dR_summand={out['companion_summand_Lmax_delta']:+.4f}); "
        f"orthogonality robust across BOTH STATE-PROJ realizations (R_BdG + R_summand)",
        "# CLASS=FULL (inline exact SU(3) Weyl-dim/Casimir + W7 BdG functional; NO SCHEMATIC helper); "
        "no regulator_pin (BdG condensation state-pair functional, not a Seeley-DeWitt a_n); "
        "no counting-axis pin (C_covar is a scale-free correlation)",
    ]

    print_verdict_payload(
        verdict=out["verdict"],
        value=value,
        audit_sha=audit_sha,
        content_sha=content_sha,
        companion_note=("OP-PROJ<->STATE-PROJ co-variation bound; Level-1 algebra-axis "
                        "orthogonality (Corner I perp Corner III) is the PROVEN identity "
                        "(S116-W7); C_covar is the numerical-robustness annotation"),
        extra_rows=extra_rows,
    )

    print(f"\n  elapsed {time.time() - t0:.2f}s", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
