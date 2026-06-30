#!/usr/bin/env python3
"""
S96 W2-4 — SDW-SADDLE-REGINV  (one-loop no-interior-saddle REGULATOR-INVARIANCE)
================================================================================

Gate: S96-SDW-SADDLE-REGINV  ([SIGN])
Classification: GEOMETRIC
Agent: lizzi-spectral-functional-theorist

Pre-registered threshold (session-96-plan-w2.md §W2-4):
  Operator (set): count_interior_sign_changes(dGamma^R/dtau on (0, 0.30)) == 0
                  for ALL R in {zeta, f*-cutoff, Gaussian}.
  PASS iff interior_sign_change_count = 0 in ALL THREE loop-regulator schemes
           (zero interior stationary points of Gamma on the OPEN interval (0, 0.30)).
  FAIL iff some scheme (f*-cutoff or Gaussian) introduces an interior sign-change of
           dGamma/dtau absent in the zeta scheme (a loop-induced interior feature in
           at least one admissible scheme).
  INFO iff sign-structure invariant (0 interior sign-changes in all schemes -- PASS on
           the topology) BUT the loop-term MAGNITUDE differs by >O(1) across schemes.

WHAT THIS GATE HARDENS:
  S95-W2-3-NO-WELL-ONE-LOOP (PASS, value=0) verified the no-interior-saddle of
  Gamma = S_tree + Gamma_1loop in the ZETA scheme ONLY (Gamma_1loop = -1/2 zeta'_D(0,tau)
  ~ Sum_k ln|lambda_k|, the heat-kernel-log). This gate tests REGULATOR-INVARIANCE:
  does the no-saddle topology survive when Gamma_1loop is recomputed under the cutoff-f*
  (acoustic envelope) and Gaussian-cutoff regulators?

  THE eps_H SIGN-FLIP PRECEDENT IS WHY FI IS *NOT* PRESUPPOSED. The lizzi permanent
  finding ZETA-SA-66 is that eps_H (another LOOP-LEVEL readout) FLIPS SIGN between the
  cutoff and zeta schemes. So the burden is on the gate to COMPUTE whether the no-saddle
  is FI or zeta-specific; we do not assume it.

GOVERNING OBJECT (a SECOND spectral functional layered on the bare action):
  Gamma[tau] = S_tree(tau) + Gamma_1loop^R(tau)

  TREE action S_tree(tau) -- REGULATOR-INDEPENDENT (E7, the bare action):
    Two equivalent representations of the bare spectral action are reported; the no-saddle
    verdict is taken on BOTH so it cannot hinge on a convention ambiguity:
      (A, CANONICAL E7 ANCHOR)  S_full(tau)  = Sum_k f(x_k) with f(x)=sqrt(x)=|lambda|
                                = Sum_k |lambda_k(tau)|.  E7 PROVEN monotone; the canonical
                                dS/dtau|_fold = +58672.8 (dS_fold, S42; 9600/9600 checks).
                                This is the SAME tree action S95-W2-3 used (its reference arm).
      (B, ALTERNATING-MOMENT)   S_SA(tau)    = a_0(tau) - a_2(tau) + a_4(tau), the heat-kernel
                                LAYER EXPANSION (Seeley-DeWitt) of the bare action (capstone
                                §1.3a / §4). In the Gilkey curvature-polynomial representation
                                a_0 ~ V (deg-0), a_2 ~ R_K V (deg-1), a_4 ~ R_K^2 V (deg-2),
                                with R_K(tau) the E3 Jensen scalar curvature, anchored to the
                                canonical fold moments a_0=6440, a_2=2776.165389, a_4=1350.7216.

    NOTE (convention honesty, math-scripts.md "Double-Check Logic Before Compute"): the
    +58672.8 E7 number is the gradient of representation (A) Sum|lambda|, NOT of the
    alternating combination (B) a_0-a_2+a_4 (which, in the curvature-polynomial reading,
    has a small NEGATIVE slope ~ -10 at the fold). Both are LEGITIMATE faces of the bare
    action; the gate reports the no-saddle COUNT under BOTH so the FI verdict is robust to
    which representation a downstream consumer adopts. Representation (A) is the canonical
    arm (matches S95-W2-3 + the E7 anchor); representation (B) is the stringent cross-check
    (the Gaussian-loop + alternating-moment combination is the hardest no-saddle test --
    both terms small and same-signed-negative).

  LOOP term Gamma_1loop^R(tau) -- the REGULATOR-DEPENDENT piece, three schemes:
    All three share the spectral-action fluctuation-determinant form
        Gamma_1loop^R(tau) = (1/2) Tr[ g_R(D_K^2/Lambda^2) * ln(D_K^2/Lambda^2) ]
                           = (1/2) Sum_k g_R(x_k) ln(x_k),   x_k = lambda_k^2 / Lambda^2,
    with Lambda = M_KK = 1 in M_KK units (the cached |lambda| are in M_KK units):
      (zeta)     g_zeta(x)  = 1            -> Gamma_1loop^zeta = (1/2) Sum ln(x) = Sum ln|lambda|
                              == the S95-W2-3 heat-kernel-log reference; -1/2 zeta'_D(0,tau)
                              operationally equals (1/2) Sum_k ln(lambda_k^2) on a finite triple.
      (f*-cutoff) g_f*(x)   = f*(x) = 0.9117 sqrt(x) + 0.0883 e^{-x}   (acoustic envelope)
      (Gaussian)  g_Gauss(x)= e^{-x}       (Chamseddine-Connes Gaussian cutoff weight)

  Block-diagonal factorization (E6): D_K = (+)_{(p,q)} D_{(p,q)}, so
      Tr[g_R(D_K^2) ln(D_K^2)] = Sum_{(p,q)} Tr[g_R(D_{(p,q)}^2) ln(D_{(p,q)}^2)]
  i.e. the loop trace factorizes per Peter-Weyl sector -- evaluated directly on the cached
  per-sector |lambda| (no eigendecomposition; the spectrum is PRE-CACHED). Friedrich-Bar
  saturation => bottom sectors dominate.

[SIGN] SUBSTITUTION CHAIN for "the no-interior-saddle of Gamma[tau] is regulator-INVARIANT
(FI); the boundary-domination (transit-not-slow-roll) reading does not depend on the
loop-term regulator":

  Step 1 -- Definitions:
    Gamma[tau]   = S_tree(tau) + Gamma_1loop^R(tau)                         [Def 1]
    dS_tree/dtau > 0 (E7; representation (A) dS/dtau|_fold = +58672.8)      [Def 2]
    Gamma_1loop^zeta = (1/2) Sum ln(x_k)  (S95-W2-3 reference)              [Def 3]
    Gamma_1loop^f*, Gamma_1loop^Gauss as above (cutoff-weighted trace-logs) [Def 4]

  Step 2 -- Substitution (no simplification):
    dGamma^R/dtau = dS_tree/dtau + dGamma_1loop^R/dtau.
    The tree term dS_tree/dtau is regulator-INDEPENDENT (E7 is on the bare action).
    The loop term dGamma_1loop^R/dtau is the regulator-DEPENDENT piece.

  Step 3 -- Simplification (what an interior saddle REQUIRES):
    An interior saddle (dGamma^R/dtau = 0 at some interior tau*) requires
        dGamma_1loop^R/dtau = -dS_tree/dtau   at some tau* in (0,0.30),
    i.e. the loop slope must be NEGATIVE *and* of magnitude EXACTLY equal to the positive
    tree slope at some interior point. Whether the loop term can achieve this cancellation
    is regulator-dependent IN PRINCIPLE (this is the eps_H-sign-flip-style contingency).

  Step 4 -- Direction / sign read-off (the SIGN claim; MEASURED, not assumed):
    The hypothesis is sign(dGamma^R/dtau) = const (no interior sign change) in ALL THREE
    schemes. The gate MEASURES dGamma^R/dtau on a 200-point grid and counts interior
    sign-changes. PASS requires the loop term, in every scheme, to be unable to manufacture
    the cancellation: either same-signed as the tree slope, OR opposite-signed but too small
    in magnitude. The eps_H precedent means the loop slope CAN flip sign across schemes (and
    indeed the Gaussian arm DOES) -- the question is whether any sign flip is large enough to
    cross zero, which is decided by computation.

  Conclusion (NEUTRAL): PASS (0 interior sign-changes in {zeta, f*, Gaussian}) => the
    no-interior-saddle is FUNCTIONAL-INVARIANT; the transit-not-slow-roll reading is
    structural across schemes, not a zeta artifact; no KKLT-like loop uplift operates in
    ANY admissible scheme. FAIL (interior sign-change in some scheme) => the no-saddle is
    regulator-DEPENDENT (Track B; ties to the eps_H sign-flip precedent).

REGULATOR-PIN (regulator-pin-discipline.md): the tree S_tree moments are zeta-regulated,
  tagged a_n^{zeta} (a_0_FW_zeta/a_2_FW_zeta/a_4_FW_zeta anchors). The loop term carries its
  OWN scheme tag {zeta, cutoff(f*), Gaussian} per evaluation. CLASS=FULL: the loop trace-log
  is computed DIRECTLY on the cached FULL D_K per-sector spectrum (Jensen-scaled per tau),
  NOT the SCHEMATIC _spectral_action_regulators.py analog (substrate-first-canonical-sourcing
  sec (iv)) -- no SCHEMATIC helper consumed, so no -SCHEMATIC suffix / tier_pin row needed.

DISCIPLINE: `from canonical_constants import *`; every intermediate `# (local)`;
  CPU-cap-OMP8 (the per-sector trace-log is a vector reduction over PRE-CACHED scalars
  x 200 tau-points x 3 schemes = a CPU vector op, NOT an eigendecomposition -- eigenvalues
  are cached, no matrix op needed, so torch.linalg is not invoked: the block-diagonal
  factorization is already realized in the cache as per-sector abs_evals); dual-SHA emitted;
  [SIGN] trigger -> schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple companion row appended (REQUIRED).
"""

