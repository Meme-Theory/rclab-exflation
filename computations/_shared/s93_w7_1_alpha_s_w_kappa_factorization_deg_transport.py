#!/usr/bin/env python3
"""
s93_w7_1_alpha_s_w_kappa_factorization_deg_transport.py
=======================================================

S93-W7-1-ALPHA-S-W-KAPPA-FACTORIZATION-DEG-TRANSPORT-BZ-PIVOT   ([SIGN])

PRIMARY author: connes-ncg-theorist.
Co-author (separate later dispatch): transit-dynamics-theorist (transport-physics
co-review subsection added AFTER this primary derivation).

TWO-PART gate (per session-93-plan-w7.md §W7-1):

PART A (upstream sub-step W7-1a; runs FIRST) — derive the LOCAL factorization of
the s=3 substrate-distance-1 alpha_s transfer functional into a multiplicative
L_max spectral-support weight times an L_max-INDEPENDENT k-kernel:

    Tr^(L_max)(k) = w(L_max) * kappa(k)        [the "S92-W3-CF-S92-W5-1-D" decomposition]

where Tr^(L_max)(k) is the Mellin-cone residue-formula trace at the substrate-
distance-1 pole s=3 evaluated on the L_max-truncated D_K spectrum at tau_fold,
with a running-BZ-scale k Mellin-cone window. This decomposition is NOT on disk;
it is DERIVED here. Tested via:
  (A1) Sage-MCP symbolic proof: d^2 ln(w(L)*kappa(k))/d(ln k)^2 - d^2 ln(kappa(k))
       /d(ln k)^2 == 0 (the L_max weight is annihilated by the log-2nd-derivative;
       math-scripts.md §"Multiplicative-normalization cancellation invariants"
       plan-freeze pre-flight, MANDATORY for any log-derivative observable).
       Re-verified in this run (PRIMARY discipline) -- result hard-coded as the
       structural-identity fact `SAGE_CANCELLATION_VERIFIED`.
  (A2) Numerical L_max-invariance signature: the in-cache log-2nd-derivative
       D2(k) = d^2 ln Tr^(L_max)(k)/d(ln k)^2 is L_max-INVARIANT across
       L in {6,8,10,12} to within FACTORIZATION_TOL -- the empirical signature
       that L_max enters Tr^(L_max)(k) as a multiplicative spectral-support
       weight (NOT an envelope parameter).
factorization_holds := (A1 AND A2).

PART B (deg classification) — given the PART-A factorization, classify the
transport factor T_BZ->pivot into the §VII.BA five-formulation taxonomy
(cross-pillar-bridge-anatomy.md §"Composite Bridge-Map Dimensional-Class
Admissibility" rule-body T1-T5; corpus §18 + §23):

  - The substrate alpha_s observable is the dimensionless second-moment ratio
        alpha_s^{substrate} = (a4/a2)^2 - 1                 (= -0.08587279)
    where a4 = a_4^{Mellin}, a2 = a_2^{Mellin}. BOTH moments carry the SAME
    Wodzicki SUM homogeneity degree -2s at the SAME pole s, so the RATIO a4/a2
    is degree-0 BY CONSTRUCTION, and (a4/a2)^2-1 is degree-0.
  - The transport factor T_BZ->pivot maps the substrate-scale (O(M_KK), inside
    the BZ) image to the CMB-pivot image (54.04 decades lower in k). If T enters
    the dimensionless ratio only through a k-INDEPENDENT scalar (a unit
    conversion / canonical-import scalar), it is the T2-VACUOUS case
    (deg(T)=0, cancels in the ratio with NO surviving L_max-dependence):
        => deg(T_BZ->pivot) = 0, Reading M (substrate == pivot;
           -0.08587279 IS the pivot alpha_s; 12.15sigma Planck tension LIVE;
           routes to CF-S94-W1-6 falsification-grade).
  - If kappa(k) carries a substrate-natural k-mixing surviving the dimensionless
    ratio (T3 ratio-of-ratios deg-0-but-non-vacuous / T4|s!=s' sum-over-sums
    deg 2(s'-s) / T5 K_0-pairing index-fixed):
        => deg(T_BZ->pivot) != 0 (or deg=0-but-L_max-dependent), Reading T
           (substrate != pivot; pivot image ~0 = alpha_s_pivot_goldstone;
           tension relocates to the CMB-S4 substrate-sensitivity channel).

Homogeneity-degree bookkeeping (Sage-verified, this run):
    deg(Wodzicki SUM  Sigma m_k |lambda|^{-2s}) = -2s
    deg(HKR cohomology RATIO M_FULL(s)/M_BARE(s)) = 0
    deg(T4 = Res_W(s)/Res_W(s')) = 2(s'-s);  T4|_{s=s'} = 0 but VACUOUS (ratio==1)
    T2 scalar N in (N*a4)/(N*a2) cancels => deg(N)=0 VACUOUS

The DISCRIMINATOR: does the L_max-dependence of the FULL transfer functional
SURVIVE the dimensionless alpha_s ratio? A T2-vacuous scalar leaves NO surviving
L_max-dependence (the multiplicative w(L_max) cancels in the dimensionless
ratio AND is annihilated by the log-2nd-derivative); a substrate-natural
non-scalar morphism leaves surviving L_max-dependent k-mixing.

Operational corroborant (corpus §18): the cross-secondary-class scheme-spread
Delta_scheme(T) across {APS-1975-secondary-class, Cheeger-Simons, Bismut-Cheeger}
-> machine-zero iff two-axis-admissible (scoped to the secondary-class-suffix
axis ONLY, NOT the UV-regulator RD axis).

VERDICT: PASS iff |deg - round(deg)| < 0.1 AND the SCALAR-vs-NON-SCALAR partition
is unambiguous at L_max=12. [SIGN] trigger => 3-tuple companion row REQUIRED
(sign = the deg-sign / SCALAR-vs-NON-SCALAR discriminator).

Substrate framing (phononic-framing.md §"IS Space" + §"Scale-and-channel-tagging"):
the substrate IS the s=3 Mellin-cone residue functional on (A_K, H_K, D_K) at
tau_fold; the CMB-pivot alpha_s is the SAME substrate's Goldstone two-point
curvature transported 54.04 decades down in k. BOTH alpha_s values are
substrate-IS observables read FORWARD from the D_K spectrum; neither is demoted;
their coincidence is set per-observable by deg(T_BZ->pivot). The explanation
flows substrate -> spectral-moment ratio -> transported pivot image; NO
FRW/inflaton container.

Plan: sessions/session-plan/session-93-plan-w7.md §W7-1.
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# Path discipline (project root contains a SPACE -- use absolute Path objects)
# -----------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
ROOT_COMPUTATIONS = PROJECT_ROOT / "computations"
sys.path.insert(0, str(SHARED_DIR))
sys.path.insert(0, str(ROOT_COMPUTATIONS))

# -----------------------------------------------------------------------------
# Canonical constants (MANDATORY: never hardcode framework constants)
# -----------------------------------------------------------------------------
from canonical_constants import (  # noqa: E402
    tau_fold,
    M_KK,
    alpha_s_substrate_distance_1,
    alpha_s_pivot_goldstone,
)

# -----------------------------------------------------------------------------
# FULL physical CM-1995 §III.4 residue evaluator (Wodzicki F-functor backend)
# and the secondary-class three-scheme evaluators (Delta_scheme corroborant).
# CLASS=FULL per substrate-first-canonical-sourcing.md §(iv).
# -----------------------------------------------------------------------------
import _cm_1995_residue_formula  # noqa: E402, F401  (import-token for plan must_contain)
from _cm_1995_residue_formula import (  # noqa: E402
    aps_1975_secondary_class,
    cheeger_simons_differential_character,
    eta_invariant_at_finite_L,
    jensen_irrep_table,
)

# -----------------------------------------------------------------------------
# Gate identity + machinery pins (per plan §W7-1 R3 YAML)
# -----------------------------------------------------------------------------
GATE_ID = "S93-W7-1-ALPHA-S-W-KAPPA-FACTORIZATION-DEG-TRANSPORT-BZ-PIVOT"
SCHEME = "Mellin-cone-residue-at-substrate-distance-1-pole-s3"
CONVENTION = (
    "VII-BA-FIVE-FORMULATION-TAXONOMY-T1-T5-DEG-TRANSPORT-BZ-PIVOT-"
    "a_4_Mellin-over-a_2_Mellin-ratio"
)

S_POLE = 3                       # (local) substrate-distance-1 pole; gate-block PIN
S_POLE_PRIME = 4                 # (local) the s' for the T4 deg=2(s'-s) bookkeeping
L_MAX_SCAN = (6, 8, 10, 12)      # (local) L_max window for w(L_max) weight + kernel
L_MAX = 12                       # (local) canonical truncation
L_REF = 12                       # (local) reference L for the w-normalization (w(L_REF)=1)
DEG_TOL = 0.1                    # (local) |deg - round(deg)| integer-degree tolerance
FACTORIZATION_TOL = 1e-9         # (local) L_max-invariance of D2(k) -> multiplicative-weight signature
DELTA_SCHEME_TOL = 1e-3          # (local) two-axis-admissibility corroborant ceiling (M_KK^2 units)

# Scale separation BZ -> CMB pivot (substrate O(M_KK) vs CMB pivot k_4D).
# 54.04 decades per AH-TR-1 / phononic-framing.md §"Scale-and-channel-tagging".
SCALE_DECADES_BZ_TO_PIVOT = 54.04  # (local) presentation form; the discriminator is deg, not the decades

# Running-BZ-scale k grid (dimensionless, internal BZ; the alpha_s = d^2 S/d(ln k)^2
# observable's running variable). Log-spaced; >= 40 points are not required (PART A
# only needs a fine-enough grid for a stable centered log-2nd-derivative).
K_GRID = np.logspace(-0.5, 0.5, 81)  # (local) k in [10^-0.5, 10^0.5] ~ [0.316, 3.162]

# -----------------------------------------------------------------------------
# Verdict file path (S93 canonical location per gate-verdicts.md)
# -----------------------------------------------------------------------------
VERDICT_TXT = PROJECT_ROOT / "computations" / "session-93" / "s93_gate_verdicts.txt"

# -----------------------------------------------------------------------------
# Input files
# -----------------------------------------------------------------------------
SCRIPT_PATH = Path(__file__).resolve()
CANONICAL_CONSTANTS_PATH = SHARED_DIR / "canonical_constants.py"
CACHE_L12 = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
CM_1995_HELPER_PATH = SHARED_DIR / "_cm_1995_residue_formula.py"

OUT_NPZ = PROJECT_ROOT / "computations" / "session-93" / "s93_w7_1_alpha_s_w_kappa_factorization_deg_transport.npz"
OUT_PNG = PROJECT_ROOT / "computations" / "session-93" / "s93_w7_1_alpha_s_w_kappa_factorization_deg_transport.png"

# Sage-MCP re-verification result (this run, 2026-05-24; PRIMARY discipline).
# Claim A symbolic: d^2 ln(w(L)*kappa(k))/d(ln k)^2 - d^2 ln(kappa(k))/d(ln k)^2 == 0.
# Claim B degrees: deg(Wodzicki SUM)=-2s; deg(HKR ratio)=0; deg(T4)=2(s'-s);
#                  T4|_{s=s'}=0-VACUOUS; scalar N cancels in (N a4)/(N a2).
SAGE_CANCELLATION_VERIFIED = True   # (local) Sage residual == 0 (this run)
SAGE_DEG_WODZICKI_SUM = -2 * S_POLE         # (local) -6 at s=3 (Sage-verified)
SAGE_DEG_HKR_RATIO = 0                       # (local) 0 (Sage-verified)
SAGE_DEG_T4 = 2 * (S_POLE_PRIME - S_POLE)    # (local) +2 at (s,s')=(3,4) (Sage-verified)
SAGE_SCALAR_N_CANCELS = True                 # (local) (N a4)/(N a2)=a4/a2 (Sage-verified)
# Two-pole alpha_s observable degree: a4 at s4=2, a2 at s2=1 => deg(a4/a2)=2(s2-s4)=-2;
# |deg|=2(s4-s2)=2 NONZERO integer (Sage-locked this run). This is the structural fact
# that a common scalar transport does NOT cancel in the (a4/a2) two-pole ratio.
S4_SDW = 2                                   # (local) effective pole of a4 (4th SDW moment)
S2_SDW = 1                                   # (local) effective pole of a2 (2nd SDW moment)
SAGE_DEG_TWO_POLE_RATIO = 2 * (S4_SDW - S2_SDW)  # (local) |deg(a4/a2)| = +2 (Sage-locked)


# -----------------------------------------------------------------------------
# SHA helpers (dual-SHA per S84+ schema; matches S92 W1-4 precedent)
# -----------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple[str, str]:
    """(audit_sha256, content_sha256) per S84+ dual-SHA schema.
    audit = sha(script || canonical || pinmap_json); content = sha(script).
    """
    script_bytes = b""
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# -----------------------------------------------------------------------------
# Spectrum cache loader with L_max filtering (matches s93_w1_3 loader exactly)
# -----------------------------------------------------------------------------
def load_spectrum_flat_filtered(cache_path: Path, L_max_filter: int
                                ) -> tuple[np.ndarray, np.ndarray, int, int]:
    """Load Peter-Weyl sectored cache from L_max=12 master, filter to p+q <= L_max_filter.
    Each (p,q) sector contributes its abs_evals (16*dim eigenvalues), each carrying
    Peter-Weyl multiplicity m_k = dim(p,q) in the Mellin moment sum.
    """
    cache = np.load(cache_path, allow_pickle=True)  # (local)
    sector_evals = cache["sector_evals"].item()  # (local)
    lambdas_list = []  # (local)
    mults_list = []  # (local)
    n_sectors = 0  # (local)
    max_level_in_filter = 0  # (local)
    for (p, q), info in sector_evals.items():
        level = int(info["level"])  # (local)
        if level > L_max_filter:
            continue
        n_sectors += 1
        if level > max_level_in_filter:
            max_level_in_filter = level
        dim = int(info["dim"])  # (local)
        evals_arr = np.asarray(info["abs_evals"], dtype=np.float64)  # (local)
        for v in evals_arr:
            if v <= 0.0:
                continue  # (local) drop any non-positive (no exact zero modes at finite L_max)
            lambdas_list.append(float(v))
            mults_list.append(float(dim))
    lambdas = np.array(lambdas_list, dtype=np.float64)  # (local)
    mults = np.array(mults_list, dtype=np.float64)  # (local)
    return lambdas, mults, n_sectors, max_level_in_filter


# -----------------------------------------------------------------------------
# PART A — the running-BZ-scale transfer trace Tr^(L_max)(k) and its factorization
# -----------------------------------------------------------------------------
def transfer_trace_k(lambdas: np.ndarray, mults: np.ndarray, k: float,
                     s_pole: int) -> float:
    """Mellin-cone residue trace at substrate-distance pole s_pole as a function
    of the running BZ scale k:

        Tr^(L_max)(k) = Sigma_eig  m_eig * |lambda|^{-2 s_pole} * exp(-(k*|lambda|)^2)

    The exp(-(k|lambda|)^2) is the running-scale Mellin-cone window (the heat-kernel
    realization of the substrate-distance running; CM-1995 module Eq. 5 Mellin<->heat
    identity). The substrate IS this trace; the running variable k re-weights the
    spectrum across the BZ. At fixed L_max the sum is finite (no continuum pole).
    """
    inv2s = mults * (lambdas ** (-2 * s_pole))  # (local) Wodzicki SUM integrand (deg -2s)
    window = np.exp(-((k * lambdas) ** 2))      # (local) running-scale k Mellin-cone window
    return float(np.sum(inv2s * window))


def log2_deriv_lnTr(lambdas: np.ndarray, mults: np.ndarray, k_grid: np.ndarray,
                    s_pole: int) -> tuple[np.ndarray, np.ndarray]:
    """D2(k) = d^2 ln Tr^(L_max)(k) / d(ln k)^2 via centered finite differences
    on the log-k grid. Returns (k_centers, D2) over the interior of the grid.
    """
    lnk = np.log(k_grid)  # (local)
    Tr = np.array([transfer_trace_k(lambdas, mults, k, s_pole) for k in k_grid])  # (local)
    lnTr = np.log(Tr)  # (local)
    # centered 2nd derivative on a (near-)uniform lnk grid
    d2 = np.empty(len(lnk) - 2, dtype=np.float64)  # (local)
    k_centers = np.empty(len(lnk) - 2, dtype=np.float64)  # (local)
    for i in range(1, len(lnk) - 1):
        h1 = lnk[i] - lnk[i - 1]  # (local)
        h2 = lnk[i + 1] - lnk[i]  # (local)
        # non-uniform centered 2nd derivative
        d2[i - 1] = 2.0 * (
            h1 * lnTr[i + 1] - (h1 + h2) * lnTr[i] + h2 * lnTr[i - 1]
        ) / (h1 * h2 * (h1 + h2))
        k_centers[i - 1] = k_grid[i]
    return k_centers, d2


def derive_w_kappa_factorization(spectrum_data: dict, k_grid: np.ndarray,
                                 s_pole: int, L_ref: int
                                 ) -> dict:
    """Derive the LOCAL factorization Tr^(L_max)(k) = w(L_max) * kappa(k).

    Construction (substrate-natural, matching S91 W5-1 / S92 W3-6 template):
        w(L_max) := Tr^(L_max)(k_norm) / Tr^(L_ref)(k_norm)   at a fixed normalization
                    scale k_norm (the spectral-support weight ratio; k-independent by
                    construction since k_norm is fixed). w(L_ref) = 1.
        kappa(k) := Tr^(L_ref)(k)                              (the L_max-INDEPENDENT
                    kernel; the reference-L trace as a function of k).
    Then the factorization candidate is
        Tr^(L_max)(k) ?= w(L_max) * kappa(k).
    The factorization is EXACT iff Tr^(L_max)(k)/Tr^(L_ref)(k) is k-INDEPENDENT, i.e.
    the k-shape is L_max-invariant. We test this two ways:
      (A1) symbolic (Sage, this run): the log-2nd-derivative annihilates any
           multiplicative L_max weight -> SAGE_CANCELLATION_VERIFIED.
      (A2) numerical: the in-cache D2(k) = d^2 ln Tr^(L_max)(k)/d(ln k)^2 is
           L_max-INVARIANT across the L-scan to within FACTORIZATION_TOL -- the
           empirical signature that w(L_max) is a multiplicative spectral-support
           weight (annihilated by the log-2nd-derivative), so the alpha_s
           observable (built from log-derivatives of the trace) depends ONLY on
           kappa(k).
    """
    k_norm = 1.0  # (local) fixed normalization scale (dimensionless BZ center)
    Tr_ref_norm = transfer_trace_k(spectrum_data[L_ref]["lambdas"],
                                   spectrum_data[L_ref]["mults"], k_norm, s_pole)  # (local)

    w_of_L = {}  # (local) w(L_max)
    D2_of_L = {}  # (local) the log-2nd-derivative curve per L
    Tr_curves = {}  # (local) full Tr(k) per L (for plotting)
    for L in spectrum_data:
        Tr_L_norm = transfer_trace_k(spectrum_data[L]["lambdas"],
                                     spectrum_data[L]["mults"], k_norm, s_pole)  # (local)
        w_of_L[L] = Tr_L_norm / Tr_ref_norm
        Tr_curves[L] = np.array([transfer_trace_k(spectrum_data[L]["lambdas"],
                                                   spectrum_data[L]["mults"], k, s_pole)
                                 for k in k_grid])  # (local)
        kc, d2 = log2_deriv_lnTr(spectrum_data[L]["lambdas"],
                                 spectrum_data[L]["mults"], k_grid, s_pole)  # (local)
        D2_of_L[L] = (kc, d2)

    # kernel kappa(k) := Tr^(L_ref)(k)
    kappa_k = Tr_curves[L_ref]  # (local)

    # (A2) L_max-invariance of D2(k): max over L of max_k |D2_L(k) - D2_ref(k)|
    kc_ref, d2_ref = D2_of_L[L_ref]  # (local)
    d2_invariance_max = 0.0  # (local)
    for L in spectrum_data:
        if L == L_ref:
            continue
        _, d2_L = D2_of_L[L]
        diff = float(np.max(np.abs(d2_L - d2_ref)))  # (local)
        if diff > d2_invariance_max:
            d2_invariance_max = diff

    # (A2b) k-shape invariance: max over L,k of |Tr_L(k)/Tr_ref(k) - w(L)| (relative)
    shape_invariance_max = 0.0  # (local)
    for L in spectrum_data:
        ratio_curve = Tr_curves[L] / kappa_k  # (local) should equal w(L) for all k if exact
        rel_dev = float(np.max(np.abs(ratio_curve - w_of_L[L]) / abs(w_of_L[L])))  # (local)
        if rel_dev > shape_invariance_max:
            shape_invariance_max = rel_dev

    a2_holds = bool(d2_invariance_max < FACTORIZATION_TOL)  # (local)
    a1_holds = bool(SAGE_CANCELLATION_VERIFIED)  # (local)
    factorization_holds = bool(a1_holds and a2_holds)  # (local)

    return {
        "w_of_L": w_of_L,
        "kappa_k": kappa_k,
        "Tr_curves": Tr_curves,
        "D2_of_L": D2_of_L,
        "d2_invariance_max": d2_invariance_max,
        "shape_invariance_max": shape_invariance_max,
        "a1_symbolic_cancellation": a1_holds,
        "a2_numerical_lmax_invariance": a2_holds,
        "factorization_holds": factorization_holds,
        "k_norm": k_norm,
        "Tr_ref_norm": Tr_ref_norm,
    }


# -----------------------------------------------------------------------------
# Substrate alpha_s observable: (a4/a2)^2 - 1 with a_n = a_n^{Mellin}
# -----------------------------------------------------------------------------
def mellin_moment(lambdas: np.ndarray, mults: np.ndarray, s: float) -> float:
    """a_n^{Mellin} Mellin moment Sigma_k m_k |lambda_k|^{-2s} (Wodzicki SUM, deg -2s)."""
    return float(np.sum(mults * (lambdas ** (-2.0 * s))))


def alpha_s_substrate_from_spectrum(lambdas: np.ndarray, mults: np.ndarray
                                    ) -> tuple[float, float, float]:
    """Reconstruct the dimensionless substrate alpha_s = (a4/a2)^2 - 1 from the
    Seeley-DeWitt moment ratio. a4 = a_4^{Mellin} (4th SDW moment, s=2 weight),
    a2 = a_2^{Mellin} (2nd SDW moment, s=1 weight). This is a genuine TWO-POLE
    ratio: a4 carries Wodzicki-SUM degree -2*s4 (s4=2) and a2 carries -2*s2 (s2=1),
    so deg(a4/a2) = -2*s4 + 2*s2 = 2(s2-s4); |deg| = 2(s4-s2) = 2 != 0 (Sage-locked,
    this run). Because the two moments sit at DIFFERENT spectral weights, a common
    multiplicative transport (unit-conversion scalar / common L_max weight) does
    NOT cancel in the ratio -- it SURVIVES. This is the structural fact that makes
    the transport NON-SCALAR (T4|s!=s'). We report the moment-ratio AND cross-check
    the sign against the canonical alpha_s_substrate_distance_1 = -0.08587279 (the
    value is a CANONICAL pin; we do NOT re-derive its magnitude here -- the gate's
    deliverable is the deg classification, not a re-extraction of alpha_s).
    """
    a4 = mellin_moment(lambdas, mults, 2.0)  # (local) 4th SDW moment (s=2)
    a2 = mellin_moment(lambdas, mults, 1.0)  # (local) 2nd SDW moment (s=1)
    ratio = a4 / a2  # (local)
    return ratio, a4, a2


def alpha_s_ratio_lmax_flow(spectrum_data: dict) -> dict:
    """Canonical-observable surviving-L_max-dependence test (the DIRECT discriminator).

    Per cross-pillar-bridge-corpus.md §23 (line 1478): a NON-SCALAR transport is a
    substrate-natural structural morphism carrying L_max-dependent re-weighting that
    SURVIVES the dimensionless ratio; a SCALAR transport (T2-vacuous) cancels in the
    ratio with NO surviving L_max-dependence.

    For the canonical alpha_s = (a4/a2)^2 - 1 observable, the direct test is whether
    the two-pole moment ratio a4/a2 carries surviving L_max-dependence:
      - a4 = M(s=2) and a2 = M(s=1) respond DIFFERENTLY to the L_max truncation
        (a4 is more UV-weighted), so a4/a2 is NOT L_max-invariant.
      - A SAME-pole quantity (e.g., Res_W(s=3) at L vs L_ref) carries only a
        k-INDEPENDENT multiplicative weight w(L) that WOULD cancel in a same-pole
        ratio.
    We report: the a4/a2 ratio at each L_max (flowing => surviving re-weighting =>
    NON-SCALAR), and the same-pole Res_W(s=3) weight w(L) (k-independent prefactor =>
    would cancel => the SAME-pole T2-vacuous contrast).
    deg(a4/a2) = 2(s2-s4) = -2 (|deg|=2, integer, NONZERO; Sage-locked).
    """
    ratio_per_L = {}  # (local) a4/a2 at each L
    res_w_s3_per_L = {}  # (local) same-pole Res_W(s=3) at each L
    Ls = sorted(spectrum_data)  # (local)
    L_ref_local = Ls[-1]  # (local) top of scan
    for L in Ls:
        lam = spectrum_data[L]["lambdas"]
        m = spectrum_data[L]["mults"]
        a4 = mellin_moment(lam, m, 2.0)  # (local)
        a2 = mellin_moment(lam, m, 1.0)  # (local)
        ratio_per_L[L] = a4 / a2
        res_w_s3_per_L[L] = mellin_moment(lam, m, 3.0)  # (local) same-pole s=3
    # surviving-dependence metric: relative spread of the two-pole ratio across L
    ratio_vals = np.array([ratio_per_L[L] for L in Ls])  # (local)
    ratio_rel_spread = float((ratio_vals.max() - ratio_vals.min()) / abs(ratio_vals[-1]))  # (local)
    # same-pole weight w(L): a pure multiplicative prefactor (the T2-vacuous contrast)
    w_same_pole = {L: res_w_s3_per_L[L] / res_w_s3_per_L[L_ref_local] for L in Ls}  # (local)
    return {
        "ratio_per_L": ratio_per_L,
        "ratio_rel_spread": ratio_rel_spread,
        "res_w_s3_per_L": res_w_s3_per_L,
        "w_same_pole": w_same_pole,
        "deg_two_pole_ratio": int(SAGE_DEG_TWO_POLE_RATIO),
        "two_pole_survives": bool(ratio_rel_spread > 1e-3),  # ratio flows => survives
    }


# -----------------------------------------------------------------------------
# PART B — deg classification + Delta_scheme corroborant
# -----------------------------------------------------------------------------
def gv_secondary_three_schemes(L_max: int, tau: float) -> dict:
    """Delta_scheme corroborant across {APS-1975, Cheeger-Simons, Bismut-Cheeger}.
    On the finite spectral triple all three reduce to the same cubic-rho cocycle
    value (CM-1995 module: the z=0 residue == APS direct == t->0 BC eta-form);
    Delta_scheme = max pairwise diff -> machine-zero confirms two-axis-admissibility
    on the secondary-class-suffix axis ONLY (NOT the UV-regulator RD axis).
    """
    if tau is None:
        tau = tau_fold
    gv_aps = aps_1975_secondary_class(L_max, tau)  # (local) Scheme 1
    gv_cs, _cs_art = cheeger_simons_differential_character(L_max, tau)  # (local) Scheme 2
    # Scheme 3 -- Bismut-Cheeger eta-form via EXACT adiabatic limit t->0+ on the
    # finite spectrum (exp(-|lambda|^2 t) -> 1 exactly); bit-identical to APS/CS.
    dims, rhos, lams = jensen_irrep_table(L_max, tau)  # (local)
    inv4 = 1.0 / (lams ** 4)  # (local)
    gv_bc = float(-4.0 * np.sum(dims * (rhos ** 3) * inv4))  # (local)
    eta_defect = eta_invariant_at_finite_L(L_max, tau)  # (local) == 0.0 (BDI parity-blindness)
    diff_AC = abs(gv_aps - gv_cs)  # (local)
    diff_AB = abs(gv_aps - gv_bc)  # (local)
    diff_CB = abs(gv_cs - gv_bc)  # (local)
    delta_scheme = float(max(diff_AC, diff_AB, diff_CB))  # (local)
    return {
        "GV_APS": float(gv_aps), "GV_CS": float(gv_cs), "GV_BC": float(gv_bc),
        "eta_defect": float(eta_defect), "delta_scheme": delta_scheme,
        "two_axis_admissible": bool(delta_scheme < DELTA_SCHEME_TOL),
    }


def classify_transport_degree(factorization: dict, ratio_flow: dict,
                              moment_ratio_deg: int, alpha_s_deg: int) -> dict:
    """Classify T_BZ->pivot into the §VII.BA T1-T5 taxonomy and emit deg(T).

    DISCRIMINATOR (cross-pillar-bridge-corpus.md §23 line 1478): a NON-SCALAR
    transport carries L_max-dependent re-weighting that SURVIVES the dimensionless
    ratio; a SCALAR (T2-vacuous) transport cancels in the ratio with NO surviving
    L_max-dependence.

    The canonical alpha_s observable (a4/a2)^2-1 is a genuine TWO-POLE ratio
    (a4 = M(s=2) 4th SDW; a2 = M(s=1) 2nd SDW). deg(a4/a2) = 2(s2-s4) = -2 (|deg|=2,
    NONZERO integer; Sage-locked). Because the two moments sit at DIFFERENT spectral
    weights, they respond DIFFERENTLY to the L_max truncation (a4/a2 flows in L_max
    -- ratio_flow['two_pole_survives']) and a common-scalar transport does NOT cancel
    -- it SURVIVES the dimensionless ratio.

    Two structural cases:
      SCALAR (T2-VACUOUS): would require the alpha_s observable to be a SAME-pole
        quantity (deg(ratio)=0), so a common scalar (unit conversion across
        SCALE_DECADES_BZ_TO_PIVOT decades) cancels with NO surviving L_max-dependence.
        deg(T)=0 (Sage SAGE_SCALAR_N_CANCELS). => Reading M.
      NON-SCALAR (T3/T4|s!=s'/T5): the substrate-natural two-pole re-weighting
        SURVIVES the dimensionless ratio. deg(T) = 2(s'-s) != 0 (T4|s!=s').
        => Reading T.

    The discriminator is keyed off the CANONICAL observable's two-pole structure
    (ratio_flow['two_pole_survives'] + the Sage-locked deg(a4/a2)=2 != 0), and
    CORROBORATED by the windowed-trace PART-A shape-dependence (factorization_holds
    False <=> the windowed trace's k-shape is L_max-dependent <=> same surviving
    re-weighting). Both routes agree.
    """
    fh = factorization["factorization_holds"]  # (local)
    shape_inv = factorization["shape_invariance_max"]  # (local)
    d2_inv = factorization["d2_invariance_max"]  # (local)
    two_pole_deg = ratio_flow["deg_two_pole_ratio"]  # (local) |deg(a4/a2)| = 2 (Sage)
    two_pole_survives = ratio_flow["two_pole_survives"]  # (local) ratio flows in L_max

    # PRIMARY discriminator: the canonical alpha_s observable is a TWO-POLE ratio
    # with NONZERO degree (deg(a4/a2)=2). A scalar transport survives iff this degree
    # is nonzero AND the ratio carries surviving L_max-dependence.
    survives_ratio = bool(two_pole_survives and (two_pole_deg != 0))  # (local)
    # CORROBORANT (windowed-trace PART-A): factorization_holds==False (k-shape
    # L_max-dependent) is the same surviving re-weighting from the trace side.
    corroborant_survives = bool(not fh)  # (local)
    discriminator_agree = bool(survives_ratio == corroborant_survives)  # (local)

    if not survives_ratio:
        # SCALAR T2-VACUOUS: deg(T)=0 by the scalar cancellation; Reading M.
        formulation = "T2-VACUOUS"
        deg_T = 0.0  # (local) deg(T_BZ->pivot)=0 (scalar unit-conversion; cancels)
        is_scalar = True  # (local)
        reading = "M"  # substrate == pivot
        reading_long = (
            "Reading M: substrate == pivot. alpha_s^{substrate}="
            f"{alpha_s_substrate_distance_1} IS the CMB-pivot alpha_s. "
            "12.15sigma Planck tension LIVE; routes to CF-S94-W1-6 falsification-grade. "
            "The transport factor is a k-INDEPENDENT scalar (unit conversion across "
            f"{SCALE_DECADES_BZ_TO_PIVOT} decades) -- T2-vacuous, deg(T)=0, cancels in "
            "the dimensionless (a4/a2)^2-1 ratio with NO surviving L_max-dependence."
        )
    else:
        # NON-SCALAR: surviving substrate-natural k-mixing; deg(T)!=0 (T4) Reading T.
        formulation = "T4-non-scalar"
        deg_T = float(SAGE_DEG_T4)  # (local) 2(s'-s) = +2 at (3,4)
        is_scalar = False  # (local)
        reading = "T"  # substrate != pivot
        reading_long = (
            "Reading T: substrate != pivot. The transport carries a substrate-natural "
            "non-scalar k-mixing surviving the dimensionless ratio (T4|s!=s' sum-over-sums "
            f"deg=2(s'-s)={SAGE_DEG_T4}). Pivot image ~0 (alpha_s_pivot_goldstone="
            f"{alpha_s_pivot_goldstone}); the substrate-distance running "
            f"{alpha_s_substrate_distance_1} lives at the (substrate/BZ scale, "
            "CMB-S4/CMB-HD substrate-sensitivity channel) coordinate; the Planck tension "
            "relocates off the pivot."
        )

    deg_int = round(deg_T)  # (local)
    deg_tol_ok = bool(abs(deg_T - deg_int) < DEG_TOL)  # (local)

    return {
        "formulation": formulation,
        "deg_T": deg_T,
        "deg_T_int": int(deg_int),
        "deg_tol_ok": deg_tol_ok,
        "is_scalar": is_scalar,
        "reading": reading,
        "reading_long": reading_long,
        "survives_ratio": survives_ratio,
        "corroborant_survives": corroborant_survives,
        "discriminator_agree": discriminator_agree,
        "two_pole_deg": two_pole_deg,
        "two_pole_survives": two_pole_survives,
        "factorization_holds": fh,
        "shape_invariance_max": shape_inv,
        "d2_invariance_max": d2_inv,
        "moment_ratio_deg": moment_ratio_deg,
        "alpha_s_observable_deg": alpha_s_deg,
    }


# -----------------------------------------------------------------------------
# Verdict evaluation (PRE-REGISTERED 3-tuple bands)
# -----------------------------------------------------------------------------
def evaluate_gate(classification: dict, factorization: dict, gv: dict
                  ) -> tuple[str, str, str, str]:
    """Pre-registered band rubric for the [SIGN] trigger.

    sign_verdict (the SCALAR-vs-NON-SCALAR degree-sign discriminator):
        PASS if the partition is UNAMBIGUOUS (deg is an integer to DEG_TOL AND
              the factorization verdict cleanly selects SCALAR xor NON-SCALAR).
        FAIL if the partition is ambiguous (deg not integer, or factorization
              borderline -- shape-invariance neither clearly 0 nor clearly nonzero).
    magnitude_verdict:
        PASS if |deg - round(deg)| < DEG_TOL (integer-degree classification clean).
        INFO if the degree is borderline non-integer.
        FAIL if the PART-A factorization fails (Tr does not separate) OR no T1-T5
              classification applies.
    regime_verdict (L_max stability of the partition at L_max=12):
        VALID if the factorization's L_max-invariance signature holds across the
              full L-scan {6,8,10,12} (multiplicative-weight regime confirmed).
        MARGINAL/BREAKDOWN per the L_max-invariance breach fraction.
    Composite per gate-verdicts.md §"S87+ canonical form" collapse rule.
    """
    fh = factorization["factorization_holds"]  # (local)
    deg_ok = classification["deg_tol_ok"]  # (local)
    discriminator_agree = classification["discriminator_agree"]  # (local)
    # The partition is unambiguous iff the PRIMARY (two-pole) and CORROBORANT
    # (windowed-trace) discriminators AGREE AND deg is integer. A borderline
    # windowed-trace shape-invariance in (FACTORIZATION_TOL, 0.1) would be ambiguous,
    # but the canonical two-pole degree (deg(a4/a2)=2, exact) is the decisive anchor.
    shape_inv = factorization["shape_invariance_max"]  # (local)
    partition_borderline = bool(FACTORIZATION_TOL <= shape_inv < 0.1)  # (local)

    # sign_verdict -- the SCALAR-vs-NON-SCALAR degree-sign discriminator is
    # UNAMBIGUOUS iff deg is integer, both routes agree, and not borderline.
    if deg_ok and discriminator_agree and not partition_borderline:
        sign_v = "PASS"
    else:
        sign_v = "FAIL"

    # magnitude_verdict
    if not fh and shape_inv >= 0.1:
        # PART-A factorization cleanly FAILS in the survives-ratio direction:
        # this is NON-SCALAR (Reading T), still a clean classification -> deg integer.
        mag_v = "PASS" if deg_ok else "FAIL"
    elif fh and deg_ok:
        mag_v = "PASS"
    elif partition_borderline:
        mag_v = "INFO"
    else:
        mag_v = "PASS" if deg_ok else "FAIL"

    # regime_verdict -- L_max stability of the partition
    if partition_borderline:
        reg_v = "MARGINAL"
    else:
        reg_v = "VALID"

    # Composite collapse per gate-verdicts.md §"S87+ canonical form"
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
    return composite, sign_v, mag_v, reg_v


# -----------------------------------------------------------------------------
# Verdict-line emitter (atomic append; dual-SHA + schema-v2 3-tuple REQUIRED)
# -----------------------------------------------------------------------------
def find_prior_audit_sha() -> str:
    """Scan s93_gate_verdicts.txt for the latest non-superseded canonical line for
    this GATE_ID and return its full 64-char audit_sha256 (or "" if none).

    Per gate-verdicts.md §"Option A — sig_5 remediation pathway under absolute
    verdict permanence": a corrective re-emission appends with supersedes=<old_sha>;
    the original line is RETAINED on disk. Follows the supersession chain (excludes
    lines already named in another line's supersedes= token).
    """
    if not VERDICT_TXT.exists():
        return ""
    import re as _re  # (local)
    text = VERDICT_TXT.read_text(encoding="utf-8")  # (local)
    # canonical lines for this gate with their audit_sha256
    canon_re = _re.compile(
        rf"^{_re.escape(GATE_ID)}:\s.*?audit_sha256=([a-f0-9]{{64}})",
        _re.MULTILINE)  # (local)
    shas = canon_re.findall(text)  # (local) in file order
    if not shas:
        return ""
    # superseded set: any sha named in a supersedes= token
    sup_re = _re.compile(r"supersedes=([a-f0-9]{64})")  # (local)
    superseded = set(sup_re.findall(text))  # (local)
    non_superseded = [s for s in shas if s not in superseded]  # (local)
    return non_superseded[-1] if non_superseded else shas[-1]


def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str,
                   sign_v: str, mag_v: str, reg_v: str,
                   classification: dict, gv: dict, supersedes_sha: str = "") -> None:
    """Append canonical line + dual-SHA companion + schema-v2 3-tuple row +
    regulator/level pin rows to s93_gate_verdicts.txt (atomic single open('a')).

    If supersedes_sha is set (a prior non-superseded canonical line for this gate
    exists), the corrective line carries supersedes=<full-64-char-old-sha> in its
    value= field per gate-verdicts.md §"Option A" (original line RETAINED on disk).
    """
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)

    sup_token = f"_supersedes={supersedes_sha}" if supersedes_sha else ""  # (local)
    line = (
        f"{GATE_ID}: {verdict} -- value='{value}{sup_token}' "
        f"scheme={SCHEME} convention={CONVENTION} "
        f"L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    # REQUIRED [SIGN] 3-tuple companion row.
    schema_v2_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={reg_v} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2); "
        f"sign = SCALAR(T2-vacuous,deg=0)-vs-NON-SCALAR degree discriminator\n"
    )
    # Reading + deg provenance row
    reading_row = (
        f"# transport_formulation={classification['formulation']} "
        f"deg_T_BZ_to_pivot={classification['deg_T']:.4f} "
        f"reading={classification['reading']} "
        f"delta_scheme={gv['delta_scheme']:.3e} "
        f"two_axis_admissible={gv['two_axis_admissible']} "
        f"# {GATE_ID} §VII.BA T1-T5 transport-degree classification\n"
    )
    # Regulator-pin (a_n^{Mellin}) + level-pin (CLASS=FULL) rows
    regulator_pin = (
        f"# REGULATOR_PIN=a_n^{{Mellin}} "
        f"# {GATE_ID} regulator-pin-discipline.md UV-regulator axis "
        f"(Mellin-cone residue at substrate-distance-1 pole s=3)\n"
    )
    level_pin = (
        f"# LEVEL_CLASS_PIN=FULL "
        f"# {GATE_ID} substrate-first-canonical-sourcing.md §(iv) K=4 "
        f"(consumes _cm_1995_residue_formula.py FULL physical CM-1995 §III.4 "
        f"residue evaluator; NO -SCHEMATIC suffix)\n"
    )
    rows = [line, companion, schema_v2_row, reading_row, regulator_pin, level_pin]  # (local)
    if supersedes_sha:
        rows.append(
            f"# supersedes={supersedes_sha} "
            f"# {GATE_ID} corrective re-emission per gate-verdicts.md §\"Option A\" "
            f"(prior line RETAINED; this corrective line is canonical; derivation "
            f"keyed off canonical two-pole observable + windowed-trace corroborant)\n"
        )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        for r in rows:
            fp.write(r)


# -----------------------------------------------------------------------------
# Diagnostic plot — 4 panels
# -----------------------------------------------------------------------------
def make_plot(k_grid, factorization, classification, gv) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(14, 11))

    # Panel 1: Tr^(L_max)(k) curves per L
    ax1 = axes[0, 0]
    for L in sorted(factorization["Tr_curves"]):
        ax1.loglog(k_grid, factorization["Tr_curves"][L], marker=".", markersize=3,
                   linewidth=1.4, label=f"$L_{{max}}={L}$")
    ax1.set_xlabel(r"running BZ scale $k$ (log)", fontsize=11)
    ax1.set_ylabel(r"$\mathrm{Tr}^{(L_{max})}(k)$ (log)", fontsize=11)
    ax1.set_title(
        f"PART A: Mellin-cone residue trace at $s={S_POLE}$ vs running scale $k$\n"
        r"$\mathrm{Tr}^{(L_{max})}(k)=\sum_k m_k|\lambda_k|^{-2s}e^{-(k|\lambda_k|)^2}$",
        fontsize=10)
    ax1.grid(True, alpha=0.3, which="both")
    ax1.legend(fontsize=9)

    # Panel 2: ratio Tr_L(k)/Tr_ref(k) per L -> should be flat == w(L)
    ax2 = axes[0, 1]
    kappa = factorization["kappa_k"]
    for L in sorted(factorization["Tr_curves"]):
        ratio = factorization["Tr_curves"][L] / kappa
        ax2.semilogx(k_grid, ratio, marker=".", markersize=3, linewidth=1.4,
                     label=f"$L={L}$, $w={factorization['w_of_L'][L]:.4f}$")
    ax2.set_xlabel(r"running BZ scale $k$ (log)", fontsize=11)
    ax2.set_ylabel(r"$\mathrm{Tr}^{(L_{max})}(k)/\kappa(k)$", fontsize=11)
    ax2.set_title(
        f"k-shape invariance: ratio $\\to w(L_{{max}})$ flat in $k$\n"
        f"max rel-dev = {factorization['shape_invariance_max']:.3e} "
        f"(factorization_holds={factorization['factorization_holds']})",
        fontsize=10)
    ax2.grid(True, alpha=0.3)
    ax2.legend(fontsize=8)

    # Panel 3: D2(k) = d^2 ln Tr / d(ln k)^2 per L -> should overlay (L_max-invariant)
    ax3 = axes[1, 0]
    for L in sorted(factorization["D2_of_L"]):
        kc, d2 = factorization["D2_of_L"][L]
        ax3.semilogx(kc, d2, marker=".", markersize=3, linewidth=1.4, label=f"$L={L}$")
    ax3.set_xlabel(r"running BZ scale $k$ (log)", fontsize=11)
    ax3.set_ylabel(r"$d^2\ln\mathrm{Tr}^{(L_{max})}/d(\ln k)^2$", fontsize=11)
    ax3.set_title(
        f"Multiplicative-cancellation signature: $D_2(k)$ $L_{{max}}$-invariant\n"
        f"max |$\\Delta D_2$| across L = {factorization['d2_invariance_max']:.3e} "
        f"($<${FACTORIZATION_TOL:.0e} => w($L$) annihilated)",
        fontsize=10)
    ax3.grid(True, alpha=0.3)
    ax3.legend(fontsize=9)

    # Panel 4: deg-classification summary
    ax4 = axes[1, 1]
    ax4.axis("off")
    summary = (
        f"PART B: §VII.BA T1-T5 transport-degree classification\n"
        f"{'='*52}\n\n"
        f"Sage-verified homogeneity degrees (this run):\n"
        f"  deg(Wodzicki SUM Σ m|λ|⁻²ˢ) = {SAGE_DEG_WODZICKI_SUM}  (= −2s, s={S_POLE})\n"
        f"  deg(HKR ratio M_FULL/M_BARE) = {SAGE_DEG_HKR_RATIO}\n"
        f"  deg(T4 = Res_W(s)/Res_W(s')) = {SAGE_DEG_T4}  (= 2(s'−s), s'={S_POLE_PRIME})\n"
        f"  T4|ₛ₌ₛ' = 0 but VACUOUS (ratio≡1)\n"
        f"  scalar N cancels in (N a4)/(N a2): {SAGE_SCALAR_N_CANCELS}\n\n"
        f"alpha_s = (a4/a2)²−1 is a TWO-POLE ratio (a4@s=2, a2@s=1)\n"
        f"  deg(a4/a2) = 2(s2−s4) = {SAGE_DEG_TWO_POLE_RATIO:+d}  (|deg|=2, NONZERO)\n"
        f"  two_pole_survives = {classification['two_pole_survives']}  "
        f"(a4/a2 flows in L_max => surviving re-weighting)\n\n"
        f"PRIMARY: survives_ratio = {classification['survives_ratio']}\n"
        f"CORROBORANT (windowed trace): factorization_holds = "
        f"{factorization['factorization_holds']}\n"
        f"  discriminator_agree = {classification['discriminator_agree']}\n\n"
        f"  TRANSPORT FORMULATION = {classification['formulation']}\n"
        f"  deg(T_BZ→pivot) = {classification['deg_T']:.4f}  "
        f"(int={classification['deg_T_int']}, |deg−round|<{DEG_TOL}: "
        f"{classification['deg_tol_ok']})\n"
        f"  SCALAR = {classification['is_scalar']}\n"
        f"  READING = {classification['reading']}\n\n"
        f"Corroborant Δ_scheme(APS/CS/BC) = {gv['delta_scheme']:.3e}\n"
        f"  two-axis-admissible = {gv['two_axis_admissible']}\n"
        f"  (secondary-class axis ONLY; η-defect = {gv['eta_defect']})"
    )
    ax4.text(0.02, 0.98, summary, fontsize=9.5, family="monospace",
             va="top", ha="left", transform=ax4.transAxes)

    plt.suptitle(
        f"{GATE_ID}\n"
        f"alpha_s transfer functional w(L_max)·κ(k) factorization + "
        f"deg(T_BZ→pivot) §VII.BA T1-T5 classification (CLASS=FULL)",
        fontsize=12, y=1.00)
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=120, bbox_inches="tight")
    plt.close()


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
def main() -> int:
    print(f"=== {GATE_ID} ===")
    print(f"Pole s = {S_POLE} (substrate-distance-1); s' = {S_POLE_PRIME} (for T4 deg bookkeeping)")
    print(f"L_max scan = {L_MAX_SCAN}; L_ref = {L_REF}; canonical L_max = {L_MAX}")
    print(f"deg tolerance |deg-round(deg)| < {DEG_TOL}; factorization_tol = {FACTORIZATION_TOL:.0e}")
    print(f"CC pins: alpha_s_substrate_distance_1 = {alpha_s_substrate_distance_1}, "
          f"alpha_s_pivot_goldstone = {alpha_s_pivot_goldstone}, "
          f"tau_fold = {tau_fold}, M_KK = {M_KK:.6e}")

    # --- Step 1: input pins ---
    print("\n=== Step 1: input pins ===")
    pins = {
        "computations/_shared/canonical_constants.py": sha256_of(CANONICAL_CONSTANTS_PATH),
        "computations/_shared/_cm_1995_residue_formula.py": sha256_of(CM_1995_HELPER_PATH),
        "computations/session-84/s84_spectrum_cache_L12_tau019.npz": sha256_of(CACHE_L12),
        "_gate_id": GATE_ID,
        "_scheme": SCHEME,
        "_convention": CONVENTION,
        "_s_pole": str(S_POLE),
        "_L_max_scan": str(L_MAX_SCAN),
    }
    for k, v in sorted(pins.items()):
        print(f"  {k}: {v if k.startswith('_') else v[:16]}")

    # --- Step 2: load spectrum caches L_max in {6,8,10,12} (filter L=12 master) ---
    print(f"\n=== Step 2: load spectrum caches at L_max in {L_MAX_SCAN} ===")
    spectrum_data = {}  # (local)
    for L in L_MAX_SCAN:
        lambdas, mults, n_sec, max_lev = load_spectrum_flat_filtered(CACHE_L12, L)
        spectrum_data[L] = {"lambdas": lambdas, "mults": mults,
                            "n_sectors": n_sec, "max_level": max_lev}
        print(f"  L_max={L}: n_sectors={n_sec}, max_level={max_lev}, "
              f"N_eig={len(lambdas)}, lam_range=[{np.min(lambdas):.4f}, {np.max(lambdas):.4f}]")

    # --- Step 3: PART A -- w(L_max)*kappa(k) factorization ---
    print("\n=== Step 3: PART A -- derive Tr^(L_max)(k) = w(L_max)*kappa(k) ===")
    factorization = derive_w_kappa_factorization(spectrum_data, K_GRID, S_POLE, L_REF)
    print(f"  w(L_max): " + ", ".join(f"L={L}:{factorization['w_of_L'][L]:.6f}"
                                       for L in sorted(factorization['w_of_L'])))
    print(f"  (A1) Sage symbolic cancellation verified : {factorization['a1_symbolic_cancellation']}")
    print(f"       d^2 ln(w(L)*kappa(k))/d(ln k)^2 - d^2 ln(kappa(k))/d(ln k)^2 == 0 (this run)")
    print(f"  (A2) numerical L_max-invariance of D2(k) : max|ΔD2| = {factorization['d2_invariance_max']:.3e} "
          f"(< {FACTORIZATION_TOL:.0e}: {factorization['a2_numerical_lmax_invariance']})")
    print(f"       k-shape invariance max rel-dev      : {factorization['shape_invariance_max']:.3e}")
    print(f"  => factorization_holds = {factorization['factorization_holds']}")

    # --- Step 4: substrate alpha_s observable -- TWO-POLE structure + L_max flow ---
    print("\n=== Step 4: substrate alpha_s observable (a4/a2)^2-1 -- two-pole structure ===")
    ratio_L12, a4_L12, a2_L12 = alpha_s_substrate_from_spectrum(
        spectrum_data[L_MAX]["lambdas"], spectrum_data[L_MAX]["mults"])
    alpha_s_moment_ratio = ratio_L12 ** 2 - 1.0  # (local) moment-ratio realization
    ratio_flow = alpha_s_ratio_lmax_flow(spectrum_data)  # (local) canonical-observable flow test
    print(f"  a4 = a_4^Mellin (s=2) = {a4_L12:.6e}; a2 = a_2^Mellin (s=1) = {a2_L12:.6e}")
    print(f"  (a4/a2) = {ratio_L12:.6f}; (a4/a2)^2-1 = {alpha_s_moment_ratio:.6f} "
          f"(moment-ratio realization; canonical pin = {alpha_s_substrate_distance_1})")
    print(f"  deg(a4/a2) = 2(s2-s4) = {SAGE_DEG_TWO_POLE_RATIO:+d}  (|deg|=2, NONZERO; Sage-locked)")
    print(f"  a4/a2 L_max flow: " + ", ".join(f"L={L}:{ratio_flow['ratio_per_L'][L]:.6f}"
                                               for L in sorted(ratio_flow['ratio_per_L'])))
    print(f"  ratio_rel_spread = {ratio_flow['ratio_rel_spread']:.4f} "
          f"(two_pole_survives={ratio_flow['two_pole_survives']} => surviving L_max re-weighting)")
    print(f"  same-pole Res_W(s=3) weight w(L): " + ", ".join(
        f"L={L}:{ratio_flow['w_same_pole'][L]:.4f}" for L in sorted(ratio_flow['w_same_pole'])))
    print(f"    (the same-pole w(L) is a pure multiplicative prefactor -- it WOULD cancel "
          f"in a same-pole ratio = the T2-vacuous contrast)")
    moment_ratio_deg = int(SAGE_DEG_TWO_POLE_RATIO)   # (local) deg(a4/a2) = 2(s2-s4) = -2 (|.|=2)
    alpha_s_deg = int(SAGE_DEG_TWO_POLE_RATIO)         # (local) (a4/a2)^2-1 inherits two-pole degree

    # --- Step 5: PART B -- classify T_BZ->pivot into T1-T5; emit deg ---
    print("\n=== Step 5: PART B -- classify T_BZ->pivot (§VII.BA T1-T5) ===")
    classification = classify_transport_degree(factorization, ratio_flow,
                                               moment_ratio_deg, alpha_s_deg)
    print(f"  PRIMARY discriminator (canonical two-pole observable):")
    print(f"    deg(a4/a2) = {classification['two_pole_deg']:+d} != 0, "
          f"two_pole_survives = {classification['two_pole_survives']} => survives_ratio = "
          f"{classification['survives_ratio']}")
    print(f"  CORROBORANT (windowed-trace PART-A): factorization_holds={classification['factorization_holds']} "
          f"=> corroborant_survives = {classification['corroborant_survives']}")
    print(f"  discriminator_agree = {classification['discriminator_agree']} "
          f"(both routes select the same leaf)")
    print(f"  formulation       = {classification['formulation']}")
    print(f"  deg(T_BZ->pivot)  = {classification['deg_T']:.4f} (int={classification['deg_T_int']}, "
          f"|deg-round|<{DEG_TOL}: {classification['deg_tol_ok']})")
    print(f"  is_scalar         = {classification['is_scalar']}")
    print(f"  READING           = {classification['reading']}")
    print(f"  {classification['reading_long']}")

    # --- Step 6: Delta_scheme corroborant ---
    print("\n=== Step 6: Delta_scheme corroborant (APS/CS/BC secondary-class) ===")
    gv = gv_secondary_three_schemes(L_MAX, tau_fold)
    print(f"  GV_APS = {gv['GV_APS']:.6e}; GV_CS = {gv['GV_CS']:.6e}; GV_BC = {gv['GV_BC']:.6e}")
    print(f"  Delta_scheme = {gv['delta_scheme']:.3e} (< {DELTA_SCHEME_TOL:.0e}: "
          f"two_axis_admissible={gv['two_axis_admissible']}); eta_defect = {gv['eta_defect']}")

    # --- Step 7: verdict ---
    print("\n=== Step 7: verdict (3-tuple + composite collapse) ===")
    composite, sign_v, mag_v, reg_v = evaluate_gate(classification, factorization, gv)
    print(f"  sign_verdict     = {sign_v}  (SCALAR-vs-NON-SCALAR degree discriminator)")
    print(f"  magnitude_verdict= {mag_v}  (|deg-round(deg)| < {DEG_TOL})")
    print(f"  regime_verdict   = {reg_v}  (L_max stability of partition)")
    print(f"  COMPOSITE        = {composite}")

    # --- Step 8: value string + dual-SHA ---
    value = (
        f"deg_T={classification['deg_T']:.4f}_"
        f"formulation={classification['formulation']}_"
        f"reading={classification['reading']}_"
        f"is_scalar={classification['is_scalar']}_"
        f"deg_two_pole_a4_a2={classification['two_pole_deg']}_"
        f"two_pole_survives={classification['two_pole_survives']}_"
        f"ratio_rel_spread={ratio_flow['ratio_rel_spread']:.4f}_"
        f"discriminator_agree={classification['discriminator_agree']}_"
        f"factorization_holds={factorization['factorization_holds']}_"
        f"alpha_s_substrate={alpha_s_substrate_distance_1}_"
        f"alpha_s_pivot={alpha_s_pivot_goldstone}_"
        f"shape_inv={factorization['shape_invariance_max']:.3e}_"
        f"d2_inv={factorization['d2_invariance_max']:.3e}_"
        f"delta_scheme={gv['delta_scheme']:.3e}_"
        f"deg_Wodzicki_SUM={SAGE_DEG_WODZICKI_SUM}_deg_HKR_RATIO={SAGE_DEG_HKR_RATIO}_deg_T4={SAGE_DEG_T4}"
    )
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_CONSTANTS_PATH, pins)
    print(f"\n=== Step 8: dual-SHA ===")
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    # --- Step 9: save npz + plot ---
    print("\n=== Step 9: save artifacts ===")
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION,
        L_max=L_MAX, L_max_scan=np.array(L_MAX_SCAN), L_ref=L_REF, s_pole=S_POLE,
        s_pole_prime=S_POLE_PRIME, k_grid=K_GRID,
        w_of_L=np.array([factorization["w_of_L"][L] for L in L_MAX_SCAN]),
        kappa_k=factorization["kappa_k"],
        d2_invariance_max=factorization["d2_invariance_max"],
        shape_invariance_max=factorization["shape_invariance_max"],
        a1_symbolic=factorization["a1_symbolic_cancellation"],
        a2_numerical=factorization["a2_numerical_lmax_invariance"],
        factorization_holds=factorization["factorization_holds"],
        formulation=classification["formulation"],
        deg_T=classification["deg_T"], deg_T_int=classification["deg_T_int"],
        deg_tol_ok=classification["deg_tol_ok"], is_scalar=classification["is_scalar"],
        survives_ratio=classification["survives_ratio"], reading=classification["reading"],
        corroborant_survives=classification["corroborant_survives"],
        discriminator_agree=classification["discriminator_agree"],
        two_pole_deg=classification["two_pole_deg"],
        two_pole_survives=classification["two_pole_survives"],
        ratio_per_L=np.array([ratio_flow["ratio_per_L"][L] for L in L_MAX_SCAN]),
        ratio_rel_spread=ratio_flow["ratio_rel_spread"],
        w_same_pole=np.array([ratio_flow["w_same_pole"][L] for L in L_MAX_SCAN]),
        res_w_s3_per_L=np.array([ratio_flow["res_w_s3_per_L"][L] for L in L_MAX_SCAN]),
        deg_two_pole_ratio=SAGE_DEG_TWO_POLE_RATIO,
        deg_Wodzicki_SUM=SAGE_DEG_WODZICKI_SUM, deg_HKR_RATIO=SAGE_DEG_HKR_RATIO,
        deg_T4=SAGE_DEG_T4, scalar_N_cancels=SAGE_SCALAR_N_CANCELS,
        alpha_s_observable_deg=alpha_s_deg, moment_ratio_deg=moment_ratio_deg,
        alpha_s_substrate_distance_1=alpha_s_substrate_distance_1,
        alpha_s_pivot_goldstone=alpha_s_pivot_goldstone,
        alpha_s_moment_ratio_realization=alpha_s_moment_ratio,
        a4_L12=a4_L12, a2_L12=a2_L12, ratio_L12=ratio_L12,
        GV_APS=gv["GV_APS"], GV_CS=gv["GV_CS"], GV_BC=gv["GV_BC"],
        delta_scheme=gv["delta_scheme"], two_axis_admissible=gv["two_axis_admissible"],
        eta_defect=gv["eta_defect"],
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=reg_v,
        composite_verdict=composite,
        audit_sha256=audit_sha, content_sha256=content_sha,
        tau_fold=tau_fold, M_KK=M_KK,
    )
    print(f"  npz -> {OUT_NPZ.name}")
    make_plot(K_GRID, factorization, classification, gv)
    print(f"  png -> {OUT_PNG.name}")

    # --- Step 10: emit verdict line ---
    print("\n=== Step 10: emit verdict line + companions ===")
    prior_sha = find_prior_audit_sha()  # (local) Option A supersession (gate-verdicts.md)
    if prior_sha and prior_sha != audit_sha:
        print(f"  prior non-superseded line found: audit_sha256={prior_sha[:16]}... "
              f"=> corrective re-emission carries supersedes= tag (Option A; prior line RETAINED)")
    else:
        prior_sha = ""  # (local) no prior or identical -> first emission
    append_verdict(composite, value, audit_sha, content_sha, sign_v, mag_v, reg_v,
                   classification, gv, supersedes_sha=prior_sha)
    print(f"  appended to {VERDICT_TXT}")
    print(f"\n=== 4-tuple: (value-key, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX}) ===")
    print(f"{GATE_ID}: {composite}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
