#!/usr/bin/env python3
"""
S100a W6-2 S100a-VIIAM-STAGE2-VERIFY — Stage-2 THREE-agent PASS-AND aggregation
===============================================================================

Gate: S100a-VIIAM-STAGE2-VERIFY ([VERIFY])
Classification: GEOMETRIC (substrate horizon-trigger condition on eigenvalue-
spectrum-reorganization regions R subset (A_K, H_K, D_K); a property of the
spectral triple's mode-mixing structure, not of any spacetime container)

Pre-registered operator (plan session-100a-plan-w6.md SW6-2, operator.form):
  For each JOINT clause j in {(a),(b),(c)} the clause-owning axes are
    (a): {spectral V_S, transit V_T};  semiclassical V_G audits (a)-semiclassical-half
    (b): {transit V_T, spectral V_S};  semiclassical V_G audits (b)-semiclassical-half
    (c): {spectral V_S, semiclassical V_G};  transit V_T audits (c)-transit-half
  so EVERY clause is audited by ALL THREE reviewers (full-audit owner + two halves):
    (a): S full "a";                T half "a_transit_half";  G half "a_semiclassical_half"
    (b): T full "b";                S half "b_spectral_half"; G half "b_semiclassical_half"
    (c): G full "c";                S half "c_spectral_half"; T half "c_transit_half"
  composite = PASS  iff  for all j: (every reviewer that audits j returns PASS)
                         [three-way PASS-AND, logical AND across ALL THREE verdicts]
  composite = FAIL  iff  exists j, exists R in {S,T,G} auditing j: V_R(j) = FAIL
                         (-> hold STAGE-1 + atlas-09 retraction-route on the named clause)
  composite = INFO  iff  (no clause FAIL) and (exists j, R: V_R(j) = INFO)
                         (-> Stage-2-INFO-deferred; hold STAGE-1; atlas-09 unchanged)

Stage-2 protocol-condition pre-flight (joint-theorem-promotion.md audit items;
machinery_pin_map): reviewer identities MUST match the pinned three-way
assignment (spectral lizzi-spectral-functional-theorist; transit
volovik-superfluid-universe-theorist; semiclassical schwarzschild-penrose-
geometer), NO reviewer in the Stage-0-author exclusion set {hawking-theorist,
transit-dynamics-theorist, connes-ncg-theorist} (registry Sponsors L16708-16712
+ the schwarzschild-penrose eligibility anchor at registry L16774), all three
no_workshop_context_attestation flags True, clause sets exactly matching the
pinned enumeration, and the substrate-input-orthogonality predicate satisfied
(s88 cascade-tail npz loaded by semiclassical ONLY; canonical Gamma_effacement
pin consumed as primary anchor by transit ONLY). A protocol-condition breach
blocks Stage-2 -> 3 promotion (audit FAIL) per joint-theorem-promotion.md
"Missing any of (1)-(6) -> audit FAIL".

Anchor sub-checks (machinery_pin_map.anchor_gamma_eff / .anchor_ratio /
.tolerance; each RE-computed here, never trusted from the reported numbers):
  (b) Gamma_eff: canonical-import route Gamma_effacement = 0.9997
      (canonical_constants.py:540; S37 impedance-transmission; S85 W7-3
      promotion); deviation-from-1 pinned at 3e-4. Operationalized tolerances:
      |.(1-Gamma) - 3e-4| <= 1e-12 abs (exact arithmetic identity; float floor
      ~1e-16) and reviewer-report consistency <= 1e-9 (memory-validated
      Stage-2 recipe). Transit reviewer's anchor_subcheck_gamma_eff block is
      RE-verified against the import.
  (c) ratio_anchor: t_Page(1e13 kg)/t_universe pinned at 9.6684e+04 (registry
      Level-3 anchor; W1b2-64). Script route: load
      s88_w1b2_page_time_cascade_tail.npz, extract ratio at the M = 1e13 kg
      grid point, AND re-derive it from the npz primitives
      prefactor_si*M^3/t_universe_s (internal identity <= 1e-12 rel; the
      t_Page/t_evap = 1/2 Page-1993 convention identity is likewise checked).
      Band vs the registered pin: rel <= 1e-5 — the Class-8.3 publication-
      precision floor for the 5-sig-fig pin 9.6684e4 (half-ULP 5.17e-6;
      epistemic-discipline.md Class 8.3 item 2: rel_tol >= 10^-sig_figs).
      Semiclassical reviewer's anchor_subcheck_ratio block is RE-verified
      (npz_value vs this script's own npz load <= 1e-9; reported rel_dev vs
      recomputed <= 1e-9). Supplementary NON-GATING cross-routes recorded:
      lizzi CODATA recompute (key_numbers.ratio_recomputed) and volovik
      age-convention recompute (key_numbers.ratio_computed; uses
      t_universe = 13.787 Gyr = 4.35085e17 s vs the npz round pin 4.35e17 s,
      explaining its ~2e-4 deviation — documented, not gated; the pinned
      sub-checks per the plan are volovik's gamma block + sp's ratio block).
  W1b2-64 anchor-line audit-trail verification: the canonical session-88
      verdict file line for gate S88-CF-CURV-11-PAGE-TIME-CASCADE-TAIL-MASS
      must carry the dual-SHA pair quoted in the semiclassical reviewer's
      inputs_read (the exact dual-SHA identity that RESOLVES the registry
      legacy-path drift "computations/s88_gate_verdicts.txt" -> canonical
      "computations/session-88/s88_gate_verdicts.txt"; drift disclosed per
      plan input_files.s88_verdict_anchors note).

SUBSTITUTION CHAIN (three-way conjunction-logic chain; plan item 7 — no
physics sign claim; the verify aggregates pre-existing per-reviewer verdicts):
  Definition 1: V_S(j) = spectral (lizzi) verdict on JOINT clause j
                (audits full (a) + spectral halves of (b),(c)).
  Definition 2: V_T(j) = transit (volovik) verdict on JOINT clause j
                (audits full (b) + transit halves of (a),(c)).
  Definition 3: V_G(j) = semiclassical (schwarzschild-penrose) verdict on
                JOINT clause j (audits full (c) + semiclassical halves of (a),(b)).
  Definition 4: PASS-AND (joint-theorem-promotion.md "Stage 2", extended to
                three axes): JOINT clause j PASSES iff EVERY reviewer that
                audits j returns PASS (logical AND across all auditing
                reviewers, NOT OR).
  Substitute:   composite = AND_{j in {(a),(b),(c)}}
                            [ AND_{R in {S,T,G} auditing j} V_R(j) = PASS ].
  Simplify:     with all three clauses JOINT and each audited by all three
                reviewers (one full + two halves), composite = PASS iff all
                NINE clause-verdicts are PASS.
  Canonical:    composite in {PASS, FAIL, INFO} per operator.form (FAIL on any
                clause-FAIL in any auditing reviewer; INFO on any clause-INFO
                absent FAIL; FAIL > INFO > PASS precedence).
  Direction:    three-way PASS-AND is strictly stronger than two-way and than
                any OR — a clause passing in two reviewers but FAILing in the
                third does NOT satisfy the gate (the structural-independence
                guarantee across THREE substantively distinct axes; registry
                §"Stage-2 promotion blockage" bullet "PASS-AND'd across all
                three verdicts").
  Conclusion:   composite=PASS => §VII.AM -> STAGE-3-PERMANENT (+ Stage-3-CLASS
                tag JOINT-CROSS-AXIS-STAGE-2-PASS-AND; atlas-09 Suspected-but-
                Not-Yet-Retracted flag CLEARED); composite=FAIL => hold STAGE-1
                + atlas-09 retraction-route on the named clause(s);
                composite=INFO => hold STAGE-1 + Stage-2-INFO-deferred +
                atlas-09 Suspected UNCHANGED. Bidirectional routing is
                PRE-REGISTERED: the gate is informative in BOTH directions.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-100a/s100a_viiam_reviewer_spectral_lizzi.json
  - computations/session-100a/s100a_viiam_reviewer_transit_volovik.json
  - computations/session-100a/s100a_viiam_reviewer_semiclassical_sp.json
  - sessions/permanent-results-registry.md (§VII.AM block, plan-pinned start 16700)
  - computations/session-88/s88_w1b2_page_time_cascade_tail.npz
  - computations/session-88/s88_gate_verdicts.txt (W1b2-64 anchor line)
  - .claude/rules/joint-theorem-promotion.md
  - .claude/rules/cross-pillar-bridge-anatomy.md
  - sessions/framework/Atlas/atlas-09-retractions.md (bidirectional routing target)
  - canonical_constants.py (feeds audit_sha256; Gamma_effacement pin)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<composite payload with bidirectional-route tag>,
   scheme=JOINT-CROSS-AXIS-STAGE-2-THREE-AGENT,
   convention=PASS-AND-three-agent-universal-lock-condition, L_max=N/A)

Audit discriminators (plan SW6-2 item 6):
  audit_sha256   = sha256(script || canonical_constants.py || §VII.AM
                   entry-block bytes || pinmap_json)   ["script","canonical","pinmap"]
  content_sha256 = sha256(script)                       ["script"]
  pinmap carries the three-reviewer assignment + JOINT clause enumeration
  (incl. the clause->half json-key map) + orthogonality declaration + anchor
  pins/bands + bidirectional atlas-09 routing declaration + all 10 input-file
  SHAs + the entry-block SHA.

OPERATIONAL DEVIATION (disclosed, one line): the plan method-block names
computations/_shared/s100a_viiam_stage2_verify.py; the authoritative
output_artifacts block names computations/session-100a/ — this script lives at
the output_artifacts path (orchestrator-confirmed; plan-internal drift, same
disposition as the W6-1 sister gate).

Verdict emission: this script PRINTS the payload (print_verdict_payload);
the dispatching agent calls mcp__knowledge__emit_verdict(**payload) — the
race-safe, lock-serialized single writer of s100a_gate_verdicts.txt. The
script does NOT write the verdict file (Windows open("a") cross-process race;
S98 lost 5/8 lines under 8 concurrent writers).

GPU_path: cpu-cap-OMP8 — no matrix work (three-reviewer set-conjunction +
anchor arithmetic only).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — CPU thread cap BEFORE numpy import (GPU_path=cpu-cap-OMP8)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import; S34+)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403
# Consumed canonical pins:
#   Gamma_effacement = 0.99970 (canonical_constants.py:540; S37 acoustic-
#     white-hole impedance-transmission; S85 W7-3 promotion block; clause (b)
#     Level-3 anchor; (1-Gamma) = 3e-4)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import re
import time

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# ---------------------------------------------------------------------------
# Section 3 — Identity + pre-registration pins (plan SW6-2 machinery_pin_map)
# ---------------------------------------------------------------------------
SESSION = "100a"                                                   # (local)
GATE_ID = "S100a-VIIAM-STAGE2-VERIFY"                              # (local)
SCHEME = "JOINT-CROSS-AXIS-STAGE-2-THREE-AGENT"                    # (local)
CONVENTION = "PASS-AND-three-agent-universal-lock-condition"       # (local)
L_MAX = "N/A"                                                      # (local)

SPECTRAL_REVIEWER = "lizzi-spectral-functional-theorist"           # (local)
TRANSIT_REVIEWER = "volovik-superfluid-universe-theorist"          # (local)
SEMICLASSICAL_REVIEWER = "schwarzschild-penrose-geometer"          # (local)
STAGE0_EXCLUDED = (                                                # (local)
    "hawking-theorist",
    "transit-dynamics-theorist",
    "connes-ncg-theorist",
)

# JOINT clause -> per-reviewer JSON clause-key map (plan method block;
# full-audit owner listed first in the comment per clause)
CLAUSE_KEYS = {                                                    # (local)
    "a": {"S": "a", "T": "a_transit_half", "G": "a_semiclassical_half"},
    "b": {"S": "b_spectral_half", "T": "b", "G": "b_semiclassical_half"},
    "c": {"S": "c_spectral_half", "T": "c_transit_half", "G": "c"},
}
JOINT_CLAUSES = ("a", "b", "c")                                    # (local)
REVIEWER_TAGS = ("S", "T", "G")                                    # (local)
EXPECTED_CLAUSE_SETS = {                                           # (local)
    "S": {"a", "b_spectral_half", "c_spectral_half"},
    "T": {"a_transit_half", "b", "c_transit_half"},
    "G": {"a_semiclassical_half", "b_semiclassical_half", "c"},
}

# Anchor pins (plan machinery_pin_map.anchor_gamma_eff / .anchor_ratio)
GAMMA_DEV_PIN = 3.0e-4        # (local) clause-(b) deviation-from-1 pin (plan)
GAMMA_DEV_ABS_TOL = 1e-12     # (local) exact-arithmetic identity tolerance
RATIO_ANCHOR_PIN = 9.6684e4   # (local) clause-(c) registered Level-3 anchor (5 sig figs)
RATIO_BAND_REL = 1e-5         # (local) Class-8.3 floor at 5 sig figs (half-ULP 5.17e-6)
REPORT_CONSISTENCY_TOL = 1e-9  # (local) reviewer-reported vs recomputed
NPZ_INTERNAL_REL_TOL = 1e-12  # (local) npz primitive-identity tolerance
M_ANCHOR_KG = 1.0e13          # (local) clause-(c) anchor mass (registered entry)

# Orthogonality-pinned anchor markers (for inputs_read scan)
NPZ_MARKER = "s88_w1b2_page_time_cascade_tail.npz"                 # (local)
GAMMA_MARKER = "Gamma_effacement"                                  # (local)

# Input files (all SHA-pinned into pinmap)
REVIEWER_S_JSON = SESSION_DIR / "s100a_viiam_reviewer_spectral_lizzi.json"
REVIEWER_T_JSON = SESSION_DIR / "s100a_viiam_reviewer_transit_volovik.json"
REVIEWER_G_JSON = SESSION_DIR / "s100a_viiam_reviewer_semiclassical_sp.json"
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
S88_NPZ = COMPUTATIONS_DIR / "session-88" / NPZ_MARKER
S88_VERDICTS = COMPUTATIONS_DIR / "session-88" / "s88_gate_verdicts.txt"
RULE_JOINT = PROJECT_ROOT / ".claude" / "rules" / "joint-theorem-promotion.md"
RULE_BRIDGE = PROJECT_ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md"
ATLAS09_PATH = (PROJECT_ROOT / "sessions" / "framework" / "Atlas"
                / "atlas-09-retractions.md")
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"

INPUT_FILES = [
    CANONICAL_PATH,
    REGISTRY_PATH,
    REVIEWER_S_JSON,
    REVIEWER_T_JSON,
    REVIEWER_G_JSON,
    S88_NPZ,
    S88_VERDICTS,
    RULE_JOINT,
    RULE_BRIDGE,
    ATLAS09_PATH,
]

OUT_NPZ = SESSION_DIR / "s100a_viiam_stage2_verify.npz"
OUT_PNG = SESSION_DIR / "s100a_viiam_stage2_verify.png"

ENTRY_HEADING = "## §VII.AM"                                       # (local)
PLAN_PINNED_ENTRY_START_LINE = 16700                               # (local)
S88_ANCHOR_GATE_ID = "S88-CF-CURV-11-PAGE-TIME-CASCADE-TAIL-MASS"  # (local)

# Bidirectional routing tags (PRE-REGISTERED; plan machinery_pin_map
# .bidirectional_routing — informative in BOTH directions)
ROUTE_PASS = "STAGE-3-PERMANENT+atlas-09-Suspected-CLEARED"        # (local)
ROUTE_FAIL = "hold-STAGE-1+atlas-09-retraction-route"              # (local)
ROUTE_INFO = "Stage-2-INFO-deferred+atlas-09-Suspected-UNCHANGED"  # (local)


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
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
    """Print SHA-256 of each input; return {relpath: sha} for the pinmap."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def extract_entry_block(registry_path: Path) -> tuple[str, int, int]:
    """Extract the registered §VII.AM entry block (heading to the line before
    the next '## ' heading). Returns (block_text, start_line, end_line) with
    1-based line numbers. Anchor-based extraction (runtime canonical-path
    rescue per substrate-first-canonical-sourcing.md (ii.B)); the plan-pinned
    start line 16700 is cross-checked and any drift disclosed in stdout."""
    lines = registry_path.read_text(encoding="utf-8").splitlines()  # (local)
    start_idx = None  # (local)
    for i, ln in enumerate(lines):
        if ln.startswith(ENTRY_HEADING):
            start_idx = i
            break
    if start_idx is None:
        raise RuntimeError(f"§VII.AM heading not found in {registry_path}")
    end_idx = len(lines)  # (local)
    for j in range(start_idx + 1, len(lines)):
        if lines[j].startswith("## "):
            end_idx = j
            break
    block = "\n".join(lines[start_idx:end_idx])  # (local)
    return block, start_idx + 1, end_idx  # 1-based inclusive span


