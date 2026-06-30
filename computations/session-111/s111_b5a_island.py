"""S111 §W4-1 — White-hole exit-slice ISLAND / QES microstate entropy = A/4 test.

Gate ID : S111-CF-B5A-ISLAND
Author  : hawking-theorist
Trigger : [SIGN]   (directional pre-registration: the island bulk-EE term is
                    NON-NEGATIVE, so R_island >= R_edge = 0.4737 — the ratio RISES
                    toward 1; SIGN of the island correction is POSITIVE / gap-closing)
Class   : GEOMETRIC (the white-hole exit slice IS the spectral-triple structure on
                    the exit configuration; the boundary entropy is a spectral
                    functional of D_K^{<=L}, not a field on a container)

WHAT THIS GATE TESTS
--------------------
S110-CF-B5A-MICROSTATE (FAIL, test_ratio=0.4737) counted ONLY the boundary
edge-mode piece S_boundary = N(|lambda| <= lambda_exit) = 9372, undercounting
A/4 = 17806.5658 by ~factor 1.9 (S_boundary/(A/4) = 0.5263).  That count is the
Area(partial I)/4 piece ALONE — the S110 construction OMITTED the bulk
entanglement-entropy contribution of the island region.

The QES / island formula (Engelhardt-Wall 2014; Penington / Almheiri-Mahajan-
Maldacena-Zhao 2019) is

    S_island  =  ext_X [ Area(partial I)/4  +  S_bulk-EE(I) ]

where
  * Area(partial I)/4 = c_conical * A_X(tau_fold)  is the a_2^{Pauli-Villars}
    conical-defect boundary term (c_conical = 0.25 from inv4_w1_euclidean_replica.npz),
    evaluated as the cumulative a_2 second-moment spectral weight enclosed up to the
    island-boundary eigenvalue threshold X = lambda_X; and
  * S_bulk-EE(I) = -Tr[rho_I ln rho_I] >= 0  is the von-Neumann entropy of the
    D_K^{<=L} bulk modes restricted to the island region I (the GGE-occupied
    exit-slice Peter-Weyl modes with |lambda| <= lambda_X), NON-NEGATIVE by
    construction.

We EXTREMIZE the generalized entropy S_gen(X) = Area(partial I)/4 + S_bulk-EE(I)
over the island-boundary location X = lambda_X (the exit-slice radial threshold),
find the quantum-extremal surface lambda_QES (dS_gen/dX = 0), and test

    R_island = S_island / (A_horizon_FW/4)   against  |R_island - 1| <= 0.10.

SUBSTRATE-FIRST DIRECTION OF EXPLANATION
----------------------------------------
  D_K^{<=L} eigenvalues
     -> conical a_2^{PV} Seeley-DeWitt coeff (gravity IS the 2nd spectral moment)
        -> Area(partial I)/4 boundary term
     -> GGE occupation of the bulk modes in the island
        -> S_bulk-EE(I) von-Neumann entropy
     -> S_gen extremization -> S_island -> comparison to the emergent area A/4
        (A = a_2 second moment, NOT a pre-existing container).

The island formula is the substrate's OWN emergent generalized-entropy functional,
NOT a holographic prescription imported from AdS/CFT.  A/4 is DERIVED from the
substrate spectral monotonicity (the area theorem is a Level-3 emergent
consequence, per phononic-framing.md "IS Space").  GR / Bekenstein-Hawking
S = A/4 is the emergent image of the substrate edge-mode + bulk-EE count, not the
input.

Output:
  - data   : computations/session-111/s111_b5a_island.npz
  - plot   : computations/session-111/s111_b5a_island.png
  - verdict: emitted via emit_verdict MCP (payload printed here)
"""

# CPU thread cap BEFORE numpy import (math-scripts.md  Environment).  The bulk-EE
# of a GGE state is DIAGONAL in the mode-occupation basis: S = sum_k s(n_k), a
# vectorized reduction over the 166,896-length occupation array.  No dense
# diagonalization is needed (the per-sector reduced density matrix is diagonal in
# the GGE occupation basis -> its eigenvalues ARE the occupations).  The GPU path
# is used for the per-mode occupation/entropy reduction + the cumulative area
# sums (and cross-checked vs numpy); CPU-OMP8 caps the numpy fallback.
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import math
import hashlib
from pathlib import Path
from collections import defaultdict

import numpy as np

# ---------------------------------------------------------------------------
# Canonical constants (S34+ MANDATORY)
# ---------------------------------------------------------------------------
ROOT = Path("C:/sandbox/Ainulindale Exflation")
sys.path.insert(0, str(ROOT / "computations" / "_shared"))
from canonical_constants import (  # noqa: E402
    M_KK, tau_fold, A_horizon_FW, a2_fold, a0_fold, T_H_FW,
)

# ---------------------------------------------------------------------------
# Identity / pins  (plan section W4-1 PRDR)
# ---------------------------------------------------------------------------
SESSION = 111  # (local)
WAVE = "w4"  # (local)
GATE_ID = "S111-CF-B5A-ISLAND"
SCHEME = "QES-island-construction"
CONVENTION = "RATIO"
L_MAX_PLAN = 12  # (local)
TAU_EXIT = 0.16  # (local) white-hole exit slice (S95 supersonic exit horizon); same as S110
N_EVAL = 300  # (local) island-boundary X extremization grid (matches inv4_w1 n_grid resolution class)
LAMBDA_SCAN = (0.5, 6.0)  # (local) island-boundary radial extremization window (plan scan_range)
QES_TOL = 1e-9  # (local) QES extremization stationarity tolerance dS_gen/dX = 0

# Pre-registered thresholds (plan W4-1 PRDR)
PASS_TOL = 0.10   # (local) |R_island - 1| <= 0.10  -> PASS
INFO_TOL = 0.25   # (local) 0.10 < |R_island - 1| <= 0.25 -> INFO ; else FAIL

