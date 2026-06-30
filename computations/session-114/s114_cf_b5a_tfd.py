"""S114 §W4-2 — White-hole exit-slice microstate count: TWO-SIDED THERMOFIELD-DOUBLE
(TFD) island construction with a DERIVED two-sided causally-accessible bulk-EE fraction.

Gate ID : CF-S113-B5A-TFD
Author  : hawking-theorist
Trigger : [SIGN]   (directional pre-registration: dR_TFD/df_bulk = R_island - R_edge
                    > 0; the two-sided TFD patch raises f_bulk above the single-sided
                    0.00396, pushing R_TFD up from the edge undershoot toward A/4)
Class   : GEOMETRIC (the white-hole exit slice + its TFD purification partner IS the
                    spectral-triple structure (A_K^{<=12}, H_K^{<=12}, D_K^{<=12}) on
                    the exit configuration; the boundary entropy and bulk-EE are
                    spectral functionals of the D_K^{<=12} eigenvalue spectrum, NOT
                    fields on a pre-existing container)

WHAT THIS GATE TESTS
--------------------
The surviving white-hole microstate route after the S110/S111/S112 bracket chain:

  * S110-CF-B5A-MICROSTATE (FAIL): edge-only S_boundary = 9372 => R_edge = 0.5263
    (boundary term ALONE, bulk-EE OMITTED -- the lower bracket, factor-1.9 undercount).
  * S111-CF-B5A-ISLAND (FAIL): full island Area(dI)/4 + S_bulk-EE(I) at lambda_exit
    => R_island = 1.382 (FULL island bulk-EE -- the upper bracket, OVERSHOOT).
  * S112-CF-B5A-BRACKETED (FAIL): SINGLE-SIDED causal patch admits only the
    inverse-Mach window-fraction of the island bulk-EE (f_bulk = 0.00396,
    sbulk_causal = 60.34 nats), landing R = 0.5297 -- back at the edge undershoot.

A/4 (R = 1) sits BETWEEN the two bracket endpoints, UNREACHED by the single-sided
causal patch. This gate tests the TWO-SIDED THERMOFIELD-DOUBLE (TFD) island route:

  The white-hole exit slice has a TFD purification partner -- the two-sided
  eternal-black-hole / eternal-white-hole geometry. In a two-sided geometry the
  TFD state purifies the single-sided thermal mixed state, and the QES/island
  region I extends across BOTH sides of the TFD. The causally-accessible bulk-EE
  on the exit slice is therefore the UNION of the two sub-Mach cones (one on the
  white-hole exit side, one on its TFD partner). Geometrically the two cones
  DOUBLE the eigenvalue-window reach from the spectral floor:

      single-sided:  lambda_causal = lam_min + W_island / M       (one cone, S112)
      two-sided TFD: lambda_causal = lam_min + 2 * W_island / M    (the cone UNION)

  This is the canonical island-formula DOUBLING that resolves the Page curve in
  two-sided geometries (the island contribution to S_rad doubles relative to the
  naive single-sided count). f_bulk^TFD is DERIVED from this two-sided causal
  geometry, NOT tuned to hit R = 1.

      R_TFD(f) = R_edge + f * (R_island - R_edge)        (the bracket interpolant)
      f_bulk^TFD = S_bulk-EE(|lambda| <= lambda_causal^TFD) / S_bulk-EE(I)

ANTI-TAUTOLOGY DISCIPLINE (carried from the S111/S112 authors)
--------------------------------------------------------------
The R_TFD = 1 crossing (f* = 0.5536) is FORBIDDEN as the canonical f_bulk^TFD --
it forces A/4 BY CONSTRUCTION (the tautology the S111 author warded off and the
S112 author recorded explicitly). It is computed DIAGNOSTIC-ONLY and reported as
the forbidden line. The canonical f_bulk^TFD MUST be the substrate-DERIVED
two-sided fraction, NEVER f* = 0.5536.

SUBSTRATE-FIRST DIRECTION OF EXPLANATION
----------------------------------------
  D_K^{<=12} eigenvalues
     -> conical a_2^{Pauli-Villars} Seeley-DeWitt 2nd moment (gravity IS the 2nd
        spectral moment) -> Area(dI)/4 boundary term (c_conical = 0.25)
     -> GGE occupation of the exit-slice bulk modes inside the TWO-SIDED
        acoustic-white-hole causal patch (the cone UNION across the TFD partner)
        -> causally-accessible S_bulk-EE(I_acc^TFD) von-Neumann entropy
        (fraction f_bulk^TFD of the full island bulk-EE)
     -> S_microstate^TFD = Area(dI)/4 + f_bulk^TFD * S_bulk-EE(I)
     -> comparison to the EMERGENT area A_horizon_FW/4 (A = a_2 2nd moment; the
        area theorem is a Level-3 emergent consequence of substrate spectral
        monotonicity, per phononic-framing.md "IS Space, Not IN Space").
Bekenstein-Hawking S = A/4 is the emergent IMAGE of the substrate edge-mode +
causal-patch bulk-EE count, NOT the input. The TFD doubling is the substrate's
OWN two-sided eternal-white-hole geometry, not a holographic prescription imported
from AdS/CFT. The acoustic white hole is a ONE-DIRECTIONAL causal disconnect on
EACH side (Mach-13.75 supersonic-flow causal disconnect, PROVEN S85); the TFD
purification partner supplies the second cone.

Output:
  - data   : computations/session-114/s114_cf_b5a_tfd.npz
  - plot   : computations/session-114/s114_cf_b5a_tfd.png
  - verdict: emitted via emit_verdict MCP (delimited payload printed here)
"""

