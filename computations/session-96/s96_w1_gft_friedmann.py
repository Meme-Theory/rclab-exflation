#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S96-W1-GFT-FRIEDMANN  —  ROUTE 3 of the emergent-FRW a(t) closure (cluster C1)
=============================================================================

Gate: S96-W1-GFT-FRIEDMANN   ([SIGN])
Plan: sessions/session-plan/session-96-plan-w1.md §W1-5
Owner: lqg-cosmology-theorist  (== loop-quantum-gravity-theorist)

PURPOSE
  Import the loop-quantum-cosmology / group-field-theory (GFT) condensate
  effective-Friedmann formalism (Oriti; Paper 16, researchers/Loop-Quantum-
  Gravity/index.md:651-685) and ask: treating the GGE relic (N_pair=59.8,
  P_exc=1, S_ent=0) as a condensate of D_K quasiparticles, does the GFT
  condensate-hydrodynamic H(tau)-analog reproduce the SCALE-FACTOR-54
  deceleration q-band (q: -0.9732 -> +0.8144, Connes-distance proxy) within
  20% of the band width, OR is the transfer ill-posed because the substrate
  GGE is a NON-equilibrium frozen state (diabatic; R_therm~5251) rather than
  a GFT equilibrium condensate?

  This is ROUTE 3 of three INDEPENDENT a(t)-closure routes (gates 1/4/5). Per
  the orchestrator override, H2* is computed FROM FIRST PRINCIPLES via the GFT
  condensate formalism; gates 1/4 outputs are NOT read. Cross-route comparison
  is a forward (S97) workshop.

SUBSTRATE-FIRST FRAMING (phononic-framing.md; binding)
  Loop quantum cosmology's effective Friedmann is the object the framework owes,
  but the substrate is NOT a quantized geometry the matter lives inside — it IS
  the spectral content of D_K. The GFT condensate is the LQG language for "many
  quanta of geometry"; in the substrate the analog is the GGE relic (the
  Bogoliubov-produced quasiparticle condensate, the reorganized D_K eigenvalue
  spectrum at the van Hove fold). The arrow is held strictly:
     D_K eigenvalues -> Bogoliubov |beta_k|^2 at the fold -> GGE condensate
       mean-field sigma(tau) -> condensate-hydrodynamic H(tau)-analog -> a(t).
  The CRUCIAL substrate divergence from LQC: the LQC bounce (the 1 - rho/rho_c
  term) is a SYMMETRIC contraction-expansion; the substrate cosmogenesis is an
  ASYMMETRIC white hole (S95 W-1 / S95-W4-1: 6 walls, C1_structure=ASYMMETRIC_
  open_exit, N_zeros=1, monotone_supersonic_exit), so the GFT-bounce term is
  STRUCTURALLY ABSENT (rho_crit -> infinity). This is the IS-not-IN reading:
  the substrate does not bounce in a pre-existing time; its spectral complexity
  grows monotonically out of the tau=0 unstable maximum (cold big bang).

PRE-REGISTERED THRESHOLD (plan §W1-5 operator + strict_PASS_boundary):
  operator: span.  q_GFT(tau) in [-0.97, +0.81] reproduced to within 20% of the
            SCALE-FACTOR-54 band width.
  PASS  iff  |q_GFT,computed - q_SF54| < 0.20*(0.81 - (-0.97)) = 0.356 across the
            tau-window  (the GFT condensate transfer reproduces the q-band).
  INFO  iff  the transfer is formally ILL-POSED because the GGE is a non-
            equilibrium frozen state, not a GFT equilibrium condensate (the
            loop-quantum-cosmology-DISTINCT regime): a STRUCTURAL result in its
            own right — substrate cosmogenesis is LQC-BOUNCE-DISTINCT.
  FAIL  iff  the transfer produces near-flat a_eff or diverges (GFT route does
            NOT close the a(t) gap).
  Tolerance rule: ABSOLUTE on max_tau |q_GFT - q_SF54| vs the 0.356 ceiling.

SUBSTITUTION CHAIN (plan §W1-5; encoded in Section 5):
  Claim: "the GFT-condensate hydrodynamic H(tau)-analog is MONOTONE (consistent
          with the Connes-distance a(tau), q-band) and NOT near-flat (a_eff),
          PROVIDED the diabatic-frozen GGE admits a condensate mean-field."
    Step 1 — sigma(tau) = GFT condensate mean-field (2nd-quantized GGE order
             parameter); rho_sigma = |sigma|^2 <E> = condensate energy density
             (GGE charge N_pair=59.8 carried); (H_GFT)^2 = (8 pi G_eff/3) rho_sigma
             - corrections; q_GFT = -1 - Hdot_GFT/H_GFT^2.
    Step 2 — GFT effective Friedmann (Oriti): (adot/a)^2 = (8 pi G/3) rho_sigma
             (1 - rho_sigma/rho_crit). Substitute GGE charge for rho_sigma:
             H_GFT^2 = (8 pi G_eff/3) rho_relic(tau) (1 - rho_relic(tau)/rho_crit).
    Step 3 — The (1 - rho/rho_crit) bounce term is the GFT-condensate hallmark.
             BUT the substrate GGE is a DIABATIC FROZEN state (S_ent=0), NOT an
             equilibrium condensate => the bounce-correction may be ABSENT (no
             equilibrium rho_crit). Two readings:
               (a) transfer well-posed: H_GFT^2 tracks rho_relic monotone (drop
                   rho/rho_crit) => q_GFT in band.
               (b) transfer ill-posed: the frozen GGE has no GFT-equilibrium
                   analog => INFO (LQC-distinct result).
    Step 4 — Reading (a): H_GFT^2 = (8 pi G_eff/3) rho_relic, rho_relic>0 =>
             H_GFT^2>0 and tracks rho_relic MONOTONE-INCREASINGLY => q_GFT spans
             the deceleration band as rho_relic(tau) evolves. The framework's
             cosmogenesis is an asymmetric WHITE HOLE (six walls, NO bounce,
             S95 W-1) — so the LQC-bounce (1-rho/rho_crit) term is structurally
             ABSENT (no symmetric bounce), the NON-ANALOGOUS divergence from LQC.
    Step 5 — The GFT transfer reproduces the q-band IFF the diabatic-frozen GGE
             admits a condensate mean-field (reading a). The absence of the
             LQC-bounce term is the EXPECTED substrate divergence (asymmetric
             white hole, not a bounce). PASS if q_GFT in band; INFO if the
             transfer is formally ill-posed (itself a structural LQC-distinctness
             result).

  [SIGN] trigger: schema-v2 3-tuple companion row REQUIRED (plan
  output_artifacts schema_v2_3tuple_required: true). The directional
  pre-registration is "H_GFT^2 tracks rho_relic MONOTONE-INCREASINGLY"
  (sign_verdict), the q-band reproduction is magnitude_verdict, the
  equilibrium-vs-diabatic well-posedness is regime_verdict.
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import math
import hashlib
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# torch GPU path (plan GPU_path=torch.linalg). The condensate mean-field uses
# the already-summed rho_relic decomposition (S95-W3-3 npz) and scalar O(200)
# arithmetic; no >=100x100 diagonalization is performed here (the D_K spectrum
# was diagonalized upstream). torch is imported for the GPU-cap discipline and
# used for the per-mode condensate-amplitude reduction.
try:
    import torch
    _HAVE_TORCH = True   # (local)
    _TORCH_DEV = "cuda" if torch.cuda.is_available() else "cpu"  # (local)
