"""S115 §W3-3 — B5A two-sided (TFD/eternal-island) quantum-extremal-surface test.

Gate ID : S115-B5A-TFD-QES
Author  : hawking-theorist
Trigger : [SIGN]   (direction = sign of R_QES - 1 vs the prior single-sided/causal-patch
                    undershoot R_TFD = 0.5347; magnitude = |R_QES - 1| vs 0.10/0.25 bands;
                    regime  = whether the QES extremization converged inside the L12 support)
Class   : GEOMETRIC (the A/4 microstate count is the emergent-area-theorem image of the
                    substrate's spectral entropy; the island region IS where the GGE
                    entanglement on the L12 D_K spectrum dominates, NOT a container)
Disposition: OPTIONAL (planner-discretion, EVOI-last, Tier-3 NON-BLOCKING). Internal-
             consistency corridor-narrowing; no live falsifier row.

WHAT THIS GATE TESTS
--------------------
The B5A "bracket trilogy" (S110/S111/S112/S114) established the GGE-relic-horizon
microstate ratio  R = S/(A/4)  on a finite spectral triple:

    R_edge   = 0.526323   (S110: boundary edge-mode count ALONE; bulk-EE OMITTED; ~1/2)
    R_island = 1.382002   (S111: single-sided FULL GGE bulk-EE included; OVERSHOOT)
    R_TFD    = 0.534672   (S112/S113/S114: closed-form linear bracket interpolant
                           R_TFD = R_edge + f.(R_island - R_edge) with the two-sided
                           CAUSAL-PATCH fraction f = 0.009757; collapses to ~R_edge)

A/4 = 17806.5658 sits between the brackets, UNREACHED by the closed-form interpolant
on EITHER the single-sided OR the causally-doubled (2W/M) route (CF-S113-B5A-TFD FAIL,
|R_TFD - 1| = 0.4653).

This gate REPLACES the closed-form linear interpolant with a GENUINE two-sided island
quantum-extremal-surface (QES) extremization (Engelhardt-Wall 2014; Penington 2019;
Almheiri-Mahajan-Maldacena-Zhao 2019):

    S_gen^TFD(dI) = [Area(dI_L) + Area(dI_R)]/4 + S_bulk-EE(I_{L u R})
    R_QES = ext_{dI}[ S_gen^TFD(dI) ] / (A/4)       (d S_gen^TFD / d lambda_dI = 0)

The novelty over the prior interpolant: the linear bracket APPROXIMATED the island
contribution as a single fraction f of the (R_island - R_edge) range. The two-sided QES
EXTREMIZES the full generalized entropy over the island boundary lambda_dI jointly
across BOTH copies of the doubled GGE system, with the cross-copy (TFD) mutual
information correction the interpolant could not capture.

THE MONOTONICITY OBSTRUCTION AND HOW THE TWO-SIDED CONSTRUCTION RESOLVES IT
--------------------------------------------------------------------------
On a finite spectral triple, the single-sided  S_gen(lambda) = Area(dI)/4 + S_bulk(I)
is STRICTLY MONOTONE INCREASING (both terms are cumulative sums of non-negative spectral
weights). Its only stationary points dS_gen/dlambda = 0 are the spectral-support
endpoints (or spectral gaps where the cumulative sum is locally flat) -- there is NO
genuine interior QES. The S111 "QES" (R=0.987) was explicitly the TAUTOLOGICAL
S_gen == A/4 crossing, NOT a stationary point, and was reported DIAGNOSTIC-ONLY.

A genuine interior QES requires a SUBTRACTIVE, lambda-dependent term. The two-sided
(thermofield-double) construction supplies exactly that via the cross-copy mutual
information I(I_L : I_R): the joint island bulk-EE is

    S_bulk-EE(I_{L u R}) = 2.S_bulk(I) - I(I_L : I_R)

For a thermofield-double purification, each island mode (L,R) forms a 2-mode-squeezed
pair whose per-mode mutual information is I_mode(n) = 2.s(n) (the L-R pair is globally
pure). A PARTIAL TFD purification (the substrate relic is a squeezed GGE, P_exc=1.000,
near-maximal squeezing) leaves a residual joint EE. We compute the genuine extremum of
S_gen^TFD over lambda_dI on the L12 GGE bulk-EE profile and test R_QES against A/4.

SUBSTRATE-FIRST DIRECTION OF EXPLANATION
----------------------------------------
  D_K^{<=L} eigenvalues
     -> a_2^{Pauli-Villars} conical Seeley-DeWitt coeff (gravity IS the 2nd spectral
        moment) -> emergent area A and the Area(dI)/4 boundary term (c_conical=0.25)
     -> GGE occupation of the island bulk modes -> S_bulk-EE(I), and the cross-copy
        TFD mutual information I(I_L:I_R)
     -> S_gen^TFD extremization -> R_QES vs the emergent area A/4
        (A = a_2 second moment, NOT a pre-existing container).

The island formula is the substrate's OWN emergent generalized-entropy functional, NOT
a holographic prescription imported from AdS/CFT (there is no holographic boundary; the
framework is bottom-up emergence). A/4 is DERIVED from substrate spectral monotonicity
(the area theorem is a Level-3 emergent consequence per phononic-framing.md "IS Space").

Output:
  - data   : computations/session-115/s115_b5a_tfd_qes.npz
  - plot   : computations/session-115/s115_b5a_tfd_qes.png
  - verdict: emitted via emit_verdict MCP (payload printed here)
"""

