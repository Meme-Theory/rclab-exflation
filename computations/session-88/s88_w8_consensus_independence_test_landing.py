#!/usr/bin/env python3
"""
S88 W8-87 — S88-CONSENSUS-INDEPENDENCE-TEST-LANDING
====================================================

Gate: S88-CONSENSUS-INDEPENDENCE-TEST-LANDING ([VERIFY])

METHODOLOGY-class wave per .claude/rules/wave-classification.md M1-M4:
  M1: artifact-existence PASS predicate (rule-file edit lands the
      Hybrid Independence Test sub-section + retroactive §VII.AG.1
      tagging + K-counter table annotation; allowlist row appended).
  M2: Edit-only on .claude/rules/cross-pillar-bridge-anatomy.md and
      .claude/rules/methodology-wave-allowlist.md. No numerical
      computation.
  M3: Source = plan §W8-87 hypothesis + substitution chain (Steps 1–5
      verbatim) + S87 W6-1 STAGE-1-CANDIDATE landing of §VII.AG.1
      quotient-functor isomorphism modulo cyclic-fold V_4.
  M4: Allowlist row appended in this script.

Pre-registered threshold (from plan §W8-87):
  PASS iff
    (a) cross-pillar-bridge-anatomy.md contains §"Hybrid Independence
        Test" sub-section with all four clauses (i/ii/iii/iv) verbatim
    (b) §VII.AG.1 retroactive tag SHARED-ANCHOR-COMPANION + PARTIAL-
        AXES-INSTANCE present
    (c) calibration-corpus K-counter table reflects the Independence
        Test verdict on §VII.AG.1 (companion entry, not counted in K)
    (d) allowlist row W8-87 appended
    (e) substantive line count >= 15 in the new sub-section.

Inputs (SHA-256 dual-pinned at runtime):
  - .claude/rules/cross-pillar-bridge-anatomy.md (PRE-edit state)
  - .claude/rules/methodology-wave-allowlist.md (PRE-edit state)
  - sessions/permanent-results-registry.md (read-only reference)
  - sessions/session-plan/session-88-plan-w8.md (plan-block source)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<five-clause-status>, scheme=METHODOLOGY-rule-file-edit,
   convention=hybrid-independence-test-i-ii-iii-AND-iv, L_max=N/A)

Classification: METHODOLOGY (M1-M4 per .claude/rules/wave-classification.md)

Stale-source disclosure (Class-(c) PIN-DRIFT-FROM-STALE-SOURCE per
.claude/rules/epistemic-discipline.md §"Source Reconciliation"):
  Plan §W8-87 threshold (c) literally reads "K-counter table updated to
  K=1 (W-5 only)". This wording was authored before S88 W4a-17 close
  (2026-05-04) which legitimately advanced K to 3 (W-5 + W11-5 + W4a-17)
  and promoted SUGGESTION → MANDATORY. Reverting K=3 → K=1 would be
  PROHIBITED_ACTIONS Class 3 (post-hoc pre-registration editing) per
  v3-closure-recovery.md. The honest closure: insert the Independence
  Test sub-section AHEAD of the existing K=3 corpus block, apply the
  retroactive §VII.AG.1 tag (SHARED-ANCHOR-COMPANION + PARTIAL-AXES-
  INSTANCE) explicitly OUTSIDE the K-counter, and annotate the
  calibration-corpus table with a "Companion entries (excluded from K
  by Independence Test)" sub-section. The plan's underlying STRUCTURAL
  intent — that §VII.AG.1 not advance K — is preserved exactly: §VII.AG.1
  was never in the K-counter table to begin with (rows are W-5/W11-5/
  W4a-17). The Independence Test now formalizes WHY.
"""

from __future__ import annotations

import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403  (per math-scripts.md MANDATORY)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION = "S88"                                                     # (local)
GATE_ID = "S88-CONSENSUS-INDEPENDENCE-TEST-LANDING"                 # (local)
SCHEME = "METHODOLOGY-rule-file-edit"                               # (local)
CONVENTION = "hybrid-independence-test-i-ii-iii-AND-iv"             # (local)
L_MAX = "N/A"                                                       # (local)

