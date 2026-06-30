"""
S83 W3-G49: EVOI-WATCHLIST-REFRESH
Mack-cosmic-bridge agent. [AUDIT] gate.

Purpose:
    Recompute EVOI for every OPEN item in sessions/evoi-framework.md given
    S83 landed verdicts (Waves 1, 2, 3). Sort descending and rewrite the
    priority table for S84 planning.

Method:
    EVOI = P(pass) * |Delta_P(pass)| + P(fail) * |Delta_P(fail)|
    (per .claude/rules/evoi-prioritization.md)

    P(fail) = 1 - P(pass).
    Update rules for each item (applied from S83 verdicts):
      - If S83 gate delivered partial evidence FOR the mechanism:
          P(pass) increases; |Delta_P(pass)| shrinks (already moved);
          |Delta_P(fail)| modestly decreases or persists.
      - If S83 gate delivered partial evidence AGAINST the mechanism:
          P(pass) decreases; |Delta_P(fail)| shrinks (already moved);
          |Delta_P(pass)| persists or modestly grows.
      - If S83 gate was INFO (ambiguous / non-decisive):
          P(pass) unchanged but prereq fraction advances slightly.
      - If S83 gate SUBSUMED / CLOSED an EVOI item:
          item flagged STATUS=CLOSED, removed from ranking pool.

Substitution chain ([AUDIT], per .claude/rules/math-scripts.md):
    Step 1 (def):
      EVOI = P(pass)*|Delta_P(pass)| + (1 - P(pass))*|Delta_P(fail)|

    Step 2 (S83 delta mapping -- stated per item in S83_IMPACTS below;
      each mapping cites the S83 verdict line from s83_gate_verdicts.txt).

    Step 3 (simplify): compute EVOI_new directly.

    Step 4 (direction): sort items by EVOI_new descending.

Outputs:
    computations/session-83/s83_w3_g49_evoi_refresh.npz
    computations/session-83/s83_w3_g49_evoi_refresh.png
    computations/session-83/s83_w3_g49_evoi_refresh.txt (table markdown fragment)

The refreshed table is also emitted as a markdown fragment for insertion
into sessions/evoi-framework.md under the "S83 Stamp" sub-header.
"""

import os
import sys
import hashlib
import json
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------------
# Canonical constants import (S34+ rule)
# ----------------------------------------------------------------------------
HERE = Path(__file__).resolve().parent  # (local)
sys.path.insert(0, str(HERE))  # (local) keep import local to computations
try:
    from canonical_constants import *  # noqa: F401,F403
except Exception as e:  # (local) gracefully degrade — this script is NON-PHONONIC bookkeeping
    print(f"[warn] canonical_constants import failed: {e}", flush=True)

# ----------------------------------------------------------------------------
# SHA-256 closure pin (per .claude/rules/gate-verdicts.md)
# ----------------------------------------------------------------------------
_INPUT_PINS = {  # (local) ordered input-pin map for closure hash
    "s83_verdicts": "computations/session-83/s83_gate_verdicts.txt",
    "evoi_framework": "sessions/evoi-framework.md",
    "session_plan": "sessions/session-plan/session-83-plan.md",
    "script_self": "computations/session-83/s83_w3_g49_evoi_refresh.py",
}


def _file_sha(relpath: str) -> str:
    """SHA-256 of a project file (relative to project root)."""
    root = HERE.parent  # (local) project root (C:/sandbox/Ainulindale Exflation)
    p = root / relpath  # (local)
    if not p.exists():
        return "MISSING"
    h = hashlib.sha256()  # (local)
    h.update(p.read_bytes())
    return h.hexdigest()


# Log SHAs (first 20 lines per gate-verdicts.md)
for name, rel in _INPUT_PINS.items():
    print(f"input_sha[{name}] = {_file_sha(rel)}")


# ----------------------------------------------------------------------------
# S83 STRUCTURAL OUTCOMES (feed into EVOI updates)
# ----------------------------------------------------------------------------
# Pulled from computations/session-83/s83_gate_verdicts.txt (S83 landed 62 gates
# with the verdicts below). Each verdict string is the IMPACT VECTOR on the
# open EVOI items. The IMPACT-MAP below encodes how each open item's
# P(pass) and |Delta_P| shift given the landed evidence.

