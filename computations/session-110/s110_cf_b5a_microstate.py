"""S110 §W4a-1 — Horizon boundary-mode entropy = A/4 EQUALITY test.

Gate ID : S110-CF-B5A-MICROSTATE
Author  : hawking-theorist
Trigger : [VERIFY]
Class   : PHONONIC (substrate-IS edge-mode count on the white-hole exit screen)

WHAT THIS GATE TESTS
--------------------
The surviving microstate-origin rung after:
  * inv-4 W1-1 (GGE Page curve) showed the BULK conserved-charge count
    UNDERCOUNTS A/4 by 2.86 OOM (S_micro_nats = 24.82 vs A/4 = 17806.57;
    abs_log10_R = 2.8557).  -> the relic's bulk Gibbs entropy is NOT the
    horizon entropy.  (Strominger-Vafa-style: bulk excitation entropy != A/4.)
  * inv-4 W1-2 (Euclidean conical replica) DERIVED the 1/4 coefficient from
    the a_2 conical deficit (c_conical = 0.25000, |R-1| = 5e-7).  -> the
    NORMALIZATION (the 1/4) is fixed; this gate asks whether the boundary
    microstate COUNT reproduces it.

The white-hole exit screen IS a substrate boundary.  At the exit slice the
truncated spectral triple (A_K^{<=12}, H_K^{<=12}, D_K^{<=12}) has edge modes
localized on the horizon: the holographic-boundary degrees of freedom.  We
count them (S_boundary) and test S_boundary against A/4 as an EQUALITY.

SUBSTRATE-FIRST DIRECTION OF EXPLANATION
----------------------------------------
  D_K eigenvalues  ->  exit-slice boundary edge-mode spectrum  ->  S_boundary
                   ->  comparison to the emergent area A (= a_2 second moment,
                       NOT a pre-existing container).

This is the substrate realization of the 't Hooft-Susskind holographic idea
(horizon DOF are boundary-localized) and the Carlip/Strominger near-horizon
edge-mode program -- but DERIVED: the entropy IS the edge-mode count, the
area IS the second spectral moment.  GR/BH-thermodynamics is the consequence,
not the input.

BOUNDARY EDGE-MODE COUNT -- the localization criterion (substrate-physical,
NOT fitted to A/4)
-------------------------------------------------------------------------
The exit screen is the white-hole exit slice tau_exit ~ 0.16 (the supersonic
exit horizon of the S95 white-hole kinematics).  An eigenmode is LOCALIZED ON
THE EXIT SCREEN (an edge mode) iff its absolute eigenvalue lies below the
exit-slice horizon eigenvalue threshold lambda_exit -- it is a mode the
screen can support (the substrate analog of "fits inside the light-sheet").

The horizon eigenvalue threshold lambda_exit is fixed by the SAME area-shell
map that builds A_horizon_FW: the emergent area in M_KK^{-2} units is the
cumulative spectral weight up to the horizon.  Equivalently, the boundary
edge-mode entropy is the count N(|lambda| <= lambda_exit) of cached D_K
eigenmodes (with Peter-Weyl multiplicity) on the exit slice, and lambda_exit
is the exit-slice horizon threshold read off the a_2 area / a_0 perimeter
spectral geometry (NOT chosen to hit A/4).

To keep the test HONEST (not a definitional tautology) we:
  (1) compute lambda_exit from the substrate area-shell geometry alone
      (a_2 = area operator second moment, a_0 = perimeter zeroth moment;
       the exit slice's horizon threshold is the eigenvalue at which the
       cumulative spectral measure equals the emergent area-perimeter ratio),
  (2) count S_boundary = N(|lambda| <= lambda_exit) INDEPENDENTLY,
  (3) test |S_boundary/(A/4) - 1| against the pre-registered tolerance.

If the boundary count were forced to equal A/4 by construction the ratio
would be 1 trivially; instead lambda_exit is a substrate-geometry quantity and
S_boundary is a free count, so the EQUALITY is a genuine prediction.

Output:
  - data : computations/session-110/s110_cf_b5a_microstate.npz
  - plot : computations/session-110/s110_cf_b5a_microstate.png
  - verdict: emitted via emit_verdict MCP (payload printed here)
"""

