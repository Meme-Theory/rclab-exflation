#!/usr/bin/env python
"""
S106-W1-HIGHL-CACHE-L1416 — build the L_max=14 and L_max=16 D_K spectrum caches at
                            tau_fold via the GT (p,0) bosonic-ladder builder + Casimir-
                            projection mixed-sector route, with a bit-exact GT-vs-cache
                            VALIDATION GATE on already-cached sectors run FIRST.

Gate: S106-W1-HIGHL-CACHE-L1416  ([VERIFY]; the PASS is the bit-exact GT-vs-cache cross-check
on the already-cached (p+q<=12) sectors + cache-completeness; schema_v2_3tuple_required: false).
Classification: GEOMETRIC.

WHAT THIS GATE DOES
-------------------
Extends the substrate's own squared-action lattice E(p,q)=|lambda(p,q)|^2 at the fixed
tau_fold=0.19 slice (Level-1 single-tau-slice) from p+q<=12 (s84 master cache) to p+q<=14 (L14
cache) and p+q<=16 (L16 cache). The two caches are THE input consumed by 1d (G_E anisotropy
trend, the DECISIVE AXIS) and 1e (length re-match). Both are emitted in ONE npz with two
L_max keys (sector_evals_L14, sector_evals_L16) carrying {dim, level, abs_evals} per (p,q),
the SAME schema as s84_spectrum_cache_L12_tau019.npz.

VALIDATION GATE (run FIRST, the S105 W1 discipline) — the PASS conjunct
-----------------------------------------------------------------------
Before consuming/building ANY new (p+q in {13,14,15,16}) sector, re-build the already-cached
(p,0)/(0,q) sectors present in the s84 master cache (p+q<=12) via the GT bosonic-ladder builder
and assert max|lambda_builder - lambda_cache| < 1e-10. The GT builder reproduces the dense
symmetric-power eigenvalues bit-exact (the sqrt((n_a+1)*n_b) ladder factor; gt-builder-high-L
memory: 'Dirac |lambda| vs s84 cache = 7.5e-14 over 24 (p,0)/(0,q) sectors'). 1e-10 is a
float64 eigendecomposition reproduction floor (well above eps~2.2e-16), NOT a physics threshold.

CACHE ASSEMBLY (PHASE 2)
------------------------
  Reused (already on disk, validated provenance):
    - s84 master cache: all sectors p+q<=12 EXCEPT (4,4) [the one (4,4) gap, dim 125].
    - s104 GT chain cache: 12 mixed level-13 sectors (1,12)..(12,1).
    - s105 resume cache: 4 GT top (13,0)/(0,13)/(14,0)/(0,14) + 13 mixed level-14 (1,13)..(13,1).
  Built NEW (this gate):
    - (4,4): gap-fill, needed for L14 completeness of the p+q<=12 levels [via GT-monkeypatched
      get_irrep Casimir-projection].
    - level 15: (15,0)/(0,15) via GT; 14 mixed (1,14)..(14,1) via Casimir-projection.
    - level 16: (16,0)/(0,16) via GT; 15 mixed (1,15)..(15,1) via Casimir-projection.
  L14 cache = {s84 p+q<=12} U {(4,4)} U {s104 mixed-13} U {s105 top-13} U {s105 mixed-14} U {GT top-14}
            (the GT top-14 (14,0)/(0,14) are in s105 resume; merged from there).
  L16 cache = L14 U {level 15} U {level 16}.

FEASIBILITY (D_K Block-Diagonality + Recursive-Casimir-Projection Pre-Check; math-scripts.md)
---------------------------------------------------------------------------------------------
D_K is BLOCK-DIAGONAL by Peter-Weyl: D_K = (+)_{(p,q)} D_{(p,q)} on V_{(p,q)} (x) C^16. Sparse
storage NOT necessary. Worst single block at L16 is the near-diagonal (8,8):
  dim(8,8) = 9*9*18/2 = 729 -> block 729*16 = 11664 -> dense complex128 = 11664^2*16 = 2.18 GB
  2.18 GB / 17.1 GB = 0.127 -> margin factor 7.85x on the worst block (< 0.5*VRAM = 8.55 GB cap).
Dense per-block GPU diagonalization is feasible throughout. The operative cost is irrep
CONSTRUCTION (Casimir-projection recursion), addressed by the GT-builder monkeypatch (lifts the
3^p Sym^p dense-intermediate wall) + a deterministic resume cache for the expensive sectors.

TWO-TIER FRIEDRICH-BAR DISPOSITION (pre-registered)
---------------------------------------------------
  (i)  full p+q<=16 construction completes -> emit FULL L16 cache (L_max_operational=16).
  (ii) FRIEDRICH-BAR FALLBACK: if the level-15/16 mixed construction binds on time, emit the
       L16 cache as PARTIAL (buildable sectors + Friedrich-Bar lower bounds eta_FB_lower *
       sqrt(C_2(p,q)+1) on the missing deep-mixed sectors) with L_max_operational < 16 disclosed
       in the npz keys + a PARTIAL-FRIEDRICH-BAR scheme-tag suffix. The L14 cache always lands.
       eta_FB(p,q) = |lambda|_min(p,q)/sqrt(C_2(p,q)+1) pinned 8-10% below the L12 empirical floor.

Verdict (PASS / FAIL / INFO):
  PASS  = sentinel max|d lambda| < 1e-10 on already-cached sectors AND both L14 & L16 caches
          written with valid sector_evals schema (FULL or PARTIAL-with-FB-bounds + L_max_op disclosed).
  FAIL  = sentinel >= 1e-10 (builder does not reproduce validated L12 spectrum) -> 1d/1e close
          PRE-REG-INC blocked_by this FAIL.
  INFO  = construction obstruction: NEITHER full L16 nor the FB PARTIAL completes for the sectors
          1d needs (L14 still lands; 1d/1e run as a 2-point {12,14} trend, L16 deferred).

regulator_pin: a_n citations N/A here (the cache stores |lambda| eigenvalues directly; no
Seeley-DeWitt moment is formed in this gate — the moments are formed downstream by 1d/1e).

Substrate-first arrow: build per-sector D_K(p,q) blocks (Jensen block-split L1=e^{2tau},
L2=e^{-2tau}, L3=e^{tau} at tau_fold) -> GPU eigvalsh(i*D) -> squared-action lattice at L14/L16
-> feed the decisive anisotropy trend (1d) and the length re-match (1e). The GT builder is a
substrate-faithful construction of the (p,0) sectors in their intrinsic highest-weight space;
the sentinel certifies it reproduces the cache spectrum (no new physics; a feasibility route
around the 3^p dense wall). This is the fabric ITSELF at finer truncation, not a measurement
in a container.

INPUT-PATH FIX (substrate-first-canonical-sourcing.md §(ii.B), per the batch-1 gates):
  the L12 cache lives at computations/session-84/s84_spectrum_cache_L12_tau019.npz, NOT the
  plan-pinned computations/_shared/ path. Resolved to the session-84 path; the drift is recorded
  as cache_path_drift in the verdict value + npz keys.
"""
from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
import time
from itertools import combinations_with_replacement
from math import sqrt
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# Section 1 — Identity + paths
# ---------------------------------------------------------------------------
SESSION = "S106"
GATE_ID = "S106-W1-HIGHL-CACHE-L1416"
SCHEME_BASE = "GT-BOSONIC-LADDER+CASIMIR-PROJECTION-MIXED"
CONVENTION = "JENSEN-BLOCK-SPLIT-L1=e^{2tau}-L2=e^{-2tau}-L3=e^{tau}"

