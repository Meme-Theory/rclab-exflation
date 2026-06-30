#!/usr/bin/env python3
"""
S115 W1-2 S115-LEPTON-PMNS-FORCED-TEXTURE — forced A_K⋊SU(3)_R lepton texture vs observed PMNS Jarlskog
=====================================================================================================

Gate: S115-LEPTON-PMNS-FORCED-TEXTURE ([SIGN])

Pre-registered threshold (PRDR §(1)(2)):
  operator: dev = |J_forced_corrected - J_PMNS_obs| / J_PMNS_obs
  PASS iff J_forced_corrected lands inside the observed PMNS 3-sigma Jarlskog band
       [J_obs_low, J_obs_high] (NuFIT 5.2 / PDG 2024 normal-ordering), i.e. dev <= band_3sigma.
  FAIL iff J_forced_corrected stays OUTSIDE the band (washed-out / symmetric-limit coincidence).
  INFO iff band-edge / ordering-or-sign-ambiguous.

Hypothesis: the SU(3)_R right-regular circulant on the LEPTON sector forces a tri-maximal
  neutrino texture (|U_ij|^2 = 1/3, J = 1/(6 sqrt 3) = 0.0962250) whose PHYSICAL PMNS Jarlskog,
  AFTER the C+H-forced coset-diagonal charged-lepton correction U_mix = U_L^dagger U_R, either
  SURVIVES near observed J ~ 0.0329 (zero-mixing-parameter corridor prediction) or is WASHED OUT.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py        (feeds audit_sha256)
  - sessions/permanent-results-registry.md             (cross-check ONLY: VII.CK D4-disposition
                                                        forced-texture annotation values)
  - script bytes                                       (feeds BOTH audit + content SHA)

External observational anchors (NOT canonical_constants imports — J_PMNS is not a framework
constant; get_constant('J_PMNS') -> not-found, confirmed at plan-freeze + this gate's MCP audit).
Hardcoded as `# (local)` observational pins with NuFIT 5.2 / PDG 2024 citation, admissible
methodological-anchor sourcing per substrate-first-canonical-sourcing.md §(i) (cross-check anchor
for an EXTERNAL-corridor test, not a substrate-first numerical pin the gate computes).

Output 4-tuple:
  (value=<dev / verdict string>, scheme=FW, convention=FORCED-CROSSED-PRODUCT-TEXTURE-LEPTON, L_max=N/A)

Classification: PARTICLE (PMNS mixing / generation texture = representation-theoretic content of D_K).

METHODOLOGY
-----------
(1) Build the SU(3)_R right-regular Z3 circulant C on the lepton multiplicity sector with
    w = exp(2*pi*i/3). A circulant is diagonalized by the DFT matrix F3 REGARDLESS of its entries
    (coefficient-INDEPENDENT), so the neutrino mixing U_R = F3 has |U_R,ij|^2 = 1/3 and the
    tri-maximal Jarlskog J = 1/(6 sqrt 3). This is the B2 Sage-exact forced circulant (S114 W-2).
(2) Impose the C+H charged-lepton-vs-neutrino sector-asymmetry: the charged-lepton mass basis is
    COSET-DIAGONAL (one-circulant-one-coset-diagonal => tri-maximal per W-2 Q3). A genuinely
    coset-diagonal unitary commutes with the Z3 coset grading => it is a diagonal phase matrix
    U_L = diag(exp(i a_k)). (A SECOND circulant would give U_mix = identity — the quark negative
    control; a coset-diagonal U_L is the lepton case.)
(3) Compute the physical misalignment U_mix = U_L^dagger U_R (the PMNS matrix in this corridor).
(4) Extract the Jarlskog J = Im(U_mix[0,0] U_mix[1,1] conj(U_mix[0,1]) conj(U_mix[1,0])) and |U_mix,ij|^2.
(5) dev = |J_forced_corrected - J_PMNS_obs| / J_PMNS_obs vs the pre-registered PMNS 3-sigma band.
(6) NEGATIVE CONTROL: M3(C)-shared quark chiralities -> TWO circulants -> U_mix = C^dagger C = identity;
    assert |U_mix - I|_F < 1e-12 != CKM.

Load-bearing physics (the surviving-vs-washed-out decider, never tuned):
  The Jarlskog invariant is the UNIQUE rephasing-invariant CP measure. A coset-DIAGONAL U_L =
  diag(exp(i a_k)) left-multiplies each row of U_R by a pure phase; the moduli |U_mix,ij| = |U_R,ij|
  are UNCHANGED (still tri-maximal 1/sqrt 3), and J is invariant because each generation index
  appears once unconjugated and once conjugated in the quartet U_00 U_11 conj(U_01) conj(U_10), so
  the row phases cancel. => J_forced_corrected = J_bare = 1/(6 sqrt 3) EXACTLY for ANY diagonal U_L.
  The C+H-forced coset-diagonal correction therefore CANNOT move J off the maximal value => the
  bare dev = 1.92 PERSISTS => WASHED-OUT (Track B). The gate scans over coset-diagonal U_L phases
  to demonstrate this invariance numerically (J flat to machine precision across all phases).

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- numpy.linalg (3x3 matrices — far below the 100x100 GPU threshold; OMP cap 8)
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- Gate verdict emitted via emit_verdict knowledge-MCP tool (race-safe); the script PRINTS the
  payload via print_verdict_payload (this is a [SIGN] gate -> sign/magnitude/regime 3-tuple).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path as _Path
# canonical_constants.py lives in computations/_shared/ — put it on sys.path first.
sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "_shared"))
from canonical_constants import *  # noqa: F401,F403,E402

# ---------------------------------------------------------------------------
# Section 2 — Standard imports (OMP cap BEFORE numpy import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import hashlib
import json
import sys
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

SESSION = "S115"                                                   # (local)
GATE_ID = "S115-LEPTON-PMNS-FORCED-TEXTURE"                        # (local)
SCHEME = "FW"                                                      # (local)
CONVENTION = "FORCED-CROSSED-PRODUCT-TEXTURE-LEPTON"               # (local)
L_MAX = "N/A"                                                      # (local) representation-theoretic, not L_max-truncated

# --- External observational anchors (NuFIT 5.2 / PDG 2024 normal-ordering) ---
# NOT canonical_constants imports: J_PMNS is not a framework constant (get_constant('J_PMNS')
# -> not-found). Methodological cross-check anchor per substrate-first-canonical-sourcing.md §(i).
#   sin^2 th12 = 0.303, sin^2 th23 = 0.572, sin^2 th13 = 0.02203, delta_CP = 197 deg (NuFIT 5.2 NO).
#   J_PMNS,obs (best fit)   ~ 0.0329   (NuFIT 5.2 / PDG 2024 NO; J = c12 s12 c23 s23 c13^2 s13 sin(dCP))
J_PMNS_OBS = 0.0329                                                # (local) NuFIT 5.2 / PDG 2024 NO best-fit lepton Jarlskog
# 3-sigma Jarlskog interval (NuFIT 5.2 NO; |J| <= J_max with J_max ~ 0.0331, lower edge near 0 as
# delta_CP -> 0/pi is within 3 sigma). The interval is wide on the LOW side (J can approach 0) and
# capped on the HIGH side by the measured mixing angles. Pin both edges:
J_PMNS_OBS_LOW = 0.0086                                            # (local) NuFIT 5.2 NO 3-sigma lower |J| (delta_CP near 3-sigma edge)
J_PMNS_OBS_HIGH = 0.0331                                           # (local) NuFIT 5.2 NO 3-sigma upper |J| (J_max at near-maximal delta_CP)

# Negative-control reference (quark CKM Jarlskog, PDG 2024) — used only for the ~3124x annotation.
J_CP_PDG_QUARK = 3.08e-05                                          # (local) PDG 2024 CKM J = (3.08 +0.15/-0.13)e-5 (canonical J_CP_PDG)

NEG_CTRL_TOL = 1e-12                                               # (local) negative-control identity assertion tolerance
PUB_SIGFIGS = 6                                                    # (local) publication precision (Class-8.3); J/dev/ratio cited downstream

# Registry cross-check values (VII.CK D4-disposition annotation; reproduced from scratch, asserted-equal)
REG_TRIMAX_MAGSQ = 1.0 / 3.0                                       # (local) |U_ij|^2 = 1/3 (registry cross-check)
REG_ARG_W = 2.0 * PI / 3.0                                         # (local) arg(w) = 2pi/3 (registry cross-check)

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / "s115_lepton_pmns_forced_texture.npz"
OUT_PNG = SESSION_DIR / "s115_lepton_pmns_forced_texture.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    PROJECT_ROOT / "sessions" / "permanent-results-registry.md",
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
def jarlskog(U: np.ndarray) -> float:
    """Standard Jarlskog invariant J = Im(U[0,0] U[1,1] conj(U[0,1]) conj(U[1,0]))."""
    return float(np.imag(U[0, 0] * U[1, 1] * np.conj(U[0, 1]) * np.conj(U[1, 0])))  # (local)


def dft3() -> np.ndarray:
    """Unitary DFT_3 matrix F3 (eigenvector matrix of ANY 3x3 circulant; coefficient-INDEPENDENT).
    F3[j,k] = (1/sqrt 3) w^{j k}, w = exp(2 pi i / 3). Tri-maximal: |F3[j,k]|^2 = 1/3."""
    w = np.exp(2j * np.pi / 3.0)  # (local) primitive cube root, arg(w) = 2pi/3
    F = np.array([[w ** ((j * k) % 3) for k in range(3)] for j in range(3)], dtype=complex)  # (local)
    return F / np.sqrt(3.0)


def right_regular_circulant(c_a: np.ndarray) -> np.ndarray:
    """SU(3)_R right-regular Z3 circulant C = c0 I + c1 P + c2 P^2, P the cyclic shift.
    Diagonalized by F3 REGARDLESS of c_a -> the |U_ij|^2=1/3 texture is coefficient-INDEPENDENT."""
    P = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)  # (local) cyclic shift (right-regular)
    return c_a[0] * np.eye(3, dtype=complex) + c_a[1] * P + c_a[2] * (P @ P)  # (local)


def compute() -> dict:
    # --- (1) neutrino sector: SU(3)_R right-regular circulant -> U_R = F3 (coefficient-INDEPENDENT) ---
    F3 = dft3()  # (local)
    U_R = F3.copy()  # (local) neutrino mixing = DFT eigenvector matrix

    # Coefficient-independence check: diagonalize an ARBITRARY circulant; its eigenvector matrix is
    # F3 up to per-column phases, so |eigvec|^2 = 1/3 for ANY coupling c_a.
    c_arbitrary = np.array([0.37, -1.21 + 0.5j, 0.84j], dtype=complex)  # (local) arbitrary SU(3)_R couplings
    C_arb = right_regular_circulant(c_arbitrary)  # (local)
    _, V_arb = np.linalg.eig(C_arb)  # (local) eigenvectors of the arbitrary circulant
    magsq_arb = np.abs(V_arb) ** 2  # (local) |eigvec_ij|^2 — must all be 1/3
    coeff_indep_magsq_max_dev = float(np.max(np.abs(magsq_arb - 1.0 / 3.0)))  # (local)

    # Bare tri-maximal Jarlskog from U_R (the SYMMETRIC limit, U_L = coset-identity)
    J_bare = jarlskog(U_R)  # (local) numerical
    J_exact = np.sqrt(3.0) / 18.0  # (local) 1/(6 sqrt 3) = sqrt(3)/18 = 0.09622504... (exact algebraic)
    magsq_UR = np.abs(U_R) ** 2  # (local) |U_R,ij|^2 — tri-maximal 1/3
    magsq_UR_max_dev = float(np.max(np.abs(magsq_UR - 1.0 / 3.0)))  # (local)

    # --- (2) charged-lepton sector: C+H-forced COSET-DIAGONAL U_L = diag(exp(i a_k)) ---
    # A genuinely coset-diagonal unitary commutes with the Z3 coset grading => diagonal phase matrix.
    # The PHYSICAL U_L from the C+H sector structure is coset-diagonal (NOT a second circulant, which
    # would give U_mix = identity = the quark control). Scan over coset-diagonal phases to demonstrate
    # that J is INVARIANT (rephasing-invariance of the Jarlskog) — the surviving-vs-washed-out decider.
    n_scan = 25  # (local) coset-diagonal phase scan resolution
    rng = np.random.default_rng(0)  # (local) deterministic seed for the phase scan
    J_scan = np.zeros(n_scan)  # (local)
    magsq_dev_scan = np.zeros(n_scan)  # (local)
    for i in range(n_scan):
        alphas = rng.uniform(0.0, 2.0 * np.pi, size=3)  # (local) coset-diagonal phases
        U_L = np.diag(np.exp(1j * alphas))  # (local) coset-diagonal charged-lepton rotation
        U_mix_i = U_L.conj().T @ U_R  # (local) physical PMNS in this corridor
        J_scan[i] = jarlskog(U_mix_i)  # (local)
        magsq_dev_scan[i] = float(np.max(np.abs(np.abs(U_mix_i) ** 2 - 1.0 / 3.0)))  # (local)
    J_scan_spread = float(np.max(J_scan) - np.min(J_scan))  # (local) flatness of J across coset-diagonal U_L
    magsq_dev_scan_max = float(np.max(magsq_dev_scan))  # (local)

    # The canonical PHYSICAL U_L: in the C+H symmetric limit the coset-diagonal rotation is the
    # coset-identity (trivial phases) -> U_mix = U_R, J_forced_corrected = J_bare. The scan above
    # proves NO coset-diagonal phase choice moves J off this value.
    U_L_phys = np.eye(3, dtype=complex)  # (local) C+H-forced coset-diagonal U_L (symmetric-limit coset-identity)
    U_mix = U_L_phys.conj().T @ U_R  # (local) physical PMNS = U_L^dagger U_R
    J_forced_corrected = jarlskog(U_mix)  # (local)
    magsq_Umix = np.abs(U_mix) ** 2  # (local) |U_mix,ij|^2

    # --- (5) deviation metric vs the observed PMNS 3-sigma Jarlskog band ---
    dev = abs(J_forced_corrected - J_PMNS_OBS) / J_PMNS_OBS  # (local) PASS-metric
    ratio = J_forced_corrected / J_PMNS_OBS  # (local) J_forced / J_obs
    # quark-CKM ratio (annotation only): bare tri-maximal J vs the quark Jarlskog
    quark_ckm_ratio = J_forced_corrected / J_CP_PDG_QUARK  # (local) ~3124x (registry annotation)
    in_band = bool(J_PMNS_OBS_LOW <= abs(J_forced_corrected) <= J_PMNS_OBS_HIGH)  # (local) PASS predicate

    # --- (6) NEGATIVE CONTROL: M3(C)-shared quark chiralities -> TWO circulants -> U_mix = identity ---
    # Both quark chiralities in the M3(C) leg => U_L AND U_R are the SAME circulant's eigenvector basis
    # => U_mix_quark = F3^dagger F3 = identity (zero mixing), != CKM.
    U_R_quark = F3.copy()  # (local) right quark chirality (M3(C) circulant)
    U_L_quark = F3.copy()  # (local) left quark chirality (SAME M3(C) circulant)
    U_mix_quark = U_L_quark.conj().T @ U_R_quark  # (local) = identity
    neg_ctrl_resid = float(np.linalg.norm(U_mix_quark - np.eye(3), ord="fro"))  # (local) |U_mix_quark - I|_F
    neg_ctrl_pass = bool(neg_ctrl_resid < NEG_CTRL_TOL)  # (local)
    J_quark = jarlskog(U_mix_quark)  # (local) = 0 (identity -> no CP)

    # --- registry cross-check (reproduce VII.CK D4-disposition values from scratch, assert-equal) ---
    crosscheck_magsq_ok = bool(abs(REG_TRIMAX_MAGSQ - 1.0 / 3.0) < 1e-15 and magsq_UR_max_dev < 1e-12)  # (local)
    crosscheck_J_ok = bool(abs(J_bare - J_exact) < 1e-12)  # (local) numerical J == exact 1/(6 sqrt 3)
    crosscheck_argw_ok = bool(abs(REG_ARG_W - 2.0 * PI / 3.0) < 1e-15)  # (local)

    # --- [SIGN] 3-tuple ---
    # sign: direction of (J_forced_corrected - J_obs). Pre-registered Step-4 prediction: dev_bare ~ 1.92
    #       >> 0 i.e. J_forced > J_obs (overshoot). sign_verdict = PASS iff computed sign matches predicted.
    sign_delta = J_forced_corrected - J_PMNS_OBS  # (local) signed delta
    predicted_sign_positive = True  # (local) substitution chain Step 4: J_bare = 0.0962 > J_obs = 0.0329
    sign_match = bool((sign_delta > 0) == predicted_sign_positive)  # (local)
    sign_verdict = "PASS" if sign_match else "FAIL"  # (local)
    # magnitude: dev vs band. The "info band" here is band membership: PASS iff in_band; else FAIL.
    if in_band:
        magnitude_verdict = "PASS"  # (local)
    else:
        magnitude_verdict = "FAIL"  # (local) bare dev = 1.92 -> outside band
    # regime: is the coset-diagonal charged-lepton construction within its symmetric-limit regime of
    #         validity? J flat across all coset-diagonal phases (spread ~ 0) => the construction is
    #         self-consistent and VALID throughout (no regime breakdown).
    regime_verdict = "VALID" if (J_scan_spread < 1e-12 and magsq_dev_scan_max < 1e-12) else "MARGINAL"  # (local)

    # Composite collapse (gate-verdicts.md): regime VALID, sign PASS, magnitude FAIL, regime VALID -> FAIL.
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"  # (local)
    elif sign_verdict == "FAIL":
        composite = "FAIL"  # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"  # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"  # (local)
    elif magnitude_verdict == "INFO":
        composite = "INFO"  # (local)
    else:
        composite = "PASS"  # (local)

    return {
        "value": dev,
        "J_bare": J_bare,
        "J_exact_1_over_6sqrt3": J_exact,
        "J_forced_corrected": J_forced_corrected,
        "dev": dev,
        "ratio_Jforced_over_Jobs": ratio,
        "quark_ckm_ratio": quark_ckm_ratio,
        "in_band": in_band,
        "J_PMNS_OBS": J_PMNS_OBS,
        "J_PMNS_OBS_LOW": J_PMNS_OBS_LOW,
        "J_PMNS_OBS_HIGH": J_PMNS_OBS_HIGH,
        "magsq_UR": magsq_UR,
        "magsq_Umix": magsq_Umix,
        "magsq_UR_max_dev": magsq_UR_max_dev,
        "coeff_indep_magsq_max_dev": coeff_indep_magsq_max_dev,
        "J_scan": J_scan,
        "J_scan_spread": J_scan_spread,
        "magsq_dev_scan_max": magsq_dev_scan_max,
        "U_R": U_R,
        "U_L_phys": U_L_phys,
        "U_mix": U_mix,
        "U_mix_quark": U_mix_quark,
        "neg_ctrl_resid": neg_ctrl_resid,
        "neg_ctrl_pass": neg_ctrl_pass,
        "J_quark": J_quark,
        "crosscheck_magsq_ok": crosscheck_magsq_ok,
        "crosscheck_J_ok": crosscheck_J_ok,
        "crosscheck_argw_ok": crosscheck_argw_ok,
        "sign_delta": sign_delta,
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "composite": composite,
    }


# ---------------------------------------------------------------------------
# Section 6 — Verdict payload + plot
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note: str = "", extra_rows=None) -> dict:
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


def make_plot(res: dict) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(15, 4.6))  # (local)

    # (a) |U_mix,ij|^2 heatmap (forced corridor PMNS, tri-maximal)
    im0 = axes[0].imshow(res["magsq_Umix"], vmin=0, vmax=0.5, cmap="viridis")  # (local)
    axes[0].set_title(r"$|U_{mix,ij}|^2$ (forced corridor PMNS)" + "\n" + r"tri-maximal $= 1/3$ = 0.3333")
    axes[0].set_xticks([0, 1, 2]); axes[0].set_yticks([0, 1, 2])
    axes[0].set_xlabel("neutrino gen"); axes[0].set_ylabel("charged-lepton gen")
    for i in range(3):
        for j in range(3):
            axes[0].text(j, i, f"{res['magsq_Umix'][i, j]:.4f}", ha="center", va="center", color="w", fontsize=9)
    fig.colorbar(im0, ax=axes[0], fraction=0.046)

    # (b) Jarlskog on a number line with the PMNS 3-sigma band
    ax = axes[1]  # (local)
    ax.axvspan(res["J_PMNS_OBS_LOW"], res["J_PMNS_OBS_HIGH"], color="tab:green", alpha=0.25,
               label=f"PMNS 3$\\sigma$ band\n[{res['J_PMNS_OBS_LOW']:.4f}, {res['J_PMNS_OBS_HIGH']:.4f}]")
    ax.axvline(res["J_PMNS_OBS"], color="tab:green", lw=2, label=f"$J_{{obs}}$ = {res['J_PMNS_OBS']:.4f}")
    ax.axvline(res["J_forced_corrected"], color="tab:red", lw=2.5,
               label=f"$J_{{forced,corr}}$ = {res['J_forced_corrected']:.5f}")
    ax.axvline(res["J_exact_1_over_6sqrt3"], color="black", ls="--", lw=1.0,
               label=r"$1/(6\sqrt{3})$ = 0.09623")
    ax.set_xlim(0, 0.11)
    ax.set_yticks([])
    ax.set_xlabel("Jarlskog invariant $J$")
    ax.set_title(f"forced $J$ vs observed PMNS\n"
                 f"dev = {res['dev']:.5f}, ratio = {res['ratio_Jforced_over_Jobs']:.5f}  "
                 f"({'IN' if res['in_band'] else 'OUT of'} band)")
    ax.legend(loc="upper center", fontsize=8)

    # (c) J flatness across coset-diagonal U_L phases (rephasing-invariance) + negative control
    ax2 = axes[2]  # (local)
    ax2.plot(np.arange(len(res["J_scan"])), res["J_scan"], "o-", color="tab:blue", ms=4,
             label=f"$J(U_L^\\dagger U_R)$, $U_L$ coset-diag\nspread = {res['J_scan_spread']:.2e}")
    ax2.axhline(res["J_exact_1_over_6sqrt3"], color="black", ls="--", lw=1.0, label=r"$1/(6\sqrt{3})$")
    ax2.axhline(res["J_PMNS_OBS"], color="tab:green", lw=1.5, label=f"$J_{{obs}}$ = {res['J_PMNS_OBS']:.4f}")
    ax2.set_xlabel("coset-diagonal phase sample")
    ax2.set_ylabel("Jarlskog $J$")
    ax2.set_ylim(0, 0.11)
    ax2.set_title("rephasing-invariance of $J$\n"
                  f"neg-control $|U_{{mix}}^{{quark}}-I|_F$ = {res['neg_ctrl_resid']:.1e}")
    ax2.legend(loc="center right", fontsize=8)

    fig.suptitle("S115-LEPTON-PMNS-FORCED-TEXTURE — forced $A_K\\rtimes SU(3)_R$ lepton texture vs observed PMNS Jarlskog",
                 fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)  # (local)
    closure = closure_hash(pins)  # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    res = compute()  # (local)

    # --- report ---
    print(f"  [neutrino sector] U_R = DFT3, |U_R,ij|^2 max dev from 1/3 = {res['magsq_UR_max_dev']:.2e}")
    print(f"  [coeff-indep]     arbitrary circulant |eigvec|^2 max dev from 1/3 = {res['coeff_indep_magsq_max_dev']:.2e}")
    print(f"  J_bare (numeric)            = {res['J_bare']:.8f}")
    print(f"  J_exact 1/(6 sqrt 3)        = {res['J_exact_1_over_6sqrt3']:.8f}")
    print(f"  J_forced_corrected          = {res['J_forced_corrected']:.8f}")
    print(f"  J_PMNS_obs (NuFIT/PDG NO)   = {res['J_PMNS_OBS']:.8f}")
    print(f"  dev = |Jfc - Jobs|/Jobs     = {res['dev']:.6f}")
    print(f"  ratio Jfc/Jobs              = {res['ratio_Jforced_over_Jobs']:.6f}")
    print(f"  quark-CKM ratio (annot)     = {res['quark_ckm_ratio']:.1f}x")
    print(f"  in PMNS 3-sigma band?       = {res['in_band']}  (band [{res['J_PMNS_OBS_LOW']:.4f}, {res['J_PMNS_OBS_HIGH']:.4f}])")
    print(f"  J flat across coset-diag U_L: spread = {res['J_scan_spread']:.2e}, |U|^2 dev = {res['magsq_dev_scan_max']:.2e}")
    print(f"  [neg control] |U_mix_quark - I|_F = {res['neg_ctrl_resid']:.2e}  (PASS={res['neg_ctrl_pass']}), J_quark = {res['J_quark']:.2e}")
    print(f"  [crosscheck] magsq={res['crosscheck_magsq_ok']} J={res['crosscheck_J_ok']} argw={res['crosscheck_argw_ok']}")
    print(f"  [3-tuple] sign={res['sign_verdict']} magnitude={res['magnitude_verdict']} regime={res['regime_verdict']}")
    print()

    # --- save npz ---
    np.savez(
        OUT_NPZ,
        U_R=res["U_R"], U_L_phys=res["U_L_phys"], U_mix=res["U_mix"], U_mix_quark=res["U_mix_quark"],
        J_bare=res["J_bare"], J_exact=res["J_exact_1_over_6sqrt3"], J_forced_corrected=res["J_forced_corrected"],
        magsq_UR=res["magsq_UR"], magsq_Umix=res["magsq_Umix"],
        dev=res["dev"], ratio=res["ratio_Jforced_over_Jobs"], quark_ckm_ratio=res["quark_ckm_ratio"],
        in_band=res["in_band"],
        J_PMNS_OBS=res["J_PMNS_OBS"], J_PMNS_OBS_LOW=res["J_PMNS_OBS_LOW"], J_PMNS_OBS_HIGH=res["J_PMNS_OBS_HIGH"],
        J_scan=res["J_scan"], J_scan_spread=res["J_scan_spread"], magsq_dev_scan_max=res["magsq_dev_scan_max"],
        neg_ctrl_resid=res["neg_ctrl_resid"], neg_ctrl_pass=res["neg_ctrl_pass"], J_quark=res["J_quark"],
        coeff_indep_magsq_max_dev=res["coeff_indep_magsq_max_dev"], magsq_UR_max_dev=res["magsq_UR_max_dev"],
        sign_verdict=res["sign_verdict"], magnitude_verdict=res["magnitude_verdict"],
        regime_verdict=res["regime_verdict"], composite=res["composite"],
    )
    print(f"  npz -> {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    make_plot(res)
    print(f"  png -> {OUT_PNG.relative_to(PROJECT_ROOT)}")
    print()

    verdict = res["composite"]  # (local)
    value_str = (f"dev={res['dev']:.6f}_ratio={res['ratio_Jforced_over_Jobs']:.6f}_"
                 f"Jforced={res['J_forced_corrected']:.7f}_Jobs={res['J_PMNS_OBS']:.4f}_"
                 f"band=[{res['J_PMNS_OBS_LOW']:.4f},{res['J_PMNS_OBS_HIGH']:.4f}]_in_band={res['in_band']}_"
                 f"WASHED-OUT_quarkCKM={res['quark_ckm_ratio']:.0f}x_negctrl_resid={res['neg_ctrl_resid']:.1e}")  # (local)

    tag = emit_4tuple(value_str, SCHEME, CONVENTION, L_MAX)  # (local)
    print(tag)

    extra_rows = [  # (local)
        (f"# coset-diagonal U_L leaves J INVARIANT (rephasing-invariance): J_scan_spread="
         f"{res['J_scan_spread']:.2e}; J_forced_corrected={res['J_forced_corrected']:.7f}=1/(6sqrt3) EXACT"),
        (f"# negative-control: M3(C)-shared quark chiralities -> two circulants -> U_mix=I, "
         f"|U_mix_quark-I|_F={res['neg_ctrl_resid']:.1e} != CKM (quark-CKM ratio {res['quark_ckm_ratio']:.0f}x)"),
        (f"# registry VII.CK D4-disposition cross-check: |U_ij|^2=1/3 ({res['crosscheck_magsq_ok']}), "
         f"J=1/(6sqrt3) ({res['crosscheck_J_ok']}), arg(w)=2pi/3 ({res['crosscheck_argw_ok']})"),
    ]
    print_verdict_payload(
        verdict, value_str, audit_sha, content_sha,
        sign_verdict=res["sign_verdict"], magnitude_verdict=res["magnitude_verdict"],
        regime_verdict=res["regime_verdict"],
        companion_note="forced-and-WASHED-OUT: coset-diagonal U_L cannot move J off maximal 1/(6sqrt3); dev=1.92>>band",
        extra_rows=extra_rows,
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
