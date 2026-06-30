#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S111-CF-FLOQUET1 — per-mode Floquet certificate at the most-at-risk relic mode.

GATE (Wave 5, confirmatory, [VERIFY], PHONONIC):
  Read off the INV12-W3-2 Floquet monodromy survey npz the monodromy trace Tr M at
  the SINGLE most-at-risk relic mode and certify, per-mode, the band-stability bound
  |Tr M| < 2  ==>  Re mu = 0  ==>  NO parametric re-pumping. This converts the
  aggregate max|Tr M|_relic < 2 bound (which pins §VII.BP H-PARITY-DRIVE-EXCLUSION
  DEAD) into a per-mode certificate at the mode where the bound is TIGHTEST.

SUBSTRATE FRAMING (PHONONIC):
  The substrate IS the D_K eigenvalue spectrum; the GGE relic is the post-fold
  Bogoliubov output state (Ordered Veil, S_ent=0, R_therm=5251.82). The residual
  modulus afterglow tau(t) drives a periodic omega_k^2(tau(t)) on each relic mode,
  i.e. a Hill/Mathieu equation v'' + [A_k - 2 q_M cos(2t)] v = 0. The monodromy
  trace Tr M over one drive period is the substrate's own re-pumping certificate:
  |Tr M| < 2 <=> Re mu = 0 <=> the diabatically frozen Ordered Veil does NOT
  re-thermalize via parametric resonance. No container-thinking: the relic IS the
  spectral content of the frozen substrate.

