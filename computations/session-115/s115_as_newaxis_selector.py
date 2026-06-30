#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S115 W3-2 — CF-S115-AS-NEWAXIS-SELECTOR  (OPTIONAL, EVOI-last)
=============================================================

Does a functional-determination principle OUTSIDE the three already-tried
{impulse-quench, UNIFIED-AS-79, Parker-adiabatic} collapse the 1.2590-OOM
cross-functional A_s spread to a SINGLE typed value?

Two NEW physical axes (neither a sudden / slow-roll / adiabatic choice):

  AXIS-1  maximum-entropy / Jaynes on the post-transit occupation n_k.
      The GGE/Jaynes prediction: given the substrate-fixed conserved charges
      <N> = sum_k |beta_k|^2  and  <E> = sum_k omega_k |beta_k|^2 read off the
      box-delta sudden Bogoliubov spectrum (s100b), the maximum-entropy
      occupation is the Bose form
          n_k^maxent = 1 / (exp(lambda_N + lambda_E * omega_k) - 1)
      with (lambda_N, lambda_E) fixed by the two constraints (Lagrange
      multipliers). A_s^maxent = n_khat^maxent / (2 pi^2) at the SAME
      k_hat = 1/xi_KZ normalization the impulse-quench FLOOR (A_s_FW, S111-CF-AS3a)
      uses.  This is the substrate's own thermalization-BLIND occupation
      (the Ordered Veil: R_therm=5252, S_ent=0 — the GGE never thermalizes,
      but its maxent IMAGE under the two conserved moments is still the
      canonical Jaynes prediction).

  AXIS-2  Connes-distance-canonical normalization of the relic spectral
      functional.  The intrinsic NCG metric between the in-vacuum and
      out-vacuum states on the substrate spectral triple (A_K, H_K, D_K).
      On the commutative diagonal sub-triple the Connes spectral distance
      d_C(omega_p, omega_q) = sup_{||[D,a]||<=1} |omega_p(a)-omega_q(a)| has the
      closed extremal value (DIAMETER) d_C = 1/(lambda_max - lambda_min) — the
      UNIQUE substrate-intrinsic dimensionless distance scale on the triple.
      A_s^Connes = |beta_khat|^2 / (2 pi^2 * d_C):  normalize the relic
      per-mode amplitude by the substrate's own spectral-triple diameter, a
      normalization that is NOT a sudden / slow-roll / adiabatic choice.
      Cross-check: the inverse-gap-at-pivot reading and the Fubini-Study
      vacuum-angle reading.

PASS  iff EITHER axis yields A_s^newaxis within 0.10 OOM (DIAGNOSTIC collapse
      band) of BOTH the impulse-quench value AND at least one OTHER pre-existing
      functional (UNIFIED or Parker) — i.e. the selector collapses the >=1.259-OOM
      spread to <= 0.10 OOM around a SINGLE typed value.
FAIL  iff neither axis collapses the spread (A_s^newaxis is a FOURTH scattered
      value, OR coincides with only ONE pre-existing functional).
      => FUNCTIONAL-PLURALISM-PERMANENT widened on the {maxent, Connes} axis-basis.
INFO  iff partial regime (one axis collapses, the other not; OR a selector
      coincides with exactly one pre-existing functional, ambiguous between
      collapse and coincidence).

NOT a Planck-comparison gate.  The 0.10-OOM band is a pre-registered DIAGNOSTIC
threshold (an order-of-magnitude tightening of the 1.259-OOM spread), chosen at
plan-freeze, NOT analytically derived.  The verdict is OPEN: prior 0.10/0.90
(PASS/FAIL) per the S114 W4-1 FUNCTIONAL-PLURALISM-PERMANENT result.  This gate
is NOT iterated toward PASS — the maxent and Connes axes are FIXED physical
principles, not tuned.

SUBSTRATE FRAMING (PHONONIC):
  D_K eigenvalues -> box-delta sudden Bogoliubov |beta_k|^2 -> relic occupation n_k
  -> (selector) -> A_s.  The substrate IS the produced occupation; the lab measures
  A_s.  The OPEN question is whether the SELECTOR node is substrate-fixed (the
  substrate types its own A_s) or free (A_s is a physical d.o.f. like the a_0/a_2
  cosmological-constant ratio).  This gate asks the substrate's OWN structure via
  two principles not yet tried (maximum-entropy occupation; Connes spectral-triple
  metric).

Pre-registration:  sessions/session-plan/session-115-plan-w3.md  §W3-2
Trigger: [SIGN]  (sign = direction of collapse vs no-collapse;
                  magnitude = min cross-functional OOM distance vs the 0.10 band;
                  regime = maxent solve + Connes-distance eval numerical validity)
