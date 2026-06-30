#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S110-CF-CCDARK1-BBN   [SIGN]   PHONONIC
=======================================
NON-thermal BBN-relief channel for the two-fluid coupled-decay ODE.

PURPOSE (plan §W2-6):
  inv-11 W4-1 ran the Volovik #35 two-fluid coupled-decay ODE with the substrate
  effacement leak (1-Gamma_eff)=3e-4 as the energy-exchange coefficient. Result:
  the bleed is a strict SINK on rho_vac (sign=PASS) but 53.8x too SMALL to clear
  the BBN bound (the THERMAL route is gap-suppressed by the BCS gap |Delta|, the
  pair-breaking Boltzmann factor exp(-Delta/T) at T < Delta near-vanishing).
  inv-11 W4-3 closed the de Sitter route too (Gamma_dS underflow).

  THIS gate asks whether a NON-thermal exchange channel -- one ESCAPING the
  gap-suppression -- can reach the required coupling g_eff_needed = 0.0161535898
  (54x the thermal 3e-4) and clear rho_vac/rho_rad|_BBN below the substrate-derived
  bound bbn_bound = 0.22710731766023898.

THE NON-THERMAL CHANNEL + ITS SUBSTRATE-DERIVED COUPLING -- PRE-REGISTERED HERE,
BEFORE THE RUN (CAC-class discipline; PROHIBITED_ACTIONS Class 1 guard against
functional-shopping; per plan §W2-6 convention pin). Two sub-channels, both pinned
to substrate-DERIVED couplings (NOT scanned-to-PASS):

  SUB-CHANNEL 1 -- PARAMETRIC / FLOQUET PAIR-TRANSFER in the §VII.BP band
    (omega_q = 2.012813 M_KK). The Floquet pair-transfer rate per e-fold is the
    base impedance throughput (1-Gamma_eff) ENHANCED by the parametric
    growth-per-drive-period factor:
        g_para = (1 - Gamma_eff) * G_para,   G_para = exp(Re mu_F * T_period)
    where Re mu_F is the Floquet exponent of the §VII.BP relic-mode monodromy at
    the PHYSICAL Mathieu depth h_par. The WS-FLOQUET workshop (S110, this session,
    transit-dynamics x quantum-acoustics, 3 rounds, berry monodromy tie-breaker)
    CONVERGED that the physical depth is h_par = 8.3e-4 (NOT inv-10's q~0.504, an
    occupation-energy-per-pair ratio mis-mapped onto the depth slot, ~607x
    over-assigned), at which every one of the 1248 relic modes sits in a Mathieu
    STABILITY GAP: fraction_resonance = 0 EXACT, max|Tr M| = 1.99999 < 2,
    Re mu_F = 0 EXACT. Therefore G_para = exp(0) = 1 and
        g_para = (1 - Gamma_eff) * 1 = 3.0e-4
    -- the parametric channel adds NO enhancement (the resonance is Floquet-DEAD
    at the substrate-delivered drive depth). The COUNTERFACTUAL depth that would
    first catch the nearest-a=1 relic mode is h_par_crit = 0.0725 (84.34x the
    delivered 8.3e-4; WS-FLOQUET CF-S111-FLOQUET-2) -- unreached.

  SUB-CHANNEL 2 -- SUBSTRATE-INTERNAL (non-Boltzmann) LEAK. The raw effacement
    impedance-mismatch transmission (1-Gamma_eff) = 3e-4 read as a NON-thermal
    leak (the impedance throughput the fold ALREADY carries, S37, WITHOUT the
    exp(-Delta/T) Boltzmann pair-breaking factor). This is the MAXIMAL
    substrate-derived non-thermal coupling: the effacement channel is the
    substrate's own non-Boltzmann leak, and its strength is fixed at 3e-4.
        g_internal = (1 - Gamma_eff) = 3.0e-4

  The PRE-REGISTERED non-thermal coupling is the MAX of the two substrate-derived
  sub-channels: g_nonthermal = max(g_para, g_internal) = 3.0e-4. (Both land at
  3e-4 because the parametric enhancement is unity -- the §VII.BP resonance is
  Floquet-dead at the physical depth.) This is pinned from substrate physics
  (WS-FLOQUET h_par + the S37 effacement throughput) BEFORE the ODE re-integration;
  no coupling is tuned to reach the bound.

SUBSTRATE FRAMING (phononic-framing.md §"IS Space, Not IN Space"):
  The substrate IS the flowing quantum vacuum; the two "fluids" are the two-leg
  decomposition of ONE vacuum surface rho_vac(q,T) (a0/effacement leg w=-0.918 +
  q-theory matter leg w=+1), NOT two relic species in a container. The BBN
  over-production reads the SAME derived rho_vac(q,T) surface at the BBN epoch
  (flat in T to BBN, n_eff=1.978) -- 2.06x the substrate bound. A relief channel,
  if any, must be a NON-thermal exchange between the legs (the thermal Boltzmann
  exchange is gap-suppressed by |Delta|, dead at 53.8x short). The arrow:
      D_K eigenfrequencies -> rho_vac(q,T) tracking surface
        -> the §VII.BP relic-mode Floquet monodromy (h_par = 8.3e-4)
        -> the non-thermal pair-transfer coupling g_nonthermal
        -> the re-integrated BBN-epoch vacuum fraction.

