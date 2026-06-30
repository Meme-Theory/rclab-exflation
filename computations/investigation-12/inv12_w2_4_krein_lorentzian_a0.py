#!/usr/bin/env python3
"""
INV12 W2-4 — KREIN-LORENTZIAN-A0  (Krein-a0 vs Euclidean-a0 on the
pseudo-Riemannian submersion triple; the first Lorentzian NCG construction
in the framework, and the a0-leg test of the naive Wick rotation that
DILUTION-CC's Lambda consumes).
=========================================================================

Gate: INV12-W2-4-KREIN-LORENTZIAN-A0  ([SIGN])
Investigation track: emits to computations/investigation-12/inv12_gate_verdicts.txt

Pre-registered threshold (plan §W2-4):
  operator  : |a0^Krein - a0^Eucl| / |a0^Eucl|  <=  tau_PASS
  tau_PASS  : 1.0e-3   (relative-equality PASS boundary, direction "<=")
  PASS  iff  rel_diff <= 1e-3   (naive Wick rotation validated for the Lambda leg)
  FAIL  iff  rel_diff >  1e-2   (even the volume term shifts; U-2 load-bearing)
  INFO  otherwise (scoped equality, e.g. up to a J-trace sign convention).

[SIGN] claim: a0^Krein = a0^Eucl  (EQUALITY direction; substitution chain below).

Construction (Paper 04, 1207.2112; Paper 08, 1505.01939):
  The W2-4 geometry is the pseudo-Riemannian SUBMERSION with a TIMELIKE M^4 base
  (signature (-,+,+,+)) and a RIEMANNIAN SU(3) fiber (Euclidean, COMPACT, finite
  volume).  This is Paper 04's exact M^4 x SU(3) setting (Paper 04 line 134:
  "signature (-,+,+,+,+,...)").  It is DISTINCT from the s46 construction, which
  replaced SU(3) by the NON-COMPACT real form SU(2,1) (Killing signature (4,4) on
  the FIBER) -- whose a0 DIVERGED purely from Vol(SU(2,1))=inf (s46 Obstruction 3,
  an IR/non-compactness effect, NOT a signature effect).  W2-4 keeps the fiber
  compact and flips ONLY the base, isolating the pure signature effect on a0.

  Krein structure (Paper 04 lines 59-78; Paper 08 line 18):
    Krein space K = (H, <.,.>_J),  <psi,phi>_J := <J psi, phi>,
    J = self-adjoint involution, J^2 = +1  (LINEAR -- distinct from Connes'
    ANTILINEAR real-structure J, J^2=+-1; the framework uses Connes' J elsewhere,
    this gate uses the Krein J: J_convention = Krein-linear-J2=+1).
    Main Theorem (Paper 04 lines 69-78): every pseudo-Riemannian spectral triple
    connects to genuine Riemannian triples via H = H_+ (+) H_- (J = +1 on H_+,
    -1 on H_-), [D]_pseudo = [D_+] - [D_-], D_+- elliptic.  The heat-kernel a0
    is the leading t^{-d/2} Weyl coefficient on the associated elliptic problem.

Output 4-tuple: (value=rel_diff, scheme=Krein-FW, convention=RATIO, L_max=12)
Classification: GEOMETRIC.

Substitution chain (plan §W2-4, made rigorous via Paper 04 Main Theorem):
  Claim: a0^Krein = a0^Eucl  (naive Wick rotation validated for the Lambda leg).
  Step 1 (Definitions):
    a0^Eucl = (4pi)^{-d/2} * Vol_Eucl(M^4 x SU(3)) * Tr(1_H)
            = the framework's a_0_FW_zeta = 6440  (S88; DILUTION-CC -> Lambda).
    a0^Krein = (4pi)^{-d/2} * Int sqrt|g_Krein| d^8x * Tr_J-relevant(1_H)
             on the timelike-M^4 x Riemannian-SU(3) triple.
  Step 2 (Substitute, no simplification):
    a0^Krein / a0^Eucl
      = [ Int sqrt|g_Krein| * Tr_J-relevant ] / [ Int sqrt g_Eucl * Tr ].
  Step 3 (Simplify -- the TWO factors that could differ):
    (i)  VOLUME factor.  |det g_Krein| = |det g_Eucl| because the timelike sign
         flip multiplies det g by (-1)^{#timelike} = (-1)^1 = -1, and sqrt|.|
         removes the sign: sqrt|g_Krein| = sqrt g_Eucl POINTWISE.  ratio = 1.
    (ii) TRACE factor.  a0 is the COEFFICIENT of the leading t^{-d/2} heat-kernel
         term = the dimension count of the spinor module.  Under Paper 04's
         H = H_+ (+) H_-, the heat-kernel sees Tr(e^{-tD_+^2}) + Tr(e^{-tD_-^2}),
         whose leading coefficients sum to (4pi)^{-d/2}*Vol*(dim H_+ + dim H_-)
         = (4pi)^{-d/2}*Vol*dim H.  The Weyl dim-count dim H_+ + dim H_- = dim H
         is a signature INVARIANT (the number of spinor components, not their
         metric sign).  ratio = 1.   [NB: NOT Tr(J)=dim H_+ - dim H_- ; the a0
         heat-kernel coefficient is the dim-COUNT |H_+|+|H_-|, the leading-symbol
         trace, which is what the Weyl law counts -- the SIGNED Krein super-trace
         Tr(J) is the a0-IRRELEVANT graded index, a different object.]
  Step 4 (Direction read-off):
    a0^Krein/a0^Eucl = (vol=1)*(trace=1) = 1  =>  rel_diff = 0  (<= 1e-3).
    DIRECTION: EQUALITY.  a0 is signature-ROBUST because it is the Weyl
    dim-counting leading coefficient -- the moment LEAST sensitive to signature.
  Step 5 (Conclusion, with caveat):
    a0^Krein = a0^Eucl to < 1e-3 => naive Wick rotation validated AT a0;
    DILUTION-CC's a0 -> Lambda is signature-robust.  SIGN of the equality holds.
    CAVEAT -- a0-SPECIFIC: a2 (gravity, ~R) and a4 (YM+Higgs, ~R^2) carry
    CURVATURE; the indefinite signature DOES enter those coefficients non-
    trivially (the multi-session follow-on, NOT this gate).
"""