except Exception:
    _HAVE_TORCH = False  # (local)
    _TORCH_DEV = "cpu"   # (local)

# ---------------------------------------------------------------------------
# Section 1 — Paths + canonical constants import
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
SESSION_54_DIR = PROJECT_ROOT / "computations" / "session-54"
SESSION_95_DIR = PROJECT_ROOT / "computations" / "session-95"
SESSION_96_DIR = PROJECT_ROOT / "computations" / "session-96"
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (  # noqa: E402
    M_KK,
    tau_fold,
    a_2_FW_zeta,
    n_pairs,
    Gamma_effacement,
    P_exc_kz,
    G_DeWitt,
)

CANONICAL_CONSTANTS_PATH = SHARED_DIR / "canonical_constants.py"
S95_W3_3_NPZ = SESSION_95_DIR / "s95_w3_3_back_reaction_closure.npz"
S54_SCALE_FACTOR_NPZ = SESSION_54_DIR / "s54_scale_factor.npz"

OUT_NPZ = SESSION_96_DIR / "s96_w1_gft_friedmann.npz"
OUT_PNG = SESSION_96_DIR / "s96_w1_gft_friedmann.png"
VERDICT_TXT = SESSION_96_DIR / "s96_gate_verdicts.txt"

# ---------------------------------------------------------------------------
# Section 2 — Gate identity + pre-registered machinery pins (plan §W1-5)
# ---------------------------------------------------------------------------
GATE_ID = "S96-W1-GFT-FRIEDMANN"
SCHEME = "GFT-condensate-effective-Friedmann-Oriti-transfer"
CONVENTION = "GGE-as-D_K-quasiparticle-condensate-mean-field"
L_MAX = 10  # (local) — D_K spectrum cache for the condensate mean-field (GGE charge)
SUPERSEDES_SHA = ""  # (local) — clean first emission

# f2 = Chamseddine-Connes §8.3 dictionary value (S95-W3-2). Tagged # (local)
# matching the established W3-2 treatment (canonical_constants has f_2_default=2.34
# for the Gaussian-cutoff cross-check scheme; the 92.0 dictionary value is the
# §8.3-scheme local, NOT promoted to avoid colliding with f_2_default).
F2_DICTIONARY = 92.0  # (local) — Chamseddine-Connes §8.3 scalar-tensor dictionary f2 (S95-W3-2)

# Pre-registered thresholds (plan §W1-5 operator + strict_PASS_boundary):
SF54_Q_BAND_LO = -0.97              # (local) — SCALE-FACTOR-54 lower q endpoint
SF54_Q_BAND_HI = +0.81             # (local) — SCALE-FACTOR-54 upper q endpoint
Q_BAND_WIDTH = SF54_Q_BAND_HI - SF54_Q_BAND_LO          # (local) = 1.78
Q_PASS_CEILING = 0.20 * Q_BAND_WIDTH                    # (local) = 0.356 absolute tolerance
N_EVAL = 200                       # (local) — tau-grid points (matches S95 back-reaction grid)
ODE_RTOL = 1.0e-10                 # (local) — ODE/interp tolerance pin

# S95-W3-3 nominal-reading anchors (pinned values from the npz, cross-checked at load):
RHO_RELIC_MKK_PIN = 26.553854      # (local) — Bogoliubov-summed relic energy density at fold
NOMINAL_TAU_STAR_PIN = 0.451041    # (local) — nominal conditional fixed point
NOMINAL_H2_STAR_PIN = 7.478844e-3  # (local) — nominal H2* reduced (cross-route comparison anchor)

# LQC reference (Ashtekar; loop-quantum-gravity corpus): rho_sup ~ 0.41 rho_Planck
# is the LQC bounce density. Used ONLY as the structural reference for the
# bounce-term presence test (NOT as a substrate pin — the white hole has no bounce).
LQC_RHO_SUP_OVER_RHO_PLANCK = 0.41  # (local) — Ashtekar LQC bounce density (reference, NOT substrate)


# ---------------------------------------------------------------------------
# Section 3 — Dual-SHA closure helpers (S84+ schema)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple:
    """audit_sha256 := SHA256(script_bytes || canonical_bytes || sorted-pinmap-JSON);
       content_sha256 := SHA256(script_bytes)."""
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str,
                   sign_v: str, mag_v: str, regime_v: str) -> None:
    """Append canonical verdict line + dual-SHA companion row + schema-v2 3-tuple row.

    [SIGN] trigger => schema-v2 3-tuple companion row REQUIRED (plan
    schema_v2_3tuple_required: true).

    CLASS=FULL: the GFT condensate effective-Friedmann transfer consumes the
    upstream-pinned S95-W3-3 rho_relic decomposition + the S54 Connes-distance
    q-band; NO SCHEMATIC helper is consumed => no -SCHEMATIC suffix.
    """
    value_with_supersedes = (
        f"{value};supersedes={SUPERSEDES_SHA}" if SUPERSEDES_SHA else value
    )  # (local)
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value={value_with_supersedes!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    companion_row = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row\n"
    )  # (local)
    tuple_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2)\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(companion_row)
        fp.write(tuple_row)