import sys
import json
import hashlib
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --- canonical constants (MANDATORY import; project root on path) -----------
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "computations" / "_shared"))
from canonical_constants import (  # noqa: E402
    A_horizon_FW, tau_fold, Mach_max_framework,
)

# ===========================================================================
# Module-level identity (consumed by print_verdict_payload)
# ===========================================================================
SESSION = "114"
WAVE = "W4-2"
GATE_ID = "CF-S113-B5A-TFD"
SCHEME = "TFD-ISLAND-TWO-SIDED-MICROSTATE-COUNT"
CONVENTION = "RATIO-DERIVED-TFD-CAUSAL-PATCH-FRACTION"
L_MAX = "12"

PASS_TOL = 0.10   # (local) |R_TFD - 1| <= 0.10 PASS band (plan tolerance)
INFO_TOL = 0.25   # (local) 0.10 < |R_TFD - 1| <= 0.25 INFO ceiling (plan tolerance)

# ===========================================================================
# Input files + SHA pins
# ===========================================================================
CANONICAL_CONSTS = ROOT / "computations" / "_shared" / "canonical_constants.py"
ISLAND_NPZ = ROOT / "computations" / "session-111" / "s111_b5a_island.npz"

# Plan-pinned SHAs (plan-freeze 2026-06-22). canonical_constants.py may drift
# mid-session (sibling S114 gate promoted a constant); per
# substrate-first-canonical-sourcing.md §(ii.B) we capture the RUNTIME SHA in the
# audit pin and document the drift in the verdict-line companion row. The values
# consumed (A_horizon_FW S92, Mach_max_framework S85) are NOT S114 promotion
# candidates, so no value-drift on consumed quantities.
CANONICAL_SHA_PLAN_PIN = "9ee1a113b200f2ad9205881f21826dc4e7975008e049b9950e38882aca722639"
ISLAND_SHA_PLAN_PIN = "378c3a3f5070390d2fb7fab2e32b5c76a442b7a102d871dac69f4ddb29ca6d2b"


def sha256_of_file(p: Path) -> str:
    h = hashlib.sha256()
    h.update(Path(p).read_bytes())
    return h.hexdigest()


def closure_hash_audit(script_path: Path, canonical_path: Path, pins: dict) -> tuple[str, str]:
    """(audit_sha256, content_sha256) per the S84+ dual-SHA schema.

    audit_sha256  = sha256( bytes(script) || bytes(canonical) || pinmap_json )
    content_sha256 = sha256( bytes(script) )   [responds to script edits only]
    """
    script_bytes = Path(script_path).read_bytes()
    canonical_bytes = Path(canonical_path).read_bytes()
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def print_verdict_payload(verdict, value_str, audit_sha, content_sha,
                          sign_v, mag_v, regime_v):
    """Emit the verdict PAYLOAD as a delimited JSON block for the dispatching
    agent to forward to the knowledge-MCP `emit_verdict` tool. The script does
    NOT write the verdict file (race-safe single-writer is emit_verdict)."""
    payload = {
        "session": int(SESSION.lstrip("Ss")),
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value_str),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
        "sign_verdict": sign_v,
        "magnitude_verdict": mag_v,
        "regime_verdict": regime_v,
    }
    print()
    print("=" * 80)
    print("VERDICT PAYLOAD (forward to emit_verdict MCP)")
    print("=" * 80)
    print(f"gate_id    = {GATE_ID}")
    print(f"verdict    = {verdict}")
    print(f"value      = {value_str}")
    print(f"sign={sign_v} magnitude={mag_v} regime={regime_v}")
    print(f"audit_sha256   = {audit_sha}")
    print(f"content_sha256 = {content_sha}")
    print("=" * 80)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ===========================================================================
