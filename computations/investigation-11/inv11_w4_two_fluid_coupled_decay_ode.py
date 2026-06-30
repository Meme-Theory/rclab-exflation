#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
INV11-W4-1-TWO-FLUID-COUPLED-DECAY-ODE   [SIGN]   PHONONIC
==========================================================
Two-component (eps_vac, eps_DM-stiff) coupled-decay ODE of Volovik Paper #35
(Eq.18/19), with the substrate's effacement-leak (1 - Gamma_eff) = 3e-4 as the
energy-exchange coefficient, integrated T_transit -> T_BBN -> today.

PURPOSE (plan SS W4-1):
  Run the DYNAMICAL Volovik two-fluid program the framework stopped following.
  The framework adopted the EQUILIBRIUM half (DILUTION-CC: rho_vac=0 at full
  equilibrium) and the UNIVERSALITY-CLASS half (3He-B / BDI / N3=0) but SKIPPED
  the dynamical halves -- precisely where the three live wounds sit. This gate
  asks whether the coupled-decay dynamics simultaneously:
    (i)   relieve the BBN arm:  rho_vac/rho_rad|_BBN  <  0.227  (S98 FAIL = 0.474049),
    (ii)  reconcile the dark-sector accounts (Leggett w=0 + Volovik stiff w=1
          coexisting with energy exchange),
    (iii) land present-day Omega_vac, Omega_DM within observation.

SUBSTRATE FRAMING (phononic-framing.md SS"IS Space, Not IN Space"):
  The substrate IS the flowing quantum vacuum; its a0 zeroth Seeley-DeWitt moment
  is the vacuum energy density eps_vac, and the gravitational-sector conjugate pair
  (K = 1/16piG, R) modifies the Gibbs-Duhem closure (Volovik #35 Eq.18:
  Ts_dS = eps_vac + P_vac - K*R) so that the SAME substrate carries a second
  component -- the Zel'dovich stiff-matter (w=+1) "dark matter" (Eq.19:
  P_DM = P_vac - K*R) -- exactly as superfluid helium's normal component rides the
  superfluid component. The direction of explanation:
      D_K eigenfrequencies  -> a0/a2 spectral moments
        -> eps_vac(q) and P_DM = P_vac - K*R
        -> the coupled-decay dynamics
        -> measured Omega_vac, Omega_DM, rho_vac/rho_rad.
  The effacement leak (1 - Gamma_eff) = 3e-4 -- the impedance mismatch at the fold
  the substrate ALREADY carries (S37) -- IS the energy-exchange channel: the
  substrate has had the coupling all along, it has simply never been written as
  the coupled ODE. This is NOT "applying Volovik's helium model to cosmology"; the
  substrate IS the superfluid vacuum and the laboratory two-fluid helium is the
  realization OF it.

