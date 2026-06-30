#!/usr/bin/env python3
"""
S111 W5-2 S111-CF-FLOQUET2 — Sage-exact DTC counterfactual-depth threshold
=========================================================================

Gate: S111-CF-FLOQUET2 ([VERIFY-THEOREM])

Pre-registered threshold (THEOREM tolerance, machine-eps):
  h_par_crit == 2*|A-1|/A  (QQ-exact)  AND  miss == h_par_crit/h_par  (QQ-exact)
  PASS-content: the Sage-exact rationals reproduce 14/193 and 1400000/16019 to QQ
                exactness (float image agreement < 1e-12).
  Canonical OUTCOME is INFO (structural-prediction registration; no PASS/FAIL on
  substrate physics). FAIL iff the rational does NOT reproduce 14/193 (algebra bug).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py (feeds audit_sha256 only)
  - computations/investigation-12/inv12_w3_2_floquet_ordered_veil_resonance.npz
        (npz-floored detuning cross-check: A_relic[i_closest], h_par)
  - computations/session-101/s101_gate_verdicts.txt (h_par=8.3e-4 provenance: S101-W1-QEQ-RELIC-ODDFLOOR)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<h_par_crit=14/193 ; miss=1400000/16019 ; INFO>,
   scheme=FLOQUET-DTC-DEPTH-THRESHOLD-SAGE-EXACT,
   convention=RATIO+ABSOLUTE/THEOREM, L_max=N/A)

Classification: PHONONIC

METHODOLOGY
-----------
A discrete time crystal (DTC) is the period-doubled re-pumping of the substrate's
GGE relic modes through the modulus afterglow tau(t). Each relic mode obeys the
Mathieu/Hill equation v'' + [A - 2 q_M cos(2t)] v = 0 (inv-12 W3-2). The period-2
(n=1) instability tongue about a=1 has half-width Delta_a_half^(1) ~ q_M = A*h_par/2
(McLachlan). DTC onset (the nearest-A=1 relic mode enters the tongue) requires the
half-width to reach the detuning: A*h_par_crit/2 = |A-1|  =>  h_par_crit = 2|A-1|/A.
This gate computes h_par_crit Sage-exact (QQ) in the rounded-spec form (A=965/1000,
|A-1|=35/1000 -> 70/965 = 14/193) and the miss-factor h_par_crit/h_par with
h_par=83/100000 -> 1400000/16019 = 87.396x. The npz-floored detuning
(A=0.9652110089, |A-1|=0.03478899) gives miss = 86.85x as a companion cross-check.
The DTC-absence is registered as a falsifiable structural prediction: a substrate
with h_par >= 14/193 (87x deeper modulus afterglow) WOULD time-crystallize.

NON-verdict-gating: this gate does NOT change the section-VII.BP DEAD verdict (already
pinned three independent ways: the INV12-W3-2 aggregate max|Tr M|_relic=1.99999996<2,
the Mathieu depth q_M<=5.25e-3<<1 narrow-regime derivation, and this counterfactual-
depth threshold). It pins the Sage-exact threshold as a prediction.

DRIFT NOTE (mnemonic-vs-exact discipline, math-scripts.md):
  The S111 context spec asserts miss="84.34x". The Sage-exact rounded-spec value is
  87.396x (3.62% deviation) and the npz-floored value is 86.850x (2.98% deviation);
  BOTH exceed the 1% mnemonic-vs-exact threshold => USE THE EXACT FORM. The gate PINS
  14/193 and 1400000/16019 as the registry THEOREM values, emits 86.85x as the npz-
  floored companion annotation, and flags the context's 84.34 as superseded in value=.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- Sage-exact arithmetic via Python `fractions.Fraction` (closed-form QQ; the rationals
  were also independently Sage-MCP-verified at plan-freeze and in-session).
- CPU-only (no GPU; trivial rational arithmetic), OMP capped at 8 threads.
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- Gate verdict emitted via the `emit_verdict` knowledge-MCP tool (race-safe); the
  script PRINTS the payload (print_verdict_payload); the dispatching AGENT calls
  mcp__knowledge__emit_verdict(**payload). The script does NOT write the verdict file.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os

os.environ.setdefault("OMP_NUM_THREADS", "8")   # CPU-cap (no GPU; trivial rationals)
os.environ.setdefault("MKL_NUM_THREADS", "8")

from canonical_constants import *  # noqa: F401,F403  (framework constants; M_KK, tau_fold, etc.)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from fractions import Fraction  # exact rationals (QQ analog for closed-form arithmetic)
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

SESSION = "S111"                                                   # (local)
GATE_ID = "S111-CF-FLOQUET2"                                       # (local)
SCHEME = "FLOQUET-DTC-DEPTH-THRESHOLD-SAGE-EXACT"                  # (local)
CONVENTION = "RATIO+ABSOLUTE/THEOREM"                              # (local)
L_MAX = "N/A"                                                      # (local) analytic Mathieu-tongue formula, not a spectral compute

# Pre-registered Sage-exact THEOREM targets (verified Sage-MCP at plan-freeze)
H_PAR_CRIT_TARGET = Fraction(14, 193)                             # (local) rounded-spec h_par_crit = 2*(35/1000)/(965/1000)
MISS_TARGET = Fraction(1400000, 16019)                           # (local) rounded-spec miss = (14/193)/(83/100000)
FLOAT_TOL = 1e-12                                                # (local) float-image agreement tolerance

# Rounded-spec inputs (clean registry rationals)
A_RS = Fraction(965, 1000)                                        # (local) A = 0.965 (rounded-spec)
DET_RS = Fraction(35, 1000)                                       # (local) |A-1| = 0.035 (rounded-spec)
H_PAR = Fraction(83, 100000)                                      # (local) realized h_par = 8.3e-4 (S101-W1-QEQ-RELIC-ODDFLOOR)
CONTEXT_MISS_DRIFT = 84.34                                        # (local) S111 context spec value (superseded; 3.62% drift)

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / "s111_cf_floquet2_dtc_depth_threshold.npz"
OUT_PNG = SESSION_DIR / "s111_cf_floquet2_dtc_depth_threshold.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    COMPUTATIONS_DIR / "investigation-12" / "inv12_w3_2_floquet_ordered_veil_resonance.npz",
    COMPUTATIONS_DIR / "session-101" / "s101_gate_verdicts.txt",
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict[str, str]) -> tuple[str, str]:
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
# Section 5 — Compute
# ---------------------------------------------------------------------------

def compute() -> dict:
    """DTC counterfactual-depth threshold, Sage-exact (QQ via Fraction).

    Substitution chain (math-scripts.md Double-Check Logic):
      Step 1: q_M(A) = A*h_par/2                         [period-2 Mathieu depth]
      Step 2: n=1 tongue half-width about a=1:
              Delta_a_half^(1) ~ q_M = A*h_par/2          [McLachlan]
      Step 3: DTC onset when half-width == detuning:
              A*h_par_crit/2 = |A-1|                       [resonance onset]
      Step 4: h_par_crit = 2*|A-1|/A.
      Simplify (rounded-spec A=965/1000, |A-1|=35/1000):
              h_par_crit = 2*(35/1000)/(965/1000) = 70/965 = 14/193.
      miss = (14/193)/(83/100000) = 1400000/16019 = 87.396x.
      Direction: miss = 87.40 >> 1 => realized h_par=8.3e-4 sits 87x BELOW DTC onset
                 => NO discrete-time-crystal re-pumping => Ordered Veil stays frozen.
    """
    # ---- ROUNDED-SPEC (registry THEOREM values) ----
    h_par_crit_rs = 2 * DET_RS / A_RS                            # (local) = 70/965 = 14/193
    miss_rs = h_par_crit_rs / H_PAR                              # (local) = 1400000/16019
    q_M_realized_rs = A_RS * H_PAR / 2                           # (local) realized period-2 depth (rounded-spec A)
    onset_identity_rs = (A_RS * h_par_crit_rs / 2)              # (local) must equal DET_RS exactly

    # Exactness checks (QQ-exact: Fraction equality is bit-exact)
    eq_14_193 = (h_par_crit_rs == H_PAR_CRIT_TARGET)             # (local)
    eq_70_965 = (h_par_crit_rs == Fraction(70, 965))            # (local) reduces to 14/193
    eq_miss = (miss_rs == MISS_TARGET)                          # (local)
    onset_exact_rs = (onset_identity_rs == DET_RS)             # (local) Step-3 onset identity

    # Float-image agreement < FLOAT_TOL
    float_dev_h = abs(float(h_par_crit_rs) - 14.0 / 193.0)       # (local)
    float_dev_miss = abs(float(miss_rs) - 1400000.0 / 16019.0)   # (local)

    # ---- NPZ-FLOORED (companion cross-check; NOT the registry value) ----
    npz = np.load(INPUT_FILES[1])                                # (local) inv-12 W3-2 npz
    A_npz_arr = np.asarray(npz["A_relic"])                       # (local)
    i_closest = int(np.argmin(np.abs(A_npz_arr - 1.0)))         # (local) nearest-A=1 relic mode
    A_npz = float(A_npz_arr[i_closest])                          # (local) = 0.9652110089
    det_npz = abs(A_npz - 1.0)                                   # (local) = 0.03478899
    h_par_npz_stored = float(npz["h_par"])                       # (local) = 0.00083 (npz ground truth)
    # npz-floored detuning -> threshold via exact dyadic rationals of the float64
    A_npz_q = Fraction(A_npz)                                    # (local) exact dyadic value
    det_npz_q = Fraction(det_npz)                                # (local) exact dyadic value
    h_par_npz_q = Fraction(h_par_npz_stored)                     # (local) exact dyadic value of stored h_par
    h_par_crit_npz = 2 * det_npz_q / A_npz_q                     # (local)
    miss_npz = h_par_crit_npz / h_par_npz_q                      # (local) = 86.850x
    onset_exact_npz = (A_npz_q * h_par_crit_npz / 2 == det_npz_q)  # (local)

    # ---- cross-check: stored h_par matches the S101-W1 pin used in rounded-spec ----
    h_par_match = (abs(h_par_npz_stored - float(H_PAR)) < 1e-12)  # (local) npz h_par == 8.3e-4

    # ---- context-drift quantification (mnemonic-vs-exact) ----
    drift_rs = abs(float(miss_rs) - CONTEXT_MISS_DRIFT) / CONTEXT_MISS_DRIFT     # (local) 3.62%
    drift_npz = abs(float(miss_npz) - CONTEXT_MISS_DRIFT) / CONTEXT_MISS_DRIFT   # (local) 2.98%

    # ---- gate verdict logic ----
    # THEOREM exactness PASS-content: all QQ-equalities hold AND float images agree.
    theorem_ok = (
        eq_14_193 and eq_70_965 and eq_miss and onset_exact_rs
        and float_dev_h < FLOAT_TOL and float_dev_miss < FLOAT_TOL
    )                                                            # (local)
    # Canonical outcome is INFO (structural-prediction registration). FAIL only on
    # algebra/script bug (theorem identities do NOT reproduce). No substrate-physics PASS.
    if not theorem_ok:
        verdict = "FAIL"                                         # (local) algebra/derivation bug
    else:
        verdict = "INFO"                                         # (local) structural-prediction registration

    return {
        "verdict": verdict,
        # rounded-spec registry THEOREM values
        "h_par_crit_num": h_par_crit_rs.numerator,
        "h_par_crit_den": h_par_crit_rs.denominator,
        "h_par_crit_float": float(h_par_crit_rs),
        "miss_num": miss_rs.numerator,
        "miss_den": miss_rs.denominator,
        "miss_float": float(miss_rs),
        "q_M_realized_float": float(q_M_realized_rs),
        "A_rs_float": float(A_RS),
        "det_rs_float": float(DET_RS),
        "h_par_float": float(H_PAR),
        # exactness flags
        "eq_14_193": eq_14_193,
        "eq_miss": eq_miss,
        "onset_exact_rs": onset_exact_rs,
        "float_dev_h": float_dev_h,
        "float_dev_miss": float_dev_miss,
        # npz-floored companion
        "i_closest": i_closest,
        "A_npz": A_npz,
        "det_npz": det_npz,
        "h_par_npz_stored": h_par_npz_stored,
        "h_par_crit_npz_float": float(h_par_crit_npz),
        "miss_npz_float": float(miss_npz),
        "onset_exact_npz": onset_exact_npz,
        "h_par_match": h_par_match,
        # drift
        "context_miss_drift": CONTEXT_MISS_DRIFT,
        "drift_rs": drift_rs,
        "drift_npz": drift_npz,
    }


def make_plot(r: dict) -> None:
    """Plot the n=1 Mathieu tongue half-width q_M(h_par)=A*h_par/2 vs the detuning |A-1|,
    marking the realized h_par and the DTC onset h_par_crit = 14/193."""
    A = r["A_rs_float"]                                          # (local)
    det = r["det_rs_float"]                                      # (local)
    h_par = r["h_par_float"]                                     # (local)
    h_crit = r["h_par_crit_float"]                               # (local)

    h_grid = np.linspace(0.0, 1.1 * h_crit, 600)                 # (local)
    halfwidth = A * h_grid / 2.0                                 # (local) Delta_a_half^(1) ~ q_M

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.2))

    # Left: half-width vs detuning; onset where they cross
    ax1.plot(h_grid, halfwidth, color="C0", lw=2,
             label=r"$\Delta a_{1/2}^{(1)} \approx q_M = A\,h_{\rm par}/2$")
    ax1.axhline(det, color="C3", ls="--", lw=1.8,
                label=r"detuning $|A-1|=%.4f$" % det)
    ax1.axvline(h_crit, color="C2", ls="-.", lw=1.8,
                label=r"DTC onset $h_{\rm par}^{\rm crit}=14/193=%.5f$" % h_crit)
    ax1.axvline(h_par, color="k", ls=":", lw=1.8,
                label=r"realized $h_{\rm par}=8.3{\times}10^{-4}$")
    ax1.plot([h_crit], [det], "o", color="C2", ms=8, zorder=5)
    ax1.set_xlabel(r"$h_{\rm par}$ (modulus-afterglow depth)")
    ax1.set_ylabel(r"period-2 tongue half-width about $a=1$")
    ax1.set_title("DTC onset: half-width reaches detuning at $14/193$")
    ax1.legend(fontsize=8, loc="upper left")
    ax1.grid(alpha=0.3)

    # Right: miss-factor bar (rounded-spec vs npz-floored vs superseded context)
    labels = ["rounded-spec\n(registry)", "npz-floored\n(cross-check)", "context\n(superseded)"]  # (local)
    vals = [r["miss_float"], r["miss_npz_float"], r["context_miss_drift"]]                        # (local)
    colors = ["C2", "C0", "0.6"]                                                                  # (local)
    bars = ax2.bar(labels, vals, color=colors)
    ax2.axhline(1.0, color="C3", ls="--", lw=1.5, label="DTC threshold (miss=1)")
    for b, v in zip(bars, vals):
        ax2.text(b.get_x() + b.get_width() / 2, v + 1.0, f"{v:.2f}x",
                 ha="center", va="bottom", fontsize=9)
    ax2.set_ylabel(r"miss-factor $h_{\rm par}^{\rm crit}/h_{\rm par}$")
    ax2.set_title("DTC-absence margin (all readings $\\gg 1$)")
    ax2.set_ylim(0, 100)
    ax2.legend(fontsize=8, loc="lower right")
    ax2.grid(alpha=0.3, axis="y")

    fig.suptitle(
        "S111-CF-FLOQUET2 — Sage-exact DTC counterfactual-depth threshold "
        "$h_{\\rm par}^{\\rm crit}=14/193$ (miss $=1400000/16019=87.40\\times$)",
        fontsize=11,
    )
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
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
    if not (sign_verdict is None and magnitude_verdict is None and regime_verdict is None):
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    r = compute()
    make_plot(r)

    # Persist data
    np.savez(
        OUT_NPZ,
        # rounded-spec registry THEOREM values
        h_par_crit_num=r["h_par_crit_num"], h_par_crit_den=r["h_par_crit_den"],
        h_par_crit_float=r["h_par_crit_float"],
        miss_num=r["miss_num"], miss_den=r["miss_den"], miss_float=r["miss_float"],
        q_M_realized_float=r["q_M_realized_float"],
        A_rs_float=r["A_rs_float"], det_rs_float=r["det_rs_float"], h_par_float=r["h_par_float"],
        # exactness flags
        eq_14_193=r["eq_14_193"], eq_miss=r["eq_miss"], onset_exact_rs=r["onset_exact_rs"],
        float_dev_h=r["float_dev_h"], float_dev_miss=r["float_dev_miss"],
        # npz-floored companion
        i_closest=r["i_closest"], A_npz=r["A_npz"], det_npz=r["det_npz"],
        h_par_npz_stored=r["h_par_npz_stored"],
        h_par_crit_npz_float=r["h_par_crit_npz_float"], miss_npz_float=r["miss_npz_float"],
        onset_exact_npz=r["onset_exact_npz"], h_par_match=r["h_par_match"],
        # drift
        context_miss_drift=r["context_miss_drift"], drift_rs=r["drift_rs"], drift_npz=r["drift_npz"],
        # provenance
        audit_sha256=audit_sha, content_sha256=content_sha,
    )

    print("=== RESULTS ===")
    print(f"  h_par_crit (rounded-spec, QQ)  = {r['h_par_crit_num']}/{r['h_par_crit_den']} "
          f"= {r['h_par_crit_float']:.10f}")
    print(f"    == 14/193 ?                  = {r['eq_14_193']}")
    print(f"  miss (rounded-spec, QQ)        = {r['miss_num']}/{r['miss_den']} "
          f"= {r['miss_float']:.6f}x")
    print(f"    == 1400000/16019 ?           = {r['eq_miss']}")
    print(f"  onset identity A*h_crit/2==det = {r['onset_exact_rs']}  (EXACT, QQ)")
    print(f"  float-image dev (h_crit)       = {r['float_dev_h']:.2e}  (< {FLOAT_TOL:.0e})")
    print(f"  float-image dev (miss)         = {r['float_dev_miss']:.2e}  (< {FLOAT_TOL:.0e})")
    print(f"  q_M realized (rounded-spec)    = {r['q_M_realized_float']:.6e}")
    print()
    print(f"  [npz-floored cross-check] i_closest = {r['i_closest']}, "
          f"A = {r['A_npz']:.10f}, |A-1| = {r['det_npz']:.8f}")
    print(f"    h_par (npz stored)           = {r['h_par_npz_stored']:.5e}  "
          f"(matches 8.3e-4: {r['h_par_match']})")
    print(f"    h_par_crit (npz-floored)     = {r['h_par_crit_npz_float']:.8f}")
    print(f"    miss (npz-floored)           = {r['miss_npz_float']:.6f}x")
    print(f"    onset identity (npz)         = {r['onset_exact_npz']}  (EXACT, dyadic QQ)")
    print()
    print(f"  [context-drift] context miss   = {r['context_miss_drift']} (SUPERSEDED)")
    print(f"    drift vs rounded-spec        = {r['drift_rs']*100:.2f}%  (>1% => use exact form)")
    print(f"    drift vs npz-floored         = {r['drift_npz']*100:.2f}%")
    print()

    verdict = r["verdict"]  # (local)

    # value payload (no single-quote chars; emit_verdict wraps value='...')
    value_payload = (
        f"h_par_crit=14/193={r['h_par_crit_float']:.8f}(QQ-exact) "
        f"miss=1400000/16019={r['miss_float']:.4f}x(QQ-exact) "
        f"miss_npz_floored={r['miss_npz_float']:.4f}x(cross-check) "
        f"onset_identity_EXACT_rs={r['onset_exact_rs']}_npz={r['onset_exact_npz']} "
        f"DTC-absent(realized_h_par=8.3e-4<<14/193;87x_margin) "
        f"context_84.34x_SUPERSEDED(drift_rs={r['drift_rs']*100:.2f}pct>1pct_use_exact) "
        f"STRUCTURAL-PREDICTION-REGISTERED(DTC_requires_h_par>=14/193)"
    )  # (local)

    tag = emit_4tuple(value_payload, SCHEME, CONVENTION, L_MAX)
    print(tag)

    # extra companion rows: regulator-pin-free (analytic Mathieu); the structural prediction
    extra = [
        ("# DTC-counterfactual-depth: h_par_crit=14/193=0.07253886 (Sage-exact QQ; rounded-spec "
         "A=965/1000,|A-1|=35/1000); miss=1400000/16019=87.3962x. npz-floored cross-check "
         "h_par_crit=0.07208577, miss=86.8503x (A=0.9652110089,|A-1|=0.03478899). Onset identity "
         "A*h_par_crit/2==|A-1| EXACT (QQ) in BOTH readings."),
        ("# STRUCTURAL PREDICTION (falsifiable): a substrate with h_par>=14/193 (87x deeper modulus "
         "afterglow) WOULD discrete-time-crystallize; the realized Ordered Veil (S_ent=0, "
         "R_therm=5251.82) is DTC-absent by this Sage-exact margin. NON-verdict-gating on VII.BP DEAD "
         "(pinned 3 independent ways: INV12-W3-2 max|TrM|=1.99999996<2; q_M<=5.25e-3<<1; this threshold)."),
        ("# DRIFT-CORRECTION: S111 context spec miss=84.34x SUPERSEDED; Sage-exact 87.3962x (rounded-spec) "
         "/ 86.8503x (npz-floored); both >1% from 84.34 => USE EXACT FORM per math-scripts.md "
         "Mnemonic-vs-exact ratio discipline. canonical write-order: verdict -> canonical_constants "
         "h_par_crit_DTC -> falsifier-master-inventory DTC-absence row (mack-cosmic-bridge)."),
    ]  # (local)

    print_verdict_payload(verdict, value_payload, audit_sha, content_sha, extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    print(f"  artifacts: {OUT_NPZ.name}, {OUT_PNG.name}")
    return 0  # INFO/PASS -> 0; FAIL would still be a valid scientific verdict but this gate FAILs only on bug


if __name__ == "__main__":
    sys.exit(main())