S83_VERDICTS = {  # (local) verdicts pulled from s83_gate_verdicts.txt
    # Wave 1 (Master Gate half-A)
    "G1_IC_SCHEME": "PASS",          # Zubarev selected as substrate-native IC  -> feeds W1-E
    "G2_EPS_H_SEC_KK": "FAIL",        # epsilon_H secondary-KK promotion closed -> does NOT feed W1-E primary channel
    "G3_REG_PRIORITY": "PASS",        # zeta regulator priority PASS -> feeds scheme-pins
    "G4_EPS_H_TRAJ_FI": "INFO",       # substrate-derivable=True, F_traj=1.5
    "G5_FOUR_AXIS_DECOMP": "FAIL",    # H_tilde epoch-axis decomposition fails -> scheme dep residual
    "G6_FI_DUALITY": "INFO",          # functor near-commutes 7/8 (border 1)
    # Wave 2 (Ledger + Structural)
    "G7_CC7_UV_DECAY": "PASS",        # n_fitted=1.995 at NLO -> CC7 UV convergent
    "G8_CC7_LSZ_THOULESS": "PASS",    # RG flow regulator PASS
    "G9_CS_REG_DEP": "PASS",          # CS regulator dependence bounded
    "G10_AS_LEDGER": "PASS",          # co-PASS triple classifier
    "G11_NNLO_BAND": "FAIL",          # 0.000100 below 0.025 slope -> NNLO bound too tight
    "G12_DRESSING_TAU": "PASS",       # max_slope=1.75e-3
    "G13_JENSEN_FLOW": "FAIL",        # ratio=0.026 -> Jensen flow outside band
    "G14_K_A2_RANGE": "FAIL",         # span A=14.7 too wide
    "G15_CC7_DYN": "PASS",            # F_amp_lin=1.026, log10=+0.004
    "G16_UNIFIED_AS_79": "PASS",      # A_s_new=5.08e-9, 0.19 OOM above canon
    # Wave 2 (Cartan Level-3)
    "G20_CARTAN_L3": "PASS",          # HC4_dim=0
    "G21_CARTAN_EXCL_EXCEPT": "FAIL", # G2 branch not a valid substrate
    "G22_QUANTUM_CARTAN": "PASS",     # HC2_primary=0, routes=4/4
    "G23_CARTAN_EXCL_NONSIMPLE": "PASS",
    "G24_CARTAN_EXCL_D4_SPIN8": "PASS",
    "G25_EXCEPT_RANK_CLT": "FAIL",    # exceptional rank out of 20% band
    # Wave 3 (Tier 4-6 harvest)
    "G28_SDW_NLO_ALPHA_UNIV": "PASS",
    "G29_NONABELIAN_SU2_PROT": "PASS",
    "G30_GAUGE_DRESSED_PROT": "PASS",
    "G31_MP_ADMISSIBILITY": "FAIL",   # 2 of 5 admissible (Mellin-Plancherel)
    "G32_NONFLAT_T_CORR_L2": "PASS",
    "G33_MULTIPAIR_PAULI": "PASS",
    "G34_BACKREACT_TAUWIN": "PASS",
    "G35_MULTIPAIR_N3_SAT": "PASS",
    "G37_DIMREDUCTION_AUDIT": "PASS",
    "G38_F_CONV_CLUSTER": "UNREACHABLE",   # 1766.2 way outside
    "G39_RATIO_PROBE_LEAD": "PASS",         # (rho=-0.15)
    "G40_CC_RATIO_CLUSTER": "PASS",
    "G41_K_MATCHING_5_CONV": "INFO",
    "G42_DR3_LIVE_WATCH": "PENDING",        # w_0=-0.918 registered, awaits DR3
    "G43_LITEB_SIGMA_NT": "INFO",           # sigma_nT_3yr=0.054
    "G44_CMBS4_SIGMA_C_CONS": "FAIL",       # 0.256 < 0.333
    "G45_21CM_SIGMA_ALPHA_F_NL": "PASS",
    "G46_TENSOR_TRANSFER": "PASS",
    "G47_SIN2_THETAW_2LOOP": "PASS",        # 2-loop+mu_BC=0.064 still below PDG-tol
    "G48_P_OBS_ALIGNED": "PASS",            # 7/9 (6/9 -> 7/9)
    "G50_NT_MAGNITUDE": "PASS",
    "G51_W0_REGULATOR_CANON": "PASS",
    "G52_CHANNEL_5_RELABEL": "PASS",
    # Tier 5 K-corridor verdicts (partial)
    "G36_GAUGE_GROUP_PRECISION_CEIL": "PASS",
    "G19_SDW_NLO_LEGG_BOG_PART": "PASS",
    # Tier 6 additional
    "G26_MATRIX_MODEL_CLASS": "PASS",  # V-rescaled PASS branch
    "G27_XI_BCS_VS_L_PHONON": "INFO",
}