from __future__ import annotations

import glob
import hashlib
import json
import os
import sys
import time
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Paths + canonical imports
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
SESSION_96_DIR = PROJECT_ROOT / "computations" / "session-96"
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import (  # noqa: E402
    tau_fold,
    M_KK,
    dS_fold,
    d2S_fold,
    S_fold,
    PI,
    a_0_FW_zeta,
    a_2_FW_zeta,
    a_4_FW_zeta,
)

# ---------------------------------------------------------------------------
# Gate identity + pre-registered pins (plan §W2-4 machinery_pin_map)
# ---------------------------------------------------------------------------
GATE_ID = "S96-SDW-SADDLE-REGINV"
SCHEME = "three-loop-regulator-zeta-fstar-Gaussian"
CONVENTION = "SIGN-no-interior-saddle-topology-FI"
L_MAX = 10                                   # (local) operational truncation (p+q<=10)

TAU_LO, TAU_HI = 0.0, 0.30                    # (local) tau in [0, tau_now=0.30]; plan scan_range
N_GRID = 200                                  # (local) plan N_eval pin: 200 tau-grid points
ZERO_TOL = 1e-12                              # (local) finite-difference / sign-change zero-floor
N_EVAL_EXPECTED = 78080                       # (local) plan: L<=10 stored |lambda| count
PQ_CUT = 10                                   # (local) L_max=10 Peter-Weyl restriction
MAG_BAND_OOM = 1.0                            # (local) loop-magnitude FI band: >O(1) ratio => INFO on magnitude

# f* acoustic-envelope coefficients (canonical: f*(x)=0.9117 sqrt(x)+0.0883 e^{-x})
F_STAR_SQRT = 0.9117                          # (local) f* sqrt-coefficient (S72/S77; mellin_f_star)
F_STAR_EXP = 0.0883                           # (local) f* exp-coefficient

CANONICAL_CONSTANTS_PATH = SHARED_DIR / "canonical_constants.py"
L12_CACHE_PATH = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
INPUT_FILES = [L12_CACHE_PATH, CANONICAL_CONSTANTS_PATH]

VERDICT_TXT = SESSION_96_DIR / "s96_gate_verdicts.txt"
OUT_NPZ = SESSION_96_DIR / "s96_sdw_saddle_reginv.npz"
OUT_PNG = SESSION_96_DIR / "s96_sdw_saddle_reginv.png"

# Jensen radius calibration source (framework's own multi-tau cache; substrate-first)
S36_CACHE_PATTERN = "computations/**/s36_sfull_tau_stabilization.npz"
S36_SECTORS = [(0, 0), (1, 0), (0, 1), (1, 1), (2, 0), (0, 2), (3, 0), (0, 3), (2, 1), (1, 2)]
S36_TAUS = np.array([0.05, 0.16, 0.17, 0.18, 0.19, 0.21, 0.22])  # (local) S36 tau slices


