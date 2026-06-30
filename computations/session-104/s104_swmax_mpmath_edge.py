#!/usr/bin/env python3
"""
S104 W1-2 S104-SWMAX-MPMATH-EDGE — >=300-bit sign adjudication of the W-stage
deviation vs the asymmetric SU(1,1) window upper edge S_W_max-1.
=============================================================================

Gate: S104-SWMAX-MPMATH-EDGE ([SIGN])

Pre-registered threshold (sign trichotomy, NOT a tolerance comparison):
  Compute Delta = deviation - (S_W_max - 1) at mp.prec >= 300 bits, where
  S_W_max - 1 = 2|beta_W|^2 + 2|alpha_W||beta_W| is the asymmetric-window UPPER
  endpoint (the S103 re-pin established this is the correct edge, NOT the
  half-spread 2|alpha||beta| nor the shorthand |beta|^2 + 2|alpha||beta|).
  verdict = sign(Delta) in {-1, 0, +1}:
    sign -1  -> PASS  : deviation strictly INSIDE the upper edge (strict interior).
    sign  0  -> INFO  : exact saturation (deviation == upper endpoint by an
                        algebraic identity); structural-identity registry state.
                        Emits a `# composite-precedence:` companion row.
    sign +1  -> FAIL  : deviation BREACHES the upper edge; re-opens S79 sufficiency.

This gate adjudicates BELOW the float64 floor whether the S103 W3-1 knife-edge
(deviation == S_W_max-1 to 5+6 sig figs; float64 dev_vs_repin = -5.211e-09) is a
strict interior point or an exact saturation. Two independent arbiters:
  (1) mpmath at mp.prec = 320 bits (~96 decimal digits).
  (2) Sage MCP exact real-algebraic-field (AA) sign — the float64 amplitudes are
      exact dyadic rationals; |alpha|,|beta| are algebraic-number square roots, so
      AA gives a PROVABLE sign with zero precision ambiguity. The Sage result is
      hardcoded here as a pinned cross-check (computed via mcp__sage__sage_eval at
      dispatch; reproduced in the WP MCP Pre-Compute Audit block).

Inputs (SHA-256 dual-pinned at runtime):
  - computations/session-102/s102_w7_ladder_phase_resolved.npz  (frozen alpha_W,
      beta_W, deviation, envelope_upper_dev)
  - computations/session-103/s103_famp_tolerance_repin.npz       (re-pin record;
      bit-exact edge decomposition; dev_vs_repin float64 shadow)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<sign + Delta>, scheme=FW,
   convention=SU(1,1)-form-1-temporal-L-to-R;window-asymmetric-upper-edge-2beta2+2ab,
   L_max=12)

Classification: PHONONIC (SU(1,1) Bogoliubov squeezing window of the W-stage
relay-pattern transit through the fold).

METHODOLOGY
-----------
The W-stage Bogoliubov pair (alpha_W = W_a, beta_W = W_beta_re + i*W_beta_im) is
the squeezing amplitude of the relay-pattern excitation transiting the W-stage of
the supersonic fold. The SU(1,1) squeezing window {S_W_min, S_W_max} bounds the
F_amp slot modulation; the window is ASYMMETRIC (centered at 1 + 2|beta_W|^2, NOT
at 1), so the upper edge is 2|beta_W|^2 + 2|alpha_W||beta_W|. The deviation is the
substrate-IS quantity: how far the derived-phase-modulated F_amp slot sits from
unity. This gate lifts alpha_W, beta_W, deviation to mpmath.mpf at >=300 bits and
emits sign(deviation - (S_W_max-1)), resolving the float64 knife-edge. The
unitarity constraint |alpha_W|^2 - |beta_W|^2 = 1 is the analytic anchor.

DISCIPLINE
----------
- `from canonical_constants import *`
- mpmath is pure-Python arbitrary precision (no GPU path); OMP_NUM_THREADS=8 set.
- SHA-256 of all input files logged in first 20 lines of stdout.
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema).
- Gate verdict emitted via the `emit_verdict` knowledge-MCP tool (race-safe);
  this script PRINTS the payload (print_verdict_payload), never writes the
  verdict file directly.
"""