# S110 predecessor pins (the area piece + threshold this gate inherits)
S_BOUNDARY_S110 = 9372       # (local) S110 boundary edge-mode count = Area(dI)/4 piece alone
LAMBDA_EXIT_S110 = 2.4893    # (local) S110 exit-slice horizon threshold
THETA_EXIT_S110 = 0.3630     # (local) S110 exit-slice fold fraction
R_EDGE_S110 = 0.5263         # (local) S110 S_boundary/(A/4) = 9372/17806.5658

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
OUT_DIR = ROOT / "computations" / f"session-{SESSION}"
OUT_DIR.mkdir(parents=True, exist_ok=True)
SCRIPT_PATH = OUT_DIR / "s111_b5a_island.py"
NPZ_PATH = OUT_DIR / "s111_b5a_island.npz"
PNG_PATH = OUT_DIR / "s111_b5a_island.png"

SPECTRUM_CACHE = ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
CANONICAL_CONSTS = ROOT / "computations" / "_shared" / "canonical_constants.py"
CONICAL_REF = ROOT / "computations" / "investigation-4" / "inv4_w1_euclidean_replica.npz"


def sha256_of_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def closure_hash(pin_map: dict) -> str:
    """SHA-256 over ordered (key,value) pairs of the input-pin map."""
    items = sorted(pin_map.items())
    s = "|".join(f"{k}={v}" for k, v in items)
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def content_hash(text: str) -> str:
    return hashlib.sha256(text.rstrip("\n").encode("utf-8")).hexdigest()


def print_verdict_payload(verdict, value_str, audit_sha, content_sha,
                          sign_v, mag_v, regime_v):
    """Print the verdict payload for the agent to forward to emit_verdict."""
    print()
    print("=" * 80)
    print("VERDICT PAYLOAD (forward to emit_verdict MCP)")
    print("=" * 80)
    print(f"gate_id   = {GATE_ID}")
    print(f"verdict   = {verdict}")
    print(f"value     = {value_str}")
    print(f"scheme    = {SCHEME}")
    print(f"convention= {CONVENTION}")
    print(f"L_max     = {L_MAX_PLAN}")
    print(f"sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v}")
    print(f"audit_sha256   = {audit_sha}")
    print(f"content_sha256 = {content_sha}")
    print("=" * 80)


# ===========================================================================
# SHA INPUT log
# ===========================================================================
print("=" * 80)
print(f"GATE ID: {GATE_ID}")
print(f"SESSION: {SESSION}   WAVE: {WAVE}")
print("=" * 80)

INPUT_PINS = {
    "canonical_constants": sha256_of_file(CANONICAL_CONSTS),
    "L12_master_cache": sha256_of_file(SPECTRUM_CACHE),
    "conical_replica": sha256_of_file(CONICAL_REF),
}
for k, v in INPUT_PINS.items():
    print(f"SHA INPUT: {k} = {v}")

# ===========================================================================
# Substitution chain (plan W4-1) -- printed for audit trail
# ===========================================================================
A_quarter = A_horizon_FW / 4.0  # (local) Bekenstein-Hawking target
print()
print("-" * 80)
print("SUBSTITUTION CHAIN (plan section W4-1):")
print("  Claim: island bulk-EE term is NON-NEGATIVE => R_island >= R_edge = 0.4737;")
print("         the ratio RISES toward 1 (SIGN of the correction is POSITIVE).")
print(f"  Step 1: R_edge = S_boundary/(A/4) = {S_BOUNDARY_S110}/{A_quarter:.4f} "
      f"= {S_BOUNDARY_S110/A_quarter:.4f}  [S110, FAIL]")
print("  Step 2: S_island := ext_X[ Area(dI)/4 + S_bulk-EE(I) ];")
print("          Area(dI)/4 = c_conical*A_X (a_2^{PV} conical), S_bulk-EE(I) >= 0 (von-Neumann)")
print("  Step 3: at extremal X, edge count IS the Area piece; S_island = S_boundary + S_bulk-EE(I)")
print("  Step 4: R_island = R_edge + S_bulk-EE(I)/(A/4) = R_edge + (NON-NEGATIVE)")
print("  Step 5: S_bulk-EE(I) >= 0 => R_island >= R_edge (direction POSITIVE; ratio rises)")
print(f"  Conclusion: PASS iff |R_island - 1| <= {PASS_TOL}; INFO iff <= {INFO_TOL}; else FAIL")
print("-" * 80)


# ===========================================================================
# Load conical 1/4 reference (the Area(dI)/4 normalization)
# ===========================================================================
conical = np.load(CONICAL_REF, allow_pickle=True)
c_conical = float(conical["c_conical"])                  # (local) 0.25000
S_replica = float(conical["S_replica"])                  # (local) 17806.57  == A/4 (full horizon)
A_quarter_ref = float(conical["A_quarter"])              # (local) 17806.566 cross-check
A_horizon_FW_ref = float(conical["A_horizon_FW"])        # (local) 71226.26 cross-check
a2_fold_canonical_repl = float(conical["a2_fold_canonical"])  # (local) 2776.165
n_eval_repl = int(conical["n_eval"])                     # (local) 166896 total modes

print()
print("Upstream conical-replica references (the Area(dI)/4 = A/4 normalization):")
print(f"  c_conical (a_2^{{PV}} conical coeff)       = {c_conical:.7f}")
print(f"  S_replica (full-horizon Area/4)           = {S_replica:.6f}")
print(f"  A/4 cross-check (canonical vs replica npz): {A_quarter:.6f} == {A_quarter_ref:.6f}")
assert abs(A_quarter - A_quarter_ref) < 1e-4, (
    f"A/4 mismatch: canonical {A_quarter} vs replica npz {A_quarter_ref}"
)
assert abs(A_horizon_FW - A_horizon_FW_ref) < 1e-4, (
    f"A mismatch: canonical {A_horizon_FW} vs replica npz {A_horizon_FW_ref}"
)
# The replica DERIVES Area/4 == A/4 at the full horizon (c_conical=0.25, |R-1|=5e-7).
# So the conical Area(dI)/4 coefficient normalizes the enclosed-area term such that
# the FULL exit slice gives exactly A/4.
print(f"  => Area(dI)/4 normalization fixed: full-slice Area/4 = {S_replica:.4f} == A/4")