CROSS_PILLAR_PATH = (
    PROJECT_ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md"
)
ALLOWLIST_PATH = (
    PROJECT_ROOT / ".claude" / "rules" / "methodology-wave-allowlist.md"
)
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
PLAN_PATH = (
    PROJECT_ROOT / "sessions" / "session-plan" / "session-88-plan-w8.md"
)
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"
VERDICT_TXT = SESSION_DIR / "s88_gate_verdicts.txt"
OUT_JSON = SESSION_DIR / "s88_w8_consensus_independence_test_landing.json"

INPUT_FILES = [
    CROSS_PILLAR_PATH,    # PRE-edit state
    ALLOWLIST_PATH,       # PRE-edit state
    REGISTRY_PATH,
    PLAN_PATH,
    CANONICAL_PATH,
]

# ---------------------------------------------------------------------------
# Section 4 — SHA-256 helpers
# ---------------------------------------------------------------------------

def sha256_of_bytes(b: bytes) -> str:
    h = hashlib.sha256()
    h.update(b)
    return h.hexdigest()


def sha256_of(path: Path) -> str:
    try:
        return sha256_of_bytes(path.read_bytes())
    except OSError:
        return ""


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins (PRE-edit) ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
    """S84+ dual-SHA schema."""
    script_bytes = b""                             # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""                          # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")                              # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                    # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()                # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Plan-block SHA over plan §W8-87 (lines 43–78)
# ---------------------------------------------------------------------------

def plan_block_sha(plan_path: Path) -> str:
    """SHA-256 over plan §W8-87 block (header line through next '---'-only line).

    Per .claude/rules/methodology-wave-allowlist.md Schema, the
    sha256_of_plan_block field is computed via closure_hash(plan_block_text).
    Here we compute SHA-256 of the literal byte slice of the block.
    """
    text = plan_path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    start = None                                   # (local)
    for i, line in enumerate(lines):
        if line.startswith("## §W8-87 "):
            start = i
            break
    if start is None:
        return ""
    end = len(lines)                               # (local)
    for j in range(start + 1, len(lines)):
        if lines[j].startswith("## §W8-"):
            end = j
            break
    block = "".join(lines[start:end])              # (local)
    return sha256_of_bytes(block.encode("utf-8"))


# ---------------------------------------------------------------------------
# Section 6 — Rule-file edits
# ---------------------------------------------------------------------------

# The 4-clause Independence Test sub-section to insert into
# cross-pillar-bridge-anatomy.md AFTER the §"Forward template-adoption"
# header but BEFORE the "### Status: MANDATORY at K=3" line so it
# governs (forward-looking) the K-counter discipline declared below it.

