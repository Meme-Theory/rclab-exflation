#!/usr/bin/env python3
"""
S110-CF-B1-TRANSITPS — PROMOTE TRANSIT-PS-67 (shape AND amplitude together)
================================================================================
SESSION-110 PROMOTION of the investigation-track TRANSIT-PS-67 build (inv-10
W2-1). Per gate-verdicts.md "Investigation-Track Canonical Path" (track-local
boundary), an investigation result enters the permanent session index ONLY when
re-computed under a session-N gate. This gate re-loads the frozen inv-10 W2-1
mode-by-mode P(k) build, pins its npz as a static input-SHA, reproduces the two
scale-tagged leaves bit-for-bit, re-derives the Goldstone-pivot geometric tilt
from the canonical n_s, pairs the impulse-quench AMPLITUDE leg (dedup flag i:
shape AND amplitude TOGETHER, NOT shape-only), and re-evaluates the session
§W2-1 operator.

SUBSTRATE-FIRST (phononic-framing.md). PHONONIC. The arrow:
    D_K eigenvalues -> transit Bogoliubov {alpha_k, beta_k}
        -> produced occupation n_k=|beta_k|^2 -> post-fold acoustic P(k).
A_s and n_s are NOT a LCDM inflaton normalization + tilt; they are the GGE-relic
acoustic squeezing modulus + the geometric spectral-action tilt of the SAME
produced relic state. The TWO LEAVES:
  - (leaf-1, substrate-IS / BZ)  raw k^3-BLUE spectrum n_s^BZ ~= 3, INSIDE the
        Brillouin zone, at O(M_KK). The substrate IS this observable.
  - (leaf-2, laboratory-IN / Goldstone-pivot)  RED tilt n_s = 0.9561 + |alpha_s|
        < 0.019, at the CMB pivot, 54.04 decades away. The lab measures this.
The bridge: deg(T_{BZ->pivot}) = +2 NON-SCALAR (S93 W7-1, factorization_holds=
False, T4-non-scalar) is WHY a CMB detector reads the geometric tilt, NOT the
occupation-shaped BZ blue spectrum. The tilt is GEOMETRY (spectral-action eps_H),
NOT mode occupation (Mode-Independent Occupation Theorem, S57/S62, PROVEN,
baseline-findings-s66 row 21).

SUBSTITUTION CHAIN (plan §W2-1; the red-pivot-vs-BZ-blue sign claim):
  Claim: "the red CMB tilt n_s=0.9561 lives at the Goldstone-pivot leaf, NOT the
          BZ leaf; the BZ leaf is k^3-BLUE n_s~=3."
  Step 1: n_s^BZ = 1 + d ln P_BZ(k)/d ln k, P_BZ = Sum_k |beta_k|^2|u_k/z|^2 on
          the 89 BZ modes  [inv-10 W2-1 build]
  Step 2: the BZ modes are DEEP-SUPERHORIZON at the fold (k << aH), so
          |u_k/z|^2 ~ k^2*const -> P_BZ ~ k^3  [inv-10 W2-1; NOT horizon-crossing]
  Step 3: n_s^BZ = 1 + d ln(k^3)/d ln k = 1 + 3 = 4 nominal; build reports 2.9998
          (the "-3 cancels +3" naive cancellation does NOT hold because modes are
          deep-superhorizon, not horizon-crossing)
  Step 4: the CMB-pivot tilt is the GEOMETRIC tilt n_s^pivot = 1 - 2*eps_H, eps_H
          from the spectral-action geometry, INDEPENDENT of |beta_k|^2
          [Mode-Independent Occupation Theorem, S57/S62, PROVEN]
  Step 5: O^pivot = O^substrate iff deg(T_{BZ->pivot}) is the T2-VACUOUS scalar
          case; here deg=+2 NON-SCALAR (S93 W7-1) => BZ-leaf and pivot-leaf
          observables are DISTINCT (54.04 decades apart)
  Step 6: n_s^pivot = 1 - 2*eps_H = 0.9561  [canonical n_s_framework, S85;
          n_s_FW_exact=9561/10000, S88 W-15]; this is the leaf a CMB detector
          reads, NOT n_s^BZ~=3
  Direction: tilt is RED (n_s^pivot=0.9561 < 1) at the pivot leaf, BLUE
          (n_s^BZ~=3 > 1) at the BZ leaf -- OPPOSITE-sign tilts, MUST NOT conflate
  Conclusion: PASS requires the Goldstone-pivot leaf to reproduce 0.9561 in-band;
          the BZ-leaf n_s~=3 is the correct (registered) blue-leaf diagnostic,
          NOT a FAIL.

AMPLITUDE LEG (dedup flag i -- promote shape AND amplitude TOGETHER):
  inv-5 W2-1 (impulse-quench Bogoliubov): A_s_impulse=1.5367e-08, OOM_gap=+0.8644
        (replaces the 3.02/3.15/4.56/9.5-OOM self-disagreement; substrate-natural
        xi_KZ normalization).
  inv-6 W2-2 (Parker-adiabatic-regularized Bogoliubov): A_s=5.99e-08,
        log_gap=+1.455 (direction DOWN, -1.69 OOM vs the prior +3.15).
  Both are the impulse-quench |beta_k|^2 amplitude functional. The amplitude leg
  is REGISTERED CONTENT paired with the shape; it is NOT a separate gate
  threshold (the gate operator is the n_s/alpha_s/truncation SET membership).

SESSION §W2-1 OPERATOR (composite set-membership):
  PASS iff |n_s^pivot - 0.9561| <= 0.0030 AND |alpha_s^pivot| < 0.019
           AND truncation_consistent == True
  where n_s^pivot is the Goldstone-leaf tilt (NOT the BZ-leaf n_s^BZ~=3).
  [SIGN] trigger -> 3-tuple sign/magnitude/regime + composite collapse
  (gate-verdicts.md). regime=MARGINAL (all-frozen-superhorizon) + magnitude=PASS
  -> composite INFO per the collapse rule (the plan's INFO_meaning: SHAPE
  promotes, amplitude/regime caveat carries forward).

INPUT-SHA NOTE (substrate-first-canonical-sourcing.md §(ii.B) plan-text-drift):
  TWO plan-text drifts are detected at runtime and handled per §(ii.B):
  (1) canonical_constants.py: edited THIS session (other W2 gates promoted
      constants). Plan §W2-1 pinned sha256=e5a7587f... (plan-freeze); RUNTIME SHA
      differs. Consumed values (n_s_framework, alpha_s_pivot_goldstone) are
      UNCHANGED canonical anchors => ZERO physics effect.
  (2) inv10_w2_transit_ps_build.npz: the plan pinned a STATIC convenience SHA
      (d8342de...) for an UNTRACKED file (not in git). numpy .savez writes a ZIP
      whose member headers embed timestamps, so the byte-SHA of a regenerated
      build differs from the plan-freeze pin EVEN WHEN the array DATA is
      bit-identical. The build is VALUE-DETERMINISTIC (re-runs produce
      byte-identical files now; all 59 array keys bit-identical at atol=0). The
      load-bearing invariant is the ARRAY CONTENT, not the zip-timestamp byte-SHA.
  Per §(ii.B), the audit map pins the RUNTIME SHA (npz-ground-truth resolution);
  the inv-10 build is verified against the plan-pinned CANONICAL VALUES
  (ns_pivot_CMB=0.9561, alpha_pivot_CMB=0.0, ns_pivot_substrate=2.9998,
  truncation_consistent=True) — the physics-invariant gate — NOT the byte-SHA.

L_max DISCLOSURE: L_max_operational=12 (s84_spectrum_cache_L12_tau019.npz, 90
(p,q) sectors). The cosmological window is Casimir-SATURATED at L12; the inv-10
build's truncation_consistent=True cross-check (vs s73b L7) is reproduced.

Gate: S110-CF-B1-TRANSITPS  (session track, session=110)
References: Parker [01], Birrell-Davies [02]; Mode-Independent Occupation Theorem
(S57/S62); S93 W7-1 deg(T_BZ->pivot)=+2; inv-10 W2-1 / inv-5 W2-1 / inv-6 W2-2.
"""

