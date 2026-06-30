#!/usr/bin/env python3
"""
S107 W4-1 S107-DESI-DR3-WZ-DECISION-RULE — FIRE the frozen S66-era w0/w_a decision rule(s) vs DESI DR3
======================================================================================================

Gate: S107-DESI-DR3-WZ-DECISION-RULE ([SIGN])

This script FIRES the EXISTING pre-registered S66-era w0/w_a decision rule(s).
It AUTHORS NO threshold. Authoring a new threshold (or re-scaling sigma, resizing
R_842, redefining the L4 band post-data) is v3-closure-recovery.md PROHIBITED_ACTIONS
Class 3 and is FORBIDDEN. Every threshold below is LOADED from a frozen registry:
  - L1 survive/fail edges (-0.35, -0.530)  : pre-registered-observations.md line 64 (S67/S68)
  - L2 S60 three-scenario sigma-tree (3.91/2.06/6.33) : pre-registered-observations.md lines 56-60 (S60)
  - L3 R_842 = [-0.942,-0.742] x [-0.2,+0.2] + 7-cell {A1..C2} : S84 W4-44
        (content_sha256 801e4690..., audit_sha256 f6e102fd...; the frozen JSON
         s84_w4_dr3_contingency_fine_grained.json is the registered payload, sourced
         here from pre-registered-observations.md lines 68-90 which carry the same SHAs)
  - L4 reversibility band [-0.86,-0.83] : w0-primary-decision-rule.md §5 (S86 W13-3)
        (audit_sha256 8893fbc2..., content_sha256 51b5584d...)

The frozen S60/S84/S86 rule SHAs ENTER audit_sha256 (audit_discriminators block) so the
rule-fire is pinned to the EXACT armed thresholds; a re-authored threshold would change
audit_sha256 (the Class-3 tripwire).

Two-step falsifier-surface rule-fire:
  STEP 1 (gating input) — DESI DR3 public-release status check:
      (a) pinned local DR3-data file presence (DESI_DR3_NPZ), AND
      (b) a recorded literature/web release-confirmation check (RELEASE_CHECK_* below),
          performed 2026-06-13 by the dispatching agent.
      If NEITHER confirms a public DR3 w0waCDM (w_0, w_a, full covariance) -> STEP 2a.
      If a public DR3 constraint IS available -> STEP 2b.
  STEP 2a (canonical likely outcome, DR3 NOT released) — emit PRE-REG-INC,
      value='blocked_pending_DESI_DR3_release;S66_rule_armed'. All four sub-rules are
      recorded ARMED with frozen thresholds + frozen SHAs. NO sigma-distance computed
      (no measured w_a to compare). Honest blocked-pending-data, NOT a FAIL, NOT INFO.
  STEP 2b (DR3 released) — FIRE L1/L2/L3/L4 mechanically against the loaded (w_0,w_a,Sigma);
      collapse L1/L2/L3 via the [SIGN] 3-tuple per gate-verdicts.md composite-collapse rule.

Output 4-tuple:
  (value=<blocked-string or composite verdict>, scheme=FW, convention=ABSOLUTE, L_max=N/A)

Classification: PHONONIC (the substrate-IS prediction w(z) is the emergent-cosmology image
of the Volovik tracking-vacuum w0_FW=-0.918; DESI measures it IN the FRW container).

RETIRED-GW CAVEAT (v2 §6): the framework's GW-channel falsifiers are RETIRED — walls=0
EXACT (S77/S96); the amplitude leg retired at falsifier-inventory Row #7.audit-3 (S96; peak
GW-detector-sterile, atlas-09 Item-49); falsifier migrated GW->LSS (Rows #71/#72). This gate
cites NO Omega_GW amplitude as a live framework prediction; w(z) is the live surface.

DISCIPLINE
----------
- `from canonical_constants import *` (w0_FW, wa_FW)
- CPU-only, OMP capped to 8 (2x2 covariance solve + scalar set-membership; no >=100x100 linalg)
- Every local/intermediate tagged `# (local)`
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 (script+canonical+pinmap+frozen_rule_shas) + content_sha256 (script) emitted
- 4-tuple printed as the final non-verdict line
- Verdict emitted via the emit_verdict knowledge-MCP tool (race-safe): this script PRINTS
  the payload via print_verdict_payload; the dispatching AGENT calls emit_verdict(**payload).
  The script does NOT write s107_gate_verdicts.txt (raw open("a") is not atomic on Windows).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — CPU thread cap (set BEFORE numpy import; GPU not used — 2x2 solve only)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403  (provides w0_FW, wa_FW)

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
from matplotlib.patches import Rectangle

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S107"                                                   # (local)
GATE_ID = "S107-DESI-DR3-WZ-DECISION-RULE"                         # (local)
SCHEME = "FW"                                                      # (local) framework canonical EoS branch
CONVENTION = "ABSOLUTE"                                            # (local) absolute set-membership + Mahalanobis in Sigma-metric
L_MAX = "N/A"                                                      # (local) observational rule-fire, no D_K truncation

# ---- FROZEN thresholds (LOADED from registries — NOT authored here) --------
L1_SURVIVE_EDGE = -0.35     # (local) FROZEN L1 SURVIVE edge (pre-registered-observations.md line 64, S67/S68)
L1_FAIL_EDGE = -0.530       # (local) FROZEN L1 FAIL edge (same source)
R842_W0_LO = -0.942         # (local) FROZEN R_842 w_0 lower edge (S84 W4-44)
R842_W0_HI = -0.742         # (local) FROZEN R_842 w_0 upper edge (S84 W4-44)
R842_WA_LO = -0.2           # (local) FROZEN R_842 w_a lower edge (S84 W4-44)
R842_WA_HI = 0.2            # (local) FROZEN R_842 w_a upper edge (S84 W4-44)
L4_REVERSAL_LO = -0.86      # (local) FROZEN L4 reversibility-band lower edge (S86 W13-3)
L4_REVERSAL_HI = -0.83      # (local) FROZEN L4 reversibility-band upper edge (S86 W13-3)
S60_SIGMA_A = 3.91          # (local) FROZEN S60 scenario-A FW-exclusion sigma (DR3-PREREGISTER-60)
S60_SIGMA_B = 2.06          # (local) FROZEN S60 scenario-B FW-exclusion sigma
S60_SIGMA_C = 6.33          # (local) FROZEN S60 scenario-C FW-exclusion sigma
DR3_RELEASE_HORIZON = 2027  # (local) documented DR3 data-release horizon (informs STEP-1 expectation; NOT a gate threshold)
TOL = 1e-12                 # (local) float64 set-membership-edge + 2x2 Mahalanobis solve tolerance

# S60 scenario central points (for L2 nearest-scenario locate + the plot) — FROZEN, S60 lines 56-60
S60_SCENARIOS = {                                                  # (local)
    "A": {"w0": -0.75, "wa": -0.73, "sigma": S60_SIGMA_A, "status": "EXCLUDED"},
    "B": {"w0": -0.90, "wa": -0.30, "sigma": S60_SIGMA_B, "status": "SURVIVES"},
    "C": {"w0": -0.65, "wa": -1.00, "sigma": S60_SIGMA_C, "status": "EXCLUDED"},
}

# FROZEN 7-cell {A1..C2} partition (S84 W4-44; pre-registered-observations.md lines 78-86) — LOADED, NOT authored
SEVEN_CELL = [                                                     # (local)
    {"cell": "A1", "w0": (-0.988, -0.942), "wa": (-0.2, 0.2),
     "verdict": "SURVIVE-promote", "scorecard": "corroboration"},
    {"cell": "A2", "w0": (-1.05, -0.988), "wa": (-0.2, 0.2),
     "verdict": "SURVIVE-recal", "scorecard": "corroboration"},
    {"cell": "B1", "w0": (-0.942, -0.742), "wa_split": True,  # [-1.0,-0.2) U (+0.2,+1.0]
     "verdict": "PARTIAL-REFUTE w_a-lock", "scorecard": "refutation (w_a)"},
    {"cell": "B2", "w0": (-0.742, -0.50), "wa": (-0.2, 0.2),
     "verdict": "PARTIAL-REFUTE Volovik-w_0 partition", "scorecard": "refutation (w_0)"},
    {"cell": "B3", "w0": (-0.742, -0.50), "wa": (-0.5, -0.2),
     "verdict": "DUAL-REFUTE partition AND lock", "scorecard": "refutation (dual)"},
    {"cell": "C1", "w0": (-0.742, -0.20), "wa": (-1.5, -0.5),
     "verdict": "STRONG-REFUTE substrate-DE", "scorecard": "refutation (triple)"},
    {"cell": "C2", "w0": (-1.20, -1.05), "wa": None,
     "verdict": "PHANTOM-REFUTE or thaw-REFUTE (impedance audit)", "scorecard": "refutation"},
]

# ---- FROZEN rule SHAs (enter audit_sha256 — Class-3 tripwire) ---------------
# These are the registered content/audit SHAs of the armed sub-rules. Pinning them into
# audit_sha256 means any re-authored threshold changes the gate's audit_sha256.
FROZEN_RULE_SHAS = {                                              # (local)
    # L3 R_842 + 7-cell (S84 W4-44 DR3-7-SCENARIO-TREE)
    "L3_content_sha256": "801e4690eee8e7f4c4152be7701567229a377ab3d23a66a5a39b318469323d6f",
    "L3_audit_sha256":   "f6e102fd5f322dd3f6fa1e4866c6a2f0c425f344d359cf07e37e4d5877cb265e",
    # L4 reversibility band (S86 W13-3 S86-W0-PRIMARY-VALUE-RESOLVE)
    "L4_audit_sha256":   "8893fbc2ee44af27585268b01481eff5560817013ec3e60ae47ee0821ccaaf0a",
    "L4_content_sha256": "51b5584d5d807bc3bdb1b73954f2dcf36768f50b094fc34e50b078f46ffa5f7e",
    # L1 + L2 are line-anchored in pre-registered-observations.md (whose runtime SHA is in the pin map);
    # the source-line anchors are recorded so a registry edit is detectable via the pin-map SHA:
    "L1_source": "pre-registered-observations.md:line64 (S67 DESI-VOLOVIK-67 / S68 W2-C)",
    "L2_source": "pre-registered-observations.md:lines56-60 (S60 DR3-PREREGISTER-60)",
}

# DR2 substitution-chain reference values (for the [SIGN] w_a-outlier-direction note;
# DR2 is the LATEST PUBLIC release — sourced pre-registered-observations.md line 50). These are
# NOT fired into any framework prediction; they establish the registered 2.92-sigma DR2 tension only.
WA_DESI_DR2 = -0.73         # (local) DESI DR2 + DESY5 central w_a (pre-registered-observations.md line 50)
SIGMA_WA_DR2 = 0.25         # (local) DESI DR2 + DESY5 sigma(w_a)  (same source)

# ---- STEP-1 RELEASE-STATUS CHECK (recorded 2026-06-13 by the dispatching agent) ----
# (a) pinned local DR3 npz path (absent => UNAVAILABLE on the local axis):
DESI_DR3_NPZ = SESSION_DIR / "desi_dr3_w0wa_constraint.npz"        # (local)
# (b) literature/web release-confirmation check, performed 2026-06-13:
RELEASE_CHECK_DATE = "2026-06-13"                                 # (local)
RELEASE_CHECK_PUBLIC_DR3 = False                                  # (local) NO public DESI DR3 w0waCDM constraint found
RELEASE_CHECK_NOTE = (                                            # (local)
    "WebSearch + arXiv (2026-06-13): latest PUBLIC DESI cosmology release is DR2 "
    "(arXiv:2503.14738v3 'DESI DR2 Results II', 3yr; w0>-1,wa<0; 3.1sigma DESI+CMB). "
    "Papers through 2025-12/2026-03 (2512.07104, 2507.01380v3) reanalyze DR2, not DR3. "
    "No public DR3 w0waCDM (w0,wa,covariance) constraint exists. DR3 horizon ~2027 "
    "(pre-registered-observations.md Timeline). Today 2026-06-13."
)

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / "s107_desi_dr3_wz_decision_rule.npz"
OUT_PNG = SESSION_DIR / "s107_desi_dr3_wz_decision_rule.png"
# The verdict file is written by the emit_verdict MCP tool — NOT by this script.

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    PROJECT_ROOT / "sessions/framework/registry/pre-registered-observations.md",
    COMPUTATIONS_DIR / "s84_w4_dr3_contingency_fine_grained.json",  # frozen L3 payload (may be absent; SHA="" then)
    PROJECT_ROOT / "sessions/framework/registry/w0-primary-decision-rule.md",
    DESI_DR3_NPZ,  # DR3 (w0,wa,Sigma) — UNAVAILABLE until ~2027; SHA="" => STEP 2a
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p).replace("\\", "/")  # (local)
        shown = sha[:16] + "..." if sha else "<ABSENT>"  # (local)
        print(f"  {rel}: {shown}")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    """Stable hash over all input SHAs (invariant to dict ordering)."""
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    """Compute (audit_sha256, content_sha256) per the S84+ dual-SHA schema, EXTENDED
    so the FROZEN rule SHAs enter audit_sha256 (audit_discriminators: frozen_rule_shas).

    audit_sha256   = sha256( bytes(script) || bytes(canonical) || pinmap_json || frozen_rule_shas_json )
    content_sha256 = sha256( bytes(script) )
    """
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
    frozen_json = json.dumps(dict(sorted(FROZEN_RULE_SHAS.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_audit.update(frozen_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Rule-fire machinery (L1/L2/L3/L4); the gate FIRES, never authors
# ---------------------------------------------------------------------------

def fire_L1(wa_meas: float) -> dict:
    """L1 primary survive/fail rule on the MEASURED w_a (FROZEN edges)."""
    if wa_meas > L1_SURVIVE_EDGE + 0.0:
        reading = "SURVIVE"  # (local)
    elif wa_meas < L1_FAIL_EDGE - 0.0:
        reading = "FAIL"  # (local)
    else:
        reading = "INFO-band"  # (local)
    return {"reading": reading, "wa_meas": wa_meas,
            "survive_edge": L1_SURVIVE_EDGE, "fail_edge": L1_FAIL_EDGE}


def fire_L2(w0_meas: float, wa_meas: float, Sigma: np.ndarray) -> dict:
    """L2 — nearest S60 scenario + actual joint 2D Mahalanobis sigma of FW=(w0_FW,wa_FW)
    from the DR3 central in the DR3 covariance Sigma. FROZEN scenario sigmas are LOADED."""
    fw = np.array([w0_FW, wa_FW], dtype=float)         # (local) canonical FW point
    dr3 = np.array([w0_meas, wa_meas], dtype=float)    # (local)
    diff = fw - dr3                                    # (local)
    # 2D Mahalanobis: d^2 = diff^T Sigma^{-1} diff via numpy.linalg.solve (2x2)
    sol = np.linalg.solve(Sigma, diff)                 # (local)
    d2 = float(diff @ sol)                             # (local)
    d_mahalanobis = float(np.sqrt(max(d2, 0.0)))       # (local)
    # nearest S60 scenario (Euclidean in (w0,wa))
    nearest, nd = None, np.inf                         # (local)
    for name, sc in S60_SCENARIOS.items():
        dd = float(np.hypot(w0_meas - sc["w0"], wa_meas - sc["wa"]))  # (local)
        if dd < nd:
            nd, nearest = dd, name
    return {"d_mahalanobis": d_mahalanobis,
            "nearest_scenario": nearest,
            "frozen_scenario_sigma": S60_SCENARIOS[nearest]["sigma"],
            "frozen_scenario_status": S60_SCENARIOS[nearest]["status"]}


def fire_L3(w0_meas: float, wa_meas: float) -> dict:
    """L3 — R_842 binary containment; if outside, classify into the FROZEN 7-cell {A1..C2}."""
    in_r842 = (R842_W0_LO <= w0_meas <= R842_W0_HI) and (R842_WA_LO <= wa_meas <= R842_WA_HI)  # (local)
    cell, verdict, scorecard = None, None, None        # (local)
    if not in_r842:
        for c in SEVEN_CELL:
            w0lo, w0hi = c["w0"]                        # (local)
            in_w0 = (min(w0lo, w0hi) <= w0_meas <= max(w0lo, w0hi))  # (local)
            if c.get("wa_split"):
                in_wa = (wa_meas < R842_WA_LO) or (wa_meas > R842_WA_HI)  # (local) [-1,-0.2)U(0.2,1]
            elif c.get("wa") is None:
                in_wa = True                            # (local) C2 catch (impedance audit)
            else:
                walo, wahi = c["wa"]                    # (local)
                in_wa = (min(walo, wahi) <= wa_meas <= max(walo, wahi))  # (local)
            if in_w0 and in_wa:
                cell, verdict, scorecard = c["cell"], c["verdict"], c["scorecard"]
                break
    return {"in_R842": in_r842, "cell": cell, "verdict": verdict, "scorecard": scorecard}


def fire_L4(w0_meas: float) -> dict:
    """L4 — reversibility re-pin trigger on MEASURED w_0 in [-0.86,-0.83] (FROZEN band).
    RECORD only; the A->B canonical re-emission is owed to a follow-up session (do NOT re-emit w0_FW)."""
    triggered = (L4_REVERSAL_LO <= w0_meas <= L4_REVERSAL_HI)  # (local)
    return {"reversal_triggered": triggered,
            "band": [L4_REVERSAL_LO, L4_REVERSAL_HI],
            "note": ("PRIMARY A(-0.918)->B(-0.842454) re-pin owed to a follow-up session "
                     "per w0-primary-decision-rule.md §6; NOT re-emitted here")}


def composite_collapse(sign_verdict: str, magnitude_verdict: str, regime_verdict: str) -> str:
    """gate-verdicts.md composite-collapse rule (PRE-REGISTERED — NOT modified, Class 3)."""
    if regime_verdict == "BREAKDOWN":
        return "FAIL"
    if sign_verdict == "FAIL":
        return "FAIL"
    if magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        return "FAIL"
    if magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        return "INFO"
    if magnitude_verdict == "INFO":
        return "INFO"
    return "PASS"


# ---------------------------------------------------------------------------
# Section 6 — Plot: (w_0, w_a) plane (armed-rule visualization)
# ---------------------------------------------------------------------------

def make_plot(dr3_central: tuple | None) -> None:
    """(w_0,w_a) plane: R_842 rect + 7-cell + S60 scenario points + L1 bands + FW point.
    Under Track A the DR3 point is annotated 'PENDING RELEASE'."""
    fig, ax = plt.subplots(figsize=(9.5, 7.5))  # (local)

    # L1 w_a survive/fail bands (horizontal regions on the w_a axis)
    ax.axhspan(L1_SURVIVE_EDGE, 0.6, color="#2ca02c", alpha=0.10, zorder=0)   # SURVIVE band (w_a > -0.35)
    ax.axhspan(-1.6, L1_FAIL_EDGE, color="#d62728", alpha=0.10, zorder=0)     # FAIL band (w_a < -0.530)
    ax.axhline(L1_SURVIVE_EDGE, color="#2ca02c", ls="--", lw=1.4,
               label=f"L1 SURVIVE edge w_a={L1_SURVIVE_EDGE}")
    ax.axhline(L1_FAIL_EDGE, color="#d62728", ls="--", lw=1.4,
               label=f"L1 FAIL edge w_a={L1_FAIL_EDGE}")

    # L3 R_842 rectangle
    ax.add_patch(Rectangle((R842_W0_LO, R842_WA_LO),
                           R842_W0_HI - R842_W0_LO, R842_WA_HI - R842_WA_LO,
                           fill=False, edgecolor="black", lw=2.2,
                           label=f"L3 R_842 = [{R842_W0_LO},{R842_W0_HI}]x[{R842_WA_LO},{R842_WA_HI}]"))

    # 7-cell partition (light outlines for finite cells)
    for c in SEVEN_CELL:
        w0lo, w0hi = c["w0"]  # (local)
        if c.get("wa") and not c.get("wa_split"):
            walo, wahi = c["wa"]  # (local)
            ax.add_patch(Rectangle((min(w0lo, w0hi), min(walo, wahi)),
                                   abs(w0hi - w0lo), abs(wahi - walo),
                                   fill=False, edgecolor="#888888", ls=":", lw=0.9, zorder=1))
            ax.text((w0lo + w0hi) / 2, (walo + wahi) / 2, c["cell"],
                    fontsize=7, color="#555555", ha="center", va="center")

    # L4 reversibility band (vertical band on w_0)
    ax.axvspan(L4_REVERSAL_LO, L4_REVERSAL_HI, color="#9467bd", alpha=0.18, zorder=0,
               label=f"L4 reversal band w_0 in [{L4_REVERSAL_LO},{L4_REVERSAL_HI}]")

    # S60 scenario points
    for name, sc in S60_SCENARIOS.items():
        ax.scatter(sc["w0"], sc["wa"], marker="s", s=90, zorder=5,
                   color="#ff7f0e", edgecolor="black")
        ax.annotate(f"S60-{name}\n{sc['sigma']}σ ({sc['status']})",
                    (sc["w0"], sc["wa"]), textcoords="offset points", xytext=(8, 6),
                    fontsize=7.5)

    # DR2 reference point (latest PUBLIC release; informational only — NOT fired)
    ax.scatter(-0.752, WA_DESI_DR2, marker="v", s=80, color="#17becf",
               edgecolor="black", zorder=5)
    ax.annotate("DESI DR2+DESY5\n(-0.752,-0.73) [latest public; informational]",
                (-0.752, WA_DESI_DR2), textcoords="offset points", xytext=(8, -22), fontsize=7)

    # Canonical FW point
    ax.scatter(w0_FW, wa_FW, marker="*", s=420, color="#1f77b4", edgecolor="black",
               zorder=6, label=f"FW canonical (w0_FW={w0_FW}, wa_FW={wa_FW})")
    ax.annotate(f"FW\n({w0_FW}, {wa_FW})", (w0_FW, wa_FW),
                textcoords="offset points", xytext=(10, 10), fontsize=9, fontweight="bold")

    # LCDM reference
    ax.scatter(-1.0, 0.0, marker="P", s=110, color="black", zorder=5)
    ax.annotate("ΛCDM (-1, 0)", (-1.0, 0.0), textcoords="offset points",
                xytext=(8, 8), fontsize=8)

    # DR3 point — PENDING RELEASE under Track A
    if dr3_central is None:
        ax.scatter(-0.842, -0.40, marker="X", s=160, color="grey", alpha=0.55, zorder=4)
        ax.annotate("DESI DR3\nPENDING RELEASE\n(rule ARMED, un-fired; horizon ~2027)",
                    (-0.842, -0.40), textcoords="offset points", xytext=(10, -34),
                    fontsize=9, color="#444444", fontweight="bold")
    else:
        ax.scatter(dr3_central[0], dr3_central[1], marker="X", s=160,
                   color="crimson", zorder=7)
        ax.annotate(f"DESI DR3\n({dr3_central[0]:.3f},{dr3_central[1]:.3f})",
                    dr3_central, textcoords="offset points", xytext=(10, 10),
                    fontsize=9, color="crimson", fontweight="bold")

    ax.set_xlim(-1.25, -0.20)
    ax.set_ylim(-1.55, 0.55)
    ax.set_xlabel("$w_0$ (present-day dark-energy equation of state)")
    ax.set_ylabel("$w_a$ (evolution parameter, CPL)")
    ax.set_title("S107 DESI-DR3 w(z) decision-rule — FROZEN S66-era rule ARMED\n"
                 "(L1 survive/fail bands + L2 S60 scenarios + L3 R_842/7-cell + L4 reversal band)")
    ax.legend(loc="lower left", fontsize=7.2, framealpha=0.9)
    ax.grid(True, alpha=0.25)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=140)
    plt.close(fig)
    print(f"  plot written: {OUT_PNG.relative_to(PROJECT_ROOT)}")


# ---------------------------------------------------------------------------
# Section 7 — verdict-payload printer (agent calls emit_verdict)
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note: str = "", extra_rows=None) -> dict:
    """Print the emit_verdict payload for the dispatching AGENT to pass to the
    knowledge-MCP emit_verdict tool. The script does NOT write the verdict file."""
    payload: dict = {
        "session": 107,
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
# Section 8 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins (first 20 lines of stdout)
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. Dual SHAs (frozen_rule_shas ENTER audit_sha256)
    script_path = Path(__file__).resolve()                 # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap+frozen_rule_shas)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 1c. Canonical-pin sanity (verify the armed predictions are the un-superseded values)
    print(f"  canonical pins: w0_FW={w0_FW}  wa_FW={wa_FW}")
    assert abs(w0_FW - (-0.918)) < 1e-9, "w0_FW drift — expected -0.918 (S58 four-fold lock)"
    assert abs(wa_FW - 0.0) < 1e-12, "wa_FW drift — expected 0.0 (four-fold structural lock)"

    # ---- DR2 substitution-chain (the [SIGN] w_a outlier-direction) — exact QQ 73/25 ----
    delta_wa = wa_FW - WA_DESI_DR2                          # (local) = 0 - (-0.73) = +0.73
    nsig_wa_dr2 = abs(delta_wa) / SIGMA_WA_DR2              # (local) = 0.73/0.25 = 73/25 = 2.92
    print(f"  [SIGN] DR2 substitution chain: delta_wa = wa_FW - w_a^DR2 = {wa_FW} - ({WA_DESI_DR2}) = {delta_wa:+.4f}")
    print(f"         nsig_wa^DR2 = |delta_wa|/sigma_wa^DR2 = {abs(delta_wa)}/{SIGMA_WA_DR2} = 73/25 = {nsig_wa_dr2:.4f} sigma")
    print(f"         delta_wa = {delta_wa:+.3f} > 0 => wa_FW=0 is the LESS-NEGATIVE (no-evolution) outlier vs DESI thawing (w_a<0)")
    print()

    # ====================================================================
    # STEP 1 — DESI DR3 public-release status check (the GATING input)
    # ====================================================================
    local_npz_present = DESI_DR3_NPZ.exists()              # (local)
    dr3_available = bool(local_npz_present and RELEASE_CHECK_PUBLIC_DR3)  # (local) need BOTH a usable local file AND a public release
    print("=== STEP 1 — DESI DR3 release-status check ===")
    print(f"  (a) local DR3 npz present?      {local_npz_present}  ({DESI_DR3_NPZ.name})")
    print(f"  (b) web/literature check date:  {RELEASE_CHECK_DATE}")
    print(f"      public DR3 w0waCDM found?    {RELEASE_CHECK_PUBLIC_DR3}")
    print(f"      note: {RELEASE_CHECK_NOTE}")
    print(f"  => DR3 available for rule-fire?  {dr3_available}")
    print()

    common_npz = {                                         # (local) base npz payload (both tracks)
        "gate_id": GATE_ID,
        "release_check_date": RELEASE_CHECK_DATE,
        "release_check_public_dr3": RELEASE_CHECK_PUBLIC_DR3,
        "local_dr3_npz_present": local_npz_present,
        "dr3_available": dr3_available,
        "w0_FW": float(w0_FW), "wa_FW": float(wa_FW),
        "L1_survive_edge": L1_SURVIVE_EDGE, "L1_fail_edge": L1_FAIL_EDGE,
        "R842": np.array([R842_W0_LO, R842_W0_HI, R842_WA_LO, R842_WA_HI]),
        "L4_reversal_band": np.array([L4_REVERSAL_LO, L4_REVERSAL_HI]),
        "S60_sigmas": np.array([S60_SIGMA_A, S60_SIGMA_B, S60_SIGMA_C]),
        "delta_wa_DR2": delta_wa, "nsig_wa_DR2": nsig_wa_dr2,
        "frozen_rule_shas": json.dumps(FROZEN_RULE_SHAS, sort_keys=True),
        "dr3_release_horizon": DR3_RELEASE_HORIZON,
        "audit_sha256": audit_sha, "content_sha256": content_sha,
    }

    if not dr3_available:
        # ================================================================
        # STEP 2a — PRE-REG-INC (canonical likely outcome; rule ARMED)
        # ================================================================
        print("=== STEP 2a — DR3 NOT released => PRE-REG-INC (rule ARMED, un-fired) ===")
        value = "blocked_pending_DESI_DR3_release;S66_rule_armed"  # (local)
        armed = {  # (local) the four armed sub-rules + frozen thresholds + frozen SHAs
            "L1": {"survive_edge": L1_SURVIVE_EDGE, "fail_edge": L1_FAIL_EDGE,
                   "source": FROZEN_RULE_SHAS["L1_source"]},
            "L2": {"sigma_A": S60_SIGMA_A, "sigma_B": S60_SIGMA_B, "sigma_C": S60_SIGMA_C,
                   "source": FROZEN_RULE_SHAS["L2_source"]},
            "L3": {"R842": [R842_W0_LO, R842_W0_HI, R842_WA_LO, R842_WA_HI],
                   "content_sha256": FROZEN_RULE_SHAS["L3_content_sha256"],
                   "audit_sha256": FROZEN_RULE_SHAS["L3_audit_sha256"]},
            "L4": {"band": [L4_REVERSAL_LO, L4_REVERSAL_HI],
                   "audit_sha256": FROZEN_RULE_SHAS["L4_audit_sha256"],
                   "content_sha256": FROZEN_RULE_SHAS["L4_content_sha256"]},
        }
        for k, v in armed.items():
            print(f"  {k} ARMED: {v}")
        print("  No sigma-distance computed (no measured w_a to compare). "
              "PRE-REG-INC is honest blocked-pending-data, NOT a FAIL, NOT INFO.")
        make_plot(dr3_central=None)
        np.savez(OUT_NPZ, track="A_PRE-REG-INC", verdict="PRE-REG-INC",
                 value=value, armed_thresholds=json.dumps(armed, sort_keys=True),
                 **common_npz)
        print(f"  npz written: {OUT_NPZ.relative_to(PROJECT_ROOT)}")
        print()
        tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
        print(tag)
        # [SIGN] gate under PRE-REG-INC: rule ARMED, un-fired; no measurement to compare.
        # The emit_verdict tool's magnitude/regime enums are {PASS,INFO,FAIL}/{VALID,MARGINAL,
        # BREAKDOWN} and do NOT accept 'N/A' (only sign_verdict does). The plan's intended
        # 3-tuple under PRE-REG-INC is (N/A, N/A, VALID) meaning "armed, un-fired, no measurement".
        # Faithful encoding within the tool's enum: sign=N/A (no measured direction); magnitude=INFO
        # (non-committal — NO measurement exists to fall in any pass/fail band, so this is an
        # armed-un-fired placeholder, NOT a partial-tension reading); regime=VALID (plan value).
        # The composite remains PRE-REG-INC (a first-class verdict, NOT collapsed from the 3-tuple).
        print_verdict_payload(
            "PRE-REG-INC", value, audit_sha, content_sha,
            sign_verdict="N/A", magnitude_verdict="INFO", regime_verdict="VALID",
            companion_note=("DR3 release-status check 2026-06-13: NO public DESI DR3 w0waCDM; "
                            "S66-era rule ARMED (L1/L2/L3/L4 frozen thresholds+SHAs); horizon ~2027; "
                            "retired-GW: no Omega_GW amplitude as live prediction. 3-tuple under "
                            "PRE-REG-INC = armed-un-fired placeholder (plan-intent sign/mag = N/A; "
                            "magnitude=INFO is the tool-enum encoding of 'no measurement', NOT partial-tension)"),
            extra_rows=[
                "# armed_sub_rules: L1(-0.35/-0.530 S67/S68) L2(3.91/2.06/6.33 S60) "
                "L3(R_842+7cell S84 content=801e4690 audit=f6e102fd) L4([-0.86,-0.83] S86 audit=8893fbc2)",
                f"# DR2_substitution_chain: delta_wa={delta_wa:+.3f} nsig_wa^DR2=73/25={nsig_wa_dr2:.2f}sigma "
                "(wa_FW=0 is the less-negative/no-evolution outlier vs DESI thawing)",
            ],
        )
        wall = time.time() - t0  # (local)
        print(f"\n=== {GATE_ID}: PRE-REG-INC (Track A; rule armed; wall {wall:.2f}s) ===")
        return 0

    # ====================================================================
    # STEP 2b — DR3 released => FIRE the frozen rules mechanically
    # ====================================================================
    print("=== STEP 2b — DR3 released => FIRE L1/L2/L3/L4 ===")
    data = np.load(DESI_DR3_NPZ)                            # (local)
    w0_meas = float(data["w0"])                            # (local)
    wa_meas = float(data["wa"])                            # (local)
    Sigma = np.array(data["cov"], dtype=float).reshape(2, 2)  # (local) 2x2 covariance

    L1 = fire_L1(wa_meas)                                  # (local)
    L2 = fire_L2(w0_meas, wa_meas, Sigma)                  # (local)
    L3 = fire_L3(w0_meas, wa_meas)                         # (local)
    L4 = fire_L4(w0_meas)                                  # (local)
    print(f"  L1: {L1}")
    print(f"  L2: {L2}")
    print(f"  L3: {L3}")
    print(f"  L4: {L4}")

    # [SIGN] 3-tuple — fired on the MEASURED w_a
    #   sign: predicted no-evolution (wa_FW=0); PASS iff the measured direction is consistent
    #         with the SURVIVE side (w_a not significantly negative), else FAIL.
    sign_verdict = "PASS" if L1["reading"] == "SURVIVE" else ("FAIL" if L1["reading"] == "FAIL" else "N/A")  # (local)
    #   magnitude: joint Mahalanobis sigma vs the frozen nearest-scenario sigma
    d_m = L2["d_mahalanobis"]                              # (local)
    frozen_sig = L2["frozen_scenario_sigma"]              # (local)
    if d_m <= 2.0:
        magnitude_verdict = "PASS"  # (local)
    elif d_m <= frozen_sig:
        magnitude_verdict = "INFO"  # (local)
    else:
        magnitude_verdict = "FAIL"  # (local)
    regime_verdict = "VALID"  # (local) no expansion/scan window applies
    composite = composite_collapse(sign_verdict, magnitude_verdict, regime_verdict)  # (local)
    # L3 refutation cells force FAIL on the composite (per FAIL_meaning)
    if L3["scorecard"] and "refutation" in L3["scorecard"]:
        composite = "FAIL"

    value = (f"L1={L1['reading']};L2_dMahalanobis={d_m:.3f}_nearest={L2['nearest_scenario']}"
             f"(sigma{frozen_sig});L3_inR842={L3['in_R842']}_cell={L3['cell']};"
             f"L4_reversal={L4['reversal_triggered']}")  # (local)
    print(f"  composite top-line: {composite}  (sign={sign_verdict} mag={magnitude_verdict} regime={regime_verdict})")

    make_plot(dr3_central=(w0_meas, wa_meas))
    np.savez(OUT_NPZ, track="B_FIRED", verdict=composite, value=value,
             w0_meas=w0_meas, wa_meas=wa_meas, Sigma=Sigma,
             L1=json.dumps(L1), L2=json.dumps({k: (v if not isinstance(v, np.generic) else float(v)) for k, v in L2.items()}),
             L3=json.dumps(L3), L4=json.dumps(L4),
             sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict, regime_verdict=regime_verdict,
             **common_npz)
    print(f"  npz written: {OUT_NPZ.relative_to(PROJECT_ROOT)}")
    print()
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)
    print_verdict_payload(
        composite, value, audit_sha, content_sha,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict, regime_verdict=regime_verdict,
        companion_note=(f"DR3 FIRED 2026-..; L1={L1['reading']} L3_cell={L3['cell']} "
                        f"L4_reversal={L4['reversal_triggered']}; retired-GW: no Omega_GW live"),
        extra_rows=[
            f"# L2_joint_Mahalanobis={d_m:.4f}sigma vs frozen S60-{L2['nearest_scenario']}={frozen_sig}sigma",
            f"# L4_reversal_trigger={L4['reversal_triggered']} (A->B re-pin owed to follow-up session, not emitted here)",
        ],
    )
    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} (Track B; rule fired; wall {wall:.2f}s) ===")
    return 0 if composite != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