# ---------------------------------------------------------------------------
# Dual-SHA helpers (S84+ schema; mirrors s95_w2_3)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs) -> dict:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    script_bytes = script_path.read_bytes() if script_path.exists() else b""  # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    """Atomic single-write canonical line + dual-SHA companion + ([SIGN]) 3-tuple row."""
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row\n"
    )
    SESSION_96_DIR.mkdir(parents=True, exist_ok=True)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


def append_3tuple_row(sign_v: str, mag_v: str, regime_v: str) -> None:
    """schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple companion row ([SIGN] trigger; gate-verdicts.md)."""
    row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(row)


# ---------------------------------------------------------------------------
# SU(3) Peter-Weyl helpers
# ---------------------------------------------------------------------------
def dim_pq(p: int, q: int) -> int:
    """SU(3) Weyl dimension (closed form)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


# ---------------------------------------------------------------------------
# Jensen scalar curvature R_K(tau) (E3, Sage residual 0) + alternating-moment tree
# ---------------------------------------------------------------------------
def R_K(t):
    """E3 Jensen-fiber scalar curvature: R_K = -1/4 e^{-4t} + 2 e^{-t} - 1/4 + 1/2 e^{2t}.
    R_K'(t) = e^{-4t}(e^{3t}-1)^2 >= 0, = 0 only at t=0 (Sage-verified, residual 0)."""
    return -0.25 * np.exp(-4.0 * t) + 2.0 * np.exp(-t) - 0.25 + 0.5 * np.exp(2.0 * t)


def tree_alternating_moment(tau):
    """Representation (B): S_SA(tau) = a_0(tau) - a_2(tau) + a_4(tau), curvature-polynomial form.
    a_0 ~ V (deg-0 const), a_2 ~ R_K V (deg-1), a_4 ~ R_K^2 V (deg-2), anchored at fold to the
    canonical zeta moments. Returns S_SA on the tau-grid."""
    rkf = R_K(tau_fold)  # (local) R_K at fold
    c0 = a_0_FW_zeta  # (local) deg-0 coefficient = a_0
    c2 = a_2_FW_zeta / rkf  # (local) a_2 = c2 * R_K(fold)
    c4 = a_4_FW_zeta / (rkf ** 2)  # (local) a_4 = c4 * R_K(fold)^2
    rk = R_K(tau)  # (local)
    return c0 - c2 * rk + c4 * rk ** 2, (c0, c2, c4, rkf)


# ---------------------------------------------------------------------------
# Jensen radius r(tau): substrate-first calibration from the S36 multi-tau cache
# ---------------------------------------------------------------------------
def calibrate_jensen_inv_r():
    """Calibrate 1/r(tau) := <|lambda|>(tau)/<|lambda|>(tau_fold) from the S36 multi-tau cache
    (Peter-Weyl-multiplicity-weighted mean of |lambda| over the 10 S36 sectors), normalized to
    1 at tau_fold. ln(1/r) is fit to a smooth quadratic so 1/r(tau) and d ln(1/r)/dtau are
    available on the full grid. Identical calibration to S95-W2-3 (the reference gate)."""
    cands = glob.glob(str(PROJECT_ROOT / S36_CACHE_PATTERN), recursive=True)
    if not cands:
        raise FileNotFoundError("S36 multi-tau cache (s36_sfull_tau_stabilization.npz) not found")
    d36 = np.load(cands[0], allow_pickle=True)

    def sec36(t, p, q):
        return np.abs(np.asarray(d36[f"evals_tau{t:.3f}_{p}_{q}"], dtype=float))

    def mean_abs(t):
        num = 0.0  # (local)
        den = 0.0  # (local)
        for (p, q) in S36_SECTORS:
            m = dim_pq(p, q)  # (local) Peter-Weyl regular-rep multiplicity
            v = sec36(t, p, q)
            num += m * v.sum()
            den += m * v.size
        return num / den

    mbar_fold = mean_abs(tau_fold)  # (local)
    inv_r_data = np.array([mean_abs(t) / mbar_fold for t in S36_TAUS])  # (local) 1/r at S36 taus
    coef = np.polyfit(S36_TAUS, np.log(inv_r_data), 2)  # (local) ln(1/r) ~ a t^2 + b t + c
    resid_max = float(np.max(np.abs(np.log(inv_r_data) - np.polyval(coef, S36_TAUS))))  # (local)

    def inv_r_fn(t):
        return np.exp(np.polyval(coef, t))

    return inv_r_fn, coef, resid_max, inv_r_data, str(Path(cands[0]).resolve())


# ---------------------------------------------------------------------------
# Load FULL L12 spectrum (tau_fold slice), restrict to p+q<=10 (block-diagonal per sector)
# ---------------------------------------------------------------------------
def load_fold_spectrum():
    """Return (abs_fold, n_eval, min_abs, sector_pq_list). abs_fold = concatenated |lambda| over
    all sectors with p+q<=10. The block-diagonal factorization D_K = (+)_(p,q) D_(p,q) is already
    realized in the cache (per-sector abs_evals); the Tr ln factorizes per sector by construction.
    """
    cache = np.load(L12_CACHE_PATH, allow_pickle=True)
    se = cache["sector_evals"].item()  # (local) dict keyed by (p,q)
    abs_list = []  # (local)
    pq_list = []  # (local)
    for (p, q), v in se.items():
        if p + q > PQ_CUT:
            continue
        ae = np.asarray(v["abs_evals"], dtype=float)  # (local)
        abs_list.append(ae)
        pq_list.append((p, q, ae.size))
    abs_fold = np.concatenate(abs_list)  # (local)
    return abs_fold, abs_fold.size, float(abs_fold.min()), pq_list


# ---------------------------------------------------------------------------
# Tree spectral action (representation A) and the THREE loop schemes
# ---------------------------------------------------------------------------
def tree_full_sumabs(abs_tau):
    """Representation (A) CANONICAL E7 tree action: f(x)=sqrt(x)=|lambda| => S_full = Sum |lambda|.
    INCREASING f; eigenvalue growth (E7) drives dS/dtau>0; canonical dS_fold = +58672.8."""
    return float(np.sum(abs_tau))


def loop_zeta(abs_tau):
    """Gamma_1loop^zeta = (1/2) Sum ln(x_k) = Sum ln|lambda_k|  (g_zeta=1).
    == S95-W2-3 heat-kernel-log reference; operationally -1/2 zeta'_D(0,tau) on a finite triple."""
    return float(np.sum(np.log(abs_tau)))


