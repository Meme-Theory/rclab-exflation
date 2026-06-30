"""
s87_w5_cross_pillar_forward_candidates.py
=========================================

Gate: S87-CROSS-PILLAR-FORWARD-CANDIDATES   (S87 W5-5 / CF-35)

Owner    : volovik-superfluid-universe-theorist (orchestrator role for forward-
           looking template adoption per feedback_agent-roster.md)
Co-signer: connes-ncg-theorist  (NCG-axiomatic side of any future Pillar A↔B
           bridge candidates)

Lands the **template-adoption SUGGESTION** clause in
.claude/rules/cross-pillar-bridge-anatomy.md enumerating 2-3 forward bridge
candidates for S88+ dispatch, cross-referencing
.claude/rules/inheritance-falsifier-protocol.md §"Generalization beyond
3He-B (W-5 Q8)" rank-2 generalization, and pinning K=1 SUGGESTION-not-
MANDATORY status per agent-standards.md HIGH-DENSITY WORKSHOP TEMPLATE
K=3 promotion threshold.

This is a METHODOLOGY-class artifact landing under a COMPUTE-classed wave
(plan §W5-5).  The verdict criterion is structural string-presence on
.claude/rules/cross-pillar-bridge-anatomy.md post-edit:

  PASS iff  ALL FOUR of the following hold post-edit:
    (1) Forward template-adoption SUGGESTION text landed in
        cross-pillar-bridge-anatomy.md (calibration corpus or sibling
        sub-section), listing W-5 as instance #1.
    (2) Rank-2 generalization clause from inheritance-falsifier-protocol.md
        §"Generalization beyond 3He-B (W-5 Q8)" cross-referenced.
    (3) 2-3 candidate forward bridge pairs explicitly enumerated, each with
        substrate-IS / laboratory-IN identifications.
    (4) SUGGESTION-not-MANDATORY status declared explicitly at K=1.

Substitution chain (K=1 ⇒ SUGGESTION, not MANDATORY; per plan §W5-5
lines 482-487):
  Step 1 (definition):  K = count of distinct high-density workshops invoking
                        the cross-pillar-bridge-anatomy template.
  Step 2 (substrate):   W-5 (Pillar III ↔ Pillar IV) is calibration-corpus
                        instance #1 ⇒  K = 1.
                        K_promotion = 3  (agent-standards.md HIGH-DENSITY
                        WORKSHOP TEMPLATE forward-calibration; aligns with
                        feedback_rules-compensate-missing-structure.md
                        K=3 promotion threshold).
  Step 3 (form):        K (=1)  <  K_promotion (=3).
  Step 4 (canonical):   1 < 3   (integer; bit-exact).
  Step 5 (direction):   K < K_promotion  ⇒  status = SUGGESTION
                                            (NOT MANDATORY).
  Conclusion: this gate MUST declare SUGGESTION-not-MANDATORY status; the
              template hardens to MANDATORY when N=3 calibration instances
              accumulate (S88+ promotion event).

Structural references:
  • .claude/rules/cross-pillar-bridge-anatomy.md  (target file; existing
    §"Calibration corpus" carries W-5 instance #1)
  • .claude/rules/inheritance-falsifier-protocol.md  §"Generalization
    beyond 3He-B (W-5 Q8)"  (rank-2 cross-ref target)
  • .claude/rules/agent-standards.md  §"HIGH-DENSITY WORKSHOP TEMPLATE"
    (K=3 promotion-threshold rule)
  • sessions/permanent-results-registry.md  §VII.AF.1  (CF-31 LANDED;
    canonical W-5 calibration-corpus instance #1)

Outputs:
  1. JSON sidecar:  computations/session-87/s87_w5_cross_pillar_forward_candidates.json
  2. Verdict line + dual-SHA companion + S87 schema-v2 3-tuple companion
     appended to computations/session-87/s87_gate_verdicts.txt
  3. Edit:  .claude/rules/cross-pillar-bridge-anatomy.md  — append
     §"Forward template-adoption (calibration-corpus tracking)" sub-section
     containing the SUGGESTION clause + 3 candidate enumerations + rank-2
     cross-ref + K=1 status pin.

CPU-only:  string-edit + SHA computation; no linear algebra; OMP_NUM_THREADS=8
cap (legacy compliance — not load-bearing here).
"""

from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# Project canonical constants (mandatory per .claude/rules/math-scripts.md S34+).
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import (  # noqa: E402
    M_KK,
    tau_fold,
)

# --------------------------------------------------------------------------
# Pinned plan-block parameters (per session-87-plan-w5.md §W5-5)
# --------------------------------------------------------------------------

