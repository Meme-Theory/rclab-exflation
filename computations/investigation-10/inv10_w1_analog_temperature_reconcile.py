#!/usr/bin/env python3
"""
INV10 W1-5 — INV10-W1-5-ANALOG-TEMPERATURE-RECONCILE
====================================================

Gate: INV10-W1-5-ANALOG-TEMPERATURE-RECONCILE ([VERIFY], solo / orchestrator-inline)
Track: investigation-10 (emit_verdict session=10, track="investigation")

Reconcile the THREE analog temperatures the corpus carries:
  (1) T_acoustic = 0.112 M_KK  — canonical S63 Level-1 internal-acoustic-horizon
                                 temperature (the surface where transit velocity
                                 equals the internal sound speed).
  (2) T_a = hbar*kappa_a/(2pi) — BLV acoustic surface-gravity temperature (S63 QA-H4.2),
                                 kappa_a = 1/2 d_n(c^2 - v^2)|_horizon.
  (3) T_H = hbar*kappa/(2pi)   — Hawking-analog temperature (phonic-exflation-equation-
                                 hawking-collab.md), IDENTICAL kappa form to (2).

Structural reductions (substitution chain, plan §W1-5):
  - T_a / T_H = kappa_a / kappa = 1 EXACTLY: T_a and T_H share the identical
    closed form kappa = 1/2 d_n(c^2 - v^2). They are the SAME surface-gravity
    temperature named twice, NOT two independent temperatures. (analytic; no compute)
  - Canonical sonic surface gravity (session-100a-plan-w3, used in the greybody /
    freeze-in derivation): kappa_SONIC = 2*pi*T_acoustic. This IS the relation
    T_acoustic = hbar*kappa_SONIC/(2*pi) = T_H read backwards — i.e. the canonical
    ledger ALREADY identifies T_acoustic as the analog-Hawking temperature of the
    sonic horizon.
  => All three temperatures collapse to ONE quantity: T_a = T_H = T_acoustic,
     with kappa = kappa_a = kappa_SONIC = 2*pi*0.112 = 0.703717 M_KK.

HONESTY SCOPE (load-bearing — do NOT overclaim):
  This is a LEDGER reconciliation (S95 non-compute-gate clause). The agreement
  T_acoustic == T_H is consistency WITHIN the canonical ledger (the framework
  DEFINES T_acoustic as the sonic surface-gravity temperature via
  kappa_SONIC = 2*pi*T_acoustic), NOT an independent numerical coincidence: this
  gate does NOT re-derive kappa from a first-principles velocity profile
  1/2 d_n(c^2 - v^2) at the Mach-1 surface. The genuine non-circular forward check
  (does the velocity-profile-evaluated kappa independently equal 0.703717?) is a
  separate gate. What this gate establishes: the corpus's three temperature symbols
  refer to one quantity, closing the non-reconciliation the hawking-collab doc
  explicitly flagged (a documentation gap, not a physics inconsistency).

PASS criterion (S95 non-numerical clause): the three temperatures are computed in
consistent M_KK units with explicit provenance, T_a == T_H confirmed by construction
(ratio = 1), the T_acoustic-vs-T_H comparison renders AGREE (max pairwise |ratio-1|
<= tol_agree = 10%), and the structural reading + extremal-branch status are recorded.

Output 4-tuple: (value=<AGREE/...>, scheme=BLV, convention=ABSOLUTE, L_max=N/A)
Classification: PHONONIC
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
SHARED = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_shared")
sys.path.insert(0, SHARED)
from canonical_constants import *  # noqa: F401,F403  (T_acoustic, c_BLV, c_fabric, Mach_max_framework, kappa_BCS, tau_fold)

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

SESSION = "10"                                                     # (local) investigation 10
GATE_ID = "INV10-W1-5-ANALOG-TEMPERATURE-RECONCILE"               # (local)
SCHEME = "BLV"                                                     # (local) surface-gravity temps are BLV-convention
CONVENTION = "ABSOLUTE"                                            # (local) all temperatures in M_KK units
L_MAX = "N/A"                                                      # (local) ledger reconciliation, not a D_K spectral compute

TOL_AGREE = 0.10                                                   # (local) S95 10% consistency band

OUT_NPZ = SESSION_DIR / "inv10_w1_analog_temperature_reconcile.npz"
OUT_PNG = SESSION_DIR / "inv10_w1_analog_temperature_reconcile.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 dual-pin block (S84+ schema)
# ---------------------------------------------------------------------------

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


def closure_hash(pins) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins):
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
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)

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
# Section 5 — Compute (the ledger reconciliation)
# ---------------------------------------------------------------------------

def compute() -> dict:
    hbar = 1.0  # (local) natural M_KK units

    # (1) Canonical Level-1 internal-acoustic-horizon temperature (S63)
    T_acoustic_val = float(T_acoustic)  # (local) 0.112 M_KK

    # (2)==(3) T_a (BLV surface gravity) and T_H (Hawking-analog) share the
    # IDENTICAL kappa form kappa = 1/2 d_n(c^2 - v^2). Hence the ratio is
    # exactly 1 by construction — analytic, no numerical evaluation of kappa needed.
    r_Ta_over_TH = 1.0  # (local) kappa_a / kappa = 1 EXACTLY

    # Canonical sonic surface gravity (session-100a-plan-w3 greybody/freeze-in
    # derivation): kappa_SONIC = 2*pi*T_acoustic. This is T_acoustic = hbar*kappa/(2pi)
    # read backwards => the canonical ledger identifies T_acoustic AS the analog-Hawking
    # temperature of the sonic horizon.
    kappa_sonic = 2.0 * np.pi * T_acoustic_val  # (local) 0.703717... M_KK

    # T_H reconstructed from the canonical sonic surface gravity (the inversion):
    T_H_from_sonic = hbar * kappa_sonic / (2.0 * np.pi)  # (local) == T_acoustic_val exactly

    # Three-way ledger (all in M_KK): T_a == T_H == T_acoustic
    T_a_val = T_H_from_sonic   # (local) T_a == T_H by identical kappa form
    T_H_val = T_H_from_sonic   # (local)

    # Pairwise ratios r_ij = T_i / T_j
    r_Tacoustic_TH = T_acoustic_val / T_H_val   # (local) == 1
    r_Tacoustic_Ta = T_acoustic_val / T_a_val   # (local) == 1
    r_Ta_TH = T_a_val / T_H_val                 # (local) == 1 (cross-check of the analytic identity)

    max_dev = max(
        abs(r_Tacoustic_TH - 1.0),
        abs(r_Tacoustic_Ta - 1.0),
        abs(r_Ta_TH - 1.0),
    )  # (local)

    # Extremal-horizon branch: kappa_SONIC == 0 would force T_H -> 0 (extremal,
    # the BCS-freeze "Dump=extremal horizon" of session-84-w8b — a DIFFERENT horizon).
    # Here kappa_sonic = 0.7037 != 0 => the transit/sonic horizon is NON-EXTREMAL.
    extremal = bool(np.isclose(kappa_sonic, 0.0, atol=1e-12))  # (local) False

    # Verdict (S95 non-numerical clause): AGREE iff T_a==T_H confirmed AND
    # max pairwise |ratio-1| <= TOL_AGREE AND non-extremal.
    Ta_eq_TH = np.isclose(r_Ta_over_TH, 1.0, atol=1e-12)  # (local) True by construction
    agree = bool(Ta_eq_TH and (max_dev <= TOL_AGREE) and (not extremal))  # (local)

    if agree:
        verdict = "PASS"  # (local) AGREE
        reading = ("AGREE: three analog temperatures collapse to one quantity "
                   "T_a==T_H==T_acoustic; kappa=2*pi*T_acoustic=0.703717 M_KK; non-extremal. "
                   "Ledger-internal consistency (canonical S100a kappa_SONIC=2*pi*T_acoustic "
                   "relation), NOT an independent velocity-profile kappa evaluation. "
                   "Closes the hawking-collab flagged non-reconciliation (documentation gap).")
    elif extremal:
        verdict = "INFO"  # (local) extremal branch
        reading = ("INFO: kappa_SONIC -> 0 (extremal horizon) => T_H -> 0, so T_acoustic "
                   "is a DIFFERENT (relic, not surface-gravity) temperature.")
    else:
        verdict = "FAIL"  # (local) genuine ledger inconsistency, non-extremal
        reading = ("FAIL: T_acoustic does not agree with T_H (max_dev > tol) and horizon "
                   "non-extremal => analog-temperature ledger inconsistency.")

    return {
        "value": verdict_value_string(verdict, kappa_sonic, max_dev, extremal),
        "verdict": verdict,
        "reading": reading,
        "T_acoustic": T_acoustic_val,
        "T_a": T_a_val,
        "T_H": T_H_val,
        "kappa_sonic": kappa_sonic,
        "kappa_BCS": float(kappa_BCS),
        "r_Tacoustic_TH": r_Tacoustic_TH,
        "r_Tacoustic_Ta": r_Tacoustic_Ta,
        "r_Ta_TH": r_Ta_TH,
        "max_dev": max_dev,
        "tol_agree": TOL_AGREE,
        "extremal": extremal,
        "c_fabric": float(c_fabric),
        "c_BLV": float(c_BLV),
        "Mach_max_framework": float(Mach_max_framework),
        "tau_fold": float(tau_fold),
    }


def verdict_value_string(verdict: str, kappa_sonic: float, max_dev: float, extremal: bool) -> str:
    # No single-quote chars (emit_verdict wraps value='...').
    return (f"{verdict}-AGREE_T_a==T_H_exact_kappa_form;"
            f"T_acoustic==T_H_via_S100a_kappa_SONIC=2pi*T_acoustic;"
            f"kappa_sonic={kappa_sonic:.6f}_M_KK;non-extremal={not extremal};"
            f"max_pairwise_dev={max_dev:.3e};ledger-internal_NOT_indep_velocity-profile_kappa")


# ---------------------------------------------------------------------------
# Section 6 — Plot
# ---------------------------------------------------------------------------

def make_plot(res: dict):
    fig, ax = plt.subplots(figsize=(7.2, 4.6))
    labels = ["T_acoustic\n(S63 canonical)", "T_a\n(BLV surf. grav.)", "T_H\n(Hawking-analog)"]
    vals = [res["T_acoustic"], res["T_a"], res["T_H"]]
    bars = ax.bar(labels, vals, color=["#3b6fb0", "#5a9b6e", "#b0723b"], width=0.6)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.002, f"{v:.4f}",
                ha="center", va="bottom", fontsize=10)
    ax.axhline(res["T_acoustic"], ls="--", color="grey", lw=0.9)
    ax.set_ylabel("Analog temperature  (M_KK units)")
    ax.set_ylim(0, max(vals) * 1.35)
    ax.set_title("INV10-W1-5: three analog temperatures collapse to ONE\n"
                 f"kappa_SONIC = 2*pi*T_acoustic = {res['kappa_sonic']:.6f} M_KK  "
                 f"(non-extremal); T_a == T_H exact", fontsize=10)
    ax.text(0.5, -0.30,
            "Ledger-internal consistency (canonical S100a relation), NOT an independent\n"
            "velocity-profile 1/2 d_n(c^2-v^2) evaluation — that is the forward gate.",
            transform=ax.transAxes, ha="center", va="top", fontsize=8, color="#555")
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 — emit payload + main
# ---------------------------------------------------------------------------

def print_verdict_payload(verdict, value, audit_sha, content_sha):
    payload = {
        "session": 10,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
        "track": "investigation",
    }
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


def main() -> int:
    t0 = time.time()  # (local)
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy, informational)")

    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    res = compute()

    print(f"  T_acoustic (S63 canonical)      = {res['T_acoustic']:.6f} M_KK")
    print(f"  T_a (BLV surface gravity)       = {res['T_a']:.6f} M_KK")
    print(f"  T_H (Hawking-analog)            = {res['T_H']:.6f} M_KK")
    print(f"  kappa_SONIC = 2*pi*T_acoustic   = {res['kappa_sonic']:.6f} M_KK")
    print(f"  kappa_BCS (extremal cross-ref)  = {res['kappa_BCS']:.6f} M_KK")
    print(f"  ratios: T_ac/T_H={res['r_Tacoustic_TH']:.6f}  T_ac/T_a={res['r_Tacoustic_Ta']:.6f}  T_a/T_H={res['r_Ta_TH']:.6f}")
    print(f"  max pairwise |ratio-1|          = {res['max_dev']:.3e}  (tol_agree={res['tol_agree']})")
    print(f"  extremal horizon                = {res['extremal']}")
    print(f"  reading: {res['reading']}")
    print()

    np.savez(
        OUT_NPZ,
        T_acoustic=res["T_acoustic"], T_a=res["T_a"], T_H=res["T_H"],
        kappa_sonic=res["kappa_sonic"], kappa_BCS=res["kappa_BCS"],
        r_Tacoustic_TH=res["r_Tacoustic_TH"], r_Tacoustic_Ta=res["r_Tacoustic_Ta"],
        r_Ta_TH=res["r_Ta_TH"], max_dev=res["max_dev"], tol_agree=res["tol_agree"],
        extremal=res["extremal"], verdict=res["verdict"], reading=res["reading"],
        c_fabric=res["c_fabric"], c_BLV=res["c_BLV"],
        Mach_max_framework=res["Mach_max_framework"], tau_fold=res["tau_fold"],
    )
    make_plot(res)

    print(f"(value={res['value']!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print_verdict_payload(res["verdict"], res["value"], audit_sha, content_sha)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {res['verdict']} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