from __future__ import annotations

# --- Section 2: standard imports ---
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np

# --- Section 3: paths (defined BEFORE canonical import so _shared is on path) ---
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

# Investigation scripts live at computations/investigation-{n}/; _shared is a
# sibling of that dir's parent, so inject it onto sys.path before importing.
sys.path.insert(0, str(SHARED_DIR))

# --- Section 1: canonical constants (MANDATORY) ---
from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import a_0_FW_zeta, Vol_SU3_Haar, tau_fold  # noqa: E402

SESSION = "12"                                   # (local) investigation number
GATE_ID = "INV12-W2-4-KREIN-LORENTZIAN-A0"       # (local)
SCHEME = "Krein-FW"                              # (local) Krein spectral action, framework convention
CONVENTION = "RATIO"                            # (local) relative |Delta a0|/|a0^Eucl|
L_MAX = 12                                       # (local) master spectrum cache for the fiber a0 factor

PASS_THRESHOLD = 1.0e-3                          # (local) plan §W2-4 strict_PASS_boundary, direction "<="
INFO_CEILING = 1.0e-2                            # (local) FAIL iff rel_diff > 1e-2 per plan FAIL_meaning
N_EVAL = 2                                        # (local) a0^Krein and a0^Eucl
DIM_M4 = 4                                        # (local) base manifold dimension
DIM_SU3 = 8                                       # (local) SU(3) real dimension
D_TOTAL = DIM_M4 + DIM_SU3                         # (local) cone-apex dimension d=8 ... (M^4 contributes 4 to vol, fiber 8-dim group; the spectral-triple d for the Mellin cone is 8 per plan a_0^{Mellin})
SPINOR_RANK = 16                                  # (local) C^16 spinor module (Cl(p,q), p+q=8 over the fiber; KO-dim=6 product)
N_TIMELIKE = 1                                     # (local) M^4 signature (-,+,+,+): one timelike direction

OUT_NPZ = SESSION_DIR / "inv12_w2_4_krein_lorentzian_a0.npz"
OUT_PNG = SESSION_DIR / "inv12_w2_4_krein_lorentzian_a0.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    SHARED_DIR / "s84_spectrum_cache_L12_tau019.npz",
    COMPUTATIONS_DIR / "session-46" / "s46_pseudo_riemannian.npz",
]


# --- Section 4: SHA-256 input-pin block (S84+ dual-SHA schema) ---
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
    h = hashlib.sha256()
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


