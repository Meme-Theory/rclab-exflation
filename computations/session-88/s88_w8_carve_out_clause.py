#!/usr/bin/env python3
"""
S88 W8-89 — S88-MECHANICAL-CLOSURE-DISCIPLINE-LAYER-SEPARABILITY-CARVE-OUT-CLAUSE
================================================================================

Gate: S88-MECHANICAL-CLOSURE-DISCIPLINE-LAYER-SEPARABILITY-CARVE-OUT-CLAUSE  ([AUDIT])

METHODOLOGY-class wave per `.claude/rules/wave-classification.md` §M1-M4:
  M1 — PASS predicate is artifact-existence-with-substantive-content; the
       carve-out clause must (a)-(f) be present in the rule-file, the
       allowlist row must be appended, and the substantive-line-count
       on the new section must be >= 15. NO numerical comparison.
  M2 — Producing operations are restricted to (i) Edit/Write on the two
       targeted rule-files, (ii) grep / regex cross-checks for clause
       presence + line counts, (iii) SHA-256 input pinning (script +
       canonical_constants.py + rule-files BEFORE edit + final state).
       NO eigenvalue / linear algebra / FFT compute path.
  M3 — Source-of-truth is the verbatim plan-block §W8-89 of
       sessions/session-plan/session-88-plan-w8.md (lines 111-145) and
       the verbatim L1-L4 conditions enumerated therein. No first-
       principles new derivation.
  M4 — Allowlist membership: row `W8-89 | S88 | S88-MECHANICAL-CLOSURE-
       DISCIPLINE-LAYER-SEPARABILITY-CARVE-OUT-CLAUSE | <plan-block SHA>`
       is appended to .claude/rules/methodology-wave-allowlist.md as
       part of this gate's authoring run (orchestrator-only edit per
       the recursion-attack-closure protocol).

Pre-registered threshold (PASS predicate, plan §W8-89):
  PASS iff
    (a) §"Layer-separability carve-out (admissible-with-conditions)"
        section present in `.claude/rules/mechanical-closure-discipline.md`
        with all four conditions L1-L4 verbatim AND
    (b) Stage-2 cross-reviewer PASS-AND requirement specified
        (axes A=connes-spectral + B=volovik-substrate per
        joint-theorem-promotion.md §"Stage 2") AND
    (c) calibration-corpus tracking K=1 -> K=3 specified (status
        SUGGESTION at K=1; MANDATORY at K=3 per
        feedback_rules-compensate-missing-structure.md) AND
    (d) cross-link to v3-closure-recovery.md PROHIBITED_ACTIONS Class 1
        present (the carve-out is a STRUCTURAL extension; convention-tag
        honesty discipline L4 is the boundary) AND
    (e) allowlist row appended to methodology-wave-allowlist.md AND
    (f) substantive line count of the NEW carve-out section >= 15.

Inputs (SHA-256 dual-pinned at runtime):
  - .claude/rules/mechanical-closure-discipline.md (BEFORE edit; pinned
    via fresh sha256_of pre-Edit; the AFTER state is part of the
    artifact JSON)
  - .claude/rules/methodology-wave-allowlist.md (BEFORE edit)
  - .claude/rules/epistemic-discipline.md (Layer-Decomposition reference;
    pinned for input-pin map; not edited by this gate)
  - .claude/rules/joint-theorem-promotion.md (Stage 2 reference;
    pinned for input-pin map; not edited by this gate)
  - .claude/rules/cross-pillar-bridge-anatomy.md (Algebra-axis
    orthogonality reference; pinned for input-pin map; not edited)
  - canonical_constants.py (feeds audit_sha256)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=PASS|FAIL, scheme=METHODOLOGY-rule-file-edit,
   convention=layer-separability-carve-out-L1-L2-L3-L4-Stage-2-PASS-AND,
   L_max=N/A)

Classification: NON-PHONONIC (rule-file edit; substrate framing in
  prose layer of the new carve-out section enforces structural
  orthogonality at the layer-functor F level).

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- No GPU / no numerical compute
- Atomic single-shot pattern per `.claude/rules/registry-landing.md`
  §"Bridge-Landing Script Architecture (single-shot pattern)":
  build edits in memory -> apply -> fsync -> re-read -> verify ->
  emit ONE verdict line whose verdict argument is the verify boolean.
- SHA-256 of all input files logged in first ~30 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- Verdict appended to `computations/session-88/s88_gate_verdicts.txt`
  per `.claude/rules/gate-verdicts.md` canonical path.

Note: this gate AUTHORS the carve-out clause. The Stage-2 PASS-AND
coordination from connes-ncg + volovik cross-reviewers is a separate
downstream orchestrator dispatch (§W8-90 dispatches CONDITIONAL on
Stage-2 PASS-AND). This gate's PASS predicate is the rule-file edit
existing per threshold (a)-(f); Stage-2 cross-review happens AFTER
this authoring lands.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import per math-scripts.md)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403,E402

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json     # noqa: E402
import re       # noqa: E402
import time     # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration constants
# ---------------------------------------------------------------------------
SESSION = "S88"                                                                 # (local)
GATE_ID = "S88-MECHANICAL-CLOSURE-DISCIPLINE-LAYER-SEPARABILITY-CARVE-OUT-CLAUSE"  # (local)
WP_ID = "W8-89"                                                                  # (local)
SCHEME = "METHODOLOGY-rule-file-edit"                                           # (local)
CONVENTION = "layer-separability-carve-out-L1-L2-L3-L4-Stage-2-PASS-AND"        # (local)
L_MAX = "N/A"                                                                    # (local)

RULES_DIR = PROJECT_ROOT / ".claude" / "rules"                                  # (local)
RULE_FILE = RULES_DIR / "mechanical-closure-discipline.md"                      # (local)
ALLOWLIST_FILE = RULES_DIR / "methodology-wave-allowlist.md"                    # (local)
PLAN_FILE = (PROJECT_ROOT / "sessions" / "session-plan"
             / "session-88-plan-w8.md")                                         # (local)

OUT_JSON = SESSION_DIR / "s88_w8_carve_out_clause.json"                         # (local)
VERDICT_TXT = SESSION_DIR / "s88_gate_verdicts.txt"                             # (local)

# Anchor pair for insertion: NEW section between §"When mechanical
# closure IS acceptable" and §"When mechanical closure indicates a
# PLANNING DEFECT" (per plan §W8-89 method step 1).
INSERT_ANCHOR_BEFORE = "## When mechanical closure indicates a PLANNING DEFECT"  # (local)
NEW_SECTION_HEADER = "## Layer-separability carve-out (admissible-with-conditions)"  # (local)

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    RULE_FILE,
    ALLOWLIST_FILE,
    RULES_DIR / "epistemic-discipline.md",
    RULES_DIR / "joint-theorem-promotion.md",
    RULES_DIR / "cross-pillar-bridge-anatomy.md",
    RULES_DIR / "v3-closure-recovery.md",
    PLAN_FILE,
]

# ---------------------------------------------------------------------------
# Section 4 — SHA-256 dual-SHA helpers (S84+ schema)
# ---------------------------------------------------------------------------

def sha256_of_bytes(b: bytes) -> str:
    h = hashlib.sha256()
    h.update(b)
    return h.hexdigest()


def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
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
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...  (file_size={p.stat().st_size if p.exists() else 0})")
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
    """audit_sha256 = sha256(script || canonical || pinmap_json)
       content_sha256 = sha256(script)."""
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        pass
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        pass
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
# Section 5 — Build the carve-out clause text (verbatim from plan §W8-89)
# ---------------------------------------------------------------------------

CARVE_OUT_SECTION = """## Layer-separability carve-out (admissible-with-conditions)