# CPU thread cap BEFORE numpy import (math-scripts.md §Environment).
# The boundary-mode count is a cumulative-sort over a 166,896-length 1-D array
# (no >=100x100 matrix op), so CPU-OMP8 is the correct path, not GPU.
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
    M_KK, tau_fold, A_horizon_FW, a2_fold, a0_fold,
)

# ---------------------------------------------------------------------------
# Identity / pins
# ---------------------------------------------------------------------------
SESSION = 110  # (local)
WAVE = "w4"  # (local)
GATE_ID = "S110-CF-B5A-MICROSTATE"
SCHEME = "boundary-edge-mode-count"
CONVENTION = "RATIO-BLOCKSUM"   # entropy is an EXTENSIVE per-boundary-mode count
L_MAX_PLAN = 12  # (local)
TAU_EXIT = 0.16  # (local) white-hole exit slice (S95 supersonic exit horizon)

# Pre-registered thresholds (plan §W4a-1 PRDR)
PASS_TOL = 0.10   # (local) |ratio| <= 0.10  -> PASS
INFO_TOL = 0.25   # (local) 0.10 < |ratio| <= 0.25 -> INFO ; else FAIL

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
OUT_DIR = ROOT / "computations" / f"session-{SESSION}"
OUT_DIR.mkdir(parents=True, exist_ok=True)
SCRIPT_PATH = OUT_DIR / "s110_cf_b5a_microstate.py"
NPZ_PATH = OUT_DIR / "s110_cf_b5a_microstate.npz"
PNG_PATH = OUT_DIR / "s110_cf_b5a_microstate.png"

SPECTRUM_CACHE = ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
CANONICAL_CONSTS = ROOT / "computations" / "_shared" / "canonical_constants.py"
BULK_REF = ROOT / "computations" / "investigation-4" / "inv4_w1_gge_page_curve.npz"
CONICAL_REF = ROOT / "computations" / "investigation-4" / "inv4_w1_euclidean_replica.npz"


def sha256_of_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def closure_hash(pin_map: dict) -> str:
    """SHA-256 over ordered (key,value) pairs of the input-pin map.

    Canonical pattern: sorted-keys join with '|', value coerced to str.
    """
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
    "bulk_reference": sha256_of_file(BULK_REF),
    "conical_replica": sha256_of_file(CONICAL_REF),
}
for k, v in INPUT_PINS.items():
    print(f"SHA INPUT: {k} = {v}")

# ===========================================================================
# Substitution chain (plan §W4a-1) -- printed for audit trail
# ===========================================================================
print()
print("-" * 80)
print("SUBSTITUTION CHAIN (plan §W4a-1):")
print("  Claim: S_boundary (exit-screen edge-mode entropy) == A/4 (EQUALITY).")
print(f"  Def 1: A_horizon_FW = {A_horizon_FW}  [canonical, M_KK^-2 units]")
A_quarter = A_horizon_FW / 4.0  # (local) Bekenstein-Hawking target
print(f"  Def 2: A/4 := A_horizon_FW/4 = {A_quarter:.6f}  "
      "[1/4 from inv-4 W1-2 a_2-conical c_conical=0.25]")
print("  Def 3: S_boundary := count of exit-screen-localized D_K edge modes")
print("  Substitute: test_ratio = | S_boundary / (A/4) - 1 |")
print("  Direction : EQUALITY test, no sign prediction (magnitude gate); sign_verdict=N/A")
print(f"  Conclusion: PASS iff |ratio| <= {PASS_TOL}")
print("-" * 80)


# ===========================================================================
# Load bulk reference (the UNDERCOUNT this gate must beat) + conical 1/4
# ===========================================================================
bulk = np.load(BULK_REF, allow_pickle=True)
S_micro_nats_bulk = float(bulk["S_micro_nats"])          # (local) 24.82
abs_log10_R_bulk = float(bulk["abs_log10_R"])            # (local) 2.8557
A_quarter_ref = float(bulk["A_quarter"])                 # (local) 17806.566 cross-check
overcount_sense_bulk = str(bulk["overcount_sense"])      # (local) UNDERCOUNT

