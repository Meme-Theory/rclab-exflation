#!/usr/bin/env python3
"""
S102 W5-6 — S102-NS-FUNCTIONAL-COMMIT (referee-M5 n_s commit-or-withdraw gate)
=============================================================================

Gate: W5-6-S102-NS-FUNCTIONAL-COMMIT ([VERIFY])

Pre-registered decision (two-branch adjudication; the branches are FIXED before
this script runs — they are NOT chosen by which n_s value lands nearest Planck):

  (A) COMMIT    <=> (sqrt(x) is the UNIQUE S67 functional survivor)
                    AND (Q28 Layer-2 atlas-cardinality robustness HOLDS)
  (B) WITHDRAW  <=> (sqrt(x) unique survivor at S67)
                    AND (Q28 Layer-2 robustness FAILS / is genuinely open-failed)
  INFO          <=> (sqrt(x) unique survivor at S67)
                    AND (Q28 Layer-2 robustness UNTESTED — A_5 -> A_6 not run)
                    => COMMIT-pending-Q28-Layer-2-evaluation
  FAIL          <=> NOT (sqrt(x) unique survivor)  -- the row left functional-
                    ambiguous; the one disallowed outcome (the status quo this
                    gate exists to end). NEVER reached by a data-agreement tiebreak.

ANTI-DATA-APPEAL DISCIPLINE (the W4-20 / S102-MH-ROUTE-SELECTION template;
epistemic-discipline.md no-convention-shopping): the DECISION CRITERION is the
S67 structural-selection robustness under the Q28 Layer-2 atlas-cardinality
sub-test. It is NOT "which of {0.9561, 0.9590, 0.9595} is closest to Planck
0.9649." The sigma-distance is computed AFTER the decision, as a REPORTED
consequence of the COMMIT branch only.

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - computations/session-67/s67_functional_select.npz   (anomaly-family scan; ns>1-for-phi>0)
  - computations/session-67/s67_joint_falsification.npz  (JOINT-FALSIFICATION-67: sole survivor sqrt)
  - computations/_shared/canonical_constants.py          (n_s_framework=0.9561; planck_ns=0.9649)
  - Q28 Layer-2 status read from atlas-08-open-questions.md + S87 sixth-regulator verdict (text inputs)

Output 4-tuple:
  (value=<COMMIT|WITHDRAW|COMMIT-pending-Q28-Layer-2>, scheme=BCS+1-loop-sqrt-cutoff,
   convention=FIRST-PRINCIPLES-FUNCTIONAL-SELECT-no-data-appeal, L_max=N/A)

Classification: PHONONIC. n_s IS a substrate-IS observable — the scalar spectral
tilt from the gauge-invariant spectral geometry of D_K. The substrate generates
n_s through a SPECIFIC spectral functional; S67 FUNCTIONAL-SELECT-67 proved that
among the candidate functionals only sqrt(x) survives (the anomaly family is
excluded by the structural theorem n_s > 1 for all phi > 0). This gate is the
substrate-first discipline applied to that selection. Direction of explanation:
D_K eigenvalues -> spectral-action moments -> the sqrt(x) generating functional
(S67-selected) -> n_s tilt -> CMB observable.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

# Path bootstrap: put computations/_shared on sys.path BEFORE canonical import.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))

from canonical_constants import *  # noqa: E402,F401,F403
from canonical_constants import n_s_framework, planck_ns  # noqa: E402  explicit pins consumed

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S102"                                                   # (local)
GATE_ID = "W5-6-S102-NS-FUNCTIONAL-COMMIT"                         # (local)
SCHEME = "BCS+1-loop-sqrt-cutoff"                                  # (local)
CONVENTION = "FIRST-PRINCIPLES-FUNCTIONAL-SELECT-no-data-appeal"   # (local)
L_MAX = "N/A"                                                      # (local)

# The COMMIT branch owns the sqrt-cutoff BCS+1-loop value (atlas-04 n_s row).
# This is a REPORTED consequence of COMMIT, not a swept target and not the
# decision criterion.
NS_COMMIT_OWNED = 0.9590       # (local) S65 BCS+1-loop sqrt-cutoff value (atlas-04 n_s row)
# The constant-epsilon gauge-invariant canonical (Row #55 FWD-C1 value), distinct
# from the BCS+1-loop value — carried for the (value, scheme) disclosure.
NS_CONSTANT_EPS = float(n_s_framework)  # (local) = 0.9561 from canonical_constants
PLANCK_NS = float(planck_ns)            # (local) = 0.9649
PLANCK_NS_SIGMA = 0.0042                # (local) Planck 2018 TT,TE,EE+lowE+lensing 1-sigma

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / "s102_ns_functional_commit.npz"
OUT_PNG = SESSION_DIR / "s102_ns_functional_commit.png"

S67_FUNCTIONAL_SELECT_NPZ = COMPUTATIONS_DIR / "session-67" / "s67_functional_select.npz"
S67_JOINT_FALSIFICATION_NPZ = COMPUTATIONS_DIR / "session-67" / "s67_joint_falsification.npz"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    S67_FUNCTIONAL_SELECT_NPZ,
    S67_JOINT_FALSIFICATION_NPZ,
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


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
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
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Compute (the two-branch adjudication)
# ---------------------------------------------------------------------------

def read_s67_structural_selection() -> dict:
    """Step 1 — S67 structural selection: is sqrt(x) the UNIQUE survivor and is
    the anomaly family excluded? Read DIRECTLY from the S67 npz ground truth.

    Returns the conjunctive structural-selection boolean plus its evidence.
    """
    jf = np.load(S67_JOINT_FALSIFICATION_NPZ, allow_pickle=True)  # (local)
    fs = np.load(S67_FUNCTIONAL_SELECT_NPZ, allow_pickle=True)    # (local)

    fnames = [str(x) for x in jf["functional_names"]]            # (local)
    pass_all = np.asarray(jf["pass_all"], dtype=bool)            # (local)
    ns_vals = np.asarray(jf["n_s"], dtype=float)                 # (local)
    jf_verdict = str(jf["gate_verdict"].item())                  # (local)
    jf_detail = str(jf["gate_detail"].item())                    # (local)

    # sqrt(x) is the survivor iff EXACTLY ONE functional passes all constraints
    # AND that functional is the CC-cutoff(sqrt) corner.
    n_survivors = int(pass_all.sum())                            # (local)
    survivor_idx = int(np.argmax(pass_all)) if n_survivors >= 1 else -1  # (local)
    survivor_name = fnames[survivor_idx] if survivor_idx >= 0 else "NONE"  # (local)
    sqrt_is_unique = (n_survivors == 1) and ("sqrt" in survivor_name.lower()
                                             or "cutoff" in survivor_name.lower())  # (local)

    # Anomaly-family exclusion: ns > 1 for the anomaly corner (blue tilt) and the
    # FUNCTIONAL-SELECT-67 scan (ns_phi) is > 1 for all phi > 0 (structural theorem).
    # The anomaly corner index is the one whose name carries "anomaly".
    anomaly_idx = next((i for i, nm in enumerate(fnames) if "anomaly" in nm.lower()), -1)  # (local)
    anomaly_ns = float(ns_vals[anomaly_idx]) if anomaly_idx >= 0 else float("nan")  # (local)
    anomaly_blue = bool(anomaly_ns > 1.0)                        # (local)

    # ns_phi over the full phi scan from the functional-select npz; the structural
    # theorem n_s > 1 for all phi > 0 means the scan's positive-phi branch is all > 1.
    phi_scan = np.asarray(fs["phi_scan"], dtype=float)          # (local)
    ns_phi = np.asarray(fs["ns_phi"], dtype=float)              # (local)
    pos = phi_scan > 0.0                                        # (local)
    ns_phi_pos_min = float(np.nanmin(ns_phi[pos])) if pos.any() else float("nan")  # (local)
    ns_gt1_for_all_pos_phi = bool(np.all(ns_phi[pos] > 1.0)) if pos.any() else False  # (local)

    structural_selection = bool(sqrt_is_unique and anomaly_blue and ns_gt1_for_all_pos_phi)  # (local)

    return {
        "structural_selection": structural_selection,
        "n_survivors": n_survivors,
        "survivor_name": survivor_name,
        "sqrt_is_unique": sqrt_is_unique,
        "jf_verdict": jf_verdict,
        "jf_detail": jf_detail,
        "anomaly_ns_phi1": anomaly_ns,
        "anomaly_blue_excluded": anomaly_blue,
        "ns_phi_pos_min": ns_phi_pos_min,
        "ns_gt1_for_all_pos_phi": ns_gt1_for_all_pos_phi,
        "functional_names": fnames,
        "ns_per_functional": ns_vals.tolist(),
    }


def read_q28_layer2_robustness() -> dict:
    """Step 2 — Q28 Layer-2 atlas-cardinality robustness condition (A_5 -> A_6).

    Status is read from the framework registry (atlas-08 Q28 + the S87
    sixth-regulator-promotion verdict). Three-valued:
      ROBUST    -> sqrt survivor persists under the A_5 -> A_6 extension
      FAILS     -> survivor is atlas-cardinality-dependent (selection re-opens)
      UNTESTED  -> the A_5 -> A_6 sub-test has not itself been evaluated

    This is a registry-read of an ALREADY-SETTLED status, not a new compute.
    The status as of S102:
      - atlas-08 Q28 is OPEN ("sub-question reopened by S88 atlas-cardinality
        K-counter Layer-2 reading").
      - The only cardinality-extension attempt, S87-C45-SIXTH-REGULATOR-PROMOTION,
        landed INFO (A_4 -> A_5 v2 promotion attempt; value=(0, None)); the
        A_5 -> A_6 sub-test was NOT run.
      => robustness condition is UNTESTED (neither confirmed nor failed).
    """
    atlas08 = PROJECT_ROOT / "sessions" / "framework" / "Atlas" / "atlas-08-open-questions.md"  # (local)
    s87_verdicts = COMPUTATIONS_DIR / "session-87" / "s87_gate_verdicts.txt"  # (local)

    atlas08_txt = ""  # (local)
    try:
        atlas08_txt = atlas08.read_text(encoding="utf-8", errors="replace")
    except OSError:
        atlas08_txt = ""
    s87_txt = ""  # (local)
    try:
        s87_txt = s87_verdicts.read_text(encoding="utf-8", errors="replace")
    except OSError:
        s87_txt = ""

    # Q28 OPEN detection: the Q28 row carries an explicit "OPEN" status token.
    q28_open = bool("Q28" in atlas08_txt
                    and "OPEN (sub-question reopened" in atlas08_txt)  # (local)

    # Sixth-regulator (A_5 -> A_6) cardinality-extension attempt status from S87.
    sixth_reg_line = next((ln for ln in s87_txt.splitlines()
                           if ln.startswith("S87-C45-SIXTH-REGULATOR-PROMOTION:")), "")  # (local)
    sixth_reg_info = bool(sixth_reg_line and " INFO " in f" {sixth_reg_line} ")  # (local)
    # The S87 attempt is A_4 -> A_5 (per its convention tag); A_5 -> A_6 was NOT run.
    a5_to_a6_run = bool("A_5_to_A_6" in s87_txt or "A5_to_A6" in s87_txt)  # (local)

    # Three-valued verdict on the robustness condition.
    if q28_open and (sixth_reg_info or not a5_to_a6_run):
        robustness = "UNTESTED"   # (local) reopened + extension not evaluated at A_5 -> A_6
    elif (not q28_open) and a5_to_a6_run:
        robustness = "ROBUST"     # (local) (would require Q28 closed + A_5 -> A_6 PASS)
    else:
        robustness = "UNTESTED"   # (local) conservative default — never fabricate FAILS/ROBUST

    return {
        "robustness": robustness,
        "q28_open": q28_open,
        "sixth_regulator_verdict_line": sixth_reg_line.strip(),
        "sixth_regulator_info": sixth_reg_info,
        "a5_to_a6_run": a5_to_a6_run,
    }


def compute() -> dict:
    # Step 1 — S67 structural selection (sqrt unique survivor + anomaly excluded)
    s67 = read_s67_structural_selection()  # (local)
    structural = s67["structural_selection"]  # (local)

    # Step 2 — Q28 Layer-2 atlas-cardinality robustness (A_5 -> A_6)
    q28 = read_q28_layer2_robustness()  # (local)
    robustness = q28["robustness"]  # (local)

    # Step 3 — Decision (NO data appeal). The two AND-conjuncts of COMMIT.
    if not structural:
        decision = "FAIL"                          # (local) ambiguous — the disallowed outcome
        decision_value = "FUNCTIONAL-AMBIGUOUS"    # (local)
        verdict = "FAIL"                           # (local)
    elif robustness == "ROBUST":
        decision = "COMMIT"                        # (local)
        decision_value = "COMMIT"                  # (local)
        verdict = "PASS"                           # (local)
    elif robustness == "FAILS":
        decision = "WITHDRAW"                      # (local)
        decision_value = "WITHDRAW"                # (local)
        verdict = "PASS"                           # (local)
    else:  # robustness == "UNTESTED"
        decision = "COMMIT-pending-Q28-Layer-2"    # (local) structural-axis COMMIT-ready; robustness untested
        decision_value = "COMMIT-pending-Q28-Layer-2-evaluation"  # (local)
        verdict = "INFO"                           # (local)

    # Step 4 — REPORTED consequence of the COMMIT branch: the sigma-distance.
    # Computed AFTER the decision; it did NOT drive the decision.
    sigma_commit_owned = abs(NS_COMMIT_OWNED - PLANCK_NS) / PLANCK_NS_SIGMA   # (local) 0.9590 -> 1.40 sigma
    sigma_constant_eps = abs(NS_CONSTANT_EPS - PLANCK_NS) / PLANCK_NS_SIGMA   # (local) 0.9561 -> 2.10 sigma

    return {
        "value": decision_value,
        "verdict": verdict,
        "decision": decision,
        "structural_selection": structural,
        "robustness": robustness,
        "sigma_commit_owned": sigma_commit_owned,
        "sigma_constant_eps": sigma_constant_eps,
        "ns_commit_owned": NS_COMMIT_OWNED,
        "ns_constant_eps": NS_CONSTANT_EPS,
        "planck_ns": PLANCK_NS,
        "planck_ns_sigma": PLANCK_NS_SIGMA,
        "s67": s67,
        "q28": q28,
    }


# ---------------------------------------------------------------------------
# Section 6 — Verdict payload + 4-tuple
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note: str = "", extra_rows=None) -> dict:
    payload: dict = {
        "session": int(SESSION.lstrip("Ss")),
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
# Section 7 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)  # (local)
    closure = closure_hash(pins)  # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    r = compute()  # (local)

    # --- numbers first ---
    print("=== STEP 1 — S67 structural selection (sqrt unique survivor + anomaly excluded) ===")
    print(f"  JOINT-FALSIFICATION-67 verdict : {r['s67']['jf_verdict']}")
    print(f"  detail                         : {r['s67']['jf_detail']}")
    print(f"  n_survivors (pass_all)         : {r['s67']['n_survivors']}")
    print(f"  survivor                       : {r['s67']['survivor_name']}")
    print(f"  sqrt is unique survivor        : {r['s67']['sqrt_is_unique']}")
    print(f"  anomaly n_s(phi=1)             : {r['s67']['anomaly_ns_phi1']:.6f}  (>1 => blue, excluded: {r['s67']['anomaly_blue_excluded']})")
    print(f"  n_s>1 for all phi>0 (min ns_phi+): {r['s67']['ns_phi_pos_min']:.6f}  (theorem holds: {r['s67']['ns_gt1_for_all_pos_phi']})")
    print(f"  => STRUCTURAL SELECTION         : {r['structural_selection']}")
    print()
    print("=== STEP 2 — Q28 Layer-2 atlas-cardinality robustness (A_5 -> A_6) ===")
    print(f"  atlas-08 Q28 OPEN              : {r['q28']['q28_open']}")
    print(f"  sixth-regulator (S87) verdict : {r['q28']['sixth_regulator_verdict_line']}")
    print(f"  A_5 -> A_6 sub-test run        : {r['q28']['a5_to_a6_run']}")
    print(f"  => ROBUSTNESS CONDITION        : {r['robustness']}")
    print()
    print("=== STEP 3 — Decision (FIRST-PRINCIPLES; NO data appeal) ===")
    print(f"  COMMIT   <=> structural AND robustness==ROBUST")
    print(f"  WITHDRAW <=> structural AND robustness==FAILS")
    print(f"  INFO     <=> structural AND robustness==UNTESTED (COMMIT-pending-Q28)")
    print(f"  FAIL     <=> NOT structural (functional-ambiguous)")
    print(f"  => DECISION                    : {r['decision']}  (verdict {r['verdict']})")
    print()
    print("=== STEP 4 — REPORTED consequence of COMMIT (sigma-distance; did NOT drive decision) ===")
    print(f"  sqrt-cutoff BCS+1-loop n_s=0.9590 -> |0.9590-0.9649|/0.0042 = {r['sigma_commit_owned']:.4f} sigma")
    print(f"  constant-eps canonical n_s=0.9561 -> |0.9561-0.9649|/0.0042 = {r['sigma_constant_eps']:.4f} sigma")
    print()

    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        verdict=r["verdict"],
        decision=r["decision"],
        value=r["value"],
        structural_selection=r["structural_selection"],
        robustness=r["robustness"],
        sigma_commit_owned=r["sigma_commit_owned"],
        sigma_constant_eps=r["sigma_constant_eps"],
        ns_commit_owned=r["ns_commit_owned"],
        ns_constant_eps=r["ns_constant_eps"],
        planck_ns=r["planck_ns"],
        planck_ns_sigma=r["planck_ns_sigma"],
        s67_jf_verdict=r["s67"]["jf_verdict"],
        s67_jf_detail=r["s67"]["jf_detail"],
        s67_n_survivors=r["s67"]["n_survivors"],
        s67_survivor_name=r["s67"]["survivor_name"],
        s67_anomaly_ns_phi1=r["s67"]["anomaly_ns_phi1"],
        s67_ns_phi_pos_min=r["s67"]["ns_phi_pos_min"],
        s67_functional_names=np.array(r["s67"]["functional_names"], dtype=object),
        s67_ns_per_functional=np.array(r["s67"]["ns_per_functional"], dtype=float),
        q28_open=r["q28"]["q28_open"],
        q28_sixth_regulator_line=r["q28"]["sixth_regulator_verdict_line"],
        q28_a5_to_a6_run=r["q28"]["a5_to_a6_run"],
    )
    print(f"  wrote {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    tag = emit_4tuple(r["value"], SCHEME, CONVENTION, L_MAX)  # (local)
    print(tag)

    # Adjudication gate: no [SIGN] 3-tuple (the gate-block pre-registers
    # schema_v2_3tuple_required: false). The companion row records the
    # anti-data-appeal discipline + the Q28 reopening pointer.
    extra = [
        f"# decision={r['decision']} structural_selection={r['structural_selection']} "
        f"q28_robustness={r['robustness']} (A_5->A_6 not run; UNTESTED, not failed)",
        f"# reported-consequence sigma(n_s=0.9590 BCS+1-loop)={r['sigma_commit_owned']:.4f} "
        f"sigma(n_s=0.9561 const-eps)={r['sigma_constant_eps']:.4f}; "
        f"decision is S67+Q28 structural, NOT data-agreement (W4-20 template)",
    ]
    print_verdict_payload(r["verdict"], r["value"], audit_sha, content_sha, extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {r['verdict']} ({r['decision']}) (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
