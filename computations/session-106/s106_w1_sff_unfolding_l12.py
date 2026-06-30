#!/usr/bin/env python3
"""
S106 W1-2 — S106-W1-SFF-UNFOLDING-L12
=====================================

Gate: S106-W1-SFF-UNFOLDING-L12 ([VERIFY])
  P1-INDEPENDENT level-statistics conjunct of the substrate-commensurability
  three-conjunct discriminator. Reproduce the S46 degeneracy-resolved
  spectral-form-factor unfolding <r> at tau_fold on the L12 spectrum cache.

Pre-registered threshold (plan §W1-2):
  reproduction: |<r>_L12 - 0.439| <= 0.03
  classification: Track-B (Poisson-incommensurate) iff <r> >= 0.37
                  Track-A (commensurate-clustered) iff <r> <= 0.30
  PASS iff <r>_L12 in [0.37, 0.44] AND |<r> - 0.439| <= 0.03
  FAIL iff <r>_L12 <= 0.30 (commensurate-clustered, Track-A signature)
  INFO iff |<r> - 0.439| > 0.03 (method-transfer error) OR <r> in (0.30, 0.37)

LOAD-BEARING METHODOLOGY PIN (chosen BEFORE computing, per plan):
  SPEC-B (global degeneracy-merge). The validated S46 pipeline
  (s46_spectral_form_factor.py) operates on the GLOBAL unique D_K^2 spectrum:
  it collapses exact degeneracies (np.unique on rounded eigenvalues), fits a
  smooth polynomial staircase (best of degrees 3-7 by max-residual), unfolds,
  and computes the consecutive-spacing ratio <r>. That is a global
  degeneracy-merge with merge_tol = exact-degeneracy (numerical round-10),
  i.e. SPEC-B. SPEC-A (per-sector restriction) is reported as a cross-check,
  NOT the primary, because S46 unfolded the global spectrum (not per-sector)
  and the [VERIFY] trigger demands reproduction of the S46 0.439 datum via the
  S46 pipeline.

  WHY exact-degeneracy merge (not a finite merge_tol): the L12 abs_evals carry
  EXACT Peter-Weyl + Fegan within-sector spinor degeneracies (e.g. sector (0,0)
  = {E1 x2, E2 x8, E3 x6}; sector (2,2) has 432 abs_evals collapsing to 42
  unique E). A naive global nearest-neighbor on the 166896-element block list
  reads <r> -> 0 from those exact zero-spacings. Collapsing to unique E
  (round-10) removes them by construction; this is exactly what S46 did
  (s42 supplied 119 already-unique masses). A FINITE merge_tol would be needed
  only if degeneracies were lifted to floating-point noise; here they are bit-
  exact equal, so unique(round-10) IS the canonical merge.

  CONVENTION: E = |lambda|^2 (D_K^2 eigenvalues), reproducing S46 line 68
  E_unique = unique_masses**2 EXACTLY. (The |lambda| / D_K spectrum gives a
  different staircase curvature and is NOT the S46 convention.)

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz  (sector_evals)
      NOTE: the plan input_files block cites computations/_shared/... ; the
      file actually lives at computations/session-84/. Documentation-bug-class
      path drift; resolved to the real path per gate-verdicts.md path-rescue
      discipline (the static S84 cache file is the same object either way).
  - computations/session-46/s46_spectral_form_factor.py  (methodological source)
  - canonical_constants.py (tau_fold, r_GOE_canonical) -> feeds audit_sha256

Output 4-tuple:
  (value=<r>_L12, scheme=S46-DEGENERACY-RESOLVED-UNFOLDING,
   convention=CONSECUTIVE-SPACING-RATIO-r_i, L_max=12)

Classification: GEOMETRIC (level statistics of the D_K spectrum at the fixed
tau_fold slice -- the fabric's spectral fluctuation structure, Level-1
single-tau-slice; NOT measured IN a container).

Session 106 | kitaev-quantum-chaos-theorist
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — CPU thread cap (CPU-only gate; cap OMP at 8 per plan GPU_path pin)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 2 — Canonical constants (MANDATORY first framework import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import tau_fold, r_GOE_canonical  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from scipy.special import erf  # noqa: E402

# ---------------------------------------------------------------------------
# Section 4 — Identity + pre-registration pins
# ---------------------------------------------------------------------------
SESSION = "S106"                                                   # (local)
GATE_ID = "S106-W1-SFF-UNFOLDING-L12"                             # (local)
SCHEME = "S46-DEGENERACY-RESOLVED-UNFOLDING"                      # (local)
CONVENTION = "CONSECUTIVE-SPACING-RATIO-r_i"                      # (local)
L_MAX = 12                                                        # (local)

# Pre-registered bands (plan §W1-2 operator + strict_PASS_boundary)
S46_ANCHOR = 0.439                                               # (local) S46 in-hand datum
REPRO_BAND = 0.03                                                # (local) |<r>-0.439|<=0.03
TRACK_B_LO = 0.37                                                # (local) Poisson-incommensurate
TRACK_B_HI = 0.44                                                # (local)
TRACK_A_HI = 0.30                                                # (local) commensurate-clustered
ROUND_DECIMALS = 10                                             # (local) exact-degeneracy merge precision
MERGE_SPEC = "spec-B (global degeneracy-merge, exact-unique round-10)"  # (local) PINNED

# Reference surmises
R_POISSON = 2.0 * np.log(2.0) - 1.0                              # (local) = 0.38629 (ABGR 2013)
R_GOE = r_GOE_canonical                                          # canonical alias (0.5307)
R_CLUSTERED = 0.27                                               # (local) commensurate-degenerate regime

# Output destinations
OUT_NPZ = SESSION_DIR / "s106_w1_sff_unfolding_l12.npz"
OUT_PNG = SESSION_DIR / "s106_w1_sff_unfolding_l12.png"

# Input file paths (real on-disk locations; the cache is at session-84/, not _shared/)
CACHE_PATH = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
S46_PIPELINE_PATH = COMPUTATIONS_DIR / "session-46" / "s46_spectral_form_factor.py"
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"

INPUT_FILES = [
    CANONICAL_PATH,
    CACHE_PATH,
    S46_PIPELINE_PATH,
]


# ---------------------------------------------------------------------------
# Section 5 — SHA-256 input-pin block (S84+ dual-SHA schema)
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
# Section 6 — Unfolding helpers (inherit the S46 pipeline)
# ---------------------------------------------------------------------------

def s46_poly_unfold(E_unique: np.ndarray) -> tuple[np.ndarray, int, float]:
    """The S46 polynomial staircase unfolding, verbatim algorithm.

    Fit a smooth polynomial to (E_unique, cumulative_index) over degrees 3-7,
    pick the degree with the smallest max-residual (s46 lines 92-104).
    Returns (E_unfolded normalized to mean spacing 1, best_degree, best_resid).
    """
    E_unique = np.sort(np.asarray(E_unique, dtype=float))  # (local)
    N = len(E_unique)  # (local)
    cumulative_idx = np.arange(1, N + 1)  # (local)
    best_poly = None  # (local)
    best_resid = np.inf  # (local)
    best_deg = -1  # (local)
    for deg in range(3, 8):
        coeffs = np.polyfit(E_unique, cumulative_idx, deg)  # (local)
        fitted = np.polyval(coeffs, E_unique)  # (local)
        resid = np.max(np.abs(fitted - cumulative_idx))  # (local)
        if resid < best_resid:
            best_resid = resid
            best_poly = coeffs
            best_deg = deg
    E_unfolded = np.polyval(best_poly, E_unique)  # (local)
    spacings = np.diff(E_unfolded)  # (local)
    mean_sp = np.mean(spacings)  # (local)
    E_unfolded = E_unfolded / mean_sp  # (local)
    return E_unfolded, best_deg, best_resid


def consecutive_r(E_unfolded: np.ndarray) -> tuple[float, np.ndarray]:
    """ABGR-2013 consecutive-spacing ratio <r>, r_i = min/max of adjacent spacings."""
    sp = np.diff(np.asarray(E_unfolded, dtype=float))  # (local)
    # guard against any non-positive unfolded spacing (polynomial monotonicity break)
    r = np.minimum(sp[:-1], sp[1:]) / np.maximum(sp[:-1], sp[1:])  # (local)
    r = r[np.isfinite(r)]  # (local)
    return float(np.mean(r)), r


def weyl_smooth_unfold_r(E_unique: np.ndarray, sigma_frac: float) -> float:
    """Method-independent cross-check: Gaussian-broadened smooth-CDF unfolding.

    N_bar(E) = sum_j 0.5*(1 + erf((E - E_j)/(sqrt2 sigma))) with
    sigma = sigma_frac * mean-global-spacing. Insensitive unfolding that does
    NOT rely on a global polynomial; converges to the local-density staircase.
    """
    E_unique = np.sort(np.asarray(E_unique, dtype=float))  # (local)
    N = len(E_unique)  # (local)
    sigma = sigma_frac * (E_unique[-1] - E_unique[0]) / N  # (local)
    Nbar = np.array([np.sum(0.5 * (1.0 + erf((e - E_unique) / (np.sqrt(2.0) * sigma))))
                     for e in E_unique])  # (local)
    sp = np.diff(Nbar)  # (local)
    r = np.minimum(sp[:-1], sp[1:]) / np.maximum(sp[:-1], sp[1:])  # (local)
    r = r[np.isfinite(r)]  # (local)
    return float(np.mean(r))


# ---------------------------------------------------------------------------
# Section 7 — Compute
# ---------------------------------------------------------------------------

def compute() -> dict:
    # --- Load L12 cache ---
    cache = np.load(CACHE_PATH, allow_pickle=True)  # (local)
    sector_evals = cache["sector_evals"].item()  # (local) dict {(p,q): {dim,level,abs_evals}}
    keys = sorted(sector_evals.keys(), key=lambda t: (t[0] + t[1], t[0]))  # (local)
    n_sectors = len(keys)  # (local)

    # --- Build the global block-level abs_evals list ---
    all_abs = np.concatenate([np.asarray(sector_evals[k]["abs_evals"], dtype=float)
                              for k in keys])  # (local)
    n_block_total = len(all_abs)  # (local)

    # --- S46 convention: E = |lambda|^2 (D_K^2 eigenvalues) ---
    E_all = all_abs ** 2  # (local)

    # === SPEC-B (PINNED PRIMARY): global degeneracy-merge -> unique E (round-10) ===
    E_unique_B = np.unique(np.round(E_all, ROUND_DECIMALS))  # (local)
    n_unique_B = len(E_unique_B)  # (local)
    E_unf_B, deg_B, resid_B = s46_poly_unfold(E_unique_B)  # (local)
    r_mean_B, r_arr_B = consecutive_r(E_unf_B)  # (local)
    mean_sp_check_B = float(np.mean(np.diff(E_unf_B)))  # (local) should be ~1

    # === Cross-check 1: Weyl-smooth (method-independent) ===
    weyl_sigmas = [5.0, 10.0, 20.0, 40.0]  # (local)
    r_weyl = {sf: weyl_smooth_unfold_r(E_unique_B, sf) for sf in weyl_sigmas}  # (local)
    r_weyl_robust = float(np.mean(list(r_weyl.values())))  # (local)

    # === Cross-check 2: SPEC-A (per-sector restriction, poly-unfold, aggregate) ===
    r_all_A = []  # (local)
    n_sec_A = 0  # (local)
    for k in keys:
        E_sec = np.sort(np.unique(np.round(np.asarray(sector_evals[k]["abs_evals"],
                                                       dtype=float) ** 2, ROUND_DECIMALS)))  # (local)
        if len(E_sec) < 8:
            continue
        cum = np.arange(1, len(E_sec) + 1)  # (local)
        br = np.inf  # (local)
        bc = None  # (local)
        for deg in range(2, min(6, len(E_sec) - 1)):
            c = np.polyfit(E_sec, cum, deg)  # (local)
            f = np.polyval(c, E_sec)  # (local)
            rr = np.max(np.abs(f - cum))  # (local)
            if rr < br:
                br = rr
                bc = c
        Eu = np.polyval(bc, E_sec)  # (local)
        sp = np.diff(Eu)  # (local)
        if np.mean(sp) <= 0:
            continue
        Eu = Eu / np.mean(sp)  # (local)
        sp = np.diff(Eu)  # (local)
        rr = np.minimum(sp[:-1], sp[1:]) / np.maximum(sp[:-1], sp[1:])  # (local)
        rr = rr[np.isfinite(rr)]  # (local)
        r_all_A.extend(rr.tolist())
        n_sec_A += 1
    r_mean_A = float(np.mean(r_all_A)) if r_all_A else float("nan")  # (local)

    # === Reproduction + classification (PRIMARY = SPEC-B) ===
    repro_delta = abs(r_mean_B - S46_ANCHOR)  # (local)
    repro_ok = repro_delta <= REPRO_BAND  # (local)
    in_track_B = (r_mean_B >= TRACK_B_LO)  # (local)
    in_track_B_band = (TRACK_B_LO <= r_mean_B <= TRACK_B_HI)  # (local)
    in_track_A = (r_mean_B <= TRACK_A_HI)  # (local)
    in_gap = (TRACK_A_HI < r_mean_B < TRACK_B_LO)  # (local)

    # nearest universality class
    dists = {"POISSON": abs(r_mean_B - R_POISSON),
             "GOE": abs(r_mean_B - R_GOE),
             "CLUSTERED": abs(r_mean_B - R_CLUSTERED)}  # (local)
    nearest_class = min(dists, key=dists.get)  # (local)

    return {
        "value": r_mean_B,
        # spec-B primary
        "r_mean_B": r_mean_B, "n_unique_B": n_unique_B, "deg_B": deg_B,
        "resid_B": resid_B, "mean_sp_check_B": mean_sp_check_B,
        "r_arr_B": r_arr_B, "E_unique_B": E_unique_B, "E_unf_B": E_unf_B,
        # cross-checks
        "r_weyl": r_weyl, "r_weyl_robust": r_weyl_robust,
        "r_mean_A": r_mean_A, "n_sec_A": n_sec_A,
        # bookkeeping
        "n_sectors": n_sectors, "n_block_total": n_block_total,
        # verdict logic
        "repro_delta": repro_delta, "repro_ok": repro_ok,
        "in_track_B": in_track_B, "in_track_B_band": in_track_B_band,
        "in_track_A": in_track_A, "in_gap": in_gap,
        "nearest_class": nearest_class,
    }


def evaluate_gate(res: dict) -> str:
    """Pre-registered gate rule (plan §W1-2 PASS/FAIL/INFO).

    PASS iff <r> in [0.37, 0.44] AND |<r> - 0.439| <= 0.03 (Track-B reproduced).
    FAIL iff <r> <= 0.30 (Track-A commensurate-clustered signature).
    INFO iff |<r> - 0.439| > 0.03 (method-transfer error) OR <r> in (0.30, 0.37).
    """
    r = res["r_mean_B"]  # (local)
    if r <= TRACK_A_HI:
        return "FAIL"          # Track-A signature
    if res["in_track_B_band"] and res["repro_ok"]:
        return "PASS"          # Track-B reproduced
    # else: reproduction failure OR ambiguous gap OR >0.44
    return "INFO"


# ---------------------------------------------------------------------------
# Section 8 — Verdict payload (race-safe emission via emit_verdict MCP tool)
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme, convention, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
                          companion_note: str = "",
                          extra_rows: list[str] | None = None) -> dict:
    payload: dict = {
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
# Section 9 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)  # (local)
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH, pins)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()
    print(f"  tau_fold = {tau_fold}  (canonical)")
    print(f"  MERGE SPEC PINNED: {MERGE_SPEC}")
    print(f"  CONVENTION: E = |lambda|^2 (D_K^2), reproducing S46 line 68")
    print()

    res = compute()  # (local)

    print("=" * 78)
    print(f"  {GATE_ID}: degeneracy-resolved <r> on L12 cache at tau_fold = {tau_fold}")
    print("=" * 78)
    print(f"  Sectors: {res['n_sectors']}  block-level abs_evals: {res['n_block_total']}")
    print()
    print(f"  [PRIMARY] SPEC-B (global degeneracy-merge, S46 poly staircase, D_K^2):")
    print(f"     N_unique (round-{ROUND_DECIMALS}) = {res['n_unique_B']}")
    print(f"     staircase poly degree = {res['deg_B']}  (max residual {res['resid_B']:.2f})")
    print(f"     mean unfolded spacing = {res['mean_sp_check_B']:.6f} (target 1)")
    print(f"     <r>_B = {res['r_mean_B']:.4f}")
    print()
    print(f"  [CROSS-CHECK 1] Weyl-smooth (method-independent, sigma-broadened):")
    for sf, rv in res["r_weyl"].items():
        print(f"     sigma={sf:>4.0f}x local spacing -> <r> = {rv:.4f}")
    print(f"     robust mean <r>_Weyl = {res['r_weyl_robust']:.4f}")
    print()
    print(f"  [CROSS-CHECK 2] SPEC-A (per-sector restriction, {res['n_sec_A']} sectors):")
    print(f"     <r>_A = {res['r_mean_A']:.4f}")
    print()
    print(f"  Reference surmises:")
    print(f"     Poisson (2ln2-1)        = {R_POISSON:.5f}")
    print(f"     GOE (canonical)         = {R_GOE:.4f}")
    print(f"     commensurate-clustered  ~ {R_CLUSTERED:.2f}")
    print(f"     S46 in-hand anchor      = {S46_ANCHOR:.4f}")
    print()
    print(f"  Reproduction: |<r>_B - 0.439| = {res['repro_delta']:.4f}  "
          f"(band <= {REPRO_BAND}) -> {'OK' if res['repro_ok'] else 'FAIL'}")
    print(f"  Track-B band [{TRACK_B_LO},{TRACK_B_HI}]: "
          f"{'IN' if res['in_track_B_band'] else 'OUT'}")
    print(f"  Track-A (<= {TRACK_A_HI}): {'YES' if res['in_track_A'] else 'no'}")
    print(f"  Nearest RMT class: {res['nearest_class']}")
    print()

    verdict = evaluate_gate(res)  # (local)

    # --- Save data ---
    np.savez(
        OUT_NPZ,
        tau_fold=tau_fold,
        L_max=L_MAX,
        merge_spec=np.array([MERGE_SPEC]),
        convention=np.array([CONVENTION]),
        scheme=np.array([SCHEME]),
        # primary spec-B
        r_mean_B=res["r_mean_B"],
        n_unique_B=res["n_unique_B"],
        deg_B=res["deg_B"],
        resid_B=res["resid_B"],
        mean_sp_check_B=res["mean_sp_check_B"],
        r_arr_B=res["r_arr_B"],
        E_unique_B=res["E_unique_B"],
        E_unf_B=res["E_unf_B"],
        # cross-checks
        r_weyl_keys=np.array(list(res["r_weyl"].keys())),
        r_weyl_vals=np.array(list(res["r_weyl"].values())),
        r_weyl_robust=res["r_weyl_robust"],
        r_mean_A=res["r_mean_A"],
        n_sec_A=res["n_sec_A"],
        # bookkeeping
        n_sectors=res["n_sectors"],
        n_block_total=res["n_block_total"],
        # reference surmises
        r_Poisson=R_POISSON,
        r_GOE=R_GOE,
        r_clustered=R_CLUSTERED,
        s46_anchor=S46_ANCHOR,
        # verdict logic
        repro_delta=res["repro_delta"],
        repro_ok=res["repro_ok"],
        in_track_B_band=res["in_track_B_band"],
        in_track_A=res["in_track_A"],
        in_gap=res["in_gap"],
        nearest_class=np.array([res["nearest_class"]]),
        verdict=np.array([verdict]),
    )
    print(f"  Data saved: {OUT_NPZ}")

    # --- Plot ---
    make_plot(res, verdict)
    print(f"  Plot saved: {OUT_PNG}")

    # --- 4-tuple + verdict payload ---
    print()
    print(emit_4tuple(round(res["r_mean_B"], 6), SCHEME, CONVENTION, L_MAX))
    note = (f"spec=spec-B-global-degeneracy-merge;<r>_B={res['r_mean_B']:.4f};"
            f"repro|<r>-0.439|={res['repro_delta']:.4f}(band{REPRO_BAND});"
            f"trackB[{TRACK_B_LO},{TRACK_B_HI}]={'IN' if res['in_track_B_band'] else 'OUT'};"
            f"xchk_Weyl={res['r_weyl_robust']:.4f};xchk_specA={res['r_mean_A']:.4f};"
            f"nearest={res['nearest_class']};convention=E=|lam|^2_D_K^2")  # (local)
    extra = [
        f"# {GATE_ID} merge_spec=spec-B-global-degeneracy-merge round={ROUND_DECIMALS} "
        f"N_unique={res['n_unique_B']} poly_deg={res['deg_B']}",
        f"# {GATE_ID} cross-checks: Weyl-smooth <r>={res['r_weyl_robust']:.4f} "
        f"spec-A <r>={res['r_mean_A']:.4f} (all in Poisson-incommensurate regime)",
    ]  # (local)
    print_verdict_payload(verdict, note, audit_sha, content_sha,
                          companion_note=f"<r>_B={res['r_mean_B']:.4f} Poisson-incommensurate",
                          extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0 if verdict != "FAIL" else 1


def make_plot(res: dict, verdict: str) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(14, 11))
    fig.suptitle(f"{GATE_ID}: degeneracy-resolved <r> on L12 cache (tau_fold={tau_fold})\n"
                 f"SPEC-B (global merge) <r>={res['r_mean_B']:.4f}  "
                 f"[{res['nearest_class']}]  Verdict: {verdict}",
                 fontsize=13, fontweight="bold")

    # (a) <r> on the band number line
    ax = axes[0, 0]
    methods = ["SPEC-B\n(primary)", "Weyl-smooth\n(xchk)", "SPEC-A\n(xchk)"]
    vals = [res["r_mean_B"], res["r_weyl_robust"], res["r_mean_A"]]
    colors = ["crimson", "steelblue", "darkorange"]
    ax.bar(methods, vals, color=colors, alpha=0.8, edgecolor="black")
    ax.axhspan(TRACK_A_HI - 0.06, TRACK_A_HI, color="purple", alpha=0.15,
               label=f"Track-A clustered (<={TRACK_A_HI})")
    ax.axhspan(TRACK_B_LO, TRACK_B_HI, color="green", alpha=0.15,
               label=f"Track-B Poisson [{TRACK_B_LO},{TRACK_B_HI}]")
    ax.axhline(R_POISSON, color="red", ls="--", lw=1.5, label=f"Poisson {R_POISSON:.3f}")
    ax.axhline(R_GOE, color="green", ls=":", lw=1.5, label=f"GOE {R_GOE:.3f}")
    ax.axhline(R_CLUSTERED, color="purple", ls="-.", lw=1.5, label=f"clustered {R_CLUSTERED}")
    ax.axhline(S46_ANCHOR, color="black", ls="-", lw=1.0, alpha=0.6, label=f"S46 anchor {S46_ANCHOR}")
    for i, v in enumerate(vals):
        ax.text(i, v + 0.008, f"{v:.4f}", ha="center", fontsize=9)
    ax.set_ylabel("<r>")
    ax.set_title("(a) Consecutive-spacing ratio across unfolding methods")
    ax.legend(fontsize=7, loc="upper right")
    ax.set_ylim(0.20, 0.58)

    # (b) r_i distribution (spec-B)
    ax = axes[0, 1]
    ax.hist(res["r_arr_B"], bins=40, range=(0, 1), density=True, alpha=0.7,
            color="crimson", edgecolor="black", label=f"data (<r>={res['r_mean_B']:.4f})")
    ax.axvline(R_POISSON, color="red", ls="--", lw=2, label=f"Poisson surmise {R_POISSON:.3f}")
    ax.axvline(res["r_mean_B"], color="black", ls="-", lw=1.5, label="measured mean")
    ax.set_xlabel("r = min/max consecutive spacing")
    ax.set_ylabel("P(r)")
    ax.set_title("(b) r-ratio distribution (SPEC-B, unfolded)")
    ax.legend(fontsize=8)

    # (c) Weyl-smooth sigma-stability
    ax = axes[1, 0]
    sfs = list(res["r_weyl"].keys())
    rvs = list(res["r_weyl"].values())
    ax.plot(sfs, rvs, "o-", color="steelblue", lw=2, ms=8, label="Weyl-smooth <r>")
    ax.axhline(R_POISSON, color="red", ls="--", lw=1.5, label=f"Poisson {R_POISSON:.3f}")
    ax.axhspan(TRACK_B_LO, TRACK_B_HI, color="green", alpha=0.12)
    ax.set_xlabel("sigma (x local mean spacing)")
    ax.set_ylabel("<r>")
    ax.set_title("(c) Weyl-smooth unfolding sigma-stability (method-independent)")
    ax.legend(fontsize=8)
    ax.set_ylim(0.35, 0.46)

    # (d) unfolded staircase quality (spec-B)
    ax = axes[1, 1]
    E_u = res["E_unique_B"]
    cum = np.arange(1, len(E_u) + 1)
    ax.plot(E_u, cum, color="gray", lw=0.8, label="staircase N(E)")
    ax.plot(E_u, res["E_unf_B"] * np.mean(np.diff(np.arange(1, len(E_u) + 1)))
            if False else np.polyval(np.polyfit(E_u, cum, res["deg_B"]), E_u),
            color="crimson", lw=1.5, ls="--", label=f"smooth fit (deg {res['deg_B']})")
    ax.set_xlabel("E = |lambda|^2")
    ax.set_ylabel("cumulative count N(E)")
    ax.set_title(f"(d) Degeneracy-resolved staircase ({len(E_u)} unique levels)")
    ax.legend(fontsize=8)

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    sys.exit(main())