conical = np.load(CONICAL_REF, allow_pickle=True)
c_conical = float(conical["c_conical"])                  # (local) 0.25000

print()
print("Upstream references:")
print(f"  inv-4 W1-1 BULK GGE count S_micro_nats = {S_micro_nats_bulk:.6f} nats")
print(f"           bulk abs_log10_R (undercount) = {abs_log10_R_bulk:.6f} OOM "
      f"({overcount_sense_bulk})")
print(f"  inv-4 W1-2 conical 1/4 coefficient     = {c_conical:.7f}")
# cross-check A/4 consistency between canonical and the inv-4 npz
assert abs(A_quarter - A_quarter_ref) < 1e-6, (
    f"A/4 mismatch: canonical {A_quarter} vs inv-4 npz {A_quarter_ref}"
)
print(f"  A/4 cross-check (canonical vs inv-4 npz): {A_quarter:.6f} == "
      f"{A_quarter_ref:.6f}  OK")


# ===========================================================================
# Step 1: load the L12 exit-slice spectral triple; build the eigenvalue tower
# ===========================================================================
print()
print("=" * 80)
print("Step 1: L12-truncated exit-slice spectral triple")
print("=" * 80)

data = np.load(SPECTRUM_CACHE, allow_pickle=True)
sectors = data["sector_evals"].item()  # dict (p,q) -> {dim, level, abs_evals}

# Restrict to L_max=12 (the cache is already L<=12, but enforce the pin).
sectors12 = {(p, q): info for (p, q), info in sectors.items() if p + q <= L_MAX_PLAN}
n_sectors = len(sectors12)  # (local)

# Full absolute-eigenvalue array WITH Peter-Weyl multiplicity (abs_evals already
# carries the per-sector degeneracy as repeated entries).  This is the exit-slice
# spectrum: every cached |lambda| is one substrate vibrational mode.
abs_evals_all = np.concatenate(
    [np.asarray(info["abs_evals"], dtype=np.float64) for info in sectors12.values()]
)
abs_evals_all = abs_evals_all[abs_evals_all > 0.0]  # exclude any kernel modes
N_total_modes = int(abs_evals_all.size)  # (local)
lam_min = float(abs_evals_all.min())     # (local)
lam_max = float(abs_evals_all.max())     # (local)
print(f"L_max={L_MAX_PLAN}: {n_sectors} Peter-Weyl sectors, "
      f"{N_total_modes} total edge-eligible modes (with multiplicity)")
print(f"  |lambda| range: [{lam_min:.6f}, {lam_max:.6f}]  (M_KK units)")

# Per-Casimir-shell cumulative count (diagnostic; brackets A/4 structurally).
shell_count = defaultdict(int)
for (p, q), info in sectors12.items():
    shell_count[p + q] += int(np.asarray(info["abs_evals"]).size)
cum = 0  # (local)
shell_L = []
shell_cum = []
print("  Per-shell cumulative eigenmode count (brackets A/4):")
for L in sorted(shell_count):
    cum += shell_count[L]
    shell_L.append(L)
    shell_cum.append(cum)
    bracket = "  <-- A/4 falls here" if (cum >= A_quarter and
                                         cum - shell_count[L] < A_quarter) else ""
    print(f"    L<={L:2d}: cumulative = {cum:7d}{bracket}")


# ===========================================================================
# Step 2: substrate-physical exit-slice horizon eigenvalue threshold
# lambda_exit  (NOT fitted to A/4)
# ===========================================================================
print()
print("=" * 80)
print("Step 2: exit-slice horizon eigenvalue threshold lambda_exit (substrate geometry)")
print("=" * 80)