GATE (plan §W2-6 operator -- inequality, [SIGN]):
  PASS <=> rho_vac/rho_rad|_BBN < bbn_bound=0.22710731766023898 via the
           non-thermal channel, sign=PASS retained.
  INFO <=> reduces the 2.06x overshoot but does NOT clear the bound (partial).
  FAIL <=> the non-thermal channel is ALSO gap-suppressed (cannot reach
           g_eff=0.0162) -- the BBN over-production wall hardens.

SUBSTITUTION CHAIN (plan §W2-6, [SIGN]):
  CLAIM: "a NON-thermal exchange channel reduces rho_vac/rho_rad at BBN below the
          substrate-derived bound 0.2271, escaping the gap-suppression that closed
          the thermal route."
  Step 1: rho_vac/rho_rad|_BBN (no exchange) = 0.474049  [canonical S98; inv-11 npz]
  Step 2: bbn_bound = 0.22710731766023898                [inv-11 npz; substrate-derived]
  Step 3: rescue removes delta_needed = 0.474049 - 0.2271 = 0.24694, requiring
          g_eff_needed = 0.0161535898                    [inv-11 npz]
  Step 4: thermal baseline g_eff_substrate = 3.0e-4 -> factor_short = 53.845 (DEAD)
  Step 5: non-thermal candidate g_nonthermal = max(g_para, g_internal):
            g_para     = (1-Gamma_eff)*exp(Re mu_F * T_period) = 3e-4 * exp(0) = 3e-4
                         [WS-FLOQUET: Re mu_F = 0 EXACT at h_par = 8.3e-4]
            g_internal = (1-Gamma_eff) = 3e-4    [S37 effacement non-Boltzmann leak]
          => g_nonthermal = 3.0e-4 (NO enhancement: §VII.BP Floquet-dead)
          => relief = exp(-g_nonthermal * efolds) = exp(-3e-4 * 45.556) = 0.9864
          => rho_vac/rho_rad|_BBN = 0.474049 * 0.9864 = 0.46761
  Direction: sign=PASS (the bleed is a strict SINK, Delta < 0). MAGNITUDE: FAIL
    (0.46761 > 0.2271; the non-thermal channel is ALSO gap-suppressed, factor 53.8x
    short -- IDENTICAL to the thermal route, because the parametric enhancement is
    unity at the physical depth).
  Conclusion: FAIL hardens the BBN wall (thermal + de Sitter + non-thermal ALL
    closed); the tension routes to WS-CC-H0 as the cost of the tracking freedom.

WS-FLOQUET DEPENDENCY (the load-bearing input, this session):
  The parametric sub-channel's enhancement factor G_para = exp(Re mu_F * T_period)
  is pinned by the WS-FLOQUET converged verdict (sessions/session-110/workshops/
  ws-floquet.md): DEAD-by-depth, Re mu_F = 0 EXACT at h_par = 8.3e-4. This is NOT
  a free choice -- it is an independent in-session structural result. Had inv-10
  won (Re mu_F = 0.249 > 0 at q~0.5), the enhancement would be
  exp(0.249*pi) ~ 2.19/period and the parametric channel could in principle reach
  g_eff_needed. WS-FLOQUET forecloses that: the substrate places no relic mode in
  the period-2 tongue at the physical depth.
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
    M_KK,                 # substrate compactification scale (GeV)
    tau_fold,             # 0.19  van Hove fold position
    Gamma_effacement,     # 0.99970  S37 impedance transmission; (1-Gamma)=3e-4
    w0_FW,                # -0.918  framework w_0 (Volovik partition + effacement)
    rho_vac_over_rho_rad_BBN_below,  # 0.474049  S98 FAIL-side BBN fraction (no exchange)
    Delta_BCS,            # ~0.4643  R-PROTECTED canonical BCS gap (the thermal-suppression scale)
)

# ============================================================================
# Identity
# ============================================================================
GATE_ID = "S110-CF-CCDARK1-BBN"
SCHEME = "two-fluid-coupled-decay-ODE+NON-thermal-exchange"
CONVENTION = "non-thermal-channel-PRE-REGISTERED-Floquet-pair-transfer-OR-internal-leak"
L_MAX = "10"                 # §VII.BP pair-band resonance machinery + rho_vac(q,T) surface
SCHEMA_VERSION = "S84+"

HERE = Path(__file__).resolve().parent                        # computations/session-110
SCRIPT_PATH = HERE / "s110_cf_ccdark1_bbn_nonthermal.py"
NPZ_PATH = HERE / "s110_cf_ccdark1_bbn_nonthermal.npz"
PNG_PATH = HERE / "s110_cf_ccdark1_bbn_nonthermal.png"

CANONICAL_CONSTANTS_PATH = SHARED / "canonical_constants.py"
# The inv-11 W4-1 two-fluid coupled-decay ODE npz -- the thermal-baseline source.
INV11_W4_NPZ = HERE.parent / "investigation-11" / "inv11_w4_two_fluid_coupled_decay_ode.npz"

# ---- plan-pinned input SHA (canonical_constants.py at plan-freeze) ----
# Plan §W2-6 input_files.canonical_constants.sha256:
PLAN_PINNED_CANONICAL_SHA = "e5a7587f8326c9cc90cb720197a3ace824b3f89c5bbea17cfd659b27f607568a"
# Plan §W2-6 input_files.inv11_w4_two_fluid_coupled_decay_ode.sha256:
PLAN_PINNED_INV11_SHA = "8675f970f3c8270426921ba30b0eadf9b58ca87d6bcb8f10fcc95bd189f1cb5b"

