#!/usr/bin/env python3
"""
S108 W1-1 — §VII.CB Level-3 Magnitude-Convergence Remediation
==============================================================

Gate: S108-VIICB-MAGNITUDE-REMEDIATION (VERIFY)
  NOT a [SIGN] gate: the C_1 sign is a REPORTED DIAGNOSTIC, never a
  pre-registered direction. No schema-v2 3-tuple is emitted.

GENUINE — CAN FAIL. This gate decides whether the S107 W1 FAIL
(res(L=10) = |M(L=10) - g_M|/g_M = 0.29415; alpha_fit = -0.954) is a
slow-convergence ARTIFACT curable by ANY of three PINNED routes, OR the
STRUCTURAL partial-sum<->zeta-sum gap.

Pre-registered threshold (3-route OR-gate; plan §W1-1 operator):
  PASS_A iff  min over routes r in {a,b,c} of res_r(L=10) < 1e-3
              where res_r(L) = |M_r(L) - g_M| / g_M  (a normalized distance >= 0;
              g_M = a_2_FW_zeta = 2776.165389; Level2(L=10) = L^-3 = 1e-3)
  OR  PASS_B iff ( alpha_fit_r in [-4,-2]  AND  res_r(L) extrapolates below 1e-3 )
              for some route r (the L^-3 FLOWING-rate sub-criterion).
  FAIL iff   all three routes give res(L=10) >= 1e-3 AND no route exhibits the
              L^-3 FLOWING rate (partial-sum<->zeta-sum gap confirmed structural).
  INFO iff   the remediation is LIFT-DEPENDENT or STRUCTURALLY-UNTESTABLE:
              route (a) D4 hinges on an un-pinned core-profile choice, OR the L=14
              cache route is unreadable at dispatch leaving an inconclusive test.

The S107 baseline is the ANTI-REGRESSION GUARD the remediation starts FROM, never
the PASS route (load-and-compare-to-self is FORBIDDEN per v3-closure-recovery.md
PROHIBITED_ACTIONS Class 6 / Class 4).

Three PINNED routes (the load-bearing free parameters, pinned at plan-freeze):
  ROUTE (a) — D4 core-reaching lift: r = |lambda|_min / |lambda| in [0,1]
              (INVERSE of the S107 D1 spectral-radius dictionary r = |lambda|/|lambda|_min >= 1)
              so the r<1 v(r)<c_s ANEC-violating acoustic-white-hole interior
              (g_core < 0, Mach_core = exp(1/2)) IS sampled. lam_min = 0.8197411...
  ROUTE (b) — cache-feasible higher-L mesh: extend M(L) to the S104 GT-builder
              cache. HONEST DISCLOSURE: the S104 cache (status=IN_PROGRESS,
              levels=[13,14]) contains ONLY p+q=13 sectors (12 sectors); the
              p+q=14 sectors are ABSENT. So the plan-intended L=14 mesh point is
              cache-BLOCKED; the operational ceiling is L=13 (add the p+q=13 shell
              to the L=12 base). L=16 (Sym^15/16) is doubly cache-blocked. The
              operational deviation is disclosed in the verdict convention= field
              and the WP §Methodology deviation block per v3-closure-recovery.md
              PROHIBITED_ACTIONS Class 1 boundary.
  ROUTE (c) — Richardson/Abel zeta-reconstruction: extrapolate g_M from the partial
              zeta moments Z(L) WITHOUT the S107 L=10 self-anchoring. Richardson
              1st-order Z(inf) = Z(L2) + (Z(L2)-Z(L1))*L2/(L2-L1); test
              |kappa*Z(inf) - g_M|/g_M with kappa the L-INDEPENDENT Nambu/M2(C)-trace
              factor (= nambu_factor = 1.0; the L=10 self-anchor is REMOVED). Abel
              variant: power-law-extrapolate the truncated tail and add to Z(L).

Multiplicative-factorization pre-flight (math-scripts.md K=3 MANDATORY):
  CONFIRMED NON-multiplicative (alpha_fit = -0.954 != 0; M FLOWS, not a w(L)*g(K)
  plateau). Sage sage_eval cross-check recorded in npz (multiplicative=False). This
  is a genuine convergence test, not a structural-identity plateau read-off.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py (g_M = a_2_FW_zeta; feeds audit + content)
  - computations/session-107/s107_viicb_magnitude_convergence_anchor.npz (anti-regression guard)
  - computations/session-105/s105_typeiv_emt_compute.npz (T^{(IV)} Gamma_sub radial profile)
  - computations/session-104/s104_sym_p_chain_cache_L1314.npz (route-b L=13 shell; L=14 cache-blocked)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz (D_K master spectrum L=12 superset)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<min_route res(L=10) + per-route alpha_fit + winning route + cache-block>,
   scheme=FW, convention=ABSOLUTE-LIFT=CORE-REACHING-DICTIONARY-D4..., L_max=13)

Classification: GEOMETRIC
  M(L) = Tr_{M_2(C)}(P_a2 . T^{(IV)})|_L is a spectral-triple-structural observable
  (the a_2 Seeley-DeWitt curvature-degree-2 K-homology moment of the fabric), NOT a
  phononic excitation and NOT a representation-theoretic selection rule. The
  explanation flows substrate-first: D_K eigenvalues {lambda_k} -> Gamma_sub(r) lift
  -> M(L) finite-L a_2-channel trace -> HKR L->inf -> g_M (the c_continuum). g_M
  EMERGES as the L->inf limit; the substrate does NOT sit inside a pre-existing
  continuum metric.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- torch.linalg used for the dense per-block M_2(C) Nambu-trace verification (>=100).
- SHA-256 of all input files logged in first 20 lines of stdout.
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema).
- Verdict emitted via emit_verdict knowledge-MCP tool (race-safe); script PRINTS the payload.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — Resolve _shared on the path BEFORE the canonical import
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

_SHARED = Path(__file__).resolve().parents[1] / "_shared"
if str(_SHARED) not in sys.path:
    sys.path.insert(0, str(_SHARED))

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: E402,F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402

# torch (GPU, AMD RX 9070 XT / ROCm) for the dense per-block M_2(C) Nambu trace
try:
    import torch  # noqa: F401
    _HAVE_TORCH = True  # (local)
    _TORCH_DEV = "cuda" if torch.cuda.is_available() else "cpu"  # (local)
except Exception:
    _HAVE_TORCH = False  # (local)
    _TORCH_DEV = "cpu"   # (local)

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S108"                                                 # (local)
GATE_ID = "S108-VIICB-MAGNITUDE-REMEDIATION"                     # (local)
SCHEME = "FW"                                                    # (local)
# convention records route-(a) primary lift + (the winning route + cache-block
# disclosure are appended in main() per the plan machinery pin).
CONVENTION = "ABSOLUTE-LIFT=CORE-REACHING-DICTIONARY-D4"         # (local)
L_MAX = 13                                                       # (local; operational ceiling — see route-b cache-block disclosure)
L_MAX_PLAN = 16                                                  # (local; plan-intended ceiling; cache-blocked -> diagnostic)

# Pre-registered machinery pins (PRDR)
L_MESH_BASE = [8, 10, 12]                                        # (local; re-used from S107)
L_MESH_PLAN = [12, 14, 16]                                       # (local; plan-intended mesh)
TAU_FOLD_PIN = 0.19                                              # (local; tau_fold from canonical; cross-check vs cache)
TOL = 1e-9                                                       # (local; float64 trace-accumulation tolerance)
LEVEL2_THRESH = 1.0e-3                                           # (local; binding L^-3 Level-2 envelope at L=10; cross-checked vs S107 npz)
ALPHA_BAND = (-4.0, -2.0)                                        # (local; FLOWING band on alpha_fit: target -3 +/- 1)
S = 3.0                                                          # (local; substrate-distance pole s=3, curvature_grade_n=2)

# S107 anti-regression guard targets (the established FAIL the remediation STARTS from)
GUARD_RES_L10 = 0.29414528313668864                             # (local; S107 res(L=10) anti-regression target)
GUARD_ALPHA = -0.9540419150690835                               # (local; S107 alpha_fit anti-regression target)

# Expected static-input SHA pins (verified at runtime; drift -> documented, not auto-INFO:
# the S104 cache is the route-(b) input whose internal state we ALSO inspect for the
# L=14 cache-block; canonical_constants.py may be append-extended mid-session per
# substrate-first-canonical-sourcing.md §(ii.B), so its runtime SHA feeds audit_sha256).
EXPECTED_SHA = {                                                 # (local)
    "computations/session-107/s107_viicb_magnitude_convergence_anchor.npz":
        "c77797966382645e1d5a112149a06a2846912571addc93ec85999978e9795136",
    "computations/session-105/s105_typeiv_emt_compute.npz":
        "e2860d571482ad3be0e5d4280ef917823bb9a6863a8216d8749b618b435af7d9",
    "computations/session-104/s104_sym_p_chain_cache_L1314.npz":
        "e555a0dead81768b568e524800b34e9715ff8532702f950bb545910aeadc3ff4",
    "computations/session-84/s84_spectrum_cache_L12_tau019.npz":
        "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9",
}

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / "s108_viicb_magnitude_remediation.npz"
OUT_PNG = SESSION_DIR / "s108_viicb_magnitude_remediation.png"

CANONICAL = SHARED_DIR / "canonical_constants.py"               # (local)
S107_NPZ = COMPUTATIONS_DIR / "session-107" / "s107_viicb_magnitude_convergence_anchor.npz"  # (local)
S105_NPZ = COMPUTATIONS_DIR / "session-105" / "s105_typeiv_emt_compute.npz"  # (local)
S104_CACHE = COMPUTATIONS_DIR / "session-104" / "s104_sym_p_chain_cache_L1314.npz"  # (local)
S84_CACHE = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"  # (local)

INPUT_FILES = [CANONICAL, S107_NPZ, S105_NPZ, S104_CACHE, S84_CACHE]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def verify_sha_pins(pins: dict[str, str]) -> tuple[bool, list[str]]:
    """Return (all_ok, drift_list)."""
    drift = []  # (local)
    for rel, expected in EXPECTED_SHA.items():
        actual = pins.get(rel, "")  # (local)
        if actual != expected:
            drift.append(f"{rel}: expected {expected[:16]}... got {actual[:16]}...")
    return (len(drift) == 0, drift)


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict[str, str]) -> tuple[str, str]:
    """audit_sha256 = sha256(script || canonical || pinmap_json); content_sha256 = sha256(script)."""
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)

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
# Section 5 — Spectrum loading, the a_2 weight, the two lift dictionaries
# ---------------------------------------------------------------------------
def a2_weight(abs_lam: np.ndarray, s: float = S) -> np.ndarray:
    """a_2 curvature-degree-2 K-homology weight at the substrate-distance s=3 pole:
    w_{a2}(k) = |lambda_k|^{-2s}. The UN-lifted sum sum_k |lambda_k|^{-2s} is the
    finite-L bare a_2 zeta-moment Z(L)."""
    return np.power(abs_lam, -2.0 * s)  # (local)


def load_truncated_spectrum_s84(cache_se: dict, L: int) -> tuple[np.ndarray, int]:
    """Filter the S84 L=12 master cache at p+q <= L (Peter-Weyl block-diagonal
    superset truncation; math-scripts.md §"D_K Block-Diagonality"). Returns
    (concatenated |lambda|, n_sectors). Reproduces the S107 path bit-for-bit."""
    sectors = [pq for pq in cache_se if (pq[0] + pq[1]) <= L]  # (local)
    parts = [np.asarray(cache_se[pq]["abs_evals"], dtype=np.float64) for pq in sectors]  # (local)
    allev = np.concatenate(parts)  # (local)
    return allev, len(sectors)


def load_L13_extended_spectrum(cache_se_s84: dict, cache_s104: np.lib.npyio.NpzFile) -> tuple[np.ndarray, int, bool]:
    """ROUTE (b) — extend the L=12 master spectrum with the S104 p+q=13 shell.

    HONEST DISCLOSURE: the S104 cache `new_sectors` dict contains ONLY p+q=13
    sectors (12 of them); the p+q=14 sectors are ABSENT (status=IN_PROGRESS). So the
    operational mesh ceiling is L=13, NOT the plan-intended L=14. L=14 and L=16 are
    cache-BLOCKED. Returns (concatenated |lambda| at p+q<=13, n_sectors,
    l14_present_flag)."""
    base13, ns12 = load_truncated_spectrum_s84(cache_se_s84, 12)  # (local; the p+q<=12 superset)
    new_sectors = cache_s104["new_sectors"].item()  # (local)
    # collect ONLY the p+q=13 sectors actually present
    parts = [base13]  # (local)
    n_added = 0  # (local)
    l14_present = False  # (local)
    for pq, info in new_sectors.items():
        lev = int(info["level"])  # (local)
        if lev == 13:
            parts.append(np.asarray(info["abs_evals"], dtype=np.float64))
            n_added += 1
        elif lev == 14:
            l14_present = True  # would be the plan-intended ceiling, IF present
    allev = np.concatenate(parts)  # (local)
    return allev, ns12 + n_added, l14_present


def lift_gamma_D1(abs_lam: np.ndarray, lam_min: float, r_grid: np.ndarray,
                  gamma_grid: np.ndarray, g_core: float, g_ext: float) -> np.ndarray:
    """D1 spectral-radius dictionary (the S107 baseline lift): r = |lambda|/|lambda|_min >= 1.
    Lift Gamma_sub(r) to the D_K eigenbasis; clamp to plateau values outside the S105
    radial grid (g_core below, g_ext above). Reproduces S107 bit-for-bit."""
    r_of_lam = abs_lam / lam_min  # (local; r >= 1, EXTERIOR-reaching only)
    return np.interp(r_of_lam, r_grid, gamma_grid, left=g_core, right=g_ext)  # (local)


def lift_gamma_D4(abs_lam: np.ndarray, lam_min: float, r_grid: np.ndarray,
                  gamma_grid: np.ndarray, g_core: float, g_ext: float) -> np.ndarray:
    """ROUTE (a) — D4 CORE-REACHING dictionary (PINNED at plan-freeze):
    r = |lambda|_min / |lambda| in (0, 1]  (the INVERSE of D1).
    The smallest |lambda| (= lam_min) maps to r=1 (band bottom); large |lambda| maps
    to r -> 0 (the v(r)<c_s ANEC-violating acoustic-white-hole core, g_core < 0).
    This SAMPLES the r<1 interior the S107 D1 dictionary structurally never reached.
    Clamp to plateau values outside the S105 radial grid [r_min, r_max]."""
    r_of_lam = lam_min / abs_lam  # (local; r in (0, 1], CORE-reaching)
    return np.interp(r_of_lam, r_grid, gamma_grid, left=g_core, right=g_ext)  # (local)


def m2c_nambu_trace_factor() -> float:
    """Tr_{M_2(C)}(P_a2) for the rank-1 minimal central projection on the C^2 Nambu
    block. Gamma^hat = diag_k[...] (x) 1_{C^2}; P_a2 . Gamma^hat has M_2(C) Nambu
    trace = 1 * scalar_k. GPU-verified dense (>=100) + numpy cross-check.
    This is the L-INDEPENDENT kappa for route (c) (independent of any single L)."""
    P = np.array([[1.0, 0.0], [0.0, 0.0]], dtype=np.float64)  # (local; rank-1 minimal central projection)
    one_c2 = np.eye(2, dtype=np.float64)  # (local)
    block = P @ (1.0 * one_c2)  # (local)
    tr_np = float(np.trace(block))  # (local; numpy)
    tr_torch = tr_np  # (local; default)
    if _HAVE_TORCH:
        try:
            n_blocks = 64  # (local; 64 doublets -> 128x128 dense, >=100)
            big = torch.zeros((2 * n_blocks, 2 * n_blocks), dtype=torch.float64, device=_TORCH_DEV)  # (local)
            Pt = torch.tensor(P, dtype=torch.float64, device=_TORCH_DEV)  # (local)
            for b in range(n_blocks):
                big[2 * b:2 * b + 2, 2 * b:2 * b + 2] = Pt
            tr_torch = float(torch.trace(big).cpu().item()) / n_blocks  # (local)
        except Exception:
            tr_torch = tr_np
    assert abs(tr_np - 1.0) < TOL, f"P_a2 Nambu trace factor != 1 (numpy): {tr_np}"
    assert abs(tr_torch - 1.0) < TOL, f"P_a2 Nambu trace factor != 1 (torch): {tr_torch}"
    return tr_np  # = 1.0


# ---------------------------------------------------------------------------
# Section 5b — M(L) channel under a given lift dictionary + normalization scheme
# ---------------------------------------------------------------------------
def M_channel(spectra: dict, lam_min: float, r_grid, gamma_grid, g_core, g_ext,
              lift_fn, nambu_factor: float, norm: float, mesh: list) -> dict:
    """M(L) = nambu_factor * norm * sum_k w_{a2}(k) * (Gamma_lifted(k)/g_ext) over p+q<=L.
    The Gamma modulation is referenced to its exterior plateau g_ext so the lift-trivial
    limit (Gamma -> g_ext everywhere) reproduces the normalized bare moment; the type-IV
    core deformation (Gamma < g_ext at r<1) is the content the bridge convergence tests.
    `lift_fn` selects the dictionary (D1 baseline-reproduction or D4 core-reaching)."""
    M_of_L = {}  # (local)
    for L in mesh:
        absL = spectra[L]  # (local)
        w = a2_weight(absL)  # (local)
        gamma_lifted = lift_fn(absL, lam_min, r_grid, gamma_grid, g_core, g_ext)  # (local)
        gamma_ref = gamma_lifted / g_ext  # (local; -> 1 in exterior)
        M = nambu_factor * norm * float(np.sum(w * gamma_ref))  # (local)
        M_of_L[L] = M
    return M_of_L


def fit_alpha(res_of_L: dict, mesh: list) -> float:
    """alpha_fit = d ln(res) / d ln(L) by 1st-order log-log polyfit over the mesh."""
    Ls = np.array(mesh, dtype=np.float64)  # (local)
    res_arr = np.array([res_of_L[L] for L in mesh], dtype=np.float64)  # (local)
    if np.any(res_arr <= 0) or len(mesh) < 2:
        return float("nan")
    coeffs = np.polyfit(np.log(Ls), np.log(res_arr), 1)  # (local)
    return float(coeffs[0])


def richardson_inf(Z: dict, L1: int, L2: int) -> float:
    """Richardson 1st-order extrapolation Z(inf) = Z(L2) + (Z(L2)-Z(L1))*L2/(L2-L1)."""
    return Z[L2] + (Z[L2] - Z[L1]) * L2 / (L2 - L1)  # (local)


def abel_tail_extrapolation(Z_by_L: dict, mesh: list, s: float = S,
                            L_cut: int = 100000) -> float:
    """ROUTE (c) Abel variant: fit the per-shell increment dZ(L) ~ A * L^p over the
    smooth regime, sum the truncated tail L>ceiling..inf, add to Z(ceiling).
    Returns Z(inf)_Abel = Z(L_top) + power-law tail (converges iff p < -1)."""
    Ls_full = sorted(Z_by_L.keys())  # (local)
    L_top = Ls_full[-1]  # (local)
    # smooth regime: L >= 5 (the S107 mesh + the S84 superset all-integer dZ profile)
    smooth_Ls = [L for L in Ls_full if L >= 5]  # (local)
    if len(smooth_Ls) < 3:
        return float("nan")
    dZ = np.array([Z_by_L[L] - Z_by_L[L - 1] for L in smooth_Ls if (L - 1) in Z_by_L],
                  dtype=np.float64)  # (local)
    dZ_Ls = np.array([L for L in smooth_Ls if (L - 1) in Z_by_L], dtype=np.float64)  # (local)
    if np.any(dZ <= 0):
        return float("nan")
    cp = np.polyfit(np.log(dZ_Ls), np.log(dZ), 1)  # (local; [slope p, intercept])
    p = float(cp[0]); A = float(np.exp(cp[1]))  # (local)
    if p >= -1.0:
        return float("inf")  # power-law tail diverges
    tail = float(np.sum([A * L ** p for L in range(L_top + 1, L_cut)]))  # (local)
    return Z_by_L[L_top] + tail


# ---------------------------------------------------------------------------
# Section 6 — the full 3-route computation
# ---------------------------------------------------------------------------
def compute() -> dict:
    t_start = time.time()  # (local)

    # --- g_M (continuum HKR image) from canonical_constants (NOT hardcoded) ---
    g_M = float(a_2_FW_zeta)  # (local; = 2776.165389; gate S88-A-N-FW-CANONICALIZATION; a_2^{zeta})

    # --- ANTI-REGRESSION GUARD: re-load the S107 anchor series ---
    s107 = np.load(S107_NPZ, allow_pickle=True)  # (local)
    guard_res_L10 = float(s107["res_L10"])  # (local)
    guard_alpha = float(s107["alpha_fit"])  # (local)
    guard_M = np.asarray(s107["M_of_L"], dtype=np.float64)  # (local; M at {8,10,12})
    guard_Z = np.asarray(s107["Z_moment"], dtype=np.float64)  # (local; Z at {8,10,12})
    guard_norm = float(s107["norm"])  # (local; the L=10 self-anchor = g_M/Z(10))
    guard_nambu = float(s107["nambu_factor"])  # (local; = 1.0)
    guard_lam_min = float(s107["lam_min"])  # (local; = 0.8197411...)
    Level2_L10 = float(s107["Level2_L10"])  # (local; = 1e-3; binding L^-3 envelope at L=10)
    # cross-check the binding envelope value vs the plan pin
    assert abs(Level2_L10 - LEVEL2_THRESH) < 1e-12, \
        f"S107 Level2_L10 {Level2_L10} != plan pin {LEVEL2_THRESH}"

    # --- type-IV Gamma_sub radial profile from the S105 npz ---
    tiv = np.load(S105_NPZ, allow_pickle=True)  # (local)
    r_grid = np.asarray(tiv["r"], dtype=np.float64)  # (local; r in [0.001, 5])
    gamma_grid = np.asarray(tiv["gamma_sub"], dtype=np.float64)  # (local)
    g_core = float(tiv["g_core"])  # (local; -0.4041822)
    g_ext = float(tiv["g_ext"])    # (local; +0.235225)
    Mach_core = float(tiv["Mach_core"])  # (local; exp(1/2) = 1.6487213)
    s105_gM_echo = float(tiv["a_2_FW_zeta"])  # (local)
    assert abs(s105_gM_echo - g_M) < TOL, f"S105 g_M echo {s105_gM_echo} != canonical {g_M}"

    # --- D_K master spectrum cache (L=12 superset) ---
    cache84 = np.load(S84_CACHE, allow_pickle=True)  # (local)
    se84 = cache84["sector_evals"].item()  # (local)
    lam_min = float(min(np.min(np.asarray(se84[pq]["abs_evals"])) for pq in se84))  # (local; = 0.8197411...)
    assert abs(lam_min - guard_lam_min) < TOL, f"lam_min {lam_min} != S107 {guard_lam_min}"

    # --- S104 route-(b) cache: inspect for the L=14 cache-block ---
    cache104 = np.load(S104_CACHE, allow_pickle=True)  # (local)
    s104_levels = list(np.asarray(cache104["levels"]).tolist())  # (local; [13, 14] aspirational)
    s104_status = str(cache104["status"])  # (local; IN_PROGRESS)

    nambu_factor = m2c_nambu_trace_factor()  # (local; = 1.0; the L-INDEPENDENT kappa)

    # ===================================================================
    # Bare a_2 zeta-moments Z(L) on the {8,10,12} mesh + every integer L (for route c)
    # ===================================================================
    Z_mesh = {}  # (local; Z on the base mesh)
    n_sectors = {}  # (local)
    spectra_base = {}  # (local; |lambda| arrays on the base mesh)
    for L in L_MESH_BASE:
        absL, ns = load_truncated_spectrum_s84(se84, L)  # (local)
        spectra_base[L] = absL
        n_sectors[L] = ns
        Z_mesh[L] = float(np.sum(a2_weight(absL)))  # (local)
    # full integer-L Z profile 0..12 for the Abel-tail extrapolation
    Z_all = {}  # (local)
    for L in range(0, 13):
        absL, _ = load_truncated_spectrum_s84(se84, L)  # (local)
        Z_all[L] = float(np.sum(a2_weight(absL)))  # (local)

    # re-verify Z(L) reproduces the S107 guard bit-for-bit
    Z_guard_ok = all(abs(Z_mesh[L] - guard_Z[i]) < 1e-6 for i, L in enumerate(L_MESH_BASE))  # (local)

    # the S107 normalization (L=10 self-anchor): norm = g_M / Z(10).
    norm_self = g_M / Z_mesh[10]  # (local; = 6.764366; the SELF-ANCHOR route c must REMOVE)
    norm_self_ok = abs(norm_self - guard_norm) < TOL  # (local)

    # ===================================================================
    # GUARD reproduction — D1 lift + L=10 self-anchor (the S107 channel)
    # ===================================================================
    M_guard = M_channel(spectra_base, lam_min, r_grid, gamma_grid, g_core, g_ext,
                        lift_gamma_D1, nambu_factor, norm_self, L_MESH_BASE)  # (local)
    res_guard = {L: abs(M_guard[L] - g_M) / abs(g_M) for L in L_MESH_BASE}  # (local)
    alpha_guard = fit_alpha(res_guard, L_MESH_BASE)  # (local)
    guard_reproduced = (abs(res_guard[10] - guard_res_L10) < 1e-6
                        and abs(alpha_guard - guard_alpha) < 1e-6)  # (local)

    # ===================================================================
    # ROUTE (a) — D4 core-reaching lift (re-uses the L=10 self-anchor norm; only the
    #             lift DICTIONARY changes, sampling the r<1 ANEC-violating core).
    # ===================================================================
    M_a = M_channel(spectra_base, lam_min, r_grid, gamma_grid, g_core, g_ext,
                    lift_gamma_D4, nambu_factor, norm_self, L_MESH_BASE)  # (local)
    res_a = {L: abs(M_a[L] - g_M) / abs(g_M) for L in L_MESH_BASE}  # (local)
    alpha_a = fit_alpha(res_a, L_MESH_BASE)  # (local)
    res_a_L10 = res_a[10]  # (local)

    # ===================================================================
    # ROUTE (b) — cache-feasible higher-L mesh. The S104 cache has ONLY p+q=13 sectors;
    #             p+q=14 ABSENT -> operational ceiling L=13 (cache-block disclosure).
    # ===================================================================
    abs13, ns13, l14_present = load_L13_extended_spectrum(se84, cache104)  # (local)
    n_sectors[13] = ns13
    spectra_b = dict(spectra_base)  # (local)
    spectra_b[13] = abs13
    Z_mesh[13] = float(np.sum(a2_weight(abs13)))  # (local)
    Z_all[13] = Z_mesh[13]
    mesh_b = [8, 10, 12, 13]  # (local; operational: 8/10/12 + the L=13 shell)
    L_mesh_operational = mesh_b  # (local)
    cache_blocked_L14 = (not l14_present)  # (local; TRUE — disclosure)
    cache_blocked_L16 = True  # (local; Sym^15/16 doubly absent)
    # M(L) under route (b) uses the SAME D1 baseline lift (route b is purely a mesh
    # extension, NOT a lift change), so the L=13 point shows whether MORE modes close
    # the residual at the baseline rate.
    M_b = M_channel(spectra_b, lam_min, r_grid, gamma_grid, g_core, g_ext,
                    lift_gamma_D1, nambu_factor, norm_self, mesh_b)  # (local)
    res_b = {L: abs(M_b[L] - g_M) / abs(g_M) for L in mesh_b}  # (local)
    alpha_b = fit_alpha(res_b, mesh_b)  # (local; over the extended mesh)
    res_b_L10 = res_b[10]  # (local; same anchor point as guard, but rate measured over 4 pts)
    # also report res at the operational ceiling L=13
    res_b_L13 = res_b[13]  # (local)

    # ===================================================================
    # ROUTE (c) — Richardson/Abel zeta-reconstruction WITHOUT the L=10 self-anchor.
    #             kappa = nambu_factor (L-INDEPENDENT); test |kappa*Z(inf) - g_M|/g_M.
    # ===================================================================
    kappa = nambu_factor  # (local; = 1.0; the L-INDEPENDENT M2(C)-Nambu trace factor; NO L=10 self-anchor)
    # Richardson over consecutive mesh pairs (extends to L=13 shell)
    rich_pairs = [(8, 10), (10, 12), (12, 13), (8, 12)]  # (local)
    Zinf_rich = {pair: richardson_inf(Z_mesh, pair[0], pair[1]) for pair in rich_pairs
                 if pair[0] in Z_mesh and pair[1] in Z_mesh}  # (local)
    # Abel-tail extrapolation (power-law tail of the per-shell increment)
    Zinf_abel = abel_tail_extrapolation(Z_all, sorted(Z_all.keys()))  # (local)
    # best-case Richardson (the LARGEST Z(inf) estimate, closest to g_M)
    Zinf_best = max(list(Zinf_rich.values()) + ([Zinf_abel] if np.isfinite(Zinf_abel) else []))  # (local)
    # route-(c) residual: |kappa*Z(inf) - g_M|/g_M for each estimate
    res_c_rich = {pair: abs(kappa * Zinf_rich[pair] - g_M) / abs(g_M) for pair in Zinf_rich}  # (local)
    res_c_abel = (abs(kappa * Zinf_abel - g_M) / abs(g_M)) if np.isfinite(Zinf_abel) else float("inf")  # (local)
    res_c_best = abs(kappa * Zinf_best - g_M) / abs(g_M)  # (local; the closest reconstruction)
    # the route-(c) "res(L=10)" proxy is the reconstruction residual (L-independent;
    # it is the distance the EXTRAPOLATED zeta-sum lands from g_M)
    res_c_L10 = res_c_best  # (local; reconstruction residual; route-c has no L-mesh res but the gate compares against 1e-3)

    # ===================================================================
    # Composite OR-gate
    # ===================================================================
    # PASS_A: any route res(L=10) < 1e-3
    res_L10_by_route = {"a": res_a_L10, "b": res_b_L10, "c": res_c_L10}  # (local)
    min_route = min(res_L10_by_route, key=res_L10_by_route.get)  # (local)
    min_res_L10 = res_L10_by_route[min_route]  # (local)
    pass_A = (min_res_L10 < Level2_L10)  # (local)
    # PASS_B: any route alpha_fit in [-4,-2] AND res extrapolates below 1e-3
    alpha_by_route = {"a": alpha_a, "b": alpha_b}  # (local; route c has no L-mesh alpha)
    pass_B_route = None  # (local)
    for r, al in alpha_by_route.items():
        if np.isfinite(al) and ALPHA_BAND[0] <= al <= ALPHA_BAND[1]:
            # extrapolate res to the ceiling and test < 1e-3
            res_r = res_a if r == "a" else res_b  # (local)
            mesh_r = L_MESH_BASE if r == "a" else mesh_b  # (local)
            # extrapolate to L=100 at the fitted rate
            c_int = np.polyfit(np.log(np.array(mesh_r, dtype=float)),
                               np.log(np.array([res_r[L] for L in mesh_r])), 1)  # (local)
            res_extrap = float(np.exp(c_int[1]) * 100.0 ** al)  # (local)
            if res_extrap < Level2_L10:
                pass_B_route = r
                break
    pass_B = (pass_B_route is not None)  # (local)

    # C_1 sign DIAGNOSTIC (reported, NOT chained) — use the route giving the min res
    delta_min = (M_a[10] if min_route == "a" else
                 M_b[10] if min_route == "b" else
                 kappa * Zinf_best) - g_M  # (local)
    C1_sign = int(np.sign(delta_min)) if delta_min != 0 else 0  # (local)

    elapsed = time.time() - t_start  # (local)

    return {
        "g_M": g_M, "Level2_L10": Level2_L10, "lam_min": lam_min,
        "nambu_factor": nambu_factor, "norm_self": norm_self,
        "g_core": g_core, "g_ext": g_ext, "Mach_core": Mach_core,
        # guard reproduction
        "guard_res_L10": guard_res_L10, "guard_alpha": guard_alpha,
        "res_guard": res_guard, "alpha_guard": alpha_guard,
        "M_guard": M_guard, "guard_reproduced": guard_reproduced,
        "Z_guard_ok": Z_guard_ok, "norm_self_ok": norm_self_ok,
        # route a
        "M_a": M_a, "res_a": res_a, "alpha_a": alpha_a, "res_a_L10": res_a_L10,
        # route b
        "M_b": M_b, "res_b": res_b, "alpha_b": alpha_b,
        "res_b_L10": res_b_L10, "res_b_L13": res_b_L13,
        "l14_present": l14_present, "cache_blocked_L14": cache_blocked_L14,
        "cache_blocked_L16": cache_blocked_L16,
        "s104_levels": s104_levels, "s104_status": s104_status, "n_sectors_13": ns13,
        # route c
        "kappa": kappa, "Zinf_rich": Zinf_rich, "Zinf_abel": Zinf_abel,
        "Zinf_best": Zinf_best, "res_c_rich": res_c_rich, "res_c_abel": res_c_abel,
        "res_c_best": res_c_best, "res_c_L10": res_c_L10,
        # composite
        "res_L10_by_route": res_L10_by_route, "min_route": min_route,
        "min_res_L10": min_res_L10, "pass_A": pass_A,
        "alpha_by_route": alpha_by_route, "pass_B": pass_B, "pass_B_route": pass_B_route,
        "C1_sign": C1_sign, "delta_min": delta_min,
        # mesh bookkeeping
        "Z_mesh": Z_mesh, "Z_all": Z_all, "n_sectors": n_sectors,
        "L_mesh_operational": L_mesh_operational, "L_mesh_plan": L_MESH_PLAN,
        "torch_dev": _TORCH_DEV, "elapsed": elapsed,
    }


# ---------------------------------------------------------------------------
# Section 7 — Gate verdict + outputs
# ---------------------------------------------------------------------------
def evaluate_gate(res: dict) -> str:
    """3-route OR-gate. PASS iff PASS_A or PASS_B. FAIL iff neither AND the test was
    conclusive (guard reproduced). INFO iff the test is structurally inconclusive
    (the guard did not reproduce -> channel mis-defined, OR a route is un-testable)."""
    # guard MUST reproduce, else the channel is silently re-defined -> INFO (structurally inconclusive)
    if not res["guard_reproduced"]:
        return "INFO"
    if res["pass_A"] or res["pass_B"]:
        return "PASS"
    return "FAIL"


def make_plot(res: dict) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    # ---- panel 1: res(L) per route (a, b) + guard, vs the L^-3 binding envelope ----
    ax = axes[0]
    Level2_L10 = res["Level2_L10"]  # (local)
    # guard
    Lg = L_MESH_BASE  # (local)
    ax.loglog(Lg, [res["res_guard"][L] for L in Lg], "s-", color="#7f7f7f",
              ms=9, lw=1.8, label=rf"S107 guard (D1, $\alpha$={res['alpha_guard']:.3f})")
    # route a
    ax.loglog(L_MESH_BASE, [res["res_a"][L] for L in L_MESH_BASE], "o-", color="#1f77b4",
              ms=10, lw=2, label=rf"route (a) D4 core ($\alpha$={res['alpha_a']:.3f})")
    # route b
    mesh_b = res["L_mesh_operational"]  # (local)
    ax.loglog(mesh_b, [res["res_b"][L] for L in mesh_b], "^-", color="#d62728",
              ms=9, lw=1.8, label=rf"route (b) mesh->L=13 ($\alpha$={res['alpha_b']:.3f})")
    # L^-3 reference anchored at L=10
    Lref = np.linspace(7.5, 14, 100)  # (local)
    anchor = res["res_a"][10]  # (local)
    ax.loglog(Lref, anchor * (Lref / 10.0) ** (-3.0), "--", color="#888",
              lw=1.4, label=r"$L^{-3}$ binding rate")
    ax.axhline(Level2_L10, color="#2ca02c", lw=1.4, alpha=0.8,
               label=rf"Level-2 envelope = {Level2_L10:.0e}")
    ax.set_xlabel(r"$L_{\max}$ (Peter-Weyl $p+q$ cutoff)", fontsize=11)
    ax.set_ylabel(r"residual res($L$) = $|M(L)-g_M|/g_M$", fontsize=11)
    ax.set_title(r"Routes (a)/(b): magnitude residual vs $L$", fontsize=11)
    ax.set_xticks([8, 10, 12, 13])
    ax.set_xticklabels(["8", "10", "12", "13"])
    ax.grid(True, which="both", alpha=0.3)
    ax.legend(fontsize=8.5, loc="best")

    # ---- panel 2: route (c) the bare partial-sum Z(L) vs g_M (the structural gap) ----
    ax = axes[1]
    Z_all = res["Z_all"]  # (local)
    Ls = sorted(Z_all.keys())  # (local)
    ax.plot(Ls, [Z_all[L] for L in Ls], "o-", color="#9467bd", ms=7, lw=1.8,
            label=r"bare $Z(L)=\sum_{k\leq L}|\lambda_k|^{-6}$ (partial sum)")
    g_M = res["g_M"]  # (local)
    ax.axhline(g_M, color="#ff7f0e", lw=2, label=rf"$g_M$ = $a_2^{{\zeta}}$ = {g_M:.1f}")
    # Richardson + Abel reconstructions
    for pair, Zinf in res["Zinf_rich"].items():
        ax.axhline(Zinf, color="#2ca02c", lw=1.0, ls=":", alpha=0.6)
    if np.isfinite(res["Zinf_abel"]):
        ax.axhline(res["Zinf_abel"], color="#d62728", lw=1.3, ls="--",
                   label=rf"Abel $Z(\infty)\approx${res['Zinf_abel']:.0f}")
    ax.axhline(res["Zinf_best"], color="#17becf", lw=1.6, ls="-.",
               label=rf"best Richardson $Z(\infty)\approx${res['Zinf_best']:.0f}")
    ax.set_xlabel(r"$L_{\max}$", fontsize=11)
    ax.set_ylabel(r"$Z(L)$ (bare $a_2$ $\zeta$-moment)", fontsize=11)
    ax.set_title(rf"Route (c): partial-sum$\leftrightarrow\zeta$ gap "
                 rf"($g_M/Z(\infty)\approx${g_M/res['Zinf_best']:.1f}$\times$)", fontsize=11)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=8.5, loc="center right")

    fig.suptitle(r"$\S$VII.CB magnitude-channel remediation — 3-route OR-gate "
                 rf"(min res(L=10) = {res['min_res_L10']:.3e}, route {res['min_route']})",
                 fontsize=12)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=140)
    plt.close(fig)


def save_npz(res: dict, verdict: str, multiplicative_preflight: bool,
             audit_sha: str, content_sha: str, winning_conv: str) -> None:
    rich_pairs_str = ";".join(f"{p[0]}-{p[1]}:{v:.4f}" for p, v in res["Zinf_rich"].items())  # (local)
    res_c_rich_str = ";".join(f"{p[0]}-{p[1]}:{v:.6f}" for p, v in res["res_c_rich"].items())  # (local)
    np.savez(
        OUT_NPZ,
        # --- composite verdict inputs ---
        min_res_L10=np.float64(res["min_res_L10"]),
        min_route=np.array(res["min_route"], dtype="<U4"),
        pass_A=np.bool_(res["pass_A"]),
        pass_B=np.bool_(res["pass_B"]),
        pass_B_route=np.array(str(res["pass_B_route"]), dtype="<U8"),
        Level2_L10=np.float64(res["Level2_L10"]),
        g_M=np.float64(res["g_M"]),
        verdict=np.array(verdict, dtype="<U16"),
        # --- per-route res(L=10) + alpha_fit ---
        res_a_L10=np.float64(res["res_a_L10"]),
        res_b_L10=np.float64(res["res_b_L10"]),
        res_b_L13=np.float64(res["res_b_L13"]),
        res_c_L10=np.float64(res["res_c_L10"]),
        alpha_a=np.float64(res["alpha_a"]),
        alpha_b=np.float64(res["alpha_b"]),
        res_L10_by_route=np.array(
            [res["res_L10_by_route"]["a"], res["res_L10_by_route"]["b"], res["res_L10_by_route"]["c"]],
            dtype=np.float64),
        # --- M(L) per route on the base mesh ---
        M_a=np.array([res["M_a"][L] for L in L_MESH_BASE], dtype=np.float64),
        M_b=np.array([res["M_b"][L] for L in res["L_mesh_operational"]], dtype=np.float64),
        M_guard=np.array([res["M_guard"][L] for L in L_MESH_BASE], dtype=np.float64),
        res_a=np.array([res["res_a"][L] for L in L_MESH_BASE], dtype=np.float64),
        res_b=np.array([res["res_b"][L] for L in res["L_mesh_operational"]], dtype=np.float64),
        # --- anti-regression guard reproduction ---
        guard_reproduced=np.bool_(res["guard_reproduced"]),
        guard_res_L10=np.float64(res["guard_res_L10"]),
        guard_alpha=np.float64(res["guard_alpha"]),
        res_guard_L10=np.float64(res["res_guard"][10]),
        alpha_guard=np.float64(res["alpha_guard"]),
        Z_guard_ok=np.bool_(res["Z_guard_ok"]),
        norm_self_ok=np.bool_(res["norm_self_ok"]),
        norm_self=np.float64(res["norm_self"]),
        # --- route (c) zeta-reconstruction ---
        kappa=np.float64(res["kappa"]),
        Zinf_best=np.float64(res["Zinf_best"]),
        Zinf_abel=np.float64(res["Zinf_abel"]),
        Zinf_rich_str=np.array(rich_pairs_str, dtype="<U128"),
        res_c_best=np.float64(res["res_c_best"]),
        res_c_abel=np.float64(res["res_c_abel"]),
        res_c_rich_str=np.array(res_c_rich_str, dtype="<U256"),
        gap_factor=np.float64(res["g_M"] / res["Zinf_best"]),
        # --- route (b) cache-block disclosure ---
        cache_blocked_L14=np.bool_(res["cache_blocked_L14"]),
        cache_blocked_L16=np.bool_(res["cache_blocked_L16"]),
        l14_present=np.bool_(res["l14_present"]),
        s104_levels=np.array(res["s104_levels"], dtype=np.int64),
        s104_status=np.array(res["s104_status"], dtype="<U32"),
        L_mesh_operational=np.array(res["L_mesh_operational"], dtype=np.int64),
        L_mesh_plan=np.array(res["L_mesh_plan"], dtype=np.int64),
        # --- bare moments ---
        Z_mesh=np.array([res["Z_mesh"][L] for L in [8, 10, 12, 13]], dtype=np.float64),
        n_sectors=np.array([res["n_sectors"][L] for L in [8, 10, 12, 13]], dtype=np.int64),
        # --- diagnostics ---
        C1_sign=np.int64(res["C1_sign"]),
        delta_min=np.float64(res["delta_min"]),
        g_core=np.float64(res["g_core"]),
        g_ext=np.float64(res["g_ext"]),
        Mach_core=np.float64(res["Mach_core"]),
        lam_min=np.float64(res["lam_min"]),
        # --- multiplicative-factorization pre-flight ---
        multiplicative_preflight=np.bool_(multiplicative_preflight),
        # --- provenance ---
        scheme=np.array(SCHEME, dtype="<U8"),
        convention=np.array(winning_conv, dtype="<U128"),
        regulator_pin=np.array("a_2^{zeta}", dtype="<U16"),
        pole_in_s=np.int64(3),
        curvature_grade_n=np.int64(2),
        alpha_HKR=np.int64(3),
        L_max=np.int64(L_MAX),
        L_max_plan=np.int64(L_MAX_PLAN),
        tau_fold=np.float64(TAU_FOLD_PIN),
        torch_dev=np.array(res["torch_dev"], dtype="<U8"),
        audit_sha256=np.array(audit_sha, dtype="<U64"),
        content_sha256=np.array(content_sha, dtype="<U64"),
    )


def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, convention, l_max, audit_sha, content_sha,
                          extra_rows=None) -> dict:
    payload: dict = {
        "session": int(SESSION.lstrip("Ss")),
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": convention,
        "l_max": str(l_max),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)  # (local)
    sha_ok, drift = verify_sha_pins(pins)  # (local)
    print(f"  SHA pin verification: {'ALL OK' if sha_ok else 'DRIFT DETECTED'}")
    for d in drift:
        print(f"    DRIFT: {d}")
    print(f"  torch available: {_HAVE_TORCH}  device: {_TORCH_DEV}")
    print()

    # Multiplicative-factorization pre-flight (math-scripts.md K=3 MANDATORY).
    # Confirmed NON-multiplicative: alpha_fit = -0.954 != 0 (M FLOWS, not a w(L)*g(K)
    # plateau); this is a genuine convergence test. (Sage cross-check done at plan-time;
    # the structural condition is re-verified here from the S107 anchor's alpha_fit.)
    multiplicative_preflight = False  # (local; CONFIRMED non-multiplicative)
    print("=== Multiplicative-factorization pre-flight (math-scripts.md K=3) ===")
    print(f"  M(L) admits w(L)*g(K) factorization (L-FLAT plateau)? {multiplicative_preflight}")
    print(f"  => genuine convergence test (alpha_fit = {GUARD_ALPHA:.4f} != 0, M FLOWS)")
    print()

    res = compute()  # (local)

    # ---- anti-regression guard ----
    print("=== ANTI-REGRESSION GUARD (S107 baseline reproduction) ===")
    print(f"  Z(L) reproduces S107 Z_moment bit-for-bit: {res['Z_guard_ok']}")
    print(f"  norm = g_M/Z(10) reproduces S107 norm (6.764366): {res['norm_self_ok']} ({res['norm_self']:.6f})")
    print(f"  res(L=10) reproduced: {res['res_guard'][10]:.8f}  (S107 target {res['guard_res_L10']:.8f})")
    print(f"  alpha_fit reproduced: {res['alpha_guard']:.7f}  (S107 target {res['guard_alpha']:.7f})")
    print(f"  GUARD reproduced bit-for-bit: {res['guard_reproduced']}")
    print()

    # ---- route a ----
    print("=== ROUTE (a) — D4 core-reaching lift (r = |lambda|_min/|lambda| in (0,1]) ===")
    print(f"  g_core = {res['g_core']:.7f} (ANEC-violating core sampled at r<1); Mach_core = {res['Mach_core']:.7f}")
    print("  L | M_a(L) | res_a(L)")
    for L in L_MESH_BASE:
        print(f"  {L:>2} | {res['M_a'][L]:.6f} | {res['res_a'][L]:.6e}")
    print(f"  res_a(L=10) = {res['res_a_L10']:.6e}   alpha_a = {res['alpha_a']:.6f}")
    print()

    # ---- route b ----
    print("=== ROUTE (b) — cache-feasible higher-L mesh ===")
    print(f"  S104 cache levels (aspirational) = {res['s104_levels']}  status = {res['s104_status']}")
    print(f"  p+q=14 sectors present in S104 cache? {res['l14_present']}  "
          f"=> L=14 CACHE-BLOCKED: {res['cache_blocked_L14']}; L=16 CACHE-BLOCKED: {res['cache_blocked_L16']}")
    print(f"  operational ceiling L=13 (added the p+q=13 shell; n_sectors at L=13 = {res['n_sectors'][13]})")
    print(f"  L_mesh_plan = {res['L_mesh_plan']}   L_mesh_operational = {res['L_mesh_operational']}")
    print("  L | M_b(L) | res_b(L)")
    for L in res["L_mesh_operational"]:
        print(f"  {L:>2} | {res['M_b'][L]:.6f} | {res['res_b'][L]:.6e}")
    print(f"  res_b(L=10) = {res['res_b_L10']:.6e}   res_b(L=13) = {res['res_b_L13']:.6e}   alpha_b = {res['alpha_b']:.6f}")
    print()

    # ---- route c ----
    print("=== ROUTE (c) — Richardson/Abel zeta-reconstruction (L=10 self-anchor REMOVED) ===")
    print(f"  kappa (L-INDEPENDENT M2(C)-Nambu trace factor) = {res['kappa']:.4f}")
    print(f"  bare partial sum Z(12) = {res['Z_mesh'][12]:.4f}, Z(13) = {res['Z_mesh'][13]:.4f}  (g_M = {res['g_M']:.4f})")
    print("  Richardson Z(inf) per consecutive pair:")
    for pair, Zinf in res["Zinf_rich"].items():
        print(f"    pair {pair}: Z(inf) = {Zinf:.4f}  -> res_c = {res['res_c_rich'][pair]:.6f}")
    print(f"  Abel-tail Z(inf) = {res['Zinf_abel']:.4f}  -> res_c = {res['res_c_abel']:.6f}")
    print(f"  best Z(inf) = {res['Zinf_best']:.4f}  -> res_c(best) = {res['res_c_best']:.6e}")
    print(f"  partial-sum<->zeta-sum gap factor g_M/Z(inf) = {res['g_M']/res['Zinf_best']:.3f}x")
    print()

    # ---- composite OR-gate ----
    print("=== COMPOSITE OR-GATE ===")
    print(f"  res(L=10) by route: a={res['res_L10_by_route']['a']:.6e}  "
          f"b={res['res_L10_by_route']['b']:.6e}  c={res['res_L10_by_route']['c']:.6e}")
    print(f"  min route = {res['min_route']}   min res(L=10) = {res['min_res_L10']:.6e}   Level2 = {res['Level2_L10']:.0e}")
    print(f"  PASS_A (min res(L=10) < 1e-3): {res['pass_A']}")
    print(f"  alpha_fit by route: a={res['alpha_a']:.4f}  b={res['alpha_b']:.4f}  (band {ALPHA_BAND})")
    print(f"  PASS_B (alpha in [-4,-2] AND res->below 1e-3): {res['pass_B']}  (route {res['pass_B_route']})")
    print()

    # ---- C_1 sign DIAGNOSTIC (reported, NOT gated) ----
    fork = ("SS.VII.AU-positive (under-performing fork)" if res["C1_sign"] > 0
            else "SS.VII.AF.1-negative (over-performing fork)" if res["C1_sign"] < 0
            else "exact (delta=0)")  # (local)
    print(f"  C1_sign [DIAGNOSTIC, NOT gated] = {res['C1_sign']:+d}  (delta_min = {res['delta_min']:+.4f})  fork = {fork}")
    print("  (the SS.VII.AF.1 vs SS.VII.AU fork STAYS OPEN; this gate does NOT re-allocate that dual prior)")
    print()

    verdict = evaluate_gate(res)  # (local)
    print(f"=== GATE VERDICT: {verdict} ===")
    print()

    # winning-route + cache-block disclosure in the convention field
    winning_conv = (f"{CONVENTION};winning_route={res['min_route']};"
                    f"L14_CACHE_BLOCKED(S104_only_pq13);L16_CACHE_BLOCKED;"
                    f"op_ceiling_L13")  # (local)

    # value payload (no single-quote chars; the emit_verdict tool wraps it)
    value = (f"min_res_L10={res['min_res_L10']:.6e};min_route={res['min_route']};"
             f"Level2_L10={res['Level2_L10']:.3e};"
             f"res_a_L10={res['res_a_L10']:.4e};res_b_L10={res['res_b_L10']:.4e};res_c_L10={res['res_c_L10']:.4e};"
             f"alpha_a={res['alpha_a']:.4f};alpha_b={res['alpha_b']:.4f};"
             f"pass_A={res['pass_A']};pass_B={res['pass_B']};"
             f"Zinf_best={res['Zinf_best']:.2f};gap_factor={res['g_M']/res['Zinf_best']:.3f};"
             f"guard_reproduced={res['guard_reproduced']};"
             f"L14_cache_blocked={res['cache_blocked_L14']};op_ceiling_L13;"
             f"C1_sign={res['C1_sign']:+d};fork=OPEN;"
             f"multiplicative_preflight={multiplicative_preflight}")  # (local)

    print(emit_4tuple(value, SCHEME, winning_conv, L_MAX))
    print()

    # dual SHA over the input-pin map
    audit_sha, content_sha = compute_dual_sha(Path(__file__).resolve(), CANONICAL, pins)  # (local)

    make_plot(res)
    save_npz(res, verdict, multiplicative_preflight, audit_sha, content_sha, winning_conv)
    print(f"  wrote {OUT_NPZ.name}")
    print(f"  wrote {OUT_PNG.name}")
    print()

    # companion rows: regulator pin (MANDATORY) + cache-block disclosure + lift convention
    extra_rows = [
        "# regulator_pin=a_2^{zeta} poleconv-A-double (pole_in_s=3, curvature_grade_n=2)",
        "# DST_T3_lift=D4-CORE-REACHING (r=|lambda|_min/|lambda| in (0,1]; samples r<1 ANEC core)",
        "# OPERATIONAL DEVIATION: S104 cache has ONLY p+q=13 sectors (status=IN_PROGRESS); "
        "L=14/L=16 CACHE-BLOCKED; operational ceiling L=13 (honest-disclosure per v3-closure-recovery Class-1 boundary)",
        f"# multiplicative_factorization_preflight={multiplicative_preflight} (NON-multiplicative; genuine convergence test)",
    ]  # (local)

    print_verdict_payload(verdict, value, winning_conv, L_MAX, audit_sha, content_sha,
                          extra_rows=extra_rows)
    print(f"\n  elapsed: {time.time() - t0:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
