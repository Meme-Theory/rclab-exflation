#!/usr/bin/env python3
"""
S92 W2 CF-W9-11-1 — §VII.AQ.OP-PROJ Scheme-Suffix Retrofit (mack-cosmic-bridge sole writer)
============================================================================================

Gate ID: S92-W2-CF-W9-11-1-VII-AQ-SCHEME-SUFFIX-RETROFIT
Trigger: [VERIFY]
Classification: NON-PHONONIC (METHODOLOGY-class per wave-classification.md §M1-M4)

Source plan: sessions/session-plan/session-92-plan-w2.md §W2-1 (lines 59-261).

Substantive task (single-shot AFTER-pattern per registry-landing.md §"Bridge-Landing
Script Architecture"):

  Step 1 (BUILD, pure-function):
      Build a CF-W9-11-1 retrofit citation block in memory. The block records the
      S91 W9-11 Reading A bit-precision scheme-INDEPENDENCE PASS (audit_sha256
      `1fef32c8f88d89f3...`; Δ_scheme = 0.000e+00 EXACTLY at L_max ∈ {5, 12, 14})
      and activates the cross-pillar-bridge-anatomy.md §"Bridge-map-scheme suffix
      discipline" carve-out at §VII.AQ.OP-PROJ. Per that rule body:

         "Bare Element 3 (no scheme suffix) is FORBIDDEN when the bridge map admits
          multiple scheme evaluations AND structural-output-type independence
          (Reading A) is not pre-established. With Reading A confirmed (e.g.,
          |GV_APS1975 − GV_Cheeger-Simons| < 1e-3 in M_KK² units), the entry MAY
          omit the suffix and cite the scheme-INDEPENDENCE theorem."

      The S91 W9-11 result strengthens that condition from `< 1e-3` to bit-identical
      (`= 0.000e+00 EXACTLY` across all three schemes APS-1975 + Cheeger-Simons
      + Bismut-Cheeger at L_max=12, with cross-pin residual 2.82e-08 at L_max=5).

  Step 2 (WRITE atomic + fsync):
      Insert the retrofit block BEFORE the trailing "**Cross-references**" section
      of §VII.AQ.OP-PROJ. The pre-existing entry text (Anchor structure, Level 1/2/3,
      IS-not-IN anatomy, CF-54 corrigendum, CF-55 substrate-physics adjudicator
      cross-link, Reading A/B sub-blocks, etc.) is PRESERVED INTACT per absolute
      verdict permanence (gate-verdicts.md §"Option A — absolute verdict permanence").

  Step 3 (RE-READ + VERIFY):
      Re-read the registry from disk; verify 5 predicates (a)..(e) PASS in
      conjunction per plan §W2-1:
        (a) §VII.AQ.OP-PROJ retrofit block present;
        (b) cites S91 W9-11 audit_sha256 = 1fef32c8f88d89f39548f0b086717b7efea8e82f3c015b73c947977f9d573f58;
        (c) cites the carve-out clause from cross-pillar-bridge-anatomy.md
            §"Bridge-map-scheme suffix discipline";
        (d) substantive_line_count(retrofit_block) >= 15;
        (e) content_sha256 of the retrofit block matches the
            input-pin-map-derived hash computed during build.

  Step 4 (EMIT, single verdict line):
      Exactly ONE canonical line + ONE dual-SHA companion comment row +
      ONE S87 schema-v2 3-tuple companion comment row.

Substrate framing (per phononic-framing.md §"IS Space, Not IN Space"):

    The substrate IS the §VII.AQ.OP-PROJ structural theorem (operator-side
    central-projection trace on A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ) under Reading A
    scheme-INDEPENDENCE bit-identity). The retrofit IS the audit-layer F-functor
    image at the registry-text layer per epistemic-discipline.md §"Layer-Decomposition".

    Direction substrate → emergent:
        A_K scheme-INDEPENDENCE (Reading A bit-identity at L_max=12)
        → S91 W9-11 PASS at machine precision (Δ_scheme = 0.000e+00 EXACTLY)
        → cross-pillar-bridge-anatomy.md §"Bridge-map-scheme suffix discipline"
          carve-out clause activated (structural-output-type independence pre-established)
        → registry-text retrofit applied at §VII.AQ.OP-PROJ
        → bridge-map-scheme suffix MANDATORY requirement structurally retired
          at this slot.

    FORBIDDEN inversion: "the retrofit IS the result." The retrofit is the
    audit-layer F-image of the substrate-IS scheme-INDEPENDENCE theorem.

Input-pin map (audit_sha256 inputs):
    - canonical_constants.py (SHARED_DIR / 'canonical_constants.py')
    - sessions/permanent-results-registry.md (pre-edit SHA)
    - .claude/rules/cross-pillar-bridge-anatomy.md
    - .claude/rules/registry-landing.md
    - computations/session-91/s91_gate_verdicts.txt
    - S91-BRIDGE-MAP-SCHEME-INDEPENDENCE-AUDIT canonical-pin audit_sha256
    - retrofit text content_sha256

Output 4-tuple:
    (value=<5-of-5_predicates_PASS_or_diagnostic>,
     scheme=registry-text-retrofit-AFTER-pattern,
     convention=VII-AQ-OP-PROJ-scheme-suffix-retrofit-Reading-A-bit-precision-scheme-INDEPENDENCE-citation,
     L_max=N/A)

Author: mack-cosmic-bridge (sole writer per feedback_mack-bridge-role.md)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import per math-scripts.md)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

# (local) Inject the _shared directory into sys.path so canonical_constants imports
SHARED_DIR_BOOT = Path(r"C:\sandbox\Ainulindale Exflation\computations\_shared")  # (local)
sys.path.insert(0, str(SHARED_DIR_BOOT))

from canonical_constants import *  # noqa: F401,F403  # mandatory per math-scripts.md
# Used downstream: M_KK_gravity, M_KK (canonical), Delta_BCS, gv_canonical_difference_FW,
# tau_fold. This script consumes M_KK² as the unit context for the bit-precision claim;
# no numerical computation depends on imported canonicals — they enter the audit SHA
# closure via the canonical_constants.py byte-content pin.

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import os
import time

# ---------------------------------------------------------------------------
# Section 3 — Identity + paths
# ---------------------------------------------------------------------------
SESSION = "S92"                                                          # (local)
GATE_ID = "S92-W2-CF-W9-11-1-VII-AQ-SCHEME-SUFFIX-RETROFIT"              # (local)
SCHEME = "registry-text-retrofit-AFTER-pattern"                          # (local)
CONVENTION = (
    "VII-AQ-OP-PROJ-scheme-suffix-retrofit-"
    "Reading-A-bit-precision-scheme-INDEPENDENCE-citation"
)                                                                        # (local)
L_MAX = "N/A"  # METHODOLOGY-class registry-text edit; no L_max axis     # (local)

# (local) Absolute Windows paths per project convention (CLAUDE.md PATH HAS A SPACE)
PROJECT_ROOT = Path(r"C:\sandbox\Ainulindale Exflation")                 # (local)
SESSION_DIR = PROJECT_ROOT / "computations" / "session-92"               # (local)
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"                   # (local)
SCRIPT_PATH = Path(__file__).resolve()                                   # (local)

REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"      # (local)
VERDICT_PATH = SESSION_DIR / "s92_gate_verdicts.txt"                              # (local)
DATA_JSON_PATH = SESSION_DIR / "s92_w2_vii_aq_scheme_suffix_retrofit.json"        # (local)

CROSS_PILLAR_RULE = PROJECT_ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md"  # (local)
REGISTRY_LANDING_RULE = PROJECT_ROOT / ".claude" / "rules" / "registry-landing.md"          # (local)
S91_VERDICTS_PATH = PROJECT_ROOT / "computations" / "session-91" / "s91_gate_verdicts.txt"  # (local)
CANONICAL_CONSTANTS = SHARED_DIR / "canonical_constants.py"                                  # (local)
PLAN_W2_PATH = PROJECT_ROOT / "sessions" / "session-plan" / "session-92-plan-w2.md"          # (local)

# (local) Pre-pinned input-pin from spawn prompt + plan §W2-1
S91_W9_11_AUDIT_SHA = (
    "1fef32c8f88d89f39548f0b086717b7efea8e82f3c015b73c947977f9d573f58"
)                                                                        # (local)
S91_W9_11_GATE_NAME = "S91-BRIDGE-MAP-SCHEME-INDEPENDENCE-AUDIT"         # (local)

# (local) Option A supersedes-tag detection: scan s92 verdict file at script-init
# for any prior canonical line matching this gate_id; if found, the corrective
# emission MUST carry `supersedes=<old_audit_sha>` per gate-verdicts.md §"Option A
# — sig_5 remediation pathway under absolute verdict permanence". Stored at this
# top-level constant scope so the audit-trail is documented in the script bytes.
PRIOR_FAIL_AUDIT_SHA_PATTERN_PREFIX = "S92-W2-CF-W9-11-1-VII-AQ-SCHEME-SUFFIX-RETROFIT:"  # (local)


# ---------------------------------------------------------------------------
# Section 4 — SHA helpers
# ---------------------------------------------------------------------------
def file_sha256(path: Path) -> str:
    """SHA-256 of a file's bytes."""
    h = hashlib.sha256()  # (local)
    try:
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                h.update(chunk)
    except OSError:
        return ""
    return h.hexdigest()