# ===========================================================================
# Step 1: load the L12 exit-slice spectral triple; build eigenvalue tower
# ===========================================================================
print()
print("=" * 80)
print("Step 1: L12-truncated exit-slice spectral triple")
print("=" * 80)

data = np.load(SPECTRUM_CACHE, allow_pickle=True)
sectors = data["sector_evals"].item()  # dict (p,q) -> {dim, level, abs_evals}
sectors12 = {(p, q): info for (p, q), info in sectors.items() if p + q <= L_MAX_PLAN}
n_sectors = len(sectors12)  # (local)

abs_evals_all = np.concatenate(
    [np.asarray(info["abs_evals"], dtype=np.float64) for info in sectors12.values()]
)
abs_evals_all = abs_evals_all[abs_evals_all > 0.0]  # exclude kernel modes
abs_evals_all = np.sort(abs_evals_all)
N_total_modes = int(abs_evals_all.size)  # (local)
lam_min = float(abs_evals_all[0])        # (local)
lam_max = float(abs_evals_all[-1])       # (local)
print(f"L_max={L_MAX_PLAN}: {n_sectors} Peter-Weyl sectors, "
      f"{N_total_modes} total edge-eligible modes (with multiplicity)")
print(f"  |lambda| range: [{lam_min:.6f}, {lam_max:.6f}]  (M_KK units)")
# Cross-check the total against the replica n_eval (same spectral support)
print(f"  N_total_modes={N_total_modes}  vs replica n_eval={n_eval_repl}  "
      f"(match: {N_total_modes == n_eval_repl})")


# ===========================================================================
# GPU helper: ship the eigenvalue tower once; per-mode reductions on GPU.
# ===========================================================================
USE_GPU = False  # (local)
try:
    import torch
    if torch.cuda.is_available():
        USE_GPU = True
        DEV = torch.device("cuda")
        lam_t = torch.tensor(abs_evals_all, device=DEV, dtype=torch.float64)
        # GPU/CPU cross-check on a small slice (computation-environment.md)
        test_n = min(2000, N_total_modes)  # (local)
        cum_gpu = torch.cumsum(lam_t[:test_n] ** 2, dim=0).cpu().numpy()
        cum_cpu = np.cumsum(abs_evals_all[:test_n] ** 2)
        xchk = float(np.max(np.abs(cum_gpu - cum_cpu)))  # (local)
        print(f"  GPU active: {torch.cuda.get_device_name(0)}; "
              f"cumsum GPU/CPU max-abs-diff (first {test_n}) = {xchk:.3e}")
        assert xchk < 1e-6, f"GPU/CPU cumsum mismatch {xchk}"
    else:
        print("  GPU not available; numpy.linalg CPU-OMP8 path")
except Exception as e:  # noqa: BLE001
    print(f"  torch unavailable ({e}); numpy CPU-OMP8 path")


# ===========================================================================
# Step 2: Area(partial I)/4 enclosed-area term as a function of the island
# boundary threshold lambda_X  (a_2^{PV} conical second-moment spectral weight)
# ===========================================================================
print()
print("=" * 80)
print("Step 2: Area(dI)/4(lambda_X) = c_conical * A_X  (a_2 second-moment enclosed area)")
print("=" * 80)

# The emergent area operator is the a_2 SECOND Seeley-DeWitt moment.  The area
# ENCLOSED up to the island-boundary eigenvalue threshold lambda_X is the
# cumulative second-moment spectral weight (sum lambda^2) of the modes with
# |lambda| <= lambda_X, NORMALIZED so that the FULL slice reproduces the
# conical-replica A/4 = S_replica (c_conical=0.25 fixes the 1/4).
#
#   Area(dI)/4 (lambda_X) = S_replica * [ sum_{|lambda|<=lambda_X} lambda^2 ]
#                                       / [ sum_{all} lambda^2 ]
#
# This is the substrate-first definition: the a_2 area operator's enclosed
# spectral weight, scaled by the conical 1/4 (S_replica == A/4 at the full slice).
# It is INDEPENDENT of A/4 except through the fixed conical normalization.

sq_all = abs_evals_all ** 2  # (local)
total_a2_weight = float(np.sum(sq_all))  # (local)

if USE_GPU:
    cum_a2_weight_full = torch.cumsum(lam_t ** 2, dim=0).cpu().numpy()  # (local)
else:
    cum_a2_weight_full = np.cumsum(sq_all)  # (local)

# Build the island-boundary scan grid in lambda_X over the plan window, clamped
# to the spectral support.
lo = max(LAMBDA_SCAN[0], lam_min)  # (local)
hi = min(LAMBDA_SCAN[1], lam_max)  # (local)
lambda_grid = np.linspace(lo, hi, N_EVAL)  # (local)

# For each lambda_X: cumulative a_2 weight enclosed -> Area(dI)/4.
def area_quarter_of(lx):
    """Area(partial I)/4 enclosed up to threshold lambda_X (a_2 second moment)."""
    idx = int(np.searchsorted(abs_evals_all, lx, side="right"))  # (local)
    if idx <= 0:
        return 0.0
    enclosed = cum_a2_weight_full[idx - 1]  # (local)
    return S_replica * (enclosed / total_a2_weight)

# Also the raw EDGE-MODE count (the S110 quantity) for diagnostics.
def edge_count_of(lx):
    return int(np.searchsorted(abs_evals_all, lx, side="right"))  # (local)

# Sanity: at the full slice, Area/4 -> S_replica == A/4.
area_full = area_quarter_of(lam_max + 1.0)  # (local)
print(f"  total a_2 second-moment weight sum(lambda^2) = {total_a2_weight:.4f}")
print(f"  Area(dI)/4 at full slice = {area_full:.4f}  (target A/4 = {A_quarter:.4f}; "
      f"|R-1| = {abs(area_full/A_quarter - 1):.3e})")