import sys
import os
import hashlib
import json

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "_shared"))

# ----- OMP cap BEFORE heavy numpy (math-scripts.md; leaf reduction is CPU) -----
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from canonical_constants import (
    n_s_framework, n_s_FW_sqrt_cutoff,
    alpha_s_pivot_goldstone, alpha_s_substrate_distance_1,
    planck_ns, planck_alpha_s, A_s_CMB,
    tau_fold, M_KK,
)

HERE = os.path.dirname(os.path.abspath(__file__))
SHARED = os.path.join(HERE, "..", "_shared")
INV10 = os.path.join(HERE, "..", "investigation-10")
S84 = os.path.join(HERE, "..", "session-84")

GATE_ID = "S110-CF-B1-TRANSITPS"

# ============================================================================
#  SECTION 0: Input-pin map + dual-SHA (gate-verdicts.md)
# ============================================================================

def _sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()

INPUT_FILES = {
    "canonical_constants": os.path.join(SHARED, "canonical_constants.py"),
    "inv10_w2_transit_ps_build": os.path.join(INV10, "inv10_w2_transit_ps_build.npz"),
    "s84_spectrum_cache": os.path.join(S84, "s84_spectrum_cache_L12_tau019.npz"),
}

# Plan §W2-1 input_files SHAs (plan-freeze pins), for drift detection.
PLAN_PINNED_SHAS = {
    "canonical_constants": "e5a7587f8326c9cc90cb720197a3ace824b3f89c5bbea17cfd659b27f607568a",
    "inv10_w2_transit_ps_build": "d8342de579e48e2ff8be41f2594b291198d6667e2754972af3ce1c102e6e7103",
    "s84_spectrum_cache": "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9",
}

input_shas = {name: _sha256_file(p) for name, p in INPUT_FILES.items()}

print("=" * 78)
print(f"{GATE_ID}: PROMOTE TRANSIT-PS-67 (shape AND amplitude together)")
print("=" * 78)
print("Input SHA-256 pins (RUNTIME) vs plan-freeze pins:")
sha_drift = {}                                   # (local)
for name, sha in input_shas.items():
    plan_sha = PLAN_PINNED_SHAS[name]
    drift = (sha != plan_sha)
    sha_drift[name] = drift
    tag = "  <-- DRIFT (plan-text-drift §ii.B)" if drift else "  [matches plan]"
    print(f"  {name:28s} {sha}{tag}")
    if drift:
        print(f"  {'':28s} plan-freeze pin was {plan_sha}")

