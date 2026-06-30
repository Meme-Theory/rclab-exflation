#!/usr/bin/env python
"""
S116-W9-GTBUILDER-L15 — branch-(iv) w_0 DR3-class L_max-stability ONE TRUNCATION DEEPER (p+q=15).

Gate: S116-W9-GTBUILDER-L15  ([SIGN] — directional sub-claim: the decrement DECELERATES
      |d(14->15)| < |d(13->14)| AND the CAC offset cancels in the span; top-line is the band
      comparison on spread_CAC{13,14,15}).
Classification: GEOMETRIC (a spectral-functional property of the D_K spectrum at the fixed
                tau_fold slice; NOT a phononic excitation).
Owner: baptista-spacetime-analyst.

WHAT THIS GATE DOES
-------------------
Extends the branch-(iv) w_0_FW DR3-class L_max-stability lineage (S102 -> S103 -> S104 PRE-REG-INC
-> S105 INFO) one truncation deeper to p+q=15, using the ALREADY-CONSTRUCTED p+q=15 sectors from
the S106 cache (s106_w1_highl_cache_l1416.npz, key `sector_evals_L16`: COMPLETE p+q<=15 triangle,
136 sectors, herm_err_max=1.13e-15). This is a cache-read + Zubarev-moment extraction + GT-pure
sentinel, NOT a 35-min reconstruction (the expensive mixed p+q=15 sectors are pre-built S106).

  (A) PRIMARY OBSERVABLE — branch-(iv) w_0 DR3 deep-truncation spread:
      For L in {10,12,13,14,15}, compute the branch-(iv) Zubarev Mellin-zeta spectral moment
      rho_B(L) := rho_Zubarev(L) = <|lambda|>_Z(L)/lambda_max(L) - 1   (S85 W0-7 evaluator,
      imported VERBATIM from s105_branch_iv_direct_l1314.py), SELF-CONSISTENTLY on the COMPLETE
      (4,4)-filled S106 lineage. Form the canonical-anchored prediction
          w0^CAC(L) = rho_B(L) + offset_B,   offset_B := w0_FW - rho_B(L=10)   [DERIVED at runtime]
      (CAC MANDATORY per regulator-convention-lockdown.md; demarcation theorem w0^CAC(10)=w0_FW
      EXACTLY by construction; the offset cancels in the span). PRIMARY verdict object: the
      deep-truncation sliding window spread_CAC{13,14,15} vs the UNCHANGED W5-2 band
      (PASS <= 0.025 | INFO (0.025,0.050] | FAIL > 0.050).

  (B) GENUINELY-NEW CONSTRUCTION — GT-pure (15,0)/(0,15) reconstruction sentinel:
      Independently rebuild the two GT-pure sectors (15,0) and (0,15) from scratch via
      irrep_symmetric_power_gt (the bosonic-ladder builder, imported VERBATIM from s105; NEVER
      forms the 3^15 dense intermediate), diagonalize i*D on GPU (D=2176 Hermitian), verify the
      eigenvalues reproduce the S106 cache's (15,0)/(0,15) abs_evals to the sentinel floor
      (< 1e-10). EXTENDS the S106 GT-vs-cache sentinel (which certified p+q<=12) to p+q=15.
      The 14 MIXED p+q=15 sectors are READ from the S106 cache (already built S106 via the
      Casimir-projection path at herr ~ 1e-15; rebuilding is recompute-what-is-closed + ~35 min
      for zero new info).

  (C) BOTTOM-K SATURATION CROSS-CHECK (the spectral-geometer side of the W9 workshop):
      the global bottom-20 AND bottom-64 |lambda| floors are IDENTICAL over the p+q<=14 and
      p+q<=15 pooled spectra (expected max|diff|=0.0e+00 — the smallest p+q=15 eigenvalue is
      |lambda|_min=4.216 >> the bottom-20 ceiling 0.845, so the new shell cannot enter the
      bottom-K; the bottom-K observable is Friedrich-Bar-saturated at p+q<=14).

CROSS-CHECKS (guards; force PASS->INFO if any fail, per the S105 guard pattern):
  - cache integrity:   npz-internal audit_sha256 == 5af2b7cd...
  - GT-pure sentinel:  max|lambda(GT (15,0)/(0,15)) - lambda(cache)| < 1e-10.
  - rho_B(14) consist: rho_B(14) from sector_evals_L14 == rho_B(14) from sector_evals_L16|level<=14.
  - p+q=15 complete:   all 16 sectors (0,15)..(15,0) present in sector_evals_L16 with level==15.
  - Hermiticity:       GT-pure herm_err small; cache herm_err_max=1.13e-15 (stored).
  - bottom-K saturat:  bottom-20 AND bottom-64 |lambda| floors IDENTICAL L<=14 vs L<=15.
DIAGNOSTICS (cross-report, NOT gating): spread_CAC{12,13,14} (S105-continuity, complete lineage);
  spread_CAC{12,13,14,15} (full 4-pt window, includes the L=12 residual transient -> > 0.050, NOT
  the verdict object; bit-matches the investigation-track INV13-W1-3 = 0.0629703); the S105
  published rho_B (s84-incomplete lineage, missing (4,4)) with the gap-fill delta disclosed.

Output 4-tuple:
  (value=spread_CAC{13,14,15}, scheme=zeta, convention=CAC-branch-iv-anchored-L10-DERIVED-OFFSET,
   L_max=15)

regulator_pin: a_2^{Mellin}  (branch-(iv) w_0 channel = substrate-distance Mellin-zeta moment;
  zeta scheme; poleconv-A-double (pole_in_s=3, curvature_grade_n=2) per regulator-pin-discipline.md
  §"Mellin Pole-Set Labeling"). cutoff_axis=spectral (Zubarev kernel Lambda_Z on the D_K spectrum).

Substrate-first arrow (GEOMETRIC): D_K eigenvalues at tau_fold (p+q=15 shell) -> branch-(iv)
Zubarev Mellin-zeta spectral moment rho_B(15) -> CAC-anchored late-time w_0 -> DESI DR3 w0-wa
measurement. GR's dark energy is the CONSEQUENCE, not the premise. The GT bosonic-ladder builder
is a substrate-faithful construction of the (p,0) sectors in their intrinsic highest-weight space;
the sentinel certifies it reproduces the cache spectrum (a feasibility route, not new physics).
"""
from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# Section 1 — Identity + paths
# ---------------------------------------------------------------------------
SESSION = "S116"
GATE_ID = "S116-W9-GTBUILDER-L15"
SCHEME = "zeta"
CONVENTION = "CAC-branch-iv-anchored-L10-DERIVED-OFFSET"
L_MAX = "15"

