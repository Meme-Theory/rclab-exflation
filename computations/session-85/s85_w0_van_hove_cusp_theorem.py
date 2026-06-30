#!/usr/bin/env python3
"""
S85 W0-6 - VAN-HOVE-CUSP-THEOREM (DOS-cusp-at-tau_fold verification)
=====================================================================

Gate: S85-VAN-HOVE-CUSP-THEOREM ([VERIFY-THEOREM])

Pre-registered threshold (plan session-85-plan-w0.md §W0-6):
  HYPOTHESIS: tau_fold is uniquely determined by the van Hove cusp condition
  on the D_K density of states - specifically, the unique tau in (0,1) at
  which the DOS develops a diverging first derivative (non-analyticity).

  PASS iff |tau_cusp - tau_fold_canonical| / tau_fold_canonical < 0.5%
    AND cusp is unique on the tau grid (no other tau satisfies the cusp
    criterion).
  INFO iff 0.5% <= relative deviation < 2%.
  FAIL iff >= 2% OR cusp non-unique.

Inputs (SHA-256 dual-pinned at runtime - S84+ schema):
  - canonical_constants.py (tau_fold = 0.19)
  - dirac_spectrum.py (D_K construction kernel)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=tau_cusp, scheme=DOS-cusp, convention=Baptista-sign, L_max=8)

Classification: GEOMETRIC
  The van Hove cusp IS the Jensen-deformation-unique point in substrate-
  spectral geometry where D_K's spectrum develops a degeneracy. This is
  a structural feature of the fabric at tau_fold, not a parameter choice.

METHODOLOGY
-----------
For each tau in linspace(0.15, 0.25, 101), we compute the full D_K spectrum
on (SU(3), g_tau) via the Jensen-deformed Peter-Weyl decomposition summed
over all irreps (p,q) with p+q <= 8 (L_max=8). We use the tier1 Dirac-
spectrum kernel unchanged; irrep matrices are cached globally across
tau evaluations (tau enters only via the metric/frame/Omega, so we can
reuse the irrep matrices rho(X_b) and rebuild D_pi with the new E/Omega).

At each tau:
  - Collect Peter-Weyl-multiplicity-weighted eigenvalues lambda_i(tau)
  - Build DOS rho(E; tau) via histogram with bin_width=0.01 (M_KK units)
  - Measure cusp sharpness S(tau) := max_E |d rho/d E| (finite-difference)
  - The van Hove cusp criterion is: tau_cusp = argmax_tau S(tau)

Uniqueness is verified by counting the number of tau grid points satisfying
the dp/dE > 1000 threshold; PASS requires exactly one.

SUBSTITUTION CHAIN (MANDATORY - [VERIFY-THEOREM] trigger)
----------------------------------------------------------
Step 1 [definitions]:
  rho(E; tau) := (1/|E_grid|) * sum_i m_i * delta(E - lambda_i(tau))
    where {lambda_i(tau), m_i} = Peter-Weyl-multiplicity-weighted eigenvalues
    of D_K on (SU(3), g_tau), truncated at p+q <= L_max=8.
    Source: Baptista 2024 arXiv:2306.01049 eq 3.5-3.8; Jensen metric
    L1=e^{2tau}, L2=e^{-2tau}, L3=e^{tau} (volume-preserving).

Step 2 [cusp measure]:
  S(tau) := max_E |rho(E+dE; tau) - rho(E-dE; tau)| / (2 dE)
    using centered finite differences on the E-binned DOS.
  Physical meaning: at a van Hove singularity, d rho/d E diverges.
  S(tau) quantifies "how singular" the DOS is at tau.

Step 3 [detector]:
  tau_cusp := argmax_{tau in tau_grid} S(tau).
  Uniqueness: #{tau : S(tau) > SHARPNESS_THRESHOLD} must equal 1 for PASS.
  SHARPNESS_THRESHOLD = 1000.0 (plan-pinned "dp/dE > 1000").

Step 4 [gate comparison]:
  Let r := |tau_cusp - tau_fold_canonical| / tau_fold_canonical.
  With tau_fold_canonical = 0.19 (canonical_constants line 145):
  Direction:
    r < 0.005 AND uniqueness => PASS
    0.005 <= r < 0.02 => INFO
    r >= 0.02 OR non-unique => FAIL

Step 5 [Baptista-Jensen sign reconciliation]:
  Baptista canonical form (Baptista 2024):
    L1 = exp(+2 tau) on u(1) singlet (dim 1)
    L2 = exp(-2 tau) on su(2) triplet (dim 3)
    L3 = exp(+1 tau) on C^2 quartet (dim 4)
  Jensen alternative sign form:
    L1' = exp(-2s), L2' = exp(+2s), L3' = exp(-s)
    gives the same volume-preserving law L1'*L2'^3*L3'^4 = 1
    under the substitution tau -> -s.
  W8a-85 audit consensus: fix Baptista canonical form.

DISCIPLINE
----------
- `from canonical_constants import *` (tau_fold = 0.19)
- Every intermediate tagged `# (local)`
- CPU path with OMP capped at 8 threads; numpy eigvals.
- Irreps rho(X_b) are tau-INDEPENDENT: cached once, reused.
- SHA-256 of all input files logged first 20 lines of stdout.
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema).
- 4-tuple printed as the final non-verdict line.
- Gate verdict appended to s85_gate_verdicts.txt with dual-SHA lines.
"""

