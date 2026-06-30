#!/usr/bin/env python3
"""
S101 W5-3 S101-TRICRITICAL-ADJACENCY — fold placement vs kitaev-litrev V.4 template
===================================================================================

Gate: S101-TRICRITICAL-ADJACENCY ([VERIFY])

Pre-registered threshold (composite-conjunction classification gate, V.4 lineage):
  PASS iff (A) r_adj < 0.9 AND (B) P1: max-residual <= 1e-6 AND
           (C) P2: |nuz_pre - 1| <= 0.10 AND |nuz_post - 1| <= 0.10.
  INFO iff r_adj in [0.9, 1.0) (marginal)  OR  P1 residual > 1e-6 (Rao-dominant
           with Li-class sub-window CANDIDATE)  OR  exactly one P2 side breaches.
  FAIL iff r_adj >= 1.0 (Li inequality reversed — contradicts stored S100b
           diagnostics)  OR  both P2 sides breach (un-pins first-order scoping).

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - computations/session-100b/s100b_fold_range_scaling.npz
      (pin 807879880dc13af38e9078ec63c47f227271f06fb58d0df949a7c3f3dfddb98f)
  - sessions/archive/session-99/session-99-litrev-nonequilibrium-transit-kitaev.md
      (pin 76954bd7ca386acbc3b73d24d7e14b5256b93e29d77b0211d2ec23f0c211a182; §V.4 read)
  - canonical_constants.py (feeds audit_sha256 only; consumed name: tau_fold)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<classification string>, scheme=RAO-RANGE-V4-TEMPLATE, convention=RATIO, L_max=N/A)

Classification: GEOMETRIC — fold placement in the (z, z', nu) diagnostic space of
the Jensen deformation manifold (Level-2 moduli-deformation substrate-IS object);
the diagnostic exponents are NOT critical exponents — nu*z ~ 1 is the analytic
slope of the d2S spectral-action curvature across the first-order van Hove fold.

METHODOLOGY
-----------
The kitaev-litrev V.4 template (session-99-litrev-nonequilibrium-transit-kitaev.md
§V.4) defines a classification gate: extract (z, z', nu) from the fold's gap closure,
apply the Li KZ-survival inequality z' < z + 1/nu as a SECONDARY scaling beneath the
dominant range-saturation, and output 'Rao-class only' vs 'Rao-dominant with a
Li-class sub-window'. KO-dim=6 emergent-SUSY (eta_b = eta_f) is a NARRATIVE
cross-link flag only — never a gate input. All three pinned criteria are evaluated
on the stored S100b W5-2 fold-range-scaling diagnostics (PASS, rho_S=1.0 exact):
  (A) r_adj = zprime_eff / (z_eff + 1/nu_eff): the Li ratio. SURVIVAL iff < 1
      (inequality verbatim), non-marginal iff < 0.9, expected 0.535352.
  (B) P1 range-law completeness: reconstruct n_hat_rel(lambda) from the SINGLE
      scalar eps_canonical ALONE (one parameter, nine points: over-determined),
      test max |n_rel/n_hat_rel - 1| <= 1e-6.
  (C) P2 VH-degeneracy reading of nu*z ~ 1: |nuz_pre-1| <= 0.10 AND
      |nuz_post-1| <= 0.10, band = 1.23x analytic curvature scale
      curv_scale*dtau_window = 0.0813.

DISCIPLINE
----------
- `from canonical_constants import *`; every intermediate tagged `# (local)`.
- a_n Seeley-DeWitt regulator tags: N/A — this gate consumes stored diagnostic
  exponents (z, z', nu, nu*z) and dimensionless ratios; no a_n coefficient is
  cited, so the `a_n^{regulator}` discipline is vacuous here. The upstream
  d2S curvature scale curv_scale is a stored npz scalar, not an a_n coefficient.
- SHA-256 of all input files logged in first 20 lines of stdout; dual-SHA emitted.
- Verdict emitted via the emit_verdict knowledge-MCP tool (race-safe); the script
  PRINTS the payload via print_verdict_payload and does NOT write the verdict file.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent.parent / "_shared"))
from canonical_constants import *  # noqa: F401,F403  (provides tau_fold)
from canonical_constants import tau_fold

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
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

SESSION = "S101"                                                   # (local)
GATE_ID = "S101-TRICRITICAL-ADJACENCY"                            # (local)
SCHEME = "RAO-RANGE-V4-TEMPLATE"                                  # (local)
CONVENTION = "RATIO"                                              # (local)
L_MAX = "N/A"                                                     # (local)

# Pre-registered thresholds (define BEFORE running) — exact rationals
R_ADJ_MARGINAL_EDGE = 9.0 / 10.0     # r_adj < 0.9 => non-marginal SURVIVAL  # (local)
R_ADJ_SURVIVAL_EDGE = 1.0            # r_adj < 1.0 => SURVIVAL (Li verbatim) # (local)
P1_RESIDUAL_TOL = 1e-6              # range-law completeness                # (local)
P2_BAND = 1.0 / 10.0               # |nu*z - 1| <= 0.10 per side           # (local)

# Output destinations
OUT_NPZ = SESSION_DIR / "s101_w5_3_tricritical_adjacency.npz"
OUT_PNG = SESSION_DIR / "s101_w5_3_tricritical_adjacency.png"

FOLD_NPZ = COMPUTATIONS_DIR / "session-100b" / "s100b_fold_range_scaling.npz"
LITREV_MD = (
    PROJECT_ROOT / "sessions" / "session-99"
    / "session-99-litrev-nonequilibrium-transit-kitaev.md"
)

# Expected input pins (plan-frozen; verified at runtime)
FOLD_NPZ_PIN = "807879880dc13af38e9078ec63c47f227271f06fb58d0df949a7c3f3dfddb98f"  # (local)
LITREV_PIN = "76954bd7ca386acbc3b73d24d7e14b5256b93e29d77b0211d2ec23f0c211a182"     # (local)

# INPUT_FILES feed the pinmap_json (the audit_sha256 input-pin map): the
# fold-range-scaling npz SHA + the litrev SHA + canonical_constants.py, exactly
# per the plan's audit_sha256_inputs "input-pin map (fold-range-scaling npz SHA
# + litrev SHA)" + machinery_pin_map.
INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    FOLD_NPZ,
    LITREV_MD,
]

# machinery_pin_map (folded into the audit closure per audit_sha256_inputs item 3)
MACHINERY_PIN_MAP = {
    "N_eval": "9(lambda)+11(mach)+1(eps_canonical)",
    "L_max": "N/A",
    "scan_range": "lambda[0.25,4] stored; no new scan",
    "step_size": "N/A stored grids",
    "tolerance": "P1=1e-6;P2=0.10;r_adj_bands={0.9,1.0}",
    "scheme": SCHEME,
    "convention": CONVENTION,
    "adjacency_band_pin": "SURVIVAL iff r_adj<1; non-marginal iff r_adj<0.9; expected 0.535352",
    "profile_class_pin": "P1(range-law,1e-6) AND P2(VH-degeneracy,+/-0.10 both sides)",
    "random_seed": "N/A deterministic",
    "GPU_path": "cpu-cap-OMP8",
}


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
    machinery: dict[str, str],
) -> tuple[str, str]:
    """(audit_sha256, content_sha256) per S84+ dual-SHA schema.

    audit_sha256   = sha256( bytes(script) || bytes(canonical) || pinmap_json )
                     where pinmap_json folds in the input-pin map (incl. the
                     fold-range-scaling npz SHA + litrev SHA) AND the
                     machinery_pin_map (audit_sha256_inputs item 3).
    content_sha256 = sha256( bytes(script) ).
    """
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

    pinmap_obj = {"input_pins": dict(sorted(pins.items())),
                  "machinery_pin_map": dict(sorted(machinery.items()))}  # (local)
    pinmap_json = json.dumps(
        pinmap_obj, separators=(",", ":"), sort_keys=True
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
# Section 5 — Compute
# ---------------------------------------------------------------------------

def compute() -> dict:
    """Evaluate the three pinned V.4-template criteria on the stored S100b npz."""
    d = np.load(FOLD_NPZ, allow_pickle=True)  # (local)

    # ---- stored diagnostic exponents (V.4 template inputs) ----
    z_eff = float(d["z_eff"])              # (local) 1.9040995889317789
    zprime_eff = float(d["zprime_eff"])    # (local) 2.0900692321679655
    nu_eff = float(d["nu_eff"])            # (local) 0.5
    li_lhs_rhs = np.asarray(d["li_inequality_lhs_rhs"], dtype=float)  # (local) cross-check pair
    eps_canonical = float(d["eps_canonical"])  # (local) 6.838563969200696e-4
    lambda_grid = np.asarray(d["lambda_grid"], dtype=float)            # (local) 9 pts
    n_rel_vs_lambda = np.asarray(d["n_rel_vs_lambda"], dtype=float)    # (local) 9 pts stored
    nuz_pre = float(d["nuz_pre"])          # (local) 0.9520497944658894
    nuz_post = float(d["nuz_post"])        # (local) 1.0450346160839827
    curv_scale = float(d["curv_scale"])    # (local) 2.7087750704568077
    dtau_window = float(d["dtau_window"])  # (local) 0.03
    rho_S = float(d["rho_S_spearman"])     # (local) 1.0 exact (monotone profile)
    p_range_fit = float(d["p_range_fit"])  # (local) 1.000859... Rao range-law exponent

    # =====================================================================
    # (A) ADJACENCY BAND — r_adj = zprime / (z + 1/nu)   [Li ratio]
    #   Substitution chain:
    #     denom = z_eff + 1/nu_eff = 1.9040995889317789 + 1/0.5
    #           = 1.9040995889317789 + 2.0 = 3.9040995889317789  (= li_rhs)
    #     r_adj = zprime_eff / denom = 2.0900692321679655 / 3.9040995889...
    #           = 0.535352...
    #     r_adj < 1.0 => SURVIVAL (Li inequality z' < z + 1/nu holds verbatim)
    #     r_adj < 0.9 => non-marginal
    # =====================================================================
    denom_li = z_eff + 1.0 / nu_eff   # (local)
    r_adj = zprime_eff / denom_li     # (local)
    margin_to_survival = R_ADJ_SURVIVAL_EDGE - r_adj  # (local) distance to boundary 1.0
    margin_to_marginal = R_ADJ_MARGINAL_EDGE - r_adj  # (local) distance to 0.9 edge

    # cross-check: stored li_inequality_lhs_rhs == (zprime, z + 1/nu)
    li_lhs_match = abs(li_lhs_rhs[0] - zprime_eff)   # (local)
    li_rhs_match = abs(li_lhs_rhs[1] - denom_li)     # (local)
    li_survival_verbatim = bool(li_lhs_rhs[0] < li_lhs_rhs[1])  # (local) z' < z+1/nu

    if r_adj >= R_ADJ_SURVIVAL_EDGE:
        band_A = "NON-SURVIVAL"          # (local)
        A_pass = False                   # (local)
        A_marginal = False               # (local)
    elif r_adj >= R_ADJ_MARGINAL_EDGE:
        band_A = "BOUNDARY-MARGINAL"     # (local)
        A_pass = False                   # (local) marginal -> INFO, not PASS
        A_marginal = True                # (local)
    else:
        band_A = "SURVIVAL-non-marginal"  # (local)
        A_pass = True                     # (local)
        A_marginal = False                # (local)

    # =====================================================================
    # (B) PROFILE-CLASS P1 — range-law completeness.
    #   Reconstruct n_hat_rel(lambda) = lambda * exp(eps_c * (1 - 1/lambda))
    #   from eps_canonical ALONE (never from n_rel_vs_lambda). One scalar
    #   parameter explains nine stored points: over-determined cross-check.
    #   PASS iff max_lambda |n_rel_vs_lambda / n_hat_rel - 1| <= 1e-6.
    # =====================================================================
    n_hat_rel = lambda_grid * np.exp(eps_canonical * (1.0 - 1.0 / lambda_grid))  # (local)
    p1_residual_profile = np.abs(n_rel_vs_lambda / n_hat_rel - 1.0)              # (local) 9 pts
    p1_max_residual = float(np.max(p1_residual_profile))                          # (local)
    P1_pass = bool(p1_max_residual <= P1_RESIDUAL_TOL)                            # (local)

    # deviation-from-proportionality structure D(lambda) = n_rel/lambda - 1
    # (the CF's 'non-monotone profile' = sign change of D at lambda=1, curvature
    #  keyed to eps_c — NOT a non-monotone n_rel; rho_S=1.0 confirms monotone).
    D_lambda = n_rel_vs_lambda / lambda_grid - 1.0                               # (local) sign-change @ lambda=1
    D_hat_lambda = n_hat_rel / lambda_grid - 1.0                                 # (local) range-law D
    D_residual = np.abs(D_lambda - D_hat_lambda)                                 # (local)
    D_max_residual = float(np.max(D_residual))                                   # (local)

    # =====================================================================
    # (C) PROFILE-CLASS P2 — VH-degeneracy reading of nu*z ~ 1.
    #   Substitution chain (band derivation):
    #     analytic first-order: nu*z = 1 EXACTLY in delta->0; finite-window
    #       corrections +/- curv_scale*delta. expected |nu*z-1| <~ curv_scale*dtau
    #       = 2.7087750704568077 * 0.03 = 0.08126.
    #     band |nu*z-1| <= 0.10 (= 1.23x the curvature-correction scale).
    #     stored deviations: |nuz_pre-1|=0.0480, |nuz_post-1|=0.0450; both
    #       < 0.08126 < 0.10 => both-side PASS; slope = analytic d2S fold
    #       curvature, NOT an independent critical exponent.
    # =====================================================================
    analytic_corr_scale = curv_scale * dtau_window  # (local) 0.08126
    dev_pre = abs(nuz_pre - 1.0)                     # (local) 0.0480
    dev_post = abs(nuz_post - 1.0)                   # (local) 0.0450
    P2_pre_pass = bool(dev_pre <= P2_BAND)           # (local)
    P2_post_pass = bool(dev_post <= P2_BAND)         # (local)
    P2_pass = bool(P2_pre_pass and P2_post_pass)     # (local)
    P2_n_breaches = int((not P2_pre_pass) + (not P2_post_pass))  # (local) 0/1/2

    # =====================================================================
    # COMPOSITE classification (composite-conjunction; V.4 template)
    # =====================================================================
    if r_adj >= R_ADJ_SURVIVAL_EDGE:
        verdict = "FAIL"                  # (local) Li inequality reversed
        fail_reason = "r_adj>=1.0 (Li inequality reversed — contradicts stored S100b diagnostics)"  # (local)
    elif P2_n_breaches == 2:
        verdict = "FAIL"                  # (local) both P2 sides breach
        fail_reason = "both P2 sides breach nu*z analytic-first-order band (un-pins S100b W5-2 first-order scoping)"  # (local)
    elif A_pass and P1_pass and P2_pass:
        verdict = "PASS"                  # (local)
        fail_reason = ""                  # (local)
    else:
        verdict = "INFO"                  # (local) marginal / P1 residual / one-sided P2
        reasons = []                      # (local)
        if A_marginal:
            reasons.append("r_adj marginal [0.9,1.0)")
        if not P1_pass:
            reasons.append("P1 residual>1e-6 (Rao-dominant with Li-class sub-window CANDIDATE)")
        if P2_n_breaches == 1:
            side = "pre" if not P2_pre_pass else "post"  # (local)
            reasons.append(f"one-sided P2 breach ({side})")
        fail_reason = "; ".join(reasons)  # (local)

    # V.4 template classification string (scoping verbatim)
    if verdict == "PASS":
        classification = "first-order, tricritical-ADJACENT only | Rao-class only (no residual Li-class KZ sub-window)"  # (local)
    elif verdict == "INFO" and not P1_pass:
        classification = "first-order, tricritical-ADJACENT only | Rao-dominant with Li-class sub-window CANDIDATE"  # (local)
    elif verdict == "INFO":
        classification = "first-order, tricritical-ADJACENT only | Rao-class (marginal/asymmetric extraction flag)"  # (local)
    else:
        classification = "FAIL — fold re-classification required (contradicts S100b first-order scoping)"  # (local)

    # KO-dim=6 emergent-SUSY adjacency flag (NARRATIVE cross-link ONLY; never a
    # gate input). The V.4 template flags eta_b = eta_f iff emergent SUSY appears
    # at the fold. This gate does NOT compute eta_b/eta_f (the boson/fermion
    # spectral-asymmetry pair); the adjacency is UNTESTED and flagged-only.
    ko6_susy_flag = "UNTESTED — eta_b=eta_f emergent-SUSY adjacency not computed here (narrative cross-link to KO-dim=6 only)"  # (local)

    return {
        # criterion A
        "z_eff": z_eff, "zprime_eff": zprime_eff, "nu_eff": nu_eff,
        "denom_li": denom_li, "r_adj": r_adj,
        "margin_to_survival": margin_to_survival,
        "margin_to_marginal": margin_to_marginal,
        "band_A": band_A, "A_pass": A_pass, "A_marginal": A_marginal,
        "li_inequality_lhs_rhs": li_lhs_rhs,
        "li_lhs_match": li_lhs_match, "li_rhs_match": li_rhs_match,
        "li_survival_verbatim": li_survival_verbatim,
        # criterion B (P1)
        "eps_canonical": eps_canonical,
        "lambda_grid": lambda_grid,
        "n_rel_vs_lambda": n_rel_vs_lambda,
        "n_hat_rel": n_hat_rel,
        "p1_residual_profile": p1_residual_profile,
        "p1_max_residual": p1_max_residual, "P1_pass": P1_pass,
        "D_lambda": D_lambda, "D_hat_lambda": D_hat_lambda,
        "D_max_residual": D_max_residual,
        "p_range_fit": p_range_fit, "rho_S": rho_S,
        # criterion C (P2)
        "nuz_pre": nuz_pre, "nuz_post": nuz_post,
        "curv_scale": curv_scale, "dtau_window": dtau_window,
        "analytic_corr_scale": analytic_corr_scale,
        "dev_pre": dev_pre, "dev_post": dev_post,
        "P2_pre_pass": P2_pre_pass, "P2_post_pass": P2_post_pass,
        "P2_pass": P2_pass, "P2_n_breaches": P2_n_breaches,
        # composite
        "verdict": verdict, "fail_reason": fail_reason,
        "classification": classification,
        "ko6_susy_flag": ko6_susy_flag,
        "tau_fold": float(tau_fold),
        # thresholds (pinned)
        "R_ADJ_MARGINAL_EDGE": R_ADJ_MARGINAL_EDGE,
        "R_ADJ_SURVIVAL_EDGE": R_ADJ_SURVIVAL_EDGE,
        "P1_RESIDUAL_TOL": P1_RESIDUAL_TOL,
        "P2_BAND": P2_BAND,
    }


# ---------------------------------------------------------------------------
# Section 6 — Verdict payload
# ---------------------------------------------------------------------------

def print_verdict_payload(verdict, value, audit_sha, content_sha):
    """Emit the verdict PAYLOAD for the dispatching AGENT to pass to emit_verdict.
    The script does NOT write the verdict file (race-safe; gate-verdicts.md)."""
    payload = {
        "session": 101,
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
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 7 — Plot
# ---------------------------------------------------------------------------

def make_plot(R: dict) -> None:
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(13, 5.2))

    # Panel (a): n_rel_vs_lambda + range-law reconstruction + residual
    lam = R["lambda_grid"]  # (local)
    ax0.plot(lam, R["n_rel_vs_lambda"], "o", ms=8, mfc="none",
             mec="C0", mew=1.8, label="stored $n_{rel}(\\lambda)$ (S100b)")
    lam_fine = np.linspace(lam.min(), lam.max(), 200)  # (local)
    eps = R["eps_canonical"]  # (local)
    n_hat_fine = lam_fine * np.exp(eps * (1.0 - 1.0 / lam_fine))  # (local)
    ax0.plot(lam_fine, n_hat_fine, "-", color="C3", lw=1.6,
             label="range law $\\hat n_{rel}=\\lambda\\,e^{\\varepsilon_c(1-1/\\lambda)}$")
    ax0.set_xlabel("$\\lambda$ (fold range / canonical)")
    ax0.set_ylabel("$n_{rel}$ (relic-count / canonical)")
    ax0.set_title("(a) range-law completeness (P1)\n"
                  f"max residual = {R['p1_max_residual']:.2e}  "
                  f"(tol $\\leq$ {R['P1_RESIDUAL_TOL']:.0e})")
    ax0.legend(loc="upper left", fontsize=8)
    ax0.grid(alpha=0.3)
    axr = ax0.twinx()  # (local)
    axr.semilogy(lam, np.maximum(R["p1_residual_profile"], 1e-18), "s",
                 ms=5, color="C2", alpha=0.7, label="|residual|")
    axr.axhline(R["P1_RESIDUAL_TOL"], color="C2", ls="--", lw=1.0, alpha=0.6)
    axr.set_ylabel("|$n_{rel}/\\hat n_{rel}-1$|  (log)", color="C2")
    axr.tick_params(axis="y", labelcolor="C2")

    # Panel (b): fold placement in (r_adj, |nuz-1|) classification plane
    ax1.axvspan(0.0, R["R_ADJ_MARGINAL_EDGE"], color="C2", alpha=0.10,
                label="SURVIVAL non-marginal ($r_{adj}<0.9$)")
    ax1.axvspan(R["R_ADJ_MARGINAL_EDGE"], R["R_ADJ_SURVIVAL_EDGE"],
                color="C1", alpha=0.12, label="boundary-marginal [0.9,1.0)")
    ax1.axvspan(R["R_ADJ_SURVIVAL_EDGE"], 1.3, color="C3", alpha=0.10,
                label="NON-SURVIVAL ($r_{adj}\\geq1$)")
    ax1.axhspan(0.0, R["P2_BAND"], color="C0", alpha=0.06)
    ax1.axhline(R["P2_BAND"], color="C0", ls="--", lw=1.0,
                label="P2 band $|\\nu z-1|\\leq0.10$")
    ax1.axhline(R["analytic_corr_scale"], color="C4", ls=":", lw=1.2,
                label=f"analytic curv. scale {R['analytic_corr_scale']:.4f}")
    # fold point: r_adj on x, max(|nuz-1|) on y
    y_fold = max(R["dev_pre"], R["dev_post"])  # (local)
    ax1.plot([R["r_adj"]], [y_fold], "*", ms=22, color="k",
             label=f"van Hove fold ($r_{{adj}}$={R['r_adj']:.4f})")
    ax1.plot([R["r_adj"]], [R["dev_pre"]], "v", ms=9, color="C5",
             alpha=0.8, label=f"$|\\nu z_{{pre}}-1|$={R['dev_pre']:.4f}")
    ax1.plot([R["r_adj"]], [R["dev_post"]], "^", ms=9, color="C6",
             alpha=0.8, label=f"$|\\nu z_{{post}}-1|$={R['dev_post']:.4f}")
    ax1.set_xlim(0.0, 1.3)
    ax1.set_ylim(0.0, max(0.12, y_fold * 1.4))
    ax1.set_xlabel("$r_{adj} = z'/(z+1/\\nu)$  (Li ratio)")
    ax1.set_ylabel("$|\\nu z - 1|$  (VH-degeneracy)")
    ax1.set_title(f"(b) fold placement — {R['verdict']}\n"
                  "first-order, tricritical-ADJACENT only")
    ax1.legend(loc="upper right", fontsize=7, ncol=1)
    ax1.grid(alpha=0.3)

    fig.suptitle("S101-TRICRITICAL-ADJACENCY — van Hove fold vs kitaev-litrev V.4 template",
                 fontsize=12, y=1.02)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    pins = log_input_pins(INPUT_FILES)  # (local)

    # Verify input pins against plan-frozen values (PIN-DRIFT guard).
    fold_sha = pins.get("computations/session-100b/s100b_fold_range_scaling.npz", "")  # (local)
    litrev_sha = pins.get(
        "sessions/archive/session-99/session-99-litrev-nonequilibrium-transit-kitaev.md", "")  # (local)
    print(f"  [pin-check] fold npz   == plan pin: {fold_sha == FOLD_NPZ_PIN}")
    print(f"  [pin-check] litrev md  == plan pin: {litrev_sha == LITREV_PIN}")
    if fold_sha != FOLD_NPZ_PIN:
        print(f"  !! FOLD NPZ SHA DRIFT: got {fold_sha}, expected {FOLD_NPZ_PIN}",
              file=sys.stderr)
        return 2
    if litrev_sha != LITREV_PIN:
        print(f"  !! LITREV SHA DRIFT: got {litrev_sha}, expected {LITREV_PIN}",
              file=sys.stderr)
        return 2

    audit_sha, content_sha = compute_dual_sha(
        Path(__file__).resolve(), SHARED_DIR / "canonical_constants.py",
        pins, MACHINERY_PIN_MAP)  # (local)
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")
    print(f"  tau_fold (canonical) = {float(tau_fold)}")

    R = compute()  # (local)

    # ---- report ----
    print("\n=== CRITERION (A) ADJACENCY BAND (Li ratio) ===")
    print(f"  z_eff = {R['z_eff']:.16g}")
    print(f"  zprime_eff = {R['zprime_eff']:.16g}")
    print(f"  nu_eff = {R['nu_eff']:.16g}  ->  1/nu = {1.0/R['nu_eff']:.16g}")
    print(f"  denom = z + 1/nu = {R['denom_li']:.16g}  "
          f"(stored li_rhs = {R['li_inequality_lhs_rhs'][1]:.8f}, "
          f"match diff = {R['li_rhs_match']:.2e})")
    print(f"  r_adj = z'/(z+1/nu) = {R['r_adj']:.16g}  (expected 0.535352)")
    print(f"  margin to survival edge (1.0) = {R['margin_to_survival']:.6f}  (expected 0.4646)")
    print(f"  margin to marginal edge (0.9) = {R['margin_to_marginal']:.6f}")
    print(f"  Li survival verbatim (z'<z+1/nu): {R['li_survival_verbatim']}")
    print(f"  BAND_A = {R['band_A']}  ->  A_pass = {R['A_pass']}")

    print("\n=== CRITERION (B) P1 RANGE-LAW COMPLETENESS ===")
    print(f"  eps_canonical = {R['eps_canonical']:.16g}  (single reconstruction parameter)")
    print(f"  n_hat_rel(lambda) reconstructed from eps_canonical ALONE over 9-pt grid")
    print(f"  max |n_rel/n_hat_rel - 1| = {R['p1_max_residual']:.3e}  (tol <= {R['P1_RESIDUAL_TOL']:.0e})")
    print(f"  D(lambda)=n_rel/lambda-1 sign-change structure residual = {R['D_max_residual']:.3e}")
    print(f"  Rao range-law exponent p_range_fit = {R['p_range_fit']:.6f}; rho_S(monotone) = {R['rho_S']:.6f}")
    print(f"  P1_pass = {R['P1_pass']}")

    print("\n=== CRITERION (C) P2 VH-DEGENERACY (nu*z ~ 1) ===")
    print(f"  curv_scale = {R['curv_scale']:.16g}, dtau_window = {R['dtau_window']:.6g}")
    print(f"  analytic curvature-correction scale = curv_scale*dtau = {R['analytic_corr_scale']:.6f}")
    print(f"  nuz_pre = {R['nuz_pre']:.16g}  ->  |nuz_pre-1| = {R['dev_pre']:.6f}  (<= 0.10? {R['P2_pre_pass']})")
    print(f"  nuz_post = {R['nuz_post']:.16g}  ->  |nuz_post-1| = {R['dev_post']:.6f}  (<= 0.10? {R['P2_post_pass']})")
    print(f"  P2_pass = {R['P2_pass']}  (n_breaches = {R['P2_n_breaches']})")

    print("\n=== COMPOSITE CLASSIFICATION ===")
    print(f"  VERDICT = {R['verdict']}")
    if R["fail_reason"]:
        print(f"  reason: {R['fail_reason']}")
    print(f"  classification: {R['classification']}")
    print(f"  KO-dim=6 SUSY flag: {R['ko6_susy_flag']}")

    # ---- save npz ----
    np.savez(
        OUT_NPZ,
        # A
        z_eff=R["z_eff"], zprime_eff=R["zprime_eff"], nu_eff=R["nu_eff"],
        denom_li=R["denom_li"], r_adj=R["r_adj"],
        margin_to_survival=R["margin_to_survival"],
        margin_to_marginal=R["margin_to_marginal"],
        band_A=np.array([R["band_A"]]), A_pass=R["A_pass"],
        li_inequality_lhs_rhs=R["li_inequality_lhs_rhs"],
        li_survival_verbatim=R["li_survival_verbatim"],
        # B (P1)
        eps_canonical=R["eps_canonical"], lambda_grid=R["lambda_grid"],
        n_rel_vs_lambda=R["n_rel_vs_lambda"], n_hat_rel=R["n_hat_rel"],
        p1_residual_profile=R["p1_residual_profile"],
        p1_max_residual=R["p1_max_residual"], P1_pass=R["P1_pass"],
        D_lambda=R["D_lambda"], D_hat_lambda=R["D_hat_lambda"],
        D_max_residual=R["D_max_residual"],
        p_range_fit=R["p_range_fit"], rho_S=R["rho_S"],
        # C (P2)
        nuz_pre=R["nuz_pre"], nuz_post=R["nuz_post"],
        curv_scale=R["curv_scale"], dtau_window=R["dtau_window"],
        analytic_corr_scale=R["analytic_corr_scale"],
        dev_pre=R["dev_pre"], dev_post=R["dev_post"],
        P2_pre_pass=R["P2_pre_pass"], P2_post_pass=R["P2_post_pass"],
        P2_pass=R["P2_pass"], P2_n_breaches=R["P2_n_breaches"],
        # composite
        verdict=np.array([R["verdict"]]),
        classification=np.array([R["classification"]]),
        ko6_susy_flag=np.array([R["ko6_susy_flag"]]),
        tau_fold=R["tau_fold"],
        # thresholds
        R_ADJ_MARGINAL_EDGE=R["R_ADJ_MARGINAL_EDGE"],
        R_ADJ_SURVIVAL_EDGE=R["R_ADJ_SURVIVAL_EDGE"],
        P1_RESIDUAL_TOL=R["P1_RESIDUAL_TOL"], P2_BAND=R["P2_BAND"],
        audit_sha256=np.array([audit_sha]),
        content_sha256=np.array([content_sha]),
    )
    print(f"\n  saved npz -> {OUT_NPZ}")

    make_plot(R)
    print(f"  saved png -> {OUT_PNG}")

    # ---- 4-tuple (final non-verdict line) ----
    val_str = (f"r_adj={R['r_adj']:.6f}|P1res={R['p1_max_residual']:.2e}|"
               f"nuzdev=({R['dev_pre']:.4f},{R['dev_post']:.4f})|{R['classification']}")  # (local)
    print(f"\n(value={val_str!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")

    # ---- verdict payload ----
    print_verdict_payload(R["verdict"], val_str, audit_sha, content_sha)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
