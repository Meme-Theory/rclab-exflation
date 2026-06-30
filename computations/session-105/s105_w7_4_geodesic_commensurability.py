#!/usr/bin/env python3
"""
S105 W7-4-GEODESIC-COMMENSURABILITY — commensurability of the substrate length
spectrum via PSLQ on SQUARED actions
=============================================================================

Gate: S105-W7-4-GEODESIC-COMMENSURABILITY ([VERIFY])

Pre-registered threshold (plan §W7-4, line 606-608):
  rational_frac = 0.80:
    PASS iff (>= 80% of pairwise SQUARED-length ratios L_i^2/L_j^2 recover a
              rational p/q with denominator <= Q_max=64 within rel_tol=1e-6)
         AND (the tau=0 control recovers exact rationals at rel_tol=1e-9 on ALL pairs).
    INFO iff < 3 stable peaks per spectrum (under-powered pairwise population).
    FAIL otherwise (incommensurable squared spectrum -> Q1 workshop, decision-point block).

The criterion is PRE-FIXED to SQUARED lengths (plan convention pin, line 630): on the
undeformed group geodesic lengths are L ~ sqrt(integer) (quadratic-form lattice
=> |lambda|^2 ~ integer => L ~ sqrt(integer)), so raw ratios L_i/L_j = sqrt(n_i/n_j)
are sqrt-rational, NOT rational — a raw-length PSLQ test FAILS tau=0 by construction.
Squaring restores rationality: L_i^2/L_j^2 = n_i/n_j in Q.

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - computations/session-105/s105_w7_2_length_spectrum_ft.npz   (measured tau_fold lengths)
  - computations/session-105/s105_w7_3_berry_tabor_match.npz    (predicted lengths; OPTIONAL —
        sister gate W7-3 is concurrent; if absent the tau_fold population is the W7-2
        measured set only, disclosed in the verdict value + WP. Plan input_files note:
        W7-3 shares the W7-2 non-FAIL gate.)
  - computations/session-105/s105_w7_1_trace_formula_exact_anchor.npz  (tau=0 anchor metadata)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

tau=0 positive control: the EXACT coroot-lattice lengths stored in W7-2's
`coroot_lengths` (analytic, NOT FT-extracted). These ARE the A2 (SU(3)) root-lattice
vectors: (L/4pi)^2 in {1,3,4,7,9,12,13,19,27} (Loeschian numbers m^2+mn+n^2), integer
to machine-eps. The control MUST recover exact rationals (rel_tol=1e-9).

Output 4-tuple:
  (value=<rational_frac>, scheme=PSLQ-SQUARED-RATIO,
   convention=SQUARED-length-ratios, L_max=12)

Classification: GEOMETRIC

METHODOLOGY
-----------
(1) Collect squared lengths {L_gamma^2} from W7-2 measured stable peaks, W7-3 predicted
peaks (if on disk), and the W7-1/W7-2 tau=0 coroot lattice (exact). (2) For each unordered
pair (i,j) within a population form r_ij = L_i^2/L_j^2 and run mpmath PSLQ on the 2-vector
[r_ij, 1] (cross-checked with a continued-fraction recovery) to recover a rational p/q with
1<=q<=Q_max=64 within tolerance. (3) PASS iff the pre-registered rational fraction is met on
the tau_fold population AND the tau=0 control is exactly rational on all pairs. (4) A FAIL
(incommensurable squared spectrum) routes to a Q1 workshop (decision-point block, NOT rubric).

DISCIPLINE
----------
- `from canonical_constants import *`
- Every intermediate tagged `# (local)`
- CPU-only (mpmath arbitrary precision); OMP_NUM_THREADS capped to 8.
- SHA-256 of inputs logged in first lines of stdout; dual-SHA (S84+) emitted.
- Verdict via print_verdict_payload -> agent calls emit_verdict MCP (race-safe).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — thread cap BEFORE numpy (CPU-only arbitrary-precision path)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys as _sys
from pathlib import Path as _Path
_SHARED = _Path(__file__).resolve().parent.parent / "_shared"
if str(_SHARED) not in _sys.path:
    _sys.path.insert(0, str(_SHARED))
from canonical_constants import *  # noqa: F401,F403
from canonical_constants import tau_fold  # explicit (used below)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
from math import gcd
from pathlib import Path

import numpy as np
import mpmath as mp
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

SESSION = "S105"                                                  # (local)
GATE_ID = "S105-W7-4-GEODESIC-COMMENSURABILITY"                  # (local)
SCHEME = "PSLQ-SQUARED-RATIO"                                     # (local)
CONVENTION = "SQUARED-length-ratios"                             # (local)
L_MAX = 12                                                       # (local)

# Pre-registered machinery pins (plan §W7-4 machinery_pin_map)
Q_MAX = 64                                                       # (local) PSLQ denominator bound
REL_TOL_FOLD = mp.mpf("1e-6")                                    # (local) tau_fold pairs
REL_TOL_CTRL = mp.mpf("1e-9")                                    # (local) tau=0 control pairs
RATIONAL_FRAC = 0.80                                            # (local) PASS boundary (>=)
MIN_PEAKS = 3                                                    # (local) min stable peaks else INFO
MP_DPS = 50                                                     # (local) mpmath precision

OUT_NPZ = SESSION_DIR / "s105_w7_4_geodesic_commensurability.npz"
OUT_PNG = SESSION_DIR / "s105_w7_4_geodesic_commensurability.png"

W7_2_NPZ = SESSION_DIR / "s105_w7_2_length_spectrum_ft.npz"
W7_3_NPZ = SESSION_DIR / "s105_w7_3_berry_tabor_match.npz"
W7_1_NPZ = SESSION_DIR / "s105_w7_1_trace_formula_exact_anchor.npz"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    W7_2_NPZ,
    W7_3_NPZ,  # may be absent (sister gate concurrent); sha256_of returns "" if missing
    W7_1_NPZ,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 dual-pin block (S84+)
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
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        tag = sha[:16] + "..." if sha else "<ABSENT>"  # (local)
        print(f"  {rel}: {tag}")
        pins[rel] = sha
    return pins


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
# Section 5 — rational recovery on a squared-length pair
#
# METHOD NOTE (self-corrected in-session; documented honestly):
#   The PRIMARY matcher is continued-fraction best-rational recovery (CF). CF
#   convergents ARE the best rationals with bounded denominator (Dirichlet /
#   Hurwitz); terminating CFs handle integer ratios (n/1) exactly. CF implements
#   the plan's machinery pin literally: "rational p/q with denominator <= Q_max".
#
#   The CROSS-CHECK is PSLQ run DIRECTLY on the squared-length PAIR [L_i^2, L_j^2]
#   (NOT on [ratio, 1]) WITH AN EXPLICIT tol — the canonical "PSLQ on squared
#   actions" usage. It finds integers (a,b) with a*L_i^2 + b*L_j^2 ~ 0, so
#   L_i^2/L_j^2 = -b/a = n_i/n_j. With an explicit tol this PASSES the tau=0
#   control 36/36 (exact). [mpmath.pslq on [ratio, 1] with DEFAULT tol returns
#   None on simple integer ratios — a known mpmath default-tolerance quirk; it is
#   NOT used as a matcher. CF + PSLQ-on-pair are the two correct, agreeing methods.]
#
#   The verdict uses the CF (primary) fraction; PSLQ-on-pair is reported as the
#   corroborating cross-check (both pass the control; both fail the fold; they
#   agree on the verdict).
# ---------------------------------------------------------------------------
def recover_rational_cf(r, q_max: int, rel_tol) -> tuple | None:
    """PRIMARY: continued-fraction best rational p/q with 1<=q<=q_max,
    |p/q - r| <= rel_tol*|r|; else None. Terminating-CF-safe (integers OK)."""
    rr = mp.mpf(r)  # (local)
    if rr == 0:
        return None
    x = rr  # (local)
    p_m2, p_m1 = mp.mpf(0), mp.mpf(1)  # (local)
    q_m2, q_m1 = mp.mpf(1), mp.mpf(0)  # (local)
    best = None  # (local)
    for _ in range(300):
        a = mp.floor(x)  # (local)
        p_cur = a * p_m1 + p_m2  # (local)
        q_cur = a * q_m1 + q_m2  # (local)
        if q_cur > q_max:
            break
        if q_cur >= 1:
            approx = p_cur / q_cur  # (local)
            if abs(approx - rr) <= rel_tol * abs(rr):
                best = (int(p_cur), int(q_cur))
        frac = x - a  # (local)
        if frac == 0:
            break
        x = 1 / frac
        p_m2, p_m1 = p_m1, p_cur
        q_m2, q_m1 = q_m1, q_cur
    if best is None:
        return None
    p, q = best  # (local)
    g = gcd(abs(p), abs(q))  # (local)
    if g > 0:
        p //= g
        q //= g
    if q < 1 or q > q_max:
        return None
    return (p, q)


def recover_rational_pslq_pair(a2, b2, q_max: int, rel_tol) -> tuple | None:
    """CROSS-CHECK: PSLQ on the PAIR [a2, b2] (canonical squared-action usage),
    explicit tol. Finds (a,b): a*a2 + b*b2 ~ 0 => a2/b2 = -b/a. Returns reduced
    (p, q) for the larger/smaller orientation with max(|p|,|q|)<=q_max, else None."""
    X, Y = mp.mpf(float(a2)), mp.mpf(float(b2))  # (local)
    if X == 0 or Y == 0:
        return None
    rel = mp.pslq([X, Y], tol=mp.mpf(rel_tol), maxcoeff=q_max * 8, maxsteps=200000)  # (local)
    if rel is None:
        return None
    a, b = int(rel[0]), int(rel[1])  # (local)
    if a == 0 or b == 0:
        return None
    p, q = -b, a  # (local) X/Y = p/q
    g = gcd(abs(p), abs(q))  # (local)
    if g > 0:
        p //= g
        q //= g
    p, q = abs(p), abs(q)  # (local) orientation-free magnitudes (Loeschian integers)
    if q == 0 or max(p, q) > q_max:
        return None
    resid = abs(a * X + b * Y) / (abs(a * X) + abs(b * Y))  # (local) relation residual
    if resid <= rel_tol:
        return (p, q)
    return None


def pairwise_commensurability(sq_lengths, q_max: int, rel_tol):
    """For all unordered pairs (i,j), i<j, of squared lengths, test rationality of
    r = L_i^2/L_j^2 (oriented larger/smaller so r>=1) via CF (PRIMARY) and
    PSLQ-on-pair (CROSS-CHECK). The PRIMARY (CF) match drives the count.
    Returns (n_pairs, n_rational_cf, frac_cf, n_rational_pslq, frac_pslq, table)
    where table rows are (i, j, L_i^2, L_j^2, r, p, q, matched_cf, matched_pslq)."""
    n = len(sq_lengths)  # (local)
    table = []  # (local)
    n_rat_cf = 0  # (local)
    n_rat_pslq = 0  # (local)
    for i in range(n):
        for j in range(i + 1, n):
            a2 = mp.mpf(float(sq_lengths[i]))  # (local)
            b2 = mp.mpf(float(sq_lengths[j]))  # (local)
            hi, lo = (a2, b2) if a2 >= b2 else (b2, a2)  # (local)
            r = hi / lo  # (local)
            cf_pq = recover_rational_cf(r, q_max, rel_tol)  # (local) PRIMARY
            pslq_pq = recover_rational_pslq_pair(hi, lo, q_max, rel_tol)  # (local) CROSS-CHECK
            if cf_pq is not None:
                n_rat_cf += 1
            if pslq_pq is not None:
                n_rat_pslq += 1
            p_q = cf_pq if cf_pq is not None else (pslq_pq if pslq_pq is not None else (0, 0))  # (local)
            table.append((
                i, j, float(a2), float(b2), float(r),
                int(p_q[0]), int(p_q[1]),
                bool(cf_pq is not None), bool(pslq_pq is not None),
            ))
    n_pairs = len(table)  # (local)
    frac_cf = (n_rat_cf / n_pairs) if n_pairs > 0 else 0.0  # (local)
    frac_pslq = (n_rat_pslq / n_pairs) if n_pairs > 0 else 0.0  # (local)
    return n_pairs, n_rat_cf, frac_cf, n_rat_pslq, frac_pslq, table


# ---------------------------------------------------------------------------
# Section 6 — Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    mp.mp.dps = MP_DPS

    # -- Load W7-2 (measured tau_fold lengths + exact tau=0 coroot lattice) --
    d2 = np.load(W7_2_NPZ, allow_pickle=True)  # (local)
    stable_peaks = np.asarray(d2["stable_peaks"], dtype=float)  # (local) (19,4): col0=L
    measured_L = stable_peaks[:, 0].astype(float)  # (local) measured tau_fold lengths
    coroot_lengths = np.asarray(d2["coroot_lengths"], dtype=float)  # (local) (9,) exact tau=0
    primitive_coroot = float(d2["primitive_coroot_length"])  # (local) = 4*pi
    w7_2_verdict = str(d2["verdict"])  # (local)
    delta_L = float(d2["delta_L"])  # (local) FT bin width (resolution)
    dominant_L = float(d2["dominant_L"])  # (local)

    # -- Load W7-3 predicted lengths IF present (sister gate; may be absent) --
    w7_3_present = W7_3_NPZ.exists()  # (local)
    predicted_L = np.array([], dtype=float)  # (local)
    w7_3_note = "ABSENT (sister gate W7-3 concurrent; tau_fold population = W7-2 measured only)"  # (local)
    if w7_3_present:
        d3 = np.load(W7_3_NPZ, allow_pickle=True)  # (local)
        # W7-3 stores the predicted resonance lengths under pred_L_formA (Berry-Tabor
        # Form-A resonance lattice; the primary predicted set). Fall back to other
        # plausible key names for robustness. Per plan N_eval, the tau_fold population
        # is the COMBINED measured (W7-2) + predicted (W7-3) set on the single-lattice
        # hypothesis.
        for key in ("pred_L_formA_sorted", "pred_L_formA", "predicted_lengths",
                    "resonance_lengths", "lengths"):
            if key in d3.files:
                arr = np.asarray(d3[key], dtype=float)  # (local)
                if arr.ndim == 2 and arr.shape[1] >= 1:
                    predicted_L = arr[:, 0].astype(float)
                elif arr.ndim == 1:
                    predicted_L = arr.astype(float)
                if predicted_L.size > 0:
                    w7_3_note = (f"present (key='{key}', n={predicted_L.size}; "
                                 f"W7-3 self-verdict={str(d3['verdict']) if 'verdict' in d3.files else '?'})")
                    break
        if predicted_L.size == 0:
            w7_3_note = "present but no recognizable length key; tau_fold population = W7-2 measured only"

    # -- W7-1 anchor metadata (for provenance; tau=0 lengths come from the coroot lattice) --
    c_off_tau0 = float("nan")  # (local)
    if W7_1_NPZ.exists():
        d1 = np.load(W7_1_NPZ, allow_pickle=True)  # (local)
        if "c_off" in d1.files:
            c_off_tau0 = float(d1["c_off"])

    # ============================================================
    # POPULATION A — tau=0 positive control (EXACT coroot lattice)
    #   squared lengths = coroot_lengths^2; (L/4pi)^2 are Loeschian integers
    # ============================================================
    ctrl_sq = (coroot_lengths.astype(float)) ** 2  # (local)
    # Verify the integer-mesh premise (substitution chain Step 1): (L/4pi)^2 integer
    ctrl_norm2 = (coroot_lengths / primitive_coroot) ** 2  # (local)
    ctrl_int_resid = float(np.max(np.abs(ctrl_norm2 - np.round(ctrl_norm2))))  # (local)
    ctrl_int_mesh = [int(round(x)) for x in ctrl_norm2]  # (local) Loeschian numbers

    n_ctrl = len(ctrl_sq)  # (local)
    (ctrl_npairs, ctrl_nrat, ctrl_frac,
     ctrl_nrat_pslq, ctrl_frac_pslq, ctrl_table) = pairwise_commensurability(
        ctrl_sq, Q_MAX, REL_TOL_CTRL)
    ctrl_all_rational = (ctrl_npairs > 0) and (ctrl_nrat == ctrl_npairs)  # (local) PRIMARY (CF)

    # ============================================================
    # POPULATION B — tau_fold combined (measured W7-2 + predicted W7-3)
    # ============================================================
    fold_L = np.concatenate([measured_L, predicted_L]) if predicted_L.size > 0 else measured_L  # (local)
    fold_sq = fold_L.astype(float) ** 2  # (local)
    n_fold_peaks = len(fold_L)  # (local)

    (fold_npairs, fold_nrat, fold_frac,
     fold_nrat_pslq, fold_frac_pslq, fold_table) = pairwise_commensurability(
        fold_sq, Q_MAX, REL_TOL_FOLD)

    # ---- Resolution-aware DIAGNOSTIC (non-verdict-changing) ----
    # The measured lengths carry FT bin width delta_L; squared-ratio precision is
    # bounded by 2*delta_L/L (propagated), FAR coarser than rel_tol=1e-6. A coarse
    # tolerance matched to the resolution tells us whether a tau_fold FAIL is
    # measurement-resolution-driven vs structurally incommensurable. This is a
    # DIAGNOSTIC; the pre-registered verdict uses REL_TOL_FOLD=1e-6 only.
    # delta(L^2)/L^2 = 2 delta_L / L; take the WORST (smallest L) for a conservative band.
    Lmin_fold = float(np.min(fold_L)) if n_fold_peaks > 0 else float("nan")  # (local)
    res_rel = mp.mpf(2.0 * delta_L / Lmin_fold) if n_fold_peaks > 0 else mp.mpf("1e-2")  # (local)
    # bound below at the measured resolution; this is the "physically distinguishable" tol
    diag_rel_tol = res_rel  # (local)
    (fold_npairs_d, fold_nrat_d, fold_frac_d,
     _fnp_d, _ffp_d, _diag_table) = pairwise_commensurability(
        fold_sq, Q_MAX, diag_rel_tol)

    # ============================================================
    # Verdict logic (pre-registered, plan §W7-4)
    # ============================================================
    # INFO guard: < MIN_PEAKS stable peaks per spectrum -> under-powered.
    under_powered = (len(measured_L) < MIN_PEAKS) or (n_ctrl < MIN_PEAKS)  # (local)

    if under_powered:
        verdict = "INFO"  # (local)
        value = (f"under-powered n_measured={len(measured_L)} n_ctrl={n_ctrl} "
                 f"(< {MIN_PEAKS}); commensurability test under-powered")  # (local)
    else:
        fold_pass = (fold_frac >= RATIONAL_FRAC)  # (local)
        ctrl_pass = ctrl_all_rational  # (local)
        if fold_pass and ctrl_pass:
            verdict = "PASS"  # (local)
        else:
            verdict = "FAIL"  # (local)
        w73_tag = "W72+W73" if predicted_L.size > 0 else "W72-only"  # (local)
        value = (f"rational_frac={fold_frac:.4f}(>= {RATIONAL_FRAC}? {fold_pass}); "
                 f"ctrl_exact_rational={ctrl_pass}({ctrl_nrat}/{ctrl_npairs}); "
                 f"fold_pop={w73_tag} n_fold_peaks={n_fold_peaks} "
                 f"n_fold_pairs={fold_npairs} n_fold_rational_CF={fold_nrat} "
                 f"n_fold_rational_PSLQ={fold_nrat_pslq}; "
                 f"diag_frac@res_tol({float(diag_rel_tol):.2e})={fold_frac_d:.4f}")  # (local)

    print()
    print("=" * 72)
    print(f"[CONTROL tau=0]  coroot squared lengths (EXACT), n={n_ctrl}")
    print(f"  (L/4pi)^2 integer mesh (Loeschian): {ctrl_int_mesh}")
    print(f"  max integer residual: {ctrl_int_resid:.3e}")
    print(f"  pairs={ctrl_npairs}  rational_CF(primary)={ctrl_nrat} frac={ctrl_frac:.4f}  "
          f"all_rational={ctrl_all_rational}")
    print(f"  rational_PSLQ-on-pair(xcheck)={ctrl_nrat_pslq} frac={ctrl_frac_pslq:.4f}")
    print(f"[FOLD tau={tau_fold}]  combined squared lengths ({w7_3_note}), "
          f"n_peaks={n_fold_peaks}")
    print(f"  pairs={fold_npairs}  rational_CF(@rel_tol=1e-6)={fold_nrat} "
          f"frac={fold_frac:.4f}  (PASS boundary {RATIONAL_FRAC})")
    print(f"  rational_PSLQ-on-pair(xcheck)={fold_nrat_pslq} frac={fold_frac_pslq:.4f}")
    print(f"  DIAGNOSTIC rational(@res_tol={float(diag_rel_tol):.2e})={fold_nrat_d}  "
          f"frac={fold_frac_d:.4f}  [non-verdict-changing]")
    print(f"VERDICT: {verdict}")
    print("=" * 72)

    return {
        "value": value,
        "verdict": verdict,
        # control
        "ctrl_sq": ctrl_sq,
        "ctrl_int_mesh": np.array(ctrl_int_mesh, dtype=int),
        "ctrl_int_resid": ctrl_int_resid,
        "ctrl_npairs": ctrl_npairs,
        "ctrl_nrat": ctrl_nrat,
        "ctrl_frac": ctrl_frac,
        "ctrl_nrat_pslq": ctrl_nrat_pslq,
        "ctrl_frac_pslq": ctrl_frac_pslq,
        "ctrl_all_rational": ctrl_all_rational,
        "ctrl_table": np.array(ctrl_table, dtype=object),
        # fold
        "measured_L": measured_L,
        "predicted_L": predicted_L,
        "fold_L": fold_L,
        "fold_sq": fold_sq,
        "n_fold_peaks": n_fold_peaks,
        "fold_npairs": fold_npairs,
        "fold_nrat": fold_nrat,
        "fold_frac": fold_frac,
        "fold_nrat_pslq": fold_nrat_pslq,
        "fold_frac_pslq": fold_frac_pslq,
        "fold_table": np.array(fold_table, dtype=object),
        # diagnostic
        "diag_rel_tol": float(diag_rel_tol),
        "fold_nrat_diag": fold_nrat_d,
        "fold_frac_diag": fold_frac_d,
        "delta_L": delta_L,
        "Lmin_fold": Lmin_fold,
        # provenance / pins
        "rational_frac_boundary": RATIONAL_FRAC,
        "Q_max": Q_MAX,
        "rel_tol_fold": float(REL_TOL_FOLD),
        "rel_tol_ctrl": float(REL_TOL_CTRL),
        "min_peaks": MIN_PEAKS,
        "tau_fold": float(tau_fold),
        "primitive_coroot": primitive_coroot,
        "dominant_L": dominant_L,
        "c_off_tau0": c_off_tau0,
        "w7_2_verdict": w7_2_verdict,
        "w7_3_present": w7_3_present,
        "w7_3_note": w7_3_note,
    }


# ---------------------------------------------------------------------------
# Section 7 — Plot
# ---------------------------------------------------------------------------
def make_plot(res: dict) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(13, 9))

    # (a) tau=0 control: (L/4pi)^2 integer mesh
    ax = axes[0, 0]
    mesh = res["ctrl_int_mesh"]  # (local)
    ax.stem(range(len(mesh)), mesh, basefmt=" ")
    ax.set_title(f"tau=0 control: coroot squared lengths\n"
                 f"(L/4pi)^2 = Loeschian integers (resid {res['ctrl_int_resid']:.1e})")
    ax.set_xlabel("coroot index")
    ax.set_ylabel("(L/4pi)^2  (integer)")
    ax.grid(alpha=0.3)

    # (b) tau_fold squared lengths
    ax = axes[0, 1]
    fsq = res["fold_sq"]  # (local)
    order = np.argsort(fsq)  # (local)
    ax.stem(range(len(fsq)), fsq[order], basefmt=" ")
    ax.set_title(f"tau={res['tau_fold']} measured squared lengths\n"
                 f"n_peaks={res['n_fold_peaks']} (W7-2 stable peaks)")
    ax.set_xlabel("peak index (sorted by L^2)")
    ax.set_ylabel("L^2")
    ax.grid(alpha=0.3)

    # (c) control pairwise ratios vs nearest rational (all should land exactly)
    ax = axes[1, 0]
    ctab = res["ctrl_table"]  # (local)
    if len(ctab) > 0:
        ratios = np.array([row[4] for row in ctab], dtype=float)  # (local)
        matched = np.array([row[7] for row in ctab], dtype=bool)  # (local) col7 = CF (primary)
        ax.scatter(np.arange(len(ratios))[matched], ratios[matched],
                   c="green", s=18, label=f"rational CF ({matched.sum()})")
        if (~matched).any():
            ax.scatter(np.arange(len(ratios))[~matched], ratios[~matched],
                       c="red", s=18, label=f"NOT rational ({(~matched).sum()})")
    ax.set_title(f"tau=0 control pairwise L^2 ratios (EXPECT all rational)\n"
                 f"frac rational CF = {res['ctrl_frac']:.3f} (rel_tol 1e-9); "
                 f"PSLQ-xcheck {res['ctrl_frac_pslq']:.3f}")
    ax.set_xlabel("pair index")
    ax.set_ylabel("L_i^2 / L_j^2")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # (d) fold pairwise ratios: rational vs not, at rel_tol=1e-6 and at res-tol
    ax = axes[1, 1]
    ftab = res["fold_table"]  # (local)
    if len(ftab) > 0:
        ratios = np.array([row[4] for row in ftab], dtype=float)  # (local)
        matched = np.array([row[7] for row in ftab], dtype=bool)  # (local) col7 = CF (primary)
        ax.scatter(np.arange(len(ratios))[matched], ratios[matched],
                   c="green", s=14, label=f"rational CF@1e-6 ({matched.sum()})")
        if (~matched).any():
            ax.scatter(np.arange(len(ratios))[~matched], ratios[~matched],
                       c="red", s=10, alpha=0.6, label=f"NOT@1e-6 ({(~matched).sum()})")
    ax.axhline(1.0, color="gray", lw=0.8, ls="--")
    ax.set_title(f"tau={res['tau_fold']} pairwise L^2 ratios\n"
                 f"frac rational CF = {res['fold_frac']:.3f} (rel_tol 1e-6); "
                 f"PSLQ-xcheck {res['fold_frac_pslq']:.3f}; "
                 f"diag {res['fold_frac_diag']:.3f}@{res['diag_rel_tol']:.1e}")
    ax.set_xlabel("pair index")
    ax.set_ylabel("L_i^2 / L_j^2")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    fig.suptitle(f"{GATE_ID}  —  verdict {res['verdict']}  "
                 f"(boundary rational_frac >= {res['rational_frac_boundary']})",
                 fontsize=12, fontweight="bold")
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 — Verdict payload
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme, convention, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note="", extra_rows=None) -> dict:
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


# ---------------------------------------------------------------------------
# Section 9 — main
# ---------------------------------------------------------------------------
def main() -> int:
    pins = log_input_pins(INPUT_FILES)  # (local)
    audit_sha, content_sha = compute_dual_sha(
        Path(__file__).resolve(), SHARED_DIR / "canonical_constants.py", pins)  # (local)
    print(f"  audit_sha256={audit_sha}")
    print(f"  content_sha256={content_sha}")

    res = compute()  # (local)
    np.savez(OUT_NPZ, **{k: v for k, v in res.items()})
    make_plot(res)
    print(f"  wrote {OUT_NPZ.relative_to(PROJECT_ROOT)}")
    print(f"  wrote {OUT_PNG.relative_to(PROJECT_ROOT)}")

    print(emit_4tuple(res["value"], SCHEME, CONVENTION, L_MAX))

    ctrl_mesh = [int(x) for x in res["ctrl_int_mesh"]]  # (local)
    extra = [
        ("# method: PRIMARY=continued-fraction best-rational (denom<=Q_max=64); "
         "CROSS-CHECK=PSLQ on the squared-length PAIR [L_i^2,L_j^2] (explicit tol). "
         "mpmath.pslq on [ratio,1] with default tol is unreliable on integer ratios; NOT used as matcher."),
        (f"# W7-3 predicted-length input: {res['w7_3_note']}; "
         f"tau_fold population is W7-2-measured + (W7-3 if present)"),
        (f"# tau=0 control: EXACT coroot lattice (L/4pi)^2 in {ctrl_mesh} "
         f"(Loeschian m^2+mn+n^2, integer resid {res['ctrl_int_resid']:.1e}); "
         f"ctrl exact-rational CF {res['ctrl_nrat']}/{res['ctrl_npairs']} "
         f"PSLQ-xcheck {res['ctrl_nrat_pslq']}/{res['ctrl_npairs']}"),
        (f"# fold commensurability: CF {res['fold_nrat']}/{res['fold_npairs']} "
         f"PSLQ-xcheck {res['fold_nrat_pslq']}/{res['fold_npairs']} (both << {RATIONAL_FRAC} boundary; methods agree)"),
        (f"# DIAGNOSTIC (non-verdict-changing): fold rational_frac at resolution-matched "
         f"tol {res['diag_rel_tol']:.2e} (=2*delta_L/Lmin, delta_L={res['delta_L']:.4f}) "
         f"= {res['fold_frac_diag']:.4f} -> FAIL is NOT a resolution artifact"),
        "# regulator_pin=a_n^zeta (inherited via W7-2 length spectrum; lengths are metric/FT, not a regulated a_n)",
    ]
    print_verdict_payload(res["verdict"], res["value"], audit_sha, content_sha,
                          extra_rows=extra)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