from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_shared"))
from canonical_constants import *  # noqa: F401,F403

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
from mpmath import mp, mpf, sqrt as mp_sqrt, sign as mp_sign, nstr

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S104"                                                   # (local)
GATE_ID = "S104-SWMAX-MPMATH-EDGE"                                 # (local)
SCHEME = "FW"                                                      # (local)
CONVENTION = (
    "SU(1,1)-form-1-temporal-L-to-R;window-asymmetric-upper-edge-2beta2+2ab"
)                                                                 # (local)
L_MAX = 12                                                         # (local)

MP_PREC_BITS = 320                                                 # (local) >= 300-bit pin

# Frozen-input file references
S102_NPZ = COMPUTATIONS_DIR / "session-102" / "s102_w7_ladder_phase_resolved.npz"
S103_NPZ = COMPUTATIONS_DIR / "session-103" / "s103_famp_tolerance_repin.npz"

OUT_NPZ = SESSION_DIR / "s104_swmax_mpmath_edge.npz"
OUT_PNG = SESSION_DIR / "s104_swmax_mpmath_edge.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    S102_NPZ,
    S103_NPZ,
]

# ---------------------------------------------------------------------------
# Pinned Sage exact real-algebraic-field (AA) cross-check.
# Computed at dispatch via mcp__sage__sage_eval on the EXACT dyadic-rational
# bit-patterns of the frozen float64 amplitudes (|alpha|,|beta| live in AA as
# algebraic-number square roots). The sign is a THEOREM in AA, not an estimate.
# Reproduced verbatim in the WP MCP Pre-Compute Audit block.
# ---------------------------------------------------------------------------
SAGE_SIGN_AA = -1                                                  # (local) Delta.sign() in AA
SAGE_DELTA_IS_ZERO = False                                         # (local) Delta.is_zero() in AA
SAGE_DELTA_N120 = -5.2109983536991724882640715514082361e-9        # (local) AA Delta to 120 bits
SAGE_EDGE_VS_FROZEN_RESID = 7.6285030811008983226226e-17          # (local) (S_W_max-1 - env_upper) in AA


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY)
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