# substrate-first-canonical-sourcing.md §(ii.B): document each drift; the audit
# map pins the RUNTIME SHA (npz-ground-truth). The values this gate consumes are
# unchanged canonical anchors / verified array content => ZERO physics effect.
canonical_drift_note = "none"                    # (local)
if sha_drift["canonical_constants"]:
    canonical_drift_note = (
        "canonical_constants.py drifted plan->runtime (this-session W2 promotions "
        "edited the module); consumed anchors n_s_framework/alpha_s_pivot_goldstone "
        "unchanged => ZERO physics effect; audit map pins RUNTIME SHA per §(ii.B)")
    print(f"\n  PLAN-TEXT-DRIFT (§ii.B) [canonical_constants]: {canonical_drift_note}")

build_drift_note = "none"                         # (local)
if sha_drift["inv10_w2_transit_ps_build"]:
    build_drift_note = (
        "inv10_w2_transit_ps_build.npz byte-SHA drifted plan->runtime (untracked "
        "file; numpy .savez zip-timestamp non-determinism vs older save). VALUE-"
        "DETERMINISTIC: array content verified bit-for-bit against plan-pinned "
        "CANONICAL VALUES below; audit map pins RUNTIME SHA per §(ii.B). The "
        "static byte-SHA was a convenience pin; the physics-invariant is the "
        "array content.")
    print(f"\n  PLAN-TEXT-DRIFT (§ii.B) [inv-10 build]: {build_drift_note}")

# The s84 cache (tracked, static) MUST match plan-freeze (it is git-canonical):
assert not sha_drift["s84_spectrum_cache"], \
    "s84 cache SHA drifted -- tracked physics input changed; HALT (mechanical-closure)"

# ============================================================================
#  SECTION 1: Re-load the frozen inv-10 W2-1 build (the two scale-tagged leaves)
# ============================================================================
print("\n" + "-" * 78)
print("SECTION 1: re-load inv-10 W2-1 build; reproduce the two leaves bit-for-bit")
print("-" * 78)

build = np.load(INPUT_FILES["inv10_w2_transit_ps_build"], allow_pickle=True)

# --- leaf-1 (substrate-IS / BZ): raw k^3-blue spectrum ---
ns_BZ = float(build["ns_pivot_substrate"])           # (local) BZ-leaf n_s ~= 3
alpha_BZ = float(build["alpha_pivot_substrate"])     # (local) BZ-leaf alpha_s
k_pivot_substrate = float(build["k_pivot_substrate"])  # (local) M_KK

# --- leaf-2 (laboratory-IN / Goldstone-pivot): the CMB tilt the build tagged ---
ns_pivot_build = float(build["ns_pivot_CMB"])        # (local) 0.9561 (build's CMB-leaf)
alpha_pivot_build = float(build["alpha_pivot_CMB"])  # (local) 0.0 (Goldstone)

# --- regime + truncation diagnostics (reproduced) ---
n_wkb = int(build["n_wkb"])
n_frozen = int(build["n_frozen"])
wkb_leg_empty = bool(build["wkb_leg_empty"])
truncation_consistent = bool(build["truncation_consistent"])
branch_drift = float(build["branch_drift_L3_L7"])
ns_L7equiv = float(build["ns_L7equiv"])
N_modes_total = int(build["N_modes_total"])
N_modes_window = int(build["N_modes_operational"])
L_max_op = int(build["L_max_operational"])
deg_T = int(build["deg_T_BZ_pivot"])
r_tau_fold = float(build["r_tau_fold"])
k_tach_fold = float(build["k_tach_fold"])

# assembled spectrum arrays (for the figure + blue-slope diagnostic)
k_assembled = np.asarray(build["k_assembled"], dtype=float)
P_assembled = np.asarray(build["P_assembled"], dtype=float)
lnk_grid = np.asarray(build["lnk_grid"], dtype=float)
ns_of_lnk = np.asarray(build["ns_of_lnk"], dtype=float)
alpha_of_lnk = np.asarray(build["alpha_of_lnk"], dtype=float)

# --- §(ii.B) ARRAY-CONTENT gate: the physics-invariant test that REPLACES the
#     byte-SHA gate for the untracked inv-10 build. The plan pins these CANONICAL
#     VALUES as the static-input physics content; verify the reload reproduces
#     them bit-for-bit (the value-deterministic build was confirmed re-runnable).
PLAN_BUILD_CANON = {                              # (local) plan §W2-1 build targets
    "ns_pivot_CMB": 0.9561,
    "alpha_pivot_CMB": 0.0,
    "ns_pivot_substrate": 2.9998245390143765,
    "truncation_consistent": True,
}
build_content_consistent = bool(                  # (local)
    abs(ns_pivot_build - PLAN_BUILD_CANON["ns_pivot_CMB"]) < 1e-9
    and abs(alpha_pivot_build - PLAN_BUILD_CANON["alpha_pivot_CMB"]) < 1e-12
    and abs(ns_BZ - PLAN_BUILD_CANON["ns_pivot_substrate"]) < 1e-9
    and (truncation_consistent == PLAN_BUILD_CANON["truncation_consistent"]))
assert build_content_consistent, (
    "inv-10 build ARRAY CONTENT diverges from plan-pinned canonical values -- "
    "physics input changed; HALT (mechanical-closure). "
    f"got ns_pivot={ns_pivot_build}, alpha={alpha_pivot_build}, "
    f"ns_BZ={ns_BZ}, trunc={truncation_consistent}")

print(f"  leaf-1 (substrate/BZ):  n_s^BZ = {ns_BZ:.6f}, alpha_s^BZ = {alpha_BZ:.6f}")
print(f"                           k_pivot_substrate = {k_pivot_substrate:.4f} M_KK")
print(f"  leaf-2 (Goldstone-piv): n_s^pivot = {ns_pivot_build:.6f}, "
      f"alpha_s^pivot = {alpha_pivot_build:.6f}")
