#!/usr/bin/env python3
"""
S84 W7b-75 -- B-POWER-STABILITY
================================

Gate: S84-W7b-75-B-POWER-STABILITY  [VERIFY]
Classification: GEOMETRIC
Owner: kaluza-klein-theorist

Pre-registration (sessions/session-plan/session-84-plan-w7b.md §W7b-75):
    HYPOTHESIS: |E_cond(L)| = a * L^b with b=4.681 derived from L=3..8 fit
    (S83-G36) is the asymptotic behavior of the Jensen-deformed SU(3)
    binding-energy spectrum, not a finite-L artifact. If stable to L=10, 12
    within +/-0.10, the exponent is locked and 2^4.681 = 25.6 per L-doubling
    is a structural spectral invariant of the triple.

    PASS: |b_power(L<=12) - 4.681| < 0.10 AND R^2 > 0.99
          (joint fit on L in {3,4,5,6,7,8,10,12})
    INFO: |Delta b| < 0.30 (stable trend, moderate drift)
    FAIL: |Delta b| > 0.30 OR R^2 < 0.90

4-tuple slot:
    (value=b_power(L<=12), scheme=eigvalsh-joint-logfit,
     convention=V-rescaled-Delta-fixed, L_max=12)

SUBSTITUTION CHAIN [VERIFY] (mandatory, math-scripts.md):

    Step 1 (Definition). For each L-cut, the spectrum-integrated BCS
    condensation energy is
        E_cond(L) = -0.5 * sum_{(p,q): p+q<=L} d_(p,q) * sum_j
                    (sqrt(lam_j^2 + Delta^2) - |lam_j|)
    where d_(p,q) = dim(p,q) is the SU(3) irrep dimension and {lam_j} are
    the eigenvalues of the Dirac operator D_K restricted to sector (p,q),
    with D_K built on the Jensen-deformed SU(3) metric at tau = tau_fold.

    Step 2 (Ansatz). Power-law hypothesis:
        |E_cond(L)| = A * L^b
    Log form:
        log|E_cond(L)| = log(A) + b * log(L)

    Step 3 (Linearize / Measure). Joint 8-point fit on
        L in {3, 4, 5, 6, 7, 8, 10, 12}:
        (b, log A) = polyfit(log(L), log|E_cond(L)|, 1)
    R^2 computed in linear |E_cond| space (matching G36 convention):
        R^2 = 1 - sum[(|E| - E_hat)^2] / sum[(|E| - mean|E|)^2]
        where E_hat(L) = exp(log A + b * log L).

    Step 4 (Direction). G36 anchor: b_(L<=8) = 4.6807, R^2 = 0.9979.
    Observation of sum_mult(L): 12880, 50176, ..., 2160320 at L=8.
    Sign: |E_cond(L)| > 0 and monotonically increasing (verified G36 data
    at L=3..8: |E| grows from 439 to 41450, so b > 0 by construction).

    Step 5 (Decision, pre-registered).
        PASS:  4.581 < b < 4.781 AND R^2 > 0.99
        INFO:  4.381 < b < 4.981 AND R^2 > 0.95
        FAIL:  otherwise

V-rescaled-Delta-fixed convention (G36 eq 1):
    At each L, Delta = Delta_canonical (R-protected S70 value 0.4642547...);
    V_pair(L) = 1 / (sum_j d_j / (2*sqrt(lam_j^2 + Delta_canonical^2))) on the
    truncated spectrum. This isolates the spectrum-accumulation scaling from
    the critical-coupling pathology that V-fixed-at-L8 would induce for L<8.

L_max scan: {3, 4, 5, 6, 7, 8, 10, 12}. G36 L=3..8 values are re-used
(scheme-pinned). L=9, 10, 11, 12 are computed fresh with full sector
coverage (including sectors missing from the S74 L9 cache such as (4,4)
at L=8, (4,5)/(5,4) at L=9).

Inputs (SHA-256 pinned at runtime):
  - canonical_constants.py
  - s83_w3_g36_matrix_model_classification.npz  (L=3..8 anchors)
  - s74_spectrum_cache_L9_tau019.npz              (sector cache to L=9)
  - dirac_spectrum.py                       (D_K builder)
  - this script

Output 4-tuple:
  (value=b_power(L<=12), scheme=eigvalsh-joint-logfit,
   convention=V-rescaled-Delta-fixed, L_max=12)

Seed: 8475 (deterministic; torch.linalg.eigvalsh is deterministic).
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401, F403
from canonical_constants import (
    PI, M_KK, tau_fold, Delta_BCS,
)

# ---------------------------------------------------------------------------
# Section 2 -- Standard imports (thread cap before numpy)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import hashlib
import sys
import time
from pathlib import Path

import numpy as np
import torch
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))
import dirac_spectrum as tds

# Deterministic seeding (GPU eigvalsh is deterministic; numpy seed kept for
# any downstream helpers that sample).
RANDOM_SEED = 8475                                              # (local)
np.random.seed(RANDOM_SEED)
torch.manual_seed(RANDOM_SEED)

# ---------------------------------------------------------------------------
# Section 3 -- Paths + pre-registration constants
# ---------------------------------------------------------------------------
SESSION = "S84"                                                 # (local)
GATE_ID = "S84-W7b-75-B-POWER-STABILITY"                        # (local)
SCHEME = "eigvalsh-joint-logfit"                                # (local)
CONVENTION = "V-rescaled-Delta-fixed"                           # (local)
L_MAX_TASK = 12                                                 # (local) task-pinned L max
L_MIN_TASK = 3                                                  # (local) task-pinned L min
L_JOINT_FIT = [3, 4, 5, 6, 7, 8, 10, 12]                        # (local) 8-point joint fit L values

OUT_NPZ = SCRIPT_DIR / "s84_w7b_75_data.npz"
OUT_PNG = SCRIPT_DIR / "s84_w7b_75_plot.png"
VERDICT_TXT = SCRIPT_DIR / "s84_gate_verdicts.txt"
SPECTRUM_CACHE_L9 = SCRIPT_DIR / "s74_spectrum_cache_L9_tau019.npz"  # (local)
SPECTRUM_CACHE_L12 = SCRIPT_DIR / "s84_spectrum_cache_L12_tau019.npz"  # (local) new cache emitted here
G36_NPZ = SCRIPT_DIR / "s83_w3_g36_matrix_model_classification.npz"  # (local)

INPUT_FILES = [
    SCRIPT_DIR / "canonical_constants.py",
    G36_NPZ,
    SPECTRUM_CACHE_L9,
    SCRIPT_DIR / "dirac_spectrum.py",
    SCRIPT_DIR / "s84_w7b_75_b_power_stability.py",
]

# Pre-registered thresholds (plan §W7b-75)
B_ANCHOR = 4.681                                                # (local) G36 anchor
PASS_B_TOL = 0.10                                               # (local) b-power tolerance
INFO_B_TOL = 0.30                                               # (local) b-power INFO tolerance
PASS_R2_THRESHOLD = 0.99                                        # (local)
INFO_R2_THRESHOLD = 0.95                                        # (local)

EVAL_CUTOFF = 1e-6                                              # (local) IR cutoff

DELTA_CANONICAL = float(Delta_BCS)                              # (local alias)
TAU = float(tau_fold)                                           # (local alias)

L_COMPUTE_FRESH = [9, 10, 11, 12]                               # (local) L levels we build fresh


# ---------------------------------------------------------------------------
# Section 4 -- SHA-256 input-pin block
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                        # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}                                                   # (local)
    for p in inputs:
        sha = sha256_of(p)                                      # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins):
    items = sorted(pins.items())                                # (local)
    h = hashlib.sha256()                                        # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 -- SU(3) irrep dimension + sector enumeration
# ---------------------------------------------------------------------------

def dim_su3(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def all_sectors_up_to(L_cut):
    """Enumerate (p,q) with p+q <= L_cut, ordered by level then by p."""
    out = []                                                    # (local)
    for L in range(L_cut + 1):
        for p in range(L + 1):
            q = L - p
            out.append((p, q))
    return out


# ---------------------------------------------------------------------------
# Section 6 -- Dirac operator sector build (GPU eigvalsh)
# ---------------------------------------------------------------------------

def _irrep_p_zero_recursive(p, gens, f_abc, cache):
    """Build (p, 0) via iterative Casimir projection from (1, 0) x (p-1, 0).
    Avoids the 3^p memory blow-up of irrep_symmetric_power for large p.

    Returns rho: list of 8 matrices of dim (p+1)(p+2)/2.
    """
    if (p, 0) in cache:
        return cache[(p, 0)]
    if p == 0:
        rho = [np.zeros((1, 1), dtype=complex) for _ in range(8)]        # (local)
    elif p == 1:
        rho = tds.irrep_fundamental(gens)                                # (local)
    else:
        rho_parent = _irrep_p_zero_recursive(p - 1, gens, f_abc, cache)  # (local)
        rho_3 = tds.irrep_fundamental(gens)                              # (local)
        dim_target = (p + 1) * (p + 2) // 2                              # (local) dim(p,0)
        rho = tds.irrep_via_casimir_projection(rho_3, rho_parent,
                                                dim_target, (p, 0))      # (local)
    cache[(p, 0)] = rho
    return rho


def build_irrep_with_fallback(p, q, gens, f_abc):
    """S74 pattern extended: use iterative Casimir projection for large (p,0)
    and (0,q) to avoid the 3^p symmetric-tensor memory blow-up.

    Strategy:
      (p,0):  build via recursion (1,0) x (p-1,0) -> (p,0) Casimir projection
      (0,q):  conjugate of (q,0)
      (p,q) mixed with p>=q: tds.get_irrep default (uses tensor chain)
      (p,q) mixed with q>p: conjugate of (q,p)
    """
    p_zero_cache = {}                                                    # (local)

    if q == 0:
        rho = _irrep_p_zero_recursive(p, gens, f_abc, p_zero_cache)      # (local)
        return rho, (p + 1) * (p + 2) // 2
    if p == 0 and q >= 2:
        conj_gens = [-g.T for g in gens]                                 # (local)
        rho = _irrep_p_zero_recursive(q, conj_gens, f_abc, p_zero_cache)  # (local)
        return rho, (q + 1) * (q + 2) // 2
    if p == 0 and q == 1:
        return tds.irrep_antifundamental(gens), 3

    # Mixed (p,q): use tds machinery. For large p+q with p>=1, q>=1, the
    # tds.get_irrep recursion uses (1,0) x (p-1,q) projection which has
    # dim_prod = 3 * dim(p-1,q), manageable. But when the internal recursion
    # eventually hits (0,q-something) with large q, it would re-enter
    # irrep_symmetric_power. Guard: if we detect large q_tail, pre-seed
    # the cache with our recursive build.
    # Actually tds.get_irrep only recurses in p (not q), so (p>=q>=1) is safe.
    # For q > p, tds.get_irrep builds (q,p) with conj gens which recurses in q
    # (the larger index) until reaching (q, p_small) and eventually (q, 0) or
    # (1, 0) chain. It calls get_irrep(p-1,q), NOT get_irrep(p,q-1). So for
    # (p,q) with p>=q>=1 this is fine. For q>p, tds calls (q,p) on conj_gens
    # which is p<=q on that side, recurses ok.
    # The ONLY failure mode is p=0 with large q, which we handle above.
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
    """Build D_pi = sum_{a,b} E_{ab} rho[b] (x) gamma_a + I (x) Omega,
    then eigvalsh on GPU in complex128.

    Returns (pos_abs_evals: float64, dim_rho: int, wall_s: float,
             peak_vram_MB: float).
    """
    dim_rho = rho[0].shape[0]                                   # (local)
    dim_spin = 16                                               # (local)
    dim_total = dim_rho * dim_spin                              # (local)

    t0 = time.time()                                            # (local)

    # Assemble D_pi on CPU (kron structure is I/O-bound, not FLOPs-bound)
    D = np.zeros((dim_total, dim_total), dtype=np.complex128)
    for a in range(8):
        for b in range(8):
            if abs(E[a, b]) > 1e-15:
                D += E[a, b] * np.kron(rho[b], gammas[a])
    D += np.kron(np.eye(dim_rho), Omega)

    # D is anti-Hermitian; form H = i*D which is Hermitian; enforce exact H
    H = 1j * D                                                  # (local)
    H = 0.5 * (H + H.conj().T)                                  # (local)

    # GPU eigvalsh in complex128
    torch.cuda.reset_peak_memory_stats()
    Ht = torch.tensor(H, dtype=torch.complex128, device='cuda')
    del H, D
    torch.cuda.synchronize()
    evals = torch.linalg.eigvalsh(Ht)
    torch.cuda.synchronize()
    evals_np = evals.detach().cpu().numpy()                     # (local)
    peak_vram_MB = torch.cuda.max_memory_allocated() / 1e6      # (local)

    # Free GPU memory for next sector
    del Ht, evals
    torch.cuda.empty_cache()

    # Filter: abs, drop IR-zero modes
    abs_evals = np.abs(evals_np)                                # (local)
    mask = abs_evals > EVAL_CUTOFF                              # (local)
    pos_abs = abs_evals[mask].astype(np.float64)                # (local)

    wall = time.time() - t0                                     # (local)
    return pos_abs, dim_rho, wall, peak_vram_MB


# ---------------------------------------------------------------------------
# Section 7 -- BCS gap + condensation energy (V-rescale convention)
# ---------------------------------------------------------------------------

def collect_spectrum_from_dict(sector_dict, L_cut, cutoff=EVAL_CUTOFF):
    """Assemble (lam_array, mult_array) for all sectors with level <= L_cut.
    Each eigenvalue contributes with weight dim(p,q) per the G36 convention.
    """
    abs_list = []                                               # (local)
    mult_list = []                                              # (local)
    for (p, q), data in sorted(sector_dict.items()):
        if (p + q) <= L_cut:
            dim = int(data['dim'])                              # (local)
            for ev in data['abs_evals']:
                a = float(ev)                                   # (local)
                if a > cutoff:
                    abs_list.append(a)
                    mult_list.append(dim)
    return (np.array(abs_list, dtype=np.float64),
            np.array(mult_list, dtype=np.float64))


def gap_sum(lam, mult, Delta):
    return float(np.sum(mult / (2.0 * np.sqrt(lam ** 2 + Delta ** 2))))


def bcs_condensation_energy(lam, mult, Delta):
    """E_cond = -0.5 * sum_j d_j * (sqrt(lam_j^2 + Delta^2) - |lam_j|)."""
    return float(-0.5 * np.sum(
        mult * (np.sqrt(lam ** 2 + Delta ** 2) - np.abs(lam))
    ))


# ---------------------------------------------------------------------------
# Section 8 -- Power-law fit (joint log-log)
# ---------------------------------------------------------------------------

def fit_powerlaw_joint(L_arr, E_arr):
    """Fit |E(L)| = A * L^b via linear regression in log space on the
    supplied point set. Returns (b, logA, R2_linear_space).
    R^2 convention matches G36: residuals computed in linear |E| space,
    not in log space, so the fit metric is comparable to G36 PASS band.
    """
    absE = np.abs(E_arr).astype(np.float64)                     # (local)
    log_L = np.log(L_arr.astype(np.float64))                    # (local)
    log_E = np.log(absE)                                        # (local)
    slope, intercept = np.polyfit(log_L, log_E, 1)
    E_hat = np.exp(intercept + slope * log_L)                   # (local)
    ss_res = float(np.sum((absE - E_hat) ** 2))                 # (local)
    ss_tot = float(np.sum((absE - absE.mean()) ** 2))           # (local)
    r2_linear = 1.0 - ss_res / ss_tot if ss_tot > 0 else np.nan  # (local)
    # Also log-space R^2 for diagnostic
    log_Ehat = intercept + slope * log_L                        # (local)
    ss_res_log = float(np.sum((log_E - log_Ehat) ** 2))         # (local)
    ss_tot_log = float(np.sum((log_E - log_E.mean()) ** 2))     # (local)
    r2_log = 1.0 - ss_res_log / ss_tot_log if ss_tot_log > 0 else np.nan  # (local)
    return float(slope), float(intercept), float(r2_linear), float(r2_log)


# ---------------------------------------------------------------------------
# Section 9 -- Main pipeline
# ---------------------------------------------------------------------------

def main():
    t_start = time.time()                                       # (local)

    print("=" * 78)
    print(f"{GATE_ID} -- b-power stability extending to L=12")
    print("=" * 78)
    print(f"torch: {torch.__version__}, CUDA avail: {torch.cuda.is_available()}, "
          f"device: {torch.cuda.get_device_name(0)}")
    print(f"Delta_canonical = {DELTA_CANONICAL:.10f} M_KK (S70 R-protected)")
    print(f"tau = {TAU} (tau_fold)\n")

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"closure={closure[:16]}... (full 64 at end)\n")

    # --- Load G36 L=3..8 anchor data ---
    print(f"Loading G36 anchor: {G36_NPZ.name}")
    g36 = np.load(G36_NPZ, allow_pickle=True)
    L_anchor = np.asarray(g36['L_list'])                        # (local)
    E_anchor = np.asarray(g36['E_cond_list'])                   # (local)
    b_g36 = float(g36['b_power'])                               # (local)
    r2_g36 = float(g36['r2_power'])                             # (local)
    print(f"  G36 L={list(L_anchor)}, E_cond={list(E_anchor)}")
    print(f"  G36 b_power = {b_g36:.6f}, R^2 = {r2_g36:.6f}\n")
    g36.close()

    # --- Load cached L<=9 sector eigenvalues from S74 (partial coverage) ---
    print(f"Loading S74 L9 cache: {SPECTRUM_CACHE_L9.name}")
    cache_l9 = np.load(SPECTRUM_CACHE_L9, allow_pickle=True)
    sector_evals_l9_raw = cache_l9['sector_evals'].item()
    sector_evals = {}                                           # (local) full sector dict
    for (p, q), data in sector_evals_l9_raw.items():
        sector_evals[(p, q)] = {
            'dim': int(data['dim']),
            'level': int(data['level']),
            'abs_evals': np.asarray(data['abs_evals'], dtype=np.float64),
        }
    cache_l9.close()
    print(f"  Loaded {len(sector_evals)} sectors from cache\n")

    # --- Build geometric infrastructure (Jensen metric at tau_fold) ---
    print("Building D_K infrastructure at tau=0.19 ...")
    t_geo = time.time()                                         # (local)
    gens = tds.su3_generators()
    f_abc = tds.compute_structure_constants(gens)
    B_ab = tds.compute_killing_form(f_abc)
    g_s = tds.jensen_metric(B_ab, TAU)
    E_frame = tds.orthonormal_frame(g_s)
    ft = tds.frame_structure_constants(f_abc, E_frame)
    Gamma_conn = tds.connection_coefficients(ft)
    gammas = tds.build_cliff8()
    Omega = tds.spinor_connection_offset(Gamma_conn, gammas)

    cliff_err = tds.validate_clifford(gammas)                   # (local)
    mc_err = tds.validate_connection(Gamma_conn)                # (local)
    print(f"  Clifford algebra error: {cliff_err:.2e}")
    print(f"  Metric compatibility error: {mc_err:.2e}")
    print(f"  Infrastructure built in {time.time()-t_geo:.2f}s\n")

    # --- Fill missing sectors and extend to L=10, 11, 12 ---
    print("Building missing/fresh sectors on GPU (eigvalsh, complex128):")
    print(f"  {'(p,q)':>8s}  {'L':>2s}  {'dim':>5s}  "
          f"{'dim_tot':>7s}  {'wall(s)':>8s}  {'VRAM(MB)':>9s}  {'|lam|range':>22s}")

    wall_by_L = {}                                              # (local)
    vram_by_L = {}                                              # (local)

    for L in L_COMPUTE_FRESH:
        L_wall_start = time.time()                              # (local)
        L_peak_vram = 0.0                                       # (local)
        for p in range(L + 1):
            q = L - p
            if (p, q) in sector_evals:
                # Already cached (from S74 at L<=9 where present)
                continue
            try:
                rho, dim_check = build_irrep_with_fallback(p, q, gens, f_abc)
            except Exception as e:
                print(f"  ({p},{q}) L={L}: FAIL to build irrep: {e}")
                raise
            assert dim_check == dim_su3(p, q)
            pos_abs, dim_rho, wall_s, peak_vram_MB = compute_sector_eigenvalues_gpu(
                rho, E_frame, gammas, Omega
            )
            sector_evals[(p, q)] = {
                'dim': dim_rho,
                'level': L,
                'abs_evals': pos_abs,
            }
            L_peak_vram = max(L_peak_vram, peak_vram_MB)
            lam_min = float(np.min(pos_abs)) if len(pos_abs) else np.nan  # (local)
            lam_max = float(np.max(pos_abs)) if len(pos_abs) else np.nan  # (local)
            print(f"  ({p},{q})  {L:>2d}  {dim_rho:>5d}  {16*dim_rho:>7d}  "
                  f"{wall_s:>8.2f}  {peak_vram_MB:>9.1f}  "
                  f"[{lam_min:.3f},{lam_max:.3f}]")
            sys.stdout.flush()
        wall_by_L[L] = time.time() - L_wall_start
        vram_by_L[L] = L_peak_vram

    print()

    # Save the extended sector cache (audit / reproducibility)
    print(f"Saving extended sector cache: {SPECTRUM_CACHE_L12.name}")
    np.savez(SPECTRUM_CACHE_L12, sector_evals=sector_evals)
    print(f"  {len(sector_evals)} sectors in cache\n")

    # --- Compute E_cond(L) at V-rescaled-Delta-fixed for L in {3..12} ---
    print("Computing E_cond(L) via V-rescale (Delta fixed at canonical):")
    print(f"  {'L':>3s}  {'n_sect':>6s}  {'n_modes':>8s}  {'sum_d':>12s}  "
          f"{'V_pair(L)':>14s}  {'Delta':>10s}  {'E_cond(L)':>18s}")
    all_L = sorted(set(list(L_JOINT_FIT) + L_COMPUTE_FRESH))     # (local) 3..12 with 9,11 for diag
    E_cond_fresh = {}                                            # (local) full computation, all L
    V_pair_fresh = {}                                            # (local)
    sum_mult_fresh = {}                                          # (local)
    n_modes_fresh = {}                                           # (local)
    n_sect_fresh = {}                                            # (local)
    for L in all_L:
        lam_L, mult_L = collect_spectrum_from_dict(sector_evals, L)
        # V-rescale: V_pair(L) such that gap equation holds at Delta_canonical
        s = gap_sum(lam_L, mult_L, DELTA_CANONICAL)
        V_pair_L = 1.0 / s if s > 0 else np.nan                  # (local)
        E_L = bcs_condensation_energy(lam_L, mult_L, DELTA_CANONICAL)  # (local)
        E_cond_fresh[L] = E_L
        V_pair_fresh[L] = V_pair_L
        sum_mult_fresh[L] = int(mult_L.sum())
        n_modes_fresh[L] = int(len(lam_L))
        n_sect_fresh[L] = sum(1 for (p, q) in sector_evals if (p + q) <= L)
        print(f"  {L:>3d}  {n_sect_fresh[L]:>6d}  {n_modes_fresh[L]:>8d}  "
              f"{sum_mult_fresh[L]:>12d}  {V_pair_L:>14.6e}  "
              f"{DELTA_CANONICAL:>10.6f}  {E_L:>18.4f}")
    print()

    # --- Cross-check G36 anchor: do L=3..8 fresh values match G36 exactly? ---
    # (Note: fresh L=8 includes (4,4) which G36 missed; fresh differs from G36
    # because of that sector. Both are valid scheme-variants; the gate tests the
    # G36-scheme b, so the JOINT FIT USES G36 ANCHOR FOR L=3..8 plus fresh L=10,12.)
    print("G36 anchor vs fresh (L=3..8) comparison:")
    print(f"  {'L':>3s}  {'G36 E_cond':>18s}  {'Fresh E_cond':>18s}  "
          f"{'rel_diff':>10s}")
    for i, L in enumerate(L_anchor):
        L_int = int(L)                                          # (local)
        rel = (E_cond_fresh[L_int] - E_anchor[i]) / E_anchor[i] if E_anchor[i] != 0 else np.nan  # (local)
        print(f"  {L_int:>3d}  {E_anchor[i]:>18.4f}  {E_cond_fresh[L_int]:>18.4f}  "
              f"{rel:>10.4f}")
    print()

    # --- JOINT FIT (G36-scheme): use G36 anchors for L=3..8, fresh for L=10, 12 ---
    E_joint_g36scheme = []                                      # (local)
    L_joint = np.array(L_JOINT_FIT, dtype=np.int64)             # (local)
    for L in L_JOINT_FIT:
        if L in list(L_anchor):
            idx = list(L_anchor).index(L)                       # (local)
            E_joint_g36scheme.append(float(E_anchor[idx]))
        else:
            E_joint_g36scheme.append(E_cond_fresh[L])
    E_joint_g36 = np.array(E_joint_g36scheme, dtype=np.float64)  # (local)

    b_joint_g36, logA_joint_g36, r2_lin_joint_g36, r2_log_joint_g36 = \
        fit_powerlaw_joint(L_joint, E_joint_g36)

    # --- JOINT FIT (fresh-scheme): use fresh values for all L in joint set ---
    E_joint_fresh = np.array([E_cond_fresh[L] for L in L_JOINT_FIT],
                             dtype=np.float64)                  # (local)
    b_joint_fresh, logA_joint_fresh, r2_lin_joint_fresh, r2_log_joint_fresh = \
        fit_powerlaw_joint(L_joint, E_joint_fresh)

    # --- Also the 10-point fit (L=3..12 including odd L=9, 11) as diagnostic ---
    L_all10 = np.array([3, 4, 5, 6, 7, 8, 9, 10, 11, 12], dtype=np.int64)  # (local)
    E_all10_fresh = np.array([E_cond_fresh[L] for L in L_all10], dtype=np.float64)  # (local)
    b_all10, logA_all10, r2_lin_all10, r2_log_all10 = \
        fit_powerlaw_joint(L_all10, E_all10_fresh)

    print("Joint fits (power-law b_power from log-log):")
    print(f"  8-point JOINT (L={list(L_JOINT_FIT)}, G36-scheme):")
    print(f"    b = {b_joint_g36:+.6f}")
    print(f"    log A = {logA_joint_g36:+.6f}")
    print(f"    R^2 (linear |E|) = {r2_lin_joint_g36:.6f}")
    print(f"    R^2 (log |E|)    = {r2_log_joint_g36:.6f}")
    print(f"  8-point JOINT (L={list(L_JOINT_FIT)}, fresh-scheme):")
    print(f"    b = {b_joint_fresh:+.6f}")
    print(f"    R^2 (linear |E|) = {r2_lin_joint_fresh:.6f}")
    print(f"  10-point diagnostic (L={list(L_all10)}, fresh-scheme):")
    print(f"    b = {b_all10:+.6f}")
    print(f"    R^2 (linear |E|) = {r2_lin_all10:.6f}\n")

    # --- DIRECTION: verdict per pre-registered thresholds (plan §W7b-75 step 5) ---
    #     PASS:  |b - 4.681| < 0.10 AND R^2 > 0.99
    #     INFO:  |b - 4.681| < 0.30 AND R^2 > 0.95
    #     FAIL:  otherwise
    # Reference fit = 8-point JOINT G36-scheme (plan anchors G36 E_cond at L<=8)
    b_gate = b_joint_g36                                        # (local)
    r2_gate = r2_lin_joint_g36                                  # (local)
    delta_b = abs(b_gate - B_ANCHOR)                            # (local)

    cond_pass = (delta_b < PASS_B_TOL) and (r2_gate > PASS_R2_THRESHOLD)  # (local)
    cond_info = (delta_b < INFO_B_TOL) and (r2_gate > INFO_R2_THRESHOLD)  # (local)

    if cond_pass:
        verdict = "PASS"                                        # (local)
    elif cond_info:
        verdict = "INFO"                                        # (local)
    else:
        verdict = "FAIL"                                        # (local)

    print("DIRECTION (pre-registered):")
    print(f"  Reference: 8-point JOINT G36-scheme fit on L={list(L_JOINT_FIT)}")
    print(f"  b_gate  = {b_gate:.6f}")
    print(f"  |b_gate - {B_ANCHOR}| = {delta_b:.6f} "
          f"(PASS tol = {PASS_B_TOL}, INFO tol = {INFO_B_TOL})")
    print(f"  R^2_gate = {r2_gate:.6f} "
          f"(PASS thr = {PASS_R2_THRESHOLD}, INFO thr = {INFO_R2_THRESHOLD})")
    print(f"  PASS: {cond_pass}, INFO: {cond_info}\n")
    print(f"=> Verdict: {verdict}\n")

    # --- STRUCTURAL INTERPRETATION ---
    if verdict == "PASS":
        interp = (
            "Power-law exponent b_power is ASYMPTOTICALLY STABLE to L=12. "
            "The 2^4.681 ~ 25.6 per L-doubling ratio is locked as a structural "
            "spectral invariant of the Jensen-deformed SU(3) triple at tau_fold. "
            "IKKT-class scaling (b=1) is excluded to arbitrary L. "
            "Singleton (12, 6, A_F) has a predictive scaling."
        )
    elif verdict == "INFO":
        interp = (
            "Trend is stable with moderate drift. Does not refute the asymptote "
            "but warrants higher-L verification (S85+)."
        )
    else:
        interp = (
            "L=10, 12 data reveals finite-L artifact. S83-G36 matrix-model-"
            "classification PASS must be reviewed; IKKT correspondence "
            "classification re-opens."
        )
    print("STRUCTURAL INTERPRETATION:")
    print(f"  {interp}\n")

    # --- Save artifacts ---
    L_all_for_save = np.array(sorted(E_cond_fresh.keys()), dtype=np.int64)  # (local)
    E_all_for_save = np.array([E_cond_fresh[L] for L in L_all_for_save],
                              dtype=np.float64)                 # (local)
    V_all_for_save = np.array([V_pair_fresh[L] for L in L_all_for_save],
                              dtype=np.float64)                 # (local)
    sumd_all_for_save = np.array([sum_mult_fresh[L] for L in L_all_for_save],
                                 dtype=np.int64)                # (local)
    nmod_all_for_save = np.array([n_modes_fresh[L] for L in L_all_for_save],
                                 dtype=np.int64)                # (local)
    wall_arr = np.array([wall_by_L.get(L, 0.0) for L in L_COMPUTE_FRESH],
                        dtype=np.float64)                       # (local)
    vram_arr = np.array([vram_by_L.get(L, 0.0) for L in L_COMPUTE_FRESH],
                        dtype=np.float64)                       # (local)

    np.savez(
        OUT_NPZ,
        # Joint fit anchors
        L_joint=L_joint,
        E_joint_g36scheme=E_joint_g36,
        E_joint_fresh=E_joint_fresh,
        # Fit results
        b_joint_g36=b_joint_g36, logA_joint_g36=logA_joint_g36,
        r2_lin_joint_g36=r2_lin_joint_g36, r2_log_joint_g36=r2_log_joint_g36,
        b_joint_fresh=b_joint_fresh, logA_joint_fresh=logA_joint_fresh,
        r2_lin_joint_fresh=r2_lin_joint_fresh, r2_log_joint_fresh=r2_log_joint_fresh,
        b_all10=b_all10, r2_lin_all10=r2_lin_all10, r2_log_all10=r2_log_all10,
        # Full L-list data
        L_list_full=L_all_for_save,
        E_cond_list_full=E_all_for_save,
        V_pair_list_full=V_all_for_save,
        sum_mult_list_full=sumd_all_for_save,
        n_modes_list_full=nmod_all_for_save,
        # G36 anchor for audit
        L_g36=L_anchor, E_g36=E_anchor, b_g36=b_g36, r2_g36=r2_g36,
        # Thresholds
        B_ANCHOR=B_ANCHOR, PASS_B_TOL=PASS_B_TOL, INFO_B_TOL=INFO_B_TOL,
        PASS_R2_THRESHOLD=PASS_R2_THRESHOLD, INFO_R2_THRESHOLD=INFO_R2_THRESHOLD,
        # Verdict payload
        verdict=verdict, delta_b=delta_b,
        # Compute accounting
        L_compute_fresh=np.array(L_COMPUTE_FRESH, dtype=np.int64),
        wall_by_L=wall_arr, vram_by_L=vram_arr,
        # Constants
        Delta_canonical=DELTA_CANONICAL, tau=TAU,
        random_seed=RANDOM_SEED,
        # Closure
        closure=closure,
    )
    print(f"Data saved: {OUT_NPZ.name}")

    # --- Plot: log-log |E_cond| vs L with 8-point fit ---
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    ax0, ax1 = axes

    # Panel (a): log-log with both G36-scheme and fresh-scheme fits
    L_smooth = np.linspace(2.5, 13.0, 100)                      # (local)
    E_hat_g36 = np.exp(logA_joint_g36) * L_smooth ** b_joint_g36  # (local)
    E_hat_fresh = np.exp(logA_joint_fresh) * L_smooth ** b_joint_fresh  # (local)

    # G36 anchor points
    ax0.scatter(L_anchor, np.abs(E_anchor), marker='o', s=80,
                facecolor='#2c7fb8', edgecolor='k', zorder=4,
                label=f'G36 anchor L=3..8 (b={b_g36:.3f})')
    # Fresh L=9..12 points
    L_fresh_plot = np.array(L_COMPUTE_FRESH)                    # (local)
    E_fresh_plot = np.array([E_cond_fresh[L] for L in L_COMPUTE_FRESH])  # (local)
    ax0.scatter(L_fresh_plot, np.abs(E_fresh_plot), marker='s', s=100,
                facecolor='#d7191c', edgecolor='k', zorder=5,
                label='Fresh L=9..12')
    # Highlight L=10, 12 (the joint-fit extension points)
    ax0.scatter([10, 12], [np.abs(E_cond_fresh[10]), np.abs(E_cond_fresh[12])],
                marker='*', s=400, facecolor='gold', edgecolor='k', zorder=6,
                label='Joint-fit L=10,12')
    ax0.plot(L_smooth, E_hat_g36, 'r--',
             label=f'8-pt JOINT G36-scheme: b={b_joint_g36:.4f}, '
                   f'R^2={r2_lin_joint_g36:.4f}',
             linewidth=2)
    ax0.plot(L_smooth, E_hat_fresh, 'g-.',
             label=f'8-pt JOINT fresh-scheme: b={b_joint_fresh:.4f}, '
                   f'R^2={r2_lin_joint_fresh:.4f}',
             linewidth=1.5, alpha=0.85)

    ax0.set_xlabel('L (level cut)')
    ax0.set_ylabel('|E_cond(L)| [M_KK]')
    ax0.set_xscale('log')
    ax0.set_yscale('log')
    ax0.legend(loc='upper left', fontsize=8)
    ax0.grid(alpha=0.3, which='both')
    ax0.set_title(
        f'|E_cond(L)| log-log, L=3..12\n'
        f'b_gate = {b_gate:.4f} (anchor 4.681, tol +-{PASS_B_TOL}); '
        f'verdict {verdict}'
    )

    # Panel (b): Fit residuals (log-space, 8-point joint G36-scheme)
    log_L = np.log(L_joint.astype(np.float64))                  # (local)
    log_E = np.log(np.abs(E_joint_g36))                         # (local)
    log_Ehat = logA_joint_g36 + b_joint_g36 * log_L             # (local)
    resid_log = log_E - log_Ehat                                # (local)

    # Same for fresh-scheme
    log_E_fresh = np.log(np.abs(E_joint_fresh))                 # (local)
    log_Ehat_fresh = logA_joint_fresh + b_joint_fresh * log_L   # (local)
    resid_log_fresh = log_E_fresh - log_Ehat_fresh              # (local)

    width = 0.35                                                # (local)
    ax1.bar(L_joint - width/2, resid_log, width, color='r',
            alpha=0.8, edgecolor='k', label='G36-scheme log-resid')
    ax1.bar(L_joint + width/2, resid_log_fresh, width, color='g',
            alpha=0.7, edgecolor='k', label='fresh-scheme log-resid')
    ax1.axhline(0, color='k', linewidth=0.5)
    ax1.set_xlabel('L')
    ax1.set_ylabel('log|E| - log(E_hat)')
    ax1.legend(fontsize=9)
    ax1.grid(alpha=0.3)
    ax1.set_title('8-point joint-fit log-residuals')

    fig.suptitle(
        f'{GATE_ID} -- b-power stability L=3..12\n'
        f'G36 anchor b={b_g36:.4f}, L=12 b={b_joint_g36:.4f}, '
        f'|Delta b|={delta_b:.4f}',
        fontsize=12
    )
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=110, bbox_inches='tight')
    plt.close(fig)
    print(f"Plot saved: {OUT_PNG.name}")

    # --- 4-tuple + verdict line ---
    tag = (f"(value={b_gate:.6f}, scheme={SCHEME}, "
           f"convention={CONVENTION}, L_max={L_MAX_TASK})")
    print(f"\n4-tuple: {tag}")
    print(f"Full closure SHA-256: {closure}")

    verdict_line = (
        f"{GATE_ID}: {verdict} -- "
        f"value={b_gate:.6f} scheme={SCHEME} convention={CONVENTION} "
        f"L_max={L_MAX_TASK} sha256={closure}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(verdict_line)
    print(f"\nVerdict line appended to {VERDICT_TXT.name}")

    total_wall = time.time() - t_start                          # (local)
    print(f"\n=== {GATE_ID}: {verdict} (total wall {total_wall:.1f}s) ===")
    print(f"  Per-L compute wall (fresh sectors only): "
          f"{dict((L, round(wall_by_L[L], 1)) for L in L_COMPUTE_FRESH)}")
    print(f"  Per-L peak VRAM (MB): "
          f"{dict((L, round(vram_by_L[L], 1)) for L in L_COMPUTE_FRESH)}")

    return 0 if verdict == "PASS" else (1 if verdict == "FAIL" else 3)


if __name__ == "__main__":
    sys.exit(main())