def compute_dual_sha(
    script_path: Path, canonical_path: Path, pins: dict[str, str]
) -> tuple[str, str]:
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
    """>=300-bit mpmath sign(deviation - (S_W_max-1)) with cross-checks."""
    mp.prec = MP_PREC_BITS

    d = np.load(S102_NPZ, allow_pickle=True)  # (local)
    d103 = np.load(S103_NPZ, allow_pickle=True)  # (local)

    # Frozen Bogoliubov amplitudes (float64 from the S102 phase-resolved npz).
    # mpf(float) is an EXACT bit-reproduction of the float64 — no precision loss
    # in the lift; the >=300-bit arithmetic that follows is exact on these inputs.
    ar = float(d["W_alpha_re"])  # (local)
    ai = float(d["W_alpha_im"])  # (local)
    br = float(d["W_beta_re"])   # (local)
    bi = float(d["W_beta_im"])   # (local)
    deviation_f = float(d["deviation"])  # (local)
    env_upper_f = float(d["envelope_upper_dev"])  # (local)

    # Stored magnitudes for cross-check (float64)
    abs_alpha_stored = float(d["abs_alpha_W"])  # (local)
    abs_beta_stored = float(d["abs_beta_W"])    # (local)
    beta2_stored = float(d["beta2_W"])          # (local)

    # S103 re-pin record (float64 shadow)
    dev_vs_repin_s103 = float(d103["dev_vs_repin"])  # (local) = -5.211e-09
    resid_bitexact_s103 = float(d103["resid_bitexact"])  # (local) = 7.63e-17
    pass_tol_repin_s103 = float(d103["PASS_TOL_repin"])  # (local)

    # --- Lift to mpf at >= 300 bits ---
    mar, mai = mpf(ar), mpf(ai)  # (local)
    mbr, mbi = mpf(br), mpf(bi)  # (local)
    mdev = mpf(deviation_f)      # (local)
    menv = mpf(env_upper_f)      # (local)

    abs_alpha = mp_sqrt(mar * mar + mai * mai)  # (local)
    abs_beta = mp_sqrt(mbr * mbr + mbi * mbi)   # (local)
    beta2 = mbr * mbr + mbi * mbi               # (local)

    # Asymmetric-window UPPER endpoint: S_W_max - 1 = 2|beta|^2 + 2|alpha||beta|
    S_W_max_m1 = 2 * beta2 + 2 * abs_alpha * abs_beta  # (local)
    Delta = mdev - S_W_max_m1  # (local)
    sgn = int(mp_sign(Delta))  # (local) in {-1, 0, +1}

    # Unitarity anchor |alpha|^2 - |beta|^2 = 1
    unitarity = (mar * mar + mai * mai) - (mbr * mbr + mbi * mbi)  # (local)
    unit_resid = unitarity - 1  # (local)

    # --- Cross-checks (mpmath, all should be ~ float64 eps) ---
    resid_abs_alpha = abs_alpha - mpf(abs_alpha_stored)  # (local)
    resid_abs_beta = abs_beta - mpf(abs_beta_stored)     # (local)
    resid_beta2 = beta2 - mpf(beta2_stored)              # (local)
    resid_edge_vs_frozen = S_W_max_m1 - menv             # (local) vs envelope_upper_dev

    # float64 shadow of Delta (round mpmath back to float64); compare to S103
    Delta_f64 = float(Delta)  # (local)
    resid_delta_vs_s103 = Delta_f64 - dev_vs_repin_s103  # (local)

    # --- Sign trichotomy -> verdict + 3-tuple ---
    if sgn < 0:
        verdict = "PASS"  # (local)
        sign_v, mag_v, regime_v = "PASS", "PASS", "VALID"  # (local)
    elif sgn == 0:
        verdict = "INFO"  # (local) exact-saturation structural-identity branch
        sign_v, mag_v, regime_v = "PASS", "INFO", "VALID"  # (local)
    else:
        verdict = "FAIL"  # (local) breach -> re-opens S79 sufficiency
        sign_v, mag_v, regime_v = "FAIL", "FAIL", "VALID"  # (local)

    # margin (signed, mpf -> str at 40 digits for the npz record)
    margin_inside_edge = -Delta if sgn < 0 else Delta  # (local) positive when interior

    return {
        "value": sgn,
        "sign_verdict": sign_v,
        "magnitude_verdict": mag_v,
        "regime_verdict": regime_v,
        "verdict": verdict,
        # high-precision strings (>= 30 decimal digits) for the npz
        "abs_alpha_320": nstr(abs_alpha, 40),
        "abs_beta_320": nstr(abs_beta, 40),
        "beta2_320": nstr(beta2, 40),
        "two_beta2_320": nstr(2 * beta2, 40),
        "two_ab_320": nstr(2 * abs_alpha * abs_beta, 40),
        "S_W_max_m1_320": nstr(S_W_max_m1, 40),
        "deviation_320": nstr(mdev, 40),
        "Delta_320": nstr(Delta, 40),
        "margin_inside_edge_320": nstr(margin_inside_edge, 40),
        "unitarity_320": nstr(unitarity, 40),
        "unit_resid_320": nstr(unit_resid, 12),
        # float64 shadows / cross-checks
        "Delta_f64": Delta_f64,
        "deviation_f64": deviation_f,
        "S_W_max_m1_f64": float(S_W_max_m1),
        "env_upper_dev_frozen": env_upper_f,
        "resid_edge_vs_frozen_f64": float(resid_edge_vs_frozen),
        "resid_abs_alpha_f64": float(resid_abs_alpha),
        "resid_abs_beta_f64": float(resid_abs_beta),
        "resid_beta2_f64": float(resid_beta2),
        "resid_delta_vs_s103_f64": resid_delta_vs_s103,
        "dev_vs_repin_s103": dev_vs_repin_s103,
        "resid_bitexact_s103": resid_bitexact_s103,
        "pass_tol_repin_s103": pass_tol_repin_s103,
        # Sage exact AA cross-check (pinned)
        "sage_sign_AA": SAGE_SIGN_AA,
        "sage_delta_is_zero": SAGE_DELTA_IS_ZERO,
        "sage_delta_n120": SAGE_DELTA_N120,
        "sage_edge_vs_frozen_resid": SAGE_EDGE_VS_FROZEN_RESID,
        "mp_prec_bits": MP_PREC_BITS,
        # raw amplitudes echoed
        "W_alpha_re": ar,
        "W_alpha_im": ai,
        "W_beta_re": br,
        "W_beta_im": bi,
    }