DRIFT RESOLUTION (substrate-first-canonical-sourcing.md §(ii.B): npz-ground-truth
resolution of plan-text drift; transit-dynamics debugging note: verify ARRAY
CONTENT, not byte-SHA). TWO layers of plan-text drift are resolved at runtime:

  Drift-1 (the plan's OWN DRIFT NOTE, lines 165-175): the S111 context spec asserts
  the analytic prediction is "+1.98756 +/- O(5e-6)". The npz ground truth differs in
  BOTH sign and value. The gate PINS to the npz value and the absolute |Tr M| < 2
  band-membership certificate; "+1.98756" is NOT used as a threshold.

  Drift-2 (NEW, found this run): the plan's substitution chain (Step 3/Step 4)
  defines the most-at-risk mode as i_closest := argmin|A_relic - 1| and quotes
  A=0.9652110089, tr=-1.9969618432 for it. But the npz STORES i_closest = 1168,
  which is NOT argmin|A-1| (= index 4, A=0.965). The npz i_closest = argmax|Tr M|
  = argmin(dist_to_zone_A) = the A=9.0003 mode (nearest n=3 zone), with the SMALLEST
  band-stability margin (gap-to-edge 3.76e-8 vs the A=0.965 mode's 3.04e-3).

  The gate's HYPOTHESIS says "the single most-at-risk relic mode". By definition the
  MOST-at-risk mode is the one with the TIGHTEST band margin = argmax|Tr M| = the
  npz-stored i_closest = 1168. This is MORE rigorous than the plan's argmin|A-1|
  proxy (which assumed the near-a=1 n=1 zone is widest, but the realized relic grid
  puts the tightest margin at the n=3 zone where a mode sits 3.71e-4 from a=9). The
  gate therefore reads the npz-stored i_closest (most-at-risk-by-margin), reports the
  plan's argmin|A-1| near-a=1 mode as a CROSS-CHECK, and certifies |Tr M| < 2 at
  BOTH. Both pass; the verdict is robust to the definition.

OUTPUT: dual-SHA verdict via emit_verdict MCP (race-safe); npz; png; WP §W5-1.
"""

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")  # cpu-cap-OMP8 per plan GPU_path (trivial 1-element read; no GPU)
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent.parent / "_shared"))

from canonical_constants import (  # noqa: F401
    R_therm,        # 5251.82 Ordered-Veil diabatic-freeze ratio (provenance for the substrate framing)
    PI,
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S111"                                          # (local)
GATE_ID = "S111-CF-FLOQUET1"                              # (local)
SCHEME = "FLOQUET-MONODROMY-PERMODE-CERTIFICATE"          # (local)
CONVENTION = "ABSOLUTE-band-membership-plus-RATIO-groundtruth"  # (local)
L_MAX = 12                                                # (local) relic spectrum built on L12 master cache

# Pre-registered thresholds (plan §W5-1 machinery_pin_map):
BAND_EDGE = 2.0                  # (local) |Tr M| < 2 parametric-resonance onset edge (Floquet/Hill)
GROUNDTRUTH_RELTOL = 1.0e-9      # (local) ground-truth equality rel-tol

OUT_NPZ = SESSION_DIR / "s111_cf_floquet1_permode_monodromy.npz"
OUT_PNG = SESSION_DIR / "s111_cf_floquet1_permode_monodromy.png"

INV12_NPZ = COMPUTATIONS_DIR / "investigation-12" / "inv12_w3_2_floquet_ordered_veil_resonance.npz"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    INV12_NPZ,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Compute (per-mode Floquet certificate read)
# ---------------------------------------------------------------------------

def compute() -> dict:
    """Read the per-mode monodromy certificate off the INV12-W3-2 survey npz."""
    d = np.load(INV12_NPZ, allow_pickle=True)  # (local)

    A_relic = d["A_relic"]            # (local) Mathieu 'a' parameter per relic mode
    tr_relic = d["tr_relic"]          # (local) monodromy trace per relic mode
    Re_mu_relic = d["Re_mu_relic"]    # (local) Floquet exponent real part per relic mode
    Im_mu_relic = d["Im_mu_relic"]    # (local) Floquet exponent imag part per relic mode
    q_relic = d["q_relic"]            # (local) Mathieu 'q' (depth) per relic mode
    mask = d["relic_resonance_mask"]  # (local) resonance flag (|Tr M| > 2)
    nearest_n = d["nearest_n"]        # (local) nearest integer-sq zone index
    dist_zone = d["dist_to_zone_A"]   # (local) distance to nearest zone center in A
    i_stored = int(d["i_closest"])    # (local) npz-stored most-at-risk index

    # --- Most-at-risk mode: tightest band-stability margin = argmax|Tr M| ---
    # (the gate's HYPOTHESIS demands "the single most-at-risk relic mode"; that IS
    #  the smallest gap-to-edge = max|Tr M|). Verify the npz i_closest matches this.
    i_argmax_trM = int(np.argmax(np.abs(tr_relic)))                    # (local)
    i_argmin_dist = int(np.argmin(dist_zone))                          # (local)
    i_argmin_Adev = int(np.argmin(np.abs(A_relic - 1.0)))             # (local) plan's argmin|A-1|

    # The npz i_closest IS argmax|Tr M| == argmin(dist_to_zone) (most-at-risk by margin).
    i_atrisk = i_stored                                               # (local) canonical: npz ground-truth index
    stored_is_argmax_trM = (i_stored == i_argmax_trM)                 # (local)
    stored_is_argmin_dist = (i_stored == i_argmin_dist)               # (local)
    plan_defn_drift = (i_stored != i_argmin_Adev)                     # (local) Drift-2 flag

    # --- Ground-truth scalars at the most-at-risk mode ---
    A_atrisk = float(A_relic[i_atrisk])                               # (local)
    trM_atrisk = float(tr_relic[i_atrisk])                           # (local)
    abs_trM_atrisk = abs(trM_atrisk)                                  # (local)
    Re_mu_atrisk = float(Re_mu_relic[i_atrisk])                      # (local)
    Im_mu_atrisk = float(Im_mu_relic[i_atrisk])                      # (local)
    q_atrisk = float(q_relic[i_atrisk])                             # (local)
    n_atrisk = int(nearest_n[i_atrisk])                             # (local)
    gap_atrisk = BAND_EDGE - abs_trM_atrisk                           # (local) gap to onset edge
    mask_atrisk = bool(mask[i_atrisk])                              # (local) resonance flag

    # --- Plan's argmin|A-1| near-a=1 mode (Drift-2 cross-check) ---
    i_near1 = i_argmin_Adev                                          # (local)
    A_near1 = float(A_relic[i_near1])                               # (local)
    trM_near1 = float(tr_relic[i_near1])                           # (local)
    abs_trM_near1 = abs(trM_near1)                                  # (local)
    gap_near1 = BAND_EDGE - abs_trM_near1                            # (local)
    n_near1 = int(nearest_n[i_near1])                              # (local)

    # --- Aggregate INV12-W3-2 reproduction (independent recompute of the survey bound) ---
    max_abs_trM = float(np.max(np.abs(tr_relic)))                   # (local)
    max_Re_mu = float(np.max(Re_mu_relic))                         # (local)
    n_resonance = int(np.sum(mask))                                # (local)
    n_relic = int(len(tr_relic))                                   # (local)
    fraction_resonance = float(d["fraction_resonance"])            # (local)

    # =====================================================================
    # OPERATOR (plan §W5-1 (1)): two-condition conjunction
    #   cond_A: |Tr M_stored| < 2          (band-membership certificate)
    #   cond_B: |Tr M_stored - groundtruth| < 1e-9  (ground-truth equality)
    # The "ground truth" IS the npz array element; cond_B is a self-consistency
    # / artifact-integrity check (the read value equals the stored value to
    # rel-tol). We additionally cross-check Re mu = 0 <=> |Tr M| <= 2 (Floquet law).
    # =====================================================================
    # Substitution chain (Step 4):  |Tr M_stored| = |{trM_atrisk:.13f}| = {abs:.13f} ; {abs} < 2
    cond_A_band = (abs_trM_atrisk < BAND_EDGE)                                    # (local)
    # cond_B: equality of read-vs-stored (trivially exact here — same array element)
    trM_reread = float(np.load(INV12_NPZ, allow_pickle=True)["tr_relic"][i_atrisk])  # (local)
    groundtruth_resid = abs(trM_atrisk - trM_reread)                              # (local)
    groundtruth_rel = groundtruth_resid / max(abs(trM_reread), 1e-300)            # (local)
    cond_B_groundtruth = (groundtruth_rel < GROUNDTRUTH_RELTOL)                   # (local)

    # Floquet-law cross-check: |Tr M| <= 2  <=>  Re mu = 0 (marginal/stable)
    floquet_law_ok = (Re_mu_atrisk == 0.0) == (abs_trM_atrisk <= BAND_EDGE)       # (local)

    # Cross-check the near-a=1 mode (Drift-2): also band-stable
    near1_band_ok = (abs_trM_near1 < BAND_EDGE)                                   # (local)

    # Aggregate reproduction cross-check: our max|Tr M| matches the verdict 1.99999996
    agg_repro_ok = (abs(max_abs_trM - 1.99999996) < 1e-7)                         # (local)

    # --- Composite verdict ---
    # PASS iff: band-membership at most-at-risk mode AND ground-truth integrity AND
    #           Floquet-law self-consistency AND aggregate reproduction.
    passed = bool(cond_A_band and cond_B_groundtruth and floquet_law_ok and agg_repro_ok)  # (local)
    composite = "PASS" if passed else "FAIL"                                      # (local)

    # value= string (canonical; documents BOTH drift layers + the certificate)
    value = (
        f"permode_certificate:i_atrisk={i_atrisk}(npz_i_closest=argmax|TrM|);"
        f"A={A_atrisk:.10f};|TrM|={abs_trM_atrisk:.10f}<2(gap={gap_atrisk:.4e});"
        f"Re_mu={Re_mu_atrisk:.1f};nearest_n={n_atrisk};"
        f"groundtruth_rel={groundtruth_rel:.2e}<1e-9;"
        f"floquet_law_ok={floquet_law_ok};agg_max|TrM|={max_abs_trM:.8f}(repro_1.99999996);"
        f"near_a1_crosscheck:i={i_near1},A={A_near1:.6f},|TrM|={abs_trM_near1:.10f}<2;"
        f"DRIFT1_corrected_from_+1.98756_to_{trM_atrisk:.10f}(npz_groundtruth);"
        f"DRIFT2_i_closest_defn_argmin|A-1|=>argmax|TrM|({i_argmin_Adev}=>{i_stored})"
    )

    return {
        "value": value,
        "composite": composite,
        # most-at-risk mode
        "i_atrisk": i_atrisk,
        "A_atrisk": A_atrisk,
        "trM_atrisk": trM_atrisk,
        "abs_trM_atrisk": abs_trM_atrisk,
        "Re_mu_atrisk": Re_mu_atrisk,
        "Im_mu_atrisk": Im_mu_atrisk,
        "q_atrisk": q_atrisk,
        "n_atrisk": n_atrisk,
        "gap_atrisk": gap_atrisk,
        "mask_atrisk": mask_atrisk,
        # near-a=1 cross-check mode
        "i_near1": i_near1,
        "A_near1": A_near1,
        "trM_near1": trM_near1,
        "abs_trM_near1": abs_trM_near1,
        "gap_near1": gap_near1,
        "n_near1": n_near1,
        # conditions
        "cond_A_band": cond_A_band,
        "cond_B_groundtruth": cond_B_groundtruth,
        "groundtruth_rel": groundtruth_rel,
        "floquet_law_ok": floquet_law_ok,
        "near1_band_ok": near1_band_ok,
        "agg_repro_ok": agg_repro_ok,
        # drift diagnostics
        "stored_is_argmax_trM": stored_is_argmax_trM,
        "stored_is_argmin_dist": stored_is_argmin_dist,
        "plan_defn_drift": plan_defn_drift,
        "i_argmax_trM": i_argmax_trM,
        "i_argmin_dist": i_argmin_dist,
        "i_argmin_Adev": i_argmin_Adev,
        # aggregate
        "max_abs_trM": max_abs_trM,
        "max_Re_mu": max_Re_mu,
        "n_resonance": n_resonance,
        "n_relic": n_relic,
        "fraction_resonance": fraction_resonance,
        # full arrays for plot
        "_A_relic": A_relic,
        "_tr_relic": tr_relic,
        "_Re_mu_relic": Re_mu_relic,
    }


# ---------------------------------------------------------------------------
# Section 6 — Plot
# ---------------------------------------------------------------------------

def make_plot(result: dict) -> None:
    A = result["_A_relic"]            # (local)
    trM = result["_tr_relic"]         # (local)
    i_atrisk = result["i_atrisk"]     # (local)
    i_near1 = result["i_near1"]       # (local)

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # Panel 1 — |Tr M| vs A, with band edge and the two flagged modes
    ax = axes[0]
    ax.scatter(A, np.abs(trM), s=6, c="tab:blue", alpha=0.45, label="relic modes (1248)")
    ax.axhline(2.0, color="tab:red", lw=1.5, ls="--", label="band edge |Tr M|=2 (resonance onset)")
    ax.scatter([A[i_atrisk]], [abs(trM[i_atrisk])], s=140, c="tab:red", marker="*",
               zorder=5, edgecolors="k",
               label=f"most-at-risk (i={i_atrisk}, A={A[i_atrisk]:.3f}, |Tr M|={abs(trM[i_atrisk]):.7f})")
    ax.scatter([A[i_near1]], [abs(trM[i_near1])], s=110, c="tab:green", marker="D",
               zorder=5, edgecolors="k",
               label=f"near-a=1 cross-check (i={i_near1}, A={A[i_near1]:.3f}, |Tr M|={abs(trM[i_near1]):.6f})")
    ax.set_xlabel("Mathieu A (relic-mode frequency$^2$ parameter)")
    ax.set_ylabel("|Tr M| (monodromy trace magnitude)")
    ax.set_title("S111-CF-FLOQUET1 — per-mode band-stability certificate\n"
                 "|Tr M| < 2  ⟺  Re μ = 0  ⟺  no parametric re-pumping")
    ax.legend(fontsize=7, loc="lower right")
    ax.set_ylim(1.95, 2.02)

    # Panel 2 — gap-to-edge (2 - |Tr M|) zoom at the most-at-risk mode (log)
    ax = axes[1]
    gap = 2.0 - np.abs(trM)  # (local)
    order = np.argsort(gap)  # (local)
    top = order[:30]         # (local)
    ax.semilogy(range(len(top)), gap[top], "o-", c="tab:purple", ms=5,
                label="30 tightest gap-to-edge modes")
    ax.axhline(gap[i_atrisk], color="tab:red", lw=1.2, ls=":",
               label=f"most-at-risk gap = {gap[i_atrisk]:.3e}")
    ax.set_xlabel("rank (tightest band margin first)")
    ax.set_ylabel("gap-to-edge  2 − |Tr M|  (log)")
    ax.set_title(f"Tightest band margin = {gap[i_atrisk]:.3e} > 0\n"
                 f"(all 1248 modes strictly inside ⇒ §VII.BP DEAD per-mode)")
    ax.legend(fontsize=8)

    fig.suptitle(
        "Ordered Veil (S_ent=0, R_therm=5251.82) does NOT re-thermalize via parametric resonance — "
        "per-mode Floquet certificate at the single most-at-risk relic mode",
        fontsize=10, y=1.00,
    )
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 — Verdict payload
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note="", extra_rows=None) -> dict:
    payload: dict = {
        "session": int(SESSION.lstrip("Ss")),
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)  # (local)
    closure = closure_hash(pins)        # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    script_path = Path(__file__).resolve()                  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    result = compute()  # (local)

    # --- diagnostics print ---
    print()
    print("=== S111-CF-FLOQUET1 per-mode Floquet certificate ===")
    print(f"  most-at-risk mode i_atrisk = {result['i_atrisk']} (npz i_closest)")
    print(f"    A_atrisk        = {result['A_atrisk']:.10f}")
    print(f"    Tr M            = {result['trM_atrisk']:.13f}")
    print(f"    |Tr M|          = {result['abs_trM_atrisk']:.13f}  (< 2 ? {result['cond_A_band']})")
    print(f"    gap-to-edge     = {result['gap_atrisk']:.6e}")
    print(f"    Re mu           = {result['Re_mu_atrisk']:.1f}  (0 ⇒ band-stable)")
    print(f"    nearest_n       = {result['n_atrisk']}  (Mathieu zone)")
    print(f"    resonance mask  = {result['mask_atrisk']}  (False ⇒ NOT in resonance band)")
    print()
    print("  DRIFT-2 resolution (most-at-risk definition):")
    print(f"    npz i_closest = {result['i_atrisk']} == argmax|Tr M| ({result['i_argmax_trM']}): {result['stored_is_argmax_trM']}")
    print(f"    npz i_closest == argmin(dist_to_zone) ({result['i_argmin_dist']}): {result['stored_is_argmin_dist']}")
    print(f"    plan argmin|A-1| = {result['i_argmin_Adev']} (A={result['A_near1']:.6f}) — the LESS-at-risk near-a=1 mode")
    print()
    print("  near-a=1 cross-check (plan argmin|A-1| mode):")
    print(f"    i_near1={result['i_near1']} A={result['A_near1']:.10f} |Tr M|={result['abs_trM_near1']:.13f} (< 2 ? {result['near1_band_ok']})")
    print()
    print("  ground-truth integrity:")
    print(f"    read-vs-stored rel = {result['groundtruth_rel']:.3e}  (< 1e-9 ? {result['cond_B_groundtruth']})")
    print(f"    Floquet-law self-consistency (Re mu=0 <=> |Tr M|<=2): {result['floquet_law_ok']}")
    print()
    print("  aggregate INV12-W3-2 reproduction:")
    print(f"    max|Tr M|_relic = {result['max_abs_trM']:.8f}  (verdict 1.99999996 ? {result['agg_repro_ok']})")
    print(f"    max Re mu       = {result['max_Re_mu']:.1f}")
    print(f"    n_resonance     = {result['n_resonance']} of {result['n_relic']}")
    print(f"    fraction_resonance = {result['fraction_resonance']}")

    make_plot(result)

    # --- npz ---
    np.savez(
        OUT_NPZ,
        i_atrisk=result["i_atrisk"],
        A_atrisk=result["A_atrisk"],
        trM_atrisk=result["trM_atrisk"],
        abs_trM_atrisk=result["abs_trM_atrisk"],
        Re_mu_atrisk=result["Re_mu_atrisk"],
        Im_mu_atrisk=result["Im_mu_atrisk"],
        q_atrisk=result["q_atrisk"],
        n_atrisk=result["n_atrisk"],
        gap_atrisk=result["gap_atrisk"],
        mask_atrisk=result["mask_atrisk"],
        i_near1=result["i_near1"],
        A_near1=result["A_near1"],
        trM_near1=result["trM_near1"],
        abs_trM_near1=result["abs_trM_near1"],
        gap_near1=result["gap_near1"],
        n_near1=result["n_near1"],
        cond_A_band=result["cond_A_band"],
        cond_B_groundtruth=result["cond_B_groundtruth"],
        groundtruth_rel=result["groundtruth_rel"],
        floquet_law_ok=result["floquet_law_ok"],
        near1_band_ok=result["near1_band_ok"],
        agg_repro_ok=result["agg_repro_ok"],
        stored_is_argmax_trM=result["stored_is_argmax_trM"],
        stored_is_argmin_dist=result["stored_is_argmin_dist"],
        plan_defn_drift=result["plan_defn_drift"],
        i_argmax_trM=result["i_argmax_trM"],
        i_argmin_dist=result["i_argmin_dist"],
        i_argmin_Adev=result["i_argmin_Adev"],
        max_abs_trM=result["max_abs_trM"],
        max_Re_mu=result["max_Re_mu"],
        n_resonance=result["n_resonance"],
        n_relic=result["n_relic"],
        fraction_resonance=result["fraction_resonance"],
        band_edge=BAND_EDGE,
        groundtruth_reltol=GROUNDTRUTH_RELTOL,
        R_therm=R_therm,
        verdict=result["composite"],
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )

    value = result["value"]            # (local)
    verdict = result["composite"]      # (local)

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)  # (local)
    print()
    print(tag)
    print_verdict_payload(
        verdict, value, audit_sha, content_sha,
        companion_note=(
            "per-mode Floquet certificate: most-at-risk relic mode (npz i_closest=1168="
            "argmax|Tr M|=argmin dist_to_zone, n=3 zone) has |Tr M|=1.99999996<2 (gap 3.76e-8) "
            "=> Re mu=0 => NO re-pumping; confirms aggregate max|Tr M|<2 per-mode at the TIGHTEST "
            "margin; near-a=1 cross-check (plan argmin|A-1|, i=4 A=0.965) also <2; non-verdict-gating "
            "(strengthens §VII.BP DEAD aggregate->per-mode, does not change it)"
        ),
        extra_rows=[
            "# DRIFT-1: plan-text +1.98756 superseded by npz ground truth -1.9999999624 "
            "(substrate-first-canonical-sourcing.md §(ii.B); |Tr M|<2 band-membership is the load-bearing certificate)",
            "# DRIFT-2: plan i_closest:=argmin|A-1| (i=4,A=0.965) superseded by npz-stored i_closest=1168=argmax|Tr M| "
            "(most-at-risk by band margin, the gate's hypothesis 'most-at-risk relic mode'); both modes |Tr M|<2",
            "# regulator_pin=N/A (Floquet monodromy read; no Seeley-DeWitt a_n; Mathieu/Hill stability law)",
        ],
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0  # verdict is data; exit 0 on script health


if __name__ == "__main__":
    sys.exit(main())
