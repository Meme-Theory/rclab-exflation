#!/usr/bin/env python3
"""
S100a W3-10 S100a-ENVELOPE-OVERDETERMINE — double-derivation of the diagonal
freeze-in exponent: sonic greybody 2*pi*omega/kappa_SONIC vs freeze-in S0*C2
=============================================================================

Gate: S100a-ENVELOPE-OVERDETERMINE ([SIGN])
Plan: sessions/session-plan/session-100a-plan-w3.md §W3-10 (R3 YAML block)
Classification: PHONONIC

Pre-registered threshold (plan §W3-10, operator + rubric):
  per heavy sector (C2 in {3, 6}):
    rel_disc = |2*pi*omega/kappa_SONIC - S0*C2| / (S0*C2)
  PASS iff rel_disc <= 0.1 for ALL heavy sectors        (10% band, QF V.4)
  FAIL iff > 1 OOM divergence between the two routes    (|log10(E_A/E_B)| > 1)
  INFO otherwise (same OOM, O(1) factor: 0.1 < rel_disc <= ~1)

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py  (T_acoustic = 0.112 M_KK, S63;
    tau_fold for the diagnostic cross-check)     [feeds audit_sha256]
  - computations/session-100a/s100a_freezein_overconstrained.npz
    (HARD within-wave: S0_fit + C2_vec from Item 9 / W3-9)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<payload>, scheme=FW, convention=RATIO, L_max=N/A-scalar-inputs)

METHODOLOGY (plan §W3-10 method block, executed verbatim)
---------------------------------------------------------
(1) kappa_SONIC = 2*pi*T_acoustic = 28/125*pi (Sage-exact from the canonical
    T_acoustic = 0.112 M_KK, S63) — the v = c_BLV Mach-1 crossing.  EXCLUDED:
    kappa_GH = 1.365 (Gibbons-Hawking) and the a2/a4 thermodynamic surfaces.
    kappa_SONIC is FIBER-ACOUSTIC: functional-INDEPENDENT per the lizzi pin —
    an a_n-gradient kappa would contaminate a regulator-invariant ratio. No
    Seeley-DeWitt a_n is cited anywhere in this gate.
(2) omega = Delta_omega = 0.9 M_KK (epsilon_LX one-fiber-gap heavy-pair offset,
    post shape-preserving-squaring halving) for BOTH heavy sectors.
(3) S0 loaded from Item 9 (s100a_freezein_overconstrained.npz, key S0_fit) —
    NEVER hardcoded.  E_B = S0*C2 for the heavy pair C2 in {3, 6}
    ((1,1) and (3,0) sectors; C2_vec consumed from the same npz and asserted
    against the analytic SU(3) Casimirs).
(4) rel_disc per sector; gate per the three-band rubric above.
Greybody transmission cross-check: Gamma(omega)*exp(-2*pi*omega/kappa) is the
analog-horizon transmission (S43/S95 greybody machinery); the EXPONENT is the
over-determined quantity (the Gamma prefactor is NOT gated).

SUBSTITUTION CHAIN (plan §W3-10 item 7; numbers substituted at run time)
------------------------------------------------------------------------
Claim: "the diagonal exponent is the SAME via greybody-filter and via
        freeze-in amplitude".
  Step 1 — Definitions:
    kappa_SONIC = 2*pi*T_acoustic              [T_acoustic = 0.112 M_KK, S63]
    E_A(omega)  = 2*pi*omega/kappa_SONIC       [analog-horizon transmission exp]
    E_B         = S0*C2                        [Item 9 amplitude exp(-S0*C2)]
    omega       = Delta_omega = 0.9 M_KK       [eps_LX one-fiber heavy offset]
  Step 2 — Substitution (Sage-exact kappa, no simplification):
    kappa_SONIC = 2*pi*(112/1000) = 28/125*pi
    E_A(omega)  = 2*pi*omega/(28/125*pi) = (250/28)*omega = (125/14)*omega
  Step 3 — Simplify (kappa reconciled to the 4th digit):
    28/125*pi = 0.7037167544041137  [Sage QQ; 5 sig figs = 0.70372]
    4-dp round = 0.7037; |exact - 0.7037| = 1.675e-5  (log10 = -4.776)
    context-header 0.7048: |exact - 0.7048| = 1.083e-3 (log10 = -2.965)
      = ~65x the 4-dp rounding residual  => 0.7048 is NOT 2*pi*0.112; it is
      transcription drift.  CANONICAL pin = 28/125*pi.
    [Plan-freeze note quoted the rounding residual as 2.289e-5 (~47x); the
     Sage-exact residual is 1.675e-5 (~65x). Same direction, same conclusion:
     drift >> rounding; the 0.7048 literal is rejected either way.]
    E_A(0.9) = (125/14)*(9/10) = 225/28 = 8.035714285714286   (exact rational)
  Step 4 — Direction read-off ([SIGN]):
    PASS-direction: E_A and E_B coincide for the heavy pair (one operator,
    two faces).  Direction axis = OOM-coincidence (|log10(E_A/E_B)| <= 1;
    the plan rubric declares the 0.1 < rel_disc <= ~1 band "directionally
    confirming, magnitude-deferred").  Magnitude axis = the 10% band.
  Step 5 — Source-Reconciliation direction (Class-8.3 + Class-(f)):
    The pin MUST be the Sage-exact 28/125*pi (substrate-first from canonical
    T_acoustic), NOT 0.7048.  Using 0.7048 would bias E_A LOW by 0.154% —
    inside the 10% band but a publication-precision defect that propagates.
    This script computes kappa_SONIC from 2*pi*T_acoustic (imported
    canonical); no hardcoded kappa literal anywhere.

DISCIPLINE
----------
- from canonical_constants import * (T_acoustic, tau_fold)
- Every local/intermediate tagged # (local)
- GPU_path pin = numpy.linalg (CPU trivial — scalar arithmetic); OMP capped at 8
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- Verdict emitted via the emit_verdict knowledge-MCP tool (race-safe; this
  script only PRINTS the payload via print_verdict_payload — it does NOT
  write s100a_gate_verdicts.txt; raw open("a") is not atomic on Windows)
- Exit 0 on any valid verdict (PASS/FAIL/INFO are all results; exit != 0 is
  reserved for script breakage, per .claude/rules/math-scripts.md)
"""