# SHA input log
# ===========================================================================
print("=" * 80)
print(f"GATE ID: {GATE_ID}   SESSION: {SESSION}   WAVE: {WAVE}")
print("=" * 80)

CANONICAL_SHA_RUNTIME = sha256_of_file(CANONICAL_CONSTS)  # (local)
ISLAND_SHA_RUNTIME = sha256_of_file(ISLAND_NPZ)           # (local)

INPUT_PINS = {
    "canonical_constants": CANONICAL_SHA_RUNTIME,
    "island_npz": ISLAND_SHA_RUNTIME,
}
for k, v in INPUT_PINS.items():
    print(f"SHA INPUT: {k} = {v}")

# --- §(ii.B) plan-text-drift detection + disclosure -------------------------
canonical_drift = (CANONICAL_SHA_RUNTIME != CANONICAL_SHA_PLAN_PIN)  # (local)
island_drift = (ISLAND_SHA_RUNTIME != ISLAND_SHA_PLAN_PIN)           # (local)
print()
print("-" * 80)
print("§(ii.B) PLAN-TEXT-DRIFT CHECK (substrate-first-canonical-sourcing):")
print(f"  canonical_constants.py plan-pin = {CANONICAL_SHA_PLAN_PIN}")
print(f"  canonical_constants.py runtime  = {CANONICAL_SHA_RUNTIME}")
print(f"  canonical DRIFT detected: {canonical_drift}  "
      f"(consumed values A_horizon_FW S92, Mach S85 are NOT S114 promotion candidates "
      f"=> no value-drift on consumed quantities; runtime SHA pinned per §(ii.B))")
print(f"  s111_b5a_island.npz plan-pin = {ISLAND_SHA_PLAN_PIN}")
print(f"  s111_b5a_island.npz runtime  = {ISLAND_SHA_RUNTIME}")
print(f"  island DRIFT detected: {island_drift}  (static file; expect no drift)")
print("-" * 80)

# ===========================================================================
# Load the bracket endpoints + the island bulk-EE profile (from S111 npz)
# ===========================================================================
island = np.load(ISLAND_NPZ, allow_pickle=True)

# Pinned bracket endpoints (plan machinery_pin_map; NOT runtime-discovered)
R_edge = float(island["R_edge_S110"])             # (local) 0.5263 S110 edge-only (lower bracket)
R_island = float(island["R_island"])              # (local) 1.3820 full-island (upper bracket)
A_quarter = float(island["A_quarter"])            # (local) 17806.5658 = A_horizon_FW/4
lambda_exit = float(island["lambda_island"])      # (local) 2.4893 substrate-fixed exit anchor
S_boundary = float(island["S_boundary_S110"])     # (local) 9372 edge-mode count
sbulk_primary = float(island["sbulk_primary"])    # (local) 15236.71 full island bulk-EE @ exit
S_bulk_total = float(island["S_bulk_total"])      # (local) 180723.4 FULL spectral-support bulk-EE
c_conical = float(island["c_conical"])            # (local) 0.2500001250 a_2^{PV} conical coeff
lam_min = float(island["lam_min"])                # (local) 0.8197 spectral floor
lam_max = float(island["lam_max"])                # (local) 5.4189 spectral ceiling
N_total_modes = int(island["N_total_modes"])      # (local) 166896 L12 modes w/ multiplicity
lambda_grid = np.asarray(island["lambda_grid"], dtype=np.float64)  # (local) 300 pts
sbulk_grid = np.asarray(island["sbulk_grid"], dtype=np.float64)    # (local) cum bulk-EE

# Cross-checks against plan-pinned bracket endpoints (publication-precision)
R_EDGE_PIN = 0.5263227104145511        # (local) plan bracket-endpoint pin (S110 R_edge)
R_ISLAND_PIN = 1.3820022088029909      # (local) plan bracket-endpoint pin (S111 R_island)
A_QUARTER_PIN = 17806.56584744038      # (local) plan A_horizon_FW/4 pin
assert abs(R_edge - R_EDGE_PIN) < 1e-9, (R_edge, R_EDGE_PIN)
assert abs(R_island - R_ISLAND_PIN) < 1e-9, (R_island, R_ISLAND_PIN)
assert abs(A_quarter - A_QUARTER_PIN) < 1e-6, (A_quarter, A_QUARTER_PIN)
# A_quarter must equal the canonical A_horizon_FW/4 (publication-precision sanity).
# Per Class-8.3 item 6 the sanity tolerance must respect the pin's publication
# precision; A_horizon_FW is full-float64, so 1e-9 rel is safe.
A_quarter_canonical = A_horizon_FW / 4.0          # (local)
assert abs(A_quarter - A_quarter_canonical) < A_quarter * 1e-9, (A_quarter, A_quarter_canonical)

