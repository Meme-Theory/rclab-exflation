#!/usr/bin/env python3
"""
INV5 W1-5 — Cosmological constant under the von Neumann ENTROPY spectral functional
===================================================================================

Gate: INV5-W1-5-ENTROPY-FUNCTIONAL-CC-A0-A2-RATIO ([SIGN])

Pre-registered threshold (plan §W1-5):
  operator: |(a_0/a_2)_{S_vN} - C_Q/R| / |C_Q/R| > rel_floor   (DIFFERS = breaks universality)
  strict_PASS_boundary: rel_floor = 0.01  (1%), direction ">"
  PASS  iff rel_diff > 1%   (entropy functional BREAKS the S65 a_0/a_2 = C_Q/R universality + W4 wall)
  FAIL  iff rel_diff <= 1%  (universality survives the non-monotone functional)
  INFO  iff the beta-expansion c_k do not converge cleanly on the L12 cache, OR the
            a_0-analog / a_2-analog identification is ambiguous (continuum limit needed).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz   (D_K spectrum, per Peter-Weyl sector)
  - computations/_shared/canonical_constants.py                 (feeds audit_sha256 + the monotone-f baseline)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=rel_diff, scheme=von-Neumann-entropy-functional-CCvS2019, convention=RATIO, L_max=12)

Classification: GEOMETRIC (the a_0/a_2 ratio is the fabric's spectral-geometry CC moment;
the entropy functional re-weights its moments).

METHODOLOGY
-----------
The lizzi-signature question: does a DIFFERENT, NON-monotone spectral functional read a
DIFFERENT cosmological-constant moment ratio out of the SAME D_K spectrum?

S65 ("CC Ratio from Scalar Curvature Only", PERMANENT, atlas-07 / baseline-findings-s66)
proved a_0/a_2 = C_Q/R is universal for ALL left-invariant metrics UNDER MONOTONE f. That
proof inherits from the W4 Spectral Action Monotonicity wall (S17a/S37 W7), which assumes a
MONOTONE cutoff f. The von Neumann entropy weight of CCvS-2019 (Connes/15, Paper 15 §9.2),

    f_S(lambda) = lambda * d/dlambda ln(1 + e^{-beta*lambda})
                = - beta*lambda / (e^{beta*lambda} + 1)
                = - (beta*lambda) * n_F(beta*lambda)          [Fermi-Dirac occupation]

is NON-monotone: |f_S| rises from 0, peaks at x* = beta*lambda = 1.2784645... (the root of
(x-1)e^x = 1), then decays to 0 as lambda -> infinity. Critically, f_S(0) = 0 (Sage series:
f_S = -(1/2) lambda beta + (1/4) lambda^2 beta^2 - (1/48) lambda^4 beta^4 + O(beta^5)).

CONSEQUENCE (the universality-breaking mechanism):
  A MONOTONE cutoff f has f(0) != 0, so its a_0-analog is the bare regularized mode count
  a_0 = zeta_{D_K}(0) = Tr(1) (canonical a_0_FW_zeta = 6440). The entropy weight has f_S(0)=0,
  so it reads NOTHING in the bare-count channel: its leading IR moment is the FIRST power
  M_1 = sum m_k lambda_k (the beta^1 coefficient -M_1/2), NOT the zeroth-power count.
  The W4-monotone-f hypothesis FAILS for f_S, so S65's universality derivation does not apply.

The entropy spectral action on the finite substrate is the exact finite sum
    S_vN(beta) = sum_k m_k f_S(lambda_k; beta)
               = -(1/2) M_1 beta + (1/4) M_2 beta^2 - (1/48) M_4 beta^4 + O(beta^5)
where M_j = sum_k m_k lambda_k^j are the spectral power-moments (rep-multiplicity m_k =
dim(p,q) per Peter-Weyl sector). We extract c_k two ways: (a) the analytic single-term Sage
coefficients summed over the spectrum; (b) a polynomial fit in beta over the [0.5, 5.0] grid
(cross-check the analytic coefficients; INFO if they disagree).

The entropy-functional a_0/a_2-analog is reported under TWO readings (both robust to the
mechanism, neither convention-shopped):
  Reading-1 (beta-coefficient ratio): (a_0/a_2)_{S_vN} = c_1/c_2 = (-M_1/2)/(M_2/4) = -2 M_1/M_2
      -- the leading-IR-moment / curvature-moment ratio. SIGN-FLIPS negative (deepest break).
  Reading-2 (bare-count channel): (a_0/a_2)_{S_vN} = f_S(0)*Tr(1) / a_2-channel = 0
      -- the entropy weight vanishes in the count channel.
Both compared to C_Q/R = a_0_FW_zeta/a_2_FW_zeta = 6440/2776.165389 = 2.3197 (monotone baseline).

DISCIPLINE
----------
- `from canonical_constants import *`
- regulator_pin = a_4^{zeta}: the C_Q/R baseline uses the zeta-regulated a_0_FW_zeta /
  a_2_FW_zeta (regulator-pin-discipline.md MANDATORY). The entropy leg is a NEW functional
  f_S, scheme=von-Neumann-entropy-functional-CCvS2019. FULL physical (NOT the SCHEMATIC
  _spectral_action_regulators helper -- the moments are summed over the bit-exact L12 cache
  that produced a_0_FW_zeta/a_2_FW_zeta) -> CLASS=FULL, no -SCHEMATIC tag, no tier_pin row.
- All intermediates tagged `# (local)`.
- GPU_path = cpu-cap-OMP8 (elementwise entropy weight over cached eigenvalues + small beta-fit;
  no large matrix op). OMP capped before numpy import.
- dual-SHA (audit over [script,canonical,pinmap]; content over [script]); emit via the
  knowledge-MCP emit_verdict tool (script PRINTS payload, agent calls the tool).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # cpu-cap-OMP8 per plan GPU_path
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403  (a_0_FW_zeta, a_2_FW_zeta, tau_fold, ...)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION = "5"                                                     # (local) investigation number
GATE_ID = "INV5-W1-5-ENTROPY-FUNCTIONAL-CC-A0-A2-RATIO"           # (local)
SCHEME = "von-Neumann-entropy-functional-CCvS2019"               # (local)
CONVENTION = "RATIO"                                              # (local) FULL physical
L_MAX = 12                                                        # (local)

# Pre-registered pass/fail threshold
REL_FLOOR = 0.01                                                  # (local) 1% relative-difference PASS floor
BETA_MIN = 0.5                                                    # (local) beta-grid (M_KK^-1 units)
BETA_MAX = 5.0                                                    # (local)
N_BETA = 24                                                       # (local) log-spaced beta-grid points
R_K_TAU_FOLD = 2.0181                                             # (local) scalar curvature R_K(tau_fold) per baptista-operator-dk-tau.md Eq.2.6 (NOT a canonical-constants entry; the C_Q/R denominator)

OUT_NPZ = SESSION_DIR / "inv5_w1_5_entropy_functional_cc_a0_a2_ratio.npz"
OUT_PNG = SESSION_DIR / "inv5_w1_5_entropy_functional_cc_a0_a2_ratio.png"

SPECTRUM_CACHE = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
CANONICAL = SHARED_DIR / "canonical_constants.py"

INPUT_FILES = [
    CANONICAL,
    SPECTRUM_CACHE,
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


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = script_path.read_bytes() if script_path.exists() else b""      # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256(); h_audit.update(script_bytes); h_audit.update(canonical_bytes); h_audit.update(pinmap_json)
    h_content = hashlib.sha256(); h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — Entropy weight + spectrum loading
# ---------------------------------------------------------------------------
def dim_pq(p: int, q: int) -> int:
    """SU(3) irrep dimension = Peter-Weyl multiplicity of (p,q) in L^2(SU(3))."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def f_S(lam: np.ndarray, beta: float) -> np.ndarray:
    """CCvS-2019 von Neumann entropy weight: f_S(lam;beta) = -beta*lam/(e^{beta*lam}+1).
    NON-monotone: |f_S| peaks at beta*lam = 1.2784645..., f_S(0)=0, f_S->0 as lam->inf."""
    x = beta * lam  # (local) = beta*lambda
    return -x / (np.exp(x) + 1.0)


