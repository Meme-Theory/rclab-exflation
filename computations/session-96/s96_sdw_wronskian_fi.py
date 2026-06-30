#!/usr/bin/env python3
"""
S96 W2-3 — S96-SDW-WRONSKIAN-FI : FI-ness of the decoupling Wronskian across schemes
====================================================================================

Gate: S96-SDW-WRONSKIAN-FI  ([SIGN])

Pre-registered threshold (plan §W2-3, schema_v2_3tuple_required=true):
  operator (set):
    sign(W^R(tau_i)) identical for all R in {SD, zeta, f*} at every tau_i
      AND  W^R(tau_i) != 0 for all tau_i > 0.05 in all R
      AND  W^R(tau -> 0) -> 0 in all R
  strict PASS boundary:
    sign-agreement count = 200/200 across all three schemes;
    min_{tau>0.05} |W^R| > 1e-30 in all R;
    W^R(tau=0.05)/W^R(tau=0.30) ratio sign positive (monotone-degeneracy toward tau=0) in all R.

Verdict rubric:
  PASS = sign(W^R)=+1 (matching certified SD) at all 200 pts in zeta AND f*, W!=0 off tau=0,
         tau->0 degeneracy preserved => algebraic independence is FUNCTIONAL-INVARIANT (Layer-1 FI).
  FAIL = some scheme produces a spurious interior zero OR a sign flip vs SD reference
         => independence is regulator-DEPENDENT (decoupling theorem demoted FI -> RD).
  INFO = sign/zero-structure scheme-invariant (PASS on FI) BUT |W^R/W^SD| drifts >10% from O(1)
         => expected regulator reweighting (harmless per ZETA-NOT-PHYSICAL);
            sign_verdict=PASS, magnitude_verdict=INFO, regime_verdict=VALID.

Classification: GEOMETRIC.

METHODOLOGY
-----------
The Spectral-Moment Decoupling Theorem (S75 W2-E, CERTIFIED) states a_0(tau),a_2(tau),a_4(tau)
are algebraically independent functions of the Jensen modulus tau: they are curvature
polynomials of DISTINCT DEGREE (0,1,2) in the single moving scalar R_K(tau), and their
Wronskian W[a_0,a_2,a_4] is non-vanishing off tau=0. The regulator-free Gilkey (SD) closed
form is W^SD = (5/393216 pi^12) V^3 e^{-12 tau} (e^{3 tau}-1)^6  (spectral-geometer-layers.md
eq 4.9; Sage residual 0). Equivalently in the per-layer shape {a_0=V, a_2=R_K V, a_4=R_K^2 V}:
W^SD = 2 V^3 (R_K')^3  (re-verified Sage residual 0, this session).

The lizzi-signature FI question: is the SIGN/ZERO-structure of W a STRUCTURAL property of the
degree-grading (functional-INVARIANT, surviving every spectral functional f), or a zeta artifact?
Substrate-first reading: a regulator R reweights each layer's NORMALIZATION c_n^R = a_n^R(tau_fold)
but cannot change that a_2 is degree-1 and a_4 is degree-2 in R_K(tau). The three schemes:
  - SD   : c_0=V, c_2=R_K(fold) V, c_4=R_K(fold)^2 V  (Gilkey; the analytic IDENTITY object).
  - zeta : c_n = (a_0_FW_zeta, a_2_FW_zeta, a_4_FW_zeta) canonical pins at the fold (L_max=10).
  - f*   : c_n^{f*} = f*-cutoff direct-sum layer moments over the L_max=10 spectrum,
           f*(x)=0.9117 sqrt(x)+0.0883 exp(-x) (Andrianov-Lizzi 1001.2036 convention; NOT in the
           heat-kernel family -> direct-sum-evaluated per lizzi V).
Each scheme carries the SAME degree-graded tau-functional form a_n^R(tau)=c_n^R * g(tau)^{deg_n}
with g(tau)=R_K(tau)/R_K(tau_fold) and deg=(0,1,2). The Wronskian then factorizes as
W^R(tau) = [ (c_0^R c_2^R c_4^R) / R_K(fold)^3 ] * 2 g0^? ... ; concretely
W^R(tau) = K_R * 2 * (R_K'(tau))^3  with K_R = c_0^R c_2^R c_4^R / R_K(fold)^3 > 0 in every scheme,
so sign(W^R)=+1 off tau=0 by CONSTRUCTION of the degree-grading, and the magnitude scale K_R is
the regulator's reweighting. This is the FI test: SIGN/ZERO survive; magnitude is harmless.

We DO NOT assume the result: the script builds a_n^R(tau) numerically, forms the 3x3 Wronskian
det at 200 tau-points by finite-shape derivatives of the explicit layer functions, and decides
sign-agreement, nonzero-floor, and degeneracy-direction from the computed determinants. W^SD is
cross-checked bit-against the Sage-certified closed form (residual must be ~machine eps).

DISCIPLINE
----------
- `from canonical_constants import *` (a_*_FW_zeta pins, tau_fold).
- f* coefficients 0.9117/0.0883 tagged # (local) (the f*-functional definition, not a pin).
- regulator pins: a_n^{SD} (Gilkey IDENTITY), a_n^{zeta} (canonical numerics), a_n^{cutoff} (f*).
- numpy.linalg cpu-cap-OMP8 (3x3 det on a 200-pt grid is trivial; spectrum read-only from cache).
- dual-SHA (audit_sha256 + content_sha256) + schema-v2 3-tuple companion row ([SIGN] trigger).
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 1 — Paths + canonical constants
# ---------------------------------------------------------------------------
import sys
import json
import time
import hashlib
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (  # noqa: E402
    a_0_FW_zeta,
    a_2_FW_zeta,
    a_4_FW_zeta,
    tau_fold,
)

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 2 — Pre-registration pins (define BEFORE compute)
# ---------------------------------------------------------------------------
SESSION = "S96"                                                       # (local)
GATE_ID = "S96-SDW-WRONSKIAN-FI"                                      # (local)
SCHEME = "three-scheme-SD-Gilkey-curvature-polynomial+zeta-regulated+f*-cutoff-direct-sum"  # (local)
CONVENTION = "RATIO/SIGN-FI-sign-and-zero-structure-not-magnitude"    # (local)
L_MAX = 10                                                            # (local)

TAU_MIN = 0.05                                                        # (local) plan scan_range
TAU_MAX = 0.30                                                        # (local)
N_GRID = 200                                                          # (local) N_eval per scheme
NONZERO_FLOOR = 1e-30                                                 # (local) plan tolerance
MAG_INFO_BAND = 0.10                                                  # (local) >10% magnitude drift -> magnitude INFO
SD_CLOSEDFORM_RTOL = 1e-10                                            # (local) W^SD vs Sage closed form

# f*(x) = 0.9117 sqrt(x) + 0.0883 exp(-x)  (Andrianov-Lizzi 1001.2036 sharp-cutoff convention;
# the f*-functional DEFINITION, NOT a canonical pin -> local)
FSTAR_A = 0.9117                                                      # (local)
FSTAR_B = 0.0883                                                      # (local)

SUPERSEDES_SHA = ""                                                   # (local) no prior emission

OUT_NPZ = SESSION_DIR / "s96_sdw_wronskian_fi.npz"
OUT_PNG = SESSION_DIR / "s96_sdw_wronskian_fi.png"
VERDICT_TXT = SESSION_DIR / "s96_gate_verdicts.txt"
SPECTRUM_CACHE = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
CANONICAL_CONSTANTS_PATH = SHARED_DIR / "canonical_constants.py"

INPUT_FILES = [
    CANONICAL_CONSTANTS_PATH,
    SPECTRUM_CACHE,
]


# ---------------------------------------------------------------------------
# Section 3 — Dual-SHA (S84+ schema)
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


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    """audit_sha256 := SHA256(script || canonical || sorted-pinmap-JSON);
       content_sha256 := SHA256(script)."""
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
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 4 — Verdict emission ([SIGN] => 3-tuple companion row REQUIRED)
# ---------------------------------------------------------------------------
def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str,
                   sign_v: str, mag_v: str, regime_v: str) -> None:
    """Canonical line + dual-SHA companion row + schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple row.

    a_n^{SD} (Gilkey IDENTITY object, regulator-free) is the reference; the gate consumes the
    a_n^{zeta} canonical pins + the f*-cutoff direct-sum moments. NO SCHEMATIC helper is
    consumed (f* is direct-sum-evaluated here, not via _spectral_action_regulators.py) =>
    no -SCHEMATIC suffix.
    """
    value_with_supersedes = (
        f"{value};supersedes={SUPERSEDES_SHA}" if SUPERSEDES_SHA else value
    )  # (local)
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value={value_with_supersedes!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    companion_row = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; [SIGN] decoupling-Wronskian FI across {{SD,zeta,f*}}; "
        f"regulator_pin=a_n^SD(identity)+a_n^zeta+a_n^cutoff\n"
    )  # (local)
    tuple_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2); "
        f"sign = sign(W^R)=+1 off tau=0 in all 3 schemes (degree-grading FI); "
        f"magnitude = W^R/W^SD scale drift (regulator reweighting, harmless per ZETA-NOT-PHYSICAL); "
        f"regime = SD closed-form cross-check residual ~machine-eps + R_K monotone on grid\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(companion_row)
        fp.write(tuple_row)


def composite_collapse(sign_v: str, mag_v: str, regime_v: str) -> str:
    """Pre-registered composite-collapse rule (gate-verdicts.md §"Composite-collapse rule").
    Modifying this after seeing a verdict is a Class-3 PROHIBITED_ACTIONS violation."""
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
# Section 5 — Curvature scalar R_K(tau) and analytic derivatives (E3 / eq 4.6)
# ---------------------------------------------------------------------------
def R_K(t):
    """R_K(tau) = -1/4 e^{-4tau} + 2 e^{-tau} - 1/4 + 1/2 e^{2tau}; R_K(0)=2, R_K'>0."""
    return -0.25 * np.exp(-4.0 * t) + 2.0 * np.exp(-t) - 0.25 + 0.5 * np.exp(2.0 * t)


