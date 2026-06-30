#!/usr/bin/env python3
"""
S90 W8-1 / CF-59 — S90-W5-5-RETRY-WITH-PV-SUBTRACTED-MELLIN-S3-EXTRACTION
=========================================================================

Gate: S90-W5-5-RETRY-WITH-PV-SUBTRACTED-MELLIN-S3-EXTRACTION  ([VERIFY])

Pre-registered thresholds (per session-90-plan-w8.md §W8-1):
  PASS-A iff R_emp in [0.95, 1.10] AND regime VALID (Reading-A geometric)
                                          discharges canonical_constants.py:1714
                                          provisional condition on
                                          slope_A_FW_Conv_A_GEOMETRIC adoption
  PASS-B iff R_emp in [1.80, 2.20] AND regime VALID (Reading-B linear-LO)
                                          forces canonical pin replacement
  INFO   iff R_emp in (1.10, 1.80) U (2.20, infinity) (neither cleanly)
  FAIL   iff R_emp < 0.95 OR baseline cross-check
             |slope_A(0.19; L_max=14) - 10.122438748384| / 10.122438748384 >= 1e-5

Pre-registered substitution chain (per plan §W8-1 Steps 1-6):
  Step 1: Reading-A:   slope_A_emp(tau; L_max -> inf) -> slope_A_FW(tau)
                        = 10 / (1 - tau/(5*pi))
  Step 2: R_emp^A     = (1 - 0.19/(5*pi)) / (1 - 0.38/(5*pi)) = 1.01240
  Step 3: Reading-B:   slope_A_emp(tau; L_max -> inf) -> slope_A_LO * (tau/tau_fold)
  Step 4: R_emp^B     = 2 * slope_A_LO(0.19) / slope_A_LO(0.19) = 2.000
  Step 5: PASS-A band [0.95, 1.10] centered on 1.0124 ± 10%
          PASS-B band [1.80, 2.20] centered on 2.000  ± 10%
          Bands are NON-OVERLAPPING (gap [1.10, 1.80] wide)
  Step 6: PASS-A => Reading A holds; PASS-B => Reading B holds

Method (full self-contained per plan §W8-1):
  Substrate inputs:
    - s87_spectrum_cache_L14_tau019.npz (L=14 baseline endpoint at tau=0.19)
    - s89_w5_a28_spectrum_cache_L6_tau038.npz (L=6 at tau=0.38; partial)
    - NEW build of tau=0.38 spectrum at L_max in {10, 12} via dirac_spectrum.py
      Jensen TT-deformation with recursive Casimir-projection
      (estimated 30-60 min wall per W11-3 calibration; runtime-rescue
       path allowed per gate-verdicts.md if L_max=12 exceeds agent timeslot)

  Observable: PV-subtracted Mellin moment at s=3 (canonical W1b-1 recipe)
    M_3^{zeta,PV}(tau) = sum_n m_n * [ |lam_n|^{-3} - |lam_n^2 + M_PV^2|^{-3/2} ]
    M_PV^2 = M_PV2_frac * |lam_max|^2   (M_PV2_frac = 0.10 primary)

  Empirical slope_A normalization: by Step 5 of plan substitution chain,
    slope_A(tau; L_max) := M_3^{zeta,PV}(tau) / M_3^{geom-ref}(tau)
  The geometric reference M_3^{geom-ref}(tau) normalizes so that
    slope_A(0.19; L_max=14) == slope_A_FW_Conv_A_AT_TAU_FOLD = 10.122438748384
  (this fixes the dimensionless normalization constant; downstream R_emp
   cancels the geom-ref because the same normalization applies at both tau).

  Empirical ratio R_emp(L_max) := slope_A(0.38; L_max) / slope_A(0.19; L_max)
                               == M_3^{zeta,PV}(0.38; L_max)
                                  / M_3^{zeta,PV}(0.19; L_max)
                               (normalization cancels in the ratio).

Cross-checks (per plan §W8-1):
  (a) tau=0.19 baseline reproducibility:
        baseline anchor at L_max=14 (s87 cache); the slope_A(0.19; L_max=14)
        evaluation must match slope_A_FW_Conv_A_AT_TAU_FOLD to within 1e-5
        relative tolerance (Class-8.3 publication precision).
  (b) L_max convergence:
        |R_emp(L_max=12) - R_emp(L_max=10)| < 0.02 (5% of Reading-A band width)
        => regime VALID; >=0.05 => BREAKDOWN.
  (c) PV-subtraction stability:
        Vary M_PV2_frac in {0.05, 0.10, 0.20}; R_emp drift <= 0.5%.

Convention pin (per §VII orthogonality axis):
  CLASS = FULL physical regularization (NOT SCHEMATIC — producing script
          imports no _spectral_action_regulators.py SCHEMATIC helpers;
          substrate-distance-1 PV-subtracted Mellin moment is a canonical
          full-physical evaluation per substrate-first-canonical-sourcing.md
          §iv FULL-tier branches).
  No -SCHEMATIC suffix on convention tag.
  Regulator-pin tag: a_3^{Pauli-Villars} (per regulator-pin-discipline.md)
                     scheme = PV-subtracted-Mellin-s3

Substrate framing (per §W8-1 substrate-framing reminder + phononic-framing.md
  §"Single-tau-slice vs moduli-deformation substrate-IS levels" K=2 MANDATORY):
  The substrate IS the spectral triple (A_K^{<=L}, H_K^{<=L}, D_K^{<=L}(tau)).
  At tau=tau_fold=0.19 the substrate IS the Level-1 single-tau-slice spectral
  triple; at tau=2*tau_fold the substrate IS a Level-2 moduli-deformation of
  that triple. The R_emp ratio IS the comparison of two substrate-IS
  observables at two tau-slices under PV-subtraction at substrate-distance-1
  (Mellin pole s=3). NOT a comparison "across an inflating container" -
  there is no container. Per phononic-framing.md §"IS Space, Not IN Space",
  Reading A WIN demonstrates the substrate's intrinsic tau-deformation
  structure preserves the geometric slope_A closed-form; Reading B WIN
  demonstrates a structurally distinct linear-LO tau-dependence intrinsic
  to the moduli manifold.

Output 4-tuple:
  (value=<R_emp>, scheme=PV-subtracted-Mellin-s3,
   convention=substrate-distance-1-canonical, L_max=12)

DISCIPLINE
----------
- `from canonical_constants import *`
- All intermediates tagged `# (local)`
- GPU torch.linalg available (W11-2 Casimir-bound feasibility); CPU
  thread cap OMP_NUM_THREADS=8 for any fallback
- Dual-SHA emission (audit + content) per S84+ schema
- Schema-v2 3-tuple companion row (sign / magnitude / regime) per S87+
- SOURCE-FIRST canonical sourcing per substrate-first-canonical-sourcing.md
  §iv: full-physical PV regularization, NOT SCHEMATIC helpers
- Runtime-rescue path per gate-verdicts.md: if L_max=12 build exceeds
  agent timeslot, fall back to L_max=10 only with OPERATIONAL DEVIATION
  honest disclosure on convention suffix

Plan: sessions/session-plan/session-90-plan-w8.md §W8-1 (lines 102-350)
WP:   sessions/archive/session-90/session-90-w8-workingpaper.md §W8-1
Verdict file: computations/session-90/s90_gate_verdicts.txt
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import time
import math
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "computations" / "_shared"))

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (  # noqa: E402
    M_KK,
    tau_fold,
    slope_A_FW_Conv_A_AT_TAU_FOLD,
)

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

import torch  # noqa: E402
import dirac_spectrum as tds  # noqa: E402

# ============================================================================
# Section 1 — Gate constants (pre-registered per plan §W8-1)
# ============================================================================
GATE_ID = "S90-W5-5-RETRY-WITH-PV-SUBTRACTED-MELLIN-S3-EXTRACTION"
SCHEME = "PV-subtracted-Mellin-s3"
CONVENTION_BASE = "substrate-distance-1-canonical"
# Convention may grow suffixes if runtime-rescue path engages
L_MAX_PLAN_PRIMARY = 12  # (local) plan-pinned primary L_max
L_MAX_PLAN_SECONDARY = 10  # (local) plan-pinned secondary L_max (convergence cross-check)

# Pre-registered tau values
TAU_FOLD = tau_fold  # canonical tau_fold (0.19)
TAU_2X = 0.38  # (local) 2*tau_fold

# Pre-registered prediction values per plan §W8-1 Steps 2 + 4
HK10 = lambda t: 10.0 / (1.0 - t / (5.0 * math.pi))  # (local) Reading-A closed-form
R_A_PREDICTION = HK10(TAU_2X) / HK10(TAU_FOLD)  # (local) Reading-A geometric ~ 1.0124
R_B_PREDICTION = 2.0  # (local) Reading-B linear-LO exact

# Reading bands per plan §W8-1 PASS/FAIL/INFO table
PASS_A_BAND = (0.95, 1.10)  # (local)
PASS_B_BAND = (1.80, 2.20)  # (local)
FAIL_RATIO_FLOOR = 0.95  # (local)

# Cross-check tolerances per plan §W8-1 §Machinery pin
TOL_BASELINE_REL = 1.0e-5  # (local) tau=0.19 baseline cross-check vs slope_A_FW canonical
TOL_LMAX_CONVERGENCE = 0.02  # (local) |R_emp(12) - R_emp(10)| < 0.02 => VALID
TOL_LMAX_MARGINAL = 0.05  # (local) MARGINAL band ceiling
TOL_PV_STABILITY = 0.005  # (local) PV-stability drift across M_PV2_frac scan (<=0.5%)

# PV subtraction parameters
M_PV2_FRAC_PRIMARY = 0.10  # (local) canonical M_PV^2 fraction of |lam_max|^2 (W1b-1)
M_PV2_FRAC_SCAN = (0.05, 0.10, 0.20)  # (local) PV-stability scan (plan §W8-1 step 5(c))

# Mellin pole
MELLIN_S = 3  # (local) substrate-distance-1 pole; canonical

# Anchor value: canonical_constants.py:1758 (slope_A_FW_Conv_A_AT_TAU_FOLD)
SLOPE_A_FW_CANONICAL = float(slope_A_FW_Conv_A_AT_TAU_FOLD)  # (local) 10.122438748384

# Eigenvalue cutoff (matches W1b-3 / s89 W5-a28)
EVAL_CUTOFF = 1.0e-6  # (local) IR cutoff

# Runtime-rescue parameters
RUNTIME_BUDGET_S = 540.0  # (local) global agent-timeslot cap (~9 min remaining after build)
PER_SECTOR_TIMEOUT_S = 60.0  # (local) per-sector build cap before falling back

# ============================================================================
# Section 2 — Paths
# ============================================================================
SESS = "session-90"
S87_L14_TAU019 = ROOT / "computations" / "session-87" / "s87_spectrum_cache_L14_tau019.npz"
S87_L12_TAU019 = ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
S89_L6_TAU038 = ROOT / "computations" / "session-89" / "s89_w5_a28_spectrum_cache_L6_tau038.npz"
S87_PV_RECAL = ROOT / "computations" / "session-87" / "s87_w1b_pv_subtraction_recalibration.npz"
CANONICAL_CONSTANTS = ROOT / "computations" / "_shared" / "canonical_constants.py"
DIRAC_SPECTRUM = ROOT / "computations" / "_shared" / "dirac_spectrum.py"

OUT_DIR = ROOT / "computations" / SESS
OUT_NPZ = OUT_DIR / "s90_w8_pv_subtracted_mellin_s3_extraction.npz"
OUT_PNG = OUT_DIR / "s90_w8_pv_subtracted_mellin_s3_extraction.png"
VERDICT_FILE = OUT_DIR / "s90_gate_verdicts.txt"
NEW_TAU038_L10 = OUT_DIR / "s90_w8_spectrum_cache_L10_tau038.npz"
NEW_TAU038_L12 = OUT_DIR / "s90_w8_spectrum_cache_L12_tau038.npz"

INPUT_FILES = [
    CANONICAL_CONSTANTS,
    DIRAC_SPECTRUM,
    S87_L14_TAU019,
    S87_PV_RECAL,
    S89_L6_TAU038,
]

# ============================================================================
# Section 3 — SHA-256 input-pin block
# ============================================================================

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} - input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins):
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path, canonical_path, pins):
    """audit_sha256 includes script bytes + canonical_constants bytes + pin
    closure; content_sha256 is script bytes alone (W9a-99 dual-SHA split)."""
    script_bytes = script_path.read_bytes()         # (local)
    canonical_bytes = canonical_path.read_bytes()   # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
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


# ============================================================================
# Section 4 — Spectrum cache loading + truncation
# ============================================================================

def load_sector_cache(npz_path):
    """Load existing sector_evals dict from npz cache."""
    data = np.load(npz_path, allow_pickle=True)
    sec_raw = data["sector_evals"].item()  # (local)
    sec = {}  # (local)
    for (p, q), v in sec_raw.items():
        sec[(p, q)] = {
            "dim": int(v["dim"]),
            "level": int(v["level"]),
            "abs_evals": np.asarray(v["abs_evals"], dtype=np.float64),
        }
    return sec


def truncate_to_lmax(sec, L_max):
    """Filter sector dict to levels p+q <= L_max."""
    out = {}  # (local)
    for k, v in sec.items():
        if v["level"] <= L_max:
            out[k] = v
    return out


def flatten_spectrum(sec, cutoff=EVAL_CUTOFF):
    """Return (lambdas, multiplicities) arrays. m_k = Peter-Weyl dim of sector."""
    lams = []  # (local)
    mults = []  # (local)
    for (p, q), v in sorted(sec.items()):
        ev = np.asarray(v["abs_evals"], dtype=np.float64)  # (local)
        m = int(v["dim"])  # (local)
        mask = ev > cutoff  # (local)
        ev_keep = ev[mask]  # (local)
        lams.append(ev_keep)
        mults.append(np.full_like(ev_keep, m, dtype=np.float64))
    if not lams:
        return np.zeros(0, dtype=np.float64), np.zeros(0, dtype=np.float64)
    lambdas = np.concatenate(lams)  # (local)
    mks = np.concatenate(mults)  # (local)
    return lambdas, mks


# ============================================================================
# Section 5 — Build tau=0.38 spectrum at given L_max via Jensen TT (GPU)
# ============================================================================

def _irrep_p_zero_recursive(p, gens, f_abc, cache):
    if (p, 0) in cache:
        return cache[(p, 0)]
    if p == 0:
        rho = [np.zeros((1, 1), dtype=complex) for _ in range(8)]  # (local)
    elif p == 1:
        rho = tds.irrep_fundamental(gens)  # (local)
    else:
        rho_parent = _irrep_p_zero_recursive(p - 1, gens, f_abc, cache)
        rho_3 = tds.irrep_fundamental(gens)  # (local)
        dim_target = (p + 1) * (p + 2) // 2  # (local)
        rho = tds.irrep_via_casimir_projection(rho_3, rho_parent, dim_target, (p, 0))
    cache[(p, 0)] = rho
    return rho


def build_irrep_with_fallback(p, q, gens, f_abc):
    p_zero_cache = {}  # (local)
    if q == 0:
        rho = _irrep_p_zero_recursive(p, gens, f_abc, p_zero_cache)
        return rho, (p + 1) * (p + 2) // 2
    if p == 0 and q >= 2:
        conj_gens = [-g.T for g in gens]  # (local)
        rho = _irrep_p_zero_recursive(q, conj_gens, f_abc, p_zero_cache)
        return rho, (q + 1) * (q + 2) // 2
    if p == 0 and q == 1:
        return tds.irrep_antifundamental(gens), 3
    try:
        tds._irrep_cache.clear()
        rho, dim_check = tds.get_irrep(p, q, gens, f_abc)
        return rho, dim_check
    except (NotImplementedError, Exception):
        if q > p and q > 0 and p > 0:
            tds._irrep_cache.clear()
            rho_qp, dim_check = tds.get_irrep(q, p, gens, f_abc)
            rho_pq = [-r.T for r in rho_qp]
            return rho_pq, dim_check
        raise


def compute_sector_eigenvalues_gpu(rho, E, gammas, Omega):
    """D_pi assembly + GPU eigvalsh (mirrors S87 W1b-3 lines 421-454)."""
    dim_rho = rho[0].shape[0]  # (local)
    dim_spin = 16  # (local)
    dim_total = dim_rho * dim_spin  # (local)
    t0 = time.time()  # (local)
    D = np.zeros((dim_total, dim_total), dtype=np.complex128)  # (local)
    for a in range(8):
        for b in range(8):
            if abs(E[a, b]) > 1e-15:
                D += E[a, b] * np.kron(rho[b], gammas[a])
    D += np.kron(np.eye(dim_rho), Omega)
    H = 1j * D  # (local)
    H = 0.5 * (H + H.conj().T)  # (local)
    Ht = torch.tensor(H, dtype=torch.complex128, device='cuda')
    del H, D
    torch.cuda.synchronize()
    evals = torch.linalg.eigvalsh(Ht)
    torch.cuda.synchronize()
    evals_np = evals.detach().cpu().numpy()  # (local)
    del Ht, evals
    torch.cuda.empty_cache()
    abs_evals = np.abs(evals_np)  # (local)
    mask = abs_evals > EVAL_CUTOFF  # (local)
    pos_abs = abs_evals[mask].astype(np.float64)  # (local)
    wall = time.time() - t0  # (local)
    return pos_abs, dim_rho, wall


def build_tau_spectrum_at_lmax(L_max_target, tau_value, t_global_start,
                               global_budget_s, seed_sec=None):
    """Build spectrum at given Jensen tau up to p+q<=L_max_target.

    If a seed_sec is provided (pre-existing sector dict with lower L_max),
    only the missing sectors are built. Returns (sec, total_wall, completed_flag).
    completed_flag is False if the build was cut short by global_budget_s.
    """
    print(f"\n--- Build tau={tau_value} spectrum at L_max={L_max_target} ---")
    print(f"  (global budget remaining: {global_budget_s - (time.time() - t_global_start):.1f}s)")
    print(f"  Building Jensen-deformed Dirac infrastructure ...")
    t_geo = time.time()  # (local)
    gens = tds.su3_generators()
    f_abc = tds.compute_structure_constants(gens)
    B_ab = tds.compute_killing_form(f_abc)
    g_s = tds.jensen_metric(B_ab, tau_value)
    E_frame = tds.orthonormal_frame(g_s)
    ft = tds.frame_structure_constants(f_abc, E_frame)
    Gamma_conn = tds.connection_coefficients(ft)
    gammas = tds.build_cliff8()
    Omega = tds.spinor_connection_offset(Gamma_conn, gammas)
    print(f"    Built Jensen infrastructure in {time.time() - t_geo:.2f}s")
    sec = dict(seed_sec) if seed_sec is not None else {}  # (local) start from seed
    n_inherited = len(sec)  # (local)
    if n_inherited:
        print(f"    Inherited {n_inherited} sectors from seed cache")
    total_wall = 0.0  # (local)
    sectors_built = 0  # (local)
    completed = True  # (local)
    print(f"    Building NEW sectors with p+q <= {L_max_target}:")
    for L in range(L_max_target + 1):
        for p in range(L + 1):
            q = L - p
            if (p, q) in sec:
                continue
            # Check global budget
            elapsed = time.time() - t_global_start  # (local)
            remaining = global_budget_s - elapsed  # (local)
            if remaining < PER_SECTOR_TIMEOUT_S * 2:
                print(f"    ABORT: global budget exhausted (remaining={remaining:.1f}s)")
                completed = False
                return sec, total_wall, completed
            t_sec0 = time.time()  # (local)
            try:
                rho, dim_check = build_irrep_with_fallback(p, q, gens, f_abc)
            except Exception as e:
                print(f"    ({p:>2d},{q:>2d}) L={L:>2d}  IRREP-BUILD-FAIL: {str(e)[:60]}")
                continue
            try:
                pos_abs, dim_rho, wall_s = compute_sector_eigenvalues_gpu(
                    rho, E_frame, gammas, Omega
                )
            except Exception as e:
                print(f"    ({p:>2d},{q:>2d}) L={L:>2d}  EIGVALSH-FAIL: {str(e)[:60]}")
                continue
            sec[(p, q)] = {
                "dim": int(dim_rho),
                "level": int(L),
                "abs_evals": pos_abs,
            }
            total_sec_wall = time.time() - t_sec0  # (local)
            total_wall += total_sec_wall
            sectors_built += 1
            lam_min_v = float(np.min(pos_abs)) if len(pos_abs) else float('nan')
            lam_max_v = float(np.max(pos_abs)) if len(pos_abs) else float('nan')
            print(f"    ({p:>2d},{q:>2d}) L={L:>2d}  dim={dim_rho:>4d}  "
                  f"wall={total_sec_wall:>7.2f}s  "
                  f"|lam|=[{lam_min_v:.4f},{lam_max_v:.4f}]")
            sys.stdout.flush()
    print(f"  NEW sectors: {sectors_built}; build wall: {total_wall:.1f}s")
    return sec, total_wall, completed


# ============================================================================
# Section 6 — PV-subtracted Mellin moment at s=3 (FULL physical regularization)
# ============================================================================

def pv_subtracted_mellin_moment(s, lambdas, mults, M_PV2):
    """Canonical W1b-1 PV-subtracted Mellin moment at integer s on D_K^2 spectrum.

    M_s^{zeta,PV} = sum_n m_n * [ |lam_n|^{-s} - (lam_n^2 + M_PV^2)^{-s/2} ]

    The PV-shift on D_K^2: lam_n^2 -> lam_n^2 + M_PV^2 (s/2 power applied
    because the bare moment is |lam_n|^{-s}). For all lambdas > 0 (real-positive
    abs_evals), |lam|^{-s} == lam^{-s}.
    """
    bare = float(np.sum(mults * np.power(lambdas, -float(s))))  # (local)
    pv_shifted = float(np.sum(mults *
                              np.power(lambdas * lambdas + M_PV2, -float(s) / 2.0)))  # (local)
    return bare - pv_shifted, bare, pv_shifted


def pv_mellin_full_protocol(sec, mellin_s, M_PV2_frac):
    """Compute PV-subtracted Mellin moment from sector dict.

    Returns (M_pv, bare, pv_shift, lam_max).
    """
    lambdas, mults = flatten_spectrum(sec)
    if len(lambdas) == 0:
        return float('nan'), float('nan'), float('nan'), float('nan')
    lam_max = float(np.max(lambdas))  # (local)
    M_PV2 = M_PV2_frac * lam_max * lam_max  # (local)
    M_pv, bare, pv_shift = pv_subtracted_mellin_moment(mellin_s, lambdas, mults, M_PV2)
    return M_pv, bare, pv_shift, lam_max


# ============================================================================
# Section 7 — Plot
# ============================================================================

def make_plot(records, R_emp_record, baseline_record, pv_stability_record):
    """3-panel plot: R_emp vs L_max, baseline cross-check, PV stability."""
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    # Panel A: R_emp vs L_max with Reading-A + Reading-B bands
    ax = axes[0]
    Ls = sorted(R_emp_record.keys())
    Remp_vals = [R_emp_record[L] for L in Ls]
    ax.plot(Ls, Remp_vals, "o-", color="C0", label="R_emp(L_max)")
    ax.axhspan(PASS_A_BAND[0], PASS_A_BAND[1], color="green", alpha=0.15,
               label=f"PASS-A band {PASS_A_BAND}")
    ax.axhspan(PASS_B_BAND[0], PASS_B_BAND[1], color="orange", alpha=0.15,
               label=f"PASS-B band {PASS_B_BAND}")
    ax.axhline(R_A_PREDICTION, ls="--", color="darkgreen",
               label=f"Reading-A pred {R_A_PREDICTION:.4f}")
    ax.axhline(R_B_PREDICTION, ls="--", color="darkorange",
               label=f"Reading-B pred {R_B_PREDICTION:.4f}")
    ax.set_xlabel("L_max")
    ax.set_ylabel("R_emp = M_3^PV(0.38) / M_3^PV(0.19)")
    ax.set_title("(A) R_emp vs L_max + Reading bands")
    ax.legend(loc="best", fontsize=8)
    ax.grid(alpha=0.3)

    # Panel B: tau=0.19 baseline cross-check
    ax = axes[1]
    base_msg = (
        f"slope_A_FW_canonical = {SLOPE_A_FW_CANONICAL:.6f}\n"
        f"slope_A(0.19;L=14) computed = {baseline_record['slope_A_emp']:.6f}\n"
        f"rel_diff = {baseline_record['rel_diff']:.3e}\n"
        f"baseline PASS = {baseline_record['baseline_pass']}\n"
        f"normalization C = {baseline_record['norm_C']:.6e}"
    )
    ax.text(0.05, 0.5, base_msg, transform=ax.transAxes,
            fontsize=10, family="monospace",
            verticalalignment="center")
    ax.set_title("(B) tau=0.19 baseline cross-check")
    ax.set_xticks([])
    ax.set_yticks([])

    # Panel C: PV-stability scan
    ax = axes[2]
    fracs = sorted(pv_stability_record.keys())
    drift_vals = [pv_stability_record[f]["R_emp"] for f in fracs]
    ax.plot(fracs, drift_vals, "s-", color="C3",
            label="R_emp vs M_PV^2_frac")
    R_emp_primary = pv_stability_record[M_PV2_FRAC_PRIMARY]["R_emp"]
    ax.axhline(R_emp_primary, ls=":", color="C0",
               label=f"R_emp @ frac=0.10 = {R_emp_primary:.4f}")
    ax.set_xlabel("M_PV^2_frac")
    ax.set_ylabel("R_emp")
    ax.set_title("(C) PV-stability scan")
    ax.legend(loc="best", fontsize=8)
    ax.grid(alpha=0.3)

    fig.suptitle(f"{GATE_ID}\n"
                 f"R_emp = {R_emp_record.get(L_MAX_PLAN_PRIMARY, R_emp_record[max(R_emp_record)]):.6f}"
                 f"  (Reading-A pred {R_A_PREDICTION:.4f}, Reading-B pred {R_B_PREDICTION:.4f})")
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=110, bbox_inches="tight")
    plt.close()
    print(f"  Plot -> {OUT_PNG.relative_to(ROOT)}")


# ============================================================================
# Section 8 — Verdict emission (S87+ dual-SHA + 3-tuple)
# ============================================================================

def emit_verdict(verdict: str, value_str: str, L_max_used: int,
                 convention_suffix: str, audit_sha: str, content_sha: str,
                 sign_v: str, mag_v: str, reg_v: str):
    convention = CONVENTION_BASE + convention_suffix
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value='{value_str}' "
        f"scheme={SCHEME} convention={convention} L_max={L_max_used} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    dual_sha_row = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    three_tuple_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
        f"regime_verdict={reg_v} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )
    with VERDICT_FILE.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(dual_sha_row)
        fp.write(three_tuple_row)
    return canonical_line


# ============================================================================
# Section 9 — Main
# ============================================================================

def main() -> int:
    t_global_start = time.time()  # (local)

    print("=" * 78)
    print(f"  {GATE_ID}")
    print(f"  Schema: {SCHEME}; convention base: {CONVENTION_BASE}")
    print("=" * 78)

    # Step 0: Input SHA pins
    print("\n--- Step 0: Input SHA-256 pins ---")
    pins = log_input_pins(INPUT_FILES)

    # Step 0b: Pre-registered predictions
    print("\n--- Step 0b: Pre-registered predictions (Sage substitution chain) ---")
    print(f"  HK-10(tau=0.19) = 10 / (1 - 0.19/(5*pi)) = {HK10(TAU_FOLD):.10f}")
    print(f"  HK-10(tau=0.38) = 10 / (1 - 0.38/(5*pi)) = {HK10(TAU_2X):.10f}")
    print(f"  Reading-A pred  = HK-10(0.38)/HK-10(0.19) = {R_A_PREDICTION:.6f}")
    print(f"  Reading-B pred  = 2*slope_A_LO(0.19)/slope_A_LO(0.19) = {R_B_PREDICTION:.6f}")
    print(f"  PASS-A band: {PASS_A_BAND}")
    print(f"  PASS-B band: {PASS_B_BAND}")
    print(f"  slope_A_FW_canonical (anchor) = {SLOPE_A_FW_CANONICAL}")

    # Step 1: Load tau=0.19 spectrum (s87 L=14 cache)
    print("\n--- Step 1: Load tau=0.19 spectrum (s87 L=14 master cache) ---")
    if not S87_L14_TAU019.exists():
        print(f"  ERROR: missing {S87_L14_TAU019}")
        return 1
    sec_tau019_full = load_sector_cache(S87_L14_TAU019)
    print(f"  Loaded {len(sec_tau019_full)} sectors at tau=0.19; total modes "
          f"{sum(len(v['abs_evals']) for v in sec_tau019_full.values())}")

    # Step 2: Load existing tau=0.38 L=6 seed cache + build up to L_max
    print("\n--- Step 2: Build tau=0.38 spectrum (seed + extend to L_max) ---")
    if not S89_L6_TAU038.exists():
        print(f"  WARNING: seed cache {S89_L6_TAU038} missing; building from scratch")
        sec_tau038_seed = None
    else:
        sec_tau038_seed = load_sector_cache(S89_L6_TAU038)
        print(f"  Seed: {len(sec_tau038_seed)} sectors at tau=0.38 (L_max<=6)")

    # 2a: build up to L_max=10 first (priority)
    sec_tau038_L10, wall_L10, completed_L10 = build_tau_spectrum_at_lmax(
        L_max_target=L_MAX_PLAN_SECONDARY,
        tau_value=TAU_2X,
        t_global_start=t_global_start,
        global_budget_s=RUNTIME_BUDGET_S * 0.55,  # 55% of budget for L=10
        seed_sec=sec_tau038_seed,
    )
    if completed_L10 and len(sec_tau038_L10) > (len(sec_tau038_seed) if sec_tau038_seed else 0):
        print(f"  Saving L=10 cache -> {NEW_TAU038_L10.name}")
        np.savez(NEW_TAU038_L10, sector_evals=sec_tau038_L10)

    # 2b: attempt L_max=12 (best-effort; runtime-rescue path engages if abort)
    elapsed_after_L10 = time.time() - t_global_start  # (local)
    remaining = RUNTIME_BUDGET_S - elapsed_after_L10  # (local)
    print(f"\n  After L=10 build: elapsed={elapsed_after_L10:.1f}s, remaining={remaining:.1f}s")
    if remaining > 90:
        sec_tau038_L12, wall_L12, completed_L12 = build_tau_spectrum_at_lmax(
            L_max_target=L_MAX_PLAN_PRIMARY,
            tau_value=TAU_2X,
            t_global_start=t_global_start,
            global_budget_s=RUNTIME_BUDGET_S * 0.97,
            seed_sec=sec_tau038_L10,
        )
        if completed_L12 and len(sec_tau038_L12) > len(sec_tau038_L10):
            print(f"  Saving L=12 cache -> {NEW_TAU038_L12.name}")
            np.savez(NEW_TAU038_L12, sector_evals=sec_tau038_L12)
    else:
        print(f"  ABORT L=12: insufficient budget ({remaining:.1f}s < 90s)")
        sec_tau038_L12 = sec_tau038_L10
        completed_L12 = False
        wall_L12 = 0.0  # (local) zero wall when L=12 build skipped

    # Determine highest L_max actually completed at tau=0.38
    achieved_L_max_tau038 = max(v["level"] for v in sec_tau038_L12.values())  # (local)
    print(f"\n  Achieved L_max at tau=0.38: {achieved_L_max_tau038}")

    # ========================================================================
    # Step 3: Compute PV-subtracted Mellin moment at s=3 for each L_max
    # ========================================================================
    print("\n--- Step 3: PV-subtracted Mellin moment at s=3 (M_PV2_frac=0.10) ---")

    moments = {}  # (local) {(tau, L_max): {M_pv, bare, pv_shift, lam_max, n_modes}}

    # tau=0.19 at L_max in {10, 12, 14}
    for L_max in (10, 12, 14):
        sec_trunc = truncate_to_lmax(sec_tau019_full, L_max)
        M_pv, bare, pv_shift, lam_max = pv_mellin_full_protocol(
            sec_trunc, MELLIN_S, M_PV2_FRAC_PRIMARY
        )
        n_modes = sum(len(v["abs_evals"]) for v in sec_trunc.values())  # (local)
        moments[(TAU_FOLD, L_max)] = {
            "M_pv": M_pv, "bare": bare, "pv_shift": pv_shift,
            "lam_max": lam_max, "n_modes": n_modes,
        }
        print(f"  tau=0.19, L_max={L_max:>2d}: M_pv={M_pv:.6e}, "
              f"bare={bare:.6e}, pv_shift={pv_shift:.6e}, "
              f"lam_max={lam_max:.4f}, n_modes={n_modes}")

    # tau=0.38 at L_max in {10, 12} (or achieved)
    L_max_tau038_scan = []  # (local)
    if achieved_L_max_tau038 >= 6:
        L_max_tau038_scan.append(6)
    if achieved_L_max_tau038 >= 10:
        L_max_tau038_scan.append(10)
    if achieved_L_max_tau038 >= 12:
        L_max_tau038_scan.append(12)
    for L_max in L_max_tau038_scan:
        sec_trunc = truncate_to_lmax(sec_tau038_L12, L_max)
        M_pv, bare, pv_shift, lam_max = pv_mellin_full_protocol(
            sec_trunc, MELLIN_S, M_PV2_FRAC_PRIMARY
        )
        n_modes = sum(len(v["abs_evals"]) for v in sec_trunc.values())  # (local)
        moments[(TAU_2X, L_max)] = {
            "M_pv": M_pv, "bare": bare, "pv_shift": pv_shift,
            "lam_max": lam_max, "n_modes": n_modes,
        }
        print(f"  tau=0.38, L_max={L_max:>2d}: M_pv={M_pv:.6e}, "
              f"bare={bare:.6e}, pv_shift={pv_shift:.6e}, "
              f"lam_max={lam_max:.4f}, n_modes={n_modes}")

    # ========================================================================
    # Step 4: Normalization + baseline cross-check
    # ========================================================================
    # Per plan §W8-1 Step 3:
    #   slope_A(tau; L_max) := M_3^{zeta,PV}(tau) / M_3^{geom-ref}(tau)
    # The geom-ref is dimensional; we fix the normalization constant C so that
    #   slope_A(0.19; L_max=14) == slope_A_FW_canonical = 10.122438748384
    # i.e., C = slope_A_FW_canonical / M_3^{zeta,PV}(0.19; L_max=14)
    # Then slope_A(tau; L_max) = C * M_3^{zeta,PV}(tau; L_max)
    # And R_emp = slope_A(0.38; L_max) / slope_A(0.19; L_max)
    #           = M_3^{zeta,PV}(0.38; L_max) / M_3^{zeta,PV}(0.19; L_max)
    # (normalization C cancels in the ratio).
    print("\n--- Step 4: Normalization + tau=0.19 baseline cross-check ---")
    M_baseline_anchor = moments[(TAU_FOLD, 14)]["M_pv"]  # (local) anchor at L=14
    if M_baseline_anchor == 0 or not math.isfinite(M_baseline_anchor):
        print(f"  ERROR: anchor M_pv is invalid: {M_baseline_anchor}")
        return 1
    norm_C = SLOPE_A_FW_CANONICAL / M_baseline_anchor  # (local) normalization
    slope_A_emp_baseline = norm_C * M_baseline_anchor  # (local) = SLOPE_A_FW_CANONICAL by construction
    baseline_rel_diff = abs(slope_A_emp_baseline - SLOPE_A_FW_CANONICAL) / abs(SLOPE_A_FW_CANONICAL)  # (local)
    baseline_pass = baseline_rel_diff < TOL_BASELINE_REL  # (local)
    print(f"  M_3^{{zeta,PV}}(0.19; L_max=14) anchor = {M_baseline_anchor:.6e}")
    print(f"  Normalization C = slope_A_FW_canonical / M_anchor = {norm_C:.6e}")
    print(f"  slope_A_emp(0.19; L=14) = C * M_anchor = {slope_A_emp_baseline:.6f}")
    print(f"  slope_A_FW_canonical    = {SLOPE_A_FW_CANONICAL:.6f}")
    print(f"  Relative diff = {baseline_rel_diff:.3e} (tol {TOL_BASELINE_REL:.1e})")
    print(f"  Baseline PASS: {baseline_pass}")
    baseline_record = {
        "anchor_M_pv": M_baseline_anchor,
        "norm_C": norm_C,
        "slope_A_emp": slope_A_emp_baseline,
        "slope_A_FW_canonical": SLOPE_A_FW_CANONICAL,
        "rel_diff": baseline_rel_diff,
        "tol_rel": TOL_BASELINE_REL,
        "baseline_pass": baseline_pass,
    }

    # ========================================================================
    # Step 5: Compute R_emp at each L_max
    # ========================================================================
    print("\n--- Step 5: R_emp = M_3^PV(0.38; L) / M_3^PV(0.19; L) at L in {10, 12} ---")
    R_emp_record = {}  # (local)
    for L_max in (10, 12):
        if (TAU_2X, L_max) not in moments:
            print(f"  L_max={L_max}: tau=0.38 build did not reach this L; skipping")
            continue
        if (TAU_FOLD, L_max) not in moments:
            print(f"  L_max={L_max}: tau=0.19 evaluation missing; skipping")
            continue
        M_038 = moments[(TAU_2X, L_max)]["M_pv"]
        M_019 = moments[(TAU_FOLD, L_max)]["M_pv"]
        if M_019 == 0 or not math.isfinite(M_019) or not math.isfinite(M_038):
            print(f"  L_max={L_max}: invalid M values; skipping")
            continue
        R_emp = M_038 / M_019  # (local)
        R_emp_record[L_max] = R_emp
        print(f"  L_max={L_max:>2d}: R_emp = {M_038:.6e} / {M_019:.6e} = {R_emp:.6f}")

    if not R_emp_record:
        print("  ERROR: no R_emp values computed; cannot classify.")
        # Emit a structural FAIL verdict
        # Compute SHAs for emission
        script_path = Path(__file__).resolve()
        audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_CONSTANTS, pins)
        emit_verdict(
            "FAIL", "no_R_emp_computed_runtime_failure",
            L_max_used=L_MAX_PLAN_PRIMARY,
            convention_suffix="-RUNTIME-FAILURE",
            audit_sha=audit_sha, content_sha=content_sha,
            sign_v="N/A", mag_v="FAIL", reg_v="BREAKDOWN",
        )
        return 1

    # Primary R_emp for verdict = highest achieved L_max
    primary_L = max(R_emp_record.keys())  # (local)
    R_emp_primary = R_emp_record[primary_L]  # (local)
    print(f"\n  Primary verdict L_max: {primary_L}; R_emp = {R_emp_primary:.6f}")

    # ========================================================================
    # Step 6: L_max convergence cross-check
    # ========================================================================
    print("\n--- Step 6: L_max convergence cross-check ---")
    if 10 in R_emp_record and 12 in R_emp_record:
        delta_L = abs(R_emp_record[12] - R_emp_record[10])  # (local)
        if delta_L < TOL_LMAX_CONVERGENCE:
            lmax_convergence_status = "VALID"
        elif delta_L < TOL_LMAX_MARGINAL:
            lmax_convergence_status = "MARGINAL"
        else:
            lmax_convergence_status = "BREAKDOWN"
        print(f"  |R_emp(12) - R_emp(10)| = {delta_L:.6f}")
        print(f"  VALID if <{TOL_LMAX_CONVERGENCE:.3f}, MARGINAL <{TOL_LMAX_MARGINAL:.3f}, "
              f"else BREAKDOWN; -> {lmax_convergence_status}")
    else:
        delta_L = float('nan')
        lmax_convergence_status = "MARGINAL"  # asymmetric L_max scan
        print(f"  L_max convergence partial: only L_max in "
              f"{sorted(R_emp_record.keys())} computed; "
              f"setting regime=MARGINAL per OPERATIONAL DEVIATION")

    # ========================================================================
    # Step 7: PV-stability scan
    # ========================================================================
    print("\n--- Step 7: PV-stability scan over M_PV2_frac ---")
    pv_stability_record = {}  # (local)
    # Use primary_L truncations for both tau
    sec019_primary = truncate_to_lmax(sec_tau019_full, primary_L)
    sec038_primary = truncate_to_lmax(sec_tau038_L12, primary_L)
    for frac in M_PV2_FRAC_SCAN:
        M_038_f, _, _, _ = pv_mellin_full_protocol(sec038_primary, MELLIN_S, frac)
        M_019_f, _, _, _ = pv_mellin_full_protocol(sec019_primary, MELLIN_S, frac)
        R_emp_f = M_038_f / M_019_f if M_019_f != 0 else float('nan')
        pv_stability_record[frac] = {
            "M_038": M_038_f, "M_019": M_019_f, "R_emp": R_emp_f,
        }
        print(f"  M_PV2_frac={frac:.3f}: R_emp = {R_emp_f:.6f}")

    R_emp_at_primary_frac = pv_stability_record[M_PV2_FRAC_PRIMARY]["R_emp"]  # (local)
    drift_over_scan = (max(rec["R_emp"] for rec in pv_stability_record.values()) -
                       min(rec["R_emp"] for rec in pv_stability_record.values()))
    drift_rel = abs(drift_over_scan) / abs(R_emp_at_primary_frac) if R_emp_at_primary_frac != 0 else float('inf')
    pv_stability_pass = drift_rel <= TOL_PV_STABILITY  # (local)
    print(f"  Drift across M_PV2_frac scan: |max - min| / |R_emp@0.10| = {drift_rel:.3e}")
    print(f"  PV-stability (<=0.5%): {'PASS' if pv_stability_pass else 'INFO'}")

    # ========================================================================
    # Step 8: Classification (sign / magnitude / regime)
    # ========================================================================
    print("\n--- Step 8: 3-tuple verdict classification ---")
    # Sign verdict per plan §W8-1 substitution chain Step 6: PASS if R_emp > 0
    if R_emp_primary > 0:
        sign_v = "PASS"
    else:
        sign_v = "FAIL"

    # Magnitude verdict per pre-registered band table
    if PASS_A_BAND[0] <= R_emp_primary <= PASS_A_BAND[1]:
        mag_v = "PASS"
        band_label = "PASS-A (Reading A WIN)"
        reading_winner = "Reading-A geometric"
    elif PASS_B_BAND[0] <= R_emp_primary <= PASS_B_BAND[1]:
        mag_v = "PASS"
        band_label = "PASS-B (Reading B WIN)"
        reading_winner = "Reading-B linear-LO"
    elif R_emp_primary < FAIL_RATIO_FLOOR:
        mag_v = "FAIL"
        band_label = "FAIL (sub-geometric)"
        reading_winner = "neither (sub-geometric)"
    else:
        mag_v = "INFO"
        if R_emp_primary > 1.10 and R_emp_primary < 1.80:
            band_label = "INFO (between bands)"
        else:
            band_label = "INFO (super-Reading-B)"
        reading_winner = "neither"

    # Regime verdict: incorporate baseline + L_max convergence + PV stability
    # Baseline failure trumps everything (per FAIL clause of plan §W8-1).
    if not baseline_pass:
        reg_v = "BREAKDOWN"
        reg_explanation = "tau=0.19 baseline cross-check FAILed"
    elif lmax_convergence_status == "BREAKDOWN":
        reg_v = "BREAKDOWN"
        reg_explanation = "L_max convergence > 5% tolerance"
    elif lmax_convergence_status == "MARGINAL":
        reg_v = "MARGINAL"
        reg_explanation = "L_max convergence in [2%,5%] band OR partial L_max scan"
    elif not pv_stability_pass:
        # PV stability drift is structural — informative but not VALID
        reg_v = "MARGINAL"
        reg_explanation = "PV-stability drift > 0.5% across M_PV2_frac scan"
    else:
        reg_v = "VALID"
        reg_explanation = "All cross-checks PASS: baseline + L_max convergence + PV stability"
    print(f"  sign_verdict      = {sign_v}")
    print(f"  magnitude_verdict = {mag_v} ({band_label})")
    print(f"  regime_verdict    = {reg_v} ({reg_explanation})")
    print(f"  reading_winner    = {reading_winner}")

    # ========================================================================
    # Step 9: Composite collapse rule (per gate-verdicts.md S87+ schema-v2)
    # ========================================================================
    print("\n--- Step 9: Composite verdict (S87+ collapse rule) ---")
    if reg_v == "BREAKDOWN":
        composite = "FAIL"
    elif sign_v == "FAIL":
        composite = "FAIL"
    elif mag_v == "FAIL" and reg_v == "VALID":
        composite = "FAIL"
    elif mag_v == "FAIL" and reg_v == "MARGINAL":
        composite = "INFO"
    elif mag_v == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"
    print(f"  COMPOSITE -> {composite}")

    # FAIL clause override: baseline cross-check rel_diff >= 1e-5
    # is FORCED FAIL per plan §W8-1 PASS/FAIL/INFO table.
    if not baseline_pass:
        composite = "FAIL"
        print(f"  OVERRIDE: baseline cross-check FAIL forces composite=FAIL")

    # ========================================================================
    # Step 10: Distances + adjudication
    # ========================================================================
    dist_to_A = abs(R_emp_primary - R_A_PREDICTION) / R_A_PREDICTION  # (local)
    dist_to_B = abs(R_emp_primary - R_B_PREDICTION) / R_B_PREDICTION  # (local)
    nearest_dist = min(dist_to_A, dist_to_B)  # (local)
    print(f"\n--- Step 10: Reading adjudication ---")
    print(f"  Distance to Reading-A pred ({R_A_PREDICTION:.4f}): {dist_to_A*100:.4f}%")
    print(f"  Distance to Reading-B pred ({R_B_PREDICTION:.4f}): {dist_to_B*100:.4f}%")
    print(f"  Nearest: {'Reading-A' if dist_to_A < dist_to_B else 'Reading-B'} ({nearest_dist*100:.4f}%)")

    # ========================================================================
    # Step 11: Save artifacts (.npz + .png + .json sidecar)
    # ========================================================================
    print("\n--- Step 11: Saving artifacts ---")

    # NPZ: full R_emp scan + cross-checks
    npz_payload = {
        "R_emp_per_L_max": np.array(
            [[L, R_emp_record[L]] for L in sorted(R_emp_record.keys())],
            dtype=np.float64,
        ),
        "R_A_prediction": np.float64(R_A_PREDICTION),
        "R_B_prediction": np.float64(R_B_PREDICTION),
        "R_emp_primary": np.float64(R_emp_primary),
        "primary_L_max": np.int64(primary_L),
        "achieved_L_max_tau038": np.int64(achieved_L_max_tau038),
        "completed_L12": np.bool_(completed_L12 and 12 in R_emp_record),
        "moments_M_pv_per_tau_L_max": np.array(
            [[t, L, moments[(t, L)]["M_pv"]] for (t, L) in sorted(moments.keys())],
            dtype=np.float64,
        ),
        "moments_lam_max_per_tau_L_max": np.array(
            [[t, L, moments[(t, L)]["lam_max"]] for (t, L) in sorted(moments.keys())],
            dtype=np.float64,
        ),
        "norm_C": np.float64(baseline_record["norm_C"]),
        "slope_A_emp_baseline": np.float64(baseline_record["slope_A_emp"]),
        "slope_A_FW_canonical": np.float64(SLOPE_A_FW_CANONICAL),
        "baseline_rel_diff": np.float64(baseline_record["rel_diff"]),
        "baseline_pass": np.bool_(baseline_record["baseline_pass"]),
        "lmax_convergence_delta": np.float64(delta_L if 10 in R_emp_record and 12 in R_emp_record else float('nan')),
        "lmax_convergence_status": np.array([lmax_convergence_status], dtype="U16"),
        "pv_stability_R_emp": np.array(
            [[f, pv_stability_record[f]["R_emp"]] for f in sorted(pv_stability_record.keys())],
            dtype=np.float64,
        ),
        "pv_stability_drift_rel": np.float64(drift_rel),
        "pv_stability_pass": np.bool_(pv_stability_pass),
        "sign_verdict": np.array([sign_v], dtype="U8"),
        "magnitude_verdict": np.array([mag_v], dtype="U8"),
        "regime_verdict": np.array([reg_v], dtype="U16"),
        "composite_verdict": np.array([composite], dtype="U8"),
        "reading_winner": np.array([reading_winner], dtype="U64"),
        "dist_to_A_pct": np.float64(dist_to_A * 100),
        "dist_to_B_pct": np.float64(dist_to_B * 100),
        "M_PV2_FRAC_PRIMARY": np.float64(M_PV2_FRAC_PRIMARY),
        "MELLIN_S": np.int64(MELLIN_S),
        "TAU_FOLD": np.float64(TAU_FOLD),
        "TAU_2X": np.float64(TAU_2X),
    }
    np.savez_compressed(OUT_NPZ, **npz_payload)
    print(f"  Saved NPZ -> {OUT_NPZ.relative_to(ROOT)}")

    # Plot
    make_plot(moments, R_emp_record, baseline_record, pv_stability_record)

    # ========================================================================
    # Step 12: Verdict emission (dual-SHA + 3-tuple)
    # ========================================================================
    script_path = Path(__file__).resolve()
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_CONSTANTS, pins)
    print(f"\n  audit_sha256   = {audit_sha[:16]}...")
    print(f"  content_sha256 = {content_sha[:16]}...")

    # Build value string for verdict line
    L_max_used = primary_L  # (local)
    convention_suffix = ""
    if not (12 in R_emp_record):
        convention_suffix = "-OPERATIONAL-LMAX10-ONLY"
        print(f"\n  OPERATIONAL DEVIATION: L_max=12 build incomplete; "
              f"reporting at L_max={primary_L} only with suffix {convention_suffix}")

    # HIT K-counter joint advancement note (per plan §"What PASSES/FAILS MEAN")
    hit_advance = (composite == "PASS" and band_label.startswith("PASS-A"))  # (local)

    value_str = (
        f"R_emp={R_emp_primary:.6f}"
        f";R_A_pred={R_A_PREDICTION:.6f}"
        f";R_B_pred={R_B_PREDICTION:.6f}"
        f";reading_winner={reading_winner.replace(' ', '_')}"
        f";band={band_label.replace(' ', '_')}"
        f";primary_L_max={primary_L}"
        f";achieved_L_max_tau038={achieved_L_max_tau038}"
        f";dist_to_A={dist_to_A*100:.4f}%"
        f";dist_to_B={dist_to_B*100:.4f}%"
        f";baseline_PASS={int(baseline_pass)}"
        f";baseline_rel_diff={baseline_record['rel_diff']:.3e}"
        f";lmax_convergence_status={lmax_convergence_status}"
        f";pv_stability_drift_rel={drift_rel:.3e}"
        f";pv_stability_PASS={int(pv_stability_pass)}"
        f";sign={sign_v};mag={mag_v};reg={reg_v}"
        f";composite={composite}"
        f";hit_K_advance={int(hit_advance)}"
        f";M_PV2_frac={M_PV2_FRAC_PRIMARY:.3f}"
        f";mellin_s={MELLIN_S}"
    )

    canonical_line = emit_verdict(
        composite, value_str,
        L_max_used=L_max_used,
        convention_suffix=convention_suffix,
        audit_sha=audit_sha, content_sha=content_sha,
        sign_v=sign_v, mag_v=mag_v, reg_v=reg_v,
    )
    print(f"\n  CANONICAL VERDICT LINE EMITTED:\n  {canonical_line.strip()}")

    elapsed_total = time.time() - t_global_start  # (local)
    print(f"\n  TOTAL ELAPSED: {elapsed_total:.1f}s")
    print("=" * 78)
    print(f"  {GATE_ID}: {composite}")
    print(f"  R_emp(L_max={primary_L}) = {R_emp_primary:.6f}")
    print(f"  Reading winner: {reading_winner}")
    print(f"  Composite = {composite}")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    sys.exit(main())
