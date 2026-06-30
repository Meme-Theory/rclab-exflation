#!/usr/bin/env python
"""
INV13-W1-3-BRANCH-IV-W0-L1516-DR3 — branch-(iv) w_0(L) DR3-readiness truncation test
at L_max in {15,16}: extend the S105 spread_CAC window from {12,13,14} to {12,13,14,15,16}.

Gate: INV13-W1-3-BRANCH-IV-W0-L1516-DR3  ([VERIFY]; band comparison on spread_CAC).
Classification: GEOMETRIC.  Track: investigation-13.

WHAT THIS GATE DOES
-------------------
The S105 gate (S105-BRANCH-IV-DIRECT-L1314, INFO) computed the deep-truncation CAC spread of the
branch-(iv) late-time w_0 Zubarev moment over L in {12,13,14} = 0.0443091 (INFO band, 0.025<x<=0.05).
This gate pushes the truncation window to L in {12,13,14,15,16}, consuming the EXISTING S106 high-L
cache (s106_w1_highl_cache_l1416.npz) which already holds:
    - sector_evals_L14: 120 sectors, levels 0..14 COMPLETE (L14_truncation_consistent=True)
    - sector_evals_L16: 136 sectors, levels 0..15 COMPLETE; NO level-16 sectors (the 17 missing
      p+q=16 sectors are Friedrich-Bar-bounded, in fb_bounded_sectors, L16_operational=15)
    - the S106 build's GT-vs-cache spectral sentinel already PASSed at sentinel_max=7.5e-14.

NO irrep construction, NO GPU diagonalization is performed here: the eigenvalues are PRE-BUILT in
the S106 cache (the cuda:0 GT-builder work was done at S106 build-time; this gate is on the
CONSUMPTION side — the substrate spectra are a deterministic pure function of (A_K,H_K,D_K) at
tau_fold and live in the cache). This is an honest operational deviation from the plan §W1-3
GPU_path pin (which prescribes torch.linalg cuda:0 for the per-block eigvals): the per-block
eigvals at p+q in {15,16} were ALREADY computed at S106 build on cuda:0, so re-diagonalizing them
here would be redundant. The gate re-verifies the cache SHA + the S106 sentinel state instead.

MOMENT-SENTINEL (MANDATORY, plan §W1-3 + spawn prompt): BEFORE consuming any new sector, reproduce
rho_B(L=8,10,12) from the s84 master cache against the recorded EXPECT_RHO anchors bit-exact (the
Zubarev-evaluator self-consistency sentinel). NO new-sector consumption before this PASSes.

For each L in {12,13,14,15,16}: truncate the appropriate cache dict at p+q<=L, compute the
branch-(iv) late-time w_0 Zubarev Mellin-zeta spectral moment rho_B(L) (S85 W0-7 verbatim formula,
identical to the S103/S104/S105 evaluator); form the canonical-anchored prediction
    w0^CAC(L) = rho_B(L) + offset_B,   offset_B := w0_FW - rho_B(L=10)   [DERIVED at runtime]
(CAC MANDATORY, RDC FORBIDDEN per regulator-convention-lockdown.md demarcation theorem:
 w0^CAC(L=10) = w0_FW EXACTLY by construction; the effacement-preservation criterion). Evaluate
    spread_CAC = max_{L in {12,...,16}} w0^CAC(L) - min_{...} w0^CAC(L)
               = max_L rho_B(L) - min_L rho_B(L)   [offset cancels EXACTLY in the span].

  Data path per L:
    L in {12,13,14}: sector_evals_L14 truncated at p+q<=L (levels 0..14 COMPLETE).
    L = 15:          sector_evals_L16 truncated at p+q<=15 (level-15 sectors INCLUDED; the genuinely
                     NEW data point relative to the S105 {12,13,14} window).
    L = 16:          sector_evals_L16 truncated at p+q<=16 == truncated at p+q<=15 (the 17 level-16
                     sectors are FB-bounded, ABSENT from the cache: their |lambda|_min >=
                     eta_FB_lower*sqrt(C_2+1) exceeds the bottom-K observable ceiling). Hence
                     rho_B(16) == rho_B(15) EXACTLY (operational L=15 saturation, math-scripts.md
                     truncation-saturation theorem). L_max_plan={14,16}, L_max_operational=15.

Verdict band (UNCHANGED from S105 / W5-2): PASS spread_CAC <= 0.025 | INFO (0.025, 0.050] | FAIL > 0.050.
The S105 value over {12,13,14} is 0.0443091 (INFO). Adding L=15 (and the FB-saturated L=16, equal to
L=15) tests whether the Friedrich-Bar tail pulls the spread below 0.025 (PASS, DR3-ready) or it stays
in the INFO band (reproduces-but-not-converged). OPEN VERDICT — the new rho_B(15) is the data.

CROSS-CHECKS:
  - moment-sentinel: rho_B(8,10,12) from s84 cache == EXPECT_RHO bit-exact (GATING, runs first).
  - rho_B(12,13,14) recomputed here == the S105 recorded values (continuity of the evaluator).
  - L14-dict vs L16-dict bit-exact agreement on shared sectors (S106 internal consistency, 0.0e+00).
  - offset cancellation residual |spread_CAC - spread_rho| ~ 0 (algebraic; the substitution-chain core).
  - CAC anchor residual |w0^CAC(L=10) - w0_FW| ~ 0 (effacement-preservation, by construction).

Output 4-tuple:
  (value=<computed>, scheme=zeta, convention=CAC-branch-iv-anchored-L10-DERIVED-OFFSET, L_max={12,13,14,15,16})

regulator_pin: a_2^{Mellin}  (branch-(iv) w_0 channel = substrate-distance Mellin-zeta moment; zeta
scheme; pole convention poleconv-A-double (s=3 substrate-distance-1, n=2)) — carried verbatim from
the S105 ancestor.

Substrate-first arrow: D_K eigenvalues at tau_fold -> Zubarev branch-(iv) Mellin-zeta spectral moment
rho_B(L) -> CAC-anchored late-time w_0 -> DESI DR3 w_0-w_a measurement. w_0 IS a spectral moment of
the substrate; the L_max -> {15,16} truncation-stability is the substrate's own convergence to its
continuum image (Level-1 single-tau-slice substrate-IS at tau_fold). This gate tests truncation-
stability ONLY; it does NOT re-litigate the separately-settled branch-(iv) derivation-admissibility
(S101-W0-BRANCH-IV-EVALUATOR). The CAC binding form preserves the effacement anchor.
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
SESSION_NUM = 13                                   # (local) investigation number
GATE_ID = "INV13-W1-3-BRANCH-IV-W0-L1516-DR3"
SCHEME = "zeta"
CONVENTION = "CAC-branch-iv-anchored-L10-DERIVED-OFFSET"
L_MAX = "{12,13,14,15,16}"

THIS_FILE = Path(__file__).resolve()
PROJECT_ROOT = THIS_FILE.parents[2]                # .../computations/investigation-13/<this> -> root
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
INV_DIR = PROJECT_ROOT / "computations" / "investigation-13"

sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import (  # noqa: E402
    w0_FW,
    Gamma_effacement,
    N_cells,
    tau_fold,
)

# ---------------------------------------------------------------------------
# Section 2 — Pre-registered constants (plan §W1-3; inherited from S105 ancestor)
# ---------------------------------------------------------------------------
W0_B = -0.842454                          # (local) branch-(iv) canonical (S85 W10-2; S102/S103/S104/S105 cross-report anchor)
SENTINEL_TOL = 1e-10                      # (local) moment-sentinel bit-exact floor (s84 Zubarev recompute; S106 sentinel_ok at max 7.5e-14)
REPRO_TOL = 1e-12                         # (local) rho-recompute reproduction abs_tol (S105 hit ~1e-16 vs EXPECT)
SPREAD_PASS_BAND = 0.025                  # (local) PASS <= 0.025 (UNCHANGED W5-2/S105)
SPREAD_INFO_BAND = 0.050                  # (local) INFO (0.025, 0.050]; FAIL > 0.050
L_SCAN = (12, 13, 14, 15, 16)             # (local) deep-truncation CAC spread window (regulator axis, DR3-class)
L_ANCHOR = 10                             # (local) canonical CAC anchor truncation (rho_B(L=10) -> w0_FW)
LAMBDA_Z = 1.0                            # (local) Zubarev kernel width (S85 W0-7 PRDR pin), M_KK units
PUBLICATION_PRECISION = 6                 # (local) spread + w0^CAC + rho_B published to 6 sig figs
OFFSET_CANCELLATION_TOL = 1e-9            # (local) |spread_CAC - spread_rho| algebraic-cancellation floor
CAC_ANCHOR_RESID_TOL = 1e-9              # (local) |w0^CAC(L=10) - w0_FW| effacement-preservation floor

L_MAX_PLAN = (14, 16)                     # (local) plan L_max (math-scripts.md item 3 record)
L_MAX_OPERATIONAL = 15                    # (local) L16 Friedrich-Bar-saturated at operational L=15

# Moment-sentinel anchors (S103/S104/S105 record; the Zubarev-evaluator self-consistency cross-anchor):
EXPECT_RHO = {8: -0.5044659979116969, 10: -0.5771725805120294, 12: -0.634885419265151}  # (local)

# S105 recorded deep-truncation values (continuity-of-evaluator cross-check for the {12,13,14} window):
S105_RHO = {12: -0.634885419265151, 13: -0.646653, 14: -0.657020}  # (local) S105 npz rho_B (13/14 to FB-prior sig figs; 12 exact)
S105_SPREAD_CAC = 0.0443091               # (local) S105 spread over {12,13,14} (the INFO datum this gate extends)

OFFSET_ZUBAREV_S86 = -0.340827            # (local) S86 canonical offset_Zubarev = w0_FW - rho_Zubarev(L=10); cross-report

JENSEN_S = float(tau_fold)                # (local) Jensen deformation parameter s = tau_fold = 0.190 (cache is tau019)

# ---------------------------------------------------------------------------
# Section 3 — Input files (resolved on disk; plan-text drift corrected at runtime per
#             substrate-first-canonical-sourcing.md §(ii.B))
# ---------------------------------------------------------------------------
P_CANONICAL = SHARED_DIR / "canonical_constants.py"
P_CACHE_S84 = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
P_CACHE_S106 = PROJECT_ROOT / "computations" / "session-106" / "s106_w1_highl_cache_l1416.npz"
P_S105_SCRIPT = PROJECT_ROOT / "computations" / "session-105" / "s105_branch_iv_direct_l1314.py"

INPUT_FILES = [P_CANONICAL, P_CACHE_S84, P_CACHE_S106, P_S105_SCRIPT]

# Plan-freeze pin (pre-W1-1-prereq baseline; the runtime SHA differs per §(ii.B) plan-text drift):
CANONICAL_PLANFREEZE_SHA = "e6829db013a713a4e56a4ca7d72e41f522bd3e3caea1bc0488ef17e0460bba34"  # (local)
S106_PINNED_SHA = "e6bc3af86a3fa7ac23cf476d86357f051ba4ced6be26fe3522622cbf61bdf6ce"            # (local)
S84_PINNED_SHA = "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9"             # (local)

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
# Section 5 — rho_Zubarev(L) kernel (S85 W0-7 verbatim formula; identical to S103/S104/S105 evaluator)
# ---------------------------------------------------------------------------

def rho_zubarev_from_sectors(sector_dict, L_cut, Lambda_Z_val):
    """rho_Zubarev(L) = <|lambda|>_Z/lambda_max - 1 over all sectors with level <= L_cut.

    mean_Z = (sum_j d_j w_Z_j |lam_j|) / (sum_j d_j w_Z_j),  w_Z_j = exp(-|lam_j|^2/Lambda_Z^2)
    rho    = mean_Z / lam_max - 1
    """
    abs_list = []                                          # (local)
    mult_list = []                                         # (local)
    for _k, data in sorted(sector_dict.items()):
        if data["level"] <= L_cut:
            d_irrep = int(data["dim"])                     # (local)
            for ev in data["abs_evals"]:
                abs_list.append(float(ev))
                mult_list.append(d_irrep)
    lam = np.array(abs_list, dtype=np.float64)             # (local)
    mult = np.array(mult_list, dtype=np.float64)           # (local)
    wZ = np.exp(-(lam / Lambda_Z_val) ** 2)                # (local)
    sum_d_wZ = float(np.sum(mult * wZ))                    # (local)
    sum_d_wZ_lam = float(np.sum(mult * wZ * lam))          # (local)
    lam_max = float(lam.max())                             # (local)
    mean_Z = sum_d_wZ_lam / sum_d_wZ                       # (local)
    rho = mean_Z / lam_max - 1.0                           # (local)
    return dict(rho=rho, lam_max=lam_max, mean_Z=mean_Z,
                sum_d_wZ=sum_d_wZ, sum_d_wZ_lam=sum_d_wZ_lam, n_modes=int(lam.size))


# ---------------------------------------------------------------------------
# Section 6 — print_verdict_payload (agent calls emit_verdict with this)
# ---------------------------------------------------------------------------

def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_v="", magnitude_v="", regime_v="", extra_rows=None):
    payload = {
        "session": SESSION_NUM,
        "track": "investigation",
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
    print(f"=== {GATE_ID} :: branch-(iv) w_0 spread_CAC over {{12,13,14,15,16}} (DR3 readiness) ===")
    print(f"[const] w0_FW={w0_FW}  tau_fold={tau_fold}  Lambda_Z={LAMBDA_Z}  "
          f"Gamma_effacement={Gamma_effacement}  N_cells={N_cells}")
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    audit_sha, content_sha = compute_dual_sha(THIS_FILE, P_CANONICAL, pins)
    print(f"  closure_hash:   {closure[:16]}...")
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    # --- Plan-text-drift detection on canonical_constants.py (substrate-first-canonical-sourcing.md §(ii.B)) ---
    canonical_runtime_sha = pins.get("computations/_shared/canonical_constants.py", "")  # (local)
    canonical_drift = (canonical_runtime_sha != CANONICAL_PLANFREEZE_SHA)                # (local)
    if canonical_drift:
        print(f"[drift] canonical_constants.py SHA drifted from plan-freeze baseline "
              f"{CANONICAL_PLANFREEZE_SHA[:16]}... -> runtime {canonical_runtime_sha[:16]}... "
              f"(expected per §(ii.B): W1-1 update_constant prereq + in-session promotions; w0_FW "
              f"value {w0_FW} unchanged — the runtime SHA is pinned into the closure hash).")
    # SHA-pin verification on the IMMUTABLE data caches (these MUST match the plan pins)
    s84_runtime = pins.get("computations/session-84/s84_spectrum_cache_L12_tau019.npz", "")  # (local)
    s106_runtime = pins.get("computations/session-106/s106_w1_highl_cache_l1416.npz", "")     # (local)
    s84_sha_ok = (s84_runtime == S84_PINNED_SHA)        # (local)
    s106_sha_ok = (s106_runtime == S106_PINNED_SHA)     # (local)
    print(f"[sha-pin] s84 cache SHA matches plan pin: {s84_sha_ok}; "
          f"s106 cache SHA matches plan pin: {s106_sha_ok}")

    if not (s84_sha_ok and s106_sha_ok):
        # Honest mechanical closure per mechanical-closure-discipline.md: the data caches drifted,
        # the truncation set cannot be trusted -> PRE-REG-INC (NOT a forced PASS).
        value = (f"PRE-REG-INC_cache_SHA_drift_s84_ok={s84_sha_ok}_s106_ok={s106_sha_ok}; "
                 f"data_cache_pin_mismatch; no_consumption; operational_fallback=S105_{{12,13,14}}_reproduce")
        np.savez_compressed(
            INV_DIR / "inv13_w1_branch_iv_w0_l1516_dr3.npz",
            verdict="PRE-REG-INC", phase="CACHE_SHA_DRIFT",
            s84_sha_ok=s84_sha_ok, s106_sha_ok=s106_sha_ok,
            s84_runtime_sha=s84_runtime, s106_runtime_sha=s106_runtime,
            audit_sha256=audit_sha, content_sha256=content_sha, closure_hash=closure,
        )
        _make_plot_fallback({}, "CACHE_SHA_DRIFT", float("nan"))
        print_verdict_payload("PRE-REG-INC", value, audit_sha, content_sha)
        return

    # --- Load s84 L<=12 master cache (the moment-sentinel anchor) ---
    z84 = np.load(P_CACHE_S84, allow_pickle=True)
    sector_evals_s84 = z84["sector_evals"].item()          # (local) {(p,q): {dim,level,abs_evals}}
    z84.close()
    cache_max_level_s84 = max(d["level"] for d in sector_evals_s84.values())  # (local)
    print(f"[cache] s84 master: {len(sector_evals_s84)} sectors, max_level={cache_max_level_s84}")

    # =====================================================================
    # MOMENT-SENTINEL (GATING, MANDATORY): reproduce rho_B(8,10,12) bit-exact on the s84 cache
    # BEFORE consuming any S106 high-L sector. (Zubarev-evaluator self-consistency.)
    # =====================================================================
    print("  --- MOMENT-SENTINEL: rho_B(8,10,12) on s84 cache vs EXPECT_RHO (runs BEFORE consumption) ---")
    rho_recompute = {}                                     # (local)
    repro_diffs = {}                                       # (local)
    for L in (8, 10, 12):
        rr = rho_zubarev_from_sectors(sector_evals_s84, L, LAMBDA_Z)
        rho_recompute[L] = rr["rho"]
        repro_diffs[L] = abs(rr["rho"] - EXPECT_RHO[L])
        print(f"  rho_B({L}) recompute = {rr['rho']:.15f}  (expect {EXPECT_RHO[L]:.15f}, "
              f"diff {repro_diffs[L]:.2e}, n_modes={rr['n_modes']})")
    moment_sentinel_max = max(repro_diffs.values())        # (local)
    moment_sentinel_ok = moment_sentinel_max <= SENTINEL_TOL  # (local)
    print(f"[moment-sentinel] s84 rho-recompute max_diff={moment_sentinel_max:.2e}  "
          f"ok(<= {SENTINEL_TOL:.0e})={moment_sentinel_ok}")

    if not moment_sentinel_ok:
        # GATING: the Zubarev evaluator does not reproduce the s84 cache anchors -> do NOT consume.
        value = (f"PRE-REG-INC_moment_sentinel_FAIL_max{moment_sentinel_max:.2e}_tol{SENTINEL_TOL:.0e}; "
                 f"Zubarev_evaluator_does_not_reproduce_s84_anchors; no_new_sector_consumption")
        np.savez_compressed(
            INV_DIR / "inv13_w1_branch_iv_w0_l1516_dr3.npz",
            verdict="PRE-REG-INC", phase="MOMENT_SENTINEL_FAIL",
            moment_sentinel_max=moment_sentinel_max, SENTINEL_TOL=SENTINEL_TOL,
            rho_recompute_8=rho_recompute[8], rho_recompute_10=rho_recompute[10],
            rho_recompute_12=rho_recompute[12],
            audit_sha256=audit_sha, content_sha256=content_sha, closure_hash=closure,
        )
        _make_plot_fallback(rho_recompute, "MOMENT_SENTINEL_FAIL", moment_sentinel_max)
        print_verdict_payload("PRE-REG-INC", value, audit_sha, content_sha)
        return

    # --- Load S106 high-L cache (PRE-BUILT eigenvalues; no diagonalization here) ---
    z106 = np.load(P_CACHE_S106, allow_pickle=True)
    sector_L14 = z106["sector_evals_L14"].item()           # (local) levels 0..14 COMPLETE (120 sectors)
    sector_L16 = z106["sector_evals_L16"].item()           # (local) levels 0..15 COMPLETE (136 sectors)
    fb_bounded = z106["fb_bounded_sectors"].item()         # (local) 17 level-16 FB-bounded sectors (no evals)
    s106_sentinel_max = float(z106["sentinel_max"])        # (local) S106 GT-vs-cache spectral sentinel (inherited)
    s106_sentinel_ok = bool(z106["sentinel_ok"])           # (local)
    s106_herm_err_max = float(z106["herm_err_max"])        # (local)
    s106_L14_consistent = bool(z106["L14_truncation_consistent"])  # (local)
    s106_L16_operational = int(z106["L16_operational"])    # (local) == 15
    s106_eta_FB_lower = float(z106["eta_FB_lower"])        # (local) Friedrich-Bar lower-bound factor
    s106_device = str(z106["device"])                      # (local) cuda:0 (build-time)
    z106.close()
    print(f"[s106] L14 dict: {len(sector_L14)} sectors (max_level={max(d['level'] for d in sector_L14.values())}); "
          f"L16 dict: {len(sector_L16)} sectors (max_level={max(d['level'] for d in sector_L16.values())}); "
          f"fb_bounded: {len(fb_bounded)} (level-16)")
    print(f"[s106-inherited] spectral_sentinel_max={s106_sentinel_max:.2e} ok={s106_sentinel_ok}  "
          f"herm_err_max={s106_herm_err_max:.2e}  L14_consistent={s106_L14_consistent}  "
          f"L16_operational={s106_L16_operational}  eta_FB_lower={s106_eta_FB_lower:.4f}  "
          f"build_device={s106_device}")

    # --- Cache-consistency cross-check: L14-dict vs L16-dict bit-exact on shared sectors (S106 build) ---
    shared_max_diff = 0.0                                  # (local)
    n_shared = 0                                           # (local)
    for k in sector_L14:
        if k in sector_L16 and sector_L14[k]["level"] <= 14:
            a = np.sort(np.asarray(sector_L14[k]["abs_evals"], dtype=np.float64))  # (local)
            b = np.sort(np.asarray(sector_L16[k]["abs_evals"], dtype=np.float64))  # (local)
            if len(a) == len(b):
                shared_max_diff = max(shared_max_diff, float(np.max(np.abs(a - b))))
            n_shared += 1
    l14_l16_consistent = shared_max_diff <= SENTINEL_TOL   # (local)
    print(f"[xcheck-cache] L14-vs-L16 shared-sector max|lambda diff| over {n_shared} sectors = "
          f"{shared_max_diff:.2e}  ok={l14_l16_consistent}")

    # --- s84 vs S106-L14 cross-check on the L<=12 overlap (the moment-sentinel anchor must persist) ---
    s84_l16_max_diff = 0.0                                 # (local)
    n_s84_overlap = 0                                      # (local)
    for k in sector_evals_s84:
        if k in sector_L16:
            a = np.sort(np.asarray(sector_evals_s84[k]["abs_evals"], dtype=np.float64))  # (local)
            b = np.sort(np.asarray(sector_L16[k]["abs_evals"], dtype=np.float64))        # (local)
            if len(a) == len(b):
                s84_l16_max_diff = max(s84_l16_max_diff, float(np.max(np.abs(a - b))))
            n_s84_overlap += 1
    s84_l16_consistent = s84_l16_max_diff <= SENTINEL_TOL  # (local)
    print(f"[xcheck-s84] s84-vs-S106L16 shared-sector max|lambda diff| over {n_s84_overlap} sectors = "
          f"{s84_l16_max_diff:.2e}  ok={s84_l16_consistent}")

    # =====================================================================
    # rho_B(L) over {10,12,13,14,15,16}: data-path per L (plan §W1-3 substitution chain)
    #   L in {10,12,13,14}: sector_evals_L14 (levels 0..14 COMPLETE)
    #   L = 15:             sector_evals_L16 truncated at p+q<=15 (level-15 INCLUDED)
    #   L = 16:             sector_evals_L16 truncated at p+q<=16 == <=15 (level-16 FB-bounded, absent)
    # =====================================================================
    rho_B = {}                                             # (local)
    rho_meta = {}                                          # (local)
    for L in (10, 12, 13, 14):
        rr = rho_zubarev_from_sectors(sector_L14, L, LAMBDA_Z)
        rho_B[L] = rr["rho"]
        rho_meta[L] = rr
        print(f"  rho_B({L:2d}) [L14-dict] = {rr['rho']:.15f}  (lam_max={rr['lam_max']:.6f}, "
              f"n_modes={rr['n_modes']})")
    for L in (15, 16):
        rr = rho_zubarev_from_sectors(sector_L16, L, LAMBDA_Z)
        rho_B[L] = rr["rho"]
        rho_meta[L] = rr
        print(f"  rho_B({L:2d}) [L16-dict] = {rr['rho']:.15f}  (lam_max={rr['lam_max']:.6f}, "
              f"n_modes={rr['n_modes']})")

    # L=16 == L=15 EXACTLY by FB-saturation (the 17 level-16 sectors are absent from the cache)
    rho16_eq_15 = abs(rho_B[16] - rho_B[15])               # (local) MUST be 0 (no level-16 modes)
    print(f"[fb-saturation] |rho_B(16) - rho_B(15)| = {rho16_eq_15:.2e} "
          f"(EXACT 0 expected: 17 level-16 sectors FB-bounded, absent from cache; L_operational=15)")

    # --- (4,4)-completeness reconciliation + continuity-of-evaluator cross-check ---
    # The S106 dicts are the COMPLETE per-level union (every (p,q) with p+q<=L present); the s84
    # cache is missing ONE level-8 sector (4,4) (8/9 at level 8) — an S84-era gap S106 rebuilt
    # (dim=125, in S106 build_times). So rho_B(12) on the COMPLETE S106 dict differs from the
    # s84-INCOMPLETE evaluation S105 recorded. This is a SECTOR-SET difference (both correct on
    # their own set), NOT an evaluator failure. Apples-to-apples continuity = rho_B(12) on the SAME
    # incomplete s84 cache the S105 EXPECT_RHO anchors used (= the moment-sentinel rho_recompute[12]).
    rho12_s84_incomplete = rho_recompute[12]               # (local) s84-incomplete set (S105/EXPECT_RHO basis)
    rho12_continuity_s84 = abs(rho12_s84_incomplete - S105_RHO[12])  # (local) MUST be ~0 (same set)
    rho12_completeness_shift = abs(rho_B[12] - rho12_s84_incomplete) # (local) the (4,4)-completeness correction
    print(f"[xcheck-continuity] rho_B(12) s84-incomplete = {rho12_s84_incomplete:.15f} "
          f"vs S105 record {S105_RHO[12]:.6f}: diff {rho12_continuity_s84:.2e} "
          f"(<= {REPRO_TOL:.0e}: {rho12_continuity_s84 <= REPRO_TOL}) [SAME sector set — evaluator continuity]")
    print(f"[xcheck-completeness] rho_B(12) COMPLETE(S106) = {rho_B[12]:.15f}  "
          f"(4,4)-completeness shift vs s84-incomplete = {rho12_completeness_shift:.2e} "
          f"[EXPECTED: S106 rebuilt the missing (4,4) level-8 sector; complete set is the canonical truncation]")
    # diagnostic-only diffs vs the S105 FB-prior sig-fig values (NOT gating; the S106-complete set differs):
    rho13_vs_s105 = abs(rho_B[13] - S105_RHO[13])          # (local) S105 13 FB-prior sig figs (diagnostic)
    rho14_vs_s105 = abs(rho_B[14] - S105_RHO[14])          # (local) S105 14 FB-prior sig figs (diagnostic)
    print(f"[xcheck-S105-diag] rho_B(13) COMPLETE={rho_B[13]:.6f} vs S105-FB-prior {S105_RHO[13]}: "
          f"diff {rho13_vs_s105:.4e} (diagnostic; completeness-shifted)")
    print(f"[xcheck-S105-diag] rho_B(14) COMPLETE={rho_B[14]:.6f} vs S105-FB-prior {S105_RHO[14]}: "
          f"diff {rho14_vs_s105:.4e} (diagnostic; completeness-shifted)")

    # --- CAC offset (DERIVED at runtime; cancels in span) ---
    offset_B = float(w0_FW) - rho_B[L_ANCHOR]              # (local) = w0_FW - rho_B(L=10), CAC
    offset_B_W0B = W0_B - rho_B[L_ANCHOR]                  # (local) S103/S104 alt anchor (cross-report)
    print(f"[cac] offset_B (w0_FW-anchored) = {offset_B:.12f}  "
          f"[w0_FW={w0_FW} - rho_B(10)={rho_B[L_ANCHOR]:.12f}]")
    print(f"[cac] offset_B (W0_B-anchored)  = {offset_B_W0B:.12f}  (S103/S104 cross-report)")
    print(f"[cac] OFFSET_ZUBAREV_S86 cross-report = {OFFSET_ZUBAREV_S86}  "
          f"(diff vs runtime = {abs(offset_B - OFFSET_ZUBAREV_S86):.2e})")

    # --- w0^CAC(L) over the scan window + the L=10 anchor identity ---
    w0_cac = {L: rho_B[L] + offset_B for L in L_SCAN}      # (local) {12,13,14,15,16}
    w0_cac_10 = rho_B[L_ANCHOR] + offset_B                 # (local) must == w0_FW EXACTLY
    cac_anchor_resid = abs(w0_cac_10 - float(w0_FW))       # (local)
    print(f"[cac] w0^CAC(L=10) = {w0_cac_10:.15f}  (== w0_FW={w0_FW}? resid={cac_anchor_resid:.2e})")
    for L in L_SCAN:
        print(f"  w0^CAC({L:2d}) = {w0_cac[L]:.15f}")

    # --- spread_CAC = max-min over {12,...,16}; offset-cancellation cross-check (the substitution-chain core) ---
    w0_vals = np.array([w0_cac[L] for L in L_SCAN])        # (local)
    rho_vals = np.array([rho_B[L] for L in L_SCAN])        # (local)
    spread_CAC = float(w0_vals.max() - w0_vals.min())      # (local)
    spread_rho = float(rho_vals.max() - rho_vals.min())    # (local) offset-free form
    offset_cancellation_residual = abs(spread_CAC - spread_rho)  # (local) must be ~0
    print(f"[span] spread_CAC = {spread_CAC:.12f}   spread_rho(offset-free) = {spread_rho:.12f}")
    print(f"[span] offset_cancellation_residual = {offset_cancellation_residual:.2e}  "
          f"(<= {OFFSET_CANCELLATION_TOL:.0e}: {offset_cancellation_residual <= OFFSET_CANCELLATION_TOL})")

    # argmax / argmin (which L drives the spread)
    L_argmax = L_SCAN[int(np.argmax(rho_vals))]            # (local)
    L_argmin = L_SCAN[int(np.argmin(rho_vals))]            # (local)
    print(f"[span] rho_B argmax at L={L_argmax} ({rho_vals.max():.6f}); "
          f"argmin at L={L_argmin} ({rho_vals.min():.6f})")

    # --- decrement diagnostics (orientation; the rho_B(L) monotone trend) ---
    decrements = {f"{L_SCAN[i]}->{L_SCAN[i+1]}": rho_B[L_SCAN[i+1]] - rho_B[L_SCAN[i]]
                  for i in range(len(L_SCAN) - 1)}         # (local)
    # exclude the trivial 15->16 (=0 by FB-saturation) from the monotone-negative test
    nontrivial_decr = [v for k, v in decrements.items() if k != "15->16"]  # (local)
    decrement_sign_negative = all(v < 0 for v in nontrivial_decr)          # (local)
    print(f"[decr] {', '.join(f'{k}={v:+.8f}' for k,v in decrements.items())}")
    print(f"[decr] nontrivial decrements all-negative (monotone-decreasing rho_B) = {decrement_sign_negative}")

    # --- comparison to the S105 {12,13,14} spread (what the L=15 point added) ---
    spread_12_13_14 = float(max(rho_B[12], rho_B[13], rho_B[14]) - min(rho_B[12], rho_B[13], rho_B[14]))  # (local)
    delta_spread_from_s105 = spread_CAC - spread_12_13_14   # (local) increment from adding L=15(/16)
    print(f"[delta] spread over {{12,13,14}} (recomputed) = {spread_12_13_14:.6f}  "
          f"(S105 record {S105_SPREAD_CAC}); spread over {{12,...,16}} = {spread_CAC:.6f}; "
          f"delta from adding L=15 = {delta_spread_from_s105:+.6f}")

    # --- Verdict band (UNCHANGED W5-2/S105): PASS <= 0.025 | INFO (0.025,0.050] | FAIL > 0.050 ---
    if spread_CAC <= SPREAD_PASS_BAND:
        verdict = "PASS"
    elif spread_CAC <= SPREAD_INFO_BAND:
        verdict = "INFO"
    else:
        verdict = "FAIL"

    # Guards: moment-sentinel (s84 anchors bit-exact), S106 inherited spectral sentinel, cache
    # consistency (L14-L16 + s84-S106 overlap), offset cancellation, CAC anchor, FB-saturation
    # identity, and evaluator continuity (rho_B(12) on the SAME incomplete s84 set vs S105 record
    # — the apples-to-apples test; NOT the (4,4)-completeness shift, which is an EXPECTED sector-set
    # difference, not an evaluator failure). If any genuine guard fails the span cannot be trusted
    # -> force INFO (NOT a clean PASS); a FAIL stays FAIL (a divergence finding is informative).
    guard_ok = (moment_sentinel_ok and s106_sentinel_ok and l14_l16_consistent
                and s84_l16_consistent and (offset_cancellation_residual <= OFFSET_CANCELLATION_TOL)
                and (cac_anchor_resid <= CAC_ANCHOR_RESID_TOL) and (rho16_eq_15 <= REPRO_TOL)
                and (rho12_continuity_s84 <= REPRO_TOL))   # (local) same-sector-set continuity
    if (not guard_ok) and verdict == "PASS":
        verdict = "INFO"
        print("[WARN] a sentinel/consistency guard failed -> PASS downgraded to INFO")

    print(f"[VERDICT] spread_CAC={spread_CAC:.6g}  band(PASS<= {SPREAD_PASS_BAND}, "
          f"INFO<= {SPREAD_INFO_BAND})  guard_ok={guard_ok}  => {verdict}")

    # --- persist npz ---
    np.savez_compressed(
        INV_DIR / "inv13_w1_branch_iv_w0_l1516_dr3.npz",
        verdict=verdict, phase="L1516_COMPLETE",
        L_SCAN=np.array(L_SCAN, dtype=np.int64), L_anchor=L_ANCHOR,
        L_max_plan=np.array(L_MAX_PLAN, dtype=np.int64), L_max_operational=L_MAX_OPERATIONAL,
        # rho_B at every truncation evaluated:
        rho_B_10=rho_B[10], rho_B_12=rho_B[12], rho_B_13=rho_B[13],
        rho_B_14=rho_B[14], rho_B_15=rho_B[15], rho_B_16=rho_B[16],
        rho_B_window=np.array([rho_B[L] for L in L_SCAN]),
        lam_max_window=np.array([rho_meta[L]["lam_max"] for L in L_SCAN]),
        n_modes_window=np.array([rho_meta[L]["n_modes"] for L in L_SCAN]),
        # CAC:
        w0_FW=float(w0_FW), W0_B=W0_B,
        offset_B=offset_B, offset_B_W0B=offset_B_W0B, OFFSET_ZUBAREV_S86=OFFSET_ZUBAREV_S86,
        w0_cac=np.array([w0_cac[L] for L in L_SCAN]), w0_cac_10=w0_cac_10,
        cac_anchor_resid=cac_anchor_resid,
        # spread + offset cancellation:
        spread_CAC=spread_CAC, spread_rho=spread_rho,
        offset_cancellation_residual=offset_cancellation_residual,
        spread_12_13_14=spread_12_13_14, delta_spread_from_s105=delta_spread_from_s105,
        S105_SPREAD_CAC=S105_SPREAD_CAC,
        L_argmax=L_argmax, L_argmin=L_argmin,
        SPREAD_PASS_BAND=SPREAD_PASS_BAND, SPREAD_INFO_BAND=SPREAD_INFO_BAND,
        # FB-saturation:
        rho16_eq_15=rho16_eq_15, eta_FB_lower=s106_eta_FB_lower, n_fb_bounded=len(fb_bounded),
        # decrements:
        decrements_json=json.dumps({k: float(v) for k, v in decrements.items()}),
        decrement_sign_negative=decrement_sign_negative,
        # moment-sentinel + inherited S106 sentinel:
        moment_sentinel_max=moment_sentinel_max, moment_sentinel_ok=moment_sentinel_ok,
        SENTINEL_TOL=SENTINEL_TOL,
        rho_recompute_8=rho_recompute[8], rho_recompute_10=rho_recompute[10],
        rho_recompute_12=rho_recompute[12],
        s106_sentinel_max=s106_sentinel_max, s106_sentinel_ok=s106_sentinel_ok,
        s106_herm_err_max=s106_herm_err_max, s106_device=s106_device,
        # cache consistency:
        l14_l16_shared_max_diff=shared_max_diff, l14_l16_consistent=l14_l16_consistent,
        s84_l16_max_diff=s84_l16_max_diff, s84_l16_consistent=s84_l16_consistent,
        # continuity vs S105:
        rho12_s84_incomplete=rho12_s84_incomplete, rho12_continuity_s84=rho12_continuity_s84,
        rho12_completeness_shift=rho12_completeness_shift,
        rho13_vs_s105=rho13_vs_s105, rho14_vs_s105=rho14_vs_s105,
        # SHA-pin drift record (substrate-first-canonical-sourcing.md §(ii.B)):
        canonical_drift=canonical_drift, canonical_runtime_sha=canonical_runtime_sha,
        canonical_planfreeze_sha=CANONICAL_PLANFREEZE_SHA,
        s84_sha_ok=s84_sha_ok, s106_sha_ok=s106_sha_ok,
        guard_ok=guard_ok,
        Lambda_Z=LAMBDA_Z, jensen_s=JENSEN_S, Gamma_effacement=float(Gamma_effacement),
        N_cells=int(N_cells),
        audit_sha256=audit_sha, content_sha256=content_sha, closure_hash=closure,
    )

    _make_plot_direct(rho_B, w0_cac, spread_CAC, verdict, L_SCAN, spread_12_13_14)

    # --- [VERIFY] gate: no 3-tuple required (plan output_artifacts schema_v2_3tuple_required: false).
    #     But the offset-cancellation identity is the structural cross-check; report it in value. ---
    value = (f"spread_CAC={spread_CAC:.6g} "
             f"rho_B(12)={rho_B[12]:.6f} rho_B(13)={rho_B[13]:.6f} rho_B(14)={rho_B[14]:.6f} "
             f"rho_B(15)={rho_B[15]:.6f} rho_B(16)={rho_B[16]:.6f} "
             f"w0CAC(15)={w0_cac[15]:.6f} w0CAC(16)={w0_cac[16]:.6f} offset_B={offset_B:.6f} "
             f"spread{{12,13,14}}={spread_12_13_14:.6f}(S105={S105_SPREAD_CAC}) "
             f"L_max_plan={{14,16}}_operational=15 FB_saturated rho16=rho15 "
             f"offset_cancel_resid={offset_cancellation_residual:.2e} guard_ok={guard_ok} "
             f"band_PASS<={SPREAD_PASS_BAND}_INFO<={SPREAD_INFO_BAND}")
    extra_rows = [
        (f"# regulator_pin=a_2^{{Mellin}} poleconv-A-double (pole_in_s=3, curvature_grade_n=2); "
         f"branch-iv-Zubarev-late-time-moment; data=S106-highL-cache(prebuilt-eigvals,no-diag-here); "
         f"moment_sentinel(s84-rho-recompute)={moment_sentinel_max:.2e}<= {SENTINEL_TOL:.0e}; "
         f"s106_spectral_sentinel(inherited)={s106_sentinel_max:.2e}; "
         f"L14_l16_consistent={l14_l16_consistent}@{shared_max_diff:.1e}; "
         f"offset_cancellation_residual={offset_cancellation_residual:.2e}; "
         f"cac_anchor_resid={cac_anchor_resid:.2e}"),
        (f"# L_max_plan={{14,16}} L_max_operational=15 (L16 Friedrich-Bar-saturated: 17 level-16 "
         f"sectors FB-bounded eta_FB_lower={s106_eta_FB_lower:.4f}, |rho_B(16)-rho_B(15)|={rho16_eq_15:.2e}); "
         f"GPU: per-block eigvals prebuilt at S106 on {s106_device} (consumption gate, no re-diag); "
         f"canonical_drift={canonical_drift} (w0_FW={w0_FW} unchanged, §(ii.B) plan-text-drift); "
         f"truncation-stability axis ONLY (NOT branch-iv derivation-admissibility, S101-W0-BRANCH-IV-EVALUATOR)"),
    ]
    print_verdict_payload(verdict, value, audit_sha, content_sha, extra_rows=extra_rows)


def _make_plot_direct(rho_B, w0_cac, spread_CAC, verdict, L_scan, spread_12_13_14):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
    Ls = list(L_scan)
    # Panel 1: rho_B(L) trajectory, with the new L=15/16 points highlighted
    ax1.plot([12, 13, 14], [rho_B[L] for L in (12, 13, 14)], "o-", color="C0",
             label=r"$\rho_B(L)$ S105 window $\{12,13,14\}$")
    ax1.plot([14, 15], [rho_B[14], rho_B[15]], "--", color="C1", lw=1)
    ax1.plot([15], [rho_B[15]], "D", color="C1", ms=9, label=r"$\rho_B(15)$ NEW (L16-dict $\leq$15)")
    ax1.plot([16], [rho_B[16]], "s", color="C3", ms=8, mfc="none",
             label=r"$\rho_B(16)=\rho_B(15)$ (FB-saturated)")
    ax1.set_xlabel("truncation L (p+q)")
    ax1.set_ylabel(r"$\rho_B(L)$  (Zubarev branch-IV moment)")
    ax1.set_title(r"branch-(iv) $\rho_B(L)$ over $\{12,\dots,16\}$"
                  "\n(L=16 FB-saturated at operational L=15)")
    ax1.set_xticks(Ls)
    ax1.grid(alpha=0.3)
    ax1.legend(fontsize=8)
    # Panel 2: w0^CAC(L) with spread band
    ax2.plot(Ls, [w0_cac[L] for L in Ls], "s-", color="C2",
             label=r"$w_0^{\rm CAC}(L)=\rho_B(L)+{\rm offset}_B$")
    ax2.axhline(float(w0_FW), color="k", ls=":", lw=1, label=fr"$w_0^{{FW}}={w0_FW}$")
    band_color = {"PASS": "C2", "INFO": "C1", "FAIL": "C3"}.get(verdict, "0.5")  # (local)
    ax2.set_xlabel("truncation L (p+q)")
    ax2.set_ylabel(r"$w_0^{\rm CAC}(L)$")
    ax2.set_title(fr"$w_0^{{\rm CAC}}$: spread$_{{\{{12..16\}}}}={spread_CAC:.5f}$  "
                  fr"$\Rightarrow$ {verdict}"
                  "\n(PASS$\\leq$0.025 | INFO(0.025,0.050] | FAIL$>$0.050; "
                  fr"$\{{12,13,14\}}$ was {spread_12_13_14:.5f})")
    ax2.set_xticks(Ls)
    ax2.grid(alpha=0.3)
    for spine in ax2.spines.values():
        spine.set_edgecolor(band_color)
        spine.set_linewidth(2)
    ax2.legend(fontsize=8)
    fig.suptitle(f"{GATE_ID} — branch-IV $w_0$ DR3-readiness truncation stability (L=15/16)",
                 fontsize=11)
    fig.tight_layout()
    fig.savefig(INV_DIR / "inv13_w1_branch_iv_w0_l1516_dr3.png", dpi=120)
    plt.close(fig)


def _make_plot_fallback(rho_recompute, phase_status, sentinel_max):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(8, 5))
    if rho_recompute:
        Ls = sorted(rho_recompute.keys())
        ax.plot(Ls, [rho_recompute[L] for L in Ls], "o-", color="C0",
                label=r"$\rho_B(L)$ (s84 cache, L$\leq$12)")
        ax.set_xlabel("truncation L (p+q)")
        ax.set_ylabel(r"$\rho_B(L)$")
        ax.legend(fontsize=9)
    ax.set_title(f"{GATE_ID} — PRE-REG-INC ({phase_status})\n"
                 f"sentinel/SHA guard max={sentinel_max:.2e} -> deferred")
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(INV_DIR / "inv13_w1_branch_iv_w0_l1516_dr3.png", dpi=120)
    plt.close(fig)


if __name__ == "__main__":
    main()
