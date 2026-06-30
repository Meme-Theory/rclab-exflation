#!/usr/bin/env python3
"""
S87 W1b-3 — S87-LMAX-WEYL-CONVERGENCE-SWEEP
==============================================

Gate: S87-LMAX-WEYL-CONVERGENCE-SWEEP ([VERIFY] CONDITIONAL)

Trigger predicate (verified TRUE upstream by the orchestrator):
  arm1 = |pv_residue_L10 - pv_residue_L12| > 1e-3
  arm1 = |41561.645 - 69955.179| = 28393.534  >> 1e-3  (7 OOM above threshold)

Pre-registered threshold (per session-87-plan-w1b.md §W1b-3):
  PASS  iff  L_inf_extrapolation_residual < 1e-4
              AND d_eff_global converges to 8.000 +/- 0.01 at L=14
              AND PV residue convergence < 1e-6 fit residual
  INFO  iff  L_inf_extrapolation_residual in [1e-4, 1e-2]
              OR d_eff_global at L=14 converges to band [7.95, 8.05]
  FAIL  iff  L_inf_extrapolation_residual > 1e-2
              OR d_eff_global at L=14 outside [7.5, 8.5]
              OR VRAM-feasibility breach (machinery-feasibility-audit hard-halt)

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz
  - computations/session-87/s87_w1b_pv_subtraction_recalibration.npz
      (provides L=10 lambdas+mults inside its npz; W1b-1 derived L=10 from
       the L=12 master cache by level-truncation, so no separate L=10 cache
       file exists on disk. We re-derive L=10 the same way.)
  - computations/session-87/s87_w1b_d_eff_anchor_verification.npz  (W1b-2 outputs)
  - computations/_shared/canonical_constants.py
  - computations/_shared/dirac_spectrum.py  (D_K builder for L=14 fresh sectors)
  - script bytes

Output 4-tuple:
  (value=L_inf_extrapolation_residual_d_eff,
   scheme=Richardson-extrapolation-3-point,
   convention=substrate-L-axis-asymptotic,
   L_max=14)

Schema-v2 3-tuple:
  sign_verdict     : N/A (AUDIT-style; no directional pre-registration)
  magnitude_verdict: per pass/info/fail bands on extrapolation_residual + d_eff band
  regime_verdict   : VALID iff cache regen + extrapolation complete without
                     numerical-precision floor breach AND VRAM-feasibility PASSes

Classification: GEOMETRIC (L_max-axis convergence sweep on substrate spectrum)

METHODOLOGY
-----------
1. VRAM-FEASIBILITY HARD GATE (Step 1 of plan).
     Estimate per-sector dense-storage requirement at L=14:
       largest level-14 sector is (p,q)=(7,7) with dim=512, matrix size=8192.
       float64 dense storage per matrix: 8192^2 * 8 = 5.37e8 bytes = 0.537 GB.
       complex128 dense storage: 1.07 GB.
     Plan-pinned ceiling: 8.5 GB (= 0.5 * 17 GB VRAM).
     Verification: 1.07 GB << 8.5 GB -> VRAM-feasibility PASS.
     If breach: emit FAIL_BY_FEASIBILITY and stop (no CPU fallback).

2. L=14 cache regeneration (sector-sequential GPU eigvalsh, complex128).
     Reuse W1b-1's `level = p+q` convention. Build (p,q) sectors with
     p+q in {13, 14} fresh; reuse p+q <= 12 from `s84_spectrum_cache_L12`.
     Save to `s87_spectrum_cache_L14_tau019.npz` with the same
     `sector_evals` dict-of-(p,q) schema.

3. Per-L spectrum loading and observable refits.
     Truncate by level p+q <= L_target for L in {10, 12, 14}.
     For each L compute:
       (a) PV-subtracted residue R_PV(L; M_KK=1) at s=3 substrate-distance-1
           using the W1b-1 recipe verbatim.
       (b) d_eff via Weyl counting fit `log N(lambda) = log C + (d_eff/2)*log lambda`
           Convention A (plan-pinned): d_eff = 2 * slope
           Convention B (s28c convention; advisory only): d_eff = slope
           (the plan PASS metric is Convention A; B is reported per spawn-prompt
           extra-reporting requirement)

4. Richardson 3-point extrapolation.
     Assume f(L) - f_inf ~ L^{-3} per plan substitution chain.
     The plan-pinned Richardson formula:
       R_3pt = [L_3^3 * f(L_3) - L_2^3 * f(L_2) + L_1^3 * f(L_1)]
                / [L_3^3 - L_2^3 + L_1^3]
     with (L_1, L_2, L_3) = (10, 12, 14).
     (Note: this is the plan's literal substitution-chain formula. It is NOT
     the canonical 3-point Richardson form for L^{-3} convergence; the canonical
     form on a non-uniform L-grid is derived below in Section 5. We compute and
     emit BOTH: `r3pt_plan_form` (the plan literal) and `r3pt_canonical`
     (the algebraically canonical L^{-3} extrapolant). Both are reported;
     the verdict uses the canonical form per regulator-convention-lockdown.md
     analog: a literal-form vs canonical-form factor mismatch is documented as
     advisory, not a verdict-controlling difference.)

5. Substitution chain for canonical Richardson 3-point on L^{-3} convergence.
     Step 1 (defs):
       f(L) = observable; f(L) - f_inf = c1/L^3 + c2/L^5 + ...  (Weyl asymptotic)
     Step 2 (3 equations, leading-order):
       f(L_i) = f_inf + c1/L_i^3,  i=1,2,3
       Linear system in (f_inf, c1) is over-determined for 3 points; solve
       least-squares on x_i = 1/L_i^3 vs y_i = f(L_i):
         y = a + b*x  ;  a = f_inf, b = c1
     Step 3 (closed form, weights uniform):
       f_inf_canonical = (sum_i y_i sum_i x_i^2 - sum_i x_i sum_i x_i y_i)
                        / (3 sum_i x_i^2 - (sum_i x_i)^2)
     Step 4 (residual):
       residual = max_i |f(L_i) - (f_inf + b/L_i^3)|
     Step 5 (verdict): PASS iff residual_max < 1e-4 AND d_eff_inf in [7.99, 8.01].

DISCIPLINE
----------
- `from canonical_constants import *`
- All intermediates tagged `# (local)`
- GPU MANDATORY (torch.linalg.eigvalsh on AMD RX 9070 XT)
- VRAM-feasibility hard gate at Step 1
- Dual-SHA emission (audit + content) per S84+ schema
- Schema-v2 3-tuple companion row per S87+ extension
- Regulator-pin tag: a_n^{Pauli-Villars} (matches W1b-1 regulator scheme)
- Atomic verdict-line append (single open("a") write; no read-modify-write)
"""