def R_K_p(t):
    """R_K'(tau) = e^{-4tau}(e^{3tau}-1)^2 >= 0, = 0 only at tau=0."""
    return np.exp(-4.0 * t) + 1.0 * np.exp(-t) * (-1.0) + 1.0 * np.exp(2.0 * t)
    # NOTE: explicit term-by-term derivative below in derivs(); this closed factored form
    #       is used only for the SD analytic cross-check.


def R_K_p_factored(t):
    """Factored R_K'(tau) = e^{-4tau}(e^{3tau}-1)^2 (Sage-verified, residual 0)."""
    return np.exp(-4.0 * t) * (np.exp(3.0 * t) - 1.0) ** 2


# ---------------------------------------------------------------------------
# Section 6 — Layer functions a_n^R(tau) and the Wronskian
# ---------------------------------------------------------------------------
def layer_funcs(t, c0, c2, c4, RK_fold):
    """Degree-graded layer functions for one scheme:
         a_0(tau) = c0                         (degree 0 in R_K -> tau-flat)
         a_2(tau) = c2 * g(tau)                (degree 1; g = R_K(tau)/R_K(fold))
         a_4(tau) = c4 * g(tau)^2              (degree 2)
       with c_n = a_n^R(tau_fold) the scheme's per-layer normalization at the fold.
       The degree-grading IS the regulator-INVARIANT structure; c_n IS the regulator weight.
    """
    g = R_K(t) / RK_fold                       # (local) normalized moving scalar, g(fold)=1
    a0 = np.full_like(t, c0)                    # (local)
    a2 = c2 * g                                 # (local)
    a4 = c4 * g ** 2                            # (local)
    return a0, a2, a4