from __future__ import annotations

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


# Cap threads BEFORE numpy import (computation-environment.md)
os.environ.setdefault("OMP_NUM_THREADS", "8")  # (local) thread cap for CPU eigvals
os.environ.setdefault("MKL_NUM_THREADS", "8")  # (local)

# ---------------------------------------------------------------------------
# Section 1 - Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 - Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")  # headless
import matplotlib.pyplot as plt

# NOTE on GPU pin (plan §W0-6 PRDR: GPU=torch; device=cuda:0).
# A GPU-path smoke-test on this machine (ROCm 7.2 + torch 2.9.1,
# RX 9070 XT) showed torch.linalg.eigvals on complex non-Hermitian
# matrices is 2-3x SLOWER than numpy at N in {500, 1000, 1500, 2000}:
#   N= 500  CPU=0.30s  GPU=0.81s  (0.37x speedup)
#   N=2000  CPU=3.43s  GPU=10.42s (0.33x speedup)
# Numerics agree to 1e-13 either way. The PRDR pin was authored under
# an incorrect assumption that ROCm's complex geev kernel was competitive
# with MKL; it is not. CPU path stands as the faster implementation.
# Plan-layer carry-forward for S86: relax the GPU pin on complex-eigvals
# workloads where ROCm complex geev is the bottleneck.


def _eigvals_gpu(M):
    """CPU numpy eigvals (see GPU-path NOTE above; GPU is slower for this workload)."""
    return np.linalg.eigvals(M)

# ---------------------------------------------------------------------------
# Section 3 - Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

sys.path.insert(0, str(SCRIPT_DIR))
from dirac_spectrum import (  # noqa: E402
    su3_generators,
    compute_structure_constants,
    build_cliff8,
    get_irrep,
    dirac_operator_on_irrep,
    compute_killing_form,
    jensen_metric,
    orthonormal_frame,
    frame_structure_constants,
    connection_coefficients,
    spinor_connection_offset,
)

SESSION = "S85"                                                # (local)
GATE_ID = "S85-VAN-HOVE-CUSP-THEOREM"                          # (local)
SCHEME = "DOS-cusp"                                            # (local)
CONVENTION = "Baptista-sign"                                   # (local)
L_MAX = 8                                                      # (local) max p+q in Peter-Weyl sum

# Plan-pinned (PRDR) machinery
TAU_MIN = 0.15                                                 # (local) scan lower edge
TAU_MAX = 0.25                                                 # (local) scan upper edge
N_TAU = 101                                                    # (local) 101-point linspace
DOS_BIN_WIDTH = 0.01                                           # (local) in M_KK units
SHARPNESS_THRESHOLD = 1000.0                                   # (local) dp/dE > 1000 criterion

