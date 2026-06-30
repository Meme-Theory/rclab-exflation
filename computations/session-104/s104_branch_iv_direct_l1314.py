#!/usr/bin/env python
"""
S104-BRANCH-IV-DIRECT-L1314 — PHASE 2 (moment + CAC span + verdict).

[VERIFY] truncation stability of the branch-IV dark-energy moment w0^CAC over L in {12,13,14}
using DIRECT rho_B(13) / rho_B(14) spectra (NOT the S103 Friedrich-Bar envelope BOUND).

GEOMETRIC. Substrate-first arrow: D_K eigenvalues at tau_fold -> Zubarev branch-IV a_4-channel
spectral moment rho_B(L) -> CAC-anchored late-time equation-of-state w0^CAC(L) -> truncation-
stability span. The CAC offset is a pure additive translation anchoring w0^CAC(L=10) = w0_FW
EXACTLY; the truncation SPREAD is offset-INDEPENDENT (offset cancels) and measures whether the
substrate's own eigenvalue spectrum has converged enough at L=12 that adding the L=13,14 Peter-
Weyl shells does not move the dark-energy moment. GR's dark energy is the consequence, not the
premise.

Moment (S85 W0-7 verbatim, reproduced bit-for-bit against the s84 cache for L<=12):
    rho_B(L) := rho_Zubarev(L) = <|lambda|>_Z(L) / lambda_max(L) - 1
        <|lambda|>_Z = (sum_j d_j w_Z_j |lam_j|) / (sum_j d_j w_Z_j),  w_Z = exp(-|lam|^2/Lambda_Z^2)
        Lambda_Z = 1.0 (M_KK units), summed over all sectors with level <= L.

CAC (regulator-convention-lockdown.md; RDC FORBIDDEN):
    offset_B   := w0_FW - rho_B(L=10)        [DERIVED at runtime; w0_FW = -0.918 canonical; ZERO free norm]
    w0^CAC(L)  := rho_B(L) + offset_B
    spread_CAC := max_{L in {12,13,14}} w0^CAC(L) - min_{...} w0^CAC(L)
                = max_L rho_B(L) - min_L rho_B(L)         [offset cancels -> span is offset-FREE]

Verdict band (UNCHANGED W5-2): PASS <= 0.025 | INFO (0.025, 0.050] | FAIL > 0.050.

Phase-1 DIRECT sectors come from computations/session-104/s104_sym_p_chain_cache_L1314.py
(offline Sym^13/14 builder + GPU eigvalsh). FEASIBILITY FALLBACK (pre-registered,
mechanical-closure-discipline.md): if the Phase-1 cache lacks a COMPLETE level-13 AND level-14
sector set, close honestly as PRE-REG-INC (deferred to S105), NOT a FAIL; the S103 FB-envelope
INFO stands as the best available bound.

Output: s104_branch_iv_direct_l1314.{npz,png} + verdict via emit_verdict MCP tool.
"""
from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# Section 1 — Identity + paths
# ---------------------------------------------------------------------------
SESSION = "S104"
GATE_ID = "S104-BRANCH-IV-DIRECT-L1314"
SCHEME = "zeta"
CONVENTION = "CAC-branch-iv-anchored-L10-DERIVED-OFFSET"
L_MAX = "{12,13,14}"

THIS_FILE = Path(__file__).resolve()
PROJECT_ROOT = THIS_FILE.parents[2]                  # .../computations/session-104/<this> -> root
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
SESSION_DIR = PROJECT_ROOT / "computations" / "session-104"

sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import (  # noqa: E402
    w0_FW,
    Gamma_effacement,
    N_cells,
    tau_fold,
)