from __future__ import annotations

# -----------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY)
# -----------------------------------------------------------------------------
import os
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import *  # noqa: F401,F403

# -----------------------------------------------------------------------------
# Section 2 -- Standard imports
# -----------------------------------------------------------------------------
import hashlib
import json
import time

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import torch

import dirac_spectrum as tds  # D_K builder

# -----------------------------------------------------------------------------
# Section 3 -- Paths + pre-registration
# -----------------------------------------------------------------------------
SESSION = "S87"                                                       # (local)
GATE_ID = "S87-LMAX-WEYL-CONVERGENCE-SWEEP"                            # (local)
SCHEME = "Richardson-extrapolation-3-point"                            # (local)
CONVENTION = "substrate-L-axis-asymptotic"                             # (local)
L_MAX = 14                                                             # (local) target

# Pre-registered thresholds (frozen at plan-freeze; DO NOT EDIT)
PASS_RESIDUAL_THRESHOLD = 1e-4         # (local) extrapolation_residual PASS ceiling
INFO_RESIDUAL_THRESHOLD = 1e-2         # (local) extrapolation_residual INFO ceiling
PASS_D_EFF_BAND = (7.99, 8.01)         # (local) d_eff_inf PASS band
INFO_D_EFF_BAND = (7.95, 8.05)         # (local) d_eff_inf INFO band
FAIL_D_EFF_BAND = (7.50, 8.50)         # (local) d_eff_inf FAIL ceiling (outside this -> FAIL)

# VRAM feasibility (machinery-feasibility-audit per math-scripts.md §"Machinery-Feasibility")
VRAM_FEASIBILITY_GB = 8.5              # (local) plan-pinned 0.5*17 GB ceiling
VRAM_TOTAL_GB = 17.1                   # (local) RX 9070 XT total VRAM

CACHE_L12 = resolve_output(84, 's84_spectrum_cache_L12_tau019.npz')
CACHE_L14_OUT = resolve_output(87, 's87_spectrum_cache_L14_tau019.npz')
W1B1_NPZ = resolve_output(87, 's87_w1b_pv_subtraction_recalibration.npz')
W1B2_NPZ = resolve_output(87, 's87_w1b_d_eff_anchor_verification.npz')

OUT_NPZ = resolve_output(87, 's87_w1b_lmax_weyl_convergence_sweep.npz')
OUT_PNG = resolve_output(87, 's87_w1b_lmax_weyl_convergence_sweep.png')
VERDICT_TXT = resolve_output(87, 's87_gate_verdicts.txt')

# Regulator-pin tag (regulator-pin-discipline.md): a_n citations carry tag
REGULATOR_TAG = "Pauli-Villars"        # (local) -> a_n^{Pauli-Villars}

# PV mass scale: substrate dimensionless M_KK = 1 (matches W1b-1)
M_KK_DIMLESS = 1.0                     # (local) PV mass-scale in eigenvalue units

TAU = float(tau_fold)                  # (local alias) Jensen deformation @ fold

EVAL_CUTOFF = 1e-6                     # (local) IR cutoff (matches s84_w7b_75)

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    CACHE_L12,
    W1B1_NPZ,
    W1B2_NPZ,
    resolve_script(None, 'dirac_spectrum.py'),
]


# -----------------------------------------------------------------------------
# Section 4 -- SHA-256 input-pin block
# -----------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} - input SHA-256 pins ===")
    pins = {}                                                          # (local)
    for p in inputs:
        sha = sha256_of(p)                                              # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")        # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins):
    items = sorted(pins.items())                                       # (local)
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path, canonical_path, pins):
    script_bytes = script_path.read_bytes()                             # (local)
    canonical_bytes = canonical_path.read_bytes()                       # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")                                                   # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                         # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()                                     # (local)
    return audit, content


# -----------------------------------------------------------------------------
# Section 5 -- VRAM feasibility audit (HARD GATE; Step 1 of plan)
# -----------------------------------------------------------------------------