INDEPENDENCE_TEST_SUBSECTION = """### Hybrid Independence Test (S88 W8-87 RULE-EXTENSION)

> **Provenance**: S88 W8-87 (gen-physicist orchestrator + lizzi-spectral-functional-theorist CO-AUTHOR rationale review). Verdict line at `computations/session-88/s88_gate_verdicts.txt`. Closes the silent narrative-inflation pathway by which a §VII registry entry citing the 5-IS-not-IN + 3-level discipline could naively advance K without structural-independence verification.

#### Status: SUGGESTION at K=1 (forward-looking from S88 W8-87 close, 2026-05-05)

A calibration corpus instance counts toward the K-counter (per `cross-pillar-bridge-anatomy.md §"Forward template-adoption"`) iff it satisfies the **Hybrid Independence Test** `(i ∨ ii ∨ iii) ∧ iv`:

- **(i)** distinct **substrate-IS pillar** from prior K-instances (Pillar I / II / III / IV / V / VI / VII)
- **(ii)** distinct **laboratory-IN pillar** from prior K-instances
- **(iii)** distinct **bridge map class** (HKR / Connes-Karoubi pairing / K-theory boundary) from prior K-instances
- **(iv)** **independent algebraic envelope** (the Level-2 envelope is NOT a numerical refinement of an existing K-instance's envelope — refinements that share the same regulator-invariant structural form do NOT count as independent)

The **disjunction `(i ∨ ii ∨ iii)`** captures structural diversity along ANY of the three substrate-axis-/-lab-axis-/-bridge-axis dimensions; the **conjunction with (iv)** enforces that the algebraic envelope itself is structurally independent — purely numerical refinements of an existing envelope do NOT advance K, even if they happen to land on different §VII slots.

#### Companion-entry tagging (retroactive)

Registry entries that cite the 5-IS-not-IN + 3-level discipline but FAIL the Hybrid Independence Test are formally tagged `SHARED-ANCHOR-COMPANION + PARTIAL-AXES-INSTANCE` and recorded OUTSIDE the K-counter table. They retain full registry-entry status (the bridge-anatomy declaration remains valid for cross-citation purposes) but do NOT advance the K-counter toward the K=3 MANDATORY promotion threshold.

#### Calibration corpus (K=1 at S88 W8-87)

| # | Registry entry | Substrate-IS pillar | Lab-IN pillar | Bridge map class | Algebraic envelope | (i) ∨ (ii) ∨ (iii) | (iv) | Independent? |
|:-:|:---------------|:--------------------|:--------------|:-----------------|:-------------------|:-------------------:|:----:|:------------:|
| 1 | §VII.AF.1 (S87 W5-1 / S86 W-5) | Pillar III (HP^1 cohomology on `(A_K^{≤L}, H_K^{≤L}, D_K^{≤L})`) | Pillar IV (Peotta-Törmä BZ-trace `R_geom`) | HKR `L_max → ∞` | `L^{-3}` at d=4 | (baseline) | (baseline) | **YES** (calibration #1) |
| Companion | §VII.AG.1 (S87 W6-1) | Pillar III (T7 cyclic-fold quotient on `(A_K^{≤L}, H_K^{≤L}, D_K^{≤L})`) | Pillar IV (S67 cyclic-fold image) | HKR `L_max → ∞` modulo cyclic-fold V_4 quotient | `L^{-3}` at d=4 (refinement of W-5 envelope under V_4 cyclic-fold quotient) | (i)=FAIL same Pillar III; (ii)=FAIL same Pillar IV; (iii)=FAIL same HKR class (V_4 quotient is REFINEMENT not new class) | (iv)=FAIL envelope is V_4-quotient REFINEMENT of W-5 `L^{-3}`, NOT independent | **NO** — tagged `SHARED-ANCHOR-COMPANION + PARTIAL-AXES-INSTANCE`; OUTSIDE K-counter |

#### Substitution chain — §VII.AG.1 evaluation

(Per `.claude/rules/math-scripts.md §"Double-Check Logic"`; reproduces plan §W8-87 Steps 1–5.)

- **Step 1** (Definition): K-counter advancement threshold = N=3 promotion to MANDATORY per `feedback_rules-compensate-missing-structure.md`.
- **Step 2** (Definition): "Distinct calibration instance" PRE-Hybrid-Independence-Test = each §VII registry entry citing the 5-IS-not-IN + 3-level discipline naively counted as one K-instance.
- **Step 3** (Substitution under `(i ∨ ii ∨ iii) ∧ iv`):
  - §VII.AG.1 substrate-IS pillar = Pillar III (T7 quotient on Jensen-deformed band-0 sector); §VII.AF.1 W-5 substrate-IS pillar = Pillar III (HP^1 cohomology on same sector). **MATCH ⇒ clause (i) FAILS.**
  - §VII.AG.1 laboratory-IN pillar = Pillar IV (S67 cyclic-fold image); §VII.AF.1 W-5 laboratory-IN pillar = Pillar IV (Peotta-Törmä BZ-trace). **MATCH ⇒ clause (ii) FAILS.**
  - §VII.AG.1 bridge map = HKR `L_max → ∞` modulo cyclic-fold V_4 (a quotient-functor REFINEMENT of W-5's HKR map); §VII.AF.1 W-5 bridge map = HKR `L_max → ∞`. The cyclic-fold V_4 quotient is a refinement of the same HKR class, not a structurally distinct bridge map class. **REFINEMENT-NOT-INDEPENDENT ⇒ clause (iii) FAILS.**
  - Disjunction `(i ∨ ii ∨ iii) = (FAIL ∨ FAIL ∨ FAIL) = FALSE`.
- **Step 4** (Simplify): Conjunction `FALSE ∧ iv = FALSE` regardless of clause (iv). §VII.AG.1 fails the Hybrid Independence Test.
- **Step 5** (Direction): K-counter does NOT advance for §VII.AG.1; therefore §VII.AG.1 is OUTSIDE the K-counter and gets the retroactive tag `SHARED-ANCHOR-COMPANION + PARTIAL-AXES-INSTANCE`. The K-counter advancement at S87 W6-1 close was naive narrative inflation that the Independence Test now formally excludes.

#### Conclusion

The retroactive tag `SHARED-ANCHOR-COMPANION + PARTIAL-AXES-INSTANCE` correctly classifies §VII.AG.1 outside the K-counter, preserving the structural integrity of the K-counter advancement (the K=3 corpus declared in §"Status: MANDATORY at K=3" below remains W-5 + W11-5 + W4a-17 — all of which ARE independent under the Hybrid Independence Test by their distinct substrate-IS pillars and/or distinct lab-IN pillars and/or distinct bridge map classes). The Hybrid Independence Test enforces that K-counter promotion to MANDATORY tracks ONLY structurally-independent calibration instances; narrative inflation cannot drive premature MANDATORY-status.

#### Forward enforcement (post-S88 W8-87)

- **Plan-freeze halt** on any S88+ K-counter advancement that does not document a per-clause Hybrid Independence Test verdict for the new instance.
- **Audit-script extension** queued for `computations/_shared/_cross_pillar_bridge_audit.py` (S86 W-5 AUDIT-1 SCAFFOLD; existing post-W7a-73 with OE-form regex extension): forward extension to verify that any S88+ K-counter row provides per-clause Independence Test pin (i/ii/iii/iv).
- **K-counter K=1 in this sub-section** refers to the calibration-corpus state UNDER the Hybrid Independence Test as a stand-alone discipline (W-5 alone is the calibration baseline for the test itself); it does NOT supersede the K=3 MANDATORY corpus declared in `§"Status: MANDATORY at K=3"` below, which was independently advanced via S88 W4a-17 close (2026-05-04) under the prior K-counter rules. The two are not in conflict: the post-W4a-17 K=3 advancement IS consistent with the Hybrid Independence Test (W-5, W11-5, W4a-17 each satisfy `(i ∨ ii ∨ iii) ∧ iv`).

"""


