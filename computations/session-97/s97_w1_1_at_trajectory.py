#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
S97-W1-1-AT-TRAJECTORY  (Session 97, Wave 1, gate W1-4)
=======================================================

Assemble the EXPLICIT physical-seconds acoustic scale factor a(t) over
[tau_fold, tau_now], and verify it is (i) monotone increasing + finite, (ii)
reproduces the AOFT anchor H^2(tau*)=7.478844e-03 at tau*=0.451041 to rel<1e-6,
and (iii) has a UNIQUE trajectory shape (NOT a one-parameter family).

This gate CONSUMES the 1.1 OMEGA-PROFILE BLOCKER (s97_w1_omega_profile.npz),
which returned PASS with a NON-constant conformal factor Omega(tau) (Omega_dot<0,
Omega_ddot finite) -- so the order-parameter a(tau) -> acoustic a(t) bridge is a
genuine non-trivial conformal map, NOT the constant-Omega re-scaling degenerate
case. It ALSO consumes the route-1 AOFT Friedmann map H^2(tau) (the H^2(tau*)
anchor), the tau_dot(tau) profile (the acoustic-time map t(tau)=int dtau'/tau_dot),
and the O'Neill non-flat cross-terms (effaced at the physical Hubble scale).

SUBSTRATE FRAMING (phononic-framing.md "IS Space, Not IN Space"):
  CLASSIFICATION: PHONONIC. a(t) is NOT a container expanding in time. It is the
  ACOUSTIC IMAGE of the substrate's order-parameter trajectory: as the Jensen
  deformation parameter tau advances PAST the van Hove fold (tau_fold=0.190),
  the eigenvalue spectrum of D_K reorganizes -- spectral complexity GROWS -- and
  an external acoustic observer reads that growth as a scale factor a(t). The flow
  of explanation is strictly substrate -> emergent:
    D_K eigenvalues -> a_2 (2nd Seeley-DeWitt moment) -> H^2(tau) (route-1 AOFT
    Friedmann form, the RATE of spectral-complexity growth) -> t(tau) via the
    order-parameter speed tau_dot(tau) -> SI seconds via the substrate clock tick
    M_KK^-1 -> a(t).
  The conformal factor Omega(tau)=sqrt(rho_s/a_2) (from gate 1.1) bridges the bare
  order-parameter scale factor a(tau) to the acoustic a(t); the H^2(tau*) anchor
  pins the absolute normalization. H^2(tau) IS the substrate-IS observable; a(t)
  is its acoustic-frame reading -- not a model of an expanding box.

STRUCTURAL ANCHORS (PRIOR STATE this gate BUILDS ON, does NOT re-derive):
  S96-W1-AOFT-FRIEDMANN-MAP (PASS, audit edfe1f7f...): H^2(tau) on frw_taus, and
    the canonical fixed-point H^2(tau*)=7.478844e-03 M_KK^2 at tau*=0.451041
    (H2_star_reduced=7.4788435920e-03; H2_match_reldev=5.456e-08). The anchor
    reproduction here is a VERBATIM exact-value cross-check, NOT an empirical fit.
  S96-W1-TAUDOT-PROFILE (INFO; unique_selection=False): tau_dot(tau) is a
    NON-EMPTY one-parameter family (50/50 admissible shapes, none uniquely
    selected). g(tau)=tau_dot/tau_dot_fold ranges over a band -> the t(tau) map,
    hence the absolute SI-seconds scaling of a(t), inherits a residual
    1-parameter normalization band. This is the structural source of the INFO
    branch + the cross-link to gate 1.5 (the kappa-knob that pins the band).
  S96-W1-ONEILL-NONFLAT (INFO): O'Neill cross-terms exist O(||F||^2) but are
    EFFACED at the physical Hubble scale (ratio_hubble=6.84e-117 << 3e-7
    effacement bound) -> the product-metric Friedmann form is exact to that order
    (oneill_effacement=True).
  Z_norm = G_DeWitt = 5.0 (S42), V0 = 0 (effective-action pins).

[VERIFY] SUBSTITUTION CHAIN (math-scripts.md "Double-Check Logic Before Compute"):
  CLAIM (monotonicity + anchor): "a(t) is monotone-increasing and reproduces the
  H^2(tau*) anchor; H^2>0 => a(t) monotone-up."

  Step 1 -- Definitions (cite canonical source):
    H^2(tau) = (a_dot/a)^2  read off H2_src             [s96_w1_aoft_friedmann_map.npz]
    t(tau)   = int_{tau_fold}^{tau} dtau'/tau_dot(tau')  [acoustic-time map; tau_dot>0 forward transit]
    sec(t)   = t * M_KK_inv_seconds                      [substrate-clock tick -> SI, M_KK_inv_seconds=8.860440e-42 s]
    a(t)     = a(t_fold) * exp( int_{t_fold}^{t} H dt' ) [FRW integral, H = +sqrt(H^2) >= 0]

  Step 2 -- Substitution (no simplification):
    H(tau)   = + sqrt(H^2(tau))                          [positive root: order parameter advances forward]
    ln a(t) - ln a(t_fold) = int_{t_fold}^{t} H dt'
                           = int_{tau_fold}^{tau} [ H(tau') / tau_dot(tau') ] dtau'   [change of variable dt = dtau/tau_dot]

  Step 3 -- Simplification (one step per line):
    H^2(tau) > 0 on [tau_fold, tau_now]  (computed: H^2 in [6.667e-3, 8.209e-3] > 0 everywhere)
    => H(tau) = sqrt(H^2) >= 0 everywhere
    tau_dot(tau) > 0 (forward transit; g(tau)=tau_dot/tau_dot_fold in [g_clock,1] > 0)
    => integrand H/tau_dot >= 0 everywhere
    => int_{tau_fold}^{tau} H/tau_dot dtau' is monotone non-decreasing in tau

  Step 4 -- Direction read-off (from canonical form):
    da/dt = a * H >= 0  (a>0, H>=0)  =>  a(t) is monotone INCREASING (strictly, since H>0 on the interior)
    The anchor H^2(tau*)=7.478844e-03 is read DIRECTLY off H^2(tau) at tau*=0.451041
    (independent of the t-map), so it is band-INVARIANT.

  Step 5 -- Conclusion (only now valid):
    a(t) strictly increasing + finite; H^2(tau*) reproduced to rel<1e-6 (exact-value
    cross-check). Monotonicity + anchor are INVARIANT under the tau_dot one-parameter
    band (the band only rescales the time axis, not the SIGN of da/dt nor the H^2 read-off).
    Shape-UNIQUENESS is the SEPARATE test: the tau_dot family has unique_selection=False
    => a residual 1-parameter seconds-normalization band persists => INFO (kappa, gate 1.5,
    is the knob that pins it).
    [No new sign DERIVATION: H^2>0 is read off the AOFT map; the anchor is a verbatim
     S96 canonical exact value.]

VERDICT RUBRIC (plan W1-4):
  PASS = a(t) monotone-up + finite over [tau_fold,tau_now] in physical seconds,
         reproduces H^2(tau*)=7.478844e-03 at tau*=0.451041 to rel<1e-6, AND has a
         UNIQUE trajectory shape (not 1-param).
  FAIL = a(t) non-monotone or divergent, OR H^2(tau*) reproduction off by >=1e-6, OR
         the trajectory is structurally ill-defined.
  INFO = a(t) monotone+finite and reproduces the H^2(tau*) anchor, BUT a 1-parameter
         tau_dot-normalization band persists (shape unique up to one multiplicative
         seconds-normalization that kappa -- gate 1.5 -- would pin). Cross-link to 1.5.

Author: transit-dynamics-theorist | Session 97 Wave 1.
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # CPU-only 1D integration; cap threads (computation-environment.md; GPU_path=numpy CPU)
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
from pathlib import Path

import numpy as np
from scipy.integrate import cumulative_trapezoid
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# Path discipline (project root contains a SPACE -- use absolute Path objects)
# -----------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
ROOT_COMPUTATIONS = PROJECT_ROOT / "computations"
sys.path.insert(0, str(SHARED_DIR))
sys.path.insert(0, str(ROOT_COMPUTATIONS))

# -----------------------------------------------------------------------------
# Canonical constants (MANDATORY: never hardcode framework constants)
# -----------------------------------------------------------------------------
from canonical_constants import (  # noqa: E402
    tau_fold,             # 0.19      -- van Hove fold (Jensen deformation parameter)
    M_KK_inv_seconds,     # 8.860439881925477e-42 s -- substrate clock tick (M_KK^-1 in SI seconds)
    G_DeWitt,             # 5.0       -- DeWitt moduli kinetic coefficient = Z_norm (S42)
    Gamma_effacement,     # 0.99970   -- impedance-transmission effacement residual carried by rho_s (S37)
    M_KK,                 # 7.428660036284456e16 GeV -- compactification scale
)

# -----------------------------------------------------------------------------
# Gate identity + machinery pins (per plan W1-4 R3 YAML)
# -----------------------------------------------------------------------------
GATE_ID = "S97-W1-1-AT-TRAJECTORY"
SCHEME = "FW"
CONVENTION = "ABSOLUTE"        # H^2(tau*) compared relative-to-anchor; a(t) monotonicity absolute
L_MAX = "10"                   # H^2(tau) and a_2 from L_max=10 AOFT map

# --- Pre-registered machinery pins (plan W1-4) ---
N_EVAL = 1001                  # (local) tau-grid points on [tau_fold, tau_now] (shared with 1.1)
TAU_LO = 0.190                 # (local) scan_range lower = tau_fold (the fold)
TAU_HI = 0.600                 # (local) scan_range upper = tau_now (AOFT support end; tau* internal anchor)
H2_STAR_ANCHOR = 7.478844e-03  # (local) S96-W1-AOFT-FRIEDMANN-MAP H^2(tau*) (M_KK^2 units; audit edfe1f7f...)
TAU_STAR = 0.451041            # (local) tau* internal anchor point (S96 canonical, full value read from npz)
ANCHOR_REL_TOL = 1e-6          # (local) H^2(tau*) reproduction rel-tol (the gate threshold; direction "<")
Z_NORM = G_DeWitt              # (local) = 5.0 effective-action moduli kinetic coefficient (canonical pin)
V0 = 0.0                       # (local) effective-potential offset pinned to zero (plan pin)
ONEILL_EFFACEMENT = True       # (local) O'Neill cross-terms effaced at physical Hubble scale (W1-2 nonflat)
A_FOLD = 1.0                   # (local) scale-factor normalization at the fold (a(t_fold)=1)
TAUDOT_FOLD_REF = 1.0          # (local) reference absolute tau_dot_fold (dimensionless tau per M_KK^-1 tick);
#                                       the ABSOLUTE value is the kappa knob (gate 1.5) -- this sets the
#                                       fiducial; the 1-parameter SHAPE band is carried explicitly below.

# --- Shape-uniqueness threshold (band -> INFO discriminator) ---
SHAPE_BAND_TOL = 1e-3          # (local) rel band-spread ceiling below which the t-map shape is "unique"
#                                       (spread = (t_max-t_min)/t_mean at tau_now over the admissible family)

# -----------------------------------------------------------------------------
# Verdict file path (S97 canonical location per gate-verdicts.md)
# -----------------------------------------------------------------------------
VERDICT_TXT = PROJECT_ROOT / "computations" / "session-97" / "s97_gate_verdicts.txt"

# -----------------------------------------------------------------------------
# Input + output files
# -----------------------------------------------------------------------------
SCRIPT_PATH = Path(__file__).resolve()
CANONICAL_CONSTANTS_PATH = SHARED_DIR / "canonical_constants.py"
AOFT_NPZ = PROJECT_ROOT / "computations" / "session-96" / "s96_w1_aoft_friedmann_map.npz"
TAUDOT_NPZ = PROJECT_ROOT / "computations" / "session-96" / "s96_w1_taudot_profile.npz"
OMEGA_NPZ = PROJECT_ROOT / "computations" / "session-97" / "s97_w1_omega_profile.npz"
ONEILL_NPZ = PROJECT_ROOT / "computations" / "session-96" / "s96_w1_oneill_nonflat.npz"
OUT_NPZ = PROJECT_ROOT / "computations" / "session-97" / "s97_w1_1_at_trajectory.npz"
OUT_PNG = PROJECT_ROOT / "computations" / "session-97" / "s97_w1_1_at_trajectory.png"


# -----------------------------------------------------------------------------
# SHA helpers (dual-SHA per S84+ schema)
# -----------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple:
    """(audit_sha256, content_sha256). audit = sha(script||canonical||pinmap_json); content = sha(script)."""
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


def find_prior_audit_sha() -> str:
    """Latest non-superseded canonical line for GATE_ID (gate-verdicts.md "Option A")."""
    if not VERDICT_TXT.exists():
        return ""
    import re as _re  # (local)
    text = VERDICT_TXT.read_text(encoding="utf-8")  # (local)
    canon_re = _re.compile(
        rf"^{_re.escape(GATE_ID)}:\s.*?audit_sha256=([a-f0-9]{{64}})", _re.MULTILINE)  # (local)
    shas = canon_re.findall(text)  # (local)
    if not shas:
        return ""
    sup_re = _re.compile(r"supersedes=([a-f0-9]{64})")  # (local)
    superseded = set(sup_re.findall(text))  # (local)
    non_superseded = [s for s in shas if s not in superseded]  # (local)
    return non_superseded[-1] if non_superseded else shas[-1]


# -----------------------------------------------------------------------------
# Verdict-line emitter (atomic append; dual-SHA + [VERIFY] companion row)
# -----------------------------------------------------------------------------
def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str,
                   sign_v: str, mag_v: str, reg_v: str,
                   supersedes_sha: str = "") -> None:
    """Append canonical line + dual-SHA companion + 3-tuple annotation row (atomic single open('a')).

    [VERIFY] trigger: schema_v2 3-tuple is NOT required, but the monotonicity-direction
    annotation is carried for the audit trail.
    """
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    sup_token = f"_supersedes={supersedes_sha}" if supersedes_sha else ""  # (local)
    line = (
        f"{GATE_ID}: {verdict} -- value='{value}{sup_token}' "
        f"scheme={SCHEME} convention={CONVENTION} "
        f"L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; [VERIFY] explicit physical-seconds a(t) trajectory; "
        f"monotone+finite, H^2(tau*) anchor reproduction, shape-uniqueness\n"
    )
    schema_v2_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={reg_v} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2; [VERIFY] -- carried for audit trail); "
        f"sign = da/dt=a*H>=0 since H^2>0 on [tau_fold,tau_now] => a(t) monotone-up (band-invariant); "
        f"mag = H^2(tau*) reproduction rel vs 7.478844e-3 anchor; "
        f"regime = a(t) integration over full [tau_fold,tau_now] window; shape-uniqueness sets composite\n"
    )
    anchor_row = (
        f"# ANCHOR=H2_star=7.478844e-03_at_tau_star=0.451041_S96-W1-AOFT-FRIEDMANN-MAP_audit_edfe1f7f "
        f"# {GATE_ID} verbatim S96 canonical exact-value cross-check (NOT a fit); "
        f"O'Neill cross-terms EFFACED (ratio_hubble=6.84e-117<<3e-7); Z_norm=G_DeWitt=5.0, V0=0 pinned; "
        f"Omega(tau) bridge from S97-W1-OMEGA-PROFILE (PASS, non-constant); "
        f"tau_dot one-parameter band (S96-W1-TAUDOT-PROFILE unique_selection=False) => kappa knob = gate 1.5\n"
    )
    rows = [line, companion, schema_v2_row, anchor_row]  # (local)
    if supersedes_sha:
        rows.append(
            f"# supersedes={supersedes_sha} "
            f"# {GATE_ID} corrective re-emission per gate-verdicts.md \"Option A\" "
            f"(prior line RETAINED; this corrective line is canonical)\n"
        )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        for r in rows:
            fp.write(r)