print()
print("-" * 80)
print("PINNED BRACKET ENDPOINTS (from S111 npz; cross-checked vs plan):")
print(f"  R_edge   (S110, lower bracket, bulk-EE OMITTED)   = {R_edge:.10f}")
print(f"  R_island (S111, upper bracket, FULL island bulk-EE)= {R_island:.10f}")
print(f"  lambda_exit (substrate a_0/a_2 fold marker)        = {lambda_exit:.4f}")
print(f"  A_quarter = A_horizon_FW/4                          = {A_quarter:.8f}")
print(f"  c_conical (a_2^Pauli-Villars conical 2nd moment)   = {c_conical:.10f}")
print(f"  S_boundary (S110 edge-mode count)                  = {S_boundary:.1f}")
print(f"  sbulk_primary (island bulk-EE @ exit; f denom)     = {sbulk_primary:.4f}")
print(f"  S_bulk_total (FULL spectral-support bulk-EE)       = {S_bulk_total:.4f}")
print("-" * 80)

# ===========================================================================
# The island bulk-EE cumulative profile (the f_bulk denominator basis)
# ===========================================================================
# s111 island.npz stores the QES scan as cumulative arrays over the upper cutoff
# lambda (lam_min -> lam_max, 300 points). sbulk_grid[i] = cumulative bulk-EE
# S_bulk-EE(|lambda| <= lambda_grid[i]). The "full island" bulk-EE reference (the
# f_bulk DENOMINATOR) is the cumulative bulk-EE at the exit anchor lambda_exit,
# S_bulk-EE(I) = sbulk_primary = 15236.71 -- the SAME denominator the S112 gate used.


def cum_bulk_at(lam_cut: float) -> float:
    """Cumulative island bulk-EE S_bulk-EE(|lambda| <= lam_cut) by interpolation
    on the cached QES scan (sbulk_grid vs lambda_grid). Clamped to the support."""
    if lam_cut <= lam_min:
        return 0.0
    if lam_cut >= lam_max:
        return float(sbulk_grid[-1])
    return float(np.interp(lam_cut, lambda_grid, sbulk_grid))


# Cross-check: cumulative bulk-EE at lambda_exit reproduces sbulk_primary
sbulk_at_exit_check = cum_bulk_at(lambda_exit)  # (local)
print(f"  cum bulk-EE at lambda_exit (interp) = {sbulk_at_exit_check:.4f}  "
      f"(vs cached sbulk_primary = {sbulk_primary:.4f}; "
      f"rel-diff {abs(sbulk_at_exit_check-sbulk_primary)/sbulk_primary:.2e})")

# --- GPU monotonicity cross-check on the L12 profile (>=100 elements) -------
used_gpu = False  # (local)
try:
    import torch
    if torch.cuda.is_available():
        dev = torch.device("cuda")
        sb_t = torch.tensor(sbulk_grid, device=dev, dtype=torch.float64)  # (local)
        dpos = torch.all(sb_t[1:] - sb_t[:-1] >= -1e-6).item()            # (local)
        used_gpu = True
        print(f"  [GPU torch path] L12 cum bulk-EE monotone-nondecreasing: {dpos} "
              f"(device={torch.cuda.get_device_name(0)}, N_modes={N_total_modes})")
    else:
        print("  [GPU path: torch.cuda not available; CPU interp used]")
except Exception as e:  # pragma: no cover
    print(f"  [GPU path unavailable, CPU cumulative interp used] {e}")

# ===========================================================================
# Reproduce the SINGLE-SIDED S112 result (continuity cross-check)
# ===========================================================================
# The acoustic white hole is a ONE-DIRECTIONAL causal disconnect (PROVEN S85):
# pre/post-transit causally separated by the Mach-13.75 supersonic flow on the
# exit slice. The single sub-Mach cone subtends an eigenvalue window of width
# W_island/M from the spectral floor.
M_wh = float(Mach_max_framework)                   # (local) 13.75 framework Mach @ van Hove fold
W_island = lambda_exit - lam_min                   # (local) island support width = 1.6696
slope = R_island - R_edge                          # (local) +0.8557 = dR_TFD/df_bulk (> 0)

lambda_causal_single = lam_min + W_island / M_wh   # (local) one-cone threshold = 0.9412
sbulk_causal_single = cum_bulk_at(lambda_causal_single)  # (local) 60.34 nats
f_bulk_single = sbulk_causal_single / sbulk_primary      # (local) 0.00396 (S112 canonical)
R_single = R_edge + f_bulk_single * slope                # (local) 0.5297 (S112 canonical)

