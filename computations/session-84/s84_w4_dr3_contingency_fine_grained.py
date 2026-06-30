#!/usr/bin/env python3
"""
S84 W4-44 -- DR3-CONTINGENCY-FINE-GRAINED (7-scenario sub-tree pre-registration)
================================================================================

Gate: S84-DR3-CONTINGENCY-FINE-GRAINED ([AUDIT])

Hypothesis being tested:
  Conditional on W1b-9 S84-DR3-RESPONSE-PROTOCOL parent gate (R_842 rectangle
  containment) firing FAIL at DR3 release, the framework pre-commits a
  7-scenario partition (A1, A2, B1, B2, B3, C1, C2) of the (w_0, w_a) plane
  OUTSIDE the rectangle R_842 = [-0.942, -0.742] x [-0.2, 0.2]. Each sub-scenario
  carries a pre-registered framework verdict (corroborates branch-(iv) /
  refutes branch-(iv) / triggers mechanism reassessment) and a post-release
  EVOI rank ordering identifying which carry-forward computation becomes #1.

Pre-registered PASS/FAIL/INFO (this gate is PRE-REGISTRATION ONLY):
  PASS: JSON file written with all 7 branches populated {scenario_id,
        w0_range, wa_range, framework_verdict, evoi_post_release}; SHA logged.
  INFO: 5-6 branches populated.
  FAIL: Not committed.

Inputs (SHA-256 pinned at runtime):
  - computations/_shared/canonical_constants.py (w0_FW, wa_FW, planck_ns)
  - computations/session-73/s73b_desi_dr3_predictions.py (taxonomy inheritance, FROZEN 2026-04-10)
  - computations/session-73/s73b_desi_dr3_predictions.npz (bundle payload)
  - computations/session-83/s83_w3_g42_dr3_live_watch.py (parent binary rectangle)
  - computations/session-83/s83_w3_g42_dr3_live_watch.npz (parent npz)

Output 4-tuple:
  (value="7-scenario-tree-frozen", scheme="pre-registration",
   convention="CPL (w_0, w_a)", L_max=N/A)

Classification: GEOMETRIC (dark-energy equation-of-state decision tree)

METHODOLOGY
-----------
This script is SINGLE-AUTHORITY-FREEZE: it writes the 7-branch decision tree
once and records the closure SHA. On DR3 release, a successor script loads this
JSON and classifies the released (w_0^DR3, w_a^DR3) into exactly one cell with
no re-registration. The decision tree partitions the (w_0, w_a) plane OUTSIDE
R_842 along two semantic axes:

  w_0 axis:  deep    = w_0 < -0.942  (below R_842 lower edge)
             corridor = w_0 in [-0.942, -0.742]  (inside R_842 w_0 range)
             shallow = w_0 > -0.742  (above R_842 upper edge; Quintom/thaw)

  w_a axis:  lock    = w_a in [-0.2, 0.2]  (four-fold locked corridor)
             moderate-dyn = w_a in [-0.5, -0.2)  (mild Quintom drift)
             extreme-dyn  = w_a < -0.5  (strongly dynamical DE)
             thaw    = w_a > 0.2  (positive drift / freezing)

  Cells:
    A1: w_0 in [-0.988, -0.942),  w_a in [-0.2, 0.2]
        -- branch-(iv) mild corroboration (w_0 landed 1-sigma deeper than R_842)
    A2: w_0 in [-1.05, -0.988),   w_a in [-0.2, 0.2]
        -- branch-(iv) stretched corroboration (w_0 ~ 2-sigma deeper)
    B1: w_0 in [-0.942, -0.742],  w_a in [-1.0, -0.2) U (0.2, 1.0]
        -- w_a-driven exclusion (S73b A & B coarse scenarios both land here)
    B2: w_0 in (-0.742, -0.50],   w_a in [-0.2, 0.2]
        -- w_0-driven exclusion (mild Quintom with w_a-lock preserved)
    B3: w_0 in (-0.742, -0.50],   w_a in [-0.5, -0.2)
        -- joint shift, moderate Quintom
    C1: w_0 in (-0.742, -0.20],   w_a in [-1.5, -0.5)
        -- extreme Quintom (S73b C coarse scenario lands here)
    C2: w_0 in [-1.20, -1.05) or (shallow, thaw-combined); deep phantom

Parent gate G42 rectangle R_842 boundaries are inherited verbatim. No
rectangle-resizing, no w_a axis migration, no dual-pin retreat (S83
sagan-synthesis §V.9 lockouts A-F enforced).

DISCIPLINE
----------
- `from canonical_constants import *` for w0_FW, wa_FW, planck_ns.
- All intermediates tagged `# (local)`.
- SHA-256 of each input logged in first 20 lines of stdout.
- 4-tuple printed as final non-verdict line.
- Verdict line appended to s84_gate_verdicts.txt with full 64-char SHA pin.
- JSON schema matches plan: {scenario_id, w0_range, wa_range,
  framework_verdict, evoi_post_release} on each of the 7 branches.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 -- Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===


# ---------------------------------------------------------------------------
# Section 3 -- Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S84"                                                 # (local)
GATE_ID = "S84-DR3-CONTINGENCY-FINE-GRAINED"                    # (local)
SCHEME = "pre-registration"                                     # (local)
CONVENTION = "CPL (w_0, w_a)"                                   # (local)
L_MAX = "N/A"                                                   # (local)

# Pre-registered rectangle R_842 (inherited from W1b-9; NO resizing)
R842_W0 = (-0.942, -0.742)                                      # (local)
R842_WA = (-0.2, 0.2)                                           # (local)

# Framework branch-(iv) canonical point under test (S83 sagan-synthesis)
BRANCH_IV_W0 = -0.842454                                        # (local)
BRANCH_IV_WA = 0.0                                              # (local)

# DR3 projected sigmas (from S71 DESI-DR3-SCENARIO-B-PRECISE-71)
SIG_W0_DR3 = 0.046                                              # (local)
SIG_WA_DR3 = 0.177                                              # (local)
RHO_DR3 = -0.85                                                 # (local)

# Output destinations
OUT_JSON = resolve_output(84, 's84_w4_dr3_contingency_fine_grained.json')
VERDICT_TXT = resolve_output(84, 's84_gate_verdicts.txt')

# Input-pin map (files whose SHA-256 is recorded in closure)
INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    resolve_script(73, 's73b_desi_dr3_predictions.py'),
    resolve_output(73, 's73b_desi_dr3_predictions.npz'),
    resolve_script(83, 's83_w3_g42_dr3_live_watch.py'),
    resolve_output(83, 's83_w3_g42_dr3_live_watch.npz'),
]


# ---------------------------------------------------------------------------
# Section 4 -- SHA-256 input-pin block
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()                                        # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}                                                   # (local)
    for p in inputs:
        sha = sha256_of(p)                                      # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins, payload_extra: str) -> str:
    """Stable SHA over inputs + pre-registered scalars + payload."""
    items = sorted(pins.items())                                # (local)
    h = hashlib.sha256()                                        # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    h.update(payload_extra.encode("utf-8"))
    return h.hexdigest()


def audit_hash(closure: str) -> str:
    """Audit SHA is a secondary hash over the closure + gate metadata
    (for S84+ dual-SHA schema)."""
    h = hashlib.sha256()                                        # (local)
    payload = (
        f"GATE_ID={GATE_ID}\nSCHEME={SCHEME}\nCONVENTION={CONVENTION}\n"
        f"L_MAX={L_MAX}\nSESSION={SESSION}\nCLOSURE={closure}\n"
    )                                                           # (local)
    h.update(payload.encode("utf-8"))
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 -- 7-scenario decision tree (single-authority freeze)
# ---------------------------------------------------------------------------

# Each branch includes w0_range, wa_range, framework_verdict,
# evoi_post_release (priority rank for carry-forward computations).

SCENARIOS = [
    {
        "scenario_id": "A1",
        "label": "branch-(iv) mild corroboration (w_0 slightly deep)",
        "w0_range": [-0.988, -0.942],   # below R_842 lower edge by up to ~1 DR3-sigma
        "wa_range": [-0.2, 0.2],
        "framework_verdict": (
            "CORROBORATES branch-(iv) at -0.842 within 1-sigma deep shift; "
            "Volovik-Josephson partition confirmed to leading order; "
            "scorecard §VII.M.scorecard.corroborations entry REQUIRED "
            "(not an automatic PASS, since DR3 landed deeper than R_842)."
        ),
        "dr3_center_example": (-0.965, 0.0),
        "sigma_distance_from_R842_edge": "(-0.023 in w_0) ~ 0.50-sigma deep of R_842 lower edge",
        "evoi_post_release": {
            "rank_1": (
                "Josephson-sector amplitude recompute: promote w_0 from -0.842 "
                "to DR3 central value; verify S58/S83 partition still closes "
                "Gibbs-Duhem consistency."
            ),
            "rank_2": (
                "Volovik-partition scheme variance: re-evaluate 0.06 scheme "
                "uncertainty band; does DR3 center lie within the scheme band?"
            ),
            "rank_3": (
                "Cross-correlate with Pantheon+ / DESY5 / Union3 SN "
                "calibrations (S72 systematic 0.08 in w_0)."
            ),
            "rank_4": "Update canonical_constants.w0_FW to DR3 central via S85 promotion.",
        },
        "post_release_action": (
            "Framework SURVIVES; scorecard corroboration entry; carry-forward "
            "to S85: promote w0_FW, recompute GGE relic via Josephson amplitude."
        ),
    },
    {
        "scenario_id": "A2",
        "label": "branch-(iv) stretched corroboration (w_0 ~ 2-sigma deep)",
        "w0_range": [-1.05, -0.988],
        "wa_range": [-0.2, 0.2],
        "framework_verdict": (
            "MARGINAL corroboration of branch-(iv); w_0 sits ~2-sigma deeper "
            "than R_842; Volovik partition requires recalibration but remains "
            "the right mechanism. Not a refutation; flags scheme-systematic "
            "larger than the S72 workshop A-Q2 estimate (0.06)."
        ),
        "dr3_center_example": (-1.02, 0.0),
        "sigma_distance_from_R842_edge": "(-0.078 in w_0) ~ 1.70-sigma deep of R_842 lower edge",
        "evoi_post_release": {
            "rank_1": (
                "Audit S83 W0-REGULATOR-RESOLUTION branches: is there a "
                "five-regulator variant landing at w_0 ~ -1.0? Branch (i)-(iv) "
                "extended scan REQUIRED."
            ),
            "rank_2": (
                "Scheme-systematic inflation: increase 0.06 band to match "
                "DR3-pinned scheme variance; document INFO-demote rule."
            ),
            "rank_3": (
                "Phantom-crossing audit: if w_0 < -1, check substrate impedance "
                "mismatch for phantom-DE-compatible mechanism."
            ),
            "rank_4": "Re-check four-fold w_a lock stability under w_0 = -1 shift.",
        },
        "post_release_action": (
            "Framework SURVIVES with scheme-systematic inflation; carry-forward "
            "to S85: full W0-regulator re-scan, scheme-band audit."
        ),
    },
    {
        "scenario_id": "B1",
        "label": "w_a-driven exclusion (w_0 corridor, w_a dynamical)",
        "w0_range": [-0.942, -0.742],   # INSIDE R_842 w_0 range
        "wa_range": [-1.0, -0.2],        # OUTSIDE R_842 w_a range (negative)
        "framework_verdict": (
            "REFUTES four-fold w_a lock; Volovik w_0 partition SURVIVES. "
            "Four-fold lock (GGE integrability + Josephson + texture + thermal "
            "barrier) was exact; w_a != 0 means one of the four mechanisms "
            "is broken at DR3 level. scorecard §VII.M.scorecard.refutations "
            "entry REQUIRED for w_a lock."
        ),
        "dr3_center_example": (-0.85, -0.40),
        "sigma_distance_from_R842_edge": "(-0.20 in w_a) ~ 1.13-sigma below lock corridor",
        "evoi_post_release": {
            "rank_1": (
                "Four-fold w_a lock diagnostic: which of GGE-integrability, "
                "Josephson, texture, thermal-barrier channels releases? "
                "Pre-registered discriminant required."
            ),
            "rank_2": (
                "Leggett-channel dispersion: w_a-running contribution from "
                "inter-band coherence; recompute S68 w_a integration."
            ),
            "rank_3": (
                "Bayesian model comparison: LCDM vs CPL vs framework-with-w_a-run; "
                "Pantheon+ + DESY5 + BAO full joint."
            ),
            "rank_4": "GGE-thermal leakage audit: which relic freezes dynamical w_a.",
        },
        "post_release_action": (
            "Framework PARTIALLY REFUTED; scorecard refutation entry for w_a "
            "lock; carry-forward to S85: four-fold diagnostic, w_a mechanism audit."
        ),
    },
    {
        "scenario_id": "B2",
        "label": "w_0-driven exclusion (w_0 shallow, w_a lock preserved)",
        "w0_range": [-0.742, -0.50],     # ABOVE R_842 upper edge
        "wa_range": [-0.2, 0.2],         # INSIDE R_842 w_a range
        "framework_verdict": (
            "REFUTES Volovik w_0 = -0.842 partition; four-fold w_a lock "
            "SURVIVES. w_0 landing shallow (closer to LCDM/Quintom thaw) "
            "means either (a) the Volovik mechanism over-estimates the "
            "effacement residual or (b) substrate impedance mismatch "
            "Gamma = 0.99970 is wrong. Refutes branch-(iv) canonical."
        ),
        "dr3_center_example": (-0.65, 0.0),
        "sigma_distance_from_R842_edge": "(+0.092 in w_0) ~ 2.00-sigma shallow of R_842 upper edge",
        "evoi_post_release": {
            "rank_1": (
                "Substrate impedance audit: is Gamma = 0.99970 correct? "
                "S58 effacement-residual recalculation REQUIRED."
            ),
            "rank_2": (
                "Alternative branch scan: does branch (i), (ii), (iii), (v) "
                "canonical land closer to DR3 w_0? S85 W0-regulator re-scan."
            ),
            "rank_3": (
                "Cross-check w_a lock survival: does DR3 w_a actually fall "
                "in [-0.2, 0.2] at 2-sigma? If so, four-fold lock corroborated."
            ),
            "rank_4": "tau_fold relocation audit (lockout F requires fresh pre-reg).",
        },
        "post_release_action": (
            "Framework PARTIALLY REFUTED; scorecard refutation entry for "
            "Volovik w_0 partition; carry-forward to S85: branch re-scan, "
            "impedance audit, alternative-canonical pre-registration."
        ),
    },
    {
        "scenario_id": "B3",
        "label": "joint shift (w_0 shallow, w_a moderately dynamical)",
        "w0_range": [-0.742, -0.50],
        "wa_range": [-0.5, -0.2],
        "framework_verdict": (
            "REFUTES both Volovik w_0 partition AND four-fold w_a lock "
            "simultaneously. Joint exclusion is the MOST CONSTRAINING B-case: "
            "the DR2 drift (shallow w_0 + negative w_a) has continued in DR3; "
            "framework requires dual-mechanism reassessment. scorecard "
            "refutation entry for BOTH w_0 and w_a."
        ),
        "dr3_center_example": (-0.65, -0.35),
        "sigma_distance_from_R842_edge": "(+0.092 in w_0, -0.15 in w_a) joint ~2.3-sigma",
        "evoi_post_release": {
            "rank_1": (
                "Unified mechanism failure audit: is there a SINGLE broken "
                "substrate assumption that yields both w_0 shallow and w_a "
                "dynamical? (e.g., GGE thermalization onset shifts both.)"
            ),
            "rank_2": (
                "CPL-vs-quintessence model selection: does the data prefer "
                "a free-field quintessence over framework? Bayesian BF."
            ),
            "rank_3": (
                "Substrate-emergence vs inflation dichotomy: if DR3 joint "
                "shift matches standard quintessence, framework discriminant "
                "power on DE disappears."
            ),
            "rank_4": "Full S85 re-scan: partition + lock + impedance all on test.",
        },
        "post_release_action": (
            "Framework JOINT-PARTIAL-REFUTED; scorecard dual refutation entry; "
            "carry-forward to S85: unified-failure audit, model-selection "
            "Bayes factor vs free quintessence."
        ),
    },
    {
        "scenario_id": "C1",
        "label": "extreme Quintom (w_0 shallow, w_a strongly dynamical)",
        "w0_range": [-0.742, -0.20],
        "wa_range": [-1.5, -0.5],
        "framework_verdict": (
            "STRONGLY REFUTES framework; DR3 confirms DR2 drift at "
            "extreme Quintom region (S73b Scenario C: w_0 = -0.65, "
            "w_a = -1.0). At 3-sigma this is CLOSED region: Volovik "
            "partition AND four-fold lock AND substrate impedance all "
            "simultaneously incorrect. Framework w_0 = -0.918 incompatible. "
            "scorecard triple refutation entry."
        ),
        "dr3_center_example": (-0.65, -1.0),
        "sigma_distance_from_R842_edge": "(+0.092 in w_0, -0.80 in w_a) joint >6-sigma",
        "evoi_post_release": {
            "rank_1": (
                "Framework-exclusion analysis: at what confidence is the "
                "substrate DE mechanism ruled out? Precompute for 3-sigma, "
                "5-sigma rejection."
            ),
            "rank_2": (
                "Forensic: which S58 assumption broke? Can the framework be "
                "restored with a single corrected mechanism, or is a "
                "fundamental rewrite needed?"
            ),
            "rank_3": (
                "Alternative substrate-DE: is there any configuration of "
                "D_K eigenvalues that yields Quintom-like w(z)? Spectral "
                "moment audit."
            ),
            "rank_4": (
                "Retraction protocol: if no substrate mechanism survives, "
                "retract DE predictions; framework retains GW/particle "
                "physics content."
            ),
        },
        "post_release_action": (
            "Framework DE-SECTOR REFUTED at high confidence; scorecard entry; "
            "S85 carry-forward: full substrate-DE forensic, retraction preparation."
        ),
    },
    {
        "scenario_id": "C2",
        "label": "deep phantom or boundary outliers",
        "w0_range": [-1.20, -1.05],
        "wa_range": [-0.5, 0.5],
        "framework_verdict": (
            "REFUTES framework via phantom crossing; w_0 < -1.05 places DE "
            "below phantom divide where substrate effacement residual cannot "
            "provide negative-pressure excess. OR w_a highly positive "
            "(> +0.5) with shallow w_0 indicates freezing/thaw inconsistent "
            "with four-fold lock. Either branch demands reassessment of "
            "substrate impedance OR retraction of phantom-exclusion claim."
        ),
        "dr3_center_example": (-1.10, 0.0),
        "sigma_distance_from_R842_edge": "(-0.158 in w_0) ~ 3.43-sigma deep of R_842",
        "evoi_post_release": {
            "rank_1": (
                "Phantom-compatibility audit: can substrate impedance "
                "mismatch produce w < -1 without violating null energy "
                "condition? S58/S67 Volovik partition re-examination."
            ),
            "rank_2": (
                "Check A2 boundary: if DR3 falls near -1.05, is it A2 "
                "(corroboration) or C2 (refutation)? Boundary rule: "
                "strict < -1.05 is C2; [-1.05, -0.988] is A2."
            ),
            "rank_3": (
                "Null energy condition: does framework predict NEC "
                "preservation at substrate level? Theorem required."
            ),
            "rank_4": "Alternative mechanism: quintom with phantom-crossing.",
        },
        "post_release_action": (
            "Framework REFUTED via phantom divide or high-freezing thaw; "
            "scorecard entry; S85 carry-forward: phantom compatibility audit, "
            "NEC theorem registration."
        ),
    },
]


def verify_partition(scenarios):
    """Sanity-check that all 7 sub-scenarios lie OUTSIDE R_842.

    A sub-scenario cell is valid only if there exists NO point inside it
    that also lies inside R_842 (i.e., the cells disjoint from R_842).
    """
    def overlaps_R842(w0r, war):                                # (local)
        w0_overlap = (w0r[0] < R842_W0[1]) and (w0r[1] > R842_W0[0])  # (local)
        wa_overlap = (war[0] < R842_WA[1]) and (war[1] > R842_WA[0])  # (local)
        return w0_overlap and wa_overlap

    violations = []                                             # (local)
    for s in scenarios:
        w0r = s["w0_range"]                                     # (local)
        war = s["wa_range"]                                     # (local)
        if overlaps_R842(w0r, war):
            # Check if the OVERLAP is the entire R_842 (invalid)
            # or only a boundary touch (acceptable).
            w0_in = max(w0r[0], R842_W0[0])                     # (local)
            w0_out = min(w0r[1], R842_W0[1])                    # (local)
            wa_in = max(war[0], R842_WA[0])                     # (local)
            wa_out = min(war[1], R842_WA[1])                    # (local)
            # Accept only if overlap has zero measure in one axis
            # (i.e., touches only a boundary point line).
            if (w0_out - w0_in) > 1e-9 and (wa_out - wa_in) > 1e-9:
                violations.append({
                    "scenario_id": s["scenario_id"],
                    "overlap_w0": (w0_in, w0_out),
                    "overlap_wa": (wa_in, wa_out),
                })
    return violations


def classify_point(w0, wa):
    """Given a (w_0, w_a) point, return the scenario_id that contains it,
    or 'INSIDE_R_842' if inside parent rectangle, or 'UNCLASSIFIED'.

    This is the successor-script classification rule, encoded here so the
    closure hash records it verbatim. The successor loads this JSON and
    applies the rule unchanged.
    """
    # Parent gate G42: inside R_842
    if R842_W0[0] <= w0 <= R842_W0[1] and R842_WA[0] <= wa <= R842_WA[1]:
        return "INSIDE_R_842"
    # A-branches: w_0 deeper than R_842 lower edge, w_a in lock
    if w0 < R842_W0[0] and R842_WA[0] <= wa <= R842_WA[1]:
        if w0 >= -0.988:
            return "A1"
        elif w0 >= -1.05:
            return "A2"
        else:
            return "C2"
    # B1: w_0 corridor, w_a out of lock
    if R842_W0[0] <= w0 <= R842_W0[1] and not (R842_WA[0] <= wa <= R842_WA[1]):
        return "B1"
    # Shallow w_0 (above R_842)
    if w0 > R842_W0[1]:
        if R842_WA[0] <= wa <= R842_WA[1]:
            return "B2"
        elif -0.5 <= wa < R842_WA[0]:
            return "B3"
        elif wa < -0.5:
            return "C1"
        else:  # wa > R842_WA[1] (positive thaw)
            return "C2"
    # Very deep w_0 (below -1.05)
    if w0 < -1.05:
        return "C2"
    return "UNCLASSIFIED"


# ---------------------------------------------------------------------------
# Section 6 -- JSON emission + verdict
# ---------------------------------------------------------------------------

def build_payload(closure_sha: str, audit_sha: str, pins: dict) -> dict:
    """Assemble the full JSON payload (single-authority freeze snapshot)."""
    payload = {                                                 # (local)
        "gate_id": GATE_ID,
        "session": SESSION,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "frozen_date": "2026-04-19",
        "frozen_note": (
            "Single-authority freeze: 7-scenario decision tree committed once; "
            "post-release application REQUIRES NO re-registration. "
            "Lockouts A-F (S83 sagan-synthesis V.9 + S84 W1b-9 DR3-RESPONSE-PROTOCOL) "
            "enforced: NO rectangle-resizing, NO dual-pin retreat, "
            "NO scheme-shopping, NO w_a axis migration, "
            "NO post-2026-04-23 branch-(iv) redefinition, NO tau_fold relocation."
        ),
        "parent_gate": "S84-DR3-RESPONSE-PROTOCOL (W1b-9)",
        "parent_verdict_required": "FAIL (DR3 central OUTSIDE R_842)",
        "pre_registered_predictions": {
            "branch_iv_w0": BRANCH_IV_W0,
            "branch_iv_wa": BRANCH_IV_WA,
            "canonical_constants_w0_FW": w0_FW,
            "canonical_constants_wa_FW": wa_FW,
        },
        "rectangle_R842": {
            "w0_range": list(R842_W0),
            "wa_range": list(R842_WA),
            "center": [sum(R842_W0)/2, sum(R842_WA)/2],
            "half_widths": [(R842_W0[1]-R842_W0[0])/2,
                            (R842_WA[1]-R842_WA[0])/2],
            "half_widths_in_DR3_sigma": [
                (R842_W0[1]-R842_W0[0])/2 / SIG_W0_DR3,
                (R842_WA[1]-R842_WA[0])/2 / SIG_WA_DR3,
            ],
        },
        "dr3_projected_cov": {
            "sigma_w0": SIG_W0_DR3,
            "sigma_wa": SIG_WA_DR3,
            "rho_w0_wa": RHO_DR3,
            "source": "S71 DESI-DR3-SCENARIO-B-PRECISE-71 (5x DR1 statistics)",
        },
        "taxonomy_inheritance": {
            "from_gate": "S73b W4-C DESI-DR3-PREP-73B",
            "frozen_at": "2026-04-10",
            "coarse_scenarios": {
                "A": {"w_0": -0.75, "w_a": -0.73,
                      "desc": "Confirms DR2 (DESY5 systematics dominate)",
                      "sub_scenario_classification": "B1"},
                "B": {"w_0": -0.90, "w_a": -0.30,
                      "desc": "Moves toward LCDM (partial regression)",
                      "sub_scenario_classification": "B1"},
                "C": {"w_0": -0.65, "w_a": -1.00,
                      "desc": "More dynamical (DR2 trend amplified)",
                      "sub_scenario_classification": "C1"},
            },
        },
        "cross_reference_s83_w0_workshop": {
            "branch_iv_retention": (
                "S83 W0-REGULATOR-RESOLUTION retired strict branches (i)-(iii); "
                "branch (iv) single-branch promotion at w_0 = -0.842454 ADOPTED "
                "(see project_s83_w0_regulator_workshop_r3.md)."
            ),
            "r_842_migration": (
                "R_918 retrospective: framework w_0 = -0.918 was OUTSIDE upper "
                "edge (self-falsifier under branch (iv)). Migrated to "
                "R_842 centered on branch (iv); no rectangle-resizing."
            ),
            "no_scheme_shopping_commitment": (
                "S83 sagan-synthesis V.9: post-data scheme selection is "
                "unacceptable. DR3 release either corroborates branch (iv) "
                "or forces genuine mechanism reassessment. Strict (iii) "
                "RETIRED; dual-pin NOT available as escape hatch."
            ),
        },
        "scenarios": [],
        "classification_rule": {
            "logic": (
                "1. Check R_842 containment (parent gate G42): "
                "w_0 in [-0.942,-0.742] AND w_a in [-0.2,0.2] -> PASS (not this gate). "
                "2. Outside R_842: apply w_0/w_a axis partition:\n"
                "   - w_0 < -0.942 AND w_a-lock: A1 (-0.988<=w_0) or A2 ([-1.05,-0.988]) or C2 (<-1.05).\n"
                "   - w_0 in [-0.942,-0.742] AND w_a out of lock: B1.\n"
                "   - w_0 > -0.742 AND w_a in lock: B2.\n"
                "   - w_0 > -0.742 AND w_a in [-0.5,-0.2]: B3.\n"
                "   - w_0 > -0.742 AND w_a < -0.5: C1.\n"
                "   - w_0 > -0.742 AND w_a > 0.2: C2 (phantom-thaw).\n"
                "   - w_0 < -1.05: C2 (deep phantom)."
            ),
            "example_classifications": [
                {"point": [-0.965, 0.0], "scenario_id": classify_point(-0.965, 0.0)},
                {"point": [-1.02, 0.0],  "scenario_id": classify_point(-1.02, 0.0)},
                {"point": [-0.85, -0.40], "scenario_id": classify_point(-0.85, -0.40)},
                {"point": [-0.65, 0.0],  "scenario_id": classify_point(-0.65, 0.0)},
                {"point": [-0.65, -0.35], "scenario_id": classify_point(-0.65, -0.35)},
                {"point": [-0.65, -1.0], "scenario_id": classify_point(-0.65, -1.0)},
                {"point": [-1.10, 0.0],  "scenario_id": classify_point(-1.10, 0.0)},
                {"point": [-0.842, 0.0], "scenario_id": classify_point(-0.842, 0.0)},
            ],
        },
        "post_release_action_matrix": {
            "A1": "SURVIVE+promote: scorecard corroboration, S85 canonical w_0 update",
            "A2": "SURVIVE+recal: scorecard corroboration, scheme-band inflation",
            "B1": "PARTIAL-REFUTE-w_a: scorecard refutation on four-fold lock",
            "B2": "PARTIAL-REFUTE-w_0: scorecard refutation on Volovik partition",
            "B3": "DUAL-REFUTE: scorecard refutation on both partition AND lock",
            "C1": "STRONG-REFUTE: substrate DE mechanism ruled out at high conf",
            "C2": "PHANTOM-REFUTE or thaw-REFUTE: impedance audit required",
        },
        "input_pins": pins,
        "closure_sha256": closure_sha,
        "audit_sha256": audit_sha,
    }
    for s in SCENARIOS:
        payload["scenarios"].append(s)
    return payload


def emit_4tuple(value, scheme, convention, L_max):
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(status_tag, closure_sha, audit_sha):
    """Append S84+ dual-SHA verdict line."""
    value_str = "7-scenario-tree-frozen"                        # (local)
    line = (
        f"{GATE_ID}: {status_tag} -- value={value_str!r} scheme={SCHEME} "
        f"convention={CONVENTION!r} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={closure_sha}\n"
    )                                                           # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


# ---------------------------------------------------------------------------
# Section 7 -- Main
# ---------------------------------------------------------------------------

def main():
    t0 = time.time()                                            # (local)

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)                          # (local)

    # 2. Verify 7 scenarios, all disjoint from R_842 interior
    assert len(SCENARIOS) == 7, f"Expected 7 scenarios, got {len(SCENARIOS)}"
    required_ids = {"A1", "A2", "B1", "B2", "B3", "C1", "C2"}   # (local)
    actual_ids = {s["scenario_id"] for s in SCENARIOS}          # (local)
    assert actual_ids == required_ids, (
        f"Scenario IDs mismatch: {actual_ids} != {required_ids}"
    )
    violations = verify_partition(SCENARIOS)                    # (local)
    if violations:
        print("WARN: sub-scenarios with interior overlap with R_842:")
        for v in violations:
            print(f"  {v}")
    else:
        print("Partition check: all 7 sub-scenarios disjoint from R_842 interior.")

    # 3. Required-field population check
    required_fields = {"scenario_id", "w0_range", "wa_range",
                       "framework_verdict", "evoi_post_release"}  # (local)
    for s in SCENARIOS:
        missing = required_fields - set(s.keys())               # (local)
        assert not missing, (
            f"Scenario {s.get('scenario_id','?')} missing fields: {missing}"
        )

    # 4. Print framework pre-registered point + rectangle
    print(f"Branch-(iv) canonical: w_0 = {BRANCH_IV_W0}, w_a = {BRANCH_IV_WA}")
    print(f"canonical_constants: w0_FW = {w0_FW}, wa_FW = {wa_FW}")
    print(f"Rectangle R_842: w_0 in {R842_W0}, w_a in {R842_WA}")
    print()

    # 5. Closure + audit hashes
    payload_extra = (                                           # (local)
        f"GATE_ID={GATE_ID}\n"
        f"SCHEME={SCHEME}\n"
        f"CONVENTION={CONVENTION}\n"
        f"L_MAX={L_MAX}\n"
        f"R842_W0={R842_W0}\n"
        f"R842_WA={R842_WA}\n"
        f"BRANCH_IV_W0={BRANCH_IV_W0}\n"
        f"BRANCH_IV_WA={BRANCH_IV_WA}\n"
        f"N_SCENARIOS={len(SCENARIOS)}\n"
        f"SCENARIO_IDS={','.join(s['scenario_id'] for s in SCENARIOS)}\n"
        f"STATUS_TAG=PASS\n"
    )
    closure = closure_hash(pins, payload_extra)                 # (local)
    audit = audit_hash(closure)                                 # (local)
    print(f"  closure (content_sha256): {closure[:16]}...  (full: {closure})")
    print(f"  audit_sha256:             {audit[:16]}...  (full: {audit})")
    print()

    # 6. Build and write JSON payload
    payload = build_payload(closure, audit, pins)               # (local)
    OUT_JSON.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"Wrote {OUT_JSON}")
    print(f"  Number of scenarios populated: {len(payload['scenarios'])}/7")
    for s in payload["scenarios"]:
        print(f"    {s['scenario_id']}: w_0 in {s['w0_range']}, "
              f"w_a in {s['wa_range']}")
    print()

    # 7. Verdict: all 7 populated with required fields -> PASS
    populated = sum(1 for s in payload["scenarios"]
                    if set(required_fields).issubset(set(s.keys())))  # (local)
    if populated == 7:
        status_tag = "PASS"                                     # (local)
    elif populated >= 5:
        status_tag = "INFO"                                     # (local)
    else:
        status_tag = "FAIL"                                     # (local)
    print(f"Populated branches: {populated}/7 -> verdict: {status_tag}")

    # 8. 4-tuple + verdict append
    tag = emit_4tuple("7-scenario-tree-frozen", SCHEME, CONVENTION, L_MAX)  # (local)
    print(tag)
    append_verdict(status_tag, closure, audit)

    wall = time.time() - t0                                     # (local)
    print(f"\n=== {GATE_ID}: {status_tag} (wall {wall:.3f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