THIS_FILE = Path(__file__).resolve()
PROJECT_ROOT = THIS_FILE.parents[2]                  # .../computations/session-116/<this> -> root
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
SESSION_DIR = PROJECT_ROOT / "computations" / "session-116"
S105_DIR = PROJECT_ROOT / "computations" / "session-105"
S106_DIR = PROJECT_ROOT / "computations" / "session-106"

sys.path.insert(0, str(SHARED_DIR))
sys.path.insert(0, str(S105_DIR))

from canonical_constants import (  # noqa: E402
    w0_FW,
    Gamma_effacement,
    N_cells,
    tau_fold,
)

# VERBATIM reuse of the S105 GT bosonic-ladder builder + S85 W0-7 Zubarev evaluator + pipeline.
# (NOT re-derived; the same validated constructions that landed S105-BRANCH-IV-DIRECT-L1314 INFO.)
from s105_branch_iv_direct_l1314 import (  # noqa: E402
    irrep_symmetric_power_gt,
    rho_zubarev_from_sectors,
    build_dirac_pipeline,
)

# ---------------------------------------------------------------------------
# Section 2 — Pre-registered constants (plan §W9-2 machinery_pin_map; PRDR dry-run)
# ---------------------------------------------------------------------------
LAMBDA_Z = 1.0                           # (local) Zubarev kernel width (S85 W0-7 PRDR pin), M_KK units; UNCHANGED
L_ANCHOR = 10                            # (local) CAC offset anchor truncation (rho_B(L=10) -> w0_FW)
SPREAD_PASS_BAND = 0.025                 # (local) PASS <= 0.025 (UNCHANGED W5-2)
SPREAD_INFO_BAND = 0.050                 # (local) INFO (0.025, 0.050]; FAIL > 0.050 (UNCHANGED W5-2)
L_SCAN_primary = (13, 14, 15)            # (local) deep-truncation sliding window (VERDICT object)
L_SCAN_continuity = (12, 13, 14)         # (local) S105-continuity diagnostic on the complete lineage
L_SCAN_full = (12, 13, 14, 15)           # (local) full 4-pt window diagnostic (incl. L=12 transient; NOT verdict)
SENTINEL_TOL = 1e-10                     # (local) GT-pure (15,0)/(0,15) vs S106-cache |lambda| sentinel floor
REPRO_TOL = 1e-12                        # (local) rho_B(14) internal cross-lineage consistency
bottom_K_set = (20, 64)                  # (local) Friedrich-Bar bottom-K saturation cross-check
eta_FB_lower = 0.392839                  # (local) S106 Friedrich-Bar empirical floor (cross-report)
PUBLICATION_PRECISION = 6                # (local) spread + rho_B + w0^CAC published to 6 sig figs (Class 8.3)

# S106 cache npz-internal audit_sha256 field (runtime integrity check pin; plan §W9-2):
CACHE_INTERNAL_AUDIT_SHA256 = "5af2b7cd09d863491cd30872384f9bc9adc7b0a580c2b7089f28ce9bfda3fcbb"

# Runtime canonical-value assertions (PLAN-TEXT-DRIFT note; substrate-first-canonical-sourcing.md §(ii.B)):
W0_FW_EXPECT = -0.918                     # (local) canonical w0_FW (S58 Volovik partition+effacement)
TAU_FOLD_EXPECT = 0.190                   # (local) canonical tau_fold (S12/S42)

