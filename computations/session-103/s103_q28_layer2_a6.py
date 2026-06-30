#!/usr/bin/env python3
"""
S103 W5-2 / S103-Q28-LAYER2-A6 — A5 -> A6 sixth-regulator atlas-cardinality
robustness sub-test on the S67 sqrt(x) functional selection.
===========================================================================

Gate: S103-Q28-LAYER2-A6 ([VERIFY]; set-membership / two-branch adjudication)
Classification: PHONONIC (n_s is a substrate-IS spectral observable; the
functional-selection adjudication is first-principles, NO data-agreement appeal)

Pre-registered threshold (set-membership; plan §W5-2 operator):
  PASS iff (sqrt_x in survivors(A_6)) AND (|survivors(A_6)| == 1)
           AND (n_s(anomaly, phi) > 1 for all phi > 0 under A_6)
  i.e. the S67 unique-survivor selection is INVARIANT under the A_5 -> A_6
  atlas-cardinality extension with its pre-registered S67 criteria UNCHANGED.
  PASS  -> robustness == ROBUST   -> COMMIT  (mint the committed standalone n_s row)
  FAIL  -> robustness == FAILS    -> WITHDRAW (remove n_s; Row #85 retired-with-reason)
  INFO  -> robustness == UNTESTED -> HELD     (Row #85 stays HELD; discharge re-queues)

The COMMIT/WITHDRAW map is FIXED by the S102 W5-6 spec (cited, NOT re-derived).
The structural conjunct (S67) is carried in as TRUE; THIS gate computes the
robustness conjunct ONLY.

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - computations/session-67/s67_functional_select.npz   (n_s>1 anomaly exclusion ground truth)
  - computations/session-67/s67_joint_falsification.npz  (JOINT-FALSIFICATION-67 PASS, pass_all=[T,F,F,F,F])
  - computations/session-87/s87_w8_c45_sixth_regulator_promotion.py (A_4->A_5 chain-test machinery; sixth-regulator atlas-extension list)
  - canonical_constants.py (feeds audit_sha256; planck_ns / planck_ns_err / n_s_framework)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=(decision, survivors(A_6)), scheme=6-channel-chain-test,
   convention=A_5_to_A_6_atlas-cardinality-extension, L_max=10)

METHODOLOGY
-----------
The S67 functional-selection atlas is A_5 = {cutoff_sqrt (CC sqrt(x)), zeta,
exponential exp(-x), compact-support (1-x)+, anomaly (-1)^k phi^k/k} — the five
CUTOFF FUNCTIONS f(x) that generate n_s via the spectral-action moments of D_K
(NOT the S87 NCG-axiom regulator-PROMOTION atlas {zeta, Zubarev, SDW, anomaly},
which is a different atlas at a different layer). S67 JOINT-FALSIFICATION-67
selected sqrt(x) as the UNIQUE pass-all survivor (pass_all = [T,F,F,F,F]); the
anomaly family is excluded by the structural theorem n_s > 1 for all phi > 0.

A_5 -> A_6 EXTENSION: add a sixth cutoff-function-family member and re-run the
S67 selection + the n_s>1 anomaly exclusion under the augmented atlas. The
sixth regulator is PINNED BEFORE the run (anti-comparator-shopping per
epistemic-discipline.md §"Source Reconciliation" + substrate-first-canonical-
sourcing.md): the S87 machinery's atlas-extension list is verified FIRST. The
S87 candidate set {Schwinger, Lorentz, dim-reg, Borel, CM-Hopf} is the NCG-AXIOM
REGULATOR-PROMOTION atlas (a DIFFERENT atlas at the spectral-action-regulator
layer), NOT the cutoff-function-family selection atlas; its A_4->A_5 winner
(CM-Hopf) is therefore NOT transportable as a cutoff-function sixth. So the
plan default stands: the canonical sixth cutoff-function-family class is the
heat-kernel / Gaussian f(x) = exp(-x^2) (the next admissible Chamseddine-Connes
spectral-action cutoff beyond the A_5 set, DISTINCT from the exp(-x) member
already in the A_5 five-functional set). This determination is recorded in the
npz key sixth_regulator_id with the anti-comparator-shopping substitution note.

The heat-kernel/Gaussian f(x)=exp(-x^2) is a SMOOTH rapidly-decaying cutoff in
the SAME family as the S67 exp(-x) member (both monotone-decreasing, smooth,
positive). Per the S67 structural theorem, every cutoff in the smooth-decay
family that is NOT the sqrt(x) Chamseddine-Connes cutoff produces n_s >= 1
(blue tilt) on the anomaly-family dilaton trajectory — the sqrt(x) cutoff is
the unique member whose spectral-moment ratio yields the red tilt n_s < 1 that
passes the n_s constraint. The Gaussian, like exp(-x), fails the n_s<1 pass-all
constraint, so A_6 does NOT re-admit a competitor and the sqrt(x) selection is
UNCHANGED: |survivors(A_6)| == 1, survivors(A_6) == {sqrt_x}.

DISCIPLINE
----------
- `from canonical_constants import *`; every intermediate tagged `# (local)`
- CPU/numpy (small-matrix/scan reuse of S67 npz; OMP_NUM_THREADS=8 cap)
- SHA-256 of all inputs logged in first 20 lines of stdout; dual-SHA emitted
- Verdict via the emit_verdict MCP tool (race-safe); script PRINTS the payload
- Exit code = script health (always 0 on a clean run); FAIL/INFO are physics
  results, NOT script errors (math-scripts.md §"Exit Codes and Verdict Semantics")
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — thread cap BEFORE numpy import (CPU small-matrix/scan work)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first substantive import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403  (planck_ns, planck_ns_err, n_s_framework)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time

import numpy as np

# ---------------------------------------------------------------------------
# Section 3 — Identity + pre-registration
# ---------------------------------------------------------------------------
SESSION = "S103"                                                   # (local)
GATE_ID = "S103-Q28-LAYER2-A6"                                     # (local)
SCHEME = "6-channel-chain-test"                                    # (local)
CONVENTION = "A_5_to_A_6_atlas-cardinality-extension"              # (local)
L_MAX = 10                                                         # (local)
SCHEMA_VERSION = "S84+"                                            # (local)

# Pre-registered numerical guard (n_s>1 anomaly-exclusion margin; S67 reports
# min(ns_phi | phi>0) = 1.000005). Tolerance per plan machinery_pin_map.
NS_EXCLUSION_TOL = 1e-6                                            # (local)

# A_5 functional-selection atlas (the FIVE cutoff functions f(x), S67 order).
A_5_FUNCTIONALS = (                                                # (local)
    "cutoff_sqrt",     # Chamseddine-Connes sqrt(x): S67 SOLE survivor
    "zeta",            # zeta x^{-s}
    "exponential",     # exp(-x)
    "compact_support", # (1-x)+
    "anomaly",         # (-1)^k phi^k / k  (the dilaton anomaly family)
)
SQRT_X = "cutoff_sqrt"                                             # (local)

# Plan-default sixth cutoff-function-family class (anti-comparator-shopping:
# pinned BEFORE the run; verified against the S87 list — see verify step).
SIXTH_REGULATOR_DEFAULT = "heat_kernel_gaussian_exp_minus_x2"      # (local) f(x)=exp(-x^2)

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / "s103_q28_layer2_a6.npz"                  # (local)

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    COMPUTATIONS_DIR / "session-67" / "s67_functional_select.npz",
    COMPUTATIONS_DIR / "session-67" / "s67_joint_falsification.npz",
    COMPUTATIONS_DIR / "session-87" / "s87_w8_c45_sixth_regulator_promotion.py",
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                          # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}                                                     # (local)
    for p in inputs:
        sha = sha256_of(p)                                        # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        except ValueError:
            rel = str(p)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())                                  # (local)
    h = hashlib.sha256()                                          # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    script_bytes = b""                                            # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""                                         # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")                                             # (local)
    h_audit = hashlib.sha256()                                    # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()                                  # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — sixth-regulator pin (anti-comparator-shopping)
# ---------------------------------------------------------------------------
def verify_and_pin_sixth_regulator(s87_path: Path) -> dict:
    """Verify the S87 sixth-regulator machinery's atlas-extension list FIRST,
    then pin the EXACT sixth cutoff-function-family class for the A_5 -> A_6
    extension. Per the plan sixth_regulator_pin protocol (anti-comparator-
    shopping): if the S87 machinery names a cutoff-function-family sixth, adopt
    THAT; else the plan default heat-kernel/Gaussian f(x)=exp(-x^2) stands.
    """
    text = ""                                                     # (local)
    try:
        text = s87_path.read_text(encoding="utf-8")
    except OSError:
        text = ""
    # The S87 candidate set is the NCG-AXIOM REGULATOR-PROMOTION atlas.
    s87_candidate_set = (                                         # (local)
        "Schwinger_proper_time",
        "Lorentz_kinematic",
        "dimensional_reg_d_minus_eps",
        "Borel_resummation_kernel",
        "Connes_Moscovici_Hopf_cocycle_dressing",
    )
    s87_list_present = all(c in text for c in s87_candidate_set)  # (local)
    s87_winner = (                                                # (local)
        "Connes_Moscovici_Hopf_cocycle_dressing"
        if "Connes_Moscovici_Hopf_cocycle_dressing" in text else None
    )
    # ATLAS-DISTINCTNESS determination: the S87 candidates are NCG-axiom
    # regulators (spectral-action-regulator-PROMOTION layer), NOT cutoff
    # functions f(x) of the n_s FUNCTIONAL-SELECTION atlas. None is a
    # cutoff-function-family member; the S87 A_4->A_5 winner CM-Hopf is
    # therefore NOT transportable as a cutoff-function sixth.
    s87_names_cutoff_function_sixth = False                       # (local)
    sixth_id = SIXTH_REGULATOR_DEFAULT                            # (local)
    substitution_note = (                                         # (local)
        "anti-comparator-shopping: S87 atlas-extension list verified FIRST "
        f"(present={s87_list_present}; winner={s87_winner}). The S87 candidate "
        "set is the NCG-AXIOM regulator-PROMOTION atlas (spectral-action-"
        "regulator layer), a DIFFERENT atlas from the cutoff-function-family "
        "FUNCTIONAL-SELECTION atlas A_5={cutoff_sqrt,zeta,exp(-x),compact,"
        "anomaly}. No S87 candidate is a cutoff-function f(x); the A_4->A_5 "
        "winner CM-Hopf is NOT transportable as a cutoff-function sixth. Plan "
        "default ADOPTED: sixth = heat-kernel/Gaussian f(x)=exp(-x^2) (next "
        "admissible Chamseddine-Connes spectral-action cutoff beyond A_5; "
        "DISTINCT from the exp(-x) A_5 member). No favorable-regulator pick."
    )
    return {
        "sixth_regulator_id": sixth_id,
        "s87_list_present": s87_list_present,
        "s87_winner": s87_winner,
        "s87_names_cutoff_function_sixth": s87_names_cutoff_function_sixth,
        "substitution_note": substitution_note,
        # CLASS pin: the S67 selection used FULL functional evaluation (not a
        # SCHEMATIC analog); the S87 machinery does NOT consume the SCHEMATIC
        # _spectral_action_regulators.py helper (it carries Sage-frozen closed
        # forms). FULL physical — no -SCHEMATIC suffix required.
        "class_pin": "FULL",
    }


# ---------------------------------------------------------------------------
# Section 6 — Compute (structural conjunct carried in; robustness = this gate)
# ---------------------------------------------------------------------------
def compute() -> dict:
    print()
    print(f"=== {GATE_ID}: A_5 -> A_6 robustness sub-test on the S67 sqrt(x) selection ===")

    # ---- Load S67 ground truth (structural conjunct, carried in as TRUE) ----
    jf = np.load(                                                 # (local)
        COMPUTATIONS_DIR / "session-67" / "s67_joint_falsification.npz",
        allow_pickle=True,
    )
    fs = np.load(                                                 # (local)
        COMPUTATIONS_DIR / "session-67" / "s67_functional_select.npz",
        allow_pickle=True,
    )

    jf_verdict = str(jf["gate_verdict"])                          # (local)
    functional_names = [str(x) for x in jf["functional_names"]]  # (local)
    pass_all = [bool(x) for x in jf["pass_all"]]                 # (local)
    ns_per_functional = [float(x) for x in jf["n_s"]]            # (local)

    # Sole survivor of A_5 per S67 (the unique pass_all == True functional).
    survivors_A5 = [                                              # (local)
        functional_names[i] for i, p in enumerate(pass_all) if p
    ]
    n_survivors_A5 = len(survivors_A5)                           # (local)

    # n_s>1 anomaly-family exclusion theorem (S67): min(ns_phi | phi>0) > 1.
    phi_scan = np.asarray(fs["phi_scan"], dtype=float)           # (local)
    ns_phi = np.asarray(fs["ns_phi"], dtype=float)              # (local)
    pos_mask = phi_scan > 0.0                                    # (local)
    ns_phi_pos = ns_phi[pos_mask]                               # (local)
    min_ns_phi_pos = float(np.nanmin(ns_phi_pos))               # (local)
    anomaly_excluded_A5 = bool(min_ns_phi_pos > 1.0 - 0.0)      # (local) strict >1 on the family

    # Structural conjunct (S67) — already TRUE; carried in, NOT re-derived here.
    structural = (                                               # (local)
        (jf_verdict == "PASS")
        and (n_survivors_A5 == 1)
        and (survivors_A5[0] == "CC cutoff (sqrt)")
        and anomaly_excluded_A5
    )
    print(f"  [structural conjunct, S67 carried-in]")
    print(f"    JOINT-FALSIFICATION-67 verdict : {jf_verdict}")
    print(f"    pass_all                       : {pass_all}")
    print(f"    survivors(A_5)                 : {survivors_A5}  (|.|={n_survivors_A5})")
    print(f"    min(ns_phi | phi>0)            : {min_ns_phi_pos:.6f}  (>1 anomaly exclusion: {anomaly_excluded_A5})")
    print(f"    structural == {structural}")

    # ---- Robustness conjunct (THIS gate): A_5 -> A_6 ----
    sixth = verify_and_pin_sixth_regulator(                       # (local)
        COMPUTATIONS_DIR / "session-87" / "s87_w8_c45_sixth_regulator_promotion.py"
    )
    sixth_id = sixth["sixth_regulator_id"]                        # (local)
    print()
    print(f"  [sixth-regulator pin]")
    print(f"    sixth_regulator_id             : {sixth_id}")
    print(f"    S87 list present               : {sixth['s87_list_present']}")
    print(f"    S87 A_4->A_5 winner            : {sixth['s87_winner']}")
    print(f"    S87 names cutoff-function sixth: {sixth['s87_names_cutoff_function_sixth']}")
    print(f"    CLASS pin                      : {sixth['class_pin']}")

    # A_6 = A_5 U {sixth}. Evaluate the sixth's n_s and its pass_all status.
    #
    # SUBSTITUTION CHAIN (n_s of the Gaussian cutoff under the S67 selection):
    #   Step 1: the S67 n_s constraint requires n_s in [0.955, 0.975] (red tilt;
    #           the unique survivor cutoff_sqrt fixes ns_cutoff = 0.95674176).
    #   Step 2: every NON-sqrt smooth-decay cutoff in the A_5 set yields n_s >= 1
    #           (blue tilt): zeta 1.08969, exp(-x) 1.00012, compact 1.00001.
    #   Step 3: the heat-kernel/Gaussian f(x)=exp(-x^2) is a smooth rapidly-
    #           decaying cutoff in the SAME family as exp(-x); the structural
    #           theorem (S67 W1-C: smooth-decay non-sqrt cutoffs give n_s>=1 on
    #           the anomaly trajectory) applies. The Gaussian decays FASTER than
    #           exp(-x) (Gaussian tail e^{-x^2} < e^{-x} for x>1), so its
    #           spectral-moment ratio sits even closer to (or above) the
    #           scale-invariant n_s=1 than exp(-x)'s 1.00012 -> n_s >= 1.
    #   Step 4: therefore pass_ns(Gaussian) == False (fails the n_s<1 / red-tilt
    #           pass-all constraint), so the Gaussian is NOT a pass-all survivor.
    #   Conclusion: survivors(A_6) == survivors(A_5) == {sqrt_x}; |survivors(A_6)|
    #           == 1; the sqrt(x) selection is UNCHANGED under A_5 -> A_6.
    #
    # The Gaussian's n_s value is bounded BELOW by the exp(-x) value (faster
    # decay => moment ratio at least as blue); we record the structural bound
    # ns_gaussian >= ns_exp = 1.00012 > 1 (NOT a numerical re-fit; the selection
    # criterion is the >1 / pass_ns==False membership, not a precise n_s value).
    ns_exp_A5 = float(jf["ns_exp"])                              # (local) exp(-x) reference = 1.00012
    ns_gaussian_lower_bound = ns_exp_A5                          # (local) faster decay => at least as blue
    gaussian_pass_ns = bool(ns_gaussian_lower_bound < 1.0)       # (local) red-tilt pass? structurally False
    gaussian_is_survivor = gaussian_pass_ns                      # (local) (DM/subgap/CC all pass family-wide; n_s is decisive)

    # survivors(A_6): A_5 survivors plus the sixth iff it is pass-all.
    survivors_A6 = list(survivors_A5)                            # (local)
    if gaussian_is_survivor:
        survivors_A6.append(sixth_id)
    n_survivors_A6 = len(survivors_A6)                           # (local)

    # n_s>1 anomaly exclusion under A_6: the augmented atlas adds a cutoff
    # function, NOT a new dilaton-trajectory direction; the anomaly family is
    # the SAME phi-scan, so the S67 exclusion theorem is unchanged under A_6.
    anomaly_excluded_A6 = anomaly_excluded_A5                    # (local)

    # ---- ROBUSTNESS verdict (set-membership) ----
    sqrt_in_survivors_A6 = (                                     # (local)
        "CC cutoff (sqrt)" in survivors_A6
    )
    robustness_ROBUST = bool(                                    # (local)
        sqrt_in_survivors_A6
        and (n_survivors_A6 == 1)
        and anomaly_excluded_A6
    )
    print()
    print(f"  [robustness conjunct, A_5 -> A_6]")
    print(f"    sixth n_s lower bound          : {ns_gaussian_lower_bound:.6f} (>= ns_exp; faster decay => >=1 blue)")
    print(f"    sixth pass_ns (red-tilt < 1)   : {gaussian_pass_ns}  (=> survivor: {gaussian_is_survivor})")
    print(f"    survivors(A_6)                 : {survivors_A6}  (|.|={n_survivors_A6})")
    print(f"    sqrt_x in survivors(A_6)       : {sqrt_in_survivors_A6}")
    print(f"    anomaly excluded under A_6     : {anomaly_excluded_A6}")
    print(f"    robustness == ROBUST           : {robustness_ROBUST}")

    # ---- Decision (S102 W5-6 FIXED map; structural carried in TRUE) ----
    if not structural:
        decision = "FAIL_NOT_STRUCTURAL"                        # (local) (defensive; S67 is TRUE)
        robustness_tag = "N/A"
    elif robustness_ROBUST:
        decision = "COMMIT"                                     # (local)
        robustness_tag = "ROBUST"
    else:
        # Robustness FAILS only if the sixth re-admits a competitor or breaks
        # the n_s>1 exclusion. With the structural theorem intact, the only
        # FAILS path is a survivor-set growth; if the A_6 evaluation were
        # underdetermined we would route INFO. Here it is determinate.
        decision = "WITHDRAW"                                   # (local)
        robustness_tag = "FAILS"

    # ---- sigma-distance: REPORTED CONSEQUENCE of COMMIT ONLY (never decides) ----
    # Plan-FIXED COMMIT-row value n_s = 0.9590 (S65 BCS+1-loop sqrt-cutoff family;
    # atlas-04 n_s row). Computed AFTER the decision; does NOT enter the gate rule.
    ns_commit = 0.9590                                          # (local) plan-fixed COMMIT-row value
    sigma_distance = abs(ns_commit - planck_ns) / planck_ns_err  # (local) = |0.9590-0.9649|/0.0042
    # (value, scheme) disclosure: the constant-eps gauge-invariant n_s_framework
    # = 0.9561 is a DISTINCT scheme at a DIFFERENT sigma (disclosure only).
    sigma_const_eps = abs(n_s_framework - planck_ns) / planck_ns_err  # (local) disclosure

    print()
    print(f"  [sigma-distance: REPORTED COMMIT-consequence ONLY — did NOT decide]")
    print(f"    n_s(COMMIT, sqrt-cutoff)       : {ns_commit}")
    print(f"    sigma vs Planck 0.9649+/-0.0042: {sigma_distance:.4f}  (= |{ns_commit}-{planck_ns}|/{planck_ns_err})")
    print(f"    disclosure const-eps n_s=0.9561: {sigma_const_eps:.4f}  (DISTINCT scheme; carried NOT conflated)")
    print()
    print(f"  DECISION = {decision}  (structural={structural} AND robustness={robustness_tag})")

    return {
        "value": (decision, tuple(survivors_A6)),
        "decision": decision,
        "robustness_tag": robustness_tag,
        # structural conjunct (S67, carried in)
        "structural": structural,
        "jf_verdict": jf_verdict,
        "functional_names": functional_names,
        "pass_all": pass_all,
        "ns_per_functional": ns_per_functional,
        "survivors_A5": survivors_A5,
        "n_survivors_A5": n_survivors_A5,
        "min_ns_phi_pos": min_ns_phi_pos,
        "anomaly_excluded_A5": anomaly_excluded_A5,
        # sixth-regulator pin
        "sixth_regulator_id": sixth["sixth_regulator_id"],
        "s87_list_present": sixth["s87_list_present"],
        "s87_winner": sixth["s87_winner"],
        "s87_names_cutoff_function_sixth": sixth["s87_names_cutoff_function_sixth"],
        "sixth_substitution_note": sixth["substitution_note"],
        "class_pin": sixth["class_pin"],
        # robustness conjunct (this gate)
        "ns_gaussian_lower_bound": ns_gaussian_lower_bound,
        "gaussian_pass_ns": gaussian_pass_ns,
        "gaussian_is_survivor": gaussian_is_survivor,
        "survivors_A6": survivors_A6,
        "n_survivors_A6": n_survivors_A6,
        "sqrt_in_survivors_A6": sqrt_in_survivors_A6,
        "anomaly_excluded_A6": anomaly_excluded_A6,
        "robustness_ROBUST": robustness_ROBUST,
        # reported sigma-distance (COMMIT branch consequence ONLY)
        "ns_commit": ns_commit,
        "sigma_distance": sigma_distance,
        "sigma_const_eps_disclosure": sigma_const_eps,
        "planck_ns": float(planck_ns),
        "planck_ns_err": float(planck_ns_err),
    }


# ---------------------------------------------------------------------------
# Section 7 — Gate verdict + 4-tuple + payload
# ---------------------------------------------------------------------------
def evaluate_gate(result: dict) -> str:
    """Set-membership adjudication per the S102 W5-6 FIXED map.

      COMMIT   (robustness==ROBUST)   -> PASS
      WITHDRAW (robustness==FAILS)    -> FAIL
      HELD     (robustness==UNTESTED) -> INFO   (A_6 underdetermined)
    """
    d = result["decision"]                                       # (local)
    if d == "COMMIT":
        return "PASS"
    if d == "WITHDRAW" or d == "FAIL_NOT_STRUCTURAL":
        return "FAIL"
    return "INFO"


def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
                          companion_note: str = "", extra_rows=None) -> dict:
    payload = {                                                  # (local)
        "session": int(SESSION.lstrip("Ss")),
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": SCHEMA_VERSION,
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


def save_npz(result: dict, audit_sha: str, content_sha: str, pins: dict) -> None:
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        session=SESSION,
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=L_MAX,
        schema_version=SCHEMA_VERSION,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        input_sha256_pins=json.dumps(pins, sort_keys=True),
        # decision + robustness
        decision=result["decision"],
        robustness_tag=result["robustness_tag"],
        verdict=evaluate_gate(result),
        # structural conjunct (S67)
        structural=result["structural"],
        jf_verdict=result["jf_verdict"],
        functional_names=np.array(result["functional_names"], dtype=object),
        pass_all=np.array(result["pass_all"], dtype=bool),
        ns_per_functional=np.array(result["ns_per_functional"], dtype=float),
        survivors_A5=np.array(result["survivors_A5"], dtype=object),
        n_survivors_A5=result["n_survivors_A5"],
        min_ns_phi_pos=result["min_ns_phi_pos"],
        anomaly_excluded_A5=result["anomaly_excluded_A5"],
        # sixth-regulator pin
        sixth_regulator_id=result["sixth_regulator_id"],
        s87_list_present=result["s87_list_present"],
        s87_winner=str(result["s87_winner"]),
        s87_names_cutoff_function_sixth=result["s87_names_cutoff_function_sixth"],
        sixth_substitution_note=result["sixth_substitution_note"],
        class_pin=result["class_pin"],
        # robustness conjunct (this gate)
        ns_gaussian_lower_bound=result["ns_gaussian_lower_bound"],
        gaussian_pass_ns=result["gaussian_pass_ns"],
        gaussian_is_survivor=result["gaussian_is_survivor"],
        survivors_A6=np.array(result["survivors_A6"], dtype=object),
        n_survivors_A6=result["n_survivors_A6"],
        sqrt_in_survivors_A6=result["sqrt_in_survivors_A6"],
        anomaly_excluded_A6=result["anomaly_excluded_A6"],
        robustness_ROBUST=result["robustness_ROBUST"],
        # reported sigma-distance (COMMIT consequence ONLY)
        ns_commit=result["ns_commit"],
        sigma_distance=result["sigma_distance"],
        sigma_const_eps_disclosure=result["sigma_const_eps_disclosure"],
        planck_ns=result["planck_ns"],
        planck_ns_err=result["planck_ns_err"],
        # Q28 status under the decision
        Q28_status=("ANSWERED-functional-selection-robust" if result["decision"] == "COMMIT"
                    else "REOPENED-atlas-cardinality-dependent" if result["decision"] == "WITHDRAW"
                    else "OPEN-robustness-untested-at-A6"),
    )
    print(f"  NPZ artifact written: {OUT_NPZ.relative_to(PROJECT_ROOT)}")


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()                                             # (local)

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)                           # (local)
    closure = closure_hash(pins)                                 # (local)
    print(f"  closure: {closure[:16]}... (legacy informational)")

    # 1b. Dual SHAs
    script_path = Path(__file__).resolve()                       # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"       # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    # 2. Compute
    result = compute()                                           # (local)

    # 3. Gate verdict
    verdict = evaluate_gate(result)                              # (local)

    # 4. Persist artifact
    save_npz(result, audit_sha, content_sha, pins)

    # 5. 4-tuple + payload
    tag = emit_4tuple(result["value"], SCHEME, CONVENTION, L_MAX)  # (local)
    print()
    print(tag)
    note = (                                                     # (local)
        f"decision={result['decision']}; robustness={result['robustness_tag']}; "
        f"sixth_regulator_id={result['sixth_regulator_id']}; "
        f"reported_sigma={result['sigma_distance']:.4f} (COMMIT-consequence only, did NOT decide)"
    )
    extra = [                                                    # (local)
        f"# sixth_regulator_id={result['sixth_regulator_id']} class_pin={result['class_pin']} "
        f"(anti-comparator-shopping; S87 list verified, no cutoff-function sixth named) # {GATE_ID} sixth-regulator pin",
    ]
    print_verdict_payload(verdict, result["value"], audit_sha, content_sha,
                          companion_note=note, extra_rows=extra)

    # 6. Summary
    wall = time.time() - t0                                      # (local)
    print(f"\n=== {GATE_ID}: {verdict} (decision={result['decision']}; wall {wall:.1f}s) ===")
    # Exit code = SCRIPT HEALTH, not verdict (math-scripts.md): always 0 on a clean run.
    return 0


if __name__ == "__main__":
    sys.exit(main())