> **Provenance**: S88 W8-89 (gen-physicist orchestrator-direct-write,
> 2026-05-05; plan source `sessions/session-plan/session-88-plan-w8.md`
> §W8-89 lines 111-145). Carve-out admissibility is **SUGGESTION** at
> K=1 (this clause); promoted to **MANDATORY** at K=3 per
> `.claude/rules/agent-standards.md` §"HIGH-DENSITY WORKSHOP TEMPLATE"
> + `feedback_rules-compensate-missing-structure.md` K-counter
> threshold. Stage-2 PASS-AND from connes-spectral + volovik-substrate
> cross-reviewers per `.claude/rules/joint-theorem-promotion.md`
> §"Stage 2" is REQUIRED before any downstream gate (the canonical
> first downstream consumer is §W8-90 `S88-CF-29-SUBSTANTIVE-RUN-VIA-
> PARTITION-CRITERION-ONLY`) is authorized to dispatch under this
> carve-out.

### Scope

The §"When mechanical closure IS acceptable" clauses 1-5 admit
mechanical-closure scripts ONLY for upstream-blocked gates with
verdict ≠ PASS (FAIL or PRE-REG-INC; never PASS). This carve-out
extends mechanical closure admissibility to a STRUCTURALLY DIFFERENT
class: **layer-separable analyses** where the layer-functor `F :
substrate → methodology → audit` (per `.claude/rules/epistemic-
discipline.md §"Layer-Decomposition"`) cleanly separates a substrate-
physics observable into a Type-F (single-summand-projection trace)
sub-observable that admits closed-form mechanical evaluation, plus a
Type-S (state-pair functional) sub-observable that requires numerical
evaluation. Mechanical closure on the Type-F sub-observable IS
admissible WITH CONDITIONS L1-L4 below; mechanical closure on the
Type-S sub-observable is NEVER admissible (state-pair functionals are
algebra-DEPENDENT per the algebra-axis orthogonality 4-corner
classification of `.claude/rules/cross-pillar-bridge-anatomy.md`
§"Algebra-axis orthogonality K-counter").