def insert_independence_test_subsection(text: str) -> tuple[str, bool]:
    """Insert §"Hybrid Independence Test" sub-section AFTER the
    `## Forward template-adoption (calibration-corpus tracking)` header
    line and BEFORE the existing `### Status: MANDATORY at K=3` line.

    Returns (new_text, did_change).
    """
    if "### Hybrid Independence Test (S88 W8-87 RULE-EXTENSION)" in text:
        return text, False  # idempotent: already inserted

    anchor = "## Forward template-adoption (calibration-corpus tracking)"
    insertion_point_marker = "### Status: MANDATORY at K=3 (promoted from SUGGESTION at S88 W4a-17 close, 2026-05-04)"

    if anchor not in text:
        raise RuntimeError(
            f"Anchor not found in cross-pillar-bridge-anatomy.md: {anchor!r}"
        )
    if insertion_point_marker not in text:
        raise RuntimeError(
            f"Insertion-point marker not found: {insertion_point_marker!r}"
        )

    # Insert the new sub-section immediately BEFORE the
    # "### Status: MANDATORY at K=3" line.
    new_text = text.replace(
        insertion_point_marker,
        INDEPENDENCE_TEST_SUBSECTION + insertion_point_marker,
    )
    return new_text, True


def append_allowlist_row(
    allowlist_text: str,
    sha_of_plan_block: str,
) -> tuple[str, bool]:
    """Append the W8-87 allowlist row.

    Schema (per .claude/rules/methodology-wave-allowlist.md):
      gate_id | session | rationale | sha256_of_plan_block

    Idempotent: if a W8-87 row already exists, return unchanged.
    """
    if "| W8-87 |" in allowlist_text:
        return allowlist_text, False

    # Append-only: add to end of file (after final allowlist row).
    rationale = (
        "S88-CONSENSUS-INDEPENDENCE-TEST-LANDING "
        "(cross-pillar-bridge-anatomy.md §\"Forward template-adoption\" "
        "extended with new §\"Hybrid Independence Test\" sub-section "
        "specifying `(i ∨ ii ∨ iii) ∧ iv` calibration-instance "
        "independence test on substrate-IS pillar / laboratory-IN pillar / "
        "bridge map class disjunction with independent algebraic envelope "
        "conjunction; retroactive §VII.AG.1 tagging "
        "SHARED-ANCHOR-COMPANION + PARTIAL-AXES-INSTANCE classifying it "
        "OUTSIDE the K-counter; 5-step substitution chain on Hybrid "
        "Independence Test against §VII.AG.1 reproduced verbatim from plan "
        "§W8-87 Steps 1–5; preserves K=3 MANDATORY corpus advanced via "
        "S88 W4a-17 close (2026-05-04) intact — Hybrid Independence Test "
        "is forward-looking discipline at SUGGESTION K=1 with W-5 baseline; "
        "future K-counter advancements MUST document per-clause Independence "
        "Test verdict; M1-M4 conjunction satisfied [M1 artifact-existence on "
        "rule-file diff; M2 Edit on .claude/rules/cross-pillar-bridge-anatomy.md; "
        "M3 verbatim from plan §W8-87 Steps 1–5 substitution chain + S87 W6-1 "
        "STAGE-1-CANDIDATE landing; M4 allowlist append herewith]; "
        "orchestrator-direct-write per wave-classification.md §\"Dispatch "
        "consequences\"; gen-physicist orchestrator PRIMARY + "
        "lizzi-spectral-functional-theorist CO-AUTHOR rationale review)"
    )

    new_row = f"| W8-87 | S88     | {rationale} | {sha_of_plan_block} |\n"

    # Append after the last existing row (the file is append-only;
    # any trailing newline structure is preserved).
    if not allowlist_text.endswith("\n"):
        allowlist_text = allowlist_text + "\n"
    new_text = allowlist_text + new_row
    return new_text, True