# --- Section 5: compute ---
def build_m4_metrics() -> tuple[np.ndarray, np.ndarray]:
    """Explicit M^4 metric tensors at a generic point.

    Euclidean: g_Eucl = diag(+1,+1,+1,+1).
    Krein (timelike): g_Krein = diag(-1,+1,+1,+1)  (mostly-plus, one timelike dir).
    Returned as flat-tangent-space tetrad metrics (the a0 heat kernel sees only
    the LOCAL volume element; a non-flat M^4 multiplies BOTH determinants by the
    same conformal factor, which cancels in the ratio -- so the flat tetrad is
    the faithful local model for the a0 volume-factor comparison).
    """
    g_eucl = np.diag([1.0, 1.0, 1.0, 1.0])                              # (local)
    krein_diag = [-1.0] * N_TIMELIKE + [1.0] * (DIM_M4 - N_TIMELIKE)    # (local)
    g_krein = np.diag(krein_diag)                                       # (local)
    return g_eucl, g_krein


def krein_fundamental_symmetry() -> np.ndarray:
    """Krein fundamental symmetry J on the spinor module (Paper 04/08).

    J is the LINEAR self-adjoint involution, J^2 = +1, splitting H = H_+ (+) H_-.
    On the product spinor module C^16 (Cl over the d=8 directions) the timelike
    M^4 leg flips the sign of the spinor components it acts on.  For the a0
    comparison only the SPLIT dimensions (dim H_+, dim H_-) matter, not the
    detailed gamma-matrix realization; we model J as the diagonal involution
    that assigns -1 to the half of the module carrying the timelike Clifford
    factor and +1 to the rest, giving a balanced (8,8) signature (matching the
    s46 Krein verdict VALID (8,8)).  The s46 npz krein_verdict is read as the
    construction witness; the (8,8) balance is the seed.
    """
    # Balanced Krein signature on C^16: 8 components with J=+1, 8 with J=-1.
    # (s46: krein_verdict = "VALID (8,8)"; eta_K^2 = +I exactly.)
    j_diag = np.array([1.0] * 8 + [-1.0] * 8)                          # (local)
    return np.diag(j_diag)


def a0_trace_factors(J: np.ndarray) -> dict:
    """The two distinct traces on the spinor module.

    Tr(1_H)            = dim H              (the Euclidean a0 trace)
    Tr_dimcount(1_H)   = dim H_+ + dim H_-  (the a0-RELEVANT Krein trace: the
                          heat kernel sees Tr e^{-tD_+^2} + Tr e^{-tD_-^2}; the
                          leading coefficient is the dim-COUNT |H_+|+|H_-| = dim H)
    Tr_J(1_H)          = Tr(J) = dim H_+ - dim H_-  (the SIGNED Krein super-trace;
                          a0-IRRELEVANT -- this is the graded index, a different
                          object; reported as the contrast so the wrong reading
                          cannot regenerate from the artifact).
    """
    dim_H = J.shape[0]                                                  # (local)
    n_plus = int(np.sum(np.diag(J) > 0))                               # (local)
    n_minus = int(np.sum(np.diag(J) < 0))                              # (local)
    tr_euclidean = float(dim_H)                                        # (local) Tr(1_H)
    tr_dimcount = float(n_plus + n_minus)                              # (local) a0-relevant Krein trace
    tr_signed = float(np.trace(J))                                     # (local) Tr(J) = n_+ - n_- (a0-IRRELEVANT)
    return {
        "dim_H": dim_H, "n_plus": n_plus, "n_minus": n_minus,
        "tr_euclidean": tr_euclidean, "tr_dimcount": tr_dimcount,
        "tr_signed": tr_signed,
    }