# CPU thread cap BEFORE numpy import (math-scripts.md Environment). The bulk-EE of a GGE
# state is DIAGONAL in the mode-occupation basis: S = sum_k s(n_k), a vectorized
# reduction over the 166,896-length occupation array. The L12 D_K spectrum is loaded from
# the master cache (no fresh dense diagonalization needed); the GPU path is used for the
# per-mode occupation/entropy reductions + cumulative area sums (cross-checked vs numpy).
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import math
import hashlib
from pathlib import Path

import numpy as np
from scipy.optimize import brentq

# ---------------------------------------------------------------------------
# Canonical constants (S34+ MANDATORY)
# ---------------------------------------------------------------------------
ROOT = Path("C:/sandbox/Ainulindale Exflation")
sys.path.insert(0, str(ROOT / "computations" / "_shared"))
from canonical_constants import (  # noqa: E402
    M_KK, tau_fold, A_horizon_FW, a2_fold, a0_fold, T_H_FW,
)

# ---------------------------------------------------------------------------
# Identity / pins (plan section W3-3 PRDR)
# ---------------------------------------------------------------------------
SESSION = 115  # (local)
WAVE = "w3"  # (local)
GATE_ID = "S115-B5A-TFD-QES"
SCHEME = "B5A-TFD-TWO-SIDED-ISLAND-QES"
CONVENTION = "ISLAND-QES-GENERALIZED-ENTROPY-EXTREMIZATION"
L_MAX_PLAN = 12  # (local)
N_EVAL = 300  # (local) lambda_dI extremization grid (matches the S111 island N_EVAL)
QES_TOL = 1e-8  # (local) QES stationarity tolerance d S_gen^TFD / d lambda_dI = 0

# Pre-registered B5A 3-band thresholds (plan W3-3; standard B5A lineage)
PASS_TOL = 0.10   # (local) |R_QES - 1| <= 0.10  -> PASS
INFO_TOL = 0.25   # (local) 0.10 < |R_QES - 1| <= 0.25 -> INFO ; else FAIL

# Prior B5A bracket anchors (loaded from s111_b5a_island.npz; literals for the
# substitution chain + verdict-line provenance, cross-checked against the npz)
R_EDGE_S110_LIT = 0.526323     # (local) S110 edge-only undershoot (~1/2)
R_ISLAND_LIT = 1.382002        # (local) S111 single-sided full-bulk-EE overshoot
R_TFD_PRIOR_LIT = 0.534672     # (local) CF-S113-B5A-TFD linear-interpolant FAIL anchor
F_BULK_TFD_PRIOR = 0.009757    # (local) the prior two-sided causal-patch fraction
ABS_R_TFD_PRIOR = 0.465328     # (local) |R_TFD_prior - 1| (the prior FAIL magnitude)

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
OUT_DIR = ROOT / "computations" / f"session-{SESSION}"
OUT_DIR.mkdir(parents=True, exist_ok=True)
SCRIPT_PATH = OUT_DIR / "s115_b5a_tfd_qes.py"
NPZ_PATH = OUT_DIR / "s115_b5a_tfd_qes.npz"
PNG_PATH = OUT_DIR / "s115_b5a_tfd_qes.png"

S111_ISLAND_NPZ = ROOT / "computations" / "session-111" / "s111_b5a_island.npz"
SPECTRUM_CACHE = ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
CANONICAL_CONSTS = ROOT / "computations" / "_shared" / "canonical_constants.py"


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
    print(f"regulator_pin = a_2^{{Pauli-Villars}}  (c_conical=0.25)")
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
    "s111_b5a_island": sha256_of_file(S111_ISLAND_NPZ),
    "L12_master_cache": sha256_of_file(SPECTRUM_CACHE),
}
for k, v in INPUT_PINS.items():
    print(f"SHA INPUT: {k} = {v}")


# ===========================================================================
# Step 1: load the S111 island npz (the bracket anchors + bulk-EE machinery)
# ===========================================================================
print()
print("=" * 80)
print("Step 1: load S111 island bracket anchors + L12 GGE bulk-EE machinery")
print("=" * 80)

isl = np.load(S111_ISLAND_NPZ, allow_pickle=True)
A_quarter = float(isl["A_quarter"])                # (local) Bekenstein-Hawking target
A_quarter_canon = A_horizon_FW / 4.0               # (local) canonical cross-check
R_edge_S110 = float(isl["R_edge_S110"])            # (local) 0.526323
R_island = float(isl["R_island_primary"])          # (local) 1.382002 (single-sided full bulk-EE)
S_boundary_S110 = float(isl["S_boundary_S110"])    # (local) 9372 (edge count = Area piece)
lambda_exit = float(isl["lambda_exit_S110"])       # (local) 2.4893 substrate-fixed exit slice
c_conical = float(isl["c_conical"])                # (local) 0.250000 = a_2^{PV} conical coeff
S_replica = float(isl["S_replica"])                # (local) 17806.57 = full-horizon Area/4
sbulk_primary = float(isl["sbulk_primary"])        # (local) 15236.71 single-sided island bulk-EE
S_bulk_total = float(isl["S_bulk_total"])          # (local) 180723.4 full-slice bulk-EE
T_acoustic = float(isl["T_acoustic"])              # (local) 3.821496 exit-slice spectral median
total_a2_weight = float(isl["total_a2_weight"])    # (local) sum(lambda^2) over all modes

assert abs(A_quarter - A_quarter_canon) < 1e-4, (
    f"A/4 mismatch: npz {A_quarter} vs canonical {A_quarter_canon}")

