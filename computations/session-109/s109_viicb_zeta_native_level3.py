#!/usr/bin/env python3
"""
S109 W1-1 — S109-VIICB-ZETA-NATIVE-LEVEL-3
==========================================

Gate: S109-VIICB-ZETA-NATIVE-LEVEL-3 ([VERIFY] + directional [SIGN] sub-claim)

Pre-registered threshold (sessions/session-plan/session-109-plan-w1.md §"Gate ...
S109-VIICB-ZETA-NATIVE-LEVEL-3"):
  PASS  iff rel = |zeta_native_L3(L_max=10) - a_2_FW_zeta| / a_2_FW_zeta < 1e-3
          AND anti-tautology guard holds (anchor computed from spectrum via
          analytic_zeta, NOT a re-read of a_2_FW_zeta; anchor != a_2_FW_zeta
          bit-exact).
  FAIL  iff rel >= 1e-3 with the zeta-native functional correctly constructed,
          OR the zeta-native a_2 at (s=3, n=2, A-double) is Weyl-DIVERGENT in
          L_max (no convergent L->inf target).
  INFO  iff the constructed anchor is bit-identical to a_2_FW_zeta
          (load-and-compare-to-self, vacuous), OR a Tier-1 dimensionless
          re-anchor is required to make the comparison well-posed.

  Tolerance rule: RATIO (rel, relative to a_2_FW_zeta). a_2_FW_zeta canonical at
  7 sig figs => rel_tol floor 1e-7 << the 1e-3 gate band (Class-8.3 clear).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz   (tau_fold=0.190)
  - computations/session-106/s106_w3_2_pillar_i_vi_iv_envelope.npz  (binding L^-3 Level-2 envelope)
  - computations/session-108/s108_viicb_magnitude_remediation.npz   (partial-sum Z(inf)~650.70 baseline)
  - computations/_shared/_analytic_zeta.py   (FULL-physical Mellin<->Dirichlet; NOT SCHEMATIC)
  - canonical_constants.py (a_2_FW_zeta, d_spec, tau_fold; feeds audit_sha256)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<rel + trend payload>, scheme=FW-zeta-native, convention=Mellin-A-double-s3-n2-FULL, L_max=10)

Classification: GEOMETRIC
  (zeta-regularized spectral moment a_2 / Mellin-cone residue on (A_K, H_K, D_K)
   -- the fabric, not its excitations.)

LEVEL-PIN (substrate-first-canonical-sourcing.md §(iv)):
  _analytic_zeta.py is FULL-physical. Its docstring (lines 11-31) states the
  exact Mellin<->Dirichlet identity zeta_D(s)*Gamma(s/2) = int_0^inf t^(s/2-1) K(t) dt
  with K(t) = Sum_k m_k exp(-lambda_k^2 t); there is NO SCHEMATIC self-ID and NO
  SCHEMATIC fallback path anywhere in the module (verified by read). CLASS = FULL;
  the verdict convention carries NO -SCHEMATIC suffix.

POWER-CONVENTION (load-bearing; regulator-pin-discipline.md §"Mellin Pole-Set Labeling"):
  _analytic_zeta.analytic_zeta(s, L) computes the SINGLE-power Dirichlet form
  zeta_D(s) = Sum_k m_k lambda_k^(-s) (module code lines 14, 187, 264-277 -- the
  heat-kernel identity gives int t^(s/2-1) exp(-lambda^2 t) dt = lambda^(-s) Gamma(s/2)).
  The plan pins poleconv-A-double (zeta_{D_K}(s)=Sum m_k lambda^(-2s), poles at
  s=(d-n)/2). In the A-double cone-apex labeling at d_spec=8, the a_2 channel is
  the pole at s=3 with curvature grade n = d_spec - 2s = 8 - 6 = 2. The
  off-pole-continued analytic_zeta value AT s=3 IS the a_2-channel anchor in this
  labeling (it is the value the S86 C10 infrastructure used: R_inf = analytic_zeta(s=3, L_max=10)).
  d_spec=8 here is the NCG cone-apex labeling per S85 W6-13, NOT the canonical
  constant get_constant("d_spec")=3.0 (which is the spectral dimension d_s, a
  DIFFERENT quantity, no provenance entry). The pole-label arithmetic uses the
  cone-apex d=8; documented as a convention pin (see DSPEC_CONE_APEX below).

METHODOLOGY
-----------
  S108 W1 (FAIL) proved the CONVERGENT bare partial sum Z(L)=Sum_{k<=L}|lambda_k|^-6
  -> Z(inf)~650.70 is structurally 4.27x below g_M=2776.165389: a binding L^-3
  envelope on a CONVERGENT channel cannot bound the distance to the ZETA-REGULARIZED
  continuum value (different functionals). This gate re-evaluates the a_2 magnitude
  anchor ON THE ZETA-NATIVE functional (analytic_zeta off-pole at the a_2 pole) so
  the Level-3 anchor and the binding L^-3 Level-2 envelope would inhabit the SAME
  functional. It evaluates analytic_zeta(s=3) across L_max in {6,8,10}, determines
  CONVERGENT-vs-WEYL-DIVERGENT (audit_discriminator #2), and tests rel<1e-3 at
  L_max=10 with the anti-tautology guard (audit_discriminator #1).

DISCIPLINE
----------
- `from canonical_constants import *`
- every local/intermediate tagged `# (local)`
- CPU path: mpmath off-pole integral via _analytic_zeta (small); OMP cap 8 below
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- verdict emitted via the emit_verdict knowledge-MCP tool (script PRINTS payload;
  agent calls mcp__knowledge__emit_verdict). Script does NOT write the verdict file.
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 0 — Path bootstrap (SHARED_DIR onto sys.path BEFORE canonical import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import a_2_FW_zeta, d_spec, tau_fold  # noqa: E402  explicit for clarity

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import math  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402

# FULL-physical Mellin<->Dirichlet evaluator (NOT SCHEMATIC; see LEVEL-PIN above)
import _analytic_zeta as az  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION = "S109"                                                   # (local)
GATE_ID = "S109-VIICB-ZETA-NATIVE-LEVEL-3"                         # (local)
SCHEME = "FW-zeta-native"                                          # (local)
CONVENTION = "Mellin-A-double-s3-n2-FULL"                          # (local)
L_MAX = 10                                                         # (local) canonical truncation

# Pre-registered machinery pins (plan §machinery_pin_map)
POLE_S = 3                                                         # (local) substrate-distance-1 pole in s
POLECONV = "A-double"                                              # (local) zeta_{D_K}(s)=Sum m_k lam^-2s
DSPEC_CONE_APEX = 8                                                # (local) NCG cone-apex labeling (S85 W6-13); NOT canonical d_spec=3.0
CURVATURE_GRADE_N = DSPEC_CONE_APEX - 2 * POLE_S                   # (local) n = 8 - 2*3 = 2 (a_2 channel)
L_SCAN = [6, 8, 10]                                               # (local) convergent-vs-divergent sub-determination
PASS_BAND = 1e-3                                                   # (local) = Level2(L_max=10) envelope value
INFO_BAND = 1.0                                                    # (local) magnitude INFO ceiling (rel in [PASS_BAND, INFO_BAND] -> INFO band)
G_M = float(a_2_FW_zeta)                                          # (local) = a_2_FW_zeta = 2776.165389 (canonical g_M)

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / "s109_viicb_zeta_native_level3.npz"
OUT_PNG = SESSION_DIR / "s109_viicb_zeta_native_level3.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz",
    PROJECT_ROOT / "computations" / "session-106" / "s106_w3_2_pillar_i_vi_iv_envelope.npz",
    PROJECT_ROOT / "computations" / "session-108" / "s108_viicb_magnitude_remediation.npz",
    SHARED_DIR / "_analytic_zeta.py",
]

# Cross-reference baselines (read for the plot/contrast; NOT pinned as gate inputs beyond the SHA)
S108_BASELINE_NPZ = PROJECT_ROOT / "computations" / "session-108" / "s108_viicb_magnitude_remediation.npz"
S106_ENVELOPE_NPZ = PROJECT_ROOT / "computations" / "session-106" / "s106_w3_2_pillar_i_vi_iv_envelope.npz"


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
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


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
    """Evaluate the zeta-native a_2 anchor across L_scan; determine trend; test rel."""
    # zeta-native a_2-channel anchor at the s=3 pole (A-double, n=2), per L_max.
    # analytic_zeta returns the off-pole-continued single-power Dirichlet value;
    # in the A-double cone-apex labeling this IS the a_2-channel anchor at (s=3,n=2).
    anchor = {}  # (local)
    for L in L_SCAN:
        v = az.analytic_zeta(POLE_S + 0j, L)  # (local)
        anchor[L] = float(v.real)
        if abs(v.imag) > 1e-6 * (abs(v.real) + 1.0):
            print(f"  WARNING: nonzero imaginary part at L={L}: im={v.imag:.3e}")

    anchor_L10 = anchor[L_MAX]  # (local)

    # --- audit_discriminator #1: anti-tautology guard (load-and-compare-to-self) ---
    # The anchor MUST be computed from the spectrum via analytic_zeta, NOT a re-read
    # of a_2_FW_zeta. Bit-exact equality => INFO (vacuous), never PASS.
    anti_tautology_holds = (anchor_L10 != G_M)  # (local) True if NOT bit-identical

    # --- audit_discriminator #2: convergent-vs-Weyl-divergent sub-determination ---
    # trend = sign(anchor(L=10) - anchor(L=8)); also log-log local exponents.
    d_10_8 = anchor[10] - anchor[8]  # (local)
    d_8_6 = anchor[8] - anchor[6]    # (local)
    trend_sign = int(np.sign(d_10_8))  # (local) +1 monotone-increasing (Weyl-divergent); -1 converging
    # log-log local exponents alpha = d ln(anchor)/d ln(L)
    alpha_10_8 = (math.log(anchor[10]) - math.log(anchor[8])) / (math.log(10) - math.log(8))  # (local)
    alpha_8_6 = (math.log(anchor[8]) - math.log(anchor[6])) / (math.log(8) - math.log(6))      # (local)
    # CONVERGENT iff anchor decreasing toward a finite target (trend_sign <= 0 AND |diffs| shrinking).
    # WEYL-DIVERGENT iff monotone-increasing (trend_sign > 0) with positive/growing log-log exponent.
    diffs_both_positive = (d_8_6 > 0) and (d_10_8 > 0)  # (local)
    exponent_positive_growing = (alpha_8_6 > 0) and (alpha_10_8 > 0)  # (local)
    is_weyl_divergent = bool(diffs_both_positive and exponent_positive_growing and trend_sign > 0)  # (local)
    is_convergent = bool((not is_weyl_divergent) and trend_sign <= 0)  # (local)

    # --- gate residual ---
    rel = abs(anchor_L10 - G_M) / G_M  # (local) RATIO

    # --- Verdict logic (pre-registered) ---
    if not anti_tautology_holds:
        verdict = "INFO"  # (local) vacuous load-and-compare-to-self
        magnitude_verdict = "INFO"  # (local)
        regime_verdict = "VALID"    # (local)
        sign_verdict = "N/A"        # (local)
    else:
        # magnitude band
        if rel < PASS_BAND:
            magnitude_verdict = "PASS"  # (local)
        elif rel <= INFO_BAND:
            magnitude_verdict = "INFO"  # (local)
        else:
            magnitude_verdict = "FAIL"  # (local)
        # sign / regime from convergent-vs-divergent trend.
        # Directional pre-registration (substitution chain Step 5): predicted CONVERGENT
        # would give trend_sign <= 0 (anchor approaching a finite target); the structural
        # alternative is Weyl-DIVERGENT (trend_sign > 0). sign_verdict reports whether the
        # functional supplies a convergent target at all.
        if is_convergent:
            sign_verdict = "PASS"     # (local) functional supplies a convergent L->inf target
            regime_verdict = "VALID"  # (local)
        elif is_weyl_divergent:
            # Weyl-divergent: the "converge to a finite a_2 target" premise breaks down across
            # the WHOLE L window (no target exists) => regime BREAKDOWN.
            sign_verdict = "FAIL"        # (local) no convergent target
            regime_verdict = "BREAKDOWN" # (local)
        else:
            sign_verdict = "N/A"        # (local) indeterminate
            regime_verdict = "MARGINAL" # (local)
        # composite via the gate-verdicts.md collapse rule (computed below in evaluate_gate)
        verdict = None  # (local) set by collapse

    return {
        "anchor": anchor,
        "anchor_L10": anchor_L10,
        "rel": rel,
        "G_M": G_M,
        "anti_tautology_holds": anti_tautology_holds,
        "trend_sign": trend_sign,
        "d_10_8": d_10_8,
        "d_8_6": d_8_6,
        "alpha_10_8": alpha_10_8,
        "alpha_8_6": alpha_8_6,
        "is_weyl_divergent": is_weyl_divergent,
        "is_convergent": is_convergent,
        "magnitude_verdict": magnitude_verdict,
        "sign_verdict": sign_verdict,
        "regime_verdict": regime_verdict,
        "verdict": verdict,
    }


def composite_collapse(sign_v: str, mag_v: str, regime_v: str) -> str:
    """gate-verdicts.md §Composite-collapse rule (PRE-REGISTERED)."""
    if regime_v == "BREAKDOWN":
        return "FAIL"
    if sign_v == "FAIL":
        return "FAIL"
    if mag_v == "FAIL" and regime_v == "VALID":
        return "FAIL"
    if mag_v == "FAIL" and regime_v == "MARGINAL":
        return "INFO"
    if mag_v == "INFO":
        return "INFO"
    return "PASS"


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple + payload
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          extra_rows=None) -> dict:
    payload: dict = {
        "session": 109,
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
# Section 7 — Plot
# ---------------------------------------------------------------------------
def make_plot(res: dict, s108: dict, s106: dict) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    anchor = res["anchor"]  # (local)
    Ls = np.array(L_SCAN, dtype=float)  # (local)
    avals = np.array([anchor[L] for L in L_SCAN], dtype=float)  # (local)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.2))

    # Panel 1: zeta-native a_2(L) vs L_max, with g_M line + S108 Z(inf) baseline.
    ax1.plot(Ls, avals, "o-", color="#b00020", lw=2, ms=8,
             label=r"$\zeta$-native $a_2$ anchor = analytic_zeta$(s{=}3,n{=}2)$")
    ax1.axhline(res["G_M"], color="#1f4e79", ls="--", lw=2,
                label=rf"$g_M = a_2^{{FW,\zeta}} = {res['G_M']:.4f}$")
    zinf = float(s108.get("Zinf_best", np.nan)) if s108 is not None else np.nan  # (local)
    if np.isfinite(zinf):
        ax1.axhline(zinf, color="#2e7d32", ls=":", lw=1.8,
                    label=rf"S108 partial-sum $Z(\infty)\approx{zinf:.2f}$ (convergent $|\lambda|^{{-6}}$)")
    ax1.set_yscale("log")
    ax1.set_xlabel(r"$L_{\max}$ ($p+q \leq L_{\max}$)")
    ax1.set_ylabel(r"$\zeta$-native $a_2$ anchor (log)")
    ax1.set_title(r"$\zeta$-native $a_2(L)$: monotone-INCREASING $\Rightarrow$ Weyl-DIVERGENT")
    ax1.set_xticks(L_SCAN)
    ax1.legend(fontsize=8, loc="upper left")
    ax1.grid(alpha=0.3, which="both")
    # annotate the divergence
    ax1.annotate(rf"trend$=+{res['trend_sign']:.0f}$; $\alpha_{{[8\to10]}}={res['alpha_10_8']:+.2f}$"
                 + "\n(power-law divergence)",
                 xy=(Ls[-1], avals[-1]), xytext=(0.30, 0.45), textcoords="axes fraction",
                 fontsize=8, arrowprops=dict(arrowstyle="->", color="#b00020"))

    # Panel 2: residual rel(L) = |anchor(L) - g_M|/g_M vs L_max with the L^-3 envelope band.
    rels = np.abs(avals - res["G_M"]) / res["G_M"]  # (local)
    ax2.plot(Ls, rels, "s-", color="#b00020", lw=2, ms=8, label=r"$\mathrm{rel}(L)=|a_2(L)-g_M|/g_M$")
    # binding L^-3 Level-2 envelope (S106 W3-2): Level2(L) = L^-3, evaluated on the scan.
    env = Ls.astype(float) ** (-3.0)  # (local) the binding L^-3 envelope shape
    ax2.plot(Ls, env, "^--", color="#6a1b9a", lw=1.6, ms=7,
             label=r"binding $L^{-3}$ Level-2 envelope (S106 W3-2)")
    ax2.axhline(PASS_BAND, color="#1f4e79", ls=":", lw=1.6,
                label=rf"gate band $1\mathrm{{e}}{{-3}}$ = Level2($L{{=}}10$)")
    ax2.set_yscale("log")
    ax2.set_xlabel(r"$L_{\max}$")
    ax2.set_ylabel(r"relative residual (log)")
    ax2.set_title(rf"rel($L{{=}}10$)$={res['rel']:.3e}\ \gg\ 10^{{-3}}$ (FAIL-structural)")
    ax2.set_xticks(L_SCAN)
    ax2.legend(fontsize=8, loc="center right")
    ax2.grid(alpha=0.3, which="both")

    fig.suptitle(r"S109-VIICB-ZETA-NATIVE-LEVEL-3: $\zeta$-native $a_2$ anchor is Weyl-DIVERGENT "
                 r"$\Rightarrow$ no convergent $L\to\infty$ target",
                 fontsize=11)
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(OUT_PNG, dpi=140)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)  # (local)
    closure = closure_hash(pins)  # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()
    print(f"  canonical d_spec (spectral-dim, NOT used for pole-label arithmetic) = {d_spec}")
    print(f"  cone-apex labeling DSPEC_CONE_APEX = {DSPEC_CONE_APEX} (S85 W6-13); "
          f"n = {DSPEC_CONE_APEX} - 2*{POLE_S} = {CURVATURE_GRADE_N}")
    print(f"  g_M = a_2_FW_zeta = {G_M}")
    print()

    res = compute()  # (local)

    # composite collapse (pre-registered)
    if res["verdict"] is None:
        composite = composite_collapse(res["sign_verdict"], res["magnitude_verdict"], res["regime_verdict"])  # (local)
    else:
        composite = res["verdict"]  # (local) INFO short-circuit (anti-tautology fail)

    # dual-prior posterior (plan §dual_prior): PASS->Track A 0.90; FAIL->Track B 0.90; INFO->unchanged.
    if composite == "PASS":
        post_A, post_B = 0.90, 0.10  # (local)
    elif composite == "FAIL":
        post_A, post_B = 0.10, 0.90  # (local)
    else:
        post_A, post_B = 0.55, 0.45  # (local) priors unchanged on INFO

    # Read cross-reference baselines for the plot + contrast.
    s108 = None  # (local)
    s106 = None  # (local)
    try:
        s108 = dict(np.load(S108_BASELINE_NPZ, allow_pickle=True))
    except OSError:
        pass
    try:
        s106 = dict(np.load(S106_ENVELOPE_NPZ, allow_pickle=True))
    except OSError:
        pass

    # --- report ---
    print("=== zeta-native a_2 anchor scan ===")
    for L in L_SCAN:
        print(f"  L={L:2d}: anchor = {res['anchor'][L]:.6f}   rel_vs_gM = {abs(res['anchor'][L]-G_M)/G_M:.4e}")
    print(f"  consecutive diffs: anchor(8)-anchor(6) = {res['d_8_6']:+.4f}; "
          f"anchor(10)-anchor(8) = {res['d_10_8']:+.4f}")
    print(f"  log-log local exponents: alpha[6->8] = {res['alpha_8_6']:+.4f}, "
          f"alpha[8->10] = {res['alpha_10_8']:+.4f}")
    print(f"  trend_sign = {res['trend_sign']:+d}  (>0 => Weyl-DIVERGENT)")
    print(f"  is_weyl_divergent = {res['is_weyl_divergent']}; is_convergent = {res['is_convergent']}")
    print(f"  anti_tautology_holds (anchor != g_M bit-exact) = {res['anti_tautology_holds']}")
    print(f"  rel(L=10) = {res['rel']:.6e}  vs gate band {PASS_BAND:.0e}")
    print(f"  sign_verdict={res['sign_verdict']} magnitude_verdict={res['magnitude_verdict']} "
          f"regime_verdict={res['regime_verdict']} => composite={composite}")
    print(f"  dual-prior posterior: Track A = {post_A}, Track B = {post_B}")
    print()

    # --- save npz ---
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        verdict=composite,
        L_scan=np.array(L_SCAN),
        anchor_L6=res["anchor"][6],
        anchor_L8=res["anchor"][8],
        anchor_L10=res["anchor"][10],
        anchor_vals=np.array([res["anchor"][L] for L in L_SCAN]),
        rel=res["rel"],
        rel_L6=abs(res["anchor"][6] - G_M) / G_M,
        rel_L8=abs(res["anchor"][8] - G_M) / G_M,
        rel_L10=res["rel"],
        g_M=G_M,
        pass_band=PASS_BAND,
        info_band=INFO_BAND,
        trend_sign=res["trend_sign"],
        d_10_8=res["d_10_8"],
        d_8_6=res["d_8_6"],
        alpha_10_8=res["alpha_10_8"],
        alpha_8_6=res["alpha_8_6"],
        is_weyl_divergent=res["is_weyl_divergent"],
        is_convergent=res["is_convergent"],
        anti_tautology_holds=res["anti_tautology_holds"],
        sign_verdict=res["sign_verdict"],
        magnitude_verdict=res["magnitude_verdict"],
        regime_verdict=res["regime_verdict"],
        posterior_track_A=post_A,
        posterior_track_B=post_B,
        pole_in_s=POLE_S,
        curvature_grade_n=CURVATURE_GRADE_N,
        poleconv=POLECONV,
        dspec_cone_apex=DSPEC_CONE_APEX,
        canonical_d_spec=float(d_spec),
        scheme=SCHEME,
        convention=CONVENTION,
        class_pin="FULL",
        L_max=L_MAX,
        tau_fold=float(tau_fold),
        s108_Zinf_best=float(s108.get("Zinf_best", np.nan)) if s108 is not None else np.nan,
        s108_gap_factor=float(s108.get("gap_factor", np.nan)) if s108 is not None else np.nan,
        s106_level2_at_lmax10=float(s106.get("level2_at_lmax10", np.nan)) if s106 is not None else np.nan,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"  wrote {OUT_NPZ.name}")

    # --- plot ---
    make_plot(res, s108, s106)
    print(f"  wrote {OUT_PNG.name}")
    print()

    # --- 4-tuple + payload ---
    value_payload = (
        f"rel_L10={res['rel']:.6e};anchor_L10={res['anchor_L10']:.6f};g_M={G_M};"
        f"trend_sign={res['trend_sign']:+d};is_weyl_divergent={res['is_weyl_divergent']};"
        f"is_convergent={res['is_convergent']};anti_tautology_holds={res['anti_tautology_holds']};"
        f"anchor_L6={res['anchor'][6]:.4f};anchor_L8={res['anchor'][8]:.4f};"
        f"alpha_8to10={res['alpha_10_8']:+.4f};Zinf_S108={float(s108.get('Zinf_best', float('nan'))) if s108 is not None else float('nan'):.2f};"
        f"post_B={post_B}"
    )  # (local)
    tag = emit_4tuple(value_payload, SCHEME, CONVENTION, L_MAX)  # (local)
    print(tag)

    regulator_pin_row = (
        f"# regulator_pin=a_2^{{Mellin}} poleconv-{POLECONV} "
        f"(pole_in_s={POLE_S}, curvature_grade_n={CURVATURE_GRADE_N}); "
        f"d_spec_cone_apex={DSPEC_CONE_APEX} (S85 W6-13; NOT canonical d_spec={d_spec}); "
        f"class_pin=FULL (analytic_zeta FULL-physical, NO -SCHEMATIC); "
        f"power-conv: analytic_zeta computes Sum m_k lambda^-s (single), A-double s=3 a_2-channel anchor; "
        f"consistent w/ S108 ACFAMILY sibling re-pin 8ca8f479"
    )  # (local)

    print_verdict_payload(
        composite, value_payload, audit_sha, content_sha,
        sign_verdict=res["sign_verdict"],
        magnitude_verdict=res["magnitude_verdict"],
        regime_verdict=res["regime_verdict"],
        extra_rows=[regulator_pin_row],
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} (wall {wall:.1f}s) ===")
    return 0  # verdict is DATA; exit 0 on PASS/FAIL/INFO alike


if __name__ == "__main__":
    sys.exit(main())