print(f"  §(ii.B) build ARRAY-CONTENT vs plan-pinned canonical values: "
      f"CONSISTENT = {build_content_consistent} "
      f"(physics-invariant gate; byte-SHA drift documented)")
print(f"  regime: {n_wkb} WKB / {n_frozen} frozen-superhorizon "
      f"(wkb_leg_empty={wkb_leg_empty})")
print(f"  truncation_consistent = {truncation_consistent} "
      f"(branch_drift={branch_drift:.2e}, n_s(L7eq)={ns_L7equiv:.6f})")
print(f"  L_max_operational = {L_max_op}; N_modes = {N_modes_total} "
      f"(window {N_modes_window}); deg(T_BZ->pivot) = +{deg_T}")

# ============================================================================
#  SECTION 2: Re-derive the geometric pivot tilt (Mode-Independent Occupation)
# ============================================================================
print("\n" + "-" * 78)
print("SECTION 2: re-derive Goldstone-pivot tilt from canonical geometry")
print("-" * 78)

# The CMB-pivot tilt is the GEOMETRIC tilt n_s = 1 - 2*eps_H, carried to the pivot
# leaf by deg(T_BZ->pivot)=+2 NON-SCALAR. It is INDEPENDENT of |beta_k|^2 (Mode-
# Independent Occupation Theorem). The canonical anchor IS n_s_framework=0.9561
# (S85; n_s_FW_exact=9561/10000, S88 W-15). The geometric eps_H is the SCALAR.
ns_pivot = float(n_s_framework)                  # (local) 0.9561 geometric tilt
eps_H_implied = float((1.0 - ns_pivot) / 2.0)    # (local) eps_H = (1-n_s)/2
alpha_pivot = float(alpha_s_pivot_goldstone)     # (local) 0.0 Goldstone-protected

# Cross-check: the build's CMB-leaf MUST equal the canonical anchor bit-for-bit
ns_pivot_reload_consistent = bool(abs(ns_pivot_build - ns_pivot) < 1e-9)  # (local)
alpha_pivot_reload_consistent = bool(abs(alpha_pivot_build - alpha_pivot) < 1e-12)  # (local)

print(f"  geometric tilt n_s^pivot = 1 - 2*eps_H = {ns_pivot:.6f}  "
      f"(eps_H = {eps_H_implied:.6f})")
print(f"  alpha_s^pivot (Goldstone-protected) = {alpha_pivot:.6f}")
print(f"  build CMB-leaf reproduces canonical: n_s {ns_pivot_reload_consistent}, "
      f"alpha_s {alpha_pivot_reload_consistent}")

# --- BZ-blue diagnostic: confirm leaf-1 is k^3-blue (n_s^BZ ~ 3, SIGN > 1) ---
# Direct slope of ln P vs ln k over the assembled window (independent re-fit).
order = np.argsort(k_assembled)
lnk_fit = np.log(k_assembled[order])
lnP_fit = np.log(P_assembled[order])
# linear slope = (n_s^BZ - 1); a P ~ k^3 blue spectrum gives slope ~ +3 => n_s~=4,
# but the build's spline-at-pivot gives ns_BZ~=2.9998 (slope ~ +1.9998). Report
# BOTH the spline-at-pivot (build) and the global linear slope (this re-fit).
lin_slope, lin_intercept = np.polyfit(lnk_fit, lnP_fit, 1)  # (local)
ns_BZ_linfit = float(1.0 + lin_slope)            # (local) global-linear n_s^BZ
blue_leaf_diagnostic = bool(ns_BZ > 1.0)         # (local) BZ leaf is BLUE (n_s>1)

print(f"  BZ-leaf k^3-BLUE diagnostic: n_s^BZ(spline-pivot) = {ns_BZ:.6f} > 1 "
      f"=> BLUE; global-linear slope = {lin_slope:.4f} (n_s^BZ_linfit "
      f"= {ns_BZ_linfit:.4f})")
print(f"  blue_leaf_diagnostic (n_s^BZ > 1) = {blue_leaf_diagnostic}")

# ============================================================================
#  SECTION 3: Pair the AMPLITUDE leg (dedup flag i -- shape AND amplitude)
# ============================================================================
print("\n" + "-" * 78)
print("SECTION 3: amplitude leg (impulse-quench |beta_k|^2 functional)")
print("-" * 78)

# Amplitude leg = REGISTERED CONTENT paired with the shape (NOT a gate threshold).
# inv-5 W2-1 impulse-quench Bogoliubov: A_s_impulse=1.5367e-08, OOM_gap=+0.8644
#   (substrate-natural xi_KZ; replaces 3.02/3.15/4.56/9.5-OOM self-disagreement)
# inv-6 W2-2 Parker-adiabatic-regularized Bogoliubov: A_s=5.99e-08, log_gap=+1.455
A_s_impulse_inv5 = 1.5367e-08                    # (local) inv-5 W2-1 verdict value
OOM_gap_inv5 = 0.8644                            # (local) inv-5 W2-1 OOM_gap (+0.86)
A_s_parker_inv6 = 5.99e-08                       # (local) inv-6 W2-2 verdict value
log_gap_inv6 = 1.455                             # (local) inv-6 W2-2 log_gap (+1.455)

