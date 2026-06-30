#!/usr/bin/env python
"""
S104-BRANCH-IV-DIRECT-L1314 — PHASE 1 builder (the multi-hour wall).

Offline / across-timeslot construction of the DIRECT D_K sectors for the deep-truncation
levels p+q in {13,14}, persisted INCREMENTALLY per-sector so partial progress survives a
timeout. The bottleneck is irrep CONSTRUCTION (recursive Casimir / symmetric-power), NOT
GPU diagonalization (per .claude/rules/math-scripts.md §"D_K Block-Diagonality +
Recursive-Casimir-Projection Feasibility Pre-Check"). S103 wall record: Sym^9 ~ 200.9 s
single-thread; Sym^13/14 are multi-hour.

For EACH (p,q) with p+q in {13,14}:
  rho, dim = get_irrep(p, q, gens, f_abc)          # CPU recursive-Casimir / Sym^p (the wall)
  D       = dirac_operator_on_irrep(...)           # anti-Hermitian
  evals   = torch.linalg.eigvalsh(i*D)             # GPU (RX 9070 XT, ROCm), NOT the bottleneck
  abs_evals = |evals|
persist {(p,q): {dim, level, abs_evals}} into the cache npz immediately.

This is the SAME assembly the s84 L12 master cache and the s103 build_new_level_sectors
used (Jensen s = tau_fold = 0.19); the moment-evaluator (Phase 2,
computations/session-104/s104_branch_iv_direct_l1314.py) reproduces rho_B(8,10,12) from the
s84 cache bit-for-bit before consuming these new sectors.

Output: computations/session-104/s104_sym_p_chain_cache_L1314.npz   (incremental, per-sector)
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")      # CPU recursive-Casimir; cap threads before numpy
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import time
import json
import numpy as np

# --- locate the shared computation modules ---
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))          # (local) computations/
SHARED = os.path.join(ROOT, "_shared")                                      # (local)
sys.path.insert(0, SHARED)

from canonical_constants import tau_fold            # Jensen deformation parameter = tau_fold = 0.19

OUT_CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "s104_sym_p_chain_cache_L1314.npz")                # (local)

JENSEN_S = tau_fold                                  # (local) = tau_fold; EXACT assembly the s84 cache used
LEVELS = (13, 14)                                   # (local) deep-truncation new levels (p+q)


def dim_su3(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2     # (local) SU(3) irrep dim


def load_existing():
    """Resume from any partial cache so a re-launch continues, not restarts."""
    done = {}                                       # (local) {(p,q): {dim, level, abs_evals}}
    timing = {}                                     # (local)
    if os.path.exists(OUT_CACHE):
        try:
            z = np.load(OUT_CACHE, allow_pickle=True)
            done = z["new_sectors"].item()
            if "timing_json" in z.files:
                tj = json.loads(str(z["timing_json"]))
                timing = {tuple(int(x) for x in k.split(",")): v for k, v in tj.items()}
            print(f"[resume] {len(done)} sectors already on disk: "
                  f"{sorted(done.keys())}", flush=True)
        except Exception as e:
            print(f"[resume] could not read existing cache ({e}); starting fresh", flush=True)
            done = {}
            timing = {}
    return done, timing


def persist(done, timing, status, herm_err_max, device):
    """Atomic-ish write of the incremental cache (write tmp, replace).

    NOTE: numpy's savez_compressed APPENDS '.npz' to the target path if it does not
    already end in '.npz'. We pass a base WITHOUT '.npz' so the actual file written is
    <base>.npz, then os.replace that onto OUT_CACHE.
    """
    tj = {f"{p},{q}": timing.get((p, q), 0.0) for (p, q) in done.keys()}     # (local)
    tmp_base = OUT_CACHE[:-4] + "_tmp"                # (local) strip '.npz'; savez re-appends it
    tmp_written = tmp_base + ".npz"                   # (local) the file savez actually creates
    np.savez_compressed(
        tmp_base,
        new_sectors=np.array(done, dtype=object),
        timing_json=json.dumps(tj),
        status=status,
        herm_err_max=float(herm_err_max),
        device=str(device),
        levels=np.array(LEVELS, dtype=np.int64),
        jensen_s=JENSEN_S,
    )
    os.replace(tmp_written, OUT_CACHE)


def main():
    import torch
    from dirac_spectrum import (
        su3_generators, compute_structure_constants, build_cliff8,
        compute_killing_form, jensen_metric, orthonormal_frame,
        frame_structure_constants, connection_coefficients,
        spinor_connection_offset, get_irrep, dirac_operator_on_irrep,
    )

    t_start = time.time()                            # (local)
    device = "cuda:0" if torch.cuda.is_available() else "cpu"   # (local)
    print(f"[env] python={sys.version.split()[0]} torch={torch.__version__} "
          f"device={device} OMP={os.environ.get('OMP_NUM_THREADS')}", flush=True)

    # --- Build the frame / connection ONCE (cheap, shared across all sectors) ---
    gens = su3_generators()                          # (local)
    f_abc = compute_structure_constants(gens)        # (local)
    gammas = build_cliff8()                          # (local)
    B_ab = compute_killing_form(f_abc)               # (local)
    g_s = jensen_metric(B_ab, JENSEN_S)              # (local)
    E = orthonormal_frame(g_s)                       # (local)
    Omega = spinor_connection_offset(
        connection_coefficients(frame_structure_constants(f_abc, E)), gammas
    )                                                # (local)

    done, timing = load_existing()
    herm_err_max = 0.0                               # (local)

    # --- Enumerate all sectors for levels {13,14}; do them in a wall-aware order. ---
    # Order WITHIN a level by build cost proxy: the pure-symmetric extremes (p,0)/(0,p)
    # are the heaviest (Sym^p super-polynomial). Do CHEAPEST first so partial progress
    # accumulates a COMPLETE level-13 set as early as possible, then level-14.
    def cost_proxy(p, q):
        # min(p,q) large => more Casimir-projection tensor work but smaller Sym base;
        # the extreme (p,0)/(0,p) (min=0) is the Sym^p wall. Center sectors are cheaper.
        return -min(p, q)                            # (local) cheaper (large min) first
    plan = []                                        # (local)
    for lvl in LEVELS:
        sectors = [(p, lvl - p) for p in range(lvl + 1)]
        sectors.sort(key=lambda pq: cost_proxy(*pq))
        plan.extend(sectors)

    total = len(plan)                                # (local)
    print(f"[plan] {total} sectors across levels {LEVELS}: "
          f"{[ (p,q) for (p,q) in plan ]}", flush=True)

    for i, (p, q) in enumerate(plan):
        lvl = p + q
        if (p, q) in done:
            continue
        dim_pq = dim_su3(p, q)                        # (local)
        t0 = time.time()                             # (local)
        print(f"[{i+1}/{total}] building ({p},{q}) lvl={lvl} dim={dim_pq} "
              f"Dsize={dim_pq*16} ...", flush=True)
        try:
            rho, dim_check = get_irrep(p, q, gens, f_abc)
            assert dim_check == dim_pq, f"dim mismatch ({p},{q}): {dim_check} != {dim_pq}"
            D = dirac_operator_on_irrep(rho, E, gammas, Omega)        # (local) anti-Hermitian
            Dt = torch.tensor(1j * D, device=device)                 # (local) i*D Hermitian
            herm_err = float(torch.max(torch.abs(
                Dt - Dt.conj().transpose(-2, -1))).cpu())            # (local)
            herm_err_max = max(herm_err_max, herm_err)
            evals = torch.linalg.eigvalsh(Dt).cpu().numpy()          # (local) real eig of i*D
            abs_evals = np.abs(evals).astype(np.float64)             # (local) |lambda|
            del Dt
            if device.startswith("cuda"):
                torch.cuda.empty_cache()
        except Exception as e:
            dt = time.time() - t0                    # (local)
            print(f"    !! FAILED ({p},{q}) after {dt:.1f}s: {e}", flush=True)
            persist(done, timing, status=f"FAILED_at_{p}_{q}",
                    herm_err_max=herm_err_max, device=device)
            raise
        dt = time.time() - t0                        # (local)
        done[(p, q)] = {"dim": dim_pq, "level": lvl, "abs_evals": abs_evals}
        timing[(p, q)] = dt
        persist(done, timing, status="IN_PROGRESS",
                herm_err_max=herm_err_max, device=device)
        print(f"    ({p},{q}) done dim={dim_pq} build+eigvalsh={dt:.1f}s "
              f"|lam|=[{abs_evals.min():.4f},{abs_evals.max():.4f}] "
              f"iD_herm_err={herm_err:.1e} elapsed_total={time.time()-t_start:.1f}s",
              flush=True)

    # --- completeness check: each level fully covered? ---
    have_13 = all((p, 13 - p) in done for p in range(14))           # (local)
    have_14 = all((p, 14 - p) in done for p in range(15))           # (local)
    status = "COMPLETE" if (have_13 and have_14) else (
        "LEVEL13_COMPLETE" if have_13 else "PARTIAL")
    persist(done, timing, status=status, herm_err_max=herm_err_max, device=device)
    print(f"[done] status={status} have_13={have_13} have_14={have_14} "
          f"n_sectors={len(done)} wall={time.time()-t_start:.1f}s "
          f"herm_err_max={herm_err_max:.1e}", flush=True)


if __name__ == "__main__":
    main()