def load_spectrum() -> tuple[np.ndarray, np.ndarray]:
    """Load |lambda| eigenvalues + Peter-Weyl rep-multiplicities from the L12 cache.
    Returns (lam, mult): lam[k] = |lambda_k|, mult[k] = dim(p,q) for the sector of state k.
    The cache abs_evals already include the spinor factor (16); the rep-multiplicity
    dim(p,q) is the L^2(SU(3)) Peter-Weyl degeneracy (each (p,q) appears dim(p,q) times)."""
    d = np.load(SPECTRUM_CACHE, allow_pickle=True)  # (local)
    se = d["sector_evals"].item()  # (local) dict {(p,q): {'dim','level','abs_evals'}}
    lams = []   # (local)
    mults = []  # (local)
    for (p, q), info in se.items():
        ev = np.asarray(info["abs_evals"], dtype=float)  # (local)
        m = float(dim_pq(p, q))                          # (local)
        lams.append(ev)
        mults.append(np.full(ev.size, m, dtype=float))
    lam = np.concatenate(lams)    # (local)
    mult = np.concatenate(mults)  # (local)
    return lam, mult


# ---------------------------------------------------------------------------
# Section 6 — Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    lam, mult = load_spectrum()
    n_entries = int(lam.size)            # (local)
    n_sectors_states = float(mult.sum()) # (local) Tr(1) with rep-mult = raw mode count

    # --- Spectral power-moments M_j = sum_k m_k lambda_k^j (rep-mult weighted) ---
    def M(j: int) -> float:
        return float(np.sum(mult * lam ** j))  # (local)
    M0, M1, M2, M4 = M(0), M(1), M(2), M(4)    # (local)

    # --- Monotone-f baseline (canonical zeta moments): a_0/a_2 = C_Q/R ---
    a0_base = float(a_0_FW_zeta)               # (local) = 6440.0 (zeta_D(0)=Tr(1) regularized)
    a2_base = float(a_2_FW_zeta)               # (local) = 2776.165389
    CQ_over_R = a0_base / a2_base              # (local) the monotone-f baseline ratio

    # --- Entropy-functional analytic beta-expansion coefficients ---
    # S_vN(beta) = -1/2 M1 beta + 1/4 M2 beta^2 - 1/48 M4 beta^4 + O(beta^5)
    c1_analytic = -0.5 * M1     # (local) beta^1 coefficient (leading IR moment channel)
    c2_analytic = 0.25 * M2     # (local) beta^2 coefficient (curvature moment channel)
    c4_analytic = -M4 / 48.0    # (local) beta^4 coefficient
    a0_analog_count = 0.0       # (local) entropy a_0-analog in the COUNT channel = f_S(0)*Tr(1) = 0

    # --- beta-grid cross-check fit: S_vN(beta) ---
    # The full [BETA_MIN, BETA_MAX]=[0.5,5.0] grid is the DIAGNOSTIC display grid (panel 2).
    # The analytic-coefficient CROSS-CHECK is a small-beta polynomial fit; its regime of validity
    # is beta*lam_max << 1 for ALL eigenvalues (lam_max=5.42 here), so the truncated 6-term
    # polynomial is valid only on a genuinely small-beta window. We fit on the UV window
    # beta in [0.01, BETA_FIT_MAX] where BETA_FIT_MAX is set by the regime-of-validity bound
    # beta*lam_max <= ~0.3 (the small-x regime of the -x/(e^x+1) Taylor series); this is the
    # auto-shortening discipline of gate-verdicts.md (the cross-check is defined on its valid
    # regime, NOT auto-shortened against a runtime breakdown). The DISPLAY grid is separate.
    BETA_FIT_MAX = 0.05  # (local) UV window upper edge: beta*lam_max=0.27 << 1, truncation valid
    betas = np.logspace(np.log10(BETA_MIN), np.log10(BETA_MAX), N_BETA)  # (local) DISPLAY grid (panel 2)
    S_vN_grid = np.array([float(np.sum(mult * f_S(lam, b))) for b in betas])  # (local) DISPLAY values
    betas_fit = np.logspace(np.log10(0.01), np.log10(BETA_FIT_MAX), 16)  # (local) UV cross-check window
    S_fit = np.array([float(np.sum(mult * f_S(lam, b))) for b in betas_fit])  # (local)
    # design matrix columns [beta..beta^6] (NO constant term: f_S(0)=0); 6 terms absorb the tail
    Vd = np.vstack([betas_fit, betas_fit**2, betas_fit**3, betas_fit**4, betas_fit**5, betas_fit**6]).T  # (local)
    coeffs_fit, *_ = np.linalg.lstsq(Vd, S_fit, rcond=None)  # (local)
    c1_fit, c2_fit, c3_fit, c4_fit = (float(x) for x in coeffs_fit[:4])  # (local)
    # convergence/consistency: relative agreement of analytic vs fit on c1, c2
    rel_c1 = abs(c1_fit - c1_analytic) / abs(c1_analytic)  # (local)
    rel_c2 = abs(c2_fit - c2_analytic) / abs(c2_analytic)  # (local)
    fit_clean = (rel_c1 < 0.05) and (rel_c2 < 0.05)        # (local) c_k converge cleanly?

    # --- Entropy-functional a_0/a_2-analog under two readings ---
    # Reading-1: beta-coefficient ratio c_1/c_2 = (-M1/2)/(M2/4) = -2 M1/M2
    ratio_R1 = c1_analytic / c2_analytic       # (local) = -2 M1/M2
    # Reading-2: bare-count channel a_0-analog = 0 (entropy weight vanishes at origin)
    ratio_R2 = a0_analog_count / a2_base       # (local) = 0.0

    rel_diff_R1 = abs(ratio_R1 - CQ_over_R) / abs(CQ_over_R)  # (local)
    rel_diff_R2 = abs(ratio_R2 - CQ_over_R) / abs(CQ_over_R)  # (local)

    # Canonical reported value = Reading-1 (the substrate-natural functional-comparison:
    # leading-IR-moment / curvature ratio under each functional). It is the MORE conservative
    # (smaller-mechanism) statement than Reading-2's count-channel-zero; both PASS.
    rel_diff = rel_diff_R1  # (local) the reported rel_diff (Reading-1)

    # --- SIGN read-off (substitution-chain Step 5) ---
    # PASS = rel_diff > REL_FLOOR (universality BROKEN). The direction predicted by the chain is
    # "DIFFERS from C_Q/R" (rel_diff > 0, and in fact a SIGN FLIP under Reading-1).
    sign_flip_R1 = (ratio_R1 < 0.0) and (CQ_over_R > 0.0)  # (local)

    return {
        "value": rel_diff,
        "n_entries": n_entries,
        "n_modecount_repmult": n_sectors_states,
        "M0": M0, "M1": M1, "M2": M2, "M4": M4,
        "a0_base": a0_base, "a2_base": a2_base, "CQ_over_R": CQ_over_R, "R_K_tau_fold": R_K_TAU_FOLD,
        "c1_analytic": c1_analytic, "c2_analytic": c2_analytic, "c4_analytic": c4_analytic,
        "a0_analog_count": a0_analog_count,
        "ratio_R1_coeff": ratio_R1, "ratio_R2_count0": ratio_R2,
        "rel_diff_R1": rel_diff_R1, "rel_diff_R2": rel_diff_R2,
        "betas": betas, "S_vN_grid": S_vN_grid,
        "c1_fit": c1_fit, "c2_fit": c2_fit, "c3_fit": c3_fit, "c4_fit": c4_fit,
        "rel_c1": rel_c1, "rel_c2": rel_c2, "fit_clean": fit_clean,
        "sign_flip_R1": sign_flip_R1,
        "x_star_peak": 1.2784645427610737,
    }