# At the S110 threshold lambda_exit=2.4893:
area_at_s110 = area_quarter_of(LAMBDA_EXIT_S110)  # (local)
edge_at_s110 = edge_count_of(LAMBDA_EXIT_S110)  # (local)
print(f"  At S110 lambda_exit={LAMBDA_EXIT_S110}: Area(dI)/4 = {area_at_s110:.4f}, "
      f"edge-count = {edge_at_s110} (S110 used {S_BOUNDARY_S110})")


# ===========================================================================
# Step 3: S_bulk-EE(I) von-Neumann entropy of the GGE-occupied island modes
# ===========================================================================
print()
print("=" * 80)
print("Step 3: S_bulk-EE(I) = -Tr[rho_I ln rho_I]  (GGE bulk modes inside island)")
print("=" * 80)

# The bulk modes are GGE-occupied at the exit-slice acoustic temperature.  The
# reduced density matrix on the island modes is DIAGONAL in the occupation basis
# (a GGE / thermal state factorizes mode-by-mode), so its von-Neumann entropy is
#
#   S_bulk-EE(I) = sum_{|lambda|<=lambda_X}  s(n_lambda)
#   s(n) = (1+n) ln(1+n) - n ln n        [Bose-Einstein single-mode entropy]
#
# with the per-mode GGE occupation set by the exit-slice horizon temperature.
# The emergent exit-slice Hawking/acoustic temperature is T_H_FW (the substrate's
# emergent horizon temperature; A = 1/(4 pi T_H^2) ties A_horizon_FW to T_H_FW).
# The dimensionless mode energy is |lambda| in M_KK units; the GGE occupation is
#
#   n_lambda = 1 / ( exp(|lambda| / T_acoustic) - 1 )
#
# where T_acoustic is the exit-slice acoustic temperature in M_KK units.  We fix
# T_acoustic from the substrate's OWN exit-slice scale: the median eigenvalue of
# the spectral support sets the thermal scale at which the GGE relic forms (the
# van Hove fold concentrates spectral weight; the occupation is O(1) at the
# characteristic mode scale).  This is substrate-first (NOT fitted to A/4): the
# thermal scale is the spectral-support characteristic eigenvalue.

# Characteristic acoustic temperature: the spectral-support scale at the fold.
# Use the MEDIAN |lambda| (robust central scale of the exit-slice spectrum) as
# the thermal scale -> O(1) occupations across the band, peaked at the soft modes.
T_acoustic = float(np.median(abs_evals_all))  # (local) exit-slice thermal scale (M_KK units)
print(f"  T_acoustic (exit-slice spectral median |lambda|) = {T_acoustic:.6f} M_KK units")

# Per-mode GGE occupation and single-mode von-Neumann entropy (vectorized).
if USE_GPU:
    x = lam_t / T_acoustic                                   # (local)
    n_occ = 1.0 / (torch.expm1(x))                            # Bose-Einstein
    n_occ = torch.clamp(n_occ, min=1e-300)
    s_mode = (1.0 + n_occ) * torch.log1p(n_occ) - n_occ * torch.log(n_occ)
    s_mode_np = s_mode.cpu().numpy()                          # (local)
    cum_S_bulk_full = torch.cumsum(s_mode, dim=0).cpu().numpy()  # (local)
    # cross-check first 2000 on CPU
    xx = abs_evals_all[:2000] / T_acoustic
    nn = 1.0 / np.expm1(xx)
    nn = np.clip(nn, 1e-300, None)
    ss = (1.0 + nn) * np.log1p(nn) - nn * np.log(nn)
    sxchk = float(np.max(np.abs(s_mode_np[:2000] - ss)))  # (local)
    print(f"  s_mode GPU/CPU max-abs-diff (first 2000) = {sxchk:.3e}")
    assert sxchk < 1e-9, f"GPU/CPU s_mode mismatch {sxchk}"
else:
    xx = abs_evals_all / T_acoustic
    nn = 1.0 / np.expm1(xx)
    nn = np.clip(nn, 1e-300, None)
    s_mode_np = (1.0 + nn) * np.log1p(nn) - nn * np.log(nn)  # (local)
    cum_S_bulk_full = np.cumsum(s_mode_np)  # (local)

S_bulk_total = float(cum_S_bulk_full[-1])  # (local)
print(f"  S_bulk-EE (full slice, all modes) = {S_bulk_total:.4f}")
print(f"  per-mode entropy range: [{s_mode_np.min():.4e}, {s_mode_np.max():.4e}]")

def S_bulk_of(lx):
    """von-Neumann bulk-EE enclosed up to island boundary lambda_X."""
    idx = int(np.searchsorted(abs_evals_all, lx, side="right"))  # (local)
    if idx <= 0:
        return 0.0
    return float(cum_S_bulk_full[idx - 1])


# ===========================================================================
# Step 4: generalized entropy S_gen(lambda_X) over the island-boundary scan
# ===========================================================================
print()
print("=" * 80)
print("Step 4: S_gen(lambda_X) = Area(dI)/4 + S_bulk-EE(I) over the scan window")
print("=" * 80)

area_grid = np.array([area_quarter_of(lx) for lx in lambda_grid])     # (local)
sbulk_grid = np.array([S_bulk_of(lx) for lx in lambda_grid])          # (local)
sgen_grid = area_grid + sbulk_grid                                    # (local)
R_grid = sgen_grid / A_quarter                                        # (local)

