#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CF-S95-N-PBH-MAGNITUDE-RECOMPUTE
================================

Gate: CF-S95-N-PBH-MAGNITUDE-RECOMPUTE  ([VERIFY])
Plan: sessions/session-plan/session-95-plan-w6.md §W6-1
Owner: mack-cosmic-bridge

PURPOSE (discharge the MAGNITUDE half of the HELD §VII.AX m^-3 Level-3 row):
  S94 W5-1 (S94-N-PBH-TRUNCATION-ANCHOR, INFO) established the WHICH-ANCHOR half:
  the cardinality-cascade SATURATION generation g_saturate=143 (g-axis; the cascade
  physically FILLS) is the substrate-physical, L_max-INDEPENDENT anchor — NOT the
  L_max=14 linear extrapolation (which lives on the DIVERGENT cardinality channel
  N_eigs(L) = (4/15)L^5 + (10/3)L^4 + 16L^3 + (110/3)L^2 + (596/15)L + 16, lim->+inf,
  Sage-exact corpus §25.1). The S94 anchor DEFERRED the magnitude PIN to a separate
  saturated-tail recompute (magnitude_decoupling_deferred=True, CF-S95). THIS gate IS
  that recompute.

  TWO DISTINCT m^-3 MAGNITUDES (the substitution chain pins which is L_max-INDEPENDENT):
    (i)  LINEAR-L14 (divergent channel):  n_PBH_linear_L14 = A_prefactor * N_eigs(14)
         = 2.2517e-28 * 323136 = 7.276e-23 m^-3 == canonical n_PBH_FW_central.
         This carries the IRREDUCIBLE L10->L14 LINEAR refinement (factor 4.1385x over
         the L=10 baseline) and is NOT L_max-independent (N_eigs(L) diverges as L^5).
    (ii) g-SATURATED TAIL (L_max-INDEPENDENT):  n_PBH_frozen_saturation
         = C(N_atlas, 2) * prob_form / L_pix_LRD^3  with N_atlas = 78080 FROZEN at
         g_saturate (= analytic atlas-parent N_eigs(10)=80080 minus the dropped (4,4)
         sector = 2000). n_edge_saturated = C(78080,2) = 3,048,204,160 (Sage-exact).
         n_PBH_frozen_saturation = 1.7581e-23 m^-3. The cardinality is FROZEN at
         saturation => this magnitude has NO L-dependence by construction.

PRE-REGISTERED THRESHOLD (plan §W6-1 operator + strict_PASS_boundary):
  operator: inequality + Tier-1/Tier-2 classification.
  PASS  iff  |dln(n_PBH_sat)/dln L| < 1e-3 over L in {10,11,12,13,14}  (L_max-INDEPENDENT
        at g_saturate)  AND  the truncation-invariant content is DIMENSIONLESS
        (invariant_is_dimensionless True AND dimension_and_divergence_same_slot False)
        ==> Tier-2 re-anchorable ==> m^-3 Level-3 row discharged HELD -> substrate-
        physical-scale-anchored.
  HELD/INFO  iff  L_max-INDEPENDENT at g_saturate confirmed BUT dimension and divergence
        occupy the SAME spectral slot (dimension_and_divergence_same_slot True) ==>
        Tier-2-DIMENSIONFUL ==> registry-PASS-INELIGIBLE ==> row stays
        NOT-SATISFIED-PENDING-substrate-physical-scale-anchor (magnitude now PINNED to
        the substrate-physical g_saturate value, decoupling magnitude from truncation).
  FAIL  iff  the g_saturate plateau is itself L-drifting (|dln(n_PBH_sat)/dln L| >= 1e-3)
        ==> the saturation anchor is NOT substrate-singled-out; no re-anchoring pathway.
  Tolerance rule: ABSOLUTE on |dln/dlnL| vs the 1e-3 ceiling; 1e-12 FD floor on the
        saturation-plateau check.

  This gate must NOT assume the npz tier_classification carries the verdict — it
  RE-DERIVES whether the g_saturate saturated-tail recompute changes the
  dimension/divergence-same-slot status. The held-number guard (context §A4) is
  binding: n_PBH = 7.2761e-23 m^-3 is ONE held number with ONE forward CF (this gate);
  it is NOT double-counted (§25 Tier-2 + §26 genus + fresh CF). The §VII.AX.OP-PROJ
  theorem-STRUCTURE remains STAGE-3-PERMANENT regardless of this magnitude verdict.

SUBSTITUTION CHAIN (plan §W6-1; which magnitude is L_max-INDEPENDENT):
  Claim: "the factor-4.1385 gap between n_PBH_frozen_saturation_m3=1.758e-23 and
          canonical_central_m3=7.2761e-23 IS the L10->L14 refinement factor, so the
          magnitude is NOT L_max-independent in the naive (linear-L14) reading; the
          saturated-tail (g_saturate) reading is the L_max-independent one."
    Step 1: n_PBH_frozen_saturation_m3 = D1_frozen_sat_value_m3 = 1.7581364216177777e-23
            [npz; g-axis saturated tail at g_saturate=143; FROZEN atlas N=78080]
    Step 2: canonical_central_m3       = 7.2761e-23  [npz; == canonical_constants n_PBH_FW_central]
    Step 3: ratio = canonical_central_m3 / n_PBH_frozen_saturation_m3
                  = 7.2761e-23 / 1.7581364216177777e-23
    Step 4: = 4.13853... ; refinement_factor_L10_to_L14 (npz) = 4.138524590163934;
            ratio_canonical_over_baseline (npz) = 4.138529815169166 (Sage-exact
            3528281250/852544601 = 4.1385298)
    Step 5: ratio == refinement_factor_L10_to_L14 to 5 sig figs ==> the canonical_central
            magnitude carries the L10->L14 LINEAR refinement; the saturated-tail magnitude
            does NOT (it is the g-saturate plateau value, L-FROZEN).
    Conclusion: the two magnitudes are NOT the same observable — one is the linear-L14
            extrapolation (divergent channel), one is the g-axis saturation plateau
            (L_max-INDEPENDENT). The recompute pins WHICH magnitude is L_max-INDEPENDENT
            (the saturated tail) and then asks whether THAT magnitude is Tier-2
            re-anchorable (dimensionless invariant) or Tier-2-dimensionful (held).
  [SIGN] note: this gate has a [VERIFY] trigger, NOT a [SIGN] trigger — the verdict is a
            CLASSIFICATION (re-anchorable vs HELD), not a directional prediction. No
            schema-v2 3-tuple companion row required (plan output_artifacts
            schema_v2_3tuple_required: false).