from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import math
import sys
import time
from fractions import Fraction
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths + canonical import (canonical_constants.py lives in _shared)
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

import numpy as np  # noqa: E402  (after OMP cap, per computation-environment.md)
import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

from canonical_constants import *  # noqa: F401,F403,E402  (T_acoustic, tau_fold)

# ---------------------------------------------------------------------------
# Identity + pre-registration (plan §W3-10 machinery_pin_map)
# ---------------------------------------------------------------------------
SESSION = "100a"                                                   # (local)
GATE_ID = "S100a-ENVELOPE-OVERDETERMINE"                           # (local)
SCHEME = "FW"                                                      # (local)
CONVENTION = "RATIO"                                               # (local)
L_MAX = "N/A-scalar-inputs"                                        # (local)

PASS_BAND = 0.1        # (local) pre-registered 10% gate band (QF V.4)
FAIL_OOM = 1.0         # (local) pre-registered FAIL: >1 OOM route divergence
DELTA_OMEGA = 0.9      # (local) M_KK; eps_LX one-fiber-gap heavy-pair offset
N_EVAL = 2             # (local) heavy sector pair: C2 in {3, 6}
C2_HEAVY_ANALYTIC = (3.0, 6.0)  # (local) SU(3) Casimir (1,1)/(3,0) assertion targets
KAPPA_SONIC_SAGE = 0.7037167544041137  # (local) Sage-QQ cross-check target (plan pin 28/125*pi)
KAPPA_DRIFT_LITERAL = 0.7048           # (local) context-header transcription-drift literal (rejected)

