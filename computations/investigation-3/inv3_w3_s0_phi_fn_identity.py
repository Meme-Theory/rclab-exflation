#!/usr/bin/env python3
"""
INV3-W3-1 — S0 =? phi_paasch^fN identity (machine-eps three-zone kill)
=====================================================================
Gate: INV3-W3-1 ([CHAIN]) — SOLO (orchestrator-inline). Investigation track 3.

Pre-registered three-zone threshold (plan §W3-1):
  delta_min = min(|S0_100a - phi^fN|, |95/56 - phi^fN|)
    PASS iff delta_min < 1e-12   (machine-eps ALGEBRAIC identity)
    FAIL iff delta_min > 1e-3    (coincidence, killed cleanly)
    INFO iff 1e-12 <= delta_min <= 1e-3  (numerical-proximity-not-identity)

Tests whether the framework's charged-lepton SHAPE selector S0 equals Paasch's
phi_paasch raised to his golden-ratio factor fN = sqrt(5)-1.

Inputs:
  - canonical_constants.py (phi_paasch; feeds audit_sha256)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)
S0 candidates are framework gate outputs (knowledge-MCP confirmed):
  - S0_100a       = 1.694153  [S101-NU-DIRAC-ENVELOPE-MAP  b=S0, (sqrtC2,0+) chart; KILL shapeDev +6.88%]
  - S0_101_graded = 95/56     [S101-W3-S0-KNOB knob=iii graded leg = tau_fold/T_acoustic; PASS dev_iii=0.0013]
fN = sqrt(5)-1 [Paasch M-value successive ratio; Sage-exact algebraic irrational]

Classification: PARTICLE (charged-lepton shape selector) on a GEOMETRIC substrate.
"""
from __future__ import annotations

import sys
from pathlib import Path

# Make computations/_shared importable (canonical_constants.py) — defensive.
_SHARED = Path(__file__).resolve().parent.parent / "_shared"
if str(_SHARED) not in sys.path:
    sys.path.insert(0, str(_SHARED))

from canonical_constants import *  # noqa: F401,F403  (provides phi_paasch)

import hashlib
import json
import time
import numpy as np
import mpmath as mp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

mp.mp.dps = 50  # 50-digit precision; the PASS bar is 1e-12, far inside this

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "3"                                            # (local) investigation 3
GATE_ID = "INV3-W3-1"                                    # (local)
SCHEME = "SAGE-QQ-HIGHPREC-S0-PHI-FN-IDENTITY"           # (local)
CONVENTION = "ABSOLUTE"                                  # (local)
L_MAX = "N/A"                                            # (local)

PASS_ZONE = mp.mpf("1e-12")                              # (local) machine-eps identity bar
FAIL_ZONE = mp.mpf("1e-3")                               # (local) coincidence-kill bar

OUT_NPZ = SESSION_DIR / "inv3_w3_s0_phi_fn_identity.npz"
OUT_PNG = SESSION_DIR / "inv3_w3_s0_phi_fn_identity.png"