# ---------------------------------------------------------------------------
# Section 2 — Pre-registered constants (plan §W1-3)
# ---------------------------------------------------------------------------
W0_B = -0.842454                          # (local) branch-iv canonical (S85 W10-2 branch-(iv); S103 anchor, cross-report)
REPRO_TOL = 1e-12                         # (local) rho-recompute reproduction rel_tol (plan tolerance pin; S103 hit 1.1e-16)
# UNCHANGED W5-2 band (plan §W1-3 strict_PASS_boundary):
SPREAD_PASS_BAND = 0.025                  # (local) PASS <= 0.025
SPREAD_INFO_BAND = 0.050                  # (local) INFO (0.025, 0.050]; FAIL > 0.050
L_SCAN = (12, 13, 14)                     # (local) deep-truncation CAC spread window (regulator axis, DR3-class)
L_ANCHOR = 10                             # (local) canonical CAC anchor truncation (rho_B(L=10) -> w0_FW)
LAMBDA_Z = 1.0                            # (local) Zubarev kernel width (S85 W0-7 PRDR pin), M_KK units
PUBLICATION_PRECISION = 6                 # (local) spread + w0^CAC published to 6 sig figs

# FB diagnostic prior (S103 sanity floor — NOT gating; cross-report only):
FB_PRIOR_RHO_13 = -0.646653               # (local) S103 FB-midpoint diagnostic prior rho_B(13)
FB_PRIOR_RHO_14 = -0.657020               # (local) S103 FB-midpoint diagnostic prior rho_B(14)
OFFSET_ZUBAREV_S86 = -0.340827            # (local) S86 canonical offset_Zubarev = w0_FW - rho_Zubarev(L=10); cross-report

JENSEN_S = float(tau_fold)                # (local) Jensen deformation parameter s = tau_fold = 0.190 (cache is tau019)

# ---------------------------------------------------------------------------
# Section 3 — Input files (plan-text drift corrected at runtime per substrate-first §(ii.B))
# ---------------------------------------------------------------------------
P_CANONICAL = SHARED_DIR / "canonical_constants.py"
P_CACHE = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
P_DIRAC = SHARED_DIR / "dirac_spectrum.py"
P_S103_NPZ = PROJECT_ROOT / "computations" / "session-103" / "s103_branch_iv_deep_truncation.npz"
P_PHASE1 = SESSION_DIR / "s104_sym_p_chain_cache_L1314.npz"   # Phase-1 DIRECT new sectors