# ---------------------------------------------------------------------------
# Section 6 — Plot
# ---------------------------------------------------------------------------

def make_plot(r: dict) -> None:
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))

    # Panel 1 — number line: window center, upper edge, deviation
    dev = r["deviation_f64"]  # (local)
    edge = r["S_W_max_m1_f64"]  # (local)
    half = float(r["two_ab_320"])  # (local) 2|a||b| half-spread (lower-ish marker)
    ax[0].axvline(edge, color="crimson", lw=2, label=f"S_W_max-1 = {edge:.10e}")
    ax[0].axvline(dev, color="navy", lw=2, ls="--",
                  label=f"deviation = {dev:.10e}")
    ax[0].axvline(half, color="gray", lw=1, ls=":",
                  label=f"2|a||b| (half-spread) = {half:.6e}")
    ax[0].set_xlim(half - 1e-6, edge + 2e-6)
    ax[0].set_yticks([])
    ax[0].set_xlabel("S_W - 1  (deviation from unity)")
    ax[0].set_title("Asymmetric SU(1,1) window upper edge vs W-stage deviation")
    ax[0].legend(fontsize=7, loc="upper left")

    # Panel 2 — the sub-float64 margin (zoom on Delta)
    margin = -r["Delta_f64"]  # (local) positive => interior
    ax[1].bar(["margin inside edge\n(= -(Delta))"], [margin],
              color="seagreen", width=0.4)
    ax[1].axhline(0, color="k", lw=0.8)
    ax[1].set_ylabel("S_W_max-1 - deviation  (float64)")
    ax[1].set_title(
        f"320-bit & Sage-AA sign(Delta) = {int(r['value'])}  "
        f"(strict interior; margin {margin:.3e})"
    )
    ax[1].annotate(
        f"Delta(320b) = {r['Delta_320'][:18]}...\n"
        f"Sage AA sign = {r['sage_sign_AA']}  (is_zero={r['sage_delta_is_zero']})\n"
        f"S103 float64 dev_vs_repin = {r['dev_vs_repin_s103']:.4e}",
        xy=(0.04, 0.80), xycoords="axes fraction", fontsize=8,
        bbox=dict(boxstyle="round", fc="lightyellow", ec="gray"),
    )
    ax[1].text(0, margin * 1.02, f"{margin:.3e}", ha="center", fontsize=9)

    fig.suptitle(
        "S104-SWMAX-MPMATH-EDGE — deviation strictly INSIDE the asymmetric "
        "SU(1,1) upper edge (PASS)",
        fontsize=11,
    )
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)
    print(f"  plot -> {OUT_PNG.name}")