# ---------------------------------------------------------------------------
# Section 7 — Verdict-line emission (atomic append per gate-verdicts.md)
# ---------------------------------------------------------------------------

def append_verdict(
    verdict: str,
    value: str,
    audit_sha: str,
    content_sha: str,
) -> None:
    """Append canonical verdict line + dual-SHA companion comment row.

    METHODOLOGY-class wave: no `[SIGN]` trigger ⇒ no 3-tuple companion
    row required (plan §W8-87 has no directional pre-registration).
    """
    canonical = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} # {GATE_ID} dual-SHA "
        f"companion row (W9a-99 split); METHODOLOGY-class per "
        f"wave-classification.md M1-M4; rule-file edit on "
        f".claude/rules/cross-pillar-bridge-anatomy.md inserts "
        f"§\"Hybrid Independence Test\" sub-section + retroactive "
        f"§VII.AG.1 tag SHARED-ANCHOR-COMPANION + PARTIAL-AXES-INSTANCE; "
        f"allowlist row W8-87 appended; orchestrator-direct-write\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical)
        fp.write(companion)


# ---------------------------------------------------------------------------
# Section 8 — Threshold evaluation (5-clause)
# ---------------------------------------------------------------------------

def evaluate_threshold(
    cross_pillar_post_text: str,
    allowlist_post_text: str,
) -> tuple[str, dict]:
    """Evaluate plan §W8-87 threshold (a)..(e). Returns (verdict, breakdown).

    Threshold:
      PASS iff (a) Hybrid Independence Test sub-section present with all
      four clauses (i/ii/iii/iv) verbatim AND
      (b) §VII.AG.1 retroactive tag SHARED-ANCHOR-COMPANION +
      PARTIAL-AXES-INSTANCE present AND
      (c) calibration-corpus K-counter table reflects the Independence
      Test verdict on §VII.AG.1 AND
      (d) allowlist row appended AND
      (e) substantive line count >= 15 in the new sub-section.
    """
    breakdown: dict = {}                                                  # (local)

    # Clause (a): all four Independence Test clauses verbatim
    clause_a_markers = [
        "### Hybrid Independence Test (S88 W8-87 RULE-EXTENSION)",
        "**(i)** distinct **substrate-IS pillar**",
        "**(ii)** distinct **laboratory-IN pillar**",
        "**(iii)** distinct **bridge map class**",
        "**(iv)** **independent algebraic envelope**",
    ]
    a_present = all(m in cross_pillar_post_text for m in clause_a_markers) # (local)
    breakdown["a_independence_test_subsection_with_four_clauses"] = a_present

    # Clause (b): retroactive §VII.AG.1 tag
    b_markers = [
        "§VII.AG.1",
        "SHARED-ANCHOR-COMPANION + PARTIAL-AXES-INSTANCE",
    ]
    b_present = all(m in cross_pillar_post_text for m in b_markers)        # (local)
    breakdown["b_VII_AG_1_retroactive_tag"] = b_present

    # Clause (c): calibration-corpus K-counter table reflects the
    # Independence Test verdict on §VII.AG.1 (companion entry).
    c_markers = [
        "Calibration corpus (K=1 at S88 W8-87)",
        "Companion |",  # the "Companion" row in the K=1 corpus table
        "OUTSIDE K-counter",
    ]
    c_present = all(m in cross_pillar_post_text for m in c_markers)        # (local)
    breakdown["c_K_counter_table_updated_companion_entry"] = c_present

    # Clause (d): allowlist row appended
    d_present = "| W8-87 |" in allowlist_post_text                         # (local)
    breakdown["d_allowlist_row_appended"] = d_present

    # Clause (e): >= 15 substantive lines in the new sub-section
    start_marker = "### Hybrid Independence Test (S88 W8-87 RULE-EXTENSION)"
    end_marker = (
        "### Status: MANDATORY at K=3 (promoted from SUGGESTION at S88 "
        "W4a-17 close, 2026-05-04)"
    )
    if start_marker in cross_pillar_post_text and end_marker in cross_pillar_post_text:
        lo = cross_pillar_post_text.index(start_marker)                    # (local)
        hi = cross_pillar_post_text.index(end_marker)                      # (local)
        block = cross_pillar_post_text[lo:hi]                              # (local)
        substantive_lines = sum(                                           # (local)
            1 for ln in block.splitlines()
            if ln.strip()
            and not ln.strip().startswith("#")
            and not ln.strip().startswith("|")
            and not ln.strip().startswith("```")
        )
        e_present = substantive_lines >= 15                                # (local)
    else:
        substantive_lines = 0                                              # (local)
        e_present = False                                                  # (local)
    breakdown["e_substantive_line_count_geq_15"] = e_present
    breakdown["e_substantive_line_count_value"] = substantive_lines

    all_pass = a_present and b_present and c_present and d_present and e_present
    verdict = "PASS" if all_pass else "FAIL"
    return verdict, breakdown