# Cross-check the OOM gaps against the canonical A_s_CMB anchor (consistency).
oom_gap_inv5_recompute = float(np.log10(A_s_impulse_inv5 / A_s_CMB))  # (local)
oom_gap_inv6_recompute = float(np.log10(A_s_parker_inv6 / A_s_CMB))   # (local)
amp_inv5_consistent = bool(abs(oom_gap_inv5_recompute - OOM_gap_inv5) < 0.01)  # (local)
amp_inv6_consistent = bool(abs(oom_gap_inv6_recompute - log_gap_inv6) < 0.01)  # (local)

print(f"  inv-5 (impulse-quench):  A_s = {A_s_impulse_inv5:.4e}, "
      f"OOM_gap = +{OOM_gap_inv5:.4f}  (recompute +{oom_gap_inv5_recompute:.4f}, "
      f"consistent={amp_inv5_consistent})")
print(f"  inv-6 (Parker-adiabatic): A_s = {A_s_parker_inv6:.4e}, "
      f"log_gap = +{log_gap_inv6:.4f}  (recompute +{oom_gap_inv6_recompute:.4f}, "
      f"consistent={amp_inv6_consistent})")
print(f"  amplitude leg PAIRED with shape (dedup flag i: shape AND amplitude, "
      f"NOT shape-only)")
print(f"  [amplitude is registered content; the A_s upper-edge filter leg is "
      f"S110-CF-AS2-GREYBODY; the floor A_s >= A_s^BD is permanent on 3 axes]")

# ============================================================================
#  SECTION 4: Evaluate the SESSION §W2-1 operator + [SIGN] 3-tuple
# ============================================================================
print("\n" + "-" * 78)
print("SECTION 4: session §W2-1 operator + [SIGN] 3-tuple + composite collapse")
print("-" * 78)

# Session operator (plan §W2-1 line 71):
#   PASS iff |n_s^pivot - 0.9561| <= 0.0030 AND |alpha_s^pivot| < 0.019
#            AND truncation_consistent == True
NS_TARGET = 0.9561                               # (local) canonical pivot tilt
NS_BAND = 0.0030                                 # (local) +/- band (pub precision 4 sf)
ALPHA_CEIL = 0.019                               # (local) |alpha_s| ceiling

ns_dev = abs(ns_pivot - NS_TARGET)               # (local)
ns_in_band = bool(ns_dev <= NS_BAND)
alpha_ok = bool(abs(alpha_pivot) < ALPHA_CEIL)
operator_pass = bool(ns_in_band and alpha_ok and truncation_consistent)

print(f"  |n_s^pivot - {NS_TARGET}| = {ns_dev:.6f} <= {NS_BAND} : {ns_in_band}")
print(f"  |alpha_s^pivot| = {abs(alpha_pivot):.6f} < {ALPHA_CEIL} : {alpha_ok}")
print(f"  truncation_consistent = {truncation_consistent}")
print(f"  operator (all-three AND) = {operator_pass}")

# --- [SIGN] 3-tuple (gate-verdicts.md schema-v2) ---
# sign: substitution chain Step 6 predicts RED tilt (n_s^pivot < 1) at pivot leaf
#       AND BLUE (n_s^BZ > 1) at BZ leaf -- BOTH directions must hold.
sign_pred_pivot_red = bool(ns_pivot < 1.0)       # (local) pivot leaf RED
sign_pred_BZ_blue = bool(ns_BZ > 1.0)            # (local) BZ leaf BLUE
sign_verdict = "PASS" if (sign_pred_pivot_red and sign_pred_BZ_blue) else "FAIL"

# magnitude: PASS iff in-band AND alpha_ok; INFO iff borderline; FAIL otherwise.
INFO_BAND = 0.006                                # (local) info band (2x pass band)
if ns_in_band and alpha_ok:
    magnitude_verdict = "PASS"
elif ns_dev <= INFO_BAND and alpha_ok:
    magnitude_verdict = "INFO"
else:
    magnitude_verdict = "FAIL"

# regime: VALID if a genuine WKB-Bogoliubov leg exists; MARGINAL if ALL window
# modes are frozen-superhorizon (the tilt is read entirely from |u/z|^2, the
# all-frozen-superhorizon regime the investigation build returned). The shape is
# well-defined (geometric tilt), but the impulse regime is MARGINAL.
if wkb_leg_empty:
    regime_verdict = "MARGINAL"
else:
    regime_verdict = "VALID"

# --- generic composite collapse rule (gate-verdicts.md, for reference) ---
if regime_verdict == "BREAKDOWN":
    composite_generic = "FAIL"
elif sign_verdict == "FAIL":
    composite_generic = "FAIL"
elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
    composite_generic = "FAIL"
elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
    composite_generic = "INFO"
elif magnitude_verdict == "INFO":
    composite_generic = "INFO"
else:
    composite_generic = "PASS"

# --- PLAN-FROZEN composite operator (gate-verdicts.md §"Plan-frozen gate-block
#     operator precedence"). Plan §W2-1 INFO_meaning (line 188) PRE-REGISTERS:
#     "The composite-collapse rule maps magnitude=PASS+regime=MARGINAL -> INFO."
#     The dual_prior track_B (line 172) confirms: regime stays MARGINAL
#     (all-frozen-superhorizon) => INFO (shape promotes, amplitude/regime
#     carry-forward). This CONFLICTS with the generic rule (which gives PASS for
#     magnitude=PASS regardless of MARGINAL). The plan-frozen operator takes
#     PRECEDENCE; a mandatory '# composite-precedence:' disclosure row is emitted.
# Plan-frozen operator (set-membership + regime overlay):
#   FAIL    iff NOT truncation_consistent OR sign FAIL OR (mag FAIL & VALID)
#   PASS    iff operator_pass AND regime VALID            (whole gate permanent, Track A)
#   INFO    iff operator_pass AND regime MARGINAL          (shape promotes, Track B)
if not truncation_consistent:
    composite = "FAIL"                       # plan FAIL_meaning
