#!/usr/bin/env python3
"""
INV4 W1-4 — INV4-W1-4-EXIT-GREYBODY-A-S-NORMALIZATION
=====================================================

Gate: INV4-W1-4-EXIT-GREYBODY-A-S-NORMALIZATION ([SIGN])

Pre-registered threshold:
  delta_OOM = log10(A_s / A_s_CMB), A_s = |beta_fold|^2 * integral Gamma(omega) d omega.
  Gap-closure metric = |delta_OOM| vs the AMPLITUDE-NORM-66 baseline 3.15 OOM.
  PASS iff |delta_OOM| <= 0.5 (greybody resolves the gap to within ~factor 3; the
          'permanent wall' reading is FALSIFIED).
  INFO iff 0.5 < |delta_OOM| < 3.15 (partial-OOM reduction).
  FAIL iff |delta_OOM| >= 3.15 (greybody does NOT reduce the gap; wall reading stands)
          OR the SIGN sub-criterion fails (integral Gamma d omega >= omega_max => amplification,
          physically forbidden barrier sign error).
  [SIGN]: greybody factor SUPPRESSES (0 <= Gamma <= 1, low-freq barrier) => A_s DECREASES
          relative to the un-filtered |beta_fold|^2.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-75/s75_dimer_z2_pair_production.npz  (|beta_fold|^2 produced squeeze)
  - canonical_constants.py (kappa_exit=47.6146 pre-promoted; T_compound=7.5781 = T_exit; A_s_CMB; n_pairs)
  - script bytes

Output 4-tuple:
  (value=<delta_OOM>, scheme=GREYBODY-TRANSMISSION-BARRIER, convention=ABSOLUTE, L_max=N/A)

Classification: PHONONIC

METHODOLOGY
-----------
The exit horizon IS a substrate feature: the a_4^{Pauli-Villars} BCS condensation-energy gradient at
the post-fold transit defines kappa_exit = 47.6146 M_KK (the surface-gravity analog;
S95-W4-2-HAWKING-ANALOG-T-LEDGER row2_exit_a4 PASS), with T_exit = kappa_exit/(2*pi) = 7.5781 M_KK =
T_compound (the a_4 exit value). The greybody factor Gamma(omega) is the frequency-dependent transmission
probability through the exit-horizon effective barrier whose characteristic scale IS kappa_exit. We model
the barrier with the canonical analytically-tractable horizon-scattering potential (Poschl-Teller, the
universal QNM/greybody barrier) of peak V0 = kappa_exit^2 and width-scale alpha = kappa_exit, giving the
EXACT transmission Gamma_PT(omega), and cross-check Gamma model-independently with a transfer-matrix (2x2
per omega) solve of the 1D scattering problem through the same V_eff(omega). Both satisfy 0 <= Gamma <= 1,
Gamma -> 0 as omega -> 0 (the barrier blocks low frequencies), Gamma -> 1 as omega >> kappa_exit. The
escaping scalar amplitude is A_s = |beta_fold|^2 * integral_0^{omega_max} Gamma(omega) d omega, with
|beta_fold|^2 = n_pairs = 59.8 (the total integrated produced squeeze at the fold, s75 Parker pair
production; per-mode |beta_k|^2 = nk_total recorded as cross-check). The residual gap delta_OOM =
log10(A_s / A_s_CMB) is compared to the un-filtered 3.15-OOM AMPLITUDE-NORM-66 baseline.

Direction: D_K eigenvalues -> a_4 BCS gradient -> kappa_exit / exit-horizon barrier -> Gamma(omega)
transmission -> A_s = |beta_fold|^2 * integral Gamma d omega -> comparison to Planck A_s. NOT the retracted
S73B dispersive-group-velocity mechanism — this is the model-independent transmission-barrier route.

DISCIPLINE
----------
- from canonical_constants import *
- kappa_exit pre-promoted to canonical_constants.py via update_constant BEFORE this run (substrate-first
  §(ii)); T_exit imported as the canonical T_compound alias.
- CLASS=FULL — full physical transmission barrier; NO SCHEMATIC helper imported.
- regulator_pin = a_4^{Pauli-Villars} (the exit-horizon barrier height is set by the a_4 BCS
  condensation-energy gradient that defines kappa_exit).
- All intermediates tagged # (local). numpy.linalg (N_omega=2000 transmission evaluations + 2x2 transfer
  matrices; below the torch.linalg matrix threshold).
- Dual-SHA (audit_sha256 + content_sha256) emitted; verdict via emit_verdict MCP tool (race-safe).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — Path setup (must precede the canonical import)
# ---------------------------------------------------------------------------
import os

os.environ.setdefault("OMP_NUM_THREADS", "8")    # CPU-only barrier/integral; avoid 32-core contention
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys

_HERE = os.path.dirname(os.path.abspath(__file__))           # computations/investigation-4
_SHARED = os.path.join(os.path.dirname(_HERE), "_shared")    # computations/_shared
sys.path.insert(0, _SHARED)

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (
    kappa_exit,
    T_compound,
    A_s_CMB,
    n_pairs,
    M_KK,
    tau_fold,
)

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
SESSION_DIR = Path(__file__).resolve().parent          # computations/investigation-4
COMPUTATIONS_DIR = SESSION_DIR.parent                  # computations
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "4"                                                       # (local) investigation number
GATE_ID = "INV4-W1-4-EXIT-GREYBODY-A-S-NORMALIZATION"              # (local)
SCHEME = "GREYBODY-TRANSMISSION-BARRIER"                            # (local)
CONVENTION = "ABSOLUTE"                                             # (local)
L_MAX = "N/A"                                                       # (local)

# Pre-registered machinery pins (PRDR)
N_OMEGA = 2000                                                      # (local) frequency grid
OMEGA_MAX_FACTOR = 10.0                                             # (local) omega_max = 10 * kappa_exit
N_OMEGA_CROSSCHECK = 4000                                           # (local) convergence cross-check grid
BASELINE_OOM = 3.15                                                # (local) AMPLITUDE-NORM-66 baseline

# Pre-registered PASS/INFO/FAIL bands on |delta_OOM|
PASS_BAND = 0.5                                                     # (local)
FAIL_BAND = 3.15                                                   # (local)

# Output destinations (investigation track)
OUT_NPZ = SESSION_DIR / "inv4_w1_exit_greybody_as.npz"
OUT_PNG = SESSION_DIR / "inv4_w1_exit_greybody_as.png"

S75_NPZ = COMPUTATIONS_DIR / "session-75" / "s75_dimer_z2_pair_production.npz"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    S75_NPZ,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY; first lines of stdout)
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
# Section 5 — Greybody barrier physics
# ---------------------------------------------------------------------------

def gamma_poschl_teller(omega: np.ndarray, V0: float, alpha: float) -> np.ndarray:
    """EXACT transmission through a Poschl-Teller barrier V(x) = V0 / cosh^2(alpha x).

    The canonical analytically-tractable horizon-scattering / QNM greybody barrier.
    Transmission probability (Ferrari-Mashhoon / standard 1D scattering result):

        Gamma(omega) = sinh^2(pi omega / alpha)
                       / [ sinh^2(pi omega / alpha) + cosh^2( pi/2 * sqrt(4 V0/alpha^2 - 1) ) ]

    Properties enforced by construction:
      0 <= Gamma <= 1 ; Gamma -> 0 as omega -> 0 ; Gamma -> 1 as omega >> sqrt(V0).
    Here omega is the wave frequency, V0 the barrier peak, alpha the inverse width-scale.
    """
    s = 4.0 * V0 / alpha**2 - 1.0  # (local)
    # cosh^2 of the constant 'shape' term (real for V0/alpha^2 > 1/4; the barrier regime)
    if s >= 0.0:
        shape = np.cosh(0.5 * np.pi * np.sqrt(s)) ** 2  # (local) over-barrier shape constant
    else:
        # sub-critical (shallow) barrier -> cos^2 branch; not reached for V0=alpha^2 (s=3)
        shape = np.cos(0.5 * np.pi * np.sqrt(-s)) ** 2  # (local)
    num = np.sinh(np.pi * omega / alpha) ** 2  # (local)
    return num / (num + shape)


def gamma_transfer_matrix(omega: np.ndarray, V0: float, alpha: float,
                          x_half: float = 12.0, n_x: int = 4000) -> np.ndarray:
    """Model-independent transmission through the SAME V_eff(x) = V0/cosh^2(alpha x)
    via a piecewise-constant transfer-matrix (2x2 per slice) solve of the 1D
    stationary Schrodinger/wave scattering problem  psi'' + (omega^2 - V(x)) psi = 0.

    Returns |t(omega)|^2 = Gamma(omega) for each omega. Cross-check on the analytic
    Poschl-Teller form (model-independence of the SIGN + magnitude of Gamma).
    """
    x = np.linspace(-x_half / alpha, x_half / alpha, n_x)  # (local) span in physical units
    dx = x[1] - x[0]  # (local)
    Vx = V0 / np.cosh(alpha * x) ** 2  # (local) potential on the grid
    out = np.empty_like(omega)  # (local)
    for i, w in enumerate(omega):
        if w <= 0.0:
            out[i] = 0.0
            continue
        k_asym = w  # (local) asymptotic wavenumber (V -> 0 at +-inf)
        # local wavenumbers q_j = sqrt(omega^2 - V_j) (complex inside classically-forbidden region)
        q = np.sqrt(np.complex128(w**2) - Vx)  # (local)
        # Build total transfer matrix across slices (piecewise-constant propagation + interface).
        M = np.eye(2, dtype=np.complex128)  # (local)
        for j in range(n_x - 1):
            qj = q[j]      # (local)
            qj1 = q[j + 1]  # (local)
            # propagation across slice j (width dx) with wavenumber qj
            phase = qj * dx  # (local)
            P = np.array([[np.exp(-1j * phase), 0.0],
                          [0.0, np.exp(1j * phase)]], dtype=np.complex128)  # (local)
            # interface j -> j+1 (matching psi, psi')
            r = qj / qj1  # (local)
            I = 0.5 * np.array([[1.0 + r, 1.0 - r],
                                [1.0 - r, 1.0 + r]], dtype=np.complex128)  # (local)
            M = I @ P @ M
        # Transmission for incidence from the left: |t|^2 = |1/M[0,0]|^2 (asymptotic q equal both sides)
        t = 1.0 / M[0, 0]  # (local)
        out[i] = float(np.abs(t) ** 2)
    return out


# ---------------------------------------------------------------------------
# Section 6 — Compute
# ---------------------------------------------------------------------------

def compute() -> dict:
    # --- Barrier parameters from the a_4 BCS gradient (canonical) ---
    kappa = float(kappa_exit)                       # (local) surface-gravity analog, M_KK units
    V0 = kappa**2                                    # (local) barrier peak ~ kappa_exit^2
    alpha = kappa                                    # (local) inverse width-scale = kappa_exit
    omega_max = OMEGA_MAX_FACTOR * kappa             # (local)

    # --- |beta_fold|^2 : the produced squeeze at the fold (s75 Parker pair production) ---
    d = np.load(S75_NPZ)  # (local)
    nk_total = np.asarray(d["nk_total"], dtype=float)  # (local) per-mode |beta_k|^2 (16 modes)
    n_even_abs = float(d["n_even_abs"])               # (local) total integrated occupation = 59.8 = n_pairs
    # Canonical aggregate squeeze at the fold = total integrated produced occupation.
    beta_fold_sq = n_even_abs                          # (local) = sum_k |beta_k|^2 (absolute) = n_pairs
    # Cross-check vs canonical n_pairs
    n_pairs_consistency = abs(beta_fold_sq - float(n_pairs))  # (local)

    # --- omega grid + transmission (analytic Poschl-Teller) ---
    omega = np.linspace(0.0, omega_max, N_OMEGA)      # (local)
    Gamma = gamma_poschl_teller(omega, V0, alpha)     # (local) 0 <= Gamma <= 1

    # Riemann-sum integral of Gamma over [0, omega_max]
    integral_Gamma = float(np.trapezoid(Gamma, omega))    # (local) units of M_KK (frequency)
    f_grey = integral_Gamma / omega_max               # (local) fractional transmission (must be < 1)

    # --- Convergence cross-check (N_omega = 4000) ---
    omega_cc = np.linspace(0.0, omega_max, N_OMEGA_CROSSCHECK)  # (local)
    Gamma_cc = gamma_poschl_teller(omega_cc, V0, alpha)         # (local)
    integral_cc = float(np.trapezoid(Gamma_cc, omega_cc))          # (local)
    integral_drift = abs(integral_cc - integral_Gamma) / integral_Gamma  # (local) must be < 1%

    # --- Model-independence cross-check: transfer-matrix Gamma on a coarse omega grid ---
    omega_tm = np.linspace(0.0, omega_max, 60)        # (local) coarse (transfer-matrix is per-omega expensive)
    Gamma_tm = gamma_transfer_matrix(omega_tm, V0, alpha)  # (local)
    Gamma_pt_on_tm = gamma_poschl_teller(omega_tm, V0, alpha)  # (local)
    # max abs deviation between analytic and transfer-matrix transmission
    tm_max_dev = float(np.max(np.abs(Gamma_tm - Gamma_pt_on_tm)))  # (local)

    # --- A_s assembly ---
    A_s_filtered = beta_fold_sq * integral_Gamma      # (local) greybody-filtered escaping amplitude
    A_s_unfiltered_norm = beta_fold_sq * omega_max    # (local) un-filtered normalization (f_grey=1 limit)

    # --- residual OOM gap vs Planck ---
    delta_OOM = float(np.log10(A_s_filtered / A_s_CMB))      # (local) signed OOM gap
    abs_delta_OOM = abs(delta_OOM)                           # (local)

    # The suppression the greybody actually supplies, in OOM, relative to the un-filtered amplitude:
    grey_suppression_OOM = float(np.log10(A_s_filtered / A_s_unfiltered_norm))  # (local) = log10(f_grey) <= 0

    # --- SIGN sub-criterion: integral Gamma < omega_max (suppression, never amplification) ---
    sign_ok = integral_Gamma < omega_max              # (local) f_grey < 1

    # --- Gate decision (composite 3-tuple) ---
    # sign_verdict: greybody SUPPRESSES (integral Gamma < omega_max)?
    sign_verdict = "PASS" if sign_ok else "FAIL"      # (local)
    # magnitude_verdict on |delta_OOM| vs the bands
    if abs_delta_OOM <= PASS_BAND:
        magnitude_verdict = "PASS"                    # (local)
    elif abs_delta_OOM < FAIL_BAND:
        magnitude_verdict = "INFO"                    # (local)
    else:
        magnitude_verdict = "FAIL"                    # (local)
    # regime_verdict: numerical method validity (integral converged + transfer-matrix agreement)
    regime_ok = (integral_drift < 0.01) and (tm_max_dev < 0.05)  # (local)
    regime_verdict = "VALID" if regime_ok else "MARGINAL"        # (local)

    return {
        "value": delta_OOM,
        "kappa": kappa,
        "V0": V0,
        "alpha": alpha,
        "omega_max": omega_max,
        "omega": omega,
        "Gamma": Gamma,
        "integral_Gamma": integral_Gamma,
        "f_grey": f_grey,
        "beta_fold_sq": beta_fold_sq,
        "nk_total": nk_total,
        "n_pairs_consistency": n_pairs_consistency,
        "A_s_filtered": A_s_filtered,
        "A_s_unfiltered_norm": A_s_unfiltered_norm,
        "delta_OOM": delta_OOM,
        "abs_delta_OOM": abs_delta_OOM,
        "grey_suppression_OOM": grey_suppression_OOM,
        "integral_drift": integral_drift,
        "omega_tm": omega_tm,
        "Gamma_tm": Gamma_tm,
        "Gamma_pt_on_tm": Gamma_pt_on_tm,
        "tm_max_dev": tm_max_dev,
        "sign_ok": sign_ok,
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
    }


def collapse_composite(sign_v: str, magnitude_v: str, regime_v: str) -> str:
    """Pre-registered composite-collapse rule (gate-verdicts.md)."""
    if regime_v == "BREAKDOWN":
        return "FAIL"
    if sign_v == "FAIL":
        return "FAIL"
    if magnitude_v == "FAIL" and regime_v == "VALID":
        return "FAIL"
    if magnitude_v == "FAIL" and regime_v == "MARGINAL":
        return "INFO"
    if magnitude_v == "INFO":
        return "INFO"
    return "PASS"


# ---------------------------------------------------------------------------
# Section 7 — Plot
# ---------------------------------------------------------------------------

def make_plot(R: dict) -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

    # Left: Gamma(omega) transmission barrier
    ax1.plot(R["omega"], R["Gamma"], color="C0", lw=2,
             label=r"$\Gamma(\omega)$ (Poschl-Teller, analytic)")
    ax1.scatter(R["omega_tm"], R["Gamma_tm"], color="C3", s=14, zorder=5,
                label=r"$\Gamma(\omega)$ (transfer-matrix x-check)")
    ax1.axvline(R["kappa"], color="k", ls="--", lw=1,
                label=fr"$\kappa_{{exit}}={R['kappa']:.3f}\,M_{{KK}}$")
    ax1.axhline(1.0, color="gray", ls=":", lw=0.8)
    ax1.set_xlabel(r"$\omega$  ($M_{KK}$ units)")
    ax1.set_ylabel(r"transmission  $\Gamma(\omega)$")
    ax1.set_title(r"Exit-horizon greybody factor  ($a_4^{Pauli-Villars}$ barrier)")
    ax1.set_ylim(-0.02, 1.05)
    ax1.legend(loc="lower right", fontsize=8)
    ax1.grid(alpha=0.25)

    # Right: A_s gap closure bar
    labels = ["un-filtered\nbaseline\n(AMP-NORM-66)", "greybody-filtered\n$A_s$", "Planck\n$A_s^{CMB}$"]
    # represent on a log10 scale relative to A_s_CMB
    vals = [BASELINE_OOM, R["delta_OOM"], 0.0]  # (local) OOM relative to A_s_CMB
    colors = ["C7", "C0", "C2"]
    bars = ax2.bar(labels, vals, color=colors, alpha=0.85)
    ax2.axhline(0.0, color="C2", ls="-", lw=1)
    ax2.axhspan(-PASS_BAND, PASS_BAND, color="C2", alpha=0.12, label=f"PASS band |Δ|≤{PASS_BAND}")
    ax2.set_ylabel(r"$\delta_{OOM}=\log_{10}(A_s/A_s^{CMB})$")
    ax2.set_title(
        f"Greybody suppression = {R['grey_suppression_OOM']:.3f} OOM\n"
        fr"$\delta_{{OOM}}$(filtered) = {R['delta_OOM']:.3f}  vs baseline {BASELINE_OOM}"
    )
    for b, v in zip(bars, vals):
        ax2.annotate(f"{v:.2f}", (b.get_x() + b.get_width() / 2, v),
                     ha="center", va="bottom" if v >= 0 else "top", fontsize=9)
    ax2.legend(loc="upper right", fontsize=8)
    ax2.grid(alpha=0.25, axis="y")

    fig.suptitle(
        f"INV4-W1-4  greybody $A_s$ normalization   "
        fr"|$\beta_{{fold}}$|$^2$={R['beta_fold_sq']:.1f},  "
        fr"$f_{{grey}}$={R['f_grey']:.4f},  $\int\Gamma d\omega$={R['integral_Gamma']:.2f}",
        fontsize=10,
    )
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 — Output payload
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
        "track": "investigation",
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
# Section 9 — Main
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

    R = compute()

    print("=== Barrier / squeeze inputs ===")
    print(f"  kappa_exit          = {R['kappa']:.6f}  M_KK   (a_4^Pauli-Villars BCS gradient)")
    print(f"  T_exit (=kappa/2pi) = {R['kappa']/(2*np.pi):.6f}  M_KK ; T_compound = {float(T_compound):.6f}")
    print(f"  V0 (barrier peak)   = {R['V0']:.4f} ; alpha (width^-1) = {R['alpha']:.4f}")
    print(f"  omega_max           = {R['omega_max']:.4f}  (= {OMEGA_MAX_FACTOR} * kappa_exit)")
    print(f"  |beta_fold|^2       = {R['beta_fold_sq']:.6f}  (= n_even_abs; |n_pairs - this| = {R['n_pairs_consistency']:.2e})")
    print()
    print("=== Greybody transmission ===")
    print(f"  integral Gamma d omega = {R['integral_Gamma']:.6f}")
    print(f"  omega_max              = {R['omega_max']:.6f}")
    print(f"  f_grey = int/omega_max = {R['f_grey']:.6f}   (must be < 1 for suppression)")
    print(f"  grey suppression       = {R['grey_suppression_OOM']:.6f} OOM  (= log10 f_grey, <= 0)")
    print(f"  integral drift (N=4000)= {R['integral_drift']:.3e}  (< 1e-2 target)")
    print(f"  transfer-matrix max dev= {R['tm_max_dev']:.3e}  (< 5e-2 target; model-independence)")
    print()
    print("=== A_s assembly ===")
    print(f"  A_s_filtered           = {R['A_s_filtered']:.6e}")
    print(f"  A_s_unfiltered_norm    = {R['A_s_unfiltered_norm']:.6e}")
    print(f"  A_s_CMB (Planck)       = {A_s_CMB:.6e}")
    print(f"  delta_OOM (filtered)   = {R['delta_OOM']:.6f}")
    print(f"  |delta_OOM|            = {R['abs_delta_OOM']:.6f}   vs baseline {BASELINE_OOM}")
    print()
    print("=== SIGN / MAGNITUDE / REGIME ===")
    print(f"  sign_ok (int < omega_max) = {R['sign_ok']}  -> sign_verdict = {R['sign_verdict']}")
    print(f"  magnitude_verdict         = {R['magnitude_verdict']}  (PASS<=0.5 / INFO<3.15 / FAIL>=3.15)")
    print(f"  regime_verdict            = {R['regime_verdict']}")
    print()

    verdict = collapse_composite(R["sign_verdict"], R["magnitude_verdict"], R["regime_verdict"])

    # Save npz (plan-mandated fields)
    np.savez(
        OUT_NPZ,
        omega_grid=R["omega"],
        Gamma_omega=R["Gamma"],
        integral_Gamma=R["integral_Gamma"],
        f_grey=R["f_grey"],
        beta_fold_sq=R["beta_fold_sq"],
        A_s_filtered=R["A_s_filtered"],
        delta_OOM=R["delta_OOM"],
        baseline_OOM=BASELINE_OOM,
        kappa_exit_used=R["kappa"],
        # cross-check / provenance extras
        A_s_unfiltered_norm=R["A_s_unfiltered_norm"],
        A_s_CMB=A_s_CMB,
        grey_suppression_OOM=R["grey_suppression_OOM"],
        V0=R["V0"],
        alpha=R["alpha"],
        omega_max=R["omega_max"],
        nk_total=R["nk_total"],
        n_pairs_consistency=R["n_pairs_consistency"],
        integral_drift=R["integral_drift"],
        omega_tm=R["omega_tm"],
        Gamma_tm=R["Gamma_tm"],
        Gamma_pt_on_tm=R["Gamma_pt_on_tm"],
        tm_max_dev=R["tm_max_dev"],
        sign_ok=R["sign_ok"],
        sign_verdict=R["sign_verdict"],
        magnitude_verdict=R["magnitude_verdict"],
        regime_verdict=R["regime_verdict"],
        composite_verdict=verdict,
        abs_delta_OOM=R["abs_delta_OOM"],
        tau_fold=float(tau_fold),
        M_KK=float(M_KK),
    )
    print(f"  wrote {OUT_NPZ.name}")

    make_plot(R)
    print(f"  wrote {OUT_PNG.name}")
    print()

    tag = emit_4tuple(R["value"], SCHEME, CONVENTION, L_MAX)
    print(tag)

    value_payload = (
        f"delta_OOM={R['delta_OOM']:.6f};abs={R['abs_delta_OOM']:.6f};"
        f"baseline_OOM={BASELINE_OOM};f_grey={R['f_grey']:.6f};"
        f"grey_suppression_OOM={R['grey_suppression_OOM']:.6f};"
        f"integral_Gamma={R['integral_Gamma']:.6f};beta_fold_sq={R['beta_fold_sq']:.4f};"
        f"A_s_filtered={R['A_s_filtered']:.6e};kappa_exit={R['kappa']:.4f}"
    )  # (local)

    extra_rows = [
        "# regulator_pin=a_4^{Pauli-Villars} CLASS=FULL (exit-horizon barrier height = a_4 BCS condensation-energy gradient)",
        f"# greybody: f_grey={R['f_grey']:.6f} grey_suppression={R['grey_suppression_OOM']:.4f}_OOM "
        f"int_Gamma={R['integral_Gamma']:.4f} omega_max={R['omega_max']:.4f} (bounded 0<=Gamma<=1 => O(1) suppression, NOT 3.15 OOM)",
        f"# cross-checks: integral_drift(N=4000)={R['integral_drift']:.2e} transfer_matrix_max_dev={R['tm_max_dev']:.2e} "
        f"n_pairs_consistency={R['n_pairs_consistency']:.2e}",
    ]

    print_verdict_payload(
        verdict,
        value_payload,
        audit_sha,
        content_sha,
        sign_verdict=R["sign_verdict"],
        magnitude_verdict=R["magnitude_verdict"],
        regime_verdict=R["regime_verdict"],
        companion_note="greybody suppression O(1) not 3.15 OOM; ratios preserved, amplitude gap NOT closed by transmission filter",
        extra_rows=extra_rows,
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