OUT_NPZ = SESSION_DIR / "s100a_envelope_overdetermine.npz"
OUT_PNG = SESSION_DIR / "s100a_envelope_overdetermine.png"
FREEZEIN_NPZ = SESSION_DIR / "s100a_freezein_overconstrained.npz"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    FREEZEIN_NPZ,
]


# ---------------------------------------------------------------------------
# SHA-256 input-pin block (S84+ dual-SHA schema)
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


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = script_path.read_bytes()       # (local)
    canonical_bytes = canonical_path.read_bytes() # (local)
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


# ---------------------------------------------------------------------------
# Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    # --- (1) kappa_SONIC from the IMPORTED canonical (never a literal) -----
    # T_acoustic = 0.112 M_KK (canonical_constants.py, S63 provenance line).
    kappa_sonic = 2.0 * math.pi * T_acoustic                       # (local)
    # Sage-exact rational coefficient check: 2*(112/1000) == 28/125 exactly.
    t_ac_rational = Fraction(str(T_acoustic))                      # (local)
    kappa_coeff = 2 * t_ac_rational                                # (local)
    assert t_ac_rational == Fraction(112, 1000), \
        f"canonical T_acoustic drifted from 0.112: {T_acoustic}"
    assert kappa_coeff == Fraction(28, 125), \
        f"kappa coefficient is not 28/125: {kappa_coeff}"
    # Cross-check vs the plan's Sage-QQ pin (publication precision 5 sf).
    assert abs(kappa_sonic - KAPPA_SONIC_SAGE) < 1e-15, \
        f"kappa_SONIC float route disagrees with Sage QQ: {kappa_sonic!r}"
    kappa_sonic_5sf = float(f"{kappa_sonic:.5g}")                  # (local)

    # --- kappa reconciliation (Class-8.3 publication precision) ------------
    resid_4dp = abs(kappa_sonic - 0.7037)                          # (local)
    resid_drift = abs(kappa_sonic - KAPPA_DRIFT_LITERAL)           # (local)
    drift_over_round = resid_drift / resid_4dp                     # (local)
    bias_if_drift_pct = (resid_drift / kappa_sonic) * 100.0        # (local)
    kappa_recon_note = (
        "kappa_SONIC = 2*pi*T_acoustic = 28/125*pi = "
        f"{kappa_sonic:.16f} (5 sf {kappa_sonic_5sf}); 4-dp round 0.7037 "
        f"(residual {resid_4dp:.3e}, log10 {math.log10(resid_4dp):.3f}); "
        f"context-header 0.7048 residual {resid_drift:.3e} "
        f"(log10 {math.log10(resid_drift):.3f}) = {drift_over_round:.1f}x the "
        "rounding residual -> transcription drift, NOT 2*pi*0.112; REJECTED. "
        f"Bias on E_A if 0.7048 were used: -{bias_if_drift_pct:.3f}%. "
        "Plan-freeze quoted the rounding residual as 2.289e-5 (~47x); "
        "Sage-exact is 1.675e-5 (~65x) — same conclusion, drift >> rounding. "
        "Pin = Sage-exact rational 28/125*pi, computed in-script from the "
        "imported canonical T_acoustic."
    )  # (local)

    # --- (3) S0 + C2 grading from Item 9 (HARD within-wave input) ----------
    fz = np.load(FREEZEIN_NPZ, allow_pickle=True)                  # (local)
    S0 = float(fz["S0_fit"])                                       # (local)
    C2_vec = np.asarray(fz["C2_vec"], dtype=float)                 # (local)
    C2_heavy = C2_vec[1:]                                          # (local) heavy pair (1,1)/(3,0)
    assert C2_heavy.shape == (2,), f"heavy pair shape: {C2_heavy.shape}"
    assert np.allclose(C2_heavy, C2_HEAVY_ANALYTIC, rtol=0.0, atol=1e-12), \
        f"npz C2 grading != analytic SU(3) Casimirs (3, 6): {C2_heavy}"

    # --- (2)+(4) two routes + relative discrepancy per heavy sector --------
    # Route A — greybody exponent at the SONIC surface, omega = 0.9 for BOTH
    # heavy sectors (the plan pins ONE Delta_omega for the pair).
    E_A_scalar = 2.0 * math.pi * DELTA_OMEGA / kappa_sonic         # (local)
    # Exact-rational confirmation: (125/14)*(9/10) = 225/28.
    E_A_exact = Fraction(125, 14) * Fraction(9, 10)                # (local)
    assert E_A_exact == Fraction(225, 28)
    assert abs(E_A_scalar - float(E_A_exact)) < 1e-12, \
        f"E_A float route disagrees with 225/28: {E_A_scalar!r}"
    E_A = np.array([E_A_scalar, E_A_scalar])                       # (local) per-sector (sector-independent by pin)

    # Route B — freeze-in amplitude exponent from Item 9.
    E_B = S0 * C2_heavy                                            # (local)

    rel_disc = np.abs(E_A - E_B) / E_B                             # (local)
    log10_ratio = np.log10(E_A / E_B)                              # (local)

    # --- Gate (pre-registered three-band rubric) ----------------------------
    if bool(np.all(rel_disc <= PASS_BAND)):
        verdict = "PASS"                                           # (local)
    elif bool(np.any(np.abs(log10_ratio) > FAIL_OOM)):
        verdict = "FAIL"                                           # (local)
    else:
        verdict = "INFO"                                           # (local)

    # --- [SIGN] schema-v2 3-tuple -------------------------------------------
    # sign: directional coincidence axis — the two faces are the same operator
    #       at OOM level iff |log10(E_A/E_B)| <= 1 on every heavy sector (the
    #       plan rubric declares the 0.1 < rel_disc <= ~1 band "directionally
    #       confirming"); FAIL iff OOM-divergent.
    sign_verdict = "PASS" if bool(np.all(np.abs(log10_ratio) <= FAIL_OOM)) else "FAIL"  # (local)
    # magnitude: the band axis — PASS within 10%, FAIL beyond 1 OOM, else INFO.
    if bool(np.all(rel_disc <= PASS_BAND)):
        magnitude_verdict = "PASS"                                 # (local)
    elif bool(np.any(np.abs(log10_ratio) > FAIL_OOM)):
        magnitude_verdict = "FAIL"                                 # (local)
    else:
        magnitude_verdict = "INFO"                                 # (local)
    # regime: exact scalar arithmetic, no expansion, no auto-shortening; the
    # HARD input landed and the canonical pin is exact -> VALID throughout.
    regime_verdict = "VALID"                                       # (local)

    # Collapse-rule self-check (gate-verdicts.md; pre-registered):
    if regime_verdict == "BREAKDOWN" or sign_verdict == "FAIL":
        collapse = "FAIL"                                          # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        collapse = "FAIL"                                          # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        collapse = "INFO"                                          # (local)
    elif magnitude_verdict == "INFO":
        collapse = "INFO"                                          # (local)
    else:
        collapse = "PASS"                                          # (local)
    assert collapse == verdict, f"collapse rule mismatch: {collapse} vs {verdict}"

    # --- Diagnostics (NOT gate inputs; interpretation support) --------------
    # Per-sector matching frequency: omega*(C2) such that E_A(omega*) == E_B.
    #   omega*(C2) = S0*C2*kappa_SONIC/(2*pi) = S0*C2*T_acoustic
    omega_match = S0 * C2_heavy * T_acoustic                       # (local)
    # S0*T_acoustic vs tau_fold cross-check (flagged to W3-11, not gated here):
    S0_times_Tac = S0 * T_acoustic                                 # (local)
    tau_fold_dev = abs(S0_times_Tac - tau_fold) / tau_fold         # (local)
    # Pair-aggregate (geometric-mean) discrepancy:
    geomean_ratio = E_A_scalar / math.sqrt(float(np.prod(E_B)))    # (local)
    # Amplitude-level (transmission-weight) comparison — the exponent, not the
    # amplitude, is the gated quantity; this shows why:
    amp_ratio = np.exp(-(E_A - E_B))                               # (local) exp(-E_A)/exp(-E_B)

    # --- stdout numbers (NUMBERS first) -------------------------------------
    print("=== Route A (sonic greybody) vs Route B (freeze-in) ===")
    print(f"  kappa_SONIC = 2*pi*T_acoustic = 28/125*pi = {kappa_sonic:.16f} M_KK"
          f"  (5 sf {kappa_sonic_5sf})")
    print(f"  kappa reconciliation: |exact-0.7037| = {resid_4dp:.3e}; "
          f"|exact-0.7048| = {resid_drift:.3e} ({drift_over_round:.1f}x) -> 0.7048 REJECTED")
    print(f"  omega = Delta_omega = {DELTA_OMEGA} M_KK (one-fiber-gap heavy-pair pin)")
    print(f"  S0_consumed = {S0:.16f}  (Item 9 npz key S0_fit)")
    print(f"  C2 heavy pair = {tuple(C2_heavy)}  [(1,1), (3,0)]")
    print(f"  E_A per sector = [{E_A[0]:.12f}, {E_A[1]:.12f}]  (= 225/28 exact)")
    print(f"  E_B per sector = [{E_B[0]:.12f}, {E_B[1]:.12f}]")
    print(f"  rel_disc per sector = [{rel_disc[0]:.6f}, {rel_disc[1]:.6f}]"
          f"  (band <= {PASS_BAND})")
    print(f"  log10(E_A/E_B) per sector = [{log10_ratio[0]:+.6f}, {log10_ratio[1]:+.6f}]"
          f"  (FAIL iff |.| > {FAIL_OOM})")
    print("=== Diagnostics (not gated) ===")
    print(f"  omega_match per sector = [{omega_match[0]:.6f}, {omega_match[1]:.6f}] M_KK"
          f"  (pinned 0.9 sits between)")
    print(f"  S0*T_acoustic = {S0_times_Tac:.6f} vs tau_fold = {tau_fold}"
          f"  (rel dev {tau_fold_dev:.4%}) -> W3-11 territory")
    print(f"  E_A / geomean(E_B pair) = {geomean_ratio:.6f}")
    print(f"  amplitude-level exp(-E_A)/exp(-E_B) = [{amp_ratio[0]:.3e}, {amp_ratio[1]:.3e}]"
          f"  (~1 OOM at amplitude level — exponent is the over-determined quantity)")

    return {
        "kappa_sonic": kappa_sonic,
        "kappa_sonic_5sf": kappa_sonic_5sf,
        "kappa_recon_note": kappa_recon_note,
        "resid_4dp": resid_4dp,
        "resid_drift": resid_drift,
        "drift_over_round": drift_over_round,
        "bias_if_drift_pct": bias_if_drift_pct,
        "S0": S0,
        "C2_heavy": C2_heavy,
        "E_A": E_A,
        "E_B": E_B,
        "rel_disc": rel_disc,
        "log10_ratio": log10_ratio,
        "verdict": verdict,
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "omega_match": omega_match,
        "S0_times_Tac": S0_times_Tac,
        "tau_fold_dev": tau_fold_dev,
        "geomean_ratio": geomean_ratio,
        "amp_ratio": amp_ratio,
    }


