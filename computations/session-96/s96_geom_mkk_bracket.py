#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
S96-GEOM-MKK-BRACKET
================================================================================
Gate:   S96-GEOM-MKK-BRACKET   (trigger [SIGN], classification GEOMETRIC)
Agent:  kaluza-klein-theorist   (cluster C5 single-value-for-multi-route quantity)
Plan:   sessions/session-plan/session-96-plan-w5.md  ## §W5-7
WP:     sessions/archive/session-96/session-96-w5-workingpaper.md  ### §W5-7

HYPOTHESIS (kk §V.1, §V.2; capstone cluster C5)
--------------------------------------------------------------------------------
M_KK is presented in the capstone as ONE substrate-fixed compactification cutoff,
but the canonical class records a 0.83-decade gravity-vs-Kerner bracket:
  - gravity route   M_KK,gravity = 7.42866e16 GeV  (1/(16 pi G_N) = f2 Lambda^2 a2^zeta/(48 pi^2))
  - Kerner route    M_KK,Kerner  = 5.04168e17 GeV  (4D gauge-kinetic normalization 1/g^2 ~ M_KK^{d-4} vol)
This gate propagates the bracket ratio R = M_KK,Kerner/M_KK,gravity into the
ABSOLUTE a0 (Lambda^4, vacuum-energy) and a2 (Lambda^2, gravity) magnitudes via the
Lambda^4 / Lambda^2 scaling of the spectral-action Seeley-DeWitt moments. The verdict:
either the routes AGREE within 10% (bracket illusory, single M_KK justified, PASS),
or the bracket is REAL and injects a factor-R^4 band into absolute a0 and R^2 into a2
(INFO -- a SECOND, independent absolute-magnitude uncertainty source beyond SDW
convergence, flagged alongside JACOBSON-NONLOCAL-64 in capstone Sec 8.5).

SUBSTRATE ARROW (phononic-framing.md; never inverted):
    D_K eigenvalues -> spectral-action Seeley-DeWitt moments (a0, a2) ->
    {Newton's constant G_N via a2, unified gauge coupling g^2 via the Kerner
    gauge-metric normalization} -> M_KK (TWO routes) -> absolute a0 (Lambda^4) /
    a2 (Lambda^2) magnitude band.
    M_KK is the SU(3)-fiber size -- a property of the internal geometry, NOT an
    externally imposed cutoff. The absolute vacuum-energy magnitude IS the a0
    Seeley-DeWitt moment times Lambda^4; so any M_KK uncertainty propagates as
    Lambda^4 to the CC magnitude. The fabric is not IN a container with a chosen
    cutoff -- M_KK emerges from how the a2 spectral weight distributes (gravity
    route) and how the gauge-kinetic term normalizes (Kerner route). The KK
    question "do the gauge and gravity sectors agree on the size of the extra
    dimensions?" IS the bracket. (Reading M_KK as a single tunable scale that
    fixes the CC is the container-thinking error this gate corrects.)

--------------------------------------------------------------------------------
SUBSTITUTION CHAIN ([SIGN] trigger -- MANDATORY, math-scripts.md
                   "Double-Check Logic Before Compute"; plan Step 1->6,
                   PRE-REGISTERED -- the predicted direction is NOT re-decided post-hoc)
--------------------------------------------------------------------------------
Claim: "the M_KK bracket injects a factor-R^4 band into the absolute a0 (Lambda^4)
        magnitude and a factor-R^2 band into the a2 (Lambda^2) magnitude, where
        R = M_KK,Kerner/M_KK,gravity ~ 6.787; the Lambda-power HIERARCHY (Lambda^4
        >> Lambda^2 >> Lambda^0) is INVARIANT under the rescaling -- only the
        absolute magnitudes inherit the band."

Step 1: M_KK,gravity = 7.428660036284456e16 GeV  [canonical_constants.py M_KK_gravity; CONST-FREEZE-42]
Step 2: M_KK,Kerner  = 5.041679838376001e17 GeV  [canonical_constants.py M_KK_kerner; CONST-FREEZE-42]
Step 3: ratio  R := M_KK,Kerner / M_KK,gravity                          [definition]
Step 4: Substitute and simplify (one step per line):
        R = 5.041679838376001e17 / 7.428660036284456e16
          = 6.786795752868596                                           [the route ratio R]
        log10(R) = 0.8316647793908398                                   [= OOM_diff_MKK canonical;
                   the 0.83-decade bracket, confirmed to <2e-15]
Step 5: the a0 vacuum term scales as Lambda^4 (zeroth Seeley-DeWitt moment x Lambda^4):
        rho_Lambda ~ (2/pi^2) a0^zeta M_KK^4   [cf. canonical rho_Lambda_spectral = (2/pi^2) a0_fold M_KK_kerner^4]
          a0-magnitude band factor = R^4 = (6.786795752868596)^4 = 2121.578558       [Lambda^4 propagation]
        the a2 gravity term scales as Lambda^2 (1/(16 pi G_N) ~ f2 a2^zeta Lambda^2/(48 pi^2)):
          a2-magnitude band factor = R^2 = (6.786795752868596)^2 = 46.060597         [Lambda^2 propagation]