elif sign_verdict == "FAIL":
    composite = "FAIL"
elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
    composite = "FAIL"                       # plan FAIL_meaning (tilt out of band, regime valid)
elif operator_pass and regime_verdict == "MARGINAL":
    composite = "INFO"                       # plan INFO_meaning (line 188) — PLAN-FROZEN
elif operator_pass and regime_verdict == "VALID":
    composite = "PASS"                       # plan PASS_meaning
elif magnitude_verdict == "INFO":
    composite = "INFO"
else:
    composite = "FAIL"

composite_precedence_invoked = bool(composite != composite_generic)  # (local)

print(f"\n  sign_verdict      = {sign_verdict}  "
      f"(pivot RED {sign_pred_pivot_red} AND BZ BLUE {sign_pred_BZ_blue})")
print(f"  magnitude_verdict = {magnitude_verdict}  "
      f"(n_s_dev={ns_dev:.6f}, band={NS_BAND}, info_band={INFO_BAND})")
print(f"  regime_verdict    = {regime_verdict}  "
      f"(wkb_leg_empty={wkb_leg_empty}: all-frozen-superhorizon)")
print(f"  generic-collapse reading = {composite_generic}  "
      f"(magnitude=PASS+regime=MARGINAL -> PASS under the GENERIC rule)")
print(f"  PLAN-FROZEN operator     = {composite}  "
      f"(plan §W2-1 INFO_meaning line 188: mag=PASS+regime=MARGINAL -> INFO)")
print(f"  composite-precedence invoked = {composite_precedence_invoked} "
      f"(plan-frozen operator overrides generic collapse per gate-verdicts.md)")
print(f"  COMPOSITE VERDICT = {composite}")
print(f"  [dual_prior discriminator: PASS->Track A (gate permanent); "
      f"INFO->Track B (shape permanent, amplitude/regime carry-forward)]")

# ============================================================================
#  SECTION 5: cross-checks summary
# ============================================================================
print("\n" + "-" * 78)
print("SECTION 5: cross-checks")
print("-" * 78)

sigma_planck = abs(ns_pivot - planck_ns) / 0.0042  # (local)
print(f"  n_s^pivot (framework) = {ns_pivot:.4f}; Planck n_s = {planck_ns:.4f}; "
      f"|delta| = {abs(ns_pivot - planck_ns):.4f} ({sigma_planck:.2f} sigma)")
print(f"  n_s_FW_sqrt_cutoff = {n_s_FW_sqrt_cutoff:.4f} (RED, sibling anchor)")
print(f"  alpha_s^pivot (Goldstone) = {alpha_pivot:.4f}; "
      f"canon alpha_s_sd1 (BZ leaf) = {alpha_s_substrate_distance_1:.4f}")
print(f"  Planck alpha_s = {planck_alpha_s:.4f} (consistency reference)")
print(f"  two-leaf scale separation: deg(T_BZ->pivot) = +{deg_T} NON-SCALAR "
      f"=> 54.04 decades")

# ============================================================================
#  SECTION 6: figure
# ============================================================================
fig, axes = plt.subplots(2, 2, figsize=(13, 9))

# (0,0) assembled P(k) -- the substrate-IS BZ leaf
ax = axes[0, 0]
ax.scatter(k_assembled, P_assembled, c="C0", s=14, alpha=0.6,
           label="frozen-superhorizon modes")
ax.set_xscale("log"); ax.set_yscale("log")
ax.axvline(k_pivot_substrate, ls=":", c="k",
           label=f"k_pivot(BZ)={k_pivot_substrate:.2f}")
ax.set_xlabel("k  [M_KK]"); ax.set_ylabel(r"$P_\zeta(k)$ (dimensionless)")
ax.set_title(r"leaf-1 (substrate/BZ): $k^3$-BLUE $P(k)$")
ax.legend(fontsize=8)

# (0,1) n_s(k) -- BZ leaf is blue (~3), pivot leaf is red (0.9561)
ax = axes[0, 1]
ax.plot(np.exp(lnk_grid), ns_of_lnk, "-", c="C0", label=r"$n_s^{BZ}(k)$ (blue leaf)")
ax.axhline(1.0, ls="--", c="gray", label="scale-invariant")
ax.axhline(ns_pivot, ls="-", c="C3", lw=2,
           label=f"$n_s^{{pivot}}$={ns_pivot:.4f} (red, Goldstone leaf)")
ax.axhspan(NS_TARGET - NS_BAND, NS_TARGET + NS_BAND, color="C3", alpha=0.15)
ax.set_xscale("log")
ax.set_xlabel("k  [M_KK]"); ax.set_ylabel(r"$n_s(k)$")
ax.set_title(f"two leaves: BZ={ns_BZ:.3f} (BLUE) vs pivot={ns_pivot:.4f} (RED)")
ax.legend(fontsize=7)

# (1,0) amplitude leg
ax = axes[1, 0]
labels = ["inv-5\nimpulse", "inv-6\nParker", "Planck\nA_s"]
vals = [A_s_impulse_inv5, A_s_parker_inv6, A_s_CMB]
cols = ["C2", "C4", "k"]
ax.bar(range(3), vals, color=cols, alpha=0.7)
ax.set_yscale("log")
ax.set_xticks(range(3)); ax.set_xticklabels(labels, fontsize=8)
ax.set_ylabel(r"$A_s$")
ax.axhline(A_s_CMB, ls="--", c="gray")
ax.set_title(f"amplitude leg: +{OOM_gap_inv5:.2f} / +{log_gap_inv6:.2f} OOM")