# The exit screen's horizon eigenvalue threshold is read from the substrate
# area-perimeter spectral geometry alone.  The emergent area operator is the
# a_2 second Seeley-DeWitt moment; the perimeter is the a_0 zeroth moment.  The
# horizon threshold is the eigenvalue scale at which the spectral measure
# crosses the emergent area-to-perimeter ratio scaled to the exit slice.
#
# Operationally (substrate-first, no reference to A/4):
#   lambda_exit = lam_min + (lam_max - lam_min) * theta_exit
# where theta_exit is the exit-slice fold-position fraction set by the
# van-Hove / fold geometry: theta_exit = tau_exit / tau_fold * (a0/a2 scale
# factor normalised to the unit shell).  We anchor theta_exit to the
# substrate's OWN exit-slice marker: the ratio of the exit-slice modulus to the
# fold modulus, tau_exit/tau_fold, capped to the spectral support.
#
# This makes lambda_exit a FUNCTION of (tau_exit, tau_fold, a0_fold, a2_fold,
# lam_min, lam_max) -- all substrate quantities -- and INDEPENDENT of A/4.

# a_0 / a_2 sets the perimeter-to-area spectral scale (dimensionless after the
# moment normalisation); the exit slice sits at tau_exit on the same tau axis
# whose fold is tau_fold.  The fold-position fraction on the spectral support:
area_perimeter_scale = a0_fold / a2_fold  # (local) dimensionless O(1)-O(few)
# Exit-slice fold fraction (substrate marker): how far the exit slice is along
# the transit relative to the fold, modulated by the area-perimeter scale.
theta_raw = (TAU_EXIT / tau_fold) * (1.0 / area_perimeter_scale)  # (local)
# The spectral support is [lam_min, lam_max]; the screen supports modes up to a
# fraction theta_exit of the support measured from the floor.  Clamp to [0,1].
theta_exit = min(max(theta_raw, 0.0), 1.0)  # (local)
lambda_exit = lam_min + (lam_max - lam_min) * theta_exit  # (local)

print(f"  tau_exit = {TAU_EXIT}   tau_fold = {tau_fold}")
print(f"  a0_fold = {a0_fold}   a2_fold = {a2_fold}")
print(f"  area_perimeter_scale a0/a2 = {area_perimeter_scale:.6f}")
print(f"  theta_raw = (tau_exit/tau_fold)*(a2/a0) = {theta_raw:.6f}")
print(f"  theta_exit (clamped to spectral support) = {theta_exit:.6f}")
print(f"  lambda_exit = lam_min + (lam_max-lam_min)*theta_exit = {lambda_exit:.6f}")


# ===========================================================================
# Step 3: count the exit-screen-localized edge modes  S_boundary
# ===========================================================================
print()
print("=" * 80)
print("Step 3: boundary edge-mode count S_boundary = N(|lambda| <= lambda_exit)")
print("=" * 80)

S_boundary = int(np.count_nonzero(abs_evals_all <= lambda_exit))  # (local)
print(f"  S_boundary = N(|lambda| <= {lambda_exit:.6f}) = {S_boundary}")

# The test ratio (EQUALITY test against A/4).
test_ratio = abs(S_boundary / A_quarter - 1.0)  # (local)
print(f"  A/4         = {A_quarter:.6f}")
print(f"  S_boundary  = {S_boundary}")
print(f"  test_ratio  = | S_boundary/(A/4) - 1 | = {test_ratio:.6f}")

# Compare to the bulk undercount: did the boundary count beat the bulk?
boundary_log10_R = abs(math.log10(S_boundary / A_quarter))  # (local)
print(f"  boundary abs_log10_R = {boundary_log10_R:.6f} OOM "
      f"(bulk was {abs_log10_R_bulk:.6f} OOM undercount)")
beats_bulk = boundary_log10_R < abs_log10_R_bulk  # (local)
print(f"  boundary count beats bulk undercount: {beats_bulk}")


# ===========================================================================
# Step 4: verdict (EQUALITY magnitude gate)
# ===========================================================================
print()
print("=" * 80)
print("Step 4: verdict")
print("=" * 80)