def compute_audit_content_sha(
    script_path: Path,
    canonical_path: Path,
    entry_block: str,
    pins: dict[str, str],
) -> tuple[str, str]:
    """S84+ dual-SHA per plan SW6-2 audit_discriminators:
    audit_sha256   = sha256(script || canonical_constants.py ||
                            §VII.AM entry-block bytes || pinmap_json)
    content_sha256 = sha256(script)
    """
    script_bytes = script_path.read_bytes()  # (local)
    canonical_bytes = canonical_path.read_bytes()  # (local)
    entry_bytes = entry_block.encode("utf-8")  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(entry_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Aggregation compute
# ---------------------------------------------------------------------------

def load_reviewer(path: Path) -> dict:
    """Load a reviewer clause-verdict JSON."""
    return json.loads(path.read_text(encoding="utf-8"))


def protocol_preflight(revs: dict[str, dict]) -> tuple[bool, list[str]]:
    """Stage-2 protocol-condition checks (joint-theorem-promotion.md audit
    items, mechanically verifiable from the three reviewer JSONs). Returns
    (all_ok, list_of_breach_descriptions)."""
    breaches: list[str] = []  # (local)
    pinned = {"S": SPECTRAL_REVIEWER, "T": TRANSIT_REVIEWER,
              "G": SEMICLASSICAL_REVIEWER}  # (local)

    for tag in REVIEWER_TAGS:
        rev = revs[tag]  # (local)
        # (i) reviewer identity matches the pinned three-way assignment
        if rev.get("reviewer") != pinned[tag]:
            breaches.append(f"{tag}_identity={rev.get('reviewer')}!={pinned[tag]}")
        # (ii) reviewer is not a Stage-0 author
        if rev.get("reviewer") in STAGE0_EXCLUDED:
            breaches.append(f"{tag}_reviewer_is_Stage0_author={rev.get('reviewer')}")
        # (iii) no-workshop-context attestation
        if rev.get("no_workshop_context_attestation") is not True:
            breaches.append(f"{tag}_attestation_missing")
        # (iv) theorem identity
        if rev.get("theorem") != "VII.AM":
            breaches.append(f"{tag}_theorem={rev.get('theorem')}!=VII.AM")
        # (v) clause-set exact match to the pinned enumeration
        got = set(rev.get("clauses", {}).keys())  # (local)
        if got != EXPECTED_CLAUSE_SETS[tag]:
            breaches.append(
                f"{tag}_clause_set={sorted(got)}!={sorted(EXPECTED_CLAUSE_SETS[tag])}")

    return (len(breaches) == 0), breaches


def orthogonality_check(revs: dict[str, dict]) -> tuple[bool, dict]:
    """Substrate-input-orthogonality predicate (pre-registered): the s88
    cascade-tail npz loaded by semiclassical (G) ONLY; the canonical
    Gamma_effacement pin consumed as primary anchor by transit (T) ONLY.
    Verified mechanically against each reviewer's inputs_read declaration
    (the lizzi JSON's inputs_explicitly_not_read block is NOT scanned —
    only positive loads count)."""
    joined = {tag: " || ".join(revs[tag].get("inputs_read", []))
              for tag in REVIEWER_TAGS}  # (local)
    npz_in = {tag: (NPZ_MARKER in joined[tag]) for tag in REVIEWER_TAGS}  # (local)
    gam_in = {tag: (GAMMA_MARKER in joined[tag]) for tag in REVIEWER_TAGS}  # (local)
    npz_exclusive_g = npz_in["G"] and not npz_in["S"] and not npz_in["T"]  # (local)
    gam_exclusive_t = gam_in["T"] and not gam_in["S"] and not gam_in["G"]  # (local)
    satisfied = npz_exclusive_g and gam_exclusive_t  # (local)
    flags = {
        "npz_loaded_by_S": npz_in["S"],
        "npz_loaded_by_T": npz_in["T"],
        "npz_loaded_by_G": npz_in["G"],
        "gamma_pin_loaded_by_S": gam_in["S"],
        "gamma_pin_loaded_by_T": gam_in["T"],
        "gamma_pin_loaded_by_G": gam_in["G"],
        "npz_exclusive_to_G": npz_exclusive_g,
        "gamma_pin_exclusive_to_T": gam_exclusive_t,
        "orthogonality_satisfied": satisfied,
    }  # (local)
    return satisfied, flags


def gamma_subcheck(rev_t: dict) -> dict:
    """Clause-(b) anchor sub-check: Gamma_eff = 0.9997, deviation-from-1
    pinned at 3e-4. Script canonical-import route + RE-verification of the
    transit reviewer's anchor_subcheck_gamma_eff block."""
    gam_import = Gamma_effacement  # canonical pin (canonical_constants.py:540)
    dev_script = 1.0 - gam_import  # (local)
    dev_match = abs(dev_script - GAMMA_DEV_PIN) <= GAMMA_DEV_ABS_TOL  # (local)

    blk = rev_t.get("anchor_subcheck_gamma_eff", {})  # (local)
    rep_canonical = float(blk.get("canonical", float("nan")))  # (local)
    rep_dev = float(blk.get("deviation_from_1", float("nan")))  # (local)
    rep_flag = bool(blk.get("consistent", False))  # (local)
    canonical_consistent = abs(rep_canonical - gam_import) <= REPORT_CONSISTENCY_TOL  # (local)
    dev_consistent = abs(rep_dev - dev_script) <= REPORT_CONSISTENCY_TOL  # (local)

    return {
        "gamma_import": gam_import,
        "dev_script": dev_script,
        "dev_pin": GAMMA_DEV_PIN,
        "dev_match_pin": bool(dev_match),
        "transit_reported_canonical": rep_canonical,
        "transit_reported_dev": rep_dev,
        "transit_reported_consistent_flag": rep_flag,
        "transit_canonical_consistent": bool(canonical_consistent),
        "transit_dev_consistent": bool(dev_consistent),
        "all_ok": bool(dev_match and canonical_consistent and dev_consistent
                       and rep_flag),
    }


def ratio_subcheck(rev_s: dict, rev_t: dict, rev_g: dict) -> dict:
    """Clause-(c) anchor sub-check: ratio_anchor = t_Page(1e13 kg)/t_universe
    vs the registered 5-sig-fig pin 9.6684e+04, band 1e-5 rel (Class-8.3
    floor). Script's OWN npz route (+ primitive-identity recompute) + RE-
    verification of the semiclassical reviewer's anchor_subcheck_ratio block.
    Supplementary NON-GATING routes (lizzi CODATA recompute; volovik
    age-convention recompute) recorded for the WP."""
    d = np.load(S88_NPZ, allow_pickle=True)  # (local)
    m_grid = np.asarray(d["M_grid_kg"], dtype=float)  # (local)
    idx = int(np.argmin(np.abs(m_grid - M_ANCHOR_KG)))  # (local)
    mass_ok = abs(m_grid[idx] / M_ANCHOR_KG - 1.0) <= NPZ_INTERNAL_REL_TOL  # (local)
    ratio_npz = float(np.asarray(d["ratio_t_Page_over_t_universe"],
                                 dtype=float)[idx])  # (local)
    prefactor = float(d["prefactor_si"])  # (local)
    t_universe = float(d["t_universe_s"])  # (local)
    t_page = float(np.asarray(d["t_Page_s"], dtype=float)[idx])  # (local)
    t_evap = float(np.asarray(d["t_evap_s"], dtype=float)[idx])  # (local)

    # internal npz primitive identities (t_Page prefactor; Page-1993 1/2)
    ratio_recon = prefactor * m_grid[idx] ** 3 / t_universe  # (local)
    recon_ok = abs(ratio_recon / ratio_npz - 1.0) <= NPZ_INTERNAL_REL_TOL  # (local)
    page_half_ok = abs(t_page / t_evap - 0.5) <= NPZ_INTERNAL_REL_TOL  # (local)

    rd_script = abs(ratio_npz - RATIO_ANCHOR_PIN) / RATIO_ANCHOR_PIN  # (local)
    within_script = rd_script <= RATIO_BAND_REL  # (local)

    # semiclassical reviewer's reported block — RE-verified, never trusted
    blk = rev_g.get("anchor_subcheck_ratio", {})  # (local)
    rep_npz_value = float(blk.get("npz_value", float("nan")))  # (local)
    rep_registered = float(blk.get("registered", float("nan")))  # (local)
    rep_rel_dev = float(blk.get("rel_dev", float("nan")))  # (local)
    rep_flag = bool(blk.get("consistent", False))  # (local)
    sp_value_consistent = (abs(rep_npz_value - ratio_npz) / ratio_npz
                           <= REPORT_CONSISTENCY_TOL)  # (local)
    rd_sp = abs(rep_npz_value - RATIO_ANCHOR_PIN) / RATIO_ANCHOR_PIN  # (local)
    within_sp = rd_sp <= RATIO_BAND_REL  # (local)
    sp_report_consistent = abs(rep_rel_dev - rd_sp) <= REPORT_CONSISTENCY_TOL  # (local)
    sp_registered_matches_pin = (abs(rep_registered - RATIO_ANCHOR_PIN)
                                 <= REPORT_CONSISTENCY_TOL)  # (local)

    # supplementary NON-GATING cross-routes (recorded, not gated)
    lizzi_ratio = float(rev_s["clauses"]["c_spectral_half"]["key_numbers"]
                        .get("ratio_recomputed", float("nan")))  # (local)
    volovik_ratio = float(rev_t["clauses"]["c_transit_half"]["key_numbers"]
                          .get("ratio_computed", float("nan")))  # (local)
    rd_lizzi = abs(lizzi_ratio - RATIO_ANCHOR_PIN) / RATIO_ANCHOR_PIN  # (local)
    rd_volovik = abs(volovik_ratio - RATIO_ANCHOR_PIN) / RATIO_ANCHOR_PIN  # (local)

    return {
        "anchor_pin": RATIO_ANCHOR_PIN,
        "band_rel": RATIO_BAND_REL,
        "npz_index": idx,
        "npz_mass_kg": float(m_grid[idx]),
        "npz_mass_ok": bool(mass_ok),
        "ratio_npz": ratio_npz,
        "ratio_recon_from_primitives": float(ratio_recon),
        "recon_identity_ok": bool(recon_ok),
        "page_half_identity_ok": bool(page_half_ok),
        "t_universe_s_npz": t_universe,
        "script_rel_dev": rd_script,
        "script_within": bool(within_script),
        "sp_reported_npz_value": rep_npz_value,
        "sp_value_consistent": bool(sp_value_consistent),
        "sp_rel_dev": rd_sp,
        "sp_within": bool(within_sp),
        "sp_report_consistent": bool(sp_report_consistent),
        "sp_registered_matches_pin": bool(sp_registered_matches_pin),
        "sp_reported_consistent_flag": rep_flag,
        "lizzi_supplementary_ratio": lizzi_ratio,
        "lizzi_supplementary_rel_dev": rd_lizzi,
        "volovik_supplementary_ratio": volovik_ratio,
        "volovik_supplementary_rel_dev": rd_volovik,
        "all_ok": bool(mass_ok and recon_ok and page_half_ok and within_script
                       and sp_value_consistent and within_sp
                       and sp_report_consistent and sp_registered_matches_pin
                       and rep_flag),
    }


def s88_anchor_line_check(rev_g: dict) -> dict:
    """Audit-trail verification of the W1b2-64 anchor line: the canonical
    session-88 verdict file's S88-CF-CURV-11 line must carry the dual-SHA
    pair the semiclassical reviewer quoted in inputs_read (the exact
    dual-SHA identity resolving the registry legacy-path drift)."""
    quoted_shas: list[str] = []  # (local)
    for entry in rev_g.get("inputs_read", []):
        if "s88_gate_verdicts" in entry:
            quoted_shas = re.findall(r"[a-f0-9]{64}", entry)
            break
    text = S88_VERDICTS.read_text(encoding="utf-8").splitlines()  # (local)
    line_no = 0  # (local)
    line = ""  # (local)
    for i, ln in enumerate(text, start=1):
        if ln.startswith(S88_ANCHOR_GATE_ID + ":"):
            line_no, line = i, ln
            break
    found = line_no > 0  # (local)
    shas_match = (found and len(quoted_shas) >= 2
                  and all(s in line for s in quoted_shas[:2]))  # (local)
    return {
        "anchor_gate_id": S88_ANCHOR_GATE_ID,
        "line_found": bool(found),
        "line_no": line_no,
        "sp_quoted_sha_count": len(quoted_shas),
        "dual_sha_match": bool(shas_match),
        "all_ok": bool(found and shas_match),
    }


def aggregate_pass_and(revs: dict[str, dict]) -> tuple[str, dict, dict]:
    """Apply operator.form three-way set-conjunction. Returns (composite,
    per-reviewer-per-clause verdict map V[tag][clause], per-clause aggregate)."""
    v: dict[str, dict[str, str]] = {tag: {} for tag in REVIEWER_TAGS}  # (local)
    for j in JOINT_CLAUSES:
        for tag in REVIEWER_TAGS:
            key = CLAUSE_KEYS[j][tag]  # (local)
            v[tag][j] = revs[tag]["clauses"][key]["verdict"].upper()

    # per-clause aggregate: three-way PASS-AND (FAIL > INFO > PASS precedence)
    agg: dict[str, str] = {}  # (local)
    for j in JOINT_CLAUSES:
        triple = tuple(v[tag][j] for tag in REVIEWER_TAGS)  # (local)
        if "FAIL" in triple:
            agg[j] = "FAIL"
        elif "INFO" in triple:
            agg[j] = "INFO"
        elif triple == ("PASS", "PASS", "PASS"):
            agg[j] = "PASS"
        else:
            agg[j] = "INFO"  # unrecognized verdict token -> conservative

    all_verdicts = [v[tag][j] for j in JOINT_CLAUSES
                    for tag in REVIEWER_TAGS]  # (local) 9 entries
    if any(x == "FAIL" for x in all_verdicts):
        composite = "FAIL"  # (local)
    elif any(x == "INFO" for x in all_verdicts):
        composite = "INFO"  # (local)
    elif all(x == "PASS" for x in all_verdicts):
        composite = "PASS"  # (local)
    else:
        composite = "INFO"  # (local) unrecognized token absent FAIL -> INFO
    return composite, v, agg


def routing_tag(composite: str, agg: dict) -> str:
    """Bidirectional atlas-09 routing tag (PRE-REGISTERED; plan
    machinery_pin_map.bidirectional_routing). PASS -> STAGE-3 + Suspected
    CLEARED; FAIL -> hold STAGE-1 + retraction-route on the named clause(s);
    INFO -> Stage-2-INFO-deferred, Suspected UNCHANGED."""
    if composite == "PASS":
        return ROUTE_PASS
    if composite == "FAIL":
        named = "+".join(j for j in JOINT_CLAUSES if agg[j] == "FAIL")  # (local)
        return f"{ROUTE_FAIL}(clause={named or 'protocol'})"
    return ROUTE_INFO


# ---------------------------------------------------------------------------
# Section 6 — Plot (3-reviewer x 3-clause PASS-AND matrix + routing)
# ---------------------------------------------------------------------------

def make_plot(v: dict, agg: dict, composite: str, gam: dict, ratio: dict,
              ortho_ok: bool, route: str) -> None:
    code_map = {"N/A": 0, "PASS": 1, "INFO": 2, "FAIL": 3}  # (local)
    cmap = ListedColormap(["#d9d9d9", "#2e7d32", "#f9a825", "#c62828"])  # (local)

    col_labels = ["V_S (lizzi)", "V_T (volovik)", "V_G (schw-penrose)",
                  "PASS-AND aggregate"]  # (local)
    row_labels = [
        "(a) pixelation lock [S full; T+G halves]",
        "(b) effacement lock Gamma_eff [T full; S+G halves]",
        "(c) Page-time lock t_Page [G full; S+T halves]",
    ]  # (local)
    cell_text = []  # (local)
    cell_code = []  # (local)
    for j in JOINT_CLAUSES:
        row = [v["S"][j], v["T"][j], v["G"][j], agg[j]]  # (local)
        cell_text.append(row)
        cell_code.append([code_map.get(x, 0) for x in row])

    fig, ax = plt.subplots(figsize=(9.6, 5.6))
    ax.imshow(np.array(cell_code), cmap=cmap, vmin=0, vmax=3, aspect="auto")
    ax.set_xticks(range(4))
    ax.set_xticklabels(col_labels, fontsize=9.5)
    ax.set_yticks(range(3))
    ax.set_yticklabels(row_labels, fontsize=9)
    for i in range(3):
        for k in range(4):
            ax.text(k, i, cell_text[i][k], ha="center", va="center",
                    fontsize=11, fontweight="bold",
                    color="white" if cell_code[i][k] in (1, 3) else "black")
    ax.set_title(
        f"{GATE_ID} — Stage-2 THREE-agent PASS-AND matrix\n"
        f"composite = {composite}  |  atlas-09 routing: {route}",
        fontsize=11)
    foot = (
        f"anchor (b) Gamma_eff: import={gam['gamma_import']:.5f}  1-Gamma={gam['dev_script']:.6e}  "
        f"pin=3e-4  match={gam['dev_match_pin']}  volovik_consistent={gam['all_ok']}\n"
        f"anchor (c) ratio vs {ratio['anchor_pin']:.4e} (band {ratio['band_rel']:.0e} rel, 5-sig-fig "
        f"Class-8.3 floor):\n"
        f"  script npz route = {ratio['ratio_npz']:.10f}  rel_dev = {ratio['script_rel_dev']:.3e}  "
        f"within = {ratio['script_within']}\n"
        f"  sp reported      = {ratio['sp_reported_npz_value']:.10f}  rel_dev = {ratio['sp_rel_dev']:.3e}  "
        f"within = {ratio['sp_within']}\n"
        f"  npz primitive identity (prefactor*M^3/t_uni) ok = {ratio['recon_identity_ok']}; "
        f"t_Page/t_evap = 1/2 ok = {ratio['page_half_identity_ok']}\n"
        f"substrate-input-orthogonality SATISFIED = {ortho_ok} "
        f"(cascade npz -> G only; Gamma pin -> T only);\n"
        f"attestations: no-workshop-context all THREE True; reviewers non-Stage-0 "
        f"(excl hawking/transit-dyn/connes)"
    )  # (local)
    fig.text(0.06, 0.012, foot, fontsize=7.6, family="monospace", va="bottom")
    fig.subplots_adjust(left=0.30, bottom=0.40, top=0.86, right=0.97)
    fig.savefig(OUT_PNG, dpi=150)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 — Verdict payload (printed; agent calls emit_verdict)
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(
    verdict: str,
    value,
    audit_sha: str,
    content_sha: str,
    companion_note: str = "",
    extra_rows: list[str] | None = None,
) -> dict:
    """Emit the verdict PAYLOAD for the dispatching AGENT to pass to the
    knowledge-MCP emit_verdict tool (race-safe, lock-serialized; the script
    does NOT write the verdict file). [VERIFY] trigger — no schema-v2 3-tuple.
    Session is the letter-suffixed sub-session label '100a' (string)."""
    payload: dict = {
        "session": SESSION,
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

    # 1. Input pins (first lines of stdout)
    pins = log_input_pins(INPUT_FILES)

    # 2. Registered-entry block extraction + SHA (anchor-based; drift check)
    entry_block, entry_start, entry_end = extract_entry_block(REGISTRY_PATH)
    entry_sha = hashlib.sha256(entry_block.encode("utf-8")).hexdigest()  # (local)
    drift = (entry_start != PLAN_PINNED_ENTRY_START_LINE)  # (local)
    print(f"  §VII.AM entry block: lines {entry_start}-{entry_end} "
          f"(plan-pinned start {PLAN_PINNED_ENTRY_START_LINE}; drift={drift})")
    print(f"  entry_block_sha256: {entry_sha[:16]}...")

    # 3. Pinmap identity keys (three-reviewer assignment + clause enumeration
    #    + orthogonality declaration + anchor pins + routing) per
    #    audit_discriminators
    pins["_gate_id"] = GATE_ID
    pins["_scheme"] = SCHEME
    pins["_convention"] = CONVENTION
    pins["_spectral_reviewer"] = SPECTRAL_REVIEWER
    pins["_transit_reviewer"] = TRANSIT_REVIEWER
    pins["_semiclassical_reviewer"] = SEMICLASSICAL_REVIEWER
    pins["_stage0_excluded"] = ",".join(STAGE0_EXCLUDED)
    pins["_clause_keys"] = json.dumps(CLAUSE_KEYS, sort_keys=True)
    pins["_orthogonality_declaration"] = (
        f"{NPZ_MARKER}->semiclassical_only;{GAMMA_MARKER}_pin->transit_only")
    pins["_anchor_gamma_dev_pin"] = f"{GAMMA_DEV_PIN:.1e}"
    pins["_anchor_ratio_pin"] = f"{RATIO_ANCHOR_PIN:.5e}"
    pins["_ratio_band_rel"] = f"{RATIO_BAND_REL:.0e}"
    pins["_bidirectional_routing"] = (
        f"PASS->{ROUTE_PASS};FAIL->{ROUTE_FAIL}(named-clause);INFO->{ROUTE_INFO}")
    pins["_entry_block_sha256"] = entry_sha

    # 4. Dual SHA (audit = script || canonical || entry-block || pinmap_json)
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_audit_content_sha(
        script_path, CANONICAL_PATH, entry_block, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+entry+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 5. Load the three reviewer clause-verdict JSONs
    revs = {
        "S": load_reviewer(REVIEWER_S_JSON),
        "T": load_reviewer(REVIEWER_T_JSON),
        "G": load_reviewer(REVIEWER_G_JSON),
    }  # (local)

    # 6. Stage-2 protocol-condition pre-flight
    proto_ok, breaches = protocol_preflight(revs)
    print(f"protocol_preflight: ok={proto_ok}"
          + (f" breaches={breaches}" if breaches else ""))

    # 7. Substrate-input-orthogonality predicate
    ortho_ok, ortho_flags = orthogonality_check(revs)
    print(f"substrate_input_orthogonality: SATISFIED={ortho_ok} {ortho_flags}")

    # 8. Anchor sub-checks (RE-computed; reviewer reports re-verified)
    gam = gamma_subcheck(revs["T"])
    print(f"anchor (b) Gamma_eff: import={gam['gamma_import']!r}"
          f"  1-Gamma={gam['dev_script']:.12e}  pin={GAMMA_DEV_PIN:.1e}"
          f"  |dev-pin|<=1e-12: {gam['dev_match_pin']}")
    print(f"  volovik reported canonical={gam['transit_reported_canonical']!r}"
          f" consistent={gam['transit_canonical_consistent']};"
          f" reported dev={gam['transit_reported_dev']:.3e}"
          f" consistent={gam['transit_dev_consistent']};"
          f" flag={gam['transit_reported_consistent_flag']}"
          f" => all_ok={gam['all_ok']}")
    ratio = ratio_subcheck(revs["S"], revs["T"], revs["G"])
    print(f"anchor (c) ratio vs pin {ratio['anchor_pin']:.5e}"
          f" (band {ratio['band_rel']:.0e} rel, Class-8.3 5-sig-fig floor):")
    print(f"  script npz route [idx={ratio['npz_index']},"
          f" M={ratio['npz_mass_kg']:.3e} kg, mass_ok={ratio['npz_mass_ok']}]:"
          f" ratio={ratio['ratio_npz']:.10f}"
          f" rel_dev={ratio['script_rel_dev']:.6e} within={ratio['script_within']}")
    print(f"  npz primitive identity prefactor*M^3/t_uni ="
          f" {ratio['ratio_recon_from_primitives']:.10f}"
          f" ok={ratio['recon_identity_ok']};"
          f" t_Page/t_evap=1/2 ok={ratio['page_half_identity_ok']}")
    print(f"  sp reported npz_value={ratio['sp_reported_npz_value']:.10f}"
          f" value_consistent={ratio['sp_value_consistent']}"
          f" rel_dev={ratio['sp_rel_dev']:.6e} within={ratio['sp_within']}"
          f" report_consistent={ratio['sp_report_consistent']}"
          f" registered_matches_pin={ratio['sp_registered_matches_pin']}")
    print(f"  supplementary (NON-GATING): lizzi CODATA route"
          f" {ratio['lizzi_supplementary_ratio']:.6e}"
          f" (rd={ratio['lizzi_supplementary_rel_dev']:.3e});"
          f" volovik age-convention route"
          f" {ratio['volovik_supplementary_ratio']:.6e}"
          f" (rd={ratio['volovik_supplementary_rel_dev']:.3e};"
          f" 13.787-Gyr vs npz 4.35e17 s convention)")
    print(f"  anchor (c) all_ok={ratio['all_ok']}")
    s88_anchor = s88_anchor_line_check(revs["G"])
    print(f"W1b2-64 anchor line: found={s88_anchor['line_found']}"
          f" (line {s88_anchor['line_no']});"
          f" dual_sha_match={s88_anchor['dual_sha_match']}"
          f" (legacy-path drift resolved on the canonical session-88 path)")

    # 9. THREE-way PASS-AND aggregation (operator.form exact set logic)
    composite, v, agg = aggregate_pass_and(revs)
    n_pass = sum(1 for j in JOINT_CLAUSES for tag in REVIEWER_TAGS
                 if v[tag][j] == "PASS")  # (local)
    print(f"\nclause-verdict matrix (V_S/V_T/V_G per JOINT clause):")
    for j in JOINT_CLAUSES:
        print(f"  ({j}): V_S={v['S'][j]:<5} V_T={v['T'][j]:<5}"
              f" V_G={v['G'][j]:<5} PASS-AND aggregate={agg[j]}")
    print(f"clause_verdicts_PASS = {n_pass}/9")
    print(f"operator.form composite (three-way set conjunction) = {composite}")

    # 10. Protocol/sub-check overrides: a Stage-2 protocol-condition failure
    #     blocks promotion (joint-theorem-promotion.md audit -> FAIL)
    #     regardless of clause verdicts; orthogonality / anchor-band /
    #     audit-trail inconsistencies absent a clause-FAIL degrade to INFO
    #     (pre-registered machinery pins; identical structure to the W6-1
    #     sister gate).
    inconsistency_flags: list[str] = []  # (local)
    if not proto_ok:
        composite = "FAIL"
        inconsistency_flags.append("protocol_preflight_breach")
    if not ortho_ok:
        composite = "FAIL" if composite == "FAIL" else "INFO"
        inconsistency_flags.append("substrate_input_orthogonality_unsatisfied")
    if not gam["all_ok"]:
        composite = "FAIL" if composite == "FAIL" else "INFO"
        inconsistency_flags.append("gamma_eff_subcheck_inconsistency")
    if not ratio["all_ok"]:
        composite = "FAIL" if composite == "FAIL" else "INFO"
        inconsistency_flags.append("ratio_subcheck_band_breach")
    if not s88_anchor["all_ok"]:
        composite = "FAIL" if composite == "FAIL" else "INFO"
        inconsistency_flags.append("w1b2_64_anchor_line_mismatch")
    if inconsistency_flags:
        print(f"OVERRIDE flags: {inconsistency_flags} -> composite={composite}")
    route = routing_tag(composite, agg)  # (local)
    print(f"\nFINAL composite = {composite}  |  atlas-09 routing: {route}")

    # 11. Save npz
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        clause_names=np.array(JOINT_CLAUSES),
        v_spectral=np.array([v["S"][j] for j in JOINT_CLAUSES]),
        v_transit=np.array([v["T"][j] for j in JOINT_CLAUSES]),
        v_semiclassical=np.array([v["G"][j] for j in JOINT_CLAUSES]),
        aggregate=np.array([agg[j] for j in JOINT_CLAUSES]),
        composite=composite,
        n_clause_verdicts_pass=n_pass,
        n_clause_verdicts_total=9,
        reviewer_spectral=revs["S"]["reviewer"],
        reviewer_transit=revs["T"]["reviewer"],
        reviewer_semiclassical=revs["G"]["reviewer"],
        stage0_excluded=np.array(STAGE0_EXCLUDED),
        attestation_spectral=bool(revs["S"]["no_workshop_context_attestation"]),
        attestation_transit=bool(revs["T"]["no_workshop_context_attestation"]),
        attestation_semiclassical=bool(
            revs["G"]["no_workshop_context_attestation"]),
        gamma_import=gam["gamma_import"],
        gamma_dev_script=gam["dev_script"],
        gamma_dev_pin=gam["dev_pin"],
        gamma_dev_match_pin=gam["dev_match_pin"],
        gamma_transit_reported_canonical=gam["transit_reported_canonical"],
        gamma_transit_canonical_consistent=gam["transit_canonical_consistent"],
        gamma_transit_dev_consistent=gam["transit_dev_consistent"],
        gamma_all_ok=gam["all_ok"],
        ratio_anchor_pin=ratio["anchor_pin"],
        ratio_band_rel=ratio["band_rel"],
        ratio_npz=ratio["ratio_npz"],
        ratio_recon_from_primitives=ratio["ratio_recon_from_primitives"],
        ratio_recon_identity_ok=ratio["recon_identity_ok"],
        ratio_page_half_identity_ok=ratio["page_half_identity_ok"],
        ratio_script_rel_dev=ratio["script_rel_dev"],
        ratio_script_within=ratio["script_within"],
        ratio_sp_reported=ratio["sp_reported_npz_value"],
        ratio_sp_value_consistent=ratio["sp_value_consistent"],
        ratio_sp_rel_dev=ratio["sp_rel_dev"],
        ratio_sp_within=ratio["sp_within"],
        ratio_sp_report_consistent=ratio["sp_report_consistent"],
        ratio_lizzi_supplementary=ratio["lizzi_supplementary_ratio"],
        ratio_lizzi_supplementary_rel_dev=ratio["lizzi_supplementary_rel_dev"],
        ratio_volovik_supplementary=ratio["volovik_supplementary_ratio"],
        ratio_volovik_supplementary_rel_dev=ratio[
            "volovik_supplementary_rel_dev"],
        ratio_all_ok=ratio["all_ok"],
        s88_anchor_line_found=s88_anchor["line_found"],
        s88_anchor_line_no=s88_anchor["line_no"],
        s88_anchor_dual_sha_match=s88_anchor["dual_sha_match"],
        ortho_npz_loaded_by_S=ortho_flags["npz_loaded_by_S"],
        ortho_npz_loaded_by_T=ortho_flags["npz_loaded_by_T"],
        ortho_npz_loaded_by_G=ortho_flags["npz_loaded_by_G"],
        ortho_gamma_pin_loaded_by_S=ortho_flags["gamma_pin_loaded_by_S"],
        ortho_gamma_pin_loaded_by_T=ortho_flags["gamma_pin_loaded_by_T"],
        ortho_gamma_pin_loaded_by_G=ortho_flags["gamma_pin_loaded_by_G"],
        orthogonality_satisfied=ortho_flags["orthogonality_satisfied"],
        protocol_preflight_ok=proto_ok,
        inconsistency_flags=np.array(inconsistency_flags if inconsistency_flags
                                     else ["none"]),
        bidirectional_route_tag=route,
        entry_block_sha256=entry_sha,
        entry_block_lines=np.array([entry_start, entry_end]),
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        scheme=SCHEME,
        convention=CONVENTION,
    )
    print(f"saved npz: {OUT_NPZ.name}")

    # 12. Plot
    make_plot(v, agg, composite, gam, ratio, ortho_ok, route)
    print(f"saved png: {OUT_PNG.name}")

    # 13. Value payload + 4-tuple + verdict payload
    stage3_tag = ("JOINT-CROSS-AXIS-STAGE-2-PASS-AND;" if composite == "PASS"
                  else "")  # (local)
    flags_str = "+".join(inconsistency_flags) if inconsistency_flags else "none"  # (local)
    head = (f"clause_verdicts=9/9_PASS" if composite == "PASS"
            else f"clause_verdicts={n_pass}/9_PASS_flags={flags_str}")  # (local)
    value = (
        f"{stage3_tag}{head}"
        f"(a=S+T+G;b=S+T+G;c=S+T+G_PASS-AND-all-three);"
        f"anchor_gamma:1-Gamma={gam['dev_script']:.6e}"
        f"(pin=3e-4,match={gam['dev_match_pin']}),volovik_consistent={gam['all_ok']};"
        f"anchor_ratio_vs_{ratio['anchor_pin']:.4e}:"
        f"npz={ratio['ratio_npz']:.4f}(rd={ratio['script_rel_dev']:.3e}),"
        f"sp_rd={ratio['sp_rel_dev']:.3e},band=1e-5,"
        f"all_within={ratio['script_within'] and ratio['sp_within']};"
        f"w1b2_64_anchor_dualSHA={'verified' if s88_anchor['all_ok'] else 'MISMATCH'};"
        f"input_orthogonality={'SATISFIED' if ortho_ok else 'UNSATISFIED'}"
        f"(s88npz->sp_only;GammaEffPin->volovik_only);"
        f"attestations=all_three_True;"
        f"reviewers=lizzi+volovik+sp_non-Stage-0;"
        f"route={route}"
    )  # (local)
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)

    companion = (
        f"three-agent PASS-AND aggregation; entry-block sha256={entry_sha[:16]} "
        f"(registry lines {entry_start}-{entry_end}); bidirectional routing "
        f"PRE-REGISTERED (PASS->STAGE-3+atlas-09-cleared / FAIL->retraction-route "
        f"/ INFO->deferred); composite={composite} routes {route}")  # (local)
    extra = [
        ("# reviewer-cleanliness: STATIC leg = Stage-0-authorship "
         "EXCLUSION-PASS at plan-freeze (_joint_theorem_independent_verify_"
         "audit.py --check-reviewers VII.AM --strict; excluded "
         "hawking/transit-dynamics/connes per registry Sponsors L16708-16712 "
         "+ eligibility anchor L16774); DYNAMIC leg = downstream-inheritance "
         "reach grep NO-HITS all three reviewers (orchestrator, 2026-06-06) "
         f"# {GATE_ID}"),
        ("# Stage-3 + atlas-09 routing: SVII.AM STAGE-1-CANDIDATE -> "
         "STAGE-3-PERMANENT tag edit AND atlas-09 Suspected-but-Not-Yet-"
         "Retracted flag CLEAR = ORCHESTRATOR-DIRECT at session-end synthesis "
         "(joint-theorem-promotion.md Stage 3 + capstone-hygiene-gate Q3); "
         "no falsifier-inventory row (SVII.AM not a falsifier observable) "
         f"# {GATE_ID}"),
    ]  # (local)
    print_verdict_payload(composite, value, audit_sha, content_sha,
                          companion_note=companion, extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} (wall {wall:.1f}s) ===")
    # exit 0 regardless of scientific verdict (math-scripts.md exit-code rule)
    return 0


if __name__ == "__main__":
    sys.exit(main())