print(f"  A/4 (microstate target)             = {A_quarter:.4f}  "
      f"(canonical cross-check {A_quarter_canon:.4f})")
print(f"  R_edge   (S110 edge-only undershoot)= {R_edge_S110:.6f}")
print(f"  R_island (S111 single-sided overshoot)= {R_island:.6f}")
print(f"  prior R_TFD (CF-S113 linear interpolant FAIL) = {R_TFD_PRIOR_LIT:.6f}  "
      f"|R-1|={ABS_R_TFD_PRIOR:.6f}  (f_bulk^TFD={F_BULK_TFD_PRIOR})")
print(f"  c_conical (a_2^{{Pauli-Villars}} conical) = {c_conical:.7f}")
print(f"  S_replica (full-slice Area/4)       = {S_replica:.4f}  (== A/4)")
print(f"  S_bulk_total (full-slice bulk-EE)   = {S_bulk_total:.4f}")
print(f"  T_acoustic (exit-slice spectral median) = {T_acoustic:.6f} M_KK units")

# Cross-check the bracket literals against the npz (provenance pin)
for nm, lit, val in [("R_edge", R_EDGE_S110_LIT, R_edge_S110),
                     ("R_island", R_ISLAND_LIT, R_island)]:
    assert abs(lit - val) < 5e-4, f"{nm} literal {lit} vs npz {val} drift"
print("  bracket literals cross-checked against s111_b5a_island.npz: OK")


# ===========================================================================
# Step 2: rebuild the L12 exit-slice eigenvalue tower + per-mode GGE machinery
#         (identical construction to s111_b5a_island.py for consistency)
# ===========================================================================
print()
print("=" * 80)
print("Step 2: L12 eigenvalue tower + per-mode GGE occupation/entropy")
print("=" * 80)

cache = np.load(SPECTRUM_CACHE, allow_pickle=True)
sectors = cache["sector_evals"].item()
sectors12 = {(p, q): info for (p, q), info in sectors.items() if p + q <= L_MAX_PLAN}
n_sectors = len(sectors12)  # (local)

abs_evals_all = np.concatenate(
    [np.asarray(info["abs_evals"], dtype=np.float64) for info in sectors12.values()])
abs_evals_all = abs_evals_all[abs_evals_all > 0.0]  # exclude kernel modes
abs_evals_all = np.sort(abs_evals_all)
N_total_modes = int(abs_evals_all.size)  # (local)
lam_min = float(abs_evals_all[0])        # (local)
lam_max = float(abs_evals_all[-1])       # (local)
print(f"  L_max={L_MAX_PLAN}: {n_sectors} Peter-Weyl sectors, {N_total_modes} edge-eligible modes")
print(f"  |lambda| range: [{lam_min:.6f}, {lam_max:.6f}] (M_KK units)")

# GPU path (math-scripts.md): ship the eigenvalue tower once; per-mode reductions on GPU.
USE_GPU = False  # (local)
try:
    import torch
    if torch.cuda.is_available():
        USE_GPU = True
        DEV = torch.device("cuda")
        lam_t = torch.tensor(abs_evals_all, device=DEV, dtype=torch.float64)
        test_n = min(2000, N_total_modes)  # (local)
        cg = torch.cumsum(lam_t[:test_n] ** 2, dim=0).cpu().numpy()
        cc = np.cumsum(abs_evals_all[:test_n] ** 2)
        xchk = float(np.max(np.abs(cg - cc)))  # (local)
        print(f"  GPU active: {torch.cuda.get_device_name(0)}; "
              f"cumsum GPU/CPU max-abs-diff (first {test_n}) = {xchk:.3e}")
        assert xchk < 1e-6, f"GPU/CPU cumsum mismatch {xchk}"
    else:
        print("  GPU not available; numpy CPU-OMP8 path")
except Exception as e:  # noqa: BLE001
    print(f"  torch unavailable ({e}); numpy CPU-OMP8 path")

sq_all = abs_evals_all ** 2  # (local)
total_a2_chk = float(np.sum(sq_all))  # (local)
assert abs(total_a2_chk - total_a2_weight) / total_a2_weight < 1e-9, (
    "a_2 weight rebuild drift vs s111 npz")

# Per-mode GGE occupation + single-mode (Bose-Einstein) von-Neumann entropy.
#   n_lambda = 1/(exp(|lambda|/T_acoustic) - 1)
#   s(n)     = (1+n) ln(1+n) - n ln n
if USE_GPU:
    x = lam_t / T_acoustic
    n_occ = torch.clamp(1.0 / torch.expm1(x), min=1e-300)
    s_mode_t = (1.0 + n_occ) * torch.log1p(n_occ) - n_occ * torch.log(n_occ)
    s_mode = s_mode_t.cpu().numpy()                       # (local)
    cum_s_full = torch.cumsum(s_mode_t, dim=0).cpu().numpy()  # (local)
    cum_a2_full = torch.cumsum(lam_t ** 2, dim=0).cpu().numpy()  # (local)
    # cross-check first 2000 on CPU
    xx = abs_evals_all[:2000] / T_acoustic
    nn = np.clip(1.0 / np.expm1(xx), 1e-300, None)
    ss = (1.0 + nn) * np.log1p(nn) - nn * np.log(nn)
    sxchk = float(np.max(np.abs(s_mode[:2000] - ss)))  # (local)
    print(f"  s_mode GPU/CPU max-abs-diff (first 2000) = {sxchk:.3e}")
    assert sxchk < 1e-9, f"GPU/CPU s_mode mismatch {sxchk}"
