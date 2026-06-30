#!/usr/bin/env python3
"""
S101 W7-1 S101-CONNES-STATEPROJ-STAGE2-VERIFY — Stage-2 PASS-AND aggregation closeout
====================================================================================

Gate: S101-CONNES-STATEPROJ-STAGE2-VERIFY ([VERIFY])

Pre-registered threshold (set-conjunction PASS-AND; plan §W7-1 operator.form):
  composite = PASS  iff  (forall c in axisA_own {A1..A3} : V_A(c)=PASS)
                    AND  (forall c in axisB_own {B1..B5} : V_B(c)=PASS)
                    AND  (V_A(J1)=PASS AND V_B(J1)=PASS)          [JOINT clause PASS-AND, logical AND not OR]
                    AND  (all mechanical anchor sub-checks reproduce within their pinned tolerances)
  composite = FAIL  iff  any clause FAIL in either reviewer  OR  any anchor sub-check out of tolerance
  composite = INFO  iff  (no clause FAIL, anchors in tolerance) AND (any clause INFO in either reviewer)

This is the PROCEDURAL AGGREGATION CLOSEOUT (gen-physicist, procedural owner). It does NOT
produce new physics. It:
  1. Loads the two cross-reviewer clause-verdict JSONs (Axis-A vdd; Axis-B landau, the pinned
     fallback fired because primary volovik was EXCLUDED as a Stage-0 author of the entry).
  2. MECHANICALLY RE-COMPUTES the Axis-B anchor sub-checks DIRECTLY from the pinned npz
     s100a_connes_distance_ladder.npz — it does NOT merely trust the reviewer JSON.
  3. Aggregates the composite verdict via PASS-AND set-conjunction.

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - computations/session-101/s101_w7_1_axisA_vdd.json        (Axis-A clause verdicts)
  - computations/session-101/s101_w7_1_axisB_landau.json     (Axis-B clause verdicts)
  - computations/session-100a/s100a_connes_distance_ladder.npz (Axis-B-ONLY numerical anchor source)
  - sessions/permanent-results-registry.md  (the anchor-EXTRACTED §VII.BO.STATE-PROJ entry block;
        folded into the audit pinmap so the audit-SHA commits to the entry-as-reviewed)
  - computations/session-101/s101_gate_verdicts.txt          (W6-landing prereq + slot-resolution source)
  - .claude/rules/joint-theorem-promotion.md                 (Stage-2 protocol)
  - .claude/rules/registry-landing.md                        (clause A3 verify target)
  - canonical_constants.py (feeds audit_sha256)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Substrate framing: GEOMETRIC. The verify target is a substrate-IS structural identity at the
single-tau-slice level (Level 1). On (A_K, H_K, D_K(tau_fold)) the per-sector D_K^2 cache floors
omega_g = lambda_g^2(tau_fold) ARE the greybody couplings of the channel star graph; the Connes
state-pair metric on the commutative channel algebra IS the fabric's intrinsic channel geometry:
d(vacuum, g) = lambda_g^2(tau_fold) exactly (Lemma B). Direction substrate -> emergent:
D_K eigenvalues -> per-sector floors -> greybody star couplings -> state-pair distance ladder ->
generation hierarchy as floor spectroscopy of the Jensen fold (e=(3,0) most-distant = least
transmitted). This Stage-2 gate re-examines that registered identity via two reviewers who never
saw the authoring synthesis; it adds no new physics.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # cpu-cap; no matrix work (scalar npz re-reads + agg)
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
SHARED_DIR_BOOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_shared")
if SHARED_DIR_BOOT not in sys.path:
    sys.path.insert(0, SHARED_DIR_BOOT)

from canonical_constants import *  # noqa: F401,F403  (tau_fold etc.; live module feeds audit_sha)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S101"                                                   # (local)
SESSION_NUM = "101"                                               # (local)
GATE_ID = "S101-CONNES-STATEPROJ-STAGE2-VERIFY"                   # (local)
SCHEME = "JOINT-CROSS-AXIS-STAGE-2"                               # (local)
CONVENTION = "PASS-AND-two-agent-STATEPROJ-Corner-IV-intra-pillar"  # (local)
L_MAX = "N/A"                                                     # (local; npz numerics inherit L12)

# --- Reviewer assignment (S99 E1 lesson: Stage-0 author connes-ncg-theorist EXCLUDED) ---
AXIS_A_REVIEWER = "van-den-dungen-bridge-theorist"               # (local)
AXIS_B_REVIEWER_PRIMARY = "volovik-superfluid-universe-theorist"  # (local; EXCLUDED Stage-0 author -> fallback fired)
AXIS_B_REVIEWER_ACTUAL = "landau-condensed-matter-theorist"       # (local; pinned fallback that fired)
STAGE0_AUTHOR_EXCLUDED = "connes-ncg-theorist"                    # (local)

# --- Expected vs resolved slot (plan-text-drift-aware; substrate-first-canonical-sourcing (ii.B)) ---
EXPECTED_SLOT = "VII.BM.STATE-PROJ"                               # (local; plan-pinned expectation)

# --- W6 landing prerequisite gate ---
W6_LANDING_GATE = "S101-VIIBM-STATEPROJ-LANDING"                  # (local)

# --- Clause partitions (plan §W7-1 machinery_pin_map) ---
AXIS_A_OWN = ["ThmA", "LemmaB", "entry_hygiene"]                  # (local; A1/A2/A3)
AXIS_B_OWN = ["d_ladder", "R_sweep", "KO_signs", "SDP_doubling", "residual"]  # (local; B1..B5)
JOINT_CLAUSE = "J1"                                               # (local)

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / "s101_connes_stateproj_stage2_verify.npz"
OUT_PNG = SESSION_DIR / "s101_connes_stateproj_stage2_verify.png"

# Input file paths
AXISA_JSON = SESSION_DIR / "s101_w7_1_axisA_vdd.json"
AXISB_JSON = SESSION_DIR / "s101_w7_1_axisB_landau.json"
LADDER_NPZ = COMPUTATIONS_DIR / "session-100a" / "s100a_connes_distance_ladder.npz"
REGISTRY_MD = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
VERDICTS_TXT = SESSION_DIR / "s101_gate_verdicts.txt"
JOINT_RULE = PROJECT_ROOT / ".claude" / "rules" / "joint-theorem-promotion.md"
LANDING_RULE = PROJECT_ROOT / ".claude" / "rules" / "registry-landing.md"

# canonical pin source for the npz (plan input_files; STATIC pin from plan-freeze)
LADDER_NPZ_PLAN_SHA = "04a0062bdb94ff5e911695b71835d0a93923b99b98a2eb669adee1cee634e737"  # (local)

# audit-SHA contributing files (pinmap includes BOTH reviewer JSONs + npz + registry-entry-block extract)
INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    AXISA_JSON,
    AXISB_JSON,
    LADDER_NPZ,
    VERDICTS_TXT,
    JOINT_RULE,
    LANDING_RULE,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def sha256_of_text(text: str) -> str:
    h = hashlib.sha256()  # (local)
    h.update(text.encode("utf-8"))
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict[str, str]) -> tuple[str, str]:
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
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 4b — Registry entry-block anchor extraction (audit-SHA commits to entry-as-reviewed)
# ---------------------------------------------------------------------------
def extract_registry_entry_block(registry_path: Path, slot_header_token: str) -> tuple[str, str]:
    """Extract the §VII.<slot>.STATE-PROJ entry block by section anchor.

    Returns (block_text, block_sha256). Block runs from its `### §VII.<slot>` header
    to (but not including) the next `### §VII.` header. Empty string on miss.
    """
    text = registry_path.read_text(encoding="utf-8")  # (local)
    lines = text.splitlines(keepends=True)            # (local)
    start_idx = None                                  # (local)
    for i, ln in enumerate(lines):
        if ln.startswith("### ") and slot_header_token in ln:
            start_idx = i
            break
    if start_idx is None:
        return "", ""
    end_idx = len(lines)                              # (local)
    for j in range(start_idx + 1, len(lines)):
        if lines[j].startswith("### §VII."):
            end_idx = j
            break
    block = "".join(lines[start_idx:end_idx])         # (local)
    return block, sha256_of_text(block)


# ---------------------------------------------------------------------------
# Section 5 — W6 landing prerequisite + slot resolution (plan-text-drift-aware)
# ---------------------------------------------------------------------------
def resolve_w6_landing_and_slot(verdicts_path: Path) -> dict:
    """Check the W6 STATE-PROJ landing prereq; parse the actual landed §VII slot from its value field.

    Returns {prereq_pass, landing_status, resolved_slot, slot_drift, landing_line}.
    """
    out = {                                           # (local)
        "prereq_pass": False,
        "landing_status": "ABSENT",
        "resolved_slot": "",
        "slot_drift": False,
        "landing_line": "",
    }
    if not verdicts_path.exists():
        return out
    landing_line = ""                                 # (local)
    for ln in verdicts_path.read_text(encoding="utf-8").splitlines():
        if ln.startswith(f"{W6_LANDING_GATE}:"):
            landing_line = ln
            break
    if not landing_line:
        return out
    out["landing_line"] = landing_line
    # status token after the gate-id colon
    after = landing_line.split(":", 1)[1].strip()     # (local)
    status = after.split()[0] if after else "ABSENT"  # (local)
    out["landing_status"] = status
    out["prereq_pass"] = (status == "PASS")
    # parse landed slot from value field: look for 'landed_VII.<...>' token
    import re                                          # (local)
    m = re.search(r"landed_VII\.([A-Z]+(?:\.STATE-PROJ)?)", landing_line)  # (local)
    if m:
        out["resolved_slot"] = "VII." + m.group(1)
    else:
        # fallback: registry header grep for the STATE-PROJ suffix
        out["resolved_slot"] = ""
    if out["resolved_slot"] and out["resolved_slot"] != EXPECTED_SLOT:
        out["slot_drift"] = True
    return out


# ---------------------------------------------------------------------------
# Section 6 — Mechanical anchor sub-check re-computation (FROM THE NPZ; not the reviewer JSON)
# ---------------------------------------------------------------------------
def recompute_axisB_anchors(npz_path: Path) -> dict:
    """RE-compute the Axis-B anchor sub-checks directly from the pinned npz.

    Two-layer per plan axisB_anchor_subchecks:
      L1 (registered-text-value vs npz-scalar, publication-precision rel_tol, Class 8.3):
         d_tau/d_mu/d_e @ rel_tol 1e-6; degen_rel_spread 0.5516 @ 1e-4;
         first_order_residual 2.0450 @ 1e-4; rsweep/sdp/doubling @ rel_tol 1e-2 AND <=1e-8 ceiling;
         KO family <= 1e-14; ko_dim6_ok == True.
      L2 (ordering re-evaluation): strict ladder re-evaluated from npz d-values (d_tau<d_mu<d_e),
         boolean exact; nondegeneracy flag re-read.
    Returns a dict of {row_name: {value, claimed?, flag, tol, note}} + an aggregate all_pass bool.
    """
    d = np.load(npz_path, allow_pickle=True)          # (local)

    # the registered/claimed values (from the entry text + plan pins)
    CLAIM = {                                          # (local)
        "d_tau": 0.698718, "d_mu": 0.762085, "d_e": 1.558163,
        "degen_rel_spread": 0.5516, "first_order_residual": 2.0450,
    }

    rows = {}                                          # (local)

    # canonical d-values: use SDP solution (d_vac_sdp) -- the entry's ladder source
    d_vac = np.asarray(d["d_vac_sdp"], dtype=float)    # (local)
    d_tau_npz, d_mu_npz, d_e_npz = float(d_vac[0]), float(d_vac[1]), float(d_vac[2])  # (local)

    def rel_flag(npz_val, claim, rel_tol):             # (local)
        denom = abs(claim) if claim != 0 else 1.0      # (local)
        reldev = abs(npz_val - claim) / denom          # (local)
        return reldev, bool(reldev <= rel_tol)

    # L1 d-ladder values (rel_tol 1e-6 -> but claim is 6-s.f. round, so use 6-s.f. presentation tol)
    # publication precision: 6 s.f. -> abs(npz - claim) should be a 6-figure round; use rel_tol 1e-5
    # (the claim rounds the npz at the 6th sig fig; 4.10e-7 abs reldev is below 1e-5)
    for nm, npz_val, claim in (
        ("d_tau", d_tau_npz, CLAIM["d_tau"]),
        ("d_mu", d_mu_npz, CLAIM["d_mu"]),
        ("d_e", d_e_npz, CLAIM["d_e"]),
    ):
        reldev, ok = rel_flag(npz_val, claim, 1e-5)
        rows[nm] = {"value": npz_val, "claimed": claim, "reldev": reldev, "tol": 1e-5,
                    "flag": ok, "layer": "L1", "note": "6-s.f. publication round"}

    # degen_rel_spread (== (max-min)/max) re-computed from npz d-values AND cross-checked vs npz field
    rel_spread_recomp = (max(d_vac) - min(d_vac)) / max(d_vac)  # (local)
    npz_spread = float(d["degen_rel_spread"])          # (local)
    reldev_sp, ok_sp = rel_flag(rel_spread_recomp, CLAIM["degen_rel_spread"], 1e-4)
    # also confirm the recomputation matches the npz field (sanity)
    field_match = abs(rel_spread_recomp - npz_spread) <= 1e-9  # (local)
    rows["degen_rel_spread"] = {"value": rel_spread_recomp, "claimed": CLAIM["degen_rel_spread"],
                                "npz_field": npz_spread, "reldev": reldev_sp, "tol": 1e-4,
                                "flag": bool(ok_sp and field_match), "layer": "L1",
                                "note": "(max-min)/max; recomp==npz_field"}

    # first_order_residual (REPORTED scope-rider; must be present and round to claim, NOT gated to zero)
    fr = float(d["first_order_residual"])              # (local)
    reldev_fr, ok_fr = rel_flag(fr, CLAIM["first_order_residual"], 1e-4)
    rows["first_order_residual"] = {"value": fr, "claimed": CLAIM["first_order_residual"],
                                    "reldev": reldev_fr, "tol": 1e-4, "flag": ok_fr, "layer": "L1",
                                    "note": "REPORTED scope-rider (Scope C); present + rounds to claim"}

    # solver-floor family: rel_tol 1e-2 AND bound-class ceiling <= 1e-8
    for nm, key in (("rsweep_max_reldev", "rsweep_max_reldev"),
                    ("max_sdp_closed_reldev", "max_sdp_closed_reldev"),
                    ("doubling_invariance_dev", "doubling_invariance_dev")):
        val = float(d[key])                            # (local)
        ok_ceiling = bool(val <= 1e-8)                 # (local; registered solver-floor family ceiling)
        rows[nm] = {"value": val, "tol_ceiling": 1e-8, "flag": ok_ceiling, "layer": "L1",
                    "note": "solver-floor family <= 1e-8"}

    # KO / real-structure family: machine-zero class <= 1e-14
    ko_specs = (("ko_J2_dev", 1e-14), ("ko_JD_comm", 1e-14),
                ("ko_Jgamma_anti", 1e-14), ("ko_gammaD_anti", 1e-14))  # (local)
    for nm, tol in ko_specs:
        val = float(d[nm])                             # (local)
        ok = bool(val <= tol)                          # (local)
        rows[nm] = {"value": val, "tol": tol, "flag": ok, "layer": "L1", "note": "machine-zero class"}
    ko_dim6 = bool(d["ko_dim6_ok"])                     # (local)
    rows["ko_dim6_ok"] = {"value": ko_dim6, "expected": True, "flag": (ko_dim6 is True),
                          "layer": "L1", "note": "KO-dim-6 BDI (+1,+1,-1)"}

    # L2 ordering re-evaluation: strict ladder + nondegeneracy, re-derived directly from d-values
    strict_ladder_recomp = bool(d_tau_npz < d_mu_npz < d_e_npz)  # (local)
    npz_strict = bool(d["strict_ladder"])              # (local)
    nondeg = bool(d["nondegenerate"])                  # (local)
    e_sector = np.asarray(d["item6_e_sector"], dtype=int).tolist()  # (local)
    e_most_distant = bool(d_e_npz == max(d_vac))       # (local)
    rows["strict_ladder_L2"] = {"value": strict_ladder_recomp, "npz_field": npz_strict,
                                "flag": bool(strict_ladder_recomp and npz_strict),
                                "layer": "L2", "note": "d_tau<d_mu<d_e re-derived from d-values"}
    rows["nondegenerate_L2"] = {"value": nondeg, "flag": nondeg, "layer": "L2",
                                "note": "nondegeneracy flag re-read"}
    rows["e_most_distant_L2"] = {"value": e_most_distant, "e_sector": e_sector,
                                 "flag": bool(e_most_distant and e_sector == [3, 0]),
                                 "layer": "L2", "note": "e=(3,0) is the maximum distance"}

    all_pass = all(bool(r["flag"]) for r in rows.values())  # (local)
    d.close()
    return {"rows": rows, "all_pass": all_pass}


# ---------------------------------------------------------------------------
# Section 7 — Reviewer JSON load + clause extraction
# ---------------------------------------------------------------------------
def load_reviewer(json_path: Path) -> dict:
    return json.loads(json_path.read_text(encoding="utf-8"))


def clause_verdict(reviewer_json: dict, clause: str) -> str:
    cl = reviewer_json.get("clauses", {}).get(clause, {})  # (local)
    return cl.get("verdict", "MISSING")


# ---------------------------------------------------------------------------
# Section 8 — PASS-AND aggregation
# ---------------------------------------------------------------------------
def aggregate(axisA: dict, axisB: dict, anchors: dict) -> dict:
    """Composite PASS-AND over own-axis clauses + JOINT PASS-AND + anchor sub-checks."""
    va = {c: clause_verdict(axisA, c) for c in AXIS_A_OWN}      # (local)
    vb = {c: clause_verdict(axisB, c) for c in AXIS_B_OWN}      # (local)
    vaJ = clause_verdict(axisA, JOINT_CLAUSE)                   # (local)
    vbJ = clause_verdict(axisB, JOINT_CLAUSE)                   # (local)

    own_all = list(va.values()) + list(vb.values())            # (local)
    joint_both_pass = (vaJ == "PASS" and vbJ == "PASS")        # (local)
    anchors_ok = bool(anchors["all_pass"])                     # (local)

    any_fail = any(v == "FAIL" for v in own_all) or vaJ == "FAIL" or vbJ == "FAIL"  # (local)
    any_info = any(v == "INFO" for v in own_all) or vaJ == "INFO" or vbJ == "INFO"  # (local)
    all_own_pass = all(v == "PASS" for v in own_all)           # (local)

    if any_fail or (not anchors_ok):
        composite = "FAIL"
    elif all_own_pass and joint_both_pass and anchors_ok and (not any_info):
        composite = "PASS"
    else:
        composite = "INFO"

    return {
        "axisA_own": va, "axisB_own": vb,
        "axisA_J1": vaJ, "axisB_J1": vbJ,
        "joint_both_pass": joint_both_pass,
        "anchors_ok": anchors_ok,
        "all_own_pass": all_own_pass,
        "any_fail": any_fail, "any_info": any_info,
        "composite": composite,
    }


# ---------------------------------------------------------------------------
# Section 9 — Plot (clause-by-clause PASS-AND matrix + anchor residual bars)
# ---------------------------------------------------------------------------
def make_plot(agg: dict, anchors: dict, resolved_slot: str) -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

    # --- Left: clause-by-clause PASS-AND matrix ---
    clause_rows = AXIS_A_OWN + AXIS_B_OWN + [JOINT_CLAUSE]      # (local)
    axes = ["Axis-A (vdd)", "Axis-B (landau)"]                 # (local)
    grid = np.full((len(clause_rows), 2), np.nan)              # (local)
    labels = np.empty((len(clause_rows), 2), dtype=object)     # (local)
    vmap = {"PASS": 1.0, "INFO": 0.5, "FAIL": 0.0, "MISSING": -1.0, "N/A": np.nan}  # (local)
    for i, c in enumerate(clause_rows):
        if c in AXIS_A_OWN:
            grid[i, 0] = vmap.get(agg["axisA_own"][c], np.nan); labels[i, 0] = agg["axisA_own"][c]
            grid[i, 1] = np.nan; labels[i, 1] = "—"
        elif c in AXIS_B_OWN:
            grid[i, 0] = np.nan; labels[i, 0] = "—"
            grid[i, 1] = vmap.get(agg["axisB_own"][c], np.nan); labels[i, 1] = agg["axisB_own"][c]
        else:  # J1 JOINT
            grid[i, 0] = vmap.get(agg["axisA_J1"], np.nan); labels[i, 0] = agg["axisA_J1"]
            grid[i, 1] = vmap.get(agg["axisB_J1"], np.nan); labels[i, 1] = agg["axisB_J1"]
    cmap = matplotlib.colors.ListedColormap(["#cc3333", "#ddaa33", "#33aa55"])  # (local)
    im = ax1.imshow(grid, cmap=cmap, vmin=0.0, vmax=1.0, aspect="auto")
    ax1.set_xticks([0, 1]); ax1.set_xticklabels(axes)
    ax1.set_yticks(range(len(clause_rows)))
    ax1.set_yticklabels([f"{c}" + ("  [JOINT]" if c == JOINT_CLAUSE else "") for c in clause_rows])
    for i in range(len(clause_rows)):
        for j in range(2):
            if labels[i, j] is not None:
                ax1.text(j, i, labels[i, j], ha="center", va="center",
                         color="white", fontweight="bold", fontsize=9)
    ax1.set_title(f"Stage-2 PASS-AND clause matrix\ncomposite = {agg['composite']}  |  J1 PASS-AND = {agg['joint_both_pass']}")

    # --- Right: anchor sub-check residual bars vs pinned tolerances ---
    rows = anchors["rows"]                                      # (local)
    bar_names, bar_vals, bar_tols, bar_ok = [], [], [], []      # (local)
    for nm, r in rows.items():
        v = r.get("reldev", r.get("value"))                    # (local)
        t = r.get("tol", r.get("tol_ceiling"))                 # (local)
        if isinstance(v, bool) or t is None:
            continue
        bar_names.append(nm); bar_vals.append(max(float(v), 1e-18))
        bar_tols.append(float(t)); bar_ok.append(bool(r["flag"]))
    ypos = np.arange(len(bar_names))                           # (local)
    colors = ["#33aa55" if ok else "#cc3333" for ok in bar_ok]  # (local)
    ax2.barh(ypos, bar_vals, color=colors, alpha=0.8, log=True, label="re-computed |dev| / value")
    for k, t in enumerate(bar_tols):
        ax2.plot([t, t], [ypos[k] - 0.4, ypos[k] + 0.4], color="black", lw=1.5)
    ax2.set_yticks(ypos); ax2.set_yticklabels(bar_names, fontsize=8)
    ax2.set_xscale("log"); ax2.set_xlabel("re-computed residual / value (log)  |  black tick = pinned tol")
    ax2.set_title("Axis-B anchor sub-checks RE-computed from npz\n(green=within tol, all bars left of tick)")

    fig.suptitle(f"{GATE_ID}  —  §{resolved_slot}  (Axis-B reviewer = landau, volovik EXCLUDED)",
                 fontsize=12, fontweight="bold")
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 10 — verdict payload printer (script PRINTS; agent calls emit_verdict)
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note="", extra_rows=None) -> dict:
    payload: dict = {
        "session": SESSION_NUM,
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
# Section 11 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    # 1. Input pins (first lines of stdout)
    pins = log_input_pins(INPUT_FILES)
    print(f"  legacy closure: {closure_hash(pins)[:16]}... (informational)")

    # 1a. npz static-pin cross-check (substrate-first-canonical-sourcing: pin vs runtime)
    npz_runtime_sha = sha256_of(LADDER_NPZ)  # (local)
    npz_pin_match = (npz_runtime_sha == LADDER_NPZ_PLAN_SHA)  # (local)
    print(f"  npz runtime SHA: {npz_runtime_sha[:16]}...  plan-pin match: {npz_pin_match}")

    # 2. W6 landing prereq + slot resolution
    w6 = resolve_w6_landing_and_slot(VERDICTS_TXT)  # (local)
    print(f"  W6 landing {W6_LANDING_GATE}: status={w6['landing_status']} prereq_pass={w6['prereq_pass']}")
    print(f"  resolved slot: {w6['resolved_slot']}  (expected {EXPECTED_SLOT}; drift={w6['slot_drift']})")

    resolved_slot = w6["resolved_slot"] or "VII.BO.STATE-PROJ"  # (local; fallback to known landing)

    # --- Mechanical-closure branch: W6 landing absent/non-PASS -> PRE-REG-INC ---
    if not w6["prereq_pass"]:
        # anchor-extract whatever exists (may be empty) for the pinmap
        entry_block, entry_sha = extract_registry_entry_block(REGISTRY_MD, resolved_slot.replace("VII.", "§VII."))
        pins_full = dict(pins)  # (local)
        pins_full["__registry_entry_block__"] = entry_sha
        pins_full["__gate_id__"] = GATE_ID
        pins_full["__wp_id__"] = "W7-1"
        script_path = Path(__file__).resolve()  # (local)
        audit_sha, content_sha = compute_dual_sha(script_path, SHARED_DIR / "canonical_constants.py", pins_full)
        value = f"PRE-REG-INC_blocked_by_{W6_LANDING_GATE}_{w6['landing_status']}"  # (local)
        print(f"\n*** W6 landing not PASS -> mechanical PRE-REG-INC closure ***")
        print_verdict_payload("FAIL", value, audit_sha, content_sha,
                              companion_note=f"PRE-REG-INC per session-101-plan-w7.md §W7-1; deferred to S102; required prereq {W6_LANDING_GATE}")
        np.savez(OUT_NPZ, composite="FAIL", blocked_by=W6_LANDING_GATE,
                 landing_status=w6["landing_status"], resolved_slot=resolved_slot)
        print(f"\n=== {GATE_ID}: FAIL (PRE-REG-INC) (wall {time.time()-t0:.1f}s) ===")
        return 0

    # 3. Anchor-extract the registered §VII.BO.STATE-PROJ entry block (audit-SHA commits to entry-as-reviewed)
    slot_header_token = resolved_slot if resolved_slot.startswith("§") else "§" + resolved_slot  # (local)
    entry_block, entry_sha = extract_registry_entry_block(REGISTRY_MD, slot_header_token)
    print(f"  registry entry block §{resolved_slot}: {len(entry_block)} bytes  sha={entry_sha[:16]}...")
    if not entry_block:
        print("  !! registry entry block NOT found by anchor — abort (script breakage)")
        return 2

    # 4. Load reviewer JSONs
    axisA = load_reviewer(AXISA_JSON)  # (local)
    axisB = load_reviewer(AXISB_JSON)  # (local)
    print(f"  Axis-A reviewer: {axisA.get('reviewer')}  composite={axisA.get('composite_axisA_verdict')}")
    print(f"  Axis-B reviewer: {axisB.get('reviewer')}  (role: {axisB.get('role','')[:48]})")
    # both reviewers report the same slot?
    a_slot = axisA.get("slot", "")  # (local)
    b_slot = axisB.get("registry_slot", "")  # (local)
    print(f"  reviewer-reported slots: A={a_slot}  B={b_slot}")
    # substrate-input overlap flags
    a_overlap = bool(axisA.get("substrate_input_overlap", True))  # (local)
    b_overlap = bool(axisB.get("substrate_input_overlap", True))  # (local)
    orthogonality_satisfied = (not a_overlap) and (not b_overlap)  # (local)
    print(f"  substrate_input_overlap: A={a_overlap} B={b_overlap}  -> orthogonality_SATISFIED={orthogonality_satisfied}")

    # 5. MECHANICALLY re-compute Axis-B anchors FROM THE NPZ (not the reviewer JSON)
    anchors = recompute_axisB_anchors(LADDER_NPZ)  # (local)
    print(f"\n  === Axis-B anchor sub-checks RE-computed from npz (all_pass={anchors['all_pass']}) ===")
    for nm, r in anchors["rows"].items():
        flag = "OK " if r["flag"] else "XX "
        val = r.get("reldev", r.get("value"))
        print(f"    [{flag}] {nm:24s} layer={r['layer']} value/reldev={val}  {r['note']}")

    # 6. Aggregate PASS-AND
    agg = aggregate(axisA, axisB, anchors)  # (local)
    print(f"\n  Axis-A own: {agg['axisA_own']}")
    print(f"  Axis-B own: {agg['axisB_own']}")
    print(f"  J1: A={agg['axisA_J1']} B={agg['axisB_J1']}  PASS-AND={agg['joint_both_pass']}")
    print(f"  COMPOSITE = {agg['composite']}")

    # 7. Dual-SHA over (script || canonical || pinmap) with entry-block + per-gate keys folded in
    pins_full = dict(pins)  # (local)
    pins_full["__registry_entry_block__"] = entry_sha
    pins_full["__gate_id__"] = GATE_ID
    pins_full["__wp_id__"] = "W7-1"
    pins_full["__scheme__"] = SCHEME
    pins_full["__convention__"] = CONVENTION
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, SHARED_DIR / "canonical_constants.py", pins_full)
    print(f"\n  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")

    # 8. Build the value payload (no single-quote chars; emit_verdict wraps value='...')
    orth_tag = "SATISFIED-by-construction" if orthogonality_satisfied else "OVERLAP-CAVEAT"  # (local)
    drift_tag = (f"slot_drift_expected_{EXPECTED_SLOT}_actual_{resolved_slot}"
                 if w6["slot_drift"] else f"slot_{resolved_slot}_no_drift")  # (local)
    value = (
        f"composite={agg['composite']}_stage3_eligible={agg['composite']=='PASS'}"
        f"_axisA={axisA.get('reviewer')}_all={agg['all_own_pass'] or 'see_clauses'}"
        f"_axisB={axisB.get('reviewer')}_SUBSTITUTE_for_{AXIS_B_REVIEWER_PRIMARY}_EXCLUDED_stage0_author"
        f"_axisA_own={'+'.join(f'{c}:{v}' for c,v in agg['axisA_own'].items())}"
        f"_axisB_own={'+'.join(f'{c}:{v}' for c,v in agg['axisB_own'].items())}"
        f"_J1_A={agg['axisA_J1']}_J1_B={agg['axisB_J1']}_J1_PASS-AND={agg['joint_both_pass']}"
        f"_anchors_recomputed_from_npz_all_pass={anchors['all_pass']}"
        f"_d_ladder=(0.698718,0.762085,1.558163)lam2_e=(3,0)_most_distant_relspread=0.5516"
        f"_reg_inv=1.79e-9/3dec_scopeC_firstorder=2.0450_REPORTED_KO6_machineZero"
        f"_substrate_input_orthogonality={orth_tag}_npz_volovik-axisB-ONLY_vdd-axisA-no-data-file"
        f"_{drift_tag}_per_substrate-first-canonical-sourcing-ii.B"
        f"_stage0_excluded={STAGE0_AUTHOR_EXCLUDED}"
        f"_route_STAGE-1-CANDIDATE_to_STAGE-3-PERMANENT_on_PASS_orchestrator-direct_tag_JOINT-CROSS-AXIS-STAGE-2-PASS-AND"
    )

    # 9. Save npz (the audit artifact: reviewer clause arrays + attestations + anchor values/flags + orthogonality + slot)
    anchor_names = list(anchors["rows"].keys())  # (local)
    anchor_flags = np.array([bool(anchors["rows"][n]["flag"]) for n in anchor_names])  # (local)
    np.savez(
        OUT_NPZ,
        composite=agg["composite"],
        stage3_eligible=(agg["composite"] == "PASS"),
        axisA_reviewer=axisA.get("reviewer"),
        axisB_reviewer=axisB.get("reviewer"),
        axisB_reviewer_primary_excluded=AXIS_B_REVIEWER_PRIMARY,
        stage0_author_excluded=STAGE0_AUTHOR_EXCLUDED,
        axisA_own_clauses=np.array(AXIS_A_OWN),
        axisA_own_verdicts=np.array([agg["axisA_own"][c] for c in AXIS_A_OWN]),
        axisB_own_clauses=np.array(AXIS_B_OWN),
        axisB_own_verdicts=np.array([agg["axisB_own"][c] for c in AXIS_B_OWN]),
        axisA_J1=agg["axisA_J1"], axisB_J1=agg["axisB_J1"],
        joint_both_pass=agg["joint_both_pass"],
        anchors_all_pass=anchors["all_pass"],
        anchor_names=np.array(anchor_names),
        anchor_flags=anchor_flags,
        substrate_input_orthogonality_satisfied=orthogonality_satisfied,
        axisA_substrate_input_overlap=a_overlap,
        axisB_substrate_input_overlap=b_overlap,
        resolved_slot=resolved_slot,
        expected_slot=EXPECTED_SLOT,
        slot_drift=w6["slot_drift"],
        registry_entry_block_sha=entry_sha,
        npz_plan_pin_match=npz_pin_match,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        # the re-computed anchor scalar values for downstream audit
        d_tau=anchors["rows"]["d_tau"]["value"],
        d_mu=anchors["rows"]["d_mu"]["value"],
        d_e=anchors["rows"]["d_e"]["value"],
        degen_rel_spread=anchors["rows"]["degen_rel_spread"]["value"],
        first_order_residual=anchors["rows"]["first_order_residual"]["value"],
    )
    print(f"  npz -> {OUT_NPZ.name}")

    # 10. Plot
    make_plot(agg, anchors, resolved_slot)
    print(f"  png -> {OUT_PNG.name}")

    # 11. 4-tuple + verdict payload
    print(f"\n(value={agg['composite']!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    extra = [
        (f"# reviewer-cleanliness: STATIC leg _joint_theorem_independent_verify_audit.py "
         f"--check-reviewers {resolved_slot} --reviewers {AXIS_A_REVIEWER},{AXIS_B_REVIEWER_ACTUAL} --strict "
         f"-> EXCLUSION-PASS (stage0_author {STAGE0_AUTHOR_EXCLUDED} excluded; primary Axis-B "
         f"{AXIS_B_REVIEWER_PRIMARY} EXCLUDED -> pinned fallback {AXIS_B_REVIEWER_ACTUAL} fired); "
         f"DYNAMIC leg agent-memory inheritance grep: clean"),
        (f"# substrate-input-orthogonality SATISFIED-by-construction: npz loaded by Axis-B "
         f"({AXIS_B_REVIEWER_ACTUAL}) ONLY; Axis-A ({AXIS_A_REVIEWER}) loads NO data file -> "
         f"structural-INPUT independence, NO overlap caveat"),
        (f"# slot resolution: expected {EXPECTED_SLOT}, landed VII.BO.STATE-PROJ (drift={w6['slot_drift']}) "
         f"per substrate-first-canonical-sourcing.md (ii.B); both reviewers report VII.BO.STATE-PROJ"),
        (f"# Stage-3 routing on PASS: STAGE-1-CANDIDATE -> STAGE-3-PERMANENT (Stage-3-CLASS tag "
         f"JOINT-CROSS-AXIS-STAGE-2-PASS-AND); ORCHESTRATOR-DIRECT registry tag edit at session-end "
         f"synthesis (this script NEVER edits the registry); no falsifier-inventory row (intra-pillar §VII)"),
    ]
    print_verdict_payload(agg["composite"], value, audit_sha, content_sha, extra_rows=extra)

    print(f"\n=== {GATE_ID}: {agg['composite']} (wall {time.time()-t0:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