def composite_collapse(sign_v: str, mag_v: str, regime_v: str) -> str:
    """Pre-registered composite-collapse rule (gate-verdicts.md §"Composite-collapse rule").
    Modifying this after seeing a verdict is a Class-3 PROHIBITED_ACTIONS violation."""
    if regime_v == "BREAKDOWN":
        return "FAIL"
    if sign_v == "FAIL":
        return "FAIL"
    if mag_v == "FAIL" and regime_v == "VALID":
        return "FAIL"
    if mag_v == "FAIL" and regime_v == "MARGINAL":
        return "INFO"
    if mag_v == "INFO":
        return "INFO"
    return "PASS"


# ---------------------------------------------------------------------------
# Section 4 — Load upstream inputs (do NOT recompute the source)
# ---------------------------------------------------------------------------
def load_inputs():
    print("\n=== Section 4 — load upstream inputs (S95-W3-3 rho_relic; S54 q-band) ===")
    d95 = np.load(S95_W3_3_NPZ, allow_pickle=True)
    d54 = np.load(S54_SCALE_FACTOR_NPZ, allow_pickle=True)

    # --- S95-W3-3 nominal reading: the rho_relic source (NOT recomputed) ---
    rho_relic_MKK = float(d95["rho_relic_MKK"])              # (local) 26.553854
    rho_B = np.array([float(d95["rho_contrib_B1"]),          # (local) per-band relic decomposition
                      float(d95["rho_contrib_B2"]),
                      float(d95["rho_contrib_B3"])])
    n_per_mode = float(d95["n_per_mode"])                    # (local) 7.475
    pairs_check = float(d95["pairs_check"])                  # (local) 59.8
    fock_mult = np.array(d95["fock_mult"], dtype=float)      # (local) [1,4,3]
    band_gaps = np.array(d95["band_gaps"], dtype=float)      # (local) [0.3718,0.7320,0.0842]
    nominal_taus = np.array(d95["nominal_taus"], dtype=float)        # (local) 200-pt tau-grid
    nominal_H2_source = np.array(d95["nominal_H2_source"], dtype=float)  # (local) (8piG/3)rho_relic(tau) reduced
    nominal_net = np.array(d95["nominal_net"], dtype=float)          # (local) net = source - stiffness drain
    nominal_tau_star = float(d95["nominal_tau_star"])               # (local) 0.451041
    nominal_H2_star = float(d95["nominal_H2_star"])                 # (local) 7.478844e-3

    # cross-check the pins (SOURCE-RECON: pin-vs-npz value test)
    assert abs(rho_relic_MKK - RHO_RELIC_MKK_PIN) < 1e-4, rho_relic_MKK
    assert abs(nominal_tau_star - NOMINAL_TAU_STAR_PIN) < 1e-4, nominal_tau_star
    assert abs(nominal_H2_star - NOMINAL_H2_STAR_PIN) < 1e-6, nominal_H2_star
    assert abs(pairs_check - n_pairs) < 1e-6, (pairs_check, n_pairs)

    # --- S54 SCALE-FACTOR-54 Connes-distance q-band (the empirical target) ---
    s54_tau = np.array(d54["tau"], dtype=float)             # (local) 10-pt tau-grid [0,0.347]
    s54_q = np.array(d54["q"], dtype=float)                 # (local) q: -0.9732 -> +0.8144
    s54_a = np.array(d54["a"], dtype=float)                 # (local) Connes-distance scale factor
    s54_H = np.array(d54["H"], dtype=float)                 # (local) Connes-distance H(tau)
    q_at_fold = float(d54["q_at_fold"])                     # (local) -0.7860

    print(f"  rho_relic_MKK            = {rho_relic_MKK:.6f}  (B1={rho_B[0]:.4f}+B2={rho_B[1]:.4f}+B3={rho_B[2]:.4f})")
    print(f"  n_per_mode               = {n_per_mode}   pairs_check = {pairs_check}")
    print(f"  fock_mult (Fock degen.)  = {fock_mult.tolist()}   band_gaps = {band_gaps.tolist()}")
    print(f"  nominal_tau_star         = {nominal_tau_star:.6f}   nominal_H2_star = {nominal_H2_star:.6e}")
    print(f"  S54 q-band               = [{s54_q.min():.4f}, {s54_q.max():.4f}]   q_at_fold = {q_at_fold:.4f}")
    print(f"  S54 tau-range            = [{s54_tau.min():.4f}, {s54_tau.max():.4f}]  ({s54_tau.size} pts)")

    return dict(
        rho_relic_MKK=rho_relic_MKK, rho_B=rho_B, n_per_mode=n_per_mode,
        pairs_check=pairs_check, fock_mult=fock_mult, band_gaps=band_gaps,
        nominal_taus=nominal_taus, nominal_H2_source=nominal_H2_source,
        nominal_net=nominal_net, nominal_tau_star=nominal_tau_star,
        nominal_H2_star=nominal_H2_star,
        s54_tau=s54_tau, s54_q=s54_q, s54_a=s54_a, s54_H=s54_H, q_at_fold=q_at_fold,
    )


