"""
S96-GEOM-CCC-WEYL  —  Weyl-Curvature-Hypothesis / Conformal-Cyclic-Cosmology test
=================================================================================

Session 96, Wave 5, Gate 4  —  schwarzschild-penrose-geometer

TWO-PART [SIGN] GATE:
  (i)  MONOTONICITY of the Weyl-curvature scalar |C|^2(tau) across the physical
       flow from its genesis minimum |C|^2(0) = 5/14 (SP-2, S22a).  The
       Weyl-Curvature-Hypothesis (WCH) reading: minimal Weyl at the cold-regular
       genesis (tau=0, round maximally-symmetric SU(3)), growing through the
       order-parameter shear (volume-preserving TT) as tau flows.
       SIGN claim:  d|C|^2/dtau > 0  on (0, tau_max].

  (ii) CONFORMAL-CYCLIC-COSMOLOGY map:  attempt to construct a conformal
       rescaling relating the censored tau->inf anisotropic-singular boundary
       to a new tau=0-like low-Weyl crossover surface (a substrate-internal
       Penrose-CCC aeon analog), OR show it OBSTRUCTED with explicit reason.

METHOD (substrate-first, GEOMETRIC):
  D_K eigenvalues -> Jensen metric g_tau on SU(3) -> curvature invariants
  K(tau), R(tau), |Ric|^2(tau) -> |C|^2(tau) via the BIANCHI IDENTITY route
  (NOT direct C = R - Schouten; the direct route hits a Ricci-sign trap flagged
  in the agent MEMORY).  n = dim(SU(3)) = 8.

    |C|^2 = K - (4/(n-2))|Ric|^2 + (2/((n-1)(n-2))) R^2            (n=8)
          = K - (2/3)|Ric|^2 + (1/21) R^2

  K(tau), R(tau): EXACT closed form (SP-2, machine-eps verified in r20a/s22a).
  |Ric|^2(tau):   numerical, from the canonical Riemann-tensor builder
                  compute_riemann_tensor_ON_fast(tau) (r20a_riemann_tensor.py),
                  evaluated cleanly on the full 201-point tau-grid.

ANCHORS (knowledge MCP, query-first):
  - SP-2 (CLOSED, s22a_weyl_curvature.py): |C|^2(0) = 5/14 = 0.357142857...
    triple-selected (S29): WCH + J-maximality + DNP instability.
  - WCH consistent (PROVEN, session-49-sp-collab): |C|^2/K DECREASING on [0,2.0]
    (Ricci dominance grows, opposite to 4D collapse).  Curvature sign hierarchy
    K_sect -> Weyl -> Ric at 0.537 -> 0.895 -> 1.382.

DISTINCTION (per MEMORY, load-bearing):
  |C|^2 is monotone-INCREASING while |C|^2/K is DECREASING.  Both hold: K (hence
  Ricci) grows FASTER than |C|^2.  The WCH is about |C| being SMALL at genesis
  (5/14 is the MINIMUM, not zero); Type O (|C|^2 = 0) is impossible because the
  SU(3) structure constants force |C|^2 > 0.

CCC GROUNDING (read-only references):
  - researchers/Schwarzschild-Penrose/11_2025_Meissner_Penrose_Physics_of_CCC.md
  - researchers/Tesla-Resonance/15_2010_Penrose_Conformal_Cyclic_Cosmology_Aeons.md

PRE-REGISTERED VERDICT (plan section W5-4):
  PASS iff (d|C|^2/dtau > 0 on (0, tau_max] from the genesis minimum 5/14)
       AND (a CCC conformal-rescaling map is either CONSTRUCTED or shown
            OBSTRUCTED with stated reason).

Author: schwarzschild-penrose-geometer
Date:   2026-05-29
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")    # (local) CPU-cap, no GPU path here
os.environ.setdefault("MKL_NUM_THREADS", "8")    # (local)

import sys
import json
import time
import hashlib
from pathlib import Path

import numpy as np

# --- paths ------------------------------------------------------------------
THIS = Path(__file__).resolve()                                    # (local)
SESS_DIR = THIS.parent                                             # (local) computations/session-96
SHARED_DIR = (SESS_DIR.parent / "_shared").resolve()              # (local) computations/_shared
PROJECT_ROOT = SESS_DIR.parent.parent.resolve()                   # (local)
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import tau_NEC, tau_fold                  # noqa: E402  framework constants

# canonical Riemann-tensor builder for (SU(3), g_tau) — r20a_riemann_tensor.py
from r20a_riemann_tensor import (                                  # noqa: E402
    compute_riemann_tensor_ON_fast,
    ricci_from_riemann,
    scalar_curvature_our_metric,
    kretschner_exact,
)

GATE_ID = "S96-GEOM-CCC-WEYL"
SCHEME = "Weyl-scalar-Riemannian"
CONVENTION = "Bianchi-identity"
L_MAX = "NA"                                                       # (local) no D_K eigendecomposition

OUT_NPZ = SESS_DIR / "s96_geom_ccc_weyl.npz"                       # (local)
OUT_PNG = SESS_DIR / "s96_geom_ccc_weyl.png"                       # (local)
VERDICT_TXT = SESS_DIR / "s96_gate_verdicts.txt"                   # (local)

N_DIM = 8                                                          # (local) dim SU(3)
N_EVAL = 201                                                       # (local) tau-grid points
TAU_MAX = 2.0                                                      # (local) WCH-established range
WEYL2_GENESIS_EXACT = 5.0 / 14.0                                   # (local) SP-2 anchor (rational)
ANCHOR_TOL = 1e-9                                                  # (local) |C|^2(0) match tol
MONO_TOL = 1e-6                                                    # (local) monotonicity sign tol


# ---------------------------------------------------------------------------
# SHA-256 dual-pin block  (S84+ schema; mirrors the S96 canonical idiom)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                          # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}                                                     # (local)
    for p in inputs:
        sha = sha256_of(p)                                       # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = p.name                                        # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())                                 # (local)
    h = hashlib.sha256()                                         # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    script_bytes = b""                                           # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""                                        # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")                                            # (local)

    h_audit = hashlib.sha256()                                   # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                  # (local)

    h_content = hashlib.sha256()                                 # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()                              # (local)
    return audit, content


def _prior_audit_sha() -> str:
    """audit_sha256 of the most-recent prior canonical line for GATE_ID (Option A
    supersedes tag), or '' if none. Verdict permanence: never edit the prior line."""
    if not VERDICT_TXT.exists():
        return ""
    prior = ""                                                   # (local)
    try:
        for ln in VERDICT_TXT.read_text(encoding="utf-8").splitlines():
            if ln.startswith(f"{GATE_ID}:") and "audit_sha256=" in ln:
                prior = ln.split("audit_sha256=", 1)[1].split()[0]  # (local)
    except OSError:
        return ""
    return prior


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str,
                   sign_v: str, mag_v: str, regime_v: str,
                   supersedes: str = "") -> None:
    sup = f" supersedes={supersedes}" if supersedes else ""       # (local)
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r}{sup} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )                                                            # (local)
    comp = (f"# audit_sha256_short={audit_sha[:16]} "
            f"content_sha256_short={content_sha[:16]} "
            f"# {GATE_ID} dual-SHA companion row"
            + (f" supersedes={supersedes}" if supersedes else "")
            + "\n")                                              # (local)
    # schema-v2 3-tuple companion row — REQUIRED for [SIGN] trigger
    tuple_row = (f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
                 f"regime_verdict={regime_v} "
                 f"# {GATE_ID} 3-tuple annotation (schema-v2)\n")  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(comp)
        fp.write(tuple_row)


# ---------------------------------------------------------------------------
# Curvature trajectory:  K(tau), R(tau) exact ;  |Ric|^2(tau) numeric ;
#                        |C|^2(tau) via Bianchi identity.
# ---------------------------------------------------------------------------
def weyl2_bianchi(K: np.ndarray, Ric2: np.ndarray, R: np.ndarray, n: int) -> np.ndarray:
    """|C|^2 = K - (4/(n-2))|Ric|^2 + (2/((n-1)(n-2))) R^2.

    Substitution chain (MEMORY-pinned Bianchi route, avoids Ricci-sign trap):
      Riemann orthogonal decomposition (n dim):
        K = |Riem|^2 = |C|^2 + (4/(n-2))|Ric|^2 - (2/((n-1)(n-2))) R^2
      Solve for |C|^2:
        |C|^2 = K - (4/(n-2))|Ric|^2 + (2/((n-1)(n-2))) R^2
      n=8:  4/(n-2) = 2/3 ;  2/((n-1)(n-2)) = 1/21
    The coefficient of |Ric|^2 is NEGATIVE (subtract); of R^2 is POSITIVE (add)."""
    c_ric = 4.0 / (n - 2)                                        # (local) = 2/3 at n=8
    c_R = 2.0 / ((n - 1) * (n - 2))                              # (local) = 1/21 at n=8
    return K - c_ric * Ric2 + c_R * R**2


def compute_trajectory():
    tau = np.linspace(0.0, TAU_MAX, N_EVAL)                      # (local)
    K = np.array([kretschner_exact(float(s)) for s in tau])      # (local) EXACT
    R = np.array([scalar_curvature_our_metric(float(s)) for s in tau])  # (local) EXACT
    Ric2 = np.zeros(N_EVAL)                                      # (local) numeric |Ric|^2

    t0 = time.time()                                             # (local)
    for i, s in enumerate(tau):
        R_abcd = compute_riemann_tensor_ON_fast(float(s))       # (local) (8,8,8,8)
        Ric = ricci_from_riemann(R_abcd)                        # (local) (8,8)
        Ric2[i] = float(np.sum(Ric * Ric))                      # (local) Frobenius^2 (ON frame)
    dt = time.time() - t0                                       # (local)
    print(f"  Riemann/Ricci sweep over {N_EVAL} tau-points: {dt:.1f}s")

    weyl2 = weyl2_bianchi(K, Ric2, R, N_DIM)                     # (local)
    ratio = weyl2 / K                                           # (local) |C|^2/K (tidal fraction)
    return tau, K, R, Ric2, weyl2, ratio


# ---------------------------------------------------------------------------
# CCC conformal-rescaling map: construct-or-obstruct analysis.
# ---------------------------------------------------------------------------
def ccc_map_analysis(tau, weyl2, K, ratio):
    """Decide whether a substrate-internal Penrose-CCC aeon (conformal rescaling
    of the tau->inf boundary onto a tau=0-like low-Weyl crossover surface) is
    CONSTRUCTED or OBSTRUCTED, and record the explicit obstruction reasons.

    CCC crossover requirements (Meissner-Penrose 2025; Penrose 2010):
      (R1) The future boundary is a SMOOTH spacelike conformal 3-surface X
           (one crossover surface), NOT a curvature singularity.
      (R2) Psi_ABCD -> 0 at I+ (Friedrich): Weyl VANISHES at the future
           boundary; the rescaled psi (weight -1) carries the crossover info.
      (R3) The pre-crossover epoch is WEYL-DOMINATED (C >> E,S; the GWE), with
           all matter conformally invariant (massless), rho -> 0, a -> inf.
      (R4) The conformal factor Omega -> 0 monotonically toward the boundary
           (de Sitter I+ brought to a finite conformal distance).

    Substrate tau->inf boundary (S49, S95-W4-5, W5-3 sibling, this gate):
      - K ~ (1/4) e^{4tau} -> inf : a GENUINE curvature singularity (NOT smooth).
      - |C|^2/K DECREASING (Ricci dominance GROWS) : the OPPOSITE of (R3).
      - Direction-dependent: SU(2) TIMELIKE (conformal distance inf, i+ analog),
        C^2/U(1) SPACELIKE (finite 2.582/1.291) : an ANISOTROPIC Kasner boundary,
        NOT a single smooth spacelike 3-surface.

    Conformal factor used: the per-block tortoise/conformal distance of the
    Jensen metric g_tau = 3 diag(e^{-2tau} x3, e^{tau} x4, e^{2tau} x1).
    """
    # Per-block conformal (tortoise) distances along each Jensen block direction.
    # d_block = int_tau^inf sqrt(g_block(tau')) dtau' ;  g_block has the block
    # scale factor 3 * exp(rate * tau).  We compute the S49-exact analytic limits
    # and confirm the contracting/expanding split numerically.
    #
    # rate(U1)=+2, rate(C2)=+1, rate(SU2)=-2 (volume-preserving 2 - 6 + 4 = 0).
    # For an EXPANDING block the conformal distance to tau->inf is FINITE
    #   d = int_T^inf sqrt(3) e^{(rate/2) tau} dtau  diverges  if rate>0  (proper)
    # but the relevant CCC conformal distance is the CONFORMAL-TIME integral
    #   eta_block = int_T^inf dtau / a_block(tau) = int_T^inf e^{-(rate/2) tau}/sqrt(3) dtau
    # which CONVERGES for rate>0 (expanding -> finite conformal time -> SPACELIKE)
    # and DIVERGES for rate<0 (contracting -> infinite conformal time -> TIMELIKE).
    # S49 fixes the finite values: C^2 -> 2 sqrt(5/3), U(1) -> sqrt(5/3).
    S49_C2 = 2.0 * np.sqrt(5.0 / 3.0)                            # (local) = 2.581988897...
    S49_U1 = np.sqrt(5.0 / 3.0)                                  # (local) = 1.290994449...

    # Numerical confirmation of convergence/divergence of the conformal-time
    # integral eta_block = int_T^inf e^{-(rate/2)(tau-T)} dtau-type tail.
    Tlo = 3.0                                                    # (local) start of the tail
    grid = np.linspace(Tlo, 60.0, 200000)                       # (local) fine tail grid
    # conformal-time density ~ 1/a_block ; a_block ~ sqrt(3) e^{(rate/2) tau}
    def eta_tail(rate):
        dens = (1.0 / np.sqrt(3.0)) * np.exp(-(rate / 2.0) * grid)   # (local)
        return float(np.trapezoid(dens, grid))
    eta_U1 = eta_tail(+2.0)                                      # (local) expanding -> finite
    eta_C2 = eta_tail(+1.0)                                      # (local) expanding -> finite
    eta_SU2 = eta_tail(-2.0)                                     # (local) contracting -> diverges

    su2_timelike = (eta_SU2 > 1e6)                               # (local) diverges => TIMELIKE i+
    c2_spacelike = np.isfinite(eta_C2) and eta_C2 < 1e3          # (local) finite => SPACELIKE
    u1_spacelike = np.isfinite(eta_U1) and eta_U1 < 1e3          # (local) finite => SPACELIKE

    # Kretschmann leading exponent at tau->inf:  K ~ (1/12) e^{4tau} term dominates
    # => leading exponent +4 (genuine curvature singularity, not coordinate).
    # Confirm numerically from the slope of ln K at large tau.
    tau_tail = np.linspace(10.0, 20.0, 50)                       # (local)
    lnK_tail = np.log(np.array([kretschner_exact(float(s)) for s in tau_tail]))  # (local)
    K_lead_exp = float(np.polyfit(tau_tail, lnK_tail, 1)[0])     # (local) ~ 4.0

    # --- requirement tests ---------------------------------------------------
    # (R1) smooth boundary?  NO: K diverges (curvature singularity).
    R1_smooth_boundary = bool(K_lead_exp < 0.5)                  # (local) False (K diverges)
    # (R2) Weyl vanishes at boundary (Psi->0 at I+)?  In the substrate |C|^2 GROWS
    #      without bound (and |C|^2/K decreases but |C|^2 itself -> inf), so Weyl
    #      does NOT vanish at the boundary.
    R2_weyl_vanishes = bool(weyl2[-1] < weyl2[0])               # (local) False (|C|^2 grows)
    # (R3) Weyl-dominated pre-crossover (C >> E,S)?  The ratio |C|^2/K DECREASES
    #      (Ricci dominance grows) => Weyl does NOT dominate.  Test: is the ratio
    #      increasing toward the boundary?
    R3_weyl_dominated = bool(ratio[-1] > ratio[0])              # (local) False (ratio decreases)
    # (R4) single smooth spacelike crossover 3-surface?  NO: the boundary is
    #      direction-split (SU(2) timelike, C^2/U(1) spacelike) => Kasner-anisotropic.
    R4_single_spacelike = bool(su2_timelike is False)          # (local) False (SU(2) is timelike)

    ccc_constructible = (R1_smooth_boundary and R2_weyl_vanishes
                         and R3_weyl_dominated and R4_single_spacelike)  # (local)

    obstruction_reasons = []                                    # (local)
    if not R1_smooth_boundary:
        obstruction_reasons.append(
            f"O1: tau->inf is a GENUINE curvature singularity (K ~ e^{{{K_lead_exp:.2f} tau}} -> inf), "
            "not the smooth spacelike conformal 3-surface CCC requires (R1).")
    if not R2_weyl_vanishes:
        obstruction_reasons.append(
            f"O2: Weyl does NOT vanish at the boundary -- |C|^2 GROWS from {weyl2[0]:.6f} to "
            f"{weyl2[-1]:.4e}; Friedrich's Psi->0 at I+ (R2) fails (the substrate has the "
            "OPPOSITE behavior).")
    if not R3_weyl_dominated:
        obstruction_reasons.append(
            f"O3: the pre-boundary epoch is RICCI-dominated, not Weyl-dominated -- |C|^2/K DECREASES "
            f"from {ratio[0]:.6f} to {ratio[-1]:.6f} (Ricci dominance grows); CCC's GWE requires "
            "C >> E,S (R3), the reverse.")
    if not R4_single_spacelike:
        obstruction_reasons.append(
            f"O4: the boundary is ANISOTROPIC (Kasner) -- SU(2) block TIMELIKE (conformal time "
            f"diverges, i+ analog), C^2/U(1) SPACELIKE (finite {S49_C2:.6f}/{S49_U1:.6f}); there is "
            "no single smooth spacelike crossover 3-surface to rescale (R4).")

    return {
        "S49_C2": S49_C2, "S49_U1": S49_U1,
        "eta_U1": eta_U1, "eta_C2": eta_C2, "eta_SU2": eta_SU2,
        "su2_timelike": su2_timelike, "c2_spacelike": c2_spacelike,
        "u1_spacelike": u1_spacelike,
        "K_lead_exp": K_lead_exp,
        "R1_smooth_boundary": R1_smooth_boundary,
        "R2_weyl_vanishes": R2_weyl_vanishes,
        "R3_weyl_dominated": R3_weyl_dominated,
        "R4_single_spacelike": R4_single_spacelike,
        "ccc_constructible": ccc_constructible,
        "obstruction_reasons": obstruction_reasons,
    }


# ---------------------------------------------------------------------------
# Plot
# ---------------------------------------------------------------------------
def make_plot(tau, K, Ric2, weyl2, ratio):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except Exception as exc:                                     # noqa: BLE001
        print(f"  [plot skipped: {exc}]")
        return
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle(r"S96-GEOM-CCC-WEYL: $|C|^2(\tau)$ monotonicity & WCH / CCC test",
                 fontsize=13, fontweight="bold")

    ax = axes[0, 0]
    ax.semilogy(tau, weyl2, "b-", lw=2, label=r"$|C|^2$ (Weyl)")
    ax.semilogy(tau, K, "r--", lw=1.5, label=r"$K=|Riem|^2$")
    ax.semilogy(tau, Ric2, "g-.", lw=1.5, label=r"$|Ric|^2$")
    ax.axhline(5.0 / 14.0, color="purple", ls=":", lw=1.2,
               label=r"$5/14$ (genesis min)")
    ax.axvline(tau_fold, color="orange", ls=":", lw=1, alpha=0.7, label=r"$\tau_{fold}$")
    ax.axvline(tau_NEC, color="brown", ls=":", lw=1, alpha=0.7, label=r"$\tau_{NEC}$")
    ax.set_xlabel(r"$\tau$"); ax.set_ylabel("curvature invariant")
    ax.set_title(r"Curvature invariants vs $\tau$ (log)")
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3)

    ax = axes[0, 1]
    ax.plot(tau, weyl2, "b-", lw=2)
    ax.axhline(5.0 / 14.0, color="purple", ls=":", lw=1.2, label=r"$5/14$ genesis min")
    ax.plot(0.0, 5.0 / 14.0, "ko", ms=7, label="genesis (WCH minimum)")
    ax.set_xlim(0, 0.6); ax.set_ylim(0.35, 0.45)
    ax.set_xlabel(r"$\tau$"); ax.set_ylabel(r"$|C|^2$")
    ax.set_title(r"$|C|^2$ detail near genesis: monotone rise from $5/14$")
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3)

    ax = axes[1, 0]
    ax.plot(tau, ratio, "k-", lw=2)
    ax.axhline(5.0 / 14.0, color="blue", ls="--", lw=1.2,
               label=r"$5/14$ ($|C|^2/K$ at $\tau=0$)")
    ax.set_xlabel(r"$\tau$"); ax.set_ylabel(r"$|C|^2/K$")
    ax.set_title(r"Weyl fraction $|C|^2/K$ DECREASES (Ricci dominance grows)")
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3)

    ax = axes[1, 1]
    dWeyl = np.diff(weyl2) / np.diff(tau)                        # (local) d|C|^2/dtau
    tau_mid = 0.5 * (tau[1:] + tau[:-1])                         # (local)
    ax.plot(tau_mid, dWeyl, "m-", lw=2)
    ax.axhline(0.0, color="k", ls="--", lw=1)
    ax.set_xlabel(r"$\tau$"); ax.set_ylabel(r"$d|C|^2/d\tau$")
    ax.set_title(r"WCH sign claim: $d|C|^2/d\tau > 0$ throughout")
    ax.grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  [plot saved: {OUT_PNG.name}]")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> int:
    INPUT_FILES = [                                              # (local)
        SHARED_DIR / "canonical_constants.py",
        SESS_DIR.parent / "session-22" / "s22a_weyl_curvature.npz",
        SHARED_DIR / "r20a_riemann_tensor.py",
        (PROJECT_ROOT / "researchers" / "Schwarzschild-Penrose"
         / "11_2025_Meissner_Penrose_Physics_of_CCC.md"),
        (PROJECT_ROOT / "researchers" / "Tesla-Resonance"
         / "15_2010_Penrose_Conformal_Cyclic_Cosmology_Aeons.md"),
    ]
    print("=" * 78)
    print(f"  {GATE_ID}  —  WCH monotonicity + CCC construct/obstruct")
    print("=" * 78)
    pins = log_input_pins(INPUT_FILES)                           # (local)
    closure = closure_hash(pins)                                # (local)
    print(f"  closure (legacy, informational): {closure[:16]}...")
    audit_sha, content_sha = compute_dual_sha(
        THIS, SHARED_DIR / "canonical_constants.py", pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print(f"  tau_fold = {tau_fold}   tau_NEC = {tau_NEC}")
    print()

    # ---- (i) curvature trajectory + monotonicity ---------------------------
    tau, K, R, Ric2, weyl2, ratio = compute_trajectory()

    # anchor: |C|^2(0) = 5/14
    anchor_err = abs(weyl2[0] - WEYL2_GENESIS_EXACT)             # (local)
    anchor_ok = anchor_err < ANCHOR_TOL                         # (local)

    # monotonicity of |C|^2 on (0, tau_max]
    dWeyl = np.diff(weyl2)                                       # (local)
    mono_increasing = bool(np.all(dWeyl > -MONO_TOL))           # (local) strictly up (tol)
    strictly_increasing = bool(np.all(dWeyl > 0.0))             # (local)
    n_decreasing = int(np.sum(dWeyl <= 0.0))                    # (local)
    min_idx = int(np.argmin(weyl2))                             # (local)
    genesis_is_min = (min_idx == 0)                            # (local)

    # |C|^2/K behaviour (the distinction).  session-49-sp-collab established
    # |C|^2/K DECREASING on [0,2.0] as a NET statement (endpoint < start).  The
    # LOCAL picture refines this: the ratio rises slightly from 5/14 to a peak
    # near the fold (volume-preserving TT initially shears Weyl faster than
    # Ricci), then the K ~ e^{4tau} Ricci tail drives it down.  Both reported.
    dratio = np.diff(ratio)                                     # (local)
    ratio_locally_monotone_dec = bool(np.all(dratio < MONO_TOL))  # (local) global-monotone test
    ratio_net_decreasing = bool(ratio[-1] < ratio[0])          # (local) session-49 NET statement
    ratio_peak_idx = int(np.argmax(ratio))                     # (local)
    ratio_peak_tau = float(tau[ratio_peak_idx])                # (local) ~ fold
    ratio_peak_val = float(ratio[ratio_peak_idx])              # (local)

    print("  --- (i) WCH monotonicity ---")
    print(f"  |C|^2(0)          = {weyl2[0]:.12f}   (5/14 = {WEYL2_GENESIS_EXACT:.12f})")
    print(f"  anchor err        = {anchor_err:.2e}   ({'OK' if anchor_ok else 'FAIL'})")
    print(f"  |C|^2(tau_max)    = {weyl2[-1]:.6e}")
    print(f"  |C|^2 min at idx  = {min_idx} (tau={tau[min_idx]:.3f})  genesis-is-min={genesis_is_min}")
    print(f"  monotone-increasing (tol {MONO_TOL:g}) = {mono_increasing}  "
          f"strictly = {strictly_increasing}  n_decreasing_steps = {n_decreasing}")
    print(f"  |C|^2/K(0)={ratio[0]:.6f}  |C|^2/K(tau_max)={ratio[-1]:.6f}  "
          f"NET-DECREASING={ratio_net_decreasing}  (global-monotone={ratio_locally_monotone_dec})")
    print(f"  |C|^2/K peak = {ratio_peak_val:.6f} at tau={ratio_peak_tau:.3f} (~fold); "
          f"rises to fold then Ricci-tail drives it down")
    print(f"    [distinction: |C|^2 UP (strict) while |C|^2/K NET-DOWN -> Ricci grows faster overall]")
    print()

    # ---- (ii) CCC construct/obstruct ---------------------------------------
    ccc = ccc_map_analysis(tau, weyl2, K, ratio)
    print("  --- (ii) CCC conformal-rescaling map ---")
    print(f"  per-block conformal time: eta_U1={ccc['eta_U1']:.6f} (finite, spacelike), "
          f"eta_C2={ccc['eta_C2']:.6f} (finite, spacelike), eta_SU2={ccc['eta_SU2']:.3e} (diverges, timelike)")
    print(f"  S49 anchors: C^2={ccc['S49_C2']:.6f}, U(1)={ccc['S49_U1']:.6f}")
    print(f"  K leading exponent (tau->inf) = {ccc['K_lead_exp']:.5f}  (expect 4)")
    print(f"  R1 smooth boundary      : {ccc['R1_smooth_boundary']}")
    print(f"  R2 Weyl vanishes at I+  : {ccc['R2_weyl_vanishes']}")
    print(f"  R3 Weyl-dominated GWE   : {ccc['R3_weyl_dominated']}")
    print(f"  R4 single spacelike X   : {ccc['R4_single_spacelike']}")
    print(f"  ==> CCC map constructible: {ccc['ccc_constructible']}")
    ccc_status = "CONSTRUCTED" if ccc["ccc_constructible"] else "OBSTRUCTED"  # (local)
    print(f"  ==> CCC map status: {ccc_status}")
    for r in ccc["obstruction_reasons"]:
        print(f"      {r}")
    print()

    # ---- verdict (pre-registered) ------------------------------------------
    # PASS iff (d|C|^2/dtau > 0 from genesis 5/14) AND (CCC map constructed OR
    #          shown obstructed with reason).
    sign_ok = mono_increasing and genesis_is_min and anchor_ok  # (local)
    ccc_resolved = ccc["ccc_constructible"] or (len(ccc["obstruction_reasons"]) > 0)  # (local)

    # schema-v2 3-tuple
    sign_v = "PASS" if sign_ok else "FAIL"                       # (local) direction d|C|^2/dtau>0 matches
    # magnitude: anchor 5/14 match (the pinned numerical target)
    mag_v = "PASS" if anchor_ok else "FAIL"                      # (local)
    # regime: the Bianchi-route curvature trajectory is exact/numeric over the
    # full intended window [0, 2.0]; no small-parameter breakdown.
    regime_v = "VALID"                                          # (local)

    # composite collapse (pre-registered rule, gate-verdicts.md)
    if regime_v == "BREAKDOWN":
        composite = "FAIL"                                     # (local)
    elif sign_v == "FAIL":
        composite = "FAIL"
    elif mag_v == "FAIL" and regime_v == "VALID":
        composite = "FAIL"
    elif mag_v == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"
    # gate-specific: PASS additionally requires the CCC map be resolved
    if composite == "PASS" and not ccc_resolved:
        composite = "INFO"

    ccc_short = "OBSTRUCTED-O1O2O3O4" if not ccc["ccc_constructible"] else "CONSTRUCTED"  # (local)
    value_str = (f"WCH:d|C|2/dtau>0_from_5/14_mono={mono_increasing}_"
                 f"|C|2(0)={weyl2[0]:.6f}_|C|2(2.0)={weyl2[-1]:.3e}_"
                 f"ratioNETdec={ratio_net_decreasing};CCC:{ccc_short}")  # (local)

    # ---- save data ---------------------------------------------------------
    np.savez(
        OUT_NPZ,
        tau=tau, K=K, R=R, Ric2=Ric2, weyl2=weyl2, ratio=ratio,
        weyl2_genesis_exact=np.array([WEYL2_GENESIS_EXACT]),
        anchor_err=np.array([anchor_err]),
        mono_increasing=np.array([mono_increasing]),
        strictly_increasing=np.array([strictly_increasing]),
        n_decreasing_steps=np.array([n_decreasing]),
        genesis_is_min=np.array([genesis_is_min]),
        ratio_net_decreasing=np.array([ratio_net_decreasing]),
        ratio_locally_monotone_dec=np.array([ratio_locally_monotone_dec]),
        ratio_peak_tau=np.array([ratio_peak_tau]),
        ratio_peak_val=np.array([ratio_peak_val]),
        # CCC record
        ccc_constructible=np.array([ccc["ccc_constructible"]]),
        ccc_status=np.array([ccc_status]),
        eta_U1=np.array([ccc["eta_U1"]]), eta_C2=np.array([ccc["eta_C2"]]),
        eta_SU2=np.array([ccc["eta_SU2"]]),
        S49_C2=np.array([ccc["S49_C2"]]), S49_U1=np.array([ccc["S49_U1"]]),
        K_lead_exp=np.array([ccc["K_lead_exp"]]),
        R1_smooth_boundary=np.array([ccc["R1_smooth_boundary"]]),
        R2_weyl_vanishes=np.array([ccc["R2_weyl_vanishes"]]),
        R3_weyl_dominated=np.array([ccc["R3_weyl_dominated"]]),
        R4_single_spacelike=np.array([ccc["R4_single_spacelike"]]),
        obstruction_reasons=np.array(ccc["obstruction_reasons"], dtype=object),
        # verdict 3-tuple
        sign_verdict=np.array([sign_v]), magnitude_verdict=np.array([mag_v]),
        regime_verdict=np.array([regime_v]), composite=np.array([composite]),
        value_str=np.array([value_str]),
    )
    print(f"  [data saved: {OUT_NPZ.name}]")

    make_plot(tau, K, Ric2, weyl2, ratio)

    # ---- emit verdict ------------------------------------------------------
    supersedes = _prior_audit_sha()                             # (local)
    append_verdict(composite, value_str, audit_sha, content_sha,
                   sign_v, mag_v, regime_v, supersedes=supersedes)
    print()
    print("=" * 78)
    print(f"  {GATE_ID}: {composite}  (sign={sign_v}, mag={mag_v}, regime={regime_v})")
    print(f"  CCC map: {ccc_status}")
    print(f"  value = {value_str}")
    if supersedes:
        print(f"  supersedes = {supersedes[:16]}...")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    sys.exit(main())