Step 6: R = 6.787 > 1 by 0.83 decades  =>  |R-1| = 5.787 >> 0.10
        =>  the bracket is REAL (NOT illusory at the 10% PASS-band)
        =>  factor-R^4 = 2121.58x band on a0; factor-R^2 = 46.06x band on a2          [direction]
        =>  the Lambda-power exponents (4, 2, 0) are UNCHANGED by the rescaling
            (R^4 / R^2 / R^0 preserve the ordering 4>2>0): the HIERARCHY is robust;
            only the absolute MAGNITUDES shift (a0 by 3.327 decades, a2 by 1.663 decades).
Conclusion: the M_KK bracket is a real 0.83-decade factor; propagated through Lambda^4
            it is a ~2122x band on the absolute a0 (CC-magnitude / vacuum-energy) term
            -- a SECOND, independent source of absolute-magnitude uncertainty beyond the
            SDW-convergence FAIL (Sec 8.5, C2). Pre-registered most-likely outcome: INFO
            (bracket real, quantify the band). PASS (|R-1|<=0.10) is excluded unless the
            Kerner-route recompute lands much closer to the gravity route than the
            canonical pin (factor 6.79) -- which it does not (the routes are pinned
            CONST-FREEZE-42 values, not recomputed-to-converge).

NOTE ON THE PLAN'S ROUNDED R: the plan substitution chain used the rounded R=6.7868,
giving R^4=2122.4. The EXACT canonical-pinned ratio is R=6.786795752868596, giving
R^4=2121.578558. This script reports the exact value and notes the plan's rounded
approximation (the 0.05% difference is rounding-of-R, not a substrate disagreement).

NOTE ON a0^zeta DIMENSIONLESSNESS: a_0_FW_zeta = 6440 is DIMENSIONLESS (a0 = zeta_{D_K}(0)
= Tr(1), a substrate mode count, R-protected per S64/S77). The Lambda^4 scaling enters
NOT through the dimensionless a0^zeta coefficient but through the SPECTRAL-ACTION
prefactor f4 Lambda^4 a0^zeta (the vacuum/CC term). So "the absolute a0 magnitude" the
gate bands is the VACUUM-ENERGY term ~ a0^zeta x M_KK^4 (as in rho_Lambda_spectral), and
the R^4 band acts on the M_KK^4 factor, NOT on the dimensionless a0^zeta=6440 coefficient.
Likewise R^2 acts on the M_KK^2 factor in 1/(16 pi G_N) ~ a2^zeta x M_KK^2, not on a2^zeta.

CLASS=FULL (two closed-form scale extractions + a ratio + Lambda^4/Lambda^2 scaling;
NO SCHEMATIC helper; the route values are canonical CONST-FREEZE-42 pins).
regulator_pin = a_n^{zeta} (a0^zeta=6440, a2^zeta=2776.165389 zeta-regularized Seeley-
DeWitt; the band is on the M_KK^n prefactors, the a_n^zeta coefficients are the
regulator-pinned dimensionless moments).

SOFT DEPENDENCY (W5-6, S96-GEOM-GAUGE-SOURCING): this gate consumes the gauge-route
M_KK reconciliation outcome of W5-6. If the W5-6 verdict is on disk in the canonical
verdict file at runtime, this script reads it and tags the a0 band accordingly; if NOT
yet present, the a0 band is tagged "gauge-route-disputed" per the plan (W5-7 does NOT
hard-block on W5-6).
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # (local) CPU thread cap; two closed-form extractions + ratio only
os.environ.setdefault("MKL_NUM_THREADS", "8")   # (local)

import sys
import json
import hashlib
import re
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --- canonical constants (MANDATORY: from canonical_constants import ...) ---
SHARED = Path(__file__).resolve().parents[1] / "_shared"          # (local) canonical_constants lives in _shared
sys.path.insert(0, str(SHARED))
from canonical_constants import (  # noqa: E402
    M_KK, M_KK_gravity, M_KK_kerner, OOM_diff_MKK,
    a_0_FW_zeta, a_2_FW_zeta, a0_fold, a2_fold,
    PI,
)

# ---------------------------------------------------------------------------
# Paths + identity
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[2]                       # (local) project root (this script in computations/session-96; parents[2]=root)
GATE_ID = "S96-GEOM-MKK-BRACKET"                                 # (local)
SCHEME = "SA-zeta"                                               # (local) plan-pinned (a0^zeta, a2^zeta zeta-regularized)
CONVENTION = "ABSOLUTE"                                          # (local) plan-pinned (absolute Lambda^4/Lambda^2 magnitudes; R convention-independent)
L_MAX = "10"                                                    # (local) canonical truncation for a2^zeta provenance
SCHEMA_VERSION = "S84+"                                          # (local)