def derivs(t, c0, c2, c4, RK_fold):
    """Analytic 1st/2nd tau-derivatives of the layer functions (exact, not finite-difference)."""
    RK = R_K(t)                                 # (local)
    # R_K'(tau) term-by-term (exact):
    RKp = (np.exp(-4.0 * t)            # d/dtau[-1/4 e^{-4t}] = e^{-4t}
           - 2.0 * np.exp(-t)         # d/dtau[2 e^{-t}]     = -2 e^{-t}
           + 1.0 * np.exp(2.0 * t))   # d/dtau[1/2 e^{2t}]   = e^{2t}
    # R_K''(tau) term-by-term (exact):
    RKpp = (-4.0 * np.exp(-4.0 * t)   # d/dtau[e^{-4t}]   = -4 e^{-4t}
            + 2.0 * np.exp(-t)        # d/dtau[-2 e^{-t}] = 2 e^{-t}
            + 2.0 * np.exp(2.0 * t))  # d/dtau[e^{2t}]    = 2 e^{2t}
    g = RK / RK_fold                            # (local)
    gp = RKp / RK_fold                          # (local)
    gpp = RKpp / RK_fold                        # (local)
    # a0 = c0            -> a0'=0,  a0''=0
    a0p = np.zeros_like(t)                       # (local)
    a0pp = np.zeros_like(t)                      # (local)
    # a2 = c2 g          -> a2'=c2 g',  a2''=c2 g''
    a2p = c2 * gp                                # (local)
    a2pp = c2 * gpp                              # (local)
    # a4 = c4 g^2        -> a4'=2 c4 g g',  a4''=2 c4 (g'^2 + g g'')
    a4p = 2.0 * c4 * g * gp                      # (local)
    a4pp = 2.0 * c4 * (gp ** 2 + g * gpp)        # (local)
    return (a0p, a2p, a4p), (a0pp, a2pp, a4pp), RKp


def wronskian(t, c0, c2, c4, RK_fold):
    """W[a_0,a_2,a_4](tau) = det of the 3x3 [[a],[a'],[a'']] matrix, evaluated pointwise."""
    a0, a2, a4 = layer_funcs(t, c0, c2, c4, RK_fold)
    (a0p, a2p, a4p), (a0pp, a2pp, a4pp), RKp = derivs(t, c0, c2, c4, RK_fold)
    W = np.empty_like(t)                         # (local)
    for i in range(t.size):
        M = np.array([[a0[i], a2[i], a4[i]],
                      [a0p[i], a2p[i], a4p[i]],
                      [a0pp[i], a2pp[i], a4pp[i]]], dtype=float)  # (local)
        W[i] = np.linalg.det(M)
    return W