THIS_FILE = Path(__file__).resolve()
PROJECT_ROOT = THIS_FILE.parents[2]                  # .../computations/session-106/<this> -> root
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
SESSION_DIR = PROJECT_ROOT / "computations" / "session-106"

sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import (  # noqa: E402
    tau_fold,
)

# ---------------------------------------------------------------------------
# Section 2 — Pre-registered constants (plan §W1-3)
# ---------------------------------------------------------------------------
SENTINEL_TOL = 1e-10                      # (local) bit-exact GT-vs-cache |lambda| cross-check floor (plan strict_PASS_boundary)
ETA_FB_SAFETY = 0.90                      # (local) eta_FB_lower pinned 10% below the L12 empirical floor (plan: 8-10%)
PUBLICATION_PRECISION = 12               # (local) eigenvalues stored full float64; cross-check reported to 12 sig figs
L_MAX_PLAN = (14, 16)                    # (local) the two target truncations
# Wall-clock budget for the NEW level-15/16 mixed construction; if exceeded mid-build, switch to
# the Friedrich-Bar PARTIAL disposition (ii). Generous; the worst (8,8) block is ~ few s clean.
NEW_BUILD_TIME_BUDGET_S = 1800.0         # (local) 30 min soft budget for level-15/16 mixed-sector construction
ID_HERM_ERR_TOL_IDEAL = 1.0e-15          # (local) ideal exact-Hermitian floor (S104/S105 pin)
EPS_F64 = float(np.finfo(np.float64).eps)  # (local) ~2.22e-16

JENSEN_S = float(tau_fold)               # (local) Jensen deformation parameter s = tau_fold = 0.190 (cache is tau019)

# ---------------------------------------------------------------------------
# Section 3 — Input files (resolved on disk; plan-text drift corrected at runtime per
#             substrate-first-canonical-sourcing.md §(ii.B))
# ---------------------------------------------------------------------------
P_CANONICAL = SHARED_DIR / "canonical_constants.py"
# plan-pinned path is computations/_shared/s84_...; the file actually lives in session-84:
P_CACHE_PLAN = SHARED_DIR / "s84_spectrum_cache_L12_tau019.npz"
P_CACHE = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
CACHE_PATH_DRIFT = (not P_CACHE_PLAN.exists()) and P_CACHE.exists()  # (local) batch-1-verified drift
P_DIRAC = SHARED_DIR / "dirac_spectrum.py"
P_S104 = PROJECT_ROOT / "computations" / "session-104" / "s104_sym_p_chain_cache_L1314.npz"
P_S105_RESUME = PROJECT_ROOT / "computations" / "session-105" / "s105_branch_iv_l1314_sectors_resume.npz"

INPUT_FILES = [P_CANONICAL, P_CACHE, P_S104, P_S105_RESUME, P_DIRAC]

# Resume cache for THIS gate's expensive new sectors ((4,4) + level 15 + level 16)
P_RESUME = SESSION_DIR / "s106_w1_highl_new_sectors_resume.npz"

# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                   # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}                              # (local)
    for p in inputs:
        sha = sha256_of(p)                                 # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p).replace("\\", "/")                # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())                           # (local)
    h = hashlib.sha256()                                   # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict[str, str]) -> tuple[str, str]:
    try:
        script_bytes = script_path.read_bytes()            # (local)
    except OSError:
        script_bytes = b""                                 # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()      # (local)
    except OSError:
        canonical_bytes = b""                              # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")                                      # (local)
    h_audit = hashlib.sha256()                             # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()                           # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5a — Gelfand-Tsetlin / bosonic-ladder (p,0)=Sym^p(C^3) DIRECT builder
#              (verbatim from s105_branch_iv_direct_l1314.py — bit-exact vs the dense
#               symmetric-power builder; gt-builder-high-L memory)
# ---------------------------------------------------------------------------

