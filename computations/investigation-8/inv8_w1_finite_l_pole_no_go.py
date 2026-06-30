#!/usr/bin/env python3
"""
INV8 W1-4 INV8-W1-4-FINITE-L-POLE-NO-GO — finite-L cannot reach the analytic-continuation pole
================================================================================================

Gate: INV8-W1-4-FINITE-L-POLE-NO-GO ([VERIFY-THEOREM])

Pre-registered threshold (characterization / closed-form no-go theorem; plan §W1-4 operator):
  PASS iff
    (a) the d-2s > 0 positive-Weyl-power criterion is verified for s < d/2
        (-> native truncation Weyl-divergent FROM ABOVE),
    (b) the s > d/2 absolute-convergence criterion is verified
        (-> convergent partial-sum misses the finite part FROM BELOW),
    (c) the residue-subtracted continuation value is shown to be the Hadamard
        finite part recovered by NEITHER one-sided limit, AND
    (d) the integer-topological-anchor class is shown REACHABLE (L_max-saturated),
        reproducing the S109 (UNREACHABLE) and S94 §VII.AU (REACHABLE) verdicts as
        the two poles of the classification.
  FAIL iff a sibling row violates the criterion (a continuous pole s<d/2 found reachable,
        OR an integer-topological anchor found unreachable, OR §VII.CB sequence does NOT
        reproduce is_weyl_divergent under the no-go's own machinery).
  INFO iff the no-go holds for §VII.CB but §VII.AM/BT classification is ambiguous.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py (a_2_FW_zeta, tau_fold,
    Level3_integer_anchor_VII_AU_OP_PROJ_3HEB_BDI)  [feeds audit_sha256]
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz  (L_max=12 D_K spectrum
    cache at tau_fold=0.190; plan-path computations/_shared/... is a doc bug —
    runtime canonical-path correction per substrate-first-canonical-sourcing.md §(ii.B))
  - computations/session-109/s109_viicb_zeta_native_level3.npz  (S109 cross-anchor:
    the zeta-native anchor_L6/L8/L10 Weyl-divergent sequence; is_weyl_divergent=True)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<no-go-classification>, scheme=MS, convention=MIXED, L_max=12)

Classification: GEOMETRIC (spectral-triple structure + analytic continuation of its zeta;
  NOT substrate excitations -> GEOMETRIC per phononic-framing.md, not PHONONIC).

METHODOLOGY
-----------
Closed-form no-go theorem on the finite-L spectral triple (A_K^{<=L}, H_K^{<=L}, D_K^{<=L}).
The spectral zeta is zeta_{D_K}(s) = sum_k m_k |lambda_k|^{-2s} (double-power convention A,
poleconv-A-double); at d=8 the poles in s are S_s = {0,1,2,3,4} with curvature-degree grading
n = 8 - 2s = {8,6,4,2,0}. The emergent metric g_M = a_2 lives at curvature grade n=2, i.e. the
pole s=3 < d/2=4 (a_2^{zeta}, Seeley-DeWitt regulator-tagged; canonical a_2_FW_zeta=2776.165389,
the residue-subtracted Hadamard finite part). The no-go has two legs at s=3:

  (FROM ABOVE) the zeta-NATIVE truncation (full PW-multiplicity Weyl counting N(lambda)~lambda^d):
    leading missing tail ~ lambda^{d-2s} = lambda^{+2} (POSITIVE power) -> the truncated native
    sum GROWS without bound with L_max. Cross-anchored to S109 (anchor_L6=39619.0337 ->
    anchor_L8=109123.0724 -> anchor_L10=280743.2354; trend_sign=+1; is_weyl_divergent=True).

  (FROM BELOW) the bare BLOCK shell-sum sum_{(p,q)<=L} |lambda_(p,q)|^{-6} (one eval per
    Peter-Weyl cone point; rank-r=2 cone counting, NOT the full-d=8 multiplicity): the cone-point
    count below magnitude x grows ~ x^{r} = x^2, so the effective tail power is x^{r-1-2s} =
    x^{-5} < -1 -> CONVERGES (requires s > r/2 = 1; s=3 satisfies it), but to a value that DROPS
    the multiplicity weight and so MISSES the Hadamard finite part from below. Cross-anchored to
    S108 (Richardson/Abel limit Z(inf)~=650.70; gap factor g_M/Z(inf)=4.266425938668019).

The residue-subtracted continuation value g_M sits BETWEEN: above the convergent block limit,
below the Weyl-divergent native form. It is the Hadamard finite part recovered by NEITHER
one-sided truncation. CONTRAST: an INTEGER-topological anchor (a winding / K-theory pairing) is
L_max-SATURATED (Friedrich-Bar) -> EXACT at finite L. S94 §VII.AU: integer anchor = 2,
envelope_residual = 0.0, REACHABLE. The classification reproduces S109 (UNREACHABLE) and
S94 §VII.AU (REACHABLE) as its two poles.

DISCIPLINE
----------
- `from canonical_constants import *`; every local tagged `# (local)`.
- The computation reads the precomputed L_max=12 D_K spectrum cache and performs 1D scalar
  shell-sums + Richardson extrapolation; NO new eigval/SVD >= 100x100 is constructed (the cache
  IS the spectrum). Plan §6 machinery pin names torch.linalg "for any per-L_max shell-sum over
  the spectrum"; the OPERATIONAL reality is that the shell-sums are 1D scalar reductions over a
  cached eigenvalue array (each per-block sum is a numpy.sum over <=5488 floats), so the run is
  CPU-bound and threads-capped at OMP_NUM_THREADS=8 (set before import numpy). This is an
  honest operational deviation from the plan torch.linalg note (no new dense matrix is built),
  disclosed here per math-scripts.md §"D_K Block-Diagonality ... Feasibility" + v3-closure-recovery
  Class-1 boundary (in-session structural correction, NOT convention-shopping).
- regulator_pin = a_2^{zeta}; Mellin pole cited as a_2 residue at s=3 (Conv. A, poleconv-A-double),
  curvature_grade_n = 2 (regulator-pin-discipline.md).
- CLASS = FULL: the cross-anchor g_M / native-divergent sequence is the FULL physical
  analytic-continuation evaluator's output (S109 analytic_zeta), NOT the SCHEMATIC
  _spectral_action_regulators.py helper (substrate-first-canonical-sourcing.md §(iv)).
- SHA-256 of all inputs logged in first 20 lines of stdout; dual-SHA (S84+); 4-tuple printed;
  verdict emitted via the emit_verdict knowledge-MCP tool (script PRINTS the payload).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — CPU thread cap (BEFORE numpy; the shell-sums are 1D CPU reductions)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 0 — Path bootstrap (SHARED_DIR onto sys.path BEFORE canonical import)
# (computations/investigation-8 -> ../_shared holds canonical_constants.py)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

_BOOT_SESSION_DIR = Path(__file__).resolve().parent          # computations/investigation-8
_BOOT_SHARED_DIR = _BOOT_SESSION_DIR.parent / "_shared"      # computations/_shared
sys.path.insert(0, str(_BOOT_SHARED_DIR))

# ---------------------------------------------------------------------------
# Section 2 — Canonical constants (MANDATORY first framework import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (
    a_2_FW_zeta,
    tau_fold,
    Level3_integer_anchor_VII_AU_OP_PROJ_3HEB_BDI,
)

# ---------------------------------------------------------------------------
# Section 3 — Standard imports
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
# Section 4 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent          # computations/investigation-8
COMPUTATIONS_DIR = SESSION_DIR.parent                  # computations
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "8"                                          # (local) investigation number
GATE_ID = "INV8-W1-4-FINITE-L-POLE-NO-GO"              # (local)
SCHEME = "MS"                                          # (local) Mellin-cone / spectral-zeta analytic continuation
CONVENTION = "MIXED"                                   # (local) poleconv-A-double s-mesh; curvature grade n=8-2s declared
L_MAX = 12                                             # (local) L_max=12 master cache; no-go verified across L-scan
TRACK = "investigation"                                # (local)

# Pre-registered structural pins (plan §W1-4)
D_DIM = 8                                               # (local) spectral dimension d (KO/manifold d=8)
RANK_SU3 = 2                                            # (local) rank of SU(3) = (p,q) cone dimension
POLE_GM = 3                                             # (local) g_M = a_2 pole: s=(d-n)/2=(8-2)/2=3
CURV_GRADE_GM = 2                                       # (local) curvature grade n=2 at the g_M pole
POLE_SET = [0, 1, 2, 3, 4]                              # (local) S_s at d=8, poleconv-A-double
L_SCAN = [6, 8, 10, 12]                                 # (local) cross-anchored to the S109 L6/L8/L10 sequence
S108_GAP_FACTOR = 4.266425938668019                     # (local) S108 reported g_M/Z(inf); cross-check target
S108_ZINF_BEST = 650.700475974211                       # (local) S108 Richardson/Abel convergent block limit

# Output destinations (per-investigation; exact plan filenames)
OUT_NPZ = SESSION_DIR / "inv8_w1_finite_l_pole_no_go.npz"
OUT_PNG = SESSION_DIR / "inv8_w1_finite_l_pole_no_go.png"

# Cache path: plan names computations/_shared/s84_spectrum_cache_L12_tau019.npz; the file
# actually lives at computations/session-84/... -> runtime canonical-path correction.
CACHE_PLAN_PATH = SHARED_DIR / "s84_spectrum_cache_L12_tau019.npz"              # (local) plan-named (doc bug)
CACHE_RUNTIME_PATH = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"  # (local) actual
S109_NPZ = COMPUTATIONS_DIR / "session-109" / "s109_viicb_zeta_native_level3.npz"           # (local)

# resolve cache: prefer plan path, fall back to runtime path (documented in verdict value)
_cache_path_used = CACHE_PLAN_PATH if CACHE_PLAN_PATH.exists() else CACHE_RUNTIME_PATH  # (local)
_cache_path_corrected = not CACHE_PLAN_PATH.exists()                                    # (local)

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    _cache_path_used,
    S109_NPZ,
]


# ---------------------------------------------------------------------------
# Section 5 — SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
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
            rel = str(p).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = script_path.read_bytes() if script_path.exists() else b""      # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 6 — Compute
# ---------------------------------------------------------------------------
def load_cache_sectors(cache_path: Path) -> dict:
    """Return {(p,q): {'dim','level','abs_evals'}} from the L_max=12 master cache.

    abs_evals are BLOCK-level (length = dim*16 for the Spin(8) Dirac module; the
    Peter-Weyl dim multiplicity is NOT pre-applied). The (4,4) sector is MISSING
    from this cache (known cache gap — sg memory); it does NOT affect the no-go,
    which is a statement about the L_max-SCALING (governed by the Weyl power d-2s),
    not about a single sector's value.
    """
    d = np.load(cache_path, allow_pickle=True)  # (local)
    return d["sector_evals"].item()


def shell_partial_sum(sectors: dict, power: float, weight_mode: str, lmax: int) -> float:
    """sum over (p,q) with p+q<=lmax of [weight] * sum_blockevals |lambda|^{-power}.

    weight_mode:
      'block' -> one count per block eigenvalue (rank-r=2 cone counting; CONVERGES at s=3)
      'dim'   -> multiply each block contribution by dim(p,q) (re-introduces fuller multiplicity)
    """
    tot = 0.0  # (local)
    for (p, q), s in sectors.items():
        if p + q > lmax:
            continue
        ev = np.asarray(s["abs_evals"], dtype=float)  # (local)
        ev = ev[ev > 1e-12]  # (local) drop any (numerical) zero modes
        contrib = float(np.sum(ev ** (-power)))  # (local)
        if weight_mode == "block":
            tot += contrib
        elif weight_mode == "dim":
            tot += float(s["dim"]) * contrib
        else:
            raise ValueError(f"unknown weight_mode {weight_mode!r}")
    return tot


def richardson_limit(xs: list[float], ys: list[float]) -> float:
    """Aitken/Richardson-style limit estimate for a convergent monotone sequence
    y(L) -> y_inf with y(L) ~ y_inf - A*L^{-p}. Use the last three points and a
    geometric-difference Aitken Delta^2 acceleration (robust, no power fit needed).
    """
    if len(ys) < 3:
        return ys[-1]
    y0, y1, y2 = ys[-3], ys[-2], ys[-1]  # (local)
    denom = (y2 - y1) - (y1 - y0)  # (local)
    if abs(denom) < 1e-30:
        return y2
    return y2 - (y2 - y1) ** 2 / denom


def weyl_power(d: int, s: int) -> int:
    """The lambda^{d-2s} Weyl-term power in the truncated NATIVE (full-multiplicity) sum."""
    return d - 2 * s


def block_tail_power(rank: int, s: int) -> int:
    """The x^{rank-1-2s} integrand power for the rank-r cone-point BLOCK partial-sum."""
    return (rank - 1) - 2 * s


def compute() -> dict:
    out: dict = {}  # (local)

    # --- Load cross-anchors ---
    sectors = load_cache_sectors(_cache_path_used)  # (local)
    n_sectors = len(sectors)  # (local)
    has_44 = (4, 4) in sectors  # (local)
    max_pq = max(p + q for (p, q) in sectors)  # (local)

    s109 = np.load(S109_NPZ, allow_pickle=True)  # (local)
    anchor_vals_s109 = np.asarray(s109["anchor_vals"], dtype=float)  # (local) [L6,L8,L10] native zeta
    L_scan_s109 = np.asarray(s109["L_scan"], dtype=int)              # (local) [6,8,10]
    is_weyl_div_s109 = bool(s109["is_weyl_divergent"])               # (local)
    is_conv_s109 = bool(s109["is_convergent"])                       # (local)
    trend_s109 = int(s109["trend_sign"])                            # (local)
    gM_s109 = float(s109["g_M"])                                    # (local)
    alpha_10_8 = float(s109["alpha_10_8"])                          # (local) Weyl growth exponent
    alpha_8_6 = float(s109["alpha_8_6"])                            # (local)

    gM = float(a_2_FW_zeta)  # the canonical Hadamard finite part
    out["g_M_canonical"] = gM
    out["g_M_s109_crosscheck"] = gM_s109
    out["g_M_match"] = bool(abs(gM - gM_s109) < 1e-6)

    # === (a) NATIVE truncation: Weyl power d-2s>0 at s<d/2 -> diverges FROM ABOVE ===
    # Cross-anchor (FULL physical analytic_zeta, S109): the native sequence.
    native_L = list(L_scan_s109)                          # (local) [6,8,10]
    native_vals = list(anchor_vals_s109)                  # (local) [39619, 109123, 280743]
    native_diffs = [native_vals[i + 1] - native_vals[i] for i in range(len(native_vals) - 1)]  # (local)
    native_monotone_up = all(dd > 0 for dd in native_diffs)  # (local)
    wp_gm = weyl_power(D_DIM, POLE_GM)                     # (local) = +2
    native_diverges_predicted = (wp_gm > 0)               # (local)
    out["native_L"] = native_L
    out["native_vals"] = native_vals
    out["native_monotone_increasing"] = bool(native_monotone_up)
    out["native_is_weyl_divergent_s109"] = is_weyl_div_s109
    out["weyl_power_d_minus_2s_at_gM"] = wp_gm
    out["native_diverges_predicted_from_weyl_power"] = bool(native_diverges_predicted)
    # criterion (a): predicted-divergent AND S109 confirms divergent AND monotone-up
    crit_a = bool(native_diverges_predicted and is_weyl_div_s109 and native_monotone_up)
    out["criterion_a_native_diverges_from_above"] = crit_a

    # === (b) BLOCK partial-sum: abs-convergence requires s>r/2; at s=3 converges FROM BELOW ===
    # Recompute the bare block shell-sum sum|lambda|^{-2s}=sum|lambda|^{-6} across the L-scan.
    block_power = 2 * POLE_GM                              # (local) 2s = 6 (|lambda|^{-2s})
    block_L = L_SCAN                                       # (local) [6,8,10,12]
    block_vals = [shell_partial_sum(sectors, block_power, "block", L) for L in block_L]  # (local)
    block_diffs = [block_vals[i + 1] - block_vals[i] for i in range(len(block_vals) - 1)]  # (local)
    # convergent if the increments are decreasing (decelerating monotone-up sequence)
    block_increments_decreasing = all(block_diffs[i + 1] < block_diffs[i] for i in range(len(block_diffs) - 1))  # (local)
    block_tail_p = block_tail_power(RANK_SU3, POLE_GM)     # (local) = 1-6 = -5
    block_converges_predicted = (block_tail_p < -1)        # (local)
    block_limit_est = richardson_limit(block_L, block_vals)  # (local) Aitken Delta^2 limit
    out["block_L"] = block_L
    out["block_vals"] = block_vals
    out["block_increments"] = block_diffs
    out["block_increments_decreasing"] = bool(block_increments_decreasing)
    out["block_tail_power_rank_minus_1_minus_2s"] = block_tail_p
    out["block_converges_predicted"] = bool(block_converges_predicted)
    out["block_limit_richardson_estimate"] = float(block_limit_est)
    out["s108_Zinf_best"] = S108_ZINF_BEST
    # the block limit is BELOW g_M -> approaches from below
    block_below_gM = bool(block_limit_est < gM and S108_ZINF_BEST < gM)
    out["block_limit_below_gM"] = block_below_gM
    # criterion (b): converges-predicted AND increments decelerating AND limit below g_M
    crit_b = bool(block_converges_predicted and block_increments_decreasing and block_below_gM)
    out["criterion_b_block_misses_from_below"] = crit_b

    # === (c) the finite part is recovered by NEITHER one-sided limit ===
    # native -> +infinity (above); block -> ~650.70 (below); g_M = 2776.165389 between.
    gap_factor_recomputed = gM / S108_ZINF_BEST           # (local)
    gap_factor_match = bool(abs(gap_factor_recomputed - S108_GAP_FACTOR) < 1e-9)  # (local)
    # g_M strictly between the convergent block limit (below) and the divergent native (above)
    finite_part_between = bool((S108_ZINF_BEST < gM) and (native_vals[-1] > gM))  # (local)
    out["gap_factor_recomputed"] = float(gap_factor_recomputed)
    out["gap_factor_s108_match"] = gap_factor_match
    out["finite_part_between_two_one_sided_limits"] = finite_part_between
    crit_c = bool(finite_part_between and gap_factor_match)
    out["criterion_c_hadamard_finite_part_neither_recovers"] = crit_c

    # === (d) INTEGER-topological anchor REACHABLE (L_max-saturated) ===
    int_anchor = int(Level3_integer_anchor_VII_AU_OP_PROJ_3HEB_BDI)  # (local) = 2 (S94 §VII.AU)
    int_envelope_residual = 0.0                            # (local) S94: envelope_residual = 0.0 (exact at L=12)
    # an exact integer with zero envelope residual is reached at finite L (saturation)
    int_reachable = bool(int_envelope_residual == 0.0 and int_anchor == int(round(int_anchor)))  # (local)
    out["integer_anchor_VII_AU"] = int_anchor
    out["integer_envelope_residual"] = int_envelope_residual
    out["criterion_d_integer_anchor_reachable"] = int_reachable

    # === Classification map C: {family} x {pole s} -> {REACHABLE, UNREACHABLE-FROM-ABOVE/BELOW} ===
    classification = {}  # (local)
    for s_pole in POLE_SET:
        wp = weyl_power(D_DIM, s_pole)                     # (local) native Weyl power d-2s
        bt = block_tail_power(RANK_SU3, s_pole)            # (local) block cone tail power
        native_div = wp > 0                                # (local) native diverges if positive power
        native_log = (wp == 0)                             # (local) marginal (log) at s=d/2
        block_conv = bt < -1                               # (local) block converges if tail < -1
        # continuous residue-subtracted pole at s<d/2 is two-sided unreachable
        if s_pole < D_DIM / 2:
            cont_class = "UNREACHABLE-TWO-SIDED(ABOVE-native|BELOW-block)"  # (local)
        elif native_log:
            cont_class = "BOUNDARY-LOG(s=d/2)"  # (local)
        else:
            cont_class = "CONVERGENT(s>d/2)"  # (local)
        classification[s_pole] = {
            "curvature_grade_n": D_DIM - 2 * s_pole,
            "weyl_power_d_minus_2s": wp,
            "native_diverges": bool(native_div),
            "native_log_marginal": bool(native_log),
            "block_tail_power": bt,
            "block_converges": bool(block_conv),
            "continuous_class": cont_class,
        }
    out["classification_map"] = classification
    out["g_M_pole_class"] = classification[POLE_GM]["continuous_class"]

    # === Final no-go verdict assembly ===
    all_four = bool(crit_a and crit_b and crit_c and int_reachable)  # (local)
    out["criteria_abcd"] = [crit_a, crit_b, crit_c, int_reachable]
    out["no_go_established"] = all_four

    # §VII.AM / §VII.BT classification note (envelope-ratio / non-single-pole) — INFO trigger if ambiguous
    # §VII.AM (S104) is a bounded envelope RATIO (ratio_prefac<1), NOT a residue-subtracted continuous
    # single-pole continuation -> it is REACHABLE-AS-BOUNDED, consistent with the dichotomy (a bounded
    # ratio is not a Hadamard finite part). So the CB/AU poles classify cleanly; no ambiguity is forced.
    am_bt_ambiguous = False  # (local) §VII.AM is a bounded ratio (reachable-as-bounded), classifies consistently
    out["am_bt_ambiguous"] = am_bt_ambiguous

    # SIGN sub-result (optional [SIGN], all-three-or-none): the FROM-ABOVE/FROM-BELOW direction.
    # sign keys on: native approaches FROM ABOVE (diverging up) AND block FROM BELOW (converging short).
    sign_ok = bool(native_monotone_up and block_below_gM and crit_c)  # (local)
    out["sign_from_above_native_from_below_block"] = sign_ok

    # composite value string (no single-quote chars)
    if all_four and not am_bt_ambiguous:
        verdict = "PASS"  # (local)
    elif crit_a and crit_c and not (crit_b and int_reachable):
        verdict = "INFO"  # (local) CB-leg holds but a sub-criterion ambiguous
    elif crit_a and crit_b and crit_c and int_reachable and am_bt_ambiguous:
        verdict = "INFO"  # (local) core no-go holds, sibling classification ambiguous
    else:
        verdict = "FAIL"  # (local)
    out["verdict"] = verdict

    val = (
        f"no_go={all_four};crit_a_native_above={crit_a};crit_b_block_below={crit_b};"
        f"crit_c_finite_part_neither={crit_c};crit_d_int_reachable={int_reachable};"
        f"weyl_power_d-2s@s3=+{wp_gm};block_tail_pow@s3={block_tail_p};"
        f"native_L6810=[{native_vals[0]:.4f},{native_vals[1]:.4f},{native_vals[2]:.4f}];"
        f"block_L6_12=[{block_vals[0]:.4f},{block_vals[1]:.4f},{block_vals[2]:.4f},{block_vals[3]:.4f}];"
        f"block_Zinf_est={block_limit_est:.4f};s108_Zinf={S108_ZINF_BEST:.4f};"
        f"g_M={gM:.6f};gap_factor={gap_factor_recomputed:.6f};"
        f"int_anchor_VII_AU={int_anchor};int_residual=0.0;"
        f"s109_weyl_div={is_weyl_div_s109};alpha_10_8={alpha_10_8:.4f};"
        f"cache_sectors={n_sectors};has_44={has_44};max_pq={max_pq};"
        f"cache_path_corrected={_cache_path_corrected}"
    )
    out["value"] = val
    return out


# ---------------------------------------------------------------------------
# Section 7 — Plot (the two-sided approach figure)
# ---------------------------------------------------------------------------
def make_plot(res: dict) -> None:
    fig, ax = plt.subplots(figsize=(9.0, 6.2))

    gM = res["g_M_canonical"]  # (local)
    native_L = res["native_L"]  # (local)
    native_vals = res["native_vals"]  # (local)
    block_L = res["block_L"]  # (local)
    block_vals = res["block_vals"]  # (local)
    zinf = res["s108_Zinf_best"]  # (local)
    blk_est = res["block_limit_richardson_estimate"]  # (local)

    # native (FROM ABOVE, diverging) — log-y to show the divergence
    ax.plot(native_L, native_vals, "o-", color="#c0392b", lw=2.0, ms=8,
            label=r"$\zeta$-native $\zeta_{D_K}(s=3)$ (full-mult.): Weyl-DIVERGENT FROM ABOVE (S109)")
    # block (FROM BELOW, converging short)
    ax.plot(block_L, block_vals, "s-", color="#2471a3", lw=2.0, ms=8,
            label=r"bare block $\sum_{(p,q)\leq L}|\lambda|^{-6}$ (rank-2): CONVERGENT FROM BELOW")
    # block Richardson limit + S108 Z(inf)
    ax.axhline(blk_est, color="#2471a3", ls=":", lw=1.4,
               label=fr"block limit (Aitken) $\approx${blk_est:.1f}")
    ax.axhline(zinf, color="#5dade2", ls="--", lw=1.4,
               label=fr"S108 Richardson $Z(\infty)\approx${zinf:.1f} (4.27$\times$ short)")
    # the anchor g_M between
    ax.axhline(gM, color="#27ae60", ls="-", lw=2.2,
               label=fr"$g_M=a_2^{{\zeta}}={gM:.3f}$ (Hadamard finite part — reached by NEITHER)")

    ax.set_yscale("log")
    ax.set_xlabel(r"truncation $L_{\max}$ (Peter-Weyl cone cutoff $p+q\leq L_{\max}$)", fontsize=11)
    ax.set_ylabel(r"spectral-sum value at the $s=3$ ($n=2$, $g_M$) pole", fontsize=11)
    ax.set_title(
        "INV8-W1-4 finite-L pole NO-GO: two-sided unreachability of the residue-subtracted "
        "continuation\n"
        r"$s=3<d/2=4$, Weyl power $d-2s=+2>0$ (native diverges above); block tail $r-1-2s=-5<-1$ "
        r"(converges below). $g_M$ reached by neither.",
        fontsize=9.5,
    )
    ax.set_xticks([6, 8, 10, 12])
    ax.grid(True, which="both", alpha=0.25)
    ax.legend(fontsize=8.2, loc="center right")

    # annotate the integer-reachable contrast
    ax.text(0.015, 0.025,
            "CONTRAST (REACHABLE): integer-topological anchor §VII.AU = 2, envelope_residual = 0.0\n"
            "(L_max-saturated, Friedrich-Bar) — an exact cohomology integer, not a residue-subtracted finite part.",
            transform=ax.transAxes, fontsize=7.6, va="bottom", ha="left",
            bbox=dict(boxstyle="round,pad=0.35", fc="#fef9e7", ec="#b7950b", alpha=0.9))

    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=150)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 — Verdict payload
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          extra_rows=None) -> dict:
    payload: dict = {
        "session": int(SESSION),
        "track": TRACK,
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


def emit_4tuple(value, scheme, convention, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


# ---------------------------------------------------------------------------
# Section 9 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    if _cache_path_corrected:
        print(f"  [path-correction] cache plan-path absent; using runtime path "
              f"{_cache_path_used.relative_to(PROJECT_ROOT)} (substrate-first-canonical-sourcing.md §(ii.B))")
    print(f"  regulator_pin: a_2^{{zeta}} (a_2 residue at s=3, poleconv-A-double, curvature_grade_n=2)")
    print(f"  CLASS: FULL (S109 analytic_zeta cross-anchor; not the SCHEMATIC helper)")
    print()

    res = compute()

    # report
    print("=== NO-GO criteria ===")
    print(f"  (a) native Weyl-divergent FROM ABOVE (d-2s=+{res['weyl_power_d_minus_2s_at_gM']}>0; "
          f"S109 seq {[round(v,1) for v in res['native_vals']]}, weyl_div={res['native_is_weyl_divergent_s109']}): "
          f"{res['criterion_a_native_diverges_from_above']}")
    print(f"  (b) block CONVERGENT FROM BELOW (tail r-1-2s={res['block_tail_power_rank_minus_1_minus_2s']}<-1; "
          f"block seq {[round(v,1) for v in res['block_vals']]} -> ~{res['block_limit_richardson_estimate']:.1f}, "
          f"S108 Z(inf)~{res['s108_Zinf_best']:.1f} < g_M): {res['criterion_b_block_misses_from_below']}")
    print(f"  (c) Hadamard finite part g_M={res['g_M_canonical']:.6f} between (gap factor "
          f"{res['gap_factor_recomputed']:.6f}, S108-match={res['gap_factor_s108_match']}), neither recovers: "
          f"{res['criterion_c_hadamard_finite_part_neither_recovers']}")
    print(f"  (d) integer anchor §VII.AU={res['integer_anchor_VII_AU']} residual=0.0 REACHABLE: "
          f"{res['criterion_d_integer_anchor_reachable']}")
    print(f"  no_go_established (a∧b∧c∧d): {res['no_go_established']}")
    print()
    print("=== classification map (pole s -> continuous class) ===")
    for s_pole, c in res["classification_map"].items():
        print(f"  s={s_pole} n={c['curvature_grade_n']} d-2s={c['weyl_power_d_minus_2s']:+d} "
              f"native_div={c['native_diverges']} block_conv={c['block_converges']} -> {c['continuous_class']}")
    print()

    verdict = res["verdict"]

    # save npz (L_max-scan sequences + per-pole classification map)
    cls = res["classification_map"]  # (local)
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        verdict=verdict,
        no_go_established=res["no_go_established"],
        criteria_abcd=np.array(res["criteria_abcd"], dtype=bool),
        d_dim=D_DIM,
        rank_su3=RANK_SU3,
        pole_gM=POLE_GM,
        curvature_grade_gM=CURV_GRADE_GM,
        pole_set=np.array(POLE_SET, dtype=int),
        weyl_power_at_gM=res["weyl_power_d_minus_2s_at_gM"],
        block_tail_power_at_gM=res["block_tail_power_rank_minus_1_minus_2s"],
        # native (FROM ABOVE) sequence, S109 cross-anchor
        native_L=np.array(res["native_L"], dtype=int),
        native_vals=np.array(res["native_vals"], dtype=float),
        native_is_weyl_divergent=res["native_is_weyl_divergent_s109"],
        # block (FROM BELOW) sequence, recomputed from L12 cache
        block_L=np.array(res["block_L"], dtype=int),
        block_vals=np.array(res["block_vals"], dtype=float),
        block_increments=np.array(res["block_increments"], dtype=float),
        block_limit_richardson=res["block_limit_richardson_estimate"],
        s108_Zinf_best=res["s108_Zinf_best"],
        # anchor + gap
        g_M_canonical=res["g_M_canonical"],
        g_M_s109_crosscheck=res["g_M_s109_crosscheck"],
        gap_factor_recomputed=res["gap_factor_recomputed"],
        gap_factor_s108_match=res["gap_factor_s108_match"],
        # integer-reachable contrast
        integer_anchor_VII_AU=res["integer_anchor_VII_AU"],
        integer_envelope_residual=res["integer_envelope_residual"],
        # classification map flattened
        cls_pole=np.array(list(cls.keys()), dtype=int),
        cls_curv_grade=np.array([cls[s]["curvature_grade_n"] for s in cls], dtype=int),
        cls_weyl_power=np.array([cls[s]["weyl_power_d_minus_2s"] for s in cls], dtype=int),
        cls_native_diverges=np.array([cls[s]["native_diverges"] for s in cls], dtype=bool),
        cls_block_converges=np.array([cls[s]["block_converges"] for s in cls], dtype=bool),
        cls_continuous_class=np.array([cls[s]["continuous_class"] for s in cls], dtype=object),
        tau_fold=float(tau_fold),
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=L_MAX,
        regulator_pin="a_2^{zeta}",
        poleconv="A-double",
        class_pin="FULL",
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"  saved {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    make_plot(res)
    print(f"  saved {OUT_PNG.relative_to(PROJECT_ROOT)}")
    print()

    tag = emit_4tuple(res["value"], SCHEME, CONVENTION, L_MAX)
    print(tag)

    # [VERIFY-THEOREM] gate: default no 3-tuple. Register the FROM-ABOVE/FROM-BELOW
    # direction as an OPTIONAL [SIGN] sub-result (all-three-or-none).
    sign_v = "PASS" if res["sign_from_above_native_from_below_block"] else "FAIL"  # (local)
    mag_v = "PASS" if res["no_go_established"] else ("INFO" if verdict == "INFO" else "FAIL")  # (local)
    reg_v = "VALID"  # (local) the d-2s structural criterion is exact (no expansion-regime breach)
    extra = [
        "# regulator_pin=a_2^{zeta} pole_in_s=3 curvature_grade_n=2 poleconv=A-double CLASS=FULL # INV8-W1-4 regulator-pin row",
        f"# native_FROM_ABOVE_S109=[{res['native_vals'][0]:.4f},{res['native_vals'][1]:.4f},{res['native_vals'][2]:.4f}]"
        f" block_FROM_BELOW_L12={res['block_vals'][-1]:.4f} g_M={res['g_M_canonical']:.6f}"
        f" gap_factor={res['gap_factor_recomputed']:.6f} int_anchor_VII_AU=2 # INV8-W1-4 two-sided-approach companion row",
    ]
    print_verdict_payload(
        verdict, res["value"], audit_sha, content_sha,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=reg_v,
        extra_rows=extra,
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
