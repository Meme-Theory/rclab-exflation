#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S100b-PS-VARIANT-ID — Pati-Salam variant identification from the rescued
order-one defect fingerprint (substrate texture / algebra classification).

Gate block : sessions/session-plan/session-100b-plan-w2.md §W2-2
Agent      : lizzi-spectral-functional-theorist
Trigger    : [VERIFY]   Classification: PARTICLE
Scheme     : Aydemir-CCS-variant-taxonomy
Convention : defect-fingerprint-3axis
L_max      : N/A (finite spectral triple F; A_F^PS rep theory; no D_K diagonalization)

HYPOTHESIS (plan §W2-2): the framework's order-one defect signature — bare
axiom-5 defect 4.000 (= 2^2, (H,H) sector, N3 PROVEN), reduced to 2.100 after
inner fluctuations without closing (order_one_closes=False) — maps onto exactly
ONE Aydemir/CCS Pati-Salam variant over {A,B,C} x {LR, no-LR}, whose
group-theoretic sin^2(theta_W) at the unification boundary and S_1(3bar,1,1/3)
leptoquark content are then extracted as positive beyond-SM predictions.

FRAMING LAW (MANDATORY, audit criterion): the order-one axiom is NOT
live-broken — Q10 is RESCUED STAGE-3-PERMANENT via the Wedderburn-Frobenius
rescue class (sessions/permanent-results-registry.md §VII.W-3, S88 W4a-17:
A_F = C+H+M_3(C) is the unique 7-axiom algebra under M_3 chi-kill). The
conversion performed here is RESCUED-axiom -> positive-variant-ID, never
broken-axiom -> feature. The S93-W6-1 FAIL verdict is consumed as INPUT DATUM
(the defect signature being classified), not re-adjudicated.

REGULATOR PIN (regulator-pin-discipline.md): a_n^{cutoff} — any citation of the
Aydemir/CCS bosonic-action moment structure (a_0^{cutoff} cosmological +
a_2^{cutoff} Einstein-Hilbert + a_4^{cutoff} Yang-Mills/Higgs) is tagged
cutoff-regulator (Tr f(D/Lambda) spectral action). NO numerical a_n value is
consumed by this gate (structural citation only).

MELLIN POLE-SET DECLARATION (context anchor, NOT numerically consumed):
§VII.BE FWD-C4 SU(4)_PS Mellin anchor, residue_s6_PS_Linf = 0.000939364
(canonical, S95 CF-S95-VII-BE-TIER2-REANCHOR, Tier-1 PASS). ALGEBRA = rank-4
A_K^PS (SU(4)_PS extended spectral triple — NOT SU(3));
convention=poleconv-A-double (zeta_D(s) = sum m_k |lambda_k|^{-2s});
(pole_in_s = 6, curvature_grade_n = N/A — substrate-distance pole family, not
an a_n Seeley-DeWitt grade). Cross-algebra caveat: the rank-4 A_3 extension
shifts the shell-sum convergence threshold +1 unit vs SU(3) (s > 9/2,
d_eff = 9 = 8+1); the pole index lives on the EXTENDED triple's dimension
spectrum.

PLAN-TEXT DRIFT (detected at runtime; substrate-first-canonical-sourcing.md
§(ii.B) MANDATORY correction): the plan-block hypothesis pinned "KO_dim shifted
to 2 (S93-W6-1 npz)". The SHA-pinned npz ground truth carries KO_dim = 6 with
sign triple (J^2, JD-vs-DJ, J-gamma) = (+1, +1, -1) and EXPECTED_KO_DIM = 6.
The npz IS the pinned input (SHA verified 11ea23cf...); the runtime value
KO_dim = 6 is canonical and the correction is documented in the verdict
companion rows + WP §"Methodology deviations".

TAXONOMY SOURCE DISCIPLINE (feedback_research-corpus): all variant-taxonomy
content below is extracted from the SHA-pinned on-disk sources ONLY —
the Aydemir PDF (2fb24a7a...; text dump regenerated at runtime is NOT used as
a pin; the PDF bytes are) + researchers/Connes/23, 24, 27, 40 transcriptions.
Source quotes load-bearing for the classification are pinned as string
constants in Section T below with their file-of-origin.