# Continuity assertion: must reproduce S112's single-sided landing
assert abs(f_bulk_single - 0.003960) < 1e-5, (f_bulk_single, 0.003960)
assert abs(R_single - 0.529711) < 1e-5, (R_single, 0.529711)

# ===========================================================================
# DERIVE the TWO-SIDED TFD causally-accessible bulk fraction f_bulk^TFD
# (the TFD island doubling; NOT tuned to R = 1)
# ===========================================================================
# In the two-sided eternal-white-hole (TFD) geometry the QES/island region I
# extends across BOTH sides of the thermofield double. The TFD state purifies the
# single-sided thermal mixed state, so the causally-accessible bulk-EE on the exit
# slice is the UNION of the two sub-Mach cones (the white-hole exit side + its TFD
# purification partner). The two cones DOUBLE the eigenvalue-window reach from the
# spectral floor:
#       lambda_causal^TFD = lam_min + 2 * W_island / M
# This is the canonical island-formula DOUBLING (the island contribution to S_rad
# doubles in two-sided geometries -- the structure that reproduces the Page curve).
# f_bulk^TFD is the bulk-EE fraction inside this DOUBLED patch:
#       f_bulk^TFD = cum_bulk_at(lambda_causal^TFD) / sbulk_primary.
lambda_causal_tfd = lam_min + 2.0 * W_island / M_wh      # (local) two-cone threshold = 1.0626
sbulk_causal_tfd = cum_bulk_at(lambda_causal_tfd)        # (local) accessible bulk-EE
f_bulk_tfd = sbulk_causal_tfd / sbulk_primary            # (local) DERIVED TFD fraction (canonical)

# ---------------------------------------------------------------------------
# Transparent DIAGNOSTIC alternatives (NOT the canonical f_bulk^TFD; reported so
# the audit can see the canonical value follows the pinned two-sided definition
# and is NOT the R=1 crossing). Each is a DIFFERENT TFD-fraction reading.
# ---------------------------------------------------------------------------
# (D1) doubled FRACTION directly (2 * f_single rather than the doubled-window cum):
f_bulk_double_frac = 2.0 * f_bulk_single                 # (local) 0.00792
R_double_frac = R_edge + f_bulk_double_frac * slope      # (local)
# (D2) direct 2/M bulk-EE fraction (two-sided inverse-Mach as a raw fraction):
f_bulk_direct_2invmach = 2.0 / M_wh                      # (local) 0.14545
R_direct_2invmach = R_edge + f_bulk_direct_2invmach * slope  # (local)
# (D3) FORBIDDEN tautology: the f_bulk^TFD that lands R EXACTLY at unity:
f_bulk_unity = (1.0 - R_edge) / slope                    # (local) 0.5536 FORBIDDEN

R_tfd = R_edge + f_bulk_tfd * slope                      # (local) canonical TFD ratio
S_microstate_tfd = R_tfd * A_quarter                     # (local) absolute microstate count
abs_R_minus_1 = abs(R_tfd - 1.0)                         # (local) the gate metric

print()
print("-" * 80)
print("DERIVED TWO-SIDED TFD CAUSAL-PATCH FRACTION f_bulk^TFD (NOT tuned to R=1):")
print(f"  Mach (framework, van Hove fold)  M       = {M_wh}")
print(f"  island support width  W = lam_exit-lam_min = {W_island:.6f}")
print(f"  SINGLE-sided patch width  W/M             = {W_island/M_wh:.6f}")
print(f"  TWO-sided TFD patch width 2W/M            = {2.0*W_island/M_wh:.6f}")
print(f"  lambda_causal(single) = lam_min + W/M     = {lambda_causal_single:.6f}")
print(f"  lambda_causal(TFD)    = lam_min + 2W/M    = {lambda_causal_tfd:.6f}")
print(f"  cum bulk-EE(single) inside W/M patch      = {sbulk_causal_single:.4f}")
print(f"  cum bulk-EE(TFD) inside 2W/M patch        = {sbulk_causal_tfd:.4f}")
print(f"  S_bulk-EE(I) full island (denominator)    = {sbulk_primary:.4f}")
print(f"  f_bulk(single, S112 continuity)           = {f_bulk_single:.6f}  -> R = {R_single:.6f}")
print(f"  ==> f_bulk^TFD (CANONICAL, pinned defn)   = {f_bulk_tfd:.6f}  -> R_TFD = {R_tfd:.6f}")
print("  DIAGNOSTIC alternatives (NOT canonical):")
print(f"    (D1) doubled fraction 2*f_single        f = {f_bulk_double_frac:.6f} -> R = {R_double_frac:.6f}")
print(f"    (D2) direct 2/M bulk-EE fraction        f = {f_bulk_direct_2invmach:.6f} -> R = {R_direct_2invmach:.6f}")
print(f"    (D3) [FORBIDDEN] R=1 tautology crossing f* = {f_bulk_unity:.6f}")
print("-" * 80)