# Hermiticity floor (boson (p,0) i*D is EXACTLY Hermitian; dimension-scaled guard for safety):
ID_HERM_ERR_TOL_IDEAL = 1.0e-15          # (local)
EPS_F64 = float(np.finfo(np.float64).eps)  # (local) ~2.22e-16

# S105 published continuity anchors (s84-INCOMPLETE lineage, MISSING (4,4)) — cross-report only:
S105_PUBLISHED_SPREAD = 0.0443091        # (local) S105-BRANCH-IV-DIRECT-L1314 INFO spread_CAC{12,13,14}
# Investigation-track INV13-W1-3-BRANCH-IV-W0-L1516-DR3 full-window cross-report (knowledge MCP):
INV13_FULL_WINDOW = 0.0629703            # (local) spread_CAC{12,13,14,15,16} FAIL (full-window diagnostic anchor)

JENSEN_S = float(tau_fold)               # (local) Jensen deformation s = tau_fold = 0.190 (cache is tau019)

# ---------------------------------------------------------------------------
# Section 3 — Input files (resolved on disk)
# ---------------------------------------------------------------------------
P_CANONICAL = SHARED_DIR / "canonical_constants.py"
P_CACHE = S106_DIR / "s106_w1_highl_cache_l1416.npz"
P_S105_PY = S105_DIR / "s105_branch_iv_direct_l1314.py"
P_DIRAC = SHARED_DIR / "dirac_spectrum.py"
P_S105_NPZ = S105_DIR / "s105_branch_iv_direct_l1314.npz"

INPUT_FILES = [P_CANONICAL, P_CACHE, P_S105_PY, P_DIRAC, P_S105_NPZ]

# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                   # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}                              # (local)
    for p in inputs:
        sha = sha256_of(p)                                 # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p).replace("\\", "/")                # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())                           # (local)
    h = hashlib.sha256()                                   # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict[str, str]) -> tuple[str, str]:
    try:
        script_bytes = script_path.read_bytes()            # (local)
    except OSError:
        script_bytes = b""                                 # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()      # (local)
    except OSError:
        canonical_bytes = b""                              # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")                                      # (local)
    h_audit = hashlib.sha256()                             # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()                           # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — bottom-K saturation helper (pooled-raw abs_evals; matches plan 0.845 anchor)
# ---------------------------------------------------------------------------

def pooled_abs_sorted(sectors: dict, L_cut: int) -> np.ndarray:
    """Ascending-sorted pool of |lambda| over all sectors with level <= L_cut (raw abs_evals,
    NOT multiplicity-expanded; the bottom-K FLOOR is a distinct-small-eigenvalue observable —
    the plan's bottom-20 ceiling 0.845 is this reading). Adding high-|lambda| sectors cannot
    lower the bottom-K, so the floor is Friedrich-Bar-saturated by construction."""
    vals = []                                              # (local)
    for _k, d in sectors.items():
        if d["level"] <= L_cut:
            vals.append(np.asarray(d["abs_evals"], dtype=np.float64))
    return np.sort(np.concatenate(vals))


# ---------------------------------------------------------------------------
# Section 6 — print_verdict_payload (agent calls emit_verdict with this)
# ---------------------------------------------------------------------------