SCRIPT_PATH = Path(__file__).resolve()                                                       # (local)
CANONICAL_CONSTANTS = SHARED / "canonical_constants.py"                                       # (local)
GN_SNAPSHOT = ROOT / "computations" / "session-42" / "s42_constants_snapshot.npz"            # (local) G_N route + M_KK provenance
VERDICT_FILE = ROOT / "computations" / "session-96" / "s96_gate_verdicts.txt"                # (local) CANONICAL path (gate-verdicts.md)
NPZ_OUT = ROOT / "computations" / "session-96" / "s96_geom_mkk_bracket.npz"                  # (local)
PNG_OUT = ROOT / "computations" / "session-96" / "s96_geom_mkk_bracket.png"                  # (local)

# Soft-dependency: W5-6 gauge-route reconciliation verdict (read-if-present, never hard-block)
W5_6_GATE_ID = "S96-GEOM-GAUGE-SOURCING"                         # (local)

# Pre-registered tolerances (plan W5-7 machinery_pin_map)
PASS_BAND = 0.10        # (local) PASS iff |R-1| <= 0.10 (bracket illusory)
RATIO_TOL = 1e-6        # (local) ratio-computation / log10 consistency tolerance
OOM_MATCH_TOL = 1e-9    # (local) |log10(R) - OOM_diff_MKK| canonical-match floor


# ---------------------------------------------------------------------------
# SHA helpers (dual-SHA per S84+ schema; mirrors s96_w3_1 reference implementation)
# ---------------------------------------------------------------------------
def sha256_of_file(p: Path) -> str:
    try:
        return hashlib.sha256(p.read_bytes()).hexdigest()
    except OSError:
        return "MISSING"


def log_input_pins(files: dict) -> dict:
    pins = {}  # (local)
    for name, p in files.items():
        sha = sha256_of_file(p)  # (local)
        try:
            rel = str(Path(p).resolve().relative_to(ROOT))  # (local)
        except ValueError:
            rel = str(p)  # (local)
        print(f"  INPUT-PIN  {name}: {rel}  sha256={sha[:16]}...")
        pins[name] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple:
    """audit_sha256 = sha256(script_bytes + canonical_bytes + pinmap_json);
       content_sha256 = sha256(script_bytes).  (S84+ dual-SHA schema.)"""
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
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


def read_w5_6_verdict(verdict_file: Path, gate_id: str):
    """Soft-dependency read: parse the latest non-superseded W5-6 canonical line if present.
    Returns (status, value_str) or (None, None) if W5-6 not yet on disk.
    Per gate-verdicts.md Option A: follow the supersedes chain (latest non-superseded line)."""
    try:
        text = verdict_file.read_text(encoding="utf-8")  # (local)
    except OSError:
        return None, None
    superseded = set()  # (local) audit_sha256 values named in a supersedes= token
    for m in re.finditer(r"supersedes=([a-f0-9]{64})", text):
        superseded.add(m.group(1))
    latest = None  # (local) (status, value_str, audit_sha)
    for line in text.splitlines():
        if line.startswith(f"{gate_id}:"):
            ms = re.match(rf"{re.escape(gate_id)}:\s*(PASS|FAIL|INFO|PRE-REG-INC)\b", line)  # (local)
            mv = re.search(r"value='([^']*)'", line)  # (local)
            ma = re.search(r"audit_sha256=([a-f0-9]{64})", line)  # (local)
            if ms and ma and ma.group(1) not in superseded:
                latest = (ms.group(1), mv.group(1) if mv else "", ma.group(1))  # (local) last wins
    if latest is None:
        return None, None
    return latest[0], latest[1]