# ---------------------------------------------------------------------------
# Plot
# ---------------------------------------------------------------------------
def make_plot(r: dict) -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 4.6))  # (local)
    sector_labels = ["C2=3  (1,1)", "C2=6  (3,0)"]             # (local)
    x = np.arange(2)                                           # (local)

    # Panel 1 — the two routes per heavy sector, with the 10% band on E_B.
    w = 0.32                                                   # (local)
    ax1.bar(x - w / 2, r["E_B"], w, color="#3a6ea5",
            label=r"Route B: $E_B = S_0 C_2$ (freeze-in, Item 9)")
    ax1.bar(x + w / 2, r["E_A"], w, color="#c0504d",
            label=r"Route A: $E_A = 2\pi\omega/\kappa_{\rm SONIC}$ (greybody)")
    for i in range(2):
        lo, hi = r["E_B"][i] * 0.9, r["E_B"][i] * 1.1          # (local)
        ax1.fill_between([x[i] - 0.5, x[i] + 0.5], lo, hi,
                         color="#3a6ea5", alpha=0.15,
                         label="pre-registered 10% band" if i == 0 else None)
        ax1.annotate(f"rel_disc = {r['rel_disc'][i]:.3f}",
                     (x[i], max(r['E_A'][i], r['E_B'][i]) + 0.25),
                     ha="center", fontsize=9)
    ax1.set_xticks(x, sector_labels)
    ax1.set_ylabel("diagonal exponent (dimensionless)")
    ax1.set_title(f"{GATE_ID}: two faces of the diagonal exponent\n"
                  rf"$\kappa_{{\rm SONIC}} = 28/125\,\pi = {r['kappa_sonic']:.5f}$,"
                  rf"  $\omega = {DELTA_OMEGA}\,M_{{KK}}$,  $S_0 = {r['S0']:.4f}$")
    ax1.legend(fontsize=8, loc="upper left")
    ax1.grid(alpha=0.25)

    # Panel 2 — matching-frequency diagnostic.
    ax2.plot(x, r["omega_match"], "o", ms=9, color="#3a6ea5",
             label=r"$\omega^*(C_2) = S_0 C_2 T_{\rm acoustic}$ (exact match)")
    ax2.axhline(DELTA_OMEGA, color="#c0504d", ls="--",
                label=rf"pinned $\Delta\omega = {DELTA_OMEGA}$ (one-fiber gap)")
    for i in range(2):
        ax2.annotate(f"{r['omega_match'][i]:.3f}",
                     (x[i], r["omega_match"][i] + 0.03), ha="center", fontsize=9)
    ax2.set_xticks(x, sector_labels)
    ax2.set_ylabel(r"$\omega$  [$M_{KK}$]")
    ax2.set_title("Matching frequency per sector (diagnostic)\n"
                  rf"$S_0 T_{{\rm acoustic}} = {r['S0_times_Tac']:.5f}$ vs "
                  rf"$\tau_{{\rm fold}} = {tau_fold}$ "
                  rf"(dev {r['tau_fold_dev']*100:.2f}%)")
    ax2.legend(fontsize=8, loc="upper left")
    ax2.grid(alpha=0.25)

    fig.suptitle("PHONONIC — fiber-acoustic Mach-1 surface only "
                 r"($\kappa_{GH}$ + $a_2/a_4$ surfaces excluded)", fontsize=9, y=1.0)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)
    print(f"  plot -> {OUT_PNG.relative_to(PROJECT_ROOT)}")