# ===========================================================================
# PASS / INFO bands on f_bulk (the pre-image of |R_TFD-1|<=tol under the interp)
# ===========================================================================
f_pass_lo = (0.90 - R_edge) / slope            # (local) R=0.90
f_pass_hi = (1.10 - R_edge) / slope            # (local) R=1.10
f_info_lo = (1.0 - INFO_TOL - R_edge) / slope  # (local) R=0.75
f_info_hi = (1.0 + INFO_TOL - R_edge) / slope  # (local) R=1.25

# ---------------------------------------------------------------------------
# Substitution chain (printed for audit trail; [SIGN] trigger MANDATORY)
# ---------------------------------------------------------------------------
print()
print("-" * 80)
print("SUBSTITUTION CHAIN ([SIGN] trigger; plan W4-2):")
print("  Claim: R_TFD is strictly increasing in f_bulk^TFD; dR_TFD/df = R_island")
print("         - R_edge > 0; the two-sided TFD patch raises f_bulk above the")
print("         single-sided 0.00396, pushing R_TFD up from the edge undershoot")
print("         toward A/4.")
print(f"  Def1: R_edge   = S_boundary/(A/4) = {S_boundary:.0f}/{A_quarter:.4f} = {R_edge:.6f}")
print(f"  Def2: R_island = [Area(dI)/4 + S_bulk-EE(I)]/(A/4) = {R_island:.6f}")
print(f"  Def3: A_quarter = A_horizon_FW/4 = {A_horizon_FW:.6f}/4 = {A_quarter:.6f}")
print(f"  Def6: f_bulk^TFD = S_bulk-EE(I_acc^TFD)/S_bulk-EE(I)")
print(f"        = {sbulk_causal_tfd:.4f}/{sbulk_primary:.4f} = {f_bulk_tfd:.6f}")
print(f"  Substitute: R_TFD(f) = R_edge + f*(R_island - R_edge) = {R_edge:.6f} + f*{slope:.6f}")
print(f"  Simplify:   dR_TFD/df = R_island - R_edge")
print(f"            = {R_island:.10f} - {R_edge:.10f}")
print(f"            = {slope:.10f}")
print(f"  Direction:  dR_TFD/df = {slope:+.4f} > 0  => R_TFD strictly increasing.")
print(f"              f_bulk^TFD = {f_bulk_tfd:.6f} > f_single = {f_bulk_single:.6f}")
print(f"              => R_TFD = {R_tfd:.6f} > R_single = {R_single:.6f} (gap-closing).")
print(f"  ANTI-TAUTOLOGY: R=1 at f* = (1-R_edge)/slope = {f_bulk_unity:.6f} -- FORBIDDEN canonical.")
print(f"  Result: |R_TFD - 1| = {abs_R_minus_1:.6f}  vs PASS {PASS_TOL}, INFO {INFO_TOL}")
print(f"          PASS band on f: [{f_pass_lo:.4f}, {f_pass_hi:.4f}] (vs 2/M ceiling {2.0/M_wh:.4f})")
print("-" * 80)

# ---------------------------------------------------------------------------
# 3-tuple verdict (sign / magnitude / regime)
# ---------------------------------------------------------------------------
# SIGN: predicted direction dR_TFD/df_bulk > 0. PASS iff the computed slope sign
#       matches (it does, by the NON-NEGATIVE bulk-EE correction; both prior B5A
#       verdicts carried sign=PASS).
sign_v = "PASS" if slope > 0 else "FAIL"           # (local)

# MAGNITUDE: |R_TFD - 1| against the PASS/INFO bands.
if abs_R_minus_1 <= PASS_TOL:
    mag_v = "PASS"
elif abs_R_minus_1 <= INFO_TOL:
    mag_v = "INFO"
else:
    mag_v = "FAIL"

# REGIME: VALID iff the derived lambda_causal^TFD sits strictly inside the island
#         support [lam_min, lambda_exit] (the two-sided causal-patch interpolation
#         is well-posed) AND f_bulk^TFD in [0,1] (a genuine fraction).
regime_ok = (lam_min < lambda_causal_tfd < lambda_exit) and (0.0 <= f_bulk_tfd <= 1.0)  # (local)
regime_v = "VALID" if regime_ok else "BREAKDOWN"   # (local)

# Composite collapse (PRE-REGISTERED rule, gate-verdicts.md)
if regime_v == "BREAKDOWN":
    composite = "FAIL"
elif sign_v == "FAIL":
    composite = "FAIL"
elif mag_v == "FAIL" and regime_v == "VALID":
    composite = "FAIL"