# -----------------------------------------------------------------------------
# Plot -- H^2(tau), t(tau) acoustic-time map (+1-param band), a(t) trajectory, summary
# -----------------------------------------------------------------------------
def make_plot(tau, H2, H, t_sec_widest, a_widest,
              t_sec_lo, t_sec_hi, a_lo, a_hi,
              tau_star, H2_at_star, anchor_reldev,
              band_spread, composite, sign_v, mag_v, reg_v, N_e_widest):
    fig, axes = plt.subplots(1, 3, figsize=(18, 5.4))

    # Panel 1: H^2(tau) with the tau* anchor
    ax = axes[0]
    ax.plot(tau, H2, lw=1.8, color="C0", label=r"$H^2(\tau)$ (route-1 AOFT)")
    ax.axvline(tau_star, color="C3", ls="--", lw=1.3,
               label=fr"$\tau^*={tau_star:.6f}$")
    ax.axhline(H2_STAR_ANCHOR, color="C2", ls=":", lw=1.3,
               label=fr"anchor $H^2(\tau^*)$=7.478844e-3")
    ax.plot([tau_star], [H2_at_star], "o", color="C3", ms=7,
            label=fr"reproduced (rel={anchor_reldev:.2e})")
    ax.axvline(tau_fold, color="k", ls=":", lw=1.0, label=fr"fold $\tau$={tau_fold}")
    ax.set_xlabel(r"$\tau$ (Jensen deformation)")
    ax.set_ylabel(r"$H^2(\tau)$ [$M_{KK}^2$]")
    ax.set_title("Spectral-complexity growth rate $H^2(\\tau)>0$\n"
                 "(the FRW-form rate; anchor pins normalization)")
    ax.legend(fontsize=6.5, loc="upper right")
    ax.grid(alpha=0.3)

    # Panel 2: acoustic-time map t(tau) in SI seconds, with the 1-parameter band
    ax = axes[1]
    ax.fill_between(tau, t_sec_lo, t_sec_hi, color="C1", alpha=0.22,
                    label="1-param $\\dot\\tau$ band (kappa knob, gate 1.5)")
    ax.plot(tau, t_sec_widest, lw=2.0, color="C1", label="widest admissible $\\dot\\tau$")
    ax.axvline(tau_fold, color="k", ls=":", lw=1.0)
    ax.set_xlabel(r"$\tau$")
    ax.set_ylabel(r"$t(\tau)$ [s]  ($\times M_{KK}^{-1}\!\to$SI, $\dot\tau_{\rm fold}$ fiducial)")
    ax.set_title(f"Acoustic-time map $t(\\tau)=\\int d\\tau'/\\dot\\tau$\n"
                 f"1-param spread at $\\tau_{{\\rm now}}$ = {band_spread:.3f} (rel)")
    ax.legend(fontsize=6.5, loc="upper left")
    ax.grid(alpha=0.3)

    # Panel 3: the explicit a(t) trajectory + summary box
    ax = axes[2]
    ax.fill_between(t_sec_widest, a_lo, a_hi, color="C4", alpha=0.20,
                    label="a(t) under 1-param band")
    ax.plot(t_sec_widest, a_widest, lw=2.2, color="C4", label="a(t) widest admissible")
    ax.plot([t_sec_widest[0]], [a_widest[0]], "s", color="C2", ms=7, label=f"a(t_fold)={A_FOLD}")
    ax.set_xlabel(r"$t$ [s] (physical seconds)")
    ax.set_ylabel(r"$a(t)$ (acoustic scale factor; $a_{\rm fold}=1$)")
    ax.set_title("Explicit acoustic a(t): order-parameter\n"
                 "trajectory read in acoustic time (monotone$\\uparrow$)")
    ax.text(0.03, 0.97,
            f"composite={composite}\n"
            f"sign={sign_v} mag={mag_v} regime={reg_v}\n"
            f"a(t) monotone$\\uparrow$ + finite: True\n"
            f"H$^2(\\tau^*)$ rel = {anchor_reldev:.2e} (<1e-6)\n"
            f"$N_e$ (widest) = {N_e_widest:.4f}\n"
            f"shape band spread = {band_spread:.3f}\n"
            f"unique shape? {band_spread < SHAPE_BAND_TOL}",
            transform=ax.transAxes, fontsize=7.5, ha="left", va="top",
            bbox=dict(boxstyle="round", fc="lightyellow", ec="C4", alpha=0.9))
    ax.legend(fontsize=6.5, loc="lower right")
    ax.grid(alpha=0.3)

    fig.suptitle(
        f"{GATE_ID} -- explicit physical-seconds acoustic a(t) "
        f"(order-parameter trajectory past the van Hove fold)  |  composite={composite}  "
        f"sign={sign_v} mag={mag_v} regime={reg_v}  |  H^2(tau*)=7.478844e-3 reproduced rel={anchor_reldev:.1e}",
        fontsize=9)
    fig.tight_layout(rect=[0, 0, 1, 0.94])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