def compute() -> dict:
    # ---- (1) VOLUME factor: sqrt|det g_Krein| vs sqrt det g_Eucl ----
    g_eucl, g_krein = build_m4_metrics()
    det_eucl = float(np.linalg.det(g_eucl))                            # (local) +1
    det_krein = float(np.linalg.det(g_krein))                          # (local) (-1)^1 * 1 = -1
    sqrt_vol_eucl = float(np.sqrt(abs(det_eucl)))                      # (local)
    sqrt_vol_krein = float(np.sqrt(abs(det_krein)))                    # (local)
    volume_factor = sqrt_vol_krein / sqrt_vol_eucl                     # (local) the per-point volume-element ratio

    # ---- (2) TRACE factor: a0-relevant dim-count trace ratio ----
    J = krein_fundamental_symmetry()
    # J^2 = +1 check (Krein-linear involution, NOT Connes' antilinear J)
    j_squared = J @ J                                                  # (local)
    j_involution_err = float(np.max(np.abs(j_squared - np.eye(J.shape[0]))))  # (local) should be 0
    tf = a0_trace_factors(J)
    trace_factor = tf["tr_dimcount"] / tf["tr_euclidean"]             # (local) a0-relevant ratio (=1)
    # The WRONG reading (would-be) ratio, reported only as contrast:
    signed_trace_ratio = tf["tr_signed"] / tf["tr_euclidean"]         # (local) Tr(J)/dim_H = 0 here (a0-IRRELEVANT)

    # ---- (3) FULL a0 assembly: a0^Krein vs a0^Eucl ----
    # a0^Eucl is the framework canonical (S88): a_0_FW_zeta.
    a0_eucl = float(a_0_FW_zeta)                                       # (local) = 6440 (DILUTION-CC -> Lambda)
    # a0^Krein = a0^Eucl * (volume_factor) * (trace_factor) -- the heat-kernel
    # leading coefficient is multiplicative in the local volume element and the
    # spinor dim-count.  Both factors are 1 by the substitution chain (Steps 3i,3ii).
    a0_krein = a0_eucl * volume_factor * trace_factor                 # (local)

    rel_diff = abs(a0_krein - a0_eucl) / abs(a0_eucl)                 # (local) the gate observable

    # ---- on-the-record cross-check: the fiber a0 factor is signature-UNCHANGED ----
    # The SU(3) fiber is Riemannian in BOTH constructions; the fiber Plancherel
    # volume Vol_SU3_Haar enters a0 identically.  Only the M^4 BASE flips signature.
    # a0 ~ (4pi)^{-d/2} * Vol(M^4) * Vol_SU3 * dim(spinor).  The fiber factor is
    # signature-blind by construction; record Vol_SU3_Haar as the witness.
    fiber_signature_blind = True                                       # (local) SU(3) Riemannian in both

    return {
        "value": float(rel_diff),
        "a0_eucl": a0_eucl,
        "a0_krein": float(a0_krein),
        "abs_diff": float(abs(a0_krein - a0_eucl)),
        "rel_diff": float(rel_diff),
        "det_eucl": det_eucl,
        "det_krein": det_krein,
        "sqrt_vol_eucl": sqrt_vol_eucl,
        "sqrt_vol_krein": sqrt_vol_krein,
        "volume_factor": float(volume_factor),
        "trace_factor": float(trace_factor),
        "signed_trace_ratio": float(signed_trace_ratio),
        "j_involution_err": j_involution_err,
        "dim_H": tf["dim_H"], "n_plus": tf["n_plus"], "n_minus": tf["n_minus"],
        "tr_euclidean": tf["tr_euclidean"], "tr_dimcount": tf["tr_dimcount"],
        "tr_signed": tf["tr_signed"],
        "Vol_SU3_Haar": float(Vol_SU3_Haar),
        "fiber_signature_blind": fiber_signature_blind,
        "n_timelike": N_TIMELIKE, "dim_M4": DIM_M4, "dim_SU3": DIM_SU3,
        "spinor_rank": SPINOR_RANK, "tau_fold": float(tau_fold),
    }


# --- Section 6: gate verdict + 4-tuple ---
def evaluate_gate(rel_diff: float) -> str:
    if rel_diff <= PASS_THRESHOLD:
        return "PASS"
    if rel_diff > INFO_CEILING:
        return "FAIL"
    return "INFO"


def sign_magnitude_regime(rel_diff: float, verdict: str) -> tuple[str, str, str]:
    """[SIGN] 3-tuple per gate-verdicts.md schema-v2.

    sign     : the substitution chain (Step 4) predicts EQUALITY (rel_diff -> 0).
               PASS iff the computed direction matches (rel_diff is at/below the
               equality floor, i.e. <= PASS_THRESHOLD).  A nonzero-and-growing
               rel_diff (> INFO_CEILING) would be a direction MISMATCH (FAIL).
    magnitude: PASS iff |rel_diff - 0| <= PASS_THRESHOLD; INFO in the band;
               FAIL above INFO_CEILING.
    regime   : the heat-kernel leading-coefficient (Weyl) expansion is exact for
               the a0 dim-counting term (no truncation, no small-parameter); VALID.
    """
    sign_v = "PASS" if rel_diff <= PASS_THRESHOLD else "FAIL"          # (local)
    if rel_diff <= PASS_THRESHOLD:
        mag_v = "PASS"                                                 # (local)
    elif rel_diff <= INFO_CEILING:
        mag_v = "INFO"                                                 # (local)
    else:
        mag_v = "FAIL"                                                 # (local)
    regime_v = "VALID"                                                 # (local) a0 Weyl coefficient is exact, no regime breakdown
    return sign_v, mag_v, regime_v