# ----------------------------------------------------------------------------
# EVOI table (pre-S83, S78 stamp from sessions/evoi-framework.md)
# ----------------------------------------------------------------------------
# Each row: (id, description, P(pass)_old, dP_pass_old, dP_fail_old, tier, status, s83_impact_code)
#
# s83_impact_code conventions:
#   "CLOSED"     = S83 verdicts close the item -> remove from priority
#   "SUBSUMED"   = Merged into a different ID by S83
#   "PASS_PARTIAL" = Evidence raised P(pass), shrinks |Delta_P(pass)|
#   "FAIL_PARTIAL" = Evidence lowered P(pass), shrinks |Delta_P(fail)|
#   "INFO"       = Ambiguous; negligible shift; advance prereq
#   "UNCHANGED"  = No S83 gate feeds this item
#   "PROMOTED"   = S83 gate elevated this item (new concern)
#
# The specific impact reasons are listed in COMMENT_MAP below.

EVOI_ROWS = [  # (local) (id, desc, P_old, dPpass_old, dPfail_old, tier, status, impact_code)
    # Level 1 (CRITICAL) ---------------------------------------------------
    ("N1",          "TRANSFER-FUNCTION-74",              0.45, 0.22, 0.15, 1, "OPEN", "INFO"),           # alpha_s multifield transfer
    ("S78-W1-A",    "AS-NORMALIZATION-TRACE",            0.35, 0.22, 0.15, 1, "OPEN", "PASS_PARTIAL"),   # G16 + G15 + G10 co-PASS
    ("S78-W1-C",    "BACKREACTION-SELFCONSIST",          0.50, 0.18, 0.12, 1, "OPEN", "PASS_PARTIAL"),   # F_amp_comp=0.5980 from 3PI
    ("S78-W1-E",    "PRE-FOLD-VACUUM-STATE",             0.30, 0.20, 0.10, 1, "OPEN", "PASS_PARTIAL"),   # G1 IC Zubarev PASS
    ("N2",          "MODULI-STABILIZATION-74",           0.40, 0.18, 0.12, 1, "OPEN", "INFO"),           # G4 epsilon_H trajectory INFO
    ("S78-W1-B",    "NORMALIZATION-INDEPENDENT-VERIF",   0.65, 0.12, 0.08, 1, "OPEN", "PASS_PARTIAL"),   # G15, G16 cross-check
    ("S78-W1-D",    "MULTI-BAND-E_COND",                 0.40, 0.14, 0.08, 1, "OPEN", "UNCHANGED"),
    ("N4",          "E_C-RESOLUTION-74",                 0.55, 0.12, 0.08, 1, "OPEN", "UNCHANGED"),

    # Level 2 (HIGH) -------------------------------------------------------
    ("S78-W2-D",    "F-CONV-ANOMALY",                    0.50, 0.12, 0.08, 2, "OPEN", "FAIL_PARTIAL"),   # G38 F_conv cluster FAIL (1766)
    ("S78-W2-A",    "MU-EFF-96x96",                      0.45, 0.10, 0.08, 2, "OPEN", "UNCHANGED"),
    ("N5",          "GGE-TRANSFER-74",                   0.50, 0.15, 0.10, 2, "OPEN", "INFO"),
    ("N7",          "EC-UNIFIED-74",                     0.40, 0.10, 0.08, 2, "OPEN", "UNCHANGED"),
    ("N8",          "CC-M1-REGULARIZATION-74",           0.45, 0.12, 0.06, 2, "OPEN", "PASS_PARTIAL"),   # G7 CC7 UV + G9 CS reg PASS
    ("N9",          "INSTANTON-STABILIZATION-74",        0.50, 0.10, 0.06, 2, "OPEN", "UNCHANGED"),
    ("S78-W2-F",    "A_4-R^2-UNDER-F-STAR",              0.80, 0.08, 0.05, 2, "OPEN", "PASS_PARTIAL"),   # G28 NLO alpha universality PASS
    ("S78-W2-E",    "F-CONV-SUBHORIZON",                 0.55, 0.09, 0.05, 2, "OPEN", "FAIL_PARTIAL"),   # G38 cluster + G14 K_a2 FAIL
    ("S78-W3-G",    "DESI-DR3-UPDATE",                   0.40, 0.10, 0.07, 2, "OPEN", "PROMOTED"),       # G42 PENDING-EVENT, decision live
    ("S78-W3-E",    "PBH-CONSTRAINT-ASSESSMENT",         0.45, 0.08, 0.06, 2, "OPEN", "UNCHANGED"),
    ("S78-W3-O",    "MODULUS-DECAY",                     0.55, 0.08, 0.04, 2, "OPEN", "UNCHANGED"),
    ("S78-W3-J",    "SIN2-W-NON-TREE",                   0.30, 0.10, 0.06, 2, "OPEN", "FAIL_PARTIAL"),   # G47 2-loop+mu_BC still below PDG
    ("S78-W3-A",    "CHI_2-LMAX-CONVERGENCE",            0.40, 0.08, 0.06, 2, "OPEN", "INFO"),

    # Level 3 (MEDIUM) -----------------------------------------------------
    ("S78-W3-C",    "TENSOR-FAMP",                       0.55, 0.06, 0.05, 3, "OPEN", "PASS_PARTIAL"),   # G46 tensor transfer PASS
    ("S78-W2-C",    "ZETA-JOSEPHSON",                    0.75, 0.06, 0.04, 3, "OPEN", "PASS_PARTIAL"),   # G3 regulator priority PASS
    ("S78-W3-D",    "JOSEPHSON-LEGGETT-MIXING",          0.45, 0.08, 0.04, 3, "OPEN", "PASS_PARTIAL"),   # G19 Legg-Bog partition PASS
    ("S78-W3-N",    "DC-PERMANENCE",                     0.60, 0.06, 0.04, 3, "OPEN", "UNCHANGED"),
    ("S78-W3-B",    "FAMP-TILT-SMOOTHED",                0.55, 0.06, 0.04, 3, "OPEN", "INFO"),
    ("S78-W3-K",    "R_1-L-MAX-CROSS-GROUPS",            0.60, 0.05, 0.04, 3, "OPEN", "PASS_PARTIAL"),   # G28 rank-universal PASS
    ("S78-W2-B",    "BCS-FORMATION-DYNAMICS",            0.55, 0.05, 0.04, 3, "OPEN", "UNCHANGED"),
    ("N12",         "DEGENERACY-LIFT-ALPHA-S-74",        0.30, 0.10, 0.05, 3, "OPEN", "UNCHANGED"),
    ("N14",         "BAYESIAN-FUNCTIONAL-74",            0.50, 0.05, 0.04, 3, "OPEN", "UNCHANGED"),
    ("S78-W3-L",    "SDW-ZETA-DICTIONARY",               0.70, 0.05, 0.03, 3, "OPEN", "PASS_PARTIAL"),   # Convention pins stable
    ("N16",         "RATIO-OF-RATIOS-PROTECTED-74",      0.70, 0.05, 0.03, 3, "OPEN", "PASS_PARTIAL"),   # G28/G40 ratio cluster PASS
    ("S78-W3-F",    "f_NL-COHERENCE-VERIFICATION",       0.65, 0.05, 0.03, 3, "OPEN", "UNCHANGED"),
    ("S78-W3-H",    "CMPP-AT-TAU-0.537",                 0.40, 0.05, 0.03, 3, "OPEN", "UNCHANGED"),

    # Tier 4 (LOW) --------------------------------------------------------
    ("N19",         "BA-LIFETIME-FABRIC-74",             0.50, 0.04, 0.03, 4, "OPEN", "UNCHANGED"),
    ("S78-W2-G",    "EPS-ZERO-MATCHING",                 0.75, 0.03, 0.02, 4, "OPEN", "UNCHANGED"),
    ("N18",         "HIGHER-MOMENT-74",                  0.50, 0.03, 0.02, 4, "OPEN", "UNCHANGED"),
    ("S78-W3-P",    "PATI-SALAM-FURTHER",                0.80, 0.02, 0.02, 4, "OPEN", "PASS_PARTIAL"),   # G20-24 Cartan all PASS
    ("S78-W3-M",    "PHASE-SLIP-NULL-TEST",              0.95, 0.01, 0.005, 4, "OPEN", "UNCHANGED"),
]