def dim_su3(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def vram_feasibility_audit(L_target):
    """Per-sector dense-storage estimate. Largest level-L sector at the
    L^{-3} convergence band lies at (p,q) ~ (L/2, L/2). For L=14 this is
    (7,7) with dim_irrep = 512, matrix dim = 16*512 = 8192.
    """
    # Largest sector at level L is (p,q) = (L//2, L - L//2) by Weyl-dim formula
    p_max, q_max = L_target // 2, L_target - L_target // 2              # (local)
    dim_irrep_max = dim_su3(p_max, q_max)                               # (local)
    matrix_dim = 16 * dim_irrep_max                                     # (local)
    bytes_complex128 = matrix_dim * matrix_dim * 16                     # (local) 16 bytes per complex128
    gb_complex128 = bytes_complex128 / 1e9                              # (local)
    bytes_float64 = matrix_dim * matrix_dim * 8                         # (local)
    gb_float64 = bytes_float64 / 1e9                                    # (local)
    print(f"=== VRAM feasibility audit (L_target={L_target}) ===")
    print(f"  Largest sector at level={L_target}: (p,q)=({p_max},{q_max})")
    print(f"  dim_irrep = {dim_irrep_max}, matrix_dim = {matrix_dim}")
    print(f"  Per-sector dense storage (complex128): {gb_complex128:.3f} GB")
    print(f"  Per-sector dense storage (float64):   {gb_float64:.3f} GB")
    print(f"  Plan-pinned ceiling: {VRAM_FEASIBILITY_GB} GB (= 0.5 * {VRAM_TOTAL_GB} GB)")
    feasibility_pass = gb_complex128 <= VRAM_FEASIBILITY_GB             # (local)
    if feasibility_pass:
        print(f"  VERDICT: PASS ({gb_complex128:.3f} GB <= {VRAM_FEASIBILITY_GB} GB)")
    else:
        print(f"  VERDICT: FAIL_BY_FEASIBILITY ({gb_complex128:.3f} GB > {VRAM_FEASIBILITY_GB} GB)")
    print()
    return feasibility_pass, gb_complex128, matrix_dim


# -----------------------------------------------------------------------------
# Section 6 -- Spectrum loading (sector dict; level convention p+q)
# -----------------------------------------------------------------------------

def load_sector_cache(npz_path):
    """Load sector_evals dict (keys (p,q), values dict with 'dim','level','abs_evals')."""
    data = np.load(npz_path, allow_pickle=True)
    sec_raw = data["sector_evals"].item()                               # (local)
    sec = {}                                                            # (local) normalized
    for (p, q), v in sec_raw.items():
        sec[(p, q)] = {
            "dim": int(v["dim"]),
            "level": int(v["level"]),
            "abs_evals": np.asarray(v["abs_evals"], dtype=np.float64),
        }
    return sec


def collect_lambdas_mults(sector_evals, L_target, cutoff=EVAL_CUTOFF):
    """Return concatenated (lambdas, mults) arrays for sectors with level <= L_target.

    Each eigenvalue's multiplicity is dim_irrep(p,q) per the Peter-Weyl
    decomposition (matches W1b-1's load_spectrum used for PV-moment computation).
    """
    lams = []                                                           # (local)
    mults = []                                                          # (local)
    for (p, q), data in sorted(sector_evals.items()):
        if data["level"] > L_target:
            continue
        ev = data["abs_evals"]                                          # (local)
        m = int(data["dim"])                                            # (local)
        mask = ev > cutoff                                              # (local)
        ev_keep = ev[mask]                                              # (local)
        lams.append(ev_keep)
        mults.append(np.full_like(ev_keep, m, dtype=np.float64))
    lambdas = np.concatenate(lams) if lams else np.zeros(0, dtype=np.float64)
    mks = np.concatenate(mults) if mults else np.zeros(0, dtype=np.float64)
    return lambdas, mks


def collect_lambdas_w1b2_protocol(sector_evals, L_target, cutoff=EVAL_CUTOFF):
    """W1b-2 protocol: concatenate raw abs_evals from each sector with level <= L
    WITHOUT Peter-Weyl multiplicity expansion. Returns the sorted 1-D array of
    166,896 entries at L=12 that W1b-2 used for its Weyl-fit. This is the binding
    array for matching W1b-2's d_eff = 10.07 at L=12 result, and therefore the
    binding convention for the PASS criterion `d_eff_inf in [7.99, 8.01]` since
    that criterion is calibrated against W1b-2's d_eff anchor.
    """
    chunks = []                                                         # (local)
    for (p, q), data in sorted(sector_evals.items()):
        if data["level"] > L_target:
            continue
        ev = data["abs_evals"]                                          # (local)
        mask = ev > cutoff                                              # (local)
        chunks.append(ev[mask])
    if not chunks:
        return np.zeros(0, dtype=np.float64)
    all_evals = np.concatenate(chunks)                                   # (local)
    return np.sort(all_evals)


# -----------------------------------------------------------------------------
# Section 7 -- L=14 cache regeneration (GPU eigvalsh; sector-sequential)
# -----------------------------------------------------------------------------

def _irrep_p_zero_recursive(p, gens, f_abc, cache):
    """Avoid 3^p memory blow-up of irrep_symmetric_power for large (p,0).
    Same recipe as s84_w7b_75_b_power_stability.py.
    """
    if (p, 0) in cache:
        return cache[(p, 0)]
    if p == 0:
        rho = [np.zeros((1, 1), dtype=complex) for _ in range(8)]      # (local)
    elif p == 1:
        rho = tds.irrep_fundamental(gens)                               # (local)
    else:
        rho_parent = _irrep_p_zero_recursive(p - 1, gens, f_abc, cache)  # (local)
        rho_3 = tds.irrep_fundamental(gens)                             # (local)
        dim_target = (p + 1) * (p + 2) // 2                             # (local)
        rho = tds.irrep_via_casimir_projection(
            rho_3, rho_parent, dim_target, (p, 0)
        )                                                                # (local)
    cache[(p, 0)] = rho
    return rho


def build_irrep_with_fallback(p, q, gens, f_abc):
    """Match s84_w7b_75 strategy: tensor-chain for (p,0)/(0,q), tds.get_irrep
    fallback for mixed (p,q) with conjugate-rep when q > p.
    """
    p_zero_cache = {}                                                   # (local)
    if q == 0:
        rho = _irrep_p_zero_recursive(p, gens, f_abc, p_zero_cache)     # (local)
        return rho, (p + 1) * (p + 2) // 2
    if p == 0 and q >= 2:
        conj_gens = [-g.T for g in gens]                                # (local)
        rho = _irrep_p_zero_recursive(q, conj_gens, f_abc, p_zero_cache)  # (local)
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
    """D_pi assembly + GPU eigvalsh. Matches s84_w7b_75."""
    dim_rho = rho[0].shape[0]                                            # (local)
    dim_spin = 16                                                        # (local)
    dim_total = dim_rho * dim_spin                                       # (local)

    t0 = time.time()                                                     # (local)

    D = np.zeros((dim_total, dim_total), dtype=np.complex128)            # (local)
    for a in range(8):
        for b in range(8):
            if abs(E[a, b]) > 1e-15:
                D += E[a, b] * np.kron(rho[b], gammas[a])
    D += np.kron(np.eye(dim_rho), Omega)
    H = 1j * D                                                           # (local)
    H = 0.5 * (H + H.conj().T)                                           # (local)

    torch.cuda.reset_peak_memory_stats()
    Ht = torch.tensor(H, dtype=torch.complex128, device='cuda')
    del H, D
    torch.cuda.synchronize()
    evals = torch.linalg.eigvalsh(Ht)
    torch.cuda.synchronize()
    evals_np = evals.detach().cpu().numpy()                              # (local)
    peak_vram_MB = torch.cuda.max_memory_allocated() / 1e6               # (local)
    del Ht, evals
    torch.cuda.empty_cache()

    abs_evals = np.abs(evals_np)                                         # (local)
    mask = abs_evals > EVAL_CUTOFF                                       # (local)
    pos_abs = abs_evals[mask].astype(np.float64)                         # (local)

    wall = time.time() - t0                                              # (local)
    return pos_abs, dim_rho, wall, peak_vram_MB


def regenerate_L14_cache(seed_sectors_L12):
    """Build all (p,q) with p+q in {13, 14} fresh, return extended sector_evals."""
    sector_evals = dict(seed_sectors_L12)                                # (local) start with L<=12 from cache
    print("Building Jensen-deformed Dirac infrastructure at tau=0.19 ...")
    t_geo = time.time()                                                  # (local)
    gens = tds.su3_generators()
    f_abc = tds.compute_structure_constants(gens)
    B_ab = tds.compute_killing_form(f_abc)
    g_s = tds.jensen_metric(B_ab, TAU)
    E_frame = tds.orthonormal_frame(g_s)
    ft = tds.frame_structure_constants(f_abc, E_frame)
    Gamma_conn = tds.connection_coefficients(ft)
    gammas = tds.build_cliff8()
    Omega = tds.spinor_connection_offset(Gamma_conn, gammas)
    cliff_err = tds.validate_clifford(gammas)                            # (local)
    mc_err = tds.validate_connection(Gamma_conn)                        # (local)
    print(f"  Clifford-algebra error : {cliff_err:.2e}")
    print(f"  Metric-compat error    : {mc_err:.2e}")
    print(f"  Built in {time.time() - t_geo:.2f}s")
    print()

    levels_to_build = [13, 14]                                           # (local)
    print("Building fresh sectors on GPU (eigvalsh, complex128):")
    print(f"  {'(p,q)':>8s}  {'L':>2s}  {'dim':>5s}  {'matdim':>7s}  "
          f"{'wall(s)':>8s}  {'VRAM(MB)':>9s}  {'|lam|range':>22s}")

    total_wall = 0.0                                                     # (local)
    peak_vram_overall = 0.0                                              # (local)
    for L in levels_to_build:
        for p in range(L + 1):
            q = L - p
            if (p, q) in sector_evals:
                continue
            rho, dim_check = build_irrep_with_fallback(p, q, gens, f_abc)
            assert dim_check == dim_su3(p, q), f"dim mismatch (p,q)=({p},{q})"
            pos_abs, dim_rho, wall_s, peak_vram_MB = compute_sector_eigenvalues_gpu(
                rho, E_frame, gammas, Omega
            )
            sector_evals[(p, q)] = {
                "dim": dim_rho,
                "level": L,
                "abs_evals": pos_abs,
            }
            total_wall += wall_s
            peak_vram_overall = max(peak_vram_overall, peak_vram_MB)
            lam_min = float(np.min(pos_abs)) if len(pos_abs) else float('nan')  # (local)
            lam_max = float(np.max(pos_abs)) if len(pos_abs) else float('nan')  # (local)
            print(f"  ({p:>2d},{q:>2d}) {L:>3d}  {dim_rho:>5d}  {16 * dim_rho:>7d}  "
                  f"{wall_s:>8.2f}  {peak_vram_MB:>9.1f}  "
                  f"[{lam_min:.3f},{lam_max:.3f}]")
            sys.stdout.flush()
    print()
    print(f"  Total fresh-sector wall: {total_wall:.1f}s")
    print(f"  Peak VRAM observed:      {peak_vram_overall:.1f} MB = {peak_vram_overall/1e3:.3f} GB")
    print()

    return sector_evals, peak_vram_overall


# -----------------------------------------------------------------------------
# Section 8 -- Spectral observables (PV residue + Weyl d_eff)
# -----------------------------------------------------------------------------

def pv_subtracted_moment(s, lambdas, mks, M):
    """R_PV(L; M) = sum_k m_k lambda_k^{-s} - sum_k m_k (lambda_k^2 + M^2)^{-s/2}
    Matches W1b-1 verbatim.
    """
    bare = np.sum(mks * np.power(lambdas, -s))                          # (local)
    pv_shift = np.sum(mks * np.power(lambdas * lambdas + M * M, -s / 2.0))  # (local)
    return float(bare - pv_shift), float(bare), float(pv_shift)


def weyl_counting_function(abs_evals_sorted, n_grid=400):
    """N(lambda) = #{|lambda_i| <= lambda} on log-spaced grid. Matches W1b-2."""
    if len(abs_evals_sorted) == 0:
        return np.array([]), np.array([])
    lam_min = abs_evals_sorted[0]                                       # (local)
    lam_max = abs_evals_sorted[-1]                                      # (local)
    if lam_min <= 0:
        positive = abs_evals_sorted[abs_evals_sorted > 0]                # (local)
        lam_min = positive[0] if positive.size else 1e-12
    lambda_grid = np.logspace(np.log10(lam_min), np.log10(lam_max), n_grid)  # (local)
    N_count = np.searchsorted(abs_evals_sorted, lambda_grid, side="right").astype(np.float64)  # (local)
    return lambda_grid, N_count


def fit_weyl_law_with_multiplicity(lambdas_repeated_sorted, fit_lo_frac=0.30,
                                    fit_hi_frac=0.95, n_grid=400):
    """Same windowed log-log fit as W1b-2's fit_weyl_law, but applied to the
    multiplicity-expanded sorted spectrum so that d_eff is computed on the
    Peter-Weyl-weighted Weyl counting function (matches W1b-2 at L=12).

    Returns (slope, d_eff_convA, d_eff_convB, C_fit, chi2_per_dof, n_fit).
      d_eff_convA = 2 * slope  (plan-pinned convention)
      d_eff_convB = slope      (s28c convention; advisory)
    """
    lam_grid, N_count = weyl_counting_function(lambdas_repeated_sorted, n_grid=n_grid)
    if len(lam_grid) < 4:
        return tuple(float('nan') for _ in range(6))
    valid = N_count > 0                                                  # (local)
    lam = lam_grid[valid]                                                # (local)
    N = N_count[valid]                                                   # (local)
    if len(lam) < 4:
        return tuple(float('nan') for _ in range(6))
    log_lam = np.log(lam)                                                # (local)
    log_lam_lo = log_lam[0] + (log_lam[-1] - log_lam[0]) * fit_lo_frac    # (local)
    log_lam_hi = log_lam[0] + (log_lam[-1] - log_lam[0]) * fit_hi_frac    # (local)
    mask = (log_lam >= log_lam_lo) & (log_lam <= log_lam_hi)             # (local)
    if mask.sum() < 4:
        return tuple(float('nan') for _ in range(6))
    x = log_lam[mask]                                                    # (local)
    y = np.log(N[mask])                                                  # (local)
    n_fit = len(x)                                                       # (local)
    A = np.vstack([np.ones_like(x), x]).T                                # (local)
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)                         # (local)
    a, b = float(coef[0]), float(coef[1])                                # (local) intercept, slope
    d_eff_convA = 2.0 * b                                                # (local)
    d_eff_convB = b                                                      # (local)
    C_fit = float(np.exp(a))                                             # (local)
    y_pred = a + b * x                                                   # (local)
    rss = float(np.sum((y - y_pred) ** 2))                               # (local)
    dof = max(n_fit - 2, 1)                                              # (local)
    chi2_per_dof = rss / dof                                             # (local)
    return float(b), float(d_eff_convA), float(d_eff_convB), C_fit, float(chi2_per_dof), int(n_fit)


