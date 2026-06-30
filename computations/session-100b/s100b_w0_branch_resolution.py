#!/usr/bin/env python3
"""
S100b-W0-BRANCH-RESOLUTION — w_0 branch resolution (leg-1 mechanical
re-execution of the PRIMARY decision rule + leg-2 branch-iv L_max stability
under the post-S86-retirement formulation with the DR3 CAC lockdown).
=======================================================================

Gate: S100b-W0-BRANCH-RESOLUTION ([VERIFY])
Plan: sessions/session-plan/session-100b-plan-w1.md §W1-4
Agent: sagan-empiricist (mack self-blacklisted: own carry-forward source)
Classification: GEOMETRIC (projection structure of the spectral triple;
the branch question is a property of how the substrate's late-time
spectral-action gradient projects onto observational coordinates).

LEG-1 (mechanical, deterministic — no re-derivation latitude):
  Re-execute w0-primary-decision-rule.md §3:
    PRIMARY = candidate satisfying (registry-history-priority AND
    DR3-rectangle-membership) = A unless a structural argument promotes B.
  Components verified for currency:
    C4 registry-history: w0_FW = -0.918 canonical pin present, unmodified,
       not superseded; w0_FW_R842 ABSENT (B has no canonical-pin history).
    C2 R_842 membership: |x - (-0.842)| <= 0.100 for BOTH candidates.
    §5 reversal protocol ARMED UNMODIFIED: file SHA == plan-freeze pin AND
       band [-0.86, -0.83] AND sigma_DR3 = 0.025 AND locked-machinery text.
  Data-proximity EXCLUSION (pre-registered): the post-Dovekie sigma
  distances (0.731 / 2.130) are echoed to a WP-table-only record and enter
  NO selection predicate (the selection function takes exactly two boolean
  inputs per candidate: history-priority, rectangle-membership).

LEG-2 (branch-iv L_max stability — the NEW content):
  Pre-registered route ladder (plan §W1-4 method):
    ROUTE-ALPHA: recover the branch-iv w_0 evaluator from the S84 SV-series
      + S85-W10 anchor scripts and re-evaluate rho_B(L) at L in {8,10,12}
      under the POST-S86 formulation (R_JK distance-2 / xi_E_GGE_inv
      distance-1 split — NO legacy single-tag R_JE evaluation).
    ROUTE-BETA (iff alpha unrecoverable): R_JK L-trajectory mapped into
      w_0 units via the S85-W10 anchor-script mapping.
    IFF NEITHER recoverable: INFO,
      value='branch-iv-w0-L-evaluator-not-recoverable', R_JK trajectory
      documented, stability UNVERIFIED (honest formulation-gap record).
  Route-adjudication tests (deterministic, evidence-based, pinned inputs):
    RA-1 archived-evaluator recovery: SV1 closed form reproduces
         w_0_iv = -0.842454 (tol 1e-5) and admits the EXACT reduction
            w_0^{(iv)} = f(R_JE),
            f(R) = (-c_J*R + P_GGE_zeta) / (c_J*R + rho_GGE_zeta),
            c_J  = |F_Josephson_zeta| / N_cells,
         verified to 1e-12. The evaluator's SOLE L_max-dependent input is
         the GGE-sector dressing ratio slot R = xi_J / xi_E_GGE(L) — the
         single-tag R_JE that S86 RETIRED.
    RA-2 post-S86 formulation facts: S86-BRANCH-IV-FORMULATION-COMMIT
         latest non-superseded line = PASS (Option-A supersession chain,
         gate-verdicts.md §"Option A"); branch-iv-canonical.md contains the
         retirement + the two successor definitions and ZERO w_0
         occurrences (no w_0 evaluator is defined by the formulation).
    RA-3 successor properties: xi_E_GGE_inv = n_pairs*Delta_BCS/K_base is
         L-INDEPENDENT BY CONSTRUCTION (pinned canonical constants only;
         identity verified 1e-12). R_JK(L) is L-dependent but is a
         STRUCTURALLY DISTINCT functional from the R_JE slot occupant
         (2B path-(c): "the two functionals carry different scaling");
         quantified: f(R_JK(10)) = -0.4307 vs w_0_B = -0.842454, an
         anchor-reproduction failure of ~0.41 in w_0 units (~16 sigma_DR3)
         — R_JK is NOT a drop-in occupant (surrogate-vs-canonical without
         the §(iv-bis) algebraic-distance theorem).
    RA-4 no recombination map: neither branch-iv-canonical.md nor the S86
         commit defines a (R_JK, xi_E_GGE_inv) -> w_0 map; LOCKOUT-E
         forbids post-2026-04-23 redefinition of the branch-iv canonical.
    => route-alpha NOT RECOVERABLE (formulation gap, not lost scripts: all
       archived scripts run; the post-S86 formulation leaves the
       evaluator's L-dependent slot without a defined occupant, and the
       legacy occupant is excluded by this gate's own pre-registration).
    RB-1 the S85-W10 anchor script (s85_w10_r842_physical_anchor_reaudit
         .py) contains NO w_0-unit mapping: -0.842454 enters as the pinned
         constant BRANCH_IV_W0_PRED; the script never references R_JK.
    RB-2 the W10-2 enumeration model w_0 = -1 + 2*xi_eff*mellin/denom maps
         LEGACY SV2 quantities (log-linearly extrapolated at L >= 10), does
         not accept R_JK, and none of its 4 branches reproduces -0.842454.
    => route-beta NOT RECOVERABLE.
  DIAGNOSTIC sensitivity table (the quantitative core of the formulation-
  gap finding; NOT a verdict input): four candidate unpinned recombination
  rules C1..C4 pushed through the CAC produce spreads spanning BOTH the
  PASS band (<= 0.025) and the INFO band ((0.025, 0.050]) — the unpinned
  recombination freedom is DECISION-RELEVANT at the pre-registered
  thresholds, so executing any one choice would set the verdict by an
  execution-time convention selection (PRU Class-8-adjacent freedom).
  Archaeology context row C0 (FORBIDDEN legacy form, computed from the
  archived W10-2 extrapolation record, NOT from any fresh spectral
  evaluation): the legacy evaluator's own value at L=10 is -0.9962,
  ~6.2 sigma_DR3 from the registered anchor — the registered -0.842454 is
  L=5-anchored and is NOT the large-L limit of its own legacy evaluator.

SUBSTITUTION CHAIN (plan §W1-4 item 7; thresholds):
  Definition 1: w_0_B = -0.842454  [SV1 PASS, S85-W10 reaudit PASS]
  Definition 2: CAC: w_0^{B,CAC}(L) := rho_B(L) + offset_B,
                offset_B := w_0_B - rho_B(L_anchor=10)
  Definition 3: spread := max_{L in {8,12}} |w_0^{B,CAC}(L) - w_0^{B,CAC}(10)|
                        = max_{L in {8,12}} |rho_B(L) - rho_B(10)|
                (offset cancels; no anchor-tuning freedom survives)
  Definition 4: sigma_DR3_fiducial = 0.025  [S69 master]
  Thresholds:   PASS  iff spread <= 0.025
                INFO  iff 0.025 < spread <= 0.050
                FAIL  iff spread > 0.050
  Direction:    smaller spread = more stable; PASS direction is <=.
  THIS RUN: rho_B(L) has NO defined post-S86 evaluator (route ladder above)
  -> spread UNCOMPUTABLE -> pre-registered INFO shape (ii).

COMPOSITE: leg-2 verdict gated by leg-1 cleanliness (leg-1 anomaly forces
INFO). Leg-1 clean + leg-2 INFO-(ii) -> composite INFO. NO w0_FW_R842
promotion (Step-2 write-order fires ON PASS only).

Machinery pins (plan §W1-4 item 5): L set {8,10,12}, L_anchor=10,
scheme=zeta (SV1-anchored), convention=CAC-branch-iv-anchored-L10,
publication precision 6 sig figs, cpu-cap-OMP8, deterministic,
regulator pins a_0^{zeta}/a_2^{zeta}/a_4^{zeta} on all Seeley-DeWitt
moment citations.
"""
from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
_SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
sys.path.insert(0, str(_SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403

import hashlib
import json
import re
import time

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# ---------------------------------------------------------------------------
# Identity + pre-registered pins (plan §W1-4)
# ---------------------------------------------------------------------------
SESSION = "100b"                                                    # (local)
GATE_ID = "S100b-W0-BRANCH-RESOLUTION"                              # (local)
SCHEME = "zeta"                                                     # (local) SV1-anchored; no scheme switch (v3 Class-1)
CONVENTION = "CAC-branch-iv-anchored-L10"                           # (local) plan-pinned
L_MAX_TAG = "mixed"                                                 # (local) multi-L gate (precedent: S85-W12-ELIM-1)

L_SCAN = (8, 10, 12)                                                # (local) plan-pinned regulator mesh
L_ANCHOR = 10                                                       # (local) CAC anchor truncation
W_0_B = -0.842454                                                   # (local) registered branch-iv value (decision-rule §1.2; SV1 target)
W_0_A_EXPECT = -0.918                                               # (local) registered PRIMARY value (== w0_FW canonical; checked below)
SPREAD_PASS = 0.025                                                 # (local) = sigma_DR3 fiducial (S69 master)
SPREAD_INFO = 0.050                                                 # (local) = 2 * sigma_DR3
R842_CENTER_W0 = -0.842                                             # (local) mack-9A R_842 center (w_0)
R842_HW_W0 = 0.100                                                  # (local) mack-9A R_842 half-width (w_0)
R842_CENTER_WA = 0.0                                                # (local) R_842 center (w_a)
R842_HW_WA = 0.200                                                  # (local) R_842 half-width (w_a)
REVERSAL_LO = -0.86                                                 # (local) §5 reversal band edge
REVERSAL_HI = -0.83                                                 # (local) §5 reversal band edge
SIGMA_DR3 = 0.025                                                   # (local) DR3 fiducial sigma (S69 master)

# Plan-freeze static input SHA pins (plan §W1-4 item 8 + Input-SHA ledger)
PIN_DECISION_RULE = "da2ba36cc861ddf3d136f7b218c2240c1c675dea391157eefd62c6b4d57ba160"  # (local)
PIN_BRANCH_IV_REG = "3ddbc3424de7a67116439fbdd961494679473c8b0c113053a3b616ff7b816978"  # (local)
PIN_S84_CACHE = "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9"      # (local)
PIN_S85_MOMENTS = "ebdeab300b4306af9c86cde4c6654b34720a7a2f6eb8a49673308b55e72bec27"    # (local)
PIN_S86_COMMIT_AUDIT = "acc751101c8ca6cec920c8fd58198a6a147bc925455f198613002a8e40161049"  # (local) latest-line PASS audit (plan header)

# WP-comparison-table-ONLY record (pre-registered EXCLUSION from selection):
POST_DOVEKIE_WP_TABLE_ONLY = {                                      # (local)
    "w0_post_dovekie": -0.803,        # non-binding 2026 anchor currency (atlas-08 Q37)
    "n_sigma_B_branch_iv": 0.731,     # |B - (-0.803)| / 0.054 register-side echo
    "n_sigma_A_canonical": 2.130,     # |A - (-0.803)| / 0.054 register-side echo
    "NOTE": "register-side anchor currency ONLY; enters NO selection predicate",
}

# Input files (item 8 + the archived-evaluator scripts the route adjudication reads)
F_CANON = _SHARED_DIR / "canonical_constants.py"                    # (local)
F_CACHE = PROJECT_ROOT / "computations/session-84/s84_spectrum_cache_L12_tau019.npz"        # (local)
F_MOMENTS = PROJECT_ROOT / "computations/session-85/s85_w12_elim1_D_K_Lmax_moments.npz"     # (local)
F_RULE = PROJECT_ROOT / "sessions/framework/registry/w0-primary-decision-rule.md"           # (local)
F_BIV = PROJECT_ROOT / "sessions/framework/registry/branch-iv-canonical.md"                 # (local)
F_S84_VERD = PROJECT_ROOT / "computations/session-84/s84_gate_verdicts.txt"                 # (local)
F_S86_VERD = PROJECT_ROOT / "computations/session-86/s86_gate_verdicts.txt"                 # (local)
F_SV1_NPZ = PROJECT_ROOT / "computations/session-84/s84_w1a_w0_sv1.npz"                     # (local)
F_SV1_PY = PROJECT_ROOT / "computations/session-84/s84_w1a_w0_sv1.py"                       # (local)
F_SV2_PY = PROJECT_ROOT / "computations/session-84/s84_w1a_w0_sv2.py"                       # (local)
F_W10_ANCHOR_PY = PROJECT_ROOT / "computations/session-85/s85_w10_r842_physical_anchor_reaudit.py"   # (local)
F_W10_ENUM_PY = PROJECT_ROOT / "computations/session-85/s85_w10_w0_inverted_branch_enumeration.py"   # (local)
F_W10_ENUM_JSON = PROJECT_ROOT / "computations/session-85/s85_w10_w0_inverted_branch_enumeration.json"  # (local)
F_W12_PY = PROJECT_ROOT / "computations/session-85/s85_w12_branch_iv_reaudit_lmax.py"       # (local)

OUT_NPZ = SCRIPT_DIR / "s100b_w0_branch_resolution.npz"             # (local)
OUT_PNG = SCRIPT_DIR / "s100b_w0_branch_resolution.png"             # (local)


# ---------------------------------------------------------------------------
# SHA helpers (template pattern, .claude/templates/script-template.py)
# ---------------------------------------------------------------------------
def sha256_of(p: Path) -> str:
    try:
        return hashlib.sha256(p.read_bytes()).hexdigest()
    except OSError:
        return "<missing>"


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)                                          # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")   # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = script_path.read_bytes()                         # (local)
    canonical_bytes = canonical_path.read_bytes()                   # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"),
                             sort_keys=True).encode("utf-8")        # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def print_verdict_payload(verdict: str, value, audit_sha: str,
                          content_sha: str, companion_note: str = "",
                          extra_rows: list[str] | None = None) -> dict:
    """Emit the verdict PAYLOAD for the agent to pass to emit_verdict
    (race-safe single writer; the script never opens the verdict file)."""
    payload: dict = {
        "session": SESSION,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX_TAG),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = extra_rows
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, indent=2, sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# LEG-1: mechanical re-execution of w0-primary-decision-rule.md §3
# ---------------------------------------------------------------------------
def leg1_mechanical_reexecution(rule_text: str, s86_text: str,
                                pins: dict[str, str]) -> dict:
    print("\n--- LEG-1: mechanical re-execution of the §3 decision rule ---")
    rec: dict = {}                                                  # (local)

    # (i) Pre-flight: decision-rule file bit-identical to plan-freeze pin
    rule_sha = pins["sessions/framework/registry/w0-primary-decision-rule.md"]  # (local)
    rec["rule_sha_matches_plan_pin"] = (rule_sha == PIN_DECISION_RULE)
    print(f"  decision-rule SHA == plan pin: {rec['rule_sha_matches_plan_pin']}")

    # (i) Criterion-4 currency — A's canonical pin stands; B has none.
    #     w0_FW imported from canonical_constants (zeta-anchored Volovik
    #     partition value; a_0^{zeta}-sector provenance, S58).
    rec["w0_FW_value"] = float(w0_FW)                               # canonical import
    rec["w0_FW_equals_minus_0p918"] = bool(abs(w0_FW - W_0_A_EXPECT) == 0.0)
    rec["w0_FW_R842_absent_in_canonical"] = ("w0_FW_R842" not in globals())
    print(f"  C4: w0_FW = {w0_FW} (expect {W_0_A_EXPECT}): "
          f"{rec['w0_FW_equals_minus_0p918']}")
    print(f"  C4: w0_FW_R842 ABSENT from canonical_constants: "
          f"{rec['w0_FW_R842_absent_in_canonical']} "
          f"(B canonical-pin history = 0; no parallel-writer promotion)")

    # (i) Criterion-2 rectangle membership (center -0.842, half-width 0.100)
    offset_A = abs(float(w0_FW) - R842_CENTER_W0)                   # (local)
    offset_B = abs(W_0_B - R842_CENTER_W0)                          # (local)
    rec["offset_A"] = offset_A
    rec["offset_B"] = offset_B
    rec["member_A"] = bool(offset_A <= R842_HW_W0)
    rec["member_B"] = bool(offset_B <= R842_HW_W0)
    print(f"  C2: |A - center| = {offset_A:.6f} <= {R842_HW_W0}: {rec['member_A']}"
          f"  ({offset_A / R842_HW_W0 * 100:.1f}% of half-width)")
    print(f"  C2: |B - center| = {offset_B:.6f} <= {R842_HW_W0}: {rec['member_B']}"
          f"  ({offset_B / R842_HW_W0 * 100:.2f}% of half-width)")

    # (ii) §5 reversal protocol armed unmodified
    m5 = re.search(r"## §5\. Reversibility protocol.*?(?=## §6\.)",
                   rule_text, flags=re.S)                           # (local)
    sec5 = m5.group(0) if m5 else ""                                # (local)
    rec["reversal_band_lo_present"] = ("-0.86" in sec5)
    rec["reversal_band_hi_present"] = ("-0.83" in sec5)
    rec["sigma_dr3_present"] = ("0.025" in sec5)
    rec["locked_machinery_present"] = ("Locked machinery" in sec5)
    rec["reversal_armed_unmodified"] = bool(
        rec["rule_sha_matches_plan_pin"]
        and rec["reversal_band_lo_present"] and rec["reversal_band_hi_present"]
        and rec["sigma_dr3_present"] and rec["locked_machinery_present"]
    )
    print(f"  §5 armed unmodified (SHA + band [-0.86,-0.83] + sigma 0.025 + "
          f"locked machinery): {rec['reversal_armed_unmodified']}")

    # (iii) Selection — PURE function of the two §3 components ONLY.
    #       Falsifiability (Criterion 3) and ALL data-proximity numbers are
    #       structurally excluded (not in the function signature).
    def select_primary(history_priority_A: bool, member_A: bool,
                       member_B: bool, structural_promotion_B: bool) -> str:
        # §3: PRIMARY = candidate satisfying (registry-history-priority AND
        # DR3-rectangle-membership) = A unless a structural argument
        # promotes B. B's membership alone is non-discriminating.
        if structural_promotion_B:
            return "B"
        if history_priority_A and member_A:
            return "A"
        return "UNRESOLVED"

    history_priority_A = bool(
        rec["w0_FW_equals_minus_0p918"]
        and rec["w0_FW_R842_absent_in_canonical"]
    )                                                               # (local) A: 28+ sessions (S58->S100b); B: 0 canonical pins
    structural_promotion_B = False                                  # (local) no registered structural promotion of B (registry survey 2026-06-07)
    primary_recomputed = select_primary(
        history_priority_A, rec["member_A"], rec["member_B"],
        structural_promotion_B,
    )                                                               # (local)
    rec["history_priority_A"] = history_priority_A
    rec["structural_promotion_B"] = structural_promotion_B
    rec["primary_recomputed"] = primary_recomputed
    print(f"  §3 selection (inputs: history-priority, rectangle-membership "
          f"ONLY): PRIMARY = {primary_recomputed}")

    # (iii) Registered designation from S86 verdict file (read-only anchor)
    m_res = re.search(
        r"^S86-W0-PRIMARY-VALUE-RESOLVE: (\w+) -- value='([^']*)'",
        s86_text, flags=re.M)                                       # (local)
    rec["registered_resolve_verdict"] = m_res.group(1) if m_res else "<absent>"
    rec["registered_resolve_value"] = m_res.group(2) if m_res else "<absent>"
    rec["registered_matches_recomputed"] = bool(
        rec["registered_resolve_verdict"] == "PASS"
        and rec["registered_resolve_value"] == "PRIMARY=A=-0.918"
        and primary_recomputed == "A"
    )
    print(f"  registered: {rec['registered_resolve_verdict']} "
          f"'{rec['registered_resolve_value']}' ; recomputed PRIMARY="
          f"{primary_recomputed} -> match: {rec['registered_matches_recomputed']}")

    rec["leg1_clean"] = bool(
        rec["reversal_armed_unmodified"]
        and rec["registered_matches_recomputed"]
        and rec["member_A"] and rec["member_B"]
    )
    print(f"  LEG-1 CLEAN: {rec['leg1_clean']}")
    return rec


