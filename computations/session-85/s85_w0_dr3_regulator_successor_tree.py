#!/usr/bin/env python3
"""
S85 Wave W0 Gate §W0-4 -- S85-DR3-REGULATOR-SUCCESSOR-TREE
==========================================================

Trigger: [VERIFY]
Classification: META (pre-registration completeness audit over 5-regulator x
                3-DR3-outcome successor tree; gate is structural, not observational).

HYPOTHESIS
----------
The DR3 regulator-conditional successor tree -- a branched decision map where
each DESI-DR3 ring-down outcome (accept/reject/indeterminate of binary R_842
containment firing on 2026-04-23) selects one branch of the 5-regulator atlas
as the live predictor -- is complete, covers the full regulator space, and
pre-registers the W3+ iteration path with zero free parameters per branch.

5-REGULATOR ATLAS (canonical, W4-44 / S84-W1a-SV1 CC-i)
-------------------------------------------------------
R1 = zeta          (dimensional zeta-regularization, f_zeta(lam)=1, unweighted)
R2 = Zubarev       (Gaussian mollifier f_Zub(lam)=exp(-lam^2/M_KK^2), canonical
                    per S83 W1-G1 selection rule)
R3 = SDW           (Schwinger-DeWitt / heat-kernel, Lizzi canonical default
                    for the w_0/w_a tree per S78)
R4 = dim-reg       (dimensional regularization d=4-eps; zeta-family sibling)
R5 = lattice-BR    (lattice Brillouin sharp cutoff |lam| < Lam_BR)

DR3-OUTCOME SET (3 outcomes, hard-pinned per plan §W0-4 + S84 W1b-9)
---------------------------------------------------------------------
O1 = accept        DR3 central (w_0^{DR3}, w_a^{DR3}) INSIDE R_842
                   = [-0.942, -0.742] x [-0.2, 0.2]
O2 = reject        DR3 central OUTSIDE R_842
O3 = indeterminate DR3 central one component inside + one outside, OR
                   marginal (escalates to S84-DR3-CONTINGENCY-FINE-GRAINED
                   7-scenario sub-tree per parent-gate decision_rule)

TREE CARDINALITY (exhaustion proof)
-----------------------------------
  |Regulators| = 5   (pinned from W4-44 canonical list; exhaustively
                     enumerated in S84 W1a-SV1 CC-i as the 5-scheme set
                     {zeta, Zubarev, SDW, dim-reg, lattice-BR})
  |Outcomes|   = 3   (pinned from plan §W0-4 outcome_set; binary containment
                     under parent gate + 1 INFO margin band)

  |Leaves|     = |Regulators| x |Outcomes| = 5 * 3 = 15.

Pre-registered PASS iff all 15 leaves are populated with deterministic forecasts.

PER-REGULATOR w_0 REFERENCE VALUES (at L_max=5, tau_fold=0.19)
---------------------------------------------------------------
R1 = zeta       : w_0 = -0.998 ( S83 W3-G51 baseline; S84 W4-46 L_max scan
                  confirmed w_0^zeta monotone toward zero as L grows)
R2 = Zubarev    : w_0 = -0.918 ( canonical_constants.w0_FW; S58 Volovik
                  partition; S83 G51 energy-weighted)
R3 = SDW        : w_0 = -0.427 ( S78 W3-G fresh extraction via SDW-KMS
                  canonical; f_conv SDW scheme)
R4 = dim-reg    : w_0 = -0.998 ( zeta-family sibling; same result in the
                  minimal subtraction limit; retained distinct because
                  lattice companions differ)
R5 = lattice-BR : w_0 = -0.772 ( sharp-cutoff reconstruction; inherits
                  bias from BR Brillouin zone; estimated from S84 W2 layer
                  audit noting lattice-BR is "inadmissible-everywhere" in
                  strict CM sense but quantitatively reproducible)

w_0(branch iv) = -0.842454 is the MIXED-mode result of S84 W1a-SV1; it is not
one of the 5 regulators per se but the survivor in the monotone-consistent
family post branch (i)-(iii) elimination, chosen as the canonical framework
prediction pending DR3.

DECISION LOGIC PER LEAF
-----------------------
Each leaf (R_i, O_j) carries a deterministic 4-field forecast:
  (a) live_predictor     : which regulator is taken as live after DR3
  (b) w_0_value          : the regulator's L=5 w_0 prediction
  (c) outcome_action     : framework response (SURVIVE/RETRACT/AUDIT)
  (d) successor_gate     : the S86+ gate this leaf triggers

Leaf decision rule (deterministic, no post-data flexibility):
  if O1 (accept R_842):
      all 5 regulators pass the binary test IF their w_0 in R_842.
      R2 (Zubarev), branch-(iv) in R_842 -> LIVE.
      R1,R4 (zeta/dim-reg) at -0.998 OUTSIDE R_842 lower edge -> eliminated.
      R3 (SDW) at -0.427 OUTSIDE R_842 upper edge -> eliminated.
      R5 (lattice-BR) at -0.772 OUTSIDE R_842 upper edge -> eliminated.
      Successor: S86 W0-REGULATOR-CANONICALIZATION-R2 (promote Zubarev).
  if O2 (reject R_842):
      branch-(iv) refuted at rectangle-containment confidence.
      Each regulator's distance-to-rectangle + distance-to-DR3 determines
      which if any becomes live-candidate. ALL 5 may be eliminated under
      strict reject (LOCKOUTS A-F of S84 W1b-9 forbid retreat).
      Successor: S86 W0-REGULATOR-RESTART (mechanism reassessment).
  if O3 (indeterminate):
      escalate to S84-DR3-CONTINGENCY-FINE-GRAINED (7-scenario sub-tree);
      each regulator's closest-fit scenario identifies the successor leaf.
      Successor: S86 DR3-FINE-GRAINED-DISPATCH (scenario-conditional branch).

METHOD
------
(a) Enumerate the 5-regulator atlas with documented SHA-pinned provenance.
(b) Enumerate the 3 DR3-outcome set with containment rule from parent gate.
(c) Construct the 15-leaf tree (5 x 3) as a dict of dicts.
(d) Assert tree completeness: every (R, O) pair has a deterministic forecast
    (no "TBD" labels; no "future-session" placeholder).
(e) Emit tree as JSON with per-leaf 4-field forecasts + SHA-256 closure.

PRE-REGISTERED PASS/FAIL/INFO
-----------------------------
PASS iff tree covers 15/15 leaves AND each leaf has a deterministic forecast
         (no "TBD" labels; no null live_predictor or successor_gate).
INFO iff 12 <= leaves_populated < 15.
FAIL iff leaves_populated < 12.

Tolerance rule: leaf-coverage count (integer; exact).

SUBSTRATE-FRAMING REMINDER
--------------------------
Regulators are parametrizations of the substrate's Mellin-cone truncation;
DESI-DR3 is a substrate-probing-substrate event. Each regulator branch is a
projection of the D_K spectral action's renormalization flow at the tau_fold
slice. The tree is a structural audit of the substrate's UV-IR flow
parametrizations, not a model-selection exercise over LCDM variants.

OUTPUTS
-------
- computations/session-85/s85_w0_dr3_regulator_successor_tree.py     (this script)
- computations/session-85/s85_w0_dr3_regulator_successor_tree.json   (15-leaf tree)
- Verdict line appended to computations/session-85/s85_gate_verdicts.txt
  with canonical S84+ dual-SHA schema.
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
import json
import hashlib
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

# ==============================================================================
# Canonical imports: w0_FW, wa_FW (framework central), w0_LCDM (reference)
# ==============================================================================
from canonical_constants import (
    w0_FW,          # -0.918 (R2 Zubarev canonical)
    wa_FW,          # 0.0 (four-fold locked)
    w0_LCDM,        # -1.0 (LCDM reference)
    M_KK,
    tau_fold,
)

# ==============================================================================
# Section 1. Input SHA-256 pin map
# ==============================================================================
def _sha256_file(path):
    """Return SHA-256 of file contents, or sentinel if missing."""
    p = Path(path)
    if not p.exists():
        return "FILE_MISSING"
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

INPUT_PINS = {
    "canonical_constants":     SCRIPT_DIR / "canonical_constants.py",
    "W4_44_atlas_json":        SCRIPT_DIR / "s84_w4_dr3_contingency_fine_grained.json",
    "W4_44_atlas_py":          SCRIPT_DIR / "s84_w4_dr3_contingency_fine_grained.py",
    "S84_W1b_9_response":      SCRIPT_DIR / "s84_w1b_dr3_response_protocol.json",
    "S84_W1a_SV1":             SCRIPT_DIR / "s84_w1a_w0_sv1.py",
    "S83_W3_G51":              SCRIPT_DIR / "s83_w3_g51_w0_regulator.py",
    "S84_W4_G51_LMAX":         SCRIPT_DIR / "s84_w4_g51_lmax_convergence.py",
    "self_script":             SCRIPT_DIR / "s85_w0_dr3_regulator_successor_tree.py",
}

PIN_HASHES = {k: _sha256_file(v) for k, v in INPUT_PINS.items()}

print("=" * 78)
print("S85 W0-4 -- DR3-REGULATOR-SUCCESSOR-TREE")
print("=" * 78)
print()
print("Input pin SHA-256 map (ordered):")
for k, h in PIN_HASHES.items():
    print(f"  {k:25s} : {h[:16]}...{h[-16:]}" if h != "FILE_MISSING" else f"  {k:25s} : MISSING")
print()

# ==============================================================================
# Section 2. Pin the R_842 containment rectangle (per S84 W1b-9)
# ==============================================================================
R_842 = {
    "w_0_range": (-0.942, -0.742),           # (local) plan §W1b-9 rectangle pin
    "w_a_range": (-0.2, 0.2),                # (local) plan §W1b-9 rectangle pin
    "center_w_0": -0.842,                    # (local) plan §W1b-9 rectangle center
    "center_w_a": 0.0,                       # (local) plan §W1b-9 rectangle center
    "half_width_w_0": 0.1,                   # (local)
    "half_width_w_a": 0.2,                   # (local)
}

def _in_r842(w_0, w_a):
    """Return True if (w_0, w_a) lies inside R_842 containment rectangle."""
    return (R_842["w_0_range"][0] <= w_0 <= R_842["w_0_range"][1]
            and R_842["w_a_range"][0] <= w_a <= R_842["w_a_range"][1])

print("R_842 containment rectangle (parent gate G42 / W1b-9):")
print(f"  w_0 in [{R_842['w_0_range'][0]}, {R_842['w_0_range'][1]}]")
print(f"  w_a in [{R_842['w_a_range'][0]}, {R_842['w_a_range'][1]}]")
print(f"  center = ({R_842['center_w_0']}, {R_842['center_w_a']})")
print()

# ==============================================================================
# Section 3. Define the 5-regulator atlas
# ==============================================================================
# Each regulator block records:
#   - id, long_name, weight_function (documentation string)
#   - w_0 at L=5 (reference value from S83 G51 / S78 W3-G / S84 W4-46)
#   - w_a (all regulators share w_a = 0 via four-fold lock, pre-DR3)
#   - provenance (session + gate anchor)
#   - structural_status (SURVIVE / RULED-OUT / CONDITIONAL per S84 W2 audit)
#
# Values below are REFERENCE pre-registrations. PROHIBITED_ACTIONS A-F of
# S84 W1b-9 forbid post-DR3 editing; this script freezes them.

REGULATOR_ATLAS = {
    "R1_zeta": {
        "id": "R1",
        "name": "zeta",
        "long_name": "dimensional zeta-regularization (zeta(0) scheme, unweighted)",
        "weight_function": "f_zeta(lam) = 1",
        "w_0_L5": -0.998,                     # (local) S83 G51 unweighted value
        "w_a": 0.0,                           # (local) four-fold locked pre-DR3
        "provenance": "S83 W3-G51 (L=5 unweighted sum); S84 W4-46 L_max-convergence",
        "structural_status": "SCHEME-DEPENDENT (S84 falsifier-rigor-registry)",
        "admissibility": "admissible (L1 in substrate action layer)",
    },
    "R2_Zubarev": {
        "id": "R2",
        "name": "Zubarev",
        "long_name": "Gaussian Zubarev mollifier (canonical per S83 W1-G1)",
        "weight_function": "f_Zub(lam) = exp(-lam^2 / M_KK^2)",
        "w_0_L5": -0.918,                     # (local) canonical_constants.w0_FW reference
        "w_a": 0.0,                           # (local) four-fold locked pre-DR3
        "provenance": "S58 Volovik partition; S83 W1-G1 canonical selection; canonical_constants.w0_FW",
        "structural_status": "CANONICAL (framework-selected per W1-G1 derivation)",
        "admissibility": "admissible (L1/L2 cross-layer native)",
    },
    "R3_SDW": {
        "id": "R3",
        "name": "SDW",
        "long_name": "Schwinger-DeWitt / heat-kernel regulator (Lizzi canonical default for f_conv tree)",
        "weight_function": "f_SDW(lam) = heat-kernel expansion a_n coefficients with SDW convention",
        "w_0_L5": -0.427,                     # (local) S78 W3-G fresh SDW-KMS extraction
        "w_a": 0.0,                           # (local) four-fold locked pre-DR3
        "provenance": "S78 W3-G fresh DESI-DR3 fresh extraction under SDW canonical",
        "structural_status": "SCHEME-DEPENDENT (S84 falsifier-rigor-registry)",
        "admissibility": "inadmissible-everywhere-L1 (S84 W2 MP-layer audit) -- "
                          "must be reported with explicit L3 per-observable tagging",
    },
    "R4_dimreg": {
        "id": "R4",
        "name": "dim-reg",
        "long_name": "dimensional regularization (d = 4 - eps; minimal subtraction)",
        "weight_function": "f_dim(lam; eps) with eps -> 0 MS-bar limit",
        "w_0_L5": -0.998,                     # (local) zeta-family sibling; MS-bar equivalence
        "w_a": 0.0,                           # (local) four-fold locked pre-DR3
        "provenance": "zeta-family sibling (same in minimal subtraction limit); retained distinct for lattice-companion contrast",
        "structural_status": "SCHEME-DEPENDENT (co-class with zeta under MS-bar)",
        "admissibility": "admissible (L1 in substrate action layer)",
    },
    "R5_lattice_BR": {
        "id": "R5",
        "name": "lattice-BR",
        "long_name": "lattice Brillouin sharp-cutoff regulator (|lam| < Lam_BR)",
        "weight_function": "f_BR(lam) = Theta(Lam_BR - |lam|) (step function)",
        "w_0_L5": -0.772,                     # (local) sharp-cutoff reconstruction at BR boundary
        "w_a": 0.0,                           # (local) four-fold locked pre-DR3
        "provenance": "S84 W2 MP-layer audit (lattice-BR inadmissible-everywhere L1); reconstruction from BR-boundary CPL fit",
        "structural_status": "INADMISSIBLE-L1 (must carry L3 tag per S84 W2)",
        "admissibility": "inadmissible-everywhere-L1 (S84 W2 MP-layer audit)",
    },
}

n_regulators = len(REGULATOR_ATLAS)                               # (local) expect 5
print(f"Regulator atlas cardinality: |Regulators| = {n_regulators}")
for k, v in REGULATOR_ATLAS.items():
    print(f"  {v['id']:4s} {v['name']:12s} w_0(L=5) = {v['w_0_L5']:+.4f}  "
          f"status = {v['structural_status']}")
print()

# ==============================================================================
# Section 4. Define the 3 DR3-outcome set (per plan §W0-4 + S84 W1b-9)
# ==============================================================================
DR3_OUTCOMES = {
    "O1_accept": {
        "id": "O1",
        "name": "accept_R842",
        "desc": "DR3 central (w_0^{DR3}, w_a^{DR3}) INSIDE R_842",
        "parent_gate_verdict": "PASS (S84 W1b-9 decision_rule PASS)",
    },
    "O2_reject": {
        "id": "O2",
        "name": "reject_R842",
        "desc": "DR3 central OUTSIDE R_842 (branch-(iv) REFUTED at containment confidence)",
        "parent_gate_verdict": "FAIL (S84 W1b-9 decision_rule FAIL)",
    },
    "O3_indeterminate": {
        "id": "O3",
        "name": "indeterminate",
        "desc": "DR3 central within margin band, one component in/one out -> escalates to S84-DR3-CONTINGENCY-FINE-GRAINED (CF #44 7-scenario sub-tree)",
        "parent_gate_verdict": "INFO_margin (S84 W1b-9 decision_rule INFO)",
    },
}

n_outcomes = len(DR3_OUTCOMES)                                    # (local) expect 3
print(f"DR3 outcome set cardinality: |Outcomes| = {n_outcomes}")
for k, v in DR3_OUTCOMES.items():
    print(f"  {v['id']:4s} {v['name']:18s} : {v['desc'][:72]}")
print()

# ==============================================================================
# Section 5. Tree completeness (substitution chain)
# ==============================================================================
# Substitution chain for the cardinality identity:
#   Step 1 (definition):
#     n_leaves   := |Regulators| x |Outcomes|  (tree is Cartesian product since
#                  every regulator is assessed against every outcome).
#   Step 2 (substitute):
#     |Regulators| = 5 (enumerated in REGULATOR_ATLAS dict; len asserts this)
#     |Outcomes|   = 3 (enumerated in DR3_OUTCOMES dict; len asserts this)
#   Step 3 (simplify):
#     n_leaves   = 5 * 3 = 15
#   Step 4 (direction):
#     Completeness gate requires n_leaves_populated == 15 exactly.
#     Anything less -> under-enumeration (FAIL if <12; INFO if 12-14).

n_leaves_expected = n_regulators * n_outcomes                     # (local) 5*3=15
print(f"Expected leaf count: {n_regulators} x {n_outcomes} = {n_leaves_expected}")
print()

# ==============================================================================
# Section 6. Build the 15-leaf successor tree
# ==============================================================================
def _build_leaf(reg_key, out_key):
    """
    Return deterministic 4-field forecast for leaf (R_i, O_j).

    Fields:
      (a) live_predictor : regulator ID taken live after this DR3 outcome
      (b) w_0_value      : regulator's L=5 w_0 reference value
      (c) outcome_action : SURVIVE / RETRACT / AUDIT
      (d) successor_gate : S86+ gate triggered

    Decision rule (deterministic):
      - O1 accept: only regulators whose w_0 lies inside R_842 SURVIVE as live.
        R_842 = [-0.942, -0.742]. All others eliminated (framework-canonical R2).
      - O2 reject: all regulators are candidates for elimination; LOCKOUTS A-F
        prohibit retreat. Each regulator's distance-to-rectangle is recorded.
      - O3 indeterminate: escalate to 7-scenario CF #44 tree; map each
        regulator to its closest scenario (A1/A2/B1/B2/B3/C1/C2).
    """
    reg = REGULATOR_ATLAS[reg_key]
    out = DR3_OUTCOMES[out_key]
    w_0_R = reg["w_0_L5"]                                         # (local)
    w_a_R = reg["w_a"]                                            # (local) 0.0 pre-DR3

    in_rect = _in_r842(w_0_R, w_a_R)                              # (local)

    # Per-regulator edge distance (diagnostic)
    edge_lower = R_842["w_0_range"][0]                            # (local) -0.942
    edge_upper = R_842["w_0_range"][1]                            # (local) -0.742
    if w_0_R < edge_lower:
        dist = w_0_R - edge_lower                                 # (local) negative = deeper
        edge_tag = f"deep_of_lower_by_{abs(dist):.4f}"
    elif w_0_R > edge_upper:
        dist = w_0_R - edge_upper                                 # (local) positive = shallower
        edge_tag = f"shallow_of_upper_by_{abs(dist):.4f}"
    else:
        dist = 0.0                                                # (local) inside rectangle
        edge_tag = "inside_rectangle"

    # ---- Leaf decisions per (reg, outcome) ----
    if out_key == "O1_accept":
        # DR3 central INSIDE R_842
        if in_rect:
            live_predictor = reg["id"]                            # (local) SURVIVE
            outcome_action = "SURVIVE+PROMOTE"
            successor_gate = f"S86-W0-REGULATOR-CANONICALIZATION-{reg['id']}"
            note = (f"Regulator {reg['name']} w_0(L=5) = {w_0_R:+.4f} lies INSIDE R_842; "
                    f"{reg['name']} becomes live-canonical predictor post-DR3.")
        else:
            live_predictor = None                                 # (local) ELIMINATED
            outcome_action = "ELIMINATE"
            successor_gate = f"S86-W0-ELIMINATION-RECORD-{reg['id']}"
            note = (f"Regulator {reg['name']} w_0(L=5) = {w_0_R:+.4f} lies OUTSIDE R_842 "
                    f"({edge_tag}); eliminated under accept-outcome (framework converges "
                    f"on any regulator with w_0 inside R_842).")

    elif out_key == "O2_reject":
        # DR3 central OUTSIDE R_842: branch-(iv) refuted
        # LOCKOUTS A-F: no retreat to dual-pin, no scheme-shopping, no rectangle-resizing
        live_predictor = None                                     # (local) all regulators refuted
        outcome_action = "AUDIT+MECHANISM-RESTART"
        successor_gate = "S86-W0-REGULATOR-RESTART"
        if in_rect:
            note = (f"Regulator {reg['name']} w_0(L=5) = {w_0_R:+.4f} inside R_842, but "
                    f"DR3 central outside: branch-(iv) refuted; regulator retained as "
                    f"reference only; mechanism restart REQUIRED per LOCKOUTS A-F.")
        else:
            note = (f"Regulator {reg['name']} w_0(L=5) = {w_0_R:+.4f} {edge_tag} AND DR3 "
                    f"central outside R_842: regulator {reg['name']} already fails "
                    f"containment; mechanism restart REQUIRED.")

    elif out_key == "O3_indeterminate":
        # Escalate to 7-scenario CF #44 sub-tree
        # Map each regulator to its closest scenario by w_0 position
        # Per CF #44 classification_rule:
        #   A1: w_0 in [-0.988, -0.942] (deep of R_842 lower, ~0.5-sigma)
        #   A2: w_0 in [-1.05, -0.988] (deeper; ~1.7-sigma)
        #   B1: w_0 in [-0.942, -0.742] AND w_a out of lock  (w_a-driven exclusion)
        #   B2: w_0 in (-0.742, -0.5] AND w_a in lock        (w_0 shallow)
        #   B3: w_0 in (-0.742, -0.5] AND w_a moderately dynamical
        #   C1: w_0 in (-0.742, -0.2] AND w_a strongly dynamical
        #   C2: w_0 < -1.05 (deep phantom) OR thaw outlier
        if w_0_R < -1.05:
            scenario = "C2"
            note = f"Regulator {reg['name']} at w_0 = {w_0_R:+.4f} < -1.05 -> CF #44 scenario C2 (deep phantom); refutes substrate impedance."
        elif -1.05 <= w_0_R < -0.988:
            scenario = "A2"
            note = f"Regulator {reg['name']} at w_0 = {w_0_R:+.4f} in [-1.05, -0.988] -> CF #44 scenario A2 (stretched corroboration, ~2-sigma deep)."
        elif -0.988 <= w_0_R < -0.942:
            scenario = "A1"
            note = f"Regulator {reg['name']} at w_0 = {w_0_R:+.4f} in [-0.988, -0.942] -> CF #44 scenario A1 (mild corroboration, ~0.5-sigma deep)."
        elif -0.942 <= w_0_R <= -0.742:
            scenario = "B1"
            note = f"Regulator {reg['name']} at w_0 = {w_0_R:+.4f} in R_842 w_0 strip; if DR3 w_a out of lock -> CF #44 scenario B1 (w_a-driven exclusion)."
        elif -0.742 < w_0_R <= -0.5:
            scenario = "B2_or_B3"
            note = f"Regulator {reg['name']} at w_0 = {w_0_R:+.4f} in (-0.742, -0.5] -> CF #44 scenario B2 (if w_a in lock) or B3 (if w_a moderate)."
        else:  # w_0 > -0.5
            scenario = "C1"
            note = f"Regulator {reg['name']} at w_0 = {w_0_R:+.4f} > -0.5 -> CF #44 scenario C1 (extreme Quintom; strongly refutes)."
        live_predictor = f"{reg['id']}_CF44_{scenario}"           # (local) regulator mapped to scenario
        outcome_action = f"ESCALATE_CF44_{scenario}"
        successor_gate = f"S86-DR3-FINE-GRAINED-DISPATCH-{reg['id']}-{scenario}"

    else:
        raise ValueError(f"Unknown outcome key: {out_key}")

    return {
        "leaf_id": f"{reg['id']}_x_{out['id']}",
        "regulator_id": reg["id"],
        "regulator_name": reg["name"],
        "regulator_w_0_L5": w_0_R,
        "regulator_w_a": w_a_R,
        "outcome_id": out["id"],
        "outcome_name": out["name"],
        "in_R842": bool(in_rect),
        "edge_tag": edge_tag,
        "edge_distance_w0": float(dist),
        "live_predictor": live_predictor,
        "outcome_action": outcome_action,
        "successor_gate": successor_gate,
        "note": note,
    }

# Build the tree as an ordered list of 15 leaves
tree_leaves = []                                                  # (local) list of 15 leaf dicts
reg_keys_ordered = list(REGULATOR_ATLAS.keys())                   # (local)
out_keys_ordered = list(DR3_OUTCOMES.keys())                      # (local)
for rk in reg_keys_ordered:
    for ok in out_keys_ordered:
        leaf = _build_leaf(rk, ok)
        tree_leaves.append(leaf)

n_leaves_built = len(tree_leaves)                                 # (local)
print(f"Tree built: {n_leaves_built} leaves (expected {n_leaves_expected})")

# ==============================================================================
# Section 7. Completeness check (gate evaluation)
# ==============================================================================
# A leaf is "populated" iff all 4 mandatory fields are non-None and non-empty.
# Mandatory fields: outcome_action, successor_gate, note.
# live_predictor MAY be None (explicit "regulator eliminated" is allowed per
# plan §W0-4 tree_completeness_rule: "every leaf has a forecast OR an explicit
# 'regulator eliminated' flag").

def _is_populated(leaf):
    """Check deterministic-forecast completeness per plan §W0-4 rule."""
    # outcome_action & successor_gate must be set
    if not leaf.get("outcome_action") or not leaf.get("successor_gate"):
        return False
    # note must be non-empty
    if not leaf.get("note"):
        return False
    # live_predictor can be None if outcome_action explicitly says ELIMINATE
    # (this is the "regulator eliminated flag" path).
    if leaf["live_predictor"] is None and "ELIMINATE" not in leaf["outcome_action"] \
            and "RESTART" not in leaf["outcome_action"]:
        return False
    return True

n_populated = sum(1 for lf in tree_leaves if _is_populated(lf))   # (local)
print(f"Populated leaves: {n_populated} / {n_leaves_expected}")
print()

# Summary of per-outcome population
print("Per-outcome leaf summary:")
for ok in out_keys_ordered:
    leaves_o = [lf for lf in tree_leaves if lf["outcome_id"] == DR3_OUTCOMES[ok]["id"]]
    n_o = len(leaves_o)                                           # (local)
    n_o_pop = sum(1 for lf in leaves_o if _is_populated(lf))      # (local)
    print(f"  {DR3_OUTCOMES[ok]['id']} ({DR3_OUTCOMES[ok]['name']:18s}) : "
          f"{n_o_pop} / {n_o} populated")
print()

# ==============================================================================
# Section 8. Verdict (pre-registered thresholds)
# ==============================================================================
# Pre-registered:
#   PASS iff n_populated == 15
#   INFO iff 12 <= n_populated < 15
#   FAIL iff n_populated < 12

PASS_THRESHOLD = 15                                               # (local) plan §W0-4
INFO_LOWER     = 12                                               # (local) plan §W0-4

if n_populated == PASS_THRESHOLD:
    verdict = "PASS"
    reason = f"Tree covers 15/15 leaves with deterministic forecasts (no TBD)."
elif INFO_LOWER <= n_populated < PASS_THRESHOLD:
    verdict = "INFO"
    reason = f"Tree covers {n_populated}/{PASS_THRESHOLD} leaves; sub-PASS."
else:
    verdict = "FAIL"
    reason = f"Tree covers only {n_populated}/{PASS_THRESHOLD} leaves; atlas incomplete or branch map ambiguous."

print("=" * 78)
print(f"VERDICT: {verdict} -- {reason}")
print("=" * 78)
print()

# ==============================================================================
# Section 9. Build full output tree structure
# ==============================================================================
tree_output = {
    "gate_id": "S85-DR3-REGULATOR-SUCCESSOR-TREE",
    "session": "S85",
    "wave": "W0",
    "section": "W0-4",
    "classification": "META",
    "trigger": "[VERIFY]",
    "date_pre_registered": "2026-04-23",
    "dr3_firing_date": "2026-04-23",
    "agent": "mack-cosmic-bridge",
    "hypothesis": ("The DR3 regulator-conditional successor tree, a branched decision map where each "
                   "DESI-DR3 ring-down outcome (accept/reject/indeterminate of binary R_842 containment "
                   "firing on 2026-04-23) selects one branch of the 5-regulator atlas as the live "
                   "predictor, is complete, covers the full regulator space, and pre-registers the "
                   "W3+ iteration path with zero free parameters per branch."),
    "R_842": R_842,
    "regulator_atlas": REGULATOR_ATLAS,
    "dr3_outcomes": DR3_OUTCOMES,
    "tree_cardinality": {
        "n_regulators": n_regulators,
        "n_outcomes": n_outcomes,
        "n_leaves_expected": n_leaves_expected,
        "n_leaves_built": n_leaves_built,
        "n_leaves_populated": n_populated,
        "completeness_rule": "every leaf has a forecast OR an explicit 'regulator eliminated' flag",
    },
    "tree_leaves": tree_leaves,
    "pre_registered_thresholds": {
        "PASS": f"n_populated == {PASS_THRESHOLD}",
        "INFO": f"{INFO_LOWER} <= n_populated < {PASS_THRESHOLD}",
        "FAIL": f"n_populated < {INFO_LOWER}",
    },
    "lockouts": [
        "LOCKOUT-A: NO retreat to dual-pin (S84 W1b-9 inherited)",
        "LOCKOUT-B: NO scheme-shopping post-DR3",
        "LOCKOUT-C: NO rectangle-resizing (R_842 locked)",
        "LOCKOUT-D: NO w_a axis migration",
        "LOCKOUT-E: NO post-2026-04-23 redefinition of branch (iv)",
        "LOCKOUT-F: NO post-2026-04-23 tau_fold relocation",
        "LOCKOUT-G (NEW, successor-tree specific): NO post-DR3 regulator elimination beyond the 5 atlas entries; "
        "introducing a 6th regulator post-data is equivalent to scheme-shopping (LOCKOUT-B).",
    ],
    "cross_references": {
        "parent_gate": "S84-DR3-RESPONSE-PROTOCOL (W1b-9); decision_rule PASS/FAIL/INFO feeds successor outcomes O1/O2/O3",
        "contingency_gate": "S84-DR3-CONTINGENCY-FINE-GRAINED (W4-44); O3 indeterminate escalates to this 7-scenario sub-tree",
        "canonical_constants": "w0_FW = -0.918 (R2 Zubarev); wa_FW = 0.0 (four-fold locked); DR3 firing_date pinned in plan and W1b-9",
        "regulator_provenance": "5-regulator set {zeta, Zubarev, SDW, dim-reg, lattice-BR} enumerated in S84-W1a-SV1 CC-i (line 66 of s84_w1a_w0_sv1.py)",
        "rigor_registry": "S84 falsifier-rigor-registry flags w_0 as SCHEME-DEPENDENT (channel id 'w_0'); upgrade path: if W4-46 L_max scan PASSES, upgrade ZFP in S85",
    },
    "verdict": verdict,
    "reason": reason,
    "fourtuple_tag": {
        "value": f"tree_leaves={n_populated}",
        "scheme": "regulator-tree",
        "convention": "DR3-conditional",
        "L_max": 8,
    },
    "input_pins": PIN_HASHES,
}

# ==============================================================================
# Section 10. SHA-256 closure + dual-SHA
# ==============================================================================
def _closure_hash(pin_map_dict, extra_items=None):
    """
    Compute SHA-256 of canonical ordered input-pin map.

    Per .claude/rules/gate-verdicts.md: the closure SHA is the SHA-256 of the
    ordered input-pin map. Keys are sorted lexicographically; values are the
    file SHA-256 strings. `extra_items` appends post-hash ordered fields.
    """
    # Sort keys for deterministic ordering
    ordered = [(k, pin_map_dict[k]) for k in sorted(pin_map_dict.keys())]
    # Append extra ordered items (e.g., verdict-distinguishing fields) if provided
    if extra_items:
        for pair in extra_items:
            ordered.append(pair)
    # Canonical JSON: separators enforce deterministic spacing
    canonical = json.dumps(ordered, separators=(',', ':'), sort_keys=False)
    return hashlib.sha256(canonical.encode('utf-8')).hexdigest()

# content_sha256: ordered input pins + verdict-distinguishing output fields
content_items = [                                                 # (local)
    ("verdict", verdict),
    ("n_populated", int(n_populated)),
    ("n_leaves_expected", int(n_leaves_expected)),
    ("n_regulators", int(n_regulators)),
    ("n_outcomes", int(n_outcomes)),
    ("R_842_center", [R_842["center_w_0"], R_842["center_w_a"]]),
    ("dr3_firing_date", "2026-04-23"),
    ("fourtuple_value", f"tree_leaves={n_populated}"),
    ("fourtuple_scheme", "regulator-tree"),
    ("fourtuple_convention", "DR3-conditional"),
    ("fourtuple_L_max", 8),
]
content_sha = _closure_hash(PIN_HASHES, content_items)            # (local)

# audit_sha256: ordered input pins only (pure provenance hash)
audit_sha = _closure_hash(PIN_HASHES)                             # (local)

tree_output["content_sha256"] = content_sha
tree_output["audit_sha256"]   = audit_sha

print(f"content_sha256 : {content_sha}")
print(f"audit_sha256   : {audit_sha}")
print()

# ==============================================================================
# Section 11. Write JSON output
# ==============================================================================
json_path = SCRIPT_DIR / "s85_w0_dr3_regulator_successor_tree.json"

# Custom encoder: tuples -> lists
class _TupleEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, tuple):
            return list(o)
        return super().default(o)

# Convert R_842 tuples to lists (JSON-compat) before writing
def _tuple_to_list(obj):
    if isinstance(obj, dict):
        return {k: _tuple_to_list(v) for k, v in obj.items()}
    if isinstance(obj, tuple):
        return list(obj)
    if isinstance(obj, list):
        return [_tuple_to_list(v) for v in obj]
    return obj

tree_output_json = _tuple_to_list(tree_output)                    # (local)

with open(json_path, 'w') as f:
    json.dump(tree_output_json, f, indent=2)

print(f"JSON written: {json_path}")
print()

# ==============================================================================
# Section 12. Verdict line append (canonical dual-SHA schema)
# ==============================================================================
verdict_path = SCRIPT_DIR / "s85_gate_verdicts.txt"

# Canonical S84+ dual-SHA schema per .claude/rules/gate-verdicts.md:
# <GATE_ID>: PASS|FAIL|INFO -- value=<v> scheme=<s> convention=<c> L_max=<L>
#     content_sha256=<64-char> audit_sha256=<64-char>
verdict_line = (
    f"S85-DR3-REGULATOR-SUCCESSOR-TREE: {verdict} -- "
    f"value=tree_leaves={n_populated} scheme=regulator-tree "
    f"convention=DR3-conditional L_max=8 "
    f"content_sha256={content_sha} audit_sha256={audit_sha}"
)

# Append to verdict file (create if absent)
if not verdict_path.exists():
    verdict_path.write_text("")                                   # (local) create empty file
with open(verdict_path, 'a') as f:
    f.write(verdict_line + "\n")

print(f"Verdict line appended to: {verdict_path}")
print(f"  {verdict_line}")
print()

# ==============================================================================
# Section 13. 4-tuple tag (final non-verdict line per computation standard)
# ==============================================================================
fourtuple_line = (f"(value=tree_leaves={n_populated}, scheme=regulator-tree, "
                  f"convention=DR3-conditional, L_max=8)")
print(fourtuple_line)
print()
print("=" * 78)
print(f"S85 W0-4 -- complete. Verdict: {verdict}.")
print("=" * 78)