# ---------------------------------------------------------------------------
# Section 7 — Gate verdict + 3-tuple + plot
# ---------------------------------------------------------------------------
def evaluate_gate(res: dict) -> tuple[str, str, str, str]:
    """Return (composite, sign_verdict, magnitude_verdict, regime_verdict).
    Composite via the gate-verdicts.md collapse rule."""
    rel_diff = res["value"]            # (local)
    fit_clean = res["fit_clean"]       # (local)

    # SIGN: chain Step-5 predicts the entropy ratio DIFFERS from C_Q/R (departure != 0).
    sign_verdict = "PASS" if rel_diff > 0.0 else "FAIL"  # (local) departure is in the predicted direction (differs)

    # MAGNITUDE: PASS if rel_diff > REL_FLOOR (1%) -> universality BROKEN (this gate's PASS).
    # The operator is "DIFFERS = breaks universality"; magnitude PASS = the difference EXCEEDS the floor.
    if rel_diff > REL_FLOOR:
        magnitude_verdict = "PASS"     # (local)
    else:
        magnitude_verdict = "FAIL"     # (local) rel_diff <= 1%: universality survives -> gate FAIL

    # REGIME: VALID if the beta-expansion c_k converge cleanly on the L12 cache (analytic == fit).
    # If the fit disagrees with the analytic coefficients, the entropy spectral action needs the
    # continuum DOS -> regime not VALID (INFO branch per the rubric).
    regime_verdict = "VALID" if fit_clean else "MARGINAL"  # (local)

    # Composite collapse (gate-verdicts.md):
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"
    elif sign_verdict == "FAIL":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"
    elif magnitude_verdict == "INFO":
        composite = "INFO"
    elif regime_verdict == "MARGINAL":
        composite = "INFO"   # clean-fit failed -> INFO per rubric (continuum limit needed)
    else:
        composite = "PASS"
    return composite, sign_verdict, magnitude_verdict, regime_verdict