# ---------------------------------------------------------------------------
# LEG-2: route adjudication + diagnostics
# ---------------------------------------------------------------------------
def f_branch_iv(R: float, c_J: float, P_G_z: float, rho_G_z: float) -> float:
    """EXACT reduction of the SV1 branch-(iv) closed form: the w_0 value
    depends on (xi_J, xi_E_GGE) ONLY through the dressing ratio R."""
    return (-c_J * R + P_G_z) / (c_J * R + rho_G_z)


def weyl_dim_su3(p: int, q: int) -> int:
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def casimir_su3(p: int, q: int) -> float:
    return (p * p + p * q + q * q + 3 * (p + q)) / 3.0


def schematic_moments(L: int) -> tuple[float, float]:
    """a_2^{zeta}, a_4^{zeta} via the multiplicity-weighted SU(3) Casimir
    schematic (S85-W12-ELIM-1 methodology) — INDEPENDENT recomputation used
    to cross-check the loaded moments npz (not load-and-compare-to-self)."""
    a2 = 0.0                                                        # (local)
    a4 = 0.0                                                        # (local)
    for p in range(L + 1):
        for q in range(L + 1):
            if (p == 0 and q == 0) or (p + q > L):
                continue
            d = weyl_dim_su3(p, q)                                  # (local)
            c = casimir_su3(p, q)                                   # (local)
            a2 += d / c
            a4 += d / (c * c)
    return a2 / Vol_SU3_Haar, a4 / Vol_SU3_Haar