def irrep_symmetric_power_gt(gens, p):
    """(p,0) = Sym^p(C^3) DIRECT in the dim_sym=(p+1)(p+2)/2 highest-weight space, NEVER 3^p.

    rho(X) = sum_{a,b} X[a,b] a_a^dag a_b on the occupation basis |n>=|n0,n1,n2>, sum n = p:
        diagonal  (a==b):  <n|rho(X)|n> += sum_a X[a,a] * n_a
        off-diag  (a!=b):  n' = n - u_b + u_a,  <n'|rho(X)|n> += X[a,b] * sqrt((n_a+1)*n_b)
    ON occupation basis ordered by combinations_with_replacement(range(3), p) -> matches
    dirac_spectrum.irrep_symmetric_power exactly (rho matrices coincide bit-for-bit). Build (0,p)
    by passing conjugated generators [-g.T for g in gens].
    """
    sorted_tuples = list(combinations_with_replacement(range(3), p))  # (local) SAME order as dense builder
    occs = [(t.count(0), t.count(1), t.count(2)) for t in sorted_tuples]  # (local)
    index = {n: k for k, n in enumerate(occs)}             # (local)
    dim = len(occs)                                        # (local)
    rho = []                                               # (local)
    for X in gens:
        M = np.zeros((dim, dim), dtype=complex)            # (local)
        for n in occs:
            kn = index[n]
            M[kn, kn] += X[0, 0] * n[0] + X[1, 1] * n[1] + X[2, 2] * n[2]
            for b in range(3):
                nb = n[b]
                if nb == 0:
                    continue
                for a in range(3):
                    if a == b:
                        continue
                    xab = X[a, b]
                    if xab == 0:
                        continue
                    npr = list(n)
                    npr[b] -= 1
                    npr[a] += 1
                    npr = tuple(npr)
                    M[index[npr], kn] += xab * sqrt((n[a] + 1) * nb)
        rho.append(M)
    return rho


# ---------------------------------------------------------------------------
# Section 5b — Casimir C_2(p,q) (SU(3) quadratic Casimir; gt-builder/spectral-geometer memory)
# ---------------------------------------------------------------------------

def casimir_pq(p, q):
    """C_2(p,q) = (p^2 + q^2 + p*q + 3p + 3q)/3 (SU(3) quadratic Casimir)."""
    return (p * p + q * q + p * q + 3 * p + 3 * q) / 3.0


# ---------------------------------------------------------------------------
# Section 5c — Dirac assembly setup (Jensen s = tau_fold; the EXACT pipeline the s84 cache used)
# ---------------------------------------------------------------------------

def build_dirac_pipeline():
    """Returns (gens, f_abc, device, dirac_abs_and_herr). Monkeypatches the GT bosonic-ladder
    builder for the wall-bound dense symmetric-power constructor so the Casimir-projection
    recursion builds Sym^p parents wall-free."""
    import torch
    import dirac_spectrum as ds
    from dirac_spectrum import (
        su3_generators, compute_structure_constants, build_cliff8,
        compute_killing_form, jensen_metric, orthonormal_frame,
        frame_structure_constants, connection_coefficients,
        spinor_connection_offset, dirac_operator_on_irrep,
    )
    ds.irrep_symmetric_power = irrep_symmetric_power_gt  # monkeypatch — math-identical, wall-free

    gens = su3_generators()                                # (local)
    f_abc = compute_structure_constants(gens)              # (local)
    gammas = build_cliff8()                                # (local)
    B_ab = compute_killing_form(f_abc)                     # (local)
    g_s = jensen_metric(B_ab, JENSEN_S)                    # (local)
    E = orthonormal_frame(g_s)                             # (local)
    Omega = spinor_connection_offset(
        connection_coefficients(frame_structure_constants(f_abc, E)), gammas
    )                                                      # (local)
    device = "cuda:0" if torch.cuda.is_available() else "cpu"  # (local)

    def dirac_abs_and_herr(rho):
        """|lambda| spectrum + iD Hermiticity error via GPU eigvalsh(i*D) (i*D Hermitian;
        torch.linalg.eigvals general-eig needs MAGMA, absent on ROCm)."""
        D = dirac_operator_on_irrep(rho, E, gammas, Omega)  # (local) anti-Hermitian
        Dt = torch.tensor(1j * D, device=device)           # (local) i*D Hermitian
        herr = float(torch.max(torch.abs(Dt - Dt.conj().transpose(-2, -1))).cpu())  # (local)
        evals = torch.linalg.eigvalsh(Dt).cpu().numpy()    # (local)
        return np.abs(evals).astype(np.float64), herr

    return gens, f_abc, device, dirac_abs_and_herr


# ---------------------------------------------------------------------------
# Section 6 — print_verdict_payload (agent calls emit_verdict with this)
# ---------------------------------------------------------------------------