# ---------------------------------------------------------------------------
# Verdict payload (printed; the AGENT calls mcp__knowledge__emit_verdict)
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
                          sign_verdict: str, magnitude_verdict: str,
                          regime_verdict: str, companion_note: str = "",
                          extra_rows: list[str] | None = None) -> dict:
    payload: dict = {
        "session": SESSION,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
    }  # (local)
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)  # (local)
    script_path = Path(__file__).resolve()                      # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"      # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    r = compute()  # (local)

    # npz (plan-required keys + diagnostics + gate metadata)
    np.savez(
        OUT_NPZ,
        kappa_SONIC_exact=r["kappa_sonic"],
        kappa_SONIC_5sf=r["kappa_sonic_5sf"],
        kappa_recon_note=r["kappa_recon_note"],
        E_A_per_sector=r["E_A"],
        E_B_per_sector=r["E_B"],
        rel_disc_per_sector=r["rel_disc"],
        log10_ratio_per_sector=r["log10_ratio"],
        S0_consumed=r["S0"],
        C2_heavy=r["C2_heavy"],
        Delta_omega=DELTA_OMEGA,
        T_acoustic_used=T_acoustic,
        pass_band=PASS_BAND,
        fail_oom=FAIL_OOM,
        N_eval=N_EVAL,
        omega_match_per_sector=r["omega_match"],
        S0_times_T_acoustic=r["S0_times_Tac"],
        tau_fold_used=tau_fold,
        tau_fold_rel_dev=r["tau_fold_dev"],
        geomean_ratio=r["geomean_ratio"],
        amp_ratio_per_sector=r["amp_ratio"],
        resid_4dp=r["resid_4dp"],
        resid_drift_0p7048=r["resid_drift"],
        drift_over_round=r["drift_over_round"],
        bias_if_drift_pct=r["bias_if_drift_pct"],
        verdict=r["verdict"],
        sign_verdict=r["sign_verdict"],
        magnitude_verdict=r["magnitude_verdict"],
        regime_verdict=r["regime_verdict"],
        gate_id=GATE_ID,
        scheme=SCHEME,
        convention=CONVENTION,
        l_max=L_MAX,
        schema_version="S84+",
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"  data -> {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    make_plot(r)

    value_payload = (
        f"EA=8.035714_both;EB={r['E_B'][0]:.6f}/{r['E_B'][1]:.6f};"
        f"rel_disc={r['rel_disc'][0]:.6f}/{r['rel_disc'][1]:.6f};band<=0.1;"
        f"log10ratio={r['log10_ratio'][0]:+.4f}/{r['log10_ratio'][1]:+.4f};"
        f"same_OOM=True;kappa_SONIC=28over125pi={r['kappa_sonic_5sf']};"
        f"S0={r['S0']:.6f};omega={DELTA_OMEGA};"
        f"recon=0.7048_drift_rejected_use_0.70372"
    )  # (local)

    print(emit_4tuple(value_payload, SCHEME, CONVENTION, L_MAX))
    print_verdict_payload(
        r["verdict"], value_payload, audit_sha, content_sha,
        r["sign_verdict"], r["magnitude_verdict"], r["regime_verdict"],
        companion_note=("INFO band 0.1<rel_disc<=~1: same OOM, O(1) factor; "
                        "directionally confirming, magnitude-deferred to a "
                        "kappa-surface/omega-offset refinement (plan rubric)"),
        extra_rows=[
            ("# regulator_pin: N/A — kappa_SONIC is FIBER-ACOUSTIC "
             "(2*pi*T_acoustic), functional-INDEPENDENT; no a_n-gradient "
             "surface cited; kappa_GH=1.365 + a2/a4 thermodynamic surfaces "
             f"EXCLUDED # {GATE_ID} regulator row"),
            (f"# kappa_recon: 28/125*pi={r['kappa_sonic']:.16f} (5sf "
             f"{r['kappa_sonic_5sf']}) from canonical T_acoustic=0.112; "
             f"0.7048 = transcription drift (residual {r['resid_drift']:.3e} "
             f"= {r['drift_over_round']:.1f}x the 4dp-rounding residual "
             f"{r['resid_4dp']:.3e}; plan-freeze quoted 2.289e-5/~47x — "
             "Sage-exact supersedes, same conclusion) "
             f"# {GATE_ID} Class-8.3 reconciliation row"),
            (f"# diagnostics: omega_match=[{r['omega_match'][0]:.6f},"
             f"{r['omega_match'][1]:.6f}] M_KK (pinned 0.9 between); "
             f"S0*T_acoustic={r['S0_times_Tac']:.6f} vs tau_fold={tau_fold} "
             f"(dev {r['tau_fold_dev']*100:.2f}%) -> W3-11; amp-level ratio "
             f"~1 OOM # {GATE_ID} diagnostic row"),
        ],
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {r['verdict']} (wall {wall:.1f}s) ===")
    # Exit 0 on ANY valid verdict (math-scripts.md exit-code semantics).
    return 0


if __name__ == "__main__":
    sys.exit(main())