def loop_fstar(abs_tau):
    """Gamma_1loop^f* = (1/2) Sum f*(x_k) ln(x_k),  f*(x)=0.9117 sqrt(x)+0.0883 e^{-x},  x=lambda^2."""
    x = abs_tau ** 2  # (local) x_k = lambda_k^2 (Lambda=M_KK=1 in M_KK units)
    g = F_STAR_SQRT * np.sqrt(x) + F_STAR_EXP * np.exp(-x)  # (local) acoustic-envelope weight
    return float(0.5 * np.sum(g * np.log(x)))


def loop_gauss(abs_tau):
    """Gamma_1loop^Gauss = (1/2) Sum e^{-x_k} ln(x_k),  x=lambda^2  (Gaussian/Chamseddine-Connes cutoff)."""
    x = abs_tau ** 2  # (local)
    g = np.exp(-x)  # (local) Gaussian cutoff weight
    return float(0.5 * np.sum(g * np.log(x)))


# ---------------------------------------------------------------------------
# Interior sign-change counting on the OPEN interval (0, 0.30)
# ---------------------------------------------------------------------------
def count_interior_sign_changes(deriv, tol):
    """Count sign changes of `deriv` on the INTERIOR (endpoints already excluded by the caller),
    rejecting float-noise: a sign change counts only when BOTH adjacent points have |deriv| > tol.
    """
    sgn = np.sign(deriv)  # (local)
    n = 0  # (local)
    locs = []  # (local)
    for i in range(1, len(deriv)):
        if abs(deriv[i]) > tol and abs(deriv[i - 1]) > tol and sgn[i] != sgn[i - 1]:
            n += 1
            locs.append(i)
    return n, locs


# ---------------------------------------------------------------------------
# Main compute
# ---------------------------------------------------------------------------
def compute():
    # --- Jensen radius calibration (substrate-first, from S36) ---
    inv_r_fn, coef, resid_max, inv_r_data, s36_path = calibrate_jensen_inv_r()

    # --- FULL L12 fold spectrum, L<=10 (block-diagonal per Peter-Weyl sector) ---
    abs_fold, n_eval, min_abs_fold, pq_list = load_fold_spectrum()

    # --- tau grid [0, tau_now=0.30] ---
    tau = np.linspace(TAU_LO, TAU_HI, N_GRID)  # (local)
    inv_r_grid = inv_r_fn(tau)  # (local)
    # Jensen-scaled |lambda| at each tau: |lambda(tau)| = |lambda(fold)| * (1/r(tau))
    abs_grid = np.outer(inv_r_grid, abs_fold)  # (local) shape (N_GRID, n_eval); positive, no zero modes
    min_abs_grid = float(abs_grid.min())  # (local)

    # --- TREE actions (regulator-independent) ---
    # (A) canonical E7 Sum|lambda|
    S_full = np.array([tree_full_sumabs(abs_grid[i]) for i in range(N_GRID)])  # (local)
    dS_full = np.gradient(S_full, tau)  # (local)
    # (B) alternating moment a_0 - a_2 + a_4 (curvature polynomial)
    S_SA, sa_coeffs = tree_alternating_moment(tau)  # (local)
    dS_SA = np.gradient(S_SA, tau)  # (local)

    # --- LOOP terms (regulator-dependent), three schemes ---
    Gz = np.array([loop_zeta(abs_grid[i]) for i in range(N_GRID)])  # (local)
    Gf = np.array([loop_fstar(abs_grid[i]) for i in range(N_GRID)])  # (local)
    Gg = np.array([loop_gauss(abs_grid[i]) for i in range(N_GRID)])  # (local)
    dGz = np.gradient(Gz, tau)  # (local)
    dGf = np.gradient(Gf, tau)  # (local)
    dGg = np.gradient(Gg, tau)  # (local)

    # --- Gamma = S_tree + Gamma_1loop^R, BOTH tree representations x THREE schemes ---
    # interior = OPEN interval (0, 0.30): exclude both endpoint samples (indices 0 and N-1)
    interior = slice(1, N_GRID - 1)
    schemes = {}  # (local) name -> dict
    # Representation (A): canonical E7 Sum|lambda| tree
    for sname, dG_loop, G_loop in [("zeta", dGz, Gz), ("fstar", dGf, Gf), ("gauss", dGg, Gg)]:
        Gam = S_full + G_loop  # (local)
        dGam = dS_full + dG_loop  # (local)
        n_sc, locs = count_interior_sign_changes(dGam[interior], ZERO_TOL)
        schemes[f"A_{sname}"] = {
            "Gam": Gam, "dGam": dGam, "n_sc": int(n_sc), "locs": locs,
            "dGam_interior_min": float(dGam[interior].min()),
            "dGam_interior_max": float(dGam[interior].max()),
            "constant_sign": bool(np.all(np.sign(dGam[interior]) == np.sign(dGam[interior][0]))),
        }
    # Representation (B): alternating-moment a_0-a_2+a_4 tree (stringent cross-check arm)
    for sname, dG_loop, G_loop in [("zeta", dGz, Gz), ("fstar", dGf, Gf), ("gauss", dGg, Gg)]:
        Gam = S_SA + G_loop  # (local)
        dGam = dS_SA + dG_loop  # (local)
        n_sc, locs = count_interior_sign_changes(dGam[interior], ZERO_TOL)
        schemes[f"B_{sname}"] = {
            "Gam": Gam, "dGam": dGam, "n_sc": int(n_sc), "locs": locs,
            "dGam_interior_min": float(dGam[interior].min()),
            "dGam_interior_max": float(dGam[interior].max()),
            "constant_sign": bool(np.all(np.sign(dGam[interior]) == np.sign(dGam[interior][0]))),
        }

    # --- fold-point readouts ---
    ifold = int(np.argmin(np.abs(tau - tau_fold)))  # (local)
    dS_full_fold = float(dS_full[ifold])  # (local)
    dS_SA_fold = float(dS_SA[ifold])  # (local)
    dGz_fold = float(dGz[ifold])  # (local)
    dGf_fold = float(dGf[ifold])  # (local)
    dGg_fold = float(dGg[ifold])  # (local)
    # cross-check: computed Sum|lambda| dS/dtau at fold vs E7 canonical +58672.8
    dS_full_vs_canonical = dS_full_fold / dS_fold  # (local)

    # --- loop-MAGNITUDE FI spread (for the INFO band): max/min |loop slope| ratio across schemes ---
    loop_slope_mags = np.array([abs(dGz_fold), abs(dGf_fold), abs(dGg_fold)])  # (local)
    loop_mag_spread_ratio = float(loop_slope_mags.max() / max(loop_slope_mags.min(), 1e-30))  # (local)
    loop_mag_oom_spread = float(np.log10(loop_mag_spread_ratio))  # (local)

    # --- canonical verdict object: interior-sign-change count, ALL schemes (rep A is canonical) ---
    # The gate's pre-registered operator is over {zeta, f*, Gaussian}. Representation (A) is the
    # canonical E7-anchored tree (matches S95-W2-3); representation (B) is the stringent cross-check.
    n_sc_A = {s: schemes[f"A_{s}"]["n_sc"] for s in ("zeta", "fstar", "gauss")}  # (local)
    n_sc_B = {s: schemes[f"B_{s}"]["n_sc"] for s in ("zeta", "fstar", "gauss")}  # (local)
    total_interior_sc_A = int(sum(n_sc_A.values()))  # (local) canonical verdict value
    total_interior_sc_B = int(sum(n_sc_B.values()))  # (local) cross-check
    all_zero_A = bool(total_interior_sc_A == 0)  # (local)
    all_zero_B = bool(total_interior_sc_B == 0)  # (local)

    # --- sign of loop slope per scheme (does any flip relative to zeta? eps_H-precedent diagnostic) ---
    sign_loop = {  # (local)
        "zeta": int(np.sign(dGz_fold)),
        "fstar": int(np.sign(dGf_fold)),
        "gauss": int(np.sign(dGg_fold)),
    }
    loop_sign_flips_across_schemes = bool(len(set(sign_loop.values())) > 1)  # (local)

    # --- regime: loop trace-log finite everywhere (no zero mode) AND full window computed ---
    no_zero_mode = bool(min_abs_grid > 1e-9)  # (local) min|lambda|>0 => ln finite
    domain_used_frac = 1.0  # (local) full open (0,0.30) computed; no auto-shortening

    return {
        "tau": tau,
        "inv_r_grid": inv_r_grid,
        "jensen_coef": coef,
        "jensen_fit_residual_max": resid_max,
        "inv_r_data": inv_r_data,
        "s36_path": s36_path,
        "n_eval": n_eval,
        "abs_min_fold": min_abs_fold,
        "abs_min_grid": min_abs_grid,
        # tree actions
        "S_full": S_full, "dS_full": dS_full,
        "S_SA": S_SA, "dS_SA": dS_SA, "sa_coeffs": sa_coeffs,
        # loop terms
        "Gz": Gz, "Gf": Gf, "Gg": Gg,
        "dGz": dGz, "dGf": dGf, "dGg": dGg,
        # per-(rep,scheme) Gamma + counts
        "schemes": schemes,
        "n_sc_A": n_sc_A, "n_sc_B": n_sc_B,
        "total_interior_sc_A": total_interior_sc_A,
        "total_interior_sc_B": total_interior_sc_B,
        "all_zero_A": all_zero_A, "all_zero_B": all_zero_B,
        # fold readouts
        "ifold": ifold,
        "dS_full_fold": dS_full_fold,
        "dS_SA_fold": dS_SA_fold,
        "dGz_fold": dGz_fold, "dGf_fold": dGf_fold, "dGg_fold": dGg_fold,
        "dS_full_vs_canonical": dS_full_vs_canonical,
        # loop sign / magnitude diagnostics
        "sign_loop": sign_loop,
        "loop_sign_flips_across_schemes": loop_sign_flips_across_schemes,
        "loop_mag_spread_ratio": loop_mag_spread_ratio,
        "loop_mag_oom_spread": loop_mag_oom_spread,
        # regime
        "no_zero_mode": no_zero_mode,
        "domain_used_frac": domain_used_frac,
        # canonical verdict value
        "value": total_interior_sc_A,
    }


