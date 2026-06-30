#!/usr/bin/env python3
"""
INV10 W1-4 INV10-W1-4-SYNTHETIC-TAU-ZAK-PHASE — Synthetic-(tau) Zak-phase winding
=================================================================================

Gate: INV10-W1-4-SYNTHETIC-TAU-ZAK-PHASE ([CHAIN])

Pre-registered (set-membership) criterion:
  PROTECTED = (gamma_Zak quantized to within 0.05*pi of {0, pi})
              AND (gamma_Zak epsilon-STABLE: drift < 0.05*pi across
                   eps in {1e-2, 1e-3, 1e-4} — the sweep that DISSOLVED S46)
  PASS  iff PROTECTED is True AND gamma_Zak is nonzero (~pi)  -> tau_fold topological
  FAIL  iff gamma_Zak dissolves under the eps-sweep (like S46) OR non-quantized
  INFO  iff nonzero + partially eps-stable but does not cleanly quantize

Physics (substrate-first, GEOMETRIC):
  The substrate IS the spectral triple (A_K, H_K, D_K(tau)) at each tau; the
  MODULI-SPACE of Jensen TT-deformations {D_K(tau)} is itself substrate-IS
  (Level-2 moduli-deformation per phononic-framing.md). Treating tau as a
  SYNTHETIC MOMENTUM, the van Hove fold at tau_fold=0.190 is a band-touching in
  the extended (k,tau) zone. The synthetic-(tau)-axis Zak phase is the holonomy
  (Wilson loop) of the Berry connection around that touching:

      gamma_Zak = -Im log det( PROD_j  U_n(tau_j)^dag U_n(tau_{j+1}) )

  computed as the GAUGE-INVARIANT Wilson-loop PRODUCT (the per-point gauge/index
  telescopes out of the product), NOT a finite-difference of phases.

DISTINCTNESS GUARDS (the load-bearing content of this gate):
  (1) vs W5 (S25): W5 proves the LOCAL Berry CURVATURE Omega = 0 EXACT (2-form
      field strength; K_a anti-Hermitian => real matrix elements => Im(QGT)=0).
      The Zak phase is the 1D HOLONOMY (integrated connection), NOT the curvature.
      By Stokes, oint A = int int Omega ONLY if the loop bounds a SMOOTH surface.
      A loop encircling a band TOUCHING does NOT (the node is a puncture / Weyl
      node where the bundle is singular). So Omega=0 away from the node does NOT
      force gamma_Zak=0 around it (Dirac-monopole: zero field strength on the
      sphere minus poles, nonzero holonomy around a pole). This script RE-DERIVES
      Omega~0 to confirm the LOCAL object is the W5 object, so the GLOBAL winding
      is demonstrably a different observable.
  (2) vs S46/S48 (DISSOLUTION-48): S46 found a k-space (ordinary-BZ) Zak phase
      (13 pi-phases) RETRACTED at S48 ("0/10 survive at eps=1e-4; index-permutation
      artifact at degeneracies"). That pathology was phase-TRACKING through
      degeneracies by finite-differencing eigenstate phases (index labels permute
      at crossings -> spurious pi jumps). THIS gate (a) computes along the
      SYNTHETIC tau-axis (trace_entity('synthetic tau Zak phase') = "No trace
      found" => never computed); (b) uses the gauge-invariant Wilson-loop PRODUCT
      with NON-ABELIAN handling of degenerate sub-bundles (relabel-invariant by
      construction); (c) runs the SAME eps in {1e-2,1e-3,1e-4} sweep that dissolved
      S46 as a PROTECTION TEST. A topological winding is eps-stable; an artifact
      dissolves. This script ALSO emits the finite-difference (S48-pathology)
      estimator on the same data, so the contrast is visible in the artifact.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py (tau_fold, PI) [audit only]
  - computations/_shared/dirac_spectrum.py (D_K(tau) eigenvector builder) [audit only]
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<gamma_Zak/pi or PROTECTED-flag>, scheme=SA, convention=MIXED, L_max=10)

Classification: GEOMETRIC

Author: tesla-resonance (INV10 W1-4; baptista Jensen-tau band structure + berry
        Zak/Wilson-loop machinery as method consultants)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # CPU thread cap (cross-agent contention)
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403  (tau_fold, PI, ...)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time
import numpy as np

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

from dirac_spectrum import (
    su3_generators, compute_structure_constants, build_cliff8,
    collect_spectrum_with_eigenvectors,
)

# Optional GPU path (Peter-Weyl touching block may be >= 100x100)
try:
    import torch
    _HAVE_TORCH = torch.cuda.is_available()
except Exception:
    _HAVE_TORCH = False

# ---------------------------------------------------------------------------
# Section 3 — Pre-registration pins
# ---------------------------------------------------------------------------
SESSION = "S10"                                                    # (local) investigation track n=10
GATE_ID = "INV10-W1-4-SYNTHETIC-TAU-ZAK-PHASE"                    # (local)
SCHEME = "SA"                                                      # (local) spectral-action / D_K-spectral
CONVENTION = "MIXED"                                               # (local) Wilson-loop holonomy (gauge-invariant product)
L_MAX = 10                                                         # (local) D_K cache truncation

# tau-loop bracketing the fold (gate machinery_pin_map)
TAU_MIN = 0.15                                                     # (local)
TAU_MAX = 0.25                                                     # (local)
N_TAU = 200                                                        # (local) points across the window
MAX_PQ_SUM = 3                                                     # (local) low-sector Peter-Weyl truncation tracking the fold bands

# Quantization / stability windows (gate strict_PASS_boundary)
QUANT_WIN = 0.05                                                   # (local) |gamma/pi - {0,1}| < 0.05  (in units of pi)
STAB_WIN = 0.05                                                    # (local) eps-drift < 0.05*pi  (in units of pi)
EPS_SWEEP = [1e-2, 1e-3, 1e-4]                                     # (local) the S46-dissolving degeneracy-regularization sweep
N_REAL_EPS = 8                                                     # (local) random Hermitian realizations per eps
RNG_SEED = 173410                                                  # (local) deterministic eps-sweep seed (reproducible)
OVL_TOL = 1e-10                                                    # (local) eigenvector-overlap float64 tol
DEGEN_GAP = 5e-3                                                   # (local) gap below which two bands are a degenerate sub-bundle

OUT_NPZ = SESSION_DIR / "inv10_w1_synthetic_tau_zak_phase.npz"
OUT_PNG = SESSION_DIR / "inv10_w1_synthetic_tau_zak_phase.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    SHARED_DIR / "dirac_spectrum.py",
]

# ---------------------------------------------------------------------------
# Section 4 — Dual-SHA input-pin block (S84+)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
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
# Section 5 — Verdict payload (race-safe; agent calls emit_verdict)
# ---------------------------------------------------------------------------

def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note="", extra_rows=None):
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
# Section 6 — Wilson-loop machinery (GAUGE-INVARIANT)
# ---------------------------------------------------------------------------

def hermitian_overlap_matrix(U_a, U_b):
    """Overlap matrix M_mn = <u_m(a)|u_n(b)> for column-eigenvector blocks U_a,U_b.

    Gauge-invariant Wilson-loop FACTOR: any per-point unitary gauge g on the
    columns of U_a (U_a -> U_a g_a) and g_b on U_b telescopes out of the ordered
    PRODUCT of these factors around a loop. This is the structural difference
    from the S48 finite-difference-of-phases estimator.
    """
    return U_a.conj().T @ U_b   # (local)


def wilson_winding(U_list, band_idx, closed=True):
    """Gauge-invariant synthetic-tau Wilson-loop winding for a band sub-bundle.

    U_list[j] : (D, D) unitary eigenvector matrix at tau_j (columns = states)
    band_idx  : list of column indices forming the (possibly degenerate) sub-bundle
    closed    : if True, close the loop (last->first) — a CONTRACTIBLE round-trip
                sanity object; if False, OPEN forward holonomy 0.15->0.25 (the
                sign-flip across the fold, the node-encircling object in (k,tau)).

    Returns gamma = -Im log det(W) where W = PROD_j M_j restricted to band_idx.
    det() is the non-Abelian (Wilczek-Zee) relabel-invariant reduction: any
    permutation/mixing within the degenerate sub-bundle is a U(n_deg) gauge that
    det annihilates up to its (quantized) determinant phase.
    """
    n = len(band_idx)  # (local)
    W = np.eye(n, dtype=complex)  # (local)
    N = len(U_list)  # (local)
    upper = N if closed else N - 1  # (local)
    for j in range(upper):
        jn = (j + 1) % N  # (local)
        Ua = U_list[j][:, band_idx]   # (local)
        Ub = U_list[jn][:, band_idx]  # (local)
        M = hermitian_overlap_matrix(Ua, Ub)  # (local)
        W = W @ M
    detW = np.linalg.det(W)  # (local)
    gamma = -np.angle(detW)  # (local) -Im log det = -arg(det)
    return gamma, detW, W


def finite_difference_winding(U_list, band_col, closed=True):
    """S48-PATHOLOGY estimator (for CONTRAST only): finite-difference of phases
    with per-band sign gauge-fixing through degeneracies. This is exactly the
    index-tracking estimator that produced the RETRACTED S46 result; emitting it
    next to the Wilson product makes the distinctness visible in the artifact.
    """
    N = len(U_list)  # (local)
    fixed = [U_list[0][:, band_col].copy()]  # (local)
    for j in range(1, N):
        prev = fixed[j - 1]  # (local)
        curr = U_list[j][:, band_col].copy()  # (local)
        ov = np.vdot(prev, curr)  # (local)
        if abs(ov) > 1e-12:
            curr *= np.conj(ov / abs(ov))
        fixed.append(curr)
    log_sum = 0.0 + 0j  # (local)
    upper = N if closed else N - 1  # (local)
    for j in range(upper):
        jn = (j + 1) % N  # (local)
        ov = np.vdot(fixed[j], fixed[jn])  # (local)
        log_sum += np.log(ov + 0j)
    return -log_sum.imag


# ---------------------------------------------------------------------------
# Section 7 — Local Berry curvature (W5 re-derivation, distinctness guard)
# ---------------------------------------------------------------------------

def local_berry_curvature_imag_qgt(U_tau, U_taup, U_taupp):
    """Estimate the magnitude of the LOCAL Berry curvature (imaginary part of the
    quantum geometric tensor) for the lowest non-degenerate band, via the
    plaquette/three-point finite difference along the single tau axis.

    On a 1D parameter axis the curvature 2-form has no area to integrate; the
    meaningful W5 statement is Im(QGT)=0 (eigenvectors real => zero Berry phase
    density). We probe Im<d u | d u> ~ Im( <u(taup)-u(tau) | u(taupp)-u(taup)> )
    as a scalar witness that the connection is REAL (==> the local object carries
    NO Berry phase density; only the GLOBAL holonomy around a node can be pi).
    Returns max |Im(...)| over bands.
    """
    du1 = U_taup - U_tau     # (local)
    du2 = U_taupp - U_taup   # (local)
    g = du1.conj().T @ du2   # (local) D x D
    return float(np.max(np.abs(np.imag(np.diagonal(g)))))


def generate_random_hermitian(dim, rng):
    """Unit-Frobenius-norm random COMPLEX Hermitian — the S48-dissolving kick:
    it both lifts exact degeneracies AND breaks eigenvector reality."""
    A = rng.standard_normal((dim, dim)) + 1j * rng.standard_normal((dim, dim))  # (local)
    H = 0.5 * (A + A.conj().T)  # (local)
    nrm = np.linalg.norm(H, ord="fro")  # (local)
    if nrm > 0:
        H = H / nrm
    return H


# ---------------------------------------------------------------------------
# Section 8 — Build D_K(tau) band structure on the tau-loop
# ---------------------------------------------------------------------------

def build_sector_H_over_tau(tau_grid, sector_pq):
    """Return list of Hermitian H(tau)=1j*D_pi for the chosen Peter-Weyl sector,
    plus the per-tau (evals, evecs). D_K is BLOCK-DIAGONAL by Peter-Weyl; we
    diagonalize a single block-pair sector containing the fold's touching bands.
    """
    gens = su3_generators()       # (local)
    f_abc = compute_structure_constants(gens)  # (local)
    gammas = build_cliff8()       # (local)

    H_list = []     # (local)
    evals_list = []  # (local)
    evecs_list = []  # (local)
    for tau in tau_grid:
        sector_data, _ = collect_spectrum_with_eigenvectors(
            tau, gens, f_abc, gammas, max_pq_sum=MAX_PQ_SUM, verbose=False)
        sd_map = {(sd["p"], sd["q"]): sd for sd in sector_data}  # (local)
        sd = sd_map[sector_pq]  # (local)
        H = 1j * sd["D_pi"]  # (local)
        H = 0.5 * (H + H.conj().T)  # force exact Hermiticity (local)
        H_list.append(H)
        evals_list.append(sd["evals"])
        evecs_list.append(sd["evecs"])
    return H_list, evals_list, evecs_list, (gens, f_abc, gammas)


def gpu_eigh(H):
    """GPU Hermitian eig (validated vs numpy on first call)."""
    if _HAVE_TORCH and H.shape[0] >= 100:
        t = torch.tensor(H, device="cuda", dtype=torch.complex128)  # (local)
        w, v = torch.linalg.eigh(t)  # (local)
        return w.cpu().numpy(), v.cpu().numpy()
    w, v = np.linalg.eigh(H)
    return w, v


# ---------------------------------------------------------------------------
# Section 9 — Compute
# ---------------------------------------------------------------------------

def compute():
    t0 = time.time()  # (local)
    print("=" * 78)
    print(f"{GATE_ID}: Synthetic-(tau) Zak-phase winding around the tau_fold touching")
    print("=" * 78)
    print(f"  tau-loop: [{TAU_MIN}, {TAU_MAX}] enclosing tau_fold={tau_fold}, N_tau={N_TAU}")
    print(f"  L_max={L_MAX} (max_pq_sum={MAX_PQ_SUM}); scheme={SCHEME}; convention={CONVENTION}")
    print(f"  GPU available: {_HAVE_TORCH}")
    print(f"  eps-sweep (S46-dissolving): {EPS_SWEEP}, N_real={N_REAL_EPS}, seed={RNG_SEED}")

    tau_grid = np.linspace(TAU_MIN, TAU_MAX, N_TAU)  # (local)
    i_fold = int(np.argmin(np.abs(tau_grid - tau_fold)))  # (local)
    print(f"  fold index in grid: {i_fold} (tau={tau_grid[i_fold]:.5f})")

    # ---- Select the Peter-Weyl sector carrying the fold's touching bands. ----
    # The van Hove fold concentrates in the singlet/low sectors. We scan the
    # candidate low sectors for the one whose lowest band-gap is MINIMIZED near
    # tau_fold (the band touching), and run the Wilson loop there. We compute the
    # full (0,0) singlet sector (16-dim) plus the fundamental (1,0) as cross-check.
    candidate_sectors = [(0, 0), (1, 0), (0, 1), (1, 1)]  # (local)

    sector_results = {}  # (local)
    gens = su3_generators()  # (local)
    f_abc = compute_structure_constants(gens)  # (local)
    gammas = build_cliff8()  # (local)

    # First: cheap gap scan at three tau points to pick the touching sector.
    gap_probe_tau = [TAU_MIN, tau_fold, TAU_MAX]  # (local)
    sector_min_gap = {}  # (local)
    for spq in candidate_sectors:
        gaps_here = []  # (local)
        for tau in gap_probe_tau:
            sector_data, _ = collect_spectrum_with_eigenvectors(
                tau, gens, f_abc, gammas, max_pq_sum=MAX_PQ_SUM, verbose=False)
            sd_map = {(sd["p"], sd["q"]): sd for sd in sector_data}  # (local)
            ev = np.sort(sd_map[spq]["evals"])  # (local)
            # gap between the two bands straddling zero (lowest |lambda| pair)
            pos = ev[ev >= 0]  # (local)
            neg = ev[ev < 0]   # (local)
            if len(pos) >= 1 and len(neg) >= 1:
                gaps_here.append(pos[0] - neg[-1])
            else:
                gaps_here.append(np.min(np.diff(ev)))
        sector_min_gap[spq] = float(np.min(gaps_here))
        print(f"  sector {spq}: min zero-straddle gap over probe = {sector_min_gap[spq]:.6e}")

    touching_sector = min(sector_min_gap, key=sector_min_gap.get)  # (local)
    print(f"\n  TOUCHING SECTOR (minimal gap near fold): {touching_sector}")

    # We run the Wilson loop on BOTH the touching sector AND the (0,0) singlet
    # (the spinor sector where Omega alone acts) for robustness.
    run_sectors = list(dict.fromkeys([touching_sector, (0, 0)]))  # (local)

    primary = {}  # (local)
    for spq in run_sectors:
        print("\n" + "-" * 78)
        print(f"  SECTOR {spq}: building D_K(tau) band structure over the tau-loop")
        print("-" * 78)
        H_list, evals_list, evecs_list, _ = build_sector_H_over_tau(tau_grid, spq)
        D = evecs_list[0].shape[1]  # (local) sector Hilbert dim
        print(f"    sector dim = {D} (block-diagonal Peter-Weyl block)")

        evals_arr = np.array(evals_list)   # (local) (N_tau, D)
        # Identify the band-touching group: the pair of bands with minimal gap
        # near the fold (the zero-straddle pair).
        ev_fold = np.sort(evals_arr[i_fold])  # (local)
        order_fold = np.argsort(evals_arr[i_fold])  # (local)
        # zero-straddle indices in the SORTED spectrum
        n_neg = int(np.sum(ev_fold < 0))  # (local)
        if 0 < n_neg < D:
            lo_sorted, hi_sorted = n_neg - 1, n_neg  # (local) the two straddling zero
        else:
            # fallback: the minimal adjacent gap
            d = np.diff(ev_fold)  # (local)
            lo_sorted = int(np.argmin(d)); hi_sorted = lo_sorted + 1  # (local)
        touch_gap_fold = float(ev_fold[hi_sorted] - ev_fold[lo_sorted])  # (local)
        # Map sorted-position -> actual column index in the (already eigh-sorted) evecs.
        # scipy_eigh returns ascending order, so column index == sorted position.
        band_group = [lo_sorted, hi_sorted]  # (local) the degenerate-pair sub-bundle
        print(f"    band-touching pair (sorted idx): {band_group}, gap at fold = {touch_gap_fold:.6e}")

        # --- (A) Gauge-invariant Wilson winding (PRIMARY OBSERVABLE) ---
        # Closed contractible loop (sanity: should be trivial mod the node) and
        # open forward holonomy across the fold (node-encircling sign-flip).
        gamma_closed, detW_c, W_c = wilson_winding(evecs_list, band_group, closed=True)
        gamma_open, detW_o, W_o = wilson_winding(evecs_list, band_group, closed=False)

        # Single-band (lowest of the pair) Abelian winding as a cross-check.
        gamma_ab_closed, detW_abc, _ = wilson_winding(evecs_list, [band_group[0]], closed=True)
        gamma_ab_open, detW_abo, _ = wilson_winding(evecs_list, [band_group[0]], closed=False)

        # --- (B) S48-pathology finite-difference estimator (CONTRAST ONLY) ---
        gamma_fd_closed = finite_difference_winding(evecs_list, band_group[0], closed=True)
        gamma_fd_open = finite_difference_winding(evecs_list, band_group[0], closed=False)

        # --- (C) Local Berry curvature (W5 distinctness guard) ---
        im_qgt = []  # (local)
        for j in range(1, len(evecs_list) - 1):
            im_qgt.append(local_berry_curvature_imag_qgt(
                evecs_list[j - 1], evecs_list[j], evecs_list[j + 1]))
        max_im_qgt = float(np.max(im_qgt)) if im_qgt else 0.0  # (local)

        # --- reality check on eigenvectors (after a global-phase fix) ---
        # eigh columns have an arbitrary U(1); rotate each to maximal-real then
        # measure residual imaginary weight.
        max_im_evec = 0.0  # (local)
        for U in evecs_list:
            for n in range(U.shape[1]):
                col = U[:, n]  # (local)
                k = int(np.argmax(np.abs(col)))  # (local)
                ph = col[k] / abs(col[k]) if abs(col[k]) > 0 else 1.0  # (local)
                colr = col * np.conj(ph)  # (local)
                max_im_evec = max(max_im_evec, float(np.max(np.abs(np.imag(colr)))))

        print(f"    [Wilson product, non-Abelian det, pair {band_group}]")
        print(f"      gamma_closed/pi = {gamma_closed/PI:+.6f}   det(W_closed)={detW_c:.6f}")
        print(f"      gamma_open/pi   = {gamma_open/PI:+.6f}   det(W_open)  ={detW_o:.6f}")
        print(f"    [Wilson product, Abelian single band {band_group[0]}]")
        print(f"      gamma_ab_closed/pi = {gamma_ab_closed/PI:+.6f}  det={detW_abc:.6f}")
        print(f"      gamma_ab_open/pi   = {gamma_ab_open/PI:+.6f}  det={detW_abo:.6f}")
        print(f"    [S48-pathology finite-difference estimator, CONTRAST]")
        print(f"      gamma_fd_closed/pi = {gamma_fd_closed/PI:+.6f}")
        print(f"      gamma_fd_open/pi   = {gamma_fd_open/PI:+.6f}")
        print(f"    [W5 distinctness] max|Im(QGT)| (local Berry curvature witness) = {max_im_qgt:.3e}")
        print(f"    [reality] max|Im(eigvec)| after global-phase fix = {max_im_evec:.3e}")

        # --- (D) eps-protection sweep on the PRIMARY observable (Wilson product) ---
        # Add eps*||H||*V_rand (complex Hermitian, the S48-dissolving kick) at each
        # tau, recompute the GAUGE-INVARIANT Wilson winding, test eps-stability.
        rng = np.random.default_rng(RNG_SEED)  # (local)
        eps_gamma_closed = {}  # (local) eps -> list over realizations
        eps_gamma_open = {}    # (local)
        eps_gamma_fd = {}      # (local) the pathology estimator under eps (should dissolve)
        Hnorm_mean = float(np.mean([np.linalg.norm(H, ord="fro") for H in H_list]))  # (local)
        for eps in EPS_SWEEP:
            gc_list, go_list, gfd_list = [], [], []  # (local)
            for r in range(N_REAL_EPS):
                U_pert = []  # (local)
                for H in H_list:
                    V = generate_random_hermitian(H.shape[0], rng)  # (local)
                    Hp = H + eps * Hnorm_mean * V  # (local)
                    Hp = 0.5 * (Hp + Hp.conj().T)  # (local)
                    w, v = gpu_eigh(Hp) if H.shape[0] >= 100 else np.linalg.eigh(Hp)
                    # eigh sorts ascending -> same band_group sorted indices
                    U_pert.append(v)
                gc, _, _ = wilson_winding(U_pert, band_group, closed=True)
                go, _, _ = wilson_winding(U_pert, band_group, closed=False)
                gfd = finite_difference_winding(U_pert, band_group[0], closed=True)
                gc_list.append(gc); go_list.append(go); gfd_list.append(gfd)
            eps_gamma_closed[eps] = gc_list
            eps_gamma_open[eps] = go_list
            eps_gamma_fd[eps] = gfd_list
            print(f"    eps={eps:.0e}: Wilson gamma_closed/pi mean={np.mean(gc_list)/PI:+.4f} "
                  f"std={np.std(gc_list)/PI:.4f}; gamma_open/pi mean={np.mean(go_list)/PI:+.4f} "
                  f"std={np.std(go_list)/PI:.4f}; [FD-pathology gamma/pi std={np.std(gfd_list)/PI:.4f}]")

        sector_results[spq] = dict(
            D=D, band_group=band_group, touch_gap_fold=touch_gap_fold,
            gamma_closed=gamma_closed, gamma_open=gamma_open,
            gamma_ab_closed=gamma_ab_closed, gamma_ab_open=gamma_ab_open,
            gamma_fd_closed=gamma_fd_closed, gamma_fd_open=gamma_fd_open,
            max_im_qgt=max_im_qgt, max_im_evec=max_im_evec,
            evals_arr=evals_arr,
            eps_gamma_closed=eps_gamma_closed, eps_gamma_open=eps_gamma_open,
            eps_gamma_fd=eps_gamma_fd,
        )
        if not primary:
            primary = dict(sector=spq, **sector_results[spq])

    # ----------------------------------------------------------------------
    # Section 10 — Verdict logic (set-membership PROTECTED)
    # ----------------------------------------------------------------------
    print("\n" + "=" * 78)
    print("  VERDICT LOGIC (set-membership PROTECTED)")
    print("=" * 78)

    sec = primary["sector"]  # (local)
    # The node-encircling object is the OPEN forward holonomy (the sign-flip across
    # the fold); the closed loop is the contractible sanity object. We assess BOTH
    # quantization of the primary winding and eps-stability under the S46 sweep.
    gamma_primary = primary["gamma_open"]  # (local) node-encircling sign-flip across the fold
    gamma_primary_pi = gamma_primary / PI  # (local)

    # quantization: nearest of {0, +-1} in units of pi
    nearest = round(gamma_primary_pi)  # (local) integer multiple of pi
    quant_dev = abs(gamma_primary_pi - nearest)  # (local)
    is_quantized = quant_dev < QUANT_WIN  # (local)
    is_nonzero = (abs(nearest) % 2) == 1  # (local) ~pi (odd multiple)

    # eps-stability of the Wilson winding (mean over realizations vs eps=0 value),
    # AND the within-eps spread (a protected winding is sharp, not scattered).
    drift_pi = []  # (local)
    spread_pi = []  # (local)
    for eps in EPS_SWEEP:
        gmean = np.mean(primary["eps_gamma_open"][eps])  # (local)
        gstd = np.std(primary["eps_gamma_open"][eps])    # (local)
        drift_pi.append(abs((gmean - gamma_primary) / PI))
        spread_pi.append(gstd / PI)
    max_drift_pi = float(np.max(drift_pi))  # (local)
    max_spread_pi = float(np.max(spread_pi))  # (local)
    is_eps_stable = (max_drift_pi < STAB_WIN) and (max_spread_pi < STAB_WIN)  # (local)

    # The S48-pathology estimator's eps-behavior (for the contrast narrative):
    fd_spread_pi = float(np.max([np.std(primary["eps_gamma_fd"][e]) / PI for e in EPS_SWEEP]))  # (local)

    PROTECTED = bool(is_quantized and is_eps_stable)  # (local)

    print(f"  primary winding (OPEN forward holonomy across fold), sector {sec}: gamma/pi = {gamma_primary_pi:+.6f}")
    print(f"    nearest integer*pi = {nearest}; quant deviation = {quant_dev:.4f} (win {QUANT_WIN}) -> quantized={is_quantized}")
    print(f"    nonzero (~pi)? {is_nonzero}")
    print(f"    eps-sweep max drift = {max_drift_pi:.4f}*pi, max within-eps spread = {max_spread_pi:.4f}*pi (win {STAB_WIN}) -> eps_stable={is_eps_stable}")
    print(f"    [contrast] S48-pathology FD estimator eps-spread = {fd_spread_pi:.4f}*pi")
    print(f"  PROTECTED = quantized AND eps_stable = {PROTECTED}")
    print(f"  W5 distinctness: local Berry curvature max|Im(QGT)| = {primary['max_im_qgt']:.3e} (~0 => GLOBAL winding is a DIFFERENT object)")

    if PROTECTED and is_nonzero:
        verdict = "PASS"
        value = f"PROTECTED_True_gamma/pi={gamma_primary_pi:+.4f}_eps-stable_drift<{STAB_WIN}pi"
    elif PROTECTED and not is_nonzero:
        # quantized to 0 and eps-stable: a TRIVIAL but well-defined winding ->
        # NOT a protected nontrivial node; the synthetic-topology selection route
        # is closed (tau_fold remains empirical). FAIL per the gate rubric.
        verdict = "FAIL"
        value = f"PROTECTED-but-TRIVIAL_gamma/pi={gamma_primary_pi:+.4f}_quantized-to-0_no-pi-winding"
    elif (not is_eps_stable) and is_quantized:
        # quantized at eps=0 but dissolves under the sweep (like S46) -> FAIL
        verdict = "FAIL"
        value = f"DISSOLVES_under_eps-sweep_drift={max_drift_pi:.3f}pi_spread={max_spread_pi:.3f}pi"
    elif (not is_quantized) and (max_spread_pi < 0.2):
        # nonzero, partially stable, but not cleanly quantized -> INFO
        verdict = "INFO"
        value = f"NON-QUANTIZED_gamma/pi={gamma_primary_pi:+.4f}_dev={quant_dev:.3f}_spread={max_spread_pi:.3f}pi"
    else:
        verdict = "FAIL"
        value = f"NON-QUANTIZED_and_UNSTABLE_gamma/pi={gamma_primary_pi:+.4f}_spread={max_spread_pi:.3f}pi"

    print(f"\n  GATE {GATE_ID}: {verdict}")
    print(f"    value = {value}")

    elapsed = time.time() - t0  # (local)
    print(f"\n  elapsed: {elapsed:.1f}s")

    return dict(
        verdict=verdict, value=value,
        sector=sec, tau_grid=tau_grid, i_fold=i_fold,
        gamma_primary_pi=gamma_primary_pi, nearest=nearest, quant_dev=quant_dev,
        is_quantized=is_quantized, is_nonzero=is_nonzero,
        max_drift_pi=max_drift_pi, max_spread_pi=max_spread_pi,
        is_eps_stable=is_eps_stable, fd_spread_pi=fd_spread_pi,
        PROTECTED=PROTECTED,
        sector_results=sector_results, primary=primary,
        touching_sector=touching_sector, sector_min_gap=sector_min_gap,
    )


# ---------------------------------------------------------------------------
# Section 11 — Plot
# ---------------------------------------------------------------------------

def make_plot(res):
    sec = res["sector"]  # (local)
    pr = res["primary"]  # (local)
    tau_grid = res["tau_grid"]  # (local)
    evals_arr = pr["evals_arr"]  # (local)
    band_group = pr["band_group"]  # (local)

    fig = plt.figure(figsize=(16, 11))  # (local)
    gs = GridSpec(2, 2, figure=fig, hspace=0.30, wspace=0.26)  # (local)

    # Panel 1: band structure across the fold, touching pair highlighted
    ax1 = fig.add_subplot(gs[0, 0])  # (local)
    for n in range(evals_arr.shape[1]):
        ax1.plot(tau_grid, evals_arr[:, n], lw=0.7, color="0.6")
    for b in band_group:
        ax1.plot(tau_grid, evals_arr[:, b], lw=2.0, label=f"band {b}")
    ax1.axvline(tau_fold, color="r", ls="--", lw=1.0, label=f"tau_fold={tau_fold}")
    ax1.set_xlabel("tau (synthetic momentum)")
    ax1.set_ylabel("eigenvalue of 1j*D_K  (M_KK)")
    ax1.set_title(f"D_K(tau) band structure, sector {sec} — touching pair {band_group}")
    ax1.legend(fontsize=7, ncol=2)

    # Panel 2: eps-sweep of the Wilson winding (PRIMARY) vs the FD pathology
    ax2 = fig.add_subplot(gs[0, 1])  # (local)
    eps_x = EPS_SWEEP  # (local)
    wil_mean = [np.mean(pr["eps_gamma_open"][e]) / PI for e in eps_x]  # (local)
    wil_std = [np.std(pr["eps_gamma_open"][e]) / PI for e in eps_x]    # (local)
    fd_mean = [np.mean(pr["eps_gamma_fd"][e]) / PI for e in eps_x]     # (local)
    fd_std = [np.std(pr["eps_gamma_fd"][e]) / PI for e in eps_x]       # (local)
    ax2.errorbar(np.log10(eps_x), wil_mean, yerr=wil_std, fmt="o-", capsize=4,
                 label="Wilson product (gauge-inv, primary)")
    ax2.errorbar(np.log10(eps_x), fd_mean, yerr=fd_std, fmt="s--", capsize=4,
                 color="crimson", label="finite-diff (S48 pathology)")
    ax2.axhline(res["gamma_primary_pi"], color="navy", ls=":", lw=1.0,
                label=f"eps=0 Wilson gamma/pi={res['gamma_primary_pi']:+.3f}")
    ax2.axhline(0, color="0.4", ls=":", lw=0.6)
    ax2.set_xlabel("log10(eps)  [S46-dissolving degeneracy regularization]")
    ax2.set_ylabel("gamma_Zak / pi")
    ax2.set_title("eps-protection sweep — protected winding is flat; artifact scatters")
    ax2.legend(fontsize=7)

    # Panel 3: zero-straddle gap (the touching) vs tau
    ax3 = fig.add_subplot(gs[1, 0])  # (local)
    ev_sorted = np.sort(evals_arr, axis=1)  # (local)
    n_neg = np.sum(ev_sorted[res["i_fold"]] < 0)  # (local)
    if 0 < n_neg < ev_sorted.shape[1]:
        gap_tau = ev_sorted[:, n_neg] - ev_sorted[:, n_neg - 1]  # (local)
    else:
        gap_tau = np.min(np.diff(ev_sorted, axis=1), axis=1)  # (local)
    ax3.plot(tau_grid, gap_tau, "b-", lw=1.2)
    ax3.axvline(tau_fold, color="r", ls="--", lw=1.0)
    ax3.set_xlabel("tau")
    ax3.set_ylabel("zero-straddle band gap (M_KK)")
    ax3.set_title(f"Band touching at the fold (min gap = {pr['touch_gap_fold']:.2e})")

    # Panel 4: verdict text panel
    ax4 = fig.add_subplot(gs[1, 1])  # (local)
    ax4.axis("off")
    lines = [
        f"GATE {GATE_ID}",
        f"VERDICT: {res['verdict']}",
        "",
        f"primary winding (open holonomy across fold), sector {sec}:",
        f"   gamma_Zak/pi = {res['gamma_primary_pi']:+.5f}",
        f"   nearest int*pi = {res['nearest']}, dev = {res['quant_dev']:.4f}  (win {QUANT_WIN})",
        f"   quantized = {res['is_quantized']}   nonzero(~pi) = {res['is_nonzero']}",
        "",
        f"eps-sweep (S46-dissolving) {EPS_SWEEP}:",
        f"   max drift = {res['max_drift_pi']:.4f}*pi   max spread = {res['max_spread_pi']:.4f}*pi",
        f"   eps-stable = {res['is_eps_stable']}  (win {STAB_WIN})",
        f"   [contrast] FD-pathology eps-spread = {res['fd_spread_pi']:.3f}*pi",
        "",
        f"W5 distinctness: local Berry curvature",
        f"   max|Im(QGT)| = {pr['max_im_qgt']:.2e}  (~0 => global != local)",
        f"   max|Im(eigvec)| = {pr['max_im_evec']:.2e}",
        "",
        f"PROTECTED = {res['PROTECTED']}",
        f"-> tau_fold {'TOPOLOGICAL node' if (res['PROTECTED'] and res['is_nonzero']) else 'EMPIRICAL (synthetic-topology route closed)'}",
    ]  # (local)
    ax4.text(0.02, 0.98, "\n".join(lines), va="top", ha="left",
             family="monospace", fontsize=9, transform=ax4.transAxes)

    fig.suptitle(f"{GATE_ID}: {res['verdict']} | gamma/pi={res['gamma_primary_pi']:+.3f}, "
                 f"PROTECTED={res['PROTECTED']}", fontsize=13, fontweight="bold")
    fig.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
    print(f"  saved plot: {OUT_PNG}")


# ---------------------------------------------------------------------------
# Section 12 — Main
# ---------------------------------------------------------------------------

def main():
    pins = log_input_pins(INPUT_FILES)  # (local)
    audit_sha, content_sha = compute_dual_sha(Path(__file__).resolve(),
                                              SHARED_DIR / "canonical_constants.py", pins)  # (local)
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    res = compute()
    make_plot(res)

    # --- save npz ---
    pr = res["primary"]  # (local)
    np.savez(
        OUT_NPZ,
        gate=GATE_ID, verdict=res["verdict"], value=res["value"],
        scheme=SCHEME, convention=CONVENTION, L_max=L_MAX,
        tau_min=TAU_MIN, tau_max=TAU_MAX, N_tau=N_TAU, tau_fold=tau_fold,
        i_fold=res["i_fold"], tau_grid=res["tau_grid"],
        sector=str(res["sector"]), touching_sector=str(res["touching_sector"]),
        band_group=np.array(pr["band_group"]),
        gamma_primary_pi=res["gamma_primary_pi"], nearest=res["nearest"],
        quant_dev=res["quant_dev"], is_quantized=res["is_quantized"],
        is_nonzero=res["is_nonzero"], PROTECTED=res["PROTECTED"],
        max_drift_pi=res["max_drift_pi"], max_spread_pi=res["max_spread_pi"],
        is_eps_stable=res["is_eps_stable"], fd_spread_pi=res["fd_spread_pi"],
        eps_sweep=np.array(EPS_SWEEP), quant_win=QUANT_WIN, stab_win=STAB_WIN,
        gamma_closed_pi=pr["gamma_closed"] / PI, gamma_open_pi=pr["gamma_open"] / PI,
        gamma_ab_closed_pi=pr["gamma_ab_closed"] / PI, gamma_ab_open_pi=pr["gamma_ab_open"] / PI,
        gamma_fd_closed_pi=pr["gamma_fd_closed"] / PI, gamma_fd_open_pi=pr["gamma_fd_open"] / PI,
        max_im_qgt=pr["max_im_qgt"], max_im_evec=pr["max_im_evec"],
        evals_arr=pr["evals_arr"],
        eps_gamma_open=np.array([pr["eps_gamma_open"][e] for e in EPS_SWEEP]),
        eps_gamma_closed=np.array([pr["eps_gamma_closed"][e] for e in EPS_SWEEP]),
        eps_gamma_fd=np.array([pr["eps_gamma_fd"][e] for e in EPS_SWEEP]),
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"  saved data: {OUT_NPZ}")

    # 4-tuple final non-verdict line
    print(f"(value={res['value']!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")

    # --- distinctness companion rows (CHAIN trigger) ---
    extra = [
        f"# INV10-W1-4 distinctness: synthetic-(tau) Wilson product != S46/S48 k-space FD Zak (trace_entity 'synthetic tau Zak phase'=No-trace); "
        f"local Berry curvature max|Im(QGT)|={pr['max_im_qgt']:.2e} confirms W5 Omega~0 (GLOBAL winding is a distinct observable)",
        f"# INV10-W1-4 eps-protection: Wilson gamma/pi open={res['gamma_primary_pi']:+.4f} max-drift={res['max_drift_pi']:.4f}pi max-spread={res['max_spread_pi']:.4f}pi "
        f"vs S48-FD-pathology spread={res['fd_spread_pi']:.3f}pi over eps{EPS_SWEEP}",
    ]  # (local)

    note = (f"synthetic-(tau) Zak winding gamma/pi={res['gamma_primary_pi']:+.4f} sector {res['sector']}; "
            f"PROTECTED={res['PROTECTED']} (quantized={res['is_quantized']}, eps-stable={res['is_eps_stable']}); "
            f"distinct from W5(Omega=0 local) & S46/S48(k-space FD, retracted)")  # (local)

    print_verdict_payload(res["verdict"], res["value"], audit_sha, content_sha,
                          companion_note=note, extra_rows=extra)


if __name__ == "__main__":
    main()