def cache_moments(sector_evals: dict, L: int) -> tuple[float, float]:
    """Cache-moment-layer a_2^{zeta}, a_4^{zeta} from the REAL D_K spectrum
    (s84 L12 cache): a_n = sum d * |lam|^{-n} / Vol. DIAGNOSTIC ONLY —
    documents the atlas-row vs cache-moment layer split per
    substrate-first-canonical-sourcing.md §(ii.A)."""
    s2 = 0.0                                                        # (local)
    s4 = 0.0                                                        # (local)
    for (p, q), info in sector_evals.items():
        if info["level"] > L or (p == 0 and q == 0):
            continue
        lam = np.asarray(info["abs_evals"], dtype=np.float64)       # (local)
        lam = lam[lam > 0]                                          # (local)
        d = float(info["dim"])                                      # (local)
        s2 += d * float(np.sum(lam ** (-2.0)))
        s4 += d * float(np.sum(lam ** (-4.0)))
    return s2 / Vol_SU3_Haar, s4 / Vol_SU3_Haar


def leg2_route_adjudication(pins: dict[str, str]) -> dict:
    print("\n--- LEG-2: branch-iv L_max stability — route adjudication ---")
    rec: dict = {}                                                  # (local)

    # ---- Static-pin verification (plan item 8) ----
    rec["cache_sha_ok"] = (pins["computations/session-84/s84_spectrum_cache_L12_tau019.npz"] == PIN_S84_CACHE)
    rec["moments_sha_ok"] = (pins["computations/session-85/s85_w12_elim1_D_K_Lmax_moments.npz"] == PIN_S85_MOMENTS)
    rec["biv_sha_ok"] = (pins["sessions/framework/registry/branch-iv-canonical.md"] == PIN_BRANCH_IV_REG)
    print(f"  static pins: cache {rec['cache_sha_ok']}, moments "
          f"{rec['moments_sha_ok']}, branch-iv registry {rec['biv_sha_ok']}")

    # ---- RA-1: archived-evaluator recovery + exact f-reduction ----
    sv1 = np.load(F_SV1_NPZ, allow_pickle=True)                     # (local)
    xi_J_sv1 = float(sv1["xi_J"])                                   # (local) 0.008911
    xi_E_sv1 = float(sv1["xi_E_GGE"])                               # (local) 0.019646 (L=5 legacy anchor)
    F_J_zeta = float(sv1["F_Josephson_zeta"])                       # (local) -336.641 M_KK (S58)
    rho_G_z = float(sv1["rho_GGE_zeta"])                            # (local) 1.709 M_KK (S57 cc_sign)
    P_G_z = float(sv1["P_GGE_zeta"])                                # (local) -0.688 M_KK (S57 cc_sign)
    w0_sv1_npz = float(sv1["w_0_iv"])                               # (local) -0.8424542759870739 full float64
    c_J = abs(F_J_zeta) / float(N_cells)                            # (local) = 10.52003125

    # Direct closed-form recomputation (SV1 Step 2-3)
    rho_J = abs(xi_J_sv1 * F_J_zeta) / float(N_cells)               # (local)
    w0_direct = (-rho_J + xi_E_sv1 * P_G_z) / (rho_J + xi_E_sv1 * rho_G_z)  # (local)
    R_sv1 = xi_J_sv1 / xi_E_sv1                                     # (local) the dressing-ratio slot occupant (legacy R_JE at L=5)
    w0_via_f = f_branch_iv(R_sv1, c_J, P_G_z, rho_G_z)              # (local)

    rec["w0_direct"] = w0_direct
    rec["w0_via_f"] = w0_via_f
    rec["R_sv1"] = R_sv1
    rec["c_J"] = c_J
    rec["RA1_reproduces_npz"] = bool(abs(w0_direct - w0_sv1_npz) < 1e-12)
    rec["RA1_reproduces_registered"] = bool(abs(w0_direct - W_0_B) < 1e-5)
    rec["RA1_f_reduction_exact"] = bool(abs(w0_via_f - w0_direct) < 1e-12)
    print(f"  RA-1: closed form -> {w0_direct:.10f} (npz {w0_sv1_npz:.10f}; "
          f"registered {W_0_B}); reproduce_npz={rec['RA1_reproduces_npz']}, "
          f"reproduce_registered={rec['RA1_reproduces_registered']}")
    print(f"  RA-1: f-reduction w_0 = f(R) with R = xi_J/xi_E_GGE = "
          f"{R_sv1:.6f}: exact to 1e-12 = {rec['RA1_f_reduction_exact']}")
    print(f"  RA-1: SOLE L-dependent input of the archived evaluator = the "
          f"dressing-ratio slot R (legacy single-tag R_JE) — RETIRED by S86")

    # ---- RA-2: post-S86 formulation facts ----
    s86_text = F_S86_VERD.read_text(encoding="utf-8")               # (local)
    commit_lines = re.findall(
        r"^S86-BRANCH-IV-FORMULATION-COMMIT: (\w+) -- .*?audit_sha256=([a-f0-9]{64})",
        s86_text, flags=re.M)                                       # (local)
    # Option-A retroactive canonicalization: latest non-superseded line wins
    rec["commit_chain"] = [(v, a[:16]) for v, a in commit_lines]
    rec["commit_latest_verdict"] = commit_lines[-1][0] if commit_lines else "<absent>"
    rec["commit_latest_audit"] = commit_lines[-1][1] if commit_lines else "<absent>"
    rec["RA2_commit_latest_PASS"] = bool(
        rec["commit_latest_verdict"] == "PASS"
        and rec["commit_latest_audit"] == PIN_S86_COMMIT_AUDIT
    )
    biv_text = F_BIV.read_text(encoding="utf-8")                    # (local)
    rec["RA2_retirement_present"] = ("RETIRED" in biv_text and "R_JE" in biv_text)
    rec["RA2_w0_occurrences_in_formulation"] = len(
        re.findall(r"w_0|w0", biv_text))                            # (local)
    rec["RA2_formulation_defines_no_w0"] = (rec["RA2_w0_occurrences_in_formulation"] == 0)
    print(f"  RA-2: commit chain {rec['commit_chain']} -> latest "
          f"{rec['commit_latest_verdict']} (audit pin match: "
          f"{rec['RA2_commit_latest_PASS']})")
    print(f"  RA-2: branch-iv-canonical.md w_0 occurrences = "
          f"{rec['RA2_w0_occurrences_in_formulation']} -> formulation defines "
          f"NO w_0 evaluator: {rec['RA2_formulation_defines_no_w0']}")

    # ---- RA-3: successor properties ----
    # Distance-1 successor: L-INDEPENDENT by construction (pinned constants)
    xi_inv_identity = float(n_pairs) * float(Delta_BCS) / float(K_base)  # (local)
    rec["xi_E_GGE_inv_canonical"] = float(xi_E_GGE_inv)             # canonical import
    rec["RA3_xi_inv_identity_ok"] = bool(
        abs(xi_inv_identity - float(xi_E_GGE_inv)) / float(xi_E_GGE_inv) < 1e-12)
    print(f"  RA-3: xi_E_GGE_inv = n_pairs*Delta_BCS/K_base = "
          f"{xi_inv_identity:.12f} vs canonical {float(xi_E_GGE_inv):.12f} "
          f"(identity 1e-12: {rec['RA3_xi_inv_identity_ok']}) -> "
          f"L-INDEPENDENT by construction (constants only)")

    # Distance-2 successor: loaded trajectory + independent recomputation
    mom = np.load(F_MOMENTS, allow_pickle=True)                     # (local)
    L_loaded = [int(x) for x in mom["L_max"]]                       # (local)
    R_JK_traj = np.asarray(mom["R_JK"], dtype=np.float64)           # (local)
    a2_loaded = np.asarray(mom["a_2"], dtype=np.float64)            # (local)
    a4_loaded = np.asarray(mom["a_4"], dtype=np.float64)            # (local)
    rec["L_loaded"] = L_loaded
    rec["R_JK_traj"] = R_JK_traj.tolist()
    rec["RA3_L_set_matches_plan"] = (tuple(L_loaded) == L_SCAN)
    rec["RA3_RJK_L10_matches_canonical"] = bool(
        abs(R_JK_traj[1] - float(R_JK)) / float(R_JK) < 1e-12)      # canonical R_JK (L=10 anchor, S86 commit)
    # Independent Casimir-schematic recomputation (a_2^{zeta}, a_4^{zeta})
    pref = float(Delta_BCS) ** 2 / float(K_base)                    # (local) L-independent prefactor
    schem_ok = True                                                 # (local)
    for i, L in enumerate(L_loaded):
        a2_i, a4_i = schematic_moments(L)                           # (local)
        r_i = (a4_i / a2_i) * pref                                  # (local)
        ok = (abs(a2_i - a2_loaded[i]) / a2_loaded[i] < 1e-7
              and abs(a4_i - a4_loaded[i]) / a4_loaded[i] < 1e-7
              and abs(r_i - R_JK_traj[i]) / R_JK_traj[i] < 1e-6)    # (local)
        schem_ok = schem_ok and ok
        print(f"  RA-3: L={L}: a_2^(zeta)={a2_i:.8f} a_4^(zeta)={a4_i:.8f} "
              f"R_JK={r_i:.8f} (loaded {R_JK_traj[i]:.8f}) recompute-ok={ok}")
    rec["RA3_schematic_recompute_ok"] = bool(schem_ok)

    # Anchor-reproduction failure of the R_JK drop-in (surrogate test)
    f_RJK_L10 = f_branch_iv(float(R_JK_traj[1]), c_J, P_G_z, rho_G_z)  # (local)
    rec["f_of_RJK_L10"] = f_RJK_L10
    rec["RA3_anchor_gap_w0_units"] = abs(f_RJK_L10 - W_0_B)
    rec["RA3_anchor_gap_sigma"] = rec["RA3_anchor_gap_w0_units"] / SIGMA_DR3
    print(f"  RA-3: f(R_JK(10)) = {f_RJK_L10:.6f} vs registered {W_0_B} -> "
          f"anchor gap {rec['RA3_anchor_gap_w0_units']:.6f} w_0-units = "
          f"{rec['RA3_anchor_gap_sigma']:.1f} sigma_DR3 -> R_JK is NOT a "
          f"drop-in occupant of the R_JE slot (structurally distinct "
          f"functional; 2B path-(c): different scaling)")

    # ---- RA-4: no recombination map registered ----
    # (RA-2 already established zero w_0 occurrences in the formulation
    # registry; LOCKOUT-E forbids post-2026-04-23 redefinition.)
    rec["RA4_no_recombination_map"] = rec["RA2_formulation_defines_no_w0"]

    rec["route_alpha_recoverable"] = bool(
        not (rec["RA2_formulation_defines_no_w0"]
             and rec["RA4_no_recombination_map"])
    )
    print(f"  => ROUTE-ALPHA recoverable: {rec['route_alpha_recoverable']} "
          f"(formulation gap: the evaluator's sole L-dependent slot has no "
          f"post-S86 occupant; legacy occupant excluded by pre-registration)")

    # ---- RB-1: S85-W10 anchor script contains no w_0-unit mapping ----
    w10_anchor_text = F_W10_ANCHOR_PY.read_text(encoding="utf-8")   # (local)
    rec["RB1_anchor_script_has_RJK"] = ("R_JK" in w10_anchor_text)
    rec["RB1_anchor_value_is_pinned_constant"] = (
        "BRANCH_IV_W0_PRED = -0.842454" in w10_anchor_text)
    rec["RB1_no_mapping"] = bool(
        (not rec["RB1_anchor_script_has_RJK"])
        and rec["RB1_anchor_value_is_pinned_constant"])
    print(f"  RB-1: W10 anchor script references R_JK: "
          f"{rec['RB1_anchor_script_has_RJK']}; -0.842454 enters as pinned "
          f"constant: {rec['RB1_anchor_value_is_pinned_constant']} -> no "
          f"w_0-unit mapping: {rec['RB1_no_mapping']}")

    # ---- RB-2: W10-2 enumeration model is legacy-family, not an R_JK map ----
    w10_enum = json.loads(F_W10_ENUM_JSON.read_text(encoding="utf-8"))  # (local)
    enum_w0_all = [w for b in w10_enum["branches"].values()
                   for w in b["w_0"]]                               # (local)
    rec["RB2_min_distance_to_registered"] = float(
        min(abs(w - W_0_B) for w in enum_w0_all))
    rec["RB2_model_inputs_legacy"] = (
        "xi_E_GGE" in w10_enum["model_description"])
    rec["RB2_extrapolated_R_JE_target"] = [
        float(x) for x in w10_enum["target"]["R_JE"]]               # (local) archaeology: 5.148, 25.658, 127.880
    rec["RB2_no_mapping"] = bool(
        rec["RB2_model_inputs_legacy"]
        and rec["RB2_min_distance_to_registered"] > 0.019)
    print(f"  RB-2: W10-2 definitional model inputs are legacy SV2 "
          f"quantities (extrapolated at L>=10): "
          f"{rec['RB2_model_inputs_legacy']}; min |branch w_0 - (-0.842454)|"
          f" = {rec['RB2_min_distance_to_registered']:.6f} -> not a "
          f"branch-(iv) w_0-unit mapping: {rec['RB2_no_mapping']}")

    rec["route_beta_recoverable"] = bool(
        not (rec["RB1_no_mapping"] and rec["RB2_no_mapping"]))
    print(f"  => ROUTE-BETA recoverable: {rec['route_beta_recoverable']}")

    # ---- SV archaeology record (INPUT evidence, not the test) ----
    s84_text = F_S84_VERD.read_text(encoding="utf-8")               # (local)
    sv1_line = re.search(r"^S84-W0-REGULATOR-RESOLUTION-SV1: .*$",
                         s84_text, flags=re.M)                      # (local)
    sv2_line = re.search(r"^S84-W0-REGULATOR-RESOLUTION-SV2: .*$",
                         s84_text, flags=re.M)                      # (local)
    rec["sv1_line"] = sv1_line.group(0) if sv1_line else "<absent>"
    rec["sv2_line"] = sv2_line.group(0) if sv2_line else "<absent>"
    rec["sv_archaeology_ok"] = bool(
        "PASS" in rec["sv1_line"] and "value=-0.842454" in rec["sv1_line"]
        and "L_max=5" in rec["sv1_line"]
        and "FAIL" in rec["sv2_line"] and "value=10.077109" in rec["sv2_line"]
        and "L_max=8" in rec["sv2_line"])
    print(f"  SV archaeology verified (SV1 PASS @L=5 / SV2 FAIL @L=8 legacy "
          f"drift record): {rec['sv_archaeology_ok']}")

    # ---- DIAGNOSTIC sensitivity table (NOT a verdict input) ----
    print("\n  --- DIAGNOSTIC: candidate unpinned recombinations through the "
          "CAC (decision-relevance of the formulation gap) ---")
    L_arr = np.array(L_loaded, dtype=int)                           # (local)
    cands: dict[str, dict] = {}                                     # (local)

    def cac_record(name: str, rho: np.ndarray, formula: str) -> dict:
        offset = W_0_B - rho[1]                                     # (local) offset_B := w_0_B - rho_B(L_anchor)
        cac = rho + offset                                          # (local)
        spread = float(max(abs(cac[0] - cac[1]), abs(cac[2] - cac[1])))  # (local) offset cancels: = max|rho(L)-rho(10)|
        band = ("PASS" if spread <= SPREAD_PASS
                else ("INFO" if spread <= SPREAD_INFO else "FAIL"))  # (local)
        d = dict(formula=formula, rho=rho.tolist(), offset=float(offset),
                 cac=cac.tolist(), spread=spread, band=band)
        print(f"    {name}: rho={np.array2string(rho, precision=6)} "
              f"offset={offset:+.6f} spread={spread:.6f} -> {band}-band")
        return d

    R10 = float(R_JK_traj[1])                                       # (local)
    cands["C1_raw_RJK"] = cac_record(
        "C1 f(R_JK(L)) raw           ",
        np.array([f_branch_iv(float(r), c_J, P_G_z, rho_G_z)
                  for r in R_JK_traj]),
        "rho_B(L) = f(R_JK(L))")
    cands["C2_relative_trajectory"] = cac_record(
        "C2 f(R_sv1*R_JK(L)/R_JK(10))",
        np.array([f_branch_iv(R_sv1 * float(r) / R10, c_J, P_G_z, rho_G_z)
                  for r in R_JK_traj]),
        "rho_B(L) = f(R_sv1 * R_JK(L)/R_JK(10))")
    cands["C3_additive"] = cac_record(
        "C3 f(R_sv1 + dR_JK(L))      ",
        np.array([f_branch_iv(R_sv1 + (float(r) - R10), c_J, P_G_z, rho_G_z)
                  for r in R_JK_traj]),
        "rho_B(L) = f(R_sv1 + (R_JK(L) - R_JK(10)))")
    cands["C4_definitional_shoehorn"] = cac_record(
        "C4 -1 + 2*R_JK(L)           ",
        np.array([-1.0 + 2.0 * float(r) for r in R_JK_traj]),
        "rho_B(L) = -1 + 2*R_JK(L)  (W10-2 model shoehorn)")

    spreads = [c["spread"] for c in cands.values()]                 # (local)
    bands = {c["band"] for c in cands.values()}                     # (local)
    rec["diag_spread_min"] = float(min(spreads))
    rec["diag_spread_max"] = float(max(spreads))
    rec["diag_decision_relevant"] = bool(len(bands) > 1)
    print(f"    span: [{rec['diag_spread_min']:.6f}, "
          f"{rec['diag_spread_max']:.6f}] crosses the {SPREAD_PASS} "
          f"boundary -> bands {sorted(bands)} -> unpinned recombination "
          f"freedom is DECISION-RELEVANT: {rec['diag_decision_relevant']}")

    # Archaeology context row C0 (FORBIDDEN legacy form — context only;
    # numbers pushed from the ARCHIVED W10-2 extrapolation record, no fresh
    # spectral evaluation of the retired tag):
    R_JE_ext = rec["RB2_extrapolated_R_JE_target"]                  # (local)
    rho_C0 = np.array([f_branch_iv(float(r), c_J, P_G_z, rho_G_z)
                       for r in R_JE_ext])                          # (local)
    rec["C0_legacy_rho"] = rho_C0.tolist()
    rec["C0_legacy_anchor_gap_sigma"] = float(
        abs(rho_C0[1] - W_0_B) / SIGMA_DR3)
    print(f"    C0 (FORBIDDEN legacy, archaeology context): "
          f"rho={np.array2string(rho_C0, precision=6)} -> the legacy "
          f"evaluator's own L=10 value sits "
          f"{rec['C0_legacy_anchor_gap_sigma']:.1f} sigma_DR3 from the "
          f"registered anchor (the -0.842454 is L=5-anchored)")
    cands["C0_FORBIDDEN_legacy_context"] = dict(
        formula="rho_B(L) = f(R_JE_extrapolated(L))  [EXCLUDED by pre-registration]",
        rho=rho_C0.tolist(), offset=float("nan"), cac=[float("nan")] * 3,
        spread=float(max(abs(rho_C0[0] - rho_C0[1]),
                         abs(rho_C0[2] - rho_C0[1]))),
        band="EXCLUDED")
    rec["candidates"] = cands

    # ---- DIAGNOSTIC cache-moment layer (real D_K spectrum, L12 cache) ----
    print("\n  --- DIAGNOSTIC: cache-moment-layer a_2^(zeta)/a_4^(zeta) from "
          "the s84 L12 spectrum cache (layer split per §(ii.A)) ---")
    cache = np.load(F_CACHE, allow_pickle=True)                     # (local)
    sector_evals = cache["sector_evals"].item()                     # (local)
    cache_rows = []                                                 # (local)
    for L in L_loaded:
        a2_c, a4_c = cache_moments(sector_evals, L)                 # (local)
        r_c = (a4_c / a2_c) * pref                                  # (local)
        cache_rows.append((L, a2_c, a4_c, r_c))
        print(f"    L={L}: a_2^(zeta,cache)={a2_c:.6f} "
              f"a_4^(zeta,cache)={a4_c:.6f} R_JK^(cache)={r_c:.8f}")
    rec["cache_layer_rows"] = [[float(x) for x in row] for row in cache_rows]
    r_cache = np.array([row[3] for row in cache_rows])              # (local)
    rec["cache_layer_monotone_decreasing"] = bool(
        r_cache[0] > r_cache[1] > r_cache[2])
    print(f"    cache-layer R_JK monotone decreasing (matches schematic "
          f"direction): {rec['cache_layer_monotone_decreasing']}")

    # ---- Leg-2 verdict per the pre-registered route ladder ----
    if rec["route_alpha_recoverable"] or rec["route_beta_recoverable"]:
        # (not reached on current registry state; kept for determinism)
        rec["leg2_verdict"] = "UNEXPECTED-ROUTE-OPEN"
        rec["route_tag"] = "UNEXPECTED"
    else:
        rec["leg2_verdict"] = "INFO"
        rec["route_tag"] = "NOT-RECOVERABLE"
    rec["canonical_rho_B"] = [float("nan")] * 3   # no defined evaluator
    rec["canonical_offset_B"] = float("nan")
    rec["canonical_cac"] = [float("nan")] * 3
    rec["canonical_spread"] = float("nan")
    rec["evaluator_recoverable"] = False
    print(f"\n  LEG-2 verdict: {rec['leg2_verdict']} "
          f"(route={rec['route_tag']}; canonical spread UNCOMPUTABLE — "
          f"stability UNVERIFIED, formulation-gap record)")
    return rec


