#!/usr/bin/env python3
"""
INV7-W2-3 — n_PBH L_pix error-budget band (investigation-7, SOLO)
=================================================================

Gate: INV7-W2-3 ([SIGN]; INFO-by-construction precision-hygiene band)
Classification: GEOMETRIC

Pre-registered "threshold":
  NONE. This is a precision-HYGIENE band, NOT a PASS/FAIL physics gate (per the
  r3 non-compute clause + plan §W2-3). The pre-registered OUTCOME is the band +
  the Class-8.3 precision-tighter-than-systematic flag. Verdict = INFO-by-construction.

Method (plan investigation-7-plan-w2.md §W2-3):
  Mechanical band propagation, NO new substrate physics. Hold L_max=14 FIXED (the
  L_max-truncation axis is the SEPARATE W4-2 workshop subject). Carry L_pix_LRD as a
  function of the virial mass via the pixelation-lock L_pix_LRD ∝ M_BH, sweep M_BH
  across the JWST virial-mass dispute range [1e5, 1e8] M_sun, and propagate through
  n_PBH ∝ 1/L_pix^3 (the 9-dex-in-volume sensitivity). Normalize to the canonical
  anchor (M_anchor = 1e7 M_sun, n_PBH_FW_central): the n_edge*prob_form/k^3 prefactor
  cancels in the ratio, so n_PBH(M_BH) = n_PBH_FW_central * (M_anchor/M_BH)^3.
  All endpoints Sage-QQ-exact via fractions.Fraction.

Substitution chain (signed band direction):
  n_PBH = n_edge*prob_form / L_pix_LRD^3                       [§VII.AX.OP-PROJ / Row #65]
  L_pix_LRD ∝ M_BH (pixelation-lock at r_s = 2 G M_BH / c^2)   [LINEAR in M_BH]
  => n_PBH(M_BH) = n_PBH_anchor * (M_anchor/M_BH)^3            [prefactor cancels]
  => n_PBH ∝ M_BH^{-3}: M_BH DOWN => L_pix DOWN => n_PBH UP    [direction; sign_verdict driver]
  3-decade M_BH dispute  ->  9-decade n_PBH band (cubed).

Output 4-tuple:
  (value=<band+flag>, scheme=FW, convention=RATIO, L_max=14)

DISCIPLINE
----------
- `from canonical_constants import *` (n_PBH_FW_central, line 628; pub precision 5 sig figs).
- SUBSTRATE-FIRST SOURCING: uses the canonical 5-sig-fig anchor 7.2761e-23, NOT the
  plan's rounded "7.28e-23". The Class-8.3 point sharpens (5 sf vs 9 dex systematic).
- dual-SHA (audit_sha256 + content_sha256) per S84+ schema (script-template.py §4).
- Verdict emitted via the emit_verdict knowledge-MCP tool (track="investigation")
  by the orchestrator; this script only PRINTS the payload (script-template.py §6).
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
import time
from fractions import Fraction
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent            # computations/investigation-7/
COMPUTATIONS_DIR = SESSION_DIR.parent                    # computations/
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403  (supplies n_PBH_FW_central)

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --- Identity (investigation 7; emit with track="investigation") ---
SESSION = "S7"                                           # (local) -> session=7 in payload
GATE_ID = "INV7-W2-3"                                    # (local)
SCHEME = "FW"                                            # (local)
CONVENTION = "RATIO"                                     # (local)
L_MAX = 14                                               # (local) held FIXED; M_BH is the swept axis

OUT_NPZ = SESSION_DIR / "inv7_w2_3_n_pbh_lpix_error_budget.npz"
OUT_PNG = SESSION_DIR / "inv7_w2_3_n_pbh_lpix_error_budget.png"

INPUT_FILES = [SHARED_DIR / "canonical_constants.py"]


# --- Section 4: SHA helpers (verbatim from script-template.py §4) ---
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


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          extra_rows=None) -> dict:
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


# --- Section 5: Compute ---
def compute() -> dict:
    # Canonical anchor (substrate-first; 5-sig-fig published value, line 628).
    central = n_PBH_FW_central                                   # 7.2761e-23 m^-3
    central_QQ = Fraction(72761, 10 ** 27)                       # (local) Sage-QQ exact image of 7.2761e-23
    assert abs(float(central_QQ) - central) / central < 1e-9, "QQ image must match canonical anchor"

    M_anchor = Fraction(10 ** 7)                                 # (local) 1e7 M_sun anchor (L_pix_LRD pin epoch)
    decade_M = [Fraction(10) ** e for e in (5, 6, 7, 8)]        # (local) virial-mass dispute decade anchors

    # n_PBH(M) = central * (M_anchor / M)^3   [prefactor cancels in the ratio]
    n_of_M_QQ = {int(M): central_QQ * (M_anchor / M) ** 3 for M in decade_M}   # (local)
    n_of_M = {M: float(v) for M, v in n_of_M_QQ.items()}        # (local)

    n_low_edge_QQ = n_of_M_QQ[10 ** 8]                           # (local) HIGH M_BH -> LOWEST n_PBH
    n_high_edge_QQ = n_of_M_QQ[10 ** 5]                          # (local) LOW M_BH  -> HIGHEST n_PBH
    n_low_edge = float(n_low_edge_QQ)                            # (local) 7.2761e-26
    n_high_edge = float(n_high_edge_QQ)                          # (local) 7.2761e-17

    span_decades = float(np.log10(n_high_edge / n_low_edge))    # (local) ~9.0 exact
    # direction check: n_PBH strictly DECREASING in M_BH (exponent -3)
    Ms_sorted = sorted(n_of_M)                                  # (local)
    monotone_decreasing = all(n_of_M[Ms_sorted[i]] > n_of_M[Ms_sorted[i + 1]]
                              for i in range(len(Ms_sorted) - 1))  # (local)

    # Class-8.3: publication precision (5 sig figs of the anchor) vs 9-decade systematic.
    pub_sig_figs = 5                                            # (local) canonical pub precision (line 628)
    systematic_dex = round(span_decades)                       # (local) 9
    precision_tighter_than_systematic = (systematic_dex > 0)   # (local) True by construction

    return {
        "central": central,
        "central_QQ": (central_QQ.numerator, central_QQ.denominator),
        "M_anchor": int(M_anchor),
        "decade_M": [int(M) for M in decade_M],
        "n_of_M": {str(k): v for k, v in n_of_M.items()},
        "n_low_edge": n_low_edge,
        "n_high_edge": n_high_edge,
        "n_low_edge_QQ": (n_low_edge_QQ.numerator, n_low_edge_QQ.denominator),
        "n_high_edge_QQ": (n_high_edge_QQ.numerator, n_high_edge_QQ.denominator),
        "span_decades": span_decades,
        "monotone_decreasing": monotone_decreasing,
        "pub_sig_figs": pub_sig_figs,
        "systematic_dex": systematic_dex,
        "precision_tighter_than_systematic": precision_tighter_than_systematic,
    }


def main() -> int:
    t0 = time.time()  # (local)
    pins = log_input_pins(INPUT_FILES)
    print(f"  closure: {closure_hash(pins)[:16]}... (legacy closure, informational)")
    audit_sha, content_sha = compute_dual_sha(Path(__file__).resolve(),
                                              SHARED_DIR / "canonical_constants.py", pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    r = compute()
    print(f"  n_PBH(M_BH=1e5, LOW/Rusakov)  = {r['n_of_M']['100000']:.4e} m^-3")
    print(f"  n_PBH(M_BH=1e7, anchor)       = {r['n_of_M']['10000000']:.4e} m^-3")
    print(f"  n_PBH(M_BH=1e8, HIGH/naive)   = {r['n_of_M']['100000000']:.4e} m^-3")
    print(f"  band = [{r['n_low_edge']:.4e}, {r['n_high_edge']:.4e}] m^-3")
    print(f"  span = {r['span_decades']:.3f} decades   (n_PBH ∝ M_BH^-3; monotone-decreasing={r['monotone_decreasing']})")
    print(f"  Class-8.3: pub precision {r['pub_sig_figs']} sig figs vs systematic {r['systematic_dex']} dex"
          f"  -> precision_tighter_than_systematic={r['precision_tighter_than_systematic']}")

    # Plot: n_PBH vs M_BH log-log with band + anchor.
    fig, ax = plt.subplots(figsize=(7, 5))
    Mgrid = np.logspace(5, 8, 256)                              # (local)
    ngrid = r["central"] * (1e7 / Mgrid) ** 3                   # (local)
    ax.loglog(Mgrid, ngrid, "b-", lw=2, label=r"$n_{\rm PBH}\propto M_{BH}^{-3}$")
    ax.axhspan(r["n_low_edge"], r["n_high_edge"], alpha=0.12, color="orange",
               label=f"9-dex band [{r['n_low_edge']:.2e}, {r['n_high_edge']:.2e}]")
    ax.plot(1e7, r["central"], "r*", ms=16, label=f"anchor 7.2761e-23 (M=1e7, L=14)")
    ax.axvspan(1e5, 1e7, alpha=0.07, color="green")
    ax.set_xlabel(r"$M_{BH}\ [M_\odot]$ (virial-mass dispute: Rusakov low $\to$ naive high)")
    ax.set_ylabel(r"$n_{\rm PBH}\ [\mathrm{m}^{-3}]$")
    ax.set_title("INV7-W2-3  n_PBH L_pix error-budget (Class-8.3 precision-hygiene; INFO-by-construction)")
    ax.legend(fontsize=8, loc="upper right")
    ax.grid(True, which="both", alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)

    np.savez(
        OUT_NPZ,
        central=r["central"],
        M_anchor=r["M_anchor"],
        decade_M=np.array(r["decade_M"], dtype=float),
        n_of_M=np.array([r["n_of_M"][str(M)] for M in r["decade_M"]], dtype=float),
        n_low_edge=r["n_low_edge"],
        n_high_edge=r["n_high_edge"],
        span_decades=r["span_decades"],
        monotone_decreasing=r["monotone_decreasing"],
        pub_sig_figs=r["pub_sig_figs"],
        systematic_dex=r["systematic_dex"],
        precision_tighter_than_systematic=r["precision_tighter_than_systematic"],
        n_low_edge_QQ_num=float(r["n_low_edge_QQ"][0]),
        n_low_edge_QQ_den=float(r["n_low_edge_QQ"][1]),
        n_high_edge_QQ_num=float(r["n_high_edge_QQ"][0]),
        n_high_edge_QQ_den=float(r["n_high_edge_QQ"][1]),
    )

    # Verdict: INFO-by-construction (precision-hygiene band; no PASS/FAIL threshold).
    #   sign_verdict   = PASS  (n_PBH ∝ M_BH^-3 confirmed: M down -> n up; band direction correct)
    #   magnitude_verdict = INFO  (no threshold; report band + Class-8.3 flag)
    #   regime_verdict = VALID (exact rational arithmetic throughout)
    sign_v = "PASS" if r["monotone_decreasing"] else "FAIL"     # (local)
    value = (f"band=[{r['n_low_edge']:.4e},{r['n_high_edge']:.4e}]m^-3;"
             f"span={r['span_decades']:.3f}dex;M_BH=[1e5,1e8]Msun;n_PBH~M_BH^-3;"
             f"anchor=7.2761e-23(M=1e7,Lmax=14_held);pub_prec=5sf;systematic=9dex;"
             f"Class-8.3-precision-tighter-than-systematic;INFO-by-construction")  # (local)

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)
    print_verdict_payload(
        "INFO", value, audit_sha, content_sha,
        sign_verdict=sign_v, magnitude_verdict="INFO", regime_verdict="VALID",
        extra_rows=[
            "# INV7-W2-3 INFO-by-construction precision-hygiene band (Class-8.3); NOT a PASS/FAIL physics gate",
            "# L_max=14 held FIXED (truncation axis = separate W4-2 workshop); M_BH virial-mass axis swept [1e5,1e8] Msun",
        ],
    )
    print(f"\n=== {GATE_ID}: INFO (wall {time.time() - t0:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
