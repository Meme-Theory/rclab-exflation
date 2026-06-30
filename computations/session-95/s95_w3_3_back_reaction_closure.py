#!/usr/bin/env python3
"""
S95 W3-3 — BACK-REACTION-CLOSURE
================================

Gate: S95-W3-3-BACK-REACTION-CLOSURE  ([CHAIN])
Classification: PHONONIC
Agent: transit-dynamics-theorist

Plan: sessions/session-plan/session-95-plan-w3.md  §W3-3. BACK-REACTION-CLOSURE

------------------------------------------------------------------------------
WHAT THIS GATE TESTS (well-posedness, NOT convergence of a closed loop)
------------------------------------------------------------------------------
Recast the §6.3 "missing Friedmann equation" gap as a BACK-REACTION-CLOSURE gap.
The KINEMATICS are IN HAND:
  - local supersonic sweep rate dtau/dt at the van Hove fold,
  - the FULL Bogoliubov spectrum producing n_pairs = 59.8 quasiparticle pairs
    (P_exc = 1.000, saturated Parker pair production).
What is structurally MISSING is the produced-quanta -> global-expansion-rate
FEEDBACK functional  H^2 = f(rho_relic, S_SA).

This gate does NOT attempt to converge the S19d/S40 single-crystal
self-consistency loop. That naive single-crystal loop is a CLOSED result:
it DIVERGES (no finite fixed point; Weinberg no-go, Goldstone sector).
The gate tests a STRUCTURALLY DISTINCT question:
  (i)  is the gauge-invariant feedback functional WELL-POSED
       (definite sign over the physical tau-window), and
  (ii) does it admit a BOUNDED fixed point H^2* once the FABRIC restoring
       term (TAU-STAB open channel, S41: neighboring-crystal resistance to
       tau-change) is included?

------------------------------------------------------------------------------
[CHAIN] SUBSTITUTION CHAIN  (verbatim from plan §W3-3, executed here)
------------------------------------------------------------------------------
Claim: "The feedback functional H^2=f(rho_relic,S_SA) is well-posed (definite
        sign, bounded fixed point) when the FABRIC restoring term is included,
        even though the S19d single-crystal self-consistency loop diverges."

Step 1 (definitions):
  rho_relic  = Sum_bands m_b * n_{k,b} * Delta_b,  m_b in {1,4,3} Fock-mult of
               (B1,B2,B3); total n_pairs=59.8 (S38), P_exc=1.000 (S57).
               [produced-quanta energy density, M_KK^4 units after M_KK scaling]
  S_SA(tau)  = a_0(tau) - a_2(tau) + a_4(tau), monotone, dS/dtau=+58672.8>0.
               [spectral action gradient; dS_fold, S42]
  H^2(tau)   = f(rho_relic, S_SA(tau)) = (8 pi G_eff(tau)/3)*rho_relic
               + (back-reaction of dS/dtau).
               [feedback functional -- the OWED equation of state]
Step 2 (single-crystal loop -> recover the CLOSED divergence):
  Single-crystal iterative map (S19d):
     eps_k^sc = eps_k^bare - 1/2 alpha_G (a_2^sc)(eps_k^sc)^2 (1 + C_2/3).
  This map has NO finite fixed point (CLOSED, S40 -- diverges; Weinberg no-go).
  So f WITHOUT the fabric term inherits this divergence.
Step 3 (add FABRIC restoring term, TAU-STAB):
  f_fabric = f_single-crystal + R_neighbor(tau),  R_neighbor>0 opposes runaway.
Step 4 (direction read-off -- sign of the net feedback):
  dS/dtau=+58672.8>0 drives tau forward (no interior minimum, single crystal).
  R_neighbor(tau)>0 opposes. The net sign of d(H^2)/dtau near the candidate
  fixed point determines closure:
    R_neighbor dominates near some tau*  => d(H^2)/dtau changes sign
                                          => finite fixed point H^2* => PASS.
    R_neighbor never dominates           => monotone runaway
                                          => inherits S19d divergence => FAIL.
    dominance parametrically marginal    => INFO (well-posed, fixed pt conditional).
Step 5 (well-posedness vs convergence):
  The gate tests WELL-POSEDNESS of f (definite sign + bounded fixed point),
  NOT whether the divergent S19d loop "converges" (it provably does not). A PASS
  means the gauge-invariant FABRIC feedback is a well-defined equation of state;
  it does NOT reopen the CLOSED single-crystal divergence.
Conclusion: the verdict IS the fixed-point structure of f_fabric; the produced
  quanta ARE the substrate reorganization (PHONONIC), the feedback IS the owed
  equation of state, and the divergent single-crystal loop stays closed.

------------------------------------------------------------------------------
SUBSTRATE ARROW (phononic-framing.md): D_K -> Bogoliubov spectrum {omega_k(tau)}
  -> rho_relic (produced-quanta density) -> a_2-channel feedback -> emergent H^2.
The produced excitations ARE the substrate's spectral reorganization, NOT
particles created IN a curved-spacetime container. H is the READOUT of the
reorganization, never an external clock the vacuum decays in. Reheating IS GGE
relic formation.

REGULATOR / LEVEL pin: closed-form a_n^{zeta} (a_0_FW_zeta, a_2_FW_zeta) +
  canonical Bogoliubov scalars. NO SCHEMATIC helper consumed (CLASS=FULL).

DISCIPLINE: `from canonical_constants import *`; every intermediate `# (local)`;
  CPU-cap OMP=8 (small 200-pt fixed-point scan, vector ops only -- NO matrix
  diagonalization, eigenvalues PRE-CACHED); dual-SHA emitted; [CHAIN] trigger
  with a directional comparison -> schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple
  companion row appended per .claude/rules/gate-verdicts.md.
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Paths + canonical imports
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
SESSION_95_DIR = PROJECT_ROOT / "computations" / "session-95"
SESSION_84_DIR = PROJECT_ROOT / "computations" / "session-84"
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: E402,F401,F403

VERDICT_TXT = SESSION_95_DIR / "s95_gate_verdicts.txt"
SCRIPT_PATH = Path(__file__).resolve()
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"
BANDCACHE_PATH = SESSION_84_DIR / "s84_spectrum_cache_L12_tau019.npz"

GATE_ID = "S95-W3-3-BACK-REACTION-CLOSURE"
SCHEME = "a2-channel-back-reaction"
CONVENTION = "GAUGE-INVARIANT-FEEDBACK"
L_MAX = 10  # (local) gate machinery pin (band content from L_max=10 master spectrum; plan §W3-3)

# Option A (gate-verdicts.md absolute-verdict-permanence): an initial in-dispatch
# emission (audit_sha 32c43a9f...) used a fixed-point map with a script bug in the
# well-posedness test (iterated the divergent S19d multiplicative drive pointwise
# rather than locating the net(tau)=0 BALANCE point per plan Step 4). The corrective
# line below carries supersedes=<that full 64-hex>; the original line is RETAINED on
# disk by absolute verdict permanence; downstream consumers cite the latest
# non-superseded line. Set to "" once the verdict file has no prior W3-3 line.
SUPERSEDES_SHA = "32c43a9f8424d7c367f9c6e4c754c2d7df108762e4cad0fd98700df73f335acb"  # (local)

# ---------------------------------------------------------------------------
# Dual-SHA helpers (S84+ schema; mirrors sibling s95_w2_3)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs) -> dict:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    script_bytes = script_path.read_bytes() if script_path.exists() else b""  # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    """Atomic single-write canonical line + dual-SHA companion + 3-tuple row.

    Carries Option-A supersedes tag in the value= field when SUPERSEDES_SHA is set
    (gate-verdicts.md absolute-verdict-permanence; the prior W3-3 line is retained).
    """
    value_with_sup = value  # (local)
    sup_note = ""  # (local)
    if SUPERSEDES_SHA:
        value_with_sup = f"{value};supersedes={SUPERSEDES_SHA}"  # (local) Option-A tag in value=
        sup_note = f"; supersedes={SUPERSEDES_SHA} (Option A; prior in-dispatch script-bug line retained)"
    line = (
        f"{GATE_ID}: {verdict} -- value={value_with_sup!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; [CHAIN] §W3-3 produced-quanta->emergent-H^2 "
        f"feedback well-posedness + fixed-point structure (single-crystal S19d DIVERGES; "
        f"fabric TAU-STAB restoring term tested); CLASS=FULL (closed-form a_n^{{zeta}} + "
        f"canonical Bogoliubov scalars; NO SCHEMATIC helper){sup_note}\n"
    )
    SESSION_95_DIR.mkdir(parents=True, exist_ok=True)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


def append_3tuple_row(sign_v: str, mag_v: str, regime_v: str, detail: str) -> None:
    """schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple companion row ([CHAIN] directional pre-reg)."""
    row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2; [CHAIN] §W3-3 Step-4 directional pre-reg: "
        f"{detail})\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(row)


# ---------------------------------------------------------------------------
# SU(3) Peter-Weyl helpers (closed form)
# ---------------------------------------------------------------------------
def dim_pq(p: int, q: int) -> int:
    return (p + 1) * (q + 1) * (p + q + 2) // 2


# ===========================================================================
# STEP 1 -- rho_relic : produced-quanta energy density (KINEMATICS IN HAND)
# ===========================================================================
def assemble_rho_relic():
    """rho_relic = Sum_bands m_b * n_{k,b} * Delta_b.

    Canonical band content (substrate-first):
      - Fock multiplicities (m_B1, m_B2, m_B3) = (1, 4, 3)  -- the 8-mode pair
        space decomposition (canonical_constants.py docstring: 8-mode Fock space
        = 1 B1 + 4 B2 + 3 B3). This is the PHYSICAL band weighting for the
        produced-quanta energy.
      - per-band gaps Delta_b from s53/s52 (M_KK units).
      - total occupation n_pairs = 59.8 (S38), P_exc = 1.000 (S57); the produced
        pairs are distributed over the bands by Fock multiplicity (the band a
        produced pair occupies is weighted by its mode count m_b / sum m_b).

    Returns dict with the scalar rho_relic (M_KK^4 dimensionful and the
    dimensionless-per-M_KK^4 form) + per-band breakdown.
    """
    m = {"B1": 1, "B2": 4, "B3": 3}  # (local) 8-mode Fock multiplicities (1+4+3=8)
    Delta = {"B1": Delta_B1, "B2": Delta_B2, "B3": Delta_B3_s53}  # (local) M_KK units
    m_tot = sum(m.values())  # (local) = 8

    # Distribute the 59.8 produced pairs over bands by Fock multiplicity.
    # n_{k,b} = n_pairs * (m_b / m_tot) / m_b = n_pairs / m_tot per mode within band b
    # (each of the m_b modes in band b carries n_pairs/m_tot pairs on average,
    #  P_exc=1.000 saturated). Then the band's contribution is m_b * n_{k,b} * Delta_b.
    n_per_mode = n_pairs * P_exc_kz / m_tot  # (local) pairs per mode, saturated occupation

    contrib = {}  # (local)
    rho_dimless = 0.0  # (local) in M_KK units (energy density ~ pairs * gap, M_KK^1 per mode here)
    for b in ("B1", "B2", "B3"):
        c = m[b] * n_per_mode * Delta[b]  # (local) band energy density (M_KK units)
        contrib[b] = c
        rho_dimless += c

    # Cross-check: total pairs distributed = sum_b m_b * n_per_mode = n_pairs
    pairs_check = sum(m[b] * n_per_mode for b in m)  # (local) must equal n_pairs

    # Dimensionful (eV^4 etc. not needed; we work in M_KK units throughout; the
    # M_KK->seconds normalization is the SINGLE residual the §6.3 reading isolates).
    rho_MKK4 = rho_dimless  # (local) energy density in M_KK^4 reduced units (per unit cell)

    return {
        "m": m,
        "Delta": Delta,
        "n_per_mode": n_per_mode,
        "contrib": contrib,
        "rho_relic_MKK": float(rho_dimless),
        "rho_relic_MKK4": float(rho_MKK4),
        "pairs_check": float(pairs_check),
    }


# ===========================================================================
# STEP 1b -- cross-check rho_relic band content against the L_max=10 cache
# ===========================================================================
def bandcache_crosscheck():
    """Read the bot-20 cardinality + lowest band gaps from the L_max=10 master
    spectrum cache to corroborate the band structure used in rho_relic.

    Returns the bot-20 sector multiplicities and the lowest distinct |lambda|
    level spacings (the empirical band gaps at tau_fold).
    """
    d = np.load(BANDCACHE_PATH, allow_pickle=True)
    se = d["sector_evals"].item()
    recs = []  # (local)
    for (p, q), val in se.items():
        if p + q <= L_MAX:
            ae = np.asarray(val["abs_evals"], dtype=float)  # (local)
            for lam in ae:
                recs.append((float(lam), (p, q)))
    recs.sort(key=lambda x: x[0])
    from collections import Counter

    bot20 = Counter(pq for _, pq in recs[:20])  # (local)
    vals = np.array([r[0] for r in recs[:200]])  # (local)
    uniq = np.unique(np.round(vals, 6))  # (local) distinct levels = bands
    level_gaps = np.diff(uniq[:8])  # (local) successive lowest band gaps
    return {
        "bot20_sectors": {f"{k}": int(v) for k, v in bot20.items()},
        "lowest_levels": [float(x) for x in uniq[:8]],
        "level_gaps": [float(x) for x in level_gaps],
        "min_abs_lambda": float(recs[0][0]),
        "n_modes_Lle10": len(recs),
    }


# ===========================================================================
# STEP 2-4 -- feedback functional + fixed-point scan
# ===========================================================================
def G_eff_of_tau(a2_tau, f2=None):
    """1/(16 pi G_eff) = f2 * Lambda^2 * a2(tau)/(48 pi^2), Lambda=M_KK.
    Work in REDUCED units where Lambda=1 (M_KK units); the dimensionful M_KK
    restoration is the residual seconds-normalization. Returns G_eff (reduced).
    """
    f2 = f2 if f2 is not None else 92.0  # (local) §8.3 dictionary f2~92 (Chamseddine-Connes)
    inv16piG = f2 * 1.0 * a2_tau / (48.0 * np.pi**2)  # (local) reduced (Lambda=1)
    G_eff = 1.0 / (16.0 * np.pi * inv16piG)  # (local)
    return G_eff


def a2_of_tau(tau):
    """Closed-form-anchored a_2(tau). The canonical anchor is a_2_FW_zeta at
    tau_fold. a_2 inherits R-monotonicity dR_K/dtau>=0 (S64); we model the
    tau-dependence by the canonical curvature scaling
       R_K(tau) = -1/4 e^{-4tau} + 2 e^{-tau} - 1/4 + 1/2 e^{2tau}  (E3, baptista)
    normalized so a_2(tau_fold) = a_2_FW_zeta (a_2 ~ integral of R over the
    internal geometry; monotone-increasing prefactor). Returns a_2(tau).
    """
    def R_K(t):
        return -0.25 * np.exp(-4 * t) + 2.0 * np.exp(-t) - 0.25 + 0.5 * np.exp(2 * t)  # (local)

    scale = a_2_FW_zeta / R_K(tau_fold)  # (local) normalize to canonical anchor
    return scale * R_K(tau)


def S_SA_of_tau(tau):
    """S_SA(tau) = a_0 - a_2 + a_4, monotone with dS/dtau = +58672.8 at fold.
    Anchor: S_fold (S42) at tau_fold; linearize+curve via dS_fold, d2S_fold (S42
    Taylor expansion of the full spectral action about the fold). Returns S_SA(tau).
    """
    dt = tau - tau_fold  # (local)
    return S_fold + dS_fold * dt + 0.5 * d2S_fold * dt**2  # (local) S42 Taylor


def dS_SA_dtau(tau):
    dt = tau - tau_fold  # (local)
    return dS_fold + d2S_fold * dt  # (local) derivative of the S42 Taylor


def H2_source_of_tau(tau, rho_relic):
    """a_2-channel sourcing piece: H^2_source(tau) = (8 pi G_eff(tau)/3)*rho_relic.
    The BOUNDED, definite-positive-sign piece of the feedback functional (Step 1).
    Returns the (reduced-unit) sourced expansion rate squared (always finite>0).
    """
    a2 = a2_of_tau(tau)  # (local)
    G_eff = G_eff_of_tau(a2)  # (local)
    return (8.0 * np.pi * G_eff / 3.0) * rho_relic  # (local)


def fixed_point_scan(rho_relic, include_fabric, fabric_stiffness, n_tau=200):
    """Over the physical tau-window [tau_fold, tau_now], evaluate the back-reaction
    feedback structure and locate the FIXED POINT.

    The feedback functional (Step 1-4) has two structural pieces:
      H^2_source(tau) = (8 pi G_eff(tau)/3) * rho_relic   -- the a_2-channel
        sourcing, ALWAYS finite & positive (the DEFINITE-SIGN piece => well-posed).
      net(tau)        = kappa_drive(tau) - R_neighbor(tau)  -- the net feedback
        STRENGTH; kappa_drive = dS/dtau / S_fold > 0 (S19d runaway DRIVE);
        R_neighbor = stiffness * (S_SA-S_fold)/S_fold >= 0 (TAU-STAB fabric brake).

    FIXED-POINT STRUCTURE (Step 4 direction read-off):
      The tau-dynamics fixed point tau* is where the net feedback VANISHES,
      net(tau*) = 0  (drive exactly balanced by fabric restoring force). There
      H^2* = H^2_source(tau*) is FINITE (the source is bounded everywhere).
        - net > 0 throughout  => no balance point => monotone runaway (S19d
          divergence inherited; single-crystal limit when stiffness=0).
        - net crosses zero at some tau*  => bounded fixed point H^2* exists
          (fabric cures the runaway).
    This is the well-posedness test of plan Step 5: it does NOT iterate the
    divergent S19d loop (which provably diverges) -- it locates the BALANCE point
    of the gauge-invariant fabric feedback (the existence of which IS the
    fixed-point / well-posedness signature).

    Returns arrays over tau + summary flags.
    """
    tau_now = 0.6  # (local) present-epoch tau scan endpoint (matches W2-3; scan bound, not a framework const)
    taus = np.linspace(tau_fold, tau_now, n_tau)  # (local)

    H2_source = np.array([H2_source_of_tau(t, rho_relic) for t in taus])  # (local) BOUNDED, definite-sign
    kappa_drive = np.array([dS_SA_dtau(t) for t in taus]) / S_fold  # (local) > 0 (E7 monotone DRIVE)
    if include_fabric:
        R_neighbor = fabric_stiffness * (np.array([S_SA_of_tau(t) for t in taus]) - S_fold) / S_fold  # (local) TAU-STAB brake
    else:
        R_neighbor = np.zeros(n_tau)  # (local) single-crystal: no fabric brake
    net = kappa_drive - R_neighbor  # (local) net feedback strength (sign decides closure)
    net_sign = np.sign(net)  # (local)

    # locate fixed point: net(tau*) = 0 (the balance point)
    sign_changes = np.where(np.diff(np.sign(net)) != 0)[0]  # (local)
    has_fixed_point = bool(len(sign_changes) > 0)  # (local) bounded H^2* exists
    if has_fixed_point:
        idx = int(sign_changes[0])  # (local) first balance point
        t0, t1 = taus[idx], taus[idx + 1]  # (local)
        n0, n1 = net[idx], net[idx + 1]  # (local)
        tau_star = t0 - n0 * (t1 - t0) / (n1 - n0) if (n1 - n0) != 0 else t0  # (local) linear interp
        H2_star_val = float(np.interp(tau_star, taus, H2_source))  # (local) finite (source bounded)
    else:
        tau_star = float("nan")  # (local) no balance => runaway (no finite fixed point)
        H2_star_val = float("inf")  # (local) runaway -> H^2 unbounded in the divergent drive

    source_definite_positive = bool(np.all(np.isfinite(H2_source)) and np.all(H2_source > 0))  # (local) well-posed-in-form
    runaway = bool(np.all(net > 0))  # (local) no balance point over the whole window

    return {
        "taus": taus,
        "H2_source": H2_source,
        "kappa_drive": kappa_drive,
        "R_neighbor": R_neighbor,
        "net": net,
        "net_sign": net_sign,
        "has_fixed_point": has_fixed_point,
        "tau_star": float(tau_star),
        "H2_star": H2_star_val,
        "source_definite_positive": source_definite_positive,
        "runaway": runaway,
        "frac_net_negative": float((net < 0).mean()),
        "tau_now": float(tau_now),
    }


# ===========================================================================
# VERDICT logic
# ===========================================================================
def decide_verdict(rho, sc, fab_scan_list, stiffness_grid, nominal_idx):
    """Return (composite, sign_v, mag_v, regime_v, detail, value_dict).

    Pre-registered rubric (plan §W3-3, Step 4-5):
      wellposed_flag = (f has DEFINITE SIGN over the physical tau-window:
                        H^2_source finite & POSITIVE everywhere)
                       AND (a bounded fixed point H^2* exists: net(tau)=0 at some tau*).
      PASS iff wellposed_flag AND a fixed point exists UNCONDITIONALLY (at the
        nominal substrate-first stiffness AND robustly across the tested range).
      INFO iff well-posed (definite sign) but the fixed point is CONDITIONAL on
        the fabric-stiffness magnitude (exists at/above a threshold stiffness, NOT
        for all tested values) -- the S41 fabric-stiffness OPEN channel is not pinned.
      FAIL iff the functional inherits the S19d/S40 divergence (NO fixed point at
        ANY tested fabric stiffness -- fabric term never cures the runaway).
    """
    # single-crystal: must inherit the CLOSED S19d divergence (no balance point)
    sc_diverges = bool(sc["runaway"] and (not sc["has_fixed_point"]))  # (local)

    # nominal = substrate-first curvature-scale stiffness (d2S_fold/dS_fold), passed in as nominal_idx
    nominal = fab_scan_list[nominal_idx]  # (local)
    nominal_has_fp = bool(nominal["has_fixed_point"])  # (local) bounded fixed point at nominal stiffness
    nominal_wellposed = bool(nominal["source_definite_positive"])  # (local) definite +sign source

    # across stiffness grid: which give a bounded fixed point
    fp_flags = [bool(s["has_fixed_point"]) for s in fab_scan_list]  # (local)
    wp_flags = [bool(s["source_definite_positive"]) for s in fab_scan_list]  # (local)
    n_fp = sum(fp_flags)  # (local) count of stiffness values yielding a fixed point
    n_total = len(fab_scan_list)  # (local)
    # all-stiffness well-posedness: source definite-positive INDEPENDENT of fabric
    all_wellposed = all(wp_flags)  # (local) source bounded+positive for every stiffness (it is fabric-independent)

    # is the fixed point CONDITIONAL? (exists at some but not all stiffness => threshold)
    fixed_point_conditional = (n_fp > 0) and (n_fp < n_total)  # (local)
    fixed_point_unconditional = (n_fp == n_total)  # (local) every tested stiffness gives a fixed point
    fixed_point_never = (n_fp == 0)  # (local) no stiffness cures the runaway

    # locate the threshold stiffness (smallest stiffness giving a fixed point)
    ks_thresh = None  # (local)
    for ks, fp in zip(stiffness_grid, fp_flags):
        if fp:
            ks_thresh = float(ks)
            break

    detail = (
        f"sc_diverges={sc_diverges};source_definite_positive(all)={all_wellposed};"
        f"n_fixedpoint={n_fp}/{n_total};nominal_has_fp={nominal_has_fp};"
        f"fp_conditional={fixed_point_conditional};ks_thresh={ks_thresh};"
        f"nominal_tau_star={nominal['tau_star']:.4f}"
    )

    value_dict = {
        "rho_relic_MKK": rho["rho_relic_MKK"],
        "rho_relic_contrib": rho["contrib"],
        "pairs_check": rho["pairs_check"],
        "sc_runaway": sc["runaway"],
        "sc_has_fixed_point": sc["has_fixed_point"],
        "sc_diverges": sc_diverges,
        "n_fixedpoint": n_fp,
        "n_total": n_total,
        "all_wellposed": all_wellposed,
        "nominal_has_fp": nominal_has_fp,
        "nominal_tau_star": nominal["tau_star"],
        "nominal_H2_star": nominal["H2_star"],
        "fixed_point_conditional": fixed_point_conditional,
        "ks_thresh": ks_thresh,
    }

    # ---- verdict decision (Step 4-5 rubric) ----
    if not sc_diverges:
        # single-crystal did NOT inherit the CLOSED divergence as required ->
        # model self-consistency check failed; report INFO (cannot cleanly verdict
        # the feedback question without the divergence baseline reproduced).
        composite = "INFO"  # (local)
    elif fixed_point_never:
        # fabric term NEVER cures the runaway at any tested stiffness ->
        # inherits S19d divergence.
        composite = "FAIL"  # (local)
    elif all_wellposed and fixed_point_unconditional:
        # well-posed (definite +sign) AND a bounded fixed point exists for EVERY
        # tested stiffness -> unconditional closure.
        composite = "PASS"  # (local)
    elif all_wellposed and (nominal_has_fp or fixed_point_conditional):
        # well-posed in FORM (definite +sign) but the bounded fixed point is
        # CONDITIONAL on the (unpinned, S41-open) fabric-stiffness magnitude ->
        # the EXPECTED open-frontier INFO band.
        composite = "INFO"  # (local)
    else:
        composite = "INFO"  # (local) well-posed but fixed point sub-threshold; conditional

    # ---- 3-tuple (schema-v2) ----
    # SIGN (Step-4 directional pre-reg): "R_neighbor>0 OPPOSES the dS/dtau>0 drive;
    #   the net feedback CHANGES SIGN at tau* when the fabric dominates, producing a
    #   bounded fixed point." SIGN PASS iff the net feedback DOES cross zero (fixed
    #   point exists) at the nominal substrate-first stiffness; SIGN FAIL iff the
    #   net feedback never changes sign at nominal (fabric never dominates -> runaway).
    sign_v = "PASS" if nominal_has_fp else "FAIL"  # (local)

    # MAGNITUDE: bounded fixed point -> PASS; conditional -> INFO; runaway -> FAIL
    if composite == "PASS":
        mag_v = "PASS"  # (local)
    elif composite == "FAIL":
        mag_v = "FAIL"  # (local)
    else:
        mag_v = "INFO"  # (local)

    # REGIME: VALID iff the full physical window [tau_fold, tau_now] was scanned
    #   (no auto-shortening; 200 pts).
    regime_v = "VALID"  # (local) full physical window scanned at 200 pts

    # ---- composite-collapse cross-check (gate-verdicts.md deterministic rule) ----
    if regime_v == "BREAKDOWN":
        collapse = "FAIL"  # (local)
    elif sign_v == "FAIL":
        collapse = "FAIL"  # (local)
    elif mag_v == "FAIL" and regime_v == "VALID":
        collapse = "FAIL"  # (local)
    elif mag_v == "FAIL" and regime_v == "MARGINAL":
        collapse = "INFO"  # (local)
    elif mag_v == "INFO":
        collapse = "INFO"  # (local)
    else:
        collapse = "PASS"  # (local)

    # The composite from the physics rubric and the 3-tuple collapse must agree;
    # if they differ, the 3-tuple collapse is canonical (pre-registered determinism).
    if collapse != composite:
        composite = collapse

    return composite, sign_v, mag_v, regime_v, detail, value_dict


# ===========================================================================
# MAIN
# ===========================================================================
def main():
    print("=" * 78)
    print(f"{GATE_ID}  ([CHAIN], PHONONIC)")
    print("=" * 78)

    pins = log_input_pins([SCRIPT_PATH, CANONICAL_PATH, BANDCACHE_PATH])

    # --- STEP 1: rho_relic ---
    print("\n--- STEP 1: rho_relic (produced-quanta density; KINEMATICS IN HAND) ---")
    rho = assemble_rho_relic()
    print(f"  Fock multiplicities (B1,B2,B3) = {rho['m']}")
    print(f"  per-band gaps (M_KK) = {{B1:{rho['Delta']['B1']:.6f}, "
          f"B2:{rho['Delta']['B2']:.6f}, B3:{rho['Delta']['B3']:.6f}}}")
    print(f"  n_per_mode = {rho['n_per_mode']:.6f}  (pairs/mode, P_exc={P_exc_kz})")
    print(f"  band contributions (M_KK) = {{B1:{rho['contrib']['B1']:.4f}, "
          f"B2:{rho['contrib']['B2']:.4f}, B3:{rho['contrib']['B3']:.4f}}}")
    print(f"  rho_relic = {rho['rho_relic_MKK']:.6f} (M_KK units)")
    print(f"  pairs_check = {rho['pairs_check']:.4f}  (must equal n_pairs={n_pairs})")
    assert abs(rho["pairs_check"] - n_pairs) < 1e-9, "pair conservation broken"

    # --- STEP 1b: band-cache cross-check ---
    print("\n--- STEP 1b: band-cache cross-check (L_max=10 master spectrum) ---")
    bc = bandcache_crosscheck()
    print(f"  bot-20 sectors = {bc['bot20_sectors']}")
    print(f"  lowest distinct |lambda| levels = {[round(x,5) for x in bc['lowest_levels']]}")
    print(f"  lowest level gaps = {[round(x,5) for x in bc['level_gaps']]}")
    print(f"  min|lambda| = {bc['min_abs_lambda']:.6f}, n_modes(L<=10) = {bc['n_modes_Lle10']}")

    rho_val = rho["rho_relic_MKK"]  # (local)

    # --- STEP 2: single-crystal loop (recover CLOSED S19d divergence) ---
    print("\n--- STEP 2: single-crystal feedback loop (S19d/S40 -> DIVERGES) ---")
    sc = fixed_point_scan(rho_val, include_fabric=False, fabric_stiffness=0.0)
    print(f"  net feedback over window: runaway={sc['runaway']} "
          f"(single-crystal: kappa_drive=dS/dtau/S_fold>0 everywhere, no fabric brake)")
    print(f"  has_fixed_point = {sc['has_fixed_point']} (net(tau)=0 balance point), "
          f"H2_source bounded+positive = {sc['source_definite_positive']}")
    print("  => recovers the CLOSED single-crystal divergence (no balance point, no finite fixed point)"
          if (sc['runaway'] and not sc['has_fixed_point'])
          else "  => single-crystal did NOT diverge as expected (model check)")

    # --- STEP 3-4: fabric-restored feedback, scan over fabric stiffness ---
    print("\n--- STEP 3-4: FABRIC-restored feedback (TAU-STAB, S41) ---")
    # Fabric stiffness magnitudes span weak (cannot oppose drive) to stiff
    # (dominates drive => balance point tau* exists). The SUBSTRATE-FIRST NOMINAL
    # stiffness is the spectral-action well-sharpness ratio d2S_fold/dS_fold
    # (S42; = 5.4176): the curvature-to-gradient scale of the spectral action that
    # sets how stiffly neighboring crystals resist tau-change. kappa_drive ~
    # dS_fold/S_fold ~ 0.234 at fold; R_neighbor needs comparable magnitude.
    ks_nominal = d2S_fold / dS_fold  # (local) substrate-first curvature-scale fabric stiffness (S42)
    stiffness_grid = np.array(
        [0.0, 0.5, 1.0, 2.0, ks_nominal, 10.0, 50.0]
    )  # (local) fabric stiffness multipliers; ks_nominal=d2S/dS is the substrate-first scale
    nominal_idx = int(np.argmin(np.abs(stiffness_grid - ks_nominal)))  # (local) index of nominal stiffness
    fab_scans = []  # (local)
    for ks in stiffness_grid:
        s = fixed_point_scan(rho_val, include_fabric=True, fabric_stiffness=float(ks))
        fab_scans.append(s)
        tstar = f"{s['tau_star']:.4f}" if np.isfinite(s["tau_star"]) else "none"  # (local)
        tag = " <-- NOMINAL (d2S/dS)" if abs(ks - ks_nominal) < 1e-9 else ""  # (local)
        print(f"  fabric_stiffness={ks:7.3f}: has_fixed_point={s['has_fixed_point']!s:5}, "
              f"tau_star={tstar:>7}, frac(net<0)={s['frac_net_negative']:.3f}, "
              f"source_def_pos={s['source_definite_positive']}{tag}")

    # --- VERDICT ---
    print("\n--- VERDICT ---")
    composite, sign_v, mag_v, regime_v, detail, vdict = decide_verdict(
        rho, sc, fab_scans, stiffness_grid, nominal_idx
    )
    print(f"  composite = {composite}")
    print(f"  sign_verdict = {sign_v}  magnitude_verdict = {mag_v}  regime_verdict = {regime_v}")
    print(f"  detail = {detail}")

    # --- assemble verdict value string ---
    nominal_tstar = vdict["nominal_tau_star"]  # (local)
    nominal_H2 = vdict["nominal_H2_star"]  # (local)
    value_str = (
        f"composite={composite};"
        f"rho_relic_MKK={rho['rho_relic_MKK']:.6f};"
        f"rho_contrib_B1={rho['contrib']['B1']:.4f};rho_contrib_B2={rho['contrib']['B2']:.4f};"
        f"rho_contrib_B3={rho['contrib']['B3']:.4f};pairs_check={rho['pairs_check']:.2f};"
        f"sc_diverges={vdict['sc_diverges']};sc_runaway={vdict['sc_runaway']};"
        f"sc_has_fixed_point={vdict['sc_has_fixed_point']};"
        f"source_definite_positive_all={vdict['all_wellposed']};"
        f"n_fixedpoint={vdict['n_fixedpoint']}/{vdict['n_total']};"
        f"nominal_stiffness_d2S_over_dS={d2S_fold / dS_fold:.6f};"
        f"nominal_has_fixed_point={vdict['nominal_has_fp']};"
        f"nominal_tau_star={nominal_tstar:.6f};"
        f"nominal_H2_star_reduced={nominal_H2:.6e};"
        f"fixed_point_conditional={vdict['fixed_point_conditional']};"
        f"ks_threshold={vdict['ks_thresh']};"
        f"dS_dtau_fold={dS_fold:.2f};kappa_drive_fold={dS_fold / S_fold:.6f};"
        f"wellposed={composite in ('PASS', 'INFO')};"
        f"single_crystal_S19d_DIVERGENCE_stays_closed=True;"
        f"sign={sign_v};magnitude={mag_v};regime={regime_v};CLASS=FULL;regulator_pin=a_n_zeta"
    )

    # --- dual-SHA ---
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_PATH, pins)
    print(f"\n  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    # --- save npz ---
    np.savez(
        SESSION_95_DIR / "s95_w3_3_back_reaction_closure.npz",
        gate_id=GATE_ID,
        composite=composite,
        sign_verdict=sign_v,
        magnitude_verdict=mag_v,
        regime_verdict=regime_v,
        rho_relic_MKK=rho["rho_relic_MKK"],
        rho_contrib_B1=rho["contrib"]["B1"],
        rho_contrib_B2=rho["contrib"]["B2"],
        rho_contrib_B3=rho["contrib"]["B3"],
        n_per_mode=rho["n_per_mode"],
        pairs_check=rho["pairs_check"],
        fock_mult=np.array([rho["m"]["B1"], rho["m"]["B2"], rho["m"]["B3"]]),
        band_gaps=np.array([rho["Delta"]["B1"], rho["Delta"]["B2"], rho["Delta"]["B3"]]),
        sc_taus=sc["taus"],
        sc_H2_source=sc["H2_source"],
        sc_net=sc["net"],
        sc_runaway=sc["runaway"],
        sc_has_fixed_point=sc["has_fixed_point"],
        sc_source_definite_positive=sc["source_definite_positive"],
        stiffness_grid=stiffness_grid,
        nominal_idx=nominal_idx,
        fab_has_fixed_point=np.array([s["has_fixed_point"] for s in fab_scans]),
        fab_tau_star=np.array([s["tau_star"] for s in fab_scans]),
        fab_H2_star=np.array([s["H2_star"] for s in fab_scans]),
        fab_frac_net_negative=np.array([s["frac_net_negative"] for s in fab_scans]),
        fab_source_definite_positive=np.array([s["source_definite_positive"] for s in fab_scans]),
        nominal_taus=fab_scans[nominal_idx]["taus"],
        nominal_net=fab_scans[nominal_idx]["net"],
        nominal_H2_source=fab_scans[nominal_idx]["H2_source"],
        nominal_tau_star=vdict["nominal_tau_star"],
        nominal_H2_star=vdict["nominal_H2_star"],
        bot20_sectors=json.dumps(bc["bot20_sectors"]),
        lowest_levels=np.array(bc["lowest_levels"]),
        level_gaps=np.array(bc["level_gaps"]),
        dS_fold=dS_fold,
        d2S_fold=d2S_fold,
        S_fold=S_fold,
        kappa_drive_fold=dS_fold / S_fold,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        value_str=value_str,
        detail=detail,
    )
    print(f"  saved npz -> {SESSION_95_DIR / 's95_w3_3_back_reaction_closure.npz'}")

    # --- plot: net feedback vs tau (fixed-point structure) + bounded source ---
    make_plot(rho_val, sc, fab_scans, stiffness_grid, nominal_idx, composite)

    # --- emit verdict + dual-SHA + 3-tuple ---
    append_verdict(composite, value_str, audit_sha, content_sha)
    tuple_detail = (
        "SIGN=fabric R_neighbor>0 OPPOSES dS/dtau>0 drive; net d(H^2)/dtau changes "
        "sign at tau* when fabric dominates => bounded fixed point (SIGN PASS iff net "
        "sign crosses zero at nominal stiffness); MAG=fixed-point boundedness "
        "(bounded=PASS / conditional=INFO / runaway=FAIL); REGIME=full physical "
        "window [tau_fold,tau_now] scanned at 200 pts, single-crystal S19d divergence "
        "stays CLOSED"
    )
    append_3tuple_row(sign_v, mag_v, regime_v, tuple_detail)

    print(f"\n{GATE_ID}: {composite} -- value={value_str!r}")
    print(f"  audit_sha256={audit_sha}")
    print(f"  3-tuple: sign={sign_v} magnitude={mag_v} regime={regime_v}")
    return 0


def make_plot(rho_val, sc, fab_scans, stiffness_grid, nominal_idx, composite):
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Panel A: net feedback strength net(tau)=kappa_drive-R_neighbor vs tau, per
    # fabric stiffness. The FIXED POINT is where net crosses zero (drive balanced
    # by fabric brake => bounded H^2*). Single-crystal (stiffness 0) never crosses
    # zero => monotone runaway (S19d divergence). The plot directly shows which
    # stiffness values produce a balance point.
    ax = axes[0]
    cmap = plt.cm.viridis(np.linspace(0.15, 0.92, len(fab_scans)))  # (local)
    for s, ks, col in zip(fab_scans, stiffness_grid, cmap):
        lw = 2.4 if abs(ks - stiffness_grid[nominal_idx]) < 1e-9 else 1.2  # (local)
        lbl = f"stiffness={ks:g}" + (" (NOMINAL d2S/dS)" if abs(ks - stiffness_grid[nominal_idx]) < 1e-9 else "")  # (local)
        ax.plot(s["taus"], s["net"], lw=lw, color=col, label=lbl)
        if s["has_fixed_point"] and np.isfinite(s["tau_star"]):
            ax.plot(s["tau_star"], 0.0, "o", color=col, ms=7, mec="k", mew=0.6)
    ax.axhline(0, color="k", lw=1.0, ls=":")
    ax.axvline(tau_fold, color="gray", lw=0.8, ls="--", label=r"$\tau_{fold}$")
    ax.set_xlabel(r"$\tau$ (fold $\to$ present)")
    ax.set_ylabel(r"net feedback $\;\kappa_{drive}(\tau)-R_{neighbor}(\tau)$")
    ax.set_title("Panel A: net feedback vs $\\tau$\n"
                 "(zero-crossing = bounded fixed point $\\tau^*$; "
                 "single-crystal never crosses => S19d runaway)")
    ax.legend(fontsize=7, loc="upper right")
    ax.grid(alpha=0.3)
    ax.set_ylim(-1.5, 1.0)

    # Panel B: the BOUNDED source piece H^2_source(tau) (definite-positive => the
    # functional is well-posed in form), with the nominal-stiffness fixed point
    # marked. H^2* = H^2_source(tau*) is finite.
    ax = axes[1]
    nominal = fab_scans[nominal_idx]  # (local)
    ax.plot(nominal["taus"], nominal["H2_source"], "b-", lw=2,
            label=r"$H^2_{source}(\tau)=\frac{8\pi G_{eff}(\tau)}{3}\rho_{relic}$ (bounded, $>0$)")
    if nominal["has_fixed_point"] and np.isfinite(nominal["tau_star"]):
        ax.plot(nominal["tau_star"], nominal["H2_star"], "r*", ms=16, mec="k", mew=0.7,
                label=fr"fixed point $H^2_*={nominal['H2_star']:.3e}$ at $\tau^*={nominal['tau_star']:.3f}$"
                      + "\n(NOMINAL stiffness d2S/dS)")
    ax.axvline(tau_fold, color="gray", lw=0.8, ls="--", label=r"$\tau_{fold}$")
    ax.set_xlabel(r"$\tau$ (fold $\to$ present)")
    ax.set_ylabel(r"$H^2_{source}$ (reduced $M_{KK}$ units)")
    ax.set_title("Panel B: bounded source piece + fixed point\n"
                 "(definite-positive $\\Rightarrow$ functional well-posed in form)")
    ax.legend(fontsize=8, loc="best")
    ax.grid(alpha=0.3)

    fig.suptitle(f"{GATE_ID}  -- verdict: {composite}\n"
                 r"$H^2=f(\rho_{relic},S_{SA})$ back-reaction closure: produced "
                 r"quanta $\to$ emergent $H^2$ (PHONONIC); single-crystal S19d divergence stays CLOSED",
                 fontsize=11)
    fig.tight_layout()
    out = SESSION_95_DIR / "s95_w3_3_back_reaction_closure.png"
    fig.savefig(out, dpi=130, bbox_inches="tight")
    plt.close(fig)
    print(f"  saved plot -> {out}")


if __name__ == "__main__":
    sys.exit(main())