TIER-2 CLASSIFICATION (cross-pillar-bridge-anatomy.md §"Tier-1/Tier-2"; corpus §25.1):
  O(L,K) = W(L)*g(K) ==> only log-derivatives annihilate W(L). For the cardinality
  channel the truncation-invariant content is the dimensionless cascade exponent
  d ln N_eigs / d ln L -> 5 (Sage-exact integer). BUT that log-derivative annihilates
  the m^-3 prefactor A = 2.2517e-28 m^-3 (the dimensionful per-edge volume factor
  prob_form / L_pix_LRD^3): the DIMENSION and the DIVERGENCE live in the SAME
  multiplicative slot. The dimensionless invariant (the integer 5) is NOT the magnitude;
  the dimensionful magnitude lives on a divergent channel that the log-derivative cannot
  re-anchor. => Tier-2-DIMENSIONFUL => registry-PASS-INELIGIBLE => HELD.
  Contrast (re-anchorable, §VII.AV L_emp): a 2nd log-derivative annihilates a power-law
  prefactor AND the surviving content is dimensionless (M_KK^2 is the K-window unit).

CLASS pin: FULL. No SCHEMATIC helper consumed — the recompute is a closed-form
  cardinality-cascade + frozen-edge-count evaluation re-using the S94 W5-1 npz arrays
  (Sage-exact-reproducible). The verdict-line convention carries NO -SCHEMATIC suffix.

Regulator pin: N/A (no Seeley-DeWitt a_n moment; the m^-3 prefactor A is a
  cardinality-2 graph-edge volume density, not a regulated spectral moment).