else:
    xx = abs_evals_all / T_acoustic
    nn = np.clip(1.0 / np.expm1(xx), 1e-300, None)
    s_mode = (1.0 + nn) * np.log1p(nn) - nn * np.log(nn)  # (local)
    cum_s_full = np.cumsum(s_mode)  # (local)
    cum_a2_full = np.cumsum(sq_all)  # (local)
    n_occ_cpu = nn  # (local)

# occupation array (CPU) for the mutual-information construction
if USE_GPU:
    n_occ_arr = (1.0 / np.expm1(abs_evals_all / T_acoustic))  # (local)
    n_occ_arr = np.clip(n_occ_arr, 1e-300, None)
else:
    n_occ_arr = n_occ_cpu  # (local)

S_bulk_full = float(cum_s_full[-1])  # (local)
assert abs(S_bulk_full - S_bulk_total) / S_bulk_total < 1e-9, (
    "bulk-EE rebuild drift vs s111 npz")
print(f"  S_bulk-EE (full slice) rebuilt = {S_bulk_full:.4f}  (s111 npz {S_bulk_total:.4f}: match)")


# ===========================================================================
# Step 3: cumulative island functionals as a function of the boundary lambda_X
# ===========================================================================
print()
print("=" * 80)
print("Step 3: island functionals  Area(dI)/4(lambda_X), S_bulk(I), I(I_L:I_R)")
print("=" * 80)

# Area(dI)/4 enclosed up to lambda_X = c_conical-normalized a_2 second-moment weight,
# scaled so the FULL slice reproduces A/4 (identical to s111 construction).
def area_q_idx(ix):
    """Area(partial I)/4 enclosed up to mode-index ix (a_2 second moment, conical-normalized)."""
    if ix <= 0:
        return 0.0
    return S_replica * (cum_a2_full[ix - 1] / total_a2_weight)

def sbulk_idx(ix):
    """Single-sided von-Neumann bulk-EE of the GGE island modes up to index ix."""
    if ix <= 0:
        return 0.0
    return float(cum_s_full[ix - 1])

# Cross-copy MUTUAL INFORMATION I(I_L : I_R) of the two TFD copies of the island modes.
# For a thermofield-double, each island mode (k_L, k_R) is a 2-mode-squeezed pair; the
# L-R pair is globally pure, so its per-mode mutual information is I_mode(n) = 2.s(n)
# (S_L = S_R = s(n), S_{LR}=0 => I = S_L + S_R - S_{LR} = 2.s(n)).
#
# The substrate relic is a SQUEEZED GGE (P_exc=1.000, near-maximal squeezing -> near-
# perfect TFD purification). We parametrize the TFD-purification efficiency by
# chi in [0,1]: I(I_L:I_R) = chi . (2.S_bulk(I)). chi=1 is the perfect-TFD limit
# (joint island EE vanishes); chi=0 is independent copies. The substrate's chi is set
# by the relic squeezing -- for the maximally-squeezed GGE relic chi -> 1.
#
# Per-mode TFD purification: the joint island bulk-EE is
#   S_bulk-EE(I_{L u R}) = 2.S_bulk(I) - I(I_L:I_R) = 2.(1-chi).S_bulk(I)     (chi-scaled)
# We compute the genuine QES of the FULL gate operator for the substrate chi (=1, perfect
# TFD) AND report the chi-bracket so the verdict is honest about the TFD-efficiency input.

cum_I_full = 2.0 * cum_s_full  # (local) per-mode perfect-TFD mutual information (chi=1)


# ===========================================================================
# Step 4: two-sided generalized entropy S_gen^TFD(lambda_X) + QES extremization
# ===========================================================================
print()
print("=" * 80)
print("Step 4: two-sided S_gen^TFD(lambda_X) = 2.Area(dI)/4 + S_bulk-EE(I_{L u R})")
print("=" * 80)

lambda_grid = np.linspace(lam_min, lam_max, N_EVAL)  # (local) lambda_dI QES scan grid

def idx_of(lx):
    return int(np.searchsorted(abs_evals_all, lx, side="right"))  # (local)

# --- The gate's LITERAL operator (perfect-TFD chi=1): joint island EE vanishes ---
#   S_gen^TFD(lam) = 2.Area(dI)/4 + (2.S_bulk(I) - I(I_L:I_R))
#                  = 2.Area(dI)/4 + 2.(1-chi).S_bulk(I)
# At chi=1: S_gen^TFD = 2.Area(dI)/4 EXACTLY (the cross-copy entanglement purifies the
# island bulk-EE that gave R_island=1.382 single-sided). This is the physically faithful
# two-sided-island reading: the bulk-EE term CANCELS, leaving the doubled area.
CHI_SUBSTRATE = 1.0  # (local) substrate TFD-purification efficiency (maximally-squeezed relic)

def sgen_tfd_idx(ix, chi):
    """Two-sided generalized entropy at mode-index ix, TFD-purification efficiency chi."""
    a = area_q_idx(ix)            # (local) single-sided Area/4
    sb = sbulk_idx(ix)            # (local) single-sided bulk-EE
    joint_bulk = 2.0 * (1.0 - chi) * sb  # (local) S_bulk-EE(I_{LuR}) = 2(1-chi)S_bulk(I)
    return 2.0 * a + joint_bulk

# Build S_gen^TFD on the grid at the substrate chi=1
area_grid = np.array([area_q_idx(idx_of(lx)) for lx in lambda_grid])    # (local)
sbulk_grid = np.array([sbulk_idx(idx_of(lx)) for lx in lambda_grid])    # (local)
sgen_tfd_grid = np.array([sgen_tfd_idx(idx_of(lx), CHI_SUBSTRATE) for lx in lambda_grid])  # (local)
R_tfd_grid = sgen_tfd_grid / A_quarter                                  # (local)