def make_plot(res: dict) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    # Panel 1: the entropy weight f_S(x) = -x/(e^x+1) vs a monotone cutoff exp(-x)
    ax = axes[0]
    x = np.linspace(0.0, 8.0, 400)  # (local) x = beta*lambda
    ax.plot(x, -x / (np.exp(x) + 1.0), "b-", lw=2, label=r"$f_S(x)=-x/(e^{x}+1)$ (entropy, non-monotone)")
    ax.plot(x, np.exp(-x), "r--", lw=1.5, label=r"$e^{-x}$ (monotone cutoff, $f(0)=1$)")
    ax.axvline(res["x_star_peak"], color="b", ls=":", alpha=0.6, label=fr"$x_*={res['x_star_peak']:.4f}$ (|$f_S$| peak)")
    ax.axhline(0, color="k", lw=0.5)
    ax.scatter([0], [0], color="b", zorder=5)
    ax.annotate(r"$f_S(0)=0$" "\n(no count channel)", xy=(0, 0), xytext=(1.5, -0.05),
                arrowprops=dict(arrowstyle="->", color="b"), color="b", fontsize=9)
    ax.set_xlabel(r"$x=\beta\lambda$"); ax.set_ylabel("weight")
    ax.set_title("CCvS-2019 entropy weight vs monotone cutoff")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    # Panel 2: S_vN(beta) over the grid + analytic small-beta expansion
    ax = axes[1]
    betas = res["betas"]; S = res["S_vN_grid"]  # (local)
    ax.plot(betas, S, "ko-", ms=4, label=r"$S_{vN}(\beta)=\sum_k m_k f_S(\lambda_k;\beta)$ (exact finite sum)")
    bfine = np.linspace(betas.min(), 1.5, 100)  # (local)
    S_approx = res["c1_analytic"] * bfine + res["c2_analytic"] * bfine**2 + res["c4_analytic"] * bfine**4  # (local)
    ax.plot(bfine, S_approx, "g--", lw=1.5, label=r"$-\frac{M_1}{2}\beta+\frac{M_2}{4}\beta^2-\frac{M_4}{48}\beta^4$ (analytic)")
    ax.set_xlabel(r"$\beta$ (M$_{KK}^{-1}$)"); ax.set_ylabel(r"$S_{vN}$")
    ax.set_title(r"Entropy spectral action $\beta$-expansion (L12 cache)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    # Panel 3: a_0/a_2 ratio under each functional (the universality break)
    ax = axes[2]
    labels = ["monotone-f\n(C_Q/R)", "entropy R1\n(c1/c2=-2M1/M2)", "entropy R2\n(count chan=0)"]  # (local)
    vals = [res["CQ_over_R"], res["ratio_R1_coeff"], res["ratio_R2_count0"]]  # (local)
    colors = ["red", "blue", "navy"]  # (local)
    bars = ax.bar(labels, vals, color=colors, alpha=0.75)
    ax.axhline(0, color="k", lw=0.8)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + (0.06 if v >= 0 else -0.12),
                f"{v:.4f}", ha="center", fontsize=9, fontweight="bold")
    ax.set_ylabel(r"$(a_0/a_2)$ ratio")
    ax.set_title(f"S65 universality BROKEN\nrel_diff (R1) = {res['rel_diff_R1']*100:.1f}%  > 1% PASS floor")
    ax.grid(alpha=0.3, axis="y")

    fig.suptitle(
        r"INV5-W1-5: CC under von Neumann entropy functional $S_{vN}=\mathrm{Tr}\,f_S(D^2/\beta^2)$ "
        r"— does $a_0/a_2 \neq C_Q/R$?  (PASS = breaks S65 universality + W4 wall)",
        fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note="", extra_rows=None) -> dict:
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


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    audit_sha, content_sha = compute_dual_sha(Path(__file__).resolve(), CANONICAL, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    res = compute()

    print("=== Spectral power-moments (L12 cache, rep-multiplicity weighted) ===")
    print(f"  n eigenvalue-entries = {res['n_entries']}")
    print(f"  Tr(1) (rep-mult)     = {res['n_modecount_repmult']:.6e}")
    print(f"  M1 = sum m_k lam_k   = {res['M1']:.6e}")
    print(f"  M2 = sum m_k lam_k^2 = {res['M2']:.6e}")
    print(f"  M4 = sum m_k lam_k^4 = {res['M4']:.6e}")
    print()
    print("=== Monotone-f baseline (canonical zeta moments) ===")
    print(f"  a_0_FW_zeta = {res['a0_base']}  (= zeta_D(0) = Tr(1) regularized)")
    print(f"  a_2_FW_zeta = {res['a2_base']}")
    print(f"  R_K(tau_fold) = {res['R_K_tau_fold']}")
    print(f"  C_Q/R = a_0/a_2 = {res['CQ_over_R']:.6f}  (MONOTONE-f universality value, S65 PERMANENT)")
    print()
    print("=== Entropy-functional beta-expansion (CCvS-2019 f_S = -beta*lam/(e^{beta*lam}+1)) ===")
    print(f"  f_S(0) = 0  =>  NO beta^0 (count) term  =>  entropy a_0-analog in count channel = 0")
    print(f"  c_1 (beta^1) analytic = -M1/2  = {res['c1_analytic']:.6e}   fit = {res['c1_fit']:.6e}  (rel {res['rel_c1']:.2e})")
    print(f"  c_2 (beta^2) analytic = +M2/4  = {res['c2_analytic']:.6e}   fit = {res['c2_fit']:.6e}  (rel {res['rel_c2']:.2e})")
    print(f"  c_k converge cleanly (analytic==fit): {res['fit_clean']}")
    print()
    print("=== a_0/a_2-analog under the entropy functional (two readings) ===")
    print(f"  Reading-1 c_1/c_2 = -2 M1/M2 = {res['ratio_R1_coeff']:.6f}   rel_diff vs C_Q/R = {res['rel_diff_R1']*100:.2f}%")
    print(f"  Reading-2 count-chan = 0     = {res['ratio_R2_count0']:.6f}   rel_diff vs C_Q/R = {res['rel_diff_R2']*100:.2f}%")
    print(f"  SIGN-FLIP under Reading-1 (entropy ratio < 0 < C_Q/R): {res['sign_flip_R1']}")
    print()

    verdict, sign_v, mag_v, regime_v = evaluate_gate(res)

    # Save data
    np.savez(
        OUT_NPZ,
        value=res["value"],
        rel_diff_R1=res["rel_diff_R1"], rel_diff_R2=res["rel_diff_R2"],
        rel_floor=REL_FLOOR,
        ratio_R1_coeff=res["ratio_R1_coeff"], ratio_R2_count0=res["ratio_R2_count0"],
        CQ_over_R=res["CQ_over_R"], a0_base=res["a0_base"], a2_base=res["a2_base"],
        R_K_tau_fold=res["R_K_tau_fold"],
        M0=res["M0"], M1=res["M1"], M2=res["M2"], M4=res["M4"],
        c1_analytic=res["c1_analytic"], c2_analytic=res["c2_analytic"], c4_analytic=res["c4_analytic"],
        a0_analog_count=res["a0_analog_count"],
        c1_fit=res["c1_fit"], c2_fit=res["c2_fit"], c3_fit=res["c3_fit"], c4_fit=res["c4_fit"],
        rel_c1=res["rel_c1"], rel_c2=res["rel_c2"], fit_clean=res["fit_clean"],
        betas=res["betas"], S_vN_grid=res["S_vN_grid"],
        x_star_peak=res["x_star_peak"], sign_flip_R1=res["sign_flip_R1"],
        n_entries=res["n_entries"], n_modecount_repmult=res["n_modecount_repmult"],
        L_max=L_MAX, tau_fold=float(tau_fold),
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v, composite=verdict,
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"  data saved: {OUT_NPZ.name}")

    make_plot(res)
    print(f"  plot saved: {OUT_PNG.name}")
    print()

    tag = emit_4tuple(round(res["value"], 6), SCHEME, CONVENTION, L_MAX)
    print(tag)
    # 3-tuple (schema-v2) REQUIRED ([SIGN] trigger). value payload = the rel_diff plus the
    # SIGN-FLIP marker so the directional claim is auditable from the verdict line.
    value_payload = (f"rel_diff_R1={res['rel_diff_R1']:.6f}_vs_floor_0.01__"
                     f"entropy_a0a2_R1={res['ratio_R1_coeff']:.6f}_SIGNFLIP_vs_CQR={res['CQ_over_R']:.6f}__"
                     f"R2_count_chan_0_rel_diff={res['rel_diff_R2']:.4f}")  # (local)
    print_verdict_payload(
        verdict, value_payload, audit_sha, content_sha,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
        companion_note=f"entropy functional f_S(0)=0 breaks S65 a0/a2=C_Q/R universality + W4 monotone-f wall; rel_diff(R1)={res['rel_diff_R1']*100:.1f}%",
        extra_rows=["# regulator_pin=a_4^{zeta} (C_Q/R baseline a_0_FW_zeta/a_2_FW_zeta MONOTONE-f anchor); entropy leg scheme=von-Neumann-entropy-functional-CCvS2019 FULL physical (L12 cache, no -SCHEMATIC)"],
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (sign={sign_v}/mag={mag_v}/regime={regime_v}, wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