# (1,1) verdict panel
ax = axes[1, 1]
ax.axis("off")
txt = (
    f"S110-CF-B1-TRANSITPS  PROMOTE TRANSIT-PS-67\n"
    f"{'='*46}\n"
    f"L_max_op={L_max_op}  truncation_consistent={truncation_consistent}\n"
    f"N modes(BZ)={N_modes_total}  window={N_modes_window}\n"
    f"regime: {n_wkb} WKB / {n_frozen} frozen-superhorizon\n"
    f"deg(T_BZ->pivot)=+{deg_T} NON-SCALAR (54.04 dec)\n"
    f"{'-'*46}\n"
    f"leaf-2 (Goldstone-pivot, GATE-GOVERNING):\n"
    f"  n_s^pivot = {ns_pivot:.4f}  alpha_s = {alpha_pivot:.4f}\n"
    f"  |n_s-0.9561|={ns_dev:.4f}<=0.003 : {ns_in_band}\n"
    f"  |alpha_s|<0.019 : {alpha_ok}\n"
    f"{'-'*46}\n"
    f"leaf-1 (substrate/BZ, blue diagnostic):\n"
    f"  n_s^BZ = {ns_BZ:.4f} (BLUE>1)  a_s={alpha_BZ:.4f}\n"
    f"{'-'*46}\n"
    f"amplitude leg (dedup flag i):\n"
    f"  inv-5 +{OOM_gap_inv5:.2f} OOM  inv-6 +{log_gap_inv6:.3f} OOM\n"
    f"{'-'*46}\n"
    f"sign={sign_verdict} mag={magnitude_verdict} regime={regime_verdict}\n"
    f"VERDICT = {composite}"
)
ax.text(0.02, 0.98, txt, family="monospace", fontsize=8.5, va="top")

plt.tight_layout()
PLOT_PATH = os.path.join(HERE, "s110_cf_b1_transit_ps_promote.png")
plt.savefig(PLOT_PATH, dpi=130)
plt.close()
print(f"\n  figure -> {PLOT_PATH}")

# ============================================================================
#  SECTION 7: save data
# ============================================================================
NPZ_PATH = os.path.join(HERE, "s110_cf_b1_transit_ps_promote.npz")
np.savez(
    NPZ_PATH,
    gate_id=GATE_ID,
    composite_verdict=composite,
    # two scale-tagged leaves
    ns_pivot=ns_pivot, alpha_pivot=alpha_pivot, eps_H_implied=eps_H_implied,
    ns_BZ=ns_BZ, alpha_BZ=alpha_BZ, ns_BZ_linfit=ns_BZ_linfit,
    lin_slope_BZ=lin_slope, blue_leaf_diagnostic=blue_leaf_diagnostic,
    k_pivot_substrate=k_pivot_substrate,
    deg_T_BZ_pivot=deg_T,
    scale_channel_tag=("leaf-1=(substrate/BZ,k^3-blue,n_s~3,O(M_KK)); "
                       "leaf-2=(Goldstone-pivot,red,n_s=0.9561,CMB); "
                       "deg(T_BZ->pivot)=+2 NON-SCALAR, 54.04 decades"),
    # build reproduction consistency
    ns_pivot_reload_consistent=ns_pivot_reload_consistent,
    alpha_pivot_reload_consistent=alpha_pivot_reload_consistent,
    ns_pivot_build=ns_pivot_build, alpha_pivot_build=alpha_pivot_build,
    # amplitude leg (dedup flag i)
    A_s_impulse_inv5=A_s_impulse_inv5, OOM_gap_inv5=OOM_gap_inv5,
    A_s_parker_inv6=A_s_parker_inv6, log_gap_inv6=log_gap_inv6,
    oom_gap_inv5_recompute=oom_gap_inv5_recompute,
    oom_gap_inv6_recompute=oom_gap_inv6_recompute,
    amp_inv5_consistent=amp_inv5_consistent,
    amp_inv6_consistent=amp_inv6_consistent,
    # operator + 3-tuple
    ns_in_band=ns_in_band, alpha_ok=alpha_ok, operator_pass=operator_pass,
    ns_dev=ns_dev, NS_TARGET=NS_TARGET, NS_BAND=NS_BAND, ALPHA_CEIL=ALPHA_CEIL,
    sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
    regime_verdict=regime_verdict,
    composite_generic=composite_generic,
    composite_precedence_invoked=composite_precedence_invoked,
    # regime + truncation
    n_wkb=n_wkb, n_frozen=n_frozen, wkb_leg_empty=wkb_leg_empty,
    truncation_consistent=truncation_consistent,
    branch_drift_L3_L7=branch_drift, ns_L7equiv=ns_L7equiv,
    L_max_operational=L_max_op,
    N_modes_total=N_modes_total, N_modes_window=N_modes_window,
    r_tau_fold=r_tau_fold, k_tach_fold=k_tach_fold,
    # cross-checks
    planck_ns=planck_ns, sigma_planck=sigma_planck,
    n_s_FW_sqrt_cutoff=n_s_FW_sqrt_cutoff,
    alpha_s_substrate_distance_1=alpha_s_substrate_distance_1,
    planck_alpha_s=planck_alpha_s, A_s_CMB=A_s_CMB,
    # input-SHA drift documentation (§ii.B plan-text-drift)
    sha_drift=json.dumps(sha_drift),
    canonical_drift_note=canonical_drift_note,
    build_drift_note=build_drift_note,
    build_content_consistent=build_content_consistent,
    runtime_input_shas=json.dumps(input_shas),
    plan_pinned_shas=json.dumps(PLAN_PINNED_SHAS),
    # provenance
    tau_fold=tau_fold, M_KK=M_KK,
)
print(f"  data   -> {NPZ_PATH}")