GATE_ID = "S87-CROSS-PILLAR-FORWARD-CANDIDATES"                              # (local)
SCHEME = "workshop-design-SUGGESTION-K1-calibration"                         # (local)
CONVENTION = "cross-pillar-bridge-anatomy-forward-template-adoption"         # (local)
L_MAX_TAG = "N/A"                                                            # (local)
SCHEMA_VERSION = "S87+"                                                      # (local)

# K-counter substitution chain (verified bit-exact: 1 < 3 ⇒ SUGGESTION).
K_CALIBRATION_INSTANCES = 1                                                  # (local) W-5 = instance #1
K_PROMOTION_THRESHOLD = 3                                                    # (local) agent-standards.md HIGH-DENSITY WORKSHOP TEMPLATE
STATUS_PIN = (
    "SUGGESTION" if K_CALIBRATION_INSTANCES < K_PROMOTION_THRESHOLD else "MANDATORY"
)                                                                            # (local)

# --------------------------------------------------------------------------
# Project paths
# --------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent
RULE_BRIDGE_ANATOMY = REPO_ROOT / ".claude/rules/cross-pillar-bridge-anatomy.md"
RULE_INHERITANCE = REPO_ROOT / ".claude/rules/inheritance-falsifier-protocol.md"
RULE_AGENT_STD = REPO_ROOT / ".claude/rules/agent-standards.md"
REGISTRY_PERM = REPO_ROOT / "sessions/permanent-results-registry.md"
VERDICT_FILE = REPO_ROOT / "computations/session-87/s87_gate_verdicts.txt"
JSON_SIDECAR = REPO_ROOT / "computations/session-87/s87_w5_cross_pillar_forward_candidates.json"
WP_FILE = REPO_ROOT / "sessions/archive/session-87/session-87-results-workingpaper.md"
PLAN_FILE = REPO_ROOT / "sessions/session-plan/session-87-plan-w5.md"

# --------------------------------------------------------------------------
# SHA helpers
# --------------------------------------------------------------------------