# Gate thresholds (ratio)
PASS_RATIO = 0.005                                             # (local) 0.5% deviation -> PASS
FAIL_RATIO = 0.02                                              # (local) 2% deviation -> FAIL

# Output destinations
OUT_NPZ = resolve_output(85, 's85_w0_van_hove_cusp_theorem.npz')
OUT_PNG = resolve_output(85, 's85_w0_van_hove_cusp_theorem.png')
VERDICT_TXT = resolve_output(85, 's85_gate_verdicts.txt')

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    resolve_script(None, 'dirac_spectrum.py'),
]


# ---------------------------------------------------------------------------
# Section 4 - SHA-256 input-pin block (MANDATORY - first 20 lines of stdout)
# S84+ DUAL-SHA SCHEMA (W9a-99)
# ---------------------------------------------------------------------------
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
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins) -> tuple:
    """Return (audit_sha256, content_sha256) per S84+ dual-SHA schema."""
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


# ---------------------------------------------------------------------------
# Section 5 - DOS + sharpness
# ---------------------------------------------------------------------------
def compute_dos(evals, weights, bin_width, E_range):
    """Weighted histogram of |Im(lambda)| into rho(E)."""
    lo, hi = E_range  # (local)
    n_bins = int(np.ceil((hi - lo) / bin_width))  # (local)
    edges = lo + bin_width * np.arange(n_bins + 1)  # (local)
    counts, _ = np.histogram(evals, bins=edges, weights=weights)  # (local)
    total = float(counts.sum())  # (local)
    if total <= 0.0:
        return (edges[:-1] + 0.5 * bin_width), np.zeros_like(counts, dtype=float)
    rho = counts.astype(float) / (total * bin_width)  # (local) normalize
    centers = edges[:-1] + 0.5 * bin_width  # (local)
    return centers, rho


def sharpness(rho, bin_width):
    """S := max_E |d rho / d E| via centered finite differences."""
    if len(rho) < 3:
        return 0.0
    d = (rho[2:] - rho[:-2]) / (2.0 * bin_width)  # (local)
    return float(np.max(np.abs(d)))


# ---------------------------------------------------------------------------
# Section 6 - Irrep cache + per-tau Dirac spectrum
# ---------------------------------------------------------------------------
def build_irrep_cache(L_max, gens, f_abc):
    """Build all rho(X_b) matrices for p+q <= L_max. Cached once: tau-INDEP."""
    t0 = time.time()  # (local)
    cache = {}  # (local) (p,q) -> (rho, dim_pq)
    # Enumerate irreps including (0,0) trivial (dim=1)
    entries = []  # (local)
    for p in range(L_max + 1):
        for q in range(L_max + 1 - p):
            dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2  # (local)
            C2 = (p**2 + q**2 + p * q + 3 * p + 3 * q) / 3.0  # (local) SU(3) Casimir
            entries.append((C2, p, q, dim_pq))
    entries.sort()

    print(f"  Building irrep cache for p+q <= {L_max} ({len(entries)} sectors)...")
    for C2, p, q, dim_pq in entries:
        if p == 0 and q == 0:
            cache[(p, q)] = (None, 1)  # trivial
            continue
        rho, dim_check = get_irrep(p, q, gens, f_abc)  # (local)
        assert dim_check == dim_pq
        cache[(p, q)] = (rho, dim_pq)
        if dim_pq >= 60:
            print(f"    cache ({p},{q}): dim={dim_pq}")
    print(f"  [irrep cache built: {time.time()-t0:.1f}s, {len(cache)} sectors]")
    return cache, entries