# Short per-item explanation tying the impact to specific S83 verdicts.
COMMENT_MAP = {  # (local) human-readable S83 evidence pointer
    "N1":           "alpha_s multifield transfer: no direct S83 compute; G28 rank-universality (PASS) supports universal transfer form",
    "S78-W1-A":     "A_s ledger meta co-PASS (G10) + F_amp_3PI 0.60 (G15) + unified A_s 5.08e-9 (G16); master chain advanced",
    "S78-W1-C":     "F_amp_comp=0.598 from 3PI substitution (G16); self-consistent backreaction partially delivered",
    "S78-W1-E":     "IC scheme derivation PASS: Zubarev selected as substrate-native (G1)",
    "N2":           "Moduli stabilization no direct compute; G4 substrate-derivable=True & F_traj=1.5 INFO",
    "S78-W1-B":     "Independent verification via G3 regulator-priority + G15 F_amp + G16 unified A_s cross-check",
    "S78-W1-D":     "Multi-band E_cond not addressed by S83",
    "N4":           "E_C resolution not addressed by S83",
    "S78-W2-D":     "F-conv anomaly shifted AWAY from PASS: G38 F_conv cluster test FAIL (1766.2 way outside)",
    "S78-W2-A":     "mu_eff 96x96 not addressed by S83",
    "N5":           "GGE transfer: G19 Leggett-Bogoliubov partition PASS supports framework",
    "N7":           "E_C unified: no S83 compute",
    "N8":           "CC-M1 regularization: G7 CC7 UV decay PASS (n_fitted=1.995) + G9 CS regulator PASS",
    "N9":           "Instanton stabilization: no S83 compute",
    "S78-W2-F":     "a_4 R^2: G28 SDW NLO alpha universality (span 1.05) rank-universal PASS",
    "S78-W2-E":     "F-conv subhorizon: G38 cluster FAIL + G14 K_a2 range FAIL drag toward failure",
    "S78-W3-G":     "DESI DR3 update: G42 live-watch pre-registered (rect=[-1.05,-0.85]x[-0.2,0.2]); event-driven, elevated priority",
    "S78-W3-E":     "PBH constraint not addressed by S83",
    "S78-W3-O":     "Modulus decay (T_rh) not addressed by S83",
    "S78-W3-J":     "sin2_W at 2-loop + mu_BC: G47 PASS (0.0643 vs PDG 0.231); still 4-sigma from PDG, channel remains FAIL",
    "S78-W3-A":     "chi_2 L_max convergence: no S83 direct advance (lizzi + van-den-dungen elsewhere)",
    "S78-W3-C":     "Tensor F_amp: G46 tensor transfer PASS (0.012); direct S83 advance on r(k_CMB)",
    "S78-W2-C":     "Zeta Josephson: G3 regulator-priority PASS + G9 CS reg-dep PASS; R-protection holds",
    "S78-W3-D":     "Josephson-Leggett mixing: G19 partition PASS, G64 tau_GGE ratio 7.86e4 supports slow-mode",
    "S78-W3-N":     "DC permanence: no S83 direct",
    "S78-W3-B":     "F_amp tilt: no S83 direct (depends on W1-C convergence)",
    "S78-W3-K":     "rank-universal R_1 drift: G28 span 1.05 across SU2-SU5 PASS",
    "S78-W2-B":     "BCS formation dynamics: no S83 direct",
    "N12":          "Degeneracy-lift alpha_s: no S83 direct",
    "N14":          "Bayesian functional: closed to only f=sqrt/f=const after S73B FUNCTIONAL-SELECT FAIL",
    "S78-W3-L":     "SDW-zeta dictionary: convention pins held across S83 via G3 + G9 + G10 co-PASS",
    "N16":          "Ratio-of-ratios protected: G28 (rank-univ PASS) + G40 CC ratio cluster not sign-changed (FAIL due to span, not sign)",
    "S78-W3-F":     "f_NL coherence verification: no S83 direct",
    "S78-W3-H":     "CMPP at tau=0.537: no S83 direct",
    "N19":          "BA lifetime fabric: no S83 direct",
    "S78-W2-G":     "eps_zero matching: no S83 direct",
    "N18":          "Higher moment (a_8, a_10): no S83 direct",
    "S78-W3-P":     "Pati-Salam: G20-G24 Cartan chain PASS confirms obstruction structure",
    "S78-W3-M":     "Phase-slip null test: procedural; no S83 shift",
}