# ---------------------------------------------------------------------------
# Plot
# ---------------------------------------------------------------------------
def make_plot(leg2: dict) -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    L_arr = np.array(leg2["L_loaded"], dtype=float)                 # (local)

    # Panel 1: candidate CAC series vs the pre-registered bands
    ax1.axhline(W_0_B, color="k", lw=1.4,
                label=f"anchor w_0_B = {W_0_B}")
    ax1.axhspan(W_0_B - SPREAD_PASS, W_0_B + SPREAD_PASS,
                color="green", alpha=0.12,
                label="PASS band ±0.025 (= σ_DR3)")
    ax1.axhspan(W_0_B - SPREAD_INFO, W_0_B + SPREAD_INFO,
                color="orange", alpha=0.08,
                label="INFO band ±0.050 (= 2σ_DR3)")
    colors = {"C1_raw_RJK": "#1f77b4", "C2_relative_trajectory": "#d62728",
              "C3_additive": "#2ca02c", "C4_definitional_shoehorn": "#9467bd"}
    for name, c in leg2["candidates"].items():
        if name.startswith("C0"):
            continue
        cac = np.array(c["cac"], dtype=float)                       # (local)
        ax1.plot(L_arr, cac, "o-", color=colors.get(name, "gray"),
                 label=f"{name.split('_')[0]}: spread={c['spread']:.6f} "
                       f"[{c['band']}]")
    ax1.set_xlabel(r"$L_{\max}$")
    ax1.set_ylabel(r"$w_0^{B,\mathrm{CAC}}(L)$  (candidate, DIAGNOSTIC)")
    ax1.set_xticks(L_arr)
    ax1.set_title("DIAGNOSTIC candidate recombinations through the CAC\n"
                  "(no canonical post-S86 evaluator exists — INFO: "
                  "evaluator-not-recoverable)")
    ax1.legend(fontsize=8, loc="lower right")
    ax1.grid(True, alpha=0.3)
    txt = (f"R_JK trajectory (schematic): "
           f"{', '.join(f'{r:.8f}' for r in leg2['R_JK_traj'])}\n"
           f"candidate spread span [{leg2['diag_spread_min']:.6f}, "
           f"{leg2['diag_spread_max']:.6f}] crosses 0.025 -> "
           f"recombination freedom DECISION-RELEVANT")                # (local)
    ax1.text(0.02, 0.02, txt, transform=ax1.transAxes, fontsize=7.5,
             va="bottom", family="monospace")

    # Panel 2: R_842 rectangle inset with both candidates + reversal band
    ax2.add_patch(Rectangle((R842_CENTER_W0 - R842_HW_W0,
                             R842_CENTER_WA - R842_HW_WA),
                            2 * R842_HW_W0, 2 * R842_HW_WA,
                            fill=False, edgecolor="k", lw=1.5,
                            label="R_842 (LOCKOUT-C)"))
    ax2.axvspan(REVERSAL_LO, REVERSAL_HI, color="red", alpha=0.10,
                label="§5 reversal band [-0.86, -0.83]")
    ax2.plot([float(w0_FW)], [0.0], "s", ms=11, color="#1f77b4",
             label=f"A = {float(w0_FW)} (PRIMARY, re-confirmed)")
    ax2.plot([W_0_B], [0.0], "D", ms=11, color="#d62728",
             label=f"B = {W_0_B} (SECONDARY; L-stability UNVERIFIED)")
    ax2.axvline(-1.0, color="gray", ls=":", lw=1, label="ΛCDM w_0 = -1")
    ax2.set_xlim(-1.05, -0.70)
    ax2.set_ylim(-0.30, 0.30)
    ax2.set_xlabel(r"$w_0$")
    ax2.set_ylabel(r"$w_a$")
    ax2.set_title("R_842 rectangle — leg-1 mechanical re-execution\n"
                  "PRIMARY = A by (registry-history ∧ rectangle-membership); "
                  "data-proximity EXCLUDED")
    ax2.legend(fontsize=8, loc="upper left")
    ax2.grid(True, alpha=0.3)

    fig.suptitle(f"{GATE_ID} — leg-1 CLEAN; leg-2 INFO "
                 f"(branch-iv-w0-L-evaluator-not-recoverable)", fontsize=11)
    plt.tight_layout(rect=(0, 0, 1, 0.95))
    plt.savefig(OUT_PNG, dpi=120)
    plt.close(fig)
    print(f"\nSaved plot: {OUT_PNG}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()                                                # (local)
    input_files = [
        F_CANON, F_CACHE, F_MOMENTS, F_RULE, F_BIV, F_S84_VERD,
        F_S86_VERD, F_SV1_NPZ, F_SV1_PY, F_SV2_PY, F_W10_ANCHOR_PY,
        F_W10_ENUM_PY, F_W10_ENUM_JSON, F_W12_PY,
    ]                                                               # (local)
    pins = log_input_pins(input_files)                              # (local)

    rule_text = F_RULE.read_text(encoding="utf-8")                  # (local)
    s86_text = F_S86_VERD.read_text(encoding="utf-8")               # (local)

    leg1 = leg1_mechanical_reexecution(rule_text, s86_text, pins)   # (local)
    leg2 = leg2_route_adjudication(pins)                            # (local)

    # Composite: leg-2 verdict gated by leg-1 cleanliness
    if not leg1["leg1_clean"]:
        composite = "INFO"                                          # (local) leg-1 anomaly forces INFO (shape iii)
        info_shape = "iii-leg1-anomaly"                             # (local)
    elif leg2["leg2_verdict"] == "INFO":
        composite = "INFO"                                          # (local) shape (ii)
        info_shape = "ii-evaluator-not-recoverable"                 # (local)
    else:
        composite = leg2["leg2_verdict"]                            # (local)
        info_shape = "n/a"                                          # (local)

    print(f"\n=== COMPOSITE: {composite} (INFO shape: {info_shape}) ===")
    print(f"  NO w0_FW_R842 promotion (Step-2 write-order fires ON PASS only)")

    # ---- npz (plan-required fields + adjudication record) ----
    cand_json = json.dumps(leg2["candidates"], sort_keys=True)      # (local)
    np.savez(
        OUT_NPZ,
        # canonical leg-2 slots (NaN: no defined post-S86 evaluator)
        rho_B=np.array(leg2["canonical_rho_B"]),
        offset_B=np.float64(leg2["canonical_offset_B"]),
        cac_series=np.array(leg2["canonical_cac"]),
        spread=np.float64(leg2["canonical_spread"]),
        evaluator_recoverable=np.bool_(leg2["evaluator_recoverable"]),
        route_tag=np.str_(leg2["route_tag"]),
        # pre-registered thresholds + pins
        L_scan=np.array(L_SCAN), L_anchor=np.int64(L_ANCHOR),
        w_0_B=np.float64(W_0_B), sigma_DR3=np.float64(SIGMA_DR3),
        spread_pass=np.float64(SPREAD_PASS), spread_info=np.float64(SPREAD_INFO),
        # leg-1 record
        leg1_clean=np.bool_(leg1["leg1_clean"]),
        primary_recomputed=np.str_(leg1["primary_recomputed"]),
        registered_resolve_value=np.str_(leg1["registered_resolve_value"]),
        offset_A_rect=np.float64(leg1["offset_A"]),
        offset_B_rect=np.float64(leg1["offset_B"]),
        member_A=np.bool_(leg1["member_A"]), member_B=np.bool_(leg1["member_B"]),
        reversal_armed=np.bool_(leg1["reversal_armed_unmodified"]),
        w0_FW_value=np.float64(leg1["w0_FW_value"]),
        w0_FW_R842_absent=np.bool_(leg1["w0_FW_R842_absent_in_canonical"]),
        post_dovekie_wp_table_only=np.str_(json.dumps(POST_DOVEKIE_WP_TABLE_ONLY)),
        # leg-2 adjudication record
        route_alpha_recoverable=np.bool_(leg2["route_alpha_recoverable"]),
        route_beta_recoverable=np.bool_(leg2["route_beta_recoverable"]),
        R_JK_trajectory=np.array(leg2["R_JK_traj"]),
        f_of_RJK_L10=np.float64(leg2["f_of_RJK_L10"]),
        anchor_gap_sigma=np.float64(leg2["RA3_anchor_gap_sigma"]),
        R_sv1=np.float64(leg2["R_sv1"]), c_J=np.float64(leg2["c_J"]),
        w0_direct=np.float64(leg2["w0_direct"]),
        w0_via_f=np.float64(leg2["w0_via_f"]),
        candidates_json=np.str_(cand_json),
        diag_spread_min=np.float64(leg2["diag_spread_min"]),
        diag_spread_max=np.float64(leg2["diag_spread_max"]),
        diag_decision_relevant=np.bool_(leg2["diag_decision_relevant"]),
        C0_legacy_rho=np.array(leg2["C0_legacy_rho"]),
        C0_legacy_anchor_gap_sigma=np.float64(leg2["C0_legacy_anchor_gap_sigma"]),
        cache_layer_rows=np.array(leg2["cache_layer_rows"]),
        # SV archaeology record
        sv1_line=np.str_(leg2["sv1_line"]), sv2_line=np.str_(leg2["sv2_line"]),
        sv_archaeology_ok=np.bool_(leg2["sv_archaeology_ok"]),
        commit_latest_verdict=np.str_(leg2["commit_latest_verdict"]),
        composite=np.str_(composite), info_shape=np.str_(info_shape),
    )
    print(f"Saved npz: {OUT_NPZ}")

    make_plot(leg2)

    # ---- Dual-SHA over the input-pin map (plan item 6: pinmap carries
    #      CAC pins, L set, route tag, leg-1 component pins) ----
    pins_with_meta = dict(pins)                                     # (local)
    pins_with_meta["_gate_id"] = GATE_ID
    pins_with_meta["_scheme"] = SCHEME
    pins_with_meta["_convention"] = CONVENTION
    pins_with_meta["_L_set"] = "8,10,12"
    pins_with_meta["_L_anchor"] = str(L_ANCHOR)
    pins_with_meta["_CAC_anchor_value"] = f"{W_0_B}"
    pins_with_meta["_spread_thresholds"] = f"{SPREAD_PASS},{SPREAD_INFO}"
    pins_with_meta["_route_tag"] = leg2["route_tag"]
    pins_with_meta["_leg1_components"] = (
        "registry-history-priority+R842-membership;"
        "falsifiability-and-data-proximity-EXCLUDED")
    audit_sha, content_sha = compute_dual_sha(
        Path(__file__).resolve(), F_CANON, pins_with_meta)          # (local)
    print(f"\naudit_sha256:   {audit_sha}")
    print(f"content_sha256: {content_sha}")

    value_str = (
        "branch-iv-w0-L-evaluator-not-recoverable;"
        f"leg1=clean_PRIMARY=A={float(w0_FW)}_reversal-armed;"
        "route-alpha=post-S86-formulation-defines-no-w0-evaluator_R_JE-slot-vacant;"
        "route-beta=no-w0-unit-mapping-in-S85-W10-anchor-script;"
        f"R_JK_traj=({leg2['R_JK_traj'][0]:.8f},{leg2['R_JK_traj'][1]:.8f},"
        f"{leg2['R_JK_traj'][2]:.8f});"
        f"diag-spread-span=({leg2['diag_spread_min']:.6f},"
        f"{leg2['diag_spread_max']:.6f})_crosses-0.025_decision-relevant"
    )                                                               # (local)
    extra_rows = [
        (f"# regulator_pin: a_0^{{zeta}}/a_2^{{zeta}}/a_4^{{zeta}} on all "
         f"Seeley-DeWitt citations; scheme=zeta SV1-anchored "
         f"# {GATE_ID} regulator-pin row"),
        (f"# route-adjudication: RA1-recovered-archived-evaluator="
         f"{leg2['RA1_reproduces_registered']} RA2-commit-latest-PASS="
         f"{leg2['RA2_commit_latest_PASS']} RA3-anchor-gap="
         f"{leg2['RA3_anchor_gap_sigma']:.1f}sigma RB1-no-map="
         f"{leg2['RB1_no_mapping']} RB2-no-map={leg2['RB2_no_mapping']} "
         f"# {GATE_ID} leg-2 ladder row"),
    ]                                                               # (local)
    print_verdict_payload(
        composite, value_str, audit_sha, content_sha,
        companion_note=("leg-2 INFO shape (ii) per plan §W1-4 rubric; "
                        "stability UNVERIFIED; NO w0_FW_R842 promotion"),
        extra_rows=extra_rows,
    )

    print(f"\n4-tuple: (value='{value_str[:60]}...', scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX_TAG})")
    print(f"=== {GATE_ID}: {composite} (wall {time.time() - t0:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