elif mag_v == "FAIL" and regime_v == "MARGINAL":
    composite = "INFO"
elif mag_v == "INFO":
    composite = "INFO"
else:
    composite = "PASS"

print()
print(f"3-tuple: sign={sign_v}  magnitude={mag_v}  regime={regime_v}  => composite={composite}")

# ===========================================================================
# Save data
# ===========================================================================
OUT_NPZ = ROOT / "computations" / "session-114" / "s114_cf_b5a_tfd.npz"
OUT_PNG = ROOT / "computations" / "session-114" / "s114_cf_b5a_tfd.png"

np.savez(
    OUT_NPZ,
    # canonical TFD landing
    R_tfd=R_tfd,
    f_bulk_tfd=f_bulk_tfd,
    S_microstate_tfd=S_microstate_tfd,
    abs_R_minus_1=abs_R_minus_1,
    sign_verdict=sign_v,
    magnitude_verdict=mag_v,
    regime_verdict=regime_v,
    composite_verdict=composite,
    PASS_TOL=PASS_TOL,
    INFO_TOL=INFO_TOL,
    # bracket endpoints (pinned)
    R_edge=R_edge,
    R_island=R_island,
    slope=slope,
    lambda_exit=lambda_exit,
    A_quarter=A_quarter,
    A_horizon_FW=A_horizon_FW,
    c_conical=c_conical,
    S_boundary=S_boundary,
    sbulk_primary=sbulk_primary,
    S_bulk_total=S_bulk_total,
    # single-sided S112 continuity cross-check
    lambda_causal_single=lambda_causal_single,
    sbulk_causal_single=sbulk_causal_single,
    f_bulk_single=f_bulk_single,
    R_single=R_single,
    # two-sided TFD derivation
    Mach_framework=M_wh,
    W_island=W_island,
    lambda_causal_tfd=lambda_causal_tfd,
    sbulk_causal_tfd=sbulk_causal_tfd,
    lam_min=lam_min,
    lam_max=lam_max,
    N_total_modes=N_total_modes,
    # PASS / INFO bands on f_bulk
    f_pass_lo=f_pass_lo,
    f_pass_hi=f_pass_hi,
    f_info_lo=f_info_lo,
    f_info_hi=f_info_hi,
    f_bulk_unity=f_bulk_unity,
    # diagnostic alternatives
    f_bulk_double_frac=f_bulk_double_frac,
    R_double_frac=R_double_frac,
    f_bulk_direct_2invmach=f_bulk_direct_2invmach,
    R_direct_2invmach=R_direct_2invmach,
    # drift disclosure (§(ii.B))
    canonical_sha_runtime=CANONICAL_SHA_RUNTIME,
    canonical_sha_plan_pin=CANONICAL_SHA_PLAN_PIN,
    canonical_drift=canonical_drift,
    island_sha_runtime=ISLAND_SHA_RUNTIME,
    island_drift=island_drift,
    used_gpu=used_gpu,
)
print(f"\nSaved: {OUT_NPZ}")

# ===========================================================================
# Plot
# ===========================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.2))

# Panel A: R_TFD(f) interpolant with bands + single-sided + TFD markers
f_axis = np.linspace(0.0, 1.0, 400)                # (local)
R_axis = R_edge + f_axis * slope                   # (local)
ax1.plot(f_axis, R_axis, color="navy", lw=2.0, label=r"$R_{\rm TFD}(f_{\rm bulk})$ interpolant")
ax1.axhline(1.0, color="black", lw=1.0, ls=":")
ax1.axhspan(0.90, 1.10, color="green", alpha=0.18, label=r"PASS band ($|R-1|\leq0.10$)")
ax1.axhspan(0.75, 0.90, color="gold", alpha=0.14)
ax1.axhspan(1.10, 1.25, color="gold", alpha=0.14, label=r"INFO band ($\leq0.25$)")
ax1.plot([0.0], [R_edge], "v", color="crimson", ms=11,
         label=fr"$R_{{\rm edge}}={R_edge:.3f}$ (S110 undershoot)")
ax1.plot([1.0], [R_island], "^", color="darkorange", ms=11,
         label=fr"$R_{{\rm island}}={R_island:.3f}$ (S111 overshoot)")
ax1.plot([f_bulk_single], [R_single], "s", color="purple", ms=9, zorder=5,
         label=fr"single-sided $f={f_bulk_single:.4f}\Rightarrow R={R_single:.3f}$ (S112)")
ax1.plot([f_bulk_tfd], [R_tfd], "o", color="black", ms=12, zorder=6,
         label=fr"TFD $f={f_bulk_tfd:.4f}\Rightarrow R_{{\rm TFD}}={R_tfd:.3f}$")