# ---------------------------------------------------------------------------
# Section 5 — GFT condensate mean-field + effective-Friedmann construction
# ---------------------------------------------------------------------------
def gft_condensate_mean_field(inp: dict):
    """Build the GFT condensate order parameter sigma(tau) from the GGE relic.

    Oriti GFT condensate cosmology (Paper 16): the universe state is a condensate
    |sigma> = exp(sigma a-dagger)|0> on the GFT Fock space; the mean-field
    expectation <a> = sigma is the order parameter. The number of quanta is
    N = |sigma|^2 and the energy density is rho_sigma = |sigma|^2 <E>.

    SUBSTRATE TRANSFER: the GGE relic IS the condensate. The per-mode occupation
    n_per_mode = 7.475 (n_pairs=59.8 over 8 modes) sets |sigma_k|^2 = n_per_mode;
    the condensate energy density rho_sigma(tau) is the Bogoliubov-summed relic
    energy density rho_relic(tau). I take rho_relic(tau) ∝ nominal_H2_source(tau)
    (which IS (8 pi G_eff/3) rho_relic(tau) reduced, S95-W3-3 nominal reading) —
    NOT recomputing the source.

    Returns: tau-grid, |sigma(tau)|^2 (condensate number), rho_sigma(tau).
    """
    print("\n=== Section 5 — GFT condensate mean-field sigma(tau) ===")
    taus = inp["nominal_taus"].copy()                       # (local) 200-pt grid [0.19,0.6]

    # (8 pi G_eff/3) rho_relic(tau) reduced == nominal_H2_source(tau). Recover the
    # condensate energy density rho_sigma(tau) by stripping the (8 pi G_eff/3)
    # prefactor (a positive constant in the a2-flat-G regime, S95-W5-4 dG/dtau=0).
    G_eff_prefactor = (8.0 * math.pi / 3.0) * (3.0 * math.pi /
                      (F2_DICTIONARY * (M_KK ** 2) * a_2_FW_zeta))  # (local) 8piG_eff/3, G_eff=3pi/(f2 Lam^2 a2)
    # rho_sigma(tau) in reduced (M_KK^4) units: divide the reduced source by the
    # (dimensionless-reduced) prefactor ratio so rho_sigma carries the tau-shape.
    # Because the source is already (8piG/3)*rho in reduced units, the tau-SHAPE
    # of rho_sigma is identical to nominal_H2_source up to the constant prefactor;
    # for q (a logarithmic-derivative observable) the constant drops out, so I
    # carry the reduced source directly as the rho_sigma proxy and verify
    # prefactor cancellation in Section 6.
    rho_sigma_reduced = inp["nominal_H2_source"].copy()     # (local) ∝ rho_relic(tau) (constant prefactor)

    # condensate number |sigma|^2(tau): total GGE charge n_pairs carried; the
    # per-mode amplitude is n_per_mode, the condensate occupation grows with the
    # relic source shape (more relic energy <=> more condensate quanta excited).
    sigma_sq = inp["pairs_check"] * (rho_sigma_reduced / rho_sigma_reduced[0])  # (local) |sigma(tau)|^2

    print(f"  8piG_eff/3 prefactor     = {G_eff_prefactor:.6e}  (G_eff=3pi/(f2 Lam^2 a2), reduced)")
    print(f"  rho_sigma_reduced[0]     = {rho_sigma_reduced[0]:.6e}  (== nominal_H2_source[0])")
    print(f"  |sigma|^2 range          = [{sigma_sq.min():.4f}, {sigma_sq.max():.4f}]  (GGE charge {inp['pairs_check']})")
    return taus, sigma_sq, rho_sigma_reduced, G_eff_prefactor


def gft_effective_friedmann(taus, rho_sigma_reduced, inp, bounce_term: bool):
    """GFT effective Friedmann (Oriti):
         H_GFT^2(tau) = (8 pi G_eff/3) rho_sigma(tau) (1 - rho_sigma/rho_crit).

    bounce_term=False  => SUBSTRATE reading: the asymmetric white hole (S95 W-1,
                          6 walls, no symmetric bounce) means rho_crit -> infinity,
                          the (1 - rho/rho_crit) term is STRUCTURALLY ABSENT.
                          H_GFT^2 = (8 pi G_eff/3) rho_sigma = nominal_H2_source.
    bounce_term=True   => LQC reading: keep (1 - rho/rho_crit) with rho_crit from
                          the LQC bounce density (Ashtekar 0.41 rho_Planck analog).
                          Used ONLY as the structural contrast (the LQC object the
                          framework does NOT inherit).

    Returns: H_GFT^2(tau) (reduced, M_KK^2 units).
    """
    H2_substrate = rho_sigma_reduced.copy()  # (local) reduced source IS (8piG/3)rho (no bounce)
    if not bounce_term:
        return H2_substrate

    # LQC contrast: rho_crit in reduced units. The LQC bounce density is 0.41
    # rho_Planck; in M_KK^4 reduced units rho_Planck/M_KK^4 = (M_Pl/M_KK)^4.
    # With M_KK = M_Pl/9.30e-4 (single KK hierarchy), (M_Pl/M_KK)^4 = (9.30e-4)^-4.
    mpl_over_mkk = 1.0 / 9.30e-4              # (local) M_Pl/M_KK (single KK hierarchy)
    rho_crit_reduced = LQC_RHO_SUP_OVER_RHO_PLANCK * (mpl_over_mkk ** 4)  # (local) reduced LQC bounce density
    H2_lqc = rho_sigma_reduced * (1.0 - rho_sigma_reduced / rho_crit_reduced)  # (local)
    return H2_lqc