# ---------------------------------------------------------------------------
# Section 9 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()                                                       # (local)

    # 1. Log PRE-edit input pins (canonical SHAs feed audit_sha256)
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)                                           # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. Compute plan-block SHA over plan §W8-87 (allowlist row pin source)
    plan_sha = plan_block_sha(PLAN_PATH)                                   # (local)
    print(f"  plan_block_sha (§W8-87): {plan_sha[:16]}... ({plan_sha})")

    # 1c. Compute S84+ dual SHAs (script bytes + canonical + pinmap)
    script_path = Path(__file__).resolve()                                 # (local)
    audit_sha, content_sha = compute_dual_sha(
        script_path, CANONICAL_PATH, pins
    )
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Apply rule-file edits
    cross_pillar_pre = CROSS_PILLAR_PATH.read_text(encoding="utf-8")       # (local)
    cross_pillar_post, cp_changed = insert_independence_test_subsection(
        cross_pillar_pre
    )
    if cp_changed:
        CROSS_PILLAR_PATH.write_text(cross_pillar_post, encoding="utf-8")
        print(
            f"[cross-pillar-bridge-anatomy.md] Inserted §\"Hybrid "
            f"Independence Test\" sub-section ({len(cross_pillar_post) - len(cross_pillar_pre)} bytes added)."
        )
    else:
        print(
            "[cross-pillar-bridge-anatomy.md] §\"Hybrid Independence "
            "Test\" sub-section already present (idempotent re-run)."
        )

    allowlist_pre = ALLOWLIST_PATH.read_text(encoding="utf-8")             # (local)
    allowlist_post, al_changed = append_allowlist_row(allowlist_pre, plan_sha)
    if al_changed:
        ALLOWLIST_PATH.write_text(allowlist_post, encoding="utf-8")
        print(
            f"[methodology-wave-allowlist.md] Appended W8-87 row "
            f"({len(allowlist_post) - len(allowlist_pre)} bytes added)."
        )
    else:
        print(
            "[methodology-wave-allowlist.md] W8-87 row already present "
            "(idempotent re-run)."
        )

    # 3. Compute POST-edit SHAs (for the JSON record + audit cross-check)
    cross_pillar_post_sha = sha256_of(CROSS_PILLAR_PATH)                   # (local)
    allowlist_post_sha = sha256_of(ALLOWLIST_PATH)                         # (local)
    print()
    print(f"  cross-pillar-bridge-anatomy.md POST-edit SHA: {cross_pillar_post_sha}")
    print(f"  methodology-wave-allowlist.md POST-edit SHA:  {allowlist_post_sha}")

    # 4. Re-read POST-edit text for threshold verification
    cross_pillar_post_text = CROSS_PILLAR_PATH.read_text(encoding="utf-8") # (local)
    allowlist_post_text = ALLOWLIST_PATH.read_text(encoding="utf-8")       # (local)

    # 5. Evaluate threshold (5 clauses)
    verdict, breakdown = evaluate_threshold(
        cross_pillar_post_text, allowlist_post_text
    )
    print()
    print(f"=== Threshold breakdown ===")
    for k, v in breakdown.items():
        print(f"  {k}: {v}")
    print()

    # 6. Build the value string for the verdict line
    value_str = (
        f"a={breakdown['a_independence_test_subsection_with_four_clauses']};"
        f"b={breakdown['b_VII_AG_1_retroactive_tag']};"
        f"c={breakdown['c_K_counter_table_updated_companion_entry']};"
        f"d={breakdown['d_allowlist_row_appended']};"
        f"e={breakdown['e_substantive_line_count_geq_15']}"
        f"_substantive_lines={breakdown['e_substantive_line_count_value']};"
        f"K_post_S88_W8_87=1_SUGGESTION_independence_test_baseline_W5;"
        f"K_corpus_below_unchanged=3_MANDATORY_W5_W11_5_W4a_17"
    )
    tag = (
        f"(value={value_str!r}, scheme={SCHEME}, convention={CONVENTION}, "
        f"L_max={L_MAX})"
    )
    print(tag)

    # 7. Append canonical verdict + companion row
    append_verdict(verdict, value_str, audit_sha, content_sha)

    # 8. Emit JSON sidecar pinning before/after SHAs
    json_payload = {
        "gate_id": GATE_ID,
        "verdict": verdict,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "plan_block_sha256_W8_87": plan_sha,
        "input_pins_pre_edit": pins,
        "cross_pillar_bridge_anatomy_md_post_edit_sha256": cross_pillar_post_sha,
        "methodology_wave_allowlist_md_post_edit_sha256": allowlist_post_sha,
        "threshold_breakdown": breakdown,
        "value_string": value_str,
        "wave_class": "METHODOLOGY",
        "M1_M4_satisfied": True,
        "stale_source_disclosure": (
            "Plan §W8-87 threshold (c) literal wording 'K-counter table "
            "updated to K=1 (W-5 only)' is Class-(c) PIN-DRIFT-FROM-STALE-"
            "SOURCE per epistemic-discipline.md §Source Reconciliation: "
            "plan was authored before S88 W4a-17 close (2026-05-04) which "
            "advanced K to 3. Honest closure: §VII.AG.1 retroactively "
            "tagged OUTSIDE K-counter; K=3 corpus block (S88 W4a-17 "
            "advancement) preserved intact; Hybrid Independence Test "
            "lands as forward-looking discipline at SUGGESTION K=1. The "
            "post-W4a-17 K=3 advancement IS consistent with the Hybrid "
            "Independence Test (W-5 / W11-5 / W4a-17 each satisfy "
            "(i ∨ ii ∨ iii) ∧ iv); the structural intent of plan §W8-87 "
            "(§VII.AG.1 outside K-counter) is preserved exactly."
        ),
    }
    OUT_JSON.write_text(
        json.dumps(json_payload, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    print(f"\n[json] {OUT_JSON.relative_to(PROJECT_ROOT)}")

    wall = time.time() - t0                                                # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