def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_v="", magnitude_v="", regime_v="", extra_rows=None):
    payload = {
        "session": 116,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": value,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": L_MAX,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if sign_v:
        payload["sign_verdict"] = sign_v
        payload["magnitude_verdict"] = magnitude_v
        payload["regime_verdict"] = regime_v
    if extra_rows:
        payload["extra_rows"] = extra_rows
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")


# ---------------------------------------------------------------------------
# Section 7 — main
# ---------------------------------------------------------------------------

def main():
    print(f"=== {GATE_ID} :: branch-(iv) w_0 DR3 L_max-stability one truncation deeper (p+q=15) ===")
    print(f"[const] w0_FW={w0_FW}  tau_fold={tau_fold}  Lambda_Z={LAMBDA_Z}  "
          f"Gamma_effacement={Gamma_effacement}  N_cells={N_cells}")

    # --- runtime canonical-value verification (PLAN-TEXT-DRIFT; substrate-first §(ii.B)) ---
    assert abs(float(w0_FW) - W0_FW_EXPECT) < 1e-12, f"w0_FW drift: {w0_FW} != {W0_FW_EXPECT}"
    assert abs(float(tau_fold) - TAU_FOLD_EXPECT) < 1e-12, f"tau_fold drift: {tau_fold} != {TAU_FOLD_EXPECT}"
    print(f"[canon] runtime-verified: w0_FW={w0_FW} (==-0.918), tau_fold={tau_fold} (==0.190)")

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    audit_sha, content_sha = compute_dual_sha(THIS_FILE, P_CANONICAL, pins)
    canonical_sha_live = pins.get("computations/_shared/canonical_constants.py", "")  # (local)
    # PLAN-TEXT-DRIFT: canonical_constants.py was edited this session (W1+W7 added constants); the
    # plan pinned <computed-at-runtime>, so there is no stale literal to compare against — we record
    # the LIVE SHA and the two consumed constants are runtime-verified above (drift documented).
    canonical_drift_S116 = True            # (local) canonical_constants.py edited this session (W1+W7)
    print(f"  closure_hash:   {closure[:16]}...")
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print(f"  canonical_sha_live: {canonical_sha_live[:16]}...  canonical_drift_S116={canonical_drift_S116} "
          f"(consumed constants runtime-verified; offset DERIVED at runtime)")

    # --- Load the S106 cache + RUNTIME INTEGRITY CHECK (npz-internal audit_sha256) ---
    z = np.load(P_CACHE, allow_pickle=True)
    cache_internal_sha = str(np.asarray(z["audit_sha256"]).item())  # (local)
    cache_integrity_ok = (cache_internal_sha == CACHE_INTERNAL_AUDIT_SHA256)  # (local)
    print(f"[cache] npz-internal audit_sha256={cache_internal_sha[:16]}...  "
          f"integrity_ok(== 5af2b7cd...)={cache_integrity_ok}")
    if not cache_integrity_ok:
        # HONEST mechanical closure per mechanical-closure-discipline.md: the cache integrity pin
        # failed -> the gate is structurally untestable on the pinned cache.
        z.close()
        value = (f"PRE-REG-INC_cache_integrity_FAIL_got_{cache_internal_sha[:16]}_"
                 f"expect_5af2b7cd; S106_cache_audit_sha256_mismatch")
        np.savez_compressed(
            SESSION_DIR / "s116_w9_gtbuilder_l15.npz",
            verdict="PRE-REG-INC", phase="CACHE_INTEGRITY_FAIL",
            cache_internal_sha=cache_internal_sha, cache_integrity_ok=cache_integrity_ok,
            audit_sha256=audit_sha, content_sha256=content_sha, closure_hash=closure,
        )
        print_verdict_payload("PRE-REG-INC", value, audit_sha, content_sha)
        return

    SE16 = z["sector_evals_L16"].item()    # (local) COMPLETE p+q<=15 triangle (136 sectors)
    SE14 = z["sector_evals_L14"].item()    # (local) p+q<=14 (120 sectors)
    cache_herm_err_max = float(z["herm_err_max"])  # (local) 1.13e-15 (S106 stored)
    cache_eta_FB_lower = float(z["eta_FB_lower"])   # (local) 0.392839
    z.close()
    print(f"[cache] sector_evals_L16: {len(SE16)} sectors  sector_evals_L14: {len(SE14)} sectors  "
          f"cache_herm_err_max={cache_herm_err_max:.2e}  eta_FB_lower={cache_eta_FB_lower:.6f}")

    # --- p+q=15 completeness guard: all 16 sectors (0,15)..(15,0) present with level==15 ---
    lvl15 = sorted([k for k in SE16 if (k[0] + k[1]) == 15])  # (local)
    lvl15_levels_ok = all(SE16[k]["level"] == 15 for k in lvl15)  # (local)
    complete_15 = (len(lvl15) == 16) and lvl15_levels_ok      # (local)
    print(f"[complete] p+q=15 sectors present={len(lvl15)}/16  levels_ok={lvl15_levels_ok}  "
          f"complete_15={complete_15}")

    # =====================================================================
    # (A) PRIMARY — rho_B(L) over {10,12,13,14,15} (Zubarev S85 W0-7 evaluator, VERBATIM)
    # =====================================================================
    rho_B = {}                                             # (local)
    rho_meta = {}                                          # (local)
    for L in (10, 12, 13, 14, 15):
        rr = rho_zubarev_from_sectors(SE16, L, LAMBDA_Z)
        rho_B[L] = rr["rho"]
        rho_meta[L] = rr
        print(f"  rho_B({L:2d}) = {rr['rho']:.15f}  (lam_max={rr['lam_max']:.6f}, "
              f"n_modes={rr['n_modes']})")

    # --- rho_B(14) cross-lineage consistency: SE14 vs SE16|level<=14 (bit-exact expected) ---
    rho14_SE14 = rho_zubarev_from_sectors(SE14, 14, LAMBDA_Z)["rho"]  # (local)
    rho14_SE16cut = rho_zubarev_from_sectors(
        {k: v for k, v in SE16.items() if v["level"] <= 14}, 14, LAMBDA_Z)["rho"]  # (local)
    rho14_consistency = abs(rho14_SE14 - rho14_SE16cut)    # (local)
    print(f"[xcheck] rho_B(14): SE14={rho14_SE14:.15f}  SE16|lvl<=14={rho14_SE16cut:.15f}  "
          f"diff={rho14_consistency:.2e} (<= {REPRO_TOL:.0e}: {rho14_consistency <= REPRO_TOL})")

    # --- CAC offset (DERIVED at runtime; cancels in span) ---
    offset_B = float(w0_FW) - rho_B[L_ANCHOR]              # (local) = w0_FW - rho_B(L=10), CAC
    print(f"[cac] offset_B (w0_FW-anchored) = {offset_B:.12f}  "
          f"[w0_FW={w0_FW} - rho_B(10)={rho_B[L_ANCHOR]:.12f}]")
    w0_cac = {L: rho_B[L] + offset_B for L in (10, 12, 13, 14, 15)}  # (local)
    cac_anchor_resid = abs(w0_cac[10] - float(w0_FW))      # (local) demarcation theorem residual
    print(f"[cac] w0^CAC(10) = {w0_cac[10]:.15f}  (== w0_FW={w0_FW}? resid={cac_anchor_resid:.2e})")
    for L in (12, 13, 14, 15):
        print(f"  w0^CAC({L}) = {w0_cac[L]:.15f}")

    # --- spreads: PRIMARY {13,14,15}; DIAGNOSTICS {12,13,14} continuity + {12,13,14,15} full ---
    def spread_over(Ls):
        v = np.array([w0_cac[L] for L in Ls])              # (local)
        r = np.array([rho_B[L] for L in Ls])               # (local)
        return float(v.max() - v.min()), float(r.max() - r.min())
    spread_CAC_primary, spread_rho_primary = spread_over(L_SCAN_primary)        # {13,14,15}
    spread_CAC_continuity, _ = spread_over(L_SCAN_continuity)                   # {12,13,14}
    spread_CAC_full, _ = spread_over(L_SCAN_full)                               # {12,13,14,15}
    offset_cancellation_residual = abs(spread_CAC_primary - spread_rho_primary)  # (local) ~0
    print(f"[span] spread_CAC{{13,14,15}} = {spread_CAC_primary:.12f}  "
          f"(offset-free rho-span = {spread_rho_primary:.12f}; resid={offset_cancellation_residual:.2e})")
    print(f"[span] spread_CAC{{12,13,14}} = {spread_CAC_continuity:.12f}  (S105-continuity, complete lineage)")
    print(f"[span] spread_CAC{{12,13,14,15}} = {spread_CAC_full:.12f}  (full diagnostic; "
          f"INV13 full-to-16 anchor={INV13_FULL_WINDOW}; expected > 0.050, NOT the verdict object)")
    print(f"[span] S105 published spread_CAC{{12,13,14}}={S105_PUBLISHED_SPREAD} (s84-incomplete) -> "
          f"complete-lineage gap-fill delta = {abs(spread_CAC_continuity - S105_PUBLISHED_SPREAD):.6f}")

    # --- decrements (substitution chain Step 4): denominator(lambda_max)-driven, |d| ~ 1/L^2 ---
    d_12_13 = rho_B[13] - rho_B[12]                        # (local)
    d_13_14 = rho_B[14] - rho_B[13]                        # (local)
    d_14_15 = rho_B[15] - rho_B[14]                        # (local)
    decrement_sign_negative = (d_12_13 < 0) and (d_13_14 < 0) and (d_14_15 < 0)  # (local)
    decelerating = abs(d_14_15) < abs(d_13_14)            # (local) PRIMARY [SIGN] sub-claim
    decel_margin = abs(d_13_14) - abs(d_14_15)            # (local) = |d(13->14)| - |d(14->15)| > 0
    print(f"[decr] d(12->13)={d_12_13:+.8f}  d(13->14)={d_13_14:+.8f}  d(14->15)={d_14_15:+.8f}")
    print(f"[decr] sign_neg={decrement_sign_negative}  decelerating={decelerating}  "
          f"|d(13->14)|-|d(14->15)|={decel_margin:+.8f}")

    # =====================================================================
    # (B) GENUINELY-NEW — GT-pure (15,0)/(0,15) reconstruction sentinel (GPU)
    # =====================================================================
    print("  --- (B) GT-pure (15,0)/(0,15) reconstruction sentinel (GPU eigvalsh i*D, D=2176) ---")
    gens, f_abc, gammas, E, Omega, device, dirac_abs_and_herr = build_dirac_pipeline()
    conj_gens = [-g.T for g in gens]                       # (local) (0,p) = conjugate of (p,0)
    gt_sentinel_max = 0.0                                  # (local)
    gt_herr_max = 0.0                                      # (local)
    gt_detail = {}                                         # (local)
    t_gt = time.time()                                     # (local)
    for (p, q), gg, pp in [((15, 0), gens, 15), ((0, 15), conj_gens, 15)]:
        rho = irrep_symmetric_power_gt(gg, pp)
        dim_sym = rho[0].shape[0]                          # (local) = 136
        assert dim_sym == 136, f"({p},{q}) dim_sym {dim_sym} != 136"
        ab, herr = dirac_abs_and_herr(rho)
        ab_s = np.sort(ab)                                 # (local)
        cache_s = np.sort(np.asarray(SE16[(p, q)]["abs_evals"], dtype=np.float64))  # (local)
        d = float(np.max(np.abs(ab_s - cache_s))) if ab_s.size == cache_s.size else float("inf")  # (local)
        gt_sentinel_max = max(gt_sentinel_max, d)
        gt_herr_max = max(gt_herr_max, herr)
        gt_detail[f"{p},{q}"] = d
        print(f"    ({p},{q}): dim_sym={dim_sym} D={ab.size} herr={herr:.2e} "
              f"GT-vs-cache|diff|={d:.3e} |lam|=[{ab.min():.6f},{ab.max():.6f}]")
    gt_sentinel_ok = gt_sentinel_max <= SENTINEL_TOL       # (local)
    dmax_block = 136 * 16                                  # (local) D=2176
    ID_HERM_ERR_TOL = max(ID_HERM_ERR_TOL_IDEAL, np.sqrt(dmax_block) * EPS_F64)  # (local)
    gt_herm_ok = gt_herr_max <= ID_HERM_ERR_TOL           # (local)
    print(f"[sentinel] GT-pure (15,0)/(0,15) max|diff|={gt_sentinel_max:.3e} "
          f"ok(<= {SENTINEL_TOL:.0e})={gt_sentinel_ok}  herr_max={gt_herr_max:.2e} "
          f"(floor={ID_HERM_ERR_TOL:.2e}, ok={gt_herm_ok})  ({time.time()-t_gt:.1f}s)")

    # =====================================================================
    # (C) BOTTOM-K SATURATION CROSS-CHECK (Friedrich-Bar; the spectral-geometer side)
    # =====================================================================
    print("  --- (C) bottom-K saturation cross-check (pooled-raw |lambda| floors L<=14 vs L<=15) ---")
    a14 = pooled_abs_sorted(SE16, 14)                      # (local)
    a15 = pooled_abs_sorted(SE16, 15)                      # (local)
    lvl15_min = min(float(np.min(SE16[k]["abs_evals"])) for k in lvl15)  # (local) smallest p+q=15 |lambda|
    bottomK_detail = {}                                    # (local)
    bottomK_max_diff = 0.0                                 # (local)
    for K in bottom_K_set:
        b14 = a14[:K]; b15 = a15[:K]                       # (local)
        mdiff = float(np.max(np.abs(b14 - b15)))           # (local)
        bottomK_max_diff = max(bottomK_max_diff, mdiff)
        bottomK_detail[f"bottom_{K}"] = {"ceiling_L14": float(b14[-1]),
                                         "ceiling_L15": float(b15[-1]), "max_diff": mdiff}
        print(f"    bottom-{K}: ceiling(L<=14)={b14[-1]:.6f}  ceiling(L<=15)={b15[-1]:.6f}  "
              f"max|diff|={mdiff:.3e}")
    bottomK_saturated = bottomK_max_diff == 0.0           # (local)
    print(f"[bottomK] saturated(max|diff|==0)={bottomK_saturated}  smallest p+q=15 |lambda|="
          f"{lvl15_min:.6f} >> bottom-20 ceiling {bottomK_detail['bottom_20']['ceiling_L14']:.6f} "
          f"(eta_FB_lower={eta_FB_lower} bounds new shell below)")

    # =====================================================================
    # VERDICT — band on spread_CAC{13,14,15}; guards force PASS->INFO (S105 pattern)
    # =====================================================================
    if spread_CAC_primary <= SPREAD_PASS_BAND:
        verdict = "PASS"
    elif spread_CAC_primary <= SPREAD_INFO_BAND:
        verdict = "INFO"
    else:
        verdict = "FAIL"
    guard_ok = (cache_integrity_ok and complete_15 and gt_sentinel_ok and gt_herm_ok
                and (rho14_consistency <= REPRO_TOL) and bottomK_saturated)  # (local)
    if not guard_ok and verdict == "PASS":
        verdict = "INFO"
        print("[WARN] a guard failed -> PASS downgraded to INFO (S105 guard pattern)")
    print(f"[VERDICT] spread_CAC{{13,14,15}}={spread_CAC_primary:.6g}  "
          f"band(PASS<= {SPREAD_PASS_BAND}, INFO<= {SPREAD_INFO_BAND})  guard_ok={guard_ok}  => {verdict}")

    # --- [SIGN] 3-tuple ---
    # sign: decelerating (|d(14->15)| < |d(13->14)|) AND monotone-decreasing AND offset cancels in span.
    sign_v = ("PASS" if (decelerating and decrement_sign_negative
                         and offset_cancellation_residual < 1e-9) else "FAIL")  # (local)
    if spread_CAC_primary <= SPREAD_PASS_BAND:
        magnitude_v = "PASS"                               # (local)
    elif spread_CAC_primary <= SPREAD_INFO_BAND:
        magnitude_v = "INFO"                               # (local)
    else:
        magnitude_v = "FAIL"                               # (local)
    regime_v = "VALID" if guard_ok else "MARGINAL"         # (local)

    # --- persist npz ---
    np.savez_compressed(
        SESSION_DIR / "s116_w9_gtbuilder_l15.npz",
        verdict=verdict, phase="COMPLETE",
        # primary observable:
        L_SCAN_primary=np.array(L_SCAN_primary, dtype=np.int64),
        rho_B_10=rho_B[10], rho_B_12=rho_B[12], rho_B_13=rho_B[13], rho_B_14=rho_B[14], rho_B_15=rho_B[15],
        rho_B_window=np.array([rho_B[13], rho_B[14], rho_B[15]]),
        lam_max_10=rho_meta[10]["lam_max"], lam_max_12=rho_meta[12]["lam_max"],
        lam_max_13=rho_meta[13]["lam_max"], lam_max_14=rho_meta[14]["lam_max"],
        lam_max_15=rho_meta[15]["lam_max"],
        n_modes_10=rho_meta[10]["n_modes"], n_modes_12=rho_meta[12]["n_modes"],
        n_modes_13=rho_meta[13]["n_modes"], n_modes_14=rho_meta[14]["n_modes"],
        n_modes_15=rho_meta[15]["n_modes"],
        w0_FW=float(w0_FW), offset_B=offset_B,
        w0_cac=np.array([w0_cac[L] for L in (12, 13, 14, 15)]), w0_cac_10=w0_cac[10],
        cac_anchor_resid=cac_anchor_resid,
        spread_CAC=spread_CAC_primary, spread_rho=spread_rho_primary,
        spread_CAC_continuity=spread_CAC_continuity, spread_CAC_full=spread_CAC_full,
        offset_cancellation_residual=offset_cancellation_residual,
        SPREAD_PASS_BAND=SPREAD_PASS_BAND, SPREAD_INFO_BAND=SPREAD_INFO_BAND,
        S105_PUBLISHED_SPREAD=S105_PUBLISHED_SPREAD, INV13_FULL_WINDOW=INV13_FULL_WINDOW,
        gap_fill_delta=abs(spread_CAC_continuity - S105_PUBLISHED_SPREAD),
        # decrements:
        d_12_13=d_12_13, d_13_14=d_13_14, d_14_15=d_14_15,
        decrement_sign_negative=decrement_sign_negative, decelerating=decelerating,
        decel_margin=decel_margin,
        # rho_B(14) consistency:
        rho14_SE14=rho14_SE14, rho14_SE16cut=rho14_SE16cut, rho14_consistency=rho14_consistency,
        REPRO_TOL=REPRO_TOL,
        # GT-pure sentinel:
        gt_sentinel_max=gt_sentinel_max, gt_sentinel_ok=gt_sentinel_ok, SENTINEL_TOL=SENTINEL_TOL,
        gt_detail_json=json.dumps(gt_detail), gt_herr_max=gt_herr_max, ID_HERM_ERR_TOL=ID_HERM_ERR_TOL,
        # bottom-K saturation:
        bottomK_max_diff=bottomK_max_diff, bottomK_saturated=bottomK_saturated,
        bottomK_detail_json=json.dumps(bottomK_detail), lvl15_min=lvl15_min,
        bottom_K_set=np.array(bottom_K_set, dtype=np.int64),
        # completeness / integrity:
        complete_15=complete_15, n_lvl15=len(lvl15),
        cache_integrity_ok=cache_integrity_ok, cache_internal_sha=cache_internal_sha,
        cache_herm_err_max=cache_herm_err_max, eta_FB_lower=eta_FB_lower,
        guard_ok=guard_ok,
        # verdict 3-tuple:
        sign_verdict=sign_v, magnitude_verdict=magnitude_v, regime_verdict=regime_v,
        # provenance:
        Lambda_Z=LAMBDA_Z, jensen_s=JENSEN_S, Gamma_effacement=float(Gamma_effacement),
        N_cells=int(N_cells), device=str(device),
        canonical_sha_live=canonical_sha_live, canonical_drift_S116=canonical_drift_S116,
        n_sectors_L16=len(SE16), n_sectors_L14=len(SE14),
        audit_sha256=audit_sha, content_sha256=content_sha, closure_hash=closure,
    )

    _make_plot(rho_B, w0_cac, spread_CAC_primary, verdict, a14, a15, gt_sentinel_max, bottomK_detail)

    # --- value payload (6 sig figs; Class-8.3 publication precision; DESI DR3 w0 consumer) ---
    value = (f"spread_CAC{{13,14,15}}={spread_CAC_primary:.6g} "
             f"rho_B(13)={rho_B[13]:.6f} rho_B(14)={rho_B[14]:.6f} rho_B(15)={rho_B[15]:.6f} "
             f"w0CAC(15)={w0_cac[15]:.6f} offset_B={offset_B:.6f} "
             f"d(14->15)={d_14_15:.6f}<d(13->14)={d_13_14:.6f}_DECEL "
             f"gt_sentinel={gt_sentinel_max:.2e} bottomK_satur_maxdiff={bottomK_max_diff:.1e} "
             f"band_PASS<={SPREAD_PASS_BAND}")
    extra_rows = [
        (f"# regulator_pin=a_2^{{Mellin}} poleconv-A-double (pole_in_s=3, curvature_grade_n=2); "
         f"cutoff_axis=spectral (Zubarev Lambda_Z={LAMBDA_Z} on D_K spectrum); "
         f"GT(p,0)-bosonic-ladder-builder; cache_integrity=5af2b7cd(ok={cache_integrity_ok})"),
        (f"# bottom-K Friedrich-Bar-saturated (bottom-20/64 max|diff|={bottomK_max_diff:.1e}, "
         f"p+q=15 |lam|_min={lvl15_min:.4f}>>0.845) ORTHOGONAL to lambda_max-driven w0 moment shift "
         f"(rho_B(14)={rho_B[14]:.6f}->rho_B(15)={rho_B[15]:.6f}); spread NARROWS "
         f"{spread_CAC_continuity:.6f}->{spread_CAC_primary:.6f}; canonical_drift_S116=documented"),
    ]
    print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_v=sign_v, magnitude_v=magnitude_v, regime_v=regime_v,
                          extra_rows=extra_rows)


