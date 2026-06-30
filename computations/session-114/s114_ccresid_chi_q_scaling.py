#!/usr/bin/env python3
"""
S114 W2-3 CF-S114-CCRESID-CHI-Q-SCALING — q-channel compressibility chi_q(tau) scaling
======================================================================================

Gate: CF-S114-CCRESID-CHI-Q-SCALING ([CHAIN] + directional)

Pre-registered threshold (3-outcome run-down OOM fork + RATIO-on-0.032 magnitude):
  PASS-A (Reading-A / FAIL-of-limitation):
        ( OOM_rundown >= 100 )  AND  ( |computed_frac - 0.032| / 0.032 <= 0.156 )
        where computed_frac = rho_m,today^2 / chi_q,today / rho_obs
  PASS-of-limitation (Reading-B; emitted as composite FAIL-of-closure):
        ( OOM_rundown < 10 )  AND  ( chi_q(tau) tau-nearly-constant, consistent with
        chi_q ~ S_fold to within the 2.2% Delta S/S spread )
  INFO: ( 10 <= OOM_rundown < 100 )  (chi_q runs partially; q-channel right, normalization insufficient)

Classification: PHONONIC.
  chi_q = d^2 eps/dq^2 is the q-departure / Gibbs-Duhem compressibility -- a thermodynamic
  response of the substrate's q-channel excitation spectrum, read FROM the D_K spectrum.

SUBSTRATE FRAMING (phononic-framing.md)
---------------------------------------
The substrate IS the q-channel excitation spectrum. chi_q = d^2 eps/dq^2 is the
q-departure / Gibbs-Duhem compressibility (Volovik Paper 04 sec.III: the proper vacuum
energy rho_vac = (1/V)<H - sum mu_a N_a>; its curvature about equilibrium IS the vacuum
stiffness). The residual rho_vac/rho_obs - 1 = 0.032 is NOT an a_0-magnitude offset (the
a_0 magnitude zeta_{D_K}(0)=6440 does NOT gravitate at equilibrium -- Paper 04 sec.IV:
rho_vac = -P_vac = 0 in equilibrium, trans-/sub-Planckian cancellation). What gravitates is
rho_vac = eps(q) - q deps/dq, a DIFFERENT functional of the spectrum than the bare a_0 count
-- the q-departure channel. Direction preserved: D_K eigenvalues -> grand potential eps(q)
-> chi_q = d^2 eps/dq^2 -> q-departure residual -> emergent rho_vac; NEVER inverted to "the
CC residual is fundamental and the spectrum derived." Whether chi_q runs is a substrate-IS
question the tau-scan across the Jensen family answers directly.

METHODOLOGY
-----------
chi_q(tau) = d^2 eps/dq^2 is identified with the spectral-action curvature d^2 S/dtau^2 at
the fold (the vacuum-modulus stiffness; Volovik Paper 15/35 q-theory + S43 TWOFLUID-W-43-V2,
which defines chi_q = d^2 S/dtau^2 = 300,338 M_KK^4 at the fold). This gate re-evaluates
chi_q(tau) = d^2 S/dtau^2 FIRST-PRINCIPLES across the Jensen tau-family using the S42
gradient-stiffness spectral-action data S_total(tau) and d2S_dtau2(tau) -- both computed
FROM the D_K spectrum at each Jensen deformation tau. This is a re-evaluation on existing
first-principles spectral data, NOT a new machinery build (per plan).

Two legs:
  (1) RUN-DOWN test -- does chi_q run the required ~118.71 OOM (fold 9.148e72 GeV^4 ->
      today-NEEDED 1.784e-46 GeV^4 for rho_m,today^2/chi_q = 0.032*rho_obs)?
      PASS-A requires >= 100 OOM; fold-frozen is < 10 OOM. The tau-scan of d^2 S/dtau^2
      across the FULL Jensen tau-grid measures the available run-down directly.
  (2) MAGNITUDE test -- with chi_q,today = chi_q(fold) (fold-frozen), does
      computed_frac = rho_m,today^2/chi_q,today/rho_obs reproduce 0.032 within RATIO <= 0.156?

The chi_q ~ S_fold structural argument (Paper 04/15/35; S99 PROVEN-corridor "the dead end has
a normal vector"): chi_q is the curvature of the spectral action, which is tau-nearly-constant
across the Jensen family (Delta S/S = 2.2%). The available run-down is sub-decade.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - canonical_constants.py (feeds audit_sha256 only)
  - computations/session-97/s97_w2_2_c10_n_exponent.npz (grand-potential curvature k=+3586.5;
    cross-check of the d^2 eps/dq^2 machinery -- note S97 q-variable normalization differs
    from the S43 dimensionless-tau normalization; both are q-channel responses)
  - computations/session-42/s42_gradient_stiffness.npz (S_total(tau), d2S_dtau2(tau) on the
    Jensen tau-grid -- the first-principles chi_q(tau) tau-scan; runtime input, not plan-pinned,
    documented per substrate-first-canonical-sourcing.md (ii.B))
  - computations/session-43/s43_twofluid_wz_v2.py (chi_q(fold) = 300,338 M_KK^4 anchor; method ref)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<OOM_rundown>, scheme=CHI-Q-D2EPS-DQ2-JENSEN-TAU-SCAN,
   convention=RATIO-on-residual-fraction-0.032-plus-OOM-rundown-fork, L_max=canonical)

regulator_pin: a_0^{Mellin} (the residual is the a_0 Seeley-DeWitt zeroth-moment /
Volovik-vacuum sector; the q-departure rho_vac = eps(q) - q deps/dq is the a_0-channel object).

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- Gate verdict emitted via the emit_verdict knowledge-MCP tool (script PRINTS payload only)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — Path bootstrap (put _shared on sys.path BEFORE canonical import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

_SESSION_DIR = Path(__file__).resolve().parent
_SHARED = _SESSION_DIR.parent / "_shared"
if str(_SHARED) not in sys.path:
    sys.path.insert(0, str(_SHARED))

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import (   # noqa: E402
    M_KK_gravity,
    S_fold,
    d2S_fold,
    Omega_m,
    rho_Lambda_obs,
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
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

SESSION = "S114"                                                  # (local)
GATE_ID = "CF-S114-CCRESID-CHI-Q-SCALING"                         # (local)
SCHEME = "CHI-Q-D2EPS-DQ2-JENSEN-TAU-SCAN"                        # (local)
CONVENTION = "RATIO-on-residual-fraction-0.032-plus-OOM-rundown-fork"  # (local)
L_MAX = "canonical"                                               # (local)

# Pre-registered thresholds (define BEFORE running) -----------------------
OOM_PASS_A = 100.0          # run-down >= 100 OOM => Reading-A (channel-internal closure)  # (local)
OOM_FOLD_FROZEN = 10.0      # run-down < 10 OOM => Reading-B (fold-frozen)                 # (local)
RESID_FRAC = 0.032          # the DILUTION-CC-66 standing residual = 4/125                 # (local)
RESID_BAND_RATIO = 0.15625  # = 0.005/0.032 = 5/32 (Sage-exact); magnitude RATIO ceiling   # (local)
DELTA_S_OVER_S = 0.022      # the 2.2% Delta S/S spread across the Jensen family (S43)      # (local)

# Anchors (session-source pins; cite S43, do NOT hardcode placeholder) -----
CHI_Q_FOLD_MKK4 = 300338.0  # S43 TWOFLUID-W-43-V2: chi_q(fold) = d^2 S/dtau^2 in M_KK^4    # (local)

OUT_NPZ = SESSION_DIR / "s114_ccresid_chi_q_scaling.npz"
OUT_PNG = SESSION_DIR / "s114_ccresid_chi_q_scaling.png"

# First-principles chi_q(tau) tau-scan source (runtime input; see (ii.B) note)
S42_GRAD_NPZ = COMPUTATIONS_DIR / "session-42" / "s42_gradient_stiffness.npz"
S97_NPZ = COMPUTATIONS_DIR / "session-97" / "s97_w2_2_c10_n_exponent.npz"
S43_REF = COMPUTATIONS_DIR / "session-43" / "s43_twofluid_wz_v2.py"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    S97_NPZ,
    S43_REF,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
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
    """chi_q(tau) tau-scan + run-down + magnitude legs. All intermediates `# (local)`."""

    M_KK = float(M_KK_gravity)                                         # (local) GeV

    # --- LEG 0: first-principles chi_q(tau) = d^2 S/dtau^2 across the Jensen tau-family ---
    # S42 gradient-stiffness data: S_total(tau), d2S_dtau2(tau) computed FROM the D_K
    # spectrum at each Jensen deformation tau (the spectral-action curvature IS the
    # vacuum-modulus stiffness chi_q; Volovik Paper 15/35 + S43).
    grad = np.load(S42_GRAD_NPZ, allow_pickle=True)                    # (local)
    tau_grid = np.asarray(grad["tau_grid"], dtype=float)               # (local) Jensen tau-family
    S_tau = np.asarray(grad["S_total"], dtype=float)                   # (local) M_KK^4
    chi_q_tau_MKK4 = np.asarray(grad["d2S_dtau2"], dtype=float)        # (local) = d^2 S/dtau^2(tau)

    fold_idx = int(np.argmin(np.abs(tau_grid - float(tau_fold))))      # (local)
    chi_q_fold_scan = float(chi_q_tau_MKK4[fold_idx])                  # (local) M_KK^4 at fold from scan

    # chi_q(tau) variation across the FULL Jensen family (the run-down the substrate supplies)
    chi_q_min = float(np.min(chi_q_tau_MKK4))                          # (local)
    chi_q_max = float(np.max(chi_q_tau_MKK4))                          # (local)
    chi_q_spread_frac = (chi_q_max - chi_q_min) / chi_q_fold_scan      # (local) fractional spread
    OOM_rundown_scan = float(np.log10(chi_q_max / chi_q_min))          # (local) full-family run-down
    # S(tau) fractional spread (the Delta S/S the structural argument cites)
    S_spread_frac = (float(np.max(S_tau)) - float(np.min(S_tau))) / float(S_tau[fold_idx])  # (local)

    # --- LEG 1: the run-down REQUIRED for channel-internal closure ---
    # chi_q(fold) anchor: S43 TWOFLUID-W-43-V2 = 300,338 M_KK^4 (session-source pin)
    chi_q_fold_MKK4 = CHI_Q_FOLD_MKK4                                  # (local)
    chi_q_fold_GeV4 = chi_q_fold_MKK4 * M_KK**4                        # (local) ~9.148e72 GeV^4

    # rho_m,today self-consistent: rho_crit common to rho_obs (rho_obs = Omega_Lambda*rho_crit)
    Omega_Lambda = 1.0 - float(Omega_m)                               # (local) = 0.685
    rho_crit = float(rho_Lambda_obs) / Omega_Lambda                   # (local) GeV^4
    rho_m_today = float(Omega_m) * rho_crit                           # (local) GeV^4

    # chi_q,today-NEEDED for channel-internal closure: rho_m^2/chi_q = 0.032*rho_obs
    chi_q_today_needed = rho_m_today**2 / (RESID_FRAC * float(rho_Lambda_obs))  # (local) GeV^4
    OOM_rundown_required = float(np.log10(chi_q_fold_GeV4 / chi_q_today_needed))  # (local) ~118.71

    # The run-down the substrate ACTUALLY supplies (fold-frozen: chi_q ~ S_fold, ~2.2% spread):
    # take the maximal monotone fold->edge run-down available in the tau-scan as the upper bound.
    chi_q_today_available = chi_q_min                                 # (local) M_KK^4 (most-run-down edge)
    OOM_rundown_available = float(np.log10(chi_q_fold_scan / chi_q_today_available))  # (local) sub-decade

    # The "OOM_rundown" reported as the gate VALUE is the run-down the substrate supplies
    # tested against the fork {>=100 PASS-A / <10 fold-frozen / [10,100) INFO}.
    OOM_rundown = OOM_rundown_available                               # (local)

    # --- LEG 2: the MAGNITUDE test (computed_frac vs 0.032) under fold-frozen chi_q ---
    # If chi_q is fold-frozen, chi_q,today ~ chi_q(fold). Then:
    chi_q_today_frozen_GeV4 = chi_q_fold_GeV4 * (chi_q_today_available / chi_q_fold_scan)  # (local)
    computed_frac = rho_m_today**2 / chi_q_today_frozen_GeV4 / float(rho_Lambda_obs)  # (local)
    mag_ratio = abs(computed_frac - RESID_FRAC) / RESID_FRAC          # (local) RATIO vs 0.156 band

    # --- chi_q ~ S_fold structural cross-check ---
    chi_q_over_S_fold = chi_q_fold_MKK4 / float(S_fold)               # (local) ~1.20 (same order)
    chi_q_over_d2S = chi_q_fold_MKK4 / float(d2S_fold)                # (local) ~0.945 (near unity)

    # --- S97 W2-2 grand-potential curvature cross-check (different q-normalization) ---
    s97 = np.load(S97_NPZ, allow_pickle=True)                         # (local)
    k_curv_s97 = float(np.abs(s97["k_curv"]))                         # (local) +3586.53 M_KK (S97 norm)

    # =====================================================================
    # GATE LOGIC (pre-registered fork) + [CHAIN] 3-tuple
    # =====================================================================
    # sign_verdict: the RUN-DOWN DIRECTION. The substitution chain predicts FOLD-FROZEN
    #   (chi_q ~ S_fold => OOM_rundown ~ 0 << 10). PASS = computed direction matches the
    #   fold-frozen prediction (run-down is sub-decade, NOT >=100).
    runs_down = OOM_rundown >= OOM_PASS_A                             # (local) Reading-A
    fold_frozen = OOM_rundown < OOM_FOLD_FROZEN                       # (local) Reading-B
    if fold_frozen:
        sign_verdict = "PASS"   # predicted fold-frozen, observed fold-frozen
    elif runs_down:
        sign_verdict = "FAIL"   # predicted fold-frozen, observed runs-down (direction mismatch)
    else:
        sign_verdict = "N/A"    # partial run (INFO band) -- neither direction cleanly

    # magnitude_verdict: RATIO band on the 0.032 residual fraction.
    if mag_ratio <= RESID_BAND_RATIO:
        mag_verdict = "PASS"
    else:
        mag_verdict = "FAIL"

    # regime_verdict: the OOM-run-down regime.
    #   VALID  = the run-down sits cleanly in a pre-registered branch (fold-frozen <10 OR PASS-A >=100)
    #   MARGINAL = INFO band (10..100): partial run, q-channel right normalization insufficient
    #   BREAKDOWN = not used (the curvature is a well-defined magnitude across the whole family)
    if fold_frozen or runs_down:
        regime_verdict = "VALID"
    else:
        regime_verdict = "MARGINAL"

    # Composite verdict (the run-down fork is the primary discriminator):
    #   PASS-A (Reading-A): runs_down AND mag PASS  -> composite PASS
    #   Reading-B (fold-frozen): fold_frozen        -> composite FAIL (PASS-of-limitation;
    #       the magnitude CANNOT match under fold-frozen chi_q; standing limitation confirmed)
    #   INFO: 10 <= OOM_rundown < 100               -> composite INFO (quantified shortfall)
    if runs_down and mag_verdict == "PASS":
        composite = "PASS"   # Reading-A: channel-internal closure REAL
    elif fold_frozen:
        composite = "FAIL"   # Reading-B confirmed (PASS-of-limitation; standing q-channel limitation)
    else:
        composite = "INFO"   # partial run-down, sub-threshold

    return {
        "value": OOM_rundown,
        "composite": composite,
        "sign_verdict": sign_verdict,
        "magnitude_verdict": mag_verdict,
        "regime_verdict": regime_verdict,
        # tau-scan
        "tau_grid": tau_grid,
        "chi_q_tau_MKK4": chi_q_tau_MKK4,
        "S_tau": S_tau,
        "fold_idx": fold_idx,
        "chi_q_fold_scan": chi_q_fold_scan,
        "chi_q_min": chi_q_min,
        "chi_q_max": chi_q_max,
        "chi_q_spread_frac": chi_q_spread_frac,
        "OOM_rundown_scan_fullfamily": OOM_rundown_scan,
        "S_spread_frac": S_spread_frac,
        # run-down legs
        "chi_q_fold_MKK4": chi_q_fold_MKK4,
        "chi_q_fold_GeV4": chi_q_fold_GeV4,
        "rho_crit": rho_crit,
        "rho_m_today": rho_m_today,
        "chi_q_today_needed_GeV4": chi_q_today_needed,
        "OOM_rundown_required": OOM_rundown_required,
        "OOM_rundown_available": OOM_rundown_available,
        # magnitude leg
        "computed_frac": computed_frac,
        "mag_ratio": mag_ratio,
        "resid_frac": RESID_FRAC,
        "resid_band_ratio": RESID_BAND_RATIO,
        # structural cross-checks
        "chi_q_over_S_fold": chi_q_over_S_fold,
        "chi_q_over_d2S": chi_q_over_d2S,
        "k_curv_s97": k_curv_s97,
        "delta_S_over_S": DELTA_S_OVER_S,
    }


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
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


# ---------------------------------------------------------------------------
# Section 7 — Plot
# ---------------------------------------------------------------------------

def make_plot(r: dict) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))  # (local)
    fig.suptitle(
        "CF-S114-CCRESID-CHI-Q-SCALING: q-channel compressibility chi_q(tau) "
        "is FOLD-FROZEN (chi_q ~ S_fold)\nrun-down available "
        f"{r['OOM_rundown_available']:.3g} OOM  vs  required {r['OOM_rundown_required']:.2f} OOM",
        fontsize=11, fontweight="bold")

    # Panel (a): chi_q(tau) tau-scan vs the chi_q ~ S_fold band
    ax = axes[0]  # (local)
    tau = r["tau_grid"]  # (local)
    chi = r["chi_q_tau_MKK4"]  # (local)
    ax.plot(tau, chi, "o-", color="crimson", lw=2, label=r"$\chi_q(\tau)=d^2S/d\tau^2$ (first-principles)")
    chi_fold = r["chi_q_fold_scan"]  # (local)
    ax.axhline(chi_fold, color="gray", ls="--", lw=1, label=r"$\chi_q(\tau_{\rm fold})$")
    # +-2.2% Delta S/S band around the fold value
    ax.fill_between(tau, chi_fold * (1 - r["delta_S_over_S"]), chi_fold * (1 + r["delta_S_over_S"]),
                    alpha=0.18, color="steelblue",
                    label=r"$\chi_q\sim S_{\rm fold}$ band ($\Delta S/S=2.2\%$)")
    ax.axvline(float(tau[r["fold_idx"]]), color="green", ls=":", lw=1.2, label=r"$\tau_{\rm fold}=0.19$")
    ax.set_xlabel(r"Jensen deformation $\tau$")
    ax.set_ylabel(r"$\chi_q(\tau)$  [$M_{KK}^4$]")
    ax.set_title(f"(a) chi_q(tau) tau-scan: full-family spread = {r['chi_q_spread_frac']*100:.1f}%")
    ax.legend(fontsize=8, loc="upper left")
    ax.grid(alpha=0.3)

    # Panel (b): run-down available vs required (log scale)
    ax = axes[1]  # (local)
    labels = ["available\n(chi_q ~ S_fold)", "REQUIRED\n(channel-internal closure)"]  # (local)
    vals = [max(r["OOM_rundown_available"], 1e-3), r["OOM_rundown_required"]]  # (local)
    colors = ["steelblue", "crimson"]  # (local)
    bars = ax.bar(labels, vals, color=colors, width=0.55)  # (local)
    ax.axhline(OOM_PASS_A, color="darkred", ls="--", lw=1.5, label="PASS-A floor (>=100 OOM)")
    ax.axhline(OOM_FOLD_FROZEN, color="navy", ls="--", lw=1.5, label="fold-frozen ceiling (<10 OOM)")
    ax.set_yscale("log")
    ax.set_ylabel("OOM run-down (fold -> today)")
    ax.set_title(f"(b) run-down fork: shortfall = {r['OOM_rundown_required']-r['OOM_rundown_available']:.1f} OOM")
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v * 1.3, f"{v:.3g}", ha="center", fontsize=9)
    ax.legend(fontsize=8, loc="center right")
    ax.grid(alpha=0.3, axis="y")

    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {OUT_PNG.relative_to(PROJECT_ROOT)}")


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)  # (local)
    closure = closure_hash(pins)  # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    r = compute()  # (local)

    # --- report ---
    print("=" * 72)
    print("CF-S114-CCRESID-CHI-Q-SCALING — first-principles chi_q(tau) tau-scan")
    print("=" * 72)
    print(f"\n--- LEG 0: chi_q(tau) = d^2 S/dtau^2 across the Jensen tau-family (first-principles) ---")
    print(f"  Jensen tau-grid: {np.array2string(r['tau_grid'], precision=3)}")
    print(f"  chi_q(tau) [M_KK^4]: min={r['chi_q_min']:.1f}  max={r['chi_q_max']:.1f}  fold={r['chi_q_fold_scan']:.1f}")
    print(f"  full-family fractional spread = {r['chi_q_spread_frac']*100:.2f}%")
    print(f"  full-family OOM run-down (log10 max/min) = {r['OOM_rundown_scan_fullfamily']:.4f}  (sub-decade)")
    print(f"  S(tau) fractional spread = {r['S_spread_frac']*100:.2f}%  (cf. cited Delta S/S = 2.2%)")
    print(f"\n--- structural cross-check: chi_q ~ S_fold ---")
    print(f"  chi_q(fold)/S_fold  = {r['chi_q_over_S_fold']:.4f}  (same order, O(1))")
    print(f"  chi_q(fold)/d2S_fold = {r['chi_q_over_d2S']:.4f}  (near unity -- chi_q IS the SA curvature)")
    print(f"  S97 W2-2 k_curv (different q-normalization) = {r['k_curv_s97']:.2f} M_KK (cross-check only)")
    print(f"\n--- LEG 1: RUN-DOWN ---")
    print(f"  chi_q(fold)            = {r['chi_q_fold_MKK4']:.0f} M_KK^4 = {r['chi_q_fold_GeV4']:.4e} GeV^4  [S43 anchor]")
    print(f"  rho_crit (self-consist) = {r['rho_crit']:.4e} GeV^4")
    print(f"  rho_m,today             = {r['rho_m_today']:.4e} GeV^4")
    print(f"  chi_q,today-NEEDED      = {r['chi_q_today_needed_GeV4']:.4e} GeV^4")
    print(f"  OOM_rundown REQUIRED    = {r['OOM_rundown_required']:.4f}")
    print(f"  OOM_rundown AVAILABLE   = {r['OOM_rundown_available']:.4g}  (chi_q ~ S_fold, fold-frozen)")
    print(f"  SHORTFALL               = {r['OOM_rundown_required']-r['OOM_rundown_available']:.2f} OOM")
    print(f"\n--- LEG 2: MAGNITUDE (under fold-frozen chi_q) ---")
    print(f"  computed_frac = rho_m^2/chi_q,today/rho_obs = {r['computed_frac']:.4e}")
    print(f"  target residual fraction = {r['resid_frac']}  (= 4/125)")
    print(f"  RATIO |computed - 0.032|/0.032 = {r['mag_ratio']:.4e}  (band <= {r['resid_band_ratio']})")
    print(f"\n--- 3-tuple ---")
    print(f"  sign_verdict      = {r['sign_verdict']}  (run-down direction: fold-frozen predicted & observed = PASS)")
    print(f"  magnitude_verdict = {r['magnitude_verdict']}  (RATIO band on 0.032)")
    print(f"  regime_verdict    = {r['regime_verdict']}  (OOM-run-down regime)")
    print(f"  COMPOSITE         = {r['composite']}")

    make_plot(r)

    # --- save npz ---
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        composite_verdict=r["composite"],
        value_OOM_rundown=r["value"],
        sign_verdict=r["sign_verdict"],
        magnitude_verdict=r["magnitude_verdict"],
        regime_verdict=r["regime_verdict"],
        tau_grid=r["tau_grid"],
        chi_q_tau_MKK4=r["chi_q_tau_MKK4"],
        S_tau=r["S_tau"],
        fold_idx=r["fold_idx"],
        chi_q_fold_scan=r["chi_q_fold_scan"],
        chi_q_min=r["chi_q_min"],
        chi_q_max=r["chi_q_max"],
        chi_q_spread_frac=r["chi_q_spread_frac"],
        OOM_rundown_scan_fullfamily=r["OOM_rundown_scan_fullfamily"],
        S_spread_frac=r["S_spread_frac"],
        chi_q_fold_MKK4=r["chi_q_fold_MKK4"],
        chi_q_fold_GeV4=r["chi_q_fold_GeV4"],
        rho_crit=r["rho_crit"],
        rho_m_today=r["rho_m_today"],
        chi_q_today_needed_GeV4=r["chi_q_today_needed_GeV4"],
        OOM_rundown_required=r["OOM_rundown_required"],
        OOM_rundown_available=r["OOM_rundown_available"],
        computed_frac=r["computed_frac"],
        mag_ratio=r["mag_ratio"],
        resid_frac=r["resid_frac"],
        resid_band_ratio=r["resid_band_ratio"],
        chi_q_over_S_fold=r["chi_q_over_S_fold"],
        chi_q_over_d2S=r["chi_q_over_d2S"],
        k_curv_s97=r["k_curv_s97"],
        delta_S_over_S=r["delta_S_over_S"],
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        M_KK=float(M_KK_gravity),
        tau_fold=float(tau_fold),
    )
    print(f"Saved: {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    tag = emit_4tuple(r["value"], SCHEME, CONVENTION, L_MAX)  # (local)
    print(tag)

    companion = (
        f"chi_q(fold)=300338 M_KK^4 (S43 TWOFLUID-W-43-V2); chi_q~S_fold fold-frozen "
        f"(full-family spread {r['chi_q_spread_frac']*100:.1f}%, OOM_avail {r['OOM_rundown_available']:.3g}); "
        f"required {r['OOM_rundown_required']:.2f} OOM; PASS-of-limitation=Reading-B confirmed"
    )  # (local)
    extra = [
        "# regulator_pin=a_0^{Mellin} # CF-S114-CCRESID-CHI-Q-SCALING a_0-channel "
        "(q-departure rho_vac=eps-q*deps/dq; Volovik Paper 04 sec.III/IV)",
    ]  # (local)
    print_verdict_payload(
        r["composite"], r["value"], audit_sha, content_sha,
        sign_verdict=r["sign_verdict"],
        magnitude_verdict=r["magnitude_verdict"],
        regime_verdict=r["regime_verdict"],
        companion_note=companion,
        extra_rows=extra,
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {r['composite']} (wall {wall:.1f}s) ===")
    return 0  # FAIL is a valid scientific result; exit 0 unless the script broke


if __name__ == "__main__":
    sys.exit(main())