def sha256_file(path: Path) -> str:
    """SHA-256 of file contents (bit-exact over current on-disk state)."""
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pin_map: dict) -> str:
    """SHA-256 over the canonical-ordered input-pin map (audit_sha256)."""
    canonical = json.dumps(pin_map, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def content_hash(text: str) -> str:
    """SHA-256 over the substantive content payload (content_sha256)."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


# --------------------------------------------------------------------------
# Forward bridge candidate specs (3 candidates; SUGGESTION-not-MANDATORY)
# --------------------------------------------------------------------------

CANDIDATE_C1 = {                                                              # (local)
    "id": "FWD-C1",
    "label": "Pillar I ↔ Pillar II  (substrate ↔ cosmology measurement)",
    "substrate_IS": (
        "n_s spectral-action prediction from finite-L D_K eigenmoments on "
        "(A_K^{≤L}, H_K^{≤L}, D_K^{≤L}) — the n_s_FW value is a substrate-IS "
        "scalar moment of the Jensen-deformed band-0 sector at τ_fold."
    ),
    "laboratory_IN": (
        "Planck CMB scalar spectral index n_s = 0.9649 ± 0.0042 (Planck 2018 "
        "TT,TE,EE+lowE+lensing) — measured IN the FRW cosmology container as "
        "the slope of the temperature power spectrum near k_pivot = 0.05 Mpc⁻¹."
    ),
    "bridge_map": (
        "Mukhanov-Sasaki gauge-invariant mode-function transfer ∘ HKR `L_max → ∞` "
        "image of the substrate scalar spectral moment.  The bridge factors "
        "through the c_sub conformal-anomaly multiplier per S86 W5a Z-factor "
        "machinery."
    ),
    "algebraic_envelope": (
        "L_max⁻³ at d=4 inherited from Pillar III ↔ IV (W-5 calibration); "
        "Level-2 canonical envelope pending substrate-first c_sub completion."
    ),
    "empirical_anchor_target": (
        "n_s_FW vs Planck n_s comparison at canonical L_max=10 under "
        "substrate-first IC (S86 W5a SR-flow Z-factor pivot)."
    ),
    "rank_kernel": "rank(ker ι_*) = 1 (single n_s scalar; rank-2 not applicable)",
    "earliest_S88_dispatch": "S88 W-? (post-c_sub completion)",
}

CANDIDATE_C2 = {                                                              # (local)
    "id": "FWD-C2",
    "label": "Pillar II ↔ Pillar V  (Mellin-cone ↔ BdG spectral triple)",
    "substrate_IS": (
        "Mellin-Barnes residue at substrate-distance s ∈ {3, 4} on the "
        "Pillar-II Mellin-cone, evaluated against ζ-regulated Hochschild "
        "moments of D_K — the substrate IS the Mellin-residue cocycle "
        "(workshop-§VII.U/V family on the spectral-distance axis)."
    ),
    "laboratory_IN": (
        "BdG (Bogoliubov-de Gennes) spectral-triple observable in a "
        "self-consistent BCS lattice — measured IN the Brillouin-zone "
        "container as the BdG band structure with Pf=−1 BDI topology "
        "(3He-B child realization; Volovik 2003 §6)."
    ),
    "bridge_map": (
        "Connes-Karoubi pairing ∘ K-theory boundary map between the Pillar-II "
        "Mellin pole structure and the Pillar-V finite-rank BdG K_0(M_2(C)) "
        "image; companion to W-6 quotient-functor framework "
        "(cross-pillar-bridge-anatomy §Quotient-functor pre-registration)."
    ),
    "algebraic_envelope": (
        "L_max⁻α with α ∈ {2, 3} under spectral-distance scaling; α pinned "
        "post-Mellin-pole-closure at S87 W2-? cluster-span PASS."
    ),
    "empirical_anchor_target": (
        "Pillar-II → Pillar-V Mellin-residue / BdG-band-edge match at "
        "canonical L_max=10; substrate-first cocycle norms ‖φ‖ Sage-exact "
        "(per W-5 phi67/phi88 calibration)."
    ),
    "rank_kernel": (
        "rank(ker ι_*) ≥ 2 expected — Mellin-cone carries multiple residue "
        "generators; invokes rank-2 generalization "
        "(inheritance-falsifier-protocol.md §Generalization beyond 3He-B)."
    ),
    "earliest_S88_dispatch": "S88 W-? (post-§VII.U/V family closure)",
}

CANDIDATE_C3 = {                                                              # (local)
    "id": "FWD-C3",
    "label": "Pillar IV ↔ Pillar V  (substrate cocycles ↔ 3He-B / 3He-A laboratory observables)",
    "substrate_IS": (
        "Substrate-resident HP^1 cocycle norms ‖φ_67‖, ‖φ_88‖ (W-5 Sage-exact: "
        "‖φ_67‖ = 0.793346 M_KK², ‖φ_88‖ = 0.108307 M_KK², ratio 7.324992) "
        "evaluated on the BdG-restricted spectral-triple sub-algebra of "
        "(A_K, H_K, D_K).  The substrate IS the cocycle pair — these are "
        "intrinsic structural numbers, not BdG band-structure derivatives."
    ),
    "laboratory_IN": (
        "3He-B vortex-core Caroli-Matricon ladder asymmetry (W11-C5; "
        "Lancaster MCT-3 / Helsinki ROTA cells) AND 3He-A µSR chirality "
        "discrimination (W11-C6; partially queued at S87 CF-32 + CF-33).  "
        "Lab measures these IN the helium cryostat container under a "
        "(p, T) sweep over 0–34 bar."
    ),
    "bridge_map": (
        "Inheritance morphism ι_*: A_K = C ⊕ H ⊕ M_3(C) → M_2(C) "
        "(BDI → BdG sector child) ∘ (Δ_B/Δ_A)^p lab-conversion factor.  "
        "Cancellation theorem (S86 W-5 DONE-5; 0.0e+00 residual) preserves "
        "‖φ_a‖/‖φ_b‖ INTACT in the lab measurement under common p."
    ),
    "algebraic_envelope": (
        "Cohomology-asymmetry test: ratio preservation 7.3250 ± 0.1% (S86 W-5 "
        "Gate-2 pre-registered band).  Level-2 envelope is the structural-"
        "exact form, not an L_max⁻α algebraic bound; the regulator-invariant "
        "ratio replaces the convergence envelope for this candidate class."
    ),
    "empirical_anchor_target": (
        "S88+ Lancaster MCT-3 vortex-core spectroscopy and RHUL/Aalto LTL "
        "µSR run delivering NULL on F1/F2/F5 + ratio 7.3250 ± 0.1% on any "
        "non-NULL detection (4-gate falsifier structure per inheritance-"
        "falsifier-protocol.md §Four-Gate Structure)."
    ),
    "rank_kernel": (
        "rank(ker ι_*) = 2 (φ_67 chiral pair + φ_88 Cartan hypercharge) — "
        "DIRECTLY invokes inheritance-falsifier-protocol.md §Generalization "
        "beyond 3He-B (W-5 Q8) rank-2 case."
    ),
    "earliest_S88_dispatch": (
        "Partially LANDED via CF-32 + CF-33 lab pre-registrations (S87 W5-2 "
        "+ W5-3); FULL bridge-anatomy registry entry queued for S88+ once "
        "lab data lands (multi-year experimental cycle)."
    ),
}

CANDIDATES = [CANDIDATE_C1, CANDIDATE_C2, CANDIDATE_C3]                       # (local)

# --------------------------------------------------------------------------
# Drafting the SUGGESTION clause
# --------------------------------------------------------------------------


def render_candidate_block(c: dict) -> str:
    """Render one forward-bridge candidate as Markdown."""
    return (
        f"#### {c['id']} — {c['label']}\n\n"
        f"- **Substrate-IS observable** — {c['substrate_IS']}\n"
        f"- **Laboratory-IN observable** — {c['laboratory_IN']}\n"
        f"- **Bridge map** — {c['bridge_map']}\n"
        f"- **Algebraic envelope** — {c['algebraic_envelope']}\n"
        f"- **Empirical anchor target** — {c['empirical_anchor_target']}\n"
        f"- **Inheritance kernel rank** — {c['rank_kernel']}\n"
        f"- **Earliest S88+ dispatch** — {c['earliest_S88_dispatch']}\n"
    )


def draft_suggestion_text() -> str:
    """Build the full SUGGESTION-clause block to append to the rule file."""
    candidate_blocks = "\n".join(render_candidate_block(c) for c in CANDIDATES)
    return (
        "\n## Forward template-adoption (calibration-corpus tracking)\n\n"
        "> **Provenance**: S87 W5-5 (volovik orchestrator role; co-signer "
        "connes-ncg-theorist).  Forward-looking template-adoption SUGGESTION "
        "for cross-pillar-bridge-anatomy.md.  Source: "
        "`sessions/session-plan/session-87-plan-w5.md` §W5-5 + `sessions/"
        "session-87/session-87-results-workingpaper.md` §W5-5.\n\n"
        "### Status: SUGGESTION (NOT MANDATORY) at K=1\n\n"
        "Per `.claude/rules/agent-standards.md` §\"HIGH-DENSITY WORKSHOP "
        "TEMPLATE\" (T2-5), the cross-pillar-bridge-anatomy discipline "
        "(5 IS-not-IN elements + 3-level ladder) hardens to a permanent "
        "MANDATORY rule when N=3 distinct high-density workshops invoke it "
        "(K=3 promotion threshold; aligns with "
        "`feedback_rules-compensate-missing-structure.md`).  At S87 close "
        "the corpus contains:\n\n"
        "| # | Workshop | Bridge | Status |\n"
        "|:--|:---------|:-------|:-------|\n"
        "| 1 | S86 W-5 (volovik PRIMARY + connes CO-AUTHOR) | "
        "Pillar III ↔ Pillar IV  (HP^1 cohomology ↔ Peotta-Törmä quantum-metric "
        "trace) | LANDED §VII.AF.1 (S87 W5-1) |\n"
        "| 2 | — | — | (awaits future high-density workshop) |\n"
        "| 3 | — | — | (awaits future high-density workshop) |\n\n"
        f"K = {K_CALIBRATION_INSTANCES}  <  K_promotion = "
        f"{K_PROMOTION_THRESHOLD}  ⇒  status = **{STATUS_PIN}** "
        "(NOT MANDATORY).  Promotion event triggers when a 2nd and 3rd "
        "calibration instance land; until then, future cross-pillar bridge "
        "candidates SHOULD adopt the 5-anatomy + 3-level discipline as a "
        "design SUGGESTION, not yet a structural REQUIREMENT.\n\n"
        "**Why K-tracked promotion (not immediate MANDATORY)**: a single "
        "calibration instance does not exhibit cross-context stress-testing.  "
        "The K=3 ladder forces three structurally-distinct workshops to "
        "instantiate the anatomy before the rule's edge cases are saturated; "
        "premature MANDATORY-status would lock in W-5-specific accidents "
        "(e.g., L^{-3} envelope is d=4-specific; future bridges at d ≠ 4 "
        "may require different α).\n\n"
        "### Three forward bridge candidates for S88+ dispatch\n\n"
        "Each candidate is pre-registered with substrate-IS / laboratory-IN "
        "identifications, an explicit bridge map, an algebraic envelope (or "
        "structural-exact replacement), an empirical anchor target, and an "
        "inheritance-kernel rank declaration.  Adoption of the 5-anatomy + "
        "3-level discipline is RECOMMENDED for each; absence of structure on "
        "an S88+ landing routes to plan-freeze halt under the existing "
        "§\"Forward-looking convention-pin\" clause (already MANDATORY at "
        "K=1 by that older clause; this SUGGESTION adds the 3-candidate "
        "calibration-corpus tracking and the rank-2 cross-reference).\n\n"
        f"{candidate_blocks}\n"
        "### Cross-reference — rank-2 generalization clause\n\n"
        "Candidates **FWD-C2** (Pillar II ↔ Pillar V) and **FWD-C3** "
        "(Pillar IV ↔ Pillar V) carry inheritance-kernel rank ≥ 2 and "
        "MUST be designed under `.claude/rules/inheritance-falsifier-"
        "protocol.md` §\"Generalization beyond 3He-B (W-5 Q8)\" "
        "(rank-2 dual-cocycle case + rank ≥ 3 binomial(rank, 2) "
        "cross-cocycle ratio enumeration).  The rank-2 generalization "
        "clause specifies that for any future bridge with rank(ker ι_*) ≥ 2, "
        "the cohomology-asymmetry test (Class B) MUST pre-register all "
        "binomial(rank, 2) cross-cocycle ratios with substrate-derived "
        "values + tolerance bands, complementing the kernel-signature "
        "tests (Class A; rows F_a returning NULL).  The W-5 calibration "
        "ratio ‖φ_67‖/‖φ_88‖ = 7.324992 (Sage-exact) is the canonical "
        "exemplar; FWD-C2 + FWD-C3 inherit the (Δ_B/Δ_A)^p cancellation "
        "theorem applicability declaration as a mandatory pre-registration "
        "field.\n\n"
        "### Promotion event (forward-looking)\n\n"
        f"When K reaches {K_PROMOTION_THRESHOLD} distinct calibration "
        "instances, this sub-section is REPLACED in-place with a "
        "MANDATORY-status note + the 3 instance rows in the table above.  "
        "Promotion is triggered structurally (instance count) NOT by "
        "narrative argument; an orchestrator landing the third bridge "
        "writes the promotion edit in the same dispatch as the registry "
        "entry, per `feedback_fix-in-session-never-defer.md`.  Until "
        "promotion, all forward bridge candidates land under the "
        "**SUGGESTION** discipline declared here.\n\n"
        "### Calibration-corpus tracking (forward-looking)\n\n"
        "- instance #1: S86 W-5 Pillar III ↔ Pillar IV bridge theorem "
        "(LANDED `sessions/permanent-results-registry.md` §VII.AF.1 at "
        "S87 W5-1; volovik PRIMARY + connes CO-AUTHOR; HKR `L_max → ∞` "
        "bridge map; L^{-3} algebraic envelope at d=4; 0.0095% F_4 strict "
        "Level-3 anchor at L_max=10).\n"
        "- instance #2: SUGGESTED candidate from {FWD-C1, FWD-C2, FWD-C3} "
        "(whichever lands first at S88+).\n"
        "- instance #3: SUGGESTED next-after-#2.\n\n"
        "### Audit at plan-freeze (forward-looking)\n\n"
        "Plan-freeze validators landing an S88+ cross-pillar bridge entry "
        "SHOULD verify:\n\n"
        "1. The bridge label maps to one of {FWD-C1, FWD-C2, FWD-C3} OR "
        "declares a new candidate ID.\n"
        "2. The 5 IS-not-IN anatomy elements are present (existing MANDATORY "
        "from §\"Audit at plan-freeze\" above).\n"
        "3. The 3 tier markers are present (existing MANDATORY).\n"
        "4. If rank(ker ι_*) ≥ 2: inheritance-falsifier-protocol.md "
        "§\"Generalization beyond 3He-B (W-5 Q8)\" cross-reference present "
        "(SUGGESTED at K=1; will be MANDATORY at K=3).\n"
        "5. K-counter incremented by 1; if K reaches "
        f"{K_PROMOTION_THRESHOLD} post-landing, the orchestrator promotes "
        "this sub-section to MANDATORY in the same dispatch.\n"
    )


# --------------------------------------------------------------------------
# Idempotent edit helper (append-only Python writer; avoids Edit-tool
# mtime races per .claude/rules/epistemic-discipline.md
# §"Registry-Write Hygiene under Parallel-Writer Race")
# --------------------------------------------------------------------------

SUGGESTION_HEADER_MARKER = "## Forward template-adoption (calibration-corpus tracking)"


def append_suggestion_clause(suggestion_text: str) -> tuple[bool, str]:
    """Install the SUGGESTION clause in cross-pillar-bridge-anatomy.md.

    If the SUGGESTION header is absent, append the freshly-drafted block.
    If present but the on-disk content diverges from the freshly-drafted
    text (e.g., previous-run capitalization that no longer matches the
    pre-registered verifier rubric), overwrite the existing block with
    the canonical drafted text.

    Returns (action, post_state) where:
      - action     : "appended" / "overwritten" / "no-op"
      - post_state : final on-disk text after the (possibly no-op) write.
    """
    current = RULE_BRIDGE_ANATOMY.read_text(encoding="utf-8")
    idx = current.find(SUGGESTION_HEADER_MARKER)
    if idx < 0:
        new_text = current
        if not new_text.endswith("\n"):
            new_text += "\n"
        new_text += suggestion_text
        RULE_BRIDGE_ANATOMY.write_text(new_text, encoding="utf-8")
        return "appended", new_text

    # Header present — verify content matches freshly-drafted block bit-exactly.
    header_start = current.rfind("\n", 0, idx) + 1                            # (local)
    pre_header = current[:header_start]                                       # (local)
    drafted_starts_with_newline = suggestion_text.startswith("\n")
    drafted_body = (
        suggestion_text[1:] if drafted_starts_with_newline else suggestion_text
    )                                                                         # (local)
    expected_remainder = drafted_body                                         # (local)
    actual_remainder = current[header_start:]                                 # (local)
    if actual_remainder.rstrip() == expected_remainder.rstrip():
        return "no-op", current
    # Diverges — overwrite the SUGGESTION block (header onwards).
    new_text = pre_header.rstrip() + "\n\n" + expected_remainder
    if not new_text.endswith("\n"):
        new_text += "\n"
    RULE_BRIDGE_ANATOMY.write_text(new_text, encoding="utf-8")
    return "overwritten", new_text


# --------------------------------------------------------------------------
# Verification grep (re-read after write)
# --------------------------------------------------------------------------


def verify_post_edit_state(post_state: str) -> dict:
    """Grep the post-edit text for the 4 PASS criteria.  Returns a dict."""
    checks = {                                                                # (local)
        "C1_suggestion_clause_present": SUGGESTION_HEADER_MARKER in post_state,
        "C1_W5_instance_1_listed": "S86 W-5" in post_state and "instance #1" in post_state,
        "C2_rank2_xref_present": (
            "Generalization beyond 3He-B" in post_state
            and "rank-2" in post_state.lower()
        ),
        "C3_three_candidates_enumerated": all(
            f"FWD-C{i}" in post_state for i in (1, 2, 3)
        ),
        "C3_substrate_IS_per_candidate": (
            post_state.count("**Substrate-IS observable**") >= 3
        ),
        "C3_laboratory_IN_per_candidate": (
            post_state.count("**Laboratory-IN observable**") >= 3
        ),
        "C4_status_SUGGESTION_declared": (
            "**SUGGESTION**" in post_state and "(NOT MANDATORY)" in post_state
        ),
        "C4_K1_pin_present": (
            "K = 1" in post_state and "K_promotion = 3" in post_state
        ),
    }
    checks["ALL_4_PASS_CRITERIA_MET"] = all(
        [
            checks["C1_suggestion_clause_present"]
            and checks["C1_W5_instance_1_listed"],
            checks["C2_rank2_xref_present"],
            checks["C3_three_candidates_enumerated"]
            and checks["C3_substrate_IS_per_candidate"]
            and checks["C3_laboratory_IN_per_candidate"],
            checks["C4_status_SUGGESTION_declared"]
            and checks["C4_K1_pin_present"],
        ]
    )
    return checks


# --------------------------------------------------------------------------
# Verdict-line emission (canonical S87+ schema-v2 with 3-tuple companion)
# --------------------------------------------------------------------------


def append_verdict_block(
    composite: str,
    audit_sha256: str,
    content_sha256: str,
    sign_v: str,
    mag_v: str,
    regime_v: str,
    value_str: str,
) -> None:
    """Append canonical line + dual-SHA companion + 3-tuple companion."""
    canon_line = (
        f"{GATE_ID}: {composite} -- value={value_str} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX_TAG} "
        f"audit_sha256={audit_sha256} content_sha256={content_sha256} "
        f"schema_version={SCHEMA_VERSION}"
    )                                                                          # (local)
    short_a = audit_sha256[:16]                                                # (local)
    short_c = content_sha256[:16]                                              # (local)
    dual_sha = (
        f"# audit_sha256_short={short_a} content_sha256_short={short_c} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)"
    )                                                                          # (local)
    tuple_line = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
        f"regime_verdict={regime_v} # {GATE_ID} 3-tuple annotation "
        "(S87 schema-v2)"
    )                                                                          # (local)
    with VERDICT_FILE.open("a", encoding="utf-8") as f:
        f.write(canon_line + "\n")
        f.write(dual_sha + "\n")
        f.write(tuple_line + "\n")


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------


def main() -> int:
    print("=" * 72)
    print(f"{GATE_ID}  —  S87 W5-5 / CF-35  —  forward template adoption")
    print("=" * 72)

    # Pre-edit input SHAs (immutable references; computed BEFORE the edit
    # so audit_sha256 closes over the inputs, not the output).
    pre_edit_anatomy_sha = sha256_file(RULE_BRIDGE_ANATOMY)                    # (local)
    inheritance_sha = sha256_file(RULE_INHERITANCE)                            # (local)
    agent_std_sha = sha256_file(RULE_AGENT_STD)                                # (local)
    registry_sha = sha256_file(REGISTRY_PERM)                                  # (local)

    print(f"Input SHA pins (pre-edit):")
    print(f"  cross-pillar-bridge-anatomy.md     = {pre_edit_anatomy_sha}")
    print(f"  inheritance-falsifier-protocol.md  = {inheritance_sha}")
    print(f"  agent-standards.md                 = {agent_std_sha}")
    print(f"  permanent-results-registry.md      = {registry_sha}")
    print()
    print(f"Substitution chain (K-counter):")
    print(f"  K  = {K_CALIBRATION_INSTANCES}  (W-5 instance #1)")
    print(f"  K_promotion = {K_PROMOTION_THRESHOLD}  (agent-standards.md)")
    print(
        f"  K < K_promotion  =>  status = {STATUS_PIN}  "
        f"(K=1 < 3 ⇒ SUGGESTION not MANDATORY)"
    )
    print()

    # Draft SUGGESTION text (deterministic; bit-exact from CANDIDATES list).
    suggestion_text = draft_suggestion_text()
    print(f"Drafted SUGGESTION clause: {len(suggestion_text)} chars; "
          f"{suggestion_text.count(chr(10))} lines.")

    # Apply edit (idempotent — no-op if already present, overwrite if diverged).
    edit_action, post_state = append_suggestion_clause(suggestion_text)
    print(f"Edit action: {edit_action}; post-edit length={len(post_state)} chars.")

    # Re-read post-edit anatomy SHA + verification grep.
    post_edit_anatomy_sha = sha256_file(RULE_BRIDGE_ANATOMY)                   # (local)
    verification = verify_post_edit_state(post_state)
    print(f"Post-edit verification:")
    for k, v in verification.items():
        print(f"  {k}: {v}")

    # Composite verdict (S87+ schema-v2 collapse rule):
    #   - sign_verdict     = N/A (no signed delta; absolute text-presence test)
    #   - magnitude_verdict = PASS iff ALL_4_PASS_CRITERIA_MET; FAIL otherwise
    #   - regime_verdict   = VALID (no numerical regime; pure structural test)
    sign_v = "N/A"                                                             # (local)
    mag_v = "PASS" if verification["ALL_4_PASS_CRITERIA_MET"] else "FAIL"      # (local)
    regime_v = "VALID"                                                         # (local)

    # Apply collapse rule (gate-verdicts.md §"Composite-collapse rule"):
    if regime_v == "BREAKDOWN":
        composite = "FAIL"                                                     # (local)
    elif sign_v == "FAIL":
        composite = "FAIL"
    elif mag_v == "FAIL" and regime_v == "VALID":
        composite = "FAIL"
    elif mag_v == "FAIL" and regime_v == "MARGINAL":
        composite = "INFO"
    elif mag_v == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"
    print(f"Composite collapse: sign={sign_v} mag={mag_v} regime={regime_v}"
          f"  ⇒  composite={composite}")

    # Build input-pin map for audit_sha256 (closes over PRE-EDIT inputs +
    # gate identity keys + machinery pin map).
    pin_map = {                                                                # (local)
        "_gate_id": GATE_ID,
        "_wp_id": "S87-W5-5",
        "_scheme": SCHEME,
        "_convention": CONVENTION,
        "_L_max": L_MAX_TAG,
        "K_calibration_instances": K_CALIBRATION_INSTANCES,
        "K_promotion_threshold": K_PROMOTION_THRESHOLD,
        "status_pin": STATUS_PIN,
        "n_candidates": len(CANDIDATES),
        "candidate_ids": [c["id"] for c in CANDIDATES],
        "input_sha_pins": {
            "cross-pillar-bridge-anatomy.md_pre_edit": pre_edit_anatomy_sha,
            "inheritance-falsifier-protocol.md": inheritance_sha,
            "agent-standards.md": agent_std_sha,
            "permanent-results-registry.md": registry_sha,
        },
        "schema_version": SCHEMA_VERSION,
    }
    audit_sha = closure_hash(pin_map)                                          # (local)
    content_sha = content_hash(suggestion_text)                                # (local)

    print(f"audit_sha256   = {audit_sha}")
    print(f"content_sha256 = {content_sha}")

    # Value string encodes the verification 4-tuple in PASS-band form.
    value_str = (
        "'forward_template_landed=1.0_C1=" + str(int(verification["C1_suggestion_clause_present"]))
        + "_C2=" + str(int(verification["C2_rank2_xref_present"]))
        + "_C3=" + str(int(verification["C3_three_candidates_enumerated"]))
        + "_C4=" + str(int(verification["C4_status_SUGGESTION_declared"]))
        + "_K=1_K_promotion=3'"
    )                                                                          # (local)

    # Emit verdict line + dual-SHA companion + 3-tuple companion.
    append_verdict_block(
        composite=composite,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        sign_v=sign_v,
        mag_v=mag_v,
        regime_v=regime_v,
        value_str=value_str,
    )
    print(f"Verdict line trio appended to {VERDICT_FILE.name}.")

    # JSON sidecar.
    sidecar = {                                                                # (local)
        "gate_id": GATE_ID,
        "wp_section": "§W5-5",
        "session": "S87",
        "wave": "W5-5",
        "carry_forward": "CF-35",
        "owner": "volovik-superfluid-universe-theorist",
        "co_signer": "connes-ncg-theorist",
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX_TAG,
        "schema_version": SCHEMA_VERSION,
        "K_substitution_chain": {
            "K_calibration_instances": K_CALIBRATION_INSTANCES,
            "K_promotion_threshold": K_PROMOTION_THRESHOLD,
            "K_lt_K_promotion": K_CALIBRATION_INSTANCES < K_PROMOTION_THRESHOLD,
            "status_pin": STATUS_PIN,
            "step1_definition": "K = count of distinct high-density workshops invoking template",
            "step2_substitute": f"K = {K_CALIBRATION_INSTANCES}; K_promotion = {K_PROMOTION_THRESHOLD}",
            "step3_form": f"K ({K_CALIBRATION_INSTANCES}) < K_promotion ({K_PROMOTION_THRESHOLD})",
            "step4_canonical": "1 < 3 (integer; bit-exact)",
            "step5_direction": "K < K_promotion ⇒ status = SUGGESTION (NOT MANDATORY)",
        },
        "input_sha_pins": pin_map["input_sha_pins"],
        "post_edit_anatomy_sha": post_edit_anatomy_sha,
        "post_edit_action": edit_action,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "audit_sha256_short": audit_sha[:16],
        "content_sha256_short": content_sha[:16],
        "verification_checks": verification,
        "composite_verdict": composite,
        "three_tuple_verdict": {
            "sign_verdict": sign_v,
            "magnitude_verdict": mag_v,
            "regime_verdict": regime_v,
        },
        "candidates": CANDIDATES,
        "drafted_suggestion_text": suggestion_text,
        "pass_criteria": {
            "C1_suggestion_text_landed": (
                "Forward template-adoption SUGGESTION text landed in "
                ".claude/rules/cross-pillar-bridge-anatomy.md listing W-5 "
                "as instance #1"
            ),
            "C2_rank2_generalization_xref": (
                "inheritance-falsifier-protocol.md §Generalization beyond "
                "3He-B (W-5 Q8) cross-referenced"
            ),
            "C3_two_to_three_candidates": (
                "2-3 candidate forward bridge pairs explicitly enumerated "
                "with substrate-IS / laboratory-IN identifications"
            ),
            "C4_suggestion_not_mandatory": (
                "SUGGESTION-not-MANDATORY status declared (K=1 calibration; "
                "awaits N=3 promotion)"
            ),
        },
        "value_str": value_str,
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    }
    JSON_SIDECAR.write_text(json.dumps(sidecar, indent=2), encoding="utf-8")
    print(f"JSON sidecar written: {JSON_SIDECAR.name} ({JSON_SIDECAR.stat().st_size} bytes).")

    print("=" * 72)
    print(f"DONE.  composite={composite}   "
          f"4_PASS_criteria_met={verification['ALL_4_PASS_CRITERIA_MET']}")
    print("=" * 72)
    return 0


if __name__ == "__main__":
    sys.exit(main())