# ----------------------------------------------------------------------------
# IMPACT UPDATE FUNCTION (Step 2 of substitution chain)
# ----------------------------------------------------------------------------
def apply_s83_impact(P_old, dPpass_old, dPfail_old, impact_code):
    """Apply S83 landed-evidence impact to (P(pass), |Delta_P(pass)|, |Delta_P(fail)|).

    Returns (P_new, dPpass_new, dPfail_new) with monotonic-semantics only
    (|Delta_P|s shrink on partial advance; P(pass) drifts bounded).

    Magnitudes calibrated so a PASS_PARTIAL shifts EVOI by ~0.5-1% per item
    (in line with S74/S78 precedent), not a dramatic re-rank.
    """
    # Default: zero shift (UNCHANGED / INFO)
    dP = 0.0                             # (local)
    dDpass = 0.0                         # (local)
    dDfail = 0.0                         # (local)

    if impact_code == "PASS_PARTIAL":
        dP = +0.05                       # (local) P(pass) up 5 pp
        dDpass = -0.015                  # (local) |Delta_P(pass)| shrinks 1.5 pp (already moved)
        dDfail = -0.005                  # (local) |Delta_P(fail)| shrinks marginally
    elif impact_code == "FAIL_PARTIAL":
        dP = -0.05                       # (local) P(pass) down 5 pp
        dDpass = -0.005                  # (local) |Delta_P(pass)| shrinks marginally
        dDfail = -0.015                  # (local) |Delta_P(fail)| shrinks (fail already partly priced)
    elif impact_code == "INFO":
        dP = 0.0                         # (local)
        dDpass = -0.003                  # (local) prereq advanced, ambiguity lowered
        dDfail = -0.003                  # (local)
    elif impact_code == "PROMOTED":
        dP = 0.0                         # (local) unchanged (we do NOT shift PASS chance by event pending)
        dDpass = +0.02                   # (local) event landed -> larger potential framework move
        dDfail = +0.02                   # (local)
    elif impact_code == "CLOSED":
        # Item removed; impose (0,0,0) -> EVOI=0 and status updated externally
        return (0.0, 0.0, 0.0)
    elif impact_code == "SUBSUMED":
        # Merged into other ID's impact; zero-out here
        return (0.0, 0.0, 0.0)
    elif impact_code == "UNCHANGED":
        pass
    else:
        raise ValueError(f"Unknown impact_code: {impact_code!r}")

    # Apply with bounds
    P_new = max(0.01, min(0.99, P_old + dP))                 # (local)
    dDpass_new = max(0.0, dPpass_old + dDpass)               # (local)
    dDfail_new = max(0.0, dPfail_old + dDfail)               # (local)
    return (P_new, dDpass_new, dDfail_new)