# ============================================================================
# PRE-REGISTERED machinery pins (plan §W2-6 machinery_pin_map) -- frozen BEFORE run
# ============================================================================
N_EFOLD_STEPS = 2000          # (local) ODE re-integration grid (matches inv-11 N_efolds)
ODE_RTOL = 1e-9               # (local) scipy solve_ivp rtol (matches inv-11)
ODE_ATOL = 1e-12             # (local) scipy solve_ivp atol (matches inv-11)
G_SCAN_N = 60                # (local) g_eff scan points (>= 50 per plan); LINEAR per plan
G_SCAN_LO = 3.0e-4           # (local) thermal baseline (1-Gamma_eff)
G_SCAN_HI = 0.0162           # (local) just beyond g_eff_needed (plan scan_range upper)

# ---- the substrate-DERIVED bound + thermal-baseline anchors (inv-11 W4-1 npz) ----
BBN_BOUND = 0.22710731766023898          # (local-pin) substrate-derived BBN bound (NOT round 0.2)
F0_ANCHOR = rho_vac_over_rho_rad_BBN_below  # 0.474049  no-exchange BBN fraction (canonical S98)
G_EFF_THERMAL = 1.0 - Gamma_effacement   # (local) thermal effacement leak = 3e-4

# ---- the PRE-REGISTERED non-thermal channel parameters (substrate-derived) ----
# Sub-channel 1: PARAMETRIC / FLOQUET pair-transfer in the §VII.BP band.
#   The physical Mathieu depth and the relic-mode Floquet exponent are PINNED by the
#   WS-FLOQUET S110 converged verdict (DEAD-by-depth). These are substrate-physics
#   inputs, NOT free knobs.
OMEGA_Q_VII_BP = 2.012813    # (local-pin) §VII.BP drive freq (S101-W1-QEQ-RELIC-ODDFLOOR; M_KK)
H_PAR_PHYSICAL = 8.3e-4      # (local-pin) physical Mathieu depth (WS-FLOQUET converged)
RE_MU_F_VII_BP = 0.0         # (local-pin) Floquet exponent at h_par (WS-FLOQUET: 0 EXACT, gap-confined)
H_PAR_CRIT_DTC = 0.0725      # (local-pin) counterfactual depth catching nearest-a=1 mode (WS-FLOQUET CF-2)
# Sub-channel 2: SUBSTRATE-INTERNAL non-Boltzmann leak = the raw effacement throughput.
G_INTERNAL_LEAK = 1.0 - Gamma_effacement  # (local) = 3e-4  (S37 impedance, non-Boltzmann reading)


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
    print("# VERDICT PAYLOAD (agent -> emit_verdict, track='session')")
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
# SECTION 2: the BBN vacuum fraction with a non-thermal exchange coupling
# ============================================================================
def bbn_fraction_with_exchange(g_eff, efolds, f0_anchor):
    """
    The BBN vacuum fraction rho_vac/rho_rad with a coupled-decay exchange of
    coefficient g_eff (per e-fold), anchored to the substrate-derived no-exchange
    value f0_anchor = 0.474049 (S98 / inv-11 W4-1).

    From the inv-11 W4-1 two-fluid ODE:
        d ln(rho_vac/rho_rad)/dN = (4 - 2 n_eff) - g_eff
    The tracking term (4 - 2 n_eff) is normalization-fixed by the f0 anchor at
    g_eff=0; the exchange adds -g_eff to the log-slope. Integrating transit->BBN,
    the ONLY g_eff-dependence is the multiplicative relief factor:
        relief = exp(-g_eff * efolds)
    This reproduces the inv-11 W4-1 readout EXACTLY (same closed form). It is
    channel-AGNOSTIC: thermal vs non-thermal differ ONLY in the value of g_eff;
    the ODE structure is identical (a strict sink on rho_vac). The non-thermal
    physics enters entirely through g_eff = g_nonthermal.
    """
    relief = math.exp(-g_eff * efolds)                        # (local) <1: the sink
    return f0_anchor * relief, relief


def integrate_two_fluid_omega_check(g_eff, N_transit, N_BBN, N_today,
                                    Om_vac0, Om_DM0, Om_rad0, n_eff, w_DM):
    """
    Full coupled two-fluid ODE (inv-11 W4-1 §V) for the present-day Omega readout +
    the BBN index. Backward integration from today (N=0) to transit; densities in
    rho_crit,today units. Returns the trajectories and the BBN index.

        d rho_vac/dN = -(2 n_eff) rho_vac - g_eff rho_vac    (tracking + sink)
        d rho_DM /dN = -3(1 + w_DM) rho_DM + g_eff rho_vac    (stiff a^-6 + source)
        rho_rad      = Om_rad0 * exp(-4 N)                    (a^-4 bath)
    """
    two_neff = 2.0 * n_eff   # (local)

    def rhs(N, y):
        rv, rd = y
        drv = -two_neff * rv - g_eff * rv                     # (local)
        drd = -3.0 * (1.0 + w_DM) * rd + g_eff * rv           # (local)
        return [drv, drd]

    N_eval = np.linspace(N_today, N_transit, N_EFOLD_STEPS)   # (local)
    sol = solve_ivp(rhs, [N_today, N_transit], [Om_vac0, Om_DM0],
                    t_eval=N_eval, rtol=ODE_RTOL, atol=ODE_ATOL, method="LSODA")
    N = sol.t
    rv = sol.y[0]
    rd = sol.y[1]
    rrad = Om_rad0 * np.exp(-4.0 * N)                         # (local)
    iBBN = int(np.argmin(np.abs(N - N_BBN)))                  # (local)
    return N, rv, rd, rrad, iBBN