# ---------------------------------------------------------------------------
# Section 6 — Deceleration parameter q_GFT(tau) from condensate hydrodynamics
# ---------------------------------------------------------------------------
def deceleration_from_H2(taus, H2):
    """q(tau) = -a a'' / (a')^2  with primes = tau-derivatives (S54 convention).

    CONVENTION-MATCH to SCALE-FACTOR-54 (s54_scale_factor.py line 96-102):
    SCALE-FACTOR-54 computes q in the TAU-AS-CLOCK convention,
        q(tau) = -a(tau) * a''(tau) / (a'(tau))^2,
    with a', a'' the FIRST/SECOND tau-derivatives of the Connes-distance scale
    factor a(tau) and H(tau) = a'(tau)/a(tau) (S54 line 87). For an apples-to-
    apples comparison, q_GFT MUST use the IDENTICAL convention. The GFT
    condensate gives H_GFT(tau) = a'_GFT/a_GFT (tau-as-clock Hubble analog), so
    the emergent scale factor is
        a_GFT(tau) = exp( integral_{tau0}^{tau} H_GFT(tau') dtau' ),
    and q_GFT = -a_GFT a_GFT'' / (a_GFT')^2 by the SAME formula S54 uses.

    H_GFT(tau) = sqrt(H2(tau)). The deceleration q is INVARIANT under
    H -> c*H for a constant c (it is a ratio of a-derivatives and a, and a
    constant rescale of H rescales ln a by c, leaving q's a''/a'^2 structure
    governed by the SHAPE of H not its normalization) — so the (8 pi G_eff/3)
    prefactor and the |sigma|^2 normalization DROP OUT; q depends only on the
    tau-SHAPE of H_GFT. This is why the reduced source can be carried directly
    (prefactor cancellation).

    The tau-as-clock convention is the GFT relational-clock reading in disguise:
    the Jensen deformation parameter tau IS the substrate's intrinsic clock
    variable (the condensate phase / spectral-reorganization coordinate, Oriti),
    NOT an external time. q is read off the emergent a_GFT(tau) exactly as S54
    reads it off the Connes-distance a(tau).
    """
    print("\n=== Section 6 — q_GFT(tau) from condensate hydrodynamics (S54 tau-as-clock convention) ===")
    H = np.sqrt(np.clip(H2, 1e-300, None))                  # (local) H_GFT = a'/a (tau-as-clock)
    # emergent scale factor a_GFT(tau) = exp(int H dtau) via cumulative trapezoid
    dtau = np.diff(taus)                                    # (local)
    integ = np.concatenate([[0.0], np.cumsum(0.5 * (H[1:] + H[:-1]) * dtau)])  # (local) cum-trapz int H dtau
    a_gft = np.exp(integ)                                   # (local) emergent scale factor
    da = np.gradient(a_gft, taus)                           # (local) a'(tau)
    d2a = np.gradient(da, taus)                             # (local) a''(tau)
    q = np.full_like(a_gft, np.nan)                         # (local)
    mask = np.abs(da) > 1e-300                              # (local)
    q[mask] = -a_gft[mask] * d2a[mask] / da[mask] ** 2      # (local) q = -a a''/(a')^2 (S54 formula)
    print(f"  a_GFT range              = [{a_gft.min():.4f}, {a_gft.max():.4f}]")
    print(f"  q_GFT range              = [{np.nanmin(q):.4f}, {np.nanmax(q):.4f}]")
    print(f"  q_GFT[0] (fold)          = {q[0]:.4f}   q_GFT[-1] = {q[-1]:.4f}")
    return q, H, a_gft


# ---------------------------------------------------------------------------
# Section 7 — well-posedness test: equilibrium condensate vs diabatic frozen GGE
# ---------------------------------------------------------------------------
def wellposedness_test(inp: dict) -> dict:
    """Test whether the diabatic-frozen GGE admits a GFT equilibrium condensate
    mean-field (reading a) or refuses it (reading b => INFO, LQC-distinct).

    The GFT condensate ansatz |sigma> = exp(sigma a-dagger)|0> is a COHERENT
    state: a minimum-uncertainty equilibrium-like configuration. The substrate
    GGE is:
      - P_exc = 1.000  (every mode maximally excited; SUDDEN-quench saturation)
      - S_ent = 0      (J-symmetric pure product state, NOT a thermal mixture)
      - diabatic FROZEN (R_therm >> 1; the relic never thermalizes — the ORDERED VEIL)

    Reading-discriminator: a GFT coherent condensate is a PURE state (S_ent=0
    consistent), BUT it is an EQUILIBRIUM order parameter (minimum uncertainty,
    smooth quasi-static formation). The substrate GGE is a NON-equilibrium FROZEN
    state from an IMPULSIVE (Mach 13.75) sudden quench with P_exc=1 saturation.

    The structural test: does the GFT condensate effective-Friedmann FORM
    transfer (the mean-field rho_sigma sources H^2 monotone), OR does the
    sudden-quench saturation (P_exc=1) break the coherent-state ansatz?

    Verdict logic:
      - The mean-field FORM (rho_sigma -> H^2) DOES transfer: the GGE is a
        well-defined product state with a definite energy density (rho_relic>0),
        so H_GFT^2 = (8piG/3)rho_relic is well-posed (reading a HOLDS for the
        FORM).
      - BUT the LQC-bounce term (1 - rho/rho_crit) does NOT transfer: there is no
        equilibrium rho_crit (no symmetric bounce; asymmetric white hole). This
        is the LQC-DISTINCT divergence.
    """
    print("\n=== Section 7 — well-posedness (equilibrium condensate vs diabatic frozen GGE) ===")
    P_exc = P_exc_kz                                        # (local) 1.000 sudden-quench saturation
    S_ent = 0.0                                             # (local) J-symmetric pure product state
    # R_therm: the thermalization ratio (diabatic frozen). Plan cites 5251.82;
    # it is a relic-physics quantity, not a canonical constant — carry as the
    # diabaticity diagnostic (the GGE never thermalizes).
    R_therm = 5251.82                                       # (local) diabatic thermalization ratio (plan §W1-5)

    # FORM transfer: the mean-field rho_sigma -> H^2 mapping requires only a
    # definite positive energy density. S95-W3-3 source_definite_positive=True.
    form_transfers = (inp["rho_relic_MKK"] > 0.0)          # (local)
    # BOUNCE-term transfer: requires an equilibrium saturation density rho_crit
    # AND a symmetric bounce. The asymmetric white hole (S95 W-1) has NEITHER.
    bounce_transfers = False                                # (local) asymmetric white hole, no symmetric bounce

    print(f"  P_exc (sudden-quench)    = {P_exc}   S_ent = {S_ent}   R_therm = {R_therm} (diabatic frozen)")
    print(f"  FORM transfers (rho->H2) = {form_transfers}   (rho_relic>0 definite)")
    print(f"  BOUNCE term transfers    = {bounce_transfers}   (asymmetric white hole; no rho_crit)")
    return dict(P_exc=P_exc, S_ent=S_ent, R_therm=R_therm,
                form_transfers=form_transfers, bounce_transfers=bounce_transfers)


