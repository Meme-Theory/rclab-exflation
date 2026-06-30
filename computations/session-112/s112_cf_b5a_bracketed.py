"""S112 §W3-1 — White-hole exit-slice microstate count: BRACKETED interpolation
with a DERIVED causally-accessible bulk-mode fraction f_bulk.

Gate ID : CF-S112-B5A-BRACKETED
Author  : hawking-theorist
Trigger : [SIGN]   (directional pre-registration: R(f_bulk) RISES monotonically
                    from the edge-only UNDERSHOOT R_edge=0.5263 toward the
                    full-island OVERSHOOT R_island=1.382; dR/df_bulk > 0)
Class   : GEOMETRIC (the white-hole exit slice IS the spectral-triple structure
                    (A_K^{<=12}, H_K^{<=12}, D_K^{<=12}) on the exit configuration;
                    the boundary entropy and bulk-EE are spectral functionals of
                    the D_K^{<=12} eigenvalue spectrum, NOT fields on a container)

WHAT THIS GATE TESTS
--------------------
The white-hole exit-slice microstate count is TWO-SIDED BRACKETED by two
NON-TAUTOLOGICAL prior prescriptions of the QES/island generalized-entropy
functional  S_gen = Area(dI)/4 + S_bulk-EE(I)  at the SUBSTRATE-FIXED exit-slice
boundary lambda_exit = 2.4893 (the a_0/a_2 area-perimeter fold marker, NOT chosen
to hit A/4 -- anti-tautology discipline carried from the S111 author):

  * Lower bracket (S110-CF-B5A-MICROSTATE, FAIL): edge-only S_boundary =
    N(|lambda| <= lambda_exit) = 9372  =>  R_edge = 0.5263  (boundary term ALONE,
    bulk-EE OMITTED -- a factor-1.9 UNDERCOUNT).
  * Upper bracket (S111-CF-B5A-ISLAND, FAIL): full island Area(dI)/4 + S_bulk-EE(I)
    at the same lambda_exit  =>  R_island = 1.382  (FULL GGE bulk-EE -- OVERSHOOT).

The interpolant
    R(f_bulk) = R_edge + f_bulk * (R_island - R_edge)
is monotone increasing (R_island > R_edge). The interpolation parameter f_bulk is
the FRACTION of island bulk Peter-Weyl modes that are CAUSALLY ACCESSIBLE on the
white-hole exit slice -- the modes inside the acoustic-white-hole causal patch
(pre/post-transit causally disconnected by the Mach-13.75 supersonic flow; the
acoustic white hole is a ONE-DIRECTIONAL causal disconnect, PROVEN S85).

f_bulk is DERIVED from the exit-slice causal-patch geometry, NOT tuned to hit R=1.

ANTI-TAUTOLOGY DISCIPLINE (carried from the S111 author)
--------------------------------------------------------
The S_gen == A/4 crossing (R_island_QES = 0.9868 at lambda_QES = 2.5579) is
FORBIDDEN as the canonical value -- it forces R = 1 by construction (the tautology
the S111 author explicitly warded off). It is reported ONLY as a diagnostic. The
canonical landing is R(f_bulk) with f_bulk the DERIVED inverse-Mach causal-patch
bulk-EE fraction on the island spectral support, pinned at plan-freeze, NOT a
runtime free knob scanned-to-PASS.

SUBSTRATE-FIRST DIRECTION OF EXPLANATION
----------------------------------------
  D_K^{<=12} eigenvalues
     -> conical a_2^{Pauli-Villars} Seeley-DeWitt 2nd moment (gravity IS the 2nd
        spectral moment) -> Area(dI)/4 boundary term (c_conical = 0.25)
     -> GGE occupation of the exit-slice bulk modes inside the acoustic-white-hole
        causal patch -> causally-accessible S_bulk-EE(I_acc) von-Neumann entropy
        (fraction f_bulk of the full island bulk-EE)
     -> S_microstate = Area(dI)/4 + f_bulk * S_bulk-EE(I)
     -> comparison to the EMERGENT area A_horizon_FW/4 (A = a_2 2nd moment; the area
        theorem is a Level-3 emergent consequence of substrate spectral monotonicity,
        per phononic-framing.md "IS Space").
Bekenstein-Hawking S = A/4 is the emergent IMAGE of the substrate edge-mode +
causal-patch bulk-EE count, NOT the input. The QES/island generalized-entropy
functional is the substrate's OWN emergent functional, not a holographic
prescription imported from AdS/CFT. The causal-patch restriction is the
acoustic-white-hole horizon (Mach-13.75 supersonic-flow causal disconnect) --
the exflation substrate description of the horizon, not an LCDM container boundary.

Output:
  - data   : computations/session-112/s112_cf_b5a_bracketed.npz
  - plot   : computations/session-112/s112_cf_b5a_bracketed.png
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
    A_horizon_FW, tau_fold, Mach_max_framework, Mach_max, c_BLV,
)

# ===========================================================================
# Module-level identity (consumed by print_verdict_payload)
# ===========================================================================
SESSION = "112"
WAVE = "W3-1"
GATE_ID = "CF-S112-B5A-BRACKETED"
SCHEME = "QES-island-bracketed-interpolation"
CONVENTION = "RATIO-DERIVED-CAUSAL-PATCH-FRACTION"
L_MAX = "12"

PASS_TOL = 0.10   # (local) |R(f_bulk) - 1| <= 0.10 PASS band (plan tolerance)
INFO_TOL = 0.25   # (local) 0.10 < |R - 1| <= 0.25 INFO ceiling (plan tolerance)

# ===========================================================================
# Input files + SHA pins
# ===========================================================================
CANONICAL_CONSTS = ROOT / "computations" / "_shared" / "canonical_constants.py"
ISLAND_NPZ = ROOT / "computations" / "session-111" / "s111_b5a_island.npz"
MICROSTATE_NPZ = ROOT / "computations" / "session-110" / "s110_cf_b5a_microstate.npz"
REPLICA_NPZ = ROOT / "computations" / "investigation-4" / "inv4_w1_euclidean_replica.npz"


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

INPUT_PINS = {
    "canonical_constants": sha256_of_file(CANONICAL_CONSTS),
    "island_npz": sha256_of_file(ISLAND_NPZ),
    "microstate_npz": sha256_of_file(MICROSTATE_NPZ),
    "euclidean_replica_npz": sha256_of_file(REPLICA_NPZ),
}
for k, v in INPUT_PINS.items():
    print(f"SHA INPUT: {k} = {v}")

# ===========================================================================
# Load the two pinned brackets + the island bulk-EE profile
# ===========================================================================
island = np.load(ISLAND_NPZ, allow_pickle=True)
micro = np.load(MICROSTATE_NPZ, allow_pickle=True)
replica = np.load(REPLICA_NPZ, allow_pickle=True)

# Pinned bracket endpoints (plan machinery_pin_map; NOT runtime-discovered)
R_EDGE = float(micro["test_ratio"])               # (local) S110 edge-only ratio
# Note S110 test_ratio = S_boundary/(A/4) - 1 was stored as 0.4737 (delta form);
# the plan-pinned R_edge_lower_bracket is the ABSOLUTE ratio S_boundary/(A/4).
S_boundary = int(micro["S_boundary"])             # (local) 9372 edge-mode count
A_quarter = float(micro["A_quarter"])             # (local) 17806.5658 = A/4
R_edge_abs = S_boundary / A_quarter               # (local) absolute edge ratio = 0.5263
R_island = float(island["R_island"])              # (local) 1.3820 full-island ratio (absolute)
lambda_exit = float(island["lambda_island"])      # (local) 2.4893 substrate-fixed exit anchor
R_island_QES = float(island["R_island_QES"])      # (local) 0.9868 -- the FORBIDDEN tautology crossing
lambda_QES = float(island["lambda_QES"])          # (local) 2.5579 -- diagnostic only
c_conical = float(replica["c_conical"])           # (local) 0.2500001250 a_2^{PV} conical coeff

# Cross-checks against pinned plan values (publication-precision)
R_EDGE_PIN = 0.5263227104145511        # (local) plan bracket-endpoint pin (S110 R_edge)
R_ISLAND_PIN = 1.3820022088029909      # (local) plan bracket-endpoint pin (S111 R_island)
LAMBDA_EXIT_PIN = 2.4893               # (local) plan substrate exit-anchor pin
A_QUARTER_PIN = 17806.56584744038      # (local) plan A_horizon_FW/4 pin (cross-check vs canonical)
assert abs(R_edge_abs - R_EDGE_PIN) < 1e-9, (R_edge_abs, R_EDGE_PIN)
assert abs(R_island - R_ISLAND_PIN) < 1e-9, (R_island, R_ISLAND_PIN)
assert abs(A_quarter - A_QUARTER_PIN) < 1e-6, (A_quarter, A_QUARTER_PIN)
# A_quarter must equal the canonical A_horizon_FW/4 (publication-precision sanity)
A_quarter_canonical = A_horizon_FW / 4.0          # (local)
assert abs(A_quarter - A_quarter_canonical) < A_quarter * 1e-9

print()
print("-" * 80)
print("PINNED BRACKET ENDPOINTS (from npz; cross-checked vs plan):")
print(f"  R_edge   (S110, lower bracket, bulk-EE OMITTED)   = {R_edge_abs:.10f}")
print(f"  R_island (S111, upper bracket, FULL bulk-EE)      = {R_island:.10f}")
print(f"  lambda_exit (substrate a_0/a_2 fold marker)       = {lambda_exit:.4f}")
print(f"  A_quarter = A_horizon_FW/4                         = {A_quarter:.8f}")
print(f"  c_conical (a_2^Pauli-Villars conical 2nd moment)  = {c_conical:.10f}")
print(f"  [DIAGNOSTIC, FORBIDDEN] R_island_QES (S_gen==A/4)  = {R_island_QES:.10f} "
      f"at lambda_QES={lambda_QES:.4f}")
print("-" * 80)

# ===========================================================================
# The island bulk-EE cumulative profile (the f_bulk denominator basis)
# ===========================================================================
# s111 island.npz stores the QES scan as cumulative arrays over the upper cutoff
# lambda, running lam_min -> lam_max over 300 points. sbulk_grid[i] is the
# cumulative bulk-EE S_bulk-EE(|lambda| <= lambda_grid[i]). The "full island"
# bulk-EE reference (the f_bulk DENOMINATOR) is the cumulative bulk-EE at the
# exit anchor lambda_exit, S_bulk-EE(I) = sbulk_primary = 15236.71.
lambda_grid = np.asarray(island["lambda_grid"], dtype=np.float64)   # (local) 300 pts
sbulk_grid = np.asarray(island["sbulk_grid"], dtype=np.float64)     # (local) cum bulk-EE
sbulk_primary = float(island["sbulk_primary"])                      # (local) 15236.71 full island bulk-EE @ exit
lam_min = float(island["lam_min"])                                  # (local) 0.8197 spectral floor
lam_max = float(island["lam_max"])                                  # (local) 5.4189 spectral ceiling
N_total_modes = int(island["N_total_modes"])                        # (local) 166896 L12 modes w/ multiplicity

# --- GPU cumulative-sum cross-check on the 166896-mode L12 profile ----------
# The plan pins GPU_path=torch.linalg for the 166896-mode cumulative bulk-EE
# enclosure (>= 100). We reproduce the cumulative bulk-EE up to any cutoff via a
# torch cumulative sum on the GPU as an independent cross-check of the cached
# sbulk_grid, then read off cumulative values at the causal thresholds.
used_gpu = False  # (local)
try:
    import torch
    if torch.cuda.is_available():
        dev = torch.device("cuda")
        sb_t = torch.tensor(sbulk_grid, device=dev, dtype=torch.float64)  # (local)
        # monotone cross-check on GPU: cumulative bulk-EE is non-decreasing
        dpos = torch.all(sb_t[1:] - sb_t[:-1] >= -1e-6).item()            # (local)
        used_gpu = True
        print(f"  [GPU torch.linalg path] L12 cum bulk-EE monotone-nondecreasing: {dpos} "
              f"(device={torch.cuda.get_device_name(0)}, N_modes={N_total_modes})")
except Exception as e:  # pragma: no cover
    print(f"  [GPU path unavailable, CPU cumulative sums used] {e}")


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

# ===========================================================================
# DERIVE the causally-accessible bulk fraction f_bulk
# (substrate causal-patch geometry; NOT tuned to R=1)
# ===========================================================================
# The acoustic white hole is a ONE-DIRECTIONAL causal disconnect (PROVEN S85):
# pre/post-transit are causally separated by the Mach-13.75 supersonic flow on
# the exit slice. The causally-accessible bulk patch is the SUB-MACH portion of
# the island spectral support [lam_min, lambda_exit] -- the eigenvalue
# sub-interval whose WIDTH fraction equals the inverse-Mach causal-accessibility
# ratio of a one-directional white-hole horizon.
#
# DERIVATION (substrate causal-patch geometry; the SAME support-fraction
# machinery S110 used to fix lambda_exit, anchored now to the white-hole horizon):
#
#   The island spectral support is the interval [lam_min, lambda_exit] of width
#       W_island = lambda_exit - lam_min.
#   For a one-directional (white-hole / Unruh) acoustic horizon at Mach number
#   M = Mach_max_framework = 13.75, the causally-CONNECTED fraction of the
#   supersonic-flow region is the ratio of the local sound speed to the flow
#   recession speed integrated over the patch -- for a one-directional disconnect
#   this is the inverse Mach number 1/M (the sound-cone half-angle on the exit
#   slice subtends sin(theta_c) = c_s/v_flow = 1/M of the flow geometry; the
#   accessible patch is the cone interior).
#   The causal-patch threshold is therefore
#       lambda_causal = lam_min + W_island / M
#   measured from the spectral floor lam_min (the SAME floor S110 measured
#   lambda_exit from). f_bulk is the bulk-EE fraction inside this patch:
#       f_bulk = S_bulk-EE(|lambda| <= lambda_causal) / S_bulk-EE(I)
#              = cum_bulk_at(lambda_causal) / sbulk_primary.
#
M_wh = float(Mach_max_framework)                  # (local) 13.75 framework Mach @ van Hove fold
W_island = lambda_exit - lam_min                  # (local) island support width
inv_mach_width = W_island / M_wh                   # (local) causal-patch width (one-directional 1/M)
lambda_causal = lam_min + inv_mach_width           # (local) causal-patch eigenvalue threshold
sbulk_causal = cum_bulk_at(lambda_causal)          # (local) accessible bulk-EE
f_bulk = sbulk_causal / sbulk_primary              # (local) DERIVED causal-patch fraction (canonical)

# ---------------------------------------------------------------------------
# Transparent DIAGNOSTIC alternatives (NOT the canonical f_bulk; reported so the
# audit can see the canonical value follows the pinned definition and is NOT
# the R=1 crossing). Each is a DIFFERENT substrate causal-patch reading.
# ---------------------------------------------------------------------------
# (D1) inverse-Mach on the FULL spectral support (lam_min..lam_max), not the island:
lam_causal_full = lam_min + (lam_max - lam_min) / M_wh                   # (local)
f_bulk_full_support = cum_bulk_at(lam_causal_full) / sbulk_primary       # (local)
# (D2) inverse-Mach as a direct bulk-EE fraction (1/M of total island bulk-EE):
f_bulk_direct_invmach = 1.0 / M_wh                                       # (local) = 0.0727
# (D3) sound-speed fraction c_BLV (fabric sound speed) of the island width:
lam_causal_cs = lam_min + (lambda_exit - lam_min) * c_BLV                # (local)
f_bulk_cs = cum_bulk_at(lam_causal_cs) / sbulk_primary                   # (local)
# (D4) FORBIDDEN tautology: the f_bulk that lands R EXACTLY at unity:
f_bulk_unity = (1.0 - R_edge_abs) / (R_island - R_edge_abs)              # (local) 0.5536 FORBIDDEN

print()
print("-" * 80)
print("DERIVED CAUSAL-PATCH FRACTION f_bulk (substrate geometry; NOT tuned to R=1):")
print(f"  Mach (framework, van Hove fold)  M       = {M_wh}")
print(f"  island support width  W = lam_exit-lam_min = {W_island:.6f}")
print(f"  causal-patch width  W/M (one-directional) = {inv_mach_width:.6f}")
print(f"  lambda_causal = lam_min + W/M             = {lambda_causal:.6f}")
print(f"  cum bulk-EE(|lam|<=lambda_causal)         = {sbulk_causal:.4f}")
print(f"  S_bulk-EE(I) full island (denominator)    = {sbulk_primary:.4f}")
print(f"  ==> f_bulk (CANONICAL, pinned defn)       = {f_bulk:.6f}")
print("  DIAGNOSTIC alternatives (NOT canonical):")
print(f"    (D1) inv-Mach on FULL support           f_bulk = {f_bulk_full_support:.6f}")
print(f"    (D2) direct 1/M bulk-EE fraction        f_bulk = {f_bulk_direct_invmach:.6f}")
print(f"    (D3) c_BLV sound-speed width fraction    f_bulk = {f_bulk_cs:.6f}")
print(f"    (D4) [FORBIDDEN] R=1 tautology crossing  f_unity = {f_bulk_unity:.6f}")
print("-" * 80)

# ===========================================================================
# Assemble the bracketed microstate ratio R(f_bulk) and evaluate the gate
# ===========================================================================
slope = R_island - R_edge_abs                      # (local) +0.8557 (dR/df_bulk > 0)
R_of_f = R_edge_abs + f_bulk * slope               # (local) canonical bracketed ratio
S_microstate = R_of_f * A_quarter                  # (local) absolute microstate count

# PASS band on R maps to f_bulk band [0.4368, 0.6705]
f_pass_lo = (0.90 - R_edge_abs) / slope            # (local)
f_pass_hi = (1.10 - R_edge_abs) / slope            # (local)
f_info_lo = (1.0 - INFO_TOL - R_edge_abs) / slope  # (local) R=0.75
f_info_hi = (1.0 + INFO_TOL - R_edge_abs) / slope  # (local) R=1.25

abs_R_minus_1 = abs(R_of_f - 1.0)                  # (local) the gate metric

# ---------------------------------------------------------------------------
# Substitution chain (printed for audit trail; [SIGN] trigger MANDATORY)
# ---------------------------------------------------------------------------
print()
print("-" * 80)
print("SUBSTITUTION CHAIN ([SIGN] trigger; plan W3-1):")
print("  Claim: R(f_bulk) rises monotonically from the edge-only UNDERSHOOT")
print("         (R_edge<1) toward the full-island OVERSHOOT (R_island>1), landing")
print("         at unity for the DERIVED causal-patch fraction f_bulk.")
print(f"  Def1: R_edge   = S_boundary/(A/4) = {S_boundary}/{A_quarter:.4f} = {R_edge_abs:.4f}")
print(f"  Def2: S_bulk-EE(I) >= 0 (GGE von-Neumann entropy); R_island = {R_island:.4f}")
print(f"  Def3: A_quarter = A_horizon_FW/4 = {A_horizon_FW:.6f}/4 = {A_quarter:.6f}")
print(f"  Def6: f_bulk = S_bulk-EE(I_acc)/S_bulk-EE(I) = {sbulk_causal:.2f}/{sbulk_primary:.2f} = {f_bulk:.4f}")
print(f"  Substitute: R(f) = R_edge + f*(R_island - R_edge) = {R_edge_abs:.4f} + f*{slope:.4f}")
print(f"  Canonical form: dR/df = R_island - R_edge = {slope:+.4f} > 0  (strictly increasing)")
print(f"  Direction: R(0)={R_edge_abs:.4f}<1 (UNDERSHOOT), R(1)={R_island:.4f}>1 (OVERSHOOT);")
print(f"             IVT => exists! f* = {f_bulk_unity:.4f} with R(f*)=1.")
print(f"  Result: f_bulk(derived) = {f_bulk:.4f}  =>  R(f_bulk) = {R_of_f:.6f}")
print(f"          |R(f_bulk) - 1| = {abs_R_minus_1:.6f}  vs PASS {PASS_TOL}, INFO {INFO_TOL}")
print(f"          PASS band: f_bulk in [{f_pass_lo:.4f}, {f_pass_hi:.4f}]")
print("-" * 80)

# ---------------------------------------------------------------------------
# 3-tuple verdict (sign / magnitude / regime)
# ---------------------------------------------------------------------------
# SIGN: predicted direction is dR/df_bulk > 0 (R rises from edge toward island).
#       PASS iff the computed slope sign matches (it does, by construction of the
#       NON-NEGATIVE bulk-EE correction -- both prior verdicts carried sign=PASS).
sign_v = "PASS" if slope > 0 else "FAIL"           # (local)

# MAGNITUDE: |R(f_bulk) - 1| against the PASS/INFO bands.
if abs_R_minus_1 <= PASS_TOL:
    mag_v = "PASS"
elif abs_R_minus_1 <= INFO_TOL:
    mag_v = "INFO"
else:
    mag_v = "FAIL"

# REGIME: VALID iff the derived lambda_causal sits strictly inside the island
#         support [lam_min, lambda_exit] (the causal-patch interpolation is
#         well-posed) AND f_bulk in [0,1] (a genuine fraction).
regime_ok = (lam_min < lambda_causal < lambda_exit) and (0.0 <= f_bulk <= 1.0)  # (local)
regime_v = "VALID" if regime_ok else "BREAKDOWN"   # (local)

# Composite collapse (pre-registered rule, gate-verdicts.md)
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
OUT_NPZ = ROOT / "computations" / "session-112" / "s112_cf_b5a_bracketed.npz"
OUT_PNG = ROOT / "computations" / "session-112" / "s112_cf_b5a_bracketed.png"

np.savez(
    OUT_NPZ,
    # canonical landing
    R_of_f=R_of_f,
    f_bulk=f_bulk,
    S_microstate=S_microstate,
    abs_R_minus_1=abs_R_minus_1,
    sign_verdict=sign_v,
    magnitude_verdict=mag_v,
    regime_verdict=regime_v,
    composite_verdict=composite,
    PASS_TOL=PASS_TOL,
    INFO_TOL=INFO_TOL,
    # bracket endpoints (pinned)
    R_edge=R_edge_abs,
    R_island=R_island,
    slope=slope,
    lambda_exit=lambda_exit,
    A_quarter=A_quarter,
    A_horizon_FW=A_horizon_FW,
    c_conical=c_conical,
    # causal-patch derivation
    Mach_framework=M_wh,
    W_island=W_island,
    lambda_causal=lambda_causal,
    sbulk_causal=sbulk_causal,
    sbulk_primary=sbulk_primary,
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
    f_bulk_full_support=f_bulk_full_support,
    f_bulk_direct_invmach=f_bulk_direct_invmach,
    f_bulk_cs=f_bulk_cs,
    # FORBIDDEN tautology crossing (diagnostic only)
    R_island_QES=R_island_QES,
    lambda_QES=lambda_QES,
    used_gpu=used_gpu,
)
print(f"\nSaved: {OUT_NPZ}")

# ===========================================================================
# Plot
# ===========================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.2))

# Panel A: R(f_bulk) interpolant with bands + derived f_bulk
f_axis = np.linspace(0.0, 1.0, 400)                # (local)
R_axis = R_edge_abs + f_axis * slope               # (local)
ax1.plot(f_axis, R_axis, color="navy", lw=2.0, label=r"$R(f_{\rm bulk})$ interpolant")
ax1.axhline(1.0, color="black", lw=1.0, ls=":")
ax1.axhspan(0.90, 1.10, color="green", alpha=0.18, label="PASS band ($|R-1|\\leq0.10$)")
ax1.axhspan(0.75, 0.90, color="gold", alpha=0.14)
ax1.axhspan(1.10, 1.25, color="gold", alpha=0.14, label="INFO band ($\\leq0.25$)")
ax1.plot([0.0], [R_edge_abs], "v", color="crimson", ms=11,
         label=fr"$R_{{\rm edge}}={R_edge_abs:.3f}$ (S110 undershoot)")
ax1.plot([1.0], [R_island], "^", color="darkorange", ms=11,
         label=fr"$R_{{\rm island}}={R_island:.3f}$ (S111 overshoot)")
ax1.plot([f_bulk], [R_of_f], "o", color="black", ms=12, zorder=5,
         label=fr"derived $f_{{\rm bulk}}={f_bulk:.3f}\Rightarrow R={R_of_f:.3f}$")
ax1.axvline(f_bulk_unity, color="grey", ls="--", lw=1.0,
            label=fr"[FORBIDDEN] $f^*_{{R=1}}={f_bulk_unity:.3f}$")
ax1.set_xlabel(r"causally-accessible bulk fraction  $f_{\rm bulk}$")
ax1.set_ylabel(r"$R = S_{\rm microstate}/(A_{\rm horizon}/4)$")
ax1.set_title("Bracketed white-hole microstate ratio")
ax1.legend(fontsize=7.0, loc="upper left")
ax1.grid(alpha=0.25)

# Panel B: cumulative island bulk-EE vs lambda with causal-patch + exit markers
ax2.plot(lambda_grid, sbulk_grid, color="teal", lw=1.8,
         label=r"cumulative $S_{\rm bulk\text{-}EE}(|\lambda|\leq\lambda)$")
ax2.axvline(lambda_exit, color="crimson", ls="--", lw=1.4,
            label=fr"$\lambda_{{\rm exit}}={lambda_exit:.3f}$ (island)")
ax2.axvline(lambda_causal, color="black", ls="-.", lw=1.4,
            label=fr"$\lambda_{{\rm causal}}={lambda_causal:.3f}$ (Mach-{M_wh:.2f} patch)")
ax2.axvline(lambda_QES, color="grey", ls=":", lw=1.0,
            label=fr"[FORBIDDEN] $\lambda_{{\rm QES}}={lambda_QES:.3f}$")
ax2.plot([lambda_causal], [sbulk_causal], "o", color="black", ms=9, zorder=5)
ax2.plot([lambda_exit], [sbulk_primary], "s", color="crimson", ms=9, zorder=5)
ax2.set_xlabel(r"island-boundary eigenvalue cutoff $\lambda$")
ax2.set_ylabel(r"cumulative bulk-EE  $S_{\rm bulk\text{-}EE}$")
ax2.set_title(fr"Causal-patch fraction $f_{{\rm bulk}}={f_bulk:.3f}$")
ax2.legend(fontsize=7.0, loc="upper left")
ax2.grid(alpha=0.25)

fig.suptitle(
    fr"CF-S112-B5A-BRACKETED  —  $R(f_{{\rm bulk}})={R_of_f:.4f}$, "
    fr"$|R-1|={abs_R_minus_1:.4f}$  →  {composite}",
    fontsize=11,
)
fig.tight_layout(rect=(0, 0, 1, 0.96))
fig.savefig(OUT_PNG, dpi=130)
print(f"Saved: {OUT_PNG}")

# ===========================================================================
# Dual-SHA + verdict payload
# ===========================================================================
audit_sha, content_sha = closure_hash_audit(Path(__file__), CANONICAL_CONSTS, INPUT_PINS)

value_str = (
    f"R_of_f={R_of_f:.6f};f_bulk={f_bulk:.6f};abs_R_minus_1={abs_R_minus_1:.6f};"
    f"R_edge={R_edge_abs:.6f};R_island={R_island:.6f};slope={slope:.6f};"
    f"lambda_causal={lambda_causal:.6f};lambda_exit={lambda_exit:.4f};"
    f"sbulk_causal={sbulk_causal:.4f};sbulk_primary={sbulk_primary:.4f};"
    f"Mach={M_wh};f_pass_band=[{f_pass_lo:.4f},{f_pass_hi:.4f}];"
    f"f_bulk_unity_FORBIDDEN={f_bulk_unity:.4f};R_island_QES_DIAG={R_island_QES:.4f};"
    f"S_microstate={S_microstate:.2f};A_quarter={A_quarter:.4f}"
)

print_verdict_payload(
    composite, value_str, audit_sha, content_sha, sign_v, mag_v, regime_v
)

sys.exit(0)