# The audit-SHA pin set per plan audit_discriminators (script, canonical, pinmap implicit,
# s84 cache, dirac_spectrum.py, s103 deep-truncation npz). Phase-1 cache pinned too (the
# DIRECT-spectra source); included for provenance.
INPUT_FILES = [P_CANONICAL, P_CACHE, P_DIRAC, P_S103_NPZ, P_PHASE1]

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
# Section 5 — rho_Zubarev(L) kernel (S85 W0-7 verbatim formula; identical to s103 evaluator)
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
        "session": 104,
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
    print(f"=== {GATE_ID} :: Phase-2 moment + CAC span + verdict ===")
    print(f"[const] w0_FW={w0_FW}  tau_fold={tau_fold}  Lambda_Z={LAMBDA_Z}  "
          f"Gamma_effacement={Gamma_effacement}  N_cells={N_cells}")
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    audit_sha, content_sha = compute_dual_sha(THIS_FILE, P_CANONICAL, pins)
    print(f"  closure_hash:   {closure[:16]}...")
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    # --- Load s84 L<=12 master cache ---
    cache = np.load(P_CACHE, allow_pickle=True)
    sector_evals = cache["sector_evals"].item()            # (local) {(p,q): {dim,level,abs_evals}}
    cache_max_level = max(d["level"] for d in sector_evals.values())  # (local)
    n_cache_sectors = len(sector_evals)                    # (local)
    print(f"[cache] s84 master: {n_cache_sectors} sectors, max_level={cache_max_level}")

    # --- Cross-check 1: reproduce rho_B(L=8,10,12) bit-exact (sentinel; the consumed S85 evaluator) ---
    rho_recompute = {}                                     # (local)
    EXPECT = {8: -0.5044659979116969, 10: -0.5771725805120294, 12: -0.634885419265151}  # (local) S103 record
    repro_diffs = {}                                       # (local)
    for L in (8, 10, 12):
        rr = rho_zubarev_from_sectors(sector_evals, L, LAMBDA_Z)
        rho_recompute[L] = rr["rho"]
        repro_diffs[L] = abs(rr["rho"] - EXPECT[L])
        print(f"  rho_B({L}) recompute = {rr['rho']:.15f}  (expect {EXPECT[L]:.15f}, "
              f"diff {repro_diffs[L]:.2e}, n_modes={rr['n_modes']})")
    rho_recompute_max_diff = max(repro_diffs.values())     # (local)
    rho_recompute_ok = rho_recompute_max_diff <= REPRO_TOL  # (local)
    print(f"[xcheck1] rho-recompute max_diff={rho_recompute_max_diff:.2e}  "
          f"ok(<= {REPRO_TOL:.0e})={rho_recompute_ok}")

    # --- Load Phase-1 DIRECT new sectors; check completeness for levels 13 + 14 ---
    have_13 = have_14 = False                               # (local)
    new_sectors = {}                                        # (local)
    phase1_status = "ABSENT"                                # (local)
    phase1_timing = {}                                      # (local)
    if P_PHASE1.exists():
        z1 = np.load(P_PHASE1, allow_pickle=True)
        new_sectors = z1["new_sectors"].item()
        phase1_status = str(z1["status"]) if "status" in z1.files else "UNKNOWN"
        if "timing_json" in z1.files:
            phase1_timing = json.loads(str(z1["timing_json"]))
        have_13 = all((p, 13 - p) in new_sectors for p in range(14))
        have_14 = all((p, 14 - p) in new_sectors for p in range(15))
        print(f"[phase1] cache status={phase1_status}  n_new={len(new_sectors)}  "
              f"have_13={have_13}  have_14={have_14}")
        print(f"[phase1] sectors: {sorted(new_sectors.keys())}")
    else:
        print(f"[phase1] cache ABSENT at {P_PHASE1}")

    feasible = bool(have_13 and have_14)                   # (local) DIRECT verdict requires BOTH levels complete

    # --- FEASIBILITY FALLBACK: PRE-REG-INC if Phase-1 incomplete ---
    if not feasible:
        miss13 = [(p, 13 - p) for p in range(14) if (p, 13 - p) not in new_sectors]  # (local)
        miss14 = [(p, 14 - p) for p in range(15) if (p, 14 - p) not in new_sectors]  # (local)
        print(f"[fallback] DIRECT spectra INCOMPLETE — Phase-1 wall not cleared.")
        print(f"           missing level-13: {miss13}")
        print(f"           missing level-14: {miss14}")
        value = (f"PRE-REG-INC_blocked_by_irrep_construction_wall_Sym13_Sym14; "
                 f"phase1_status={phase1_status}; have_13={have_13}; have_14={have_14}; "
                 f"n_new={len(new_sectors)}; deferred_to_S105; "
                 f"S103_FB_envelope_INFO_508c7cf3_stands_as_best_bound")
        # Persist the partial state + npz so the next session resumes.
        np.savez_compressed(
            SESSION_DIR / "s104_branch_iv_direct_l1314.npz",
            verdict="PRE-REG-INC",
            feasible=False,
            phase1_status=phase1_status,
            have_13=have_13, have_14=have_14,
            n_new_sectors=len(new_sectors),
            new_sectors_present=np.array(sorted(new_sectors.keys()), dtype=object),
            missing_13=np.array(miss13, dtype=object),
            missing_14=np.array(miss14, dtype=object),
            rho_recompute_8=rho_recompute[8], rho_recompute_10=rho_recompute[10],
            rho_recompute_12=rho_recompute[12],
            rho_recompute_max_diff=rho_recompute_max_diff, rho_recompute_ok=rho_recompute_ok,
            w0_FW=float(w0_FW), W0_B=W0_B, OFFSET_ZUBAREV_S86=OFFSET_ZUBAREV_S86,
            FB_PRIOR_RHO_13=FB_PRIOR_RHO_13, FB_PRIOR_RHO_14=FB_PRIOR_RHO_14,
            L_SCAN=np.array(L_SCAN, dtype=np.int64), Lambda_Z=LAMBDA_Z, jensen_s=JENSEN_S,
            SPREAD_PASS_BAND=SPREAD_PASS_BAND, SPREAD_INFO_BAND=SPREAD_INFO_BAND,
            audit_sha256=audit_sha, content_sha256=content_sha, closure_hash=closure,
            phase1_timing_json=json.dumps(phase1_timing),
        )
        _make_plot_fallback(rho_recompute, phase1_status, len(new_sectors), have_13, have_14)
        print_verdict_payload("PRE-REG-INC", value, audit_sha, content_sha)
        return

    # --- DIRECT branch: merge new sectors, compute rho_B(13), rho_B(14) DIRECT ---
    merged = dict(sector_evals)                            # (local)
    merged.update(new_sectors)
    merged_max_level = max(d["level"] for d in merged.values())  # (local)
    print(f"[direct] merged cache: {len(merged)} sectors, max_level={merged_max_level}")

    rho_B = {}                                             # (local)
    rho_meta = {}                                          # (local)
    for L in (10, 12, 13, 14):                             # 10 needed for offset; 12,13,14 for span
        rr = rho_zubarev_from_sectors(merged, L, LAMBDA_Z)
        rho_B[L] = rr["rho"]
        rho_meta[L] = rr
        print(f"  rho_B({L}) DIRECT = {rr['rho']:.15f}  (lam_max={rr['lam_max']:.6f}, "
              f"n_modes={rr['n_modes']})")

    # rho_B(12) must equal the cache reproduction (L=12 fully in s84 cache) — consistency floor
    rho12_consistency = abs(rho_B[12] - rho_recompute[12])  # (local)
    print(f"[xcheck2] rho_B(12) DIRECT vs cache-recompute diff = {rho12_consistency:.2e} "
          f"(<= {REPRO_TOL:.0e}: {rho12_consistency <= REPRO_TOL})")

    # --- CAC offset (DERIVED at runtime; offset cancels in span) ---
    offset_B = float(w0_FW) - rho_B[L_ANCHOR]              # (local) = w0_FW - rho_B(L=10), CAC
    offset_B_W0B = W0_B - rho_B[L_ANCHOR]                  # (local) S103 alt anchor (cross-report)
    print(f"[cac] offset_B (w0_FW-anchored) = {offset_B:.12f}  "
          f"[w0_FW={w0_FW} - rho_B(10)={rho_B[L_ANCHOR]:.12f}]")
    print(f"[cac] offset_B (W0_B-anchored)  = {offset_B_W0B:.12f}  (S103 cross-report; = -0.265281)")
    print(f"[cac] offset_Zubarev_S86 xref   = {OFFSET_ZUBAREV_S86:.6f}")

    w0_cac = {L: rho_B[L] + offset_B for L in L_SCAN}      # (local) {12,13,14}
    # CAC anchor identity check at L=10:
    w0_cac_10 = rho_B[L_ANCHOR] + offset_B                 # (local) must == w0_FW EXACTLY
    cac_anchor_resid = abs(w0_cac_10 - float(w0_FW))       # (local)
    print(f"[cac] w0^CAC(L=10) = {w0_cac_10:.15f}  (== w0_FW={w0_FW}? resid={cac_anchor_resid:.2e})")
    for L in L_SCAN:
        print(f"  w0^CAC({L}) = {w0_cac[L]:.15f}")

    # --- spread_CAC = max-min over {12,13,14}; offset-cancellation cross-check ---
    w0_vals = np.array([w0_cac[L] for L in L_SCAN])        # (local)
    rho_vals = np.array([rho_B[L] for L in L_SCAN])        # (local)
    spread_CAC = float(w0_vals.max() - w0_vals.min())      # (local)
    spread_rho = float(rho_vals.max() - rho_vals.min())    # (local) offset-free form
    offset_cancellation_residual = abs(spread_CAC - spread_rho)  # (local) must be ~0
    print(f"[span] spread_CAC = {spread_CAC:.12f}   spread_rho(offset-free) = {spread_rho:.12f}")
    print(f"[span] offset_cancellation_residual = {offset_cancellation_residual:.2e}")

    # --- decrement diagnostics (orientation; matches S103 FB-prior direction) ---
    decrement_12_13 = rho_B[13] - rho_B[12]                # (local)
    decrement_13_14 = rho_B[14] - rho_B[13]                # (local)
    decrement_sign_negative = (decrement_12_13 < 0) and (decrement_13_14 < 0)   # (local)
    decelerating = abs(decrement_13_14) < abs(decrement_12_13)                  # (local)
    print(f"[decr] d(12->13)={decrement_12_13:.8f}  d(13->14)={decrement_13_14:.8f}  "
          f"sign_neg={decrement_sign_negative}  decelerating={decelerating}")

    # --- FB-prior sanity cross-report (NOT gating) ---
    fb13_diff = abs(rho_B[13] - FB_PRIOR_RHO_13)           # (local)
    fb14_diff = abs(rho_B[14] - FB_PRIOR_RHO_14)           # (local)
    print(f"[fb-prior] rho_B(13) DIRECT={rho_B[13]:.6f} vs FB-prior {FB_PRIOR_RHO_13} (diff {fb13_diff:.4f})")
    print(f"[fb-prior] rho_B(14) DIRECT={rho_B[14]:.6f} vs FB-prior {FB_PRIOR_RHO_14} (diff {fb14_diff:.4f})")

    # --- Verdict band (UNCHANGED W5-2): PASS <= 0.025 | INFO (0.025,0.050] | FAIL > 0.050 ---
    if spread_CAC <= SPREAD_PASS_BAND:
        verdict = "PASS"
    elif spread_CAC <= SPREAD_INFO_BAND:
        verdict = "INFO"
    else:
        verdict = "FAIL"
    # Sentinel gate: if rho recompute failed, the evaluator drifted -> cannot trust the span.
    if not rho_recompute_ok:
        verdict = "INFO"
        print("[WARN] rho-recompute sentinel FAILED -> evaluator drift; verdict forced INFO")

    print(f"[VERDICT] spread_CAC={spread_CAC:.6g}  band(PASS<= {SPREAD_PASS_BAND}, "
          f"INFO<= {SPREAD_INFO_BAND})  => {verdict}")

    # --- persist npz ---
    np.savez_compressed(
        SESSION_DIR / "s104_branch_iv_direct_l1314.npz",
        verdict=verdict, feasible=True, phase1_status=phase1_status,
        L_SCAN=np.array(L_SCAN, dtype=np.int64), L_anchor=L_ANCHOR,
        rho_B_10=rho_B[10], rho_B_12=rho_B[12], rho_B_13=rho_B[13], rho_B_14=rho_B[14],
        rho_B_window=np.array([rho_B[12], rho_B[13], rho_B[14]]),
        lam_max_12=rho_meta[12]["lam_max"], lam_max_13=rho_meta[13]["lam_max"],
        lam_max_14=rho_meta[14]["lam_max"],
        n_modes_12=rho_meta[12]["n_modes"], n_modes_13=rho_meta[13]["n_modes"],
        n_modes_14=rho_meta[14]["n_modes"],
        w0_FW=float(w0_FW), W0_B=W0_B,
        offset_B=offset_B, offset_B_W0B=offset_B_W0B, OFFSET_ZUBAREV_S86=OFFSET_ZUBAREV_S86,
        w0_cac=np.array([w0_cac[L] for L in L_SCAN]), w0_cac_10=w0_cac_10,
        cac_anchor_resid=cac_anchor_resid,
        spread_CAC=spread_CAC, spread_rho=spread_rho,
        offset_cancellation_residual=offset_cancellation_residual,
        SPREAD_PASS_BAND=SPREAD_PASS_BAND, SPREAD_INFO_BAND=SPREAD_INFO_BAND,
        decrement_12_13=decrement_12_13, decrement_13_14=decrement_13_14,
        decrement_sign_negative=decrement_sign_negative, decelerating=decelerating,
        FB_PRIOR_RHO_13=FB_PRIOR_RHO_13, FB_PRIOR_RHO_14=FB_PRIOR_RHO_14,
        fb13_diff=fb13_diff, fb14_diff=fb14_diff,
        rho_recompute_8=rho_recompute[8], rho_recompute_10=rho_recompute[10],
        rho_recompute_12=rho_recompute[12], rho_recompute_max_diff=rho_recompute_max_diff,
        rho_recompute_ok=rho_recompute_ok, rho12_consistency=rho12_consistency,
        n_cache_sectors=n_cache_sectors, n_merged_sectors=len(merged),
        merged_max_level=merged_max_level, have_13=have_13, have_14=have_14,
        Lambda_Z=LAMBDA_Z, jensen_s=JENSEN_S, Gamma_effacement=float(Gamma_effacement),
        N_cells=int(N_cells),
        audit_sha256=audit_sha, content_sha256=content_sha, closure_hash=closure,
        phase1_timing_json=json.dumps(phase1_timing),
    )

    _make_plot_direct(rho_B, w0_cac, spread_CAC, verdict, FB_PRIOR_RHO_13, FB_PRIOR_RHO_14)

    value = (f"spread_CAC={spread_CAC:.6g} rho_B(12)={rho_B[12]:.6f} rho_B(13)={rho_B[13]:.6f} "
             f"rho_B(14)={rho_B[14]:.6f} w0CAC(12)={w0_cac[12]:.6f} w0CAC(13)={w0_cac[13]:.6f} "
             f"w0CAC(14)={w0_cac[14]:.6f} offset_B={offset_B:.6f} DIRECT_L1314 band_PASS<={SPREAD_PASS_BAND}")
    print_verdict_payload(verdict, value, audit_sha, content_sha)