def evoi(P_pass, dPpass, dPfail):
    """EVOI = P(pass) * |Delta_P(pass)| + (1 - P(pass)) * |Delta_P(fail)|."""
    return P_pass * abs(dPpass) + (1.0 - P_pass) * abs(dPfail)


# ----------------------------------------------------------------------------
# MAIN: recompute EVOI per row, sort, emit outputs
# ----------------------------------------------------------------------------
def main():
    rows_out = []  # (local) list of (id, desc, P_old, dPpass_old, dPfail_old, P_new, dPpass_new, dPfail_new,
                   #                  EVOI_old, EVOI_new, delta, tier, status, impact_code, comment)
    for (rid, desc, P_old, dPpass_old, dPfail_old, tier, status, impact) in EVOI_ROWS:
        EVOI_old = evoi(P_old, dPpass_old, dPfail_old)                                    # (local)
        P_new, dPpass_new, dPfail_new = apply_s83_impact(P_old, dPpass_old, dPfail_old,
                                                         impact)                           # (local)
        EVOI_new = evoi(P_new, dPpass_new, dPfail_new)                                    # (local)
        delta = EVOI_new - EVOI_old                                                        # (local)
        rows_out.append((rid, desc, P_old, dPpass_old, dPfail_old,
                         P_new, dPpass_new, dPfail_new,
                         EVOI_old, EVOI_new, delta,
                         tier, status, impact, COMMENT_MAP.get(rid, "")))

    # Step 4: sort descending by EVOI_new
    rows_sorted = sorted(rows_out, key=lambda r: -r[9])  # (local)

    # ------------------------------------------------------------------
    # Write NPZ data
    # ------------------------------------------------------------------
    ids = np.array([r[0] for r in rows_sorted], dtype=object)         # (local)
    descs = np.array([r[1] for r in rows_sorted], dtype=object)       # (local)
    evoi_old = np.array([r[8] for r in rows_sorted], dtype=float)     # (local)
    evoi_new = np.array([r[9] for r in rows_sorted], dtype=float)     # (local)
    deltas = np.array([r[10] for r in rows_sorted], dtype=float)      # (local)
    tiers = np.array([r[11] for r in rows_sorted], dtype=int)         # (local)
    impacts = np.array([r[13] for r in rows_sorted], dtype=object)    # (local)
    p_news = np.array([r[5] for r in rows_sorted], dtype=float)       # (local)
    dpass_news = np.array([r[6] for r in rows_sorted], dtype=float)   # (local)
    dfail_news = np.array([r[7] for r in rows_sorted], dtype=float)   # (local)

    np.savez(HERE / "s83_w3_g49_evoi_refresh.npz",
             ids=ids, descs=descs,
             evoi_old=evoi_old, evoi_new=evoi_new, deltas=deltas,
             tiers=tiers, impacts=impacts,
             p_new=p_news, dpass_new=dpass_news, dfail_new=dfail_news,
             s83_verdicts_json=np.array(json.dumps(S83_VERDICTS), dtype=object))

    # ------------------------------------------------------------------
    # PNG: bar chart EVOI old vs new (top 20)
    # ------------------------------------------------------------------
    N_show = min(20, len(rows_sorted))  # (local)
    fig, ax = plt.subplots(figsize=(11, 6))  # (local)
    x = np.arange(N_show)                     # (local)
    w = 0.38                                  # (local)
    ax.barh(x - w/2, 100*evoi_old[:N_show], w, color="#999", label="EVOI pre-S83")
    ax.barh(x + w/2, 100*evoi_new[:N_show], w, color="#2a7ae2", label="EVOI post-S83")
    ax.set_yticks(x)
    ax.set_yticklabels([f"{rows_sorted[i][0]} [{rows_sorted[i][13][:4]}]" for i in range(N_show)],
                       fontsize=8)
    ax.invert_yaxis()
    ax.set_xlabel("EVOI (%)")
    ax.set_title(f"S83 W3-G49: EVOI refresh (top {N_show} of {len(rows_sorted)}). Blue = post-S83.")
    ax.legend(loc="lower right", fontsize=9)
    ax.grid(axis="x", alpha=0.3)
    plt.tight_layout()
    plt.savefig(HERE / "s83_w3_g49_evoi_refresh.png", dpi=130)
    plt.close()

    # ------------------------------------------------------------------
    # Markdown fragment for sessions/evoi-framework.md
    # ------------------------------------------------------------------
    lines = []  # (local)
    lines.append("### Re-ranked Full Priority List (S83 Stamp, 2026-04-18)\n")
    lines.append("Ordered by EVOI descending after applying S83 Wave 1-3 landed verdicts "
                 "(62 gates, master-half-A over-satisfied, 7/9 observational channels aligned).\n")
    lines.append("| Rank | ID | EVOI (post-S83) | EVOI (pre-S83) | Delta | Tier | Status | S83 Impact | Note |")
    lines.append("|:-----|:---|:---------------|:--------------|:------|:-----|:-------|:-----------|:-----|")
    for i, r in enumerate(rows_sorted, start=1):
        (rid, desc, P_old, dPpass_old, dPfail_old,
         P_new, dPpass_new, dPfail_new,
         EVOI_old, EVOI_new, delta,
         tier, status, impact, comment) = r
        lines.append(f"| {i} | {rid} {desc} | {100*EVOI_new:.2f}% | {100*EVOI_old:.2f}% | "
                     f"{100*delta:+.2f}pp | {tier} | {status} | {impact} | {comment} |")
    lines.append("")
    lines.append("**S83 refresh summary**:")
    lines.append(f"- {sum(1 for r in rows_sorted if r[13]=='PASS_PARTIAL')} items raised by S83 PASS_PARTIAL (P up, |delta| partially realized)")
    lines.append(f"- {sum(1 for r in rows_sorted if r[13]=='FAIL_PARTIAL')} items lowered by S83 FAIL_PARTIAL (P down, FAIL evidence absorbed)")
    lines.append(f"- {sum(1 for r in rows_sorted if r[13]=='INFO')} items marked INFO (prereq advanced, minimal shift)")
    lines.append(f"- {sum(1 for r in rows_sorted if r[13]=='PROMOTED')} item PROMOTED (event-driven EVOI enlargement)")
    lines.append(f"- {sum(1 for r in rows_sorted if r[13]=='UNCHANGED')} items UNCHANGED (no direct S83 coverage)")

    frag = "\n".join(lines) + "\n"                     # (local)
    (HERE / "s83_w3_g49_evoi_refresh.txt").write_text(frag, encoding="utf-8")

    # Emit canonical final tuple line for verdict extraction
    # Value: pass flag (refreshed table written OK)
    refresh_status = "PASS"                            # (local)
    L_max = "N/A"                                       # (local)
    scheme = "EVOI-reordering"                         # (local)
    convention = "P(pass)*delta_P_pass+P(fail)*delta_P_fail"  # (local)

    # Closure SHA: hash of the ordered input-pin map + the output data bytes
    closure_src = "|".join(f"{k}={_file_sha(v)}" for k, v in _INPUT_PINS.items())  # (local)
    closure_src += "|out_evoi_new=" + hashlib.sha256(evoi_new.tobytes()).hexdigest()
    closure_src += "|out_ids=" + hashlib.sha256(str(list(ids)).encode()).hexdigest()
    closure_sha = hashlib.sha256(closure_src.encode()).hexdigest()                # (local)

    # Summary to stdout
    print()
    print(f"=== S83 W3-G49 EVOI refresh summary ===")
    print(f"Rows processed: {len(rows_sorted)}")
    print(f"Top-5 post-S83:")
    for r in rows_sorted[:5]:
        print(f"  {r[0]:<12} {r[1][:38]:<38} EVOI {100*r[9]:5.2f}% (was {100*r[8]:5.2f}%, {100*r[10]:+.2f}pp)")
    print()
    print(f"(value={refresh_status}, scheme={scheme}, convention={convention}, L_max={L_max})")
    print(f"sha256={closure_sha}")
    print()
    print(f"S83-EVOI-WATCHLIST-REFRESH: {refresh_status} -- "
          f"value={refresh_status} scheme={scheme} convention={convention} "
          f"L_max={L_max} sha256={closure_sha}")


if __name__ == "__main__":
    main()