def text_sha256(text: str) -> str:
    """SHA-256 of a text string (UTF-8 encoded)."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def closure_hash(input_pin_map: dict) -> str:
    """Compute audit_sha256 over the ordered input-pin map.

    Mirrors computations/_shared/_script_template.py canonical closure pattern
    (sorted (k, v) pairs, NL-separated, UTF-8 SHA-256).
    """
    items = sorted(input_pin_map.items())  # (local)
    serialized = "\n".join(f"{k}={v}" for k, v in items)  # (local)
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — BUILD: retrofit citation block (pure function; no I/O)
# ---------------------------------------------------------------------------
def build_retrofit_block() -> str:
    """Build the CF-W9-11-1 scheme-suffix retrofit citation block.

    Single-shot AFTER-pattern Step 1: pure-function, no I/O. The block has
    >=15 substantive lines, cites the S91 W9-11 audit_sha256, cites the
    cross-pillar-bridge-anatomy.md §"Bridge-map-scheme suffix discipline"
    carve-out clause, and explicitly materializes the structural retirement
    of the bridge-map-scheme suffix MANDATORY requirement at this slot.
    """
    block = (
        "**CF-W9-11-1 scheme-suffix retrofit (S92 W2 — mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`, 2026-05-22)**\n"
        "\n"
        "Downstream of the S91 W9-11 `S91-BRIDGE-MAP-SCHEME-INDEPENDENCE-AUDIT` PASS verdict (audit_sha256=`1fef32c8f88d89f39548f0b086717b7efea8e82f3c015b73c947977f9d573f58`; "
        "verdict line at `computations/session-91/s91_gate_verdicts.txt:218`; three-scheme audit at L_max=12 with cross-pin at L_max=5 + L_max=14), "
        "the §VII.AQ.OP-PROJ bridge-map-scheme suffix MANDATORY requirement is **STRUCTURALLY RETIRED at this slot** under the carve-out clause of `.claude/rules/cross-pillar-bridge-anatomy.md §\"Bridge-map-scheme suffix discipline\"`:\n"
        "\n"
        "  > Bare Element 3 (no scheme suffix) is FORBIDDEN when the bridge map admits multiple scheme evaluations AND structural-output-type independence (Reading A) is not pre-established. With Reading A confirmed (e.g., `|GV_APS1975 − GV_Cheeger-Simons| < 1e-3` in M_KK² units), the entry MAY omit the suffix and cite the scheme-INDEPENDENCE theorem.\n"
        "\n"
        "**S91 W9-11 substrate-physics result (citation; consumed verbatim from the upstream PASS)**:\n"
        "\n"
        "- `max_pairwise_diff = 0.000000e+00` across the three scheme pairs at L_max=12 (`diff_AC = diff_AB = diff_CB = 0.000000e+00`).\n"
        "- `GV_APS_L12 = GV_CS_L12 = GV_BC_L12 = -1.2081580929e+08` (bit-identical 10-significant-figure agreement; Atiyah-Patodi-Singer 1975 secondary-class = Cheeger-Simons differential-character = Bismut-Cheeger η-form at boundary).\n"
        "- `GV_APS_L5 = -40579.1500479788` vs `gv_canonical_pin = gv_canonical_difference_FW = -40579.1500479506`; cross-pin residual `2.822e-08` (well below CF-55 1e-3 carve-out threshold; this is the S87 W8-8 canonical anchor reproduced at L_max=5 to bit precision).\n"
        "- `BC_adiabatic_residual = 6.121e-13`; `CS_Mellin_drift = 6.119e-09` (numerical-floor diagnostics; both well below the 1e-3 threshold).\n"
        "- Convention pins on the S91 W9-11 verdict line: `scheme=gv-heitsch-invariant-three-scheme-secondary-class-evaluation-scheme-independence-audit`; `convention=VII-AQ-three-scheme-APS-1975-Cheeger-Simons-Bismut-Cheeger-independence-Reading-A-vs-B`; `L_max=12`; `level_pin=FULL`; `regulator_pin=a_n^{Mellin}`; `binding_axis=canonical-import-binding`; `machinery_scope=CACHE-PROJECTION-Lmax-12-canonical-anchor-Lmax-5`. Composite verdict PASS; 3-tuple PASS/PASS/VALID.\n"
        "\n"
        "**Carve-out conditions satisfied at §VII.AQ.OP-PROJ (S92 W2 ratification)**:\n"
        "\n"
        "1. **Multi-scheme bridge map**: the (η, GV) Connes-Karoubi pairing admits three distinct scheme evaluations — APS-1975 secondary-class (Atiyah-Patodi-Singer 1975 ρ-invariant route; boundary-anchored η residue), Cheeger-Simons 1985 differential-character (full-leaf-foliation; foliation-aware), and Bismut-Cheeger η-form (boundary; adiabatic-limit). All three are enumerated at the bridge-map suffix discipline rule body lines 133-135. The pre-condition of the carve-out (multi-scheme bridge map) is satisfied by construction.\n"
        "2. **Structural-output-type independence PRE-ESTABLISHED and CONFIRMED**: S91 W9-11 demonstrates `Δ_scheme = 0.000e+00 EXACTLY` at L_max=12 across all three scheme evaluations; this is **structurally stronger** than the carve-out's textual threshold `< 1e-3` in M_KK² units. The bit-identity is reproduced at L_max=5 (canonical anchor) with cross-pin residual `2.82e-08` and at L_max=14 (cross-check) to within the numerical-floor diagnostic. The independence pre-establishment is the load-bearing audit conjunct.\n"
        "3. **Cross-link to upstream substrate-physics adjudicator**: this retrofit composes with the prior S90 W7 CF-55 substrate-physics adjudicator result (audit_sha256=`f634be0d942241095e40ce71562b69fee522faaa520c9ce861844c15f02a8f77`; Reading A confirmed at L_max=12 at `Δ_scheme = 0.000e+00 EXACTLY` between APS-1975 and Cheeger-Simons). S91 W9-11 EXTENDS the two-scheme CF-55 result to three-scheme bit-identity AND adds the L_max ∈ {5, 14} cross-pins. The carve-out activation is now load-bearing on TWO independent verdict events (S90 W7 CF-55 + S91 W9-11), not a single-event prediction.\n"
        "\n"
        "**Retrofit consequence for downstream consumers**:\n"
        "\n"
        "Downstream registry consumers citing §VII.AQ.OP-PROJ — including any future Element-3 bridge-map citation, any new §VII slot allocating the (η, GV) joint-probe Connes-Karoubi pairing at this corner, or any Stage-2 cross-axis independent-verify dispatch loading the §VII.AQ.OP-PROJ STAGE-1-CANDIDATE — MAY omit the `-APS-1975-secondary-class` / `-Cheeger-Simons` / `-Bismut-Cheeger` scheme-suffix tag on the verdict-line `convention=` field PROVIDED the substrate-physics adjudicator chain (S90 W7 CF-55 + S91 W9-11) remains a load-bearing input pin. The scheme-INDEPENDENCE theorem citation `S91-BRIDGE-MAP-SCHEME-INDEPENDENCE-AUDIT audit_sha256=1fef32c8f88d89f3...` REPLACES the suffix-tag requirement at this slot.\n"
        "\n"
        "Bare Element 3 references at §VII.AQ.OP-PROJ downstream consumers REMAIN admissible under the carve-out (the negative-match regex `Element 3.*: ...bridge map\\.|connecting map\\.|fiducial-anchor\\.` at the bridge-map-scheme suffix discipline rule body lines 145-148 does NOT fire when the carve-out is active). The carve-out is `slot-LOCAL` — it activates at this §VII.AQ.OP-PROJ slot only; other §VII slots inheriting multi-scheme bridge maps WITHOUT pre-established structural-output-type independence remain bound by the suffix-tag MANDATORY clause.\n"
        "\n"
        "**Provenance + audit trail**:\n"
        "\n"
        "- **CF-W9-11-1 retrofit gate**: `S92-W2-CF-W9-11-1-VII-AQ-SCHEME-SUFFIX-RETROFIT`; verdict line at `computations/session-92/s92_gate_verdicts.txt` (emitted at this script's run).\n"
        "- **Upstream input pin (S91 W9-11)**: `S91-BRIDGE-MAP-SCHEME-INDEPENDENCE-AUDIT`; audit_sha256=`1fef32c8f88d89f39548f0b086717b7efea8e82f3c015b73c947977f9d573f58`; `computations/session-91/s91_gate_verdicts.txt:218`.\n"
        "- **Upstream input pin (S90 W7 CF-55)**: `S90-AQ-SECONDARY-CLASS-SCHEME-DISCRIMINATOR`; audit_sha256=`f634be0d942241095e40ce71562b69fee522faaa520c9ce861844c15f02a8f77`; `computations/session-90/s90_gate_verdicts.txt:128`.\n"
        "- **Rule citation**: `.claude/rules/cross-pillar-bridge-anatomy.md §\"Bridge-map-scheme suffix discipline\"` (rule body lines 129-151 of the cited rule file; carve-out clause line 137).\n"
        "- **Methodology-class wave classification**: per `.claude/rules/wave-classification.md §M1-M4` 4-test conjunction (M1 artifact-existence PASS predicate; M2 producing operation is Edit/Write on registry text; M3 source-of-truth is verbatim from S91 W9-11 PASS + upstream rule body; M4 allowlist append per `.claude/rules/methodology-wave-allowlist.md` orchestrator-only-edit + append-only edit-discipline).\n"
        "- **Calibration corpus advancement note (forward-pinned to CF-W9-11-2)**: this retrofit is calibration corpus Instance #2 for the Bridge-map-scheme suffix discipline at `sessions/framework/registry/cross-pillar-bridge-corpus.md §10`; K=1 → K=2 advancement appended in the parallel §W2-2 `S92-W2-CF-W9-11-2-CORPUS-ROW-K2-ADVANCEMENT` gate. The retrofit itself (this §W2-1 gate) materializes the slot-LOCAL carve-out activation; the corpus row (§W2-2 gate) records the K-counter advancement at the rule-level meta-axis.\n"
    )
    return block


def build_anchor_for_insertion(registry_text: str) -> str:
    """Locate the insertion anchor — immediately BEFORE the `**Cross-references**:` block.

    The §VII.AQ.OP-PROJ section is bounded on the upper end by
    `## §VII.AQ.OP-PROJ — STRUCTURAL-EVEN-GRADING-BLINDNESS` (header at line 17460)
    and on the lower end by the next section start
    `### §VII.AQ.STATE-PROJ — STRUCTURAL-EVEN-GRADING-BLINDNESS` (companion at line 17717).

    Within that range, the trailing **Cross-references** block lives between
    the **Substrate framing** + Stage-2-style upgrade clause and the
    **CF-54 Phase-2 retrofit provenance** + `---` separator. We insert the
    CF-W9-11-1 retrofit block immediately BEFORE the **Cross-references**
    block so it lands within the section but BEFORE the cross-link list.

    Returns the substring marker that the insertion targets.
    """
    # (local) The insertion anchor is the **Cross-references**: line within §VII.AQ.OP-PROJ.
    # We do NOT use a long anchor sentence (those carry backtick / em-dash characters that
    # are fragile across reflow). The anchor is the unique substring
    # "\n\n**Cross-references**:" within the §VII.AQ.OP-PROJ section bounds. The Phase 2
    # main loop locates this anchor BY SEARCH FROM op_proj_start (so the first match is
    # the OP-PROJ section's Cross-references header, not a later section's).
    return "\n\n**Cross-references**:"


# ---------------------------------------------------------------------------
# Section 6 — WRITE: atomic + fsync
# ---------------------------------------------------------------------------
def write_atomic_with_fsync(path: Path, content: str) -> None:
    """Atomic write + fsync per registry-landing.md §"Bridge-Landing Script Architecture".

    Single-shot pattern: write the full new content to a tmp path, fsync, then
    os.replace into target. The replace is atomic on Windows/NTFS for files
    on the same volume.
    """
    tmp_path = path.with_suffix(path.suffix + f".tmp_{GATE_ID.lower()}")  # (local)
    with open(tmp_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp_path, path)


# ---------------------------------------------------------------------------
# Section 7 — RE-READ + VERIFY: 5-predicate conjunction (a)..(e)
# ---------------------------------------------------------------------------
def verify_section_matches(
    registry_path: Path,
    retrofit_block_expected: str,
    expected_substrate_substrings: list,
    expected_block_content_sha256: str,
) -> dict:
    """Re-read registry; evaluate 5-predicate (a)..(e) PASS conjunction.

    Predicates:
      (a) §VII.AQ.OP-PROJ retrofit block present (block identifier substring
          'CF-W9-11-1 scheme-suffix retrofit (S92 W2' appears within
          §VII.AQ.OP-PROJ section).
      (b) Cites S91 W9-11 audit_sha256 = 1fef32c8f88d89f39548f0b086717b7efea8e82f3c015b73c947977f9d573f58.
      (c) Cites the carve-out clause from cross-pillar-bridge-anatomy.md
          §"Bridge-map-scheme suffix discipline".
      (d) substantive_line_count(retrofit_block) >= 15 (per
          wave-classification.md §M1 METHODOLOGY-class artifact-existence threshold).
      (e) content_sha256 of the retrofit_block extracted from re-read registry
          matches the input-pin-map-derived hash from build_retrofit_block.
    """
    with open(registry_path, "r", encoding="utf-8") as f:
        actual_text = f.read()  # (local)

    # Locate §VII.AQ.OP-PROJ section bounds
    op_proj_header = "## §VII.AQ.OP-PROJ — STRUCTURAL-EVEN-GRADING-BLINDNESS"          # (local)
    state_proj_header = "### §VII.AQ.STATE-PROJ — STRUCTURAL-EVEN-GRADING-BLINDNESS"  # (local)

    op_proj_start = actual_text.find(op_proj_header)  # (local)
    state_proj_start = actual_text.find(state_proj_header)  # (local)

    if op_proj_start == -1 or state_proj_start == -1 or state_proj_start <= op_proj_start:
        # Section bounds invalid — fail fast with diagnostic
        return {
            "predicate_a_block_present": False,
            "predicate_b_s91_w9_11_sha_cited": False,
            "predicate_c_carveout_cited": False,
            "predicate_d_substantive_line_count_ge_15": False,
            "predicate_e_content_sha_matches": False,
            "all_pass": False,
            "section_bounds": (op_proj_start, state_proj_start),
            "missing_substrings": ["section bounds invalid"],
            "section_text_len": 0,
            "retrofit_block_line_count": 0,
            "retrofit_block_content_sha256_actual": "",
            "retrofit_block_content_sha256_expected": expected_block_content_sha256,
        }

    section_text = actual_text[op_proj_start:state_proj_start]  # (local)

    # (a) retrofit block identifier substring present within section bounds.
    # The block starts with markdown bold `**CF-W9-11-1 ...` so the marker INCLUDES
    # the leading `**` to ensure extraction begins at the actual start-of-block
    # (predicate-(e) content_sha256 invariance requires byte-exact start alignment).
    block_marker = "**CF-W9-11-1 scheme-suffix retrofit (S92 W2"  # (local)
    predicate_a = block_marker in section_text  # (local)

    # (b) S91 W9-11 audit_sha256 cited
    s91_sha_marker = S91_W9_11_AUDIT_SHA  # (local)
    predicate_b = s91_sha_marker in section_text  # (local)

    # (c) carve-out clause from cross-pillar-bridge-anatomy.md cited
    # Acceptable forms: (i) explicit rule-file path with section title; (ii) carve-out
    # rule body text quoted; (iii) both. We require BOTH the rule-file cite AND the
    # carve-out clause text to be present, since the carve-out activation is the
    # load-bearing structural claim.
    carveout_path_marker = "cross-pillar-bridge-anatomy.md"  # (local)
    carveout_clause_marker = "Bridge-map-scheme suffix discipline"  # (local)
    carveout_body_marker = "MAY omit the suffix and cite the scheme-INDEPENDENCE theorem"  # (local)
    predicate_c = (
        carveout_path_marker in section_text
        and carveout_clause_marker in section_text
        and carveout_body_marker in section_text
    )  # (local)

    # (d) substantive_line_count of the retrofit block
    # Extract the retrofit block from section_text by locating its start + its end
    # (end = next section-level boundary OR end of section).
    block_start = section_text.find(block_marker)  # (local)
    retrofit_block_line_count = 0  # (local)
    retrofit_block_extracted = ""  # (local)
    if block_start != -1:
        # The block ends at the next `**` heading or at the **Cross-references** anchor.
        # We use the literal end-marker that is part of the block: the
        # `K=1 → K=2 advancement` line is the final substantive line of the block.
        # The simplest robust scheme: take everything from block_start until the next
        # `**Cross-references**:` substring inside section_text (the insertion
        # anchor is precisely before `**Cross-references**:`, so the block ends
        # at the empty-line break immediately before that anchor).
        end_marker = "**Cross-references**:"  # (local)
        end_offset = section_text.find(end_marker, block_start)  # (local)
        if end_offset == -1:
            retrofit_block_extracted = section_text[block_start:]
        else:
            retrofit_block_extracted = section_text[block_start:end_offset]
        # Count substantive lines (non-blank, stripped)
        retrofit_block_line_count = sum(
            1
            for line in retrofit_block_extracted.splitlines()
            if line.strip()
        )
    predicate_d = retrofit_block_line_count >= 15  # (local)

    # (e) content_sha256 of the retrofit block matches input-pin-map-derived hash.
    # Normalize: the on-disk extracted slice runs from block_start to the
    # "**Cross-references**:" anchor and includes the splice-separator newline(s) the
    # writer inserted between the block and the next section header. The build output
    # has no trailing splice newline. We compare the build output verbatim against
    # the extracted slice with trailing whitespace (newlines / spaces) stripped — the
    # block CONTENT is invariant under the splice separator (which is structural
    # connective tissue between block and next section header).
    extracted_trimmed = retrofit_block_extracted.rstrip()  # (local)
    expected_trimmed = (
        retrofit_block_expected.rstrip()
        if retrofit_block_expected is not None
        else ""
    )  # (local)
    actual_block_sha = text_sha256(extracted_trimmed)  # (local)
    # Recompute the expected SHA on the trimmed build output for invariance under
    # splice-separator perturbation.
    expected_block_sha_trimmed = text_sha256(expected_trimmed)  # (local)
    predicate_e = (
        actual_block_sha == expected_block_sha_trimmed
        and extracted_trimmed == expected_trimmed
    )  # (local)
    expected_block_sha = expected_block_sha_trimmed  # (local; report this value downstream)

    missing = []  # (local)
    if not predicate_a:
        missing.append(f"(a) block marker '{block_marker}' not found within §VII.AQ.OP-PROJ section")
    if not predicate_b:
        missing.append(f"(b) S91 W9-11 audit_sha256 '{s91_sha_marker[:16]}...' not cited")
    if not predicate_c:
        missing.append(
            f"(c) carve-out citation incomplete: "
            f"path={carveout_path_marker in section_text}, "
            f"clause={carveout_clause_marker in section_text}, "
            f"body={carveout_body_marker in section_text}"
        )
    if not predicate_d:
        missing.append(f"(d) substantive_line_count={retrofit_block_line_count} < 15")
    if not predicate_e:
        missing.append(
            f"(e) content_sha256 mismatch: "
            f"actual={actual_block_sha[:16]}..., expected={expected_block_sha[:16]}..."
        )

    # Cross-check substrate substrings (defense-in-depth)
    for sub in expected_substrate_substrings:
        if sub not in section_text:
            missing.append(f"(cross-check) substrate substring missing: '{sub[:80]}'")

    all_pass = predicate_a and predicate_b and predicate_c and predicate_d and predicate_e  # (local)

    return {
        "predicate_a_block_present": predicate_a,
        "predicate_b_s91_w9_11_sha_cited": predicate_b,
        "predicate_c_carveout_cited": predicate_c,
        "predicate_d_substantive_line_count_ge_15": predicate_d,
        "predicate_e_content_sha_matches": predicate_e,
        "all_pass": all_pass,
        "section_bounds": (op_proj_start, state_proj_start),
        "section_text_len": len(section_text),
        "retrofit_block_line_count": retrofit_block_line_count,
        "retrofit_block_content_sha256_actual": actual_block_sha,
        "retrofit_block_content_sha256_expected": expected_block_sha,
        "missing_substrings": missing,
    }


# ---------------------------------------------------------------------------
# Section 8 — EMIT: single canonical verdict line + companions
# ---------------------------------------------------------------------------
def append_verdict_line(
    verdict_path: Path,
    gate_id: str,
    verdict: str,
    value: str,
    scheme: str,
    convention: str,
    l_max: str,
    audit_sha: str,
    content_sha: str,
    sign_verdict: str,
    magnitude_verdict: str,
    regime_verdict: str,
    supersedes_audit_sha: str = "",
) -> None:
    """Append canonical line + dual-SHA row + 3-tuple row (S87+ schema-v2) atomically.

    Per gate-verdicts.md §"S87+ canonical form" + §"Schema-v2" + §"Option A —
    sig_5 remediation pathway under absolute verdict permanence":
      - canonical line: GATE_ID: PASS|FAIL|INFO -- value=... scheme=... convention=...
                       L_max=... [supersedes=<old_64char>] audit_sha256=<64>
                       content_sha256=<64> schema_version=S87+
      - dual-SHA companion row: # audit_sha256_short=<16> content_sha256_short=<16>
                       # GATE_ID dual-SHA companion row (W9a-99 split)
      - 3-tuple companion row: # sign_verdict=... magnitude_verdict=... regime_verdict=...
                       # GATE_ID 3-tuple annotation (S87 schema-v2)
      - (corrective only) in-session supersedes chain comment row: documents the
                       prior canonical line's audit_sha256 being superseded.

    Option A absolute verdict permanence: when supersedes_audit_sha is non-empty
    the function emits a `supersedes=<full-64-char>` token on the canonical line
    AND appends an `in_session_supersedes_chain` comment row pinning the prior
    audit_sha256. The prior canonical line is RETAINED on disk; consumers cite
    the LATEST non-superseded line per the Option A reading discipline.
    """
    supersedes_token = (
        f"supersedes={supersedes_audit_sha} "
        if supersedes_audit_sha
        else ""
    )
    canonical = (
        f"{gate_id}: {verdict} -- value='{value}' "
        f"scheme={scheme} convention={convention} L_max={l_max} "
        f"{supersedes_token}"
        f"audit_sha256={audit_sha} content_sha256={content_sha} schema_version=S87+\n"
    )
    dual_sha_row = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {gate_id} dual-SHA companion row (W9a-99 split); "
        f"[VERIFY] trigger; CF-W9-11-1 §VII.AQ.OP-PROJ scheme-suffix retrofit per "
        f"cross-pillar-bridge-anatomy.md §\"Bridge-map-scheme suffix discipline\" carve-out clause\n"
    )
    three_tuple_row = (
        f"# sign_verdict={sign_verdict} magnitude_verdict={magnitude_verdict} "
        f"regime_verdict={regime_verdict} "
        f"# {gate_id} 3-tuple annotation (S87 schema-v2); 5-predicate (a)..(e) conjunction PASS-AND aggregation\n"
    )
    chain_row = ""
    if supersedes_audit_sha:
        chain_row = (
            f"# in_session_supersedes_chain corrective_audit_sha256={audit_sha} "
            f"prior_audit_sha256={supersedes_audit_sha} "
            f"# {gate_id} Option A in-session corrective emission per gate-verdicts.md "
            f"§\"Option A — sig_5 remediation pathway under absolute verdict permanence\"; "
            f"prior canonical line retained on disk per verdict permanence; "
            f"consumers cite LATEST non-superseded line; "
            f"reason=predicate_e_boundary_normalization_bugfix_splice_separator_invariance\n"
        )
    with open(verdict_path, "a", encoding="utf-8", newline="\n") as f:
        f.write(canonical)
        f.write(dual_sha_row)
        f.write(three_tuple_row)
        if chain_row:
            f.write(chain_row)
        f.flush()
        os.fsync(f.fileno())


# ---------------------------------------------------------------------------
# Section 9 — Main: single-shot AFTER-pattern orchestration
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    # ============================================================
    # PHASE 0: Banner + input-pin logging (first 20 lines of stdout
    # per math-scripts.md / script-template canonical requirement)
    # ============================================================
    print("=" * 78)
    print(f"S92 W2 CF-W9-11-1 — §VII.AQ.OP-PROJ Scheme-Suffix Retrofit")
    print(f"Gate ID: {GATE_ID}")
    print(f"Agent: mack-cosmic-bridge (sole-writer per feedback_mack-bridge-role.md)")
    print(f"Pattern: single-shot AFTER (build → write → re-read → verify → emit)")
    print("=" * 78)

    # Input-pin SHA-256 logging
    registry_pre_sha = file_sha256(REGISTRY_PATH)             # (local)
    canonical_sha = file_sha256(CANONICAL_CONSTANTS)          # (local)
    cross_pillar_sha = file_sha256(CROSS_PILLAR_RULE)         # (local)
    registry_landing_sha = file_sha256(REGISTRY_LANDING_RULE) # (local)
    s91_verdicts_sha = file_sha256(S91_VERDICTS_PATH)         # (local)
    plan_w2_sha = file_sha256(PLAN_W2_PATH)                   # (local)
    script_sha = file_sha256(SCRIPT_PATH)                     # (local)

    # (local) Option A scan: detect any prior canonical line for this gate_id in
    # s92_gate_verdicts.txt. If found, the LATEST non-superseded prior audit_sha256
    # is the supersedes target for the corrective emission per
    # gate-verdicts.md §"Option A — sig_5 remediation pathway under absolute verdict
    # permanence" rule (5): forward emission discipline.
    supersedes_audit_sha = ""  # (local)
    prior_verdict_line = ""    # (local)
    if VERDICT_PATH.exists():
        with open(VERDICT_PATH, "r", encoding="utf-8") as f:
            verdict_lines = f.readlines()  # (local)
        # Scan for prior canonical lines matching this gate_id (not the comment rows)
        prior_canonicals = [
            ln for ln in verdict_lines
            if ln.startswith(PRIOR_FAIL_AUDIT_SHA_PATTERN_PREFIX)
        ]  # (local)
        if prior_canonicals:
            # Latest non-superseded line is the one whose audit_sha256 is NOT named
            # in any other line's `supersedes=` token.
            superseded_shas = set()  # (local)
            for ln in prior_canonicals:
                # Extract `supersedes=<sha>` if present
                if " supersedes=" in ln:
                    sup_token_start = ln.find(" supersedes=") + len(" supersedes=")
                    sup_token_end = ln.find(" ", sup_token_start)
                    if sup_token_end == -1:
                        sup_token_end = len(ln)
                    superseded_shas.add(ln[sup_token_start:sup_token_end].strip())
            latest_non_superseded = ""  # (local)
            for ln in reversed(prior_canonicals):
                if " audit_sha256=" in ln:
                    audit_start = ln.find(" audit_sha256=") + len(" audit_sha256=")
                    audit_end = ln.find(" ", audit_start)
                    if audit_end == -1:
                        audit_end = len(ln)
                    sha_val = ln[audit_start:audit_end].strip()
                    if sha_val and sha_val not in superseded_shas:
                        latest_non_superseded = sha_val
                        prior_verdict_line = ln.strip()
                        break
            supersedes_audit_sha = latest_non_superseded

    print(f"\n[INPUT-PIN MAP]")
    print(f"  registry_pre_edit_sha256             = {registry_pre_sha}")
    print(f"  canonical_constants_py_sha256        = {canonical_sha}")
    print(f"  cross_pillar_bridge_anatomy_md_sha256 = {cross_pillar_sha}")
    print(f"  registry_landing_md_sha256           = {registry_landing_sha}")
    print(f"  s91_gate_verdicts_txt_sha256          = {s91_verdicts_sha}")
    print(f"  session_92_plan_w2_md_sha256         = {plan_w2_sha}")
    print(f"  script_sha256                        = {script_sha}")
    print(f"  s91_w9_11_audit_sha256 (canonical pin) = {S91_W9_11_AUDIT_SHA}")
    if supersedes_audit_sha:
        print(f"\n[OPTION A SUPERSEDES DETECTION]")
        print(f"  prior_canonical_line for {GATE_ID} found in {VERDICT_PATH.name}")
        print(f"  latest_non_superseded_audit_sha256 = {supersedes_audit_sha}")
        print(f"  corrective emission will carry supersedes=<full-64-char> token + in_session_supersedes_chain row")
    else:
        print(f"\n[OPTION A SUPERSEDES DETECTION]")
        print(f"  no prior canonical line for {GATE_ID}; fresh emission (no supersedes tag)")

    # ============================================================
    # PHASE 1: BUILD (pure-function, no I/O)
    # ============================================================
    print(f"\n[PHASE 1: BUILD (pure-function)]")
    retrofit_block = build_retrofit_block()
    # Canonical content_sha256 is computed over the trimmed block (invariant under
    # splice-separator newlines that the writer adds between block and next section
    # header). This matches the predicate-(e) verifier's normalization.
    retrofit_block_canonical = retrofit_block.rstrip()  # (local)
    retrofit_block_sha = text_sha256(retrofit_block_canonical)  # (local; canonical)
    retrofit_block_sha_untrimmed = text_sha256(retrofit_block)  # (local; diagnostic only)
    block_line_count = sum(1 for ln in retrofit_block.splitlines() if ln.strip())
    print(f"  retrofit_block_built: {len(retrofit_block)} bytes, "
          f"{block_line_count} substantive lines")
    print(f"  retrofit_block_content_sha256 (trimmed-canonical): {retrofit_block_sha}")
    print(f"  retrofit_block_content_sha256 (untrimmed-diagnostic): {retrofit_block_sha_untrimmed}")

    insertion_anchor = build_anchor_for_insertion("")  # anchor is anchor-text-based; no registry needed here  # (local)

    # ============================================================
    # PHASE 2: Read registry; locate insertion point; assemble new content
    # ============================================================
    print(f"\n[PHASE 2: LOCATE INSERTION POINT]")
    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        registry_text = f.read()  # (local)
    print(f"  registry_pre_edit_bytes: {len(registry_text)}")

    # Locate §VII.AQ.OP-PROJ section bounds for sanity check
    op_proj_header = "## §VII.AQ.OP-PROJ — STRUCTURAL-EVEN-GRADING-BLINDNESS"           # (local)
    state_proj_header = "### §VII.AQ.STATE-PROJ — STRUCTURAL-EVEN-GRADING-BLINDNESS"   # (local)
    op_proj_start = registry_text.find(op_proj_header)                                 # (local)
    state_proj_start = registry_text.find(state_proj_header)                           # (local)
    print(f"  §VII.AQ.OP-PROJ header offset: {op_proj_start}")
    print(f"  §VII.AQ.STATE-PROJ companion header offset: {state_proj_start}")

    # Idempotency check: if the retrofit block is already present, write is a no-op
    block_marker = "CF-W9-11-1 scheme-suffix retrofit (S92 W2"                          # (local)
    section_text = (
        registry_text[op_proj_start:state_proj_start]
        if op_proj_start != -1 and state_proj_start != -1 and state_proj_start > op_proj_start
        else ""
    )                                                                                  # (local)
    already_retrofitted = block_marker in section_text                                  # (local)
    print(f"  already_retrofitted: {already_retrofitted}")

    if already_retrofitted:
        print(f"  IDEMPOTENT: retrofit block already present; skipping write.")
        new_registry_text = registry_text  # (local)
        wrote_bytes = 0  # (local)
    else:
        # Locate insertion anchor within §VII.AQ.OP-PROJ section.
        # The anchor "\n\n**Cross-references**:" occurs ~20 times in the registry
        # (one per §VII slot). We scan FROM op_proj_start so the first match is the
        # OP-PROJ section's Cross-references header, not a later section's.
        anchor_offset = registry_text.find(insertion_anchor, op_proj_start)             # (local)
        if anchor_offset == -1:
            print(f"  FAIL: insertion anchor not found in registry text from op_proj_start={op_proj_start}")
            print(f"  expected anchor: {insertion_anchor[:80]}...")
            sys.exit(0)  # exit 0 — script health PASS, verdict FAIL
        if not (op_proj_start < anchor_offset < state_proj_start):
            print(f"  FAIL: insertion anchor offset {anchor_offset} not within "
                  f"§VII.AQ.OP-PROJ bounds ({op_proj_start}, {state_proj_start})")
            sys.exit(0)

        # Insert retrofit_block immediately BEFORE "**Cross-references**:" anchor.
        # The anchor is the substring "Stage-2-style upgrade extends Reading A
        # robustness check to the deformed `D_K + A` evaluator.\n\n**Cross-references**:"
        # We split at the "\n\n**Cross-references**:" boundary and insert the block
        # between the closing sentence of Stage-2-style upgrade clause and the
        # **Cross-references** header.
        split_marker = "\n\n**Cross-references**:"                                       # (local)
        split_offset = registry_text.find(split_marker, op_proj_start)                   # (local)
        if split_offset == -1 or split_offset >= state_proj_start:
            print(f"  FAIL: split marker '{split_marker[:32]}...' not found in OP-PROJ section")
            sys.exit(0)

        # Compose new registry text: [pre-split] + retrofit_block + "\n" + [post-split (Cross-refs onward)]
        new_registry_text = (
            registry_text[: split_offset + 2]  # include preceding "\n\n"
            + retrofit_block
            + "\n"
            + registry_text[split_offset + 2:]  # "**Cross-references**:..." onward
        )
        wrote_bytes = len(new_registry_text) - len(registry_text)
        print(f"  insertion_split_offset: {split_offset}")
        print(f"  new_registry_bytes: {len(new_registry_text)} (delta +{wrote_bytes})")

        # ============================================================
        # PHASE 3: WRITE atomic + fsync
        # ============================================================
        print(f"\n[PHASE 3: WRITE atomic + fsync]")
        write_atomic_with_fsync(REGISTRY_PATH, new_registry_text)
        print(f"  registry written to disk + fsync OK")

    # ============================================================
    # PHASE 4: RE-READ + VERIFY (5-predicate conjunction)
    # ============================================================
    print(f"\n[PHASE 4: RE-READ + VERIFY]")
    expected_substrate_substrings = [
        # Defensive cross-checks: substrings that MUST appear in §VII.AQ.OP-PROJ
        # for the retrofit to be substantively complete
        "CF-W9-11-1 scheme-suffix retrofit (S92 W2",
        S91_W9_11_AUDIT_SHA,
        "S91-BRIDGE-MAP-SCHEME-INDEPENDENCE-AUDIT",
        "Bridge-map-scheme suffix discipline",
        "MAY omit the suffix and cite the scheme-INDEPENDENCE theorem",
        "STRUCTURALLY RETIRED at this slot",
        "max_pairwise_diff = 0.000000e+00",
        "APS-1975 secondary-class",
        "Cheeger-Simons 1985 differential-character",
        "Bismut-Cheeger η-form",
    ]
    verify_report = verify_section_matches(
        REGISTRY_PATH,
        retrofit_block,
        expected_substrate_substrings,
        retrofit_block_sha,
    )
    for k, v in verify_report.items():
        if k == "missing_substrings":
            if v:
                print(f"  {k}: ({len(v)} items)")
                for m in v[:10]:
                    print(f"    - {m[:140]}")
            else:
                print(f"  {k}: [] (all present)")
        else:
            print(f"  {k}: {v}")

    # Predicate aggregate
    pred_a = verify_report["predicate_a_block_present"]
    pred_b = verify_report["predicate_b_s91_w9_11_sha_cited"]
    pred_c = verify_report["predicate_c_carveout_cited"]
    pred_d = verify_report["predicate_d_substantive_line_count_ge_15"]
    pred_e = verify_report["predicate_e_content_sha_matches"]
    all_pass = pred_a and pred_b and pred_c and pred_d and pred_e

    # ============================================================
    # PHASE 5: Compute audit_sha256 over ordered input-pin map
    # ============================================================
    print(f"\n[PHASE 5: AUDIT CLOSURE]")
    registry_post_sha = file_sha256(REGISTRY_PATH)  # (local)
    print(f"  registry_post_edit_sha256: {registry_post_sha}")

    input_pin_map = {
        "gate_id": GATE_ID,
        "session": SESSION,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "trigger": "[VERIFY]",
        "classification": "NON-PHONONIC",
        "methodology_class_per_wave_classification_md_M1_M4": "True",
        "agent_sole_writer": "mack-cosmic-bridge",
        # File-content pins
        "canonical_constants_py_sha256": canonical_sha,
        "cross_pillar_bridge_anatomy_md_sha256": cross_pillar_sha,
        "registry_landing_md_sha256": registry_landing_sha,
        "s91_gate_verdicts_txt_sha256": s91_verdicts_sha,
        "session_92_plan_w2_md_sha256": plan_w2_sha,
        "script_sha256": script_sha,
        "registry_pre_edit_sha256": registry_pre_sha,
        "registry_post_edit_sha256": registry_post_sha,
        # Upstream verdict pin (the canonical S91 W9-11 audit_sha256)
        "s91_w9_11_canonical_audit_sha256": S91_W9_11_AUDIT_SHA,
        "s91_w9_11_gate_name": S91_W9_11_GATE_NAME,
        # Retrofit-block content pin
        "retrofit_block_content_sha256": retrofit_block_sha,
        "retrofit_block_line_count": str(block_line_count),
        # Predicate outcomes
        "predicate_a_block_present": str(pred_a),
        "predicate_b_s91_w9_11_sha_cited": str(pred_b),
        "predicate_c_carveout_cited": str(pred_c),
        "predicate_d_substantive_line_count_ge_15": str(pred_d),
        "predicate_e_content_sha_matches": str(pred_e),
        "all_pass": str(all_pass),
    }
    audit_sha = closure_hash(input_pin_map)  # (local)
    print(f"  audit_sha256 = {audit_sha}")
    print(f"  content_sha256 (retrofit block) = {retrofit_block_sha}")

    # ============================================================
    # PHASE 6: Emit verdict + JSON sidecar
    # ============================================================
    print(f"\n[PHASE 6: EMIT VERDICT]")
    if all_pass:
        verdict = "PASS"
        # Composite collapse rule per gate-verdicts.md §"Composite-collapse rule":
        # sign_verdict=PASS (predicted in plan §W2-1: predicate conjunction PASS)
        # magnitude_verdict=PASS (5-of-5 predicates PASS within zero tolerance)
        # regime_verdict=VALID (methodology-class registry-text edit; no regime axis)
        sign_verdict = "PASS"
        magnitude_verdict = "PASS"
        regime_verdict = "VALID"
        value_string = (
            f"retrofit_complete=True;"
            f"predicates_5_of_5_PASS=True;"
            f"predicate_a={pred_a};"
            f"predicate_b={pred_b};"
            f"predicate_c={pred_c};"
            f"predicate_d={pred_d};"
            f"predicate_e={pred_e};"
            f"block_line_count={block_line_count};"
            f"retrofit_block_content_sha256={retrofit_block_sha[:16]};"
            f"s91_w9_11_input_pin={S91_W9_11_AUDIT_SHA[:16]};"
            f"already_retrofitted={already_retrofitted};"
            f"carveout_active_at_slot=True;"
            f"bridge_map_scheme_suffix_MANDATORY_clause_STRUCTURALLY_RETIRED_at_this_slot=True;"
            f"single_shot_AFTER_pattern=True"
        )
    else:
        verdict = "FAIL"
        sign_verdict = "FAIL"
        magnitude_verdict = "FAIL"
        regime_verdict = "VALID"
        missing_str = ";".join(verify_report["missing_substrings"][:5]) if verify_report["missing_substrings"] else "none"
        value_string = (
            f"retrofit_incomplete;"
            f"predicate_a={pred_a};"
            f"predicate_b={pred_b};"
            f"predicate_c={pred_c};"
            f"predicate_d={pred_d};"
            f"predicate_e={pred_e};"
            f"block_line_count={block_line_count};"
            f"missing={missing_str};"
            f"already_retrofitted={already_retrofitted}"
        )

    print(f"  verdict = {verdict}")
    print(f"  value (first 200 chars): {value_string[:200]}")
    print(f"  3-tuple = sign={sign_verdict} magnitude={magnitude_verdict} regime={regime_verdict}")

    append_verdict_line(
        VERDICT_PATH,
        GATE_ID,
        verdict,
        value_string,
        SCHEME,
        CONVENTION,
        L_MAX,
        audit_sha,
        retrofit_block_sha,
        sign_verdict,
        magnitude_verdict,
        regime_verdict,
        supersedes_audit_sha=supersedes_audit_sha,
    )

    # JSON sidecar — predicate outcomes + provenance
    sidecar = {
        "gate_id": GATE_ID,
        "session": SESSION,
        "wave": "W2",
        "trigger": "[VERIFY]",
        "classification": "NON-PHONONIC",
        "agent_sole_writer": "mack-cosmic-bridge",
        "verdict": verdict,
        "value": value_string,
        "audit_sha256": audit_sha,
        "content_sha256": retrofit_block_sha,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "predicates": {
            "a_block_present": pred_a,
            "b_s91_w9_11_sha_cited": pred_b,
            "c_carveout_cited": pred_c,
            "d_substantive_line_count_ge_15": pred_d,
            "e_content_sha_matches": pred_e,
        },
        "all_pass": all_pass,
        "input_pin_map": input_pin_map,
        "verify_report": {
            "section_bounds": list(verify_report["section_bounds"]),
            "section_text_len": verify_report["section_text_len"],
            "retrofit_block_line_count": verify_report["retrofit_block_line_count"],
            "retrofit_block_content_sha256_actual": verify_report["retrofit_block_content_sha256_actual"],
            "retrofit_block_content_sha256_expected": verify_report["retrofit_block_content_sha256_expected"],
            "missing_substrings": verify_report["missing_substrings"],
        },
        "structural_provenance": {
            "rule_carve_out_clause": "cross-pillar-bridge-anatomy.md §\"Bridge-map-scheme suffix discipline\" lines 129-151; carve-out clause line 137",
            "upstream_pass_pin_S91_W9_11": S91_W9_11_AUDIT_SHA,
            "upstream_pass_pin_S91_W9_11_gate": S91_W9_11_GATE_NAME,
            "upstream_pass_pin_S91_W9_11_verdict_line": "computations/session-91/s91_gate_verdicts.txt:218",
            "upstream_pass_pin_S90_W7_CF_55": "f634be0d942241095e40ce71562b69fee522faaa520c9ce861844c15f02a8f77",
            "upstream_pass_pin_S90_W7_CF_55_gate": "S90-AQ-SECONDARY-CLASS-SCHEME-DISCRIMINATOR",
        },
        "substrate_framing_direction": (
            "substrate IS A_K scheme-INDEPENDENCE (Reading A bit-identity at L_max=12) → "
            "S91 W9-11 PASS at machine precision (Δ_scheme = 0.000e+00 EXACTLY) → "
            "cross-pillar-bridge-anatomy.md §\"Bridge-map-scheme suffix discipline\" "
            "carve-out clause activated (structural-output-type independence pre-established) → "
            "registry-text retrofit applied at §VII.AQ.OP-PROJ (audit-layer F-functor image)"
        ),
        "methodology_class_M1_M4_declaration": {
            "M1_PASS_predicate_artifact_existence_with_substantive_content": True,
            "M2_producing_operation_Edit_Write_on_registry_text": True,
            "M3_source_of_truth_verbatim_from_S91_W9_11_and_rule_body": True,
            "M4_allowlist_membership_orchestrator_append_at_plan_freeze_required": True,
        },
        "wall_time_seconds": time.time() - t0,
    }
    with open(DATA_JSON_PATH, "w", encoding="utf-8", newline="\n") as f:
        json.dump(sidecar, f, indent=2, sort_keys=False, ensure_ascii=False)
        f.flush()
        os.fsync(f.fileno())
    print(f"\n  JSON sidecar written: {DATA_JSON_PATH}")

    # Final 4-tuple emission
    tag = (
        f"(value='{value_string[:80]}...', scheme={SCHEME}, "
        f"convention={CONVENTION[:60]}..., L_max={L_MAX})"
    )
    print(f"\n{tag}")

    wall = time.time() - t0
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")

    # Per math-scripts.md §"Exit Codes and Verdict Semantics":
    #   verdict is data; exit 0 regardless of PASS/FAIL/INFO (script health == OK)
    return 0


if __name__ == "__main__":
    sys.exit(main())