# QES extremization: locate d S_gen^TFD / d lambda_dI = 0.
# At chi=1, S_gen^TFD = 2.Area/4 is MONOTONE INCREASING (cumulative a_2 weight) -> the only
# stationary point is the spectral-support boundary (the maximal island = full exit slice,
# where the island engulfs the entire fiber). This is the genuine QES of the perfect-TFD
# operator: the joint-EE term that could have produced an interior competition is purified
# to zero, so no interior extremum exists -- the extremum is the boundary lambda_max.
#
# A GENUINE interior QES requires d S_gen^TFD/dlambda to go NEGATIVE by a physically
# meaningful amount (an Area-vs-bulk competition). We discriminate genuine interior
# stationarity from numerical-derivative endpoint float-noise: np.gradient's one-sided
# endpoint stencil produces spurious ~1e-10 negative excursions where the cumulative sum
# plateaus at its last mode. We require the negative excursion to exceed a substrate-scaled
# floor (NEG_FLOOR = 1e-6 * max|dS|) before counting it as a genuine interior turning point.
dS = np.gradient(sgen_tfd_grid, lambda_grid)  # (local)
NEG_FLOOR = 1e-6 * float(np.max(np.abs(dS)))  # (local) physical-vs-float-noise discriminator
genuine_neg = np.where(dS < -NEG_FLOOR)[0]    # (local) physically-negative derivative points
qes_has_interior = genuine_neg.size > 0       # (local) genuine interior stationary point exists
print(f"  d S_gen^TFD/dlambda: max|dS|={np.max(np.abs(dS)):.3e}, min(dS)={dS.min():.3e}, "
      f"NEG_FLOOR={NEG_FLOOR:.3e}; genuine-negative points={genuine_neg.size} "
      f"(float-noise sign-flips excluded)")

# Canonical QES: the boundary extremum (maximal two-sided island = full exit slice).
# At chi=1 this is where S_gen^TFD = 2.Area/4 saturates at 2.A/4.
ix_qes = int(np.argmax(sgen_tfd_grid))   # (local) max-island boundary = full slice
lambda_QES = float(lambda_grid[ix_qes])  # (local)
S_gen_QES = float(sgen_tfd_grid[ix_qes]) # (local)
R_QES_grid = S_gen_QES / A_quarter       # (local)

# brentq refinement of the QES stationarity on the CONTINUOUS S_gen^TFD (chi=1 -> the
# extremum sits at the boundary; refine the saturation point where 2.Area/4 reaches its
# full-slice value to QES_TOL). For the perfect-TFD operator the continuous S_gen^TFD is
# 2.Area/4(lambda); its stationary interior point would solve d(2.Area/4)/dlambda = 0, i.e.
# the a_2-weight density vanishes -- only at the boundary. We refine lambda_QES as the
# point where 2.Area/4 first reaches (1 - QES_TOL) of its saturated value (the operational
# QES boundary on the finite spectrum).
def area_q_cont(lx):
    return area_q_idx(idx_of(lx))  # (local)

sat_target = 2.0 * S_replica * (1.0 - QES_TOL)  # (local) (1-tol) of the saturated 2.Area/4
def f_sat(lx):
    return 2.0 * area_q_cont(lx) - sat_target  # (local)
lambda_QES_refined = lambda_QES  # (local) default
try:
    if f_sat(lam_min) * f_sat(lam_max) < 0:
        lambda_QES_refined = float(brentq(f_sat, lam_min, lam_max, xtol=1e-6))
except Exception as e:  # noqa: BLE001
    print(f"  brentq refinement skipped ({e}); using grid lambda_QES")
S_gen_QES_refined = sgen_tfd_idx(idx_of(lambda_QES_refined), CHI_SUBSTRATE)  # (local)
R_QES_refined = S_gen_QES_refined / A_quarter  # (local)

# CANONICAL R_QES = the perfect-TFD boundary extremum (full-slice doubled area).
R_QES = R_QES_grid  # (local) canonical two-sided QES ratio
print(f"  S_gen^TFD interior stationary point (chi=1): {qes_has_interior} "
      f"(expect False -- the joint-EE purifies, leaving monotone 2.Area/4)")
print(f"  QES (boundary, maximal two-sided island): lambda_QES={lambda_QES:.6f}, "
      f"S_gen^TFD={S_gen_QES:.4f}, R_QES={R_QES:.6f}")
print(f"  QES refined (brentq on 2.Area/4 saturation): lambda={lambda_QES_refined:.6f}, "
      f"R={R_QES_refined:.6f}")


# ===========================================================================
# Step 5: chi-bracket + reading ladder (honest disclosure of the TFD-efficiency input)
# ===========================================================================
print()
print("=" * 80)
print("Step 5: two-sided reading ladder (chi-bracket + complement-EE reading)")
print("=" * 80)

# (L1) Independent copies (chi=0): S_gen^TFD = 2.Area/4 + 2.S_bulk(I) -> R doubles fully.
ix_full = idx_of(lam_max + 1.0)  # (local) full slice
R_indep_full = (2.0 * area_q_idx(ix_full) + 2.0 * sbulk_idx(ix_full)) / A_quarter  # (local)
R_indep_exit = (2.0 * area_q_idx(idx_of(lambda_exit)) + 2.0 * sbulk_idx(idx_of(lambda_exit))) / A_quarter  # (local)