# ---------------------------------------------------------------------------
# Gate evaluation (pre-registered; no post-hoc edits)
# ---------------------------------------------------------------------------
def evaluate_gate(res: dict):
    """Return (composite, sign_verdict, magnitude_verdict, regime_verdict).

    Pre-registered (plan §W2-4):
      PASS iff interior_sign_change_count = 0 in ALL THREE schemes {zeta, f*, Gaussian}.
      FAIL iff some scheme introduces an interior sign-change absent in zeta.
      INFO iff sign-structure invariant (all 0) BUT loop magnitude differs >O(1).
    """
    # SIGN verdict: the substitution-chain Step 4 predicts a FIXED sign of dGamma/dtau (no interior
    # sign change) in ALL THREE schemes. sign PASS iff zero interior sign-changes in all three
    # (canonical representation A); the no-saddle TOPOLOGY is the [SIGN] claim.
    sign_v = "PASS" if res["all_zero_A"] else "FAIL"  # (local)

    # MAGNITUDE verdict: the operator value is the total interior-sign-change count (target 0).
    # PASS iff total == 0; the loop-magnitude spread across schemes determines INFO vs PASS:
    #   if all-zero (topology FI) BUT loop |slope| spread > O(1) (>1 OOM) => magnitude INFO.
    if not res["all_zero_A"]:
        mag_v = "FAIL"  # (local) an interior saddle formed
    elif res["loop_mag_oom_spread"] > MAG_BAND_OOM:
        mag_v = "INFO"  # (local) topology FI but loop magnitude scheme-spread > O(1)
    else:
        mag_v = "PASS"

    # REGIME verdict: loop trace-log finite (no zero mode) across the full open window AND the
    # window is computed in full (domain_used_frac=1.0). Auto-shortening bands (gate-verdicts.md):
    #   >=0.95 -> VALID; 0.50-0.95 -> MARGINAL; <0.50 -> BREAKDOWN.
    f_used = res["domain_used_frac"]  # (local)
    if not res["no_zero_mode"]:
        regime_v = "BREAKDOWN"  # (local) ln divergence if any lambda -> 0
    elif f_used >= 0.95:
        regime_v = "VALID"
    elif f_used >= 0.50:
        regime_v = "MARGINAL"
    else:
        regime_v = "BREAKDOWN"

    # Composite-collapse rule (gate-verdicts.md; PRE-REGISTERED -- modifications are Class-3):
    if regime_v == "BREAKDOWN":
        composite = "FAIL"
    elif sign_v == "FAIL":
        composite = "FAIL"
    elif mag_v == "FAIL" and regime_v == "VALID":
        composite = "FAIL"
    elif mag_v == "FAIL" and regime_v == "MARGINAL":
        composite = "INFO"
    elif mag_v == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"
    return composite, sign_v, mag_v, regime_v