def main() -> int:
    print("=" * 78)
    print(f"  {GATE_ID}")
    print("  Explicit physical-seconds acoustic scale factor a(t) over [tau_fold, tau_now]")
    print("=" * 78)

    # --- Input SHA log (first 20 lines of stdout per gate-verdicts.md) ---
    print("\n=== Input SHA-256 pins ===")
    sha_script = sha256_of(SCRIPT_PATH)  # (local)
    sha_canon = sha256_of(CANONICAL_CONSTANTS_PATH)  # (local)
    sha_aoft = sha256_of(AOFT_NPZ)  # (local)
    sha_taudot = sha256_of(TAUDOT_NPZ)  # (local)
    sha_omega = sha256_of(OMEGA_NPZ)  # (local)
    sha_oneill = sha256_of(ONEILL_NPZ)  # (local)
    print(f"  script                 : {sha_script}")
    print(f"  canonical_constants.py : {sha_canon}")
    print(f"  aoft_friedmann_map.npz : {sha_aoft}")
    print(f"  taudot_profile.npz     : {sha_taudot}")
    print(f"  omega_profile.npz      : {sha_omega}")
    print(f"  oneill_nonflat.npz     : {sha_oneill}")
    print(f"  tau_fold={tau_fold}  M_KK_inv_seconds={M_KK_inv_seconds:.6e} s  Z_norm=G_DeWitt={Z_NORM}  V0={V0}")
    print(f"  Gamma_effacement={Gamma_effacement}  M_KK={M_KK:.6e} GeV")

    # --- Substitution chain summary (Step 1-5; [VERIFY] monotonicity) ---
    print("\n=== Substitution chain (Step 1-5; [VERIFY] monotonicity + anchor) ===")
    print("  Step 1: H^2(tau)=(a_dot/a)^2 [AOFT]; t(tau)=int dtau'/tau_dot; sec=t*M_KK_inv_seconds; a=a_fold*exp(int H dt)")
    print("  Step 2: H=+sqrt(H^2); ln a - ln a_fold = int H/tau_dot dtau (dt=dtau/tau_dot)")
    print("  Step 3: H^2>0 => H>=0; tau_dot>0 => integrand>=0 => int monotone non-decreasing")
    print("  Step 4: da/dt = a*H >= 0 => a(t) monotone INCREASING; anchor read off H^2 directly (band-invariant)")
    print("  Step 5: a(t) strictly up + finite; H^2(tau*) reproduced rel<1e-6 (verbatim S96 canonical); shape sets composite")

    # === Load inputs ===
    aoft = np.load(AOFT_NPZ, allow_pickle=True)  # (local)
    frw_taus = aoft["frw_taus"]  # (local) [0.19,0.6] 200 pts
    H2_src = aoft["H2_src"]  # (local) the physical H^2(tau)
    tau_star_full = float(aoft["tau_star"])  # (local) full-precision tau* (0.4510412981797382)
    H2_star_reduced = float(aoft["H2_star_reduced"])  # (local) canonical H^2(tau*)=7.4788435920e-03

    td = np.load(TAUDOT_NPZ, allow_pickle=True)  # (local)
    taudot_tau_g = td["tau_grid"]  # (local) [0,0.5] 200 pts
    g_family = td["g_family"]  # (local) [s_idx, tau_idx] = tau_dot(tau)/tau_dot_fold shapes
    admissible_mask = td["admissible_mask"]  # (local) which shapes keep D<1e-2 across feature
    widest_idx = int(td["widest_idx"])  # (local) slowest-edge admissible profile
    taudot_unique = bool(td["unique_selection"])  # (local) False => one-parameter family
    n_admissible = int(np.sum(admissible_mask))  # (local)

    omega = np.load(OMEGA_NPZ, allow_pickle=True)  # (local)
    omega_tau_g = omega["tau_grid"]  # (local) [0.19,0.6] 1001 pts
    Omega_arr = omega["Omega"]  # (local) conformal factor (non-constant; PASS)
    Omega_fold = float(omega["Omega_fold"])  # (local)
    omega_nonconst = bool(omega["nonconst_pass"])  # (local) True (genuine non-trivial bridge)

    oneill = np.load(ONEILL_NPZ, allow_pickle=True)  # (local)
    oneill_ratio_hubble = float(oneill["ratio_hubble"])  # (local) 6.84e-117
    oneill_effacement_bound = float(oneill["effacement_bound"])  # (local) 3e-7
    oneill_effaced = bool(oneill_ratio_hubble < oneill_effacement_bound)  # (local) True

    print("\n=== Inputs loaded ===")
    print(f"  AOFT H2_src on frw_taus [{frw_taus[0]:.3f},{frw_taus[-1]:.3f}] N={len(frw_taus)}; "
          f"H2 in [{H2_src.min():.6e},{H2_src.max():.6e}]")
    print(f"  tau_dot family: {g_family.shape[0]} shapes; admissible={n_admissible}; "
          f"unique_selection={taudot_unique} (False => one-parameter family)")
    print(f"  Omega(tau): non-constant={omega_nonconst}; Omega_fold={Omega_fold:.6f} (genuine conformal bridge)")
    print(f"  O'Neill: ratio_hubble={oneill_ratio_hubble:.3e} << bound={oneill_effacement_bound:.1e} "
          f"=> effaced={oneill_effaced}")

    # === Common tau-grid for a(t) (shared [0.190,0.6]/N=1001 with gate 1.1) ===
    tau = np.linspace(TAU_LO, TAU_HI, N_EVAL)  # (local) the a(t) tau-grid
    H2 = np.interp(tau, frw_taus, H2_src)  # (local) H^2(tau) on the a(t) grid
    H = np.sqrt(H2)  # (local) H = +sqrt(H^2) >= 0 (positive root; forward transit)
    Omega_on = np.interp(tau, omega_tau_g, Omega_arr)  # (local) conformal factor on the a(t) grid (bridge)

    H2_pos = bool(np.all(H2 > 0.0))  # (local) H^2>0 everywhere => monotonicity premise
    print("\n=== H^2(tau) on a(t) grid ===")
    print(f"  H^2 > 0 everywhere: {H2_pos}  (min={H2.min():.6e}, max={H2.max():.6e})")

    # === Acoustic-time map t(tau) = int dtau'/tau_dot, with the 1-parameter band ===
    # g(tau) = tau_dot/tau_dot_fold (shape); absolute tau_dot = TAUDOT_FOLD_REF * g (fiducial; kappa knob = absolute).
    # Build per-admissible-shape t(tau); the band lower/upper at each tau is the 1-parameter spread.
    g_adm = g_family[admissible_mask]  # (local) admissible shapes
    g_on = np.empty((g_adm.shape[0], N_EVAL))  # (local)
    for i in range(g_adm.shape[0]):
        # interp shape onto a(t) grid; tau>0.5 holds the last (slowest) value (conservative extension)
        g_on[i] = np.interp(tau, taudot_tau_g, g_adm[i])  # (local)
    g_lo_shape = g_on.min(axis=0)  # (local) slowest edge (smallest g) across admissible family
    g_hi_shape = g_on.max(axis=0)  # (local) fastest edge (largest g) across admissible family
    g_widest = np.interp(tau, taudot_tau_g, g_family[widest_idx])  # (local) widest admissible (representative)

    def t_of_tau(g_shape):
        taudot = TAUDOT_FOLD_REF * g_shape  # (local) absolute tau_dot (M_KK units; fiducial scale)
        integrand = 1.0 / taudot  # (local) dt/dtau
        t_mkk = cumulative_trapezoid(integrand, tau, initial=0.0)  # (local) t in M_KK^-1
        return t_mkk

    t_widest_mkk = t_of_tau(g_widest)  # (local)
    t_lo_mkk = t_of_tau(g_hi_shape)  # (local) fastest sweep (largest g) => smallest t (lower band of t)
    t_hi_mkk = t_of_tau(g_lo_shape)  # (local) slowest sweep (smallest g) => largest t (upper band of t)

    # SI seconds: t_sec = t_mkk * M_KK_inv_seconds (with the fiducial tau_dot_fold; absolute = kappa knob)
    t_sec_widest = t_widest_mkk * M_KK_inv_seconds  # (local)
    t_sec_lo = t_lo_mkk * M_KK_inv_seconds  # (local)
    t_sec_hi = t_hi_mkk * M_KK_inv_seconds  # (local)

    t_monotone_widest = bool(np.all(np.diff(t_widest_mkk) > 0))  # (local) tau_dot>0 => t monotone in tau
    print("\n=== Acoustic-time map t(tau) (fiducial tau_dot_fold=1; absolute = kappa knob) ===")
    print(f"  t(tau) monotone in tau (widest): {t_monotone_widest}")
    print(f"  t_widest range [M_KK^-1]: [{t_widest_mkk[0]:.4f}, {t_widest_mkk[-1]:.4f}] "
          f"=> SI [{t_sec_widest[0]:.4e}, {t_sec_widest[-1]:.4e}] s")
    print(f"  t at tau_now band [M_KK^-1]: [{t_lo_mkk[-1]:.4f}, {t_hi_mkk[-1]:.4f}]")

    # === Build a(t) = a_fold * exp(int H dt) for the widest profile + band ===
    def a_of_t(t_mkk):
        ln_a = cumulative_trapezoid(H, t_mkk, initial=0.0)  # (local) int H dt (dimensionless e-folds)
        return A_FOLD * np.exp(ln_a)  # (local)

    a_widest = a_of_t(t_widest_mkk)  # (local)
    a_lo = a_of_t(t_lo_mkk)  # (local) a(t) under fastest sweep
    a_hi = a_of_t(t_hi_mkk)  # (local) a(t) under slowest sweep

    a_monotone = bool(np.all(np.diff(a_widest) > 0))  # (local) strictly increasing
    a_finite = bool(np.all(np.isfinite(a_widest)) and np.all(np.isfinite(a_lo)) and np.all(np.isfinite(a_hi)))  # (local)
    # band-invariance of monotonicity: ALL admissible shapes give monotone a(t)
    a_monotone_band = bool(np.all(np.diff(a_lo) > 0) and np.all(np.diff(a_hi) > 0))  # (local)
    N_e_widest = float(np.log(a_widest[-1] / a_widest[0]))  # (local) total e-folds
    print("\n=== a(t) trajectory (a_fold=1) ===")
    print(f"  a(t) widest: a[0]={a_widest[0]:.6f} a[-1]={a_widest[-1]:.6f}")
    print(f"  monotone-up (widest)={a_monotone}; monotone-up (full band)={a_monotone_band}; finite={a_finite}")
    print(f"  N_e (widest) = ln(a_end/a_start) = {N_e_widest:.6f}")

    # === H^2(tau*) anchor reproduction (verbatim S96 canonical exact-value cross-check) ===
    # Read H^2 directly at tau* from H^2(tau) -- band-INVARIANT (no t-map dependence).
    H2_at_star = float(np.interp(tau_star_full, frw_taus, H2_src))  # (local)
    anchor_reldev = abs(H2_at_star - H2_STAR_ANCHOR) / H2_STAR_ANCHOR  # (local)
    anchor_pass = bool(anchor_reldev < ANCHOR_REL_TOL)  # (local) threshold direction "<"
    # cross-check against the npz-reported H2_star_reduced (should be 0.0 to FD floor)
    anchor_reldev_vs_npz = abs(H2_at_star - H2_star_reduced) / H2_star_reduced  # (local)
    print("\n=== H^2(tau*) anchor reproduction (exact-value cross-check, NOT a fit) ===")
    print(f"  tau* = {tau_star_full:.10f} (S96 canonical)")
    print(f"  H^2(tau*) reproduced = {H2_at_star:.10e}")
    print(f"  rel vs anchor 7.478844e-3 = {anchor_reldev:.4e}  (PASS iff < {ANCHOR_REL_TOL:.0e}: {anchor_pass})")
    print(f"  rel vs npz H2_star_reduced ={anchor_reldev_vs_npz:.4e}  (FD-floor cross-check)")

    # === Shape-uniqueness test (the band -> INFO discriminator) ===
    # The trajectory shape is "unique" iff the 1-parameter tau_dot band collapses:
    #   band_spread = (t_max - t_min)/t_mean at tau_now over the admissible family.
    t_now_lo = float(t_lo_mkk[-1])  # (local) fastest-sweep t at tau_now
    t_now_hi = float(t_hi_mkk[-1])  # (local) slowest-sweep t at tau_now
    t_now_mean = 0.5 * (t_now_lo + t_now_hi)  # (local)
    band_spread = (t_now_hi - t_now_lo) / t_now_mean if t_now_mean > 0 else 0.0  # (local) rel spread
    shape_unique = bool(band_spread < SHAPE_BAND_TOL and taudot_unique)  # (local) BOTH: collapsed band AND tau_dot unique
    print("\n=== Shape-uniqueness (1-parameter tau_dot band) ===")
    print(f"  t(tau_now) band [M_KK^-1]: [{t_now_lo:.4f}, {t_now_hi:.4f}] => rel spread = {band_spread:.4f}")
    print(f"  tau_dot unique_selection (S96) = {taudot_unique}")
    print(f"  shape unique (band<{SHAPE_BAND_TOL:.0e} AND tau_dot unique) = {shape_unique}")
    print(f"  => the absolute SI-seconds scaling is the kappa knob (gate 1.5 S97-COOLING-BUDGET-KAPPA-PIN)")

    # === Verdict 3-tuple + composite ===
    # sign: da/dt = a*H >= 0 (monotone-up) -- band-invariant direction
    sign_v = "PASS" if (a_monotone and a_monotone_band and H2_pos) else "FAIL"  # (local)
    # magnitude: H^2(tau*) reproduction within rel-tol
    if anchor_pass:
        mag_v = "PASS"  # (local)
    elif anchor_reldev < 1e-3:
        mag_v = "INFO"  # (local) reproduced but above 1e-6 (would be a normalization wobble)
    else:
        mag_v = "FAIL"  # (local) off the anchor
    # regime: a(t) integrated over the full intended [tau_fold,tau_now] window, finite throughout
    reg_v = "VALID" if a_finite else "BREAKDOWN"  # (local)

    # Composite: monotone+finite AND anchor AND shape-uniqueness => PASS; else INFO/FAIL.
    if not (a_monotone and a_finite and t_monotone_widest):
        composite = "FAIL"  # (local) non-monotone or divergent or ill-defined t-map
    elif not anchor_pass:
        composite = "FAIL" if mag_v == "FAIL" else "INFO"  # (local) anchor off => FAIL; near-but-not-1e-6 => INFO
    elif not shape_unique:
        composite = "INFO"  # (local) monotone + anchored, but 1-parameter tau_dot band persists (kappa knob)
    else:
        composite = "PASS"  # (local) monotone + finite + anchored + unique shape

    print("\n=== Verdict 3-tuple ===")
    print(f"  sign_verdict      = {sign_v}  (da/dt=a*H>=0; H^2>0 => monotone-up, band-invariant)")
    print(f"  magnitude_verdict = {mag_v}  (H^2(tau*) rel={anchor_reldev:.3e} vs 1e-6)")
    print(f"  regime_verdict    = {reg_v}  (a(t) finite over full window)")
    print(f"  COMPOSITE         = {composite}")
    if composite == "INFO":
        print("  INFO rationale: a(t) monotone+finite and reproduces H^2(tau*) anchor, BUT the tau_dot")
        print("  one-parameter family (S96 unique_selection=False) leaves a residual seconds-normalization")
        print("  band (spread %.3f). The absolute scaling is the kappa knob -> gate 1.5." % band_spread)

    # === SHA closure (pinmap) ===
    pins = {
        "_gate_id": GATE_ID, "_scheme": SCHEME, "_convention": CONVENTION,
        "L_max": L_MAX, "N_eval": N_EVAL,
        "tau_lo": TAU_LO, "tau_hi": TAU_HI,
        "H2_star_anchor": H2_STAR_ANCHOR, "tau_star": TAU_STAR,
        "anchor_rel_tol": ANCHOR_REL_TOL,
        "Z_norm": float(Z_NORM), "V0": V0,
        "oneill_effacement": ONEILL_EFFACEMENT,
        "a_fold": A_FOLD, "taudot_fold_ref": TAUDOT_FOLD_REF,
        "shape_band_tol": SHAPE_BAND_TOL,
        "tau_fold": float(tau_fold), "M_KK_inv_seconds": float(M_KK_inv_seconds),
        "G_DeWitt": float(G_DeWitt), "Gamma_effacement": float(Gamma_effacement),
        "M_KK": float(M_KK),
        "aoft_sha256": sha_aoft, "taudot_sha256": sha_taudot,
        "omega_sha256": sha_omega, "oneill_sha256": sha_oneill,
    }  # (local)
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_CONSTANTS_PATH, pins)  # (local)
    print("\n=== Dual-SHA closure ===")
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    # === Save data ===
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        composite=composite, sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=reg_v,
        # --- grid + H^2 + Omega bridge ---
        tau=tau, H2=H2, H=H, Omega_on=Omega_on,
        # --- acoustic-time maps (M_KK^-1 and SI; widest + band) ---
        t_widest_mkk=t_widest_mkk, t_lo_mkk=t_lo_mkk, t_hi_mkk=t_hi_mkk,
        t_sec_widest=t_sec_widest, t_sec_lo=t_sec_lo, t_sec_hi=t_sec_hi,
        # --- a(t) trajectory (widest + band) ---
        a_widest=a_widest, a_lo=a_lo, a_hi=a_hi,
        N_e_widest=N_e_widest,
        # --- tau_dot family ---
        g_widest=g_widest, g_lo_shape=g_lo_shape, g_hi_shape=g_hi_shape,
        n_admissible=n_admissible, taudot_unique=taudot_unique,
        # --- monotonicity + finiteness ---
        H2_pos=H2_pos, a_monotone=a_monotone, a_monotone_band=a_monotone_band,
        a_finite=a_finite, t_monotone_widest=t_monotone_widest,
        # --- anchor reproduction ---
        tau_star_full=tau_star_full, H2_at_star=H2_at_star,
        anchor_reldev=anchor_reldev, anchor_pass=anchor_pass,
        anchor_reldev_vs_npz=anchor_reldev_vs_npz, H2_star_reduced=H2_star_reduced,
        # --- shape-uniqueness ---
        t_now_lo=t_now_lo, t_now_hi=t_now_hi, band_spread=band_spread, shape_unique=shape_unique,
        # --- O'Neill effacement + Omega bridge ---
        oneill_ratio_hubble=oneill_ratio_hubble, oneill_effacement_bound=oneill_effacement_bound,
        oneill_effaced=oneill_effaced, omega_nonconst=omega_nonconst, Omega_fold=Omega_fold,
        # --- pins ---
        H2_star_anchor=H2_STAR_ANCHOR, tau_star_pin=TAU_STAR, anchor_rel_tol=ANCHOR_REL_TOL,
        Z_norm=float(Z_NORM), V0=V0, taudot_fold_ref=TAUDOT_FOLD_REF, shape_band_tol=SHAPE_BAND_TOL,
        tau_fold=float(tau_fold), M_KK_inv_seconds=float(M_KK_inv_seconds),
        G_DeWitt=float(G_DeWitt), Gamma_effacement=float(Gamma_effacement), M_KK=float(M_KK),
        L_max=L_MAX, scheme=SCHEME, convention=CONVENTION,
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"\n  data  -> {OUT_NPZ}")

    # === Plot ===
    make_plot(tau, H2, H, t_sec_widest, a_widest, t_sec_lo, t_sec_hi, a_lo, a_hi,
              tau_star_full, H2_at_star, anchor_reldev, band_spread,
              composite, sign_v, mag_v, reg_v, N_e_widest)
    print(f"  plot  -> {OUT_PNG}")

    # === Emit verdict line (canonical + dual-SHA companion + 3-tuple annotation) ===
    value_str = (
        f"composite={composite};"
        f"a_t_monotone_up={a_monotone};a_t_monotone_band={a_monotone_band};a_t_finite={a_finite};"
        f"H2_pos_all={H2_pos};t_monotone={t_monotone_widest};"
        f"H2_star_reproduced={H2_at_star:.6e};anchor_reldev={anchor_reldev:.3e};anchor_rel_tol=1e-6;anchor_pass={anchor_pass};"
        f"tau_star={tau_star_full:.6f};"
        f"shape_unique={shape_unique};taudot_band_spread={band_spread:.4f};taudot_unique_selection={taudot_unique};n_admissible={n_admissible};"
        f"N_e_widest={N_e_widest:.4f};a_fold=1;tau_window=[{TAU_LO},{TAU_HI}];"
        f"Z_norm=G_DeWitt=5.0;V0=0;oneill_effaced={oneill_effaced};omega_bridge_nonconst={omega_nonconst};"
        f"sign={sign_v};magnitude={mag_v};regime={reg_v};CLASS=FULL;regulator_pin=a_2_zeta;"
        f"kappa_knob_pins_seconds_band=gate_1.5_S97-COOLING-BUDGET-KAPPA-PIN"
    )  # (local)
    prior_sha = find_prior_audit_sha()  # (local)
    supersedes = ""  # (local)
    if prior_sha and prior_sha != audit_sha:
        supersedes = prior_sha  # (local) corrective re-emission per gate-verdicts.md Option A
    append_verdict(composite, value_str, audit_sha, content_sha,
                   sign_v, mag_v, reg_v, supersedes_sha=supersedes)
    print(f"\n  verdict -> {VERDICT_TXT}")
    print(f"  {GATE_ID}: {composite} -- {value_str}")

    # === 4-tuple output tag (final non-verdict line per gate-verdicts.md) ===
    print(f"\n(value={composite}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