# ANTI-TAUTOLOGY DISCIPLINE (S110 author's caution carried forward):
#   "If the boundary count were forced to equal A/4 by construction the ratio
#    would be 1 trivially; instead lambda_exit is a substrate-geometry quantity
#    and the count is a free prediction."
#
# Both Area(dI)/4 and S_bulk-EE are MONOTONE NON-DECREASING in lambda_X
# (cumulative sums of non-negative weights), so S_gen is monotone non-decreasing.
# A NAIVE QES prescription "pick lambda where S_gen == A/4" would force R = 1 by
# construction -- a TAUTOLOGY that closes the gate trivially regardless of physics.
# We therefore DO NOT use the S_gen == A/4 crossing as the canonical value.
#
# The QES / island prescription on a finite spectral triple selects the island
# whose boundary sits at the SUBSTRATE-FIXED exit-slice marker lambda_exit
# (S110's substrate-geometry threshold, derived from the a_0/a_2 area-perimeter
# fold geometry, NOT chosen to hit A/4).  At that fixed boundary the island
# entropy is S_island = Area(dI)/4 + S_bulk-EE(I) -- the genuine prediction of the
# plan's substitution chain (Step 5 below).  The S_gen == A/4 crossing is reported
# ONLY as a DIAGNOSTIC (where the island boundary WOULD have to sit to reach A/4),
# explicitly NOT as the canonical verdict value.

# DIAGNOSTIC ONLY: lambda where S_gen is closest to A/4 (NOT the canonical value).
idx_qes = int(np.argmin(np.abs(sgen_grid - A_quarter)))  # (local)
lambda_QES = float(lambda_grid[idx_qes])                 # (local) DIAGNOSTIC
S_island_QES = float(sgen_grid[idx_qes])                 # (local) DIAGNOSTIC
R_island_QES = S_island_QES / A_quarter                  # (local) ~1 by construction
area_QES = float(area_grid[idx_qes])                     # (local)
sbulk_QES = float(sbulk_grid[idx_qes])                   # (local)

# (b) Maximal island = full exit slice (entire exit fiber is the island).
S_island_full = float(sgen_grid[-1])                     # (local)
R_island_full = S_island_full / A_quarter                # (local)

# (c) Refine the QES nucleation point by bisection on (S_gen - A/4) for the
#     stationary-against-horizon condition (dense interpolation).
#     S_gen is monotone increasing => unique crossing of A/4.
def sgen_continuous(lx):
    return area_quarter_of(lx) + S_bulk_of(lx)  # (local)

# bisection for S_gen(lx) = A_quarter
a_lo, a_hi = lo, hi  # (local)
f_lo = sgen_continuous(a_lo) - A_quarter  # (local)
f_hi = sgen_continuous(a_hi) - A_quarter  # (local)
lambda_QES_refined = lambda_QES  # (local) default
if f_lo * f_hi < 0:
    for _ in range(200):
        mid = 0.5 * (a_lo + a_hi)  # (local)
        fm = sgen_continuous(mid) - A_quarter  # (local)
        if abs(fm) < QES_TOL * A_quarter:
            break
        if f_lo * fm < 0:
            a_hi = mid
        else:
            a_lo = mid
            f_lo = fm
    lambda_QES_refined = 0.5 * (a_lo + a_hi)
S_island_refined = sgen_continuous(lambda_QES_refined)   # (local)
R_island_refined = S_island_refined / A_quarter          # (local)

print(f"  Area(dI)/4 monotone non-decreasing: {np.all(np.diff(area_grid) >= -1e-9)}")
print(f"  S_bulk-EE  monotone non-decreasing: {np.all(np.diff(sbulk_grid) >= -1e-9)}")
print(f"  S_gen      monotone non-decreasing: {np.all(np.diff(sgen_grid) >= -1e-9)}")
print()
print("  QES nucleation point (S_gen stationary against A/4 horizon constraint):")
print(f"    lambda_QES (grid)    = {lambda_QES:.6f}   S_island = {S_island_QES:.4f}  "
      f"R = {R_island_QES:.6f}")
print(f"    lambda_QES (refined) = {lambda_QES_refined:.6f}   S_island = {S_island_refined:.4f}  "
      f"R = {R_island_refined:.6f}")
print(f"    decomposition at QES: Area(dI)/4 = {area_QES:.4f} + S_bulk-EE = {sbulk_QES:.4f}")
print()
print("  Maximal island (full exit slice = entire exit fiber):")
print(f"    S_island_full = {S_island_full:.4f}  R = {R_island_full:.6f}  "
      f"(Area/4={area_grid[-1]:.4f} + S_bulk={sbulk_grid[-1]:.4f})")


# ===========================================================================
# Step 5: PRIMARY island construction at the S110 exit-slice anchor
#         (the plan's substitution chain: R_island = R_edge + S_bulk-EE/(A/4))
# ===========================================================================
print()
print("=" * 80)
print("Step 5: PRIMARY island entropy at the S110 exit-slice anchor lambda_exit")
print("=" * 80)

# The plan's substitution chain pins the PRIMARY test at the S110 exit-slice
# threshold: the area piece is S_boundary=9372 (S110), and we ADD the bulk-EE of
# the SAME island region.  R_island = R_edge + S_bulk-EE(I)/(A/4).
# Here Area(dI)/4 at the island IS the S110 edge count (the S110 construction's
# "boundary entropy"), and the island region I = {modes with |lambda| <= lambda_exit}.
area_piece_primary = float(S_BOUNDARY_S110)              # (local) S110 Area(dI)/4 = 9372
sbulk_primary = S_bulk_of(LAMBDA_EXIT_S110)              # (local) bulk-EE of island modes
S_island_primary = area_piece_primary + sbulk_primary    # (local)
R_island_primary = S_island_primary / A_quarter          # (local)
R_edge_check = area_piece_primary / A_quarter            # (local) == R_EDGE_S110

print(f"  R_edge (S110 area piece)        = {R_edge_check:.6f}  (S110: {R_EDGE_S110})")
print(f"  S_bulk-EE(I) at lambda_exit     = {sbulk_primary:.4f}")
print(f"  S_island = S_boundary + S_bulk  = {area_piece_primary:.1f} + {sbulk_primary:.4f}"
      f" = {S_island_primary:.4f}")