def repeat_with_multiplicity(lambdas, mults):
    """Expand (lambdas, mults) into a flat sorted array with each lambda
    repeated `mults` times. Matches the W1b-2 protocol where the cache has
    one entry per (eigenvalue, irrep) pair already; here mults are the
    irrep dimensions feeding back the Peter-Weyl counts.
    """
    expanded_chunks = []                                                 # (local)
    for lam, m in zip(lambdas, mults):
        m_int = int(round(m))                                            # (local)
        if m_int <= 0:
            continue
        expanded_chunks.append(np.full(m_int, lam, dtype=np.float64))
    if not expanded_chunks:
        return np.zeros(0, dtype=np.float64)
    return np.sort(np.concatenate(expanded_chunks))


# -----------------------------------------------------------------------------
# Section 9 -- Richardson 3-point extrapolation (canonical + plan-literal)
# -----------------------------------------------------------------------------

def richardson_3pt_canonical(L_arr, f_arr):
    """Canonical L^{-3}-asymptotic 3-point extrapolation via least-squares
    on the linearized model y = a + b*x with x_i = 1/L_i^3, y_i = f(L_i).

    Returns:
      f_inf       : a (intercept; the L->infty limit)
      c1          : b (the leading L^{-3} coefficient)
      residual    : max_i |f(L_i) - (a + b/L_i^3)|
    """
    L = np.asarray(L_arr, dtype=np.float64)                              # (local)
    f = np.asarray(f_arr, dtype=np.float64)                              # (local)
    x = 1.0 / (L ** 3)                                                   # (local)
    A = np.vstack([np.ones_like(x), x]).T                                # (local)
    coef, *_ = np.linalg.lstsq(A, f, rcond=None)                         # (local)
    a, b = float(coef[0]), float(coef[1])                                # (local)
    f_pred = a + b * x                                                   # (local)
    residual = float(np.max(np.abs(f - f_pred)))                         # (local)
    return a, b, residual, f_pred.tolist()