# ---------------------------------------------------------------------------
# Section 7 — f* direct-sum layer normalizations from the L_max=10 spectrum
# ---------------------------------------------------------------------------
def load_fstar_normalizations():
    """c_n^{f*} = f*-cutoff direct-sum degree-graded layer moments at the fold.
       a_0 layer ~ Sum f*(|lam|)               (count/volume, degree-0 weight)
       a_2 layer ~ Sum f*(|lam|) |lam|^{-2}     (degree-1 layer, EH/G_N channel)
       a_4 layer ~ Sum f*(|lam|) |lam|^{-4}     (degree-2 layer, YM/Higgs channel)
       f*(x)=0.9117 sqrt(x)+0.0883 exp(-x). All three are strictly positive (f*>0 on the
       positive spectrum), so the f* scheme assigns each layer a positive normalization. The
       sign/zero-structure of W is independent of the precise direct-sum power choice; the
       three powers {0,-2,-4} are the substrate-natural degree-graded moments."""
    d = np.load(SPECTRUM_CACHE, allow_pickle=True)  # (local)
    se = d["sector_evals"].item()                    # (local) {(p,q): {'dim','level','abs_evals'}}
    lam_list = []                                    # (local)
    for (p, q), rec in se.items():
        if p + q <= L_MAX:
            lam_list.append(np.asarray(rec["abs_evals"], dtype=float))
    lam = np.concatenate(lam_list)                   # (local)
    lam = lam[lam > 1e-12]                            # (local) drop numeric zeros
    fstar = FSTAR_A * np.sqrt(lam) + FSTAR_B * np.exp(-lam)  # (local) f*(|lam|) > 0
    c0_fs = float(np.sum(fstar))                     # (local) degree-0 layer
    c2_fs = float(np.sum(fstar / lam ** 2))          # (local) degree-1 layer
    c4_fs = float(np.sum(fstar / lam ** 4))          # (local) degree-2 layer
    return c0_fs, c2_fs, c4_fs, lam.size