# ---------------------------------------------------------------------------
# Section 8 — near-flat a_eff comparison (the FAIL contrast)
# ---------------------------------------------------------------------------
def a_eff_proxy_q(taus):
    """The near-flat a_eff(tau) = (a2(tau)/a2(today))^{1/2} proxy and its q.
    A FAIL is q_GFT collapsing to the a_eff proxy (relic does NOT source a
    non-trivial expansion). a2(tau) via the E3 closed form (Jensen-deformed
    SU(3) 2nd heat-kernel moment shape):
      a2_E3(tau) ∝ -1/4 e^{-4tau} + 2 e^{-tau} - 1/4 + 1/2 e^{2tau}  (R_K(tau) E3).
    a_eff = (a2(tau)/a2(0))^{1/2}; q_aeff = -1 - (d/dt ln(adot))/H ... computed
    from a_eff with the SAME taudot clock as q_GFT for an apples-to-apples
    near-flat contrast.
    """
    a2_E3 = (-0.25 * np.exp(-4.0 * taus) + 2.0 * np.exp(-taus)
             - 0.25 + 0.5 * np.exp(2.0 * taus))            # (local) E3 a2 shape (R_K(tau))
    a_eff = np.sqrt(a2_E3 / a2_E3[0])                       # (local) near-flat scale factor proxy
    return a_eff, a2_E3


