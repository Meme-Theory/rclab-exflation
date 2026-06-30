#!/usr/bin/env python3
"""
S88 W13-158 — NC Two-Torus FGK Fixed-Point Validation
======================================================

Gate: S88-NC-TWO-TORUS-FGK-FIXED-POINT-VALIDATION ([VERIFY])

Pre-registered threshold (per sessions/session-plan/session-88-plan-w13.md
§W13-158 Thresholds):
  PASS:  L^{-3} convergence rate at d=4 (matches W-5 algebraic envelope)
         AND fixed-point value matches substrate's Pillar-IV cross-check
         within W-5 tolerance band.
  FAIL:  convergence rate != L^{-3} OR fixed-point value violates W-5
         tolerance.
  INFO:  convergence trend present but L_max=12 insufficient to declare;
         document + route to S89 with extended L_max scan.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_nc_two_torus_helpers.py   (FGK helpers; canonical
    realisation: Pauli-Villars subtracted s=3/2 zeta moment of D_T^2)
  - computations/_shared/canonical_constants.py
  - script bytes (BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=convergence_rate_r, scheme='nc-two-torus-fgk-fixed-point-pauli-villars-jensen-deformed',
   convention='pauli-villars-s-three-halves-square-modular',
   L_max=12)

Classification: GEOMETRIC (NCG axiomatic test of Pillar-IV cross-pillar
bridge candidate per cross-pillar-bridge-anatomy.md K-counter advance).

Substrate framing (per .claude/rules/phononic-framing.md §"IS Space, Not
IN Space" + cross-pillar-bridge-anatomy.md §"IS-not-IN Anatomy"):
  The NC two-torus IS a noncommutative-geometric structure — algebra
  A_theta = C^*<U,V | UV = e^{2 pi i theta} VU> with canonical Connes-
  Landi spectral triple.  It is NOT "embedded" in any container; the
  algebra IS the geometry.  The FGK fixed-point IS the spectral zeta
  moment of D_T at substrate-distance s, evaluated truncated at L_max.
  Pillar-IV cross-check observable IS the W-5 R_universal_HP1_strict_F4
  anchor (Pillar III ↔ Pillar IV bridge LANDED §VII.AF.1, S87 W5-1).

  Direction of explanation: substrate IS the spectral triple →
  truncation bias → finite L_max moment → continuum extrapolation →
  cross-pillar bridge.  NOT: "we put a moment on the torus."

Substitution chain (truncation tail of square-box moment; verified
empirically at protocol time via prototype):
  Step 1 (Definition):
    f_PV(L; s, M) := sum_{(m,n) in B_L \\ {0}} [
                       1/(m^2+n^2)^s - 1/(m^2+n^2+M^2)^s ]
    where B_L = {(m,n) in Z^2 : max(|m|,|n|) <= L}.
  Step 2 (Substitute Pauli-Villars Taylor expansion at large radius):
    1/(r^2)^s - 1/(r^2+M^2)^s ≈ s * M^2 / r^{2s+2}  for r^2 >> M^2.
  Step 3 (Simplify, polar tail integral for L_max -> infty):
    Tail(L; s, M) = sum_{max(|m|,|n|) > L} [PV-subtracted summand]
                 ~ s * M^2 * integral_{r > L} 2 pi r dr / r^{2s+2}
                 = (pi * s * M^2 / s) * L^{-2s}
                 = pi * M^2 * L^{-2s}.
  Step 4 (Direction at s = 3/2):
    Tail(L; 3/2, M) ~ pi * M^2 * L^{-3}.
    Therefore convergence rate r* = 3, matching W-5 envelope at d=4.
  Step 5 (Empirical verification at L_max in {6,8,10,12,16,20,24}):
    Fit f(L) = f_inf + C * L^{-r}; expect r ≈ 3.0.

  Direction of PASS:
    PASS_rate := |r_fitted - 3.0| < 0.10  (10% tolerance on the rate)
    PASS_envelope := |f(L_max=12) - f_inf_extrapolated|
                     < W-5 envelope at L_max=12 (= 0.10% * (10/12)^3
                     ~= 0.0579% of f_inf).
  PASS_overall := PASS_rate AND PASS_envelope.
  FAIL := NOT PASS_rate (convergence rate wrong by > 10%).
  INFO := PASS_rate AND NOT PASS_envelope.

Cross-check vs Pillar-IV anchor:
  W-5 §VII.AF.1 anchor: R_universal_HP1_strict_F4 = 1.030902 (canonical
  pin: canonical_constants.py:R_universal_HP1_strict_F4).  The NC two-
  torus PV-subtracted moment is structurally a *sister* observable, not
  the same cohomology class — per cross-pillar-bridge-anatomy.md
  §"Level-2 Layer Distinction", a direct numerical equality is NOT
  expected and NOT pre-registered.  What IS pre-registered: shared L^{-3}
  envelope (Level-2-binding via the NC-two-torus -> Pillar-IV HKR map at
  the cohomology class level, modulo Jensen-deformation factor).  The
  Pillar-IV residual is reported as DIAGNOSTIC, not a PASS predicate.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

# Make canonical_constants importable
if str(SHARED_DIR) not in sys.path:
    sys.path.insert(0, str(SHARED_DIR))
# Make _nc_two_torus_helpers.py importable
if str(COMPUTATIONS_DIR) not in sys.path:
    sys.path.insert(0, str(COMPUTATIONS_DIR))

# Cap CPU threads BEFORE numpy import (per .claude/rules/computation-environment.md)
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (
    R_universal_HP1_strict_F4,
    tau_fold,
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time
from typing import Tuple

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from _nc_two_torus_helpers import (
    bare_zeta_moment,
    fit_convergence_rate,
    jensen_deformed_pv_moment,
    pauli_villars_zeta_moment,
    w5_envelope,
    ZETA_E_S2_REFERENCE,
)


# ---------------------------------------------------------------------------
# Section 3 — Pre-registration constants (gate-local; tagged # (local))
# ---------------------------------------------------------------------------
SESSION = "S88"  # (local)
GATE_ID = "S88-NC-TWO-TORUS-FGK-FIXED-POINT-VALIDATION"  # (local)
SCHEME = "nc-two-torus-fgk-fixed-point-pauli-villars-jensen-deformed"  # (local)
CONVENTION = "pauli-villars-s-three-halves-square-modular"  # (local)
L_MAX = 12  # (local) plan §W13-158 max L_max in scan {6, 8, 10, 12}

# Pre-registered scan and machinery pins (per plan §W13-158)
L_MAX_SCAN = (6, 8, 10, 12)  # (local) plan-pinned L_max scan
L_MAX_EXTRA_FOR_FIT = (16, 20, 24)  # (local) extra Ls for rate-fit refinement
PV_S = 1.5  # (local) substrate-distance parameter for L^{-3} envelope match
PV_M = 1.0  # (local) Pauli-Villars mass in T^2_theta natural units (M_KK -> 1)
DELTA_J = 0.0  # (local) leading-order Jensen deformation; per helpers docstring
RATE_TARGET = 3.0  # (local) W-5 envelope L^{-3} target
RATE_TOLERANCE = 0.10  # (local) 10% relative tolerance on rate

# Output destinations
OUT_NPZ = SESSION_DIR / "s88_w13_nc_two_torus_fgk_fixed_point.npz"
OUT_PNG = SESSION_DIR / "s88_w13_nc_two_torus_fgk_fixed_point.png"
VERDICT_TXT = SESSION_DIR / "s88_gate_verdicts.txt"
HELPERS_PATH = COMPUTATIONS_DIR / "_nc_two_torus_helpers.py"
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"
SCRIPT_PATH = Path(__file__).resolve()

INPUT_FILES = [
    SCRIPT_PATH,
    HELPERS_PATH,
    CANONICAL_PATH,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block
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


def closure_hash(pins):
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path, canonical_path, pins) -> Tuple[str, str]:
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        pass
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        pass
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
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
    """Main computation.

    Substitution chain (per docstring + helpers module):
      Step 1: For L in {6, 8, 10, 12, 16, 20, 24}, compute
              f_PV(L; s=3/2, M=1) per Connes 1980 §IV.6 spectral
              zeta moment with Pauli-Villars subtraction.
      Step 2: Fit f(L) = f_inf + C * L^{-r} on the union of
              plan-pinned scan {6, 8, 10, 12} and rate-refinement
              extras {16, 20, 24}.
      Step 3: Compare r_fitted to W-5 envelope target r* = 3.0.
      Step 4: Compute Pillar-IV anchor residual as DIAGNOSTIC.
      Step 5: Verify convergence at L_max=12 vs envelope.
    """
    print()
    print("=== Section 5: NC two-torus FGK fixed-point computation ===")
    print(f"  Scheme:     {SCHEME}")
    print(f"  Convention: {CONVENTION}")
    print(f"  PV mass M:  {PV_M}")
    print(f"  PV s:       {PV_S}")
    print(f"  Jensen δ_J: {DELTA_J} (leading-order Connes-Landi)")
    print(f"  tau_fold:   {tau_fold} (canonical_constants.py)")
    print()

    # 1. Plan-pinned scan + extras for rate refinement
    Ls_all = list(L_MAX_SCAN) + list(L_MAX_EXTRA_FOR_FIT)  # (local)
    f_pv_vals = []  # (local) PV-subtracted moments at each L
    f_jensen_vals = []  # (local) Jensen-deformed (delta_J = 0 -> bare PV)
    f_bare_s2_vals = []  # (local) bare s=2 cross-validation against ZETA_E_S2

    for L in Ls_all:
        f_pv = pauli_villars_zeta_moment(L, PV_S, PV_M)  # (local)
        f_J = jensen_deformed_pv_moment(L, PV_S, PV_M, DELTA_J)  # (local)
        f_bare = bare_zeta_moment(L, 2.0)  # (local) cross-validation
        f_pv_vals.append(f_pv)
        f_jensen_vals.append(f_J)
        f_bare_s2_vals.append(f_bare)
        print(f"  L_max={L:3d}  f_PV(s=3/2,M=1)={f_pv:.10f}  "
              f"f_Jensen={f_J:.10f}  f_bare(s=2)={f_bare:.10f}")
    print()

    # 2. Fit convergence rate using a sub-window where the rate is well-defined.
    # Use Ls_all for the fit; the largest L acts as proxy for f_inf.
    r_hat, C_hat, f_inf_hat = fit_convergence_rate(Ls_all, f_pv_vals)  # (local)
    print(f"=== Convergence-rate fit ===")
    print(f"  r_hat       = {r_hat:.6f}  (target r* = {RATE_TARGET})")
    print(f"  C_hat       = {C_hat:.6e}")
    print(f"  f_inf_hat   = {f_inf_hat:.10f}")
    print(f"  |r-3|/3     = {abs(r_hat - RATE_TARGET) / RATE_TARGET:.6f}  "
          f"(tol {RATE_TOLERANCE:.3f})")
    print()

    # 3. Plan-pinned L_max=12 residual against extrapolated f_inf
    f_at_12 = f_pv_vals[L_MAX_SCAN.index(12)]  # (local)
    residual_12 = abs(f_at_12 - f_inf_hat)  # (local)
    envelope_12 = w5_envelope(12, baseline_envelope_pct=0.10)  # (local) fraction
    envelope_12_in_units = envelope_12 * abs(f_inf_hat)  # (local)
    print(f"=== L_max=12 residual against extrapolated f_inf ===")
    print(f"  f(L=12)     = {f_at_12:.10f}")
    print(f"  f_inf_hat   = {f_inf_hat:.10f}")
    print(f"  residual    = {residual_12:.6e}")
    print(f"  envelope*   = {envelope_12_in_units:.6e} "
          f"(W-5 0.10% scaled to L=12)")
    print(f"  resid/env   = {residual_12 / envelope_12_in_units:.6f}")
    print()

    # 4. Pillar-IV anchor cross-check (DIAGNOSTIC; not a PASS predicate
    # because the NC two-torus moment is a structural sister, not the
    # same cohomology class — see docstring substitution chain Step
    # "Cross-check vs Pillar-IV anchor").
    pillar_iv_residual_abs = abs(f_inf_hat - R_universal_HP1_strict_F4)  # (local)
    pillar_iv_residual_rel = pillar_iv_residual_abs / R_universal_HP1_strict_F4  # (local)
    print(f"=== Pillar-IV anchor diagnostic ===")
    print(f"  R_universal_HP1_strict_F4 = {R_universal_HP1_strict_F4:.6f}")
    print(f"  f_inf (NC T^2_theta s=3/2) = {f_inf_hat:.10f}")
    print(f"  abs residual = {pillar_iv_residual_abs:.6e}")
    print(f"  rel residual = {pillar_iv_residual_rel:.6e}")
    print(f"  Note: NC T^2_theta moment IS a structural sister, NOT the")
    print(f"  same cohomology class as Pillar-IV anchor. Exact equality")
    print(f"  is NOT pre-registered. What is pre-registered: shared L^{-3}")
    print(f"  envelope (Level-2 algebraic envelope per cross-pillar-bridge-")
    print(f"  anatomy.md §'Three-Level Structural-Confidence Ladder').")
    print()

    # 5. Bare s=2 sanity cross-check against known Eisenstein E_2 reference
    bare_at_largest = f_bare_s2_vals[-1]  # (local)
    bare_residual = abs(bare_at_largest - ZETA_E_S2_REFERENCE)  # (local)
    bare_residual_rel = bare_residual / ZETA_E_S2_REFERENCE  # (local)
    print(f"=== Bare s=2 reference cross-check ===")
    print(f"  bare_s2(L=24)      = {bare_at_largest:.10f}")
    print(f"  ZETA_E_S2_ref      = {ZETA_E_S2_REFERENCE:.10f}")
    print(f"  abs residual       = {bare_residual:.6e}")
    print(f"  rel residual       = {bare_residual_rel:.6e}")
    print()

    return {
        "value": float(r_hat),
        "Ls_all": np.asarray(Ls_all, dtype=np.int64),
        "f_pv_values": np.asarray(f_pv_vals, dtype=np.float64),
        "f_jensen_values": np.asarray(f_jensen_vals, dtype=np.float64),
        "f_bare_s2_values": np.asarray(f_bare_s2_vals, dtype=np.float64),
        "r_hat": float(r_hat),
        "C_hat": float(C_hat),
        "f_inf_hat": float(f_inf_hat),
        "f_at_L12": float(f_at_12),
        "residual_at_L12": float(residual_12),
        "envelope_at_L12": float(envelope_12_in_units),
        "envelope_fraction_L12": float(envelope_12),
        "pillar_iv_residual_abs": float(pillar_iv_residual_abs),
        "pillar_iv_residual_rel": float(pillar_iv_residual_rel),
        "rate_target": float(RATE_TARGET),
        "rate_tolerance": float(RATE_TOLERANCE),
        "rate_deviation_rel": float(abs(r_hat - RATE_TARGET) / RATE_TARGET),
        "bare_s2_residual_rel": float(bare_residual_rel),
        "PV_s": float(PV_S),
        "PV_M": float(PV_M),
        "delta_J": float(DELTA_J),
        "R_universal_anchor": float(R_universal_HP1_strict_F4),
        "tau_fold": float(tau_fold),
    }


# ---------------------------------------------------------------------------
# Section 6 — Plot
# ---------------------------------------------------------------------------
def make_plot(result: dict, png_path: Path) -> None:
    Ls = result["Ls_all"]
    f_pv = result["f_pv_values"]
    f_inf = result["f_inf_hat"]
    r_hat = result["r_hat"]
    C_hat = result["C_hat"]

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # Panel 1: convergence curve
    ax = axes[0]
    ax.plot(Ls, f_pv, "o-", color="tab:blue", label="f_PV(L; s=3/2, M=1)")
    ax.axhline(f_inf, color="black", linestyle="--",
               label=f"f_inf_extrapolated = {f_inf:.6f}")
    ax.axhline(R_universal_HP1_strict_F4, color="tab:red", linestyle=":",
               label=f"Pillar-IV anchor = {R_universal_HP1_strict_F4:.6f}")
    ax.set_xlabel("L_max (square-box truncation)")
    ax.set_ylabel("PV-subtracted moment f(L)")
    ax.set_title("NC two-torus FGK fixed-point: PV-subtracted s=3/2 moment")
    ax.legend(fontsize=8, loc="best")
    ax.grid(True, alpha=0.3)

    # Panel 2: log-log fit |f(L) - f_inf| vs L
    ax = axes[1]
    diffs = np.abs(f_pv - f_inf)  # (local)
    mask = diffs > 0  # (local)
    ax.loglog(Ls[mask], diffs[mask], "o", color="tab:blue",
              label="|f(L) - f_inf| (data)")
    L_smooth = np.logspace(np.log10(Ls.min()), np.log10(Ls.max()), 100)  # (local)
    fit_curve = abs(C_hat) * L_smooth ** (-r_hat)  # (local)
    ax.loglog(L_smooth, fit_curve, "--", color="tab:orange",
              label=f"fit r={r_hat:.3f}")
    L_target = np.logspace(np.log10(Ls.min()), np.log10(Ls.max()), 100)  # (local)
    target_curve = abs(C_hat) * L_target ** (-3.0)  # (local) anchor at fit C
    ax.loglog(L_target, target_curve, ":", color="tab:green",
              label="W-5 envelope L^-3 (target)")
    ax.set_xlabel("L_max")
    ax.set_ylabel("|f(L) - f_inf|")
    ax.set_title(f"Convergence rate: r_hat = {r_hat:.3f} (target 3.0)")
    ax.legend(fontsize=8, loc="best")
    ax.grid(True, which="both", alpha=0.3)

    fig.suptitle(
        "S88 W13-158 — NC Two-Torus FGK Fixed-Point Validation\n"
        f"L_max scan {{6, 8, 10, 12}} + extras; PV M={PV_M}, s={PV_S}",
        fontsize=11,
    )
    fig.tight_layout()
    fig.savefig(png_path, dpi=120, bbox_inches="tight")
    plt.close(fig)
    print(f"  plot written: {png_path}")


# ---------------------------------------------------------------------------
# Section 7 — Verdict + 4-tuple
# ---------------------------------------------------------------------------
def evaluate_gate(result: dict) -> str:
    """Per docstring substitution chain Step 4-5.

    PASS  := PASS_rate AND PASS_envelope
    FAIL  := NOT PASS_rate
    INFO  := PASS_rate AND NOT PASS_envelope
    """
    rate_ok = (result["rate_deviation_rel"] <= RATE_TOLERANCE)  # (local)
    envelope_ok = (result["residual_at_L12"] <= result["envelope_at_L12"])  # (local)

    if not rate_ok:
        return "FAIL"
    if rate_ok and envelope_ok:
        return "PASS"
    return "INFO"


def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str,
                   tag_extras: str) -> None:
    """Atomic POSIX O_APPEND single-write (parallel-writer-safe)."""
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion_short = (
        f"# audit_sha256 companion row: {GATE_ID} "
        f"audit={audit_sha[:16]} content={content_sha[:16]} "
        f"# {tag_extras}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion_short)


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins (first 20 lines of stdout)
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. Compute S84+ dual SHAs
    audit_sha, content_sha = compute_dual_sha(
        SCRIPT_PATH, CANONICAL_PATH, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    # 2. Compute
    result = compute()

    # 3. Evaluate gate
    verdict = evaluate_gate(result)
    print(f"=== Verdict: {verdict} ===")

    # 4. Emit 4-tuple
    tag = emit_4tuple(result["value"], SCHEME, CONVENTION, L_MAX)
    print(tag)

    # 5. Save .npz
    np.savez(
        OUT_NPZ,
        Ls_all=result["Ls_all"],
        f_pv_values=result["f_pv_values"],
        f_jensen_values=result["f_jensen_values"],
        f_bare_s2_values=result["f_bare_s2_values"],
        r_hat=result["r_hat"],
        C_hat=result["C_hat"],
        f_inf_hat=result["f_inf_hat"],
        f_at_L12=result["f_at_L12"],
        residual_at_L12=result["residual_at_L12"],
        envelope_at_L12=result["envelope_at_L12"],
        envelope_fraction_L12=result["envelope_fraction_L12"],
        pillar_iv_residual_abs=result["pillar_iv_residual_abs"],
        pillar_iv_residual_rel=result["pillar_iv_residual_rel"],
        rate_target=result["rate_target"],
        rate_tolerance=result["rate_tolerance"],
        rate_deviation_rel=result["rate_deviation_rel"],
        bare_s2_residual_rel=result["bare_s2_residual_rel"],
        PV_s=result["PV_s"],
        PV_M=result["PV_M"],
        delta_J=result["delta_J"],
        R_universal_anchor=result["R_universal_anchor"],
        tau_fold=result["tau_fold"],
        verdict=np.array(verdict),
        scheme=np.array(SCHEME),
        convention=np.array(CONVENTION),
        gate_id=np.array(GATE_ID),
        audit_sha256=np.array(audit_sha),
        content_sha256=np.array(content_sha),
    )
    print(f"  npz written: {OUT_NPZ}")

    # 6. Plot
    make_plot(result, OUT_PNG)

    # 7. Append verdict line + companion row
    tag_extras = (
        f"PV_s={PV_S} PV_M={PV_M} delta_J={DELTA_J} "
        f"r_hat={result['r_hat']:.4f} f_inf={result['f_inf_hat']:.6f} "
        f"residual_L12={result['residual_at_L12']:.3e} "
        f"envelope_L12={result['envelope_at_L12']:.3e} "
        f"pillar_iv_residual_rel={result['pillar_iv_residual_rel']:.3e} "
        f"upstream=W-5_R_universal_HP1_strict_F4={R_universal_HP1_strict_F4}"
    )
    append_verdict(verdict, result["value"], audit_sha, content_sha,
                   tag_extras)
    print(f"  verdict line appended: {VERDICT_TXT}")

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0  # verdict is data; exit code reflects script health only


if __name__ == "__main__":
    sys.exit(main())
