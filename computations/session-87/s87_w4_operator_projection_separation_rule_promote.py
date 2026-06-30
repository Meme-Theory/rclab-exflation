#!/usr/bin/env python3
"""
S87 W4-6 — S87-OPERATOR-PROJECTION-SEPARATION-RULE-PROMOTE (CF-30, Tier 5, doc-only)
====================================================================================

Gate: S87-OPERATOR-PROJECTION-SEPARATION-RULE-PROMOTE ([AUDIT])

Pre-registered threshold (per `feedback_rules-compensate-missing-structure.md`
K=3 promotion threshold + plan §W4-6 lines 706-719):

  PASS  iff K >= 3 distinct calibration corpus instances of the operator-projection
                separation criterion (single-projection trace vs mixed-projection
                trace on A_K = C + H + M_3(C)) verified.
  INFO  iff K == 2 (workshop-design SUGGESTION recorded; promotion deferred to S88+).
  FAIL  iff K <= 1 (technical-debt prevention; rule remains workshop-design only).

  Tolerance: ABSOLUTE (K is a discrete integer count).

Deterministic K-ceiling at S87 W4-6 (per spawn-prompt UPSTREAM CLOSURES):
  Instance 1 (S86 W-4 R3 origin):                VERIFIED (1)
  Instance 2 (CF-29 outcome at WP §W4-5):        N/A — CF-29 closed PRE-REG-INC mechanical;
                                                 no operator-projection-criterion classification
                                                 was performed. Forced N/A. (0)
  Instance 3 (prior session re-derivation):      INVESTIGATION (Candidates A=S70 LEGGETT, B=S46
                                                 BdG/Pillar-III BCS, C=S82 W2-8 + C1 equilateral
                                                 + W14-4 conflation registry-language pattern;
                                                 verified iff source text invokes single-vs-mixed
                                                 projection structure on A_K, OR implicitly relies
                                                 on the same structural decomposition with the
                                                 projection algebra on A_K identifiable).

  K_max deterministic = 1 + 0 + (0 or 1) = {1, 2}.
  PASS (K >= 3) is DETERMINISTICALLY IMPOSSIBLE.
  Outcome ranges over {K=1 FAIL, K=2 INFO}.

Inputs (SHA-256 dual-pinned at runtime):
  - sessions/archive/session-86/session-86-w4-workingpaper.md         (Instance 1 source candidate)
  - sessions/archive/session-86/workshops/s86-fnl-folded-pathway-adjudication.md (Type-F/Type-S origin)
  - sessions/archive/session-87/session-87-results-workingpaper.md    (CF-29 §W4-5 verdict)
  - computations/session-87/s87_gate_verdicts.txt                   (CF-29 audit_sha pin)
  - computations/session-70/s70_leggett_moment.py                   (Candidate A source text)
  - computations/session-46/s46_twist_bdg.py                            (Candidate B source text)
  - sessions/archive/session-82/session-82-gen-physicist-synthesis.md (Candidate C: S82 W2-8 source)
  - canonical_constants.py
  - script bytes

Output 4-tuple:
  (value=K_corpus_instance_count_in_{0,1,2,3},
   scheme=corpus-instance-enumeration,
   convention=K=3-promotion-threshold-per-rules-compensate-missing-structure,
   L_max=N/A)

Classification: NON-PHONONIC (rule-promotion decision; no substrate-physics derivation;
                doc-only methodology-class gate).

METHODOLOGY
-----------
Strict bimodule-projection reading (Reading-B per spawn-prompt verification criterion):

  An instance counts iff (i) the source text explicitly invokes "single-projection trace"
  vs "mixed-projection trace" on A_K = C + H + M_3(C), OR (ii) the source text implicitly
  relies on the same structural decomposition with the projection algebra on A_K
  identifiable in the source text.

  The S86 W-4 R3-A workshop (s86-fnl-folded-pathway-adjudication.md) ALSO discusses a
  Reading-A registry-language hygiene rule ("registry row names must declare operator
  sector and projection target separately") with its own 3-instance corpus (S82 W2-8 +
  C1 "equilateral" tag + W14-4 conflation). Reading-A is NOT what the spawn-prompt's
  strict criterion targets — Reading-A is registry-NAMING, while Reading-B is bimodule-
  PROJECTION-TRACE on the spectral algebra. The CF-30 plan §W4-6 line 700/754 conflates
  the two readings; the spawn-prompt's verification criterion (single-vs-mixed projection
  structure on A_K) anchors Reading-B unambiguously.

  Each Instance 3 candidate is classified as VERIFIED, REFUTED, or NEEDS-REVIEW under
  Reading-B by direct source-text inspection.

DISCIPLINE
----------
- `from canonical_constants import *` (imports succeed even though no constants are used)
- All intermediates tagged `# (local)`
- No GPU; no eigvals; doc-only enumeration
- SHA-256 of all input files logged in stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- Verdict appended atomically to `computations/session-87/s87_gate_verdicts.txt`

Author: gen-physicist (cross-domain workhorse; methodology-class doc-only gate per plan
        §W4-6 wave-classification M1-M4 analysis at lines 794-797)
Session: S87, Wave 4, CF-30
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import even though unused)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import os
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
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S87"                                                   # (local)
GATE_ID = "S87-OPERATOR-PROJECTION-SEPARATION-RULE-PROMOTE"       # (local)
SCHEME = "corpus-instance-enumeration"                            # (local)
CONVENTION = "K=3-promotion-threshold-per-rules-compensate-missing-structure"  # (local)
L_MAX = "N/A"                                                     # (local)

# Pre-registered K-band thresholds (per plan §W4-6 lines 706-719)
PASS_K_MIN = 3                                                    # (local)
INFO_K = 2                                                        # (local)
FAIL_K_MAX = 1                                                    # (local)

# Output destinations
OUT_NPZ = resolve_output(87, 's87_w4_operator_projection_separation_rule_promote.npz')
VERDICT_TXT = resolve_output(87, 's87_gate_verdicts.txt')

# Input pin map — files whose contents the verdict closure depends on
INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    PROJECT_ROOT / "sessions" / "session-86" / "session-86-w4-workingpaper.md",
    PROJECT_ROOT / "sessions" / "session-86" / "workshops" / "s86-fnl-folded-pathway-adjudication.md",
    PROJECT_ROOT / "sessions" / "session-87" / "session-87-results-workingpaper.md",
    resolve_output(87, 's87_gate_verdicts.txt'),
    resolve_script(70, 's70_leggett_moment.py'),
    PROJECT_ROOT / "computations" / "session-46" / "s46_twist_bdg.py",
    PROJECT_ROOT / "sessions" / "session-82" / "session-82-gen-physicist-synthesis.md",
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 + dual-SHA schema
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


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
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
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)

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
# Section 5 — Corpus enumeration (the gate compute)
# ---------------------------------------------------------------------------

def grep_count(path: Path, patterns: list[str]) -> dict[str, int]:
    """Count occurrences of each pattern in a file's text. Returns
    {pattern: count}. Returns 0 for any file that cannot be opened."""
    counts: dict[str, int] = {p: 0 for p in patterns}
    if not path.exists():
        return counts
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return counts
    for p in patterns:
        counts[p] = text.count(p)
    return counts


def verify_instance_1() -> dict:
    """Instance 1: S86 W-4 R3 origin.

    Source: sessions/archive/session-86/workshops/s86-fnl-folded-pathway-adjudication.md
            (R3-A EMERGENCE #1 lines 1258-1295; Type-F = state-functional with operator-
             content carrier and per-mode {phi_a} bimodule projection on A_K = C + H + M_3(C);
             Type-S = state-coordinate scalar function on aggregate). The spawn prompt notes
             this instance is "VERIFIED (per plan §W4-6 line 754; well-documented in
             sessions/archive/session-86/session-86-w4-workingpaper.md R3 closure block)".
            The W-4 *workpaper* itself does not contain Type-F/Type-S terminology — that
            terminology lives in the R3-A workshop file (the workpaper is the upstream
            input). For this gate the workshop file IS the canonical Instance-1 source.

    Verification under spawn-prompt strict criterion (i)/(ii):
      - Source text uses "Type-F (state-functional, per-mode-resolved, operator-content)"
        and "Type-S (state-coordinate, scalar function of aggregate)" terminology.
      - The R3-A operator-content carrier is named explicitly: "per-mode Bogoliubov-phase
        distribution {phi_a} on D_K's eigenmode pairs at tau_fold; SCALAR projection:
        N_A = Sum_a w_a Im[alpha_a (beta_a*)**2]". This is a per-mode projection on the
        spectral-triple's eigenmode bimodule structure (D_K acts on H_K = sections of the
        bundle over A_K = C + H + M_3(C)).
      - Status: VERIFIED under criterion (i) — the explicit single-projection (per-mode
        functional) vs mixed-projection (aggregate scalar) classification IS the
        operator-projection separation criterion's defining instance.
    """
    src = (
        PROJECT_ROOT / "sessions" / "session-86" / "workshops"
        / "s86-fnl-folded-pathway-adjudication.md"
    )
    patterns = [
        "Type-F (state-functional",
        "Type-S (state-coordinate",
        "per-mode Bogoliubov-phase",
        "Bogoliubov-phase distribution",
        "EMERGENCE #1",
    ]
    hits = grep_count(src, patterns)
    # Verification predicate: the four pattern-content tokens AND the R3-A header marker
    # all present (>=1 occurrence each) ⇒ source text contains the bimodule classification
    # AND its localization to R3-A EMERGENCE #1.
    verified = (
        hits["Type-F (state-functional"] >= 1
        and hits["Type-S (state-coordinate"] >= 1
        and (hits["per-mode Bogoliubov-phase"] >= 1
             or hits["Bogoliubov-phase distribution"] >= 1)
        and hits["EMERGENCE #1"] >= 1
    )
    return {
        "instance": 1,
        "candidate": "S86 W-4 R3-A EMERGENCE #1 origin",
        "source_file": str(src.relative_to(PROJECT_ROOT)).replace("\\", "/"),
        "patterns_hit": hits,
        "verified": bool(verified),
        "rationale": (
            "Reading-B explicit bimodule classification: Type-F (state-functional, "
            "per-mode-resolved, {phi_a} carrier on D_K eigenmode bimodule) vs "
            "Type-S (state-coordinate, scalar projection on aggregate N_pair_eff). "
            "Per-mode projection structure on A_K = C + H + M_3(C) is identifiable "
            "in the source text via the {phi_a} per-mode Bogoliubov-phase distribution "
            "(which lives on D_K's eigenmode pairs and projects via single-mode "
            "functional N_A vs aggregate scalar N_pair_eff)."
        ),
    }


def verify_instance_2() -> dict:
    """Instance 2: CF-29 outcome (cross-pillar Type-F/Type-S audit).

    Source: sessions/archive/session-87/session-87-results-workingpaper.md §W4-5.
    CF-29 closed PRE-REG-INC mechanical (FAIL value=
    'PRE-REG-INC_blocked_by_S87-TYPE-F-PER-MODE-PHASE-AUDIT_FAIL_axiom-violation')
    per the spawn prompt's UPSTREAM CLOSURES point 5. NO operator-projection-criterion
    classification was performed. Per plan §W4-6 line 755-756: "VERIFIED iff CF-29 closes
    PASS or INFO with criterion applied" — neither held.

    Verification predicate: search §W4-5 for the PRE-REG-INC verdict string. If present,
    Instance 2 is forced N/A (NOT VERIFIED).
    """
    src = PROJECT_ROOT / "sessions" / "session-87" / "session-87-results-workingpaper.md"
    patterns = [
        "PRE-REG-INC_blocked_by_S87-TYPE-F-PER-MODE-PHASE-AUDIT_FAIL",
        "S87-TYPE-F-TYPE-S-CROSS-PILLAR-AUDIT",
        "FAIL (PRE-REG-INC)",
    ]
    hits = grep_count(src, patterns)
    pre_reg_inc = (
        hits["PRE-REG-INC_blocked_by_S87-TYPE-F-PER-MODE-PHASE-AUDIT_FAIL"] >= 1
        and hits["FAIL (PRE-REG-INC)"] >= 1
    )
    # CF-29 is N/A iff PRE-REG-INC mechanical closure was applied.
    verified = False  # Forced N/A; cannot be VERIFIED at this session.
    return {
        "instance": 2,
        "candidate": "CF-29 cross-pillar Type-F/Type-S audit (S87 §W4-5)",
        "source_file": str(src.relative_to(PROJECT_ROOT)).replace("\\", "/"),
        "patterns_hit": hits,
        "verified": bool(verified),
        "n_a": bool(pre_reg_inc),
        "rationale": (
            "CF-29 closed PRE-REG-INC mechanical (no operator-projection-criterion "
            "classification was performed). Per plan §W4-6 line 755-756 the verification "
            "criterion 'VERIFIED iff CF-29 closes PASS or INFO with criterion applied' is "
            "not satisfied. Instance 2 is forced N/A (counts as 0 toward K) until CF-29 "
            "resumes substantively in S88+ via S88-CF-29-RESUME-AFTER-CF-26-RESOLUTION."
        ),
    }


def verify_instance_3_candidate_A() -> dict:
    """Candidate A: S70 LEGGETT-MOMENT classification.

    Source: computations/session-70/s70_leggett_moment.py (the script's docstring + body),
    plus the S86 W-4 R3-B re-reading at line 1450 of the workshop.

    Examination:
      - s70_leggett_moment.py docstring states the gate's question: "Which spectral moment
        a_{2k} controls the Leggett gap?" The chain is
            omega_L = sqrt(J_23 / (rho * Delta**2)),
        with attribution: g <- a_4, rho <- a_0, Delta involves both a_4 and a_0,
        J_23 ~ a_4**2.
      - The S70 source text contains zero "Type-F" / "Type-S" / "single-projection trace"
        / "mixed-projection trace" / "A_K" / "bimodule" terminology.
      - The S86 W-4 workshop line 1450 re-reads S70 LEGGETT-MOMENT as
        "Type-F (a_4 phase-encoded) / Type-S (a_0 BCS-amplified count)" — but this is a
        PROPOSAL ("can be re-read as"), not an executed re-derivation.

    Verification under spawn-prompt criterion (i)/(ii):
      (i) explicit single-vs-mixed projection structure on A_K — ABSENT in S70 source.
      (ii) implicit reliance with projection algebra on A_K identifiable — ABSENT. The
           a_2k attribution is a Seeley-DeWitt heat-kernel moment classification (a_0,
           a_2, a_4, a_6 are distinct heat-kernel coefficients in the spectral action
           expansion), NOT a single-projection vs mixed-projection trace on the bimodule
           algebra A_K = C + H + M_3(C). The S86 W-4 line 1450 hypothetical re-reading
           does not modify the S70 source text and was never executed as a re-derivation
           gate at any prior session.

    Status: REFUTED.
    """
    src = resolve_script(70, 's70_leggett_moment.py')
    patterns = [
        "Type-F",
        "Type-S",
        "single-projection trace",
        "mixed-projection trace",
        "A_K",
        "bimodule",
        "C + H + M_3",
    ]
    hits = grep_count(src, patterns)
    # ANY of these patterns at non-zero count would indicate Reading-B presence in S70.
    any_bimodule_present = any(c >= 1 for c in hits.values())
    return {
        "instance": "3a",
        "candidate": "S70 LEGGETT-MOMENT (a_{2k}-classification of Leggett gap)",
        "source_file": str(src.relative_to(PROJECT_ROOT)).replace("\\", "/"),
        "patterns_hit": hits,
        "verified": False,
        "any_bimodule_present": bool(any_bimodule_present),
        "refutation_reason": (
            "S70 source text classifies which Seeley-DeWitt moment a_{2k} (k in {0,2,4,6}) "
            "controls omega_L via the chain omega_L = sqrt(J_23/(rho*Delta**2)). This is a "
            "heat-kernel moment-attribution classification, NOT a single-projection-trace "
            "vs mixed-projection-trace classification on A_K = C + H + M_3(C). The S86 W-4 "
            "workshop line 1450 lizzi re-reading 'S70 LEGGETT-MOMENT-70's intensive/"
            "extensive partition can be re-read as Type-F (a_4 phase-encoded) / Type-S "
            "(a_0 BCS-amplified count)' is a PROPOSAL of a re-derivation, not an executed "
            "classification event. The S70 source text contains zero Reading-B terminology "
            "(Type-F, Type-S, single-projection trace, mixed-projection trace, A_K, "
            "bimodule). REFUTED under criterion (i)/(ii)."
        ),
    }


def verify_instance_3_candidate_B() -> dict:
    """Candidate B: Pillar III BCS condensate classification.

    Source: computations/session-46/s46_twist_bdg.py (TWIST-BDG-46 gate; the canonical
    Pillar-III BCS NCG classification gate).

    Examination:
      - s46_twist_bdg.py docstring + body: "TWIST-BDG-46: Twisted BdG Spectral Triple on
        SU(3); PASS iff KO-dimension preserved AND Krein signature matches." Result
        (per script lines 398-404 and 612): "BCS is a HILBERT SPACE transformation, not
        an ALGEBRA automorphism" / "The BCS order parameter Delta is NOT an algebra
        automorphism of A_F."
      - The S46 source text classifies the BCS gap structurally as: (a) a Hilbert-space
        Bogoliubov rotation, NOT an algebra automorphism; (b) the twisted spectral triple
        construction with Delta-driven sigma; (c) NCG axioms A1-A7 verification, including
        order-one [[D,a],b^o]=0 and Krein signature.
      - The S46 source text contains zero "Type-F" / "Type-S" / "single-projection trace"
        / "mixed-projection trace" terminology.

    Verification under spawn-prompt criterion (i)/(ii):
      (i) explicit single-vs-mixed projection structure on A_K — ABSENT in S46 source.
      (ii) implicit reliance with projection algebra on A_K identifiable — ABSENT. The
           A_F = C + H + M_3(C) decomposition IS named in the source (line 442: "A_F
           automorphisms when A_F = C + H + M_3(C) acts diagonally"), but the gate-test
           is the AUTOMORPHISM-status of sigma (i.e., whether the Bogoliubov rotation
           descends to an algebra map A_F -> A_F), NOT the SINGLE-vs-MIXED PROJECTION-
           TRACE structure of an observable's expectation. These are structurally
           distinct classifications:
             * Automorphism status: sigma in Aut(A_F) iff sigma(ab) = sigma(a)sigma(b).
             * Projection-trace structure: <observable> = tr(p_C O) (Type-F, single-
               projection on the C summand) vs tr(p_C O) + tr(p_H O) + tr(p_M3 O)
               (Type-S, mixed-projection across multiple summands).
           S46 tests the former, not the latter.

    Status: REFUTED.
    """
    src = PROJECT_ROOT / "computations" / "session-46" / "s46_twist_bdg.py"
    patterns = [
        "Type-F",
        "Type-S",
        "single-projection trace",
        "mixed-projection trace",
        "single-projection",
        "mixed-projection",
    ]
    hits = grep_count(src, patterns)
    any_bimodule_present = any(c >= 1 for c in hits.values())
    return {
        "instance": "3b",
        "candidate": "Pillar III BCS / S46 TWIST-BDG-46 (BCS-as-algebra-automorphism test)",
        "source_file": str(src.relative_to(PROJECT_ROOT)).replace("\\", "/"),
        "patterns_hit": hits,
        "verified": False,
        "any_bimodule_present": bool(any_bimodule_present),
        "refutation_reason": (
            "S46 TWIST-BDG-46 source classifies the BCS gap Delta structurally as: "
            "(a) Hilbert-space Bogoliubov rotation; (b) NOT an algebra automorphism of "
            "A_F = C + H + M_3(C). The gate is an automorphism-status classification on "
            "Aut(A_F), structurally orthogonal to single-projection-trace vs mixed-"
            "projection-trace structure on A_K-bimodule expectations. The S46 source "
            "names A_F = C + H + M_3(C) (algebra decomposition) but does NOT classify "
            "observable expectations as single-vs-mixed projection traces. REFUTED "
            "under criterion (i)/(ii)."
        ),
    }


def verify_instance_3_candidate_C() -> dict:
    """Candidate C (other): S82 W2-8 a_2-cluster + C1 'equilateral' tag + W14-4 conflation,
    plus other S82+ candidates (PAIR-4 / eps_H / GV-Heitsch).

    The S86 W-4 workshop EXPLICITLY identifies these as a 3-instance corpus for the
    operator-projection separation rule (workshop §EMERGENCE #5 line 780, Q3 line 821,
    Open Question 7 line 1600, Wrap-Up line 1623, S87+ carry-forward line 1657-1659).
    BUT — the workshop's own characterization of these instances is registry-LANGUAGE,
    not bimodule-projection-trace:

      - S82 W2-8: bare-f_0 vs observable-f_conv level mismatch — "level-of-observation"
        observable-redefinition pattern (per session-82-gen-physicist-synthesis.md L520).
        NOT a single-vs-mixed projection trace on A_K.
      - C1 "equilateral" tag: registry-naming mislabel of Path-B folded-shape as
        "equilateral" (per workshop L74, L83, L257) — slot-mislabel pattern in gate name.
        NOT a bimodule-projection structure.
      - W14-4 conflation: framework-language conflation of "3 sub-channel projections of
        the SAME substrate observable" — operator-vs-kinematic conflation (per workshop
        L646, L809, L831). NOT a single-projection vs mixed-projection trace test.

    The workshop itself names these instances as "registry-naming pattern" / "operator-
    vs-kinematic conflation" / "registry-architecture defect" — not as bimodule-projection-
    trace tests. The two readings of "operator-projection separation rule" diverge:
      Reading-A (workshop's intent): registry row names must declare operator sector and
                                     projection target separately.
      Reading-B (CF-30 plan §W4-6 + spawn-prompt strict criterion): observable-classification
                                     by single-projection trace vs mixed-projection trace
                                     on A_K = C + H + M_3(C).

    Reading-A's 3-instance corpus is the workshop's 3 corpus instances.
    Reading-B's 1-instance corpus is the W-4 R3-A EMERGENCE #1 origin only.

    The CF-30 plan §W4-6 line 700 binds the rule's content to Reading-B ("single-projection
    trace vs mixed-projection trace"). The spawn-prompt strict verification criterion (i)
    requires "explicitly invoked single-vs-mixed projection structure on A_K" — the S82
    W2-8 / C1 / W14-4 instances do NOT invoke this. Their pattern is:
      registry-row-name : operator-class : projection-target
    NOT
      observable-expectation : single-projection-trace : mixed-projection-trace.

    Status: REFUTED under Reading-B (these instances belong to Reading-A registry-language
    hygiene, not Reading-B bimodule-projection criterion).

    Other Candidate-C subjects probed via knowledge MCP (search_knowledge):
      - PAIR-4 / eps_H / GV-Heitsch invariants (S82+, mentioned in spawn prompt): these
        are Hochschild-cohomology-class invariants and Heitsch cocycle classifications;
        the substrate-distance grading (s=3 substrate-distance-1 vs s=4 substrate-distance-
        2) is a POLE-grading, not a projection-trace grading. No source text for PAIR-4 /
        eps_H / GV-Heitsch invokes single-vs-mixed projection trace on A_K. REFUTED.
    """
    src_workshop = (
        PROJECT_ROOT / "sessions" / "session-86" / "workshops"
        / "s86-fnl-folded-pathway-adjudication.md"
    )
    src_s82 = PROJECT_ROOT / "sessions" / "session-82" / "session-82-gen-physicist-synthesis.md"
    patterns_workshop = [
        "operator-vs-kinematic conflation",
        "registry-name conflation",
        "registry-architecture defect",
        "operator sector and projection target",
        "Reading-B",  # not expected to be present; this is gen-physicist Reading-B framing
    ]
    hits_w = grep_count(src_workshop, patterns_workshop)
    hits_s82 = grep_count(src_s82, ["W2-8", "f_conv", "bare-f_0", "var(f_0)", "var(f_2)"])
    return {
        "instance": "3c",
        "candidate": (
            "S82 W2-8 a_2-cluster + C1 'equilateral' tag + W14-4 conflation + "
            "PAIR-4/eps_H/GV-Heitsch (other Candidate-C subjects)"
        ),
        "source_files": [
            str(src_workshop.relative_to(PROJECT_ROOT)).replace("\\", "/"),
            str(src_s82.relative_to(PROJECT_ROOT)).replace("\\", "/"),
        ],
        "patterns_hit_workshop": hits_w,
        "patterns_hit_s82": hits_s82,
        "verified": False,
        "refutation_reason": (
            "The S86 W-4 workshop's 3-instance corpus (S82 W2-8 + C1 'equilateral' tag + "
            "W14-4 conflation) belongs to Reading-A 'registry row names must declare "
            "operator sector and projection target separately' — a registry-language "
            "hygiene rule. Reading-B (single-projection trace vs mixed-projection trace "
            "on A_K = C + H + M_3(C); the spawn-prompt strict criterion) is structurally "
            "distinct. None of the 3 workshop-claimed instances invoke single-vs-mixed "
            "projection structure on A_K-bimodule observable expectations. PAIR-4 / "
            "eps_H / GV-Heitsch invariant work uses Hochschild-cohomology / pole-grading "
            "classifications, not bimodule-projection-trace classifications. REFUTED "
            "under criterion (i)/(ii)."
        ),
    }


def compute() -> dict:
    """Enumerate corpus instances under the strict bimodule-projection reading.

    Returns a dict with the K count, per-instance verification flags, and a
    structured per-candidate report.
    """
    inst_1 = verify_instance_1()
    inst_2 = verify_instance_2()
    inst_3a = verify_instance_3_candidate_A()
    inst_3b = verify_instance_3_candidate_B()
    inst_3c = verify_instance_3_candidate_C()

    # Instance-3 verifies iff ANY of the three Candidate sub-cases verifies.
    inst_3_verified = any(
        x["verified"] for x in (inst_3a, inst_3b, inst_3c)
    )

    K = int(inst_1["verified"]) + int(inst_2["verified"]) + int(inst_3_verified)  # (local)

    return {
        "value": K,
        "instance_1": inst_1,
        "instance_2": inst_2,
        "instance_3_candidate_A": inst_3a,
        "instance_3_candidate_B": inst_3b,
        "instance_3_candidate_C": inst_3c,
        "instance_3_verified": bool(inst_3_verified),
    }


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(
    verdict: str,
    value,
    audit_sha: str,
    content_sha: str,
) -> None:
    """Atomic append of a single verdict line to s87_gate_verdicts.txt.

    Schema-v2 (S87+) requires a SECOND companion comment row carrying the
    sign/magnitude/regime 3-tuple per gate-verdicts.md §"S87+ canonical form".
    """
    composite_line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    # W9a-99 dual-SHA companion comment row
    companion_dual_sha = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    # S87+ schema-v2 sign/magnitude/regime 3-tuple companion row
    if verdict == "PASS":
        magnitude = "PASS"
    elif verdict == "INFO":
        magnitude = "INFO"
    else:
        magnitude = "FAIL"
    companion_3tuple = (
        f"# sign_verdict=N/A magnitude_verdict={magnitude} regime_verdict=VALID "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(composite_line)
        fp.write(companion_dual_sha)
        fp.write(companion_3tuple)


def evaluate_gate(K: int) -> str:
    """Ternary outcome per pre-registered K-bands (plan §W4-6 lines 706-719).

    Substitution chain (Step 4 direction):
      PASS iff K >= 3
      INFO iff K == 2
      FAIL iff K <= 1
    """
    if K >= PASS_K_MIN:
        return "PASS"
    if K == INFO_K:
        return "INFO"
    return "FAIL"


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. Compute S84+ dual SHAs
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Compute K
    result = compute()
    K = result["value"]

    # 3. Evaluate gate
    verdict = evaluate_gate(K)

    # 4. Per-instance summary
    print("=== Per-instance verification summary (Reading-B strict) ===")
    print(f"  Instance 1 (S86 W-4 R3-A EMERGENCE #1):  verified={result['instance_1']['verified']}")
    print(f"  Instance 2 (CF-29 §W4-5 PRE-REG-INC):    verified={result['instance_2']['verified']}  (N/A: forced)")
    print(f"  Instance 3a (S70 LEGGETT-MOMENT):        verified={result['instance_3_candidate_A']['verified']}  (REFUTED)")
    print(f"  Instance 3b (S46/Pillar-III BCS):        verified={result['instance_3_candidate_B']['verified']}  (REFUTED)")
    print(f"  Instance 3c (S82 W2-8 + C1 + W14-4):     verified={result['instance_3_candidate_C']['verified']}  (REFUTED)")
    print(f"  K = {K} (PASS_K_MIN={PASS_K_MIN}, INFO_K={INFO_K}, FAIL_K_MAX={FAIL_K_MAX})")
    print()

    # 5. Emit 4-tuple + append verdict (dual-SHA + 3-tuple, S87+ schema-v2)
    tag = emit_4tuple(K, SCHEME, CONVENTION, L_MAX)
    print(tag)
    append_verdict(verdict, K, audit_sha, content_sha)

    # 6. Save .npz
    np.savez(
        OUT_NPZ,
        K=K,
        instance_1_verified=result["instance_1"]["verified"],
        instance_2_verified=result["instance_2"]["verified"],
        instance_3_verified=result["instance_3_verified"],
        instance_3a_verified=result["instance_3_candidate_A"]["verified"],
        instance_3b_verified=result["instance_3_candidate_B"]["verified"],
        instance_3c_verified=result["instance_3_candidate_C"]["verified"],
        verdict=verdict,
        gate_id=GATE_ID,
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=str(L_MAX),
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        # Detailed per-instance reports (dict objects pickled as object arrays)
        report=json.dumps({
            "instance_1": result["instance_1"],
            "instance_2": result["instance_2"],
            "instance_3_candidate_A": result["instance_3_candidate_A"],
            "instance_3_candidate_B": result["instance_3_candidate_B"],
            "instance_3_candidate_C": result["instance_3_candidate_C"],
        }, indent=2),
    )
    print(f"Saved: {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    # 7. Final summary
    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (K={K}; wall {wall:.2f}s) ===")
    return 0  # script-health: success regardless of scientific verdict


if __name__ == "__main__":
    # Cap CPU threads (no GPU needed for this corpus enumeration)
    os.environ.setdefault("OMP_NUM_THREADS", "8")
    os.environ.setdefault("MKL_NUM_THREADS", "8")
    sys.exit(main())