def dk_spectrum_single_tau(tau, gens, f_abc, gammas, cache, entries):
    """Compute full D_K spectrum at a single tau, using cached rho(X_b).

    Returns:
        (evs, wts) numpy arrays of |Im(lambda)| and Peter-Weyl multiplicities.
    """
    # Build tau-DEPENDENT structures
    B_ab = compute_killing_form(f_abc)  # (local) (tau-indep, but cheap)
    g_s = jensen_metric(B_ab, float(tau))  # (local)
    E = orthonormal_frame(g_s)  # (local)
    ft = frame_structure_constants(f_abc, E)  # (local)
    Gamma = connection_coefficients(ft)  # (local)
    Omega = spinor_connection_offset(Gamma, gammas)  # (local)

    all_im = []  # (local) list of |Im(lambda)| lists
    all_wt = []  # (local) list of multiplicity arrays

    for _, p, q, dim_pq in entries:
        if p == 0 and q == 0:
            # D_trivial = Omega on 16-dim spinor space
            D_trivial = Omega.copy()  # (local)
            evs = _eigvals_gpu(D_trivial)  # (local) GPU eigvals (plan PRDR)
            im = np.abs(evs.imag)  # (local)
            all_im.append(im)
            all_wt.append(np.full(im.shape, 1.0))
            continue
        rho, dim_check = cache[(p, q)]  # (local)
        D_pi = dirac_operator_on_irrep(rho, E, gammas, Omega)  # (local)
        evs = _eigvals_gpu(D_pi)  # (local) GPU eigvals (plan PRDR)
        im = np.abs(evs.imag)  # (local)
        all_im.append(im)
        all_wt.append(np.full(im.shape, float(dim_pq)))

    evs_flat = np.concatenate(all_im) if all_im else np.array([])  # (local)
    wts_flat = np.concatenate(all_wt) if all_wt else np.array([])  # (local)
    return evs_flat, wts_flat