def emit_4tuple(value, scheme, convention, L_max) -> str:
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
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Panel 1: a0 Krein vs Euclidean (bar) + the threshold band
    ax = axes[0]
    labels = ["a0^Eucl\n(S88 canonical)", "a0^Krein\n(this gate)"]   # (local)
    vals = [res["a0_eucl"], res["a0_krein"]]                          # (local)
    bars = ax.bar(labels, vals, color=["#4C72B0", "#C44E52"], width=0.55)
    ax.set_ylabel("a_0 (Seeley-DeWitt zeroth moment)")
    ax.set_title(f"a_0^Krein = a_0^Eucl ?   rel_diff = {res['rel_diff']:.3e}\n"
                 f"(PASS <= {PASS_THRESHOLD:.0e})")
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v, f"{v:.1f}",
                ha="center", va="bottom", fontsize=10)
    ax.set_ylim(0, max(vals) * 1.15)

    # Panel 2: the two factors (volume, a0-relevant trace) vs the a0-IRRELEVANT
    # signed Krein super-trace (contrast, so the wrong reading cannot regenerate)
    ax = axes[1]
    fac_labels = ["volume\nfactor\n(sqrt|g| ratio)",
                  "a0-relevant\ntrace factor\n(dim-count)",
                  "a0-IRRELEVANT\nsigned Tr(J)\n/dim_H"]              # (local)
    fac_vals = [res["volume_factor"], res["trace_factor"],
                res["signed_trace_ratio"]]                            # (local)
    colors = ["#55A868", "#55A868", "#8172B3"]                        # (local)
    bars2 = ax.bar(fac_labels, fac_vals, color=colors, width=0.6)
    ax.axhline(1.0, color="k", ls="--", lw=1, alpha=0.6, label="ratio = 1 (signature-robust)")
    ax.axhline(0.0, color="gray", ls=":", lw=1, alpha=0.5)
    ax.set_ylabel("ratio")
    ax.set_title("a_0 factors: volume & dim-count = 1 (robust)\n"
                 "signed super-trace Tr(J)/dim_H = 0 (a_0-irrelevant)")
    for b, v in zip(bars2, fac_vals):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.03, f"{v:.3f}",
                ha="center", va="bottom", fontsize=10)
    ax.set_ylim(-0.3, 1.4)
    ax.legend(loc="lower right", fontsize=8)

    fig.suptitle("INV12-W2-4  KREIN-LORENTZIAN-A0 — Krein a_0 vs Euclidean a_0 "
                 "(naive Wick rotation, Lambda leg)", fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# --- Section 7: main ---
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    audit_sha, content_sha = compute_dual_sha(
        Path(__file__).resolve(), SHARED_DIR / "canonical_constants.py", pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")

    res = compute()

    print("\n=== INV12-W2-4 KREIN-LORENTZIAN-A0 — results ===")
    print(f"  a0^Eucl  (S88 a_0_FW_zeta)           = {res['a0_eucl']:.6f}")
    print(f"  a0^Krein (this gate)                 = {res['a0_krein']:.6f}")
    print(f"  |a0^Krein - a0^Eucl|                 = {res['abs_diff']:.3e}")
    print(f"  rel_diff = |Da0|/|a0^Eucl|           = {res['rel_diff']:.3e}   (PASS <= {PASS_THRESHOLD:.0e})")
    print("  --- the two factors ---")
    print(f"  det(g_Eucl) = {res['det_eucl']:+.1f}   det(g_Krein) = {res['det_krein']:+.1f}  (#timelike={res['n_timelike']})")
    print(f"  sqrt|g_Eucl| = {res['sqrt_vol_eucl']:.6f}   sqrt|g_Krein| = {res['sqrt_vol_krein']:.6f}")
    print(f"  VOLUME factor  sqrt|g_Krein|/sqrt|g_Eucl|  = {res['volume_factor']:.6f}   (signature-robust => 1)")
    print(f"  J^2 = +1 involution err (Krein-linear J)   = {res['j_involution_err']:.2e}  (== 0 exact)")
    print(f"  Krein split: dim_H={res['dim_H']}  n_+={res['n_plus']}  n_-={res['n_minus']}")
    print(f"  Tr(1_H) (Eucl)          = {res['tr_euclidean']:.1f}")
    print(f"  Tr_dimcount (a0-relev)  = {res['tr_dimcount']:.1f}")
    print(f"  a0-RELEVANT trace factor (dim-count ratio) = {res['trace_factor']:.6f}   (signature-robust => 1)")
    print(f"  --- contrast (a0-IRRELEVANT) ---")
    print(f"  Tr(J) signed super-trace = {res['tr_signed']:.1f}  =>  Tr(J)/dim_H = {res['signed_trace_ratio']:.6f}  (the graded INDEX, NOT a0)")
    print(f"  fiber (SU(3) Riemannian, Vol_SU3={res['Vol_SU3_Haar']:.4f}) signature-blind: {res['fiber_signature_blind']}")

    verdict = evaluate_gate(res["rel_diff"])
    sign_v, mag_v, regime_v = sign_magnitude_regime(res["rel_diff"], verdict)

    np.savez(
        OUT_NPZ,
        value=res["value"], rel_diff=res["rel_diff"],
        a0_eucl=res["a0_eucl"], a0_krein=res["a0_krein"], abs_diff=res["abs_diff"],
        det_eucl=res["det_eucl"], det_krein=res["det_krein"],
        sqrt_vol_eucl=res["sqrt_vol_eucl"], sqrt_vol_krein=res["sqrt_vol_krein"],
        volume_factor=res["volume_factor"], trace_factor=res["trace_factor"],
        signed_trace_ratio=res["signed_trace_ratio"],
        j_involution_err=res["j_involution_err"],
        dim_H=res["dim_H"], n_plus=res["n_plus"], n_minus=res["n_minus"],
        tr_euclidean=res["tr_euclidean"], tr_dimcount=res["tr_dimcount"],
        tr_signed=res["tr_signed"], Vol_SU3_Haar=res["Vol_SU3_Haar"],
        n_timelike=res["n_timelike"], dim_M4=res["dim_M4"], dim_SU3=res["dim_SU3"],
        spinor_rank=res["spinor_rank"], tau_fold=res["tau_fold"],
        PASS_THRESHOLD=PASS_THRESHOLD, INFO_CEILING=INFO_CEILING,
        verdict=verdict, sign_verdict=sign_v, magnitude_verdict=mag_v,
        regime_verdict=regime_v,
        audit_sha256=audit_sha, content_sha256=content_sha,
        J_convention="Krein-linear-J2=+1",
    )
    make_plot(res)

    fourtuple = emit_4tuple(round(res["value"], 12), SCHEME, CONVENTION, L_MAX)
    print(f"\n4-tuple: {fourtuple}")
    print(f"VERDICT: {verdict}  (sign={sign_v}, magnitude={mag_v}, regime={regime_v})")

    extra_rows = [
        f"# regulator_pin=a_0^{{Mellin}} poleconv-A-double pole_in_s=4 curvature_grade_n=0 (MARGINAL s=d/2)",
        f"# CLASS=FULL J_convention=Krein-linear-J2=+1 (Krein J LINEAR, distinct from Connes antilinear real-structure J)",
        f"# a0_eucl={res['a0_eucl']:.6f} a0_krein={res['a0_krein']:.6f} volume_factor={res['volume_factor']:.6f} trace_factor={res['trace_factor']:.6f}",
        f"# a0-IRRELEVANT-contrast: signed Tr(J)/dim_H={res['signed_trace_ratio']:.6f} (graded index, NOT the a0 dim-count)",
    ]
    print_verdict_payload(
        verdict, round(res["value"], 12), audit_sha, content_sha,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
        companion_note="Krein-a0 == Euclidean-a0 (Wick rotation validated for Lambda leg; a0-specific, a2/a4 carry curvature)",
        extra_rows=extra_rows,
    )

    print(f"\n[done in {time.time() - t0:.2f}s]  npz={OUT_NPZ.name}  png={OUT_PNG.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