def _make_plot_direct(rho_B, w0_cac, spread_CAC, verdict, fb13, fb14):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    Ls = [12, 13, 14]
    ax1.plot(Ls, [rho_B[L] for L in Ls], "o-", color="C0", label=r"$\rho_B(L)$ DIRECT")
    ax1.plot([13, 14], [fb13, fb14], "x--", color="C3", label="S103 FB-prior (diagnostic)")
    ax1.set_xlabel("truncation L (p+q)")
    ax1.set_ylabel(r"$\rho_B(L)$  (Zubarev branch-IV moment)")
    ax1.set_title(r"DIRECT $\rho_B(L)$ over $\{12,13,14\}$")
    ax1.set_xticks(Ls)
    ax1.grid(alpha=0.3)
    ax1.legend(fontsize=8)
    ax2.plot(Ls, [w0_cac[L] for L in Ls], "s-", color="C2",
             label=r"$w_0^{\rm CAC}(L)=\rho_B(L)+{\rm offset}_B$")
    ax2.axhline(float(w0_FW), color="k", ls=":", lw=1, label=fr"$w_0^{{FW}}={w0_FW}$")
    ax2.set_xlabel("truncation L (p+q)")
    ax2.set_ylabel(r"$w_0^{\rm CAC}(L)$")
    ax2.set_title(fr"$w_0^{{\rm CAC}}$: spread$={spread_CAC:.5f}$  $\Rightarrow$ {verdict}"
                  f"\n(PASS$\\leq$0.025 | INFO(0.025,0.050] | FAIL$>$0.050)")
    ax2.set_xticks(Ls)
    ax2.grid(alpha=0.3)
    ax2.legend(fontsize=8)
    fig.suptitle(f"{GATE_ID} — branch-IV $w_0$ deep-truncation stability (DIRECT spectra)",
                 fontsize=11)
    fig.tight_layout()
    fig.savefig(SESSION_DIR / "s104_branch_iv_direct_l1314.png", dpi=120)
    plt.close(fig)


def _make_plot_fallback(rho_recompute, phase1_status, n_new, have_13, have_14):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(8, 5))
    Ls = [8, 10, 12]
    ax.plot(Ls, [rho_recompute[L] for L in Ls], "o-", color="C0",
            label=r"$\rho_B(L)$ (cache, L$\leq$12)")
    ax.set_xlabel("truncation L (p+q)")
    ax.set_ylabel(r"$\rho_B(L)$")
    ax.set_title(f"{GATE_ID} — PRE-REG-INC (Phase-1 Sym$^{{13/14}}$ wall not cleared)\n"
                 f"phase1_status={phase1_status}  n_new={n_new}  "
                 f"have_13={have_13} have_14={have_14}  -> deferred to S105")
    ax.grid(alpha=0.3)
    ax.legend(fontsize=9)
    fig.tight_layout()
    fig.savefig(SESSION_DIR / "s104_branch_iv_direct_l1314.png", dpi=120)
    plt.close(fig)


if __name__ == "__main__":
    main()