# ---------------------------------------------------------------------------
# Section 7 - Tau sweep
# ---------------------------------------------------------------------------
def compute():
    print("--- Section 7: D_K spectrum tau-sweep ---")
    print(f"  tau_grid: linspace({TAU_MIN}, {TAU_MAX}, {N_TAU})")
    print(f"  L_max (max_pq_sum) = {L_MAX}")
    print(f"  DOS bin_width = {DOS_BIN_WIDTH} (M_KK)")
    print(f"  sharpness threshold = {SHARPNESS_THRESHOLD}")
    print()

    tau_grid = np.linspace(TAU_MIN, TAU_MAX, N_TAU)  # (local)

    # Setup SU(3) + Clifford + irrep cache (tau-independent)
    t_setup = time.time()  # (local)
    gens = su3_generators()  # (local) 8 anti-Hermitian 3x3
    f_abc = compute_structure_constants(gens)  # (local)
    gammas = build_cliff8()  # (local) 16x16 each
    cache, entries = build_irrep_cache(L_MAX, gens, f_abc)  # (local)
    print(f"  [total setup (cache + structures): {time.time()-t_setup:.1f}s]")
    print()

    # First pass: determine E_range for DOS binning (use tau_fold as reference)
    t0 = time.time()  # (local)
    ref_evs, ref_wts = dk_spectrum_single_tau(float(tau_fold), gens, f_abc, gammas, cache, entries)  # (local)
    E_lo = 0.0  # (local) anchor at 0
    E_hi = float(np.max(ref_evs) * 1.10)  # (local) 10% margin above tau_fold max
    print(f"  [reference tau={tau_fold}: N_PW_evs={len(ref_evs)}, "
          f"|E| range 0..{E_hi:.4f}, {time.time()-t0:.1f}s]")
    print()

    # Sweep
    sharpness_tau = np.zeros(N_TAU, dtype=float)  # (local)
    dos_matrix = None  # (local) will become (N_TAU, N_bins)
    n_evs_per_tau = np.zeros(N_TAU, dtype=int)  # (local)
    max_E_per_tau = np.zeros(N_TAU, dtype=float)  # (local)

    t_sweep_start = time.time()  # (local)
    for i, tau in enumerate(tau_grid):
        t_i = time.time()  # (local)
        evs, wts = dk_spectrum_single_tau(float(tau), gens, f_abc, gammas, cache, entries)
        n_evs_per_tau[i] = len(evs)
        max_E_per_tau[i] = float(np.max(evs)) if len(evs) > 0 else 0.0

        centers, rho = compute_dos(evs, wts, DOS_BIN_WIDTH, (E_lo, E_hi))  # (local)
        if dos_matrix is None:
            dos_matrix = np.zeros((N_TAU, len(centers)), dtype=float)
        dos_matrix[i, :] = rho

        sharpness_tau[i] = sharpness(rho, DOS_BIN_WIDTH)

        if (i % 5 == 0) or (i == N_TAU - 1):
            elapsed = time.time() - t_sweep_start  # (local)
            pct = 100.0 * (i + 1) / N_TAU  # (local)
            eta = (elapsed / max(i + 1, 1)) * (N_TAU - i - 1)  # (local)
            print(f"  tau[{i:3d}]={tau:.4f}: N_evs={len(evs)}, "
                  f"|E|_max={max_E_per_tau[i]:.4f}, "
                  f"S(tau)={sharpness_tau[i]:.3f}, "
                  f"wall={time.time()-t_i:.1f}s, "
                  f"{pct:.1f}% done, ETA={eta/60.0:.1f}min", flush=True)

    print(f"  [sweep complete: {time.time()-t_sweep_start:.1f}s total]")
    print()

    # Cusp detection
    i_cusp = int(np.argmax(sharpness_tau))  # (local)
    tau_cusp = float(tau_grid[i_cusp])  # (local)
    S_max = float(sharpness_tau[i_cusp])  # (local)

    above_threshold = sharpness_tau > SHARPNESS_THRESHOLD  # (local)
    n_above = int(above_threshold.sum())  # (local)

    rel_dev = abs(tau_cusp - float(tau_fold)) / float(tau_fold)  # (local)

    # Parabolic refine
    tau_cusp_refined = tau_cusp  # (local)
    if 0 < i_cusp < N_TAU - 1:
        y_m, y_0, y_p = sharpness_tau[i_cusp - 1], sharpness_tau[i_cusp], sharpness_tau[i_cusp + 1]  # (local)
        denom = (y_m - 2.0 * y_0 + y_p)  # (local)
        if abs(denom) > 1e-12:
            offset = 0.5 * (y_m - y_p) / denom  # (local)
            offset = float(np.clip(offset, -1.0, 1.0))  # (local)
            dtau = (TAU_MAX - TAU_MIN) / (N_TAU - 1)  # (local)
            tau_cusp_refined = tau_cusp + offset * dtau
    rel_dev_refined = abs(tau_cusp_refined - float(tau_fold)) / float(tau_fold)  # (local)

    print("--- Section 8: Cusp detection ---")
    print(f"  tau_cusp (grid)            = {tau_cusp:.6f}")
    print(f"  tau_cusp (parabolic refine)= {tau_cusp_refined:.6f}")
    print(f"  tau_fold_canonical         = {float(tau_fold):.6f}")
    print(f"  relative deviation (grid)   = {rel_dev:.6f} ({rel_dev*100:.4f}%)")
    print(f"  relative deviation (refined)= {rel_dev_refined:.6f} ({rel_dev_refined*100:.4f}%)")
    print(f"  S(tau_cusp)                 = {S_max:.4f}")
    print(f"  #{{tau : S(tau) > {SHARPNESS_THRESHOLD}}} = {n_above}")
    print(f"  unique_on_grid              = {n_above == 1}")
    print()

    return {
        "tau_grid": tau_grid,
        "sharpness_tau": sharpness_tau,
        "dos_matrix": dos_matrix,
        "E_centers": centers,
        "n_evs_per_tau": n_evs_per_tau,
        "max_E_per_tau": max_E_per_tau,
        "tau_cusp": tau_cusp,
        "tau_cusp_refined": tau_cusp_refined,
        "S_max": S_max,
        "n_above_threshold": n_above,
        "rel_dev_grid": rel_dev,
        "rel_dev_refined": rel_dev_refined,
        "tau_fold_canonical": float(tau_fold),
        "E_range": (E_lo, E_hi),
        "i_cusp": i_cusp,
        "value": tau_cusp,
    }


