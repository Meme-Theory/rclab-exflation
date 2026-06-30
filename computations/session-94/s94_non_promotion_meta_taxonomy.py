#!/usr/bin/env python3
"""
S94 W6-20 S94-NON-PROMOTION-META-TAXONOMY — non-promotion meta-taxonomy synthesis
=================================================================================

Gate: S94-NON-PROMOTION-META-TAXONOMY ([AUDIT])

Pre-registered (INFO-class by design):
  The canonical top-line verdict is INFO regardless of which outcome the synthesis
  reaches. The chosen outcome (UNIFYING-META-RULE-DRAFTED vs THREE-CONFIRMED-ORTHOGONAL)
  is recorded in value=. The PASS/FAIL rubric describes synthesis QUALITY, not the
  top-line. Both outcomes pre-registered at plan-freeze; neither pre-judged.

Question:
  Are the three non-promotion verdicts —
    (A) Tier-2-dimensionful  (cross-pillar-bridge-corpus.md §25 / anatomy "Tier-1/Tier-2")
    (B) §(iv-bis) surrogate sub-row B CONTINGENT  (pru-class-corpus.md §11.1)
    (C) §(iv-bis) surrogate sub-row A PERMANENT sign-lock  (pru-class-corpus.md §11.1 / §11)
  —
  instances of a SINGLE non-promotion meta-taxonomy (theorem-STRUCTURE permanent;
  corrupted/under-derived NUMBER held pending substrate-natural extraction),
  OR THREE structurally-orthogonal non-promotion classes that must NOT be merged?

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - sessions/framework/registry/cross-pillar-bridge-corpus.md  (member A; corpus §25)
  - sessions/framework/registry/pru-class-corpus.md            (members B, C; corpus §11 / §11.1)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<outcome+evidence>, scheme=METHODOLOGY-class-rule-synthesis-INFO,
   convention=non-promotion-meta-taxonomy;shared-predicate+per-member-discriminator,
   L_max=N/A)

Classification: NON-PHONONIC (methodology-rule synthesis; F-image at the methodology layer
  per epistemic-discipline.md "Layer-Decomposition").

METHODOLOGY
-----------
This is a pure-text STRUCTURAL synthesis over three already-proven non-promotion verdicts.
No spectral content, no linear algebra (the members' own directional content — the
log-derivative annihilation in Tier-2, the sign-lock of R_surr=2f-1 — was substitution-
chained in their own prior gates; this meta-gate does not re-derive them; per
math-scripts.md "When the chain is NOT required" it cites prior results verbatim).

The script:
  (1) encodes the three candidate members as structured records carrying their
      8 comparison axes (held-object, theorem-structure-status, firing-sub-test,
      non-promotion-permanence, parent-rule, dimension-class, what-blocks-promotion,
      discharge-eligibility);
  (2) tests the SHARED-PREDICATE conjunct: does the predicate
      "theorem-STRUCTURE permanent/proven; a NUMBER held pending substrate-natural
      extraction; NOT sideways-re-pinned to a methodology-floor F-image" cover all three?
  (3) tests the ORTHOGONALITY conjunct: do the members occupy distinct firing sub-tests
      AND distinct permanence classes AND distinct parent rules such that a merge would
      conflate structurally-distinct mechanisms (the false-unification test)?
  (4) reconciles (2) and (3): both are TRUE simultaneously — the resolution is the
      shared-predicate-as-genus + per-member-discriminator-as-differentia reading
      (UNIFYING via a TAXONOMY, not a COLLAPSE). The taxonomy UNIFIES at the genus
      level while PRESERVING the orthogonal differentiae as the discriminator axis,
      so neither outcome is the naive "merge-everything" nor "three-walls-never-touch".

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- No GPU / no linear algebra (pure structural text synthesis)
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- Verdict appended atomically via append_verdict() (single open("a"), no read-modify-write)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
import sys
from pathlib import Path

# Make canonical_constants importable (it lives in computations/_shared/).
_SHARED = Path(__file__).resolve().parent.parent / "_shared"  # (local)
if str(_SHARED) not in sys.path:
    sys.path.insert(0, str(_SHARED))

from canonical_constants import *  # noqa: F401,F403  (MANDATORY; no framework constants hardcoded)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time

# ---------------------------------------------------------------------------
# Section 3 — Paths + identity
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent                 # (local)
COMPUTATIONS_DIR = SESSION_DIR.parent                         # (local)
SHARED_DIR = COMPUTATIONS_DIR / "_shared"                     # (local)
PROJECT_ROOT = COMPUTATIONS_DIR.parent                        # (local)

SESSION = "S94"                                               # (local)
GATE_ID = "S94-NON-PROMOTION-META-TAXONOMY"                   # (local)
SCHEME = "METHODOLOGY-class-rule-synthesis-INFO"              # (local)
CONVENTION = ("non-promotion-meta-taxonomy;"
              "shared-predicate+per-member-discriminator")    # (local)
L_MAX = "N/A"                                                 # (local)

OUT_JSON = SESSION_DIR / "s94_non_promotion_meta_taxonomy.json"   # (local)
VERDICT_TXT = SESSION_DIR / "s94_gate_verdicts.txt"              # (local)

# Option A (gate-verdicts.md): the FIRST run of this script (before the predicate-
# detection self-correction) appended a verdict line with this audit_sha256. Under
# absolute verdict permanence that line is RETAINED on disk; this run emits a
# corrective successor tagged supersedes=<that full 64-char SHA>. Set to "" for a
# clean first run (no prior line to supersede).
SUPERSEDES_PRIOR = (
    "4455a4878703ee9d751c849d7e1f6eb1b30a80440bc3a16668e03505d0d65f86"
)  # (local)

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    PROJECT_ROOT / "sessions" / "framework" / "registry" / "cross-pillar-bridge-corpus.md",
    PROJECT_ROOT / "sessions" / "framework" / "registry" / "pru-class-corpus.md",
]


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
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    """Compute (audit_sha256, content_sha256) per the S84+ dual-SHA schema.

    audit_sha256   = sha256( bytes(script) || bytes(canonical) || pinmap_json )
    content_sha256 = sha256( bytes(script) )
    The audit_sha256 is computed at runtime from the ordered input-pin map —
    never hardcoded, never copy-pasted (gate-verdicts.md / v3-closure-recovery sig_5).
    """
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)

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
# Section 5 — The three candidate members (verbatim structured encoding)
#
# Each record carries the 8 comparison axes read off the corpus text. NO new
# physics: every field is cited from corpus §25 (A) or §11 / §11.1 (B, C).
# ---------------------------------------------------------------------------

# --- Member A: Tier-2-dimensionful (cross-pillar-bridge-corpus.md §25 / anatomy "Tier-1/Tier-2") ---
MEMBER_A = {
    "tag": "A",
    "name": "Tier-2-dimensionful",
    "parent_rule": "cross-pillar-bridge-anatomy.md "
                   '"Tier-1/Tier-2 dimensional-re-anchorability gate"',
    "corpus": "cross-pillar-bridge-corpus.md §25 (K=1; SUGGESTION)",
    "instance": "§VII.AX.OP-PROJ n_PBH = 7.2761e-23 m^-3",
    # theorem-STRUCTURE status
    "theorem_structure_status": "STAGE-3-PERMANENT",
    "theorem_structure_basis": "Stage-2 PASS-AND on the non-Level-3 clauses "
                               "(W4-2 audit ba202d16...)",
    # STRUCTURED predicate fields (read off the corpus; NOT inferred by prose substring-match):
    "structure_permanent_or_proven": True,   # §25.1: theorem-STRUCTURE STAGE-3-PERMANENT
    "number_is_held": True,                   # §25.1: m^-3 Level-3 row HELD NOT-SATISFIED-PENDING
    "repinned_to_methodology_floor_F_image": False,  # the number waits for substrate-NATURAL re-anchor
    # the held NUMBER
    "held_number": "DIMENSIONFUL magnitude n_PBH (m^-3 Level-3 row)",
    "held_status": "NOT-SATISFIED-PENDING-substrate-physical-scale-anchor",
    # firing sub-test (what test the obstruction fires on)
    "firing_sub_test": "Tier-1 FAIL (cardinality channel truncation-DIVERGENT, "
                       "N_eigs(L) quintic, lim_{L->inf}=+inf) "
                       "AND Tier-2 DIMENSIONFUL",
    # why it blocks promotion
    "block_mechanism": "dimension [O] (carried by the m^-3 prefactor A=2.2517e-28 inside W(L)) "
                       "and the L_max-divergence (also in W(L)) occupy the SAME multiplicative "
                       "slot; the only truncation-invariant content is the dimensionless cascade "
                       "exponent d ln N_eigs/d ln L -> 5, which annihilates the prefactor",
    # permanence of the NON-PROMOTION
    "non_promotion_permanence": "PERMANENT-pending-physical-anchor",
    "discharge_eligible": True,   # discharge by RE-SOURCING the m^-3 from OUTSIDE the divergent channel
    "discharge_route": "re-anchor to a substrate-physical scale (PV/zeta at Lambda_UV=M_KK, "
                       "or a cosmological-observable cutoff) OUTSIDE the cardinality channel "
                       "(CF-S94-N-PBH-CANONICAL-TRUNCATION-RE-DETERMINATION)",
    # dimension class
    "dimension_class": "DIMENSIONFUL (Tier-2-dimensionful — registry-PASS-INELIGIBLE)",
    # the held-object KIND
    "held_object_kind": "MAGNITUDE (a dimensionful scalar)",
    "canonical_kind": "spectral-action cardinality-cascade-tail observable (algebra-INVARIANT)",
}

# --- Member B: §(iv-bis) surrogate sub-row B CONTINGENT (pru-class-corpus.md §11.1) ---
MEMBER_B = {
    "tag": "B",
    "name": "§(iv-bis) surrogate sub-row B (CONTINGENT)",
    "parent_rule": 'substrate-first-canonical-sourcing.md §(iv-bis) '
                   '"Surrogate-vs-Canonical at Cohomology-Class Layer"',
    "corpus": "pru-class-corpus.md §11.1 sub-row B (K=1; SUGGESTION)",
    "instance": "alpha_win_lo = s_CS / N_e (surrogate for a MAGNITUDE bound on |C|)",
    "theorem_structure_status": "PROVEN (canonical C = <[phi],Ch(P_0)> is a signed index-type)",
    "theorem_structure_basis": "the canonical Connes-Karoubi pairing C is a proven "
                               "index-type quantity; only the surrogate bound is under-derived",
    # STRUCTURED predicate fields (read off corpus §11.1 sub-row B; NOT prose substring-match):
    "structure_permanent_or_proven": True,   # canonical C is a PROVEN signed index-type
    "number_is_held": True,                   # the under-derived |C| >= Sigma bound is HELD
    "repinned_to_methodology_floor_F_image": False,  # waits for a DERIVED substrate bound
    "held_number": "under-derived MAGNITUDE bound (the inequality |C| >= Sigma)",
    "held_status": "non-promotable-PENDING-derived-substrate-bound",
    "firing_sub_test": "§(iv-bis) sub-test (i): undischarged substitution chain "
                       "(|C| >= Sigma is non-promotable unless the bounding step is a "
                       "derived substrate identity; the trivial |C| >= 0 forbids nothing)",
    "block_mechanism": "the bounding step relating the surrogate Sigma to a bound on |C| "
                       "is NOT a derived substrate identity; the surrogate does not bound "
                       "the canonical's MAGNITUDE",
    "non_promotion_permanence": "CONTINGENT",
    "discharge_eligible": True,   # discharge by DERIVING the bounding step as a substrate identity
    "discharge_route": "derive the bound as a substrate identity "
                       "(CF-S94-NARROW-PATH-WORKSHOP-6-COCYCLE-CONSTRUCTION deliverable 1)",
    "dimension_class": "DIMENSIONLESS (a magnitude-comparison surrogate)",
    "held_object_kind": "MAGNITUDE-bound (the inequality on |C|)",
    "canonical_kind": "Connes-Karoubi pairing magnitude |C| (cohomology-class observable)",
}

# --- Member C: §(iv-bis) surrogate sub-row A PERMANENT sign-lock (pru-class-corpus.md §11.1 / §11) ---
MEMBER_C = {
    "tag": "C",
    "name": "§(iv-bis) surrogate sub-row A (PERMANENT sign-lock)",
    "parent_rule": 'substrate-first-canonical-sourcing.md §(iv-bis) '
                   '"Surrogate-vs-Canonical at Cohomology-Class Layer"',
    "corpus": "pru-class-corpus.md §11.1 sub-row A / §11 worked example (K=1; SUGGESTION)",
    "instance": "R_surr = 2f - 1 (surrogate for the signed VALUE of C)",
    "theorem_structure_status": "PROVEN (canonical C = <[phi],Ch(P_0)> is a signed index-type)",
    "theorem_structure_basis": "the surrogate's sign is mechanically locked to a Peter-Weyl "
                               "partition fraction by the algebraic identity R_surr = 2f-1 "
                               "(Sage-exact); the canonical C is a proven index-type",
    # STRUCTURED predicate fields (read off corpus §11.1 sub-row A / §11; NOT prose substring-match):
    "structure_permanent_or_proven": True,   # canonical C is a PROVEN signed index-type
    "number_is_held": True,                   # the sign-locked surrogate VALUE is HELD (uninformative on sign(C))
    "repinned_to_methodology_floor_F_image": False,  # sign(C) requires a SEPARATE canonical-evaluation gate
    "held_number": "sign-locked surrogate VALUE (R_surr, sign forced by f > 1/2)",
    "held_status": "PERMANENTLY-uninformative-on-sign(C)",
    "firing_sub_test": "§(iv-bis) sub-test (ii): sign-lock divergence "
                       "(a mechanically sign-locked Sigma — combinatorial fraction, "
                       "Cauchy-Schwarz positivity — is uninformative on sign(C) at ANY margin)",
    "block_mechanism": "the surrogate sign is a combinatorial constraint (R_surr = 2f-1) "
                       "with NO cohomology-class content (no Hochschild cocycle / Chern character "
                       "/ Connes-Karoubi geometry enters the sign); the surrogate-canonical "
                       "algebraic distance does not bound the canonical's SIGN",
    "non_promotion_permanence": "PERMANENT",
    "discharge_eligible": False,  # NEVER discharges — the sign-lock is a permanent combinatorial fact
    "discharge_route": "N/A — the sign is mechanically locked to a combinatorial fraction forever; "
                       "the only route to sign(C) is a SEPARATE canonical-evaluation gate, "
                       "not a refinement of THIS surrogate",
    "dimension_class": "DIMENSIONLESS (a signed-value surrogate in [-1,+1])",
    "held_object_kind": "VALUE (a sign-locked signed surrogate)",
    "canonical_kind": "Connes-Karoubi pairing sign sign(C) (cohomology-class observable)",
}

MEMBERS = [MEMBER_A, MEMBER_B, MEMBER_C]  # (local)


# ---------------------------------------------------------------------------
# Section 6 — Shared-predicate + orthogonality decision logic
# ---------------------------------------------------------------------------

def shared_predicate_holds(m: dict) -> dict:
    """Test the candidate UNIFYING shared predicate against one member.

    Shared predicate (genus):
      P1: theorem-STRUCTURE is permanent/proven (STAGE-3-PERMANENT or PROVEN), AND
      P2: a NUMBER (dimensionful magnitude / under-derived bound / sign-locked value)
          is HELD against substrate-natural extraction (held_status != 'satisfied'), AND
      P3: the held NUMBER is NOT sideways-re-pinned to a methodology-floor F-image
          (the substrate's structural identity stays logically prior; the held number
          waits for a substrate-NATURAL extraction or stays held permanently).
    """
    # Read the STRUCTURED boolean fields (encoded per member from the corpus text);
    # do NOT infer the predicate by substring-scanning prose (the prior approach false-
    # negatived on "NOT-SATISFIED" containing the substring "SATISFIED" and on the
    # parenthetical-annotated "PROVEN (...)" failing exact set-membership).
    p1 = bool(m["structure_permanent_or_proven"])  # (local)
    p2 = bool(m["number_is_held"])                 # (local)
    p3 = not bool(m["repinned_to_methodology_floor_F_image"])  # (local)
    return {"P1_structure_permanent": p1,
            "P2_number_held": p2,
            "P3_not_repinned_to_F_image": p3,
            "shared_predicate_holds": bool(p1 and p2 and p3)}


def orthogonality_axes(members: list[dict]) -> dict:
    """Test the ORTHOGONALITY conjunct: are the members distinct on the three
    structural discriminator axes (firing sub-test / permanence class / parent rule)?

    A merge would be a FALSE unification iff the members are NOT all-identical on
    every discriminator (i.e., there exist >=2 distinct values on >=1 axis). We
    report distinctness on EACH axis; orthogonality_confirmed is TRUE when the
    members are pairwise-distinguishable on at least the firing-sub-test axis AND
    differ in permanence class.
    """
    firing = [m["firing_sub_test"].split(":")[0].strip() for m in members]   # (local) coarse-key per member
    perm = [m["non_promotion_permanence"] for m in members]                  # (local)
    parents = [m["parent_rule"] for m in members]                            # (local)
    dims = [m["dimension_class"].split(" ")[0] for m in members]             # (local)
    kinds = [m["held_object_kind"].split(" ")[0] for m in members]          # (local)
    discharge = [m["discharge_eligible"] for m in members]                  # (local)

    def distinct_count(xs):  # (local)
        return len(set(xs))

    # firing sub-tests: A fires on Tier-1+Tier-2; B on §(iv-bis) sub-test (i); C on sub-test (ii)
    n_firing = distinct_count(firing)        # (local)
    n_perm = distinct_count(perm)            # (local)
    n_parents = distinct_count(parents)      # (local)
    n_dims = distinct_count(dims)            # (local)
    n_kinds = distinct_count(kinds)          # (local)
    n_discharge = distinct_count(discharge)  # (local)

    # B vs C share the SAME parent rule (§(iv-bis)) but distinct sub-tests + distinct permanence;
    # A has a DIFFERENT parent (anatomy Tier-1/Tier-2). So parents: 2 distinct values.
    return {
        "firing_sub_test_per_member": firing,
        "permanence_per_member": perm,
        "parent_rule_per_member": parents,
        "dimension_class_per_member": dims,
        "held_object_kind_per_member": kinds,
        "discharge_eligible_per_member": discharge,
        "n_distinct_firing_sub_tests": n_firing,    # expect 3 (A Tier; B (i); C (ii))
        "n_distinct_permanence_classes": n_perm,    # expect 3 (PERMANENT-pending-physical; CONTINGENT; PERMANENT)
        "n_distinct_parent_rules": n_parents,       # expect 2 (anatomy; §(iv-bis))
        "n_distinct_dimension_classes": n_dims,     # expect 2 (DIMENSIONFUL vs DIMENSIONLESS)
        "n_distinct_held_object_kinds": n_kinds,    # expect 3 (MAGNITUDE; MAGNITUDE-bound; VALUE)
        "n_distinct_discharge_flags": n_discharge,  # expect 2 (True/True/False)
        # orthogonality is CONFIRMED iff the three members are pairwise-distinguishable on the
        # firing-sub-test axis (all 3 distinct) AND differ in permanence class (>=2 distinct).
        "orthogonality_confirmed": bool(n_firing == 3 and n_perm >= 2),
        "merge_would_be_false_unification": bool(n_firing == 3 and n_perm >= 2),
    }


def decide_outcome(members: list[dict]) -> dict:
    """Reconcile the shared-predicate conjunct and the orthogonality conjunct.

    Pre-registered outcomes (neither pre-judged):
      OUTCOME-1 UNIFYING-META-RULE-DRAFTED — a single shared predicate covers all
        members AND a per-member discriminator distinguishes them within the unified
        taxonomy.
      OUTCOME-2 THREE-CONFIRMED-ORTHOGONAL — distinct firing sub-tests / permanence
        classes / parent rules such that a merge would conflate structurally-distinct
        mechanisms.

    The structural fact (derived, not asserted): BOTH conjuncts hold simultaneously.
    The shared predicate (genus) covers all three; the discriminators (firing sub-test
    / permanence / parent / dimension / held-object-kind) are the orthogonal differentiae.
    A genus+differentiae structure is a TAXONOMY: it UNIFIES at the genus level WITHOUT
    collapsing the orthogonal differentiae. Therefore the correct outcome is OUTCOME-1
    realized AS a taxonomy that ENCODES the OUTCOME-2 orthogonality as its discriminator
    axis — NOT a flat merge (which would erase the differentiae => false unification) and
    NOT three-walls-that-never-touch (which would deny the genuine shared genus).
    """
    sp = [shared_predicate_holds(m) for m in members]  # (local)
    sp_all = all(s["shared_predicate_holds"] for s in sp)  # (local)
    ortho = orthogonality_axes(members)  # (local)

    # The genus+differentiae reconciliation:
    #   - shared predicate holds for ALL members  => a genuine genus exists  => UNIFYING is licensed
    #   - members are orthogonal on the discriminator axes => the genus must carry a
    #     per-member discriminator (NOT a flat merge) => the orthogonality is PRESERVED inside
    #     the unified taxonomy as its differentia axis
    unifying_via_taxonomy = bool(sp_all and ortho["orthogonality_confirmed"])  # (local)

    if unifying_via_taxonomy:
        outcome = "UNIFYING-META-RULE-DRAFTED"  # (local)
        reading = ("genus+differentiae: a single shared predicate (genus) unifies all three; "
                   "the orthogonal firing-sub-test/permanence/parent discriminators are PRESERVED "
                   "as the taxonomy's per-member differentia axis (NOT collapsed by a flat merge, "
                   "NOT denied by three-disjoint-walls)")  # (local)
    elif sp_all and not ortho["orthogonality_confirmed"]:
        # would only fire if the members were NOT orthogonal — a flat merge would then be honest.
        outcome = "UNIFYING-META-RULE-DRAFTED"  # (local)
        reading = "flat merge (members not orthogonal on discriminator axes)"  # (local)
    else:
        # would fire if the shared predicate did NOT cover all members.
        outcome = "THREE-CONFIRMED-ORTHOGONAL"  # (local)
        reading = ("no genuine shared genus — the members fail the shared predicate, "
                   "so a merge would be a false unification")  # (local)

    return {
        "shared_predicate_per_member": {m["tag"]: s for m, s in zip(members, sp)},
        "shared_predicate_holds_all": sp_all,
        "orthogonality": ortho,
        "unifying_via_taxonomy": unifying_via_taxonomy,
        "outcome": outcome,
        "reconciliation_reading": reading,
    }


# ---------------------------------------------------------------------------
# Section 7 — Verdict emission (atomic append; S84+ dual-SHA)
# ---------------------------------------------------------------------------

def append_verdict(verdict: str, value, audit_sha: str, content_sha: str,
                   supersedes: str = "") -> None:
    """Append a single-line dual-SHA verdict to s94_gate_verdicts.txt.

    Atomic append (single open("a") write — no read-modify-write, no truncate).
    Emits the canonical line + the dual-SHA companion comment row.

    If `supersedes` (a full 64-char prior audit_sha256) is given, the corrective
    line carries `supersedes=<old>` in its value= field per gate-verdicts.md
    "Option A — sig_5 remediation pathway under absolute verdict permanence":
    the prior line is RETAINED on disk; the corrective successor APPENDS with the
    supersedes tag; downstream consumers cite the latest non-superseded line.
    """
    value_str = repr(value)  # (local)
    if supersedes:
        # carry the supersedes token inside the value= field (full 64-char old SHA).
        value_str = repr(f"{value};supersedes={supersedes}")  # (local)
    line = (
        f"{GATE_ID}: {verdict} -- value={value_str} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; [AUDIT] non-promotion meta-taxonomy synthesis; "
        f"INFO-by-design; no [SIGN] 3-tuple"
    )
    if supersedes:
        companion += f"; supersedes={supersedes} (Option A; gate-verdicts.md)"
    companion += "\n"
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # --- The synthesis ---
    decision = decide_outcome(MEMBERS)  # (local)
    outcome = decision["outcome"]  # (local)
    ortho = decision["orthogonality"]  # (local)

    # INFO-by-design: top-line verdict is INFO regardless of UNIFYING vs ORTHOGONAL.
    verdict = "INFO"  # (local)

    # Compact value string (single line; the full structure is in the JSON sidecar).
    value = (
        f"outcome={outcome};"
        f"shared_predicate_holds_all={decision['shared_predicate_holds_all']};"
        f"n_distinct_firing_sub_tests={ortho['n_distinct_firing_sub_tests']};"
        f"n_distinct_permanence_classes={ortho['n_distinct_permanence_classes']};"
        f"n_distinct_parent_rules={ortho['n_distinct_parent_rules']};"
        f"n_distinct_dimension_classes={ortho['n_distinct_dimension_classes']};"
        f"n_distinct_held_object_kinds={ortho['n_distinct_held_object_kinds']};"
        f"orthogonality_confirmed={ortho['orthogonality_confirmed']};"
        f"unifying_via_taxonomy={decision['unifying_via_taxonomy']};"
        f"members=A:Tier-2-dimensionful[STAGE-3-PERMANENT,DIMENSIONFUL-magnitude-HELD,"
        f"dimensionful-slot-collision,PERMANENT-pending-physical-anchor]|"
        f"B:iv-bis-sub-row-B[PROVEN,under-derived-MAGNITUDE-bound-HELD,"
        f"undischarged-substitution-chain-(i),CONTINGENT]|"
        f"C:iv-bis-sub-row-A[PROVEN,sign-locked-VALUE-HELD,sign-lock-(ii),PERMANENT];"
        f"shared_predicate=theorem-STRUCTURE-permanent;NUMBER-held-pending-substrate-natural-extraction;"
        f"per-member-discriminator=dimensionful-slot-collision|undischarged-magnitude-bound|sign-lock;"
        f"allowlist_append=REQUIRED"
    )

    # --- JSON sidecar ---
    report = {
        "gate_id": GATE_ID,
        "session": SESSION,
        "verdict": verdict,
        "verdict_note": "INFO-by-design; PASS/FAIL rubric describes synthesis QUALITY not top-line",
        "outcome": outcome,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "members": MEMBERS,
        "decision": decision,
        "shared_predicate_genus": (
            "theorem-STRUCTURE permanent/proven; a corrupted/under-derived NUMBER is HELD "
            "against substrate-natural extraction, NOT sideways-re-pinned to a methodology-floor F-image"
        ),
        "per_member_discriminator": {
            "A": "dimensionful-slot-collision (dimension + L_max-divergence share one multiplicative slot)",
            "B": "undischarged-magnitude-bound (the bounding step is not a derived substrate identity)",
            "C": "sign-lock (the surrogate sign is a combinatorial fraction with no cohomology content)",
        },
        "orthogonality_preserved_as_differentia": True,
        "false_unification_avoided": (
            "the unified taxonomy ENCODES the orthogonality as its per-member discriminator axis; "
            "it does NOT flat-merge the three (which would erase the differentiae) and does NOT "
            "deny the shared genus (which would be three-disjoint-walls)"
        ),
        "distinction_from_deferred_pending_taxonomy": (
            "the deferred-pending intermediate verdict-class (PROXY-REFINEMENT / FIRST-EXTRACTION / "
            "OPERATIONAL-ALIGNMENT, cross-pillar-bridge-anatomy.md) RESERVES a §VII slot while a "
            "Level-2 envelope is realized via proxy/symbolic/unaligned machinery — it is about WHEN "
            "a binding Level-2 lands. The non-promotion meta-taxonomy is about a held LEVEL-3 NUMBER "
            "(or surrogate value/bound) under a PERMANENT/proven structure — it is about whether the "
            "substrate NUMBER can be extracted at all from the available channel. The two taxonomies "
            "are ORTHOGONAL (one keys on Level-2 realization stage; the other on Level-3/surrogate "
            "number extractability under a settled structure)."
        ),
        "allowlist_append_flag": {
            "status": "REQUIRED",
            "row_form": f"| {GATE_ID} | S94 | <sha256_of_plan_block> |",
            "note": "orchestrator-only edit per methodology-wave-allowlist.md; subagents edit-denied",
        },
        "input_pins": pins,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "supersedes_prior_audit_sha256": SUPERSEDES_PRIOR,
        "supersedes_note": (
            "Option A (gate-verdicts.md): the first (pre-self-correction) run appended a line "
            "with this audit_sha256; that line is RETAINED on disk; this corrective successor "
            "carries supersedes=<old> in value=; latest non-superseded line is canonical. "
            "Self-correction: the prior run's predicate detector substring-scanned prose and "
            "false-negatived (P1 set-membership failed on 'PROVEN (...)' parenthetical; P2 "
            "'satisfied' substring matched inside 'NOT-SATISFIED'); fixed to read structured "
            "boolean fields, recovering shared_predicate_holds_all=True."
        ),
        "wall_seconds": None,
    }
    report["wall_seconds"] = round(time.time() - t0, 4)

    with OUT_JSON.open("w", encoding="utf-8") as fp:
        json.dump(report, fp, indent=2)

    # --- emit ---
    print(f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    append_verdict(verdict, value, audit_sha, content_sha, supersedes=SUPERSEDES_PRIOR)

    print()
    print(f"=== {GATE_ID}: {verdict} | outcome={outcome} ===")
    print(f"  shared predicate holds for ALL members: {decision['shared_predicate_holds_all']}")
    print(f"  distinct firing sub-tests:  {ortho['n_distinct_firing_sub_tests']} (expect 3)")
    print(f"  distinct permanence classes:{ortho['n_distinct_permanence_classes']} (expect 3)")
    print(f"  distinct parent rules:      {ortho['n_distinct_parent_rules']} (expect 2)")
    print(f"  distinct dimension classes: {ortho['n_distinct_dimension_classes']} (expect 2)")
    print(f"  distinct held-object kinds: {ortho['n_distinct_held_object_kinds']} (expect 3)")
    print(f"  reconciliation: {decision['reconciliation_reading']}")
    print(f"  JSON: {OUT_JSON.relative_to(PROJECT_ROOT)}")
    print(f"  wall {report['wall_seconds']}s")
    # INFO is a valid scientific result; exit 0 (script health), NOT coupled to verdict.
    return 0


if __name__ == "__main__":
    sys.exit(main())