def print_verdict_payload(verdict, value, scheme, audit_sha, content_sha, extra_rows=None):
    payload = {
        "session": 106,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": value,
        "scheme": scheme,
        "convention": CONVENTION,
        "l_max": "[14,16]",
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if extra_rows:
        payload["extra_rows"] = extra_rows
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")


def dim_pq(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2


# ---------------------------------------------------------------------------
# Section 7 — main
# ---------------------------------------------------------------------------

def main():
    print(f"=== {GATE_ID} :: build L14 & L16 D_K spectrum caches @ tau_fold via GT + Casimir ===")
    print(f"[const] tau_fold={tau_fold}  Jensen_s={JENSEN_S}  sentinel_tol={SENTINEL_TOL:.0e}")
    if CACHE_PATH_DRIFT:
        print(f"[drift] cache plan-pin {P_CACHE_PLAN} ABSENT; resolved to {P_CACHE} "
              f"(substrate-first-canonical-sourcing.md §(ii.B))")
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    audit_sha, content_sha = compute_dual_sha(THIS_FILE, P_CANONICAL, pins)
    print(f"  closure_hash:   {closure[:16]}...")
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    # --- Load s84 L<=12 master cache ---
    cache = np.load(P_CACHE, allow_pickle=True)
    s84 = cache["sector_evals"].item()                     # (local) {(p,q): {dim,level,abs_evals}}
    cache.close()
    n_s84 = len(s84)                                        # (local)
    s84_max_level = max(d["level"] for d in s84.values())  # (local)
    print(f"[cache] s84 master: {n_s84} sectors, max_level={s84_max_level}")

    # --- Build the Dirac pipeline (GT builder monkeypatched into get_irrep recursion) ---
    gens, f_abc, device, dirac_abs_and_herr = build_dirac_pipeline()
    conj_gens = [-g.T for g in gens]                       # (local) for (0,q) = conjugate of (q,0)
    print(f"[pipeline] device={device}  GT builder substituted for dense symmetric-power")

    # =====================================================================
    # PHASE 1 — VALIDATION GATE: bit-exact GT-vs-cache sentinel on cached (p,0)/(0,q) p+q<=12
    #           (MANDATORY, run FIRST; no new-sector consumption before it PASSes)
    # =====================================================================
    print("  --- PHASE 1 (VALIDATION GATE): GT-vs-cache bit-exact sentinel on cached "
          "(p,0)/(0,q) p+q<=12 ---")
    sentinel_max = 0.0                                     # (local)
    sentinel_detail = {}                                   # (local)
    t_phase1 = time.time()                                 # (local)
    cached_p0 = sorted([k for k in s84 if (k[1] == 0 and k[0] >= 1)])  # (local) (1,0)..(12,0)
    cached_0q = sorted([k for k in s84 if (k[0] == 0 and k[1] >= 1)])  # (local) (0,1)..(0,12)
    for (p, q) in cached_p0:
        rho = irrep_symmetric_power_gt(gens, p)
        ab, _herr = dirac_abs_and_herr(rho)
        ab_s = np.sort(ab)                                 # (local)
        cache_s = np.sort(np.asarray(s84[(p, q)]["abs_evals"], dtype=np.float64))  # (local)
        d = float(np.max(np.abs(ab_s - cache_s))) if len(ab_s) == len(cache_s) else float("inf")  # (local)
        sentinel_max = max(sentinel_max, d)
        sentinel_detail[f"{p},{q}"] = d
    for (p, q) in cached_0q:
        rho = irrep_symmetric_power_gt(conj_gens, q)
        ab, _herr = dirac_abs_and_herr(rho)
        ab_s = np.sort(ab)                                 # (local)
        cache_s = np.sort(np.asarray(s84[(p, q)]["abs_evals"], dtype=np.float64))  # (local)
        d = float(np.max(np.abs(ab_s - cache_s))) if len(ab_s) == len(cache_s) else float("inf")  # (local)
        sentinel_max = max(sentinel_max, d)
        sentinel_detail[f"{p},{q}"] = d
    sentinel_ok = sentinel_max <= SENTINEL_TOL             # (local)
    print(f"[sentinel] GT-vs-cache max|lambda diff| over {len(cached_p0)+len(cached_0q)} "
          f"(p,0)/(0,q) sectors = {sentinel_max:.3e}  ok(< {SENTINEL_TOL:.0e})={sentinel_ok} "
          f"({time.time()-t_phase1:.1f}s)")

    if not sentinel_ok:
        # GATING: do NOT consume/build new sectors if the GT builder fails to reproduce the cache.
        value = (f"FAIL_GT_sentinel_max={sentinel_max:.3e}_>=_tol{SENTINEL_TOL:.0e}; "
                 f"GT_builder_does_not_reproduce_L12_cache_spectrum; no_new_sector_consumption; "
                 f"1d_1e_close_PRE-REG-INC_blocked_by_this_FAIL")
        np.savez_compressed(
            SESSION_DIR / "s106_w1_highl_cache_l1416.npz",
            verdict="FAIL", phase="PHASE1_SENTINEL_FAIL",
            sentinel_max=sentinel_max, SENTINEL_TOL=SENTINEL_TOL,
            sentinel_detail_json=json.dumps(sentinel_detail),
            tau_fold=float(tau_fold), jensen_s=JENSEN_S,
            cache_path_drift=bool(CACHE_PATH_DRIFT),
            audit_sha256=audit_sha, content_sha256=content_sha, closure_hash=closure,
        )
        _make_plot_fail(sentinel_detail, sentinel_max)
        print_verdict_payload("FAIL", value, SCHEME_BASE + "-SENTINEL-FAIL", audit_sha, content_sha)
        return

    # =====================================================================
    # PHASE 2a — load already-built reused sectors (s104 mixed-13, s105 top+mixed-14)
    # =====================================================================
    z104 = np.load(P_S104, allow_pickle=True)
    s104_mixed13 = z104["new_sectors"].item()              # (local) 12 mixed level-13
    z104.close()
    have_mixed13 = all((p, 13 - p) in s104_mixed13 for p in range(1, 13))  # (local)
    print(f"[s104] mixed-13: {len(s104_mixed13)} sectors complete(1..12,12..1)={have_mixed13}")

    z105 = np.load(P_S105_RESUME, allow_pickle=True)
    s105_top = z105["new_top"].item()                      # (local) (13,0)/(0,13)/(14,0)/(0,14)
    s105_mixed14 = z105["new_mixed14"].item()              # (local) 13 mixed level-14
    s105_top_herr = float(z105["top_herr_max"])            # (local)
    s105_mixed_herr = float(z105["mixed_herr_max"])        # (local)
    z105.close()
    have_top1314 = all(k in s105_top for k in [(13, 0), (0, 13), (14, 0), (0, 14)])  # (local)
    have_mixed14 = all((p, 14 - p) in s105_mixed14 for p in range(1, 14))            # (local)
    print(f"[s105] resume: top={len(s105_top)} (complete={have_top1314}) mixed14="
          f"{len(s105_mixed14)} (complete={have_mixed14}) "
          f"top_herr={s105_top_herr:.2e} mixed_herr={s105_mixed_herr:.2e}")

    # =====================================================================
    # PHASE 2b — build the NEW sectors: (4,4) gap-fill + level 15 + level 16
    #            (deterministic; resume-cached so re-runs are fast)
    # =====================================================================
    new_sectors = {}                                       # (local) ALL freshly-built sectors this gate
    build_herr_max = 0.0                                   # (local)
    build_times = {}                                       # (local)
    new_resume_loaded = False                              # (local)
    construction_complete = True                           # (local) tier-(i) flag
    t_newbuild = time.time()                               # (local)

    # The full target set of NEW sectors:
    target_44 = [(4, 4)]
    target_l15 = [(p, 15 - p) for p in range(0, 16)]       # (0,15)..(15,0)
    target_l16 = [(p, 16 - p) for p in range(0, 17)]       # (0,16)..(16,0)
    target_new = target_44 + target_l15 + target_l16
    print(f"[newbuild] target NEW sectors: (4,4) + level15 ({len(target_l15)}) + level16 "
          f"({len(target_l16)}) = {len(target_new)} total")

    # Try resume cache first (deterministic substrate spectra)
    if P_RESUME.exists():
        zr = np.load(P_RESUME, allow_pickle=True)
        loaded = zr["new_sectors"].item()                  # (local)
        build_herr_max = float(zr["build_herr_max"])
        zr.close()
        have_all = all(k in loaded for k in target_new)    # (local)
        if have_all:
            new_sectors = loaded
            new_resume_loaded = True
            print(f"[resume] loaded ALL {len(new_sectors)} new sectors from {P_RESUME.name} "
                  f"(build_herr={build_herr_max:.2e})")
        else:
            new_sectors = dict(loaded)                      # partial resume; build the rest below
            missing = [k for k in target_new if k not in loaded]  # (local)
            print(f"[resume] partial: {len(loaded)} loaded, {len(missing)} still to build")

    if not new_resume_loaded:
        from dirac_spectrum import get_irrep, _irrep_cache

        def build_one(p, q, level):
            """Build a single (p,q) sector via GT (pure-symmetric) or Casimir-projection (mixed)."""
            nonlocal build_herr_max
            t0 = time.time()                               # (local)
            d_pq = dim_pq(p, q)                             # (local)
            if q == 0:
                rho = irrep_symmetric_power_gt(gens, p)
            elif p == 0:
                rho = irrep_symmetric_power_gt(conj_gens, q)
            else:
                _irrep_cache.clear()                        # bound memory + avoid cross-sector contamination
                rho, dim_check = get_irrep(p, q, gens, f_abc)
                assert dim_check == d_pq, f"({p},{q}) dim {dim_check} != {d_pq}"
            assert rho[0].shape[0] == d_pq, f"({p},{q}) rho dim {rho[0].shape[0]} != {d_pq}"
            ab, herr = dirac_abs_and_herr(rho)
            build_herr_max = max(build_herr_max, herr)
            dt = time.time() - t0                          # (local)
            build_times[f"{p},{q}"] = dt
            return {"dim": d_pq, "level": level, "abs_evals": ab}, herr, dt

        # (4,4) gap-fill (level 8) — small (dim 125), always build first
        for (p, q) in target_44:
            if (p, q) in new_sectors:
                continue
            rec, herr, dt = build_one(p, q, p + q)
            new_sectors[(p, q)] = rec
            print(f"    ({p},{q}) [gap-fill]: dim={rec['dim']} D={rec['dim']*16} "
                  f"|lam|=[{rec['abs_evals'].min():.4f},{rec['abs_evals'].max():.4f}] "
                  f"herr={herr:.1e} ({dt:.1f}s)")

        # level 15 then level 16 — build (p,0)/(0,p) GT first (cheap), then mixed by descending
        # closeness to the diagonal (worst (p~q) last so a time-bind leaves the buildable subset).
        for level, targets in [(15, target_l15), (16, target_l16)]:
            # order: pure-symmetric first, then mixed ordered by |p-q| descending (skinniest first)
            pure = [(p, q) for (p, q) in targets if p == 0 or q == 0]
            mixed = [(p, q) for (p, q) in targets if p > 0 and q > 0]
            mixed_sorted = sorted(mixed, key=lambda pq: -abs(pq[0] - pq[1]))  # skinniest first
            print(f"  --- PHASE 2b: building level {level} "
                  f"({len(pure)} GT pure + {len(mixed_sorted)} Casimir mixed) ---")
            for (p, q) in pure + mixed_sorted:
                if (p, q) in new_sectors:
                    continue
                if (time.time() - t_newbuild) > NEW_BUILD_TIME_BUDGET_S:
                    construction_complete = False
                    print(f"  [time-budget] {NEW_BUILD_TIME_BUDGET_S:.0f}s exceeded at ({p},{q}); "
                          f"switching to Friedrich-Bar PARTIAL disposition (ii)")
                    break
                rec, herr, dt = build_one(p, q, level)
                new_sectors[(p, q)] = rec
                tag = "GT" if (p == 0 or q == 0) else "Casimir"
                print(f"    ({p},{q}) [{tag}]: dim={rec['dim']} D={rec['dim']*16} "
                      f"|lam|=[{rec['abs_evals'].min():.4f},{rec['abs_evals'].max():.4f}] "
                      f"herr={herr:.1e} ({dt:.1f}s)")
            if not construction_complete:
                break

        # persist the resume cache (deterministic substrate spectra)
        np.savez_compressed(
            P_RESUME, new_sectors=np.array(new_sectors, dtype=object),
            build_herr_max=build_herr_max,
            build_times_json=json.dumps(build_times),
            construction_complete=bool(construction_complete),
        )
        print(f"[resume] saved {len(new_sectors)} new sectors to {P_RESUME.name} "
              f"(build_herr={build_herr_max:.2e}, complete={construction_complete}, "
              f"{time.time()-t_newbuild:.1f}s)")

    # Dimension-scaled Hermiticity floor (boson (p,0) i*D exactly Hermitian; Casimir-assembled
    # blocks carry FP-noise residual ~ sqrt(D)*eps; gt-builder-high-L memory)
    all_built_dims = [d["dim"] * 16 for d in new_sectors.values()] + [1]  # (local)
    dmax_block = max(all_built_dims)                       # (local)
    ID_HERM_ERR_TOL = max(ID_HERM_ERR_TOL_IDEAL, np.sqrt(dmax_block) * EPS_F64)  # (local)
    herm_err_max = max(build_herr_max, s105_top_herr, s105_mixed_herr)  # (local)
    print(f"[herm-guard] D_max_block={dmax_block} -> floor=max(1e-15, sqrt(D)*eps)="
          f"{ID_HERM_ERR_TOL:.2e}  herm_err_max={herm_err_max:.2e} "
          f"(<= : {herm_err_max <= ID_HERM_ERR_TOL})")

    # =====================================================================
    # PHASE 2c — cross-check: conjugate-pair symmetry |lambda(p,q)| == |lambda(q,p)| (CPT pairing)
    #            on the NEW sectors (independent self-consistency for the un-cached sectors)
    # =====================================================================
    conj_pair_max = 0.0                                    # (local)
    conj_pairs_checked = 0                                 # (local)
    for (p, q) in new_sectors:
        if (q, p) in new_sectors and (p, q) <= (q, p) and p != q:
            a = np.sort(np.asarray(new_sectors[(p, q)]["abs_evals"], dtype=np.float64))   # (local)
            b = np.sort(np.asarray(new_sectors[(q, p)]["abs_evals"], dtype=np.float64))   # (local)
            d = float(np.max(np.abs(a - b))) if len(a) == len(b) else float("inf")        # (local)
            conj_pair_max = max(conj_pair_max, d)
            conj_pairs_checked += 1
    print(f"[xcheck-conj] |lambda(p,q)|==|lambda(q,p)| over {conj_pairs_checked} NEW conjugate "
          f"pairs: max|diff|={conj_pair_max:.3e}")

    # =====================================================================
    # PHASE 3 — assemble L14 and L16 caches; Friedrich-Bar PARTIAL if construction binds
    # =====================================================================
    # eta_FB empirical floor on the L12 master cache (per-sector |lambda|_min / sqrt(C_2+1))
    eta_FB_vals = []                                       # (local)
    for (p, q), data in s84.items():
        if p == 0 and q == 0:
            continue
        lam_min = float(np.min(data["abs_evals"]))         # (local)
        eta_FB_vals.append(lam_min / sqrt(casimir_pq(p, q) + 1.0))
    eta_FB_floor = float(np.min(eta_FB_vals))              # (local)
    eta_FB_lower = ETA_FB_SAFETY * eta_FB_floor            # (local) 10% below floor
    print(f"[FB] eta_FB empirical floor on L12 = {eta_FB_floor:.6f}; "
          f"eta_FB_lower (10% below) = {eta_FB_lower:.6f}")

    # L14 cache: s84 (p+q<=12) U (4,4) U s104-mixed13 U s105-top(13/14) U s105-mixed14
    sector_evals_L14 = dict(s84)                           # (local)
    if (4, 4) in new_sectors:
        sector_evals_L14[(4, 4)] = new_sectors[(4, 4)]
    sector_evals_L14.update(s104_mixed13)                 # 12 mixed level-13
    for k in [(13, 0), (0, 13), (14, 0), (0, 14)]:
        sector_evals_L14[k] = s105_top[k]
    sector_evals_L14.update(s105_mixed14)                 # 13 mixed level-14
    # completeness check for L14 (all p+q<=14 present)
    full14 = set((p, L - p) for L in range(15) for p in range(L + 1))  # (local)
    missing_L14 = sorted(full14 - set(sector_evals_L14.keys()))        # (local)
    L14_complete = len(missing_L14) == 0                              # (local)
    L14_max_level = max(d["level"] for d in sector_evals_L14.values())  # (local)
    print(f"[L14] sectors={len(sector_evals_L14)} (full triangle={len(full14)}) "
          f"complete={L14_complete} max_level={L14_max_level} missing={missing_L14}")

    # L16 cache: L14 U level15 U level16 (FULL or PARTIAL-with-FB-bounds)
    sector_evals_L16 = dict(sector_evals_L14)             # (local)
    fb_bounded_sectors = {}                                # (local) Friedrich-Bar lower-bounded fills
    for (p, q) in target_l15 + target_l16:
        if (p, q) in new_sectors:
            sector_evals_L16[(p, q)] = new_sectors[(p, q)]
        else:
            # Friedrich-Bar lower bound on the missing deep-mixed sector (tier-(ii) fallback)
            lam_lower = eta_FB_lower * sqrt(casimir_pq(p, q) + 1.0)  # (local)
            fb_bounded_sectors[(p, q)] = {
                "dim": dim_pq(p, q), "level": p + q,
                "lambda_lower_bound": lam_lower, "fb_bounded": True,
            }
    full16 = set((p, L - p) for L in range(17) for p in range(L + 1))  # (local)
    built_L16 = set(sector_evals_L16.keys())                          # (local)
    missing_built_L16 = sorted(full16 - built_L16)                    # (local) FB-bounded only
    L16_full = len(missing_built_L16) == 0                            # (local) tier-(i) achieved
    n_fb = len(fb_bounded_sectors)                                    # (local)
    L16_max_level = max(d["level"] for d in sector_evals_L16.values())  # (local)
    print(f"[L16] explicit sectors={len(sector_evals_L16)} (full triangle={len(full16)}) "
          f"FB-bounded={n_fb} FULL={L16_full} max_level={L16_max_level}")

    # L_max_operational disclosure:
    #   L14: operational = 14 iff L14_complete else max contiguous level
    #   L16: operational = 16 iff L16_full else the deepest fully-explicit level
    if L14_complete:
        L14_operational = 14                              # (local)
    else:
        # deepest level with all sectors explicit
        L14_operational = _deepest_complete_level(sector_evals_L14, 14)  # (local)
    if L16_full:
        L16_operational = 16                              # (local)
    else:
        L16_operational = _deepest_complete_level(sector_evals_L16, 16)  # (local)
    L14_trunc_consistent = (L14_operational == 14)        # (local)
    L16_trunc_consistent = (L16_operational == 16)        # (local)
    print(f"[L_max_op] L14_operational={L14_operational} (truncation_consistent={L14_trunc_consistent}) "
          f"L16_operational={L16_operational} (truncation_consistent={L16_trunc_consistent})")

    # ---- Disposition / scheme tag ----
    partial = (n_fb > 0) or (not construction_complete) or (not L16_full)  # (local)
    scheme = SCHEME_BASE + ("-PARTIAL-FRIEDRICH-BAR" if partial else "")    # (local)

    # ---- Verdict ----
    # PASS  = sentinel < 1e-10 AND both L14 & L16 caches written with valid schema
    #         (FULL or PARTIAL-with-FB-bounds + L_max_operational disclosed)
    # FAIL  = sentinel failed (handled in PHASE 1)
    # INFO  = NEITHER full L16 nor FB-PARTIAL completes for what 1d needs (L14 still landed)
    schema_ok = (len(sector_evals_L14) > 0 and len(sector_evals_L16) > 0
                 and all("abs_evals" in v for v in sector_evals_L14.values())
                 and all(("abs_evals" in v or "fb_bounded" in v)
                         for v in {**sector_evals_L16, **fb_bounded_sectors}.values()))  # (local)
    herm_ok = herm_err_max <= ID_HERM_ERR_TOL             # (local)

    # 1d needs the high-(p,q) G_E representatives at L16. If FB-bounding is so heavy that NO
    # explicit level-15/16 sector landed, the L16 G_E point is undetermined -> INFO (L14 still lands).
    l15_l16_explicit = sum(1 for k in new_sectors if (k[0] + k[1]) in (15, 16))  # (local)
    l16_determinable = l15_l16_explicit > 0 and L16_operational >= 15           # (local)

    if not (sentinel_ok and schema_ok):
        verdict = "FAIL"
    elif L14_complete and (L16_full or l16_determinable):
        verdict = "PASS"
    else:
        verdict = "INFO"
    if verdict == "PASS" and not herm_ok:
        verdict = "INFO"
        print("[WARN] Hermiticity guard failed -> PASS downgraded to INFO")

    print(f"[VERDICT] sentinel={sentinel_max:.3e}(<{SENTINEL_TOL:.0e}:{sentinel_ok}) "
          f"L14_complete={L14_complete} L16_full={L16_full} l16_determinable={l16_determinable} "
          f"herm_ok={herm_ok} partial={partial} => {verdict}")

    # =====================================================================
    # Persist THE cache npz (both L14 and L16 sector_evals, two L_max keys)
    # =====================================================================
    np.savez_compressed(
        SESSION_DIR / "s106_w1_highl_cache_l1416.npz",
        # --- THE caches (consumed by 1d/1e) ---
        sector_evals_L14=np.array(sector_evals_L14, dtype=object),
        sector_evals_L16=np.array(sector_evals_L16, dtype=object),
        fb_bounded_sectors=np.array(fb_bounded_sectors, dtype=object),
        # --- L_max keys (plan: L_max_operational + truncation_consistent) ---
        L_max_plan=np.array(L_MAX_PLAN, dtype=np.int64),
        L14_operational=int(L14_operational), L16_operational=int(L16_operational),
        L14_truncation_consistent=bool(L14_trunc_consistent),
        L16_truncation_consistent=bool(L16_trunc_consistent),
        L14_complete=bool(L14_complete), L16_full=bool(L16_full),
        n_sectors_L14=len(sector_evals_L14), n_sectors_L16=len(sector_evals_L16),
        n_fb_bounded=int(n_fb), construction_complete=bool(construction_complete),
        # --- VALIDATION GATE (sentinel) ---
        verdict=verdict, phase="PHASE3_COMPLETE",
        sentinel_max=sentinel_max, sentinel_ok=bool(sentinel_ok), SENTINEL_TOL=SENTINEL_TOL,
        sentinel_detail_json=json.dumps(sentinel_detail),
        # --- cross-checks ---
        conj_pair_max=conj_pair_max, conj_pairs_checked=int(conj_pairs_checked),
        herm_err_max=herm_err_max, ID_HERM_ERR_TOL=ID_HERM_ERR_TOL, herm_ok=bool(herm_ok),
        build_herr_max=build_herr_max, s105_top_herr=s105_top_herr, s105_mixed_herr=s105_mixed_herr,
        dmax_block=int(dmax_block),
        # --- Friedrich-Bar ---
        eta_FB_floor=eta_FB_floor, eta_FB_lower=eta_FB_lower, ETA_FB_SAFETY=ETA_FB_SAFETY,
        # --- provenance / inputs ---
        have_mixed13=bool(have_mixed13), have_top1314=bool(have_top1314),
        have_mixed14=bool(have_mixed14),
        n_new_sectors=len(new_sectors), n_s84=n_s84,
        missing_L14_json=json.dumps([list(k) for k in missing_L14]),
        missing_built_L16_json=json.dumps([list(k) for k in missing_built_L16]),
        cache_path_drift=bool(CACHE_PATH_DRIFT),
        cache_path_used=str(P_CACHE), cache_path_plan=str(P_CACHE_PLAN),
        tau_fold=float(tau_fold), jensen_s=JENSEN_S, device=str(device),
        build_times_json=json.dumps(build_times),
        audit_sha256=audit_sha, content_sha256=content_sha, closure_hash=closure,
    )
    print(f"[npz] wrote s106_w1_highl_cache_l1416.npz "
          f"(L14={len(sector_evals_L14)} sectors, L16={len(sector_evals_L16)} explicit "
          f"+ {n_fb} FB-bounded)")

    _make_plot(sector_evals_L14, sector_evals_L16, fb_bounded_sectors, sentinel_detail,
               sentinel_max, verdict, L14_operational, L16_operational)

    # ---- verdict value + extra rows ----
    value = (f"L14_sectors={len(sector_evals_L14)}(complete={L14_complete}) "
             f"L16_sectors={len(sector_evals_L16)}_explicit+{n_fb}_FB(full={L16_full}) "
             f"sentinel={sentinel_max:.3e}<{SENTINEL_TOL:.0e} conj_pair={conj_pair_max:.3e} "
             f"herr={herm_err_max:.2e} L14_op={L14_operational} L16_op={L16_operational} "
             f"cache_path_drift={CACHE_PATH_DRIFT}")
    extra_rows = [
        (f"# GT(p,0)-bosonic-ladder-builder + Casimir-projection-mixed; "
         f"VALIDATION-GATE sentinel(GT-vs-cache)={sentinel_max:.3e} < {SENTINEL_TOL:.0e} on "
         f"{len(cached_p0)+len(cached_0q)} cached (p,0)/(0,q) p+q<=12 sectors; "
         f"conj-pair |lam(p,q)|==|lam(q,p)| max={conj_pair_max:.3e} over {conj_pairs_checked} NEW pairs; "
         f"herm_err_max={herm_err_max:.2e} <= floor {ID_HERM_ERR_TOL:.2e}"),
        (f"# cache_path_drift={CACHE_PATH_DRIFT}: plan-pin computations/_shared/ ABSENT, resolved to "
         f"computations/session-84/s84_spectrum_cache_L12_tau019.npz "
         f"(substrate-first-canonical-sourcing.md §(ii.B)); "
         f"L_max_operational: L14={L14_operational}(consistent={L14_trunc_consistent}) "
         f"L16={L16_operational}(consistent={L16_trunc_consistent}); "
         f"disposition={'FULL-(i)' if not partial else 'PARTIAL-FRIEDRICH-BAR-(ii)'}"),
    ]
    print_verdict_payload(verdict, value, scheme, audit_sha, content_sha, extra_rows=extra_rows)


def _deepest_complete_level(sector_evals, L_target):
    """Deepest contiguous level L for which all p+q=L sectors are explicit in sector_evals."""
    present = set(sector_evals.keys())                     # (local)
    for L in range(L_target, -1, -1):
        full_L = set((p, L - p) for p in range(L + 1))     # (local)
        if full_L.issubset(present):
            return L
    return 0


def _make_plot(se_L14, se_L16, fb_bounded, sentinel_detail, sentinel_max, verdict,
               L14_op, L16_op):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

    # Left: sector count vs level (L14 vs L16) — the cache-completeness diagnostic
    from collections import Counter
    lvl_L14 = Counter(d["level"] for d in se_L14.values())
    lvl_L16 = Counter(d["level"] for d in se_L16.values())
    lvl_fb = Counter(d["level"] for d in fb_bounded.values())
    Ls = sorted(set(lvl_L16) | set(lvl_fb))
    expected = [L + 1 for L in Ls]                          # full triangle count per level
    ax1.plot(Ls, expected, "k--", lw=1, label="full triangle (L+1)")
    ax1.plot(sorted(lvl_L14), [lvl_L14[L] for L in sorted(lvl_L14)], "o-", color="C0",
             label="L14 cache explicit")
    ax1.plot(sorted(lvl_L16), [lvl_L16[L] for L in sorted(lvl_L16)], "s-", color="C2",
             label="L16 cache explicit")
    if lvl_fb:
        ax1.plot(sorted(lvl_fb), [lvl_fb[L] for L in sorted(lvl_fb)], "x", color="C3",
                 label="Friedrich-Bar bounded")
    ax1.set_xlabel("level (p+q)")
    ax1.set_ylabel("sector count")
    ax1.set_title(f"cache completeness  (L14_op={L14_op}, L16_op={L16_op})")
    ax1.grid(alpha=0.3)
    ax1.legend(fontsize=8)

    # Right: sentinel residual per cached (p,0)/(0,q) sector (the VALIDATION GATE)
    items = sorted(sentinel_detail.items(), key=lambda kv: kv[1])
    labels = [k for k, _ in items]
    vals = [max(v, 1e-18) for _, v in items]               # floor for log scale
    ax2.barh(range(len(vals)), vals, color="C0")
    ax2.axvline(sentinel_max, color="C3", ls="--", lw=1, label=f"max={sentinel_max:.2e}")
    ax2.axvline(1e-10, color="k", ls=":", lw=1, label="tol 1e-10")
    ax2.set_xscale("log")
    ax2.set_yticks(range(len(labels)))
    ax2.set_yticklabels(labels, fontsize=6)
    ax2.set_xlabel(r"GT-vs-cache $\max|\Delta\lambda|$ per sector")
    ax2.set_title(f"VALIDATION GATE (bit-exact GT-vs-cache)  =>  {verdict}")
    ax2.grid(alpha=0.3, axis="x")
    ax2.legend(fontsize=8)

    fig.suptitle(f"{GATE_ID} — L14/L16 D_K spectrum caches @ tau_fold "
                 f"(GT (p,0) ladder + Casimir mixed)  =>  {verdict}", fontsize=11)
    fig.tight_layout()
    fig.savefig(SESSION_DIR / "s106_w1_highl_cache_l1416.png", dpi=120)
    plt.close(fig)


def _make_plot_fail(sentinel_detail, sentinel_max):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(8, 6))
    items = sorted(sentinel_detail.items(), key=lambda kv: kv[1])
    labels = [k for k, _ in items]
    vals = [max(v, 1e-18) for _, v in items]
    ax.barh(range(len(vals)), vals, color="C3")
    ax.axvline(sentinel_max, color="k", ls="--", lw=1, label=f"max={sentinel_max:.2e}")
    ax.axvline(1e-10, color="C0", ls=":", lw=1, label="tol 1e-10")
    ax.set_xscale("log")
    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels(labels, fontsize=6)
    ax.set_xlabel(r"GT-vs-cache $\max|\Delta\lambda|$ per sector")
    ax.set_title(f"{GATE_ID} — VALIDATION GATE FAIL\n"
                 f"GT-vs-cache sentinel max={sentinel_max:.2e} >= 1e-10 -> no new-sector consumption")
    ax.grid(alpha=0.3, axis="x")
    ax.legend(fontsize=9)
    fig.tight_layout()
    fig.savefig(SESSION_DIR / "s106_w1_highl_cache_l1416.png", dpi=120)
    plt.close(fig)


if __name__ == "__main__":
    main()