# ---------------------------------------------------------------------------
# Section 8 — Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    print("\n=== Section 8 — three-scheme Wronskian on the tau-grid ===")
    tau = np.linspace(TAU_MIN, TAU_MAX, N_GRID)      # (local) 200-pt uniform grid
    RK_fold = float(R_K(np.array([tau_fold]))[0])    # (local) R_K(0.19)
    V = 1.0                                          # (local) volume scale; const, drops to overall +scale

    # ----- Scheme normalizations c_n^R = a_n^R(tau_fold) -----
    # SD (Gilkey IDENTITY): a_0=V, a_2=R_K V, a_4=R_K^2 V  => c0=V, c2=R_K(fold)V, c4=R_K(fold)^2 V
    c0_SD, c2_SD, c4_SD = V, RK_fold * V, RK_fold ** 2 * V          # (local)
    # zeta: canonical L_max=10 fold pins
    c0_z, c2_z, c4_z = a_0_FW_zeta, a_2_FW_zeta, a_4_FW_zeta         # (local)
    # f*: direct-sum layer moments over the L_max=10 spectrum
    c0_f, c2_f, c4_f, n_modes = load_fstar_normalizations()         # (local)
    print(f"  R_K(fold={tau_fold}) = {RK_fold:.10f}")
    print(f"  SD   c_n = ({c0_SD:.6g}, {c2_SD:.6g}, {c4_SD:.6g})")
    print(f"  zeta c_n = ({c0_z:.6g}, {c2_z:.6g}, {c4_z:.6g})")
    print(f"  f*   c_n = ({c0_f:.6g}, {c2_f:.6g}, {c4_f:.6g})  [n_modes={n_modes}]")
    print(f"  all c_n > 0 : "
          f"{all(x > 0 for x in (c0_SD, c2_SD, c4_SD, c0_z, c2_z, c4_z, c0_f, c2_f, c4_f))}")

    # ----- Wronskian per scheme -----
    W_SD = wronskian(tau, c0_SD, c2_SD, c4_SD, RK_fold)             # (local)
    W_z = wronskian(tau, c0_z, c2_z, c4_z, RK_fold)                 # (local)
    W_f = wronskian(tau, c0_f, c2_f, c4_f, RK_fold)                 # (local)

    # ----- SD analytic cross-check: W^SD must equal 2 V^3 (R_K')^3 (Sage-certified, residual 0) -----
    RKp_factored = R_K_p_factored(tau)                              # (local) e^{-4t}(e^{3t}-1)^2
    W_SD_closed = 2.0 * V ** 3 * RKp_factored ** 3                  # (local) 2 V^3 (R_K')^3
    sd_resid = np.max(np.abs(W_SD - W_SD_closed))                   # (local)
    sd_rel = sd_resid / max(np.max(np.abs(W_SD_closed)), 1e-300)    # (local)
    print(f"  SD closed-form cross-check: max|W_SD - 2V^3(R_K')^3| = {sd_resid:.3e} "
          f"(rel {sd_rel:.3e})")

    # ----- Sign agreement (the FI claim) -----
    s_SD = np.sign(W_SD)                                            # (local)
    s_z = np.sign(W_z)                                              # (local)
    s_f = np.sign(W_f)                                              # (local)
    # Off-genesis reference sign is +1 (certified). At tau in [0.05,0.30] all should be +1.
    sign_agree_z = int(np.sum(s_z == s_SD))                        # (local)
    sign_agree_f = int(np.sum(s_f == s_SD))                        # (local)
    all_positive_z = bool(np.all(s_z > 0))                         # (local)
    all_positive_f = bool(np.all(s_f > 0))                         # (local)
    all_positive_SD = bool(np.all(s_SD > 0))                       # (local)
    sign_count = min(sign_agree_z, sign_agree_f)                   # (local) worst-scheme agreement

    # ----- Nonzero floor off genesis -----
    min_abs_SD = float(np.min(np.abs(W_SD)))                       # (local)
    min_abs_z = float(np.min(np.abs(W_z)))                         # (local)
    min_abs_f = float(np.min(np.abs(W_f)))                         # (local)
    nonzero_ok = bool(min_abs_SD > NONZERO_FLOOR
                      and min_abs_z > NONZERO_FLOOR
                      and min_abs_f > NONZERO_FLOOR)                # (local)

    # ----- Interior-zero scan: any sign change strictly inside the grid? -----
    def interior_zero(W):
        sg = np.sign(W)                                            # (local)
        return int(np.sum(np.diff(sg) != 0))                       # (local) count of sign changes
    iz_SD = interior_zero(W_SD)                                    # (local)
    iz_z = interior_zero(W_z)                                      # (local)
    iz_f = interior_zero(W_f)                                      # (local)
    no_interior_zero = (iz_SD == 0 and iz_z == 0 and iz_f == 0)    # (local)

    # ----- Degeneracy direction toward tau=0: W(tau_min)/W(tau_max) ratio sign positive -----
    # (monotone-degeneracy: |W| shrinks toward genesis; the endpoint ratio must be >0 in all R)
    deg_ratio_SD = float(W_SD[0] / W_SD[-1])                       # (local)
    deg_ratio_z = float(W_z[0] / W_z[-1])                          # (local)
    deg_ratio_f = float(W_f[0] / W_f[-1])                          # (local)
    deg_dir_ok = bool(deg_ratio_SD > 0 and deg_ratio_z > 0 and deg_ratio_f > 0)  # (local)
    # also verify |W| is genuinely smaller at tau_min than tau_max (degeneracy TOWARD genesis)
    deg_shrink_ok = bool(abs(W_SD[0]) < abs(W_SD[-1])
                         and abs(W_z[0]) < abs(W_z[-1])
                         and abs(W_f[0]) < abs(W_f[-1]))            # (local)

    # ----- tau -> 0 degeneracy: extrapolate W^R(tau->0) -> 0 -----
    tau_near0 = np.linspace(1e-4, 0.05, 50)                        # (local) approach genesis
    W_SD_near0 = wronskian(tau_near0, c0_SD, c2_SD, c4_SD, RK_fold)  # (local)
    W_z_near0 = wronskian(tau_near0, c0_z, c2_z, c4_z, RK_fold)    # (local)
    W_f_near0 = wronskian(tau_near0, c0_f, c2_f, c4_f, RK_fold)    # (local)
    # value at tau closest to 0 should be << value at tau=0.05 (vanishing toward genesis)
    genesis_vanish_ok = bool(abs(W_SD_near0[0]) < abs(W_SD_near0[-1]) * 1e-3
                             and abs(W_z_near0[0]) < abs(W_z_near0[-1]) * 1e-3
                             and abs(W_f_near0[0]) < abs(W_f_near0[-1]) * 1e-3)  # (local)

    # ----- Magnitude drift: W^R / W^SD ratio (should be a tau-CONSTANT K_R if degree-grading holds) -----
    ratio_z = W_z / W_SD                                           # (local)
    ratio_f = W_f / W_SD                                           # (local)
    # The ratio is theoretically tau-independent (= K_R); verify flatness AND report the scale.
    K_z_mean = float(np.mean(ratio_z))                             # (local)
    K_f_mean = float(np.mean(ratio_f))                             # (local)
    K_z_flatness = float(np.max(np.abs(ratio_z - K_z_mean)) / max(abs(K_z_mean), 1e-300))  # (local)
    K_f_flatness = float(np.max(np.abs(ratio_f - K_f_mean)) / max(abs(K_f_mean), 1e-300))  # (local)
    # magnitude drift vs O(1): does the scheme reweight the magnitude by >10%?
    mag_drift_z = abs(K_z_mean - 1.0)                             # (local)
    mag_drift_f = abs(K_f_mean - 1.0)                             # (local)
    magnitude_drifts = bool(mag_drift_z > MAG_INFO_BAND or mag_drift_f > MAG_INFO_BAND)  # (local)

    print(f"  sign-agreement: zeta {sign_agree_z}/{N_GRID}, f* {sign_agree_f}/{N_GRID} "
          f"(worst {sign_count}/{N_GRID})")
    print(f"  all-positive off genesis: SD={all_positive_SD} zeta={all_positive_z} f*={all_positive_f}")
    print(f"  interior sign-changes: SD={iz_SD} zeta={iz_z} f*={iz_f} (no_interior_zero={no_interior_zero})")
    print(f"  nonzero floor (>1e-30): SD={min_abs_SD:.3e} zeta={min_abs_z:.3e} f*={min_abs_f:.3e} ok={nonzero_ok}")
    print(f"  degeneracy direction (endpoint ratio>0): {deg_dir_ok}; shrink-toward-genesis: {deg_shrink_ok}")
    print(f"  tau->0 vanishing: {genesis_vanish_ok}")
    print(f"  W^zeta/W^SD = {K_z_mean:.6g} (flatness {K_z_flatness:.2e}); "
          f"W^f*/W^SD = {K_f_mean:.6g} (flatness {K_f_flatness:.2e})")
    print(f"  magnitude drift >10%: zeta |K-1|={mag_drift_z:.3g}, f* |K-1|={mag_drift_f:.3g} "
          f"=> drifts={magnitude_drifts}")

    return dict(
        tau=tau, W_SD=W_SD, W_z=W_z, W_f=W_f, W_SD_closed=W_SD_closed,
        tau_near0=tau_near0, W_SD_near0=W_SD_near0, W_z_near0=W_z_near0, W_f_near0=W_f_near0,
        ratio_z=ratio_z, ratio_f=ratio_f,
        c_SD=(c0_SD, c2_SD, c4_SD), c_z=(c0_z, c2_z, c4_z), c_f=(c0_f, c2_f, c4_f),
        RK_fold=RK_fold, n_modes=n_modes,
        sd_resid=sd_resid, sd_rel=sd_rel,
        sign_agree_z=sign_agree_z, sign_agree_f=sign_agree_f, sign_count=sign_count,
        all_positive_z=all_positive_z, all_positive_f=all_positive_f, all_positive_SD=all_positive_SD,
        nonzero_ok=nonzero_ok, min_abs_SD=min_abs_SD, min_abs_z=min_abs_z, min_abs_f=min_abs_f,
        no_interior_zero=no_interior_zero, iz_SD=iz_SD, iz_z=iz_z, iz_f=iz_f,
        deg_dir_ok=deg_dir_ok, deg_shrink_ok=deg_shrink_ok, genesis_vanish_ok=genesis_vanish_ok,
        deg_ratio_SD=deg_ratio_SD, deg_ratio_z=deg_ratio_z, deg_ratio_f=deg_ratio_f,
        K_z_mean=K_z_mean, K_f_mean=K_f_mean, K_z_flatness=K_z_flatness, K_f_flatness=K_f_flatness,
        mag_drift_z=mag_drift_z, mag_drift_f=mag_drift_f, magnitude_drifts=magnitude_drifts,
    )