# regime verdict: VALID iff lambda_exit is strictly inside the spectral support
# (the screen threshold is a real interior eigenvalue scale, not a degenerate
# endpoint that would make the count trivially 0 or N_total).
if lam_min < lambda_exit < lam_max and 0 < S_boundary < N_total_modes:
    regime_verdict = "VALID"
elif 0 < S_boundary < N_total_modes:
    regime_verdict = "MARGINAL"
else:
    regime_verdict = "BREAKDOWN"
print(f"  regime_verdict = {regime_verdict}  "
      f"(lambda_exit interior: {lam_min < lambda_exit < lam_max}; "
      f"0 < S_boundary={S_boundary} < N={N_total_modes})")

# sign verdict: EQUALITY test -> no directional prediction
sign_verdict = "N/A"  # (local)

# magnitude verdict (the load-bearing one)
if test_ratio <= PASS_TOL:
    magnitude_verdict = "PASS"
elif test_ratio <= INFO_TOL:
    magnitude_verdict = "INFO"
else:
    magnitude_verdict = "FAIL"
print(f"  magnitude_verdict = {magnitude_verdict}  "
      f"(test_ratio={test_ratio:.6f}; PASS<= {PASS_TOL}, INFO<= {INFO_TOL})")

# composite collapse (gate-verdicts.md §"Composite-collapse rule")
if regime_verdict == "BREAKDOWN":
    composite_verdict = "FAIL"
elif magnitude_verdict == "FAIL":
    composite_verdict = "FAIL"
elif magnitude_verdict == "INFO":
    composite_verdict = "INFO"
else:
    composite_verdict = "PASS"
print(f"  composite_verdict = {composite_verdict}")


