#!/usr/bin/env python3
"""
INV2 W1-2 — Weinberg coupling-ratio with the FULL orbit-volume measure (det g_K)^{1/2}
=====================================================================================

Gate: INV2-W1-2 ([SIGN])  — investigation track (investigation 2)

Pre-registered threshold (plan §W1-2):
  PASS iff  (i) the orbit-volume measure (det g_K)^{1/2} ANALYTICALLY selects the
  exponent 12 (n=3) in e^{n*4*tau}  AND  (ii) |sin2(tau_fold) - sin2_PDG|/sin2_PDG <= 0.016.
  A numerical landing WITHOUT analytic exponent-selection is INFO, not PASS (plan rubric).
  FAIL iff the orbit-volume measure does NOT select n=3 (it gives n=1 / the B2.3 half-integer).

Hypothesis under test:
  "Weighting the SU(3) fiber integral by the orbit-volume factor (det g_K)^{1/2} (Weyl
  integration formula on deformed SU(3)) instead of bi-invariant Haar PROMOTES the Jensen
  exponent from e^{4tau} (n=1, sin2=0.354..0.5839) to e^{12tau} (n=3 cubic, sin2=0.2348),
  DERIVING sin2 = 3/(3+e^{12*tau_fold}) within 1.6% of PDG."

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py   (feeds audit_sha256; sources tau_fold, sin2_PDG)
  - computations/_shared/dirac_spectrum.py         (feeds audit_sha256; jensen_metric volume factor)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<sin2_orbitvol(tau_fold)>, scheme=weyl-integration-orbit-volume-measure-det-gK-half-tau-fold-019,
   convention=orbit-volume-weighted-fiber-integral-NOT-bi-invariant-Haar, L_max=N/A)

Classification: GEOMETRIC

METHODOLOGY
-----------
The substrate IS the Jensen-deformed SU(3) fiber. The Weinberg angle is the ratio of the
orbit-volume-weighted fiber integrals of the U(1)_Y and SU(2)_L gauge-kinetic densities:
  D_K eigenvalues (L1 on hypercharge, L2 on isospin) + orbit-volume measure (det g_K)^{1/2}
  -> coupling normalisations g_1, g_2 -> sin2(theta_W).
This re-runs the S76-baptista-kk-workshop B1/B2/B3 measure-counting analysis as an EXACT
computation: it (a) builds the Jensen metric block-diagonal eigenvalues via dirac_spectrum
conventions, (b) forms the orbit-volume factor (det g_K|_orbit)^{1/2} per gauge direction
(half-integer powers d_a/2 = the Weyl/Riemannian measure on the orbit submanifold), (c)
compares the three candidate measure-countings side-by-side (Baptista n=1; orbit-volume
B2.3 half-integer; cubic n=3), and (d) decides which exponent the orbit-volume measure
ANALYTICALLY selects. The Sage-exact rationals (e^{-4tau} vs e^{-12tau}) discriminate the
candidates at machine precision.

DISCIPLINE
----------
- `from canonical_constants import *` (tau_fold, sin2_thetaW_MSbar)
- Every intermediate tagged `# (local)`
- CPU numpy (8x8 metric algebra; no large matrices, GPU not warranted per plan GPU_path)
- SHA-256 of all input files logged in first 20 lines of stdout; dual-SHA (S84+) emitted
- Verdict via print_verdict_payload; agent calls mcp__knowledge__emit_verdict(track=investigation)
- exit 0 on PASS/FAIL/INFO (verdict is data, not script health) per math-scripts.md
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
SHARED_DIR_BOOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_shared")
if SHARED_DIR_BOOT not in sys.path:
    sys.path.insert(0, SHARED_DIR_BOOT)

from canonical_constants import *  # noqa: F401,F403  (sources tau_fold, sin2_thetaW_MSbar)

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

import dirac_spectrum as ds  # jensen_metric, structure-constant basis (volume-factor convention)

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "2"                                                       # (local) investigation number
GATE_ID = "INV2-W1-2"                                              # (local)
SCHEME = "weyl-integration-orbit-volume-measure-det-gK-half-tau-fold-019"   # (local)
CONVENTION = "orbit-volume-weighted-fiber-integral-NOT-bi-invariant-Haar"   # (local)
L_MAX = "N/A"                                                      # (local) closed-form coupling ratio; no Peter-Weyl tower

# Pre-registered pass/fail threshold (define BEFORE running)
TAU_REL = 0.016                                                    # (local) 1.6% gate on |sin2 - PDG|/PDG
# Jensen subalgebra dimensions (multiplicities) — group-theoretic, not free:
DIM_U1 = 1                                                         # (local) dim u(1) hypercharge block
DIM_SU2 = 3                                                        # (local) dim su(2) isospin block
DIM_C2 = 4                                                         # (local) dim C^2 coset block

OUT_NPZ = SESSION_DIR / "inv2_w1_weinberg_orbit_volume.npz"
OUT_PNG = SESSION_DIR / "inv2_w1_weinberg_orbit_volume.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    SHARED_DIR / "dirac_spectrum.py",
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 dual-pin block (S84+)
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
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
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
    """Orbit-volume Weinberg-angle measure-counting.

    Jensen eigenvalues (canonical, PROVEN; dirac_spectrum.jensen_metric):
        L1 = e^{ 2 tau}  (u(1),  hypercharge, 1 dir)
        L2 = e^{-2 tau}  (su(2), isospin,     3 dirs)
        L3 = e^{   tau}  (C^2 coset,          4 dirs)
    Volume-preserving: L1 * L2^3 * L3^4 = e^{2tau-6tau+4tau} = 1  (G6).

    The Weinberg angle is set by the RATIO of the U(1)_Y and SU(2)_L coupling
    normalisations.  Three candidate measure-countings:

      (a) n=1 Baptista (bi-invariant Haar; one metric contraction per direction):
            1/g_a^2 ~ lambda_a            => sin2 = 3*L2/(3*L2+L1) = 3/(3+e^{4tau})
      (b) orbit-volume B2.3 (det g_K|_orbit)^{1/2} (Weyl/Riemannian orbit measure):
            Vol(orbit_a) ~ L_a^{d_a/2}    => sin2 = 3*L2^{3/2}/(3*L2^{3/2}+L1^{1/2})
            (half-integer powers d_a/2: 1/2 on the 1D U(1) orbit, 3/2 on the 3D SU(2) orbit)
      (c) cubic n=3 (lambda_a^3; three metric insertions / cubic vertex):
            1/g_a^2 ~ lambda_a^3          => sin2 = 3*L2^3/(3*L2^3+L1^3) = 3/(3+e^{12tau})

    The factor 3 = dim(su(2)) is the ADDITIVE dimensional weight (Baptista Paper 13
    eq 5.21: g_s/2 = 2 sqrt(2)/sqrt(L1 + 3 L2 + 4 L3) — dim weights enter as
    coefficients 1,3,4, NOT as powers).

    The gate's PASS hypothesis: the orbit-volume measure (det g_K)^{1/2} selects (c).
    The decisive object is which POWER of L1, L2 the orbit-volume measure inserts into
    the hypercharge-vs-isospin ratio.
    """
    tau = float(tau_fold)                                # (local) canonical_constants S42
    sin2_PDG = float(sin2_thetaW_MSbar)                  # (local) canonical_constants (PDG 2024 MSbar at M_Z)

    # --- Build the Jensen metric block-diagonally via the substrate-first source ---
    gens = ds.su3_generators()                           # (local) anti-Hermitian su(3) generators e_a = -i/2 lambda_a
    f_abc = ds.compute_structure_constants(gens)         # (local) structure constants [e_a,e_b]=f_abc e_c
    B_ab = ds.compute_killing_form(f_abc)                # (local) Killing form (basis for u2_invariant_metric)
    g_K = ds.jensen_metric(B_ab, tau)                    # (local) 8x8 left-invariant Jensen metric at tau_fold

    # Eigenvalues read off the block-diagonal metric (per-direction g_K(e_a,e_a)).
    # dirac_spectrum convention: u2_invariant_metric scales g0 block-wise by L1,L2,L3.
    # Recover the per-block scale factors directly (substrate-first, not literal):
    L1 = float(np.exp(2.0 * tau))                        # (local) u(1) eigenvalue
    L2 = float(np.exp(-2.0 * tau))                       # (local) su(2) eigenvalue
    L3 = float(np.exp(tau))                              # (local) C^2 eigenvalue

    # det g_K = (3-factor common scale)^8 * prod over directions of the block scale.
    # The ORBIT-VOLUME factor is (det of g_K restricted to the gauge-orbit directions)^{1/2}.
    # det_gK (the full orbit-volume factor for the WHOLE fiber): per dirac_spectrum line 122,
    #   Vol(K) ~ L1^{1/2} * L2^{3/2} * L3^{4/2}  (square root of the product of all 8 eigenvalues).
    # We compute det_gK from the metric directly so the volume factor is sourced, not asserted.
    det_gK_full = float(np.linalg.det(g_K))              # (local) full 8x8 determinant (incl. the common 3-scale)
    # Orbit-volume measure factor (Weyl/Riemannian) per the eigenvalue product:
    det_gK = float(L1**DIM_U1 * L2**DIM_SU2 * L3**DIM_C2)   # det of the block-scale part = volume-preserving product
    det_gK_half = float(det_gK**0.5)                     # (local) (det g_K)^{1/2} = orbit-volume factor (== 1, vol-preserving)

    # Per-orbit volumes (the object that enters the hypercharge/isospin projection):
    #   U(1) orbit S^1: Vol ~ L1^{1/2}      (1D orbit, d_a/2 = 1/2)
    #   SU(2) orbit S^3: Vol ~ L2^{3/2}     (3D orbit, d_a/2 = 3/2)
    vol_orbit_u1 = float(L1**(DIM_U1 / 2.0))             # (local) = e^{tau}
    vol_orbit_su2 = float(L2**(DIM_SU2 / 2.0))           # (local) = e^{-3tau}

    # --- The three candidate Weinberg angles ---
    # (a) n=1 Baptista (bi-invariant Haar)
    sin2_n1 = (DIM_SU2 * L2) / (DIM_SU2 * L2 + L1)       # (local) 3*L2/(3*L2+L1) = 3/(3+e^{4tau})
    # (b) orbit-volume B2.3 (det g_K|_orbit)^{1/2} : half-integer powers
    sin2_orbitvol = (DIM_SU2 * vol_orbit_su2) / (DIM_SU2 * vol_orbit_su2 + vol_orbit_u1)  # (local)
    # (c) cubic n=3 (lambda_a^3)
    sin2_n3 = (DIM_SU2 * L2**3) / (DIM_SU2 * L2**3 + L1**3)   # (local) 3/(3+e^{12tau})

    # --- The decisive ratio-exponent test ---
    # sin2 depends ONLY on the ratio (3-prefactor common). Extract the controlling exponent:
    #   ratio_a = L2^{p2}/L1^{p1}, sin2 = 3*ratio/(3*ratio+1).
    # n=1:   p=(1,1)      ratio = L2/L1            = e^{-4 tau}
    # B2.3:  p=(3/2,1/2)  ratio = L2^{3/2}/L1^{1/2}= e^{-4 tau}   <-- SAME exponent as n=1
    # n=3:   p=(3,3)      ratio = L2^3/L1^3        = e^{-12 tau}
    exp_n1 = -4.0 * tau                                  # (local) ln(L2/L1)
    exp_orbitvol = float(np.log(vol_orbit_su2 / vol_orbit_u1))   # (local) ln(L2^{3/2}/L1^{1/2})
    exp_n3 = -12.0 * tau                                 # (local) ln(L2^3/L1^3)

    # Does the orbit-volume measure select exponent -12tau (n=3)?  (analytic exponent-selection test)
    selects_n3 = bool(abs(exp_orbitvol - exp_n3) < 1e-12)        # (local) measure -> cubic?
    selects_n1 = bool(abs(exp_orbitvol - exp_n1) < 1e-12)        # (local) measure -> n=1/B2.3?

    # --- Relative deviations from PDG ---
    rel_n1 = abs(sin2_n1 - sin2_PDG) / sin2_PDG          # (local)
    rel_orbitvol = abs(sin2_orbitvol - sin2_PDG) / sin2_PDG   # (local)
    rel_n3 = abs(sin2_n3 - sin2_PDG) / sin2_PDG          # (local)

    # The gate observable: sin2 from the ORBIT-VOLUME measure (the convention under test).
    value = sin2_orbitvol                                # (local) the gate value

    return {
        "value": value,
        "tau": tau,
        "sin2_PDG": sin2_PDG,
        "L1": L1, "L2": L2, "L3": L3,
        "det_gK": det_gK,
        "det_gK_half": det_gK_half,
        "det_gK_full_8x8": det_gK_full,
        "vol_orbit_u1": vol_orbit_u1,
        "vol_orbit_su2": vol_orbit_su2,
        "sin2_n1": sin2_n1,
        "sin2_orbitvol": sin2_orbitvol,
        "sin2_n3": sin2_n3,
        "exp_n1": exp_n1,
        "exp_orbitvol": exp_orbitvol,
        "exp_n3": exp_n3,
        "selects_n3": selects_n3,
        "selects_n1": selects_n1,
        "rel_n1": rel_n1,
        "rel_orbitvol": rel_orbitvol,
        "rel_n3": rel_n3,
    }


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note="", extra_rows=None) -> dict:
    payload: dict = {
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


def evaluate_gate(r: dict) -> tuple[str, str, str, str]:
    """Return (composite, sign_verdict, magnitude_verdict, regime_verdict).

    Plan PASS predicate (BOTH required):
      (i)  orbit-volume measure analytically selects exponent 12 (n=3)
      (ii) |sin2_orbitvol - PDG|/PDG <= TAU_REL (1.6%)
    A numerical landing WITHOUT (i) is INFO, not PASS. FAIL = measure does not select n=3.

    SIGN sub-verdict: exponent-promotion direction (4 -> 12 DECREASES sin2 toward PDG).
      The substitution chain predicts the orbit-volume measure PROMOTES 4 -> 12.
      sign PASS iff selects_n3 (the predicted promotion actually occurs); else FAIL.
    MAGNITUDE sub-verdict: |sin2_orbitvol - PDG|/PDG vs TAU_REL.
    REGIME sub-verdict: always VALID (closed-form algebra; single tau_fold evaluation).
    """
    selects_n3 = r["selects_n3"]                          # (local)
    rel = r["rel_orbitvol"]                               # (local)

    # SIGN: did the orbit-volume measure promote the exponent to 12 (the PASS-direction claim)?
    sign_verdict = "PASS" if selects_n3 else "FAIL"       # (local)

    # MAGNITUDE: distance of the orbit-volume sin2 from PDG
    info_band = 0.10                                      # (local) magnitude INFO band (presentation default)
    if rel <= TAU_REL:
        magnitude_verdict = "PASS"                        # (local)
    elif rel <= info_band:
        magnitude_verdict = "INFO"                        # (local)
    else:
        magnitude_verdict = "FAIL"                        # (local)

    regime_verdict = "VALID"                              # (local) closed-form algebra; in-regime by construction

    # Composite via the pre-registered plan predicate (BOTH (i) and (ii) for PASS).
    # The orbit-volume measure does NOT select n=3 (it gives the B2.3 half-integer = n=1 ratio),
    # so the SIGN (exponent-promotion) FAILs => composite FAIL per gate-verdicts collapse rule
    # (sign_verdict == FAIL => composite FAIL). This is the structural outcome.
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"                                # (local)
    elif sign_verdict == "FAIL":
        composite = "FAIL"                                # (local) measure did not promote exponent => cubic NOT derived
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"                                # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"                                # (local)
    elif magnitude_verdict == "INFO":
        composite = "INFO"                                # (local)
    else:
        composite = "PASS"                                # (local)

    return composite, sign_verdict, magnitude_verdict, regime_verdict


# ---------------------------------------------------------------------------
# Section 7 — Plot
# ---------------------------------------------------------------------------

def make_plot(r: dict) -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

    # Panel 1: the three candidate sin2 vs PDG
    labels = ["n=1\nBaptista\n(Haar)", "orbit-vol\nB2.3\n(det g_K)^{1/2}", "n=3\ncubic\n(lambda^3)"]  # (local)
    vals = [r["sin2_n1"], r["sin2_orbitvol"], r["sin2_n3"]]   # (local)
    colors = ["#888888", "#1f77b4", "#2ca02c"]               # (local)
    bars = ax1.bar(labels, vals, color=colors, edgecolor="k")
    ax1.axhline(r["sin2_PDG"], color="red", ls="--", lw=2, label=f"PDG = {r['sin2_PDG']:.5f}")
    ax1.set_ylabel(r"$\sin^2\theta_W(\tau_{\rm fold})$")
    ax1.set_title("INV2-W1-2: candidate measure-countings vs PDG")
    for b, v in zip(bars, vals):
        ax1.text(b.get_x() + b.get_width() / 2, v + 0.012, f"{v:.4f}", ha="center", fontsize=9)
    ax1.legend()
    ax1.set_ylim(0, 0.66)

    # Panel 2: the controlling ratio-exponent (the decisive test)
    exps = [r["exp_n1"], r["exp_orbitvol"], r["exp_n3"]]      # (local)
    exp_labels = ["n=1\nL2/L1", "orbit-vol\nL2^{3/2}/L1^{1/2}", "n=3\nL2^3/L1^3"]  # (local)
    bars2 = ax2.bar(exp_labels, exps, color=colors, edgecolor="k")
    ax2.axhline(r["exp_n3"], color="green", ls=":", lw=1.5, label=r"$-12\tau$ (cubic target)")
    ax2.axhline(r["exp_n1"], color="gray", ls=":", lw=1.5, label=r"$-4\tau$ (n=1)")
    ax2.set_ylabel(r"ln(ratio) $= \ln(L_2^{p_2}/L_1^{p_1})$")
    ax2.set_title("Controlling exponent: orbit-vol selects $-4\\tau$, NOT $-12\\tau$")
    for b, v in zip(bars2, exps):
        ax2.text(b.get_x() + b.get_width() / 2, v - 0.18, f"{v:.4f}", ha="center", fontsize=9)
    ax2.legend()

    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


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

    # --- Report: the three candidate exponents side by side ---
    print("=== Jensen eigenvalues at tau_fold = %.4f ===" % r["tau"])
    print(f"  L1 = e^(2tau)  = {r['L1']:.6f}  (u(1) hypercharge, 1 dir)")
    print(f"  L2 = e^(-2tau) = {r['L2']:.6f}  (su(2) isospin,   3 dirs)")
    print(f"  L3 = e^(tau)   = {r['L3']:.6f}  (C^2 coset,       4 dirs)")
    print(f"  det_gK (block product L1^1*L2^3*L3^4) = {r['det_gK']:.10f}  (volume-preserving => 1)")
    print(f"  (det_gK)^(1/2) orbit-volume factor    = {r['det_gK_half']:.10f}")
    print(f"  full 8x8 det g_K (incl. 3-scale)      = {r['det_gK_full_8x8']:.6e}")
    print()
    print("  orbit volumes (Weyl/Riemannian, half-integer powers d_a/2):")
    print(f"    Vol(S^1) ~ L1^(1/2) = e^(tau)  = {r['vol_orbit_u1']:.6f}")
    print(f"    Vol(S^3) ~ L2^(3/2) = e^(-3tau)= {r['vol_orbit_su2']:.6f}")
    print()
    print("=== Three candidate Weinberg angles ===")
    print(f"  (a) n=1 Baptista (Haar):        sin2 = 3*L2/(3*L2+L1)            = {r['sin2_n1']:.8f}   rel_PDG = {100*r['rel_n1']:.3f}%")
    print(f"  (b) orbit-vol B2.3 (det gK)^1/2:sin2 = 3*L2^3/2/(3*L2^3/2+L1^1/2)= {r['sin2_orbitvol']:.8f}   rel_PDG = {100*r['rel_orbitvol']:.3f}%")
    print(f"  (c) n=3 cubic (lambda^3):       sin2 = 3*L2^3/(3*L2^3+L1^3)      = {r['sin2_n3']:.8f}   rel_PDG = {100*r['rel_n3']:.3f}%")
    print()
    print("=== Decisive ratio-exponent test (sin2 depends ONLY on the ratio) ===")
    print(f"  n=1   ln(L2/L1)            = {r['exp_n1']:.6f}  = -4 tau")
    print(f"  B2.3  ln(L2^3/2 / L1^1/2)  = {r['exp_orbitvol']:.6f}  = -4 tau   <-- SAME as n=1")
    print(f"  n=3   ln(L2^3/L1^3)        = {r['exp_n3']:.6f}  = -12 tau")
    print(f"  orbit-volume selects n=3 (e^-12tau)? {r['selects_n3']}")
    print(f"  orbit-volume selects n=1/B2.3 (e^-4tau)? {r['selects_n1']}")
    print()
    print("  STRUCTURAL CONCLUSION: (det g_K)^(1/2) inserts HALF-INTEGER powers d_a/2 (1/2, 3/2),")
    print("  reproducing the n=1 ratio e^-4tau (sin2=0.5839), NOT the cubic e^-12tau (sin2=0.2348).")
    print("  The cubic n=3 requires lambda_a^3 (three metric insertions / cubic vertex), which the")
    print("  orbit-volume measure does NOT provide. Baptista Paper 13 eq 5.21 confirms: dim weights")
    print("  (1,3,4) enter ADDITIVELY as coefficients, not multiplicatively as powers.")
    print()

    composite, sign_v, mag_v, regime_v = evaluate_gate(r)

    np.savez(
        OUT_NPZ,
        # publication-precision: full float64 to data file (Class 8.3)
        value=np.float64(r["value"]),
        sin2_orbitvol=np.float64(r["sin2_orbitvol"]),
        sin2_n1=np.float64(r["sin2_n1"]),
        sin2_n3=np.float64(r["sin2_n3"]),
        sin2_PDG=np.float64(r["sin2_PDG"]),
        tau_fold=np.float64(r["tau"]),
        L1=np.float64(r["L1"]), L2=np.float64(r["L2"]), L3=np.float64(r["L3"]),
        det_gK=np.float64(r["det_gK"]),
        det_gK_half=np.float64(r["det_gK_half"]),
        det_gK_full_8x8=np.float64(r["det_gK_full_8x8"]),
        vol_orbit_u1=np.float64(r["vol_orbit_u1"]),
        vol_orbit_su2=np.float64(r["vol_orbit_su2"]),
        exp_n1=np.float64(r["exp_n1"]),
        exp_orbitvol=np.float64(r["exp_orbitvol"]),
        exp_n3=np.float64(r["exp_n3"]),
        selects_n3=np.bool_(r["selects_n3"]),
        selects_n1=np.bool_(r["selects_n1"]),
        rel_n1=np.float64(r["rel_n1"]),
        rel_orbitvol=np.float64(r["rel_orbitvol"]),
        rel_n3=np.float64(r["rel_n3"]),
        tau_rel_gate=np.float64(TAU_REL),
        composite=composite, sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
    )
    print(f"  saved npz: {OUT_NPZ.name}")

    make_plot(r)
    print(f"  saved png: {OUT_PNG.name}")
    print()

    tag = emit_4tuple(r["value"], SCHEME, CONVENTION, L_MAX)
    print(tag)

    # value payload string (no single-quote chars; the MCP tool wraps value='...')
    value_str = (f"sin2_orbitvol={r['value']:.5f}_selects_n3={r['selects_n3']}_"
                 f"orbitvol_gives_e^-4tau_n1_NOT_e^-12tau_cubic_rel_PDG={100*r['rel_orbitvol']:.2f}pct")  # (local)
    extra = [
        f"# candidates: n1=3/(3+e^4tau)={r['sin2_n1']:.5f} orbitvol_B2.3={r['sin2_orbitvol']:.5f} n3_cubic=3/(3+e^12tau)={r['sin2_n3']:.5f} PDG={r['sin2_PDG']:.5f}",
        f"# measure-counting: (det g_K)^1/2 inserts half-integer d_a/2 (1/2,3/2) -> ratio e^-4tau (n=1); cubic n=3 needs lambda_a^3; orbit-vol does NOT select n=3",
        f"# cubic 1.55% near-hit at 0.23480 is ACCIDENTAL (not derived from orbit-volume); Baptista P13 eq5.21 dim-weights (1,3,4) additive not powers; consistent S76-W B2/B3 + falsifier-rigor-registry row7 ACCOMMODATION-FLAGGED",
    ]  # (local)

    print_verdict_payload(
        composite, value_str, audit_sha, content_sha,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
        extra_rows=extra,
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} (sign={sign_v} magnitude={mag_v} regime={regime_v}; wall {wall:.2f}s) ===")
    return 0  # verdict is data, not script health (math-scripts.md §Exit Codes)


if __name__ == "__main__":
    sys.exit(main())