print(f"  R_island_primary = R_edge + S_bulk/(A/4) = {R_edge_check:.4f} + "
      f"{sbulk_primary/A_quarter:.4f} = {R_island_primary:.6f}")

# The SIGN check (plan substitution chain Step 5): R_island >= R_edge (correction
# is non-negative).
sign_correct_primary = R_island_primary >= R_edge_check - 1e-12  # (local)
print(f"  SIGN check: R_island ({R_island_primary:.4f}) >= R_edge "
      f"({R_edge_check:.4f}): {sign_correct_primary}")

# --- ROBUSTNESS: T_acoustic sensitivity of the bulk-EE / R_island ----------
# The single free physics input is T_acoustic (the GGE thermal scale).  We
# pre-registered it as the spectral-support MEDIAN (substrate-first central
# scale).  To keep the verdict HONEST we record how R_island moves across a
# defensible range of thermal scales -- so the FAIL is reported with its
# sensitivity, NOT cherry-picked.  We DO NOT switch T_acoustic to reach PASS
# (that would be iterate-until-PASS, PROHIBITED Class 2).
island_ev = abs_evals_all[abs_evals_all <= LAMBDA_EXIT_S110]  # (local) island modes
def _sbulk_island(T):
    x = island_ev / T
    n = 1.0 / np.expm1(x); n = np.clip(n, 1e-300, None)
    return float(np.sum((1.0 + n) * np.log1p(n) - n * np.log(n)))
T_cands = {  # (local) defensible substrate thermal scales
    "median_all": float(np.median(abs_evals_all)),
    "median_island": float(np.median(island_ev)),
    "mean_island": float(np.mean(island_ev)),
    "lam_exit": LAMBDA_EXIT_S110,
}
print("  T_acoustic sensitivity (R_island = (S_boundary + S_bulk)/(A/4)):")
T_scan_names = []   # (local)
T_scan_vals = []    # (local)
R_scan_vals = []    # (local)
for nm, Tc in T_cands.items():
    Sb = _sbulk_island(Tc)  # (local)
    Rc = (area_piece_primary + Sb) / A_quarter  # (local)
    vc = "PASS" if abs(Rc - 1) <= PASS_TOL else ("INFO" if abs(Rc - 1) <= INFO_TOL else "FAIL")  # (local)
    print(f"    T={nm:>14}={Tc:6.3f}  S_bulk={Sb:10.2f}  R={Rc:7.4f}  |R-1|={abs(Rc-1):6.4f}  {vc}")
    T_scan_names.append(nm); T_scan_vals.append(Tc); R_scan_vals.append(Rc)
# Span of R across the thermal-scale choices (the band-landing is NOT robust):
R_scan_arr = np.array(R_scan_vals)  # (local)
R_scan_min = float(R_scan_arr.min())  # (local)
R_scan_max = float(R_scan_arr.max())  # (local)
print(f"  => R_island spans [{R_scan_min:.4f}, {R_scan_max:.4f}] across thermal scales: "
      f"band-landing is thermal-scale-SENSITIVE (the canonical median_all gives "
      f"{R_island_primary:.4f}).")


# ===========================================================================
# Step 6: select the canonical R_island for the verdict
# ===========================================================================
print()
print("=" * 80)
print("Step 6: canonical R_island selection + verdict")
print("=" * 80)

# CANONICAL selection (anti-tautology): the island boundary is FIXED at the
# substrate-geometry exit-slice marker lambda_exit (S110's a_0/a_2 fold threshold,
# NOT chosen to hit A/4).  The canonical island entropy is the PRIMARY value
#   S_island = Area(dI)/4 [= S110 edge count] + S_bulk-EE(I)
# = the plan's substitution-chain prediction R_island = R_edge + S_bulk/(A/4).
# This is a GENUINE prediction: the boundary is substrate-fixed, the only added
# physics is the non-negative bulk-EE.  The QES "S_gen == A/4 crossing"
# (R_island_refined ~ 1) is a TAUTOLOGY and is reported as DIAGNOSTIC ONLY.

R_island = R_island_primary  # (local) CANONICAL: substrate-fixed island + bulk-EE
S_island = S_island_primary  # (local)
lambda_island = LAMBDA_EXIT_S110  # (local) substrate-fixed exit-slice boundary

test_ratio = abs(R_island - 1.0)  # (local) |R_island - 1|
print(f"  CANONICAL R_island (substrate-fixed boundary + bulk-EE) = {R_island:.6f}")
print(f"  S_island = Area(dI)/4 + S_bulk-EE = {S_island:.4f}")
print(f"  island boundary lambda_exit (substrate-fixed)           = {lambda_island:.4f}")
print(f"  A/4 target                = {A_quarter:.4f}")
print(f"  test_ratio = |R_island-1| = {test_ratio:.6f}")
print()
print("  Cross-check ladder (all island constructions):")
print(f"    (S110 edge-only)         R_edge   = {R_edge_check:.4f}  (the FAIL predecessor)")
print(f"    (S110-anchor +bulk-EE)   R_island = {R_island:.4f}  <-- CANONICAL")
print(f"    (full-slice maximal)     R_full   = {R_island_full:.4f}")
print(f"    (QES S_gen==A/4 crossing R_qes    = {R_island_refined:.4f}  [DIAGNOSTIC ONLY, "
      f"tautological ~1; lambda would be {lambda_QES_refined:.4f}])")


# ===========================================================================
# Step 7: verdict (composite collapse rule)
# ===========================================================================
print()
print("=" * 80)
print("Step 7: verdict (SIGN/MAGNITUDE/REGIME 3-tuple + composite collapse)")
print("=" * 80)

# SIGN: the substitution chain predicts the island correction is POSITIVE
# (R_island >= R_edge).  sign_verdict = PASS iff the bulk-EE correction is
# non-negative (the ratio rose from the S110 edge-only baseline).
sign_correct = R_island >= R_edge_check - 1e-9  # (local) island rose above edge-only
sign_verdict = "PASS" if sign_correct else "FAIL"  # (local)
print(f"  sign_verdict = {sign_verdict}  (R_island={R_island:.4f} >= "
      f"R_edge={R_edge_check:.4f}: {sign_correct}; correction is POSITIVE/gap-closing)")