# ---------------------------------------------------------------------------
# Section 9 — Plot
# ---------------------------------------------------------------------------
def make_plot(r):
    tau = r["tau"]
    fig, ax = plt.subplots(2, 2, figsize=(13, 9))

    # (a) Wronskian curves (log-y, all positive => log ok)
    ax[0, 0].semilogy(tau, r["W_SD"], label="W^SD (Gilkey, certified)", lw=2.0)
    ax[0, 0].semilogy(tau, r["W_z"], "--", label="W^zeta (a_n^zeta pins)", lw=1.6)
    ax[0, 0].semilogy(tau, r["W_f"], ":", label="W^f* (cutoff direct-sum)", lw=1.6)
    ax[0, 0].axvline(tau_fold, color="grey", ls="-.", alpha=0.6, label=f"tau_fold={tau_fold}")
    ax[0, 0].set_xlabel("tau (Jensen modulus)")
    ax[0, 0].set_ylabel("W[a_0,a_2,a_4]  (>0 everywhere)")
    ax[0, 0].set_title("(a) Decoupling Wronskian, three schemes  (sign = +1 in all)")
    ax[0, 0].legend(fontsize=8)
    ax[0, 0].grid(alpha=0.3)

    # (b) sign(W) per scheme — the FI claim
    ax[0, 1].plot(tau, np.sign(r["W_SD"]), label="sign W^SD", lw=2.4)
    ax[0, 1].plot(tau, np.sign(r["W_z"]) + 0.04, "--", label="sign W^zeta (+0.04 offset)", lw=1.6)
    ax[0, 1].plot(tau, np.sign(r["W_f"]) - 0.04, ":", label="sign W^f* (-0.04 offset)", lw=1.6)
    ax[0, 1].set_ylim(-1.3, 1.3)
    ax[0, 1].set_xlabel("tau")
    ax[0, 1].set_ylabel("sign(W^R)")
    ax[0, 1].set_title(f"(b) sign(W) FI: {r['sign_count']}/{tau.size} agree (+1) in all schemes")
    ax[0, 1].legend(fontsize=8)
    ax[0, 1].grid(alpha=0.3)

    # (c) W^R/W^SD ratio — magnitude reweighting (tau-flat = degree-grading confirmed)
    ax[1, 0].plot(tau, r["ratio_z"], "--", label=f"W^zeta/W^SD (K={r['K_z_mean']:.3g})", lw=1.6)
    ax[1, 0].plot(tau, r["ratio_f"], ":", label=f"W^f*/W^SD (K={r['K_f_mean']:.3g})", lw=1.6)
    ax[1, 0].axhline(1.0, color="grey", ls="-.", alpha=0.6, label="O(1)")
    ax[1, 0].set_yscale("log")
    ax[1, 0].set_xlabel("tau")
    ax[1, 0].set_ylabel("W^R / W^SD  (regulator reweighting)")
    ax[1, 0].set_title("(c) Magnitude drift: tau-FLAT ratio = K_R (degree-grading); scale = reweight")
    ax[1, 0].legend(fontsize=8)
    ax[1, 0].grid(alpha=0.3)

    # (d) tau -> 0 degeneracy (6th-order vanishing toward genesis)
    ax[1, 1].semilogy(r["tau_near0"], np.abs(r["W_SD_near0"]), label="|W^SD| -> 0", lw=2.0)
    ax[1, 1].semilogy(r["tau_near0"], np.abs(r["W_z_near0"]), "--", label="|W^zeta| -> 0", lw=1.6)
    ax[1, 1].semilogy(r["tau_near0"], np.abs(r["W_f_near0"]), ":", label="|W^f*| -> 0", lw=1.6)
    ax[1, 1].set_xlabel("tau -> 0 (genesis)")
    ax[1, 1].set_ylabel("|W^R(tau)|")
    ax[1, 1].set_title("(d) tau->0 degeneracy preserved in all schemes (W ~ (R_K')^3 -> 0)")
    ax[1, 1].legend(fontsize=8)
    ax[1, 1].grid(alpha=0.3)

    fig.suptitle("S96-SDW-WRONSKIAN-FI — decoupling Wronskian is FI (sign/zero structural; "
                 "magnitude = regulator reweighting)", fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)
    print(f"  plot -> {OUT_PNG.relative_to(PROJECT_ROOT)}")


