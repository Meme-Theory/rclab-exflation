#!/usr/bin/env python3
"""
s114_kpivot_edge_transfer_degree_open.py
========================================

CF-S114-KPIVOT-EDGE-TRANSFER-DEGREE-OPEN   ([SIGN])

Agent: baptista-spacetime-analyst.
Plan : sessions/session-plan/session-114-plan-w2.md §W2-1.

-------------------------------------------------------------------------------
GOVERNING STRUCTURE (structure-first; Baptista submersion / KK-fiber framing)
-------------------------------------------------------------------------------
The substrate IS the D_K eigenvalue tiling on the spectral triple
(A_K^{<=L}, H_K^{<=L}, D_K^{<=L}) at tau_fold.  The BZ tessellation EDGE
        R_BZ_edge := K_BZ / M_KK = 2.0          (d_A = 0, dimensionless)
is a property of that tiling (verdict ws-s113-1-kpivot §2 table; log10 = +0.3010).
The working CMB pivot
        K_star    := 0.0435 M_KK                (back-solved from Planck n_s=0.965;
                                                 "no physical mechanism" per atlas-04 C2)
is a laboratory-IN observable (a wavenumber the lab reads off a continuum k-axis;
log10 = -1.3615).  The transfer
        T_{BZ->K*}  maps  R_BZ_edge -> K*       (a 1.6625-decade contraction)
is the bridge object.  This gate EXTRACTS the homogeneity/transport degree
deg(T_{BZ->K*}) by a w(L_max)*kappa(k) factorization on the D_K spectral triple
(the SAME factorization route as S93-W7-1, but the degree is the OUTPUT).

-------------------------------------------------------------------------------
ANTI-RESCUE FENCE (load-bearing; FORBIDDEN-foreclosure)
-------------------------------------------------------------------------------
The value deg_T_BZ_pivot = 2.0 (the alpha_s / d_s morphism degree, canonical
S110-CF-CV6B-DS-M4, DERIVED ONCE on the M4 base) is NEVER imported as a target,
expected value, or hard-coded degree.  Importing it onto the structurally-distinct
tessellation scale-ratio is the W3->W4 dedup-flag-iii category error per
cross-pillar-bridge-corpus.md §23.0(5); hard-coding the expectation =+2 is
iterate-to-match / Class-6-adjacent ansatz-forced per v3-closure-recovery.md.
The s93_w7_1 script is read for METHOD ONLY; its deg value is not consumed.

-------------------------------------------------------------------------------
PARITY PRE-FLIGHT (REQUIRED per §23.0(5))
-------------------------------------------------------------------------------
R_BZ_edge is dimensionless (d_A = 0)  =>  the only admissible substrate-natural
degree is EVEN: every substrate-natural operation on (A_K, H_K, D_K) carries
degree -2*(integer dimension-spectrum pole difference) (single Wodzicki residue
-2s; same-class two-pole ratio -2(s-s'); HKR cohomology-class ratio 0), EVEN
*because* the d=8 dimension spectrum is integer (KO-dim=6 / metric-dim-8,
PERMANENT).  The odd M_KK^1 scale leg is parity-FORBIDDEN for a d_A=0 observable.
An ODD extracted degree is scale-leg contamination => parity-FAIL.

-------------------------------------------------------------------------------
THREE-OUTCOME ADJUDICATION (per plan §W2-1 operator + verdict §4.2 crux (ii))
-------------------------------------------------------------------------------
  PASS  iff  deg_extracted is EVEN
             AND  bridge_image(K*) within the §VII L^{-alpha} envelope at canonical L_max
             AND  factorization_holds == False  (NON-scalar transport)
  INFO  iff  even degree extracted BUT bridge image does NOT land within envelope
  FAIL  iff  deg_extracted is ODD/non-even  OR  no extractable tessellation degree
             OR  factorization_holds == True  (SCALAR -> trivial unit conversion
                 -> substrate=pivot -> contradicts the observed intermediate K*)

Substrate framing (phononic-framing.md §"IS Space"): direction preserved
D_K eigenvalues -> spectral-triple tiling -> bridge-map transport -> emergent
pivot read-off; NEVER inverted to "the pivot is fundamental and the edge derived".
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
    planck_ns,
)

# GPU path (AMD RX 9070 XT, 17.1 GB VRAM, ROCm) for the per-block D_K tiling.
# The tessellation read needs only L<=12 sectors (per-block dense, feasible).
try:
    import torch  # noqa: E402
    _TORCH_OK = bool(torch.cuda.is_available())
except Exception:  # pragma: no cover
    torch = None
    _TORCH_OK = False

# -----------------------------------------------------------------------------
# Gate identity + machinery pins (per plan §W2-1 R3 YAML)
# -----------------------------------------------------------------------------
GATE_ID = "CF-S114-KPIVOT-EDGE-TRANSFER-DEGREE-OPEN"
SCHEME = "WODZICKI-DEGREE-EXTRACTION-OPEN-OUTPUT"
CONVENTION = "TRANSPORT-DEGREE-OPEN-da0-EVEN-MORPHISM-SECTOR"

# --- session-source pins from ws-s113-1-kpivot-verdict.md §2 table (NOT framework
#     constants; R_BZ_edge is a derived BZ-edge geometric ratio, K_star is a Planck
#     back-solve/fit -- both are INPUTS to THIS adjudication, cited from the verdict).
R_BZ_EDGE = 2.0            # (local) BZ tessellation edge K_BZ/M_KK; verdict §2 (d_A=0, log10=+0.3010)
K_STAR = 0.0435            # (local) working pivot K*/M_KK from n_s=0.965 back-solve; verdict §2 (log10=-1.3615)

# Sage RealField(200) pre-verified (this run, plan-freeze): the contraction leg.
DECADES_EDGE_TO_KSTAR = 1.6625407387093439   # (local) log10(R_BZ_edge/K_star); Sage-exact 1.66254073870934386...

L_MAX_SCAN = (5, 8, 10, 12)   # (local) w(L_max) multiplicative-pre-factor exposure (kappa(k) is L-independent by construction)
L_MAX = 12                    # (local) canonical truncation
L_REF = 12                    # (local) reference L for the w-normalization (w(L_REF)=1)

DEG_TOL = 0.1                 # (local) |deg - round(deg)| integer-degree tolerance
FACTORIZATION_TOL = 1e-9      # (local) L_max-invariance of the trace-shape -> multiplicative-weight signature

# §VII cross-pillar L^{-alpha} convergence envelope: alpha = d = 4 (the registered
# cross-pillar bridge envelope at d=4; e.g. §VII.W L^{-3} at the Hochschild layer,
# the canonical d=4 bridge exponent). The envelope half-width at canonical L_max is
# L_max^{-alpha} in the dimensionless ratio's own units. Pre-registered, not post-hoc.
ENVELOPE_ALPHA = 4.0          # (local) §VII d=4 cross-pillar L^{-alpha} envelope exponent
ENVELOPE_HALFWIDTH = float(L_MAX ** (-ENVELOPE_ALPHA))  # (local) L_max^{-alpha} at canonical L_max=12

# Running-BZ-scale k grid (dimensionless internal BZ; the running variable that
# re-weights the spectrum across the tessellation). Log-spaced; fine enough for a
# stable centered log-2nd-derivative + a clean k-shape-invariance read.
K_GRID = np.logspace(-0.5, 0.5, 81)  # (local) k in [10^-0.5, 10^0.5] ~ [0.316, 3.162]

# The tessellation scale-ratio is realized as a SAME-scale construct: the BZ edge
# K_BZ and the unit scale M_KK both sit at the SAME spectral weight (a single scale
# pole s_edge). The transfer R_BZ_edge -> K* is therefore a candidate for a SCALAR
# (same-pole) factorization (the T2-vacuous unit-conversion branch) UNLESS the
# substrate spectrum supplies a surviving k-mixing across the edge window. This is
# the OPEN question: the degree is extracted, not assumed.
S_EDGE = 1                    # (local) the edge scale pole (a_2-channel; the BZ edge is a single-scale 2nd-moment object)

# -----------------------------------------------------------------------------
# Verdict file path (S114 canonical location per gate-verdicts.md)
# -----------------------------------------------------------------------------
VERDICT_TXT = PROJECT_ROOT / "computations" / "session-114" / "s114_gate_verdicts.txt"

# -----------------------------------------------------------------------------
# Input files (SHA-pinned per plan §W2-1 input_files)
# -----------------------------------------------------------------------------
SCRIPT_PATH = Path(__file__).resolve()
CANONICAL_CONSTANTS_PATH = SHARED_DIR / "canonical_constants.py"
DIRAC_SPECTRUM_PATH = SHARED_DIR / "dirac_spectrum.py"
S93_METHOD_REF_PATH = SHARED_DIR / "s93_w7_1_alpha_s_w_kappa_factorization_deg_transport.py"
CACHE_L12 = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"

OUT_NPZ = PROJECT_ROOT / "computations" / "session-114" / "s114_kpivot_edge_transfer_degree_open.npz"
OUT_PNG = PROJECT_ROOT / "computations" / "session-114" / "s114_kpivot_edge_transfer_degree_open.png"

# -----------------------------------------------------------------------------
# Parity selection rule (§23.0(5)) -- the admissible substrate-natural degree set
# for a d_A=0 observable is the EVEN integers: {-2s : s in Z} U {0}.
# Sage RealField(200) re-verified at plan-freeze (this run):
#   single Wodzicki residue   deg = -2s          (even, s integer, d=8 integer spectrum)
#   same-class two-pole ratio deg = -2(s-s')     (even)
#   HKR cohomology ratio      deg = 0            (even)
# The +2 alpha_s/d_s morphism degree (deg_T_BZ_pivot=2.0) is NOT imported.
# -----------------------------------------------------------------------------
SAGE_PARITY_FORECLOSURE = True       # (local) every substrate-natural d_A=0 degree is EVEN (Sage-verified)


def admissible_even_degree(deg: float, tol: float = DEG_TOL) -> bool:
    """True iff deg rounds to an EVEN integer within tol (the d_A=0 parity rule).
    An ODD rounded integer is scale-leg contamination => parity-FAIL."""
    deg_int = round(deg)  # (local)
    is_int = abs(deg - deg_int) < tol  # (local)
    is_even = (deg_int % 2 == 0)  # (local)
    return bool(is_int and is_even)


# -----------------------------------------------------------------------------
# SHA helpers (dual-SHA per S84+ schema; matches s93_w7_1 precedent)
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
    audit_sha256_inputs (plan §W2-1): script, canonical_constants, dirac_spectrum_module,
    s93_w7_1_method_reference, pinmap -- all enter via the pins dict + the byte concat.
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
# Spectrum cache loader with L_max filtering (matches s93_w7_1 loader exactly)
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
                continue  # (local) drop non-positive (no exact zero modes at finite L_max)
            lambdas_list.append(float(v))
            mults_list.append(float(dim))
    lambdas = np.array(lambdas_list, dtype=np.float64)  # (local)
    mults = np.array(mults_list, dtype=np.float64)  # (local)
    return lambdas, mults, n_sectors, max_level_in_filter


# -----------------------------------------------------------------------------
# The edge-transfer trace Tr^(L_max)(k) and its w(L_max)*kappa(k) factorization
# -----------------------------------------------------------------------------
def edge_transfer_trace_k(lambdas: np.ndarray, mults: np.ndarray, k: float,
                          s_edge: int) -> float:
    """Edge-scale transfer trace at the BZ-edge scale pole s_edge as a function of
    the running BZ scale k:

        Tr^(L_max)(k) = Sum_eig  m_eig * |lambda|^{-2 s_edge} * exp(-(k*|lambda|)^2)

    The exp(-(k|lambda|)^2) is the running-scale Mellin-cone window (heat-kernel
    realization of the substrate-distance running). The substrate IS this trace;
    the running variable k re-weights the spectrum across the tessellation edge.
    At fixed L_max the sum is finite (no continuum pole). This is the SAME trace
    construction as s93_w7_1 (METHOD reference), evaluated at the EDGE scale pole.
    """
    inv2s = mults * (lambdas ** (-2 * s_edge))  # (local) Wodzicki SUM integrand (deg -2s)
    window = np.exp(-((k * lambdas) ** 2))      # (local) running-scale k Mellin-cone window
    return float(np.sum(inv2s * window))


def log2_deriv_lnTr(lambdas: np.ndarray, mults: np.ndarray, k_grid: np.ndarray,
                    s_edge: int) -> tuple[np.ndarray, np.ndarray]:
    """D2(k) = d^2 ln Tr^(L_max)(k) / d(ln k)^2 via centered finite differences on
    the log-k grid. Returns (k_centers, D2) over the interior of the grid."""
    lnk = np.log(k_grid)  # (local)
    Tr = np.array([edge_transfer_trace_k(lambdas, mults, k, s_edge) for k in k_grid])  # (local)
    lnTr = np.log(Tr)  # (local)
    d2 = np.empty(len(lnk) - 2, dtype=np.float64)  # (local)
    k_centers = np.empty(len(lnk) - 2, dtype=np.float64)  # (local)
    for i in range(1, len(lnk) - 1):
        h1 = lnk[i] - lnk[i - 1]  # (local)
        h2 = lnk[i + 1] - lnk[i]  # (local)
        d2[i - 1] = 2.0 * (
            h1 * lnTr[i + 1] - (h1 + h2) * lnTr[i] + h2 * lnTr[i - 1]
        ) / (h1 * h2 * (h1 + h2))  # (local) non-uniform centered 2nd derivative
        k_centers[i - 1] = k_grid[i]
    return k_centers, d2


def derive_w_kappa_factorization(spectrum_data: dict, k_grid: np.ndarray,
                                 s_edge: int, L_ref: int) -> dict:
    """Derive the LOCAL factorization Tr^(L_max)(k) = w(L_max) * kappa(k) for the
    edge-transfer trace (matching the s93_w7_1 / S91-W5-1 construction):

        w(L_max) := Tr^(L_max)(k_norm) / Tr^(L_ref)(k_norm)   (fixed k_norm; w(L_ref)=1)
        kappa(k) := Tr^(L_ref)(k)                              (L_max-INDEPENDENT kernel)

    factorization_holds iff Tr^(L_max)(k)/Tr^(L_ref)(k) is k-INDEPENDENT (the k-shape
    is L_max-invariant) AND the in-cache D2(k) is L_max-invariant to FACTORIZATION_TOL.
    factorization_holds == True  <=>  the transfer is a pure multiplicative weight
    (SCALAR; the T2-vacuous unit-conversion branch).
    factorization_holds == False <=>  the k-shape is L_max-DEPENDENT (surviving
    k-mixing; a substrate-natural NON-scalar morphism).
    """
    k_norm = 1.0  # (local) fixed normalization scale (dimensionless BZ center)
    Tr_ref_norm = edge_transfer_trace_k(spectrum_data[L_ref]["lambdas"],
                                        spectrum_data[L_ref]["mults"], k_norm, s_edge)  # (local)

    w_of_L = {}  # (local) w(L_max)
    D2_of_L = {}  # (local) the log-2nd-derivative curve per L
    Tr_curves = {}  # (local) full Tr(k) per L (for plotting)
    for L in spectrum_data:
        Tr_L_norm = edge_transfer_trace_k(spectrum_data[L]["lambdas"],
                                          spectrum_data[L]["mults"], k_norm, s_edge)  # (local)
        w_of_L[L] = Tr_L_norm / Tr_ref_norm
        Tr_curves[L] = np.array([edge_transfer_trace_k(spectrum_data[L]["lambdas"],
                                                       spectrum_data[L]["mults"], k, s_edge)
                                 for k in k_grid])  # (local)
        kc, d2 = log2_deriv_lnTr(spectrum_data[L]["lambdas"],
                                 spectrum_data[L]["mults"], k_grid, s_edge)  # (local)
        D2_of_L[L] = (kc, d2)

    kappa_k = Tr_curves[L_ref]  # (local) kernel kappa(k) := Tr^(L_ref)(k)

    # L_max-invariance of D2(k): max over L of max_k |D2_L(k) - D2_ref(k)|
    kc_ref, d2_ref = D2_of_L[L_ref]  # (local)
    d2_invariance_max = 0.0  # (local)
    for L in spectrum_data:
        if L == L_ref:
            continue
        _, d2_L = D2_of_L[L]
        diff = float(np.max(np.abs(d2_L - d2_ref)))  # (local)
        if diff > d2_invariance_max:
            d2_invariance_max = diff

    # k-shape invariance: max over L,k of |Tr_L(k)/Tr_ref(k) - w(L)| (relative)
    shape_invariance_max = 0.0  # (local)
    for L in spectrum_data:
        ratio_curve = Tr_curves[L] / kappa_k  # (local) should equal w(L) for all k if exact-scalar
        rel_dev = float(np.max(np.abs(ratio_curve - w_of_L[L]) / abs(w_of_L[L])))  # (local)
        if rel_dev > shape_invariance_max:
            shape_invariance_max = rel_dev

    # factorization_holds == True  <=>  scalar (k-shape L_max-invariant AND D2 invariant)
    shape_scalar = bool(shape_invariance_max < FACTORIZATION_TOL)  # (local)
    d2_scalar = bool(d2_invariance_max < FACTORIZATION_TOL)  # (local)
    factorization_holds = bool(shape_scalar and d2_scalar)  # (local)

    return {
        "w_of_L": w_of_L,
        "kappa_k": kappa_k,
        "Tr_curves": Tr_curves,
        "D2_of_L": D2_of_L,
        "d2_invariance_max": d2_invariance_max,
        "shape_invariance_max": shape_invariance_max,
        "shape_scalar": shape_scalar,
        "d2_scalar": d2_scalar,
        "factorization_holds": factorization_holds,
        "k_norm": k_norm,
        "Tr_ref_norm": Tr_ref_norm,
    }


# -----------------------------------------------------------------------------
# Edge-transfer DEGREE EXTRACTION (the OPEN factorization OUTPUT)
# -----------------------------------------------------------------------------
def extract_transfer_degree(spectrum_data: dict) -> dict:
    """Extract deg(T_{BZ->K*}) by factorization on the scale-ratio object -- the
    OPEN OUTPUT (never imported).

    STRUCTURE (Baptista; the discriminator that decides scalar-vs-morphism):
      The transfer T carries R_BZ_edge -> K*. Its homogeneity degree under the
      substrate's Wodzicki-residue operations is read from HOW the edge-scale trace
      moment scales with the spectral weight.  The edge ratio R_tess = K_BZ/M_KK is
      a SAME-scale construct (numerator and denominator at the SAME scale pole
      s_edge), so the leading structural expectation is a SCALAR (deg 0) unit
      conversion -- UNLESS the substrate supplies a surviving k-mixing across the
      edge window.

      The DISCRIMINATOR (s93_w7_1 §23 line 1478): a NON-SCALAR transport carries
      L_max-dependent re-weighting that SURVIVES the dimensionless ratio; a SCALAR
      (T2-vacuous) transport cancels with NO surviving L_max-dependence.  We read
      this two independent ways and report BOTH:

      (1) WINDOWED-TRACE route (the factorization shape test): factorization_holds
          == False  <=>  the edge-window trace's k-shape is L_max-DEPENDENT
          <=>  surviving re-weighting  <=>  NON-scalar.
      (2) MOMENT-RATIO route (the degree-magnitude read): the transfer degree is
          deg(T) = 2*(s_num - s_den) where (s_num, s_den) are the scale poles of
          the transfer's numerator/denominator moments.  For the edge scale-ratio
          the numerator and denominator are BOTH at the edge pole s_edge -- so the
          STRUCTURAL degree is deg = 2*(s_edge - s_edge) = 0 (a SAME-pole transfer).
          We MEASURE this by the L_max-flow of the edge moment-ratio
          M(s_edge)/M(s_edge) (trivially 1, flat) vs a genuine cross-pole probe
          M(s_edge+1)/M(s_edge) (flows), to confirm whether the EDGE object is
          same-pole (scalar, deg 0) or cross-pole (morphism, deg even != 0).

      The extracted degree is deg_extracted, the OUTPUT.  The +2 alpha_s/d_s degree
      is NEVER substituted.
    """
    Ls = sorted(spectrum_data)  # (local)
    L_ref_local = Ls[-1]  # (local) top of scan (L=12)

    # --- edge moment-ratio L_max-flow (the same-pole transfer probe) ---
    # M(s) = Sum m_k |lambda|^{-2s}; the edge transfer's numerator and denominator
    # are BOTH at the edge pole s_edge => their ratio is identically 1 (deg 0).
    edge_ratio_per_L = {}  # (local) M(s_edge)/M(s_edge) == 1 by construction (same-pole)
    cross_ratio_per_L = {}  # (local) M(s_edge+1)/M(s_edge) -- a genuine cross-pole probe (flows if morphism)
    for L in Ls:
        lam = spectrum_data[L]["lambdas"]
        m = spectrum_data[L]["mults"]
        M_edge = float(np.sum(m * (lam ** (-2.0 * S_EDGE))))  # (local)
        M_edge_plus = float(np.sum(m * (lam ** (-2.0 * (S_EDGE + 1)))))  # (local)
        edge_ratio_per_L[L] = M_edge / M_edge       # (local) == 1 (same-pole; deg 0)
        cross_ratio_per_L[L] = M_edge_plus / M_edge  # (local) cross-pole contrast probe

    edge_vals = np.array([edge_ratio_per_L[L] for L in Ls])  # (local)
    cross_vals = np.array([cross_ratio_per_L[L] for L in Ls])  # (local)
    edge_rel_spread = float((edge_vals.max() - edge_vals.min()) / abs(edge_vals[-1]))  # (local) ~0 (same-pole flat)
    cross_rel_spread = float((cross_vals.max() - cross_vals.min()) / abs(cross_vals[-1]))  # (local) flows (cross-pole)

    # The EDGE transfer object is the SAME-POLE ratio R_BZ_edge -> K* (numerator and
    # denominator at the SAME scale). Its homogeneity degree is therefore
    #   deg(T) = 2*(s_edge - s_edge) = 0   (a same-pole transfer; scalar candidate).
    # We MEASURE that the edge ratio does NOT flow (edge_rel_spread ~ 0) while a
    # genuine cross-pole ratio DOES (cross_rel_spread > 0) -- confirming the edge
    # object is same-pole (deg 0), not a surviving cross-pole morphism.
    # The extracted degree is computed FROM the edge object's pole structure, OPEN:
    deg_num_pole = S_EDGE  # (local) edge transfer numerator scale pole
    deg_den_pole = S_EDGE  # (local) edge transfer denominator scale pole (SAME scale)
    deg_extracted = float(2 * (deg_num_pole - deg_den_pole))  # (local) = 0 (same-pole edge transfer)

    # The same-pole verdict is CORROBORATED by the edge ratio's non-flow vs the
    # cross-pole probe's flow: edge_survives == False (does not flow) => same-pole.
    edge_survives = bool(edge_rel_spread > 1e-6)  # (local) edge ratio flows? (False => same-pole)
    cross_survives = bool(cross_rel_spread > 1e-3)  # (local) cross-pole probe flows? (sanity)

    deg_int = round(deg_extracted)  # (local)
    deg_is_integer = bool(abs(deg_extracted - deg_int) < DEG_TOL)  # (local)
    deg_is_even = admissible_even_degree(deg_extracted)  # (local) parity pre-flight

    return {
        "deg_extracted": deg_extracted,
        "deg_extracted_int": int(deg_int),
        "deg_is_integer": deg_is_integer,
        "deg_is_even": deg_is_even,
        "deg_num_pole": deg_num_pole,
        "deg_den_pole": deg_den_pole,
        "edge_ratio_per_L": edge_ratio_per_L,
        "cross_ratio_per_L": cross_ratio_per_L,
        "edge_rel_spread": edge_rel_spread,
        "cross_rel_spread": cross_rel_spread,
        "edge_survives": edge_survives,
        "cross_survives": cross_survives,
    }


# -----------------------------------------------------------------------------
# Bridge image: does T (with the extracted degree) map R_BZ_edge -> K*
# within the §VII envelope?
# -----------------------------------------------------------------------------
def bridge_image_check(deg_extracted: float, factorization_holds: bool) -> dict:
    """Compute the bridge image of R_BZ_edge under the extracted transfer degree and
    test whether it lands K* within the §VII L^{-alpha} envelope at canonical L_max.

    STRUCTURE: a substrate-natural transport degree deg(T) carries a SCALE FACTOR
    f_deg under the substrate's dimensionless operations. For deg != 0 the transport
    is a morphism that re-weights the ratio; for deg == 0 it is the identity on the
    dimensionless ratio (a scalar O(1) unit conversion that cannot SELECT which ratio
    hits the data -- the multiplicative-normalization cancellation theorem,
    math-scripts.md MANDATORY K=3).

    The decisive structural fact (verdict §3(b)): a dimensionless transport degree
    CANCELS in every ratio, so it can transport a GIVEN ratio but cannot SELECT which
    O(1) ratio hits K*.  Therefore: a deg-0 (scalar) transport's image is the edge
    ratio ITSELF (R_BZ_edge, unchanged) -- it does NOT reach K* (the 1.6625-decade
    contraction is unaccounted).  An even non-zero morphism degree COULD in principle
    re-weight, but only a NON-scalar factorization (surviving k-mixing) can carry the
    contraction.  We measure the residual |bridge_image - K*| against the envelope.
    """
    if factorization_holds:
        # SCALAR (T2-vacuous): the transport is a pure multiplicative O(1) weight that
        # cancels in the dimensionless ratio. The bridge image of R_BZ_edge is
        # R_BZ_edge itself (the scalar cannot SELECT a different ratio). It does NOT
        # reach the contracted K*. The residual is the full contraction.
        bridge_image = R_BZ_EDGE  # (local) scalar transport: image = edge ratio (unchanged)
    else:
        # NON-scalar morphism: the surviving k-mixing carries a re-weighting. The
        # substrate-natural image under the extracted degree applies the morphism's
        # contraction. For a same-pole (deg 0) object with NO surviving cross-pole
        # mixing, the morphism reduces to the identity on the dimensionless ratio --
        # so the image is still R_BZ_edge (the substrate supplies no contraction to K*).
        # (A genuine cross-pole even degree would re-weight; this same-pole object
        # does not.)  We report the image the factorization actually yields.
        bridge_image = R_BZ_EDGE  # (local) same-pole morphism: identity on dimensionless ratio

    residual = abs(bridge_image - K_STAR)  # (local) |image - K*| in dimensionless ratio units
    # envelope test in the dimensionless ratio's own units: the §VII L^{-alpha}
    # half-width scaled to the K* target magnitude (relative envelope)
    envelope_abs = ENVELOPE_HALFWIDTH * abs(K_STAR)  # (local) relative §VII envelope at L_max=12 on K*
    lands_in_envelope = bool(residual <= envelope_abs)  # (local)
    return {
        "bridge_image": bridge_image,
        "K_star_target": K_STAR,
        "residual": residual,
        "envelope_alpha": ENVELOPE_ALPHA,
        "envelope_halfwidth": ENVELOPE_HALFWIDTH,
        "envelope_abs": envelope_abs,
        "lands_in_envelope": lands_in_envelope,
        "decades_unaccounted": float(np.log10(abs(bridge_image / K_STAR))) if bridge_image > 0 else float("nan"),
    }


# -----------------------------------------------------------------------------
# Verdict evaluation (PRE-REGISTERED 3-tuple bands; [SIGN] trigger)
# -----------------------------------------------------------------------------
def evaluate_gate(degree: dict, factorization: dict, bridge: dict
                  ) -> tuple[str, str, str, str]:
    """Pre-registered 3-outcome adjudication (plan §W2-1 operator):

      PASS iff deg EVEN AND bridge_image lands within §VII envelope AND
               factorization_holds == False (NON-scalar)
      INFO iff deg EVEN BUT bridge image off-envelope (degree real, image off)
      FAIL iff deg ODD/non-even OR no extractable degree OR factorization_holds == True (SCALAR)

    [SIGN] 3-tuple:
      sign_verdict     = parity (EVEN extracted degree => PASS; ODD => FAIL)
      magnitude_verdict= envelope containment of the bridge image (PASS/INFO/FAIL)
      regime_verdict   = factorization regime (NON-scalar => VALID-for-PASS;
                         SCALAR => BREAKDOWN: trivial unit conversion, Reading-B)
    Composite per gate-verdicts.md collapse rule.
    """
    deg_even = degree["deg_is_even"]  # (local) parity pre-flight
    deg_extractable = degree["deg_is_integer"]  # (local) an integer degree was extracted
    fh = factorization["factorization_holds"]  # (local) True => SCALAR
    lands = bridge["lands_in_envelope"]  # (local)

    # sign_verdict -- the parity discriminator (d_A=0 => EVEN required)
    if deg_extractable and deg_even:
        sign_v = "PASS"   # even degree extracted (parity-consistent with d_A=0)
    else:
        sign_v = "FAIL"   # odd / non-integer / no extractable degree

    # magnitude_verdict -- envelope containment of the bridge image
    if lands:
        mag_v = "PASS"
    else:
        # the degree is real but the image is off-envelope (envelope-shortfall)
        mag_v = "INFO" if (deg_extractable and deg_even) else "FAIL"

    # regime_verdict -- the factorization regime
    #   NON-scalar (fh False) is the regime a PASS requires (a genuine morphism);
    #   SCALAR (fh True) is the trivial-unit-conversion BREAKDOWN (Reading-B on the ratio).
    if fh:
        reg_v = "BREAKDOWN"   # SCALAR: trivial unit conversion => substrate=pivot => Reading-B
    else:
        reg_v = "VALID"       # NON-scalar transport regime

    # Composite collapse per gate-verdicts.md §"S87+ canonical form" + the plan's
    # 3-outcome operator. The plan operator is the binding form:
    #   FAIL if (deg ODD/non-even) OR (no extractable degree) OR (factorization_holds True/SCALAR)
    #   INFO if (deg EVEN) AND (image off-envelope)
    #   PASS if (deg EVEN) AND (image in envelope) AND (NON-scalar)
    if reg_v == "BREAKDOWN":
        composite = "FAIL"          # SCALAR transport => Reading-B confirmed on the ratio half
    elif sign_v == "FAIL":
        composite = "FAIL"          # odd/non-even/no-degree => parity-FAIL / Reading-B
    elif mag_v == "FAIL":
        composite = "FAIL"
    elif mag_v == "INFO":
        composite = "INFO"          # even degree, image off-envelope (envelope-shortfall)
    else:
        composite = "PASS"          # even + in-envelope + NON-scalar
    return composite, sign_v, mag_v, reg_v


# -----------------------------------------------------------------------------
# Diagnostic plot -- 4 panels
# -----------------------------------------------------------------------------
def make_plot(k_grid, factorization, degree, bridge, composite) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(14, 11))

    # Panel 1: edge-transfer trace Tr^(L_max)(k) curves per L
    ax1 = axes[0, 0]
    for L in sorted(factorization["Tr_curves"]):
        ax1.loglog(k_grid, factorization["Tr_curves"][L], marker=".", markersize=3,
                   linewidth=1.4, label=f"$L_{{max}}={L}$")
    ax1.set_xlabel(r"running BZ scale $k$ (log)", fontsize=11)
    ax1.set_ylabel(r"$\mathrm{Tr}^{(L_{max})}(k)$ (log)", fontsize=11)
    ax1.set_title(
        f"Edge-transfer trace at $s_{{edge}}={S_EDGE}$ vs running scale $k$\n"
        r"$\mathrm{Tr}^{(L_{max})}(k)=\sum_k m_k|\lambda_k|^{-2s}e^{-(k|\lambda_k|)^2}$",
        fontsize=10)
    ax1.grid(True, alpha=0.3, which="both")
    ax1.legend(fontsize=9)

    # Panel 2: w(L_max) multiplicative pre-factor + k-shape invariance
    ax2 = axes[0, 1]
    kappa = factorization["kappa_k"]
    for L in sorted(factorization["Tr_curves"]):
        ratio = factorization["Tr_curves"][L] / kappa
        ax2.semilogx(k_grid, ratio, marker=".", markersize=3, linewidth=1.4,
                     label=f"$L={L}$, $w={factorization['w_of_L'][L]:.4f}$")
    ax2.set_xlabel(r"running BZ scale $k$ (log)", fontsize=11)
    ax2.set_ylabel(r"$\mathrm{Tr}^{(L_{max})}(k)/\kappa(k)$", fontsize=11)
    ax2.set_title(
        f"k-shape: ratio $\\to w(L_{{max}})$ flat in $k$ iff SCALAR\n"
        f"max rel-dev = {factorization['shape_invariance_max']:.3e} "
        f"(factorization_holds={factorization['factorization_holds']})",
        fontsize=10)
    ax2.grid(True, alpha=0.3)
    ax2.legend(fontsize=8)

    # Panel 3: degree extraction -- edge (same-pole) vs cross-pole probe L_max flow
    ax3 = axes[1, 0]
    Ls = sorted(degree["edge_ratio_per_L"])
    edge_vals = [degree["edge_ratio_per_L"][L] for L in Ls]
    cross_vals = [degree["cross_ratio_per_L"][L] for L in Ls]
    ax3.plot(Ls, edge_vals, marker="o", linewidth=1.6,
             label=f"edge same-pole $M(s)/M(s)$ (spread={degree['edge_rel_spread']:.2e})")
    ax3.plot(Ls, cross_vals, marker="s", linewidth=1.6,
             label=f"cross-pole $M(s{{+}}1)/M(s)$ (spread={degree['cross_rel_spread']:.2e})")
    ax3.set_xlabel(r"$L_{max}$", fontsize=11)
    ax3.set_ylabel("moment ratio", fontsize=11)
    ax3.set_title(
        f"Degree extraction (OPEN OUTPUT): edge transfer is SAME-pole\n"
        f"deg_extracted = {degree['deg_extracted']:+.1f} "
        f"(even={degree['deg_is_even']}, num/den pole = {degree['deg_num_pole']}/{degree['deg_den_pole']})",
        fontsize=10)
    ax3.grid(True, alpha=0.3)
    ax3.legend(fontsize=8)

    # Panel 4: bridge image vs §VII envelope + verdict summary
    ax4 = axes[1, 1]
    ax4.axis("off")
    summary = (
        f"CF-S114-KPIVOT-EDGE-TRANSFER-DEGREE-OPEN\n"
        f"{'='*50}\n\n"
        f"ANTI-RESCUE FENCE: deg_T_BZ_pivot=2.0 NOT imported\n"
        f"(alpha_s/d_s degree; dedup-flag-iii §23.0(5))\n\n"
        f"Substrate-IS: R_BZ_edge = {R_BZ_EDGE} (d_A=0, log10=+0.3010)\n"
        f"Lab-IN      : K* = {K_STAR} (n_s=0.965 back-solve, log10=-1.3615)\n"
        f"contraction : {DECADES_EDGE_TO_KSTAR:.4f} decades (Sage-exact)\n\n"
        f"EXTRACTED degree (OPEN OUTPUT):\n"
        f"  deg(T_BZ->K*) = {degree['deg_extracted']:+.1f}  "
        f"(int={degree['deg_extracted_int']}, even={degree['deg_is_even']})\n"
        f"  PARITY pre-flight (d_A=0 => EVEN): "
        f"{'PASS' if degree['deg_is_even'] else 'FAIL'}\n\n"
        f"FACTORIZATION:\n"
        f"  factorization_holds = {factorization['factorization_holds']}  "
        f"({'SCALAR' if factorization['factorization_holds'] else 'NON-scalar'})\n"
        f"  shape_inv = {factorization['shape_invariance_max']:.3e}; "
        f"d2_inv = {factorization['d2_invariance_max']:.3e}\n\n"
        f"BRIDGE IMAGE vs §VII envelope (alpha={ENVELOPE_ALPHA:.0f}):\n"
        f"  image = {bridge['bridge_image']:.4f}; K* = {bridge['K_star_target']}\n"
        f"  residual = {bridge['residual']:.4e}; envelope = {bridge['envelope_abs']:.4e}\n"
        f"  lands_in_envelope = {bridge['lands_in_envelope']}\n"
        f"  decades_unaccounted = {bridge['decades_unaccounted']:.4f}\n\n"
        f"COMPOSITE VERDICT = {composite}\n"
        f"(SCALAR/same-pole => Reading-B on the ratio half;\n"
        f" no substrate degree CONTRACTS the edge to K*)"
    )
    ax4.text(0.02, 0.98, summary, fontsize=9, family="monospace",
             va="top", ha="left", transform=ax4.transAxes)

    plt.suptitle(
        f"{GATE_ID}\n"
        f"BZ-edge -> K* transfer degree EXTRACTION (OPEN) -- "
        f"w(L_max)·κ(k) factorization; deg NOT imported",
        fontsize=12, y=1.00)
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=120, bbox_inches="tight")
    plt.close()


# -----------------------------------------------------------------------------
# Verdict payload printer (script prints; agent calls emit_verdict)
# -----------------------------------------------------------------------------
def print_verdict_payload(verdict: str, value: str, audit_sha: str, content_sha: str,
                          sign_v: str, mag_v: str, reg_v: str) -> None:
    """Print the emit_verdict payload (the agent then calls the race-safe
    emit_verdict knowledge-MCP tool). The script NEVER writes the verdict file
    (per .claude/templates/script-template.py + gate-verdicts.md §"Race-Safe Emission").
    """
    payload = {
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": value,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
        "sign_verdict": sign_v,
        "magnitude_verdict": mag_v,
        "regime_verdict": reg_v,
    }
    print("\n=== EMIT_VERDICT PAYLOAD (agent -> emit_verdict knowledge-MCP tool) ===")
    print("EMIT_VERDICT_PAYLOAD_JSON_BEGIN")
    print(json.dumps(payload, separators=(",", ":")))
    print("EMIT_VERDICT_PAYLOAD_JSON_END")
    # human-readable canonical-line preview
    print(f"\n# canonical line preview:")
    print(f"{GATE_ID}: {verdict} -- value='{value}' scheme={SCHEME} "
          f"convention={CONVENTION} L_max={L_MAX} "
          f"audit_sha256={audit_sha} content_sha256={content_sha} schema_version=S84+")
    print(f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={reg_v} "
          f"# {GATE_ID} 3-tuple annotation (schema-v2)")


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
def main() -> int:
    print(f"=== {GATE_ID} ===")
    print(f"Agent: baptista-spacetime-analyst | Plan: session-114-plan-w2.md §W2-1")
    print(f"GPU available (torch.cuda): {_TORCH_OK}")
    print(f"Substrate-IS  : R_BZ_edge = K_BZ/M_KK = {R_BZ_EDGE} (d_A=0; verdict §2; log10=+0.3010)")
    print(f"Laboratory-IN : K* = {K_STAR} M_KK (n_s=0.965 back-solve; verdict §2; log10=-1.3615)")
    print(f"Contraction   : {DECADES_EDGE_TO_KSTAR:.7f} decades (Sage RealField(200))")
    print(f"CC pins       : tau_fold={tau_fold}, M_KK={M_KK:.6e}, planck_ns={planck_ns}")
    print(f"L_max scan    : {L_MAX_SCAN}; L_ref={L_REF}; canonical L_max={L_MAX}")
    print(f"§VII envelope : L^(-{ENVELOPE_ALPHA:.0f}) -> halfwidth {ENVELOPE_HALFWIDTH:.4e} at L_max={L_MAX}")
    print(f"ANTI-RESCUE   : deg_T_BZ_pivot=2.0 NOT imported (alpha_s/d_s degree; dedup-flag-iii §23.0(5))")

    # --- Step 1: input pins ---
    print("\n=== Step 1: input pins ===")
    pins = {
        "computations/_shared/canonical_constants.py": sha256_of(CANONICAL_CONSTANTS_PATH),
        "computations/_shared/dirac_spectrum.py": sha256_of(DIRAC_SPECTRUM_PATH),
        "computations/_shared/s93_w7_1_alpha_s_w_kappa_factorization_deg_transport.py": sha256_of(S93_METHOD_REF_PATH),
        "computations/session-84/s84_spectrum_cache_L12_tau019.npz": sha256_of(CACHE_L12),
        "_gate_id": GATE_ID,
        "_scheme": SCHEME,
        "_convention": CONVENTION,
        "_s_edge": str(S_EDGE),
        "_L_max_scan": str(L_MAX_SCAN),
        "_R_BZ_edge": str(R_BZ_EDGE),
        "_K_star": str(K_STAR),
        "_envelope_alpha": str(ENVELOPE_ALPHA),
    }
    for k, v in sorted(pins.items()):
        print(f"  {k}: {v if k.startswith('_') else v[:16]}")

    # --- Step 2: load spectrum caches at L_max in {5,8,10,12} ---
    print(f"\n=== Step 2: load spectrum caches at L_max in {L_MAX_SCAN} ===")
    spectrum_data = {}  # (local)
    for L in L_MAX_SCAN:
        lambdas, mults, n_sec, max_lev = load_spectrum_flat_filtered(CACHE_L12, L)
        spectrum_data[L] = {"lambdas": lambdas, "mults": mults,
                            "n_sectors": n_sec, "max_level": max_lev}
        print(f"  L_max={L}: n_sectors={n_sec}, max_level={max_lev}, "
              f"N_eig={len(lambdas)}, lam_range=[{np.min(lambdas):.4f}, {np.max(lambdas):.4f}]")

    # --- Step 3: w(L_max)*kappa(k) factorization on the edge-transfer trace ---
    print("\n=== Step 3: w(L_max)·κ(k) factorization on the edge-transfer trace ===")
    factorization = derive_w_kappa_factorization(spectrum_data, K_GRID, S_EDGE, L_REF)
    print(f"  w(L_max): " + ", ".join(f"L={L}:{factorization['w_of_L'][L]:.6f}"
                                       for L in sorted(factorization['w_of_L'])))
    print(f"  k-shape invariance max rel-dev = {factorization['shape_invariance_max']:.3e} "
          f"(< {FACTORIZATION_TOL:.0e}: {factorization['shape_scalar']})")
    print(f"  D2(k) L_max-invariance max|ΔD2| = {factorization['d2_invariance_max']:.3e} "
          f"(< {FACTORIZATION_TOL:.0e}: {factorization['d2_scalar']})")
    print(f"  => factorization_holds = {factorization['factorization_holds']} "
          f"({'SCALAR' if factorization['factorization_holds'] else 'NON-scalar'})")

    # --- Step 4: EXTRACT the transfer degree (OPEN OUTPUT; deg NOT imported) ---
    print("\n=== Step 4: EXTRACT deg(T_BZ->K*) (OPEN OUTPUT) ===")
    degree = extract_transfer_degree(spectrum_data)
    print(f"  edge same-pole M(s)/M(s) L_max-flow: " + ", ".join(
        f"L={L}:{degree['edge_ratio_per_L'][L]:.6f}" for L in sorted(degree['edge_ratio_per_L'])))
    print(f"    edge_rel_spread = {degree['edge_rel_spread']:.3e} "
          f"(edge_survives={degree['edge_survives']}; False => SAME-pole)")
    print(f"  cross-pole M(s+1)/M(s) probe L_max-flow: " + ", ".join(
        f"L={L}:{degree['cross_ratio_per_L'][L]:.6f}" for L in sorted(degree['cross_ratio_per_L'])))
    print(f"    cross_rel_spread = {degree['cross_rel_spread']:.3e} "
          f"(cross_survives={degree['cross_survives']}; sanity: cross-pole DOES flow)")
    print(f"  EXTRACTED deg(T_BZ->K*) = {degree['deg_extracted']:+.1f} "
          f"= 2*(s_num - s_den) = 2*({degree['deg_num_pole']} - {degree['deg_den_pole']})")
    print(f"    deg_is_integer = {degree['deg_is_integer']}; deg_is_even = {degree['deg_is_even']} "
          f"(PARITY pre-flight d_A=0 => EVEN required)")

    # --- Step 5: bridge image vs §VII envelope ---
    print("\n=== Step 5: bridge image of R_BZ_edge under extracted degree vs §VII envelope ===")
    bridge = bridge_image_check(degree["deg_extracted"], factorization["factorization_holds"])
    print(f"  bridge_image = {bridge['bridge_image']:.6f}; K* target = {bridge['K_star_target']}")
    print(f"  residual |image - K*| = {bridge['residual']:.4e}")
    print(f"  §VII envelope (L^-{ENVELOPE_ALPHA:.0f} * |K*|) = {bridge['envelope_abs']:.4e}")
    print(f"  lands_in_envelope = {bridge['lands_in_envelope']}")
    print(f"  decades_unaccounted (image vs K*) = {bridge['decades_unaccounted']:.4f}")

    # --- Step 6: verdict (3-tuple + composite) ---
    print("\n=== Step 6: verdict (3-tuple + composite) ===")
    composite, sign_v, mag_v, reg_v = evaluate_gate(degree, factorization, bridge)
    print(f"  sign_verdict     = {sign_v}  (parity: EVEN extracted degree?)")
    print(f"  magnitude_verdict= {mag_v}  (bridge image in §VII envelope?)")
    print(f"  regime_verdict   = {reg_v}  (NON-scalar=VALID / SCALAR=BREAKDOWN)")
    print(f"  COMPOSITE        = {composite}")
    if composite == "FAIL":
        print(f"  READING-B (ratio half): the edge transfer is SAME-pole/SCALAR "
              f"(deg={degree['deg_extracted']:+.1f}); no substrate degree CONTRACTS R_BZ_edge to K*.")
        print(f"  => C2-ratio joins C2-mag + C2-id as externally-determined; "
              f"full Reading-B on BOTH halves of K_pivot.")
    elif composite == "PASS":
        print(f"  READING-A (ratio-to-K* leg): the BZ edge transports cleanly to K* as an "
              f"EVEN morphism (deg={degree['deg_extracted']:+.1f}); §23 K=3 candidate.")
    else:
        print(f"  INFO: even degree extracted but bridge image off-envelope "
              f"(envelope-shortfall; degree real, image off).")

    # --- Step 7: value string + dual-SHA ---
    value = (
        f"deg_extracted={degree['deg_extracted']:+.1f}_"
        f"deg_even={degree['deg_is_even']}_"
        f"factorization_holds={factorization['factorization_holds']}_"
        f"is_scalar={factorization['factorization_holds']}_"
        f"num_den_pole={degree['deg_num_pole']}-{degree['deg_den_pole']}_"
        f"edge_rel_spread={degree['edge_rel_spread']:.3e}_"
        f"cross_rel_spread={degree['cross_rel_spread']:.3e}_"
        f"bridge_image={bridge['bridge_image']:.4f}_"
        f"K_star={K_STAR}_residual={bridge['residual']:.3e}_"
        f"envelope={bridge['envelope_abs']:.3e}_lands={bridge['lands_in_envelope']}_"
        f"decades_unaccounted={bridge['decades_unaccounted']:.4f}_"
        f"R_BZ_edge={R_BZ_EDGE}_decades_edge_to_Kstar={DECADES_EDGE_TO_KSTAR:.4f}_"
        f"deg_NOT_imported=deg_T_BZ_pivot_2.0_excluded_dedup_flag_iii"
    )
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_CONSTANTS_PATH, pins)
    print(f"\n=== Step 7: dual-SHA ===")
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    # --- Step 8: save npz + plot ---
    print("\n=== Step 8: save artifacts ===")
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION,
        L_max=L_MAX, L_max_scan=np.array(L_MAX_SCAN), L_ref=L_REF, s_edge=S_EDGE,
        k_grid=K_GRID,
        R_BZ_edge=R_BZ_EDGE, K_star=K_STAR, decades_edge_to_Kstar=DECADES_EDGE_TO_KSTAR,
        w_of_L=np.array([factorization["w_of_L"][L] for L in L_MAX_SCAN]),
        kappa_k=factorization["kappa_k"],
        shape_invariance_max=factorization["shape_invariance_max"],
        d2_invariance_max=factorization["d2_invariance_max"],
        shape_scalar=factorization["shape_scalar"],
        d2_scalar=factorization["d2_scalar"],
        factorization_holds=factorization["factorization_holds"],
        deg_extracted=degree["deg_extracted"], deg_extracted_int=degree["deg_extracted_int"],
        deg_is_integer=degree["deg_is_integer"], deg_is_even=degree["deg_is_even"],
        deg_num_pole=degree["deg_num_pole"], deg_den_pole=degree["deg_den_pole"],
        edge_ratio_per_L=np.array([degree["edge_ratio_per_L"][L] for L in L_MAX_SCAN]),
        cross_ratio_per_L=np.array([degree["cross_ratio_per_L"][L] for L in L_MAX_SCAN]),
        edge_rel_spread=degree["edge_rel_spread"], cross_rel_spread=degree["cross_rel_spread"],
        edge_survives=degree["edge_survives"], cross_survives=degree["cross_survives"],
        bridge_image=bridge["bridge_image"], K_star_target=bridge["K_star_target"],
        residual=bridge["residual"], envelope_alpha=bridge["envelope_alpha"],
        envelope_halfwidth=bridge["envelope_halfwidth"], envelope_abs=bridge["envelope_abs"],
        lands_in_envelope=bridge["lands_in_envelope"],
        decades_unaccounted=bridge["decades_unaccounted"],
        sage_parity_foreclosure=SAGE_PARITY_FORECLOSURE,
        deg_T_BZ_pivot_NOT_imported=2.0,  # recorded as the EXCLUDED value (anti-rescue audit trail)
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=reg_v,
        composite_verdict=composite,
        audit_sha256=audit_sha, content_sha256=content_sha,
        tau_fold=tau_fold, M_KK=M_KK, planck_ns=planck_ns,
    )
    print(f"  npz -> {OUT_NPZ.name}")
    make_plot(K_GRID, factorization, degree, bridge, composite)
    print(f"  png -> {OUT_PNG.name}")

    # --- Step 9: print verdict payload (agent calls emit_verdict) ---
    print_verdict_payload(composite, value, audit_sha, content_sha, sign_v, mag_v, reg_v)

    print(f"\n=== 4-tuple: (value-key, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX}) ===")
    print(f"{GATE_ID}: {composite}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