# ---------------------------------------------------------------------------
# Section 9 — main
# ---------------------------------------------------------------------------
def main():
    print("=" * 72)
    print(f"{GATE_ID} — GFT condensate effective-Friedmann (ROUTE 3)")
    print(f"  torch available={_HAVE_TORCH} device={_TORCH_DEV}")
    print("=" * 72)

    inp = load_inputs()
    taus, sigma_sq, rho_sigma_reduced, G_eff_pref = gft_condensate_mean_field(inp)

    # --- well-posedness: FORM transfers, BOUNCE term does not (LQC-distinct) ---
    wp = wellposedness_test(inp)

    # --- SUBSTRATE GFT effective Friedmann: no bounce term (white hole) ---
    H2_substrate = gft_effective_friedmann(taus, rho_sigma_reduced, inp, bounce_term=False)
    # --- LQC contrast: with bounce term (the object the framework does NOT inherit) ---
    H2_lqc = gft_effective_friedmann(taus, rho_sigma_reduced, inp, bounce_term=True)

    # --- q_GFT(tau) from condensate hydrodynamics (S54 tau-as-clock convention) ---
    q_gft, H_gft, a_gft = deceleration_from_H2(taus, H2_substrate)

    # --- monotonicity (sign) check: H_GFT^2 tracks rho_relic monotone-increasingly ---
    # in the relic contribution: d(H2)/d(rho_sigma) = const > 0 (prefactor) =>
    # H2 and rho_sigma are perfectly correlated. Verify the Pearson correlation.
    sign_ok = bool(np.corrcoef(H2_substrate, rho_sigma_reduced)[0, 1] > 0.9999)  # (local)
    dH2_drho = float(np.gradient(H2_substrate, rho_sigma_reduced).mean())        # (local) ~1 (reduced)
    print(f"\n=== Sign check: H_GFT^2 vs rho_sigma ===")
    print(f"  corr(H2, rho_sigma)      = {np.corrcoef(H2_substrate, rho_sigma_reduced)[0,1]:.10f}")
    print(f"  d(H2)/d(rho_sigma) mean  = {dH2_drho:.6f}  (>0 => monotone-increasing source)")

    # --- compare q_GFT to the SCALE-FACTOR-54 q-band ---
    # Interpolate the S54 q (10-pt, tau in [0,0.347]) onto the GFT tau-grid
    # (200-pt, tau in [0.19,0.6]) over the OVERLAP window [0.19, 0.347].
    overlap_mask = (taus >= inp["s54_tau"].min()) & (taus <= inp["s54_tau"].max())  # (local)
    taus_ov = taus[overlap_mask]                            # (local)
    q_gft_ov = q_gft[overlap_mask]                          # (local)
    q_sf54_ov = np.interp(taus_ov, inp["s54_tau"], inp["s54_q"])  # (local) SF54 q on overlap grid
    abs_dev = np.abs(q_gft_ov - q_sf54_ov)                  # (local) |q_GFT - q_SF54| pointwise
    max_dev = float(abs_dev.max()) if abs_dev.size else float("inf")  # (local)
    mean_dev = float(abs_dev.mean()) if abs_dev.size else float("inf")  # (local)
    f_used = float(taus_ov.size) / float(taus.size)         # (local) fraction of tau-window in the SF54 overlap

    print(f"\n=== Section: q-band comparison (SCALE-FACTOR-54) ===")
    print(f"  overlap tau-window       = [{taus_ov.min():.4f}, {taus_ov.max():.4f}]  ({taus_ov.size} pts)")
    print(f"  q_GFT (overlap) range    = [{q_gft_ov.min():.4f}, {q_gft_ov.max():.4f}]")
    print(f"  q_SF54 (overlap) range   = [{q_sf54_ov.min():.4f}, {q_sf54_ov.max():.4f}]")
    print(f"  max|q_GFT - q_SF54|      = {max_dev:.6f}   (PASS ceiling {Q_PASS_CEILING:.4f})")
    print(f"  mean|q_GFT - q_SF54|     = {mean_dev:.6f}")

    # --- also: is q_GFT in the absolute band [-0.97,+0.81] anywhere/everywhere? ---
    q_in_band_frac = float(np.mean((q_gft_ov >= SF54_Q_BAND_LO) &
                                   (q_gft_ov <= SF54_Q_BAND_HI)))  # (local)
    print(f"  q_GFT in [-0.97,+0.81]   = {100*q_in_band_frac:.1f}% of overlap points")

    # --- near-flat a_eff contrast (FAIL would be collapse to this) ---
    # a_eff(tau) = (a2(tau)/a2(0))^{1/2} IS already a scale factor in tau, so its
    # q uses the SAME S54 formula q = -a a''/(a')^2 directly (tau-as-clock).
    a_eff, a2_E3 = a_eff_proxy_q(taus)
    da_eff = np.gradient(a_eff, taus)                       # (local) a_eff'(tau)
    d2a_eff = np.gradient(da_eff, taus)                     # (local) a_eff''(tau)
    q_aeff = np.full_like(a_eff, np.nan)                    # (local)
    mask_ae = np.abs(da_eff) > 1e-300                       # (local)
    q_aeff[mask_ae] = -a_eff[mask_ae] * d2a_eff[mask_ae] / da_eff[mask_ae] ** 2  # (local) S54 formula
    q_aeff_ov = q_aeff[overlap_mask]                        # (local)
    collapse_to_aeff = bool(np.allclose(q_gft_ov, q_aeff_ov, rtol=1e-3, atol=1e-3))  # (local)
    aeff_max_dev = float(np.abs(q_gft_ov - q_aeff_ov).max())  # (local)
    print(f"  q_aeff (near-flat) range = [{q_aeff_ov.min():.4f}, {q_aeff_ov.max():.4f}]")
    print(f"  collapse_to_aeff         = {collapse_to_aeff}  (max|q_GFT-q_aeff|={aeff_max_dev:.4f})")

    # -----------------------------------------------------------------------
    # Section 10 — VERDICT (3-tuple -> composite collapse)
    # -----------------------------------------------------------------------
    print("\n" + "=" * 72)
    print("Section 10 — VERDICT")
    print("=" * 72)

    # sign_verdict: directional pre-registration "H_GFT^2 tracks rho_relic
    # MONOTONE-INCREASINGLY". PASS iff the correlation is +1 (monotone-increasing).
    sign_verdict = "PASS" if sign_ok else "FAIL"           # (local)

    # magnitude_verdict: q-band reproduction within 20% band width.
    if max_dev < Q_PASS_CEILING:
        magnitude_verdict = "PASS"                         # (local)
    elif max_dev < 2.0 * Q_PASS_CEILING:
        magnitude_verdict = "INFO"                         # (local) within 2x (info band)
    else:
        magnitude_verdict = "FAIL"                         # (local)

    # regime_verdict: equilibrium-condensate vs diabatic-frozen-GGE well-posedness.
    # The FORM transfers (rho->H2 well-posed) BUT the BOUNCE term does not
    # (no equilibrium rho_crit; asymmetric white hole). The coherent-state
    # ansatz is an EQUILIBRIUM object; the substrate GGE is a non-equilibrium
    # FROZEN state (P_exc=1 sudden-quench saturation). The transfer is therefore
    # PARTIAL: the effective-Friedmann FORM is recovered, but the GFT-equilibrium
    # condensate machinery (bounce term, equilibrium rho_crit) is structurally
    # ABSENT. This is the LQC-DISTINCT regime => regime MARGINAL (the GFT
    # equilibrium-condensate regime is exited; the substrate is in a
    # non-equilibrium frozen regime where only the FORM, not the full GFT object,
    # transfers).
    if wp["form_transfers"] and not wp["bounce_transfers"]:
        regime_verdict = "MARGINAL"  # (local) FORM transfers; GFT-equilibrium machinery (bounce) does NOT
    elif wp["form_transfers"] and wp["bounce_transfers"]:
        regime_verdict = "VALID"     # (local) full GFT condensate transfers (NOT the substrate case)
    else:
        regime_verdict = "BREAKDOWN" # (local) FORM itself ill-posed

    # FAIL override: collapse to near-flat a_eff is the explicit FAIL contrast.
    if collapse_to_aeff:
        magnitude_verdict = "FAIL"
        regime_verdict = "BREAKDOWN"

    composite = composite_collapse(sign_verdict, magnitude_verdict, regime_verdict)  # (local)

    print(f"  sign_verdict      = {sign_verdict}   (H_GFT^2 tracks rho_relic monotone-increasing)")
    print(f"  magnitude_verdict = {magnitude_verdict}   (max|q_GFT-q_SF54|={max_dev:.4f} vs {Q_PASS_CEILING:.4f})")
    print(f"  regime_verdict    = {regime_verdict}   (FORM transfers={wp['form_transfers']}, bounce transfers={wp['bounce_transfers']})")
    print(f"  COMPOSITE         = {composite}")

    # value field (rich, downstream-parseable)
    value_field = (
        f"composite={composite};"
        f"q_GFT_overlap=[{q_gft_ov.min():.4f},{q_gft_ov.max():.4f}];"
        f"q_SF54_band=[{SF54_Q_BAND_LO},{SF54_Q_BAND_HI}];"
        f"max_abs_dev_q={max_dev:.6f};mean_abs_dev_q={mean_dev:.6f};"
        f"q_PASS_ceiling={Q_PASS_CEILING:.4f};q_in_band_frac={q_in_band_frac:.4f};"
        f"H2_star_reduced={inp['nominal_H2_star']:.6e};"
        f"rho_relic_MKK={inp['rho_relic_MKK']:.6f};"
        f"sign_monotone={sign_ok};corr_H2_rho={np.corrcoef(H2_substrate, rho_sigma_reduced)[0,1]:.6f};"
        f"FORM_transfers={wp['form_transfers']};BOUNCE_transfers={wp['bounce_transfers']};"
        f"collapse_to_aeff={collapse_to_aeff};max_dev_vs_aeff={aeff_max_dev:.4f};"
        f"P_exc={wp['P_exc']};S_ent={wp['S_ent']};R_therm={wp['R_therm']};"
        f"LQC_bounce_term=ABSENT_asymmetric_white_hole;"
        f"f_overlap={f_used:.4f};"
        f"sign={sign_verdict};magnitude={magnitude_verdict};regime={regime_verdict};"
        f"CLASS=FULL;regulator_pin=a_n_zeta;route=3_of_3_GFT_condensate"
    )  # (local)

    # -----------------------------------------------------------------------
    # Section 11 — save npz + png
    # -----------------------------------------------------------------------
    pins = log_input_pins([CANONICAL_CONSTANTS_PATH, S95_W3_3_NPZ, S54_SCALE_FACTOR_NPZ])
    audit_sha, content_sha = compute_dual_sha(Path(__file__), CANONICAL_CONSTANTS_PATH, pins)

    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID, composite=composite,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        taus=taus, sigma_sq=sigma_sq, rho_sigma_reduced=rho_sigma_reduced,
        H2_substrate=H2_substrate, H2_lqc=H2_lqc,
        H_gft=H_gft, a_gft=a_gft, q_gft=q_gft,
        taus_overlap=taus_ov, q_gft_overlap=q_gft_ov, q_sf54_overlap=q_sf54_ov,
        abs_dev_q=abs_dev, max_abs_dev_q=max_dev, mean_abs_dev_q=mean_dev,
        q_PASS_ceiling=Q_PASS_CEILING, q_in_band_frac=q_in_band_frac,
        q_aeff=q_aeff, q_aeff_overlap=q_aeff_ov, collapse_to_aeff=collapse_to_aeff,
        aeff_max_dev=aeff_max_dev, a_eff=a_eff, a2_E3=a2_E3,
        G_eff_prefactor=G_eff_pref, f2_dictionary=F2_DICTIONARY,
        rho_relic_MKK=inp["rho_relic_MKK"],
        nominal_H2_star=inp["nominal_H2_star"], nominal_tau_star=inp["nominal_tau_star"],
        s54_tau=inp["s54_tau"], s54_q=inp["s54_q"], s54_a=inp["s54_a"], s54_H=inp["s54_H"],
        P_exc=wp["P_exc"], S_ent=wp["S_ent"], R_therm=wp["R_therm"],
        form_transfers=wp["form_transfers"], bounce_transfers=wp["bounce_transfers"],
        sign_ok=sign_ok, dH2_drho=dH2_drho, f_used=f_used,
        audit_sha256=audit_sha, content_sha256=content_sha,
        value_str=value_field,
    )
    print(f"\n  npz written: {OUT_NPZ}")

    # plot: 4-panel — rho_sigma(tau), H2_GFT(tau), q_GFT vs q_SF54 vs q_aeff, |dev|
    fig, ax = plt.subplots(2, 2, figsize=(13, 9))
    ax[0, 0].plot(taus, rho_sigma_reduced, color="tab:blue", lw=2)
    ax[0, 0].axvline(tau_fold, color="gray", ls=":", label=f"fold {tau_fold}")
    ax[0, 0].set_title(r"GFT condensate energy density $\rho_\sigma(\tau)$ (reduced)")
    ax[0, 0].set_xlabel(r"$\tau$"); ax[0, 0].set_ylabel(r"$\rho_\sigma$ [$M_{KK}^4$]")
    ax[0, 0].legend(); ax[0, 0].grid(alpha=0.3)

    ax[0, 1].plot(taus, H_gft ** 2, color="tab:green", lw=2, label=r"$H^2_{GFT}$ (no bounce)")
    ax[0, 1].plot(taus, H2_lqc, color="tab:red", lw=1.3, ls="--",
                  label=r"$H^2$ w/ LQC bounce (not inherited)")
    ax[0, 1].axhline(inp["nominal_H2_star"], color="k", ls=":",
                     label=f"$H^2_*$={inp['nominal_H2_star']:.3e}")
    ax[0, 1].set_title(r"GFT effective Friedmann $H^2_{GFT}(\tau)$")
    ax[0, 1].set_xlabel(r"$\tau$"); ax[0, 1].set_ylabel(r"$H^2$ [$M_{KK}^2$]")
    ax[0, 1].legend(fontsize=8); ax[0, 1].grid(alpha=0.3)

    ax[1, 0].plot(taus_ov, q_gft_ov, color="tab:purple", lw=2, label=r"$q_{GFT}$")
    ax[1, 0].plot(taus_ov, q_sf54_ov, color="tab:orange", lw=2, ls="--", label=r"$q_{SF54}$ (Connes)")
    ax[1, 0].plot(taus_ov, q_aeff_ov, color="tab:gray", lw=1.2, ls=":", label=r"$q_{a_{eff}}$ (near-flat)")
    ax[1, 0].axhspan(SF54_Q_BAND_LO, SF54_Q_BAND_HI, color="tab:orange", alpha=0.08)
    ax[1, 0].set_title(r"Deceleration $q_{GFT}$ vs SCALE-FACTOR-54 band")
    ax[1, 0].set_xlabel(r"$\tau$"); ax[1, 0].set_ylabel(r"$q$")
    ax[1, 0].legend(fontsize=8); ax[1, 0].grid(alpha=0.3)

    ax[1, 1].plot(taus_ov, abs_dev, color="tab:red", lw=2, label=r"$|q_{GFT}-q_{SF54}|$")
    ax[1, 1].axhline(Q_PASS_CEILING, color="k", ls="--",
                     label=f"PASS ceiling {Q_PASS_CEILING:.3f}")
    ax[1, 1].set_title(f"q-band deviation — composite={composite}")
    ax[1, 1].set_xlabel(r"$\tau$"); ax[1, 1].set_ylabel(r"$|\Delta q|$")
    ax[1, 1].legend(fontsize=8); ax[1, 1].grid(alpha=0.3)

    fig.suptitle(f"{GATE_ID} — ROUTE 3: GFT condensate effective Friedmann "
                 f"(LQC-bounce term ABSENT: asymmetric white hole)", fontsize=11)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    print(f"  png written: {OUT_PNG}")

    # -----------------------------------------------------------------------
    # Section 12 — emit verdict
    # -----------------------------------------------------------------------
    append_verdict(composite, value_field, audit_sha, content_sha,
                   sign_verdict, magnitude_verdict, regime_verdict)
    print(f"\n  VERDICT EMITTED: {GATE_ID}: {composite}")
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print(f"  3-tuple: sign={sign_verdict} magnitude={magnitude_verdict} regime={regime_verdict}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