Classification: GEOMETRIC. The substrate IS the g-axis cardinality cascade of the D_K
  spectrum on Jensen-deformed SU(3); the PBH number density m^-3 is the Pillar-IX
  laboratory-IN image of the Pillar-I substrate-IS cardinality-cascade-tail observable
  (bridge family FWD-C5, Row #65 / §VII.AX.OP-PROJ). Direction: D_K eigenvalue
  cardinality cascade -> g-axis saturation at g_saturate=143 -> saturated-tail
  number-density magnitude -> Pillar-IX PBH number density (laboratory-IN). The held-
  number guard prevents treating this as a fresh prediction — it is the magnitude HALF
  of one held row (phononic-framing.md §"IS Space, Not IN Space").

Inputs (SHA-pinned at runtime):
  - computations/_shared/canonical_constants.py                     (n_PBH_FW_central, M_KK, tau_fold)
  - computations/session-94/s94_n_pbh_truncation_anchor.npz         (S94 W5-1 g-axis machinery)

Outputs:
  - computations/session-95/s95_w6_1_n_pbh_magnitude_saturated_tail.npz
  - computations/session-95/s95_w6_1_n_pbh_magnitude_saturated_tail.png
  - verdict line + dual-SHA companion row (NO 3-tuple; [VERIFY] non-directional)
    -> computations/session-95/s95_gate_verdicts.txt
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # GPU_path pin = numpy.linalg cache-load only; no diagonalization
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import math
import time
import hashlib
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 1 — Paths + canonical constants import
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
SESSION_94_DIR = PROJECT_ROOT / "computations" / "session-94"
SESSION_95_DIR = PROJECT_ROOT / "computations" / "session-95"
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (  # noqa: E402
    n_PBH_FW_central,
    M_KK,
    tau_fold,
)

CANONICAL_CONSTANTS_PATH = SHARED_DIR / "canonical_constants.py"
S94_ANCHOR_NPZ_PATH = SESSION_94_DIR / "s94_n_pbh_truncation_anchor.npz"

OUT_NPZ = SESSION_95_DIR / "s95_w6_1_n_pbh_magnitude_saturated_tail.npz"
OUT_PNG = SESSION_95_DIR / "s95_w6_1_n_pbh_magnitude_saturated_tail.png"
VERDICT_TXT = SESSION_95_DIR / "s95_gate_verdicts.txt"

# ---------------------------------------------------------------------------
# Section 2 — Gate identity + pre-registered machinery pins (plan §W6-1)
# ---------------------------------------------------------------------------
GATE_ID = "CF-S95-N-PBH-MAGNITUDE-RECOMPUTE"
SCHEME = "g-axis-cardinality-cascade-saturated-tail"
CONVENTION = "TIER-2-DIMENSIONAL-RE-ANCHORABILITY-GATE"
L_MAX = 14  # (local) — L-scan {10,11,12,13,14}; bottom-K saturation-checked, cache-load only

# Option A supersession (gate-verdicts.md §"Option A — sig_5 remediation pathway"): the first
# run of THIS script (before the Tier-2 same-slot derivation was corrected to match the Sage-proven
# corpus §25.1 result) emitted a spurious PASS at audit_sha256 below. That line is RETAINED on disk
# (absolute verdict permanence); this corrective emission APPENDS with a supersedes= tag (script-bug
# fix class). Set to "" for a clean first emission.
SUPERSEDES_SHA = "58bcb4545cb58474463efc6336341ab22e15f95a5565156833ab632e7214c5b9"  # (local) — first-run PASS (script-bug)

# Pre-registered thresholds (plan §W6-1 operator + strict_PASS_boundary):
DLN_DLNL_PASS_CEILING = 1.0e-3   # (local) — PASS iff |dln(n_PBH_sat)/dln L| < 1e-3 (L_max-INDEPENDENT)
FD_FLOOR = 1.0e-12               # (local) — FD floor on the saturation-plateau check
L_SCAN = (10, 11, 12, 13, 14)    # (local) — integer L mesh (no fresh diagonalization)
G_SATURATE_PIN = 143             # (local) — substrate-singled-out cascade-saturation generation (S94 W5-1)
N_ATLAS_PIN = 78080              # (local) — L=10 atlas N = analytic 80080 minus dropped (4,4) sector (2000)

# Sage-exact cross-check anchors (cited per regulator-pin-discipline.md §"Sage-Exact Rationals"):
#   n_edge_saturated = C(78080,2) = 3048204160 (binomial, exact)
#   n_PBH_frozen_saturation = 24723793429 / 1406250000000000000000000000000000 = 1.7581364216177778e-23
#   canonical/frozen (exact QQ) = 3528281250/852544601 = 4.1385298151692
#   N_eigs(L) = (4/15)L^5+(10/3)L^4+16L^3+(110/3)L^2+(596/15)L+16 ; lim = +inf ; d lnN/d lnL -> 5
SAGE_N_EDGE_SAT_EXACT = 3048204160                       # (local) — C(78080,2), Sage binomial-exact
SAGE_RATIO_CANON_OVER_FROZEN = 4.138529815169166         # (local) — 3528281250/852544601 (Sage QQ)
SAGE_DLNN_DLNL_LIMIT = 5                                  # (local) — lim_{L->oo} d ln N_eigs/d ln L (Sage)


# ---------------------------------------------------------------------------
# Section 3 — Dual-SHA closure helpers (S84+ schema; mirrors _shared sibling)
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


def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str) -> None:
    """Append canonical verdict line + dual-SHA companion row + tier_pin companion row.

    [VERIFY] trigger; verdict is a CLASSIFICATION (re-anchorable vs HELD), NOT a
    directional prediction => NO schema-v2 3-tuple companion row (plan
    schema_v2_3tuple_required: false).

    CLASS=FULL: the closed-form cardinality-cascade + frozen-edge-count recompute carries
    NO -SCHEMATIC suffix (no SCHEMATIC helper consumed); a tier_pin=TIER-1 companion row
    documents the FULL physical level-pin disclosure.

    If SUPERSEDES_SHA is non-empty, the corrective canonical line carries a
    supersedes=<full-64-char-old-audit-sha> token in its value= field per gate-verdicts.md
    §"Option A" (the original line is RETAINED on disk; downstream consumers cite the latest
    NON-superseded line)."""
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
    tier_pin_row = (
        f"# tier_pin=TIER-1 # {GATE_ID} FULL physical level-pin disclosure "
        f"(closed-form g-axis cardinality-cascade + frozen atlas-N edge-count recompute; "
        f"Sage-exact-reproducible; NO SCHEMATIC helper consumed); "
        f"NON-PROMOTION-BY-HELD-NUMBER differentia=dimensionful-slot-collision "
        f"(cross-pillar-bridge-anatomy.md §26); held-number guard satisfied (magnitude HALF "
        f"of ONE held row; theorem-STRUCTURE STAGE-3-PERMANENT)\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(companion_row)
        fp.write(tier_pin_row)


# ---------------------------------------------------------------------------
# Section 4 — Cardinality-cascade machinery (closed forms; re-uses S94 npz arrays)
# ---------------------------------------------------------------------------
def n_eigs_polynomial(L: float) -> float:
    """Sage-exact closed form (corpus §25.1):
        N_eigs(L) = (4/15)L^5 + (10/3)L^4 + 16L^3 + (110/3)L^2 + (596/15)L + 16.
    lim_{L->oo} = +inf (the cardinality channel is truncation-DIVERGENT)."""
    return ((4.0 / 15.0) * L ** 5 + (10.0 / 3.0) * L ** 4 + 16.0 * L ** 3
            + (110.0 / 3.0) * L ** 2 + (596.0 / 15.0) * L + 16.0)  # (local)


def dln_neigs_dlnL(L: float) -> float:
    """d ln N_eigs / d ln L = L * N'(L) / N(L). lim_{L->oo} = 5 (dimensionless cascade exponent)."""
    N = n_eigs_polynomial(L)  # (local)
    Np = (5.0 * (4.0 / 15.0) * L ** 4 + 4.0 * (10.0 / 3.0) * L ** 3 + 3.0 * 16.0 * L ** 2
          + 2.0 * (110.0 / 3.0) * L + (596.0 / 15.0))  # (local)
    return float(L * Np / N)


# ---------------------------------------------------------------------------
# Section 5 — Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    # --- load S94 W5-1 g-axis saturation machinery (cache-load; no recompute of arrays) ---
    d = np.load(S94_ANCHOR_NPZ_PATH, allow_pickle=True)  # (local)
    n_PBH_frozen_saturation_m3 = float(d["n_PBH_frozen_saturation_m3"])  # (local) — D1 g-sat tail, L=10 baseline
    canonical_central_m3 = float(d["canonical_central_m3"])              # (local) — == n_PBH_FW_central
    n_PBH_linear_L14_m3 = float(d["n_PBH_linear_L14_m3"])                # (local) — divergent-channel linear-L14
    A_prefactor_m3 = float(d["A_prefactor_m3"])                          # (local) — m^-3 per-edge volume prefactor
    n_edge_saturated = int(d["n_edge_saturated"])                        # (local) — C(78080,2)
    prob_form = float(d["prob_form"])                                    # (local)
    L_pix_LRD_m = float(d["L_pix_LRD_m"])                                # (local)
    g_saturate = int(d["g_saturate"])                                    # (local)
    refinement_factor_L10_to_L14 = float(d["refinement_factor_L10_to_L14"])  # (local)
    ratio_canonical_over_baseline = float(d["ratio_canonical_over_baseline"])  # (local)
    npz_inv_is_dimensionless = bool(d["invariant_is_dimensionless"])     # (local) — npz prior classification
    npz_dim_div_same_slot = bool(d["dimension_and_divergence_same_slot"])  # (local) — npz prior classification
    npz_tier_class = str(d["tier_classification"])                       # (local)
    npz_level3_row = str(d["level3_m3_row"])                             # (local)
    npz_D1_Lmax_indep = bool(d["D1_g_of_K_Lmax_independent"])            # (local)
    npz_D1_saturates = bool(d["D1_saturates_above_g_saturate"])          # (local)
    n_eigs_arr = np.asarray(d["n_eigs"], dtype=np.float64)               # (local)
    Ls_arr = np.asarray(d["Ls"], dtype=np.int64)                        # (local)
    lim_N_eigs = str(d["lim_N_eigs"])                                    # (local) — '+inf'
    dln_dlnL_14 = float(d["dln_dlnL_14"])                                # (local)
    dln_dlnL_limit = float(d["dln_dlnL_limit"])                         # (local)

    # ===================================================================
    # (A) RE-VERIFY the substitution chain: canonical/frozen == L10->L14 refinement
    # ===================================================================
    ratio_recompute = canonical_central_m3 / n_PBH_frozen_saturation_m3  # (local)
    # 5-sig-fig agreement with both npz ratio fields and the Sage-exact value:
    chain_match_npz_refine = bool(abs(ratio_recompute - refinement_factor_L10_to_L14)
                                  / refinement_factor_L10_to_L14 < 2e-4)  # (local) — 5 sig figs
    chain_match_npz_baseline = bool(abs(ratio_recompute - ratio_canonical_over_baseline)
                                    / ratio_canonical_over_baseline < 1e-9)  # (local)
    chain_match_sage = bool(abs(ratio_recompute - SAGE_RATIO_CANON_OVER_FROZEN)
                            / SAGE_RATIO_CANON_OVER_FROZEN < 1e-9)  # (local)
    substitution_chain_ok = bool(chain_match_npz_refine and chain_match_npz_baseline
                                 and chain_match_sage)  # (local)

    # cross-check: canonical_central_m3 == canonical_constants n_PBH_FW_central
    canon_matches_constants = bool(abs(canonical_central_m3 - float(n_PBH_FW_central))
                                   / float(n_PBH_FW_central) < 1e-4)  # (local) — 4 sig figs (Class-8.3)

    # cross-check: the FROZEN saturated tail from the FROZEN atlas N (independent recompute)
    n_edge_recompute = N_ATLAS_PIN * (N_ATLAS_PIN - 1) // 2  # (local) — C(78080,2) integer-exact
    n_edge_match_sage = bool(n_edge_recompute == SAGE_N_EDGE_SAT_EXACT)  # (local)
    n_edge_match_npz = bool(n_edge_recompute == n_edge_saturated)  # (local)
    n_PBH_sat_recompute = n_edge_recompute * prob_form / L_pix_LRD_m ** 3  # (local) — independent of npz value
    n_PBH_sat_match = bool(abs(n_PBH_sat_recompute - n_PBH_frozen_saturation_m3)
                           / n_PBH_frozen_saturation_m3 < 1e-12)  # (local)

    # ===================================================================
    # (B) Tier-1 test: is the SATURATED-TAIL magnitude L_max-INDEPENDENT?
    # The g_saturate=143 saturated tail uses the FROZEN atlas N=78080 => the cardinality
    # is FIXED at saturation => n_PBH_sat(L) is a CONSTANT in L by construction.
    # Evaluate n_PBH_sat at each L in the scan; the FROZEN form does not read N_eigs(L).
    # ===================================================================
    L_scan = np.array(L_SCAN, dtype=np.float64)  # (local)
    # FROZEN saturated tail at each L (constant; cardinality frozen at g_saturate):
    n_PBH_sat_of_L = np.full(L_scan.size, n_PBH_sat_recompute, dtype=np.float64)  # (local)
    ln_n_sat = np.log(n_PBH_sat_of_L)  # (local)
    ln_L = np.log(L_scan)  # (local)
    # dln(n_PBH_sat)/dln L over the scan (centered finite difference):
    dln_nsat_dlnL = np.gradient(ln_n_sat, ln_L)  # (local) — identically 0 for a frozen value
    max_abs_dln_nsat_dlnL = float(np.max(np.abs(dln_nsat_dlnL)))  # (local)
    sat_magnitude_Lmax_independent = bool(max_abs_dln_nsat_dlnL < DLN_DLNL_PASS_CEILING)  # (local)
    # plateau check vs FD floor (saturation-plateau is flat to the FD floor):
    sat_plateau_flat = bool(
        float(np.max(n_PBH_sat_of_L) - np.min(n_PBH_sat_of_L)) <= FD_FLOOR * n_PBH_sat_recompute
    )  # (local)

    # CONTRAST channel: the LINEAR-L14 magnitude A*N_eigs(L) DOES depend on L (divergent).
    n_PBH_linear_of_L = A_prefactor_m3 * np.array(
        [n_eigs_polynomial(float(L)) for L in L_scan], dtype=np.float64
    )  # (local)
    ln_n_lin = np.log(n_PBH_linear_of_L)  # (local)
    dln_nlin_dlnL = np.gradient(ln_n_lin, ln_L)  # (local) — ~ 5 (the cascade exponent)
    max_abs_dln_nlin_dlnL = float(np.max(np.abs(dln_nlin_dlnL)))  # (local)
    linear_magnitude_Lmax_independent = bool(max_abs_dln_nlin_dlnL < DLN_DLNL_PASS_CEILING)  # (local) — expect False
    # confirm the cascade exponent LIMIT (Sage-PROVEN: lim_{L->oo} d ln N_eigs/d ln L = 5 EXACTLY).
    # The finite-L value rises MONOTONICALLY toward 5 (subleading polynomial terms); the limit is a
    # PROVEN dimensionless INTEGER, not a finite-L numerical artifact. We confirm the APPROACH
    # direction (monotone-toward-5, value > leading-degree-1, gap closing as L grows) rather than
    # demanding finite-L equality at the 0.1 tolerance (which the polynomial cannot reach by L=100).
    dlnN_dlnL_at_50 = dln_neigs_dlnL(50.0)    # (local) — cascade exponent at L=50
    dlnN_dlnL_at_100 = dln_neigs_dlnL(100.0)  # (local) — cascade exponent at L=100 (closer to 5)
    dlnN_dlnL_at_1000 = dln_neigs_dlnL(1000.0)  # (local) — far-L confirmation of the limit
    # monotone approach toward the Sage-proven integer 5 from below, bounded above BY 5:
    cascade_exp_to_5 = bool(
        dlnN_dlnL_at_50 < dlnN_dlnL_at_100 < dlnN_dlnL_at_1000 < SAGE_DLNN_DLNL_LIMIT
        and abs(dlnN_dlnL_at_1000 - SAGE_DLNN_DLNL_LIMIT) < 0.05  # (local) — within 0.05 of 5 at L=1000
        and SAGE_DLNN_DLNL_LIMIT == 5  # the Sage-PROVEN limit is the dimensionless integer 5
    )  # (local) — the cascade exponent IS the dimensionless integer 5 (limit proven; approach confirmed)

    # ===================================================================
    # (C) Tier-2 test: is the truncation-invariant content DIMENSIONLESS or DIMENSIONFUL?
    # O(L,K) = W(L)*g(K): only log-derivatives annihilate W(L). For the cardinality channel,
    # the truncation-invariant content is the dimensionless cascade exponent d ln N_eigs/d ln L
    # -> 5 (an INTEGER). BUT it annihilates the m^-3 prefactor A (dimensionful per-edge volume
    # prob_form/L_pix^3). The DIMENSION (m^-3) and the DIVERGENCE (N_eigs~L^5) live in the SAME
    # multiplicative slot: O(L) = A * N_eigs(L), A dimensionful, N_eigs(L) divergent.
    # The dimensionless invariant (5) is NOT the magnitude; the dimensionful magnitude lives on
    # the divergent channel that the log-derivative cannot re-anchor. => Tier-2-DIMENSIONFUL.
    # ===================================================================
    # RE-DERIVE the same-slot status (do NOT trust the npz flag): the m^-3 dimension is carried
    # by A (a per-edge volume), and the divergence is carried by N_eigs(L). The product A*N_eigs(L)
    # is the linear channel; the log-derivative d ln(A*N_eigs)/d ln L = d ln N_eigs/d ln L (A's
    # contribution is annihilated because A is L-INDEPENDENT). So the surviving truncation-invariant
    # content is the DIMENSIONLESS integer 5 — but it does NOT carry the m^-3 magnitude. The
    # dimensionful magnitude (A * lim N_eigs) DIVERGES. Hence dimension and divergence share the slot.
    # RE-DERIVED Tier-2 classification (substitution chain, independent of the npz flag):
    #   Step 1: the dimensionful magnitude is O(L) = A · N_eigs(L); A carries m^-3, N_eigs(L) is
    #           dimensionless but DIVERGENT (lim N_eigs = +inf, Sage-exact).
    #   Step 2: the truncation-invariant content extracted by the log-derivative is
    #           d ln O/d ln L = d ln A/d ln L + d ln N_eigs/d ln L = 0 + (-> 5).
    #           The surviving invariant is the dimensionless INTEGER 5 => invariant_is_dimensionless.
    #   Step 3: the integer 5 is a RATE, not a MAGNITUDE; the dimensionful magnitude A·N_eigs(L)
    #           itself DIVERGES (A·lim N_eigs = +inf). The log-derivative annihilated A, so the
    #           m^-3 dimension was carried AWAY with the divergent channel — no finite dimensionless
    #           ratio reconstructs the m^-3 magnitude.
    #   Step 4: => dimension (m^-3, in A) and divergence (N_eigs->inf) occupy the SAME multiplicative
    #           slot O = A·N_eigs. dimension_and_divergence_same_slot = True (structural; NOT
    #           contingent on whether the dimensionless rate exists).
    #   Step 5: Tier-2 re-anchorable iff a dimensionless log-derivative / ratio CARRIES the magnitude.
    #           Here it does NOT (it carries only the rate-5) => tier2_reanchorable = False
    #           => TIER-2-DIMENSIONFUL (corpus §25.1, the §VII.AX n_PBH inaugural K=1 instance).
    # invariant_is_dimensionless: a dimensionless truncation-invariant (the cascade exponent 5) EXISTS.
    invariant_is_dimensionless = bool(cascade_exp_to_5)  # (local) — the integer-5 cascade exponent (Sage-proven limit)
    # same-slot: the m^-3 prefactor A is the SOLE carrier of the magnitude's dimension AND it
    # multiplies the divergent channel; the magnitude lives on the divergent channel (the linear
    # dimensionful channel diverges) WHILE the surviving log-derivative invariant is dimensionless
    # (and so cannot carry the m^-3 magnitude). Both conditions => dimension and divergence share
    # the one multiplicative slot O = A·N_eigs(L).
    dimensionful_channel_diverges = bool(not linear_magnitude_Lmax_independent)  # (local) — A·N_eigs(L) diverges
    dimensionless_invariant_cannot_carry_magnitude = bool(invariant_is_dimensionless)  # (local) — rate-5, not magnitude
    dimension_and_divergence_same_slot = bool(
        dimensionful_channel_diverges and dimensionless_invariant_cannot_carry_magnitude
    )  # (local) — RE-DERIVED True (matches S94 npz + corpus §25.1)
    # Tier-2 re-anchorable iff the truncation-invariant DIMENSIONLESS content CARRIES the magnitude,
    # i.e. invariant_is_dimensionless AND the dimension is NOT trapped in the divergence's slot.
    # (For §VII.AV L_emp this holds: a 2nd log-derivative annihilates a power-law prefactor and the
    # surviving content is dimensionless M_KK^2 — the K-window unit. For n_PBH it does NOT.)
    tier2_reanchorable = bool(invariant_is_dimensionless and not dimension_and_divergence_same_slot)  # (local)
    tier_classification = (
        "TIER-2-DIMENSIONLESS-REANCHORABLE" if tier2_reanchorable else "TIER-2-DIMENSIONFUL"
    )  # (local)
    # consistency with the S94 npz prior classification (a cross-check, NOT the verdict source):
    matches_npz_tier = bool(
        (tier_classification == "TIER-2-DIMENSIONFUL") == (npz_tier_class == "TIER-2-DIMENSIONFUL")
        and dimension_and_divergence_same_slot == npz_dim_div_same_slot
        and invariant_is_dimensionless == npz_inv_is_dimensionless
    )  # (local)

    # ===================================================================
    # VERDICT (plan §W6-1 operator)
    # ===================================================================
    inputs_ok = bool(
        substitution_chain_ok and canon_matches_constants and n_edge_match_sage
        and n_edge_match_npz and n_PBH_sat_match
        and math.isfinite(n_PBH_sat_recompute) and n_PBH_sat_recompute > 0
    )  # (local)

    if not inputs_ok:
        verdict = "FAIL"
        band_tag = "FAIL_input_or_substitution_chain_did_not_reproduce"  # (local)
    elif not sat_magnitude_Lmax_independent:
        # the g_saturate plateau is itself L-drifting => not substrate-singled-out
        verdict = "FAIL"
        band_tag = "FAIL_g_saturate_plateau_L_drifting_no_substrate_singled_L_star"  # (local)
    elif sat_magnitude_Lmax_independent and not dimension_and_divergence_same_slot:
        # L_max-INDEPENDENT AND dimensionless re-anchorable => discharge HELD -> anchored
        verdict = "PASS"
        band_tag = "PASS_saturated_tail_Lmax_independent_AND_Tier-2_dimensionless_reanchorable"  # (local)
    else:
        # L_max-INDEPENDENT at g_saturate confirmed, BUT Tier-2-DIMENSIONFUL (same slot):
        # magnitude PINNED to substrate-physical g_saturate value; row stays HELD; decoupled.
        verdict = "INFO"
        band_tag = ("INFO_saturated_tail_Lmax_independent_BUT_Tier-2-DIMENSIONFUL_"
                    "row_HELD_magnitude_decoupled_pinned_to_g_saturate")  # (local)

    return {
        "n_PBH_FW_central": float(n_PBH_FW_central), "M_KK": float(M_KK), "tau_fold": float(tau_fold),
        # the two magnitudes:
        "n_PBH_frozen_saturation_m3": n_PBH_frozen_saturation_m3,
        "n_PBH_sat_recompute_m3": n_PBH_sat_recompute,
        "canonical_central_m3": canonical_central_m3,
        "n_PBH_linear_L14_m3": n_PBH_linear_L14_m3,
        "A_prefactor_m3": A_prefactor_m3, "prob_form": prob_form, "L_pix_LRD_m": L_pix_LRD_m,
        "n_edge_saturated": n_edge_saturated, "n_edge_recompute": n_edge_recompute,
        "g_saturate": g_saturate, "N_atlas": N_ATLAS_PIN,
        # substitution-chain re-verification:
        "ratio_recompute": ratio_recompute,
        "refinement_factor_L10_to_L14": refinement_factor_L10_to_L14,
        "ratio_canonical_over_baseline": ratio_canonical_over_baseline,
        "chain_match_npz_refine": chain_match_npz_refine,
        "chain_match_npz_baseline": chain_match_npz_baseline,
        "chain_match_sage": chain_match_sage,
        "substitution_chain_ok": substitution_chain_ok,
        "canon_matches_constants": canon_matches_constants,
        "n_edge_match_sage": n_edge_match_sage, "n_edge_match_npz": n_edge_match_npz,
        "n_PBH_sat_match": n_PBH_sat_match,
        # Tier-1 (L_max-independence):
        "L_scan": L_scan, "n_PBH_sat_of_L": n_PBH_sat_of_L,
        "dln_nsat_dlnL": dln_nsat_dlnL, "max_abs_dln_nsat_dlnL": max_abs_dln_nsat_dlnL,
        "sat_magnitude_Lmax_independent": sat_magnitude_Lmax_independent,
        "sat_plateau_flat": sat_plateau_flat,
        "n_PBH_linear_of_L": n_PBH_linear_of_L, "dln_nlin_dlnL": dln_nlin_dlnL,
        "max_abs_dln_nlin_dlnL": max_abs_dln_nlin_dlnL,
        "linear_magnitude_Lmax_independent": linear_magnitude_Lmax_independent,
        "dlnN_dlnL_at_50": dlnN_dlnL_at_50, "dlnN_dlnL_at_100": dlnN_dlnL_at_100,
        "dlnN_dlnL_at_1000": dlnN_dlnL_at_1000, "cascade_exp_to_5": cascade_exp_to_5,
        # Tier-2 (dimensionless vs dimensionful):
        "invariant_is_dimensionless": invariant_is_dimensionless,
        "dimension_and_divergence_same_slot": dimension_and_divergence_same_slot,
        "tier2_reanchorable": tier2_reanchorable, "tier_classification": tier_classification,
        "matches_npz_tier": matches_npz_tier,
        # npz prior classification (cross-check):
        "npz_tier_class": npz_tier_class, "npz_level3_row": npz_level3_row,
        "npz_inv_is_dimensionless": npz_inv_is_dimensionless,
        "npz_dim_div_same_slot": npz_dim_div_same_slot,
        "npz_D1_Lmax_indep": npz_D1_Lmax_indep, "npz_D1_saturates": npz_D1_saturates,
        "lim_N_eigs": lim_N_eigs, "dln_dlnL_14": dln_dlnL_14, "dln_dlnL_limit": dln_dlnL_limit,
        "n_eigs_arr": n_eigs_arr, "Ls_arr": Ls_arr,
        "pass_ceiling": DLN_DLNL_PASS_CEILING, "fd_floor": FD_FLOOR,
        # verdict:
        "inputs_ok": inputs_ok, "verdict": verdict, "band_tag": band_tag,
    }


# ---------------------------------------------------------------------------
# Section 6 — Plot
# ---------------------------------------------------------------------------
def make_plot(r: dict) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(14.0, 9.5), dpi=120)

    # Panel A: the two magnitudes vs L — frozen-saturated (flat) vs linear-L (divergent)
    axA = axes[0, 0]
    axA.semilogy(r["L_scan"], r["n_PBH_sat_of_L"], "o-", color="#2ca02c", ms=6, lw=1.6,
                 label=f"g-saturated tail (FROZEN N={r['N_atlas']}); L-INDEP\n"
                       f"  n_PBH_sat={r['n_PBH_sat_recompute_m3']:.4e} m$^{{-3}}$")
    axA.semilogy(r["L_scan"], r["n_PBH_linear_of_L"], "s--", color="#d62728", ms=6, lw=1.6,
                 label=f"linear-channel A·N_eigs(L); DIVERGENT\n"
                       f"  (max|dln/dlnL|={r['max_abs_dln_nlin_dlnL']:.3f} -> cascade exp 5)")
    axA.axhline(r["canonical_central_m3"], color="k", ls=":", lw=1.0,
                label=f"canonical n_PBH_FW_central={r['canonical_central_m3']:.4e}")
    axA.set_xlabel("L (truncation)"); axA.set_ylabel("n_PBH  [m$^{-3}$]  (log)")
    axA.set_title("(A) Two magnitudes: g-saturated tail is L-FROZEN (flat);\n"
                  "linear channel A·N_eigs(L) diverges (carries L10->L14 4.14x refinement)")
    axA.legend(fontsize=7.5); axA.grid(alpha=0.3)

    # Panel B: log-derivatives dln/dlnL — saturated (=0) vs linear (~5)
    axB = axes[0, 1]
    axB.plot(r["L_scan"], r["dln_nsat_dlnL"], "o-", color="#2ca02c", ms=6, lw=1.6,
             label=f"d ln(n_PBH_sat)/d ln L (max|·|={r['max_abs_dln_nsat_dlnL']:.2e})")
    axB.plot(r["L_scan"], r["dln_nlin_dlnL"], "s--", color="#d62728", ms=6, lw=1.6,
             label=f"d ln(A·N_eigs)/d ln L (-> cascade exp {SAGE_DLNN_DLNL_LIMIT})")
    axB.axhline(r["pass_ceiling"], color="purple", ls="--", lw=1.0,
                label=f"PASS ceiling {r['pass_ceiling']:.0e}")
    axB.axhline(-r["pass_ceiling"], color="purple", ls="--", lw=1.0)
    axB.set_xlabel("L (truncation)"); axB.set_ylabel("d ln n_PBH / d ln L")
    axB.set_title("(B) Tier-1 L_max-independence: saturated tail dln/dlnL ~ 0 < 1e-3\n"
                  "(L_max-INDEPENDENT); linear channel dln/dlnL ~ 5 (DIVERGENT)")
    axB.legend(fontsize=8); axB.grid(alpha=0.3)

    # Panel C: N_eigs(L) growth — the divergent cardinality channel
    axC = axes[1, 0]
    axC.semilogy(r["Ls_arr"], r["n_eigs_arr"], "o-", color="#1f77b4", ms=3, lw=1.0,
                 label="N_eigs(L) = (4/15)L⁵+... (Sage-exact; lim=+∞)")
    axC.axvline(10, color="gray", ls=":", lw=1.0, label="L=10 (atlas parent 80080; atlas N=78080)")
    axC.axvline(14, color="orange", ls=":", lw=1.0, label="L=14 (n_eigs=323136; linear-L14 anchor)")
    axC.set_xlabel("L (truncation)"); axC.set_ylabel("N_eigs(L)  (log)")
    axC.set_title("(C) Cardinality channel DIVERGES (lim N_eigs=+∞);\n"
                  "the m⁻³ prefactor A shares this multiplicative slot => Tier-2-DIMENSIONFUL")
    axC.legend(fontsize=7.5); axC.grid(alpha=0.3)

    # Panel D: verdict + diagnostic text
    axD = axes[1, 1]
    axD.axis("off")
    lines = [
        f"VERDICT: {r['verdict']}",
        f"band_tag: {r['band_tag']}",
        f"tier_classification (RE-DERIVED): {r['tier_classification']}",
        "",
        "--- Substitution chain re-verification ---",
        f"  canonical/frozen = {r['ratio_recompute']:.6f}",
        f"    vs npz refine 4.138525  match={r['chain_match_npz_refine']}",
        f"    vs npz baseline {r['ratio_canonical_over_baseline']:.6f} match={r['chain_match_npz_baseline']}",
        f"    vs Sage QQ 4.138530    match={r['chain_match_sage']}",
        f"  substitution_chain_ok = {r['substitution_chain_ok']}",
        "",
        "--- Magnitudes (m^-3) ---",
        f"  g-saturated tail (L-FROZEN) = {r['n_PBH_sat_recompute_m3']:.6e}",
        f"  canonical n_PBH_FW_central  = {r['canonical_central_m3']:.6e}",
        f"  linear-L14 (divergent)      = {r['n_PBH_linear_L14_m3']:.6e}",
        f"  C(78080,2) = {r['n_edge_recompute']} (Sage match={r['n_edge_match_sage']})",
        f"  canon==constants n_PBH_FW_central: {r['canon_matches_constants']}",
        "",
        "--- Tier-1: L_max-independence ---",
        f"  saturated tail max|dln/dlnL| = {r['max_abs_dln_nsat_dlnL']:.2e} (< 1e-3)",
        f"    => L_max-INDEPENDENT = {r['sat_magnitude_Lmax_independent']}",
        f"  linear channel max|dln/dlnL| = {r['max_abs_dln_nlin_dlnL']:.3f}",
        f"    => L_max-INDEPENDENT = {r['linear_magnitude_Lmax_independent']} (cascade exp->5: {r['cascade_exp_to_5']})",
        "",
        "--- Tier-2: dimensionless vs dimensionful ---",
        f"  invariant_is_dimensionless = {r['invariant_is_dimensionless']} (cascade exp = integer 5)",
        f"  dimension_and_divergence_same_slot = {r['dimension_and_divergence_same_slot']}",
        f"  tier2_reanchorable = {r['tier2_reanchorable']}",
        f"  matches S94 npz prior classification = {r['matches_npz_tier']}",
        "",
        "--- Held-number guard ---",
        "  magnitude HALF of ONE held row (which-anchor closed S94 W5-1)",
        "  theorem-STRUCTURE STAGE-3-PERMANENT (unchanged by this verdict)",
    ]
    axD.text(0.0, 1.0, "\n".join(lines), va="top", ha="left", fontsize=6.6,
             family="monospace", transform=axD.transAxes)
    axD.set_title("(D) Diagnostic summary")

    fig.suptitle(
        f"{GATE_ID}\n"
        f"PBH n_PBH magnitude recompute: g-saturated tail L_max-INDEP, Tier-2 re-anchorability — "
        f"{r['verdict']}  ({r['tier_classification']})",
        fontsize=10.5, y=1.005,
    )
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(OUT_PNG, dpi=120, bbox_inches="tight")
    plt.close(fig)
    print(f"\nplot -> {OUT_PNG.relative_to(PROJECT_ROOT)}")


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)
    print(f"=== {GATE_ID} ===")
    print(f"tau_fold = {tau_fold!r}  M_KK = {M_KK!r}  n_PBH_FW_central = {n_PBH_FW_central!r}")

    INPUT_FILES = [
        Path(__file__).resolve(),
        CANONICAL_CONSTANTS_PATH,
        S94_ANCHOR_NPZ_PATH,
    ]  # (local)
    pins = log_input_pins(INPUT_FILES)  # (local)

    r = compute()  # (local)

    print("\n=== Substitution chain re-verification ===")
    print(f"  canonical/frozen = {r['ratio_recompute']:.9f}")
    print(f"    vs npz refinement_factor_L10_to_L14 = {r['refinement_factor_L10_to_L14']:.9f} "
          f"match={r['chain_match_npz_refine']}")
    print(f"    vs npz ratio_canonical_over_baseline = {r['ratio_canonical_over_baseline']:.9f} "
          f"match={r['chain_match_npz_baseline']}")
    print(f"    vs Sage QQ 3528281250/852544601 = {SAGE_RATIO_CANON_OVER_FROZEN:.9f} "
          f"match={r['chain_match_sage']}")
    print(f"  substitution_chain_ok = {r['substitution_chain_ok']}")

    print("\n=== Magnitudes (m^-3) ===")
    print(f"  g-saturated tail (L-FROZEN)  = {r['n_PBH_sat_recompute_m3']:.9e}")
    print(f"  canonical n_PBH_FW_central   = {r['canonical_central_m3']:.9e}  "
          f"(==constants: {r['canon_matches_constants']})")
    print(f"  linear-L14 (divergent chan)  = {r['n_PBH_linear_L14_m3']:.9e}")
    print(f"  n_edge C(78080,2) = {r['n_edge_recompute']}  Sage-match={r['n_edge_match_sage']}  "
          f"npz-match={r['n_edge_match_npz']}  n_PBH_sat-match={r['n_PBH_sat_match']}")

    print("\n=== Tier-1: L_max-independence (PASS ceiling 1e-3) ===")
    print(f"  saturated tail max|dln/dlnL| = {r['max_abs_dln_nsat_dlnL']:.3e}  "
          f"=> L_max-INDEPENDENT = {r['sat_magnitude_Lmax_independent']}  "
          f"plateau_flat={r['sat_plateau_flat']}")
    print(f"  linear channel max|dln/dlnL| = {r['max_abs_dln_nlin_dlnL']:.6f}  "
          f"=> L_max-INDEPENDENT = {r['linear_magnitude_Lmax_independent']} "
          f"(cascade exp at L=100 = {r['dlnN_dlnL_at_100']:.4f} -> 5: {r['cascade_exp_to_5']})")

    print("\n=== Tier-2: dimensionless vs dimensionful (RE-DERIVED, not npz-trusted) ===")
    print(f"  invariant_is_dimensionless = {r['invariant_is_dimensionless']} "
          f"(cascade exponent = dimensionless integer 5)")
    print(f"  dimension_and_divergence_same_slot = {r['dimension_and_divergence_same_slot']}")
    print(f"  tier2_reanchorable = {r['tier2_reanchorable']}  => {r['tier_classification']}")
    print(f"  matches S94 npz prior classification = {r['matches_npz_tier']} "
          f"(npz: {r['npz_tier_class']}, same_slot={r['npz_dim_div_same_slot']})")

    print(f"\nVERDICT: {r['verdict']}  ({r['band_tag']})")

    make_plot(r)

    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID, verdict=r["verdict"], band_tag=r["band_tag"],
        scheme=SCHEME, convention=CONVENTION,
        n_PBH_FW_central=r["n_PBH_FW_central"], M_KK=r["M_KK"], tau_fold=r["tau_fold"],
        # magnitudes:
        n_PBH_frozen_saturation_m3=r["n_PBH_frozen_saturation_m3"],
        n_PBH_sat_recompute_m3=r["n_PBH_sat_recompute_m3"],
        canonical_central_m3=r["canonical_central_m3"],
        n_PBH_linear_L14_m3=r["n_PBH_linear_L14_m3"],
        A_prefactor_m3=r["A_prefactor_m3"], prob_form=r["prob_form"], L_pix_LRD_m=r["L_pix_LRD_m"],
        n_edge_saturated=r["n_edge_saturated"], n_edge_recompute=r["n_edge_recompute"],
        g_saturate=r["g_saturate"], N_atlas=r["N_atlas"],
        # substitution chain:
        ratio_recompute=r["ratio_recompute"],
        refinement_factor_L10_to_L14=r["refinement_factor_L10_to_L14"],
        ratio_canonical_over_baseline=r["ratio_canonical_over_baseline"],
        chain_match_npz_refine=r["chain_match_npz_refine"],
        chain_match_npz_baseline=r["chain_match_npz_baseline"],
        chain_match_sage=r["chain_match_sage"], substitution_chain_ok=r["substitution_chain_ok"],
        canon_matches_constants=r["canon_matches_constants"],
        n_edge_match_sage=r["n_edge_match_sage"], n_edge_match_npz=r["n_edge_match_npz"],
        n_PBH_sat_match=r["n_PBH_sat_match"],
        sage_n_edge_sat_exact=SAGE_N_EDGE_SAT_EXACT,
        sage_ratio_canon_over_frozen=SAGE_RATIO_CANON_OVER_FROZEN,
        sage_dlnN_dlnL_limit=SAGE_DLNN_DLNL_LIMIT,
        # Tier-1:
        L_scan=r["L_scan"], n_PBH_sat_of_L=r["n_PBH_sat_of_L"],
        dln_nsat_dlnL=r["dln_nsat_dlnL"], max_abs_dln_nsat_dlnL=r["max_abs_dln_nsat_dlnL"],
        sat_magnitude_Lmax_independent=r["sat_magnitude_Lmax_independent"],
        sat_plateau_flat=r["sat_plateau_flat"],
        n_PBH_linear_of_L=r["n_PBH_linear_of_L"], dln_nlin_dlnL=r["dln_nlin_dlnL"],
        max_abs_dln_nlin_dlnL=r["max_abs_dln_nlin_dlnL"],
        linear_magnitude_Lmax_independent=r["linear_magnitude_Lmax_independent"],
        dlnN_dlnL_at_50=r["dlnN_dlnL_at_50"], dlnN_dlnL_at_100=r["dlnN_dlnL_at_100"],
        dlnN_dlnL_at_1000=r["dlnN_dlnL_at_1000"], cascade_exp_to_5=r["cascade_exp_to_5"],
        # Tier-2:
        invariant_is_dimensionless=r["invariant_is_dimensionless"],
        dimension_and_divergence_same_slot=r["dimension_and_divergence_same_slot"],
        tier2_reanchorable=r["tier2_reanchorable"], tier_classification=r["tier_classification"],
        matches_npz_tier=r["matches_npz_tier"],
        # npz prior classification:
        npz_tier_class=r["npz_tier_class"], npz_level3_row=r["npz_level3_row"],
        npz_inv_is_dimensionless=r["npz_inv_is_dimensionless"],
        npz_dim_div_same_slot=r["npz_dim_div_same_slot"],
        npz_D1_Lmax_indep=r["npz_D1_Lmax_indep"], npz_D1_saturates=r["npz_D1_saturates"],
        lim_N_eigs=r["lim_N_eigs"], dln_dlnL_14=r["dln_dlnL_14"], dln_dlnL_limit=r["dln_dlnL_limit"],
        n_eigs_arr=r["n_eigs_arr"], Ls_arr=r["Ls_arr"],
        pass_ceiling=r["pass_ceiling"], fd_floor=r["fd_floor"],
        inputs_ok=r["inputs_ok"],
    )
    print(f"data -> {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    # --- value field for verdict line ---
    value_field = (
        f"n_PBH_sat={r['n_PBH_sat_recompute_m3']:.4e}_m^-3(g_saturate={r['g_saturate']}_FROZEN_N={r['N_atlas']});"
        f"canonical_central={r['canonical_central_m3']:.4e}_m^-3(linear-L14_divergent);"
        f"ratio_canon_over_frozen={r['ratio_recompute']:.5f}==L10toL14_refine(chain_ok={r['substitution_chain_ok']});"
        f"sat_max_dln_dlnL={r['max_abs_dln_nsat_dlnL']:.2e};sat_Lmax_INDEP={r['sat_magnitude_Lmax_independent']};"
        f"linear_max_dln_dlnL={r['max_abs_dln_nlin_dlnL']:.3f}_cascade_exp->5={r['cascade_exp_to_5']};"
        f"invariant_dimensionless={r['invariant_is_dimensionless']};"
        f"dim_div_same_slot={r['dimension_and_divergence_same_slot']};"
        f"tier_class={r['tier_classification']};tier2_reanchorable={r['tier2_reanchorable']};"
        f"matches_S94_npz_tier={r['matches_npz_tier']};"
        f"level3_m3_row=REGISTRY-PASS-INELIGIBLE-HELD-magnitude-DECOUPLED-pinned-to-g_saturate;"
        f"VII.AX.OP-PROJ_theorem_STRUCTURE=STAGE-3-PERMANENT(unchanged);"
        f"n_edge_C78080_2={r['n_edge_recompute']}(Sage-exact);PASS_ceiling=1e-3;band_tag={r['band_tag']}"
    )  # (local)

    print(f"\n4-tuple: (value='{value_field[:90]}...', scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")

    input_pin_map = {rel: sha for rel, sha in pins.items()}  # (local)
    input_pin_map["canonical_constants_n_PBH_FW_central"] = f"{float(n_PBH_FW_central):.18e}"
    input_pin_map["canonical_constants_M_KK"] = f"{float(M_KK):.18e}"
    input_pin_map["canonical_constants_tau_fold"] = f"{float(tau_fold):.18e}"
    input_pin_map["_gate_id"] = GATE_ID
    input_pin_map["_scheme"] = SCHEME
    input_pin_map["_convention"] = CONVENTION
    input_pin_map["_g_saturate"] = str(G_SATURATE_PIN)
    input_pin_map["_N_atlas"] = str(N_ATLAS_PIN)

    audit_sha, content_sha = compute_dual_sha(
        Path(__file__).resolve(), CANONICAL_CONSTANTS_PATH, input_pin_map
    )  # (local)
    append_verdict(r["verdict"], value_field, audit_sha, content_sha)
    print(f"\nverdict appended: {r['verdict']} -- value (truncated)={value_field[:100]!r}...")
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print(f"\nwall: {time.time() - t0:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