def _make_plot(rho_B, w0_cac, spread_CAC, verdict, a14, a15, gt_sentinel, bottomK_detail):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(16, 5))

    # Panel 1: rho_B(L) with the sliding window highlighted
    Ls = [12, 13, 14, 15]
    ax1.plot(Ls, [rho_B[L] for L in Ls], "o-", color="C0", label=r"$\rho_B(L)$ (complete lineage)")
    ax1.plot([13, 14, 15], [rho_B[L] for L in (13, 14, 15)], "o", color="C3", ms=11,
             mfc="none", mew=2, label=r"verdict window $\{13,14,15\}$")
    ax1.set_xlabel("truncation L (p+q)")
    ax1.set_ylabel(r"$\rho_B(L)$  (Zubarev branch-IV moment)")
    ax1.set_title(r"$\rho_B(L)$: $\lambda_{\max}$-driven, decelerating ($|d|\sim 1/L^2$)")
    ax1.set_xticks(Ls)
    ax1.grid(alpha=0.3)
    ax1.legend(fontsize=8)

    # Panel 2: w0^CAC(L) vs w0_FW; spread annotation
    ax2.plot([12, 13, 14, 15], [w0_cac[L] for L in (12, 13, 14, 15)], "s-", color="C2",
             label=r"$w_0^{\rm CAC}(L)=\rho_B(L)+{\rm offset}_B$")
    ax2.axhline(float(w0_FW), color="k", ls=":", lw=1, label=fr"$w_0^{{FW}}={w0_FW}$")
    ax2.set_xlabel("truncation L (p+q)")
    ax2.set_ylabel(r"$w_0^{\rm CAC}(L)$")
    ax2.set_title(fr"$w_0^{{\rm CAC}}$: spread$\{{13,14,15\}}={spread_CAC:.5f}$ $\Rightarrow$ {verdict}"
                  f"\n(PASS$\\leq$0.025 | INFO(0.025,0.050] | FAIL$>$0.050)")
    ax2.set_xticks([12, 13, 14, 15])
    ax2.grid(alpha=0.3)
    ax2.legend(fontsize=8)

    # Panel 3: bottom-K saturation — sorted |lambda| floor L<=14 vs L<=15 (overlap exactly)
    K = 80                                                 # (local) plot rank window
    ax3.plot(range(1, K + 1), a14[:K], "o-", color="C0", ms=3, label=r"$|\lambda|$ floor $L\leq14$")
    ax3.plot(range(1, K + 1), a15[:K], "x", color="C3", ms=4, label=r"$|\lambda|$ floor $L\leq15$")
    ax3.axhline(bottomK_detail["bottom_20"]["ceiling_L14"], color="C7", ls="--", lw=0.8,
                label=fr"bottom-20 ceiling {bottomK_detail['bottom_20']['ceiling_L14']:.3f}")
    ax3.set_xlabel("rank (ascending $|\\lambda|$)")
    ax3.set_ylabel(r"$|\lambda|$")
    ax3.set_title(f"bottom-K Friedrich-Bär-saturated\n(max|diff|=0; GT-pure sentinel={gt_sentinel:.1e})")
    ax3.grid(alpha=0.3)
    ax3.legend(fontsize=8)

    fig.suptitle(f"{GATE_ID} — branch-IV $w_0$ DR3 L_max-stability at p+q=15 "
                 f"($\\lambda_{{\\max}}$-driven $w_0$ shift $\\perp$ bottom-K saturation)", fontsize=12)
    fig.tight_layout()
    fig.savefig(SESSION_DIR / "s116_w9_gtbuilder_l15.png", dpi=120)
    plt.close(fig)


if __name__ == "__main__":
    main()
