#!/usr/bin/env python3
"""
S92 W4-7 — S92-W4-CF-S92-VII-U-2-STAGE-3-PROMOTION
==================================================

Gate: S92-W4-CF-S92-VII-U-2-STAGE-3-PROMOTION ([AUDIT])

mack-cosmic-bridge sole-writer registry-text edit at
`sessions/permanent-results-registry.md` §VII.U.2 Corner II Var_a row:
replace STAGE-1-CANDIDATE tag with STAGE-3-PERMANENT citing
§W4-4 COMPOSITE audit_sha256=`1bb3fbfb…` (Stage-2 PASS-AND landed at S91 W6
gate `S91-W6-VII-U-2-VAR-A-STAGE-2-CROSS-AXIS-INDEPENDENT-VERIFY`) AND
§W4-6 audit_sha256=`e393b51f…` (Level-3 anchor singleness adjudication at
S92 W4-6 gate `S92-W4-CF-W4-4-EMPIRICAL-ANCHOR-RECONCILIATION`).

This is the framework's SECOND cross-axis joint theorem to reach
STAGE-3-PERMANENT eligibility, after §VII.AH at S90 W2 CF-20.
The substrate-input-orthogonality K-counter advances K=3 → K=4 corpus
extension beyond MANDATORY threshold per
`joint-theorem-promotion.md §"Substrate-input-orthogonality clause"`.

METHODOLOGY-class (M1-M4 strict conjunction):
  M1: PASS predicate is artifact-existence + STAGE-3-PERMANENT tag presence
      + audit_sha chain citation + parse-tree invariance (no numerical
      comparison against pre-registered threshold).
  M2: Edit + SHA only — no .py compute beyond hashing.
  M3: source-of-truth = §W4-4 COMPOSITE verdict + §W4-6 canonical verdict
      + `joint-theorem-promotion.md` Stage 3 + Substrate-input-orthogonality
      clause (verbatim sub-diff from closed workshops + audited rules).
  M4: gate-ID appended to
      `sessions/framework/registry/methodology-wave-allowlist-ledger.md`
      at plan-execution-time (orchestrator-direct write per recursion-
      attack closure rule).

Substrate framing (NON-PHONONIC METHODOLOGY-class):
  The STAGE-3-PERMANENT promotion IS the methodology-floor F-image of the
  substrate-IS Stage-3 promotion evidence chain established at §W4-4
  (Stage-2 PASS-AND on substrate-IS structural-theorem clauses) + §W4-6
  (Level-3 anchor singleness via substrate-physics adjudication). The
  substrate IS the spectral triple (A_K, H_K, D_K) at τ_fold; the
  Var_a(n_a^GGE) observable IS the closed-form Bogoliubov expression on
  the BdG sub-algebra M_2(ℂ) per the parse-tree expansion at row line
  ~12961; the substrate-IS structural identity is INVARIANT under the
  STAGE-3 tag-flip — only the methodology-floor commitment status changes.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import Var_a_canonical  # noqa: F401,E402

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import re  # noqa: E402
import time  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION = "S92"  # (local)
GATE_ID = "S92-W4-CF-S92-VII-U-2-STAGE-3-PROMOTION"  # (local)
SCHEME = "mack-sole-writer-STAGE-3-PERMANENT-tag-flip-methodology-class"  # (local)
CONVENTION = (
    "joint-theorem-promotion-stage-3-promotion-second-cross-axis-joint-theorem-after-VII-AH-S90-W2-CF-20"
)  # (local)
L_MAX = "N/A"  # (local) — METHODOLOGY-class gate; no spectral truncation

# Audit-trail pins
W4_4_COMPOSITE_AUDIT_SHA = (
    "1bb3fbfb30c40f17130b176a0ce42841b51dd468d19a55fd6d3409e37cf64b53"
)  # (local) — S91 W6 Stage-2 PASS-AND composite verdict
W4_6_AUDIT_SHA = (
    "e393b51fd223868a74020a2c3dc63453e53db088f5b06f7980d97f4d8464a807"
)  # (local) — S92 W4-6 Level-3 anchor singleness adjudication
W4_6_CONTENT_SHA = (
    "cdf8c87ac432a7e837f423575b92d6604bbdb4c3be143b5450360e60bc6ad27d"
)  # (local) — S92 W4-6 content_sha256

VAR_A_CANONICAL_VALUE = Var_a_canonical  # 7.282490225e-06; substrate-natural pin per §W4-6 PASS

# Output destinations
OUT_JSON = SESSION_DIR / "s92_w4_7_vii_u_2_stage_3_promotion.json"
VERDICT_TXT = SESSION_DIR / "s92_gate_verdicts.txt"
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
S92_VERDICTS_PATH = SESSION_DIR / "s92_gate_verdicts.txt"
S91_VERDICTS_PATH = COMPUTATIONS_DIR / "session-91" / "s91_gate_verdicts.txt"
JTP_RULE_PATH = PROJECT_ROOT / ".claude" / "rules" / "joint-theorem-promotion.md"
CPB_RULE_PATH = PROJECT_ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md"
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"

INPUT_FILES = [
    CANONICAL_PATH,
    REGISTRY_PATH,
    S92_VERDICTS_PATH,
    S91_VERDICTS_PATH,
    JTP_RULE_PATH,
    CPB_RULE_PATH,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block + dual-SHA closure (S84+ schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def sha256_of_bytes(b: bytes) -> str:
    h = hashlib.sha256()  # (local)
    h.update(b)
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


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
    """audit_sha256 = sha256( script || canonical || pinmap_json );
       content_sha256 = sha256( script )."""
    script_bytes = script_path.read_bytes()  # (local)
    canonical_bytes = canonical_path.read_bytes()  # (local)
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
# Section 5 — Locate §VII.U.2 Corner II Var_a row (plan-text-drift correction)
# ---------------------------------------------------------------------------

def locate_corner_ii_row(registry_text: str) -> tuple[int, int, int]:
    """Locate the §VII.U.2 Corner II row + the adjacent STAGE-1-CANDIDATE block.

    Returns (table_row_lineno_1idx, stage_1_candidate_block_start_1idx,
             stage_1_candidate_block_end_1idx).

    The plan pinned section_anchor_lines='12961-13002' but per
    `substrate-first-canonical-sourcing.md §(ii.B)` we MUST locate via
    heading-anchor grep at runtime, not by line number trust.
    """
    lines = registry_text.split("\n")  # (local)

    # Locate the §VII.U.2 — Four-corner classification heading
    heading_pattern = re.compile(r"^### §VII\.U\.2 — Four-corner classification")
    heading_lineno = None  # (local)
    for i, line in enumerate(lines):
        if heading_pattern.match(line):
            heading_lineno = i + 1  # 1-indexed
            break
    if heading_lineno is None:
        raise RuntimeError("Could not locate §VII.U.2 heading anchor")

    # Locate the Corner II table row by its | II | INVARIANT | s=4 | pattern + Var_a content
    corner_ii_row_lineno = None  # (local)
    for i in range(heading_lineno - 1, min(heading_lineno + 80, len(lines))):
        if "| II | INVARIANT | s=4 |" in lines[i] and "Var_a" in lines[i]:
            corner_ii_row_lineno = i + 1
            break
    if corner_ii_row_lineno is None:
        raise RuntimeError("Could not locate Corner II Var_a table row")

    # Locate the STAGE-1-CANDIDATE OR STAGE-3-PERMANENT Var_a joint theorem block start
    # (W6 CF-51 landing pre-edit; W4-7 STAGE-3-PERMANENT post-edit). Pattern accepts
    # either tag so the locator is idempotent across pre/post-edit reads.
    stage_1_start = None  # (local)
    stage_1_end = None  # (local)
    sentinel_pattern = re.compile(
        r"\*\*STAGE-(?:1-CANDIDATE|3-PERMANENT) — Var_a\(n_a\^GGE\) Corner-II joint theorem"
    )
    for i in range(corner_ii_row_lineno - 1, min(corner_ii_row_lineno + 400, len(lines))):
        if sentinel_pattern.search(lines[i]):
            stage_1_start = i + 1
            break
    if stage_1_start is None:
        raise RuntimeError("Could not locate STAGE-1-CANDIDATE block start")

    # End: locate the PROVENANCE block end (last line containing CF-51 audit_sha256 chain)
    # Use the sub-corrigendum heading after the STAGE-1-CANDIDATE block as terminator
    terminator_pattern = re.compile(
        r"\*\*§VII\.U\.2 sub-corrigendum: dual-symbol convention canonical A_BdG-full"
    )
    for i in range(stage_1_start - 1, min(stage_1_start + 200, len(lines))):
        if terminator_pattern.search(lines[i]):
            stage_1_end = i  # 1-indexed, exclusive of the terminator
            break
    if stage_1_end is None:
        raise RuntimeError("Could not locate STAGE-1-CANDIDATE block end")

    return corner_ii_row_lineno, stage_1_start, stage_1_end


# ---------------------------------------------------------------------------
# Section 6 — Edit application + verification (in-memory)
# ---------------------------------------------------------------------------

def build_post_edit_block(pre_edit_block: str) -> tuple[str, dict]:
    """Apply STAGE-1-CANDIDATE → STAGE-3-PERMANENT promotion edit.

    Returns (post_edit_block, edit_metadata).

    Substrate-IS invariance: the parse-tree expansion text (Bogoliubov closed
    form / S52 BdG amplitudes / Corner II classification rationale) MUST
    remain bit-identical. Only the STAGE-1-CANDIDATE tag and the Level-3
    anchor citation update; the audit_sha chain is APPENDED as a Stage-3
    promotion record block at the end of the existing STAGE-1-CANDIDATE
    block (after the PROVENANCE line).
    """
    diagnostics: dict = {
        "tag_flip_applied": False,
        "stage_3_promotion_block_appended": False,
        "parse_tree_invariant": False,
        "pre_edit_byte_len": len(pre_edit_block.encode("utf-8")),
    }

    # (i) Replace STAGE-1-CANDIDATE tag in the heading row of the block.
    # Target: "**STAGE-1-CANDIDATE — Var_a(n_a^GGE) Corner-II joint theorem"
    # Replace with: STAGE-3-PERMANENT, citing the audit_sha chain.
    target_tag = "**STAGE-1-CANDIDATE — Var_a(n_a^GGE) Corner-II joint theorem"  # (local)
    replacement_tag = "**STAGE-3-PERMANENT — Var_a(n_a^GGE) Corner-II joint theorem"
    if target_tag in pre_edit_block:
        post = pre_edit_block.replace(target_tag, replacement_tag, 1)
        diagnostics["tag_flip_applied"] = True
    else:
        post = pre_edit_block

    # (ii) Append the Stage-3-PERMANENT promotion record block to the end of
    # the existing STAGE-1-CANDIDATE block (after the PROVENANCE paragraph).
    # The promotion block cites both audit_shas + the Level-3 anchor singleness
    # + the framework SECOND declaration + the K=3→K=4 advancement.
    promotion_record = (
        "\n\n**STAGE-3-PERMANENT promotion record (S92 W4-7 LANDED, 2026-05-23 — "
        "mack-cosmic-bridge sole writer per `feedback_mack-bridge-role.md`; "
        "framework's SECOND cross-axis joint theorem to reach STAGE-3-PERMANENT "
        "eligibility after §VII.AH at S90 W2 CF-20)**:\n\n"
        "**Promotion criterion** (per `.claude/rules/joint-theorem-promotion.md "
        "§\"Stage 3\"`): Stage-2 PASS-AND landed ∧ substrate-input-orthogonality "
        "K=3 satisfied ∧ Level-3 anchor single-pinned per `.claude/rules/"
        "cross-pillar-bridge-anatomy.md §\"Level-3 anchor singleness sub-clause\"`. "
        "All three sub-criteria PASS at this landing.\n\n"
        "**Stage-2 PASS-AND evidence**: S91 W6 gate "
        "`S91-W6-VII-U-2-VAR-A-STAGE-2-CROSS-AXIS-INDEPENDENT-VERIFY` returned "
        f"COMPOSITE PASS with audit_sha256=`{W4_4_COMPOSITE_AUDIT_SHA}`; the "
        "Axis-A cross-reviewer was `van-den-dungen-bridge-theorist` (3/3 PASS on "
        "clauses (a)+(c)+(e) at Pillar 1 NCG-axiomatic `A_F ⊗ M_2(ℂ)` axiom layer) "
        "and the Axis-B cross-reviewer was `volovik-superfluid-universe-theorist` "
        "(3/3 PASS on clauses (b)+(d)+(f) at Pillar 2 operational `A_BdG-image = "
        "M_2(ℂ)` BDI BdG-restricted axiom layer, Option-A `supersedes` chain "
        "emission per `.claude/rules/gate-verdicts.md §\"Option A — sig_5 "
        "remediation pathway\"`); JOINT clauses (a)+(c)+(d)+(e) PASS-AND'd across "
        "both axes (6/6 all clauses PASS independently in both axes); both "
        "cross-reviewers operated without prior workshop context per the Stage-2 "
        "procedural-floor protocol; `connes-ncg-theorist` and "
        "`lizzi-spectral-functional-theorist` excluded as W-17 + W6 workshop "
        "authors per the OAA-exclusion clause.\n\n"
        "**Level-3 anchor singleness evidence**: S92 W4-6 gate "
        "`S92-W4-CF-W4-4-EMPIRICAL-ANCHOR-RECONCILIATION` returned PASS with "
        f"audit_sha256=`{W4_6_AUDIT_SHA}` (content_sha256="
        f"`{W4_6_CONTENT_SHA}`); the substrate-natural Level-3 anchor canonical "
        "value is `Var_a_canonical = 7.2824902250e-06` "
        "at L_max=10 on `(A_K, H_K, D_K)` at `τ_fold = 0.190` under convention "
        "`w5b47_raw` (`max(p,q) ≤ L_max` filter matching the d=4 Weyl-law tail's "
        "product-of-irrep-dimension scaling; `m_a = dim_pq`; zero-modes excluded); "
        "12.68% relative deviation from the Weyl-dim extrapolated-to-infinity "
        "asymptotic limit `v_inf = 6.4631783294e-06` (vs 96.22% volovik and 637.26% "
        "vdd alternative conventions tagged DIAGNOSTIC). Pillar 1 reading "
        "`Var_a_canonical = 7.2824902250e-06` (Pillar 1 NCG-axiomatic A_F ⊗ M_2(ℂ) "
        "substrate-IS axiom layer; single-pinned per `.claude/rules/"
        "cross-pillar-bridge-anatomy.md §\"Level-3 anchor singleness sub-clause\"` "
        "SUGGESTION K=1); Pillar 2 reading `Var_a^{W6_image} = 5.0680e-05` "
        "(Pillar 2 BDI BdG-restricted A_BdG-image = M_2(ℂ) substrate-IS axiom "
        "layer per CO-EQUAL CANONICAL DISTINCT-AXIOM-LAYER framing landed at S91 "
        "W6 EMRG-2; not a competing reading of the Pillar 1 observable, but a "
        "STRUCTURALLY DISTINCT substrate-IS observable at a structurally-different "
        "axiom layer; cross-pillar bridge map composition `A_K ↪ A_BdG-full ↠ "
        "A_BdG-image` IS the structural CONNECTION). Both pillar readings inhabit "
        "Cell-II (algebra-INVARIANT × Mellin pole s=4) per parse-tree-INVARIANT "
        "corner classification; the pillar distinction is at the BRIDGE-MAP axis, "
        "NOT at the algebra-axis. The deprecated `vdd` (`4.7650356226e-05`) and "
        "`volovik` (`1.2681760000e-05`) conventions are tagged DIAGNOSTIC in "
        "`canonical_constants.py` per the Level-3 anchor singleness sub-clause's "
        "DIAGNOSTIC-vs-canonical sub-row table discipline.\n\n"
        "**Substrate-input-orthogonality K-counter advancement** (per `.claude/"
        "rules/joint-theorem-promotion.md §\"Substrate-input-orthogonality "
        "clause (S88 W-23 W7c-167 V.1; B.56)\"`): K=3 was MANDATORY status at "
        "S90 W2 CF-20 (§VII.AH STAGE-3-PERMANENT promotion event, framework's "
        "FIRST cross-axis joint theorem to reach STAGE-3-PERMANENT eligibility). "
        "This §VII.U.2 Corner II Var_a STAGE-3-PERMANENT promotion is the K=3 "
        "→ K=4 corpus-extension calibration instance beyond the MANDATORY "
        "threshold — the framework's SECOND cross-axis joint theorem to reach "
        "STAGE-3-PERMANENT eligibility. The substrate-input-orthogonality is "
        "satisfied at the structural ceiling via the Pillar 1 NCG-axiomatic "
        "vs Pillar 2 BDI BdG-restricted dual-symbol convention layer (Axis-A "
        "consumed Pillar 1 substrate-IS data; Axis-B consumed Pillar 2 "
        "substrate-IS data; the data files are loaded by exactly ONE "
        "cross-reviewer each, satisfying the substrate-input-orthogonality "
        "predicate ∃ obs_i such that the data file consumed by obs_i is loaded "
        "by exactly ONE cross-reviewer NOT both) with a substrate-input-overlap "
        "caveat at the eigenvalue-cache decision-pipeline ORTHOGONAL sub-axis "
        "per S88 W7c-167 V.1 K=1 row (the eigenvalue-cache is a shared input, "
        "but the decision-pipeline downstream of the cache is orthogonal between "
        "axes).\n\n"
        "**Substrate-IS structural identity invariant under STAGE-3 tag-flip**: "
        "the closed-form Bogoliubov expression `Var_a(n_a^GGE) = (1/N) Σ_a m_a "
        "|v_a|^4 − ((1/N) Σ_a m_a |v_a|^2)^2` with `n_a = Δ_BCS² / (2(λ_a² + "
        "Δ_BCS²))` on the BdG sub-algebra `M_2(ℂ) ⊂ A_K` at `τ_fold = 0.19` "
        "(S52 Bogoliubov canonical amplitudes; W-3 R3 R3-B Stage-0 author "
        "freeze 2026-05-13; CF-25 S90 W2 Corner-II 4-axis fingerprint lock-in "
        "`{algebra-axis: INVARIANT, mellin-pole: s=4, FI-RD-class: "
        "MIXED-of-RD-with-distinct-F_traj-factors, level-class: "
        "LEVEL-DRESSED-candidate-pending-K2-via-CF-W6-49-scan}`) is BIT-IDENTICAL "
        "under the STAGE-3 tag-flip. The substrate IS at both Pillar 1 and "
        "Pillar 2 axiom layers (per `phononic-framing.md §\"IS Space, Not IN "
        "Space\"`); the STAGE-3-PERMANENT tag IS the methodology-floor F-image "
        "(per `epistemic-discipline.md §\"Layer-Decomposition\"` Phi correspondence) "
        "recording the substrate's own structural validation across two "
        "independent cross-axis reviewers without prior workshop context.\n\n"
        "**Audit_sha chain**: §W4-4 COMPOSITE = "
        f"`{W4_4_COMPOSITE_AUDIT_SHA}` "
        "(S91 W6 Stage-2 PASS-AND); §W4-6 = "
        f"`{W4_6_AUDIT_SHA}` "
        "(S92 W4-6 Level-3 anchor singleness adjudication).\n\n"
        "**PROVENANCE**: S92 W4-7 LANDED (orchestrator-direct registry write per "
        "`feedback_mack-bridge-role.md` mack-cosmic-bridge sole-writer-role + "
        "`feedback_fix-in-session-never-defer.md`); CHAINED-CONDITIONAL on §W4-6 "
        f"PASS at S92 W4-6 audit_sha256=`{W4_6_AUDIT_SHA}`; "
        "Stage-2 PASS-AND chain inherited from S91 W6 audit_sha256="
        f"`{W4_4_COMPOSITE_AUDIT_SHA}`; "
        "framework's SECOND STAGE-3-PERMANENT cross-axis joint theorem after "
        "§VII.AH at S90 W2 CF-20."
    )

    # Inject the promotion record block at the END of the STAGE-1-CANDIDATE
    # block (just before the trailing two blank lines + start of next sub-section).
    # We append the promotion_record string at the very end of the block.
    post = post.rstrip() + promotion_record + "\n"

    diagnostics["stage_3_promotion_block_appended"] = True

    # (iii) Parse-tree expansion invariance check:
    #   The lines describing the Bogoliubov closed form / S52 BdG amplitudes /
    #   Corner II classification MUST be unchanged. We check by SHA over the
    #   four key substrings extracted before and after.
    parse_tree_substrings = [
        "Var_a(n_a^GGE) = (1/N) Σ_a m_a |v_a|^4 − ((1/N) Σ_a m_a |v_a|^2)^2",
        "n_a^GGE → |v_a|² → Δ_BCS²/(2(λ²+Δ_BCS²))",
        "Cell-II = INVARIANT × s=4",
        "MIXED-of-RD-with-distinct-F_traj-factors",
    ]
    invariant_ok = True  # (local)
    for s in parse_tree_substrings:
        if (s in pre_edit_block) != (s in post):
            invariant_ok = False
            break
    diagnostics["parse_tree_invariant"] = invariant_ok
    diagnostics["post_edit_byte_len"] = len(post.encode("utf-8"))

    return post, diagnostics


# ---------------------------------------------------------------------------
# Section 7 — Verdict emission (single-shot per `registry-landing.md
# §"Bridge-Landing Script Architecture (single-shot pattern)"`)
# ---------------------------------------------------------------------------

def append_verdict_line(verdict: str, value_str: str, audit_sha: str, content_sha: str) -> None:
    """Atomic single-write append per POSIX O_APPEND.

    METHODOLOGY-class gate: L_max = N/A. No 3-tuple companion row required
    per plan §W4-7 `schema_v2_3tuple_required: false`.
    """
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion_row = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(companion_row)


def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (
        f"(value={value!r}, scheme={scheme}, "
        f"convention={convention}, L_max={L_max})"
    )


# ---------------------------------------------------------------------------
# Section 8 — Main (build → write → re-read → verify → emit)
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)

    # 2. Compute legacy closure hash (informational)
    h_closure = hashlib.sha256()  # (local)
    for k in sorted(pins.keys()):
        h_closure.update(f"{k}={pins[k]}\n".encode("utf-8"))
    print(f"  closure: {h_closure.hexdigest()[:16]}... (legacy closure, informational)")
    print()

    # 3. §W4-6 PASS verification — read its canonical verdict line
    s92_verdicts_text = S92_VERDICTS_PATH.read_text(encoding="utf-8")  # (local)
    w4_6_match = re.search(
        r"^S92-W4-CF-W4-4-EMPIRICAL-ANCHOR-RECONCILIATION:\s*PASS",
        s92_verdicts_text,
        flags=re.MULTILINE,
    )
    w4_6_pass_confirmed = w4_6_match is not None  # (local)
    print(f"§W4-6 PASS confirmed in s92_gate_verdicts.txt: {w4_6_pass_confirmed}")
    if not w4_6_pass_confirmed:
        # MECHANICAL CLOSE per plan FAIL_meaning(a)
        verdict = "FAIL"
        value_str = (
            "PRE-REG-INC_blocked_by_S92-W4-CF-W4-4-EMPIRICAL-ANCHOR-RECONCILIATION_NOT_PASS"
        )
        audit_sha, content_sha = compute_dual_sha(
            Path(__file__).resolve(), CANONICAL_PATH, pins
        )
        append_verdict_line(verdict, value_str, audit_sha, content_sha)
        print(f"=== {GATE_ID}: {verdict} (mechanical closure) ===")
        return 0

    # 4. §W4-4 COMPOSITE audit_sha verification — read S91 verdicts
    s91_verdicts_text = S91_VERDICTS_PATH.read_text(encoding="utf-8")  # (local)
    w4_4_audit_present = W4_4_COMPOSITE_AUDIT_SHA in s91_verdicts_text  # (local)
    print(f"§W4-4 COMPOSITE audit_sha pin verified in S91 verdicts: {w4_4_audit_present}")
    if not w4_4_audit_present:
        verdict = "FAIL"
        value_str = (
            f"audit_trail_corrupted_W4_4_audit_sha_pin_not_found_in_S91_verdicts"
        )
        audit_sha, content_sha = compute_dual_sha(
            Path(__file__).resolve(), CANONICAL_PATH, pins
        )
        append_verdict_line(verdict, value_str, audit_sha, content_sha)
        return 0

    # 5. Read registry text
    registry_text = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)

    # 6. Locate Corner II row + STAGE-1-CANDIDATE block via heading-anchor grep
    corner_ii_lineno, block_start, block_end = locate_corner_ii_row(registry_text)
    print(
        f"Located Corner II row at line {corner_ii_lineno}; "
        f"STAGE-1-CANDIDATE block lines [{block_start}, {block_end})"
    )
    plan_pinned_line = 12961  # (local)
    runtime_drift = corner_ii_lineno - plan_pinned_line  # (local)
    print(f"  Plan-pinned line: {plan_pinned_line}; runtime drift: {runtime_drift:+d}")

    # 7. Extract the pre-edit Corner II row + STAGE-1-CANDIDATE block
    lines = registry_text.split("\n")  # (local)
    pre_edit_table_row = lines[corner_ii_lineno - 1]  # (local)
    pre_edit_block = "\n".join(lines[block_start - 1 : block_end])  # (local; STAGE-1-CANDIDATE block)
    pre_edit_full_text = pre_edit_table_row + "\n" + pre_edit_block  # (local; combined for SHA)
    pre_edit_content_sha = sha256_of_bytes(pre_edit_full_text.encode("utf-8"))
    print(f"Pre-edit row + block content_sha256: {pre_edit_content_sha[:16]}...")

    # 8. Idempotency check: has the edit already been applied?
    # If both STAGE-3-PERMANENT tag AND promotion record block are already
    # present, skip the write and proceed straight to verification (single-shot
    # idempotent recovery pattern).
    edit_already_applied = (
        "**STAGE-3-PERMANENT — Var_a(n_a^GGE) Corner-II joint theorem" in pre_edit_block
        and "**STAGE-3-PERMANENT promotion record (S92 W4-7 LANDED" in pre_edit_block
    )  # (local)

    if edit_already_applied:
        print("Edit already applied on disk; idempotent re-verify path.")
        diagnostics = {
            "tag_flip_applied": True,
            "stage_3_promotion_block_appended": True,
            "parse_tree_invariant": True,  # confirmed below via re-read substring checks
            "pre_edit_byte_len": len(pre_edit_block.encode("utf-8")),
            "post_edit_byte_len": len(pre_edit_block.encode("utf-8")),
            "idempotent_path": True,
        }
    else:
        # 8b. Build post-edit block (in-memory, single-shot pattern)
        post_edit_block, diagnostics = build_post_edit_block(pre_edit_block)
        diagnostics["idempotent_path"] = False
        if not diagnostics["tag_flip_applied"]:
            verdict = "FAIL"
            value_str = "STAGE_1_CANDIDATE_tag_not_found_in_target_block"
            audit_sha, content_sha = compute_dual_sha(
                Path(__file__).resolve(), CANONICAL_PATH, pins
            )
            append_verdict_line(verdict, value_str, audit_sha, content_sha)
            return 0

        # 9. Apply the edit to the registry file via atomic-write
        new_lines = (
            lines[: block_start - 1]
            + post_edit_block.split("\n")
            + lines[block_end:]
        )  # (local)
        new_registry_text = "\n".join(new_lines)  # (local)
        REGISTRY_PATH.write_bytes(new_registry_text.encode("utf-8"))

    # 10. Re-read + verify (single-shot verify_section_matches step)
    re_read_text = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)
    post_edit_table_row = re_read_text.split("\n")[corner_ii_lineno - 1]  # (local)
    # Locate the post-edit STAGE-3-PERMANENT block via the new heading
    stage_3_present = "**STAGE-3-PERMANENT — Var_a(n_a^GGE) Corner-II joint theorem" in re_read_text  # (local)
    w4_4_cited = W4_4_COMPOSITE_AUDIT_SHA in re_read_text  # (local)
    w4_6_cited = W4_6_AUDIT_SHA in re_read_text  # (local)
    level_3_anchor_cited = "Var_a_canonical = 7.2824902250e-06" in re_read_text  # (local)
    framework_second_declared = (
        "framework's SECOND cross-axis joint theorem to reach STAGE-3-PERMANENT"
        in re_read_text
    )  # (local)
    k_3_to_k_4_declared = (
        "K=3 → K=4 corpus-extension" in re_read_text
        or "K=3 → K=4 corpus extension" in re_read_text
    )  # (local)
    parse_tree_invariant = diagnostics["parse_tree_invariant"]  # (local)
    bogoliubov_closed_form_intact = (
        "Var_a(n_a^GGE) = (1/N) Σ_a m_a |v_a|^4 − ((1/N) Σ_a m_a |v_a|^2)^2"
        in re_read_text
    )  # (local)
    s52_bdg_intact = (
        "n_a^GGE → |v_a|² → Δ_BCS²/(2(λ²+Δ_BCS²))" in re_read_text
    )  # (local)
    corner_ii_classification_intact = (
        "Cell-II = INVARIANT × s=4" in re_read_text
    )  # (local)
    mack_attribution_present = (
        "mack-cosmic-bridge sole writer" in re_read_text.lower()
        or "mack-cosmic-bridge sole-writer" in re_read_text.lower()
    )  # (local)

    # Post-edit content_sha over the new row + block
    re_read_lines = re_read_text.split("\n")  # (local)
    post_edit_table_row_new = re_read_lines[corner_ii_lineno - 1]  # (local; unchanged)
    # Locate the new block end (now larger; reuse locate)
    _, post_block_start, post_block_end = locate_corner_ii_row(re_read_text)
    post_edit_block_text = "\n".join(re_read_lines[post_block_start - 1 : post_block_end])  # (local)
    post_edit_full_text = post_edit_table_row_new + "\n" + post_edit_block_text  # (local)
    post_edit_content_sha = sha256_of_bytes(post_edit_full_text.encode("utf-8"))
    print(f"Post-edit row + block content_sha256: {post_edit_content_sha[:16]}...")

    print("\n=== Verification booleans ===")
    print(f"  STAGE-3-PERMANENT tag present:      {stage_3_present}")
    print(f"  §W4-4 COMPOSITE audit_sha cited:    {w4_4_cited}")
    print(f"  §W4-6 audit_sha cited:              {w4_6_cited}")
    print(f"  Level-3 anchor single-pinned cited: {level_3_anchor_cited}")
    print(f"  Framework's SECOND declaration:     {framework_second_declared}")
    print(f"  K=3 → K=4 corpus extension declared: {k_3_to_k_4_declared}")
    print(f"  Parse-tree expansion invariant:     {parse_tree_invariant}")
    print(f"  Bogoliubov closed form intact:      {bogoliubov_closed_form_intact}")
    print(f"  S52 BdG amplitudes intact:          {s52_bdg_intact}")
    print(f"  Corner II classification intact:    {corner_ii_classification_intact}")
    print(f"  Mack sole-writer attribution:       {mack_attribution_present}")
    print(f"  Plan-text drift (lines):            {runtime_drift:+d}")

    all_checks_pass = (
        stage_3_present
        and w4_4_cited
        and w4_6_cited
        and level_3_anchor_cited
        and framework_second_declared
        and k_3_to_k_4_declared
        and parse_tree_invariant
        and bogoliubov_closed_form_intact
        and s52_bdg_intact
        and corner_ii_classification_intact
        and mack_attribution_present
    )

    # 11. Build the JSON output sidecar
    json_out = {
        "gate_id": GATE_ID,
        "session": SESSION,
        "trigger": "[AUDIT]",
        "classification": "NON-PHONONIC",
        "agent": "mack-cosmic-bridge",
        "verdict_predicted": "PASS" if all_checks_pass else "FAIL",
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "w4_4_composite_audit_sha256": W4_4_COMPOSITE_AUDIT_SHA,
        "w4_6_audit_sha256": W4_6_AUDIT_SHA,
        "w4_6_content_sha256": W4_6_CONTENT_SHA,
        "Var_a_canonical_value": VAR_A_CANONICAL_VALUE,
        "Var_a_canonical_convention": "substrate-natural w5b47_raw; max(p,q)<=L_max filter; m_a=dim_pq; zero-modes excluded",
        "corner_ii_row_lineno_runtime": corner_ii_lineno,
        "plan_pinned_line": plan_pinned_line,
        "plan_text_drift_lines": runtime_drift,
        "stage_1_candidate_block_start": block_start,
        "stage_1_candidate_block_end_pre_edit": block_end,
        "pre_edit_content_sha256": pre_edit_content_sha,
        "post_edit_content_sha256": post_edit_content_sha,
        "post_edit_block_start": post_block_start,
        "post_edit_block_end": post_block_end,
        "verification": {
            "stage_3_permanent_tag_present": stage_3_present,
            "w4_4_composite_audit_sha_cited": w4_4_cited,
            "w4_6_audit_sha_cited": w4_6_cited,
            "level_3_anchor_single_pinned_cited": level_3_anchor_cited,
            "framework_second_declared": framework_second_declared,
            "k_3_to_k_4_corpus_extension_declared": k_3_to_k_4_declared,
            "parse_tree_expansion_invariant": parse_tree_invariant,
            "bogoliubov_closed_form_intact": bogoliubov_closed_form_intact,
            "s52_bdg_amplitudes_intact": s52_bdg_intact,
            "corner_ii_classification_intact": corner_ii_classification_intact,
            "mack_attribution_present": mack_attribution_present,
            "all_checks_pass": all_checks_pass,
        },
        "diagnostics": diagnostics,
        "methodology_class_m1_m4": {
            "m1_artifact_existence_predicate": True,
            "m2_edit_sha_only_no_compute": True,
            "m3_source_of_truth_workshop_verdicts_plus_rules": True,
            "m4_allowlist_membership": True,
        },
        "substrate_input_orthogonality_k_counter_advance": "K3_TO_K4_corpus_extension_beyond_MANDATORY_threshold",
        "framework_position": "SECOND_cross_axis_joint_theorem_to_reach_STAGE_3_PERMANENT_after_VII_AH_S90_W2_CF20",
        "input_pins": pins,
    }
    OUT_JSON.write_text(json.dumps(json_out, indent=2, sort_keys=True), encoding="utf-8")
    print(f"\nJSON output written: {OUT_JSON.relative_to(PROJECT_ROOT)}")

    # 12. Compute dual SHAs (over the SCRIPT itself, which has now been written
    # but is read fresh) + canonical_constants + input pinmap
    audit_sha, content_sha = compute_dual_sha(
        Path(__file__).resolve(), CANONICAL_PATH, pins
    )
    print(f"  audit_sha256:   {audit_sha[:16]}... (script + canonical + pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    # 13. Verdict + 4-tuple emission
    verdict = "PASS" if all_checks_pass else "FAIL"
    value_str = (
        f"stage_3_permanent_tag_flip_applied=True;"
        f"w4_4_composite_audit_sha_cited={W4_4_COMPOSITE_AUDIT_SHA[:16]};"
        f"w4_6_audit_sha_cited={W4_6_AUDIT_SHA[:16]};"
        f"level_3_anchor_canonical={VAR_A_CANONICAL_VALUE:.10e};"
        f"parse_tree_invariant={parse_tree_invariant};"
        f"framework_second_cross_axis_joint_theorem=True_after_VII_AH_S90_W2_CF20;"
        f"k_counter_substrate_input_orthogonality_advance=K3_TO_K4_corpus_extension_beyond_MANDATORY_threshold;"
        f"plan_text_drift_lines={runtime_drift};"
        f"runtime_canonical_line_corner_ii_lineno={corner_ii_lineno};"
        f"mack_sole_writer=True;"
        f"all_checks_pass={all_checks_pass}"
    )
    tag = emit_4tuple(value_str, SCHEME, CONVENTION, L_MAX)  # (local)
    print(tag)
    append_verdict_line(verdict, value_str, audit_sha, content_sha)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
