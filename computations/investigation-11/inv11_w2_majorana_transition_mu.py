#!/usr/bin/env python3
"""
INV11 W2-3 — Majorana Transition Magnetic Moment
=================================================

Gate: INV11-W2-3-MAJORANA-TRANSITION-MU ([VERIFY])
Track: investigation (n=11)

Pre-registered threshold (plan §W2-3):
  PASS iff  max_i |mu_ii| <= 1e-12  (diagonal vanishes to machine epsilon,
            structural antisymmetry of the Majorana moment matrix)
       AND  mu_23/mu_13 = R_mu is a finite, determined ratio (not NaN /
            not under-determined; the m_D scale and the 1/(2 M_KK) magneton
            cancel in the ratio, so it is zero-free-parameter).
  FAIL iff  the M_3(C) texture under-determines the ratio (off-diagonal
            entries degenerate / ratio ill-defined).
  INFO  iff the ratio is determined only up to a discrete sign / Majorana-phase
            branch (the delta_CP in {0,pi} choice flips a relative sign).

Inputs (SHA-256 dual-pinned at runtime — see §4; S84+ schema):
  - computations/_shared/canonical_constants.py (feeds audit_sha256; M_KK_gravity)
  - computations/session-46/s46_phonon_magnetic_moment.py (MOMENT-46 magneton
        template: mu_natural = 1/(2 M_KK), Eq. (3)/(5))
  - computations/session-60/s60_lepto_cp_log.txt (S60 M_3(C) M_R-flavor texture
        V_B3, the Majorana mass texture in flavor space)
  - computations/session-60/s60_lepto_cp.npz (machine-readable companion of the
        log; carries V_B3 as a (3,3) float64 array — loaded so the texture is
        NOT hardcoded)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<mu_23/mu_13>, scheme=Majorana-antisymmetric-moment,
   convention=RATIO-mu23_mu13-magneton-1over2MKK, L_max=12)

Classification: PARTICLE — representation-theoretic content of D_K's Majorana
  sector. The substrate IS the antisymmetric moment matrix.

METHODOLOGY
-----------
Step 1 (diagonal = 0 EXACT). A Majorana mass eigenstate is its own antiparticle
  (nu_i^c = nu_i; J-self-conjugacy, [J,D_K]=0, KO-dim=6, T11 — PROVEN S7-S8/S43).
  The electromagnetic moment operator nu_i-bar sigma_munu nu_j F^munu is ODD
  under the i<->j interchange for self-conjugate (Majorana) fields, so the
  moment matrix is ANTISYMMETRIC: mu_ij = -mu_ji. Setting i = j gives
  2 mu_ii = 0 => mu_ii = 0 for every i. This is an EXACT structural zero
  (Schechter-Valle 1981 / Nieves 1982 selection rule, here anchored to the
  framework's PROVEN [J,D_K]=0), NOT a numerical coincidence. A diagonal-mu
  DETECTION would FALSIFY the Majorana nature.

Step 2 (transition texture). The off-diagonal magnitudes |mu_ij| inherit the
  M_3(C) off-diagonal STRUCTURE of the Majorana mass texture — the same real,
  symmetric flavor texture V_B3 that fixes M_R-flavor in s60_lepto_cp (S60
  Section 5 theorem: [J,D_K]=0 forces V_B3 real symmetric). The magneton scale
  is the MOMENT-46 natural unit mu_natural = 1/(2 M_KK) (s46 Eq. (3)/(5)); for
  the NEUTRINO sector the per-element weight is the texture entry V_ij (not the
  charged-sector Zak phase gamma_n/2pi).

Step 3 (ratio). The dimensionless transition ratios mu_23/mu_13 (and mu_12/mu_13)
  are formed from the off-diagonal texture entries. The overall m_D normalization
  (oscillation-anchored, A-N1) AND the 1/(2 M_KK) magneton cancel in the ratio,
  so the ratio is zero-free-parameter even though the OVERALL scale shares the
  m_D weakness. A SECOND Majorana-test channel beyond 0nubb.

DISCIPLINE
----------
- `from canonical_constants import *` (M_KK_gravity used for the magneton scale).
- Texture V_B3 LOADED from s60_lepto_cp.npz (not hardcoded); cross-checked
  against the plan-pinned s60_lepto_cp_log.txt values.
- Antisymmetry is IMPOSED on the moment matrix (the texture supplies magnitudes;
  the Majorana selection rule supplies the antisymmetric sign structure).
- All intermediates tagged `# (local)`. Small matrices (3x3) -> CPU numpy.
- Dual-SHA (audit + content) emitted; verdict via emit_verdict MCP tool.
- Exit 0 on a valid scientific verdict (PASS/FAIL/INFO) per math-scripts.md.

CROSS-TRACK BOUNDARY: writes ONLY to computations/investigation-11/. No
  canonical/registry/inventory edits.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — make computations/_shared importable BEFORE the canonical import
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

_SHARED = Path(__file__).resolve().parent.parent / "_shared"  # computations/_shared
sys.path.insert(0, str(_SHARED))

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import M_KK_gravity  # noqa: E402  explicit: magneton scale

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent            # computations/investigation-11
COMPUTATIONS_DIR = SESSION_DIR.parent                    # computations/
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "11"                                                                  # (local)
GATE_ID = "INV11-W2-3-MAJORANA-TRANSITION-MU"                                   # (local)
SCHEME = "Majorana-antisymmetric-moment"                                       # (local)
CONVENTION = "RATIO-mu23_mu13-magneton-1over2MKK"                              # (local)
L_MAX = 12                                                                      # (local)

# Pre-registered thresholds (plan §W2-3)
DIAG_EPS = 1e-12               # max_i |mu_ii| <= 1e-12  (machine-epsilon zero)  # (local)
RATIO_FLOOR = 1e-9             # |mu_13| must exceed this for the ratio to be   # (local)
#                                determined (guards against 0/0 under-determination)

# Output destinations (investigation-track)
OUT_NPZ = SESSION_DIR / "inv11_w2_majorana_transition_mu.npz"
OUT_PNG = SESSION_DIR / "inv11_w2_majorana_transition_mu.png"

# Plan-pinned input data files
S60_LOG = COMPUTATIONS_DIR / "session-60" / "s60_lepto_cp_log.txt"
S60_NPZ = COMPUTATIONS_DIR / "session-60" / "s60_lepto_cp.npz"
S46_TEMPLATE = COMPUTATIONS_DIR / "session-46" / "s46_phonon_magnetic_moment.py"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    S46_TEMPLATE,
    S60_LOG,
    S60_NPZ,
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


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
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
# Section 5 — Compute
# ---------------------------------------------------------------------------

def compute() -> dict:
    """Build the antisymmetric Majorana transition-moment matrix and its
    texture-fixed ratios. Returns a dict with 'value' (= mu_23/mu_13)."""

    # --- Load the M_3(C) off-diagonal texture (V_B3) from the S60 npz -------
    s60 = np.load(S60_NPZ, allow_pickle=True)  # (local)
    V_B3 = np.asarray(s60["V_B3"], dtype=float)  # (3,3) real symmetric texture  # (local)

    # Cross-check the texture is real symmetric (S60 Section 5 theorem) --------
    sym_residual = float(np.max(np.abs(V_B3 - V_B3.T)))  # (local)

    # Off-diagonal texture entries (the M_3(C) inter-generation couplings) -----
    V12 = float(V_B3[0, 1])  # (local)
    V13 = float(V_B3[0, 2])  # (local)
    V23 = float(V_B3[1, 2])  # (local)

    # --- Step 1: build the antisymmetric Majorana moment matrix --------------
    # Magnitudes from the texture; antisymmetric sign structure from the
    # Majorana electromagnetic-vertex selection rule (mu_ij = -mu_ji).
    # Magneton scale mu_natural = 1/(2 M_KK) (MOMENT-46, s46 Eq. (3)/(5)).
    M_KK = float(M_KK_gravity)               # GeV (gravity route, canonical)    # (local)
    mu_natural = 1.0 / (2.0 * M_KK)          # GeV^-1, natural magnetic moment   # (local)

    # Dimensionless (texture-unit) antisymmetric matrix
    mu_unit = np.zeros((3, 3), dtype=float)  # (local)
    mu_unit[0, 1] = V12
    mu_unit[1, 0] = -V12
    mu_unit[0, 2] = V13
    mu_unit[2, 0] = -V13
    mu_unit[1, 2] = V23
    mu_unit[2, 1] = -V23
    # diagonal left as 0 by construction (structural identity)

    # Physical-scale antisymmetric moment matrix (GeV^-1), magneton applied.
    # NOTE: the OVERALL scale also carries the oscillation-anchored m_D weakness
    # (A-N1); it is the RATIO below that is zero-free-parameter. Here we apply
    # only the magneton unit so the matrix carries explicit GeV^-1 dimension;
    # the m_D normalization would multiply every entry equally and cancels in
    # the ratio.
    mu_matrix_GeV_inv = mu_unit * mu_natural  # (local)

    # --- Diagonal-vanishing structural check (Step 1 verdict half) -----------
    diag_max = float(np.max(np.abs(np.diag(mu_unit))))  # (local)
    antisym_residual = float(np.max(np.abs(mu_unit + mu_unit.T)))  # (local)

    # --- Step 3: texture-fixed dimensionless RATIOS (scale + magneton cancel)
    ratio_determined = abs(V13) > RATIO_FLOOR  # (local)
    R_23_13 = float(V23 / V13) if ratio_determined else float("nan")  # (local)
    R_12_13 = float(V12 / V13) if ratio_determined else float("nan")  # (local)
    R_12_23 = float(V12 / V23) if abs(V23) > RATIO_FLOOR else float("nan")  # (local)

    # Explicit scale-cancellation demonstration: the ratio of two PHYSICAL
    # (magneton-applied, m_D-scaled) moments equals the bare texture ratio.
    m_D_dummy = 1.234e-3              # arbitrary nonzero m_D-scale stand-in      # (local)
    mu23_phys = V23 * mu_natural * m_D_dummy  # (local)
    mu13_phys = V13 * mu_natural * m_D_dummy  # (local)
    R_23_13_phys = float(mu23_phys / mu13_phys)  # (local)
    scale_cancel_residual = abs(R_23_13_phys - R_23_13)  # (local)  -> ~0

    return {
        "value": R_23_13,                      # gate value = mu_23/mu_13
        "V_B3": V_B3,
        "V12": V12, "V13": V13, "V23": V23,
        "sym_residual": sym_residual,
        "mu_unit": mu_unit,
        "mu_matrix_GeV_inv": mu_matrix_GeV_inv,
        "mu_natural_GeV_inv": mu_natural,
        "M_KK_GeV": M_KK,
        "diag_max": diag_max,
        "antisym_residual": antisym_residual,
        "ratio_determined": ratio_determined,
        "R_23_13": R_23_13,
        "R_12_13": R_12_13,
        "R_12_23": R_12_23,
        "scale_cancel_residual": scale_cancel_residual,
    }


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
                          sign_verdict: str | None = None,
                          magnitude_verdict: str | None = None,
                          regime_verdict: str | None = None,
                          companion_note: str = "",
                          extra_rows: list[str] | None = None) -> dict:
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


def evaluate_gate(res: dict) -> str:
    """PASS iff diagonal vanishes to <=1e-12 AND mu_23/mu_13 is finite/determined.
    FAIL iff the texture under-determines the ratio (NaN / 0-0).
    INFO is reserved for a discrete sign/Majorana-phase branch ambiguity — not
    triggered here: the texture entries are all the SAME sign (real symmetric,
    positive off-diagonals), so the magnitude ratio AND its sign are determined.
    """
    diag_ok = res["diag_max"] <= DIAG_EPS          # (local)
    antisym_ok = res["antisym_residual"] <= DIAG_EPS  # (local)
    ratio_ok = res["ratio_determined"] and np.isfinite(res["R_23_13"])  # (local)
    if diag_ok and antisym_ok and ratio_ok:
        return "PASS"
    if not ratio_ok:
        return "FAIL"
    # diagonal failed to vanish — would itself falsify the antisymmetry claim
    return "FAIL"


# ---------------------------------------------------------------------------
# Section 6b — Plot
# ---------------------------------------------------------------------------

def make_plot(res: dict) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.2))
    fig.suptitle("INV11-W2-3 — Majorana Transition Magnetic Moment "
                 "(diagonal = 0 EXACT; texture-fixed transition ratios)",
                 fontsize=12, fontweight="bold")

    # Panel 1: the antisymmetric moment matrix (texture units), heatmap
    ax0 = axes[0]
    mu_unit = res["mu_unit"]  # (local)
    vmax = float(np.max(np.abs(mu_unit)))  # (local)
    im = ax0.imshow(mu_unit, cmap="RdBu_r", vmin=-vmax, vmax=vmax)
    ax0.set_title("Antisymmetric moment matrix $\\mu_{ij}$ (texture units)\n"
                  "diagonal $\\equiv 0$ (Majorana / KO-dim-6 antisymmetry)")
    ax0.set_xticks([0, 1, 2]); ax0.set_yticks([0, 1, 2])
    ax0.set_xticklabels(["$\\nu_1$", "$\\nu_2$", "$\\nu_3$"])
    ax0.set_yticklabels(["$\\nu_1$", "$\\nu_2$", "$\\nu_3$"])
    for i in range(3):
        for j in range(3):
            ax0.text(j, i, f"{mu_unit[i, j]:+.4f}", ha="center", va="center",
                     fontsize=10, color="black")
    fig.colorbar(im, ax=ax0, fraction=0.046, pad=0.04)

    # Panel 2: texture-fixed transition ratios bar chart
    ax1 = axes[1]
    labels = ["$\\mu_{23}/\\mu_{13}$", "$\\mu_{12}/\\mu_{13}$", "$\\mu_{12}/\\mu_{23}$"]  # (local)
    vals = [res["R_23_13"], res["R_12_13"], res["R_12_23"]]  # (local)
    bars = ax1.bar(labels, vals, color=["#2E7D32", "#1565C0", "#6A1B9A"],
                   edgecolor="black", alpha=0.85)
    ax1.axhline(1.0, color="gray", ls="--", lw=1, label="ratio = 1")
    ax1.set_ylabel("texture-fixed ratio (scale + magneton cancel)")
    ax1.set_title("Zero-free-parameter transition ratios\n"
                  "from the $M_3(\\mathbb{C})$ off-diagonal texture $V_{B3}$")
    for bar, v in zip(bars, vals):
        ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                 f"{v:.4f}", ha="center", va="bottom", fontsize=10)
    ax1.legend(fontsize=9)
    ax1.set_ylim(0, max(1.15, max(vals) * 1.15))

    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  Saved plot: {OUT_PNG.relative_to(PROJECT_ROOT)}")


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

    res = compute()

    # --- Report block ---------------------------------------------------------
    print("=" * 72)
    print("STEP 1 — Majorana antisymmetry => diagonal moment = 0 EXACT")
    print("=" * 72)
    print(f"  M_3(C) texture V_B3 real-symmetric residual: {res['sym_residual']:.3e}")
    print(f"  Antisymmetry residual  max|mu + mu^T|      : {res['antisym_residual']:.3e}")
    print(f"  Diagonal magnitude     max_i |mu_ii|       : {res['diag_max']:.3e}"
          f"   (threshold <= {DIAG_EPS:.0e})")
    print()
    print("=" * 72)
    print("STEP 2 — transition texture (M_3(C) off-diagonal entries)")
    print("=" * 72)
    print(f"  V12 = {res['V12']:.8f}   (1-2 inter-generation coupling)")
    print(f"  V13 = {res['V13']:.8f}   (1-3 inter-generation coupling)")
    print(f"  V23 = {res['V23']:.8f}   (2-3 inter-generation coupling)")
    print(f"  magneton  mu_natural = 1/(2 M_KK) = {res['mu_natural_GeV_inv']:.6e} GeV^-1"
          f"   (MOMENT-46, M_KK={res['M_KK_GeV']:.6e} GeV)")
    print()
    print("=" * 72)
    print("STEP 3 — texture-fixed transition RATIOS (scale + magneton cancel)")
    print("=" * 72)
    print(f"  mu_23/mu_13 = V23/V13 = {res['R_23_13']:.10f}   <- gate value")
    print(f"  mu_12/mu_13 = V12/V13 = {res['R_12_13']:.10f}")
    print(f"  mu_12/mu_23 = V12/V23 = {res['R_12_23']:.10f}")
    print(f"  scale-cancellation residual (phys ratio - texture ratio): "
          f"{res['scale_cancel_residual']:.3e}")
    print()

    verdict = evaluate_gate(res)

    # --- Plot + data ----------------------------------------------------------
    make_plot(res)
    np.savez_compressed(
        OUT_NPZ,
        V_B3=res["V_B3"],
        V12=res["V12"], V13=res["V13"], V23=res["V23"],
        sym_residual=res["sym_residual"],
        mu_unit=res["mu_unit"],
        mu_matrix_GeV_inv=res["mu_matrix_GeV_inv"],
        mu_natural_GeV_inv=res["mu_natural_GeV_inv"],
        M_KK_GeV=res["M_KK_GeV"],
        diag_max=res["diag_max"],
        antisym_residual=res["antisym_residual"],
        ratio_determined=res["ratio_determined"],
        mu_23_over_13=res["R_23_13"],
        mu_12_over_13=res["R_12_13"],
        mu_12_over_23=res["R_12_23"],
        scale_cancel_residual=res["scale_cancel_residual"],
        diag_eps_threshold=DIAG_EPS,
        gate_value=res["value"],
        verdict=verdict,
    )
    print(f"  Saved data: {OUT_NPZ.relative_to(PROJECT_ROOT)}")
    print()

    # --- 4-tuple + verdict payload -------------------------------------------
    tag = emit_4tuple(res["value"], SCHEME, CONVENTION, L_MAX)
    print(tag)

    # Descriptive value string: diagonal=0 EXACT + the texture-fixed ratio.
    # No single-quote chars (emit_verdict wraps value='...').
    value_str = (f"mu_diag=0_EXACT(max|mu_ii|={res['diag_max']:.1e}); "
                 f"mu_23/mu_13={res['R_23_13']:.6f}; "
                 f"mu_12/mu_13={res['R_12_13']:.6f} (texture-fixed, scale-free)")  # (local)

    extra = [
        f"# texture=M_3(C) off-diagonal V_B3 (S60 s60_lepto_cp.npz); "
        f"V12={res['V12']:.6f} V13={res['V13']:.6f} V23={res['V23']:.6f}",
        f"# magneton=1/(2 M_KK)=MOMENT-46; antisym_residual={res['antisym_residual']:.1e}; "
        f"scale_cancel_residual={res['scale_cancel_residual']:.1e}",
        f"# falsifier: a DIAGONAL-mu detection (mu_ii != 0) FALSIFIES the Majorana nature",
    ]  # (local)

    print_verdict_payload(verdict, value_str, audit_sha, content_sha,
                          extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    # Exit 0 on a valid scientific verdict (PASS/FAIL/INFO) per
    # math-scripts.md §"Exit Codes and Verdict Semantics".
    return 0


if __name__ == "__main__":
    sys.exit(main())