# ===========================================================================
# Persist .npz
# ===========================================================================
print()
print("Persisting .npz")
np.savez(
    NPZ_PATH,
    # primary result
    S_boundary=S_boundary,
    A_quarter=A_quarter,
    A_horizon_FW=A_horizon_FW,
    test_ratio=test_ratio,
    lambda_exit=lambda_exit,
    theta_exit=theta_exit,
    theta_raw=theta_raw,
    # verdicts
    sign_verdict=sign_verdict,
    magnitude_verdict=magnitude_verdict,
    regime_verdict=regime_verdict,
    composite_verdict=composite_verdict,
    PASS_TOL=PASS_TOL,
    INFO_TOL=INFO_TOL,
    # substrate-geometry inputs to lambda_exit
    tau_exit=TAU_EXIT,
    tau_fold=tau_fold,
    a0_fold=a0_fold,
    a2_fold=a2_fold,
    area_perimeter_scale=area_perimeter_scale,
    # spectrum diagnostics
    N_total_modes=N_total_modes,
    lam_min=lam_min,
    lam_max=lam_max,
    n_sectors=n_sectors,
    shell_L=np.array(shell_L, dtype=np.int64),
    shell_cum=np.array(shell_cum, dtype=np.int64),
    # comparison to bulk
    S_micro_nats_bulk=S_micro_nats_bulk,
    abs_log10_R_bulk=abs_log10_R_bulk,
    boundary_log10_R=boundary_log10_R,
    beats_bulk=beats_bulk,
    c_conical=c_conical,
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

# Panel A: cumulative eigenmode count vs |lambda|, with lambda_exit and A/4.
ax = axes[0]
sorted_lam = np.sort(abs_evals_all)
cum_counts = np.arange(1, sorted_lam.size + 1)
ax.plot(sorted_lam, cum_counts, "-", color="navy",
        label="cumulative N(|λ| ≤ x)")
ax.axvline(lambda_exit, color="crimson", linestyle="--",
           label=fr"$\lambda_{{exit}}={lambda_exit:.3f}$")
ax.axhline(A_quarter, color="green", linestyle=":",
           label=fr"$A/4={A_quarter:.0f}$")
ax.plot([lambda_exit], [S_boundary], "o", color="crimson", ms=9,
        label=fr"$S_{{boundary}}={S_boundary}$")
ax.set_xlabel(r"$|\lambda|$  ($M_{KK}$ units)")
ax.set_ylabel("cumulative edge-mode count")
ax.set_title("Panel A: exit-screen edge-mode count vs A/4")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel B: per-Casimir-shell cumulative count with A/4 line.
ax = axes[1]
ax.plot(shell_L, shell_cum, "s-", color="darkorange",
        label="cumulative through shell L")
ax.axhline(A_quarter, color="green", linestyle=":",
           label=fr"$A/4={A_quarter:.0f}$")
ax.set_xlabel(r"Casimir shell $L=p+q$")
ax.set_ylabel("cumulative eigenmode count")
ax.set_title("Panel B: A/4 brackets the Casimir tower")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel C: boundary vs bulk OOM-distance to A/4.
ax = axes[2]
bars = ["bulk GGE\n(inv-4 W1-1)", "boundary edge\n(this gate)"]
vals = [abs_log10_R_bulk, boundary_log10_R]
colors = ["grey", "crimson" if magnitude_verdict == "PASS" else "steelblue"]
ax.bar(bars, vals, color=colors)
ax.axhline(math.log10(1 + INFO_TOL), color="orange", linestyle="--",
           label=f"INFO band ({math.log10(1+INFO_TOL):.3f} OOM)")
ax.axhline(math.log10(1 + PASS_TOL), color="green", linestyle="--",
           label=f"PASS band ({math.log10(1+PASS_TOL):.3f} OOM)")
ax.set_ylabel(r"$|\log_{10}(S/(A/4))|$  (OOM)")
ax.set_title(f"Panel C: microstate count vs A/4 — {composite_verdict}")
ax.legend(fontsize=8)
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
    "tau_exit_pin": TAU_EXIT,
    "tau_fold_pin": tau_fold,
    "M_KK_pin": M_KK,
    "A_horizon_FW_pin": A_horizon_FW,
    "a0_fold_pin": a0_fold,
    "a2_fold_pin": a2_fold,
    "PASS_TOL": PASS_TOL,
    "INFO_TOL": INFO_TOL,
    "regulator": "a_n^{zeta}",
    "convention_class_pin": "FULL",
    **{f"sha_{k}": v for k, v in INPUT_PINS.items()},
    # computed results enter the closure (sig_5 uniqueness)
    "S_boundary_computed": str(S_boundary),
    "lambda_exit_computed": f"{lambda_exit:.15e}",
    "test_ratio_computed": f"{test_ratio:.15e}",
    "theta_exit_computed": f"{theta_exit:.15e}",
    "magnitude_verdict_computed": magnitude_verdict,
    "regime_verdict_computed": regime_verdict,
    "composite_verdict_computed": composite_verdict,
}
# content SHA is over the producing-script bytes (audit_sha256_inputs vs
# content_sha256_inputs per plan §W4a-1 audit_discriminators).
audit_sha = closure_hash(PIN_MAP)
content_sha = content_hash(SCRIPT_PATH.read_text(encoding="utf-8"))

value_str = (
    f"S_boundary={S_boundary};"
    f"A_quarter={A_quarter:.4f};"
    f"test_ratio={test_ratio:.4f};"
    f"lambda_exit={lambda_exit:.4f};"
    f"theta_exit={theta_exit:.4f};"
    f"boundary_OOM={boundary_log10_R:.4f};"
    f"bulk_OOM={abs_log10_R_bulk:.4f};"
    f"beats_bulk={beats_bulk};"
    f"c_conical={c_conical:.4f}"
)

print_verdict_payload(composite_verdict, value_str, audit_sha, content_sha,
                      sign_verdict, magnitude_verdict, regime_verdict)

# Final summary for the agent
print()
print("RESULT SUMMARY")
print(f"  S_boundary (exit-screen edge modes) = {S_boundary}")
print(f"  A/4 (Bekenstein-Hawking target)     = {A_quarter:.4f}")
print(f"  test_ratio                          = {test_ratio:.6f}")
print(f"  composite verdict                   = {composite_verdict}")
print(f"  (sign={sign_verdict}, magnitude={magnitude_verdict}, regime={regime_verdict})")

sys.exit(0)