Verdict: composite in {PASS=collapse, FAIL=PLURALISM-PERMANENT-widened, INFO=partial}
"""

import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# Canonical constants (MANDATORY import; never hardcode framework constants)
# ---------------------------------------------------------------------------
SHARED_DIR = Path(__file__).resolve().parents[1] / "_shared"
sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403  (A_s_FW, A_s_CMB, xi_KZ_FW)

# ---------------------------------------------------------------------------
# Section 1 — Identity
# ---------------------------------------------------------------------------
SESSION = "S115"
GATE_ID = "S115-AS-NEWAXIS-SELECTOR"
SCHEME = "AS-NEWAXIS-SELECTOR-MAXENT-CONNES"
CONVENTION = "OOM-COLLAPSE-DIAGNOSTIC"
L_MAX = "12"  # box-delta spectrum + Connes triple on the L12 D_K cache (A_s_FW lineage S111)

THIS_DIR = Path(__file__).resolve().parent
REPO_ROOT = THIS_DIR.parents[1]

# ---------------------------------------------------------------------------
# Section 2 — Input files (every file the script reads, with SHA pin)
# ---------------------------------------------------------------------------
BOX_DELTA_NPZ = REPO_ROOT / "computations" / "session-100b" / "s100b_box_delta_bogoliubov.npz"
L12_CACHE_NPZ = REPO_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"

INPUT_FILES = {
    "canonical_constants.py": CANONICAL_PATH,
    "s100b_box_delta_bogoliubov.npz": BOX_DELTA_NPZ,
    "s84_spectrum_cache_L12_tau019.npz": L12_CACHE_NPZ,
}


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    h.update(Path(path).read_bytes())
    return h.hexdigest()


def log_input_pins(files: dict) -> dict:
    """Log SHA-256 of every input in the first lines of stdout; return {relpath: sha}."""
    pins = {}  # (local)
    print("=== INPUT SHA-256 PINS ===")
    for rel, p in files.items():
        s = sha256_of(p)  # (local)
        pins[rel] = s
        print(f"  {rel}: {s}")
    return pins


# ---------------------------------------------------------------------------
# Section 3 — dual-SHA (S84+ schema)
# ---------------------------------------------------------------------------
def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    """audit = sha256(script || canonical || pinmap_json); content = sha256(script)."""
    script_bytes = script_path.read_bytes()  # (local)
    canonical_bytes = canonical_path.read_bytes()  # (local)
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
# Section 4 — Compute
# ---------------------------------------------------------------------------

# Pre-registered DIAGNOSTIC collapse band (plan §W3-2 strict_PASS_boundary).
# NOT a Planck-comparison gate; an OOM tightening of the 1.2590-OOM spread.
COLLAPSE_BAND_OOM = 0.10  # (local) PASS band on the OOM distance to a single typed value

# Maxent constraint-satisfaction residual + Connes convergence tolerance (plan tolerance pin).
SOLVE_TOL = 1e-10  # (local)


def maxent_occupation(omega, beta2, tol):
    """Maximum-entropy (Jaynes/GGE) Bose occupation subject to two conserved moments.

    n_k^maxent = 1 / (exp(lambda_N + lambda_E * omega_k) - 1), with
    (lambda_N, lambda_E) the Lagrange multipliers enforcing
      <N> = sum_k n_k^maxent = sum_k |beta_k|^2     (mean pair number)
      <E> = sum_k omega_k n_k^maxent = sum_k omega_k |beta_k|^2   (total energy, M_KK clock)

    Returns (n_k^maxent array, lambda_N, lambda_E, residual_N, residual_E).
    Deterministic Lagrange-multiplier root-find (scipy.optimize.fsolve on the two
    constraint equations).
    """
    from scipy.optimize import fsolve

    N_tot = float(np.sum(beta2))                 # (local) <N> target
    E_tot = float(np.sum(omega * beta2))         # (local) <E> target

    def occ(lN, lE):
        x = lN + lE * omega                       # (local)
        x = np.clip(x, 1e-12, 700.0)              # (local) overflow guard (dilute => large x)
        return 1.0 / np.expm1(x)

    def eqs(p):
        lN, lE = p
        nk = occ(lN, lE)                          # (local)
        return [float(np.sum(nk)) - N_tot,
                float(np.sum(omega * nk)) - E_tot]

    # Seed near the dilute-Bose regime: sum|beta|^2 ~ 2e-5 => deep dilute => large lambda_N.
    sol, info, ier, msg = fsolve(eqs, [10.0, 0.1], full_output=True, xtol=tol)
    lN, lE = float(sol[0]), float(sol[1])         # (local)
    nk = occ(lN, lE)                              # (local)
    res_N = abs(float(np.sum(nk)) - N_tot)        # (local)
    res_E = abs(float(np.sum(omega * nk)) - E_tot)  # (local)
    converged = bool(ier == 1 and res_N <= 1e-9 * max(N_tot, 1e-30)
                     and res_E <= 1e-9 * max(E_tot, 1e-30))  # (local)
    return nk, lN, lE, res_N, res_E, converged, N_tot, E_tot


def connes_diameter_distance(abs_evals_sorted):
    """Connes spectral DIAMETER on the commutative diagonal sub-triple of (A_K, H_K, D_K).

    For two pure vector states omega_p, omega_q (eigenbasis), the Connes spectral distance
      d_C(omega_p, omega_q) = sup_{a in A : ||[D,a]||<=1} |omega_p(a) - omega_q(a)|
    on the diagonal commutative sub-algebra reduces to the resistance/path metric on the
    eigenvalue line; its EXTREMAL value (the metric DIAMETER, between the lowest and
    highest D_K eigenstates) has the closed form
      d_C^diam = 1 / (lambda_max - lambda_min)
    with the optimal element a saturating ||[D,a]|| = 1.  This is the UNIQUE substrate-
    intrinsic dimensionless distance scale on the triple (regulator-free; an L_max-dependent
    structural property of the finite spectral triple).
    """
    lam_min = float(abs_evals_sorted.min())       # (local)
    lam_max = float(abs_evals_sorted.max())        # (local)
    return 1.0 / (lam_max - lam_min), lam_min, lam_max


def compute() -> dict:
    out = {}  # (local)

    # ---- Load the box-delta sudden Bogoliubov spectrum (the MAGNITUDE source) ----
    d = np.load(BOX_DELTA_NPZ, allow_pickle=True)  # (local)
    beta2_spectrum = np.asarray(d["beta2_spectrum"], dtype=float)    # (local) 64 modes
    k_grid = np.asarray(d["k_grid"], dtype=float)                    # (local) k in [1,50]
    beta2_pivot_closed = float(d["beta2_pivot_closed_form"])         # (local) 3.0454e-07
    k_pivot = float(d["k_pivot"])                                    # (local) 14.311
    mu_pivot_sq = float(d["mu_pivot_sq"])                            # (local) 202.9 (eff mass^2)

    N_modes = int(k_grid.shape[0])                                   # (local) 64
    out["N_modes"] = N_modes
    out["k_pivot"] = k_pivot
    out["beta2_pivot_closed_form"] = beta2_pivot_closed
    out["mu_pivot_sq"] = mu_pivot_sq

    # ---- The three EXISTING functional A_s values (the SPREAD to collapse) ----
    # impulse-quench POINT = A_s_FW (canonical, S111-CF-AS3a). UNIFIED + Parker OOM are
    # pinned literals from their provenance (S82 / inv-6); reconstruct A_s from OOM vs Planck.
    A_planck = float(A_s_CMB)                       # (local) 2.1e-9
    A_s_impulse = float(A_s_FW)                     # (local) 1.5367e-08 (canonical)
    oom_impulse = float(np.log10(A_s_impulse / A_planck))   # (local) +0.86437
    oom_unified = 0.196                             # (local) S82 UNIFIED-AS-79 (A_s=3.298e-9)
    oom_parker = 1.455                              # (local) inv-6 W2-2 Parker (A_s=5.99e-8)
    A_s_unified = A_planck * 10.0 ** oom_unified    # (local) 3.298e-9
    A_s_parker = A_planck * 10.0 ** oom_parker      # (local) 5.987e-8
    ooms_existing = np.array([oom_impulse, oom_unified, oom_parker])  # (local)
    spread_existing = float(np.max(ooms_existing) - np.min(ooms_existing))  # (local) 1.2590 OOM

    out["A_s_Planck"] = A_planck
    out["A_s_impulse"] = A_s_impulse
    out["A_s_unified"] = A_s_unified
    out["A_s_parker"] = A_s_parker
    out["oom_impulse"] = oom_impulse
    out["oom_unified"] = oom_unified
    out["oom_parker"] = oom_parker
    out["spread_existing_OOM"] = spread_existing

    # k_hat normalization the impulse-quench FLOOR uses (S111-CF-AS3a): k_hat = 1/xi_KZ.
    xi = float(xi_KZ_FW)                            # (local) 0.018760
    k_hat = 1.0 / xi                               # (local) 53.3048 M_KK
    out["xi_KZ"] = xi
    out["k_hat"] = k_hat
    # |beta_khat|^2 implied by the floor A_s_FW = |beta_khat|^2/(2 pi^2):
    beta2_khat_floor = 2.0 * np.pi ** 2 * A_s_impulse  # (local) 3.0333e-07
    out["beta2_khat_floor"] = beta2_khat_floor

    # ======================================================================
    # AXIS-1 — maximum-entropy / Jaynes occupation
    # ======================================================================
    # omega_k: the out-frequency (M_KK clock). Massless out-dispersion omega_k = k is the
    # leading clock for the box-delta sudden problem; the effective mass mu_pivot_sq enters
    # only sub-leading. Use omega_k = k (the conserved-energy moment <E> = sum k |beta_k|^2).
    omega_k = k_grid.copy()                        # (local) out-frequency = k (massless out, M_KK)

    nk_maxent, lN, lE, res_N, res_E, me_conv, N_tot, E_tot = maxent_occupation(
        omega_k, beta2_spectrum, SOLVE_TOL)
    out["maxent_lambda_N"] = lN
    out["maxent_lambda_E"] = lE
    out["maxent_residual_N"] = res_N
    out["maxent_residual_E"] = res_E
    out["maxent_converged"] = me_conv
    out["maxent_N_tot"] = N_tot
    out["maxent_E_tot"] = E_tot
    out["maxent_mean_energy_per_pair"] = E_tot / N_tot

    # Pivot occupation: interpolate n_k^maxent at k_pivot (inside the grid).
    nk_pivot_maxent = float(np.interp(k_pivot, k_grid, nk_maxent))   # (local)
    out["nk_pivot_maxent"] = nk_pivot_maxent
    # k_hat occupation: k_hat = 53.30 is OUTSIDE the grid (k<=50). The squeezed spectrum is
    # near-flat out to the first RT zero (k~2779), so n_k^maxent(k_hat) ~ flat extrapolation
    # of the maxent occupation; take the top-grid value as the k_hat-normalization proxy AND
    # report the pivot value. Primary A_s^maxent uses the k_hat-normalization to match the
    # floor's own construction (A_s_FW = |beta_khat|^2/2pi^2 at k_hat=1/xi).
    nk_khat_maxent = float(nk_maxent[-1])           # (local) top-grid (k=50) ~ k_hat proxy
    out["nk_khat_maxent"] = nk_khat_maxent

    A_s_maxent_pivot = nk_pivot_maxent / (2.0 * np.pi ** 2)   # (local) pivot-normalized
    A_s_maxent_khat = nk_khat_maxent / (2.0 * np.pi ** 2)     # (local) k_hat-normalized (primary)
    out["A_s_maxent_pivot"] = A_s_maxent_pivot
    out["A_s_maxent_khat"] = A_s_maxent_khat
    # Primary A_s^maxent = k_hat-normalized (matches the floor construction).
    A_s_maxent = A_s_maxent_khat                    # (local) PRIMARY
    out["A_s_maxent"] = A_s_maxent
    oom_maxent = float(np.log10(A_s_maxent / A_planck))   # (local)
    out["oom_maxent"] = oom_maxent

    # ======================================================================
    # AXIS-2 — Connes-distance-canonical normalization
    # ======================================================================
    cache = np.load(L12_CACHE_NPZ, allow_pickle=True)  # (local)
    sector_evals = cache["sector_evals"].item()        # (local) dict {(p,q): {abs_evals,...}}
    all_evals = np.sort(np.concatenate(
        [np.asarray(v["abs_evals"], dtype=float) for v in sector_evals.values()]))  # (local)
    out["L12_n_evals"] = int(all_evals.size)

    # Connes DIAMETER (the unique substrate-intrinsic extremal distance scale on the triple).
    d_connes_diam, lam_min, lam_max = connes_diameter_distance(all_evals)  # (local)
    out["lam_min"] = lam_min
    out["lam_max"] = lam_max
    out["d_connes_diameter"] = d_connes_diam        # = 1/(lam_max - lam_min) = 0.217429

    # Cross-check Connes scales: (i) inverse max-gap (smallest consecutive Connes distance),
    # (ii) Fubini-Study vacuum angle between in/out vacua.
    uq = np.unique(np.round(all_evals, 10))         # (local)
    gaps = np.diff(uq)                               # (local)
    d_connes_invmaxgap = 1.0 / float(gaps.max())     # (local) smallest level-to-level distance
    out["d_connes_invmaxgap"] = d_connes_invmaxgap
    sum_beta2 = float(np.sum(beta2_spectrum))        # (local)
    vac_overlap = float(np.exp(-0.5 * sum_beta2))    # (local) |<in|out>| ~ exp(-1/2 sum|beta|^2)
    fs_angle = float(np.arccos(min(1.0, vac_overlap)))  # (local) Fubini-Study angle
    out["sum_beta2"] = sum_beta2
    out["vac_overlap"] = vac_overlap
    out["fs_angle"] = fs_angle

    # GPU cross-validation of the spectral-triple extremal eigenvalues (>=100x100 triple):
    # ship the full eigenvalue array to ROCm and re-confirm min/max via torch.
    try:
        import torch
        if torch.cuda.is_available():
            t = torch.tensor(all_evals, device="cuda")
            gpu_min = float(torch.min(t).cpu())      # (local)
            gpu_max = float(torch.max(t).cpu())      # (local)
            gpu_dev = abs(gpu_min - lam_min) + abs(gpu_max - lam_max)  # (local)
            out["gpu_extremal_dev"] = gpu_dev
            out["gpu_device"] = torch.cuda.get_device_name(0)
        else:
            out["gpu_extremal_dev"] = -1.0
            out["gpu_device"] = "cpu-fallback"
    except Exception as e:  # noqa: BLE001
        out["gpu_extremal_dev"] = -1.0
        out["gpu_device"] = f"torch-unavailable: {type(e).__name__}"

    # A_s^Connes: normalize the relic per-mode amplitude |beta_khat|^2 by the substrate's
    # OWN spectral-triple Connes DIAMETER (dimensionless).  This is the substrate-canonical
    # normalization (NOT a sudden/slow-roll/adiabatic choice):
    #   A_s^Connes = |beta_khat|^2 / (2 pi^2 * d_C^diam)
    A_s_connes = beta2_khat_floor / (2.0 * np.pi ** 2 * d_connes_diam)  # (local) PRIMARY
    out["A_s_connes"] = A_s_connes
    oom_connes = float(np.log10(A_s_connes / A_planck))   # (local)
    out["oom_connes"] = oom_connes
    # Cross-check Connes normalizations (reported, NOT primary):
    A_s_connes_invgap = beta2_khat_floor / (2.0 * np.pi ** 2 * d_connes_invmaxgap)  # (local)
    A_s_connes_fs = beta2_khat_floor / (2.0 * np.pi ** 2 * fs_angle)  # (local)
    out["A_s_connes_invgap"] = A_s_connes_invgap
    out["A_s_connes_fs"] = A_s_connes_fs
    out["oom_connes_invgap"] = float(np.log10(A_s_connes_invgap / A_planck))
    out["oom_connes_fs"] = float(np.log10(A_s_connes_fs / A_planck))

    # ======================================================================
    # COLLAPSE TEST — does either axis collapse the spread to a single typed value?
    # ======================================================================
    # PASS iff EITHER axis lands within COLLAPSE_BAND_OOM of BOTH impulse AND at least one
    # OTHER pre-existing functional (UNIFIED or Parker). i.e. the selector pulls the new value
    # into agreement with impulse AND a second functional => the >=1.259-OOM spread collapses.
    def collapse_check(oom_axis):
        """Return (collapses_bool, d_impulse, d_unified, d_parker, n_within_band, which_2nd)."""
        d_imp = abs(oom_axis - oom_impulse)          # (local)
        d_uni = abs(oom_axis - oom_unified)          # (local)
        d_par = abs(oom_axis - oom_parker)           # (local)
        within = {"impulse": d_imp <= COLLAPSE_BAND_OOM,
                  "unified": d_uni <= COLLAPSE_BAND_OOM,
                  "parker": d_par <= COLLAPSE_BAND_OOM}  # (local)
        n_within = int(sum(within.values()))         # (local)
        # PASS requires impulse AND >=1 other within band (i.e. >=2 incl impulse, impulse in set)
        seconds = [name for name in ("unified", "parker") if within[name]]  # (local)
        collapses = bool(within["impulse"] and len(seconds) >= 1)            # (local)
        which_2nd = seconds[0] if seconds else "none"                        # (local)
        return collapses, d_imp, d_uni, d_par, n_within, which_2nd

    me_collapse, me_di, me_du, me_dp, me_n, me_2nd = collapse_check(oom_maxent)   # (local)
    cn_collapse, cn_di, cn_du, cn_dp, cn_n, cn_2nd = collapse_check(oom_connes)   # (local)
    out["maxent_collapses"] = me_collapse
    out["maxent_d_impulse"] = me_di
    out["maxent_d_unified"] = me_du
    out["maxent_d_parker"] = me_dp
    out["maxent_n_within_band"] = me_n
    out["maxent_which_2nd"] = me_2nd
    out["connes_collapses"] = cn_collapse
    out["connes_d_impulse"] = cn_di
    out["connes_d_unified"] = cn_du
    out["connes_d_parker"] = cn_dp
    out["connes_n_within_band"] = cn_n
    out["connes_which_2nd"] = cn_2nd

    any_collapse = bool(me_collapse or cn_collapse)   # (local)
    out["any_axis_collapses"] = any_collapse

    # "coincides with only ONE functional" detection (the INFO-vs-FAIL discriminator):
    # an axis that lands within band of EXACTLY ONE pre-existing functional is a coincidence,
    # not a collapse (ambiguous). Used for the regime/composite reading.
    me_single_coincidence = bool((not me_collapse) and me_n == 1)   # (local)
    cn_single_coincidence = bool((not cn_collapse) and cn_n == 1)   # (local)
    out["maxent_single_coincidence"] = me_single_coincidence
    out["connes_single_coincidence"] = cn_single_coincidence

    # The MINIMUM cross-functional OOM distance achieved by the new axes to the
    # nearest-collapse target (the magnitude leg vs the 0.10 band):
    # for each axis, the "collapse distance" = max(d_impulse, min(d_unified, d_parker)) —
    # the value that must be <= band for a two-functional collapse.
    me_collapse_dist = max(me_di, min(me_du, me_dp))   # (local)
    cn_collapse_dist = max(cn_di, min(cn_du, cn_dp))   # (local)
    min_collapse_dist = float(min(me_collapse_dist, cn_collapse_dist))  # (local)
    out["maxent_collapse_dist"] = me_collapse_dist
    out["connes_collapse_dist"] = cn_collapse_dist
    out["min_collapse_dist_OOM"] = min_collapse_dist

    # ======================================================================
    # VERDICT (set-membership) + 3-tuple [SIGN]
    # ======================================================================
    # sign_verdict: direction of collapse vs no-collapse.
    #   Predicted direction (the OPEN hypothesis's PASS leg): a selector COLLAPSES the spread
    #   (sign = "collapse"). PASS iff any axis collapses; FAIL iff none collapses (the
    #   no-collapse direction is itself substrate content, per the dual_prior discriminator —
    #   a non-collapse is NOT a null, but the SIGN of the directional prediction is then FAIL).
    sign_verdict = "PASS" if any_collapse else "FAIL"  # (local)

    # magnitude_verdict: min cross-functional collapse distance vs the 0.10 band.
    #   PASS iff min_collapse_dist <= 0.10 (band) ; INFO if in (0.10, 0.25] (near-collapse) ;
    #   FAIL if > 0.25 (no axis comes near a two-functional collapse).
    INFO_BAND_OOM = 0.25  # (local) near-collapse info band (an OOM-scale margin above PASS)
    out["INFO_BAND_OOM"] = INFO_BAND_OOM
    if min_collapse_dist <= COLLAPSE_BAND_OOM:
        magnitude_verdict = "PASS"   # (local)
    elif min_collapse_dist <= INFO_BAND_OOM:
        magnitude_verdict = "INFO"   # (local)
    else:
        magnitude_verdict = "FAIL"   # (local)

    # regime_verdict: are BOTH legs within their numerical regime of validity?
    #   maxent solve converged (constraints satisfied to 1e-9) AND Connes eval well-defined
    #   (positive diameter, GPU cross-check tiny). MARGINAL if one leg is borderline;
    #   BREAKDOWN if a leg failed numerically.
    connes_ok = bool(d_connes_diam > 0.0 and np.isfinite(d_connes_diam)
                     and (out["gpu_extremal_dev"] < 1e-6 or out["gpu_extremal_dev"] < 0))  # (local)
    if me_conv and connes_ok:
        regime_verdict = "VALID"     # (local)
    elif me_conv or connes_ok:
        regime_verdict = "MARGINAL"  # (local)
    else:
        regime_verdict = "BREAKDOWN"  # (local)
    out["maxent_converged_flag"] = me_conv
    out["connes_ok_flag"] = connes_ok

    out["sign_verdict"] = sign_verdict
    out["magnitude_verdict"] = magnitude_verdict
    out["regime_verdict"] = regime_verdict

    # ---- selection verdict (set-membership label) ----
    if any_collapse:
        selection_verdict = "SELECTED"   # (local) a new axis collapses the spread
    elif me_single_coincidence or cn_single_coincidence:
        selection_verdict = "COINCIDENCE-ONLY"  # (local) coincides with one functional only
    else:
        selection_verdict = "PLURALISM-WIDENED"  # (local) no collapse, no single-coincidence
    out["selection_verdict"] = selection_verdict

    # ======================================================================
    # Composite collapse (gate-verdicts.md deterministic rule)
    # ======================================================================
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"  # (local)
    elif sign_verdict == "FAIL":
        composite = "FAIL"  # (local)  <- no-collapse: PLURALISM-PERMANENT widened
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"  # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"  # (local)
    elif magnitude_verdict == "INFO":
        composite = "INFO"  # (local)
    else:
        composite = "PASS"  # (local)  <- SELECTED
    out["composite_verdict"] = composite

    # ---- dual-prior posterior re-allocation (plan §W3-2 dual_prior) ----
    # PASS -> 0.90 Track A (A_s typed, §EVOI.BF retired) ; FAIL -> 0.95 Track B
    # (pluralism permanent on wider axis-basis) ; INFO -> unchanged 0.10/0.90.
    if composite == "PASS":
        posterior = {"track_A_SELECTED": 0.90, "track_B_PLURALISM": 0.10}  # (local)
    elif composite == "FAIL":
        posterior = {"track_A_SELECTED": 0.05, "track_B_PLURALISM": 0.95}  # (local)
    else:
        posterior = {"track_A_SELECTED": 0.10, "track_B_PLURALISM": 0.90}  # (local)
    out["dual_prior_posterior"] = posterior

    # value payload string (no single-quote chars; the emit tool wraps value='...')
    value_str = (f"selection={selection_verdict}|spread_existing_OOM={spread_existing:.4f}|"
                 f"oom_maxent={oom_maxent:.4f}|oom_connes={oom_connes:.4f}|"
                 f"min_collapse_dist_OOM={min_collapse_dist:.4f}|"
                 f"any_collapse={int(any_collapse)}|band={COLLAPSE_BAND_OOM}")  # (local)
    out["value"] = value_str

    return out


# ---------------------------------------------------------------------------
# Section 5 — Plot
# ---------------------------------------------------------------------------
def make_plot(out: dict, path: Path):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14.0, 5.6))

    # --- LEFT: the FIVE functionals' A_s vs Planck (3 existing + 2 new axes) ---
    labels = ["impulse-\nquench", "UNIFIED-\nAS-79", "Parker\nadiab.",
              "maxent\n(AXIS-1)", "Connes\n(AXIS-2)"]
    ooms = [out["oom_impulse"], out["oom_unified"], out["oom_parker"],
            out["oom_maxent"], out["oom_connes"]]
    colors = ["#1f77b4", "#2ca02c", "#d62728", "#9467bd", "#ff7f0e"]
    is_new = [False, False, False, True, True]
    xpos = np.arange(5)
    bars = ax1.bar(xpos, ooms, color=colors, alpha=0.80, width=0.6,
                   edgecolor=["k" if n else "none" for n in is_new],
                   linewidth=[1.8 if n else 0 for n in is_new])
    for x, o in zip(xpos, ooms):
        ax1.text(x, o + 0.03, f"+{o:.3f}", ha="center", va="bottom", fontsize=8.5, fontweight="bold")
    # existing-spread band
    ax1.axhspan(out["oom_unified"], out["oom_parker"], color="gray", alpha=0.12,
                label=f"existing spread = {out['spread_existing_OOM']:.4f} OOM")
    # 0.10-OOM collapse band around impulse (the PASS target neighborhood)
    band = 0.10  # (local) plot band marker (= COLLAPSE_BAND_OOM)
    ax1.axhspan(out["oom_impulse"] - band, out["oom_impulse"] + band, color="gold", alpha=0.30,
                label=f"$\\pm$0.10 OOM collapse band (DIAGNOSTIC)")
    ax1.axhline(0.0, color="k", lw=0.8, ls=":")
    ax1.set_xticks(xpos)
    ax1.set_xticklabels(labels, fontsize=8.5)
    ax1.set_ylabel("$\\log_{10}(A_s / A_s^{Planck})$  [OOM]", fontsize=10)
    ax1.set_title(f"A_s across functionals (new axes outlined)\n"
                  f"min collapse-dist = {out['min_collapse_dist_OOM']:.4f} OOM "
                  f"$\\Rightarrow$ {out['selection_verdict']}", fontsize=9.5)
    ax1.legend(fontsize=7.5, loc="upper left")
    ax1.grid(True, axis="y", alpha=0.25)

    # --- RIGHT: AXIS-1 maxent occupation vs raw |beta|^2 (the redistribution) ---
    d = np.load(BOX_DELTA_NPZ, allow_pickle=True)
    kg = np.asarray(d["k_grid"], float)
    beta2 = np.asarray(d["beta2_spectrum"], float)
    # recompute maxent occ for the plot from stored multipliers
    lN, lE = out["maxent_lambda_N"], out["maxent_lambda_E"]
    x = np.clip(lN + lE * kg, 1e-12, 700.0)
    nk_me = 1.0 / np.expm1(x)
    ax2.plot(kg, beta2 * 1e7, "o-", color="#1f77b4", ms=4, lw=1.2,
             label="raw $|\\beta_k|^2$ (box-delta)")
    ax2.plot(kg, nk_me * 1e7, "s--", color="#9467bd", ms=4, lw=1.2,
             label="$n_k^{maxent}$ (Jaynes/GGE)")
    ax2.axvline(out["k_pivot"], color="gray", ls=":", lw=1.0,
                label=f"$k_{{pivot}}$={out['k_pivot']:.2f}")
    ax2.set_xlabel("$k$  [M_KK]", fontsize=9.5)
    ax2.set_ylabel("occupation $\\times 10^7$", fontsize=10)
    ax2.set_title(f"(AXIS-1) maxent redistribution: $n_k^{{maxent}}/|\\beta_k|^2_{{pivot}}$ "
                  f"= {out['nk_pivot_maxent']/out['beta2_pivot_closed_form']:.3f}\n"
                  f"$\\lambda_N$={lN:.3f} $\\lambda_E$={lE:.4f}  "
                  f"($d_C^{{diam}}$={out['d_connes_diameter']:.4f}, AXIS-2)", fontsize=9.0)
    ax2.legend(fontsize=8, loc="upper right")
    ax2.grid(True, alpha=0.25)

    fig.suptitle(f"{GATE_ID} — new-axis A_s selector  "
                 f"(composite: {out['composite_verdict']}; "
                 f"sign={out['sign_verdict']}/mag={out['magnitude_verdict']}/"
                 f"reg={out['regime_verdict']})", fontsize=11.0, fontweight="bold")
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(path, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 6 — verdict payload
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme, convention, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          extra_rows=None) -> dict:
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
# Section 7 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    out = compute()

    # ---- report ----
    print("=== EXISTING three-functional spread (the 1.2590-OOM spread to collapse) ===")
    print(f"  A_s Planck (anchor)             = {out['A_s_Planck']:.4e}")
    print(f"  impulse-quench A_s              = {out['A_s_impulse']:.6e}  (OOM +{out['oom_impulse']:.5f})")
    print(f"  UNIFIED-AS-79  A_s              = {out['A_s_unified']:.6e}  (OOM +{out['oom_unified']:.5f})")
    print(f"  Parker-adiab.  A_s              = {out['A_s_parker']:.6e}  (OOM +{out['oom_parker']:.5f})")
    print(f"  existing spread                 = {out['spread_existing_OOM']:.5f} OOM")
    print()
    print("=== AXIS-1 — maximum-entropy / Jaynes occupation ===")
    print(f"  <N> = sum|beta|^2               = {out['maxent_N_tot']:.6e}")
    print(f"  <E> = sum omega*|beta|^2        = {out['maxent_E_tot']:.6e}")
    print(f"  <E>/<N> mean energy per pair    = {out['maxent_mean_energy_per_pair']:.4f}")
    print(f"  Lagrange (lambda_N, lambda_E)   = ({out['maxent_lambda_N']:.6f}, {out['maxent_lambda_E']:.6f})")
    print(f"  constraint residuals (N, E)     = ({out['maxent_residual_N']:.3e}, {out['maxent_residual_E']:.3e})")
    print(f"  maxent converged?               = {out['maxent_converged']}")
    print(f"  n_k^maxent at pivot             = {out['nk_pivot_maxent']:.6e}  "
          f"(ratio to raw pivot {out['nk_pivot_maxent']/out['beta2_pivot_closed_form']:.4f})")
    print(f"  A_s^maxent (k_hat-norm, PRIMARY)= {out['A_s_maxent']:.6e}  (OOM +{out['oom_maxent']:.5f})")
    print(f"  A_s^maxent (pivot-norm)         = {out['A_s_maxent_pivot']:.6e}")
    print()
    print("=== AXIS-2 — Connes-distance-canonical normalization ===")
    print(f"  L12 D_K: lam_min/lam_max        = {out['lam_min']:.6f} / {out['lam_max']:.6f}  "
          f"({out['L12_n_evals']} evals)")
    print(f"  Connes diameter d_C (PRIMARY)   = {out['d_connes_diameter']:.6f}  = 1/(lam_max-lam_min)")
    print(f"  GPU extremal cross-check dev    = {out['gpu_extremal_dev']:.3e}  ({out['gpu_device']})")
    print(f"  A_s^Connes (diam-norm, PRIMARY) = {out['A_s_connes']:.6e}  (OOM +{out['oom_connes']:.5f})")
    print(f"  [x-check] d_C invmaxgap         = {out['d_connes_invmaxgap']:.6f}  "
          f"=> A_s={out['A_s_connes_invgap']:.4e} (OOM {out['oom_connes_invgap']:+.4f})")
    print(f"  [x-check] FS vacuum angle       = {out['fs_angle']:.6e}  "
          f"=> A_s={out['A_s_connes_fs']:.4e} (OOM {out['oom_connes_fs']:+.4f})")
    print()
    print("=== COLLAPSE TEST (PASS iff axis within 0.10 OOM of impulse AND a 2nd functional) ===")
    print(f"  AXIS-1 maxent: d(impulse/unified/parker) = "
          f"{out['maxent_d_impulse']:.4f}/{out['maxent_d_unified']:.4f}/{out['maxent_d_parker']:.4f}  "
          f"collapses={out['maxent_collapses']} (n_in_band={out['maxent_n_within_band']}, 2nd={out['maxent_which_2nd']})")
    print(f"  AXIS-2 Connes: d(impulse/unified/parker) = "
          f"{out['connes_d_impulse']:.4f}/{out['connes_d_unified']:.4f}/{out['connes_d_parker']:.4f}  "
          f"collapses={out['connes_collapses']} (n_in_band={out['connes_n_within_band']}, 2nd={out['connes_which_2nd']})")
    print(f"  min collapse distance           = {out['min_collapse_dist_OOM']:.5f} OOM  (band {COLLAPSE_BAND_OOM})")
    print(f"  any axis collapses?             = {out['any_axis_collapses']}")
    print()
    print(f"  SELECTION verdict (set)         = {out['selection_verdict']}")
    print(f"  sign / magnitude / regime       = {out['sign_verdict']} / "
          f"{out['magnitude_verdict']} / {out['regime_verdict']}")
    print(f"  dual-prior posterior            = {out['dual_prior_posterior']}")
    print()

    # ---- write npz ----
    npz_path = THIS_DIR / "s115_as_newaxis_selector.npz"  # (local)
    np.savez(
        npz_path,
        # existing spread
        A_s_Planck=out["A_s_Planck"],
        A_s_impulse=out["A_s_impulse"],
        A_s_unified=out["A_s_unified"],
        A_s_parker=out["A_s_parker"],
        oom_impulse=out["oom_impulse"],
        oom_unified=out["oom_unified"],
        oom_parker=out["oom_parker"],
        spread_existing_OOM=out["spread_existing_OOM"],
        # k_hat normalization
        xi_KZ=out["xi_KZ"],
        k_hat=out["k_hat"],
        beta2_khat_floor=out["beta2_khat_floor"],
        # AXIS-1 maxent
        maxent_lambda_N=out["maxent_lambda_N"],
        maxent_lambda_E=out["maxent_lambda_E"],
        maxent_residual_N=out["maxent_residual_N"],
        maxent_residual_E=out["maxent_residual_E"],
        maxent_converged=out["maxent_converged"],
        maxent_N_tot=out["maxent_N_tot"],
        maxent_E_tot=out["maxent_E_tot"],
        maxent_mean_energy_per_pair=out["maxent_mean_energy_per_pair"],
        nk_pivot_maxent=out["nk_pivot_maxent"],
        nk_khat_maxent=out["nk_khat_maxent"],
        A_s_maxent=out["A_s_maxent"],
        A_s_maxent_pivot=out["A_s_maxent_pivot"],
        A_s_maxent_khat=out["A_s_maxent_khat"],
        oom_maxent=out["oom_maxent"],
        # AXIS-2 Connes
        lam_min=out["lam_min"],
        lam_max=out["lam_max"],
        L12_n_evals=out["L12_n_evals"],
        d_connes_diameter=out["d_connes_diameter"],
        d_connes_invmaxgap=out["d_connes_invmaxgap"],
        fs_angle=out["fs_angle"],
        sum_beta2=out["sum_beta2"],
        vac_overlap=out["vac_overlap"],
        gpu_extremal_dev=out["gpu_extremal_dev"],
        A_s_connes=out["A_s_connes"],
        A_s_connes_invgap=out["A_s_connes_invgap"],
        A_s_connes_fs=out["A_s_connes_fs"],
        oom_connes=out["oom_connes"],
        oom_connes_invgap=out["oom_connes_invgap"],
        oom_connes_fs=out["oom_connes_fs"],
        # collapse test
        maxent_collapses=out["maxent_collapses"],
        connes_collapses=out["connes_collapses"],
        maxent_d_impulse=out["maxent_d_impulse"],
        maxent_d_unified=out["maxent_d_unified"],
        maxent_d_parker=out["maxent_d_parker"],
        connes_d_impulse=out["connes_d_impulse"],
        connes_d_unified=out["connes_d_unified"],
        connes_d_parker=out["connes_d_parker"],
        maxent_n_within_band=out["maxent_n_within_band"],
        connes_n_within_band=out["connes_n_within_band"],
        maxent_collapse_dist=out["maxent_collapse_dist"],
        connes_collapse_dist=out["connes_collapse_dist"],
        min_collapse_dist_OOM=out["min_collapse_dist_OOM"],
        any_axis_collapses=out["any_axis_collapses"],
        COLLAPSE_BAND_OOM=COLLAPSE_BAND_OOM,
        INFO_BAND_OOM=out["INFO_BAND_OOM"],
        # provenance / cross-checks
        N_modes=out["N_modes"],
        k_pivot=out["k_pivot"],
        beta2_pivot_closed_form=out["beta2_pivot_closed_form"],
        mu_pivot_sq=out["mu_pivot_sq"],
        # verdicts
        selection_verdict=out["selection_verdict"],
        sign_verdict=out["sign_verdict"],
        magnitude_verdict=out["magnitude_verdict"],
        regime_verdict=out["regime_verdict"],
        composite_verdict=out["composite_verdict"],
        dual_prior_track_A=out["dual_prior_posterior"]["track_A_SELECTED"],
        dual_prior_track_B=out["dual_prior_posterior"]["track_B_PLURALISM"],
        # dual-SHA
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        value=out["value"],
    )
    print(f"  wrote {npz_path.name}")

    # ---- write plot ----
    png_path = THIS_DIR / "s115_as_newaxis_selector.png"  # (local)
    make_plot(out, png_path)
    print(f"  wrote {png_path.name}")
    print()

    # ---- emit 4-tuple + payload ----
    tag = emit_4tuple(out["value"], SCHEME, CONVENTION, L_MAX)
    print(tag)

    # companion row: the two new-axis A_s values + the collapse outcome (audit-trail detail)
    detail_row = (f"# newaxis-detail: A_s_maxent={out['A_s_maxent']:.6e} (OOM {out['oom_maxent']:+.4f}); "
                  f"A_s_Connes={out['A_s_connes']:.6e} (OOM {out['oom_connes']:+.4f}); "
                  f"d_C_diam={out['d_connes_diameter']:.6f}; min_collapse_dist={out['min_collapse_dist_OOM']:.4f} OOM "
                  f"vs band {COLLAPSE_BAND_OOM}; maxent_2nd={out['maxent_which_2nd']}/connes_2nd={out['connes_which_2nd']}")  # (local)
    payload = print_verdict_payload(
        out["composite_verdict"], out["value"], audit_sha, content_sha,
        sign_verdict=out["sign_verdict"],
        magnitude_verdict=out["magnitude_verdict"],
        regime_verdict=out["regime_verdict"],
        extra_rows=[detail_row],
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {out['composite_verdict']} "
          f"(SELECTION={out['selection_verdict']}; wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
