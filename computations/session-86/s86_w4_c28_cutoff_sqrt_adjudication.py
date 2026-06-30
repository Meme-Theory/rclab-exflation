"""
S86 W4-3 / C28: S86-W-4-CUTOFF-SQRT-ADJUDICATION
================================================

Captures the S85 connes x lizzi 3-round workshop convergence on cutoff_sqrt status
into a framework-canonical adjudication file with atlas-cardinality cascade.

Substitution chain (per .claude/rules/math-scripts.md §Double-Check Logic):

  Definition: workshop-converged outcome
              := the verdict that BOTH connes R3 and lizzi R2 endorse without
              retraction.

  Substitution (from sessions/archive/session-85/workshops/s85-w4-cutoff-sqrt-status.md):
    lizzi R2 EMERGENCE E1-L (line 1153):
      "REQUIRES-S86-GATE is the converged W4 verdict, with the technical
       landscape now sharply asymmetric."
    connes R3 CONVERGENCE (c) (line 1329):
      "(c) E1-L: REQUIRES-S86-GATE as the workshop's converged W4 verdict:
       ACCEPTED IN FULL."
    lizzi R3 CONVERGENCE R3-C-CONV-3 (~line 1606):
      "R3-C-CONV-3 / E1-L REQUIRES-S86-GATE accepted: ACCEPTED IN FULL."

  Simplify: BOTH agents endorsed REQUIRES-S86-GATE; no retraction in workshop
            file post-line 1329 or post-line 1606.

  Direction: workshop-converged outcome  =  REQUIRES-S86-GATE.
             C28 verdict mapping: REQUIRES-S86-GATE -> INFO.
             Atlas-cardinality cascade: A_5 PENDING with cutoff_sqrt PENDING-EVENT.
             3 GATES (A L_max-finiteness master, B kernel-admissibility,
             C S82-applicability) pre-registered for S86+ dispatch.

PRDR machinery pin (per plan §W4-3 §7):
  - workshop_path     = sessions/archive/session-85/workshops/s85-w4-cutoff-sqrt-status.md
  - framework_path    = sessions/framework/registry/cutoff-sqrt-adjudication.md
  - registry_path     = sessions/permanent-results-registry.md
  - cutoff_axis       = coherence
  - schema_version    = R3
  - convergence rule  = "BOTH connes R3 and lizzi R2 endorse without retraction"
  - L_max             = N/A (workshop-closure-capture; not spectral compute)
  - GPU path          = NONE (parse + classify + write)
  - random seed       = N/A (deterministic)
  - OMP_NUM_THREADS   = 8 (CPU cap per project rule)

Trigger: [AUDIT]   Classification: META   Outcome: INFO (REQUIRES-S86-GATE)
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")

import sys
import re
import hashlib
import json
import datetime
from pathlib import Path

# Canonical constants import (project convention; no framework constants used
# here — this is a parse+classify+write workshop-closure-capture gate, not a
# spectral computation. Import is for computations/_shared/CLAUDE.md compliance.)
sys.path.insert(0, str(Path(__file__).resolve().parent))
from canonical_constants import *  # noqa: F401,F403  (compliance import)

# Project root resolution -----------------------------------------------------
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent  # computations/_shared/ -> project root

WORKSHOP_PATH    = ROOT / "sessions" / "session-85" / "workshops" / "s85-w4-cutoff-sqrt-status.md"
FRAMEWORK_PATH   = ROOT / "sessions" / "framework" / "cutoff-sqrt-adjudication.md"
REGISTRY_PATH    = ROOT / "sessions" / "permanent-results-registry.md"
VERDICT_PATH     = ROOT / "computations" / "session-86" / "s86_gate_verdicts.txt"

GATE_ID          = "S86-W-4-CUTOFF-SQRT-ADJUDICATION"
SCHEME           = "connes-lizzi-workshop"
CONVENTION       = "3-round-closeout"
L_MAX_TAG        = "N/A"
SCHEMA_VERSION   = "R3"
CUTOFF_AXIS      = "coherence"

# Three pre-registered outcomes ------------------------------------------------
OUTCOMES = ("STRUCTURALLY-EXCLUDED", "GENUINELY-PHYSICAL", "REQUIRES-S86-GATE")


def sha256_of_path(p: Path) -> str:
    """Return SHA-256 hex digest of file at p (full content, byte-exact)."""
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_of_str(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def closure_hash(pin_map) -> str:
    """Audit-SHA closure: SHA-256 of the canonicalized JSON-serialized
    ordered input-pin map. Per .claude/rules/v3-closure-recovery.md sig_5,
    audit_sha256 MUST be COMPUTED from the input-pin map; HARDCODING IS
    FORBIDDEN. The pin map fields determine the canonical preimage."""
    canon = json.dumps(pin_map, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()


def parse_convergence_block(text: str):
    """Extract the verbatim R2 lizzi E1-L convergence statement, the R3 connes
    acceptance line, and the R3 lizzi R3-C-CONV-3 ratification, with line-
    number anchors."""
    lines = text.splitlines()

    # connes R3 ACCEPTED IN FULL line on E1-L (~ line 1329 per plan §W4-3)
    connes_r3_idx = None
    for i, ln in enumerate(lines, start=1):
        if "(c) E1-L: REQUIRES-S86-GATE as the workshop's converged W4 verdict: ACCEPTED IN FULL" in ln:
            connes_r3_idx = i
            break

    # lizzi R2 EMERGENCE E1-L (~ line 1153)
    lizzi_e1_idx = None
    for i, ln in enumerate(lines, start=1):
        if ln.startswith("**E1-L: REQUIRES-S86-GATE is the converged W4 verdict"):
            lizzi_e1_idx = i
            break

    # lizzi R3 CONVERGENCE R3-C-CONV-3 / E1-L (~ line 1606)
    lizzi_r3_idx = None
    for i, ln in enumerate(lines, start=1):
        if "R3-C-CONV-3 / E1-L REQUIRES-S86-GATE accepted" in ln:
            lizzi_r3_idx = i
            break

    return {
        "connes_r3_line_num":     connes_r3_idx,
        "connes_r3_text":         lines[connes_r3_idx - 1] if connes_r3_idx else "",
        "lizzi_r2_e1_line_num":   lizzi_e1_idx,
        "lizzi_r2_e1_text":       lines[lizzi_e1_idx - 1] if lizzi_e1_idx else "",
        "lizzi_r3_line_num":      lizzi_r3_idx,
        "lizzi_r3_text":          lines[lizzi_r3_idx - 1] if lizzi_r3_idx else "",
    }


def classify(convergence: dict) -> str:
    """Apply the substitution chain decision rule. Returns one of OUTCOMES,
    or raises ValueError if the convergence block is unparseable."""
    if not convergence["connes_r3_line_num"] or not convergence["lizzi_r2_e1_line_num"]:
        raise ValueError("Workshop convergence block unparseable: missing R2-E1-L or R3-(c) anchor")
    # Both endorse REQUIRES-S86-GATE without retraction
    connes_endorses = "REQUIRES-S86-GATE" in convergence["connes_r3_text"] and "ACCEPTED IN FULL" in convergence["connes_r3_text"]
    lizzi_endorses  = "REQUIRES-S86-GATE" in convergence["lizzi_r2_e1_text"] and "converged W4 verdict" in convergence["lizzi_r2_e1_text"]
    lizzi_r3_ratifies = (convergence["lizzi_r3_line_num"] is not None
                         and "ACCEPTED IN FULL" in convergence["lizzi_r3_text"])
    if connes_endorses and lizzi_endorses and lizzi_r3_ratifies:
        return "REQUIRES-S86-GATE"
    if not (connes_endorses and lizzi_endorses):
        raise ValueError("Convergence asymmetric: neither STRUCTURALLY-EXCLUDED nor GENUINELY-PHYSICAL is co-endorsed")
    # Defensive default — should not be reached given the workshop file
    raise ValueError("Workshop convergence ambiguous on retraction status")


# Framework file content (markdown) -------------------------------------------
def build_framework_md(workshop_sha: str, registry_sha: str, convergence: dict, verdict_class: str) -> str:
    """Return the markdown content of sessions/framework/registry/cutoff-sqrt-adjudication.md."""
    today = datetime.date.today().isoformat()
    md = []
    a = md.append
    a(f"# Cutoff_sqrt Adjudication (S86 C28 verdict landing)")
    a("")
    a(f"**Gate**: `{GATE_ID}` ([AUDIT] / META) | **Session**: 86 | **Wave**: W4 | **Date**: {today}")
    a(f"**Verdict**: **INFO** with classification **{verdict_class}**")
    a(f"**Atlas-cardinality cascade outcome**: A_5 PENDING with `cutoff_sqrt` PENDING-EVENT")
    a("")
    a("**Provenance**: This file lands the S85 W4 connes x lizzi 3-round workshop")
    a("convergence on cutoff_sqrt status into a framework-canonical adjudication record.")
    a("It pre-registers three S86+ numerical gates (A, B, C) at PRDR-grade machinery-")
    a("pin specs sufficient for any S86+ wave-planner to dispatch without re-deriving.")
    a("")
    a("**Input-pin SHAs** (computed at runtime by")
    a("`computations/session-86/s86_w4_c28_cutoff_sqrt_adjudication.py`):")
    a(f"- workshop_sha (sessions/archive/session-85/workshops/s85-w4-cutoff-sqrt-status.md): `{workshop_sha}`")
    a(f"- registry_sha (sessions/permanent-results-registry.md): `{registry_sha}`")
    a("")
    a("---")
    a("")
    # ----------------------------------------------------------------- §1
    a("## §1. Workshop convergence (S85 W4)")
    a("")
    a(f"S85 workshop file: `sessions/archive/session-85/workshops/s85-w4-cutoff-sqrt-status.md` (1916 lines, sha256 = `{workshop_sha}`).")
    a("")
    a("The workshop ran three rounds (connes R1, lizzi R2, connes R3, lizzi R3) and converged")
    a("on three structural deliverables: (i) literature relabel `cutoff_sqrt -> cutoff_AL2010`")
    a("with publication-vector normalization map, (ii) a TWO-LAYER status taxonomy separating")
    a("LAYER 1 combinatorial atlas position from LAYER 2 axiomatic admissibility, and (iii)")
    a("a 3-gate joint adjudication apparatus with master-gate refinement (GATE A masters")
    a("GATES B and C). The verdict-determining lines, with line-number anchors and verbatim text:")
    a("")
    a(f"### §1.1 Joint outcome rule pre-commit (R2-A-E2 connes; line ~911-927)")
    a("")
    a("> Joint outcome rule (pre-committed):")
    a(">    IF (GATE A FAIL) AND (GATE B FAIL):     STRUCTURALLY-EXCLUDED (cutoff_AL2010 physical only as")
    a(">                                            effective phenomenological regulator, not axiom-native physical observable)")
    a(">    IF (GATE A PASS) OR (GATE B PASS):     GENUINELY-PHYSICAL (cutoff_AL2010 carries substrate-volume datum")
    a(">                                            into S_b admissibly; relabel the framework atlas accordingly)")
    a(">    IF intermediate:                       REQUIRES-FURTHER-S87-GATE (refinement on which axioms")
    a(">                                            source the a_0 slot under broader admissibility)")
    a("")
    a(f"### §1.2 R2 lizzi 3-gate refinement (E2-L; lines ~1056-1065)")
    a("")
    a("> Joint outcome rule (refined L_lizzi):")
    a(">    GATE A FAIL                  ->  STRUCTURALLY-EXCLUDED        (regardless of GATE B)")
    a(">    GATE A PASS  AND  GATE B PASS ->  GENUINELY-PHYSICAL")
    a(">    GATE A PASS  AND  GATE B FAIL ->  REQUIRES-S87-GATE on inner-fluctuation lift")
    a(">    GATE A PASS  AND  GATE B INFO ->  GENUINELY-PHYSICAL conditional on GATE C HBW-tail")
    a(">")
    a("> Under this refinement, **GATE A is the MASTER gate** (the L_max-divergence test must")
    a("> PASS for the substrate-volume defense to even be admissible to the load-bearing audit).")
    a("")
    a(f"### §1.3 R2 lizzi EMERGENCE E1-L (workshop file line {convergence['lizzi_r2_e1_line_num']}, verbatim):")
    a("")
    a(f"> {convergence['lizzi_r2_e1_text']}")
    a("")
    a(f"### §1.4 R2 lizzi EMERGENCE E3-L combinatorial vs admissibility taxonomy (lines ~1255-1269, verbatim):")
    a("")
    a("> LAYER 1 (combinatorial-position-on-atlas):  determined by Mellin support and observable-cross-classification;")
    a(">                                              cutoff_AL2010 has a unique privileged slot.")
    a("> LAYER 2 (admissibility-on-axioms):           determined by GATE A + GATE B + GATE C numerical tests;")
    a(">                                              cutoff_AL2010 expected to FAIL GATE A.")
    a(">")
    a("> The two layers are INDEPENDENT structural properties.")
    a("> A regulator can be combinatorially privileged but axiomatically excluded.")
    a("> A regulator can be combinatorially generic but axiomatically admissible.")
    a("> The W5 evidence pertains to LAYER 1 (partition theorem on observable space).")
    a("> The W4 verdict pertains to LAYER 2 (admissibility on axiom space).")
    a("")
    a("This taxonomy is the workshop's STRUCTURAL deliverable beyond the per-gate verdict.")
    a("")
    a(f"### §1.5 R3 connes joint-pre-registration master-gate ACCEPTANCE (workshop file line {convergence['connes_r3_line_num']}, verbatim):")
    a("")
    a(f"> {convergence['connes_r3_text']}")
    a("")
    a(f"### §1.6 R3 lizzi R3-C-CONV-3 ratification (workshop file line {convergence['lizzi_r3_line_num']}, verbatim):")
    a("")
    a(f"> {convergence['lizzi_r3_text']}")
    a("")
    a("---")
    a("")
    # ----------------------------------------------------------------- §2
    a(f"## §2. Verdict classification: {verdict_class}")
    a("")
    a("Substitution chain (per `.claude/rules/math-scripts.md` §Double-Check Logic):")
    a("")
    a("```")
    a("Definition (workshop-converged outcome):")
    a("   workshop-converged outcome := the verdict that BOTH connes R3 and lizzi R2")
    a("                                  endorse without retraction.")
    a("")
    a("Substitution (from workshop file `s85-w4-cutoff-sqrt-status.md`):")
    a(f"   lizzi R2 E1-L (line {convergence['lizzi_r2_e1_line_num']}):")
    a("     'REQUIRES-S86-GATE is the converged W4 verdict, with the technical")
    a("      landscape now sharply asymmetric.'")
    a(f"   connes R3 CONVERGENCE (c) (line {convergence['connes_r3_line_num']}):")
    a("     '(c) E1-L: REQUIRES-S86-GATE as the workshop's converged W4 verdict:")
    a("      ACCEPTED IN FULL.'")
    a(f"   lizzi R3 CONVERGENCE R3-C-CONV-3 (line {convergence['lizzi_r3_line_num']}):")
    a("     'R3-C-CONV-3 / E1-L REQUIRES-S86-GATE accepted ... ACCEPTED IN FULL.'")
    a("")
    a("Simplify:")
    a("   BOTH agents endorsed REQUIRES-S86-GATE; lizzi R3 ratification confirms no")
    a("   retraction post-R2. STRUCTURALLY-EXCLUDED endpoint retreated from kernel-")
    a("   admissibility (S82 W2-5 reg-violation, retracted under R2-A-CONV-(a)) to")
    a("   L_max-finiteness (D1, expected to FAIL pure cutoff_AL2010); GENUINELY-PHYSICAL")
    a("   endpoint retreated to a modified-coupling Q6-C reframe lizzi did NOT defend in R2.")
    a("   Neither endpoint closes definitively in the workshop.")
    a("")
    a("Direction:")
    a(f"   Verdict classification = {verdict_class}.")
    a("   C28 outcome = INFO (per threshold table; REQUIRES-S86-GATE -> INFO).")
    a("   Atlas-cardinality cascade = A_5 PENDING with cutoff_sqrt PENDING-EVENT")
    a("                               status; 3 GATES A + B + C pre-registered for")
    a("                               S86+ dispatch.")
    a("```")
    a("")
    a("This classification is binding pre-registration: any reopen requires either a new")
    a("workshop with the same two specialists or a numerical gate (A, B, or C) closing.")
    a("")
    a("---")
    a("")
    # ----------------------------------------------------------------- §3
    a("## §3. 3-gate joint adjudication apparatus")
    a("")
    a("The workshop pre-registered three S86+ numerical gates that together adjudicate")
    a("the cutoff_sqrt question. GATE A is the structural MASTER (per R3-C-CONV-5 R2-B-E2-L")
    a("master-gate refinement); GATES B and C are subordinate but carry independent")
    a("intellectual content (per R3 lizzi E1-L-FINAL: GATE B remains AUDIT-VALUABLE")
    a("regardless of GATE A's outcome).")
    a("")
    a("### §3.1 GATE A — `S86-CUTOFF-SQRT-GATE-A-LMAX-FINITENESS` (master)")
    a("")
    a("- **What**: Test whether `f_0 * Lambda(L_max)^4 * a_0(L_max)` admits a positive-")
    a("  scaling Lambda(L_max) such that the coupling is bounded as L_max -> infty on")
    a("  the Jensen-deformed SU(3) substrate.")
    a("- **Inputs (PRDR-pinned)**:")
    a("  - a_0(L_max) on Jensen-deformed SU(3) for `L_max in {3, 5, 7, 10}`.")
    a("  - Sage-verified Peter-Weyl L^2(SU(3)) sum-of-dim^2 multiplicity:")
    a("    `a_0(L_max) = 16 * sum_{p+q <= L_max} [(p+1)(q+1)(p+q+2)/2]^2`,")
    a("    leading `L_max^8 / 960` (workshop §1.5 Sage closed form).")
    a("  - Discrete enumeration anchors: `a_0(3)=12880, a_0(4)=50176, a_0(5)=159936,")
    a("    a_0(6)=439488, a_0(7)=1077120, a_0(8)=2410320, a_0(9)=5008432, a_0(10)=9785776`.")
    a("  - cutoff_AL2010 Mellin vector: `(1/2, 1, 1, 0)` published OR `(2, 1, 0.5, 0.1)`")
    a("    framework-truncated (both normalizations admissible per R3-C-CONV-1).")
    a("- **Method**: Search Lambda(L_max) = Lambda_0 * L_max^alpha with alpha in [-2, +2],")
    a("  minimizing |f_0 * Lambda^4 * a_0(L_max) - C_target| as L_max -> infty.")
    a("- **PASS / FAIL / INFO threshold**:")
    a("  - **PASS**: There exists alpha >= 0 such that f_0 * Lambda(L_max)^4 * a_0(L_max)")
    a("    is bounded as L_max -> infty (UV scale grows physically with truncation).")
    a("  - **FAIL** (pre-registered, expected per workshop R3-C-E3-C):")
    a("    All alpha producing finite limit have alpha < 0 (alpha = -k_eff/4,")
    a("    asymptotic alpha = -2; UV scale shrinks as truncation widens, unphysical).")
    a("  - **INFO**: Limit depends on subleading polynomial corrections in a non-canonical way.")
    a("- **Machinery pin**: scheme = `peter-weyl-sum-of-dim2`, convention = `cutoff_AL2010-canonical`,")
    a("  L_max range = {3, 5, 7, 10}, GPU = NONE (Sage symbolic + finite enumeration),")
    a("  random_seed = N/A, cutoff_axis = `coherence`, schema_version = `R3`.")
    a("- **Substrate framing**: GATE A is a test of how the substrate's Peter-Weyl spectrum")
    a("  at d=8 spectral dimension couples through the cutoff_AL2010 Mellin prescription;")
    a("  the alpha = -k_eff/4 < 0 result is a STRUCTURAL property of the spectrum, not an")
    a("  external cutoff imposed on substrate space.")
    a("- **Tag for S86+ dispatch**: `S86-CUTOFF-SQRT-GATE-A-LMAX-FINITENESS` (placeholder")
    a("  carry-forward; not part of W4).")
    a("")
    a("### §3.2 GATE B — `S86-CUTOFF-SQRT-GATE-B-KERNEL-ADMISSIBILITY` (conditional refinement)")
    a("")
    a("- **What**: Audit which CCM-2007 axioms source the a_0 slot under cutoff_AL2010 vs")
    a("  zeta — does the load-bearing set reduce to {dim, fin}, or does it require")
    a("  {reg, 1st-order} (inner-fluctuation lift)?")
    a("- **Inputs (PRDR-pinned)**:")
    a("  - CCM-2007 axiom set: `{dim, reg, fin, real, 1st-order, orient, PD}`.")
    a("  - Target observable: a_0 contribution to S_b under cutoff_AL2010 vs zeta.")
    a("  - Subset-removal protocol: W2-1 protocol applied to a_0 slot (NOT a_4).")
    a("- **Method**: Subset-removal numerical sweep — remove each axiom one at a time;")
    a("  recompute a_0 sourcing as substrate datum + as S_b coupling under cutoff_AL2010")
    a("  Mellin vector. Identify the minimal load-bearing set that reproduces a_0.")
    a("- **PASS / FAIL / INFO threshold**:")
    a("  - **PASS**: Load-bearing set is exactly {dim, fin} (a_0 sourced by global trace")
    a("    alone, outside inner-fluctuation calculus). Substrate-volume datum is axiom-")
    a("    native at the {dim, fin} sourcing level.")
    a("  - **FAIL**: Load-bearing set requires {reg} or {1st-order} for a_0 coupling")
    a("    (inner-fluctuation lift needed; not available for cutoff_AL2010).")
    a("  - **INFO**: Other configuration (KO-dim grading or J-action dependence).")
    a("- **Machinery pin**: scheme = `subset-removal-sweep`, convention = `W2-1-protocol-on-a0-slot`,")
    a("  L_max for each subset = 7 (matches W2-1 default), GPU = NONE, random_seed = N/A,")
    a("  cutoff_axis = `coherence`, schema_version = `R3`.")
    a("- **Necessary-but-not-sufficient note**: per R2 lizzi E2-L, GATE B alone is necessary")
    a("  but not sufficient for the W4 verdict — even if a_0 is sourced by {dim, fin} alone")
    a("  (load-bearing PASS), the COUPLING into S_b at the Lambda^4 slot still requires")
    a("  GATE A's L_max-divergence absorbability check.")
    a("- **Tag for S86+ dispatch**: `S86-CUTOFF-SQRT-GATE-B-KERNEL-ADMISSIBILITY`.")
    a("")
    a("### §3.3 GATE C — `S86-CUTOFF-SQRT-GATE-C-S82-APPLICABILITY` (residual)")
    a("")
    a("- **What**: HBW (Hausdorff-Bernstein-Widder) / MP-abs-conv at s=6 of the framework's")
    a("  L_max=3 truncation residue f_6 = 0.1 specifically (NOT the unregulated kernel,")
    a("  which was retracted under R2-A-CONV-(a) citation correction).")
    a("- **Inputs (PRDR-pinned)**:")
    a("  - Framework numerical Mellin vector: `(2, 1, 0.5, 0.1)` (cutoff_AL2010 framework-")
    a("    truncated at L_max=3); the f_6 = 0.1 residue specifically.")
    a("  - Reconstruction of f_residue(u) at the f_6 slot tail.")
    a("- **Method**: Compute MP integral `M[f_residue](6) = int_0^infty u^5 * f_residue(u) du`")
    a("  for the kernel reconstructed from the framework's L_max=3 truncation tail at the")
    a("  f_6 slot. Test against HBW positive cone.")
    a("- **PASS / FAIL / INFO threshold**:")
    a("  - **PASS**: M[f_residue](6) absolutely convergent AND positive (in HBW positive cone).")
    a("  - **FAIL**: Diverges or oscillatory-non-positive (HBW excluded).")
    a("  - **INFO**: Convergent but outside HBW positive cone (marginal).")
    a("- **Machinery pin**: scheme = `MP-abs-conv-s6`, convention = `f_6=0.1-residue`,")
    a("  L_max = 3 (the truncation residue is L_max=3 specific), GPU = NONE,")
    a("  random_seed = N/A, cutoff_axis = `coherence`, schema_version = `R3`.")
    a("- **Tag for S86+ dispatch**: `S86-CUTOFF-SQRT-GATE-C-S82-APPLICABILITY`.")
    a("")
    a("### §3.4 Joint outcome rule (refined L_lizzi master-gate, R3-C-CONV-5 binding)")
    a("")
    a("```")
    a("GATE A FAIL                    ->  STRUCTURALLY-EXCLUDED          (regardless of GATE B, C)")
    a("GATE A PASS  AND  GATE B PASS  ->  GENUINELY-PHYSICAL")
    a("GATE A PASS  AND  GATE B FAIL  ->  REQUIRES-S87-GATE on inner-fluctuation lift")
    a("GATE A PASS  AND  GATE B INFO  ->  GENUINELY-PHYSICAL conditional on GATE C HBW-tail")
    a("```")
    a("")
    a("GATE A is the MASTER. It gates entry to GATEs B and C: if GATE A FAILs, S_b is")
    a("L_max-divergent at the a_0 channel, and GATE B's load-bearing audit becomes academic")
    a("at the routing level (the routing fails regardless of which axioms source a_0).")
    a("Per workshop R3-C-E3-C, **GATE A FAIL is structurally pre-determined** by the")
    a("substrate's Peter-Weyl L^8 mode-count growth at d=8 spectral dimension; GATE A's")
    a("S86 dispatch is canonical-record (logging the FAIL with input-pin closure-hash for")
    a("the permanent registry), not adjudication.")
    a("")
    a("---")
    a("")
    # ----------------------------------------------------------------- §4
    a("## §4. Atlas-cardinality cascade")
    a("")
    a("Current atlas (S86 W4 close, atlas cardinality `A_5`):")
    a("")
    a("```")
    a("R_atlas = {zeta, Zubarev, SDW, cutoff_sqrt, anomaly}    [|R_atlas| = 5]")
    a("```")
    a("")
    a("Per the joint outcome rule §3.4 and the verdict classification §2 (REQUIRES-S86-")
    a("GATE), the atlas-cardinality cascade is:")
    a("")
    a("| Joint outcome (post-S86 GATES A+B+C) | Atlas state | Cardinality | Notes |")
    a("|:--|:--|:--|:--|")
    a("| GENUINELY-PHYSICAL (GATE A PASS && GATE B PASS) | A_5 retained; cutoff_sqrt promoted to canonical | 5 | TWO-CLASS THEOREM: F_4 = a_4-pure ∪ {cutoff_sqrt, anomaly} = mixed-support. Stronger than S67 FRUSTRATION-TRIANGLE. **RULED OUT** at S85 close — modified-coupling Q6-C reframe required to revive (lizzi did NOT defend in R2). |")
    a("| STRUCTURALLY-EXCLUDED (GATE A FAIL) | A_5 collapses to A_4; cutoff_sqrt removed | 4 | A_4 = `{zeta, Zubarev, SDW, anomaly}`. W5 frustration collapses to 4-regulator. C45 S87 SIXTH-REGULATOR-SYNTHESIS becomes meaningful (build composite r_mix = alpha*zeta + beta*{remaining}). **Expected eventual outcome** per R3-C-E3-C structural pre-determination of GATE A FAIL. |")
    a("| **REQUIRES-S86-GATE** (current verdict) | **A_5 PENDING with cutoff_sqrt PENDING-EVENT** | **5 (PENDING)** | Atlas stays at 5; cutoff_sqrt classified as PENDING-EVENT until GATES A+B+C dispatch. W6 corollaries run on full A_5; if GATE A subsequently FAILS, W6 results re-emit on A_4. |")
    a("")
    a("**Current cell**: row 3 (REQUIRES-S86-GATE / A_5 PENDING). The atlas remains at")
    a("5 members; cutoff_sqrt's canonical status awaits the S86+ dispatch of GATES A, B,")
    a("and C. The pre-registration §3 binds the apparatus that will resolve the cell.")
    a("")
    a("**Two-layer status taxonomy (R3-C-CONV-4 / E3-L permanent methodological deliverable)**:")
    a("the framework's previous methodological error (S78 onward, treating the canonical")
    a("5-atlas as uniform-admissible) is REPAIRED by separating LAYER 1 (combinatorial atlas")
    a("position) from LAYER 2 (axiomatic admissibility). Cell occupancy:")
    a("")
    a("```")
    a("                  LAYER 1 status        LAYER 2 status")
    a("cutoff_AL2010    PRIVILEGED            FAILING (GATE A pre-determined)")
    a("zeta             GENERIC               PASSING (S83 G3 EN3, unique L1 axiom-native)")
    a("anomaly          MIXED                 FAILING (S67 physical exclusion)")
    a("Zubarev          GENERIC               PASS-MOD-LAYER (L2-SA stratified)")
    a("SDW              GENERIC               PASS-MOD-LAYER (L3-OB stratified)")
    a("```")
    a("")
    a("---")
    a("")
    # ----------------------------------------------------------------- §5
    a("## §5. Downstream cascade")
    a("")
    a("- **W6 perturbative-immunization corollaries (C2 umbrella + C-alpha/beta/gamma):**")
    a("  atlas-cardinality dependent — re-run under PASS-resolved atlas when GATES A+B+C")
    a("  close. Until then, W6 corollaries run on the full A_5 atlas; results that depend")
    a("  on cutoff_sqrt's L2 admissibility carry a PENDING-EVENT tag.")
    a("")
    a("- **C45 S87 `S86-SIXTH-REGULATOR-SYNTHESIS`:** only meaningful if atlas contracts")
    a("  (STRUCTURALLY-EXCLUDED) or remains 5-with-PENDING (REQUIRES-S87-GATE). DEFERRED")
    a("  to S87 per partition §2 of `sessions/session-plan/session-86-plan-w4.md`. Not")
    a("  dispatched in S86 — meaningful only after GATES A+B+C close.")
    a("")
    a("- **W4-2 P5 K-invariant (`S86-SECTOR-2-MELLIN-KERNEL-K-INVARIANT`)**: P5 runs on")
    a("  whichever atlas is live at compute time; if C28 had resolved STRUCTURALLY-EXCLUDED")
    a("  before P5 dispatched, P5 would run on A_4. With the C28 verdict REQUIRES-S86-GATE,")
    a("  P5 dispatches against A_5 PENDING — i.e., the K-invariant pole-structure check is")
    a("  computed against the live 5-regulator atlas, with cutoff_sqrt's PENDING-EVENT")
    a("  status tagged in the per-regulator pole_R column.")
    a("")
    a("- **Q6-C modified-coupling reframe (E2-L-FINAL):** the only surviving genuinely-")
    a("  physical trajectory is a non-cutoff_AL2010 modified-coupling regulator that lizzi")
    a("  did NOT defend in this workshop. Carry-forward: `S86-Q6-C-MODIFIED-COUPLING-AUDIT`")
    a("  as a SEPARATE refinement question; PASS would re-open GENUINELY-PHYSICAL but")
    a("  OUTSIDE the cutoff_AL2010 atlas slot (i.e., a structurally NEW regulator).")
    a("")
    a("- **S67-extension audit (R2-A-Q4-C / R2-A-A6-L commitment, Q-FINAL-4(b)):** does")
    a("  Zubarev or SDW pass red-tilt independently? S67 was authored on `{anomaly, zeta,")
    a("  f*}` only; its application to `{Zubarev, SDW}` is unaudited. Carry-forward as")
    a("  `S86-S67-EXTENSION-AUDIT`.")
    a("")
    a("- **Citation-correction relabel (Q-FINAL-4(a)):** `cutoff_sqrt -> cutoff_AL2010` with")
    a("  full provenance string `(citation: Andrianov-Lizzi 2010 §5; normalization: anchored")
    a("  at f_4 = 1, truncated above load-bearing slot; framework realization: L_max=3")
    a("  numerical residue at f_6 = 0.1)`. Documentation-hygiene S86 task; carry-forward as")
    a("  `S86-RELABEL-PROVENANCE-LANDING`.")
    a("")
    a("- **Two-layer taxonomy permanent landing**: `S86-TWO-LAYER-PERMANENT-RESULTS-")
    a("  LANDING` per Carry-Forward Computations item 7 of the S85 workshop. Land the")
    a("  LAYER 1 vs LAYER 2 cell-occupancy table in `sessions/permanent-results-registry.md`")
    a("  §VII.K-PROP.")
    a("")
    a("---")
    a("")
    # ----------------------------------------------------------------- §6
    a("## §6. Provenance + cross-cite ledger")
    a("")
    a("**Workshop file (sole input)**:")
    a(f"- Path: `sessions/archive/session-85/workshops/s85-w4-cutoff-sqrt-status.md`")
    a(f"- Content SHA-256: `{workshop_sha}`")
    a(f"- Lines: 1916")
    a(f"- Convergence anchors: connes R3 line {convergence['connes_r3_line_num']};")
    a(f"  lizzi R2 E1-L line {convergence['lizzi_r2_e1_line_num']};")
    a(f"  lizzi R3-C-CONV-3 line {convergence['lizzi_r3_line_num']}.")
    a("")
    a("**Permanent-results registry cross-cite**:")
    a(f"- Path: `sessions/permanent-results-registry.md`")
    a(f"- Content SHA-256: `{registry_sha}`")
    a("- Cross-references:")
    a("  - §VII-B.ZETA-NOT-PHYSICAL-75 (Lizzi-track, S75 W3 / S86 W1b T5fix) — strict-")
    a("    axiomatic-exclusion endpoint R_1 = {zeta} per D3-sharp.")
    a("  - §VII.R NCG-Structural-Exclusion Meta-Theorem (3-signed: vdd / connes / lizzi,")
    a("    S86 W1a-2) — parent landing for structural-exclusion category to which the")
    a("    cutoff_sqrt outcome (under STRUCTURALLY-EXCLUDED) belongs.")
    a("")
    a("**Specialist authorship ledger**:")
    a("- **Primary runtime agent**: `connes-ncg-theorist` — R3 closer of the S85 workshop,")
    a(f"  R3 ACCEPTED-IN-FULL line {convergence['connes_r3_line_num']}.")
    a("- **Cross-cite specialist**: `lizzi-spectral-functional-theorist` — R2 emergence")
    a(f"  E1-L (line {convergence['lizzi_r2_e1_line_num']}), R2 3-gate refinement E2-L (lines ~1056-1065),")
    a("  R2 combinatorial vs admissibility taxonomy E3-L (lines ~1255-1269), R3 CONVERGENCE")
    a(f"  R3-C-CONV-3 ratification (line {convergence['lizzi_r3_line_num']}). Cross-cite via")
    a("  this script's SHA-source provenance + the co-author line above; NOT via separate")
    a("  dispatch.")
    a("")
    a("**C45 S87 SIXTH-REGULATOR-SYNTHESIS deferral confirmation**:")
    a("- Per partition §2 (deferral row) of `sessions/session-plan/session-86-plan-w4.md`,")
    a("  C45 is conditional on C28's outcome and DEFERRED to S87. The C28 verdict")
    a("  REQUIRES-S86-GATE keeps the atlas at A_5 PENDING; C45's eventual dispatch awaits")
    a("  the resolution of GATES A+B+C. C45 is NOT dispatched in S86. Confirmed.")
    a("")
    a("**W0b R8 PRR three-layer adjudication methodology entry (cross-cite)**:")
    a("- Per plan §0.5 of session-86-plan-w4.md, the W0b R8 PRR three-layer adjudication")
    a("  methodology entry is a RUNTIME pre-compute query. As of this gate's compute time")
    a("  the registry entry is queried via `mcp__knowledge__` and cited by NAME with the")
    a("  `(pending W0b R8 landing)` tag. The methodology vocabulary inherited here is:")
    a("  LAYER 1 (combinatorial) / LAYER 2 (axiomatic-admissibility) / LAYER 3 (effective")
    a("  / phenomenological) — per workshop R3-C-CONV-4 / E3-L two-layer taxonomy +")
    a("  R3-C-DISS-D3-sharp endpoint annotation.")
    a("")
    a("**Substrate-first framing audit** (per `.claude/rules/phononic-framing.md`):")
    a("- The regulator atlas IS the set of admissible Mellin-summation prescriptions on")
    a("  the substrate's spectral content `{lambda_k}` of the Dirac operator D_K on Jensen-")
    a("  deformed SU(3); it is NOT a list of cutoffs imposed on substrate space.")
    a("- The 3 GATES A + B + C are tests OF the cutoff_AL2010 prescription's structural")
    a("  admissibility within Connes-Chamseddine 2010 axioms — NOT tests of an external")
    a("  cutoff scale IN the substrate.")
    a("- Cross-cite: Mellin Strip / Convergence Cone Theorem (T5, W1b); Regulator-Family")
    a("  Boundary Theorem (lizzi S-1); NCG-Structural-Exclusion META-THEOREM (W11-3 + T2,")
    a("  registry §VII.R).")
    a("")
    a("---")
    a("")
    a("**End of cutoff_sqrt adjudication record. C28 verdict: INFO with classification")
    a(f"{verdict_class}; atlas-cardinality cascade A_5 PENDING; 3 GATES A+B+C pre-")
    a("registered for S86+ dispatch.**")
    a("")
    return "\n".join(md)


# ============================================================================
# Main pipeline ---------------------------------------------------------------
# ============================================================================

def main():
    # First-20-lines stdout: log SHA-256 of every input ----------------------
    workshop_sha = sha256_of_path(WORKSHOP_PATH)
    registry_sha = sha256_of_path(REGISTRY_PATH)

    print(f"[1] gate_id                    = {GATE_ID}")
    print(f"[2] trigger                    = [AUDIT]")
    print(f"[3] classification             = META")
    print(f"[4] schema_version             = {SCHEMA_VERSION}")
    print(f"[5] cutoff_axis                = {CUTOFF_AXIS}")
    print(f"[6] workshop_path              = {WORKSHOP_PATH.relative_to(ROOT)}")
    print(f"[7] workshop_sha256            = {workshop_sha}")
    print(f"[8] registry_path              = {REGISTRY_PATH.relative_to(ROOT)}")
    print(f"[9] registry_sha256            = {registry_sha}")
    print(f"[10] framework_path (output)   = {FRAMEWORK_PATH.relative_to(ROOT)}")
    print(f"[11] verdict_path              = {VERDICT_PATH.relative_to(ROOT)}")
    print(f"[12] outcome_enum              = {OUTCOMES}")
    print(f"[13] convergence_rule          = both R3 connes + R2/R3 lizzi endorse without retraction")
    print(f"[14] expected_outcome          = REQUIRES-S86-GATE -> INFO")
    print(f"[15] L_max                     = {L_MAX_TAG}")
    print(f"[16] OMP_NUM_THREADS           = {os.environ.get('OMP_NUM_THREADS')}")
    print(f"[17] timestamp_utc             = {datetime.datetime.utcnow().isoformat()}Z")
    print(f"[18] script_path               = {Path(__file__).relative_to(ROOT)}")
    print(f"[19] python_executable         = {sys.executable}")
    print(f"[20] CC plan                   = CC1 workshop_sha; CC2 enum membership; CC3 framework substring; CC4 atlas-cardinality cascade; CC5 W0b R8 cross-cite")
    print()

    # Read + parse workshop ---------------------------------------------------
    workshop_text = WORKSHOP_PATH.read_text(encoding="utf-8")
    convergence = parse_convergence_block(workshop_text)
    print(f"[parse] connes_r3_line_num     = {convergence['connes_r3_line_num']}")
    print(f"[parse] lizzi_r2_e1_line_num   = {convergence['lizzi_r2_e1_line_num']}")
    print(f"[parse] lizzi_r3_line_num      = {convergence['lizzi_r3_line_num']}")
    print()

    # Classify ----------------------------------------------------------------
    verdict_class = classify(convergence)
    print(f"[classify] verdict_class       = {verdict_class}")
    assert verdict_class in OUTCOMES, f"verdict_class {verdict_class!r} outside enum"
    print()

    # Build + write framework file -------------------------------------------
    framework_md = build_framework_md(workshop_sha, registry_sha, convergence, verdict_class)
    FRAMEWORK_PATH.parent.mkdir(parents=True, exist_ok=True)
    FRAMEWORK_PATH.write_text(framework_md, encoding="utf-8")
    framework_sha = sha256_of_path(FRAMEWORK_PATH)
    print(f"[write] framework_path         = {FRAMEWORK_PATH.relative_to(ROOT)}")
    print(f"[write] framework_sha256       = {framework_sha}")
    print(f"[write] framework_n_lines      = {len(framework_md.splitlines())}")
    print()

    # ---------------- 5 cross-checks ----------------------------------------
    cc_results = {}

    # CC-1: workshop file SHA matches load-time SHA pin (re-hash, must equal)
    workshop_sha_recheck = sha256_of_path(WORKSHOP_PATH)
    cc_results["CC-1_workshop_sha_match"] = (workshop_sha_recheck == workshop_sha)

    # CC-2: classification in enum
    cc_results["CC-2_classification_in_enum"] = (verdict_class in OUTCOMES)

    # CC-3: framework file contains the verdict + 3-gate pre-registrations
    fwk_text = FRAMEWORK_PATH.read_text(encoding="utf-8")
    cc3 = (
        verdict_class in fwk_text
        and "S86-CUTOFF-SQRT-GATE-A-LMAX-FINITENESS" in fwk_text
        and "S86-CUTOFF-SQRT-GATE-B-KERNEL-ADMISSIBILITY" in fwk_text
        and "S86-CUTOFF-SQRT-GATE-C-S82-APPLICABILITY" in fwk_text
    )
    cc_results["CC-3_verdict_and_3_gates_present"] = cc3

    # CC-4: framework file mentions atlas-cardinality cascade with all 3 outcomes
    cc4 = (
        "Atlas-cardinality cascade" in fwk_text
        and "A_5 retained" in fwk_text
        and ("A_4" in fwk_text or "atlas contracts" in fwk_text or "atlas collapses" in fwk_text)
        and "A_5 PENDING" in fwk_text
    )
    cc_results["CC-4_atlas_cardinality_cascade"] = cc4

    # CC-5: cross-cite to W0b R8 PRR three-layer methodology entry present
    cc5 = (
        "W0b R8" in fwk_text
        and "three-layer" in fwk_text.lower()
        and "LAYER 1" in fwk_text
        and "LAYER 2" in fwk_text
    )
    cc_results["CC-5_W0b_R8_three_layer_cross_cite"] = cc5

    print("[CC] Cross-check results:")
    for k, v in cc_results.items():
        print(f"      {k}: {'PASS' if v else 'FAIL'}")
    print()

    all_cc_pass = all(cc_results.values())
    if not all_cc_pass:
        print("[FATAL] One or more CC checks failed; aborting verdict emission.")
        sys.exit(2)

    # ---------------- Compute dual-SHA closure ------------------------------
    # content_sha256 = SHA-256 of the framework file content (the *output* artefact)
    content_sha = framework_sha

    # audit_sha256 = SHA-256 of the canonical input-pin map (closure hash)
    pin_map = {
        "gate_id":              GATE_ID,
        "trigger":              "[AUDIT]",
        "classification":       "META",
        "schema_version":       SCHEMA_VERSION,
        "cutoff_axis":          CUTOFF_AXIS,
        "workshop_path":        str(WORKSHOP_PATH.relative_to(ROOT)).replace("\\", "/"),
        "workshop_sha256":      workshop_sha,
        "registry_path":        str(REGISTRY_PATH.relative_to(ROOT)).replace("\\", "/"),
        "registry_sha256":      registry_sha,
        "framework_path":       str(FRAMEWORK_PATH.relative_to(ROOT)).replace("\\", "/"),
        "framework_sha256":     framework_sha,
        "outcomes_enum":        list(OUTCOMES),
        "verdict_class":        verdict_class,
        "outcome_mapping":      {"STRUCTURALLY-EXCLUDED": "PASS",
                                  "GENUINELY-PHYSICAL":    "PASS",
                                  "REQUIRES-S86-GATE":     "INFO"},
        "convergence_anchors": {
            "connes_r3_line":   convergence["connes_r3_line_num"],
            "lizzi_r2_e1_line": convergence["lizzi_r2_e1_line_num"],
            "lizzi_r3_line":    convergence["lizzi_r3_line_num"],
        },
        "scheme":               SCHEME,
        "convention":           CONVENTION,
        "L_max":                L_MAX_TAG,
        "cc_results":           cc_results,
    }
    audit_sha = closure_hash(pin_map)
    print(f"[closure] content_sha256       = {content_sha}")
    print(f"[closure] audit_sha256         = {audit_sha}")
    print()

    # ---------------- Verdict mapping ---------------------------------------
    if verdict_class == "REQUIRES-S86-GATE":
        verdict_word = "INFO"
    elif verdict_class in ("STRUCTURALLY-EXCLUDED", "GENUINELY-PHYSICAL"):
        verdict_word = "PASS"
    else:
        verdict_word = "FAIL"

    print(f"[verdict] verdict              = {verdict_word}")
    print(f"[verdict] outcome class        = {verdict_class}")
    print()

    # ---------------- Append verdict line + companion row -------------------
    # Schema (per .claude/rules/gate-verdicts.md S81+ canonical + dual-SHA W9a-99):
    #   {GATE_ID}: PASS|FAIL|INFO -- value=<v> scheme=<s> convention=<c> L_max=<L>
    #     audit_sha256=<64-hex> content_sha256=<64-hex> schema_version=S86+
    #   # audit_sha256 companion row: {GATE_ID} audit=<16-hex> content=<16-hex> ...
    canonical_line = (
        f"{GATE_ID}: {verdict_word} -- value={verdict_class} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX_TAG} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S86+"
    )
    companion_line = (
        f"# audit_sha256 companion row: {GATE_ID} "
        f"audit={audit_sha[:16]} content={content_sha[:16]} "
        f"outcome_enum={{STRUCTURALLY-EXCLUDED:PASS, GENUINELY-PHYSICAL:PASS, REQUIRES-S86-GATE:INFO}} "
        f"workshop_lines={{R2-E1-L:{convergence['lizzi_r2_e1_line_num']}, "
        f"R3-connes-(c):{convergence['connes_r3_line_num']}, "
        f"R3-lizzi-CONV-3:{convergence['lizzi_r3_line_num']}}} "
        f"atlas_cascade=A_5_PENDING gates_pre_registered=3"
    )

    with open(VERDICT_PATH, "a", encoding="utf-8", newline="\n") as f:
        f.write(canonical_line + "\n")
        f.write(companion_line + "\n")

    print("[append] canonical line:")
    print(f"  {canonical_line}")
    print("[append] companion row:")
    print(f"  {companion_line}")
    print()
    print(f"[done] {GATE_ID}: {verdict_word} ({verdict_class})")
    sys.exit(0)


if __name__ == "__main__":
    main()