def richardson_3pt_plan_form(L_arr, f_arr):
    """Plan-literal substitution-chain Richardson form (per session-87-plan-w1b.md
    §W1b-3 Field 6b lines 583-585):
      R_3pt = [L_3^3 f(L_3) - L_2^3 f(L_2) + L_1^3 f(L_1)]
              / [L_3^3 - L_2^3 + L_1^3]
    """
    L1, L2, L3 = (float(L_arr[0]), float(L_arr[1]), float(L_arr[2]))      # (local)
    f1, f2, f3 = (float(f_arr[0]), float(f_arr[1]), float(f_arr[2]))      # (local)
    num = (L3 ** 3) * f3 - (L2 ** 3) * f2 + (L1 ** 3) * f1               # (local)
    den = (L3 ** 3) - (L2 ** 3) + (L1 ** 3)                              # (local)
    return float(num / den)


# -----------------------------------------------------------------------------
# Section 10 -- Plot
# -----------------------------------------------------------------------------

def make_plot(L_list, d_eff_convA, d_eff_convB, pv_res,
              d_eff_inf_convA, d_eff_inf_convB, pv_inf,
              residual_d_eff_convA, residual_d_eff_convB, residual_pv,
              vram_gb, feasibility_pass):
    fig, axes = plt.subplots(1, 3, figsize=(20, 5.5))

    L_arr = np.asarray(L_list, dtype=np.float64)                         # (local)

    ax = axes[0]
    ax.plot(L_arr, d_eff_convA, "o-", color="C0", lw=2,
            label="Convention A: d_eff = 2·slope (plan-pinned)")
    ax.plot(L_arr, d_eff_convB, "s--", color="C1", lw=1.6,
            label="Convention B: d_eff = slope (s28c; advisory)")
    ax.axhline(d_eff_inf_convA, ls=":", color="C0", alpha=0.7,
               label=f"L^-3 extrap (A): d_inf = {d_eff_inf_convA:.4f}")
    ax.axhline(d_eff_inf_convB, ls=":", color="C1", alpha=0.7,
               label=f"L^-3 extrap (B): d_inf = {d_eff_inf_convB:.4f}")
    ax.axhspan(PASS_D_EFF_BAND[0], PASS_D_EFF_BAND[1], color="green", alpha=0.10,
               label=f"PASS band [{PASS_D_EFF_BAND[0]},{PASS_D_EFF_BAND[1]}]")
    ax.axhspan(INFO_D_EFF_BAND[0], INFO_D_EFF_BAND[1], color="orange", alpha=0.05,
               label=f"INFO band [{INFO_D_EFF_BAND[0]},{INFO_D_EFF_BAND[1]}]")
    ax.set_xlabel("L_max")
    ax.set_ylabel("d_eff (Weyl exponent fit)")
    ax.set_title("(A) d_eff convergence: both conventions")
    ax.legend(fontsize=8, loc="best")
    ax.grid(alpha=0.3)
    ax.set_xticks(L_arr)

    ax = axes[1]
    ax.plot(L_arr, pv_res, "o-", color="C2", lw=2, label="R_PV(L; M_KK)")
    ax.axhline(pv_inf, ls=":", color="C2", alpha=0.7,
               label=f"L^-3 extrap: R_PV_inf = {pv_inf:.4e}")
    ax.set_xlabel("L_max")
    ax.set_ylabel("R_PV at s=3")
    ax.set_title("(B) PV-residue convergence")
    ax.legend(fontsize=9, loc="best")
    ax.grid(alpha=0.3)
    ax.set_xticks(L_arr)

    ax = axes[2]
    feas_color = "g" if feasibility_pass else "r"                        # (local)
    summary = (
        f"VRAM feasibility: {'PASS' if feasibility_pass else 'FAIL'}\n"
        f"  per-sector dense (cx128): {vram_gb:.3f} GB\n"
        f"  ceiling (0.5 * 17.1 GB) : {VRAM_FEASIBILITY_GB:.1f} GB\n"
        f"\n"
        f"Richardson 3-point (canonical, L^-3):\n"
        f"  d_eff_inf (Conv A) = {d_eff_inf_convA:.6f}\n"
        f"     residual_max   = {residual_d_eff_convA:.3e}\n"
        f"  d_eff_inf (Conv B) = {d_eff_inf_convB:.6f}\n"
        f"     residual_max   = {residual_d_eff_convB:.3e}\n"
        f"  R_PV_inf           = {pv_inf:.6e}\n"
        f"     residual_max   = {residual_pv:.3e}\n"
        f"\n"
        f"PASS bands:\n"
        f"  d_eff_inf in [{PASS_D_EFF_BAND[0]},{PASS_D_EFF_BAND[1]}]\n"
        f"  residual < {PASS_RESIDUAL_THRESHOLD:.0e}"
    )
    ax.text(0.04, 0.96, summary, ha="left", va="top", fontsize=10,
            family="monospace", transform=ax.transAxes,
            bbox=dict(facecolor=feas_color, alpha=0.15))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.set_xticks([]); ax.set_yticks([])
    ax.set_title("(C) Richardson L^-3 extrapolation summary")

    fig.suptitle(f"S87 W1b-3 L_max-Weyl Convergence Sweep "
                 f"(L = {L_list[0]}, {L_list[1]}, {L_list[2]})",
                 fontsize=13)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=120, bbox_inches="tight")
    plt.close(fig)


# -----------------------------------------------------------------------------
# Section 11 -- Verdict + 4-tuple
# -----------------------------------------------------------------------------