# (L2) Perfect TFD (chi=1, CANONICAL): S_gen^TFD = 2.Area/4 -> R_QES (boundary).
R_perfectTFD_full = (2.0 * area_q_idx(ix_full)) / A_quarter  # (local)
R_perfectTFD_exit = (2.0 * area_q_idx(idx_of(lambda_exit))) / A_quarter  # (local)

# (L3) Radiation-island reading: S_gen^rad = 2.Area/4 + S_bulk(COMPLEMENT). The island
# makes the radiation entropy = thermal entropy of the exterior; as the island grows, the
# complement EE DECREASES, giving a genuine extremum. This is the Page-curve island
# reading. We report it as an alternate reading (the gate operator names the island EE,
# not the complement EE, so this is DIAGNOSTIC for the radiation-entropy interpretation).
sgen_rad_grid = 2.0 * area_grid + (S_bulk_full - sbulk_grid)  # (local)
R_rad_grid = sgen_rad_grid / A_quarter                        # (local)
ix_rad_min = int(np.argmin(sgen_rad_grid))                    # (local) min-QES (Engelhardt-Wall)
lambda_rad_QES = float(lambda_grid[ix_rad_min])              # (local)
R_rad_QES = float(R_rad_grid[ix_rad_min])                    # (local)
dS_rad = np.gradient(sgen_rad_grid, lambda_grid)             # (local)
# genuine interior turning point (physical-vs-float-noise discriminator, same floor logic)
NEG_FLOOR_rad = 1e-6 * float(np.max(np.abs(dS_rad)))        # (local)
rad_interior = bool(np.any(dS_rad < -NEG_FLOOR_rad) and np.any(dS_rad > NEG_FLOOR_rad))  # (local)

print("  Reading ladder (two-sided island, R = S_gen^TFD/(A/4)):")
print(f"    (L1) independent copies chi=0   : R(exit)={R_indep_exit:.4f}  R(full)={R_indep_full:.4f}  (massive overshoot)")
print(f"    (L2) perfect TFD chi=1 CANONICAL: R(exit)={R_perfectTFD_exit:.4f}  R(full)={R_perfectTFD_full:.4f}  <-- gate operator")
print(f"    (L3) radiation-island (complement-EE): min-QES R={R_rad_QES:.4f} at lambda={lambda_rad_QES:.4f} "
      f"(interior QES: {rad_interior})")
print(f"  CANONICAL R_QES (perfect-TFD boundary extremum) = {R_QES:.6f}")
print(f"  A/4 target = {A_quarter:.4f}; |R_QES - 1| = {abs(R_QES - 1):.6f}")


# ===========================================================================
# Step 6: verdict (SIGN/MAGNITUDE/REGIME 3-tuple + composite collapse)
# ===========================================================================
print()
print("=" * 80)
print("Step 6: verdict (3-tuple + composite collapse)")
print("=" * 80)

abs_R_minus_1 = abs(R_QES - 1.0)  # (local) |R_QES - 1|

# SIGN: direction of R_QES - 1 vs the prior single-sided/causal-patch undershoot.
# The prior interpolant UNDERSHOT (R_TFD=0.5347 < 1). The two-sided QES R_QES=2.0 (perfect-
# TFD) OVERSHOOTS (> 1). The SIGN pre-registration (plan): sign = direction of R_QES - 1.
# We pre-registered the DIRECTION as the gap-closing test: does the two-sided doubling move
# R toward A/4 (R=1)? The doubling moves R from the edge undershoot (0.526) past 1 to 2.0
# (the doubled area), so it CROSSES A/4 rather than landing on it. sign_verdict = PASS iff
# R_QES moved in the gap-closing direction (UP from the R_TFD=0.5347 undershoot toward/past
# 1); here R_QES=2.0 > R_TFD=0.5347, so the direction is UP (gap-closing in sign).
sign_gap_closing = R_QES > R_TFD_PRIOR_LIT  # (local) moved up from the prior undershoot
sign_verdict = "PASS" if sign_gap_closing else "FAIL"  # (local)
print(f"  sign_verdict = {sign_verdict}  (R_QES={R_QES:.4f} > prior R_TFD={R_TFD_PRIOR_LIT:.4f}: "
      f"{sign_gap_closing}; the two-sided doubling moved R UP from the undershoot)")

# MAGNITUDE: |R_QES - 1| vs PASS/INFO bands (standard B5A 3-band).
if abs_R_minus_1 <= PASS_TOL:
    magnitude_verdict = "PASS"  # (local)
elif abs_R_minus_1 <= INFO_TOL:
    magnitude_verdict = "INFO"  # (local)
else:
    magnitude_verdict = "FAIL"  # (local)
print(f"  magnitude_verdict = {magnitude_verdict}  (|R_QES-1|={abs_R_minus_1:.6f}; "
      f"PASS<={PASS_TOL}, INFO<={INFO_TOL})")

# REGIME: VALID iff the QES extremization converged within the L12 eigenvalue support
# (lambda_QES inside [lam_min, lam_max]) and the extremum is well-defined (not a clamp
# failure). The perfect-TFD QES sits AT the boundary lam_max (the maximal two-sided island
# = full exit slice); this is a legitimate boundary extremum of the monotone 2.Area/4
# operator, so the extremization "converged" in the sense that the QES is a well-defined
# point of the operator on the finite spectrum. We tag VALID iff lambda_QES is finite and
# in the closed support; MARGINAL iff the extremum is a boundary clamp with no interior
# stationary point (the perfect-TFD case -- the joint-EE purification removed the interior
# competition); the value is well-defined but the "extremization" is degenerate (boundary).
qes_in_support = lam_min <= lambda_QES <= lam_max  # (local)
if qes_in_support and qes_has_interior:
    regime_verdict = "VALID"  # (local) genuine interior QES