The carve-out is a STRUCTURAL extension of mechanical closure, NOT a
per-gate convention swap. The convention-tag honesty discipline L4
is the boundary that distinguishes the structural extension from
PROHIBITED_ACTIONS Class 1 (convention-shopping) per
`.claude/rules/v3-closure-recovery.md` §PROHIBITED_ACTIONS.

### Four conditions (L1-L4)

A mechanical-closure script may be authored under this carve-out
ONLY when ALL FOUR of the following conditions hold simultaneously:

- **L1 (Layer-functor cleanness)**: the substrate-physics observable
  admits a layer-functor `F` decomposition `F : substrate →
  methodology → audit` per `.claude/rules/epistemic-discipline.md`
  §"Layer-Decomposition", AND the Type-F vs Type-S partition aligns
  with the substrate ↔ methodology layer pair under `F`. Equivalently,
  the Type-F sub-observable is the substrate-physics image and the
  Type-S sub-observable is the methodology-floor image; the layer-
  functor preserves the partition by construction.

- **L2 (Type-F closed-form)**: the Type-F sub-observable admits a
  closed-form algebraic identity (canonical exemplar: a single-
  summand-projection trace `Tr_{M_n(ℂ)}(P · A)` with `P` a minimal
  central projection on `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` and `A` the observable
  expression) whose evaluation is **mechanical**: no numerical
  iteration, no random seed, no scan, no convergence loop. The
  closed-form must be evaluable bit-precision in a single-pass pure
  function on the substrate algebra.

- **L3 (Type-S separation)**: the Type-S sub-observable is
  structurally separated from the Type-F sub-observable per the
  algebra-axis orthogonality 4-corner classification of
  `.claude/rules/cross-pillar-bridge-anatomy.md` §"Algebra-axis
  orthogonality K-counter" (Type-F is algebra-INVARIANT spectrum-only
  functional; Type-S is algebra-DEPENDENT state-pair functional).
  Mechanical closure on the Type-F sub-observable does **NOT** pre-
  determine the Type-S sub-observable's verdict; the Type-S verdict
  remains a separate numerical evaluation under its own pre-
  registered threshold.

- **L4 (Honesty disclosure)**: the closure script's verdict-line
  `convention=` field MUST encode the carve-out tag explicitly,
  following the canonical pattern
  `convention=<scheme>-LAYER-SEPARABLE-CARVE-OUT-TYPE-F`. The
  corresponding working-paper section MUST include an explicit
  Type-F / Type-S separation paragraph naming the central projection
  used for the Type-F evaluation and citing the Type-S sub-observable
  routing (separate gate or PRE-REG-INC carry-forward). Failure to
  disclose either the convention tag OR the working-paper paragraph is
  a PROHIBITED_ACTIONS Class 1 violation (convention-shopping) per
  `.claude/rules/v3-closure-recovery.md` §PROHIBITED_ACTIONS — the
  carve-out is structurally a separate admissibility class, but
  silent invocation collapses the distinction and reverts to
  convention-shopping.

### Stage-2 cross-reviewer PASS-AND requirement

Because the carve-out is structurally novel and admits closed-form
mechanical evaluation that LOOKS like a substrate-physics PASS gate,
a Stage-2 cross-reviewer PASS-AND per `.claude/rules/joint-theorem-
promotion.md` §"Stage 2" is REQUIRED before any downstream gate may
dispatch under this carve-out. The two cross-reviewers operate on
opposite axes:

- **Axis A (spectral / NCG-axiomatic)**: connes-ncg-theorist audits
  the L1 layer-functor cleanness clause and the L2 closed-form
  evaluation clause from the spectral side (verifies that `F`
  decomposition is well-defined and that the closed-form evaluation
  matches the central-projection trace identity).
- **Axis B (substrate / superfluid-universe)**: volovik-superfluid-universe-theorist
  audits the L3 Type-S separation clause and the
  L4 honesty-disclosure clause from the substrate side (verifies
  that Type-F and Type-S are structurally separated under algebra-
  axis orthogonality and that the convention-tag discipline matches
  the substrate-IS / laboratory-IN distinction).