INPUT_FILES = [SHARED_DIR / "canonical_constants.py"]


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins):
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path, canonical_path, pins):
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def print_verdict_payload(verdict, value, audit_sha, content_sha, extra_rows=None):
    payload = {
        "session": int(SESSION),
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
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


def main():
    t0 = time.time()  # (local)
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)  # (local)
    print(f"  closure: {closure[:16]}... (legacy, informational)")
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    # --- Constants (phi_paasch imported from canonical_constants; never hardcoded) ---
    phi = mp.mpf(repr(float(phi_paasch)))       # (local) bare (3,0)/(0,0) ratio at s=0.15
    fN = mp.sqrt(5) - 1                          # (local) Paasch golden factor (Sage-exact)
    S0_100a = mp.mpf("1.694153")                 # (local) S101-NU-DIRAC-ENVELOPE-MAP b=S0
    S0_101_graded = mp.mpf(95) / mp.mpf(56)      # (local) S101-W3-S0-KNOB graded leg

    # --- Identity test ---
    phi_fN = phi ** fN                           # (local)
    delta_a = abs(S0_100a - phi_fN)              # (local)
    delta_b = abs(S0_101_graded - phi_fN)        # (local)
    delta_min = min(delta_a, delta_b)            # (local)
    closest = "S0_100a=1.694153" if delta_a <= delta_b else "95/56"  # (local)
    inv_a = mp.log(S0_100a) / mp.log(phi)        # (local) exponent x with phi^x = S0_100a
    inv_b = mp.log(S0_101_graded) / mp.log(phi)  # (local)

    if delta_min < PASS_ZONE:
        verdict = "PASS"  # (local)
    elif delta_min > FAIL_ZONE:
        verdict = "FAIL"  # (local)
    else:
        verdict = "INFO"  # (local)

    print(f"phi_paasch          = {mp.nstr(phi, 12)}")
    print(f"fN = sqrt(5)-1      = {mp.nstr(fN, 12)}")
    print(f"phi_paasch^fN       = {mp.nstr(phi_fN, 12)}")
    print(f"S0_100a             = {mp.nstr(S0_100a, 12)}   delta_a = {mp.nstr(delta_a, 6)}")
    print(f"S0_101_graded=95/56 = {mp.nstr(S0_101_graded, 12)}   delta_b = {mp.nstr(delta_b, 6)}")
    print(f"inv exponent a      = {mp.nstr(inv_a, 12)}   (vs fN={mp.nstr(fN, 12)})")
    print(f"inv exponent b      = {mp.nstr(inv_b, 12)}")
    print(f"delta_min           = {mp.nstr(delta_min, 6)}  closest={closest}  -> {verdict}")

    # --- Diagnostic plot: |S0 - phi^x| vs x near x=fN ---
    xs = np.linspace(float(fN) - 0.05, float(fN) + 0.05, 401)  # (local)
    curve_a = np.array([abs(float(S0_100a) - float(phi) ** x) for x in xs])  # (local)
    curve_b = np.array([abs(float(S0_101_graded) - float(phi) ** x) for x in xs])  # (local)

    fig, ax = plt.subplots(1, 1, figsize=(8, 5))
    ax.semilogy(xs, curve_a, color="C0", label="|S0_100a=1.694153 - phi^x|")
    ax.semilogy(xs, curve_b, color="C1", label="|95/56 - phi^x|")
    ax.axvline(float(fN), color="k", ls="--", lw=1, label=f"x = fN = {float(fN):.6f}")
    ax.axhline(1e-3, color="r", ls=":", lw=1, label="FAIL bar 1e-3")
    ax.axhline(1e-12, color="g", ls=":", lw=1, label="PASS bar 1e-12")
    ax.set_xlabel("exponent x")
    ax.set_ylabel("|S0 - phi_paasch^x|")
    ax.set_title(f"INV3-W3-1: S0 =? phi_paasch^fN   (delta_min={float(delta_min):.3e} -> {verdict})")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)

    np.savez(
        OUT_NPZ,
        phi_paasch=float(phi),
        fN=float(fN),
        phi_fN=float(phi_fN),
        S0_100a=float(S0_100a),
        S0_101_graded=float(S0_101_graded),
        delta_a=float(delta_a),
        delta_b=float(delta_b),
        delta_min=float(delta_min),
        inv_exponent_a=float(inv_a),
        inv_exponent_b=float(inv_b),
        pass_zone=float(PASS_ZONE),
        fail_zone=float(FAIL_ZONE),
        x_grid=xs,
        curve_a=curve_a,
        curve_b=curve_b,
        verdict=verdict,
        closest=closest,
    )

    value = (
        f"S0=phi_paasch^fN_TEST:verdict={verdict};"
        f"delta_min={float(delta_min):.6e}@{closest};"
        f"delta_a={float(delta_a):.6e}(S0_100a=1.694153,dead-band);"
        f"delta_b={float(delta_b):.6e}(95div56,FAIL-zone);"
        f"phi_fN={float(phi_fN):.10f};fN={float(fN):.10f};"
        f"inv_exp_a={float(inv_a):.10f}_vs_fN={float(fN):.10f};"
        f"PASSlt1e-12_FAILgt1e-3;NUMERICAL-PROXIMITY-NOT-IDENTITY"
    )  # (local)

    tag = f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})"  # (local)
    print(tag)
    extra = [
        f"# INV3-W3-1 three-zone: PASS<1e-12 (machine-eps identity) / FAIL>1e-3 (coincidence-kill) / INFO dead-band; closest={closest} delta_min={float(delta_min):.6e}",
        "# S0 candidates: S0_100a=1.694153 (S101-NU-DIRAC-ENVELOPE-MAP b=S0, KILL shapeDev+6.88%); 95/56 (S101-W3-S0-KNOB knob=iii graded=tau_fold/T_acoustic)",
        "# phi_paasch=1.531580 known to ~7 sig figs => an algebraic identity is testable to ~1e-6 at best; delta_min=4.19e-4 is ~8 OOM above the 1e-12 bar AND ~2 OOM above the phi_paasch precision floor => proximity, not identity",
    ]  # (local)
    print_verdict_payload(verdict, value, audit_sha, content_sha, extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