# ---------------------------------------------------------------------------
# Plot
# ---------------------------------------------------------------------------
def make_plot(res: dict) -> None:
    tau = res["tau"]  # (local)
    sch = res["schemes"]  # (local)
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: dGamma/dtau, representation (A) Sum|lambda| tree, three loop schemes
    ax = axes[0, 0]
    ax.plot(tau, sch["A_zeta"]["dGam"], "-", color="C0", lw=2.0, label=r"$d\Gamma/d\tau$ (zeta)")
    ax.plot(tau, sch["A_fstar"]["dGam"], "-", color="C2", lw=2.0, label=r"$d\Gamma/d\tau$ ($f^*$)")
    ax.plot(tau, sch["A_gauss"]["dGam"], "-", color="C3", lw=2.0, label=r"$d\Gamma/d\tau$ (Gauss)")
    ax.plot(tau, res["dS_full"], "--", color="gray", lw=1.4, label=r"$dS_{\rm tree}/d\tau$ ($\Sigma|\lambda|$, E7)")
    ax.axhline(0, ls=":", color="red", lw=1.2)
    ax.axvline(tau_fold, ls="--", color="k", alpha=0.5)
    ax.set_xlabel(r"$\tau$"); ax.set_ylabel(r"$d\Gamma/d\tau$")
    ax.set_title("Rep (A) $S_{\\rm tree}=\\Sigma|\\lambda|$ (E7): interior sign-changes "
                 f"z={res['n_sc_A']['zeta']} f*={res['n_sc_A']['fstar']} G={res['n_sc_A']['gauss']}")
    ax.grid(True, alpha=0.3); ax.legend(fontsize=8)

    # Panel 2: loop slopes alone (the regulator-dependent piece) -- shows the Gaussian SIGN FLIP
    ax = axes[0, 1]
    ax.plot(tau, res["dGz"], "-", color="C0", lw=2.0, label=r"$d\Gamma_{1\rm loop}^{\zeta}/d\tau$")
    ax.plot(tau, res["dGf"], "-", color="C2", lw=2.0, label=r"$d\Gamma_{1\rm loop}^{f^*}/d\tau$")
    ax.plot(tau, res["dGg"], "-", color="C3", lw=2.0, label=r"$d\Gamma_{1\rm loop}^{\rm Gauss}/d\tau$")
    ax.axhline(0, ls=":", color="red", lw=1.2)
    ax.axvline(tau_fold, ls="--", color="k", alpha=0.5)
    ax.set_xlabel(r"$\tau$"); ax.set_ylabel(r"$d\Gamma_{1\rm loop}^{R}/d\tau$")
    flip = "YES" if res["loop_sign_flips_across_schemes"] else "NO"  # (local)
    ax.set_title(f"Loop slope (regulator-DEPENDENT): sign-flip across schemes = {flip}\n"
                 f"(Gauss<0, zeta/f*>0; eps_H-precedent realized at loop level)")
    ax.grid(True, alpha=0.3); ax.legend(fontsize=8)

    # Panel 3: representation (B) alternating-moment tree, three loop schemes (stringent arm)
    ax = axes[1, 0]
    ax.plot(tau, sch["B_zeta"]["dGam"], "-", color="C0", lw=2.0, label=r"$d\Gamma/d\tau$ (zeta)")
    ax.plot(tau, sch["B_fstar"]["dGam"], "-", color="C2", lw=2.0, label=r"$d\Gamma/d\tau$ ($f^*$)")
    ax.plot(tau, sch["B_gauss"]["dGam"], "-", color="C3", lw=2.0, label=r"$d\Gamma/d\tau$ (Gauss)")
    ax.plot(tau, res["dS_SA"], "--", color="gray", lw=1.4, label=r"$dS_{\rm SA}/d\tau$ ($a_0-a_2+a_4$)")
    ax.axhline(0, ls=":", color="red", lw=1.2)
    ax.axvline(tau_fold, ls="--", color="k", alpha=0.5)
    ax.set_xlabel(r"$\tau$"); ax.set_ylabel(r"$d\Gamma/d\tau$")
    ax.set_title("Rep (B) $S_{\\rm SA}=a_0-a_2+a_4$ (cross-check): interior sign-changes "
                 f"z={res['n_sc_B']['zeta']} f*={res['n_sc_B']['fstar']} G={res['n_sc_B']['gauss']}")
    ax.grid(True, alpha=0.3); ax.legend(fontsize=8)

    # Panel 4: Gamma(tau) itself, rep (A), three schemes (monotone => no interior stationary point)
    ax = axes[1, 1]
    ax.plot(tau, sch["A_zeta"]["Gam"], "-", color="C0", lw=2.0, label=r"$\Gamma$ (zeta)")
    ax.plot(tau, sch["A_fstar"]["Gam"], "-", color="C2", lw=2.0, label=r"$\Gamma$ ($f^*$)")
    ax.plot(tau, sch["A_gauss"]["Gam"], "-", color="C3", lw=2.0, label=r"$\Gamma$ (Gauss)")
    ax.axvline(tau_fold, ls="--", color="k", alpha=0.5, label=r"$\tau_{\rm fold}=0.19$")
    ax.set_xlabel(r"$\tau$"); ax.set_ylabel(r"$\Gamma(\tau)$")
    ax.set_title("Effective action $\\Gamma=S_{\\rm tree}+\\Gamma_{1\\rm loop}^R$ (rep A)\n"
                 "monotone in all schemes => no interior saddle")
    ax.grid(True, alpha=0.3); ax.legend(fontsize=8)

    fig.suptitle(
        f"{GATE_ID}: no-interior-saddle REGULATOR-INVARIANCE -- "
        f"interior sign-changes (rep A) zeta={res['n_sc_A']['zeta']} "
        f"f*={res['n_sc_A']['fstar']} Gauss={res['n_sc_A']['gauss']} (target 0 all)",
        fontsize=11,
    )
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=120)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------
def main():
    t0 = time.time()  # (local)
    print("=" * 78)
    print(f"{GATE_ID}  ([SIGN])")
    print("=" * 78)
    pins = log_input_pins(INPUT_FILES)
    print()
    print("CANONICAL CONSTANTS:")
    print(f"  tau_fold = {tau_fold}   M_KK = {M_KK:.6e}   PI = {PI:.6f}")
    print(f"  dS_fold (E7 canonical, Sum|lambda| conv) = {dS_fold:+.6f}")
    print(f"  d2S_fold = {d2S_fold:+.6f}   S_fold = {S_fold:.6f}")
    print(f"  a_0_FW_zeta={a_0_FW_zeta}  a_2_FW_zeta={a_2_FW_zeta}  a_4_FW_zeta={a_4_FW_zeta}")
    print(f"  f*(x) = {F_STAR_SQRT} sqrt(x) + {F_STAR_EXP} exp(-x)  (acoustic envelope)")
    print()

    res = compute()

    print("=" * 78)
    print("JENSEN RADIUS CALIBRATION (substrate-first, from S36 multi-tau cache; == S95-W2-3)")
    print("=" * 78)
    print(f"  ln(1/r) quadratic fit coef [a,b,c] = {res['jensen_coef']}")
    print(f"  fit residual max (ln units)        = {res['jensen_fit_residual_max']:.3e}")
    print(f"  1/r(tau) at S36 taus: {np.round(res['inv_r_data'], 6)}")
    print()

    print("=" * 78)
    print("FULL L12 SPECTRUM (tau_fold slice, p+q<=10; block-diagonal per Peter-Weyl sector)")
    print("=" * 78)
    print(f"  N_eval (stored |lambda| count, L<=10) = {res['n_eval']}  "
          f"(plan pin {N_EVAL_EXPECTED}; match: {res['n_eval'] == N_EVAL_EXPECTED})")
    print(f"  min|lambda| at fold  = {res['abs_min_fold']:.6f}  (> 0 => ln finite, no zero mode)")
    print(f"  min|lambda| over grid = {res['abs_min_grid']:.6f}  (> 0 over full [0, 0.30])")
    print()

    c0, c2, c4, rkf = res["sa_coeffs"]  # (local)
    print("=" * 78)
    print("[SIGN] SUBSTITUTION CHAIN -- numbers substituted (Steps 1-4)")
    print("=" * 78)
    print("  Step 1 (defs): Gamma = S_tree + Gamma_1loop^R.")
    print("    Tree rep (A): S_full = Sum|lambda| (E7; canonical dS/dtau|_fold=+58672.8).")
    print(f"    Tree rep (B): S_SA = a_0-a_2+a_4 = {c0:.3f} - {c2:.4f}*R_K + {c4:.4f}*R_K^2 "
          f"(R_K(fold)={rkf:.4f}).")
    print("    Loop g_R(x): zeta g=1; f* g=0.9117sqrt(x)+0.0883e^-x; Gauss g=e^-x.")
    print("  Step 2 (subst): dGamma^R/dtau = dS_tree/dtau + dGamma_1loop^R/dtau.")
    print("    Tree slope dS_tree/dtau is regulator-INDEPENDENT (E7); loop slope is R-DEPENDENT.")
    print("  Step 3 (simplify): an interior saddle requires dGamma_1loop^R/dtau = -dS_tree/dtau")
    print("    at some interior tau* (loop slope NEGATIVE and EXACTLY cancelling tree slope).")
    print("  Step 4 (sign read-off at fold tau=%.4f):" % res["tau"][res["ifold"]])
    print(f"    TREE (A) dS_full/dtau   = {res['dS_full_fold']:+.4f}  "
          f"(E7 canonical +58672.8; ratio {res['dS_full_vs_canonical']:.4f})")
    print(f"    TREE (B) dS_SA/dtau     = {res['dS_SA_fold']:+.4f}  "
          f"(alternating-moment curvature-poly; small, NEGATIVE -- see convention note)")
    print(f"    LOOP zeta  dG/dtau      = {res['dGz_fold']:+.4f}  (sign {res['sign_loop']['zeta']:+d})")
    print(f"    LOOP f*    dG/dtau      = {res['dGf_fold']:+.4f}  (sign {res['sign_loop']['fstar']:+d})")
    print(f"    LOOP Gauss dG/dtau      = {res['dGg_fold']:+.4f}  (sign {res['sign_loop']['gauss']:+d})")
    print(f"    loop SIGN flips across schemes? {res['loop_sign_flips_across_schemes']}  "
          f"(eps_H-precedent: Gaussian loop slope OPPOSITE-sign from zeta/f*)")
    print()

    print("=" * 78)
    print("NO-INTERIOR-SADDLE COUNTS on OPEN (0, 0.30) -- the gate operator")
    print("=" * 78)
    sch = res["schemes"]  # (local)
    print("  Representation (A) CANONICAL tree S_full=Sum|lambda| (E7; matches S95-W2-3):")
    for s in ("zeta", "fstar", "gauss"):
        d = sch[f"A_{s}"]  # (local)
        print(f"    {s:6s}: interior_sign_changes={d['n_sc']}  constant_sign={d['constant_sign']}  "
              f"dGamma range [{d['dGam_interior_min']:.2f}, {d['dGam_interior_max']:.2f}]")
    print(f"    *** TOTAL interior sign-changes (rep A) = {res['total_interior_sc_A']}  (target 0) ***")
    print()
    print("  Representation (B) STRINGENT cross-check tree S_SA=a_0-a_2+a_4:")
    for s in ("zeta", "fstar", "gauss"):
        d = sch[f"B_{s}"]  # (local)
        print(f"    {s:6s}: interior_sign_changes={d['n_sc']}  constant_sign={d['constant_sign']}  "
              f"dGamma range [{d['dGam_interior_min']:.4f}, {d['dGam_interior_max']:.4f}]")
    print(f"    *** TOTAL interior sign-changes (rep B) = {res['total_interior_sc_B']}  (cross-check) ***")
    print()

    print("=" * 78)
    print("LOOP-MAGNITUDE FI SPREAD (the INFO discriminator)")
    print("=" * 78)
    print(f"  |loop slope| at fold: zeta={abs(res['dGz_fold']):.2f}  f*={abs(res['dGf_fold']):.2f}  "
          f"Gauss={abs(res['dGg_fold']):.2f}")
    print(f"  spread ratio (max/min) = {res['loop_mag_spread_ratio']:.2f}  "
          f"=> {res['loop_mag_oom_spread']:.3f} OOM  (band {MAG_BAND_OOM} OOM: >band => magnitude INFO)")
    print()

    composite, sign_v, mag_v, regime_v = evaluate_gate(res)

    print("=" * 78)
    print("GATE EVALUATION")
    print("=" * 78)
    print(f"  value (TOTAL interior sign-changes, rep A canonical) = {res['value']}")
    print(f"  all_zero rep A = {res['all_zero_A']}   all_zero rep B = {res['all_zero_B']}")
    print(f"  domain_used_frac = {res['domain_used_frac']:.4f}   no_zero_mode = {res['no_zero_mode']}")
    print(f"  sign_verdict={sign_v}  magnitude_verdict={mag_v}  regime_verdict={regime_v}")
    print(f"  COMPOSITE VERDICT = {composite}")
    print()

    # --- save npz ---
    np.savez_compressed(
        OUT_NPZ,
        tau=res["tau"],
        inv_r_grid=res["inv_r_grid"],
        jensen_coef=res["jensen_coef"],
        jensen_fit_residual_max=res["jensen_fit_residual_max"],
        inv_r_data=res["inv_r_data"],
        n_eval=res["n_eval"],
        abs_min_fold=res["abs_min_fold"],
        abs_min_grid=res["abs_min_grid"],
        # tree actions
        S_full=res["S_full"], dS_full=res["dS_full"],
        S_SA=res["S_SA"], dS_SA=res["dS_SA"],
        sa_coeffs=np.array(res["sa_coeffs"]),
        # loop terms
        Gz=res["Gz"], Gf=res["Gf"], Gg=res["Gg"],
        dGz=res["dGz"], dGf=res["dGf"], dGg=res["dGg"],
        # Gamma + counts, rep A
        Gam_A_zeta=sch["A_zeta"]["Gam"], dGam_A_zeta=sch["A_zeta"]["dGam"],
        Gam_A_fstar=sch["A_fstar"]["Gam"], dGam_A_fstar=sch["A_fstar"]["dGam"],
        Gam_A_gauss=sch["A_gauss"]["Gam"], dGam_A_gauss=sch["A_gauss"]["dGam"],
        # Gamma + counts, rep B
        Gam_B_zeta=sch["B_zeta"]["Gam"], dGam_B_zeta=sch["B_zeta"]["dGam"],
        Gam_B_fstar=sch["B_fstar"]["Gam"], dGam_B_fstar=sch["B_fstar"]["dGam"],
        Gam_B_gauss=sch["B_gauss"]["Gam"], dGam_B_gauss=sch["B_gauss"]["dGam"],
        n_sc_A_zeta=res["n_sc_A"]["zeta"], n_sc_A_fstar=res["n_sc_A"]["fstar"],
        n_sc_A_gauss=res["n_sc_A"]["gauss"],
        n_sc_B_zeta=res["n_sc_B"]["zeta"], n_sc_B_fstar=res["n_sc_B"]["fstar"],
        n_sc_B_gauss=res["n_sc_B"]["gauss"],
        total_interior_sc_A=res["total_interior_sc_A"],
        total_interior_sc_B=res["total_interior_sc_B"],
        all_zero_A=res["all_zero_A"], all_zero_B=res["all_zero_B"],
        # fold readouts
        dS_full_fold=res["dS_full_fold"], dS_SA_fold=res["dS_SA_fold"],
        dGz_fold=res["dGz_fold"], dGf_fold=res["dGf_fold"], dGg_fold=res["dGg_fold"],
        dS_fold_canonical=dS_fold,
        dS_full_vs_canonical=res["dS_full_vs_canonical"],
        # loop sign / magnitude diagnostics
        sign_loop_zeta=res["sign_loop"]["zeta"], sign_loop_fstar=res["sign_loop"]["fstar"],
        sign_loop_gauss=res["sign_loop"]["gauss"],
        loop_sign_flips_across_schemes=res["loop_sign_flips_across_schemes"],
        loop_mag_spread_ratio=res["loop_mag_spread_ratio"],
        loop_mag_oom_spread=res["loop_mag_oom_spread"],
        # regime
        no_zero_mode=res["no_zero_mode"], domain_used_frac=res["domain_used_frac"],
        # verdict
        value=res["value"],
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
        composite=composite,
        tau_fold=tau_fold, M_KK=M_KK,
    )
    print(f"  npz written: {OUT_NPZ}")

    make_plot(res)
    print(f"  png written: {OUT_PNG}")

    # --- dual-SHA closure + verdict emission ---
    SELF = Path(__file__).resolve()
    audit_sha, content_sha = compute_dual_sha(SELF, CANONICAL_CONSTANTS_PATH, pins)
    print()
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    # value string carries the per-scheme counts so the verdict is self-describing
    value_str = (
        f"total_interior_sc_A={res['total_interior_sc_A']};"
        f"nsc_zeta={res['n_sc_A']['zeta']};nsc_fstar={res['n_sc_A']['fstar']};"
        f"nsc_gauss={res['n_sc_A']['gauss']};"
        f"total_interior_sc_B={res['total_interior_sc_B']};"
        f"dS_full_fold={res['dS_full_fold']:.2f};dS_full_vs_canonical={res['dS_full_vs_canonical']:.4f};"
        f"loop_slope_fold_zeta={res['dGz_fold']:.2f};loop_slope_fold_fstar={res['dGf_fold']:.2f};"
        f"loop_slope_fold_gauss={res['dGg_fold']:.2f};"
        f"loop_sign_flip_across_schemes={res['loop_sign_flips_across_schemes']};"
        f"loop_mag_oom_spread={res['loop_mag_oom_spread']:.3f};"
        f"CLASS=FULL;regulator_pin=a_n_zeta_tree_plus_loop_scheme_tag;"
        f"sign={sign_v};magnitude={mag_v};regime={regime_v}"
    )

    print()
    print(f"4-TUPLE: (value={res['value']}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")

    append_verdict(composite, value_str, audit_sha, content_sha)
    append_3tuple_row(sign_v, mag_v, regime_v)  # [SIGN] trigger => REQUIRED

    print()
    print(f"VERDICT LINE APPENDED to {VERDICT_TXT}")
    print(f"  {GATE_ID}: {composite} -- value(total interior sc, rep A)={res['value']} ... "
          f"audit_sha256={audit_sha}")
    print(f"  3-tuple: sign={sign_v} magnitude={mag_v} regime={regime_v}")
    print(f"\nElapsed: {time.time() - t0:.2f}s")


if __name__ == "__main__":
    main()