ax1.axvline(f_bulk_unity, color="grey", ls="--", lw=1.0,
            label=fr"[FORBIDDEN] $f^*_{{R=1}}={f_bulk_unity:.3f}$")
ax1.axvspan(f_pass_lo, f_pass_hi, color="green", alpha=0.07)
ax1.set_xlabel(r"causally-accessible bulk fraction  $f_{\rm bulk}$")
ax1.set_ylabel(r"$R = S_{\rm microstate}/(A_{\rm horizon}/4)$")
ax1.set_title("Two-sided TFD white-hole microstate ratio")
ax1.legend(fontsize=6.6, loc="upper left")
ax1.grid(alpha=0.25)

# Panel B: cumulative island bulk-EE vs lambda with single + TFD + exit markers
ax2.plot(lambda_grid, sbulk_grid, color="teal", lw=1.8,
         label=r"cumulative $S_{\rm bulk\text{-}EE}(|\lambda|\leq\lambda)$")
ax2.axvline(lambda_exit, color="crimson", ls="--", lw=1.4,
            label=fr"$\lambda_{{\rm exit}}={lambda_exit:.3f}$ (island)")
ax2.axvline(lambda_causal_single, color="purple", ls=":", lw=1.3,
            label=fr"$\lambda_{{\rm causal}}^{{(1)}}={lambda_causal_single:.3f}$ (single $W/M$)")
ax2.axvline(lambda_causal_tfd, color="black", ls="-.", lw=1.4,
            label=fr"$\lambda_{{\rm causal}}^{{\rm TFD}}={lambda_causal_tfd:.3f}$ (two-sided $2W/M$)")
ax2.plot([lambda_causal_single], [sbulk_causal_single], "s", color="purple", ms=8, zorder=5)
ax2.plot([lambda_causal_tfd], [sbulk_causal_tfd], "o", color="black", ms=9, zorder=5)
ax2.plot([lambda_exit], [sbulk_primary], "D", color="crimson", ms=8, zorder=5)
ax2.set_xlabel(r"island-boundary eigenvalue cutoff $\lambda$")
ax2.set_ylabel(r"cumulative bulk-EE  $S_{\rm bulk\text{-}EE}$")
ax2.set_title(fr"TFD doubling: $f_{{\rm bulk}}^{{\rm TFD}}={f_bulk_tfd:.4f}$ (vs single {f_bulk_single:.4f})")
ax2.legend(fontsize=6.8, loc="upper left")
ax2.grid(alpha=0.25)

fig.suptitle(
    fr"CF-S113-B5A-TFD  —  $R_{{\rm TFD}}={R_tfd:.4f}$, "
    fr"$|R_{{\rm TFD}}-1|={abs_R_minus_1:.4f}$  →  {composite}  "
    fr"(sign={sign_v}, mag={mag_v}, regime={regime_v})",
    fontsize=10.5,
)
fig.tight_layout(rect=(0, 0, 1, 0.96))
fig.savefig(OUT_PNG, dpi=130)
print(f"Saved: {OUT_PNG}")

# ===========================================================================
# Dual-SHA + verdict payload
# ===========================================================================
audit_sha, content_sha = closure_hash_audit(Path(__file__), CANONICAL_CONSTS, INPUT_PINS)

value_str = (
    f"R_TFD={R_tfd:.6f};f_bulk_TFD={f_bulk_tfd:.6f};abs_R_minus_1={abs_R_minus_1:.6f};"
    f"R_edge={R_edge:.6f};R_island={R_island:.6f};slope={slope:.6f};"
    f"lambda_causal_TFD={lambda_causal_tfd:.6f};lambda_causal_single={lambda_causal_single:.6f};"
    f"lambda_exit={lambda_exit:.4f};sbulk_causal_TFD={sbulk_causal_tfd:.4f};"
    f"sbulk_causal_single={sbulk_causal_single:.4f};sbulk_primary={sbulk_primary:.4f};"
    f"f_bulk_single={f_bulk_single:.6f};R_single={R_single:.6f};Mach={M_wh};"
    f"f_pass_band=[{f_pass_lo:.4f},{f_pass_hi:.4f}];f_bulk_unity_FORBIDDEN={f_bulk_unity:.4f};"
    f"f_direct_2invMach_DIAG={f_bulk_direct_2invmach:.4f};R_direct_2invMach_DIAG={R_direct_2invmach:.4f};"
    f"S_microstate_TFD={S_microstate_tfd:.2f};A_quarter={A_quarter:.4f};c_conical={c_conical:.7f}"
)

print_verdict_payload(
    composite, value_str, audit_sha, content_sha, sign_v, mag_v, regime_v
)

sys.exit(0)