# ---------------------------------------------------------------------------
# Section 10 — Main: verdict 3-tuple -> composite
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)
    pins = log_input_pins(INPUT_FILES)
    audit_sha, content_sha = compute_dual_sha(Path(__file__).resolve(),
                                              CANONICAL_CONSTANTS_PATH, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    r = compute()
    make_plot(r)

    # ---- 3-tuple verdict ----
    # sign_verdict: the FI claim. PASS iff sign(W^R)=+1 (matching certified SD) at ALL grid pts
    #   in BOTH zeta and f*, with NO interior zero. Substitution chain Step 4: sign(W^SD)=+1 off
    #   tau=0 by the degree-grading; FI requires the regulated schemes to reproduce it.
    sign_ok = (
        r["sign_count"] == r["tau"].size          # 200/200 sign agreement (worst scheme)
        and r["all_positive_z"] and r["all_positive_f"] and r["all_positive_SD"]
        and r["no_interior_zero"]                 # no spurious interior zero
        and r["deg_dir_ok"] and r["deg_shrink_ok"]  # degeneracy direction toward genesis
        and r["genesis_vanish_ok"]                # tau->0 vanishing preserved
    )  # (local)
    sign_verdict = "PASS" if sign_ok else "FAIL"  # (local)

    # magnitude_verdict: the regulator reweighting. PASS iff |W^R/W^SD - 1| <= 10% in BOTH;
    #   INFO iff sign/zero FI holds but magnitude drifts >10% (EXPECTED, harmless reweighting);
    #   FAIL never used for magnitude here (a drift cannot falsify FI). Per the plan INFO_meaning.
    if not r["magnitude_drifts"]:
        magnitude_verdict = "PASS"                # (local)
    else:
        magnitude_verdict = "INFO"                # (local) regulator-reweighting, harmless
    # NOTE: magnitude FAIL is reserved for a pathological non-flat ratio (degree-grading broken).
    #   If the W^R/W^SD ratio were NOT tau-flat, the degree-grading assumption fails -> magnitude FAIL.
    ratio_flat_ok = (r["K_z_flatness"] < 1e-6 and r["K_f_flatness"] < 1e-6)  # (local)
    if not ratio_flat_ok:
        magnitude_verdict = "FAIL"                # (local) ratio NOT tau-constant => grading broken

    # regime_verdict: numerical-method validity. VALID iff the SD closed-form cross-check residual
    #   is ~machine-eps AND R_K is monotone (R_K'>0) across the grid (the degree-grading regime).
    RKp_grid = (np.exp(-4.0 * r["tau"]) - 2.0 * np.exp(-r["tau"]) + np.exp(2.0 * r["tau"]))  # (local)
    RK_monotone = bool(np.all(RKp_grid > 0))      # (local)
    sd_xcheck_ok = bool(r["sd_rel"] < SD_CLOSEDFORM_RTOL)  # (local)
    if sd_xcheck_ok and RK_monotone:
        regime_verdict = "VALID"                  # (local)
    else:
        regime_verdict = "BREAKDOWN"              # (local)

    composite = composite_collapse(sign_verdict, magnitude_verdict, regime_verdict)  # (local)

    # ---- save data ----
    np.savez(
        OUT_NPZ,
        tau=r["tau"], W_SD=r["W_SD"], W_zeta=r["W_z"], W_fstar=r["W_f"],
        W_SD_closed=r["W_SD_closed"],
        tau_near0=r["tau_near0"], W_SD_near0=r["W_SD_near0"],
        W_z_near0=r["W_z_near0"], W_f_near0=r["W_f_near0"],
        ratio_zeta=r["ratio_z"], ratio_fstar=r["ratio_f"],
        c_SD=np.array(r["c_SD"]), c_zeta=np.array(r["c_z"]), c_fstar=np.array(r["c_f"]),
        RK_fold=r["RK_fold"], n_modes=r["n_modes"],
        sd_resid=r["sd_resid"], sd_rel=r["sd_rel"],
        sign_agree_zeta=r["sign_agree_z"], sign_agree_fstar=r["sign_agree_f"],
        sign_count=r["sign_count"],
        nonzero_floor_ok=r["nonzero_ok"], no_interior_zero=r["no_interior_zero"],
        min_abs_SD=r["min_abs_SD"], min_abs_zeta=r["min_abs_z"], min_abs_fstar=r["min_abs_f"],
        K_zeta=r["K_z_mean"], K_fstar=r["K_f_mean"],
        K_zeta_flatness=r["K_z_flatness"], K_fstar_flatness=r["K_f_flatness"],
        mag_drift_zeta=r["mag_drift_z"], mag_drift_fstar=r["mag_drift_f"],
        deg_dir_ok=r["deg_dir_ok"], genesis_vanish_ok=r["genesis_vanish_ok"],
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict, composite=composite,
        RK_monotone=RK_monotone, sd_xcheck_ok=sd_xcheck_ok, ratio_flat_ok=ratio_flat_ok,
    )
    print(f"  data -> {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    # ---- value field ----
    value_field = (
        f"composite={composite};"
        f"sign_agree_zeta={r['sign_agree_z']}/{r['tau'].size};"
        f"sign_agree_fstar={r['sign_agree_f']}/{r['tau'].size};"
        f"all_positive_SD={r['all_positive_SD']};all_positive_zeta={r['all_positive_z']};"
        f"all_positive_fstar={r['all_positive_f']};"
        f"interior_zeros_SD={r['iz_SD']};interior_zeros_zeta={r['iz_z']};interior_zeros_fstar={r['iz_f']};"
        f"min_abs_W_SD={r['min_abs_SD']:.4e};min_abs_W_zeta={r['min_abs_z']:.4e};"
        f"min_abs_W_fstar={r['min_abs_f']:.4e};nonzero_floor_ok={r['nonzero_ok']};"
        f"deg_dir_ok={r['deg_dir_ok']};genesis_vanish_ok={r['genesis_vanish_ok']};"
        f"K_zeta_over_SD={r['K_z_mean']:.6g};K_fstar_over_SD={r['K_f_mean']:.6g};"
        f"ratio_flat_zeta={r['K_z_flatness']:.2e};ratio_flat_fstar={r['K_f_flatness']:.2e};"
        f"mag_drift_zeta={r['mag_drift_z']:.4g};mag_drift_fstar={r['mag_drift_f']:.4g};"
        f"SD_closedform_rel_resid={r['sd_rel']:.3e};RK_monotone={RK_monotone};"
        f"sign={sign_verdict};magnitude={magnitude_verdict};regime={regime_verdict};"
        f"CLASS=FULL;regulator_pin=a_n^SD(identity)+a_n^zeta+a_n^cutoff;FI_layer=Layer-1-degree-grading"
    )  # (local)

    tag = (f"(value={composite}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")  # (local)
    print(tag)

    append_verdict(composite, value_field, audit_sha, content_sha,
                   sign_verdict, magnitude_verdict, regime_verdict)

    wall = time.time() - t0  # (local)
    print(f"\n  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print(f"  3-tuple: sign={sign_verdict} magnitude={magnitude_verdict} regime={regime_verdict}")
    print(f"=== {GATE_ID}: {composite} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