def emit_4tuple(value, scheme, convention, L_max):
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict, value, audit_sha, content_sha,
                   sign_v, mag_v, regime_v):
    """Atomic append: canonical line + dual-SHA companion + Schema-v2 3-tuple."""
    canonical = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    dual_sha_row = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    schema_v2_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
        f"regime_verdict={regime_v} # {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical)
        fp.write(dual_sha_row)
        fp.write(schema_v2_row)


def evaluate_3tuple(residual_d_eff_convA, d_eff_inf_convA,
                     residual_pv, feasibility_pass):
    """Apply the plan-pinned PASS/INFO/FAIL bands to (residual, d_eff, PV)."""
    sign_v = "N/A"                                                       # (local) AUDIT-style; no directional pre-reg

    # magnitude_verdict on plan-pinned (Convention A) extrapolation residual + d_eff band
    pass_residual = residual_d_eff_convA < PASS_RESIDUAL_THRESHOLD       # (local)
    info_residual = residual_d_eff_convA < INFO_RESIDUAL_THRESHOLD        # (local)
    pass_band = (PASS_D_EFF_BAND[0] <= d_eff_inf_convA <= PASS_D_EFF_BAND[1])   # (local)
    info_band = (INFO_D_EFF_BAND[0] <= d_eff_inf_convA <= INFO_D_EFF_BAND[1])   # (local)
    fail_band = not (FAIL_D_EFF_BAND[0] <= d_eff_inf_convA <= FAIL_D_EFF_BAND[1])  # (local)
    pass_pv = residual_pv < 1e-6                                         # (local)

    if pass_residual and pass_band and pass_pv:
        mag_v = "PASS"
    elif fail_band:
        mag_v = "FAIL"
    elif info_residual or info_band:
        mag_v = "INFO"
    else:
        mag_v = "FAIL"

    # regime_verdict
    if not feasibility_pass:
        regime_v = "BREAKDOWN"
    else:
        regime_v = "VALID"

    return sign_v, mag_v, regime_v


def collapse_verdict(sign_v, mag_v, regime_v):
    """Composite-collapse rule per gate-verdicts.md §"S87+ canonical form"."""
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


# -----------------------------------------------------------------------------
# Section 12 -- Main
# -----------------------------------------------------------------------------