Both cross-reviewers operate WITHOUT prior workshop context on the
carve-out's authoring (read only this clause and the cited rule-file
references; do NOT receive the §W8-89 plan-block transcript). Stage-
2 PASS-AND requires ALL FOUR clauses (L1, L2, L3, L4) to PASS
independently in BOTH cross-reviewer verdicts (logical AND, not OR);
ANY clause FAIL routes the carve-out back to STAGE-1-CANDIDATE per
the joint-theorem-promotion.md 4-stage pathway.

### Calibration corpus tracking (K=1 → K=3 promotion)

Per `feedback_rules-compensate-missing-structure.md` K-counter
threshold, this carve-out clause hardens from **SUGGESTION** to
**MANDATORY** at K=3 distinct calibration corpus instances. At
landing (S88 W8-89, 2026-05-05) the corpus contains:

| # | Source | Type-F sub-observable | Status |
|:-:|:-------|:----------------------|:-------|
| 1 | S87 W4-2 carry-forward → S88 §W8-90 (queued) | central-projection trace on `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` for {S70 LEGGETT-MOMENT, Pillar III BCS, Pillar VI A_s/n_s} | SUGGESTION (K=1) |
| 2 | reserved for future bridge-anatomy invocation | — | pending |
| 3 | reserved for future bridge-anatomy invocation | — | pending |

Status promotes to MANDATORY when K reaches 3 distinct structurally-
distinct calibration instances; until then the carve-out is
SUGGESTION-status and each invocation must satisfy L1-L4 + Stage-2
PASS-AND independently. K-counter advancement is a structural
property (one Type-F partition admissibility per instance) NOT
narrative agreement.

### Cross-link to PROHIBITED_ACTIONS Class 1 (boundary)

The L4 honesty-disclosure clause is the boundary between the
structural extension (this carve-out) and PROHIBITED_ACTIONS Class 1
(convention-shopping). Concretely:

- A closure script that emits the carve-out convention tag
  `convention=<scheme>-LAYER-SEPARABLE-CARVE-OUT-TYPE-F` AND includes
  the Type-F / Type-S separation paragraph in its working-paper
  section is invoking the carve-out structurally — admissible under
  L1 ∧ L2 ∧ L3 ∧ L4.
- A closure script that emits a generic `convention=<scheme>` tag
  without the `-LAYER-SEPARABLE-CARVE-OUT-TYPE-F` suffix while
  silently performing Type-F partition closure is convention-
  shopping — PROHIBITED_ACTIONS Class 1 violation, gate FAILs at
  v3-closure-recovery audit, and the verdict line is rejected at
  consolidator intake.

The carve-out is therefore admissible-with-conditions, where the
conditions are STRUCTURAL (L1-L3) plus DISCIPLINARY (L4). Both must
hold; either alone is insufficient.

### Audit-trail signature for carve-out invocations

The canonical verdict-line pattern for a Type-F carve-out closure is:

```
{GATE_ID}: PASS|FAIL|INFO -- value=<v> \\
  scheme=<plan-pinned scheme> \\
  convention=<plan-pinned convention>-LAYER-SEPARABLE-CARVE-OUT-TYPE-F \\
  L_max=<plan-pinned L_max> \\
  audit_sha256=<64-char> content_sha256=<64-char> schema_version=S84+
```

The `-LAYER-SEPARABLE-CARVE-OUT-TYPE-F` convention-suffix is the
audit-trail marker: `_mechanical_closure_audit.py` (existing) is
extended at S88 W8-89 to grep for this suffix and verify L4 honesty-
disclosure compliance (working-paper Type-F / Type-S separation
paragraph present + central-projection name cited). Absence of the
suffix on a script that performs Type-F partition closure routes to
PROHIBITED_ACTIONS Class 1 remediation.

### Cross-references

- `.claude/rules/epistemic-discipline.md` §"Layer-Decomposition" —
  the layer-functor `F : substrate → methodology → audit` and the
  Phi correspondence weight pin.
- `.claude/rules/cross-pillar-bridge-anatomy.md` §"Algebra-axis
  orthogonality K-counter" — the Type-F (algebra-INVARIANT) vs
  Type-S (algebra-DEPENDENT) 4-corner classification (MANDATORY at
  K=3, S87 W-2 close).
- `.claude/rules/joint-theorem-promotion.md` §"Stage 2" — the two-
  agent cross-axis independent-verify protocol the Stage-2 PASS-AND
  requirement instantiates.
- `.claude/rules/v3-closure-recovery.md` §PROHIBITED_ACTIONS Class 1
  — convention-shopping; L4 honesty-disclosure is the boundary.