def append_verdict(verdict, value_str, audit_sha, content_sha, sign_v, mag_v, regime_v,
                   R, log10R, R2, R4, w5_6_status):
    """Single canonical dual-SHA verdict line + dual-SHA companion row + schema-v2
    3-tuple companion row ([SIGN] directional pre-reg). Append-only single open('a')
    (atomic; POSIX O_APPEND; no read-modify-write, no truncate-and-rewrite)."""
    gauge_tag = w5_6_status if w5_6_status is not None else "gauge-route-disputed"  # (local)
    canonical = (  # (local)
        f"{GATE_ID}: {verdict} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )
    companion = (  # (local)
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; [SIGN] M_KK gravity-vs-Kerner bracket -> absolute a0 (Lambda^4) band; "
        f"R = M_KK_kerner/M_KK_gravity = {R:.12f} (log10 R = {log10R:.12f} = OOM_diff_MKK 0.83-decade bracket); "
        f"R^4 = {R4:.6f} band on absolute a0 (Lambda^4 vacuum/CC magnitude); R^2 = {R2:.6f} band on a2 (Lambda^2 gravity); "
        f"Lambda-power HIERARCHY (4>2>0) INVARIANT under rescaling, only absolute magnitudes inherit the band; "
        f"a0^zeta=6440 / a2^zeta=2776.165389 are dimensionless R-protected moments, band acts on M_KK^n prefactors; "
        f"CLASS=FULL (CONST-FREEZE-42 route pins, no SCHEMATIC helper); regulator_pin=a_n^{{zeta}}; "
        f"W5-6 gauge-route soft-dep = {gauge_tag}; second absolute-magnitude uncertainty source beyond SDW-convergence (Sec 8.5)\n"
    )
    tuple_row = (  # (local)
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2; [SIGN] W5-7 Step-6 directional pre-reg: "
        f"SIGN=R>1 (bracket real, predicted; computed R={R:.6f}>1 => a0/a2 magnitudes scale UP by R^4/R^2); "
        f"MAG=|R-1| vs 0.10 PASS-band (PASS=bracket illusory; computed |R-1|={abs(R-1.0):.6f}>>0.10 => INFO, band quantified R^4={R4:.2f}x); "
        f"REGIME=VALID iff (log10 R matches OOM_diff_MKK canonical to {OOM_MATCH_TOL:.0e}) AND (route pins CONST-FREEZE-42 unsuperseded) "
        f"AND (Lambda-power hierarchy 4>2>0 preserved))\n"
    )
    with VERDICT_FILE.open("a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(companion)
        f.write(tuple_row)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> int:
    print("=" * 78)
    print(f"=== {GATE_ID} ===")
    print("=" * 78)

    # ---- (1) input pins ----
    input_files = {
        "script": SCRIPT_PATH,
        "canonical": CANONICAL_CONSTANTS,
        "gn_snapshot": GN_SNAPSHOT,
    }
    print("\nINPUT SHA-256 PINS:")
    pins = log_input_pins(input_files)

    print("\n  canonical constants imported:")
    print(f"    M_KK (default alias) = {M_KK:.12e}  (= M_KK_gravity)")
    print(f"    M_KK_gravity         = {M_KK_gravity:.12e}  GeV  (1/(16 pi G_N) route; CONST-FREEZE-42)")
    print(f"    M_KK_kerner          = {M_KK_kerner:.12e}  GeV  (Kerner gauge-metric route; CONST-FREEZE-42)")
    print(f"    OOM_diff_MKK (canon) = {OOM_diff_MKK:.15f}  (= log10(M_KK_kerner/M_KK_gravity), S42)")
    print(f"    a_0_FW_zeta          = {a_0_FW_zeta}  (DIMENSIONLESS a0 = zeta_D(0) = Tr(1); R-protected S64/S77)")
    print(f"    a_2_FW_zeta          = {a_2_FW_zeta}  (a2^zeta; spectral-zeta sum S42)")
    # sanity: default alias is the conservative gravity route
    alias_ok = bool(abs(M_KK - M_KK_gravity) < 1e-3 * M_KK_gravity)  # (local)
    print(f"    M_KK default == gravity route: {alias_ok}")

    # ---- (2) THE BRACKET RATIO R and its decade span ----
    print("\n" + "=" * 78)
    print("STEP 3-4: the route ratio R = M_KK,Kerner / M_KK,gravity and its decade span")
    print("=" * 78)
    R = M_KK_kerner / M_KK_gravity                    # (local) the bracket ratio
    log10R = float(np.log10(R))                       # (local) decade span
    oom_match = abs(log10R - OOM_diff_MKK)            # (local) match to canonical OOM_diff_MKK
    oom_match_ok = bool(oom_match < OOM_MATCH_TOL)    # (local)
    print(f"  R = M_KK,Kerner / M_KK,gravity = {M_KK_kerner:.6e} / {M_KK_gravity:.6e}")
    print(f"    = {R:.15f}")
    print(f"  log10(R) = {log10R:.15f}")
    print(f"  OOM_diff_MKK (canonical)  = {OOM_diff_MKK:.15f}")
    print(f"  |log10(R) - OOM_diff_MKK| = {oom_match:.3e}  (match to {OOM_MATCH_TOL:.0e}: {oom_match_ok})")
    print(f"  => the 0.83-decade gravity-vs-Kerner bracket, confirmed to machine precision.")

    # ---- (3) STEP 5: Lambda^4 / Lambda^2 propagation into absolute magnitudes ----
    print("\n" + "=" * 78)
    print("STEP 5: Lambda^4 (a0 vacuum) / Lambda^2 (a2 gravity) band propagation")
    print("=" * 78)
    R2 = R ** 2     # (local) a2 (Lambda^2) magnitude band factor
    R4 = R ** 4     # (local) a0 (Lambda^4) magnitude band factor
    R0 = R ** 0     # (local) a4 (Lambda^0) -- dimensionless, NO band (the Yang-Mills/Higgs-quartic coefficient is M_KK-independent)
    log10_R4 = float(np.log10(R4))  # (local) decades on a0
    log10_R2 = float(np.log10(R2))  # (local) decades on a2
    # absolute CC magnitude both routes (rho_Lambda ~ (2/pi^2) a0^zeta M_KK^4), for context (GeV^4)
    rho_Lambda_gravity = (2.0 / PI ** 2) * a_0_FW_zeta * M_KK_gravity ** 4  # (local) GeV^4, gravity route
    rho_Lambda_kerner = (2.0 / PI ** 2) * a_0_FW_zeta * M_KK_kerner ** 4    # (local) GeV^4, Kerner route (= canonical rho_Lambda_spectral)
    rho_band = rho_Lambda_kerner / rho_Lambda_gravity                      # (local) should equal R^4 exactly
    rho_band_consistent = bool(abs(rho_band - R4) / R4 < RATIO_TOL)        # (local)
    # absolute 1/(16 pi G_N) ~ f2 a2^zeta M_KK^2 band (just the M_KK^2 ratio, route-prefactor-independent)
    g2_term_band = (M_KK_kerner / M_KK_gravity) ** 2                       # (local) = R^2
    print(f"  a0 vacuum term  ~ Lambda^4 :  a0-magnitude band = R^4 = {R4:.6f}   ({log10_R4:.6f} decades on a0)")
    print(f"  a2 gravity term ~ Lambda^2 :  a2-magnitude band = R^2 = {R2:.6f}   ({log10_R2:.6f} decades on a2)")
    print(f"  a4 (YM/Higgs)   ~ Lambda^0 :  a4-magnitude band = R^0 = {R0:.6f}   (M_KK-INDEPENDENT; no band)")
    print(f"  --- absolute CC magnitude both routes (rho_Lambda = (2/pi^2) a0^zeta M_KK^4): ---")
    print(f"    rho_Lambda(gravity) = {rho_Lambda_gravity:.6e} GeV^4")
    print(f"    rho_Lambda(Kerner)  = {rho_Lambda_kerner:.6e} GeV^4  (= canonical rho_Lambda_spectral)")
    print(f"    rho_Lambda band = Kerner/gravity = {rho_band:.6f}  (= R^4: {rho_band_consistent})")
    print(f"  1/(16 pi G_N) ~ a2^zeta M_KK^2 band = {g2_term_band:.6f}  (= R^2)")

    # plan's rounded-R cross-check (the plan used R=6.7868 -> R^4=2122.4; exact differs by rounding-of-R)
    R_plan_rounded = 6.7868      # (local) the plan substitution-chain rounded value
    R4_plan = R_plan_rounded ** 4  # (local) plan's quoted ~2122.4
    plan_round_diff = abs(R4 - R4_plan) / R4  # (local) rel difference (rounding of R, not substrate)
    print(f"\n  plan rounded R={R_plan_rounded} -> R^4={R4_plan:.4f} (plan quoted ~2122.4);")
    print(f"    exact R={R:.6f} -> R^4={R4:.6f}; rel diff = {plan_round_diff:.3e} (rounding-of-R only, not substrate)")

    # ---- (4) STEP 6: Lambda-power HIERARCHY invariance under the rescaling ----
    print("\n" + "=" * 78)
    print("STEP 6: Lambda-power HIERARCHY (Lambda^4 >> Lambda^2 >> Lambda^0) invariance")
    print("=" * 78)
    # The qualitative ordering of the Lambda EXPONENTS (4 > 2 > 0) is unchanged by ANY positive R:
    # R^4 / R^2 / R^0 preserve the ordering for R > 1 (R^4 > R^2 > R^0 = 1). Only absolute magnitudes shift.
    powers = np.array([4, 2, 0])  # (local) Lambda-power exponents (a0, a2, a4)
    band_factors = R ** powers     # (local) [R^4, R^2, 1]
    hierarchy_preserved = bool(np.all(np.diff(band_factors) < 0) and band_factors[-1] == 1.0)  # (local) strictly decreasing, a4 fixed
    print(f"  Lambda-power exponents (a0, a2, a4) = {powers.tolist()}  (the EXPONENTS are R-INVARIANT)")
    print(f"  band factors R^power                = [{band_factors[0]:.4f}, {band_factors[1]:.4f}, {band_factors[2]:.4f}]")
    print(f"  hierarchy (R^4 > R^2 > R^0=1) preserved for R>1: {hierarchy_preserved}")
    print(f"  => only the absolute MAGNITUDES inherit the band; the qualitative Lambda^4 >> Lambda^2 >> Lambda^0")
    print(f"     ordering (the structure of the spectral-action expansion) is ROBUST to the M_KK bracket.")

    # ---- (5) soft-dependency: W5-6 gauge-route reconciliation (read-if-present) ----
    print("\n" + "-" * 78)
    print("Soft-dependency: W5-6 (S96-GEOM-GAUGE-SOURCING) gauge-route reconciliation")
    print("-" * 78)
    w5_6_status, w5_6_value = read_w5_6_verdict(VERDICT_FILE, W5_6_GATE_ID)  # (local)
    if w5_6_status is None:
        gauge_route_tag = "gauge-route-disputed"  # (local) plan-pinned tag when W5-6 not yet on disk
        print(f"  W5-6 verdict NOT yet on disk => a0 band tagged 'gauge-route-disputed' (plan W5-7; NO hard-block)")
    else:
        gauge_route_tag = f"W5-6={w5_6_status}"  # (local)
        print(f"  W5-6 verdict present: {W5_6_GATE_ID} = {w5_6_status}  (value='{w5_6_value[:80]}...')")
        print(f"  => a0 band tagged with W5-6 outcome ({gauge_route_tag})")

    # ---- (6) VERDICT (composite collapse rule; gate-verdicts.md) ----
    print("\n" + "=" * 78)
    print("VERDICT (M_KK bracket -> absolute a0 band; composite collapse)")
    print("=" * 78)
    abs_R_minus_1 = abs(R - 1.0)  # (local)

    # sign_verdict: PRE-REGISTERED predicted direction is R > 1 (bracket real => magnitudes scale UP).
    #   PASS iff computed sign(R-1) matches the predicted +1 (R>1).
    predicted_sign = +1            # (local) R > 1 predicted (Kerner route HIGHER than gravity route)
    computed_sign = int(np.sign(R - 1.0))  # (local)
    sign_v = "PASS" if (computed_sign == predicted_sign and computed_sign != 0) else "FAIL"  # (local)

    # magnitude_verdict: this is the bracket-illusory test. PASS iff |R-1| <= 0.10 (routes agree, single M_KK).
    #   FAIL-direction here is the "bracket real" finding -> mapped to INFO via regime (see collapse).
    #   |R-1| = 5.787 >> 0.10 => the bracket is REAL. Per the plan rubric this is the INFO branch
    #   (NOT a structural FAIL): the routes legitimately differ; the gate's job is to quantify the band.
    if abs_R_minus_1 <= PASS_BAND:
        mag_v = "PASS"  # (local) routes agree within 10% => bracket illusory
    else:
        mag_v = "FAIL"  # (local) |R-1| exceeds PASS-band => bracket real (collapses to INFO under MARGINAL regime, see below)

    # regime_verdict: the bracket-real outcome is the pre-registered INFO branch, NOT a method breakdown.
    #   We set regime=MARGINAL when the bracket is real (mag FAIL) so the collapse maps to INFO (not FAIL):
    #   the routes legitimately differ; the Lambda-power hierarchy is robust; only magnitudes inherit the band.
    #   regime=VALID requires the structural integrity checks (canonical-match, hierarchy, alias, rho consistency).
    structural_ok = bool(oom_match_ok and hierarchy_preserved and alias_ok
                         and rho_band_consistent)  # (local)
    if not structural_ok:
        regime_v = "BREAKDOWN"  # (local) a structural integrity check failed (escalate)
    elif mag_v == "FAIL":
        regime_v = "MARGINAL"   # (local) bracket REAL: pre-registered INFO branch (routes differ; band quantified)
    else:
        regime_v = "VALID"      # (local) bracket illusory (PASS) with full structural integrity

    # composite collapse rule (PRE-REGISTERED; gate-verdicts.md)
    if regime_v == "BREAKDOWN":
        composite = "FAIL"  # (local)
    elif sign_v == "FAIL":
        composite = "FAIL"
    elif mag_v == "FAIL" and regime_v == "VALID":
        composite = "FAIL"
    elif mag_v == "FAIL" and regime_v == "MARGINAL":
        composite = "INFO"   # (local) SIGN-correct (R>1), MAGNITUDE-outside-PASS-band (bracket real), regime-MARGINAL => INFO
    elif mag_v == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"

    print(f"  R = M_KK,Kerner/M_KK,gravity         = {R:.12f}")
    print(f"  |R - 1|                              = {abs_R_minus_1:.6f}  (PASS iff <= {PASS_BAND})")
    print(f"  log10(R) [decade span]              = {log10R:.6f}  (canonical OOM_diff_MKK match: {oom_match_ok})")
    print(f"  R^4 (a0 Lambda^4 band)              = {R4:.6f}  ({log10_R4:.4f} decades)")
    print(f"  R^2 (a2 Lambda^2 band)              = {R2:.6f}  ({log10_R2:.4f} decades)")
    print(f"  Lambda-power hierarchy preserved    = {hierarchy_preserved}")
    print(f"  predicted sign / computed sign      = {predicted_sign} / {computed_sign}  (R>1 predicted)")
    print(f"  W5-6 gauge-route soft-dep tag       = {gauge_route_tag}")
    print(f"  sign_verdict                        = {sign_v}")
    print(f"  magnitude_verdict                   = {mag_v}")
    print(f"  regime_verdict                      = {regime_v}")
    print(f"  COMPOSITE                           = {composite}")

    # ---- physics statement ----
    print("\n" + "-" * 78)
    if composite == "PASS":
        print("  THE 0.83-DECADE BRACKET IS ILLUSORY: the gravity and Kerner gauge-metric routes")
        print("  agree on M_KK within 10%. A single M_KK is justified; the absolute a0/a2 magnitudes")
        print("  carry NO M_KK-bracket uncertainty (only SDW-convergence uncertainty remains).")
    elif composite == "INFO":
        print("  THE M_KK BRACKET IS REAL: R = 6.787 (0.83 decades). The gravity route (through G_N,")
        print("  Lambda^2) and the Kerner gauge-metric route (through the 4D gauge-kinetic normalization)")
        print("  do NOT agree on the size of the extra dimensions. Propagated through the Lambda^4")
        print("  scaling of the a0 vacuum term, this is a factor-R^4 = 2121.58x band on the absolute a0")
        print("  (CC / vacuum-energy) magnitude (R^2 = 46.06x on a2 gravity). This is a SECOND, INDEPENDENT")
        print("  source of absolute-magnitude uncertainty beyond the SDW-convergence FAIL (capstone Sec 8.5,")
        print("  C2) -- flag alongside JACOBSON-NONLOCAL-64. CRUCIALLY: the Lambda-power HIERARCHY")
        print("  (Lambda^4 >> Lambda^2 >> Lambda^0) is INVARIANT under the bracket -- the structure of the")
        print("  spectral-action expansion is robust; only the absolute energy MAGNITUDES (CC, A_s) inherit")
        print("  the factor-R^4 band. M_KK is a BRACKET, not a point.")
    else:
        print("  STRUCTURAL FAIL: either the gauge-route M_KK breaks the unification consistency, or a")
        print("  structural integrity check (canonical OOM-match / hierarchy / alias / rho-consistency)")
        print("  failed. Escalate; do NOT overturn CONST-FREEZE-42 route pins.")

    # ---- (7) data file (full float64 round-trip) ----
    value_str = (  # (local) compact, audit-greppable
        f"composite={composite};R={R:.15e};R_6sf={R:.6g};log10R={log10R:.15e};OOM_diff_MKK={OOM_diff_MKK:.15e};"
        f"oom_match={oom_match:.3e};oom_match_ok={oom_match_ok};"
        f"R2_a2_band={R2:.6f};R4_a0_band={R4:.6f};log10_R4={log10_R4:.6f};log10_R2={log10_R2:.6f};"
        f"abs_R_minus_1={abs_R_minus_1:.6f};PASS_band={PASS_BAND};"
        f"M_KK_gravity={M_KK_gravity:.6e};M_KK_kerner={M_KK_kerner:.6e};"
        f"a0_zeta={a_0_FW_zeta};a2_zeta={a_2_FW_zeta};"
        f"rho_Lambda_gravity={rho_Lambda_gravity:.6e};rho_Lambda_kerner={rho_Lambda_kerner:.6e};"
        f"rho_band={rho_band:.6f};rho_band_consistent={rho_band_consistent};"
        f"hierarchy_preserved={hierarchy_preserved};alias_ok={alias_ok};"
        f"predicted_sign={predicted_sign};computed_sign={computed_sign};"
        f"sign_verdict={sign_v};magnitude_verdict={mag_v};regime_verdict={regime_v};"
        f"w5_6_status={w5_6_status};gauge_route_tag={gauge_route_tag};"
        f"CLASS=FULL;regulator_pin=a_n_zeta;"
        f"finding=M_KK_bracket_real_factor_R4_band_on_absolute_a0_Lambda4_hierarchy_invariant"
    )

    np.savez(
        NPZ_OUT,
        gate_id=GATE_ID,
        # core deliverable (full float64)
        R=R, log10R=log10R, OOM_diff_MKK=OOM_diff_MKK, oom_match=oom_match, oom_match_ok=oom_match_ok,
        R2=R2, R4=R4, R0=R0, log10_R4=log10_R4, log10_R2=log10_R2,
        abs_R_minus_1=abs_R_minus_1, PASS_band=PASS_BAND,
        # route values
        M_KK=M_KK, M_KK_gravity=M_KK_gravity, M_KK_kerner=M_KK_kerner,
        a_0_FW_zeta=a_0_FW_zeta, a_2_FW_zeta=a_2_FW_zeta, a0_fold=a0_fold, a2_fold=a2_fold,
        # absolute magnitude propagation
        rho_Lambda_gravity=rho_Lambda_gravity, rho_Lambda_kerner=rho_Lambda_kerner,
        rho_band=rho_band, rho_band_consistent=rho_band_consistent, g2_term_band=g2_term_band,
        # hierarchy invariance
        powers=powers, band_factors=band_factors, hierarchy_preserved=hierarchy_preserved,
        alias_ok=alias_ok,
        # plan rounded-R cross-check
        R_plan_rounded=R_plan_rounded, R4_plan=R4_plan, plan_round_diff=plan_round_diff,
        # soft-dependency
        w5_6_status=(w5_6_status if w5_6_status is not None else "ABSENT"),
        gauge_route_tag=gauge_route_tag,
        # verdict
        predicted_sign=predicted_sign, computed_sign=computed_sign,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v, composite=composite,
        reading="M_KK_gravity_vs_Kerner_bracket_real_0.83_decade_R4_band_on_absolute_a0_Lambda4_only_magnitudes_inherit_hierarchy_robust",
    )
    print(f"\n  npz  -> {NPZ_OUT.relative_to(ROOT)}")

    # ---- (8) plot: two M_KK routes + Lambda^4/Lambda^2/Lambda^0 band propagation ----
    fig, axes = plt.subplots(1, 2, figsize=(13.4, 5.3))

    # Panel 1: the two M_KK routes (log scale) + the 0.83-decade bracket.
    ax = axes[0]
    route_labels = ["gravity route\n$1/(16\\pi G_N)$\n$\\sim a_2^\\zeta \\Lambda^2$",
                    "Kerner route\n$1/g^2 \\sim M_{KK}^{d-4}$vol"]  # (local)
    route_vals = [M_KK_gravity, M_KK_kerner]  # (local)
    xpos = np.arange(2)  # (local)
    bars = ax.bar(xpos, route_vals, color=["tab:blue", "tab:red"], alpha=0.85, edgecolor="k", zorder=3)
    for xi, vi in zip(xpos, route_vals):
        ax.annotate(f"{vi:.3e}\nGeV", (xi, vi), textcoords="offset points",
                    xytext=(0, 6), ha="center", fontsize=8.6)
    ax.set_yscale("log")
    ax.set_xticks(xpos)
    ax.set_xticklabels(route_labels, fontsize=8.4)
    ax.set_ylabel(r"$M_{KK}$  (GeV, log scale)")
    ax.set_title(fr"Two non-Abelian KK $M_{{KK}}$ routes"
                 "\n" fr"$R = M_{{KK,Kerner}}/M_{{KK,gravity}} = {R:.4f}$  "
                 fr"($\log_{{10}} R = {log10R:.4f}$, the 0.83-decade bracket)",
                 fontsize=9.6)
    # annotate the bracket span
    ax.annotate("", xy=(1, M_KK_kerner), xytext=(1, M_KK_gravity),
                arrowprops=dict(arrowstyle="<->", color="tab:green", lw=1.8))
    ax.annotate(fr"0.83 dec", (1.06, np.sqrt(M_KK_gravity * M_KK_kerner)),
                fontsize=8.4, color="tab:green", rotation=90, va="center")
    ax.grid(axis="y", ls=":", alpha=0.4)

    # Panel 2: Lambda^4/Lambda^2/Lambda^0 band propagation into absolute a0/a2/a4 magnitudes.
    ax = axes[1]
    band_labels = [r"$a_0$ vacuum" "\n" r"($\Lambda^4$, CC)" "\n" r"band $=R^4$",
                   r"$a_2$ gravity" "\n" r"($\Lambda^2$, $G_N$)" "\n" r"band $=R^2$",
                   r"$a_4$ YM/Higgs" "\n" r"($\Lambda^0$)" "\n" r"band $=R^0=1$"]  # (local)
    band_vals = [R4, R2, R0]  # (local)
    colors = ["tab:orange", "tab:purple", "tab:gray"]  # (local)
    xpos2 = np.arange(3)  # (local)
    ax.bar(xpos2, band_vals, color=colors, alpha=0.85, edgecolor="k", zorder=3)
    for xi, vi in zip(xpos2, band_vals):
        ax.annotate(f"{vi:.2f}x", (xi, vi), textcoords="offset points",
                    xytext=(0, 6), ha="center", fontsize=9.0, fontweight="bold")
    ax.axhline(1.0, color="k", ls="--", lw=1.2, zorder=2, label=r"no band ($R^0=1$)")
    ax.axhline(PASS_BAND + 1.0, color="green", ls=":", lw=1.2, zorder=2,
               label=fr"PASS-band $|R-1|\leq{PASS_BAND}$")
    ax.set_yscale("log")
    ax.set_xticks(xpos2)
    ax.set_xticklabels(band_labels, fontsize=8.2)
    ax.set_ylabel(r"absolute-magnitude band factor (log scale)")
    ax.set_title(f"{GATE_ID}  (composite: {composite})\n"
                 fr"$R^4={R4:.1f}\times$ on $a_0$; $R^2={R2:.1f}\times$ on $a_2$; "
                 r"$\Lambda$-hierarchy ($4\!\gg\!2\!\gg\!0$) INVARIANT",
                 fontsize=9.2)
    ax.legend(loc="upper right", fontsize=7.8)
    ax.grid(axis="y", ls=":", alpha=0.4)

    fig.tight_layout()
    fig.savefig(PNG_OUT, dpi=130)
    plt.close(fig)
    print(f"  png  -> {PNG_OUT.relative_to(ROOT)}")

    # ---- (9) dual-SHA + verdict line ----
    print("\n" + "-" * 78)
    print("Dual-SHA closure + verdict-line emission")
    print("-" * 78)
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_CONSTANTS, pins)
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    append_verdict(composite, value_str, audit_sha, content_sha, sign_v, mag_v, regime_v,
                   R, log10R, R2, R4, w5_6_status)
    print(f"\n  verdict line appended -> {VERDICT_FILE.relative_to(ROOT)}")

    # 4-tuple output tag (final non-verdict line per gate-verdicts.md "During computation")
    print(f"\n4-TUPLE OUTPUT TAG: (value=R={R:.6g}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