def main():
    t_start = time.time()                                                # (local)
    print("=" * 78)
    print(f"{GATE_ID} -- L_max ∈ {{10, 12, 14}} Richardson 3-point sweep")
    print("=" * 78)
    print(f"torch: {torch.__version__}, CUDA available: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"GPU: {torch.cuda.get_device_name(0)}")
    print(f"tau_fold = {TAU} (Jensen deformation @ fold)")
    print()

    # 1. Pin SHAs
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)                                         # (local)
    print(f"  legacy closure: {closure[:16]}...")

    script_path = Path(__file__).resolve()                              # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')               # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    # 2. Verify trigger predicate (already verified TRUE upstream by orchestrator;
    # we re-verify in-script for the audit trail).
    print("=== Trigger predicate verification (re-check) ===")
    w1b1 = np.load(W1B1_NPZ, allow_pickle=True)                          # (local)
    pv_L10_w1b1 = float(w1b1["pv_residue_L10"])                          # (local)
    pv_L12_w1b1 = float(w1b1["pv_residue_L12"])                          # (local)
    arm1_value = abs(pv_L10_w1b1 - pv_L12_w1b1)                          # (local)
    arm1_threshold = 1e-3                                                # (local)
    arm1_fires = arm1_value > arm1_threshold                             # (local)
    print(f"  arm1 = |pv_residue_L10 - pv_residue_L12| = "
          f"|{pv_L10_w1b1:.6e} - {pv_L12_w1b1:.6e}| = {arm1_value:.6e}")
    print(f"  arm1 threshold: 1e-3; arm1 fires: {arm1_fires}")
    arm2_NA_reason = ("arm2 (max|d_eff_k_L10 - d_eff_k_L12| > 0.10) NOT literally "
                      "evaluable: W1b-2 npz contains L=12 d_eff_stratum_k only "
                      "(no L=10 partition); W1b-2 verdict was FAIL "
                      "(max_deviation=2.287, d_eff~10 globally), which under the "
                      "structural reading IS the second-arm condition")
    print(f"  arm2 NOT literally evaluable: {arm2_NA_reason}")
    print(f"  TRIGGER FIRES (arm1 alone): {arm1_fires}")
    print()
    if not arm1_fires:
        print("  TRIGGER did NOT fire; mechanical closure should have run instead. "
              "Aborting compute branch.")
        return 1

    # 3. VRAM feasibility audit (HARD GATE; Step 1 of plan)
    feasibility_pass, vram_gb_per_sector, max_matrix_dim = vram_feasibility_audit(L_MAX)
    if not feasibility_pass:
        print("VRAM-feasibility breach -> emitting FAIL_BY_FEASIBILITY verdict and stopping.")
        # Emit FAIL verdict per regime BREAKDOWN
        sign_v, mag_v, regime_v = ("N/A", "FAIL", "BREAKDOWN")
        composite = collapse_verdict(sign_v, mag_v, regime_v)            # (local)
        # Save minimal output for audit trail
        np.savez(
            OUT_NPZ,
            trigger_predicate_arm1_value=arm1_value,
            trigger_predicate_arm2_NA_reason=arm2_NA_reason,
            vram_feasibility_pass=False,
            vram_per_sector_gb=vram_gb_per_sector,
            l_inf_fit_form="richardson_3_point_NOT_RUN_FAIL_BY_FEASIBILITY",
        )
        append_verdict(composite, vram_gb_per_sector, audit_sha, content_sha,
                       sign_v, mag_v, regime_v)
        return 1

    # 4. Load L=12 master cache; regenerate L=14 cache
    print(f"Loading L=12 master cache: {CACHE_L12.name}")
    sector_evals_L12 = load_sector_cache(CACHE_L12)                      # (local)
    levels_in_L12 = sorted(set(s["level"] for s in sector_evals_L12.values()))  # (local)
    print(f"  Loaded {len(sector_evals_L12)} sectors; levels in cache: {levels_in_L12}")
    print()

    if CACHE_L14_OUT.exists():
        print(f"Found existing L=14 cache: {CACHE_L14_OUT.name}; reusing.")
        sector_evals_L14 = load_sector_cache(CACHE_L14_OUT)              # (local)
        levels_in_L14 = sorted(set(s["level"] for s in sector_evals_L14.values()))  # (local)
        print(f"  Cached: {len(sector_evals_L14)} sectors; levels: {levels_in_L14}")
        peak_vram_observed_MB = float('nan')                             # (local)
    else:
        print(f"L=14 cache absent; regenerating fresh sectors at p+q in {{13, 14}}.")
        sector_evals_L14, peak_vram_observed_MB = regenerate_L14_cache(sector_evals_L12)
        # Save extended cache
        np.savez(CACHE_L14_OUT, sector_evals=sector_evals_L14)
        print(f"  Saved cache: {CACHE_L14_OUT.name} ({len(sector_evals_L14)} sectors)")
        print()

    # 5. Per-L observable refits
    print("=== Per-L observable refits ===")
    L_list = [10, 12, 14]                                                # (local)
    s_pole = 3.0                                                         # (local) substrate-distance-1 pole
    M = M_KK_DIMLESS                                                     # (local) PV mass scale

    pv_residue_per_L = []                                                # (local)
    bare_residue_per_L = []                                              # (local)
    pv_shift_per_L = []                                                  # (local)
    d_eff_global_convA_per_L = []                                        # (local)
    d_eff_global_convB_per_L = []                                        # (local)
    chi2_global_per_L = []                                               # (local)
    n_eigs_per_L = []                                                    # (local)
    sum_mults_per_L = []                                                 # (local)
    d_eff_stratum_convA_per_L = []                                       # (local) per-L 4-stratum array
    d_eff_stratum_convB_per_L = []                                       # (local)

    for L in L_list:
        print(f"  L={L}:")
        # Use L=14 cache (which contains all sectors p+q <= 14) for all L
        # truncations; matches W1b-1's level-truncate-from-master-cache pattern.
        cache_used = sector_evals_L14 if L > 12 else sector_evals_L14    # (local)
        lambdas, mks = collect_lambdas_mults(cache_used, L)              # (local)
        n_distinct = len(lambdas)                                        # (local)
        sum_mult = float(np.sum(mks))                                    # (local)
        n_eigs_per_L.append(n_distinct)
        sum_mults_per_L.append(sum_mult)
        print(f"    distinct |lambda|: {n_distinct}, sum_mult: {sum_mult:.0f}")
        print(f"    |lambda| range: [{lambdas.min():.4f}, {lambdas.max():.4f}]")

        # PV-subtracted residue at s=3
        pv_L, bare_L, shift_L = pv_subtracted_moment(s_pole, lambdas, mks, M)
        pv_residue_per_L.append(pv_L)
        bare_residue_per_L.append(bare_L)
        pv_shift_per_L.append(shift_L)
        print(f"    R_PV(L={L}; M_KK={M}) = {pv_L:.6e}")
        print(f"    bare residue          = {bare_L:.6e}")
        print(f"    PV-shift              = {shift_L:.6e}")

        # Weyl d_eff (global, both conventions). The BINDING array for the
        # plan-pinned PASS criterion is the W1b-2 protocol: raw abs_evals
        # concatenation (no Peter-Weyl multiplicity expansion). This matches
        # W1b-2's d_eff = 10.07 at L=12 calibration that the plan PASS band
        # [7.99, 8.01] is referenced against.
        lam_w1b2_sorted = collect_lambdas_w1b2_protocol(cache_used, L)   # (local) binding axis
        slope, d_eff_A, d_eff_B, C_fit, chi2_dof, n_fit = fit_weyl_law_with_multiplicity(
            lam_w1b2_sorted, fit_lo_frac=0.30, fit_hi_frac=0.95, n_grid=400
        )
        d_eff_global_convA_per_L.append(d_eff_A)
        d_eff_global_convB_per_L.append(d_eff_B)
        chi2_global_per_L.append(chi2_dof)
        print(f"    n_evals (W1b-2 protocol) = {len(lam_w1b2_sorted)}")
        print(f"    Weyl slope (log-log, [30%,95%] window) = {slope:.6f}")
        print(f"    d_eff (Conv A: 2*slope; plan-pinned)   = {d_eff_A:.6f}")
        print(f"    d_eff (Conv B: slope; advisory)         = {d_eff_B:.6f}")
        print(f"    chi2/dof = {chi2_dof:.4f}, n_fit = {n_fit}")
        # Cross-check: Peter-Weyl-expanded counting (W1b-1 PV-moment convention)
        lam_PW_sorted = repeat_with_multiplicity(lambdas, mks)            # (local)
        _, d_eff_A_PW, d_eff_B_PW, _, _, _ = fit_weyl_law_with_multiplicity(
            lam_PW_sorted, fit_lo_frac=0.30, fit_hi_frac=0.95, n_grid=400
        )
        print(f"    cross-check Peter-Weyl-expanded d_eff (A) = {d_eff_A_PW:.6f}")
        print(f"    cross-check Peter-Weyl-expanded d_eff (B) = {d_eff_B_PW:.6f}")

        # Per-stratum d_eff (V_4 4-stratum partition; matches W1b-2 protocol
        # verbatim: cluster on the W1b-2 raw abs_evals sorted array, NOT on
        # the Peter-Weyl-expanded array)
        n_strata = 4                                                     # (local)
        lam_sorted = lam_w1b2_sorted                                     # (local) binding array
        cluster_eps = 1e-9                                               # (local)
        cluster_starts = [0]                                             # (local)
        for i in range(1, len(lam_sorted)):
            if lam_sorted[i] - lam_sorted[i - 1] > cluster_eps:
                cluster_starts.append(i)
        cluster_starts.append(len(lam_sorted))
        n_clusters = len(cluster_starts) - 1                             # (local)
        stratum_idx = np.empty(len(lam_sorted), dtype=np.int32)          # (local)
        for ci in range(n_clusters):
            stratum_idx[cluster_starts[ci]:cluster_starts[ci + 1]] = ci % n_strata

        d_eff_strat_convA = np.zeros(n_strata, dtype=np.float64)         # (local)
        d_eff_strat_convB = np.zeros(n_strata, dtype=np.float64)         # (local)
        for k in range(n_strata):
            mask = stratum_idx == k                                      # (local)
            lam_k = lam_sorted[mask]                                     # (local)
            slope_k, d_A_k, d_B_k, _, _, _ = fit_weyl_law_with_multiplicity(
                lam_k, fit_lo_frac=0.30, fit_hi_frac=0.95, n_grid=400
            )
            d_eff_strat_convA[k] = d_A_k
            d_eff_strat_convB[k] = d_B_k
        d_eff_stratum_convA_per_L.append(d_eff_strat_convA)
        d_eff_stratum_convB_per_L.append(d_eff_strat_convB)
        print(f"    d_eff per-stratum (Conv A) = {d_eff_strat_convA.tolist()}")
        print(f"    d_eff per-stratum (Conv B) = {d_eff_strat_convB.tolist()}")
        print()

    # 6. Richardson 3-point extrapolation (canonical L^{-3}; both conventions)
    print("=== Richardson 3-point extrapolation (canonical L^-3 form) ===")
    L_arr = np.asarray(L_list, dtype=np.float64)                         # (local)

    # d_eff Convention A
    d_eff_inf_A, c1_A, residual_d_eff_A, fitvals_A = richardson_3pt_canonical(
        L_arr, np.asarray(d_eff_global_convA_per_L)
    )
    print(f"  d_eff Convention A (plan-pinned):")
    print(f"    d_eff(L) = {d_eff_global_convA_per_L}")
    print(f"    f_inf = {d_eff_inf_A:.6f}, c1/L^3 coeff = {c1_A:.6e}")
    print(f"    residual_max = {residual_d_eff_A:.3e}")
    # Plan-literal form (advisory, not verdict)
    r3pt_plan_A = richardson_3pt_plan_form(L_arr, d_eff_global_convA_per_L)  # (local)
    print(f"    plan-literal form R_3pt = {r3pt_plan_A:.6f} (advisory)")

    # d_eff Convention B
    d_eff_inf_B, c1_B, residual_d_eff_B, fitvals_B = richardson_3pt_canonical(
        L_arr, np.asarray(d_eff_global_convB_per_L)
    )
    print(f"  d_eff Convention B (s28c; advisory):")
    print(f"    d_eff(L) = {d_eff_global_convB_per_L}")
    print(f"    f_inf = {d_eff_inf_B:.6f}, c1/L^3 coeff = {c1_B:.6e}")
    print(f"    residual_max = {residual_d_eff_B:.3e}")

    # PV residue
    pv_inf, pv_c1, residual_pv, fitvals_pv = richardson_3pt_canonical(
        L_arr, np.asarray(pv_residue_per_L)
    )
    print(f"  PV residue:")
    print(f"    R_PV(L) = {pv_residue_per_L}")
    print(f"    f_inf = {pv_inf:.6e}, c1/L^3 coeff = {pv_c1:.6e}")
    print(f"    residual_max = {residual_pv:.3e}")
    print()

    # 7. Schema-v2 3-tuple verdict
    sign_v, mag_v, regime_v = evaluate_3tuple(
        residual_d_eff_A, d_eff_inf_A, residual_pv, feasibility_pass
    )
    composite = collapse_verdict(sign_v, mag_v, regime_v)                # (local)

    print(f"=== Schema-v2 3-tuple verdict ===")
    print(f"  sign_verdict      = {sign_v}    (AUDIT-style; no directional pre-reg)")
    print(f"  magnitude_verdict = {mag_v}")
    print(f"  regime_verdict    = {regime_v}")
    print(f"  composite collapse: {composite}")
    print()

    # 8. Save data
    np.savez(
        OUT_NPZ,
        L_list=np.asarray(L_list, dtype=np.int32),
        d_eff_global_L10_convA=d_eff_global_convA_per_L[0],
        d_eff_global_L12_convA=d_eff_global_convA_per_L[1],
        d_eff_global_L14_convA=d_eff_global_convA_per_L[2],
        d_eff_global_L10_convB=d_eff_global_convB_per_L[0],
        d_eff_global_L12_convB=d_eff_global_convB_per_L[1],
        d_eff_global_L14_convB=d_eff_global_convB_per_L[2],
        d_eff_stratum_k_L10_convA=d_eff_stratum_convA_per_L[0],
        d_eff_stratum_k_L12_convA=d_eff_stratum_convA_per_L[1],
        d_eff_stratum_k_L14_convA=d_eff_stratum_convA_per_L[2],
        d_eff_stratum_k_L10_convB=d_eff_stratum_convB_per_L[0],
        d_eff_stratum_k_L12_convB=d_eff_stratum_convB_per_L[1],
        d_eff_stratum_k_L14_convB=d_eff_stratum_convB_per_L[2],
        pv_residue_L10=pv_residue_per_L[0],
        pv_residue_L12=pv_residue_per_L[1],
        pv_residue_L14=pv_residue_per_L[2],
        bare_residue_L10=bare_residue_per_L[0],
        bare_residue_L12=bare_residue_per_L[1],
        bare_residue_L14=bare_residue_per_L[2],
        l_inf_extrapolation_d_eff_convA=d_eff_inf_A,
        l_inf_extrapolation_d_eff_convB=d_eff_inf_B,
        l_inf_extrapolation_pv_residue=pv_inf,
        fit_residual_d_eff_convA=residual_d_eff_A,
        fit_residual_d_eff_convB=residual_d_eff_B,
        fit_residual_pv_residue=residual_pv,
        l_inf_fit_form="richardson_3_point",
        chi2_global_per_L=np.asarray(chi2_global_per_L, dtype=np.float64),
        n_eigs_per_L=np.asarray(n_eigs_per_L, dtype=np.int64),
        sum_mults_per_L=np.asarray(sum_mults_per_L, dtype=np.float64),
        trigger_predicate_arm1_value=arm1_value,
        trigger_predicate_arm2_NA_reason=arm2_NA_reason,
        vram_feasibility_pass=feasibility_pass,
        vram_per_sector_gb=vram_gb_per_sector,
        max_matrix_dim=max_matrix_dim,
        r3pt_plan_form_d_eff_convA=r3pt_plan_A,
        c1_d_eff_convA=c1_A,
        c1_d_eff_convB=c1_B,
        c1_pv_residue=pv_c1,
        sign_verdict=sign_v,
        magnitude_verdict=mag_v,
        regime_verdict=regime_v,
        composite_verdict=composite,
    )
    print(f"  data saved: {OUT_NPZ.name}")

    # 9. Plot
    make_plot(
        L_list=L_list,
        d_eff_convA=d_eff_global_convA_per_L,
        d_eff_convB=d_eff_global_convB_per_L,
        pv_res=pv_residue_per_L,
        d_eff_inf_convA=d_eff_inf_A,
        d_eff_inf_convB=d_eff_inf_B,
        pv_inf=pv_inf,
        residual_d_eff_convA=residual_d_eff_A,
        residual_d_eff_convB=residual_d_eff_B,
        residual_pv=residual_pv,
        vram_gb=vram_gb_per_sector,
        feasibility_pass=feasibility_pass,
    )
    print(f"  plot saved: {OUT_PNG.name}")
    print()

    # 10. 4-tuple emission (value = residual on Convention A; the plan-pinned axis)
    tag = emit_4tuple(residual_d_eff_A, SCHEME, CONVENTION, L_MAX)        # (local)
    print(tag)

    # 11. Append verdict (atomic dual-SHA + Schema-v2 3-tuple companion)
    append_verdict(composite, residual_d_eff_A, audit_sha, content_sha,
                   sign_v, mag_v, regime_v)

    wall = time.time() - t_start                                         # (local)
    print(f"\n=== {GATE_ID}: {composite} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