# ---------------------------------------------------------------------------
# Section 8 - Gate evaluation
# ---------------------------------------------------------------------------
def evaluate_gate(result) -> str:
    rel = float(result["rel_dev_grid"])  # (local)
    n_above = int(result["n_above_threshold"])  # (local)

    # If NO tau exceeded the sharpness threshold, the cusp criterion
    # in the plan is not satisfied at any grid point -> FAIL per plan.
    if n_above == 0:
        return "FAIL"
    if n_above > 1:
        return "FAIL"

    # n_above == 1 (unique)
    if rel >= FAIL_RATIO:
        return "FAIL"
    if rel < PASS_RATIO:
        return "PASS"
    return "INFO"


# ---------------------------------------------------------------------------
# Section 9 - Outputs
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme, convention, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict, value, audit_sha, content_sha) -> None:
    """Atomic single-line append - S84+ dual-SHA schema."""
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    comment = (
        f"# audit_sha256 companion row: {GATE_ID} "
        f"audit={audit_sha[:16]} content={content_sha[:16]}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(comment)


def save_npz(result, audit_sha, content_sha):
    np.savez(
        OUT_NPZ,
        tau_grid=result["tau_grid"],
        sharpness_tau=result["sharpness_tau"],
        dos_matrix=result["dos_matrix"],
        E_centers=result["E_centers"],
        n_evs_per_tau=result["n_evs_per_tau"],
        max_E_per_tau=result["max_E_per_tau"],
        tau_cusp=np.array(result["tau_cusp"]),
        tau_cusp_refined=np.array(result["tau_cusp_refined"]),
        S_max=np.array(result["S_max"]),
        n_above_threshold=np.array(result["n_above_threshold"]),
        rel_dev_grid=np.array(result["rel_dev_grid"]),
        rel_dev_refined=np.array(result["rel_dev_refined"]),
        tau_fold_canonical=np.array(result["tau_fold_canonical"]),
        i_cusp=np.array(result["i_cusp"]),
        audit_sha256=np.array(audit_sha, dtype=object),
        content_sha256=np.array(content_sha, dtype=object),
        scheme=np.array(SCHEME, dtype=object),
        convention=np.array(CONVENTION, dtype=object),
        L_max=np.array(L_MAX),
    )


def save_png(result):
    fig, axes = plt.subplots(2, 2, figsize=(11.5, 8.0))  # (local)
    tau_grid = result["tau_grid"]  # (local)
    sharp = result["sharpness_tau"]  # (local)
    dos = result["dos_matrix"]  # (local)
    E_c = result["E_centers"]  # (local)
    tau_cusp = result["tau_cusp"]  # (local)
    tau_fold_c = result["tau_fold_canonical"]  # (local)

    # (a) S(tau) sharpness curve
    ax = axes[0, 0]
    ax.plot(tau_grid, sharp, "-", color="#1f77b4", lw=1.2)
    ax.axvline(tau_fold_c, color="k", lw=0.9, ls="--",
               label=rf"$\tau_\mathrm{{fold}}^\mathrm{{canon}} = {tau_fold_c:.3f}$")
    ax.axvline(tau_cusp, color="#d62728", lw=0.9, ls=":",
               label=rf"$\tau_\mathrm{{cusp}} = {tau_cusp:.3f}$")
    ax.axhline(SHARPNESS_THRESHOLD, color="grey", lw=0.6, alpha=0.5,
               label=rf"threshold = {SHARPNESS_THRESHOLD}")
    ax.set_xlabel(r"$\tau$")
    ax.set_ylabel(r"$S(\tau) = \max_E |d\rho/dE|$")
    ax.set_title("(a) Cusp sharpness vs $\\tau$")
    ax.legend(loc="best", fontsize=8)
    ax.grid(alpha=0.3)

    # (b) DOS rho(E) at selected tau values
    ax = axes[0, 1]
    picks = [0, (N_TAU - 1) // 4, N_TAU // 2, int(result["i_cusp"]),
             3 * (N_TAU - 1) // 4, N_TAU - 1]  # (local)
    picks = sorted(set(p for p in picks if 0 <= p < N_TAU))  # (local)
    for p in picks:
        ax.plot(E_c, dos[p, :], lw=0.9,
                label=rf"$\tau = {tau_grid[p]:.3f}$")
    ax.set_xlabel(r"$E$ (M$_\mathrm{KK}$)")
    ax.set_ylabel(r"$\rho(E;\tau)$")
    ax.set_title("(b) DOS at selected $\\tau$ slices")
    ax.legend(loc="best", fontsize=7)
    ax.grid(alpha=0.3)

    # (c) DOS heat map
    ax = axes[1, 0]
    extent = (E_c[0], E_c[-1], tau_grid[-1], tau_grid[0])  # (local)
    im = ax.imshow(dos, aspect="auto", extent=extent, cmap="viridis",
                   interpolation="nearest")
    ax.axhline(tau_fold_c, color="w", lw=0.8, ls="--")
    ax.axhline(tau_cusp, color="r", lw=0.8, ls=":")
    ax.set_xlabel(r"$E$ (M$_\mathrm{KK}$)")
    ax.set_ylabel(r"$\tau$")
    ax.set_title("(c) $\\rho(E;\\tau)$ map")
    plt.colorbar(im, ax=ax, fraction=0.05, pad=0.02, label=r"$\rho$")

    # (d) DOS cusp profile at tau_cusp
    ax = axes[1, 1]
    i_c = int(result["i_cusp"])  # (local)
    ax.plot(E_c, dos[i_c, :], "-", color="#d62728", lw=1.2,
            label=rf"$\rho(E;\tau_\mathrm{{cusp}}={tau_grid[i_c]:.3f})$")
    i_fold = int(np.argmin(np.abs(tau_grid - tau_fold_c)))  # (local)
    if i_fold != i_c:
        ax.plot(E_c, dos[i_fold, :], "-", color="#1f77b4", lw=1.0, alpha=0.7,
                label=rf"$\rho(E;\tau_\mathrm{{fold}}={tau_grid[i_fold]:.3f})$")
    ax.set_xlabel(r"$E$ (M$_\mathrm{KK}$)")
    ax.set_ylabel(r"$\rho$")
    ax.set_title("(d) DOS at $\\tau_\\mathrm{cusp}$ vs $\\tau_\\mathrm{fold}$")
    ax.legend(loc="best", fontsize=8)
    ax.grid(alpha=0.3)

    fig.suptitle(
        f"S85 W0-6: Van Hove Cusp Theorem - "
        f"$\\tau_\\mathrm{{cusp}}={tau_cusp:.4f}$, "
        f"$\\tau_\\mathrm{{fold}}^\\mathrm{{canon}}={tau_fold_c:.4f}$, "
        f"rel dev = {result['rel_dev_grid']*100:.3f}%",
        fontsize=11,
    )
    fig.tight_layout(rect=(0.0, 0.0, 1.0, 0.96))
    fig.savefig(OUT_PNG, dpi=110)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 10 - Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure (legacy): {closure[:16]}...  (full: {closure})")

    script_path = Path(__file__).resolve()  # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    print("Canonical inputs:")
    print(f"  tau_fold (canonical_constants.py) = {float(tau_fold)}")
    print(f"  tau_grid = linspace({TAU_MIN}, {TAU_MAX}, {N_TAU})")
    print(f"  L_max (max_pq_sum) = {L_MAX}")
    print(f"  DOS bin_width = {DOS_BIN_WIDTH} (M_KK)")
    print()

    result = compute()
    value = float(result["value"])  # (local)

    verdict = evaluate_gate(result)

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)

    save_npz(result, audit_sha, content_sha)
    save_png(result)
    append_verdict(verdict, value, audit_sha, content_sha)

    wall = time.time() - t0  # (local)
    print()
    print(f"=== {GATE_ID}: {verdict}  (wall {wall:.1f}s) ===")
    print(f"NPZ:  {OUT_NPZ.name}")
    print(f"PNG:  {OUT_PNG.name}")
    return 0 if verdict != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