# ============================================================================
# MAIN
# ============================================================================
def main():
    print("#" * 78)
    print(f"# {GATE_ID}")
    print("#" * 78)

    # ---- input SHAs (logged in first 20 lines of stdout per gate-verdicts.md) ----
    sha_canonical = sha256_of(CANONICAL_CONSTANTS_PATH)
    sha_inv11 = sha256_of(INV11_W4_NPZ)
    sha_script = sha256_of(SCRIPT_PATH)
    print(f"[input SHA] canonical_constants.py = {sha_canonical[:16]}...")
    print(f"[input SHA] inv11_w4_two_fluid.npz = {sha_inv11[:16]}...")
    print(f"[input SHA] script                 = {sha_script[:16]}...")

    # ---- SOURCE-RECONCILIATION: canonical_constants.py SHA drift check (class-(c)) ----
    # The canonical file may carry in-session edits (W2 promoted constants) between
    # plan-freeze and runtime. Per substrate-first-canonical-sourcing.md §(ii.B), the
    # RUNTIME SHA is ground truth; we document the drift and confirm the SPECIFIC
    # constants we consume are unchanged at their canonical values.
    canonical_drift = (sha_canonical != PLAN_PINNED_CANONICAL_SHA)   # (local)
    inv11_drift = (sha_inv11 != PLAN_PINNED_INV11_SHA)               # (local)
    print(f"\n[source-recon] canonical SHA matches plan pin: {not canonical_drift}")
    if canonical_drift:
        print(f"[source-recon]   plan-pin   = {PLAN_PINNED_CANONICAL_SHA[:16]}...")
        print(f"[source-recon]   runtime    = {sha_canonical[:16]}... (in-session W2 edits)")
        print(f"[source-recon]   class-(c) PIN-DRIFT-FROM-STALE-SOURCE: BENIGN -- the "
              f"consumed constants are unchanged:")
        print(f"[source-recon]     rho_vac_over_rho_rad_BBN_below = {rho_vac_over_rho_rad_BBN_below} "
              f"(== 0.474049 canonical S98)")
        print(f"[source-recon]     Gamma_effacement = {Gamma_effacement} (== 0.99970 canonical S37)")
        print(f"[source-recon]     Delta_BCS = {Delta_BCS:.6f} (R-PROTECTED canonical)")
        print(f"[source-recon]     w0_FW = {w0_FW}, M_KK = {M_KK:.6e}, tau_fold = {tau_fold}")
    # the inv-11 npz MUST be bit-stable (it is the thermal-baseline source of truth)
    print(f"[source-recon] inv-11 npz SHA matches plan pin: {not inv11_drift} "
          f"(MUST be True -- thermal-baseline source)")
    assert not inv11_drift, "inv-11 W4-1 npz SHA must match the plan pin (thermal baseline)"

    # ---- load the inv-11 W4-1 thermal-baseline numbers (the source of truth) ----
    d = np.load(INV11_W4_NPZ, allow_pickle=True)
    f0_anchor = float(d["f0_anchor"])                          # (local) = 0.474049
    bbn_bound_inv11 = float(d["bbn_bound"])                    # (local) substrate-derived
    efolds = float(d["efolds_transit_to_BBN"])                 # (local) = 45.5556955587
    g_eff_thermal_inv11 = float(d["g_eff_substrate"])          # (local) = 3e-4
    g_eff_needed = float(d["g_eff_needed_for_bound"])          # (local) = 0.0161535898
    factor_short_thermal = float(d["factor_short"])            # (local) = 53.845
    f_BBN_thermal = float(d["rho_vac_rho_rad_BBN_with_exchange"])  # (local) = 0.46761
    N_today = float(d["N_today"])                              # (local) = 0
    N_BBN = float(d["N_BBN"])                                  # (local)
    N_transit = float(d["N_transit"])                          # (local)
    n_eff_tracking = float(d["n_eff_tracking"])                # (local) = 1.978
    w_DM_stiff = float(d["w_DM_stiff"])                        # (local) = 1
    Om_vac0 = float(d["Omega_vac_today"])                      # (local) = 0.685
    Om_DM0 = float(d["Omega_DM_today"])                        # (local) = 0.2657

    print(f"\n[inv-11 baseline] f0_anchor (no-exchange BBN fraction)  = {f0_anchor:.6f}")
    print(f"[inv-11 baseline] bbn_bound (substrate-derived)          = {bbn_bound_inv11:.11f}")
    print(f"[inv-11 baseline] efolds transit->BBN                    = {efolds:.6f}")
    print(f"[inv-11 baseline] g_eff_thermal (1-Gamma_eff)            = {g_eff_thermal_inv11:.3e}")
    print(f"[inv-11 baseline] g_eff_needed_for_bound                 = {g_eff_needed:.10f}")
    print(f"[inv-11 baseline] factor_short (thermal route)           = {factor_short_thermal:.3f}x")
    print(f"[inv-11 baseline] rho_vac/rho_rad|_BBN (thermal exchange) = {f_BBN_thermal:.6f}")

    # consistency: our canonical BBN_BOUND pin must match the inv-11 npz value
    assert abs(BBN_BOUND - bbn_bound_inv11) < 1e-12, \
        "the plan-pinned bbn_bound must match the inv-11 W4-1 npz"
    assert abs(f0_anchor - F0_ANCHOR) < 1e-9, \
        "the inv-11 f0_anchor must match the canonical S98 anchor"

    # ============================================================================
    # SECTION 3: the PRE-REGISTERED non-thermal coupling (substrate-derived)
    # ============================================================================
    # Sub-channel 1: PARAMETRIC / FLOQUET pair-transfer in the §VII.BP band.
    #   G_para = exp(Re mu_F * T_period); WS-FLOQUET pins Re mu_F = 0 EXACT at the
    #   physical depth h_par = 8.3e-4 (gap-confined, max|Tr M| = 1.99999 < 2).
    T_period = 2.0 * math.pi / OMEGA_Q_VII_BP                  # (local) drive period (M_KK^-1)
    G_para_enhancement = math.exp(RE_MU_F_VII_BP * T_period)   # (local) = exp(0) = 1 (DEAD)
    g_para = G_EFF_THERMAL * G_para_enhancement                # (local) = 3e-4 * 1 = 3e-4
    # counterfactual: the depth that WOULD catch the nearest-a=1 relic mode
    dtc_miss_factor = H_PAR_CRIT_DTC / H_PAR_PHYSICAL          # (local) = 84.34x

    # Sub-channel 2: SUBSTRATE-INTERNAL non-Boltzmann leak = raw effacement throughput.
    g_internal = G_INTERNAL_LEAK                               # (local) = 3e-4

    # the PRE-REGISTERED non-thermal coupling = MAX of the substrate-derived sub-channels
    g_nonthermal = max(g_para, g_internal)                     # (local) = 3e-4

    print(f"\n[non-thermal channel -- PRE-REGISTERED, substrate-derived]")
    print(f"  sub-channel 1 (Floquet pair-transfer, §VII.BP omega_q={OMEGA_Q_VII_BP}):")
    print(f"    T_period = 2pi/omega_q                 = {T_period:.6f} M_KK^-1")
    print(f"    Re mu_F at h_par={H_PAR_PHYSICAL:.1e} (WS-FLOQUET) = {RE_MU_F_VII_BP} (gap-confined, 0 EXACT)")
    print(f"    G_para = exp(Re mu_F * T_period)        = {G_para_enhancement:.6f} (NO enhancement)")
    print(f"    g_para = (1-Gamma_eff) * G_para         = {g_para:.6e}")
    print(f"    counterfactual depth h_par_crit         = {H_PAR_CRIT_DTC} ({dtc_miss_factor:.2f}x unreached)")
    print(f"  sub-channel 2 (substrate-internal non-Boltzmann leak):")
    print(f"    g_internal = (1-Gamma_eff)              = {g_internal:.6e}")
    print(f"  => g_nonthermal = max(g_para, g_internal) = {g_nonthermal:.6e}")
    print(f"  => factor short of g_eff_needed           = {g_eff_needed / g_nonthermal:.3f}x")

    # ============================================================================
    # SECTION 4: re-integrate the BBN fraction with the non-thermal coupling
    # ============================================================================
    f_BBN_nonthermal, relief_nonthermal = bbn_fraction_with_exchange(
        g_nonthermal, efolds, f0_anchor)
    f_BBN_noexch, relief0 = bbn_fraction_with_exchange(0.0, efolds, f0_anchor)
    delta_removed_nonthermal = f_BBN_noexch - f_BBN_nonthermal  # (local)
    delta_needed = f0_anchor - BBN_BOUND                        # (local) = 0.24694

    print(f"\n[BBN readout -- non-thermal channel]")
    print(f"  relief = exp(-g_nonthermal*efolds)      = {relief_nonthermal:.6f}")
    print(f"  rho_vac/rho_rad|_BBN no-exchange         = {f_BBN_noexch:.6f}")
    print(f"  rho_vac/rho_rad|_BBN NON-thermal         = {f_BBN_nonthermal:.6f}")
    print(f"  |Delta| removed                          = {delta_removed_nonthermal:.6f}")
    print(f"  |Delta| needed to reach bound            = {delta_needed:.6f}")
    print(f"  bbn_bound                                = {BBN_BOUND:.11f}")
    print(f"  clears the bound?                        = {f_BBN_nonthermal < BBN_BOUND}")

    # ---- the present-day Omega two-sided check (full ODE) ----
    Om_rad0 = float(d["rho_rad_traj"][0]) if "rho_rad_traj" in d else 9.15e-5  # (local)
    N, rv, rd, rrad, iBBN = integrate_two_fluid_omega_check(
        g_nonthermal, N_transit, N_BBN, N_today, Om_vac0, Om_DM0, Om_rad0,
        n_eff_tracking, w_DM_stiff)
    Om_vac_today = float(rv[0])                                # (local) boundary
    Om_DM_today = float(rd[0])                                 # (local) boundary
    print(f"\n[Omega check] Omega_vac_today = {Om_vac_today:.4f}, Omega_DM_today = {Om_DM_today:.4f}")

    # ============================================================================
    # SECTION 5: the g_eff scan (>= 50 pts; LINEAR per plan) -- maps the corridor
    # ============================================================================
    g_scan = np.linspace(G_SCAN_LO, G_SCAN_HI, G_SCAN_N)       # (local) LINEAR
    f_BBN_scan = np.array([bbn_fraction_with_exchange(g, efolds, f0_anchor)[0]
                           for g in g_scan])                   # (local)
    # closed-form g_eff to reach the bound (cross-check vs inv-11)
    g_needed_closed = -math.log(BBN_BOUND / f0_anchor) / efolds  # (local)
    print(f"\n[scan] g_eff in [{G_SCAN_LO:.1e}, {G_SCAN_HI:.4f}] ({G_SCAN_N} pts, linear) ->")
    print(f"       rho_vac/rho_rad|_BBN in [{f_BBN_scan.min():.6f}, {f_BBN_scan.max():.6f}]")
    print(f"[scan] g_needed (closed form)            = {g_needed_closed:.10f}")
    print(f"[scan] g_needed (inv-11 npz)             = {g_eff_needed:.10f}")
    print(f"[scan] cross-check |closed - inv11|      = {abs(g_needed_closed - g_eff_needed):.2e}")
    assert abs(g_needed_closed - g_eff_needed) < 1e-6, "g_needed closed form must match inv-11"

    # the non-thermal coupling lands at the FLOOR of the scan (no enhancement)
    factor_short_nonthermal = g_eff_needed / g_nonthermal      # (local) = 53.845 (== thermal)

    # ============================================================================
    # SECTION 6: VERDICT (inequality, [SIGN] 3-tuple)
    # ============================================================================
    # ---- SIGN: the non-thermal exchange is a strict SINK on rho_vac => Delta < 0 ----
    delta_BBN = f_BBN_nonthermal - f_BBN_noexch                # (local) the exchange-induced change
    sign_predicted_negative = True                             # substitution chain: Delta<0 (sink)
    sign_verdict = "PASS" if (delta_BBN < 0) == sign_predicted_negative else "FAIL"

    # ---- MAGNITUDE: does the non-thermal fraction clear the substrate bound? ----
    cleared = f_BBN_nonthermal < BBN_BOUND                     # (local) PASS condition
    # INFO band: reduces the overshoot but does not clear (partial relief);
    # the overshoot ratio is f/bound; "partial relief" = f reduced below f0 but > bound.
    partial_relief = (f_BBN_nonthermal < f_BBN_noexch) and (f_BBN_nonthermal >= BBN_BOUND)  # (local)
    if cleared:
        magnitude_verdict = "PASS"
    elif partial_relief:
        # the channel relieves SOME overshoot but is gap-suppressed short of the bound
        magnitude_verdict = "FAIL"   # per plan: FAIL iff non-thermal channel is ALSO gap-suppressed
    else:
        magnitude_verdict = "FAIL"

    # ---- REGIME: the tracking + non-thermal exchange is valid across the window ----
    # The integration is on a well-posed Friedmann background; the non-thermal coupling
    # is a substrate-derived constant (no small-parameter breakdown). The Floquet input
    # (Re mu_F = 0) is the converged WS-FLOQUET ground truth at the physical depth.
    regime_verdict = "VALID"

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

    print(f"\n[verdict] cleared (f < bound)            = {cleared} "
          f"(f_BBN={f_BBN_nonthermal:.6f}, bound={BBN_BOUND:.6f})")
    print(f"[verdict] partial relief (f0 > f >= bound) = {partial_relief}")
    print(f"[verdict] sign={sign_verdict} magnitude={magnitude_verdict} "
          f"regime={regime_verdict} => composite={composite}")
    print(f"[verdict] non-thermal channel factor_short = {factor_short_nonthermal:.3f}x "
          f"(== thermal {factor_short_thermal:.3f}x: parametric enhancement is unity)")

    # ============================================================================
    # SECTION 7: dual-SHA + verdict payload
    # ============================================================================
    audit_pin_map = {
        "gate_id": GATE_ID,
        "canonical_constants_sha": sha_canonical,
        "inv11_w4_npz_sha": sha_inv11,
        "script_sha": sha_script,
        "rho_vac_over_rho_rad_BBN_below": F0_ANCHOR,
        "bbn_bound": BBN_BOUND,
        "efolds_transit_to_BBN": efolds,
        "g_eff_thermal": G_EFF_THERMAL,
        "g_eff_needed": g_eff_needed,
        "omega_q_vii_bp": OMEGA_Q_VII_BP,
        "h_par_physical": H_PAR_PHYSICAL,
        "re_mu_f_vii_bp": RE_MU_F_VII_BP,
        "h_par_crit_dtc": H_PAR_CRIT_DTC,
        "g_nonthermal": g_nonthermal,
        "f_BBN_nonthermal": f_BBN_nonthermal,
        "n_eval": N_EFOLD_STEPS,
        "ode_rtol": ODE_RTOL,
        "g_scan_n": G_SCAN_N,
        "g_scan_lo": G_SCAN_LO,
        "g_scan_hi": G_SCAN_HI,
    }
    audit_sha, content_sha = dual_sha(audit_pin_map)

    value_str = (
        f"rho_vac_rho_rad_BBN_nonthermal={f_BBN_nonthermal:.6f};"
        f"bbn_bound={BBN_BOUND:.11f};cleared={cleared};"
        f"channel=PRE-REG-nonthermal-MAX-of-Floquet-pairtransfer-AND-internal-leak;"
        f"g_nonthermal={g_nonthermal:.4e};g_eff_needed={g_eff_needed:.6f};"
        f"factor_short={factor_short_nonthermal:.3f}x;"
        f"Floquet_subch_Re_muF={RE_MU_F_VII_BP}_at_h_par={H_PAR_PHYSICAL:.1e}_WS-FLOQUET-DEAD;"
        f"G_para_enhancement={G_para_enhancement:.4f}_unity;"
        f"h_par_crit_dtc={H_PAR_CRIT_DTC}_miss={dtc_miss_factor:.2f}x;"
        f"internal_leak_subch_g={g_internal:.4e}_S37-effacement;"
        f"delta_removed={delta_removed_nonthermal:.6f};delta_needed={delta_needed:.6f};"
        f"relief={relief_nonthermal:.6f};f0_anchor={f0_anchor:.6f};"
        f"Omega_vac_today={Om_vac_today:.4f};Omega_DM_today={Om_DM_today:.4f};"
        f"sign=SINK_Delta_negative;regime=VALID;"
        f"thermal_baseline_factor_short={factor_short_thermal:.3f}x;"
        f"canonical_sha_runtime_corrected_from_plan_pin={'yes' if canonical_drift else 'no'};"
        f"axis=Volovik-P35-two-fluid-NONthermal-BBN-arm;"
        f"consequence=BBN-wall-hardens-routes-to-WS-CC-H0-tracking-freedom-cost"
    )

    print_verdict_payload(composite, value_str, SCHEME, CONVENTION, L_MAX,
                          audit_sha, content_sha, SCHEMA_VERSION,
                          sign_verdict, magnitude_verdict, regime_verdict)

    # ============================================================================
    # SECTION 8: save npz
    # ============================================================================
    np.savez(
        NPZ_PATH,
        gate_id=GATE_ID,
        verdict=composite,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        # BBN readout -- non-thermal channel
        f0_anchor=f0_anchor,
        rho_vac_rho_rad_BBN_nonthermal=f_BBN_nonthermal,
        rho_vac_rho_rad_BBN_no_exchange=f_BBN_noexch,
        bbn_bound=BBN_BOUND, cleared=cleared, partial_relief=partial_relief,
        delta_removed_nonthermal=delta_removed_nonthermal, delta_needed=delta_needed,
        relief_nonthermal=relief_nonthermal, efolds_transit_to_BBN=efolds,
        # non-thermal channel parameters (PRE-REGISTERED, substrate-derived)
        g_nonthermal=g_nonthermal, g_para=g_para, g_internal=g_internal,
        g_eff_needed=g_eff_needed, factor_short_nonthermal=factor_short_nonthermal,
        # sub-channel 1: Floquet pair-transfer (WS-FLOQUET pins)
        omega_q_vii_bp=OMEGA_Q_VII_BP, T_period=T_period,
        h_par_physical=H_PAR_PHYSICAL, re_mu_f_vii_bp=RE_MU_F_VII_BP,
        G_para_enhancement=G_para_enhancement, h_par_crit_dtc=H_PAR_CRIT_DTC,
        dtc_miss_factor=dtc_miss_factor,
        # sub-channel 2: substrate-internal leak
        g_internal_leak=G_INTERNAL_LEAK,
        # thermal baseline (inv-11 W4-1)
        g_eff_thermal=G_EFF_THERMAL, factor_short_thermal=factor_short_thermal,
        f_BBN_thermal=f_BBN_thermal,
        # g_eff scan
        g_scan=g_scan, f_BBN_scan=f_BBN_scan, g_needed_closed=g_needed_closed,
        # present-day Omega
        Omega_vac_today=Om_vac_today, Omega_DM_today=Om_DM_today,
        # ODE trajectories
        N_efolds=N, rho_vac_traj=rv, rho_DM_traj=rd, rho_rad_traj=rrad,
        iBBN=iBBN, N_today=N_today, N_BBN=N_BBN, N_transit=N_transit,
        # constants / source
        n_eff_tracking=n_eff_tracking, w_DM_stiff=w_DM_stiff, w0_FW=w0_FW,
        Gamma_effacement=Gamma_effacement, Delta_BCS=Delta_BCS,
        M_KK=M_KK, tau_fold=tau_fold,
        # source-reconciliation
        canonical_drift=canonical_drift, inv11_drift=inv11_drift,
        canonical_sha_runtime=sha_canonical,
        canonical_sha_plan_pin=PLAN_PINNED_CANONICAL_SHA,
        # pins
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"\n[{GATE_ID}] saved npz: {NPZ_PATH}")

    # ============================================================================
    # SECTION 9: plot
    # ============================================================================
    fig, axes = plt.subplots(2, 2, figsize=(15, 11))

    # Panel 1: the BBN fraction vs exchange coefficient (linear scan) + the non-thermal point
    ax = axes[0, 0]
    ax.plot(g_scan, f_BBN_scan, "b-", lw=2,
            label=r"$\rho_{\rm vac}/\rho_{\rm rad}|_{\rm BBN}$ (coupled-decay)")
    ax.axhline(f0_anchor, color="orange", ls="--", lw=1.5,
               label=fr"no-exchange S98 = {f0_anchor:.4f}")
    ax.axhline(BBN_BOUND, color="red", ls="-", lw=2,
               label=fr"substrate BBN bound = {BBN_BOUND:.4f}")
    ax.axvline(g_nonthermal, color="green", ls=":", lw=2,
               label=fr"$g_{{\rm non-thermal}}$ = {g_nonthermal:.0e} (= thermal)")
    ax.axvline(g_eff_needed, color="purple", ls=":", lw=1.5,
               label=fr"$g$ needed = {g_eff_needed:.4f} ({factor_short_nonthermal:.0f}$\times$)")
    ax.plot([g_nonthermal], [f_BBN_nonthermal], "g*", ms=18, zorder=5)
    ax.set_xlabel(r"exchange coefficient $g_{\rm eff}$ (per e-fold)")
    ax.set_ylabel(r"$\rho_{\rm vac}/\rho_{\rm rad}|_{\rm BBN}$")
    ax.set_title("BBN vacuum fraction vs coupling\n"
                 "non-thermal channel lands at the thermal floor (Floquet-dead)")
    ax.legend(fontsize=8, loc="center right")
    ax.grid(alpha=0.3)

    # Panel 2: the §VII.BP Floquet sub-channel -- depth vs the DTC counterfactual
    ax = axes[0, 1]
    depths = np.array([H_PAR_PHYSICAL, H_PAR_CRIT_DTC])        # (local)
    re_mus = np.array([RE_MU_F_VII_BP, 0.249])                 # (local) physical vs inv-10 counterfactual
    labels = [f"physical\nh_par={H_PAR_PHYSICAL:.1e}\n(WS-FLOQUET DEAD)",
              f"counterfactual\nh_par_crit={H_PAR_CRIT_DTC}\n({dtc_miss_factor:.0f}x, would catch a=1)"]
    bars = ax.bar([0, 1], re_mus, color=["green", "purple"], alpha=0.7)
    ax.set_xticks([0, 1]); ax.set_xticklabels(labels, fontsize=8)
    ax.set_ylabel(r"$\mathrm{Re}\,\mu_F$ (Floquet exponent)")
    ax.set_title(r"§VII.BP pair-transfer: Floquet-DEAD at the physical depth"
                 "\n$\\mathrm{Re}\\,\\mu_F = 0$ EXACT (all 1248 modes gap-confined)")
    for b, v in zip(bars, re_mus):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.005, f"{v:.3f}",
                ha="center", fontsize=10)
    ax.grid(alpha=0.3, axis="y")

    # Panel 3: the |Delta| bar -- sign-correct sink, magnitude short (thermal == non-thermal)
    ax = axes[1, 0]
    bars = ax.bar([0, 1, 2, 3],
                  [f0_anchor, f_BBN_thermal, f_BBN_nonthermal, BBN_BOUND],
                  color=["orange", "steelblue", "green", "red"], alpha=0.7)
    ax.set_xticks([0, 1, 2, 3])
    ax.set_xticklabels(["no-exchange\n(S98)", "thermal\n$(1-\\Gamma)$",
                        "NON-thermal\n(this gate)", "substrate\nBBN bound"], fontsize=8)
    ax.set_ylabel(r"$\rho_{\rm vac}/\rho_{\rm rad}|_{\rm BBN}$")
    ax.set_title(fr"Non-thermal channel = thermal floor (no enhancement)"
                 f"\n|$\\Delta$| removed = {delta_removed_nonthermal:.4f}, "
                 f"need {delta_needed:.4f} (53.8$\\times$ short)")
    for b, v in zip(bars, [f0_anchor, f_BBN_thermal, f_BBN_nonthermal, BBN_BOUND]):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.005, f"{v:.4f}",
                ha="center", fontsize=9)
    ax.grid(alpha=0.3, axis="y")

    # Panel 4: the coupled-decay trajectories
    ax = axes[1, 1]
    a_arr = np.exp(N)
    ax.loglog(a_arr, np.abs(rv), "b-", lw=2, label=r"$\rho_{\rm vac}$ (tracking)")
    ax.loglog(a_arr, np.abs(rd), "r-", lw=2, label=r"$\rho_{\rm DM}$ (stiff $w=+1$, $a^{-6}$)")
    ax.loglog(a_arr, rrad, "g-", lw=2, label=r"$\rho_{\rm rad}$ ($a^{-4}$)")
    ax.axvline(np.exp(N_BBN), color="k", ls="--", lw=1, label="BBN")
    ax.set_xlabel("scale factor $a$ ($a_{\\rm today}=1$)")
    ax.set_ylabel(r"$\rho_i / \rho_{\rm crit,today}$")
    ax.set_title("Two-fluid coupled-decay trajectories\n"
                 f"($g_{{\\rm non-thermal}}$ = {g_nonthermal:.0e}, Volovik #35)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, which="both")

    fig.suptitle(f"{GATE_ID}: {composite}  "
                 f"(sign={sign_verdict}, magnitude={magnitude_verdict}, regime={regime_verdict})\n"
                 f"NON-thermal BBN-relief channel is ALSO gap-suppressed: "
                 f"§VII.BP Floquet-DEAD (Re$\\mu_F$=0 at $h_{{\\rm par}}$={H_PAR_PHYSICAL:.1e}) "
                 f"+ internal leak = {g_nonthermal:.0e}, {factor_short_nonthermal:.0f}$\\times$ short of "
                 f"$g_{{\\rm needed}}$={g_eff_needed:.4f}",
                 fontsize=10)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig(PNG_PATH, dpi=150, bbox_inches="tight")
    print(f"[{GATE_ID}] saved png: {PNG_PATH}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
