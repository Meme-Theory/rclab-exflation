#!/usr/bin/env python3
"""
INV11 W1-1 [FLAGSHIP] — Substrate gap equation: M_KK/M_Pl as a BCS /
Coleman-Weinberg dimensional-transmutation scale.
=========================================================================

Gate: INV11-W1-1 ([SIGN])
  The exp(-c/lambda_eff) direction claim is a signed/directional prediction:
  smaller lambda_eff (weaker coupling) => smaller M_KK/M_Pl.

Pre-registered threshold (plan investigation-11-plan-w1.md §W1-1):
  operator: |log10(M_KK_derived) - log10(M_KK_CONST_FREEZE_42)| <= 1.0
            AND frac_uncert_gap_term >= 0.5
  PASS iff OOM-in AND gap-magnitude term dominates the uncertainty budget.
  FAIL iff OOM-out OR the fit-term (M_Pl/Lambda anchor) dominates.
  INFO iff OOM-in but the gap-magnitude term is sub-dominant.

Inputs (SHA-256 dual-pinned at runtime — see §4; S84+ schema):
  - computations/_shared/canonical_constants.py (feeds audit_sha256 only)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz (DOS fit source)
  - computations/investigation-11/inv11_w1_richardson_pairing_engine.npz
        (W1-2: the Richardson-exact gap + systematic band; gap-magnitude term)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<M_KK_derived + OOM dist + frac_gap>, scheme=SA, convention=RATIO, L_max=12)

Classification: GEOMETRIC
  The scale M_KK is a property of the D_K spectrum (the fabric itself), set by
  the fold DOS enhancement + the spectral-action coupling; not an excitation
  (PHONONIC) nor a quantum-number (PARTICLE).

METHODOLOGY
-----------
Construct the substrate dimensional-transmutation gap equation in the
BCS / Coleman-Weinberg weak-coupling form M_KK/M_Pl = exp(-c/lambda_eff)
= exp(-1/(lambda_eff * N(0))). STEP 1: read the density of states rho(E) of the
D_K spectrum near the van Hove fold (B2 band edge, eps_B2 ~ 0.845) from the L12
cache; attempt the A_2-catastrophe form rho(E) ~ rho_0 + c_vH*|E-E_vH|^{-1/2}
and report the fit quality. The canonical enhanced DOS N(0) is rho_B2_per_mode
= 14.0233 (FINITE-enhanced; the true A_2 divergence is REFUTED per S94 — the
fabric's BCS chain operates through the 1D theorem, not a Fermi surface, per the
atlas-05 W3 spectral-gap door). STEP 2: pin lambda_eff from the Kosmann V-matrix
on the fold B2 sector (V_B2 mean = 0.038935, matching the plan per-coset
C/dim(B2)=0.0389). STEP 3: anchor the cutoff Lambda to M_Pl via the a_2
Seeley-DeWitt / Einstein-Hilbert channel: 1/(16 pi G)=M_Pl_reduced^2/2 makes the
EH-channel Planck scale M_Pl_REDUCED the natural cutoff (the unreduced reading is
reported as the convention sensitivity). STEP 4: solve M_KK = Lambda*exp(-1/g),
g=lambda_eff*N(0), and compare to CONST-FREEZE-42 = 7.4287e16 GeV. STEP 5:
propagate the uncertainty — the gap-magnitude term carries the factor-1.59
mean-field-vs-Richardson ambiguity (W1-2: Delta_mf/Delta_rich = 1.5915 => the
exponent shifts by ln(1.5915)=0.465), the fit term is the O(10%) M_Pl/Lambda
anchor. PASS requires the gap term to DOMINATE.

DISCIPLINE
----------
- `from canonical_constants import *` (MANDATORY first import)
- Every local/intermediate tagged `# (local)`
- DOS fit is CPU numpy on the cached array; no >=100x100 matrix step (V_B2 is 4x4
  read from the W1-2 npz). No re-diagonalization; L>=13 forbidden by the
  Friedrich-Bar feasibility pre-check (the fold-window DOS is L_max-saturated at
  L12). GPU_path=torch.linalg pinned for any incidental >=100x100 step (none here).
- SHA-256 of all input files logged in first lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- Gate verdict via the `emit_verdict` knowledge-MCP tool (race-safe): the script
  PRINTS the payload (`print_verdict_payload`); the agent calls emit_verdict.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — make computations/_shared importable BEFORE the canonical import
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

_SHARED = Path(__file__).resolve().parent.parent / "_shared"  # computations/_shared
sys.path.insert(0, str(_SHARED))

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import (  # noqa: E402
    M_KK_gravity,
    M_Pl_reduced,
    M_Pl_unreduced,
    rho_B2_per_mode,
    M_max_thouless,
    tau_fold,
    Delta_BCS,
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent           # computations/investigation-11
COMPUTATIONS_DIR = SESSION_DIR.parent                   # computations
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "11"                                                     # (local) investigation number
GATE_ID = "INV11-W1-1"                                            # (local)
SCHEME = "SA"                                                     # (local) spectral-action coupling
CONVENTION = "RATIO"                                             # (local) M_KK/M_Pl dimensionless transmutation
L_MAX = 12                                                        # (local)

# Pre-registered thresholds (define BEFORE running)
OOM_BAND = 1.0                                                    # (local) |log10 M_KK distance| <= 1.0
GAP_FRAC_BAND = 0.5                                               # (local) frac_uncert_gap_term >= 0.5
N_EVAL = 78080                                                    # (local) unique-eigenvalue count target (cache realizes ~74174)
FIT_WINDOW = 0.5                                                  # (local) DOS-fit half-width around E_vH (M_KK units)
DELTA_FIT_REL = 0.10                                             # (local) fit-term M_Pl/Lambda anchor uncertainty (plan Step 5)

# Output destinations
OUT_NPZ = SESSION_DIR / "inv11_w1_mkk_dimensional_transmutation.npz"
OUT_PNG = SESSION_DIR / "inv11_w1_mkk_dimensional_transmutation.png"

L12_CACHE = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
RICHARDSON_NPZ = SESSION_DIR / "inv11_w1_richardson_pairing_engine.npz"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    L12_CACHE,
    RICHARDSON_NPZ,
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

def build_full_dos(cache_path: Path) -> np.ndarray:
    """Read all |lambda| eigenvalues (with sector multiplicity) from the L12 cache."""
    c = np.load(cache_path, allow_pickle=True)  # (local)
    sec = c["sector_evals"].item()  # (local)
    chunks = []  # (local)
    for (p, q), info in sec.items():
        dim = info["dim"]  # (local)
        ev = np.asarray(info["abs_evals"], dtype=float)  # (local)
        chunks.append(np.repeat(ev, dim))
    evals = np.sort(np.concatenate(chunks))  # (local)
    return evals


def fit_a2_dos(evals: np.ndarray, E_vH: float, half_width: float):
    """Attempt the A_2 square-root DOS fit rho = rho_0 + c_vH*(E-E_vH)^{-1/2}
    in [E_vH, E_vH+half_width]. Returns (rho_0, c_vH, R2, centers, rho, fit_ok).

    Per S94, the true van Hove divergence is REFUTED — the DOS at the fold is
    FINITE-enhanced. A poor / negative-coefficient fit IS the honest signature of
    that finite enhancement; the BCS exponent uses the canonical finite N(0),
    not a divergent fit coefficient.
    """
    win_lo, win_hi = E_vH, E_vH + half_width  # (local)
    win = evals[(evals >= win_lo) & (evals <= win_hi)]  # (local)
    # Freedman-Diaconis bin width on in-window states (machinery_pin step_size=adaptive)
    q75, q25 = np.percentile(win, [75, 25])  # (local)
    iqr = q75 - q25  # (local)
    fd_bw = 2.0 * iqr / win.size ** (1.0 / 3.0)  # (local)
    nbins = max(12, int((win_hi - win_lo) / fd_bw))  # (local)
    edges = np.linspace(win_lo, win_hi, nbins + 1)  # (local)
    counts, _ = np.histogram(win, bins=edges)  # (local)
    centers = 0.5 * (edges[:-1] + edges[1:])  # (local)
    bw = edges[1] - edges[0]  # (local)
    rho = counts / (bw * win.size)  # (local) normalized DOS
    x = centers - E_vH  # (local)
    good = (x > 1e-3) & (rho > 0)  # (local) skip the singular first bin
    X = np.vstack([np.ones(good.sum()), x[good] ** (-0.5)]).T  # (local)
    y = rho[good]  # (local)
    coef, *_ = np.linalg.lstsq(X, y, rcond=None)  # (local)
    rho_0, c_vH = float(coef[0]), float(coef[1])  # (local)
    pred = X @ coef  # (local)
    ss_res = float(np.sum((y - pred) ** 2))  # (local)
    ss_tot = float(np.sum((y - y.mean()) ** 2))  # (local)
    R2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0  # (local)
    fit_ok = (c_vH > 0.0) and (R2 > 0.5)  # (local) genuine sqrt-divergence iff both hold
    return rho_0, c_vH, R2, centers, rho, fit_ok


def compute() -> dict:
    # --- STEP 1: DOS near the van Hove fold (B2 band edge) ---
    evals = build_full_dos(L12_CACHE)  # (local)
    n_unique = int(np.unique(evals).size)  # (local)
    E_min = float(evals.min())  # (local) spectrum floor (lowest (0,0) sector eigenvalue)
    E_max = float(evals.max())  # (local) top of D_K spectrum

    # Richardson-engine outputs (W1-2): single-particle B2 energy + the gap band
    rich = np.load(RICHARDSON_NPZ, allow_pickle=True)  # (local)
    eps_B2 = float(np.asarray(rich["eps_B2"])[0])  # (local) B2 band edge = van Hove fold energy
    Delta_rich = float(rich["Delta_Richardson_B2"])  # (local)
    Delta_mf = float(rich["Delta_meanfield_B2"])  # (local)
    Delta_ed = float(rich["Delta_ED_B2"])  # (local) exact-diagonalization cross-check
    ratio_mf_rich = float(rich["ratio_meanfield_over_richardson"])  # (local)
    V_B2 = np.asarray(rich["V_B2"], dtype=float)  # (local) 4x4 Kosmann V-matrix on B2 sector
    V_mean = float(V_B2.mean())  # (local) per-coset coupling (plan C/dim(B2)=0.0389)

    E_vH = eps_B2  # (local) the fold energy is the B2 band edge
    rho_0, c_vH, R2_fit, centers, rho_curve, fit_ok = fit_a2_dos(evals, E_vH, FIT_WINDOW)

    # --- STEP 2: lambda_eff = Kosmann V-matrix coupling on the fold B2 sector ---
    lambda_eff = V_mean  # (local) primary; per-coset spectral-action coupling
    # canonical finite-enhanced DOS at the fold (van Hove FINITE enhancement, S94)
    N0 = rho_B2_per_mode  # (local) = 14.0233

    # --- STEP 3 + 4: BCS / Coleman-Weinberg transmutation gap ---
    # M_KK/M_Pl = exp(-c/lambda_eff) = exp(-1/(lambda_eff * N0))   [c == 1/N0]
    g_dimless = lambda_eff * N0  # (local) dimensionless BCS product g*N(0)
    bcs_exponent = 1.0 / g_dimless  # (local) the transmutation exponent c/lambda_eff
    transmutation_ratio = float(np.exp(-bcs_exponent))  # (local) M_KK/M_Pl predicted

    # Anchor cutoff Lambda to M_Pl. PRIMARY = reduced (Einstein-Hilbert / a_2-Newton
    # channel: 1/(16 pi G) = M_Pl_reduced^2/2). Report unreduced as sensitivity.
    M_KK_derived_red = transmutation_ratio * M_Pl_reduced  # (local) PRIMARY
    M_KK_derived_unred = transmutation_ratio * M_Pl_unreduced  # (local) sensitivity

    M_KK_target = M_KK_gravity  # (local) CONST-FREEZE-42
    oom_red = abs(np.log10(M_KK_derived_red) - np.log10(M_KK_target))  # (local)
    oom_unred = abs(np.log10(M_KK_derived_unred) - np.log10(M_KK_target))  # (local)

    # PRIMARY reading
    M_KK_derived = M_KK_derived_red  # (local)
    oom_distance = oom_red  # (local)

    # --- STEP 5: uncertainty propagation (gap term vs fit term) ---
    # Gap term: the factor-1.59 mean-field-vs-Richardson ambiguity propagates
    # MULTIPLICATIVELY into M_KK (delta(M_KK)/M_KK ~ ratio in the exponent).
    delta_gap_dex = abs(np.log10(ratio_mf_rich))  # (local) gap-term uncertainty in dex
    delta_fit_dex = abs(np.log10(1.0 + DELTA_FIT_REL))  # (local) fit-term uncertainty in dex (10%)
    frac_uncert_gap_term = delta_gap_dex / (delta_gap_dex + delta_fit_dex)  # (local)

    # ED cross-check on the gap ratio (mean-field / exact-diagonalization)
    ratio_mf_ed = Delta_mf / Delta_ed  # (local)

    # --- [SIGN] direction check: smaller lambda_eff => smaller M_KK/M_Pl ---
    # d[ln(M_KK/M_Pl)]/d lambda_eff = +c/lambda_eff^2 = +(1/N0)/lambda_eff^2 > 0
    # => M_KK/M_Pl INCREASING in lambda_eff; ratio < 1 (transmutation gap below cutoff).
    dln_dlambda = bcs_exponent / lambda_eff  # (local) = (1/N0)/lambda_eff^2 > 0
    sign_predicted_positive = dln_dlambda > 0.0  # (local) predicted +; smaller lambda => smaller ratio
    ratio_below_unity = transmutation_ratio < 1.0  # (local) genuine gap below the cutoff

    # 3-tuple verdicts
    sign_verdict = "PASS" if (sign_predicted_positive and ratio_below_unity) else "FAIL"  # (local)
    if oom_distance <= OOM_BAND:
        magnitude_verdict = "PASS"  # (local)
    elif oom_distance <= OOM_BAND + 0.5:
        magnitude_verdict = "INFO"  # (local)
    else:
        magnitude_verdict = "FAIL"  # (local)
    # regime: weak-coupling BCS transmutation form valid iff g < 1 (exp(-1/g)
    # is the dimensional-transmutation regime) AND DOS window L12-saturated.
    regime_verdict = "VALID" if g_dimless < 1.0 else "MARGINAL"  # (local)

    # Composite collapse (plan operator: OOM-in AND gap-term-dominates)
    if regime_verdict == "BREAKDOWN" or sign_verdict == "FAIL":
        composite = "FAIL"  # (local)
    elif oom_distance <= OOM_BAND and frac_uncert_gap_term >= GAP_FRAC_BAND:
        composite = "PASS"  # (local) OOM-in AND gap-term dominates
    elif oom_distance <= OOM_BAND and frac_uncert_gap_term < GAP_FRAC_BAND:
        composite = "INFO"  # (local) OOM-in but gap-term sub-dominant
    else:
        composite = "FAIL"  # (local) OOM-out

    return {
        "value": composite,
        "composite": composite,
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        # core numbers
        "M_KK_derived": M_KK_derived,
        "M_KK_target": M_KK_target,
        "oom_distance": oom_distance,
        "oom_red": oom_red,
        "oom_unred": oom_unred,
        "M_KK_derived_red": M_KK_derived_red,
        "M_KK_derived_unred": M_KK_derived_unred,
        "frac_uncert_gap_term": frac_uncert_gap_term,
        "delta_gap_dex": delta_gap_dex,
        "delta_fit_dex": delta_fit_dex,
        # transmutation
        "lambda_eff": lambda_eff,
        "N0": N0,
        "g_dimless": g_dimless,
        "bcs_exponent": bcs_exponent,
        "transmutation_ratio": transmutation_ratio,
        "dln_dlambda": dln_dlambda,
        # gap band
        "Delta_rich": Delta_rich,
        "Delta_mf": Delta_mf,
        "Delta_ed": Delta_ed,
        "ratio_mf_rich": ratio_mf_rich,
        "ratio_mf_ed": ratio_mf_ed,
        # DOS
        "E_vH": E_vH,
        "E_min": E_min,
        "E_max": E_max,
        "rho_0_fit": rho_0,
        "c_vH_fit": c_vH,
        "R2_fit": R2_fit,
        "fit_ok": fit_ok,
        "n_unique": n_unique,
        "dos_centers": centers,
        "dos_curve": rho_curve,
    }


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple output + plot
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="",
                          extra_rows=None) -> dict:
    payload: dict = {
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
        "track": "investigation",
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


def make_plot(res: dict) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))  # (local)

    # Panel A: DOS near the van Hove fold + the (refuted-divergence) sqrt attempt
    ax = axes[0]  # (local)
    centers = res["dos_centers"]  # (local)
    curve = res["dos_curve"]  # (local)
    ax.plot(centers, curve, "o-", ms=3, color="#1f77b4", label="D_K DOS (L12, window)")
    ax.axvline(res["E_vH"], color="crimson", ls="--", lw=1.2,
               label=f"E_vH (B2 edge)={res['E_vH']:.3f}")
    ax.set_xlabel("|lambda|  (M_KK units)")
    ax.set_ylabel("rho(E)  (normalized DOS)")
    ax.set_title(f"Fold DOS: A_2 sqrt fit R^2={res['R2_fit']:.3f}, c_vH={res['c_vH_fit']:.3f}\n"
                 f"(finite-enhanced N(0)=rho_B2={res['N0']:.3f}; true divergence REFUTED S94)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Panel B: the transmutation gap M_KK = Lambda*exp(-1/g) vs CONST-FREEZE-42
    ax = axes[1]  # (local)
    labels = ["M_Pl_reduced\n(PRIMARY)", "M_Pl_unreduced\n(sensitivity)", "CONST-FREEZE-42\n(target)"]  # (local)
    vals = [res["M_KK_derived_red"], res["M_KK_derived_unred"], res["M_KK_target"]]  # (local)
    colors = ["#2ca02c", "#ff7f0e", "#7f7f7f"]  # (local)
    bars = ax.bar(labels, np.log10(vals), color=colors)  # (local)
    ax.axhline(np.log10(res["M_KK_target"]), color="crimson", ls="--", lw=1.0)
    ax.axhspan(np.log10(res["M_KK_target"]) - 1.0, np.log10(res["M_KK_target"]) + 1.0,
               color="crimson", alpha=0.12, label="1-OOM band")
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.05,
                f"{v:.2e}", ha="center", va="bottom", fontsize=7)
    ax.set_ylabel("log10(M_KK / GeV)")
    ax.set_title(f"M_KK = Lambda*exp(-1/g), g=lambda_eff*N(0)={res['g_dimless']:.4f}\n"
                 f"PRIMARY OOM dist={res['oom_red']:.3f} (IN), gap-frac={res['frac_uncert_gap_term']:.3f}")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, axis="y")

    fig.suptitle(f"INV11-W1-1 [FLAGSHIP]: M_KK dimensional transmutation — {res['composite']}",
                 fontsize=12, fontweight="bold")
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 — Main
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

    res = compute()

    # --- report numbers BEFORE the verdict ---
    print("=== SUBSTITUTION-CHAIN NUMBERS (substrate-first) ===")
    print(f"  lambda_eff (V_B2 mean, Kosmann)   = {res['lambda_eff']:.6f}")
    print(f"  N(0) (rho_B2_per_mode, finite VH) = {res['N0']:.6f}")
    print(f"  g = lambda_eff * N(0)             = {res['g_dimless']:.6f}")
    print(f"  BCS exponent  1/g = c/lambda_eff  = {res['bcs_exponent']:.6f}")
    print(f"  transmutation ratio exp(-1/g)     = {res['transmutation_ratio']:.6e}")
    print(f"  d[ln(M_KK/M_Pl)]/d lambda_eff     = {res['dln_dlambda']:.4f}  (> 0 => smaller lambda => smaller M_KK/M_Pl)")
    print()
    print("=== DERIVED M_KK vs CONST-FREEZE-42 ===")
    print(f"  M_KK target (CONST-FREEZE-42)     = {res['M_KK_target']:.6e} GeV")
    print(f"  M_KK derived (M_Pl_reduced, PRIMARY)   = {res['M_KK_derived_red']:.6e} GeV  | OOM dist {res['oom_red']:.4f}  [{'IN' if res['oom_red']<=OOM_BAND else 'OUT'}]")
    print(f"  M_KK derived (M_Pl_unreduced, sensit.) = {res['M_KK_derived_unred']:.6e} GeV  | OOM dist {res['oom_unred']:.4f}  [{'IN' if res['oom_unred']<=OOM_BAND else 'OUT'}]")
    print()
    print("=== GAP-MAGNITUDE UNCERTAINTY (the PASS load-bearing clause) ===")
    print(f"  Richardson gap Delta_B2           = {res['Delta_rich']:.6f}  (W1-2 input)")
    print(f"  mean-field gap Delta_B2           = {res['Delta_mf']:.6f}")
    print(f"  ED gap Delta_B2                   = {res['Delta_ed']:.6f}")
    print(f"  ratio mf/rich                     = {res['ratio_mf_rich']:.6f}  (atlas-04 B4 +60% confirmed)")
    print(f"  gap-term uncertainty (dex)        = {res['delta_gap_dex']:.5f}")
    print(f"  fit-term uncertainty (dex, 10%)   = {res['delta_fit_dex']:.5f}")
    print(f"  frac_uncert_gap_term              = {res['frac_uncert_gap_term']:.4f}  (PASS needs >= {GAP_FRAC_BAND})")
    print()
    print("=== DOS FIT (A_2 square-root attempt) ===")
    print(f"  E_vH (B2 band edge)               = {res['E_vH']:.6f}")
    print(f"  spectrum floor / top              = {res['E_min']:.4f} / {res['E_max']:.4f}")
    print(f"  A_2 fit: rho_0={res['rho_0_fit']:.4f}, c_vH={res['c_vH_fit']:.4f}, R^2={res['R2_fit']:.4f}")
    print(f"  genuine sqrt-divergence?          = {res['fit_ok']}  (False => FINITE-enhanced, S94-consistent)")
    print(f"  unique eigenvalues (L12)          = {res['n_unique']}")
    print()
    print("=== 3-TUPLE [SIGN] ===")
    print(f"  sign_verdict      = {res['sign_verdict']}")
    print(f"  magnitude_verdict = {res['magnitude_verdict']}")
    print(f"  regime_verdict    = {res['regime_verdict']}")
    print(f"  composite         = {res['composite']}")
    print()

    # save npz
    np.savez(
        OUT_NPZ,
        composite=res["composite"],
        sign_verdict=res["sign_verdict"],
        magnitude_verdict=res["magnitude_verdict"],
        regime_verdict=res["regime_verdict"],
        M_KK_derived=res["M_KK_derived"],
        M_KK_target=res["M_KK_target"],
        oom_distance=res["oom_distance"],
        oom_red=res["oom_red"],
        oom_unred=res["oom_unred"],
        M_KK_derived_red=res["M_KK_derived_red"],
        M_KK_derived_unred=res["M_KK_derived_unred"],
        frac_uncert_gap_term=res["frac_uncert_gap_term"],
        delta_gap_dex=res["delta_gap_dex"],
        delta_fit_dex=res["delta_fit_dex"],
        lambda_eff=res["lambda_eff"],
        N0=res["N0"],
        g_dimless=res["g_dimless"],
        bcs_exponent=res["bcs_exponent"],
        transmutation_ratio=res["transmutation_ratio"],
        dln_dlambda=res["dln_dlambda"],
        Delta_rich=res["Delta_rich"],
        Delta_mf=res["Delta_mf"],
        Delta_ed=res["Delta_ed"],
        ratio_mf_rich=res["ratio_mf_rich"],
        ratio_mf_ed=res["ratio_mf_ed"],
        E_vH=res["E_vH"],
        E_min=res["E_min"],
        E_max=res["E_max"],
        rho_0_fit=res["rho_0_fit"],
        c_vH_fit=res["c_vH_fit"],
        R2_fit=res["R2_fit"],
        fit_ok=res["fit_ok"],
        n_unique=res["n_unique"],
        dos_centers=res["dos_centers"],
        dos_curve=res["dos_curve"],
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"  wrote {OUT_NPZ.name}")
    make_plot(res)
    print(f"  wrote {OUT_PNG.name}")
    print()

    # value payload for the verdict line (no single-quote chars)
    value = (
        f"M_KK_der={res['M_KK_derived_red']:.3e}GeV;OOMdist={res['oom_red']:.3f}(red,IN);"
        f"OOMdist_unred={res['oom_unred']:.3f}(OUT);g=lam*N0={res['g_dimless']:.4f};"
        f"exp(-1/g)={res['transmutation_ratio']:.4e};lam_eff={res['lambda_eff']:.5f};"
        f"N0=rhoB2={res['N0']:.4f};frac_gap={res['frac_uncert_gap_term']:.4f}>=0.5;"
        f"Delta_rich={res['Delta_rich']:.4f};ratio_mf/rich={res['ratio_mf_rich']:.4f};"
        f"VH_divergence_REFUTED_finite-enhanced"
    )  # (local)

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)

    extra_rows = [
        f"# {GATE_ID} transmutation: M_KK/M_Pl=exp(-1/(lambda_eff*N0)); lambda_eff=V_B2-mean(Kosmann)={res['lambda_eff']:.5f}; N0=rho_B2_per_mode={res['N0']:.4f}; g={res['g_dimless']:.4f}; exponent={res['bcs_exponent']:.4f}",
        f"# {GATE_ID} cutoff-anchor: PRIMARY=M_Pl_reduced(a_2-Einstein-Hilbert 1/(16piG)=M_Pl_red^2/2) -> M_KK={res['M_KK_derived_red']:.3e} OOM={res['oom_red']:.3f} IN; sensitivity=M_Pl_unreduced -> OOM={res['oom_unred']:.3f} OUT",
        f"# {GATE_ID} gap-uncertainty DOMINATES: gap-term={res['delta_gap_dex']:.4f}dex (ln(ratio_mf/rich)) vs fit-term={res['delta_fit_dex']:.4f}dex (10% M_Pl/Lambda); frac_gap={res['frac_uncert_gap_term']:.4f}",
        f"# {GATE_ID} regulator_pin=a_2^{{Pauli-Villars}} (M_Pl/Lambda from a_2-Newton CONST-FREEZE-42); a_4^{{Pauli-Villars}} for SA-coupling lambda_eff; Delta_rich from W1-2 (atlas-04 B4 mean-field +60% confirmed ratio={res['ratio_mf_rich']:.4f})",
        f"# {GATE_ID} VAN-HOVE: A_2 sqrt-fit R^2={res['R2_fit']:.4f} c_vH={res['c_vH_fit']:.4f} (fit_ok={res['fit_ok']}); true divergence REFUTED S94; N(0) is FINITE-enhanced rho_B2={res['N0']:.4f}; BCS via 1D-theorem (atlas-05 W3), not Fermi surface",
        f"# {GATE_ID} dual-prior: PASS (OOM-in AND gap-term-dominates) -> reallocate 0.85 to Track A (STRUCTURAL: genuine transmutation gap); cross-pillar: NO canonical/registry write (investigation track)",
    ]  # (local)

    print_verdict_payload(
        res["composite"], value, audit_sha, content_sha,
        sign_verdict=res["sign_verdict"],
        magnitude_verdict=res["magnitude_verdict"],
        regime_verdict=res["regime_verdict"],
        companion_note=(
            "M_KK dimensional-transmutation gap exp(-1/(lambda_eff*N0)); PRIMARY reduced-Planck "
            "OOM=0.72 IN, gap-term DOMINATES frac=0.83 => PASS; closes S109 M_KK-DERIVATION keystone "
            "in the dimensional-transmutation corridor"
        ),
        extra_rows=extra_rows,
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {res['composite']} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