# MAGNITUDE: |R_island - 1| vs PASS/INFO bands.
if test_ratio <= PASS_TOL:
    magnitude_verdict = "PASS"  # (local)
elif test_ratio <= INFO_TOL:
    magnitude_verdict = "INFO"  # (local)
else:
    magnitude_verdict = "FAIL"  # (local)
print(f"  magnitude_verdict = {magnitude_verdict}  "
      f"(test_ratio={test_ratio:.6f}; PASS<= {PASS_TOL}, INFO<= {INFO_TOL})")

# REGIME: VALID iff the QES is a strict interior stationary point of the spectral
# support (lambda_island strictly inside [lam_min, lam_max]) and the S_gen
# crossing of A/4 is real (not a clamped endpoint).
qes_interior = lam_min < lambda_island < lam_max  # (local)
crossing_real = (f_lo * f_hi < 0) or (idx_qes not in (0, N_EVAL - 1))  # (local)
if qes_interior and crossing_real:
    regime_verdict = "VALID"  # (local)
elif qes_interior:
    regime_verdict = "MARGINAL"  # (local)
else:
    regime_verdict = "BREAKDOWN"  # (local)
print(f"  regime_verdict = {regime_verdict}  "
      f"(QES interior: {qes_interior}, lambda_island={lambda_island:.4f} in "
      f"[{lam_min:.4f},{lam_max:.4f}]; A/4-crossing real: {crossing_real})")

# COMPOSITE collapse (gate-verdicts.md  Composite-collapse rule)
if regime_verdict == "BREAKDOWN":
    composite_verdict = "FAIL"  # (local)
elif sign_verdict == "FAIL":
    composite_verdict = "FAIL"  # (local)
elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
    composite_verdict = "FAIL"  # (local)
elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
    composite_verdict = "INFO"  # (local)
elif magnitude_verdict == "INFO":
    composite_verdict = "INFO"  # (local)
else:
    composite_verdict = "PASS"  # (local)
print(f"  composite_verdict = {composite_verdict}")


# ===========================================================================
# Persist .npz
# ===========================================================================
print()
print("Persisting .npz")
np.savez(
    NPZ_PATH,
    # primary result (CANONICAL = QES)
    R_island=R_island,
    S_island=S_island,
    lambda_island=lambda_island,
    A_quarter=A_quarter,
    A_horizon_FW=A_horizon_FW,
    test_ratio=test_ratio,
    # verdicts
    sign_verdict=sign_verdict,
    magnitude_verdict=magnitude_verdict,
    regime_verdict=regime_verdict,
    composite_verdict=composite_verdict,
    PASS_TOL=PASS_TOL,
    INFO_TOL=INFO_TOL,
    # island construction ladder
    R_edge_S110=R_edge_check,
    S_boundary_S110=S_BOUNDARY_S110,
    lambda_exit_S110=LAMBDA_EXIT_S110,
    R_island_primary=R_island_primary,
    S_island_primary=S_island_primary,
    sbulk_primary=sbulk_primary,
    R_island_QES=R_island_QES,
    lambda_QES=lambda_QES,
    lambda_QES_refined=lambda_QES_refined,
    R_island_full=R_island_full,
    S_island_full=S_island_full,
    area_QES=area_QES,
    sbulk_QES=sbulk_QES,
    # bulk-EE machinery
    T_acoustic=T_acoustic,
    S_bulk_total=S_bulk_total,
    # T_acoustic robustness scan (the band-landing sensitivity)
    T_scan_names=np.array(T_scan_names),
    T_scan_vals=np.array(T_scan_vals),
    R_scan_vals=np.array(R_scan_vals),
    R_scan_min=R_scan_min,
    R_scan_max=R_scan_max,
    # area machinery
    c_conical=c_conical,
    S_replica=S_replica,
    total_a2_weight=total_a2_weight,
    area_full=area_full,
    # scan grids (for plot + audit)
    lambda_grid=lambda_grid,
    area_grid=area_grid,
    sbulk_grid=sbulk_grid,
    sgen_grid=sgen_grid,
    R_grid=R_grid,
    # spectrum diagnostics
    N_total_modes=N_total_modes,
    lam_min=lam_min,
    lam_max=lam_max,
    n_sectors=n_sectors,
    # SIGN bookkeeping
    sign_correct_primary=sign_correct_primary,
    used_gpu=USE_GPU,
)
print(f".npz written: {NPZ_PATH}  ({NPZ_PATH.stat().st_size} bytes)")


# ===========================================================================
# Plot (3 panels)
# ===========================================================================
print("Plotting")
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Panel A: S_gen(lambda_X) = Area/4 + S_bulk-EE, with A/4 line and QES.
ax = axes[0]
ax.plot(lambda_grid, area_grid, "-", color="steelblue", label=r"Area$(\partial I)/4$")
ax.plot(lambda_grid, sbulk_grid, "-", color="darkorange", label=r"$S_{bulk\text{-}EE}(I)$")
ax.plot(lambda_grid, sgen_grid, "-", color="navy", lw=2, label=r"$S_{gen}=$Area$/4+S_{bulk}$")
ax.axhline(A_quarter, color="green", linestyle=":", label=fr"$A/4={A_quarter:.0f}$")
ax.axvline(lambda_island, color="crimson", linestyle="--",
           label=fr"$\lambda_{{QES}}={lambda_island:.3f}$")
ax.plot([lambda_island], [S_island], "o", color="crimson", ms=9,
        label=fr"$S_{{island}}={S_island:.0f}$")
ax.set_xlabel(r"island boundary $\lambda_X$  ($M_{KK}$ units)")
ax.set_ylabel("entropy")
ax.set_title("Panel A: generalized entropy + QES extremization")
ax.legend(fontsize=7, loc="upper left")
ax.grid(True, alpha=0.3)

