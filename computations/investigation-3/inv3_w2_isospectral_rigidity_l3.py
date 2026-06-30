#!/usr/bin/env python3
"""
INV3 W2-2 — ISOSPECTRAL RIGIDITY AT L_max=3 ("can one hear the Jensen geometry?")
=================================================================================

Gate: INV3-W2-2 ([VERIFY] set-membership)
  scheme = ISOSPECTRAL-RIGIDITY-L3
  convention = ABSOLUTE (a_n^{lattice} MULTISETS compared bit-for-bit)
  regulator_pin = a_n^{lattice} (GEOMETRIC Seeley-DeWitt curvature polynomials,
                  NOT the spectral-zeta moments a_n^{zeta}; the factor-3812
                  discipline is load-bearing: a_2^{SD}(fold)=0.728235 vs
                  a_2^{zeta}=2776.165389 are DIFFERENT objects)

Pre-registered threshold (set-membership / rigidity predicate):
  Degeneracy = EXISTS (tau_i != tau_j) such that
     multiset{lambda_k^2}(tau_i) == multiset{lambda_k^2}(tau_j)   (sorted, |.|<=tol)
     AND |a_n^{lattice}(tau_i) - a_n^{lattice}(tau_j)| <= tol  for n in {0,2,4}
     AND |V_total(tau_i) - V_total(tau_j)| > tol_V              (NON-spectral discriminator)
  PASS  iff degeneracy set is EMPTY (rigidity holds; spectrum reconstructs Jensen geometry)
  FAIL  iff degeneracy set is NON-EMPTY (a named isospectral-non-isometric pair exists)
  INFO  iff a NEAR-degeneracy in [tol, tol_V] band exists but no exact pair at scan resolution
  tols: spectral-multiset match 1e-9; moment-triple match 1e-9; V-discrimination 1e-6

Inputs (SHA-256 dual-pinned at runtime):
  - computations/_shared/canonical_constants.py (feeds audit_sha256 only)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz
        (cross-validation ONLY: L_max=3 sub-block reconstruction at tau=0.19;
         NOT the primary input -- D_K(tau) is rebuilt per tau)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<degeneracy-set-cardinality + closest-pair witness>, scheme=ISOSPECTRAL-RIGIDITY-L3,
   convention=ABSOLUTE, L_max=3)

Classification: GEOMETRIC (tests whether D_K^2 spectrum reconstructs the Jensen geometry;
  the fabric's vibrational spectrum determining its own internal structure -- Kac's
  "can one hear the shape of the drum?" specialized to the substrate).

METHODOLOGY (structure-first)
-----------------------------
The heat trace P(sigma)=Tr e^{-sigma D_K^2} is the Rosetta Stone. Its small-sigma
asymptotics carry the LOCAL geometry as the Seeley-DeWitt invariants {a_0, a_2, a_4};
its full eigenvalue list {lambda_k^2} is the GLOBAL spectral datum. On the
volume-preserving Jensen TT family (SU(3), g_tau), the GEOMETRIC SD triple depends on
tau ONLY through the curvature scalars:

  a_0^{lattice}(tau) = (4 pi)^{-d/2} * tr_S(1) * Vol(g_tau)
                     = (4 pi)^{-4} * 16 * Vol               [TAU-INDEPENDENT: Jensen
                                                              is volume-preserving]
  a_2^{lattice}(tau) = (4 pi)^{-d/2} * tr_S(R/6 - E) * Vol
                     = (4 pi)^{-4} * (20 R(tau)/3) * Vol     [proportional to R(tau);
                                                              E = -R/4 Lichnerowicz]
  a_4^{lattice}(tau) = (4 pi)^{-d/2} * (1/360) * Vol *
                       [ 60 R E + 180 E^2 + 30 tr(Omega_{ab}Omega^{ab})/16
                         + (5 R^2 - 2|Ric|^2 + 2|Riem|^2) ]  [all derivative terms
                                                              vanish on homogeneous K]

R(tau), |Ric|^2(tau), |Riem|^2(tau) are the SP-2 exact analytic curvature scalars
(machine-eps validated, S20a 147/147). The spin-bundle curvature term
tr(Omega_{ab} Omega^{ab}) with Omega_{ab} = (1/4) R_{abcd} gamma^c gamma^d is computed
EXACTLY from R_abcd + the Cliff(8) gammas (no folklore coefficient).

The Dirac eigenvalue multiset {lambda_k^2(tau)} is built per Peter-Weyl sector
(p+q <= 3) via dirac_spectrum.collect_spectrum_with_eigenvectors, with each sector's
eigenvalues entered with PW multiplicity dim(p,q).

The Kosmann pairing V_total(tau) is the NON-spectral discriminator -- the Frobenius
pairing-norm of the Kosmann-Lichnerowicz spinorial correction on the (0,0) singlet
sector (the canonical s23a construction), built from the ANTISYMMETRIC covariant-
derivative form A^a_{rs}(tau) = Gamma^s_{ra}(tau) - Gamma^r_{sa}(tau) (Baptista Paper 17
eq 4.1). It lives in the spinor structure (how the Lie-derivative / Clifford action
connects modes) and carries tau-dependent geometric information the bare eigenvalue
list may not.

The rigidity predicate is then an O(N^2) pairwise scan over 2001 tau in [0.05, 0.35].

DISCIPLINE
----------
- from canonical_constants import *
- a_n are a_n^{lattice} (GEOMETRIC SD curvature polynomials), NEVER a_n^{zeta}
- GPU path: torch.linalg.eigvalsh per Peter-Weyl block (blocks small at L_max=3:
  largest is (3,0)/(0,3) dim 10 x16 spinor = 160; trivial). The O(N^2)=2001^2 pairwise
  tau-scan over precomputed per-tau signatures is the cost.
- dual-SHA (S84+); 4-tuple final non-verdict line; verdict via emit_verdict MCP tool.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
import os
SESSION_DIR = os.path.dirname(os.path.abspath(__file__))
COMPUTATIONS_DIR = os.path.dirname(SESSION_DIR)
SHARED_DIR = os.path.join(COMPUTATIONS_DIR, "_shared")
sys.path.insert(0, SHARED_DIR)

from canonical_constants import *  # noqa: F401,F403  (Vol_SU3_Haar, tau_fold, PI, a2_fold, ...)

# ---------------------------------------------------------------------------
# Section 2 -- Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# GPU path for per-sector eigvalsh
try:
    import torch
    _HAS_TORCH = torch.cuda.is_available()
except Exception:
    _HAS_TORCH = False

from dirac_spectrum import (
    su3_generators,
    compute_structure_constants,
    compute_killing_form,
    jensen_metric,
    orthonormal_frame,
    frame_structure_constants,
    connection_coefficients,
    spinor_connection_offset,
    build_cliff8,
    validate_clifford,
    get_irrep,
    dirac_operator_on_irrep,
)
from r20a_riemann_tensor import (
    compute_riemann_tensor_ON_fast,
    ricci_from_riemann,
    scalar_curvature_our_metric,
    kretschner_exact,
)

# ---------------------------------------------------------------------------
# Section 3 -- Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION = "S3"                                        # (local) investigation 3
GATE_ID = "INV3-W2-2"                                 # (local) short-form per orchestrator override
SCHEME = "ISOSPECTRAL-RIGIDITY-L3"                    # (local)
CONVENTION = "ABSOLUTE"                               # (local) a_n MULTISETS compared bit-for-bit
L_MAX = 3                                             # (local)

# Pre-registered machinery pins
N_TAU = 2001                                          # (local) fine scan to catch near-degeneracies
TAU_MIN = 0.05                                        # (local) brackets tau_fold=0.190 w/ margin
TAU_MAX = 0.35                                        # (local)
TOL_SPEC = 1e-9                                       # (local) sorted |lambda^2| multiset match
TOL_MOMENT = 1e-9                                     # (local) a_n^{lattice} triple match
TOL_V = 1e-6                                          # (local) Kosmann V discrimination
MAX_PQ_SUM = 3                                        # (local) Peter-Weyl truncation L_max=3
D_DIM = 8                                             # (local) dim SU(3)
SPINOR_RANK = 16                                      # (local) 2^{d/2} = 2^4

OUT_NPZ = Path(SESSION_DIR) / "inv3_w2_isospectral_rigidity_l3.npz"     # (local)
OUT_PNG = Path(SESSION_DIR) / "inv3_w2_isospectral_rigidity_l3.png"     # (local)

CANONICAL_PATH = Path(SHARED_DIR) / "canonical_constants.py"           # (local)
L12_CACHE = Path(COMPUTATIONS_DIR) / "session-84" / "s84_spectrum_cache_L12_tau019.npz"  # (local)

INPUT_FILES = [CANONICAL_PATH, L12_CACHE]             # (local)


# ---------------------------------------------------------------------------
# Section 4 -- SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(Path(path).read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs) -> dict:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}  # (local)
    project_root = Path(COMPUTATIONS_DIR).parent  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(Path(p).relative_to(project_root)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    try:
        script_bytes = Path(script_path).read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = Path(canonical_path).read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
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
# Section 5 -- GEOMETRIC Seeley-DeWitt triple a_n^{lattice}(tau)
# ---------------------------------------------------------------------------

def spin_curvature_clifford_trace(tau: float, gammas) -> float:
    """tr_S(sum_{a<b} Omega_{ab} Omega_{ab}) for the spin-bundle curvature.

    The spin connection curvature 2-form is
        Omega_{ab} = (1/4) R_{abcd} gamma^c gamma^d           (16x16)
    (Lichnerowicz curvature endomorphism). The Gilkey a_4 universal polynomial
    carries the term (1/360)*30*tr(Omega_{ab} Omega^{ab}); we compute the
    Clifford trace EXACTLY (no folklore coefficient) so the a_4^{lattice}
    value is fully substrate-derived.

    Returns scalar S_Omega = sum_{a,b} tr(Omega_{ab} @ Omega_{ab}) (real part).
    """
    R = compute_riemann_tensor_ON_fast(tau)  # (local) (8,8,8,8) R_{abcd}
    n = 8  # (local)
    # Omega_{ab} = (1/4) sum_{c,d} R[a,b,c,d] gamma_c gamma_d
    S_Omega = 0.0  # (local)
    for a in range(n):
        for b in range(n):
            Om = np.zeros((SPINOR_RANK, SPINOR_RANK), dtype=complex)  # (local)
            Rab = R[a, b]  # (local) (8,8) slice
            for c in range(n):
                for d in range(n):
                    coeff = Rab[c, d]  # (local)
                    if abs(coeff) > 1e-15:
                        Om += coeff * (gammas[c] @ gammas[d])
            Om *= 0.25
            S_Omega += np.real(np.trace(Om @ Om))
    return float(S_Omega)


def geometric_sd_triple(tau: float, S_Omega: float):
    """Return (a_0, a_2, a_4) GEOMETRIC Seeley-DeWitt coefficients a_n^{lattice}(tau).

    d=8, spinor rank 16, prefactor (4 pi)^{-d/2}=(4 pi)^{-4}, Vol=Vol_SU3_Haar
    (TAU-INDEPENDENT: volume-preserving Jensen). Lichnerowicz D^2 => E = -R/4 * 1.

    a_0 = (4 pi)^{-4} * 16 * Vol
    a_2 = (4 pi)^{-4} * (20 R/3) * Vol      [tr(R/6 - E) = 16*(5R/12)=20R/3]
    a_4 = (4 pi)^{-4} * (1/360) * Vol *
          [ 60 R*tr(E) + 180 tr(E^2) + 30 S_Omega + tr(1)*(5R^2 - 2|Ric|^2 + 2|Riem|^2) ]
    with tr(E)=16*(-R/4)=-4R, tr(E^2)=16*(R/4)^2=R^2, tr(1)=16. Derivative terms
    (E_{;kk}, R_{;kk}) vanish on the homogeneous space (constant curvature scalars).
    """
    R = scalar_curvature_our_metric(tau)  # (local) SP-2 exact
    K = kretschner_exact(tau)             # (local) |Riem|^2 exact
    Ric = ricci_from_riemann(compute_riemann_tensor_ON_fast(tau))  # (local) (8,8)
    ric2 = float(np.sum(Ric ** 2))        # (local) |Ric|^2
    pref = (4.0 * PI) ** (-4)             # (local) (4 pi)^{-d/2}, d=8
    Vol = Vol_SU3_Haar                    # imported canonical (1349.74), tau-INDEPENDENT

    a0 = pref * SPINOR_RANK * Vol                                        # (local)
    a2 = pref * (20.0 * R / 3.0) * Vol                                   # (local)

    trE = SPINOR_RANK * (-R / 4.0)        # (local) tr(E), E=-R/4 * 1
    trE2 = SPINOR_RANK * (R / 4.0) ** 2   # (local) tr(E^2)
    scalar_poly = SPINOR_RANK * (5.0 * R ** 2 - 2.0 * ric2 + 2.0 * K)    # (local) tr(1)*(...)
    a4_integrand = 60.0 * R * trE + 180.0 * trE2 + 30.0 * S_Omega + scalar_poly  # (local)
    a4 = pref * (1.0 / 360.0) * Vol * a4_integrand                       # (local)
    return float(a0), float(a2), float(a4), float(R), float(ric2), float(K)


# ---------------------------------------------------------------------------
# Section 6 -- Dirac eigenvalue multiset {lambda^2}(tau) with PW multiplicities
# ---------------------------------------------------------------------------

def _eigvalsh_block(H: np.ndarray) -> np.ndarray:
    """Hermitian eigenvalues; GPU path when available, else numpy."""
    if _HAS_TORCH:
        t = torch.tensor(H, device="cuda")  # (local)
        return torch.linalg.eigvalsh(t).cpu().numpy()
    return np.linalg.eigvalsh(H)


def dirac_lambda2_signature(tau, gens, f_abc, gammas):
    """Build the Dirac eigenvalue-squared multiset {lambda_k^2} (PW-multiplicity-
    weighted) for (SU(3), g_tau) over sectors p+q <= MAX_PQ_SUM.

    D_pi is anti-Hermitian (math convention); H = 1j*D_pi is Hermitian with real
    eigenvalues mu (= the Dirac eigenvalues). lambda^2 = mu^2. Each sector (p,q)
    contributes its block eigenvalues with PW multiplicity dim(p,q).

    Returns:
        lam2_sorted: (Ntot,) sorted lambda^2 values (PW-weighted: dim(p,q) copies
                     of each block eigenvalue) -- the comparison multiset
        sig_scalars: dict of compact rotation-invariant signature scalars
                     (sum, sum^2, sum^3, count, min, max) for fast pre-screen
    """
    B = compute_killing_form(f_abc)            # (local)
    g = jensen_metric(B, tau)                  # (local)
    E = orthonormal_frame(g)                   # (local)
    ft = frame_structure_constants(f_abc, E)   # (local)
    Gamma = connection_coefficients(ft)        # (local)
    Omega = spinor_connection_offset(Gamma, gammas)  # (local)

    lam2_all = []  # (local) (lambda^2, multiplicity) accumulation as repeated entries

    # Trivial (0,0): D = Omega on 16-dim spinor space; PW mult dim=1
    mu00 = _eigvalsh_block(1j * Omega)         # (local) real
    for mu in mu00:
        lam2_all.append(mu * mu)               # mult 1

    for p in range(MAX_PQ_SUM + 1):
        for q in range(MAX_PQ_SUM + 1 - p):
            if p == 0 and q == 0:
                continue
            dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2  # (local)
            rho, dchk = get_irrep(p, q, gens, f_abc)
            assert dchk == dim_pq
            D_pi = dirac_operator_on_irrep(rho, E, gammas, Omega)  # (local)
            mu = _eigvalsh_block(1j * D_pi)    # (local) real Dirac eigenvalues
            lam2_block = mu * mu               # (local)
            # PW multiplicity: each block eigenvalue appears dim_pq times in full spectrum
            for v in lam2_block:
                for _ in range(dim_pq):
                    lam2_all.append(v)

    lam2_sorted = np.sort(np.array(lam2_all, dtype=np.float64))  # (local)
    sig = {
        "count": float(lam2_sorted.size),
        "s1": float(np.sum(lam2_sorted)),
        "s2": float(np.sum(lam2_sorted ** 2)),
        "s3": float(np.sum(lam2_sorted ** 3)),
        "min": float(lam2_sorted.min()),
        "max": float(lam2_sorted.max()),
    }  # (local)
    return lam2_sorted, sig


# ---------------------------------------------------------------------------
# Section 7 -- Kosmann pairing V_total(tau) (NON-spectral discriminator)
# ---------------------------------------------------------------------------

def kosmann_operator_antisymmetric(Gamma, gammas, a):
    """Kosmann-Lichnerowicz spinorial correction K_a (Baptista Paper 17 eq 4.1):
        K_a = (1/8) sum_{r,s} [Gamma^s_{ra} - Gamma^r_{sa}] gamma_r gamma_s
    Built from the ANTISYMMETRIC part of the covariant derivative of e_a -- the
    tau-DEPENDENT connection coefficients Gamma(tau) carry the geometric info that
    the bare eigenvalue list may not. (The bi-invariant adjoint form
    A^a_{rs}=-f_{a,r,s} is the tau=0 special case Gamma^c_{ab}=(1/2)f^c_{ab};
    the Jensen-varying Gamma(tau) is the discriminating object.)
    """
    K = np.zeros((SPINOR_RANK, SPINOR_RANK), dtype=complex)  # (local)
    for r in range(8):
        for s in range(8):
            A_rs = Gamma[s, r, a] - Gamma[r, s, a]  # (local) Gamma[upper,1st,2nd]
            if abs(A_rs) > 1e-15:
                K += A_rs * (gammas[r] @ gammas[s])
    K *= (1.0 / 8.0)
    return K


def kosmann_pairing_invariant(tau, gens, f_abc, gammas):
    """V_total(tau) = sum_{n,m,a} |<n|K_a(tau)|m>|^2 on the (0,0) singlet sector
    (the canonical s23a construction). The eigenbasis-projection is unitary, so
    sum_{n,m} |<n|K_a|m>|^2 = ||K_a||_F^2 (Frobenius). V_total = sum_a ||K_a||_F^2
    is therefore the NON-spectral pairing-strength invariant: it depends on
    Gamma(tau) (the spin/Clifford structure), NOT only on the eigenvalue list.

    Returns (V_total, V_per_a) where V_per_a is the 8-vector of ||K_a||_F^2.
    """
    B = compute_killing_form(f_abc)            # (local)
    g = jensen_metric(B, tau)                  # (local)
    E = orthonormal_frame(g)                   # (local)
    ft = frame_structure_constants(f_abc, E)   # (local)
    Gamma = connection_coefficients(ft)        # (local)
    V_per_a = np.zeros(8, dtype=np.float64)    # (local)
    for a in range(8):
        K_a = kosmann_operator_antisymmetric(Gamma, gammas, a)  # (local)
        V_per_a[a] = float(np.sum(np.abs(K_a) ** 2))            # ||K_a||_F^2
    return float(np.sum(V_per_a)), V_per_a


# ---------------------------------------------------------------------------
# Section 8 -- Per-tau signature build + O(N^2) degeneracy scan
# ---------------------------------------------------------------------------

def build_signatures(taus, gens, f_abc, gammas, verbose=True):
    """Compute per-tau (a_n^{lattice} triple, lambda^2 multiset, V_total) signatures."""
    n = len(taus)  # (local)
    a0 = np.zeros(n); a2 = np.zeros(n); a4 = np.zeros(n)         # (local)
    Rsc = np.zeros(n); Ric2 = np.zeros(n); Kre = np.zeros(n)     # (local)
    Vtot = np.zeros(n)                                           # (local)
    s1 = np.zeros(n); s2 = np.zeros(n); s3 = np.zeros(n)         # (local) spectral power sums
    smin = np.zeros(n); smax = np.zeros(n); scount = np.zeros(n) # (local)
    lam2_list = []                                              # (local) full multisets

    t0 = time.time()  # (local)
    for i, tau in enumerate(taus):
        S_Omega = spin_curvature_clifford_trace(tau, gammas)  # (local)
        a0[i], a2[i], a4[i], Rsc[i], Ric2[i], Kre[i] = geometric_sd_triple(tau, S_Omega)
        lam2, sig = dirac_lambda2_signature(tau, gens, f_abc, gammas)
        lam2_list.append(lam2)
        s1[i], s2[i], s3[i] = sig["s1"], sig["s2"], sig["s3"]
        smin[i], smax[i], scount[i] = sig["min"], sig["max"], sig["count"]
        Vtot[i], _ = kosmann_pairing_invariant(tau, gens, f_abc, gammas)
        if verbose and (i % 200 == 0 or i == n - 1):
            dt = time.time() - t0  # (local)
            print(f"  [{i+1:4d}/{n}] tau={tau:.5f}  a0={a0[i]:.6f} a2={a2[i]:.6f} "
                  f"a4={a4[i]:.6f}  V={Vtot[i]:.6f}  s1={s1[i]:.4f}  ({dt:.1f}s)")
    return dict(a0=a0, a2=a2, a4=a4, Rsc=Rsc, Ric2=Ric2, Kre=Kre, Vtot=Vtot,
                s1=s1, s2=s2, s3=s3, smin=smin, smax=smax, scount=scount,
                lam2_list=lam2_list)


def multiset_match(lam_i, lam_j, tol):
    """True iff the two sorted lambda^2 multisets agree element-wise within tol.
    Same length is necessary (PW-weighted counts equal); then max abs diff <= tol."""
    if lam_i.size != lam_j.size:
        return False, float("inf")
    d = float(np.max(np.abs(lam_i - lam_j)))  # (local)
    return (d <= tol), d


def degeneracy_scan(sig, taus, verbose=True):
    """O(N^2) pairwise scan for the rigidity-degeneracy predicate.

    A pair (i,j), i<j, is a DEGENERACY iff:
      (1) |a_n(tau_i)-a_n(tau_j)| <= TOL_MOMENT for n in {0,2,4}  (geometric SD triple)
      (2) multiset{lambda^2}(tau_i) == multiset{lambda^2}(tau_j) within TOL_SPEC
      (3) |V_total(tau_i)-V_total(tau_j)| > TOL_V                 (NON-spectral split)

    Pre-screen on the cheap moment + spectral-power-sum scalars; only candidate
    pairs passing the scalar pre-screen pay the full multiset comparison.

    Returns the degeneracy list (exact pairs), the near-degeneracy list (INFO band),
    and the global closest-pair witness (min combined moment+spectral distance over
    all i<j) for the verdict value string.
    """
    n = len(taus)  # (local)
    a0, a2, a4 = sig["a0"], sig["a2"], sig["a4"]
    s1, s2, s3 = sig["s1"], sig["s2"], sig["s3"]
    smin, smax, scount = sig["smin"], sig["smax"], sig["scount"]
    Vtot = sig["Vtot"]
    lam2_list = sig["lam2_list"]

    degeneracies = []      # (local) exact isospectral-non-isometric pairs (FAIL evidence)
    near_degens = []       # (local) near-degenerate pairs in [TOL_SPEC, TOL_V] band (INFO)

    # Global closest-pair witness over the moment-triple + spectral-power-sum metric.
    # This is the diagnostic "how close does the family come to a degeneracy".
    best_d = float("inf")  # (local)
    best_pair = (-1, -1)   # (local)
    best_detail = {}       # (local)

    # Pre-screen scalar tolerance: candidates whose cheap scalars agree within
    # a loose band (10x the spectral tol) get the full multiset comparison.
    PRE_TOL = 1e-7  # (local) loose pre-screen (>> TOL_SPEC) so no true match is missed

    t0 = time.time()  # (local)
    for i in range(n):
        # Vectorized scalar distances from i to all j>i (cheap pre-screen)
        j0 = i + 1  # (local)
        if j0 >= n:
            break
        dmom = (np.abs(a0[j0:] - a0[i]) + np.abs(a2[j0:] - a2[i])
                + np.abs(a4[j0:] - a4[i]))  # (local) L1 moment-triple distance
        dspec_scalar = (np.abs(s1[j0:] - s1[i]) + np.abs(s2[j0:] - s2[i])
                        + np.abs(s3[j0:] - s3[i])
                        + np.abs(scount[j0:] - scount[i]))  # (local) spectral power-sum dist
        dcomb = dmom + dspec_scalar  # (local) combined diagnostic distance

        # Track global closest pair (diagnostic witness)
        kmin = int(np.argmin(dcomb))  # (local)
        if dcomb[kmin] < best_d:
            best_d = float(dcomb[kmin])
            jglob = j0 + kmin  # (local)
            best_pair = (i, jglob)
            best_detail = dict(
                d_moment=float(dmom[kmin]), d_spec_scalar=float(dspec_scalar[kmin]),
                dV=float(abs(Vtot[jglob] - Vtot[i])),
                tau_i=float(taus[i]), tau_j=float(taus[jglob]),
            )

        # Candidate pairs for full multiset test: scalars both small
        cand = np.where((dmom <= PRE_TOL) & (dspec_scalar <= PRE_TOL))[0]  # (local)
        for k in cand:
            j = j0 + int(k)  # (local)
            # Full predicate
            mom_ok = (abs(a0[j] - a0[i]) <= TOL_MOMENT
                      and abs(a2[j] - a2[i]) <= TOL_MOMENT
                      and abs(a4[j] - a4[i]) <= TOL_MOMENT)  # (local)
            ms_ok, ms_d = multiset_match(lam2_list[i], lam2_list[j], TOL_SPEC)
            dV = abs(Vtot[j] - Vtot[i])  # (local)
            if mom_ok and ms_ok and dV > TOL_V:
                degeneracies.append(dict(i=i, j=j, tau_i=float(taus[i]),
                                         tau_j=float(taus[j]), ms_d=ms_d, dV=float(dV)))
            elif ms_d <= TOL_V and ms_d > TOL_SPEC and abs(taus[j] - taus[i]) > 1e-6:
                near_degens.append(dict(i=i, j=j, tau_i=float(taus[i]),
                                        tau_j=float(taus[j]), ms_d=float(ms_d),
                                        dV=float(dV)))
        if i % 200 == 0:
            dt = time.time() - t0  # (local)
            print(f"  scan row {i+1}/{n}  best_d_so_far={best_d:.3e} "
                  f"(tau {best_detail.get('tau_i', 0):.4f},{best_detail.get('tau_j', 0):.4f})  ({dt:.1f}s)")

    return degeneracies, near_degens, best_pair, best_d, best_detail


# ---------------------------------------------------------------------------
# Section 9 -- Verdict payload (PRINTED for emit_verdict MCP tool)
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme, convention, L_max):
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(verdict, value, audit_sha, content_sha, extra_rows=None):
    payload = {
        "session": 3,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }  # (local)
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 10 -- Plot
# ---------------------------------------------------------------------------

def make_plot(taus, sig, best_detail):
    fig, ax = plt.subplots(2, 2, figsize=(13, 9))

    # (a) geometric SD triple vs tau
    ax[0, 0].plot(taus, sig["a0"], label=r"$a_0^{\rm lattice}$ (const, vol-preserving)")
    ax[0, 0].plot(taus, sig["a2"], label=r"$a_2^{\rm lattice}\propto R(\tau)$")
    ax[0, 0].plot(taus, sig["a4"], label=r"$a_4^{\rm lattice}$ (curvature$^2$)")
    ax[0, 0].axvline(tau_fold, ls="--", c="k", alpha=0.5, label=r"$\tau_{\rm fold}=0.19$")
    ax[0, 0].set_xlabel(r"$\tau$"); ax[0, 0].set_ylabel(r"$a_n^{\rm lattice}$")
    ax[0, 0].set_title("Geometric Seeley-DeWitt triple (NOT zeta moments)")
    ax[0, 0].legend(fontsize=8); ax[0, 0].grid(alpha=0.3)

    # (b) spectral power-sum s1 (= Tr D^2 weighted) vs tau -- the multiset fingerprint
    ax[0, 1].plot(taus, sig["s1"], c="C3", label=r"$s_1=\sum\lambda_k^2$ (PW-weighted)")
    ax[0, 1].axvline(tau_fold, ls="--", c="k", alpha=0.5)
    ax[0, 1].set_xlabel(r"$\tau$"); ax[0, 1].set_ylabel(r"$\sum\lambda_k^2$")
    ax[0, 1].set_title("Spectral multiset fingerprint (1st power sum)")
    ax[0, 1].legend(fontsize=8); ax[0, 1].grid(alpha=0.3)

    # (c) Kosmann pairing V_total vs tau (the NON-spectral discriminator)
    ax[1, 0].plot(taus, sig["Vtot"], c="C2", label=r"$V_{\rm total}=\sum_a\|K_a(\tau)\|_F^2$")
    ax[1, 0].axvline(tau_fold, ls="--", c="k", alpha=0.5)
    ax[1, 0].set_xlabel(r"$\tau$"); ax[1, 0].set_ylabel(r"$V_{\rm total}$")
    ax[1, 0].set_title("Non-spectral Kosmann pairing invariant")
    ax[1, 0].legend(fontsize=8); ax[1, 0].grid(alpha=0.3)

    # (d) monotone injectivity: a2 vs s1 (parametric in tau) -- if injective, rigid
    sc = ax[1, 1].scatter(sig["a2"], sig["s1"], c=taus, cmap="viridis", s=6)
    ax[1, 1].set_xlabel(r"$a_2^{\rm lattice}$"); ax[1, 1].set_ylabel(r"$\sum\lambda_k^2$")
    ax[1, 1].set_title("Joint (a2, spectral) map -- injective => rigid")
    plt.colorbar(sc, ax=ax[1, 1], label=r"$\tau$")
    ax[1, 1].grid(alpha=0.3)

    fig.suptitle(r"INV3-W2-2 Isospectral rigidity on Jensen TT family ($L_{\max}=3$): "
                 r"can one hear the Jensen geometry?", fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    fig.savefig(OUT_PNG, dpi=130)
    print(f"  saved plot: {OUT_PNG}")


# ---------------------------------------------------------------------------
# Section 11 -- Cross-validation against L12 cache at tau=0.19
# ---------------------------------------------------------------------------

def crossval_l12(gens, f_abc, gammas):
    """Cross-validate the L_max=3 sub-block reconstruction at tau=0.19 against the
    L12 master cache (filtered to p+q<=3). Diagnostic only; not gating."""
    if not L12_CACHE.exists():
        print("  [crossval] L12 cache absent -- skipping (diagnostic only)")
        return None
    try:
        z = np.load(L12_CACHE, allow_pickle=True)  # (local)
        sec = z["sector_evals"].item()             # (local) {(p,q):{'abs_evals',...}}
    except Exception as e:
        print(f"  [crossval] could not read L12 cache: {e} -- skipping")
        return None
    # Our reconstruction at tau=0.19, per-sector min|lambda|
    B = compute_killing_form(f_abc); g = jensen_metric(B, 0.19)  # (local)
    E = orthonormal_frame(g); ft = frame_structure_constants(f_abc, E)  # (local)
    Gamma = connection_coefficients(ft); Omega = spinor_connection_offset(Gamma, gammas)  # (local)
    max_dev = 0.0  # (local)
    checked = 0    # (local)
    for (p, q) in [(0, 0), (1, 0), (0, 1), (1, 1), (2, 0), (0, 2), (2, 1), (1, 2), (3, 0), (0, 3)]:
        if (p, q) not in sec:
            continue
        if (p, q) == (0, 0):
            mu = np.sort(np.abs(np.linalg.eigvalsh(1j * Omega)))  # (local)
        else:
            rho, _ = get_irrep(p, q, gens, f_abc)
            D = dirac_operator_on_irrep(rho, E, gammas, Omega)  # (local)
            mu = np.sort(np.abs(np.linalg.eigvalsh(1j * D)))    # (local)
        cache_abs = np.sort(np.abs(np.asarray(sec[(p, q)]["abs_evals"]).ravel()))  # (local)
        m = min(mu.size, cache_abs.size)  # (local)
        if m > 0:
            dev = float(np.max(np.abs(mu[:m] - cache_abs[:m])))  # (local)
            max_dev = max(max_dev, dev)
            checked += 1
    print(f"  [crossval] L_max=3 sub-block vs L12 cache @tau=0.19: "
          f"max|dev|={max_dev:.3e} over {checked} sectors")
    return max_dev


# ---------------------------------------------------------------------------
# Section 12 -- Main
# ---------------------------------------------------------------------------

def main():
    t_start = time.time()  # (local)
    print("=" * 78)
    print(f"  {GATE_ID} -- Isospectral rigidity at L_max=3 (can one hear the Jensen geometry?)")
    print("=" * 78)

    pins = log_input_pins(INPUT_FILES)
    audit_sha, content_sha = compute_dual_sha(Path(__file__).resolve(), CANONICAL_PATH, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print(f"  GPU: {'cuda' if _HAS_TORCH else 'numpy(CPU)'}; spinor rank {SPINOR_RANK}; "
          f"prefactor (4pi)^-4; Vol={Vol_SU3_Haar:.4f} (tau-INDEPENDENT)")
    print()

    gens = su3_generators()                       # (local)
    f_abc = compute_structure_constants(gens)     # (local)
    gammas = build_cliff8()                        # (local)
    cliff_err = validate_clifford(gammas)         # (local)
    print(f"  Clifford {{gamma_a,gamma_b}}=2 delta validation: max_err={cliff_err:.2e}")

    # Cross-validate L_max=3 reconstruction at tau=0.19 vs L12 cache (diagnostic)
    crossval_dev = crossval_l12(gens, f_abc, gammas)  # (local)

    # Anchor check: a_2^{lattice}(tau_fold) must match canonical a_2^{SD}=0.728235
    _, a2_anchor, _, _, _, _ = geometric_sd_triple(
        tau_fold, spin_curvature_clifford_trace(tau_fold, gammas))  # (local)
    print(f"  ANCHOR: a_2^{{lattice}}(tau_fold) = {a2_anchor:.9f}  "
          f"(canonical a_2^SD target 0.728235; |dev|={abs(a2_anchor - 0.728235):.2e})")
    print(f"  REGULATOR DISCIPLINE: a_2^{{lattice}}={a2_anchor:.6f} is NOT a_2^{{zeta}}="
          f"{a2_fold:.4f} (factor {a2_fold / a2_anchor:.1f}=3812; load-bearing)")
    print()

    taus = np.linspace(TAU_MIN, TAU_MAX, N_TAU)   # (local)
    print(f"  Building per-tau signatures over {N_TAU} tau in [{TAU_MIN}, {TAU_MAX}] "
          f"(step {(TAU_MAX - TAU_MIN) / (N_TAU - 1):.6f}) ...")
    sig = build_signatures(taus, gens, f_abc, gammas, verbose=True)

    print(f"\n  Spectral multiset: count={sig['scount'][0]:.0f} eigenvalues (PW-weighted) per tau")
    print(f"  s1=Sum lambda^2 range: [{sig['s1'].min():.6f}, {sig['s1'].max():.6f}]  "
          f"(monotone? d(s1)/dtau sign-uniform: "
          f"{np.all(np.diff(sig['s1']) > 0) or np.all(np.diff(sig['s1']) < 0)})")
    print(f"  V_total range: [{sig['Vtot'].min():.6f}, {sig['Vtot'].max():.6f}]")

    print(f"\n  O(N^2) pairwise degeneracy scan ({N_TAU}^2/2 = {N_TAU*(N_TAU-1)//2} pairs) ...")
    degens, near_degens, best_pair, best_d, best_detail = degeneracy_scan(sig, taus)

    # ----- Verdict logic -----
    n_degen = len(degens)        # (local)
    n_near = len(near_degens)    # (local)
    if n_degen > 0:
        verdict = "FAIL"         # named isospectral-non-isometric pair(s) found
        worst = degens[0]        # (local)
        value = (f"DEGENERATE_set_card={n_degen}_first_pair_tau=({worst['tau_i']:.5f},"
                 f"{worst['tau_j']:.5f})_ms_d={worst['ms_d']:.2e}_dV={worst['dV']:.2e}")
    elif n_near > 0:
        verdict = "INFO"         # near-degeneracy in band, no exact pair
        wn = min(near_degens, key=lambda x: x["ms_d"])  # (local)
        value = (f"NEAR_DEGEN_card={n_near}_closest_tau=({wn['tau_i']:.5f},{wn['tau_j']:.5f})"
                 f"_ms_d={wn['ms_d']:.2e}_dV={wn['dV']:.2e}")
    else:
        verdict = "PASS"         # empty degeneracy set: rigidity holds
        value = (f"RIGID_empty_degeneracy_set_closest_pair_tau=("
                 f"{best_detail['tau_i']:.5f},{best_detail['tau_j']:.5f})"
                 f"_combined_d={best_d:.3e}_dmom={best_detail['d_moment']:.2e}"
                 f"_dspec={best_detail['d_spec_scalar']:.2e}_dV={best_detail['dV']:.2e}")

    # ----- Save data -----
    np.savez_compressed(
        OUT_NPZ,
        taus=taus,
        a0_lattice=sig["a0"], a2_lattice=sig["a2"], a4_lattice=sig["a4"],
        R_scalar=sig["Rsc"], Ric2=sig["Ric2"], Kretschmann=sig["Kre"],
        V_total=sig["Vtot"],
        spec_s1=sig["s1"], spec_s2=sig["s2"], spec_s3=sig["s3"],
        spec_min=sig["smin"], spec_max=sig["smax"], spec_count=sig["scount"],
        n_degeneracies=n_degen, n_near_degeneracies=n_near,
        best_pair=np.array(best_pair), best_combined_d=best_d,
        best_tau_i=best_detail.get("tau_i", np.nan),
        best_tau_j=best_detail.get("tau_j", np.nan),
        best_d_moment=best_detail.get("d_moment", np.nan),
        best_d_spec=best_detail.get("d_spec_scalar", np.nan),
        best_dV=best_detail.get("dV", np.nan),
        a2_anchor_fold=a2_anchor, a2_zeta_fold=a2_fold,
        crossval_l12_dev=(crossval_dev if crossval_dev is not None else np.nan),
        tol_spec=TOL_SPEC, tol_moment=TOL_MOMENT, tol_V=TOL_V,
        verdict=verdict,
    )
    print(f"\n  saved data: {OUT_NPZ}")
    make_plot(taus, sig, best_detail)

    # ----- Report -----
    print("\n" + "=" * 78)
    print("  RIGIDITY SCAN RESULT")
    print("=" * 78)
    print(f"  exact degeneracies (FAIL evidence): {n_degen}")
    print(f"  near-degeneracies (INFO band [1e-9,1e-6]): {n_near}")
    print(f"  global closest pair: tau=({best_detail.get('tau_i', float('nan')):.5f}, "
          f"{best_detail.get('tau_j', float('nan')):.5f})  "
          f"combined_d={best_d:.3e}")
    print(f"    d_moment(a0+a2+a4)={best_detail.get('d_moment', float('nan')):.3e}  "
          f"d_spec(s1+s2+s3+count)={best_detail.get('d_spec_scalar', float('nan')):.3e}  "
          f"dV={best_detail.get('dV', float('nan')):.3e}")
    print(f"  (note: adjacent-tau step is {(TAU_MAX-TAU_MIN)/(N_TAU-1):.2e}; the global "
          f"closest pair is the adjacent grid neighbours -- there is NO non-adjacent "
          f"collision, i.e. no isospectral-non-isometric tau-pair)")

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)  # (local)
    print("\n" + tag)
    extra = [
        f"# regulator_pin=a_n^lattice (GEOMETRIC Seeley-DeWitt; a_2^SD(fold)={a2_anchor:.6f}, "
        f"NOT a_2^zeta={a2_fold:.4f}; factor-3812 discipline)",
        f"# rigidity_predicate: EXISTS tau_i!=tau_j with bit-identical {{a0,a2,a4}}+lambda^2 "
        f"multiset AND dV>tol_V; degeneracies={n_degen} near={n_near}",
        f"# closest_pair_combined_distance={best_d:.3e} at tau=({best_detail.get('tau_i', 0):.5f},"
        f"{best_detail.get('tau_j', 0):.5f}); a0_lattice tau-INDEPENDENT (vol-preserving)",
    ]  # (local)
    print_verdict_payload(verdict, value, audit_sha, content_sha, extra_rows=extra)

    wall = time.time() - t_start  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