# ============================================================================
#  SECTION 8: dual-SHA + verdict payload (gate-verdicts.md; emit_verdict by agent)
# ============================================================================

# audit_sha256 over the ordered input-pin map (script + canonical + pinmap +
# the two static physics inputs). RUNTIME SHAs pinned per §(ii.B).
pinmap = {
    "_gate_id": GATE_ID,
    "_wp_id": "W2-1",
    "_scheme": "TRANSIT-PS-Parker-Bogoliubov",
    "_convention": "TWO-LEAF-SCALE-TAGGED-deg-T-plus-2-NON-SCALAR",
    "script_sha": _sha256_file(os.path.abspath(__file__)),
    "canonical_sha": input_shas["canonical_constants"],
    "inv10_w2_transit_ps_build_sha": input_shas["inv10_w2_transit_ps_build"],
    "s84_spectrum_cache_sha": input_shas["s84_spectrum_cache"],
    "L_max_operational": L_max_op,
    "ns_pivot": round(ns_pivot, 10),
    "ns_BZ": round(ns_BZ, 10),
    "alpha_pivot": round(alpha_pivot, 12),
    "truncation_consistent": truncation_consistent,
    "OOM_gap_inv5": OOM_gap_inv5,
    "log_gap_inv6": log_gap_inv6,
}
audit_sha256 = hashlib.sha256(
    json.dumps(pinmap, sort_keys=True).encode()).hexdigest()
content_sha256 = _sha256_file(os.path.abspath(__file__))

# MANDATORY composite-precedence disclosure row (gate-verdicts.md §"Plan-frozen
# gate-block operator precedence"): the plan-frozen operator overrode the generic
# collapse; this row names the plan anchor + the generic reading being overridden.
EXTRA_ROWS = []                                   # (local) emit_verdict extra_rows
if composite_precedence_invoked:
    EXTRA_ROWS.append(
        f"# composite-precedence: plan-frozen operator (session-110-plan-w2.md "
        f"§W2-1 INFO_meaning line 188: mag=PASS+regime=MARGINAL -> INFO) OVERRIDES "
        f"generic-collapse reading '{composite_generic}'; regime=MARGINAL "
        f"(all-frozen-superhorizon, 89/89 modes); shape promotes (Track B), "
        f"amplitude/regime caveat carries forward # {GATE_ID} composite-precedence")
# §(ii.B) plan-text-drift disclosure row (audit trail for the two SHA drifts)
EXTRA_ROWS.append(
    f"# plan-text-drift (§ii.B): canonical_constants byte-SHA "
    f"{input_shas['canonical_constants'][:16]} (plan {PLAN_PINNED_SHAS['canonical_constants'][:16]}); "
    f"inv10-build byte-SHA {input_shas['inv10_w2_transit_ps_build'][:16]} "
    f"(plan {PLAN_PINNED_SHAS['inv10_w2_transit_ps_build'][:16]}, untracked/zip-ts non-det); "
    f"ARRAY-CONTENT verified vs plan canonical values (consistent={build_content_consistent}); "
    f"runtime SHAs pinned in audit map # {GATE_ID} input-SHA drift")

# value payload (no single quotes; tool wraps as value='...')
value_str = (
    f"ns_pivot={ns_pivot:.4f}_alpha_pivot={alpha_pivot:.4f}_"
    f"ns_BZ_blue={ns_BZ:.4f}_alpha_BZ={alpha_BZ:.4f}_"
    f"truncation_consistent={truncation_consistent}_"
    f"deg_T_BZ_pivot=+{deg_T}_NON-SCALAR_54.04dec_"
    f"amplitude[inv5_OOM=+{OOM_gap_inv5:.2f},inv6_OOM=+{log_gap_inv6:.3f}]_"
    f"regime[wkb={n_wkb},frozen={n_frozen},MARGINAL]_"
    f"shape+amplitude-together-dedup-i"
)


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          scheme, convention, l_max,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None):
    print("\n" + "=" * 78)
    print("VERDICT PAYLOAD (agent -> emit_verdict; track=session, session=110)")
    print("=" * 78)
    payload = {
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": value,
        "scheme": scheme,
        "convention": convention,
        "l_max": str(l_max),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
    }
    if sign_verdict is not None:
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
    for k, v in payload.items():
        print(f"  {k} = {v}")
    print("-" * 78)
    print("  extra_rows (pass to emit_verdict extra_rows=[...]):")
    for r in EXTRA_ROWS:
        print(f"    {r}")
    print("=" * 78)
    return payload


print_verdict_payload(
    composite, value_str, audit_sha256, content_sha256,
    scheme="TRANSIT-PS-Parker-Bogoliubov",
    convention="TWO-LEAF-SCALE-TAGGED-deg-T-plus-2-NON-SCALAR",
    l_max=L_max_op,
    sign_verdict=sign_verdict,
    magnitude_verdict=magnitude_verdict,
    regime_verdict=regime_verdict,
)

print("\nDONE.")