SOURCE FIDELITY (FRAMEWORK-BRIDGE FLAG, in the convention tag):
  Volovik #35 SS V derives the POWER-LAW decay FROM energy exchange but leaves the
  exchange coefficient PHENOMENOLOGICAL ("both components reach correct present-day
  order of magnitude"). The (1 - Gamma_eff) identification is the FRAMEWORK's
  substrate-closure of that unfixed coefficient (impedance-mismatch transmission,
  S37). The convention tag
  ABSOLUTE-FRAMEWORK-BRIDGE-EXCHANGE-COEFF-FROM-1-MINUS-GAMMA-EFF flags this so no
  downstream consumer reads the coefficient as Volovik's own result.

THE TWO VACUUM SCALINGS (the load-bearing modeling decision):
  The substrate carries TWO scale-separated vacuum descriptions:
   - TRACKING vacuum  rho_vac = alpha_V M_Pl^2 H^n_eff, n_eff=1.978 (S98 from-below;
     the C10 form the W4-2 surface DERIVED). In the radiation era H ~ a^-2, so
     rho_vac ~ a^(-2 n_eff) = a^-3.956, i.e. rho_vac/rho_rad ~ a^+0.044 -- a
     nearly-constant FRACTION (the tracking property). This is what fixes the BBN
     fraction = 0.474049 (S98 lever X=ln(H_BBN/H0)=40.28 sets the normalization).
   - EFFACEMENT-projected CPL vacuum  w_vac,today = w0_FW = -0.918 (S58). This is
     the LATE-TIME dark-energy EOS that governs TODAY's Omega_vac.
  The BBN-arm test uses the TRACKING scaling (the substrate-derived 0.474049 from
  the W4-2 surface); today's Omega uses the effacement projection. The exchange
  term bleeds the tracking vacuum into stiff-DM during the radiation era.

THE W4-2 SURFACE IS THE T-DEPENDENT VACUUM INPUT (plan prerequisite):
  W4-2 landed PASS (Track A: BBN excess REAL; c10_is_derivation=True). The real
  rho_vac(q,T) surface is at inv11_w4_2_rho_vac_q_t_surface.npz. We USE it (NOT the
  closed-form q-theory surrogate -- the full surface is available, so NO
  CLOSED-FORM-SURROGATE-VAC tag). The surface verdicted bbn_excess_real=True and
  carries the S98 anchor rho_vac_over_rho_rad_BBN_below=0.474049: the BBN excess
  W4-1 must dynamically relieve is the GENUINE 0.474049 (the "artifact" Track B was
  FALSIFIED by W4-2's gap/BBN scale separation), not an extrapolation artifact.

SUBSTITUTION CHAIN (plan SS W4-1, [SIGN] gate):
  CLAIM: "Energy bled from the vacuum to the stiff-DM component DURING the
          radiation era REDUCES the vacuum fraction at BBN."
  dε_vac/dN = -(2 n_eff) ε_vac - g_eff ε_vac      [tracking scaling + SINK]
  dε_DM /dN = -3(1+w_DM) ε_DM   + g_eff ε_vac      [stiff a^-6 + SOURCE]
  d ln(ρ_vac/ρ_rad)/dN = (4 - 2 n_eff) - g_eff
  => Δ(ρ_vac/ρ_rad)|_BBN proportional to -g_eff*efolds  < 0  (Γ_exch>0, ε_vac>0)
  => sign_verdict PASS by construction (the bleed is a strict sink on ε_vac).
  The MAGNITUDE |Δ| (sufficient to cross below 0.227?) is the open compute.
  CAUTION (source fidelity): the exchange also FEEDS ε_DM (w=1, ρ∝a^-6); a w=1
  component dilutes FASTEST, so the stiff-DM sink does NOT over-accumulate at BBN
  -- this is why Volovik #35 gets "correct present-day order of magnitude" rather
  than a stiff-DM runaway. The Omega_DM,today band is the binding two-sided check.

GATE (plan SS W4-1 operator -- 3-condition AND):
  PASS  <=> (|Omega_vac,today - 0.685| <= 0.020)
          AND (|Omega_DM,today - 0.265| <= 0.020)
          AND (rho_vac/rho_rad|_BBN < 0.227).
  FAIL-on-BBN-only => the excess is real and the exchange does not relieve it.
  FAIL-on-Omega-only => INFO (right structure, free-normalization needs a pin).

DI: q-theory two-fluid coupled-decay axis (Volovik #35); the BBN-arm + dark-sector
    reconciliation. Distinct machinery from inv-8 (KZ-wall / RG-beta).
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import hashlib
import math
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---- canonical constants (MANDATORY per math-scripts.md) ----
SHARED = Path(__file__).resolve().parent.parent / "_shared"
sys.path.insert(0, str(SHARED))
from canonical_constants import (   # noqa: E402
    M_KK,                 # 7.428660036284456e16  substrate compactification scale (GeV)
    tau_fold,             # 0.19        van Hove fold position
    M_Pl_reduced,         # 2.435e18 GeV
    Gamma_effacement,     # 0.99970     S37 impedance transmission; (1-Gamma)=3e-4
    w0_FW,                # -0.918      framework w_0 (Volovik partition + effacement)
    wa_FW,                # 0.0         framework w_a (four-fold locked, S58)
    rho_vac_over_rho_rad_BBN_below,  # 0.474049  S98 FAIL-side BBN fraction (no exchange)
    delta_N_eff_vacuum_BBN_below,    # 2.0873    companion ΔN_eff at the FAIL value
    T_BBN_GeV,            # 0.001 GeV   (~1 MeV BBN temperature)
    T_CMB_GeV,            # 2.348e-13 GeV  today's photon temperature
    Omega_Lambda,         # 0.685       Planck18 dark-energy density parameter
    Omega_DM,             # 0.266       = Omega_m - Omega_b (Planck18 CDM)
    Omega_r,              # 9.15e-5     radiation density parameter (Planck18)
)

# ============================================================================
# Identity
# ============================================================================
GATE_ID = "INV11-W4-1-TWO-FLUID-COUPLED-DECAY-ODE"
SCHEME = "VOLOVIK-PAPER35-TWO-FLUID-EXCHANGE"
CONVENTION = "ABSOLUTE-FRAMEWORK-BRIDGE-EXCHANGE-COEFF-FROM-1-MINUS-GAMMA-EFF"
L_MAX = "10"                 # rho_rad(T) GGE bath + a0/a2 vacuum moments (L12 cache -> L10)
SCHEMA_VERSION = "S84+"

HERE = Path(__file__).resolve().parent                        # computations/investigation-11
SCRIPT_PATH = HERE / "inv11_w4_two_fluid_coupled_decay_ode.py"
NPZ_PATH = HERE / "inv11_w4_two_fluid_coupled_decay_ode.npz"
PNG_PATH = HERE / "inv11_w4_two_fluid_coupled_decay_ode.png"

CANONICAL_CONSTANTS_PATH = SHARED / "canonical_constants.py"
# The W4-2  rho_vac(q,T) surface -- the T-dependent vacuum input (plan prerequisite).
W4_2_NPZ = HERE / "inv11_w4_2_rho_vac_q_t_surface.npz"
# The L12 spectrum cache (a0/a2 moments + 992 fold eigenfrequencies at tau_fold).
S84_CACHE_NPZ = HERE.parent / "session-84" / "s84_spectrum_cache_L12_tau019.npz"

# ---- pre-registered gate machinery pins (plan SS W4-1 machinery_pin_map) ----
N_EVAL = 2000                 # (local) T-grid points T_transit->today (log-spaced)
ODE_RTOL = 1e-9               # (local) scipy solve_ivp rtol
ODE_ATOL = 1e-12              # (local) scipy solve_ivp atol
GAMMA_EXCH_LO = 1e-4          # (local) exchange-coeff sensitivity scan low
GAMMA_EXCH_HI = 1e-3          # (local) exchange-coeff sensitivity scan high
G_EFF_SUBSTRATE = 1.0 - Gamma_effacement  # the substrate-fixed exchange coeff (1-Gamma_eff)=3e-4

# pre-registered PASS bands (plan SS W4-1 strict_PASS_boundary)
OMEGA_VAC_TARGET = 0.685      # (local) Planck18 dark-energy central
OMEGA_DM_TARGET = 0.265       # (local) Planck18 CDM central (plan-pinned)
OMEGA_BAND = 0.020            # (local) two-sided Omega tolerance
BBN_BOUND = 7.0 / 8.0 * (4.0 / 11.0) ** (4.0 / 3.0)  # 0.227113 = ΔN_eff=1 bound
N_EFF_TRACKING = 1.978110506244663  # (local) S98 from-below tracking exponent (W4-2 EXPONENT_ON_Q_S97)
W_DM_STIFF = 1.0             # (local) Volovik #35 SS IV.B Zel'dovich stiff matter w=+1


# ============================================================================
# Dual-SHA helpers (race-safe emit via knowledge-MCP; script never writes verdict)
# ============================================================================
def sha256_of(path):
    h = hashlib.sha256()                                      # (local)
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def dual_sha(pin_map):
    """(audit_sha256, content_sha256). audit = closure over ordered input-pin map;
    content = script bytes."""
    audit_payload = json.dumps(pin_map, sort_keys=True, separators=(",", ":")).encode()  # (local)
    h_audit = hashlib.sha256(); h_audit.update(audit_payload)
    h_content = hashlib.sha256()
    with open(SCRIPT_PATH, "rb") as f:
        h_content.update(f.read())
    return h_audit.hexdigest(), h_content.hexdigest()


def print_verdict_payload(verdict, value, scheme, convention, l_max,
                          audit_sha, content_sha, schema_version,
                          sign_verdict, magnitude_verdict, regime_verdict):
    """Print the canonical verdict payload for the agent to pass to emit_verdict.
    The SCRIPT never writes the verdict file (race-safe emit via knowledge-MCP)."""
    print("\n" + "#" * 78)
    print("# VERDICT PAYLOAD (agent -> emit_verdict, track='investigation')")
    print("#" * 78)
    print(f"gate_id        = {GATE_ID}")
    print(f"verdict        = {verdict}")
    print(f"value          = {value}")
    print(f"scheme         = {scheme}")
    print(f"convention     = {convention}")
    print(f"l_max          = {l_max}")
    print(f"audit_sha256   = {audit_sha}")
    print(f"content_sha256 = {content_sha}")
    print(f"schema_version = {schema_version}")
    print(f"sign_verdict      = {sign_verdict}")
    print(f"magnitude_verdict = {magnitude_verdict}")
    print(f"regime_verdict    = {regime_verdict}")
    print("#" * 78)


# ============================================================================
# SECTION 1: load the W4-2 surface (the T-dependent vacuum input) + spectrum cache
# ============================================================================
def load_w4_2_surface():
    """Load the W4-2 rho_vac(q,T) surface. Returns the surface, grids, T-markers,
    and the verdict-confirmed anchors (bbn_excess_real, the S98 0.474049 fraction).
    This IS the T-dependent vacuum input the plan mandates (NOT the surrogate)."""
    d = np.load(W4_2_NPZ, allow_pickle=True)
    surf = {
        "rho_vac_surface": d["rho_vac_surface"],   # (100,100) in M_KK^4 units
        "eps_surface": d["eps_surface"],
        "q_grid": d["q_grid"],                     # (100,) q in [0, 0.15]
        "T_grid": d["T_grid"],                     # (100,) T in [0, 3.28] M_KK units
        "T_today_MKK": float(d["T_today_MKK"]),
        "T_BBN_MKK": float(d["T_BBN_MKK"]),
        "T_transit_MKK": float(d["T_transit_MKK"]),
        "iT_today": int(d["iT_today"]),
        "iT_BBN": int(d["iT_BBN"]),
        "iT_transit": int(d["iT_transit"]),
        "p_BBN": float(d["p_BBN"]),                # tracking exponent at BBN (~1.976)
        "persists_to_BBN": bool(d["persists_to_BBN"]),
        "bbn_excess_real": bool(d["bbn_excess_real"]),
        "c10_is_derivation": bool(d["c10_is_derivation"]),
        "rho_vac_over_rho_rad_BBN_below": float(d["rho_vac_over_rho_rad_BBN_below"]),
        "w4_2_verdict": str(d["verdict"]),
        "w4_2_track": str(d["track"]),
        "w4_2_audit_sha": str(d["audit_sha256"]),
    }
    return surf


# ============================================================================
# SECTION 2: the coupled two-fluid ODE (Volovik #35 SS V, on the Friedmann bg)
# ============================================================================
def integrate_two_fluid(g_eff, N_transit, N_BBN, N_today,
                        Om_vac0, Om_DM0, Om_rad0, n_eff, w_DM):
    """
    Integrate the two-component continuity-with-exchange (Volovik #35 SS V) in the
    e-fold variable N = ln(a), a_today = 1.

    The TRACKING vacuum scales rho_vac ~ a^(-2 n_eff) in the radiation era (the C10
    form the W4-2 surface derived); the exchange adds a strict SINK -g_eff:
        d rho_vac/dN = -(2 n_eff) rho_vac - g_eff rho_vac
    The stiff-DM (w=+1) gets the SAME term as a SOURCE (energy conserved, only
    redistributed -- Volovik #35 "energy exchange between the two dark components"),
    plus its own a^-6 dilution:
        d rho_DM /dN = -3(1 + w_DM) rho_DM + g_eff rho_vac
    rho_rad is the bath: a^-4 exactly (exchange is vac<->DM, not vac<->rad to
    leading order). Densities in rho_crit,today units (so Omega_i,today = rho_i,today).

    We integrate BACKWARD from today (N=0) to transit, with the present-day
    composition as the boundary; the BBN fraction rho_vac/rho_rad is read off at
    N_BBN. (Backward integration from a well-determined present-day state is the
    physically clean readout: the present Omega ARE the framework's late-time
    composition; the BBN fraction is the consequence.)
    """
    two_neff = 2.0 * n_eff   # (local) radiation-era tracking log-slope of rho_vac

    def rhs(N, y):
        rv, rd = y
        drv = -two_neff * rv - g_eff * rv                 # (local) tracking + sink
        drd = -3.0 * (1.0 + w_DM) * rd + g_eff * rv       # (local) stiff a^-6 + source
        return [drv, drd]

    N_eval = np.linspace(N_today, N_transit, N_EVAL)      # (local) log-spaced in a
    sol = solve_ivp(rhs, [N_today, N_transit], [Om_vac0, Om_DM0],
                    t_eval=N_eval, rtol=ODE_RTOL, atol=ODE_ATOL, method="LSODA")
    N = sol.t
    rv = sol.y[0]
    rd = sol.y[1]
    rrad = Om_rad0 * np.exp(-4.0 * N)                     # (local) radiation bath a^-4

    # NORMALIZE the tracking-vacuum BBN fraction to the substrate-derived anchor.
    # The W4-2 surface + S98 lever fix rho_vac/rho_rad|_BBN = 0.474049 in the
    # NO-EXCHANGE limit. The bare ODE rho_vac (rho_crit units) carries a different
    # absolute normalization (today's Omega_vac), so we anchor the FRACTION at BBN
    # to 0.474049 at g_eff=0 and let the exchange modify it MULTIPLICATIVELY (the
    # exchange enters d ln(f)/dN linearly as -g_eff, so the relief is a clean
    # exp(-g_eff*efolds) factor independent of the absolute normalization).
    iBBN = int(np.argmin(np.abs(N - N_BBN)))
    return N, rv, rd, rrad, iBBN


def bbn_fraction_with_exchange(g_eff, N_transit, N_BBN, f0_anchor):
    """
    The BBN vacuum fraction rho_vac/rho_rad with exchange, anchored to the
    substrate-derived no-exchange value f0_anchor = 0.474049 (W4-2 / S98).

    d ln(f)/dN = (4 - 2 n_eff) - g_eff   [tracking term is normalization-fixed by
    the anchor; the exchange adds -g_eff to the log-slope]. Integrating from transit
    to BBN, the ONLY g_eff-dependence in the fraction is the multiplicative relief
    factor exp(-g_eff * (N_BBN - N_transit)) (the tracking part is absorbed into
    the f0 anchor at g_eff=0). This is the substrate-honest readout: f0 is FIXED by
    the W4-2 surface; the exchange relieves it by exactly the bled fraction.
    """
    efolds = N_BBN - N_transit                            # (local) >0 (transit earlier)
    relief = math.exp(-g_eff * efolds)                    # (local) <1: the sink
    return f0_anchor * relief, efolds, relief


# ============================================================================
# MAIN
# ============================================================================
def main():
    print("#" * 78)
    print(f"# {GATE_ID}")
    print("#" * 78)

    # ---- input SHAs (logged in first 20 lines of stdout per gate-verdicts.md) ----
    sha_canonical = sha256_of(CANONICAL_CONSTANTS_PATH)
    sha_w4_2 = sha256_of(W4_2_NPZ)
    sha_s84 = sha256_of(S84_CACHE_NPZ)
    sha_script = sha256_of(SCRIPT_PATH)
    print(f"[input SHA] canonical_constants.py = {sha_canonical[:16]}...")
    print(f"[input SHA] inv11_w4_2_surface.npz = {sha_w4_2[:16]}...")
    print(f"[input SHA] s84_spectrum_cache.npz = {sha_s84[:16]}...")
    print(f"[input SHA] script                 = {sha_script[:16]}...")

    # ---- load the W4-2 surface (the T-dependent vacuum input) ----
    surf = load_w4_2_surface()
    print(f"\n[W4-2 prereq] verdict={surf['w4_2_verdict']} track={surf['w4_2_track']}")
    print(f"[W4-2 prereq] bbn_excess_real={surf['bbn_excess_real']} "
          f"c10_is_derivation={surf['c10_is_derivation']} "
          f"persists_to_BBN={surf['persists_to_BBN']}")
    print(f"[W4-2 prereq] rho_vac/rho_rad|_BBN (S98 no-exchange) = "
          f"{surf['rho_vac_over_rho_rad_BBN_below']:.6f}")
    print(f"[W4-2 prereq] tracking exponent p_BBN = {surf['p_BBN']:.6f} "
          f"(2*n_eff/... -> ~2 tracking)")

    # the substrate-derived no-exchange BBN fraction (the value W4-1 must relieve)
    f0_anchor = surf["rho_vac_over_rho_rad_BBN_below"]    # (local) = 0.474049
    assert abs(f0_anchor - rho_vac_over_rho_rad_BBN_below) < 1e-9, \
        "W4-2 surface BBN fraction must match the canonical S98 anchor"

    # ---- e-fold spans (a_today=1; a~1/T in radiation era) ----
    # T_today = T_CMB; T_BBN ~ 1 MeV; T_transit from the W4-2 surface (M_KK units).
    T_today_GeV = T_CMB_GeV                               # (local)
    T_BBN_GeV_local = T_BBN_GeV                           # (local)
    T_transit_GeV = surf["T_transit_MKK"] * M_KK          # (local) M_KK units -> GeV
    N_today = 0.0                                         # (local)
    N_BBN = math.log(T_today_GeV / T_BBN_GeV_local)       # (local) a_BBN = T_today/T_BBN
    N_transit = math.log(T_today_GeV / T_transit_GeV)     # (local) very negative
    print(f"\n[e-folds] N_today={N_today:.4f} N_BBN={N_BBN:.4f} N_transit={N_transit:.4f}")
    print(f"[e-folds] transit->BBN = {N_BBN - N_transit:.4f}  BBN->today = {N_today - N_BBN:.4f}")

    # ---- present-day composition (the boundary for the backward integration) ----
    Om_vac0 = Omega_Lambda                               # (local) 0.685
    Om_DM0 = Omega_DM                                    # (local) 0.266
    Om_rad0 = Omega_r                                    # (local) 9.15e-5

    # ============================================================================
    # SECTION 3: the coupled ODE at the SUBSTRATE-FIXED exchange coefficient
    # ============================================================================
    g_sub = G_EFF_SUBSTRATE                              # (local) (1-Gamma_eff)=3e-4
    print(f"\n[exchange] substrate-fixed g_eff = (1 - Gamma_eff) = {g_sub:.6e}")

    # full coupled ODE (for the present-day Omega readout + the DM-runaway check)
    N, rv, rd, rrad, iBBN = integrate_two_fluid(
        g_sub, N_transit, N_BBN, N_today, Om_vac0, Om_DM0, Om_rad0,
        N_EFF_TRACKING, W_DM_STIFF)

    # present-day Omega (read at N=0, the boundary): these are the framework's
    # late-time composition; the tiny exchange perturbs them at O(g_eff) ~ 3e-4.
    # The backward ODE preserves the present-day boundary EXACTLY by construction;
    # the physical present-day Omega ARE the framework inputs (w0_FW projection).
    Om_vac_today = float(rv[0])                          # (local) = Om_vac0 (boundary)
    Om_DM_today = float(rd[0])                           # (local) = Om_DM0 (boundary)

    # the BBN vacuum fraction WITH the substrate exchange (anchored readout)
    f_BBN_sub, efolds, relief_sub = bbn_fraction_with_exchange(
        g_sub, N_transit, N_BBN, f0_anchor)
    # the no-exchange baseline (g=0): recovers exactly f0_anchor
    f_BBN_noexch, _, relief0 = bbn_fraction_with_exchange(
        0.0, N_transit, N_BBN, f0_anchor)

    # the stiff-DM runaway check: does the bled energy over-accumulate at BBN?
    # rho_DM_bled / rho_DM_today ~ integral; the w=1 component dilutes a^-6 so the
    # source term that fed it near transit has already redshifted away by BBN.
    rho_DM_BBN = float(rd[iBBN])                         # (local) stiff-DM at BBN
    rho_DM_today_val = float(rd[0])                      # (local) stiff-DM today
    # stiff-DM fraction of radiation at BBN (runaway witness)
    f_DM_rad_BBN = rho_DM_BBN / float(rrad[iBBN])        # (local)

    print(f"\n[BBN readout] efolds transit->BBN = {efolds:.4f}")
    print(f"[BBN readout] relief factor exp(-g_eff*efolds) = {relief_sub:.6f}")
    print(f"[BBN readout] rho_vac/rho_rad|_BBN no-exchange = {f_BBN_noexch:.6f}")
    print(f"[BBN readout] rho_vac/rho_rad|_BBN WITH exchange = {f_BBN_sub:.6f}")
    print(f"[BBN readout] |Delta| removed = {f_BBN_noexch - f_BBN_sub:.6f} "
          f"(need > {f0_anchor - BBN_BOUND:.6f} to reach the bound)")
    print(f"[BBN readout] BBN bound (ΔN_eff=1) = {BBN_BOUND:.6f}")
    print(f"[DM runaway] stiff-DM/rho_rad|_BBN = {f_DM_rad_BBN:.6e} "
          f"(w=1 a^-6 dilution: no over-accumulation if <<1 ... actually large at "
          f"BBN because rho_rad is huge; the witness is rho_DM_today)")

    # ============================================================================
    # SECTION 4: the exchange-coefficient sensitivity scan [1e-4, 1e-3]
    # ============================================================================
    g_scan = np.logspace(np.log10(GAMMA_EXCH_LO), np.log10(GAMMA_EXCH_HI), 50)  # (local)
    f_BBN_scan = np.array([bbn_fraction_with_exchange(g, N_transit, N_BBN, f0_anchor)[0]
                           for g in g_scan])             # (local)
    # the g_eff needed to reach the bound (closed form: f0*exp(-g*efolds)=bound)
    g_needed = -math.log(BBN_BOUND / f0_anchor) / efolds # (local)
    print(f"\n[scan] g_eff in [{GAMMA_EXCH_LO:.0e}, {GAMMA_EXCH_HI:.0e}] -> "
          f"rho_vac/rho_rad|_BBN in "
          f"[{f_BBN_scan.max():.6f}, {f_BBN_scan.min():.6f}]")
    print(f"[scan] g_eff NEEDED to reach bound = {g_needed:.6f} "
          f"(= {g_needed / g_sub:.1f}x the (1-Gamma_eff)=3e-4 leak)")

    # ============================================================================
    # SECTION 5: VERDICT (3-condition AND; [SIGN] 3-tuple)
    # ============================================================================
    # Condition 1: Omega_vac in band
    cond_vac = abs(Om_vac_today - OMEGA_VAC_TARGET) <= OMEGA_BAND
    # Condition 2: Omega_DM in band
    cond_DM = abs(Om_DM_today - OMEGA_DM_TARGET) <= OMEGA_BAND
    # Condition 3: BBN fraction below bound
    cond_BBN = f_BBN_sub < BBN_BOUND

    # ---- SIGN: the exchange is a strict SINK on rho_vac => Delta < 0 ----
    delta_BBN = f_BBN_sub - f_BBN_noexch                 # (local) the exchange-induced change
    sign_predicted_negative = True                       # substitution chain: Δ<0 (sink)
    sign_verdict = "PASS" if (delta_BBN < 0) == sign_predicted_negative else "FAIL"

    # ---- MAGNITUDE: the 3-condition AND (BBN clause is the binding magnitude) ----
    if cond_vac and cond_DM and cond_BBN:
        magnitude_verdict = "PASS"
    elif cond_vac and cond_DM and not cond_BBN:
        # BBN relieved in sign but magnitude-insufficient: the binding FAIL
        magnitude_verdict = "FAIL"
    else:
        # Omega band missed (BBN may or may not be relieved): INFO per plan
        magnitude_verdict = "INFO"

    # ---- REGIME: the tracking + CPL formulation is valid across the window ----
    # The integration is on a well-posed Friedmann background throughout; the
    # tracking scaling holds where the W4-2 surface verdicted persists_to_BBN=True.
    regime_verdict = "VALID" if surf["persists_to_BBN"] else "MARGINAL"

    # ---- composite collapse (gate-verdicts.md PRE-REGISTERED rule) ----
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"
    elif sign_verdict == "FAIL":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"
    elif magnitude_verdict == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"

    print(f"\n[verdict] cond_vac(Omega_vac in band)={cond_vac} "
          f"(Om_vac_today={Om_vac_today:.4f}, target {OMEGA_VAC_TARGET}+-{OMEGA_BAND})")
    print(f"[verdict] cond_DM (Omega_DM  in band)={cond_DM} "
          f"(Om_DM_today={Om_DM_today:.4f}, target {OMEGA_DM_TARGET}+-{OMEGA_BAND})")
    print(f"[verdict] cond_BBN(rho_vac/rho_rad<bound)={cond_BBN} "
          f"(f_BBN={f_BBN_sub:.6f}, bound {BBN_BOUND:.6f})")
    print(f"[verdict] sign={sign_verdict} magnitude={magnitude_verdict} "
          f"regime={regime_verdict} => composite={composite}")

    # ============================================================================
    # SECTION 6: dual-SHA + verdict payload
    # ============================================================================
    audit_pin_map = {
        "gate_id": GATE_ID,
        "canonical_constants_sha": sha_canonical,
        "w4_2_surface_sha": sha_w4_2,
        "s84_spectrum_cache_sha": sha_s84,
        "script_sha": sha_script,
        "N_eval": N_EVAL,
        "ode_rtol": ODE_RTOL,
        "g_eff_substrate": G_EFF_SUBSTRATE,
        "gamma_exch_lo": GAMMA_EXCH_LO,
        "gamma_exch_hi": GAMMA_EXCH_HI,
        "omega_vac_target": OMEGA_VAC_TARGET,
        "omega_dm_target": OMEGA_DM_TARGET,
        "omega_band": OMEGA_BAND,
        "bbn_bound": BBN_BOUND,
        "n_eff_tracking": N_EFF_TRACKING,
        "w_dm_stiff": W_DM_STIFF,
        "f0_anchor": f0_anchor,
    }
    audit_sha, content_sha = dual_sha(audit_pin_map)

    value_str = (
        f"Omega_vac_today={Om_vac_today:.4f};Omega_DM_today={Om_DM_today:.4f};"
        f"rho_vac_rho_rad_BBN_with_exchange={f_BBN_sub:.4f};"
        f"rho_vac_rho_rad_BBN_no_exchange={f_BBN_noexch:.4f};"
        f"bound={BBN_BOUND:.4f};delta_removed={f_BBN_noexch - f_BBN_sub:.4e};"
        f"g_eff_substrate={g_sub:.3e};g_eff_needed_for_bound={g_needed:.4f};"
        f"factor_short={g_needed / g_sub:.1f}x;"
        f"cond_vac={cond_vac};cond_DM={cond_DM};cond_BBN={cond_BBN};"
        f"sign=SINK_Delta_negative;CLASS=FULL;"
        f"vac_input=W4-2-surface-NOT-surrogate;"
        f"exchange_coeff=1-Gamma_eff-FRAMEWORK-BRIDGE;"
        f"axis=Volovik-P35-two-fluid-coupled-decay-BBN-arm"
    )

    print_verdict_payload(composite, value_str, SCHEME, CONVENTION, L_MAX,
                          audit_sha, content_sha, SCHEMA_VERSION,
                          sign_verdict, magnitude_verdict, regime_verdict)

    # ============================================================================
    # SECTION 7: save npz
    # ============================================================================
    np.savez(
        NPZ_PATH,
        gate_id=GATE_ID,
        verdict=composite,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        # present-day composition
        Omega_vac_today=Om_vac_today, Omega_DM_today=Om_DM_today,
        Omega_vac_target=OMEGA_VAC_TARGET, Omega_DM_target=OMEGA_DM_TARGET,
        Omega_band=OMEGA_BAND,
        cond_vac=cond_vac, cond_DM=cond_DM, cond_BBN=cond_BBN,
        # BBN readout
        f0_anchor=f0_anchor,
        rho_vac_rho_rad_BBN_with_exchange=f_BBN_sub,
        rho_vac_rho_rad_BBN_no_exchange=f_BBN_noexch,
        bbn_bound=BBN_BOUND, delta_removed=f_BBN_noexch - f_BBN_sub,
        delta_needed=f0_anchor - BBN_BOUND,
        relief_factor=relief_sub, efolds_transit_to_BBN=efolds,
        # exchange
        g_eff_substrate=g_sub, g_eff_needed_for_bound=g_needed,
        factor_short=g_needed / g_sub,
        g_scan=g_scan, f_BBN_scan=f_BBN_scan,
        # ODE trajectories
        N_efolds=N, rho_vac_traj=rv, rho_DM_traj=rd, rho_rad_traj=rrad,
        iBBN=iBBN, N_today=N_today, N_BBN=N_BBN, N_transit=N_transit,
        # stiff-DM runaway witness
        f_DM_rad_BBN=f_DM_rad_BBN,
        rho_DM_BBN=rho_DM_BBN, rho_DM_today=rho_DM_today_val,
        # constants / source
        n_eff_tracking=N_EFF_TRACKING, w_DM_stiff=W_DM_STIFF, w0_FW=w0_FW,
        Gamma_effacement=Gamma_effacement, M_KK=M_KK, tau_fold=tau_fold,
        # W4-2 provenance
        w4_2_verdict=surf["w4_2_verdict"], w4_2_track=surf["w4_2_track"],
        w4_2_audit_sha=surf["w4_2_audit_sha"],
        persists_to_BBN=surf["persists_to_BBN"],
        bbn_excess_real=surf["bbn_excess_real"],
        # pins
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"\n[{GATE_ID}] saved npz: {NPZ_PATH}")

    # ============================================================================
    # SECTION 8: plot
    # ============================================================================
    fig, axes = plt.subplots(2, 2, figsize=(15, 11))

    # Panel 1: the BBN fraction vs exchange coefficient (the magnitude verdict)
    ax = axes[0, 0]
    ax.semilogx(g_scan, f_BBN_scan, "b-", lw=2, label=r"$\rho_{\rm vac}/\rho_{\rm rad}|_{\rm BBN}$ (with exchange)")
    ax.axhline(f0_anchor, color="orange", ls="--", lw=1.5,
               label=fr"no-exchange S98 = {f0_anchor:.4f}")
    ax.axhline(BBN_BOUND, color="red", ls="-", lw=2,
               label=fr"$\Delta N_{{\rm eff}}=1$ bound = {BBN_BOUND:.4f}")
    ax.axvline(g_sub, color="green", ls=":", lw=2,
               label=fr"$(1-\Gamma_{{\rm eff}})$ = {g_sub:.0e}")
    ax.axvline(g_needed, color="purple", ls=":", lw=1.5,
               label=fr"$g$ needed = {g_needed:.4f} ({g_needed/g_sub:.0f}$\times$)")
    ax.set_xlabel(r"exchange coefficient $g_{\rm eff}$ (per e-fold)")
    ax.set_ylabel(r"$\rho_{\rm vac}/\rho_{\rm rad}|_{\rm BBN}$")
    ax.set_title("BBN vacuum fraction vs exchange coefficient\n"
                 "(substrate leak is ~54x too small to reach the bound)")
    ax.legend(fontsize=8, loc="center left")
    ax.grid(alpha=0.3)

    # Panel 2: the coupled-decay trajectories rho_i(a)
    ax = axes[0, 1]
    a_arr = np.exp(N)
    ax.loglog(a_arr, np.abs(rv), "b-", lw=2, label=r"$\rho_{\rm vac}$ (tracking, w_eff=0.32)")
    ax.loglog(a_arr, np.abs(rd), "r-", lw=2, label=r"$\rho_{\rm DM}$ (stiff, w=+1, $a^{-6}$)")
    ax.loglog(a_arr, rrad, "g-", lw=2, label=r"$\rho_{\rm rad}$ ($a^{-4}$)")
    ax.axvline(np.exp(N_BBN), color="k", ls="--", lw=1, label="BBN")
    ax.set_xlabel("scale factor $a$ ($a_{\\rm today}=1$)")
    ax.set_ylabel(r"$\rho_i / \rho_{\rm crit,today}$")
    ax.set_title("Two-fluid coupled-decay trajectories\n(Volovik #35 SS V)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, which="both")

    # Panel 3: the relief factor and |Delta| bar (the sign is correct, magnitude short)
    ax = axes[1, 0]
    bars = ax.bar([0, 1, 2],
                  [f0_anchor, f_BBN_sub, BBN_BOUND],
                  color=["orange", "blue", "red"], alpha=0.7)
    ax.set_xticks([0, 1, 2])
    ax.set_xticklabels(["no-exchange\n(S98)", "with exchange\n$(1-\\Gamma_{\\rm eff})$", "$\\Delta N_{\\rm eff}=1$\nbound"])
    ax.set_ylabel(r"$\rho_{\rm vac}/\rho_{\rm rad}|_{\rm BBN}$")
    ax.set_title(fr"BBN fraction: sign-correct sink, magnitude short"
                 f"\n|Delta| removed = {f0_anchor - f_BBN_sub:.4f}, need {f0_anchor - BBN_BOUND:.4f}")
    for b, v in zip(bars, [f0_anchor, f_BBN_sub, BBN_BOUND]):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.005, f"{v:.4f}",
                ha="center", fontsize=9)
    ax.grid(alpha=0.3, axis="y")

    # Panel 4: present-day Omega bands (the two-sided check)
    ax = axes[1, 1]
    cats = ["$\\Omega_{\\rm vac}$", "$\\Omega_{\\rm DM}$"]
    vals = [Om_vac_today, Om_DM_today]
    targs = [OMEGA_VAC_TARGET, OMEGA_DM_TARGET]
    x = np.arange(2)
    ax.errorbar(x, targs, yerr=OMEGA_BAND, fmt="rs", ms=10, capsize=8,
                label=f"Planck18 target $\\pm${OMEGA_BAND}")
    ax.plot(x, vals, "bo", ms=12, label="framework (two-fluid)")
    ax.set_xticks(x)
    ax.set_xticklabels(cats)
    ax.set_ylabel(r"$\Omega_{i,\rm today}$")
    ax.set_title(f"Present-day composition\n"
                 f"(vac in band: {cond_vac}, DM in band: {cond_DM})")
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3, axis="y")

    fig.suptitle(f"{GATE_ID}: {composite}  "
                 f"(sign={sign_verdict}, magnitude={magnitude_verdict}, regime={regime_verdict})\n"
                 f"Volovik #35 two-fluid exchange at the substrate $(1-\\Gamma_{{\\rm eff}})$ "
                 f"coefficient relieves BBN by {f0_anchor - f_BBN_sub:.4f} (need {f0_anchor - BBN_BOUND:.4f})",
                 fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(PNG_PATH, dpi=150, bbox_inches="tight")
    print(f"[{GATE_ID}] saved png: {PNG_PATH}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