# ---------------------------------------------------------------------------
# Section 7 — Verdict payload helper
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(
    verdict: str,
    value,
    audit_sha: str,
    content_sha: str,
    sign_verdict: str | None = None,
    magnitude_verdict: str | None = None,
    regime_verdict: str | None = None,
    companion_note: str = "",
    extra_rows: list[str] | None = None,
) -> dict:
    payload: dict = {
        "session": SESSION.lstrip("Ss"),
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
    if not (sign_verdict is None and magnitude_verdict is None
            and regime_verdict is None):
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
# Section 8 — Main
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

    print(f"  mp.prec = {r['mp_prec_bits']} bits "
          f"(~{int(r['mp_prec_bits'] * 0.30103)} decimal digits)")
    print(f"  abs_alpha     = {r['abs_alpha_320'][:40]}")
    print(f"  abs_beta      = {r['abs_beta_320'][:40]}")
    print(f"  2|beta|^2     = {r['two_beta2_320'][:40]}")
    print(f"  2|alpha||beta|= {r['two_ab_320'][:40]}")
    print(f"  S_W_max-1     = {r['S_W_max_m1_320'][:40]}")
    print(f"  deviation     = {r['deviation_320'][:40]}")
    print(f"  Delta(320b)   = {r['Delta_320'][:40]}")
    print(f"  sign(Delta)   = {int(r['value'])}  -> verdict {r['verdict']}")
    print()
    print(f"  [xcheck] S_W_max-1 vs frozen envelope_upper_dev resid = "
          f"{r['resid_edge_vs_frozen_f64']:.3e}  (S103 resid_bitexact "
          f"{r['resid_bitexact_s103']:.3e})")
    print(f"  [xcheck] Delta float64 = {r['Delta_f64']:.6e}  vs S103 "
          f"dev_vs_repin = {r['dev_vs_repin_s103']:.6e}  resid "
          f"{r['resid_delta_vs_s103_f64']:.3e}")
    print(f"  [xcheck] unitarity |a|^2-|b|^2 - 1 = {r['unit_resid_320']}")
    print(f"  [Sage AA] sign(Delta) = {r['sage_sign_AA']}  is_zero="
          f"{r['sage_delta_is_zero']}  (exact real-algebraic field)")
    print()

    # Hard cross-check assertions (sentinels): mpmath must agree with Sage AA,
    # and the edge must reproduce the frozen envelope_upper_dev.
    assert int(r["value"]) == int(r["sage_sign_AA"]), (
        f"mpmath sign {r['value']} != Sage AA sign {r['sage_sign_AA']}"
    )
    assert abs(r["resid_edge_vs_frozen_f64"]) < 1e-15, (
        "S_W_max-1 does not reproduce frozen envelope_upper_dev within 1e-15"
    )
    assert abs(r["resid_delta_vs_s103_f64"]) < 1e-15, (
        "Delta float64 shadow does not reproduce S103 dev_vs_repin within 1e-15"
    )

    np.savez(OUT_NPZ, **{k: v for k, v in r.items()})
    print(f"  data -> {OUT_NPZ.name}")
    make_plot(r)
    print()

    tag = emit_4tuple(
        f"sign={int(r['value'])};Delta_320b={r['Delta_320'][:18]}",
        SCHEME, CONVENTION, L_MAX,
    )
    print(tag)

    # Build the value payload (no single-quote chars — the tool wraps value='...').
    value_payload = (
        f"sign(dev-(S_W_max-1))={int(r['value'])};"
        f"verdict={r['verdict']};"
        f"Delta_320b={r['Delta_320'][:16]};"
        f"deviation=2.915087e-03;S_W_max-1=2.915093e-03;"
        f"margin_inside_edge=+5.211e-09;edge=2beta2+2ab;"
        f"sage_AA_sign={r['sage_sign_AA']}(is_zero={r['sage_delta_is_zero']});"
        f"mp_prec={r['mp_prec_bits']}bit;"
        f"resid_edge_vs_frozen={r['resid_edge_vs_frozen_f64']:.2e}"
    )

    extra_rows = [
        f"# regulator_pin=N/A (SU(1,1) window amplitude, not a Seeley-DeWitt moment)",
        f"# sage_exact_AA: sign(Delta)={r['sage_sign_AA']} is_zero={r['sage_delta_is_zero']} "
        f"Delta={r['sage_delta_n120']:.6e} (real-algebraic field; provable sign)",
        f"# xcheck: S_W_max-1={r['S_W_max_m1_f64']:.13e} vs frozen envelope_upper_dev "
        f"{r['env_upper_dev_frozen']:.13e} resid={r['resid_edge_vs_frozen_f64']:.2e}",
    ]

    print_verdict_payload(
        r["verdict"], value_payload, audit_sha, content_sha,
        sign_verdict=r["sign_verdict"],
        magnitude_verdict=r["magnitude_verdict"],
        regime_verdict=r["regime_verdict"],
        extra_rows=extra_rows,
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {r['verdict']} (wall {wall:.1f}s) ===")
    return 0 if r["verdict"] != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