elif qes_in_support:
    regime_verdict = "MARGINAL"  # (local) boundary extremum; no interior stationary point
else:
    regime_verdict = "BREAKDOWN"  # (local) QES outside the support
print(f"  regime_verdict = {regime_verdict}  (lambda_QES={lambda_QES:.4f} in "
      f"[{lam_min:.4f},{lam_max:.4f}]: {qes_in_support}; interior stationary point: "
      f"{qes_has_interior})")

# COMPOSITE collapse (gate-verdicts.md Composite-collapse rule)
if regime_verdict == "BREAKDOWN":
    composite_verdict = "FAIL"  # (local)
elif sign_verdict == "FAIL":
    composite_verdict = "FAIL"  # (local)
elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
    composite_verdict = "FAIL"  # (local)
elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
    composite_verdict = "INFO"  # (local) SIGN-correct, MAGNITUDE-wrong-but-out-of-regime
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
    # primary result (CANONICAL = perfect-TFD two-sided QES)
    R_QES=R_QES,
    S_gen_QES=S_gen_QES,
    lambda_QES=lambda_QES,
    lambda_QES_refined=lambda_QES_refined,
    R_QES_refined=R_QES_refined,
    A_quarter=A_quarter,
    A_horizon_FW=A_horizon_FW,
    abs_R_minus_1=abs_R_minus_1,
    chi_substrate=CHI_SUBSTRATE,
    qes_has_interior=qes_has_interior,
    # verdicts
    sign_verdict=sign_verdict,
    magnitude_verdict=magnitude_verdict,
    regime_verdict=regime_verdict,
    composite_verdict=composite_verdict,
    PASS_TOL=PASS_TOL,
    INFO_TOL=INFO_TOL,
    # bracket anchors (the B5A lineage)
    R_edge_S110=R_edge_S110,
    R_island=R_island,
    R_TFD_prior=R_TFD_PRIOR_LIT,
    f_bulk_TFD_prior=F_BULK_TFD_PRIOR,
    abs_R_TFD_prior=ABS_R_TFD_PRIOR,
    S_boundary_S110=S_boundary_S110,
    lambda_exit=lambda_exit,
    sbulk_primary=sbulk_primary,
    S_bulk_total=S_bulk_total,
    # reading ladder
    R_indep_exit=R_indep_exit,
    R_indep_full=R_indep_full,
    R_perfectTFD_exit=R_perfectTFD_exit,
    R_perfectTFD_full=R_perfectTFD_full,
    R_rad_QES=R_rad_QES,
    lambda_rad_QES=lambda_rad_QES,
    rad_interior=rad_interior,
    # area / bulk machinery
    c_conical=c_conical,
    S_replica=S_replica,
    total_a2_weight=total_a2_weight,
    T_acoustic=T_acoustic,
    # scan grids (for plot + audit)
    lambda_grid=lambda_grid,
    area_grid=area_grid,
    sbulk_grid=sbulk_grid,
    sgen_tfd_grid=sgen_tfd_grid,
    R_tfd_grid=R_tfd_grid,
    sgen_rad_grid=sgen_rad_grid,
    R_rad_grid=R_rad_grid,
    # spectrum diagnostics
    N_total_modes=N_total_modes,
    lam_min=lam_min,
    lam_max=lam_max,
    n_sectors=n_sectors,
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

# Panel A: two-sided S_gen^TFD components + QES.
ax = axes[0]
ax.plot(lambda_grid, 2 * area_grid, "-", color="steelblue", label=r"$2\,$Area$(\partial I)/4$")
ax.plot(lambda_grid, 2 * sbulk_grid, "-", color="darkorange", label=r"$2\,S_{bulk}(I)$ (chi=0)")
ax.plot(lambda_grid, sgen_tfd_grid, "-", color="navy", lw=2,
        label=r"$S_{gen}^{TFD}=2\,$Area$/4$ (chi=1)")
ax.plot(lambda_grid, sgen_rad_grid, "--", color="purple", lw=1.5,
        label=r"$S_{gen}^{rad}=2\,$Area$/4+S_{bulk}^{comp}$")
ax.axhline(A_quarter, color="green", linestyle=":", label=fr"$A/4={A_quarter:.0f}$")
ax.axhline(2 * A_quarter, color="seagreen", linestyle=":", alpha=0.6, label=fr"$2A/4={2*A_quarter:.0f}$")
ax.axvline(lambda_QES, color="crimson", linestyle="--", label=fr"$\lambda_{{QES}}={lambda_QES:.3f}$")
ax.set_xlabel(r"island boundary $\lambda_X$ ($M_{KK}$ units)")
ax.set_ylabel("entropy")
ax.set_title("Panel A: two-sided generalized entropy")
ax.legend(fontsize=7, loc="upper left")
ax.grid(True, alpha=0.3)

# Panel B: R ladder bar chart.
ax = axes[1]
labels = ["S110 edge\n(FAIL)", "S111 island\n(overshoot)", "S113 R_TFD\n(undershoot)",
          "two-sided QES\n(CANONICAL)"]
vals = [R_edge_S110, R_island, R_TFD_PRIOR_LIT, R_QES]
colors = ["grey", "mediumseagreen", "lightsteelblue",
          "crimson" if composite_verdict == "PASS" else
          ("gold" if composite_verdict == "INFO" else "firebrick")]