# Panel B: R_island ladder bar chart.
ax = axes[1]
labels = ["S110 edge\n(FAIL)", "S110+bulk\n(primary)", "QES\n(canonical)", "full slice\n(maximal)"]
vals = [R_edge_check, R_island_primary, R_island, R_island_full]
colors = ["grey", "steelblue",
          "crimson" if composite_verdict == "PASS" else
          ("gold" if composite_verdict == "INFO" else "firebrick"),
          "mediumseagreen"]
ax.bar(labels, vals, color=colors)
ax.axhline(1.0, color="green", linestyle=":", label=r"$R=1$ (= $A/4$)")
ax.axhspan(1 - PASS_TOL, 1 + PASS_TOL, color="green", alpha=0.15, label="PASS band")
ax.axhspan(1 - INFO_TOL, 1 - PASS_TOL, color="gold", alpha=0.15)
ax.axhspan(1 + PASS_TOL, 1 + INFO_TOL, color="gold", alpha=0.15, label="INFO band")
ax.set_ylabel(r"$R_{island}=S/(A/4)$")
ax.set_title(f"Panel B: island ratio ladder — {composite_verdict}")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel C: R_grid(lambda_X) trajectory with bands.
ax = axes[2]
ax.plot(lambda_grid, R_grid, "-", color="navy", label=r"$R_{island}(\lambda_X)$")
ax.axhline(1.0, color="green", linestyle=":", label=r"$R=1$")
ax.axhspan(1 - PASS_TOL, 1 + PASS_TOL, color="green", alpha=0.15, label="PASS")
ax.axhspan(1 - INFO_TOL, 1 - PASS_TOL, color="gold", alpha=0.12)
ax.axhspan(1 + PASS_TOL, 1 + INFO_TOL, color="gold", alpha=0.12, label="INFO")
ax.axvline(lambda_island, color="crimson", linestyle="--",
           label=fr"$\lambda_{{QES}}={lambda_island:.3f}$")
ax.axhline(R_edge_check, color="grey", linestyle="-.", label=fr"$R_{{edge}}={R_edge_check:.3f}$ (S110)")
ax.set_xlabel(r"island boundary $\lambda_X$  ($M_{KK}$ units)")
ax.set_ylabel(r"$R_{island}=S_{gen}/(A/4)$")
ax.set_title("Panel C: ratio trajectory vs island boundary")
ax.legend(fontsize=7, loc="upper left")
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(PNG_PATH, dpi=140, bbox_inches="tight")
plt.close()
print(f".png written: {PNG_PATH}  ({PNG_PATH.stat().st_size} bytes)")


# ===========================================================================
# Verdict-line SHAs
# ===========================================================================
PIN_MAP = {
    "gate_id": GATE_ID,
    "session": SESSION,
    "wave": WAVE,
    "scheme": SCHEME,
    "convention": CONVENTION,
    "L_max": L_MAX_PLAN,
    "N_eval": N_EVAL,
    "tau_exit_pin": TAU_EXIT,
    "tau_fold_pin": tau_fold,
    "M_KK_pin": M_KK,
    "A_horizon_FW_pin": A_horizon_FW,
    "T_H_FW_pin": T_H_FW,
    "a2_fold_pin": a2_fold,
    "a0_fold_pin": a0_fold,
    "PASS_TOL": PASS_TOL,
    "INFO_TOL": INFO_TOL,
    "lambda_scan": str(LAMBDA_SCAN),
    "regulator": "a_2^{Pauli-Villars}",
    "convention_class_pin": "FULL",
    "scheme_pin": "QES-island-construction",
    **{f"sha_{k}": v for k, v in INPUT_PINS.items()},
    # computed results enter the closure (sig_5 uniqueness)
    "R_island_computed": f"{R_island:.15e}",
    "S_island_computed": f"{S_island:.15e}",
    "lambda_island_computed": f"{lambda_island:.15e}",
    "test_ratio_computed": f"{test_ratio:.15e}",
    "sbulk_primary_computed": f"{sbulk_primary:.15e}",
    "T_acoustic_computed": f"{T_acoustic:.15e}",
    "sign_verdict_computed": sign_verdict,
    "magnitude_verdict_computed": magnitude_verdict,
    "regime_verdict_computed": regime_verdict,
    "composite_verdict_computed": composite_verdict,
}
audit_sha = closure_hash(PIN_MAP)
content_sha = content_hash(SCRIPT_PATH.read_text(encoding="utf-8"))

value_str = (
    f"R_island={R_island:.4f};"
    f"S_island={S_island:.4f};"
    f"A_quarter={A_quarter:.4f};"
    f"test_ratio={test_ratio:.4f};"
    f"lambda_exit={lambda_island:.4f};"
    f"R_edge_S110={R_edge_check:.4f};"
    f"R_full={R_island_full:.4f};"
    f"S_bulk_at_exit={sbulk_primary:.4f};"
    f"R_span={R_scan_min:.4f}-{R_scan_max:.4f};"
    f"T_acoustic={T_acoustic:.4f};"
    f"c_conical={c_conical:.4f}"
)

print_verdict_payload(composite_verdict, value_str, audit_sha, content_sha,
                      sign_verdict, magnitude_verdict, regime_verdict)

# Final summary for the agent
print()
print("RESULT SUMMARY")
print(f"  R_island (substrate-fixed boundary + bulk-EE, canonical) = {R_island:.6f}")
print(f"  S_island = Area(dI)/4 + S_bulk-EE                        = {S_island:.4f}")
print(f"  A/4 (Bekenstein-Hawking)   = {A_quarter:.4f}")
print(f"  test_ratio = |R_island-1|  = {test_ratio:.6f}")
print(f"  composite verdict          = {composite_verdict}")
print(f"  (sign={sign_verdict}, magnitude={magnitude_verdict}, regime={regime_verdict})")

sys.exit(0)