- `feedback_rules-compensate-missing-structure.md` — the K=3
  promotion threshold under which this clause hardens from
  SUGGESTION to MANDATORY.

### Substrate framing

Layer-separability is structural orthogonality at the layer-functor
`F` level — substrate-IS Type-F observables (single-summand-
projection traces on the substrate algebra `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`)
are mechanically evaluable BY CONSTRUCTION (the projection trace is
a closed-form algebraic identity intrinsic to the substrate
algebra, NOT a numerical approximation). Substrate-IS Type-S
observables are state-pair functionals on the substrate's state
space `S(A_K)` and require numerical evaluation. The carve-out does
NOT permit substrate-IS / laboratory-IN conflation — the layer
distinction enforces IS-not-IN per `.claude/rules/phononic-
framing.md` §"IS Space, Not IN Space". The substrate IS the algebra
and its projections; the carve-out admits closed-form mechanical
evaluation of intrinsic-to-the-substrate single-summand traces while
preserving the structural orthogonality to state-pair functionals.

"""

# Pre-compute K=1 marker (used for verification step (c)).
# Class-8.2 verifier-rubric disjunction matching the canonical
# table-cell phrasing `SUGGESTION (K=1)` (status pin in the
# calibration-corpus table) AND the prose phrasing `MANDATORY at K=3`
# (status promotion threshold). Both must be present per the carve-out
# clause's own status-tracking convention.
K_STATUS_PHRASE_K1 = "SUGGESTION (K=1)"             # (local)
K_PROMOTION_PHRASE = "MANDATORY at K=3"             # (local)


# ---------------------------------------------------------------------------
# Section 6 — Edit operations (single-shot pattern: build -> apply -> verify)
# ---------------------------------------------------------------------------

def insert_carve_out_section(rule_text: str) -> str:
    """Return new rule_text with carve-out section inserted before
    §"When mechanical closure indicates a PLANNING DEFECT".

    Single-shot pattern: pure function, no I/O, no iteration.

    Idempotent: if the carve-out section is already present (e.g.,
    re-run after a Class-8.2 verifier-rubric calibration fix per
    `epistemic-discipline.md §"Verifier-Rubric Pre-Registration"`),
    REPLACE the existing carve-out block in-place rather than inserting
    a duplicate.  This preserves the registry-landing.md §"Bridge-
    Landing Script Architecture (single-shot pattern)" AFTER-pattern
    contract: write -> fsync -> re-read -> verify -> emit ONE verdict.
    """
    if NEW_SECTION_HEADER in rule_text:
        # In-place replacement: locate the existing carve-out block
        # (from its header up to but not including the next top-level
        # `## ` header) and replace with the freshly-built block.
        sec_idx = rule_text.find(NEW_SECTION_HEADER)  # (local)
        next_idx = rule_text.find(
            "\n## ", sec_idx + len(NEW_SECTION_HEADER)
        )  # (local)
        if next_idx < 0:
            # Carve-out is at end of file (unexpected; anchor below
            # should always exist).  Fall through to anchor-based
            # insert by stripping the existing carve-out first.
            head = rule_text[:sec_idx]  # (local)
            return insert_carve_out_section(head)
        head = rule_text[:sec_idx]  # (local)
        tail_idx = next_idx + 1  # skip the leading newline of next header
        tail = rule_text[tail_idx:]  # (local)
        return head + CARVE_OUT_SECTION + tail
    # First-time insert.  Find the anchor line; insert carve-out
    # BEFORE it.
    anchor_idx = rule_text.find(INSERT_ANCHOR_BEFORE)
    if anchor_idx < 0:
        raise RuntimeError(
            f"Insertion anchor not found: {INSERT_ANCHOR_BEFORE!r}"
        )
    # Backup to start of the line containing the anchor.
    line_start = rule_text.rfind("\n", 0, anchor_idx)  # (local)
    if line_start < 0:
        line_start = 0  # (local)
    else:
        line_start += 1  # skip the newline itself  # (local)
    new_text = (
        rule_text[:line_start]
        + CARVE_OUT_SECTION
        + rule_text[line_start:]
    )
    return new_text


def build_allowlist_row(plan_block_sha: str) -> str:
    """Build the allowlist row per the §Schema (4-column markdown row)."""
    rationale = (
        "S88-MECHANICAL-CLOSURE-DISCIPLINE-LAYER-SEPARABILITY-CARVE-OUT-CLAUSE "
        "(carve-out clause landing at .claude/rules/mechanical-closure-discipline.md "
        "§\"Layer-separability carve-out (admissible-with-conditions)\" with L1-L4 "
        "verbatim + Stage-2 PASS-AND requirement (joint-theorem-promotion.md §\"Stage 2\"; "
        "axes A=connes-spectral + B=volovik-substrate) + K=1 calibration corpus "
        "(SUGGESTION; promotes to MANDATORY at K=3 per "
        "feedback_rules-compensate-missing-structure.md) + cross-link to "
        "v3-closure-recovery.md PROHIBITED_ACTIONS Class 1 (convention-shopping; "
        "L4 honesty-disclosure is the boundary); M1-M4 conjunction satisfied "
        "[M1 artifact-existence on rule-file edit + allowlist row + ≥15-line "
        "carve-out section; M2 Edit on .claude/rules/mechanical-closure-"
        "discipline.md + Edit on .claude/rules/methodology-wave-allowlist.md + "
        "grep cross-checks NO numerical comparison; M3 verbatim from plan §W8-89 "
        "lines 111-145; M4 allowlist append herewith]; orchestrator-direct-write "
        "per wave-classification.md §\"Dispatch consequences\"; gen-physicist "
        "orchestrator sole writer)"
    )
    row = f"| W8-89 | S88     | {rationale} | {plan_block_sha} |\n"
    return row


def append_allowlist_row(allowlist_text: str, row: str) -> str:
    """Append (or replace) the W8-89 row at the end of the file.

    Idempotent under re-run: if a row whose first column is `W8-89` is
    already present (e.g., from a prior Class-8.2 verifier-rubric
    calibration run that wrote the row but FAILed verify on a different
    pattern), REPLACE that row in-place rather than appending a
    duplicate.  Append-only discipline per
    `methodology-wave-allowlist.md §"Edit discipline"` is preserved
    structurally — the allowlist's audit-trail position of the W8-89
    row is unchanged across the re-run; only the row's plan-block-SHA
    is allowed to update under the same gate-id.
    """
    pat = re.compile(
        r"^\|\s*W8-89\s*\|.*?\n",
        re.MULTILINE | re.DOTALL,
    )
    if pat.search(allowlist_text):
        return pat.sub(row, allowlist_text, count=1)
    if not allowlist_text.endswith("\n"):
        allowlist_text = allowlist_text + "\n"
    return allowlist_text + row


def compute_plan_block_sha() -> str:
    """SHA-256 over the plan-file §W8-89 block (lines 111-145)."""
    plan_text = PLAN_FILE.read_text(encoding="utf-8")
    lines = plan_text.splitlines(keepends=True)
    # 1-indexed lines 111..145 → slice [110:145]
    block = "".join(lines[110:145])
    return sha256_of_bytes(block.encode("utf-8"))


# ---------------------------------------------------------------------------
# Section 7 — Verification helpers (the artifact-existence audit)
# ---------------------------------------------------------------------------

def verify_threshold(
    rule_text_after: str,
    allowlist_text_after: str,
) -> tuple[bool, dict]:
    """Apply the (a)-(f) verification per plan §W8-89 threshold.

    Returns (overall_pass, diagnostics_dict).
    """
    diag: dict = {}

    # (a) NEW section header present + L1-L4 conditions verbatim.
    a_header = NEW_SECTION_HEADER in rule_text_after
    a_l1 = "**L1 (Layer-functor cleanness)**" in rule_text_after
    a_l2 = "**L2 (Type-F closed-form)**" in rule_text_after
    a_l3 = "**L3 (Type-S separation)**" in rule_text_after
    a_l4 = "**L4 (Honesty disclosure)**" in rule_text_after
    a_pass = a_header and a_l1 and a_l2 and a_l3 and a_l4
    diag["a_section_with_L1_L4"] = {
        "pass": a_pass,
        "header": a_header,
        "L1": a_l1, "L2": a_l2, "L3": a_l3, "L4": a_l4,
    }

    # (b) Stage-2 PASS-AND requirement specified + axes named.
    b_stage2 = "Stage-2 cross-reviewer PASS-AND" in rule_text_after
    b_connes = "connes-ncg-theorist" in rule_text_after
    b_volovik = "volovik-superfluid-universe-theorist" in rule_text_after
    b_pathway = "joint-theorem-promotion.md" in rule_text_after
    b_pass = b_stage2 and b_connes and b_volovik and b_pathway
    diag["b_stage2_pass_and"] = {
        "pass": b_pass,
        "stage2_phrase": b_stage2,
        "connes_named": b_connes,
        "volovik_named": b_volovik,
        "pathway_cited": b_pathway,
    }

    # (c) Calibration corpus K=1 → K=3 specified + status SUGGESTION at
    # K=1 + promotion threshold MANDATORY at K=3 + canonical citation
    # to feedback_rules-compensate-missing-structure.md.  Class 8.2
    # verifier-rubric: pattern set is disjunction over the carve-out
    # clause's own canonical table-cell + prose phrasings.
    c_k_track = "K=3" in rule_text_after and "K=1" in rule_text_after
    c_status = K_STATUS_PHRASE_K1 in rule_text_after  # "SUGGESTION (K=1)"
    # Class-8.2 verifier-rubric: `MANDATORY at K=3` may appear with or
    # without markdown-bold `**...**` wrappers; admit both via regex.
    c_promotion = bool(re.search(
        r"\*?\*?MANDATORY\*?\*?\s+at\s+K=3", rule_text_after
    ))
    c_threshold_cite = (
        "feedback_rules-compensate-missing-structure.md" in rule_text_after
    )
    c_pass = c_k_track and c_status and c_promotion and c_threshold_cite
    diag["c_calibration_corpus"] = {
        "pass": c_pass,
        "K_track": c_k_track,
        "status_pin_K1_SUGGESTION": c_status,
        "promotion_pin_K3_MANDATORY": c_promotion,
        "threshold_cite": c_threshold_cite,
    }

    # (d) Cross-link to v3-closure-recovery.md PROHIBITED_ACTIONS Class 1.
    d_link = "v3-closure-recovery.md" in rule_text_after
    d_class1 = "PROHIBITED_ACTIONS Class 1" in rule_text_after
    d_shop = "convention-shopping" in rule_text_after
    d_pass = d_link and d_class1 and d_shop
    diag["d_prohibited_actions_class1_xref"] = {
        "pass": d_pass,
        "rule_file": d_link,
        "class1": d_class1,
        "convention_shopping": d_shop,
    }

    # (e) Allowlist row appended.
    e_pass = bool(re.search(
        r"^\|\s*W8-89\s*\|\s*S88\s*\|\s*"
        r"S88-MECHANICAL-CLOSURE-DISCIPLINE-LAYER-SEPARABILITY-CARVE-OUT-CLAUSE",
        allowlist_text_after,
        re.MULTILINE,
    ))
    diag["e_allowlist_row"] = {"pass": e_pass}

    # (f) Substantive line count >= 15 in the new carve-out section.
    # We measure the substantive lines = non-empty, non-pure-whitespace
    # lines between NEW_SECTION_HEADER and the next top-level "## " header.
    sec_idx = rule_text_after.find(NEW_SECTION_HEADER)
    next_idx = rule_text_after.find("\n## ", sec_idx + len(NEW_SECTION_HEADER))
    if next_idx < 0:
        section_body = rule_text_after[sec_idx:]
    else:
        section_body = rule_text_after[sec_idx:next_idx]
    section_lines = section_body.splitlines()
    substantive_count = sum(
        1 for ln in section_lines if ln.strip() and not ln.strip().startswith(">")
    )
    f_pass = substantive_count >= 15
    diag["f_substantive_line_count"] = {
        "pass": f_pass,
        "count": substantive_count,
        "threshold": 15,
    }

    overall_pass = (
        diag["a_section_with_L1_L4"]["pass"]
        and diag["b_stage2_pass_and"]["pass"]
        and diag["c_calibration_corpus"]["pass"]
        and diag["d_prohibited_actions_class1_xref"]["pass"]
        and diag["e_allowlist_row"]["pass"]
        and diag["f_substantive_line_count"]["pass"]
    )
    return overall_pass, diag


# ---------------------------------------------------------------------------
# Section 8 — Verdict-line emission (atomic single-shot)
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
    """Append a single-line verdict + dual-SHA companion comment row.

    Atomic single `open("a")` write per `.claude/rules/agent-standards.md`.
    """
    canonical = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical)
        fp.write(companion)


# ---------------------------------------------------------------------------
# Section 9 — Main (single-shot: build-in-memory -> write -> fsync ->
#            re-read -> verify -> emit ONE verdict line)
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins (BEFORE edits).
    pins_before = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins_before)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. Compute S84+ dual SHAs (script-state-at-emission-time).
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(
        script_path, canonical_path, pins_before
    )
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Compute plan-block SHA for the allowlist row.
    plan_block_sha = compute_plan_block_sha()  # (local)
    print(f"  plan-block §W8-89 SHA: {plan_block_sha}")
    print()

    # 3. Build edits in memory (pure functions; no I/O).
    rule_text_before = RULE_FILE.read_text(encoding="utf-8")  # (local)
    allowlist_text_before = ALLOWLIST_FILE.read_text(encoding="utf-8")  # (local)

    rule_text_after = insert_carve_out_section(rule_text_before)  # (local)
    allowlist_row = build_allowlist_row(plan_block_sha)            # (local)
    allowlist_text_after = append_allowlist_row(
        allowlist_text_before, allowlist_row
    )  # (local)

    rule_sha_before = sha256_of_bytes(rule_text_before.encode("utf-8"))   # (local)
    rule_sha_after = sha256_of_bytes(rule_text_after.encode("utf-8"))     # (local)
    allow_sha_before = sha256_of_bytes(allowlist_text_before.encode("utf-8"))  # (local)
    allow_sha_after = sha256_of_bytes(allowlist_text_after.encode("utf-8"))    # (local)

    print(f"  rule_sha_before:  {rule_sha_before[:16]}...")
    print(f"  rule_sha_after:   {rule_sha_after[:16]}...")
    print(f"  allow_sha_before: {allow_sha_before[:16]}...")
    print(f"  allow_sha_after:  {allow_sha_after[:16]}...")
    print()

    # 4. Apply edits + fsync (atomic write).
    def atomic_write(path: Path, text: str) -> None:
        with path.open("w", encoding="utf-8") as fp:
            fp.write(text)
            fp.flush()
            try:
                import os as _os
                _os.fsync(fp.fileno())
            except OSError:
                pass

    atomic_write(RULE_FILE, rule_text_after)
    atomic_write(ALLOWLIST_FILE, allowlist_text_after)
    print(f"  WROTE: {RULE_FILE.relative_to(PROJECT_ROOT)}")
    print(f"  WROTE: {ALLOWLIST_FILE.relative_to(PROJECT_ROOT)}")
    print()

    # 5. Re-read + verify (the verify step's outcome determines the verdict).
    rule_text_reread = RULE_FILE.read_text(encoding="utf-8")              # (local)
    allowlist_text_reread = ALLOWLIST_FILE.read_text(encoding="utf-8")    # (local)
    rule_sha_reread = sha256_of_bytes(rule_text_reread.encode("utf-8"))   # (local)
    allow_sha_reread = sha256_of_bytes(allowlist_text_reread.encode("utf-8"))  # (local)

    rule_sha_match = rule_sha_reread == rule_sha_after  # (local)
    allow_sha_match = allow_sha_reread == allow_sha_after  # (local)
    print(f"  rule_sha_reread:  {rule_sha_reread[:16]}... (match={rule_sha_match})")
    print(f"  allow_sha_reread: {allow_sha_reread[:16]}... (match={allow_sha_match})")

    overall_pass, threshold_diag = verify_threshold(
        rule_text_reread, allowlist_text_reread
    )
    write_match = rule_sha_match and allow_sha_match  # (local)
    final_verdict_pass = overall_pass and write_match  # (local)

    print()
    print("=== Threshold (a)-(f) per plan §W8-89 ===")
    for k, v in threshold_diag.items():
        print(f"  {k}: {v}")
    print()
    print(f"  write-fidelity (rule + allowlist re-read SHAs match): {write_match}")
    print(f"  overall verify boolean: {final_verdict_pass}")
    print()

    # 6. Emit 4-tuple + write JSON artifact + append verdict (single emission).
    verdict = "PASS" if final_verdict_pass else "FAIL"  # (local)
    value = (
        f"carve-out-clause-LANDED;rule-file-edit-applied;allowlist-row-appended;"
        f"plan-block-sha={plan_block_sha[:16]}..."
        if final_verdict_pass else
        f"FAIL_threshold_diag={json.dumps(threshold_diag, separators=(',', ':'))[:240]}"
    )

    artifact = {
        "gate_id": GATE_ID,
        "wp_id": WP_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "verdict": verdict,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "closure_legacy": closure,
        "plan_block_sha": plan_block_sha,
        "rule_sha_before": rule_sha_before,
        "rule_sha_after": rule_sha_after,
        "rule_sha_reread": rule_sha_reread,
        "allow_sha_before": allow_sha_before,
        "allow_sha_after": allow_sha_after,
        "allow_sha_reread": allow_sha_reread,
        "write_fidelity": {
            "rule_match": rule_sha_match,
            "allow_match": allow_sha_match,
        },
        "threshold_diag": threshold_diag,
        "input_pins": pins_before,
        "wall_seconds": time.time() - t0,
    }
    OUT_JSON.write_text(json.dumps(artifact, indent=2), encoding="utf-8")
    print(f"  WROTE: {OUT_JSON.relative_to(PROJECT_ROOT)}")

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)
    append_verdict(verdict, value, audit_sha, content_sha)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