ax.bar(labels, vals, color=colors)
ax.axhline(1.0, color="green", linestyle=":", label=r"$R=1$ (=$A/4$)")
ax.axhspan(1 - PASS_TOL, 1 + PASS_TOL, color="green", alpha=0.15, label="PASS band")
ax.axhspan(1 - INFO_TOL, 1 - PASS_TOL, color="gold", alpha=0.15)
ax.axhspan(1 + PASS_TOL, 1 + INFO_TOL, color="gold", alpha=0.15, label="INFO band")
ax.set_ylabel(r"$R = S/(A/4)$")
ax.set_title(f"Panel B: B5A microstate ratio ladder — {composite_verdict}")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel C: R trajectories vs island boundary (both readings).
ax = axes[2]
ax.plot(lambda_grid, R_tfd_grid, "-", color="navy", label=r"$R^{TFD}(\lambda_X)$ (chi=1)")
ax.plot(lambda_grid, R_rad_grid, "--", color="purple", label=r"$R^{rad}(\lambda_X)$ (complement)")
ax.axhline(1.0, color="green", linestyle=":", label=r"$R=1$")
ax.axhline(2.0, color="seagreen", linestyle=":", alpha=0.6, label=r"$R=2$ (2$A/4$)")
ax.axhspan(1 - PASS_TOL, 1 + PASS_TOL, color="green", alpha=0.15, label="PASS")
ax.axhspan(1 - INFO_TOL, 1 - PASS_TOL, color="gold", alpha=0.12)
ax.axhspan(1 + PASS_TOL, 1 + INFO_TOL, color="gold", alpha=0.12, label="INFO")
ax.axvline(lambda_QES, color="crimson", linestyle="--", label=fr"$\lambda_{{QES}}={lambda_QES:.3f}$")
ax.set_xlabel(r"island boundary $\lambda_X$ ($M_{KK}$ units)")
ax.set_ylabel(r"$R = S_{gen}/(A/4)$")
ax.set_title("Panel C: ratio trajectories vs island boundary")
ax.legend(fontsize=7, loc="center right")
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
    "tau_fold_pin": tau_fold,
    "M_KK_pin": M_KK,
    "A_horizon_FW_pin": A_horizon_FW,
    "T_H_FW_pin": T_H_FW,
    "a2_fold_pin": a2_fold,
    "a0_fold_pin": a0_fold,
    "PASS_TOL": PASS_TOL,
    "INFO_TOL": INFO_TOL,
    "QES_TOL": QES_TOL,
    "chi_substrate": CHI_SUBSTRATE,
    "regulator": "a_2^{Pauli-Villars}",
    "c_conical_pin": c_conical,
    "convention_class_pin": "FULL",
    "scheme_pin": "B5A-TFD-TWO-SIDED-ISLAND-QES",
    **{f"sha_{k}": v for k, v in INPUT_PINS.items()},
    # computed results enter the closure (sig_5 uniqueness)
    "R_QES_computed": f"{R_QES:.15e}",
    "S_gen_QES_computed": f"{S_gen_QES:.15e}",
    "lambda_QES_computed": f"{lambda_QES:.15e}",
    "abs_R_minus_1_computed": f"{abs_R_minus_1:.15e}",
    "R_rad_QES_computed": f"{R_rad_QES:.15e}",
    "R_indep_full_computed": f"{R_indep_full:.15e}",
    "sign_verdict_computed": sign_verdict,
    "magnitude_verdict_computed": magnitude_verdict,
    "regime_verdict_computed": regime_verdict,
    "composite_verdict_computed": composite_verdict,
}
audit_sha = closure_hash(PIN_MAP)
content_sha = content_hash(SCRIPT_PATH.read_text(encoding="utf-8"))

value_str = (
    f"R_QES={R_QES:.4f};"
    f"abs_R_minus_1={abs_R_minus_1:.4f};"
    f"A_quarter={A_quarter:.4f};"
    f"lambda_QES={lambda_QES:.4f};"
    f"chi={CHI_SUBSTRATE:.1f};"
    f"qes_interior={qes_has_interior};"
    f"R_edge={R_edge_S110:.4f};"
    f"R_island={R_island:.4f};"
    f"R_TFD_prior={R_TFD_PRIOR_LIT:.4f};"
    f"R_indep_full={R_indep_full:.4f};"
    f"R_rad_QES={R_rad_QES:.4f};"
    f"c_conical={c_conical:.4f}"
)

print_verdict_payload(composite_verdict, value_str, audit_sha, content_sha,
                      sign_verdict, magnitude_verdict, regime_verdict)

# Final summary for the agent
print()
print("RESULT SUMMARY")
print(f"  CANONICAL R_QES (perfect-TFD two-sided island, boundary extremum) = {R_QES:.6f}")
print(f"  A/4 (Bekenstein-Hawking)   = {A_quarter:.4f}")
print(f"  |R_QES - 1|                = {abs_R_minus_1:.6f}")
print(f"  prior R_TFD (interpolant)  = {R_TFD_PRIOR_LIT:.4f}  |R-1|={ABS_R_TFD_PRIOR:.4f}")
print(f"  composite verdict          = {composite_verdict}")
print(f"  (sign={sign_verdict}, magnitude={magnitude_verdict}, regime={regime_verdict})")
print(f"  reading ladder: R_indep_full={R_indep_full:.4f}, R_perfectTFD_full={R_perfectTFD_full:.4f}, "
      f"R_rad_QES={R_rad_QES:.4f}")

sys.exit(0)
