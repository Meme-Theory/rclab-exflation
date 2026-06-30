#!/usr/bin/env python3
"""
INV8 W3-1 — Kibble-Zurek Z_3 Wall Network of the Transit
========================================================

Gate: INV8-W3-1-KZ-Z3-WALL-NETWORK ([SIGN])

Pre-registered threshold (plan §W3-1):
  operator (set): pi_0(U(1)_7 x Z_3) = Z_3 != {e}  (walls ADMITTED by homotopy)
                  AND n_wall(Mach) monotone-increasing in Mach
  strict_PASS_boundary: pi_0 = Z_3 (|pi_0| = 3 > 1) => WALLS-FORM; the composite
    verdict is set by the 3-tuple
      (homotopy-admits-walls, KZ-freezes-network, w=-2/3-component-nonzero)
  PASS_meaning : the Z_3 wall network FORMS, survives, and sources a w=-2/3 DE
                 component + an a^{-1} BBN channel (ONE mechanism for C-1 + C-4);
                 the 'no-walls' verdict used the wrong symmetry group.
  FAIL_meaning : no Z_3 wall network survives the transit; the frozen-modulus
                 w_a=0 lock (C-1) stands on a SHARPER footing (the KZ route is CLOSED).
  INFO_meaning : walls form but anneal partially, OR homotopy admits walls but the
                 wall tension / EoS is regime-dependent (a partial channel).

Two-track dual prior (plan-frozen):
  track_A (0.5): walls FORM and survive -> 0.9 to A on PASS
  track_B (0.5): no walls survive (0D regime / dilution / bias is the SHARPER
                 argument) -> 0.9 to B on FAIL
  discriminator: PASS (xi_hat sub-horizon AND sigma_wall > thermal scale) -> 0.9 A;
                 INFO (xi_hat sub-horizon, sigma_wall sub-threshold; forms then anneals)
                   -> mass split per annealing fraction;
                 FAIL (no Z_3 walls at any Mach) -> 0.9 B.

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - canonical_constants.py (feeds audit_sha256 only; supplies xi_BCS, dt_transit,
    Mach_max_framework, L_over_xi, c_fabric, tau_fold, Delta_BCS, M_KK, w0_FW)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)
  No npz input — the KZ scaling is computed from canonical constants. The s53
  canonical xi_KZ=0.162075 M_KK^{-1} (tau_0 = 1/omega_att = 0.699301) is the
  METHODOLOGICAL cross-check value (cited, recomputed, NOT loaded).

Output 4-tuple:
  (value=<n_wall direction sign + 0D-regime ratio>, scheme=FW,
   convention=KZ-mean-field-BCS-z2-nu-half, L_max=N/A)

Classification: PHONONIC
  The transit IS a quench of the substrate's internal spectral structure through
  the van Hove fold — not a system passing through a phase transition IN a
  container. The order-parameter manifold IS the structure the D_K spectrum
  reorganizes onto at tau_fold: U(1)_7 BCS-condensate phase (Cooper pairs carry
  K_7 charge +/-1/2, B6) TIMES the Z_3 Jensen-deformation structure
  (pi_0(Z_3)=Z_3, the 512-plaquette frustration §VII.AG.4). A Kibble-Zurek wall
  is a frozen-in mismatch between Z_3 sectors of the reorganized spectrum — a
  relay-pattern domain boundary, NOT a topological defect embedded in spacetime.

METHODOLOGY (plan §W3-1; MCP pre-compute audit branches included)
-----------------------------------------------------------------
The gate's central claim has TWO logically separable parts:
  (H) HOMOTOPY: the broken-symmetry manifold is U(1)_7 x Z_3, not U(1) alone, so
      pi_0 = Z_3 != {e} and codim-1 Z_3 walls ARE admitted. This part is CORRECT
      (the framework's bulk Z_3 wall solutions exist; framework-paasch-potential.md
      §1.2 'Domain walls between Z_3 sectors carry topological charge classified by
      pi_0(Z_3)=Z_3'; ANDREEV-Z3 BdG wall at delta_phi=2pi/3).
  (F) FORMATION/SURVIVAL: does a finite-rate transit at Mach=13.75 FREEZE a network
      that SURVIVES to source cosmology? The MCP pre-compute surfaced THREE prior
      structural results that bear decisively on (F), all INDEPENDENT of and SHARPER
      than the pi_0(U(1))=0 homotopy argument the gate set out to overturn:
        (F1) 0D-REGIME (T3-S38-KZ-DEFECTS, S81 PASS, convention=0D_pair_reformulated;
             INST-MC-37, S37): L/xi_BCS = 0.031, L/xi_KZ = 0.1546. The fold-crossing
             region is a FRACTION OF ONE correlation length across — there is no room
             for even a single domain boundary, so KZ defect formation is reformulated
             as 0D pair production. A network needs L/xi >> 1; here L/xi << 1.
        (F2) GGE UNIVERSALITY (S57, PROVEN): all cells identical post-transit, E_DW=0,
             no domain walls. The sudden quench (dt/T_L=1.25e-5, P_exc=1.000) populates
             the Z_3 sectors UNIFORMLY (no domain selection).
        (F3) DILUTION + BIAS (S42; S77 RETRACTED): even a wall network that DID form
             carries f_wall(transit)=3.06e-7 and dilutes as rho_wall ~ a^{-1}, so
             f_wall(today) = f_wall(transit)*a_transit ~ 7e-29 (utterly negligible);
             and the Josephson bias annihilates walls 15,000x before reheating (S77).

The computation therefore:
  (1) CONFIRMS (H): |pi_0(U(1)_7 x Z_3)| = |pi_0(Z_3)| = 3 > 1. Walls admitted.
  (2) Computes the KZ frozen correlation length xi_hat = xi_0 (tau_Q/tau_0)^{nu/(1+z nu)}
      at the canonical (z=2, nu=1/2, tau_Q=dt_transit, tau_0=1/omega_att) and
      cross-checks against the s53 canonical 0.162075 to 3 sig figs.
  (3) Computes the 0D-regime ratio L/xi_hat. This is the SURVIVAL discriminator:
      a network resolves iff L/xi_hat >> 1.
  (4) Computes the Mach-dependence direction: tau_Q proportional to 1/Mach =>
      xi_hat proportional to Mach^{-1/4} => n_wall proportional to Mach^{+1/2}
      (denser network at higher Mach IF one forms). Reads off the SIGN.
  (5) Maps to cosmology: w_wall = -2/3, rho_wall ~ a^{-1}, and the S42 dilution to
      today. Reports the w_a contribution as the survived-fraction-weighted band.

The composite verdict honors the substitution chain (the SIGN n_wall-vs-Mach is +)
AND the substrate physics (the 0D regime + dilution kill the SURVIVING network).
This is the genuine dual-prior outcome: (H) PASS on homotopy, but (F) the network
does NOT survive -> the w_a/BBN route via a FROZEN wall network is CLOSED, and the
running-vacuum mechanism (INV8-W2-4) is the surviving candidate.

DISCIPLINE
----------
- `from canonical_constants import *`
- every local/intermediate tagged `# (local)`
- scalar KZ arithmetic; cpu-cap OMP8, no matrices
- SHA-256 of all inputs logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- script PRINTS the verdict payload; the AGENT calls emit_verdict (race-safe)
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")  # (local) cpu-cap; scalar arithmetic

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
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
SESSION_DIR = Path(__file__).resolve().parent           # computations/investigation-8/
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "8"                                            # (local) investigation number
GATE_ID = "INV8-W3-1-KZ-Z3-WALL-NETWORK"                # (local)
SCHEME = "FW"                                            # (local)
CONVENTION = "KZ-mean-field-BCS-z2-nu-half"             # (local)
L_MAX = "N/A"                                            # (local)

OUT_NPZ = SESSION_DIR / "inv8_w3_kz_z3_wall_network.npz"
OUT_PNG = SESSION_DIR / "inv8_w3_kz_z3_wall_network.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
]

# ---- Pre-registered KZ machinery (plan §W3-1 machinery_pin_map) ----
NU_KZ = 0.5                       # (local) mean-field BCS, S53/S88
Z_DYN = 2.0                       # (local) dynamical exponent z=2 (model A, dissipative; EXPONENT-63)
KZ_EXPONENT = NU_KZ / (1.0 + Z_DYN * NU_KZ)   # (local) = 1/4 (rational)
# s53 canonical microscopic relaxation scale tau_0 = 1/omega_att = 0.699301 M_KK^{-1}
# (s53_vortex_nucleation_output.txt STEP 1). This is the substrate microscopic time.
TAU_0_S53 = 0.699301              # (local) 1/omega_att, s53 canonical
XI_KZ_S53_CANON = 0.162075        # (local) s53 canonical xi_KZ (M_KK^{-1}); cross-check target
W_WALL = -2.0 / 3.0               # (local) codim-1 domain-wall EoS (rational)
MACH_SCAN_HI_FACTOR = 2.0         # (local) Mach scan upper = 2 x 13.75 = 27.5
N_MACH = 8                        # (local) 8 log-spaced Mach points (direction scan)
XCHECK_TOL_SIGFIG = 1e-3          # (local) cross-check xi_hat vs s53 to 3 sig figs (rel)


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
def kz_xi_hat(mach: float) -> float:
    """KZ frozen correlation length xi_hat = xi_0 (tau_Q/tau_0)^{nu/(1+z nu)}.

    xi_0 = xi_BCS (canonical); tau_Q(Mach) = dt_transit * (Mach_ref/Mach)
    (faster transit = shorter fold-crossing); tau_0 = 1/omega_att (s53 canonical).
    """
    tau_Q = dt_transit * (Mach_max_framework / mach)        # (local)
    quench_ratio = tau_Q / TAU_0_S53                        # (local)
    return xi_BCS * (quench_ratio ** KZ_EXPONENT)           # (local)


def compute() -> dict:
    # --- (H) HOMOTOPY: pi_0(U(1)_7 x Z_3) = pi_0(U(1)_7) x pi_0(Z_3) ---
    # pi_0(U(1)) = {e} (connected); pi_0(Z_3) = Z_3 (3 components).
    # => pi_0(product) = Z_3, cardinality 3.
    pi0_U1_card = 1                          # (local) |pi_0(U(1)_7)| = 1 (connected)
    pi0_Z3_card = 3                          # (local) |pi_0(Z_3)| = 3
    pi0_product_card = pi0_U1_card * pi0_Z3_card   # (local) = 3
    homotopy_admits_walls = pi0_product_card > 1   # (local) True

    # --- (2) KZ frozen correlation length at the canonical Mach=13.75 ---
    xi_hat_canon = kz_xi_hat(Mach_max_framework)     # (local)
    tau_Q_canon = dt_transit * (Mach_max_framework / Mach_max_framework)  # (local) = dt_transit
    quench_ratio_canon = tau_Q_canon / TAU_0_S53     # (local)
    # cross-check against s53 canonical 0.162075 (3 sig figs, relative)
    xcheck_rel = abs(xi_hat_canon - XI_KZ_S53_CANON) / XI_KZ_S53_CANON   # (local)
    xcheck_pass = xcheck_rel < XCHECK_TOL_SIGFIG      # (local)

    # --- (3) 0D-regime SURVIVAL discriminator: L / xi_hat ---
    # L = the fold-crossing system size. The canonical 0D ratio L/xi_BCS = 0.031
    # (L_over_xi, S37/INST-MC-37). So L = L_over_xi * xi_BCS (in M_KK^{-1}).
    L_fold = L_over_xi * xi_BCS                       # (local) fold system size, M_KK^{-1}
    L_over_xi_hat = L_fold / xi_hat_canon             # (local) survival ratio
    # A domain-wall NETWORK resolves iff L/xi_hat >> 1 (many correlation volumes).
    # Here L/xi_hat << 1: the fold is a fraction of ONE correlation length.
    network_resolves = L_over_xi_hat > 1.0            # (local) False (0D regime)

    # --- (4) Mach-dependence direction (8-point scan) ---
    mach_grid = np.logspace(np.log10(Mach_max_framework),
                            np.log10(Mach_max_framework * MACH_SCAN_HI_FACTOR),
                            N_MACH)                   # (local)
    xi_hat_grid = np.array([kz_xi_hat(m) for m in mach_grid])   # (local)
    # n_wall ~ xi_hat^{-2} (codim-1 walls in d=3 give area-density ~ xi^{-2});
    # also report the d=3 number density xi^{-3} (illustrative per plan).
    n_wall_grid = xi_hat_grid ** (-2.0)               # (local) codim-1 area density
    n_wall_d3_grid = xi_hat_grid ** (-3.0)            # (local) illustrative number density
    # direction: sign of d n_wall / d Mach (finite difference, monotone)
    dn_dMach = np.gradient(n_wall_grid, mach_grid)    # (local)
    n_wall_direction = int(np.sign(np.mean(dn_dMach)))  # (local) +1 expected
    # analytic check: n_wall ∝ Mach^{+1/2}; slope > 0
    analytic_exponent = 2.0 * KZ_EXPONENT             # (local) = 1/2 (n_wall ∝ Mach^{+1/2})

    # --- (5) Cosmology mapping (S42 canonical; recomputed, not loaded) ---
    # w_wall = -2/3; rho_wall ~ a^{-1}; f_wall(today) = f_wall(transit)*a_transit.
    # S42: f_wall_energy(transit) = 3.06e-7. a_transit ~ 2.35e-22 (S42).
    f_wall_transit = 3.06e-7                          # (local) S42 wall energy frac at transit
    a_transit = 2.35e-22                              # (local) S42 transit scale factor
    f_wall_today = f_wall_transit * a_transit         # (local) ~ 7e-29 (negligible)
    # The w_a contribution: a wall component with f_wall_today ~ 7e-29 contributes
    # |delta w_a| <~ f_wall_today (order-of-magnitude), far below DESI sensitivity (~0.3).
    desi_w_a_sensitivity = 0.3                        # (local) approx DESI w_a 1-sigma
    w_a_contribution_bound = f_wall_today             # (local) << desi_w_a_sensitivity

    # --- composite 3-tuple components ---
    # (a) homotopy-admits-walls : TRUE (pi_0 = Z_3)
    # (b) KZ-freezes-network    : FALSE — L/xi_hat << 1 (0D regime; T3-S38, S57)
    # (c) w=-2/3-component-nonzero (SURVIVING) : FALSE — f_wall_today ~ 7e-29
    tuple_homotopy = homotopy_admits_walls            # (local) True
    tuple_freezes_network = network_resolves          # (local) False
    tuple_w_component_survives = (f_wall_today > desi_w_a_sensitivity)  # (local) False

    return {
        # the headline 'value' is the n_wall-vs-Mach SIGN (the [SIGN] prediction)
        # tagged with the 0D survival ratio that closes the SURVIVAL question.
        "value": (f"n_wall_dir=+{n_wall_direction:d}_Mach^+0.5"
                  f"|L/xi_hat={L_over_xi_hat:.4f}(0D,no-network)"
                  f"|pi0=Z3(card3)|f_wall_today={f_wall_today:.3e}"
                  f"|w_wall={W_WALL:.4f}"),
        # structural scalars
        "pi0_product_card": pi0_product_card,
        "homotopy_admits_walls": bool(homotopy_admits_walls),
        "xi_hat_canon": float(xi_hat_canon),
        "xi_KZ_s53_canon": XI_KZ_S53_CANON,
        "xcheck_rel": float(xcheck_rel),
        "xcheck_pass": bool(xcheck_pass),
        "tau_Q_canon": float(tau_Q_canon),
        "tau_0_s53": TAU_0_S53,
        "quench_ratio_canon": float(quench_ratio_canon),
        "kz_exponent": float(KZ_EXPONENT),
        "L_fold": float(L_fold),
        "L_over_xi_hat": float(L_over_xi_hat),
        "L_over_xi_BCS": float(L_over_xi),
        "network_resolves": bool(network_resolves),
        "n_wall_direction": n_wall_direction,
        "analytic_exponent": float(analytic_exponent),
        "w_wall": float(W_WALL),
        "f_wall_transit": f_wall_transit,
        "a_transit": a_transit,
        "f_wall_today": float(f_wall_today),
        "desi_w_a_sensitivity": desi_w_a_sensitivity,
        "w_a_contribution_bound": float(w_a_contribution_bound),
        # 3-tuple components
        "tuple_homotopy_admits": bool(tuple_homotopy),
        "tuple_freezes_network": bool(tuple_freezes_network),
        "tuple_w_component_survives": bool(tuple_w_component_survives),
        # grids
        "mach_grid": mach_grid,
        "xi_hat_grid": xi_hat_grid,
        "n_wall_grid": n_wall_grid,
        "n_wall_d3_grid": n_wall_d3_grid,
        "dn_dMach": dn_dMach,
    }


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 3-tuple ([SIGN]) + 4-tuple output
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme, convention, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def evaluate_gate(r: dict) -> tuple[str, str, str, str]:
    """Return (composite_verdict, sign_verdict, magnitude_verdict, regime_verdict).

    SIGN: the substitution-chain Step-4/5 prediction is n_wall ∝ Mach^{+1/2}
          (d n_wall/d Mach > 0). PASS iff the computed sign is +1.
    MAGNITUDE: the SURVIVAL question — does a w=-2/3 wall component survive to
          source DESI w_a? PASS would require f_wall_today > DESI sensitivity.
          Here f_wall_today ~ 7e-29 << 0.3 => FAIL (no surviving component).
    REGIME: is the KZ network-formation regime VALID? A network requires L/xi_hat
          >> 1. Here L/xi_hat ~ 0.07 << 1 — the 0D regime: the network-formation
          interpretation of KZ BREAKS DOWN (it is reformulated as 0D pair
          production, T3-S38-KZ-DEFECTS). => BREAKDOWN.

    Composite collapse (gate-verdicts.md): regime=BREAKDOWN => composite FAIL.
    This is the genuine dual-prior FAIL: the HOMOTOPY part is correct (pi_0=Z_3),
    but the network does NOT form/survive -> the frozen-wall route to w_a/BBN is
    CLOSED; 0.9 mass to Track B.
    """
    # SIGN
    sign_v = "PASS" if r["n_wall_direction"] == 1 else "FAIL"   # (local)
    # MAGNITUDE — surviving w=-2/3 component vs DESI sensitivity
    if r["f_wall_today"] > r["desi_w_a_sensitivity"]:
        mag_v = "PASS"   # (local) would-be live DESI w_a signal
    elif r["f_wall_today"] > 1e-3 * r["desi_w_a_sensitivity"]:
        mag_v = "INFO"   # (local) partial channel
    else:
        mag_v = "FAIL"   # (local) negligible — no surviving wall component
    # REGIME — KZ network-formation regime of validity (L/xi >> 1)
    if r["L_over_xi_hat"] >= 1.0:
        reg_v = "VALID"      # (local) network resolves
    elif r["L_over_xi_hat"] >= 0.5:
        reg_v = "MARGINAL"   # (local)
    else:
        reg_v = "BREAKDOWN"  # (local) 0D regime — network-formation interpretation invalid
    # Composite collapse rule (pre-registered, gate-verdicts.md)
    if reg_v == "BREAKDOWN":
        composite = "FAIL"
    elif sign_v == "FAIL":
        composite = "FAIL"
    elif mag_v == "FAIL" and reg_v == "VALID":
        composite = "FAIL"
    elif mag_v == "FAIL" and reg_v == "MARGINAL":
        composite = "INFO"
    elif mag_v == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"
    return composite, sign_v, mag_v, reg_v


def make_plot(r: dict) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(13, 9))

    # (a) xi_hat vs Mach
    ax = axes[0, 0]
    ax.plot(r["mach_grid"], r["xi_hat_grid"], "o-", color="C0")
    ax.axhline(r["xi_KZ_s53_canon"], ls="--", color="grey",
               label=f"s53 canonical xi_KZ={r['xi_KZ_s53_canon']:.4f}")
    ax.axvline(Mach_max_framework, ls=":", color="C3",
               label=f"Mach={Mach_max_framework}")
    ax.set_xlabel("Mach")
    ax.set_ylabel(r"$\hat{\xi}$  (M$_{KK}^{-1}$)")
    ax.set_title(r"(a) KZ frozen length $\hat{\xi}=\xi_0(\tau_Q/\tau_0)^{1/4}$, $\hat{\xi}\propto$Mach$^{-1/4}$")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # (b) n_wall vs Mach (the SIGN read-off)
    ax = axes[0, 1]
    ax.plot(r["mach_grid"], r["n_wall_grid"], "s-", color="C2",
            label=r"$n_{wall}\sim\hat{\xi}^{-2}\propto$Mach$^{+1/2}$ (UP)")
    ax.set_xlabel("Mach")
    ax.set_ylabel(r"$n_{wall}$ (codim-1 area density, M$_{KK}^{2}$)")
    ax.set_title(f"(b) [SIGN] dn_wall/dMach = +{r['n_wall_direction']} (denser at higher Mach)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # (c) the SURVIVAL discriminator: L/xi_hat (0D regime bar)
    ax = axes[1, 0]
    bars = ["L/xi_BCS\n(S37 0D)", "L/xi_hat\n(KZ)", "network\nthreshold"]
    vals = [r["L_over_xi_BCS"], r["L_over_xi_hat"], 1.0]
    cols = ["C1", "C3", "k"]
    ax.bar(bars, vals, color=cols, alpha=0.7)
    ax.axhline(1.0, ls="--", color="k")
    ax.set_yscale("log")
    ax.set_ylabel(r"$L/\xi$ (network resolves iff $\gg 1$)")
    ax.set_title(f"(c) 0D regime: L/xi_hat={r['L_over_xi_hat']:.3f} << 1  => NO network")

    # (d) cosmological dilution (S42)
    ax = axes[1, 1]
    stages = ["f_wall\n(transit)", "f_wall\n(today)", "DESI w_a\nsensitivity"]
    fvals = [r["f_wall_transit"], r["f_wall_today"], r["desi_w_a_sensitivity"]]
    ax.bar(stages, fvals, color=["C0", "C3", "C2"], alpha=0.7)
    ax.set_yscale("log")
    ax.set_ylabel("energy fraction / w_a bound")
    ax.set_title(f"(d) w_wall={r['w_wall']:.3f}, a$^{{-1}}$ dilution: f_today={r['f_wall_today']:.1e} << DESI")

    fig.suptitle("INV8-W3-1 — Kibble-Zurek Z_3 Wall Network of the Transit\n"
                 "Homotopy admits walls (pi_0=Z_3) BUT 0D regime + a^{-1} dilution => no surviving network",
                 fontsize=11)
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


def save_npz(r: dict, audit_sha: str, content_sha: str, verdict_tuple: tuple) -> None:
    composite, sign_v, mag_v, reg_v = verdict_tuple
    np.savez(
        OUT_NPZ,
        value=r["value"],
        composite_verdict=composite, sign_verdict=sign_v,
        magnitude_verdict=mag_v, regime_verdict=reg_v,
        pi0_product_card=r["pi0_product_card"],
        homotopy_admits_walls=r["homotopy_admits_walls"],
        xi_hat_canon=r["xi_hat_canon"], xi_KZ_s53_canon=r["xi_KZ_s53_canon"],
        xcheck_rel=r["xcheck_rel"], xcheck_pass=r["xcheck_pass"],
        tau_Q_canon=r["tau_Q_canon"], tau_0_s53=r["tau_0_s53"],
        quench_ratio_canon=r["quench_ratio_canon"], kz_exponent=r["kz_exponent"],
        L_fold=r["L_fold"], L_over_xi_hat=r["L_over_xi_hat"],
        L_over_xi_BCS=r["L_over_xi_BCS"], network_resolves=r["network_resolves"],
        n_wall_direction=r["n_wall_direction"], analytic_exponent=r["analytic_exponent"],
        w_wall=r["w_wall"], f_wall_transit=r["f_wall_transit"],
        a_transit=r["a_transit"], f_wall_today=r["f_wall_today"],
        desi_w_a_sensitivity=r["desi_w_a_sensitivity"],
        w_a_contribution_bound=r["w_a_contribution_bound"],
        tuple_homotopy_admits=r["tuple_homotopy_admits"],
        tuple_freezes_network=r["tuple_freezes_network"],
        tuple_w_component_survives=r["tuple_w_component_survives"],
        mach_grid=r["mach_grid"], xi_hat_grid=r["xi_hat_grid"],
        n_wall_grid=r["n_wall_grid"], n_wall_d3_grid=r["n_wall_d3_grid"],
        dn_dMach=r["dn_dMach"],
        audit_sha256=audit_sha, content_sha256=content_sha,
    )


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="",
                          extra_rows=None) -> dict:
    payload: dict = {
        "session": int(SESSION),
        "track": "investigation",
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
# Section 7 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    r = compute()

    # --- echo the physics ---
    print("--- (H) HOMOTOPY ---")
    print(f"  pi_0(U(1)_7 x Z_3) = Z_3, |pi_0| = {r['pi0_product_card']}  "
          f"=> walls ADMITTED: {r['homotopy_admits_walls']}")
    print("--- (2) KZ frozen correlation length ---")
    print(f"  KZ exponent nu/(1+z nu) = {r['kz_exponent']:.4f}")
    print(f"  tau_Q(13.75) = dt_transit = {r['tau_Q_canon']:.6e};  tau_0 = {r['tau_0_s53']:.6f}")
    print(f"  quench_ratio = {r['quench_ratio_canon']:.6e}  (<1 => SUDDEN QUENCH)")
    print(f"  xi_hat(13.75) = {r['xi_hat_canon']:.6f} M_KK^-1   "
          f"(s53 canonical {r['xi_KZ_s53_canon']:.6f}; rel dev {r['xcheck_rel']:.2e}; "
          f"xcheck_pass={r['xcheck_pass']})")
    print("--- (3) SURVIVAL discriminator (0D regime) ---")
    print(f"  L_fold = L_over_xi_BCS * xi_BCS = {r['L_fold']:.6f} M_KK^-1")
    print(f"  L/xi_hat = {r['L_over_xi_hat']:.6f}  (network resolves iff >>1)  "
          f"=> network_resolves={r['network_resolves']}")
    print("--- (4) Mach direction (SIGN) ---")
    print(f"  n_wall ∝ Mach^{{+{r['analytic_exponent']:.2f}}}  "
          f"=> dn_wall/dMach sign = +{r['n_wall_direction']}  (denser at higher Mach)")
    print("--- (5) cosmology (S42) ---")
    print(f"  w_wall = {r['w_wall']:.6f}; rho_wall ~ a^-1")
    print(f"  f_wall(transit) = {r['f_wall_transit']:.3e}; a_transit = {r['a_transit']:.3e}")
    print(f"  f_wall(today) = {r['f_wall_today']:.3e}  (<< DESI w_a sens {r['desi_w_a_sensitivity']})")
    print()

    composite, sign_v, mag_v, reg_v = evaluate_gate(r)
    print(f"  3-tuple: sign={sign_v} magnitude={mag_v} regime={reg_v}  => composite={composite}")
    print()

    make_plot(r)
    save_npz(r, audit_sha, content_sha, (composite, sign_v, mag_v, reg_v))
    print(f"  wrote {OUT_NPZ.name}")
    print(f"  wrote {OUT_PNG.name}")
    print()

    tag = emit_4tuple(r["value"], SCHEME, CONVENTION, L_MAX)
    print(tag)
    extra = [
        "# regulator_pin=N/A (homotopy + KZ scaling; no spectral truncation)",
        ("# 3-tuple-components: homotopy_admits_walls=True(pi_0=Z_3); "
         "KZ_freezes_network=False(L/xi_hat<<1, 0D regime T3-S38-KZ-DEFECTS S81); "
         "w=-2/3-component-survives=False(f_wall_today~7e-29, S42 a^-1 dilution)"),
        ("# MCP-pre-compute: T3-S38-KZ-DEFECTS(S81 PASS 0D_pair_reformulated); "
         "GGE-Universality(S57 PROVEN E_DW=0); Domain-wall-GW(RETRACTED S77 Josephson-bias)"),
    ]
    print_verdict_payload(
        composite, r["value"], audit_sha, content_sha,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=reg_v,
        companion_note="Kibble-Zurek Z_3 wall network: homotopy admits walls, 0D regime kills network",
        extra_rows=extra,
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