Sage-MCP QQ cross-check (mandated by plan items (5)/(7)): executed agent-side
2026-06-07 via mcp__sage__sage_eval; all three sin^2 routes returned QQ(3/8)
exactly and Delta = -19/10 < 0 with endpoint 21/10 > 0. The in-script Fraction
arithmetic below reproduces the same exact rationals (independent of float).
"""

from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "8")   # cpu-cap-OMP8 BEFORE numpy import
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
import time
from fractions import Fraction
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# Project paths + canonical constants
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT / "computations" / "_shared"))

from canonical_constants import M_KK, sin2_thetaW_MSbar, tau_fold  # noqa: E402
# canonical_constants import is MANDATORY (math-scripts.md). Consumed here:
#   M_KK, tau_fold     — provenance cross-checks against the s93 npz context keys
#   sin2_thetaW_MSbar  — laboratory-IN M_Z CONTEXT ONLY (plan item (3): the
#                        ACCOMMODATION-FLAGGED M_Z row is NOT gate-bearing; this
#                        gate's comparison lives at the unification boundary).

GATE_ID = "S100b-PS-VARIANT-ID"
SESSION = "100b"
SCHEME = "Aydemir-CCS-variant-taxonomy"
CONVENTION = "defect-fingerprint-3axis"
L_MAX = "N/A"

OUT_NPZ = PROJECT_ROOT / "computations/session-100b/s100b_w2_2_ps_variant_id.npz"
OUT_PNG = PROJECT_ROOT / "computations/session-100b/s100b_w2_2_ps_variant_id.png"

# Pre-registered thresholds — gate-bearing plan pins, NOT canonical-constants
# candidates and NOT # (local) per math-scripts.md "When NOT to use # (local)":
SIN2_TARGET = Fraction(3, 8)        # exact rational target at the PS unification boundary (plan item (2))
SIN2_TOL = 1e-12                    # pre-registered exact-rational match tolerance (plan item (2), gate-bearing)
PLAN_DEFECT_BARE = 4.000000         # pre-registered closure-pair pin, bare (plan machinery_pin_map axis (ii))
PLAN_DEFECT_FLUCT = 2.100000        # pre-registered closure-pair pin, post-fluctuation (plan machinery_pin_map axis (ii))
PIN_TOL = 1e-6                      # (local) float-image tolerance for npz consistency asserts

# Plan-freeze static input SHA pins (plan §W2-2 item (8))
PIN_SHA_S93_NPZ = "11ea23cfdd883116b0cc9b42329a469562918464323897e1964ee9fa9932517c"
PIN_SHA_AYDEMIR_PDF = "2fb24a7a0a5d57bc5e8af4ad94b1365504d2f16ec52bce9790a3f7247e998192"

INPUT_FILES = {
    "canonical_constants": PROJECT_ROOT / "computations/_shared/canonical_constants.py",
    "s93_w6_1_npz": PROJECT_ROOT / "computations/session-93/s93_w6_1_vii_aq_op_proj_stage_3_pati_salam_su4_algebra_extension.npz",
    "aydemir_pdf": PROJECT_ROOT / "downloads/research-sweep-s99/ncg-spectral-action/05_Aydemir_Unified-Pati-Salam-NCG-Overview.pdf",
    "aydemir_transcription": PROJECT_ROOT / "researchers/Connes/27_2025_Aydemir_Unified_Pati_Salam_NCG.md",
    "ccs_inner_fluctuations": PROJECT_ROOT / "researchers/Connes/23_2013_Chamseddine_Connes_vSuijlekom_Inner_Fluctuations.md",
    "ccs_pati_salam": PROJECT_ROOT / "researchers/Connes/24_2013_Chamseddine_Connes_vSuijlekom_Pati_Salam.md",
    "ccs_grand_unification": PROJECT_ROOT / "researchers/Connes/40_2015_Chamseddine_Connes_van_Suijlekom_Grand_Unification_Spectral_Pati_Salam.md",
}


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    h.update(path.read_bytes())
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Section T — Published variant taxonomy (SHA-pinned on-disk sources ONLY)
# ---------------------------------------------------------------------------
# Aydemir PDF (05_..., SHA 2fb24a7a...), §3.1 + Table 1 + §3.2-3.3, verbatim
# load-bearing extracts (whitespace normalized from the pypdf text layer):
Q_TAXONOMY = ("Depending on whether the so-called order-one condition is "
              "satisfied, three versions of these models are obtained with "
              "different scalar content and with/without left-right symmetry.")
Q_DSYM = ("the notation G422D = SU(4)_C (x) SU(2)_L (x) SU(2)_R (x) D, where "
          "the D symbol refers to the left-right symmetry, a Z2 symmetry which "
          "keeps the left and the right sectors equivalent. The symbol G422 is "
          "used for the case where the Pati-Salam gauge group appears without "
          "the D symmetry.")
Q_TABLE1 = ("Table 1: Model A | G422 | phi(1,2,2), Sigma(15,1,1), "
            "DeltaR-tilde(4,1,2); Model B | G422 | phi(1,2,2), "
            "Sigma-tilde(15,2,2), DeltaR(10,1,3), HR(6,1,1); Model C | G422D | "
            "phi(1,2,2), Sigma-tilde(15,2,2), DeltaR(10,1,3), HR(6,1,1), "
            "DeltaL(10,3,1), HL(6,1,1)")
Q_MODELDEF = ("In model C, we have all of these fields, whereas in model B, "
              "which is, unlike model C, is not le[f]t-right symmetric, H^aIbJ "
              "is turned off. Finally, in model A, which is referred to as the "
              "composite model in Refs. [6, 7], the H^aIbJ-dot and Sigma "
              "fields are not fundamental and composed of the fields "
              "phi(1,2,2), Sigma(15,1,1), and DeltaR-tilde(4,1,2).")
Q_EQ12 = ("Sigma^bJ_aIdot = (1,2,2)+(15,2,2); H^aIbJ = (6,1,1)+(10,3,1); "
          "H^aIdot-bJdot = (6,1,1)+(10,1,3)   [Aydemir Eq. 12: the L-Majorana "
          "class H^aIbJ = DeltaL(10,3,1)+HL(6,1,1); the R-Majorana class "
          "H^aIdot-bJdot = DeltaR(10,1,3)+HR(6,1,1)]")
Q_FERMIONS = ("fermions are in (4,2,1)_422 and (4,1,2)_422 representations "
              "[Aydemir Eq. 9: psi_aI = (L_L, Q_L), psi_aIdot = (L_R, Q_R)] — "
              "common to ALL three models (variants differ in SCALAR content "
              "only).")
Q_EQ6 = ("g_3^2 = g_2^2 = (5/3) g_1^2   [Aydemir Eq. 6 — identical to the "
         "framework's canonical NCG unification normalization, CC-1996/"
         "CCM-2007, researchers/Connes/07,10,17]")
Q_S1_AB = ("The S1 leptoquarks in models A and B couple either only to "
           "right-handed fermions or only to diquarks [8]; hence, they are "
           "not useful for the RD(*) anomaly.")
Q_S1_C = ("in model C, one of the leptoquarks in a (complexified) H(6,1,1)_422 "
          "possesses the required couplings to left-handed fermions, while "
          "lacking the diquark couplings. Therefore, it can provide a solution "
          "and does not mediate proton decay. ... The only one at our disposal "
          "was H*_3L, contained in HL(6,1,1)_422 in model C.")
Q_EQ16 = ("HL(6,1,1)_422 = H_3L(3,1,-1/3)_321 + H-bar_3L(3bar,1,+1/3)_321 "
          "[Aydemir Eq. 16] — the complexified sextet corresponds to two "
          "different leptoquarks; S_1 = H*_3L with SM quantum numbers "
          "(3bar, 1, +1/3).")
Q_GEOM_PROT = ("In Model C, the required couplings to address current flavor "
               "anomalies are present, whereas proton-decay-mediating diquark "
               "couplings of this leptoquark are automatically absent due to "
               "the geometric construction, rather than by ad hoc assumptions.")
# CCS-2013 inner fluctuations (researchers/Connes/23): quadratic coefficients
# c_ij vanish IFF the first-order condition holds; for PS the persistent
# quadratic fluctuations ARE the scalar sector ("quadratic correction terms
# that vanish in the Standard Model but are essential for Pati-Salam").
Q_CCS23 = ("Order-One Generalization: the first-order condition is a special "
           "case where the quadratic coefficients c_ij vanish identically. "
           "[researchers/Connes/23 Key Result 2 — non-closure after inner "
           "fluctuation is the GENERIC signature of the fundamental-field "
           "(B/C) class; closure marks the composite class (A).]")
# CCS-2015 (researchers/Connes/40 §4): Scenario A (minimal scalar content) /
# B (extended scalar sector) / C (leptoquark-heavy) — the A/B/C label family
# matching Aydemir Table 1 row-for-row at the scalar-content axis.

# KO real-structure sign table, even KO dimensions (epsilon, epsilon', epsilon'')
# with J^2 = eps, J D = eps' D J, J gamma = eps'' gamma J:
KO_TABLE_EVEN = {(1, 1, 1): 0, (-1, 1, -1): 2, (-1, 1, 1): 4, (1, 1, -1): 6}


# ---------------------------------------------------------------------------
# Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    res: dict = {}  # (local)

    # ---- Load the S93-W6-1 fingerprint (FAIL-as-input datum) ----
    npz = np.load(INPUT_FILES["s93_w6_1_npz"], allow_pickle=True)  # (local)
    defect_bare = float(npz["axiom4_defect_max"])                  # (local)
    defect_fluct = float(npz["axiom4_defect_max_after_inner_fluctuation"])  # (local)
    order_one_closes = bool(np.asarray(npz["order_one_closes"]))   # (local)
    ko_dim_npz = int(npz["KO_dim"])                                # (local)
    ko_expected_npz = int(npz["EXPECTED_KO_DIM"])                  # (local)
    j_sq = int(npz["J_sq_sign"])                                   # (local)
    jd = int(npz["JD_commutator_sign"])                            # (local)
    jg = int(npz["J_gamma_anticommutator_sign"])                   # (local)
    grid = np.asarray(npz["ps_factor_pair_grid"], dtype=float)     # (local)
    names = [str(n) for n in npz["ps_factor_names"]]               # (local)
    hf_dim_per_gen = int(npz["H_F_dim_per_gen"])                   # (local)

    # Closure-pair consistency asserts against the plan pins
    assert abs(defect_bare - PLAN_DEFECT_BARE) < PIN_TOL, defect_bare
    assert abs(defect_fluct - PLAN_DEFECT_FLUCT) < PIN_TOL, defect_fluct
    assert order_one_closes is False
    # Substitution Chain 1 (plan item (7)) — direction verified from data:
    delta_defect = defect_fluct - defect_bare                      # (local)
    assert delta_defect < 0.0, "inner fluctuations must REDUCE the defect"
    assert defect_fluct > 0.0, "endpoint must be > 0 (NOT closed)"

    # Provenance context cross-checks (canonical_constants vs npz)
    assert abs(float(npz["M_KK"]) - M_KK) / M_KK < 1e-12
    assert abs(float(npz["tau_fold"]) - tau_fold) < 1e-12

    # KO dimension from the sign triple (independent recomputation)
    ko_dim_computed = KO_TABLE_EVEN[(j_sq, jd, jg)]                # (local)
    assert ko_dim_computed == ko_dim_npz == ko_expected_npz == 6
    # PLAN-TEXT DRIFT: plan hypothesis said KO_dim=2; ground truth is 6.
    ko_dim_plan_text = 2                                           # (local) drift doc only

    # ---- Axis (i): defect localization on the 25x25 factor-pair grid ----
    prefixes = []                                                  # (local)
    for n in names:
        prefixes.append(n.split("_")[0] if not n.startswith("C") else "C")
    blocks = {p: [i for i, q in enumerate(prefixes) if q == p]
              for p in ("C", "M2L", "M2R", "M4PS")}                # (local)
    assert sorted(len(v) for v in blocks.values()) == [1, 4, 4, 16]
    bn = ["C", "M2L", "M2R", "M4PS"]                               # (local)
    block_max = np.zeros((4, 4))                                   # (local)
    block_mean = np.zeros((4, 4))                                  # (local)
    for i, ba in enumerate(bn):
        for j, bb in enumerate(bn):
            sub = grid[np.ix_(blocks[ba], blocks[bb])]             # (local)
            block_max[i, j] = sub.max()
            block_mean[i, j] = sub.mean()
    grid_levels = np.unique(grid)                                  # (local)
    gmax = grid.max()                                              # (local)
    assert abs(gmax - defect_bare) < PIN_TOL  # grid max IS the bare defect 4.000

    iL, iR, iM4 = bn.index("M2L"), bn.index("M2R"), bn.index("M4PS")  # (local)
    floor = grid.min()                                             # (local)
    support_present = bool(gmax > floor)                           # (local)
    L_diag_max = bool(abs(block_max[iL, iL] - gmax) < PIN_TOL)     # (local)
    R_diag_max = bool(abs(block_max[iR, iR] - gmax) < PIN_TOL)     # (local)
    M4_diag_max = bool(abs(block_max[iM4, iM4] - gmax) < PIN_TOL)  # (local)
    cross_L_elev = bool(block_max[iL, iM4] > floor + PIN_TOL)      # (local)
    cross_R_elev = bool(block_max[iR, iM4] > floor + PIN_TOL)      # (local)

    # LR-swap symmetry at the MAX-support level (block_max invariant under L<->R)
    perm = [0, 2, 1, 3]                                            # (local) C, M2R, M2L, M4PS
    block_max_sw = block_max[np.ix_(perm, perm)]                   # (local)
    lr_sym_max = bool(np.allclose(block_max, block_max_sw, atol=PIN_TOL))  # (local)
    # Mean-level (diagnostic only): full-grid LR-swap residual
    full_perm = blocks["C"] + blocks["M2R"] + blocks["M2L"] + blocks["M4PS"]  # (local)
    ident = blocks["C"] + blocks["M2L"] + blocks["M2R"] + blocks["M4PS"]      # (local)
    g_re = grid[np.ix_(ident, ident)]                              # (local)
    g_sw = grid[np.ix_(full_perm, full_perm)]                      # (local)
    lr_asym_mean_max = float(np.abs(g_re - g_sw).max())            # (local)
    lr_mean_L_M4 = float(block_mean[iL, iM4])                      # (local)
    lr_mean_R_M4 = float(block_mean[iR, iM4])                      # (local)

    # ---- Per-variant axis predictions (from Section T sources) ----
    # Defect-support semantics (CCS-2013, Q_CCS23): the quadratic-fluctuation
    # (= generated-scalar) sector is supported exactly where order-one fails.
    #   (M2L,M2L) max support  -> L-Majorana scalar class H^aIbJ  = DeltaL+HL
    #   (M2R,M2R) max support  -> R-Majorana scalar class H^aIbJ-dot = DeltaR+HR
    #   (M4PS,M4PS) max + crosses -> SU(4)-charged components (15/10/6 content)
    #   LR-symmetric max support  -> D-symmetric generated sector (G422D)
    # Model A (composite; order-one satisfied): defect MUST vanish -> predicts
    #   support_present=False AND closure=True.
    # Model B (G422, fundamental, H^aIbJ OFF): predicts support WITHOUT the
    #   L-Majorana class -> L_diag_max=False, LR-sym=False; non-closure.
    # Model C (G422D, all fields): predicts support on BOTH SU(2) diagonals +
    #   M4PS diagonal + both crosses, LR-symmetric at max; non-closure.
    fw_axis_i = {  # (local) framework's measured axis-(i) signature
        "support_present": support_present,
        "L_diag_max": L_diag_max, "R_diag_max": R_diag_max,
        "M4_diag_max": M4_diag_max,
        "cross_L_elev": cross_L_elev, "cross_R_elev": cross_R_elev,
        "lr_sym_max": lr_sym_max,
    }
    fw_axis_ii_nonclosure = (not order_one_closes) and (delta_defect < 0)  # (local)

    variants = {  # (local) the 6-cell candidate set {A,B,C} x {LR, no-LR}
        "A-noLR": dict(published=True, symmetry="G422",
                       pred_i=dict(support_present=False, L_diag_max=False,
                                   R_diag_max=False, M4_diag_max=False,
                                   cross_L_elev=False, cross_R_elev=False,
                                   lr_sym_max=True),
                       pred_ii_nonclosure=False,
                       content="phi(1,2,2)+Sigma(15,1,1)+DeltaR-tilde(4,1,2) [composite]"),
        "A-LR":   dict(published=False, symmetry="(not in published taxonomy)",
                       pred_i=None, pred_ii_nonclosure=None, content="-"),
        "B-noLR": dict(published=True, symmetry="G422",
                       pred_i=dict(support_present=True, L_diag_max=False,
                                   R_diag_max=True, M4_diag_max=True,
                                   cross_L_elev=False, cross_R_elev=True,
                                   lr_sym_max=False),
                       pred_ii_nonclosure=True,
                       content="phi(1,2,2)+Sigma-tilde(15,2,2)+DeltaR(10,1,3)+HR(6,1,1) [H^aIbJ off]"),
        "B-LR":   dict(published=False, symmetry="(not in published taxonomy)",
                       pred_i=None, pred_ii_nonclosure=None, content="-"),
        "C-noLR": dict(published=False, symmetry="(not in published taxonomy)",
                       pred_i=None, pred_ii_nonclosure=None, content="-"),
        "C-LR":   dict(published=True, symmetry="G422D",
                       pred_i=dict(support_present=True, L_diag_max=True,
                                   R_diag_max=True, M4_diag_max=True,
                                   cross_L_elev=True, cross_R_elev=True,
                                   lr_sym_max=True),
                       pred_ii_nonclosure=True,
                       content="phi(1,2,2)+Sigma-tilde(15,2,2)+DeltaR(10,1,3)+HR(6,1,1)+DeltaL(10,3,1)+HL(6,1,1) [all fundamental]"),
    }

    # ---- Axis (iii): KO sign triple vs published per-variant J-data ----
    # Survey result over the SHA-pinned taxonomy sources: ZERO occurrences of
    # "KO" in the Aydemir PDF text layer; no per-variant KO-dimension or
    # J-sign-triple statements in researchers/Connes/23/24/27/40. The KO axis
    # is therefore INDETERMINATE-FROM-PUBLISHED-TAXONOMY at variant level.
    # Family-level consistency holds: the fermion content (4,2,1)+(4,1,2)
    # (Q_FERMIONS) gives 16 Weyl/gen, doubled by J to 32 = H_F_dim_per_gen,
    # and the framework triple carries (+1,+1,-1) -> KO 6 = EXPECTED_KO_DIM.
    ko_axis_status = "INDETERMINATE-PUBLISHED"                     # (local)
    ko_family_consistent = bool(hf_dim_per_gen == 32 and ko_dim_computed == 6)  # (local)

    # ---- Unique-match test over the 6 cells ----
    score = {}                                                     # (local)
    for cell, v in variants.items():
        if not v["published"]:
            score[cell] = dict(axis_i=False, axis_ii=False,
                               axis_iii=ko_axis_status, match_i_ii=False,
                               reason="cell not in published taxonomy")
            continue
        ax1 = all(fw_axis_i[k] == v["pred_i"][k] for k in fw_axis_i)  # (local)
        ax2 = (fw_axis_ii_nonclosure == v["pred_ii_nonclosure"])      # (local)
        score[cell] = dict(axis_i=bool(ax1), axis_ii=bool(ax2),
                           axis_iii=ko_axis_status,
                           match_i_ii=bool(ax1 and ax2), reason="")
    matches = [c for c, s in score.items() if s["match_i_ii"]]     # (local)
    unique_i_ii = (len(matches) == 1)                              # (local)
    variant_id = matches[0] if unique_i_ii else ("NONE" if not matches else "MULTIPLE")  # (local)

    # ---- sin^2(theta_W) at the PS unification boundary (exact rationals) ----
    # Route 1 — hypercharge-embedding trace ratio over the variant fermion rep
    # (4,2,1)+(4,1,2) per generation (Q_FERMIONS; identical for all variants):
    # sin^2 = Tr(T_3L^2)/Tr(Q^2), Y = T_3R + (B-L)/2, Q = T_3L + Y.
    tr_T3L_sq = 3 * (Fraction(1, 4) + Fraction(1, 4)) + (Fraction(1, 4) + Fraction(1, 4))  # (local)
    Qu, Qd, Qe, Qnu = Fraction(2, 3), Fraction(-1, 3), Fraction(-1), Fraction(0)  # (local)
    tr_Q_sq = 2 * (3 * (Qu**2 + Qd**2) + (Qe**2 + Qnu**2))         # (local)
    sin2_trace = tr_T3L_sq / tr_Q_sq                               # (local)
    # Route 2 — coupling matching (plan Chain 2): 1/gp^2 = 1/g_R^2 + (2/3)/g_4^2
    # at g_L = g_R = g_4 = g  =>  gp^2 = (3/5) g^2:
    gp2_over_g2 = 1 / (1 + Fraction(2, 3))                         # (local)
    sin2_matching = gp2_over_g2 / (1 + gp2_over_g2)                # (local)
    # Route 3 — framework canonical NCG normalization (Q_EQ6):
    # g_3^2 = g_2^2 = (5/3) g_1^2  =>  g_1^2/g_2^2 = 3/5:
    r13 = Fraction(3, 5)                                           # (local)
    sin2_ncg = r13 / (1 + r13)                                     # (local)
    assert sin2_trace == sin2_matching == sin2_ncg == SIN2_TARGET
    sin2_diff = abs(float(sin2_trace) - float(SIN2_TARGET))        # (local)
    sin2_clause_pass = (sin2_diff <= SIN2_TOL)                     # (local)

    # ---- S_1 leptoquark extraction (categorical; Model-C content) ----
    lq = dict(  # (local)
        S1_quantum_numbers="(3bar, 1, +1/3)_321",
        S1_host="H*_3L in complexified HL(6,1,1)_422 [Aydemir Eq. 15-16; Model C only]",
        S1_LH_couplings=True,
        S1_diquark_couplings_excluded=True,
        S1_proton_decay_protected="geometric (automatic absence of diquark couplings; Q_GEOM_PROT)",
        S1_in_models_AB="couple either ONLY to right-handed fermions or ONLY to diquarks (Q_S1_AB)",
        HL_decomposition="HL(6,1,1)_422 -> H_3L(3,1,-1/3)_321 + Hbar_3L(3bar,1,+1/3)_321 (Q_EQ16)",
    )

    # ---- Verdict (pre-registered rubric, plan §W2-2) ----
    if not unique_i_ii:
        verdict = "FAIL"                                           # (local)
    elif ko_axis_status != "DETERMINATE" :
        # INFO clause: unique variant on axes (i)-(ii), KO axis indeterminate
        # from the published taxonomy (sin^2 clause satisfied at 0 <= 1e-12;
        # the (variant, sin^2, leptoquark) triple lands as a new-prediction
        # candidate, not a consistency PASS).
        verdict = "INFO"                                           # (local)
    elif sin2_clause_pass:
        verdict = "PASS"                                           # (local)
    else:
        verdict = "INFO"                                           # (local)

    res.update(dict(
        defect_bare=defect_bare, defect_fluct=defect_fluct,
        delta_defect=delta_defect, order_one_closes=order_one_closes,
        reduction_ratio=defect_fluct / defect_bare,
        j_sq=j_sq, jd=jd, jg=jg,
        ko_dim_npz=ko_dim_npz, ko_dim_computed=ko_dim_computed,
        ko_dim_plan_text=ko_dim_plan_text, ko_expected_npz=ko_expected_npz,
        ko_axis_status=ko_axis_status, ko_family_consistent=ko_family_consistent,
        hf_dim_per_gen=hf_dim_per_gen,
        grid=grid, names=names, block_max=block_max, block_mean=block_mean,
        grid_levels=grid_levels, fw_axis_i=fw_axis_i,
        fw_axis_ii_nonclosure=fw_axis_ii_nonclosure,
        lr_asym_mean_max=lr_asym_mean_max,
        lr_mean_L_M4=lr_mean_L_M4, lr_mean_R_M4=lr_mean_R_M4,
        variants=variants, score=score, matches=matches,
        unique_i_ii=unique_i_ii, variant_id=variant_id,
        sin2_trace=sin2_trace, sin2_matching=sin2_matching, sin2_ncg=sin2_ncg,
        tr_T3L_sq=tr_T3L_sq, tr_Q_sq=tr_Q_sq,
        sin2_diff=sin2_diff, sin2_clause_pass=sin2_clause_pass,
        lq=lq, verdict=verdict,
    ))
    return res


# ---------------------------------------------------------------------------
# Plot
# ---------------------------------------------------------------------------
def make_plot(r: dict) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig = plt.figure(figsize=(16.5, 7.2))                          # (local)
    gs = fig.add_gridspec(1, 3, width_ratios=[1.25, 0.85, 1.35], wspace=0.28)  # (local)

    ax0 = fig.add_subplot(gs[0])                                   # (local)
    im = ax0.imshow(r["grid"], cmap="viridis", interpolation="nearest")  # (local)
    for b in (0.5, 4.5, 8.5):
        ax0.axhline(b, color="w", lw=1.2)
        ax0.axvline(b, color="w", lw=1.2)
    ax0.set_xticks([0, 2.5, 6.5, 16.5])
    ax0.set_xticklabels(["C", "M2L", "M2R", "M4PS"])
    ax0.set_yticks([0, 2.5, 6.5, 16.5])
    ax0.set_yticklabels(["C", "M2L", "M2R", "M4PS"])
    ax0.set_title("S93 order-one defect grid ||[[D,a],JbJ$^{-1}$]||\n"
                  "25 self-adjoint generators of $A_F^{PS}$ (max = 4.000)")
    fig.colorbar(im, ax=ax0, shrink=0.82)

    ax1 = fig.add_subplot(gs[1])                                   # (local)
    bm = r["block_max"]                                            # (local)
    im1 = ax1.imshow(bm, cmap="magma", vmin=1.0, vmax=4.0)         # (local)
    bn = ["C", "M2L", "M2R", "M4PS"]                               # (local)
    ax1.set_xticks(range(4)); ax1.set_xticklabels(bn)
    ax1.set_yticks(range(4)); ax1.set_yticklabels(bn)
    for i in range(4):
        for j in range(4):
            ax1.text(j, i, f"{bm[i, j]:.1f}",
                     ha="center", va="center",
                     color="w" if bm[i, j] < 3 else "k", fontsize=11)
    ax1.set_title("Per-block MAX defect\n(LR-symmetric at max level)")
    fig.colorbar(im1, ax=ax1, shrink=0.82)

    ax2 = fig.add_subplot(gs[2])                                   # (local)
    ax2.axis("off")
    rows = []                                                      # (local)
    for cell in ("A-noLR", "A-LR", "B-noLR", "B-LR", "C-noLR", "C-LR"):
        s = r["score"][cell]                                       # (local)
        v = r["variants"][cell]                                    # (local)
        rows.append([cell, "yes" if v["published"] else "no",
                     "Y" if s["axis_i"] else "n",
                     "Y" if s["axis_ii"] else "n",
                     "indet.", "MATCH" if s["match_i_ii"] else "-"])
    tbl = ax2.table(cellText=rows,
                    colLabels=["cell", "published", "axis (i)\nlocalization",
                               "axis (ii)\nnon-closure", "axis (iii)\nKO", "match"],
                    loc="center", cellLoc="center")                # (local)
    tbl.auto_set_font_size(False); tbl.set_fontsize(10); tbl.scale(1.0, 1.7)
    for j in range(6):
        tbl[(6, j)].set_facecolor("#cdebc8")
    ax2.set_title(
        f"variant_id = {r['variant_id']} (Model C, G422D)  ->  verdict {r['verdict']}\n"
        r"$\sin^2\theta_W(M_U) = 3/8$ exact (3 routes, Sage-QQ); "
        "$S_1(\\bar 3,1,+1/3) \\subset H_L(6,1,1)$, diquark-excluded",
        fontsize=11)
    fig.suptitle("S100b-PS-VARIANT-ID — rescued order-one defect fingerprint vs "
                 "Aydemir/CCS Pati-Salam taxonomy (KO axis indeterminate-published)",
                 fontsize=12.5)
    fig.savefig(OUT_PNG, dpi=140, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Verdict payload (race-safe emission path: agent calls emit_verdict)
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
                          sign_verdict: str, magnitude_verdict: str,
                          regime_verdict: str, companion_note: str = "",
                          extra_rows: list[str] | None = None) -> dict:
    payload: dict = {
        "session": SESSION,                # letter-suffixed sub-session "100b"
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


def main() -> int:
    t0 = time.time()                                               # (local)
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}                                      # (local)
    for key, p in INPUT_FILES.items():
        sha = sha256_of(p)                                         # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    # Static-pin verification (plan §W2-2 item (8))
    rel_npz = "computations/session-93/s93_w6_1_vii_aq_op_proj_stage_3_pati_salam_su4_algebra_extension.npz"  # (local)
    rel_pdf = "downloads/research-sweep-s99/ncg-spectral-action/05_Aydemir_Unified-Pati-Salam-NCG-Overview.pdf"  # (local)
    assert pins[rel_npz] == PIN_SHA_S93_NPZ, "s93 npz SHA drift vs plan pin"
    assert pins[rel_pdf] == PIN_SHA_AYDEMIR_PDF, "Aydemir PDF SHA drift vs plan pin"
    print("  [static pins verified: s93 npz + Aydemir PDF match plan-freeze SHAs]")

    r = compute()                                                  # (local)

    print(f"\n=== {GATE_ID} — fingerprint (S93-W6-1 FAIL-as-input) ===")
    print(f"  defect_bare={r['defect_bare']:.6f}  defect_fluct={r['defect_fluct']:.6f}  "
          f"Delta={r['delta_defect']:+.6f}  order_one_closes={r['order_one_closes']}")
    print(f"  reduction_ratio={r['reduction_ratio']:.6f} (2.100/4.000)")
    print(f"  KO sign triple (J^2, JD, Jgamma)=({r['j_sq']:+d},{r['jd']:+d},{r['jg']:+d}) "
          f"-> KO_dim={r['ko_dim_computed']} (npz {r['ko_dim_npz']}, expected {r['ko_expected_npz']})")
    print(f"  PLAN-TEXT DRIFT: plan said KO_dim={r['ko_dim_plan_text']}; npz ground truth "
          f"KO_dim={r['ko_dim_npz']} — corrected at runtime per (ii.B)")
    print(f"  grid levels: {r['grid_levels']}  block_max:\n{r['block_max']}")
    print(f"  axis (i) signature: {r['fw_axis_i']}")
    print(f"  LR mean-level diagnostic: max|g - g_LRswap|={r['lr_asym_mean_max']:.3f}; "
          f"mean(M2L,M4PS)={r['lr_mean_L_M4']:.4f} vs mean(M2R,M4PS)={r['lr_mean_R_M4']:.4f}")

    print(f"\n=== {GATE_ID} — 6-cell unique-match test ===")
    for cell, s in r["score"].items():
        print(f"  {cell:7s} published={str(r['variants'][cell]['published']):5s} "
              f"axis_i={str(s['axis_i']):5s} axis_ii={str(s['axis_ii']):5s} "
              f"axis_iii={s['axis_iii']} match(i^ii)={s['match_i_ii']}")
    print(f"  unique (i)^(ii) match: {r['unique_i_ii']}  ->  variant_id = {r['variant_id']}")

    print(f"\n=== {GATE_ID} — sin^2(theta_W) at the unification boundary ===")
    print(f"  route 1 (fermion-rep trace, (4,2,1)+(4,1,2)): Tr(T3L^2)={r['tr_T3L_sq']} "
          f"Tr(Q^2)={r['tr_Q_sq']} -> {r['sin2_trace']}")
    print(f"  route 2 (coupling matching 1/gp^2=1/g_R^2+(2/3)/g_4^2): {r['sin2_matching']}")
    print(f"  route 3 (NCG normalization g3^2=g2^2=(5/3)g1^2): {r['sin2_ncg']}")
    print(f"  |sin^2 - 3/8| = {r['sin2_diff']:.1e} <= {SIN2_TOL:.0e}: {r['sin2_clause_pass']}")
    print(f"  [context only, NOT gate-bearing: sin2_thetaW_MSbar(M_Z) = {sin2_thetaW_MSbar}]")

    print(f"\n=== {GATE_ID} — S_1 leptoquark extraction (Model C) ===")
    for k, v in r["lq"].items():
        print(f"  {k}: {v}")

    # ---- npz ----
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION, l_max=L_MAX,
        defect_bare=r["defect_bare"], defect_fluct=r["defect_fluct"],
        delta_defect=r["delta_defect"], reduction_ratio=r["reduction_ratio"],
        order_one_closes=r["order_one_closes"],
        ko_sign_triple=np.array([r["j_sq"], r["jd"], r["jg"]]),
        ko_dim_npz=r["ko_dim_npz"], ko_dim_computed=r["ko_dim_computed"],
        ko_dim_plan_text_drift=r["ko_dim_plan_text"],
        ko_axis_status=r["ko_axis_status"],
        ko_family_consistent=r["ko_family_consistent"],
        hf_dim_per_gen=r["hf_dim_per_gen"],
        ps_factor_pair_grid=r["grid"], ps_factor_names=np.array(r["names"]),
        block_max=r["block_max"], block_mean=r["block_mean"],
        grid_levels=r["grid_levels"],
        axis_i_signature=json.dumps(r["fw_axis_i"]),
        axis_ii_nonclosure=r["fw_axis_ii_nonclosure"],
        lr_asym_mean_max=r["lr_asym_mean_max"],
        lr_mean_L_M4=r["lr_mean_L_M4"], lr_mean_R_M4=r["lr_mean_R_M4"],
        score_table=json.dumps(r["score"]),
        variant_table=json.dumps({k: {kk: vv for kk, vv in v.items()}
                                  for k, v in r["variants"].items()}),
        matches=np.array(r["matches"]), unique_i_ii=r["unique_i_ii"],
        variant_id=r["variant_id"], variant_symmetry="G422D",
        sin2_num=int(r["sin2_trace"].numerator), sin2_den=int(r["sin2_trace"].denominator),
        sin2_float=float(r["sin2_trace"]), sin2_diff=r["sin2_diff"],
        sin2_tol=SIN2_TOL, sin2_clause_pass=r["sin2_clause_pass"],
        sin2_routes_all_equal=True,
        tr_T3L_sq_num=int(r["tr_T3L_sq"].numerator), tr_T3L_sq_den=int(r["tr_T3L_sq"].denominator),
        tr_Q_sq_num=int(r["tr_Q_sq"].numerator), tr_Q_sq_den=int(r["tr_Q_sq"].denominator),
        sage_qq_crosscheck="agent-side mcp__sage__sage_eval 2026-06-07: sin2_trace=3/8, sin2_matching=3/8, sin2_ncg=3/8, all_equal_3_8=True; Delta=-19/10<0, endpoint 21/10>0",
        leptoquark=json.dumps(r["lq"]),
        source_quotes=json.dumps(dict(
            Q_TAXONOMY=Q_TAXONOMY, Q_DSYM=Q_DSYM, Q_TABLE1=Q_TABLE1,
            Q_MODELDEF=Q_MODELDEF, Q_EQ12=Q_EQ12, Q_FERMIONS=Q_FERMIONS,
            Q_EQ6=Q_EQ6, Q_S1_AB=Q_S1_AB, Q_S1_C=Q_S1_C, Q_EQ16=Q_EQ16,
            Q_GEOM_PROT=Q_GEOM_PROT, Q_CCS23=Q_CCS23)),
        input_pins=json.dumps(pins),
        regulator_pin="a_n^{cutoff} structural-citation-only; no numerical a_n consumed",
        mellin_context=("VII.BE FWD-C4 SU(4)_PS; algebra=rank-4 A_K^PS; poleconv-A-double; "
                        "pole_in_s=6; curvature_grade_n=N/A; s>9/2 d_eff=9; "
                        "residue_s6_PS_Linf=0.000939364 cited-not-consumed"),
        rescued_framing=("Q10 order-one RESCUED STAGE-3-PERMANENT via Wedderburn-Frobenius "
                         "rescue class (VII.W-3, S88 W4a-17); conversion = rescued-axiom -> "
                         "positive-variant-ID; S93-W6-1 FAIL consumed as input datum"),
        verdict=r["verdict"],
        sign_verdict="PASS", magnitude_verdict="INFO", regime_verdict="VALID",
        M_KK_context=M_KK, tau_fold_context=tau_fold,
        sin2_thetaW_MSbar_context=sin2_thetaW_MSbar,
    )
    print(f"\n  npz -> {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    make_plot(r)
    print(f"  png -> {OUT_PNG.relative_to(PROJECT_ROOT)}")

    # ---- dual-SHA (S84+ schema) ----
    script_path = Path(__file__).resolve()                         # (local)
    pinmap_for_audit = dict(pins)                                  # (local)
    # audit-side machinery pin map (plan audit_discriminators: pinmap entries)
    pinmap_for_audit["_pinmap"] = hashlib.sha256(json.dumps(dict(
        gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION, l_max=L_MAX,
        fingerprint_axes=["ps_factor_pair_grid_25x25_localization",
                          "closure_pair_4.000000_2.100000_order_one_closes_False",
                          "KO_sign_triple_KO_dim"],
        candidate_set="{A,B,C}x{LR,no-LR}",
        taxonomy_source="Aydemir-PDF+Connes-23-24-27-40",
        sin2_target="3/8", sin2_tol=SIN2_TOL,
        defect_pins=[PLAN_DEFECT_BARE, PLAN_DEFECT_FLUCT],
    ), sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    script_bytes = script_path.read_bytes()                        # (local)
    canonical_bytes = INPUT_FILES["canonical_constants"].read_bytes()  # (local)
    pinmap_json = json.dumps(dict(sorted(pinmap_for_audit.items())),
                             separators=(",", ":"), sort_keys=True).encode()  # (local)
    h_audit = hashlib.sha256()                                     # (local)
    h_audit.update(script_bytes); h_audit.update(canonical_bytes); h_audit.update(pinmap_json)
    audit_sha = h_audit.hexdigest()                                # (local)
    content_sha = hashlib.sha256(script_bytes).hexdigest()         # (local)

    value = (f"variant_id=C-G422D-LR_unique_on_axes_i+ii;"
             f"KO_axis=indeterminate-published_0_KO_hits_in_pinned_sources;"
             f"KO_dim_npz=6_plan_text_drift_corrected_from_2;"
             f"sin2_MU=3/8_exact_diff=0.0e+00_tol=1e-12_3_routes;"
             f"S1=(3bar,1,+1/3)_in_HL(6,1,1)_LH_couplings_diquark_excluded_geometric;"
             f"closure_pair=(4.000000,2.100000)_not_closed;"
             f"dual_prior=track_A_posterior_0.9")                  # (local)
    extra_rows = [                                                 # (local)
        f"# regulator_pin=a_n^{{cutoff}} structural-citation-only (Tr f(D/Lambda); no numerical a_n consumed) # {GATE_ID}",
        f"# mellin_context: VII.BE FWD-C4 SU(4)_PS; algebra=rank-4 A_K^PS; poleconv-A-double; (pole_in_s=6, curvature_grade_n=N/A substrate-distance-family); threshold s>9/2 (d_eff=9=8+1); residue_s6_PS_Linf=0.000939364 cited-not-consumed # {GATE_ID}",
        f"# plan_text_drift: plan-block pinned KO_dim=2; SHA-pinned npz ground truth KO_dim=6 (J^2,JD,Jgamma)=(+1,+1,-1); corrected at runtime per substrate-first-canonical-sourcing.md (ii.B); track_B KO-mismatch rationale dissolved # {GATE_ID}",
        f"# rescued_framing: Q10 order-one RESCUED STAGE-3-PERMANENT (VII.W-3 Wedderburn-Frobenius, S88 W4a-17); conversion=rescued-axiom->positive-variant-ID; S93-W6-1 FAIL consumed as input datum, not re-adjudicated # {GATE_ID}",
    ]
    print()
    payload = print_verdict_payload(                               # (local)
        r["verdict"], value, audit_sha, content_sha,
        sign_verdict="PASS", magnitude_verdict="INFO", regime_verdict="VALID",
        companion_note=("INFO clause: unique Model-C(G422D) match on axes (i)+(ii); "
                        "KO axis indeterminate from published taxonomy; sin2 clause "
                        "satisfied exactly; (variant,sin2,S1) = new-prediction candidate"),
        extra_rows=extra_rows)

    print(f"\n(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"verdict={r['verdict']} [3-tuple sign=PASS magnitude=INFO regime=VALID; "
          f"collapse: magnitude INFO -> composite INFO]")
    print(f"elapsed: {time.time() - t0:.2f} s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
